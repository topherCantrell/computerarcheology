![Main Board RAM Use](Frogger.jpg)

# RAM Usage

Work RAM lives at `0x8000`–`0x87FF`. Each name below describes the cell by its role in
the running game; the hex address is the stable identity. Cells that share a byte, or
whose role is only partly pinned, carry a terse caveat.

>>> memory

| Address | Name | Description |
| --- | --- | --- |
| 8001 | scrollCopySrcPtr | scroll-copy source-pointer scratch (word); blitScrollTileGrid saves the source pointer here and the per-column loop reloads it |
| 8003 | scrollCopyRowcount | scroll-copy row-count scratch; blitScrollTileGrid saves the row count here and the per-column loop reloads it |
| 8004 | holdFlag | hold flag / object-frog hit flag; stampHomeBaySlot stamps the slot but leaves the selector pending when non-zero, flagSpriteObjectFrogHit sets it to 1 (with gate loc_842c) when a sprite object overlaps the frog |
| 8007 | objectReady0 | object-ready flag; loc_1952 sets it to 1 after the frog render (with 0x8009/0x800b) |
| 8008 | spriteShadowSrcBase | work-RAM source of the per-frame sprite-shadow DMA (0x8008-0x803f, nibble-swapped, -> OBJRAM 0xb008) |
| 8009 | objectReady1 | object-ready flag; loc_1952 sets it to 1 after the frog render |
| 800b | objectReady2 | object-ready flag; loc_1952 sets it to 1 after the frog render |
| 800c | liveObjectPage | demo object block base; clearObjectBlocksAndMirrorToObjRam clears 44 bytes here + mirrors 43 to OBJRAM, swapOutActivePlayerPages banks/restores its 43-byte object page |
| 800d | objectAnimState800d | object-animation state block base; seedObjectAnimationState seeds 10 stride-2 cells (0x800d-0x801f) from a fixed table at board init |
| 800f | demoScrollRegister | demo scroll register; loc_0de0 writes 3 here (paired with OBJECT_ANIM_STATE_800D) each dwell tick |
| 8014 | freeRunningPosCounter | free-running position counter (rises +1/frame, wraps 0xff->0x00, independent of the frog); sprite-object motion arms drift each object toward it -- NOT the frog X (frog X is 0x8044/0x8047) |
| 8015 | objectAnimState8015 | object-animation state cell in the 0x800d-0x801f block; dispatchGameModeFrame zeroes it on the mode-5 reset, seedObjectAnimationState seeds it at board init |
| 8019 | objectAnimState8019 | object/animation-state cell in the 0x800d-0x801f block; renderMode3ScoreRankingScreen seeds it =3 at the mode-3 ranking-screen draw (a work cell, not a screen-id) |
| 801b | introCounter801b | intro counter; loc_2d88 seeds it to 5 during the mode-2 setup -- ALSO a mode-4 sprite-record CODE cell renderMode4PointTablePhase seeds =3 (-> OBJRAM); shared work RAM, per-mode use |
| 801d | pointTableSpriteAttr801d | mode-4 point-table sprite-record ATTR/Y field; renderMode4PointTablePhase phase 4 seeds it 6 (-> OBJRAM 0xB01d) |
| 801f | objectAnimState801f | top of the 0x800d-0x801f object/animation work block; base of renderMode3ScoreRankingScreen's 5-cell 4-strided clear (0x801f/8023/8027/802b/802f) that wipes leftover attract-demo objects off the ranking page |
| 8021 | objectAnimState8021 | object-animation cell block base; seedObjectAnimationState seeds 14 stride-2 cells (0x8021-0x803b) from a fixed table at board init -- renderMode4PointTablePhase writes a mode-4 sprite CODE (=3) into this same object table |
| 8023 | screenModeState | screen/mode state byte; blitPlayerSelectPrompt sets it to 3 on the two-player prompt arm -- ALSO a mode-4 sprite-record ATTR/Y field renderMode4PointTablePhase seeds =6 (-> OBJRAM); shared, per-mode use |
| 8027 | pointTableSpriteCode8027 | mode-4 point-table sprite-record CODE field; renderMode4PointTablePhase phase 4 seeds it 3 (-> OBJRAM 0xB027) |
| 8029 | pointTableSpriteAttr8029 | mode-4 point-table sprite-record ATTR/Y field; renderMode4PointTablePhase phase 4 seeds it 6 (-> OBJRAM 0xB029) |
| 802b | introCounter802b | intro counter; loc_2d88 seeds it to 3 (also the store target of loc_0c4a) -- ALSO re-stamped =4 by placeScoreRankMarkers on the mode-3 ranking screen (rank-marker tile) |
| 802d | pointTableSpriteCode802d | mode-4 point-table sprite-record CODE field; renderMode4PointTablePhase phase 4 seeds it 3 (-> OBJRAM 0xB02d) |
| 802f | laneLowBoundSelector | lane low-bound selector; loc_12e4 branches on it (<128 vs >=128) to pick the offset (12 vs 3) added to FROG_X — also a mode-4 sprite ATTR/Y field renderMode4PointTablePhase seeds =6; shared, per-mode use |
| 8039 | mode3StripState | mode-3 final-strip state cell; zeroed by blitMode3FinalStrip before the strip blit |
| 803f | objramCol3fAttrShadow | work-RAM shadow of OBJRAM col-0x3f attribute byte 0xB03F (DMA'd 0x8007-803f -> 0xb007-b03f each frame); display routines write it (never read as a flag) to set col 0x3f's attribute (not a page-swap-done flag) |
| 8040 | flySpriteX | fly sprite X / base of the 4-cell block armHomeGoalSprite arms; driveFlyPatrol writes FLY_DRIFT_COUNTER + path-table offset, armHomeGoalSprite arms the lead byte + fixed tail 25,3,16 |
| 8041 | flySpriteCode | fly sprite code; driveFlyPatrol sets it at the timer midpoint (33 or flipped 0xA1) and to the turn sprite (30) at an endpoint |
| 8043 | flySpriteY | fly/goal sprite Y (byte3 of the 0x8040-0x8043 block, FLY_SPRITE_X base); cocktail +2 source for OBJRAM 0xb043 |
| 8044 | frogX | frog X (game-space horizontal; watched 0x84->0x90 as the demo frog moved right) and frog object block base; activateFrogObject/resetFrogObject write the object bytes, the move dispatcher scans lanes against it |
| 8045 | frogSpriteCode | frog sprite/tile code; activateFrogObject clears it on activate, the river-ride handlers stamp the ride/move/home tile codes into it |
| 8046 | frogObjAttr | frog object attribute byte (between the sprite code and Y); set to 7 as the death phase advances |
| 8047 | frogY | frog Y / row (game-space vertical position); frog object sub-field -- activateFrogObject clears it when activating the frog, the move dispatcher keys its lane-scan arm on it |
| 8048 | spriteObjectSlotA | sprite-object slot A base (the IY slot the sprite-object dispatchers write; blitSpriteShadow mirrors 6x4 bytes to 0xb048) |
| 8050 | spriteObjectSlotASecond | IY slot for dispatcher-A's 2nd pass (level count >= 6) |
| 8058 | spriteObjectSlotB | shared 4-byte sprite-object block; loc_2bab clears it (with the 16-byte IX struct) when an object reaches its target and despawns |
| 805c | goalAwardRecord | home-bay goal-award 4-byte record (0x805C-5F); sub_2673 writes it on a home arrival and starts the goal-celebration countdown (0xA0), clearFourByteCounterBlock zeros it on drain (NOT a generic counter, not on the river-ride path) |
| 80ff | laneObjectIndex | lane-object walk index (0..10); moveLaneObjectsAndCarryFrog increments it per object, wrapping to 0 after object 10 — also the base of the 183-byte per-player object page swapIn/swapOutActivePlayerPages bank |
| 8100 | spriteBlock2Base | second work-RAM sprite block base; clearObjectBlocksAndMirrorToObjRam zeroes 99 bytes from here |
| 8101 | figureAnimPhase | animateTwoPairFigure idle-clears the figure-animation phase when this is 0, else runs the animation |
| 8107 | scrollEdgeFlag | scroll edge flag; stampScrollRevealColumn clears it on the 128/176 arm and sets it to 1 on the 160 arm |
| 8108 | scrollWrapLatch | scroll wrap-latch; blitScrollBand raises it to 1 on the mode-80 phase and clears it on the mode-48/96 phases |
| 8109 | laneObjlist8109 | loc_12e4 scans it as a lane object list (count byte then object X positions, band width 31); loc_1058 arms both plot cursors (IX/IY) to it for the frog-anim render loop |
| 8110 | scrollStampPhase | scroll-phase selector; stampScrollRevealColumn dispatches on it (80/208, 128/176, 160) to pick the stamp table |
| 8111 | scrollBandPhase | scroll-phase mode; blitScrollBand dispatches the source-row choice on it (0/112->A, 48/96->B, 80->C), loc_2005 steps it by 2 |
| 8112 | laneObjlist8112 | lane object list (count byte then object X positions), band width 92; loc_12e4 scans it for an object in the frog's move band |
| 8118 | frogAnimBlitTrigger | frog-anim blit trigger; blitFrogAnimColumnOnTrigger blits the tile pair when non-zero then clears it to 0, else returns at once |
| 8119 | scrollBandRowspan | scroll row-span shadow; blitScrollBand stores row count - 1 here at exit |
| 811a | scrollStampRowcount | scroll-object row-count mirror; stampScrollRevealColumn writes (row-count field - 1) here before returning |
| 811b | laneObjlist811b | lane object list (count byte then object X positions), band width 44; loc_12e4 scans it for an object in the frog's move band |
| 811c | flyDriftCounter | drifting counter in the 0x811b block; the block-mover advances it +1 ~every 6 frames (wraps 0xff->0, ~25.6s); its wrap-to-0 is the FLY-APPEARANCE trigger (animateFlyEatCollision arms the tongue at 0), and driveFlyPatrol adds it as the fly X base (NOT a fly-path X base) |
| 8120 | homeBaySlotCursorMirror | home-bay slot cursor mirror; stampHomeBayGatorEmerging writes the slot value here, stampHomeBayGatorFull reads it as its 1..5 home-slot index, stampHomeBaySlot clears it with PENDING_HOME_BAY_SLOT |
| 8121 | pendingHomeBaySlot | pending home-bay slot selector (1..5); stampHomeBayFly/stampHomeBayGatorFull write it, stampHomeBaySlot dispatches on it to pick a bay and clears it after stamping |
| 8122 | scrollTimerCounter | per-frame counter driving the fly/gator/slot arms (orchestrateCollisionsAndFrogInput) |
| 8123 | homeBaySlotCursor | home-bay slot cursor (mod 6); loc_23eb increments-and-wraps it, stampHomeBayFly/stampHomeBayGatorEmerging read it as the 1..5 home-slot index and mirror it (not a river/scroll phase) |
| 8124 | laneObjlist8124 | lane object list (count byte then object X positions), band width 47; loc_12e4 scans it for an object in the frog's move band |
| 8134 | collisionSubflag | collision sub-flag; loc_27b3 zeroes it before falling through to the clear helper (loc_27bc) |
| 8135 | collisionLatch | collision-latched flag; loc_27b3 returns early when 0, else clears it via the clear helper (also read by loc_26a6) |
| 8136 | laneObjlist8136 | loc_12e4 scans it as a lane object list (band width 34); loc_10f8 uses it as the frog-anim arm-6 plot-cursor base |
| 813d | flyEatPhase | fly tongue-out/eat phase; bit0 set = retract this frame (animateFlyEatCollision) |
| 813f | laneObjlist813f | lane object list (count byte then object X positions), band width 18; loc_12e4 scans it for an object in the frog's move band |
| 8140 | laneRunScrollPos | lane sprite-run scroll-position byte (byte 0 of the 9-byte lane-run header 0x813f); the lane mover ramps+wraps it each frame, enqueueLaneScrollSyncedCommand reads it as a scroll-phase==0 gate (NOT a frog-on-log blit-busy gate) |
| 8145 | twoplayerFrameCell8145 | one of five cells clearTwoPlayerFrameCells zeroes in play-mode 2 |
| 8146 | twoplayerFrameCell8146 | one of five cells clearTwoPlayerFrameCells zeroes in play-mode 2 |
| 8147 | twoplayerFrameCell8147 | one of five cells clearTwoPlayerFrameCells zeroes in play-mode 2 |
| 8148 | laneObjlist8148 | lane object list (count byte then object X positions), band width 18; loc_12e4 scans it for an object in the frog's move band |
| 814e | twoplayerFrameCell814e | one of five cells clearTwoPlayerFrameCells zeroes in play-mode 2 |
| 814f | spriteFrameBusyLatch1 | sprite-frame busy latch 1; advanceAnimationFrameBuffer returns without stepping while non-zero, animateTwoPairFigure reads it as a busy gate that must be 0, clearTwoPlayerFrameCells zeroes it in play-mode 2 |
| 8150 | figureAnimStepGate | animateTwoPairFigure gates its step on bit0 of this cell |
| 8151 | laneObjlist8151 | lane object list (count byte then object X positions), band width 18; loc_12e4 scans it for an object in the frog's move band |
| 815a | laneObjlist815a | lane object list (count byte then object X positions), band width 18; loc_12e4 scans it for an object in the frog's move band |
| 815b | spriteFrameBusyLatch2 | sprite-frame busy latch 2; advanceAnimationFrameBuffer returns without stepping while it is non-zero |
| 819b | animFrameBuffer | animation frame buffer; advanceAnimationFrameBuffer copies 11 bytes of the current frame source into it |
| 81a2 | laneControlSpeed7 | lane-control byte 7 of the 11-byte per-board block 0x819b-81a5 (loaded by the ldir at 0x183e): low nibble = lane speed, bit4 = sub-rate; enqueueLaneScrollSyncedCommand reads it as a gate input (fixed 0x13, never animates) |
| 81a6 | laneObjectPhaseTable | 11-byte per-object phase-countdown table (0x81a6+i); moveLaneObjectsAndCarryFrog holds object i while its countdown drains, stepping one pixel and clearing it at 1, reloading from the lane control-nibble-1 |
| 81b1 | scrollCopyColumnStride | scroll-copy column stride; blitScrollTileGrid advances the destination by this between columns |
| 81b2 | deathPhase | death-phase index, bumped as the death counter reloads (driveFrogDeathAnimation) |
| 81b3 | animFrameIndex | animation frame index; advanceAnimationFrameBuffer advances it into the ANIM_FRAME_SRC_PTR_TABLE pointer table, wrapping to 0 at index 10 |
| 81b4 | animFrameTimer | animation frame timer; advanceAnimationFrameBuffer ticks it down each pass and reloads it to 21 when it reaches 0 |
| 8247 | hopFrameCounter | per-frame hop/death counter; driveFrogDeathAnimation advances the phase when it reaches 0x10 |
| 8248 | frogHopDownActive | down-hop active flag; scanFrogInputAndDispatchHop tails to advanceFrogHopDown when set, else clears the down-hop mirror FROG_HOP_DOWN_ARRIVAL. |
| 8249 | frogHopUpActive | up-hop active flag; scanFrogInputAndDispatchHop tails to advanceFrogHopUp when set, else clears FROG_HOP_UP_ARRIVAL. |
| 824a | frogHopRightActive | right-hop active flag; scanFrogInputAndDispatchHop tails to advanceFrogHopRight when set, else clears FROG_HOP_RIGHT_ARRIVAL. |
| 824b | frogHopLeftActive | left-hop active flag; scanFrogInputAndDispatchHop tails to advanceFrogHopLeft when set, else clears FROG_HOP_LEFT_ARRIVAL. |
| 824c | frogHopDownArrival | down-hop arrival mirror flag; scanFrogInputAndDispatchHop clears it when FROG_HOP_DOWN_ACTIVE is clear, advanceFrogHopDown sets it on drain. |
| 824d | frogHopUpArrival | up-hop arrival mirror flag; scanFrogInputAndDispatchHop clears it when FROG_HOP_UP_ACTIVE is clear, advanceFrogHopUp sets it on drain. |
| 824e | frogHopRightArrival | right-hop arrival mirror flag; scanFrogInputAndDispatchHop clears it when FROG_HOP_RIGHT_ACTIVE is clear, advanceFrogHopRight sets it on drain. |
| 824f | frogHopLeftArrival | left-hop arrival mirror flag; scanFrogInputAndDispatchHop clears it when FROG_HOP_LEFT_ACTIVE is clear. |
| 8250 | frogHopDownAnimCounter | down-hop animation counter; beginFrogHopDown primes it from FROG_HOP_DOWN_ANIM_RELOAD, advanceFrogHopDown decrements it each frame and marks arrival (FROG_HOP_DOWN_ARRIVAL) at 0 |
| 8251 | frogHopUpAnimCounter | up-hop animation counter; beginFrogHopUp primes it from FROG_HOP_UP_ANIM_RELOAD, advanceFrogHopUp decrements it each frame and marks arrival (FROG_HOP_UP_ARRIVAL) at 0 |
| 8252 | frogHopRightAnimCounter | right-hop animation counter; beginFrogHopRight primes it from FROG_HOP_RIGHT_ANIM_RELOAD, advanceFrogHopRight decrements it each frame and marks arrival (FROG_HOP_RIGHT_ARRIVAL) at 0 |
| 8253 | frogHopLeftAnimCounter | left-hop animation counter; beginFrogHopLeft primes it from FROG_HOP_LEFT_ANIM_RELOAD, advanceFrogHopLeft decrements it each frame and marks arrival (FROG_HOP_LEFT_ARRIVAL) at 0 |
| 8254 | frogHopVerticalDelta | vertical hop step delta; added to FROG_Y by advanceFrogHopDown and subtracted by advanceFrogHopUp each frame while a hop steps. |
| 8255 | frogHopHorizontalDelta | horizontal hop step delta; added to FROG_X by advanceFrogHopRight and subtracted by advanceFrogHopLeft each frame while a hop steps. |
| 8256 | frogHopDownAnimReload | down-hop animation-length reload; beginFrogHopDown copies it into FROG_HOP_DOWN_ANIM_COUNTER to prime the hop. |
| 8257 | frogHopUpAnimReload | up-hop animation-length reload; beginFrogHopUp copies it into FROG_HOP_UP_ANIM_COUNTER to prime the hop. |
| 8258 | frogHopRightAnimReload | right-hop animation-length reload; beginFrogHopRight copies it into FROG_HOP_RIGHT_ANIM_COUNTER to prime the hop. |
| 8259 | frogHopLeftAnimReload | left-hop animation-length reload; beginFrogHopLeft copies it into FROG_HOP_LEFT_ANIM_COUNTER to prime the hop. |
| 825a | playerStartDemoFlag | per-player start/demo flag; loc_05d3 sets it to 1, handOffToOtherPlayer sets it to 1 on the player hand-off |
| 825b | twoPlayerStartFlag | 2-player start flag; loc_05d3 clears it, raiseTwoPlayerStartFlag raises it, swapOutActivePlayerPages restores it under the init guard |
| 825c | player1Slot | player-1 slot byte; loc_0534 zeros it before the cold-start pre-clear (loc_048f's P1-init later sets it to 1) |
| 825d | player2Slot | player-2 home count (sibling of PLAYER1_SLOT); awardHomeBayGoal / stampHomeGoalAndResetFrog use it for the inactive-slot home tally |
| 825e | homeBay1OccupancyPrimary | home-bay-1 occupancy gate, primary bank (used when (0x83FD)==1); the home-bay stampers skip that bay when non-zero |
| 825f | homeBay2OccupancyPrimary | home-bay-2 occupancy gate, primary bank ((0x83FD)==1); skipped when non-zero |
| 8260 | homeBay3OccupancyPrimary | home-bay-3 occupancy gate, primary bank ((0x83FD)==1); skipped when non-zero |
| 8261 | homeBay4OccupancyPrimary | home-bay-4 occupancy gate, primary bank ((0x83FD)==1); skipped when non-zero |
| 8262 | homeBay5OccupancyPrimary | home-bay-5 occupancy gate, primary bank ((0x83FD)==1); skipped when non-zero |
| 8263 | homeBay1OccupancyAlt | home-bay-1 occupancy gate, alternate bank (used when (0x83FD)!=1); skipped when non-zero |
| 8264 | homeBay2OccupancyAlt | home-bay-2 occupancy gate, alternate bank ((0x83FD)!=1); skipped when non-zero |
| 8265 | homeBay3OccupancyAlt | home-bay-3 occupancy gate, alternate bank ((0x83FD)!=1); skipped when non-zero |
| 8266 | homeBay4OccupancyAlt | home-bay-4 occupancy gate, alternate bank ((0x83FD)!=1); skipped when non-zero |
| 8267 | homeBay5OccupancyAlt | home-bay-5 occupancy gate, alternate bank ((0x83FD)!=1); skipped when non-zero |
| 8268 | frogHopInputTimer | hop-input lock timer; scanFrogInputAndDispatchHop decrements it and ticks the home-bay slot cursor each frame while it counts, locking joystick input until it drains to 0 |
| 8269 | frogFurthestRow | frog row-progress high-water mark; scoreFrogRowProgress seeds/updates it as the furthest (nearest-top) row the frog has reached, resetFrogObject clears it on frog reset |
| 826a | gatedCountdownCounter | gated countdown counter; tickGatedCountdown decrements it and, when it reaches 0, clears the enable flag GATED_COUNTDOWN_ENABLE_FLAG |
| 826c | gatedCountdownEnableFlag | countdown enable flag; tickGatedCountdown returns early while it is 0 and clears it to 0 once GATED_COUNTDOWN_COUNTER reaches 0 |
| 826d | boardAdvanceRequest | board-advance / board-complete-pending flag; loc_05d3 sets it =1 when all five frogs reach home, setUpBoardOrContinueLife fires advanceBoardForeground then clears it; raiseTwoPlayerStartFlag also reads it during the 2P start raise (NOT a 2-player-mode flag) |
| 826e | scrollPhaseCounter | scroll phase counter; loc_2005 steps it each NMI and runs a lane block at 16/32/48, clearing it to 0 at phase 48 |
| 8270 | activeLaneParamBlock | active player's lane-parameter block (33 bytes); loadActivePlayerLaneParams copies the selected difficulty block into here |
| 8273 | scrollObjectBlockBase | scroll-object block base; stampScrollRevealColumn reads its row/column/row-count fields (+0/+1/+2) to build the VRAM stamp address |
| 8274 | scrollObjARowCount | scroll object A descriptor +1 (row count); loc_2005 loads it as the grid copy engine's B row-count at phase 16/32/48 |
| 8276 | spriteSpawnXStride | sprite-spawn placement pair (spawnSpriteObjectArmA): rotated right twice + 0x24 gives the per-band X stride walked to place a new object |
| 8278 | spriteSpawnBandScanCount | sprite-spawn placement pair (spawnSpriteObjectArmA): band-scan count for the placement djnz walk |
| 827c | scrollBandDescriptorBase | scroll-band descriptor base; blitScrollBand reads column (+0), unit count (+1), row count (+2) to place the video band |
| 827d | scrollObjBRowCount | scroll object B descriptor +1 (row count); loc_2005 loads it as the band copy entry's B row-count |
| 8282 | frogAnimArm6SpriteCode | frog-anim arm-6 sprite triple code byte; loc_10f8 reads it into A and stashes it at SCROLL_COPY_COLUMN_STRIDE for the render loop |
| 8283 | frogAnimArm6RowCount | frog-anim arm-6 row count; loc_10f8 loads it as the render loop's B (rows per pass) |
| 8284 | frogAnimArm6PassCount | frog-anim arm-6 outer-pass count; loc_10f8 loads it as the render loop's C (passes, 0=>256) |
| 8293 | player1DifficultyIndex | player 1 difficulty index; loadActivePlayerLaneParams reads it to index the lane-parameter pointer table |
| 8294 | player2DifficultyIndex | player 2 difficulty index; loadActivePlayerLaneParams reads it when the active player (0x83FD) is not 1 |
| 8295 | initGuardLatch | one-shot init guard latch; swapOutActivePlayerPages returns early when set, else latches it to 1 |
| 8297 | homeRevealCountdown | board-complete "all frogs home" reveal countdown / home-column selector; loc_05d3 sets 255, decremented each frame, fed to stampHomeBayFrogByColumn as the selector |
| 8298 | homeRevealDelayTimer | board-complete reveal delay timer; loc_05d3 sets it to 0x40, it drains before the 0x8297 reveal countdown starts |
| 8299 | attractHopDwell | attract-demo hop dwell cell; driveAttractDemoFrogHop loads/decrements/reloads it, driveFrogDeathAnimation clears it on board advance |
| 829a | inPlayBoardStateByte | board-state byte cleared at in-play board init (initInPlayBoardOnce) |
| 829b | introCounter829b | intro counter; loc_2d88 zeroes it during the mode-2 setup |
| 829c | secondBank | mid-river / second-bank kill cell; raised (=1) by the frog-kill tail in the river band 0x30<=FROG_Y<0x80, read by driveFrogDeathAnimation |
| 829d | inplayCountdownWord | NMI in-play countdown word; loc_0292 decrements it each pass |
| 8300 | soundQueueCount | pending sound-command count; loc_07ac returns when it is 0, else decrements it, issues the command at SOUND_QUEUE_COUNT+1, and shifts SOUND_QUEUE_COUNT+2.. |
| 833d | flyTravelDirStep | fly travel direction/step byte; bit7 = direction (also the sprite flip bit), low 7 bits = path-table step index, walked by driveFlyPatrol |
| 833e | flyAttackTimer | fly tongue/attack timer; driveFlyPatrol counts it down each frame and reloads it to 60 at a path endpoint or hold |
| 833f | twoPairFigureAnimPhase | figure-animation phase animateTwoPairFigure increments; blits at 64 and 112, clears it at 112 and whenever idle |
| 8340 | homeGoalSpriteArmCell | arm cell armHomeGoalSprite sets to 160 alongside the four-cell block |
| 8370 | numPlayers | number-of-players; renderScoreHeader draws the 2-UP column only when it is not 1 (==1 -> single player) |
| 8371 | perTurnScratch | per-turn scratch cell; handOffToOtherPlayer clears it at the top of the player hand-off |
| 837e | coinPulseTimer0 | coin-counter-0 pulse timer; scanCoinInputAndCredit seeds it to 4 when pulsing counter 0 |
| 837f | coinPulseTimer1 | coin-counter-1 pulse timer; scanCoinInputAndCredit seeds it to 4 when pulsing counter 1 |
| 8380 | boardAdvanceDoneFlag | set to 1 by board-advance foreground once the new board is laid out (advanceBoardForeground) |
| 8381 | fanfareIndex | arrival-fanfare index (boot seeds 0x15, reload 0x14); stampHomeGoalAndResetFrog steps it |
| 8382 | soundSequenceCountdown | 16-bit vblank countdown for the active sound sequence; the NMI handler decrements it and fires the end-of-sequence sound pair when it hits 0; writers (fanfare/death/intro) seed a frame duration, 0 = silent |
| 8384 | statusRowBlitCountdown | board-complete status-row redraw countdown: seeded 0xff, drained each frame, at 0 blits the status row |
| 839a | scoreDisplayCursorLo | score-display cursor low byte; zeroed with 0x839b when the score field is cleared and seeded (clearAndSeedScoreField) |
| 839b | scoreDisplayCursorHi | score-display cursor high byte; zeroed with 0x839a at score-field seed |
| 839c | hudStampBase | board-start HUD base; three cells stamped at board start (setUpBoardOrContinueLife) |
| 83a0 | perLifeHudBase | per-life HUD base (beginNextLifeOrIntro) |
| 83ae | countdownExpiryFlag | countdown-expiry flag; loc_0292 clears it when the countdown word reaches zero |
| 83b3 | startLatch | start-already-latched flag; the new-game setup sets it =1, and while non-zero the attract pace tail loops without re-reading the START buttons |
| 83b4 | creditColumnClearLatch | renderCreditLine one-time credit-column-clear latch; set to 1 on the first call after clearing the credit column, then checked to skip the clear thereafter |
| 83b5 | gatedCountdownEnableMirror | mirror/complement of GATED_COUNTDOWN_ENABLE_FLAG; also the one-shot latch for the no-more-frogs reveal |
| 83b6 | perPlayerResetCell | per-player reset cell; handOffToOtherPlayer clears it when handing play to the other player |
| 83b7 | livesCount | life/level count; renderLivesRow clamps it to draw the lives row, awardExtraLife mirrors the new count here, handOffToOtherPlayer loads the other player's into it |
| 83b8 | player1Lives | player 1 life count; awardExtraLife increments it, handOffToOtherPlayer reads it |
| 83b9 | player2Lives | player 2 life count; awardExtraLife increments it, handOffToOtherPlayer reads it |
| 83ba | inPlayBoardInitGuard | once-per-board in-play-init guard; set to 1 after the board is initialised, checked on entry to skip re-init (initInPlayBoardOnce) |
| 83bb | attractPhaseCompanion | attract companion byte cleared to 0 alongside ATTRACT_SEQUENCER_PHASE at cold-start (0x05b3) and the attract drain (stampAttractDemoCell); write-only-to-0, holds no live state — its only read is the cold-boot LDIR zero-fill (NOT attract-sequencer state) |
| 83bc | attractDemoDwell | attract demo dwell counter; loc_0de0 decrements it and reloads 32 on expiry |
| 83bd | attractFrameTimer | attract-cell frame timer byte; next byte (0x83be) is the frame index |
| 83be | attractFrameIndex | attract-cell frame index (tickAttractCellFrameClock) |
| 83bf | attractSequencerPhase | attract sequencer phase byte; loc_0de0 clears it to 0 after placing the last cell |
| 83c2 | cocktailEnabledFlag | cocktail-enabled flag; handOffToOtherPlayer toggles the screen flip only when it is non-zero |
| 83c3 | frogReadyFlag | frog-ready flag; resetFrogObject sets it to 1 at the end of the frog-object reset |
| 83c5 | introTimer | intro/game-over countdown timer; runIntroTimerThenInitGame counts it down before init |
| 83c7 | spinDelayWord | 16-bit spin-delay count (boot seeds 0x0100; the main-loop spin reads it) |
| 83c9 | continueFlag | player-1-path continue flag; set by runIntroTimerThenInitGame, checked by setUpPlayerTwoContinue |
| 83ca | continueFlag2p | player-2-path continue flag; set by setUpPlayerTwoContinue, checked by runIntroTimerThenInitGame |
| 83cb | screenFlipLatch | screen-flip latch (work-RAM shadow); handOffToOtherPlayer toggles bit 0 and mirrors it to the flip IO ports |
| 83cd | frogStateDemoFlag | frog-state / demo flag; loc_05d3 sets it to 1, resetFrogObject clears it during the frog-object reset |
| 83ce | lifeRestartFlag | life-restart gate: read by beginNextLifeOrIntro (0 resumes play), set by driveFrogDeathAnimation's reset arm, cleared each frame by renderFrogSceneAndTickTimer |
| 83d2 | frogTimerA | frog 16-bit timer A; activateFrogObject seeds it to 64 in a two-player game |
| 83d4 | coinageWord | coinage-select word in {0,2,4,6}; scanCoinInputAndCredit indexes the per-slot credit amount by it |
| 83d6 | gameMode | top-level game mode; loc_0341 masks it against 2 to gate the attract dispatcher 0x0d11, loc_0567 sets it =3 at cold-start (finer 1-4 labels still inferred) |
| 83d7 | attractDemoPhaseCounter | attract-demo phase counter (1..7); loc_0de0 dispatches the cell arm on it, decrements it, reloads 7 when drained — also the mode-4 sub-phase counter (reload 5, counts 4..0) for renderMode4PointTablePhase |
| 83d8 | pointTableDrawState | mode-2 intro state cell; loc_2d88 stores 0xff here at the intro setup -- ALSO the shared attract frame-pacing/drawn-state gate loc_0d11 checks; renderMode4PointTablePhase parks it 0xC0 idle / 0x80 drawn |
| 83d9 | soundCtrlShadow | sound-control byte RAM shadow; issueSoundCommand reads it to pulse bit 3 of the sound-control port |
| 83da | frogTimerB | frog 16-bit timer B; activateFrogObject seeds it to 64 in a two-player game |
| 83dd | scoreDisplayCounterHi | score-display counter high byte; when zero the driver takes the end-strip tail, else decremented, and its bits index the bar tile |
| 83df | scoreDisplayArmSelect | score-display arm select; nonzero routes the driver into its bonus-strip arm (driveScoreDisplayCountdown) |
| 83e1 | creditBcd | on-screen credit total, packed BCD; the pace tail compares it against the player count and subtracts (daa) when a game starts |
| 83e2 | coinInputLatch | coin/service input latch; scanCoinInputAndCredit stores ~IN0 & 0xC4 here on the attract pass and credits on the release edge |
| 83e3 | coinPairToggle | every-other-coin toggle; scanCoinInputAndCredit bumps it and credits only on the even count for the 2-coins/credit coinage |
| 83e4 | sharedTimeByte | shared time byte / inactive sentinel; renderTimeBar returns without drawing when it holds 255, else uses it as the fallback time source |
| 83e5 | timeRemainingP1 | player-1 time-remaining byte; renderTimeBar uses it as the bar length when player 1 is active |
| 83e6 | timeRemainingP2 | player-2 time-remaining byte; renderTimeBar uses it as the bar length when player 2 is active |
| 83e7 | player1ExtraLifeAwarded | player-1 extra-life-awarded flag (0x83e7 P1 / 0x83e8 P2 pair); loc_08e0 sets it when the extra life is awarded, initNewGameScoreAndTimers clears the pair at new-game start |
| 83e8 | player2ExtraLifeAwarded | player-2 extra-life-awarded flag (0x83e7 P1 / 0x83e8 P2 pair); addScoreAndAwardExtraLife sets it when the score first reaches the target, initNewGameScoreAndTimers clears the pair |
| 83ea | boardLayoutGate | board-layout gate; cleared =0 to request a fresh layout (new-life, board-complete, boot), set =1 by setUpBoardOrContinueLife once laid; read each frame at 0x040b to route fresh-setup vs in-play (NOT a demo start flag) |
| 83eb | player2Score | player-2 score word (16-bit); loc_0f69 reads it as one of the two players' scores to rank and pack |
| 83ed | player1Score | player-1 score word (16-bit); loc_0f69 reads it as one of the two players' scores to rank and pack, renderScoreHeader draws it in the 1-UP column (swapped from the earlier high-score reading -- 0x83ef is the high score) |
| 83ef | highScore | high-score word (16-bit), entry[0] of the ranking table read at 0x83ef+2r; renderScoreHeader draws it in the HI-SCORE column, initNewGameScoreAndTimers does NOT touch it |
| 83f1 | highScoreTableBase | high-score word table base (5 rank words 0x83f1-0x83fa, read at 0x83ef+2r); renderMode3ScoreRankingScreen reads it for the on-screen ranking scores; maintained by insertHighScoreEntry |
| 83f2 | highScoreTableTopHi | key-high of the first slot of the 5-entry descending table; insertHighScoreEntry inserts into it |
| 83fb | introDigitField | two-byte score display / intro digit field (0x83fb low, 0x83fc high); loc_0c3d reads the pair to draw the two intro digits, loc_0f69 stores the larger word's rank code at 0x83fb and the smaller's at 0x83fc |
| 83fd | activePlayer | active player number (1/2); awardExtraLife and renderTimeBar pick the active player's counter, handOffToOtherPlayer toggles it |
| 83fe | playFlag | in-play flag AND player count (0 = attract, 1/2 = a game with that many players); the pace tail branches to the in-play tree 0x040b when non-zero, new-game setup stores the count here |
| 8400 | spawnRngRingBase | ring cursor cell + buffer base; nextSpawnRandomByte decrements the cursor and XOR-folds two ring cells |
| 8420 | homeBayGateBlock | 12-byte home-bay gate block base (0x8420-0x842b); force-cleared at cold-start / player work-RAM reset (forceClearPlayerWorkRam) |
| 842f | homeColumnState | home-column state cell; loc_0670 clears it to 0 before tailing into the extra-life award |
| 8440 | spriteObjectRecordAP1 | dispatcher-A sprite-object record base (16-byte IX struct), player 1 |
| 8460 | spriteObjectRecordAP2 | dispatcher-A sprite-object record base, player 2 |
| 8480 | spriteObjectRecordBP1 | dispatcher-B sprite-object record base (16-byte IX struct), player 1 |
| 8490 | spriteObjectRecordBP2 | dispatcher-B sprite-object record base, player 2 |
| 8500 | workPageSaveBank | work-page save bank base; swapOutActivePlayerPages banks 183 live bytes into here |
| 85c0 | otherPlayerObjectPage | other player's saved object page; swapOutActivePlayerPages restores 43 object bytes from here |
| 8600 | otherPlayerWorkPage | other player's saved work page; swapOutActivePlayerPages restores 183 bytes from here |
| 86c0 | objectPageSaveBank | object save bank base; swapOutActivePlayerPages banks 43 live object bytes into here |
| 87ff | workRamTop | inclusive top of the 2KB work RAM (0x8000-0x87ff); boot-clear upper bound |