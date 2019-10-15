![RAM](megabug.jpg)

# Game variables

>>> memory
| | | |
| ----  | ---- | ---- |
| 80:81 | Note1 | Tone value for note 1 |
| 82:83 | Note2 | Tone value for note 2 |
| 84:85 | NoteC1 | Note1 tally count |
| 86:87 | NoteC2 | Note2 tally count |
| 88    | BitPos | Pixel position while printing, neighbor count in maze generation |
| 89    | BitPosSrc | Pixel position of the source while drawing the magnifier |
| 8A:8B | HeadCellList | Start of the list of cells needing visiting in the maze draw |
| 8C:8D | EndCellList | End of the list (+1) of cells needing visiting |
| 8E:8F | Temp1 | Used to check coordinates and other ?? |
| 90:91 | RndSeed | Used to fetch bytes from ROM as random numbers |
| 92    | RequestedPage | Upper byte of address of visible screen page (04 or ??) |
| 93:94 | GenDirection | Current direction in maze generation |
| 95:96 | TargetCell | The target cell last used by the open-cell-wall function |
| 97    | WallOpened | Maze generation. 00 if a wall was opened during the dig run |
| 98    | Temp2 | General use |
| 99    | Temp3 | General use (used as a counter in finding possible directions for a bug) |
| 9A:9B | DrawingScreenPtr | The screen that is currently being drawn on (1000 or 1C00) |
| 9C:9D | VisibleScreenPtr | The screen that is currently being shown (1000 or 1C00) |
| 9E:9F | ScreenPtr        | Pointer to the screen buffer being drawn on (1000, 1C00, or 0400) |
| A0    | NumBugs          | Number of bugs in game | 
| A1    | MouthOpen        | 0 if mouth is open or 1 if mouth is closed. Used as a temporary between rounds. |
| A2:A3 | PlayerCoords     | Player's coordinates on the screen (y,x) |
| A4    | PlayerDir        | Player's facing direction |
| A5    | HorzDoubler      | Flag used to double the horizontal pixels when magnified |
| A6    | Temp4            | Used with A5 as a temporary word |
| A7:A8 | MagnifierStart   | Starting point screen pointer of the magnifier |
| A9:AA | MagnifierEnd     | The last screen pointer of the magnifier |
| AB:AC | PixCoords        | Coordinates on the screen (y,x) |
| AD    | ColorMask        | A color mask for printing characters |
| AE    | ChangeColor      | Rotate the color mask after every character (for splash) |
| AF    | NumMinutes       | Number of minutes in game time BCD |
| B0    | NumSeconds       | Number of seconds in game time BCD |
| B1:B2 | Score | Game score BCD |
| B3:B4 | HighScore | High score BDC |
| B5    | LiveOrDemo | 0 if demo game, not 0 if live game |
| B6    | ISRCountScore | Counts ISRs in live game mode to decrement score once a second |
| B7    | ISRCountTime  | Counts ISRs in live game to increment the time once a second |
| B8    | DrawScore | 0 to skip drawing the score or non-zero to draw it |
| B9    | DrawCountSecs | 0 to skip drawing seconds-count or non-zero to draw it |
| BA    | MakeEatSound | Non-zero to play the eat-dot-sound |
| BB    | EatSnd1 | Used in timing the sound effect for eating-a-dot |
| BC    | EatSnd2 | Used in timing the sound effect for eating-a-dot |
| BD    | EatSnd3 | Used in timing the sound effect for eating-a-dot |
| BE:BF | DotsLeft | Number of dots left to be eaten in the maze |
| C0    | MazeLoopiness | Controls the loopiness of the maze. If RND>=<$C0 then dead-end, otherwise a loop. Starts at $C0 and divides by two each level (more dead-ends)  |
| C1    | ShowingGame | FF if game screen is showing. 00 if other things are being shown. |
| C2    | JoyOrKey | FF if player is using joystick or 00 if player is using keyboard |
| C3:C4 | DemoTimer | Count-down by the ISR used to time the demo play (and direct restart after losing) |
| C5    | NumStartBugs  | Hold ENTER down at powerup to start the game with 16 bugs |
| C6    | PlayShortSong | 00 if we should play the long song or FF if we already have (and should play the short song) |
| C7    | VisiblePage   | Upper byte of address of visible screen page  |

Graphics pages (3K each)
  * 0400 - 0FFF
  * 1000 - 1BFF
  * 1C00 - 27FF
  
The data on the bugs is kept in an array at $2808. 3 bytes each: y,x,dir

  * 2800:2807: during maze generation, list of unvisited neighbors (2 bytes * 4 possible)
  * 2808:2868: data on up to 32 bugs ... 3 bytes each (y,x,dir)
  * 2868:28C7: ?? duplicate of the previous data (y,x,dir) ?? Seems to be two sets of data for mouth open/close times ??
  * 28C8:28E7: column-has-content flags set by the draw-magnifier routine and read by the draw-bug routine
  * 28E8:2A27: array of bytes, one per cell, 20*10 cells. 00=not visited, FF=visited
  * 2A28:????: array of words, coordinates of cells we need to revisit in the maze generation
