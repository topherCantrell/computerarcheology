![Asteroids RAM Usage](Asteroids.jpg)

# Asteroids RAM Usage

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 00        |  $00               |             |
| 01        |  $01               |             |
| 02        |  $02               |             |
| 03        |  $03               |             |
| 04        |  $04               |             |
| 05        |  $05               |             |
| 06        |  $06               |             |
| 07        |  $07               |             |
| 08        |  $08               |             |
| 09        |  $09               |             |
| 0A        |  $0A               |             |
| 0B        |  $0B               |             |
| 0C        |  $0C               |             |
| 0D        |  $0D               |             |
| 0E        |  $0E               |             |
| 0F        |  $0F               |             |
| 10        |  $10               |             |
| 11        |  $11               |             |
| 12        |  $12               |             |
| 13        |  $13               |             |
| 14        |  $14               |             |
| 15        |  $15               |             |
| 16        |  $16               |             |
| 17        |  $17               |             | 
| 18        | curPlayer          | Current Player (0 = Player 1, 1 = Player 2) |
| 19        |  $19               |             |
| 1A        |  numPrevPlayers    | Number Of Players In Previous Game (0 = None, 1 = Singleplayer, 2 = Multiplayer) |
| 1B        |  $1B               |             |
| 1C        | numPlayers         | Number Of Players In Current Game |
| 1D:30     | highScores         | High Score Table (Scores) 2 Byte Format In Decimal. Byte 1 Tens, Byte 2 Thousands (In Decimal) |
| 31        | highScoreLetter    | Current Letter On High Score Entry |
| 32        | ply1HighPlacement  | Placement Of Player 1 High Score |
| 33        | ply2HighPlacement  | Placement Of Player 2 High Score |
| 34:51     | highScoresInitials | High Score Table (Initials) 3 Byte Format |
| 52        | ply1ScoreTens      | Player 1 Score Tens (In Decimal) |
| 53        | ply1ScoreThous     | Player 1 Score Thousands (In Decimal) |
| 54        | ply2ScoreTens      | Player 2 Score Tens (In Decimal) |
| 55        | ply2ScoreThous     | Player 2 Score Thousands (In Decimal) |
| 56        | numShipsPerGame    | Number Of Starting Ships Per Game |
| 57        | ply1CurShips       | Current Number Of Ships, Player 1 |
| 58        | ply2CurShips       | Current Number Of Ships, Player 2 |
| 59        | hyperSpaceFlag     | Hyperspace Flag: 1 = Successful Hyperspace Jump, $80 = Unsuccessful Hyperspace Jump (DEATH), 0 = Hyperspace Not Currently Active |
| 5A        | delayBeforePlay    | Time before game starts/time in 2 player game before it switches from current player to next after current player death. Starts at #$80 and counts down to 0 |
| 5B        | ??timeout??        | ?? Appears to be a timeout for the code. Game will lock up if this goes above 3. Checked in the NMI |
| 5C        | fastTimer          | Fast Timer |
| 5D        | slowTimer          | Slow Timer |
| 5E        |  $5E               |             |
| 5F        | rndValue           | "Random" Value |
| 60        |  $60               |             |
| 61        | direction          | Ship Direction |
| 62        | saucerShotDir      | Direction Shot Is Fired From Saucer |
| 63        | photomLimiter      | Photon Input Limiter (0 = No Input, +128 Per Photon, 255 = Max Input Limit) can't shoot a photon if value is above 127. Also used for initials input length on high score entry |
| 64        | ship_thrust_dH     | Ship Horizontal Velocity Low |
| 65        | ship_thrust_dV     | Ship Vertical Velocity Low |
| 66        | sndTimePlayerFire  | TIMER: Length Of Time To Play Player Fire Sound |
| 67        | sndTimeSaucerFire  | TIMER: Length Of Time To Play Saucer Fire Sound |
| 68        | sndTimeBonusShip   | TIMER: Length Of Time To Play Bonus Ship Sound |
| 69        | sndTimeExplosion   | TIMER: Length Of Time To Play Explosion Sound |
| 6A        | sndAltFirePlayer   | Alternate Fire Sound Flag For Player |
| 6B        | sndAltFireSaucer   | Alternate Fire Sound Flag For Saucer |
| 6C        | sndThump           | Current Volume & Frequency Settings For THUMP Sound |
| 6D        | sndThumpOn         | TIMER: Time THUMP Sound Remains On |
| 6E        | sndTHumpOff        | TIMER: Time THUMP Sound Remains Off (Speeds Up As Game Progresses) |
| 6F        | holdLampValues     | Bitmap Of Changes To Be Made In $3200 |
| 70        | numCredits         | Current Number Of Credits |
| 71        | holdDIP            | Bitmap Of DIP Switches 4-8 |
| 72        | slamFlag           | Slam Switch Flag |
| 73        | coinsToCredits     | Total Coins (After Multipliers) To Be Converted To Credits |
| 74        |  $74               |             |
| 75        |  $75               |             |
| 76        |  $76               |             |
| 77        |  $77               |             |
| 78        |  $78               |             |
| 79        |  $79               |             |
| 7A        | coin1InpLen        | Coin 1 Input Length (31 = No Input) goes down by 1 until it hits 0, if input is released before 0 then credit is added |
| 7B        | coin2InpLen        | Coin 2 Input Length |
| 7C        | coin3InpLen        | Coin 3 Input Length |
| 7D:88     |  $7D               | Ship explosion pieces x offsets (byte 1 minor, byte 2 major) |
| 89:94     |  $89               | Ship explosion pieces y offsets (byte 1 minor, byte 2 major) |
| 95:FF     |  $95               |             |
| 0100:01FF | stack              | Stack Space |

