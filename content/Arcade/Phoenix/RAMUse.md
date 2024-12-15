![RAM](Phoenix.jpg)

# RAM Use

There are two banks of memory that map to 4000 - 4FFF (4K each). The lower bit of $5000 controls which bank is active.
Write a 0 for the 1st bank and a 1 for the 2nd bank. The Phoenix game only uses 3K from each bank (4000 - 4BFF). I'm
guessing this allows the cabinet to leave out a 1K RAM chip for each bank to save money.

These banks include the video memory with a twist -- literally. When bank 1 is selected, the screen is rotated to face 
player 2 in cocktail mode. When bank 0 is selected, the screen faces player 1 (and both players in a non-cocktail cabinet). 

The idea for these banks is that the first bank holds all the player 1 info and the second holds all the player 2
info. This could make switching players easy. But there is no "common" memory for global info and the stack. The code 
must carefully manage the bank switching -- especially in regards to the stack pointer.

  - 4000 - 433F Foreground
  - 4340 - 47FF General storage (see the table below)
  - 4800 - 4B3F Background 
  - 4B40 - 4BFF Stack space

# Screen memory

The screen is rotated physically clockwise, but the screen memory layout is standard upper-left corner to lower right corner. There are two screens: foreground and background. Each screen is 26 columns by 32 rows (after rotation).

The first (upper left) byte of screen memory maps to the upper right corner of the rotated screen. Adding one to a
screen memory pointer moves 1 row down the screen. Subtracting one moves the pointer 1 row up on the screen. Adding
32 to a screen memory pointer moves 1 column left. Subtracting 32 moves the pointer 1 column right. I spell these
out because I get confused easily!

Each graphics tile is 8x8 pixels. This gives a rotated screen dimension of 26*8 x 32*8 = 208x256 pixels. 

# Variables

The values below are kept in bank 0. ?? TODO see how/if the 2nd bank is used? Maybe it is just a copy in cocktail?

## Foreground screen 

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 4000:433F | ForegroundScreen     | 32*26 bytes for the foreground screen |


