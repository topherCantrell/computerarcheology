![Madness and the Minotaur](Madness.jpg)

# Madness and the Minotaur Save-Game Viewer

>>> playMe {

Paste the text of your save-game text file into the box below and click the "Show" button.

Leave the box blank to show the game-independent map.

The map is SVG -- you can scroll in and out.

```html
</p>
<textarea id="cocoTape" rows="16" style="font-size:8px;width:80ch;" ></textarea>
</p>
<button id="parseData">Show</button>
</p>

<svg id="svg" width="1400" height="5600">
</svg>

```

>>> }

```html
<div id="rawData" style="display:none">
```

## Engine Memory (0000-00FF stored in save game file 0000-00FF)

```plain
&nbsp;
0000: {{value1}}      ; current room
0001: {{value1}}      ; last room
0002: {{value1}}      ; direction command bit pattern
0003: {{value1}}      ; length of user input
0004: {{value1}}      ; weight of pack
0005: {{value1}}      ; physical condition
0006: {{value1}}      ; bulk of pack
0007: {{value1}}      ; decoded object number from noun
0008: {{value1}}      ; Accumulated odds of falling (0, 1/8, 2/8, 3/8 ... with each step in the dark)
0009: {{value1}}      ; Scorpion sting (0=not, not-zero=number of times)
000A: {{value1}}      ; 0 if lamp is off, not 0 is on
000B: {{value1}}      ; Count of spaces at the end of the row in print routine
000C: {{value1}}      ; Set by BetweenRoomACDE if a climb-down failed ... abort the movement
000D: {{value1}}      ; pushed back flag (nobody reads this)
000E: {{value1}}      ; HydraStatus: AA = tied up, 1 = dead, 0 = free
000F: {{value1}}      ; HydraPushedUsBack (must be set to TIE HYDRA)  0 = not, 1 = hydra blocked last move (cleared every direction command)
0010: {{value1}}      ; 1 if "pile of rocks" has been moved to us
0011: {{value1}}      ; 1 if "pile of rocks" has been exposed with OKKAN
0012: {{value1}}      ; 1 if south passage in room 9 is open. 0 if closed. (open with drapes)
0013: {{value1}}      ; Count down timer until we can walk through aura and heal again (10 seconds each time)
0014: {{value1}}      ; 1 if lamp has been blown from pack by entering room routine or failed jump
0015: {{value1}}      ; 1 if treasure "$0B" has been released
0016: {{value1}}      ; NEVER USED
0017: {{value1}}      ; Random number for passage-description printing
0018: {{value1}} {{value2}}   ; Rolling pointer to BASIC rom for random numbers
001A: {{value1}}      ; Number of times advice has been given 0-13
001B: {{value1}}      ; Object 0 
001C: {{value1}}      ; Object 1
001D: {{value1}}      ; Object 2
001E: {{value1}}      ; Object 3    Advice table. Object number is stored here. Upper
001F: {{value1}}      ; Object 4    bit set if advice has already been given for this
0020: {{value1}}      ; Object 5    protected object.
0021: {{value1}}      ; Object 6
0022: {{value1}}      ; Object 7
0023: {{value1}}      ; Object 8
0024: {{value1}}      ; Object 9
0025: {{value1}}      ; Object 10
0026: {{value1}}      ; Object 11
0027: {{value1}}      ; Object 12
0028: {{value1}}      ; Calculated score
0029: {{value1}}      ; NEVER USED
002A: {{value1}}      ; Verb command number
002B: {{value1}}      ; Noun word number
002C: {{value1}}      ; Trigger object to make packrat drop treasure
002D: {{value1}}      ; NEVER USED
002E: {{value1}}      ; Holder value for BetweenRoomACDE
002F: {{value1}}      ; General use lots of places
0030: {{value1}}      ; Used in InPack
0031: {{value1}}      ; Used in InPack
0032: {{value1}}      ; Set by EnteringRoomAction_q (MYSTERIOUS FOG)
0033: {{value1}}      ; Current room of HYDRA
0034: {{value1}}      ; Number of times more ISHTAR can be used. Random init to 1-4.
0035: {{value1}}      ; Room for small pit in corner of room
0036: {{value1}}      ; Room of LEDGE
0037: {{value1}}      ; Room of "pile of rocks" (OKKAN spell)
0038: {{value1}} {{value2}}   ; Oil level of lamp (0 is empty)
003A: {{value1}}      ; Number of times lamp can be filled (init to $34 + 4)
003B: {{value1}} {{value2}}   ; Pointer to start of input on screen
003D: {{value1}}      ; Used in Random-between-0-and-B
003E: {{value1}}      ; Time until we can drink from bottle to heal again (16 seconds)
003F: {{value1}}      ; Interrupt divisor count (seconds)
0040: {{value1}}      ; Interrupt sub divisor (minutes)
0041: {{value1}}      ; Minotaur state timer
0042: {{value1}}      ; Troglodyte state timer
0043: {{value1}}      ; Satyr state timer
0044: {{value1}}      ; Scorpion state timer
0045: {{value1}}      ; Fog clock runs in room MYSTERIOUS FOG. At 6 seconds we get warned. At 10 we die.
0046: {{value1}}      ; Minutes of immunity left (AKHIROM gives 3 minutes)
0047: {{value1}}      ; Count of times entering room with EnteringRoomAction_r. 3 times and treasure drops.
0048: {{value1}}      ; NEVER USED
0049: {{value1}}      ; NEVER USED
004A: {{value1}} {{value2}}   ; Continual second counter (nobody uses it)
004C: {{value1}} {{value2}}   ; Counts the time in a room. Once 15, no going BACK
004E: {{value1}}      ; NEVER USED
004F: {{value1}}      ; NEVER USED
0050: {{value1}}      ; NEVER USED
0051: {{value1}}      ; Used in Oracle advice
0052: {{value1}}      ; Used in killing Hydra
0053: {{value1}}      ; Used in sound effects
0054: {{value1}} {{value2}}   ; Used in tape-write
;
; 16 byte for decode and word wrap
0056: {{mvalue_16}}
;
; Not used 
0066: {{mvalue_10}}
0070: {{mvalue_16}}
0080: {{mvalue_16}}
0090: {{mvalue_16}}
00A0: {{mvalue_16}}
00B0: {{mvalue_16}}
00C0: {{mvalue_16}}
00D0: {{mvalue_16}}
00E0: {{mvalue_16}}
00F0: {{mvalue_3}}
;
00F3: {{value1}}    {{decode}}  ;
00F4: {{value1}}    {{decode}}  ;
00F5: {{value1}}    {{decode}}  ;
00F6: {{value1}}    {{decode}}  ;
00F7: {{value1}}    {{decode}}  ; Shifting buffer of rooms blocked by Shaking Ground.
00F8: {{value1}}    {{decode}}  ; As new rooms are blocked at random, they go on the
00F9: {{value1}}    {{decode}}  ; end of the list. Rooms are pulled off of the front
00FA: {{value1}}    {{decode}}  ; of the list and unblocked completely. This keeps
00FB: {{value1}}    {{decode}}  ; lots of shaking from blocking up the floors over
00FC: {{value1}}    {{decode}}  ; time.
00FD: {{value1}}    {{decode}}  ;
00FE: {{value1}}    {{decode}}  ;
00FF: {{value1}}    {{decode}}  ;
```

