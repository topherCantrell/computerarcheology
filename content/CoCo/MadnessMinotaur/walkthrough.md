![Madness and the Minotaur](Madness.jpg)

# Walk-Through of my Game 

This is a walk-through of my game from start to finish. I broke the game up into 25 tasks,
and I present my save-game files after every task. Open the [Emulator on the Main Page](index.html) in 
a new tab and you can play along with my game. 

I made heavy use of the save-game viewer along the way. I can't imagine trying to find things
by wondering around. And I certainly can't imagine figuring out all the secrets without having
seen the code. This walk-through was challenging enough using the viewer and the code.

You can follow along with my steps, but you won't be able to blindly type them in. There are many random
elements in the game you have to adjust for:

Passages will block and unblock at random over time. You'll see the GROUND SHAKING. You can either find 
another route around a blocked passage or wait for the passage to unblock with time. The POWERRING will
let you walk through blocked passages, but the ring is heavy.

There are several passage-actions and enter-room-actions that might move you to a random room. You might
have to find your way back onto my path to follow along.

The creatures move around at random. The SPRITE relocates (at random) any objects it finds dropped in the
rooms. The creatures will attack you (with random damage). You might get hurt where I didn't, and you will
need to heal up before continuing on my path.

## General Strategy

There is limited access to the treasure room, Room 202 "GREAT FOREST". You can go UP from Room 10 "TABLE
AND CHAIR", the starting room, but you have to be light and healthy. Most of the objects are too heavy
to take UP by themselves let alone in groups.

The only other way to get to Room 202 "GREAT FOREST" is to JUMP PIT from Room 164 "NARROW PATH" or 
JUMP PIT from Room 203 "MAZE". Both of these jumps will fail if you are hurt and/or carrying multiple
items.

I used the JUMP PIT from Room 203 "MAZE" exclusively. Thus I carried treasures down to the bottom floor
one by one and jumped to the treasure room above the first floor. My game is a long series of loops from
top to bottom and back around.

There are 8 spells to learn (10 points each) and 16 treasures to drop in the treasure room (10 points each). 
My plan is to learn the spells first, then kill the SPRITE so it wouldn't relocate my treasures, and then 
score the treasures one by one.

## Task 1: Learn VETAR

SAVE GAME: after_start.txt

We have to have the LAMP to see on lower levels. The LAMP is in the Room 1 "EMPTY ROOM" along
with "_o", which pushes us back at random if we don't have CROM. Every time we
get pushed, it's 5 points of damage. The only thing we can do is keep trying WEST to get into
the room with lamp.

The VETAR spell in Room 3 "PILE OF BONES" requires us to have the FOOD (Room 14 "BEDROOM") and the 
MUSHROOM (Room 141 "NARROW TWISTING"). 

We start in Room 10 "TABLE AND CHAIR" (start).

```

; Get the LAMP
;
NORTH    ; Room 2 "GUARD ROOM" 
WEST*    ; Room 1 "EMPTY ROOM". You might get pushed back by "_o" trying to get into this room. Keep trying.
GET LAMP
LAMP ON

; Down to the mushroom
;
EAST SOUTH ; Back to Room 10 "TABLE AND CHAIR" (start)
WEST WEST  ; Room 8 "MARBLE FLOOR". This room has "_u", which will drop the SILVER if our LAMP is on. 
NORTH      ; Room 0 "STONE TOWER"
DOWN       ; Room 64 "GREAT PIT" (URN)

; The URN has oil in it. When our LAMP runs out, we'll return here to fill it.
;
EAST ; Room 65 "STONE WALL". This room has "_r" in it. After 3 visits, "_r" drops the SCARAB, which we won't need.
;
SOUTH WEST SOUTH SOUTH                      ; Room 88 "MUSTY, CORRIDOR". The "_q" poison is here ... KEEP MOVING
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
;
; We now know VETRA
;
WEST SOUTH           ; Room 10 "TABLE AND CHAIR"
;
DROP FOOD            ; These will be here if you need to heal up
DROP MUSHROOM

SCORE ; points=10 (out of 240), condition=251 (out of 255)

QUIET ; Saved as "after_1.txt"
```

## Task 2: Learn MITRA

Getting pushed will drain your health. So will the poison fog in Room 88 "MUSTY, CORRIDOR". So will a creature
if you got attacked on that run! You can EAT FOOD at this point and/or EAT MUSHROOM to restore your health.

It would be nice to pick up several objects at once, but that makes jumping much more likely to fail. Instead
we'll make several loops getting one object at a time. Next up is the PARCHMENT from Room 206 "Maze".

