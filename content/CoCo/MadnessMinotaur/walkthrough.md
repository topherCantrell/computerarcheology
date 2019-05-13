![Madness and the Minotaur](Madness.jpg)

# Walk-Through of my Game 

This is the description of my game experience played using the saved-game info below. 
Open the [Emulator on the Main Page](index.html) in a new tab and you can play along with 
my game. Use the save-game files after every task. Have a look at the labyrinth with the
save-vile viewer after every task.


## General Strategy
Hard to find your way around. No random movements (move to maze). 240 points max.

Forest treasure room is on the same floor with the maze but not connected to it. Just a convienient
way to make it UP from start.

TODO In and out of the maze. Can't carry everything around because you have to jump.

Entrance to maze: 
  * 1way 1st floor 34 south
  * 1way 3rd floor 161, 162, 163, 164, 165 (all south)
  * 2way passage action H 3rd floor 167 and 175 (north/south)
  * 2way 3rd floor 191 and 192 (east/west)
  
Exit from maze:
  * 1way 2nd floor passage action H from 105 north to 97
  * 1way 4th floor 235 north to 227
  * 2way passage action H 3rd floor 167 and 175 (north/south)
  * 2way 3rd floor 191 and 192 (east/west)

Fully connected except the lower right and upper left and edges along the top and bottom.

Action I east/west between 104 and 105 and 105 and 106.
Action I east/west between 174 and 175 and 175 and 176



Must JUMP in places, which means your condition must be good. Getting one item at a
time to make jumping easier. Pushing through rooms that push you back.

random walls blocking. might be different for you. might have to wait it out.

  * Spells: 8*10 Learned
  * Treasures: 16*10 Dropped at entrance
  
start.cas

## Task 1: Learn VETAR

We have to have the LAMP (room 1) to see on lower levels. The LAMP is in the room
with "_o", which pushes us back at random if we don't have CROM. Every time we
get pushed, it's 5 points of damage. Nothing to it but to keep trying WEST into
the room with lamp.

We need the FOOD (room 14) and the MUSHROOM (room 141). We start in room 10.

```

; We need the lamp for other floors
;
NORTH    ; Room 2 "GUARD ROOM" 
WEST*    ; Room 1 "EMPTY ROOM". You might get pushed back by "_o" trying to get into this room. Keep trying.
GET LAMP
LAMP ON

; Down to the mushroom
;
EAST SOUTH       ; Back to start Room 10
WEST WEST NORTH  ; Room 0 "STONE TOWER"
DOWN             ; Room 64 "GREAT PIT"
;
EAST SOUTH WEST SOUTH SOUTH                 ; Room 88 "MUSTY, CORRIDOR" (the "_q" poison is here ... keep moving)
SOUTH EAST EAST EAST NORTH NORTH EAST SOUTH ; Room 92 "WIDE ROOM" (*SKULL)
JUMP DOWN                                   ; Room 156 "CAVERN, BONES"
;
EAST          ; Room 157 "TWISTING, WINDING" (MACE) 
NORTH*        ; Room 149 "NARROW WINDING". You might get pushed back by "_k". Keep trying and you'll get through.
NORTH         ; Room 141 "NARROW TWISTING" (MUSHROOM)
GET MUSHROOM

; Back up to the food and VETRA
;
SOUTH*               ; Room 149 "NARROW WINDING". You might get pushed back by "_k". Keep trying and you'll get through. 
SOUTH WEST           ; Room 156 "CAVERN, BONES". (You need to be light and healthy to make this climb.)
UP                   ; Room 92 "WIDE ROOM" (*SKULL)
NORTH WEST UP        ; Room 19 "ANCIENT CARVINGS"
EAST NORTH EAST EAST ; Room 14 "BED ROOM" (FOOD, DAGGER)
GET FOOD
WEST NORTH WEST WEST ; Room 3 "PILE OF BONES" (VETRA)
; We now know VETRA
WEST SOUTH           ; Room 10 "TABLE AND CHAIR"
DROP FOOD 
DROP MUSHROOM

SCORE ; points=10 (out of 240), condition=251 (out of 255)

QUIET ; Saved as "after_1.cas"
```

## Task 2: Learn MITRA

Getting pushed will drain your health. So will the poison fog in Room 88 "MUSTY, CORRIDOR". So will a creature
if you got attacked on that run! You can EAT FOOD at this point and/or EAT MUSHROOM to restore your health.

