![Centipede](centiped.jpg)

# RAM Usage

Work RAM lives at `0x0000`–`0x03FF`. Each name below describes the cell by its role in
the running game; the hex address is the stable identity. Cells that share a byte, or
whose role is only partly pinned, carry a terse caveat.

>>> memory

| Address | Name | Description |
| --- | --- | --- |
| 0032 | tilemapPtrLo | 16-bit working tile/screen pointer (lo 0x32 / hi 0x33) through which advanceHeadOrientatio |
| 0033 | tilemapPtrHi | Tile-map cell pointer, high byte. |
| 0050 | headVelocitySeed | Head velocity SEED: steerHeadAndSeedVelocity writes a random small magnitude (2 when |
| 0081 | objectYSteer | Steered object's vertical (Y) steer delta: loc_71 is stepped by +/- loc_81 (sign from |
| 0084 | moveSubstepAccumA | Sub-step (fractional) accumulator for the $63-axis coordinate integrator: $2ACE ac |
| 0085 | moveSubstepAccumB | Sub-step (fractional) accumulator for the $73-axis coordinate integrator: $2AEB ac |
| 0098 | shadowTileLowNibble | Transient low-nibble of the tile/attribute source (loc_34+x) captured during the per- |
| 0099 | shadowSignLatch | Sign-bit latch of loc_44+x held during shadow build, XORed into the shadow sub-value |
| 00a0 | spawnTimer | spawnActorOnTimer's own periodic countdown timer: decremented each enabled frame and, on r |
| 00b3 | sfxTimerCh2 | SFX countdown timer feeding POKEY ch2 (AUDF2/AUDC2) |
| 00b4 | sfxTimerCh3 | SFX countdown timer feeding POKEY ch3 (AUDF3/AUDC3, fixed AUDC3=0x64) |
| 00b5 | sfxTimerCh4 | Companion timer cell re-armed to 0x14 by tickColumnCountdown; consumed (counted down) by a |
| 00b6 | sfxTimerCh2Priority | Pitched pre-empt timer for POKEY ch2 (takes AUDF2 before the collision decision) |
| 00b7 | sfxTimerCh1Priority | ch1 priority SFX timer: armed to 0x13 by armSlotState, decremented by the ch1 voice updater |
| 00ba | trackballLastDelta | Per-axis last-committed signed trackball delta (hysteresis reference, array 0xba/0xbc |
| 00be | objectXDriftStash | Saved copy of the horizontal drift OBJECT_X_DRIFT (loc_51) while it is paused: advanc |
| 00c9 | segmentMoveAccumB | Second parallel segment-movement accumulator, advanced by delta+1 alongside 0xca on each c |
| 00ca | segmentMoveAccum | Shared segment-movement accumulator. |
| 00cb | segmentRowCrossCount | Row-crossing counter: bumped once when the accumulator clears the threshold, and a second |
| 00cc | segmentColLifeTimer | Per-column life countdown (array 0xcc,0xcd,0xce). |
| 00cf | segmentColBody | Per-column centipede body/step cell (array 0xcf,0xd0,0xd1 for cols 0..2). |
| 00d2 | segmentReloadTimer | Shared reload timer: reloaded to 0xf0 unless IN1 bit4 is set; while nonzero it decrements |
| 00d4 | segmentMoveFrameCounter | Free-running movement frame counter: stepPhasedCountersAndWrapCells increments it eve |
| 00da | fieldScanPtrLo | Low byte of the 16-bit playfield cell-stream scan pointer walked forward by scanForRa |
| 00db | fieldScanPtrHi | High byte of the 16-bit playfield cell-stream scan pointer (paired with loc_da); incr |
| 00fd | configDipByte | Mode/control byte whose bits 5-4 select a ROM table variant in readFdBitsTableByte. |
| 0178 | highScoreTable | High-score table RAM mirror base — first byte of the 64-byte EAROM-backed high-score block |
| 018a | highScoreConfigByte | Config-byte snapshot stored inside the hi-score table (table+0x12); validate compares/reco |
| 01b5 | highScoreChecksum | High-score table integrity checksum byte (last used byte of the hs block; foldHighScoreChe |
| 01b8 | trackballAxis0StepState | Per-axis (axis 0) trackball step-state carried between IRQ frames and fed to stepAxis |
| 01b9 | trackballAxis1StepState | Per-axis (axis 1) trackball step-state, companion to $01B8 |
