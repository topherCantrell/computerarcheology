![Asteroids](Asteroids.jpg)

# Asteroids Hardware

There is 1K game RAM, 2K vector-RAM, 2K vector-ROM, and 6K game ROM.

The CPU runs at 1.5MHz.

The MMI interrupt is clocked at 250Hz.

The upper address line is ignored. Thus the interrupt vectors beginning at FFFA
map to the ROM space at 7FFA. The ROM was assembled with 6000-7FFF addresses
and not E000-FFFF.

The DVG and CPU share the memory space from 4000-5FFF (8K bytes). 
The DVG reads this as 4K words. The address mapping is shown above.
Only half of the RAM/ROM space is actually populated. There is room
for expansion.

## IN0 

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 2001      | CLCK3KHZ  | 3 KHz  Clock      |
| 2002      | HALT      | HALT Switch       |
| 2003      | SWHYPER   | Hyperspace Switch |
| 2004      | SWFIRE    | Fire Switch       |
| 2005      | SWDIAGST  | Diagnostic Step   |
| 2006      | SWSLAM    | Slam Switch       |
| 2007      | SWTEST    | Self Test Switch  |


## IN1 

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 2400      | SWLCOIN   | Left Coin Switch      |
| 2401      | SWCCOIN   | Center Coin Switch    |
| 2402      | SWRCOIN   | Right Coin Switch     |
| 2403      | SW1START  | 1 Player Start Switch |
| 2404      | SW2START  | 2 Player Start Switch |
| 2405      | SWTHRUST  | Thrust Switch         |
| 2406      | SWROTRGHT | Rotate Right Switch   |
| 2407      | SWROTLEFT | Rotate Left Switch    |


## DSW1 

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 2800      | SWCOINAGE  | Coinage 0 = Free Play, 1 = 1 Coin 2 Credits, 2 = 1 Coin 1 Credit, 3 = 2 Coins 1 Credit | 
| 2801      | SWCNRMULT  | Right Coin Multiplier 0 = 1x, 1 = 4x, 2 = 5x, 3 = 6x | 
| 2802      | SWCNCMULT  | Center Coin Multiplier & Starting Lives 1x & 4, 1 = 1x & 3, 2 = 2x & 4, 3 = 2x & 3 | 
| 2803      | SWLANGUAGE | Language 0 = English, 1 = German, 2 = French, 3 = Spanish |


## Other 

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |
| 3000      | GODVG     | AVG/DVG Go          |
| 3200      | LMPSCNS   | Bit 1 = 2 Player Start Lamp, Bit 2 = 1 Player Start Lamp, Bit 3 = RAMSEL, Bit 4 = Left Coin Counter, Bit 5 = Center Coin Counter, Bit 6 = Right Coin Counter |
| 3400      | WATCHDOG  | Watchdog            |
| 3600      | SNDEXP    | Sound (explosion)   |
| 3A00      | SNDTHUMP  | Sound (thump)       |
| 3C00      | SNDSAUCR  | Sound (saucer)      |
| 3C01      | SNDSFIRE  | Sound (saucer fire) |
| 3C02      | SNDSELSAU | Sound Select (large/small saucer) |
| 3C03      | SNDTHRUST | Sound (ship thrust) |
| 3C04      | SNDFIRE   | Sound (ship fire)   |
| 3C05      | SNDBONUS  | Sound (bonus life)  |
| 3E00      | SNDRESET  | Sound (noise reset) |
| 4000:47FF | VRAM      | Vector RAM   DVG word 0000-03FF |
| 4800:4FFF | VRAMunusd | Unused VRAM  DVG word 0400-07FF |
| 5000:47FF | VROM      | Vector ROM   DVG word 0800-0BFF |
| 5800:5FFF | VROMunusd | Unused VROM  DVG word 0C00-0FFF |