## General storage

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 4350      | M4350                | ? |
| 4351      | M4351                | ? |
| 4352      | M4352                | ? |
| 4353      | M4353                | ? |
| 4354      | M4354                | LSB of pointer to ? |
| 4355      | M4355                | ? |
| 4356      | M4356                | ? |
| 4357      | M4357                | ? |
| 4358      | M4358                | ? |
| 4359      | M4359                | ? |
| 435A      | M435A                | ? |
| 435B      | M435B                | ? |
| 435E      | M435E                | ? |
| 435F      | M435F                | 8 bit counter for alien movement |
| 4360      | PlayerMoved          | Flag for: 'player moved' ($FF) |
| 4361      | BulletTriggered      | Flag for: 'bullet triggered' ($30) and counter ? |
| 4362      | M4362                | Player shield animation counter ? |
| 4363      | PlayerWasHit         | Flag for: 'player ship was hit by alien' ($10) and counter ? |
| 4364      | M4364                | ? |
| 4366      | M4366                | ? |
| 4368      | M4368                | ? |
| 4369      | M4369                | ? |
| 436A      | M436A                | ? |
| 436B      | M436B                | ? |
| 436D      | M436D                | ? |
| 436E      | M436E                | ? |
| 436F      | M436F                | ? |
| 4370      | M4370                | ? |
| 4371      | M4371                | ? |
| 4372      | M4372                | ? |
| 4373      | M4373                | ? |
| 4374      | M4374                | ? |
| 4378      | M4378                | Animation counter for the bonus explosion |
| 4379      | M4379                | First two digits of BCD score value for the bonus explosion (last digit is ever 0) |
| 437A      | M437A                | ? |
| 437B      | M437B                | ? |
| 437C      | M437C                | ? |
| 4380      | M4380                | Ever set to 0 (prevents overflow) |
| 4381      | Score1high           | Player 1 score BCD (high) |
| 4382      | Score1mid            | Player 1 score BCD (mid) |
| 4383      | Score1low            | Player 1 score BCD (low) |
| 4384      | M4384                | Ever set to 0 (prevents overflow) |
| 4385      | Score2high           | Player 2 score BCD (high) |
| 4386      | Score2mid            | Player 2 score BCD (mid) |
| 4387      | Score2low            | Player 2 score BCD (low) |
| 4388      | M4388                | Ever set to 0 (prevents overflow) |
| 4389      | HiScorehigh          | Hi score BCD (high) |
| 438A      | HiScoremid           | Hi score BCD (mid) |
| 438B      | HiScorelow           | Hi score BCD (low) |
| 438C      | SoundControlA        | RAM copy of sound device control register A (0x6000) |
| 438D      | SoundControlB        | RAM copy of sound device control register B (0x6800) |
| 438E      | M438E                | ? |
| 438F      | CoinCount            | Number of coins inserted (max is 9) |
| 4390      | Player1Lives         | Player 1 number of lives |
| 4391      | Player2Lives         | Player 2 number of lives |
| 4392      | M4392                | ? |
| 4393      | M4393                | ? |
| 4394      | M4394                | ? |
| 4395      | M4395                | ? |
| 4396      | M4396                | ? |
| 4397      | M4397                | ? |
| 4398:4399 | M4398                | 16 bit counter (MSB:LSB) actual index for slow print at intro splash |
| 439A:439B | Counter16            | 16 bit counter (MSB:LSB) and.. |
| 439B      | M439B                | Next index for slow print at intro splash |
| 439C      | M439C                | ? |
| 439D      | M439D                | Fist two digits of BCD score value for mothership explosion |
| 439E      | M439E                | Mapped player ship position, left part: ($09 to $C0) |
| 439F      | M439F                | Mapped player ship position, right part: ($17 to $C8) |
| 43A0      | IN0Current           | Current value of IN0: bit0='coin', bit1='1 player', bit2='2 players', bit4='fire', bit5='right', bit6='left', bit7='shield' |
| 43A1      | IN0Previous          | Previous value of IN0    |
| 43A2      | GameOrAttract        | Attract mode=0, One player game mode=1, Two players game mode=2 |
| 43A3      | GameAndDemoOrSplash  | Game and demo for player 1=0, Game for player 2=1, Intro splash=2 |
| 43A4      | GameState            | Game state=0 - 7 |
| 43A5      | Counter8             | 8 bit counter (score flash time) |
| 43A6      | ShieldCount          | Counts shield time and controls shield picture. Shields end at C0. |
| 43A7      | AnimationCounter     | For mothership's antenna and the alien pilot animation |
| 43A8      | M43A8                | Temporary storage (MSB of pointer to table $1860) |
| 43A9      | M43A9                | Temporary storage (LSB of pointer to table $1860) |
| 43AA      | M43AA                | ? |
| 43AB      | M43AB                | Counter value for (2x2) planets |
| 43AC      | M43AC                | ? |
| 43AD      | M43AD                | ? |
| 43AE      | M43AE                | ? |
| 43AF      | M43AF                | ? |
| 43B0      | M43B0                | ? |
| 43B1      | M43B1                | ? |
| 43B2      | M43B2                | MSB of pointer to table T1C00 or T1D00 or T1F00 |
| 43B3      | M43B3                | LSB of pointer to table T1C00 or T1D00 or T1F00 |
| 43B4      | B4Counter            | 8 bit counter (stars scrolling down, aliens fade in time) |
| 43B5      | M43B5                | ? |
| 43B6      | M43B6                | ? |
| 43B8      | LevelAndRound        | Bit0 - 3: game level, bit4 - 7: game round |
| 43B9      | B9Counter            | 8 bit backwards counter |
| 43BA      | AliensLeft           | Number of aliens left in wave (16 at new) |
| 43BB      | BirdsLeft            | Number of birds left in wave (8 at new) |
| 43BC      | M43BC                | ? |
| 43BD      | M43BD                | ? |
| 43BE      | BonusLivesAt         | Bonus lives (at 30K, 40K, 50K or 60K) from DIP switch settings |
| 43BF      | M43BF                | ? |


