![Madness and the Minotaur](Madness.jpg)

# Madness and the Minotaur

>>> deploy:<br>
>>>   +Madness.jpg<br>
>>>   +splash.jpg<br>
>>>   +madness.js<br>
>>>   +savegame.js<br>
>>>   +flute.wav<br>
>>>   +inst.cas<br>
>>>   walkthrough:Walk Through<br>
>>>   RAMUse.md<br>
>>>   %Code.md<br>
>>>   ----<br>
>>>   SaveGameViewer.md<br>
>>>   ----<br>
>>>   Journal.md<br>

>>> playMe {

# Play Me! 

Play the game in a CoCo emulator. Click on the splash screen below to open the console and then press any key.

```html
<p>
<img id="splashElement" src="splash.jpg">
<textarea readonly id="madnessConsole" rows="16" style="display:none;background-color: #00FF01; color: black;font-family: monospace;font-size:12px;width:33ch;"></textarea>
</p>

<p>
<button class="btn btn-primary" type="button" data-toggle="collapse" data-target="#cocoTapeArea">Open/Close Virtual Tape</button>
</p>

<div class="collapse" id="cocoTapeArea">
<p>
To access tape functions, enter the QUIET command. Then press one of the following 3 keys:
<ul>
<li>W - Return to game</li>
<li>! - Save game to tape area below</li>
<li>) - Load game from tape area below</li>
</ul>
</p>
<p>
The text area below is the virtual cassette tape. Instead of writing to tape, the emulator writes base64 encoded data 
to this text area.
</p>
</p>
The "!" command will write 2111 bytes to the text box. You must select all the characters (CNTRL-A) and copy 
them (CNTRL-C). Then store them in a text file for later use.
</p>
Before the ")" command you must paste the desired saved-data back into the text area.
</p>
<textarea id="cocoTape" rows="16" style="font-size:8px;width:180ch;" ></textarea>
</div>

```
>>> }

# Walk-Through

Follow along with [My Game](walkthrough) step by step. Open the emulator and save-game viewer and follow along as I win the game.
You have my save-files after every major task. You can jump in to my journey at any point.

# Code Links

* [RAM Usage](RAMUse.md)
* [Disassembled Code](Code.md)

# The Labyrinth of King Minos

"Rumor has it that there are treasures hidden in the vicinity of the Labyrinth.
Are these treasures worth risking life or sanity? If your answer to this question
is negative or you are plagued with skepticism, it is suggested that you re-evaluate
your priorities and establish some healthy materialism." 

> From the game manual introduction

