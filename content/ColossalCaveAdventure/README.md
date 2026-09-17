![Adventure](adventure.jpg)

# Colossal Cave Adventure

>>> deploy:<br>
>>>    +adventure.jpg<br>
>>>    CodeOrg.md<br>
>>>    DataOrg.md<br>
>>>   ----<br>
>>>    Code350.md<br>
>>>    Data350.md<br>

Should we consider this the first AI halucinations? Might be in Eliza more appropriately.

William Crowther. Born 1936. BS in physics in 1958 from MIT. Working at BBN as a defense contractor. Internet
pioneer in small group developing ARPAnet. Combined his hobbies of DnD and caving to create a "what will you
do next" adventure game based on Mammoth Cave in Kentucky -- particularly the Bedquilt area. He wrote it on the
PDP-10 in 1975 and it spread to other PDP-10s on the early ARPAnet. Players played at teleprinters -- monitors
were rare back then -- connected to the mainframe.

Crowther game is about 700 lines of fortran plus 700 lines of data. Briefly discuss the features.

Enter Don Woods. Born 1954. Working at the Stanford AI Lab (SAIL) contacted Crowther who gave him permission
to enhanceme the original game. 3000 lines of fortran and 1800 lines of data. Discuss features added including
the access control to let admins pick when the game could be played (like in off hours). Woods released his
source code alongside the compiled binary. This is the 350-point version of the game. Other versions over the
years including the 1979 550 point version by David Platt. Crowther and Woods 1995 released their final update
the 430 point version.

Robert Arnstein ported the 350 point version to the Color Computer changing the setting to a Pyramid -- the game:
Pyramid 2000 -- that started a series of adventure games from him. We'll follow the evolution of his game
engine from Pyramid (and Huanted House) to RaakaTu to Bedlam and finally to Xenos.

Plenty of sites out there with interviews, maps, and photographs of the inspiring cave sections. My maps are
based on the code -- not game play. You can see all the available options and chance percentages. The focus
here is on the code and not so much the cultural history.

PDP-10 ... 36 bit machine. 5 characters per memory location (7 bit chars -- 5*7 = 35 bits with left over upper bit).





From the wiki page: 
William Crowther wrote the Colossal Cave Adventure in 1976.

Maps and simulator

Windows playable version: https://en.wikipedia.org/wiki/Colossal_Cave_Adventure

1975 -- William Crowther worked at RTX BBN Technologies  in Cambrige, Massachusetts. His hobbies included
caving and playing D&D. He combined the two to make the Colossal Cave Adventure on the PDP-10 mainframe
at BBN. His cave layout and descriptions are based on his time in Mammoth Cave, Kentucky -- particularly
the Bedquilt area. No explicit title -- simple "WELCOME TO ADVENTURE".

PDP-10 ?no user restrictions ... anyone could access/copy? He took a month vacation and his coworkers 
distributed it to other PDP-10s on the developing ARPANET.

Lots of sites on the web. Pictures of the actual spots in Mamoth Cave. My focus here is the code.

Like D&D, there were treasures to find, but no scoring system -- no ending. You can pick things up and
drop them, but you can't list the things you are carying.

Don Woods contacted Crowther for the source and expanded it to what we call the 350-point version. I'll
show the evolution here.

The Crowther original version created:
  - Grate you can lock/unlock
  - Lamp (you must turn on)
  - Gold Nugget (broken neck if you climb down with it)
  - Snake/bird/box/rod sequence
  - Use the rod to create the bridge
  - Maze
  - Dwarves

Keys, Lamp, Food, Bottle, Cage, Rod, Bird, Nugget, Diamonds, Jewelry, Coins, Silver, Axe

Many online sites to play that reproduce the experience to varying degrees. I found this PC
executable to be faithful:

TODO add others here

https://www.ifarchive.org/if-archive/games/pc/adv_crowther_win.zip

If you "down" in room 7, you go to room 8 like the travel table in the code says. And going "south" from
the swiss cheese room crashes the simulation because of a bug in the original. Discussions on those
shortly.