## Player and player bullets, data structure (grid)

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 43C0      | PlayerState            | Player ship control state register |
| 43C1      | PlayerShape            | LSB for T1400 player ship character block shapes table |
| 43C2      | PlayerShipX            | Player ship, coordinate X ($0C=min.left, $64=default, $C0=max.right) |
| 43C3      | PlayerShipY            | Player ship, coordinate Y ($D8) |
| 43C4      | PlayerBulletState      | Player bullet, control state register |
| 43C5      | PlayerBulletShape      | Player bullet, character code ($50 to $57) |
| 43C6      | PlayerBulletX          | Player bullet, coordinate X |
| 43C7      | PlayerBulletY          | Player bullet, coordinate Y ($D0=min.bottom, $18=max.top) |
| 43C8      | AbovePlayerBulletState | One position above player bullet, control state register |
| 43C9      | AbovePlayerBulletShape | One position above player bullet, character code ($50 to $57) |
| 43CA      | AbovePlayerBulletX     | One position above player bullet, coordinate X |
| 43CB      | AbovePlayerBulletY     | One position above player bullet, coordinate Y |


## Alien bullets, data structure (grid)

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 43CC      | AlienBullet0State      | Alien bullet 0, control state register |
| 43CD      | AlienBullet0Shape      | Alien bullet 0, character code ($58 to $5F) |
| 43CE      | AlienBullet0X          | Alien bullet 0, coordinate X |
| 43CF      | AlienBullet0Y          | Alien bullet 0, coordinate Y |
| 43D0      | AlienBullet1State      | Alien bullet 1, control state register |
| 43D1      | AlienBullet1Shape      | Alien bullet 1, character code ($58 to $5F) |
| 43D2      | AlienBullet1X          | Alien bullet 1, coordinate X |
| 43D3      | AlienBullet1Y          | Alien bullet 1, coordinate Y |
| 43D4      | AlienBullet2State      | Alien bullet 2, control state register |
| 43D5      | AlienBullet2Shape      | Alien bullet 2, character code ($58 to $5F) |
| 43D6      | AlienBullet2X          | Alien bullet 2, coordinate X |
| 43D7      | AlienBullet2Y          | Alien bullet 2, coordinate Y |
| 43D8      | AlienBullet3State      | Alien bullet 3, control state register |
| 43D9      | AlienBullet3Shape      | Alien bullet 3, character code ($58 to $5F) |
| 43DA      | AlienBullet3X          | Alien bullet 3, coordinate X |
| 43DB      | AlienBullet3Y          | Alien bullet 3, coordinate Y |
| 43DC      | AlienBullet4State      | Alien bullet 4, control state register |
| 43DD      | AlienBullet4Shape      | Alien bullet 4, character code ($58 to $5F) |
| 43DE      | AlienBullet4X          | Alien bullet 4, coordinate X |
| 43DF      | AlienBullet4Y          | Alien bullet 4, coordinate Y |


## Player and player bullets, data structure (screen ram)

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 43E0      | OldPlayerShipMSB        | Old MSB screen ram: Upper left character of player ship |
| 43E1      | OldPlayerShipLSB        | Old LSB screen ram: Upper left character of player ship |
| 43E2      | PlayerShipMSB           | MSB screen ram: Upper left character of player ship |
| 43E3      | PlayerShipLSB           | LSB screen ram: Upper left character of player ship |
| 43E4      | PlayerBulletMSB         | MSB screen ram: Player bullet |
| 43E5      | PlayerBulletLSB         | LSB screen ram: Player bullet |
| 43E6      | AbovePlayerBulletMSB    | MSB screen ram: One character above player bullet |
| 43E7      | AbovePlayerBulletLSB    | LSB screen ram: One character above player bullet |
| 43E8      | M43E8                   | ? |
| 43E9      | M43E9                   | ? |
| 43EA      | M43EA                   | ? |
| 43EB      | M43EB                   | ? |