```
UP               ; Room 202 "GREAT FORREST" Treasure room
JUMP DOWN        ; Room 162 "STONE CROSS" (*LIGHTRING)
SOUTH            ; Room 170 "MAZE"
DOWN EAST NORTH  ; Room 227 "MAZE". It says "maze", but we are really out.
;
EAST EAST EAST EAST EAST ; Room 231 "MAZE"
NORTH NORTH NORTH NORTH  ; Room 199 "MAZE"
WEST SOUTH               ; Room 206 "MAZE" (PARCHMENT)
GET PARCHMENT
;
NORTH EAST SOUTH SOUTH WEST WEST ; Room 213 "MAZE"
JUMP MIST                        ; Room 212 "MAZE"
NORTH WEST                       ; Room 203 "MAZE"
JUMP PIT                         ; Room 202 "GREAT FOREST" Treasure room
;
; Now back to the 2nd floor for MITRA 
DOWN* ; Room 10 "TABLE AND CHAIR" start (you might end up in a nearby room instead)
;
WEST WEST NORTH DOWN               ; 64 great pit
EAST SOUTH WEST SOUTH SOUTH SOUTH  ; Room 96 "MUSTY PASSAGE" (OKKAN)
EAST EAST                          ; Room 96 "BROKEN PASSAGE" now  know MITRA

DROP PARCHMENT 

SCORE ; points=20 (out of 240), condition=251 (out of 255)

QUIET ; save as "after_1.cas"
```

## Task 3: Learn OKKAN

We just passed the OKKAN spell in Room 96 "MUSTY PASSAGE". We need the TALISMAN from
Room 241 "MAZE" to learn it.

```
WEST DOWN        ; Room 161 "LARGE STONE"
SOUTH DOWN SOUTH ; Room 241 "MAZE" (TALISMAN)
GET TALISMAN
;
; We'll be taking this path a lot in the game to come
EAST EAST NORTH NORTH  ; Room 227 "MAZE" Really out
;
EAST EAST NORTH NORTH  ; Room 213 "MAZE"
JUMP MIST              ; Room 212 "MAZE"
NORTH WEST             ; Room 203 "MAZE"
JUMP PIT               ; Room 202 "GREAT FOREST" Treasure room
;
; Now back to the 2nd floor for OKKAN
DOWN* ; Room 10 "TABLE AND CHAIR" start
;
WEST WEST NORTH DOWN               ; 64 great pit
EAST SOUTH WEST SOUTH SOUTH SOUTH  ; Room 96 "MUSTY PASSAGE" (OKKAN)

DROP TALISMAN

SCORE ; points=30 (out of 240), condition=251 (out of 255)

QUIET ; save as "after_3.txt"
```

## Task 4: Learn AKHIROM

Back around the loop again to get the ROPE from the 4th floor.

```
EAST DOWN SOUTH DOWN      ; Room 233 "MAZE"
EAST EAST NORTH           ; Room 227 "MAZE" out again
NORTH EAST EAST EAST EAST ; Room 223 "MAZE" (ROPE)
GET ROPE
;
; Now back to the 2nd floor for AKHIROM
NORTH WEST WEST  ; Room 213 "MAZE"
JUMP MIST        ; Room 212 "MAZE"
NORTH WEST       ; Room 203 "MAZE"
JUMP PIT         ; Room 202 "GREAT FOREST" Treasure room
;
DOWN* ; Room 10 "TABLE AND CHAIR" start
;
WEST WEST NORTH DOWN              ; Room 64 "GREAT PIT"
EAST SOUTH WEST SOUTH SOUTH SOUTH ; Room 96 "MUSTY PASSAGE"
EAST EAST EAST NORTH              ; Room 91 "STONE TILES" We now know AKHIROM

DROP ROPE

SCORE ; points=40 (out of 240), condition=251 (out of 255)

QUIET ; save as "after_4.txt"
```

## Task 5: Learn NERGAL

We are halfway through the spells. We need the SCEPTER from the 4th floor Room 218 "MAZE". The
NERGAL spell is in the room with "_x", which will heal us and move us to a 
random room. There is no way around dealing with "_x".