The fortran code is coupled to the PDP-10. The PDP-10 is a 36-bit machine (12 octal digits -- octal was popular with
DEC in the 1970s ... I have several books on the PDP that all use octal). The "A5" format in fortran for the PDPs
reads/writes 5 6-bit characters from a single 36-bit memory location. The woods expansion uses the leftover upper
sign bit as a marker between messages. Treating a single memory location as a number or a 5-digit string. 



This shows the "down at slit takes you south" proof.

Archive of the crowther fortran:

https://www.ifarchive.org/if-archive/games/source/adv_crowther.zip


Order in data file:

Original:
- 1..8 Surface
- 9..F Entrance
- 10, 14, 15, 16, 17, 18, 19, 1F, 20, 28, 3B, 4F Messages
- 1A NOWHERE
- 11..29 Most of 1st part
- 2A..3A Maze
- 3C..3F Rest of 1st part
- 40..4E 2nd part

Woods:
- 17, 18, 19, 1A, 1F repurposed for plant area
- [2A]    50..57 Additions to maze
- [43,44] 58..5F plant and giant
- [42]    60 Soft room
- [48,48] 61..65 Green light area (emerald, vase)
- [40]    66..69 Oyster
- [40]    6A, 6C Witt's end
- [3D]    6B New maze
- [47]    6D, 6E, 71 Mirror
- [46]    6F Stalactite (more maze entrances)
- [8C]    70 Vending machine
- [54]    72 Pirate's chest
- [--]    73..74 End game
- [48]    75..76 Troll bridge
- [45,4A] 77..79 Dragon
- [75]    7A..82 Volcano/bear
- [6B]    83..8C New maze




Notes made on maps:

The BACK is caught and handled by the code. They are useless here.

For instance, BACK in room 5 travel table executes s300 to either 5 or 6. But the code takes you back to the last room (try coming from 01 and then BACK)

Woods removes the BACK words

Discuss magid words for quick travel

FOOD and WATER don't do anything (Woods will change). No "inventory" system to see what you have. But you can still drop/get.

Demo of how the travel table works with 7.
Show original data and decoded data. Discuss sets
of words. Show how "DOW" for slit is shadowed (Woods fixes this).
Discuss the "You don't fit" room and show that decoded. Woods enhanced the travel info to allow for print and stay. Discuss later.

Dest goto UsedIn         Description
s300 22   RM5            random 50/50 chance of staying in 5 or going to 6
s301 23   RM8            grate: 9 (open) or 23 (closed)
s302 24   RM9            grate: 8 (open) or 9 (closed)
s303 25   RM14           nugget: 15 (not in pack) or 20 (in pack)
s304 26   RM15           nugget: 15 (not in pack) or 22 (in pack)
s305 31   RM17           GAME OVER (probably meant RM21)
s306 27   RM17           bridge: 31 (no) 27 (yes)
s307 28   RM19           snake: 32 (here) 28 (gone)
s308 29   RM19           snake: 32 (here) 29 (gone)
s309 30   RM19           snake: 32 (here) 30 (gone)
s310 33   RM11,12,13,14  grate: 8 (open) or 9 (closed)
s311 34   RM41           random: 80% 65 with message or 20% 68
s312 36   RM41           random: 80% 65 with message or 10% 70 or 10% 39
s313 37   RM42           random: 60% 66 with message or 10% 72 or 30% 71
s314 ?39? RM42           random: 80% 66 with message or 20% 77

From the 350 notes

There are 12 rooms in this maze. 6B and 8C are special rooms. The other 10 are what I'll call "core" rooms as explained below.

Room 8C (the last room in the game) is a dead end with one route back to 70.

Room 6B has the one exit from the maze back to 3D. The other 9 routes from 6B go to a different core room.

Every room has 10 incoming routes (not shown on the map).

Every room has 10 outgoing routes (except 8C, the dead end).

The 10 core rooms are all constructed the same way. One route goes to 70 (next to the dead end). On route goes to 6B. The other 8 routes go to each of the other core rooms.