## Screen State

```plain
; Text screens stored in save file 0100-03BF
; Only the last 6 rows of the 1st screen
0340: {{value}} ; {{decode}}
0360: {{value}} ; {{decode}}
0380: {{value}} ; {{decode}}
03A0: {{value}} ; {{decode}}
03C0: {{value}} ; {{decode}}
03E0: {{value}} ; {{decode}}
;
; All 16 rows of the 2nd screen
0400: {{value}} ; {{decode}}
0420: {{value}} ; {{decode}}
0440: {{value}} ; {{decode}}
0460: {{value}} ; {{decode}}
0480: {{value}} ; {{decode}}
04A0: {{value}} ; {{decode}}
04C0: {{value}} ; {{decode}}
04E0: {{value}} ; {{decode}}
0500: {{value}} ; {{decode}}
0520: {{value}} ; {{decode}}
0540: {{value}} ; {{decode}}
0560: {{value}} ; {{decode}}
0580: {{value}} ; {{decode}}
05A0: {{value}} ; {{decode}}
05C0: {{value}} ; {{decode}}
05E0: {{value}} ; {{decode}}
```

## Game Data (3BC1-3FFF stored in save game file 03C0-07FE)
### Spells

```plain
; Spell data
;   AA BB CC DD
;   AA = 1st required object to learn spell
;   BB = 2nd required object to learn spell
;   CC = room spell is in (not learned)
;   DD = $80 if learned, 0 if not
;
;                      Spell    Must have to learn
3BC1: 09 01 {{value1}} {{value2}}    ; VETRA:   MUSHROOM and FOOD     {{decode}}
3BC5: 0E 37 {{value1}} {{value2}}    ; MITRA:   PARCHMENT and  VETRA  {{decode}}                 
3BC9: 11 38 {{value1}} {{value2}}    ; OKKAN:   TALISMAN and MITRA    {{decode}}
3BCD: 18 39 {{value1}} {{value2}}    ; AKHIROM: ROPE and OKKAN        {{decode}}
3BD1: 0B 3A {{value1}} {{value2}}    ; NERGAL:  SCEPTER and AKHIROM   {{decode}}
3BD5: 0F 3B {{value1}} {{value2}}    ; BELROG:  VIAL and NERGAL       {{decode}}
3BD9: 0A 3C {{value1}} {{value2}}    ; CROM:    PENDANT and BELROG    {{decode}}
3BDD: 23 3D {{value1}} {{value2}}    ; ISHTAR:  SPELLBOOK and CROM    {{decode}}  
```

