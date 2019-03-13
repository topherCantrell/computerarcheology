![RAM](Madness.jpg)

# RAM Use

Init clears 00-66 inclusive. The area is in BASIC's memory usage. The code uses some of
BASIC's routines, but this first area of memory is for the BASIC interpreter. The code
can overwrite this area without interfering with the BASIC calls it uses. 

>>> memory

| | | |
| --- | --- | --- |
| 00       | curRoom          | current room |
| 01       | lastRoom         | last room |
| 02       | dirBits          | direction command bit pattern |
| 03       | inpLen           | length of user input |
| 04       | weight           | weight of pack |
| 05       | condition        | physical condition |
| 06       | bulk             | bulk of pack |
| 07       | nounObjNum       | decoded object number from noun |
| 08       | fallOdds         | Accumulated odds of falling (0, 1/8, 2/8, 3/8 ... with each step in the dark) |
| 09       | stingCount       | Scorpion sting (0=not, not-zero=number of times) |
| 0A       | lampOn           | 0 if lamp is off, not 0 is on |
| 0B       | spacesOnEnd      | Count of spaces at the end of the row in print routine |
| 0C       | downFail         | Set by BetweenRoomACDE if a climb-down failed ... abort the movement |
| 0D       | pushedBack       | pushed back flag (nobody reads this) |
| 0E       | hydraStatus      | HydraStatus: AA = tied up, 1 = dead, 0 = free |
| 0F       | hydraPushed      | HydraPushedUsBack (must be set to TIE HYDRA)  0 = not, 1 = hydra blocked last move (cleared every direction command) |
| 10       | rocksMoved       | 1 if "pile of rocks" has been moved to us |
| 11       | rocksExposed     | 1 if "pile of rocks" has been exposed with OKKAN |
| 12       | drapesOpen       | 1 if south passage in room 9 is open. 0 if closed. (open with drapes) |
| 13       | auraTimer        | Count down timer until we can walk through aura and heal again (10 seconds each time) |
| 14       | lampStripped     | 1 if lamp has been blown from pack by entering room routine or failed jump |
| 15       | treas0BReleased  | 1 if treasure "$0B" has been released |
| 16       | m16              | NEVER USED |
| 17       | randPass         | Random number for passage-description printing |
| 18:19    | randPoint        | Rolling pointer to BASIC rom for random numbers |
| 1A       | numAdviceGiven   | Number of times advice has been given 0-13 |


Oracle advice table. Object number is stored here. Upper bit set if advice has already been given for this
protected object.

>>> memory

| | | |
| --- | --- | --- |
| 1B       | m1B     | Oracle advice object 0  |
| 1C       | m1C     | Oracle advice object 1  |
| 1D       | m1D     | Oracle advice object 2  |
| 1E       | m1E     | Oracle advice object 3  | 
| 1F       | m1F     | Oracle advice object 4  |
| 20       | m20     | Oracle advice object 5  |
| 21       | m21     | Oracle advice object 6  |
| 22       | m22     | Oracle advice object 7  |
| 23       | m23     | Oracle advice object 8  |
| 24       | m24     | Oracle advice object 9  |
| 25       | m25     | Oracle advice object 10 |
| 26       | m26     | Oracle advice object 11 |
| 27       | m27     | Oracle advice object 12 |


>>> memory