```
SOUTH WEST WEST DOWN SOUTH DOWN  ; Room 233 "MAZE"
EAST EAST NORTH                  ; Room 227 "MAZE" out again
EAST EAST NORTH NORTH            ; Room 213 "MAZE"
JUMP MIST                        ; Room 212 "MAZE"
WEST WEST SOUTH                  ; Room 218 "MAZE" (SCEPTER)
GET SCEPTER
;
; Now to the 3rd floor for NERGAL
NORTH EAST EAST NORTH WEST ; Room 203 "MAZE"
JUMP PIT                   ; Room 202 "GREAT FOREST" Treasure room
;
DOWN ; Room 10 "TABLE AND CHAIR" start
;
WEST WEST NORTH DOWN ; 64 great pit
JUMP PIT             ; Room 128 "NARROW TUNNEL"
;
SOUTH ; Room 136 "SMALL CAVERN"
; 
SOUTH ; Room 144 "HIGH NARROW" walk through an enchanted aura (random placement)

; This room has _x in it. It heals us 40 health but moves us to a random room
; on this level (but not the maze). It won't heal/move us again for 10 minutes.
; We'll come right back to get the spell within that 10 minute window.

LOOK ; Room 90 "TOMB, SKULL" (*VIAL)

EAST NORTH UP         ; Room 19 "ANCIENT CARVINGS"
EAST NORTH WEST WEST  ; Room 10 "TABLE AND CHAIR" start
;
WEST WEST NORTH DOWN  ; Room 64 "GREAT PIT
JUMP PIT              ; Room 128 "NARROW TUNNEL"
;
SOUTH SOUTH           ; Room 144 "HIGH NARROW" we now know NERGAL
NORTH NORTH           ; Room 128 "NARROW TUNNEL"
JUMP UP               ; Room 64 "GREAT PIT 
;
UP SOUTH EAST EAST    ; Room 10 "TABLE AND CHAIR" start
;
DROP SCEPTER

SCORE ; points=50 (out of 240), condition=255 (out of 255)

QUIET ; save as "after_5.txt"
```

## Task 6: Learn BELROG

The BELROG spell requires us to have the VIAL from Room 90 "TOMB, SKULL". The VIAL is protected. We must have the
PARCHMENT, which we happened to leave near the VIAL in Room 98 "BROKEN PASSAGE".

```
WEST WEST NORTH DOWN               ; Room 64 "GREAT PIT"
EAST SOUTH WEST SOUTH SOUTH SOUTH  ; Room 96 "MUSTY PASSAGE"
EAST EAST                          ; Room 98 "BROKEN PASSAGE" (PARCHMENT)
GET PARCHMENT
;
EAST NORTH WEST ; Room 90 "TOMB, SKULL" (*VIAL)
GET VIAL
DROP PARCHMENT
;
EAST SOUTH WEST WEST DOWN WEST NORTH ; Room 152 "GREAT TUNNEL" we now know BELROG
;
DROP VIAL

SCORE ; points=60 (out of 240), condition=255 (out of 255)

QUIET ; save as "after_6.txt"
```

## Task 7: Learn CROM

CROM is in Room 237 "MAZE". We need the PENDANT from Room 146 "NARROW TUNNEL", which is just around the corner
from where we are.

```
EAST EAST NORTH ; Room 146 "NARROW TUNNEL" (PENDANT)
GET PENDANT
;
SOUTH SOUTH SOUTH DOWN  ; Room 234 "MAZE"
EAST EAST EAST          ; Room 237 "MAZE" we now know CROM
;
DROP PENDANT

SCORE ; points=70 (out of 240), condition=255 (out of 255)

QUIET ; save as "after_7.txt"
```

## Task 8: Learn ISHTAR

The final spell is in Room 179 "MAZE". We need the *SPELLBOOK from Room 35 "SERVANT CHAMBER" on the 1st floor. The *SPELLBOOK
is protected. We must have the *POWERRING to get it. We already have BELROG, which is what we need for the *POWERRING.

So, we must go get the *POWERRING from Room 155 "TWISTING CORRIDOR" and then the *SPELLBOOK from Room 35. Then we go get ISHTAR from Room 179.

