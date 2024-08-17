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

>>> memory

| | | |
| --- | --- | --- |
| 4000:433F | ForegroundScreen     | 32*26 bytes for the foreground screen |
| --- | --- | --- |
| 4360      | M4360                | ? |
| 4361      | M4361                | ? |
| 4363      | M4363                | ? |
| 4370      | M4370                | ? |
| 4374      | M4374                | ? |
| 4378      | M4378                | ? |
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
| 438F      | CoinCount            | Number of coins inserted (max counted is 9) |
| 4390      | Player1Lives         | Player 1 number of lives |
| 4391      | Player2Lives         | Player 2 number of lives |
| 4392      | M4392                | ? |
| 4393      | M4393                | ? |
| 4394      | M4394                | ? |
| 4395      | M4395                | ? |
| 4396      | M4396                | ? |
| 4397      | ?                    | ? |
| 4398      | M4398                | Zero reference for M4399 |
| 4399      | M4399                | Actual index for slow print at intro splash |
| 439A:439B | Counter16            | 16 bit counter (MSB:LSB) and.. |
| 439B      | M439B                | Next index for slow print at intro splash |
| 439E      | M439E                | ? |
| 439F      | M439F                | ? |
| 43A0      | IN0Current           | Current value of IN0     |
| 43A1      | IN0Previous          | Previous value of IN0    |
| 43A2      | GameOrAttract        | Attract mode:0 Game mode:1 |
| 43A3      | GameAndDemoOrSplash  | Game and demo:0 Intro splash:2 |
| 43A4      | GameState            | Game state:0 - 7 |
| 43A5      | Counter8             | 8 bit counter (score flash time) |
| 43A6      | ShieldCount          | Counts shield time and controls shield picture. Shields end at C0. |
| 43A8      | M43A8                | temporary storage (MSB of pointer to table $1860) |
| 43A9      | M43A9                | temporary storage (LSB of pointer to table $1860) |
| 43AB      | M43AB                | ? |
| 43AC      | ?                    | ? |
| 43AD      | ?                    | ? |
| 43AE      | ?                    | ? |
| 43AF      | ?                    | ? |
| 43B0      | ?                    | ? |
| 43B1      | M43B1                | ? |
| 43B2      | ?                    | ? |
| 43B3      | M43B3                | ? |
| 43B4      | B4Counter            | 8 bit counter (stars scrolling down, aliens fade in time) |
| 43B5      | ?                    | ? |
| 43B6      | ?                    | ? |
| 43B8      | LevelAndRound        | bit0 - 3: game level, bit4 - 7: game round |
| 43B9      | M43B9                | free running 8 bit backwards counter |
| 43BA      | M43BA                | ? |
| 43BB      | M43BB                | ? |
| 43BC      | ?                    | ? |
| 43BD      | ?                    | ? |
| 43BE      | BonusLivesAt         | Bonus lives (at 30K, 40K, 50K or 60K) from DIP switch settings |
| 43BF      | ?                    | ? |
| --- | --- | --- |
| 43C0      | M43C0                | 32 byte data structure (43C0:43DF) for player ship and shields ? |
| 43C1      | ?                    |  ? |
| 43C2      | M43C2                |  ? |
| 43C3      | M43C3                |  ? |
| 43C4      | M43C4                |  ? |
| 43C5      | ?                    |  ? |
| 43C6      | ?                    |  ? |
| 43C7      | ?                    |  ? |
| 43C8      | M43C8                |  ? |
| 43C9      | ?                    |  ? |
| 43CA      | ?                    |  ? |
| 43CB      | ?                    |  ? |
| 43CC      | M43CC                |  ? |
| 43CD      | ?                    |  ? |
| 43CE      | M43CE                |  ? |
| 43CF      | ?                    |  ? |
| 43D0      | ?                    |  ? |
| 43D1      | ?                    |  ? |
| 43D2      | ?                    |  ? |
| 43D3      | ?                    |  ? |
| 43D4      | ?                    |  ? |
| 43D5      | ?                    |  ? |
| 43D6      | ?                    |  ? |
| 43D7      | ?                    |  ? |
| 43D8      | ?                    |  ? |
| 43D9      | ?                    |  ? |
| 43DA      | ?                    |  ? |
| 43DB      | ?                    |  ? |
| 43DC      | ?                    |  ? |
| 43DD      | ?                    |  ? |
| 43DE      | ?                    |  ? |
| 43DF      | ?                    |  ? |
| --- | --- | --- |
| 43E0      | M43E0                | 32 byte data structure (43E0:43FF) for player ship and shields ? |
| 43E1      | ?                    |  ? |
| 43E2      | PlayerCoordMSB       |  The X,Y in screen memory (doesn't include bit offset) |
| 43E3      | PlayerCoordLSB       |  The X,Y in screen memory (doesn't include bit offset) |
| 43E4      | ?                    |  ? |
| 43E5      | ?                    |  ? |
| 43E6      | M43E6                |  ? |
| 43E7      | ?                    |  ? |
| 43E8      | ?                    |  ? |
| 43E9      | ?                    |  ? |
| 43EA      | M43EA                |  ? |
| 43EB      | M43EB                |  ? |
| 43EC      | M43EC                |  ? |
| 43ED      | ?                    |  ? |
| 43EE      | M43EE                |  ? |
| 43EF      | ?                    |  ? |
| 43F0      | ?                    |  ? |
| 43F1      | ?                    |  ? |
| 43F2      | ?                    |  ? |
| 43F3      | ?                    |  ? |
| 43F4      | ?                    |  ? |
| 43F5      | ?                    |  ? |
| 43F6      | ?                    |  ? |
| 43F7      | ?                    |  ? |
| 43F8      | ?                    |  ? |
| 43F9      | ?                    |  ? |
| 43FA      | ?                    |  ? |
| 43FB      | ?                    |  ? |
| 43FC      | ?                    |  ? |
| 43FD      | ?                    |  ? |
| 43FE      | ?                    |  ? |
| 43FF      | M43FF                |  ? |
| --- | --- | --- |
| 4800:4B3F | BackgroundScreen     | 32*26 bytes for the background screen |
| --- | --- | --- |
| 4B50      | M4B50                | ? |
| --- | --- | --- |
| 4B70      | M4B70                |  alien0 control state A ?   |
| 4B71      | M4B71                |  alien0 control state B ?   |
| 4B72      | M4B72                |  alien0 screen coordinate X |
| 4B73      | M4B73                |  alien0 screen coordinate Y |
| 4B74      | M4B74                |  alien1 control state A ?   |
| 4B75      | M4B75                |  alien1 control state B ?   |
| 4B76      | M4B76                |  alien1 screen coordinate X |
| 4B77      | M4B77                |  alien1 screen coordinate Y |
| 4B78      | M4B78                |  alien2 control state A ?   |
| 4B79      | M4B79                |  alien2 control state B ?   |
| 4B7A      | M4B7A                |  alien2 screen coordinate X |
| 4B7B      | M4B7B                |  alien2 screen coordinate Y |
| 4B7C      | M4B7C                |  alien3 control state A ?   |
| 4B7D      | M4B7D                |  alien3 control state B ?   |
| 4B7E      | M4B7E                |  alien3 screen coordinate X |
| 4B7F      | M4B7F                |  alien3 screen coordinate Y |
| 4B80      | M4B80                |  alien4 control state A ?   |
| 4B81      | M4B81                |  alien4 control state B ?   |
| 4B82      | M4B82                |  alien4 screen coordinate X |
| 4B83      | M4B83                |  alien4 screen coordinate Y |
| 4B84      | M4B84                |  alien5 control state A ?   |
| 4B85      | M4B85                |  alien5 control state B ?   |
| 4B86      | M4B86                |  alien5 screen coordinate X |
| 4B87      | M4B87                |  alien5 screen coordinate Y |
| 4B88      | M4B88                |  alien6 control state A ?   |
| 4B89      | M4B89                |  alien6 control state B ?   |
| 4B8A      | M4B8A                |  alien6 screen coordinate X |
| 4B8B      | M4B8B                |  alien6 screen coordinate Y |
| 4B8C      | M4B8C                |  alien7 control state A ?   |
| 4B8D      | M4B8D                |  alien7 control state B ?   |
| 4B8E      | M4B8E                |  alien7 screen coordinate X |
| 4B8F      | M4B8F                |  alien7 screen coordinate Y |
| 4B90      | M4B90                |  alien8 control state A ?   |
| 4B91      | M4B91                |  alien8 control state B ?   |
| 4B92      | M4B92                |  alien8 screen coordinate X |
| 4B93      | M4B93                |  alien8 screen coordinate Y |
| 4B94      | M4B94                |  alien9 control state A ?   |
| 4B95      | M4B95                |  alien9 control state B ?   |
| 4B96      | M4B96                |  alien9 screen coordinate X |
| 4B97      | M4B97                |  alien9 screen coordinate Y |
| 4B98      | M4B98                |  alienA control state A ?   |
| 4B99      | M4B99                |  alienA control state B ?   |
| 4B9A      | M4B9A                |  alienA screen coordinate X |
| 4B9B      | M4B9B                |  alienA screen coordinate Y |
| 4B9C      | M4B9C                |  alienB control state A ?   |
| 4B9D      | M4B9D                |  alienB control state B ?   |
| 4B9E      | M4B9E                |  alienB screen coordinate X |
| 4B9F      | M4B9F                |  alienB screen coordinate Y |
| 4BA0      | M4BA0                |  alienC control state A ?   |
| 4BA1      | M4BA1                |  alienC control state B ?   |
| 4BA2      | M4BA2                |  alienC screen coordinate X |
| 4BA3      | M4BA3                |  alienC screen coordinate Y |
| 4BA4      | M4BA4                |  alienD control state A ?   |
| 4BA5      | M4BA5                |  alienD control state B ?   |
| 4BA6      | M4BA6                |  alienD screen coordinate X |
| 4BA7      | M4BA7                |  alienD screen coordinate Y |
| 4BA8      | M4BA8                |  alienE control state A ?   |
| 4BA9      | M4BA9                |  alienE control state B ?   |
| 4BAA      | M4BAA                |  alienE screen coordinate X |
| 4BAB      | M4BAB                |  alienE screen coordinate Y |
| 4BAC      | M4BAC                |  alienF control state A ?   |
| 4BAD      | M4BAD                |  alienF control state B ?   |
| 4BAE      | M4BAE                |  alienF screen coordinate X |
| 4BAF      | M4BAF                |  alienF screen coordinate Y |
| --- | --- | --- |
| 4BB0      | M4BB0                | ? |
| 4BB3      | M4BB3                | ? |
| 4BC0      | M4BC0                | ? |
| --- | --- | --- |
| 4BD8:4BFF | Stack                | Stack space |
| --- | --- | --- |
