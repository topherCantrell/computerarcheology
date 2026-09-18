![Tempest](tempest.jpg)

# Tempest

>>> cpu 6502

>>> binary 9000:roms/136002-133.d1 + roms/136002-134.f1 + roms/136002-235.j1 + roms/136002-136.lm1 + roms/136002-237.p1

>>> memoryTable hard

[Hardware Info](Hardware.md)

>>> memoryTable ram

[RAM Usage](RAMUse.md)

```code
; Tempest (Atari, 1981).
;
; What follows is the code reached from the reset and interrupt entry points,
; shown as instructions; spans never reached appear as data (the "---- data
; ----" blocks).


; ---- $9000-$9008: data ----
9000: 02 BB 5A 30 50 EE 3D A8 4D

; initialize wave state: run the four setup passes $92C5, $9234,
; resetWorkingRamForStateEntry, $A831 in order, then seed 0x5b=0xfa and
; clear 0x106, 0x5f, 0x1.
runWaveInit:
9009: 20 C5 92        JSR     $92C5               ; {code.reseedStateTables} rebuild the per-wave enemy state tables
900C: 20 34 92        JSR     $9234               ; {code.seedPerLaneSpikeArray} lay out this wave's per-lane spikes
900F: 20 2B 90        JSR     $902B               ; {code.resetWorkingRamForStateEntry} clear working RAM for the state being entered
9012: 20 31 A8        JSR     $A831               ; {code.clearReadyLatchPair} drop the paired ready latches
9015: A9 FA           LDA     #$FA                
9017: 85 5B           STA     $5B                 ; {hard.workRam+5B} prime the tube-depth counter high byte to 250
9019: A9 00           LDA     #$00                
901B: 8D 06 01        STA     $0106               ; {hard.workRam+106} clear the moving-spike active flag
901E: 85 5F           STA     $5F                 ; {hard.workRam+5F} clear the tube-depth counter low byte
9020: A9 00           LDA     #$00                
9022: 85 01           STA     $01                 ; {hard.workRam+1} reset the mode-dispatch selector
9024: 60              RTS                         

; level-entry init: run $921B then $92C5, then tail-delegate to the main
; init resetWorkingRamForStateEntry. No own memory write.
runLevelInit:
9025: 20 1B 92        JSR     $921B               ; {code.seedFrameControlTimers} arm the per-frame control timers and plant the blaster's start pose
9028: 20 C5 92        JSR     $92C5               ; {code.reseedStateTables} rebuild the enemy state tables from the record tables

; master state-entry sweep: run the six reset/seed leaves back to back
; ($928F, $926F, $9246, $929F, $92AD, $C16E), then arm loc_124 and loc_148
; to 0xff and clear loc_123.
resetWorkingRamForStateEntry:
902B: 20 8F 92        JSR     $928F               ; {code.clearActiveShots} wipe the active-shot bank
902E: 20 6F 92        JSR     $926F               ; {code.clearShotTableAndStateFlags} clear the per-slot depth table and the enemy population counts
9031: 20 46 92        JSR     $9246               ; {code.seedSlotRandomTags} give each active enemy slot a fresh random tag
9034: 20 9F 92        JSR     $929F               ; {code.clearEightByteTableAndFlag} clear the shape-active table and its object count
9037: 20 AD 92        JSR     $92AD               ; {code.clearByte50} zero the spinner accumulator
903A: 20 6E C1        JSR     $C16E               ; {code.buildLevelLayout} rebuild the level layout
903D: A9 FF           LDA     #$FF                
903F: 8D 24 01        STA     $0124               ; {hard.workRam+124} arm the rim-color animation cursor high
9042: 8D 48 01        STA     $0148               ; {hard.workRam+148} arm the enemy-animation accumulator high
9045: A9 00           LDA     #$00                
9047: 8D 23 01        STA     $0123               ; {hard.workRam+123} clear the spiked-segment count
904A: 60              RTS                         

; feed the rim-rotation update from a fixed-stride position accumulator:
; set floor loc_202=0x10, sign-extend delta loc_121 across loc_29/2a/2b
; (asr twice), fold into the 24-bit total loc_122/68/69, step the 16-bit
; position loc_5f/loc_5b by stride 0x18 (arm loc_115 at loc_5b>=0xfc), and
; on a collapsed high difference against loc_5d rebuild the seeds, set
; mode loc_0 (0x04/0x08 by loc_5 sign) and clear loc_102[loc_3d]; marks
; loc_114=0xff and continues into rotateBlasterAroundRim.
autoAdvanceRimRotation:
904B: A9 10           LDA     #$10                
904D: 8D 02 02        STA     $0202               ; {hard.workRam+202} set the player-shot depth to the near/rim end
9050: A9 00           LDA     #$00                
9052: 85 29           STA     $29                 ; {hard.workRam+29}
9054: 85 2B           STA     $2B                 ; {hard.workRam+2B}
9056: AD 21 01        LDA     $0121               ; {hard.workRam+121} read the level's signed tube-geometry scale delta
9059: 85 2A           STA     $2A                 ; {hard.workRam+2A}
905B: 10 02           BPL     $905F               ; {code.loc_905f}
905D: C6 2B           DEC     $2B                 ; {hard.workRam+2B} sign-extend the delta when negative

loc_905f:
905F: A2 01           LDX     #$01                

loc_9061:
9061: A5 2A           LDA     $2A                 ; {hard.workRam+2A}
9063: 0A              ASL     A                   
9064: 66 2A           ROR     $2A                 ; {hard.workRam+2A}
9066: 66 29           ROR     $29                 ; {hard.workRam+29}
9068: CA              DEX                         
9069: 10 F6           BPL     $9061               ; {code.loc_9061}
906B: A5 29           LDA     $29                 ; {hard.workRam+29}
906D: 18              CLC                         
906E: 6D 22 01        ADC     $0122               ; {hard.workRam+122} fold the scaled delta into the running zoom/position accumulator
9071: 8D 22 01        STA     $0122               ; {hard.workRam+122}
9074: A5 2A           LDA     $2A                 ; {hard.workRam+2A}
9076: 65 68           ADC     $68                 ; {hard.workRam+68} carry it up through the projection-offset low byte
9078: 85 68           STA     $68                 ; {hard.workRam+68}
907A: A5 2B           LDA     $2B                 ; {hard.workRam+2B}
907C: 65 69           ADC     $69                 ; {hard.workRam+69} and the projection-offset high byte
907E: 85 69           STA     $69                 ; {hard.workRam+69}
9080: A5 5F           LDA     $5F                 ; {hard.workRam+5F}
9082: 18              CLC                         
9083: 69 18           ADC     #$18                ; advance the tube-depth position by a fixed stride
9085: 85 5F           STA     $5F                 ; {hard.workRam+5F}
9087: A5 5B           LDA     $5B                 ; {hard.workRam+5B}
9089: 69 00           ADC     #$00                
908B: 85 5B           STA     $5B                 ; {hard.workRam+5B} carry into the depth high byte
908D: C9 FC           CMP     #$FC                
908F: 90 05           BCC     $9096               ; {code.loc_9096}
9091: A9 01           LDA     #$01                
9093: 8D 15 01        STA     $0115               ; {hard.workRam+115} arm the descending-spike table guard once the depth reaches the far limit

loc_9096:
9096: A5 5F           LDA     $5F                 ; {hard.workRam+5F}
9098: 38              SEC                         
9099: E5 5D           SBC     $5D                 ; {hard.workRam+5D} measure the remaining distance to the target depth
909B: A5 5B           LDA     $5B                 ; {hard.workRam+5B}
909D: F0 02           BEQ     $90A1               ; {code.loc_90a1}
909F: E9 FF           SBC     #$FF                

loc_90a1:
90A1: D0 19           BNE     $90BC               ; {code.loc_90bc} skip the snap until the depth window collapses
90A3: A5 5D           LDA     $5D                 ; {hard.workRam+5D}
90A5: 85 5F           STA     $5F                 ; {hard.workRam+5F} snap the position onto the target depth
90A7: A9 FF           LDA     #$FF                
90A9: 85 5B           STA     $5B                 ; {hard.workRam+5B}
90AB: A9 04           LDA     #$04                
90AD: 24 05           BIT     $05                 ; {hard.workRam+5} pick the next game mode by the play/active state bit
90AF: 30 02           BMI     $90B3               ; {code.loc_90b3}
90B1: A9 08           LDA     #$08                

loc_90b3:
90B3: 85 00           STA     $00                 ; {hard.workRam} commit the chosen game mode
90B5: A6 3D           LDX     $3D                 ; {hard.workRam+3D}
90B7: A9 00           LDA     #$00                
90B9: 9D 02 01        STA     $0102,X             ; {hard.workRam+102} clear the active seat's cell

loc_90bc:
90BC: A9 FF           LDA     #$FF                
90BE: 8D 14 01        STA     $0114               ; {hard.workRam+114} flag the frame dirty for redraw
90C1: 4C 49 97        JMP     $9749               ; {code.rotateBlasterAroundRim} place the blaster on the now-advanced rim

; choose the wave's start slot: scan threshold table 0x91fe downward for
; the highest slot at or below seed 0x126, clamp up against a floor
; derived from wave state (0x16a/0x71d/0x9), publish the floor in 0x29 and
; the start index in 0x127, then fall into reseedWaveWorkingSet.
selectWaveStartSlot:
90C4: AD 26 01        LDA     $0126               ; {hard.workRam+126} read the wave start-slot seed
90C7: A2 1C           LDX     #$1C                

loc_90c9:
90C9: CA              DEX                         
90CA: DD FE 91        CMP     $91FE,X             ; {hard.rom+1FE} scan the slot-threshold table for the deepest slot at or below the seed
90CD: 90 FA           BCC     $90C9               ; {code.loc_90c9}
90CF: A0 04           LDY     #$04                ; start the depth floor at 4
90D1: AD 6A 01        LDA     $016A               ; {hard.workRam+16A}
90D4: 29 04           AND     #$04                ; test the difficulty switch that ratchets the start deeper
90D6: F0 12           BEQ     $90EA               ; {code.loc_90ea}
90D8: AD 1D 07        LDA     $071D               ; {hard.workRam+71D} read the current wave number
90DB: C9 30           CMP     #$30                
90DD: 90 01           BCC     $90E0               ; {code.loc_90e0}
90DF: C8              INY                         ; push the floor one deeper past wave 48

loc_90e0:
90E0: C9 50           CMP     #$50                
90E2: 90 01           BCC     $90E5               ; {code.loc_90e5}
90E4: C8              INY                         ; again past wave 80

loc_90e5:
90E5: C9 70           CMP     #$70                
90E7: 90 01           BCC     $90EA               ; {code.loc_90ea}
90E9: C8              INY                         ; again past wave 112

loc_90ea:
90EA: A5 09           LDA     $09                 ; {hard.workRam+9}
90EC: 29 43           AND     #$43                ; test the cabinet configuration for the deep-start override
90EE: C9 40           CMP     #$40                
90F0: D0 02           BNE     $90F4               ; {code.loc_90f4}
90F2: A0 1B           LDY     #$1B                ; force the start floor to 27

loc_90f4:
90F4: 84 29           STY     $29                 ; {hard.workRam+29} publish the depth floor
90F6: E4 29           CPX     $29                 ; {hard.workRam+29}
90F8: B0 02           BCS     $90FC               ; {code.loc_90fc}
90FA: A6 29           LDX     $29                 ; {hard.workRam+29} clamp the start slot up to the floor

loc_90fc:
90FC: 8E 27 01        STX     $0127               ; {hard.workRam+127} store the wave start-depth ceiling
90FF: A5 05           LDA     $05                 ; {hard.workRam+5}
9101: 10 05           BPL     $9108               ; {code.reseedWaveWorkingSet}
9103: A9 00           LDA     #$00                
9105: 8D 26 01        STA     $0126               ; {hard.workRam+126} retire the seed so it does not carry into the next wave

; reseed the wave working set: latch 0x3d from 0x3f (running
; swapParallelTables when nonzero), seed 0x7c/0x5b/0x200/0x51/0x7b/0x605,
; and on the 0x5 sign flag prime the intro cells
; (0x605/0x111/0x00/0x1/0x9f via unpackLevelNibbleTables), write 0x4, then
; fall into tickWaveSpawnCadence.
reseedWaveWorkingSet:
9108: A6 3F           LDX     $3F                 ; {hard.workRam+3F} latch the active level seat from the current level id
910A: 86 3D           STX     $3D                 ; {hard.workRam+3D}
910C: F0 03           BEQ     $9111               ; {code.loc_9111}
910E: 20 B2 92        JSR     $92B2               ; {code.swapParallelTables} swap in the level's parallel lane tables

loc_9111:
9111: A9 04           LDA     #$04                
9113: 85 7C           STA     $7C                 ; {hard.workRam+7C} seed the spread coordinate
9115: A9 FF           LDA     #$FF                
9117: 85 5B           STA     $5B                 ; {hard.workRam+5B} set the tube-depth high byte to the far end
9119: A9 00           LDA     #$00                
911B: 8D 00 02        STA     $0200               ; {hard.workRam+200} reset the player's rim segment
911E: 85 51           STA     $51                 ; {hard.workRam+51} clear the rim rotation offset
9120: 85 7B           STA     $7B                 ; {hard.workRam+7B} clear the spread coordinate low byte
9122: 8D 05 06        STA     $0605               ; {hard.workRam+605} clear the pass counter
9125: A6 05           LDX     $05                 ; {hard.workRam+5}
9127: 10 1B           BPL     $9144               ; {code.loc_9144} branch unless this is a level intro
9129: A9 14           LDA     #$14                
912B: 8D 05 06        STA     $0605               ; {hard.workRam+605} arm the intro pass counter to 20
912E: A9 FF           LDA     #$FF                
9130: 8D 11 01        STA     $0111               ; {hard.workRam+111} raise the tube-geometry flag
9133: A9 16           LDA     #$16                
9135: 85 00           STA     $00                 ; {hard.workRam} enter the level-intro mode
9137: A9 08           LDA     #$08                
9139: 85 01           STA     $01                 ; {hard.workRam+1} set the mode-dispatch selector
913B: A9 00           LDA     #$00                
913D: 85 9F           STA     $9F                 ; {hard.workRam+9F} clear the wave-progress index
913F: 20 96 C1        JSR     $C196               ; {code.unpackLevelNibbleTables} unpack the level nibble tables
9142: A9 10           LDA     #$10                

loc_9144:
9144: 85 04           STA     $04                 ; {hard.workRam+4} store the mode-delay timer
9146: 20 AD 92        JSR     $92AD               ; {code.clearByte50} zero the spinner accumulator

; tick the wave spawn cadence: decrement frame counter 0x605, on underflow
; BCD-count-down the phase 0x4 and reload; when the 0x4e phase gate
; passes, release one entry (index 0x91fe, seed 0x102/0x46/0x9f, run the
; spawn chain unpackLevelNibbleTables/reseedStateTables/seedPerLaneSpikeAr
; ray/clearReadyLatchPair/clearByte50), then trim 0x4e to its low 3 bits.
tickWaveSpawnCadence:
9149: CE 05 06        DEC     $0605               ; {hard.workRam+605} tick down the frame counter and act only on underflow
914C: 10 1B           BPL     $9169               ; {code.loc_9169}
914E: F8              SED                         
914F: A5 04           LDA     $04                 ; {hard.workRam+4}
9151: 38              SEC                         
9152: E9 01           SBC     #$01                ; decimal-decrement the intro/spawn phase
9154: 85 04           STA     $04                 ; {hard.workRam+4}
9156: D8              CLD                         
9157: 10 04           BPL     $915D               ; {code.loc_915d}
9159: A9 10           LDA     #$10                
915B: 85 4E           STA     $4E                 ; {hard.workRam+4E} on phase underflow set the spawn gate bit

loc_915d:
915D: C9 03           CMP     #$03                
915F: D0 03           BNE     $9164               ; {code.loc_9164}
9161: 20 FE CC        JSR     $CCFE               ; {code.requestLevelIntroSound} at phase 3 cue the level-intro sound

loc_9164:
9164: A9 14           LDA     #$14                
9166: 8D 05 06        STA     $0605               ; {hard.workRam+605} reload the frame counter to 20

loc_9169:
9169: 20 AB B0        JSR     $B0AB               ; {code.nudgeBlasterRimPosition} nudge the blaster's rim position
916C: A9 18           LDA     #$18                ; pick the spawn edge mask by phase
916E: A4 04           LDY     $04                 ; {hard.workRam+4}
9170: C0 08           CPY     #$08                
9172: B0 02           BCS     $9176               ; {code.loc_9176}
9174: A9 78           LDA     #$78                

loc_9176:
9176: 25 4E           AND     $4E                 ; {hard.workRam+4E}
9178: F0 34           BEQ     $91AE               ; {code.loc_91ae} spawn only if a masked edge flag is set
917A: A9 00           LDA     #$00                
917C: 85 4E           STA     $4E                 ; {hard.workRam+4E} clear the edge flags
917E: AD 00 02        LDA     $0200               ; {hard.workRam+200} read the player's rim segment
9181: A8              TAY                         
9182: A6 3D           LDX     $3D                 ; {hard.workRam+3D}
9184: 9D 02 01        STA     $0102,X             ; {hard.workRam+102} record the player segment against the active seat
9187: B9 FE 91        LDA     $91FE,Y             ; {hard.rom+1FE} take the start slot from the threshold table by segment
918A: 24 05           BIT     $05                 ; {hard.workRam+5}
918C: 30 09           BMI     $9197               ; {code.loc_9197} off the play-state sign take a random slot instead
918E: A0 01           LDY     #$01                
9190: 84 48           STY     $48                 ; {hard.workRam+48} mark the slot countdown
9192: AD CA 60        LDA     $60CA               ; {hard.pokey1+A}
9195: 29 07           AND     #$07                ; pull a random 0..7 from the POKEY RNG

loc_9197:
9197: 95 46           STA     $46,X               ; {hard.workRam+46} store the chosen slot into the per-slot level table
9199: 85 9F           STA     $9F                 ; {hard.workRam+9F} and into the wave-progress index
919B: 20 96 C1        JSR     $C196               ; {code.unpackLevelNibbleTables} unpack the level nibble tables
919E: 20 C5 92        JSR     $92C5               ; {code.reseedStateTables} rebuild the enemy state tables
91A1: 20 34 92        JSR     $9234               ; {code.seedPerLaneSpikeArray} lay out the per-lane spikes
91A4: 20 31 A8        JSR     $A831               ; {code.clearReadyLatchPair} drop the paired ready latches
91A7: A9 02           LDA     #$02                
91A9: 85 00           STA     $00                 ; {hard.workRam} set the active-play game mode
91AB: 20 AD 92        JSR     $92AD               ; {code.clearByte50} zero the spinner accumulator

loc_91ae:
91AE: A5 4E           LDA     $4E                 ; {hard.workRam+4E}
91B0: 29 07           AND     #$07                ; keep only the low 3 edge bits for the next frame
91B2: 85 4E           STA     $4E                 ; {hard.workRam+4E}
91B4: 60              RTS                         

; seat the in-page working pointer 0x2a/0x2b: double the selector into a
; word index, clear paired flag byte 0x29, and copy the little-endian
; pointer from ROM table 0x91c6/0x91c7 at that index.
seatInPagePointer:
91B5: 0A              ASL     A                   ; double the selector into a two-byte table offset
91B6: AA              TAX                         
91B7: A9 00           LDA     #$00                
91B9: 85 29           STA     $29                 ; {hard.workRam+29} clear the flag byte paired with this pointer
91BB: BD C6 91        LDA     $91C6,X             ; {hard.rom+1C6} copy the selected structure's pointer low byte from the in-page table
91BE: 85 2A           STA     $2A                 ; {hard.workRam+2A}
91C0: BD C7 91        LDA     $91C7,X             ; {hard.rom+1C7} copy its pointer high byte
91C3: 85 2B           STA     $2B                 ; {hard.workRam+2B}
91C5: 60              RTS                         

; ---- $91C6-$921A: data ----
91C6: 00 00 60 00 60 01 20 03 40 05 40 07 40 09 40 11
91D6: 40 13 20 15 00 17 80 18 80 20 60 22 80 24 60 26
91E6: 00 30 00 34 20 38 50 41 90 43 20 47 10 53 10 58
91F6: 40 62 60 65 60 76 80 89 00 02 04 06 08 0A 0C 0E
9206: 10 13 15 17 19 1B 1E 20 23 27 2B 2E 30 33 37 3B
9216: 3E 40 48 50 FF

; init seeder: write fixed startup constants loc_200=0x0e, loc_51=0xf0,
; loc_106=0x00, loc_201=0x0f and loc_202=0x10 (the frame-control byte
; loc_201 and counter loc_202 later drive ageShotsAndAdvanceFrameClock).
seedFrameControlTimers:
921B: A9 0E           LDA     #$0E                
921D: 8D 00 02        STA     $0200               ; {hard.workRam+200} seat the blaster at the starting rim segment
9220: A9 F0           LDA     #$F0                
9222: 85 51           STA     $51                 ; {hard.workRam+51} set the rim fine-rotation offset
9224: A9 00           LDA     #$00                
9226: 8D 06 01        STA     $0106               ; {hard.workRam+106} disarm the moving spike
9229: A9 0F           LDA     #$0F                
922B: 8D 01 02        STA     $0201               ; {hard.workRam+201} set the player's fine rotation angle
922E: A9 10           LDA     #$10                
9230: 8D 02 02        STA     $0202               ; {hard.workRam+202} set the player-shot depth to the rim end
9233: 60              RTS                         

; init seeder: copy header byte loc_15b into loc_3ab, then fill the
; sixteen per-lane cells loc_3ac..loc_3ac+0x0f with the byte read from
; loc_15a.
seedPerLaneSpikeArray:
9234: AD 5B 01        LDA     $015B               ; {hard.workRam+15B} read the wave's initial active-slot count
9237: 8D AB 03        STA     $03AB               ; {hard.workRam+3AB} seat it as the per-lane header count
923A: AD 5A 01        LDA     $015A               ; {hard.workRam+15A} read the per-lane fill constant
923D: A2 0F           LDX     #$0F                

loc_923f:
923F: 9D AC 03        STA     $03AC,X             ; {hard.workRam+3AC} fill all sixteen lane cells with the constant
9242: CA              DEX                         
9243: 10 FA           BPL     $923F               ; {code.loc_923f}
9245: 60              RTS                         

; assign a fresh random tag to each active climber slot: zero the 64-byte
; tag table loc_243+0..0x3f, then for each slot from loc_3ab-1 down write
; a 4-bit POKEY-random $60CA&0x0f into loc_203,x and pack the slot index
; with it into loc_243,x=(x<<4)|nibble, substituting 0x0f when the packed
; tag would be zero.
seedSlotRandomTags:
9246: A9 00           LDA     #$00                
9248: A2 3F           LDX     #$3F                

loc_924a:
924A: 9D 43 02        STA     $0243,X             ; {hard.workRam+243} clear the 64-byte slot tag/record table
924D: CA              DEX                         
924E: 10 FA           BPL     $924A               ; {code.loc_924a}
9250: AE AB 03        LDX     $03AB               ; {hard.workRam+3AB} start at the top active slot
9253: CA              DEX                         

loc_9254:
9254: AD CA 60        LDA     $60CA               ; {hard.pokey1+A} take a 4-bit POKEY random for this slot
9257: 29 0F           AND     #$0F                
9259: 9D 03 02        STA     $0203,X             ; {hard.workRam+203} stash the random nibble in the slot's index cell
925C: 8A              TXA                         
925D: 0A              ASL     A                   ; pack the slot index with its random nibble
925E: 0A              ASL     A                   
925F: 0A              ASL     A                   
9260: 0A              ASL     A                   
9261: 1D 03 02        ORA     $0203,X             ; {hard.workRam+203}
9264: D0 02           BNE     $9268               ; {code.loc_9268}
9266: A9 0F           LDA     #$0F                ; substitute 0x0f so a live slot never carries an all-zero tag

loc_9268:
9268: 9D 43 02        STA     $0243,X             ; {hard.workRam+243} store the packed slot tag
926B: CA              DEX                         
926C: 10 E6           BPL     $9254               ; {code.loc_9254}
926E: 60              RTS                         

; reset leaf: blank the seven shot-depth cells loc_2df..loc_2df+6 top-
; down, then clear seven scattered state flags loc_108, loc_109, loc_145,
; loc_142, loc_144, loc_143 and loc_146.
clearShotTableAndStateFlags:
926F: A2 06           LDX     #$06                
9271: A9 00           LDA     #$00                

loc_9273:
9273: 9D DF 02        STA     $02DF,X             ; {hard.workRam+2DF} clear the seven-cell per-slot depth table
9276: CA              DEX                         
9277: 10 FA           BPL     $9273               ; {code.loc_9273}
9279: 8D 08 01        STA     $0108               ; {hard.workRam+108} clear the total enemy count
927C: 8D 09 01        STA     $0109               ; {hard.workRam+109} clear the enemy-type count
927F: 8D 45 01        STA     $0145               ; {hard.workRam+145} clear the five per-lane enemy counts
9282: 8D 42 01        STA     $0142               ; {hard.workRam+142}
9285: 8D 44 01        STA     $0144               ; {hard.workRam+144}
9288: 8D 43 01        STA     $0143               ; {hard.workRam+143}
928B: 8D 46 01        STA     $0146               ; {hard.workRam+146}
928E: 60              RTS                         

; reset the shot bank: zero the 12-byte depth array loc_2d3 (0x0b..0) and
; both count cells loc_135 and loc_a6 to baseline.
clearActiveShots:
928F: A9 00           LDA     #$00                
9291: A2 0B           LDX     #$0B                

loc_9293:
9293: 9D D3 02        STA     $02D3,X             ; {hard.workRam+2D3} clear the 12-entry per-slot shot-state array
9296: CA              DEX                         
9297: 10 FA           BPL     $9293               ; {code.loc_9293}
9299: 8D 35 01        STA     $0135               ; {hard.workRam+135} clear the active object count
929C: 85 A6           STA     $A6                 ; {hard.workRam+A6} clear the active enemy count
929E: 60              RTS                         

; reset leaf: blank the eight-byte table loc_30a..loc_30a+7 top-down, then
; clear the trailing flag byte loc_116.
clearEightByteTableAndFlag:
929F: A2 07           LDX     #$07                
92A1: A9 00           LDA     #$00                

loc_92a3:
92A3: 9D 0A 03        STA     $030A,X             ; {hard.workRam+30A} clear the eight-cell shape-active table
92A6: CA              DEX                         
92A7: 10 FA           BPL     $92A3               ; {code.loc_92a3}
92A9: 8D 16 01        STA     $0116               ; {hard.workRam+116} clear the timed-object count
92AC: 60              RTS                         

; minimal reset leaf: clear the single state cell loc_50 (a cell that
; ranges 0x00..0xde in play) to zero and return.
clearByte50:
92AD: A9 00           LDA     #$00                
92AF: 85 50           STA     $50                 ; {hard.workRam+50} zero the spinner accumulator
92B1: 60              RTS                         

; swap the two parallel 18-entry tables loc_3aa and loc_3bc slot-for-slot
; (index 0x11 down to 0), so each table ends holding what its sibling
; held.
swapParallelTables:
92B2: A2 11           LDX     #$11                

loc_92b4:
92B4: BD AA 03        LDA     $03AA,X             ; {hard.workRam+3AA} swap the two parallel 18-entry lane tables slot for slot
92B7: BC BC 03        LDY     $03BC,X             ; {hard.workRam+3BC}
92BA: 9D BC 03        STA     $03BC,X             ; {hard.workRam+3BC}
92BD: 98              TYA                         
92BE: 9D AA 03        STA     $03AA,X             ; {hard.workRam+3AA}
92C1: CA              DEX                         
92C2: 10 F0           BPL     $92B4               ; {code.loc_92b4}
92C4: 60              RTS                         

; re-seed game state: build search key loc_2b from loc_9f (or a POKEY-
; random masked value via $60DA when >=98, then +1), walk the 4-byte
; record table at $9604 from record 111 down to 3 loading source ptr
; loc_2c/loc_2d and dest ptr loc_3b/loc_3c per record, scan each source
; list (via dispatchRangeValueBySelector/dispatchCursorAdvanceBySelector)
; for the range bracketing the key and store the resolved byte through the
; dest ptr, rescale loc_160/loc_15b per loc_16a&3, fold
; loc_163/loc_120/loc_160 through partitionByteToFineCoarseSeed, then seed
; many loc_01xx cells plus loc_155/loc_161/loc_166/loc_149/loc_14a.
reseedStateTables:
92C5: A5 9F           LDA     $9F                 ; {hard.workRam+9F} read the wave-progress index as the difficulty key
92C7: C9 62           CMP     #$62                
92C9: 90 07           BCC     $92D2               ; {code.loc_92d2} branch unless the key runs off the top of the tables
92CB: AD DA 60        LDA     $60DA               ; {hard.pokey2+A} substitute a POKEY random key when off the top
92CE: 29 1F           AND     #$1F                
92D0: 09 40           ORA     #$40                

loc_92d2:
92D2: 85 2B           STA     $2B                 ; {hard.workRam+2B} store the difficulty search key
92D4: E6 2B           INC     $2B                 ; {hard.workRam+2B} bump it by one
92D6: A2 6F           LDX     #$6F                
92D8: 86 37           STX     $37                 ; {hard.workRam+37} start the record walk at index 111

loc_92da:
92DA: A6 37           LDX     $37                 ; {hard.workRam+37}
92DC: BD 07 96        LDA     $9607,X             ; {hard.rom+607} read the record's destination pointer high byte
92DF: 85 3C           STA     $3C                 ; {hard.workRam+3C}
92E1: BD 06 96        LDA     $9606,X             ; {hard.rom+606} and its low byte
92E4: 85 3B           STA     $3B                 ; {hard.workRam+3B}
92E6: BD 05 96        LDA     $9605,X             ; {hard.rom+605} read the source-list pointer high byte
92E9: 85 2D           STA     $2D                 ; {hard.workRam+2D}
92EB: BD 04 96        LDA     $9604,X             ; {hard.rom+604} and its low byte
92EE: 85 2C           STA     $2C                 ; {hard.workRam+2C}
92F0: A9 01           LDA     #$01                
92F2: 85 38           STA     $38                 ; {hard.workRam+38} reset the per-record scan cursor
92F4: A0 00           LDY     #$00                

loc_92f6:
92F6: B1 2C           LDA     ($2C),Y             ; {hard.workRam+2C} read the next source-list entry
92F8: 8D 5E 01        STA     $015E               ; {hard.workRam+15E}
92FB: F0 1C           BEQ     $9319               ; {code.loc_9319} end the list on a zero entry
92FD: A5 2B           LDA     $2B                 ; {hard.workRam+2B}
92FF: C8              INY                         
9300: D1 2C           CMP     ($2C),Y             ; {hard.workRam+2C} compare the key against the range low bound
9302: C8              INY                         
9303: 90 0E           BCC     $9313               ; {code.loc_9313}
9305: D1 2C           CMP     ($2C),Y             ; {hard.workRam+2C} compare against the range high bound
9307: D0 01           BNE     $930A               ; {code.loc_930a}
9309: 18              CLC                         

loc_930a:
930A: B0 07           BCS     $9313               ; {code.loc_9313} skip this range if the key is outside it
930C: C8              INY                         
930D: 20 77 96        JSR     $9677               ; {code.dispatchRangeValueBySelector} resolve the value for this destination cell
9310: 4C 19 93        JMP     $9319               ; {code.loc_9319}

loc_9313:
9313: 20 83 96        JSR     $9683               ; {code.dispatchCursorAdvanceBySelector} advance the cursor to the next range
9316: 18              CLC                         
9317: 90 DD           BCC     $92F6               ; {code.loc_92f6}

loc_9319:
9319: A0 00           LDY     #$00                
931B: 91 3B           STA     ($3B),Y             ; {hard.workRam+3B} store the resolved byte through the destination pointer
931D: A5 37           LDA     $37                 ; {hard.workRam+37}
931F: 38              SEC                         
9320: E9 04           SBC     #$04                ; step to the next record, four bytes back
9322: 85 37           STA     $37                 ; {hard.workRam+37}
9324: C9 FF           CMP     #$FF                
9326: D0 B2           BNE     $92DA               ; {code.loc_92da} loop until the record table is exhausted
9328: AD 6A 01        LDA     $016A               ; {hard.workRam+16A}
932B: 29 03           AND     #$03                ; select the enemy-speed rescale by difficulty mode
932D: C9 01           CMP     #$01                
932F: D0 1C           BNE     $934D               ; {code.loc_934d}
9331: CE 1A 01        DEC     $011A               ; {hard.workRam+11A} easy mode: lower the free-flight slot ceiling
9334: AD 60 01        LDA     $0160               ; {hard.workRam+160}
9337: 49 FF           EOR     #$FF                
9339: 4A              LSR     A                   
933A: 4A              LSR     A                   
933B: 4A              LSR     A                   
933C: 6D 60 01        ADC     $0160               ; {hard.workRam+160}
933F: 8D 60 01        STA     $0160               ; {hard.workRam+160} ramp the segment-0 climb speed down
9342: A5 9F           LDA     $9F                 ; {hard.workRam+9F}
9344: C9 11           CMP     #$11                
9346: B0 02           BCS     $934A               ; {code.loc_934a}
9348: C6 B3           DEC     $B3                 ; {hard.workRam+B3} ease the early waves further

loc_934a:
934A: B8              CLV                         
934B: 50 35           BVC     $9382               ; {code.loc_9382}

loc_934d:
934D: C9 02           CMP     #$02                ; hard mode?
934F: D0 31           BNE     $9382               ; {code.loc_9382}
9351: EE 1A 01        INC     $011A               ; {hard.workRam+11A} raise the free-flight slot ceiling
9354: AD 1A 01        LDA     $011A               ; {hard.workRam+11A}
9357: C9 03           CMP     #$03                
9359: 90 05           BCC     $9360               ; {code.loc_9360}
935B: A9 03           LDA     #$03                
935D: 8D 1A 01        STA     $011A               ; {hard.workRam+11A} clamp the ceiling to 3

loc_9360:
9360: AD 60 01        LDA     $0160               ; {hard.workRam+160}
9363: 4A              LSR     A                   
9364: 4A              LSR     A                   
9365: 4A              LSR     A                   
9366: 09 E0           ORA     #$E0                
9368: 6D 60 01        ADC     $0160               ; {hard.workRam+160}
936B: 8D 60 01        STA     $0160               ; {hard.workRam+160} ramp the segment-0 climb speed up
936E: AD 5B 01        LDA     $015B               ; {hard.workRam+15B}
9371: 4A              LSR     A                   
9372: 4A              LSR     A                   
9373: 4A              LSR     A                   
9374: 6D 5B 01        ADC     $015B               ; {hard.workRam+15B}
9377: 8D 5B 01        STA     $015B               ; {hard.workRam+15B} raise the wave's initial active count
937A: AD 6D 01        LDA     $016D               ; {hard.workRam+16D}
937D: 09 40           ORA     #$40                
937F: 8D 6D 01        STA     $016D               ; {hard.workRam+16D} select the hard-mode alternate list set

loc_9382:
9382: AD 63 01        LDA     $0163               ; {hard.workRam+163}
9385: 20 E0 93        JSR     $93E0               ; {code.partitionByteToFineCoarseSeed} fold the segment-3 climb delta into fine and coarse seeds
9388: 8D 63 01        STA     $0163               ; {hard.workRam+163} store the segment-3 climb-delta low byte
938B: 8C 68 01        STY     $0168               ; {hard.workRam+168} store the segment-3 climb-delta high byte
938E: 8E 54 01        STX     $0154               ; {hard.workRam+154} store the segment-3 band threshold
9391: AD 20 01        LDA     $0120               ; {hard.workRam+120}
9394: 20 E0 93        JSR     $93E0               ; {code.partitionByteToFineCoarseSeed} fold the object velocity into fine and coarse seeds
9397: 8D 20 01        STA     $0120               ; {hard.workRam+120} store the object-velocity low byte
939A: 8C 18 01        STY     $0118               ; {hard.workRam+118} store the object-velocity high byte
939D: 86 A7           STX     $A7                 ; {hard.workRam+A7} store the hit-distance threshold
939F: AD 60 01        LDA     $0160               ; {hard.workRam+160}
93A2: 20 E0 93        JSR     $93E0               ; {code.partitionByteToFineCoarseSeed} fold the segment-0 climb delta into fine and coarse seeds
93A5: 8D 60 01        STA     $0160               ; {hard.workRam+160} store the segment-0 climb-delta low byte
93A8: 8D 62 01        STA     $0162               ; {hard.workRam+162} mirror it into the segment-2 climb delta
93AB: 8C 67 01        STY     $0167               ; {hard.workRam+167} store the segment-2 climb-delta high byte
93AE: 8C 65 01        STY     $0165               ; {hard.workRam+165} store the segment-0 climb-delta high byte
93B1: 8E 51 01        STX     $0151               ; {hard.workRam+151} store band threshold 0
93B4: 8E 53 01        STX     $0153               ; {hard.workRam+153} store band threshold 2
93B7: 8E 52 01        STX     $0152               ; {hard.workRam+152} store band threshold 1
93BA: AD 60 01        LDA     $0160               ; {hard.workRam+160}
93BD: 0A              ASL     A                   
93BE: 8D 64 01        STA     $0164               ; {hard.workRam+164} derive the segment-4 climb delta by doubling segment-0
93C1: AD 65 01        LDA     $0165               ; {hard.workRam+165}
93C4: 2A              ROL     A                   
93C5: 8D 69 01        STA     $0169               ; {hard.workRam+169} and its high byte with the carry
93C8: A9 06           LDA     #$06                
93CA: 8D 55 01        STA     $0155               ; {hard.workRam+155} hard-seed band threshold 4
93CD: A9 A0           LDA     #$A0                
93CF: 8D 61 01        STA     $0161               ; {hard.workRam+161} hard-seed the segment-1 climb-delta low byte
93D2: A9 FE           LDA     #$FE                
93D4: 8D 66 01        STA     $0166               ; {hard.workRam+166} and its high byte
93D7: A9 01           LDA     #$01                
93D9: 8D 4A 01        STA     $014A               ; {hard.workRam+14A} seed the first candidate lane
93DC: 8D 49 01        STA     $0149               ; {hard.workRam+149} seed the second candidate lane
93DF: 60              RTS                         

; split one input byte into three derived; used by reseedStateTables to
; fan loc_163/loc_120/loc_160 out into their satellite cells.
partitionByteToFineCoarseSeed:
93E0: A0 FF           LDY     #$FF                ; seed the bit-fold accumulator with 0xff
93E2: 84 29           STY     $29                 ; {hard.workRam+29} hold the running seed in scratch
93E4: 0A              ASL     A                   ; shift the source byte's top bit out
93E5: 26 29           ROL     $29                 ; {hard.workRam+29} fold that top bit into the seed's low end
93E7: 0A              ASL     A                   ; shift the next source bit out
93E8: 26 29           ROL     $29                 ; {hard.workRam+29} fold it into the seed
93EA: 0A              ASL     A                   ; shift the third source bit out
93EB: 26 29           ROL     $29                 ; {hard.workRam+29} fold it into the seed
93ED: A4 29           LDY     $29                 ; {hard.workRam+29} take the finished fine seed into Y
93EF: 48              PHA                         
93F0: 98              TYA                         
93F1: 49 FF           EOR     #$FF                ; complement the seed
93F3: 18              CLC                         
93F4: 69 0D           ADC     #$0D                ; bias the complement by 0x0d
93F6: 4A              LSR     A                   ; halve it to form the coarse index
93F7: AA              TAX                         
93F8: 68              PLA                         
93F9: 60              RTS                         

; ---- $93FA-$9676: data ----
93FA: 08 01 14 50 FD 02 15 40 14 02 41 63 0A 04 01 09
940A: 01 01 01 02 03 02 02 03 03 02 0A 40 02 02 41 63
941A: 03 08 01 08 D4 FB 04 09 10 AF AC AC AC A8 A4 A0
942A: A0 08 11 19 AF FD 08 1A 20 9D FD 08 21 27 94 FD
943A: 08 28 30 92 FF 08 31 40 88 FF 0C 41 63 60 41 0A
944A: 01 63 C0 0A 01 14 00 0A 15 20 D0 0A 21 30 D8 0A
945A: 31 63 D0 02 01 20 A0 02 21 40 A0 02 41 63 C0 02
946A: 01 30 04 02 31 40 06 02 41 63 08 02 01 20 01 02
947A: 21 28 03 02 29 63 02 02 01 30 01 02 31 63 03 04
948A: 01 04 00 00 00 01 02 05 10 02 02 11 13 00 02 14
949A: 20 01 02 23 27 01 02 2C 63 01 00 04 01 06 00 00
94AA: 00 02 03 04 02 07 0A 04 02 0B 10 03 02 14 19 02
94BA: 04 1A 20 01 02 02 02 01 01 02 02 35 27 01 02 2B
94CA: 63 01 00 02 01 04 01 02 05 63 00 00 02 01 04 04
94DA: 02 05 10 05 02 11 13 03 02 14 19 04 02 1A 63 05
94EA: 00 04 01 04 00 00 01 00 02 05 10 01 02 11 20 01
94FA: 02 21 27 01 02 28 63 01 00 04 01 05 00 00 01 00
950A: 01 02 06 10 02 02 11 1A 01 02 1B 20 01 02 21 2C
951A: 02 02 2D 63 03 00 02 11 20 02 02 21 63 01 00 04
952A: 11 20 05 03 02 02 02 02 02 02 02 02 02 02 02 03
953A: 04 02 02 21 63 03 00 02 0B 10 01 02 16 19 01 02
954A: 1B 63 01 00 02 0B 10 01 02 16 19 01 02 1B 20 01
955A: 02 21 27 04 02 28 63 03 00 04 11 12 28 14 0C 13
956A: 20 14 28 08 21 27 14 FF 0C 28 63 14 0A 00 0C 11
957A: 20 00 40 0C 21 30 40 C0 02 31 63 C0 00 02 01 10
958A: DC 02 11 27 C0 08 28 40 C0 01 02 41 63 E6 02 01
959A: 63 06 06 01 63 00 00 00 E0 D8 D4 D0 C8 C0 B8 B0
95AA: A8 A0 A0 A0 A8 A0 9C 9A 98 04 01 10 0A 0C 0F 11
95BA: 14 16 14 18 1B 1D 1B 18 1A 1C 1E 1B 08 11 1A 14
95CA: 01 02 1B 27 1B 08 28 30 1D 01 08 31 40 1F 01 08
95DA: 41 50 23 01 08 51 63 2B 01 02 01 14 02 02 15 20
95EA: 02 02 21 63 03 02 3C 63 40 00 06 01 63 07 0B 19
95FA: 24 53 0B 24 19 53 87 24 19 53 07 87 24 EF 95 6D
960A: 01 E3 95 B3 00 FA 93 19 01 07 94 1A 01 CD 94 29
961A: 01 D6 94 2E 01 20 95 2A 01 29 95 2F 01 EB 94 2B
962A: 01 03 95 30 01 89 94 2C 01 A5 94 31 01 41 95 2D
963A: 01 4E 95 32 01 5D 94 57 01 69 94 47 01 75 94 4B
964A: 01 81 94 4C 01 98 95 1C 01 B3 95 5B 01 9C 95 5A
965A: 01 63 95 B2 00 F4 95 5D 01 4D 94 63 01 49 94 20
966A: 01 1B 94 60 01 78 95 59 01 87 95 5F 01

; resolve the range-bracketed list value: read the even selector byte
; 0x15e, halve it, and tail-call the matching 0x96xx coordinate helper
; ($96C4/96b7/96ab/96e2/96db/9700), returning its byte to $92C5's table
; walk.
dispatchRangeValueBySelector:
9677: AE 5E 01        LDX     $015E               ; {hard.workRam+15E} load the coordinate-value helper selector
967A: BD 90 96        LDA     $9690,X             ; {hard.rom+690} read the chosen helper's return-address high byte
967D: 48              PHA                         
967E: BD 8F 96        LDA     $968F,X             ; {hard.rom+68F} read its low byte
9681: 48              PHA                         
9682: 60              RTS                         ; computed jump into the selected coordinate-value helper

; advance the source-list cursor: use selector 0x15e to pick a cursor-
; advance helper (advanceListCursorByTwo/96cb/96c7) and tail-call it, pre-
; seating A to the selected pointer's low byte for the Y-only handlers.
dispatchCursorAdvanceBySelector:
9683: AE 5E 01        LDX     $015E               ; {hard.workRam+15E} load the cursor-advance helper selector
9686: BD 9E 96        LDA     $969E,X             ; {hard.rom+69E} read the chosen advance helper's high byte
9689: 48              PHA                         
968A: BD 9D 96        LDA     $969D,X             ; {hard.rom+69D} read its low byte
968D: 48              PHA                         
968E: 60              RTS                         ; computed jump into the selected cursor-advance helper

; ---- $968F-$96AA: data ----
968F: 00 00 C3 96 B6 96 AA 96 E1 96 DA 96 FF 96 00 00
969F: C7 96 CA 96 CA 96 C6 96 C7 96 C6 96

; fetch a coordinate-list entry by re-indexing: stash Y at 0x29, form the
; index value ((0x2b-1)&0x0f)+1, subtract the list byte two entries back
; (pointer+(Y-2)), add back the saved Y, re-index the pointer by the
; result, and load and return that entry.
fetchCoordListEntryByCounter:
96AB: A5 2B           LDA     $2B                 ; {hard.workRam+2B} read the list counter
96AD: 38              SEC                         
96AE: E9 01           SBC     #$01                ; counter minus one
96B0: 29 0F           AND     #$0F                ; wrap into the low nibble
96B2: 18              CLC                         
96B3: 69 01           ADC     #$01                ; plus one -- the counter-derived seed
96B5: 10 02           BPL     $96B9               ; {code.loc_96b9} join the shared re-index

; sibling of 0x96ab that uses the raw index 0x2b (not the counter-wrapped
; value): stash Y at 0x29, subtract the list byte two entries back, add
; back saved Y, re-index the pointer, and load and return that entry.
fetchCoordListEntryByIndex:
96B7: A5 2B           LDA     $2B                 ; {hard.workRam+2B} index variant -- seed from the raw counter instead

loc_96b9:
96B9: 84 29           STY     $29                 ; {hard.workRam+29} stash the incoming cursor
96BB: 88              DEY                         ; step back one entry
96BC: 88              DEY                         ; step back a second entry
96BD: 38              SEC                         
96BE: F1 2C           SBC     ($2C),Y             ; {hard.workRam+2C} subtract the stride byte two entries back
96C0: 18              CLC                         
96C1: 65 29           ADC     $29                 ; {hard.workRam+29} add the saved cursor back in
96C3: A8              TAY                         

; the bare coordinate-list read: return the byte at pointer 0x2c offset by
; Y, with no index arithmetic.
readCoordListEntry:
96C4: B1 2C           LDA     ($2C),Y             ; {hard.workRam+2C} load the coordinate-list entry the offset points at
96C6: 60              RTS                         

; cursor-skip helper: advance the list cursor Y by a fixed run to step
; over a packed record without reading it -- the first entry moves Y
; forward by three (bumps by one then falls into the second entry), the
; second entry by two; register only, writes no memory
advanceCursorPastPackedRecord:
96C7: C8              INY                         ; first entry -- advance the cursor by one

; step the list cursor forward past a two-byte record without reading it:
; return Y+2 (register only).
advanceListCursorByTwo:
96C8: C8              INY                         ; advance the cursor two past a packed record
96C9: C8              INY                         
96CA: 60              RTS                         

; walk the packed coordinate list through 0x2c/0x2d: read the entry at Y
; and its predecessor at Y-1, store their difference (cur-prev) at 0x29 as
; the step delta, and advance Y by that delta plus two.
advanceCoordListByEntryStride:
96CB: B1 2C           LDA     ($2C),Y             ; {hard.workRam+2C} read the coordinate entry under the cursor
96CD: 88              DEY                         ; back up to the predecessor entry
96CE: 38              SEC                         
96CF: F1 2C           SBC     ($2C),Y             ; {hard.workRam+2C} subtract it -- the inter-entry stride
96D1: 85 29           STA     $29                 ; {hard.workRam+29} publish the stride delta in scratch
96D3: 98              TYA                         
96D4: 38              SEC                         
96D5: 65 29           ADC     $29                 ; {hard.workRam+29} advance the cursor forward by the stride
96D7: A8              TAY                         
96D8: C8              INY                         ; leave the cursor one past
96D9: C8              INY                         ; leave it two past, ready for the next entry pair
96DA: 60              RTS                         

; resolve one list entry to an absolute coordinate: read the byte at
; pointer 0x2c offset by Y and add the base value in 0x160, returning the
; 8-bit sum in A.
resolveCoordListEntryToAbsolute:
96DB: B1 2C           LDA     ($2C),Y             ; {hard.workRam+2C} read the relative list entry
96DD: 18              CLC                         
96DE: 6D 60 01        ADC     $0160               ; {hard.workRam+160} fold it onto the anchor base for the absolute coordinate
96E1: 60              RTS                         

; fold a run of coordinate-list entries: use 0x96f4 as a repeat count,
; load the first entry at pointer 0x2c offset Y, then add that many
; further consecutive entries into a single wrapped one-byte total.
sumCoordListEntryRun:
96E2: 20 F4 96        JSR     $96F4               ; {code.computeCoordListBackDelta} get the repeat count for this run

; ---- $96E5-$96E5: data ----
96E5: AA
96E6: B1 2C           LDA     ($2C),Y             ; {hard.workRam+2C} seed the total with the first entry
96E8: C8              INY                         ; step to the next entry
96E9: E0 00           CPX     #$00                ; test the count
96EB: F0 06           BEQ     $96F3               ; {code.loc_96f3} nothing to add when the count is zero

loc_96ed:
96ED: 18              CLC                         ; add the next entry into the running total
96EE: 71 2C           ADC     ($2C),Y             ; {hard.workRam+2C}
96F0: CA              DEX                         ; drop the count
96F1: D0 FA           BNE     $96ED               ; {code.loc_96ed} repeat until the run is summed

loc_96f3:
96F3: 60              RTS                         

; compute the coordinate-list index delta: record Y at 0x29 and return
; (0x2b minus the list byte two slots back at pointer+(Y-2)) & 0xff; a
; leaf whose result is consumed downstream.
computeCoordListBackDelta:
96F4: A5 2B           LDA     $2B                 ; {hard.workRam+2B} read the scratch base value
96F6: 84 29           STY     $29                 ; {hard.workRam+29} record the cursor so the caller can recover it
96F8: 88              DEY                         ; step back one slot
96F9: 88              DEY                         ; step back a second slot
96FA: 38              SEC                         
96FB: F1 2C           SBC     ($2C),Y             ; {hard.workRam+2C} base minus the list byte two slots back -- the delta
96FD: C8              INY                         
96FE: C8              INY                         
96FF: 60              RTS                         

; ---- $9700-$9704: data ----
9700: 20 F4 96 29 01
9705: F0 01           BEQ     $9708               ; {code.loc_9708} even delta -- fetch the entry as-is
9707: C8              INY                         ; odd delta -- step one slot forward

loc_9708:
9708: B1 2C           LDA     ($2C),Y             ; {hard.workRam+2C} load the entry the cursor now points at
970A: 60              RTS                         

; run the nine per-frame update passes in fixed order ($9749, $A23F,
; $A83A, $98A2, $9B1E, $A18F, $A2A6, $A454, $A416) then tail-delegate to
; $A504; makes no own role-defining write.
runPerFrameUpdates:
970B: 20 49 97        JSR     $9749               ; {code.rotateBlasterAroundRim} rotate the player's blaster around the rim
970E: 20 3F A2        JSR     $A23F               ; {code.spawnEntityIntoFreeSlot} seat a newly spawned enemy into a free slot
9711: 20 3A A8        JSR     $A83A               ; {code.stepAttractEnemySweepTimer} advance the attract-mode enemy sweep timer
9714: 20 A2 98        JSR     $98A2               ; {code.tickSpawnSlotTimers} count down the per-slot spawn timers
9717: 20 1E 9B        JSR     $9B1E               ; {code.runObjectMotionScripts} run every occupied slot's motion script
971A: 20 8F A1        JSR     $A18F               ; {code.stepActiveShots} advance the active shots
971D: 20 A6 A2        JSR     $A2A6               ; {code.spawnClimbersFromSourceSlots} spawn climbers up the lanes from their source slots
9720: 20 54 A4        JSR     $A454               ; {code.scanAllSlotsForProximity} proximity and collision scan across all slots
9723: 20 16 A4        JSR     $A416               ; {code.ageTimedObjects} age the transient timed objects
9726: 4C 04 A5        JMP     $A504               ; {code.ageShotsAndAdvanceFrameClock} tail into aging shots and ticking the frame clock

; run the per-frame state updaters: clear bit7 of 0x123, run $9749, $97F8,
; $A416, $A23F, $A18F in order, then run the extra updater $A504 only when
; 0x201 is negative.
runFrameStateUpdaters:
9729: AD 23 01        LDA     $0123               ; {hard.workRam+123} read the spiked-segment tally cell
972C: 29 7F           AND     #$7F                ; clear its per-frame high bit, keep the tally
972E: 8D 23 01        STA     $0123               ; {hard.workRam+123} write back the clean count
9731: 20 49 97        JSR     $9749               ; {code.rotateBlasterAroundRim} turn the spinner/aim into the player's new rim angle
9734: 20 F8 97        JSR     $97F8               ; {code.advanceMovingSpike} step the moving spike
9737: 20 16 A4        JSR     $A416               ; {code.ageTimedObjects} age the timed objects
973A: 20 3F A2        JSR     $A23F               ; {code.spawnEntityIntoFreeSlot} seat a new enemy into a free slot
973D: 20 8F A1        JSR     $A18F               ; {code.stepActiveShots} advance the live shots
9740: AD 01 02        LDA     $0201               ; {hard.workRam+201} read the fine-angle rotation-pending flag
9743: 10 03           BPL     $9748               ; {code.loc_9748} skip the extra pass unless its high bit is set
9745: 20 04 A5        JSR     $A504               ; {code.ageShotsAndAdvanceFrameClock} extra pass -- age shots and tick the frame clock

loc_9748:
9748: 60              RTS                         

; advance the rim rotation/spinner state: skip while fine-angle flag
; loc_201 bit7 set; take the delta from manual reading loc_50 (clamped to
; band [0xe1,0x1f], then consumed) when loc_5 bit7 is set else the auto-
; aim from aimSpinnerAtNearestEnemy; fold it into work cells
; loc_2b/loc_2c, and on a live level (loc_111!=0) cap loc_2c to 0xef and
; saturate toward the stored sign on a sign flip; the high nibble becomes
; coarse angle loc_2a, ring sound cueRimRotationSound on a changed coarse
; angle, then commit loc_200/loc_201/loc_51.
rotateBlasterAroundRim:
9749: AD 01 02        LDA     $0201               ; {hard.workRam+201} read the fine-angle rotation-pending flag
974C: 10 01           BPL     $974F               ; {code.loc_974f} proceed only when no rotation is pending
974E: 60              RTS                         ; pending or locked -- do nothing this frame

loc_974f:
974F: A2 00           LDX     #$00                
9751: A5 05           LDA     $05                 ; {hard.workRam+5} read the status flags
9753: 30 06           BMI     $975B               ; {code.loc_975b} manual-play bit set -- take the raw spinner delta
9755: 20 C5 97        JSR     $97C5               ; {code.aimSpinnerAtNearestEnemy} aim mode -- auto-aim delta toward the nearest enemy
9758: B8              CLV                         
9759: 50 15           BVC     $9770               ; {code.loc_9770} join the offset computation

loc_975b:
975B: A5 50           LDA     $50                 ; {hard.workRam+50} manual play -- read the raw spinner delta
975D: 10 09           BPL     $9768               ; {code.loc_9768} positive delta -- go cap it
975F: C9 E1           CMP     #$E1                ; negative delta below the floor
9761: B0 02           BCS     $9765               ; {code.loc_9765}
9763: A9 E1           LDA     #$E1                ; floor the delta at 0xe1

loc_9765:
9765: B8              CLV                         
9766: 50 06           BVC     $976E               ; {code.loc_976e}

loc_9768:
9768: C9 1F           CMP     #$1F                ; positive delta at or below the cap
976A: 90 02           BCC     $976E               ; {code.loc_976e}
976C: A9 1F           LDA     #$1F                ; cap the delta at 0x1f

loc_976e:
976E: 86 50           STX     $50                 ; {hard.workRam+50} consume the spinner reading -- zero it

loc_9770:
9770: 85 2B           STA     $2B                 ; {hard.workRam+2B} stash the chosen turn delta
9772: 49 FF           EOR     #$FF                
9774: 38              SEC                         
9775: 65 51           ADC     $51                 ; {hard.workRam+51} form rim-offset minus the delta
9777: 85 2C           STA     $2C                 ; {hard.workRam+2C} provisional new rim offset
9779: AE 11 01        LDX     $0111               ; {hard.workRam+111} read the live-board tube-geometry flag
977C: F0 1F           BEQ     $979D               ; {code.loc_979d} skip the end-of-rim clamps when no board is live
977E: C9 F0           CMP     #$F0                ; offset short of the top limit
9780: 90 04           BCC     $9786               ; {code.loc_9786}
9782: A9 EF           LDA     #$EF                ; cap the offset to the top lane
9784: 85 2C           STA     $2C                 ; {hard.workRam+2C}

loc_9786:
9786: 45 2B           EOR     $2B                 ; {hard.workRam+2B} compare the offset's sign against the delta
9788: 10 13           BPL     $979D               ; {code.loc_979d} same sign -- no over-rotation, continue
978A: A5 2C           LDA     $2C                 ; {hard.workRam+2C} compare the offset's sign against the old offset
978C: 45 51           EOR     $51                 ; {hard.workRam+51}
978E: 10 0D           BPL     $979D               ; {code.loc_979d} same sign -- continue
9790: A5 51           LDA     $51                 ; {hard.workRam+51} pick the saturation end by the old offset's sign
9792: 30 05           BMI     $9799               ; {code.loc_9799}
9794: A9 00           LDA     #$00                ; saturate to the bottom end of the rim
9796: B8              CLV                         
9797: 50 02           BVC     $979B               ; {code.loc_979b}

loc_9799:
9799: A9 EF           LDA     #$EF                ; saturate to the top end of the rim

loc_979b:
979B: 85 2C           STA     $2C                 ; {hard.workRam+2C}

loc_979d:
979D: A5 2C           LDA     $2C                 ; {hard.workRam+2C} take the offset's high nibble
979F: 4A              LSR     A                   
97A0: 4A              LSR     A                   
97A1: 4A              LSR     A                   
97A2: 4A              LSR     A                   
97A3: 85 2A           STA     $2A                 ; {hard.workRam+2A} store it as the coarse lane
97A5: 18              CLC                         
97A6: 69 01           ADC     #$01                ; pair the fine angle as high-nibble plus one
97A8: 29 0F           AND     #$0F                
97AA: 85 2B           STA     $2B                 ; {hard.workRam+2B} store the fine angle
97AC: A5 2A           LDA     $2A                 ; {hard.workRam+2A} compare the new coarse lane against the current segment
97AE: CD 00 02        CMP     $0200               ; {hard.workRam+200}
97B1: F0 03           BEQ     $97B6               ; {code.loc_97b6} unchanged -- skip the movement sound
97B3: 20 B5 CC        JSR     $CCB5               ; {code.cueRimRotationSound} crossed into a new lane -- ring the rim-movement sound

loc_97b6:
97B6: A5 2A           LDA     $2A                 ; {hard.workRam+2A}
97B8: 8D 00 02        STA     $0200               ; {hard.workRam+200} commit the coarse lane as the player's segment
97BB: A5 2B           LDA     $2B                 ; {hard.workRam+2B}
97BD: 8D 01 02        STA     $0201               ; {hard.workRam+201} commit the fine angle
97C0: A5 2C           LDA     $2C                 ; {hard.workRam+2C}
97C2: 85 51           STA     $51                 ; {hard.workRam+51} carry the rim offset to the next frame
97C4: 60              RTS                         

; scan the depth table loc_2df over count loc_11c for the smallest nonzero
; entry (value in loc_29, index in loc_2a); with a candidate take the
; signed segment delta of loc_2b9[idx] against player segment loc_200
; (signedSegmentDelta) and return an auto-aim spinner code -- 0x00
; aligned, 0x09 one side, 0xf7 the other -- consumed by
; rotateBlasterAroundRim.
aimSpinnerAtNearestEnemy:
97C5: A9 FF           LDA     #$FF                ; seed the shallowest-depth-seen with 0xff
97C7: 85 29           STA     $29                 ; {hard.workRam+29}
97C9: 85 2A           STA     $2A                 ; {hard.workRam+2A} seed its slot index with none
97CB: AE 1C 01        LDX     $011C               ; {hard.workRam+11C} start at the top enemy slot

loc_97ce:
97CE: BD DF 02        LDA     $02DF,X             ; {hard.workRam+2DF} read the slot's depth
97D1: F0 08           BEQ     $97DB               ; {code.loc_97db} empty slot -- skip it
97D3: C5 29           CMP     $29                 ; {hard.workRam+29}
97D5: B0 04           BCS     $97DB               ; {code.loc_97db} not shallower than the best -- skip it
97D7: 85 29           STA     $29                 ; {hard.workRam+29} record the new shallowest depth
97D9: 86 2A           STX     $2A                 ; {hard.workRam+2A} record its slot index

loc_97db:
97DB: CA              DEX                         ; step down to the next slot
97DC: 10 F0           BPL     $97CE               ; {code.loc_97ce} keep walking while the index stays non-negative
97DE: A6 2A           LDX     $2A                 ; {hard.workRam+2A} no candidate found -- return the last depth read
97E0: 30 15           BMI     $97F7               ; {code.loc_97f7}
97E2: BD B9 02        LDA     $02B9,X             ; {hard.workRam+2B9} read the nearest enemy's segment
97E5: AC 00 02        LDY     $0200               ; {hard.workRam+200} read the player's segment
97E8: 20 A6 A7        JSR     $A7A6               ; {code.signedSegmentDelta} signed segment delta between them
97EB: A8              TAY                         
97EC: F0 09           BEQ     $97F7               ; {code.loc_97f7} already aligned -- turn code zero
97EE: 30 05           BMI     $97F5               ; {code.loc_97f5} enemy on one side versus the other
97F0: A9 F7           LDA     #$F7                ; turn code for one direction
97F2: B8              CLV                         
97F3: 50 02           BVC     $97F7               ; {code.loc_97f7}

loc_97f5:
97F5: A9 09           LDA     #$09                ; turn code for the other direction

loc_97f7:
97F7: 60              RTS                         

; step the moving spike each frame while loc_201 bit7 is clear and arm
; flag loc_106 bit7 is set: cue a start sound at trigger height
; loc_202==0x10, advance 16-bit height loc_107/loc_202 by loc_104/loc_105
; (park loc_202=0xff, request mode loc_0=0x0e, cue end sound on ceiling
; overflow), rebuild the spike table (rebuildSpikeTable) past 0x50,
; rederive the per-frame delta from loc_9f, then scan loc_3ac for the
; player-segment lane loc_200 and register a collision
; (cueSpikeCollisionSound/insertObjectHeadTag7/clearActiveShots, clear
; loc_115).
advanceMovingSpike:
97F8: AD 01 02        LDA     $0201               ; {hard.workRam+201} read the field-transition gate -- spike stepping is frozen while the player field is mid-transition
97FB: 10 01           BPL     $97FE               ; {code.loc_97fe} run the spike only while the field is settled
97FD: 60              RTS                         

loc_97fe:
97FE: AD 06 01        LDA     $0106               ; {hard.workRam+106} read the spike arm flag
9801: 30 01           BMI     $9804               ; {code.loc_9804} step the spike only while it is armed
9803: 60              RTS                         

loc_9804:
9804: AD 02 02        LDA     $0202               ; {hard.workRam+202} at the trigger height 0x10...
9807: C9 10           CMP     #$10                
9809: D0 03           BNE     $980E               ; {code.loc_980e}
980B: 20 EE CC        JSR     $CCEE               ; {code.cueMovingSpikeStartSound} cue the spike's rising start note, exactly once at trigger height

loc_980e:
980E: AD 07 01        LDA     $0107               ; {hard.workRam+107} advance the spike height low byte by the per-frame growth step
9811: 18              CLC                         
9812: 6D 04 01        ADC     $0104               ; {hard.workRam+104} add the step low byte
9815: 8D 07 01        STA     $0107               ; {hard.workRam+107} store the spike height low byte
9818: AD 02 02        LDA     $0202               ; {hard.workRam+202} carry into the spike height high byte
981B: 6D 05 01        ADC     $0105               ; {hard.workRam+105} add the step high byte
981E: 8D 02 02        STA     $0202               ; {hard.workRam+202} store the spike height high byte
9821: B0 02           BCS     $9825               ; {code.loc_9825} spike overflowed past the top -> retire it
9823: C9 F0           CMP     #$F0                ; still below the 0xf0 ceiling -> keep growing

loc_9825:
9825: 90 0C           BCC     $9833               ; {code.loc_9833}
9827: A9 0E           LDA     #$0E                ; request game mode 0x0e -- the spike has reached the top
9829: 85 00           STA     $00                 ; {hard.workRam}
982B: 20 F2 CC        JSR     $CCF2               ; {code.cueMovingSpikeEndSound} cue the spike's end sound
982E: A9 FF           LDA     #$FF                ; pin the height at max so it stops climbing
9830: 8D 02 02        STA     $0202               ; {hard.workRam+202}

loc_9833:
9833: AD 02 02        LDA     $0202               ; {hard.workRam+202} once the spike passes the 0x50 reset height...
9836: C9 50           CMP     #$50                ; compare against 0x50
9838: 90 08           BCC     $9842               ; {code.loc_9842} below it -> skip the table rebuild
983A: AD 15 01        LDA     $0115               ; {hard.workRam+115} ...and the spike-table guard is clear...
983D: D0 03           BNE     $9842               ; {code.loc_9842} guard set -> skip
983F: 20 BD A7        JSR     $A7BD               ; {code.rebuildSpikeTable} rebuild the on-screen spike table

loc_9842:
9842: A5 5C           LDA     $5C                 ; {hard.workRam+5C} step the depth-shading accumulator low byte by the same growth step
9844: 18              CLC                         
9845: 6D 04 01        ADC     $0104               ; {hard.workRam+104} add the step low byte
9848: 85 5C           STA     $5C                 ; {hard.workRam+5C} store the accumulator low byte
984A: A5 5F           LDA     $5F                 ; {hard.workRam+5F} carry into the accumulator high byte
984C: 6D 05 01        ADC     $0105               ; {hard.workRam+105} add the step high byte
984F: 90 02           BCC     $9853               ; {code.loc_9853} no overflow -> skip the page byte
9851: E6 5B           INC     $5B                 ; {hard.workRam+5B} page the depth accumulator's extra byte on overflow

loc_9853:
9853: C5 5F           CMP     $5F                 ; {hard.workRam+5F} did the depth high byte move this frame?
9855: F0 03           BEQ     $985A               ; {code.loc_985a} unchanged -> skip the redraw bump
9857: EE 14 01        INC     $0114               ; {hard.workRam+114} bump the redraw counter so the depth-shaded view refreshes

loc_985a:
985A: 85 5F           STA     $5F                 ; {hard.workRam+5F} store the depth accumulator high byte
985C: A5 9F           LDA     $9F                 ; {hard.workRam+9F} take the step source cell
985E: 0A              ASL     A                   ; scale it by 4
985F: 0A              ASL     A                   
9860: C9 30           CMP     #$30                ; clamp the scaled step source to 0x30
9862: 90 02           BCC     $9866               ; {code.loc_9866}
9864: A9 30           LDA     #$30                ; clamp to 0x30

loc_9866:
9866: 18              CLC                         
9867: 69 20           ADC     #$20                ; bias by a minimum climb rate
9869: 18              CLC                         
986A: 6D 04 01        ADC     $0104               ; {hard.workRam+104} fold the new step into the growth step low byte
986D: 8D 04 01        STA     $0104               ; {hard.workRam+104} store the step low byte
9870: AD 05 01        LDA     $0105               ; {hard.workRam+105} carry into the growth step high byte
9873: 69 00           ADC     #$00                
9875: 8D 05 01        STA     $0105               ; {hard.workRam+105} store the step high byte
9878: AD 02 02        LDA     $0202               ; {hard.workRam+202} no collision test once the spike has parked at the ceiling
987B: C9 F0           CMP     #$F0                
987D: B0 22           BCS     $98A1               ; {code.loc_98a1} parked -> done
987F: A2 0F           LDX     #$0F                ; scan the 16 lane-height cells from the top down

loc_9881:
9881: BD AC 03        LDA     $03AC,X             ; {hard.workRam+3AC} read this lane's stored spike height
9884: F0 18           BEQ     $989E               ; {code.loc_989e} empty lane -> skip
9886: EC 00 02        CPX     $0200               ; {hard.workRam+200} only the player's own lane can be hit
9889: D0 13           BNE     $989E               ; {code.loc_989e} other lane -> skip
988B: CD 02 02        CMP     $0202               ; {hard.workRam+202} spike hasn't grown past the player yet -> skip
988E: B0 0E           BCS     $989E               ; {code.loc_989e} not yet -> skip
9890: 20 06 CD        JSR     $CD06               ; {code.cueSpikeCollisionSound} cue the spike collision sound
9893: 20 47 A3        JSR     $A347               ; {code.insertObjectHeadTag7} drop an object-head marker at the hit
9896: A9 00           LDA     #$00                ; clear the spike-table guard
9898: 8D 15 01        STA     $0115               ; {hard.workRam+115}
989B: 20 8F 92        JSR     $928F               ; {code.clearActiveShots} clear the player's live shots

loc_989e:
989E: CA              DEX                         ; next lane
989F: 10 E0           BPL     $9881               ; {code.loc_9881} loop the lane scan

loc_98a1:
98A1: 60              RTS                         

; age the 64-entry per-slot spawn-timer table loc_243 (slot 63..0): freeze
; ageing when the gate loc_2f has bit7 set (raised when loc_108+loc_109
; overshoots loc_11c or loc_125 is set), decrement each active timer, fire
; the expiry handler spawnEnemyOnTimerExpiry when it reaches 0, accumulate
; a per-slot bit mask (via loc_203/$CA38) into loc_14f and copy it out to
; loc_150.
tickSpawnSlotTimers:
98A2: A0 00           LDY     #$00                ; clear the spike-lane mask accumulator
98A4: 8C 4F 01        STY     $014F               ; {hard.workRam+14F}
98A7: AD 08 01        LDA     $0108               ; {hard.workRam+108} sum the active-enemy and enemy-type counts
98AA: 18              CLC                         
98AB: 6D 09 01        ADC     $0109               ; {hard.workRam+109} add the enemy-type count
98AE: CD 1C 01        CMP     $011C               ; {hard.workRam+11C} compare the pair against the slot ceiling
98B1: 90 04           BCC     $98B7               ; {code.loc_98b7} within budget -> no freeze from crowding
98B3: F0 02           BEQ     $98B7               ; {code.loc_98b7} exactly at the ceiling -> no freeze
98B5: A0 FF           LDY     #$FF                ; overcrowded -> raise the ageing-freeze gate

loc_98b7:
98B7: AD 25 01        LDA     $0125               ; {hard.workRam+125} a latched wave transition...
98BA: F0 02           BEQ     $98BE               ; {code.loc_98be} none -> leave the gate as is
98BC: A0 FF           LDY     #$FF                ; ...also freezes timer ageing

loc_98be:
98BE: 84 2F           STY     $2F                 ; {hard.workRam+2F} store the freeze gate
98C0: A2 3F           LDX     #$3F                ; walk the 64-entry spawn-timer table from the top

loc_98c2:
98C2: BD 43 02        LDA     $0243,X             ; {hard.workRam+243} read this slot's timer
98C5: F0 52           BEQ     $9919               ; {code.loc_9919} empty slot -> skip
98C7: 24 2F           BIT     $2F                 ; {hard.workRam+2F} freeze gate raised -> don't age this slot
98C9: 30 23           BMI     $98EE               ; {code.loc_98ee}
98CB: 38              SEC                         ; age the timer down by one
98CC: E9 01           SBC     #$01                
98CE: 9D 43 02        STA     $0243,X             ; {hard.workRam+243} store the aged timer
98D1: D0 06           BNE     $98D9               ; {code.loc_98d9} reached zero?
98D3: 20 23 99        JSR     $9923               ; {code.spawnEnemyOnTimerExpiry} timer expired -> fire the spawn handler for this slot
98D6: B8              CLV                         
98D7: 50 15           BVC     $98EE               ; {code.loc_98ee}

loc_98d9:
98D9: C9 3F           CMP     #$3F                ; just crossed into the mask band at 0x3f?
98DB: D0 11           BNE     $98EE               ; {code.loc_98ee} no -> skip the hold check
98DD: BC 03 02        LDY     $0203,X             ; {hard.workRam+203} read this slot's lane index
98E0: AD 4F 01        LDA     $014F               ; {hard.workRam+14F} fold the mask
98E3: 0D 4F 01        ORA     $014F               ; {hard.workRam+14F}
98E6: 39 38 CA        AND     $CA38,Y             ; {hard.rom+3A38} take this lane's bit from the lane-bit table
98E9: F0 03           BEQ     $98EE               ; {code.loc_98ee} lane not already carrying a spike -> leave it
98EB: FE 43 02        INC     $0243,X             ; {hard.workRam+243} lane already busy -> hold the timer back at 0x40

loc_98ee:
98EE: BD 43 02        LDA     $0243,X             ; {hard.workRam+243} re-read the timer and classify it
98F1: C9 40           CMP     #$40                ; compare against 0x40
98F3: 90 14           BCC     $9909               ; {code.loc_9909} below 0x40 -> mask band
98F5: A5 03           LDA     $03                 ; {hard.workRam+3} on the high band, act only on even frames
98F7: 29 01           AND     #$01                
98F9: D0 0B           BNE     $9906               ; {code.loc_9906} odd frame -> hold
98FB: BD 03 02        LDA     $0203,X             ; {hard.workRam+203} rotate this slot's lane index by one, mod 16
98FE: 18              CLC                         
98FF: 69 01           ADC     #$01                
9901: 29 0F           AND     #$0F                
9903: 9D 03 02        STA     $0203,X             ; {hard.workRam+203} store the rotated lane index

loc_9906:
9906: B8              CLV                         
9907: 50 10           BVC     $9919               ; {code.loc_9919}

loc_9909:
9909: C9 20           CMP     #$20                ; in the 0x20..0x3f band?
990B: 90 0C           BCC     $9919               ; {code.loc_9919} below 0x20 -> skip
990D: BC 03 02        LDY     $0203,X             ; {hard.workRam+203} take this lane's bit
9910: B9 38 CA        LDA     $CA38,Y             ; {hard.rom+3A38} from the lane-bit table
9913: 0D 4F 01        ORA     $014F               ; {hard.workRam+14F} set this lane's bit in the spike-lane mask
9916: 8D 4F 01        STA     $014F               ; {hard.workRam+14F} store the mask accumulator

loc_9919:
9919: CA              DEX                         ; next slot
991A: 10 A6           BPL     $98C2               ; {code.loc_98c2} loop the slot scan
991C: AD 4F 01        LDA     $014F               ; {hard.workRam+14F} publish the rebuilt spike-lane mask for the rest of the frame
991F: 8D 50 01        STA     $0150               ; {hard.workRam+150} store the published mask
9922: 60              RTS                         

; spawn on slot-timer expiry for slot X: raise spawn request 0x29=0xf0,
; latch 0x203,x into 0x2a, save X in 0x35, run the placement pass
; placeSpawnListForColumnDeficit; if the request survives and
; spawnClimberInFreeSlot allocates a free slot, drop 0x3ab and clear the
; slot timer 0x243,x, else flag 0x2f=0xff and re-arm 0x243,x.
spawnEnemyOnTimerExpiry:
9923: A9 F0           LDA     #$F0                ; raise the spawn request with its depth seed 0xf0
9925: 85 29           STA     $29                 ; {hard.workRam+29} store the request depth
9927: BD 03 02        LDA     $0203,X             ; {hard.workRam+203} stage this slot's lane/segment for the spawn
992A: 85 2A           STA     $2A                 ; {hard.workRam+2A} store the staged segment
992C: 86 35           STX     $35                 ; {hard.workRam+35} save the slot index across the placement pass
992E: 20 A5 99        JSR     $99A5               ; {code.placeSpawnListForColumnDeficit} run the per-column spawn placement
9931: A6 35           LDX     $35                 ; {hard.workRam+35} reload the saved slot index
9933: A5 29           LDA     $29                 ; {hard.workRam+29} spawn request still live?
9935: F0 0E           BEQ     $9945               ; {code.loc_9945} cancelled by placement -> fail path
9937: 20 4D 99        JSR     $994D               ; {code.spawnClimberInFreeSlot} try to seat a climber in a free enemy slot
993A: F0 09           BEQ     $9945               ; {code.loc_9945} no free slot -> fail path
993C: CE AB 03        DEC     $03AB               ; {hard.workRam+3AB} spend a fire-gate credit
993F: A9 00           LDA     #$00                ; clear this slot's timer -- the spawn is done
9941: 9D 43 02        STA     $0243,X             ; {hard.workRam+243} clear the slot timer
9944: 60              RTS                         

loc_9945:
9945: A9 FF           LDA     #$FF                ; flag the placement failed, freezing the rest of the scan
9947: 85 2F           STA     $2F                 ; {hard.workRam+2F} store the freeze flag
9949: FE 43 02        INC     $0243,X             ; {hard.workRam+243} re-arm the slot timer to retry later
994C: 60              RTS                         

; spawn a new climber into a free slot: scan the free-slot index down from
; loc_11c skipping slots whose depth loc_2df,y is nonzero, and on a free
; slot seed depth loc_2df,y from loc_29, target segment loc_2b9,y from
; loc_2a (POKEY-random even $60CA&0x0e when loc_2a==0x0f and loc_111 bit7
; set), successor loc_2cc,y, timer loc_2a6,y=0, flags loc_28a,y from
; loc_2c, coord-high loc_291,y from loc_2d, lane byte loc_283,y from
; loc_2b; bump active count loc_108 and per-lane counter loc_142,lane,
; report 0x10 (0x00 when no slot free).
spawnClimberInFreeSlot:
994D: 84 36           STY     $36                 ; {hard.workRam+36} park the caller's scan index
994F: AC 1C 01        LDY     $011C               ; {hard.workRam+11C} scan enemy slots from the top down

loc_9952:
9952: B9 DF 02        LDA     $02DF,Y             ; {hard.workRam+2DF} read this slot's depth cell
9955: D0 46           BNE     $999D               ; {code.loc_999d} slot occupied -> keep scanning
9957: A5 29           LDA     $29                 ; {hard.workRam+29} seat the new enemy's depth from the staged request
9959: 99 DF 02        STA     $02DF,Y             ; {hard.workRam+2DF} store the enemy depth
995C: A5 2A           LDA     $2A                 ; {hard.workRam+2A} staged segment 0x0f...
995E: C9 0F           CMP     #$0F                ; compare against 0x0f
9960: D0 0A           BNE     $996C               ; {code.loc_996c} not 0x0f -> take the segment as staged
9962: 2C 11 01        BIT     $0111               ; {hard.workRam+111} ...and a closed tube...
9965: 10 05           BPL     $996C               ; {code.loc_996c} open tube -> keep the segment
9967: AD CA 60        LDA     $60CA               ; {hard.pokey1+A} ...replaced by a random even lane so spawns spread across the rim
996A: 29 0E           AND     #$0E                ; random even lane

loc_996c:
996C: 99 B9 02        STA     $02B9,Y             ; {hard.workRam+2B9} seat the enemy's tube segment
996F: 18              CLC                         ; animation phase...
9970: 69 01           ADC     #$01                ; segment + 1
9972: 29 0F           AND     #$0F                ; mod 16
9974: 99 CC 02        STA     $02CC,Y             ; {hard.workRam+2CC} seat the enemy's animation phase
9977: A9 00           LDA     #$00                
9979: 99 A6 02        STA     $02A6,Y             ; {hard.workRam+2A6} clear the enemy's timer
997C: A5 2C           LDA     $2C                 ; {hard.workRam+2C} seat the coordinate-list pointer low byte for this enemy
997E: 99 8A 02        STA     $028A,Y             ; {hard.workRam+28A} store the pointer low byte
9981: A5 2D           LDA     $2D                 ; {hard.workRam+2D} seat the coordinate-list pointer high byte
9983: 99 91 02        STA     $0291,Y             ; {hard.workRam+291} store the pointer high byte
9986: EE 08 01        INC     $0108               ; {hard.workRam+108} one more active enemy
9989: A5 2B           LDA     $2B                 ; {hard.workRam+2B} take the staged flag byte
998B: 99 83 02        STA     $0283,Y             ; {hard.workRam+283} seat the enemy's flag byte
998E: A4 36           LDY     $36                 ; {hard.workRam+36}
9990: 29 07           AND     #$07                ; lane = low 3 bits of the flag byte
9992: 86 36           STX     $36                 ; {hard.workRam+36}
9994: AA              TAX                         
9995: FE 42 01        INC     $0142,X             ; {hard.workRam+142} bump this lane's enemy count
9998: A6 36           LDX     $36                 ; {hard.workRam+36}
999A: A9 10           LDA     #$10                ; report a successful spawn
999C: 60              RTS                         

loc_999d:
999D: 88              DEY                         ; step down and continue the free-slot scan
999E: 10 B2           BPL     $9952               ; {code.loc_9952} loop the scan
99A0: A4 36           LDY     $36                 ; {hard.workRam+36}
99A2: A9 00           LDA     #$00                ; report no free slot found
99A4: 60              RTS                         

; top up per-column enemy quotas: build the five-column deficit table
; 0x13d[0..4] from 0x12e minus 0x142 (clamped >=0), deduct 2 per active
; lane (0x2df set, 0x28a&3 nonzero, lane3->col5), cap each at
; (0x11c+1)-sum(0x142), seed 0x61, then per nonzero-column count invoke
; the list-setup dispatcher (dispatchListSetupByColumn) to place a spawn
; list; every exhausted path clears the request flag 0x29.
placeSpawnListForColumnDeficit:
99A5: A9 00           LDA     #$00                
99A7: A2 04           LDX     #$04                

loc_99a9:
99A9: 9D 3D 01        STA     $013D,X             ; {hard.workRam+13D} clear the five-column deficit table
99AC: CA              DEX                         
99AD: 10 FA           BPL     $99A9               ; {code.loc_99a9}
99AF: A2 04           LDX     #$04                

loc_99b1:
99B1: BD 2E 01        LDA     $012E,X             ; {hard.workRam+12E} this column's enemy target
99B4: 38              SEC                         ; minus the enemies already on the lane
99B5: FD 42 01        SBC     $0142,X             ; {hard.workRam+142}
99B8: 90 03           BCC     $99BD               ; {code.loc_99bd} negative deficit -> leave this column at zero
99BA: 9D 3D 01        STA     $013D,X             ; {hard.workRam+13D} store the column's deficit

loc_99bd:
99BD: CA              DEX                         
99BE: 10 F1           BPL     $99B1               ; {code.loc_99b1}
99C0: AC 1C 01        LDY     $011C               ; {hard.workRam+11C} walk every enemy slot

loc_99c3:
99C3: B9 DF 02        LDA     $02DF,Y             ; {hard.workRam+2DF} skip empty slots
99C6: F0 14           BEQ     $99DC               ; {code.loc_99dc}
99C8: B9 8A 02        LDA     $028A,Y             ; {hard.workRam+28A} take this enemy's lane, low two bits
99CB: 29 03           AND     #$03                
99CD: F0 0D           BEQ     $99DC               ; {code.loc_99dc} lane 0 -> skip
99CF: AA              TAX                         
99D0: E0 03           CPX     #$03                ; lane 3 remaps to column 5
99D2: D0 02           BNE     $99D6               ; {code.loc_99d6}
99D4: A2 05           LDX     #$05                

loc_99d6:
99D6: DE 3C 01        DEC     $013C,X             ; {hard.workRam+13C} deduct 2 from that column's budget for this in-flight enemy
99D9: DE 3C 01        DEC     $013C,X             ; {hard.workRam+13C} deduct the second unit

loc_99dc:
99DC: 88              DEY                         ; next slot
99DD: 10 E4           BPL     $99C3               ; {code.loc_99c3}
99DF: A2 04           LDX     #$04                
99E1: AD 1C 01        LDA     $011C               ; {hard.workRam+11C} global cap = slot ceiling plus one...
99E4: 18              CLC                         
99E5: 69 01           ADC     #$01                ; plus one

loc_99e7:
99E7: 38              SEC                         
99E8: FD 42 01        SBC     $0142,X             ; {hard.workRam+142} ...minus the total lane occupancy
99EB: CA              DEX                         
99EC: 10 F9           BPL     $99E7               ; {code.loc_99e7}
99EE: A2 04           LDX     #$04                

loc_99f0:
99F0: DD 3D 01        CMP     $013D,X             ; {hard.workRam+13D} clamp each column's deficit down to the cap
99F3: B0 03           BCS     $99F8               ; {code.loc_99f8}
99F5: 9D 3D 01        STA     $013D,X             ; {hard.workRam+13D} store the clamped deficit

loc_99f8:
99F8: CA              DEX                         
99F9: 10 F5           BPL     $99F0               ; {code.loc_99f0}
99FB: A2 04           LDX     #$04                
99FD: A0 00           LDY     #$00                

loc_99ff:
99FF: BD 3D 01        LDA     $013D,X             ; {hard.workRam+13D} count the nonzero columns
9A02: F0 01           BEQ     $9A05               ; {code.loc_9a05}
9A04: C8              INY                         ; one more nonzero column

loc_9a05:
9A05: CA              DEX                         
9A06: 10 F7           BPL     $99FF               ; {code.loc_99ff}
9A08: 98              TYA                         ; no column needs enemies -> clear the request
9A09: F0 77           BEQ     $9A82               ; {code.loc_9a82}
9A0B: 88              DEY                         ; two or more columns -> multi-column path
9A0C: D0 18           BNE     $9A26               ; {code.loc_9a26}
9A0E: A2 04           LDX     #$04                

loc_9a10:
9A10: BD 3D 01        LDA     $013D,X             ; {hard.workRam+13D} single column: find the column with a deficit...
9A13: F0 0B           BEQ     $9A20               ; {code.loc_9a20}
9A15: BD 29 01        LDA     $0129,X             ; {hard.workRam+129} ...that also has a spawn-cap entry
9A18: F0 06           BEQ     $9A20               ; {code.loc_9a20} none -> keep looking
9A1A: 20 87 9A        JSR     $9A87               ; {code.dispatchListSetupByColumn} seat a spawn list on that column
9A1D: F0 01           BEQ     $9A20               ; {code.loc_9a20} no placement -> keep looking
9A1F: 60              RTS                         ; placed -> done

loc_9a20:
9A20: CA              DEX                         
9A21: 10 ED           BPL     $9A10               ; {code.loc_9a10}
9A23: B8              CLV                         
9A24: 50 5C           BVC     $9A82               ; {code.loc_9a82} exhausted -> clear the request

loc_9a26:
9A26: 84 61           STY     $61                 ; {hard.workRam+61} record the column count minus one
9A28: A2 04           LDX     #$04                

loc_9a2a:
9A2A: BD 3D 01        LDA     $013D,X             ; {hard.workRam+13D} multi-column: skip empty columns
9A2D: F0 0E           BEQ     $9A3D               ; {code.loc_9a3d}
9A2F: BD 42 01        LDA     $0142,X             ; {hard.workRam+142} skip columns already at their cap
9A32: DD 29 01        CMP     $0129,X             ; {hard.workRam+129} compare occupancy to the cap
9A35: B0 06           BCS     $9A3D               ; {code.loc_9a3d}
9A37: 20 87 9A        JSR     $9A87               ; {code.dispatchListSetupByColumn} seat a spawn list on the first below-cap column
9A3A: F0 01           BEQ     $9A3D               ; {code.loc_9a3d} no placement -> keep looking
9A3C: 60              RTS                         ; placed -> done

loc_9a3d:
9A3D: CA              DEX                         
9A3E: 10 EA           BPL     $9A2A               ; {code.loc_9a2a}
9A40: AD 40 01        LDA     $0140               ; {hard.workRam+140} if columns 3 and 2 both still owe enemies...
9A43: F0 1C           BEQ     $9A61               ; {code.loc_9a61}
9A45: AD 3F 01        LDA     $013F               ; {hard.workRam+13F} both live?
9A48: F0 17           BEQ     $9A61               ; {code.loc_9a61}
9A4A: A4 2A           LDY     $2A                 ; {hard.workRam+2A} read the staged lane's stored height
9A4C: B9 AC 03        LDA     $03AC,Y             ; {hard.workRam+3AC}
9A4F: D0 02           BNE     $9A53               ; {code.loc_9a53} nonempty -> use it
9A51: A9 FF           LDA     #$FF                ; default to 0xff when the lane is empty

loc_9a53:
9A53: A2 03           LDX     #$03                
9A55: C9 CC           CMP     #$CC                ; pick column 3 or 2 by the 0xcc height threshold
9A57: B0 02           BCS     $9A5B               ; {code.loc_9a5b}
9A59: A2 02           LDX     #$02                

loc_9a5b:
9A5B: 20 87 9A        JSR     $9A87               ; {code.dispatchListSetupByColumn} seat a spawn list on the chosen column
9A5E: F0 01           BEQ     $9A61               ; {code.loc_9a61} no placement -> fall through
9A60: 60              RTS                         ; placed -> done

loc_9a61:
9A61: AD DA 60        LDA     $60DA               ; {hard.pokey2+A} POKEY-random start column for the round-robin sweep
9A64: 29 03           AND     #$03                
9A66: AA              TAX                         
9A67: E8              INX                         ; step to the start column
9A68: A0 04           LDY     #$04                ; sweep all five columns

loc_9a6a:
9A6A: BD 29 01        LDA     $0129,X             ; {hard.workRam+129} column has a spawn-cap entry...
9A6D: F0 0B           BEQ     $9A7A               ; {code.loc_9a7a} none -> next
9A6F: BD 3D 01        LDA     $013D,X             ; {hard.workRam+13D} ...and a deficit...
9A72: F0 06           BEQ     $9A7A               ; {code.loc_9a7a} none -> next
9A74: 20 87 9A        JSR     $9A87               ; {code.dispatchListSetupByColumn} ...seat a spawn list on it
9A77: F0 01           BEQ     $9A7A               ; {code.loc_9a7a} no placement -> next
9A79: 60              RTS                         ; placed -> done

loc_9a7a:
9A7A: CA              DEX                         
9A7B: 10 02           BPL     $9A7F               ; {code.loc_9a7f} wrap the column index
9A7D: A2 04           LDX     #$04                

loc_9a7f:
9A7F: 88              DEY                         
9A80: 10 E8           BPL     $9A6A               ; {code.loc_9a6a} next column

loc_9a82:
9A82: A9 00           LDA     #$00                ; no placement made: clear the spawn request flag
9A84: 85 29           STA     $29                 ; {hard.workRam+29} store the cleared flag
9A86: 60              RTS                         

; route to the list-setup entry for column X: copy X into the dispatch
; index and enter the computed jump dispatchCoordListSetup, tail-returning
; the selected entry's result to placeSpawnListForColumnDeficit.
dispatchListSetupByColumn:
9A87: 8A              TXA                         ; take the column number as the dispatch selector

; route by the incoming value to one of five coordinate-list setup entries
; (0x9a9d, 0x9aa9, 0x9abb, 0x9ab7, 0x9ab3), passing the slot index X
; through, each of which front-loads a specific index/low-byte then falls
; into the shared 0x9aee/0x9af1 seating.
dispatchCoordListSetup:
9A88: 0A              ASL     A                   ; double the selector to a two-byte table offset
9A89: A8              TAY                         
9A8A: B9 94 9A        LDA     $9A94,Y             ; {hard.rom+A94} push the selected setup entry's address high byte...
9A8D: 48              PHA                         
9A8E: B9 93 9A        LDA     $9A93,Y             ; {hard.rom+A93} ...and its low byte
9A91: 48              PHA                         
9A92: 60              RTS                         ; return jumps into the selected coordinate-list setup entry

; ---- $9A93-$9A9C: data ----
9A93: 9C 9A A8 9A BA 9A B6 9A B2 9A

; seat the index-0 coordinate list: take the low pointer byte from fixed
; table byte 0x9b02, mark index 0 at 0x2b, take the high pointer from held
; source cell 0x15d into 0x2d, reload A from 0x29.
seatDemoCoordListPointer:
9A9D: AD 02 9B        LDA     $9B02               ; {hard.rom+B02} coordinate-list pointer low from the fixed table head
9AA0: 85 2C           STA     $2C                 ; {hard.workRam+2C} store the pointer low byte
9AA2: AD 5D 01        LDA     $015D               ; {hard.workRam+15D} high byte from the runtime-steered source cell
9AA5: A0 00           LDY     #$00                ; selecting index 0
9AA7: F0 4D           BEQ     $9AF6               ; {code.seatCoordListPointerWithHighByte} finish via the shared seater's high-byte tail
9AA9: AD 03 9B        LDA     $9B03               ; {hard.rom+B03} compose the pointer low byte from a table byte OR'd with the list-select flags
9AAC: 0D 6D 01        ORA     $016D               ; {hard.workRam+16D} OR in the list-select flags
9AAF: A0 01           LDY     #$01                ; selecting index 1
9AB1: D0 3E           BNE     $9AF1               ; {code.seatCoordListPointerWithLowByte} finish via the shared seater with the computed low byte
9AB3: A0 04           LDY     #$04                ; selecting index 4
9AB5: D0 37           BNE     $9AEE               ; {code.seatCoordListPointer} into the shared seater

; preset the selecting index to 3 and run the shared 0x9aee seating,
; parking the coordinate-list pointer 0x2c/0x2d from ROM tables
; 0x9b02[3]/0x9afd[3].
seatCoordListPointerAtIndex3:
9AB7: A0 03           LDY     #$03                ; selecting index 3
9AB9: D0 33           BNE     $9AEE               ; {code.seatCoordListPointer} into the shared seater

; pick the lane a new climber will use: from a POKEY-random start
; (0x60ca&3) walk the four-entry lane table 0x149 with a four-step
; countdown in 0x2b, skipping lanes whose occupancy cell 0x13c is empty;
; on a hit set 0x2c to the chosen lane|0x40, seat the list-high byte
; 0x9afd[2] into 0x2d, index 0x02 into 0x2b, and report 0x29 (report 0x00
; on underflow).
selectClimberSpawnLane:
9ABB: AD CA 60        LDA     $60CA               ; {hard.pokey1+A} POKEY-random start lane
9ABE: 29 03           AND     #$03                ; low two bits -> candidate index 0..3
9AC0: A8              TAY                         
9AC1: A9 04           LDA     #$04                ; set a four-attempt countdown
9AC3: 85 2B           STA     $2B                 ; {hard.workRam+2B}
9AC5: 86 39           STX     $39                 ; {hard.workRam+39} stash the caller's index

loc_9ac7:
9AC7: C6 2B           DEC     $2B                 ; {hard.workRam+2B} count down an attempt
9AC9: 10 05           BPL     $9AD0               ; {code.loc_9ad0} attempts remain?
9ACB: A6 39           LDX     $39                 ; {hard.workRam+39} restore the caller's index
9ACD: A9 00           LDA     #$00                ; report no eligible lane
9ACF: 60              RTS                         

loc_9ad0:
9AD0: 88              DEY                         ; step the candidate index down...
9AD1: 10 02           BPL     $9AD5               ; {code.loc_9ad5}
9AD3: A0 03           LDY     #$03                ; ...wrapping to the top

loc_9ad5:
9AD5: BE 49 01        LDX     $0149,Y             ; {hard.workRam+149} read the candidate lane id from the table
9AD8: E0 03           CPX     #$03                ; remap candidate lane 3 to 5
9ADA: D0 02           BNE     $9ADE               ; {code.loc_9ade}
9ADC: A2 05           LDX     #$05                ; lane 5

loc_9ade:
9ADE: BD 3C 01        LDA     $013C,X             ; {hard.workRam+13C} reject an empty lane and try again
9AE1: F0 E4           BEQ     $9AC7               ; {code.loc_9ac7}
9AE3: A6 39           LDX     $39                 ; {hard.workRam+39} restore the caller's index
9AE5: B9 49 01        LDA     $0149,Y             ; {hard.workRam+149} form the pointer low byte: chosen lane OR 0x40
9AE8: 09 40           ORA     #$40                ; OR in 0x40
9AEA: A0 02           LDY     #$02                ; selecting index 2
9AEC: D0 03           BNE     $9AF1               ; {code.seatCoordListPointerWithLowByte} finish via the shared seater with this low byte

; aim the coordinate-list pointer at a packed vector list: read the low
; byte from ROM table 0x9b02+Y into 0x2c and the high byte from 0x9afd+Y
; into 0x2d, remember the selecting index at 0x2b, and reload A from
; holding cell 0x29.
seatCoordListPointer:
9AEE: B9 02 9B        LDA     $9B02,Y             ; {hard.rom+B02} coordinate-list pointer low from the ROM table

; seat the coordinate-list pointer entered one step in: store the caller-
; supplied low byte straight into 0x2c, pull the high byte from ROM table
; 0x9afd+Y into 0x2d, stash index at 0x2b, reload A from 0x29.
seatCoordListPointerWithLowByte:
9AF1: 85 2C           STA     $2C                 ; {hard.workRam+2C} install the pointer low byte
9AF3: B9 FD 9A        LDA     $9AFD,Y             ; {hard.rom+AFD} coordinate-list pointer high from the ROM table

; seat the coordinate-list pointer at its deepest entry: caller already
; parked the low byte at 0x2c, so take the high byte straight from A into
; 0x2d, stash index at 0x2b, reload A from 0x29.
seatCoordListPointerWithHighByte:
9AF6: 84 2B           STY     $2B                 ; {hard.workRam+2B} remember the selecting index
9AF8: 85 2D           STA     $2D                 ; {hard.workRam+2D} install the pointer high byte
9AFA: A5 29           LDA     $29                 ; {hard.workRam+29} reload the accumulator from its holding cell
9AFC: 60              RTS                         

; ---- $9AFD-$9B06: data ----
9AFD: 07 72 07 00 61 40 00 41 40 00

; set up the coordinate/shape list for the packed index in loc_2b
; (saving/restoring the caller index in loc_36): when the held count
; loc_29 >= 0x20 select a list-setup entry through dispatcher
; dispatchCoordListSetup, otherwise seat the pointer pair directly at that
; index via seatCoordListPointer.
setupEnemyCoordList:
9B07: 84 36           STY     $36                 ; {hard.workRam+36} save the caller's index across the setup
9B09: A5 29           LDA     $29                 ; {hard.workRam+29} held count at or above 0x20?
9B0B: C9 20           CMP     #$20                ; compare against 0x20
9B0D: A5 2B           LDA     $2B                 ; {hard.workRam+2B} the packed list index
9B0F: B0 07           BCS     $9B18               ; {code.loc_9b18} high count -> route through the setup dispatcher
9B11: A8              TAY                         
9B12: 20 EE 9A        JSR     $9AEE               ; {code.seatCoordListPointer} else seat the pointer directly at that index
9B15: B8              CLV                         
9B16: 50 03           BVC     $9B1B               ; {code.loc_9b1b}

loc_9b18:
9B18: 20 88 9A        JSR     $9A88               ; {code.dispatchCoordListSetup} route the index through the setup dispatcher

loc_9b1b:
9B1B: A4 36           LDY     $36                 ; {hard.workRam+36} restore the caller's index
9B1D: 60              RTS                         

; the per-frame motion-script walker: when loc_201>=0, walk slots
; loc_37=loc_11c down to 0 and for each nonzero loc_2df,x run its script
; from cursor loc_291,x, dispatching each script byte at $A0F7[loc_10b] to
; a motion opcode handler until the continuation flag loc_10a clears, then
; store the cursor back to loc_291,x; finally signed-accumulate loc_147
; into loc_148, fire the cd06/cd02 sound cues on a sign flip, and negate
; loc_147 to reverse sweep when loc_148 leaves the [0x0f,0xc0] band
runObjectMotionScripts:
9B1E: AD 01 02        LDA     $0201               ; {hard.workRam+201} skip the slot walk while the player field is mid-transition
9B21: 30 33           BMI     $9B56               ; {code.loc_9b56}
9B23: AE 1C 01        LDX     $011C               ; {hard.workRam+11C} seed the slot loop from the top slot
9B26: 86 37           STX     $37                 ; {hard.workRam+37}

loc_9b28:
9B28: A6 37           LDX     $37                 ; {hard.workRam+37}
9B2A: BD DF 02        LDA     $02DF,X             ; {hard.workRam+2DF} skip empty slots
9B2D: F0 23           BEQ     $9B52               ; {code.loc_9b52}
9B2F: A9 01           LDA     #$01                ; raise the script-walk continue flag
9B31: 8D 0A 01        STA     $010A               ; {hard.workRam+10A} store the continue flag
9B34: BD 91 02        LDA     $0291,X             ; {hard.workRam+291} load this slot's saved script cursor
9B37: 8D 0B 01        STA     $010B               ; {hard.workRam+10B} store the working cursor

loc_9b3a:
9B3A: AD 0B 01        LDA     $010B               ; {hard.workRam+10B} the current cursor
9B3D: A8              TAY                         
9B3E: B9 F7 A0        LDA     $A0F7,Y             ; {hard.rom+10F7} read the motion opcode at the cursor
9B41: 20 98 9B        JSR     $9B98               ; {code.dispatchSlotMotionHandler} dispatch the motion opcode for this slot
9B44: EE 0B 01        INC     $010B               ; {hard.workRam+10B} advance the script cursor
9B47: AD 0A 01        LDA     $010A               ; {hard.workRam+10A} keep walking until a handler ends the script
9B4A: D0 EE           BNE     $9B3A               ; {code.loc_9b3a}
9B4C: AD 0B 01        LDA     $010B               ; {hard.workRam+10B} store the advanced cursor back to the slot
9B4F: 9D 91 02        STA     $0291,X             ; {hard.workRam+291} store the cursor

loc_9b52:
9B52: C6 37           DEC     $37                 ; {hard.workRam+37} next slot
9B54: 10 D2           BPL     $9B28               ; {code.loc_9b28} loop the slot scan

loc_9b56:
9B56: AD 48 01        LDA     $0148               ; {hard.workRam+148} signed-accumulate the sweep step into the sweep accumulator
9B59: 18              CLC                         
9B5A: 6D 47 01        ADC     $0147               ; {hard.workRam+147} add the step
9B5D: A8              TAY                         
9B5E: 4D 48 01        EOR     $0148               ; {hard.workRam+148} did the accumulate cross a sign boundary?
9B61: 8C 48 01        STY     $0148               ; {hard.workRam+148} store the new sweep accumulator
9B64: 10 16           BPL     $9B7C               ; {code.loc_9b7c} no sign change -> skip the sweep cues
9B66: 98              TYA                         ; accumulator turned negative...
9B67: 10 06           BPL     $9B6F               ; {code.loc_9b6f}
9B69: 20 06 CD        JSR     $CD06               ; {code.cueSpikeCollisionSound} cue the segment/collision sound as the sweep turns negative
9B6C: B8              CLV                         
9B6D: 50 0D           BVC     $9B7C               ; {code.loc_9b7c}

loc_9b6f:
9B6F: AD 43 01        LDA     $0143               ; {hard.workRam+143} lanes populated...
9B72: F0 08           BEQ     $9B7C               ; {code.loc_9b7c} empty -> skip
9B74: AD 01 02        LDA     $0201               ; {hard.workRam+201} ...and the field settled...
9B77: 30 03           BMI     $9B7C               ; {code.loc_9b7c} mid-transition -> skip
9B79: 20 02 CD        JSR     $CD02               ; {code.requestMotionFlipSound} ...cue the motion-flip sound

loc_9b7c:
9B7C: AD 48 01        LDA     $0148               ; {hard.workRam+148} check the sweep accumulator against its band
9B7F: 30 07           BMI     $9B88               ; {code.loc_9b88} negative side -> test the low bound
9B81: C9 0F           CMP     #$0F                ; inside [0x0f,0xc0] -> reverse the sweep
9B83: B0 07           BCS     $9B8C               ; {code.loc_9b8c} at or above 0x0f -> reverse
9B85: B8              CLV                         
9B86: 50 0F           BVC     $9B97               ; {code.loc_9b97}

loc_9b88:
9B88: C9 C1           CMP     #$C1                ; outside the band -> leave the direction
9B8A: B0 0B           BCS     $9B97               ; {code.loc_9b97} at or above 0xc1 -> leave

loc_9b8c:
9B8C: AD 47 01        LDA     $0147               ; {hard.workRam+147} negate the sweep step to reverse the field's breathing
9B8F: 49 FF           EOR     #$FF                ; one's-complement
9B91: 18              CLC                         
9B92: 69 01           ADC     #$01                ; plus one
9B94: 8D 47 01        STA     $0147               ; {hard.workRam+147} store the reversed sweep step

loc_9b97:
9B97: 60              RTS                         

; route to one of twenty per-slot motion/steering/coordinate handlers
; ($9BCA..$9C3B, incl. the steering step $9CB6) by the pre-doubled table
; offset in the incoming value, passing slot x through and threading the
; offset as the object-insert seed for the collision handlers.
dispatchSlotMotionHandler:
9B98: A8              TAY                         ; the pre-doubled opcode as a table offset
9B99: B9 A3 9B        LDA     $9BA3,Y             ; {hard.rom+BA3} push the selected motion handler's address high byte...
9B9C: 48              PHA                         
9B9D: B9 A2 9B        LDA     $9BA2,Y             ; {hard.rom+BA2} ...and its low byte
9BA0: 48              PHA                         
9BA1: 60              RTS                         ; return jumps into the selected motion handler

; ---- $9BA2-$9BC9: data ----
9BA2: C9 9B CF 9B ED 9B 16 9C 0B 9C CE 9B 57 9C C3 9F
9BB2: DC 9B 5B 9E 81 9D 4E 9C 2E 9E F9 9B 20 9C F0 9E
9BC2: 47 9E B5 9C 66 9D 3A 9C

; housekeeping leaf: clear the walk-continuation flag by writing
; loc_10a=0, ending the walker's inner loop over this object's script
; entries
endObjectMotionScript:
9BCA: A9 00           LDA     #$00                
9BCC: 8D 0A 01        STA     $010A               ; {hard.workRam+10A} clear the walk-continue flag to end this object's script

; no-op leaf that returns immediately, occupying a slot in a computed-
; dispatch set so selecting it falls straight back to the caller.
noopDispatchStub:
9BCF: 60              RTS                         

; immediate store opcode: advance the script cursor loc_10b by one
; (wrapping to a byte) and copy the script byte it now points at,
; $A0F7[loc_10b], verbatim into the acting object's cell loc_298,x
writeScriptConstantToSlot:
9BD0: EE 0B 01        INC     $010B               ; {hard.workRam+10B} advance the motion-script cursor one byte
9BD3: AC 0B 01        LDY     $010B               ; {hard.workRam+10B} load the cursor as the table index
9BD6: B9 F7 A0        LDA     $A0F7,Y             ; {hard.rom+10F7} fetch the literal byte the cursor now points at from the motion-script table
9BD9: 9D 98 02        STA     $0298,X             ; {hard.workRam+298} store that constant into the acting slot's cell
9BDC: 60              RTS                         

; indirect store opcode: advance the script cursor loc_10b by one, treat
; the fetched script byte $A0F7[loc_10b] as a zero-page address, and copy
; the live variable at loc_00+ptr into the acting object's cell loc_298,x
writeScriptVariableToSlot:
9BDD: EE 0B 01        INC     $010B               ; {hard.workRam+10B} advance the motion-script cursor one byte
9BE0: AC 0B 01        LDY     $010B               ; {hard.workRam+10B} load the cursor as the table index
9BE3: B9 F7 A0        LDA     $A0F7,Y             ; {hard.rom+10F7} fetch the script byte -- here a zero-page pointer, not a value
9BE6: A8              TAY                         
9BE7: B9 00 00        LDA     $0000,Y             ; {hard.workRam} read the live zero-page variable the script byte points at
9BEA: 9D 98 02        STA     $0298,X             ; {hard.workRam+298} copy that variable's current value into the acting slot's cell
9BED: 60              RTS                         

; conditional-skip opcode: if the branch flag loc_10c is nonzero do
; nothing, otherwise advance the script cursor loc_10b by two to step past
; a two-byte operand
skipScriptOperandWhenFlagClear:
9BEE: AD 0C 01        LDA     $010C               ; {hard.workRam+10C} read the script branch-test flag
9BF1: D0 06           BNE     $9BF9               ; {code.loc_9bf9} flag set: leave the cursor put -- the operand is consumed on the taken path
9BF3: EE 0B 01        INC     $010B               ; {hard.workRam+10B} flag clear: step the cursor past the...
9BF6: EE 0B 01        INC     $010B               ; {hard.workRam+10B} ...two-byte operand

loc_9bf9:
9BF9: 60              RTS                         

; conditional-jump opcode: advance the script cursor loc_10b by one, then
; only while the branch flag loc_10c is zero replace the cursor entirely
; with the operand target $A0F7[loc_10b], reloading the script position
jumpScriptCursorWhenFlagClear:
9BFA: EE 0B 01        INC     $010B               ; {hard.workRam+10B} advance the script cursor one
9BFD: AD 0C 01        LDA     $010C               ; {hard.workRam+10C} read the branch-suppress flag
9C00: D0 09           BNE     $9C0B               ; {code.loc_9c0b} flag set: suppress the jump and fall through to the next entry
9C02: AC 0B 01        LDY     $010B               ; {hard.workRam+10B}
9C05: B9 F7 A0        LDA     $A0F7,Y             ; {hard.rom+10F7} read the jump target from the script table at the new cursor
9C08: 8D 0B 01        STA     $010B               ; {hard.workRam+10B} reload the cursor with the target -- the scripted jump

loc_9c0b:
9C0B: 60              RTS                         

; dwell opcode: decrement the acting slot's timer loc_298,x; while it
; stays nonzero delegate to the $A0F8-driven goto (followScriptGoto) so
; the object keeps cycling its current state, and only when the timer hits
; zero bump the shared cursor loc_10b to release the script to the next
; instruction
holdSlotPoseUntilTimerExpires:
9C0C: DE 98 02        DEC     $0298,X             ; {hard.workRam+298} count this slot's dwell timer down one frame
9C0F: D0 06           BNE     $9C17               ; {code.followScriptGoto} still dwelling: re-run the current script state
9C11: EE 0B 01        INC     $010B               ; {hard.workRam+10B} timer expired: release the script to the next instruction
9C14: B8              CLV                         
9C15: 50 09           BVC     $9C20               ; {code.loc_9c20}

; unconditional-goto opcode: use the current cursor loc_10b to index the
; parallel table $A0F8 and write $A0F8[loc_10b] back as the new cursor,
; following the chained operand
followScriptGoto:
9C17: AC 0B 01        LDY     $010B               ; {hard.workRam+10B} current script position
9C1A: B9 F8 A0        LDA     $A0F8,Y             ; {hard.rom+10F8} read the goto target from the parallel goto table
9C1D: 8D 0B 01        STA     $010B               ; {hard.workRam+10B} write it back as the new cursor -- the unconditional goto

loc_9c20:
9C20: 60              RTS                         

; boundary-test opcode: read the slot's segment loc_2b9,x, look up its
; boundary in loc_3ac (a zero entry reads as the maximum 0xff), and set
; the branch flag loc_10c to 1 when the boundary is at or beyond the
; slot's depth loc_2df,x, else 0
setFlagIfSlotPastSegmentBound:
9C21: BC B9 02        LDY     $02B9,X             ; {hard.workRam+2B9} read slot x's tube segment
9C24: B9 AC 03        LDA     $03AC,Y             ; {hard.workRam+3AC} index that segment's boundary depth in the per-lane limit table
9C27: D0 02           BNE     $9C2B               ; {code.loc_9c2b} nonzero limit: use it
9C29: A9 FF           LDA     #$FF                ; a zero entry means no limit -- read as the maximum depth

loc_9c2b:
9C2B: DD DF 02        CMP     $02DF,X             ; {hard.workRam+2DF} compare the boundary against the slot's depth
9C2E: B0 05           BCS     $9C35               ; {code.loc_9c35} boundary at or beyond the depth: flag 1
9C30: A9 00           LDA     #$00                ; else flag 0
9C32: B8              CLV                         
9C33: 50 02           BVC     $9C37               ; {code.loc_9c37}

loc_9c35:
9C35: A9 01           LDA     #$01                ; boundary reached: flag 1

loc_9c37:
9C37: 8D 0C 01        STA     $010C               ; {hard.workRam+10C} leave the 1/0 verdict in the script branch flag
9C3A: 60              RTS                         

; phase-probe opcode: form ((loc_147<<2)+loc_148) & loc_148 & 0x80, XOR
; against 0x80, and store to the branch flag loc_10c so it becomes 0x00
; when that high bit is set and 0x80 when clear
setFlagFromPhaseAccumulatorSign:
9C3B: AD 47 01        LDA     $0147               ; {hard.workRam+147} read the per-frame enemy animation delta
9C3E: 0A              ASL     A                   ; scale the delta by four
9C3F: 0A              ASL     A                   
9C40: 18              CLC                         
9C41: 6D 48 01        ADC     $0148               ; {hard.workRam+148} add the animation-phase accumulator
9C44: 2D 48 01        AND     $0148               ; {hard.workRam+148} AND with the accumulator to isolate the shared sign
9C47: 29 80           AND     #$80                ; keep just the high sign bit
9C49: 49 80           EOR     #$80                ; invert it
9C4B: 8D 0C 01        STA     $010C               ; {hard.workRam+10C} leave the phase-sign verdict in the script branch flag
9C4E: 60              RTS                         

; toggle bit6 (the turn/rotation side flag) of the slot's flag cell
; loc_283,x in place and return the new value.
toggleEnemyTurnSide:
9C4F: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} read slot x's flag byte
9C52: 49 40           EOR     #$40                ; invert bit6 -- the rim turn side
9C54: 9D 83 02        STA     $0283,X             ; {hard.workRam+283} store the flipped turn side back
9C57: 60              RTS                         

; step slot x's 16-bit tube depth (low loc_29f,x / high loc_2df,x) by the
; per-segment delta from the loc_160/loc_165 table indexed by the segment
; (loc_283,x & 7), routing to the add path advanceEnemyLaneDepth when
; loc_28a,x bit7 is clear or the subtract path reverseEnemyLaneDepth when
; set.
stepEnemyDepthInLaneDirection:
9C58: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} read slot x's flag byte
9C5B: 29 07           AND     #$07                ; low 3 bits are the lane segment -- the per-segment speed-table index
9C5D: A8              TAY                         
9C5E: BD 8A 02        LDA     $028A,X             ; {hard.workRam+28A} read the slot's direction byte
9C61: 30 36           BMI     $9C99               ; {code.reverseEnemyLaneDepth} bit7 set: take the reverse (retreat) path

; add-direction depth step: loc_29f,x += loc_160,seg (16-bit) into
; loc_2df,x, then on the new high byte settle the slot via
; settleEnemyAtTargetDepth (hi <= floor loc_202), finish with the new high
; as exit value (hi >= 0x20), or retire/replace the slot via
; retireEnemyAndSpawnSplit when hi < 0x20 with an armed gate (loc_28a,x &
; 3).
advanceEnemyLaneDepth:
9C63: BD 9F 02        LDA     $029F,X             ; {hard.workRam+29F} low byte of the slot's 16-bit tube depth
9C66: 18              CLC                         
9C67: 79 60 01        ADC     $0160,Y             ; {hard.workRam+160} add the per-segment climb-speed low byte
9C6A: 9D 9F 02        STA     $029F,X             ; {hard.workRam+29F} store the depth low byte
9C6D: BD DF 02        LDA     $02DF,X             ; {hard.workRam+2DF} depth high byte
9C70: 79 65 01        ADC     $0165,Y             ; {hard.workRam+165} add the per-segment climb-speed high byte with carry
9C73: 9D DF 02        STA     $02DF,X             ; {hard.workRam+2DF} store the depth high byte -- enemy advanced toward the rim
9C76: CD 02 02        CMP     $0202               ; {hard.workRam+202} compare against the shared shot/floor depth
9C79: F0 02           BEQ     $9C7D               ; {code.loc_9c7d} at the floor
9C7B: B0 06           BCS     $9C83               ; {code.loc_9c83} past the floor: carry on

loc_9c7d:
9C7D: 20 06 9D        JSR     $9D06               ; {code.settleEnemyAtTargetDepth} reached the floor: settle the enemy at target depth
9C80: B8              CLV                         
9C81: 50 13           BVC     $9C96               ; {code.loc_9c96}

loc_9c83:
9C83: C9 20           CMP     #$20                ; high byte still above 0x20?
9C85: B0 0F           BCS     $9C96               ; {code.loc_9c96} yes, still deep: done
9C87: BD 8A 02        LDA     $028A,X             ; {hard.workRam+28A} read the direction byte
9C8A: 29 03           AND     #$03                ; the replacement/split gate bits
9C8C: F0 08           BEQ     $9C96               ; {code.loc_9c96} gate clear: done
9C8E: 8A              TXA                         
9C8F: 48              PHA                         
9C90: A8              TAY                         
9C91: 20 6F A0        JSR     $A06F               ; {code.retireEnemyAndSpawnSplit} retire the enemy and spawn its split/replacement
9C94: 68              PLA                         
9C95: AA              TAX                         

loc_9c96:
9C96: B8              CLV                         
9C97: 50 1C           BVC     $9CB5               ; {code.loc_9cb5}

; subtract-direction depth step: loc_29f,x -= loc_160,seg (16-bit, with
; borrow) into loc_2df,x, flooring the high byte to 0xf2 when it
; underflows past 0xf0; returns the new (or floored) high byte.
reverseEnemyLaneDepth:
9C99: BD 9F 02        LDA     $029F,X             ; {hard.workRam+29F} depth low byte
9C9C: 38              SEC                         
9C9D: F9 60 01        SBC     $0160,Y             ; {hard.workRam+160} subtract the per-segment climb-speed low byte
9CA0: 9D 9F 02        STA     $029F,X             ; {hard.workRam+29F} store the depth low byte
9CA3: BD DF 02        LDA     $02DF,X             ; {hard.workRam+2DF} depth high byte
9CA6: F9 65 01        SBC     $0165,Y             ; {hard.workRam+165} subtract the climb-speed high byte with borrow
9CA9: 9D DF 02        STA     $02DF,X             ; {hard.workRam+2DF} store the depth high byte -- enemy retreats up the tube
9CAC: C9 F0           CMP     #$F0                ; underflowed past the far rim?
9CAE: 90 05           BCC     $9CB5               ; {code.loc_9cb5} no underflow: done
9CB0: A9 F2           LDA     #$F2                ; clamp value
9CB2: 9D DF 02        STA     $02DF,X             ; {hard.workRam+2DF} floor the depth at the far rim (0xf2)

loc_9cb5:
9CB5: 60              RTS                         

; step slot x's coordinate keyed on loc_28a,x bit7 (sub-step via
; reverseEnemyLaneDepth flipping direction at the loc_157 threshold when
; loc_3ab is set, else add-step via advanceEnemyLaneDepth), and on the
; common tail -- loc_148 bit7 clear AND loc_2df,x < loc_157 AND
; loc_200==loc_2b9,x AND loc_201==loc_2cc,x -- seed a fresh object for
; that slot via insertObjectHeadTag7 with the stepped Y.
steerSlotCoordinate:
9CB6: A0 01           LDY     #$01                ; default steering index
9CB8: BD 8A 02        LDA     $028A,X             ; {hard.workRam+28A} read the slot's direction byte
9CBB: 30 10           BMI     $9CCD               ; {code.loc_9ccd} bit7 set: retreating slot, take the sub-step path
9CBD: BD DF 02        LDA     $02DF,X             ; {hard.workRam+2DF} depth high byte
9CC0: CD 57 01        CMP     $0157               ; {hard.workRam+157} compare against the near-rim threshold
9CC3: 90 02           BCC     $9CC7               ; {code.loc_9cc7} below threshold: keep steering index 1
9CC5: A0 00           LDY     #$00                ; at or over threshold: steering index 0

loc_9cc7:
9CC7: 20 63 9C        JSR     $9C63               ; {code.advanceEnemyLaneDepth} add-step the depth forward one tick
9CCA: B8              CLV                         
9CCB: 50 17           BVC     $9CE4               ; {code.loc_9ce4}

loc_9ccd:
9CCD: 20 99 9C        JSR     $9C99               ; {code.reverseEnemyLaneDepth} sub-step the depth backward one tick -- retreat
9CD0: AC AB 03        LDY     $03AB               ; {hard.workRam+3AB} read the enemy-fire gate
9CD3: D0 02           BNE     $9CD7               ; {code.loc_9cd7} gate armed: probe with the stepped depth
9CD5: A9 FF           LDA     #$FF                ; gate clear: probe as the far value

loc_9cd7:
9CD7: CD 57 01        CMP     $0157               ; {hard.workRam+157} compare the probe against the near threshold
9CDA: 90 08           BCC     $9CE4               ; {code.loc_9ce4} not yet at the far threshold: on to the tail
9CDC: BD 8A 02        LDA     $028A,X             ; {hard.workRam+28A} reached the threshold: read the direction byte
9CDF: 49 80           EOR     #$80                ; flip the climb-direction bit
9CE1: 9D 8A 02        STA     $028A,X             ; {hard.workRam+28A} reverse the slot's travel direction

loc_9ce4:
9CE4: AD 48 01        LDA     $0148               ; {hard.workRam+148} read the animation accumulator
9CE7: 30 1B           BMI     $9D04               ; {code.loc_9d04} busy (bit7 set): bail
9CE9: BD DF 02        LDA     $02DF,X             ; {hard.workRam+2DF} depth high byte
9CEC: CD 57 01        CMP     $0157               ; {hard.workRam+157} near-rim threshold
9CEF: B0 13           BCS     $9D04               ; {code.loc_9d04} not close enough: bail
9CF1: AD 00 02        LDA     $0200               ; {hard.workRam+200} player's segment
9CF4: DD B9 02        CMP     $02B9,X             ; {hard.workRam+2B9} same lane as this enemy?
9CF7: D0 0B           BNE     $9D04               ; {code.loc_9d04} wrong lane: bail
9CF9: AD 01 02        LDA     $0201               ; {hard.workRam+201} player's fine angle
9CFC: DD CC 02        CMP     $02CC,X             ; {hard.workRam+2CC} matches the enemy's phase/angle?
9CFF: D0 03           BNE     $9D04               ; {code.loc_9d04} wrong angle: bail
9D01: 20 47 A3        JSR     $A347               ; {code.insertObjectHeadTag7} enemy is on the player: seed a fresh object for the slot

loc_9d04:
9D04: 60              RTS                         

; ---- $9D05-$9D05: data ----
9D05: 16

; settle slot x at the target depth: stash floor loc_202 into loc_2df,x,
; then by kind -- a kind-1 slot (loc_283,x&7==1) with loc_3ab!=0 flips
; bit7 of loc_28a,x; a negative slot bumps its stashed depth; else drop
; count loc_108, and when per-type count loc_109==1 scan slots 6..0 for a
; matching-depth neighbour (index into loc_38) and copy its inverted bit6
; into loc_283,x, otherwise re-aim via faceEnemyTowardPlayerSegment,
; finally marking loc_10b=0x41 and bumping loc_109.
settleEnemyAtTargetDepth:
9D06: AD 02 02        LDA     $0202               ; {hard.workRam+202} read the shared floor/shot depth
9D09: 9D DF 02        STA     $02DF,X             ; {hard.workRam+2DF} stash it as this slot's depth
9D0C: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} read the flag byte
9D0F: 29 07           AND     #$07                ; low 3 bits: the lane kind
9D11: C9 01           CMP     #$01                ; kind 1?
9D13: D0 0E           BNE     $9D23               ; {code.loc_9d23} not kind 1: skip the fire flip
9D15: AD AB 03        LDA     $03AB               ; {hard.workRam+3AB} read the enemy-fire gate
9D18: F0 09           BEQ     $9D23               ; {code.loc_9d23} gate clear: skip
9D1A: BD 8A 02        LDA     $028A,X             ; {hard.workRam+28A} read the direction byte
9D1D: 49 80           EOR     #$80                ; flip the climb direction -- turn to fire
9D1F: 9D 8A 02        STA     $028A,X             ; {hard.workRam+28A} store it
9D22: 60              RTS                         

loc_9d23:
9D23: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} read the flag byte
9D26: 10 04           BPL     $9D2C               ; {code.loc_9d2c} positive slot: go to the split logic
9D28: FE DF 02        INC     $02DF,X             ; {hard.workRam+2DF} negative slot: nudge its stashed depth and stop
9D2B: 60              RTS                         

loc_9d2c:
9D2C: CE 08 01        DEC     $0108               ; {hard.workRam+108} drop the total live-enemy count
9D2F: AD 09 01        LDA     $0109               ; {hard.workRam+109} read the per-type enemy count
9D32: C9 01           CMP     #$01                ; exactly one of this type?
9D34: F0 06           BEQ     $9D3C               ; {code.loc_9d3c} yes: scan for a matching neighbour
9D36: 20 67 9D        JSR     $9D67               ; {code.faceEnemyTowardPlayerSegment} otherwise re-aim the slot toward the player
9D39: B8              CLV                         
9D3A: 50 22           BVC     $9D5E               ; {code.loc_9d5e}

loc_9d3c:
9D3C: A0 06           LDY     #$06                ; scan from slot 6 downward

loc_9d3e:
9D3E: B9 DF 02        LDA     $02DF,Y             ; {hard.workRam+2DF} read the candidate slot's depth
9D41: F0 0E           BEQ     $9D51               ; {code.loc_9d51} empty slot: skip it
9D43: 84 38           STY     $38                 ; {hard.workRam+38} record the current scan index
9D45: E4 38           CPX     $38                 ; {hard.workRam+38} is it this same slot?
9D47: F0 08           BEQ     $9D51               ; {code.loc_9d51} self: skip
9D49: B9 DF 02        LDA     $02DF,Y             ; {hard.workRam+2DF} candidate depth
9D4C: CD 02 02        CMP     $0202               ; {hard.workRam+202} matches the shared floor depth?
9D4F: F0 03           BEQ     $9D54               ; {code.loc_9d54} match: take this neighbour

loc_9d51:
9D51: 88              DEY                         ; next slot down
9D52: 10 EA           BPL     $9D3E               ; {code.loc_9d3e} keep scanning while slots remain

loc_9d54:
9D54: B9 83 02        LDA     $0283,Y             ; {hard.workRam+283} read the matched neighbour's flag byte
9D57: 29 40           AND     #$40                ; its turn-side bit
9D59: 49 40           EOR     #$40                ; inverted
9D5B: 9D 83 02        STA     $0283,X             ; {hard.workRam+283} set this slot's turn side opposite the neighbour's

loc_9d5e:
9D5E: A9 41           LDA     #$41                ; script-cursor seed
9D60: 8D 0B 01        STA     $010B               ; {hard.workRam+10B} point the motion-script cursor at 0x41
9D63: EE 09 01        INC     $0109               ; {hard.workRam+109} bump the per-type enemy count
9D66: 60              RTS                         

; aim slot x's turn side toward the player: take the signed segment delta
; of loc_2b9,x against player segment loc_200 via signedSegmentDelta, then
; clear bit6 of loc_283,x when the delta is negative (bit7 set) and set it
; otherwise.
faceEnemyTowardPlayerSegment:
9D67: BD B9 02        LDA     $02B9,X             ; {hard.workRam+2B9} read slot x's own segment
9D6A: A8              TAY                         
9D6B: AD 00 02        LDA     $0200               ; {hard.workRam+200} player's segment
9D6E: 20 A6 A7        JSR     $A7A6               ; {code.signedSegmentDelta} signed ring distance from the player to this enemy
9D71: 0A              ASL     A                   ; shift the sign into carry
9D72: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} read the flag byte
9D75: B0 05           BCS     $9D7C               ; {code.loc_9d7c} distance negative: clear the turn-side bit
9D77: 09 40           ORA     #$40                ; else set bit6 -- turn toward the player
9D79: B8              CLV                         
9D7A: 50 02           BVC     $9D7E               ; {code.loc_9d7e}

loc_9d7c:
9D7C: 29 BF           AND     #$BF                ; clear bit6 -- turn the other way

loc_9d7e:
9D7E: 9D 83 02        STA     $0283,X             ; {hard.workRam+283} store the turn-side decision
9D81: 60              RTS                         

; step the flipper's turn animation for slot x: advance phase counter
; loc_2cc,x by loc_283,x bit6 (keep nibble, force bit7); when state
; loc_283,x&7 != 4 re-aim (lookupRingHeading of loc_283,x^0x40 vs
; loc_2b9,x) and on a phase match drop bit7 and reseed the phase/lane
; loc_2b9,x; when state==4 at a step boundary rotate loc_2b9,x, reseed
; phase to 0x20, flip loc_28a,x bit7 and (loc_3ab==0) kick
; flipEnemyLaneTowardTarget when depth loc_2df,x==floor loc_202; every
; exit copies loc_283,x bit7 into shared flag loc_10c.
animateFlipperTurn:
9D82: BC CC 02        LDY     $02CC,X             ; {hard.workRam+2CC} read the slot's phase counter
9D85: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} read the flag byte
9D88: 29 40           AND     #$40                ; bit6: which way the phase steps
9D8A: D0 04           BNE     $9D90               ; {code.loc_9d90} bit6 set: step the phase down
9D8C: C8              INY                         ; bit6 clear: step the phase up
9D8D: B8              CLV                         
9D8E: 50 01           BVC     $9D91               ; {code.loc_9d91}

loc_9d90:
9D90: 88              DEY                         ; step the phase down

loc_9d91:
9D91: 98              TYA                         
9D92: 29 0F           AND     #$0F                ; keep the low nibble
9D94: 09 80           ORA     #$80                ; force bit7 active
9D96: 9D CC 02        STA     $02CC,X             ; {hard.workRam+2CC} store the advanced phase
9D99: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} read the flag byte
9D9C: 29 07           AND     #$07                ; low 3 bits: the animation state
9D9E: C9 04           CMP     #$04                ; settling state (4)?
9DA0: D0 4C           BNE     $9DEE               ; {code.loc_9dee} not settling: re-aim/walk branch
9DA2: BD CC 02        LDA     $02CC,X             ; {hard.workRam+2CC} settling: read the phase
9DA5: 29 07           AND     #$07                ; at a step boundary?
9DA7: D0 42           BNE     $9DEB               ; {code.loc_9deb} not on a boundary: done
9DA9: BD CC 02        LDA     $02CC,X             ; {hard.workRam+2CC} read the phase
9DAC: 29 08           AND     #$08                ; phase bit3?
9DAE: F0 0B           BEQ     $9DBB               ; {code.loc_9dbb} clear: skip the lane rotate
9DB0: BD B9 02        LDA     $02B9,X             ; {hard.workRam+2B9} read the segment
9DB3: 18              CLC                         
9DB4: 69 01           ADC     #$01                ; plus one lane
9DB6: 29 0F           AND     #$0F                ; wrap to the 16-lane ring
9DB8: 9D B9 02        STA     $02B9,X             ; {hard.workRam+2B9} rotate the enemy up one lane

loc_9dbb:
9DBB: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} read the flag byte
9DBE: 29 7F           AND     #$7F                ; drop bit7
9DC0: 9D 83 02        STA     $0283,X             ; {hard.workRam+283} mark the flip settled
9DC3: A9 20           LDA     #$20                ; reseed value
9DC5: 9D CC 02        STA     $02CC,X             ; {hard.workRam+2CC} reset the phase to 0x20
9DC8: BD 8A 02        LDA     $028A,X             ; {hard.workRam+28A} read the direction byte
9DCB: 49 80           EOR     #$80                ; flip the turn sign
9DCD: 9D 8A 02        STA     $028A,X             ; {hard.workRam+28A} store it
9DD0: AD AB 03        LDA     $03AB               ; {hard.workRam+3AB} read the enemy-fire gate
9DD3: D0 16           BNE     $9DEB               ; {code.loc_9deb} gate armed: done
9DD5: BD DF 02        LDA     $02DF,X             ; {hard.workRam+2DF} read the flipper's depth
9DD8: CD 02 02        CMP     $0202               ; {hard.workRam+202} at the player's floor depth?
9DDB: D0 06           BNE     $9DE3               ; {code.loc_9de3} no: just isolate the direction sign
9DDD: 20 81 9F        JSR     $9F81               ; {code.flipEnemyLaneTowardTarget} at the player: lunge across toward the target lane
9DE0: B8              CLV                         
9DE1: 50 08           BVC     $9DEB               ; {code.loc_9deb}

loc_9de3:
9DE3: BD 8A 02        LDA     $028A,X             ; {hard.workRam+28A} read the direction byte
9DE6: 29 80           AND     #$80                ; keep just the sign bit
9DE8: 9D 8A 02        STA     $028A,X             ; {hard.workRam+28A} mask the direction down to its sign

loc_9deb:
9DEB: B8              CLV                         
9DEC: 50 38           BVC     $9E26               ; {code.loc_9e26}

loc_9dee:
9DEE: BC B9 02        LDY     $02B9,X             ; {hard.workRam+2B9} not settling: read the segment
9DF1: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} read the flag byte
9DF4: 49 40           EOR     #$40                ; flip bit6 for the heading lookup
9DF6: 20 D7 9E        JSR     $9ED7               ; {code.lookupRingHeading} look up the target ring heading
9DF9: DD CC 02        CMP     $02CC,X             ; {hard.workRam+2CC} does it match the current phase?
9DFC: D0 28           BNE     $9E26               ; {code.loc_9e26} no: done for this frame
9DFE: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} read the flag byte
9E01: 29 7F           AND     #$7F                ; drop bit7
9E03: 9D 83 02        STA     $0283,X             ; {hard.workRam+283} clear the active bit
9E06: 29 40           AND     #$40                ; test the turn-side bit
9E08: D0 11           BNE     $9E1B               ; {code.loc_9e1b} set: take the +1-lane branch
9E0A: BD B9 02        LDA     $02B9,X             ; {hard.workRam+2B9} read the segment
9E0D: 9D CC 02        STA     $02CC,X             ; {hard.workRam+2CC} copy the segment into the phase
9E10: 38              SEC                         
9E11: E9 01           SBC     #$01                ; minus one lane
9E13: 29 0F           AND     #$0F                ; wrap the ring
9E15: 9D B9 02        STA     $02B9,X             ; {hard.workRam+2B9} step the segment down one lane
9E18: B8              CLV                         
9E19: 50 0B           BVC     $9E26               ; {code.loc_9e26}

loc_9e1b:
9E1B: BD B9 02        LDA     $02B9,X             ; {hard.workRam+2B9} read the segment
9E1E: 18              CLC                         
9E1F: 69 01           ADC     #$01                ; plus one lane
9E21: 29 0F           AND     #$0F                ; wrap the ring
9E23: 9D CC 02        STA     $02CC,X             ; {hard.workRam+2CC} set the phase to the next lane up

loc_9e26:
9E26: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} read the flag byte
9E29: 29 80           AND     #$80                ; isolate bit7 active
9E2B: 8D 0C 01        STA     $010C               ; {hard.workRam+10C} copy it into the shared script branch flag
9E2E: 60              RTS                         

; spawn a type-5 object when a live slot (loc_283,x bit7 clear) has its
; coordinate pair loc_2b9,x/loc_2cc,x matching the current target pair
; loc_200/loc_201.
spawnType5OnCoordMatch:
9E2F: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} read this slot's enemy state byte
9E32: 30 13           BMI     $9E47               ; {code.loc_9e47} bail if the slot is already live -- only act on a not-yet-live slot
9E34: BD B9 02        LDA     $02B9,X             ; {hard.workRam+2B9} read the slot's segment
9E37: CD 00 02        CMP     $0200               ; {hard.workRam+200} compare against the player's current rim segment
9E3A: D0 0B           BNE     $9E47               ; {code.loc_9e47} bail unless the slot's segment matches the player lane
9E3C: BD CC 02        LDA     $02CC,X             ; {hard.workRam+2CC} read the slot's phase/successor heading
9E3F: CD 01 02        CMP     $0201               ; {hard.workRam+201} compare against the player fine-angle cell
9E42: D0 03           BNE     $9E47               ; {code.loc_9e47} bail unless it matches too
9E44: 20 3A A3        JSR     $A33A               ; {code.insertType5AndDrainPending} on a full coordinate match, spawn the type-5 object and drain the pending queue

loc_9e47:
9E47: 60              RTS                         

; fire the player-collision hit when a slot's depth loc_2df,x matches
; loc_202 and its segment loc_2b9,x matches loc_200.
fireHitOnPlayerCollision:
9E48: BD DF 02        LDA     $02DF,X             ; {hard.workRam+2DF} read the slot's tube-depth high byte
9E4B: CD 02 02        CMP     $0202               ; {hard.workRam+202} compare with the player shot depth
9E4E: D0 0B           BNE     $9E5B               ; {code.loc_9e5b} bail unless the depth matches
9E50: BD B9 02        LDA     $02B9,X             ; {hard.workRam+2B9} read the slot's segment
9E53: CD 00 02        CMP     $0200               ; {hard.workRam+200} compare with the player rim segment
9E56: D0 03           BNE     $9E5B               ; {code.loc_9e5b} bail unless the lane matches
9E58: 20 43 A3        JSR     $A343               ; {code.insertObjectHeadTag9} register the hit on the player and insert the object head tag

loc_9e5b:
9E5B: 60              RTS                         

; step a climber's segment with the flip guard: run the depth-gated bit6
; keeper first, then fall into the shared segment-step body for slot x.
stepClimberSegmentGuarded:
9E5C: 20 AB 9E        JSR     $9EAB               ; {code.keepClimberFlipBitByDepth} run the depth-gated flip-bit keeper first, then fall into the segment step

; step a climber one segment and set its next heading: force bit7 on
; loc_283,x (mark live) and branch on its low-3-bit segment -- for the
; seam segment 4 step depth loc_2b9,x down one mod16 and store 0x87 (bit6
; set) or store 0x81 (bit6 clear); for any other segment step depth up one
; mod16 (bit6 set) then store the ring-lookup heading into loc_2cc,x.
stepClimberSegmentAndHeading:
9E5F: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} read the enemy state byte
9E62: 09 80           ORA     #$80                ; mark the slot live -- set bit7
9E64: 9D 83 02        STA     $0283,X             ; {hard.workRam+283} store it back
9E67: 29 07           AND     #$07                ; isolate the low-3-bit segment kind
9E69: C9 04           CMP     #$04                ; is this segment kind 4
9E6B: D0 1F           BNE     $9E8C               ; {code.loc_9e8c} branch to the ordinary-segment case if not
9E6D: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} reload state for the kind-4 case
9E70: 29 40           AND     #$40                ; test the turn-side bit
9E72: D0 05           BNE     $9E79               ; {code.loc_9e79} branch by side
9E74: A9 81           LDA     #$81                ; heading 0x81 for one side
9E76: B8              CLV                         
9E77: 50 0D           BVC     $9E86               ; {code.loc_9e86}

loc_9e79:
9E79: BD B9 02        LDA     $02B9,X             ; {hard.workRam+2B9} read the segment for the other side
9E7C: 38              SEC                         
9E7D: E9 01           SBC     #$01                ; step the segment down one
9E7F: 29 0F           AND     #$0F                ; wrap mod 16
9E81: 9D B9 02        STA     $02B9,X             ; {hard.workRam+2B9} store the stepped segment
9E84: A9 87           LDA     #$87                ; heading 0x87 -- the bit6-set variant

loc_9e86:
9E86: 9D CC 02        STA     $02CC,X             ; {hard.workRam+2CC} store the phase/heading
9E89: B8              CLV                         
9E8A: 50 1E           BVC     $9EAA               ; {code.loc_9eaa}

loc_9e8c:
9E8C: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} reload state for the ordinary-segment case
9E8F: 29 40           AND     #$40                ; test the turn-side bit
9E91: F0 0B           BEQ     $9E9E               ; {code.loc_9e9e} skip the step-up if the side bit is clear
9E93: BD B9 02        LDA     $02B9,X             ; {hard.workRam+2B9} read the segment
9E96: 18              CLC                         
9E97: 69 01           ADC     #$01                ; step the segment up one
9E99: 29 0F           AND     #$0F                ; wrap mod 16
9E9B: 9D B9 02        STA     $02B9,X             ; {hard.workRam+2B9} store the stepped segment

loc_9e9e:
9E9E: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} reload state for the heading lookup
9EA1: BC B9 02        LDY     $02B9,X             ; {hard.workRam+2B9} index by the current segment
9EA4: 20 D7 9E        JSR     $9ED7               ; {code.lookupRingHeading} look up the ring heading
9EA7: 9D CC 02        STA     $02CC,X             ; {hard.workRam+2CC} store the heading into the phase cell

loc_9eaa:
9EAA: 60              RTS                         

; keep the climber's flip bit (bit6 of loc_283,x) in step with its segment
; depth loc_2b9,x while gate loc_111 is on: when bit6 is set clear it once
; depth reaches 0x0e; when bit6 is clear set it only while depth is 0.
keepClimberFlipBitByDepth:
9EAB: AD 11 01        LDA     $0111               ; {hard.workRam+111} read the tube-geometry / live-board flag
9EAE: F0 26           BEQ     $9ED6               ; {code.loc_9ed6} do nothing unless the board is live
9EB0: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} read the enemy state byte
9EB3: 29 40           AND     #$40                ; test the flip/turn-side bit
9EB5: F0 12           BEQ     $9EC9               ; {code.loc_9ec9} branch if the bit is clear
9EB7: BD B9 02        LDA     $02B9,X             ; {hard.workRam+2B9} bit set: read the segment depth
9EBA: C9 0E           CMP     #$0E                ; has it reached 0x0e
9EBC: 90 08           BCC     $9EC6               ; {code.loc_9ec6} keep the bit while depth is below 0x0e
9EBE: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} else reload state to clear the flip bit
9EC1: 29 BF           AND     #$BF                ; clear bit6
9EC3: 9D 83 02        STA     $0283,X             ; {hard.workRam+283} store it back

loc_9ec6:
9EC6: B8              CLV                         
9EC7: 50 0D           BVC     $9ED6               ; {code.loc_9ed6}

loc_9ec9:
9EC9: BD B9 02        LDA     $02B9,X             ; {hard.workRam+2B9} bit clear: read the segment depth
9ECC: D0 08           BNE     $9ED6               ; {code.loc_9ed6} leave it clear unless depth is 0
9ECE: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} at depth 0, reload state to set the flip bit
9ED1: 09 40           ORA     #$40                ; set bit6
9ED3: 9D 83 02        STA     $0283,X             ; {hard.workRam+283} store it back

loc_9ed6:
9ED6: 60              RTS                         

; look up a climber heading from the ring-direction table loc_3ee,y with
; bit7 forced on; when the caller's bit6 is set take the half-turn first
; -- index y=(y-1)&0x0f, value (loc_3ee,y+8)&0x0f.
lookupRingHeading:
9ED7: 29 40           AND     #$40                ; test the caller's turn-side bit
9ED9: F0 10           BEQ     $9EEB               ; {code.loc_9eeb} straight lookup when clear
9EDB: 88              DEY                         ; half-turn: step the index back one
9EDC: 98              TYA                         
9EDD: 29 0F           AND     #$0F                ; wrap the index mod 16
9EDF: A8              TAY                         
9EE0: B9 EE 03        LDA     $03EE,Y             ; {hard.workRam+3EE} read the ring-direction table
9EE3: 18              CLC                         
9EE4: 69 08           ADC     #$08                ; add a half turn (8)
9EE6: 29 0F           AND     #$0F                ; wrap mod 16
9EE8: B8              CLV                         
9EE9: 50 03           BVC     $9EEE               ; {code.loc_9eee}

loc_9eeb:
9EEB: B9 EE 03        LDA     $03EE,Y             ; {hard.workRam+3EE} straight case: read the ring-direction table

loc_9eee:
9EEE: 09 80           ORA     #$80                ; force bit7 on the heading
9EF0: 60              RTS                         

; per-slot pursuit mover: when loc_28a,x bit7 is set re-seek the subtract
; way (reverseEnemyLaneDepth with delta index 0x04) and dispatch on the
; returned high (maybeFireEnemyStep fire step for hi<0x80, else
; flipEnemyLaneRandomSide/flipEnemyLaneTowardTarget by loc_159 bit6); when
; clear advance the 16-bit depth (loc_29f,x += loc_164; loc_2df,x +=
; loc_169) clamped to floor loc_202, producing a fire carry only when
; loc_3ab!=0 and (loc_9f>=0x11 or hi>=0x20), then run maybeFireEnemyStep
; or pick flipEnemyLaneTowardTarget/flipEnemyLaneRandomSide by loc_159
; sign.
advanceEnemyPursuit:
9EF1: A0 04           LDY     #$04                ; select climb-delta table entry 4
9EF3: BD 8A 02        LDA     $028A,X             ; {hard.workRam+28A} read the enemy direction/state byte
9EF6: 30 4B           BMI     $9F43               ; {code.loc_9f43} take the re-seek path when the climb-direction bit is set
9EF8: BD 9F 02        LDA     $029F,X             ; {hard.workRam+29F} read the depth low byte
9EFB: 18              CLC                         
9EFC: 6D 64 01        ADC     $0164               ; {hard.workRam+164} add the per-segment climb-speed delta (low)
9EFF: 9D 9F 02        STA     $029F,X             ; {hard.workRam+29F} store the depth low
9F02: BD DF 02        LDA     $02DF,X             ; {hard.workRam+2DF} read the depth high byte
9F05: 6D 69 01        ADC     $0169               ; {hard.workRam+169} add the climb-speed delta (high) with carry
9F08: 9D DF 02        STA     $02DF,X             ; {hard.workRam+2DF} store the depth high
9F0B: CD 02 02        CMP     $0202               ; {hard.workRam+202} compare against the player-shot floor depth
9F0E: B0 09           BCS     $9F19               ; {code.loc_9f19} branch if at or above the floor
9F10: AD 02 02        LDA     $0202               ; {hard.workRam+202} else clamp depth to the floor
9F13: 9D DF 02        STA     $02DF,X             ; {hard.workRam+2DF} store the clamped depth
9F16: B8              CLV                         
9F17: 50 11           BVC     $9F2A               ; {code.loc_9f2a}

loc_9f19:
9F19: AC AB 03        LDY     $03AB               ; {hard.workRam+3AB} read the enemy-fire gate
9F1C: F0 0B           BEQ     $9F29               ; {code.loc_9f29} no fire step when the gate is closed
9F1E: A4 9F           LDY     $9F                 ; {hard.workRam+9F} read zero-page scratch $9f
9F20: C0 11           CPY     #$11                ; compare it against 0x11
9F22: B0 02           BCS     $9F26               ; {code.loc_9f26} arm the fire step when it is high enough
9F24: C9 20           CMP     #$20                ; else arm the fire step once depth reaches 0x20

loc_9f26:
9F26: B8              CLV                         
9F27: 50 01           BVC     $9F2A               ; {code.loc_9f2a}

loc_9f29:
9F29: 60              RTS                         

loc_9f2a:
9F2A: B0 11           BCS     $9F3D               ; {code.loc_9f3d} with the fire carry, take the fire step
9F2C: AD 59 01        LDA     $0159               ; {hard.workRam+159} read the fire/aim selector
9F2F: 10 06           BPL     $9F37               ; {code.loc_9f37} pick the turn side by its sign
9F31: 20 81 9F        JSR     $9F81               ; {code.flipEnemyLaneTowardTarget} flip the enemy toward the target lane
9F34: B8              CLV                         
9F35: 50 03           BVC     $9F3A               ; {code.loc_9f3a}

loc_9f37:
9F37: 20 8A 9F        JSR     $9F8A               ; {code.flipEnemyLaneRandomSide} else flip to a random side

loc_9f3a:
9F3A: B8              CLV                         
9F3B: 50 03           BVC     $9F40               ; {code.loc_9f40}

loc_9f3d:
9F3D: 20 5F 9F        JSR     $9F5F               ; {code.maybeFireEnemyStep} run the fire-gate step

loc_9f40:
9F40: B8              CLV                         
9F41: 50 1B           BVC     $9F5E               ; {code.loc_9f5e}

loc_9f43:
9F43: 20 99 9C        JSR     $9C99               ; {code.reverseEnemyLaneDepth} re-seek path: step depth in the lane direction (subtract way)
9F46: C9 80           CMP     #$80                ; test the returned depth high byte
9F48: 90 11           BCC     $9F5B               ; {code.loc_9f5b} low half -> fire step
9F4A: 2C 59 01        BIT     $0159               ; {hard.workRam+159} test the fire/aim selector bit6
9F4D: 50 06           BVC     $9F55               ; {code.loc_9f55}
9F4F: 20 81 9F        JSR     $9F81               ; {code.flipEnemyLaneTowardTarget} flip toward the target lane
9F52: B8              CLV                         
9F53: 50 03           BVC     $9F58               ; {code.loc_9f58}

loc_9f55:
9F55: 20 8A 9F        JSR     $9F8A               ; {code.flipEnemyLaneRandomSide} else flip to a random side

loc_9f58:
9F58: B8              CLV                         
9F59: 50 03           BVC     $9F5E               ; {code.loc_9f5e}

loc_9f5b:
9F5B: 20 5F 9F        JSR     $9F5F               ; {code.maybeFireEnemyStep} fire-gate step

loc_9f5e:
9F5E: 60              RTS                         

; per-slot fire gate: run a step only when the slot's fire bit loc_2df,x &
; 0x20 is set and a fresh POKEY draw $60DA >= threshold loc_15f; then
; route to flipEnemyLaneRandomSide when loc_159 bit6 is clear or the slot
; index is even, otherwise flipEnemyLaneTowardTarget.
maybeFireEnemyStep:
9F5F: BD DF 02        LDA     $02DF,X             ; {hard.workRam+2DF} read the slot's depth high byte
9F62: 29 20           AND     #$20                ; test the fire-enable bit
9F64: F0 1A           BEQ     $9F80               ; {code.loc_9f80} no step unless the bit is set
9F66: AD DA 60        LDA     $60DA               ; {hard.pokey2+A} draw a fresh secondary-RNG byte
9F69: CD 5F 01        CMP     $015F               ; {hard.workRam+15F} compare against the fire threshold
9F6C: 90 12           BCC     $9F80               ; {code.loc_9f80} no fire when the draw is under threshold
9F6E: 2C 59 01        BIT     $0159               ; {hard.workRam+159} test the fire/aim selector bit6
9F71: 50 0A           BVC     $9F7D               ; {code.loc_9f7d}
9F73: 8A              TXA                         
9F74: 4A              LSR     A                   ; test the slot index parity
9F75: 90 13           BCC     $9F8A               ; {code.flipEnemyLaneRandomSide} even slot -> flip to a random side
9F77: 20 81 9F        JSR     $9F81               ; {code.flipEnemyLaneTowardTarget} else flip toward the target lane
9F7A: B8              CLV                         
9F7B: 50 03           BVC     $9F80               ; {code.loc_9f80}

loc_9f7d:
9F7D: 20 8A 9F        JSR     $9F8A               ; {code.flipEnemyLaneRandomSide} flip to a random side

loc_9f80:
9F80: 60              RTS                         

; flip-step entry that re-derives slot x's turn side toward its target
; (faceEnemyTowardPlayerSegment) then toggles bit6 of loc_283,x
; (toggleEnemyTurnSide), then runs the shared tail: on a live board
; (loc_111!=0) flip bit6 by ring depth via loc_2b9,x, mark loc_10b=0x66,
; and continue into stepClimberSegmentAndHeading -- the flipper's lane-to-
; adjacent-lane hop.
flipEnemyLaneTowardTarget:
9F81: 20 67 9D        JSR     $9D67               ; {code.faceEnemyTowardPlayerSegment} re-derive this slot's turn side to face the player segment
9F84: 20 4F 9C        JSR     $9C4F               ; {code.toggleEnemyTurnSide} toggle the slot's turn-side bit
9F87: 4C 99 9F        JMP     $9F99               ; {code.loc_9f99} into the shared flip tail

; flip-step entry that reseeds slot x's turn side from a random bit ($60CA
; & 0x40) into bit6 of loc_283,x, then runs the shared tail: on a live
; board (loc_111!=0) flip bit6 again by ring depth (loc_2b9,x==0 when bit6
; set, >=0x0f when clear), mark loc_10b=0x66, and continue into
; stepClimberSegmentAndHeading.
flipEnemyLaneRandomSide:
9F8A: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} read the enemy state byte
9F8D: 29 BF           AND     #$BF                ; clear the turn-side bit
9F8F: 2C CA 60        BIT     $60CA               ; {hard.pokey1+A} test a primary-RNG bit (bit6)
9F92: 50 02           BVC     $9F96               ; {code.loc_9f96} leave the side clear on a 0 draw
9F94: 09 40           ORA     #$40                ; else set the turn-side bit from the random draw

loc_9f96:
9F96: 9D 83 02        STA     $0283,X             ; {hard.workRam+283} store the reseeded state

loc_9f99:
9F99: AD 11 01        LDA     $0111               ; {hard.workRam+111} shared tail: read the live-board flag
9F9C: F0 1E           BEQ     $9FBC               ; {code.loc_9fbc} skip the ring-depth flip on a dead board
9F9E: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} read the state byte
9FA1: 29 40           AND     #$40                ; test the turn-side bit
9FA3: D0 0A           BNE     $9FAF               ; {code.loc_9faf} branch by side
9FA5: BD B9 02        LDA     $02B9,X             ; {hard.workRam+2B9} side clear: read the segment
9FA8: C9 0F           CMP     #$0F                ; compare with 0x0f
9FAA: B0 08           BCS     $9FB4               ; {code.loc_9fb4} flip the bit only at the top edge (>=0x0f)
9FAC: B8              CLV                         
9FAD: 50 0D           BVC     $9FBC               ; {code.loc_9fbc}

loc_9faf:
9FAF: BD B9 02        LDA     $02B9,X             ; {hard.workRam+2B9} side set: read the segment
9FB2: D0 08           BNE     $9FBC               ; {code.loc_9fbc} flip only when the segment is 0

loc_9fb4:
9FB4: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} reload state to flip the turn-side bit
9FB7: 49 40           EOR     #$40                ; toggle bit6
9FB9: 9D 83 02        STA     $0283,X             ; {hard.workRam+283} store it back

loc_9fbc:
9FBC: A9 66           LDA     #$66                ; set the object-script cursor to 0x66
9FBE: 8D 0B 01        STA     $010B               ; {hard.workRam+10B} store the script cursor
9FC1: 4C 5F 9E        JMP     $9E5F               ; {code.stepClimberSegmentAndHeading} continue into the segment step

; advance climber slot x toward the rim while tracking each column's
; shallowest occupant: raise loc_10c, seed empty column loc_3ac,col to
; 0xf1, record a fresh minimum for the column (tagging loc_39a,col=0x80),
; clamp a too-shallow depth loc_2df,x (set bit7 of loc_28a,x,
; depth->0x20), or past the far limit call the deepest-column aim, repark
; depth at 0xf0 and (only when loc_3ab==0) rewrite flag loc_28a,x and lane
; loc_283,x.
advanceClimberTrackingColumnMin:
9FC4: A9 01           LDA     #$01                ; raise the script-branch flag
9FC6: 8D 0C 01        STA     $010C               ; {hard.workRam+10C} store 1 into the script-branch flag
9FC9: BC B9 02        LDY     $02B9,X             ; {hard.workRam+2B9} index by this enemy's segment/column
9FCC: B9 AC 03        LDA     $03AC,Y             ; {hard.workRam+3AC} read the column's shallowest-depth record
9FCF: D0 05           BNE     $9FD6               ; {code.loc_9fd6} skip seeding if it already holds a value
9FD1: A9 F1           LDA     #$F1                ; seed an empty column with 0xf1
9FD3: 99 AC 03        STA     $03AC,Y             ; {hard.workRam+3AC} store it

loc_9fd6:
9FD6: BD DF 02        LDA     $02DF,X             ; {hard.workRam+2DF} read this enemy's depth
9FD9: D9 AC 03        CMP     $03AC,Y             ; {hard.workRam+3AC} compare with the column's recorded minimum
9FDC: B0 08           BCS     $9FE6               ; {code.loc_9fe6} skip if not a new shallowest
9FDE: 99 AC 03        STA     $03AC,Y             ; {hard.workRam+3AC} record the new column minimum
9FE1: A9 80           LDA     #$80                ; tag the column as flagged
9FE3: 99 9A 03        STA     $039A,Y             ; {hard.workRam+39A} store the lane-target flag

loc_9fe6:
9FE6: BD DF 02        LDA     $02DF,X             ; {hard.workRam+2DF} read the depth again
9FE9: C9 20           CMP     #$20                ; is it too shallow (below 0x20)
9FEB: B0 10           BCS     $9FFD               ; {code.loc_9ffd} branch if deep enough
9FED: BD 8A 02        LDA     $028A,X             ; {hard.workRam+28A} too shallow: read the direction byte
9FF0: 09 80           ORA     #$80                ; set the climb-direction bit -- turn it around
9FF2: 9D 8A 02        STA     $028A,X             ; {hard.workRam+28A} store it back
9FF5: A9 20           LDA     #$20                ; clamp depth to 0x20
9FF7: 9D DF 02        STA     $02DF,X             ; {hard.workRam+2DF} store the clamped depth
9FFA: B8              CLV                         
9FFB: 50 2A           BVC     $A027               ; {code.loc_a027}

loc_9ffd:
9FFD: C9 F2           CMP     #$F2                ; past the far limit (>=0xf2)
9FFF: 90 26           BCC     $A027               ; {code.loc_a027} branch out if still within the tube
A001: 20 28 A0        JSR     $A028               ; {code.aimClimberAtDeepestColumn} aim the enemy at the deepest column
A004: A9 F0           LDA     #$F0                ; repark depth at the far wall 0xf0
A006: 9D DF 02        STA     $02DF,X             ; {hard.workRam+2DF} store it
A009: AD AB 03        LDA     $03AB               ; {hard.workRam+3AB} read the fire gate
A00C: D0 19           BNE     $A027               ; {code.loc_a027} skip the rewrite while the gate is open
A00E: BD 8A 02        LDA     $028A,X             ; {hard.workRam+28A} rewrite the direction byte
A011: 29 FC           AND     #$FC                ; clear its low 2 bits
A013: 09 01           ORA     #$01                ; set kind to 1
A015: 9D 8A 02        STA     $028A,X             ; {hard.workRam+28A} store it back
A018: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} rewrite the enemy state byte
A01B: 29 F8           AND     #$F8                ; clear the low 3 bits
A01D: 09 02           ORA     #$02                ; set segment kind to 2
A01F: 9D 83 02        STA     $0283,X             ; {hard.workRam+283} store it back
A022: A9 00           LDA     #$00                
A024: 8D 0C 01        STA     $010C               ; {hard.workRam+10C} clear the script-branch flag

loc_a027:
A027: 60              RTS                         

; aim a climber slot at the deepest tube column: scan the 16-column depth
; table loc_3ac from a POKEY2-random start $60DA&0x0f (empty column counts
; as maximal 0xff, last column skipped while loc_111 nonzero) keeping the
; max in loc_2d and its column in loc_29, then set the slot's target
; segment loc_2b9,x to the winner, successor loc_2cc,x=(winner+1)&0x0f,
; and clear bit7 of loc_28a,x.
aimClimberAtDeepestColumn:
A028: A9 00           LDA     #$00                
A02A: 85 2D           STA     $2D                 ; {hard.workRam+2D} clear the running-max holder
A02C: A9 0F           LDA     #$0F                
A02E: 8D 40 01        STA     $0140               ; {hard.workRam+140} set the 16-column scan countdown
A031: AD DA 60        LDA     $60DA               ; {hard.pokey2+A} draw a secondary-RNG start
A034: 29 0F           AND     #$0F                ; reduce to a column index 0..15
A036: A8              TAY                         

loc_a037:
A037: C0 0F           CPY     #$0F                ; is this the last column
A039: D0 05           BNE     $A040               ; {code.loc_a040} skip the last-column special case
A03B: AD 11 01        LDA     $0111               ; {hard.workRam+111} read the live-board flag
A03E: D0 0F           BNE     $A04F               ; {code.loc_a04f} skip the last column while the board is live

loc_a040:
A040: B9 AC 03        LDA     $03AC,Y             ; {hard.workRam+3AC} read the column's recorded depth
A043: D0 02           BNE     $A047               ; {code.loc_a047} an empty column...
A045: A9 FF           LDA     #$FF                ; ...counts as maximal depth 0xff

loc_a047:
A047: C5 2D           CMP     $2D                 ; {hard.workRam+2D} compare against the running max
A049: 90 04           BCC     $A04F               ; {code.loc_a04f} keep the previous max if not deeper
A04B: 85 2D           STA     $2D                 ; {hard.workRam+2D} record the new max depth
A04D: 84 29           STY     $29                 ; {hard.workRam+29} record its column

loc_a04f:
A04F: 88              DEY                         ; step to the previous column
A050: 10 02           BPL     $A054               ; {code.loc_a054} wrap...
A052: A0 0F           LDY     #$0F                ; ...back to column 15

loc_a054:
A054: CE 40 01        DEC     $0140               ; {hard.workRam+140} decrement the scan countdown
A057: 10 DE           BPL     $A037               ; {code.loc_a037} loop over all 16 columns
A059: A5 29           LDA     $29                 ; {hard.workRam+29} take the winning column
A05B: 9D B9 02        STA     $02B9,X             ; {hard.workRam+2B9} set the enemy's target segment
A05E: 18              CLC                         
A05F: 69 01           ADC     #$01                ; successor column = winner + 1
A061: 29 0F           AND     #$0F                ; wrap mod 16
A063: 9D CC 02        STA     $02CC,X             ; {hard.workRam+2CC} store the successor heading
A066: BD 8A 02        LDA     $028A,X             ; {hard.workRam+28A} read the direction byte
A069: 29 7F           AND     #$7F                ; clear the climb-direction bit -- aim inward
A06B: 9D 8A 02        STA     $028A,X             ; {hard.workRam+28A} store it back
A06E: 60              RTS                         

; retire the enemy in slot y and optionally split it: clear loc_2df,y,
; drop per-type loc_109 (when depth==loc_202 and lane loc_283,y&7 != 4) or
; total loc_108, drop per-lane loc_142; then when the replacement gate
; loc_28a,y&3 is armed, seat draw cells loc_2b/loc_2a, build the
; coordinate list via setupEnemyCoordList, seed loc_10b/loc_10a, spawn a
; replacement via spawnClimberInFreeSlot, and if it took, spawn a mirrored
; second one.
retireEnemyAndSpawnSplit:
A06F: B9 DF 02        LDA     $02DF,Y             ; {hard.workRam+2DF} read the retiring enemy's depth
A072: 85 29           STA     $29                 ; {hard.workRam+29} stash it
A074: CD 02 02        CMP     $0202               ; {hard.workRam+202} compare with the player-shot depth
A077: D0 0F           BNE     $A088               ; {code.loc_a088} branch to the total-count path unless at that depth
A079: B9 83 02        LDA     $0283,Y             ; {hard.workRam+283} read the enemy state byte
A07C: 29 07           AND     #$07                ; isolate the segment kind
A07E: C9 04           CMP     #$04                ; is it segment kind 4
A080: F0 06           BEQ     $A088               ; {code.loc_a088} if so, drop the total count instead
A082: CE 09 01        DEC     $0109               ; {hard.workRam+109} drop the per-type live-enemy count
A085: B8              CLV                         
A086: 50 03           BVC     $A08B               ; {code.loc_a08b}

loc_a088:
A088: CE 08 01        DEC     $0108               ; {hard.workRam+108} drop the total live-enemy count

loc_a08b:
A08B: A9 00           LDA     #$00                
A08D: 99 DF 02        STA     $02DF,Y             ; {hard.workRam+2DF} clear the slot depth -- retire it
A090: B9 83 02        LDA     $0283,Y             ; {hard.workRam+283} read the state byte
A093: 29 07           AND     #$07                ; isolate the segment kind
A095: 86 35           STX     $35                 ; {hard.workRam+35} save the caller's slot index
A097: AA              TAX                         
A098: DE 42 01        DEC     $0142,X             ; {hard.workRam+142} drop that column's active-enemy counter
A09B: A6 35           LDX     $35                 ; {hard.workRam+35} restore the slot index
A09D: B9 8A 02        LDA     $028A,Y             ; {hard.workRam+28A} read the direction byte
A0A0: 29 03           AND     #$03                ; isolate the replacement-gate bits
A0A2: F0 52           BEQ     $A0F6               ; {code.loc_a0f6} no split when the gate is 0
A0A4: 38              SEC                         
A0A5: E9 01           SBC     #$01                ; decode the split count
A0A7: C9 02           CMP     #$02                ; is it 2
A0A9: D0 02           BNE     $A0AD               ; {code.loc_a0ad}
A0AB: A9 04           LDA     #$04                ; remap 2 to 4

loc_a0ad:
A0AD: 85 2B           STA     $2B                 ; {hard.workRam+2B} seat the split draw cell
A0AF: B9 B9 02        LDA     $02B9,Y             ; {hard.workRam+2B9} read the enemy's segment
A0B2: 38              SEC                         
A0B3: E9 01           SBC     #$01                ; step it back one
A0B5: 29 0F           AND     #$0F                ; wrap mod 16
A0B7: C9 0F           CMP     #$0F                ; did it wrap to 0x0f
A0B9: 90 07           BCC     $A0C2               ; {code.loc_a0c2} skip the wrap fix-up if not
A0BB: 2C 11 01        BIT     $0111               ; {hard.workRam+111} test the live-board flag bit7
A0BE: 10 02           BPL     $A0C2               ; {code.loc_a0c2} skip unless the wrap bit governs
A0C0: A9 00           LDA     #$00                ; clamp the segment to 0

loc_a0c2:
A0C2: 85 2A           STA     $2A                 ; {hard.workRam+2A} seat the split lane cell
A0C4: 20 07 9B        JSR     $9B07               ; {code.setupEnemyCoordList} build the coordinate list for the replacement
A0C7: A5 2D           LDA     $2D                 ; {hard.workRam+2D} take the list-high byte
A0C9: 8D 0B 01        STA     $010B               ; {hard.workRam+10B} seed the object-script cursor
A0CC: CE 0B 01        DEC     $010B               ; {hard.workRam+10B} step it back one
A0CF: A9 00           LDA     #$00                
A0D1: 8D 0A 01        STA     $010A               ; {hard.workRam+10A} clear the script sub-cursor
A0D4: 20 4D 99        JSR     $994D               ; {code.spawnClimberInFreeSlot} spawn the replacement climber in a free slot
A0D7: F0 1D           BEQ     $A0F6               ; {code.loc_a0f6} done if no free slot took it
A0D9: A5 2A           LDA     $2A                 ; {hard.workRam+2A} took: read the split lane
A0DB: 18              CLC                         
A0DC: 69 02           ADC     #$02                ; offset the mirror lane by 2
A0DE: 29 0F           AND     #$0F                ; wrap mod 16
A0E0: C9 0F           CMP     #$0F                ; did it land on 0x0f
A0E2: D0 07           BNE     $A0EB               ; {code.loc_a0eb} skip the fix-up if not
A0E4: 2C 11 01        BIT     $0111               ; {hard.workRam+111} test the live-board bit7
A0E7: 10 02           BPL     $A0EB               ; {code.loc_a0eb} skip unless it governs
A0E9: A9 0E           LDA     #$0E                ; clamp the mirror lane to 0x0e

loc_a0eb:
A0EB: 85 2A           STA     $2A                 ; {hard.workRam+2A} seat the mirror lane
A0ED: A5 2B           LDA     $2B                 ; {hard.workRam+2B}
A0EF: 09 40           ORA     #$40                ; tag the mirror as the second of the pair
A0F1: 85 2B           STA     $2B                 ; {hard.workRam+2B} store it
A0F3: 20 4D 99        JSR     $994D               ; {code.spawnClimberInFreeSlot} spawn the mirrored second climber

loc_a0f6:
A0F6: 60              RTS                         

; ---- $A0F7-$A18E: data ----
A0F7: 0C 0E 1A 06 00 06 FF 0C 00 06 06 02 08 0C 00 08
A107: 0C 12 00 14 04 06 11 06 0A 0C 00 12 00 14 0C 04
A117: 06 1B 06 18 0C 00 02 02 12 00 14 0C 04 06 28 00
A127: 08 27 16 02 03 12 00 14 0C 04 06 35 00 08 34 16
A137: 06 23 02 04 18 00 08 43 12 00 10 B3 14 1A 41 08
A147: 4B 06 48 00 0C 1C 1A 52 12 00 0C 14 1A 52 00 06
A157: 5A 1E 20 00 06 60 00 02 03 20 00 08 68 14 1A 60
A167: 06 65 10 B2 22 00 08 73 26 1A 7E 22 00 06 77 24
A177: 12 00 14 1A 71 06 80 24 16 12 00 0C 14 04 06 89
A187: 02 04 00 0C 08 91 06 86

; advance every active shot slot (0x0b..0): slots >=8 integrate a 16-bit
; velocity loc_2e6,x/loc_2d3,x by loc_120/loc_118 and retire (drop loc_a6,
; finalize via primeTopObjectOnTargetMatch, clear loc_2d3,x) when the new
; high falls below the floor loc_202; slots <8 step counter loc_2d3,x by
; 0x09 (less 4 when loc_2f2,x is flagged), resolve via
; advanceShotAndScoreLaneHit, and clear (drop loc_135) at the far limit
; >=0xf0.
stepActiveShots:
A18F: A2 0B           LDX     #$0B                ; start at shot slot 0x0b
A191: 86 37           STX     $37                 ; {hard.workRam+37} seat the slot loop index

loc_a193:
A193: A6 37           LDX     $37                 ; {hard.workRam+37} reload the slot index (loop head)
A195: BD D3 02        LDA     $02D3,X             ; {hard.workRam+2D3} read the shot slot's counter/state
A198: F0 45           BEQ     $A1DF               ; {code.loc_a1df} skip an empty slot
A19A: E0 08           CPX     #$08                ; slots 8 and above...
A19C: B0 22           BCS     $A1C0               ; {code.loc_a1c0} ...take the velocity-integration path
A19E: 69 09           ADC     #$09                ; near slot: step the counter by 0x09
A1A0: BC F2 02        LDY     $02F2,X             ; {hard.workRam+2F2} read the slot's hit tally/flag
A1A3: F0 03           BEQ     $A1A8               ; {code.loc_a1a8} if it is flagged...
A1A5: 38              SEC                         
A1A6: E9 04           SBC     #$04                ; ...take 4 back off the step

loc_a1a8:
A1A8: 9D D3 02        STA     $02D3,X             ; {hard.workRam+2D3} store the stepped counter
A1AB: 20 FA A1        JSR     $A1FA               ; {code.advanceShotAndScoreLaneHit} advance the shot and score a lane hit
A1AE: BD D3 02        LDA     $02D3,X             ; {hard.workRam+2D3} reread the counter
A1B1: C9 F0           CMP     #$F0                ; past the far limit (>=0xf0)
A1B3: 90 08           BCC     $A1BD               ; {code.loc_a1bd} branch if still in the tube
A1B5: CE 35 01        DEC     $0135               ; {hard.workRam+135} drop the active-object count
A1B8: A9 00           LDA     #$00                
A1BA: 9D D3 02        STA     $02D3,X             ; {hard.workRam+2D3} clear the slot

loc_a1bd:
A1BD: B8              CLV                         
A1BE: 50 1F           BVC     $A1DF               ; {code.loc_a1df}

loc_a1c0:
A1C0: BD E6 02        LDA     $02E6,X             ; {hard.workRam+2E6} far slot: read the velocity accumulator low
A1C3: 18              CLC                         
A1C4: 6D 20 01        ADC     $0120               ; {hard.workRam+120} add the per-frame velocity low
A1C7: 9D E6 02        STA     $02E6,X             ; {hard.workRam+2E6} store it
A1CA: BD D3 02        LDA     $02D3,X             ; {hard.workRam+2D3} read the position high byte
A1CD: 6D 18 01        ADC     $0118               ; {hard.workRam+118} add the velocity high with carry
A1D0: CD 02 02        CMP     $0202               ; {hard.workRam+202} compare against the shot-depth floor
A1D3: B0 07           BCS     $A1DC               ; {code.loc_a1dc} keep it if still at or above the floor
A1D5: C6 A6           DEC     $A6                 ; {hard.workRam+A6} else drop the live-climber count
A1D7: 20 E4 A1        JSR     $A1E4               ; {code.primeTopObjectOnTargetMatch} finalize the top object on a target match
A1DA: A9 00           LDA     #$00                

loc_a1dc:
A1DC: 9D D3 02        STA     $02D3,X             ; {hard.workRam+2D3} clear the slot

loc_a1df:
A1DF: C6 37           DEC     $37                 ; {hard.workRam+37} step to the previous slot
A1E1: 10 B0           BPL     $A193               ; {code.loc_a193} loop over all shot slots
A1E3: 60              RTS                         

; prime the top-priority object only when the live byte loc_200 matches
; slot x's target loc_2ad,x and ready flag loc_201 bit7 is clear -- run
; the prime and latch loc_201=0x81.
primeTopObjectOnTargetMatch:
A1E4: AD 00 02        LDA     $0200               ; {hard.workRam+200} read the player rim segment
A1E7: DD AD 02        CMP     $02AD,X             ; {hard.workRam+2AD} compare with the slot's target segment
A1EA: D0 0D           BNE     $A1F9               ; {code.loc_a1f9} bail unless they match
A1EC: AD 01 02        LDA     $0201               ; {hard.workRam+201} read the player fine-angle/ready cell
A1EF: 30 08           BMI     $A1F9               ; {code.loc_a1f9} bail if the ready bit (bit7) is set
A1F1: 20 4B A3        JSR     $A34B               ; {code.primeTopPriorityObject} prime the top-priority object
A1F4: A9 81           LDA     #$81                
A1F6: 8D 01 02        STA     $0201               ; {hard.workRam+201} latch the ready flag 0x81

loc_a1f9:
A1F9: 60              RTS                         

; advance shot slot x's counter loc_2d3,x toward the per-lane target-depth
; loc_3ac,y (y=loc_2ad,x); on reaching it shrink/clear loc_3ac,y, bump the
; hit tally loc_2f2,x, flag the target loc_39a,y=0xc0, chime
; (requestSegmentHitSound) and award (addBcdScoreAndAwardAtThreshold),
; returning the live slot; a second hit spends the shot (clear loc_2d3,x,
; drop the shot count loc_135).
advanceShotAndScoreLaneHit:
A1FA: BC AD 02        LDY     $02AD,X             ; {hard.workRam+2AD} index by the shot's target segment
A1FD: B9 AC 03        LDA     $03AC,Y             ; {hard.workRam+3AC} read that lane's target depth
A200: F0 3C           BEQ     $A23E               ; {code.loc_a23e} nothing to hit if the lane depth is 0
A202: BD D3 02        LDA     $02D3,X             ; {hard.workRam+2D3} read the shot's counter
A205: D9 AC 03        CMP     $03AC,Y             ; {hard.workRam+3AC} compare with the lane target depth
A208: 90 25           BCC     $A22F               ; {code.loc_a22f} not yet reached -> check the tally
A20A: C9 F0           CMP     #$F0                ; reached: past the far limit
A20C: 90 02           BCC     $A210               ; {code.loc_a210} branch if within the tube
A20E: A9 00           LDA     #$00                ; else zero the value to store

loc_a210:
A210: 99 AC 03        STA     $03AC,Y             ; {hard.workRam+3AC} shrink or clear the lane target depth
A213: FE F2 02        INC     $02F2,X             ; {hard.workRam+2F2} bump the shot's hit tally
A216: A9 C0           LDA     #$C0                
A218: 99 9A 03        STA     $039A,Y             ; {hard.workRam+39A} flag the hit lane (0xc0)
A21B: 20 F6 CC        JSR     $CCF6               ; {code.requestSegmentHitSound} request the segment-hit sound
A21E: A2 FF           LDX     #$FF                ; seat the award parameters
A220: A9 00           LDA     #$00                
A222: 85 2A           STA     $2A                 ; {hard.workRam+2A}
A224: 85 2B           STA     $2B                 ; {hard.workRam+2B}
A226: A9 01           LDA     #$01                
A228: 85 29           STA     $29                 ; {hard.workRam+29}
A22A: 20 6C CA        JSR     $CA6C               ; {code.addBcdScoreAndAwardAtThreshold} add the BCD score and award at the threshold
A22D: A6 37           LDX     $37                 ; {hard.workRam+37} restore the shot slot index

loc_a22f:
A22F: BD F2 02        LDA     $02F2,X             ; {hard.workRam+2F2} read the hit tally
A232: C9 02           CMP     #$02                ; a second hit
A234: 90 08           BCC     $A23E               ; {code.loc_a23e} not yet -> keep the shot live
A236: A9 00           LDA     #$00                
A238: 9D D3 02        STA     $02D3,X             ; {hard.workRam+2D3} spend the shot -- clear it
A23B: CE 35 01        DEC     $0135               ; {hard.workRam+135} drop the active-object count

loc_a23e:
A23E: 60              RTS                         

; spawn a new entity into a free slot: bail if 0x201 negative; form a gate
; (0x4d&0x10 when 0x5 negative, else 0x29 from 0x106 plus one per live
; 0x2db slot whose 0x2b5 sits within 1 of 0x200); on a nonzero gate scan
; 0x2d3 (x=7..0) for the first zero slot, seed it across
; 0x2d3/0x2ad/0x2c0/0x2f2 from 0x202/0x200/0x201/0, bump live count 0x135,
; and fire requestEnemySpawnSound + resolveSlotProximityInteractions.
spawnEntityIntoFreeSlot:
A23F: AD 01 02        LDA     $0201               ; {hard.workRam+201} read the player fine-angle/ready cell
A242: 30 61           BMI     $A2A5               ; {code.loc_a2a5} bail while its bit7 is set
A244: A5 05           LDA     $05                 ; {hard.workRam+5} read the game status byte
A246: 30 28           BMI     $A270               ; {code.loc_a270} take the fire-button path during active play
A248: AD 06 01        LDA     $0106               ; {hard.workRam+106} read the moving-spike active flag
A24B: 85 29           STA     $29                 ; {hard.workRam+29} seed the gate accumulator with it
A24D: A2 0A           LDX     #$0A                ; scan slots 0x0a..0

loc_a24f:
A24F: BD DB 02        LDA     $02DB,X             ; {hard.workRam+2DB} read the slot's live byte (loop head)
A252: F0 14           BEQ     $A268               ; {code.loc_a268} skip an empty slot
A254: BD B5 02        LDA     $02B5,X             ; {hard.workRam+2B5} read the slot's segment
A257: 38              SEC                         
A258: ED 00 02        SBC     $0200               ; {hard.workRam+200} distance from the player segment
A25B: 10 05           BPL     $A262               ; {code.loc_a262} take the absolute value...
A25D: 49 FF           EOR     #$FF                
A25F: 18              CLC                         
A260: 69 01           ADC     #$01                ; ...negate if below

loc_a262:
A262: C9 02           CMP     #$02                ; within 1 segment of the player
A264: B0 02           BCS     $A268               ; {code.loc_a268} skip if farther
A266: E6 29           INC     $29                 ; {hard.workRam+29} count this near slot into the gate

loc_a268:
A268: CA              DEX                         
A269: 10 E4           BPL     $A24F               ; {code.loc_a24f} loop over the slots
A26B: A5 29           LDA     $29                 ; {hard.workRam+29} take the gate value
A26D: B8              CLV                         
A26E: 50 04           BVC     $A274               ; {code.loc_a274}

loc_a270:
A270: A5 4D           LDA     $4D                 ; {hard.workRam+4D} fire-button path: read the debounced input
A272: 29 10           AND     #$10                ; isolate the fire button bit

loc_a274:
A274: F0 2F           BEQ     $A2A5               ; {code.loc_a2a5} bail if the gate is 0 / button not held
A276: A2 07           LDX     #$07                ; scan slots 7..0 for a free one

loc_a278:
A278: BD D3 02        LDA     $02D3,X             ; {hard.workRam+2D3} read the slot state (loop head)
A27B: D0 25           BNE     $A2A2               ; {code.loc_a2a2} skip an occupied slot
A27D: EE 35 01        INC     $0135               ; {hard.workRam+135} take it: bump the active-object count
A280: AD 02 02        LDA     $0202               ; {hard.workRam+202} seed the slot depth from the player-shot depth
A283: 9D D3 02        STA     $02D3,X             ; {hard.workRam+2D3}
A286: AD 00 02        LDA     $0200               ; {hard.workRam+200} seed the target segment from the player segment
A289: 9D AD 02        STA     $02AD,X             ; {hard.workRam+2AD}
A28C: AD 01 02        LDA     $0201               ; {hard.workRam+201} seed the fine angle from the player fine-angle
A28F: 9D C0 02        STA     $02C0,X             ; {hard.workRam+2C0}
A292: A9 00           LDA     #$00                
A294: 9D F2 02        STA     $02F2,X             ; {hard.workRam+2F2} clear the slot's hit tally
A297: 20 EA CC        JSR     $CCEA               ; {code.requestEnemySpawnSound} request the enemy-spawn sound
A29A: AD 02 02        LDA     $0202               ; {hard.workRam+202} read the player-shot depth
A29D: 20 63 A4        JSR     $A463               ; {code.resolveSlotProximityInteractions} resolve interactions with nearby slots
A2A0: A2 00           LDX     #$00                

loc_a2a2:
A2A2: CA              DEX                         
A2A3: 10 D3           BPL     $A278               ; {code.loc_a278} loop -- and exit after a take

loc_a2a5:
A2A5: 60              RTS                         

; spawn climbers from the seven source slots each frame: skip while
; loc_201 bit7 set; for each armed slot (loc_28a,x bit6) with depth
; loc_2df,x>=0x30 whose timer loc_2a6,x underflows and whose POKEY roll
; $60CA beats the per-wave gate $A304[loc_a6], copy
; depth/segment/successor into the first empty destination loc_2db,y,
; reseed the timer from loc_119, cue the sound, and bump live count
; loc_a6.
spawnClimbersFromSourceSlots:
A2A6: AD 01 02        LDA     $0201               ; {hard.workRam+201} read the player rotation / object-pending flag
A2A9: 30 58           BMI     $A303               ; {code.loc_a303} skip the whole hatch pass while the pending flag (bit7) is set
A2AB: A2 06           LDX     #$06                ; index the top source enemy slot (6..0)

loc_a2ad:
A2AD: BD DF 02        LDA     $02DF,X             ; {hard.workRam+2DF} read the source slot's tube depth
A2B0: F0 4E           BEQ     $A300               ; {code.loc_a300} skip an empty slot
A2B2: C9 30           CMP     #$30                
A2B4: 90 4A           BCC     $A300               ; {code.loc_a300} skip unless the source sits deep enough down the tube to hatch
A2B6: BD 8A 02        LDA     $028A,X             ; {hard.workRam+28A} read the slot's direction/state byte
A2B9: 29 40           AND     #$40                
A2BB: F0 43           BEQ     $A300               ; {code.loc_a300} skip unless the slot is an armed source (bit6)
A2BD: DE A6 02        DEC     $02A6,X             ; {hard.workRam+2A6} tick the source's emit timer down
A2C0: 10 3E           BPL     $A300               ; {code.loc_a300} fire only on the tick the timer underflows
A2C2: FE A6 02        INC     $02A6,X             ; {hard.workRam+2A6} restore the underflow tick to the timer
A2C5: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} read the slot flags
A2C8: 29 80           AND     #$80                
A2CA: D0 34           BNE     $A300               ; {code.loc_a300} skip a slot flagged done (bit7)
A2CC: AD CA 60        LDA     $60CA               ; {hard.pokey1+A} read the RNG
A2CF: A4 A6           LDY     $A6                 ; {hard.workRam+A6} index the per-wave spawn-rate gate by the live-enemy count
A2D1: D9 04 A3        CMP     $A304,Y             ; {hard.rom+1304} gate the hatch against the per-wave spawn-rate table
A2D4: 90 2A           BCC     $A300               ; {code.loc_a300} a low roll blocks the hatch -- denser waves emit less often
A2D6: AC 1A 01        LDY     $011A               ; {hard.workRam+11A} start the free flyer-slot scan at the difficulty-clamped top index

loc_a2d9:
A2D9: B9 DB 02        LDA     $02DB,Y             ; {hard.workRam+2DB} read a candidate flyer destination slot
A2DC: D0 1F           BNE     $A2FD               ; {code.loc_a2fd} skip an occupied destination slot
A2DE: BD DF 02        LDA     $02DF,X             ; {hard.workRam+2DF} read the source depth
A2E1: 99 DB 02        STA     $02DB,Y             ; {hard.workRam+2DB} seed the new flyer's depth from the source
A2E4: BD B9 02        LDA     $02B9,X             ; {hard.workRam+2B9} read the source segment
A2E7: 99 B5 02        STA     $02B5,Y             ; {hard.workRam+2B5} copy the source segment into the flyer
A2EA: BD CC 02        LDA     $02CC,X             ; {hard.workRam+2CC} read the source phase
A2ED: 99 C8 02        STA     $02C8,Y             ; {hard.workRam+2C8} copy the source phase into the flyer
A2F0: AD 19 01        LDA     $0119               ; {hard.workRam+119} load the source timer reload period
A2F3: 9D A6 02        STA     $02A6,X             ; {hard.workRam+2A6} reload the source's emit timer
A2F6: 20 BD CC        JSR     $CCBD               ; {code.gateSound8f} cue the hatch sound
A2F9: E6 A6           INC     $A6                 ; {hard.workRam+A6} count the new enemy
A2FB: A0 00           LDY     #$00                ; end the free-slot scan once the flyer is seated

loc_a2fd:
A2FD: 88              DEY                         
A2FE: 10 D9           BPL     $A2D9               ; {code.loc_a2d9} step to the next destination slot

loc_a300:
A300: CA              DEX                         ; next source slot
A301: 10 AA           BPL     $A2AD               ; {code.loc_a2ad} loop back over the source slots

loc_a303:
A303: 60              RTS                         

; ---- $A304-$A308: data ----
A304: 00 E0 F0 FA FF

; spawn the lane enemy in slot X and award: mark slot active
; (0x2f2,x=0xff), seed 0x2d from the (Y-4)-indexed geometry byte 0x2b9,
; clamp POKEY random 0x60da low 3 bits to under 3 (else 0), run the
; insert/retire chain insertObjectFromSlotDepth+retireEnemyAndSpawnSplit
; with clamp+2, then award via addBcdScoreAndAwardAtThreshold indexed by
; clamp+5.
spawnLaneEnemyAndAward:
A309: 86 37           STX     $37                 ; {hard.workRam+37} stash the slot index for the insert/retire chain
A30B: A9 FF           LDA     #$FF                
A30D: 9D F2 02        STA     $02F2,X             ; {hard.workRam+2F2} mark enemy slot X live
A310: 98              TYA                         
A311: 38              SEC                         
A312: E9 04           SBC     #$04                ; convert the 4-based slot handle to a 0-based lane index
A314: A8              TAY                         
A315: B9 B9 02        LDA     $02B9,Y             ; {hard.workRam+2B9} read the lane's geometry byte
A318: 85 2D           STA     $2D                 ; {hard.workRam+2D} latch the lane geometry for the object inserter
A31A: AD DA 60        LDA     $60DA               ; {hard.pokey2+A} draw a random variant seed
A31D: 29 07           AND     #$07                
A31F: C9 03           CMP     #$03                ; keep the variant only in 0..2
A321: 90 02           BCC     $A325               ; {code.loc_a325} values 0..2 pass through
A323: A9 00           LDA     #$00                ; fold a 3..7 variant to 0

loc_a325:
A325: 48              PHA                         
A326: 18              CLC                         
A327: 69 02           ADC     #$02                ; depth class = variant + 2
A329: 20 CA A3        JSR     $A3CA               ; {code.insertObjectFromSlotDepth} place the object at the variant's depth class
A32C: 20 6F A0        JSR     $A06F               ; {code.retireEnemyAndSpawnSplit} fold the prior lane occupant and spawn any split
A32F: 68              PLA                         
A330: 18              CLC                         
A331: 69 05           ADC     #$05                ; score tier = variant + 5
A333: AA              TAX                         
A334: 20 6C CA        JSR     $CA6C               ; {code.addBcdScoreAndAwardAtThreshold} award the variant's score tier and grant a bonus life at the threshold
A337: A6 37           LDX     $37                 ; {hard.workRam+37} restore the slot index
A339: 60              RTS                         

; insert a type-5 object through the shared tail, then step the pending
; counter loc_201 down one.
insertType5AndDrainPending:
A33A: A9 05           LDA     #$05                ; spawn a fixed type-5 object
A33C: 20 52 A3        JSR     $A352               ; {code.insertObjectAndSignalReady} seat it through the shared insert-and-signal-ready tail
A33F: CE 01 02        DEC     $0201               ; {hard.workRam+201} draw the pending-spawn counter down by one
A342: 60              RTS                         

; insert a type-1 object after stamping head flag loc_13b with 0x09.
insertObjectHeadTag9:
A343: A9 09           LDA     #$09                ; preset the head-flag tag to 0x09
A345: D0 06           BNE     $A34D               ; {code.insertType1WithHeadFlag}

; insert a type-1 object after stamping head flag loc_13b with 0x07.
insertObjectHeadTag7:
A347: A9 07           LDA     #$07                ; alternate entry: preset the head-flag tag to 0x07
A349: D0 02           BNE     $A34D               ; {code.insertType1WithHeadFlag}

; prime a fresh top-priority object: stamp head flag loc_13b=0xff and run
; the type-1 insert.
primeTopPriorityObject:
A34B: A9 FF           LDA     #$FF                ; top-priority head flag 0xff

; insert a type-1 object after stamping the head flag loc_13b with the
; caller's value, then run the shared insert tail.
insertType1WithHeadFlag:
A34D: 8D 3B 01        STA     $013B               ; {hard.workRam+13B} stamp the object's head / animation-phase flag
A350: A9 01           LDA     #$01                ; object type 1

; insert an object and signal the spawn ready (shared insert tail): seat
; the type byte loc_2c, copy source loc_29 from loc_202 and target loc_2d
; from loc_200, fire the sound gate, insert into the 8-slot table, then
; raise ready flags loc_201=0x81 and loc_13c=0x01.
insertObjectAndSignalReady:
A352: 85 2C           STA     $2C                 ; {hard.workRam+2C} seat the object type byte
A354: AD 02 02        LDA     $0202               ; {hard.workRam+202} read the current shot depth
A357: 85 29           STA     $29                 ; {hard.workRam+29} source = current shot depth
A359: AD 00 02        LDA     $0200               ; {hard.workRam+200} read the player segment
A35C: 85 2D           STA     $2D                 ; {hard.workRam+2D} target = player segment
A35E: 20 B0 CC        JSR     $CCB0               ; {code.gateSound5f} fire the spawn sound
A361: 20 D6 A3        JSR     $A3D6               ; {code.insertTimedObject} seat the object in the eight-slot table
A364: A9 81           LDA     #$81                
A366: 8D 01 02        STA     $0201               ; {hard.workRam+201} raise the spawn-ready flag (bit7 pending)
A369: A9 01           LDA     #$01                
A36B: 8D 3C 01        STA     $013C               ; {hard.workRam+13C} arm the object's animation timer
A36E: 60              RTS                         

; retire the object in slot Y: cue the sound, stage source loc_29 from
; loc_2db,y and target loc_2d from loc_2b5,y, re-insert a zeroed object,
; clear the slot loc_2db,y, drop live count loc_a6, and flag lane X spent
; with loc_2f2,x=0xff.
retireSpawnedObject:
A36F: 20 C1 CC        JSR     $CCC1               ; {code.gateSound1f} cue the destruction sound
A372: B9 DB 02        LDA     $02DB,Y             ; {hard.workRam+2DB} read the object's depth
A375: 85 29           STA     $29                 ; {hard.workRam+29} stage the object's depth as the retract source
A377: B9 B5 02        LDA     $02B5,Y             ; {hard.workRam+2B5} read the object's segment
A37A: 85 2D           STA     $2D                 ; {hard.workRam+2D} stage the object's segment
A37C: A9 00           LDA     #$00                
A37E: 20 D4 A3        JSR     $A3D4               ; {code.insertTimedObjectOfType} retract the object's draw record (type 0)
A381: A9 00           LDA     #$00                
A383: 99 DB 02        STA     $02DB,Y             ; {hard.workRam+2DB} empty the slot
A386: C6 A6           DEC     $A6                 ; {hard.workRam+A6} one fewer live enemy
A388: A9 FF           LDA     #$FF                
A38A: 9D F2 02        STA     $02F2,X             ; {hard.workRam+2F2} flag lane X spent for the caller's teardown
A38D: 60              RTS                         

; activate enemy slot X (0x2f2,x=0xff), step the lane index back by four,
; then tail-delegate the retire/spawn/award for that stepped-back slot to
; respawnEnemyAndAward.
activateSlotAndRespawn:
A38E: A9 FF           LDA     #$FF                ; raise slot X's active flag
A390: 9D F2 02        STA     $02F2,X             ; {hard.workRam+2F2}
A393: 98              TYA                         
A394: 38              SEC                         
A395: E9 04           SBC     #$04                ; step the lane index back by four -- the slot recycled this pass
A397: A8              TAY                         

; retire enemy slot Y and spawn its replacement, then award: seed 0x2d
; from 0x2b9,y (decremented into the low nibble when descriptor 0x283,y
; has both top bits set), run
; insertObjectFromSlotDepth+retireEnemyAndSpawnSplit, then tail-delegate a
; score award (addBcdScoreAndAwardAtThreshold) selected by the re-read
; slot's lane through the $A3C5 table.
respawnEnemyAndAward:
A398: B9 83 02        LDA     $0283,Y             ; {hard.workRam+283} read the slot descriptor
A39B: 29 C0           AND     #$C0                
A39D: C9 C0           CMP     #$C0                
A39F: F0 06           BEQ     $A3A7               ; {code.loc_a3a7} both top bits set marks the split/offset case
A3A1: B9 B9 02        LDA     $02B9,Y             ; {hard.workRam+2B9} take the seated segment as-is
A3A4: B8              CLV                         
A3A5: 50 08           BVC     $A3AF               ; {code.loc_a3af}

loc_a3a7:
A3A7: B9 B9 02        LDA     $02B9,Y             ; {hard.workRam+2B9} read the seated segment
A3AA: 38              SEC                         
A3AB: E9 01           SBC     #$01                ; split case: step the segment back one
A3AD: 29 0F           AND     #$0F                ; wrap it within the low nibble

loc_a3af:
A3AF: 85 2D           STA     $2D                 ; {hard.workRam+2D} seed the list-anchor segment
A3B1: A9 00           LDA     #$00                
A3B3: 20 CA A3        JSR     $A3CA               ; {code.insertObjectFromSlotDepth} insert the replacement object from the slot's depth
A3B6: 20 6F A0        JSR     $A06F               ; {code.retireEnemyAndSpawnSplit} retire the enemy and spawn any split
A3B9: B9 83 02        LDA     $0283,Y             ; {hard.workRam+283} re-read the descriptor -- the spawn may have reused the slot
A3BC: 29 07           AND     #$07                ; lane = descriptor low 3 bits
A3BE: A8              TAY                         
A3BF: BE C5 A3        LDX     $A3C5,Y             ; {hard.rom+13C5} look up the lane's score selector
A3C2: 4C 6C CA        JMP     $CA6C               ; {code.addBcdScoreAndAwardAtThreshold} award the kill score for that lane

; ---- $A3C5-$A3C9: data ----
A3C5: 01 02 03 04 01

; insert an object seeded from a slot's depth: cue the sound, copy the
; y-indexed depth loc_2df,y into loc_29, then insert a fresh object into
; the table.
insertObjectFromSlotDepth:
A3CA: 48              PHA                         
A3CB: 20 C1 CC        JSR     $CCC1               ; {code.gateSound1f} cue the spawn sound
A3CE: B9 DF 02        LDA     $02DF,Y             ; {hard.workRam+2DF} read slot Y's depth
A3D1: 85 29           STA     $29                 ; {hard.workRam+29} seed the new object's depth from the slot
A3D3: 68              PLA                         

; insert a timed object of a given type: stash A into the type scratch
; loc_2c, then insert into the 8-slot table.
insertTimedObjectOfType:
A3D4: 85 2C           STA     $2C                 ; {hard.workRam+2C} seat the caller's object type

; insert a timed object into the 8-slot table: reuse the first empty slot
; (loc_30a,i==0) or evict the slot holding the largest counter loc_312,i
; (dropping loc_116 by one), then fill counter loc_312=0, type loc_302
; from loc_2c, presence loc_30a from loc_29, lane loc_2fa from loc_2d, and
; bump loc_116.
insertTimedObject:
A3D6: 86 35           STX     $35                 ; {hard.workRam+35}
A3D8: 84 36           STY     $36                 ; {hard.workRam+36}
A3DA: A9 00           LDA     #$00                
A3DC: 85 2A           STA     $2A                 ; {hard.workRam+2A}
A3DE: 85 2B           STA     $2B                 ; {hard.workRam+2B}
A3E0: A2 07           LDX     #$07                ; scan the eight object slots for a home, high index first

loc_a3e2:
A3E2: BD 0A 03        LDA     $030A,X             ; {hard.workRam+30A} read the slot's presence byte
A3E5: F0 13           BEQ     $A3FA               ; {code.loc_a3fa} an empty slot wins outright
A3E7: BD 12 03        LDA     $0312,X             ; {hard.workRam+312} read the slot's age counter
A3EA: C5 2A           CMP     $2A                 ; {hard.workRam+2A}
A3EC: 90 04           BCC     $A3F2               ; {code.loc_a3f2}
A3EE: 85 2A           STA     $2A                 ; {hard.workRam+2A} remember the oldest slot so far as the eviction candidate
A3F0: 86 2B           STX     $2B                 ; {hard.workRam+2B}

loc_a3f2:
A3F2: CA              DEX                         
A3F3: 10 ED           BPL     $A3E2               ; {code.loc_a3e2} loop over the slots
A3F5: CE 16 01        DEC     $0116               ; {hard.workRam+116} pool full: evict the oldest, balancing the bump below
A3F8: A6 2B           LDX     $2B                 ; {hard.workRam+2B} reuse the oldest slot

loc_a3fa:
A3FA: A9 00           LDA     #$00                
A3FC: 9D 12 03        STA     $0312,X             ; {hard.workRam+312} reset the chosen slot's age -- a fresh object
A3FF: A5 2C           LDA     $2C                 ; {hard.workRam+2C}
A401: 9D 02 03        STA     $0302,X             ; {hard.workRam+302} write the object type
A404: A5 29           LDA     $29                 ; {hard.workRam+29}
A406: 9D 0A 03        STA     $030A,X             ; {hard.workRam+30A} write the object's presence / depth
A409: A5 2D           LDA     $2D                 ; {hard.workRam+2D}
A40B: 9D FA 02        STA     $02FA,X             ; {hard.workRam+2FA} write the object's lane coordinate
A40E: EE 16 01        INC     $0116               ; {hard.workRam+116} one more live object
A411: A6 35           LDX     $35                 ; {hard.workRam+35}
A413: A4 36           LDY     $36                 ; {hard.workRam+36}
A415: 60              RTS                         

; age the timed-object table: if pending flag loc_116 is zero do nothing,
; else clear it and advance each live slot's counter loc_312,i by the per-
; type step $A44E[type], freeing a slot that reaches its per-type limit
; $A448[type] (loc_30a,i=0) and re-raising loc_116 for any slot still
; short.
ageTimedObjects:
A416: AD 16 01        LDA     $0116               ; {hard.workRam+116} read the pending-animation flag
A419: F0 2C           BEQ     $A447               ; {code.loc_a447} skip when nothing is animating
A41B: A9 00           LDA     #$00                
A41D: 8D 16 01        STA     $0116               ; {hard.workRam+116} clear the count -- rebuilt below as the live-slot tally
A420: A2 07           LDX     #$07                ; walk the eight object slots

loc_a422:
A422: BD 0A 03        LDA     $030A,X             ; {hard.workRam+30A} read the slot's presence byte
A425: F0 1D           BEQ     $A444               ; {code.loc_a444} skip an empty slot
A427: BD 12 03        LDA     $0312,X             ; {hard.workRam+312} read the animation counter
A42A: BC 02 03        LDY     $0302,X             ; {hard.workRam+302} index the per-type tables by the object's type
A42D: 18              CLC                         
A42E: 79 4E A4        ADC     $A44E,Y             ; {hard.rom+144E} advance the counter by the object's per-type step
A431: 9D 12 03        STA     $0312,X             ; {hard.workRam+312}
A434: D9 48 A4        CMP     $A448,Y             ; {hard.rom+1448} compare against the object's per-type animation limit
A437: 90 08           BCC     $A441               ; {code.loc_a441} still below the limit -- keep animating
A439: A9 00           LDA     #$00                
A43B: 9D 0A 03        STA     $030A,X             ; {hard.workRam+30A} reached the limit -- free the slot
A43E: B8              CLV                         
A43F: 50 03           BVC     $A444               ; {code.loc_a444}

loc_a441:
A441: EE 16 01        INC     $0116               ; {hard.workRam+116} count this slot as still animating

loc_a444:
A444: CA              DEX                         
A445: 10 DB           BPL     $A422               ; {code.loc_a422} loop over the slots

loc_a447:
A447: 60              RTS                         

; ---- $A448-$A453: data ----
A448: 10 15 20 20 20 10 03 01 03 03 03 03

; drive the proximity pass across the live set: scan slots x=7..0 and, for
; each nonzero 0x2d3 entry, invoke resolveSlotProximityInteractions with
; that entry as the threshold and x as the slot index.
scanAllSlotsForProximity:
A454: A2 07           LDX     #$07                ; walk the eight active object slots, high index first

loc_a456:
A456: BD D3 02        LDA     $02D3,X             ; {hard.workRam+2D3} read the slot's state byte
A459: F0 03           BEQ     $A45E               ; {code.loc_a45e} skip a dead slot
A45B: 20 63 A4        JSR     $A463               ; {code.resolveSlotProximityInteractions} resolve this slot's proximity interactions -- state byte is the depth threshold

loc_a45e:
A45E: CA              DEX                         
A45F: 10 F5           BPL     $A456               ; {code.loc_a456} loop over the slots
A461: 60              RTS                         

; ---- $A462-$A462: data ----
A462: AB

; resolve slot X's proximity interactions: store threshold A in 0x2e, scan
; 0x2db slots y=10..0 forming delta=|entry-threshold|; near slots (y<4)
; under 0x a7 with a matching 0x2b5/0x2ad pair retire via
; retireSpawnedObject; far slots (y>=4) fold 0x27f,y to a 3-bit band, test
; delta against 0x151,band, then dispatch spawnLaneEnemyAndAward (band 4)
; or activateSlotAndRespawn (other bands); after the scan, if
; 0x2f2,x==0xff tear down the slot (clear 0x2d3,x/0x2f2,x, drop live count
; 0x135).
resolveSlotProximityInteractions:
A463: 85 2E           STA     $2E                 ; {hard.workRam+2E} park the query depth for the scan
A465: A0 0A           LDY     #$0A                ; scan all eleven enemy slots (10..0)

loc_a467:
A467: B9 DB 02        LDA     $02DB,Y             ; {hard.workRam+2DB} read the enemy slot's depth
A46A: F0 7F           BEQ     $A4EB               ; {code.loc_a4eb} skip an empty enemy slot
A46C: C5 2E           CMP     $2E                 ; {hard.workRam+2E}
A46E: 90 05           BCC     $A475               ; {code.loc_a475}
A470: E5 2E           SBC     $2E                 ; {hard.workRam+2E} form the absolute depth distance between the object and the enemy
A472: B8              CLV                         
A473: 50 06           BVC     $A47B               ; {code.loc_a47b}

loc_a475:
A475: A5 2E           LDA     $2E                 ; {hard.workRam+2E}
A477: 38              SEC                         
A478: F9 DB 02        SBC     $02DB,Y             ; {hard.workRam+2DB}

loc_a47b:
A47B: C0 04           CPY     #$04                
A47D: B0 12           BCS     $A491               ; {code.loc_a491} slots 0..3 are near the rim; 4..10 are far
A47F: C5 A7           CMP     $A7                 ; {hard.workRam+A7} near the rim: require the enemy within the kill distance
A481: B0 0B           BCS     $A48E               ; {code.loc_a48e}
A483: B9 B5 02        LDA     $02B5,Y             ; {hard.workRam+2B5}
A486: 5D AD 02        EOR     $02AD,X             ; {hard.workRam+2AD} and require a matching segment
A489: D0 03           BNE     $A48E               ; {code.loc_a48e}
A48B: 20 6F A3        JSR     $A36F               ; {code.retireSpawnedObject} retire the object -- a near, same-segment kill

loc_a48e:
A48E: B8              CLV                         
A48F: 50 5A           BVC     $A4EB               ; {code.loc_a4eb}

loc_a491:
A491: 48              PHA                         
A492: 84 38           STY     $38                 ; {hard.workRam+38} record the scan cursor
A494: B9 7F 02        LDA     $027F,Y             ; {hard.workRam+27F} read the object's band attribute
A497: 29 07           AND     #$07                ; fold it to a 3-bit distance band
A499: A8              TAY                         
A49A: 68              PLA                         
A49B: D9 51 01        CMP     $0151,Y             ; {hard.workRam+151} test the distance against the per-band threshold
A49E: B0 49           BCS     $A4E9               ; {code.loc_a4e9} skip when the enemy is beyond the band's reach
A4A0: C0 04           CPY     #$04                
A4A2: D0 1D           BNE     $A4C1               ; {code.loc_a4c1} band 4 has its own spawn/award handler
A4A4: A4 38           LDY     $38                 ; {hard.workRam+38}
A4A6: B9 DB 02        LDA     $02DB,Y             ; {hard.workRam+2DB}
A4A9: CD 02 02        CMP     $0202               ; {hard.workRam+202} band 4: skip when the enemy is at the shot depth
A4AC: F0 10           BEQ     $A4BE               ; {code.loc_a4be}
A4AE: BD AD 02        LDA     $02AD,X             ; {hard.workRam+2AD}
A4B1: D9 B5 02        CMP     $02B5,Y             ; {hard.workRam+2B5} require a matching segment
A4B4: D0 08           BNE     $A4BE               ; {code.loc_a4be}
A4B6: B9 C8 02        LDA     $02C8,Y             ; {hard.workRam+2C8}
A4B9: 10 03           BPL     $A4BE               ; {code.loc_a4be} require the enemy's armed bit set
A4BB: 20 09 A3        JSR     $A309               ; {code.spawnLaneEnemyAndAward} spawn a fresh lane enemy and award the points

loc_a4be:
A4BE: B8              CLV                         
A4BF: 50 28           BVC     $A4E9               ; {code.loc_a4e9}

loc_a4c1:
A4C1: A4 38           LDY     $38                 ; {hard.workRam+38}
A4C3: B9 C8 02        LDA     $02C8,Y             ; {hard.workRam+2C8} branch on the enemy's armed bit
A4C6: 10 0A           BPL     $A4D2               ; {code.loc_a4d2}
A4C8: B9 B5 02        LDA     $02B5,Y             ; {hard.workRam+2B5}
A4CB: DD C0 02        CMP     $02C0,X             ; {hard.workRam+2C0} armed: match the enemy segment against the slot's alternate target
A4CE: F0 12           BEQ     $A4E2               ; {code.loc_a4e2} on a match, re-activate the slot
A4D0: D0 08           BNE     $A4DA               ; {code.loc_a4da}

loc_a4d2:
A4D2: B9 DB 02        LDA     $02DB,Y             ; {hard.workRam+2DB}
A4D5: CD 02 02        CMP     $0202               ; {hard.workRam+202} unarmed and at the shot depth -> skip
A4D8: F0 0F           BEQ     $A4E9               ; {code.loc_a4e9}

loc_a4da:
A4DA: B9 B5 02        LDA     $02B5,Y             ; {hard.workRam+2B5}
A4DD: DD AD 02        CMP     $02AD,X             ; {hard.workRam+2AD} otherwise require a matching target segment
A4E0: D0 07           BNE     $A4E9               ; {code.loc_a4e9}

loc_a4e2:
A4E2: 86 37           STX     $37                 ; {hard.workRam+37} stash the slot index
A4E4: 20 8E A3        JSR     $A38E               ; {code.activateSlotAndRespawn} re-activate the slot and respawn
A4E7: A6 37           LDX     $37                 ; {hard.workRam+37}

loc_a4e9:
A4E9: A4 38           LDY     $38                 ; {hard.workRam+38}

loc_a4eb:
A4EB: 88              DEY                         
A4EC: 30 03           BMI     $A4F1               ; {code.loc_a4f1}
A4EE: 4C 67 A4        JMP     $A467               ; {code.loc_a467} continue the enemy-slot scan

loc_a4f1:
A4F1: BD F2 02        LDA     $02F2,X             ; {hard.workRam+2F2} after the scan, check the slot's spent sentinel
A4F4: C9 FF           CMP     #$FF                
A4F6: D0 0B           BNE     $A503               ; {code.loc_a503}
A4F8: A9 00           LDA     #$00                
A4FA: 9D D3 02        STA     $02D3,X             ; {hard.workRam+2D3} spent slot: clear its state
A4FD: CE 35 01        DEC     $0135               ; {hard.workRam+135} drop the live object count
A500: 9D F2 02        STA     $02F2,X             ; {hard.workRam+2F2} clear the spent sentinel

loc_a503:
A503: 60              RTS                         

; per-frame ager keyed on the sign of loc_201: the positive arm bumps
; timer cell loc_00+loc_40 behind a gate and conditionally re-inits shot
; state via initWaveStateCountingSpikes/clearActiveShots; the negative arm
; ages every live shot in loc_2df from index loc_11c down by +0x0f
; (snapping >=0xf0 to 0), steps loc_202 or the loc_5f/loc_5b countdown
; clock, and on proceed writes loc_00=0x06, runs clearActiveShots, and
; folds loc_108+loc_109+loc_3ab into loc_3ab clamped to 0x3f.
ageShotsAndAdvanceFrameClock:
A504: AD 01 02        LDA     $0201               ; {hard.workRam+201} read the per-frame control byte -- its sign selects which bookkeeping job runs
A507: 10 78           BPL     $A581               ; {code.loc_a581} positive: branch to the wave-setup arm
A509: AD 35 01        LDA     $0135               ; {hard.workRam+135} gather the live-object counts
A50C: 05 A6           ORA     $A6                 ; {hard.workRam+A6}
A50E: 0D 16 01        ORA     $0116               ; {hard.workRam+116} fold in the timed-object count
A511: D0 6B           BNE     $A57E               ; {code.loc_a57e} bail while any object is still live
A513: AE 1C 01        LDX     $011C               ; {hard.workRam+11C} start at the top shot slot

loc_a516:
A516: BD DF 02        LDA     $02DF,X             ; {hard.workRam+2DF} read this shot's depth down the tube
A519: F0 0E           BEQ     $A529               ; {code.loc_a529} skip an empty slot
A51B: 18              CLC                         
A51C: 69 0F           ADC     #$0F                ; age the shot by a fixed step
A51E: B0 02           BCS     $A522               ; {code.loc_a522}
A520: C9 F0           CMP     #$F0                ; clamp against the far rim

loc_a522:
A522: 90 02           BCC     $A526               ; {code.loc_a526}
A524: A9 00           LDA     #$00                ; snap to zero at the far rim

loc_a526:
A526: 9D DF 02        STA     $02DF,X             ; {hard.workRam+2DF} store the aged depth

loc_a529:
A529: CA              DEX                         
A52A: 10 EA           BPL     $A516               ; {code.loc_a516} next shot slot
A52C: A6 3D           LDX     $3D                 ; {hard.workRam+3D} index the current slot
A52E: B5 48           LDA     $48,X               ; {hard.workRam+48} read this slot's countdown
A530: C9 01           CMP     #$01                ; branch on whether the countdown is at its last tick
A532: D0 20           BNE     $A554               ; {code.loc_a554}
A534: A9 00           LDA     #$00                
A536: 8D 0F 01        STA     $010F               ; {hard.workRam+10F} clear a wave flag
A539: A9 01           LDA     #$01                
A53B: 8D 14 01        STA     $0114               ; {hard.workRam+114} arm the redraw
A53E: A5 5F           LDA     $5F                 ; {hard.workRam+5F} step the between-wave clock low byte down by 0x20
A540: 38              SEC                         
A541: E9 20           SBC     #$20                
A543: 85 5F           STA     $5F                 ; {hard.workRam+5F} store the clock low byte
A545: A5 5B           LDA     $5B                 ; {hard.workRam+5B} borrow into the clock high byte
A547: E9 00           SBC     #$00                
A549: 85 5B           STA     $5B                 ; {hard.workRam+5B} store the clock high byte
A54B: C9 FA           CMP     #$FA                ; proceed when the clock reaches its marker
A54D: 18              CLC                         
A54E: D0 01           BNE     $A551               ; {code.loc_a551}
A550: 38              SEC                         

loc_a551:
A551: B8              CLV                         
A552: 50 0D           BVC     $A561               ; {code.loc_a561}

loc_a554:
A554: AD 02 02        LDA     $0202               ; {hard.workRam+202} step the shot-depth counter by a fixed amount
A557: 18              CLC                         
A558: 69 0F           ADC     #$0F                
A55A: 8D 02 02        STA     $0202               ; {hard.workRam+202} store the stepped shot depth
A55D: B0 02           BCS     $A561               ; {code.loc_a561}
A55F: C9 F0           CMP     #$F0                ; proceed once it passes the far rim

loc_a561:
A561: 90 1B           BCC     $A57E               ; {code.loc_a57e} not yet -- exit
A563: A9 06           LDA     #$06                ; hand off: set the game mode to 6
A565: 85 00           STA     $00                 ; {hard.workRam}
A567: 20 8F 92        JSR     $928F               ; {code.clearActiveShots} clear all active shots
A56A: AD 08 01        LDA     $0108               ; {hard.workRam+108} sum the enemy-total and enemy-type budgets
A56D: 18              CLC                         
A56E: 6D 09 01        ADC     $0109               ; {hard.workRam+109}
A571: 18              CLC                         
A572: 6D AB 03        ADC     $03AB               ; {hard.workRam+3AB} add in the running fire budget
A575: C9 3F           CMP     #$3F                ; clamp the enemy budget to 0x3f
A577: 90 02           BCC     $A57B               ; {code.loc_a57b}
A579: A9 3F           LDA     #$3F                

loc_a57b:
A57B: 8D AB 03        STA     $03AB               ; {hard.workRam+3AB} store the clamped fire budget

loc_a57e:
A57E: B8              CLV                         
A57F: 50 49           BVC     $A5CA               ; {code.loc_a5ca}

loc_a581:
A581: AD 55 04        LDA     $0455               ; {hard.workRam+455} test the wave-setup gate cell pair
A584: 0D 1B 01        ORA     $011B               ; {hard.workRam+11B}
A587: F0 0A           BEQ     $A593               ; {code.loc_a593} skip the timer bump unless a gate is live
A589: A9 17           LDA     #$17                
A58B: C5 42           CMP     $42                 ; {hard.workRam+42} only bump past the threshold
A58D: B0 04           BCS     $A593               ; {code.loc_a593}
A58F: A6 40           LDX     $40                 ; {hard.workRam+40} index the per-slot setup timer
A591: F6 00           INC     $00,X               ; {hard.workRam} bump the per-slot setup timer

loc_a593:
A593: AD 06 01        LDA     $0106               ; {hard.workRam+106} read the spike-active flag
A596: D0 32           BNE     $A5CA               ; {code.loc_a5ca} bail while a spike is active
A598: AD AB 03        LDA     $03AB               ; {hard.workRam+3AB} combine the fire budget and timed-object count
A59B: 0D 16 01        ORA     $0116               ; {hard.workRam+116}
A59E: D0 15           BNE     $A5B5               ; {code.loc_a5b5} only recycle the wave when both are clear
A5A0: AC 1C 01        LDY     $011C               ; {hard.workRam+11C} scan the shot table from the top slot

loc_a5a3:
A5A3: B9 DF 02        LDA     $02DF,Y             ; {hard.workRam+2DF} read this shot's depth
A5A6: F0 04           BEQ     $A5AC               ; {code.loc_a5ac}
A5A8: C9 11           CMP     #$11                ; abort the reset if any shot has grown past 0x11
A5AA: B0 09           BCS     $A5B5               ; {code.loc_a5b5}

loc_a5ac:
A5AC: 88              DEY                         
A5AD: 10 F4           BPL     $A5A3               ; {code.loc_a5a3} keep scanning
A5AF: 20 CB A5        JSR     $A5CB               ; {code.initWaveStateCountingSpikes} re-seed the wave state
A5B2: 20 8F 92        JSR     $928F               ; {code.clearActiveShots} clear active shots

loc_a5b5:
A5B5: A5 4D           LDA     $4D                 ; {hard.workRam+4D} gate the second wave reset on a start input
A5B7: 29 60           AND     #$60                
A5B9: F0 0F           BEQ     $A5CA               ; {code.loc_a5ca}
A5BB: 24 05           BIT     $05                 ; {hard.workRam+5} gate on the attract/status flag
A5BD: 10 0B           BPL     $A5CA               ; {code.loc_a5ca}
A5BF: A5 09           LDA     $09                 ; {hard.workRam+9} gate on a dip-switch setting
A5C1: 29 43           AND     #$43                
A5C3: C9 40           CMP     #$40                
A5C5: D0 03           BNE     $A5CA               ; {code.loc_a5ca}
A5C7: 20 CB A5        JSR     $A5CB               ; {code.initWaveStateCountingSpikes} re-seed the wave state

loc_a5ca:
A5CA: 60              RTS                         

; wave-state init: reset the batch loc_0=0x20, loc_104=0, loc_107=0,
; loc_5c=0, loc_123=0, loc_105=0x02 and OR bit7 into loc_106, tally into
; loc_123 how many of the sixteen loc_3ac lane cells are nonzero, and if
; that tally is nonzero with level loc_9f<0x07 overwrite the intro block
; (loc_4=0x1e, loc_0=0x0a, loc_2=0x20, loc_123=0x80), finally latching
; loc_125=0xff ready.
initWaveStateCountingSpikes:
A5CB: A9 20           LDA     #$20                ; set the game mode to the wave-start value
A5CD: 85 00           STA     $00                 ; {hard.workRam}
A5CF: AD 06 01        LDA     $0106               ; {hard.workRam+106} arm the spike-active bit
A5D2: 09 80           ORA     #$80                
A5D4: 8D 06 01        STA     $0106               ; {hard.workRam+106} store the spike-active flag
A5D7: A9 00           LDA     #$00                
A5D9: 8D 04 01        STA     $0104               ; {hard.workRam+104} clear the spike step-low byte
A5DC: 8D 07 01        STA     $0107               ; {hard.workRam+107} clear the spike height-low byte
A5DF: 85 5C           STA     $5C                 ; {hard.workRam+5C} clear the depth accumulator
A5E1: 8D 23 01        STA     $0123               ; {hard.workRam+123} clear the spiked-lane tally
A5E4: A9 02           LDA     #$02                
A5E6: 8D 05 01        STA     $0105               ; {hard.workRam+105} set the spike step-high byte
A5E9: A2 0F           LDX     #$0F                ; scan the sixteen lane-limit cells

loc_a5eb:
A5EB: BD AC 03        LDA     $03AC,X             ; {hard.workRam+3AC} read this lane's limit
A5EE: F0 03           BEQ     $A5F3               ; {code.loc_a5f3}
A5F0: EE 23 01        INC     $0123               ; {hard.workRam+123} count each spiked lane

loc_a5f3:
A5F3: CA              DEX                         
A5F4: 10 F5           BPL     $A5EB               ; {code.loc_a5eb}
A5F6: AD 23 01        LDA     $0123               ; {hard.workRam+123} skip the intro if no lane is spiked
A5F9: F0 17           BEQ     $A612               ; {code.loc_a612}
A5FB: A5 9F           LDA     $9F                 ; {hard.workRam+9F} only run the intro on early waves -- level below 7
A5FD: C9 07           CMP     #$07                
A5FF: B0 11           BCS     $A612               ; {code.loc_a612}
A601: A9 1E           LDA     #$1E                ; arm the intro delay timer
A603: 85 04           STA     $04                 ; {hard.workRam+4}
A605: A9 0A           LDA     #$0A                ; set the game mode to the spike-intro value
A607: 85 00           STA     $00                 ; {hard.workRam}
A609: A9 20           LDA     #$20                ; queue the pending mode
A60B: 85 02           STA     $02                 ; {hard.workRam+2}
A60D: A9 80           LDA     #$80                
A60F: 8D 23 01        STA     $0123               ; {hard.workRam+123} stamp the spike-intro marker into the tally

loc_a612:
A612: A9 FF           LDA     #$FF                ; arm the block-ready latch
A614: 8D 25 01        STA     $0125               ; {hard.workRam+125}
A617: 60              RTS                         

; drive one frame of the enemy bank: seed frame-active flag loc_10d from
; spawn budget loc_10e, walk slots 0x0f..0, integrate+decay each live slot
; (loc_283,x!=0) via the flight steps and refill each free slot from the
; budget, tick loc_10e on even frames (loc_3 bit0 clear), settle
; loc_37=0xff, and raise mode-request loc_0=0x12 when nothing was live or
; spawned.
stepEnemyFleetAndSpawn:
A618: AD 0E 01        LDA     $010E               ; {hard.workRam+10E} seed the frame-active flag from the spawn budget
A61B: 8D 0D 01        STA     $010D               ; {hard.workRam+10D}
A61E: A2 0F           LDX     #$0F                ; walk the sixteen enemy slots top-down
A620: 86 37           STX     $37                 ; {hard.workRam+37}

loc_a622:
A622: A6 37           LDX     $37                 ; {hard.workRam+37}
A624: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} read this slot's flags
A627: D0 0B           BNE     $A634               ; {code.loc_a634} branch on whether the slot holds a live enemy
A629: AD 0E 01        LDA     $010E               ; {hard.workRam+10E} free slot: spawn only while the spawn budget remains
A62C: F0 03           BEQ     $A631               ; {code.loc_a631}
A62E: 20 5B A6        JSR     $A65B               ; {code.spawnEnemyInSlot} spawn a new enemy in this slot

loc_a631:
A631: B8              CLV                         
A632: 50 0B           BVC     $A63F               ; {code.loc_a63f}

loc_a634:
A634: 20 A9 A6        JSR     $A6A9               ; {code.advanceEnemyFreeFlight} advance the live enemy's free flight
A637: 20 21 A7        JSR     $A721               ; {code.decayEnemyFreeFlightVelocity} decay its velocity
A63A: A9 FF           LDA     #$FF                
A63C: 8D 0D 01        STA     $010D               ; {hard.workRam+10D} mark the frame active

loc_a63f:
A63F: C6 37           DEC     $37                 ; {hard.workRam+37} next slot
A641: 10 DF           BPL     $A622               ; {code.loc_a622}
A643: A5 03           LDA     $03                 ; {hard.workRam+3} tick the spawn budget only on even frames
A645: 29 01           AND     #$01                
A647: D0 08           BNE     $A651               ; {code.loc_a651}
A649: AD 0E 01        LDA     $010E               ; {hard.workRam+10E}
A64C: F0 03           BEQ     $A651               ; {code.loc_a651}
A64E: CE 0E 01        DEC     $010E               ; {hard.workRam+10E} count the spawn budget down

loc_a651:
A651: AD 0D 01        LDA     $010D               ; {hard.workRam+10D} test whether anything was live or spawned
A654: D0 04           BNE     $A65A               ; {code.loc_a65a} something happened -- exit
A656: A9 12           LDA     #$12                ; nothing left: raise the mode request to 0x12
A658: 85 00           STA     $00                 ; {hard.workRam}

loc_a65a:
A65A: 60              RTS                         

; spawn an enemy into free slot x: mark loc_263,x/loc_283,x/loc_2a3,x =
; 0x80, seed three velocity/coordinate pairs from POKEY draws $60DA/$60CA
; (raw into loc_2c3/2e3/303,x, signed nudge from drawSignedVelocityNudge
; into loc_323/343/363,x, forcing the middle nudge non-positive), then cue
; the spawn sound gateSound1f.
spawnEnemyInSlot:
A65B: A5 03           LDA     $03                 ; {hard.workRam+3}
A65D: 29 00           AND     #$00                
A65F: D0 39           BNE     $A69A               ; {code.loc_a69a}
A661: A9 80           LDA     #$80                ; center axis-1 position and mark the slot live
A663: 9D 63 02        STA     $0263,X             ; {hard.workRam+263}
A666: 9D 83 02        STA     $0283,X             ; {hard.workRam+283} mark the slot occupied
A669: 9D A3 02        STA     $02A3,X             ; {hard.workRam+2A3} center the third axis position
A66C: AD DA 60        LDA     $60DA               ; {hard.pokey2+A} seed axis-1 velocity low from a random source
A66F: 9D C3 02        STA     $02C3,X             ; {hard.workRam+2C3} store axis-1 velocity low
A672: 20 9B A6        JSR     $A69B               ; {code.drawSignedVelocityNudge} draw a signed velocity nudge
A675: 9D 23 03        STA     $0323,X             ; {hard.workRam+323} store axis-1 velocity nudge
A678: AD CA 60        LDA     $60CA               ; {hard.pokey1+A} seed axis-0 velocity low from a random source
A67B: 9D E3 02        STA     $02E3,X             ; {hard.workRam+2E3} store axis-0 velocity low
A67E: 20 9B A6        JSR     $A69B               ; {code.drawSignedVelocityNudge} draw a nudge for the middle axis
A681: 30 05           BMI     $A688               ; {code.loc_a688} force the middle nudge non-positive
A683: 49 FF           EOR     #$FF                
A685: 18              CLC                         
A686: 69 01           ADC     #$01                

loc_a688:
A688: 9D 43 03        STA     $0343,X             ; {hard.workRam+343} store axis-0 velocity nudge
A68B: AD CA 60        LDA     $60CA               ; {hard.pokey1+A} seed axis-2 velocity low from a random source
A68E: 9D 03 03        STA     $0303,X             ; {hard.workRam+303} store axis-2 velocity low
A691: 20 9B A6        JSR     $A69B               ; {code.drawSignedVelocityNudge} draw a nudge for axis 2
A694: 9D 63 03        STA     $0363,X             ; {hard.workRam+363} store axis-2 velocity nudge
A697: 20 C1 CC        JSR     $CCC1               ; {code.gateSound1f} cue the spawn sound for this slot

loc_a69a:
A69A: 60              RTS                         

; produce a signed random velocity nudge: take a 3-bit magnitude ($60DA &
; 0x07, 0..7) and negate it when the caller's incoming value has bit0 set,
; yielding a signed step in [-7,+7] consumed by spawnEnemyInSlot as a
; whole-velocity seed.
drawSignedVelocityNudge:
A69B: 4A              LSR     A                   ; shift the caller's low bit into carry to pick the sign
A69C: AD DA 60        LDA     $60DA               ; {hard.pokey2+A} take a 3-bit random magnitude, 0..7
A69F: 29 07           AND     #$07                
A6A1: 90 05           BCC     $A6A8               ; {code.loc_a6a8} keep it positive when the selector bit was clear
A6A3: 49 FF           EOR     #$FF                ; two's-complement negate for a negative step
A6A5: 18              CLC                         
A6A6: 69 01           ADC     #$01                

loc_a6a8:
A6A8: 60              RTS                         

; integrate slot x's three free-flight axes: fold each low velocity
; (loc_2e3/2c3/303,x) into its fraction (loc_223/203/243,x) and add
; carry+signed whole (loc_343/323/363,x) into a whole coordinate,
; committing loc_263,x and loc_2a3,x and loc_283,x, but forcing loc_283,x
; to 0 (retiring the slot) if any axis crosses the tube ring [0x10,0xf0).
advanceEnemyFreeFlight:
A6A9: BD E3 02        LDA     $02E3,X             ; {hard.workRam+2E3} axis 0: fold velocity-low into the fraction
A6AC: 18              CLC                         
A6AD: 7D 23 02        ADC     $0223,X             ; {hard.workRam+223}
A6B0: 9D 23 02        STA     $0223,X             ; {hard.workRam+223} store the axis-0 fraction
A6B3: BD 43 03        LDA     $0343,X             ; {hard.workRam+343} branch on the axis-0 velocity sign
A6B6: 30 0C           BMI     $A6C4               ; {code.loc_a6c4}
A6B8: 7D 83 02        ADC     $0283,X             ; {hard.workRam+283} rising axis: add the whole, overflow at the far rim
A6BB: C9 F0           CMP     #$F0                
A6BD: 90 02           BCC     $A6C1               ; {code.loc_a6c1}
A6BF: A9 00           LDA     #$00                ; off the ring -> zero

loc_a6c1:
A6C1: B8              CLV                         
A6C2: 50 09           BVC     $A6CD               ; {code.loc_a6cd}

loc_a6c4:
A6C4: 7D 83 02        ADC     $0283,X             ; {hard.workRam+283} falling axis: add the whole, overflow below the near rim
A6C7: C9 10           CMP     #$10                
A6C9: B0 02           BCS     $A6CD               ; {code.loc_a6cd}
A6CB: A9 00           LDA     #$00                ; off the ring -> zero

loc_a6cd:
A6CD: A8              TAY                         ; hold the axis-0 whole
A6CE: BD C3 02        LDA     $02C3,X             ; {hard.workRam+2C3} axis 1: fold velocity-low into the fraction
A6D1: 18              CLC                         
A6D2: 7D 03 02        ADC     $0203,X             ; {hard.workRam+203}
A6D5: 9D 03 02        STA     $0203,X             ; {hard.workRam+203} store the axis-1 fraction
A6D8: BD 23 03        LDA     $0323,X             ; {hard.workRam+323} branch on the axis-1 velocity sign
A6DB: 30 0C           BMI     $A6E9               ; {code.loc_a6e9}
A6DD: 7D 63 02        ADC     $0263,X             ; {hard.workRam+263} rising axis: add the whole, overflow at the far rim
A6E0: C9 F0           CMP     #$F0                
A6E2: 90 02           BCC     $A6E6               ; {code.loc_a6e6}
A6E4: A0 00           LDY     #$00                ; overflow retires the slot -- zero the shared whole

loc_a6e6:
A6E6: B8              CLV                         
A6E7: 50 09           BVC     $A6F2               ; {code.loc_a6f2}

loc_a6e9:
A6E9: 7D 63 02        ADC     $0263,X             ; {hard.workRam+263} falling axis: add the whole, overflow below the near rim
A6EC: C9 10           CMP     #$10                
A6EE: B0 02           BCS     $A6F2               ; {code.loc_a6f2}
A6F0: A0 00           LDY     #$00                ; overflow retires the slot

loc_a6f2:
A6F2: 9D 63 02        STA     $0263,X             ; {hard.workRam+263} commit the axis-1 whole position
A6F5: BD 03 03        LDA     $0303,X             ; {hard.workRam+303} axis 2: fold velocity-low into the fraction
A6F8: 18              CLC                         
A6F9: 7D 43 02        ADC     $0243,X             ; {hard.workRam+243}
A6FC: 9D 43 02        STA     $0243,X             ; {hard.workRam+243} store the axis-2 fraction
A6FF: BD 63 03        LDA     $0363,X             ; {hard.workRam+363} branch on the axis-2 velocity sign
A702: 30 0C           BMI     $A710               ; {code.loc_a710}
A704: 7D A3 02        ADC     $02A3,X             ; {hard.workRam+2A3} rising axis: add the whole, overflow at the far rim
A707: C9 F0           CMP     #$F0                
A709: 90 02           BCC     $A70D               ; {code.loc_a70d}
A70B: A0 00           LDY     #$00                ; overflow retires the slot

loc_a70d:
A70D: B8              CLV                         
A70E: 50 09           BVC     $A719               ; {code.loc_a719}

loc_a710:
A710: 7D A3 02        ADC     $02A3,X             ; {hard.workRam+2A3} falling axis: add the whole, overflow below the near rim
A713: C9 10           CMP     #$10                
A715: B0 02           BCS     $A719               ; {code.loc_a719}
A717: A0 00           LDY     #$00                ; overflow retires the slot

loc_a719:
A719: 9D A3 02        STA     $02A3,X             ; {hard.workRam+2A3} commit the axis-2 whole position
A71C: 98              TYA                         
A71D: 9D 83 02        STA     $0283,X             ; {hard.workRam+283} stamp the axis-0 whole into the shared slot cell -- zero here retires the slot
A720: 60              RTS                         

; decay slot x's free-flight velocities: seed saturation counter
; loc_29=0xfd, step each velocity pair (loc_2c3/323, loc_2e3/343,
; loc_303/363,x) one increment toward zero via stepVelocityTowardZero, and
; clear the slot's whole coordinate loc_283,x only when all three axes
; saturate in the same frame.
decayEnemyFreeFlightVelocity:
A721: A9 FD           LDA     #$FD                ; seed the saturation counter
A723: 85 29           STA     $29                 ; {hard.workRam+29}
A725: BD C3 02        LDA     $02C3,X             ; {hard.workRam+2C3} axis 1: read the velocity pair
A728: BC 23 03        LDY     $0323,X             ; {hard.workRam+323}
A72B: 20 5D A7        JSR     $A75D               ; {code.stepVelocityTowardZero} step it one increment toward zero
A72E: 9D C3 02        STA     $02C3,X             ; {hard.workRam+2C3} store the stepped axis-1 low byte
A731: 98              TYA                         
A732: 9D 23 03        STA     $0323,X             ; {hard.workRam+323} store the stepped axis-1 whole byte
A735: BD E3 02        LDA     $02E3,X             ; {hard.workRam+2E3} axis 0: read the velocity pair
A738: BC 43 03        LDY     $0343,X             ; {hard.workRam+343}
A73B: 20 5D A7        JSR     $A75D               ; {code.stepVelocityTowardZero} step it toward zero
A73E: 9D E3 02        STA     $02E3,X             ; {hard.workRam+2E3} store the stepped axis-0 low byte
A741: 98              TYA                         
A742: 9D 43 03        STA     $0343,X             ; {hard.workRam+343} store the stepped axis-0 whole byte
A745: BD 03 03        LDA     $0303,X             ; {hard.workRam+303} axis 2: read the velocity pair
A748: BC 63 03        LDY     $0363,X             ; {hard.workRam+363}
A74B: 20 5D A7        JSR     $A75D               ; {code.stepVelocityTowardZero} step it toward zero
A74E: 9D 03 03        STA     $0303,X             ; {hard.workRam+303} store the stepped axis-2 low byte
A751: 98              TYA                         
A752: 9D 63 03        STA     $0363,X             ; {hard.workRam+363} store the stepped axis-2 whole byte
A755: A5 29           LDA     $29                 ; {hard.workRam+29} only when every axis reached rest
A757: D0 03           BNE     $A75C               ; {code.loc_a75c}
A759: 9D 83 02        STA     $0283,X             ; {hard.workRam+283} retire the slot -- clear its coordinate

loc_a75c:
A75C: 60              RTS                         

; step one signed 16-bit velocity (whole:low) one fixed increment $A788
; (0x20) toward zero (add when whole negative, subtract otherwise),
; snapping low loc_2a=0 and bumping saturation counter loc_29 on crossing
; zero; returns the stepped [low,whole].
stepVelocityTowardZero:
A75D: 84 2B           STY     $2B                 ; {hard.workRam+2B} snapshot the incoming whole byte
A75F: 24 2B           BIT     $2B                 ; {hard.workRam+2B} branch on the velocity sign
A761: 30 0F           BMI     $A772               ; {code.loc_a772}
A763: 38              SEC                         ; non-negative: subtract the fixed decay step
A764: ED 88 A7        SBC     $A788               ; {hard.rom+1788}
A767: 85 2A           STA     $2A                 ; {hard.workRam+2A} store the stepped low byte
A769: A5 2B           LDA     $2B                 ; {hard.workRam+2B} borrow from the whole byte
A76B: E9 00           SBC     #$00                
A76D: 90 0F           BCC     $A77E               ; {code.loc_a77e} below zero -> zero crossing
A76F: B8              CLV                         
A770: 50 12           BVC     $A784               ; {code.loc_a784}

loc_a772:
A772: 18              CLC                         ; negative: add the fixed decay step
A773: 6D 88 A7        ADC     $A788               ; {hard.rom+1788}
A776: 85 2A           STA     $2A                 ; {hard.workRam+2A} store the stepped low byte
A778: A5 2B           LDA     $2B                 ; {hard.workRam+2B} carry into the whole byte
A77A: 69 00           ADC     #$00                
A77C: 90 06           BCC     $A784               ; {code.loc_a784} past the ceiling -> zero crossing

loc_a77e:
A77E: E6 29           INC     $29                 ; {hard.workRam+29} count this axis as saturated
A780: A9 00           LDA     #$00                ; snap the velocity to zero
A782: 85 2A           STA     $2A                 ; {hard.workRam+2A}

loc_a784:
A784: A8              TAY                         
A785: A5 2A           LDA     $2A                 ; {hard.workRam+2A}
A787: 60              RTS                         

; ---- $A788-$A788: data ----
A788: 20

; slot-arm init leaf: zero the sixteen-byte per-slot state/flags table
; loc_283..loc_283+0x0f, then re-seed scalars loc_10e=0x20, loc_10d=0x20,
; loc_1=0x04, loc_68=0 and loc_69=0.
resetPerSlotStateTable:
A789: A2 0F           LDX     #$0F                ; start at the top of the per-slot flags table

loc_a78b:
A78B: A9 00           LDA     #$00                
A78D: 9D 83 02        STA     $0283,X             ; {hard.workRam+283} clear this slot's flags
A790: CA              DEX                         ; next slot
A791: 10 F8           BPL     $A78B               ; {code.loc_a78b}
A793: A9 20           LDA     #$20                ; reset the spawn budget
A795: 8D 0E 01        STA     $010E               ; {hard.workRam+10E}
A798: 8D 0D 01        STA     $010D               ; {hard.workRam+10D} reset the spawn-found flag
A79B: A9 04           LDA     #$04                
A79D: 85 01           STA     $01                 ; {hard.workRam+1} reset the mode selector
A79F: A9 00           LDA     #$00                ; clear the projection X offset low
A7A1: 85 68           STA     $68                 ; {hard.workRam+68}
A7A3: 85 69           STA     $69                 ; {hard.workRam+69} clear the projection X offset high
A7A5: 60              RTS                         

; shared signed segment-distance helper: compute A minus Y, stash it in
; loc_2a, then keep the full byte when loc_111 bit7 is set, else mask to
; the low nibble and sign-extend bit3 into a signed byte.
signedSegmentDelta:
A7A6: 84 2A           STY     $2A                 ; {hard.workRam+2A} stash the target segment
A7A8: 38              SEC                         
A7A9: E5 2A           SBC     $2A                 ; {hard.workRam+2A} compute the signed segment distance
A7AB: 85 2A           STA     $2A                 ; {hard.workRam+2A} store the raw difference
A7AD: 2C 11 01        BIT     $0111               ; {hard.workRam+111} test the tube-geometry flag
A7B0: 30 09           BMI     $A7BB               ; {code.loc_a7bb} open tube -> keep the full signed byte
A7B2: 29 0F           AND     #$0F                ; closed tube -> take the low nibble
A7B4: 2C BC A7        BIT     $A7BC               ; {hard.rom+17BC} test the nibble sign bit
A7B7: F0 02           BEQ     $A7BB               ; {code.loc_a7bb}
A7B9: 09 F8           ORA     #$F8                ; sign-extend the nibble into a signed byte

loc_a7bb:
A7BB: 60              RTS                         

; ---- $A7BC-$A7BC: data ----
A7BC: 08

; rebuild the spike table: zero the 8-byte array loc_3fe (7..0), stamp its
; last slot loc_405=0xf0, and arm the remap reference loc_115=0xff.
rebuildSpikeTable:
A7BD: A2 07           LDX     #$07                ; walk the eight-lane spike table
A7BF: A9 00           LDA     #$00                

loc_a7c1:
A7C1: 9D FE 03        STA     $03FE,X             ; {hard.workRam+3FE} clear this lane's spike height
A7C4: CA              DEX                         ; next lane
A7C5: 10 FA           BPL     $A7C1               ; {code.loc_a7c1}
A7C7: A9 F0           LDA     #$F0                ; stamp the final slot with the sentinel guard
A7C9: 8D 05 04        STA     $0405               ; {hard.workRam+405}
A7CC: A9 FF           LDA     #$FF                ; arm the remap-reference guard
A7CE: 8D 15 01        STA     $0115               ; {hard.workRam+115}
A7D1: 60              RTS                         

; remap the 8-entry spike table loc_3fe against reference loc_115: entries
; >=0x17 shrink by 7, smaller nonzero entries snap to a rail (0xf0/0) by
; loc_115's sign, a zero entry adopts a neighbour's rail; OR-fold results
; into loc_29, set loc_37=0xff, and clear loc_115 when the whole table has
; collapsed to zero. No-op while loc_115 is zero.
stepSpikeTableCollapse:
A7D2: AD 15 01        LDA     $0115               ; {hard.workRam+115} no-op while the collapse object is disarmed
A7D5: F0 59           BEQ     $A830               ; {code.loc_a830}
A7D7: A9 00           LDA     #$00                
A7D9: 85 29           STA     $29                 ; {hard.workRam+29} clear the remaining-height accumulator
A7DB: A2 07           LDX     #$07                ; walk the eight height slots top-down
A7DD: 86 37           STX     $37                 ; {hard.workRam+37}

loc_a7df:
A7DF: A6 37           LDX     $37                 ; {hard.workRam+37}
A7E1: BD FE 03        LDA     $03FE,X             ; {hard.workRam+3FE} read this lane's spike height
A7E4: F0 18           BEQ     $A7FE               ; {code.loc_a7fe} handle an empty slot separately
A7E6: 38              SEC                         
A7E7: E9 07           SBC     #$07                ; shrink a spike by a fixed step
A7E9: 90 02           BCC     $A7ED               ; {code.loc_a7ed}
A7EB: C9 10           CMP     #$10                

loc_a7ed:
A7ED: B0 0C           BCS     $A7FB               ; {code.loc_a7fb} tall enough -> keep the shrunk height
A7EF: AC 15 01        LDY     $0115               ; {hard.workRam+115} short spike: pick a rail from the guard sign
A7F2: 10 05           BPL     $A7F9               ; {code.loc_a7f9}
A7F4: A9 F0           LDA     #$F0                ; negative guard -> high rail
A7F6: B8              CLV                         
A7F7: 50 02           BVC     $A7FB               ; {code.loc_a7fb}

loc_a7f9:
A7F9: A9 00           LDA     #$00                ; non-negative guard -> low rail

loc_a7fb:
A7FB: B8              CLV                         
A7FC: 50 20           BVC     $A81E               ; {code.loc_a81e}

loc_a7fe:
A7FE: AC 15 01        LDY     $0115               ; {hard.workRam+115} empty slot stays empty unless the guard is negative
A801: 10 1B           BPL     $A81E               ; {code.loc_a81e}
A803: 8A              TXA                         
A804: 18              CLC                         
A805: 69 01           ADC     #$01                ; index the wrap-around next neighbour
A807: C9 08           CMP     #$08                
A809: 90 02           BCC     $A80D               ; {code.loc_a80d}
A80B: A9 00           LDA     #$00                ; wrap the top slot back to slot 0

loc_a80d:
A80D: A8              TAY                         
A80E: B9 FE 03        LDA     $03FE,Y             ; {hard.workRam+3FE} read the neighbour's height
A811: F0 0B           BEQ     $A81E               ; {code.loc_a81e} no neighbour to borrow from
A813: C9 D5           CMP     #$D5                ; neighbour too tall to borrow
A815: B0 05           BCS     $A81C               ; {code.loc_a81c}
A817: A9 F0           LDA     #$F0                ; adopt the high rail from the neighbour
A819: B8              CLV                         
A81A: 50 02           BVC     $A81E               ; {code.loc_a81e}

loc_a81c:
A81C: A9 00           LDA     #$00                

loc_a81e:
A81E: 9D FE 03        STA     $03FE,X             ; {hard.workRam+3FE} store the new spike height
A821: 05 29           ORA     $29                 ; {hard.workRam+29} fold into the remaining-height accumulator
A823: 85 29           STA     $29                 ; {hard.workRam+29}
A825: C6 37           DEC     $37                 ; {hard.workRam+37}
A827: 10 B6           BPL     $A7DF               ; {code.loc_a7df} next slot
A829: A5 29           LDA     $29                 ; {hard.workRam+29}
A82B: D0 03           BNE     $A830               ; {code.loc_a830} leave the object armed while any height remains
A82D: 8D 15 01        STA     $0115               ; {hard.workRam+115} table fully collapsed -> disarm the object

loc_a830:
A830: 60              RTS                         

; reset leaf: clear the pair loc_3aa and loc_125 together, where loc_125
; is the block-ready latch set to 0xff elsewhere.
clearReadyLatchPair:
A831: A9 00           LDA     #$00                ; reset the sweep/stage cell
A833: 8D AA 03        STA     $03AA               ; {hard.workRam+3AA}
A836: 8D 25 01        STA     $0125               ; {hard.workRam+125} disarm the block-ready latch
A839: 60              RTS                         

; step the attract-mode phase timer (only while 0x5 bit7 set): with 0x125
; running advance it and at the 0x3aa-indexed limit (table $A883) restart
; it and run the sweep sweepLaneSlotsForRespawn; with 0x125 idle, arm the
; next stage (bump 0x3aa, seed 0x125=1) when 0x201 is clear and 0x4e bit3
; is set; every path clears bit7 of 0x4e.
stepAttractEnemySweepTimer:
A83A: A5 05           LDA     $05                 ; {hard.workRam+5} run only while attract mode is active
A83C: 10 3E           BPL     $A87C               ; {code.loc_a87c}
A83E: AD 25 01        LDA     $0125               ; {hard.workRam+125} phase already running -> advance it
A841: D0 23           BNE     $A866               ; {code.loc_a866}
A843: AD 01 02        LDA     $0201               ; {hard.workRam+201} idle: arm the next stage only when the control byte is positive
A846: 30 1B           BMI     $A863               ; {code.loc_a863}
A848: A5 4E           LDA     $4E                 ; {hard.workRam+4E} and a trigger edge is present
A84A: 29 08           AND     #$08                
A84C: F0 15           BEQ     $A863               ; {code.loc_a863}
A84E: AD AA 03        LDA     $03AA               ; {hard.workRam+3AA} up to three stages
A851: C9 02           CMP     #$02                
A853: B0 08           BCS     $A85D               ; {code.loc_a85d}
A855: EE AA 03        INC     $03AA               ; {hard.workRam+3AA} bump the sweep stage
A858: A9 01           LDA     #$01                ; seed the phase latch
A85A: 8D 25 01        STA     $0125               ; {hard.workRam+125}

loc_a85d:
A85D: A5 4E           LDA     $4E                 ; {hard.workRam+4E} consume the trigger edge
A85F: 29 77           AND     #$77                
A861: 85 4E           STA     $4E                 ; {hard.workRam+4E}

loc_a863:
A863: B8              CLV                         
A864: 50 16           BVC     $A87C               ; {code.loc_a87c}

loc_a866:
A866: EE 25 01        INC     $0125               ; {hard.workRam+125} tick the running phase
A869: AE AA 03        LDX     $03AA               ; {hard.workRam+3AA} the stage indexes the timer-limit table
A86C: AD 25 01        LDA     $0125               ; {hard.workRam+125}
A86F: DD 83 A8        CMP     $A883,X             ; {hard.rom+1883} phase reached its limit?
A872: 90 05           BCC     $A879               ; {code.loc_a879}
A874: A9 00           LDA     #$00                ; phase done -> reset the latch
A876: 8D 25 01        STA     $0125               ; {hard.workRam+125}

loc_a879:
A879: 20 88 A8        JSR     $A888               ; {code.sweepLaneSlotsForRespawn} run the lane-respawn sweep

loc_a87c:
A87C: A5 4E           LDA     $4E                 ; {hard.workRam+4E} always clear the input-edge bit7 on the way out
A87E: 29 7F           AND     #$7F                
A880: 85 4E           STA     $4E                 ; {hard.workRam+4E}
A882: 60              RTS                         

; ---- $A883-$A887: data ----
A883: 00 13 05 00 00

; on the timed phase (phase cell 0x125 >= 3 and even) sweep 0x2df,y
; downward from y=0x11c for the first nonzero slot: on a hit clear the low
; two bits of 0x28a,y and tail-delegate to respawnEnemyAndAward, on no hit
; reset 0x125 to 0.
sweepLaneSlotsForRespawn:
A888: AD 25 01        LDA     $0125               ; {hard.workRam+125} only sweep once the phase reaches 3
A88B: C9 03           CMP     #$03                
A88D: 90 14           BCC     $A8A3               ; {code.loc_a8a3}
A88F: 29 01           AND     #$01                ; and only on even phases
A891: D0 10           BNE     $A8A3               ; {code.loc_a8a3}
A893: AC 1C 01        LDY     $011C               ; {hard.workRam+11C} scan the slots from the top

loc_a896:
A896: B9 DF 02        LDA     $02DF,Y             ; {hard.workRam+2DF} first occupied lane is the hit
A899: D0 09           BNE     $A8A4               ; {code.loc_a8a4}
A89B: 88              DEY                         ; keep scanning
A89C: 10 F8           BPL     $A896               ; {code.loc_a896}
A89E: A9 00           LDA     #$00                ; nothing occupied -> mark the phase done
A8A0: 8D 25 01        STA     $0125               ; {hard.workRam+125}

loc_a8a3:
A8A3: 60              RTS                         

loc_a8a4:
A8A4: B9 8A 02        LDA     $028A,Y             ; {hard.workRam+28A} clear the found slot's low two direction bits
A8A7: 29 FC           AND     #$FC                
A8A9: 99 8A 02        STA     $028A,Y             ; {hard.workRam+28A} store back the masked direction
A8AC: 4C 98 A3        JMP     $A398               ; {code.respawnEnemyAndAward} respawn the enemy and award its points

; ---- $A8AF-$A8B3: data ----
A8AF: E1 24 26 28 2A

; compose the per-frame text/marker overlay into buffer 0x2f60: mirror
; control 0x72, refresh the header (emitColorStatIfChanged), and when 0x5
; bit7 is clear pick a marker slot, draw it
; (drawSlotShapeRecord/emitFixedVectorWord) and duplicate a glyph snapshot
; into 0x2fa6/0x2fa8; emit glyph strings via
; buildMarkerRowVectorList/buildTextBufferDigitString; off the safe mode
; (0x0!=0x04) rebuild checksum 0x16c and a 3-entry mirror; then emit the
; framing word (emitCoordinateVectorWord) and, in the active phase, the
; indexed slot pair (0x102) and two trailing markers.
buildTextOverlayList:
A8B4: A9 01           LDA     #$01                ; seed the last-stat cell
A8B6: 85 72           STA     $72                 ; {hard.workRam+72}
A8B8: 20 6A DF        JSR     $DF6A               ; {code.emitBlankVectorWordTag70} lead the list with the blank/tag-70 word
A8BB: A0 05           LDY     #$05                
A8BD: 20 D1 B0        JSR     $B0D1               ; {code.emitColorStatIfChanged} refresh the colour-stat header
A8C0: A5 05           LDA     $05                 ; {hard.workRam+5} skip the live-glyph block in attract mode
A8C2: 30 26           BMI     $A8EA               ; {code.loc_a8ea}
A8C4: A2 00           LDX     #$00                
A8C6: A5 03           LDA     $03                 ; {hard.workRam+3} pick the marker shape from the frame phase
A8C8: 29 20           AND     #$20                
A8CA: D0 0C           BNE     $A8D8               ; {code.loc_a8d8} frame bit set -> first marker shape
A8CC: A2 22           LDX     #$22                
A8CE: A5 06           LDA     $06                 ; {hard.workRam+6}
A8D0: F0 06           BEQ     $A8D8               ; {code.loc_a8d8} idle phase -> alternate marker shape
A8D2: 24 A2           BIT     $A2                 ; {hard.workRam+A2} or the phase sign flag -> alternate marker shape
A8D4: 30 02           BMI     $A8D8               ; {code.loc_a8d8}
A8D6: A2 06           LDX     #$06                

loc_a8d8:
A8D8: 20 14 AB        JSR     $AB14               ; {code.drawSlotShapeRecord} draw the chosen marker slot shape
A8DB: 20 0D AB        JSR     $AB0D               ; {code.emitFixedVectorWord} emit the fixed vector word
A8DE: AD E4 31        LDA     $31E4               ; {hard.vectorRom+1E4} read the glyph snapshot
A8E1: 8D A6 2F        STA     $2FA6               ; {hard.vectorRam+FA6} mirror it into the first snapshot cell
A8E4: 8D A8 2F        STA     $2FA8               ; {hard.vectorRam+FA8} and the second snapshot cell

; compose one frame's full display list: draw the base overlay
; (drawOverlayFrame), emit the base list (buildMarkerRowVectorList) and —
; when the flag source is live (loc_3e while loc_5 bit7 set, else
; loc_43|loc_44|loc_45) — a second list; unless loc_00==0x04 rebuild the
; self-check byte loc_16c by XOR-folding 0xa7 over eleven bytes at $AACE
; and rebuild the strided mirror $2F60 from loc_61b through $31FA; emit
; framing word emitCoordinateVectorWord, draw slot 0x36 when loc_123 bit7
; set, and when loc_00==0x18 with loc_5 bit7 set draw slots 0x30 (+numeric
; run) / 0x3a / 0x38.
composeFrameDisplayList:
A8E7: 20 A8 AA        JSR     $AAA8               ; {code.drawOverlayFrame} draw the recurring base overlay

loc_a8ea:
A8EA: A9 01           LDA     #$01                
A8EC: A0 00           LDY     #$00                
A8EE: 20 7F A9        JSR     $A97F               ; {code.buildMarkerRowVectorList} emit the first marker row
A8F1: 24 05           BIT     $05                 ; {hard.workRam+5} attract mode -> gate the second row on the active-slot count
A8F3: 30 09           BMI     $A8FE               ; {code.loc_a8fe}
A8F5: A5 43           LDA     $43                 ; {hard.workRam+43} else gate on the score/status flags
A8F7: 05 44           ORA     $44                 ; {hard.workRam+44}
A8F9: 05 45           ORA     $45                 ; {hard.workRam+45}
A8FB: B8              CLV                         
A8FC: 50 02           BVC     $A900               ; {code.loc_a900}

loc_a8fe:
A8FE: A5 3E           LDA     $3E                 ; {hard.workRam+3E} attract: the active-slot count

loc_a900:
A900: F0 06           BEQ     $A908               ; {code.loc_a908} no gate -> skip the second row
A902: A9 01           LDA     #$01                
A904: A8              TAY                         
A905: 20 7F A9        JSR     $A97F               ; {code.buildMarkerRowVectorList} emit the second marker row

loc_a908:
A908: A5 00           LDA     $00                 ; {hard.workRam} mode 4 skips the text and self-check rebuild
A90A: C9 04           CMP     #$04                
A90C: F0 35           BEQ     $A943               ; {code.loc_a943}
A90E: A9 1D           LDA     #$1D                ; aim the work pointer at the glyph source
A910: 85 3B           STA     $3B                 ; {hard.workRam+3B}
A912: A9 07           LDA     #$07                
A914: 85 3C           STA     $3C                 ; {hard.workRam+3C}
A916: AE E4 CD        LDX     $CDE4               ; {hard.rom+3DE4} load the glyph-buffer offset
A919: 20 D7 A9        JSR     $A9D7               ; {code.buildTextBufferDigitString} build the digit/glyph text buffer
A91C: A0 0A           LDY     #$0A                
A91E: A9 A7           LDA     #$A7                ; seed the self-check fold

loc_a920:
A920: 59 CE AA        EOR     $AACE,Y             ; {hard.rom+1ACE} XOR-fold the self-check byte table
A923: 88              DEY                         
A924: 10 FA           BPL     $A920               ; {code.loc_a920}
A926: 8D 6C 01        STA     $016C               ; {hard.workRam+16C} publish the self-check byte
A929: AE E5 CD        LDX     $CDE5               ; {hard.rom+3DE5} load the mirror destination offset
A92C: A9 02           LDA     #$02                ; three doubled glyph entries
A92E: 85 38           STA     $38                 ; {hard.workRam+38}

loc_a930:
A930: A4 38           LDY     $38                 ; {hard.workRam+38}
A932: B9 1B 06        LDA     $061B,Y             ; {hard.workRam+61B} index the glyph through the source table
A935: 0A              ASL     A                   ; double the index
A936: A8              TAY                         
A937: B9 FA 31        LDA     $31FA,Y             ; {hard.vectorRom+1FA} read the glyph word
A93A: 9D 60 2F        STA     $2F60,X             ; {hard.vectorRam+F60} copy it into the strided mirror
A93D: E8              INX                         
A93E: E8              INX                         
A93F: C6 38           DEC     $38                 ; {hard.workRam+38} next entry
A941: 10 ED           BPL     $A930               ; {code.loc_a930}

loc_a943:
A943: A9 2F           LDA     #$2F                
A945: A2 60           LDX     #$60                
A947: 20 39 DF        JSR     $DF39               ; {code.emitCoordinateVectorWord} post the framing coordinate word
A94A: AD 23 01        LDA     $0123               ; {hard.workRam+123} spiked-segment marker only when its high bit is set
A94D: 10 05           BPL     $A954               ; {code.loc_a954}
A94F: A2 36           LDX     #$36                
A951: 20 14 AB        JSR     $AB14               ; {code.drawSlotShapeRecord} draw the spike marker slot

loc_a954:
A954: A5 00           LDA     $00                 ; {hard.workRam}
A956: C9 18           CMP     #$18                ; tail decorations only in mode 0x18
A958: D0 22           BNE     $A97C               ; {code.loc_a97c}
A95A: A5 05           LDA     $05                 ; {hard.workRam+5}
A95C: 10 1E           BPL     $A97C               ; {code.loc_a97c} and only with the status flag set
A95E: A6 3D           LDX     $3D                 ; {hard.workRam+3D}
A960: BD 02 01        LDA     $0102,X             ; {hard.workRam+102} draw only when the current slot is live
A963: F0 0D           BEQ     $A972               ; {code.loc_a972}
A965: A2 30           LDX     #$30                
A967: 20 14 AB        JSR     $AB14               ; {code.drawSlotShapeRecord} draw the labelled slot record
A96A: A4 3D           LDY     $3D                 ; {hard.workRam+3D}
A96C: BE 02 01        LDX     $0102,Y             ; {hard.workRam+102}
A96F: 20 C6 B0        JSR     $B0C6               ; {code.emitTableValueDigitRun} emit its numeric value run

loc_a972:
A972: A2 3A           LDX     #$3A                
A974: 20 14 AB        JSR     $AB14               ; {code.drawSlotShapeRecord} draw a trailing marker slot
A977: A2 38           LDX     #$38                
A979: 20 14 AB        JSR     $AB14               ; {code.drawSlotShapeRecord} draw a trailing marker slot

loc_a97c:
A97C: 60              RTS                         

; ---- $A97D-$A97E: data ----
A97D: 42 45

; Lays a header byte at $2F60 (zeroed only when row index y equals the
; marker loc_3d with loc_5 bit7 set), fills seven glyph entries from
; $3284/$3286, and unless state 4 away from the marker seeds the glyph
; pointer loc_3b/loc_3c and hands off to the digit-string builder.
buildMarkerRowVectorList:
A97F: A6 00           LDX     $00                 ; {hard.workRam}
A981: E0 04           CPX     #$04                
A983: 84 2B           STY     $2B                 ; {hard.workRam+2B} stash the row index in scratch
A985: C4 3D           CPY     $3D                 ; {hard.workRam+3D} is this row the currently selected marker
A987: D0 06           BNE     $A98F               ; {code.loc_a98f} skip the head-blank unless this is the marker row
A989: 24 05           BIT     $05                 ; {hard.workRam+5} test the marker-active flag
A98B: 10 02           BPL     $A98F               ; {code.loc_a98f} skip unless the marker-active bit is set
A98D: A9 00           LDA     #$00                ; blank the row head so the highlight can overdraw it

loc_a98f:
A98F: 09 70           ORA     #$70                ; or in the 0x70 vector tag for the head word
A991: BE DE CD        LDX     $CDDE,Y             ; {hard.rom+3DDE} head-word offset for this row
A994: 9D 60 2F        STA     $2F60,X             ; {hard.vectorRam+F60} write the head word into the glyph buffer
A997: BE E0 CD        LDX     $CDE0,Y             ; {hard.rom+3DE0} glyph-slot offset for this row
A99A: B9 48 00        LDA     $0048,Y             ; {hard.workRam+48} the row's filled-tick count
A99D: 85 38           STA     $38                 ; {hard.workRam+38} seed the count cursor
A99F: F0 06           BEQ     $A9A7               ; {code.loc_a9a7} skip the dock when the count is zero
A9A1: C4 3D           CPY     $3D                 ; {hard.workRam+3D} is this the selected marker row
A9A3: D0 02           BNE     $A9A7               ; {code.loc_a9a7} skip unless the marker row
A9A5: C6 38           DEC     $38                 ; {hard.workRam+38} the selected row shows one fewer filled tick

loc_a9a7:
A9A7: A0 01           LDY     #$01                ; start at glyph slot 1

loc_a9a9:
A9A9: AD 84 32        LDA     $3284               ; {hard.vectorRom+284} filled-tick glyph
A9AC: C4 38           CPY     $38                 ; {hard.workRam+38} slot index vs the tick count
A9AE: 90 05           BCC     $A9B5               ; {code.loc_a9b5} slots up to the count get the filled glyph
A9B0: F0 03           BEQ     $A9B5               ; {code.loc_a9b5} the slot at the count gets the filled glyph too
A9B2: AD 86 32        LDA     $3286               ; {hard.vectorRom+286} past the count -- the empty-tick glyph

loc_a9b5:
A9B5: 9D 60 2F        STA     $2F60,X             ; {hard.vectorRam+F60} write the glyph into the buffer
A9B8: E8              INX                         ; advance two bytes -- one glyph plus its tag
A9B9: E8              INX                         
A9BA: C8              INY                         ; next slot
A9BB: C0 07           CPY     #$07                ; seven glyph slots per row
A9BD: 90 EA           BCC     $A9A9               ; {code.loc_a9a9} loop the seven slots
A9BF: A4 2B           LDY     $2B                 ; {hard.workRam+2B} restore the row index
A9C1: A5 00           LDA     $00                 ; {hard.workRam} read the game mode
A9C3: C9 04           CMP     #$04                ; mode 4
A9C5: D0 04           BNE     $A9CB               ; {code.loc_a9cb} otherwise go on to emit the number
A9C7: C4 3D           CPY     $3D                 ; {hard.workRam+3D} is this the marker row
A9C9: D0 30           BNE     $A9FB               ; {code.loc_a9fb} in mode 4, skip the number on non-marker rows

loc_a9cb:
A9CB: BE E2 CD        LDX     $CDE2,Y             ; {hard.rom+3DE2} buffer cursor for this row's digit string
A9CE: B9 7D A9        LDA     $A97D,Y             ; {hard.rom+197D} low byte of the digit-source pointer
A9D1: 85 3B           STA     $3B                 ; {hard.workRam+3B} seat the source pointer low
A9D3: A9 00           LDA     #$00                
A9D5: 85 3C           STA     $3C                 ; {hard.workRam+3C} source high byte 0 -- the digits live in zero page

; Walks three source bytes backward (pointer loc_3b/loc_3c) emitting each
; byte's high then low nibble into the text buffer, threading carry so
; only the final low nibble on the last pass sees it cleared.
buildTextBufferDigitString:
A9D7: A0 02           LDY     #$02                ; three digit passes -- two down to zero
A9D9: 84 2A           STY     $2A                 ; {hard.workRam+2A} seat the pass counter
A9DB: 38              SEC                         ; set the leading-zero suppress flag

loc_a9dc:
A9DC: 08              PHP                         ; carry the suppress flag across the high-nibble emit
A9DD: A0 00           LDY     #$00                
A9DF: B1 3B           LDA     ($3B),Y             ; {hard.workRam+3B} read the packed-BCD source byte
A9E1: 4A              LSR     A                   ; shift the high nibble down
A9E2: 4A              LSR     A                   
A9E3: 4A              LSR     A                   
A9E4: 4A              LSR     A                   
A9E5: 28              PLP                         ; restore the suppress carry
A9E6: 20 FC A9        JSR     $A9FC               ; {code.writeNibbleGlyphToTextBuffer} emit the high-nibble digit glyph
A9E9: A5 2A           LDA     $2A                 ; {hard.workRam+2A} the pass counter
A9EB: D0 01           BNE     $A9EE               ; {code.loc_a9ee} on the final pass only
A9ED: 18              CLC                         ; clear suppress so the units digit always prints

loc_a9ee:
A9EE: A0 00           LDY     #$00                
A9F0: B1 3B           LDA     ($3B),Y             ; {hard.workRam+3B} reread the byte for its low nibble
A9F2: 20 FC A9        JSR     $A9FC               ; {code.writeNibbleGlyphToTextBuffer} emit the low-nibble digit glyph
A9F5: C6 3B           DEC     $3B                 ; {hard.workRam+3B} walk the source pointer back one byte
A9F7: C6 2A           DEC     $2A                 ; {hard.workRam+2A} count down the passes
A9F9: 10 E1           BPL     $A9DC               ; {code.loc_a9dc} loop until the pass counter underflows

loc_a9fb:
A9FB: 60              RTS                         

; Maps A's low nibble to a stroke byte from ROM table $31E4, stores it at
; the text-buffer cursor $2F60+x, and advances x by two.
writeNibbleGlyphToTextBuffer:
A9FC: 29 0F           AND     #$0F                ; take the low nibble -- the digit value
A9FE: A8              TAY                         
A9FF: F0 01           BEQ     $AA02               ; {code.loc_aa02} is the nibble zero
AA01: 18              CLC                         ; a nonzero digit clears the leading-zero suppress

loc_aa02:
AA02: B0 01           BCS     $AA05               ; {code.loc_aa05} a suppressed leading zero selects the blank glyph
AA04: C8              INY                         ; otherwise index the digit's own glyph

loc_aa05:
AA05: 08              PHP                         
AA06: 98              TYA                         
AA07: 0A              ASL     A                   ; double the index -- two bytes per glyph entry
AA08: A8              TAY                         
AA09: B9 E4 31        LDA     $31E4,Y             ; {hard.vectorRom+1E4} fetch the digit's stroke byte from the glyph table
AA0C: 9D 60 2F        STA     $2F60,X             ; {hard.vectorRam+F60} store it into the text buffer at the cursor
AA0F: E8              INX                         ; advance the cursor
AA10: E8              INX                         ; past this two-byte glyph
AA11: 28              PLP                         
AA12: 60              RTS                         

; stage a text line into the vector text buffer at 0x2f60: pick a string
; index in loc_3e (forced to 0x01 when loc_5 bit7 is clear and any of
; loc_43/loc_44/loc_45 is set), seat the write cursor loc_74/loc_75 at
; 0x2f60, copy $CE66[index]+1 stroke bytes from ROM $CDE6 into it, and on
; the loc_5 bit7 path also emit the BCD of (loc_9f+1) at 0x2fa6 before
; restoring the cursor low byte and terminating the record via
; emitRecordBodyC0.
stageTextLineWithCount:
AA13: A6 3E           LDX     $3E                 ; {hard.workRam+3E} default template index -- the active slot count
AA15: 24 05           BIT     $05                 ; {hard.workRam+5} test the status flag bit7
AA17: 30 0A           BMI     $AA23               ; {code.loc_aa23} bit7 set -- keep the default template
AA19: A5 43           LDA     $43                 ; {hard.workRam+43} combine the loc_43/44/45 trio
AA1B: 05 44           ORA     $44                 ; {hard.workRam+44} fold in loc_44
AA1D: 05 45           ORA     $45                 ; {hard.workRam+45} fold in loc_45
AA1F: F0 02           BEQ     $AA23               ; {code.loc_aa23} all zero -- keep the default template
AA21: A2 01           LDX     #$01                ; any of the trio set -- force template index 1

loc_aa23:
AA23: A9 60           LDA     #$60                ; write cursor low byte
AA25: 85 74           STA     $74                 ; {hard.workRam+74} seat the cursor low
AA27: A9 2F           LDA     #$2F                ; write cursor high byte
AA29: 85 75           STA     $75                 ; {hard.workRam+75} seat the cursor high -- text buffer at 0x2f60
AA2B: BD 66 CE        LDA     $CE66,X             ; {hard.rom+3E66} template byte length from the length table
AA2E: A8              TAY                         
AA2F: 38              SEC                         
AA30: 65 74           ADC     $74                 ; {hard.workRam+74} length plus cursor low
AA32: 48              PHA                         ; save the post-copy cursor low

loc_aa33:
AA33: B9 E6 CD        LDA     $CDE6,Y             ; {hard.rom+3DE6} copy a stroke byte from the template block
AA36: 91 74           STA     ($74),Y             ; {hard.workRam+74} into the text buffer
AA38: 88              DEY                         ; step down the copy counter
AA39: D0 F8           BNE     $AA33               ; {code.loc_aa33} copy the template down toward index 0
AA3B: B9 E6 CD        LDA     $CDE6,Y             ; {hard.rom+3DE6} final stroke byte at index 0
AA3E: 91 74           STA     ($74),Y             ; {hard.workRam+74} store it
AA40: A5 05           LDA     $05                 ; {hard.workRam+5} read the status flags
AA42: 10 10           BPL     $AA54               ; {code.loc_aa54} bit7 clear -- skip the live count
AA44: A9 2F           LDA     #$2F                
AA46: 85 75           STA     $75                 ; {hard.workRam+75} repoint the cursor high
AA48: A9 A6           LDA     #$A6                
AA4A: 85 74           STA     $74                 ; {hard.workRam+74} and low -- to the count field at 0x2fa6
AA4C: A5 9F           LDA     $9F                 ; {hard.workRam+9F} the count source
AA4E: 18              CLC                         
AA4F: 69 01           ADC     #$01                ; plus one
AA51: 20 77 AF        JSR     $AF77               ; {code.emitByteAsBcdDigits} render it as BCD digits

loc_aa54:
AA54: 68              PLA                         ; restore the saved cursor low
AA55: 85 74           STA     $74                 ; {hard.workRam+74} seat it back
AA57: 4C 09 DF        JMP     $DF09               ; {code.emitRecordBodyC0} tail into the record-close emitter

; compose a frame led by slot 0x08: draw slot 0x08 (drawSlotShapeRecord)
; then chain prepCountThenComposeFrame (the count prep followed by the
; per-frame composition $A8E7).
drawFrameWithSlot08:
AA5A: A2 08           LDX     #$08                ; lead this frame with draw slot 0x08
AA5C: 20 14 AB        JSR     $AB14               ; {code.drawSlotShapeRecord} draw that slot's shape record
AA5F: 4C 69 AA        JMP     $AA69               ; {code.prepCountThenComposeFrame} chain into the shared count-prep and frame composer

; compose a frame led by slot 0x00: prime slot 0x00 with header 0x30
; (drawSlotShapeWithHeader), run the shared count prep
; (drawSlotThenDigitRun), then dispatch the per-frame composition $A8E7.
drawFrameWithSlot00:
AA62: A9 30           LDA     #$30                ; header/colour seed 0x30
AA64: A2 00           LDX     #$00                ; lead with slot 0x00 -- the player/overlay slot
AA66: 20 17 AB        JSR     $AB17               ; {code.drawSlotShapeWithHeader} draw that slot's record with the given header

; run the shared count prep (drawSlotThenDigitRun: slot 0x02 + digit run)
; then dispatch the per-frame composition $A8E7.
prepCountThenComposeFrame:
AA69: 20 92 AA        JSR     $AA92               ; {code.drawSlotThenDigitRun} count prep -- draw slot 0x02 and lay the digit run
AA6C: 4C E7 A8        JMP     $A8E7               ; {code.composeFrameDisplayList} hand to the per-frame composition driver

; run the alternate per-frame composition $A8B4, then prime slot 0x06
; through the shared entry drawSlotShapeWithHeader (header 0x00).
composeFrameThenDrawSlot06:
AA6F: 20 B4 A8        JSR     $A8B4               ; {code.buildTextOverlayList} build the alternate text-overlay display list
AA72: A9 00           LDA     #$00                ; header seed 0x00
AA74: A2 06           LDX     #$06                ; slot 0x06
AA76: 4C 17 AB        JMP     $AB17               ; {code.drawSlotShapeWithHeader} append slot 0x06's shape record

; compose a frame led by slot 0x32: draw slot 0x32
; (drawSlotShapeWithHeader, header 0x00), add a second draw of slot 0x22
; (header 0xe0) only while status nibble loc_3&0x1f < 0x10, then finish
; with the alternate per-frame composition $A8B4.
drawFrameWithSlot32:
AA79: A9 00           LDA     #$00                ; header seed 0x00
AA7B: A2 32           LDX     #$32                ; lead with slot 0x32
AA7D: 20 17 AB        JSR     $AB17               ; {code.drawSlotShapeWithHeader} draw that slot's shape record
AA80: A5 03           LDA     $03                 ; {hard.workRam+3} read the frame counter
AA82: 29 1F           AND     #$1F                ; low bits of the 32-frame cycle
AA84: C9 10           CMP     #$10                ; in the first sixteen frames
AA86: B0 07           BCS     $AA8F               ; {code.loc_aa8f} skip the blink slot in the second half
AA88: A9 E0           LDA     #$E0                ; header seed 0xe0
AA8A: A2 22           LDX     #$22                ; slot 0x22
AA8C: 20 17 AB        JSR     $AB17               ; {code.drawSlotShapeWithHeader} draw it only in the first half -- a 50%-duty blink

loc_aa8f:
AA8F: 4C B4 A8        JMP     $A8B4               ; {code.buildTextOverlayList} finish through the text-overlay builder

; draw fixed slot 0x02 (drawSlotShapeRecord) then hand off to
; emitCountDigitRun to lay down the numeric run.
drawSlotThenDigitRun:
AA92: A2 02           LDX     #$02                ; the fixed slot 0x02
AA94: 20 14 AB        JSR     $AB14               ; {code.drawSlotShapeRecord} draw its shape record

; publish a zero scale header (emitScaleWordIfChanged with 0x00) then emit
; the one-byte digit run for the slot named by loc_3d via $AA9E, drawing
; the count as nibble digits.
emitCountDigitRun:
AA97: A9 00           LDA     #$00                ; baseline scale value 0
AA99: 20 DD B0        JSR     $B0DD               ; {code.emitScaleWordIfChanged} set the vector scale to baseline, emit only if it changed
AA9C: A6 3D           LDX     $3D                 ; {hard.workRam+3D} the slot index named by loc_3d

; Increments the slot index, publishes it into loc_61, and emits that
; single byte as a digit run.
emitSlotIndexDigit:
AA9E: E8              INX                         ; advance the slot index by one
AA9F: 86 61           STX     $61                 ; {hard.workRam+61} publish it into the byte the digit emitter reads
AAA1: A9 61           LDA     #$61                ; source pointer 0x61
AAA3: A0 01           LDY     #$01                ; one byte long
AAA5: 4C B1 DF        JMP     $DFB1               ; {code.emitNibbleDigitRun} emit it as a single digit glyph

; the recurring per-frame overlay driver: draw the phase-selected slot
; from ROM table $A8B0[loc_9&0x03], tick timer loc_16e down, draw either
; alternate slot 0x32 (when loc_a bit0 set and loc_3 bit5 clear) or defer
; to computeDisplayListChecksum, always redraw marker slot 0x2c and slot
; 0x2e, clamp loc_6 to ceiling 0x28 and emit it via emitByteAsBcdDigits,
; and when loc_17 is nonzero post a final coordinate word
; (emitCoordinateVectorWord from $AAF4/$AAF3).
drawOverlayFrame:
AAA8: A5 09           LDA     $09                 ; {hard.workRam+9} the config-switch snapshot
AAAA: 29 03           AND     #$03                ; its low two bits
AAAC: AA              TAX                         
AAAD: BD B0 A8        LDA     $A8B0,X             ; {hard.rom+18B0} pick a shape id from the slot table
AAB0: AA              TAX                         
AAB1: 20 14 AB        JSR     $AB14               ; {code.drawSlotShapeRecord} draw the config-selected slot
AAB4: CE 6E 01        DEC     $016E               ; {hard.workRam+16E} tick down the display countdown timer
AAB7: A5 0A           LDA     $0A                 ; {hard.workRam+A} the second config snapshot
AAB9: 29 01           AND     #$01                ; bit 0
AABB: F0 0E           BEQ     $AACB               ; {code.loc_aacb} clear -- spend the slot on the checksum instead
AABD: A5 03           LDA     $03                 ; {hard.workRam+3} the frame counter
AABF: 29 20           AND     #$20                ; phase-gate bit
AAC1: D0 08           BNE     $AACB               ; {code.loc_aacb} gate high -- take the checksum path
AAC3: A2 32           LDX     #$32                ; alternate slot 0x32
AAC5: 20 14 AB        JSR     $AB14               ; {code.drawSlotShapeRecord} draw it
AAC8: B8              CLV                         
AAC9: 50 03           BVC     $AACE               ; {code.loc_aace} skip the checksum this frame

loc_aacb:
AACB: 20 CA AE        JSR     $AECA               ; {code.computeDisplayListChecksum} recompute the display-list checksum

loc_aace:
AACE: A2 2C           LDX     #$2C                ; fixed marker slot 0x2c
AAD0: 20 14 AB        JSR     $AB14               ; {code.drawSlotShapeRecord} draw it
AAD3: A2 2E           LDX     #$2E                ; fixed marker slot 0x2e
AAD5: 20 14 AB        JSR     $AB14               ; {code.drawSlotShapeRecord} draw it
AAD8: A5 06           LDA     $06                 ; {hard.workRam+6} the level/phase index
AADA: C9 28           CMP     #$28                ; against its ceiling 0x28
AADC: 90 04           BCC     $AAE2               ; {code.loc_aae2} below -- keep it
AADE: A9 28           LDA     #$28                ; clamp to 0x28
AAE0: 85 06           STA     $06                 ; {hard.workRam+6} store the clamp

loc_aae2:
AAE2: 20 77 AF        JSR     $AF77               ; {code.emitByteAsBcdDigits} draw the phase index as BCD digits
AAE5: A5 17           LDA     $17                 ; {hard.workRam+17} the heartbeat accumulator high byte
AAE7: F0 09           BEQ     $AAF2               ; {code.loc_aaf2} skip the trailing word while it is zero
AAE9: AD F4 AA        LDA     $AAF4               ; {hard.rom+1AF4} trailing coordinate word, low byte
AAEC: AE F3 AA        LDX     $AAF3               ; {hard.rom+1AF3} and high byte
AAEF: 20 39 DF        JSR     $DF39               ; {code.emitCoordinateVectorWord} post it into the display list

loc_aaf2:
AAF2: 60              RTS                         

; ---- $AAF3-$AAF4: data ----
AAF3: 5C 32

; Converts the binary byte in A to packed BCD by double-dabble and writes
; the packed digits into loc_29 and loc_2c.
packBinaryToBcd:
AAF5: F8              SED                         ; switch the CPU to decimal mode for the conversion
AAF6: 85 29           STA     $29                 ; {hard.workRam+29} the binary byte to convert
AAF8: A9 00           LDA     #$00                
AAFA: 85 2C           STA     $2C                 ; {hard.workRam+2C} clear the BCD accumulator
AAFC: A0 07           LDY     #$07                ; eight double-dabble passes

loc_aafe:
AAFE: 06 29           ASL     $29                 ; {hard.workRam+29} shift the top bit out of the source byte
AB00: A5 2C           LDA     $2C                 ; {hard.workRam+2C} load the accumulator
AB02: 65 2C           ADC     $2C                 ; {hard.workRam+2C} double it in decimal, folding in that bit
AB04: 85 2C           STA     $2C                 ; {hard.workRam+2C} back to the accumulator
AB06: 88              DEY                         
AB07: 10 F5           BPL     $AAFE               ; {code.loc_aafe} repeat for all eight bits
AB09: D8              CLD                         ; back to binary mode
AB0A: 85 29           STA     $29                 ; {hard.workRam+29} publish the packed-BCD result
AB0C: 60              RTS                         

; emit one fixed vector word (bytes 0x20, 0x80) through the draw cursor
; 0x74 and step past it (via $DF57).
emitFixedVectorWord:
AB0D: A9 20           LDA     #$20                ; constant vector word, low byte
AB0F: A2 80           LDX     #$80                ; high byte
AB11: 4C 57 DF        JMP     $DF57               ; {code.emitVectorWord} emit it through the draw cursor

; draw slot x's object record into the display list at cursor (loc_74):
; latch slot into loc_35, take the colour/header seed from ROM $D122+x
; into loc_2b, load the slot's shape-list pointer from (loc_ac)+x into
; loc_3b/loc_3c (snapshotting cursor into loc_b6/loc_b7 for marker slot
; 0x2c), position via loc_2a, split scale key $D121+loc_35 into
; emitColorStatIfChanged/emitScaleWordIfChanged, then walk the shape list
; copying point pairs from $31E4/$31E5 into (loc_74) until a high-bit
; terminator and close with advanceDisplayCursor.
drawSlotShapeRecord:
AB14: BD 22 D1        LDA     $D122,X             ; {hard.rom+4122} fetch the slot's colour/header seed from the ROM table

; draw slot x's object record like drawSlotShapeRecord but take the loc_2b
; colour/header seed from the argument a instead of ROM $D122: latch
; loc_35=x, loc_2b=a, load shape-list pointer (loc_ac)+x, set scale from
; $D121, expand the shape list of point pairs ($31E4/$31E5) into (loc_74)
; and close with advanceDisplayCursor.
drawSlotShapeWithHeader:
AB17: 86 35           STX     $35                 ; {hard.workRam+35} remember the slot index
AB19: 85 2B           STA     $2B                 ; {hard.workRam+2B} the caller's colour/header seed
AB1B: A4 35           LDY     $35                 ; {hard.workRam+35}
AB1D: B1 AC           LDA     ($AC),Y             ; {hard.workRam+AC} shape-list pointer low from the per-slot table
AB1F: 85 3B           STA     $3B                 ; {hard.workRam+3B} seat the pointer low
AB21: C8              INY                         
AB22: B1 AC           LDA     ($AC),Y             ; {hard.workRam+AC} and the high byte
AB24: 85 3C           STA     $3C                 ; {hard.workRam+3C} seat the pointer high
AB26: E0 2C           CPX     #$2C                ; is this the marker slot 0x2c
AB28: D0 08           BNE     $AB32               ; {code.loc_ab32} if not, skip the snapshot
AB2A: A5 74           LDA     $74                 ; {hard.workRam+74} snapshot the draw cursor low so a later pass can find this record
AB2C: 85 B6           STA     $B6                 ; {hard.workRam+B6} store it
AB2E: A5 75           LDA     $75                 ; {hard.workRam+75} and the cursor high
AB30: 85 B7           STA     $B7                 ; {hard.workRam+B7} store it

loc_ab32:
AB32: A0 00           LDY     #$00                
AB34: B1 3B           LDA     ($3B),Y             ; {hard.workRam+3B} the record's first byte -- its position
AB36: 85 2A           STA     $2A                 ; {hard.workRam+2A} seat the position
AB38: 20 0D AB        JSR     $AB0D               ; {code.emitFixedVectorWord} emit the fixed framing word

; the shared tail all three builders converge on: with
; loc_2a/loc_2b/loc_35 pre-seeded, clear loc_73, set loc_72=0x01, emit the
; intensity header (emitBlankVectorWordTag70) and beam-position record
; (emitScaledCoordinateRecord), reload the shape-list pointer from
; (loc_ac)+loc_35, split scale key $D121+loc_35 into
; emitColorStatIfChanged/emitScaleWordIfChanged, then walk the list
; copying point pairs from $31E4/$31E5 into (loc_74) until a high-bit
; terminator and close with advanceDisplayCursor.
expandShapeListToVectors:
AB3B: A9 00           LDA     #$00                
AB3D: 85 73           STA     $73                 ; {hard.workRam+73} clear the vector-record header cell
AB3F: A9 01           LDA     #$01                
AB41: 85 72           STA     $72                 ; {hard.workRam+72} seed the last-status latch = 1
AB43: 20 6A DF        JSR     $DF6A               ; {code.emitBlankVectorWordTag70} emit the blank/intensity vector header word
AB46: A5 2A           LDA     $2A                 ; {hard.workRam+2A}
AB48: A6 2B           LDX     $2B                 ; {hard.workRam+2B}
AB4A: 20 75 DF        JSR     $DF75               ; {code.emitScaledCoordinateRecord} emit the scaled beam move to the shape's position
AB4D: A4 35           LDY     $35                 ; {hard.workRam+35} load this shape's slot index
AB4F: B1 AC           LDA     ($AC),Y             ; {hard.workRam+AC} read the shape's coordinate-list pointer low from the slot table
AB51: 85 3B           STA     $3B                 ; {hard.workRam+3B}
AB53: C8              INY                         
AB54: B1 AC           LDA     ($AC),Y             ; {hard.workRam+AC} read the pointer high from the next table byte
AB56: 85 3C           STA     $3C                 ; {hard.workRam+3C}
AB58: A6 35           LDX     $35                 ; {hard.workRam+35}
AB5A: BD 21 D1        LDA     $D121,X             ; {hard.rom+4121} read this shape's packed colour/scale key
AB5D: 48              PHA                         
AB5E: 4A              LSR     A                   
AB5F: 4A              LSR     A                   
AB60: 4A              LSR     A                   
AB61: 4A              LSR     A                   
AB62: A8              TAY                         
AB63: 20 D1 B0        JSR     $B0D1               ; {code.emitColorStatIfChanged} set the beam colour from the key's high nibble
AB66: 68              PLA                         
AB67: 29 0F           AND     #$0F                
AB69: 20 DD B0        JSR     $B0DD               ; {code.emitScaleWordIfChanged} set the draw scale from the key's low nibble
AB6C: A0 01           LDY     #$01                
AB6E: A9 00           LDA     #$00                
AB70: 85 2A           STA     $2A                 ; {hard.workRam+2A} reset the output offset

loc_ab72:
AB72: B1 3B           LDA     ($3B),Y             ; {hard.workRam+3B} read the next point entry from the shape list
AB74: 85 2B           STA     $2B                 ; {hard.workRam+2B}
AB76: 29 7F           AND     #$7F                ; low 7 bits index the point-coordinate table
AB78: C8              INY                         
AB79: 84 2C           STY     $2C                 ; {hard.workRam+2C}
AB7B: AA              TAX                         
AB7C: BD E4 31        LDA     $31E4,X             ; {hard.vectorRom+1E4} fetch the point's low byte from the coordinate table
AB7F: A4 2A           LDY     $2A                 ; {hard.workRam+2A}
AB81: 91 74           STA     ($74),Y             ; {hard.workRam+74} write the point low byte into the display buffer
AB83: C8              INY                         
AB84: BD E5 31        LDA     $31E5,X             ; {hard.vectorRom+1E5} fetch the point's high byte
AB87: 91 74           STA     ($74),Y             ; {hard.workRam+74} write the point high byte into the display buffer
AB89: C8              INY                         
AB8A: 84 2A           STY     $2A                 ; {hard.workRam+2A}
AB8C: A4 2C           LDY     $2C                 ; {hard.workRam+2C}
AB8E: 24 2B           BIT     $2B                 ; {hard.workRam+2B} test the entry's terminator bit
AB90: 10 E0           BPL     $AB72               ; {code.loc_ab72} loop until an entry's high bit ends the shape list
AB92: A4 2A           LDY     $2A                 ; {hard.workRam+2A}
AB94: 88              DEY                         
AB95: 4C 5F DF        JMP     $DF5F               ; {code.advanceDisplayCursor} close the record, advancing the cursor past the points

; thin front over the shared builder: seat loc_35=x (slot), loc_2a=a
; (position seed), and a zero colour header loc_2b=0x00, then fall into
; expandShapeListToVectors to emit the slot's vector run.
drawShapeListAtPosition:
AB98: 86 35           STX     $35                 ; {hard.workRam+35} set which shape slot to draw
AB9A: 85 2A           STA     $2A                 ; {hard.workRam+2A} set the draw position seed
AB9C: A9 00           LDA     #$00                
AB9E: 85 2B           STA     $2B                 ; {hard.workRam+2B} clear the colour/flag header
ABA0: F0 99           BEQ     $AB3B               ; {code.expandShapeListToVectors} fall into the shared shape-list emitter

; guarded front for the rebuilder: refresh via $AC20, and if loc_1c9's low
; two request bits are clear take the no-op tail $AC07, otherwise run the
; rebuild path $ABAC.
rebuildControlBlocksIfRequested:
ABA2: 20 20 AC        JSR     $AC20               ; {code.requestRebuildIfSwitchesChanged} refresh the option-switch snapshot -- may request a rebuild
ABA5: AD C9 01        LDA     $01C9               ; {hard.workRam+1C9} read the pending-work flags
ABA8: 29 03           AND     #$03                ; test the two rebuild-request bits
ABAA: F0 5B           BEQ     $AC07               ; {code.noRebuildRequestReturn} no rebuild requested -- take the do-nothing tail

; control-block rebuilder: refresh via requestRebuildIfSwitchesChanged,
; write loc_100=0x08, raise the requests via raiseRebuildRequestBits when
; (loc_71b|loc_71c|loc_71d) are idle, then keyed on loc_1c9's low two bits
; copy template $AC08 into loc_606 (top 0x17 if bit0 else 0x0e) and fill
; loc_706 with 0x01 (top 0x17 if bit1 else 0x0e), latch
; loc_71e=(loc_a&0xf8)/loc_71f=(loc_16a&0x03) when any request bit was
; set, and clear the two request bits (loc_1c9 &= 0xfc).
rebuildControlBlocksFromTemplate:
ABAC: 20 20 AC        JSR     $AC20               ; {code.requestRebuildIfSwitchesChanged} refresh the option-switch snapshot -- may request a rebuild
ABAF: A9 08           LDA     #$08                
ABB1: 8D 00 01        STA     $0100               ; {hard.workRam+100} stamp the block-system state marker
ABB4: AD 1B 07        LDA     $071B               ; {hard.workRam+71B} gather the three activity sources
ABB7: 0D 1C 07        ORA     $071C               ; {hard.workRam+71C}
ABBA: 0D 1D 07        ORA     $071D               ; {hard.workRam+71D}
ABBD: D0 03           BNE     $ABC2               ; {code.loc_abc2} skip the force when any source is active
ABBF: 20 36 AC        JSR     $AC36               ; {code.raiseRebuildRequestBits} fully idle machine -- force both rebuild requests on

loc_abc2:
ABC2: A2 17           LDX     #$17                ; wider copy run when the copy bit is armed
ABC4: AD C9 01        LDA     $01C9               ; {hard.workRam+1C9} test the copy-block request bit
ABC7: 29 01           AND     #$01                
ABC9: D0 02           BNE     $ABCD               ; {code.loc_abcd}
ABCB: A2 0E           LDX     #$0E                ; narrower copy run otherwise

loc_abcd:
ABCD: BD 08 AC        LDA     $AC08,X             ; {hard.rom+1C08} read a template control-block byte
ABD0: 9D 06 06        STA     $0606,X             ; {hard.workRam+606} write it into the live control block
ABD3: CA              DEX                         
ABD4: 10 F7           BPL     $ABCD               ; {code.loc_abcd} loop over the block
ABD6: A2 17           LDX     #$17                
ABD8: AD C9 01        LDA     $01C9               ; {hard.workRam+1C9} test the glyph-fill request bit
ABDB: 29 02           AND     #$02                
ABDD: D0 02           BNE     $ABE1               ; {code.loc_abe1}
ABDF: A2 0E           LDX     #$0E                

loc_abe1:
ABE1: A9 01           LDA     #$01                
ABE3: 9D 06 07        STA     $0706,X             ; {hard.workRam+706} fill the glyph-parameter block with ones
ABE6: CA              DEX                         
ABE7: 10 F8           BPL     $ABE1               ; {code.loc_abe1} loop over the block
ABE9: AD C9 01        LDA     $01C9               ; {hard.workRam+1C9} test whether any request bit is set
ABEC: 29 03           AND     #$03                
ABEE: F0 0F           BEQ     $ABFF               ; {code.loc_abff} no rebuild happened -- skip the snapshot latch
ABF0: A5 0A           LDA     $0A                 ; {hard.workRam+A}
ABF2: 29 F8           AND     #$F8                
ABF4: 8D 1E 07        STA     $071E               ; {hard.workRam+71E} latch the option-switch snapshot (high bits)
ABF7: AD 6A 01        LDA     $016A               ; {hard.workRam+16A}
ABFA: 29 03           AND     #$03                
ABFC: 8D 1F 07        STA     $071F               ; {hard.workRam+71F} latch the difficulty snapshot (low bits)

loc_abff:
ABFF: AD C9 01        LDA     $01C9               ; {hard.workRam+1C9}
AC02: 29 FC           AND     #$FC                
AC04: 8D C9 01        STA     $01C9               ; {hard.workRam+1C9} clear the two rebuild-request bits, keep the rest

; no-op return tail taken by rebuildControlBlocksIfRequested when no
; rebuild request bit is set in loc_1c9; does nothing and returns.
noRebuildRequestReturn:
AC07: 60              RTS                         

; ---- $AC08-$AC1F: data ----
AC08: 07 04 01 0F 09 0C 0B 03 12 13 05 03 07 0F 0C 11
AC18: 11 11 12 04 03 03 09 04

; refresh the live option/switch snapshot via decodeOptionSwitches, then
; compare (loc_a & 0xf8) to cached loc_71e and (loc_16a & 0x03) to cached
; loc_71f: a match takes the no-op tail switchesUnchangedReturn, a
; mismatch calls raiseRebuildRequestBits to raise the pending-rebuild
; request bits.
requestRebuildIfSwitchesChanged:
AC20: 20 BB D6        JSR     $D6BB               ; {code.decodeOptionSwitches} re-read and decode the operator option switches
AC23: A5 0A           LDA     $0A                 ; {hard.workRam+A}
AC25: 29 F8           AND     #$F8                ; mask the option-switch high bits
AC27: CD 1E 07        CMP     $071E               ; {hard.workRam+71E} compare against the cached snapshot
AC2A: D0 08           BNE     $AC34               ; {code.loc_ac34} differ -- request a rebuild
AC2C: AD 6A 01        LDA     $016A               ; {hard.workRam+16A}
AC2F: 29 03           AND     #$03                
AC31: CD 1F 07        CMP     $071F               ; {hard.workRam+71F} compare difficulty against the cached snapshot

loc_ac34:
AC34: F0 08           BEQ     $AC3E               ; {code.switchesUnchangedReturn} switches unchanged -- take the no-op tail

; set both low request bits by OR-ing 0x03 into the pending-rebuild flags
; cell loc_1c9 and return the merged value.
raiseRebuildRequestBits:
AC36: AD C9 01        LDA     $01C9               ; {hard.workRam+1C9}
AC39: 09 03           ORA     #$03                ; arm both rebuild-request bits
AC3B: 8D C9 01        STA     $01C9               ; {hard.workRam+1C9} store the armed request flags

; shared no-op return tail taken by requestRebuildIfSwitchesChanged when
; the option/switch snapshot still matches the cached targets; does
; nothing and returns.
switchesUnchangedReturn:
AC3E: 60              RTS                         

; build a sound draw request: clear bit6 of loc_5, pre-clear the staging
; block via clearChannelStagingBlock when loc_9&0x43==0x40, zero total
; loc_601; for each of the two channels (0 or 3 by loc_3e) seat the key
; triple loc_2c/loc_2d/loc_2e from loc_42/loc_41/loc_40 and bubble-sort
; the row triples loc_620/loc_61f/loc_61e (with payload
; loc_51e/loc_51f/loc_520) into lexicographic order, counting settle
; passes in loc_605 stored to loc_600,channel; then nudge loc_601, derive
; the packed request byte loc_603 from loc_3d, and hand off to the request
; walker armRequestedSoundSlot.
buildSortedSoundRequest:
AC3F: A5 05           LDA     $05                 ; {hard.workRam+5}
AC41: 29 BF           AND     #$BF                
AC43: 85 05           STA     $05                 ; {hard.workRam+5} clear the request-in-progress flag
AC45: A5 09           LDA     $09                 ; {hard.workRam+9}
AC47: 29 43           AND     #$43                
AC49: C9 40           CMP     #$40                ; option-switch test gating the staging wipe
AC4B: D0 03           BNE     $AC50               ; {code.loc_ac50}
AC4D: 20 62 CA        JSR     $CA62               ; {code.clearChannelStagingBlock} wipe the sound staging block

loc_ac50:
AC50: 20 FB DD        JSR     $DDFB               ; {code.queueEaromRegionSave} fold in the periodic high-score save
AC53: A9 00           LDA     #$00                
AC55: 8D 01 06        STA     $0601               ; {hard.workRam+601} zero the running total
AC58: A6 3E           LDX     $3E                 ; {hard.workRam+3E} pick the starting channel from the active-slot count
AC5A: F0 02           BEQ     $AC5E               ; {code.loc_ac5e}
AC5C: A2 03           LDX     #$03                

loc_ac5e:
AC5E: B5 42           LDA     $42,X               ; {hard.workRam+42} seat this channel's sort-key triple from its base cells
AC60: 85 2C           STA     $2C                 ; {hard.workRam+2C}
AC62: B5 41           LDA     $41,X               ; {hard.workRam+41}
AC64: 85 2D           STA     $2D                 ; {hard.workRam+2D}
AC66: B5 40           LDA     $40,X               ; {hard.workRam+40}
AC68: 85 2E           STA     $2E                 ; {hard.workRam+2E}
AC6A: 8A              TXA                         
AC6B: 29 01           AND     #$01                
AC6D: 85 36           STA     $36                 ; {hard.workRam+36} remember the channel parity across the sort
AC6F: A9 00           LDA     #$00                
AC71: 85 2B           STA     $2B                 ; {hard.workRam+2B}
AC73: A9 1A           LDA     #$1A                ; seed the swap-temp triple
AC75: 85 2A           STA     $2A                 ; {hard.workRam+2A}
AC77: 85 29           STA     $29                 ; {hard.workRam+29}
AC79: A9 00           LDA     #$00                
AC7B: 8D 05 06        STA     $0605               ; {hard.workRam+605} clear this channel's pass counter
AC7E: A0 FD           LDY     #$FD                ; start the row cursor at the top

loc_ac80:
AC80: B9 20 06        LDA     $0620,Y             ; {hard.workRam+620}
AC83: C5 2C           CMP     $2C                 ; {hard.workRam+2C} compare this row's key high against the running key
AC85: D0 14           BNE     $AC9B               ; {code.loc_ac9b}
AC87: B9 1F 06        LDA     $061F,Y             ; {hard.workRam+61F}
AC8A: C5 2D           CMP     $2D                 ; {hard.workRam+2D} compare the key middle byte
AC8C: D0 0D           BNE     $AC9B               ; {code.loc_ac9b}
AC8E: C0 52           CPY     #$52                
AC90: 90 08           BCC     $AC9A               ; {code.loc_ac9a}
AC92: B9 1E 06        LDA     $061E,Y             ; {hard.workRam+61E}
AC95: C5 2E           CMP     $2E                 ; {hard.workRam+2E} compare the key low byte
AC97: B8              CLV                         
AC98: 50 01           BVC     $AC9B               ; {code.loc_ac9b}

loc_ac9a:
AC9A: 38              SEC                         

loc_ac9b:
AC9B: B0 4F           BCS     $ACEC               ; {code.loc_acec} rows already ordered -- skip the swap

loc_ac9d:
AC9D: C0 E8           CPY     #$E8                
AC9F: 90 1E           BCC     $ACBF               ; {code.loc_acbf} below the high region -- skip the payload swap
ACA1: A5 29           LDA     $29                 ; {hard.workRam+29}
ACA3: BE 1E 05        LDX     $051E,Y             ; {hard.workRam+51E}
ACA6: 99 1E 05        STA     $051E,Y             ; {hard.workRam+51E} swap the parallel payload triple alongside the key
ACA9: 86 29           STX     $29                 ; {hard.workRam+29}
ACAB: A5 2A           LDA     $2A                 ; {hard.workRam+2A}
ACAD: BE 1F 05        LDX     $051F,Y             ; {hard.workRam+51F}
ACB0: 99 1F 05        STA     $051F,Y             ; {hard.workRam+51F}
ACB3: 86 2A           STX     $2A                 ; {hard.workRam+2A}
ACB5: A5 2B           LDA     $2B                 ; {hard.workRam+2B}
ACB7: BE 20 05        LDX     $0520,Y             ; {hard.workRam+520}
ACBA: 99 20 05        STA     $0520,Y             ; {hard.workRam+520}
ACBD: 86 2B           STX     $2B                 ; {hard.workRam+2B}

loc_acbf:
ACBF: A5 2D           LDA     $2D                 ; {hard.workRam+2D}
ACC1: BE 1F 06        LDX     $061F,Y             ; {hard.workRam+61F}
ACC4: 99 1F 06        STA     $061F,Y             ; {hard.workRam+61F} swap this row's key with the running key
ACC7: 86 2D           STX     $2D                 ; {hard.workRam+2D}
ACC9: A5 2C           LDA     $2C                 ; {hard.workRam+2C}
ACCB: BE 20 06        LDX     $0620,Y             ; {hard.workRam+620}
ACCE: 99 20 06        STA     $0620,Y             ; {hard.workRam+620}
ACD1: 86 2C           STX     $2C                 ; {hard.workRam+2C}
ACD3: C0 52           CPY     #$52                
ACD5: 90 0A           BCC     $ACE1               ; {code.loc_ace1}
ACD7: A5 2E           LDA     $2E                 ; {hard.workRam+2E}
ACD9: BE 1E 06        LDX     $061E,Y             ; {hard.workRam+61E}
ACDC: 99 1E 06        STA     $061E,Y             ; {hard.workRam+61E} swap the key's low byte too
ACDF: 86 2E           STX     $2E                 ; {hard.workRam+2E}

loc_ace1:
ACE1: C0 55           CPY     #$55                
ACE3: 90 01           BCC     $ACE6               ; {code.loc_ace6}
ACE5: 88              DEY                         

loc_ace6:
ACE6: 88              DEY                         
ACE7: 88              DEY                         
ACE8: D0 B3           BNE     $AC9D               ; {code.loc_ac9d} keep bubbling the swap down the table
ACEA: A0 02           LDY     #$02                

loc_acec:
ACEC: EE 05 06        INC     $0605               ; {hard.workRam+605} count a settle pass
ACEF: C0 55           CPY     #$55                
ACF1: 90 01           BCC     $ACF4               ; {code.loc_acf4}
ACF3: 88              DEY                         

loc_acf4:
ACF4: 88              DEY                         
ACF5: 88              DEY                         
ACF6: D0 88           BNE     $AC80               ; {code.loc_ac80} advance to the next row pair
ACF8: A6 36           LDX     $36                 ; {hard.workRam+36}
ACFA: AD 05 06        LDA     $0605               ; {hard.workRam+605}
ACFD: 9D 00 06        STA     $0600,X             ; {hard.workRam+600} record this channel's pass count
AD00: CA              DEX                         
AD01: 30 03           BMI     $AD06               ; {code.loc_ad06} both channels done -- exit the sort loop

; ---- $AD03-$AD05: data ----
AD03: 4C 5E AC

loc_ad06:
AD06: AD 01 06        LDA     $0601               ; {hard.workRam+601}
AD09: CD 00 06        CMP     $0600               ; {hard.workRam+600}
AD0C: 90 07           BCC     $AD15               ; {code.loc_ad15}
AD0E: C9 63           CMP     #$63                
AD10: B0 03           BCS     $AD15               ; {code.loc_ad15}
AD12: EE 01 06        INC     $0601               ; {hard.workRam+601} nudge the running total up by one

loc_ad15:
AD15: A5 3D           LDA     $3D                 ; {hard.workRam+3D}
AD17: 49 01           EOR     #$01                
AD19: 0A              ASL     A                   
AD1A: 0A              ASL     A                   
AD1B: 05 3D           ORA     $3D                 ; {hard.workRam+3D}
AD1D: 69 05           ADC     #$05                
AD1F: 8D 03 06        STA     $0603               ; {hard.workRam+603} pack the sound-request byte and store it

; walk the packed request word loc_603 two bits at a time: on an empty
; word write idle status loc_0=0x14 and return; else take the low two bits
; as slot index loc_3d, consume them, read loc_600+index, skip slots whose
; byte is 0 or >=9, and for a live slot form loc_602 = ((3*byte) ^ 0xff) -
; 0xe5, call selectProjectionScale, seed
; loc_605=0x60/loc_4e=0/loc_50=0/loc_604=2, run the per-slot reset
; resetPerSlotStateTable, write armed status loc_0=0x24 and return.
armRequestedSoundSlot:
AD22: A0 14           LDY     #$14                
AD24: AD 03 06        LDA     $0603               ; {hard.workRam+603}
AD27: F0 42           BEQ     $AD6B               ; {code.loc_ad6b} no pending sound request -- drop to idle
AD29: 29 03           AND     #$03                
AD2B: 85 3D           STA     $3D                 ; {hard.workRam+3D} take the low two bits as the slot index
AD2D: C6 3D           DEC     $3D                 ; {hard.workRam+3D}
AD2F: 4E 03 06        LSR     $0603               ; {hard.workRam+603} consume those two bits from the request word
AD32: 4E 03 06        LSR     $0603               ; {hard.workRam+603}
AD35: A6 3D           LDX     $3D                 ; {hard.workRam+3D}
AD37: BD 00 06        LDA     $0600,X             ; {hard.workRam+600} read this slot's metric
AD3A: F0 2C           BEQ     $AD68               ; {code.loc_ad68} skip empty or out-of-range slots
AD3C: C9 09           CMP     #$09                
AD3E: B0 28           BCS     $AD68               ; {code.loc_ad68}
AD40: 0A              ASL     A                   
AD41: 18              CLC                         
AD42: 7D 00 06        ADC     $0600,X             ; {hard.workRam+600}
AD45: 49 FF           EOR     #$FF                
AD47: 38              SEC                         
AD48: E9 E5           SBC     #$E5                
AD4A: 8D 02 06        STA     $0602               ; {hard.workRam+602} form the slot's control value (scale by three, invert, offset)
AD4D: 20 48 CA        JSR     $CA48               ; {code.selectProjectionScale} select the projection scale
AD50: A9 60           LDA     #$60                
AD52: 8D 05 06        STA     $0605               ; {hard.workRam+605} seed the slow pass counter
AD55: A9 00           LDA     #$00                
AD57: 85 4E           STA     $4E                 ; {hard.workRam+4E} clear the input-edge flags
AD59: 85 50           STA     $50                 ; {hard.workRam+50} clear the spinner accumulator
AD5B: A9 02           LDA     #$02                
AD5D: 8D 04 06        STA     $0604               ; {hard.workRam+604} seed the re-arm counter
AD60: 20 89 A7        JSR     $A789               ; {code.resetPerSlotStateTable} reset the per-slot state table
AD63: A0 24           LDY     #$24                
AD65: 84 00           STY     $00                 ; {hard.workRam} set the sound state to armed
AD67: 60              RTS                         

loc_ad68:
AD68: 4C 22 AD        JMP     $AD22               ; {code.armRequestedSoundSlot} walk on to the next requested slot

loc_ad6b:
AD6B: 84 00           STY     $00                 ; {hard.workRam} set the sound state to idle
AD6D: 60              RTS                         

; per-frame tick of the active slot: set loc_1=0x06; while the low 5 bits
; of loc_3 are clear run countdown loc_605 down and on zero write
; loc_00=0x14 and return; otherwise clamp the active slot value
; loc_606,slot via foldStepIntoFraction (negative->0x1a, >=0x1b->0), gate
; on bits 3-4 of loc_4e (clearing them plus bit7), and when gated step
; cursor loc_602 and counter loc_604 -- on underflow re-arm
; (requestWriteLowRegions when loc_600,loc_3d < 4, then
; armRequestedSoundSlot), else clear the retired slot loc_606,slot-1.
tickActiveSoundSlot:
AD6E: A9 06           LDA     #$06                
AD70: 85 01           STA     $01                 ; {hard.workRam+1} select this mode's dispatch code
AD72: A5 03           LDA     $03                 ; {hard.workRam+3}
AD74: 29 1F           AND     #$1F                
AD76: D0 0A           BNE     $AD82               ; {code.loc_ad82} run the slow tick only every 32nd frame
AD78: CE 05 06        DEC     $0605               ; {hard.workRam+605} count down the slow pass counter
AD7B: D0 05           BNE     $AD82               ; {code.loc_ad82}
AD7D: A0 14           LDY     #$14                
AD7F: 84 00           STY     $00                 ; {hard.workRam} pass counter expired -- leave this mode
AD81: 60              RTS                         

loc_ad82:
AD82: AE 02 06        LDX     $0602               ; {hard.workRam+602}
AD85: BD 06 06        LDA     $0606,X             ; {hard.workRam+606} load the active slot's ramp value
AD88: 20 CE AD        JSR     $ADCE               ; {code.foldStepIntoFraction} fold the spinner step into the value
AD8B: A8              TAY                         
AD8C: 10 05           BPL     $AD93               ; {code.loc_ad93}
AD8E: A9 1A           LDA     #$1A                ; rail a negative value to 0x1a
AD90: B8              CLV                         
AD91: 50 06           BVC     $AD99               ; {code.loc_ad99}

loc_ad93:
AD93: C9 1B           CMP     #$1B                
AD95: 90 02           BCC     $AD99               ; {code.loc_ad99}
AD97: A9 00           LDA     #$00                ; rail an over-range value to 0x00

loc_ad99:
AD99: AE 02 06        LDX     $0602               ; {hard.workRam+602}
AD9C: 9D 06 06        STA     $0606,X             ; {hard.workRam+606} store the clamped ramp value back
AD9F: A5 4E           LDA     $4E                 ; {hard.workRam+4E}
ADA1: 29 18           AND     #$18                ; read the input-edge gate (bits 3-4)
ADA3: A8              TAY                         
ADA4: A5 4E           LDA     $4E                 ; {hard.workRam+4E}
ADA6: 29 67           AND     #$67                
ADA8: 85 4E           STA     $4E                 ; {hard.workRam+4E} consume the edge bits
ADAA: 98              TYA                         
ADAB: F0 20           BEQ     $ADCD               ; {code.loc_adcd} no edge -- done
ADAD: CE 02 06        DEC     $0602               ; {hard.workRam+602} step the slot cursor down
ADB0: CE 04 06        DEC     $0604               ; {hard.workRam+604} count down the re-arm counter
ADB3: 10 12           BPL     $ADC7               ; {code.loc_adc7}
ADB5: A6 3D           LDX     $3D                 ; {hard.workRam+3D}
ADB7: BD 00 06        LDA     $0600,X             ; {hard.workRam+600}
ADBA: C9 04           CMP     #$04                ; metric gate for the low-region write
ADBC: B0 03           BCS     $ADC1               ; {code.loc_adc1}
ADBE: 20 F7 DD        JSR     $DDF7               ; {code.requestWriteLowRegions} request the low-region write for a low-metric slot

loc_adc1:
ADC1: 20 22 AD        JSR     $AD22               ; {code.armRequestedSoundSlot} arm the next requested slot
ADC4: B8              CLV                         
ADC5: 50 06           BVC     $ADCD               ; {code.loc_adcd}

loc_adc7:
ADC7: CA              DEX                         
ADC8: A9 00           LDA     #$00                
ADCA: 9D 06 06        STA     $0606,X             ; {hard.workRam+606} silence the slot just retired

loc_adcd:
ADCD: 60              RTS                         

; fold the signed sub-step loc_50 (times 8) into the fraction cell loc_51,
; add the fold carry plus loc_50's sign-extension into A, and clear
; loc_50; returns the updated whole byte in A.
foldStepIntoFraction:
ADCE: 48              PHA                         
ADCF: A5 50           LDA     $50                 ; {hard.workRam+50} read the signed spinner sub-step
ADD1: 0A              ASL     A                   ; scale the sub-step by eight
ADD2: 0A              ASL     A                   
ADD3: 0A              ASL     A                   
ADD4: 18              CLC                         
ADD5: 65 51           ADC     $51                 ; {hard.workRam+51}
ADD7: 85 51           STA     $51                 ; {hard.workRam+51} fold it into the fine rotation fraction
ADD9: 68              PLA                         
ADDA: A4 50           LDY     $50                 ; {hard.workRam+50} check the sub-step's sign
ADDC: 30 05           BMI     $ADE3               ; {code.loc_ade3}
ADDE: 69 00           ADC     #$00                ; positive step -- add only the fraction carry
ADE0: B8              CLV                         
ADE1: 50 02           BVC     $ADE5               ; {code.loc_ade5}

loc_ade3:
ADE3: 69 FF           ADC     #$FF                ; negative step -- carry one down from the whole byte

loc_ade5:
ADE5: A0 00           LDY     #$00                
ADE7: 84 50           STY     $50                 ; {hard.workRam+50} consume the spinner sub-step
ADE9: 60              RTS                         

; draw a fixed frame ($AB17/$AB14 chain), tick the countdown loc_16e down
; by one, then hand the score delta loc_602-loc_604 to the glyph-row
; builder drawHighlightedGlyphRowList.
drawScoreDeltaPanel:
ADEA: 20 B4 A8        JSR     $A8B4               ; {code.buildTextOverlayList} build the static text overlay
ADED: A9 C0           LDA     #$C0                
ADEF: A2 02           LDX     #$02                
ADF1: 20 17 AB        JSR     $AB17               ; {code.drawSlotShapeWithHeader} draw the framing shape
ADF4: CE 6E 01        DEC     $016E               ; {hard.workRam+16E} tick down the score-display countdown
ADF7: 20 97 AA        JSR     $AA97               ; {code.emitCountDigitRun} draw the countdown digits
ADFA: A2 0A           LDX     #$0A                
ADFC: 20 14 AB        JSR     $AB14               ; {code.drawSlotShapeRecord} draw a marker shape
ADFF: A9 A6           LDA     #$A6                
AE01: A2 0C           LDX     #$0C                
AE03: 20 17 AB        JSR     $AB17               ; {code.drawSlotShapeWithHeader} draw a label shape
AE06: A9 9C           LDA     #$9C                
AE08: A2 0E           LDX     #$0E                
AE0A: 20 17 AB        JSR     $AB17               ; {code.drawSlotShapeWithHeader} draw a label shape
AE0D: A2 2C           LDX     #$2C                
AE0F: 20 14 AB        JSR     $AB14               ; {code.drawSlotShapeRecord} draw a marker shape
AE12: AD 02 06        LDA     $0602               ; {hard.workRam+602}
AE15: 38              SEC                         
AE16: ED 04 06        SBC     $0604               ; {hard.workRam+604} form the highlighted-row selector (control value minus re-arm counter)
AE19: 4C 4E AE        JMP     $AE4E               ; {code.drawHighlightedGlyphRowList} draw the glyph rows, highlighting the selected one

; fold two POKEY random samples $60CA/$60DA into scratch loc_29 and stored
; nibble loc_11f, draw the counters via drawCounterPair, then draw the
; highlighted glyph-row list via drawHighlightedGlyphRowList(0xff).
seedRngAndDrawCounterPanel:
AE1C: 20 B4 A8        JSR     $A8B4               ; {code.buildTextOverlayList} build the static text overlay
AE1F: 78              SEI                         ; block interrupts around the paired random reads
AE20: AD CA 60        LDA     $60CA               ; {hard.pokey1+A} sample the first POKEY random register
AE23: AC CA 60        LDY     $60CA               ; {hard.pokey1+A}
AE26: 84 29           STY     $29                 ; {hard.workRam+29} seed the scratch random byte
AE28: 4A              LSR     A                   
AE29: 4A              LSR     A                   
AE2A: 4A              LSR     A                   
AE2B: 4A              LSR     A                   
AE2C: 45 29           EOR     $29                 ; {hard.workRam+29} fold its high nibble into the scratch byte
AE2E: 85 29           STA     $29                 ; {hard.workRam+29}
AE30: AD DA 60        LDA     $60DA               ; {hard.pokey2+A} sample the second POKEY random register
AE33: AC DA 60        LDY     $60DA               ; {hard.pokey2+A}
AE36: 58              CLI                         ; re-enable interrupts
AE37: 45 29           EOR     $29                 ; {hard.workRam+29}
AE39: 29 F0           AND     #$F0                
AE3B: 45 29           EOR     $29                 ; {hard.workRam+29}
AE3D: 85 29           STA     $29                 ; {hard.workRam+29} fold the second sample's high nibble in
AE3F: 98              TYA                         
AE40: 0A              ASL     A                   
AE41: 0A              ASL     A                   
AE42: 0A              ASL     A                   
AE43: 0A              ASL     A                   
AE44: 45 29           EOR     $29                 ; {hard.workRam+29}
AE46: 8D 1F 01        STA     $011F               ; {hard.workRam+11F} store the stirred random nibble
AE49: 20 26 AF        JSR     $AF26               ; {code.drawCounterPair} draw the counter pair
AE4C: A9 FF           LDA     #$FF                ; no row highlighted -- fall into the row list

; draw a descending run of glyph rows: prime the pen ($B0DD(0x01)), set
; column loc_2c=0x28 and row index loc_37=0x15, and each pass step loc_2c
; back 0x0a, position ($DF75), select tag 0x00 when the row loc_37 equals
; the argument loc_63 else 0x07 ($B0D1), draw the glyph body
; ($DFB1/$B56A/$AEF8), re-seat loc_56/loc_57/loc_58 from
; loc_706/loc_707/loc_708, and drop loc_37 by 3.
drawHighlightedGlyphRowList:
AE4E: 85 63           STA     $63                 ; {hard.workRam+63} remember which row to highlight
AE50: A2 10           LDX     #$10                
AE52: 20 14 AB        JSR     $AB14               ; {code.drawSlotShapeRecord} prime the pen with a fixed shape
AE55: A9 01           LDA     #$01                
AE57: 85 61           STA     $61                 ; {hard.workRam+61} set the row base position
AE59: 20 DD B0        JSR     $B0DD               ; {code.emitScaleWordIfChanged} set the drawing scale
AE5C: A9 28           LDA     #$28                
AE5E: 85 2C           STA     $2C                 ; {hard.workRam+2C} seed the column cursor
AE60: A2 15           LDX     #$15                
AE62: 86 37           STX     $37                 ; {hard.workRam+37} set the top row index (steps down by three)

loc_ae64:
AE64: 20 0D AB        JSR     $AB0D               ; {code.emitFixedVectorWord} emit a fixed vector word
AE67: A9 00           LDA     #$00                
AE69: 85 73           STA     $73                 ; {hard.workRam+73} clear the vector-record header
AE6B: A5 2C           LDA     $2C                 ; {hard.workRam+2C}
AE6D: AA              TAX                         
AE6E: 38              SEC                         
AE6F: E9 0A           SBC     #$0A                
AE71: 85 2C           STA     $2C                 ; {hard.workRam+2C} step the column cursor back one row
AE73: A9 D0           LDA     #$D0                
AE75: 20 75 DF        JSR     $DF75               ; {code.emitScaledCoordinateRecord} position this row
AE78: A0 07           LDY     #$07                
AE7A: A5 63           LDA     $63                 ; {hard.workRam+63}
AE7C: C5 37           CMP     $37                 ; {hard.workRam+37} pick the highlight tint when this is the selected row
AE7E: D0 02           BNE     $AE82               ; {code.loc_ae82}
AE80: A0 00           LDY     #$00                

loc_ae82:
AE82: 20 D1 B0        JSR     $B0D1               ; {code.emitColorStatIfChanged} set the row colour
AE85: A9 61           LDA     #$61                
AE87: A0 01           LDY     #$01                
AE89: 20 B1 DF        JSR     $DFB1               ; {code.emitNibbleDigitRun} emit a one-digit numeric run
AE8C: A9 A0           LDA     #$A0                
AE8E: 20 6A B5        JSR     $B56A               ; {code.emitBlankValueRecord} emit a blank value record
AE91: A9 00           LDA     #$00                
AE93: 85 73           STA     $73                 ; {hard.workRam+73}
AE95: AA              TAX                         
AE96: A9 08           LDA     #$08                
AE98: 20 75 DF        JSR     $DF75               ; {code.emitScaledCoordinateRecord} position the label
AE9B: E6 61           INC     $61                 ; {hard.workRam+61} advance down a row
AE9D: A5 37           LDA     $37                 ; {hard.workRam+37}
AE9F: 20 F8 AE        JSR     $AEF8               ; {code.drawThreeCharGlyphString} draw this row's three-character label
AEA2: A2 00           LDX     #$00                
AEA4: A9 08           LDA     #$08                
AEA6: 20 75 DF        JSR     $DF75               ; {code.emitScaledCoordinateRecord} position the numeric run
AEA9: A6 37           LDX     $37                 ; {hard.workRam+37}
AEAB: BD 06 07        LDA     $0706,X             ; {hard.workRam+706} seat the row's numeric triple from the per-row tables
AEAE: 85 56           STA     $56                 ; {hard.workRam+56}
AEB0: BD 07 07        LDA     $0707,X             ; {hard.workRam+707}
AEB3: 85 57           STA     $57                 ; {hard.workRam+57}
AEB5: BD 08 07        LDA     $0708,X             ; {hard.workRam+708}
AEB8: 85 58           STA     $58                 ; {hard.workRam+58}
AEBA: A9 56           LDA     #$56                
AEBC: A0 03           LDY     #$03                
AEBE: 20 B1 DF        JSR     $DFB1               ; {code.emitNibbleDigitRun} emit the three-value numeric run
AEC1: C6 37           DEC     $37                 ; {hard.workRam+37} step to the next row up (index minus three)
AEC3: C6 37           DEC     $37                 ; {hard.workRam+37}
AEC5: C6 37           DEC     $37                 ; {hard.workRam+37}
AEC7: 10 9B           BPL     $AE64               ; {code.loc_ae64} loop until the row index wraps below zero

; ---- $AEC9-$AEC9: data ----
AEC9: 60

; publish the object-list gate checksum and optionally draw a flag record:
; when loc_156 is nonzero seat it into loc_58, open a record
; (drawSlotShapeRecord 0x34) and emit a cleared coordinate pair
; (loc_56=loc_57=0x00, emitNibbleDigitRun); always fold the seventeen
; bytes at $D575 (indices 0x10..0) into an accumulator seeded 0x85 with
; carry and store the result to loc_b5 (the end-of-list gate
; buildObjectDisplayList reads).
computeDisplayListChecksum:
AECA: AD 56 01        LDA     $0156               ; {hard.workRam+156} read the bonus-life interval -- skip the marker when zero
AECD: F0 14           BEQ     $AEE3               ; {code.loc_aee3}
AECF: 85 58           STA     $58                 ; {hard.workRam+58} seat the interval into the flag record
AED1: A2 34           LDX     #$34                
AED3: 20 14 AB        JSR     $AB14               ; {code.drawSlotShapeRecord} open the bonus-life flag shape
AED6: A9 00           LDA     #$00                
AED8: 85 56           STA     $56                 ; {hard.workRam+56} clear the flag's coordinate pair
AEDA: 85 57           STA     $57                 ; {hard.workRam+57}
AEDC: A9 56           LDA     #$56                
AEDE: A0 03           LDY     #$03                
AEE0: 20 B1 DF        JSR     $DFB1               ; {code.emitNibbleDigitRun} emit the flag's numeric run

loc_aee3:
AEE3: 18              CLC                         
AEE4: A0 10           LDY     #$10                
AEE6: A9 85           LDA     #$85                ; seed the checksum accumulator

loc_aee8:
AEE8: 79 75 D5        ADC     $D575,Y             ; {hard.rom+4575} fold the next source byte into the checksum
AEEB: 88              DEY                         
AEEC: 10 FA           BPL     $AEE8               ; {code.loc_aee8} fold all seventeen source bytes
AEEE: 85 B5           STA     $B5                 ; {hard.workRam+B5} publish the display-list checksum to the end-of-list gate
AEF0: 60              RTS                         

; ---- $AEF1-$AEF7: data ----
AEF1: AD 02 06 38 ED 04 06

; render three characters into the display list: walk three codes from the
; text buffer 0x606 (position at 0x38, count at 0x39), clamp each code to
; 0x1a (0x1e+ folds to 0x1a), double it to index glyph word table 0x31fa,
; copy each 2-byte glyph word to the cursor 0x74, then advance the cursor
; past everything written.
drawThreeCharGlyphString:
AEF8: 18              CLC                         
AEF9: 69 02           ADC     #$02                
AEFB: 85 38           STA     $38                 ; {hard.workRam+38} point at the last of the three character codes
AEFD: A0 00           LDY     #$00                
AEFF: A9 02           LDA     #$02                
AF01: 85 39           STA     $39                 ; {hard.workRam+39} set the three-character pass count

loc_af03:
AF03: A6 38           LDX     $38                 ; {hard.workRam+38}
AF05: BD 06 06        LDA     $0606,X             ; {hard.workRam+606} read this character's code
AF08: C9 1E           CMP     #$1E                
AF0A: 90 02           BCC     $AF0E               ; {code.loc_af0e}
AF0C: A9 1A           LDA     #$1A                ; fold an out-of-range code to a blank

loc_af0e:
AF0E: 0A              ASL     A                   ; double the code into a glyph-table index
AF0F: AA              TAX                         
AF10: BD FA 31        LDA     $31FA,X             ; {hard.vectorRom+1FA} copy the glyph's low byte into the display list
AF13: 91 74           STA     ($74),Y             ; {hard.workRam+74}
AF15: C8              INY                         
AF16: BD FB 31        LDA     $31FB,X             ; {hard.vectorRom+1FB} copy the glyph's high byte
AF19: 91 74           STA     ($74),Y             ; {hard.workRam+74}
AF1B: C8              INY                         
AF1C: C6 38           DEC     $38                 ; {hard.workRam+38} step back to the previous character
AF1E: C6 39           DEC     $39                 ; {hard.workRam+39}
AF20: 10 E1           BPL     $AF03               ; {code.loc_af03}
AF22: 88              DEY                         
AF23: 4C 5F DF        JMP     $DF5F               ; {code.advanceDisplayCursor} advance the display cursor past the string

; when either counter byte loc_600/loc_601 is nonzero, draw a shared
; header ($AB14(0x12), emitCappedCount(0x63)) and both counter slots via
; drawCounterSlot(0x00) and drawCounterSlot(0x01); otherwise return
; through the bare tail $AF6E.
drawCounterPair:
AF26: AD 00 06        LDA     $0600               ; {hard.workRam+600} read the first counter byte of the paired readout panel
AF29: 0D 01 06        ORA     $0601               ; {hard.workRam+601} or in the second counter byte -- panel is empty only if both are zero
AF2C: F0 40           BEQ     $AF6E               ; {code.sharedReturnTail} both counters zero: draw nothing, return through the shared tail
AF2E: A2 12           LDX     #$12                ; select the shared header shape record
AF30: 20 14 AB        JSR     $AB14               ; {code.drawSlotShapeRecord} emit the panel header shape record
AF33: A9 63           LDA     #$63                ; header count value -- 99
AF35: 20 71 AF        JSR     $AF71               ; {code.emitCappedCount} emit the header count, clamped to 99
AF38: A2 00           LDX     #$00                ; slot 0
AF3A: 20 3F AF        JSR     $AF3F               ; {code.drawCounterSlot} draw counter slot 0
AF3D: A2 01           LDX     #$01                ; slot 1: fall through into the per-slot worker

; draw one counter slot x: return when count loc_600+x is zero, else
; record the slot in loc_2e, position it at $AF6F+loc_2e ($DF75), and emit
; the capped count (emitCappedCount, $B56A, $AB98, $AA9E).
drawCounterSlot:
AF3F: BD 00 06        LDA     $0600,X             ; {hard.workRam+600} read this slot's counter byte from the counter array
AF42: F0 2A           BEQ     $AF6E               ; {code.sharedReturnTail} empty slot: draw nothing
AF44: 48              PHA                         
AF45: 86 2E           STX     $2E                 ; {hard.workRam+2E} stash the slot index in scratch
AF47: A0 03           LDY     #$03                ; colour/intensity attribute for the slot
AF49: 20 D1 B0        JSR     $B0D1               ; {code.emitColorStatIfChanged} emit the colour stat only if it changed
AF4C: 20 0D AB        JSR     $AB0D               ; {code.emitFixedVectorWord} emit a fixed vector word
AF4F: A9 D0           LDA     #$D0                ; coordinate scale for the count glyph
AF51: A4 2E           LDY     $2E                 ; {hard.workRam+2E} reload the slot index
AF53: BE 6F AF        LDX     $AF6F,Y             ; {hard.rom+1F6F} read this slot's Y position from the glyph-coordinate table
AF56: 20 75 DF        JSR     $DF75               ; {code.emitScaledCoordinateRecord} emit the scaled coordinate record
AF59: 68              PLA                         
AF5A: 20 71 AF        JSR     $AF71               ; {code.emitCappedCount} emit the count itself, clamped to 99
AF5D: A9 A0           LDA     #$A0                ; blank spacer value
AF5F: 20 6A B5        JSR     $B56A               ; {code.emitBlankValueRecord} emit a blank value spacer record
AF62: A9 10           LDA     #$10                
AF64: A2 04           LDX     #$04                
AF66: 20 98 AB        JSR     $AB98               ; {code.drawShapeListAtPosition} draw the small count shape list at position
AF69: A6 2E           LDX     $2E                 ; {hard.workRam+2E} reload the slot index
AF6B: 20 9E AA        JSR     $AA9E               ; {code.emitSlotIndexDigit} emit the trailing slot-index digit

; no-op leaf: return immediately; the shared RTS tail that drawCounterPair
; falls through to when both counters loc_600/loc_601 are zero.
sharedReturnTail:
AF6E: 60              RTS                         

; ---- $AF6F-$AF70: data ----
AF6F: C0 B0

; clamp the incoming byte to a max of 0x63 (99), then pack-and-emit it via
; $AF77.
emitCappedCount:
AF71: C9 63           CMP     #$63                ; compare the count against the 99 ceiling
AF73: 90 02           BCC     $AF77               ; {code.emitByteAsBcdDigits} already under the ceiling: emit as is
AF75: A9 63           LDA     #$63                ; clamp the count to 99

; Packs the incoming byte to BCD (into loc_29) then emits that single
; zeropage byte as its two decimal nibbles.
emitByteAsBcdDigits:
AF77: 20 F5 AA        JSR     $AAF5               ; {code.packBinaryToBcd} pack the binary value to packed BCD in the scratch cell
AF7A: A9 29           LDA     #$29                ; point at the packed-BCD scratch byte
AF7C: A0 01           LDY     #$01                ; one byte to walk
AF7E: 4C B1 DF        JMP     $DFB1               ; {code.emitNibbleDigitRun} emit that byte's two nibbles as decimal digit glyphs

; draw the whole playfield well: refresh gates (selectProjectionScale),
; tick loc_16e, draw the eight rim segments walking loc_37 7->0
; (drawSlotShapeRecord($B09B+loc_37)), nudge the depth window pair
; loc_7b/loc_7c one step toward target loc_200 (bounded by ceiling
; loc_127), draw five depth rows deepest-first from $91FE+loc_3a (skipping
; rows >=0x63; emitTableValueDigitRun/drawTubeShapeOutline), and close
; with a framing draw and a four-entry trailer walk over $B0A3.
drawTubeWell:
AF81: 20 48 CA        JSR     $CA48               ; {code.selectProjectionScale} refresh the projection/scale gates for this frame
AF84: CE 6E 01        DEC     $016E               ; {hard.workRam+16E} tick the score-display timer down
AF87: A0 03           LDY     #$03                ; colour attribute for the tube preamble
AF89: 20 D1 B0        JSR     $B0D1               ; {code.emitColorStatIfChanged} open the draw stream with a colour stat if it changed
AF8C: A9 01           LDA     #$01                
AF8E: 85 72           STA     $72                 ; {hard.workRam+72} prime the last-scale latch
AF90: 20 6A DF        JSR     $DF6A               ; {code.emitBlankVectorWordTag70} emit a blank vector word
AF93: A2 2C           LDX     #$2C                
AF95: A9 60           LDA     #$60                
AF97: 20 17 AB        JSR     $AB17               ; {code.drawSlotShapeWithHeader} draw the header slot shape record
AF9A: 20 92 AA        JSR     $AA92               ; {code.drawSlotThenDigitRun} draw the preamble slot then its digit run
AF9D: A2 07           LDX     #$07                ; rim ring: start at the top segment index 7
AF9F: 86 37           STX     $37                 ; {hard.workRam+37} seed the rim loop counter

loc_afa1:
AFA1: A4 37           LDY     $37                 ; {hard.workRam+37} current rim segment index
AFA3: BE 9B B0        LDX     $B09B,Y             ; {hard.rom+209B} read this rim segment's shape arg from the table
AFA6: 20 14 AB        JSR     $AB14               ; {code.drawSlotShapeRecord} draw this rim segment shape record
AFA9: C6 37           DEC     $37                 ; {hard.workRam+37} next rim segment
AFAB: 10 F4           BPL     $AFA1               ; {code.loc_afa1} loop through rim segments 7 down to 0
AFAD: AD 00 02        LDA     $0200               ; {hard.workRam+200} read the blaster's rim target position
AFB0: 38              SEC                         
AFB1: E5 7B           SBC     $7B                 ; {hard.workRam+7B} signed distance from the depth window to the target
AFB3: 10 07           BPL     $AFBC               ; {code.loc_afbc} target at or above the window: handle the non-negative case
AFB5: C6 7B           DEC     $7B                 ; {hard.workRam+7B} target below the window: step the depth-window pair down
AFB7: C6 7C           DEC     $7C                 ; {hard.workRam+7C} step the window's second byte down as well
AFB9: B8              CLV                         
AFBA: 50 25           BVC     $AFE1               ; {code.loc_afe1}

loc_afbc:
AFBC: D0 0D           BNE     $AFCB               ; {code.loc_afcb} nonzero distance: window still chasing the target
AFBE: C6 7C           DEC     $7C                 ; {hard.workRam+7C} on target: pull the window in by one
AFC0: C6 7B           DEC     $7B                 ; {hard.workRam+7B} pull the window's other byte in as well
AFC2: 10 04           BPL     $AFC8               ; {code.loc_afc8} skip the undo unless the step underflowed
AFC4: E6 7B           INC     $7B                 ; {hard.workRam+7B} undo the pull-in if it dropped below zero
AFC6: E6 7C           INC     $7C                 ; {hard.workRam+7C} restore the window's second byte

loc_afc8:
AFC8: B8              CLV                         
AFC9: 50 16           BVC     $AFE1               ; {code.loc_afe1}

loc_afcb:
AFCB: A5 7C           LDA     $7C                 ; {hard.workRam+7C} load the window far byte
AFCD: CD 27 01        CMP     $0127               ; {hard.workRam+127} compare it against the depth ceiling
AFD0: F0 02           BEQ     $AFD4               ; {code.loc_afd4}
AFD2: B0 0D           BCS     $AFE1               ; {code.loc_afe1} past the ceiling: settle without stepping closer

loc_afd4:
AFD4: 38              SEC                         
AFD5: ED 00 02        SBC     $0200               ; {hard.workRam+200} distance past the target position
AFD8: D0 01           BNE     $AFDB               ; {code.loc_afdb}
AFDA: 18              CLC                         

loc_afdb:
AFDB: B0 04           BCS     $AFE1               ; {code.loc_afe1} at or beyond the target: settle
AFDD: E6 7B           INC     $7B                 ; {hard.workRam+7B} step the window one closer to the target
AFDF: E6 7C           INC     $7C                 ; {hard.workRam+7C} step the window's second byte closer as well

loc_afe1:
AFE1: A5 7C           LDA     $7C                 ; {hard.workRam+7C} seed the depth cursor from the window far byte
AFE3: 85 3A           STA     $3A                 ; {hard.workRam+3A} store the depth-row cursor
AFE5: A2 04           LDX     #$04                ; five depth rings, deepest first: index 4
AFE7: 86 37           STX     $37                 ; {hard.workRam+37}

loc_afe9:
AFE9: A0 05           LDY     #$05                ; colour stat for this depth ring
AFEB: 20 D1 B0        JSR     $B0D1               ; {code.emitColorStatIfChanged}
AFEE: A9 00           LDA     #$00                
AFF0: 85 73           STA     $73                 ; {hard.workRam+73} clear the record header byte
AFF2: 20 0D AB        JSR     $AB0D               ; {code.emitFixedVectorWord} emit a fixed vector word
AFF5: A2 D8           LDX     #$D8                ; coordinate scale for the ring
AFF7: A4 37           LDY     $37                 ; {hard.workRam+37}
AFF9: B9 96 B0        LDA     $B096,Y             ; {hard.rom+2096} read this ring's tube-well segment coordinate from the table
AFFC: 18              CLC                         
AFFD: 69 F8           ADC     #$F8                ; offset the coordinate back for the ring position
AFFF: 20 75 DF        JSR     $DF75               ; {code.emitScaledCoordinateRecord} emit the ring's scaled coordinate record
B002: A6 3A           LDX     $3A                 ; {hard.workRam+3A}
B004: BC FE 91        LDY     $91FE,X             ; {hard.rom+1FE} read this ring's depth threshold from the table
B007: C0 63           CPY     #$63                ; compare the threshold against the far edge -- 99
B009: B0 37           BCS     $B042               ; {code.loc_b042} ring already at the far edge: skip its label body
B00B: C8              INY                         ; depth label value: threshold plus one
B00C: 98              TYA                         
B00D: 20 77 AF        JSR     $AF77               ; {code.emitByteAsBcdDigits} draw the depth label as two decimal digits
B010: A0 03           LDY     #$03                ; colour attribute for the label
B012: 20 D1 B0        JSR     $B0D1               ; {code.emitColorStatIfChanged} emit the colour stat if changed
B015: 20 0D AB        JSR     $AB0D               ; {code.emitFixedVectorWord} emit a fixed vector word
B018: A2 BA           LDX     #$BA                ; label scale
B01A: A4 37           LDY     $37                 ; {hard.workRam+37}
B01C: B9 96 B0        LDA     $B096,Y             ; {hard.rom+2096} this ring's segment coordinate
B01F: 18              CLC                         
B020: 69 EC           ADC     #$EC                ; offset the coordinate for the label position
B022: 20 75 DF        JSR     $DF75               ; {code.emitScaledCoordinateRecord} emit the label's scaled coordinate record
B025: A6 3A           LDX     $3A                 ; {hard.workRam+3A} emit the depth row's table-value digit run
B027: 20 C6 B0        JSR     $B0C6               ; {code.emitTableValueDigitRun}
B02A: 20 0D AB        JSR     $AB0D               ; {code.emitFixedVectorWord} emit a fixed vector word
B02D: A2 CC           LDX     #$CC                ; outline scale
B02F: A4 37           LDY     $37                 ; {hard.workRam+37}
B031: B9 96 B0        LDA     $B096,Y             ; {hard.rom+2096} this ring's segment coordinate for the outline
B034: 18              CLC                         
B035: 69 00           ADC     #$00                
B037: 20 75 DF        JSR     $DF75               ; {code.emitScaledCoordinateRecord} emit the outline's scaled coordinate record
B03A: A6 3A           LDX     $3A                 ; {hard.workRam+3A}
B03C: BD FE 91        LDA     $91FE,X             ; {hard.rom+1FE} this ring's depth threshold
B03F: 20 E1 C4        JSR     $C4E1               ; {code.drawTubeShapeOutline} draw the tube ring outline

loc_b042:
B042: C6 3A           DEC     $3A                 ; {hard.workRam+3A} recede one ring deeper
B044: C6 37           DEC     $37                 ; {hard.workRam+37} next ring
B046: 10 A1           BPL     $AFE9               ; {code.loc_afe9} loop through the five depth rings
B048: A9 00           LDA     #$00                
B04A: 85 73           STA     $73                 ; {hard.workRam+73} clear the record header for the trailer
B04C: 20 0D AB        JSR     $AB0D               ; {code.emitFixedVectorWord} emit a fixed vector word
B04F: A2 1C           LDX     #$1C                ; draw the framing slot shape record
B051: 20 14 AB        JSR     $AB14               ; {code.drawSlotShapeRecord}
B054: A9 04           LDA     #$04                
B056: A0 01           LDY     #$01                
B058: 20 B1 DF        JSR     $DFB1               ; {code.emitNibbleDigitRun} emit a short nibble digit run
B05B: A0 00           LDY     #$00                ; colour attribute for the blaster
B05D: 20 D1 B0        JSR     $B0D1               ; {code.emitColorStatIfChanged} emit the colour stat if changed
B060: 20 0D AB        JSR     $AB0D               ; {code.emitFixedVectorWord} emit a fixed vector word
B063: A2 B8           LDX     #$B8                
B065: 20 AB B0        JSR     $B0AB               ; {code.nudgeBlasterRimPosition} advance the blaster rim position and clamp it into the tube
B068: 38              SEC                         
B069: E5 7B           SBC     $7B                 ; {hard.workRam+7B} index the well coordinate relative to the depth window
B06B: A8              TAY                         
B06C: B9 96 B0        LDA     $B096,Y             ; {hard.rom+2096} read the well segment coordinate for the blaster position
B06F: 38              SEC                         
B070: E9 16           SBC     #$16                ; offset the blaster coordinate
B072: 20 75 DF        JSR     $DF75               ; {code.emitScaledCoordinateRecord} emit the blaster-relative coordinate record
B075: A9 E0           LDA     #$E0                
B077: 85 73           STA     $73                 ; {hard.workRam+73} closing frame uses the $e0 record header
B079: A2 00           LDX     #$00                
B07B: 86 38           STX     $38                 ; {hard.workRam+38} vertex table cursor: start at 0
B07D: A0 03           LDY     #$03                
B07F: 84 37           STY     $37                 ; {hard.workRam+37} four closing frame vertices

loc_b081:
B081: A4 38           LDY     $38                 ; {hard.workRam+38} current vertex table index
B083: B9 A3 B0        LDA     $B0A3,Y             ; {hard.rom+20A3} read the vertex x byte from the table
B086: AA              TAX                         
B087: C8              INY                         
B088: B9 A3 B0        LDA     $B0A3,Y             ; {hard.rom+20A3} read the paired vertex a byte
B08B: C8              INY                         
B08C: 84 38           STY     $38                 ; {hard.workRam+38} step to the next vertex pair
B08E: 20 75 DF        JSR     $DF75               ; {code.emitScaledCoordinateRecord} emit the closing frame vertex coordinate
B091: C6 37           DEC     $37                 ; {hard.workRam+37} next vertex
B093: 10 EC           BPL     $B081               ; {code.loc_b081} loop through the four closing vertices
B095: 60              RTS                         

; ---- $B096-$B0AA: data ----
B096: BE E3 09 30 58 14 0C 0E 16 18 1E 20 1A 00 26 28
B0A6: 00 00 DA D8 00

; nudge the blaster's rim position loc_200 by its signed sub-step (via
; foldStepIntoFraction), clamp into [0, ceiling loc_127] (a negative
; result floors to 0, an over-ceiling result pins to loc_127), write it
; back to loc_200, and return it in both A and Y.
nudgeBlasterRimPosition:
B0AB: AD 00 02        LDA     $0200               ; {hard.workRam+200} read the current blaster rim position
B0AE: 20 CE AD        JSR     $ADCE               ; {code.foldStepIntoFraction} fold the pending signed sub-step into the position
B0B1: A8              TAY                         
B0B2: 10 05           BPL     $B0B9               ; {code.loc_b0b9} negative result: stepped below the first lane?
B0B4: A9 00           LDA     #$00                ; floor to lane 0
B0B6: B8              CLV                         
B0B7: 50 08           BVC     $B0C1               ; {code.loc_b0c1}

loc_b0b9:
B0B9: CD 27 01        CMP     $0127               ; {hard.workRam+127} compare against the depth ceiling
B0BC: 90 03           BCC     $B0C1               ; {code.loc_b0c1} under the ceiling: keep the position
B0BE: AD 27 01        LDA     $0127               ; {hard.workRam+127} clamp to the ceiling

loc_b0c1:
B0C1: 8D 00 02        STA     $0200               ; {hard.workRam+200} write back the new rim position
B0C4: A8              TAY                         ; return it in Y as well
B0C5: 60              RTS                         

; Seats a table pointer by index (via $91B5) then emits the three-byte
; zeropage run at loc_29 as nibble digits.
emitTableValueDigitRun:
B0C6: 8A              TXA                         
B0C7: 20 B5 91        JSR     $91B5               ; {code.seatInPagePointer} seat the working pointer from the ROM pointer table at this index
B0CA: A9 29           LDA     #$29                ; point at the three-byte scratch run
B0CC: A0 03           LDY     #$03                ; three bytes to walk
B0CE: 4C B1 DF        JMP     $DFB1               ; {code.emitNibbleDigitRun} emit those three bytes as decimal digit glyphs

; emit a colour/intensity stat word (emitTaggedVectorWord with 0x08 and y)
; into the display list only when it changes: return if loc_9e already
; equals y, otherwise latch loc_9e=y and emit — the coarse (high-nibble)
; scale/colour attribute for the current slot.
emitColorStatIfChanged:
B0D1: C4 9E           CPY     $9E                 ; {hard.workRam+9E} compare the requested attribute against the latched colour value
B0D3: F0 07           BEQ     $B0DC               ; {code.loc_b0dc} unchanged: emit nothing
B0D5: 84 9E           STY     $9E                 ; {hard.workRam+9E} latch the new colour/intensity value
B0D7: A9 08           LDA     #$08                
B0D9: 4C 4C DF        JMP     $DF4C               ; {code.emitTaggedVectorWord} emit the tagged colour/intensity attribute word

loc_b0dc:
B0DC: 60              RTS                         

; emit a scale word (emitBlankVectorWordTag70 with a) into the display
; list only when it changes: return if a already equals loc_72, otherwise
; latch loc_72=a and emit — the fine (low-nibble) scale attribute for the
; current slot.
emitScaleWordIfChanged:
B0DD: C5 72           CMP     $72                 ; {hard.workRam+72} compare the requested scale against the last-emitted scale
B0DF: F0 05           BEQ     $B0E6               ; {code.loc_b0e6} unchanged: emit nothing
B0E1: 85 72           STA     $72                 ; {hard.workRam+72} latch the new scale value
B0E3: 4C 6A DF        JMP     $DF6A               ; {code.emitBlankVectorWordTag70} emit it as a tagged scale word

loc_b0e6:
B0E6: 60              RTS                         

; alternate state-entry seeder: write loc_0=0x0a, loc_2=0x00, loc_4=0xdf,
; loc_1=0x12, loc_14e=0x19 and loc_14d=0x18 into the config block plus the
; two bound cells.
seedModeParamsWithBounds:
B0E7: A9 0A           LDA     #$0A                ; set the game mode to live
B0E9: 85 00           STA     $00                 ; {hard.workRam} store the game mode
B0EB: A9 00           LDA     #$00                ; clear the pending mode
B0ED: 85 02           STA     $02                 ; {hard.workRam+2}
B0EF: A9 DF           LDA     #$DF                ; seed the mode-promotion countdown
B0F1: 85 04           STA     $04                 ; {hard.workRam+4}
B0F3: A9 12           LDA     #$12                
B0F5: 85 01           STA     $01                 ; {hard.workRam+1} set the display-mode selector -- pre-doubled table offset
B0F7: A9 19           LDA     #$19                ; far cursor of the animated span
B0F9: 8D 4E 01        STA     $014E               ; {hard.workRam+14E} store the far cursor
B0FC: A9 18           LDA     #$18                ; near cursor of the animated span
B0FE: 8D 4D 01        STA     $014D               ; {hard.workRam+14D} store the near cursor
B101: 60              RTS                         

; redraw the paired-cursor span via
; emitSegmentedSpanBetweenCursors(0x34,0xaa) then spread the two cursors
; apart one frame: wrap the far cursor loc_14e up by 0x14 while below
; 0xa0, and once it clears 0x50 step the near cursor loc_14d up by 0x08,
; pinning it at 0xa0 and latching phase byte loc_1=0x14 when near reaches
; far.
advanceSpreadingSpanAnimation:
B102: A9 34           LDA     #$34                ; coordinate byte handed to the span emitter -- reused at each step
B104: A2 AA           LDX     #$AA                ; second coordinate byte handed to the span emitter
B106: 20 5A B1        JSR     $B15A               ; {code.emitSegmentedSpanBetweenCursors} redraw the segmented span between the current cursors
B109: AD 4E 01        LDA     $014E               ; {hard.workRam+14E} load the far cursor
B10C: C9 A0           CMP     #$A0                
B10E: B0 05           BCS     $B115               ; {code.loc_b115} far cursor at the 0xa0 ceiling: stop growing it
B110: 69 14           ADC     #$14                ; step the far cursor up by 0x14
B112: 8D 4E 01        STA     $014E               ; {hard.workRam+14E} store the far cursor

loc_b115:
B115: C9 50           CMP     #$50                
B117: 90 17           BCC     $B130               ; {code.loc_b130} hold the near cursor until the far cursor clears 0x50
B119: AD 4D 01        LDA     $014D               ; {hard.workRam+14D}
B11C: 18              CLC                         
B11D: 69 08           ADC     #$08                ; step the near cursor up by 0x08
B11F: 8D 4D 01        STA     $014D               ; {hard.workRam+14D} store the near cursor
B122: CD 4E 01        CMP     $014E               ; {hard.workRam+14E} near cursor still trailing the far cursor?
B125: 90 09           BCC     $B130               ; {code.loc_b130} still trailing: keep spreading this frame
B127: A9 A0           LDA     #$A0                ; spread complete: pin the near cursor at the ceiling
B129: 8D 4D 01        STA     $014D               ; {hard.workRam+14D} store the pinned near cursor
B12C: A9 14           LDA     #$14                
B12E: 85 01           STA     $01                 ; {hard.workRam+1} latch the display-mode selector to advance to the next state

loc_b130:
B130: 60              RTS                         

; redraw the paired-cursor span via
; emitSegmentedSpanBetweenCursors(0x3f,0x4e) then squeeze the two cursors
; together one frame: decrement the near cursor loc_14d while at/above
; 0x30 (bail if it wraps to >=0x80) and pull the far cursor loc_14e down
; by one but never below the near cursor.
advancePinchingSpanAnimation:
B131: A9 3F           LDA     #$3F                ; coordinate byte handed to the span emitter -- reused at each step
B133: A2 4E           LDX     #$4E                ; second coordinate byte handed to the span emitter
B135: 20 5A B1        JSR     $B15A               ; {code.emitSegmentedSpanBetweenCursors} redraw the segmented span between the current cursors
B138: AD 4D 01        LDA     $014D               ; {hard.workRam+14D} load the near cursor
B13B: C9 30           CMP     #$30                
B13D: 90 05           BCC     $B144               ; {code.loc_b144} near cursor below the 0x30 floor: hold it in place
B13F: E9 01           SBC     #$01                ; step the near cursor down by one
B141: 8D 4D 01        STA     $014D               ; {hard.workRam+14D} store the near cursor

loc_b144:
B144: C9 80           CMP     #$80                
B146: B0 11           BCS     $B159               ; {code.loc_b159} underflowed past zero: pinch done, leave the far cursor
B148: AD 4E 01        LDA     $014E               ; {hard.workRam+14E} load the far cursor
B14B: 38              SEC                         
B14C: E9 01           SBC     #$01                ; step the far cursor down by one
B14E: CD 4D 01        CMP     $014D               ; {hard.workRam+14D} compare the far cursor against the near cursor
B151: B0 03           BCS     $B156               ; {code.loc_b156} far cursor still above the near cursor: keep it
B153: AD 4D 01        LDA     $014D               ; {hard.workRam+14D} clamp the far cursor at the near cursor so the pair meets

loc_b156:
B156: 8D 4E 01        STA     $014E               ; {hard.workRam+14E} store the far cursor

loc_b159:
B159: 60              RTS                         

; emit a segmented vector run spanning the near-to-far cursor pair: stash
; A/X into loc_57/loc_56, seed loc_37 from the near cursor loc_14d,
; decrement loc_16e, and for each step (cursor +=2 until it reaches the
; far cursor loc_14e) lay a header word (emitVectorWordTag70), a position-
; derived marker (emitTaggedVectorWord 0x68 with segment (cur>>3)&7, 7->3,
; 0 at the start) and the stashed coordinate pair
; (emitCoordinateVectorWord), then two fixed trailer words
; (drawSlotShapeWithHeader 0xd0,0x2c and emitCoordinateVectorWord
; 0x3f,0xf2).
emitSegmentedSpanBetweenCursors:
B15A: 85 57           STA     $57                 ; {hard.workRam+57} stash the coordinate pair's first byte
B15C: 86 56           STX     $56                 ; {hard.workRam+56} stash the coordinate pair's second byte
B15E: AD 4D 01        LDA     $014D               ; {hard.workRam+14D} seed the walking cursor at the near bound
B161: 85 37           STA     $37                 ; {hard.workRam+37} store the walking cursor
B163: CE 6E 01        DEC     $016E               ; {hard.workRam+16E} tick the score-display countdown down

loc_b166:
B166: A5 37           LDA     $37                 ; {hard.workRam+37} load the walking cursor
B168: 0A              ASL     A                   ; shift the cursor low bits into the header payload
B169: 0A              ASL     A                   
B16A: 29 7F           AND     #$7F                ; mask to seven bits
B16C: A8              TAY                         
B16D: A5 37           LDA     $37                 ; {hard.workRam+37} load the walking cursor again
B16F: 4A              LSR     A                   ; shift out the cursor high bits for the header Y byte
B170: 4A              LSR     A                   
B171: 4A              LSR     A                   
B172: 4A              LSR     A                   
B173: 4A              LSR     A                   
B174: 20 6C DF        JSR     $DF6C               ; {code.emitVectorWordTag70} emit the segment header word
B177: A5 37           LDA     $37                 ; {hard.workRam+37}
B179: CD 4D 01        CMP     $014D               ; {hard.workRam+14D} first cursor position?
B17C: D0 05           BNE     $B183               ; {code.loc_b183}
B17E: A9 00           LDA     #$00                ; first position gets a plain 0 marker
B180: B8              CLV                         
B181: 50 0C           BVC     $B18F               ; {code.loc_b18f}

loc_b183:
B183: 4A              LSR     A                   ; derive the segment number from the cursor
B184: 4A              LSR     A                   
B185: 4A              LSR     A                   
B186: EA              NOP                         
B187: 29 07           AND     #$07                ; mask to the low three bits
B189: C9 07           CMP     #$07                ; top segment 7?
B18B: D0 02           BNE     $B18F               ; {code.loc_b18f}
B18D: A9 03           LDA     #$03                ; fold the top segment down to 3

loc_b18f:
B18F: A8              TAY                         
B190: A9 68           LDA     #$68                
B192: 20 4C DF        JSR     $DF4C               ; {code.emitTaggedVectorWord} emit the tick marker tagged 0x68
B195: A5 57           LDA     $57                 ; {hard.workRam+57}
B197: A6 56           LDX     $56                 ; {hard.workRam+56}
B199: 20 39 DF        JSR     $DF39               ; {code.emitCoordinateVectorWord} emit the stashed coordinate pair for this step
B19C: A5 37           LDA     $37                 ; {hard.workRam+37}
B19E: 18              CLC                         
B19F: 69 02           ADC     #$02                ; step the cursor two forward
B1A1: 85 37           STA     $37                 ; {hard.workRam+37} store the walking cursor
B1A3: CD 4E 01        CMP     $014E               ; {hard.workRam+14E} loop while the cursor stays below the far bound
B1A6: 90 BE           BCC     $B166               ; {code.loc_b166}
B1A8: A2 2C           LDX     #$2C                
B1AA: A9 D0           LDA     #$D0                
B1AC: 20 17 AB        JSR     $AB17               ; {code.drawSlotShapeWithHeader} draw the span's closing slot shape trailer
B1AF: A9 3F           LDA     #$3F                
B1B1: A2 F2           LDX     #$F2                
B1B3: 4C 39 DF        JMP     $DF39               ; {code.emitCoordinateVectorWord} emit the final trailer coordinate word

; per-frame vector housekeeping: clear frame work cells
; (resetMathboxInputs), early-return when guard cells 0x2000==0xcec6 &&
; 0x133==0 say the frame is settled; when mode cell 0x1==0 hand the whole
; draw to the frame builder drawFrame; otherwise publish the active
; pointer, run the computed-jump trampoline dispatchDisplayModeHandler,
; fold a 40-byte block under 0xb6 into checksum 0x455 (unless
; emitFrameLink reports a change), then emit the trailing header and latch
; 0xcec4/0xcec5 into display words 0x2000/0x2001.
buildFrameVectors:
B1B6: 20 C3 C1        JSR     $C1C3               ; {code.resetMathboxInputs} clear the math-box and frame work cells
B1B9: AD 00 20        LDA     $2000               ; {hard.vectorRam} read the display-list header guard word
B1BC: CD C6 CE        CMP     $CEC6               ; {hard.rom+3EC6} compare it against its level checkpoint
B1BF: D0 06           BNE     $B1C7               ; {code.loc_b1c7} guard differs: rebuild the list
B1C1: AD 33 01        LDA     $0133               ; {hard.workRam+133} read the pending level-layout trigger
B1C4: D0 01           BNE     $B1C7               ; {code.loc_b1c7} trigger set: rebuild the list
B1C6: 60              RTS                         ; frame already settled: return

loc_b1c7:
B1C7: A5 01           LDA     $01                 ; {hard.workRam+1} read the display-mode selector
B1C9: C9 00           CMP     #$00                
B1CB: F0 3C           BEQ     $B209               ; {code.loc_b209} selector zero: route the whole draw through the frame builder
B1CD: A9 00           LDA     #$00                
B1CF: 20 BE B2        JSR     $B2BE               ; {code.seatDrawCursor} seat the draw cursor for the list
B1D2: 20 32 B3        JSR     $B332               ; {code.emitFrameLink} publish the frame link
B1D5: B0 1E           BCS     $B1F5               ; {code.loc_b1f5} a change was published: skip the mode dispatch and checksum
B1D7: 20 0D B2        JSR     $B20D               ; {code.dispatchDisplayModeHandler} run the display-mode dispatch trampoline
B1DA: AD 6E 01        LDA     $016E               ; {hard.workRam+16E} score-display timer zero: skip the checksum fold
B1DD: F0 16           BEQ     $B1F5               ; {code.loc_b1f5}
B1DF: A0 27           LDY     #$27                ; walk 40 bytes of the record
B1E1: A9 0E           LDA     #$0E                ; checksum seed
B1E3: 38              SEC                         

loc_b1e4:
B1E4: F1 B6           SBC     ($B6),Y             ; {hard.workRam+B6} subtract each record byte under the draw pointer, carry-chained
B1E6: 88              DEY                         
B1E7: 10 FB           BPL     $B1E4               ; {code.loc_b1e4} fold all 40 bytes
B1E9: A8              TAY                         
B1EA: F0 02           BEQ     $B1EE               ; {code.loc_b1ee}
B1EC: 49 E5           EOR     #$E5                ; whiten the checksum with 0xe5

loc_b1ee:
B1EE: F0 02           BEQ     $B1F2               ; {code.loc_b1f2}
B1F0: 49 29           EOR     #$29                ; whiten it again with 0x29

loc_b1f2:
B1F2: 8D 55 04        STA     $0455               ; {hard.workRam+455} store the record checksum

loc_b1f5:
B1F5: A9 00           LDA     #$00                
B1F7: 20 FE B2        JSR     $B2FE               ; {code.closeLayerPointer} close the layer pointer
B1FA: AD C4 CE        LDA     $CEC4               ; {hard.rom+3EC4} latch the play-mode header low byte into the first display word
B1FD: 8D 00 20        STA     $2000               ; {hard.vectorRam} store it into the first display word
B200: AD C5 CE        LDA     $CEC5               ; {hard.rom+3EC5} latch the play-mode header high byte
B203: 8D 01 20        STA     $2001               ; {hard.vectorRam+1} store it into the second display word
B206: B8              CLV                         
B207: 50 03           BVC     $B20C               ; {code.loc_b20c}

loc_b209:
B209: 4C 30 B2        JMP     $B230               ; {code.drawFrame} route the whole frame through the frame builder

loc_b20c:
B20C: 60              RTS                         

; computed-jump trampoline turned on by the vector housekeeping: the pre-
; doubled selector in mode cell 0x1 picks one of twelve display-mode
; targets (drawFrame, $D804, $B8BA,...) from the word table and runs it,
; dissolved here into a direct TABLE[0x1>>1] select.
dispatchDisplayModeHandler:
B20D: A6 01           LDX     $01                 ; {hard.workRam+1} read the pre-doubled display-mode selector
B20F: BD 19 B2        LDA     $B219,X             ; {hard.rom+2219} push the selected handler address high byte from the mode table
B212: 48              PHA                         
B213: BD 18 B2        LDA     $B218,X             ; {hard.rom+2218} push the handler address low byte
B216: 48              PHA                         
B217: 60              RTS                         ; jump to the selected display-mode handler

; ---- $B218-$B22F: data ----
B218: 2F B2 03 D8 B9 B8 E9 AD 80 AF 1B AE 61 AA 59 AA
B228: 6E AA 01 B1 30 B1 78 AA

; draw one whole frame: route each drawing subsystem in a fixed layer
; order (ids 0x07,0x04,0x03,0x06,0x05,0x00,0x01,0x08), bracketing each
; with cursor-setup $B2BE and teardown $B2FE; inside the player layer
; (0x00), when 0x5 bit7 is clear, sum a 40-byte block reached via pointer
; 0xb6/0xb7 into status cell 0x11b, then zero change-counter 0x114 and
; latch ROM constants 0xcec2/0xcec3 into head words 0x2000/0x2001.
drawFrame:
B230: A9 07           LDA     #$07                ; seat the draw cursor for layer 07
B232: 20 BE B2        JSR     $B2BE               ; {code.seatDrawCursor}
B235: 20 86 B5        JSR     $B586               ; {code.drawScoreStatusList} draw the score / status text list
B238: A9 07           LDA     #$07                
B23A: 20 FE B2        JSR     $B2FE               ; {code.closeLayerPointer} close layer 07
B23D: A9 04           LDA     #$04                
B23F: 20 BE B2        JSR     $B2BE               ; {code.seatDrawCursor} seat the draw cursor for layer 04
B242: 20 5B B7        JSR     $B75B               ; {code.drawSlotShapeList} draw the styled slot shape list
B245: A9 04           LDA     #$04                
B247: 20 FE B2        JSR     $B2FE               ; {code.closeLayerPointer} close layer 04
B24A: A9 03           LDA     #$03                
B24C: 20 BE B2        JSR     $B2BE               ; {code.seatDrawCursor} seat the draw cursor for layer 03
B24F: 20 AD B5        JSR     $B5AD               ; {code.drawStyledSlotList} draw the secondary styled slot list
B252: A9 03           LDA     #$03                
B254: 20 FE B2        JSR     $B2FE               ; {code.closeLayerPointer} close layer 03
B257: A9 06           LDA     #$06                
B259: 20 BE B2        JSR     $B2BE               ; {code.seatDrawCursor} seat the draw cursor for layer 06
B25C: 20 9A B7        JSR     $B79A               ; {code.drawEnemyShapeList} draw the enemy shape list
B25F: A9 06           LDA     #$06                
B261: 20 FE B2        JSR     $B2FE               ; {code.closeLayerPointer} close layer 06
B264: A9 05           LDA     #$05                
B266: 20 BE B2        JSR     $B2BE               ; {code.seatDrawCursor} seat the draw cursor for layer 05
B269: 20 98 B4        JSR     $B498               ; {code.buildObjectDisplayList} build the general object display list
B26C: A9 05           LDA     #$05                
B26E: 20 FE B2        JSR     $B2FE               ; {code.closeLayerPointer} close layer 05
B271: A9 00           LDA     #$00                
B273: 20 BE B2        JSR     $B2BE               ; {code.seatDrawCursor} seat the draw cursor for the player layer 00
B276: 20 B4 A8        JSR     $A8B4               ; {code.buildTextOverlayList} build the text overlay list
B279: A5 05           LDA     $05                 ; {hard.workRam+5}
B27B: 30 0D           BMI     $B28A               ; {code.loc_b28a} status sign bit set: skip the player-shape checksum
B27D: A9 F2           LDA     #$F2                ; player-shape checksum seed
B27F: 18              CLC                         
B280: A0 27           LDY     #$27                

loc_b282:
B282: 71 B6           ADC     ($B6),Y             ; {hard.workRam+B6} add each player-shape byte under the draw pointer, carry-chained
B284: 88              DEY                         
B285: 10 FB           BPL     $B282               ; {code.loc_b282} fold all 40 bytes
B287: 8D 1B 01        STA     $011B               ; {hard.workRam+11B} store the player-shape signature

loc_b28a:
B28A: A9 00           LDA     #$00                
B28C: 20 FE B2        JSR     $B2FE               ; {code.closeLayerPointer} close the player layer 00
B28F: 20 67 B3        JSR     $B367               ; {code.paintRimLanes} draw the tube rim lanes
B292: A9 01           LDA     #$01                
B294: 20 BE B2        JSR     $B2BE               ; {code.seatDrawCursor} seat the draw cursor for layer 01
B297: 20 C2 C5        JSR     $C5C2               ; {code.buildEnemyDisplayList} build the enemy display list
B29A: A9 01           LDA     #$01                
B29C: 20 FE B2        JSR     $B2FE               ; {code.closeLayerPointer} close layer 01
B29F: A9 08           LDA     #$08                
B2A1: 20 BE B2        JSR     $B2BE               ; {code.seatDrawCursor} seat the draw cursor for layer 08
B2A4: 20 4D C5        JSR     $C54D               ; {code.drawTimedObjectList} draw the timed-object list
B2A7: A9 08           LDA     #$08                
B2A9: 20 FE B2        JSR     $B2FE               ; {code.closeLayerPointer} close layer 08
B2AC: A9 00           LDA     #$00                
B2AE: 8D 14 01        STA     $0114               ; {hard.workRam+114} clear the redraw change-counter
B2B1: AD C2 CE        LDA     $CEC2               ; {hard.rom+3EC2} latch the per-frame header low byte
B2B4: 8D 00 20        STA     $2000               ; {hard.vectorRam} store it into the first display word
B2B7: AD C3 CE        LDA     $CEC3               ; {hard.rom+3EC3} latch the per-frame header high byte
B2BA: 8D 01 20        STA     $2001               ; {hard.vectorRam+1} store it into the second display word
B2BD: 60              RTS                         

; seat the indirect draw cursor 0x74/0x75 for a layer: at stride 2*index
; pick the 16-bit pointer from table 0xce68 (when per-index flag
; 0x415+index is nonzero) else 0xce7a, publish it into 0x74/0x75, then
; clear status cell 0xa9.
seatDrawCursor:
B2BE: AA              TAX                         
B2BF: 0A              ASL     A                   ; double the layer index into a two-byte pointer-table stride
B2C0: A8              TAY                         
B2C1: BD 15 04        LDA     $0415,X             ; {hard.workRam+415} read this layer's pointer-parity flag
B2C4: D0 09           BNE     $B2CF               ; {code.loc_b2cf} nonzero flag selects pointer table A
B2C6: BE 7A CE        LDX     $CE7A,Y             ; {hard.rom+3E7A} zero flag: take the pointer low byte from table B
B2C9: B9 7B CE        LDA     $CE7B,Y             ; {hard.rom+3E7B} and its high byte
B2CC: B8              CLV                         
B2CD: 50 06           BVC     $B2D5               ; {code.loc_b2d5}

loc_b2cf:
B2CF: BE 68 CE        LDX     $CE68,Y             ; {hard.rom+3E68} nonzero flag: take the pointer low byte from table A
B2D2: B9 69 CE        LDA     $CE69,Y             ; {hard.rom+3E69} and its high byte

loc_b2d5:
B2D5: 86 74           STX     $74                 ; {hard.workRam+74} seat the indirect draw cursor low byte
B2D7: 85 75           STA     $75                 ; {hard.workRam+75} seat the draw cursor high byte
B2D9: A9 00           LDA     #$00                
B2DB: 85 A9           STA     $A9                 ; {hard.workRam+A9} clear the list offset so the walk starts at the head
B2DD: 60              RTS                         

; seat the alternate draw pointer 0x3b/0x3c: at stride 2*index pick from
; table 0xce7a (when flag 0x415+index nonzero) else 0xce68 (table sense
; reversed vs seatDrawCursor), publish it into 0x3b/0x3c, then clear
; status cell 0xa9.
seatAltDrawPointer:
B2DE: AA              TAX                         
B2DF: 0A              ASL     A                   ; double the layer index into a two-byte pointer-table stride
B2E0: A8              TAY                         
B2E1: BD 15 04        LDA     $0415,X             ; {hard.workRam+415} read this layer's pointer-parity flag
B2E4: D0 09           BNE     $B2EF               ; {code.loc_b2ef} nonzero flag selects pointer table B -- sense reversed from the primary seater
B2E6: BE 68 CE        LDX     $CE68,Y             ; {hard.rom+3E68} zero flag: take the pointer low byte from table A
B2E9: B9 69 CE        LDA     $CE69,Y             ; {hard.rom+3E69} and its high byte
B2EC: B8              CLV                         
B2ED: 50 06           BVC     $B2F5               ; {code.loc_b2f5}

loc_b2ef:
B2EF: BE 7A CE        LDX     $CE7A,Y             ; {hard.rom+3E7A} nonzero flag: take the pointer low byte from table B
B2F2: B9 7B CE        LDA     $CE7B,Y             ; {hard.rom+3E7B} and its high byte

loc_b2f5:
B2F5: 86 3B           STX     $3B                 ; {hard.workRam+3B} seat the alternate draw pointer low byte
B2F7: 85 3C           STA     $3C                 ; {hard.workRam+3C} and its high byte
B2F9: A9 00           LDA     #$00                
B2FB: 85 A9           STA     $A9                 ; {hard.workRam+A9} clear the list offset so the consumer starts at the head
B2FD: 60              RTS                         

; close a layer: emit a header record (emitRecordBodyC0), seat base
; pointer from 0xce8c/0xce8d at stride 2*slot, toggle the layer's parity
; flag 0x415+slot, and write the ($3b) pointer target with the word chosen
; by parity — 0xceb0/0xceb1 when set, else 0xce9e/0xce9f.
closeLayerPointer:
B2FE: 48              PHA                         
B2FF: 20 09 DF        JSR     $DF09               ; {code.emitRecordBodyC0} finalize the layer's header record
B302: 68              PLA                         
B303: AA              TAX                         
B304: 0A              ASL     A                   ; double the slot into a two-byte table index
B305: A8              TAY                         
B306: B9 8C CE        LDA     $CE8C,Y             ; {hard.rom+3E8C} read the layer's base pointer low byte
B309: 85 3B           STA     $3B                 ; {hard.workRam+3B} seat the working pointer low byte
B30B: B9 8D CE        LDA     $CE8D,Y             ; {hard.rom+3E8D} base pointer high byte
B30E: 85 3C           STA     $3C                 ; {hard.workRam+3C} seat working pointer high byte
B310: BD 15 04        LDA     $0415,X             ; {hard.workRam+415} read this slot's double-buffer parity flag
B313: 49 01           EOR     #$01                ; toggle it
B315: 9D 15 04        STA     $0415,X             ; {hard.workRam+415} store the toggled parity back
B318: D0 09           BNE     $B323               ; {code.loc_b323} parity set selects the odd draw buffer
B31A: B9 9E CE        LDA     $CE9E,Y             ; {hard.rom+3E9E} even buffer pointer low byte
B31D: BE 9F CE        LDX     $CE9F,Y             ; {hard.rom+3E9F} even buffer pointer high byte
B320: B8              CLV                         
B321: 50 06           BVC     $B329               ; {code.loc_b329}

loc_b323:
B323: B9 B0 CE        LDA     $CEB0,Y             ; {hard.rom+3EB0} odd buffer pointer low byte
B326: BE B1 CE        LDX     $CEB1,Y             ; {hard.rom+3EB1} odd buffer pointer high byte

loc_b329:
B329: A0 00           LDY     #$00                
B32B: 91 3B           STA     ($3B),Y             ; {hard.workRam+3B} write the selected buffer pointer low byte through the working pointer
B32D: 8A              TXA                         
B32E: C8              INY                         
B32F: 91 3B           STA     ($3B),Y             ; {hard.workRam+3B} and its high byte
B331: 60              RTS                         

; emit a frame-link record with a mid-frame-change guard: if source 0xcec4
; differs from checkpoint 0x2000, latch it into 0x2000 and return carry
; set (caller redoes the frame); else copy a word from 0xce9e (offset 8
; when 0x415 nonzero, else 2) through cursor 0x74, clear 0x16e, reload
; cursor 0x74/0x75 from 0xce68 at that offset, and return carry clear.
emitFrameLink:
B332: AD C4 CE        LDA     $CEC4               ; {hard.rom+3EC4} read the live vector-list source header
B335: CD 00 20        CMP     $2000               ; {hard.vectorRam} compare it against the checkpoint copy
B338: F0 05           BEQ     $B33F               ; {code.loc_b33f} unchanged: go emit the frame link
B33A: 8D 00 20        STA     $2000               ; {hard.vectorRam} source moved mid-frame: re-latch the checkpoint
B33D: 38              SEC                         ; signal the caller to rebuild the frame
B33E: 60              RTS                         

loc_b33f:
B33F: AD 15 04        LDA     $0415               ; {hard.workRam+415} read the pointer-parity mode flag
B342: D0 05           BNE     $B349               ; {code.loc_b349} nonzero mode picks the 0x08 record slot
B344: A2 02           LDX     #$02                ; otherwise the 0x02 record slot
B346: B8              CLV                         
B347: 50 02           BVC     $B34B               ; {code.loc_b34b}

loc_b349:
B349: A2 08           LDX     #$08                ; the 0x08 record slot

loc_b34b:
B34B: BD 9E CE        LDA     $CE9E,X             ; {hard.rom+3E9E} read the selected buffer word's low byte
B34E: A0 00           LDY     #$00                
B350: 8C 6E 01        STY     $016E               ; {hard.workRam+16E} clear the score-display timer
B353: 91 74           STA     ($74),Y             ; {hard.workRam+74} splice the low byte into the list at the draw cursor
B355: C8              INY                         
B356: BD 9F CE        LDA     $CE9F,X             ; {hard.rom+3E9F} selected buffer word's high byte
B359: 91 74           STA     ($74),Y             ; {hard.workRam+74} splice the high byte
B35B: BD 68 CE        LDA     $CE68,X             ; {hard.rom+3E68} reload the draw cursor low byte from the second table so the next record chains on
B35E: 85 74           STA     $74                 ; {hard.workRam+74}
B360: BD 69 CE        LDA     $CE69,X             ; {hard.rom+3E69} and its high byte
B363: 85 75           STA     $75                 ; {hard.workRam+75}
B365: 18              CLC                         
B366: 60              RTS                         

; rebuild the sixteen-entry lane-flag block 0x425 from the active enemy
; tables (depth 0x2df, lane 0x283, near/far segments 0x2cc/0x2b9) and
; paint the rim lanes: an optional pre-pass seats pointers
; (seatDrawCursor/initAndDrawRimDepthCounters/closeLayerPointer on 0x114),
; a first pass writes each column's colour value through the ($3b) list,
; and a second pass ORs colour bits (0x00 or 0xc0) into the ($b0) list.
paintRimLanes:
B367: AD 14 01        LDA     $0114               ; {hard.workRam+114} read the redraw counter
B36A: F0 0D           BEQ     $B379               ; {code.loc_b379} clear: skip the pointer pre-pass
B36C: A9 02           LDA     #$02                
B36E: 20 BE B2        JSR     $B2BE               ; {code.seatDrawCursor} seat the draw cursor for rim layer 2
B371: 20 0D C3        JSR     $C30D               ; {code.initAndDrawRimDepthCounters} init and draw the rim depth counters
B374: A9 02           LDA     #$02                
B376: 20 FE B2        JSR     $B2FE               ; {code.closeLayerPointer} close rim layer 2 and flip its buffer

loc_b379:
B379: A9 02           LDA     #$02                
B37B: 20 DE B2        JSR     $B2DE               ; {code.seatAltDrawPointer} refresh the alternate draw pointer for layer 2
B37E: A9 00           LDA     #$00                
B380: A2 0F           LDX     #$0F                

loc_b382:
B382: 9D 25 04        STA     $0425,X             ; {hard.workRam+425} clear the sixteen-entry lane-flag block
B385: CA              DEX                         
B386: 10 FA           BPL     $B382               ; {code.loc_b382}

; ---- $B388-$B38A: data ----
B388: AD 06 01
B38B: 30 49           BMI     $B3D6               ; {code.loc_b3d6} spike/close-up guard negative: skip the enemy-state merge
B38D: AE 1C 01        LDX     $011C               ; {hard.workRam+11C} start the enemy-slot sweep at the top slot

loc_b390:
B390: BD DF 02        LDA     $02DF,X             ; {hard.workRam+2DF} read this slot's depth
B393: F0 3E           BEQ     $B3D3               ; {code.loc_b3d3} empty slot: skip
B395: A0 00           LDY     #$00                
B397: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} read this slot's state flags
B39A: 29 07           AND     #$07                ; low three state bits
B39C: C9 01           CMP     #$01                ; on-rim state?
B39E: D0 33           BNE     $B3D3               ; {code.loc_b3d3} not drawn on the rim: skip
B3A0: C8              INY                         
B3A1: 84 29           STY     $29                 ; {hard.workRam+29} seed the per-lane flag byte at 1
B3A3: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} re-read the slot state flags
B3A6: 29 80           AND     #$80                ; test the sign bit
B3A8: D0 1C           BNE     $B3C6               ; {code.loc_b3c6} sign set: skip the near-lane contribution
B3AA: AD 48 01        LDA     $0148               ; {hard.workRam+148} read the enemy animation accumulator
B3AD: 30 0C           BMI     $B3BB               ; {code.loc_b3bb} not animating: don't bump the flag
B3AF: BD DF 02        LDA     $02DF,X             ; {hard.workRam+2DF} read this slot's depth
B3B2: CD 57 01        CMP     $0157               ; {hard.workRam+157} compare against the near-rim depth threshold
B3B5: B0 04           BCS     $B3BB               ; {code.loc_b3bb} farther than the threshold: don't bump
B3B7: E6 29           INC     $29                 ; {hard.workRam+29} nearer while animating: bump the lane flag so the lane blinks
B3B9: E6 29           INC     $29                 ; {hard.workRam+29}

loc_b3bb:
B3BB: A5 29           LDA     $29                 ; {hard.workRam+29} load the per-lane flag byte
B3BD: BC CC 02        LDY     $02CC,X             ; {hard.workRam+2CC} near lane index
B3C0: 19 25 04        ORA     $0425,Y             ; {hard.workRam+425}
B3C3: 99 25 04        STA     $0425,Y             ; {hard.workRam+425} OR the flag into the near lane

loc_b3c6:
B3C6: BC B9 02        LDY     $02B9,X             ; {hard.workRam+2B9} far lane index
B3C9: A5 29           LDA     $29                 ; {hard.workRam+29}
B3CB: 09 80           ORA     #$80                ; tag the far lane with bit7
B3CD: 19 25 04        ORA     $0425,Y             ; {hard.workRam+425}
B3D0: 99 25 04        STA     $0425,Y             ; {hard.workRam+425} OR the tagged flag into the far lane

loc_b3d3:
B3D3: CA              DEX                         
B3D4: 10 BA           BPL     $B390               ; {code.loc_b390}

loc_b3d6:
B3D6: A9 06           LDA     #$06                ; base rim colour
B3D8: AC 25 01        LDY     $0125               ; {hard.workRam+125} read the wave-phase latch
B3DB: F0 0C           BEQ     $B3E9               ; {code.loc_b3e9}
B3DD: 30 0A           BMI     $B3E9               ; {code.loc_b3e9}
B3DF: A5 03           LDA     $03                 ; {hard.workRam+3}
B3E1: 29 07           AND     #$07                
B3E3: C9 07           CMP     #$07                ; every eighth frame while the wave is ready...
B3E5: D0 02           BNE     $B3E9               ; {code.loc_b3e9}
B3E7: A9 01           LDA     #$01                ; ...use the alternate base colour

loc_b3e9:
B3E9: 85 29           STA     $29                 ; {hard.workRam+29} latch the base colour
B3EB: A0 FF           LDY     #$FF                
B3ED: A2 FF           LDX     #$FF                
B3EF: 86 2C           STX     $2C                 ; {hard.workRam+2C} default the colour-cycle ramp offset to none
B3F1: AD 02 02        LDA     $0202               ; {hard.workRam+202} read the player's shot depth
B3F4: F0 0B           BEQ     $B401               ; {code.loc_b401} no live shot: no aim highlight
B3F6: AD 01 02        LDA     $0201               ; {hard.workRam+201} read the player's fine aim angle
B3F9: 30 06           BMI     $B401               ; {code.loc_b401}
B3FB: AE 00 02        LDX     $0200               ; {hard.workRam+200} aim column A = the player's segment
B3FE: AC 01 02        LDY     $0201               ; {hard.workRam+201} aim column B = the player's fine angle

loc_b401:
B401: 86 2A           STX     $2A                 ; {hard.workRam+2A} cache aim column A
B403: 84 2B           STY     $2B                 ; {hard.workRam+2B} cache aim column B
B405: AD 24 01        LDA     $0124               ; {hard.workRam+124} read the rim colour-cycle phase
B408: 30 08           BMI     $B412               ; {code.loc_b412} phase exhausted: no rotating ramp
B40A: 29 0E           AND     #$0E                
B40C: 4A              LSR     A                   
B40D: 85 2C           STA     $2C                 ; {hard.workRam+2C} set the ramp offset from the colour-cycle phase
B40F: CE 24 01        DEC     $0124               ; {hard.workRam+124} advance the rim colour cycle

loc_b412:
B412: A2 0F           LDX     #$0F                ; first pass: lanes 15..0

loc_b414:
B414: A0 06           LDY     #$06                
B416: BD 25 04        LDA     $0425,X             ; {hard.workRam+425} read this lane's flag
B419: F0 0C           BEQ     $B427               ; {code.loc_b427} unflagged lane: pick an aim or ramp colour
B41B: 29 02           AND     #$02                ; test the blink bit
B41D: F0 05           BEQ     $B424               ; {code.loc_b424} flagged but non-blink: solid colour
B41F: A5 03           LDA     $03                 ; {hard.workRam+3} blink with frame parity
B421: 29 01           AND     #$01                
B423: A8              TAY                         

loc_b424:
B424: B8              CLV                         
B425: 50 24           BVC     $B44B               ; {code.loc_b44b}

loc_b427:
B427: E4 2A           CPX     $2A                 ; {hard.workRam+2A} compare the lane to aim column A
B429: F0 02           BEQ     $B42D               ; {code.loc_b42d}
B42B: E4 2B           CPX     $2B                 ; {hard.workRam+2B} compare the lane to aim column B

loc_b42d:
B42D: D0 05           BNE     $B434               ; {code.loc_b434} not an aim column
B42F: A0 01           LDY     #$01                ; aim column: highlight colour
B431: B8              CLV                         
B432: 50 17           BVC     $B44B               ; {code.loc_b44b}

loc_b434:
B434: AD 24 01        LDA     $0124               ; {hard.workRam+124} read the colour-cycle phase
B437: 30 10           BMI     $B449               ; {code.loc_b449} ramp exhausted: use the held base colour
B439: 8A              TXA                         
B43A: 18              CLC                         
B43B: 65 2C           ADC     $2C                 ; {hard.workRam+2C} rotate the ramp by the lane index
B43D: 29 07           AND     #$07                
B43F: C9 07           CMP     #$07                
B441: D0 02           BNE     $B445               ; {code.loc_b445}
B443: A9 03           LDA     #$03                ; wrap the top ramp step to colour 3

loc_b445:
B445: A8              TAY                         
B446: B8              CLV                         
B447: 50 02           BVC     $B44B               ; {code.loc_b44b}

loc_b449:
B449: A4 29           LDY     $29                 ; {hard.workRam+29} held base colour

loc_b44b:
B44B: 98              TYA                         
B44C: BC 76 B4        LDY     $B476,X             ; {hard.rom+2476} look up this lane's slot in the rim list
B44F: 91 3B           STA     ($3B),Y             ; {hard.workRam+3B} write the colour into the rim display list
B451: CA              DEX                         
B452: 10 C0           BPL     $B414               ; {code.loc_b414}

; ---- $B454-$B455: data ----
B454: A2 0F
B456: 2C 11 01        BIT     $0111               ; {hard.workRam+111} read the tube-geometry flag
B459: 10 01           BPL     $B45C               ; {code.loc_b45c}
B45B: CA              DEX                         ; geometry set: start the second pass one lane lower

loc_b45c:
B45C: A0 C0           LDY     #$C0                
B45E: BD 25 04        LDA     $0425,X             ; {hard.workRam+425} read this lane's flag
B461: 10 02           BPL     $B465               ; {code.loc_b465} bit7 clear keeps the colour bits
B463: A0 00           LDY     #$00                ; bit7 set clears the colour bits

loc_b465:
B465: 84 58           STY     $58                 ; {hard.workRam+58}
B467: BC 87 B4        LDY     $B487,X             ; {hard.rom+2487} look up this lane's slot in the patch list
B46A: B1 B0           LDA     ($B0),Y             ; {hard.workRam+B0} read the current patch-list byte
B46C: 29 1F           AND     #$1F                ; keep its low five bits
B46E: 05 58           ORA     $58                 ; {hard.workRam+58} fold in the chosen colour bits
B470: 91 B0           STA     ($B0),Y             ; {hard.workRam+B0} write the recoloured byte back to the patch list
B472: CA              DEX                         
B473: 10 E7           BPL     $B45C               ; {code.loc_b45c}

; ---- $B475-$B497: data ----
B475: 60 A8 9C 92 86 7C 70 66 5A 50 44 3A 2E 24 18 0E
B485: 02 B2 3B 37 33 2F 2B 27 23 1F 1B 17 13 0F 0B 07
B495: 03 3F 1D

; build a vector display list for up to 0x12 active objects (kind from tag
; table 0x243, coords via 0x203 into the four coord banks
; 0x35a/0x36a/0x37a/0x38a): emit a rotated header code, screen-relative
; coordinate words and their negated shadow words per object through
; cursor 0x74/0x75, flushing the cursor when the byte offset saturates,
; then close with a trailing header (emitBlankVectorWordTag70).
buildObjectDisplayList:
B498: A0 0C           LDY     #$0C                
B49A: 84 9E           STY     $9E                 ; {hard.workRam+9E} run count for the record header
B49C: A9 08           LDA     #$08                
B49E: 20 4C DF        JSR     $DF4C               ; {code.emitTaggedVectorWord} emit the leading tagged vector word
B4A1: A2 66           LDX     #$66                
B4A3: 20 65 C7        JSR     $C765               ; {code.layHeaderAndBuildRecord} open the object record header
B4A6: A9 12           LDA     #$12                
B4A8: 85 56           STA     $56                 ; {hard.workRam+56} draw budget: at most 18 objects
B4AA: A2 3F           LDX     #$3F                
B4AC: 86 37           STX     $37                 ; {hard.workRam+37} scan object slots from the top down
B4AE: A0 00           LDY     #$00                

loc_b4b0:
B4B0: A6 37           LDX     $37                 ; {hard.workRam+37}
B4B2: BD 43 02        LDA     $0243,X             ; {hard.workRam+243} read this slot's object kind
B4B5: D0 03           BNE     $B4BA               ; {code.loc_b4ba}
B4B7: 4C 49 B5        JMP     $B549               ; {code.loc_b549} empty slot: move to the next

loc_b4ba:
B4BA: C9 50           CMP     #$50                ; high kinds...
B4BC: 90 02           BCC     $B4C0               ; {code.loc_b4c0}
B4BE: C6 37           DEC     $37                 ; {hard.workRam+37} ...consume an extra slot

loc_b4c0:
B4C0: 48              PHA                         
B4C1: 29 3F           AND     #$3F                ; low six bits are the shape selector
B4C3: 91 74           STA     ($74),Y             ; {hard.workRam+74} write the shape selector into the display list
B4C5: 68              PLA                         
B4C6: 2A              ROL     A                   ; rotate the kind byte to lift its top bits
B4C7: 2A              ROL     A                   
B4C8: 2A              ROL     A                   
B4C9: 29 03           AND     #$03                
B4CB: 18              CLC                         
B4CC: 69 01           ADC     #$01                
B4CE: 09 70           ORA     #$70                ; form the 0x70-tagged header code
B4D0: C8              INY                         
B4D1: 91 74           STA     ($74),Y             ; {hard.workRam+74} write the header word
B4D3: C8              INY                         
B4D4: BD 03 02        LDA     $0203,X             ; {hard.workRam+203} look up the object's record index
B4D7: AA              TAX                         
B4D8: BD 8A 03        LDA     $038A,X             ; {hard.workRam+38A} object X low byte
B4DB: 38              SEC                         
B4DC: E5 68           SBC     $68                 ; {hard.workRam+68} subtract the viewpoint X offset
B4DE: 85 63           STA     $63                 ; {hard.workRam+63}
B4E0: 91 74           STA     ($74),Y             ; {hard.workRam+74} emit the projected X low byte
B4E2: C8              INY                         
B4E3: BD 7A 03        LDA     $037A,X             ; {hard.workRam+37A} object X high byte
B4E6: E5 69           SBC     $69                 ; {hard.workRam+69} subtract the viewpoint X offset with borrow
B4E8: 85 64           STA     $64                 ; {hard.workRam+64}
B4EA: 29 1F           AND     #$1F                ; vector word high byte is five bits
B4EC: 91 74           STA     ($74),Y             ; {hard.workRam+74} emit the projected X high byte
B4EE: C8              INY                         
B4EF: BD 6A 03        LDA     $036A,X             ; {hard.workRam+36A} object Y low byte
B4F2: 85 61           STA     $61                 ; {hard.workRam+61}
B4F4: 91 74           STA     ($74),Y             ; {hard.workRam+74} emit the Y low byte
B4F6: C8              INY                         
B4F7: BD 5A 03        LDA     $035A,X             ; {hard.workRam+35A} object Y high byte
B4FA: 85 62           STA     $62                 ; {hard.workRam+62}
B4FC: 29 1F           AND     #$1F                
B4FE: 91 74           STA     ($74),Y             ; {hard.workRam+74} emit the Y high byte
B500: C8              INY                         
B501: A9 00           LDA     #$00                
B503: 91 74           STA     ($74),Y             ; {hard.workRam+74} three zero separator bytes...
B505: C8              INY                         
B506: 91 74           STA     ($74),Y             ; {hard.workRam+74}
B508: C8              INY                         
B509: 91 74           STA     ($74),Y             ; {hard.workRam+74}
B50B: A9 A0           LDA     #$A0                ; ...ending in the 0xa0 tag
B50D: C8              INY                         
B50E: 91 74           STA     ($74),Y             ; {hard.workRam+74} write the tag byte
B510: C8              INY                         
B511: A5 63           LDA     $63                 ; {hard.workRam+63} negated X low byte -- the beam return stroke to origin
B513: 49 FF           EOR     #$FF                
B515: 18              CLC                         
B516: 69 01           ADC     #$01                
B518: 91 74           STA     ($74),Y             ; {hard.workRam+74} emit it
B51A: C8              INY                         
B51B: A5 64           LDA     $64                 ; {hard.workRam+64} negated X high byte with carry
B51D: 49 FF           EOR     #$FF                
B51F: 69 00           ADC     #$00                
B521: 29 1F           AND     #$1F                
B523: 91 74           STA     ($74),Y             ; {hard.workRam+74} emit it
B525: C8              INY                         
B526: A5 61           LDA     $61                 ; {hard.workRam+61} negated Y low byte
B528: 49 FF           EOR     #$FF                
B52A: 18              CLC                         
B52B: 69 01           ADC     #$01                
B52D: 91 74           STA     ($74),Y             ; {hard.workRam+74} emit it
B52F: C8              INY                         
B530: A5 62           LDA     $62                 ; {hard.workRam+62} negated Y high byte with carry
B532: 49 FF           EOR     #$FF                
B534: 69 00           ADC     #$00                
B536: 29 1F           AND     #$1F                
B538: 91 74           STA     ($74),Y             ; {hard.workRam+74} emit it
B53A: C8              INY                         
B53B: C0 F0           CPY     #$F0                ; page nearly full?
B53D: 90 06           BCC     $B545               ; {code.loc_b545}
B53F: 88              DEY                         
B540: 20 5F DF        JSR     $DF5F               ; {code.advanceDisplayCursor} flush the display page
B543: A0 00           LDY     #$00                

loc_b545:
B545: C6 56           DEC     $56                 ; {hard.workRam+56} spend one from the draw budget
B547: 30 07           BMI     $B550               ; {code.loc_b550} budget exhausted: done

loc_b549:
B549: C6 37           DEC     $37                 ; {hard.workRam+37} step to the next slot down
B54B: 30 03           BMI     $B550               ; {code.loc_b550} scanned past slot 0: done
B54D: 4C B0 B4        JMP     $B4B0               ; {code.loc_b4b0}

loc_b550:
B550: 98              TYA                         
B551: F0 04           BEQ     $B557               ; {code.loc_b557}
B553: 88              DEY                         
B554: 20 5F DF        JSR     $DF5F               ; {code.advanceDisplayCursor} flush the final partial page

loc_b557:
B557: A5 B5           LDA     $B5                 ; {hard.workRam+B5} read the rolling display checksum
B559: F0 0A           BEQ     $B565               ; {code.loc_b565}
B55B: A5 46           LDA     $46                 ; {hard.workRam+46}
B55D: C9 0A           CMP     #$0A                ; on level 10 or higher...
B55F: 90 04           BCC     $B565               ; {code.loc_b565}
B561: A9 7A           LDA     #$7A                ; ...a nonzero checksum stamps the interrupt heartbeat -- an anti-tamper poke
B563: 85 53           STA     $53                 ; {hard.workRam+53}

loc_b565:
B565: A9 01           LDA     #$01                
B567: 4C 6A DF        JMP     $DF6A               ; {code.emitBlankVectorWordTag70} close the list with a trailing blank tagged word

; Stores 0, 0, 0, A into the four bytes at the working pointer
; loc_74/loc_75 and advances the cursor by four.
emitBlankValueRecord:
B56A: 48              PHA                         
B56B: A0 00           LDY     #$00                
B56D: 98              TYA                         
B56E: 91 74           STA     ($74),Y             ; {hard.workRam+74} three zero fields...
B570: C8              INY                         
B571: 91 74           STA     ($74),Y             ; {hard.workRam+74}
B573: C8              INY                         
B574: 91 74           STA     ($74),Y             ; {hard.workRam+74}
B576: C8              INY                         
B577: 68              PLA                         
B578: 91 74           STA     ($74),Y             ; {hard.workRam+74} ...then the caller's value byte
B57A: A9 04           LDA     #$04                
B57C: 18              CLC                         
B57D: 65 74           ADC     $74                 ; {hard.workRam+74} advance the draw cursor by four
B57F: 85 74           STA     $74                 ; {hard.workRam+74}
B581: 90 02           BCC     $B585               ; {code.loc_b585}
B583: E6 75           INC     $75                 ; {hard.workRam+75} carry into the cursor high byte

loc_b585:
B585: 60              RTS                         

; build the score/status vector run: raise rebuild flag 0x9e=0x01, read
; gate 0x202 and bail if 0 or >=0xf0, else latch it into 0x57 and 0x2f and
; — unless marker 0x201 holds 0x81 — kick the run builder
; drawTubeRimSegmentFromCorner with corner index 0x200 and size
; ((0x51>>1)&7)+1.
drawScoreStatusList:
B586: A9 01           LDA     #$01                
B588: 85 9E           STA     $9E                 ; {hard.workRam+9E} raise the rebuild flag for this frame
B58A: AD 02 02        LDA     $0202               ; {hard.workRam+202} read the marker's depth/gate
B58D: F0 1D           BEQ     $B5AC               ; {code.loc_b5ac} zero: nothing to show
B58F: C9 F0           CMP     #$F0                
B591: B0 19           BCS     $B5AC               ; {code.loc_b5ac} out of the valid depth band: skip
B593: 85 57           STA     $57                 ; {hard.workRam+57} latch the depth
B595: 85 2F           STA     $2F                 ; {hard.workRam+2F} and its mirror
B597: AD 01 02        LDA     $0201               ; {hard.workRam+201} read the marker byte
B59A: C9 81           CMP     #$81                
B59C: F0 0E           BEQ     $B5AC               ; {code.loc_b5ac} skip marker 0x81: draw nothing
B59E: AC 00 02        LDY     $0200               ; {hard.workRam+200} the player's segment is the corner index
B5A1: A5 51           LDA     $51                 ; {hard.workRam+51} read the rim rotation offset
B5A3: 4A              LSR     A                   
B5A4: 29 07           AND     #$07                
B5A6: 18              CLC                         
B5A7: 69 01           ADC     #$01                ; spread size 1..8 from the rotation offset
B5A9: 20 A0 BD        JSR     $BDA0               ; {code.drawTubeRimSegmentFromCorner} emit the rim-segment spread from the corner

loc_b5ac:
B5AC: 60              RTS                         

; draw a per-slot vector record for seven slots (0x37 from 6 down) when
; guard 0x106 bit7 is clear: for each non-empty control 0x2df+x cache it
; in 0x57, split paired byte 0x283+x into style nibble
; 0x55=(paired&0x18)>>3 and a doubled selector (paired&7)<<1, and dispatch
; the style's draw handler via dispatchSlotDrawHandler carrying slot index
; x.
drawStyledSlotList:
B5AD: AD 06 01        LDA     $0106               ; {hard.workRam+106} read the spike guard
B5B0: 30 24           BMI     $B5D6               ; {code.loc_b5d6} spike/close-up pass suppresses the slot draw
B5B2: A2 06           LDX     #$06                
B5B4: 86 37           STX     $37                 ; {hard.workRam+37} walk the seven tube slots 6..0

loc_b5b6:
B5B6: A6 37           LDX     $37                 ; {hard.workRam+37}
B5B8: BD DF 02        LDA     $02DF,X             ; {hard.workRam+2DF} read this slot's enemy control/depth
B5BB: F0 15           BEQ     $B5D2               ; {code.loc_b5d2} empty slot: skip
B5BD: 85 57           STA     $57                 ; {hard.workRam+57} hand the depth to the draw handler
B5BF: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} read the paired flags byte
B5C2: 29 18           AND     #$18                ; style nibble, bits 4..3
B5C4: 4A              LSR     A                   
B5C5: 4A              LSR     A                   
B5C6: 4A              LSR     A                   
B5C7: 85 55           STA     $55                 ; {hard.workRam+55} latch the draw style
B5C9: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} low three bits, doubled into a shape selector
B5CC: 29 07           AND     #$07                
B5CE: 0A              ASL     A                   
B5CF: 20 D7 B5        JSR     $B5D7               ; {code.dispatchSlotDrawHandler} dispatch this slot's draw handler

loc_b5d2:
B5D2: C6 37           DEC     $37                 ; {hard.workRam+37}
B5D4: 10 E0           BPL     $B5B6               ; {code.loc_b5b6}

loc_b5d6:
B5D6: 60              RTS                         

; computed jump: select one of five slot-draw handlers
; [$B5EB,$B71B,$B60F,$B622,$B69B] by A>>1 and tail-return its result,
; carrying the slot index x.
dispatchSlotDrawHandler:
B5D7: A8              TAY                         
B5D8: B9 E2 B5        LDA     $B5E2,Y             ; {hard.rom+25E2} look up the draw handler's address for this style
B5DB: 48              PHA                         
B5DC: B9 E1 B5        LDA     $B5E1,Y             ; {hard.rom+25E1}
B5DF: 48              PHA                         
B5E0: 60              RTS                         ; jump into the selected handler

; ---- $B5E1-$B5EA: data ----
B5E1: EA B5 1A B7 0E B6 21 B6 9A B6

; draw the rim segment for slot x: set run count loc_9e=0x03, and on a
; negative slot byte loc_283+x prep a coordinate (buildSlotScreenPoint)
; and build at corner 0 (emitTubeRimSegmentVectors(0)), else build at the
; slot's own corner loc_2b9+x with a header picked from $B60B by style
; loc_55.
drawSlotRimSegment:
B5EB: A9 03           LDA     #$03                
B5ED: 85 9E           STA     $9E                 ; {hard.workRam+9E} three vectors make the rim segment
B5EF: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} read this slot's flag byte
B5F2: 30 0E           BMI     $B602               ; {code.loc_b602} negative slot: compute the point and draw at corner 0
B5F4: BC B9 02        LDY     $02B9,X             ; {hard.workRam+2B9} the slot's own tube corner
B5F7: A6 55           LDX     $55                 ; {hard.workRam+55}
B5F9: BD 0B B6        LDA     $B60B,X             ; {hard.rom+260B} pick the shape header for this draw style
B5FC: 20 A0 BD        JSR     $BDA0               ; {code.drawTubeRimSegmentFromCorner} draw the rim segment from the corner
B5FF: B8              CLV                         
B600: 50 08           BVC     $B60A               ; {code.loc_b60a}

loc_b602:
B602: 20 34 B6        JSR     $B634               ; {code.buildSlotScreenPoint} derive the slot's screen point
B605: A0 00           LDY     #$00                
B607: 20 CB BD        JSR     $BDCB               ; {code.emitTubeRimSegmentVectors} emit the rim segment anchored at corner 0

loc_b60a:
B60A: 60              RTS                         

; ---- $B60B-$B60E: data ----
B60B: 00 00 00 00

; Pairs a jump-mode byte from table $B61E (indexed by loc_28a+x & 0x03)
; with slot target loc_2b9+x and emits via bcfd.
emitJumpModeSlot:
B60F: BD 8A 02        LDA     $028A,X             ; {hard.workRam+28A} read the enemy's direction byte
B612: 29 03           AND     #$03                ; low two bits pick one of four jump-frame shapes
B614: A8              TAY                         
B615: B9 1E B6        LDA     $B61E,Y             ; {hard.rom+261E} look up the jump-frame shape
B618: BC B9 02        LDY     $02B9,X             ; {hard.workRam+2B9} the enemy's target segment
B61B: 4C FD BC        JMP     $BCFD               ; {code.seatShapeParamsAndEmit} seat the shape and emit its vector record

; ---- $B61E-$B621: data ----
B61E: 1A 1A 4A 4C

; Pairs slot target loc_2b9+x with a four-phase animation offset (((loc_3
; & 0x03)<<1)+0x12) and emits via bcfd.
emitAnimatedPhaseSlot:
B622: BC B9 02        LDY     $02B9,X             ; {hard.workRam+2B9} the lane this enemy occupies
B625: A5 03           LDA     $03                 ; {hard.workRam+3} frame counter
B627: 29 03           AND     #$03                
B629: 0A              ASL     A                   
B62A: 18              CLC                         
B62B: 69 12           ADC     #$12                ; four-phase shape index 0x12..0x18 from the frame counter
B62D: 4C FD BC        JMP     $BCFD               ; {code.seatShapeParamsAndEmit} seat the shape and emit its record

; ---- $B630-$B633: data ----
B630: 12 14 16 18

; build slot x's screen point: index base coords loc_3ce/loc_3de by the
; slot's segment loc_2b9,x into loc_56/loc_58, offset each by the signed
; animation delta $B68B/$B687 at phase loc_2cc,x&0x0f (0x80-biased
; saturating add) into loc_2e (X)/loc_30 (Y), copy loc_57 to loc_2f, and
; load the style pair $BCDC/$BCEC at loc_112 into loc_59/loc_5a.
buildSlotScreenPoint:
B634: A5 57           LDA     $57                 ; {hard.workRam+57} stage the projection depth
B636: 85 2F           STA     $2F                 ; {hard.workRam+2F}
B638: BC B9 02        LDY     $02B9,X             ; {hard.workRam+2B9} the slot's segment number
B63B: B9 CE 03        LDA     $03CE,Y             ; {hard.workRam+3CE} base X of the segment corner
B63E: 85 56           STA     $56                 ; {hard.workRam+56}
B640: B9 DE 03        LDA     $03DE,Y             ; {hard.workRam+3DE} base Y of the segment corner
B643: 85 58           STA     $58                 ; {hard.workRam+58}
B645: BD CC 02        LDA     $02CC,X             ; {hard.workRam+2CC} animation phase, low nibble
B648: 29 0F           AND     #$0F                
B64A: A8              TAY                         
B64B: A5 56           LDA     $56                 ; {hard.workRam+56}
B64D: 49 80           EOR     #$80                
B64F: 18              CLC                         
B650: 79 8B B6        ADC     $B68B,Y             ; {hard.rom+268B} add the per-phase X vertex offset -- signed, excess-128
B653: 50 09           BVC     $B65E               ; {code.loc_b65e}
B655: 10 05           BPL     $B65C               ; {code.loc_b65c}
B657: A9 7F           LDA     #$7F                ; clamp toward the sign that overflowed
B659: B8              CLV                         
B65A: 50 02           BVC     $B65E               ; {code.loc_b65e}

loc_b65c:
B65C: A9 80           LDA     #$80                

loc_b65e:
B65E: 49 80           EOR     #$80                
B660: 85 2E           STA     $2E                 ; {hard.workRam+2E} store the finished screen X
B662: A5 58           LDA     $58                 ; {hard.workRam+58}
B664: 49 80           EOR     #$80                
B666: 18              CLC                         
B667: 79 87 B6        ADC     $B687,Y             ; {hard.rom+2687} add the per-phase Y vertex offset
B66A: 50 09           BVC     $B675               ; {code.loc_b675}
B66C: 10 05           BPL     $B673               ; {code.loc_b673}
B66E: A9 7F           LDA     #$7F                ; clamp on signed overflow
B670: B8              CLV                         
B671: 50 02           BVC     $B675               ; {code.loc_b675}

loc_b673:
B673: A9 80           LDA     #$80                

loc_b675:
B675: 49 80           EOR     #$80                
B677: 85 30           STA     $30                 ; {hard.workRam+30} store the finished screen Y
B679: AC 12 01        LDY     $0112               ; {hard.workRam+112} current tube shape
B67C: B9 DC BC        LDA     $BCDC,Y             ; {hard.rom+2CDC} first draw-style byte for this shape
B67F: 85 59           STA     $59                 ; {hard.workRam+59}
B681: B9 EC BC        LDA     $BCEC,Y             ; {hard.rom+2CEC} second draw-style byte
B684: 85 5A           STA     $5A                 ; {hard.workRam+5A}
B686: 60              RTS                         

; ---- $B687-$B69A: data ----
B687: 00 10 1F 28 2C 28 1F 10 00 F0 E1 D8 D4 D8 E1 F0
B697: 00 10 1F 28

; Builds slot x's screen position from loc_2df+x and segment base
; loc_3ce/loc_3de (segment loc_2b9+x), interpolating toward the next
; segment via b6fa when loc_2cc+x is negative, then folds deltas (c098),
; lays the header (c765), appends the pair (bd3e), and emits a frame-
; phased template word from $CEC8/$CEC9.
emitInterpolatedSlotVector:
B69B: BD DF 02        LDA     $02DF,X             ; {hard.workRam+2DF} stage the slot's depth
B69E: 85 57           STA     $57                 ; {hard.workRam+57}
B6A0: BC B9 02        LDY     $02B9,X             ; {hard.workRam+2B9} the slot's segment
B6A3: B9 CE 03        LDA     $03CE,Y             ; {hard.workRam+3CE} base X of the segment corner
B6A6: 85 56           STA     $56                 ; {hard.workRam+56}
B6A8: B9 DE 03        LDA     $03DE,Y             ; {hard.workRam+3DE} base Y of the segment corner
B6AB: 85 58           STA     $58                 ; {hard.workRam+58}
B6AD: BD CC 02        LDA     $02CC,X             ; {hard.workRam+2CC} read the phase byte
B6B0: 10 23           BPL     $B6D5               ; {code.loc_b6d5} not mid-flip: use the segment position directly
B6B2: 98              TYA                         
B6B3: 18              CLC                         
B6B4: 69 01           ADC     #$01                ; the next segment, wrapping 0..15
B6B6: 29 0F           AND     #$0F                
B6B8: A8              TAY                         
B6B9: B9 CE 03        LDA     $03CE,Y             ; {hard.workRam+3CE}
B6BC: 38              SEC                         
B6BD: E5 56           SBC     $56                 ; {hard.workRam+56} delta to the next segment's X
B6BF: 20 FA B6        JSR     $B6FA               ; {code.scaleByPhaseFraction} scale it by the flip-phase fraction
B6C2: 18              CLC                         
B6C3: 65 56           ADC     $56                 ; {hard.workRam+56} interpolate the X toward the next segment
B6C5: 85 56           STA     $56                 ; {hard.workRam+56}
B6C7: B9 DE 03        LDA     $03DE,Y             ; {hard.workRam+3DE} delta to the next segment's Y
B6CA: 38              SEC                         
B6CB: E5 58           SBC     $58                 ; {hard.workRam+58}
B6CD: 20 FA B6        JSR     $B6FA               ; {code.scaleByPhaseFraction} scale it by the flip-phase fraction
B6D0: 18              CLC                         
B6D1: 65 58           ADC     $58                 ; {hard.workRam+58} interpolate the Y toward the next segment
B6D3: 85 58           STA     $58                 ; {hard.workRam+58}

loc_b6d5:
B6D5: 20 98 C0        JSR     $C098               ; {code.projectPointThroughMathbox} project the point through the math box
B6D8: A2 61           LDX     #$61                
B6DA: 20 65 C7        JSR     $C765               ; {code.layHeaderAndBuildRecord} lay the 0x61 header and open the record
B6DD: A9 00           LDA     #$00                
B6DF: 85 A9           STA     $A9                 ; {hard.workRam+A9} reset the list offset
B6E1: 20 3E BD        JSR     $BD3E               ; {code.appendNormalizedMantissaExponent} append the normalized mantissa/exponent pair
B6E4: 84 A9           STY     $A9                 ; {hard.workRam+A9} save the appender's exit cursor
B6E6: A5 03           LDA     $03                 ; {hard.workRam+3}
B6E8: 29 03           AND     #$03                
B6EA: 0A              ASL     A                   
B6EB: 18              CLC                         
B6EC: 69 4E           ADC     #$4E                ; pick a frame-phased template word
B6EE: A8              TAY                         
B6EF: BE C9 CE        LDX     $CEC9,Y             ; {hard.rom+3EC9} template word high byte
B6F2: B9 C8 CE        LDA     $CEC8,Y             ; {hard.rom+3EC8} template word low byte
B6F5: A4 A9           LDY     $A9                 ; {hard.workRam+A9}
B6F7: 4C 59 DF        JMP     $DF59               ; {code.emitVectorWordAtOffset} emit the template vector word at the saved offset

; Scales a value by slot x's low-three-bit phase fraction (loc_2cc+x &
; 0x07 into loc_2c) via three LSB-first conditional-add rounds with sign-
; preserving right shifts.
scaleByPhaseFraction:
B6FA: 85 29           STA     $29                 ; {hard.workRam+29} stash the input value
B6FC: BD CC 02        LDA     $02CC,X             ; {hard.workRam+2CC}
B6FF: 29 07           AND     #$07                ; the phase's 3-bit fraction, in eighths
B701: 85 2C           STA     $2C                 ; {hard.workRam+2C}
B703: 86 2B           STX     $2B                 ; {hard.workRam+2B}
B705: A2 02           LDX     #$02                
B707: A9 00           LDA     #$00                

loc_b709:
B709: 46 2C           LSR     $2C                 ; {hard.workRam+2C} shift out the fraction's low bit
B70B: 90 03           BCC     $B710               ; {code.loc_b710} bit clear: add nothing this round
B70D: 18              CLC                         
B70E: 65 29           ADC     $29                 ; {hard.workRam+29} bit set: add the input

loc_b710:
B710: 0A              ASL     A                   ; sign-preserving halve of the accumulator
B711: 08              PHP                         
B712: 6A              ROR     A                   
B713: 28              PLP                         
B714: 6A              ROR     A                   
B715: CA              DEX                         
B716: 10 F1           BPL     $B709               ; {code.loc_b709}
B718: A6 2B           LDX     $2B                 ; {hard.workRam+2B}
B71A: 60              RTS                         

; draw the rim segment for slot x with an animation style: latch loc_9e
; from loc_148's sign (0x04 if negative else 0x00) and a style byte loc_29
; from $B755 indexed by ((loc_148+0x40)&0xff)>>4 (clamped to 0 when >=5),
; then split on loc_283+x's sign into
; buildSlotScreenPoint+emitTubeRimSegmentVectors(loc_29) or
; drawTubeRimSegmentFromCorner(loc_29,loc_2b9+x).
drawStyledSlotRimSegment:
B71B: A9 04           LDA     #$04                
B71D: AC 48 01        LDY     $0148               ; {hard.workRam+148} read the animation accumulator
B720: 30 02           BMI     $B724               ; {code.loc_b724} negative phase sets the run flag
B722: A9 00           LDA     #$00                

loc_b724:
B724: 85 9E           STA     $9E                 ; {hard.workRam+9E} latch the run flag
B726: AD 48 01        LDA     $0148               ; {hard.workRam+148}
B729: 18              CLC                         
B72A: 69 40           ADC     #$40                ; bias the animation accumulator
B72C: 4A              LSR     A                   ; high nibble is the phase index
B72D: 4A              LSR     A                   
B72E: 4A              LSR     A                   
B72F: 4A              LSR     A                   
B730: C9 05           CMP     #$05                ; wrap past the five style phases
B732: 90 02           BCC     $B736               ; {code.loc_b736}
B734: A9 00           LDA     #$00                

loc_b736:
B736: A8              TAY                         
B737: B9 55 B7        LDA     $B755,Y             ; {hard.rom+2755} latch this phase's style byte
B73A: 85 29           STA     $29                 ; {hard.workRam+29}
B73C: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} read this slot's flag byte
B73F: 30 0B           BMI     $B74C               ; {code.loc_b74c} negative slot: compute its screen point
B741: BC B9 02        LDY     $02B9,X             ; {hard.workRam+2B9} the enemy's rim corner
B744: A5 29           LDA     $29                 ; {hard.workRam+29}
B746: 20 A0 BD        JSR     $BDA0               ; {code.drawTubeRimSegmentFromCorner} draw the styled segment from the corner
B749: B8              CLV                         
B74A: 50 08           BVC     $B754               ; {code.loc_b754}

loc_b74c:
B74C: 20 34 B6        JSR     $B634               ; {code.buildSlotScreenPoint} derive the slot's screen point
B74F: A4 29           LDY     $29                 ; {hard.workRam+29}
B751: 20 CB BD        JSR     $BDCB               ; {code.emitTubeRimSegmentVectors} emit the styled segment at the point

loc_b754:
B754: 60              RTS                         

; ---- $B755-$B75A: data ----
B755: 0D 0C 0B 0A 09 09

; emit a shape vector for each of twelve slots (index 0x37 from 0x0b
; down): for each non-empty entry 0x2d3+x seat the shape in 0x57/0x2f,
; read target 0x2ad+x, and emit via seatShapeParamsAndEmit (near value
; 0x08 for x<8, phase-derived for far slots); afterward latch a per-level
; segment colour (0x04/0x0b/0x0c by stage 0x135) into colour RAM 0x808.
drawSlotShapeList:
B75B: A2 0B           LDX     #$0B                ; walk the twelve tube slots, high-to-low
B75D: 86 37           STX     $37                 ; {hard.workRam+37} seed the slot loop index

loc_b75f:
B75F: A6 37           LDX     $37                 ; {hard.workRam+37}
B761: BD D3 02        LDA     $02D3,X             ; {hard.workRam+2D3} read the slot's occupancy/depth byte
B764: F0 1B           BEQ     $B781               ; {code.loc_b781} empty slot, skip it
B766: 85 57           STA     $57                 ; {hard.workRam+57} seat the object depth
B768: 85 2F           STA     $2F                 ; {hard.workRam+2F} carry the depth to the emitter
B76A: E0 08           CPX     #$08                ; near slots (below 8) vs far slots
B76C: BC AD 02        LDY     $02AD,X             ; {hard.workRam+2AD} the slot's target tube segment
B76F: B0 05           BCS     $B776               ; {code.loc_b776} far slot: size pulses with the frame phase
B771: A9 08           LDA     #$08                ; near slot: fixed shape size
B773: B8              CLV                         
B774: 50 08           BVC     $B77E               ; {code.loc_b77e}

loc_b776:
B776: A5 03           LDA     $03                 ; {hard.workRam+3} far slot: read the frame phase counter
B778: 0A              ASL     A                   
B779: 29 06           AND     #$06                
B77B: 18              CLC                         
B77C: 69 20           ADC     #$20                ; build a pulsing size for distant shapes

loc_b77e:
B77E: 20 FD BC        JSR     $BCFD               ; {code.seatShapeParamsAndEmit} seat the params and emit the shape

loc_b781:
B781: C6 37           DEC     $37                 ; {hard.workRam+37}
B783: 10 DA           BPL     $B75F               ; {code.loc_b75f} loop until the index passes 0
B785: A0 04           LDY     #$04                
B787: AD 35 01        LDA     $0135               ; {hard.workRam+135} read the current stage
B78A: C9 06           CMP     #$06                
B78C: 90 08           BCC     $B796               ; {code.loc_b796} below stage 6: rim colour 0x04
B78E: A0 0B           LDY     #$0B                
B790: C9 08           CMP     #$08                
B792: 90 02           BCC     $B796               ; {code.loc_b796} below stage 8: rim colour 0x0b
B794: A0 0C           LDY     #$0C                

loc_b796:
B796: 8C 08 08        STY     $0808               ; {hard.colorRam+8} latch the per-level rim colour into colour RAM
B799: 60              RTS                         

; emit one shape record per active enemy slot (0x37 from 7 down): clear
; 0x9e, and for each non-empty 0x30a+slot seat 0x57 and 0x29(=0x2fa+slot);
; shape 1 draws specially via animateShapeOneVector, else compute a shape
; word from 0x312+slot and 0xb7e5+shape and emit via
; seatShapeParamsAndEmit; finally latch 0x9f into 0x1ff when 0x720 nonzero
; and 0x9f>=0x0d.
drawEnemyShapeList:
B79A: A0 00           LDY     #$00                
B79C: 84 9E           STY     $9E                 ; {hard.workRam+9E} clear the draw scratch
B79E: A2 07           LDX     #$07                ; walk the eight shape-bank slots, high-to-low
B7A0: 86 37           STX     $37                 ; {hard.workRam+37}

loc_b7a2:
B7A2: A6 37           LDX     $37                 ; {hard.workRam+37}
B7A4: BD 0A 03        LDA     $030A,X             ; {hard.workRam+30A} slot's active flag -- also its object depth
B7A7: F0 29           BEQ     $B7D2               ; {code.loc_b7d2} empty slot, skip
B7A9: 85 57           STA     $57                 ; {hard.workRam+57} seat the object depth
B7AB: BD FA 02        LDA     $02FA,X             ; {hard.workRam+2FA} slot's tube coordinate
B7AE: 85 29           STA     $29                 ; {hard.workRam+29}
B7B0: BC 02 03        LDY     $0302,X             ; {hard.workRam+302} slot's shape id
B7B3: C0 01           CPY     #$01                
B7B5: D0 06           BNE     $B7BD               ; {code.loc_b7bd} shape id other than 1
B7B7: 20 EB B7        JSR     $B7EB               ; {code.animateShapeOneVector} shape 1: the special animated draw path
B7BA: B8              CLV                         
B7BB: 50 15           BVC     $B7D2               ; {code.loc_b7d2}

loc_b7bd:
B7BD: BD 12 03        LDA     $0312,X             ; {hard.workRam+312} other shapes: the animation byte
B7C0: 4A              LSR     A                   
B7C1: 29 FE           AND     #$FE                ; animation base, forced even
B7C3: C0 02           CPY     #$02                
B7C5: 90 02           BCC     $B7C9               ; {code.loc_b7c9} shape id below 2 keeps the base
B7C7: A9 00           LDA     #$00                ; shape id 2 or more forces base 0

loc_b7c9:
B7C9: 18              CLC                         
B7CA: 79 E5 B7        ADC     $B7E5,Y             ; {hard.rom+27E5} add the per-shape table offset
B7CD: A4 29           LDY     $29                 ; {hard.workRam+29} the shape's coordinate
B7CF: 20 FD BC        JSR     $BCFD               ; {code.seatShapeParamsAndEmit} seat the params and emit

loc_b7d2:
B7D2: C6 37           DEC     $37                 ; {hard.workRam+37}
B7D4: 10 CC           BPL     $B7A2               ; {code.loc_b7a2} loop until the index passes 0
B7D6: AD 20 07        LDA     $0720               ; {hard.workRam+720} high-level guard
B7D9: F0 09           BEQ     $B7E4               ; {code.loc_b7e4} guard clear, nothing to latch
B7DB: A5 9F           LDA     $9F                 ; {hard.workRam+9F} the current level byte
B7DD: C9 0D           CMP     #$0D                
B7DF: 90 03           BCC     $B7E4               ; {code.loc_b7e4} only levels 0x0d and up are remembered
B7E1: 8D FF 01        STA     $01FF               ; {hard.workRam+1FF} latch the high-level marker

loc_b7e4:
B7E4: 60              RTS                         

; ---- $B7E5-$B7EA: data ----
B7E5: 00 00 5A 58 56 1C

; advance and emit the shape-1 enemy animation: refresh axis params
; loc_56/loc_58 from loc_435/loc_445 at loc_29, run frame updaters
; (projectPointThroughMathbox, layHeaderAndBuildRecord), tick sub-timer
; loc_13c and on wrap advance phase loc_13b and reload loc_13c from
; $B82A+loc_13b, run phase handler dispatchDrawSetup when
; $B83D+loc_13b<0x80, then emit the phase's vector-pair word from
; $CEC8/$CEC9 at ((loc_13b<<1)+0x28)&0xff.
animateShapeOneVector:
B7EB: A4 29           LDY     $29                 ; {hard.workRam+29} the enemy's lane index
B7ED: B9 35 04        LDA     $0435,Y             ; {hard.workRam+435} lane midpoint into the projection point
B7F0: 85 56           STA     $56                 ; {hard.workRam+56}
B7F2: B9 45 04        LDA     $0445,Y             ; {hard.workRam+445} lane midpoint, second axis
B7F5: 85 58           STA     $58                 ; {hard.workRam+58}
B7F7: 20 98 C0        JSR     $C098               ; {code.projectPointThroughMathbox} project the point through the math box
B7FA: A2 61           LDX     #$61                
B7FC: 20 65 C7        JSR     $C765               ; {code.layHeaderAndBuildRecord} lay the record header
B7FF: AE 3B 01        LDX     $013B               ; {hard.workRam+13B} the animation phase
B802: CE 3C 01        DEC     $013C               ; {hard.workRam+13C} age the animation sub-timer
B805: D0 0A           BNE     $B811               ; {code.loc_b811} sub-timer not expired yet
B807: E8              INX                         ; advance the keyframe phase
B808: 8E 3B 01        STX     $013B               ; {hard.workRam+13B}
B80B: BD 2A B8        LDA     $B82A,X             ; {hard.rom+282A} reload the sub-timer from the per-phase duration table
B80E: 8D 3C 01        STA     $013C               ; {hard.workRam+13C}

loc_b811:
B811: BC 3D B8        LDY     $B83D,X             ; {hard.rom+283D} this phase's setup code
B814: 30 03           BMI     $B819               ; {code.loc_b819} 0x80 or more: no setup handler
B816: 20 4E B8        JSR     $B84E               ; {code.dispatchDrawSetup} run the phase's setup handler

loc_b819:
B819: AD 3B 01        LDA     $013B               ; {hard.workRam+13B}
B81C: 0A              ASL     A                   
B81D: 18              CLC                         
B81E: 69 28           ADC     #$28                ; form the template index for this phase
B820: A8              TAY                         
B821: BE C9 CE        LDX     $CEC9,Y             ; {hard.rom+3EC9} fetch the phase's vector-pair word, high
B824: B9 C8 CE        LDA     $CEC8,Y             ; {hard.rom+3EC8} vector-pair word, low
B827: 4C 57 DF        JMP     $DF57               ; {code.emitVectorWord} emit the vector word

; ---- $B82A-$B84D: data ----
B82A: 02 02 02 02 02 04 03 02 01 20 03 03 03 03 03 03
B83A: 03 3B B8 00 02 02 02 02 02 02 02 04 06 FF FF FF
B84A: FF FF FF FF

; computed-jump dispatcher: caller's Y is a byte offset (0,2,4,6)
; selecting one of four draw-setup targets $B85F/$B875/$B888/$B896, and it
; tail-returns that routine's result.
dispatchDrawSetup:
B84E: B9 58 B8        LDA     $B858,Y             ; {hard.rom+2858} push the selected setup routine's address, high
B851: 48              PHA                         
B852: B9 57 B8        LDA     $B857,Y             ; {hard.rom+2857} setup routine address, low
B855: 48              PHA                         
B856: 60              RTS                         ; jump into the chosen setup routine

; ---- $B857-$B85E: data ----
B857: 5E B8 74 B8 87 B8 95 B8

; seed the paired three-entry arrays 0x22-0x24 and 0x809-0x80b with the
; fixed values 0x00, 0x04, 0x0c.
seedTripleArrays:
B85F: A9 0C           LDA     #$0C                
B861: 8D 0B 08        STA     $080B               ; {hard.colorRam+B} colour-RAM triple, entry 2
B864: 85 24           STA     $24                 ; {hard.workRam+24} colour-cycle triple, entry 2
B866: A9 04           LDA     #$04                
B868: 8D 0A 08        STA     $080A               ; {hard.colorRam+A} colour-RAM entry 1
B86B: 85 23           STA     $23                 ; {hard.workRam+23} colour-cycle entry 1
B86D: A9 00           LDA     #$00                
B86F: 85 22           STA     $22                 ; {hard.workRam+22} colour-cycle entry 0
B871: 8D 09 08        STA     $0809               ; {hard.colorRam+9} colour-RAM entry 0
B874: 60              RTS                         

; rotate the three-entry array 0x22-0x24 down by one, threading the
; wrapped value, and mirror each new entry into paired array 0x809-0x80b.
rotateTripleArray:
B875: A4 22           LDY     $22                 ; {hard.workRam+22} capture entry 0 as the wrap-around value
B877: A2 02           LDX     #$02                ; walk the triple, top-down

loc_b879:
B879: B5 22           LDA     $22,X               ; {hard.workRam+22} save the current occupant
B87B: 48              PHA                         
B87C: 94 22           STY     $22,X               ; {hard.workRam+22} drop the carried value into the colour-cycle slot
B87E: 98              TYA                         
B87F: 9D 09 08        STA     $0809,X             ; {hard.colorRam+9} mirror it into visible colour RAM
B882: 68              PLA                         
B883: A8              TAY                         ; the displaced occupant carries to the next slot
B884: CA              DEX                         
B885: 10 F2           BPL     $B879               ; {code.loc_b879}
B887: 60              RTS                         

; rebuild the packed-nibble table via unpackLevelNibbleTables, then seat
; the vector-list tail cursor 0x139=0x7f and 0x13a=0x04.
resetVectorTailCursor:
B888: 20 96 C1        JSR     $C196               ; {code.unpackLevelNibbleTables} rebuild the packed per-level nibble geometry tables
B88B: A9 7F           LDA     #$7F                
B88D: 8D 39 01        STA     $0139               ; {hard.workRam+139} seat the vector-list tail cursor low
B890: A9 04           LDA     #$04                
B892: 8D 3A 01        STA     $013A               ; {hard.workRam+13A} seat the tail cursor high -- cursor sits at 0x047f
B895: 60              RTS                         

; emit a vector-RAM tail record from cursor 0x139/0x13a — low byte to
; 0x2ffc, high byte tagged 0x70 to 0x2ffd, 0xc0 terminator to 0x2fff —
; then step the cursor down by 0x20 with a 16-bit borrow into 0x13a and
; mask the low byte to 0x7f.
emitVectorTailRecord:
B896: AD 39 01        LDA     $0139               ; {hard.workRam+139}
B899: 8D FC 2F        STA     $2FFC               ; {hard.vectorRam+FFC} jump target low = the current tail cursor
B89C: AD 3A 01        LDA     $013A               ; {hard.workRam+13A}
B89F: 09 70           ORA     #$70                ; tag with the vector-generator jump opcode bits
B8A1: 8D FD 2F        STA     $2FFD               ; {hard.vectorRam+FFD} jump target high
B8A4: A9 C0           LDA     #$C0                
B8A6: 8D FF 2F        STA     $2FFF               ; {hard.vectorRam+FFF} halt word that ends the beam scan
B8A9: AD 39 01        LDA     $0139               ; {hard.workRam+139}
B8AC: 38              SEC                         
B8AD: E9 20           SBC     #$20                ; step the cursor down one record
B8AF: 10 05           BPL     $B8B6               ; {code.loc_b8b6}
B8B1: 29 7F           AND     #$7F                
B8B3: CE 3A 01        DEC     $013A               ; {hard.workRam+13A} borrow into the cursor high byte

loc_b8b6:
B8B6: 8D 39 01        STA     $0139               ; {hard.workRam+139} store the advanced tail cursor low
B8B9: 60              RTS                         

; draw the 16-slot moving-object cascade into the display list: reset
; accumulators (loc_6a-loc_6d, loc_202, loc_68/loc_69) with
; loc_5f=0xe0/loc_5b=0xff, cache the base draw-struct pointer from
; selectPointerPair into loc_76/loc_77, lay an opening coord
; (emitCoordinateVectorWord), then count loc_37 from 0x0f down and for
; each active slot (loc_283+x nonzero) load loc_57/loc_56/loc_58 from
; loc_283/loc_263/loc_2a3+x, integrate deltas
; (projectPointThroughMathbox), emit the record body
; (emitCoordDeltaRecord, emitBlankValueRecord, emitObjectPositionVector)
; with pointer-swap shadow passes (swapDrawPointers), and set the slot
; phase into loc_9e; closes by swapping pointers back and finishing the
; base list (emitBlankVectorWordTag70, emitRecordBodyC0).
drawMovingObjectSlots:
B8BA: A9 3F           LDA     #$3F                
B8BC: A2 F2           LDX     #$F2                
B8BE: 20 39 DF        JSR     $DF39               ; {code.emitCoordinateVectorWord} emit the opening framing word
B8C1: A9 00           LDA     #$00                
B8C3: 85 6A           STA     $6A                 ; {hard.workRam+6A} reset the delta integrators
B8C5: 85 6B           STA     $6B                 ; {hard.workRam+6B}
B8C7: 85 6C           STA     $6C                 ; {hard.workRam+6C}
B8C9: 85 6D           STA     $6D                 ; {hard.workRam+6D}
B8CB: 8D 02 02        STA     $0202               ; {hard.workRam+202} clear the player-shot depth
B8CE: 85 68           STA     $68                 ; {hard.workRam+68} clear the x-offset accumulator
B8D0: 85 69           STA     $69                 ; {hard.workRam+69}
B8D2: A9 E0           LDA     #$E0                
B8D4: 85 5F           STA     $5F                 ; {hard.workRam+5F} depth seed high
B8D6: A9 FF           LDA     #$FF                
B8D8: 85 5B           STA     $5B                 ; {hard.workRam+5B} depth seed low
B8DA: 20 67 B9        JSR     $B967               ; {code.selectPointerPair} pick the base draw-struct pointer pair
B8DD: 85 77           STA     $77                 ; {hard.workRam+77} cache it as the alternate cursor high
B8DF: 86 76           STX     $76                 ; {hard.workRam+76} alternate cursor low
B8E1: A2 0F           LDX     #$0F                ; walk the sixteen object slots, top-down
B8E3: 86 37           STX     $37                 ; {hard.workRam+37}

loc_b8e5:
B8E5: A6 37           LDX     $37                 ; {hard.workRam+37}
B8E7: BD 83 02        LDA     $0283,X             ; {hard.workRam+283} slot activity/flag byte
B8EA: F0 49           BEQ     $B935               ; {code.loc_b935} inactive slot, skip
B8EC: 85 57           STA     $57                 ; {hard.workRam+57} the flag doubles as the object depth
B8EE: BD 63 02        LDA     $0263,X             ; {hard.workRam+263} object position, axis 1
B8F1: 85 56           STA     $56                 ; {hard.workRam+56}
B8F3: BD A3 02        LDA     $02A3,X             ; {hard.workRam+2A3} object position, axis 2
B8F6: 85 58           STA     $58                 ; {hard.workRam+58}
B8F8: 20 98 C0        JSR     $C098               ; {code.projectPointThroughMathbox} project the tube position to screen
B8FB: A9 00           LDA     #$00                
B8FD: 85 73           STA     $73                 ; {hard.workRam+73} clear the record header
B8FF: 20 44 B9        JSR     $B944               ; {code.swapDrawPointers} swap to the alternate cursor for the shadow pass
B902: 20 BA C3        JSR     $C3BA               ; {code.emitCoordDeltaRecord} emit the coord-delta record
B905: A9 A0           LDA     #$A0                
B907: 20 6A B5        JSR     $B56A               ; {code.emitBlankValueRecord} emit a blank value record
B90A: 20 44 B9        JSR     $B944               ; {code.swapDrawPointers} swap back to the base cursor
B90D: A2 61           LDX     #$61                
B90F: 20 72 C7        JSR     $C772               ; {code.emitObjectPositionVector} emit the object-position vector
B912: 20 55 B9        JSR     $B955               ; {code.returnConstantTwo} fetch the constant 2
B915: 20 6C DF        JSR     $DF6C               ; {code.emitVectorWordTag70} emit the tag-70 word
B918: A5 37           LDA     $37                 ; {hard.workRam+37}
B91A: 29 07           AND     #$07                ; 8-phase animation index from the slot
B91C: C9 07           CMP     #$07                
B91E: D0 02           BNE     $B922               ; {code.loc_b922}
B920: A9 00           LDA     #$00                ; fold phase 7 to 0

loc_b922:
B922: A8              TAY                         
B923: 84 9E           STY     $9E                 ; {hard.workRam+9E} store the animation phase
B925: A9 08           LDA     #$08                
B927: 20 4C DF        JSR     $DF4C               ; {code.emitTaggedVectorWord} emit the tagged style/phase word
B92A: A9 00           LDA     #$00                
B92C: 20 4A DF        JSR     $DF4A               ; {code.emitVectorWordTag60FromKey} emit the tag-60 word
B92F: 20 67 B9        JSR     $B967               ; {code.selectPointerPair} re-cache the pointer pair
B932: 20 39 DF        JSR     $DF39               ; {code.emitCoordinateVectorWord} lay the next framing word

loc_b935:
B935: C6 37           DEC     $37                 ; {hard.workRam+37}
B937: 10 AC           BPL     $B8E5               ; {code.loc_b8e5} loop until the slot index passes 0
B939: 20 44 B9        JSR     $B944               ; {code.swapDrawPointers} restore the pointer orientation
B93C: A9 01           LDA     #$01                
B93E: 20 6A DF        JSR     $DF6A               ; {code.emitBlankVectorWordTag70} emit the closing blank tag-70 word
B941: 20 09 DF        JSR     $DF09               ; {code.emitRecordBodyC0} emit the C0 record body

; swap the two 16-bit draw pointers 0x74/0x75 and 0x76/0x77 so the shared
; cursor addresses the other structure.
swapDrawPointers:
B944: A6 74           LDX     $74                 ; {hard.workRam+74} exchange the primary and alternate draw cursors
B946: A4 75           LDY     $75                 ; {hard.workRam+75}
B948: A5 76           LDA     $76                 ; {hard.workRam+76}
B94A: 85 74           STA     $74                 ; {hard.workRam+74}
B94C: 86 76           STX     $76                 ; {hard.workRam+76}
B94E: A5 77           LDA     $77                 ; {hard.workRam+77}
B950: 85 75           STA     $75                 ; {hard.workRam+75}
B952: 84 77           STY     $77                 ; {hard.workRam+77}
B954: 60              RTS                         

; register-only leaf that always returns the constant pair A=0x02, Y=0x00
; and touches no memory.
returnConstantTwo:
B955: A5 57           LDA     $57                 ; {hard.workRam+57}
B957: 4A              LSR     A                   
B958: 4A              LSR     A                   
B959: 4A              LSR     A                   
B95A: 4A              LSR     A                   
B95B: A0 00           LDY     #$00                

loc_b95d:
B95D: C8              INY                         
B95E: 4A              LSR     A                   
B95F: D0 FC           BNE     $B95D               ; {code.loc_b95d}
B961: 18              CLC                         
B962: 69 02           ADC     #$02                ; hand back the constant 2 -- the shift loop above always leaves a at 0
B964: A0 00           LDY     #$00                
B966: 60              RTS                         

; select a pointer pair by flag 0x415: zero picks 0xce87/0xce86, nonzero
; picks 0xce6f/0xce6e; returns the pair as (A,X).
selectPointerPair:
B967: AD 15 04        LDA     $0415               ; {hard.workRam+415} read the draw-struct parity flag
B96A: F0 09           BEQ     $B975               ; {code.loc_b975} even parity: the clear pointer
B96C: AD 6F CE        LDA     $CE6F               ; {hard.rom+3E6F} odd parity: the set draw pointer, high
B96F: AE 6E CE        LDX     $CE6E               ; {hard.rom+3E6E} set draw pointer, low
B972: B8              CLV                         
B973: 50 06           BVC     $B97B               ; {code.loc_b97b}

loc_b975:
B975: AD 87 CE        LDA     $CE87               ; {hard.rom+3E87} even parity: the clear draw pointer, high
B978: AE 86 CE        LDX     $CE86               ; {hard.rom+3E86} clear draw pointer, low

loc_b97b:
B97B: 60              RTS                         

; ---- $B97C-$BCFC: data ----
B97C: F0 E7 CF AA 80 56 31 19 10 19 31 56 80 AA CF E7
B98C: F0 F0 F0 B8 80 48 10 10 10 10 10 48 80 B8 F0 F0
B99C: F0 F0 B8 B8 80 48 48 10 10 10 48 48 80 B8 B8 F0
B9AC: EC D5 B1 90 70 4F 2B 14 14 2B 4F 70 90 B1 D5 EC
B9BC: F0 C0 A0 94 6C 60 40 10 10 40 60 6C 94 A0 C0 F0
B9CC: D9 C2 AC 97 80 69 52 3C 27 10 35 5A 80 A6 CA F0
B9DC: EA E0 9C 80 64 20 16 50 16 20 64 80 9C E0 EA B0
B9EC: 10 1E 2C 3A 48 56 64 70 90 9E AC BA C8 D6 E4 F0
B9FC: 10 1E 2D 3C 4B 5A 69 78 87 96 A5 B4 C3 D2 E1 F0
BA0C: 10 10 10 10 16 29 46 69 97 BA D7 EA F0 F0 F0 F0
BA1C: 10 24 30 36 3E 49 5A 75 94 A4 AC BA DA E2 EA F0
BA2C: 80 70 48 20 10 20 48 70 80 90 B8 E0 F0 E0 B8 90
BA3C: DA A4 87 80 79 5C 26 10 10 20 48 80 B8 E0 F0 F0
BA4C: 10 10 30 30 50 50 70 70 90 90 B0 B0 D0 D0 F0 F0
BA5C: B0 80 50 47 18 30 18 47 50 80 B0 B9 E8 D4 E8 B9
BA6C: 10 1E 21 28 3C 55 66 73 8D 9A AB C4 D8 DF E2 F0
BA7C: 80 AA CF E7 F0 E7 CF AA 80 56 31 19 10 19 31 56
BA8C: 80 B8 F0 F0 F0 F0 F0 B8 80 48 10 10 10 10 10 48
BA9C: 80 B8 B8 F0 F0 F0 B8 B8 80 48 48 10 10 10 48 48
BAAC: 94 B0 B8 A7 A7 B8 B0 94 6C 50 48 59 59 48 50 6C
BABC: 96 A3 C5 F0 F0 C5 A3 96 6A 5D 3B 10 10 3B 5D 6A
BACC: 3D 6A 97 C4 F0 C4 97 6A 3D 10 10 10 10 10 10 10
BADC: A0 E0 EA B0 EA E0 A0 80 60 20 16 50 16 20 60 80
BAEC: F0 D0 B0 90 70 50 30 10 10 30 50 70 90 B0 D0 F0
BAFC: 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40
BB0C: F0 CB A6 80 5C 39 20 12 12 20 39 5C 80 A6 CB F0
BB1C: C0 A6 8A 6A 4A 2F 14 24 20 39 59 75 72 90 B0 D0
BB2C: 80 57 48 57 80 A9 BA A9 80 57 48 57 80 A9 BA A9
BB3C: E4 E8 B7 80 B7 E8 E4 B2 7A 47 20 10 20 47 7A B2
BB4C: 90 70 70 50 50 30 30 10 10 30 30 50 50 70 70 90
BB5C: E6 D0 E6 B9 AE 80 52 47 14 30 14 47 52 80 AE B9
BB6C: 7E 6A 51 3A 2C 2C 38 4E 4E 38 2C 2C 3A 51 6A 7E
BB7C: 05 06 07 08 09 0A 0B 0C 0D 0E 0F 00 01 02 03 04
BB8C: 04 04 08 08 08 08 0C 0C 0C 0C 00 00 00 00 04 04
BB9C: 04 08 04 08 08 0C 08 0C 0C 00 0C 00 00 04 00 04
BBAC: 06 07 09 08 07 09 0A 0C 0E 0F 01 00 0F 01 02 04
BBBC: 07 06 05 08 0B 0A 09 0C 0F 0E 0D 00 03 02 01 04
BBCC: 05 05 05 05 0B 0B 0B 0B 0B 00 00 00 00 00 00 05
BBDC: 04 08 0B 05 08 0C 0E 09 0C 00 03 0D 00 04 07 02
BBEC: 0D 0D 0D 0D 0D 0D 0D 00 03 03 03 03 03 03 03 00
BBFC: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
BC0C: 0C 0C 0C 0D 0E 0F 0F 00 01 01 02 03 04 04 04 00
BC1C: 0E 0D 0C 0D 0D 0D 01 0F 02 03 03 00 03 03 03 00
BC2C: 0B 09 07 05 03 01 0F 0D 0D 0F 01 03 05 07 09 0B
BC3C: 08 0B 0C 04 05 08 0B 0C 0D 0E 0F 01 02 03 04 05
BC4C: 0C 00 0C 00 0C 00 0C 00 04 00 04 00 04 00 04 00
BC5C: 0A 06 0C 08 0E 0A 00 0C 02 0E 04 00 06 02 08 04
BC6C: 0E 0C 0D 0E 00 02 02 00 0E 0E 00 02 03 04 02 00
BC7C: 00 01 02 03 04 05 06 07 0D 09 08 0C 0E 0F 0A 0B
BC8C: 18 1C 18 0F 18 18 18 18 0A 18 10 0F 18 0C 14 0A
BC9C: 50 50 50 68 50 50 68 B0 A0 50 90 80 20 B0 60 A0
BCAC: 40 20 40 80 40 40 70 60 00 20 40 00 A0 40 40 00
BCBC: FF FF FF FF FF FF FF 00 01 FF 00 00 FE 01 FF 01
BCCC: 00 00 00 00 00 00 00 FF FF FF FF 00 00 FF 00 FF
BCDC: 00 00 60 40 00 00 48 40 50 28 50 00 00 50 00 40
BCEC: 04 04 03 04 04 04 03 04 05 04 04 04 04 04 04 05
BCFC: 3E

; Stashes the value byte into loc_55 and loads loc_435+y/loc_445+y into
; loc_56/loc_58, then emits the coloured shape vector (bd09).
seatShapeParamsAndEmit:
BCFD: 85 55           STA     $55                 ; {hard.workRam+55} seat the draw style/colour selector
BCFF: B9 35 04        LDA     $0435,Y             ; {hard.workRam+435} segment midpoint into the projection point
BD02: 85 56           STA     $56                 ; {hard.workRam+56}
BD04: B9 45 04        LDA     $0445,Y             ; {hard.workRam+445} segment midpoint, second axis
BD07: 85 58           STA     $58                 ; {hard.workRam+58}

; Folds deltas (c098), lays the header (c765), appends the pair (bd3e),
; clamps a colour/intensity nibble from loc_78 (XOR 0x07, doubled, floored
; to 0x0a, high nibble) OR'd with 0x60, and emits a template word keyed by
; loc_55.
emitColoredShapeVector:
BD09: 20 98 C0        JSR     $C098               ; {code.projectPointThroughMathbox} fold the coordinate deltas through the math box
BD0C: A2 61           LDX     #$61                
BD0E: 20 65 C7        JSR     $C765               ; {code.layHeaderAndBuildRecord} lay the fixed record header
BD11: A9 00           LDA     #$00                
BD13: 85 A9           STA     $A9                 ; {hard.workRam+A9} reset the cursor run length
BD15: 20 3E BD        JSR     $BD3E               ; {code.appendNormalizedMantissaExponent} append the mantissa/exponent size pair
BD18: A5 78           LDA     $78                 ; {hard.workRam+78} the interpolated colour attribute
BD1A: 49 07           EOR     #$07                ; invert the low colour bits
BD1C: 0A              ASL     A                   
BD1D: C9 0A           CMP     #$0A                
BD1F: B0 02           BCS     $BD23               ; {code.loc_bd23}
BD21: A9 0A           LDA     #$0A                ; floor the intensity to a visible minimum

loc_bd23:
BD23: 0A              ASL     A                   ; seat the colour in the high nibble
BD24: 0A              ASL     A                   
BD25: 0A              ASL     A                   
BD26: 0A              ASL     A                   
BD27: 91 74           STA     ($74),Y             ; {hard.workRam+74} write the colour/intensity byte
BD29: C8              INY                         
BD2A: A9 60           LDA     #$60                
BD2C: 91 74           STA     ($74),Y             ; {hard.workRam+74} write the companion attribute byte
BD2E: C8              INY                         
BD2F: 84 A9           STY     $A9                 ; {hard.workRam+A9} record the advanced run length
BD31: A4 55           LDY     $55                 ; {hard.workRam+55} the style selector indexes the template tables
BD33: BE C9 CE        LDX     $CEC9,Y             ; {hard.rom+3EC9} entry glyph word, high
BD36: B9 C8 CE        LDA     $CEC8,Y             ; {hard.rom+3EC8} entry glyph word, low
BD39: A4 A9           LDY     $A9                 ; {hard.workRam+A9}
BD3B: 4C 59 DF        JMP     $DF59               ; {code.emitVectorWordAtOffset} emit the templated glyph word

; Appends a (mantissa, exponent) pair for loc_57: trivial (1,0) when
; loc_57<0x10, else drives the math box on loc_57-loc_5f/loc_5b and
; normalizes loc_79 into shift count loc_78; writes the pair (exponent
; tagged 0x70) at cursor loc_a9.
appendNormalizedMantissaExponent:
BD3E: A5 57           LDA     $57                 ; {hard.workRam+57} the object depth
BD40: C9 10           CMP     #$10                
BD42: 90 48           BCC     $BD8C               ; {code.loc_bd8c} near object: draw at full size
BD44: 38              SEC                         
BD45: E5 5F           SBC     $5F                 ; {hard.workRam+5F} depth minus the seed -- a 16-bit difference
BD47: 8D 95 60        STA     $6095               ; {hard.mathboxGo+15} into the math-box operand low
BD4A: A9 00           LDA     #$00                
BD4C: E5 5B           SBC     $5B                 ; {hard.workRam+5B}
BD4E: 8D 96 60        STA     $6096               ; {hard.mathboxGo+16} math-box operand high
BD51: A9 18           LDA     #$18                
BD53: 8D 8C 60        STA     $608C               ; {hard.mathboxGo+C} iteration count
BD56: A5 A0           LDA     $A0                 ; {hard.workRam+A0}
BD58: 8D 8E 60        STA     $608E               ; {hard.mathboxGo+E} divisor
BD5B: 8D 94 60        STA     $6094               ; {hard.mathboxGo+14} issue the divide

loc_bd5e:
BD5E: 2C 40 60        BIT     $6040               ; {hard.mathboxStatus / earomControl} poll the math-box busy bit
BD61: 30 FB           BMI     $BD5E               ; {code.loc_bd5e} spin until the divide is done
BD63: AD 60 60        LDA     $6060               ; {hard.mathboxLo} read the result low
BD66: 85 79           STA     $79                 ; {hard.workRam+79}
BD68: AD 70 60        LDA     $6070               ; {hard.mathboxHi} read the result high
BD6B: 85 7A           STA     $7A                 ; {hard.workRam+7A}
BD6D: A2 0F           LDX     #$0F                
BD6F: 8E 8C 60        STX     $608C               ; {hard.mathboxGo+C} reload the iteration count
BD72: 38              SEC                         
BD73: E9 01           SBC     #$01                
BD75: D0 02           BNE     $BD79               ; {code.loc_bd79}
BD77: A9 01           LDA     #$01                ; clamp the high byte to at least 1

loc_bd79:
BD79: A2 00           LDX     #$00                

loc_bd7b:
BD7B: E8              INX                         ; normalize: count the shifts
BD7C: 06 79           ASL     $79                 ; {hard.workRam+79}
BD7E: 2A              ROL     A                   
BD7F: 90 FA           BCC     $BD7B               ; {code.loc_bd7b} until a 1 rolls out of the top
BD81: 4A              LSR     A                   
BD82: 49 7F           EOR     #$7F                ; two's-complement fold into the exponent
BD84: 18              CLC                         
BD85: 69 01           ADC     #$01                
BD87: A8              TAY                         
BD88: 8A              TXA                         
BD89: B8              CLV                         
BD8A: 50 04           BVC     $BD90               ; {code.loc_bd90}

loc_bd8c:
BD8C: A9 01           LDA     #$01                ; near path: mantissa 1
BD8E: A0 00           LDY     #$00                ; exponent 0 -- full size

loc_bd90:
BD90: 85 78           STA     $78                 ; {hard.workRam+78} store the mantissa
BD92: 48              PHA                         
BD93: 98              TYA                         
BD94: A4 A9           LDY     $A9                 ; {hard.workRam+A9}
BD96: 91 74           STA     ($74),Y             ; {hard.workRam+74} write the exponent byte
BD98: C8              INY                         
BD99: 68              PLA                         
BD9A: 09 70           ORA     #$70                ; tag the mantissa with 0x70
BD9C: 91 74           STA     ($74),Y             ; {hard.workRam+74} write the mantissa byte
BD9E: C8              INY                         
BD9F: 60              RTS                         

; draw one tube-rim segment: fetch the source corner (loc_3ce+y/loc_3de+y
; into loc_56/loc_58, loc_2f from loc_57) and the next corner ((y+1)&0x0f)
; into loc_2e/loc_30, seed run counters loc_59=0 and loc_5a=4, then fall
; into emitTubeRimSegmentVectors to emit the segment's four-byte vector
; records.
drawTubeRimSegmentFromCorner:
BDA0: 85 36           STA     $36                 ; {hard.workRam+36} stash the style/shape selector
BDA2: B9 CE 03        LDA     $03CE,Y             ; {hard.workRam+3CE} first endpoint from source corner
BDA5: 85 56           STA     $56                 ; {hard.workRam+56}
BDA7: B9 DE 03        LDA     $03DE,Y             ; {hard.workRam+3DE} first endpoint, second axis
BDAA: 85 58           STA     $58                 ; {hard.workRam+58}
BDAC: A5 57           LDA     $57                 ; {hard.workRam+57}
BDAE: 85 2F           STA     $2F                 ; {hard.workRam+2F} carry the depth to the second endpoint
BDB0: 98              TYA                         
BDB1: 18              CLC                         
BDB2: 69 01           ADC     #$01                
BDB4: 29 0F           AND     #$0F                ; next corner, wrapping the 16-corner ring
BDB6: AA              TAX                         
BDB7: BD CE 03        LDA     $03CE,X             ; {hard.workRam+3CE} second endpoint
BDBA: 85 2E           STA     $2E                 ; {hard.workRam+2E}
BDBC: BD DE 03        LDA     $03DE,X             ; {hard.workRam+3DE} second endpoint, second axis
BDBF: 85 30           STA     $30                 ; {hard.workRam+30}
BDC1: A9 00           LDA     #$00                
BDC3: 85 59           STA     $59                 ; {hard.workRam+59} seed the clamp tally
BDC5: A9 04           LDA     #$04                
BDC7: 85 5A           STA     $5A                 ; {hard.workRam+5A} seed the run size to 4
BDC9: A4 36           LDY     $36                 ; {hard.workRam+36}

; emit the tube-rim segment's vector records: gate (unless loc_5b bit7,
; return when loc_57<loc_5f), read record count loc_99 and cursor loc_38
; from $BFB6/$BFC4, project both endpoints through the math box
; (projectPointThroughMathbox), form two clamped signed deltas
; (loc_79/loc_9b, loc_89/loc_9d), expand the fivefold spread, then write
; loc_99 four-byte records into (loc_74)+loc_a9 and close with
; advanceDisplayCursor.
emitTubeRimSegmentVectors:
BDCB: A5 5B           LDA     $5B                 ; {hard.workRam+5B} the depth-force flag
BDCD: 30 07           BMI     $BDD6               ; {code.loc_bdd6} bit 7 forces the segment to draw
BDCF: A5 57           LDA     $57                 ; {hard.workRam+57} object depth
BDD1: C5 5F           CMP     $5F                 ; {hard.workRam+5F}
BDD3: B0 01           BCS     $BDD6               ; {code.loc_bdd6}
BDD5: 60              RTS                         ; too near the rim, skip the segment

loc_bdd6:
BDD6: B9 B6 BF        LDA     $BFB6,Y             ; {hard.rom+2FB6} this corner's record count
BDD9: 85 99           STA     $99                 ; {hard.workRam+99}
BDDB: B9 C4 BF        LDA     $BFC4,Y             ; {hard.rom+2FC4} start of this corner's packed table
BDDE: 85 38           STA     $38                 ; {hard.workRam+38}
BDE0: A4 9E           LDY     $9E                 ; {hard.workRam+9E}
BDE2: A9 08           LDA     #$08                
BDE4: 20 4C DF        JSR     $DF4C               ; {code.emitTaggedVectorWord} emit the run's colour/style word
BDE7: 20 98 C0        JSR     $C098               ; {code.projectPointThroughMathbox} project the first endpoint
BDEA: A2 61           LDX     #$61                
BDEC: 20 65 C7        JSR     $C765               ; {code.layHeaderAndBuildRecord} lay its header record
BDEF: A5 2E           LDA     $2E                 ; {hard.workRam+2E} move in the second endpoint
BDF1: 85 56           STA     $56                 ; {hard.workRam+56}
BDF3: A5 2F           LDA     $2F                 ; {hard.workRam+2F}
BDF5: 85 57           STA     $57                 ; {hard.workRam+57}
BDF7: A5 30           LDA     $30                 ; {hard.workRam+30}
BDF9: 85 58           STA     $58                 ; {hard.workRam+58}
BDFB: 20 98 C0        JSR     $C098               ; {code.projectPointThroughMathbox} project the second endpoint
BDFE: A4 59           LDY     $59                 ; {hard.workRam+59}
BE00: A5 5A           LDA     $5A                 ; {hard.workRam+5A}
BE02: 20 6C DF        JSR     $DF6C               ; {code.emitVectorWordTag70} emit the run's tag-70 word
BE05: A5 61           LDA     $61                 ; {hard.workRam+61} delta 1: projected Y minus previous Y
BE07: 38              SEC                         
BE08: E5 6A           SBC     $6A                 ; {hard.workRam+6A}
BE0A: 85 79           STA     $79                 ; {hard.workRam+79} the segment's direction magnitude
BE0C: A5 62           LDA     $62                 ; {hard.workRam+62}
BE0E: E5 6B           SBC     $6B                 ; {hard.workRam+6B}
BE10: 85 9B           STA     $9B                 ; {hard.workRam+9B} its sign high byte
BE12: 30 09           BMI     $BE1D               ; {code.loc_be1d}
BE14: F0 04           BEQ     $BE1A               ; {code.loc_be1a}
BE16: A9 FF           LDA     #$FF                ; clamp the magnitude on overflow
BE18: 85 79           STA     $79                 ; {hard.workRam+79}

loc_be1a:
BE1A: B8              CLV                         
BE1B: 50 16           BVC     $BE33               ; {code.loc_be33}

loc_be1d:
BE1D: C9 FF           CMP     #$FF                
BE1F: F0 05           BEQ     $BE26               ; {code.loc_be26}
BE21: A9 FF           LDA     #$FF                
BE23: B8              CLV                         
BE24: 50 0B           BVC     $BE31               ; {code.loc_be31}

loc_be26:
BE26: A5 79           LDA     $79                 ; {hard.workRam+79}
BE28: 49 FF           EOR     #$FF                
BE2A: 18              CLC                         
BE2B: 69 01           ADC     #$01                
BE2D: 90 02           BCC     $BE31               ; {code.loc_be31}
BE2F: A9 FF           LDA     #$FF                

loc_be31:
BE31: 85 79           STA     $79                 ; {hard.workRam+79}

loc_be33:
BE33: A5 63           LDA     $63                 ; {hard.workRam+63} delta 2: projected X minus previous X
BE35: 38              SEC                         
BE36: E5 6C           SBC     $6C                 ; {hard.workRam+6C}
BE38: 85 89           STA     $89                 ; {hard.workRam+89} the segment's direction magnitude
BE3A: A5 64           LDA     $64                 ; {hard.workRam+64}
BE3C: E5 6D           SBC     $6D                 ; {hard.workRam+6D}
BE3E: 85 9D           STA     $9D                 ; {hard.workRam+9D} its sign high byte
BE40: 30 09           BMI     $BE4B               ; {code.loc_be4b}
BE42: F0 04           BEQ     $BE48               ; {code.loc_be48}
BE44: A9 FF           LDA     #$FF                ; clamp on overflow
BE46: 85 89           STA     $89                 ; {hard.workRam+89}

loc_be48:
BE48: B8              CLV                         
BE49: 50 12           BVC     $BE5D               ; {code.loc_be5d}

loc_be4b:
BE4B: C9 FF           CMP     #$FF                
BE4D: F0 05           BEQ     $BE54               ; {code.loc_be54}
BE4F: A9 FF           LDA     #$FF                
BE51: B8              CLV                         
BE52: 50 07           BVC     $BE5B               ; {code.loc_be5b}

loc_be54:
BE54: A5 89           LDA     $89                 ; {hard.workRam+89}
BE56: 49 FF           EOR     #$FF                
BE58: 18              CLC                         
BE59: 69 01           ADC     #$01                

loc_be5b:
BE5B: 85 89           STA     $89                 ; {hard.workRam+89}

loc_be5d:
BE5D: A9 00           LDA     #$00                
BE5F: 85 82           STA     $82                 ; {hard.workRam+82}
BE61: 85 92           STA     $92                 ; {hard.workRam+92}
BE63: A5 79           LDA     $79                 ; {hard.workRam+79} scale the Y-delta into the x1..x7 offset ladder
BE65: 0A              ASL     A                   
BE66: 26 82           ROL     $82                 ; {hard.workRam+82}
BE68: 85 7A           STA     $7A                 ; {hard.workRam+7A}
BE6A: 0A              ASL     A                   
BE6B: 85 7C           STA     $7C                 ; {hard.workRam+7C}
BE6D: A5 82           LDA     $82                 ; {hard.workRam+82}
BE6F: 2A              ROL     A                   
BE70: 85 84           STA     $84                 ; {hard.workRam+84}
BE72: A5 7C           LDA     $7C                 ; {hard.workRam+7C}
BE74: 65 79           ADC     $79                 ; {hard.workRam+79}
BE76: 85 7D           STA     $7D                 ; {hard.workRam+7D}
BE78: A5 84           LDA     $84                 ; {hard.workRam+84}
BE7A: 69 00           ADC     #$00                
BE7C: 85 85           STA     $85                 ; {hard.workRam+85}
BE7E: A5 7A           LDA     $7A                 ; {hard.workRam+7A}
BE80: 65 79           ADC     $79                 ; {hard.workRam+79}
BE82: 85 7B           STA     $7B                 ; {hard.workRam+7B}
BE84: A5 82           LDA     $82                 ; {hard.workRam+82}
BE86: 69 00           ADC     #$00                
BE88: 85 83           STA     $83                 ; {hard.workRam+83}
BE8A: 85 86           STA     $86                 ; {hard.workRam+86}
BE8C: A5 7B           LDA     $7B                 ; {hard.workRam+7B}
BE8E: 0A              ASL     A                   
BE8F: 85 7E           STA     $7E                 ; {hard.workRam+7E}
BE91: 26 86           ROL     $86                 ; {hard.workRam+86}
BE93: 65 79           ADC     $79                 ; {hard.workRam+79}
BE95: 85 7F           STA     $7F                 ; {hard.workRam+7F}
BE97: A5 86           LDA     $86                 ; {hard.workRam+86}
BE99: 69 00           ADC     #$00                
BE9B: 85 87           STA     $87                 ; {hard.workRam+87}
BE9D: A5 89           LDA     $89                 ; {hard.workRam+89} scale the X-delta into the x1..x7 offset ladder
BE9F: 0A              ASL     A                   
BEA0: 26 92           ROL     $92                 ; {hard.workRam+92}
BEA2: 85 8A           STA     $8A                 ; {hard.workRam+8A}
BEA4: 0A              ASL     A                   
BEA5: 85 8C           STA     $8C                 ; {hard.workRam+8C}
BEA7: A5 92           LDA     $92                 ; {hard.workRam+92}
BEA9: 2A              ROL     A                   
BEAA: 85 94           STA     $94                 ; {hard.workRam+94}
BEAC: A5 8C           LDA     $8C                 ; {hard.workRam+8C}
BEAE: 65 89           ADC     $89                 ; {hard.workRam+89}
BEB0: 85 8D           STA     $8D                 ; {hard.workRam+8D}
BEB2: A5 94           LDA     $94                 ; {hard.workRam+94}
BEB4: 69 00           ADC     #$00                
BEB6: 85 95           STA     $95                 ; {hard.workRam+95}
BEB8: A5 8A           LDA     $8A                 ; {hard.workRam+8A}
BEBA: 65 89           ADC     $89                 ; {hard.workRam+89}
BEBC: 85 8B           STA     $8B                 ; {hard.workRam+8B}
BEBE: A5 92           LDA     $92                 ; {hard.workRam+92}
BEC0: 69 00           ADC     #$00                
BEC2: 85 93           STA     $93                 ; {hard.workRam+93}
BEC4: 85 96           STA     $96                 ; {hard.workRam+96}
BEC6: A5 8B           LDA     $8B                 ; {hard.workRam+8B}
BEC8: 0A              ASL     A                   
BEC9: 85 8E           STA     $8E                 ; {hard.workRam+8E}
BECB: 26 96           ROL     $96                 ; {hard.workRam+96}
BECD: 65 89           ADC     $89                 ; {hard.workRam+89}
BECF: 85 8F           STA     $8F                 ; {hard.workRam+8F}
BED1: A5 96           LDA     $96                 ; {hard.workRam+96}
BED3: 69 00           ADC     #$00                
BED5: 85 97           STA     $97                 ; {hard.workRam+97}
BED7: A0 00           LDY     #$00                
BED9: 84 A9           STY     $A9                 ; {hard.workRam+A9}

loc_bedb:
BEDB: A4 38           LDY     $38                 ; {hard.workRam+38} walk the packed corner table
BEDD: B9 D3 BF        LDA     $BFD3,Y             ; {hard.rom+2FD3} the record's vector-generator header
BEE0: C9 01           CMP     #$01                
BEE2: D0 02           BNE     $BEE6               ; {code.loc_bee6}
BEE4: A9 C0           LDA     #$C0                ; header 1 is shorthand for the 0xc0 draw-mode

loc_bee6:
BEE6: 85 73           STA     $73                 ; {hard.workRam+73}
BEE8: B9 D2 BF        LDA     $BFD2,Y             ; {hard.rom+2FD2} the packed sign/index selector byte
BEEB: 85 2D           STA     $2D                 ; {hard.workRam+2D}
BEED: C8              INY                         
BEEE: C8              INY                         
BEEF: 84 38           STY     $38                 ; {hard.workRam+38}
BEF1: AA              TAX                         
BEF2: 29 07           AND     #$07                ; low 3 bits index the spread for the point
BEF4: A8              TAY                         
BEF5: 8A              TXA                         
BEF6: 0A              ASL     A                   
BEF7: 85 2B           STA     $2B                 ; {hard.workRam+2B} doubled copy carries the x sign into bit 7
BEF9: 4A              LSR     A                   
BEFA: 4A              LSR     A                   
BEFB: 4A              LSR     A                   
BEFC: 4A              LSR     A                   
BEFD: 29 07           AND     #$07                ; next 3 bits index the cross offset
BEFF: AA              TAX                         
BF00: A5 2B           LDA     $2B                 ; {hard.workRam+2B}
BF02: 45 9B           EOR     $9B                 ; {hard.workRam+9B} combine the packed sign with the direction sign
BF04: 30 0B           BMI     $BF11               ; {code.loc_bf11} negate the offset when the signs differ
BF06: B9 78 00        LDA     $0078,Y             ; {hard.workRam+78}
BF09: 85 61           STA     $61                 ; {hard.workRam+61}
BF0B: B9 80 00        LDA     $0080,Y             ; {hard.workRam+80}
BF0E: B8              CLV                         
BF0F: 50 11           BVC     $BF22               ; {code.loc_bf22}

loc_bf11:
BF11: B9 78 00        LDA     $0078,Y             ; {hard.workRam+78}
BF14: 49 FF           EOR     #$FF                
BF16: 18              CLC                         
BF17: 69 01           ADC     #$01                
BF19: 85 61           STA     $61                 ; {hard.workRam+61}
BF1B: B9 80 00        LDA     $0080,Y             ; {hard.workRam+80}
BF1E: 49 FF           EOR     #$FF                
BF20: 69 00           ADC     #$00                

loc_bf22:
BF22: 85 62           STA     $62                 ; {hard.workRam+62}
BF24: A5 2D           LDA     $2D                 ; {hard.workRam+2D}
BF26: 45 9D           EOR     $9D                 ; {hard.workRam+9D} combine with the second direction sign
BF28: 10 0E           BPL     $BF38               ; {code.loc_bf38}
BF2A: B5 88           LDA     $88,X               ; {hard.workRam+88}
BF2C: 18              CLC                         
BF2D: 65 61           ADC     $61                 ; {hard.workRam+61}
BF2F: 85 61           STA     $61                 ; {hard.workRam+61}
BF31: B5 90           LDA     $90,X               ; {hard.workRam+90}
BF33: 65 62           ADC     $62                 ; {hard.workRam+62}
BF35: B8              CLV                         
BF36: 50 0B           BVC     $BF43               ; {code.loc_bf43}

loc_bf38:
BF38: A5 61           LDA     $61                 ; {hard.workRam+61}
BF3A: 38              SEC                         
BF3B: F5 88           SBC     $88,X               ; {hard.workRam+88}
BF3D: 85 61           STA     $61                 ; {hard.workRam+61}
BF3F: A5 62           LDA     $62                 ; {hard.workRam+62}
BF41: F5 90           SBC     $90,X               ; {hard.workRam+90}

loc_bf43:
BF43: 85 62           STA     $62                 ; {hard.workRam+62}
BF45: A5 2B           LDA     $2B                 ; {hard.workRam+2B}
BF47: 45 9D           EOR     $9D                 ; {hard.workRam+9D}
BF49: 30 0B           BMI     $BF56               ; {code.loc_bf56}
BF4B: B9 88 00        LDA     $0088,Y             ; {hard.workRam+88}
BF4E: 85 63           STA     $63                 ; {hard.workRam+63}
BF50: B9 90 00        LDA     $0090,Y             ; {hard.workRam+90}
BF53: B8              CLV                         
BF54: 50 11           BVC     $BF67               ; {code.loc_bf67}

loc_bf56:
BF56: B9 88 00        LDA     $0088,Y             ; {hard.workRam+88}
BF59: 49 FF           EOR     #$FF                
BF5B: 18              CLC                         
BF5C: 69 01           ADC     #$01                
BF5E: 85 63           STA     $63                 ; {hard.workRam+63}
BF60: B9 90 00        LDA     $0090,Y             ; {hard.workRam+90}
BF63: 49 FF           EOR     #$FF                
BF65: 69 00           ADC     #$00                

loc_bf67:
BF67: 85 64           STA     $64                 ; {hard.workRam+64}
BF69: A5 2D           LDA     $2D                 ; {hard.workRam+2D}
BF6B: 45 9B           EOR     $9B                 ; {hard.workRam+9B}
BF6D: 10 0E           BPL     $BF7D               ; {code.loc_bf7d}
BF6F: A5 63           LDA     $63                 ; {hard.workRam+63}
BF71: 38              SEC                         
BF72: F5 78           SBC     $78,X               ; {hard.workRam+78}
BF74: 85 63           STA     $63                 ; {hard.workRam+63}
BF76: A5 64           LDA     $64                 ; {hard.workRam+64}
BF78: F5 80           SBC     $80,X               ; {hard.workRam+80}
BF7A: B8              CLV                         
BF7B: 50 0B           BVC     $BF88               ; {code.loc_bf88}

loc_bf7d:
BF7D: A5 63           LDA     $63                 ; {hard.workRam+63}
BF7F: 18              CLC                         
BF80: 75 78           ADC     $78,X               ; {hard.workRam+78}
BF82: 85 63           STA     $63                 ; {hard.workRam+63}
BF84: A5 64           LDA     $64                 ; {hard.workRam+64}
BF86: 75 80           ADC     $80,X               ; {hard.workRam+80}

loc_bf88:
BF88: 85 64           STA     $64                 ; {hard.workRam+64}
BF8A: A4 A9           LDY     $A9                 ; {hard.workRam+A9}
BF8C: A5 63           LDA     $63                 ; {hard.workRam+63}
BF8E: 91 74           STA     ($74),Y             ; {hard.workRam+74} write the record's X low
BF90: C8              INY                         
BF91: A5 64           LDA     $64                 ; {hard.workRam+64}
BF93: 29 1F           AND     #$1F                ; clamp X high to the low 5 bits
BF95: 91 74           STA     ($74),Y             ; {hard.workRam+74}
BF97: C8              INY                         
BF98: A5 61           LDA     $61                 ; {hard.workRam+61}
BF9A: 91 74           STA     ($74),Y             ; {hard.workRam+74} write the record's Y low
BF9C: C8              INY                         
BF9D: A5 62           LDA     $62                 ; {hard.workRam+62}
BF9F: 29 1F           AND     #$1F                
BFA1: 05 73           ORA     $73                 ; {hard.workRam+73} OR in the record header
BFA3: 91 74           STA     ($74),Y             ; {hard.workRam+74} write the record's Y high
BFA5: C8              INY                         
BFA6: 84 A9           STY     $A9                 ; {hard.workRam+A9}
BFA8: C6 99           DEC     $99                 ; {hard.workRam+99} one record done
BFAA: F0 03           BEQ     $BFAF               ; {code.loc_bfaf}
BFAC: 4C DB BE        JMP     $BEDB               ; {code.loc_bedb} loop over the corner's records

loc_bfaf:
BFAF: A4 A9           LDY     $A9                 ; {hard.workRam+A9}
BFB1: 88              DEY                         
BFB2: 4C 5F DF        JMP     $DF5F               ; {code.advanceDisplayCursor} advance the display cursor past the run

; ---- $BFB5-$C097: data ----
BFB5: 08 08 08 08 08 08 08 08 08 09 06 07 07 04 02 00
BFC5: 10 20 30 40 50 60 70 80 92 9E AC BA C2 0C 01 8C
BFD5: 01 4A 01 09 01 CB 01 4B 01 89 01 CA 01 90 01 8A
BFE5: 01 23 01 DB 01 41 01 10 01 0A 01 CB 01 91 01 17
BFF5: 01 4B 01 8A 01 CE 01 08 01 0A 01 CB 01 92 01 16
C005: 01 4B 01 8A 01 CD 01 49 01 0A 01 CB 01 93 01 15
C015: 01 4B 01 8A 01 CC 01 4A 01 0A 01 CB 01 95 01 13
C025: 01 4B 01 8A 01 CA 01 4C 01 0A 01 CB 01 96 01 12
C035: 01 4B 01 8A 01 C9 01 4D 01 0A 01 CB 01 97 01 11
C045: 01 4B 01 8A 01 88 01 4E 01 0A 01 CB 01 0B 00 A3
C055: 01 0A 01 10 01 4B 01 8A 01 90 01 41 01 5B 01 9A
C065: 01 31 01 B1 01 31 01 B1 01 1A 01 01 00 91 01 21
C075: 01 A1 01 21 01 A1 01 11 01 01 00 89 01 11 01 91
C085: 01 11 01 91 01 09 01 01 00 8A 01 12 01 8A 01 01
C095: 00 06 01

; Projects one tube-space point into a screen-coordinate pair: forms
; clamped signed deltas from
; loc_57/loc_5f/loc_5b/loc_58/loc_60/loc_56/loc_5e into the math box, then
; folds offset pairs loc_68/loc_69 and loc_66/loc_67 into accumulators
; loc_63/64 and loc_61/62 with saturation.
projectPointThroughMathbox:
C098: A5 57           LDA     $57                 ; {hard.workRam+57} load the object depth (Z)
C09A: 38              SEC                         
C09B: E5 5F           SBC     $5F                 ; {hard.workRam+5F} subtract the reference depth -- form the depth delta
C09D: 8D 95 60        STA     $6095               ; {hard.mathboxGo+15} feed the math-box divisor low byte
C0A0: A9 00           LDA     #$00                
C0A2: E5 5B           SBC     $5B                 ; {hard.workRam+5B} borrow through the depth guard byte
C0A4: 8D 96 60        STA     $6096               ; {hard.mathboxGo+16} feed the math-box divisor high byte
C0A7: 10 0A           BPL     $C0B3               ; {code.loc_c0b3} skip the clamp when the divisor stayed non-negative
C0A9: A9 00           LDA     #$00                
C0AB: 8D 96 60        STA     $6096               ; {hard.mathboxGo+16} clamp the divisor high byte to zero
C0AE: A9 01           LDA     #$01                
C0B0: 8D 95 60        STA     $6095               ; {hard.mathboxGo+15} floor the divisor low byte at 1 -- never divide by zero

loc_c0b3:
C0B3: A5 58           LDA     $58                 ; {hard.workRam+58} load the point X
C0B5: C5 60           CMP     $60                 ; {hard.workRam+60} compare against the X reference
C0B7: 90 07           BCC     $C0C0               ; {code.loc_c0c0}
C0B9: E5 60           SBC     $60                 ; {hard.workRam+60} X minus reference -- positive branch
C0BB: A2 00           LDX     #$00                ; mark the X delta positive
C0BD: B8              CLV                         
C0BE: 50 07           BVC     $C0C7               ; {code.loc_c0c7}

loc_c0c0:
C0C0: A5 60           LDA     $60                 ; {hard.workRam+60}
C0C2: 38              SEC                         
C0C3: E5 58           SBC     $58                 ; {hard.workRam+58} reference minus X -- negative branch
C0C5: A2 FF           LDX     #$FF                ; mark the X delta negative

loc_c0c7:
C0C7: 8D 8E 60        STA     $608E               ; {hard.mathboxGo+E} feed the X magnitude as the math-box operand
C0CA: 8D 94 60        STA     $6094               ; {hard.mathboxGo+14} trigger the divide for the X projection
C0CD: 86 33           STX     $33                 ; {hard.workRam+33} stash the X sign
C0CF: A5 56           LDA     $56                 ; {hard.workRam+56} load the point Y
C0D1: C5 5E           CMP     $5E                 ; {hard.workRam+5E} compare against the Y reference
C0D3: 90 07           BCC     $C0DC               ; {code.loc_c0dc}
C0D5: E5 5E           SBC     $5E                 ; {hard.workRam+5E} Y minus reference -- positive branch
C0D7: A2 00           LDX     #$00                
C0D9: B8              CLV                         
C0DA: 50 07           BVC     $C0E3               ; {code.loc_c0e3}

loc_c0dc:
C0DC: A5 5E           LDA     $5E                 ; {hard.workRam+5E}
C0DE: 38              SEC                         
C0DF: E5 56           SBC     $56                 ; {hard.workRam+56} reference minus Y -- negative branch
C0E1: A2 FF           LDX     #$FF                

loc_c0e3:
C0E3: 85 32           STA     $32                 ; {hard.workRam+32} stash the Y magnitude
C0E5: 86 34           STX     $34                 ; {hard.workRam+34} stash the Y sign

loc_c0e7:
C0E7: 2C 40 60        BIT     $6040               ; {hard.mathboxStatus / earomControl} read the math-box busy status
C0EA: 30 FB           BMI     $C0E7               ; {code.loc_c0e7} spin while the math box is busy
C0EC: AD 60 60        LDA     $6060               ; {hard.mathboxLo} read the math-box result low byte
C0EF: 85 63           STA     $63                 ; {hard.workRam+63} into the projected X accumulator low
C0F1: AD 70 60        LDA     $6070               ; {hard.mathboxHi} read the math-box result high byte
C0F4: 85 64           STA     $64                 ; {hard.workRam+64} into the projected X accumulator high
C0F6: A5 32           LDA     $32                 ; {hard.workRam+32} reload the Y magnitude
C0F8: 8D 8E 60        STA     $608E               ; {hard.mathboxGo+E} feed it as the math-box operand
C0FB: 8D 94 60        STA     $6094               ; {hard.mathboxGo+14} trigger the divide for the Y projection
C0FE: A5 33           LDA     $33                 ; {hard.workRam+33} test the X sign
C100: 30 18           BMI     $C11A               ; {code.loc_c11a} branch to the subtract path on a negative sign
C102: A5 63           LDA     $63                 ; {hard.workRam+63}
C104: 18              CLC                         
C105: 65 68           ADC     $68                 ; {hard.workRam+68} add the X offset low into the projected X
C107: 85 63           STA     $63                 ; {hard.workRam+63}
C109: A5 64           LDA     $64                 ; {hard.workRam+64}
C10B: 65 69           ADC     $69                 ; {hard.workRam+69} add the X offset high with carry
C10D: 50 06           BVC     $C115               ; {code.loc_c115} branch past the saturation clamp on no overflow
C10F: A9 FF           LDA     #$FF                
C111: 85 63           STA     $63                 ; {hard.workRam+63}
C113: A9 7F           LDA     #$7F                ; saturate the projected X to positive maximum

loc_c115:
C115: 85 64           STA     $64                 ; {hard.workRam+64}
C117: B8              CLV                         
C118: 50 15           BVC     $C12F               ; {code.loc_c12f}

loc_c11a:
C11A: A5 68           LDA     $68                 ; {hard.workRam+68}
C11C: 38              SEC                         
C11D: E5 63           SBC     $63                 ; {hard.workRam+63} offset minus projected X -- negative-sign path
C11F: 85 63           STA     $63                 ; {hard.workRam+63}
C121: A5 69           LDA     $69                 ; {hard.workRam+69}
C123: E5 64           SBC     $64                 ; {hard.workRam+64} subtract the projected-X high with borrow
C125: 50 06           BVC     $C12D               ; {code.loc_c12d} branch past the clamp on no overflow
C127: A9 00           LDA     #$00                
C129: 85 63           STA     $63                 ; {hard.workRam+63}
C12B: A9 80           LDA     #$80                ; saturate the projected X to negative maximum

loc_c12d:
C12D: 85 64           STA     $64                 ; {hard.workRam+64}

loc_c12f:
C12F: 2C 40 60        BIT     $6040               ; {hard.mathboxStatus / earomControl} read the math-box busy status
C132: 30 FB           BMI     $C12F               ; {code.loc_c12f} spin while the math box is busy
C134: AD 60 60        LDA     $6060               ; {hard.mathboxLo} read the math-box result low byte
C137: 85 61           STA     $61                 ; {hard.workRam+61} into the projected Y accumulator low
C139: AD 70 60        LDA     $6070               ; {hard.mathboxHi} read the math-box result high byte
C13C: 85 62           STA     $62                 ; {hard.workRam+62} into the projected Y accumulator high
C13E: A6 34           LDX     $34                 ; {hard.workRam+34} test the Y sign
C140: 30 16           BMI     $C158               ; {code.loc_c158} branch to the subtract path on a negative sign
C142: A5 61           LDA     $61                 ; {hard.workRam+61}
C144: 18              CLC                         
C145: 65 66           ADC     $66                 ; {hard.workRam+66} add the Y offset low into the projected Y
C147: 85 61           STA     $61                 ; {hard.workRam+61}
C149: A5 62           LDA     $62                 ; {hard.workRam+62}
C14B: 65 67           ADC     $67                 ; {hard.workRam+67} add the Y offset high with carry
C14D: 50 06           BVC     $C155               ; {code.loc_c155}
C14F: A9 FF           LDA     #$FF                
C151: 85 61           STA     $61                 ; {hard.workRam+61}
C153: A9 7F           LDA     #$7F                ; saturate the projected Y to positive maximum

loc_c155:
C155: 85 62           STA     $62                 ; {hard.workRam+62}
C157: 60              RTS                         

loc_c158:
C158: A5 66           LDA     $66                 ; {hard.workRam+66}
C15A: 38              SEC                         
C15B: E5 61           SBC     $61                 ; {hard.workRam+61} offset minus projected Y -- negative-sign path
C15D: 85 61           STA     $61                 ; {hard.workRam+61}
C15F: A5 67           LDA     $67                 ; {hard.workRam+67}
C161: E5 62           SBC     $62                 ; {hard.workRam+62}
C163: 50 06           BVC     $C16B               ; {code.loc_c16b}
C165: A9 00           LDA     #$00                
C167: 85 61           STA     $61                 ; {hard.workRam+61}
C169: A9 80           LDA     #$80                ; saturate the projected Y to negative maximum

loc_c16b:
C16B: 85 62           STA     $62                 ; {hard.workRam+62}
C16D: 60              RTS                         

; build the current level's full layout: prime working flags (0x5e=0x80,
; 0x114=0xff), build the tube lane coordinates via buildTubeLaneCoords,
; clear 0x5800 only when mode trigger 0x133 was already zero then force
; 0x133=0, mirror header bytes 0xcec6/0xcec7 into display registers
; 0x2000/0x2001, and inline the 0xc1fd nibble unpack into 0x19/0x800 and
; 0x21/0x808.
buildLevelLayout:
C16E: 20 13 AA        JSR     $AA13               ; {code.stageTextLineWithCount} stage the level's text line into the vector buffer
C171: A9 80           LDA     #$80                
C173: 85 5E           STA     $5E                 ; {hard.workRam+5E} seed the projection Y reference
C175: A9 FF           LDA     #$FF                
C177: 8D 14 01        STA     $0114               ; {hard.workRam+114} mark the display dirty for a full redraw
C17A: 20 35 C2        JSR     $C235               ; {code.buildTubeLaneCoords} build the tube lane coordinates
C17D: AD 33 01        LDA     $0133               ; {hard.workRam+133} test the one-shot level-layout trigger
C180: D0 03           BNE     $C185               ; {code.loc_c185}
C182: 8D 00 58        STA     $5800               ; {hard.avgReset} strobe the vector-generator reset when the trigger was already clear

loc_c185:
C185: A9 00           LDA     #$00                
C187: 8D 33 01        STA     $0133               ; {hard.workRam+133} force the one-shot layout trigger clear
C18A: AD C6 CE        LDA     $CEC6               ; {hard.rom+3EC6} load the first level display-list head word
C18D: 8D 00 20        STA     $2000               ; {hard.vectorRam} latch it into the vector-list header low
C190: AD C7 CE        LDA     $CEC7               ; {hard.rom+3EC7} load the second head word
C193: 8D 01 20        STA     $2001               ; {hard.vectorRam+1} latch it into the vector-list header high

; expand the packed ROM level table 0xc1fd into the working nibble tables:
; mask selector 0x9f with 0x70 clamped to 0x5f, form read index
; (sel>>1)|0x07, and for y=7..0 write each packed byte's low nibble into
; 0x19+y and display mirror 0x800+y and its high nibble into 0x21+y and
; mirror 0x808+y.
unpackLevelNibbleTables:
C196: A5 9F           LDA     $9F                 ; {hard.workRam+9F} load the level selector
C198: 29 70           AND     #$70                ; mask the selector bits
C19A: C9 5F           CMP     #$5F                
C19C: 90 02           BCC     $C1A0               ; {code.loc_c1a0}
C19E: A9 5F           LDA     #$5F                ; clamp the selector to 0x5f

loc_c1a0:
C1A0: 4A              LSR     A                   ; halve the selector
C1A1: 09 07           ORA     #$07                ; form the packed-table read index
C1A3: AA              TAX                         
C1A4: A0 07           LDY     #$07                

loc_c1a6:
C1A6: BD FD C1        LDA     $C1FD,X             ; {hard.rom+31FD} read a packed level-layout byte
C1A9: 29 0F           AND     #$0F                ; take the low nibble
C1AB: 99 19 00        STA     $0019,Y             ; {hard.workRam+19} write it into the working nibble table
C1AE: 99 00 08        STA     $0800,Y             ; {hard.colorRam} mirror it into color RAM
C1B1: BD FD C1        LDA     $C1FD,X             ; {hard.rom+31FD} re-read the packed byte
C1B4: 4A              LSR     A                   
C1B5: 4A              LSR     A                   
C1B6: 4A              LSR     A                   
C1B7: 4A              LSR     A                   
C1B8: 99 21 00        STA     $0021,Y             ; {hard.workRam+21} write the high nibble into the second nibble table
C1BB: 99 08 08        STA     $0808,Y             ; {hard.colorRam+8} mirror it into color RAM
C1BE: CA              DEX                         
C1BF: 88              DEY                         
C1C0: 10 E4           BPL     $C1A6               ; {code.loc_c1a6} loop over the eight table entries
C1C2: 60              RTS                         

; clear the working state before a tube-projection run: zero the zero-page
; scratch cells 0x78/0x80/0x81/0x88/0x90/0x91 and the math-coprocessor
; input block 0x6080/0x6081/0x6083/0x6084/0x6085/0x6086/0x6087/0x6089/0x60
; 8d/0x608e/0x608f/0x6090, then write 0x0f into the control latch 0x608c
; to arm the coprocessor.
resetMathboxInputs:
C1C3: A9 00           LDA     #$00                ; clear the zero-page projection scratch cells
C1C5: 85 81           STA     $81                 ; {hard.workRam+81}
C1C7: 85 91           STA     $91                 ; {hard.workRam+91}
C1C9: 85 80           STA     $80                 ; {hard.workRam+80}
C1CB: 85 78           STA     $78                 ; {hard.workRam+78}
C1CD: 85 90           STA     $90                 ; {hard.workRam+90}
C1CF: 85 88           STA     $88                 ; {hard.workRam+88}
C1D1: A9 00           LDA     #$00                
C1D3: 8D 80 60        STA     $6080               ; {hard.mathboxGo} zero the math-box coprocessor input ports
C1D6: 8D 81 60        STA     $6081               ; {hard.mathboxGo+1}
C1D9: 8D 84 60        STA     $6084               ; {hard.mathboxGo+4}
C1DC: 8D 85 60        STA     $6085               ; {hard.mathboxGo+5}
C1DF: 8D 86 60        STA     $6086               ; {hard.mathboxGo+6}
C1E2: 8D 87 60        STA     $6087               ; {hard.mathboxGo+7}
C1E5: 8D 89 60        STA     $6089               ; {hard.mathboxGo+9}
C1E8: 8D 83 60        STA     $6083               ; {hard.mathboxGo+3}
C1EB: 8D 8D 60        STA     $608D               ; {hard.mathboxGo+D}
C1EE: 8D 8E 60        STA     $608E               ; {hard.mathboxGo+E}
C1F1: 8D 8F 60        STA     $608F               ; {hard.mathboxGo+F}
C1F4: 8D 90 60        STA     $6090               ; {hard.mathboxGo+10}
C1F7: A9 0F           LDA     #$0F                
C1F9: 8D 8C 60        STA     $608C               ; {hard.mathboxGo+C} load step count 0x0f to arm the math box
C1FC: 60              RTS                         

; ---- $C1FD-$C234: data ----
C1FD: 00 04 08 0C C3 07 0B 0B 00 07 0B 08 44 03 0C 0C
C20D: 00 0B 03 07 C8 0C 04 04 00 0B 08 07 C4 0C 03 03
C21D: 00 04 08 0C C3 07 0F 0B 00 0C 08 04 C3 0B 07 07
C22D: 06 03 01 04 00 05 05 05

; lay out the current level's tube: reduce table byte 0x46+0x3d through
; resolveShapeTableIndex to get shape row y (0x112), derive span cells
; (negated 0xbc8c+y into 0x5f/0x5d, 0x10-neg into 0xa0, 0x5b=0xff,
; 0x60=0xbc9c+y, 0x111=0xbccc+y), copy or shift-right the offset pair
; 0x68/0x69 (scale into 0x121) by mode 0x2, clear 0x66/0x67/0x10f/0x110
; and set 0x113=0x2c, then seed the per-lane vertex arrays
; 0x3ce/0x3de/0x3ee from ROM vertex tables 0xb97c/0xba7c/0xbb7c (clearing
; 0x31a/0x33a/0x39a) and fill midpoint arrays 0x435/0x445 by rounding-
; averaging adjacent lanes.
buildTubeLaneCoords:
C235: A6 3D           LDX     $3D                 ; {hard.workRam+3D} index the player's progress slot
C237: B5 46           LDA     $46,X               ; {hard.workRam+46} read the per-slot level value
C239: 20 E8 C2        JSR     $C2E8               ; {code.resolveShapeTableIndex} reduce it to a shape-table index
C23C: 48              PHA                         
C23D: AC 12 01        LDY     $0112               ; {hard.workRam+112}
C240: B9 8C BC        LDA     $BC8C,Y             ; {hard.rom+2C8C} read the per-shape tube-depth parameter
C243: 49 FF           EOR     #$FF                ; negate the depth
C245: 18              CLC                         
C246: 69 01           ADC     #$01                
C248: 85 5F           STA     $5F                 ; {hard.workRam+5F} into the depth high byte
C24A: 85 5D           STA     $5D                 ; {hard.workRam+5D} and into the depth target
C24C: A9 10           LDA     #$10                
C24E: 38              SEC                         
C24F: E5 5F           SBC     $5F                 ; {hard.workRam+5F} form 0x10 minus the depth into the span cell
C251: 85 A0           STA     $A0                 ; {hard.workRam+A0}
C253: A9 FF           LDA     #$FF                
C255: 85 5B           STA     $5B                 ; {hard.workRam+5B} set the depth-low guard to 0xff
C257: B9 9C BC        LDA     $BC9C,Y             ; {hard.rom+2C9C} read the per-shape X reference
C25A: 85 60           STA     $60                 ; {hard.workRam+60} into the projection X reference
C25C: B9 CC BC        LDA     $BCCC,Y             ; {hard.rom+2CCC} read the per-shape level gate flag
C25F: 8D 11 01        STA     $0111               ; {hard.workRam+111} into the tube-geometry flag
C262: A5 02           LDA     $02                 ; {hard.workRam+2} load the pending game mode
C264: C9 1E           CMP     #$1E                
C266: D0 0D           BNE     $C275               ; {code.loc_c275} branch unless the pending mode is 0x1e
C268: B9 AC BC        LDA     $BCAC,Y             ; {hard.rom+2CAC} copy the per-shape offset-pair low
C26B: 85 68           STA     $68                 ; {hard.workRam+68} into the X offset low
C26D: B9 BC BC        LDA     $BCBC,Y             ; {hard.rom+2CBC} copy the per-shape offset-pair high
C270: 85 69           STA     $69                 ; {hard.workRam+69} into the X offset high
C272: B8              CLV                         
C273: 50 18           BVC     $C28D               ; {code.loc_c28d}

loc_c275:
C275: B9 AC BC        LDA     $BCAC,Y             ; {hard.rom+2CAC} offset-pair low minus current -- geometry scale
C278: 38              SEC                         
C279: E5 68           SBC     $68                 ; {hard.workRam+68}
C27B: 8D 21 01        STA     $0121               ; {hard.workRam+121} store the geometry scale low byte
C27E: B9 BC BC        LDA     $BCBC,Y             ; {hard.rom+2CBC}
C281: ED 69 00        SBC     $0069               ; {hard.workRam+69} offset-pair high minus current
C284: A2 03           LDX     #$03                

loc_c286:
C286: 4A              LSR     A                   ; shift the 16-bit scale right by four
C287: 6E 21 01        ROR     $0121               ; {hard.workRam+121}
C28A: CA              DEX                         
C28B: 10 F9           BPL     $C286               ; {code.loc_c286}

loc_c28d:
C28D: A9 00           LDA     #$00                
C28F: 85 66           STA     $66                 ; {hard.workRam+66} clear the Y offset low
C291: 85 67           STA     $67                 ; {hard.workRam+67} clear the Y offset high
C293: A9 00           LDA     #$00                
C295: 8D 0F 01        STA     $010F               ; {hard.workRam+10F}
C298: 8D 10 01        STA     $0110               ; {hard.workRam+110}
C29B: A9 2C           LDA     #$2C                
C29D: 8D 13 01        STA     $0113               ; {hard.workRam+113} seed the record-count cell at 0x2c
C2A0: 68              PLA                         ; restore the packed shape index
C2A1: A8              TAY                         
C2A2: A2 0F           LDX     #$0F                

loc_c2a4:
C2A4: B9 7C B9        LDA     $B97C,Y             ; {hard.rom+297C} read the ROM lane vertex X
C2A7: 9D CE 03        STA     $03CE,X             ; {hard.workRam+3CE} into the working lane base X
C2AA: B9 7C BA        LDA     $BA7C,Y             ; {hard.rom+2A7C} read the ROM lane vertex Y
C2AD: 9D DE 03        STA     $03DE,X             ; {hard.workRam+3DE} into the working lane base Y
C2B0: A9 00           LDA     #$00                
C2B2: 9D 1A 03        STA     $031A,X             ; {hard.workRam+31A} clear the per-column plane-A value
C2B5: 9D 3A 03        STA     $033A,X             ; {hard.workRam+33A} clear the per-column plane-B value
C2B8: 9D 9A 03        STA     $039A,X             ; {hard.workRam+39A} clear the per-lane target flag
C2BB: B9 7C BB        LDA     $BB7C,Y             ; {hard.rom+2B7C} read the ROM ring-heading seed
C2BE: 9D EE 03        STA     $03EE,X             ; {hard.workRam+3EE} into the segment direction table
C2C1: 88              DEY                         
C2C2: CA              DEX                         
C2C3: 10 DF           BPL     $C2A4               ; {code.loc_c2a4} loop over the sixteen lanes
C2C5: A0 00           LDY     #$00                
C2C7: A2 0F           LDX     #$0F                

loc_c2c9:
C2C9: B9 CE 03        LDA     $03CE,Y             ; {hard.workRam+3CE}
C2CC: 38              SEC                         
C2CD: 7D CE 03        ADC     $03CE,X             ; {hard.workRam+3CE} sum adjacent lanes' X
C2D0: 6A              ROR     A                   ; rounding-average into the midpoint X
C2D1: 9D 35 04        STA     $0435,X             ; {hard.workRam+435} store the lane midpoint X
C2D4: B9 DE 03        LDA     $03DE,Y             ; {hard.workRam+3DE}
C2D7: 38              SEC                         
C2D8: 7D DE 03        ADC     $03DE,X             ; {hard.workRam+3DE} sum adjacent lanes' Y
C2DB: 6A              ROR     A                   ; rounding-average into the midpoint Y
C2DC: 9D 45 04        STA     $0445,X             ; {hard.workRam+445} store the lane midpoint Y
C2DF: 88              DEY                         
C2E0: 10 02           BPL     $C2E4               ; {code.loc_c2e4}
C2E2: A0 0F           LDY     #$0F                ; wrap the second cursor back to the top lane

loc_c2e4:
C2E4: CA              DEX                         
C2E5: 10 E2           BPL     $C2C9               ; {code.loc_c2c9} loop the midpoint fill
C2E7: 60              RTS                         

; reduce an input byte into the level/shape table index: values >= 0x62
; are swapped for the POKEY random byte 0x60ca AND 0x5f, the value is
; split into quotient (>>4) and remainder (&0x0f), the remainder indexes
; ROM table 0xbc7c whose entry is stored to shape-index cell 0x112 and
; returned packed into the high nibble with the low nibble forced to 0x0f
; (quotient/remainder in X/Y).
resolveShapeTableIndex:
C2E8: A2 00           LDX     #$00                
C2EA: C9 62           CMP     #$62                ; pass values under 0x62 straight through
C2EC: 90 05           BCC     $C2F3               ; {code.loc_c2f3}
C2EE: AD CA 60        LDA     $60CA               ; {hard.pokey1+A} otherwise pull the POKEY random byte
C2F1: 29 5F           AND     #$5F                ; mask it to range

loc_c2f3:
C2F3: C9 10           CMP     #$10                

loc_c2f5:
C2F5: 90 04           BCC     $C2FB               ; {code.loc_c2fb}
C2F7: E8              INX                         ; bump the quotient
C2F8: 38              SEC                         
C2F9: E9 10           SBC     #$10                ; subtract 0x10

loc_c2fb:
C2FB: C9 10           CMP     #$10                
C2FD: B0 F6           BCS     $C2F5               ; {code.loc_c2f5} loop -- quotient is the value shifted right four, A the remainder
C2FF: A8              TAY                         
C300: B9 7C BC        LDA     $BC7C,Y             ; {hard.rom+2C7C} map the remainder through the ROM shape table
C303: 8D 12 01        STA     $0112               ; {hard.workRam+112} store the shape/level index
C306: 0A              ASL     A                   
C307: 0A              ASL     A                   
C308: 0A              ASL     A                   
C309: 0A              ASL     A                   
C30A: 09 0F           ORA     #$0F                ; force the low nibble to 0x0f
C30C: 60              RTS                         

; first-time rim-counter setup: when loc_110==0 seed loc_110/loc_10f
; through the projection integrator projectAllLanesThroughMathbox (nudging
; the low counter via snapCoordUpToReference when it lags at index 0x0f),
; always emit a header (emitBlankVectorWordTag70, loc_9e=0x06), return
; unless both counters live and loc_113!=0, then clear the record slots
; two-at-a-time via drawFramedCounterSlot and draw each counter's record
; set with drawGatedRecordLoop.
initAndDrawRimDepthCounters:
C30D: AD 10 01        LDA     $0110               ; {hard.workRam+110} test whether the rim counter is already live
C310: D0 27           BNE     $C339               ; {code.loc_c339} skip the first-time setup when it is
C312: A9 F0           LDA     #$F0                
C314: 85 57           STA     $57                 ; {hard.workRam+57} seed the object depth at the far wall
C316: A2 4F           LDX     #$4F                
C318: 20 73 C4        JSR     $C473               ; {code.projectAllLanesThroughMathbox} project all lanes -- returns the clamp count
C31B: 8D 10 01        STA     $0110               ; {hard.workRam+110} store it as the rim counter
C31E: F0 03           BEQ     $C323               ; {code.loc_c323}
C320: 8D 0F 01        STA     $010F               ; {hard.workRam+10F} mirror it into the second counter

loc_c323:
C323: AD 0F 01        LDA     $010F               ; {hard.workRam+10F}
C326: D0 11           BNE     $C339               ; {code.loc_c339}
C328: A9 10           LDA     #$10                
C32A: 85 57           STA     $57                 ; {hard.workRam+57} seed the object depth at the near rim
C32C: 20 53 C4        JSR     $C453               ; {code.snapCoordUpToReference} snap the depth up to reference
C32F: A5 57           LDA     $57                 ; {hard.workRam+57}
C331: A2 0F           LDX     #$0F                
C333: 20 73 C4        JSR     $C473               ; {code.projectAllLanesThroughMathbox} project the lanes again
C336: 8D 0F 01        STA     $010F               ; {hard.workRam+10F} store the near counter

loc_c339:
C339: A9 01           LDA     #$01                
C33B: 20 6A DF        JSR     $DF6A               ; {code.emitBlankVectorWordTag70} emit a blank leading vector word
C33E: A0 06           LDY     #$06                
C340: 84 9E           STY     $9E                 ; {hard.workRam+9E} select color mode 6
C342: AE 10 01        LDX     $0110               ; {hard.workRam+110} load the rim counter
C345: F0 01           BEQ     $C348               ; {code.loc_c348}
C347: 60              RTS                         ; bail when the counter is zero

loc_c348:
C348: AE 13 01        LDX     $0113               ; {hard.workRam+113} load the record-count cell
C34B: D0 01           BNE     $C34E               ; {code.loc_c34e}
C34D: 60              RTS                         ; bail when it is zero

loc_c34e:
C34E: A2 0F           LDX     #$0F                

loc_c350:
C350: A9 C0           LDA     #$C0                
C352: 20 EE C3        JSR     $C3EE               ; {code.drawFramedCounterSlot} clear a framed counter slot pair
C355: CA              DEX                         
C356: 10 F8           BPL     $C350               ; {code.loc_c350} loop over sixteen slots
C358: A0 06           LDY     #$06                
C35A: 84 9E           STY     $9E                 ; {hard.workRam+9E} select color mode 6
C35C: A9 08           LDA     #$08                
C35E: 20 4C DF        JSR     $DF4C               ; {code.emitTaggedVectorWord} emit a tagged vector word
C361: A0 4F           LDY     #$4F                
C363: AD 10 01        LDA     $0110               ; {hard.workRam+110} load the far rim counter
C366: 20 6E C3        JSR     $C36E               ; {code.drawGatedRecordLoop} draw its record set
C369: A0 0F           LDY     #$0F                
C36B: AD 0F 01        LDA     $010F               ; {hard.workRam+10F} load the near rim counter

; Returns when gate A is nonzero; else seats loc_61-64 from
; loc_32a/loc_31a/loc_34a/loc_33a at loc_37, emits the header (c772), and
; draws one record per pass over 0x0f passes (0x0e when loc_111 is set),
; bumping the index by 0x10 on low-nibble wrap.
drawGatedRecordLoop:
C36E: D0 49           BNE     $C3B9               ; {code.loc_c3b9} return when the gate byte is nonzero
C370: 84 37           STY     $37                 ; {hard.workRam+37} seat the slot loop index
C372: B9 2A 03        LDA     $032A,Y             ; {hard.workRam+32A} load the column plane-A sub into the projected Y low
C375: 85 61           STA     $61                 ; {hard.workRam+61}
C377: B9 1A 03        LDA     $031A,Y             ; {hard.workRam+31A} load the plane-A value into the projected Y high
C37A: 85 62           STA     $62                 ; {hard.workRam+62}
C37C: B9 4A 03        LDA     $034A,Y             ; {hard.workRam+34A} load the plane-B sub into the projected X low
C37F: 85 63           STA     $63                 ; {hard.workRam+63}
C381: B9 3A 03        LDA     $033A,Y             ; {hard.workRam+33A} load the plane-B value into the projected X high
C384: 85 64           STA     $64                 ; {hard.workRam+64}
C386: A2 61           LDX     #$61                
C388: 20 72 C7        JSR     $C772               ; {code.emitObjectPositionVector} emit the object's position vector
C38B: A5 74           LDA     $74                 ; {hard.workRam+74}
C38D: 85 B0           STA     $B0                 ; {hard.workRam+B0} cache the draw cursor low
C38F: A5 75           LDA     $75                 ; {hard.workRam+75}
C391: 85 B1           STA     $B1                 ; {hard.workRam+B1} cache the draw cursor high
C393: A2 0F           LDX     #$0F                
C395: AD 11 01        LDA     $0111               ; {hard.workRam+111} test the tube-geometry flag
C398: F0 01           BEQ     $C39B               ; {code.loc_c39b}
C39A: CA              DEX                         ; drop to fifteen passes when the flag is set

loc_c39b:
C39B: A9 C0           LDA     #$C0                
C39D: 85 73           STA     $73                 ; {hard.workRam+73} set the record header to 0xc0
C39F: 86 38           STX     $38                 ; {hard.workRam+38}

loc_c3a1:
C3A1: C6 37           DEC     $37                 ; {hard.workRam+37} step the slot index back one
C3A3: A5 37           LDA     $37                 ; {hard.workRam+37}
C3A5: 29 0F           AND     #$0F                
C3A7: C9 0F           CMP     #$0F                
C3A9: D0 07           BNE     $C3B2               ; {code.loc_c3b2}
C3AB: A5 37           LDA     $37                 ; {hard.workRam+37}
C3AD: 18              CLC                         
C3AE: 69 10           ADC     #$10                ; wrap the index up by 0x10 on low-nibble underflow
C3B0: 85 37           STA     $37                 ; {hard.workRam+37}

loc_c3b2:
C3B2: 20 23 C4        JSR     $C423               ; {code.emitProjectedSlotRecord} emit the projected slot record
C3B5: C6 38           DEC     $38                 ; {hard.workRam+38}
C3B7: 10 E8           BPL     $C3A1               ; {code.loc_c3a1} loop the passes

loc_c3b9:
C3B9: 60              RTS                         

; Forms two 16-bit differences of loc_61/loc_63 minus previous
; loc_6a/loc_6c into delta slots loc_6e-loc_71, emits the record, latches
; current into loc_6a-loc_6d, and sets loc_73=0xc0.
emitCoordDeltaRecord:
C3BA: A5 61           LDA     $61                 ; {hard.workRam+61}
C3BC: 38              SEC                         
C3BD: E5 6A           SBC     $6A                 ; {hard.workRam+6A} projected Y low minus previous -- delta low
C3BF: 85 6E           STA     $6E                 ; {hard.workRam+6E} store the Y delta low
C3C1: A5 62           LDA     $62                 ; {hard.workRam+62}
C3C3: E5 6B           SBC     $6B                 ; {hard.workRam+6B} subtract the previous Y high
C3C5: 85 6F           STA     $6F                 ; {hard.workRam+6F} store the Y delta high
C3C7: A5 63           LDA     $63                 ; {hard.workRam+63}
C3C9: 38              SEC                         
C3CA: E5 6C           SBC     $6C                 ; {hard.workRam+6C} projected X low minus previous -- delta low
C3CC: 85 70           STA     $70                 ; {hard.workRam+70} store the X delta low
C3CE: A5 64           LDA     $64                 ; {hard.workRam+64}
C3D0: E5 6D           SBC     $6D                 ; {hard.workRam+6D} subtract the previous X high
C3D2: 85 71           STA     $71                 ; {hard.workRam+71} store the X delta high
C3D4: A2 6E           LDX     #$6E                
C3D6: 20 92 DF        JSR     $DF92               ; {code.emitCoordinateRecord} emit the coordinate delta record
C3D9: A5 61           LDA     $61                 ; {hard.workRam+61}
C3DB: 85 6A           STA     $6A                 ; {hard.workRam+6A} latch the current Y low as previous
C3DD: A5 62           LDA     $62                 ; {hard.workRam+62}
C3DF: 85 6B           STA     $6B                 ; {hard.workRam+6B}
C3E1: A5 63           LDA     $63                 ; {hard.workRam+63}
C3E3: 85 6C           STA     $6C                 ; {hard.workRam+6C} latch the current X low as previous
C3E5: A5 64           LDA     $64                 ; {hard.workRam+64}
C3E7: 85 6D           STA     $6D                 ; {hard.workRam+6D}
C3E9: A9 C0           LDA     #$C0                
C3EB: 85 73           STA     $73                 ; {hard.workRam+73} reset the record header to 0xc0
C3ED: 60              RTS                         

; draw a framed counter element in two passes: emit slot loc_37 with
; colour loc_73 live ($C43C/$C423), step loc_37 back one and re-emit
; uncoloured, restore the colour and close the frame ($C3BA); return the
; stepped-back index.
drawFramedCounterSlot:
C3EE: 86 37           STX     $37                 ; {hard.workRam+37} seat the slot index
C3F0: 48              PHA                         ; save the color header
C3F1: A4 9E           LDY     $9E                 ; {hard.workRam+9E}
C3F3: A9 08           LDA     #$08                
C3F5: 20 4C DF        JSR     $DF4C               ; {code.emitTaggedVectorWord} emit a tagged vector word
C3F8: 20 3C C4        JSR     $C43C               ; {code.loadSlotCoordBlock} load the slot's coordinate block
C3FB: A2 61           LDX     #$61                
C3FD: 20 72 C7        JSR     $C772               ; {code.emitObjectPositionVector} emit the object's position vector
C400: 68              PLA                         
C401: 85 73           STA     $73                 ; {hard.workRam+73} restore the live color header
C403: 48              PHA                         
C404: 20 23 C4        JSR     $C423               ; {code.emitProjectedSlotRecord} emit the colored slot record
C407: C6 37           DEC     $37                 ; {hard.workRam+37} step the slot back one
C409: A4 9E           LDY     $9E                 ; {hard.workRam+9E}
C40B: A9 00           LDA     #$00                
C40D: 85 73           STA     $73                 ; {hard.workRam+73} blank the header for the uncolored pass
C40F: A9 08           LDA     #$08                
C411: 20 4C DF        JSR     $DF4C               ; {code.emitTaggedVectorWord} emit a tagged vector word
C414: 20 23 C4        JSR     $C423               ; {code.emitProjectedSlotRecord} re-emit the slot record uncolored
C417: 68              PLA                         
C418: 85 73           STA     $73                 ; {hard.workRam+73} restore the color header
C41A: 20 3C C4        JSR     $C43C               ; {code.loadSlotCoordBlock} reload the slot's coordinate block
C41D: 20 BA C3        JSR     $C3BA               ; {code.emitCoordDeltaRecord} close the frame via the coordinate-delta record
C420: A6 37           LDX     $37                 ; {hard.workRam+37} return the stepped-back index
C422: 60              RTS                         

; Copies slot loc_37's projected-delta cells
; loc_32a/loc_31a/loc_34a/loc_33a into loc_61-loc_64 and emits the delta
; record.
emitProjectedSlotRecord:
C423: A6 37           LDX     $37                 ; {hard.workRam+37} load the slot index
C425: BD 2A 03        LDA     $032A,X             ; {hard.workRam+32A} load plane-A sub into the projected Y low
C428: 85 61           STA     $61                 ; {hard.workRam+61}
C42A: BD 1A 03        LDA     $031A,X             ; {hard.workRam+31A} load plane-A value into the projected Y high
C42D: 85 62           STA     $62                 ; {hard.workRam+62}
C42F: BD 4A 03        LDA     $034A,X             ; {hard.workRam+34A} load plane-B sub into the projected X low
C432: 85 63           STA     $63                 ; {hard.workRam+63}
C434: BD 3A 03        LDA     $033A,X             ; {hard.workRam+33A} load plane-B value into the projected X high
C437: 85 64           STA     $64                 ; {hard.workRam+64}
C439: 4C BA C3        JMP     $C3BA               ; {code.emitCoordDeltaRecord} emit the coordinate delta record

; Reads slot index loc_37 and copies that column of
; loc_36a/loc_35a/loc_38a/loc_37a into the working coord block
; loc_61-loc_64.
loadSlotCoordBlock:
C43C: A6 37           LDX     $37                 ; {hard.workRam+37} load the slot index
C43E: BD 6A 03        LDA     $036A,X             ; {hard.workRam+36A} load the per-object Y-delta low
C441: 85 61           STA     $61                 ; {hard.workRam+61}
C443: BD 5A 03        LDA     $035A,X             ; {hard.workRam+35A} load the per-object Y-delta high
C446: 85 62           STA     $62                 ; {hard.workRam+62}
C448: BD 8A 03        LDA     $038A,X             ; {hard.workRam+38A} load the per-object X-delta low
C44B: 85 63           STA     $63                 ; {hard.workRam+63}
C44D: BD 7A 03        LDA     $037A,X             ; {hard.workRam+37A} load the per-object X-delta high
C450: 85 64           STA     $64                 ; {hard.workRam+64}
C452: 60              RTS                         

; When guard loc_5b is clear and loc_57 sits under 0x0c above reference
; loc_5f, raises loc_57 to loc_5f+0x0f, capped at ceiling 0xf0.
snapCoordUpToReference:
C453: A5 5B           LDA     $5B                 ; {hard.workRam+5B} load the depth-low guard
C455: D0 1A           BNE     $C471               ; {code.loc_c471} bail unless the guard is clear
C457: A5 57           LDA     $57                 ; {hard.workRam+57}
C459: 38              SEC                         
C45A: E5 5F           SBC     $5F                 ; {hard.workRam+5F} object depth minus reference
C45C: 90 02           BCC     $C460               ; {code.loc_c460}
C45E: C9 0C           CMP     #$0C                

loc_c460:
C460: B0 0F           BCS     $C471               ; {code.loc_c471} bail when the gap is too wide
C462: A5 5F           LDA     $5F                 ; {hard.workRam+5F}
C464: 18              CLC                         
C465: 69 0F           ADC     #$0F                ; form reference plus 0x0f
C467: B0 02           BCS     $C46B               ; {code.loc_c46b}
C469: C9 F0           CMP     #$F0                

loc_c46b:
C46B: 90 02           BCC     $C46F               ; {code.loc_c46f}
C46D: A9 F0           LDA     #$F0                ; cap at the ceiling 0xf0

loc_c46f:
C46F: 85 57           STA     $57                 ; {hard.workRam+57} raise the object depth

loc_c471:
C471: 60              RTS                         

; ---- $C472-$C472: data ----
C472: DB

; project the sixteen tube lanes: from loc_57=A and out index loc_38=x,
; run 16 passes loading each column's base coords from loc_3ce/loc_3de
; into loc_56/loc_58, drive projectPointThroughMathbox, clamp both signed
; high-byte results into [-4..+3] (0xfc..0x03) writing value/sign into
; loc_31a/loc_32a and loc_33a/loc_34a at loc_38, tally each clamp in
; loc_59, and return the clamp count.
projectAllLanesThroughMathbox:
C473: 85 57           STA     $57                 ; {hard.workRam+57} seed the object depth from A
C475: 86 38           STX     $38                 ; {hard.workRam+38} stash the output index
C477: A9 00           LDA     #$00                
C479: 85 59           STA     $59                 ; {hard.workRam+59} clear the clamp tally
C47B: A2 0F           LDX     #$0F                
C47D: 86 37           STX     $37                 ; {hard.workRam+37}

loc_c47f:
C47F: A6 37           LDX     $37                 ; {hard.workRam+37}
C481: BD CE 03        LDA     $03CE,X             ; {hard.workRam+3CE} load the lane base X into the projection operand
C484: 85 56           STA     $56                 ; {hard.workRam+56}
C486: BD DE 03        LDA     $03DE,X             ; {hard.workRam+3DE} load the lane base Y into the projection operand
C489: 85 58           STA     $58                 ; {hard.workRam+58}
C48B: 20 98 C0        JSR     $C098               ; {code.projectPointThroughMathbox} project the point through the math box
C48E: A6 38           LDX     $38                 ; {hard.workRam+38}
C490: A4 61           LDY     $61                 ; {hard.workRam+61} load the projected Y low
C492: A5 62           LDA     $62                 ; {hard.workRam+62} load the projected Y high
C494: 30 0D           BMI     $C4A3               ; {code.loc_c4a3} branch to clamp the low side on a negative result
C496: C9 04           CMP     #$04                
C498: 90 06           BCC     $C4A0               ; {code.loc_c4a0} within range -- keep the value
C49A: A0 FF           LDY     #$FF                
C49C: A9 03           LDA     #$03                ; clamp the high side to +3
C49E: E6 59           INC     $59                 ; {hard.workRam+59} tally the clamp

loc_c4a0:
C4A0: B8              CLV                         
C4A1: 50 0A           BVC     $C4AD               ; {code.loc_c4ad}

loc_c4a3:
C4A3: C9 FC           CMP     #$FC                ; compare against the low limit
C4A5: B0 06           BCS     $C4AD               ; {code.loc_c4ad}
C4A7: A0 01           LDY     #$01                
C4A9: A9 FC           LDA     #$FC                ; clamp the low side to -4
C4AB: E6 59           INC     $59                 ; {hard.workRam+59} tally the clamp

loc_c4ad:
C4AD: 9D 1A 03        STA     $031A,X             ; {hard.workRam+31A} store the clamped value into plane A
C4B0: 98              TYA                         
C4B1: 9D 2A 03        STA     $032A,X             ; {hard.workRam+32A} store the sign into the plane-A sub
C4B4: A4 63           LDY     $63                 ; {hard.workRam+63} load the projected X low
C4B6: A5 64           LDA     $64                 ; {hard.workRam+64} load the projected X high
C4B8: 30 0D           BMI     $C4C7               ; {code.loc_c4c7}
C4BA: C9 04           CMP     #$04                
C4BC: 90 06           BCC     $C4C4               ; {code.loc_c4c4}
C4BE: A0 FF           LDY     #$FF                
C4C0: A9 03           LDA     #$03                ; clamp the high side to +3
C4C2: E6 59           INC     $59                 ; {hard.workRam+59} tally the clamp

loc_c4c4:
C4C4: B8              CLV                         
C4C5: 50 0A           BVC     $C4D1               ; {code.loc_c4d1}

loc_c4c7:
C4C7: C9 FC           CMP     #$FC                
C4C9: B0 06           BCS     $C4D1               ; {code.loc_c4d1}
C4CB: A9 FC           LDA     #$FC                ; clamp the low side to -4
C4CD: A0 01           LDY     #$01                
C4CF: E6 59           INC     $59                 ; {hard.workRam+59} tally the clamp

loc_c4d1:
C4D1: 9D 3A 03        STA     $033A,X             ; {hard.workRam+33A} store the clamped value into plane B
C4D4: 98              TYA                         
C4D5: 9D 4A 03        STA     $034A,X             ; {hard.workRam+34A} store the sign into the plane-B sub
C4D8: C6 38           DEC     $38                 ; {hard.workRam+38}
C4DA: C6 37           DEC     $37                 ; {hard.workRam+37}
C4DC: 10 A1           BPL     $C47F               ; {code.loc_c47f} loop over the sixteen lanes
C4DE: A5 59           LDA     $59                 ; {hard.workRam+59} return the clamp count
C4E0: 60              RTS                         

; draw a sixteen-segment tube-shape outline: reduce the input byte via
; resolveShapeTableIndex (reduced->loc_36, quotient->loc_35), emit a
; framing record, pick a header from $C22D by loc_35&0x07 into loc_9e,
; seat the first vertex from $B97C/$BA7C (biased 0x80, seed rolled back
; 0x0f when $BCCC+loc_112 is zero), then walk 16 steps emitting each
; signed vertex delta from $B97C/$BA7C.
drawTubeShapeOutline:
C4E1: 20 E8 C2        JSR     $C2E8               ; {code.resolveShapeTableIndex} reduce the input byte to a shape index
C4E4: 85 36           STA     $36                 ; {hard.workRam+36} save the reduced value
C4E6: 86 35           STX     $35                 ; {hard.workRam+35} save the quotient
C4E8: A9 00           LDA     #$00                
C4EA: 85 73           STA     $73                 ; {hard.workRam+73} blank the record header
C4EC: A9 05           LDA     #$05                
C4EE: 20 6A DF        JSR     $DF6A               ; {code.emitBlankVectorWordTag70} emit a leading vector word
C4F1: A5 35           LDA     $35                 ; {hard.workRam+35}
C4F3: 29 07           AND     #$07                
C4F5: AA              TAX                         
C4F6: BC 2D C2        LDY     $C22D,X             ; {hard.rom+322D} pick the outline header from ROM
C4F9: 84 9E           STY     $9E                 ; {hard.workRam+9E} stash it as the color mode
C4FB: A9 08           LDA     #$08                
C4FD: 20 4C DF        JSR     $DF4C               ; {code.emitTaggedVectorWord} emit a tagged vector word
C500: AE 12 01        LDX     $0112               ; {hard.workRam+112} load the shape/level index
C503: A5 36           LDA     $36                 ; {hard.workRam+36}
C505: BC CC BC        LDY     $BCCC,X             ; {hard.rom+2CCC} read the per-shape level gate flag
C508: D0 03           BNE     $C50D               ; {code.loc_c50d}
C50A: 38              SEC                         
C50B: E9 0F           SBC     #$0F                ; roll the first-vertex seed back 0x0f when the gate is clear

loc_c50d:
C50D: A8              TAY                         
C50E: B9 7C BA        LDA     $BA7C,Y             ; {hard.rom+2A7C} read the ROM lane vertex Y
C511: 85 57           STA     $57                 ; {hard.workRam+57} seed the vertex Y
C513: 49 80           EOR     #$80                ; bias by 0x80
C515: AA              TAX                         
C516: B9 7C B9        LDA     $B97C,Y             ; {hard.rom+297C} read the ROM lane vertex X
C519: 85 56           STA     $56                 ; {hard.workRam+56} seed the vertex X
C51B: 49 80           EOR     #$80                ; bias by 0x80
C51D: 20 75 DF        JSR     $DF75               ; {code.emitScaledCoordinateRecord} emit the first scaled vertex record
C520: A9 C0           LDA     #$C0                
C522: 85 73           STA     $73                 ; {hard.workRam+73} set the record header to 0xc0
C524: A2 0F           LDX     #$0F                
C526: 86 38           STX     $38                 ; {hard.workRam+38} sixteen segments

loc_c528:
C528: A4 36           LDY     $36                 ; {hard.workRam+36}
C52A: B9 7C B9        LDA     $B97C,Y             ; {hard.rom+297C} read the next lane vertex X
C52D: AA              TAX                         
C52E: 38              SEC                         
C52F: E5 56           SBC     $56                 ; {hard.workRam+56} delta from the previous X
C531: 48              PHA                         
C532: 86 56           STX     $56                 ; {hard.workRam+56} cache it as the previous X
C534: B9 7C BA        LDA     $BA7C,Y             ; {hard.rom+2A7C} read the next lane vertex Y
C537: A8              TAY                         
C538: 38              SEC                         
C539: E5 57           SBC     $57                 ; {hard.workRam+57} delta from the previous Y
C53B: AA              TAX                         
C53C: 84 57           STY     $57                 ; {hard.workRam+57} cache it as the previous Y
C53E: 68              PLA                         
C53F: 20 75 DF        JSR     $DF75               ; {code.emitScaledCoordinateRecord} emit the signed vertex delta record
C542: C6 36           DEC     $36                 ; {hard.workRam+36}
C544: C6 38           DEC     $38                 ; {hard.workRam+38}
C546: 10 E0           BPL     $C528               ; {code.loc_c528} loop the sixteen segments
C548: A9 01           LDA     #$01                
C54A: 4C 6A DF        JMP     $DF6A               ; {code.emitBlankVectorWordTag70} emit the trailing blank word and return

; draw eight slots from table 0x3fe while guard 0x115 is set (forcing
; 0x5f=0xe8, 0x5b=0xff, 0xa0=0x28): per non-empty entry seat 0x57 with
; 0x56=0x58=0x80, pick a colour mode into 0x9e (slot&7 with 7->4 when
; 0x9f>=5, else 6), emit via emitTaggedVectorWord, set style
; 0x55=((slot&3)<<1)+0x0a, and draw via emitColoredShapeVector; restore
; the forced cells; tail increments 0x200+0x40 when 0x11f set and
; 0x42>=0x15.
drawTimedObjectList:
C54D: AD 15 01        LDA     $0115               ; {hard.workRam+115} load the descending-object guard
C550: F0 5F           BEQ     $C5B1               ; {code.loc_c5b1} skip the list when the guard is clear
C552: A5 5F           LDA     $5F                 ; {hard.workRam+5F}
C554: 48              PHA                         ; save the depth high byte
C555: A5 5B           LDA     $5B                 ; {hard.workRam+5B}
C557: 48              PHA                         ; save the depth guard
C558: A5 A0           LDA     $A0                 ; {hard.workRam+A0}
C55A: 48              PHA                         ; save the span cell
C55B: A9 E8           LDA     #$E8                
C55D: 85 5F           STA     $5F                 ; {hard.workRam+5F} force the depth high to 0xe8
C55F: A9 FF           LDA     #$FF                
C561: 85 5B           STA     $5B                 ; {hard.workRam+5B} force the depth guard to 0xff
C563: A9 28           LDA     #$28                
C565: 85 A0           STA     $A0                 ; {hard.workRam+A0} force the span cell to 0x28
C567: A2 07           LDX     #$07                
C569: 86 37           STX     $37                 ; {hard.workRam+37} eight object slots

loc_c56b:
C56B: A6 37           LDX     $37                 ; {hard.workRam+37}
C56D: BD FE 03        LDA     $03FE,X             ; {hard.workRam+3FE} read the object table entry
C570: F0 32           BEQ     $C5A4               ; {code.loc_c5a4} skip an empty entry
C572: 85 57           STA     $57                 ; {hard.workRam+57} entry into the object depth
C574: A9 80           LDA     #$80                
C576: 85 56           STA     $56                 ; {hard.workRam+56} center the X operand
C578: A9 80           LDA     #$80                
C57A: 85 58           STA     $58                 ; {hard.workRam+58} center the Y operand
C57C: A5 9F           LDA     $9F                 ; {hard.workRam+9F} load the level
C57E: C9 05           CMP     #$05                
C580: B0 05           BCS     $C587               ; {code.loc_c587} high levels take the per-slot color path
C582: A9 06           LDA     #$06                ; color mode 6 for low levels
C584: B8              CLV                         
C585: 50 09           BVC     $C590               ; {code.loc_c590}

loc_c587:
C587: 8A              TXA                         
C588: 29 07           AND     #$07                
C58A: C9 07           CMP     #$07                ; is this the last slot
C58C: D0 02           BNE     $C590               ; {code.loc_c590}
C58E: A9 04           LDA     #$04                ; the last slot uses color mode 4

loc_c590:
C590: 85 9E           STA     $9E                 ; {hard.workRam+9E} store the color mode
C592: A8              TAY                         
C593: A9 08           LDA     #$08                
C595: 20 4C DF        JSR     $DF4C               ; {code.emitTaggedVectorWord} emit a tagged vector word
C598: A5 37           LDA     $37                 ; {hard.workRam+37}
C59A: 29 03           AND     #$03                
C59C: 0A              ASL     A                   ; form the draw style from the slot's low bits
C59D: 69 0A           ADC     #$0A                
C59F: 85 55           STA     $55                 ; {hard.workRam+55} store the draw style
C5A1: 20 09 BD        JSR     $BD09               ; {code.emitColoredShapeVector} draw the colored shape vector

loc_c5a4:
C5A4: C6 37           DEC     $37                 ; {hard.workRam+37}
C5A6: 10 C3           BPL     $C56B               ; {code.loc_c56b} loop the eight slots
C5A8: 68              PLA                         
C5A9: 85 A0           STA     $A0                 ; {hard.workRam+A0} restore the span cell
C5AB: 68              PLA                         
C5AC: 85 5B           STA     $5B                 ; {hard.workRam+5B} restore the depth guard
C5AE: 68              PLA                         
C5AF: 85 5F           STA     $5F                 ; {hard.workRam+5F} restore the depth high byte

loc_c5b1:
C5B1: AD 1F 01        LDA     $011F               ; {hard.workRam+11F} test the award gate
C5B4: F0 0B           BEQ     $C5C1               ; {code.loc_c5c1}
C5B6: A6 42           LDX     $42                 ; {hard.workRam+42}
C5B8: E0 15           CPX     #$15                ; require the counter to have reached 0x15
C5BA: 90 05           BCC     $C5C1               ; {code.loc_c5c1}
C5BC: A6 40           LDX     $40                 ; {hard.workRam+40} index the player's rim segment
C5BE: FE 00 02        INC     $0200,X             ; {hard.workRam+200} bump that segment's tally

loc_c5c1:
C5C1: 60              RTS                         

; rebuild the per-frame enemy display list over up to sixteen slots (0x37
; from 0x0f, 0x0e when 0x111 set): early-out on gates 0x110/0x5b/0x5f,
; then per slot copy the fixed 4-byte header 0xc669 through cursor 0x74 at
; offset 0xa9 and append either a computed midpoint pair
; (emitSlotMidpointVertex + emitEnemySlotEntry) when 0x114 set, or a
; straight/sign-fixed coordinate block read from ($aa); restores the saved
; cursor 0xaa/0xab and flushes via advanceDisplayCursor.
buildEnemyDisplayList:
C5C2: AD 10 01        LDA     $0110               ; {hard.workRam+110} load the rim counter gate
C5C5: F0 01           BEQ     $C5C8               ; {code.loc_c5c8}
C5C7: 60              RTS                         ; bail when the counter is live

loc_c5c8:
C5C8: A5 5B           LDA     $5B                 ; {hard.workRam+5B} load the depth guard
C5CA: D0 07           BNE     $C5D3               ; {code.loc_c5d3}
C5CC: A5 5F           LDA     $5F                 ; {hard.workRam+5F}
C5CE: C9 F0           CMP     #$F0                ; compare the depth against the ceiling
C5D0: 90 01           BCC     $C5D3               ; {code.loc_c5d3}
C5D2: 60              RTS                         ; bail when the depth is at the ceiling

loc_c5d3:
C5D3: A9 01           LDA     #$01                
C5D5: 20 6A DF        JSR     $DF6A               ; {code.emitBlankVectorWordTag70} emit a blank leading vector word
C5D8: A5 74           LDA     $74                 ; {hard.workRam+74}
C5DA: 48              PHA                         ; save the draw cursor low
C5DB: A5 75           LDA     $75                 ; {hard.workRam+75}
C5DD: 48              PHA                         ; save the draw cursor high
C5DE: A9 00           LDA     #$00                
C5E0: 85 38           STA     $38                 ; {hard.workRam+38} clear the table cursor
C5E2: 85 A9           STA     $A9                 ; {hard.workRam+A9} clear the draw-cursor offset
C5E4: A2 0F           LDX     #$0F                
C5E6: AD 11 01        LDA     $0111               ; {hard.workRam+111} test the tube-geometry flag
C5E9: F0 01           BEQ     $C5EC               ; {code.loc_c5ec}
C5EB: CA              DEX                         ; drop to fifteen slots when the flag is set

loc_c5ec:
C5EC: 86 37           STX     $37                 ; {hard.workRam+37} seat the slot loop index

loc_c5ee:
C5EE: A2 03           LDX     #$03                
C5F0: A4 A9           LDY     $A9                 ; {hard.workRam+A9}

loc_c5f2:
C5F2: BD 69 C6        LDA     $C669,X             ; {hard.rom+3669} read the fixed enemy-list header
C5F5: 91 74           STA     ($74),Y             ; {hard.workRam+74} write the header byte through the cursor
C5F7: C8              INY                         
C5F8: CA              DEX                         
C5F9: 10 F7           BPL     $C5F2               ; {code.loc_c5f2} copy the four header bytes
C5FB: 84 A9           STY     $A9                 ; {hard.workRam+A9} advance the cursor offset
C5FD: AD 14 01        LDA     $0114               ; {hard.workRam+114} test the display-dirty flag
C600: D0 4A           BNE     $C64C               ; {code.loc_c64c} take the midpoint path when dirty
C602: A6 38           LDX     $38                 ; {hard.workRam+38}
C604: BD 9A 03        LDA     $039A,X             ; {hard.workRam+39A} read the lane target flag
C607: 30 11           BMI     $C61A               ; {code.loc_c61a} a flagged lane takes the full-record path
C609: A2 0B           LDX     #$0B                
C60B: A4 A9           LDY     $A9                 ; {hard.workRam+A9}

loc_c60d:
C60D: B1 AA           LDA     ($AA),Y             ; {hard.workRam+AA} read a source record byte
C60F: 91 74           STA     ($74),Y             ; {hard.workRam+74} copy it through the cursor
C611: C8              INY                         
C612: CA              DEX                         
C613: 10 F8           BPL     $C60D               ; {code.loc_c60d} copy the twelve-byte block
C615: 84 A9           STY     $A9                 ; {hard.workRam+A9} advance the cursor offset
C617: B8              CLV                         
C618: 50 2F           BVC     $C649               ; {code.loc_c649}

loc_c61a:
C61A: A4 A9           LDY     $A9                 ; {hard.workRam+A9}
C61C: B1 AA           LDA     ($AA),Y             ; {hard.workRam+AA} read the source X low
C61E: 91 74           STA     ($74),Y             ; {hard.workRam+74} copy it through the cursor
C620: 85 6C           STA     $6C                 ; {hard.workRam+6C} cache it as the previous X low
C622: C8              INY                         
C623: B1 AA           LDA     ($AA),Y             ; {hard.workRam+AA} read the source X high
C625: 91 74           STA     ($74),Y             ; {hard.workRam+74} copy it through the cursor
C627: C9 10           CMP     #$10                
C629: 90 02           BCC     $C62D               ; {code.loc_c62d}
C62B: 09 E0           ORA     #$E0                ; sign-extend the high nibble

loc_c62d:
C62D: 85 6D           STA     $6D                 ; {hard.workRam+6D} store the previous X high
C62F: C8              INY                         
C630: B1 AA           LDA     ($AA),Y             ; {hard.workRam+AA} read the source Y low
C632: 91 74           STA     ($74),Y             ; {hard.workRam+74} copy it through the cursor
C634: 85 6A           STA     $6A                 ; {hard.workRam+6A} cache it as the previous Y low
C636: C8              INY                         
C637: B1 AA           LDA     ($AA),Y             ; {hard.workRam+AA} read the source Y high
C639: 91 74           STA     ($74),Y             ; {hard.workRam+74} copy it through the cursor
C63B: C9 10           CMP     #$10                
C63D: 90 02           BCC     $C641               ; {code.loc_c641}
C63F: 09 E0           ORA     #$E0                ; sign-extend the high nibble

loc_c641:
C641: 85 6B           STA     $6B                 ; {hard.workRam+6B} store the previous Y high
C643: C8              INY                         
C644: 84 A9           STY     $A9                 ; {hard.workRam+A9} advance the cursor offset
C646: 20 C7 C6        JSR     $C6C7               ; {code.emitEnemySlotEntry} emit the enemy-slot entry

loc_c649:
C649: B8              CLV                         
C64A: 50 06           BVC     $C652               ; {code.loc_c652}

loc_c64c:
C64C: 20 6D C6        JSR     $C66D               ; {code.emitSlotMidpointVertex} emit the slot midpoint vertex
C64F: 20 C7 C6        JSR     $C6C7               ; {code.emitEnemySlotEntry} emit the enemy-slot entry

loc_c652:
C652: A6 38           LDX     $38                 ; {hard.workRam+38}
C654: 1E 9A 03        ASL     $039A,X             ; {hard.workRam+39A} shift the lane target flag left
C657: E6 38           INC     $38                 ; {hard.workRam+38} step to the next table slot
C659: C6 37           DEC     $37                 ; {hard.workRam+37}
C65B: 10 91           BPL     $C5EE               ; {code.loc_c5ee} loop the slots
C65D: 68              PLA                         
C65E: 85 AB           STA     $AB                 ; {hard.workRam+AB} restore the source pointer high
C660: 68              PLA                         
C661: 85 AA           STA     $AA                 ; {hard.workRam+AA} restore the source pointer low
C663: A4 A9           LDY     $A9                 ; {hard.workRam+A9}
C665: 88              DEY                         
C666: 4C 5F DF        JMP     $DF5F               ; {code.advanceDisplayCursor} flush by advancing the display cursor

; ---- $C669-$C66C: data ----
C669: 80 40 68 05

; Round-up averages tube slot loc_38's two coord pairs (loc_36a/loc_35a,
; loc_38a/loc_37a) with its wrap neighbour (loc_38+1 & 0x0f) into
; loc_61-loc_64 and appends four midpoint bytes (high bytes masked 0x1f)
; to the display list at loc_a9.
emitSlotMidpointVertex:
C66D: A5 38           LDA     $38                 ; {hard.workRam+38} read the active tube lane (0..15)
C66F: AA              TAX                         
C670: 18              CLC                         
C671: 69 01           ADC     #$01                ; step to the next lane
C673: 29 0F           AND     #$0F                ; wrap the neighbour lane index around the 16-lane ring
C675: A8              TAY                         
C676: BD 6A 03        LDA     $036A,X             ; {hard.workRam+36A} this lane's Y coordinate
C679: 38              SEC                         
C67A: 79 6A 03        ADC     $036A,Y             ; {hard.workRam+36A} add the neighbour lane's Y, rounded up by one
C67D: 85 61           STA     $61                 ; {hard.workRam+61} stash the Y sum low byte
C67F: BD 5A 03        LDA     $035A,X             ; {hard.workRam+35A}
C682: 79 5A 03        ADC     $035A,Y             ; {hard.workRam+35A}
C685: 85 62           STA     $62                 ; {hard.workRam+62} carry into the Y sum high byte
C687: 0A              ASL     A                   ; halve the 16-bit Y sum, preserving its sign -- the lane-pair Y midpoint
C688: 66 62           ROR     $62                 ; {hard.workRam+62}
C68A: 66 61           ROR     $61                 ; {hard.workRam+61}
C68C: BD 8A 03        LDA     $038A,X             ; {hard.workRam+38A} this lane's X coordinate
C68F: 38              SEC                         
C690: 79 8A 03        ADC     $038A,Y             ; {hard.workRam+38A} add the neighbour lane's X, rounded up
C693: 85 63           STA     $63                 ; {hard.workRam+63} stash the X sum low byte
C695: BD 7A 03        LDA     $037A,X             ; {hard.workRam+37A}
C698: 79 7A 03        ADC     $037A,Y             ; {hard.workRam+37A}
C69B: 85 64           STA     $64                 ; {hard.workRam+64} carry into the X sum high byte
C69D: 0A              ASL     A                   ; halve the 16-bit X sum, preserving its sign -- the lane-pair X midpoint
C69E: 66 64           ROR     $64                 ; {hard.workRam+64}
C6A0: 66 63           ROR     $63                 ; {hard.workRam+63}
C6A2: A4 A9           LDY     $A9                 ; {hard.workRam+A9} load the running byte offset into the display list
C6A4: A5 63           LDA     $63                 ; {hard.workRam+63}
C6A6: 91 74           STA     ($74),Y             ; {hard.workRam+74} write the X midpoint low byte to the display list
C6A8: C8              INY                         
C6A9: 85 6C           STA     $6C                 ; {hard.workRam+6C} mirror it as the previous-point X low
C6AB: A5 64           LDA     $64                 ; {hard.workRam+64}
C6AD: 85 6D           STA     $6D                 ; {hard.workRam+6D} previous-point X high
C6AF: 29 1F           AND     #$1F                ; strip the vector-opcode tag bits from the high byte
C6B1: 91 74           STA     ($74),Y             ; {hard.workRam+74} write the X midpoint high byte
C6B3: C8              INY                         
C6B4: A5 61           LDA     $61                 ; {hard.workRam+61}
C6B6: 91 74           STA     ($74),Y             ; {hard.workRam+74} write the Y midpoint low byte
C6B8: C8              INY                         
C6B9: 85 6A           STA     $6A                 ; {hard.workRam+6A} mirror it as the previous-point Y low
C6BB: A5 62           LDA     $62                 ; {hard.workRam+62}
C6BD: 85 6B           STA     $6B                 ; {hard.workRam+6B} previous-point Y high
C6BF: 29 1F           AND     #$1F                ; strip the vector-opcode tag bits
C6C1: 91 74           STA     ($74),Y             ; {hard.workRam+74} write the Y midpoint high byte
C6C3: C8              INY                         
C6C4: 84 A9           STY     $A9                 ; {hard.workRam+A9} commit the advanced list offset -- four bytes appended
C6C6: 60              RTS                         

; Emits one enemy-slot vector entry keyed by kind byte loc_3ac+loc_38:
; four blank+0x71 pairs when inactive, else seats loc_57/loc_56/loc_58,
; clamps depth via c453, runs c098/c73c, and appends a random ($60CA-
; selected) or fixed marker word per loc_39a bit6.
emitEnemySlotEntry:
C6C7: A6 38           LDX     $38                 ; {hard.workRam+38} index by the active enemy slot
C6C9: BD AC 03        LDA     $03AC,X             ; {hard.workRam+3AC} read the slot's depth/kind byte
C6CC: D0 16           BNE     $C6E4               ; {code.loc_c6e4} live slot -> project it; a zero byte means the slot is empty
C6CE: A4 A9           LDY     $A9                 ; {hard.workRam+A9} empty slot: load the list offset
C6D0: A2 03           LDX     #$03                

loc_c6d2:
C6D2: A9 00           LDA     #$00                
C6D4: 91 74           STA     ($74),Y             ; {hard.workRam+74} write a blank byte
C6D6: C8              INY                         
C6D7: A9 71           LDA     #$71                ; write the 0x71 blanking word
C6D9: 91 74           STA     ($74),Y             ; {hard.workRam+74}
C6DB: C8              INY                         
C6DC: CA              DEX                         
C6DD: 10 F3           BPL     $C6D2               ; {code.loc_c6d2} repeat for four placeholder pairs -- keeps the list stride fixed
C6DF: 84 A9           STY     $A9                 ; {hard.workRam+A9} commit the advanced offset
C6E1: B8              CLV                         
C6E2: 50 57           BVC     $C73B               ; {code.loc_c73b} done

loc_c6e4:
C6E4: 85 57           STA     $57                 ; {hard.workRam+57} live slot: seat the depth as the projection input
C6E6: 20 53 C4        JSR     $C453               ; {code.snapCoordUpToReference} clamp the depth to the reference point
C6E9: BD 35 04        LDA     $0435,X             ; {hard.workRam+435} seat this slot's segment midpoint as the point to project (one axis)
C6EC: 85 56           STA     $56                 ; {hard.workRam+56}
C6EE: BD 45 04        LDA     $0445,X             ; {hard.workRam+445} seat the other axis of the point
C6F1: 85 58           STA     $58                 ; {hard.workRam+58}
C6F3: 20 98 C0        JSR     $C098               ; {code.projectPointThroughMathbox} project the point through the math box
C6F6: 20 3C C7        JSR     $C73C               ; {code.emitDeltaVectorPair} emit the projected delta vectors
C6F9: A6 38           LDX     $38                 ; {hard.workRam+38} reload the slot index
C6FB: BD 9A 03        LDA     $039A,X             ; {hard.workRam+39A} read the slot's target flag
C6FE: 29 40           AND     #$40                ; test target-flag bit6
C700: F0 1F           BEQ     $C721               ; {code.loc_c721} flag clear -> draw the fixed marker word
C702: 20 3E BD        JSR     $BD3E               ; {code.appendNormalizedMantissaExponent} flag set: append a normalized mantissa/exponent pair, advancing the cursor
C705: AD CA 60        LDA     $60CA               ; {hard.pokey1+A} read a bit of the sound chip's random register
C708: 29 02           AND     #$02                
C70A: 18              CLC                         
C70B: 69 1C           ADC     #$1C                ; pick one of two enemy template words at random
C70D: AA              TAX                         
C70E: BD C9 CE        LDA     $CEC9,X             ; {hard.rom+3EC9} write the template word high byte
C711: C8              INY                         
C712: 91 74           STA     ($74),Y             ; {hard.workRam+74}
C714: 88              DEY                         
C715: BD C8 CE        LDA     $CEC8,X             ; {hard.rom+3EC8} write the template word low byte
C718: 91 74           STA     ($74),Y             ; {hard.workRam+74}
C71A: C8              INY                         
C71B: C8              INY                         
C71C: 84 A9           STY     $A9                 ; {hard.workRam+A9} commit the offset -- a four-byte record
C71E: B8              CLV                         
C71F: 50 1A           BVC     $C73B               ; {code.loc_c73b} done

loc_c721:
C721: A4 A9           LDY     $A9                 ; {hard.workRam+A9} marker path: load the list offset
C723: A9 00           LDA     #$00                
C725: 91 74           STA     ($74),Y             ; {hard.workRam+74} write a blank byte
C727: C8              INY                         
C728: A9 68           LDA     #$68                ; write the 0x68 marker word
C72A: 91 74           STA     ($74),Y             ; {hard.workRam+74}
C72C: C8              INY                         
C72D: AD B2 3D        LDA     $3DB2               ; {hard.vectorRom+DB2} write the blank-slot vector low byte
C730: 91 74           STA     ($74),Y             ; {hard.workRam+74}
C732: C8              INY                         
C733: AD B3 3D        LDA     $3DB3               ; {hard.vectorRom+DB3} write the blank-slot vector high byte
C736: 91 74           STA     ($74),Y             ; {hard.workRam+74}
C738: C8              INY                         
C739: 84 A9           STY     $A9                 ; {hard.workRam+A9} commit the advanced offset

loc_c73b:
C73B: 60              RTS                         

; Emits two 16-bit differences (loc_63:64 minus loc_6c:6d, then loc_61:62
; minus loc_6a:6b) as vector words, high bytes masked to five bits and the
; second OR'd with opcode 0xa0, advancing cursor loc_a9 by four.
emitDeltaVectorPair:
C73C: A4 A9           LDY     $A9                 ; {hard.workRam+A9} load the running list offset
C73E: A5 63           LDA     $63                 ; {hard.workRam+63} X delta: projected X minus the previous point's X
C740: 38              SEC                         
C741: E5 6C           SBC     $6C                 ; {hard.workRam+6C}
C743: 91 74           STA     ($74),Y             ; {hard.workRam+74} write the X delta low byte
C745: C8              INY                         
C746: A5 64           LDA     $64                 ; {hard.workRam+64} X delta high byte, clipped to five bits
C748: E5 6D           SBC     $6D                 ; {hard.workRam+6D}
C74A: 29 1F           AND     #$1F                
C74C: 91 74           STA     ($74),Y             ; {hard.workRam+74} write it
C74E: C8              INY                         
C74F: A5 61           LDA     $61                 ; {hard.workRam+61} Y delta: projected Y minus the previous point's Y
C751: 38              SEC                         
C752: E5 6A           SBC     $6A                 ; {hard.workRam+6A}
C754: 91 74           STA     ($74),Y             ; {hard.workRam+74} write the Y delta low byte
C756: C8              INY                         
C757: A5 62           LDA     $62                 ; {hard.workRam+62} Y delta high byte, clipped and stamped with the 0xa0 vector opcode
C759: E5 6B           SBC     $6B                 ; {hard.workRam+6B}
C75B: 29 1F           AND     #$1F                
C75D: 09 A0           ORA     #$A0                
C75F: 91 74           STA     ($74),Y             ; {hard.workRam+74} write it
C761: C8              INY                         
C762: 84 A9           STY     $A9                 ; {hard.workRam+A9} commit the offset -- two delta words appended
C764: 60              RTS                         

; Writes the fixed header word 0x00/0x71 at the draw cursor start
; (loc_74/loc_75) then resumes the shared vector-record builder from
; cursor slot 2.
layHeaderAndBuildRecord:
C765: A0 00           LDY     #$00                ; start the write at the cursor head
C767: 98              TYA                         
C768: 91 74           STA     ($74),Y             ; {hard.workRam+74} write the fixed header byte 0x00
C76A: A9 71           LDA     #$71                ; write the fixed header byte 0x71
C76C: C8              INY                         
C76D: 91 74           STA     ($74),Y             ; {hard.workRam+74}
C76F: C8              INY                         
C770: D0 02           BNE     $C774               ; {code.emitObjectPositionRecord} fall into the position-record builder past the header

; emit an object's position vector: from cursor offset 0, write the
; {0x40,0x80} header, an X word from zero-page pair 0x2/0x3 indexed by X
; and a Y word from pair 0x00/0x1 (each high byte masked to 5 bits),
; caching the raw bytes as the previous point (X low/high at 0x6c/0x6d, Y
; low/high at 0x6a/0x6b), then advance the cursor 0x74/0x75 past the six
; emitted bytes.
emitObjectPositionVector:
C772: A0 00           LDY     #$00                ; public entry: start the record at cursor offset 0

; emit a six-byte object position record into the vector list at write
; cursor loc_74/loc_75 offset Y: a fixed header (0x40,0x80) then the
; object's X pair (loc_2+x low, loc_3+x high masked to 5 bits) and Y pair
; (loc_00+x low, loc_1+x high masked to 5 bits), caching the raw bytes
; into loc_6c/loc_6d/loc_6a/loc_6b, then advancing the cursor past the
; bytes via advanceDisplayCursor (entry emitObjectPositionVector starts
; the offset at 0).
emitObjectPositionRecord:
C774: A9 40           LDA     #$40                ; write position-record header byte 0x40
C776: 91 74           STA     ($74),Y             ; {hard.workRam+74}
C778: A9 80           LDA     #$80                ; write position-record header byte 0x80
C77A: C8              INY                         
C77B: 91 74           STA     ($74),Y             ; {hard.workRam+74}
C77D: C8              INY                         
C77E: B5 02           LDA     $02,X               ; {hard.workRam+2} object X low, cached as the previous point's X low
C780: 85 6C           STA     $6C                 ; {hard.workRam+6C}
C782: 91 74           STA     ($74),Y             ; {hard.workRam+74} write it
C784: C8              INY                         
C785: B5 03           LDA     $03,X               ; {hard.workRam+3} object X high, cached, clipped to five bits
C787: 85 6D           STA     $6D                 ; {hard.workRam+6D}
C789: 29 1F           AND     #$1F                
C78B: 91 74           STA     ($74),Y             ; {hard.workRam+74} write it
C78D: B5 00           LDA     $00,X               ; {hard.workRam} object Y low, cached as the previous point's Y low
C78F: 85 6A           STA     $6A                 ; {hard.workRam+6A}
C791: C8              INY                         
C792: 91 74           STA     ($74),Y             ; {hard.workRam+74} write it
C794: B5 01           LDA     $01,X               ; {hard.workRam+1} object Y high, cached, clipped to five bits
C796: 85 6B           STA     $6B                 ; {hard.workRam+6B}
C798: 29 1F           AND     #$1F                
C79A: C8              INY                         
C79B: 91 74           STA     ($74),Y             ; {hard.workRam+74} write it
C79D: 4C 5F DF        JMP     $DF5F               ; {code.advanceDisplayCursor} advance the draw cursor past the six emitted bytes

; the main frame loop (a generator): after a one-time board-init pass
; (resetBothPokeyChips) and seeding 0x00=0, free-run forever -- each pass
; yields until the interrupt counter 0x53 reaches 9, clears it, and runs
; the three per-update passes dispatchFramePhaseHandler,
; seedFramePhaseAndTick, buildFrameVectors (~26.5Hz).
runMainFrameLoop:
C7A0: 20 95 CD        JSR     $CD95               ; {code.resetBothPokeyChips} one-time: reset both sound/IO chips
C7A3: A9 00           LDA     #$00                
C7A5: 85 00           STA     $00                 ; {hard.workRam} seed the live game mode to 0

loc_c7a7:
C7A7: A5 53           LDA     $53                 ; {hard.workRam+53} frame boundary: wait until nine interrupts have accumulated (~26.5Hz)
C7A9: C9 09           CMP     #$09                
C7AB: 90 FA           BCC     $C7A7               ; {code.loc_c7a7}
C7AD: A9 00           LDA     #$00                ; consume the interrupt count, start the next frame
C7AF: 85 53           STA     $53                 ; {hard.workRam+53}
C7B1: 20 BD C7        JSR     $C7BD               ; {code.dispatchFramePhaseHandler} run the current mode's phase handler
C7B4: 20 91 C8        JSR     $C891               ; {code.seedFramePhaseAndTick} seed the next phase and tick the frame clock
C7B7: 20 B6 B1        JSR     $B1B6               ; {code.buildFrameVectors} build this frame's vector display list
C7BA: 18              CLC                         
C7BB: 90 EA           BCC     $C7A7               ; {code.loc_c7a7} loop back forever to the frame wait

; DSW-gated per-frame handler dispatch: do nothing when the coinage dip
; (0xd00 & 0x83) reads 0x82; otherwise run a pre-pass ($A7D2), set bit7 of
; 0x4e, and select one of eighteen per-frame handlers by the byte offset
; in 0x00 (index offset>>1 into a 19-entry table whose one slot is
; unused).
dispatchFramePhaseHandler:
C7BD: AD 00 0D        LDA     $0D00               ; {hard.dsw1} coinage dip config 0x82 disables this whole update pass
C7C0: 29 83           AND     #$83                
C7C2: C9 82           CMP     #$82                
C7C4: F0 13           BEQ     $C7D9               ; {code.loc_c7d9}
C7C6: 20 D2 A7        JSR     $A7D2               ; {code.stepSpikeTableCollapse} pre-pass: step the spike-table collapse
C7C9: A6 00           LDX     $00                 ; {hard.workRam} select the phase handler by the current game mode
C7CB: A5 4E           LDA     $4E                 ; {hard.workRam+4E}
C7CD: 09 80           ORA     #$80                ; mark this frame's edge state -- set bit7
C7CF: 85 4E           STA     $4E                 ; {hard.workRam+4E}
C7D1: BD DB C7        LDA     $C7DB,X             ; {hard.rom+37DB} push the handler's address high byte from the mode dispatch table
C7D4: 48              PHA                         
C7D5: BD DA C7        LDA     $C7DA,X             ; {hard.rom+37DA} push its low byte
C7D8: 48              PHA                         

loc_c7d9:
C7D9: 60              RTS                         ; jump to the selected phase handler

; ---- $C7DA-$C7FF: data ----
C7DA: 0B C9 3F C9 0A 97 AE C9 F0 C9 FF C7 00 00 8B C9
C7EA: 3E AC 6D AD 17 CA 48 91 4A 90 E6 B0 07 91 7A C9
C7FA: 28 97 E0 D7 17 A6

; while the guard loc_3 & loc_16b is set do nothing; otherwise run delay
; counter loc_4 down and, on the frame it reaches zero, load the live mode
; loc_0 from the pending mode loc_2 and clear the guard loc_16b; every
; path tail-delegates the spinner update rotateBlasterAroundRim.
commitPendingModeAfterDelay:
C800: A5 03           LDA     $03                 ; {hard.workRam+3} while the guarded frame-counter bit is set, suppress the countdown
C802: 2D 6B 01        AND     $016B               ; {hard.workRam+16B}
C805: D0 11           BNE     $C818               ; {code.loc_c818}
C807: A5 04           LDA     $04                 ; {hard.workRam+4} tick the mode-change delay timer toward zero
C809: F0 02           BEQ     $C80D               ; {code.loc_c80d}
C80B: C6 04           DEC     $04                 ; {hard.workRam+4}

loc_c80d:
C80D: D0 09           BNE     $C818               ; {code.loc_c818} not expired yet -> just service the shooter
C80F: A5 02           LDA     $02                 ; {hard.workRam+2} delay expired: commit the pending mode as the live mode
C811: 85 00           STA     $00                 ; {hard.workRam}
C813: A9 00           LDA     #$00                
C815: 8D 6B 01        STA     $016B               ; {hard.workRam+16B} clear the arming guard

loc_c818:
C818: 4C 49 97        JMP     $9749               ; {code.rotateBlasterAroundRim} advance the player's shooter around the tube rim

; from the 2-bit gate loc_4e&0x60 (then cleared) and a >=2 test on counter
; loc_6 derive a step 0..2 and drain loc_6; when the gate is clear
; optionally seed intro cells (loc_1/loc_4/loc_0/loc_2, gated by loc_50
; and loc_5 bit7); when the step is nonzero set loc_5|=0xc0, zero
; loc_16/loc_18/loc_0, bump the 16-bit tally loc_40c,x/loc_40d,x, and
; advance the level cell loc_100 by step+1 clamped to 0x63.
advanceLevelCounter:
C81B: A5 06           LDA     $06                 ; {hard.workRam+6} read the phase counter -- phases still owed
C81D: A0 00           LDY     #$00                
C81F: C9 02           CMP     #$02                ; note whether at least two phases remain
C821: A5 4E           LDA     $4E                 ; {hard.workRam+4E} extract the pending-advance request bits (6..5)
C823: 29 60           AND     #$60                
C825: 84 4E           STY     $4E                 ; {hard.workRam+4E} consume the request, clearing the flags
C827: F0 48           BEQ     $C871               ; {code.loc_c871} no advance requested -> the queued-intro path
C829: B0 05           BCS     $C830               ; {code.loc_c830} two or more phases owed -> the double-step branch
C82B: 29 20           AND     #$20                ; otherwise test request bit5 only
C82D: B8              CLV                         
C82E: 50 05           BVC     $C835               ; {code.loc_c835}

loc_c830:
C830: C8              INY                         ; count one step and drain a phase
C831: C6 06           DEC     $06                 ; {hard.workRam+6}
C833: 29 40           AND     #$40                ; request bit6 -> a second step

loc_c835:
C835: F0 03           BEQ     $C83A               ; {code.loc_c83a}
C837: C6 06           DEC     $06                 ; {hard.workRam+6} drain another phase for the double step
C839: C8              INY                         

loc_c83a:
C83A: 98              TYA                         
C83B: 85 3E           STA     $3E                 ; {hard.workRam+3E} store the derived 0..2 level step
C83D: F0 2F           BEQ     $C86E               ; {code.loc_c86e} a zero step -> nothing to advance
C83F: A5 05           LDA     $05                 ; {hard.workRam+5} latch the advance in the status flags (top two bits)
C841: 09 C0           ORA     #$C0                
C843: 85 05           STA     $05                 ; {hard.workRam+5}
C845: A9 00           LDA     #$00                
C847: 85 16           STA     $16                 ; {hard.workRam+16} clear the heartbeat accumulator low byte
C849: 85 18           STA     $18                 ; {hard.workRam+18} clear its overflow byte
C84B: A9 00           LDA     #$00                
C84D: 85 00           STA     $00                 ; {hard.workRam} reset the game mode to 0
C84F: C6 3E           DEC     $3E                 ; {hard.workRam+3E} index the level tally by the step: 1 -> offset 0, 2 -> offset 3
C851: A6 3E           LDX     $3E                 ; {hard.workRam+3E}
C853: F0 02           BEQ     $C857               ; {code.loc_c857}
C855: A2 03           LDX     #$03                

loc_c857:
C857: FE 0C 04        INC     $040C,X             ; {hard.workRam+40C} bump the 16-bit level tally, carrying into the high byte
C85A: D0 03           BNE     $C85F               ; {code.loc_c85f}
C85C: FE 0D 04        INC     $040D,X             ; {hard.workRam+40D}

loc_c85f:
C85F: AD 00 01        LDA     $0100               ; {hard.workRam+100} advance the on-screen level number by the step (1 or 2)
C862: 38              SEC                         
C863: 65 3E           ADC     $3E                 ; {hard.workRam+3E}
C865: C9 63           CMP     #$63                ; clamp it to 0x63
C867: 90 02           BCC     $C86B               ; {code.loc_c86b}
C869: A9 63           LDA     #$63                

loc_c86b:
C86B: 8D 00 01        STA     $0100               ; {hard.workRam+100} store the new level number

loc_c86e:
C86E: B8              CLV                         ; done
C86F: 50 1F           BVC     $C890               ; {code.loc_c890}

loc_c871:
C871: A5 50           LDA     $50                 ; {hard.workRam+50} no-advance path: nothing latched -> exit
C873: F0 1B           BEQ     $C890               ; {code.loc_c890}
C875: 24 05           BIT     $05                 ; {hard.workRam+5} status bit7 set -> exit
C877: 30 17           BMI     $C890               ; {code.loc_c890}
C879: A9 10           LDA     #$10                ; arm the intro dispatch selector
C87B: 85 01           STA     $01                 ; {hard.workRam+1}
C87D: A9 20           LDA     #$20                ; set the mode-delay countdown
C87F: 85 04           STA     $04                 ; {hard.workRam+4}
C881: A9 0A           LDA     #$0A                ; enter mode 0x0a
C883: 85 00           STA     $00                 ; {hard.workRam}
C885: A9 14           LDA     #$14                ; queue the next mode 0x14
C887: 85 02           STA     $02                 ; {hard.workRam+2}
C889: A9 00           LDA     #$00                
C88B: 85 50           STA     $50                 ; {hard.workRam+50} disarm the latched spinner value
C88D: 8D 23 01        STA     $0123               ; {hard.workRam+123} reset the spike tally

loc_c890:
C890: 60              RTS                         

; per-frame mode/timing driver: from coin input 0xc00, mode flag 0x5 and
; phase counters 0xa/0x6, seed the phase/speed cells 0x00/0x1/0xa2
; (running the setup step advanceLevelCounter on the appropriate phase),
; then a common tail advances the frame counter 0x3, fires the EAROM step
; stepEaromTransfer on odd frames and the sound-register step
; requestActiveSoundCue when 0xc is live, and trims bit7 of 0x4e.
seedFramePhaseAndTick:
C891: AD 00 0C        LDA     $0C00               ; {hard.in0} coin input bit4 clear -> force game mode 0x22
C894: 29 10           AND     #$10                
C896: D0 07           BNE     $C89F               ; {code.loc_c89f}
C898: A9 22           LDA     #$22                ; force mode 0x22
C89A: 85 00           STA     $00                 ; {hard.workRam}
C89C: B8              CLV                         
C89D: 50 44           BVC     $C8E3               ; {code.loc_c8e3} skip to the common tail

loc_c89f:
C89F: 24 05           BIT     $05                 ; {hard.workRam+5} status bit6 set -> skip to the tail
C8A1: 70 40           BVS     $C8E3               ; {code.loc_c8e3}
C8A3: A5 0A           LDA     $0A                 ; {hard.workRam+A} even phase -> straight to the level-counter step
C8A5: 29 01           AND     #$01                
C8A7: F0 29           BEQ     $C8D2               ; {code.loc_c8d2}
C8A9: A4 06           LDY     $06                 ; {hard.workRam+6} read the phase counter
C8AB: D0 04           BNE     $C8B1               ; {code.loc_c8b1}
C8AD: A9 80           LDA     #$80                ; an expired counter arms the phase gate
C8AF: 85 A2           STA     $A2                 ; {hard.workRam+A2}

loc_c8b1:
C8B1: 24 A2           BIT     $A2                 ; {hard.workRam+A2} gate clear -> the level-counter step
C8B3: 10 1D           BPL     $C8D2               ; {code.loc_c8d2}
C8B5: C0 02           CPY     #$02                ; two or more phases owed -> the mode-0x14 branch
C8B7: B0 11           BCS     $C8CA               ; {code.loc_c8ca}
C8B9: 98              TYA                         
C8BA: F0 08           BEQ     $C8C4               ; {code.loc_c8c4} zero phases -> skip the mode seed
C8BC: A9 16           LDA     #$16                ; one phase: select dispatch 0x16
C8BE: 85 01           STA     $01                 ; {hard.workRam+1}
C8C0: A9 0A           LDA     #$0A                ; enter mode 0x0a
C8C2: 85 00           STA     $00                 ; {hard.workRam}

loc_c8c4:
C8C4: 4C D9 C8        JMP     $C8D9               ; {code.loc_c8d9} continue to the frame tick

; ---- $C8C7-$C8C9: data ----
C8C7: B8 50 08

loc_c8ca:
C8CA: A9 14           LDA     #$14                ; set game mode 0x14
C8CC: 85 00           STA     $00                 ; {hard.workRam}
C8CE: A9 00           LDA     #$00                ; clear the phase gate
C8D0: 85 A2           STA     $A2                 ; {hard.workRam+A2}

loc_c8d2:
C8D2: A5 06           LDA     $06                 ; {hard.workRam+6} run the level-advance bookkeeper only when a phase is owed
C8D4: F0 03           BEQ     $C8D9               ; {code.loc_c8d9}
C8D6: 20 1B C8        JSR     $C81B               ; {code.advanceLevelCounter} step the level-advance bookkeeper

loc_c8d9:
C8D9: A5 09           LDA     $09                 ; {hard.workRam+9} every fourth frame...
C8DB: 29 03           AND     #$03                
C8DD: D0 04           BNE     $C8E3               ; {code.loc_c8e3}
C8DF: A9 02           LDA     #$02                ; ...reseed the phase counter to 2
C8E1: 85 06           STA     $06                 ; {hard.workRam+6}

loc_c8e3:
C8E3: E6 03           INC     $03                 ; {hard.workRam+3} advance the master frame counter
C8E5: A5 03           LDA     $03                 ; {hard.workRam+3} on odd frames...
C8E7: 29 01           AND     #$01                
C8E9: F0 03           BEQ     $C8EE               ; {code.loc_c8ee}
C8EB: 20 1B DE        JSR     $DE1B               ; {code.stepEaromTransfer} ...step the non-volatile high-score store transfer

loc_c8ee:
C8EE: A5 0C           LDA     $0C                 ; {hard.workRam+C} when a sound step is queued...
C8F0: F0 03           BEQ     $C8F5               ; {code.loc_c8f5}
C8F2: 20 FA CC        JSR     $CCFA               ; {code.requestActiveSoundCue} ...register the active sound

loc_c8f5:
C8F5: AD 6C 01        LDA     $016C               ; {hard.workRam+16C} read the decimal-mode guard
C8F8: F0 07           BEQ     $C901               ; {code.loc_c901}
C8FA: A9 13           LDA     #$13                
C8FC: C5 9F           CMP     $9F                 ; {hard.workRam+9F}
C8FE: B0 01           BCS     $C901               ; {code.loc_c901}
C900: F8              SED                         ; arm decimal mode when the guard opens

loc_c901:
C901: A5 4E           LDA     $4E                 ; {hard.workRam+4E} if this frame's edge bit is set...
C903: 29 80           AND     #$80                
C905: F0 04           BEQ     $C90B               ; {code.loc_c90b}
C907: A9 00           LDA     #$00                ; ...clear the edge flags
C909: 85 4E           STA     $4E                 ; {hard.workRam+4E}

loc_c90b:
C90B: 60              RTS                         

; reset the per-slot playfield state: run setup passes
; rebuildControlBlocksIfRequested/buildLevelLayout (and
; clearChannelStagingBlock when 0x5 negative), clear 0x49, walk every slot
; from 0x3e down to 0 seeding 0x48,slot from 0x158 and 0x46,slot=0xff,
; clear 0x3f and 0x115, reload 0x3d from 0x3e, then tail-delegate to
; selectWaveStartSlot.
resetLevelPlayfieldSlots:
C90C: 20 A2 AB        JSR     $ABA2               ; {code.rebuildControlBlocksIfRequested} rebuild the control blocks if requested
C90F: 20 6E C1        JSR     $C16E               ; {code.buildLevelLayout} build the level's geometry layout
C912: A5 05           LDA     $05                 ; {hard.workRam+5} only when the status byte is negative...
C914: 10 03           BPL     $C919               ; {code.loc_c919}
C916: 20 62 CA        JSR     $CA62               ; {code.clearChannelStagingBlock} ...clear the channel staging block

loc_c919:
C919: A9 00           LDA     #$00                ; clear the slot-countdown high byte
C91B: 85 49           STA     $49                 ; {hard.workRam+49}
C91D: A6 3E           LDX     $3E                 ; {hard.workRam+3E} start the loop index at the top live slot
C91F: 86 3D           STX     $3D                 ; {hard.workRam+3D}

loc_c921:
C921: A6 3D           LDX     $3D                 ; {hard.workRam+3D}
C923: AD 58 01        LDA     $0158               ; {hard.workRam+158} seed this slot's countdown from the bonus config
C926: 9D 48 00        STA     $0048,X             ; {hard.workRam+48}
C929: A9 FF           LDA     #$FF                ; mark the slot's level entry unassigned
C92B: 9D 46 00        STA     $0046,X             ; {hard.workRam+46}
C92E: C6 3D           DEC     $3D                 ; {hard.workRam+3D} walk down through every live slot
C930: 10 EF           BPL     $C921               ; {code.loc_c921}
C932: A9 00           LDA     #$00                
C934: 85 3F           STA     $3F                 ; {hard.workRam+3F} clear the level id
C936: 8D 15 01        STA     $0115               ; {hard.workRam+115} clear the spike-table guard
C939: A5 3E           LDA     $3E                 ; {hard.workRam+3E} reload the index to the top slot for the next consumer
C93B: 85 3D           STA     $3D                 ; {hard.workRam+3D}
C93D: 4C C4 90        JMP     $90C4               ; {code.selectWaveStartSlot} hand off to wave-start slot selection

; set up the level: seed sizing/timer cells loc_1=0, loc_00=30, loc_2=30,
; and when the level id loc_3f differs from last-seen loc_3d latch loc_3d
; and (with loc_5 negative) install the new-level timers
; loc_1=14/loc_00=10/loc_4=40or80 (by loc_117) via swapParallelTables,
; then run selectProjectionScale, index loc_46 by loc_3d into loc_9f, run
; runLevelInit and tail-delegate to the readout reset resetBothPokeyChips.
setupLevelTimers:
C940: A9 00           LDA     #$00                ; clear the dispatch selector
C942: 85 01           STA     $01                 ; {hard.workRam+1}
C944: A9 1E           LDA     #$1E                ; seed the game mode and pending mode to 30
C946: 85 00           STA     $00                 ; {hard.workRam}
C948: 85 02           STA     $02                 ; {hard.workRam+2}
C94A: A5 3F           LDA     $3F                 ; {hard.workRam+3F} only on a genuine level change...
C94C: C5 3D           CMP     $3D                 ; {hard.workRam+3D}
C94E: F0 1C           BEQ     $C96C               ; {code.loc_c96c}
C950: 85 3D           STA     $3D                 ; {hard.workRam+3D} latch the new level id
C952: A5 05           LDA     $05                 ; {hard.workRam+5} ...and only when the status byte is negative
C954: 10 16           BPL     $C96C               ; {code.loc_c96c}
C956: A9 0E           LDA     #$0E                ; install the new-level dispatch selector
C958: 85 01           STA     $01                 ; {hard.workRam+1}
C95A: A9 0A           LDA     #$0A                ; set game mode 10
C95C: 85 00           STA     $00                 ; {hard.workRam}
C95E: A9 50           LDA     #$50                ; pick the level-delay timer -- 40 or 80
C960: AC 17 01        LDY     $0117               ; {hard.workRam+117}
C963: F0 02           BEQ     $C967               ; {code.loc_c967}
C965: A9 28           LDA     #$28                

loc_c967:
C967: 85 04           STA     $04                 ; {hard.workRam+4} store the delay timer
C969: 20 B2 92        JSR     $92B2               ; {code.swapParallelTables} swap the paired geometry tables

loc_c96c:
C96C: 20 48 CA        JSR     $CA48               ; {code.selectProjectionScale} size the projection scale
C96F: A6 3D           LDX     $3D                 ; {hard.workRam+3D}
C971: B5 46           LDA     $46,X               ; {hard.workRam+46} copy this level's per-slot level into the working cell
C973: 85 9F           STA     $9F                 ; {hard.workRam+9F}
C975: 20 25 90        JSR     $9025               ; {code.runLevelInit} run the level startup init
C978: 4C 95 CD        JMP     $CD95               ; {code.resetBothPokeyChips} reset the sound chips

; alternate state-entry seeder: write the four config cells loc_2=0x04,
; loc_1=0x00, loc_0=0x0a and loc_4=0x14.
seedModeParamsMinimal:
C97B: A9 04           LDA     #$04                ; queue mode 0x04 to promote after the delay
C97D: 85 02           STA     $02                 ; {hard.workRam+2}
C97F: A9 00           LDA     #$00                
C981: 85 01           STA     $01                 ; {hard.workRam+1} clear the dispatch selector
C983: A9 0A           LDA     #$0A                
C985: 85 00           STA     $00                 ; {hard.workRam} enter the live mode 0x0a
C987: A9 14           LDA     #$14                
C989: 85 04           STA     $04                 ; {hard.workRam+4} set the promotion countdown
C98B: 60              RTS                         

; ramp the per-level enemy quota: while the loc_46-slot indexed by level
; loc_3d is below 0x62, bump that slot and the working copy loc_9f
; together, seed loc_00=0x18, and when the loc_102-slot is nonzero run the
; handler chain (seatInPagePointer, addBcdScoreAndAwardAtThreshold,
; requestScoreAwardSound), then tail-delegate to init runWaveInit.
bumpLevelEnemyQuota:
C98C: A6 3D           LDX     $3D                 ; {hard.workRam+3D} index this level's enemy-quota cell
C98E: B5 46           LDA     $46,X               ; {hard.workRam+46}
C990: C9 62           CMP     #$62                ; quota below the cap?
C992: B0 04           BCS     $C998               ; {code.loc_c998} at the cap -> skip the bump
C994: F6 46           INC     $46,X               ; {hard.workRam+46} bump the level's enemy quota
C996: E6 9F           INC     $9F                 ; {hard.workRam+9F} bump its working copy in lockstep

loc_c998:
C998: A9 18           LDA     #$18                ; enter wave-active mode
C99A: 85 00           STA     $00                 ; {hard.workRam}
C99C: BD 02 01        LDA     $0102,X             ; {hard.workRam+102} if this level carries a bonus trigger...
C99F: F0 0B           BEQ     $C9AC               ; {code.loc_c9ac}
C9A1: 20 B5 91        JSR     $91B5               ; {code.seatInPagePointer} seat it as an in-page pointer
C9A4: A2 FF           LDX     #$FF                
C9A6: 20 6C CA        JSR     $CA6C               ; {code.addBcdScoreAndAwardAtThreshold} add it to the score at the top threshold
C9A9: 20 B9 CC        JSR     $CCB9               ; {code.requestScoreAwardSound} cue the score-award sound

loc_c9ac:
C9AC: 4C 09 90        JMP     $9009               ; {code.runWaveInit} bring the wave up

; clear loc_4, decrement the active slot's countdown loc_48[loc_3d]; when
; the loc_48/loc_49 pair is fully spent finalize via
; reloadPacingFromPeakSlot, otherwise (flag loc_1=0x0c and loc_4=0x28 if
; this tick hit zero) toggle loc_3f to pick the next non-empty slot, arm
; its timer loc_2 (0x1c when loc_46[x]+1 wraps, else 0x02), and request
; mode loc_0=0x0a.
tickEnemyPacingCountdown:
C9AF: A9 00           LDA     #$00                ; clear the mode-delay timer
C9B1: 85 04           STA     $04                 ; {hard.workRam+4}
C9B3: A6 3D           LDX     $3D                 ; {hard.workRam+3D} tick the active slot's pacing countdown low byte
C9B5: D6 48           DEC     $48,X               ; {hard.workRam+48}
C9B7: A5 48           LDA     $48                 ; {hard.workRam+48} if the whole countdown pair is spent...
C9B9: 05 49           ORA     $49                 ; {hard.workRam+49}
C9BB: D0 06           BNE     $C9C3               ; {code.loc_c9c3}
C9BD: 20 F1 C9        JSR     $C9F1               ; {code.reloadPacingFromPeakSlot} ...reload the wave's pacing from the peak slot
C9C0: B8              CLV                         ; and return
C9C1: 50 2D           BVC     $C9F0               ; {code.loc_c9f0}

loc_c9c3:
C9C3: A6 3D           LDX     $3D                 ; {hard.workRam+3D}
C9C5: B5 48           LDA     $48,X               ; {hard.workRam+48} if this tick zeroed the active slot...
C9C7: D0 08           BNE     $C9D1               ; {code.loc_c9d1}
C9C9: A9 0C           LDA     #$0C                ; ...raise the dispatch selector
C9CB: 85 01           STA     $01                 ; {hard.workRam+1}
C9CD: A9 28           LDA     #$28                ; and set the mode delay
C9CF: 85 04           STA     $04                 ; {hard.workRam+4}

loc_c9d1:
C9D1: A5 3E           LDA     $3E                 ; {hard.workRam+3E}
C9D3: F0 06           BEQ     $C9DB               ; {code.loc_c9db}
C9D5: A5 3F           LDA     $3F                 ; {hard.workRam+3F} toggle to the other pacing slot
C9D7: 49 01           EOR     #$01                
C9D9: 85 3F           STA     $3F                 ; {hard.workRam+3F}

loc_c9db:
C9DB: A6 3F           LDX     $3F                 ; {hard.workRam+3F}
C9DD: B5 48           LDA     $48,X               ; {hard.workRam+48} keep toggling until a non-empty slot is found
C9DF: F0 F0           BEQ     $C9D1               ; {code.loc_c9d1}
C9E1: A9 02           LDA     #$02                ; pick the slot's arm value -- 0x1c on wrap, else 0x02
C9E3: B4 46           LDY     $46,X               ; {hard.workRam+46}
C9E5: C8              INY                         
C9E6: D0 02           BNE     $C9EA               ; {code.loc_c9ea}
C9E8: A9 1C           LDA     #$1C                

loc_c9ea:
C9EA: 85 02           STA     $02                 ; {hard.workRam+2} queue it as the pending mode
C9EC: A9 0A           LDA     #$0A                ; request the pacing mode 0x0a
C9EE: 85 00           STA     $00                 ; {hard.workRam}

loc_c9f0:
C9F0: 60              RTS                         

; scan the zero-page window loc_46[loc_3e..0] for its maximum, store it
; decremented-once (when nonzero) into loc_126, and set the mode-request
; cell loc_0 to 0x14 (or 0x10 when the status byte loc_5 is negative).
reloadPacingFromPeakSlot:
C9F1: A9 00           LDA     #$00                ; reset the running peak
C9F3: 8D 26 01        STA     $0126               ; {hard.workRam+126}
C9F6: A6 3E           LDX     $3E                 ; {hard.workRam+3E} scan from the top live slot down

loc_c9f8:
C9F8: B5 46           LDA     $46,X               ; {hard.workRam+46} keep the highest per-slot level seen
C9FA: CD 26 01        CMP     $0126               ; {hard.workRam+126}
C9FD: 90 03           BCC     $CA02               ; {code.loc_ca02}
C9FF: 8D 26 01        STA     $0126               ; {hard.workRam+126}

loc_ca02:
CA02: CA              DEX                         ; across the whole live window
CA03: 10 F3           BPL     $C9F8               ; {code.loc_c9f8}
CA05: AC 26 01        LDY     $0126               ; {hard.workRam+126} seed the pacing floor with peak-1 -- zero stays zero
CA08: F0 03           BEQ     $CA0D               ; {code.loc_ca0d}
CA0A: CE 26 01        DEC     $0126               ; {hard.workRam+126}

loc_ca0d:
CA0D: A9 14           LDA     #$14                ; pick the next mode -- 0x10 when the status byte is negative, else 0x14
CA0F: 24 05           BIT     $05                 ; {hard.workRam+5}
CA11: 10 02           BPL     $CA15               ; {code.loc_ca15}
CA13: A9 10           LDA     #$10                

loc_ca15:
CA15: 85 00           STA     $00                 ; {hard.workRam} request it
CA17: 60              RTS                         

; alternate state-entry seeder: mask loc_5 to its low six bits (clearing
; the top two flag bits), then write loc_3e=0x00, loc_2=0x1a, loc_0=0x0a,
; loc_4=0xa0, loc_16b=0x01 and loc_1=0x0a.
seedModeParamsFromMaskedFlags:
CA18: A5 05           LDA     $05                 ; {hard.workRam+5} load the status flags
CA1A: 29 3F           AND     #$3F                ; keep only the low six gating bits -- clear the play/active-state flags
CA1C: 85 05           STA     $05                 ; {hard.workRam+5} store the masked status back
CA1E: A9 00           LDA     #$00                
CA20: 85 3E           STA     $3E                 ; {hard.workRam+3E} clear the active-slot count
CA22: A9 1A           LDA     #$1A                
CA24: 85 02           STA     $02                 ; {hard.workRam+2} queue the mode to promote once the delay expires
CA26: A9 0A           LDA     #$0A                
CA28: 85 00           STA     $00                 ; {hard.workRam} set the live game mode
CA2A: A9 A0           LDA     #$A0                
CA2C: 85 04           STA     $04                 ; {hard.workRam+4} arm the mode-promotion countdown
CA2E: A9 01           LDA     #$01                
CA30: 8D 6B 01        STA     $016B               ; {hard.workRam+16B} arm the guard holding the pending transition
CA33: A9 0A           LDA     #$0A                
CA35: 85 01           STA     $01                 ; {hard.workRam+1} set the pre-doubled dispatch selector paired with the mode
CA37: 60              RTS                         

; ---- $CA38-$CA47: data ----
CA38: 80 40 20 10 08 04 02 01 01 02 04 08 10 20 40 80

; choose the projection scale and mode bit from gates loc_117/loc_3d:
; default value 0x00/scale 0x10, but when both gates are nonzero value
; 0x04/scale 0x08; copy bit2 of the value into flag loc_a1 (preserving the
; rest) and store the scale into loc_b4.
selectProjectionScale:
CA48: A0 10           LDY     #$10                ; default projection scale
CA4A: AD 17 01        LDA     $0117               ; {hard.workRam+117} read the spinner heartbeat flag
CA4D: F0 08           BEQ     $CA57               ; {code.loc_ca57} skip the alternate regime if the flag is clear
CA4F: A5 3D           LDA     $3D                 ; {hard.workRam+3D} read the active seat
CA51: F0 04           BEQ     $CA57               ; {code.loc_ca57} skip the alternate regime if no live seat
CA53: A9 04           LDA     #$04                ; alternate mode-bit source
CA55: A0 08           LDY     #$08                ; alternate projection scale

loc_ca57:
CA57: 45 A1           EOR     $A1                 ; {hard.workRam+A1} masked bit-merge -- fold only bit 2 of the chosen value into the vector-mode flag
CA59: 29 04           AND     #$04                
CA5B: 45 A1           EOR     $A1                 ; {hard.workRam+A1}
CA5D: 85 A1           STA     $A1                 ; {hard.workRam+A1} store the updated vector-mode flag
CA5F: 84 B4           STY     $B4                 ; {hard.workRam+B4} publish the projection scale for the depth math
CA61: 60              RTS                         

; zero the six-byte working block loc_40..loc_45 (a pre-clear used before
; that block is staged with fresh channel entries).
clearChannelStagingBlock:
CA62: A9 00           LDA     #$00                ; value to write
CA64: A2 05           LDX     #$05                ; index over the six staging cells

loc_ca66:
CA66: 95 40           STA     $40,X               ; {hard.workRam+40} zero one sound-request staging cell
CA68: CA              DEX                         
CA69: 10 FB           BPL     $CA66               ; {code.loc_ca66} loop until the whole staging block is blank
CA6B: 60              RTS                         

; add a three-byte BCD amount into the score triplet at
; loc_40/loc_41/loc_42 (offset 0 when loc_3d==0 else 3) using fixed table
; bytes $CAF1+x/$CAF9+x when index x<0x08 else the live operand triplet
; loc_29/loc_2a/loc_2b, then range-check against threshold loc_156; on
; qualifying, if the per-slot counter loc_48+loc_3d is under 0x06 bump it,
; fire sound 0x4f via requestSoundIfEnabled and set loc_124=0x20; gated
; off unless loc_5 bit7 is set.
addBcdScoreAndAwardAtThreshold:
CA6C: F8              SED                         ; switch to BCD arithmetic for the score add
CA6D: 24 05           BIT     $05                 ; {hard.workRam+5} test the scoring-armed flag -- bit 7 of the status byte
CA6F: 10 7E           BPL     $CAEF               ; {code.loc_caef} bail out unless scoring is armed
CA71: A4 3D           LDY     $3D                 ; {hard.workRam+3D} read the active seat
CA73: F0 02           BEQ     $CA77               ; {code.loc_ca77}
CA75: A0 03           LDY     #$03                ; player-two score bank offset

loc_ca77:
CA77: E0 08           CPX     #$08                ; small index selects a fixed point value, else the live operand triplet
CA79: 90 16           BCC     $CA91               ; {code.loc_ca91} branch to the fixed score-value table path
CA7B: A5 29           LDA     $29                 ; {hard.workRam+29} live operand low byte
CA7D: 18              CLC                         
CA7E: 79 40 00        ADC     $0040,Y             ; {hard.workRam+40} add it into the score low byte
CA81: 99 40 00        STA     $0040,Y             ; {hard.workRam+40} store the running score low byte
CA84: A5 2A           LDA     $2A                 ; {hard.workRam+2A} live operand mid byte
CA86: 79 41 00        ADC     $0041,Y             ; {hard.workRam+41} add into the score mid byte with carry
CA89: 99 41 00        STA     $0041,Y             ; {hard.workRam+41} store the running score mid byte
CA8C: A5 2B           LDA     $2B                 ; {hard.workRam+2B} live operand high byte
CA8E: B8              CLV                         
CA8F: 50 15           BVC     $CAA6               ; {code.loc_caa6}

loc_ca91:
CA91: BD F1 CA        LDA     $CAF1,X             ; {hard.rom+3AF1} low byte of the point value from the score-value table
CA94: 18              CLC                         
CA95: 79 40 00        ADC     $0040,Y             ; {hard.workRam+40} add into the score low byte
CA98: 99 40 00        STA     $0040,Y             ; {hard.workRam+40} store the running score low byte
CA9B: BD F9 CA        LDA     $CAF9,X             ; {hard.rom+3AF9} high byte of the point value from the score-value table
CA9E: 79 41 00        ADC     $0041,Y             ; {hard.workRam+41} add into the score mid byte with carry
CAA1: 99 41 00        STA     $0041,Y             ; {hard.workRam+41} store the running score mid byte
CAA4: A9 00           LDA     #$00                ; fixed-table value has no third byte

loc_caa6:
CAA6: 08              PHP                         
CAA7: 79 42 00        ADC     $0042,Y             ; {hard.workRam+42} add the third byte into the score high cell with carry
CAAA: 99 42 00        STA     $0042,Y             ; {hard.workRam+42} store the running score high byte
CAAD: 28              PLP                         
CAAE: F0 0B           BEQ     $CABB               ; {code.loc_cabb}
CAB0: AE 56 01        LDX     $0156               ; {hard.workRam+156} read the bonus-life interval
CAB3: F0 06           BEQ     $CABB               ; {code.loc_cabb}
CAB5: E4 2B           CPX     $2B                 ; {hard.workRam+2B} compare it against the operand high byte
CAB7: F0 23           BEQ     $CADC               ; {code.loc_cadc} exact landing -- grant the award
CAB9: 90 21           BCC     $CADC               ; {code.loc_cadc}

loc_cabb:
CABB: 90 32           BCC     $CAEF               ; {code.loc_caef}
CABD: AE 56 01        LDX     $0156               ; {hard.workRam+156} reload the bonus-life interval
CAC0: F0 2C           BEQ     $CAEE               ; {code.loc_caee}
CAC2: E0 03           CPX     #$03                ; tiny interval takes a direct compare, else repeated subtraction
CAC4: 90 0B           BCC     $CAD1               ; {code.loc_cad1}

loc_cac6:
CAC6: 38              SEC                         ; repeatedly subtract the bonus interval from the score high byte
CAC7: ED 56 01        SBC     $0156               ; {hard.workRam+156}
CACA: F0 10           BEQ     $CADC               ; {code.loc_cadc} exact multiple of the interval -- grant the award
CACC: B0 F8           BCS     $CAC6               ; {code.loc_cac6} keep subtracting while it still fits
CACE: B8              CLV                         
CACF: 50 1D           BVC     $CAEE               ; {code.loc_caee}

loc_cad1:
CAD1: E0 02           CPX     #$02                
CAD3: D0 07           BNE     $CADC               ; {code.loc_cadc}
CAD5: 29 01           AND     #$01                
CAD7: F0 03           BEQ     $CADC               ; {code.loc_cadc}
CAD9: B8              CLV                         
CADA: 50 12           BVC     $CAEE               ; {code.loc_caee}

loc_cadc:
CADC: A6 3D           LDX     $3D                 ; {hard.workRam+3D} read the active seat
CADE: B5 48           LDA     $48,X               ; {hard.workRam+48} load this seat's bonus-life counter
CAE0: C9 06           CMP     #$06                ; cap the counter at six
CAE2: B0 0A           BCS     $CAEE               ; {code.loc_caee} skip the award if already at the cap
CAE4: F6 48           INC     $48,X               ; {hard.workRam+48} grant the extra life -- bump the counter
CAE6: 20 B9 CC        JSR     $CCB9               ; {code.requestScoreAwardSound} fire the score-award chime
CAE9: A9 20           LDA     #$20                
CAEB: 8D 24 01        STA     $0124               ; {hard.workRam+124} kick the rim colour animation

loc_caee:
CAEE: 38              SEC                         

loc_caef:
CAEF: D8              CLD                         ; back to binary arithmetic
CAF0: 60              RTS                         

; ---- $CAF1-$CCAF: data ----
CAF1: 00 50 00 00 50 50 00 50 00 01 02 01 00 02 05 07
CB01: 00 00 00 00 00 00 00 00 35 38 00 00 00 00 00 00
CB11: 00 00 47 4A 00 00 00 00 00 00 00 00 00 00 00 00
CB21: 00 00 00 00 0D 10 00 00 00 00 00 00 00 00 00 00
CB31: 00 00 00 00 00 00 00 00 00 00 65 68 00 00 00 00
CB41: 00 00 00 00 00 00 21 32 00 00 00 00 00 00 00 00
CB51: 13 1A 00 00 00 00 00 00 00 00 00 00 00 00 00 00
CB61: 00 00 00 00 00 00 00 00 00 00 53 56 00 00 00 00
CB71: 00 00 00 00 00 00 00 00 00 00 59 5C 00 00 00 00
CB81: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 3B 3E
CB91: 00 00 00 00 00 00 00 00 00 00 00 00 41 44 00 00
CBA1: 4D 50 00 00 00 00 00 00 00 00 00 00 00 00 00 00
CBB1: 5F 62 00 00 00 00 00 00 00 00 00 00 00 00 00 00
CBC1: 00 00 00 00 00 00 00 00 00 00 6D 6D 00 00 00 00
CBD1: C0 08 04 10 00 00 A6 20 F8 04 00 00 40 08 04 10
CBE1: 00 00 A6 20 FE 04 00 00 10 01 07 20 00 00 A2 01
CBF1: F8 20 00 00 08 04 20 0A 08 04 01 09 10 0D 04 0C
CC01: 00 00 08 04 00 0A 68 04 00 09 68 12 FF 09 00 00
CC11: 40 01 00 01 40 01 FF 40 30 01 FF 30 20 01 FF 20
CC21: 18 01 FF 18 14 01 FF 14 12 01 FF 12 10 01 FF 10
CC31: 00 00 A8 93 00 02 00 00 0F 04 00 01 00 00 A2 04
CC41: 40 01 00 00 00 03 02 09 00 00 08 03 FF 09 00 00
CC51: 80 01 E8 05 00 00 A1 01 01 05 00 00 01 08 02 10
CC61: 00 00 86 20 00 04 00 00 18 04 00 FF 00 00 AF 04
CC71: 00 FF 00 00 C0 02 FF FF 00 00 28 02 00 F0 00 00
CC81: 10 0B 01 40 00 00 86 40 00 0B 00 00 20 80 00 03
CC91: 00 00 A8 40 F8 06 00 00 B0 02 00 FF 00 00 C8 01
CCA1: 02 FF C8 01 02 FF 00 00 C0 01 00 01 00 00 00

; cue the fixed sound id 0x5f through the sound gate, carrying the
; caller's X/Y.
gateSound5f:
CCB0: A9 5F           LDA     #$5F                ; sound id -- fixed effect 0x5f
CCB2: 4C C3 CC        JMP     $CCC3               ; {code.requestSoundIfEnabled} hand it to the sound-enable gate

; load fixed sound id 0x0f and pass it through the sound gate $CCC3
; (keeping caller X/Y); rung by $9749 when the coarse rim angle changes,
; i.e. the spinner-rotation sound cue.
cueRimRotationSound:
CCB5: A9 0F           LDA     #$0F                ; sound id -- rim-rotation click
CCB7: D0 0A           BNE     $CCC3               ; {code.requestSoundIfEnabled} branch into the enable gate

; one-line cue: request fixed sound id 0x4f through the enable gate $CCC3;
; caller $C98C fires it on the bonus/level-advance handler chain, and the
; same id 0x4f is fired by the score-award path $CA6C, so it voices a
; score/bonus award.
requestScoreAwardSound:
CCB9: A9 4F           LDA     #$4F                ; sound id -- score-award chime
CCBB: D0 06           BNE     $CCC3               ; {code.requestSoundIfEnabled} branch into the enable gate

; cue the fixed sound id 0x8f through the sound gate, carrying the
; caller's X/Y.
gateSound8f:
CCBD: A9 8F           LDA     #$8F                ; sound id -- effect 0x8f
CCBF: D0 02           BNE     $CCC3               ; {code.requestSoundIfEnabled} branch into the enable gate

; cue the fixed sound id 0x1f through the sound gate, carrying the
; caller's X/Y.
gateSound1f:
CCC1: A9 1F           LDA     #$1F                ; sound id -- enemy-spawn cue

; sound enable gate: only when bit7 of the enable flag loc_5 is set,
; forward the sound id in A (with X/Y) to the loader loadSoundVoiceSlots;
; with sound disabled it returns making no write.
requestSoundIfEnabled:
CCC3: 24 05           BIT     $05                 ; {hard.workRam+5} test the sound-enable flag -- bit 7 of the status byte
CCC5: 10 22           BPL     $CCE9               ; {code.loc_cce9} muted: drop the cue and return

; sound loader: stash caller X/Y into loc_31/loc_32, read the sound's row
; of bytes from $CB01 by descending id, and for each nonzero table byte
; claim its slot -- mark slot in loc_bf, write the byte to loc_c0,x, set
; fast/slow flags loc_e0,x and loc_f0,x to 1, then restore the 0xff
; sentinel to loc_bf.
loadSoundVoiceSlots:
CCC7: 86 31           STX     $31                 ; {hard.workRam+31} stash the caller's X/Y
CCC9: 84 32           STY     $32                 ; {hard.workRam+32}
CCCB: A8              TAY                         ; sound id becomes the starting index into the voice table
CCCC: A2 0F           LDX     #$0F                ; walk all sixteen voice slots

loc_ccce:
CCCE: B9 01 CB        LDA     $CB01,Y             ; {hard.rom+3B01} read this slot's byte from the voice table
CCD1: F0 0E           BEQ     $CCE1               ; {code.loc_cce1} zero byte is a gap -- leave the slot untouched
CCD3: 86 BF           STX     $BF                 ; {hard.workRam+BF} mark the slot being claimed
CCD5: 95 C0           STA     $C0,X               ; {hard.workRam+C0} load the voice value into the slot
CCD7: A9 01           LDA     #$01                
CCD9: 95 E0           STA     $E0,X               ; {hard.workRam+E0} arm the fast timer
CCDB: 95 F0           STA     $F0,X               ; {hard.workRam+F0} arm the slow timer
CCDD: A9 FF           LDA     #$FF                
CCDF: 85 BF           STA     $BF                 ; {hard.workRam+BF} restore the idle sentinel

loc_cce1:
CCE1: 88              DEY                         
CCE2: CA              DEX                         
CCE3: 10 E9           BPL     $CCCE               ; {code.loc_ccce} loop over the remaining slots
CCE5: A6 31           LDX     $31                 ; {hard.workRam+31} restore the caller's X/Y
CCE7: A4 32           LDY     $32                 ; {hard.workRam+32}

loc_cce9:
CCE9: 60              RTS                         

; one-line cue: request fixed sound id 0x2f through the enable gate $CCC3,
; forwarding slot index X; its sole caller is the enemy spawner $A23F, so
; it voices a new enemy entering the tube.
requestEnemySpawnSound:
CCEA: A9 2F           LDA     #$2F                ; sound id -- new enemy entering the tube
CCEC: D0 D5           BNE     $CCC3               ; {code.requestSoundIfEnabled} branch into the enable gate

; register the fixed sound id 0x6f through the sound-enable gate $CCC3 --
; the moving spike's start cue, fired by $97F8 at trigger height
; loc_202==0x10.
cueMovingSpikeStartSound:
CCEE: A9 6F           LDA     #$6F                ; sound id -- moving-spike start cue
CCF0: D0 D1           BNE     $CCC3               ; {code.requestSoundIfEnabled} branch into the enable gate

; register the fixed sound id 0x7f through the sound-enable gate $CCC3 --
; the moving spike's end cue, fired by $97F8 when the height overflows the
; ceiling.
cueMovingSpikeEndSound:
CCF2: A9 7F           LDA     #$7F                ; sound id -- moving-spike end cue
CCF4: D0 CD           BNE     $CCC3               ; {code.requestSoundIfEnabled} branch into the enable gate

; one-line cue: request fixed sound id 0x9f through the enable gate $CCC3,
; forwarding X/Y; its sole caller is the per-slot hit/award routine $A1FA,
; so it chimes when a segment/enemy is hit.
requestSegmentHitSound:
CCF6: A9 9F           LDA     #$9F                ; sound id -- segment-hit chime
CCF8: D0 C9           BNE     $CCC3               ; {code.requestSoundIfEnabled} branch into the enable gate

; request fixed sound id 0xaf by jumping straight into the loader $CCC7,
; bypassing the enable gate; the frame dispatcher $C891 calls it every
; frame while loc_c is live, so it (re)voices the currently-active held
; cue regardless of the loc_5 enable flag.
requestActiveSoundCue:
CCFA: A9 AF           LDA     #$AF                ; sound id -- currently-held active cue
CCFC: D0 C9           BNE     $CCC7               ; {code.loadSoundVoiceSlots} branch straight to the voice loader -- bypass the enable gate

; one-line cue: request fixed sound id 0xbf through the enable gate $CCC3;
; its sole caller $90C4 fires it at phase 3 of the start-slot pick / wave
; working-set reseed, so it voices the level-intro / skill-step start.
requestLevelIntroSound:
CCFE: A9 BF           LDA     #$BF                ; sound id -- level-intro / skill-step start
CD00: D0 C1           BNE     $CCC3               ; {code.requestSoundIfEnabled} branch into the enable gate

; one-line cue: request fixed sound id 0x3f through the enable gate $CCC3,
; threading X; its sole caller $9B1E fires it as a correction when the
; per-slot motion accumulator loc_148 sign-flips, so it voices an enemy
; direction reversal on the rim.
requestMotionFlipSound:
CD02: A9 3F           LDA     #$3F                ; load fixed sound id 0x3f -- the enemy direction-reversal cue on the rim
CD04: D0 BD           BNE     $CCC3               ; {code.requestSoundIfEnabled} hand the id to the sound-enable gate -- queued only while sound is on

; register the fixed sound id 0xcf through the sound-enable gate $CCC3,
; threading X/Y -- the spike-collision cue fired by $97F8 when the spike
; reaches the player segment.
cueSpikeCollisionSound:
CD06: A9 CF           LDA     #$CF                ; load fixed sound id 0xcf -- the spike-strikes-blaster hit
CD08: D0 B9           BNE     $CCC3               ; {code.requestSoundIfEnabled} hand the id to the sound-enable gate

; per-frame voice engine: scan 16 slots 0x0f..0, skip idle slots
; (loc_c0,x==0) and the reserved slot loc_bf; decrement fast timer
; loc_e0,x then slow timer loc_f0,x, step the slot through the $CBCC/$CCCC
; animation tables (single step, or walk to a nonzero frame when both
; expire), fold the result into level byte loc_d0,x (odd slots keep the
; prior high nibble), and publish loc_d0,x to POKEY audio register $60C0+x
; for slots<8 or $60C8+x for the upper slots.
stepSoundVoices:
CD0A: A2 0F           LDX     #$0F                ; start at sound slot 15 and walk down to 0

loc_cd0c:
CD0C: B5 C0           LDA     $C0,X               ; {hard.workRam+C0} read this slot's envelope pointer
CD0E: F0 7E           BEQ     $CD8E               ; {code.loc_cd8e} skip an idle slot (pointer 0)
CD10: E4 BF           CPX     $BF                 ; {hard.workRam+BF} is this the reserved slot
CD12: F0 7A           BEQ     $CD8E               ; {code.loc_cd8e} skip the reserved slot
CD14: D6 E0           DEC     $E0,X               ; {hard.workRam+E0} age the slot's fast timer
CD16: D0 76           BNE     $CD8E               ; {code.loc_cd8e} still running -- nothing more for this slot this frame
CD18: D6 F0           DEC     $F0,X               ; {hard.workRam+F0} fast timer expired -- age the slow timer too
CD1A: D0 38           BNE     $CD54               ; {code.loc_cd54} slow timer still running -- take a single envelope step

loc_cd1c:
CD1C: F6 C0           INC     $C0,X               ; {hard.workRam+C0} both timers expired: advance the envelope pointer by two
CD1E: F6 C0           INC     $C0,X               ; {hard.workRam+C0} (second half of the two-step advance to the next frame)
CD20: B5 C0           LDA     $C0,X               ; {hard.workRam+C0} reload the envelope pointer
CD22: 0A              ASL     A                   ; double it into a word-stride table index
CD23: A8              TAY                         
CD24: B0 10           BCS     $CD36               ; {code.loc_cd36} top bit set -- read the frame from the high envelope table
CD26: B9 CB CB        LDA     $CBCB,Y             ; {hard.rom+3BCB} low table: load the frame's level byte
CD29: 95 D0           STA     $D0,X               ; {hard.workRam+D0} store it as the slot's level
CD2B: B9 CE CB        LDA     $CBCE,Y             ; {hard.rom+3BCE} load the frame's slow-timer reload
CD2E: 95 F0           STA     $F0,X               ; {hard.workRam+F0} store the slow timer
CD30: B9 CC CB        LDA     $CBCC,Y             ; {hard.rom+3BCC} load the frame's fast-timer reload
CD33: B8              CLV                         
CD34: 50 0D           BVC     $CD43               ; {code.loc_cd43}

loc_cd36:
CD36: B9 CB CC        LDA     $CCCB,Y             ; {hard.rom+3CCB} high table: load the frame's level byte
CD39: 95 D0           STA     $D0,X               ; {hard.workRam+D0} store it as the slot's level
CD3B: B9 CE CC        LDA     $CCCE,Y             ; {hard.rom+3CCE} load the frame's slow-timer reload
CD3E: 95 F0           STA     $F0,X               ; {hard.workRam+F0} store the slow timer
CD40: B9 CC CC        LDA     $CCCC,Y             ; {hard.rom+3CCC} load the frame's fast-timer reload

loc_cd43:
CD43: 95 E0           STA     $E0,X               ; {hard.workRam+E0} store the fast timer
CD45: D0 0A           BNE     $CD51               ; {code.loc_cd51} nonzero fast timer -- a real frame, publish it
CD47: 95 C0           STA     $C0,X               ; {hard.workRam+C0} zero fast timer: park the envelope pointer at 0
CD49: B5 D0           LDA     $D0,X               ; {hard.workRam+D0} reload the level byte
CD4B: F0 04           BEQ     $CD51               ; {code.loc_cd51} level 0 is a terminator -- publish
CD4D: 95 C0           STA     $C0,X               ; {hard.workRam+C0} otherwise treat the level as the next pointer
CD4F: D0 CB           BNE     $CD1C               ; {code.loc_cd1c} keep walking the envelope

loc_cd51:
CD51: B8              CLV                         
CD52: 50 2B           BVC     $CD7F               ; {code.loc_cd7f}

loc_cd54:
CD54: 0A              ASL     A                   ; single-step path: double the pointer into a table index
CD55: A8              TAY                         
CD56: B0 0B           BCS     $CD63               ; {code.loc_cd63} top bit set -- read from the high envelope table
CD58: B9 CC CB        LDA     $CBCC,Y             ; {hard.rom+3BCC} low table: load the fast-timer reload
CD5B: 95 E0           STA     $E0,X               ; {hard.workRam+E0} reload the fast timer
CD5D: B9 CD CB        LDA     $CBCD,Y             ; {hard.rom+3BCD} load the level increment
CD60: B8              CLV                         
CD61: 50 08           BVC     $CD6B               ; {code.loc_cd6b}

loc_cd63:
CD63: B9 CC CC        LDA     $CCCC,Y             ; {hard.rom+3CCC} high table: load the fast-timer reload
CD66: 95 E0           STA     $E0,X               ; {hard.workRam+E0} reload the fast timer
CD68: B9 CD CC        LDA     $CCCD,Y             ; {hard.rom+3CCD} load the level increment

loc_cd6b:
CD6B: B4 D0           LDY     $D0,X               ; {hard.workRam+D0} fetch the running level
CD6D: 18              CLC                         
CD6E: 75 D0           ADC     $D0,X               ; {hard.workRam+D0} add the increment into the running level
CD70: 95 D0           STA     $D0,X               ; {hard.workRam+D0} store the stepped level
CD72: 8A              TXA                         
CD73: 4A              LSR     A                   ; test whether this is an odd slot
CD74: 90 09           BCC     $CD7F               ; {code.loc_cd7f} even slot -- publish as is
CD76: 98              TYA                         
CD77: 55 D0           EOR     $D0,X               ; {hard.workRam+D0} odd slot: preserve the prior high nibble of the level byte
CD79: 29 F0           AND     #$F0                ; (mask off the low nibble of the delta)
CD7B: 55 D0           EOR     $D0,X               ; {hard.workRam+D0} (merge back the retained high nibble)
CD7D: 95 D0           STA     $D0,X               ; {hard.workRam+D0} store the merged level

loc_cd7f:
CD7F: B5 D0           LDA     $D0,X               ; {hard.workRam+D0} load the slot's level to publish
CD81: E0 08           CPX     #$08                ; slots below 8 use the first sound chip
CD83: 90 06           BCC     $CD8B               ; {code.loc_cd8b}
CD85: 9D C8 60        STA     $60C8,X             ; {hard.pokey1+8} publish the level to the second sound chip's voice register
CD88: B8              CLV                         
CD89: 50 03           BVC     $CD8E               ; {code.loc_cd8e}

loc_cd8b:
CD8B: 9D C0 60        STA     $60C0,X             ; {hard.pokey1} publish the level to the first sound chip's voice register

loc_cd8e:
CD8E: CA              DEX                         ; step down to the next slot
CD8F: 30 03           BMI     $CD94               ; {code.loc_cd94} done all 16 slots
CD91: 4C 0C CD        JMP     $CD0C               ; {code.loc_cd0c} loop to the next slot

loc_cd94:
CD94: 60              RTS                         

; dual-POKEY reset: zero both serial-control regs $60CF/$60DF and the
; scratch flag loc_720, poll random regs $60CA/$60DA across five
; iterations latching the first sample into loc_720 the moment either
; changes, set both serial-control regs to 7, clear both chips' eight
; audio regs $60C0..7/$60D0..7 and the software arrays loc_c0,x/loc_d0,x,
; then zero both control regs $60C8/$60D8.
resetBothPokeyChips:
CD95: A9 00           LDA     #$00                
CD97: 8D CF 60        STA     $60CF               ; {hard.pokey1+F} hold the first sound chip in serial reset (control latch 0)
CD9A: 8D DF 60        STA     $60DF               ; {hard.pokey2+F} hold the second sound chip in serial reset
CD9D: 8D 20 07        STA     $0720               ; {hard.workRam+720} clear the random-seed scratch cell
CDA0: A2 04           LDX     #$04                ; poll the entropy registers up to five times
CDA2: AD CA 60        LDA     $60CA               ; {hard.pokey1+A} snapshot the first chip's free-running random register
CDA5: AC DA 60        LDY     $60DA               ; {hard.pokey2+A} snapshot the second chip's random register

loc_cda8:
CDA8: CD CA 60        CMP     $60CA               ; {hard.pokey1+A} has the first chip's random register advanced
CDAB: D0 03           BNE     $CDB0               ; {code.loc_cdb0}
CDAD: CC DA 60        CPY     $60DA               ; {hard.pokey2+A} has the second chip's advanced

loc_cdb0:
CDB0: F0 05           BEQ     $CDB7               ; {code.loc_cdb7} neither moved -- keep polling
CDB2: 8D 20 07        STA     $0720               ; {hard.workRam+720} one moved -- latch the snapshot as the random seed
CDB5: A2 00           LDX     #$00                ; stop polling

loc_cdb7:
CDB7: CA              DEX                         
CDB8: 10 EE           BPL     $CDA8               ; {code.loc_cda8}
CDBA: A9 07           LDA     #$07                ; release value for the serial-control latch
CDBC: 8D CF 60        STA     $60CF               ; {hard.pokey1+F} release the first chip (control latch 7, the init handshake)
CDBF: 8D DF 60        STA     $60DF               ; {hard.pokey2+F} release the second chip
CDC2: A2 07           LDX     #$07                ; walk the eight audio registers of each chip
CDC4: A9 00           LDA     #$00                

loc_cdc6:
CDC6: 9D C0 60        STA     $60C0,X             ; {hard.pokey1} silence a first-chip audio register
CDC9: 9D D0 60        STA     $60D0,X             ; {hard.pokey2} silence a second-chip audio register
CDCC: 95 C0           STA     $C0,X               ; {hard.workRam+C0} clear the slot's software voice-value mirror
CDCE: 95 D0           STA     $D0,X               ; {hard.workRam+D0} clear the slot's software voice-level mirror
CDD0: CA              DEX                         
CDD1: 10 F3           BPL     $CDC6               ; {code.loc_cdc6}
CDD3: A9 00           LDA     #$00                
CDD5: 8D C8 60        STA     $60C8               ; {hard.pokey1+8} clear the first chip's control register
CDD8: A9 00           LDA     #$00                
CDDA: 8D D8 60        STA     $60D8               ; {hard.pokey2+8} clear the second chip's control register
CDDD: 60              RTS                         

; ---- $CDDE-$CF23: data ----
CDDE: 0B 5D 22 74 0C 5E 34 50 00 71 C5 68 40 80 6C 01
CDEE: 40 1E 00 71 B4 A8 B4 A8 B4 A8 B4 A8 B4 A8 65 A8
CDFE: 00 00 70 1F 00 71 00 58 C1 68 3F A9 3F A9 3F A9
CE0E: 3F A9 3F A9 3F A9 30 00 D0 1F C5 68 B4 A8 B4 A8
CE1E: B4 A8 B4 A8 B4 A8 B4 A8 DC 1F 00 00 C7 68 B4 A8
CE2E: B4 A8 C5 68 24 00 E8 1F B4 A8 B4 A8 B4 A8 00 71
CE3E: E0 1F 28 00 00 71 B4 A8 B4 A8 B4 A8 B4 A8 B4 A8
CE4E: 65 A8 00 00 70 1F 00 71 00 58 C1 68 3F A9 3F A9
CE5E: 3F A9 3F A9 3F A9 3F A9 55 7F 06 20 02 22 0C 24
CE6E: 92 26 00 29 56 2A D8 2C BE 2D 24 2E 04 21 06 23
CE7E: 4E 25 C8 27 AA 29 96 2B 4A 2D F0 2D A6 2E 04 20
CE8E: 00 22 0A 24 90 26 FE 28 54 2A D6 2C BC 2D 22 2E
CE9E: 03 E0 01 E1 06 E2 49 E3 80 E4 2B E5 6C E6 DF E6
CEAE: 12 E7 82 E0 83 E1 A7 E2 E4 E3 D5 E4 CB E5 A5 E6
CEBE: F8 E6 53 E7 DA EE E4 EE E6 EE 61 AA 7C AA 91 AA
CECE: AD AA CA AA 14 AB 6F AB C0 AB 15 AC 66 AC 7D AC
CEDE: 94 AC AB AC D8 AC FA AC 0D AD 20 AD 39 AD 51 AD
CEEE: 6A AD 8C AD 8A AD 88 AD 86 AD 84 AD 82 AD 86 AD
CEFE: 8A AD 8C AD D7 AD C2 AD C5 AD C8 AD CB AD CE AD
CF0E: D1 AD D4 AD C2 AC CB AC 35 AE 59 AE 7E AE A2 AE
CF1E: C5 AE CB AE D2 AE

; on every interrupt advance the three timebase counter lanes gated by
; loc_8: step each enabled lane's wrapped position loc_d/loc_e/loc_f
; (masked to 0x1f, wrapping the 0x20 boundary), run its down-timer
; loc_10,x (reload 0x78 on zero), fold a small per-lane increment into the
; running accumulator pair loc_16/loc_17 and bump counter loc_13,x; then
; subtract a $CFD9-table amount from loc_16 (advancing overflow tally
; loc_18), nudge loc_6, store loc_17, and run two clamp passes over the
; loc_13 triple.
tickHeartbeatCounters:
CF24: A2 02           LDX     #$02                ; step the three timebase lanes, x = 2,1,0

loc_cf26:
CF26: AD 08 00        LDA     $0008               ; {hard.workRam+8} read the latched input port for this lane's control bits
CF29: E0 01           CPX     #$01                
CF2B: F0 03           BEQ     $CF30               ; {code.loc_cf30}
CF2D: B0 02           BCS     $CF31               ; {code.loc_cf31}
CF2F: 4A              LSR     A                   ; shift out this lane's control bits

loc_cf30:
CF30: 4A              LSR     A                   

loc_cf31:
CF31: 4A              LSR     A                   
CF32: B5 0D           LDA     $0D,X               ; {hard.workRam+D} load this lane's wrapped position
CF34: 29 1F           AND     #$1F                ; mask to the 0..0x1f rail
CF36: B0 37           BCS     $CF6F               ; {code.loc_cf6f} control bit set -- take the wrap-up path
CF38: F0 10           BEQ     $CF4A               ; {code.loc_cf4a} position at 0 -- store as-is
CF3A: C9 1B           CMP     #$1B                ; near the top rail
CF3C: B0 0A           BCS     $CF48               ; {code.loc_cf48}
CF3E: A8              TAY                         
CF3F: A5 07           LDA     $07                 ; {hard.workRam+7} read the interrupt sub-timer
CF41: 29 07           AND     #$07                ; take its low phase
CF43: C9 07           CMP     #$07                ; pace the step to sub-timer phase 7
CF45: 98              TYA                         
CF46: 90 02           BCC     $CF4A               ; {code.loc_cf4a}

loc_cf48:
CF48: E9 01           SBC     #$01                ; decrement the position with borrow

loc_cf4a:
CF4A: 95 0D           STA     $0D,X               ; {hard.workRam+D} store the updated lane position
CF4C: AD 08 00        LDA     $0008               ; {hard.workRam+8} test input bit 3
CF4F: 29 08           AND     #$08                
CF51: D0 04           BNE     $CF57               ; {code.loc_cf57}
CF53: A9 F0           LDA     #$F0                ; prime the sound-step gate to 0xf0
CF55: 85 0C           STA     $0C                 ; {hard.workRam+C}

loc_cf57:
CF57: A5 0C           LDA     $0C                 ; {hard.workRam+C} read the sound-step gate
CF59: F0 08           BEQ     $CF63               ; {code.loc_cf63}
CF5B: C6 0C           DEC     $0C                 ; {hard.workRam+C} tick the sound-step gate down
CF5D: A9 00           LDA     #$00                
CF5F: 95 0D           STA     $0D,X               ; {hard.workRam+D} reset this lane's position on gate drain
CF61: 95 10           STA     $10,X               ; {hard.workRam+10} reset this lane's down-timer

loc_cf63:
CF63: 18              CLC                         
CF64: B5 10           LDA     $10,X               ; {hard.workRam+10} read the lane down-timer
CF66: F0 23           BEQ     $CF8B               ; {code.loc_cf8b}
CF68: D6 10           DEC     $10,X               ; {hard.workRam+10} decrement the down-timer
CF6A: D0 1F           BNE     $CF8B               ; {code.loc_cf8b}
CF6C: 38              SEC                         ; timer reached 0 -- flag an event tick
CF6D: B0 1C           BCS     $CF8B               ; {code.loc_cf8b}

loc_cf6f:
CF6F: C9 1B           CMP     #$1B                ; wrap-up path: position near the top rail
CF71: B0 09           BCS     $CF7C               ; {code.loc_cf7c}
CF73: B5 0D           LDA     $0D,X               ; {hard.workRam+D} load the position
CF75: 69 20           ADC     #$20                ; add 0x20 to the position
CF77: 90 D1           BCC     $CF4A               ; {code.loc_cf4a}
CF79: F0 01           BEQ     $CF7C               ; {code.loc_cf7c}
CF7B: 18              CLC                         

loc_cf7c:
CF7C: A9 1F           LDA     #$1F                ; rail the position at 0x1f
CF7E: B0 CA           BCS     $CF4A               ; {code.loc_cf4a}
CF80: 95 0D           STA     $0D,X               ; {hard.workRam+D} store the railed position
CF82: B5 10           LDA     $10,X               ; {hard.workRam+10} read the down-timer
CF84: F0 01           BEQ     $CF87               ; {code.loc_cf87}
CF86: 38              SEC                         

loc_cf87:
CF87: A9 78           LDA     #$78                ; reload the lane down-timer to 0x78
CF89: 95 10           STA     $10,X               ; {hard.workRam+10} store the reloaded down-timer

loc_cf8b:
CF8B: 90 2A           BCC     $CFB7               ; {code.loc_cfb7} no event this lane -- skip the accumulator fold
CF8D: A9 00           LDA     #$00                
CF8F: E0 01           CPX     #$01                ; select the increment by lane
CF91: 90 16           BCC     $CFA9               ; {code.loc_cfa9}
CF93: F0 0C           BEQ     $CFA1               ; {code.loc_cfa1}
CF95: A5 09           LDA     $09                 ; {hard.workRam+9} lane 2: take option bits 2-3 as the increment
CF97: 29 0C           AND     #$0C                
CF99: 4A              LSR     A                   
CF9A: 4A              LSR     A                   
CF9B: F0 0C           BEQ     $CFA9               ; {code.loc_cfa9}
CF9D: 69 02           ADC     #$02                ; bias the increment
CF9F: D0 08           BNE     $CFA9               ; {code.loc_cfa9}

loc_cfa1:
CFA1: A5 09           LDA     $09                 ; {hard.workRam+9} lane 1: option bit 4 selects
CFA3: 29 10           AND     #$10                
CFA5: F0 02           BEQ     $CFA9               ; {code.loc_cfa9}
CFA7: A9 01           LDA     #$01                ; a +1 increment

loc_cfa9:
CFA9: 38              SEC                         
CFAA: 48              PHA                         
CFAB: 65 16           ADC     $16                 ; {hard.workRam+16} fold the increment into the accumulator low byte
CFAD: 85 16           STA     $16                 ; {hard.workRam+16} store the accumulator low byte
CFAF: 68              PLA                         
CFB0: 38              SEC                         
CFB1: 65 17           ADC     $17                 ; {hard.workRam+17} carry into the accumulator high byte
CFB3: 85 17           STA     $17                 ; {hard.workRam+17} store the accumulator high byte
CFB5: F6 13           INC     $13,X               ; {hard.workRam+13} bump this lane's event counter

loc_cfb7:
CFB7: CA              DEX                         ; advance to the next lane
CFB8: 30 03           BMI     $CFBD               ; {code.loc_cfbd}
CFBA: 4C 26 CF        JMP     $CF26               ; {code.loc_cf26} loop to the next lane

loc_cfbd:
CFBD: A5 09           LDA     $09                 ; {hard.workRam+9} option top three bits index the reduction table
CFBF: 4A              LSR     A                   
CFC0: 4A              LSR     A                   
CFC1: 4A              LSR     A                   
CFC2: 4A              LSR     A                   
CFC3: 4A              LSR     A                   
CFC4: A8              TAY                         
CFC5: A5 16           LDA     $16                 ; {hard.workRam+16} load the accumulator low byte
CFC7: 38              SEC                         
CFC8: F9 D9 CF        SBC     $CFD9,Y             ; {hard.rom+3FD9} drain it by the option-indexed reduction amount
CFCB: 30 14           BMI     $CFE1               ; {code.loc_cfe1}
CFCD: 85 16           STA     $16                 ; {hard.workRam+16} store the drained low byte
CFCF: E6 18           INC     $18                 ; {hard.workRam+18} advance the overflow tally
CFD1: C0 03           CPY     #$03                ; at the maximum reduction index
CFD3: D0 0C           BNE     $CFE1               ; {code.loc_cfe1}
CFD5: E6 18           INC     $18                 ; {hard.workRam+18} advance the overflow tally a second time
CFD7: D0 08           BNE     $CFE1               ; {code.loc_cfe1}

; A short data table subtracted from a running value via `sbc $cfd9,y`
; (y=0..3) by the routine just above; a fall-through mis-decoded its first
; byte as an undefined opcode. Real code resumes at $cfe1.
; ---- $CFD9-$CFE0: data table ----
CFD9: 7F 02 04 04 05 03 7F 7F

loc_cfe1:
CFE1: A5 09           LDA     $09                 ; {hard.workRam+9} option low two bits select a high-byte correction
CFE3: 29 03           AND     #$03                
CFE5: A8              TAY                         
CFE6: F0 1A           BEQ     $D002               ; {code.loc_d002}
CFE8: 4A              LSR     A                   
CFE9: 69 00           ADC     #$00                
CFEB: 49 FF           EOR     #$FF                
CFED: 38              SEC                         
CFEE: 65 17           ADC     $17                 ; {hard.workRam+17} apply the correction to the accumulator high byte
CFF0: B0 08           BCS     $CFFA               ; {code.loc_cffa}
CFF2: 65 18           ADC     $18                 ; {hard.workRam+18} carry it through the overflow tally
CFF4: 30 0E           BMI     $D004               ; {code.loc_d004}
CFF6: 85 18           STA     $18                 ; {hard.workRam+18} store the overflow tally
CFF8: A9 00           LDA     #$00                

loc_cffa:
CFFA: C0 02           CPY     #$02                
CFFC: B0 02           BCS     $D000               ; {code.loc_d000}
CFFE: E6 06           INC     $06                 ; {hard.workRam+6} step the phase counter

loc_d000:
D000: E6 06           INC     $06                 ; {hard.workRam+6} step the phase counter again

loc_d002:
D002: 85 17           STA     $17                 ; {hard.workRam+17} commit the accumulator high byte

loc_d004:
D004: A5 07           LDA     $07                 ; {hard.workRam+7} gate the clamp passes on the sub-timer's low bit
D006: 4A              LSR     A                   
D007: B0 27           BCS     $D030               ; {code.loc_d030} odd sub-timer -- skip the clamp
D009: A0 00           LDY     #$00                
D00B: A2 02           LDX     #$02                ; first clamp pass over the three lane counters

loc_d00d:
D00D: B5 13           LDA     $13,X               ; {hard.workRam+13} read a lane counter
D00F: F0 09           BEQ     $D01A               ; {code.loc_d01a}
D011: C9 10           CMP     #$10                ; is it 0x10 or more
D013: 90 05           BCC     $D01A               ; {code.loc_d01a}
D015: 69 EF           ADC     #$EF                ; reduce it by 0x11
D017: C8              INY                         ; tally that a lane was reduced
D018: 95 13           STA     $13,X               ; {hard.workRam+13} store the reduced counter

loc_d01a:
D01A: CA              DEX                         
D01B: 10 F0           BPL     $D00D               ; {code.loc_d00d}
D01D: 98              TYA                         ; any lane reduced
D01E: D0 10           BNE     $D030               ; {code.loc_d030} yes -- skip the second pass
D020: A2 02           LDX     #$02                ; second clamp pass over the lane counters

loc_d022:
D022: B5 13           LDA     $13,X               ; {hard.workRam+13} read a lane counter
D024: F0 07           BEQ     $D02D               ; {code.loc_d02d}
D026: 18              CLC                         
D027: 69 EF           ADC     #$EF                ; reduce it by 0x11
D029: 95 13           STA     $13,X               ; {hard.workRam+13} store it
D02B: 30 03           BMI     $D030               ; {code.loc_d030} stop at the first that goes negative

loc_d02d:
D02D: CA              DEX                         
D02E: 10 F2           BPL     $D022               ; {code.loc_d022}

loc_d030:
D030: 60              RTS                         

; ---- $D031-$D6BA: data ----
D031: 5D D1 8F D1 8F D1 B1 D1 EB D1 03 D2 61 D2 CB D2
D041: 33 D3 66 D3 B0 D3 E6 D3 FF D3 17 D4 1D D4 34 D4
D051: 4C D4 60 D4 A1 D4 AB D4 EF D4 30 D5 75 D5 85 D5
D061: A1 D5 A8 D5 E9 D5 1C D6 62 D6 7A D6 67 D1 97 D1
D071: 97 D1 BD D1 F0 D1 17 D2 75 D2 E0 D2 3F D3 79 D3
D081: BE D3 E6 D3 FF D3 17 D4 22 D4 3A D4 51 D4 6D D4
D091: A1 D4 BA D4 FD D4 3F D5 75 D5 85 D5 A1 D5 B9 D5
D0A1: F6 D5 29 D6 68 D6 7A D6 75 D1 9F D1 9F D1 CF D1
D0B1: F6 D1 30 D2 94 D2 FB D2 50 D3 8B D3 CB D3 F5 D3
D0C1: 0E D4 17 D4 28 D4 41 D4 5B D4 83 D4 A1 D4 CC D4
D0D1: 0E D5 51 D5 75 D5 8E D5 A1 D5 C8 D5 04 D6 3E D6
D0E1: 6F D6 8F D6 7F D1 A8 D1 A8 D1 DE D1 FC D1 4D D2
D0F1: AE D2 16 D3 5E D3 A0 D3 DA D3 ED D3 06 D4 17 D4
D101: 2D D4 46 D4 56 D4 92 D4 A1 D4 DD D4 1F D5 63 D5
D111: 75 D5 97 D5 A1 D5 D9 D5 10 D6 51 D6 74 D6 A1 D6
D121: 51 56 00 1A 01 20 31 56 01 38 31 B0 41 00 11 F6
D131: 30 38 31 CE 51 0A 31 E2 31 E2 51 BA 51 98 51 D8
D141: 51 C9 31 56 51 80 51 80 51 80 51 80 71 92 51 80
D151: 31 B0 51 89 41 89 00 00 71 5A 71 A0 E5 22 16 2E
D161: 1E 00 32 40 1E B8 D9 20 26 30 00 1C 1E 00 34 16
D171: 38 3C 26 9E E5 3A 34 26 1E 2C 1E 30 1C 9E D3 28
D181: 3E 1E 22 32 00 3C 1E 38 2E 26 30 16 1C B2 CD 34
D191: 2C 16 46 1E 38 80 C6 28 32 3E 1E 3E 38 80 C6 3A
D1A1: 34 26 1E 2C 1E 38 80 C6 28 3E 22 16 1C 32 38 80
D1B1: DF 34 38 1E 3A 3A 00 3A 3C 16 38 BC CD 16 34 34
D1C1: 3E 46 1E 48 00 3A 3E 38 00 3A 3C 16 38 BC D6 3A
D1D1: 3C 16 38 3C 00 1C 38 3E 1E 1A 2A 1E B0 DC 34 3E
D1E1: 2C 3A 16 38 00 3A 3C 16 38 BC F4 34 2C 16 C6 F1
D1F1: 28 32 3E 1E C8 F1 3A 34 26 1E AC EE 28 3E 1E 22
D201: 3E 9E C7 1E 30 3C 1E 38 00 46 32 3E 38 00 26 30
D211: 26 3C 26 16 2C BA B8 3A 40 34 00 1E 30 3C 38 1E
D221: 48 00 40 32 3A 00 26 30 26 3C 26 16 2C 1E BA AC
D231: 22 1E 18 1E 30 00 3A 26 1E 00 26 24 38 1E 00 26
D241: 30 26 3C 26 16 2C 1E 30 00 1E 26 B0 C7 1E 30 3C
D251: 38 1E 00 3A 3E 3A 00 26 30 26 1A 26 16 2C 1E BA
D261: C7 3A 34 26 30 00 2A 30 32 18 00 3C 32 00 1A 24
D271: 16 30 22 9E A6 3C 32 3E 38 30 1E 48 00 2C 1E 00
D281: 18 32 3E 3C 32 30 00 34 32 3E 38 00 1A 24 16 30
D291: 22 1E B8 B5 2A 30 32 34 20 00 1C 38 1E 24 1E 30
D2A1: 00 48 3E 2E 00 42 1E 1A 24 3A 1E 2C B0 AC 22 26
D2B1: 38 1E 00 2C 16 00 34 1E 38 26 2C 2C 16 00 34 16
D2C1: 38 16 00 1A 16 2E 18 26 16 B8 C4 34 38 1E 3A 3A
D2D1: 00 20 26 38 1E 00 3C 32 00 3A 1E 2C 1E 1A BC B2
D2E1: 34 32 3E 3A 3A 1E 48 00 20 1E 3E 00 36 3E 16 30
D2F1: 1C 00 1A 32 38 38 1E 1A 3C 9E B2 20 26 38 1E 00
D301: 1C 38 3E 1E 1A 2A 1E 30 00 42 1E 30 30 00 38 26
D311: 1A 24 3C 26 A2 AC 32 34 38 26 2E 16 00 20 26 38
D321: 1E 00 34 16 38 16 00 3A 1E 2C 1E 1A 1A 26 32 30
D331: 16 B8 BC 24 26 22 24 00 3A 1A 32 38 1E BA 9E 2E
D341: 1E 26 2C 2C 1E 3E 38 3A 00 3A 1A 32 38 1E BA B0
D351: 24 32 1E 1A 24 3A 3C 48 16 24 2C 1E B0 D4 38 1E
D361: 1A 32 38 1C BA C2 38 16 30 2A 26 30 22 00 20 38
D371: 32 2E 00 04 00 3C 32 80 C2 34 2C 16 1A 1E 2E 1E
D381: 30 3C 00 1C 1E 00 04 00 16 80 BC 38 16 30 22 2C
D391: 26 3A 3C 1E 00 40 32 30 00 04 00 48 3E 2E 80 C8
D3A1: 38 16 30 2A 26 30 22 00 1C 1E 00 04 00 16 80 D9
D3B1: 38 16 3C 1E 00 46 32 3E 38 3A 1E 2C A0 DC 1E 40
D3C1: 16 2C 3E 1E 48 4C 40 32 3E BA D6 3A 1E 2C 18 3A
D3D1: 3C 00 38 1E 1A 24 30 1E B0 DF 1A 16 2C 26 20 26
D3E1: 36 3E 1E 3A 9E AA 30 32 40 26 1A 9E AA 30 32 40
D3F1: 26 1A 26 B2 AA 16 30 20 16 1E 30 22 1E B8 4A 1E
D401: 44 34 1E 38 BC 45 1E 44 34 1E 38 3C B2 40 1E 38
D411: 20 16 24 38 1E B0 8B 18 32 30 3E BA E8 3C 26 2E
D421: 9E E0 1C 3E 38 1E 9E E8 48 1E 26 BC E4 3C 26 1E
D431: 2E 34 B2 8B 2C 1E 40 1E AC 8B 30 26 40 1E 16 BE
D441: 8B 22 38 16 9C 8B 30 26 40 1E AC 8B 24 32 2C 9E
D451: 8B 3C 38 32 BE 8B 24 32 46 B2 8B 2C 32 1A A4 DC
D461: 26 30 3A 1E 38 3C 00 1A 32 26 30 BA C1 26 30 3C
D471: 38 32 1C 3E 26 38 1E 00 2C 1E 3A 00 34 26 1E 1A
D481: 1E BA D6 22 1E 2C 1C 00 1E 26 30 42 1E 38 20 1E
D491: B0 D6 26 30 3A 1E 38 3C 1E 00 20 26 1A 24 16 BA
D4A1: 00 20 38 1E 1E 00 34 2C 16 C6 0E 04 00 1A 32 26
D4B1: 30 00 06 00 34 2C 16 46 BA FA 04 00 34 26 1E 1A
D4C1: 1E 00 06 00 28 32 3E 1E 3E 38 BA 00 04 00 2E 3E
D4D1: 1E 30 48 00 06 00 3A 34 26 1E 2C 9E FA 04 00 2E
D4E1: 32 30 1E 1C 16 00 06 00 28 3E 1E 22 32 BA 14 04
D4F1: 00 1A 32 26 30 00 04 00 34 2C 16 C6 00 04 00 34
D501: 26 1E 1A 1E 00 04 00 28 32 3E 1E 3E B8 00 04 00
D511: 2E 3E 1E 30 48 1E 00 04 00 3A 34 26 1E AC 00 04
D521: 00 2E 32 30 1E 1C 16 00 04 00 28 3E 1E 22 B2 0E
D531: 06 00 1A 32 26 30 3A 00 04 00 34 2C 16 C6 FA 06
D541: 00 34 26 1E 1A 1E 3A 00 04 00 28 32 3E 1E 3E B8
D551: FA 06 00 2E 3E 1E 30 48 1E 30 00 04 00 3A 34 26
D561: 1E AC FA 06 00 2E 32 30 1E 1C 16 3A 00 04 00 28
D571: 3E 1E 22 B2 D3 50 00 2E 1A 2E 2C 44 44 44 00 16
D581: 3C 16 38 A6 A0 1A 38 1E 1C 26 3C 3A 80 A0 2A 38
D591: 1E 1C 26 3C 1E 80 A0 1A 38 1E 1C 26 3C 32 3A 80
D5A1: DA 18 32 30 3E 3A 80 D0 06 00 1A 38 1E 1C 26 3C
D5B1: 00 2E 26 30 26 2E 3E AE D6 06 00 28 1E 3E 44 00
D5C1: 2E 26 30 26 2E 3E AE D0 06 00 3A 34 26 1E 2C 1E
D5D1: 00 2E 26 30 26 2E 3E AE D3 06 00 28 3E 1E 22 32
D5E1: 3A 00 2E 26 30 26 2E B2 C8 18 32 30 3E 3A 00 1E
D5F1: 40 1E 38 46 80 CE 18 32 30 3E 3A 00 1A 24 16 36
D601: 3E 1E 80 CE 18 32 30 3E 3A 00 28 1E 1C 1E 80 C8
D611: 18 32 30 3E 3A 00 1A 16 1C 16 80 B8 16 40 32 26
D621: 1C 00 3A 34 26 2A 1E BA 88 16 3C 3C 1E 30 3C 26
D631: 32 30 00 16 3E 44 00 2C 16 30 1A 1E BA 96 3A 34
D641: 26 3C 48 1E 30 00 16 3E 3A 42 1E 26 1A 24 1E B0
D651: A0 1E 40 26 3C 1E 00 2C 16 3A 00 34 3E 30 3C 16
D661: BA E0 2C 1E 40 1E AC DA 30 26 40 1E 16 BE E2 22
D671: 38 16 9C E0 30 26 40 1E AC C4 3A 3E 34 1E 38 48
D681: 16 34 34 1E 38 00 38 1E 1A 24 16 38 22 9E CD 30
D691: 1E 3E 1E 38 00 3A 3E 34 1E 38 48 16 34 34 1E B8
D6A1: CD 30 3E 1E 40 32 00 3A 3E 34 1E 38 48 16 34 34
D6B1: 1E B8 31 D0 6D D0 A9 D0 E5 D0

; decode the option (DIP) switch ports into game config: read port loc_e00
; into loc_a, index $D6F7 by bits 5-3 into loc_156, $D6FF by bits 7-6 into
; loc_158, and the a0&0x06 field into $D6B3/$D6B4 -> loc_ac/loc_ad; store
; the other port loc_d00 (bit1 toggled) into loc_9, and fold loc_ad
; through assemblePotStatusByte recording the merge in loc_16a.
decodeOptionSwitches:
D6BB: AD 00 0E        LDA     $0E00               ; {hard.dsw2} read the options DIP-switch port
D6BE: 85 0A           STA     $0A                 ; {hard.workRam+A} snapshot the options byte
D6C0: 29 38           AND     #$38                ; bits 5-3 select the bonus-life interval
D6C2: 4A              LSR     A                   
D6C3: 4A              LSR     A                   
D6C4: 4A              LSR     A                   
D6C5: AA              TAX                         
D6C6: BD F7 D6        LDA     $D6F7,X             ; {hard.rom+46F7} read the bonus-interval table
D6C9: 8D 56 01        STA     $0156               ; {hard.workRam+156} store the live bonus-life interval
D6CC: AD 00 0D        LDA     $0D00               ; {hard.dsw1} read the coinage DIP-switch port
D6CF: 49 02           EOR     #$02                ; toggle bit 1
D6D1: 85 09           STA     $09                 ; {hard.workRam+9} store the coinage snapshot
D6D3: A5 0A           LDA     $0A                 ; {hard.workRam+A} bits 7-6 select the bonus config
D6D5: 2A              ROL     A                   
D6D6: 2A              ROL     A                   
D6D7: 2A              ROL     A                   
D6D8: 29 03           AND     #$03                
D6DA: AA              TAX                         
D6DB: BD FF D6        LDA     $D6FF,X             ; {hard.rom+46FF} read the bonus-config table
D6DE: 8D 58 01        STA     $0158               ; {hard.workRam+158} store the bonus config
D6E1: A5 0A           LDA     $0A                 ; {hard.workRam+A} take the two-bit difficulty field
D6E3: 29 06           AND     #$06                
D6E5: A8              TAY                         
D6E6: B9 B3 D6        LDA     $D6B3,Y             ; {hard.rom+46B3} read paired config entry A
D6E9: 85 AC           STA     $AC                 ; {hard.workRam+AC} store config A
D6EB: B9 B4 D6        LDA     $D6B4,Y             ; {hard.rom+46B4} read paired config entry B
D6EE: 85 AD           STA     $AD                 ; {hard.workRam+AD} store config B
D6F0: 20 E0 DB        JSR     $DBE0               ; {code.assemblePotStatusByte} fold config B through the pot/status merge
D6F3: 8D 6A 01        STA     $016A               ; {hard.workRam+16A} store the merged difficulty config
D6F6: 60              RTS                         

; ---- $D6F7-$D703: data ----
D6F7: 02 01 03 04 05 06 07 00 03 04 05 02 7C

serviceHeartbeatInterrupt:
D704: 48              PHA                         
D705: 8A              TXA                         
D706: 48              PHA                         
D707: 98              TYA                         
D708: 48              PHA                         
D709: D8              CLD                         
D70A: BA              TSX                         ; read the stack pointer for the depth guard
D70B: E0 D0           CPX     #$D0                ; stack too shallow
D70D: 90 04           BCC     $D713               ; {code.loc_d713}
D70F: A5 53           LDA     $53                 ; {hard.workRam+53} read the heartbeat counter for the sign guard
D711: 10 04           BPL     $D717               ; {code.loc_d717} heartbeat still positive -- proceed

loc_d713:
D713: 00              BRK                         ; guard tripped -- force a reset
D714: 4C 3F D9        JMP     $D93F               ; {code.bootMachineFromReset} divert to the power-on reset

loc_d717:
D717: 8D 00 50        STA     $5000               ; {hard.wdclr / irqAck} kick the watchdog and acknowledge the interrupt
D71A: 8D CB 60        STA     $60CB               ; {hard.pokey1+B} pulse the first chip's pot-scan start
D71D: AD C8 60        LDA     $60C8               ; {hard.pokey1+8} read the spinner pot
D720: 49 0F           EOR     #$0F                ; invert the pot reading
D722: A8              TAY                         
D723: 29 10           AND     #$10                ; stash the pot's bit-4 flag
D725: 8D 17 01        STA     $0117               ; {hard.workRam+117}
D728: 98              TYA                         
D729: 38              SEC                         
D72A: E5 52           SBC     $52                 ; {hard.workRam+52} form the delta versus the previous pot reading
D72C: 29 0F           AND     #$0F                ; keep the low nibble
D72E: C9 08           CMP     #$08                ; is the delta's sign bit set
D730: 90 02           BCC     $D734               ; {code.loc_d734}
D732: 09 F0           ORA     #$F0                ; sign-extend the 4-bit delta

loc_d734:
D734: 18              CLC                         
D735: 65 50           ADC     $50                 ; {hard.workRam+50} accumulate the delta into the spinner accumulator
D737: 85 50           STA     $50                 ; {hard.workRam+50} store the spinner accumulator
D739: 84 52           STY     $52                 ; {hard.workRam+52} save this frame's pot reading
D73B: 8D DB 60        STA     $60DB               ; {hard.pokey2+B} mirror the accumulator to the second chip's pot register
D73E: AC D8 60        LDY     $60D8               ; {hard.pokey2+8} read the coin/switch input
D741: AD 00 0C        LDA     $0C00               ; {hard.in0} latch the raw input port
D744: 85 08           STA     $08                 ; {hard.workRam+8} store the input latch
D746: A5 4C           LDA     $4C                 ; {hard.workRam+4C} last frame's inputs
D748: 84 4C           STY     $4C                 ; {hard.workRam+4C} latch this frame's coin/switch inputs
D74A: A8              TAY                         
D74B: 25 4C           AND     $4C                 ; {hard.workRam+4C}
D74D: 05 4D           ORA     $4D                 ; {hard.workRam+4D}
D74F: 85 4D           STA     $4D                 ; {hard.workRam+4D} update the debounced-input cell
D751: 98              TYA                         
D752: 05 4C           ORA     $4C                 ; {hard.workRam+4C}
D754: 25 4D           AND     $4D                 ; {hard.workRam+4D}
D756: 85 4D           STA     $4D                 ; {hard.workRam+4D} settle the debounced inputs
D758: A8              TAY                         
D759: 45 4F           EOR     $4F                 ; {hard.workRam+4F} compare against the previous held state for edges
D75B: 25 4D           AND     $4D                 ; {hard.workRam+4D}
D75D: 05 4E           ORA     $4E                 ; {hard.workRam+4E}
D75F: 85 4E           STA     $4E                 ; {hard.workRam+4E} record the newly-pressed edge flags
D761: 84 4F           STY     $4F                 ; {hard.workRam+4F} save the held state
D763: A5 B4           LDA     $B4                 ; {hard.workRam+B4} base the output flags on the vector scale
D765: A4 13           LDY     $13                 ; {hard.workRam+13} lane-0 status counter
D767: 10 02           BPL     $D76B               ; {code.loc_d76b}
D769: 09 04           ORA     #$04                ; set a bit for an active lane-0 counter

loc_d76b:
D76B: A4 14           LDY     $14                 ; {hard.workRam+14}
D76D: 10 02           BPL     $D771               ; {code.loc_d771}
D76F: 09 02           ORA     #$02                ; set a bit for an active lane-1 counter

loc_d771:
D771: A4 15           LDY     $15                 ; {hard.workRam+15}
D773: 10 02           BPL     $D777               ; {code.loc_d777}
D775: 09 01           ORA     #$01                ; set a bit for an active lane-2 counter

loc_d777:
D777: 8D 00 40        STA     $4000               ; {hard.coin} write the coin-counter / screen-flip output latch
D77A: A6 3E           LDX     $3E                 ; {hard.workRam+3E}
D77C: E8              INX                         
D77D: A4 05           LDY     $05                 ; {hard.workRam+5} status flags set -- use the phase index + 1
D77F: D0 10           BNE     $D791               ; {code.loc_d791}
D781: A2 00           LDX     #$00                
D783: A4 07           LDY     $07                 ; {hard.workRam+7} idle: sub-timer still low -- index 0
D785: C0 40           CPY     #$40                
D787: 90 08           BCC     $D791               ; {code.loc_d791}
D789: A6 06           LDX     $06                 ; {hard.workRam+6} else the phase counter (0 or 1)
D78B: E0 02           CPX     #$02                
D78D: 90 02           BCC     $D791               ; {code.loc_d791}
D78F: A2 03           LDX     #$03                ; else a fixed index 3

loc_d791:
D791: BD DD D7        LDA     $D7DD,X             ; {hard.rom+47DD} read the vector-generator state-code table
D794: 45 A1           EOR     $A1                 ; {hard.workRam+A1} fold its low two bits into the draw-mode flag
D796: 29 03           AND     #$03                
D798: 45 A1           EOR     $A1                 ; {hard.workRam+A1}
D79A: 85 A1           STA     $A1                 ; {hard.workRam+A1}
D79C: 8D E0 60        STA     $60E0               ; {hard.led} mirror the draw mode to the LED / screen-flip latch
D79F: 20 24 CF        JSR     $CF24               ; {code.tickHeartbeatCounters} run the timebase lane engine
D7A2: 20 0A CD        JSR     $CD0A               ; {code.stepSoundVoices} run the per-frame sound engine
D7A5: E6 53           INC     $53                 ; {hard.workRam+53} advance the heartbeat counter
D7A7: E6 07           INC     $07                 ; {hard.workRam+7} advance the interrupt sub-timer
D7A9: D0 1E           BNE     $D7C9               ; {code.loc_d7c9} only on the sub-timer wrap, run the timer cascades
D7AB: EE 06 04        INC     $0406               ; {hard.workRam+406} carry into timer-1 low byte
D7AE: D0 08           BNE     $D7B8               ; {code.loc_d7b8}
D7B0: EE 07 04        INC     $0407               ; {hard.workRam+407} carry into timer-1 mid byte
D7B3: D0 03           BNE     $D7B8               ; {code.loc_d7b8}
D7B5: EE 08 04        INC     $0408               ; {hard.workRam+408} carry into timer-1 high byte

loc_d7b8:
D7B8: 24 05           BIT     $05                 ; {hard.workRam+5} the second cascade is gated by a status flag
D7BA: 50 0D           BVC     $D7C9               ; {code.loc_d7c9}
D7BC: EE 09 04        INC     $0409               ; {hard.workRam+409} carry into timer-2 low byte
D7BF: D0 08           BNE     $D7C9               ; {code.loc_d7c9}
D7C1: EE 0A 04        INC     $040A               ; {hard.workRam+40A} carry into timer-2 mid byte
D7C4: D0 03           BNE     $D7C9               ; {code.loc_d7c9}
D7C6: EE 0B 04        INC     $040B               ; {hard.workRam+40B} carry into timer-2 high byte

loc_d7c9:
D7C9: 2C 00 0C        BIT     $0C00               ; {hard.in0} is the vector-generator-done input asserted
D7CC: 50 09           BVC     $D7D7               ; {code.loc_d7d7}
D7CE: EE 33 01        INC     $0133               ; {hard.workRam+133} bump the redraw counter
D7D1: 8D 00 58        STA     $5800               ; {hard.avgReset} strobe the vector-generator reset
D7D4: 8D 00 48        STA     $4800               ; {hard.avgGo} strobe the vector-generator go -- launch the redraw

loc_d7d7:
D7D7: 68              PLA                         
D7D8: A8              TAY                         
D7D9: 68              PLA                         
D7DA: AA              TAX                         
D7DB: 68              PLA                         
D7DC: 40              RTI                         

; ---- $D7DD-$D7E0: data ----
D7DD: FF FD FE FC

; arm mode bytes loc_5=0x00 and loc_1=0x02, then rebuild only while idle
; and enabled: bail if loc_1ca is nonzero (busy) or bit4 of option port
; loc_c00 is clear (disabled), write loc_0=0x00, and run
; rebuildControlBlocksFromTemplate only when loc_1c9's low two bits show a
; pending request.
armModeAndRebuildIfEnabled:
D7E1: A9 00           LDA     #$00                
D7E3: 85 05           STA     $05                 ; {hard.workRam+5} clear the status/flags byte
D7E5: A9 02           LDA     #$02                
D7E7: 85 01           STA     $01                 ; {hard.workRam+1} arm the dispatch selector to 2
D7E9: AD CA 01        LDA     $01CA               ; {hard.workRam+1CA} high-score store busy
D7EC: D0 15           BNE     $D803               ; {code.loc_d803} busy -- bail
D7EE: AD 00 0C        LDA     $0C00               ; {hard.in0} read the feature-enable input
D7F1: 29 10           AND     #$10                
D7F3: F0 0E           BEQ     $D803               ; {code.loc_d803} feature disabled -- bail
D7F5: A9 00           LDA     #$00                
D7F7: 85 00           STA     $00                 ; {hard.workRam} set idle game mode
D7F9: AD C9 01        LDA     $01C9               ; {hard.workRam+1C9} check the pending-work bits
D7FC: 29 03           AND     #$03                
D7FE: F0 03           BEQ     $D803               ; {code.loc_d803} nothing queued -- bail
D800: 20 AC AB        JSR     $ABAC               ; {code.rebuildControlBlocksFromTemplate} rebuild the control blocks from their template

loc_d803:
D803: 60              RTS                         

; a trampoline target that assembles the frame's vector item list into
; display RAM: four setup passes, a header pair, a marker emitted 0x158
; times (dec-counted via 0x37), then table-indexed coordinate records
; selected by state cells 0x16a/0x200/0x4d and the 0xd8b6/0xd8ba/0xd8c2
; tables, with a mask-table gated branch
; (eraseEaromLowRegions/queueEaromRegionErase).
buildVectorItemList:
D804: 20 BB D6        JSR     $D6BB               ; {code.decodeOptionSwitches} read the option DIP switches
D807: 20 A8 AA        JSR     $AAA8               ; {code.drawOverlayFrame} draw the overlay frame
D80A: 20 0D DD        JSR     $DD0D               ; {code.buildPotReadoutVectorList} build the pot readout list
D80D: 20 41 DD        JSR     $DD41               ; {code.buildLargeDecimalNumber} build the large decimal number
D810: AD 58 01        LDA     $0158               ; {hard.workRam+158} marker repeat count from the bonus config
D813: 85 37           STA     $37                 ; {hard.workRam+37}
D815: 20 53 DF        JSR     $DF53               ; {code.emitVectorHeaderWord} emit the vector-list header word
D818: A9 E8           LDA     #$E8                
D81A: A2 C0           LDX     #$C0                
D81C: 20 75 DF        JSR     $DF75               ; {code.emitScaledCoordinateRecord} emit a scaled coordinate record

loc_d81f:
D81F: A9 32           LDA     #$32                
D821: A2 6C           LDX     #$6C                
D823: 20 39 DF        JSR     $DF39               ; {code.emitCoordinateVectorWord} emit a marker coordinate word
D826: C6 37           DEC     $37                 ; {hard.workRam+37} decrement the marker count
D828: D0 F5           BNE     $D81F               ; {code.loc_d81f} repeat the marker that many times
D82A: AD 6A 01        LDA     $016A               ; {hard.workRam+16A} difficulty (0..3) doubled into a table index
D82D: 29 03           AND     #$03                
D82F: 0A              ASL     A                   
D830: A8              TAY                         
D831: B9 1F 3F        LDA     $3F1F,Y             ; {hard.vectorRom+F1F} read the difficulty coordinate pair (high byte)
D834: BE 1E 3F        LDX     $3F1E,Y             ; {hard.vectorRom+F1E} read the difficulty coordinate pair (low byte)
D837: 20 39 DF        JSR     $DF39               ; {code.emitCoordinateVectorWord} emit the difficulty coordinate word
D83A: AD 00 02        LDA     $0200               ; {hard.workRam+200} read the player's rim segment
D83D: 20 CE AD        JSR     $ADCE               ; {code.foldStepIntoFraction} fold it through the step-into-fraction helper
D840: 8D 00 02        STA     $0200               ; {hard.workRam+200} write the folded segment back
D843: 29 06           AND     #$06                ; segment-selected table index
D845: 48              PHA                         
D846: A8              TAY                         
D847: B9 17 3F        LDA     $3F17,Y             ; {hard.vectorRom+F17} read the segment coordinate pair (high byte)
D84A: BE 16 3F        LDX     $3F16,Y             ; {hard.vectorRom+F16} read the segment coordinate pair (low byte)
D84D: 20 39 DF        JSR     $DF39               ; {code.emitCoordinateVectorWord} emit the segment coordinate word
D850: 68              PLA                         
D851: 4A              LSR     A                   
D852: AA              TAX                         
D853: A5 4D           LDA     $4D                 ; {hard.workRam+4D} load the debounced inputs
D855: 3D B6 D8        AND     $D8B6,X             ; {hard.rom+48B6} mask them with the diagnostic mask-table entry
D858: DD B6 D8        CMP     $D8B6,X             ; {hard.rom+48B6} compare against the mask
D85B: D0 1A           BNE     $D877               ; {code.loc_d877} not every mask bit present -- skip the erase work
D85D: CA              DEX                         
D85E: CA              DEX                         
D85F: 10 03           BPL     $D864               ; {code.loc_d864}
D861: 4C 3F D9        JMP     $D93F               ; {code.bootMachineFromReset} slot underflow -- force a full reset

loc_d864:
D864: D0 06           BNE     $D86C               ; {code.loc_d86c}
D866: 20 E9 DD        JSR     $DDE9               ; {code.queueEaromRegionErase} erase the low high-score-store regions
D869: B8              CLV                         
D86A: 50 0B           BVC     $D877               ; {code.loc_d877}

loc_d86c:
D86C: 20 ED DD        JSR     $DDED               ; {code.eraseEaromLowRegions} queue a single high-score-store region erase
D86F: AD C9 01        LDA     $01C9               ; {hard.workRam+1C9}
D872: 09 03           ORA     #$03                ; arm the pending erase-work bits
D874: 8D C9 01        STA     $01C9               ; {hard.workRam+1C9} store the pending-work byte

loc_d877:
D877: AD CA 01        LDA     $01CA               ; {hard.workRam+1CA} read the high-score-store mode flag
D87A: 2D C6 01        AND     $01C6               ; {hard.workRam+1C6} and it with the blank flag
D87D: F0 07           BEQ     $D886               ; {code.loc_d886} flags disagree -- skip the extra word
D87F: A9 34           LDA     #$34                ; emit an extra coordinate word (high byte)
D881: A2 6E           LDX     #$6E                
D883: 20 39 DF        JSR     $DF39               ; {code.emitCoordinateVectorWord}

loc_d886:
D886: 20 53 DF        JSR     $DF53               ; {code.emitVectorHeaderWord} emit the second header word
D889: A5 09           LDA     $09                 ; {hard.workRam+9} coinage bits 2-4 select the low diagnostic digit
D88B: 29 1C           AND     #$1C                
D88D: 4A              LSR     A                   
D88E: 4A              LSR     A                   
D88F: AA              TAX                         
D890: BD BA D8        LDA     $D8BA,X             ; {hard.rom+48BA} read the low digit value
D893: A0 EE           LDY     #$EE                
D895: A2 1B           LDX     #$1B                
D897: 20 A9 D8        JSR     $D8A9               ; {code.emitScaledByteDigit} draw it as a scaled digit
D89A: A5 09           LDA     $09                 ; {hard.workRam+9} coinage top three bits select the high digit
D89C: 4A              LSR     A                   
D89D: 4A              LSR     A                   
D89E: 4A              LSR     A                   
D89F: 4A              LSR     A                   
D8A0: 4A              LSR     A                   
D8A1: AA              TAX                         
D8A2: BD C2 D8        LDA     $D8C2,X             ; {hard.rom+48C2} read the high digit value
D8A5: A0 32           LDY     #$32                
D8A7: A2 F8           LDX     #$F8                

; Stashes A into loc_29, scales the two coordinates (y, x), and emits that
; one stashed byte as a single-entry digit run.
emitScaledByteDigit:
D8A9: 85 29           STA     $29                 ; {hard.workRam+29} stash the byte to draw
D8AB: 98              TYA                         
D8AC: 20 75 DF        JSR     $DF75               ; {code.emitScaledCoordinateRecord} emit the scaled coordinate record for the anchor
D8AF: A9 29           LDA     #$29                ; point at the stashed byte
D8B1: A0 01           LDY     #$01                ; one digit
D8B3: 4C B1 DF        JMP     $DFB1               ; {code.emitNibbleDigitRun} lay the byte down as a single-digit glyph run

; ---- $D8B6-$D8C9: data ----
D8B6: 18 18 30 50 11 14 15 16 21 24 25 26 00 12 14 24
D8C6: 15 13 00 00

; power-on tone-and-delay entry: store the passed byte at loc_79 then
; drive POKEY chip-0 through a descending run of tone bursts (writing
; $60C1/$60C0/$60E0 and strobing output latch $5000 while draining fixed
; counts), before tail-delegating to the checksum/self-test
; checksumRomAndSettleEntropy.
playPowerOnTone:
D8CA: A8              TAY                         ; hold the passed byte as the burst count
D8CB: A9 00           LDA     #$00                ; seed the pass count to 0

; second entry of the power-on tone driver (same file as playPowerOnTone):
; store `count` at loc_79, derive the pass total from a ((a>>2)<<1, +1
; when count's low nibble is zero), then loop the descending POKEY tone
; bursts ($60C1/$60C0/$60E0, watchdog strobe $5000) switching to the low
; tone on the last pass, and tail-delegate to checksumRomAndSettleEntropy.
runPowerOnToneBursts:
D8CD: 84 79           STY     $79                 ; {hard.workRam+79} store the burst count
D8CF: 4A              LSR     A                   
D8D0: 4A              LSR     A                   
D8D1: 0A              ASL     A                   
D8D2: AA              TAX                         
D8D3: 98              TYA                         
D8D4: 29 0F           AND     #$0F                ; one extra pass when the count's low nibble is 0
D8D6: D0 01           BNE     $D8D9               ; {code.loc_d8d9}
D8D8: E8              INX                         

loc_d8d9:
D8D9: 9A              TXS                         

loc_d8da:
D8DA: A9 A2           LDA     #$A2                
D8DC: 8D C1 60        STA     $60C1               ; {hard.pokey1+1} set voice-1 control -- tone on
D8DF: BA              TSX                         
D8E0: D0 07           BNE     $D8E9               ; {code.loc_d8e9} is this the final pass
D8E2: A9 60           LDA     #$60                ; final pass: low tone, nine drains
D8E4: A0 09           LDY     #$09                
D8E6: B8              CLV                         
D8E7: 50 04           BVC     $D8ED               ; {code.loc_d8ed}

loc_d8e9:
D8E9: A9 C0           LDA     #$C0                ; normal pass: high tone, one drain
D8EB: A0 01           LDY     #$01                

loc_d8ed:
D8ED: 8D C0 60        STA     $60C0               ; {hard.pokey1} write voice-1 frequency -- the tone
D8F0: A9 03           LDA     #$03                
D8F2: 8D E0 60        STA     $60E0               ; {hard.led} strobe the LED / screen-flip latch
D8F5: A2 00           LDX     #$00                

loc_d8f7:
D8F7: 2C 00 0C        BIT     $0C00               ; {hard.in0} sync to the 3kHz line
D8FA: 30 FB           BMI     $D8F7               ; {code.loc_d8f7}

loc_d8fc:
D8FC: 2C 00 0C        BIT     $0C00               ; {hard.in0}
D8FF: 10 FB           BPL     $D8FC               ; {code.loc_d8fc}
D901: 8D 00 50        STA     $5000               ; {hard.wdclr / irqAck} kick the watchdog through the tone drain
D904: CA              DEX                         
D905: D0 F0           BNE     $D8F7               ; {code.loc_d8f7}
D907: 88              DEY                         
D908: D0 ED           BNE     $D8F7               ; {code.loc_d8f7}
D90A: 8E C1 60        STX     $60C1               ; {hard.pokey1+1} silence voice-1
D90D: A9 00           LDA     #$00                
D90F: 8D E0 60        STA     $60E0               ; {hard.led} clear the LED / screen-flip latch
D912: A0 09           LDY     #$09                

loc_d914:
D914: 2C 00 0C        BIT     $0C00               ; {hard.in0}
D917: 30 FB           BMI     $D914               ; {code.loc_d914}

loc_d919:
D919: 2C 00 0C        BIT     $0C00               ; {hard.in0}
D91C: 10 FB           BPL     $D919               ; {code.loc_d919}
D91E: 8D 00 50        STA     $5000               ; {hard.wdclr / irqAck} kick the watchdog through the silent gap
D921: CA              DEX                         
D922: D0 F0           BNE     $D914               ; {code.loc_d914}
D924: 88              DEY                         
D925: D0 ED           BNE     $D914               ; {code.loc_d914}
D927: BA              TSX                         
D928: CA              DEX                         
D929: 9A              TXS                         
D92A: 10 AE           BPL     $D8DA               ; {code.loc_d8da} loop until the pass counter underflows
D92C: 4C 0A DA        JMP     $DA0A               ; {code.checksumRomAndSettleEntropy} continue into the ROM checksum

; fold one table byte (read through the zero-page pointer at loc_0,
; indexed by the incoming cursor y) into the running byte a by XOR, then
; continue into the tone-burst count path seedToneBurstCount with that
; result.
foldToneTableByte:
D92F: 51 00           EOR     ($00),Y             ; {hard.workRam} fold one table byte into the running tone byte

; carry the incoming byte through as the tone-burst count and derive the
; pass-seed from loc_1 (values >=0x20 fold down by 0x18, then masked to
; five bits), handing both to the power-on tone burst
; runPowerOnToneBursts.
seedToneBurstCount:
D931: A8              TAY                         ; carry the folded byte as the burst count
D932: A5 01           LDA     $01                 ; {hard.workRam+1} read the dispatch selector as the pass seed
D934: C9 20           CMP     #$20                ; is the seed 0x20 or more
D936: 90 02           BCC     $D93A               ; {code.loc_d93a}
D938: E9 18           SBC     #$18                ; fold high seed values back into range

loc_d93a:
D93A: 29 1F           AND     #$1F                ; keep the low five bits
D93C: 4C CD D8        JMP     $D8CD               ; {code.runPowerOnToneBursts} drive the power-on tone bursts

; power-on RESET entry (a generator): wipe the two mapped RAM windows (2KB
; from 0x00, 4KB from 0x2000), seed the control block (0x1=0, 0x60e0=0,
; 0x60cf=7, 0x60df=7, and the 0x60c0/0x60d0 runs zeroed), then fork on
; self-test switch 0xc00 bit4 -- released seeds 0xb4=0x10, runs the
; device-init chain and becomes the main loop; held spins the operator
; diagnostic.
bootMachineFromReset:
D93F: 78              SEI                         ; mask interrupts at the reset entry
D940: 8D 00 50        STA     $5000               ; {hard.wdclr / irqAck} kick the watchdog
D943: 8D 00 58        STA     $5800               ; {hard.avgReset} strobe the vector-generator reset
D946: A2 FF           LDX     #$FF                
D948: 9A              TXS                         ; seat the stack
D949: D8              CLD                         
D94A: E8              INX                         
D94B: 8A              TXA                         
D94C: A8              TAY                         

loc_d94d:
D94D: 84 00           STY     $00                 ; {hard.workRam} set up a rolling zero-page pointer for the RAM wipe
D94F: 86 01           STX     $01                 ; {hard.workRam+1} (pointer high byte)
D951: A0 00           LDY     #$00                

loc_d953:
D953: 91 00           STA     ($00),Y             ; {hard.workRam} zero a work-RAM byte
D955: C8              INY                         
D956: D0 FB           BNE     $D953               ; {code.loc_d953} wipe the whole page
D958: E8              INX                         
D959: E0 08           CPX     #$08                ; reached the unmapped gap
D95B: D0 02           BNE     $D95F               ; {code.loc_d95f}
D95D: A2 20           LDX     #$20                ; resume at the 0x2000 vector-RAM window

loc_d95f:
D95F: E0 30           CPX     #$30                ; wipe through 0x2fff
D961: 8D 00 50        STA     $5000               ; {hard.wdclr / irqAck} kick the watchdog during the wipe
D964: 90 E7           BCC     $D94D               ; {code.loc_d94d} continue the wipe
D966: 85 01           STA     $01                 ; {hard.workRam+1}
D968: 8D E0 60        STA     $60E0               ; {hard.led} clear the LED / screen-flip latch
D96B: 8D CF 60        STA     $60CF               ; {hard.pokey1+F} hold the first sound chip in reset
D96E: 8D DF 60        STA     $60DF               ; {hard.pokey2+F} hold the second sound chip in reset
D971: A2 07           LDX     #$07                
D973: 8E CF 60        STX     $60CF               ; {hard.pokey1+F} release the first sound chip (control latch 7)
D976: 8E DF 60        STX     $60DF               ; {hard.pokey2+F} release the second sound chip
D979: E8              INX                         

loc_d97a:
D97A: 9D C0 60        STA     $60C0,X             ; {hard.pokey1} silence a first-chip audio register
D97D: 9D D0 60        STA     $60D0,X             ; {hard.pokey2} silence a second-chip audio register
D980: CA              DEX                         
D981: 10 F7           BPL     $D97A               ; {code.loc_d97a}
D983: AD 00 0C        LDA     $0C00               ; {hard.in0} read the self-test switch
D986: 29 10           AND     #$10                
D988: F0 1F           BEQ     $D9A9               ; {code.loc_d9a9} switch held -- run the RAM diagnostic

loc_d98a:
D98A: 8D 00 50        STA     $5000               ; {hard.wdclr / irqAck} normal boot: kick the watchdog through a settle delay
D98D: CE 00 01        DEC     $0100               ; {hard.workRam+100} settle-delay countdown low byte
D990: D0 F8           BNE     $D98A               ; {code.loc_d98a}
D992: CE 01 01        DEC     $0101               ; {hard.workRam+101} settle-delay countdown high byte
D995: D0 F3           BNE     $D98A               ; {code.loc_d98a}
D997: A9 10           LDA     #$10                
D999: 85 B4           STA     $B4                 ; {hard.workRam+B4} set the vector-generator scale
D99B: 20 11 DE        JSR     $DE11               ; {code.armEaromReadback} arm the high-score-store readback
D99E: 20 AC AB        JSR     $ABAC               ; {code.rebuildControlBlocksFromTemplate} rebuild the control blocks from their template
D9A1: 20 6E C1        JSR     $C16E               ; {code.buildLevelLayout} build the level layout
D9A4: 58              CLI                         ; enable interrupts
D9A5: 4C A0 C7        JMP     $C7A0               ; {code.runMainFrameLoop} enter the main frame loop

; ---- $D9A8-$D9A8: data ----
D9A8: A0

loc_d9a9:
D9A9: A2 11           LDX     #$11                

loc_d9ab:
D9AB: 9A              TXS                         
D9AC: A0 00           LDY     #$00                

loc_d9ae:
D9AE: BA              TSX                         
D9AF: 96 00           STX     $00,Y               ; {hard.workRam} RAM diagnostic: write a walking pattern to a cell
D9B1: A2 01           LDX     #$01                

loc_d9b3:
D9B3: C8              INY                         
D9B4: B9 00 00        LDA     $0000,Y             ; {hard.workRam} read the cell back
D9B7: F0 03           BEQ     $D9BC               ; {code.loc_d9bc}

loc_d9b9:
D9B9: 4C CA D8        JMP     $D8CA               ; {code.playPowerOnTone} verify failed -- sound the error tone

loc_d9bc:
D9BC: E8              INX                         
D9BD: D0 F4           BNE     $D9B3               ; {code.loc_d9b3}
D9BF: BA              TSX                         
D9C0: 8A              TXA                         
D9C1: 8D 00 50        STA     $5000               ; {hard.wdclr / irqAck} kick the watchdog during the test
D9C4: C8              INY                         
D9C5: 59 00 00        EOR     $0000,Y             ; {hard.workRam} check the read-back byte against the pattern
D9C8: D0 EF           BNE     $D9B9               ; {code.loc_d9b9} mismatch -- error tone
D9CA: 99 00 00        STA     $0000,Y             ; {hard.workRam} advance the pattern
D9CD: C8              INY                         
D9CE: D0 DE           BNE     $D9AE               ; {code.loc_d9ae}
D9D0: BA              TSX                         
D9D1: 8A              TXA                         
D9D2: 0A              ASL     A                   
D9D3: AA              TAX                         
D9D4: 90 D5           BCC     $D9AB               ; {code.loc_d9ab}
D9D6: A0 00           LDY     #$00                
D9D8: A2 01           LDX     #$01                

loc_d9da:
D9DA: 84 00           STY     $00                 ; {hard.workRam}
D9DC: 86 01           STX     $01                 ; {hard.workRam+1}
D9DE: A0 00           LDY     #$00                

loc_d9e0:
D9E0: B1 00           LDA     ($00),Y             ; {hard.workRam} second pass: read a byte, expect zero
D9E2: F0 03           BEQ     $D9E7               ; {code.loc_d9e7}
D9E4: 4C 31 D9        JMP     $D931               ; {code.seedToneBurstCount} nonzero -- error tone

loc_d9e7:
D9E7: A9 11           LDA     #$11                

loc_d9e9:
D9E9: 91 00           STA     ($00),Y             ; {hard.workRam} write a walking-ones pattern
D9EB: D1 00           CMP     ($00),Y             ; {hard.workRam} read it back
D9ED: F0 03           BEQ     $D9F2               ; {code.loc_d9f2}
D9EF: 4C 2F D9        JMP     $D92F               ; {code.foldToneTableByte} mismatch -- error tone

loc_d9f2:
D9F2: 0A              ASL     A                   
D9F3: 90 F4           BCC     $D9E9               ; {code.loc_d9e9}
D9F5: A9 00           LDA     #$00                
D9F7: 91 00           STA     ($00),Y             ; {hard.workRam} clear the cell again
D9F9: C8              INY                         
D9FA: D0 E4           BNE     $D9E0               ; {code.loc_d9e0}
D9FC: 8D 00 50        STA     $5000               ; {hard.wdclr / irqAck} kick the watchdog
D9FF: E8              INX                         
DA00: E0 08           CPX     #$08                ; reached the unmapped gap
DA02: D0 02           BNE     $DA06               ; {code.loc_da06}
DA04: A2 20           LDX     #$20                ; resume at the 0x2000 window

loc_da06:
DA06: E0 30           CPX     #$30                
DA08: 90 D0           BCC     $D9DA               ; {code.loc_d9da} cover through 0x2fff

; power-on ROM checksum + entropy settle: walk 12 banks of 8 pages, XOR
; every byte into a per-bank checksum seeded with the bank index (strobing
; watchdog 0x5000 per page), land the 12 checksums from 0x7d; if bank 0's
; checksum is nonzero arm the error tone (0x60c4/0x60c5); then settle each
; entropy register (0x60ca->0x7a, 0x60da->0x7b) storing only when six re-
; reads match, and continue into runSelfTestLoop.
checksumRomAndSettleEntropy:
DA0A: A9 00           LDA     #$00                
DA0C: A8              TAY                         
DA0D: AA              TAX                         
DA0E: 85 3B           STA     $3B                 ; {hard.workRam+3B} set the ROM-scan pointer low byte
DA10: A9 30           LDA     #$30                
DA12: 85 3C           STA     $3C                 ; {hard.workRam+3C} pointer high byte -- first ROM bank

loc_da14:
DA14: A9 08           LDA     #$08                
DA16: 85 38           STA     $38                 ; {hard.workRam+38} eight pages per bank
DA18: 8A              TXA                         ; seed this bank's checksum with the bank index

loc_da19:
DA19: 51 3B           EOR     ($3B),Y             ; {hard.workRam+3B} fold each ROM byte into the checksum
DA1B: C8              INY                         
DA1C: D0 FB           BNE     $DA19               ; {code.loc_da19}
DA1E: E6 3C           INC     $3C                 ; {hard.workRam+3C} advance to the next page
DA20: 8D 00 50        STA     $5000               ; {hard.wdclr / irqAck} kick the watchdog once per page
DA23: C6 38           DEC     $38                 ; {hard.workRam+38} eight pages per bank
DA25: D0 F2           BNE     $DA19               ; {code.loc_da19}
DA27: 95 7D           STA     $7D,X               ; {hard.workRam+7D} store this bank's checksum
DA29: E8              INX                         ; next bank
DA2A: E0 02           CPX     #$02                
DA2C: D0 04           BNE     $DA32               ; {code.loc_da32}
DA2E: A9 90           LDA     #$90                ; after two banks, jump to the high ROM window
DA30: 85 3C           STA     $3C                 ; {hard.workRam+3C}

loc_da32:
DA32: E0 0C           CPX     #$0C                ; twelve banks total
DA34: 90 DE           BCC     $DA14               ; {code.loc_da14}
DA36: A5 7D           LDA     $7D                 ; {hard.workRam+7D} bank-0 checksum nonzero -- a bad ROM
DA38: F0 0A           BEQ     $DA44               ; {code.loc_da44}
DA3A: A9 40           LDA     #$40                ; arm the error tone -- voice-3 frequency
DA3C: A2 A4           LDX     #$A4                
DA3E: 8D C4 60        STA     $60C4               ; {hard.pokey1+4}
DA41: 8E C5 60        STX     $60C5               ; {hard.pokey1+5} error-tone voice-3 control

loc_da44:
DA44: A2 05           LDX     #$05                
DA46: AD CA 60        LDA     $60CA               ; {hard.pokey1+A} sample the first chip's random register

loc_da49:
DA49: CD CA 60        CMP     $60CA               ; {hard.pokey1+A} re-read until it reads stable
DA4C: D0 05           BNE     $DA53               ; {code.loc_da53}
DA4E: CA              DEX                         
DA4F: 10 F8           BPL     $DA49               ; {code.loc_da49}
DA51: 85 7A           STA     $7A                 ; {hard.workRam+7A} store the settled entropy sample

loc_da53:
DA53: A2 05           LDX     #$05                
DA55: AD DA 60        LDA     $60DA               ; {hard.pokey2+A} sample the second chip's random register

loc_da58:
DA58: CD DA 60        CMP     $60DA               ; {hard.pokey2+A} re-read until stable
DA5B: D0 05           BNE     $DA62               ; {code.runSelfTestLoop}
DA5D: CA              DEX                         
DA5E: 10 F8           BPL     $DA58               ; {code.loc_da58}
DA60: 85 7B           STA     $7B                 ; {hard.workRam+7B} store the second entropy sample

; run the self-test session: seed the state machine (armEaromReadback),
; forward a pending request (queueEaromEraseAllRegions), copy the 8-byte
; colour table $DAF9 into colour RAM at 0x800, idle coin/flip 0x4000; then
; each pass strobe watchdog 0x5000/display-reset 0x5800, sample option
; switches 0x60c8 and diagnostics 0xc00, build/show a frame via
; dispatchDrawHandler/emitHeaderedBodyRecord, call stepEaromTransfer every
; fourth frame, until the self-test switch (0xc00 bit4) is released.
runSelfTestLoop:
DA62: 20 11 DE        JSR     $DE11               ; {code.armEaromReadback} arm the high-score-store readback
DA65: A0 02           LDY     #$02                
DA67: AD C9 01        LDA     $01C9               ; {hard.workRam+1C9} branch on the pending-work byte
DA6A: F0 0A           BEQ     $DA76               ; {code.loc_da76}
DA6C: 85 7C           STA     $7C                 ; {hard.workRam+7C} stash the pending-work value
DA6E: 20 F1 DD        JSR     $DDF1               ; {code.queueEaromEraseAllRegions} queue an erase of every high-score-store region
DA71: A0 00           LDY     #$00                
DA73: 8C C9 01        STY     $01C9               ; {hard.workRam+1C9} clear the pending-work byte

loc_da76:
DA76: 84 00           STY     $00                 ; {hard.workRam} set the diagnostic mode state
DA78: A2 07           LDX     #$07                

loc_da7a:
DA7A: BD F9 DA        LDA     $DAF9,X             ; {hard.rom+4AF9} copy the self-test colour table
DA7D: 9D 00 08        STA     $0800,X             ; {hard.colorRam} into colour RAM
DA80: CA              DEX                         
DA81: 10 F7           BPL     $DA7A               ; {code.loc_da7a}
DA83: A9 00           LDA     #$00                
DA85: 8D E0 60        STA     $60E0               ; {hard.led} blank the LED / screen-flip latch
DA88: A9 10           LDA     #$10                
DA8A: 8D 00 40        STA     $4000               ; {hard.coin} idle the coin-counter / flip output latch

loc_da8d:
DA8D: A0 04           LDY     #$04                

loc_da8f:
DA8F: A2 14           LDX     #$14                

loc_da91:
DA91: 2C 00 0C        BIT     $0C00               ; {hard.in0} busy-wait on the video sync line
DA94: 10 FB           BPL     $DA91               ; {code.loc_da91}

loc_da96:
DA96: 2C 00 0C        BIT     $0C00               ; {hard.in0}
DA99: 30 FB           BMI     $DA96               ; {code.loc_da96}
DA9B: CA              DEX                         
DA9C: 10 F3           BPL     $DA91               ; {code.loc_da91}
DA9E: 88              DEY                         
DA9F: 30 08           BMI     $DAA9               ; {code.loc_daa9}
DAA1: 8D 00 50        STA     $5000               ; {hard.wdclr / irqAck} kick the watchdog
DAA4: 2C 00 0C        BIT     $0C00               ; {hard.in0}
DAA7: 50 E6           BVC     $DA8F               ; {code.loc_da8f} loop on the vector-generator-done line

loc_daa9:
DAA9: 8D 00 58        STA     $5800               ; {hard.avgReset} strobe the vector-generator reset
DAAC: A9 00           LDA     #$00                
DAAE: 85 74           STA     $74                 ; {hard.workRam+74} reset the draw cursor low byte
DAB0: A9 20           LDA     #$20                
DAB2: 85 75           STA     $75                 ; {hard.workRam+75} draw cursor high byte -- cursor at 0x2000
DAB4: 8D CB 60        STA     $60CB               ; {hard.pokey1+B} pulse the first chip's pot scan
DAB7: AD C8 60        LDA     $60C8               ; {hard.pokey1+8} read the spinner pot
DABA: 85 52           STA     $52                 ; {hard.workRam+52} save the pot reading as the previous value
DABC: 29 0F           AND     #$0F                ; keep the low nibble
DABE: 85 50           STA     $50                 ; {hard.workRam+50} store it
DAC0: AD 00 0C        LDA     $0C00               ; {hard.in0} read and invert the input port
DAC3: 49 FF           EOR     #$FF                
DAC5: 29 2F           AND     #$2F                ; mask the input edges
DAC7: 85 4E           STA     $4E                 ; {hard.workRam+4E} store the edge flags
DAC9: 29 28           AND     #$28                ; either diagnostic-select bit set
DACB: F0 0B           BEQ     $DAD8               ; {code.loc_dad8}
DACD: 06 4C           ASL     $4C                 ; {hard.workRam+4C} shift the diagnostic-select state
DACF: 90 04           BCC     $DAD5               ; {code.loc_dad5}
DAD1: E6 00           INC     $00                 ; {hard.workRam} advance the diagnostic page by two
DAD3: E6 00           INC     $00                 ; {hard.workRam}

loc_dad5:
DAD5: B8              CLV                         
DAD6: 50 04           BVC     $DADC               ; {code.loc_dadc}

loc_dad8:
DAD8: A9 20           LDA     #$20                ; reset the select state
DADA: 85 4C           STA     $4C                 ; {hard.workRam+4C}

loc_dadc:
DADC: 20 0F DB        JSR     $DB0F               ; {code.dispatchDrawHandler} build the diagnostic frame
DADF: 20 0D DF        JSR     $DF0D               ; {code.emitHeaderedBodyRecord} emit the headered body record
DAE2: 8D 00 48        STA     $4800               ; {hard.avgGo} strobe the vector-generator go
DAE5: E6 03           INC     $03                 ; {hard.workRam+3} tick the frame counter
DAE7: A5 03           LDA     $03                 ; {hard.workRam+3}
DAE9: 29 03           AND     #$03                ; every fourth frame
DAEB: D0 03           BNE     $DAF0               ; {code.loc_daf0}
DAED: 20 1B DE        JSR     $DE1B               ; {code.stepEaromTransfer} service one high-score-store transfer step

loc_daf0:
DAF0: AD 00 0C        LDA     $0C00               ; {hard.in0} read the self-test switch
DAF3: 29 10           AND     #$10                
DAF5: F0 96           BEQ     $DA8D               ; {code.loc_da8d} still held -- run another diagnostic frame

loc_daf7:
DAF7: D0 FE           BNE     $DAF7               ; {code.loc_daf7} switch released -- spin until the watchdog resets the board

; ---- $DAF9-$DB0E: data ----
DAF9: 00 04 08 0C 03 07 0B 0B 59 DB F6 DB 83 DB 99 DB
DB09: 7D DB 6E DB 21 DB

; draw-handler dispatch on the display-finalize/self-test path: byte
; offset in 0x00 (0,2,..,12) selects one of seven per-frame draw handlers
; ($DB5A, $DBF7,...) at offset>>1; an out-of-range offset (>=0x0e) is
; clamped to 0x02 and the clamp persisted to 0x00, then tail-returns the
; handler's result.
dispatchDrawHandler:
DB0F: A6 00           LDX     $00                 ; {hard.workRam} read the per-frame draw-handler selector from the game-mode cell
DB11: E0 0E           CPX     #$0E                ; range-check the handler offset against the table size
DB13: 90 04           BCC     $DB19               ; {code.loc_db19} in range -- dispatch the selected handler
DB15: A2 02           LDX     #$02                ; out of range -- clamp the selector to handler entry 1
DB17: 86 00           STX     $00                 ; {hard.workRam} persist the clamped selector back to the game-mode cell

loc_db19:
DB19: BD 02 DB        LDA     $DB02,X             ; {hard.rom+4B02} push the selected handler's address high byte from the dispatch table
DB1C: 48              PHA                         
DB1D: BD 01 DB        LDA     $DB01,X             ; {hard.rom+4B01} push the handler's address low byte from the dispatch table
DB20: 48              PHA                         
DB21: 60              RTS                         ; rts-dispatch into the chosen draw handler

; reset the $60xx vector-display register bank (zero
; 0x60e0/0x6080/0x60c0/0x60d0/0x6000/0x6040, four settling reads, then
; raise 0x60e0 to 0x08), march a single set bit across the 32 slots at
; 0x6080, and emit one framing word via
; emitCoordinateVectorWord(0x34,0xa6).
initVectorDisplayRegisters:
DB22: A9 00           LDA     #$00                
DB24: 8D E0 60        STA     $60E0               ; {hard.led} zero the LED/flip/coin latch
DB27: 8D 80 60        STA     $6080               ; {hard.mathboxGo} zero the mathbox R0-low load register
DB2A: 8D C0 60        STA     $60C0               ; {hard.pokey1} zero POKEY 1 pitch
DB2D: 8D D0 60        STA     $60D0               ; {hard.pokey2} zero POKEY 2 pitch
DB30: 8D 00 60        STA     $6000               ; {hard.earomWrite} zero the EAROM data latch
DB33: 8D 40 60        STA     $6040               ; {hard.mathboxStatus / earomControl} zero the EAROM control latch (0x6040 write) -- a write here hits EAROM control, not the read-only mathbox status
DB36: AD 40 60        LDA     $6040               ; {hard.mathboxStatus / earomControl} dummy read to let the mathbox status flip-flop settle
DB39: AD 60 60        LDA     $6060               ; {hard.mathboxLo} dummy read of the mathbox result low byte
DB3C: AD 70 60        LDA     $6070               ; {hard.mathboxHi} dummy read of the mathbox result high byte
DB3F: AD 50 60        LDA     $6050               ; {hard.earomRead} dummy read of the EAROM read latch
DB42: A9 08           LDA     #$08                
DB44: 8D E0 60        STA     $60E0               ; {hard.led} raise the LED/flip latch
DB47: A9 01           LDA     #$01                ; seed a single set bit for the walking-bit march
DB49: A2 1F           LDX     #$1F                ; prepare to march across 32 mathbox load slots
DB4B: 18              CLC                         

loc_db4c:
DB4C: 9D 80 60        STA     $6080,X             ; {hard.mathboxGo} write the walking-bit pattern into mathbox load slot x
DB4F: 2A              ROL     A                   ; rotate the set bit up through carry
DB50: CA              DEX                         
DB51: 10 F9           BPL     $DB4C               ; {code.loc_db4c} loop the 32-slot bit march
DB53: A9 34           LDA     #$34                
DB55: A2 A6           LDX     #$A6                
DB57: 4C 39 DF        JMP     $DF39               ; {code.emitCoordinateVectorWord} emit one framing coordinate word (tail)

; When guards loc_1ca and loc_1c7 are both clear, runs the EAROM seeder
; (de11) and stamps loc_7c=loc_1c9 and loc_0=0x02.
beginEaromSequenceIfIdle:
DB5A: AD CA 01        LDA     $01CA               ; {hard.workRam+1CA} read the EAROM mode/active-operation flag
DB5D: 0D C7 01        ORA     $01C7               ; {hard.workRam+1C7} OR in the queued-region (pending) flag -- bail if a sequence is pending or running
DB60: D0 0C           BNE     $DB6E               ; {code.loc_db6e} a sequence is already pending or running -- bail
DB62: 20 11 DE        JSR     $DE11               ; {code.armEaromReadback} arm the EAROM readback state machine
DB65: AD C9 01        LDA     $01C9               ; {hard.workRam+1C9} copy the pending-work flags...
DB68: 85 7C           STA     $7C                 ; {hard.workRam+7C} ...into the walk's scratch cell
DB6A: A9 02           LDA     #$02                
DB6C: 85 00           STA     $00                 ; {hard.workRam} advance the game-mode cell

loc_db6e:
DB6E: 60              RTS                         

; emit a header from the halved slot count via emitTaggedVectorWord(0x68,
; 0x50>>1), then run $DB88(0x33,0x4e) to emit its header and blank the
; four even slots of 0x60c1 and 0x60d1.
emitHalvedCountHeaderAndClearVectorSlots:
DB6F: A5 50           LDA     $50                 ; {hard.workRam+50} read the spinner accumulator (player rotation count)
DB71: 4A              LSR     A                   ; halve it
DB72: A8              TAY                         
DB73: A9 68           LDA     #$68                
DB75: 20 4C DF        JSR     $DF4C               ; {code.emitTaggedVectorWord} emit a 0x68-tagged header word carrying half the spinner count
DB78: A2 4E           LDX     #$4E                
DB7A: A9 33           LDA     #$33                
DB7C: D0 0A           BNE     $DB88               ; {code.emitVectorHeaderAndClearSlots} emit the fixed header and clear the slot banks

; front onto emitVectorHeaderAndClearSlots with the fixed header pair
; (0x32,0xb6): emit that header word then blank the four even slots of
; 0x60c1 and 0x60d1.
emitPrimedHeaderAndClearVectorSlots:
DB7E: A2 B6           LDX     #$B6                
DB80: A9 32           LDA     #$32                
DB82: D0 04           BNE     $DB88               ; {code.emitVectorHeaderAndClearSlots} emit the primed header (pair 0x32,0xb6) and clear the slots

; emit a fixed framing word via emitCoordinateVectorWord(0x33,0x0a), then
; blank the four even-indexed slots of output tables 0x60c1 and 0x60d1.
emitFixedHeaderAndClearVectorSlots:
DB84: A9 33           LDA     #$33                
DB86: A2 0A           LDX     #$0A                

; emit a caller-supplied header word via emitCoordinateVectorWord(a,x),
; then blank the four even-indexed slots of output tables 0x60c1 and
; 0x60d1.
emitVectorHeaderAndClearSlots:
DB88: 20 39 DF        JSR     $DF39               ; {code.emitCoordinateVectorWord} emit the caller's framing word into the display list
DB8B: A2 06           LDX     #$06                
DB8D: A9 00           LDA     #$00                

loc_db8f:
DB8F: 9D C1 60        STA     $60C1,X             ; {hard.pokey1+1} silence POKEY 1 voice control at even slot x
DB92: 9D D1 60        STA     $60D1,X             ; {hard.pokey2+1} silence POKEY 2 voice control at even slot x
DB95: CA              DEX                         
DB96: CA              DEX                         
DB97: 10 F6           BPL     $DB8F               ; {code.loc_db8f} loop the four even AUDC slots
DB99: 60              RTS                         

; advance phase counter 0x39 (only while frame gate 0x3 & 0x3f is clear),
; index three parallel ROM rows ($DBD5/$DBD6/$DFDC) by 0x39 & 0x07 to seed
; output cells (clear 0x60c1+slotA, write ROM value into 0x60c0+slotB and
; 0xa8 into 0x60c1+slotB), then emit three words via
; emitCoordinateVectorWord(0x34,0x56)/emitVectorWordTag70(0x01, 0x3 &
; 0x7f)/emitCoordinateVectorWord(0x34,0xaa).
stepVectorPhaseAnimation:
DB9A: A5 03           LDA     $03                 ; {hard.workRam+3} read the frame counter
DB9C: 29 3F           AND     #$3F                ; gate on the low six bits -- once every 64 frames
DB9E: D0 02           BNE     $DBA2               ; {code.loc_dba2}
DBA0: E6 39           INC     $39                 ; {hard.workRam+39} advance the 8-phase sound/vector sequencer

loc_dba2:
DBA2: A5 39           LDA     $39                 ; {hard.workRam+39}
DBA4: 29 07           AND     #$07                ; mask the phase to 0..7 for the sequencer row index
DBA6: AA              TAX                         
DBA7: BC D5 DB        LDY     $DBD5,X             ; {hard.rom+4BD5} pick this phase's voice to silence from the row table
DBAA: A9 00           LDA     #$00                
DBAC: 99 C1 60        STA     $60C1,Y             ; {hard.pokey1+1} silence that POKEY 1 voice
DBAF: BC D6 DB        LDY     $DBD6,X             ; {hard.rom+4BD6} pick this phase's voice to fire from the row table
DBB2: BD DC DF        LDA     $DFDC,X             ; {hard.rom+4FDC} read this phase's value byte from the row table
DBB5: 99 C0 60        STA     $60C0,Y             ; {hard.pokey1} set the fired voice's frequency
DBB8: A9 A8           LDA     #$A8                
DBBA: 99 C1 60        STA     $60C1,Y             ; {hard.pokey1+1} fire it at fixed volume and distortion
DBBD: A9 34           LDA     #$34                
DBBF: A2 56           LDX     #$56                
DBC1: 20 39 DF        JSR     $DF39               ; {code.emitCoordinateVectorWord} emit the opening coordinate word
DBC4: A5 03           LDA     $03                 ; {hard.workRam+3} take the low seven bits of the frame counter
DBC6: 29 7F           AND     #$7F                
DBC8: A8              TAY                         
DBC9: A9 01           LDA     #$01                
DBCB: 20 6C DF        JSR     $DF6C               ; {code.emitVectorWordTag70} emit a tag-70 word that scrolls with time
DBCE: A9 34           LDA     #$34                
DBD0: A2 AA           LDX     #$AA                
DBD2: 4C 39 DF        JMP     $DF39               ; {code.emitCoordinateVectorWord} emit the closing coordinate word (tail)

; ---- $DBD5-$DBDF: data ----
DBD5: 16 00 10 02 12 04 14 06 16 00 EA

; Assembles a pot-status byte from the low three bits of $60D8 (mirrored
; into loc_37 and $60CB) merged with one relocated bit lifted from $60C8.
assemblePotStatusByte:
DBE0: 8D DB 60        STA     $60DB               ; {hard.pokey2+B} strobe POKEY 2 pot scan with the incoming value
DBE3: AD D8 60        LDA     $60D8               ; {hard.pokey2+8} read POKEY 2 pot lines (ALLPOT at 0x60d8)
DBE6: 29 07           AND     #$07                ; keep the low three control bits
DBE8: 85 37           STA     $37                 ; {hard.workRam+37} mirror them into scratch
DBEA: 8D CB 60        STA     $60CB               ; {hard.pokey1+B} and into the POKEY 1 pot-scan strobe
DBED: AD C8 60        LDA     $60C8               ; {hard.pokey1+8} read POKEY 1 pot lines (ALLPOT at 0x60c8)
DBF0: 29 20           AND     #$20                ; isolate bit 5
DBF2: 4A              LSR     A                   
DBF3: 4A              LSR     A                   ; shift it down to bit 3
DBF4: 05 37           ORA     $37                 ; {hard.workRam+37} merge with the low three bits
DBF6: 60              RTS                         ; return the assembled pot-status byte

; per-frame vector-list emit (handler index 1 of dispatchDrawHandler):
; when the 16-bit counter 0x2e/0x2f is nonzero, seed the POKEY operand
; cells and run the math-coprocessor scan (runMathboxDivide) to decide
; 0x78=0xff and the POKEY status byte; advance the 15-bit counter
; 0x2e/0x2f; build the POKEY work word from 0x4d/0x4e; fire the readout
; draws; conditionally emit the 0x52-bit marker; walk the 0x7d (x=11..0)
; and 0x78 (x=4..0) emit tables; then tail-delegate the 0x50-indexed
; colour pair to the colour-pair emitter emitKeyedScaledCoordinateRecord.
emitReadoutVectorList:
DBF7: A5 2E           LDA     $2E                 ; {hard.workRam+2E} read the sweep counter low byte
DBF9: F0 1E           BEQ     $DC19               ; {code.loc_dc19} counter zero -- skip the mathbox scan
DBFB: 8D 95 60        STA     $6095               ; {hard.mathboxGo+15} seed mathbox R7 low with the counter
DBFE: 8D 8D 60        STA     $608D               ; {hard.mathboxGo+D} and mathbox RA low
DC01: A5 2F           LDA     $2F                 ; {hard.workRam+2F} read the sweep counter high byte
DC03: 8D 96 60        STA     $6096               ; {hard.mathboxGo+16} seed mathbox R7 high
DC06: A2 00           LDX     #$00                
DC08: 20 E6 DC        JSR     $DCE6               ; {code.runMathboxDivide} run the mathbox divide
DC0B: C9 01           CMP     #$01                ; result A == 1?
DC0D: D0 06           BNE     $DC15               ; {code.loc_dc15} A != 1 -- force the status byte to 0xff
DC0F: 98              TYA                         
DC10: D0 03           BNE     $DC15               ; {code.loc_dc15} A == 1 but Y != 0 -- force the status byte to 0xff
DC12: 8A              TXA                         
DC13: 10 04           BPL     $DC19               ; {code.loc_dc19} remainder positive -- clear (keep X as the status byte)

loc_dc15:
DC15: A9 FF           LDA     #$FF                
DC17: 85 78           STA     $78                 ; {hard.workRam+78} force the spread/scan flag to 0xff

loc_dc19:
DC19: A2 00           LDX     #$00                
DC1B: 86 73           STX     $73                 ; {hard.workRam+73} clear the vector-record header
DC1D: E6 2E           INC     $2E                 ; {hard.workRam+2E} advance the sweep counter low byte
DC1F: D0 06           BNE     $DC27               ; {code.loc_dc27}
DC21: E6 2F           INC     $2F                 ; {hard.workRam+2F} carry into the sweep counter high byte
DC23: 10 02           BPL     $DC27               ; {code.loc_dc27}
DC25: 86 2F           STX     $2F                 ; {hard.workRam+2F} wrap the high byte at bit 7 (7-bit sweep)

loc_dc27:
DC27: 8D DB 60        STA     $60DB               ; {hard.pokey2+B} write the decided status byte to the POKEY 2 pot-scan strobe
DC2A: AD D8 60        LDA     $60D8               ; {hard.pokey2+8} read POKEY 2 pot lines (ALLPOT at 0x60d8)
DC2D: 29 78           AND     #$78                ; keep the option bits
DC2F: 85 4D           STA     $4D                 ; {hard.workRam+4D} stash the debounced input
DC31: F0 05           BEQ     $DC38               ; {code.loc_dc38} no bits set -- leave voice 1 silent
DC33: 8D C0 60        STA     $60C0               ; {hard.pokey1} set POKEY 1 voice 1 frequency
DC36: A2 A4           LDX     #$A4                ; arm voice 1 control

loc_dc38:
DC38: 8E C1 60        STX     $60C1               ; {hard.pokey1+1} write POKEY 1 voice 1 control
DC3B: A2 00           LDX     #$00                
DC3D: A5 4E           LDA     $4E                 ; {hard.workRam+4E} read the input edge flags
DC3F: F0 06           BEQ     $DC47               ; {code.loc_dc47} none set -- leave voice 2 silent
DC41: 0A              ASL     A                   
DC42: 8D C2 60        STA     $60C2               ; {hard.pokey1+2} set POKEY 1 voice 2 frequency (edge flags << 1)
DC45: A2 A4           LDX     #$A4                ; arm voice 2 control

loc_dc47:
DC47: 8E C3 60        STX     $60C3               ; {hard.pokey1+3} write POKEY 1 voice 2 control
DC4A: 20 0D DD        JSR     $DD0D               ; {code.buildPotReadoutVectorList} build the DIP/pot diagnostic readout
DC4D: A4 4D           LDY     $4D                 ; {hard.workRam+4D}
DC4F: A9 D0           LDA     #$D0                
DC51: A2 F0           LDX     #$F0                
DC53: 20 2B DD        JSR     $DD2B               ; {code.emitByteBitsAsDigits} render the debounced-input byte as eight per-bit digits
DC56: A4 4E           LDY     $4E                 ; {hard.workRam+4E}
DC58: 20 27 DD        JSR     $DD27               ; {code.emitByteBitsAsDigitsFixed} render the edge-flags byte as eight per-bit digits
DC5B: A5 52           LDA     $52                 ; {hard.workRam+52} read the previous spinner-pot sample
DC5D: 29 10           AND     #$10                ; test bit 4
DC5F: F0 1D           BEQ     $DC7E               ; {code.loc_dc7e} clear -- skip the marker and latch writes
DC61: A9 34           LDA     #$34                
DC63: A2 82           LDX     #$82                
DC65: 20 39 DF        JSR     $DF39               ; {code.emitCoordinateVectorWord} emit a marker coordinate word
DC68: A0 10           LDY     #$10                
DC6A: A5 4D           LDA     $4D                 ; {hard.workRam+4D} read the debounced input
DC6C: 29 60           AND     #$60                ; test the coin/mode bits
DC6E: F0 0E           BEQ     $DC7E               ; {code.loc_dc7e} none set -- skip the latch write
DC70: 49 20           EOR     #$20                ; flip bit 5 -- result zero iff only the coin bit (bit 5) was set
DC72: F0 04           BEQ     $DC78               ; {code.loc_dc78} exactly bit 5 -- keep the default latch value
DC74: A9 04           LDA     #$04                ; otherwise use the alternate mode value...
DC76: A0 08           LDY     #$08                ; ...and the alternate latch value

loc_dc78:
DC78: 8D E0 60        STA     $60E0               ; {hard.led} write the LED/flip latch
DC7B: 8C 00 40        STY     $4000               ; {hard.coin} write the coin-counter/flip output latch

loc_dc7e:
DC7E: A9 34           LDA     #$34                
DC80: A2 92           LDX     #$92                
DC82: 20 39 DF        JSR     $DF39               ; {code.emitCoordinateVectorWord} emit a coordinate mark
DC85: A2 0B           LDX     #$0B                ; walk the 12-slot spread table (x = 11..0)

loc_dc87:
DC87: B5 7D           LDA     $7D,X               ; {hard.workRam+7D} read spread slot x
DC89: F0 19           BEQ     $DCA4               ; {code.loc_dca4} empty slot -- skip
DC8B: 85 35           STA     $35                 ; {hard.workRam+35} stash the slot value
DC8D: 86 38           STX     $38                 ; {hard.workRam+38} save the loop index
DC8F: 8A              TXA                         
DC90: 20 1F DF        JSR     $DF1F               ; {code.emitStrokeWordFromNibblePlusOne} emit a stroke word for slot index + 1
DC93: A0 F4           LDY     #$F4                
DC95: A2 F4           LDX     #$F4                
DC97: A5 35           LDA     $35                 ; {hard.workRam+35}
DC99: 20 A9 D8        JSR     $D8A9               ; {code.emitScaledByteDigit} emit the slot value as a scaled digit
DC9C: A9 0C           LDA     #$0C                
DC9E: AA              TAX                         
DC9F: 20 75 DF        JSR     $DF75               ; {code.emitScaledCoordinateRecord} emit a scaled coordinate record
DCA2: A6 38           LDX     $38                 ; {hard.workRam+38} restore the loop index

loc_dca4:
DCA4: CA              DEX                         
DCA5: 10 E0           BPL     $DC87               ; {code.loc_dc87} next spread-table slot
DCA7: 20 53 DF        JSR     $DF53               ; {code.emitVectorHeaderWord} emit the header word
DCAA: A9 00           LDA     #$00                
DCAC: A2 16           LDX     #$16                
DCAE: 20 75 DF        JSR     $DF75               ; {code.emitScaledCoordinateRecord} emit a scaled coordinate record
DCB1: A2 04           LDX     #$04                ; walk the 5-slot spread table (x = 4..0)
DCB3: 86 37           STX     $37                 ; {hard.workRam+37}

loc_dcb5:
DCB5: A6 37           LDX     $37                 ; {hard.workRam+37}
DCB7: A0 00           LDY     #$00                
DCB9: B5 78           LDA     $78,X               ; {hard.workRam+78} read spread slot x
DCBB: F0 03           BEQ     $DCC0               ; {code.loc_dcc0} empty slot -- use word index 0
DCBD: BC E1 DC        LDY     $DCE1,X             ; {hard.rom+4CE1} pick this slot's coordinate-word index from the table

loc_dcc0:
DCC0: B9 E4 31        LDA     $31E4,Y             ; {hard.vectorRom+1E4} read the coordinate word low byte from the glyph table
DCC3: BE E5 31        LDX     $31E5,Y             ; {hard.vectorRom+1E5} read the coordinate word high byte from the glyph table
DCC6: 20 57 DF        JSR     $DF57               ; {code.emitVectorWord} emit the coordinate word
DCC9: C6 37           DEC     $37                 ; {hard.workRam+37}
DCCB: 10 E8           BPL     $DCB5               ; {code.loc_dcb5} next slot
DCCD: A2 AC           LDX     #$AC                
DCCF: A9 30           LDA     #$30                
DCD1: 20 75 DF        JSR     $DF75               ; {code.emitScaledCoordinateRecord} emit the final coordinate mark
DCD4: A4 50           LDY     $50                 ; {hard.workRam+50} index by the spinner accumulator
DCD6: B9 E8 DF        LDA     $DFE8,Y             ; {hard.rom+4FE8} read the colour-pair high byte
DCD9: BE E4 DF        LDX     $DFE4,Y             ; {hard.rom+4FE4} read the colour-pair low byte
DCDC: A0 C0           LDY     #$C0                
DCDE: 4C 73 DF        JMP     $DF73               ; {code.emitKeyedScaledCoordinateRecord} emit the keyed scaled coordinate record (tail)

; ---- $DCE1-$DCE5: data ----
DCE1: 2E 38 34 36 1E

; Primes the math-coprocessor operand/count registers $608C-$6096 from A
; and X, kicks its divide, spins a 16-step window on $6040 for the first
; ready result, and returns the $6060/$6070 low/high pair.
runMathboxDivide:
DCE6: A0 00           LDY     #$00                
DCE8: 84 73           STY     $73                 ; {hard.workRam+73} clear the vector-record header staging cell
DCEA: 8C 14 04        STY     $0414               ; {hard.workRam+414} clear the second staging cell
DCED: 8D 8E 60        STA     $608E               ; {hard.mathboxGo+E} load mathbox Ra high operand
DCF0: 8E 8F 60        STX     $608F               ; {hard.mathboxGo+F} load mathbox Rb low operand
DCF3: 8C 90 60        STY     $6090               ; {hard.mathboxGo+10} clear mathbox Rb high
DCF6: A2 10           LDX     #$10                
DCF8: 8E 8C 60        STX     $608C               ; {hard.mathboxGo+C} seed the mathbox iteration count
DCFB: 8E 94 60        STX     $6094               ; {hard.mathboxGo+14} strobe the divide to start

loc_dcfe:
DCFE: CA              DEX                         ; count down the poll window
DCFF: 30 0B           BMI     $DD0C               ; {code.loc_dd0c} window exhausted -- no result ready
DD01: AD 40 60        LDA     $6040               ; {hard.mathboxStatus / earomControl} read the mathbox status
DD04: 30 F8           BMI     $DCFE               ; {code.loc_dcfe} still busy -- keep polling
DD06: AD 60 60        LDA     $6060               ; {hard.mathboxLo} ready -- latch the result low byte
DD09: AC 70 60        LDY     $6070               ; {hard.mathboxHi} latch the result high byte

loc_dd0c:
DD0C: 60              RTS                         

; Builds a diagnostic readout vector list: a fixed header word ($DF53), a
; zero word (emitBlankVectorWordTag70), then eight-digit runs keyed by DIP
; ports loc_d00/loc_e00 and a pot-status byte.
buildPotReadoutVectorList:
DD0D: 20 53 DF        JSR     $DF53               ; {code.emitVectorHeaderWord} emit the fixed header word
DD10: A9 00           LDA     #$00                
DD12: 20 6A DF        JSR     $DF6A               ; {code.emitBlankVectorWordTag70} emit a zero-valued tag-70 framing word
DD15: A9 E8           LDA     #$E8                
DD17: AC 00 0D        LDY     $0D00               ; {hard.dsw1} read the coinage DIP bank
DD1A: 20 29 DD        JSR     $DD29               ; {code.emitByteBitsAsDigitsAtF8} render it as an eight-bit digit run at column 0xe8
DD1D: AC 00 0E        LDY     $0E00               ; {hard.dsw2} read the options DIP bank
DD20: 20 27 DD        JSR     $DD27               ; {code.emitByteBitsAsDigitsFixed} render it as an eight-bit digit run
DD23: 20 E0 DB        JSR     $DBE0               ; {code.assemblePotStatusByte} pulse the POKEY pot scan and fold to a status byte
DD26: A8              TAY                         

; Fixed-position front feeding the coordinate deltas 0xd0/0xf8 into the
; eight-bit byte-digit emit, displaying the byte in y.
emitByteBitsAsDigitsFixed:
DD27: A9 D0           LDA     #$D0                ; inject the fixed value byte 0xd0

; Fixed-position front feeding coordinate x = 0xf8 into the eight-bit
; byte-digit emit.
emitByteBitsAsDigitsAtF8:
DD29: A2 F8           LDX     #$F8                ; inject the fixed screen-X column 0xf8

; Stashes the byte y into loc_35, scales the two coordinates, then shifts
; loc_35 out MSB-first emitting each of its eight bits as one vector
; digit.
emitByteBitsAsDigits:
DD2B: 84 35           STY     $35                 ; {hard.workRam+35} stash the byte to render
DD2D: 20 75 DF        JSR     $DF75               ; {code.emitScaledCoordinateRecord} position the eight-bit row on screen
DD30: A2 07           LDX     #$07                ; eight bits to draw
DD32: 86 37           STX     $37                 ; {hard.workRam+37}

loc_dd34:
DD34: 06 35           ASL     $35                 ; {hard.workRam+35} shift the byte's top bit out
DD36: A9 00           LDA     #$00                
DD38: 2A              ROL     A                   ; capture the shifted-out (MSB-first) bit
DD39: 20 1F DF        JSR     $DF1F               ; {code.emitStrokeWordFromNibblePlusOne} emit one stroke word for that bit
DD3C: C6 37           DEC     $37                 ; {hard.workRam+37}
DD3E: 10 F4           BPL     $DD34               ; {code.loc_dd34} next bit
DD40: 60              RTS                         

; Doubles-and-adds two little-endian input pairs into the math-box
; operands $6095/$6096 (floored to one), seeds a divide, emits a header,
; then makes repeated passes of binary-to-BCD double-dabble over the
; three-byte source at loc_3b/loc_3c emitting each pass's digits with a
; scaled coordinate record.
buildLargeDecimalNumber:
DD41: AD 0F 04        LDA     $040F               ; {hard.workRam+40F} read the input pair low byte
DD44: 0A              ASL     A                   ; double it
DD45: 85 29           STA     $29                 ; {hard.workRam+29}
DD47: AD 10 04        LDA     $0410               ; {hard.workRam+410} read the input pair high byte
DD4A: 2A              ROL     A                   ; double it, threading the carry
DD4B: 85 2A           STA     $2A                 ; {hard.workRam+2A}
DD4D: AD 0C 04        LDA     $040C               ; {hard.workRam+40C} read the coordinate accumulator low byte
DD50: 18              CLC                         
DD51: 65 29           ADC     $29                 ; {hard.workRam+29} add the doubled input
DD53: 8D 95 60        STA     $6095               ; {hard.mathboxGo+15} store as mathbox R7 low operand
DD56: 85 29           STA     $29                 ; {hard.workRam+29}
DD58: AD 0D 04        LDA     $040D               ; {hard.workRam+40D} read the coordinate accumulator high byte
DD5B: 65 2A           ADC     $2A                 ; {hard.workRam+2A} add with carry
DD5D: 8D 96 60        STA     $6096               ; {hard.mathboxGo+16} store as mathbox R7 high operand
DD60: 05 29           ORA     $29                 ; {hard.workRam+29} test whether the whole operand is zero
DD62: D0 05           BNE     $DD69               ; {code.loc_dd69} nonzero -- keep it
DD64: A9 01           LDA     #$01                
DD66: 8D 95 60        STA     $6095               ; {hard.mathboxGo+15} floor the operand to one so the divide never sees zero

loc_dd69:
DD69: AD 09 04        LDA     $0409               ; {hard.workRam+409} load mathbox Ra low from the timer low byte
DD6C: 8D 8D 60        STA     $608D               ; {hard.mathboxGo+D}
DD6F: AD 0A 04        LDA     $040A               ; {hard.workRam+40A} read the timer mid byte
DD72: AE 0B 04        LDX     $040B               ; {hard.workRam+40B} read the timer high byte
DD75: 20 E6 DC        JSR     $DCE6               ; {code.runMathboxDivide} run the mathbox divide
DD78: 8D 12 04        STA     $0412               ; {hard.workRam+412} stash the quotient
DD7B: 8C 13 04        STY     $0413               ; {hard.workRam+413} stash the remainder
DD7E: A9 3D           LDA     #$3D                
DD80: A2 CE           LDX     #$CE                
DD82: 20 39 DF        JSR     $DF39               ; {code.emitCoordinateVectorWord} emit the fixed coordinate header word
DD85: A9 06           LDA     #$06                
DD87: 85 3B           STA     $3B                 ; {hard.workRam+3B} set the source pointer low -> 0x0406
DD89: A9 04           LDA     #$04                
DD8B: 85 3C           STA     $3C                 ; {hard.workRam+3C} set the source pointer high
DD8D: 85 37           STA     $37                 ; {hard.workRam+37} outer loop -- five numbers (post-decrement bpl runs 5 passes; the 5th draws the divide quotient/remainder at 0x0412/0x0413)

loc_dd8f:
DD8F: A0 00           LDY     #$00                
DD91: 84 31           STY     $31                 ; {hard.workRam+31} clear the 4-byte BCD accumulator
DD93: 84 32           STY     $32                 ; {hard.workRam+32}
DD95: 84 33           STY     $33                 ; {hard.workRam+33}
DD97: 84 34           STY     $34                 ; {hard.workRam+34}
DD99: B1 3B           LDA     ($3B),Y             ; {hard.workRam+3B} load the first binary source byte
DD9B: 85 56           STA     $56                 ; {hard.workRam+56}
DD9D: E6 3B           INC     $3B                 ; {hard.workRam+3B}
DD9F: B1 3B           LDA     ($3B),Y             ; {hard.workRam+3B} load the second binary source byte
DDA1: 85 57           STA     $57                 ; {hard.workRam+57}
DDA3: E6 3B           INC     $3B                 ; {hard.workRam+3B}
DDA5: B1 3B           LDA     ($3B),Y             ; {hard.workRam+3B} load the third binary source byte
DDA7: 85 58           STA     $58                 ; {hard.workRam+58}
DDA9: E6 3B           INC     $3B                 ; {hard.workRam+3B}
DDAB: F8              SED                         ; enter decimal mode for double-dabble
DDAC: A0 17           LDY     #$17                ; 24 source bits
DDAE: 84 38           STY     $38                 ; {hard.workRam+38}

loc_ddb0:
DDB0: 26 56           ROL     $56                 ; {hard.workRam+56} shift the 24-bit binary source left one bit...
DDB2: 26 57           ROL     $57                 ; {hard.workRam+57} ...carry chained low to high...
DDB4: 26 58           ROL     $58                 ; {hard.workRam+58} ...through the third byte
DDB6: A0 03           LDY     #$03                
DDB8: A2 00           LDX     #$00                

loc_ddba:
DDBA: B5 31           LDA     $31,X               ; {hard.workRam+31} BCD-double each accumulator byte with the shifted-out bit
DDBC: 75 31           ADC     $31,X               ; {hard.workRam+31}
DDBE: 95 31           STA     $31,X               ; {hard.workRam+31}
DDC0: E8              INX                         
DDC1: 88              DEY                         
DDC2: 10 F6           BPL     $DDBA               ; {code.loc_ddba} across the four BCD bytes
DDC4: C6 38           DEC     $38                 ; {hard.workRam+38}
DDC6: 10 E8           BPL     $DDB0               ; {code.loc_ddb0} next of the 24 bits
DDC8: D8              CLD                         ; leave decimal mode
DDC9: A9 31           LDA     #$31                
DDCB: A0 04           LDY     #$04                
DDCD: 20 B1 DF        JSR     $DFB1               ; {code.emitNibbleDigitRun} emit the converted decimal digit run
DDD0: A9 D0           LDA     #$D0                
DDD2: A2 F8           LDX     #$F8                
DDD4: 20 75 DF        JSR     $DF75               ; {code.emitScaledCoordinateRecord} emit the number's scaled coordinate record
DDD7: C6 37           DEC     $37                 ; {hard.workRam+37}
DDD9: 10 B4           BPL     $DD8F               ; {code.loc_dd8f} next of the five numbers
DDDB: 60              RTS                         

; ---- $DDDC-$DDE8: data ----
DDDC: 73 00 09 0A 15 16 22 15 06 15 07 06 04

; queue a blanked write (erase) of the single region on bit 0x04 by
; feeding mask 0x04 into the blank-mode merge $DDF3 (which forces blank-
; flag 0x1c6=0xff then ORs the mask into 0x1c7/0x1c8).
queueEaromRegionErase:
DDE9: A9 04           LDA     #$04                ; select the EAROM region on bit mask 0x04
DDEB: D0 06           BNE     $DDF3               ; {code.requestEaromBlankWrite} request a blanked (erase) write of that region

; Branch-only trampoline requesting a blanked EAROM write of the two low
; regions via ddf3 with mask 0x03; downstream loc_1c7/loc_1c8 observed
; changing.
eraseEaromLowRegions:
DDED: A9 03           LDA     #$03                ; load region mask 0x03 -- the two low high-score regions
DDEF: D0 02           BNE     $DDF3               ; {code.requestEaromBlankWrite} jump into the blank-write request builder with the mask

; queue a blanked write (erase) of all three EAROM regions: stamp 0xff
; into blank-flag 0x1c6 and OR mask 0x07 into region-pending 0x1c7 and
; direction 0x1c8.
queueEaromEraseAllRegions:
DDF1: A9 07           LDA     #$07                ; load region mask 0x07 -- all three high-score regions -- then build a blank/erase request

; Forces the EAROM index byte to 0xff (blank mode) then merges the
; caller's mask, requesting a blanked write of those regions.
requestEaromBlankWrite:
DDF3: A0 FF           LDY     #$FF                ; force the index byte to 0xff, the blank/erase sentinel
DDF5: D0 08           BNE     $DDFF               ; {code.queueEaromRequest} jump to the shared request tail, mask still in a

; request a (non-blanked) EAROM write of the two low NVRAM regions: pass
; the fixed mask 0x03 to the shared zeroed-index merge tail $DDFD, which
; ORs the mask into the region-pending loc_1c7 and direction loc_1c8 cells
; with a cleared blank-index loc_1c6.
requestWriteLowRegions:
DDF7: A9 03           LDA     #$03                ; load region mask 0x03 -- the two low regions -- for a live save
DDF9: D0 02           BNE     $DDFD               ; {code.queueEaromRequestAtIndexZero} jump into the index-zero (live-save) tail

; queue a plain (non-blanked) EAROM save of the region on bit 0x04: store
; index 0x00 into blank-flag 0x1c6 and OR mask 0x04 into region-pending
; 0x1c7 and direction 0x1c8.
queueEaromRegionSave:
DDFB: A9 04           LDA     #$04                ; load region mask 0x04 -- the third region -- then fall into the live-save tail

; queue an EAROM (high-score NVRAM) request at cell index 0: store 0x00
; into the target-index cell loc_1c6 and OR the caller's mask A into both
; request-flag cells loc_1c7 and loc_1c8 (shared tail queueEaromRequest);
; entry queueEaromRegionSave presets mask 0x04.
queueEaromRequestAtIndexZero:
DDFD: A0 00           LDY     #$00                ; force the index byte to 0 -- live save, not erase

; queue an EAROM (high-score NVRAM) request: store Y into the target-index
; cell loc_1c6 and OR the request mask A into both request-flag cells
; loc_1c7 and loc_1c8.
queueEaromRequest:
DDFF: 8C C6 01        STY     $01C6               ; {hard.workRam+1C6} store the index/blank byte (0 = live save, 0xff = erase)
DE02: 48              PHA                         
DE03: 0D C7 01        ORA     $01C7               ; {hard.workRam+1C7} merge the mask into the region-pending bits
DE06: 8D C7 01        STA     $01C7               ; {hard.workRam+1C7} store the regions awaiting service
DE09: 68              PLA                         
DE0A: 0D C8 01        ORA     $01C8               ; {hard.workRam+1C8} merge the mask into the per-region direction bits
DE0D: 8D C8 01        STA     $01C8               ; {hard.workRam+1C8} store direction (set = write out, clear = read back)
DE10: 60              RTS                         

; Sets EAROM mode byte loc_1c7=0x07 and clears loc_1c8=0x00, then drives
; the step machine to arm a read-back of all regions.
armEaromReadback:
DE11: A9 07           LDA     #$07                ; command all three regions
DE13: 8D C7 01        STA     $01C7               ; {hard.workRam+1C7} set the region-pending bits to read every region back
DE16: A9 00           LDA     #$00                ; clear the direction bits
DE18: 8D C8 01        STA     $01C8               ; {hard.workRam+1C8} so all regions are read back in, then fall into the transfer step

; drain one entry of the queued EAROM save/read: when mode 0x1ca is idle
; and pending 0x1c7 is set, isolate one region bit into 0x1ce, seed cursor
; 0x1cc/limit 0x1cd and row pointer 0xbd/0xbe from packed ROM rows
; ($DDDD/ddde/dde3/dde4) and arm 0x1ca write(0x80)/read(0x20) per 0x1c8;
; each pass folds the RAM/read-back byte into checksum 0x1cf, moves it
; through the 0x6000 data window with the 0x6040/0x6050 handshake, at the
; limit writes/compares the checksum (recording failures into 0x1c9), and
; clocks 0x6040 to signal re-enter or stop.
stepEaromTransfer:
DE1B: AD CA 01        LDA     $01CA               ; {hard.workRam+1CA} read the EAROM step-machine mode/busy byte
DE1E: D0 4B           BNE     $DE6B               ; {code.loc_de6b} a pass is already active: skip region setup
DE20: AD C7 01        LDA     $01C7               ; {hard.workRam+1C7} read the region-pending bits
DE23: F0 46           BEQ     $DE6B               ; {code.loc_de6b} nothing queued: skip setup
DE25: A2 00           LDX     #$00                
DE27: 8E CB 01        STX     $01CB               ; {hard.workRam+1CB} clear the per-region pass counter
DE2A: 8E CF 01        STX     $01CF               ; {hard.workRam+1CF} clear the running checksum accumulator
DE2D: 8E CE 01        STX     $01CE               ; {hard.workRam+1CE} clear the single-region walking mask
DE30: A2 08           LDX     #$08                ; 8 bits to rotate -- x also becomes the region index
DE32: 38              SEC                         

loc_de33:
DE33: 6E CE 01        ROR     $01CE               ; {hard.workRam+1CE} rotate a set bit into the walking mask
DE36: 0A              ASL     A                   ; shift the pending bits left, hunting the highest (most-significant) set region bit
DE37: CA              DEX                         ; count down toward the region index
DE38: 90 F9           BCC     $DE33               ; {code.loc_de33} keep rotating until a set bit falls out
DE3A: A0 80           LDY     #$80                ; default to write mode (0x80)
DE3C: AD CE 01        LDA     $01CE               ; {hard.workRam+1CE}
DE3F: 2D C8 01        AND     $01C8               ; {hard.workRam+1C8} test the isolated region mask against the direction bits
DE42: D0 02           BNE     $DE46               ; {code.loc_de46} region flagged write: keep write mode
DE44: A0 20           LDY     #$20                ; else read mode (0x20)

loc_de46:
DE46: 8C CA 01        STY     $01CA               ; {hard.workRam+1CA} arm the step-machine mode for this region
DE49: AD CE 01        LDA     $01CE               ; {hard.workRam+1CE}
DE4C: 4D C7 01        EOR     $01C7               ; {hard.workRam+1C7} drop this region's bit out of the pending set
DE4F: 8D C7 01        STA     $01C7               ; {hard.workRam+1C7} so it is not serviced again
DE52: 8A              TXA                         
DE53: 0A              ASL     A                   ; word-stride the region index into the packed tables
DE54: AA              TAX                         
DE55: BD DD DD        LDA     $DDDD,X             ; {hard.rom+4DDD} read the region's start cursor from the packed table
DE58: 8D CC 01        STA     $01CC               ; {hard.workRam+1CC} seed the region byte cursor
DE5B: BD DE DD        LDA     $DDDE,X             ; {hard.rom+4DDE} read the region's end/limit from the packed table
DE5E: 8D CD 01        STA     $01CD               ; {hard.workRam+1CD} seed the checksum-position limit
DE61: BD E3 DD        LDA     $DDE3,X             ; {hard.rom+4DE3} read the region RAM-copy pointer low byte
DE64: 85 BD           STA     $BD                 ; {hard.workRam+BD} seed the region walk-pointer low
DE66: BD E4 DD        LDA     $DDE4,X             ; {hard.rom+4DE4} read the region RAM-copy pointer high byte
DE69: 85 BE           STA     $BE                 ; {hard.workRam+BE} seed the region walk-pointer high

loc_de6b:
DE6B: A0 00           LDY     #$00                
DE6D: 8C 40 60        STY     $6040               ; {hard.mathboxStatus / earomControl} reset the math-box / EAROM control port
DE70: AD CA 01        LDA     $01CA               ; {hard.workRam+1CA} read the mode byte
DE73: D0 01           BNE     $DE76               ; {code.loc_de76} mode active: run a pass
DE75: 60              RTS                         

loc_de76:
DE76: AC CB 01        LDY     $01CB               ; {hard.workRam+1CB} y = which entry of the region is being serviced
DE79: AE CC 01        LDX     $01CC               ; {hard.workRam+1CC} x = position in the EAROM data window
DE7C: 0A              ASL     A                   ; shift the mode byte to select the sub-operation
DE7D: 90 0D           BCC     $DE8C               ; {code.loc_de8c}
DE7F: 9D 00 60        STA     $6000,X             ; {hard.earomWrite} stage a data byte into the EAROM data window
DE82: A9 40           LDA     #$40                
DE84: 8D CA 01        STA     $01CA               ; {hard.workRam+1CA} arm the write sub-mode (0x40)
DE87: A0 0E           LDY     #$0E                
DE89: B8              CLV                         
DE8A: 50 73           BVC     $DEFF               ; {code.loc_deff}

loc_de8c:
DE8C: 10 25           BPL     $DEB3               ; {code.loc_deb3}
DE8E: A9 80           LDA     #$80                ; set write mode
DE90: 8D CA 01        STA     $01CA               ; {hard.workRam+1CA}
DE93: AD C6 01        LDA     $01C6               ; {hard.workRam+1C6} read the blank flag
DE96: F0 04           BEQ     $DE9C               ; {code.loc_de9c} not blanking: keep the RAM byte
DE98: A9 00           LDA     #$00                
DE9A: 91 BD           STA     ($BD),Y             ; {hard.workRam+BD} blank the RAM byte through the region walk pointer

loc_de9c:
DE9C: B1 BD           LDA     ($BD),Y             ; {hard.workRam+BD} read the RAM byte through the region walk pointer
DE9E: EC CD 01        CPX     $01CD               ; {hard.workRam+1CD} reached the region limit?
DEA1: 90 08           BCC     $DEAB               ; {code.loc_deab} not yet
DEA3: A9 00           LDA     #$00                
DEA5: 8D CA 01        STA     $01CA               ; {hard.workRam+1CA} clear mode: region done
DEA8: AD CF 01        LDA     $01CF               ; {hard.workRam+1CF} at the limit, emit the running checksum instead

loc_deab:
DEAB: 9D 00 60        STA     $6000,X             ; {hard.earomWrite} stage the byte into the EAROM data window
DEAE: A0 0C           LDY     #$0C                
DEB0: B8              CLV                         
DEB1: 50 3F           BVC     $DEF2               ; {code.loc_def2}

loc_deb3:
DEB3: A9 08           LDA     #$08                
DEB5: 8D 40 60        STA     $6040               ; {hard.mathboxStatus / earomControl} begin the EAROM read handshake on the control port
DEB8: 9D 00 60        STA     $6000,X             ; {hard.earomWrite}
DEBB: A9 09           LDA     #$09                
DEBD: 8D 40 60        STA     $6040               ; {hard.mathboxStatus / earomControl} clock the control port
DEC0: EA              NOP                         
DEC1: A9 08           LDA     #$08                
DEC3: 8D 40 60        STA     $6040               ; {hard.mathboxStatus / earomControl} return the control port
DEC6: EC CD 01        CPX     $01CD               ; {hard.workRam+1CD} reached the region limit?
DEC9: AD 50 60        LDA     $6050               ; {hard.earomRead} read the EAROM read-back port
DECC: 90 20           BCC     $DEEE               ; {code.loc_deee} not at limit: store the byte
DECE: 4D CF 01        EOR     $01CF               ; {hard.workRam+1CF} at the limit, xor the read-back against the running checksum
DED1: F0 13           BEQ     $DEE6               ; {code.loc_dee6} zero means the region verified
DED3: A9 00           LDA     #$00                
DED5: AC CB 01        LDY     $01CB               ; {hard.workRam+1CB}

loc_ded8:
DED8: 91 BD           STA     ($BD),Y             ; {hard.workRam+BD} checksum mismatch: blank the region's RAM bytes back to front
DEDA: 88              DEY                         
DEDB: 10 FB           BPL     $DED8               ; {code.loc_ded8} loop until the whole region is blanked
DEDD: AD CE 01        LDA     $01CE               ; {hard.workRam+1CE}
DEE0: 0D C9 01        ORA     $01C9               ; {hard.workRam+1C9} record the failure by re-queuing the region bit
DEE3: 8D C9 01        STA     $01C9               ; {hard.workRam+1C9} into the pending-work flags

loc_dee6:
DEE6: A9 00           LDA     #$00                
DEE8: 8D CA 01        STA     $01CA               ; {hard.workRam+1CA} retire the mode byte -- region done
DEEB: B8              CLV                         
DEEC: 50 02           BVC     $DEF0               ; {code.loc_def0}

loc_deee:
DEEE: 91 BD           STA     ($BD),Y             ; {hard.workRam+BD} store the read-back byte through the region walk pointer

loc_def0:
DEF0: A0 00           LDY     #$00                

loc_def2:
DEF2: 18              CLC                         
DEF3: 6D CF 01        ADC     $01CF               ; {hard.workRam+1CF} fold the byte into the running checksum
DEF6: 8D CF 01        STA     $01CF               ; {hard.workRam+1CF} store the checksum accumulator
DEF9: EE CB 01        INC     $01CB               ; {hard.workRam+1CB} bump the per-region pass counter
DEFC: EE CC 01        INC     $01CC               ; {hard.workRam+1CC} bump the region byte cursor

loc_deff:
DEFF: 8C 40 60        STY     $6040               ; {hard.mathboxStatus / earomControl} write the exit code to the control port
DF02: 98              TYA                         
DF03: D0 03           BNE     $DF08               ; {code.loc_df08} nonzero exit: return, re-enter later
DF05: 4C 1B DE        JMP     $DE1B               ; {code.stepEaromTransfer} else loop to drain the next entry

loc_df08:
DF08: 60              RTS                         

; Stores the fixed body byte 0xc0 at the draw cursor origin loc_74 and
; runs the shared record-tail emit.
emitRecordBodyC0:
DF09: A9 C0           LDA     #$C0                ; fixed body byte 0xc0 -- the vector-generator opcode for this record class
DF0B: D0 05           BNE     $DF12               ; {code.emitRecordBodyByte} jump to the body-write step

; build a two-byte-header record: emit the {0x40,0x80} header via 0x74,
; then store the fixed body byte 0x20 at the cursor origin and run the
; shared record tail.
emitHeaderedBodyRecord:
DF0D: 20 53 DF        JSR     $DF53               ; {code.emitVectorHeaderWord} lay the record header word through the draw cursor
DF10: A9 20           LDA     #$20                ; fixed body byte 0x20, then fall into the body-write step

; store one body byte (A) at the display cursor origin (0x74)+0 and
; continue into the shared record tail (0xdfac).
emitRecordBodyByte:
DF12: A0 00           LDY     #$00                
DF14: 91 74           STA     ($74),Y             ; {hard.workRam+74} store the body byte at the draw-cursor origin
DF16: 4C AC DF        JMP     $DFAC               ; {code.emitRecordTailByte} continue into the shared record tail

; emit a stroke-table word: form a word index from A's low nibble (0 when
; carry set and nibble is zero, else nibble+1), double it, copy the two
; bytes of table 0x31e4[index] into the display list at cursor 0x74, and
; advance two.
emitStrokeWordFromNibble:
DF19: 90 04           BCC     $DF1F               ; {code.emitStrokeWordFromNibblePlusOne} carry clear: skip the zero-terminator test, use nibble+1
DF1B: 29 0F           AND     #$0F                ; keep the low nibble -- the glyph selector
DF1D: F0 05           BEQ     $DF24               ; {code.emitStrokeWordByIndex} carry set and nibble zero: select terminator glyph 0

; thin index wrapper: form the stroke-table index (A&0x0f)+1 and share the
; 0x31e4 copy-and-advance emit tail, laying that word into the display
; list at cursor 0x74.
emitStrokeWordFromNibblePlusOne:
DF1F: 29 0F           AND     #$0F                ; keep the low nibble
DF21: 18              CLC                         
DF22: 69 01           ADC     #$01                ; index = nibble + 1

; emit one glyph/stroke vector word by table index A: copy the two bytes
; of ROM stroke-table $31E4 entry ($31E4 + (A<<1)) into the vector list at
; write cursor mem16[loc_74] and step the cursor past them via
; advanceDisplayCursor (entry emitStrokeWordFromNibblePlusOne first maps a
; low nibble to index (nibble&0x0f)+1).
emitStrokeWordByIndex:
DF24: 08              PHP                         
DF25: 0A              ASL     A                   ; double the index -- stroke entries are 16-bit words
DF26: A0 00           LDY     #$00                
DF28: AA              TAX                         
DF29: BD E4 31        LDA     $31E4,X             ; {hard.vectorRom+1E4} read the glyph's first stroke byte from the vector-ROM stroke table
DF2C: 91 74           STA     ($74),Y             ; {hard.workRam+74} copy it into the display list at the draw cursor
DF2E: BD E5 31        LDA     $31E5,X             ; {hard.vectorRom+1E5} read the glyph's second stroke byte
DF31: C8              INY                         
DF32: 91 74           STA     ($74),Y             ; {hard.workRam+74} copy it to draw cursor +1
DF34: 20 5F DF        JSR     $DF5F               ; {code.advanceDisplayCursor} advance the draw cursor two bytes past the word
DF37: 28              PLP                         
DF38: 60              RTS                         

; Emits a coordinate vector word: high byte is a's upper nibble tagged
; 0xa0, low byte is x shifted right with a's carry rotated into bit7,
; written through loc_74 then advanced (or, on cursor wrap, tailing
; emitTaggedVectorWord with key loc_73).
emitCoordinateVectorWord:
DF39: 4A              LSR     A                   ; shift a right, low bit into carry
DF3A: 29 0F           AND     #$0F                ; keep a's upper nibble
DF3C: 09 A0           ORA     #$A0                ; tag the high byte with the 0xa0 vector-generator opcode
DF3E: A0 01           LDY     #$01                
DF40: 91 74           STA     ($74),Y             ; {hard.workRam+74} store the tagged high byte at draw cursor +1
DF42: 88              DEY                         
DF43: 8A              TXA                         
DF44: 6A              ROR     A                   ; rotate x right with a's old bit0 into bit7 -- the low byte
DF45: 91 74           STA     ($74),Y             ; {hard.workRam+74} store the low byte at the draw-cursor origin
DF47: C8              INY                         
DF48: D0 15           BNE     $DF5F               ; {code.advanceDisplayCursor} advance the draw cursor past the word

; Emits a vector word tagged 0x60 using the key byte loc_73 as its data
; byte through the draw cursor loc_74.
emitVectorWordTag60FromKey:
DF4A: A4 73           LDY     $73                 ; {hard.workRam+73} take the second payload byte from the current record-header key

; emit one vector word through cursor 0x74: first byte the Y payload,
; second byte the A payload tagged with header bits 0x60 (via $DF57).
emitTaggedVectorWord:
DF4C: 09 60           ORA     #$60                ; OR the 0x60 header tag into the payload byte
DF4E: AA              TAX                         
DF4F: 98              TYA                         
DF50: 4C 57 DF        JMP     $DF57               ; {code.emitVectorWord} lay the tagged pair into the display list via the shared vector-word writer

; emit the fixed {0x40,0x80} vector header word at the cursor 0x74 (0x40
; then 0x80 into display RAM) and advance the cursor two.
emitVectorHeaderWord:
DF53: A9 40           LDA     #$40                ; load the canonical beam-position header low byte 0x40
DF55: A2 80           LDX     #$80                ; load its high byte 0x80 -- the fixed record-opening header word

; lay one vector word into the display list: store A at cursor (0x74)+0
; and X at +1, then advance the cursor two via 0x74/0x75.
emitVectorWord:
DF57: A0 00           LDY     #$00                ; point at the draw cursor origin (offset 0)

; indexed word emit: store A at cursor 0x74 offset Y and X at Y+1, then
; advance the cursor past them by (Y+1)+1.
emitVectorWordAtOffset:
DF59: 91 74           STA     ($74),Y             ; {hard.workRam+74} store the word's low byte at draw cursor + y
DF5B: C8              INY                         
DF5C: 8A              TXA                         
DF5D: 91 74           STA     ($74),Y             ; {hard.workRam+74} store the word's high byte at draw cursor + y+1

; advance the 16-bit display cursor 0x74/0x75 by Y+1 (carry forced set),
; storing the new low byte at 0x74 and bumping high byte 0x75 on overflow;
; returns the new low byte in A.
advanceDisplayCursor:
DF5F: 98              TYA                         ; stride for the cursor advance = the offset just consumed
DF60: 38              SEC                         ; force the carry so the add yields stride + 1
DF61: 65 74           ADC     $74                 ; {hard.workRam+74} add stride+1 to the draw cursor low byte
DF63: 85 74           STA     $74                 ; {hard.workRam+74} store the advanced draw cursor low byte
DF65: 90 02           BCC     $DF69               ; {code.loc_df69} if no page overflow, done
DF67: E6 75           INC     $75                 ; {hard.workRam+75} carry the draw cursor into the next page

loc_df69:
DF69: 60              RTS                         

; Emits a 0x70-tagged vector word with a zero data byte through the draw
; cursor loc_74.
emitBlankVectorWordTag70:
DF6A: A0 00           LDY     #$00                ; zero the data byte for a blank 0x70-tagged record opener

; Emits one vector word through the draw cursor loc_74 -- first byte the y
; payload, second byte the a payload OR 0x70 -- then advances.
emitVectorWordTag70:
DF6C: 09 70           ORA     #$70                ; OR the 0x70 header tag into the payload byte
DF6E: AA              TAX                         
DF6F: 98              TYA                         
DF70: 4C 57 DF        JMP     $DF57               ; {code.emitVectorWord} lay the tagged word via the shared vector-word writer

; Stashes the index byte into the key cell loc_73, then scales the two
; coordinates and emits the scaled coordinate record.
emitKeyedScaledCoordinateRecord:
DF73: 84 73           STY     $73                 ; {hard.workRam+73} stash the record's key/index byte into the header cell (loc_73)

; Widens two input values by four with sign extension into the delta pairs
; loc_6e/loc_6f and loc_70/loc_71, then emits the coordinate record they
; anchor.
emitScaledCoordinateRecord:
DF75: A0 00           LDY     #$00                
DF77: 0A              ASL     A                   ; shift the first coordinate left (x2)
DF78: 90 01           BCC     $DF7B               ; {code.loc_df7b} if no sign bit shifted out, leave the sign fill zero
DF7A: 88              DEY                         ; else set an all-ones negative sign fill

loc_df7b:
DF7B: 84 6F           STY     $6F                 ; {hard.workRam+6F} store the first delta's high-byte sign fill (loc_6f)
DF7D: 0A              ASL     A                   ; shift again -- x4 total
DF7E: 26 6F           ROL     $6F                 ; {hard.workRam+6F} roll the shifted-out bit into the delta high byte
DF80: 85 6E           STA     $6E                 ; {hard.workRam+6E} store the first coordinate's scaled low byte (loc_6e)
DF82: 8A              TXA                         ; second coordinate into a
DF83: 0A              ASL     A                   ; shift the second coordinate left (x2)
DF84: A0 00           LDY     #$00                
DF86: 90 01           BCC     $DF89               ; {code.loc_df89} sign check for the second coordinate
DF88: 88              DEY                         ; set an all-ones negative sign fill

loc_df89:
DF89: 84 71           STY     $71                 ; {hard.workRam+71} store the second delta's high-byte sign fill (loc_71)
DF8B: 0A              ASL     A                   ; shift again -- x4 total
DF8C: 26 71           ROL     $71                 ; {hard.workRam+71} roll the shifted-out bit into the delta high byte
DF8E: 85 70           STA     $70                 ; {hard.workRam+70} store the second coordinate's scaled low byte (loc_70)
DF90: A2 6E           LDX     #$6E                ; anchor the coordinate record at the first delta pair (loc_6e)

; Emits a four-byte coordinate record from the zeropage slots off x --
; loc_2+x, loc_3+x masked 0x1f, loc_0+x, and a key-folded 5-bit loc_1+x --
; through the draw cursor loc_74.
emitCoordinateRecord:
DF92: A0 00           LDY     #$00                ; point at the draw cursor origin
DF94: B5 02           LDA     $02,X               ; {hard.workRam+2} read coordinate source byte (loc_2 + x)
DF96: 91 74           STA     ($74),Y             ; {hard.workRam+74} write it at draw cursor +0
DF98: B5 03           LDA     $03,X               ; {hard.workRam+3} read source byte (loc_3 + x)
DF9A: 29 1F           AND     #$1F                ; clip to five bits
DF9C: C8              INY                         
DF9D: 91 74           STA     ($74),Y             ; {hard.workRam+74} write at draw cursor +1
DF9F: B5 00           LDA     $00,X               ; {hard.workRam} read source byte (loc_0 + x)
DFA1: C8              INY                         
DFA2: 91 74           STA     ($74),Y             ; {hard.workRam+74} write at draw cursor +2
DFA4: B5 01           LDA     $01,X               ; {hard.workRam+1} read the key-folded source byte (loc_1 + x)
DFA6: 45 73           EOR     $73                 ; {hard.workRam+73} XOR with the record header key (loc_73)
DFA8: 29 1F           AND     #$1F                ; keep only the low five bits re-keyed
DFAA: 45 73           EOR     $73                 ; {hard.workRam+73} XOR the key back so the top three bits come from the key

; Stores one final record byte at the next draw-cursor slot loc_74 and
; either advances the cursor or, on wrap to zero, runs the terminating
; nibble run.
emitRecordTailByte:
DFAC: C8              INY                         ; advance to the record's tail slot
DFAD: 91 74           STA     ($74),Y             ; {hard.workRam+74} write the key-folded fourth byte at the tail slot
DFAF: D0 AE           BNE     $DF5F               ; {code.advanceDisplayCursor} if the slot index has not wrapped to zero, advance the cursor -- else terminate the run

; Emits a run of y zeropage bytes from the top index a+y-1 downward, each
; byte as its high then low nibble via the glyph-word lookup, chaining
; carry so only the final low nibble sees carry cleared as the terminator.
emitNibbleDigitRun:
DFB1: 38              SEC                         ; seed the carry set for the digit run
DFB2: 08              PHP                         
DFB3: 88              DEY                         ; run counter = length - 1
DFB4: 84 AE           STY     $AE                 ; {hard.workRam+AE} store the run counter (loc_ae)
DFB6: 18              CLC                         
DFB7: 65 AE           ADC     $AE                 ; {hard.workRam+AE} index = run base + count -- the top byte of the run
DFB9: 28              PLP                         
DFBA: AA              TAX                         ; working index into x

loc_dfbb:
DFBB: 08              PHP                         
DFBC: 86 AF           STX     $AF                 ; {hard.workRam+AF} save the working index (loc_af)
DFBE: B5 00           LDA     $00,X               ; {hard.workRam} fetch the packed byte at the run base + x
DFC0: 4A              LSR     A                   ; shift the packed byte's high nibble down into the low four bits
DFC1: 4A              LSR     A                   
DFC2: 4A              LSR     A                   
DFC3: 4A              LSR     A                   
DFC4: 28              PLP                         
DFC5: 20 19 DF        JSR     $DF19               ; {code.emitStrokeWordFromNibble} emit the high nibble as a glyph stroke word
DFC8: A5 AE           LDA     $AE                 ; {hard.workRam+AE} reload the run counter
DFCA: D0 01           BNE     $DFCD               ; {code.loc_dfcd} if not the last byte, keep the propagating carry
DFCC: 18              CLC                         ; last byte -- force the carry clear as the run terminator marker

loc_dfcd:
DFCD: A6 AF           LDX     $AF                 ; {hard.workRam+AF} restore the working index
DFCF: B5 00           LDA     $00,X               ; {hard.workRam} re-fetch the packed byte for its low nibble
DFD1: 20 19 DF        JSR     $DF19               ; {code.emitStrokeWordFromNibble} emit the low nibble as a glyph stroke word
DFD4: A6 AF           LDX     $AF                 ; {hard.workRam+AF}
DFD6: CA              DEX                         ; step to the previous byte of the run
DFD7: C6 AE           DEC     $AE                 ; {hard.workRam+AE} decrement the run counter
DFD9: 10 E0           BPL     $DFBB               ; {code.loc_dfbb} loop while the counter stays non-negative
DFDB: 60              RTS                         

; ---- $DFDC-$DFFF: data ----
DFDC: 10 10 40 40 90 90 FF FF 00 0C 16 1E 20 1E 16 0C
DFEC: 00 F4 EA E2 E0 E2 EA F4 00 0C 16 1E 00 00
  
DFFA: 04 D7  ; NMI vector to D704
DFFC: 3F D9  ; RESET vector to D93F
DFFE: 04 D7  ; IRQ vector to D704
```