### Jump Info

```plain
; Describes places where you can JUMP. Everything but one byte is static (same every game).
; The room number of the last jump is set to the room with Enter Room Action _203.
;  AA BB CC DD EE
;   AA = Starting room
;   BB = Compared to (Phys-weight) AND (Phys-bulk) ... see below
;   CC = Fail action (see below)
;   DD = Target room of jump
;   EE = Word of thing to jump (or FF for just JUMP)
;
;     If Phys-weight is less than BB, you fail the jump as CC describes.
;     Otherwise if Phys-bulk is less than BB, you fumble (make the jump but
;       drop the heaviest object).
;
;     CC = 0x00 ... a failed jump (BB condition) is death
;     CC = 0x80 ... a failure is a fumble. You make the jump but drop the
;                   heaviest object object. There is a 1/8th chance that
;                   the fumbled object is lost (unless it is required).
;     CC =    N ... a failure is a stumble. You don't make the jump and
;                   take N damage.
;
3BE1: 8F 80 00 97 6D ; From 143 "JUMP PIT"   to 151. Required=128 or DEATH
3BE6: 97 80 80 8F 6D ; From 151 "JUMP PIT"   to 143. Required=128 or FUMBLE
3BEB: 10 80 80 11 2C ; From 16  "JUMP POOL"  to 17.  Required=128 or FUMBLE
3BF0: 11 80 80 10 2C ; From 17  "JUMP POOL"  to 16.  Required=128 or FUMBLE
3BF5: 4E 40 80 56 41 ; From 78  "JUMP CHASM" to 86.  Required=64  or FUMBLE
3BFA: 56 40 80 4E 41 ; From 86  "JUMP CHASM" to 78.  Required=64  or FUMBLE
3BFF: 2C 0A 0A B6 6D ; From 44  "JUMP PIT"   to 182. Required=10  or STUMBLE(10)
3C04: B6 14 14 2C 6D ; From 182 "JUMP PIT"   to 44.  Required=20  or STUMBLE(20)
3C09: A4 A0 00 CA 6D ; From 164 "JUMP PIT"   to 202. Required=160 or DEATH
3C0E: 85 C0 80 CB 6D ; From 133 "JUMP PIT"   to 203. Required=192 or FUMBLE
3C13: 90 14 14 85 FF ; From 144 "JUMP"       to 133. Required=20  or STUMBLE(20)
3C18: CB 80 1E CA 6D ; From 203 "JUMP PIT"   to 202. Required=128 or STUMBLE(30)
3C1D: D5 46 14 D4 6B ; From 213 "JUMP MIST"  to 212. Required=70  or STUMBLE(20)
3C22: D4 46 14 D5 6B ; From 212 "JUMP MIST"  to 213. Required=70  or STUMBLE(20)
3C27: 23 96 28 22 9F ; From 35  "JUMP HOLE"  to 34.  Required=150 or STUMBLE(40)
3C2C: 22 78 14 23 6D ; From 34  "JUMP PIT"   to 35.  Required=120 or STUMBLE(20)
3C31: 80 64 80 40 05 ; From 128 "JUMP UP"    to 64.  Required=100 or FUMBLE
3C36: A6 50 80 66 05 ; From 166 "JUMP UP"    to 102. Required=80  or FUMBLE
3C3B: 66 A0 80 26 05 ; From 102 "JUMP UP"    to 38.  Required=160 or FUMBLE
3C40: 5C 96 1E 9C 06 ; From 92  "JUMP DOWN"  to 156. Required=150 or STUMBLE(30)
3C45: 46 50 14 8C 06 ; From 70  "JUMP DOWN"  to 140. Required=80  or STUMBLE(20)
3C4A: 5E 5A 0A 9E 06 ; From 94  "JUMP DOWN"  to 158. Required=90  or STUMBLE(10)
3C4F: 40 1E 00 80 6D ; From 64  "JUMP PIT"   to 128. Required=30  or DEATH
3C54: CA 1E 14 A2 06 ; From 202 "JUMP DOWN"  to 162. Required=30  or STUMBLE(20)
;
3C59: {{value}} 8C 80 27 06 ; From {{decode}} "JUMP DOWN"  to 39.  Required=140 or FUMBLE
;
3C5E: 00      
```
    
