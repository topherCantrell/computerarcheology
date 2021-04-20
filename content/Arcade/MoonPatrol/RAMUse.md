![RAM](MoonPatrol.jpg)

# RAM Use

>>> memory

| | | |
| --- | --- | --- |
| E001      | SndQueue1            | Sound effects queue buffer |
| E002      | SndQueue2            | Sound effects queue buffer |
| E003      | SndQueue3            | Sound effects queue buffer |
| E004      | SndQueue4            | Sound effects queue buffer |
| E005      | SndQueue5            | Sound effects queue buffer |
| E006      | SndQueue6            | Sound effects queue buffer |
| E007      | SndQueue7            | Sound effects queue buffer |
| E008      | highScore            | 3-byte (6-digit) high-score |
| E009      | highScore1           | 3-byte (6-digit) high-score |
| E00A      | highScore2           | 3-byte (6-digit) high-score |
| E00B      | highPoint            | The passed "point" where high-score was |
| E03C      | mE03C                |  |
| E03E      | slotHisA             | Coin and service-credit switch history for slot A |
| E03F      | slotHisB             | Coin and service-credit switch history for slot B |
| E040      | PerCredit            | Settings: Lives per credit (1,2,3, or 5) |
| E041      | slotModeA            | Settings: Coin mode for slot A |
| E042      | slotModeB            | Settings: Coin mode for slot B |
| E043      | cabMode              | Settings: Cabinet mode 1=UPRIGHT, 0=TABLE |
| E044      | slotMode             | Settings: Slot mode 1=two slots, 0=one slot |
| E045      | extPoints            | Settings: extended points |
| E046      | mE046                | Something that controls sound (and other things). AHHHHH. Demo mode ??! |
| E047      | cntTillCred          | Coin count till credit (when it reaches the magic value the credit goes up) |
| E048      | Credits              | Number of credits in BCD 00 to 99 |
| E049      | mE049                | Current start buttons (active high) |
| E04A      | mE04A                | Current inputs (active high) |
| E04B      | mE04B                | Last inputs (active high) |
| E04C      | flipValue            | Current flip bits value |
| E04D      | mE04D                | Incremented when buggy-held-in-air is done |
| E04E      | isrCNT_1             | Bumped up with every IRQ |
| E04F      | isrCNT_16            | Bumped up every 16 IRQs |
| E050      | isrCount3            | Bumped down every IRQ |
| E051      | isrCount4            | Bumped down every IRQ |
| E052      | mE052                |  |
| E053      | coinStart            | Holds the current value (active high) of D000. Filled in the ISR. |
| E054      | mE054                |  |
| E05F      | mE05F                |  |
| E068      | mE068                |  |
| E094      | mE094                |  |
| E096      | mE096                |  |
| E098      | mE098                |  |
| E0D6      | mE0D6                |  |
| E0D8      | mE0D8                |  |
| E0DA      | mE0DA                |  |
| E0DC      | mE0DC                |  |
| E0E4      | mE0E4                |  |
| E0E6      | mE0E6                |  |
| E0E7      | mE0E7                | Counts command buffers when running them |
| E0E8      | mE0E8                | |
| E0E9      | splashLSB            | Splash screen data cursor LSB |
| E0EA      | splashMSB            | Splash screen data cursor MSB |
| E0EB      | splshObjLSB          | Pointer to screen for splash object LSB |
| E0EC      | splshObjMSB          | Pointer to screen for splash object MSB |
| E0ED      | servCrdCnt           | Every 16 ISRs the service-credit is pressed add one credit |
| E0EE      | mE0EE                |  |
| E0EF      | mE0EF                |  |
| E0F1      | mE0F1                |  |
| E0F3      | mystCnt              | Bumped every ISR if *unused* bit 3 of DS2 is flipped |
| E0F4      | mE0F4                |  |
| E0F6      | mE0F6                |  |
| E0F7      | mE0F7                |  |
| E0F9      | champColors          | If zero then use "beginner" colors. Else use "champ" colors. |

>>>memory

| | | |
| --- | --- | --- |
| E172      | mE172                | |
| E1A2      | mE1A2                | |
| E1A6      | mE1A6                | |
| E1AA      | mE1AA                | |
| E1AE      | mE1AE                | |
| E1C0      | mE1C0                | |
| E1C1      | mE1C1                | |
| E1C2      | mE1C2                | |
| E1C3      | mE1C3                | |
| E1C4      | mE1C4                | |
| E1C5      | mE1C5                | |
| E302      | mE302                | |
| E304      | mE304                | |
| E305      | mE305                | |
| E306      | mE306                | |
| E308      | mE308                | |
| E309      | mE309                | |
| E30A      | mE30A                | |
| E30D      | mE30D                | |
| E30E      | mE30E                | |
| E314      | mE314                | |
| E31A      | mE31A                | |
| E31C      | mE31C                | |
| E320      | mE320                | |
| E322      | mE322                | |
| E323      | mE323                | |
| E327      | mE327                | |
| E32A      | mE32A                | |
| E32D      | mE32D                | |
| E32F      | mE32F                | |
| E372      | mE372                | |