```
WEST WEST NORTH NORTH EAST EAST NORTH ; Room 213 "MAZE"
JUMP MIST    ; Room 212 "MAZE"
NORTH WEST   ; Room 203 "MAZE"
JUMP PIT     ; Room 202 "GREAT FOREST" treasure room
;
DOWN ; Room 10 "TABLE AND CHAIR" start
;
WEST WEST NORTH DOWN                  ; 64 great pit
EAST SOUTH WEST SOUTH SOUTH SOUTH     ; Room 96 "MUSTY PASSAGE"
EAST EAST EAST NORTH NORTH EAST SOUTH ; Room 92 "WIDE ROOM"
JUMP DOWN                             ; Room 156 "CAVERN, BONES"
WEST                                  ; Room 155 "TWISTING CORRIDOR" (*POWERRING)
GET POWERRING
;
EAST SOUTH SOUTH DOWN WEST NORTH  ; Room 227 "MAZE" out again
EAST EAST NORTH NORTH             ; Room 213 "MAZE"
JUMP MIST                         ; Room 212 "MAZE"
NORTH WEST                        ; Room 203 "MAZE"
JUMP PIT                          ; Room 202 "GREAT FOREST" treasure room
;
DOWN* ; Room 10 "TABLE AND CHAIR" start
;
EAST EAST SOUTH SOUTH SOUTH ; Room 36 "PANTRY"
;
DROP LAMP  ; We have to be light or the floor in the next room will cave in
WEST       ; Room 35 "SERVANT CHAMBERS" (*SPELLBOOK)
GET SPELLBOOK
EAST       ; Room 36 "PANTRY"
GET LAMP
;
NORTH NORTH NORTH WEST WEST ; Room 10 "TABLE AND CHAIR" start
DROP POWERRING
;
WEST WEST NORTH DOWN              ; 64 great pit
EAST SOUTH WEST SOUTH SOUTH SOUTH ; Room 96 "MUSTY PASSAGE"
EAST DOWN SOUTH SOUTH EAST EAST   ; Room 179 "MAZE" we now know ISHTAR
;
DROP SPELLBOOK

SCORE ; points=80 (out of 240), condition=255 (out of 255)

QUIET ; save to "after_8.txt"
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
* Score RUBY "_e" in Room 196 "MAZE" (PARCHMENT, FLUTE, ROPE) PLAY FLUTE, CLIMB LEDGE  
* Score OPAL "_g" Room 70 "FOUL SMELLING" (ROPE,DAGGER) TIE HYDRA, STAB HYDRA
* FLEECE       SCORPION (*SKULL) (SCEPTER)

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
  * GOLD         
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

## Task 17: Score RUBY

The RUBY is held by "_e" in Room 196 "MAZE". We have to have the PARCHMENT from Room 90,
the FLUTE from Room 176 "MAZE", and the ROPE from Room 91.

```
DOWN ; Room 10 "TABLE AND CHAIR"
;
WEST WEST NORTH DOWN ; Room 64 "GREAT PIT"
EAST SOUTH WEST SOUTH SOUTH SOUTH EAST EAST EAST NORTH ; Room 91 "STONE TILES"
GET ROPE
;
WEST ; Room 90 "TOMB, SKULL"
GET PARCHMENT
;
EAST SOUTH WEST WEST ; Room 97 "TWISTING PASSAGE"
DOWN SOUTH SOUTH WEST ; Room 176 "MAZE"
GET FLUTE
;
DOWN EAST EAST EAST NORTH NORTH ; Room 227 "MAZE" out again
EAST EAST EAST EAST NORTH NORTH NORTH NORTH ; Room 199 "MAZE"
WEST SOUTH WEST NORTH WEST ; Room 196 "MAZE"
PLAY FLUTE
CLIMB LEDGE
GET RUBY
;
EAST SOUTH EAST NORTH EAST SOUTH SOUTH WEST WEST ; Room 213 "MAZE"
DROP FLUTE
DROP PARCHMENT
DROP ROPE
JUMP MIST ; Room 212 "MAZE"
NORTH WEST ; ROOM 203 "MAZE"
JUMP PIT

DROP RUBY

SCORE ; points=160 (out of 240), condition=255 (out of 254)

QUIET ; save as after_17.txt
```

## Task 18: Score OPAL

Now we take on the HYDRA in Room 70 "FOUL SMELLING". For that battle we need the ROPE (just
dropped in Room 213) and the DAGGER from Room 14 "BED ROOM".

But first we have to refill the LAMP. It has been flickering. We can refill it from the URN
in Room 64 "GREAT PIT".

```
DOWN ; Room 10 "TABLE AND CHAIR"
;
EAST EAST EAST EAST ; Room 14 "BED ROOM"
GET DAGGER
WEST WEST WEST WEST ; Room 10 "TABLE AND CHAIR"
;
WEST WEST NORTH DOWN ; Room 64 "GREAT PIT"
GET URN
FILL LAMP
DROP URN
;
EAST SOUTH WEST SOUTH SOUTH SOUTH EAST ; Room 97 "TWISTING PASSAGE"
DROP DAGGER
;
DOWN SOUTH DOWN EAST EAST NORTH ; Room 227 "MAZE" out again
NORTH EAST EAST NORTH ; Room 213
GET ROPE
JUMP MIST ; Room 212
NORTH WEST
JUMP PIT ;
;