## Alien bullets, data structure (screen ram)

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 43EC      | OldAlienBullet0MSB      | Old MSB screen ram: Alien bullet 0 |
| 43ED      | OldAlienBullet0LSB      | Old LSB screen ram: Alien bullet 0 |
| 43EE      | AlienBullet0MSB         | MSB screen ram: Alien bullet 0 |
| 43EF      | AlienBullet0LSB         | LSB screen ram: Alien bullet 0 |
| 43F0      | OldAlienBullet1MSB      | Old MSB screen ram: Alien bullet 1 |
| 43F1      | OldAlienBullet1LSB      | Old LSB screen ram: Alien bullet 1 |
| 43F2      | AlienBullet1MSB         | MSB screen ram: Alien bullet 1 |
| 43F3      | AlienBullet1LSB         | LSB screen ram: Alien bullet 1 |
| 43F4      | OldAlienBullet2MSB      | Old MSB screen ram: Alien bullet 2 |
| 43F5      | OldAlienBullet2LSB      | Old LSB screen ram: Alien bullet 2 |
| 43F6      | AlienBullet2MSB         | MSB screen ram: Alien bullet 2 |
| 43F7      | AlienBullet2LSB         | LSB screen ram: Alien bullet 2 |
| 43F8      | OldAlienBullet3MSB      | Old MSB screen ram: Alien bullet 3 |
| 43F9      | OldAlienBullet3LSB      | Old LSB screen ram: Alien bullet 3 |
| 43FA      | AlienBullet3MSB         | MSB screen ram: Alien bullet 3 |
| 43FB      | AlienBullet3LSB         | LSB screen ram: Alien bullet 3 |
| 43FC      | OldAlienBullet4MSB      | Old MSB screen ram: Alien bullet 4 |
| 43FD      | OldAlienBullet4LSB      | Old LSB screen ram: Alien bullet 4 |
| 43FE      | AlienBullet4MSB         | MSB screen ram: Alien bullet 4 |
| 43FF      | AlienBullet4LSB         | LSB screen ram: Alien bullet 4 |


## Background screen 

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 4800:4B3F | BackgroundScreen     | 32*26 bytes for the background screen |


## Pointer to alien movement pattern

Default values (all: $10,$00 pointing to T1000) are defined at table: T1520.

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 4B50      | M4B50                | Alien0 movement pattern table MSB |
| 4B51      | M4B51                | Alien0 movement pattern table LSB |
| 4B52      | M4B52                | Alien1 movement pattern table MSB |
| 4B53      | M4B53                | Alien1 movement pattern table LSB |
| 4B54      | M4B54                | Alien2 movement pattern table MSB |
| 4B55      | M4B55                | Alien2 movement pattern table LSB |
| 4B56      | M4B56                | Alien3 movement pattern table MSB |
| 4B57      | M4B57                | Alien3 movement pattern table LSB |
| 4B58      | M4B58                | Alien4 movement pattern table MSB |
| 4B59      | M4B59                | Alien4 movement pattern table LSB |
| 4B5A      | M4B5A                | Alien5 movement pattern table MSB |
| 4B5B      | M4B5B                | Alien5 movement pattern table LSB |
| 4B5C      | M4B5C                | Alien6 movement pattern table MSB |
| 4B5D      | M4B5D                | Alien6 movement pattern table LSB |
| 4B5E      | M4B5E                | Alien7 movement pattern table MSB |
| 4B5F      | M4B5F                | Alien7 movement pattern table LSB |
| 4B60      | M4B60                | Alien8 movement pattern table MSB |
| 4B61      | M4B61                | Alien8 movement pattern table LSB |
| 4B62      | M4B62                | Alien9 movement pattern table MSB |
| 4B63      | M4B63                | Alien9 movement pattern table LSB |
| 4B64      | M4B64                | AlienA movement pattern table MSB |
| 4B65      | M4B65                | AlienA movement pattern table LSB |
| 4B66      | M4B66                | AlienB movement pattern table MSB |
| 4B67      | M4B67                | AlienB movement pattern table LSB |
| 4B68      | M4B68                | AlienC movement pattern table MSB |
| 4B69      | M4B69                | AlienC movement pattern table LSB |
| 4B6A      | M4B6A                | AlienD movement pattern table MSB |
| 4B6B      | M4B6B                | AlienD movement pattern table LSB |
| 4B6C      | M4B6C                | AlienE movement pattern table MSB |
| 4B6D      | M4B6D                | AlienE movement pattern table LSB |
| 4B6E      | M4B6E                | AlienF movement pattern table MSB |
| 4B6F      | M4B6F                | AlienF movement pattern table LSB |


