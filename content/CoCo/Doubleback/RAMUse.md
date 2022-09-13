![Doubleback Usage](doubleback.jpg)

# Doubleback RAM Usage

The game works with 4K of RAM, which means it only uses one
screen buffer.

Stack builds to lower from 0150.

Screen uses 0400 to 1000.

>>> memory
|       |            |     |
| ----- | ---------- | ----------------- |
| B4    | numPlayers | 0 for ONE PLAYER, 1 for TWO PLAYER |
| B5    | numLives   | Current number of lives |
| B6    | player     | Current player number (0 or 1) |
| B7:B8 | p1Score    | Player one score |
| B9:BA | p2Score    | Player two score |
| BB:BC | highScore  | Highest score since power on            |
| BD    | collision | 1 if the player touches a game object |
| BE    | endOfPlayer | Offset to the end of the player's point buffer |
| BF    | origPixel | For collision detection |
| C0    | objCounter | Counter temporary for looping through objects |
| C1    | loopStart | Temporary for noting where player loop starts |
| C2    | transY | Temporary for translating the player's Y coordinate |
| C3    | nontouch | Temporary for counting number of non-overlapping points |
| C4    | numLooped | number of objects currently looped by player |
| C5    | digitColor | number can be printed white on black or black on white |
| C6    | loopScoreCnt | counter for showing the loop score |
| C7    | hasLoopScore | non-zero if there is a loop score to display |
| C8:C9 | loopScoreTmp | sum of scores for objects currently looped by player |
| CA:CB | loopScoreShown | the loop score being shown |
| CC:CD | loopScoreLoc | screen location of the loop score being shown |
| CE    | liveObjCnt | Number of live game objects on the screen |
| CF    | skullCount | number of skulls being shown |
| D0    | totalLoops | total number of loops made in round |
| D1    | nextObjTime | count to wait before making another object |
| D2:D3 | nextFreeObj | next free game object memory slot |
| D4    | cycleCount | used to pace the objects so not all update at once |
| D5    | flashCount | used to time the flashing "one" or "two" during game play |
| D6    | flashType  | used to flash "one" or "two" during game play (FF draws word, 00 draws space) |
| D7    | random     | Random value. Entropy: waits for VBLANK, player's X axis input |
| D8:DD | playerObj  | Player object (for drawing the point) | 
| DE:E3 | eraseObj   | Utility object for erasing points |
| E4:E9 | splashObj  | Utility object for messages and cursive drawing |
| EA:EF | gameObj    | Utility object for the current game object |
| 0160:1FFF | gameObjs | Game objects |
| 0200:02FF | playerLine | Points for the player's line |
| 0380:0390 | pixelMask | Pixel mask table |