### Name Table

```plain
; Read by the code to place objects, but never changed.
3C5F: 19 ; Sprite
3C60: 1A ; Troglodyte
3C61: 1B ; Scorpion
3C62: 1C ; Nymph
3C63: 1D ; Satyr
3C64: 1E ; Minotaur
3C65: 01 ; Crypt
3C66: 02 ; Crypt of kings
3C67: 03 ; Entering-room-u
3C68: 04 ; Entering-room-aa
3C69: 05 ; Small pit
3C6A: 06 ; Ledge
3C6B: 07 ; Hydra
3C6C: 08 ; Pile of glowing rocks
3C6D: 09 ; Eerie glow
3C6E: 0A ; Packrat
```

### Who Holds What

```plain
; Held-by table. Treasures are carried by creatures or "held" by a room. This
; table maps the holder to the treasure.
;  AA BB
;   A = owner (see object list below)
;   B = held object
;
; Objects by number:
;   1=crypt, 2=crypt-kings, 3=_u, 4=_33, 5=pit, 6=ledge, 7=hydra, 
;   8=pile-of-rocks, 9=_s, 10=_t(rat), 11=_r, 
;   Greater than 12: creature number
;
3C6F: {{value}} 2E  ; 46 "OPAL"      Held by {{decode}}
3C71: {{value}} 2F  ; 47 "SAPPHIRE"  Held by {{decode}}
3C73: {{value}} 12  ; 18 "SCROLL"    Held by {{decode}}    
3C75: {{value}} 15  ; 21 "SCARAB"    Held by {{decode}}
3C77: {{value}} 16  ; 22 "JEWLBOX"   Held by {{decode}}
3C79: {{value}} 17  ; 23 "TABLET"    Held by {{decode}}
3C7B: {{value}} 20  ; 32 "GOLD"      Held by {{decode}}
3C7D: {{value}} 21  ; 33 "SILVER"    Held by {{decode}}
3C7F: {{value}} 22  ; 34 "DIAMOND"   Held by {{decode}}
3C81: {{value}} 24  ; 36 "RUBY"      Held by {{decode}}
3C83: {{value}} 25  ; 37 "FLEECE"    Held by {{decode}}
3C85: {{value}} 26  ; 38 "TIARA"     Held by {{decode}}
3C87: {{value}} 27  ; 39 "POWDER"    Held by {{decode}}
3C89: {{value}} 28  ; 40 "AMULET"    Held by {{decode}}
3C8B: {{value}} 29  ; 41 "POTION"    Held by {{decode}}
3C8D: {{value}} 2D  ; 45 "CROWN"     Held by {{decode}}
```

### Enter Room Actions

