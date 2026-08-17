# The Clam/Sarcophagus

In Colossal, you needed the jewel encrusted trident to open the oyster (clam). In Pyramid it is a jewel encrusted
key.  Sarcophagus were not indended to be open. The message says you have nothing strong enough to open the clam.
The message persists in Pyramid, but using a key isn't a matter of strength. Trident, sea, clam oyster, pearl. 
Makes sense in a cave.

# Treasures WITH the chest

# Bear in Room

# Map

Did Crowther have a grid? It looks like a 13*6 grid? Do some work here. There are lots and lots of maps on the web, 
but mine is based on the code.

# Missing GOTO number

Original was meant for a teleprinter ... not a monitor -- from a mainframe

# Travel table

The first few rooms of the game recognize lots of words. In addition to the compass, you can "BUILDing", "STREAm", "FORESt",
"DEPREssion". The words "BACK" and "RETREat" and "RETURn" are all synnonyms. The game treats them all as the same word.

The travel table allows multiple groups of words to be tied to a destination. For instance, from the first room, there are 4
groups of words to get to the well house: "03 <--- ['ENTER', 'DOOR', 'GATE'], ['BUILD', 'BLD', 'HOUSE'], ['INWAR', 'INSID', 'IN'], ['EAST', 'E']"

I've shown the complete list of words for rooms 5 and 6. The remainder of the map shows the compass points (without the words) and other words
that have direction.

There are two magic words "XYZZY" and "PLUGH" that transport between key locations. Woods added "Y2" to that -- Y2 being a large rock room.

See the mapOrg.txt for complete paths.

A word entry of "1" in the table means the code immediately moves to the target room without prompting the user for a command.
This is used for error messages. Like in room 07 if you type "SLIT" (trying to squeeze into the slit), the travel table takes
you to room 18, whose description is "YOU DON'T FIT THROUGH ...". Room 18 has a "1" destination of 07 that takes you back to
room 07. Woods improved the travel specs to allow for message-then-room without consuming an intermediate room.

The last room of the game is an error message for room 3 well house (you don't fit in sewer pipes). I bet this was added last after several
players kept trying to get into the sewer.

In the original, room 19 is a "YOU DON'T FIT" that dumps back into room 9. The goto3 and maybe ?goto11? should target this room instead
of room 9 so the user sees the error. But nobody references room 19. Woods fixed room 9 to print the message. But not the other
"DEPRESSION" commands. In the original, these "DEPRESSION" would return to room 8 if the grate is open OR back to room 9
confusingly. I might have kept the user in the same room, which would have required several different GOTOs. Woods preserved the
travel-to-9 behavior. Better wording on all this.

```
08       prop(3) NOT 0 ['OUT', 'OUTSI', 'EXIT', 'LEAVE'], ['UPWAR', 'UP', 'U', 'ABOVE', 'ASCEN'] 
mesg_93  else ['OUT', 'OUTSI', 'EXIT', 'LEAVE'] YOU CAN'T GO THROUGH A LOCKED STEEL GRATE!
0A       <--- ['CRAWL'], ['COBBL'], ['INWAR', 'INSID', 'IN'], ['WEST', 'W'] 
```

Talk about prop checks and "goto". Woods extended the specs: (TODO show the org list and woods list).

The original invokes 15 different "goto" code checks. "Goto1" is the 50/50 "north" path from room 5 (half the time you
go to 06 valley road and half you stay put).

List of GOTOs

```
	IL=L-300+1
	GOTO(22,23,24,25,26,31,27,28,29,30,33,34,36,37)IL
	GOTO 2

22	L=6
	IF(RAN(QZ).GT.0.5) L=5
	GOTO 2
23	L=23
	IF(PROP(GRATE).NE.0) L=9
	GOTO 2
24	L=9
	IF(PROP(GRATE).NE.0)L=8
	GOTO 2
```

changing terminology to "s300" instead of "goto1"

Map    label desc
s300   35   function

The second line there is a "computed goto" that would be dropped in mondern versions of fortran. L is the value of the
travel destination. If this were <300, then it would be a room number. Anything greater than a 300 is a goto. Subtract
300 and add one. 300 is goto1, 301 is goto2:

A value of 300 is goto1 which ends up on label 22. L (the next room to go to) is 5 or 6 depending on the random value.

A value of 301 maps to label 23. The next room is 23 or 9. 23 if the gate is locked (property 0). 23 is the "GATE IS LOCKED"
room that returns to room 8. Room 9 is the room beyond the open gate.

```
5      4    9  43  30
5      300  6  7   8   45
5      5    44 46
```

Talk through this above example. List of GOTOs.

Look at room 42 (decimal 66) -- the Swidss Cheese room.

```
66     313  45
66     65   60
66     67   44
66     77   25
66     314  46
```

The first entry is NORTH->goto314 (313-300+1=15). Here is the code for that:

```
37	L=66
	IF(RAN(QZ).GT.0.4)GOTO 38
	L=71
	IF(RAN(QZ).GT.0.25)L=72
	GOTO 2
```

But value 314 = goto15. There isn't a 15th entry in the goto list. There IS a 15th
routine that is coded for room 66 (similar to 314). But "39" isn't on the end of the
list.

The intention was for NORTH and SOUTH to be random. FORTRAN treats an out of range value as a do-nothing
and the code falls through to the next line, which returns to the main loop. The player remains in the
room with no message that anything did or didn't happen. I think this is a bug in the code.

The woods version of code corrects this bug adding the random sequence to SOUTH as intended.

```
39	L=66
	IF(RAN(QZ).GT.0.2)GOTO 38
	L=77
	GOTO 2
```

Complex random sequence ending in room ??% 66 with message, ??%71, or ??%%72.


The last entry is SOUTH->goto315 (314-300+1=15)

Talk through the room 5 RND. example.

Lowercase blue objects are fixed -- game use. Like the grate that can be opened or the bridge or snake.
Other objects can be picked up like the keys and lamp and bird and cage. Some objects, like the BIRD,
are needed in the cave. The BIRD drives the snake away. The food and water serve no purpose in the original.
Woods added a score system and gave points to the treasures. You also get points for visiting deep into
the cave.

TODO whole section on score