It would be nice to pick up several objects at once, but that makes jumping much more likely to fail. Instead
we'll make several loops getting one object at a time. Next up is the PARCHMENT Room 206 "Maze".

```
UP ; Room 202 "GREAT FORREST" Treasure room
JUMP DOWN ; Room 162 "STONE CROSS" (*LIGHTRING)
SOUTH ; Room 70 "MAZE"
DOWN EAST NORTH ; Room 227 "MAZE". It says "maze", but we are really out.
;
EAST EAST EAST EAST EAST ; Room 231 "MAZE"
NORTH NORTH NORTH NORTH ; Room 199 "MAZE"
WEST SOUTH ; Room 206 "MAZE" (PARCHMENT)
GET PARCHMENT
;
NORTH EAST SOUTH SOUTH WEST WEST ; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
NORTH WEST ; Room 203 "MAZE"
JUMP PIT ; Room 202 "GREAT FOREST" Treasure room
;
; Now back to the 2nd floor for MITRA 
DOWN ; Room 10 "TABLE AND CHAIR" start
;
WEST WEST NORTH DOWN ; 64 great pit
EAST SOUTH WEST SOUTH SOUTH SOUTH ; Room 96 "MUSTY PASSAGE" (OKKAN)
EAST EAST ; Room 96 "BROKEN PASSAGE" now  know MITRA

DROP PARCHMENT 

SCORE ; points=20 (out of 240), condition=251 (out of 255)

QUIET ; save as after_2.cas
```

## Task 3: Learn OKKAN

TODO DOWN FROM 10 might land you in a random room. Make your way back to start.

```
WEST DOWN ; Room 161 "LARGE STONE"
SOUTH DOWN SOUTH ; Room 241 "MAZE" (TALISMAN)
GET TALISMAN
;
EAST EAST NORTH NORTH ; Room 227 "MAZE" Really out
;
EAST EAST NORTH NORTH ; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
NORTH WEST ; Room 203 "MAZE"
JUMP PIT ; Room 202 "GREAT FOREST" Treasure room
;
; Now back to the 2nd floor for OKKAN
DOWN ; Room 10 "TABLE AND CHAIR" start
;
WEST WEST NORTH DOWN ; 64 great pit
EAST SOUTH WEST SOUTH SOUTH SOUTH ; Room 96 "MUSTY PASSAGE" (OKKAN)

DROP TALISMAN

SCORE ; points=30 (out of 240), condition=251 (out of 255)

QUIET ; save as after_3.cas
```

## Task 4: Learn AKHIROM

Back around the loop again to get the ROPE from the 4th floor.

```
EAST DOWN SOUTH DOWN ; Room 233 "MAZE"
EAST EAST NORTH; Room 227 "MAZE" out again
NORTH EAST EAST EAST EAST; Room 223 "MAZE" (ROPE)
GET ROPE
;
; Now back to the 2nd floor for AKHIROM
NORTH WEST WEST ; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
NORTH WEST ; Room 203 "MAZE"
JUMP PIT ; Room 202 "GREAT FOREST" Treasure room
;
; Now back to the 2nd floor for OKKAN
DOWN ; Room 10 "TABLE AND CHAIR" start
;
WEST WEST NORTH DOWN ; 64 great pit
EAST SOUTH WEST SOUTH SOUTH SOUTH ; Room 96 "MUSTY PASSAGE"
EAST EAST EAST NORTH ; Room 91 "STONE TILES" now know AKHIROM

DROP ROPE

SCORE ; points=40 (out of 240), condition=251 (out of 255)

QUIET ; save as after_4.cas
```

## Task 5: Learn NERGAL

We are halfway through the spells. We need the SCEPTER from the 4th floor. The
NERGAL spell is in the room with _x, which will heal us and move us to a 
random room. There is no way around dealing with _x.