```plain
&nbsp;
3C8F: {{value}} 1B 6D  ; Room {{decode}}  _a     ; Cave in to next floor if pack heavier than 192. If so move _a and _b to random rooms.
3C92: {{value}} 1B 70  ; Room {{decode}}  _b     ; Cave in to next floor if pack heavier than 128. If so move _a and _b to random rooms.
3C95: {{value}} 1B 73  ; Room {{decode}}  _c     ; Cave in to next floor if pack heavier than 95. If so move _a and _b to random rooms.
3C98: {{value}} 1B 9C  ; Room {{decode}}  _d     ; If we have VETAR make the pile-of-rocks appear in this room (it stays here).
3C9B: {{value}} 1B B3  ; Room {{decode}}  _e     ; Play sound effect. If we play the flute and have the parchment then the LEDGE appears here.
3C9E: {{value}} 1B B7  ; Room {{decode}}  _f     ; Powerful gust blows lamp out of grasp. 
3CA1: {{value}} 1B F9  ; Room {{decode}}  _g     ; Hydra is here. If it is free it pushes us back to last room. 
3CA4: {{value}} 1C 15  ; Room {{decode}}  _h     ; If we know VETAR or have the SCEPTER, nothing happens. Otherwise we RUN.
3CA7: {{value}} 1C 2C  ; Room {{decode}}  _i     ; Pushed back if we don't have VETAR.
3CAA: {{value}} 1C 2F  ; Room {{decode}}  _j     ; Pushed back if we don't have MITRA.
3CAD: {{value}} 1C 32  ; Room {{decode}}  _k     ; Pushed back if we don't have OKKAN.
3CB0: {{value}} 1C 35  ; Room {{decode}}  _l     ; Pushed back if we don't have AKHIROM.
3CB3: {{value}} 1C 38  ; Room {{decode}}  _m     ; Pushed back if we don't have NERGAL.
3CB6: {{value}} 1C 3B  ; Room {{decode}}  _n     ; Pushed back if we don't have BELROG.
3CB9: {{value}} 1C 3E  ; Room {{decode}}  _o     ; Pushed back if we don't have CROM.
3CBC: {{value}} 1C 41  ; Room {{decode}}  _p     ; Pushed back if we don't have ISHTAR.
3CBF: {{value}} 1C 68  ; Room {{decode}}  _q     ; Start the poison clock (we can't stay here long). 1/3 of the time we give the clock an extra tick.
3CC2: {{value}} 1C 7A  ; Room {{decode}}  _r     ; When we enter this room 3 times the treasure is released.
3CC5: {{value}} 1C 68  ; Room {{decode}}  _q     ; see above 
3CC8: {{value}} 1C 68  ; Room {{decode}}  _q     ; see above
3CCB: {{value}} 1C 8D  ; Room {{decode}}  _s     ; If we have the lamp and it is off then the room drops its treasure. (Strange color walls)
3CCE: {{value}} 1C A9  ; Room {{decode}}  _t     ; If we are holding the packrat's trigger treasure (randomized at start) then the packrat drops his treasure.
3CD1: {{value}} 1C 68  ; Room {{decode}}  _q     ; see above
3CD4: {{value}} 1C CC  ; Room {{decode}}  _u     ; If we can see you instantly get the treasure.
3CD7: {{value}} 1C F0  ; Room {{decode}}  _v     ; Print POOL OF OIL if the lamp can be refilled.
3CDA: {{value}} 1B B7  ; Room {{decode}}  _f     ; see above
3CDD: {{value}} 1C E0  ; Room {{decode}}  _32    ; (Same as 32 below)
3CE0: {{value}} 1D 00  ; Room {{decode}}  _x     ; Add 40 to health and move us a short distance away. 10 minutes must pass before again. 
3CE3: {{value}} 1D 00  ; Room {{decode}}  _x     ; see above
3CE6: {{value}} 1D 22  ; Room {{decode}}  _203   ; Print "SMALL PIT IN CORNER OF ROOM"
3CE9: D5 1D 27  ; Room 213  _213   ; Print "LAYER OF MIST EAST WALL"
3CEC: 20 1C E0  ; Room 32   _32    ; If we can't see we take 30 damage.
3CEF: 21 1C D6  ; Room 33   _33    ; If we can see you instantly get the treasure.
3CF2: CB 1D 22  ; Room 203  _203   ; Print SMALL PIT IN CORNER OF ROOM.
3CF5: {{value}} 1B B4  ; Room {{decode}}  _z       ; Room with music (init to room 16 to 39). The sprite can't move objects here.
3CF8: E8 1D 2D  ; Room 232  _232   ; _232 If we came south to this room and carrying pendant move us near start and random room for pendant.
3CFB: 00
```

### Object Data

