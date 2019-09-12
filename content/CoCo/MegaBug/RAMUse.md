![RAM](megabug.jpg)

# Game variables DP=??

>>> memory
| | | |
| ----  | ---- | ---- |
| 80:81 | Note1 | Tone value for note 1 |
| 82:83 | Note2 | Tone value for note 2 |
| 84:85 | NoteC1 | Note1 tally count |
| 86:87 | NoteC2 | Note2 tally count ||
| AB:AC | ?AB? | |
| AD    | ?AD? | |
| AE    | ?AE? | |
| 92    | RequestedPage | Upper byte of address of visible screen page (04 or ??) |
| 9A:9B | ?ScreenPointerA | |
| 9C:9D | ?ScreenPointerB | |
| C2    | JoyOrKey | FF if player is using joystick or 00 if player is using keyboard |
| C5    | ??AtBoot??    | set to 8 normally or $10 if ENTER pressed at start |
| C7    | VisiblePage   | Upper byte of address of visible screen page (04 or ??) |

Graphics pages (3K each)
  * 0400 - 0FFF
  * 1000 - 1BFF
  * 1C00 - 27FF