>>> tourGuide {

# Tour Guide

Code bugs are always fun to explore. You should visit these:
* [Error message with POTION](Code.md#code-bug-1)
* [Error when KILL ORACLE](Code.md#code-bug-2)
* [ISHTAR does not clear fog poison](Code.md#code-bug-3)
* [Should fail if overburdeoned](Code.md#code-bug-4)
* [Missing word WATER from message](Code.md#code-bug-5)
* [Shadowed jump](Code.md#code-bug-6)
* [Invisible Oil hides the URN](Code.md#code-bug-7)
* [YOUR SIGHT IS DIM never gets printed (Joe Hagan)](Code.md#code-bug-8)

You should see the routines that [Move each Creature](Code.md#move-creatures) and the
routines that [Make Each Creature Attack](Code.md#creatures-attack).

Have a look at the [Individual User Commands](Code.md#individual-commands) -- especially the
[Spell Commands](Code.md#use-spell).

Check out the routines that run [Between Certain Rooms](Code.md#between-room-actions) and when you [Enter Certain Rooms](Code.md#entering-room-actions).

Read through the text messages of the game:
* [Item Descriptions](Code.md#item-descriptions)
* [Room Descriptions](Code.md#room-descriptions)
* [Game Messages](Code.md#misc-strings)

Here is the map of all the passages between all 256 rooms: [Dungeon Map](Code.md#passage-configuration)
>>> }

# References

For more information on Madness and the Minotaur check out Sean Murphy's wonderful site:<br>
[http://www.figmentfly.com](http://www.figmentfly.com) 

John Layman has translated the 6809 opcodes to x86 to run on a LINUX, BSD, and OSX. Follow his awesome work:<br>
[http://www.frijid.net/madness/madness.html](http://www.frijid.net/madness/madness.html)

# Text Adventure and Real Time Strategy

Madness and the Minotaur is a text adventure game that includes elements of a D&D game and a non-turn-based action game. 
You have "hit points" (physical condition) and you will die when they run out. There are creatures that move from room 
to room once a minute. If you sit still long enough a creature will find you and kill you. Your pack has bulk and weight. 
The more you carry and the lower your hit-points the harder it is for you to jump.

To win the game you have to learn all 8 spells and drop all 16 treasure objects in the forest (room 202). The spells are 
sprinkled around the rooms at random. Some objects are "protected" and require you have a set of other objects to release 
(see below). Some object are "carried" by creatures. Some objects are attached to special room-actions.

# Game Room Geometry 

There are 256 rooms in the game -- 4 floors of 64 rooms each. Each floor is a square grid of 8x8 rooms. Rooms are numbered from 0 
to 255. Room 0 is the upper left of the first floor and room 255 is the lower right of the last floor. Going EAST adds 1 to the 
room number. WEST subtracts one. NORTH subtracts 8. SOUTH adds 8. UP subtracts 64. DOWN adds 64. If the room number becomes less 
than 0 or greater than 255 it "wraps around".

There is a table in the game that defines the "natural" passages between rooms. Most of these passages are two way, but some are one way.
The best way to visualize the large map is with the [save-game viewer](SaveGameViewer.html?BLANK). The lines between the rooms represent directions you can move. 
A line that touches two rooms is a two way passage between the rooms. A broken line between rooms is a one way passage. For instance, 
you can take the passage from room 7 to 6 but not from 6 to 7. This map is NOT randomized between games. The natural passages are the same for all games.

Every room has a single one-sentence description (see the code). There are eight different messages to describe a passage leading from 
a room in any one direction. The game builds the description of passages by selecting a random description for each open direction. Thus 
a room is described a little bit differently every time you see it.

The game keeps a list of "blocked" passages. Randomly (on the average of once every 4 minutes) the ground will begin to shake and three 
passages are blocked somewhere in the dungeon. The game keeps a list of the last 12 rooms it has blocked. It pulls the oldest rooms from 
this list and unblocks them as it blocks new ones. Thus only 12 can be blocked up by the shaking ground and the dungeon doesn't get clogged 
up completely over time. You can use the CROM spell to unblock all passages in a room. If you have the POWERRING in your pack you can walk 
through blocked passages. Otherwise just wait around (with your lamp off to save oil) and the passages will eventually unblock.

The last three rows (40 rooms) of the every floor is the "maze of tunnels stretching in all directions". These behave like normal rooms, but 
they all share the same room description and they all have full connectivity to their neighboring maze rooms. There is also limited entry 
and exit to the maze. Note that all the rooms on the 4th floor (except the treasure room) are a "maze of tunnels" even though the first 5 rows 
are not laid out like the maze.

# Jumps 

There are 24 places in the dungeon where you can jump. The map shows these jump locations and where they go. The map also shows landing 
points for jumps so you can quickly reference back to the starting room. For instance, "j:102" in room 38 means that you can jump into 
room 38 from room 102.

All jumps check your dexterity ... your physical-condition minus the weight of your pack. Each jump has a dexterity requirement to succeed. 
If your dexterity is less than this value you fail, and each jump has its own description of what to do for a failure.

You start the game with the maximum physical condition of 255. The maximum for weight is 255. The maximum for bulk is 255.

A failed jump can end in instant "death". Or a failed jump can end in a "fumble" in which case you actually make the jump but you drop the 
heaviest object you are carrying in the room you jumped from. Or a failed jump can end in a "stumble" where you don't make the jump and you 
take a specific amount of damage. Here is the jump table:

```
3BE1: 8F 80 00 97 6D; From 143 "JUMP PIT"   to 151. Required=128 or DEATH
3BE6: 97 80 80 8F 6D; From 151 "JUMP PIT"   to 143. Required=128 or FUMBLE
3BEB: 10 80 80 11 2C; From 16  "JUMP POOL"  to 17.  Required=128 or FUMBLE
3BF0: 11 80 80 10 2C; From 17  "JUMP POOL"  to 16.  Required=128 or FUMBLE
3BF5: 4E 40 80 56 41; From 78  "JUMP CHASM" to 86.  Required=64  or FUMBLE
3BFA: 56 40 80 4E 41; From 86  "JUMP CHASM" to 78.  Required=64  or FUMBLE
3BFF: 2C 0A 0A B6 6D; From 44  "JUMP PIT"   to 182. Required=10  or STUMBLE(10)
3C04: B6 14 14 2C 6D; From 182 "JUMP PIT"   to 44.  Required=20  or STUMBLE(20)
3C09: A4 A0 00 CA 6D; From 164 "JUMP PIT"   to 202. Required=160 or DEATH
3C0E: 85 C0 80 CB 6D; From 133 "JUMP PIT"   to 203. Required=192 or FUMBLE
3C13: 90 14 14 85 FF; From 144 "JUMP"       to 133. Required=20  or STUMBLE(20)
3C18: CB 80 1E CA 6D; From 203 "JUMP PIT"   to 202. Required=128 or STUMBLE(30)
3C1D: D5 46 14 D4 6B; From 213 "JUMP MIST"  to 212. Required=70  or STUMBLE(20)
3C22: D4 46 14 D5 6B; From 212 "JUMP MIST"  to 213. Required=70  or STUMBLE(20)
3C27: 23 96 28 22 9F; From 35  "JUMP HOLE"  to 34.  Required=150 or STUMBLE(40)
3C2C: 22 78 14 23 6D; From 34  "JUMP PIT"   to 35.  Required=120 or STUMBLE(20)
3C31: 80 64 80 40 05; From 128 "JUMP UP"    to 64.  Required=100 or FUMBLE
3C36: A6 50 80 66 05; From 166 "JUMP UP"    to 102. Required=80  or FUMBLE
3C3B: 66 A0 80 26 05; From 102 "JUMP UP"    to 38.  Required=160 or FUMBLE
3C40: 5C 96 1E 9C 06; From 92  "JUMP DOWN"  to 156. Required=150 or STUMBLE(30)
3C45: 46 50 14 8C 06; From 70  "JUMP DOWN"  to 140. Required=80  or STUMBLE(20)
3C4A: 5E 5A 0A 9E 06; From 94  "JUMP DOWN"  to 158. Required=90  or STUMBLE(10)
3C4F: 40 1E 00 80 6D; From 64  "JUMP PIT"   to 128. Required=30  or DEATH
3C54: CA 1E 14 A2 06; From 202 "JUMP DOWN"  to 162. Required=30  or STUMBLE(20)
;##CodeBug6
; The source for this last jump is set by the code at 0CC7. This jump is given to the
; same room where the RoomEnterAction_203 (SMALL PIT IN CORNER OF ROOM). A JUMP DOWN
; (into the pit) lands you in room 39 -- The Temple of Zeus. REA_203 is placed at
; random anywhere on the 4th floor. The code that reads this table (19AC) only finds
; the first entry in this list for a room. If there is a second jump then it will
; never get discovered. If the RAE_203 is placed in a room with an existing jump then
; the jump to the Temple of Zeus doesn't work.
3C59: 10 8C 80 27 06; From 16  "JUMP DOWN"  to 39.  Required=140 or FUMBLE
```

For instance, the jump description in room 16 says "J:POOL:17:128F". That means you "JUMP POOL" to get to room 17. The jump 
requires a dexterity of 128 and if you fail you "fumble" an object. All of these jumps except the last are NOT randomized. 
They are same every game. The last jump in the table is dynamically assigned to the room with the "SMALL PIT IN THE CORNER". 
If this jump is placed in a room that already has a jump then it is never seen.

# Passage Actions 

There are several passages that have action triggers associated with them. You can see these triggers as letters on the passage 
lines between the rooms. The same triggers are used for multiple passages. Like the passage configurations and the jumps, these 
triggers are NOT randomized. They are the same for every game:

```
;##BetweenRoomA
; If phys minus weight is less than random 64-191 then a climb-up fails.
;##BetweenRoomB
; Most of time this moves us to room 10 ... the start room. But there is a 20% chance that 
; it moves us to a random room 0-F. Either way we tell the game loop to skip moving us
;##BetweenRoomC
; If phys minus weight is less than 192 then a climb-up fails.
;##BetweenRoomD
; If phys minus weight is less than 64 then a climb-up fails.
;##BetweenRoomE
; If phys minus weight is less than 128 then a climb-up fails.
;##BetweenRoomF
; If the lamp is in our pack this moves us to a totally random room.     
;##BetweenRoomG
; There is a 50/50 chance of moving to a random room in the first half of the last floor.
;##BetweenRoomH
; There is a 21/32 chance of going to a random room in the maze on a random floor. We flag the main
; routine to skip movement.
;##BetweenRoomI
; There is a 244 in 255 chance of moving to a random room in the maze on a random floor. 
; We flag the main routine to skip movement.
```

I believe the designers had intended for these to be randomizable. The data table is stored in the area that is saved to tape 
along with the other randomizable things. Also note that action A is applied to the EAST/WEST passage between room 74 and 75. 
But action A specifically checks to see that it is used in an up/down passage or nothing happens. Perhaps these were randomized 
once and then "locked down" in the code.

# Enter-Room Actions 

There are 36 rooms that are given random "enter actions" at the start of the game. There are only 28 different actions - some are
used multiple times. The first 30 action are placed at random. The "room with the music" is also placed at random. The other 5 are fixed.

```
; The first 30 entering-room-actions are placed using this table. The first two
; bytes are the lower and upper bounds of room numbers (inclusive) it can appear.
; The third byte is ANDed with the room number.
; The DF limits the room to the 1st half of the floor (away from the maze).
;
;                Room     Mask  Action
1DE9: 00 7F FF ; 0 - 127   & FF _a
1DEC: 00 7F FF ; 0 - 127   & FF _b
1DEF: 00 7F FF ; 0 - 127   & FF _c
1DF2: C0 FF FF ; 192 - 255 & FF _d
1DF5: C0 FF FF ; 192 - 255 & FF _e
1DF8: 40 7F FF ; 64 - 127  & FF _f1
1DFB: 40 7F DF ; 64 - 127  & DF _g (not maze)
1DFE: 40 7F DF ; 64 - 127  & DF _h (not maze)
1E01: E0 FF DF ; 224 - 255 & DF _i (not maze)
1E04: C0 DF DF ; 192 - 223 & DF _j (not maze)
1E07: A0 BF DF ; 160 - 191 & DF _k (not maze)
1E0A: 80 9F DF ; 128 - 159 & DF _l (not maze)
1E0D: 60 7F DF ; 96 - 127  & DF _m (not maze)
1E10: 40 5F DF ; 64 - 95   & DF _n (not maze)
1E13: 20 3F DF ; 32 - 63   & DF _o (not maze)
1E16: 00 1F DF ; 0 - 31    & DF _p (not maze)
1E19: 00 FF DF ; 0 - 255   & DF _q1 (not maze)
1E1C: 00 7F FF ; 0 - 127   & FF _r
1E1F: 00 FF FF ; 0 - 255   & FF _q2
1E22: 00 FF FF ; 0 - 255   & FF _q3
1E25: 40 BF DF ; 64 - 191  & DF _s (not maze)
1E28: 80 FF FF ; 128 - 255 & FF _t
1E2B: 80 FF FF ; 128 - 255 & FF _q4
1E2E: 00 3F DF ; 0 - 63    & DF _u (not maze)
1E31: 40 FF FF ; 64 - 255  & FF _v
1E34: 80 BF FF ; 128 - 191 & FF _f2
1E37: C0 FF FF ; 192 - 255 & FF _32a  
1E3A: 40 7F FF ; 64 - 127  & FF _x1
1E3D: 80 BF FF ; 128 - 191 & FF _x2
1E40: C0 FF FF ; 192 - 255 & FF _203a (with jump to room 39)
; This room could be placed with room 203b. That would mean that
; there are 2 pits in the same room.
;
; _213
; _32b
; _33
; _203b
; _z (music room that sprite can't go in) Random 16 - 39
; _232
The actions themselves are described below:

; _a Cave in to next floor (32 damage) if pack heavier than 192. If so move a and b to random rooms.
; _b Cave in to next floor (32 damage) if pack heavier than 128. If so move a and b to random rooms.
; _c Cave in to next floor (32 damage) if pack heavier than 95. If so move a and b to random rooms.
; _d If we have VETAR make the pile-of-rocks appear in this room (it stays here).
; _e Play sound effect (same as bb). If we play the flute and have the parchment then the LEDGE appears here.
; _f Powerful gust blows lamp out of grasp. 
;    No lamp in pack ... do nothing. Otherwise:
;    1/2 the time do nothing. The other half:
;    - Take 30 from physical condition
;    - Move the lamp to a neighboring room
;    - Spill 256 seconds of oil from the lamp
;    - Turn the lamp off
;    - Enable VETAR until next move
;    - 1/4th of the time move the handler to a room on level 0,1, or 2
; _g Hydra is here. If it is free it pushes us back to last room. 
; _h If we know VETAR or have the SCEPTER, nothing happens. Otherwise we do command RUN.
; _i Do nothing if we have VETAR. If random number > phys condition or 1/2 the time we RUN and take 5 damage.
; _j Do nothing if we have MITRA. If random number > phys condition or 1/2 the time we RUN and take 5 damage.
; _k Do nothing if we have OKKAN. If random number > phys condition or 1/2 the time we RUN and take 5 damage.
; _l Do nothing if we have AKHIROM. If random number > phys condition or 1/2 the time we RUN and take 5 damage.
; _m Do nothing if we have NERGAL. If random number > phys condition or 1/2 the time we RUN and take 5 damage.
; _n Do nothing if we have BELROG. If random number > phys condition or 1/2 the time we RUN and take 5 damage.
; _o Do nothing if we have CROM. If random number > phys condition or 1/2 the time we RUN and take 5 damage.
; _p Do nothing if we have ISHTAR. If random number > phys condition or 1/2 the time we RUN and take 5 damage.
; _q Start the poison clock (we can't stay here long). 1/3 of the time we give the clock an extra tick.
; _r When we enter this room 3 times the treasure is released.
; _s If we have the lamp and it is off then the room drops its treasure.
;    If the lamp is on we see the walls are a strange color.
; _t If we are holding the packrat's trigger treasure (randomized at start) then the
;    packrat drops his treasure. If the packrat holds his own trigger then he
;    drops it immediately.
; _u If we can see you instantly get the treasure.
; _v Print POOL OF OIL if the pool has oil in it. 
;    There are a limited number of refills (number chosen at init) and 
;    the oil does not appear until we know ISHTAR.
; _x Add 40 to health and move us a short distance away. 10 minutes must pass before again.   
; _z Room with music (init to room 16 to 39). The sprite can't move objects here.
; _32 If we can't see we take 30 damage.
; _33 If we can see you instantly get the treasure.
; _203 Print SMALL PIT IN CORNER OF ROOM.
; _213 Print LAYER OF MIST EAST WALL.
; _232 If we came south to this room and we are carying the pendant then move the 
;      pendant to a random room and move us to (or near) the start.
```

# Objects 

There are 40 objects in the game. 16 of those are treasures. 8 objects are "protected", which requires you to have a combination 
of other objects in your pack in order to pick them up. Once you have released a protected object it remains unprotected the rest 
of the game. The 6 creatures are also "protected". You have to have the combination to kill them.

Every object has a weight and every object has a bulk. In order to pick up an object your combined pack weight (including the new 
object) must be less than your physical condition. The new combined bulk must be less than your physical condition.

Objects are randomly placed using a combination of random ranges, masks, and a table of target rooms. Most objects are placed 
outside the maze. The lamp is placed near the starting point so you don't have to search far for it. Objects that are marked 
PROTECTED are described shortly.

```
; This script controls how objects are placed and how the flags are initialized.
; For range placment the room is ((u-l)&mask)+lower. Table for table placement
; is above. Protection does OR #$10. Invisible object does OR #$01.
; Weights and Bulk values are copied from the table at 354A.
;                   weight Bulk
20D5: 00 00 3F 1F     ; 07 07  FOOD       Random range 0 to 63 mask=1F(1st 4 rows 1st floor)
20D9: 00 00 3F 1F     ; 07 07  BOTTLE     Random range 0 to 63 mask=1F(1st 4 rows 1st floor)
20DD: 00 00 3F 1F     ; 28 14  DAGGER     Random range 0 to 63 mask=1F(1st 4 rows 1st floor)
20E1: 00 80 BF 1F     ; 3C 3C  MACE       Random range 128 to 191 mask=1F(1st 4 rows 1st floor)
20E5: 00 80 BF 1F     ; 3C 3C  AX         Random range 128 to 191 mask=1F(1st 4 rows 1st floor)
20E9: 80              ; 46 28  SWORD      Random location from table AND PROTECTED 
20EA: 03 00 3F DF     ; 3C 32  SHIELD     Random range 0 to 63 mask=DF(1st 4 rows any floor) AND PROTECTED 
20EE: 00 40 7F 1F     ; 1E 14  FLUTE      Random range 64 to 127 mask=1F(1st 4 rows 1st floor)
20F2: 00 80 BF 1F     ; 32 1E  MUSHROOM   Random range 128 to 191 mask=1F(1st 4 rows 1st floor)
20F6: 00 80 BF 1F     ; 1E 28  PENDANT    Random range 128 to 191 mask=1F(1st 4 rows 1st floor)
20FA: 00 C0 FF FF     ; 32 41  SCEPTER    Random range 192 to 255 mask=FF(anywhere)
20FE: 00 00 0C 0B     ; 06 06  LAMP       Random range 0 to 12 mask=0B(early 1st level)
2102: 00 80 BF 1F     ; 14 00  BASKET     Random range 128 to 191 mask=1F(1st 4 rows 1st floor)
2106: 00 C0 FF FF     ; 23 28  PARCHMENT  Random range 192 to 255 mask=FF(anywhere)
210A: 80              ; 2D 32  VIAL       Random location from table AND PROTECTED
210B: 00 40 7F 1F     ; 32 6E  URN        Random range 64 to 127 mask=1F(1st 4 rows 1st floor)
210F: 00 C0 FF FF     ; 28 28  TALISMAN   Random range 192 to 255 mask=FF(anywhere)
2113: 01              ; 28 32  SCROLL     Carried object
2114: 00 C0 FF FF     ; 28 46  GOBLET     Random range 192 to 255 mask=FF(anywhere)
2118: 03 40 7F DF     ; 28 28  SKULL      Random range 64 to 127 mask=DF(1st 4 rows any floor) AND PROTECTED
211C: 01              ; 1E 32  SCARAB     Carried object
211D: 01              ; 1E 46  JEWELBOX   Carried object
211E: 01              ; 32 55  TABLET     Carried object
211F: 00 C0 FF DF     ; 28 3C  ROPE       Random range 192 to 255 mask=DF(1st 4 rows any floor)
2123: 00 00 7F DF     ;        SPRITE     Random range 0 to 127 mask=DF(1st 4 rows any floor)
2127: 00 80 BF 1F     ;        TROGLODYTE Random range 128 to 191 mask=1F(1st 4 rows 1st floor)
212B: 00 40 BF DF     ;        SCORPION   Random range 64 to 191 mask=DF(1st 4 rows any floor)
212F: 00 40 7F 1F     ;        NYMPH      Random range 64 to 127 mask=1F(1st 4 rows 1st floor)
2133: 00 80 BF 1F     ;        SATYR      Random range 128 to 191 mask=1F(1st 4 rows 1st floor)
2137: 00 80 BF 1F     ;        MINOTAUR   Random range 128 to 191 mask=1F(1st 4 rows 1st floor)
213B: 00 00 7F DF     ;        ORACLE     Random range 0 to 127 mask=DF(1st 4 rows any floor)
213F: 01              ; 64 1E  GOLD       (treasure) Carried object
2140: 01              ; 46 32  SILVER     (treasure) Carried object
2141: 01              ; 28 32  DIAMOND    (treasure) Carried object
2142: 03 00 FF FF     ; 46 50  SPELLBOOK  (treasure) Random range 0 to 255 mask=FF(anywhere) AND PROTECTED
2146: 01              ; 28 3C  RUBY       (treasure) Carried object
2147: 01              ; 5A 50  FLEECE     (treasure) Carried object
2148: 01              ; 32 37  TIARA      (treasure) Carried object
2149: 01              ; 3C 28  POWDER     (treasure) Carried object
214A: 01              ; 5A 2D  AMULET     (treasure) Carried object
214B: 01              ; 46 46  POTION     (treasure) Carried object
214C: 03 80 BF DF     ; 5A 5A  POWERRING  (treasure) Random range 128 to 191 mask=DF(1st 4 rows any floor) AND PROTECTED
2150: 80              ; 5A 5A  LIGHTRING  (treasure) Random location from table AND PROTECTED
2151: 80              ; 5A 5A  TRUTHRING  (treasure) Random location from table AND PROTECTED
2152: 01              ; 50 32  CROWN      (treasure) Carried object
2153: 01              ; 28 28  OPAL       (treasure) Carried object
2154: 01              ; 3C 3C  SAPPHIRE   (treasure) Carried object

; 16 different rooms that protected objects may be placed in. It is likely that
; multiple protected objects will be dropped in the same room.
20C5: 64 ; 100
20C6: 96 ; 150          
20C7: 5A ;  90                
20C8: 4D ;  77               
20C9: A2 ; 162
20CA: 10 ;  16       
20CB: 73 ; 115
20CC: 90 ; 144
20CD: 38 ;  56         
20CE: 19 ;  25                         
20CF: 2C ;  44
20D0: 87 ; 135                    
20D1: DE ; 222
20D2: 4F ;  79                      
20D3: 85 ; 133
20D4: 9E ; 158        
```
     
Some of the objects have special abilities:

LAMP - The first 40 rooms of level one and the treasure room (202) are naturally lit. The rest of the rooms need lamp light for you to see. 
You can LAMP ON and LAMP OFF to turn the lamp on and off.

SCARAB - The AKHIROM spell makes you invulnerable for 3 minutes IF you have the scarab in your pack. Once you are invulnerable you will 
see the scarab glowing if you "LOOK SCARAB". At the end of three minutes the scarab moves to a random room.

FOOD - The foods adds 30 to your physical condition (no more than 95). Then the food moves to a random room to be eaten again. 
You can EAT FOOD.

POWDER - If you EAT POWDER then the URN and BOTTLE (fillable things) come to your current room and the POWDER moves to a random room.

MUSHROOM - Most of the time eating the mushroom adds 60 to your physical condition. Then the mushroom moves to a random room. But be 
careful: the mushroom has a 1/32 chance of killing you instantly. Save your game before you eat it. You can EAT MUSHROOM.

BOTTLE - The bottle can be filled up with water in several rooms. Drinking the water from the bottle heals your physical condition by 
32 points and starts a 16 minute timer. You can only heal up by drinking water once every 16 minutes. You can DRINK WATER. The bottle 
starts full of water.

You can also attempt to DRINK SPRITE - a pun on the soda drink. You'll get a "YOU MUST BE JOKING" message.

URN - The urn holds oil to refill the lamp. There is a pool of oil that moves every time you fill from it. You can fill the lamp directly 
from the pool of oil or you can fill the urn from the pool. In fact, the urn will hold four fills. The number of refills in the pool of 
oil is randomized at the start of the game from 4 to 7. You can only see the pool of oil when you know ISHTAR. You can FILL URN or FILL LAMP. 
The URN starts with 4 refills of oils.

FLUTE and PARCHMENT - There is a room in the dungeon (placed at random) that plays music when you enter it. If you PLAY FLUTE and have 
the parchment in your pack a ledge will appear. You climb the ledge with the rope to get the treasure. You can PLAY FLUTE.

ROPE - You need the rope to climb the ledge for its treasure. You also need the rope to tie up the Hydra before stabbing it. You can 
TIE HYDRA and CLIMB LEDGE.

TABLET - If you in room 19 (with the ancient carvings on the wall) you can LOOK TABLET to bring the Oracle to the room. The tablet 
then moves to a random room.

POWERRING - If you have the tablet you can walk through blocked passages. You can also OPEN CRYPT in the "crypt of the ancient king" 
with the powering. Otherwise your physical condition must be greater than 250 to open it.

SCEPTER - In the room with action "_h" you have to know VETRA or have the SCEPTER or you get pushed out.

POTION - If you DRINK POTION you heal by adding 200 to your physical condition and the potion moves to a random room. There is also 
a 7/8 chance of curing the scorpion sting if you have been stung. If fact, this is the only way to cure the scorpion sting so keep it on you until you have killed the scorpion.

There is a bug in the code for "DRINK POTION". If you enter the command but don't have potion you'll see "THE BOTTLE IS EMPTY" - even 
if you don't have the potion or the bottle.

PENDANT - If you are carrying the PENDANT and enter room 232 from the south then you are moved to a random room near the start (room 10) 
and the PENDANT drops in a random room.

SCROLL - If you have the scroll you can OPEN SCROLL anywhere on the 3rd or 4th floor to bring the Troglodyte to you.

JEWLBOX - If you open the JEWLBOX in room 158 (the Minotaur's lair) the Minotaur will appear in the room.

DRAPES - If you OPEN DRAPES in room 9 there is a 1 in 4 chance of opening the passage to the south. You only get one chance at this.

# Protected Objects 

Object marked with a "*" in the table above are protected. You must have a specific set of objects in your pack in order to GET these 
objects. You can have other objects in your pack too, but you must have all of the combo objects. Once you have freed a protected object 
it remains free. You can DROP and GET it back without the specific combo on objects in your pack.

There is potential here for a deadlock. Protected object A could require you to have object B but B might be protected and require you 
have object A. The developers went to great lengths to keep this from happening. Instead of making the trigger-lists at random, they 
created a handful of possible lists for each object. At startup the game picks a random list from the possible lists for each protected object.

The lists were carefully constructed to avoid a deadlock. Here are the possible protected-object requirements for each object:

```
; There are 14 objects in the game that require us to have a combination
; of objects to kill/get. This table lists a number of configurations
; for each of these objects. On initialization, a random list is chosen
; from the possibile lists for each object. 
;
; Note that none of these are treasures, so the game can't be unwinnable because a
; creature carries the object needed to kill it.
;
; These lists are carefully constructed so that we can never have an unwinnable
; game because two objects require one another to get.
1D4D: 1A              ; TROGLODYTE
1D4E: 45 0B 38 80     ;   AX, SCEPTER, MITRA
1D52: 23 7D 80        ;   SPELLBOOK, CROM
1D55: 43 07 3B FF     ;   DAGGER, SHIELD, NERGAL
1D59: 1D              ; SATYR
1D5A: 46 3B 80        ;   SWORD, NERGAL
1D5D: 44 2B 38 80     ;   MACE, LIGHTRING, MITRA
1D61: 23 77 FF        ;   SPELLBOOK, VETAR
1D64: 1E              ; MINOTAUR
1D65: 46 07 2A 80     ;   SWORD, SHIELD, POWERRING
1D69: 44 0F 0B 38 80  ;   MACE, VIAL, SCEPTER, MITRA
1D6E: 45 3B FF        ;   AX, NERGAL
1D71: 1B              ; SCORPION
1D72: 48 3B 80        ;   FLUTE, NERGAL
1D75: 14 3D 80        ;   SKULL, CROM
1D78: 51 2A FF        ;   TALISMAN, POWERRING
1D7B: 1C              ; NYMPH
1D7C: 49 2C 80        ;   MUSHROOM, TRUTHRING
1D7F: 41 0A 80        ;   FOOD, PENDANT
1D82: 48 39 FF        ;   FLUTE, OKKAN
1D85: 19              ; SPRITE
1D86: 54 2A 80        ;   SKULL, POWERRING
1D89: 41 3B 80        ;   FOOD, NERGAL
1D8C: 43 3A FF        ;   DAGGER, AKHIROM
;
1D8F: 06              ; SWORD
1D90: 18 80           ;   ROPE
1D92: 38 80           ;   MITRA
1D94: 0E FF           ;   PARCHMENT
1D96: 0F              ; VIAL
1D97: 09 77 80        ;   MUSHROOM, VETAR
1D9A: 0E 38 80        ;   PARCHMENT, MITRA
1D9D: 11 38 FF        ;   TALISMAN, MITRA
1DA0: 07              ; SHIELD
1DA1: 06 80           ;   SWORD
1DA3: 04 80           ;   MACE
1DA5: 03 FF           ;   DAGGER
1DA7: 14              ; SKULL
1DA8: 11 0A 80        ;   TALISMAN, PENDANT
1DAB: 39 80           ;   OKKAN
1DAD: 0B FF           ;   SCEPTER
1DAF: 2A              ; POWERRING
1DB0: 7C 80           ;   BELROG
1DB2: 07 0B 0E 79 80  ;   SHIELD, SCEPTER, PARCHMENT, OKKAN
1DB7: 07 04 14 78 80  ;   SHIELD, MACE, SKULL, MITRA
1DBC: 07 06 7A FF     ;   SHIELD, SWORD, AKHIROM
1DC0: 2B              ; LIGHTRING
1DC1: 2A 7D 11 80     ;   POWERRING, CROM, TALISMAN
1DC5: 2A 05 39 80     ;   POWERRING, AX, OKKAN
1DC9: 2A 18 7B FF     ;   POWERRING, ROPE, NERGAL
1DCD: 2C              ; TRUTHRING
1DCE: 2B 7D 0D 80     ;   LIGHTRING, CROM, BASKET
1DD2: 2B 05 39 80     ;   LIGHTRING, AX, OKKAN
1DD6: 2B 08 7A FF     ;   LIGHTRING, FLUTE, AKHIROM
1DDA: 23              ; SPELLBOOK
1DDB: 14 08 80        ;   SKULL, FLUTE
1DDE: 0A 7D 80        ;   PENDANT, CROM
1DE1: 09 13 7C 80     ;   MUSHROOM, GOBLET, BELROG
1DE5: 2A 7B FF        ;   POWERRING, NERGAL
1DE8: FF 
```

For instance, to get the POWERRING you might only need to have learned BELROG. Or you might need the SHIELD, SWORD, and AKHIROM. 
The Oracle will tell you (one object at a time) the required objects for each protected item except the SPELLBOOK. You get the combination 
for the SPELLBOOK by "LOOK POOL" in room 0.

# Spells 

The "AIR IS CRACKLING WITH ENCHANTMENT" if you enter a room with a spell (or multiple spells). If you have the right item in your backpack 
you will automatically learn the spell. You have to learn the spells in order. You have to have the MUSHROOM and the FOOD to learn VETAR. 
You have to know VETAR and have the PARCHMENT to learn MITRA. The following table shows what you have to have to learn a spell and the rooms 
that the spells may appear in (random pick between the first and second room number inclusively).

```
3BC1: 09 01 00 00    ; VETRA:   MUSHROOM and FOOD                   
3BC5: 0E 37 00 00    ; MITRA:   PARCHMENT and  VETRA                   
3BC9: 11 38 00 00    ; OKKAN:   TALISMAN and MITRA              
3BCD: 18 39 00 00    ; AKHIROM: ROPE and OKKAN                   
3BD1: 0B 3A 00 00    ; NERGAL:  SCEPTER and AKHIROM               
3BD5: 0F 3B 00 00    ; BELROG:  VIAL and NERGAL               
3BD9: 0A 3C 00 00    ; CROM:    PENDANT and BELROG             
3BDD: 23 3D 00 00    ; ISHTAR:  SPELLBOOK and CROM

; This table describes where a spell can be placed at random. The last 24
; rooms on floors 1-3 and all of 4th floor is the maze (except for exit
; room on 4th floor). The given spell must be placed between the start and
; stop values (inclusive).
1D3D: 00 27 ; VETRA     0 -  39  1st floor (except last 24 rooms ... the maze)
1D3F: 40 67 ; MITRA    64 - 103  2nd floor (except last 24 rooms ... the maze)
1D41: 40 67 ; OKKAN    64 - 103  2nd floor (except last 24 rooms ... the maze)
1D43: 40 67 ; AKHIROM  64 - 103  2nd floor (except last 24 rooms ... the maze)
1D45: 80 A7 ; NERGAL  128 - 167  3rd floor (except last 24 rooms ... the maze) 
1D47: 80 A7 ; BELROG  128 - 167  3rd floor (except last 24 rooms ... the maze)
1D49: 80 FF ; CROM    128 - 255  anywhere on 3rd or 4th floor
1D4B: 80 FF ; ISHTAR  128 - 255  anywhere on 3rd or 4th floor        
```
    
Using a spell costs hit points (physical condition). The more powerful the spell, the more it costs. Here are the details of what they 
cost and what they do:

```
;##CommandVETAR
; Take 10 damage. GET LAMP immediately after it has been blown away. 
; Note the SCROLL can be used to retrieve the lamp on the 4th floor.
;##CommandMITRA
; Take 12 damnage. Remove scorpion sting. 
;##CommandOKKAN
; Take 14 damage. Get treasure from "pile of rocks" if it is here.             
;##CommandAKHIROM      
; Take 16 damage. If SCARAB is in pack, make us invulnerable for 3 minutes. At the 
; end of that if the scarab is in the pack, move it to a random room. So be sure 
; and drop the scarab while you are invulnerable or you'll have to look for it 
; to do it again. Also kill the HYDRA if it is in the room (no SCARAB required).
;##CommandNERGAL
; Take 18 damage. Allows us to stay in poison room.     
;##CommandBELROG          
; Take 20 damage. Make JUMP from this room without failing.
;##CommandCROM
; Take 22 damage. Ublocks all passages.  
;##CommandISHTAR
; Take 24 damage. Move to "exit" point where we drop treasure. This has a limited 
; number of uses (randomized at start to 1-4) so use it wisely.
```

There are several places in the dungeon where the lamp gets blown out of your hands. You can use VETAR on your next turn to get it 
back. If you take a step, VETAR won't work.

ISHTAR moves you to the exit room. At the beginning of the game the number of uses is randomized from 1 to 4. The room with the oil 
in it (to refill the URN or LAMP) will not appear until you know ISHTAR.

# Creatures 

There are six "real" creatures in the game that move around and attack you. The Oracle moves like a creature but gives you advice if 
you ASK ORACLE. Once the oracle gives advice it moves to a random room in the dungeon and continues walking around. The ORACLE starts 
in a random room on the 1st two floors. Once a minute the oracle picks a random direction from its current room and moves to the 
target room. It is not stopped by blocked passages or even missing passages.

There is an interesting bug in the code involving the Oracle. If you KILL ORACLE you will get the message THE URN IS FILLED WITH OIL, 
which doesn't make much sense. Then the oracle moves to a random room.

The Hydra is placed in a random room and caries a treasure. When you try to enter the room with the Hydra it will push you back. As soon 
as it pushes you back you can TIE HYDRA if you have the rope. This binds the Hydra allowing you to enter the room with it. Then you 
STAB HYDRA to kill it. If you have the SWORD in your pack your physical condition must be at least 200 to kill it. If instead you have 
the DAGGER, your physical condition must be at least 240. All other stabs miss. The AKHIROM spell (makes you invulnerable) will also 
kill the Hydra no matter what your condition. When the Hydra dies it drops its treasure and the rope.

At the beginning of the game the packrat is given a random treasure and notes a random treasure to watch for. It is placed in a random 
room. If you enter the room carrying the trigger treasure then the packrat will drop its own treasure for you. If you don't have the 
trigger then the rat runs into hiding. And if the rat happens to be carrying its own trigger? The designers coded for that. If the rat 
is carrying its own trigger it immediately drops the treasure for you.

The six "real" creatures all move once a minute. Once they are in the room with you they go into a second-by-second attack phase 
described below. If you are still alive when the minute tick comes along, the creature moves on.

To kill a creature you use the KILL command: KILL MINOTAR for example. The creatures have combinations-of-objects you must possess 
just like the protected objects in order for the KILL to take them down. If you don't have the right combination you miss and take 
50 damage to your physical condition.

Like the protected objects the creatures have "possible" lists that are chosen at random at the start of the game. The oracle will 
tell you what the combinations are.

## Sprite 

The SPRITE starts in a random room on the 1st two floors (not the maze). Once a minute the SPRITE moves in a random direction. It 
may only move in a valid, unblocked direction. It may not move to the 4th floor except for the treasure room.

When the SPRITE enters a room it moves all objects on the floor to a random room anywhere in the dungeon. To protected dropped objects 
there are some rooms the SPRITE may not go. The SPRITE may not move to the room with the music on the 1st floor (enter-action "_z").

The SPRITE may not move to the room with the VIAL in it (whether the vial is protected or free). Thus you can drop the vial anywhere 
you want to protect them from the SPRITE.

The SPRITE does not attack.

In order to KILL SPRITE, you must have one of the following combinations of objects (the list is chosen at random at the start of the game):

```
1D86: 54 2A 80        ;   SKULL, POWERRING
1D89: 41 3B 80        ;   FOOD, NERGAL
1D8C: 43 3A FF        ;   DAGGER, AKHIROM
```

## Troglodyte 

The TROGLODYTE starts in a random room on the 3rd floor (not the maze). Once a minute the TROGLODYTE moves in a random direction. It may 
only move in a valid, unblocked direction. It may not move to the 4th floor.

If the TROGLODYTE is in the room with you it attacks on a twelve second cycle. The 1st second it has a random chance of hitting with 60 
damage to your physical condition. The chance depends on your room number. In low room numbers (like on the 1st floor) the chance of hitting 
is low. Try to take it on there!

```
1D4E: 45 0B 38 80     ;   AX, SCEPTER, MITRA
1D52: 23 7D 80        ;   SPELLBOOK, CROM
1D55: 43 07 3B FF     ;   DAGGER, SHIELD, NERGAL
```

## Scorpion 

The SCORPION starts in a random room on the 2nd or 3rd floor (not the maze). Once a minute the SCORPTION moves in a random direction. It 
does not check for passages or blocks. It may move to any floor.

If the SCORPION is in a room with attacks on a random second. The attack does one of two things. Half the time it does nothing and the 
SCORPION vanishes for 16 seconds. Other half of the time it increases the sting count. Once stung, you take damage once a minute from the 
accumulated stings at a rate of 5 times number-of-stings to your physical condition. The only cure for the SCORPION sting is the POTION, 
and even it doesn't work 1/8th of the time. If it doesn't work you have to find the POTION and try again before you die.

In order to KILL SCORPION, you must have one of the following combination of objects (the list is chosen at random at the start of the game):

```
1D72: 48 3B 80        ;   FLUTE, NERGAL
1D75: 14 3D 80        ;   SKULL, CROM
1D78: 51 2A FF        ;   TALISMAN, POWERRING
```

## Nymph 

The NYMPH starts in a random room on the 2nd floor (not the maze). Once a minute the NYMPH moves in a random direction. It may only move 
in a valid, unblocked direction. It may move to any floor.

The NYMPH does not attack.

In order to KILL NYMPH, you must have one of the following combination of objects (the list is chosen at random at the start of the game):

```
1D7C: 49 2C 80        ;   MUSHROOM, TRUTHRING
1D7F: 41 0A 80        ;   FOOD, PENDANT
1D82: 48 39 FF        ;   FLUTE, OKKAN
```

## Satyr 

The SATYR starts in a random room on the 3rd floor (not the maze). Once a minute the SATYR moves in a random direction. It may only 
move in a valid, unblocked direction. It may not move to the 1st floor.

If the SATYR is in the room with you it attacks on a 15 second cycle. On the 1st second it attacks with 30 damage to your physical condition.

In order to KILL SATYR, you must have one of the following combination of objects (the list is chosen at random at the start of the game):

```
1D5A: 46 3B 80        ;   SWORD, NERGAL
1D5D: 44 2B 38 80     ;   MACE, LIGHTRING, MITRA
1D61: 23 77 FF        ;   SPELLBOOK, VETAR
```

## Minotaur 

The MINOTAUR starts in a random room on the 3rd floor (not the maze). Once a minute the MINOTAUR moves in a random direction. It may 
only move in a valid, unblocked direction. It may not move to the 1st floor.

If the MINOTAUR is in the room with you it attacks on a ten second cycle. The 1st second it prints "THE MINOTAUR IS HERE". On the 10th 
second it hits with 0 to 70 points of damage to your physical condition.

In order to KILL MINOTAUR you must have one of the following combinations of objects (the list is chosen at random at the start of the game):

```
1D65: 46 07 2A 80     ;   SWORD, SHIELD, POWERRING
1D69: 44 0F 0B 38 80  ;   MACE, VIAL, SCEPTER, MITRA
1D6E: 45 3B FF        ;   AX, NERGAL
```

# Healing 

EAT FOOD adds 30. Food moves to random room.

EAT MUSHROOM adds 60. (1 in 32 chance of killing you.) Mushroom moves to random room.

DRINK POTION adds 200. Potion moves to random room.

DRINK WATER adds 32 (must wait 16 minutes before drinking again).

Entering room with aura adds 40 (must wait 10 minutes before it will heal again). You are moved to a nearby room.

# Getting Treasures 

There are 16 treasure objects you must get to the ground in room 202: GOLD, SILVER, DIAMNOD, SPELLBOOK, RUBY, FLEECE, TIARA, POWDER, 
AMULET, POTION, POWERRING, LIGHTRIGHT, TRUTHRING, CROWN, OPAL, and SAPPHIRE. These are the last 16 objects in the object table above.

Four of these treasures are "protected", and you'll see them as you walk around the dungeon. The other 12 are "carried" and will be 
assigned randomly to the following 17 "containers". There are 4 other carried objects too that are not treasures: SCROLL, SCARAB, JEWELBOX, 
and TABLET. Thus 16 of the 17 containers described next will have an object, but remember not all of them are treasures.

Five of the six moving creatures are given objects. You will have to KILL them: SPRITE, TROGLODYTE, SCORPION, NYMPH, SATYR, and MINOTAUR. 
One of these creatures is chosen to be "empty" when the carried objects are passed out. But it is never the MINOTAUR. Killing the MINOTAUR 
will always produce a reward, though it may not be a treasure.

The "EnterRoomAction_t" is the packrat. It is placed at random on the last 2 floors. You must be carrying the object it wants to see. 
Then it will drop its own object.

The "EnterRoomAction_g" is the HYDRA. It is placed at random outside the maze on the 2nd floor. The HYDRA holds an object. When it pushes 
you back you must immediately "TIE HYDRA" with the rope in your pack. Then you can enter the room with it and STAB HYDRA with the sword or 
dagger in your pack. Or you can kill it with the AKHIROM spell (you must have the SCARAB in your pack).

The "EnterRoomAction_203a" is a "SMALL PIT IN THE CORNER OF THE ROOM". This room is placed at random anywhere on the last floor. If you 
LOOK PIT you will get the object. You may have to look several times as there is a 50/50 chance of seeing it each time.

The "EnterRoomAction_e" is a room with music playing. It is placed at random anywhere on the last floor. If you have the PARCHMENT in your 
pack and PLAY FLUTE then a ledge will appear. If you have the rope in your pack you can CLIMB LEDGE to get the object.

The "EnterRoomAction_d" is a "PILE OF ROCKS". It is placed at random anywhere on the last floor. You will only see the rocks once you have 
learned the VETAR spell. Then the OKKAN spell will get the treasure from the rocks.

The "EnterRoomAction_33" is in room 33. Walk in with the lamp on and get the object.

The "EnterRoomAction_u" has a free object. Walk in with the lamp on and get the object. This action is placed outside the maze on the 
first floor.

The "EnterRoomAction_s" is the room with the eerie glow and strange color walls. It is placed at random outside the maze on the second 
floor. If you LAMP OFF in this room you'll get the object.

The "EnterRoomAction_r" has an object. It is placed at random on the first two floors. The object is "free", but you have to enter the 
room three times for it to be released. There is no way to know when you have entered this room. You just have to drift around until you 
enter it 3 times.

There is a crypt in room 67. If you OPEN CRYPT in this room then the object will fall out. Your physical condition minus your pack-weight 
must be 250 or better. You'll probably have to drop everything before you can open the crypt.

There is a crypt in room 102. If you OPEN CRYPT in this room then the object will fall out. If you have the POWERRING you will 
automatically open it. Otherwise your physical condition minus your pack-bulk must be 250 or better.

# Corrections 

Thanks to Joe Hagan for pointing out some mistakes in the original disassembly (now corrected here and in the code). 
The original comments at 09C5 said the Sprite can't move to the treasure room, but it can. The original comments at 1125 
said that OPEN SCROLL would bring the LAMP to us on the 4th floor. Actually it brings the Troglodyte to us on floors 3 
and 4. And the original comments misinterpreted the VETAR flag. They said the flag temporarily disables VETAR. Actually it 
temporarily enables it.

Joe fixed a couple of typos here and in the Frogger dig.

Joe found a code bug in Madness at 0D51. The message "YOUR SIGHT IS DIM" is stored as a packed string. But the code to print 
it calls "PrintMess" instead of "PrintPacked". The message never appears on the screen. Joe fixed the code and verified it 
in the emulator.

Thanks again, Joe.

# The Save-Game Viewer 

The map and info at the end of this write-up was created by my save-game viewer. Download the code JAR from the "Tools" page on my site 
to your machine and play the game online using the signed-version of the [online Mocha emulator](http://members.cox.net/javacoco/signedmocha.html ). 
The signed version will allow you to save your game to your local machine.

In the emulator's "SETUP" click on "MOUNT LOCAL". When you save your game you will be prompted for a local CAS file. 
Remember to click on MOUNT LOCAL every time you want a new save file. Otherwise your save will be appended to the 
end of the first file.

To run the save-game viewer, enter the following command:

java -classpath TOOLS.JAR ca.madness.SaveGameViewer NAME.CAS
Where "NAME.CAS" is the name of your saved game.

# ZCode Translation (for iPod)

I started working on translating the original source into ZCode for play with Frotz. Frotz is an interpreter for Infocom games 
and other Z-machine games. It compiles for many platforms including Windows and the iPod. You can download Frotz from the 
apple app-store for free and then upload "Madness.z5" to your iPod and play madness on the go.

I abandoned the effort when I realized that JavaScript on a web-site (or in NodeJS) is a better platform than ZCode.

Here is the ZCode as far as I got. Currently you can explore the game's rooms through their natural passages (no jumps). 
The spells, objects, and creatures are placed. The "protected" lists work. You can learn spells and score points. 

[https://github.com/topherCantrell/computerarcheology/tree/master/content/CoCo/MadnessMinotaur/zcode](https://github.com/topherCantrell/computerarcheology/tree/master/content/CoCo/MadnessMinotaur/zcode)

# Cheats 

You type "CLOADM" to load the game. Then you type "EXEC" to run the game. Between these commands you can make patches to the 
code with BASIC POKE commands. Here are some useful cheats:

```
39->1A2F    POKE 6703,57    Invulnerable to damage
21->78D     POKE 1933,33    Lamp doesn't burn oil
21->11CD    POKE 4557,33    ASK ORACLE any time
20->E0E     POKE 3598,32    Move in any direction

12->751(3)  POKE 1873,18    Skip creatures moving
            POKE 1874,18
            POKE 1875,18

12->80B(3)  POKE 2059,18    Skip creatures attacking
            POKE 2060,18
            POKE 2061,18
```

In making the ZCode port I wrote a debug system that loads from virtual tape to memory at 7000. The system allows you to read
 and write any memory location from inside the game. The system hooks into the "EAT" and the "TIE" commands.

The command "EAT 0000" will print the value at memory location 0000 (hex). The command "TIE 0000:50" will set memory 
location 0000 to 50 (hex). The disassembly describes location 0000 as the "current room". This debug command thus allows 
you to set the room number to anything letting you teleport around the dungeon at will.

You load the debug system into memory first with the CLOADM BASIC command. Then you load Madness. 
Then you make 6 pokes to tie the system to the game's commands. As shown in the comments below:

```
; cload (instbas.cas) basic poker
; cloadm (inst.cas) loads debug to 7000
 
;    1253: 7E 70 0D  JMP $700D ; EAT 1234:56         POKE 4691,   126 112 13
;    137D: 7E 70 00  JMP $7000 ; TIE 1234	     POKE 4989,   126 112 0
	 
;doPeek
7000: 8E 05 C4 LDX #05C4
7003: 8D 16    BSR fromhexword
7005: E6 A4    LDB ,Y
7007: BD 17 15 JSR 1715
700A: 7E 10 17 JMP $1017
	 
;doPoke
700D: 8E 05 C4 LDX #05C4         ; Start of 4-digit address on screen
7010: 8D 09    BSR fromhexword   ; Convert to word in Y
7012: A6 80    LDA ,X+           ; Skip the ':' on the screen
7014: 8D 11    BSR fromhexbyte   ; Get the value
7016: A7 A4    STA ,Y            ; Store the value to the address
7018: 7E 10 17 JMP $1017         ; Done with command

;fromHexWord
701B: 8D 0A    BSR fromHexByte   ; Get the left byte  
701D: 97 54    STA >$54          ; Store left byte (used by tape-write)
701F: 8D 06    BSR fromHexByte   ; Get the right byte
7021: 97 55    STA >$55          ; Store right byte
7023: 10 9E 54 LDY >$54          ; Read 16-bit value
7026: 39       RTS               ; Done
	   
;fromHexByte
7027: 8D 0B    BSR fromHexDigit  ; Get the left digit
7029: 48       ASLA              ; Shfit ...
702A: 48       ASLA              ; ... it ...
702B: 48       ASLA              ; ... one ...
702C: 48       ASLA	             ; ... nibble
702D: 97 28    STA >$28          ; Store upper nibble (calculated score)	    
702F: 8D 03    BSR fromHexDigit  ; Get the right digit
7031: 9A 28    ORA >$28          ; OR in the upper nibble
7033: 39       RTS               ; Done
	 
;fromHexDigit:
7034: A6 80    LDA ,X+           ; Get character from screen and bump
7036: 81 70    CMPA #$70         ; '0'
7038: 24 03    BCC isnumber      ; It is a number
703A: 80 37    SUBA #$37         ; It is 'A'-'F' ... subtract 55 ('A' becomes 10)
703C: 39       RTS               ; Done
;isnumber:
703D: 80 70    SUBA #$70         ; '0' becomes 0
703F: 39       RTS               ; Done
```

Here is the virtual COCO tape that contains the debug system: [inst.cas](inst.cas).

```html
<script src="/js/6809.js"></script>
<script src="/js/Binary.js"></script>
<script src="/CoCo/CoCoText.js"></script>
<script src="madness.js"></script>
<script>
    window.onload = function() {
        startMadness();
    }
</script>
```