There is no visual pattern to the layout of the rooms and routes. The verbs appear to be attached to the routes at random. The mapping for each room is shown here.

50 is first "new" room after old 4F. This is the first addition besides the travel table. 

He added three rooms at the beginning of the maze and three at the end. Then two more dead ends -- brings the total to eight.

South from 2A was routed to 2D instead of 2C. The other routes are just word-scrambles in individual rooms. For instance 2F goes to 2D in both, but changed the word to EAST instead of NORTH. Makes it a little more twisty -- a little less aligned to compass points.

Added some u turns in N and S.

The chest room 72 was added later as the game evolved -- probably when the pirate code was born. NE and SE are used in other parts of the cave, but this is the only place a fraction is used in the maze. Very tricky.

34 has a lot of changes, but its just the outgoing routes. The incoming routes from 33, 32, and 37 still point to 34 in the middle. He just swapped the words around in the travel table for 34.

The pyramid map follows this ?exactly?. Woods put the vendening machine for fresh batteries in his 2nd maze. Arnstein moved it to this move at the dead end 52.

Maze entrances are close together

The PLOVER (or emerald) is new to WOODs. POVER teleports you to 64, 
but if you have the emerald, it gets dropped here.

Had a bedquilt -- needed a pillow

301 goto 199-LOC if carying more than emerald
302 drop PLOVER then location
303 troll bridge

Didn't like the CROSS from 0F to 3E. I don't either. Red shows removed

Orig path from 1B to 11 was "BACK" without checking the bridge. In the orig the bridge cannot be retracted. Woods changed that to WAVE

Removed shadowed BACK words

Discuss magid words for quick travel

FOOD and WATER don't do anything (Woods will change). No "inventory" system to see what you have. But you can still drop/get.

Demo of how the travel table works with 7.
Show original data and decoded data. Discuss sets
of words. Show how "DOW" for slit is shadowed (Woods fixes this).
Discuss the "You don't fit" room and show that decoded. Woods enhanced the travel info to allow for print and stay. Discuss later.

woods left the travel table alone here except for the new message features. He fixed the DOWN in 7. Tweaked word list. Pulled BACK.

Rooms 17 and 18 are freed up and used in the plant sequence. Could have freed up 4F, but left it as a room.

Basically the same as Colossal Cave. Migrated the "s10" to the new "check property" ability, but the result is the same. And again, no error message. Could have easily fixed with the new message+go ??TODO make sure??

In original room 9, you can "LOCK" and the grate is locked. But "LOCK GRATE" gets you I see no GRATE here. TODO check this in woods.

Added a return to the ENTRANCE from all rooms.

Freed up 19 for other use ??plant??. Could have freed up 10 and with a little effort -- 14 (change several places). ?? verify
Maybe there is only PRINT AND STAY -- and not PRINT AND GO

You can go DOWN to get out of this area, 
but the only way in is by climbing the plant

Looks like the Troll bridge was added first and the volcano a little later

Order of adds:
- 50..57: 8 rooms to original maze

- 6B: Start of new maze

- 72 priage chest room

Climbing the plant to the giant area makes sense ... like Jack and the Beanstalk

The North/RND/30/60/10 from 66:SwissCheese was moved to Bedquilt. Another NW to 66:SwissCheese for the greenlight area

The new areas plug into the old areas.