| | | |
| --- | --- | --- |
| 28       | score            | Calculated score |
| 29       | m29                 | NEVER USED |
| 2A       | verbNum          | Verb command number |
| 2B       | nounNum          | Noun word number |
| 2C       | ratObject        | Trigger object to make packrat drop treasure |
| 2D       | m2D                 | NEVER USED |
| 2E       | holderACDE       | Holder value for BetweenRoomACDE |
| 2F       | temporary        | General use lots of places |
| 30       | m30                 | Used in InPack |
| 31       | m31                 | Used in InPack |
| 32       | enteredFog       | Set by EnteringRoomAction_q (MYSTERIOUS FOG) |
| 33       | hydraRoom        | Current room of HYDRA |
| 34       | ishtarUses       | Number of times more ISHTAR can be used. Random init to 1-4. |
| 35       | smallPitRoom     | Room for small pit in corner of room |
| 36       | ledgeRoom        | Room of LEDGE |
| 37       | rocksRoom        | Room of "pile of rocks" (OKKAN spell) |
| 38:39    | lampOil          | Oil level of lamp (0 is empty) |
| 3A       | lampFills        | Number of times lamp can be filled (init to $34 + 4) |
| 3B:3C    | m3B                 | Pointer to start of input on screen |
| 3D       | m3D                 | Used in Random-between-0-and-B |
| 3E       | drinkTimer       | Time until we can drink from bottle to heal again (16 seconds) |
| 3F       | ticksTillSec     | Interrupt divisor count (60 ticks till one seconds) |
| 40       | secsTillMin      | Interrupt divisor count (60 ticks till one minute) |
| 41       | minotaurTimer    | Minotaur state timer |
| 42       | trogTimer        | Troglodyte state timer |
| 43       | satyrTimer       | Satyr state timer |
| 44       | scorpTimer       | Scorpion state timer |
| 45       | fogClock         | Fog clock runs in room MYSTERIOUS FOG. At 6 seconds we get warned. At 10 we die. |
| 46       | akhiromMins      | Minutes of immunity left (AKHIROM gives 3 minutes) |
| 47       | enterRcount      | Count of times entering room with EnteringRoomAction_r. 3 times and treasure drops. |
| 48       | m48                 | NEVER USED |
| 49       | m49                 | NEVER USED |
| 4A:4B    | seconds          | Continual second counter (nobody uses it) |
| 4C:4D    | secsInRoom       | Counts the time in a room. Once 15, no going BACK |
| 4E       | m4E                 | NEVER USED |
| 4F       | m4F                 | NEVER USED |
| 50       | m50                 | NEVER USED |
| 51       | m51                 | Used in Oracle advice |
| 52       | m52                 | Used in killing Hydra |
| 53       | m53                 | Used in sound effects |
| 54:55    | m54                 | Used in tape-write |
| 56:65    | m56                 | 16 byte buffer for decode and auto-word wrap |
| 66       | m66                 | NEVER USED |


This area of BASIC's memory includes tape and cursor information
that the ROM calls use.

>>> memory

| | | |
| --- | --- | --- |
| 67:87    | m67          | BASIC vars |
| 88:89    | scrCursor | Screen cursor |
| 8A:8B    | zeroWord  | BASIC always 0 |
| 8C:F3    | m8C          | BASIC vars |

# Blocked Rooms 

Shifting buffer of rooms blocked by Shaking Ground.
As new rooms are blocked at random, they go on the
end of the list. Rooms are pulled off of the front
of the list and unblocked completely. This keeps
lots of shaking from blocking up the floors over
time.

>>> memory

| | | |
| --- | --- | --- |
| F3:FF     | blkRooms   | Blocked rooms (in BASIC's "unused variables" section) |

# Random Number Seeds

>>> memory

| | | |
| --- | --- | --- |
| 0186:018D | seeds | Random-number bytes (in BASIC's extension vectors) |


# Stack

>>> memory

| | | |
| --- | --- | --- |
| 01FF   | stack  | Stack builds towards 0 (in BASIC's cassette file data buffer) |


# Screen Memory

>>> memory

| | | |
| --- | --- | --- |
| 0200:03FF | | Screen 0 (in some buffers used by BASIC) |
| 0400:05FF | | Screen 1 |

# Game code 

>>> memory

| | | |
| --- | --- | --- |
| 0300:3EB7 | | Game loads from tape |

# Blocked Passages

>>> memory

| | | |
| --- | --- | --- |
| 3EB8:3FB7 | | Block passage table |


# Protected Objects Lists

>>> memory

| | | |
| --- | --- | --- |
| 3FB8:3FFF | | Protected object lists |