```plain
; AA BB bsdp_PPxy
;  A = Current room number
;  B = Display name to use
;
;   b=1 if in backpack
;   s=1 if spell or creature
;   d=1 if object is required in game (can't get permanently lost in a failed jump)
;   p=1 if "protected"
;
;   PP is bottle/urn fill status
;   x=1 if spell or dead creature 
;   y=1 if carried object or creature
;
; Objects are not accessible to the player (noun) if x or y are set.
;
3CFC: {{value1}} 01 {{value2}}  ; 1 "FOOD"         {{decode}}
3CFF: {{value1}} 02 {{value2}}  ; 2 "BOTTLE"       {{decode}}
3D02: {{value1}} 03 {{value2}}  ; 3 "DAGGER"       {{decode}}
3D05: {{value1}} 04 {{value2}}  ; 4 "MACE"         {{decode}}
3D08: {{value1}} 05 {{value2}}  ; 5 "AX"           {{decode}}
3D0B: {{value1}} 06 {{value2}}  ; 6 "SWORD"        {{decode}}
3D0E: {{value1}} 07 {{value2}}  ; 7 "SHIELD"       {{decode}}
3D11: {{value1}} 08 {{value2}}  ; 8 "FLUTE"        {{decode}}
3D14: {{value1}} 09 {{value2}}  ; 9 "MUSHROOM"     {{decode}}
3D17: {{value1}} 0A {{value2}}  ; 10 "PENDANT"     {{decode}}
3D1A: {{value1}} 0B {{value2}}  ; 11 "SCEPTER"     {{decode}}
3D1D: {{value1}} 0C {{value2}}  ; 12 "LAMP"        {{decode}}
3D20: {{value1}} 0D {{value2}}  ; 13 "BASKET"      {{decode}}
3D23: {{value1}} 0E {{value2}}  ; 14 "PARCHMENT"   {{decode}}
3D26: {{value1}} 0F {{value2}}  ; 15 "VIAL"        {{decode}}
3D29: {{value1}} 10 {{value2}}  ; 16 "URN"         {{decode}}
3D2C: {{value1}} 11 {{value2}}  ; 17 "TALISMAN"    {{decode}}
3D2F: {{value1}} 12 {{value2}}  ; 18 "SCROLL"      {{decode}}
3D32: {{value1}} 13 {{value2}}  ; 19 "GOBLET"      {{decode}}
3D35: {{value1}} 14 {{value2}}  ; 20 "SKULL"       {{decode}}
3D38: {{value1}} 15 {{value2}}  ; 21 "SCARAB"      {{decode}}
3D3B: {{value1}} 16 {{value2}}  ; 22 "JEWELBOX"    {{decode}}
3D3E: {{value1}} 17 {{value2}}  ; 23 "TABLET"      {{decode}}
3D41: {{value1}} 18 {{value2}}  ; 24 "ROPE"        {{decode}}
3D44: {{value1}} 19 {{value2}}  ; 25 "SPRITE"      {{decode}}
3D47: {{value1}} 1A {{value2}}  ; 26 "TROGLODYTE"  {{decode}}
3D4A: {{value1}} 1B {{value2}}  ; 27 "SCORPION"    {{decode}}
3D4D: {{value1}} 1C {{value2}}  ; 28 "NYMPH"       {{decode}}
3D50: {{value1}} 1D {{value2}}  ; 29 "SATYR"       {{decode}}
3D53: {{value1}} 1E {{value2}}  ; 30 "MINOTAUR"    {{decode}}
3D56: {{value1}} 1F {{value2}}  ; 31 "ORACLE"      {{decode}}
3D59: {{value1}} 20 {{value2}}  ; 32 "GOLD"        {{decode}}
3D5C: {{value1}} 21 {{value2}}  ; 33 "SILVER"      {{decode}}
3D5F: {{value1}} 22 {{value2}}  ; 34 "DIAMOND"     {{decode}}
3D62: {{value1}} 23 {{value2}}  ; 35 "SPELLBOOK"   {{decode}}
3D65: {{value1}} 24 {{value2}}  ; 36 "RUBY"        {{decode}}
3D68: {{value1}} 25 {{value2}}  ; 37 "FLEECE"      {{decode}}
3D6B: {{value1}} 26 {{value2}}  ; 38 "TIARA"       {{decode}}
3D6E: {{value1}} 27 {{value2}}  ; 39 "POWDER"      {{decode}}
3D71: {{value1}} 28 {{value2}}  ; 40 "AMULET"      {{decode}}
3D74: {{value1}} 29 {{value2}}  ; 41 "POTION"      {{decode}}
3D77: {{value1}} 2A {{value2}}  ; 42 "POWERRING"   {{decode}}
3D7A: {{value1}} 2B {{value2}}  ; 43 "LIGHTRING"   {{decode}}
3D7D: {{value1}} 2C {{value2}}  ; 44 "TRUTHRING"   {{decode}}
3D80: {{value1}} 2D {{value2}}  ; 45 "CROWN"       {{decode}}
3D83: {{value1}} 2E {{value2}}  ; 46 "OPAL"        {{decode}}
3D86: {{value1}} 2F {{value2}}  ; 47 "SAPPHIRE"    {{decode}}
3D89: {{value1}} 30 {{value2}}  ; 48 "NORTH"       {{decode}}
3D8C: {{value1}} 31 {{value2}}  ; 49 "NORTH"       {{decode}}
3D8F: {{value1}} 32 {{value2}}  ; 50 "NORTH"       {{decode}}
3D92: {{value1}} 33 {{value2}}  ; 51 "NORTH"       {{decode}}
3D95: {{value1}} 34 {{value2}}  ; 52 "NORTH"       {{decode}}
3D98: {{value1}} 35 {{value2}}  ; 53 "NORTH"       {{decode}}
3D9B: {{value1}} 36 {{value2}}  ; 54 "NORTH"       {{decode}}
3D9E: {{value1}} 37 {{value2}}  ; 55 "VETAR"       {{decode}}
3DA1: {{value1}} 38 {{value2}}  ; 56 "MITRA"       {{decode}}
3DA4: {{value1}} 39 {{value2}}  ; 57 "OKKAN"       {{decode}}
3DA7: {{value1}} 3A {{value2}}  ; 58 "AKHIROM"     {{decode}}
3DAA: {{value1}} 3B {{value2}}  ; 59 "NERGAL"      {{decode}}
3DAD: {{value1}} 3C {{value2}}  ; 60 "BELROG"      {{decode}}
3DB0: {{value1}} 3D {{value2}}  ; 61 "CROM"        {{decode}}
3DB3: {{value1}} 3E {{value2}}  ; 62 "ISHTAR"      {{decode}}
;
3DB6: 00 FF     ; End of list marker
```