```
SOUTH WEST WEST DOWN SOUTH DOWN ; Room 233 "MAZE"
EAST EAST NORTH; Room 227 "MAZE" out again
EAST EAST NORTH NORTH ; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
WEST WEST SOUTH ; Room 218 "MAZE" (SCEPTER)
GET SCEPTER
;
; Now to the 3rd floor for NERGAL
NORTH EAST EAST NORTH WEST ; Room 203 "MAZE"
JUMP PIT ; Room 202 "GREAT FOREST" Treasure room
;
DOWN ; Room 10 "TABLE AND CHAIR" start
;
WEST WEST NORTH DOWN ; 64 great pit
JUMP PIT ; Room 128 "NARROW TUNNEL"
;
SOUTH ; Room 136 "SMALL CAVERN"
; 
SOUTH ; Room 144 "HIGH NARROW" walk through an enchanged aura (random placement)

; This room has _x in it. It heals us 40 health but moves us to a random room
; on this level (but not the maze). It won't heal/move us again for 10 minutes.
; We'll come right back to get the spell within that 10 minute window.

LOOK ; Room 90 "TOMB, SKULL" (*VIAL)

EAST NORTH UP ; Room 19 "ANCIENT CARVINGS"
EAST NORTH WEST WEST ; Room 10 "TABLE AND CHAIR" start
;
WEST WEST NORTH DOWN ; Room 64 "GREAT PIT
JUMP PIT ; Room 128 "NARROW TUNNEL"
;
SOUTH SOUTH ; Room 144 "HIGH NARROW" now know NERGAL
NORTH NORTH ; Room 128 "NARROW TUNNEL"
JUMP UP     ; Room 64 "GREAT PIT 

UP SOUTH EAST EAST ; Room 10 "TABLE AND CHAIR" start

DROP SCEPTER

SCORE ; points=50 (out of 240), condition=255 (out of 255)

QUIET ; save as after_5.cas
```

## Task 6: Learn BELROG

The BELROG spell requires us to have the VIAL from Room 90 "TOMB, SKULL". The VIAL is protected. We must have the
PARCHMENT, which we happened to leave near the VIAL in Room 98 "BROKEN PASSAGE".

```
WEST WEST NORTH DOWN ; Room 64 "GREAT PIT"
EAST SOUTH WEST SOUTH SOUTH SOUTH ; Room 96 "MUSTY PASSAGE"
EAST EAST ; Room 98 "BROKEN PASSAGE" (PARCHMENT)
GET PARCHMENT
;
EAST NORTH WEST ; Room 90 "TOMB, SKULL" (*VIAL)
GET VIAL
DROP PARCHMENT
;
EAST SOUTH WEST WEST DOWN WEST NORTH; Room 152 "GREAT TUNNEL" now know BELROG

DROP VIAL

SCORE ; points=60 (out of 240), condition=255 (out of 255)

QUIET ; save as after_6.cas
```

## Task 7: Learn CROM

CROM is in Room 237 "MAZE". We need the PENDANT from Room 146 "NARROW TUNNEL", which is just around the corner
from where we are.

```
EAST EAST NORTH ; Room 146 "NARROW TUNNEL" (PENDANT)
GET PENDANT
;
SOUTH SOUTH SOUTH DOWN ; Room 234 "MAZE"
EAST EAST EAST ; Room 237 "MAZE" now know CROM

DROP PENDANT

SCORE ; points=70 (out of 240), condition=255 (out of 255)

QUIET ; save as after_7.cas
```

## Task 8: Learn ISHTAR

The final spell is in Room 179 "MAZE". We need the *SPELLBOOK from Room 35 "SERVANT CHAMBER" on the 1st floor. The *SPELLBOOK
is protected. We must have the *POWERRING to get it. We already have BELROG, which is what we need for the *POWERRING.

So, we must go get the *POWERRING from Room 155 "TWISTING CORRIDOR" and then the *SPELLBOOK from Room 35. Then we go get ISHTAR from Room 179.

```
WEST WEST NORTH NORTH EAST EAST NORTH ; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
NORTH WEST ; Room 203 "MAZE"
JUMP PIT ; Room 202 "GREAT FOREST" treasure room
;
DOWN ; Room 10 "TABLE AND CHAIR" start
;
WEST WEST NORTH DOWN ; 64 great pit
EAST SOUTH WEST SOUTH SOUTH SOUTH ; Room 96 "MUSTY PASSAGE"
EAST EAST EAST NORTH NORTH EAST SOUTH ; Room 92 "WIDE ROOM"
JUMP DOWN ; Room 156 "CAVERN, BONES"
WEST ; Room 155 "TWISTING CORRIDOR" (*POWERRING)
GET POWERRING
;
EAST SOUTH SOUTH DOWN WEST NORTH ; Room 227 "MAZE" out again
EAST EAST NORTH NORTH ; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
NORTH WEST ; Room 203 "MAZE"
JUMP PIT ; Room 202 "GREAT FOREST" treasure room
;
DOWN ; Room 10 "TABLE AND CHAIR" start
;
EAST EAST SOUTH SOUTH SOUTH ; Room 36 "PANTRY"
DROP LAMP  ; We have to be light or the floor in the next room will cave in
WEST ; Room 35 "SERVANT CHAMBERS" (*SPELLBOOK)
GET SPELLBOOK
EAST ; Room 36 "PANTRY"
GET LAMP
NORTH NORTH NORTH WEST WEST; Room 10 "TABLE AND CHAIR" start
DROP POWERRING

;
WEST WEST NORTH DOWN ; 64 great pit
EAST SOUTH WEST SOUTH SOUTH SOUTH ; Room 96 "MUSTY PASSAGE"
EAST DOWN SOUTH SOUTH EAST EAST ; Room 179 "MAZE" now know ISHTAR

DROP SPELLBOOK

SCORE ; points=80 (out of 240), condition=255 (out of 255)

QUIET ; save to after_8.txt
```

