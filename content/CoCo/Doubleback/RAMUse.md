![Doubleback Usage](doubleback.jpg)

# Doubleback RAM Usage

The game works with 4K of RAM, which means it only uses one
screen buffer.

Stack builds to lower from 0150.

Screen uses 0400 to 1000.

>>> memory
|    |      |     |
| -------- | ------- | ----------------- |
| B4        | NumPlayers | 0 for ONE PLAYER, 1 for TWO PLAYER |
| B5        | NumLives | Current number of lives |
| B6        | Player | Current player number (0 or 1) |
| B7:B8     | P1Score | Player one score |
| B9:BA     | P2Score | Player two score |
| BB:BC     | HighScore  | Highest score since power on            |
| BD | BD | |
| BE | BE | |
| BF | BF | |
| C0 | C0 | |
| C1 | C1 | |
| C2 | C2 | |
| C3 | C3 | |
| C4 | C4 | |
| C5 | C5 | |
| C6 | C6 | |
| C7 | C7 | |
| C8 | C8 | |
| C9 | C9 | |
| CA | CA | |
| CB | CB | |
| CC | CC | |
| CD | CD | |
| CE | CE | |
| CF | CF | |
| D0 | D0 | |
| D1 | D1 | |
| D2 | D2 | |
| D3 | D3 | |
| D4 | D4 | |
| D5 | D5 | |
| D6 | D6 | |
| D7 | Random | Random value. Entropy: waits for VBLANK, player's X axis input |
| 0380:0390 | PixelMask | Pixel mask table |