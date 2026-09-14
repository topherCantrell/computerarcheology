![Pooyan](pooyan.jpg)

# RAM Usage

Work RAM lives at `0x8800`–`0x8FFF`. Each name below describes the cell by its role in
the running game; the hex address is the stable identity. Cells that share a byte, or
whose role is only partly pinned, carry a terse caveat.

>>> memory

| Address | Name | Description |
| --- | --- | --- |
| 8800 | bonusAwardDsw | (both goldens static 0 (DSW1 bit3=0 default) -> unobservable/code; runSelfTestAndInitMachineState boot cpl's the DSW1 port then decodes ~(bit3) here, advanceBonusAwardQueueAndBumpGauge picks award queue 5/3 & step 8/7 off it) DSW1 bit3 (complemented, boot-only): selects bonus/extra-life award schedule -- queue reload 5/3, BCD step 8/7 |
| 8802 | creditCount | (gameplay golden: coin at f302 -> 0->1, 1P start at f362 -> 1->0 (credit added then consumed); static 0 in attract = credit counter, REFUTES A's score-drip) BCD credit counter (max 0x63): coin +1, 1P start consumes 1, 2P start consumes 2; drawn as 2 HUD digits |
| 8805 | mainGameState | (attract cycles 0/1/3, gameplay 0->1->2->3 (distinct=4) discrete states; runVblankNmiService indexes table 0x06f0 on (0x8805)) top-level NMI state selector dispatched via table 0x06f0 (072d/0899/0c4e/159b/0e53): attract/intro/play |
| 8806 | gameActiveFlag | (gameplay: 0->1 at f362 (game start, coincides 0x8805->3), 1->0 at f4324 (game over); static 0 in attract) in-play gate: set 1 at start-of-life, cleared 0 at game-over; gameplay handlers ret early when 0 |
| 8807 | livesDsw | cabinet lives-count byte (from the lives DSW), seeded into both players' lives at board reset |
| 8808 | phaseTimer | (gameplay distinct=256, wraps 0->255, 530 transitions = a per-frame countdown timer reloading/wrapping; selectRoundDisplayListAndAdvancePhase 'dec (0x8808)... |
| 8809 | fillRowCounter | (both goldens: 0->32 then decrement 32..0 per frame, repeated (420/468 trans); loc_02e6 seeds 0x20, blankFillRowAndStepCounter/fillIntroRowsThenBuildBoardIntro walk down) down-counter (seeded 0x20) for the row-by-row VRAM tile fill; zero ends the fill and advances state |
| 880a | playStateIndex | (steps discrete phase values 1/2/3/4/7/10/13/18 (gameplay distinct=12); dispatchInPlaySubState dispatches (0x880a)&0x1f via table 0x15a8) in-play sub-state index (&0x1f) dispatched via table 0x15a8; stepped through round/intro phases |
| 880b | tileFillPtr | (low byte steps +32 (0,32,64,..,224,0) with 465 transitions; loc_02e6 stores HL, blankFillRowAndStepCounter fills B tiles then adds 0x20-B) 16-bit VRAM write cursor for the row-by-row tile fill, advanced +0x20 per row (paired with 0x8809) |
| 880d | activePlayer | (MAME 2P golden: toggles P1<->P2 exactly on swaps -- 0->1 at P1 death f2854, 1->0 at P2 death f7129; the f319 scratch 0x1f is loc_075d's leftover stored by fetchWordFromTableIndex, not a player value) active-player select; bit0=0 -> P1 banks (score 0x88a2/counter 0x88a4), 1 -> P2 (0x88a5/0x88a7) |
| 880e | twoPlayerFlag | (MAME 2P golden: 0->1 at 2P start f402, holds 1; static 0 in the 1P golden = positive control; startNewGamePlay sets 1 on 2P start, startGameOnStartButtonPress picks player bank when nonzero) nonzero for a 2-player game; gates per-player bank selection (with 0x880d) and the 2P start event |
| 880f | cabinetModeFlag | cabinet/cocktail flag (DSW1 bit2 complemented, boot-decoded); read by round-init (initRoundArenaAndRestorePlayerBank) as a boolean to gate cocktail/flip handling |
| 8810 | inputPort0 | (gameplay: bit0=1 at f302 (coin), bit3(val 8) at f362 (1P start); runVblankNmiService writes cpl(IN0 @a080) here each NMI) inverted IN0 sample (head of 0x8810-0x8812 edge-detect ring): coin bit0, 1P-start bit3, 2P-start bit4 |
| 8811 | inputPort1 | inverted active-high sample of IN1 (P1 controls); cell 2 of the 0x8810 input edge-detect ring, sampled each vblank NMI by runVblankNmiService |
| 8812 | inputPort2 | inverted sample of IN2 (P2 controls); cell 3 (tail) of the 0x8810 input edge-detect ring, sampled each vblank NMI by runVblankNmiService |
| 881e | tamperFreezeFlag | (static 0 in BOTH goldens (ROM intact) -> code; only bumped by checksum guards (rebuildFieldAndLatchPlayStateWithTamperCheck !=0x7c, seedFirstFreeSlotForTimedSpawnWithTamperCheck signature), aborts actors (advanceLeadActorPrimaryState), traps spawn (runPhase1LauncherThenDriver) -- REFUTES B's round-active (would go nonzero during a round)) anti-tamper miss tally bumped by ROM/signature checksum guards; nonzero freezes spawns, aborts actor updates, skips HUD setup |
| 881f | flipScreenFlag | (both goldens: 0->1 at f32 (boot init to normal orientation), held; runVblankNmiService epilogue copies (0x881f)->0xa187 b7, tickCounterAndMirrorIfFlipped gates mirror pass when ==0) screen orientation flag copied to flipscreen latch 0xa187 b7 each NMI; 1=normal (upright), gates the vertical-mirror pass |
| 8820 | difficultyDsw | (static 0 in both goldens (difficulty 0) -> unobservable/code; runSelfTestAndInitMachineState boot cpl's the DSW1 port then writes (~DSW1>>4)&0x07 (only writer), spawnFormationEnemyOnInterval/spawnShotTargetOnInterval/loc_39fb threshold spawns on it) 3-bit difficulty (DSW1 bits4-6, complemented, boot-only); scales enemy spawn schedules and tier/threshold tables |
| 8821 | demoSoundsDsw | DSW1 bit7 complemented (boot-only; decoded in runSelfTestAndInitMachineState): demo/attract sounds enable; bit0 gates queued sound dispatch when the game is idle |
| 8824 | coin1PulseCount | (gwtrace pc=5a6c inc (0x8824) 0x00->0x01 at a coin accept; decremented one per completed strobe by the coin-1 pulse generator) coin-counter 1 queued-pulse count |
| 8825 | coin1PulsePhase | coin-counter 1 pulse phase timer (seeded 0x30, drop point 0x18) |
| 8826 | coin2PulseCount | coin-counter 2 queued-pulse count: bumped by the per-frame coin step at 0x5a1f and drained one per completed strobe by the coin-2 pulse generator; twin of COIN1_PULSE_COUNT (0x8824) |
| 8827 | coin2PulsePhase | coin-counter 2 pulse phase timer (seeded 0x30, drop point 0x18) |
| 8829 | dripRingA | drip ring a (0x8829) |
| 882a | dripRingC | variant-C drip debounce ring: one input bit rotated in per frame, acted on at 3-bit phase 1 (sibling of DRIP_RING_A=0x8829) |
| 882b | scoreDripAccum | score-drip accumulator: the coin-1 drip step (accrueCreditFromCoin1Pulse) steps it +0x10 with a carry into COINAGE_CONFIG, and the play-state actor handler (advancePlayStateToPhase7OnActorDelay) stamps 0x07 into it; the loc_585b ROM-checksum writer that sets it to 1 is a secondary, unreached facet |
| 882c | coinageConfig | (both goldens: 0->1 at f32 (boot seeds coinage=1c/1c via table 0x0053, 0x882f gets hi nibble); serviceCoinCreditAndCountersUnlessFreePlay/resetToBoardBuildToContinuePlay/queueCreditDisplayCommands test ==0x0f free play (A's slot-B label unverified)) coin-slot coinage nibble from DSW0 low nibble via table 0x0053; 0x0f = free play; read by credit logic |
| 882d | dripRingB | cadence ring for the per-frame step at 0x5a1f: rotated left each frame injecting an input-port bit; low 3 bits == 1 triggers the step |
| 882e | dripCoordB | first byte of the 0x5a1f step's pair (0x882e/0x882f; neighbor COINAGE_CONFIG_SLOT2): advanced +0x10 per step, wrapped against the second byte |
| 882f | coinageConfigSlot2 | coin-slot-2 coinage nibble, from the DSW0 high nibble via the coinage table; 0x0f = free play; read by serviceCoinCreditAndCountersUnlessFreePlay (sibling of COINAGE_CONFIG 0x882c) |
| 883f | workerControlByte | per-frame worker control byte (one below SPRITE_DISPLAY_LIST): low nibble != 0 gates the program-signature check, bit 4 gates the final scroll-column blank |
| 8840 | spriteDisplayList | (attract+play: byte0 0->176 then descends ~1 per 2f (35/40 distinct) = a live sprite Y at the list base; rebuildSpriteDisplayList builds it, loc_0378 mirrors 24 entries) Base of the 24-entry x4 sprite display list; byte0 is the first sprite's Y, rebuilt each frame, swept for collisions |
| 8842 | playerXCoord | Launcher/player position coordinate; shifted >>3 (rrca x3 & 0x1f) with the flip-screen flag to derive the target column used to align an enemy shot. |
| 8848 | spriteActorRecordSlots | (attract 1766 / play 2735 transitions, byte descends by 3 = an actively-rewritten sprite record region (sweepActorRecordSlotsBothParitiesOnOddRound/5f6a walk it)) Stride-4 actor-record slots inside the sprite display list, swept B=2 by the display/DMA drivers (gated on 0x8907 bit0) |
| 8850 | enemyScanBoxTable | enemy scan box table (0x8850) |
| 8852 | spriteScanYslots | stride-4 sprite y-coordinate slots (6 scanned) tested for the closest in-band aim target vs the player's y (SPRITE_DISPLAY_LIST+2) |
| 8868 | spriteScanActorSlots | stride-4 actor coordinate slots (base IX, 5 scanned) swept by the object-record proximity scan; +0 (x)/+2 (y) is the moving actor tested against each object record |
| 887c | spriteTargetSlots | (attract 1410 / play 951 transitions, range to 248 = live sprite-coordinate target slots (scanProximityTargetPairsAgainstSource/5df7 IY=0x887c, scanObjectBankForActorCollision player-2)) Stride-4 target/collision slots in the sprite list, scanned as proximity targets vs 0x8be8 records (player-2 set in 2P split) |
| 8888 | formationCoordSlots | formation coord slots (0x8888) |
| 888c | spriteTargetSlotsP1 | player-1 stride-4 target/collision coordinate slots scanned vs the 0x8c48 records (counterpart of 0x887c/SPRITE_TARGET_SLOTS; selected when PLAY_MODE_LATCH==0) |
| 889c | proximitySourceObject | (MAME: 0x889c written 00->c0 n=11038 as byte-0 of a display-list object entry (alongside 0x889d=00->40,0x889e=00->56,0x889f=00->16) — confirms PROXIMITY_SOURCE_OBJECT 'sits inside the sprite display list') fixed source object record scanned for proximity by scanProximityTargetPairsAgainstSource (screen X at +0, Y at +2); sits inside the sprite display list |
| 88a0 | displayCmdRingWritePtr | low-byte write pointer into the display-command ring (page 0x88), advanced by two per enqueue and clamped up to 0xc0 |
| 88a1 | displayCmdRingReadPtr | read/dispatch cursor into the display-command ring (walks 0xc0..0xff, indexes page 0x88); read+advanced by loc_020f / mainLoopStep (paired with write ptr 0x88a0) |
| 88a2 | p1ScoreBcd | (MAME 2P golden: buffer accumulates during P1's turn only -- mid byte 0x88a3 0->0x14 while ACTIVE_PLAYER=0, frozen after the swap; base 0x88a2 low BCD pair stays 0 (scores x100) so; loc_04f2 selects this vs P2_SCORE_BCD off ACTIVE_PLAYER) player-1 live 3-byte BCD score buffer (0x88a2..0x88a4) |
| 88a5 | p2ScoreBcd | (MAME 2P golden: buffer accumulates during P2's turn only -- mid byte 0x88a6 0->0x78 while ACTIVE_PLAYER=1, frozen otherwise; base 0x88a5 low BCD pair stays 0 (scores x100) so; loc_04f2 P2 bank) player-2 live 3-byte BCD score buffer (0x88a5..0x88a7) |
| 88a8 | highScoreBcd | LSB of the 3-byte BCD high-score counter (0x88a8..0x88aa, MSB at 0x88aa) |
| 88aa | highScoreBcdHi | (attract+play: 0->1 at f65 then held = default high score 10000 (MSB byte 0x01), rarely written; accrueScoreAndUpdateHighScore compares descending from 0x88aa) MSB of the 3-byte BCD high score (0x88a8..0x88aa); a new score is compared MSB-first here and copied down if higher |
| 88ab | perFrameScoreIncrement | 3-byte BCD per-frame score increment added to the active player's score when the award index is 0 |
| 88b7 | subphaseTick | (cycles 0..27 (28 distinct), 457 transitions = mod-0x1c counter) period-0x1c frame tick; on wrap advances the 0x8920 display sub-phase one-shot |
| 88b8 | displayListDstPtrAlt | (MAME: Written 308x by paintDisplayListRunToVram (whose interpreter role is confirmed), value 0x8462->0x87c2 -- a live pointer INTO video RAM (0x8400-0x87ff), i.e. the paint destination. |
| 88ba | displayListSrcPtrAlt | (MAME: Written 308x by paintDisplayListRunToVram, value 0x43eb->0x4872 -- a live pointer INTO the display-list stream table (0x43e1-0x4a0a in ROM), i.e. the layout source. |
| 88bc | statusRenderPhase | (MAME: inc n=229 gated on 0x88bd wrap-to-0, v0=03 vN=03) status render phase (0x88bc) |
| 88bd | statusRenderRing | (MAME: inc then AND 0x07, n=3748, values cycling 06->02) status render ring (0x88bd) |
| 88be | tileAnimCursor | (both goldens: high byte 0x84 (VIDEO RAM), low byte oscillates 0xe6-0xf0; loc_2405 (odd frames)/loc_23ec (even) dereference it and WRITE tile codes -- not ROM) 16-bit cursor into video RAM (0x84xx tilemap) marching a tile strip forward on odd frames / back on even, cycling tile codes 0x10/0x34/0x37 to animate on screen (0x34/0x37 gate the step) |
| 88c0 | displayCmdRingBuffer | base of the display-command ring buffer (0x88c0-0x88ff, 32 two-byte slots); boot fills 0xff (empty); read via computed page-0x88 addressing by the main loop |
| 8900 | speedIndex | (MAME round-advance capture: escalates 0->2->4->..->14 = 2x round as round steps 1->7; initChildActorRecordFromParent/379d speed-table index, pickEnemyGroupSpeedAndClearAim escalating write) Enemy speed/difficulty index, read clamped <8 to index velocity tables (negated per 0x8907 bit0); escalates with wave/round |
| 8901 | stageCountdown | (gameplay 0x20 then slow decrement 32->..->25 = per-stage countdown) counts down from 0x20 over a stage; near 0 gates actor AI; init value selects the stage label |
| 8902 | spawnPhaseCounter | (MAME round-advance capture: cycles per-round 0->1 f1291, 1->2 f7618, 2->3 f7750; static 0 without a round poke; armSirenAndTickWaveEventCountdown mode-select, resetBoardRamAndReseedSpawnCounters reseed at 7) Per-round phase/step counter (cycles to 7) selecting spawn/fire mode branches; snapshotted into 0x8d43/0x8934 |
| 8903 | waveArrivalCounter | (play: counts up 0..6 per stage then resets at transition = a per-stage arrival/wave counter (advanceEnemyToArrivalAndTallyWave bump, advanceActorState2AndCapWaveArrival cap, addRopeSegmentAndAdvanceExtendState rope bound)) Per-stage counter bumped on enemy arrival (caps 9->8); bounds the rope-segment count (0x8931 <= this-2), parity picks spawn variant |
| 8904 | roundInProgress | (attract+play: 0/1 flag, 1 while a round runs, resets at stage/life transitions (startRoundAfterIntroDelay/1798 set, paintPlayfieldAttributeMapForVariant/16b7 read)) In-progress flag for the active round; set to 1 at level start, keys render/state decision trees |
| 8907 | roundCounter | (MAME round-advance capture: increments per stage transition -- natural 2->3 f2059, 3->4 f2431 beyond the poked value; bit1 gates target-group fan-out, bit0 the rope path; drawStageLabelOncePerLevel/1ead BCD render) Round counter; +1 BCD-rendered as the HUD round number; bit0 selects stage-type/facing variant, low bits index difficulty tables |
| 8908 | gaugePhaseCounter | (play: 3->2->1->0 then reset to 3; exhaustion runs advancePlayStateThenInsertHighScore (phase transition, not death) rendered by loc_03c2 = a phase gauge) Phase counter drained per phase, drawn as a 5-cell vertical HUD gauge; on reaching 0 it triggers phase-exhausted (clears rope) |
| 8909 | awardQueue | pending bonus-award queue value (BCD threshold): 0 reloads the slot (5/3 per BONUS_AWARD_DSW), else gated vs the active player's score MSB then BCD-stepped (8/7) |
| 8920 | formationSlotTable | (both goldens: byte0 cycles 0/1/2 = the 0x88b7-wrap display one-shot (startRoundAfterIntroDelay/7517 inc/test/clear); the pointer-table role (dispatchFormationPhaseOrQueueLaunchSlots/30f1 register 4 formation slots, stride 2) is unobserved -- no formation spawned in 180s) display sub-phase one-shot (byte0, fired on the 0x88b7 mod-0x1c wrap); byte0 also the base of the 4-slot enemy-formation pointer table (stride 2) |
| 8921 | selftestDispatchState | attract/self-test state selector (masked &3) dispatched by dispatchSelfTestState to handlers 0x744e/0x7517/0x755d; runDisplayListAndAdvanceToGameplay is state 1 and advances it to state 2 |
| 8922 | wolfLaunchVariantIndex | cursor into the wolf launch-variant table (0x8922) |
| 8928 | frameTimerBlockBase | base of the 9-byte per-frame timer/flag block (0x8928..0x8930) cleared at screen re-init (byte before SHARED_FRAME_DELAY_TIMER=0x8929) |
| 8929 | sharedFrameDelayTimer | shared per-frame delay/timer counter; decremented while nonzero to gate several object-update sweeps (ascendEnemyActorAndLinkedSlotOnTimer/6905/756d/6523), reseeded by their handlers |
| 892a | blinkCountdown | blink-timer countdown (reload 0x16); decremented per tick, on 0 toggles the phase |
| 892b | blinkPhase | (MULTIPLEXED, role contested: MAME shows the blink path (blinkTilePairOnCountdown/0x76af) toggle it in step with the tile swap (n=30), while the object-anim path seeds it 0x08 (spawnActorGroupRecords) and decrements/reloads it as a countdown (cycleActorGroupSpriteFramesOnTimer/0x66a1); kept code) blink path: phase byte toggled on 0x892a expiry, parity selects the tile pair |
| 892c | animPhaseToggle892c | toggle byte incremented when the flip countdown (0x892f) expires; bit0 selects the grow (even) vs shrink (odd) animation half and the render tile-source row |
| 892d | waveNumber | wave/stage progression index (0..8): incremented per wave (launchWolfIntoSlot/756d), gated at >=8 = all-waves-done (spawnPairedEnemyOnDelaySweep), indexes the wave-param table; runObjectsElseVerifyTilemapChecksum arms its tilemap integrity check at ==2. |
| 892e | sharedPhaseCountdown | shared per-frame phase/animation countdown reloaded to 0x12 (also used by spawnEnemyTargetOrAnimateLaunchFlipTile/dispatchEnemyActorAnimTickState) |
| 892f | launchFlipCountdown | (MULTIPLEXED w/ the 0x65xx eagle path (both write/dec); kept code; observed MAME: pc 27fd dec (n=3492), 27ff reload 0x10 (n=216); expiry increments 0x892e at 2802; sibling 27ca reseeds to 8 (v 08->08, n=20)) frame countdown reseeded to 8 by this handler and decremented by spawnEnemyTargetOrAnimateLaunchFlipTile; on reaching 0 it drives the 0x892e tile-flip bit |
| 8930 | sharedPhaseGate | boolean gate flag enabling the shared actor phase countdown (written by animateActorGroupGrowShrink) |
| 8931 | ropeSegmentCount | (play: up-counter 0..4, resets to 0 at phase exhaustion (f3778); static 0 in attract (no rope); addRopeSegmentAndAdvanceExtendState steps it, retractRopeSegment retracts) Count of extended rope segments; stepped up to 0x8903-2; drives per-segment retract anim and the attribute byte |
| 8932 | markerLayoutPtr | work-RAM word holding the saved round-marker layout pointer |
| 8934 | ropeDrawCount | (MAME round-advance capture: mirrors 0x8902 one frame later -- 0->1 f1292 vs 0x8902 f1291, 1->2 f7623) rope/lift segment draw count (snapshot of 0x8902 phase, reseeds to 4 at 7); sets rope sprite rows |
| 8940 | player0StateBank | (MAME 2P golden: block saved on P1 death f2854 -- byte1 0x8941 0x20->0x1a via saveLivePageToPlayer0Bank; base byte0=colour stays 0 (source 0x8820=0) so) Base of player-0's 0x3f-byte saved actor/state block, swapped with live page 0x8900; byte0=sprite colour |
| 8948 | player0Lives | (Gameplay golden: 0->3 (seed=default 3 lives) then 3->2->1->0 drain per death, then ->3 for next game. |
| 8980 | player1StateBank | (MAME 2P golden: block saved on P2 death f7129 -- byte1 0x8981 0x20->0x0f; base byte0=colour stays 0 (source 0x8820=0) so) Base of player-1's 0x3f-byte saved actor/state block, swapped with live page 0x8900; byte0=sprite colour |
| 8988 | player1Lives | (Both goldens: 0->3 (seed=lives DSW), gameplay 3->0->3 reset pattern parallel to 0x8948. |
| 89c0 | panelDigitSourceTable | work-RAM source table (ten 3-byte rows) rendered as packed-BCD digit pairs into the digit panel |
| 89e0 | highScoreTimeTable | top of the per-entry play-time side table (3-byte stride) shifted alongside the high-score table on insert; the new entry's two play-timer BCD bytes are stored into the opened slot |
| 89e1 | playTimerGateP1 | gate byte for the player-0/1 BCD play-timer; nonzero suppresses the per-frame tick |
| 89e2 | playTimerGateP2 | gate byte for the player-1/2 BCD play-timer; nonzero suppresses the tick |
| 89e5 | boardClearFlag | (Static 0 both goldens (no board completed in capture). |
| 89e7 | integrityFlagScanBase | base of a 7-byte flag block scanned after the timer render; the first nonzero flag diverts to the tail integrity checksum |
| 89e8 | tamperStrikesSlotsweep | anti-tamper strike counter bumped when the slot-sweep code-block checksum misses its sentinel; also read by the eagle-spawn handler |
| 89e9 | tamperStrikesObjmove | anti-tamper strike counter (integrity flag block +2) (0x89e9) |
| 89ea | creditTamperCounter | RAM counter incremented when the credit-consume integrity checksum folds nonzero |
| 89eb | tamperStrikesCatch | tamper strikes catch (0x89eb) |
| 89ed | tamperStrikesState0 | anti-tamper strike counter (last slot of the 7-flag integrity table at INTEGRITY_FLAG_SCAN_BASE=0x89e7) bumped when the state-0 code-window checksum misses its 0x55 running-sum sentinel |
| 89ef | tamperStrikesRom | (static 0 (ROM intact) -> code) anti-tamper strike counter bumped when the 0x64be ROM checksum misses its sentinel |
| 89f0 | displayMsgBuf | (Both goldens: toggles 0<->0x0a (tile code written then cleared). |
| 89fb | tamperObjectFreezeFlag | anti-tamper flag (set by the resetToAttractScreenStart guard, cleared at reset by resetBoardRamAndReseedSpawnCounters); ORed with BOARD_CLEAR_FLAG to freeze the per-frame object update |
| 89fc | highScoreInsertRank | high-score insert rank+1: set to the winning rank plus one when a new score is inserted |
| 89fd | wipeColumnVramPtr | 16-bit tilemap pointer for the column wipe, built from WIPE_COLUMN_VRAM_BASE; the fill in dispatchRoundEndElseWipeColumn walks it stride +0x20 for 0x1c cells |
| 89ff | wipeColumnFillTile | fill tile value for the column wipe; seeded to 0x07 here, incremented each pass in dispatchRoundEndElseWipeColumn and clamped 0x10->0x06 |
| 8a00 | highScoreTable | (Static 0 both goldens (top-score MSB stays 0 in short capture). |
| 8a30 | playTimerBcdP1 | player-0/1 BCD play-timer bank: base byte = per-frame sub-counter (rolls at 0x3b/0x3c), +1/+2 = BCD seconds/minutes digits |
| 8a33 | playTimerBcdP2 | player-1/2 BCD play-timer bank (frame sub-counter + BCD seconds/minutes) |
| 8a38 | tamperStrikesSig | (static 0 (ROM intact) -> code) anti-tamper strike counter bumped when the 0x5328/0x557f signature checksums miss their sentinel |
| 8a39 | tamperStrikesState10 | (loc_3fe9 state-10 integrity guard bumps it on a checksum bit-pattern failure; adjacent TAMPER_STRIKES_SIG) anti-tamper strike counter for the state-10 ROM checksum |
| 8a3a | tamperStrikesObjsig | anti-tamper strike counter (object signature), sibling of tamper_strikes_sig (0x8a3a) |
| 8a3c | tamperStrikesHudGuard | anti-tamper strike counter bumped when the credit-draw checksum tripwire misses its 0x8c sentinel |
| 8a40 | soundRingWritePtr | sound-command ring buffer write/tail pointer (0x43..0x5e, wraps); enqueueSoundCommandRing stores into the slot it points at |
| 8a41 | soundRingReadPtr | sound-command ring buffer read/head index (0x43..0x5e, wraps); the slot it points at is consumed then freed |
| 8a43 | soundRingBuffer | base of the sound-command ring buffer (slots 0x8a43-0x8a5e); boot fills 0xff (empty); confirmed by enqueueSoundCommandRing |
| 8a5f | frameCounter | (Both goldens: 256 distinct, ~10.8k transitions, decrements 255->254->253... |
| 8a80 | actorTable | (Both goldens: slot-0 field0 toggles 0<->1 exactly when the player becomes active (gameplay f1090, same frame 0x8a84 starts moving). |
| 8a82 | leadActorState | (Both goldens: steps 0->1->2->3->4->5->0 in ~16-frame intervals, matching the 6-entry dispatch table (advanceLeadActorPrimaryState reads (ix+2)&7 -> 0x2442..0x24fb; advanceLeadActorDescentToLanding inc's it). |
| 8a84 | playerY | (Both goldens: smoothly varies 0..225 (elevator motion; attract decrements, gameplay increments). |
| 8a87 | playerAimFlags | (MAME: takes nonzero aim values in play -- 0x8a87=0x04 (pc 6d0d/71f8 n=611/240), 0x08 (pc 71f5/6bfa), 0x18 (pc 6d12 n=490), 0x10 (pc 7226); cleared to 0 by loc_7292 in the eagle-phase reset. |
| 8a91 | leadActorFrameDelay | (MAME: dec each entry then reseed to 0x30 on expiry, n=12 v0=01 vN=30) lead actor record frame-delay byte (actor_table+0x11) (0x8a91) |
| 8a98 | actorTableSlot1 | (MAME: pc=245a writes the contiguous 0x18-byte range 0x8a98..0x8aaf in one pass = the 0x18-byte lead-record copy into slot 1, matching the documented role.) second 0x18-stride actor record slot (ACTOR_TABLE + 0x18); beginLeadActorLiftOnClear snapshots the lead record here |
| 8ab4 | arrowY | (MAME: n=3782 v0=49 vN=46, exactly 0x8acc(baseY)-0x10 each frame) actor-record Y of the arrow/launch object (slot 2, ix+4); launch state machine gates on it (>=0x3c here, >=0x34 in state 1) |
| 8ae0 | enemyActorTable | (byte0 toggles 0/1, 30 transitions = live record-active flag) enemy actor record sub-array (stride 0x18) at +0x60 in the 0x8a80 arena; byte0 = record-active |
| 8afa | enemyRecDispatchGate | gate byte: when zero, dispatchSpecialObjectRecordState skips the 0x8b28 enemy-record state dispatch |
| 8b70 | spriteObjectTable | (attract+play: byte0 toggles 0/1 (38/30 transitions) = slot-active flag; spawnChildActorIntoFreeSpriteSlot scans 5 slots stride 0x18 for a free one) Base of the secondary 5-slot object/sprite record pool (stride 0x18); slot free when byte0/1 bit0 clear |
| 8ba0 | objectStateRecordBase | (MAME: 0x8ba0=00, 0x8ba1=01, 0x8ba2=08 (n=4 each), +0x12=0x8bb2=ff, +0x16/17=0x8bb6/b7=04/04; play) base of the 6-slot per-frame object-state record array (stride 0x18, spans into PROJECTILE_TABLE at 0x8be8) swept by dispatchAllObjectStates via dispatchActiveObjectState |
| 8be8 | projectileTable | (attract+play: byte0 toggles 0/1 (50/38 transitions); launchProjectileIntoFreeSlot allocates a free slot (bumps 0x8d42) and writes byte0=1) Base of the 3-slot projectile/object record table (stride 0x18); launch marks byte0=1 active |
| 8bea | projectileSlotState | (MAME: 0x3e69 increments 0x8bea via incMem8(ix+0x02) at pc=3e99 from 0x0b to 0x0c, handing the slot to the state-12 in-flight mover (0x3e9c), which then runs on it -- confirming +2 is the dispatch…) state byte (+2) of each of the 3 projectile-table slots (0x8be8, stride 0x18); drivePhase1RecordsThenCheckCompletion gates phase-1 completion on all three being idle (also coincides with the +2 state bytes of enemy-actor records 11/12/13 at 0x8ae0) |
| 8c00 | hunterCounterPage | base page of the per-slot hunter-return paced counters; a slot's counter cell is this \| ((field-0 + 5) & 0xff) |
| 8c30 | formationTable | (MAME round-advance capture: byte0 record-active toggles 0<->1, 35 transitions from f1863, only under a round-gated formation; dispatchFormationObjectStates sweeps 4 records stride 0x18) Base of the 4-slot formation object table (stride 0x18); one-shot spawn/init, swept per-record |
| 8c48 | spawnObjectTable | (gameplay: byte0 takes {0,1,7} matching spawnHangingRopeObject writing (iy+0)=0x07 to a free slot; scanObjectBankForActorCollision collision-scans B=3; attract static 0) Base of the 3-slot spawned-object table (stride 0x18) hit-tested vs shots; free slot seeded with state 0x07 |
| 8c60 | formationSpawnTable | base of the formation spawn record table scanned by scanFormationSlotsAndLaunchFree/launchFormationObjectIntoFreeSlot (records 0x18 bytes apart, descending) |
| 8c78 | hunterTableBase | (SHARED actor table — the 0x65xx path also seeds it; kept code; observed MAME: spawnHunterIntoTableAndAdvanceLaunch seeds fields 0x8c79..0x8c88 (pc 2872-2892) and stores base ptr 0x8c78 to 0x8f32/0x8f33; only slot 0 exercised in capture, so the 6-slot / 0x18-stride / downward-scan structure rema…) base of the 6-slot hunter record table (0x18 stride, scanned DOWNWARD) seeded by launch state 2 |
| 8c90 | enemyTargetRec0 | (attract+play: byte0 cycles 0..3 = presence bits (testEnemyRecordHitAndRegister tests iy+0 bit0/bit1); latchObjectTypeAndScanEnemyRecords selects 0x8c90 when I==0) Slot 0 (I=0) of the 2-entry I-parity enemy/target actor-record pair; byte0 low bits = presence/state |
| 8c94 | eagleYCoord | (SHARED actor-record coord — eagle species (read by advanceEagleToArrivalAndTallyWave) not write-confirmed; kept code; observed MAME: advanceTargetActorState writes 0x8c94 at pc=0x2218 n=356, 0x5b->0xea (launch-phase Y+=4). |
| 8c96 | eagleXCoord | (SHARED actor-record coord — eagle species (read by advanceEagleToArrivalAndTallyWave) not write-confirmed; kept code; observed MAME: advanceTargetActorState writes 0x8c96 at pc=0x2200 n=2101, 0xb0->0x50 (X-=4 per frame; JS despawns when < 4). |
| 8ca8 | enemyTargetRec1 | (attract+play: byte0 cycles 0..2 = presence bits of slot 1; latchObjectTypeAndScanEnemyRecords selects 0x8ca8 when I!=0 (0x8ca8=0x8c90+0x18)) Slot 1 (I!=0) of the 2-entry I-parity enemy/target actor-record pair (0x8c90+0x18); byte0 low bits = presence/state |
| 8d01 | formationSpawnIndex | index into the formation param tables (0x8d01) |
| 8d04 | spawnCountdownA | per-type spawn countdown, reloaded from the spawn reload table on zero (0x8d04) |
| 8d05 | spawnIntervalCountdown | per-type spawn countdown (scheduler b), reloaded from the interval table at zero (0x8d05) |
| 8d06 | spawnReloadTimer | frame-timer gated spawner countdown, reloaded from the table on expiry (0x8d06) |
| 8d07 | enemySpawnTimer | (attract+play: reloads 0x80/0x20 and drains 128->127->...->0 (3734/2647 transitions) = countdown; tickSpawnTimerAndSeedFreeEnemy dec-while-nonzero, seedFreeEnemyRecordFromRoundTables reseeds) Spawn-cadence countdown; decremented each tick, at 0 gates the 0x8ae0 spawn sweep then reseeded |
| 8d11 | formationStateRow2 | second 6-byte formation state row blanked at entry (0x8d11) |
| 8d12 | spawnTypeCursor | spawn type cursor (0x8d12) |
| 8d13 | spawnSequenceIndex8d13 | rotating spawn-sequence cursor (scheduler B) (0x8d13) |
| 8d14 | spawnSequenceIndex8d14 | rotating spawn cursor (frame-timer spawner) (0x8d14) |
| 8d19 | flashCellBase | base of the collision-flash cell pair (interrupt-register parity selects base or +1, i.e. 0x8d19/0x8d1a); set to 1 on a proximity hit |
| 8d1b | objHitFlagI0 | (attract+play: 0/1 one-frame pulses (set on hit, cleared next frame) = a FLAG; BOTH this and 0x8d1c fire in the 1P golden, so the selector is the I-parity/0x8848 slot index, NOT the player) Hit flag for the I=0 slot (pairs 0x8c90): set 1 on a collision; advanceTargetActorState clears it and tears the struck object down |
| 8d1c | objHitFlagI1 | (attract+play: 0/1 one-frame pulses = flag; selected when I!=0 in scanObjectBankForActorCollision/scanTargetSlotsAndSpawnOnProximityHit/markHitFlagSeedActorAndScanEnemyRecords; fires in the 1P golden = an I-parity slot index, not player 1) Hit flag for the I!=0 slot (pairs 0x8ca8, partner of 0x8d1b): set 1 on a collision, cleared on teardown by advanceTargetActorState |
| 8d1d | soundIdLatch8d1d | work-ram landing sound-id latch = (ix+0x17)+1 (0x8d1d) |
| 8d20 | soundRingPendingByte | byte pending append into the page-0x8a00 text ring (stashed across the append gate) |
| 8d21 | waveEventLatch | (attract: 0->1 at f1448 held to f5798 then 0 (only 3 transitions) = long-held latch; armSirenAndTickWaveEventCountdown sets it on 0x8d22 expiry, stampTwoPlaneColumnStrip/32bd clear it) One-shot latch set when the 0x8d22 periodic-event timer expires (fires queueSirenSoundRun); cleared on wave teardown |
| 8d22 | periodicEventTimer | periodic-event countdown; on expiry reloads (0x20), sets the wave-event latch and fires the siren-tile run (per the existing wave-event-latch note) |
| 8d30 | formationSpawnTimer | (static 0 in BOTH goldens (no formation-spawn cycle observed in 180s); tickFormationSpawnAndScanSlots decs while nonzero, on expiry sets IX=0x8c60/DE=0xffe8) Formation-spawn countdown (seeded from level 0x8903); returns while nonzero, at 0 runs the 0x8c60 spawn loop |
| 8d32 | grabActiveFlag | (attract: 0->1 at f4466 held ~147f to f4613 then 0 (4 transitions) = event latch; testHangingRopeGrabConnect sets 0x8d32=1 on catch, armSirenAndTickWaveEventCountdown/others gate on ==0) Rope-grab in-progress latch; set 1 when a grab fires, gates/aborts spawn & event routines while nonzero |
| 8d40 | activeEnemyCount | (play: ramps 0..5 then resets 0 per wave (gated 0x8901/cap6); attract: ramps 0..32 (anim); despawnActorAndRenderStageCountdown dec on despawn, advanceAttractAnimationAndRepaint uses &0x03 as 4-phase anim) Active enemy count: inc on spawn, dec on despawn, gated vs threshold 0x8901/cap 6; low 2 bits = anim phase |
| 8d41 | animFrameCounter | (attract: counts down 10->1 reloading 0x0a each frame (advanceAttractAnimationAndRepaint); play: increments 0..5; spawnChildActorIntoFreeSpriteSlot bumps skipping 0, resolveTargetColumnAndArmApproach/matchActorScheduleThenSpawnOrAnimate index by &7/&0x0f) Global anim frame counter; reseeded to 0x0a, bumped skipping 0 as sprite id, indexes tile cols by &7/&0x0f |
| 8d42 | spawnCounter | (MAME: 0x3a6c loads hl=0x8d42 and increments it on entry (source line 15); MAME write-set shows it bumped n=35 (== play reach) with a monotonic v 01->04, i.e. watched incrementing once per launch.…) spawn counter (0x8d42) |
| 8d43 | spawnPhaseSnapshot | work-RAM snapshot of the spawn-phase counter (written alongside ROPE_DRAW_COUNT) |
| 8d44 | activeObjectType | (attract: 4 distinct 0..3 incl 3 (f1469 0->2); play: 0..3 — cycles discrete object-type values, confirms type/mode byte) Latched type byte of the active hit record (0x8c90/0x8ca8, I-parity); type 0 skips, ==3 selects the main hit path |
| 8d46 | eagleStepCounter | eagle step counter (0x8d46) |
| 8d47 | eagleStageTimers | eagle stage timers (0x8d47) |
| 8d4a | spawnActiveFlag | spawn active flag (0x8d4a) |
| 8d4a | specialActorActiveFlag | special actor active flag (0x8d4a) |
| 8d4b | turnColumnLimit | (MAME round-advance capture: takes {0, 8, 0xff} -- 0->8 f1291, 8->0xff f1863 = threshold then interior-entry; advanceActorColumnAndArmTurnOrBand/34f2 compare vs (ix+6)&0x1f, latchColumnLimitAndArmTurnAnimation arm) Tile-column threshold at which a moving object starts its turn animation; anim-arm routines set it to 0 or 0xff |
| 8d4c | eagleTargetColumnBias | eagle target column bias (0x8d4c) |
| 8d4c | spawnColumnBias | spawn column bias (0x8d4c) |
| 8d52 | aimIndicatorMode | aim-indicator mode/direction latch: 0 triggers a redraw pass, 1 selects the above bit and 2 the below bit of PLAYER_AIM_FLAGS; set to 1/2 on a timed proximity hit and read by the indicator stepper (driveAimIndicatorHitTimerElseRescan) |
| 8d53 | aimIndicatorTimer | aim-indicator countdown reloaded to 0x18 on a timed proximity hit; decremented by the indicator stepper (driveAimIndicatorHitTimerElseRescan), and on reaching 0 it clears AIM_INDICATOR_MODE |
| 8d54 | proximityHitFlag | proximity-hit/target-acquired flag: set 1 on a target-in-band hit, cleared 0 by this scan when no record hits (gates the aim-acquisition updater acquireTargetLockAndSetAimIndicator, which bails when nonzero) |
| 8d55 | periodicModeLatch | busy/mode latch for the periodic siren driver: nonzero disables the whole routine; the >5 spawn-phase value is latched here |
| 8d56 | levelTagDoneLatch | once-per-level done latch (0x8d56) |
| 8d57 | spawnRingCounter | spawn ring counter: read+incremented per object-arm by the object cluster's state-0 handler (0x771d); cleared to 0 by the state-1 animation-tick handler on the phase-transition reseed |
| 8d58 | objectDrawnFlag | per-object "drawn" flag: set to 1 once an object is drawn (object cluster's state-2 handler 0x7790); the state-2 animation tick holds while it is set |
| 8d59 | spawnLatch | one-shot spawn latch for the 0x8c30 formation record; set 1 when spawned, gates re-spawn |
| 8d5a | spawnSweepCountdown | spawn sweep countdown paired with the sweep trigger (0x8d5a) |
| 8d5b | spawnSweepTrigger | spawn sweep trigger (also cleared during object-slot init) (0x8d5b) |
| 8d5c | spawnSpeedIndex | spawn speed index = (ROUND_COUNTER>>1)+1 clamped to 6; indexes SPAWN_SPEED_TABLE |
| 8d5d | spawnSpeedValue | spawn speed value looked up from SPAWN_SPEED_TABLE via SPAWN_SPEED_INDEX |
| 8d5e | pendingObjectCountdown | countdown gating the deferred-object promotion: 0 idles, >1 decrements, ==1 fires; reseeded to 0xff on fire |
| 8d5f | pendingObjectState | deferred-object promotion busy/state latch; must be 0 to run, armed to 0x11 (matching the play-state) on fire |
| 8d65 | activeEnemyTargetPairPtr | active enemy target pair ptr (0x8d65) |
| 8d65 | struckTargetLatch | struck target latch (0x8d65) |
| 8d68 | sirenEnableGate | warning-siren enable gate: tickIdleSirenAndTogglePhase ticks only while nonzero |
| 8d69 | sirenPhaseByte | warning-siren phase byte; bit0 selects the phase-A/B command, reset to 1/0 on toggle |
| 8d6a | sirenFrameCountdown | warning-siren frame countdown (reload 0x18); on expiry toggles the phase |
| 8d6b | actorDelayCounter | actor delay counter (0x8d6b) |
| 8d6b | spawnStepTimer | spawn step timer (0x8d6b) |
| 8d6c | spawnAttrIndex | (MAME: MAME write-set: n=32, v 01->04 (genuinely changes across 1..4), bumped in lockstep with launches; source reads (0x8d6c)&7 as the rst-0x20 index into attribute tables 0x3b37/0x3b3f (launchProjectileIntoFreeSlot…) spawn attr index (0x8d6c) |
| 8d6d | scriptAdvanceGuard | (attract+play: values {0,16,24,32} latched then cleared to 0 (few transitions) — discrete guard thresholds, confirms guard role) Threshold the phase counter (0x8901) must reach before the attract/board script advances; latched to it, nonzero=busy |
| 8d6e | slotSweepLatch | once-only latch for the gated slot-sweep checksum guard; 0 = pending, set to the free-slot count once the sweep runs |
| 8d6f | altTargetTablePtr | alt target table ptr (0x8d6f) |
| 8d71 | scriptDataPtr | 16-bit live-script pointer seeded from the script data table (0x8d71) |
| 8d73 | scriptDelayTimer | script delay countdown seeded by the script seeder, ticked/reseeded (0x8d73) |
| 8d74 | scriptValueByte | matched script-row value byte, indexes the script flag table (0x8d74) |
| 8d75 | laneSpawnCountdown | (gameplay 5->4->..->0 repeated (32 transitions) = countdown) counts down (from the 0x8d79 lane count) while a lane-spawn sequence runs; suppresses enemy fire; cleared at wave end |
| 8d79 | activeLaneCount | (attract+play: ramps up 0->5 then drains 5->0 — activate/consume counter, confirms lane count) Count of activated lane actors: inc on activate (activateLaneActorSlot), dec on slot init (spawnObjectIntoFreeSlot); ==0 selects primary target table |
| 8d7a | launchArmLatchSeed | value copied into the launch-arm latch (0x8f20) when nonzero; producer not in the decompiled set |
| 8d7b | slotSpawnIndex | (attract+play: ramps 0->5 then resets to 0 at board-script re-arm (armEnemySpawnScript) — confirms per-spawn tally) Per-slot spawn tally bumped each actor-slot init; indexes the alternate target-column/anim source (with 0x8d6f); cleared on script re-arm |
| 8d7d | waveProgressCounter | (play: monotone 0->1->2->3->4 then reset (f3261+); attract static 0 — confirms progress/arrival counter (advanceEnemyToArrivalAndTallyWave inc, fireEnemyShotWhenAlignedWithPlayer/57b4 gate)) Arrival/progress counter bumped on each object arrival; ramps enemy fire aggressiveness and gates late-wave phases |
| 8d7e | laneResetLatch | (MAME: 0x3be3 (state-0 handler) reads 0x8d7e as a guard (pc 3c54: read, ret if nonzero) then re-arms it to 0x02 at pc=3c6f after running the reset -- matches the doc's read-guard + re-arm-to-2 rol…) one-shot guard for the state-0 lane reset: nonzero blocks re-running the reset; re-armed to 2 by the reset itself and cleared elsewhere (armEnemySpawnScript) |
| 8d80 | promotedObjectList | base of the promoted-object list built on fire (3 bytes/entry: record pointer low/high + the saved (rec+6) field) |
| 8df8 | hiscoreTableCorruptFlag | (loc_0644 sets 1 on a bad header or wrong checksum) work-RAM high-score-table corruption flag |
| 8df9 | tamperStrikesTerminator | anti-tamper strike counter bumped by the terminator match-scan guard (verifyTerminatorTableOrCountTamper); nonzero diverts handlers to the board/reset path |
| 8dfd | writeAnimRecordAnchor | write-anim record-array base-minus-one anchor: only loaded as an immediate (ld ix,0x8dfd @0x7ec6) to compute the record pointer (ANIM_WORK_BLOCK_PTR 0x8e1f) = 0x8dfd + 3*(HIGH_SCORE_INSERT_RANK 0x89fc); dispatchWriteAnimStateAndPollStart dispatches the seeder only when 0x89fc != 0 (rank >= 1), so the pointer is always >= 0x8e00 and 0x8dfd itself is never read/written as a cell by role code (only the boot RAM-clear pc 0x0111 touches it) |
| 8e00 | panelTileSource | (loc_0460 paints PANEL_VRAM_DEST from here) 30-byte status-panel tile source table (10 rows x 3 cells), work RAM |
| 8e1f | animWorkBlockPtr | 16-bit anim work-block pointer: seedWriteAnimWorkBlock seeds it and appendWriteAnimBlockRowOnPhase/floodWriteAnimCellsAndLatchPhase append the growing block through it (the 2P start-of-life 12-byte clear at this base is a generic fill, not its role) |
| 8e23 | writeAnimTileIndex | write-anim animation tile index; stepped up/down between 0x10 and 0x2c and stamped into the growing block (advanceWriteAnimTileIndexOnCountdown/appendWriteAnimBlockRowOnPhase) |
| 8e24 | writeAnimStepDelay | write-anim per-step delay sub-timer (reload 0x0c); decremented each frame, gates when the tile index steps (advanceWriteAnimTileIndexOnCountdown) |
| 8e25 | writeAnimRowCount | write-anim row/pass count (seed 3); decremented per appended row, at 0 the anim hands off to its tail (appendWriteAnimBlockRowOnPhase/floodWriteAnimCellsAndLatchPhase) |
| 8e26 | writeAnimHandlerSelect | write-anim state selector (0/1/2) picking one of the three write-anim handlers (seedWriteAnimWorkBlock/advanceWriteAnimTileIndexOnCountdown/appendWriteAnimBlockRowOnPhase) each frame |
| 8e27 | writeAnimWritePtr | 16-bit write pointer for the write-anim block; seeded from DISPLAY_LIST_VRAM_TILE and advanced per pass (seedWriteAnimWorkBlock/appendWriteAnimBlockRowOnPhase) |
| 8e29 | writeanimPhaseRing | write-anim phase ring: bit 4 of the source byte rotated in each frame; low 3 bits gate the append phase (appendWriteAnimBlockRowOnPhase) |
| 8e2a | resetScanLatch | reset scan latch (0x8e2a) |
| 8e2b | writeanimCountdown | 16-bit write-anim countdown (low byte here, high byte 0x8e2c); drained per frame, at 0 hands off to the tail (advanceWriteAnimTileIndexOnCountdown) |
| 8e50 | scriptFrameTimer | (attract+play: 256 distinct, sawtooth 255->254->...->0 (f795 0->255) — classic per-frame countdown timer) Per-frame countdown for the attract/intro text-draw script; on expiry advances the script step and pulls the next byte |
| 8e51 | attractSubstate | (attract+play: 9 distinct 0..8 cycling (f99 0->1) — discrete state selector, confirms sub-state (dispatchAttractSubstate dispatch)) Attract/demo sequence sub-state selector; indexes dispatch table 0x08a1; handlers inc/set it to advance phases |
| 8e52 | scriptStepCountdown | script down-counter gating attract-substate advance + the 14-row checksum, reloaded to 0x0d (0x8e52) |
| 8e53 | scriptColCheckTick | (gwtrace pc=0b68 dec (0x8e53) x10, 0x04->0x00 countdown, read by the state-4 column-check gate) attract state-4 column-check tick countdown |
| 8e54 | scriptReadPtr | 16-bit script read cursor, paired with the script write cursor (0x8e54) |
| 8e56 | scriptWritePtr | (attract+play: low byte steps down by 0x20 per pass (72->40->8->232->200...) — confirms row-stride VRAM cursor) 16-bit VRAM write pointer for the attract/text-draw script; bytes emitted through it, backed up one row (0x20) each pass |
| 8ef0 | signatureMismatchFlag | (loc_208c sets 1 on a signature mismatch) work-RAM ROM-signature mismatch flag |
| 8efe | attractEpilogueTick | (gwtrace inc HL=0x8efe x1402, 0x01->0x7a wrapping) counter bumped each time the shared epilogue reaches its HUD-integrity check |
| 8f00 | animScriptCursor | (attract+play: cursor cycles 213->228->243->reset (238+/376 transitions) — moving script cursor, confirms role (advanceActorAnimationFrame)) 16-bit cursor into the shared per-actor animation script; advanced past 3-byte {tile,colour,delay} entries; 0xff lead = control marker |
| 8f02 | targetSpawnArmLatch | (MAME: set to 1 by spawnTargetActorOnLaunchTrigger at pc=0x211e (n=149, on trigger frames) and cleared to 0 by stepActiveTargetActorRecords at pc=0x2180 (n=5615, ~every frame). |
| 8f03 | inputRotateLatch | shift latch: sampleJoystickIntoPlayerAimState rotates the complemented joystick's bit4 into bit0 each frame; its low 3 bits decide whether the aim bit4 is cleared (also touched by acquireTargetLockAndSetAimIndicator) |
| 8f04 | formationEnableFlag | formation enable flag (0x8f04) |
| 8f04 | ropeDrawCompleteFlag | rope draw complete flag (0x8f04) |
| 8f05 | ropeDrawExtendFlag | rope draw extend flag (0x8f05) |
| 8f06 | twotileAnimHold | (MAME: MAME pc 0x256f dec 0x0f->0x04 n=7362; pc 0x2571 reload 0x0c n=606 (and loc_6b1a/6b1c dec 0x0b->0x00 + reload 0x0c, same discipline)) two-tile animation hold countdown (reload 0x0c); decremented per frame, on 0 advances the phase |
| 8f07 | twotileAnimPhase | (MAME: MAME pc 0x2574 inc 0x8f07 n=606, exact lockstep with the 606 reloads of 0x8f06) two-tile animation phase byte; incremented on hold expiry, its parity selects the source block |
| 8f08 | formationState | (MAME formation capture: cycles 0->1->2->3->0, 100 transitions from f1101 = gather->full->dispatch->reset, exactly as noted; dispatchFormationPhaseOrQueueLaunchSlots) Enemy-formation launch state; 0 while gathering launch-ready slots, set 1 when full then dispatched (&3)-1 into launch handlers |
| 8f09 | ropeDrawStepTimer | rope draw step timer (0x8f09) |
| 8f0a | ropeDrawAnimPhase | rope draw anim phase (0x8f0a) |
| 8f10 | objectVelX | (MAME: ->. Loader stores it per-phase at PC 0x2295 (MAME n=200, 00->40); mover advanceTargetActorAlongVelocityElseDespawn reads it at PC 0x2231 and integrates it into the eagle X coordinate 0x8c95/0x8c96 (EAGLE_X, MAME…) object mover X velocity word (0x8f10) |
| 8f12 | objectVelY | (MAME: ->. Loader stores it per-phase at PC 0x22a2 (MAME n=200, 00->c0); mover advanceTargetActorAlongVelocityElseDespawn reads it at PC 0x2255 and integrates it into the eagle Y coordinate 0x8c93/0x8c94 (EAGLE_Y, MAME…) object mover Y velocity word (0x8f12) |
| 8f14 | ropeExtendState | (MAME: n=4 v0=00 vN=00, set to 0 when the frame index reaches 8) rope-extend sub-state selector (0/1) dispatched by the rope state handler; this routine is its state-0 handler and advances it |
| 8f15 | targetScanCounter | (MAME: stepActiveTargetActorRecords writes it at pc=0x215d, n=17080 (~2 writes/frame), value 0x02->0x01. |
| 8f16 | ropeExtendTimer | (MAME: n=356 v0=0f vN=08, decremented per frame and reloaded, play-only) rope-extend sub-timer, reloaded to 0x10 when a segment is added (timer role inferred from the reload, not) |
| 8f18 | ropeExtendIndex | (MAME: pc 2d98 inc 01->04 (n=4); feeds the rst-0x20 column lookup at 2d9c and the 0x8f26+2*idx timer loop at 2da3) rope-extend segment index: gates the extend (below 4), indexes the video-column table and the per-segment cell timer |
| 8f19 | ropeColumnVramPtr | (MAME: pc 2da0 writes low byte 0x8f19 (97..8a) and high byte 0x8f1a=0x84 (n=4), from the 0x2db8 column table) 16-bit video-RAM column base (page 0x84) for the current rope segment, looked up from the column table |
| 8f1b | ropeExtendFrameIndex | (MAME: n=36 v0=00 vN=08, cycles 0->8 exactly) rope-extend blit frame index 0..8 (0x8f1b) |
| 8f1c | ropeCellStateBase | (MAME: n=1 v0=01 vN=01) rope cell state base (0x8f1c) |
| 8f20 | launchArmLatch | (attract+play: toggles 0<->1 (f1805 0->1) — binary latch, confirms arm-flag role (armLaunchAndAdvanceToHunterSpawn gate)) Arrow/rope launch arm latch: nonzero blocks re-arming launch flag 0x8f3f, seeded from 0x8d7a; cleared with 0x8d75 at wave end |
| 8f24 | waveTeardownState | (MAME formation capture: cycles 0->2->3->0, 75 transitions from f1157, in lockstep with the formation; advanceWaveTeardownByState) Enemy-formation teardown dispatch state: state1 tears down wave, state2 walks boss down; nonzero gates new grabs/launch as busy |
| 8f28 | ropeCellTimers | (MAME: PC 2e50 (0x2e45) writes all four stride-2 cells as decrementing timers (n=131/108/64/6); re-arm writes to 0x8f28 come from the state handlers (PC 2e68/2e8d in 0x2e5e -> 01/27, 2edb in 0x2ec…) base of four per-cell frame timers (stride 2) for the rope-cell state handlers |
| 8f30 | launchState | (attract+play: cycles 0->1->2->3->4->0 (f1448) — confirms 5-state launch state machine (dispatchLaunchState dispatch)) State selector for the arrow/rope launch state machine; per-frame driver dispatches (&7) into handlers 0..4 |
| 8f32 | hunterRecordPtr | (MAME: pc 2892 stores 0x8c78 (low 0x78 @0x8f32, high 0x8c @0x8f33, n=17) immediately after seeding the record) work-RAM word holding the pointer to the most-recently-seeded hunter record |
| 8f34 | hunterSpawnCountdown | (MAME: pc 28a6 writes 0x20 (n=17); consumed (decremented to 0) by advanceLaunchOnDelayAndClearHunterRecord pc 28b4 (1f->00, n=544)) spawn countdown seeded 0x20 by launch state 2 on the non-flip path |
| 8f36 | waveHoldTimer | (attract+play: 48->47->...->0 one step/frame (range 0..48, reseed to 0x30) = drains toward 0 = hold countdown) Inter-wave hold countdown; drains to 0 per frame to gate the next attack wave, reseeded 0x18/0x20/0x30 |
| 8f37 | tileAnimParity | (MAME gameplay golden: increments +1 per frame in play; loc_2405 advance/even, loc_23ec retreat, bit0 gates which pass runs on TILE_ANIM_CURSOR) per-frame tile-animation parity counter |
| 8f38 | waveOuterPhase | (MAME: inc (0x8f38) observed, n=8, play; 0x8f39 cleared to 0 in the same routine) eagle-wave outer-phase counter; cleared when a wave seeds (alongside WAVE_RECORDS_ARRIVED 0x8f39), incremented on the 4th-wave re-arm |
| 8f39 | waveRecordsArrived | (gameplay sub-phase progress counter vs 0x8f3d) count of records arrived in the current attack wave; compared to wave count 0x8f3d |
| 8f3a | waveLaunchFlag | eagle-wave launch flag; set 1 when a wave is seeded, driveEagleWavePerFrame gates its driver on it being nonzero |
| 8f3b | eagleGridStepTick | eagle grid-advance frame tick; low 3 bits gate the every-eighth-frame grid marker step |
| 8f3c | waveRecordCount | eagle-wave record count = 2*WAVE_INDEX; driveEagleWavePerFrame walks this many records of the 0x8ae0 table |
| 8f3d | waveIndex | (attract+play: monotonic 0->1->2->3->4->0 (range 0..4) = wave counter incrementing then wrapping) Current attack-wave index; bumped per wave (wraps after 4th), scales record counts and wave sounds |
| 8f3e | eagleFinishFlag | eagle grid-advance done latch: set 1 when the eagle reaches the grid edge (>=0xd0); diverts the approach machine to its reset epilogue |
| 8f3f | launchArmedFlag | (attract+play: toggles 0<->1 (range 0..1, 33/27 trans) = flag arming (armLaunchAndAdvanceToHunterSpawn=1) then clearing (resetActorStateForBoard/2226)) One-shot arm flag for the arrow/formation launch; set when preconditions hold, cleared at init and when object spent |
| 8f40 | targetLock | 5-byte acquired-aim-target lock: +0 closest-distance/lock-active byte, +1..+2 the locked y-slot pointer (little-endian), +3..+4 the locked enemy-block pointer (block+1, little-endian); overlaps DISPLAY_LIST_DST_PTR at 0x8f43 (multiplexed by game phase), accessed here as TARGET_LOCK+3/+4 |
| 8f43 | displayListDstPtr | (attract+play: low byte cycles many pointer values (232/265 trans) = paintDisplayListRunToVram write pointer advancing then stored back) Destination pointer for the display-list interpreter, paired with source 0x8f45; advanced during the copy |
| 8f45 | displayListSrcPtr | (attract+play: low byte sweeps 0..255 (44/69 distinct) = paintDisplayListRunToVram read pointer advancing through layout data then stored back) Source/layout read pointer for the display-list interpreter, paired with dest 0x8f43; advanced during the copy |
| 8f47 | targetGroupCount | (MAME target-group capture: 0->5 at f1090 when block-C fans out (0x880a 3->0x0f), value 5 = round-2 clamp 5..8, recycles per stage; written only when 0x8907 bit1 set; spawnEnemyWave seeds) Targets in the current group; scaled x5 into HUD 0x8634 and 3x compared to hit tally 0x8f52 for end-level bonus |
| 8f48 | introDelayCksumWord | (attract+play: low byte steps +2 across 0x26..0x30 then resets = checksum-ptr walk (advanceAttractSequenceToPlay/6df9 r/w 16-bit); 0x8f51 intro machine idle so delay-timer use unobserved) Dual-use: intro-phase delay timer (0x40/0x60/0x80, counts down) & anti-tamper column-checksum pointer |
| 8f49 | launchSeqCounter | launch seq counter (0x8f49) |
| 8f4a | launchScriptPtr | (MAME formation capture: toggles 0<->1, 50 transitions from f1157, in lockstep with the launch path; the 0x40-countdown sub-role is, not distinctly observed; launchNextScriptedObjectOnDelay/6db8 script ptr) Dual-use: 0xff-terminated object launch/dive-script pointer & 8-bit countdown firing at 0x40 in the launch path |
| 8f4b | hunterScriptPtr | 16-bit read-pointer into the lead hunter's active movement script (swoop; repointed to the dive script when the dive arms) |
| 8f4d | hudRefreshTick | hud refresh tick (0x8f4d) |
| 8f50 | playModeLatch | (static 0 across BOTH goldens (incl. attract) -> refutes A attract-flag; only writes set 1 (reseedSpawnCountersAndArmPlayMode) & 2 (announceBonusStageAndStartPlay) -> refutes B P1/P2 index; a mode/state latch) Multi-valued play-state latch (0/1/2): set by gameplay handler / post-countdown; gates alternate update paths + table select |
| 8f51 | introPhaseIndex | (static 0 in BOTH goldens (intro machine idle at capture) -- role code-confident: dispatchLevelIntroPhase rst-0x28 dispatch, handlers advance it) Level-intro phase selector (0..6); dispatched through the 0x6daa jump table, advanced by each phase handler |
| 8f52 | hitTally | (static 0 in BOTH goldens -- role code-confident: scanObjectBankForActorCollision inc per hit, drivePhase1RecordsThenCheckCompletion/6f42 consume for bonus, resetBoardRamAndReseedSpawnCounters/705f clear) Running tally of target hits; bumped per collision, compared vs group count 0x8f47 for end-level bonus, cleared on reset |
| 8f54 | introPhase5Toggle | level-intro phase-5 toggle byte incremented each 16-frame boundary; its new bit0 selects which display command is queued |
| 8f55 | tileChecksumLatch | once-only latch gating the playfield tile-region tamper checksum (verifyPlayfieldTileChecksumOnce/verifyPlayfieldTileChecksum) |
| 8f56 | tileSumOnceLatch | run-once latch for the playfield tilemap-sum integrity check (runObjectsElseVerifyTilemapChecksum sums once and sets 1); cleared/re-armed to 0 when the state-1 descending object reaches the bottom |
| 8f57 | secondaryTeardownFlag | state/flag ORed with WAVE_TEARDOWN_STATE (0x8f24) to gate/abort the player-object update; base of a 4-byte block cleared at reset by resetBoardRamAndReseedSpawnCounters (role partially understood) |
| 8f5b | latchedEnemyX | (attract+play: toggles 0<->96 (0x60) exactly matching the >=0x60 latch threshold in advanceEagleApproachAndPaintGridMarker = captures/clears the enemy X) Latched enemy screen-X; captured when the enemy X>=0x60, drives its animation-flag bits, cleared at phase reset |
| 8f5c | mainloopSubstateSelector | main-loop sub-state selector (&7), dispatched by dispatchMainLoopSubstate via the inline table at 0x0fe3; adjustCounterAndPaintBcdHudFields bumps it to advance the phase |
| 8f5d | hunterSpawnSubcounter | sub-counter bumped by launch state 2 on the flip path |
| 8f5e | substateField2Value | source value for adjustCounterAndPaintBcdHudFields's second BCD HUD field (drawn raw when <10, else re-encoded to packed BCD) |
| 8f5f | hunterSpawnCount | cumulative hunter-spawn-init counter: seedFreeEnemyRecordFromRoundTables bumps it (inc (hl), pc 0x11f2) once per freshly-initialised free enemy-record in the ENEMY_ACTOR_TABLE (0x8ae0) pool, in lock-step with the adjacent ACTIVE_ENEMY_COUNT (0x8d40) inc; unlike that per-wave spawn budget it is never reset, so it accumulates across the game; not read on the spawn path |
| 8f60 | substateField3Value | presence/source value for adjustCounterAndPaintBcdHudFields's third BCD HUD field: nonzero enables the field (drawn x2) and is folded into the field-1 counter |
| 8f61 | hunterSpawnFlipFlag | flip flag: when set, launch state 2 bumps a sub-counter instead of enqueuing the spawn display command |
| 8f62 | substateField1Counter | counter adjusted by adjustCounterAndPaintBcdHudFields and drawn x2 as its first BCD HUD field; the third-field source is added into it when present |
| 8f63 | animArmedLatch | (static 0 in BOTH goldens (band-build path not sampled) -- role code-confident: advanceActorColumnAndArmTurnOrBand/3473 gate+set=1, resetBoardRamAndReseedSpawnCounters/25a6 clear) One-shot latch: interior/rope sprite band has been built; gates re-setup, cleared on board reset and at rope terminal |
| 8ffe | bootStackTop | boot stack-pointer seed: SP=0x9000 then one unbalanced push (reserves the top word 0x8fff for ROM_SELFTEST_TALLY, keeping it above the stack so the vblank NMI's register-save cannot clobber it). |
| 8fff | romSelftestTally | ROM self-test pass tally; seeded to the bank count (8) and bumped once per matching bank, == 0x10 on a full pass; blankFillRowThenFinishAttractSetup requires 0x10 to finish setup. |