You are in the giant room -- another play on words. Pretty much Jack and the Beanstalk and magic hen that lays golden eggs 
(not to be confused with Aseop's Goose).

Neptune wields a trident ... might be related to using the trident in the shell room to open oyster.

# ---------------------------------------------

The data file is read into variables at startup. The file is read one line at a time.
There are 6 sections in the original version (12 in the Woods version).

Sections begin with a line with a single number (1-6) with a section number of 0 marking
the end of the file. Sections end with a negative one. 

Sections:
  1. Long room descriptions 
  2. Short room descriptions
  3. Travel table (how rooms are connected)
  4. List of words
  5. Object descriptions
  6. Messages printed during play

Each section has its own format depending on its function. Sections 1, 2, 5, and 6 are text strings.
Each line has a number number referenced by the FORTRAN code. The rest of the line is the text of
the string. 

Strings can span multiple printed lines as seen in part of section 1 shown here. Each line of text
is a separate line printed on the teletype (or screen). The section begins
with its number "1" -- this is section 1.

## Section 1: Room Descriptions

This section contains the room descriptions. The numbers on the left are the room numbers. Room 1
has three printed lines of text. Line two has three lines. Room 3 is a single line. The last room,
Room 79, has two lines of text. The "-1 END" line marks the end of the section, and section number
2 begins with the next line.

```
1
1	 YOU ARE STANDING AT THE END OF A ROAD BEFORE A SMALL BRICK
1	 BUILDING . AROUND YOU IS A FOREST. A SMALL
1	 STREAM FLOWS OUT OF THE BUILDING AND DOWN A GULLY.
2	 YOU HAVE WALKED UP A HILL, STILL IN THE FOREST
2	 THE ROAD NOW SLOPES BACK DOWN THE OTHER SIDE OF THE HILL.
2	 THERE IS A BUILDING IN THE DISTANCE.
3	 YOU ARE INSIDE A BUILDING, A WELL HOUSE FOR A LARGE SPRING.
4	 YOU ARE IN A VALLEY IN THE FOREST BESIDE A STREAM TUMBLING
4	 ALONG A ROCKY BED.
...
78	 THE CANYON RUNS INTO A MASS OF BOULDERS - DEAD END.
79	 THE STREAM FLOWS OUT THROUGH A PAIR OF 1 FOOT DIAMETER SEWER
79	 PIPES. IT WOULD BE ADVISABLE TO USE THE DOOR.
-1	END
2
1	 YOU'RE AT END OF ROAD AGAIN.
```

## Section 4: Word List

A function number followed by the word. The "function" number is not a unique number for
each word. Instead, the function number is how the word is used by the FORTRAN code. Several
words can be synnonyms of the same function. For instance, ENTER, DOOR, and GATE are all
function 3. The words can be used interchangeably wherever function 3 is used in the code. 

```
4
2	ROAD
3	ENTER
3	DOOR
3	GATE
4	UPSTR
5	DOWNS
...
3051	HELP
3051	?
3051	WHAT
3064	TREE
3066	DIG
3066	EXCIV
3067	BLAST
3068	LOST
3069	MIST
3049	THROW
3079	F---
-1
5
```

The list has one cursor word -- THE word. The mother of all curse words. The F blank blank blank word with function 3079. I have
blurred it out with dashes above. It the code sees this function, it prints "WATCH IT!".

There are a total of 193 recognized words. These are grouped into 113 functions.

Largest group: 12 words for picking up an object "STEAL LAMP" and "GET LAMP" are the same. Code doesn't know the difference.
I wonder why "WHERE" is in this list. "WHERE LAMP" would pick it up.

Notice the words are truncated after 5 character. The code only matches the first 5 characters. Words like "EXCIVate" could be
typed in as "EXCIVblahblahblah". The code stops looking after 5.

TODO ... some examples of commands with different words after 5 commands

"GRATEFULNESS" ... todo

Why? Discuss the 36 bit packing here

Interesting

## Travel Table

Use room 7 as an example. Show room 5. Show the "words" jpg. Woods would enhance this "language" and Arnstein would ...

Reference the "mapOrg.txt" decode.

## Game play

No inventory system in original. You can get/drop things, but you can't get a list of things you have.

The general commands are handled in fortran -- picking things up and dropping them, waving the rod, turning
the lamp on/off.

WEST 10 times (no other direction)

A bug:

```
lamp get
 YOU ARE ALREADY CARRYING IT!
```

Did this get fixed by woods?

Can't go through grate in entrance, but can't open it either. Might run into this using magic words
to teleport. You can go east over the fissure without the bridge. Woods fixes this.