DOWN ; Room 10 "TABLE AND CHAIR"
;
WEST WEST NORTH DOWN ; Room 64 "GREAT PIT"
EAST SOUTH WEST SOUTH SOUTH SOUTH EAST ; Room 97 "TWISTING PASSAGE"
GET DAGGER
EAST EAST NORTH NORTH EAST EAST NORTH NORTH

;
NORTH EAST EAST NORTH NORTH ; Room 69 "CHILL MIST"
;
; TODO might get the lamp blown from us and need to use VETRA
;
; The HYDRA is in the room to the EAST. We go in and get pushed back. Then
; we tie it up (from a distance) and go back in to stab it.
;
EAST ; Room 70 "FOUL SMELLING"
TIE HYDRA
EAST ; Room 70 "FOUL SMELLING"
STAB HYDRA
GET OPAL
DROP DAGGER
;
JUMP DOWN ; Room 140 "NARROW TWISTING"
EAST SOUTH SOUTH WEST SOUTH ; Room 164 "NARROW PATH
JUMP PIT ; Room 202 "GREAT FOREST"

DROP OPAL

SCORE ; points=170 (out of 240), condition=255 (out of 254)

QUIET ; save as after_18.txt
```

## Task 19: Score FLEECE

The SCORPION is carrying the FLEECE. To kill the SCORPION we need the SKULL from Room 92 "WIDE ROOM".
The SKULL is protected and requires the SCEPTER from the starting room to get.

The save-game viewer shows the SCORPION in Room 14 "BED ROOM", but it might move to a neighboring
room before we get there.

```
DOWN ; Room 10 "TABLE AND CHAIRS"
;
GET SCEPTER
;
WEST WEST NORTH DOWN EAST SOUTH WEST SOUTH SOUTH SOUTH ; Room 96 "MUSTY PASSAGE"
EAST EAST EAST NORTH NORTH EAST SOUTH ; Room 92 "WIDE ROOM"
GET SKULL
; 
; save game viewer shows the SCORPION on the 1st floor
;
NORTH WEST SOUTH SOUTH WEST WEST WEST ; Room 96 "MUSTY PASSAGE"
NORTH NORTH NORTH EAST NORTH WEST UP ; Room 0 "STONE TOWER"
;
SOUTH EAST EAST EAST EAST EAST ; Room 13 "BROKEN TILES"
KILL SCORPION
;
; The FLEECE is thrown to a neighboring room. Search for it or use the save-game viewer.
;
WEST ; Room 12 "BROKEN GLASS"
GET FLEECE
WEST WEST ; Room 10 "TABLE AND CHAIR" start
DROP SCEPTER
DROP SKULL
;
WEST WEST NORTH DOWN EAST SOUTH WEST SOUTH SOUTH SOUTH ; Room 96 "MUSTY PASSAGE"
EAST DOWN SOUTH DOWN EAST EAST NORTH ; Room 227 "MAZE" out again
EAST EAST NORTH NORTH ; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
NORTH WEST ; Room 203
JUMP PIT ; Room 202

DROP FLEECE

SCORE ; points=180 (out of 240), condition=255 (out of 254)

QUIET ; save as after_19.txt
```

## Task 20: Score SILVER

The remaining treasures are easy! We just have to pick them up.

The SILVER was dropped by "_u" in Room 8 early in our game.

```
DOWN ; Room 10 "TABLE AND CHAIR" start
;
WEST WEST ; Room 8 "MARBLE FLOOR"
GET SILVER
NORTH DOWN EAST SOUTH WEST SOUTH SOUTH SOUTH EAST ; Room 97 "TWISTING PASSAGES"
DOWN SOUTH DOWN EAST EAST NORTH ; Room 227 "MAZE" out again
;
EAST EAST NORTH NORTH ; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
NORTH WEST ; Room 203
JUMP PIT ; Room 202

DROP SILVER

SCORE ; points=190 (out of 240), condition=255 (out of 254)