## Task 9: Kill the SPRITE

Now for the 16 treasures worth 10 points each. We need to deposit these in the treasure room, but we
need to kill the SPRITE first. Otherwise the SPRITE might get in the treasure room and move things
around.

All we need to kill the sprite is the FOOD and NERGAL. The save-game-viewer for after_8 shows the
SPRITE is in Room 28: "DARK CHAMBER". But it might move to a nearby room before I get to it.

```
NORTH DOWN NORTH ; Room 227 "MAZE" out again
EAST EAST NORTH NORTH ; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
NORTH WEST ; Room 203 "MAZE"
JUMP PIT ; Room 202 "GREAT FOREST" treasure room
;
DOWN ; Room 10 "TABLE AND CHAIR" start
;
GET FOOD
EAST EAST SOUTH ; Room 28 "DARK CHAMBER"
KILL SPRITE

; The SPRITE throws the TABLET to a nearby room. We don't need it.

QUIET ; save to after_9.txt
```

## Task 10: Score POWERRING

* Use POWERRING to unlock SAPPHIRE, LIGHTRING. Score POWERRING.
* Use SAPPHIRE to unlock AMULET. SCORE SAPPHIRE.
* SCORE AMULET. 
* Use LIGHTRING to unlock TRUTHRING. Score LIGHTRING.
* Score TRUTHRING.
* Use SPELLBOOK to unlock POWDER. Score SPELLBOOK.
* Score POWDER.

Score RUBY "_e" in Room 196 "MAZE" (PARCHMENT, FLUTE, ROPE) PLAY FLUTE, CLIMB LEDGE  
Score OPAL "_g" Room 70 "FOUL SMELLING" (ROPE,DAGGER) TIE HYDRA, STAB HYDRA
FLEECE       SCORPION (*SKULL) (SCEPTER)

TREASURES:

  * POWERRING    Dropped earlier in Room 10 "TABLE AND CHAIR" start  
  * SAPPHIRE     Room 102 "ANCIENT KING" (POWERRING) OPEN CRYPT
  * AMULET       "_t" in Room 131 "STONE CORRIDOR" (SAPPHIRE)    
  * *LIGHTRING   Room 162 "STONE CROSS" (POWERRING, TALISMAN)
  * *TRUTHRING   Room 133 "DEEP PIT" (LIGHTRING, AX)
  * SPELLBOOK    Dropped earlier in Room 179 "MAZE"
  * POWDER       SATYR (SPELLBOOK)  

  * RUBY         "_e" in Room 196 "MAZE" (PARCHMENT, FLUTE, ROPE) PLAY FLUTE, CLIMB LEDGE  
  * OPAL         "_g" Room 70 "FOUL SMELLING" (ROPE,DAGGER) TIE HYDRA, STAB HYDRA
  * FLEECE       SCORPION (*SKULL) (SCEPTER)
  
  * SILVER       Dropped by "_u" in Room 8 "MARBLE FLOOR  
  * GOLD         "_s" in Room 216 "MAZE" LAMP OFF
  * DIAMNOD      "_n" in Room 67 "GREAT CRYPT" OPEN CRYPT
  * TIARA        "_203" in Room 203 "MAZE" LOOK PIT (may take several looks)
  * POTION       "_d" in Room 8 "MARBLE FLOOR" Dropped earlier
  * CROWN        "_33" in Room 33 "DARK, TOWER" Walk in with lamp on  

