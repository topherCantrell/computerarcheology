![RAM](megabug.jpg)

# Game variables

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
| 9E:9F | CurrentScreen | Pointer to the screen buffer being drawn on |
| A0    | NumBugs | Number of bugs in game | 
| A1    | Temp3 | Used in picking the picture when drawing the line of bugs between rounds |
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
| BE:BF | DotsLeft | Number of dots left to be eaten in the maze |
| C2    | JoyOrKey | FF if player is using joystick or 00 if player is using keyboard |
| C3:C4 | DemoTimer | Count-down by the ISR used to time the demo play (and direct restart after losing) |
| C5    | NumStartBugs  | Hold ENTER down at powerup to start the game with 16 bugs |
| C7    | VisiblePage   | Upper byte of address of visible screen page (04 or ??) |

Graphics pages (3K each)
  * 0400 - 0FFF
  * 1000 - 1BFF
  * 1C00 - 27FF
  
The data on the bugs is kept in an array at $2808. 3 bytes each: y,x,dir

28E8-2A27: array of bytes, one per cell, 20*10 cells