### Natural Passages

```plain
; Read by the code but never changed (these are the passages on the map above).

; Floor 1
3DB8: 11 04 07 06 06 03 01 12 ; .D...S  ...E..  ...EWS  ...EW.  ...EW.  ....WS  .....S  .D..W.
3DC0: 0C 06 2F 06 07 0E 0B 01 ; ..NE..  ...EW.  U.NEWS  ...EW.  ...EWS  ..NEW.  ..N.WS  .....S
3DC8: 01 08 09 04 0B 01 0D 0B ; .....S  ..N...  ..N..S  ...E..  ..N.WS  .....S  ..NE.S  ..N.WS
3DD0: 19 14 06 03 0D 0E 0A 09 ; .DN..S  .D.E..  ...EW.  ....WS  ..NE.S  ..NEW.  ..N.W.  ..N..S
3DD8: 0C 06 03 0C 0E 06 12 08 ; ..NE..  ...EW.  ....WS  ..NE..  ..NEW.  ...EW.  .D..W.  ..N...
3DE0: 35 37 37 37 37 37 37 37 ; UD.E.S  UD.EWS  UD.EWS  UD.EWS  UD.EWS  UD.EWS  UD.EWS  UD.EWS
3DE8: 3F 3F 3F 3F 3F 3F 3F 3F ; UDNEWS  UDNEWS  UDNEWS  UDNEWS  UDNEWS  UDNEWS  UDNEWS  UDNEWS
3DF0: 3E 3E 3E 3E 3E 3E 3E 3A ; UDNEW.  UDNEW.  UDNEW.  UDNEW.  UDNEW.  UDNEW.  UDNEW.  UDN.W.

; Floor 2
3DF8: 24 03 24 03 25 06 03 38 ; U..E..  ....WS  U..E..  ....WS  U..E.S  ...EW.  ....WS  UDN...
3E00: 0D 0E 06 0E 0A 09 08 01 ; ..NE.S  ..NEW.  ...EW.  ..NEW.  ..N.W.  ..N..S  ..N...  .....S
3E08: 09 04 06 27 07 0B 05 0B ; ..N..S  ...E..  ...EW.  U..EWS  ...EWS  ..N.WS  ...E.S  ..N.WS
3E10: 09 30 04 0B 08 0C 0A 09 ; ..N..S  UD....  ...E..  ..N.WS  ..N...  ..NE..  ..N.W.  ..N..S
3E18: 0C 16 06 0E 06 06 10 18 ; ..NE..  .D.EW.  ...EW.  ..NEW.  ...EW.  ...EW.  .D....  .DN...
3E20: 35 3F 37 37 37 37 37 37 ; UD.E.S  UDNEWS  UD.EWS  UD.EWS  UD.EWS  UD.EWS  UD.EWS  UD.EWS
3E28: 3F 3F 3F 3F 3F 3F 3F 3F ; UDNEWS  UDNEWS  UDNEWS  UDNEWS  UDNEWS  UDNEWS  UDNEWS  UDNEWS
3E30: 3E 3E 3E 3E 3E 3E 3E 3A ; UDNEW.  UDNEW.  UDNEW.  UDNEW.  UDNEW.  UDNEW.  UDNEW.  UDN.W.

; Floor 3
3E38: 01 04 27 06 06 02 05 20 ; .....S  ...E..  U..EWS  ...EW.  ...EW.  ....W.  ...E.S  U.....
3E40: 09 05 07 06 06 03 0B 02 ; ..N..S  ...E.S  ...EWS  ...EW.  ...EW.  ....WS  ..N.WS  ....W.
3E48: 08 09 09 05 03 09 28 01 ; ..N...  ..N..S  ..N..S  ...E.S  ....WS  ..N..S  U.N...  .....S
3E50: 05 2F 0B 0C 2F 0E 10 09 ; ...E.S  U.NEWS  ..N.WS  ..NE..  U.NEWS  ..NEW.  .D....  ..N..S
3E58: 0C 0F 0F 07 07 03 02 09 ; ..NE..  ..NEWS  ..NEWS  ...EWS  ...EWS  ....WS  ....W.  ..N..S
3E60: 35 37 37 37 37 37 37 3F ; UD.E.S  UD.EWS  UD.EWS  UD.EWS  UD.EWS  UD.EWS  UD.EWS  UDNEWS
3E68: 3F 3F 3F 3F 3F 3F 3F 3F ; UDNEWS  UDNEWS  UDNEWS  UDNEWS  UDNEWS  UDNEWS  UDNEWS  UDNEWS
3E70: 3E 3E 3E 3E 3E 3E 3E 3E ; UDNEW.  UDNEW.  UDNEW.  UDNEW.  UDNEW.  UDNEW.  UDNEW.  UDNEW.

; Floor 4
3E78: 05 06 06 06 06 03 05 03 ; ...E.S  ...EW.  ...EW.  ...EW.  ...EW.  ....WS  ...E.S  ....WS
3E80: 0D 03 10 04 03 0C 0A 09 ; ..NE.S  ....WS  .D....  ...E..  ....WS  ..NE..  ..N.W.  ..N..S
3E88: 0D 0B 05 06 0A 05 07 0B ; ..NE.S  ..N.WS  ...E.S  ...EW.  ..N.W.  ...E.S  ...EWS  ..N.WS
3E90: 0C 0B 09 05 07 0F 0F 0B ; ..NE..  ..N.WS  ..N..S  ...E.S  ...EWS  ..NEWS  ..NEWS  ..N.WS
3E98: 05 0E 0A 0C 0E 0E 0E 0A ; ...E.S  ..NEW.  ..N.W.  ..NE..  ..NEW.  ..NEW.  ..NEW.  ..N.W.
3EA0: 35 37 37 3F 37 37 37 37 ; UD.E.S  UD.EWS  UD.EWS  UDNEWS  UD.EWS  UD.EWS  UD.EWS  UD.EWS
3EA8: 3F 3F 3F 3F 3F 3F 3F 3F ; UDNEWS  UDNEWS  UDNEWS  UDNEWS  UDNEWS  UDNEWS  UDNEWS  UDNEWS
3EB0: 3E 3E 3E 3E 3E 3E 3E 3A ; UDNEW.  UDNEW.  UDNEW.  UDNEW.  UDNEW.  UDNEW.  UDNEW.  UDN.W.
```