## Alien data structure (grid)

Used for all levels with the 16 aliens.
Level: 1, 2, 5 (with mothership), 6, 7, 10(with mothership).
During 'fade in' phase, the alien control state B is holding the character code!

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 4B70      | M4B70                | Alien0 control state A     |
| 4B71      | M4B71                | Alien0 control state B (LSB for T14xx) |
| 4B72      | M4B72                | Alien0 screen coordinate X |
| 4B73      | M4B73                | Alien0 screen coordinate Y |
| 4B74      | M4B74                | Alien1 control state A     |
| 4B75      | M4B75                | Alien1 control state B (LSB for T14xx) |
| 4B76      | M4B76                | Alien1 screen coordinate X |
| 4B77      | M4B77                | Alien1 screen coordinate Y |
| 4B78      | M4B78                | Alien2 control state A     |
| 4B79      | M4B79                | Alien2 control state B (LSB for T14xx) |
| 4B7A      | M4B7A                | Alien2 screen coordinate X |
| 4B7B      | M4B7B                | Alien2 screen coordinate Y |
| 4B7C      | M4B7C                | Alien3 control state A     |
| 4B7D      | M4B7D                | Alien3 control state B (LSB for T14xx) |
| 4B7E      | M4B7E                | Alien3 screen coordinate X |
| 4B7F      | M4B7F                | Alien3 screen coordinate Y |
| 4B80      | M4B80                | Alien4 control state A     |
| 4B81      | M4B81                | Alien4 control state B (LSB for T14xx) |
| 4B82      | M4B82                | Alien4 screen coordinate X |
| 4B83      | M4B83                | Alien4 screen coordinate Y |
| 4B84      | M4B84                | Alien5 control state A     |
| 4B85      | M4B85                | Alien5 control state B (LSB for T14xx) |
| 4B86      | M4B86                | Alien5 screen coordinate X |
| 4B87      | M4B87                | Alien5 screen coordinate Y |
| 4B88      | M4B88                | Alien6 control state A     |
| 4B89      | M4B89                | Alien6 control state B (LSB for T14xx) |
| 4B8A      | M4B8A                | Alien6 screen coordinate X |
| 4B8B      | M4B8B                | Alien6 screen coordinate Y |
| 4B8C      | M4B8C                | Alien7 control state A     |
| 4B8D      | M4B8D                | Alien7 control state B (LSB for T14xx) |
| 4B8E      | M4B8E                | Alien7 screen coordinate X |
| 4B8F      | M4B8F                | Alien7 screen coordinate Y |
| 4B90      | M4B90                | Alien8 control state A     |
| 4B91      | M4B91                | Alien8 control state B (LSB for T14xx) |
| 4B92      | M4B92                | Alien8 screen coordinate X |
| 4B93      | M4B93                | Alien8 screen coordinate Y |
| 4B94      | M4B94                | Alien9 control state A     |
| 4B95      | M4B95                | Alien9 control state B (LSB for T14xx) |
| 4B96      | M4B96                | Alien9 screen coordinate X |
| 4B97      | M4B97                | Alien9 screen coordinate Y |
| 4B98      | M4B98                | AlienA control state A     |
| 4B99      | M4B99                | AlienA control state B (LSB for T14xx) |
| 4B9A      | M4B9A                | AlienA screen coordinate X |
| 4B9B      | M4B9B                | AlienA screen coordinate Y |
| 4B9C      | M4B9C                | AlienB control state A     |
| 4B9D      | M4B9D                | AlienB control state B (LSB for T14xx) |
| 4B9E      | M4B9E                | AlienB screen coordinate X |
| 4B9F      | M4B9F                | AlienB screen coordinate Y |
| 4BA0      | M4BA0                | AlienC control state A     |
| 4BA1      | M4BA1                | AlienC control state B (LSB for T14xx) |
| 4BA2      | M4BA2                | AlienC screen coordinate X |
| 4BA3      | M4BA3                | AlienC screen coordinate Y |
| 4BA4      | M4BA4                | AlienD control state A     |
| 4BA5      | M4BA5                | AlienD control state B (LSB for T14xx) |
| 4BA6      | M4BA6                | AlienD screen coordinate X |
| 4BA7      | M4BA7                | AlienD screen coordinate Y |
| 4BA8      | M4BA8                | AlienE control state A     |
| 4BA9      | M4BA9                | AlienE control state B (LSB for T14xx) |
| 4BAA      | M4BAA                | AlienE screen coordinate X |
| 4BAB      | M4BAB                | AlienE screen coordinate Y |
| 4BAC      | M4BAC                | AlienF control state A     |
| 4BAD      | M4BAD                | AlienF control state B (LSB for T14xx) |
| 4BAE      | M4BAE                | AlienF screen coordinate X |
| 4BAF      | M4BAF                | AlienF screen coordinate Y |

