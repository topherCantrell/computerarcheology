![The Pit](thepit.jpg)

# The Pit — Work RAM

Work RAM lives at `0x8000`–`0x87FF`. Each name below describes the cell by its role in
the running game; the hex address is the stable identity. Cells that share a byte, or
whose role is only partly pinned, carry a terse caveat.

>>> memory

| Address | Name | Description |
| --- | --- | --- |
| 8000 | creditCount | Credit counter; banked from the coin lines (clamp 9), spent on start; the corruption-watchdog anchor |
| 8001 | gameState | 0 attract / 1 one-player / 2 two-player / 3 credit-standby / 4 attract-demo |
| 8002 | activePlayer | Active player index (1 or 2); read on the P1/P2 handoff |
| 8003 | coinSwAccum | Coin switch (IN1 bit0) edge-detect accumulator; a completed pulse banks a credit |
| 8004 | start1SwAccum | 1P-start switch (IN1 bit2) edge accumulator; a pulse pays a credit + starts a 1P game |
| 8005 | start2SwAccum | 2P-start switch (IN1 bit1) edge accumulator; starts a 2P game |
| 8007 | frameCounterPrescaler | /60 down-divider; on rollover reloads 60 and ticks playPhaseCounter |
| 8009 | frameWaitCountdown | Per-frame countdown decremented by the vblank NMI; armed + busy-waited to 0 by the frame-wait |
| 800a | loopCounter | General loop down-counter (setup-repeat, screen-hold); also the board-complete bonus count 5/10/15 |
| 800d | prngLow | 16-bit LFSR PRNG state, low byte — also the returned random draw |
| 800e | prngHigh | PRNG state high byte |
| 8010 | playPhaseCounter | Board-startup ramp + master gate: enemies 1&2 run at >=8, enemy-3 + mountain erosion at >=0x0a |
| 8011 | mainLoopDelay | Per-frame busy-wait length = loopDelayBase - level; wraps to a ~17x crawl at level 10 |
| 8015 | in1Debounced | Debounced IN1 (coin/start): stable value latched after two equal reads of 0xa800 |
| 8016 | in1Prev | Previous IN1 sample, rolled each frame for the debounce compare |
| 8018 | in0Debounced | Debounced IN0 (joystick + dig/fire); movement/action code reads this, not the raw port |
| 8019 | in0Prev | Previous IN0 sample, rolled for the debounce |
| 801a | playerAnimPhase | Player packed animation/command phase (wind-up countdown high bits, move command low bits) |
| 801b | demoSteerDir | Attract-demo synthetic steering (one-hot 01/02/04/08); read in place of the stick at gameState >=3 |
| 801c | creditMirrorA | Redundant copy of creditCount, cross-checked by the corruption watchdog |
| 801e | soundHead | Sound-command ring WRITE/head index (mod 8) |
| 801f | soundTail | Sound-command ring READ/dequeue index (mod 8) |
| 8020 | soundRing | Sound-command ring buffer base (8 slots); enqueue writes (code ors 0x80) at head |
| 8028 | level | Current player's level/round counter (inits 1, +1 per clear); every difficulty subsystem scales off it |
| 802b | menLeft | Active player's working lives; game-over gate is this reaching 0 (P1/P2 backups 802c/802d kept hex) |
| 8031 | scoreLo | Low packed-BCD byte of the active score (all score is displayed x100) |
| 8034 | scoreHi | High packed-BCD byte of the active score, paired with 8031 |
| 8037 | scoreDisplayLow | Low byte of a 16-bit score value staged per high-score record for digit unpacking |
| 8038 | scoreDisplayHigh | High byte of that staged 16-bit score value |
| 8039 | highScoreTable | Base/top rank of the descending 3-entry high-score table (5-byte records: 3 initials + 16-bit value) |
| 8048 | variant | Board/entry variant selector read at round setup and by the fill dispatch (role weakly pinned) |
| 804b | initialsRemaining | High-score initials-entry down-counter (seeded 3, ->0 ends entry) |
| 804c | coinsPerCreditA | DSW coin cost for coin line 2 (0 = free play) |
| 804d | coinsPerCreditB | DSW coin cost for coin line 3 |
| 804e | loopDelayBase | DSW main-loop pacing base that mainLoopDelay derives from |
| 804f | stepTimerBase | DSW-decoded base that seeds the mountain-erosion step timer (804f - 4*level) |
| 8051 | spriteCoordBias | flipBit<<1 (= 0x02 when flipped): a +2 sprite-Y nudge, NOT the screen flip itself |
| 8053 | startingMen | DSW starting lives ((dsw&0x40)?4:3); seeds menLeft |
| 8055 | plotRunLength | Run length (cells) for the shared down-column tile/colour plotter |
| 8057 | boardMode | Board/entry-select mode byte the multi-door entry family stows before the shared body |
| 8058 | tileCol | Tile-cell COLUMN byte fed to the (row,col)->tilemap-offset calc |
| 8059 | tileRow | Tile-cell ROW byte fed to the tilemap-offset calc |
| 805a | tilemapOffset | 16-bit tilemap offset 32*row+col; consumed to derive the colour/video write cursors |
| 805c | glitterCountdown | Free-running 8->1 countdown pacing the jewel-glitter cell recolour |
| 805e | colourRamCursor | 16-bit colour-RAM write cursor (tilemap offset + 0x8800), walked down-column by the fillers |
| 8065 | mountainErodePtr | 16-bit VRAM cursor for mountain erosion (seed 0x9104, +0x20/step writing tile 0x31) |
| 8067 | mountainErodeTimer | Per-step erosion countdown, armed level-scaled (804f - 4*level, faster every level) |
| 8068 | playerY | Player Y (game-space work-Y); renders screen-HORIZONTAL under ROT270; drives the tilemap row |
| 8069 | playerFacing | Player facing + sprite-frame code (bit7 = horizontal mirror); selects the laser direction |
| 806a | playerSpriteAttr | Player sprite attribute byte (palette bits0-2 + priority bit3) |
| 806b | playerX | Player X (game-space work-X); renders screen-VERTICAL under ROT270; drives the tilemap column |
| 806c | playerStepY | Player per-frame Y step, added to / subtracted from playerY |
| 806d | playerStepX | Player per-frame X step, added to / subtracted from playerX |
| 806e | playerCellPtr | 16-bit pointer to the player's current video-RAM display cell |
| 8071 | playerTileCol | Tilemap COLUMN cell under the player (from playerX>>3); low part of the 806e cell pointer |
| 8073 | playerTileRow | Tilemap ROW cell under the player (from playerY); *0x20 major part of the 806e cell pointer |
| 8076 | prizeGate | Latch set by under-tile 0x26 — the prerequisite that unlocks the diamond pickup (NOT the 0x27 goal path) |
| 8077 | pitCrossActive | Sticky Pit-crossing flag set at goal tile 0x27; gates boarding the ship + disables the laser; awards no points |
| 8078 | treasureCollected | Set nonzero on a diamond pickup; the top-rung completion gate reads it (byte also reused by dig/twin-actor — coupling unproven) |
| 8079 | playerActive | Presence flag for the player object (0 none / 0xff present) |
| 807b | boardEndPhase | End-of-board state when the mountain is gone: 0 idle / 1 escape (-> rescue ship -> level advance) / >=2 done |
| 807c | transitionTimer | Master board-transition countdown; on expiry vectors to lose-a-life OR advance-a-level |
| 807d | postTransitionMode | Death-vs-advance selector read at transitionTimer expiry: 0 lose a life / 1 advance a level |
| 807e | carveSeamLeft | Flag set when a dug channel abuts the object's tile column on one side (left/right assignment rotation-ambiguous) |
| 807f | carveSeamRight | Mirror seam flag for the opposite move arm |
| 8080 | moveBlockFlag | Movement blocker: a falling rock/arrow overlapping the player sets it and freezes climbing (hazards block, don't kill) |
| 8081 | crystalCount | Crystals collected (tile 0x3a); award +1000 displayed; board-complete bonus threshold ==4 (4 per board) |
| 8082 | diamondCount | Diamonds collected (tiles 0x3b/3c/3d); award +2000 displayed; bonus threshold ==3 (3 per board) |
| 8084 | enemyWorkSprite | Sprite/orientation byte of whichever enemy is ldir'd into the shared work slot; enemy-catch sets 0x17 |
| 8089 | probeCellPtr | 16-bit tilemap cell pointer (base 0x9000) the enemy tile-probe helpers deref +-0x20/row |
| 808b | enemyActionTimer | Mover-record cadence/dwell countdown every mover routine drives (record offset 8) |
| 808d | subtilePhase | Sub-tile phase / probe-table row index derived from the enemy's pixel position |
| 8090 | enemyWorkState | Signed state byte of the enemy in the work slot; also the laser-kill death marker (parked 0xc0 -> respawn) |
| 8091 | enemyWorkMovePeriod | Working-block mover cadence reload period |
| 8092 | enemyWorkDir | Published travel-direction index (0/1/2/3) stamped by the four direction presets |
| 8093 | enemyWorkTargetCol | Working-block mover target column it steers toward |
| 8094 | reactionObjX | playerY-paired position of the reaction/laser sprite entity (sprite record byte0); box-tested vs enemies |
| 8095 | reactionObjCode | Sprite/frame-code byte (byte1) of the reaction object's record |
| 8096 | reactionObjAttr | Attribute/anim byte (byte2) of the reaction record |
| 8097 | reactionObjY | playerX-paired position of the reaction/laser entity (sprite record byte3) |
| 809a | laserScanPtr | 16-bit tilemap cell the horizontal laser/terrain-scan walker samples (steps -0x20/frame) |
| 809e | scrollSubphase | Sub-tile column phase selecting the ROM stop-tile slice for the laser/scroll |
| 80a1 | laserState | Laser-bolt state: 0 ready / +8 flying right / 0xf8 flying left / 1 spent (one bolt in flight) |
| 80a2 | reactionState | Per-object reaction/animation selector: 0 idle, 1-4 a collision/dig/push reaction armed; also a busy-lock |
| 80a4 | reactionTimer | Reaction step/animation countdown (reload from period 80a3); value 0x18 cues a sound |
| 80a5 | curTile | Saved current tile under the object |
| 80a7 | expectedTile | The object cell's table-resolved expected tile; cross-checked vs curTile to detect a change |
| 80a8 | nextTile | Next-tile slot, pre-cleared before classify |
| 80a9 | hazardX | X of the falling-hazard / dig-carve target cell (shared record; bbox-compared vs the player) |
| 80aa | hazardState | State/phase AND sprite SHAPE of the falling-hazard/dig object: 0x10 falling (down-arrow) / 0x30 resting / 0x09 done |
| 80ab | hazardType | Falling-hazard COLOUR (not glyph): 0x06 rock / 0x07 arrow — same shape, different palette; resting seed = 0x07 |
| 80ac | hazardY | Y of the same hazard record; advances +1/frame while falling |
| 80b1 | digObjTimer | Dig-carve object countdown/animation timer; shared — also the falling-hazard lifetime |
| 80b6 | stagedTargetX | Staged X coord (reactionObjX-4) promoted into hazardX at commit |
| 80b9 | stagedTargetY | Staged Y coord (playerX grid-snapped) promoted into hazardY at commit |
| 80ba | stagedCellPtr | 16-bit copy of playerCellPtr saved at spawn, reloaded into the live carve cursor at commit |
| 80bc | stagedDigTimer | Staged dig timer (reactionPeriod<<1) promoted into digObjTimer at commit |
| 80bd | hazardActiveCount | Number of falling hazards currently live (0 = none); bounds the drop machinery |
| 80bf | stagedDigSpriteId | Staged classified dig-entity id, stamped into the tilemap cell before the carve cursor at commit |
| 80c0 | digObjSubtype | Sub-type of the committed dig entity (0 plain / 2 special: arm timer + patch neighbour tiles to 0xc1) |
| 80c1 | digCollisionState | Arm/capture state of the carve object (0 idle / 1 armed / 2 latched); gates dispatch |
| 80c3 | dropQueue | Base of the 24-slot pending-spawn column queue (12 left paired to 12 right) |
| 80db | chamberCreatureX | Left-chamber creature X (byte0); horizontal bounce in [0x19,0x38) (velocity 80df) |
| 80dc | chamberCreatureFrame | Creature sprite frame toggled 0x38<->0x39 every 8 frames |
| 80dd | chamberCreatureAttr | Creature sprite byte2 attribute (color low bits + priority) |
| 80de | chamberCreatureFallY | Creature's own accelerating fall-Y (step 80e0), clamped 0x86 then RNG-reseeded (drops and resets; no separate shell) |
| 80e3 | chamberCreatureAnimPhase | Creature frame-clock down-counter mod 8; reloads 8 on wrap, toggles the frame |
| 80e4 | pitFloorRevealPeriod | Level-derived reload period (7..3) for the Pit sliding-floor reveal gate |
| 80e5 | pitFloorRevealGate | Per-column frame-gate down-counter; on wrap reveals one Pit floor column |
| 80e6 | pitFloorRevealCursor | Byte offset into tile-pattern table 0x3048, stepped back 6 per reveal (==0 = reveal finished) |
| 80e7 | goalTileLatch | Latch set when the player reaches goal tile 0x27; reroutes state dispatch + enables the floor reveal |
| 80e8 | enemy1X | Base (offset 0, X) of enemy-1's 17-byte record |
| 80e9 | enemy1Sprite | Enemy-1 record byte1: sprite code + flipX/flipY orientation |
| 80ea | enemy1Attr | Enemy-1 record offset 2: attr/color (priority bit3 held clear while color-cycling) |
| 80f0 | enemy1Timer | Enemy-1 mover cadence/dwell countdown (record offset 8) |
| 80f5 | enemy1State | Enemy-1 mover signed state byte the mover sign-dispatches on (offset 13) |
| 80f6 | enemy1MovePeriod | Enemy-1 mover cadence reload period = 7 - (level&6) (periodic mod 8, not monotonic) |
| 80f8 | enemy1TargetCol | Enemy-1 mover target column (record offset 16) |
| 80f9 | enemy2X | Base (offset 0, X) of enemy-2's 17-byte record |
| 80fa | enemy2Sprite | Enemy-2 record offset 1 sprite tile/code byte |
| 80fb | enemy2Attr | Enemy-2 record offset 2 attr/color byte |
| 8101 | enemy2Timer | Enemy-2 mover cadence/dwell countdown (mirror of enemy1Timer) |
| 8106 | enemy2State | Enemy-2 mover signed state byte (mirror of enemy1State) |
| 8107 | enemy2MovePeriod | Enemy-2 mover cadence reload period (mirror of enemy1MovePeriod) |
| 8109 | enemy2TargetCol | Enemy-2 mover target column (seed 5) |
| 810a | enemy3X | Enemy-3 primary-half X (offset 0); a 2-sprite actor, also intro set-piece + escape rescue-ship (NOT a plain ship) |
| 810b | enemy3Tile | Enemy-3 primary-half sprite/tile field |
| 810c | enemy3Attr | Enemy-3 primary record byte+2 (color bits0-2 + priority bit3) |
| 810d | enemy3Y | Enemy-3 primary-half Y |
| 810e | enemy3StepX | Low byte of the actor's 16-bit step vector, added to enemy3X each cadence tick |
| 810f | enemy3StepY | High byte of the actor step vector, added to enemy3Y each cadence tick |
| 8112 | enemy3Timer | Enemy-3 cadence timer (record offset 8) |
| 811b | enemy3TwinX | Enemy-3 twin-half X, locked +16 to enemy3X |
| 811c | enemy3TwinTile | Enemy-3 twin-half sprite/tile field |
| 811d | enemy3TwinAttr | Enemy-3 twin record byte+2 (color + priority) |
| 811e | enemy3TwinY | Enemy-3 twin-half Y (record offset +3) |
| 8123 | enemy3TwinTimer | Enemy-3 twin cadence countdown (twin of enemy3Timer) |
| 812c | creditMirrorB | Third redundant copy of creditCount, watchdog-read |
| 8134 | savedCellPtr | 16-bit scratch holding a tilemap cell pointer (save/restore within the enemy neighbour-search) |
| 8220 | spriteStagingBase | Base of the 32-byte (8x4) sprite-record staging buffer the NMI copies to sprite RAM 0x9840 |
| 8238 | enemy3SpriteSlot | Sprite-staging slot 6 (base+24), the actor body's record |
| 823c | enemy3TwinSpriteSlot | Sprite-staging slot 7 (base+28), the twin's record |
| 8280 | scoreReadoutStrip | Base of a 32-cell work-RAM strip staging the on-screen score-readout column |