### Blocked Passages

```plain
; These appear on the map above

; Floor 1
3EB8: {{mvalue}}
3EC0: {{mvalue}}
3EC8: {{mvalue}}
3ED0: {{mvalue}}
3ED8: {{mvalue}}
3EE0: {{mvalue}}
3EE8: {{mvalue}}
3EF0: {{mvalue}}

; Floor 2
3EF8: {{mvalue}}
3F00: {{mvalue}}
3F08: {{mvalue}}
3F10: {{mvalue}}
3F18: {{mvalue}}
3F20: {{mvalue}}
3F28: {{mvalue}}
3F30: {{mvalue}}

; Floor 3
3F38: {{mvalue}}
3F40: {{mvalue}}
3F48: {{mvalue}}
3F50: {{mvalue}}
3F58: {{mvalue}}
3F60: {{mvalue}}
3F68: {{mvalue}}
3F70: {{mvalue}}

; Floor 4
3F78: {{mvalue}}
3F80: {{mvalue}}
3F88: {{mvalue}}
3F90: {{mvalue}}
3F98: {{mvalue}}
3FA0: {{mvalue}}
3FA8: {{mvalue}}
3FB0: {{mvalue}}
```

### Protection Lists

```plain
&nbsp;
3FB8: 
```

```html
</div>

<script src="/js/Binary.js"></script>
<script src="madness.js"></script>
<script src="savegame.js"></script>
<script>
window.onload = function() {
	$('#parseData').on('click',function() {
		viewSaveFile($('#cocoTape').val());
	});
};
</script>

```