## Bird data structure 

Used for all levels with the 8 birds.
Level: 3, 4, 8, 9.
For the bird animation during intro splash, bird0 memory is used.

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 4B70      | B4B70                | Bird0 index character block shape ? |
| 4B71      | B4B71                | Bird0 MSB initial screen address ?  |
| 4B72      | B4B72                | Bird0 LSB initial screen address ?  |
| 4B73      | B4B73                | Bird0 ?                             |
| 4B74      | B4B74                | Bird0 ?                             |
| 4B75      | B4B75                | Bird0 grid coordinate X ?           |
| 4B76      | B4B76                | Bird0 ?                             |
| 4B77      | B4B77                | Bird0 grid coordinate Y ?           |
| 4B78      | B4B78                | Bird1 index character block shape ? |
| 4B79      | B4B79                | Bird1 MSB initial screen address ?  |
| 4B7A      | B4B7A                | Bird1 LSB initial screen address ?  |
| 4B7B      | B4B7B                | Bird1 ?                             |
| 4B7C      | B4B7C                | Bird1 ?                             |
| 4B7D      | B4B7D                | Bird1 grid coordinate X ?           |
| 4B7E      | B4B7E                | Bird1 ?                             |
| 4B7F      | B4B7F                | Bird1 grid coordinate Y ?           |
| 4B80      | B4B80                | Bird2 index character block shape ? |
| 4B81      | B4B81                | Bird2 MSB initial screen address ?  |
| 4B82      | B4B82                | Bird2 LSB initial screen address ?  |
| 4B83      | B4B83                | Bird2 ?                             |
| 4B84      | B4B84                | Bird2 ?                             |
| 4B85      | B4B85                | Bird2 grid coordinate X ?           |
| 4B86      | B4B86                | Bird2 ?                             |
| 4B87      | B4B87                | Bird2 grid coordinate Y ?           |
| 4B88      | B4B88                | Bird3 index character block shape ? |
| 4B89      | B4B89                | Bird3 MSB initial screen address ?  |
| 4B8A      | B4B8A                | Bird3 LSB initial screen address ?  |
| 4B8B      | B4B8B                | Bird3 ?                             |
| 4B8C      | B4B8C                | Bird3 ?                             |
| 4B8D      | B4B8D                | Bird3 grid coordinate X ?           |
| 4B8E      | B4B8E                | Bird3 ?                             |
| 4B8F      | B4B8F                | Bird3 grid coordinate Y ?           |
| 4B90      | B4B90                | Bird4 index character block shape ? |
| 4B91      | B4B91                | Bird4 MSB initial screen address ?  |
| 4B92      | B4B92                | Bird4 LSB initial screen address ?  |
| 4B93      | B4B93                | Bird4 ?                             |
| 4B94      | B4B94                | Bird4 ?                             |
| 4B95      | B4B95                | Bird4 grid coordinate X ?           |
| 4B96      | B4B96                | Bird4 ?                             |
| 4B97      | B4B97                | Bird4 grid coordinate Y ?           |
| 4B98      | B4B98                | Bird5 index character block shape ? |
| 4B99      | B4B99                | Bird5 MSB initial screen address ?  |
| 4B9A      | B4B9A                | Bird5 LSB initial screen address ?  |
| 4B9B      | B4B9B                | Bird5 ?                             |
| 4B9C      | B4B9C                | Bird5 ?                             |
| 4B9D      | B4B9D                | Bird5 grid coordinate X ?           |
| 4B9E      | B4B9E                | Bird5 ?                             |
| 4B9F      | B4B9F                | Bird5 grid coordinate Y ?           |
| 4BA0      | B4BA0                | Bird6 index character block shape ? |
| 4BA1      | B4BA1                | Bird6 MSB initial screen address ?  |
| 4BA2      | B4BA2                | Bird6 LSB initial screen address ?  |
| 4BA3      | B4BA3                | Bird6 ?                             |
| 4BA4      | B4BA4                | Bird6 ?                             |
| 4BA5      | B4BA5                | Bird6 grid coordinate X ?           |
| 4BA6      | B4BA6                | Bird6 ?                             |
| 4BA7      | B4BA7                | Bird6 grid coordinate Y ?           |
| 4BA8      | B4BA8                | Bird7 index character block shape ? |
| 4BA9      | B4BA9                | Bird7 MSB initial screen address ?  |
| 4BAA      | B4BAA                | Bird7 LSB initial screen address ?  |
| 4BAB      | B4BAB                | Bird7 ?                             |
| 4BAC      | B4BAC                | Bird7 ?                             |
| 4BAD      | B4BAD                | Bird7 grid coordinate X ?           |
| 4BAE      | B4BAE                | Bird7 ?                             |
| 4BAF      | B4BAF                | Bird7 grid coordinate Y ?           |


