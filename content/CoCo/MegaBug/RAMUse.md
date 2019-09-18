![RAM](megabug.jpg)

# Game variables DP=??

>>> memory
| | | |
| ----  | ---- | ---- |
| 80:81 | Note1 | Tone value for note 1 |
| 82:83 | Note2 | Tone value for note 2 |
| 84:85 | NoteC1 | Note1 tally count |
| 86:87 | NoteC2 | Note2 tally count |
| 88    | BitPos | Pixel position while printing |
| 8E:8F | Temp2 | Used to check coordinates and other ?? |
| 90:91 | RndSeed | Used to fetch bytes from ROM as random numbers |
| 92    | RequestedPage | Upper byte of address of visible screen page (04 or ??) |
| 98    | Temp1 | General use |
| 9A:9B | ?ScreenPointerA | |
| 9C:9D | ?ScreenPointerB | |
| A0    | NumBugs | Number of bugs in game | 
| A2:A3 | PlayerCoords | Player's coordinates on the screen (y,x) |
| A4    | PlayerDir | Player's facing direction |
| AB:AC | PixCoords | Coordinates on the screen (y,x) |
| AD    | ColorMask | A color mask for printing characters |
| AE    | ChangeColor | Rotate the color mask after every character (for splash) |
| AF    | NumMinutes | Number of minutes in game time BCD |
| B0    | NumSeconds | Number of seconds in game time BCD |
| B1:B2 | Score | Game score BCD |
| B3:B4 | HighScore | High score BDC |
| B5    | LiveOrDemo | 0 if demo game, not 0 if live game |
| B6    | ISRCountScore | Counts ISRs in live game mode to decrement score once a second |
| B7    | ISRCountTime  | Counts ISRs in live game to increment the time once a second |
| C2    | JoyOrKey | FF if player is using joystick or 00 if player is using keyboard |
| C5    | ??AtBoot??    | set to 8 normally or $10 if ENTER pressed at start |
| C7    | VisiblePage   | Upper byte of address of visible screen page (04 or ??) |

Graphics pages (3K each)
  * 0400 - 0FFF
  * 1000 - 1BFF
  * 1C00 - 27FF
  
The data on the bugs is kept in an array at $2808. 3 bytes each: y,x,dir
