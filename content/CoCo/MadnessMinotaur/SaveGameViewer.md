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

<script src="BinaryDataMadness.js"></script>
<script src="savegame.js"></script>
<script>
$(function() {

$('#parseData').on('click',function() {
	viewSaveFile($('#cocoTape').val());
});

});
</script>

<svg id="svg" width="1400" height="5600">
</svg>

```

>>> }

```html
<div id="rawData" style="display:none">
```

```plain

<h2>Engine Memory (0000-00FF stored in save game file 0000-00FF)</h2>
0000: <span class="sg_value">{{value1}}</span>      current room
0001: <span class="sg_value">{{value1}}</span>      last room
0002: <span class="sg_value">{{value1}}</span>      direction command bit pattern
0003: <span class="sg_value">{{value1}}</span>      length of user input
0004: <span class="sg_value">{{value1}}</span>      weight of pack
0005: <span class="sg_value">{{value1}}</span>      physical condition
0006: <span class="sg_value">{{value1}}</span>      bulk of pack
0007: <span class="sg_value">{{value1}}</span>      decoded object number from noun
0008: <span class="sg_value">{{value1}}</span>      Accumulated odds of falling (0, 1/8, 2/8, 3/8 ... with each step in the dark)
0009: <span class="sg_value">{{value1}}</span>      Scorpion sting (0=not, not-zero=number of times)
000A: <span class="sg_value">{{value1}}</span>      0 if lamp is off, not 0 is on
000B: <span class="sg_value">{{value1}}</span>      Count of spaces at the end of the row in print routine
000C: <span class="sg_value">{{value1}}</span>      Set by BetweenRoomACDE if a climb-down failed ... abort the movement
000D: <span class="sg_value">{{value1}}</span>      pushed back flag (nobody reads this)
000E: <span class="sg_value">{{value1}}</span>      HydraStatus: AA = tied up, 1 = dead, 0 = free
000F: <span class="sg_value">{{value1}}</span>      HydraPushedUsBack (must be set to TIE HYDRA)  0 = not, 1 = hydra blocked last move (cleared every direction command)
0010: <span class="sg_value">{{value1}}</span>      1 if "pile of rocks" has been moved to us
0011: <span class="sg_value">{{value1}}</span>      1 if "pile of rocks" has been exposed with OKKAN
0012: <span class="sg_value">{{value1}}</span>      1 if south passage in room 9 is open. 0 if closed. (open with drapes)
0013: <span class="sg_value">{{value1}}</span>      Count down timer until we can walk through aura and heal again (10 seconds each time)
0014: <span class="sg_value">{{value1}}</span>      1 if lamp has been blown from pack by entering room routine or failed jump
0015: <span class="sg_value">{{value1}}</span>      1 if treasure "$0B" has been released
0016: <span class="sg_value">{{value1}}</span>      NEVER USED
0017: <span class="sg_value">{{value1}}</span>      Random number for passage-description printing
0018: <span class="sg_value">{{value1}}</span> <span class="sg_value">{{value2}}</span>   Rolling pointer to BASIC rom for random numbers
001A: <span class="sg_value">{{value1}}</span>      Number of times advice has been given 0-13
001B: <span class="sg_value">{{value1}}</span>      Object 0 
001C: <span class="sg_value">{{value1}}</span>      Object 1
001D: <span class="sg_value">{{value1}}</span>      Object 2
001E: <span class="sg_value">{{value1}}</span>      Object 3    Advice table. Object number is stored here. Upper
001F: <span class="sg_value">{{value1}}</span>      Object 4    bit set if advice has already been given for this
0020: <span class="sg_value">{{value1}}</span>      Object 5    protected object.
0021: <span class="sg_value">{{value1}}</span>      Object 6
0022: <span class="sg_value">{{value1}}</span>      Object 7
0023: <span class="sg_value">{{value1}}</span>      Object 8
0024: <span class="sg_value">{{value1}}</span>      Object 9
0025: <span class="sg_value">{{value1}}</span>      Object 10
0026: <span class="sg_value">{{value1}}</span>      Object 11
0027: <span class="sg_value">{{value1}}</span>      Object 12
0028: <span class="sg_value">{{value1}}</span>      Calculated score
0029: <span class="sg_value">{{value1}}</span>      NEVER USED
002A: <span class="sg_value">{{value1}}</span>      Verb command number
002B: <span class="sg_value">{{value1}}</span>      Noun word number
002C: <span class="sg_value">{{value1}}</span>      Trigger object to make packrat drop treasure
002D: <span class="sg_value">{{value1}}</span>      NEVER USED
002E: <span class="sg_value">{{value1}}</span>      Holder value for BetweenRoomACDE
002F: <span class="sg_value">{{value1}}</span>      General use lots of places
0030: <span class="sg_value">{{value1}}</span>      Used in InPack
0031: <span class="sg_value">{{value1}}</span>      Used in InPack
0032: <span class="sg_value">{{value1}}</span>      Set by EnteringRoomAction_q (MYSTERIOUS FOG)
0033: <span class="sg_value">{{value1}}</span>      Current room of HYDRA
0034: <span class="sg_value">{{value1}}</span>      Number of times more ISHTAR can be used. Random init to 1-4.
0035: <span class="sg_value">{{value1}}</span>      Room for small pit in corner of room
0036: <span class="sg_value">{{value1}}</span>      Room of LEDGE
0037: <span class="sg_value">{{value1}}</span>      Room of "pile of rocks" (OKKAN spell)
0038: <span class="sg_value">{{value1}}</span> <span class="sg_value">{{value2}}</span>   Oil level of lamp (0 is empty)
003A: <span class="sg_value">{{value1}}</span>      Number of times lamp can be filled (init to $34 + 4)
003B: <span class="sg_value">{{value1}}</span> <span class="sg_value">{{value2}}</span>   Pointer to start of input on screen
003D: <span class="sg_value">{{value1}}</span>      Used in Random-between-0-and-B
003E: <span class="sg_value">{{value1}}</span>      Time until we can drink from bottle to heal again (16 seconds)
003F: <span class="sg_value">{{value1}}</span>      Interrupt divisor count (seconds)
0040: <span class="sg_value">{{value1}}</span>      Interrupt sub divisor (minutes)
0041: <span class="sg_value">{{value1}}</span>      Minotaur state timer
0042: <span class="sg_value">{{value1}}</span>      Troglodyte state timer
0043: <span class="sg_value">{{value1}}</span>      Satyr state timer
0044: <span class="sg_value">{{value1}}</span>      Scorpion state timer
0045: <span class="sg_value">{{value1}}</span>      Fog clock runs in room MYSTERIOUS FOG. At 6 seconds we get warned. At 10 we die.
0046: <span class="sg_value">{{value1}}</span>      Minutes of immunity left (AKHIROM gives 3 minutes)
0047: <span class="sg_value">{{value1}}</span>      Count of times entering room with EnteringRoomAction_r. 3 times and treasure drops.
0048: <span class="sg_value">{{value1}}</span>      NEVER USED
0049: <span class="sg_value">{{value1}}</span>      NEVER USED
004A: <span class="sg_value">{{value1}}</span> <span class="sg_value">{{value2}}</span>   Continual second counter (nobody uses it)
004C: <span class="sg_value">{{value1}}</span> <span class="sg_value">{{value2}}</span>   Counts the time in a room. Once 15, no going BACK
004E: <span class="sg_value">{{value1}}</span>      NEVER USED
004F: <span class="sg_value">{{value1}}</span>      NEVER USED
0050: <span class="sg_value">{{value1}}</span>      NEVER USED
0051: <span class="sg_value">{{value1}}</span>      Used in Oracle advice
0052: <span class="sg_value">{{value1}}</span>      Used in killing Hydra
0053: <span class="sg_value">{{value1}}</span>      Used in sound effects
0054: <span class="sg_value">{{value1}}</span> <span class="sg_value">{{value2}}</span>   Used in tape-write
;
; 16 byte for decode and word wrap
0056: <span class="sg_value">{{mvalue_16}}</span>
;
; Not used 
0066: <span class="sg_value">{{mvalue_10}}</span>
0070: <span class="sg_value">{{mvalue_16}}</span>
0080: <span class="sg_value">{{mvalue_16}}</span>
0090: <span class="sg_value">{{mvalue_16}}</span>
00A0: <span class="sg_value">{{mvalue_16}}</span>
00B0: <span class="sg_value">{{mvalue_16}}</span>
00C0: <span class="sg_value">{{mvalue_16}}</span>
00D0: <span class="sg_value">{{mvalue_16}}</span>
00E0: <span class="sg_value">{{mvalue_16}}</span>
00F0: <span class="sg_value">{{mvalue_3}}</span>
;
00F3: <span class="sg_value">{{value1}}</span>    <span class="sg_value">{{decode}}</span>  .
00F4: <span class="sg_value">{{value1}}</span>    <span class="sg_value">{{decode}}</span>  .
00F5: <span class="sg_value">{{value1}}</span>    <span class="sg_value">{{decode}}</span>  .
00F6: <span class="sg_value">{{value1}}</span>    <span class="sg_value">{{decode}}</span>  .
00F7: <span class="sg_value">{{value1}}</span>    <span class="sg_value">{{decode}}</span>  Shifting buffer of rooms blocked by Shaking Ground.
00F8: <span class="sg_value">{{value1}}</span>    <span class="sg_value">{{decode}}</span>  As new rooms are blocked at random, they go on the
00F9: <span class="sg_value">{{value1}}</span>    <span class="sg_value">{{decode}}</span>  end of the list. Rooms are pulled off of the front
00FA: <span class="sg_value">{{value1}}</span>    <span class="sg_value">{{decode}}</span>  of the list and unblocked completely. This keeps
00FB: <span class="sg_value">{{value1}}</span>    <span class="sg_value">{{decode}}</span>  lots of shaking from blocking up the floors over
00FC: <span class="sg_value">{{value1}}</span>    <span class="sg_value">{{decode}}</span>  time.
00FD: <span class="sg_value">{{value1}}</span>    <span class="sg_value">{{decode}}</span>  .
00FE: <span class="sg_value">{{value1}}</span>    <span class="sg_value">{{decode}}</span>  .
00FF: <span class="sg_value">{{value1}}</span>    <span class="sg_value">{{decode}}</span>  .
<h2>Screen State</h2>
; Text screens stored in save file 0100-03BF
; Only the last 6 rows of the 1st screen
0340: <span class="sg_value">{{value}}</span> <span class="sg_value">{{decode}}</span>
0360: <span class="sg_value">{{value}}</span> <span class="sg_value">{{decode}}</span>
0380: <span class="sg_value">{{value}}</span> <span class="sg_value">{{decode}}</span>
03A0: <span class="sg_value">{{value}}</span> <span class="sg_value">{{decode}}</span>
03C0: <span class="sg_value">{{value}}</span> <span class="sg_value">{{decode}}</span>
03E0: <span class="sg_value">{{value}}</span> <span class="sg_value">{{decode}}</span>
;
; All 16 rows of the 2nd screen
0400: <span class="sg_value">{{value}}</span> <span class="sg_value">{{decode}}</span>
0420: <span class="sg_value">{{value}}</span> <span class="sg_value">{{decode}}</span>
0440: <span class="sg_value">{{value}}</span> <span class="sg_value">{{decode}}</span>
0460: <span class="sg_value">{{value}}</span> <span class="sg_value">{{decode}}</span>
0480: <span class="sg_value">{{value}}</span> <span class="sg_value">{{decode}}</span>
04A0: <span class="sg_value">{{value}}</span> <span class="sg_value">{{decode}}</span>
04C0: <span class="sg_value">{{value}}</span> <span class="sg_value">{{decode}}</span>
04E0: <span class="sg_value">{{value}}</span> <span class="sg_value">{{decode}}</span>
0500: <span class="sg_value">{{value}}</span> <span class="sg_value">{{decode}}</span>
0520: <span class="sg_value">{{value}}</span> <span class="sg_value">{{decode}}</span>
0540: <span class="sg_value">{{value}}</span> <span class="sg_value">{{decode}}</span>
0560: <span class="sg_value">{{value}}</span> <span class="sg_value">{{decode}}</span>
0580: <span class="sg_value">{{value}}</span> <span class="sg_value">{{decode}}</span>
05A0: <span class="sg_value">{{value}}</span> <span class="sg_value">{{decode}}</span>
05C0: <span class="sg_value">{{value}}</span> <span class="sg_value">{{decode}}</span>
05E0: <span class="sg_value">{{value}}</span> <span class="sg_value">{{decode}}</span>
<h2>Game Data (3BC1-3FFF stored in save game file 03C0-07FE)</h2>
<h3>Spells</h3>
; Spell data
;   AA BB CC DD
;   AA = 1st required object to learn spell
;   BB = 2nd required object to learn spell
;   CC = room spell is in (not learned)
;   DD = $80 if learned, 0 if not
;
;                      Spell    Must have to learn
3BC1: 09 01 <span class="sg_value">{{value1}}</span> <span class="sg_value">{{value2}}</span>    ; VETRA:   MUSHROOM and FOOD     <span class="sg_value">{{decode}}</span>
3BC5: 0E 37 <span class="sg_value">{{value1}}</span> <span class="sg_value">{{value2}}</span>    ; MITRA:   PARCHMENT and  VETRA  <span class="sg_value">{{decode}}</span>                 
3BC9: 11 38 <span class="sg_value">{{value1}}</span> <span class="sg_value">{{value2}}</span>    ; OKKAN:   TALISMAN and MITRA    <span class="sg_value">{{decode}}</span>
3BCD: 18 39 <span class="sg_value">{{value1}}</span> <span class="sg_value">{{value2}}</span>    ; AKHIROM: ROPE and OKKAN        <span class="sg_value">{{decode}}</span>
3BD1: 0B 3A <span class="sg_value">{{value1}}</span> <span class="sg_value">{{value2}}</span>    ; NERGAL:  SCEPTER and AKHIROM   <span class="sg_value">{{decode}}</span>
3BD5: 0F 3B <span class="sg_value">{{value1}}</span> <span class="sg_value">{{value2}}</span>    ; BELROG:  VIAL and NERGAL       <span class="sg_value">{{decode}}</span>
3BD9: 0A 3C <span class="sg_value">{{value1}}</span> <span class="sg_value">{{value2}}</span>    ; CROM:    PENDANT and BELROG    <span class="sg_value">{{decode}}</span>
3BDD: 23 3D <span class="sg_value">{{value1}}</span> <span class="sg_value">{{value2}}</span>    ; ISHTAR:  SPELLBOOK and CROM    <span class="sg_value">{{decode}}</span>  
<h3>Jump Info</h3> 
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
;
3C59: <span class="sg_value">{{value}}</span> 8C 80 27 06; From <span class="sg_value">{{decode}}</span> "JUMP DOWN"  to 39.  Required=140 or FUMBLE
;
3C5E: 00          
<h3>Name Table</h3>
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
<h3>Who Holds What</h3>
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
3C6F: <span class="sg_value">{{value}}</span> 2E  ; 46 "OPAL"      Held by <span class="sg_value">{{decode}}</span>
3C71: <span class="sg_value">{{value}}</span> 2F  ; 47 "SAPPHIRE"  Held by <span class="sg_value">{{decode}}</span>
3C73: <span class="sg_value">{{value}}</span> 12  ; 18 "SCROLL"    Held by <span class="sg_value">{{decode}}</span>    
3C75: <span class="sg_value">{{value}}</span> 15  ; 21 "SCARAB"    Held by <span class="sg_value">{{decode}}</span>
3C77: <span class="sg_value">{{value}}</span> 16  ; 22 "JEWLBOX"   Held by <span class="sg_value">{{decode}}</span>
3C79: <span class="sg_value">{{value}}</span> 17  ; 23 "TABLET"    Held by <span class="sg_value">{{decode}}</span>
3C7B: <span class="sg_value">{{value}}</span> 20  ; 32 "GOLD"      Held by <span class="sg_value">{{decode}}</span>
3C7D: <span class="sg_value">{{value}}</span> 21  ; 33 "SILVER"    Held by <span class="sg_value">{{decode}}</span>
3C7F: <span class="sg_value">{{value}}</span> 22  ; 34 "DIAMOND"   Held by <span class="sg_value">{{decode}}</span>
3C81: <span class="sg_value">{{value}}</span> 24  ; 36 "RUBY"      Held by <span class="sg_value">{{decode}}</span>
3C83: <span class="sg_value">{{value}}</span> 25  ; 37 "FLEECE"    Held by <span class="sg_value">{{decode}}</span>
3C85: <span class="sg_value">{{value}}</span> 26  ; 38 "TIARA"     Held by <span class="sg_value">{{decode}}</span>
3C87: <span class="sg_value">{{value}}</span> 27  ; 39 "POWDER"    Held by <span class="sg_value">{{decode}}</span>
3C89: <span class="sg_value">{{value}}</span> 28  ; 40 "AMULET"    Held by <span class="sg_value">{{decode}}</span>
3C8B: <span class="sg_value">{{value}}</span> 29  ; 41 "POTION"    Held by <span class="sg_value">{{decode}}</span>
3C8D: <span class="sg_value">{{value}}</span> 2D  ; 45 "CROWN"     Held by <span class="sg_value">{{decode}}</span>
<h3>Enter Room Table</h3> 
3C8F: <span class="sg_value">{{value}}</span> 1B 6D  ; <span class="sg_value">{{decode}}</span>  _a     ; Cave in to next floor if pack heavier than 192. If so move a nd b to random rooms.
3C92: <span class="sg_value">{{value}}</span> 1B 70  ; <span class="sg_value">{{decode}}</span>  _b     ; Cave in to next floor if pack heavier than 128. If so move a nd b to random rooms.
3C95: <span class="sg_value">{{value}}</span> 1B 73  ; <span class="sg_value">{{decode}}</span>  _c     ; Cave in to next floor if pack heavier than 95. If so move a nd b to random rooms.
3C98: <span class="sg_value">{{value}}</span> 1B 9C  ; <span class="sg_value">{{decode}}</span>  _d     ; If we have VETAR make the pile-of-rocks appear in this room (it stays here).
3C9B: <span class="sg_value">{{value}}</span> 1B B3  ; <span class="sg_value">{{decode}}</span>  _e     ; Play sound effect. If we play the flute and have the parchment then the LEDGE appears here.
3C9E: <span class="sg_value">{{value}}</span> 1B B7  ; <span class="sg_value">{{decode}}</span>  _f     ; Powerful gust blows lamp out of grasp. 
3CA1: <span class="sg_value">{{value}}</span> 1B F9  ; <span class="sg_value">{{decode}}</span>  _g     ; Hydra is here. If it is free it pushes us back to last room. 
3CA4: <span class="sg_value">{{value}}</span> 1C 15  ; <span class="sg_value">{{decode}}</span>  _h     ; If we know VETAR or have the SCEPTER, nothing happens. Otherwise we RUN.
3CA7: <span class="sg_value">{{value}}</span> 1C 2C  ; <span class="sg_value">{{decode}}</span>  _i     ; Pushed back if we don't have VETAR.
3CAA: <span class="sg_value">{{value}}</span> 1C 2F  ; <span class="sg_value">{{decode}}</span>  _j     ; Pushed back if we don't have MITRA.
3CAD: <span class="sg_value">{{value}}</span> 1C 32  ; <span class="sg_value">{{decode}}</span>  _k     ; Pushed back if we don't have OKKAN.
3CB0: <span class="sg_value">{{value}}</span> 1C 35  ; <span class="sg_value">{{decode}}</span>  _l     ; Pushed back if we don't have AKHIROM.
3CB3: <span class="sg_value">{{value}}</span> 1C 38  ; <span class="sg_value">{{decode}}</span>  _m     ; Pushed back if we don't have NERGAL.
3CB6: <span class="sg_value">{{value}}</span> 1C 3B  ; <span class="sg_value">{{decode}}</span>  _n     ; Pushed back if we don't have BELROG.
3CB9: <span class="sg_value">{{value}}</span> 1C 3E  ; <span class="sg_value">{{decode}}</span>  _o     ; Pushed back if we don't have CROM.
3CBC: <span class="sg_value">{{value}}</span> 1C 41  ; <span class="sg_value">{{decode}}</span>  _p     ; Pushed back if we don't have ISHTAR.
3CBF: <span class="sg_value">{{value}}</span> 1C 68  ; <span class="sg_value">{{decode}}</span>  _q     ; Start the poison clock (we can't stay here long). 1/3 of the time we give the clock an extra tick.
3CC2: <span class="sg_value">{{value}}</span> 1C 7A  ; <span class="sg_value">{{decode}}</span>  _r     ; When we enter this room 3 times the treasure is released.
3CC5: <span class="sg_value">{{value}}</span> 1C 68  ; <span class="sg_value">{{decode}}</span>  _q     ; see above 
3CC8: <span class="sg_value">{{value}}</span> 1C 68  ; <span class="sg_value">{{decode}}</span>  _q     ; see above
3CCB: <span class="sg_value">{{value}}</span> 1C 8D  ; <span class="sg_value">{{decode}}</span>  _s     ; If we have the lamp and it is off then the room drops its treasure. (Strange color walls)
3CCE: <span class="sg_value">{{value}}</span> 1C A9  ; <span class="sg_value">{{decode}}</span>  _t     ; If we are holding the packrat's trigger treasure (randomized at start) then the packrat drops his treasure.
3CD1: <span class="sg_value">{{value}}</span> 1C 68  ; <span class="sg_value">{{decode}}</span>  _q     ; see above
3CD4: <span class="sg_value">{{value}}</span> 1C CC  ; <span class="sg_value">{{decode}}</span>  _u     ; If we can see you instantly get the treasure.
3CD7: <span class="sg_value">{{value}}</span> 1C F0  ; <span class="sg_value">{{decode}}</span>  _v     ; Print POOL OF OIL if the lamp can be refilled.
3CDA: <span class="sg_value">{{value}}</span> 1B B7  ; <span class="sg_value">{{decode}}</span>  _f     ; see above
3CDD: <span class="sg_value">{{value}}</span> 1C E0  ; <span class="sg_value">{{decode}}</span>  _32    ; (Same as 32 below)
3CE0: <span class="sg_value">{{value}}</span> 1D 00  ; <span class="sg_value">{{decode}}</span>  _x     ; Add 40 to health and move us a short distance away. 10 minutes must pass before again. 
3CE3: <span class="sg_value">{{value}}</span> 1D 00  ; <span class="sg_value">{{decode}}</span>  _x     ; see above
3CE6: <span class="sg_value">{{value}}</span> 1D 22  ; <span class="sg_value">{{decode}}</span>  _203   ; Print "SMALL PIT IN CORNER OF ROOM"
3CE9: D5 1D 27  ; 213  _213     ; Print "LAYER OF MIST EAST WALL"
3CEC: 20 1C E0  ; 32   _32      ; If we can't see we take 30 damage.
3CEF: 21 1C D6  ; 33   _33      ; If we can see you instantly get the treasure.
3CF2: CB 1D 22  ; 203  _203     ; Print SMALL PIT IN CORNER OF ROOM.
3CF5: <span class="sg_value">{{value}}</span> 1B B4  ; <span class="sg_value">{{decode}}</span>  _z       ; Room with music (init to room 16 to 39). The sprite can't move objects here.
3CF8: E8 1D 2D  ; 232  _232     ; _232 If we came south to this room and carrying pendant move us near start and random room for pendant.
3CFB: 00
<h3>Object Data</h3> 
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
3CFC: <span class="sg_value">{{mvalue}}</span>  ; 1 "FOOD"         <span class="sg_value">{{decode}}</span>
3CFF: <span class="sg_value">{{mvalue}}</span>  ; 2 "BOTTLE"       <span class="sg_value">{{decode}}</span>
3D02: <span class="sg_value">{{mvalue}}</span>  ; 3 "DAGGER"       <span class="sg_value">{{decode}}</span>
3D05: <span class="sg_value">{{mvalue}}</span>  ; 4 "MACE"         <span class="sg_value">{{decode}}</span>
3D08: <span class="sg_value">{{mvalue}}</span>  ; 5 "AX"           <span class="sg_value">{{decode}}</span>
3D0B: <span class="sg_value">{{mvalue}}</span>  ; 6 "SWORD"        <span class="sg_value">{{decode}}</span>
3D0E: <span class="sg_value">{{mvalue}}</span>  ; 7 "SHIELD"       <span class="sg_value">{{decode}}</span>
3D11: <span class="sg_value">{{mvalue}}</span>  ; 8 "FLUTE"        <span class="sg_value">{{decode}}</span>
3D14: <span class="sg_value">{{mvalue}}</span>  ; 9 "MUSHROOM"     <span class="sg_value">{{decode}}</span>
3D17: <span class="sg_value">{{mvalue}}</span>  ; 10 "PENDANT"     <span class="sg_value">{{decode}}</span>
3D1A: <span class="sg_value">{{mvalue}}</span>  ; 11 "SCEPTER"     <span class="sg_value">{{decode}}</span>
3D1D: <span class="sg_value">{{mvalue}}</span>  ; 12 "LAMP"        <span class="sg_value">{{decode}}</span>
3D20: <span class="sg_value">{{mvalue}}</span>  ; 13 "BASKET"      <span class="sg_value">{{decode}}</span>
3D23: <span class="sg_value">{{mvalue}}</span>  ; 14 "PARCHMENT"   <span class="sg_value">{{decode}}</span>
3D26: <span class="sg_value">{{mvalue}}</span>  ; 15 "VIAL"        <span class="sg_value">{{decode}}</span>
3D29: <span class="sg_value">{{mvalue}}</span>  ; 16 "URN"         <span class="sg_value">{{decode}}</span>
3D2C: <span class="sg_value">{{mvalue}}</span>  ; 17 "TALISMAN"    <span class="sg_value">{{decode}}</span>
3D2F: <span class="sg_value">{{mvalue}}</span>  ; 18 "SCROLL"      <span class="sg_value">{{decode}}</span>
3D32: <span class="sg_value">{{mvalue}}</span>  ; 19 "GOBLET"      <span class="sg_value">{{decode}}</span>
3D35: <span class="sg_value">{{mvalue}}</span>  ; 20 "SKULL"       <span class="sg_value">{{decode}}</span>
3D38: <span class="sg_value">{{mvalue}}</span>  ; 21 "SCARAB"      <span class="sg_value">{{decode}}</span>
3D3B: <span class="sg_value">{{mvalue}}</span>  ; 22 "JEWELBOX"    <span class="sg_value">{{decode}}</span>
3D3E: <span class="sg_value">{{mvalue}}</span>  ; 23 "TABLET"      <span class="sg_value">{{decode}}</span>
3D41: <span class="sg_value">{{mvalue}}</span>  ; 24 "ROPE"        <span class="sg_value">{{decode}}</span>
3D44: <span class="sg_value">{{mvalue}}</span>  ; 25 "SPRITE"      <span class="sg_value">{{decode}}</span>
3D47: <span class="sg_value">{{mvalue}}</span>  ; 26 "TROGLODYTE"  <span class="sg_value">{{decode}}</span>
3D4A: <span class="sg_value">{{mvalue}}</span>  ; 27 "SCORPION"    <span class="sg_value">{{decode}}</span>
3D4D: <span class="sg_value">{{mvalue}}</span>  ; 28 "NYMPH"       <span class="sg_value">{{decode}}</span>
3D50: <span class="sg_value">{{mvalue}}</span>  ; 29 "SATYR"       <span class="sg_value">{{decode}}</span>
3D53: <span class="sg_value">{{mvalue}}</span>  ; 30 "MINOTAUR"    <span class="sg_value">{{decode}}</span>
3D56: <span class="sg_value">{{mvalue}}</span>  ; 31 "ORACLE"      <span class="sg_value">{{decode}}</span>
3D59: <span class="sg_value">{{mvalue}}</span>  ; 32 "GOLD"        <span class="sg_value">{{decode}}</span>
3D5C: <span class="sg_value">{{mvalue}}</span>  ; 33 "SILVER"      <span class="sg_value">{{decode}}</span>
3D5F: <span class="sg_value">{{mvalue}}</span>  ; 34 "DIAMOND"     <span class="sg_value">{{decode}}</span>
3D62: <span class="sg_value">{{mvalue}}</span>  ; 35 "SPELLBOOK"   <span class="sg_value">{{decode}}</span>
3D65: <span class="sg_value">{{mvalue}}</span>  ; 36 "RUBY"        <span class="sg_value">{{decode}}</span>
3D68: <span class="sg_value">{{mvalue}}</span>  ; 37 "FLEECE"      <span class="sg_value">{{decode}}</span>
3D6B: <span class="sg_value">{{mvalue}}</span>  ; 38 "TIARA"       <span class="sg_value">{{decode}}</span>
3D6E: <span class="sg_value">{{mvalue}}</span>  ; 39 "POWDER"      <span class="sg_value">{{decode}}</span>
3D71: <span class="sg_value">{{mvalue}}</span>  ; 40 "AMULET"      <span class="sg_value">{{decode}}</span>
3D74: <span class="sg_value">{{mvalue}}</span>  ; 41 "POTION"      <span class="sg_value">{{decode}}</span>
3D77: <span class="sg_value">{{mvalue}}</span>  ; 42 "POWERRING"   <span class="sg_value">{{decode}}</span>
3D7A: <span class="sg_value">{{mvalue}}</span>  ; 43 "LIGHTRING"   <span class="sg_value">{{decode}}</span>
3D7D: <span class="sg_value">{{mvalue}}</span>  ; 44 "TRUTHRING"   <span class="sg_value">{{decode}}</span>
3D80: <span class="sg_value">{{mvalue}}</span>  ; 45 "CROWN"       <span class="sg_value">{{decode}}</span>
3D83: <span class="sg_value">{{mvalue}}</span>  ; 46 "OPAL"        <span class="sg_value">{{decode}}</span>
3D86: <span class="sg_value">{{mvalue}}</span>  ; 47 "SAPPHIRE"    <span class="sg_value">{{decode}}</span>
3D89: <span class="sg_value">{{mvalue}}</span>  ; 48 "NORTH"       <span class="sg_value">{{decode}}</span>
3D8C: <span class="sg_value">{{mvalue}}</span>  ; 49 "NORTH"       <span class="sg_value">{{decode}}</span>
3D8F: <span class="sg_value">{{mvalue}}</span>  ; 50 "NORTH"       <span class="sg_value">{{decode}}</span>
3D92: <span class="sg_value">{{mvalue}}</span>  ; 51 "NORTH"       <span class="sg_value">{{decode}}</span>
3D95: <span class="sg_value">{{mvalue}}</span>  ; 52 "NORTH"       <span class="sg_value">{{decode}}</span>
3D98: <span class="sg_value">{{mvalue}}</span>  ; 53 "NORTH"       <span class="sg_value">{{decode}}</span>
3D9B: <span class="sg_value">{{mvalue}}</span>  ; 54 "NORTH"       <span class="sg_value">{{decode}}</span>
3D9E: <span class="sg_value">{{mvalue}}</span>  ; 55 "VETAR"       <span class="sg_value">{{decode}}</span>
3DA1: <span class="sg_value">{{mvalue}}</span>  ; 56 "MITRA"       <span class="sg_value">{{decode}}</span>
3DA4: <span class="sg_value">{{mvalue}}</span>  ; 57 "OKKAN"       <span class="sg_value">{{decode}}</span>
3DA7: <span class="sg_value">{{mvalue}}</span>  ; 58 "AKHIROM"     <span class="sg_value">{{decode}}</span>
3DAA: <span class="sg_value">{{mvalue}}</span>  ; 59 "NERGAL"      <span class="sg_value">{{decode}}</span>
3DAD: <span class="sg_value">{{mvalue}}</span>  ; 60 "BELROG"      <span class="sg_value">{{decode}}</span>
3DB0: <span class="sg_value">{{mvalue}}</span>  ; 61 "CROM"        <span class="sg_value">{{decode}}</span>
3DB3: <span class="sg_value">{{mvalue}}</span>  ; 62 "ISHTAR"      <span class="sg_value">{{decode}}</span>
;
3DB6: 00 FF     ; End of list marker
<h3>Natural Passages</h3>
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
<h3>Blocked Passages</h3>
; These appear on the map above

; Floor 1
3EB8: <span class="sg_value">{{decode}}</span>
3EC0: <span class="sg_value">{{mvalue}}</span>
3EC8: <span class="sg_value">{{mvalue}}</span>
3ED0: <span class="sg_value">{{mvalue}}</span>
3ED8: <span class="sg_value">{{mvalue}}</span>
3EE0: <span class="sg_value">{{mvalue}}</span>
3EE8: <span class="sg_value">{{mvalue}}</span>
3EF0: <span class="sg_value">{{mvalue}}</span>

; Floor 2
3EF8: <span class="sg_value">{{mvalue}}</span>
3F00: <span class="sg_value">{{mvalue}}</span>
3F08: <span class="sg_value">{{mvalue}}</span>
3F10: <span class="sg_value">{{mvalue}}</span>
3F18: <span class="sg_value">{{mvalue}}</span>
3F20: <span class="sg_value">{{mvalue}}</span>
3F28: <span class="sg_value">{{mvalue}}</span>
3F30: <span class="sg_value">{{mvalue}}</span>

; Floor 3
3F38: <span class="sg_value">{{mvalue}}</span>
3F40: <span class="sg_value">{{mvalue}}</span>
3F48: <span class="sg_value">{{mvalue}}</span>
3F50: <span class="sg_value">{{mvalue}}</span>
3F58: <span class="sg_value">{{mvalue}}</span>
3F60: <span class="sg_value">{{mvalue}}</span>
3F68: <span class="sg_value">{{mvalue}}</span>
3F70: <span class="sg_value">{{mvalue}}</span>

; Floor 4
3F78: <span class="sg_value">{{mvalue}}</span>
3F80: <span class="sg_value">{{mvalue}}</span>
3F88: <span class="sg_value">{{mvalue}}</span>
3F90: <span class="sg_value">{{mvalue}}</span>
3F98: <span class="sg_value">{{mvalue}}</span>
3FA0: <span class="sg_value">{{mvalue}}</span>
3FA8: <span class="sg_value">{{mvalue}}</span>
3FB0: <span class="sg_value">{{mvalue}}</span>
<h3>Protection Lists</h3> 
3FB8: 1A              ; TROGLODYTE
3FB9: 43 07 3B FF     ;   DAGGER (plus bits), SHIELD, NERGAL
3FBD: 1D              ; SATYR
3FBE: 23 77 FF        ;   SPELLBOOK, VETAR (plus bits)
3FC1: 1E              ; MINOTAUR
3FC2: 45 3B FF        ;   AX (plus bits), NERGAL
3FC5: 1B              ; SCORPION
3FC6: 48 3B FF        ;   FLUTE (plus bits), NERGAL
3FC9: 1C              ; NYMPH
3FCA: 48 39 FF        ;   FLUTE (plus bits), OKKAN
3FCD: 19              ; SPRITE
3FCE: 54 2A FF        ;   SKULL (plus bits), POWERRING
3FD1: 06              ; SWORD
3FD2: 0E FF           ;   PARCHMENT
3FD4: 0F              ; VIAL
3FD5: 09 77 FF        ;   MUSHROOM, VETAR (plus bits)
3FD8: 07              ; SHIELD
3FD9: 06 FF           ;   SWORD
3FDB: 14              ; SKULL
3FDC: 0B FF           ;   SCEPTER
3FDE: 2A              ; POWERRING
3FDF: 07 0B 0E 79 FF  ;   SHIELD, SCEPTER, PARCHMENT, OKKAN (plus bits)
3FE4: 2B              ; LIGHTRING
3FE5: 2A 7D 11 FF     ;   POWERRING, CROM (plus bits), TALISMAN
3FE9: 2C              ; TRUTHRING
3FEA: 2B 08 7A FF     ;   LIGHTRING, FLUTE, AKHIROM (plus bits)
3FEE: 23              ; SPELLBOOK
3FEF: 09 13 7C FF     ;   MUSHROOM, GOBLET, BELROG (plus bits)

TODO show any data not used but written
```

```html
</div>
```