## Alien data structure (screen ram)

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 4BB0      | M4BB0                | Old MSB screen ram adress alien0 |
| 4BB1      | M4BB1                | Old LSB screen ram adress alien0 |
| 4BB2      | M4BB2                | MSB screen ram adress alien0 |
| 4BB3      | M4BB3                | LSB screen ram adress alien0 |
| 4BB4      | M4BB4                | Old MSB screen ram adress alien1 |
| 4BB5      | M4BB5                | Old LSB screen ram adress alien1 |
| 4BB6      | M4BB6                | MSB screen ram adress alien1 |
| 4BB7      | M4BB7                | LSB screen ram adress alien1 |
| 4BB8      | M4BB8                | Old MSB screen ram adress alien2 |
| 4BB9      | M4BB9                | Old LSB screen ram adress alien2 |
| 4BBA      | M4BBA                | MSB screen ram adress alien2 |
| 4BBB      | M4BBB                | LSB screen ram adress alien2 |
| 4BBC      | M4BBC                | Old MSB screen ram adress alien3 |
| 4BBD      | M4BBD                | Old LSB screen ram adress alien3 |
| 4BBE      | M4BBE                | MSB screen ram adress alien3 |
| 4BBF      | M4BBF                | LSB screen ram adress alien3 |
| 4BC0      | M4BC0                | Old MSB screen ram adress alien4 |
| 4BC1      | M4BC1                | Old LSB screen ram adress alien4 |
| 4BC2      | M4BC2                | MSB screen ram adress alien4 |
| 4BC3      | M4BC3                | LSB screen ram adress alien4 |
| 4BC4      | M4BC4                | Old MSB screen ram adress alien5 |
| 4BC5      | M4BC5                | Old LSB screen ram adress alien5 |
| 4BC6      | M4BC6                | MSB screen ram adress alien5 |
| 4BC7      | M4BC7                | LSB screen ram adress alien5 |
| 4BC8      | M4BC8                | Old MSB screen ram adress alien6 |
| 4BC9      | M4BC9                | Old LSB screen ram adress alien6 |
| 4BCA      | M4BCA                | MSB screen ram adress alien6 |
| 4BCB      | M4BCB                | LSB screen ram adress alien6 |
| 4BCC      | M4BCC                | Old MSB screen ram adress alien7 |
| 4BCD      | M4BCD                | Old LSB screen ram adress alien7 |
| 4BCE      | M4BCE                | MSB screen ram adress alien7 |
| 4BCF      | M4BCF                | LSB screen ram adress alien7 |
| 4BD0      | M4BD0                | Old MSB screen ram adress alien8 |
| 4BD1      | M4BD1                | Old LSB screen ram adress alien8 |
| 4BD2      | M4BD2                | MSB screen ram adress alien8 |
| 4BD3      | M4BD3                | LSB screen ram adress alien8 |
| 4BD4      | M4BD4                | Old MSB screen ram adress alien9 |
| 4BD5      | M4BD5                | Old LSB screen ram adress alien9 |
| 4BD6      | M4BD6                | MSB screen ram adress alien9 |
| 4BD7      | M4BD7                | LSB screen ram adress alien9 |
| 4BD8      | M4BD8                | Old MSB screen ram adress alienA |
| 4BD9      | M4BD9                | Old LSB screen ram adress alienA |
| 4BDA      | M4BDA                | MSB screen ram adress alienA |
| 4BDB      | M4BDB                | LSB screen ram adress alienA |
| 4BDC      | M4BDC                | Old MSB screen ram adress alienB |
| 4BDD      | M4BDD                | Old LSB screen ram adress alienB |
| 4BDE      | M4BDE                | MSB screen ram adress alienB |
| 4BDF      | M4BDF                | LSB screen ram adress alienB |
| 4BE0      | M4BE0                | Old MSB screen ram adress alienC |
| 4BE1      | M4BE1                | Old LSB screen ram adress alienC |
| 4BE2      | M4BE2                | MSB screen ram adress alienC |
| 4BE3      | M4BE3                | LSB screen ram adress alienC |
| 4BE4      | M4BE4                | Old MSB screen ram adress alienD |
| 4BE5      | M4BE5                | Old LSB screen ram adress alienD |
| 4BE6      | M4BE6                | MSB screen ram adress alienD |
| 4BE7      | M4BE7                | LSB screen ram adress alienD |
| 4BE8      | M4BE8                | Old MSB screen ram adress alienE |
| 4BE9      | M4BE9                | Old LSB screen ram adress alienE |
| 4BEA      | M4BEA                | MSB screen ram adress alienE |
| 4BEB      | M4BEB                | LSB screen ram adress alienE |
| 4BEC      | M4BEC                | Old MSB screen ram adress alienF |
| 4BED      | M4BED                | Old LSB screen ram adress alienF |
| 4BEE      | M4BEE                | MSB screen ram adress alienF |
| 4BEF      | M4BEF                | LSB screen ram adress alienF |


## Stack 

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 4BF0:4BFF | Stack                | Stack space |