QUIET ; save as after_20.txt
```

## Task 21: Score GOLD

The GOLD is held by "_s" in Room 152. All we have to do is turn the lamp off in that room.

```
DOWN ; Room 10 "TABLE AND CHAIR" start
;
WEST WEST NORTH DOWN EAST SOUTH WEST SOUTH SOUTH SOUTH EAST DOWN ; Room 161 "LARGE STONE"
WEST NORTH ; Room 152 "GREAT TUNNEL"
LAMP OFF
LOOK
GET GOLD
LAMP ON
;
SOUTH EAST SOUTH DOWN EAST EAST NORTH ; Room 227 "MAZE" out again
;
EAST EAST NORTH NORTH ; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
NORTH WEST ; Room 203
JUMP PIT ; Room 202

DROP GOLD

SCORE ; points=200 (out of 240), condition=255 (out of 254)

QUIET ; save as after_21.txt
```

## Task 22: Score TIARA

The TIARA is held by "_203" in Room 201 "MAZE". We just have to look in the pit -- maybe
several times.

TODO Maybe _203 should be _201? The map shows _203 in _201 and _203. Error.

```
JUMP DOWN ; Room 162 "STONE CROSS"
SOUTH DOWN EAST NORTH ; Room 227 "MAZE" out again
;
EAST EAST NORTH NORTH ; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
WEST WEST SOUTH SOUTH WEST NORTH NORTH NORTH ; Room 201 "MAZE"
LOOK PIT ; Keep looking until you see the TIARA
GET TIARA
;
SOUTH SOUTH SOUTH EAST NORTH NORTH EAST EAST NORTH WEST ; Room 203 "MAZE
JUMP PIT ; Room 202

DROP TIARA 

SCORE ; points=210 (out of 240), condition=255 (out of 254)

QUIET ; save as after_22.txt
```

## Task 23: Score CROWN

The CROWN is held by "_33" in Room 33 "DARK, TOWER". Walk in with the LAMP on.

```
DOWN ; Room 10 "TABLE AND CHAIR"
;
; We have to work our way around some blocked passages.
EAST EAST EAST EAST SOUTH SOUTH WEST WEST SOUTH WEST ; Room 35 "SERVANT CHAMBER"
JUMP HOLE ; Room 34 SUNKEN PIT
WEST ; Room 33 "DARK, TOWER"
GET CROWN
;
WEST NORTH DOWN SOUTH EAST DOWN ; Room 161 "LARGE STONE"
SOUTH DOWN EAST EAST NORTH ; Room 227 "MAZE" out again
;
EAST EAST NORTH NORTH ; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
NORTH WEST ; Room 203
JUMP PIT ; Room 202

DROP CROWN

SCORE ; points=220 (out of 240), condition=255 (out of 254)

QUIET ; save as after_23.txt
```

## Task 24: Score 

  * POTION       "_d" in Room 216 "MAZE" Pile of glowing rocks
  
The POTION is in the "_d" PILE OF GLOWING ROCKS in Room 216. You have to drop everything to open the crypt.

```
DOWN ; Room 10 "TABLE AND CHAIR"
;
WEST WEST NORTH DOWN ; Room 64 "GREAT PIT"
EAST SOUTH EAST EAST NORTH ; Room 67 "GREAT CRYPT"
DROP LAMP
OPEN CRYPT
GET LAMP
LAMP ON
GET DIAMOND
;
SOUTH WEST WEST WEST SOUTH SOUTH SOUTH ; Room 96 "MUSTY PASSAGE"
EAST DOWN SOUTH DOWN EAST EAST NORTH ; Room 227 "MAZE" out again
;
EAST EAST NORTH NORTH ; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
NORTH WEST ; Room 203
JUMP PIT ; Room 202

DROP DIAMOND

SCORE ; points=230 (out of 240), condition=255 (out of 254)

QUIET ; save as after_24.txt
```

## Task 25: Score POTION

This is it! The last treasure! The "_d" PILE OF ROCKS holds the POTION in Room 216 "MAZE".

```
JUMP DOWN ; Room 162 "STONE CROSS"
SOUTH DOWN EAST NORTH; Room 227 "MAZE" out again
NORTH EAST EAST NORTH ; Room 213 "MAZE"
JUMP MIST ; Room 212 "MAZE"
WEST WEST SOUTH SOUTH WEST NORTH WEST ; Room 216 "MAZE"
;
OKKAN ; This gets the treasure from the rocks
;
GET POTION
EAST SOUTH EAST NORTH NORTH EAST EAST NORTH WEST ; Room 203 "MAZE"
JUMP PIT

SCORE ; points=235 (out of 240), condition=244 (out of 254) the spell drained us a bit

QUIET ; save as after_25.txt (just before winning)

DROP POTION

; CONGRATULATIONS!!! YOU WIN!

```
