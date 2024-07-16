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
| 4380      | M4380??              | ?? part of scoring ?? |
| 4381      | Score1high           | Player 1 score BCD (high) |
| 4382      | Score1mid            | Player 1 score BCD (mid) |
| 4383      | Score1low            | Player 1 score BCD (low) |
| 4385      | Score2high           | Player 2 score BCD (high) |
| 4386      | Score2mid            | Player 2 score BCD (mid) |
| 4387      | Score2low            | Player 2 score BCD (low) |
| 4389      | HiScorehigh          | Hi score BCD (high) |
| 438A      | HiScoremid           | Hi score BCD (mid) |
| 438B      | HiScorelow           | Hi score BCD (low) |
| 438C      | SoundControlA        | RAM copy of sound device control register A (0x6000) |
| 438D      | SoundControlB        | RAM copy of sound device control register B (0x6800) |
| 438F      | CoinCount            | Number of coins inserted (max counted is 9) |
| 4390      | Player1Lives         | Player 1 number of lives |
| 4391      | Player2Lives         | Player 2 number of lives |
| 439A:439B | Counter16            | 16 bit counter (MSB:LSB) |
| 43A0      | IN0Current           | Current value of IN0     |
| 43A1      | IN0Previous          | Previous value of IN0    |
| 43A2      | GameOrAttract        | Attract mode:0 Game mode:1 |
| 43A4      | GameState            | Game state:0 - 7 |
| 43A5      | Counter8             | 8 bit counter (score flash time) |
| 43A6      | ShieldCount??        | Counts shield time and controls shield picture. Shields end at C0. |
| 43B8      | LevelAndRound        | bit0 - 3: game level, bit4 - 7: game round |
| 43C0      | M43C0??              | ?? shields |        
| 43E2      | PlayerCoordMSB       | The X,Y in screen memory (doesn't include bit offset) |
| 43E3      | PlayerCoordLSB       | The X,Y in screen memory (doesn't include bit offset) |
| 4800:4B3F | BackgroundScreen     | 32*26 bytes for the background screen |
| 4B40:4BFF | Stack                | Stack space |