TODO blurb in the general on this.
Unfortunately, we can't carry it UP into the treasure room because of action C (by itself, the
SILVER is still too heavy. We have to go back through the maze and JUMP in.

We left the POWERRING in the start room. We need it to unlock the SPPHIRE and the LIGHTRING. We'll
unlock those on the way to the treasure room.

First to Room 102 "ANCIENT KING" to OPEN CRYPT. Then to 

```
NORTH WEST WEST
DROP FOOD
GET POWERRING
EAST EAST SOUTH SOUTH SOUTH EAST EAST
DOWN
OPEN CRYPT
;
DOWN
WEST SOUTH DOWN WEST WEST NORTH ; 227 "MAZE" out again
EAST EAST NORTH NORTH ; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
NORTH WEST ; Room 203 "MAZE"
JUMP PIT ; Room 202 "GREAT FOREST" treasure room
;
DOWN ; Room 10 "TABLE AND CHAIR" start
;
WEST WEST NORTH DOWN EAST SOUTH WEST SOUTH SOUTH SOUTH 
GET TALISMAN
EAST DOWN EAST ; Room 162 "STONE CROSS"
GET LIGHTRING
DROP LIGHTRING
DROP TALISMAN
;
SOUTH EAST DOWN NORTH 
; 227 "MAZE" out again
EAST EAST NORTH NORTH ; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
NORTH WEST ; Room 203 "MAZE"
JUMP PIT ; Room 202 "GREAT FOREST" treasure room
;
DROP POWERRING

SCORE ; points=90 (out of 240), condition=255 (out of 255)

QUIET ; after_10.txt
```

## Task 11: Score SAPPHIRE

The packrat "_t" Room 131 "STONE CORRIDOR" has the AMULET. If we are carrying the SAPPHIRE then "_t"
will drop the AMULET.

```
DOWN ; Room 10 "TABLE AND CHAIR" start
;
EAST EAST SOUTH SOUTH SOUTH EAST EAST ; Room 38 "EMPTY CHAMBER"
DOWN ; Room 102 "ANCIENT KING"
GET SAPPHIRE
JUMP UP ; Room 38 "EMPTY CHAMBER"
WEST WEST NORTH NORTH NORTH WEST WEST WEST WEST NORTH DOWN ; Room 64 "GREAT PIT"
;
JUMP PIT ; Room 128 "NARROW TUNNEL"
SOUTH SOUTH ; Room 144 "HIGH NARROW"
;
; ENCHANTED AURA moves us
;
LOOK ; Room 129 "SMOOTH MARBLE" we had good luck
;
EAST EAST ; Room 131 "STONE CORRIDOR"
GET AMULET
;
WEST SOUTH SOUTH SOUTH SOUTH SOUTH EAST DOWN NORTH ; 227 "MAZE" out again
;
DROP AMULET ; Easier to get to here
;
EAST EAST NORTH NORTH ; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
NORTH WEST ; Room 203 "MAZE"
JUMP PIT ; Room 202 "GREAT FOREST" treasure room
;
DROP SAPPHIRE

SCORE ; points=100 (out of 240), condition=255 (out of 255)

QUIET ; save as after_11.txt
```
## Task 12: Score AMULET

Back around the loop for the AMULET we dropped.

```
DOWN ; Room 10 "TABLE AND CHAIR" start
;
WEST WEST NORTH DOWN ; Room 64 "GREAT PIT"
EAST SOUTH WEST SOUTH SOUTH SOUTH EAST DOWN SOUTH EAST DOWN EAST NORTH ; 227 "MAZE" out again
;
GET AMULET
;
EAST EAST NORTH NORTH ; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
NORTH WEST ; Room 203 "MAZE"
JUMP PIT ; Room 202 "GREAT FOREST" treasure room
;
DROP AMULET

SCORE ; points=110 (out of 240), condition=255 (out of 255)

QUIET ; save as after_12.txt 
```

## Task 13 : Score LIGHTRING

We need the LIGHTRING to unlock the TRUTHRING. We already unlocked the LIGHTRING. We also need
the AX from Room 157 "WINDING TWISTING".