0200 - 02FF Current Player RAM

0200 - 0222 Status

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 0200:021A | statusAsteroids    | Asteroids 27-1 |
| 021B      | statusShip         | Ship, 0 = No Ship Or Currently In Hyperspace, 1 = Alive, 0x160+ = Ship Currently Exploding |
| 021C      | statusSaucer       | Saucer, 0 = No Saucer, 1 = Small Saucer, 2 = Large Saucer |
| 021D:021E | saucerShotTimer    | Saucer Shots 2-1 Countdown Timer |
| 021F:0222 | shipShotsTimer     | Ship Shots 4-1 Countdown Timer |

0223 - 0245 Horizontal Velocity 0-255, (255-192) = Left, 1-63 = Right

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 0223:023D | horzVelAsteroids   | Asteroids 27-1 |
| 023E      | horzVelShip        | Ship |
| 023F      | horzVelSaucer      | Saucer |
| 0240:0241 | horzVelSaucerShots | Saucer Shots 2-1 |
| 0242:0245 | horzVelShipShots   | Ship Shots 4-1 |

0246 - 0268 Vertical Velocity 0-255, (255-192) = Down, 1-63 = Up

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 0246:0260 | vertVelAsteroids   | Asteroids 27-1 |
| 0261      | vertVelShip        | Ship |
| 0262      | vertVelSaucer      | Saucer |
| 0263:0264 | vertVelSaucerShots | Saucer Shots 2-1 |
| 0265:0268 | vertVelShipShots   | Ship Shots 4-1 |

0269 - 028B Horizontal Position High (0-31), 0 = Left, 31 = Right

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 0269:0283 | hposhAsteroids     | Asteroids 27-1 |
| 0284      | hposhShip          | Ship |
| 0285      | hposhSaucer        | Saucer |
| 0286:0287 | hposhSaucerShots   | Saucer Shots 2-1 |
| 0288:028B | hposhShipShots     | Ship Shots 4-1 |

028C - 02AE Vertical Position High (0-23), 0 = Bottom, 23 = Top

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 028C:02A6 | vposhAsteroids     | Asteroids 27-1 |
| 02A7      | vposhShip          | Ship |
| 02A8      | vposhSaucer        | Saucer |
| 02A9:02AA | vposhSaucerShots   | Saucer Shots 2-1 |
| 02AB:02AE | vposhShipShots     | Ship Shots 4-1 |

02AF - 02D1 Horizontal Position Low (0-255), 0 = Left, 255 = Right

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 02AF:02C9 | hposlAsteroids     | Asteroids 27-1 |
| 02CA      | hposlShip          | Ship |
| 02CB      | hposlSaucer        | Saucer |
| 02CC:02CD | hposlSaucerShots   | Saucer Shots 2-1 |
| 02CE:02D1 | hposlShipShots     | Ship Shots 4-1 |

02D2 - 02F4 Vertical Position Low (0-255), 0 = Bottom, 255 = Top

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 02D2:02EC | vposlAsteroids     | Asteroids 27-1 |
| 02ED      | vposlShip          | Ship |
| 02EE      | vposlSaucer        | Saucer |
| 02EF:02F0 | vposlSaucerShots   | Saucer Shots 2-1 |
| 02F1:02F4 | vposlShipShots     | Ship Shots 4-1 |
| 02F5      | asteroidsPerWave   | Starting Asteroids Per Wave |
| 02F6      | curAsteroidCount   | Current Amount Of Asteroids |
| 02F7      | saucerTimer        | Countdown Timer For Saucer, At 0, Saucer Appears. Also Used For Time Between Saucer Shots While Saucer Is Alive |
| 02F8      | saucerTimeReload   | Starting Value For Timer At 02F7 |
| 02F9      | asteroid_hit_timer | Goes Up After Explosion |
| 02FA      | shipSpawnTimer     | Timer For Ship Spawning |
| 02FB      | astdWaveTimer      | Timer For Asteroid Wave |
| 02FC      | astWaveTimerReload | Starting Value For Timer At 6E |
| 02FD      | max_rocks_for_ufo  | Goes Up By One Every Wave |
| 02FE      |  $02FE             |             |
| 02FF      |  $02FF             |             |

Holding area for "other player"

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 0300:03FF | otherPlayerRAM     | Other Player RAM |