```
E100-E1BF Sprites (48) info copied to hardware by ISR

E100->C840 (0x40 bytes) ?? Enemy rocks and ships
E140->C820 (0x20 bytes) 

E160->C8C0 (0x40 bytes)
E1A0->C8A0 (0x20 bytes) ?? Buggy, wheels, forward shot

E1C0-E1CE also used by ISR ??
```

>>> memory

| | | |
| --- | --- | --- |
| E1CF      | comListHead          | the LSB of the first entry in the wrap-around command list at E600..E6FF |
| E1D0      | comListTail          | the LSB of the next-available slot in the  command list. |
| E1D3      | mE1D3                |  |
| E1D4      | mE1D4                |  |
| E1D5      | mE1D5                |  |
| E1D6      | mE1D6                |  |
| E1D7      | mE1D7                |  |
| E1D8      | mE1D8                |  |
| E1D9      | mE1D9                |  |
| E1DA      | mE1DA                |  |
| E1DC      | mE1DC                |  |
| E1DD      | SndQFront            | Next to pull from the sound queue (MSB is #$E0) |
| E1DE      | SndQBack             | Next to store in sound queue (MSB is #$E0) |
| E1DF      | mE1DF                |  |
| E1E0      | mE1E0                |  |
| E1E1      | mE1E1                |  |
| E1E2      | mE1E2                |  |

>>> memory

| | | |
| --- | --- | --- |
| E300      | buggyHandler         | the current handler routine for the moon buggy |
| E301      | buggyObject          | LSB of sprite object for buggy |
| E303      | buggyX               | X coordinate of the moon buggy |
| E307      | buggyY               | Y coordinate of the moon buggy  +0A ... count-down jump timer in demo |
| E310      | ??Object1??          | |
| E330      | airShot0             | |
| E340      | airShot1             | |
| E350      | airShot2             | |
| E360      | airShot3             | |
| E370      | ??object7??          | |
| E380      | ??object8??          | |
| E390      | ??object9??          | |
| E3A0      | ??objectA??          | |
| E3B0      | ??objectB??          | |
| E3C0      | ??objectC??          | |
| E3D0      | ??objectD??          | |
| E3E0      | ??objectE??          | |
| E3F0      | ??objectF??          | |
| E400      | ??object10??         | |
| E410      | ??object11??         | |
| E420      | ??object12??         | |
| E430      | ??object13??         | |
| E440      | ??object14??         | |
| E450      | ??object15??         | |
| E460      | ??object16??         | |
| E470      | ??object17??         | |
| E480      | ??object18??         | |
| E490      | ??object19??         | |
| E4A0      | ??object1A??         | |
| E4B0      | ??object1B??         | |
| E4C0      | ??object1C??         | |
| E4D0      | ??object1D??         | |
| E4E0      | ??object1E??         | |
| E4F0      | ??object1F??         | |

E500 - E517 is current player

>>> memory

| | | |
| --- | --- | --- |
| E518      | mE518                | |
| E52F      | mE52F                | is other player (swapped at 60A) |
| E500      | curScore             |   Score for current player 3-byte (6-digit) |
| E501      | curScore1            |   Score for current player 3-byte (6-digit) |
| E502      | curScore2            |  Score for current player 3-byte (6-digit) |
| E503      | mE503                | |
| E504      | mE504                | |
| E505      | mE505                | |
| E506      | mE506                | |
| E507      | mE507                | |
| E508      | mE508                | |
| E509      | mE509                | |
| E50A      | mE50A                | |
| E50B      | mE50B                | |
| E50C      | mE50C                | |
| E50D      | mE50D                | |
| E50E      | curPoint             |   Current passed point |
| E50F      | ??E50F??             | cleared when course number is incremented |
| E510      | courseNum            |   Course number (0=beginner, 1.. champion) |
| E511      | mE511                | |
| E512      | mE512                | |
| E513      | mE513                | |
| E514      | mE514                | |
| E515      | mE515                | |
| E516      | mE516                | |
| E517      | mE517                | |
| E518      | othScore             |  Score for "other" player 3-byte (6-digit) |
| E519      | othScore1            |  Score for "other" player 3-byte (6-digit) |
| E51A      | othScore2            |  Score for "other" player 3-byte (6-digit) |
| E51B      | mE51B                | |
| E51C      | mE51C                | |
| E51D      | mE51D                | |
| E51E      | mE51E                | |
| E51F      | mE51F                | |
| E520      | mE520                | |
| E521      | mE521                | |
| E522      | mE522                | |
| E523      | mE523                | |
| E524      | mE524                | |
| E525      | mE525                | |
| E526      | mE526                | |
| E527      | mE527                | |
| E528      | mE528                | |
| E529      | mE529                | |
| E52A      | mE52A                | |
| E52B      | mE52B                | |
| E52C      | mE52C                | |
| E52D      | mE52D                | |
| E52E      | mE52E                | |
| E52F      | mE52F                | |

>>> memory

| | | |
| --- | --- | --- |
| E700      | mE700                |  |
| E701      | menuRow              | The current main menu row number (3-8) |
| E702      | keyValue             | During up/down in menu ... the input value that triggered delta | 
| E703      | stopRow              | During up/down in menu ... stop value for delta (3 or 8) |
| E704      | rowDelta             | During up/down in menu ... row delta (1 or -1) |
| E705      | sndNumber            | Current row number in sound menu |
| E706      | sndLastRow           | Last row in sound menu (14) |
| E707      | sndFirstRow          | First row in sound menu (1) |
| E708      | sndValue             |  During snd left/right ... the input value that triggered delta |
| E709      | sndStop              | During snd left/right ... the stop value for delta (1 or 14) |
| E80A      | sndDelta             | During snd left/right ... row delta (1 or -1) |
| E70B      | sndTable             | Table of offsets to sounds in sound menu |
| E70C      | UN_E70C              | Unused |
| E70D      | isrCntM              | MSB of 4-digit BCD ISR counter |
| E70E      | isrCntL              | LSB of 4-digit BCD ISR counter |
| E70F      | isrCVal              | Current value of upper 2 bits of ISR (changes every 1.1 secs) |
| E710      | lrButtons            | L/R buttons toggle bits for debouncing |
| E711      | startButtons         | Start buttons toggle bits for debouncing |
| E712      | colorScreen          | Number of color-screen in the color menu |

Stack builds down from end of RAM (E800)

E000-E6FF is cleared at startup. Stack is probably reserved from E700-E800. That's huge.
I captured RAM access for a typical run through MAME and found the stack builds down
to E7E0. It has a long way to go still!

```
E000     Sound effects queue buffer

These are read once at power-up

>011E bit 0 clear
>01D4 00
>0567 80 or 90
>0609 toggle bit 3 (swap players)
>0C7F bit 0 set
>27C0 bit 0 cleared

  0  1=run game objects in ISR in game mode, 0=skip @00F2
  1  1=skip pause cheat, 0=check pause cheat in ISR (00AB) and (00DD) >0104
  2   @00E7
  3  0=player 1's game, 1=player 2's game @015D @061C @0D41
  4  0=single player, 1 = multi ?? @0136 @0153 @0CF6
  5
  6
  7 1=??Demo mode??   1=don't register score @062C, @00D9, @047A, @062C @0D76
```

There are 32 objects that are processed with each ISR interrupt. All 32 are processed
every ISR. Each object is a 16 byte structure. The first byte selects the code to run
for the object when the ISR fires. This value is an offset in a jump table with 1 being 
the first entry. A value of 0 means do nothing (the object is inactive or available).

Unlike the "text" objects processed in the main-loop, these objects are fixed. Object 0
is always the moon-buggy. Object 2 is always the player's forward shot. Objects 3..6
are always the four player-air-shots.

```
E300 ISRobjects   Start of ISR game object structures
 E300 ... E4FF 32 object slots (16 bytes each)

   00 Command number to execute (0 means none)
   01 LSB of object pointer E1xx (4 bytes each)
   02
   03 X coordinate
   05
   06
   07 Y coordinate
   08
   09
   0A count-down timer (number of movements for forward shot)
   0B
   0C
   0D
   0E
   0F
```

```
E600..E6FF contains a list of ??text??game commands to execute.
E1CF contains the LSB of the first command.
E1D0 contains the LSB of the next-available command.
The loop at 0283 starts with the pointer E1CF and runs commands until
it reaches E1D0 (the list wraps back around as the LSB wraps). 

The code at 02C2 adds new commands to the list. There is no checking to
see if the list overflows.

The code at 029C advances the list's "head" over an inactive command. All
commands eventually become inactive thus they eventually all get removed
from the front of the list.

The format of these commands:
  00 Command number (00=none)
  01 ?? ISR value for next execution (@0325) --
  02 Text script LSB
  03 Text script MSB
```