```
DOWN ; Room 10 "TABLE AND CHAIR" start
;
WEST WEST NORTH DOWN EAST SOUTH WEST SOUTH SOUTH SOUTH ; Room 96 "MUSTY PASSAGE"
EAST EAST EAST NORTH NORTH EAST SOUTH ; Room 92 "WIDE ROOM"
JUMP DOWN ; Room 156 "CAVERN BONES"
EAST ; Room 157 "WINDING TWISTING"
GET AX
;
WEST SOUTH WEST SOUTH DOWN NORTH ; 227 "MAZE" out again
;
EAST EAST NORTH NORTH ; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
NORTH WEST ; Room 203 "MAZE"
JUMP PIT ; Room 202 "GREAT FOREST" treasure room
;
DOWN ; Room 10 "TABLE AND CHAIR" start
;
WEST WEST NORTH DOWN ; Room 64 "GREAT PIT"
JUMP PIT ;  Room 128 "NARROW TUNNEL"
SOUTH SOUTH ; Room 144 "HIGH NARROW"
JUMP ; Room 133 "DEEP PIT"
DROP AX
;
WEST WEST WEST SOUTH SOUTH SOUTH SOUTH ; Room 162 "STONE CROSS"
GET LIGHTRING
SOUTH DOWN EAST NORTH ; 227 "MAZE" out again
;
EAST EAST NORTH NORTH ; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
NORTH WEST ; Room 203 "MAZE"
JUMP PIT ; Room 202 "GREAT FOREST" treasure room
;
DOWN ; Room 10 "TABLE AND CHAIR" start
;
WEST WEST NORTH DOWN ; Room 64 "GREAT PIT"
JUMP PIT ; Room 128 "NARROW TUNNEL"
SOUTH SOUTH ; Room 144 "HIGH NARROW"
JUMP ; Room 133 "DEEP PIT
;
GET AX
GET TRUTHRING

;
WEST WEST WEST SOUTH SOUTH SOUTH SOUTH SOUTH DOWN EAST NORTH ; 227 "MAZE" out again
DROP AX
DROP TRUTHRING
;
EAST EAST NORTH NORTH ; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
NORTH WEST ; Room 203 "MAZE"
JUMP PIT ; Room 202 "GREAT FOREST" treasure room
;
DROP LIGHTRING

SCORE ; points=120 (out of 240), condition=255 (out of 255)
; Halfway done!

QUIET ; save as after_13.txt

## Task 14: Score TRUTHRING

Loop back around and get the TRUTHRING.

```
JUMP DOWN ; 162 "STONE CROSS"
SOUTH DOWN EAST NORTH ; 227 "MAZE" out again
GET TRUTHRING
;
EAST EAST NORTH NORTH ; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
NORTH WEST ; Room 203 "MAZE"
JUMP PIT ; Room 202 "GREAT FOREST" treasure room
;
DROP TRUTHRING

SCORE ; points=130 (out of 240), condition=255 (out of 255)

QUIET ; save as after_14.txt
```

## Task 15: Score SPELLBOOK

We dropped the SPELLBOOK in Room 179 "MAZE" earlier. We need it to kill the SAYTR to get the POWDER. The
save-game viewer shows the SATYR in Room 220 "MAZE", but it will might move to a nearby room before we
get there.

```
JUMP DOWN ; Room 162 "STONE CROSS"
SOUTH SOUTH EAST ; Room 179 "MAZE"
GET SPELLBOOK

NORTH DOWN NORTH EAST ; Room 228 "MAZE"
KILL SATYR
NORTH EAST NORTH; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
NORTH WEST ; Room 203 "MAZE"
JUMP PIT ; Room 202 "GREAT FOREST" treasure room
;
DROP SPELLBOOK

SCORE ; points=140 (out of 240), condition=255 (out of 254)
; The SATYR did ONE damage. I was really lucky.
; Use the FOOD if you weren't so lucky.

QUIET ; save as after_15.txt
```

## Task 16: Score the POWDER

The SATYR tosses the POWDER to a nearby room. The save-game viewer shows it
in Room 229 "MAZE". Let's make the loop and grab it.

```
JUMP DOWN ; Room 162 "STONE CROSS"
SOUTH SOUTH EAST ; Room 179 "MAZE"

NORTH DOWN NORTH EAST ; Room 228 "MAZE"
EAST ; Room 229 "MAZE"
GET POWDER
;
NORTH NORTH ; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
NORTH WEST ; Room 203 "MAZE"
JUMP PIT ; Room 202 "GREAT FOREST" treasure room
;
DROP POWDER

SCORE ; points=150 (out of 240), condition=255 (out of 254)

QUIET ; save as after_16.txt
```

## Task 17:  