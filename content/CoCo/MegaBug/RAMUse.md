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
| 90:91 | ScrPtr | Pointer to top of screen to draw on |
| 92    | RequestedPage | Upper byte of address of visible screen page (04 or ??) |
| 98    | JumpCnt | Used to count 14 jumps when player gets eaten |
| 9A:9B | ?ScreenPointerA | |
| 9C:9D | ?ScreenPointerB | |
| AB:AC | PixCoords | Coordinates on the screen (y,x) |
| AD    | ColorMask | A color mask for printing characters |
| AE    | ChangeColor | Rotate the color mask after every character (for splash) |
| AF    | NumMinutes | Number of minutes in game time BCD |
| B0    | NumSeconds | Number of seconds in game time BCD |
| B1:B2 | Score | Game score BCD |
| B3:B4 | HighScore | High score BDC |
| B5    | LiveOrDemo | 0 if demo game, not 0 if live game |
| C2    | JoyOrKey | FF if player is using joystick or 00 if player is using keyboard |
| C5    | ??AtBoot??    | set to 8 normally or $10 if ENTER pressed at start |
| C7    | VisiblePage   | Upper byte of address of visible screen page (04 or ??) |

Graphics pages (3K each)
  * 0400 - 0FFF
  * 1000 - 1BFF
  * 1C00 - 27FF