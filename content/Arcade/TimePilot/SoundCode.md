![Sound Board](TimePilot.jpg)

# Time Pilot sound board

>>> cpu Z80

>>> memoryTable hard 
[Hardware Info](SoundHardware.md)

>>> memoryTable ram 
[RAM Usage](SoundRAMUse.md)

1982 by Centuri/Konami

```
TO DO:
  - Decompose music script into command text

; Z80 CPU and 2 AY-3-8910 Sound Chips
; The sound board receives commands from the game board through
; port A of one sound chip. The upper nibble of Port B is connected
; to an oscillator and drives sound timing.
;
; Sound board oscillator is 14.318MHz. The CPU and sound chips use
; the same division ... 14.31818 / 8 = 1.789772.
;
; The timer on the upper four bits of Port B reaches 0 at the main
; clock divided by 10240 (1024*10).
;
; Processing loop = 1.789772MHz / 10240 = 174.782421875Hz (0.005721399 sec per tick)
```

# Sound Commands

```
; First number is command number
; Second is filter-capacitor configuration
;
; 00   Stop all sounds
; 01 0 Coin 
; 02 0 Plane fire
; 03 0 1910 bomb
; 04 1 Missile launch
; 05 0 UFO shot
; 06 0 Missile (continuous)
; 07 0 User Fire
; 08 1 Enemy Explosion Component (thud)
; 09 1 Enemy Explosion Component (white-noise)
; 0A 0 Tracker or Bomb Explosion
; 0B 0 Squad Appears
; 0C 1 1st boss (blimp)
; 0D 1 2nd boss (jet)
; 0E 1 3rd boss (helicopter)
; 0F 1 4th boss (super jet)
; 10 1 5th boss (mother ship)
; 11 1 User explosion component
; 12 1 User explosion component
; 13 2 User explosion component
; 14 2 User explosion component
; 15 1 User explosion component
; 16 0 Pickup parachute
; 17 1 Free man
; 18 0 Time jump 1
; 19 0 Time jump 2
; 1A 0 Initialize song 2
; 1B 1 Initialize song 1
; 1C 0 Initialize music D1
; 1D 0 Initialize music D2
; 1E 0 Initialize music D3
; 1F 0 Initialize music D4
; 20 0 Initialize music D5
```

# Start

```code
Start: 
; Reset/Startup
0000: 21 00 30        LD      HL,$3000            ; Command buffer
0003: 06 00           LD      B,$00               ; Fill value
0005: C3 9B 00        JP      $009B               ; Continue initialization
```

# AYChipIO

```code
RST8:
; Read CHIP0 register. A=register, return in A
0008: 32 00 50        LD      ($5000),A           ; Store the register number
000B: 3A 00 40        LD      A,($4000)           ; Read the value
000E: C9              RET                         ; Done
000F: FF              RST     $38                 ; Filler to align RST routines

RST10:
; Read CHIP1 register. A=register, retun in A
0010: 32 00 70        LD      ($7000),A           ; Store the register number
0013: 3A 00 60        LD      A,($6000)           ; Read the value
0016: C9              RET                         ; Done
0017: FF              RST     $38                 ; Filler to align RST routines

RST18:
; Write CHIP0 register. A=register, C=value
0018: 32 00 50        LD      ($5000),A           ; Store register number
001B: 79              LD      A,C                 ; Write ...
001C: 32 00 40        LD      ($4000),A           ; ... value
001F: C9              RET                         ; Done

RST20:
; Write CHIP1 register. A=register, C=value
0020: 32 00 70        LD      ($7000),A           ; Store register number
0023: 79              LD      A,C                 ; Write ...
0024: 32 00 60        LD      ($6000),A           ; ... value
0027: C9              RET                         ; Done

; Vector to desired function indexed by A
; HL = address table
; A  = index
0028: 87              ADD     A,A                 ; *2
0029: 85              ADD     A,L                 ; Add to offset
002A: 6F              LD      L,A                 ; Set LSB of pointer
002B: 7C              LD      A,H                 ; Carry into ...
002C: CE 00           ADC     A,$00               ; ... MSB of pointer
002E: 67              LD      H,A                 ; Set MSB of pointer
002F: 7E              LD      A,(HL)              ; Get LSB of address
0030: 23              INC     HL                  ; Next in table
0031: 66              LD      H,(HL)              ; Get MSB of address
0032: 6F              LD      L,A                 ; Get LSB of address
0033: E9              JP      (HL)                ; Jump to routine
0034: FF              RST     $38                 ; Filler ...
0035: FF              RST     $38                 ; ...
0036: FF              RST     $38                 ; ...
0037: FF              RST     $38                 ; ...
```

# Interrupt

```code
InterruptService: 
; Called when the main CPU signals a new sound command.
; Switch banks and call the command fetch routine
0038: D9              EXX                         ; Switch banks B-L
0039: 08              EX      AF,AF'              ; Switch AF banks
003A: CD 40 00        CALL    $0040               ;{CommandBuffer} Make the call
003D: 08              EX      AF,AF'              ; Set the AF banks back
003E: D9              EXX                         ; Set the B-L banks back
003F: C9              RET                         ; Done
```

# Command Buffer

The command Buffer is kept at 3000 and contains 6 2-byte entries.
That's one entry for each hardware voice. The first of the two 
bytes is the command. A zero marks an available slot. The second byte 
indicates initialization status. 0=not initialized, 1=initialized. 
Note that entries are removed by setting them to 0000, which clears
the initialized-flag for the next command.

The main CPU writes the command to Port A of sound chip 0 and 
triggers an interrupt in this code.

If the upper bit of the command is set, then that command is removed 
from the buffer if it is still playing. Command values above 0x20 are 
ignored. 

Command 0 clears all six command slots thus stopping all sound.

If a command is already running, it is restarted.

If the command buffer is full, then the command numbers are used as 
priorities. The higher the command number, the higher the priority. 
If all commands in the buffer are of higher priority than the new command,
then the new command is ignored. Otherwise the new command replaces the 
lowest priority command in the buffer.

```code
HandleCommand: 
; Fetch a command from the port and place it in the
; command buffer.
0040: 3E 0E           LD      A,$0E               ; Port A
0042: CF              RST     $08                 ; Read CHIP0 Port A
0043: B7              OR      A                   ; If zero then ...
0044: 28 2F           JR      Z,$75               ; ... clear the entire buffer and out
0046: 57              LD      D,A                 ; Hang on to command
0047: E6 7F           AND     $7F                 ; Mask off upper bit
0049: FE 21           CP      $21                 ; Compare command to 21
004B: D0              RET     NC                  ; Ignore invalid commands (above 20)
004C: CB 7A           BIT     7,D                 ; Is the upper bit set?
004E: 20 42           JR      NZ,$92              ; Yes -- remove the command from the buffer
0050: CD 80 00        CALL    $0080               ; Is the command already in the buffer?
0053: 20 1C           JR      NZ,$71              ; Found ... restart it.
0055: CD 80 00        CALL    $0080               ; Find A=0 (empty slot) in the buffer
0058: 20 16           JR      NZ,$70              ; Found a slot -- store command in buffer
; Find the lowest numbered command
005A: 21 00 30        LD      HL,$3000            ; Buffer
005D: 1E 06           LD      E,$06               ; 6 entries to check
005F: 7E              LD      A,(HL)              ; Get command value
0060: 1D              DEC     E                   ; Count down
0061: 28 08           JR      Z,$6B               ; All checked ... done
0063: 2C              INC     L                   ; Bump to next ...
0064: 2C              INC     L                   ; ... entry
0065: BE              CP      (HL)                ; Compare current lowest with next entry
0066: 38 F8           JR      C,$60               ; Next entry is higher -- keep our lowest
0068: C3 5F 00        JP      $005F               ; New lowest value
;
006B: BA              CP      D                   ; Is the new command even lower?
006C: D0              RET     NC                  ; Yes -- ignore the command
; Find entry, replace type with D and clear second byte
006D: CD 80 00        CALL    $0080               ; Find entry
0070: 72              LD      (HL),D              ; Store D
0071: 2C              INC     L                   ; Second byte in entry
0072: 36 00           LD      (HL),$00            ; Flag command needs initializing
0074: C9              RET                         ; Done

StopAllCommands:
0075: 21 00 30        LD      HL,$3000            ; Clear 13 bytes ...
0078: 06 0C           LD      B,$0C               ; ... starting at ...
007A: AF              XOR     A                   ; ...
007B: 77              LD      (HL),A              ; ...
007C: 2C              INC     L                   ; ...
007D: 10 FC           DJNZ    $7B                 ; ... 3000
007F: C9              RET                         ; Done

FindCommand:
; Find entry A in buffer. Return slot number (1,2,3,4,5,6) and HL if found.
; If not found, return 0
0080: 21 00 30        LD      HL,$3000            ; Buffer area
0083: 06 06           LD      B,$06               ; 6 entries to check
0085: 0E 07           LD      C,$07               ; Subtraction constant (never changes here)
0087: BE              CP      (HL)                ; Is this the same command?
0088: 28 05           JR      Z,$8F               ; Yes -- done
008A: 2C              INC     L                   ; Bump to ...
008B: 2C              INC     L                   ; ... next entry
008C: 10 F9           DJNZ    $87                 ; Check all entries
008E: 41              LD      B,C                 ; Not found -- ends up becoming 0
008F: 79              LD      A,C                 ; Subtract remaining counter ...
0090: 90              SUB     B                   ; ... from 7
0091: C9              RET                         ; Return slot number 0 or 1-6

; Remove entry from buffer
0092: CD 80 00        CALL    $0080               ; Find entry
0095: C8              RET     Z                   ; Not found -- out
0096: AF              XOR     A                   ; Fast 0
0097: 77              LD      (HL),A              ; Clear ...
0098: 2C              INC     L                   ; ... entry ...
0099: 77              LD      (HL),A              ; ... from buffer.
009A: C9              RET                         ; Out

; Initialization continued.
; Clear RAM
009B: 70              LD      (HL),B              ; Store 0
009C: 23              INC     HL                  ; Bump pointer
009D: 7C              LD      A,H                 ; Clear until ...
009E: FE 34           CP      $34                 ; ... done
00A0: 20 F9           JR      NZ,$9B              ; Loop back
00A2: F9              LD      SP,HL               ; Set SP to 3400
00A3: ED 56           IM      1                   ; Set interrupt MODE 1 (always vector to 0038)
00A5: 21 00 80        LD      HL,$8000            ; All cap filters zero plus upper bit set.
00A8: 22 0C 30        LD      ($300C),HL          ; Keep up with write-only value
00AB: 77              LD      (HL),A              ; All caps disconnected from the channels

; Initialize sound chips
00AC: 0E 00           LD      C,$00               ; Amplitude value 0
00AE: 16 06           LD      D,$06               ; 6 voices
00B0: 7A              LD      A,D                 ; Pass to function
00B1: CD 9C 01        CALL    $019C               ; Channel x to 0. (Amplitude to silence.)
00B4: 15              DEC     D                   ; Silence all ...
00B5: 20 F9           JR      NZ,$B0              ; ... six voices
00B7: 0E 38           LD      C,$38               ; Both IO Ports IN, Tones only on ...
00B9: 3E 07           LD      A,$07               ; ... all voices.
00BB: DF              RST     $18                 ; Configure AY38910 chip 0
00BC: 3E 07           LD      A,$07               ; "Enable" register again
00BE: E7              RST     $20                 ; Configure AY38910 chip 1
```

# Main Loop

```code
MainLoop:
; Use the upper nibble of chip 0 port B as a counter. When it reaches 0,
; then process all the voices. This is happens at approximately 175Hz.
00BF: FB              EI                          ; Enable interrupts
00C0: 3E 0F           LD      A,$0F               ; Port B
00C2: CF              RST     $08                 ; Read CHIP0 Port B
00C3: E6 F0           AND     $F0                 ; Timer value hit?
00C5: 20 F9           JR      NZ,$C0              ; No -- keep waiting

; Process Entry Index 1
00C7: F3              DI                          ; Disable interrupts
00C8: 3E 01           LD      A,$01               ; Voice index 1
00CA: 32 0E 30        LD      ($300E),A           ; Hang onto it
00CD: 3A 01 30        LD      A,($3001)           ; First voice, 2nd byte
00D0: B7              OR      A                   ; Set flags about 2nd byte
00D1: 3A 00 30        LD      A,($3000)           ; Get command (no flags)
00D4: 28 06           JR      Z,$DC               ; 2nd byte == 0
00D6: CD 7F 01        CALL    $017F               ; Continue command
00D9: C3 DF 00        JP      $00DF               ; Skip over
00DC: CD 69 01        CALL    $0169               ; Initialize command
00DF: FB              EI                          ; Enable interrupts
00E0: 00              NOP                         ; Probably to make all the index handlers the ...
00E1: 00              NOP                         ; ... same number of bytes (the last one is 2 bytes longer).

; Process Entry Index 2 (see Index 1 above)
00E2: F3              DI                          ;
00E3: 3E 02           LD      A,$02               ;
00E5: 32 0E 30        LD      ($300E),A           ;
00E8: 3A 03 30        LD      A,($3003)           ;
00EB: B7              OR      A                   ;
00EC: 3A 02 30        LD      A,($3002)           ;
00EF: 28 06           JR      Z,$F7               ; Same as index 1
00F1: CD 7F 01        CALL    $017F               ;
00F4: C3 FA 00        JP      $00FA               ;
00F7: CD 69 01        CALL    $0169               ;
00FA: FB              EI                          ;
00FB: 00              NOP                         ;
00FC: 00              NOP                         ;

; Process Entry Index 3 (see Index 1 above)
00FD: F3              DI                          ;
00FE: 3E 03           LD      A,$03               ;
0100: 32 0E 30        LD      ($300E),A           ;
0103: 3A 05 30        LD      A,($3005)           ;
0106: B7              OR      A                   ;
0107: 3A 04 30        LD      A,($3004)           ;
010A: 28 06           JR      Z,$112              ; Same as index 1
010C: CD 7F 01        CALL    $017F               ;
010F: C3 15 01        JP      $0115               ;
0112: CD 69 01        CALL    $0169               ;
0115: FB              EI                          ;
0116: 00              NOP                         ;
0117: 00              NOP                         ;

; Process Entry Index 4 (see Index 1 above)
0118: F3              DI                          ;
0119: 3E 04           LD      A,$04               ;
011B: 32 0E 30        LD      ($300E),A           ;
011E: 3A 07 30        LD      A,($3007)           ;
0121: B7              OR      A                   ;
0122: 3A 06 30        LD      A,($3006)           ;
0125: 28 06           JR      Z,$12D              ;
0127: CD 7F 01        CALL    $017F               ; Same as index 1
012A: C3 30 01        JP      $0130               ;
012D: CD 69 01        CALL    $0169               ;
0130: FB              EI                          ;
0131: 00              NOP                         ;
0132: 00              NOP                         ;

; Process Entry Index 5 (see Index 1 above)
0133: F3              DI                          ;
0134: 3E 05           LD      A,$05               ;
0136: 32 0E 30        LD      ($300E),A           ;
0139: 3A 09 30        LD      A,($3009)           ;
013C: B7              OR      A                   ;
013D: 3A 08 30        LD      A,($3008)           ;
0140: 28 06           JR      Z,$148              ; Same as index 1
0142: CD 7F 01        CALL    $017F               ;
0145: C3 4B 01        JP      $014B               ;
0148: CD 69 01        CALL    $0169               ;
014B: FB              EI                          ;
014C: 00              NOP                         ;
014D: 00              NOP                         ;

; Process Entry Index 6 (see Index 1 above)
014E: F3              DI                          ;
014F: 3E 06           LD      A,$06               ;
0151: 32 0E 30        LD      ($300E),A           ;
0154: 3A 0B 30        LD      A,($300B)           ;
0157: B7              OR      A                   ;
0158: 3A 0A 30        LD      A,($300A)           ;
015B: 28 06           JR      Z,$163              ; Same as index 1
015D: CD 7F 01        CALL    $017F               ;
0160: C3 BF 00        JP      $00BF               ; Back to the main loop
0163: CD 69 01        CALL    $0169               ;

; The upper nibble in B should be non-zero by now.
0166: C3 BF 00        JP      $00BF               ;{MainLoop} Continue main loop

InitCommand:
; Initialize command and flag it initialized
; Vector to command. If return is 0, set second byte to 1. If return
; is not 0, remove the command from the buffer.
0169: 21 92 0A        LD      HL,$0A92            ; Jump table
016C: EF              RST     $28                 ; Vector to address A in table HL
016D: B7              OR      A                   ; Test return
016E: 20 17           JR      NZ,$187             ; Remove the command
0170: 21 01 30        LD      HL,$3001            ; Command buffer (2nd bytes)
0173: 3A 0E 30        LD      A,($300E)           ; Index of command
0176: 3D              DEC     A                   ; Convert to ...
0177: 87              ADD     A,A                 ; ... pointer
0178: 5F              LD      E,A                 ; LSB
0179: 16 00           LD      D,$00               ; MSB=0
017B: 19              ADD     HL,DE               ; Pointer to command 2nd byte
017C: 36 01           LD      (HL),$01            ; Set second byte to 1
017E: C9              RET                         ; Done

ContinueCommand:
; Continue processing a command
; Vector to command. If return is 0, leave buffer alone. If return
; is not 0, remove command from buffer.
; The vector table for "continues" does have an entry for "0" even
; though the initialization does (it clears the voice). I would have
; pointed the "continue" for command 0 at a return-zero for consistency. Then
; no special check would be needed here.
017F: B7              OR      A                   ; If slot is empty ...
0180: C8              RET     Z                   ; ... do nothing
0181: 21 D4 0A        LD      HL,$0AD4            ; Jump table
0184: EF              RST     $28                 ; Vector to address A in table HL
0185: B7              OR      A                   ; Test return
0186: C8              RET     Z                   ; If zero -- out
;
0187: 21 00 30        LD      HL,$3000            ; Command buffer
018A: 3A 0E 30        LD      A,($300E)           ; Index of command
018D: 3D              DEC     A                   ; Convert to ...
018E: 87              ADD     A,A                 ; ... pointer
018F: 4F              LD      C,A                 ; LSB
0190: 06 00           LD      B,$00               ; MSB=0
0192: 09              ADD     HL,BC               ; Pointer to command
0193: 70              LD      (HL),B              ; Clear command type
0194: 2C              INC     L                   ; Next byte
0195: 70              LD      (HL),B              ; Clear second byte
0196: C9              RET                         ; Done
```

# Command 00 Silence

```code
Command00: 
; Silence
; Initialize Routine Vector 00 (Silence the channel)

0197: 0E 00           LD      C,$00               ; Silence the voice
;  Write to amplitude control of given voice
0199: 3A 0E 30        LD      A,($300E)           ; Get voice number
019C: FE 04           CP      $04                 ; Voice 4-6
019E: 30 05           JR      NC,$1A5             ; Yes -- do chip 1
01A0: C6 07           ADD     A,$07               ; Add 7 (8,9, or 10)
01A2: C3 18 00        JP      $0018               ; Write C to reg A chip 0
01A5: C6 04           ADD     A,$04               ; Add 4 (8,9, or 10)
01A7: C3 20 00        JP      $0020               ; Write C to reg A chip 1

; Write to tone registers for the specified voice.
; Write HL = value, voice (1-3 Chip0, 4-6 Chip1)
01AA: 3A 0E 30        LD      A,($300E)           ; Get register
01AD: FE 04           CP      $04                 ; Register 4-6
01AF: 30 0B           JR      NC,$1BC             ; Yes ... next chip
01B1: 3D              DEC     A                   ; -1
01B2: 87              ADD     A,A                 ; *2
01B3: 47              LD      B,A                 ; Hold onto register
01B4: 4D              LD      C,L                 ; Value
01B5: DF              RST     $18                 ; Write Chip 0
01B6: 78              LD      A,B                 ; Restore register
01B7: 3C              INC     A                   ; Next
01B8: 4C              LD      C,H                 ; Value
01B9: C3 18 00        JP      $0018               ; Write Chip 0
01BC: D6 04           SUB     $04                 ; Registers in chip 1
01BE: 87              ADD     A,A                 ; ...
01BF: 47              LD      B,A                 ; ...
01C0: 4D              LD      C,L                 ; ...
01C1: E7              RST     $20                 ; ...
01C2: 78              LD      A,B                 ; ...
01C3: 3C              INC     A                   ; ...
01C4: 4C              LD      C,H                 ; ...
01C5: C3 20 00        JP      $0020               ; Done
```

# FilterCaps

There are two capacitors that can be switched onto each audio channel
to ground. The MSB bit set to one selects a 0.22 and the LSB bit set selects
a 0.047 cap. Most effects just switch out the caps (writing 00), but the
explosion effects switch in one or the other (never both).

  * V1 1000xxxxAAxxxxxx
  * V2 1000xxAAxxxxxxxx
  * V3 1000AAxxxxxxxxxx
  * V4 1000xxxxxxxxxxAA
  * V5 1000xxxxxxxxAAxx
  * V6 1000xxxxxxAAxxxx

```code
SetFilterCaps:
; Reverse A bits
01C8: 01 FC FF        LD      BC,$FFFC            ; 11111111 11111100
01CB: 21 00 00        LD      HL,$0000            ; Clear HL
01CE: 1F              RRA                         ; Bit 0 ...
01CF: CB 15           RL      L                   ; ... into L
01D1: 1F              RRA                         ; Bit 1 ...
01D2: CB 15           RL      L                   ; ... into L
; Move bits and calculate mask
; V=1 HL*=64    BC=1111111100111111
;   2 HL*=256   BC=1111110011111111
;   3 HL*=1024  BC=1111001111111111
;   4 HL*=1     BC=1111111111111100
;   5 HL*=4     BC=1111111111110011
;   6 HL*=16    BC=1111111111001111
01D4: 3A 0E 30        LD      A,($300E)           ; Voice number
01D7: C6 02           ADD     A,$02               ; 2 bits in field
01D9: FE 06           CP      $06                 ; Split the field map
01DB: 38 04           JR      C,$1E1              ; ...
01DD: D6 06           SUB     $06                 ; ...
01DF: 28 0A           JR      Z,$1EB              ; ...
01E1: 87              ADD     A,A                 ; = number of moves
01E2: 29              ADD     HL,HL               ; HL * 2
01E3: 37              SCF                         ; Set carry flag
01E4: CB 11           RL      C                   ; Roll ...
01E6: CB 10           RL      B                   ; ... the mask
01E8: 3D              DEC     A                   ; Position counter
01E9: 20 F7           JR      NZ,$1E2             ; Complete the pattern
; CurrentValue = (CurrentValue & Mask) | HL
01EB: EB              EX      DE,HL               ; HL->DE
01EC: 2A 0C 30        LD      HL,($300C)          ; Old value
01EF: 7D              LD      A,L                 ; LSB
01F0: A1              AND     C                   ; Mask
01F1: B3              OR      E                   ; OR in old value
01F2: 6F              LD      L,A                 ; New LSB
01F3: 7C              LD      A,H                 ; MSB
01F4: A0              AND     B                   ; Mask
01F5: B2              OR      D                   ; OR in old value
01F6: 67              LD      H,A                 ; New MSB
01F7: 22 0C 30        LD      ($300C),HL          ; New configuration value
01FA: 77              LD      (HL),A              ; Write the new filter value (the address value) ...
01FB: C9              RET                         ; ... to the latches
```

# Music Processing

Offset 00: The first byte is the currently playing note. The upper 3 bits 
define the duration: 7=64th note, 6=32nd, 5=16th, 4=8th, 3=quarter note, 
2=half note, and 1=whole note. A value of 0 is not allowed.

01: The second byte is the base delay for all notes in the song. This is the reload
value of the delay counter. Thus a lower value speeds up all notes in the song.
This value remains constant while the song plays.

The lower 5 bits of the first byte define the note number. This is added to the
song's base note number in bytes 4 and 5. Thus some songs can be higher on the
scale than other songs. This value changes with each new note in the song.

A note value of all 0s is a rest.

A note value of all 1s indicates a special music command. The command is processed
and the next note is immediately processed. This allows several special commands
to be handled at once. If the note value is all 1s then the MSB is the special
command. The next value in the song is the data used to:

  * MSB=0 Load base note table pointer from music
  *     1 Load base delay from music
  *     2 Load volume from music
  *     3 Load volume modification from music
  *     4 End of song
  *     5 End of song
  *     6 Jump to new music address
  *     7 End of song

02,03: The Music Pointer points to the next byte in the song to process. This is the
song's "program counter". This value changes as the song moves from note to note.

04,05: The Base Note Table Pointer points to the start of an octave in the note table. 
All notes in the song are relative to this base. This value remains constant while
the song plays. 

06: The initial amplitude is the initial volume of each note when the note begins. The
amplitude is modified as the note plays by the value in byte 09. This initial value 
for all notes remains constant while the song plays.

07: The running amplitude is the current volume level of the currently playing note.
This value is modified every other MSB delay count until the note's duration is over
or the value is at a minimum (and thus changing it would wrap the value).

08: This is the duration delay count for the currently playing note. When this value
reaches zero, it is reloaded with the value in 01 and the MSB is decremented. When
the MSB reaches 0, the next note is played.

09: This is the value used to modify each note's amplitude every other MSB tick. This
value remains constant for every note over the entire song.

```code
MusicProcessing:
; Process Music Descriptor
; Amplitude of a note is reduced at a rate of 0.5 the MSB delay.
01FC: DD 35 01        DEC     (IX+$01)            ; Decrement base delay count
01FF: C0              RET     NZ                  ; Not time for new note -- out
0200: DD 7E 08        LD      A,(IX+$08)          ; Reload ...
0203: DD 77 01        LD      (IX+$01),A          ; ... base delay
0206: DD 35 00        DEC     (IX+$00)            ; Decrement MSB of delay
0209: 28 15           JR      Z,$220              ; Load next note
;
020B: DD CB 00 46     BIT     0,(IX+$00)          ; Test bit 0 of MSB of delay
020F: C8              RET     Z                   ; Not time to fool with volume
0210: DD 7E 09        LD      A,(IX+$09)          ; Get volume modifier
0213: B7              OR      A                   ; Test it
0214: C8              RET     Z                   ; No modification ... out
0215: DD 86 07        ADD     A,(IX+$07)          ; Modify current volume.
0218: F8              RET     M                   ; Ignore it if it wrapped
0219: DD 77 07        LD      (IX+$07),A          ; New amplitude
021C: 4F              LD      C,A                 ; To C
021D: C3 99 01        JP      $0199               ; Set amplitude and out
;
; Load next note
0220: DD 6E 02        LD      L,(IX+$02)          ; LSB of music pointer
0223: DD 66 03        LD      H,(IX+$03)          ; MSB of music pointer
0226: 7E              LD      A,(HL)              ; Get next command
0227: 57              LD      D,A                 ; Hang onto it
0228: E6 1F           AND     $1F                 ; Mask out note
022A: 28 24           JR      Z,$250              ; Note 0? Just set delay
022C: FE 1F           CP      $1F                 ; Special command?
022E: 28 37           JR      Z,$267              ; Yes ... process special command.
0230: CD 50 02        CALL    $0250               ; Regular note -- set delay
0233: 7A              LD      A,D                 ; Get note
0234: E6 1F           AND     $1F                 ; Mask off upper 3 bits
0236: 3D              DEC     A                   ; -1 (0 is not a note)
0237: 07              RLCA                        ; *2 (2 bytes per note)
0238: 4F              LD      C,A                 ; Hold it
0239: DD 6E 04        LD      L,(IX+$04)          ; Base pointer into ...
023C: DD 66 05        LD      H,(IX+$05)          ; ... note table
023F: 09              ADD     HL,BC               ; B got set to 0 in the delay set!
0240: 5E              LD      E,(HL)              ; Get tone ...
0241: 23              INC     HL                  ; ... value ...
0242: 56              LD      D,(HL)              ; ... from table
0243: EB              EX      DE,HL               ; To HL
0244: CD AA 01        CALL    $01AA               ; Write tone
0247: DD 4E 06        LD      C,(IX+$06)          ; Get amplitude
024A: DD 71 07        LD      (IX+$07),C          ; Initialize running amplitude
024D: C3 99 01        JP      $0199               ; Set amplitude and out

; Convert next byte to power of 2 and store as delay MSB
0250: 23              INC     HL                  ; Next byte in music
0251: DD 75 02        LD      (IX+$02),L          ; Update ...
0254: DD 74 03        LD      (IX+$03),H          ; ... music pointer
0257: 7A              LD      A,D                 ; Restore command
0258: E6 E0           AND     $E0                 ; Mask off lower 5 bits
025A: 07              RLCA                        ; Move upper three bits ...
025B: 07              RLCA                        ; ...
025C: 07              RLCA                        ; ... to lower bits.
025D: 47              LD      B,A                 ; Save it
025E: 3E 80           LD      A,$80               ; One bit
0260: 07              RLCA                        ; Set bit position ...
0261: 10 FD           DJNZ    $260                ; ... B
0263: DD 77 00        LD      (IX+$00),A          ; Store to MSB delay
0266: C9              RET                         ; Done

; Music byte xxx11111 (special command)
; Vector to function xxx and continue processing
0267: 7A              LD      A,D                 ; Restore command
0268: E6 E0           AND     $E0                 ; Mask off lower bits
026A: 07              RLCA                        ; Move upper ...
026B: 07              RLCA                        ; ... three bits ...
026C: 07              RLCA                        ; ... to low end
026D: 11 20 02        LD      DE,$0220            ; Return to process ...
0270: D5              PUSH    DE                  ; ... next command
0271: 23              INC     HL                  ; Bump music pointer
0272: 5D              LD      E,L                 ; Hold ...
0273: 54              LD      D,H                 ; ... pointer
0274: 23              INC     HL                  ; Next
0275: DD 75 02        LD      (IX+$02),L          ; Save ...
0278: DD 74 03        LD      (IX+$03),H          ; ... music pointer
027B: 21 81 02        LD      HL,$0281            ; Jump table
027E: C3 28 00        JP      $0028               ; Do command and continue with next

; Music commands (DE contains pointer to 2nd byte)
0281: 91 02 ; 0 Load base note table pointer from music
0283: A5 02 ; 1 Load LSB delay from music
0285: B5 02 ; 2 Load amplitude from music
0287: BA 02 ; 3 Load amplitude modification from music
0289: C9 02 ; 4 End of song
028B: C9 02 ; 5 End of song
028D: BF 02 ; 6 Jump to new music address
028F: C9 02 ; 7 End of song

MusicCmd0:
; Load base note table pointer
; 2 bytes
0291: EB              EX      DE,HL               ; Pointer to second byte
0292: 4E              LD      C,(HL)              ; Get second byte
0293: CB 21           SLA     C                   ; *2
0295: 06 00           LD      B,$00               ; MSB = 0
0297: 21 CE 02        LD      HL,$02CE            ; Base pointers
029A: 09              ADD     HL,BC               ; Offset into table
029B: 5E              LD      E,(HL)              ; Get byte
029C: 23              INC     HL                  ; Next
029D: 56              LD      D,(HL)              ; Get byte
029E: DD 73 04        LD      (IX+$04),E          ; Store ...
02A1: DD 72 05        LD      (IX+$05),D          ; ... tone pointer
02A4: C9              RET                         ;

MusicCmd1:
; Load delay from table. ?? why not just store the delay value in the song and
; skip the table lookup?
02A5: EB              EX      DE,HL               ; Second byte pointer
02A6: 4E              LD      C,(HL)              ; Get second byte
02A7: 06 00           LD      B,$00               ; MSB = 0
02A9: 21 66 03        LD      HL,$0366            ; Data
02AC: 09              ADD     HL,BC               ; Point to entry
02AD: 7E              LD      A,(HL)              ; Get data
02AE: DD 77 08        LD      (IX+$08),A          ; Delay
02B1: DD 77 01        LD      (IX+$01),A          ; Delay
02B4: C9              RET                         ; Done

MusicCmd2:
; Load amplitude
02B5: 1A              LD      A,(DE)              ; Get second byte
02B6: DD 77 06        LD      (IX+$06),A          ; Store it to amplitude
02B9: C9              RET                         ; Done

MusicCmd3:
; Set 09 Amplitude modification
02BA: 1A              LD      A,(DE)              ; Get second byte
02BB: DD 77 09        LD      (IX+$09),A          ; Store it to modification value
02BE: C9              RET                         ; Done

MusicCmd6:
; Jump to new music address
02BF: 1A              LD      A,(DE)              ; Get second byte
02C0: DD 77 02        LD      (IX+$02),A          ; Set ...
02C3: 13              INC     DE                  ; ...
02C4: 1A              LD      A,(DE)              ; ...
02C5: DD 77 03        LD      (IX+$03),A          ; ... new pointer
02C8: C9              RET                         ; Done

MusicCmd4:
MusicCmd5:
MusicCmd7:
; End this song
02C9: E1              POP     HL                  ; Clear for return ...
02CA: E1              POP     HL                  ; ... from music routine
02CB: 3E FF           LD      A,$FF               ; Flag end of processing
02CD: C9              RET                         ; Done

BaseNotePtrs:
; Base offsets into note table. The notes in a song are relative
; to these pointers into the note table.
02CE: EE 02  ; Lowest note (Would be G#1)
02D0: F2 02  ; A#1
;
02D2: F6 02  ; C2
02D4: FA 02  ; D2
02D6: FE 02  ; E2
02D8: 02 03  ; F#2
02DA: 06 03  ; G#2
02DC: 0A 03  ; A#2
;
02DE: 0E 03  ; C3
02E0: 12 03  ; D3
02E2: 16 03  ; E3
02E4: 1A 03  ; F#3
02E6: 1E 03  ; G#3
02E8: 22 03  ; A#3
;
02EA: 26 03  ; C4
02EC: 2A 03  ; D4

NoteTable:
; Note Table -- tones for notes on the chromatic scale
; Frequency is 1789772 / (16 * value)
;
;              Value   Freq   MIDI Note      Ideal Freq
02EE: FF 0F  ; 4095    27.31    x  x         x
02F0: F2 07  ; 2034    54.99    33 A1        55.00
02F2: 80 07  ; 1920    58.26    34 A#1/Bb1   58.27
02F4: 14 07  ; 1812    61.73    35 B1        61.74
02F6: AE 06  ; 1710    65.41    36 C2        65.41
02F8: 4E 06  ; 1614    69.30    37 C#2/Db2   69.30
02FA: F3 05  ; 1523    73.44    38 D2        73.42
02FC: 9E 05  ; 1438    77.78    39 D#2/Eb2   77.78
02FE: 4E 05  ; 1358    82.37    40 E2        82.41
0300: 01 05  ; 1281    87.32    41 F2        87.31
0302: B9 04  ; 1209    92.52    42 F#2/Gb2   92.50
0304: 76 04  ; 1142    97.95    43 G2        98.00
0306: 36 04  ; 1078   103.76    44 G#2/Ab2  103.83
0308: F9 03  ; 1017   109.99    45 A2       110.00
030A: C0 03  ;  960   116.52    46 A#2/Bb2  116.54
030C: 8A 03  ;  906   123.46    47 B2       123.47
030E: 57 03  ;  855   130.83    48 C3       130.81
0310: 27 03  ;  807   138.61    49 C#3/Db3  138.59
0312: FA 02  ;  762   146.79    50 D3       146.83
0314: CF 02  ;  719   155.57    51 D#3/Eb3  155.56
0316: A7 02  ;  679   164.74    52 E3       164.81
0318: 81 02  ;  641   174.50    53 F3       174.61
031A: 5D 02  ;  605   184.89    54 F#3/Gb3  185.00
031C: 3B 02  ;  571   195.90    55 G3       196.00
031E: 1B 02  ;  539   207.53    56 G#3/Ab3  207.65
0320: FD 01  ;  509   219.76    57 A3       220.00
0322: E0 01  ;  480   233.04    58 A#3/Bb3  233.08
0324: C5 01  ;  453   246.93    59 B3       246.94
0326: AC 01  ;  428   261.35    60 C4       261.63 (middle C)
0328: 94 01  ;  404   276.88    61 C#4/Db4  277.18
032A: 7D 01  ;  381   293.59    62 D4       293.66
032C: 68 01  ;  360   310.72    63 D#4/Eb4  311.13
032E: 53 01  ;  339   329.97    64 E4       329.63
0330: 40 01  ;  320   349.56    65 F4       349.23
0332: 2E 01  ;  302   370.39    66 F#4/Gb4  369.99
0334: 1D 01  ;  285   392.49    67 G4       392.00
0336: 0D 01  ;  269   415.83    68 G#4/Ab4  415.30
0338: FE 00  ;  254   440.39    69 A4       440.00 (concert pitch)
033A: F0 00  ;  240   466.08    70 A#4/Bb4  466.16
033C: E3 00  ;  227   492.76    71 B4       493.88
033E: D6 00  ;  214   522.71    72 C5       523.25
0340: CA 00  ;  202   553.76    73 C#5/Db5  554.37
0342: BE 00  ;  190   588.74    74 D5       587.33
0344: B4 00  ;  180   621.44    75 D#5/Eb5  622.25
0346: AA 00  ;  170   658.00    76 E5       659.26
0348: A0 00  ;  160   699.12    77 F5       698.46
034A: 97 00  ;  151   740.79    78 F#5/Gb5  739.99
034C: 8F 00  ;  143   782.24    79 G5       783.99
034E: 87 00  ;  135   828.59    80 G#5/Ab   830.61
0350: 7F 00  ;  127   880.79    81 A5       880.00
0352: 78 00  ;  120   932.17    82 A#5/Bb5  932.33
0354: 71 00  ;  113   989.91    83 B5       987.77
0356: 6B 00  ;  107  1045.42    84 C6      1046.50
0358: 65 00  ;  101  1107.53    85 C#6/Db6 1108.73
035A: 5F 00  ;   95  1177.48    86 D6      1174.66
035C: 5A 00  ;   90  1242.89    87 D#6/Eb6 1244.51
035E: 55 00  ;   85  1316.00    88 E6      1318.51
0360: 50 00  ;   80  1398.25    89 F6      1396.91
0362: 4C 00  ;   76  1471.85    90 F#6/Gb6 1479.98
0364: 07 00  ;    7 15980.10    x  x       x

DelayTable:
; 24 fixed base-delay values. ?? The music command could just
; store this one byte value instead of storing a one byte index
; into this table.
0366: 3C 38 34 30 2C 28 24 20 1E 1C 1A 18  
0372: 16 14 12 10 0F 0E 0D 0C 0B 0A 09 08 

InitSong:
; Initialize descriptors for a specified song number in A
037E: 21 B5 03        LD      HL,$03B5            ; Initialization data
0381: 11 0F 30        LD      DE,$300F            ; First music descriptor
0384: 01 32 00        LD      BC,$0032            ; $32 = d50 = 10*5 = 50 bytes (5 descriptors)
0387: ED B0           LDIR                        ; Initialize the data
;
; Song number * 10 (5 music pointers, 2 bytes each)
0389: 87              ADD     A,A                 ; A*2
038A: 4F              LD      C,A                 ; Hold
038B: 87              ADD     A,A                 ; A*4
038C: 87              ADD     A,A                 ; A*8
038D: 81              ADD     A,C                 ; A*10
038E: 4F              LD      C,A                 ; Hold it
038F: 06 00           LD      B,$00               ; MSB = 0
0391: 21 6E 0B        LD      HL,$0B6E            ; Data region
0394: 09              ADD     HL,BC               ; Point to song
0395: 11 11 30        LD      DE,$3011            ; Music pointer descriptor 1
0398: ED A0           LDI                         ; Set ...
039A: ED A0           LDI                         ; ... pointer
039C: 1E 1B           LD      E,$1B               ; Music pointer descriptor 2
039E: ED A0           LDI                         ; Set ...
03A0: ED A0           LDI                         ; ... pointer
03A2: 1E 25           LD      E,$25               ; Music pointer descriptor 3
03A4: ED A0           LDI                         ; Set ...
03A6: ED A0           LDI                         ; ... pointer
03A8: 1E 2F           LD      E,$2F               ; Music pointer descriptor 4
03AA: ED A0           LDI                         ; Set ...
03AC: ED A0           LDI                         ; ... pointer
03AE: 1E 39           LD      E,$39               ; Music pointer descriptor 5
03B0: ED A0           LDI                         ; Set ...
03B2: ED A0           LDI                         ; ... pointer
03B4: C9              RET                         ; Done

SongDescInit:
; Initialization data for music descriptors (10 bytes each)
; Note=Rest, MSB=reload, LSB=reload, AmpMod=-1
03B5: 01 01 00 00 00 00 00 00 00 FF 
03BF: 01 01 00 00 00 00 00 00 00 FF 
03C9: 01 01 00 00 00 00 00 00 00 FF 
03D3: 01 01 00 00 00 00 00 00 00 FF 
03DD: 01 01 00 00 00 00 00 00 00 FF 

; The sounds produced by this code were discovered by modifying
; the game code ROM to play a single sound and go into an infinite
; loop. The modified code was run through the MAME emulator.
```

# Command 01

Coin drop

```code
Command01: 
; Initialize Routine Vector 01 (Coin Drop)
03E7: AF              XOR     A                   ; No ...
03E8: CD C8 01        CALL    $01C8               ; {FilterCaps} ... capacitors
03EB: 21 6B 00        LD      HL,$006B            ; Fine=6B, Coars=00
03EE: CD AA 01        CALL    $01AA               ; Write to tone registers
03F1: 21 41 30        LD      HL,$3041            ;
03F4: 36 00           LD      (HL),$00            ;
03F6: 2C              INC     L                   ;
03F7: 36 47           LD      (HL),$47            ;
03F9: 2C              INC     L                   ;
03FA: 0E 09           LD      C,$09               ; Amplitude
03FC: 71              LD      (HL),C              ;
03FD: CD 99 01        CALL    $0199               ; Set amplitude
0400: AF              XOR     A                   ; Return 0
0401: C9              RET                         ; Done

; Continue Sound Routine Vector 01  (Coin Drop)
0402: 21 41 30        LD      HL,$3041            ;
0405: 35              DEC     (HL)                ;
0406: 7E              LD      A,(HL)              ;
0407: E6 03           AND     $03                 ;
0409: 20 18           JR      NZ,$423             ;
040B: 2C              INC     L                   ;
040C: 35              DEC     (HL)                ;
040D: 7E              LD      A,(HL)              ;
040E: 28 1D           JR      Z,$42D              ; Return 1
0410: E6 07           AND     $07                 ;
0412: 28 11           JR      Z,$425              ;
0414: E6 03           AND     $03                 ;
0416: 3D              DEC     A                   ;
0417: 4F              LD      C,A                 ;
0418: 06 00           LD      B,$00               ;
041A: 21 2F 04        LD      HL,$042F            ;
041D: 09              ADD     HL,BC               ;
041E: 6E              LD      L,(HL)              ;
041F: 60              LD      H,B                 ;
0420: CD AA 01        CALL    $01AA               ; Write tone registers
0423: AF              XOR     A                   ; Return 0
0424: C9              RET                         ; Out
0425: 2C              INC     L                   ;
0426: 35              DEC     (HL)                ;
0427: 4E              LD      C,(HL)              ;
0428: CD 99 01        CALL    $0199               ; Set amplitude
042B: AF              XOR     A                   ; Return 0
042C: C9              RET                         ; Out
042D: 3D              DEC     A                   ; Zero becomes FF
042E: C9              RET                         ; Done

042F: 47 55 6B 
```

# Command 02

```code
Command02: 
; Initialization Vector Routine 02 (Plane Fire)
0432: AF              XOR     A                   ; A=0
0433: CD C8 01        CALL    $01C8               ;{FilterCaps} No filter caps on channel
0436: 0E 0A           LD      C,$0A               ; Set volume ...
0438: CD 99 01        CALL    $0199               ; ... to 10
043B: 3E 80           LD      A,$80               ; Loop count ...
043D: 32 44 30        LD      ($3044),A           ; ... is 128
0440: 21 04 00        LD      HL,$0004            ; Initial frequency ...
0443: 22 45 30        LD      ($3045),HL          ; ... is 4
0446: CD AA 01        CALL    $01AA               ; Write tone (HL=tone)
0449: AF              XOR     A                   ; Return a 0 (continue)
044A: C9              RET                         ;

; Continue Sound Routine Vector 02 (Plane Fire)
044B: 21 44 30        LD      HL,$3044            ; Decrement ...
044E: 35              DEC     (HL)                ; ... counter
044F: 7E              LD      A,(HL)              ; Stop if ...
0450: 28 0E           JR      Z,$460              ; ... done
0452: FE 6D           CP      $6D                 ; At loop value 6D ...
0454: 28 EA           JR      Z,$440              ; ... reset frequency to 4
0456: 2A 45 30        LD      HL,($3045)          ; Current tone value
0459: 01 18 00        LD      BC,$0018            ; Add ...
045C: 09              ADD     HL,BC               ; ... 18 to frequency
045D: C3 43 04        JP      $0443               ; Store and play tone
0460: 3D              DEC     A                   ; Return ...
0461: C9              RET                         ; ... -1 (finished)
```

# Command 03

```code
Command03: 
; Initialization Routine Vector 03 (1910 Bomb)
0462: AF              XOR     A                   ; No filter ...
0463: CD C8 01        CALL    $01C8               ;{FilterCaps} ... caps on channel
0466: 21 C0 00        LD      HL,$00C0            ; Inital ...
0469: 22 47 30        LD      ($3047),HL          ; ... tone
046C: CD AA 01        CALL    $01AA               ; Write tone
046F: 0E 09           LD      C,$09               ; Set ...
0471: CD 99 01        CALL    $0199               ; ... volume
0474: AF              XOR     A                   ; Set ...
0475: 21 49 30        LD      HL,$3049            ; ... 3049 = 0 ...
0478: 77              LD      (HL),A              ; ...
0479: C9              RET                         ;

; Continue Sound Routine Vector 03 (1910 Bomb)
047A: 21 49 30        LD      HL,$3049            ; Decrement ...
047D: 35              DEC     (HL)                ; ... counter
047E: 7E              LD      A,(HL)              ; Do nothing ...
047F: E6 07           AND     $07                 ; ... until MSB ...
0481: 20 12           JR      NZ,$495             ; ... is 0
0483: 2A 47 30        LD      HL,($3047)          ; Add ...
0486: 01 40 00        LD      BC,$0040            ; ... 40 ...
0489: 09              ADD     HL,BC               ; ... to tone
048A: 7C              LD      A,H                 ; When MSB is ...
048B: FE 0C           CP      $0C                 ; ... 0C ...
048D: 28 08           JR      Z,$497              ; ... the effect is done
048F: 22 47 30        LD      ($3047),HL          ; Store new tone
0492: CD AA 01        CALL    $01AA               ; Write tone
0495: AF              XOR     A                   ; Continue
0496: C9              RET                         ;
0497: 3E FF           LD      A,$FF               ; Done
0499: C9              RET                         ;
```

# Command 04

```code
Command04: 
; Initialization Routine Vector 04 (Missile Launch)
049A: 3E 01           LD      A,$01               ;
049C: CD C8 01        CALL    $01C8               ;{FilterCaps}
049F: 21 4A 30        LD      HL,$304A            ;
04A2: 36 00           LD      (HL),$00            ;
04A4: 2C              INC     L                   ;
04A5: 0E 0F           LD      C,$0F               ;
04A7: 71              LD      (HL),C              ;
04A8: CD 99 01        CALL    $0199               ; Set volume
04AB: 21 60 00        LD      HL,$0060            ;
04AE: 22 4C 30        LD      ($304C),HL          ;
04B1: AF              XOR     A                   ;
04B2: C9              RET                         ;

; Continue Sound Routine Vector 04 (Missile Launch)
04B3: 21 4A 30        LD      HL,$304A            ;
04B6: 35              DEC     (HL)                ;
04B7: 7E              LD      A,(HL)              ;
04B8: E6 0F           AND     $0F                 ;
04BA: 28 16           JR      Z,$4D2              ;
04BC: 2A 4C 30        LD      HL,($304C)          ;
04BF: FE 0C           CP      $0C                 ;
04C1: 01 10 00        LD      BC,$0010            ;
04C4: 30 03           JR      NC,$4C9             ;
04C6: 01 D0 FF        LD      BC,$FFD0            ;
04C9: 09              ADD     HL,BC               ;
04CA: 22 4C 30        LD      ($304C),HL          ;
04CD: CD AA 01        CALL    $01AA               ; Write tone
04D0: AF              XOR     A                   ;
04D1: C9              RET                         ;
04D2: 2C              INC     L                   ;
04D3: 35              DEC     (HL)                ;
04D4: 4E              LD      C,(HL)              ;
04D5: 20 D1           JR      NZ,$4A8             ;
04D7: 3D              DEC     A                   ;
04D8: C9              RET                         ;
```

# Command 05

```code
Command05: 
; Initialization Routine Vector 05 (Missile - continuous)
04D9: AF              XOR     A                   ;
04DA: CD C8 01        CALL    $01C8               ;{FilterCaps}
04DD: 21 4E 30        LD      HL,$304E            ;
04E0: 36 B0           LD      (HL),$B0            ;
04E2: 2C              INC     L                   ;
04E3: 36 0D           LD      (HL),$0D            ;
04E5: 35              DEC     (HL)                ;
04E6: 4E              LD      C,(HL)              ;
04E7: CD 99 01        CALL    $0199               ; Set volume
04EA: 2C              INC     L                   ;
04EB: 36 20           LD      (HL),$20            ;
04ED: 6E              LD      L,(HL)              ;
04EE: 26 00           LD      H,$00               ;
04F0: CD AA 01        CALL    $01AA               ; Write tone
04F3: AF              XOR     A                   ;
04F4: C9              RET                         ;

; Continue Sound Routine Vector 05 (Missile - continuous)
04F5: 21 4E 30        LD      HL,$304E            ;
04F8: 35              DEC     (HL)                ;
04F9: 7E              LD      A,(HL)              ;
04FA: 28 0C           JR      Z,$508              ;
04FC: 2C              INC     L                   ;
04FD: E6 0F           AND     $0F                 ;
04FF: 28 E4           JR      Z,$4E5              ;
0501: 2C              INC     L                   ;
0502: 34              INC     (HL)                ;
0503: C3 ED 04        JP      $04ED               ;
0506: AF              XOR     A                   ;
0507: C9              RET                         ;
0508: 3D              DEC     A                   ;
0509: C9              RET                         ;
```

# Command 06

```code
Command06: 
; Initialization Routine Vector 06 (UFO shot)
050A: AF              XOR     A                   ;
050B: CD C8 01        CALL    $01C8               ;{FilterCaps}
050E: 21 50 00        LD      HL,$0050            ;
0511: CD AA 01        CALL    $01AA               ; Write tone
0514: 21 51 30        LD      HL,$3051            ;
0517: 36 40           LD      (HL),$40            ;
0519: 2C              INC     L                   ;
051A: 0E 05           LD      C,$05               ;
051C: 71              LD      (HL),C              ;
051D: CD 99 01        CALL    $0199               ; Set volume
0520: 2C              INC     L                   ;
0521: 36 17           LD      (HL),$17            ;
0523: 2C              INC     L                   ;
0524: 36 50           LD      (HL),$50            ;
0526: AF              XOR     A                   ;
0527: C9              RET                         ;

; Continue Sound Routine Vector 06 (UFO shot)
0528: 21 51 30        LD      HL,$3051            ;
052B: 35              DEC     (HL)                ;
052C: 28 E9           JR      Z,$517              ;
052E: 7E              LD      A,(HL)              ;
052F: 2C              INC     L                   ;
0530: E6 0F           AND     $0F                 ;
0532: 20 05           JR      NZ,$539             ;
0534: 34              INC     (HL)                ;
0535: 4E              LD      C,(HL)              ;
0536: CD 99 01        CALL    $0199               ; Set volume
0539: 2C              INC     L                   ;
053A: 7E              LD      A,(HL)              ;
053B: C6 29           ADD     A,$29               ;
053D: 77              LD      (HL),A              ;
053E: 2C              INC     L                   ;
053F: AE              XOR     (HL)                ;
0540: E6 3F           AND     $3F                 ;
0542: C6 50           ADD     A,$50               ;
0544: 77              LD      (HL),A              ;
0545: 6F              LD      L,A                 ;
0546: 26 00           LD      H,$00               ;
0548: CD AA 01        CALL    $01AA               ; Write tone
054B: AF              XOR     A                   ;
054C: C9              RET                         ;
```

# Command 07

```code
Command07: 
; Initialization Routine Vector 07 (User Fire)
054D: AF              XOR     A                   ;
054E: CD C8 01        CALL    $01C8               ;{FilterCaps}
0551: 21 56 30        LD      HL,$3056            ;
0554: 36 08           LD      (HL),$08            ;
0556: 2D              DEC     L                   ;
0557: 36 2C           LD      (HL),$2C            ;
0559: 2C              INC     L                   ;
055A: 35              DEC     (HL)                ;
055B: 28 29           JR      Z,$586              ;
055D: 4E              LD      C,(HL)              ;
055E: CD 99 01        CALL    $0199               ; Set volume
0561: 21 00 00        LD      HL,$0000            ;
0564: 22 57 30        LD      ($3057),HL          ;
0567: CD AA 01        CALL    $01AA               ; Write tone
056A: AF              XOR     A                   ;
056B: C9              RET                         ;

; Continue Sound Routine Vector 07 (User Fire)
056C: 21 55 30        LD      HL,$3055            ;
056F: 35              DEC     (HL)                ;
0570: 7E              LD      A,(HL)              ;
0571: 28 E4           JR      Z,$557              ;
0573: FE 16           CP      $16                 ;
0575: 28 EA           JR      Z,$561              ;
0577: 2A 57 30        LD      HL,($3057)          ;
057A: 01 10 00        LD      BC,$0010            ;
057D: 09              ADD     HL,BC               ;
057E: 22 57 30        LD      ($3057),HL          ;
0581: CD AA 01        CALL    $01AA               ; Write tone
0584: AF              XOR     A                   ;
0585: C9              RET                         ;
0586: 3D              DEC     A                   ;
0587: C9              RET                         ;
```

# Command 08

```code
Command08: 
; Initialization Routine Vector 08 (Enemy Explosion Component - thud)
0588: 3E 01           LD      A,$01               ;
058A: CD C8 01        CALL    $01C8               ;{FilterCaps}
058D: 21 5C 30        LD      HL,$305C            ;
0590: 36 0C           LD      (HL),$0C            ;
0592: 4E              LD      C,(HL)              ;
0593: CD 99 01        CALL    $0199               ; Set volume
0596: 2D              DEC     L                   ;
0597: 36 00           LD      (HL),$00            ;
0599: 21 80 00        LD      HL,$0080            ;
059C: 22 59 30        LD      ($3059),HL          ;
059F: CD AA 01        CALL    $01AA               ; Write tone
05A2: AF              XOR     A                   ;
05A3: C9              RET                         ;

; Continue Sound Routine Vector 08 (Enemy Explosion Component - thud)
05A4: 21 5B 30        LD      HL,$305B            ;
05A7: 34              INC     (HL)                ;
05A8: 7E              LD      A,(HL)              ;
05A9: FE 59           CP      $59                 ;
05AB: 28 0F           JR      Z,$5BC              ;
05AD: 4F              LD      C,A                 ;
05AE: 06 00           LD      B,$00               ;
05B0: 2A 59 30        LD      HL,($3059)          ;
05B3: 09              ADD     HL,BC               ;
05B4: 22 59 30        LD      ($3059),HL          ;
05B7: CD AA 01        CALL    $01AA               ; Write tone
05BA: AF              XOR     A                   ;
05BB: C9              RET                         ;
05BC: 2C              INC     L                   ;
05BD: 7E              LD      A,(HL)              ;
05BE: D6 04           SUB     $04                 ;
05C0: 28 04           JR      Z,$5C6              ;
05C2: 77              LD      (HL),A              ;
05C3: C3 92 05        JP      $0592               ;
05C6: 3D              DEC     A                   ;
05C7: C9              RET                         ;
```

# Command 09

```code
Command09: 
; Initialization Routine Vector 09 (Enemy Explosion Component white-noise)
05C8: 3E 01           LD      A,$01               ;
05CA: CD C8 01        CALL    $01C8               ;{FilterCaps}
05CD: 21 5D 30        LD      HL,$305D            ;
05D0: 36 00           LD      (HL),$00            ;
05D2: 2C              INC     L                   ;
05D3: 36 E0           LD      (HL),$E0            ;
05D5: 2C              INC     L                   ;
05D6: 0E 0D           LD      C,$0D               ;
05D8: 71              LD      (HL),C              ;
05D9: CD 99 01        CALL    $0199               ; Set volume
05DC: 2C              INC     L                   ;
05DD: 36 93           LD      (HL),$93            ;
05DF: 2C              INC     L                   ;
05E0: 36 D5           LD      (HL),$D5            ;
05E2: 21 C0 00        LD      HL,$00C0            ;
05E5: CD AA 01        CALL    $01AA               ; Write tone
05E8: AF              XOR     A                   ;
05E9: C9              RET                         ;

; Continue Sound Routine Vector 09 (Enemy Explosion Component white-noise)
05EA: 21 5D 30        LD      HL,$305D            ;
05ED: 35              DEC     (HL)                ;
05EE: CB 46           BIT     0,(HL)              ;
05F0: 20 25           JR      NZ,$617             ;
05F2: 2C              INC     L                   ;
05F3: 35              DEC     (HL)                ;
05F4: 7E              LD      A,(HL)              ;
05F5: 28 22           JR      Z,$619              ;
05F7: FE D0           CP      $D0                 ;
05F9: 28 DA           JR      Z,$5D5              ;
05FB: 2C              INC     L                   ;
05FC: E6 0F           AND     $0F                 ;
05FE: 20 05           JR      NZ,$605             ;
0600: 35              DEC     (HL)                ;
0601: 4E              LD      C,(HL)              ;
0602: CD 99 01        CALL    $0199               ; Set volume
0605: 2C              INC     L                   ;
0606: 7E              LD      A,(HL)              ;
0607: C6 53           ADD     A,$53               ;
0609: 77              LD      (HL),A              ;
060A: 2C              INC     L                   ;
060B: AE              XOR     (HL)                ;
060C: 77              LD      (HL),A              ;
060D: 6F              LD      L,A                 ;
060E: FE E0           CP      $E0                 ;
0610: 38 01           JR      C,$613              ;
0612: AF              XOR     A                   ;
0613: 67              LD      H,A                 ;
0614: CD AA 01        CALL    $01AA               ; Write tone
0617: AF              XOR     A                   ;
0618: C9              RET                         ;
0619: 3D              DEC     A                   ;
061A: C9              RET                         ;
```

# Command 0A

```code
Command0A: 
; Initialization Routine Vector 0A (Traker or Bomb Explosion)
061B: AF              XOR     A                   ;
061C: CD C8 01        CALL    $01C8               ;{FilterCaps}
061F: 21 62 30        LD      HL,$3062            ;
0622: 36 00           LD      (HL),$00            ;
0624: 2C              INC     L                   ;
0625: 36 C0           LD      (HL),$C0            ;
0627: 2C              INC     L                   ;
0628: 36 0D           LD      (HL),$0D            ;
062A: 35              DEC     (HL)                ;
062B: 4E              LD      C,(HL)              ;
062C: CD 99 01        CALL    $0199               ; Set volume
062F: 21 20 00        LD      HL,$0020            ;
0632: 22 65 30        LD      ($3065),HL          ;
0635: CD AA 01        CALL    $01AA               ; Write tone
0638: AF              XOR     A                   ;
0639: C9              RET                         ;

; Continue Sound Routine Vector 0A (Traker or Bomb Explosion)
063A: 21 62 30        LD      HL,$3062            ;
063D: 35              DEC     (HL)                ;
063E: 7E              LD      A,(HL)              ;
063F: E6 01           AND     $01                 ;
0641: 20 17           JR      NZ,$65A             ;
0643: 2C              INC     L                   ;
0644: 35              DEC     (HL)                ;
0645: 7E              LD      A,(HL)              ;
0646: 28 14           JR      Z,$65C              ;
0648: 2C              INC     L                   ;
0649: E6 0F           AND     $0F                 ;
064B: 28 DD           JR      Z,$62A              ;
064D: 2A 65 30        LD      HL,($3065)          ;
0650: 01 40 00        LD      BC,$0040            ;
0653: 09              ADD     HL,BC               ;
0654: 22 65 30        LD      ($3065),HL          ;
0657: CD AA 01        CALL    $01AA               ; Write tone
065A: AF              XOR     A                   ;
065B: C9              RET                         ;
065C: 3D              DEC     A                   ;
065D: C9              RET                         ;
```

# Command 0B

```code
Command0B: 
; Initialization Routine Vector 0B (Squad appears)
065E: AF              XOR     A                   ; No filter ...
065F: CD C8 01        CALL    $01C8               ;{FilterCaps} ... caps on channel
0662: 0E 0C           LD      C,$0C               ; Set ...
0664: CD 99 01        CALL    $0199               ; ... volume
0667: 21 67 30        LD      HL,$3067            ; Set ...
066A: 36 B8           LD      (HL),$B8            ; ... 3067 = B8
066C: 2C              INC     L                   ; Set ...
066D: 36 1F           LD      (HL),$1F            ; ... 3068 = 1F
066F: 21 1F 00        LD      HL,$001F            ; Initial tone
0672: CD AA 01        CALL    $01AA               ; Write tone
0675: AF              XOR     A                   ; Continue
0676: C9              RET                         ;

; Continue Sound Routine Vector 0B (Squad appears)
0677: 21 67 30        LD      HL,$3067            ; (3067) = (3067) - 1
067A: 35              DEC     (HL)                ; ...
067B: 7E              LD      A,(HL)              ; End when MSB ...
067C: 28 15           JR      Z,$693              ; ... is 0
067E: FE 60           CP      $60                 ;
0680: 28 EA           JR      Z,$66C              ;
0682: E6 03           AND     $03                 ;
0684: 20 0B           JR      NZ,$691             ;
0686: 2C              INC     L                   ;
0687: 7E              LD      A,(HL)              ;
0688: C6 20           ADD     A,$20               ;
068A: 77              LD      (HL),A              ;
068B: 6F              LD      L,A                 ;
068C: 26 00           LD      H,$00               ;
068E: CD AA 01        CALL    $01AA               ; Write tone
0691: AF              XOR     A                   ;
0692: C9              RET                         ;
0693: 3D              DEC     A                   ;
0694: C9              RET                         ;
```

# Command 0C

```code
Command0C: 
; Initialization Routine Vector 0C (1st boss - blimp)
0695: 3E 01           LD      A,$01               ;
0697: CD C8 01        CALL    $01C8               ;{FilterCaps}
069A: 21 C0 00        LD      HL,$00C0            ;
069D: CD AA 01        CALL    $01AA               ; Write tone
06A0: 0E 0F           LD      C,$0F               ;
06A2: CD 99 01        CALL    $0199               ; Set volume
06A5: AF              XOR     A                   ;
06A6: 21 69 30        LD      HL,$3069            ;
06A9: 77              LD      (HL),A              ;
06AA: 2C              INC     L                   ;
06AB: 36 53           LD      (HL),$53            ;
06AD: 2C              INC     L                   ;
06AE: 36 09           LD      (HL),$09            ;
06B0: 2C              INC     L                   ;
06B1: 36 37           LD      (HL),$37            ;
06B3: C9              RET                         ;

; Continue Sound Routine Vector 0C (1st boss - blimp)
06B4: 21 69 30        LD      HL,$3069            ;
06B7: 35              DEC     (HL)                ;
06B8: 56              LD      D,(HL)              ;
06B9: 2C              INC     L                   ;
06BA: 7E              LD      A,(HL)              ;
06BB: C6 D5           ADD     A,$D5               ;
06BD: 77              LD      (HL),A              ;
06BE: 2C              INC     L                   ;
06BF: CB 42           BIT     0,D                 ;
06C1: 20 09           JR      NZ,$6CC             ;
06C3: AE              XOR     (HL)                ;
06C4: 77              LD      (HL),A              ;
06C5: E6 EF           AND     $EF                 ;
06C7: 4F              LD      C,A                 ;
06C8: CD 99 01        CALL    $0199               ; Set volume
06CB: 79              LD      A,C                 ;
06CC: 2C              INC     L                   ;
06CD: AE              XOR     (HL)                ;
06CE: 77              LD      (HL),A              ;
06CF: F6 80           OR      $80                 ;
06D1: 6F              LD      L,A                 ;
06D2: 26 00           LD      H,$00               ;
06D4: CD AA 01        CALL    $01AA               ; Write tone
06D7: AF              XOR     A                   ;
06D8: C9              RET                         ;
```
# Command 0D

```code
Command0D: 
; Initialization Routine Vector 0D (2nd boss - jet)
06D9: 3E 01           LD      A,$01               ;
06DB: CD C8 01        CALL    $01C8               ;{FilterCaps}
06DE: 21 6D 30        LD      HL,$306D            ;
06E1: 36 28           LD      (HL),$28            ;
06E3: 2C              INC     L                   ;
06E4: 36 05           LD      (HL),$05            ;
06E6: 2C              INC     L                   ;
06E7: 36 30           LD      (HL),$30            ;
06E9: 21 00 06        LD      HL,$0600            ;
06EC: CD AA 01        CALL    $01AA               ; Write tone
06EF: 0E 08           LD      C,$08               ;
06F1: CD 99 01        CALL    $0199               ; Set volume
06F4: AF              XOR     A                   ;
06F5: C9              RET                         ;

; Continue Sound Routine Vector 0D (2nd boss - jet)
06F6: 21 6D 30        LD      HL,$306D            ;
06F9: 35              DEC     (HL)                ;
06FA: 28 E5           JR      Z,$6E1              ;
06FC: 7E              LD      A,(HL)              ;
06FD: E6 07           AND     $07                 ;
06FF: C6 08           ADD     A,$08               ;
0701: 4F              LD      C,A                 ;
0702: CD 99 01        CALL    $0199               ; Set volume
0705: 2C              INC     L                   ;
0706: 7E              LD      A,(HL)              ;
0707: C6 B9           ADD     A,$B9               ;
0709: 77              LD      (HL),A              ;
070A: 2C              INC     L                   ;
070B: AE              XOR     (HL)                ;
070C: 77              LD      (HL),A              ;
070D: 6F              LD      L,A                 ;
070E: 26 06           LD      H,$06               ;
0710: CD AA 01        CALL    $01AA               ; Write tone
0713: AF              XOR     A                   ;
0714: C9              RET                         ;
```

# Command 0E

```code
Command0E: 
; Initialization Routine Vector 0E (3rd boss - helicopter)
0715: 3E 01           LD      A,$01               ;
0717: CD C8 01        CALL    $01C8               ;{FilterCaps}
071A: 21 00 01        LD      HL,$0100            ;
071D: CD AA 01        CALL    $01AA               ; Write tone
0720: 21 70 30        LD      HL,$3070            ;
0723: 36 00           LD      (HL),$00            ;
0725: 2C              INC     L                   ;
0726: 0E 0F           LD      C,$0F               ;
0728: 71              LD      (HL),C              ;
0729: CD 99 01        CALL    $0199               ; Set volume
072C: AF              XOR     A                   ;
072D: 2C              INC     L                   ;
072E: 77              LD      (HL),A              ;
072F: 2C              INC     L                   ;
0730: 77              LD      (HL),A              ;
0731: C9              RET                         ;

; Continue Sound Routine Vector 0E (3rd boss - helicopter)
0732: 21 70 30        LD      HL,$3070            ;
0735: 35              DEC     (HL)                ;
0736: 7E              LD      A,(HL)              ;
0737: CB 47           BIT     0,A                 ;
0739: 23              INC     HL                  ;
073A: 20 0B           JR      NZ,$747             ;
073C: 35              DEC     (HL)                ;
073D: E6 10           AND     $10                 ;
073F: 20 02           JR      NZ,$743             ;
0741: 34              INC     (HL)                ;
0742: 34              INC     (HL)                ;
0743: 4E              LD      C,(HL)              ;
0744: CD 99 01        CALL    $0199               ; Set volume
0747: 2C              INC     L                   ;
0748: 7E              LD      A,(HL)              ;
0749: C6 D3           ADD     A,$D3               ;
074B: 77              LD      (HL),A              ;
074C: 2C              INC     L                   ;
074D: AE              XOR     (HL)                ;
074E: 77              LD      (HL),A              ;
074F: E6 7F           AND     $7F                 ;
0751: C6 A8           ADD     A,$A8               ;
0753: 6F              LD      L,A                 ;
0754: E6 07           AND     $07                 ;
0756: 67              LD      H,A                 ;
0757: CD AA 01        CALL    $01AA               ; Write tone
075A: AF              XOR     A                   ;
075B: C9              RET                         ;
```

# Command 0F

```code
Command0F: 
; Initialization Routine Vector 0F (4th boss - super jet)
075C: 3E 01           LD      A,$01               ;
075E: CD C8 01        CALL    $01C8               ;{FilterCaps}
0761: 21 00 01        LD      HL,$0100            ;
0764: CD AA 01        CALL    $01AA               ; Write tone
0767: 0E 0C           LD      C,$0C               ;
0769: CD 99 01        CALL    $0199               ; Set volume
076C: AF              XOR     A                   ;
076D: 21 74 30        LD      HL,$3074            ;
0770: 77              LD      (HL),A              ;
0771: 2C              INC     L                   ;
0772: 77              LD      (HL),A              ;
0773: C9              RET                         ;

; Continue Sound Routine Vector 0F (4th boss - super jet)
0774: 21 74 30        LD      HL,$3074            ;
0777: 7E              LD      A,(HL)              ;
0778: C6 97           ADD     A,$97               ;
077A: 77              LD      (HL),A              ;
077B: 2C              INC     L                   ;
077C: AE              XOR     (HL)                ;
077D: 77              LD      (HL),A              ;
077E: E6 7F           AND     $7F                 ;
0780: C6 C0           ADD     A,$C0               ;
0782: 6F              LD      L,A                 ;
0783: 26 01           LD      H,$01               ;
0785: CD AA 01        CALL    $01AA               ; Write tone
0788: AF              XOR     A                   ;
0789: C9              RET                         ;
```

# Command 10

```code
Command10: 
; Initialization Routine Vector 10 (5th boss - mother ship)
078A: 3E 01           LD      A,$01               ;
078C: CD C8 01        CALL    $01C8               ;{FilterCaps}
078F: 0E 0A           LD      C,$0A               ;
0791: CD 99 01        CALL    $0199               ; Set volume
0794: 21 76 30        LD      HL,$3076            ;
0797: 36 30           LD      (HL),$30            ;
0799: 2C              INC     L                   ;
079A: 36 02           LD      (HL),$02            ;
079C: 2C              INC     L                   ;
079D: 3E E0           LD      A,$E0               ;
079F: 77              LD      (HL),A              ;
07A0: 2C              INC     L                   ;
07A1: 77              LD      (HL),A              ;
07A2: 6F              LD      L,A                 ;
07A3: 26 00           LD      H,$00               ;
07A5: CD AA 01        CALL    $01AA               ; Write tone
07A8: AF              XOR     A                   ;
07A9: C9              RET                         ;

; Continue Sound Routine Vector 10 (5th boss - mother ship)
07AA: 21 76 30        LD      HL,$3076            ;
07AD: 35              DEC     (HL)                ;
07AE: 7E              LD      A,(HL)              ;
07AF: 28 E6           JR      Z,$797              ;
07B1: 2C              INC     L                   ;
07B2: E6 0F           AND     $0F                 ;
07B4: 28 07           JR      Z,$7BD              ;
07B6: 7E              LD      A,(HL)              ;
07B7: 2C              INC     L                   ;
07B8: 2C              INC     L                   ;
07B9: 86              ADD     A,(HL)              ;
07BA: C3 A1 07        JP      $07A1               ;
07BD: 34              INC     (HL)                ;
07BE: 34              INC     (HL)                ;
07BF: 2C              INC     L                   ;
07C0: 7E              LD      A,(HL)              ;
07C1: D6 20           SUB     $20                 ;
07C3: C3 9F 07        JP      $079F               ;

```
# Command 11

```code
Command11: 
; Initialization Routine Vector 11 (User Explosion Component)
07C6: 3E 01           LD      A,$01               ;
07C8: CD C8 01        CALL    $01C8               ;{FilterCaps}
07CB: 21 00 00        LD      HL,$0000            ;
07CE: CD AA 01        CALL    $01AA               ; Write tone
07D1: 21 7A 30        LD      HL,$307A            ;
07D4: 36 00           LD      (HL),$00            ;
07D6: 2C              INC     L                   ;
07D7: 0E 0F           LD      C,$0F               ;
07D9: 71              LD      (HL),C              ;
07DA: CD 99 01        CALL    $0199               ; Set volume
07DD: 2C              INC     L                   ;
07DE: 36 45           LD      (HL),$45            ;
07E0: 2C              INC     L                   ;
07E1: 36 99           LD      (HL),$99            ;
07E3: AF              XOR     A                   ;
07E4: C9              RET                         ;

; Continue Sound Routine Vector 11 (User Explosion Component)
07E5: 21 7A 30        LD      HL,$307A            ;
07E8: 35              DEC     (HL)                ;
07E9: 7E              LD      A,(HL)              ;
07EA: CB 47           BIT     0,A                 ;
07EC: 20 19           JR      NZ,$807             ;
07EE: 2C              INC     L                   ;
07EF: E6 3F           AND     $3F                 ;
07F1: 20 07           JR      NZ,$7FA             ;
07F3: 35              DEC     (HL)                ;
07F4: 28 13           JR      Z,$809              ;
07F6: 4E              LD      C,(HL)              ;
07F7: CD 99 01        CALL    $0199               ; Set volume
07FA: 2C              INC     L                   ;
07FB: 7E              LD      A,(HL)              ;
07FC: C6 D3           ADD     A,$D3               ;
07FE: 77              LD      (HL),A              ;
07FF: 2C              INC     L                   ;
0800: AE              XOR     (HL)                ;
0801: 77              LD      (HL),A              ;
0802: 6F              LD      L,A                 ;
0803: 67              LD      H,A                 ;
0804: CD AA 01        CALL    $01AA               ; Write tone
0807: AF              XOR     A                   ;
0808: C9              RET                         ;
0809: 3D              DEC     A                   ;
080A: C9              RET                         ;
```

# Command 12

```code
Command12: 
; Initialization Routine Vector 12 (User Explosion Component)
080B: 3E 01           LD      A,$01               ;
080D: CD C8 01        CALL    $01C8               ;{FilterCaps}
0810: 21 00 00        LD      HL,$0000            ;
0813: 22 81 30        LD      ($3081),HL          ;
0816: CD AA 01        CALL    $01AA               ; Write tone
0819: 21 7E 30        LD      HL,$307E            ;
081C: 36 00           LD      (HL),$00            ;
081E: 2C              INC     L                   ;
081F: 0E 0F           LD      C,$0F               ;
0821: 71              LD      (HL),C              ;
0822: CD 99 01        CALL    $0199               ; Set volume
0825: 2C              INC     L                   ;
0826: AF              XOR     A                   ;
0827: 77              LD      (HL),A              ;
0828: C9              RET                         ;

; Continue Sound Routine Vector 12 (User Explosion Component)
0829: 21 7E 30        LD      HL,$307E            ;
082C: 35              DEC     (HL)                ;
082D: 7E              LD      A,(HL)              ;
082E: 57              LD      D,A                 ;
082F: 2C              INC     L                   ;
0830: E6 1F           AND     $1F                 ;
0832: 20 07           JR      NZ,$83B             ;
0834: 35              DEC     (HL)                ;
0835: 28 1E           JR      Z,$855              ;
0837: 4E              LD      C,(HL)              ;
0838: CD 99 01        CALL    $0199               ; Set volume
083B: 2C              INC     L                   ;
083C: 7E              LD      A,(HL)              ;
083D: C6 C5           ADD     A,$C5               ;
083F: 77              LD      (HL),A              ;
0840: 2A 81 30        LD      HL,($3081)          ;
0843: AA              XOR     D                   ;
0844: AD              XOR     L                   ;
0845: 6F              LD      L,A                 ;
0846: 67              LD      H,A                 ;
0847: FE 80           CP      $80                 ;
0849: 30 02           JR      NC,$84D             ;
084B: 26 01           LD      H,$01               ;
084D: 22 81 30        LD      ($3081),HL          ;
0850: CD AA 01        CALL    $01AA               ; Write tone
0853: AF              XOR     A                   ;
0854: C9              RET                         ;
0855: 3D              DEC     A                   ;
0856: C9              RET                         ;
```

# Command 13

```code
Command13: 
; Initialization Routine Vector 13 (User Explosion Component)
0857: 3E 02           LD      A,$02               ;
0859: CD C8 01        CALL    $01C8               ;{FilterCaps}
085C: 21 00 00        LD      HL,$0000            ;
085F: CD AA 01        CALL    $01AA               ; Write tone
0862: 21 83 30        LD      HL,$3083            ;
0865: 0E 0F           LD      C,$0F               ;
0867: 71              LD      (HL),C              ;
0868: CD 99 01        CALL    $0199               ; Set volume
086B: 2C              INC     L                   ;
086C: 36 30           LD      (HL),$30            ;
086E: 2C              INC     L                   ;
086F: 36 95           LD      (HL),$95            ;
0871: 2C              INC     L                   ;
0872: 36 3D           LD      (HL),$3D            ;
0874: 21 70 00        LD      HL,$0070            ;
0877: 22 87 30        LD      ($3087),HL          ;
087A: 22 89 30        LD      ($3089),HL          ;
087D: AF              XOR     A                   ;
087E: C9              RET                         ;

; Continue Sound Routine Vector 13 (User Explosion Component)
087F: 21 84 30        LD      HL,$3084            ;
0882: 35              DEC     (HL)                ;
0883: 7E              LD      A,(HL)              ;
0884: 28 28           JR      Z,$8AE              ;
0886: FE 10           CP      $10                 ;
0888: 38 10           JR      C,$89A              ;
088A: 2C              INC     L                   ;
088B: 7E              LD      A,(HL)              ;
088C: C6 C9           ADD     A,$C9               ;
088E: 77              LD      (HL),A              ;
088F: 2C              INC     L                   ;
0890: AE              XOR     (HL)                ;
0891: 77              LD      (HL),A              ;
0892: 6F              LD      L,A                 ;
0893: 26 01           LD      H,$01               ;
0895: CD AA 01        CALL    $01AA               ; Write tone
0898: AF              XOR     A                   ;
0899: C9              RET                         ;
089A: D6 10           SUB     $10                 ;
089C: ED 44           NEG                         ;
089E: 87              ADD     A,A                 ;
089F: 4F              LD      C,A                 ;
08A0: 06 00           LD      B,$00               ;
08A2: 2A 89 30        LD      HL,($3089)          ;
08A5: 09              ADD     HL,BC               ;
08A6: 22 89 30        LD      ($3089),HL          ;
08A9: CD AA 01        CALL    $01AA               ; Write tone
08AC: AF              XOR     A                   ;
08AD: C9              RET                         ;
08AE: 2D              DEC     L                   ;
08AF: 35              DEC     (HL)                ;
08B0: 28 1C           JR      Z,$8CE              ;
08B2: 4E              LD      C,(HL)              ;
08B3: CD 99 01        CALL    $0199               ; Set volume
08B6: 2C              INC     L                   ;
08B7: 3A 85 30        LD      A,($3085)           ;
08BA: E6 3F           AND     $3F                 ;
08BC: C6 30           ADD     A,$30               ;
08BE: 77              LD      (HL),A              ;
08BF: 2A 87 30        LD      HL,($3087)          ;
08C2: 01 60 00        LD      BC,$0060            ;
08C5: 09              ADD     HL,BC               ;
08C6: 22 87 30        LD      ($3087),HL          ;
08C9: 22 89 30        LD      ($3089),HL          ;
08CC: AF              XOR     A                   ;
08CD: C9              RET                         ;
08CE: 3D              DEC     A                   ;
08CF: C9              RET                         ;
```

# Command 14

```code
Command14: 
; Initialization Routine Vector 14 (User Explosion Component)
08D0: 3E 02           LD      A,$02               ;
08D2: CD C8 01        CALL    $01C8               ;{FilterCaps}
08D5: 21 00 00        LD      HL,$0000            ;
08D8: CD AA 01        CALL    $01AA               ; Write tone
08DB: 21 8B 30        LD      HL,$308B            ;
08DE: 0E 0F           LD      C,$0F               ;
08E0: 71              LD      (HL),C              ;
08E1: CD 99 01        CALL    $0199               ; Set volume
08E4: 2C              INC     L                   ;
08E5: 36 30           LD      (HL),$30            ;
08E7: 2C              INC     L                   ;
08E8: 36 95           LD      (HL),$95            ;
08EA: 2C              INC     L                   ;
08EB: 36 3D           LD      (HL),$3D            ;
08ED: 21 38 00        LD      HL,$0038            ;
08F0: 22 8F 30        LD      ($308F),HL          ;
08F3: 22 91 30        LD      ($3091),HL          ;
08F6: AF              XOR     A                   ;
08F7: C9              RET                         ;

; Continue Sound Routine Vector 14 (User Explosion Component)
08F8: 21 8C 30        LD      HL,$308C            ;
08FB: 35              DEC     (HL)                ;
08FC: 7E              LD      A,(HL)              ;
08FD: 28 23           JR      Z,$922              ;
08FF: FE 10           CP      $10                 ;
0901: 38 10           JR      C,$913              ;
0903: 2C              INC     L                   ;
0904: 7E              LD      A,(HL)              ;
0905: C6 D3           ADD     A,$D3               ;
0907: 77              LD      (HL),A              ;
0908: 2C              INC     L                   ;
0909: AE              XOR     (HL)                ;
090A: 77              LD      (HL),A              ;
090B: 6F              LD      L,A                 ;
090C: 26 01           LD      H,$01               ;
090E: CD AA 01        CALL    $01AA               ; Write tone
0911: AF              XOR     A                   ;
0912: C9              RET                         ;
0913: 2A 91 30        LD      HL,($3091)          ;
0916: 01 30 00        LD      BC,$0030            ;
0919: 09              ADD     HL,BC               ;
091A: 22 91 30        LD      ($3091),HL          ;
091D: CD AA 01        CALL    $01AA               ; Write tone
0920: AF              XOR     A                   ;
0921: C9              RET                         ;
0922: 2D              DEC     L                   ;
0923: 35              DEC     (HL)                ;
0924: 28 1C           JR      Z,$942              ;
0926: 4E              LD      C,(HL)              ;
0927: CD 99 01        CALL    $0199               ; Set volume
092A: 2C              INC     L                   ;
092B: 3A 8D 30        LD      A,($308D)           ;
092E: E6 3F           AND     $3F                 ;
0930: C6 30           ADD     A,$30               ;
0932: 77              LD      (HL),A              ;
0933: 2A 8F 30        LD      HL,($308F)          ;
0936: 01 06 00        LD      BC,$0006            ;
0939: 09              ADD     HL,BC               ;
093A: 22 8F 30        LD      ($308F),HL          ;
093D: 22 91 30        LD      ($3091),HL          ;
0940: AF              XOR     A                   ;
0941: C9              RET                         ;
0942: 3D              DEC     A                   ;
0943: C9              RET                         ;
```

# Command 15

```code
Command15: 
; Initialization Routine Vector 15 (User Explosion Component)
0944: 3E 01           LD      A,$01               ;
0946: CD C8 01        CALL    $01C8               ;{FilterCaps}
0949: 21 93 30        LD      HL,$3093            ;
094C: 36 00           LD      (HL),$00            ;
094E: 2C              INC     L                   ;
094F: 36 D0           LD      (HL),$D0            ;
0951: 2C              INC     L                   ;
0952: 0E 0D           LD      C,$0D               ;
0954: 71              LD      (HL),C              ;
0955: CD 99 01        CALL    $0199               ; Set volume
0958: 2C              INC     L                   ;
0959: 36 93           LD      (HL),$93            ;
095B: 2C              INC     L                   ;
095C: 36 D5           LD      (HL),$D5            ;
095E: 21 C0 00        LD      HL,$00C0            ;
0961: CD AA 01        CALL    $01AA               ; Write tone
0964: AF              XOR     A                   ;
0965: C9              RET                         ;

; Continue Sound Routine Vector 15 (User Explosion Component)
0966: 21 93 30        LD      HL,$3093            ;
0969: 35              DEC     (HL)                ;
096A: 7E              LD      A,(HL)              ;
096B: E6 03           AND     $03                 ;
096D: 20 29           JR      NZ,$998             ;
096F: 2C              INC     L                   ;
0970: 35              DEC     (HL)                ;
0971: 28 27           JR      Z,$99A              ;
0973: 7E              LD      A,(HL)              ;
0974: FE 98           CP      $98                 ;
0976: 28 D9           JR      Z,$951              ;
0978: FE 80           CP      $80                 ;
097A: 28 D5           JR      Z,$951              ;
097C: 2C              INC     L                   ;
097D: E6 0F           AND     $0F                 ;
097F: 20 05           JR      NZ,$986             ;
0981: 35              DEC     (HL)                ;
0982: 4E              LD      C,(HL)              ;
0983: CD 99 01        CALL    $0199               ; Set volume
0986: 2C              INC     L                   ;
0987: 7E              LD      A,(HL)              ;
0988: C6 53           ADD     A,$53               ;
098A: 77              LD      (HL),A              ;
098B: 2C              INC     L                   ;
098C: AE              XOR     (HL)                ;
098D: 77              LD      (HL),A              ;
098E: 6F              LD      L,A                 ;
098F: FE E0           CP      $E0                 ;
0991: 38 01           JR      C,$994              ;
0993: AF              XOR     A                   ;
0994: 67              LD      H,A                 ;
0995: CD AA 01        CALL    $01AA               ; Write tone
0998: AF              XOR     A                   ;
0999: C9              RET                         ;
099A: 3D              DEC     A                   ;
099B: C9              RET                         ;
```

# Command 16

```code
Command16: 
; Initialization Routine Vector 16 (Pickup Parachute)
099C: AF              XOR     A                   ;
099D: CD C8 01        CALL    $01C8               ;{FilterCaps}
09A0: 0E 09           LD      C,$09               ;
09A2: CD 99 01        CALL    $0199               ; Set volume
09A5: 21 99 30        LD      HL,$3099            ;
09A8: 3E F6           LD      A,$F6               ;
09AA: D6 06           SUB     $06                 ;
09AC: 77              LD      (HL),A              ;
09AD: D6 7E           SUB     $7E                 ;
09AF: 28 1E           JR      Z,$9CF              ;
09B1: 2D              DEC     L                   ;
09B2: 36 30           LD      (HL),$30            ;
09B4: 21 30 00        LD      HL,$0030            ;
09B7: CD AA 01        CALL    $01AA               ; Write tone
09BA: AF              XOR     A                   ;
09BB: C9              RET                         ;

; Continue Sound Routine Vector 16 (Pickup Parachute)
09BC: 21 98 30        LD      HL,$3098            ;
09BF: 7E              LD      A,(HL)              ;
09C0: C6 06           ADD     A,$06               ;
09C2: 77              LD      (HL),A              ;
09C3: 2C              INC     L                   ;
09C4: BE              CP      (HL)                ;
09C5: 28 E3           JR      Z,$9AA              ;
09C7: 6F              LD      L,A                 ;
09C8: 26 00           LD      H,$00               ;
09CA: CD AA 01        CALL    $01AA               ; Write tone
09CD: AF              XOR     A                   ;
09CE: C9              RET                         ;
09CF: 3D              DEC     A                   ;
09D0: C9              RET                         ;
```

# Command 17

```code
Command17: 
; Initialization Routine Vector 17 (Free Man)
09D1: 3E 01           LD      A,$01               ;
09D3: CD C8 01        CALL    $01C8               ;{FilterCaps}
09D6: 0E 0F           LD      C,$0F               ;
09D8: CD 99 01        CALL    $0199               ; Set volume
09DB: 21 9A 30        LD      HL,$309A            ;
09DE: 36 1D           LD      (HL),$1D            ;
09E0: 2C              INC     L                   ;
09E1: 2D              DEC     L                   ;
09E2: 35              DEC     (HL)                ;
09E3: 7E              LD      A,(HL)              ;
09E4: 28 1A           JR      Z,$A00              ;
09E6: 2C              INC     L                   ;
09E7: 77              LD      (HL),A              ;
09E8: 87              ADD     A,A                 ;
09E9: 6F              LD      L,A                 ;
09EA: 26 00           LD      H,$00               ;
09EC: CD AA 01        CALL    $01AA               ; Write tone
09EF: AF              XOR     A                   ;
09F0: C9              RET                         ;

; Continue Sound Routine Vector 17 (Free Man)
09F1: 21 9B 30        LD      HL,$309B            ;
09F4: 35              DEC     (HL)                ;
09F5: 28 EA           JR      Z,$9E1              ;
09F7: 6E              LD      L,(HL)              ;
09F8: 26 00           LD      H,$00               ;
09FA: 29              ADD     HL,HL               ;
09FB: CD AA 01        CALL    $01AA               ; Write tone
09FE: AF              XOR     A                   ;
09FF: C9              RET                         ;
0A00: 3D              DEC     A                   ;
0A01: C9              RET                         ;
```

# Command 18

```code
Command18: 
; Initialization Routine Vector 18 (Time Jump 1)
0A02: AF              XOR     A                   ;
0A03: CD C8 01        CALL    $01C8               ;{FilterCaps}
0A06: 0E 0A           LD      C,$0A               ;
0A08: CD 99 01        CALL    $0199               ; Set volume
0A0B: 3E 80           LD      A,$80               ;
0A0D: 32 9E 30        LD      ($309E),A           ;
0A10: 21 9C 30        LD      HL,$309C            ;
0A13: 36 00           LD      (HL),$00            ;
0A15: 2C              INC     L                   ;
0A16: 36 C0           LD      (HL),$C0            ;
0A18: 21 C0 00        LD      HL,$00C0            ;
0A1B: CD AA 01        CALL    $01AA               ; Write tone
0A1E: AF              XOR     A                   ;
0A1F: C9              RET                         ;

; Continue Sound Routine Vector 18 (Time Jump 1)
0A20: 21 9C 30        LD      HL,$309C            ;
0A23: 35              DEC     (HL)                ;
0A24: CB 46           BIT     0,(HL)              ;
0A26: 23              INC     HL                  ;
0A27: 7E              LD      A,(HL)              ;
0A28: 20 15           JR      NZ,$A3F             ;
0A2A: 35              DEC     (HL)                ;
0A2B: 7E              LD      A,(HL)              ;
0A2C: FE 20           CP      $20                 ;
0A2E: 28 18           JR      Z,$A48              ;
0A30: 2C              INC     L                   ;
0A31: BE              CP      (HL)                ;
0A32: 3A 9D 30        LD      A,($309D)           ;
0A35: 20 09           JR      NZ,$A40             ;
0A37: 7E              LD      A,(HL)              ;
0A38: C6 05           ADD     A,$05               ;
0A3A: 77              LD      (HL),A              ;
0A3B: 2D              DEC     L                   ;
0A3C: C3 16 0A        JP      $0A16               ;
0A3F: 1F              RRA                         ;
0A40: 6F              LD      L,A                 ;
0A41: 26 00           LD      H,$00               ;
0A43: CD AA 01        CALL    $01AA               ; Write tone
0A46: AF              XOR     A                   ;
0A47: C9              RET                         ;
0A48: 3E FF           LD      A,$FF               ;
0A4A: C9              RET                         ;
```

# Command 19

```code
Command19: 
; Initialization Routine Vector 19 (Time Jump 2)
0A4B: AF              XOR     A                   ;
0A4C: CD C8 01        CALL    $01C8               ;{FilterCaps}
0A4F: 21 C0 00        LD      HL,$00C0            ;
0A52: CD AA 01        CALL    $01AA               ; Write tone
0A55: 0E 0F           LD      C,$0F               ;
0A57: CD 99 01        CALL    $0199               ; Set volume
0A5A: 21 9F 30        LD      HL,$309F            ;
0A5D: 36 00           LD      (HL),$00            ;
0A5F: 2C              INC     L                   ;
0A60: 36 10           LD      (HL),$10            ;
0A62: 2C              INC     L                   ;
0A63: 36 03           LD      (HL),$03            ;
0A65: 2C              INC     L                   ;
0A66: 36 05           LD      (HL),$05            ;
0A68: AF              XOR     A                   ;
0A69: C9              RET                         ;

; Continue Sound Routine Vector 19 (Time Jump 2)
0A6A: 21 9F 30        LD      HL,$309F            ;
0A6D: 35              DEC     (HL)                ;
0A6E: 7E              LD      A,(HL)              ;
0A6F: 2C              INC     L                   ;
0A70: E6 3F           AND     $3F                 ;
0A72: 20 03           JR      NZ,$A77             ;
0A74: 35              DEC     (HL)                ;
0A75: 28 19           JR      Z,$A90              ;
0A77: E6 03           AND     $03                 ;
0A79: 20 13           JR      NZ,$A8E             ;
0A7B: 56              LD      D,(HL)              ;
0A7C: 2C              INC     L                   ;
0A7D: 7E              LD      A,(HL)              ;
0A7E: C6 05           ADD     A,$05               ;
0A80: 77              LD      (HL),A              ;
0A81: 2C              INC     L                   ;
0A82: AE              XOR     (HL)                ;
0A83: E6 0F           AND     $0F                 ;
0A85: 77              LD      (HL),A              ;
0A86: BA              CP      D                   ;
0A87: 38 01           JR      C,$A8A              ;
0A89: AF              XOR     A                   ;
0A8A: 4F              LD      C,A                 ;
0A8B: CD 99 01        CALL    $0199               ; Set volume
0A8E: AF              XOR     A                   ;
0A8F: C9              RET                         ;
0A90: 3D              DEC     A                   ;
0A91: C9              RET                         ;
```

# Command Table

```code
CommandTable: 
; Initialize sound routines
0A92: 97 01 ; 0   Stop all sounds
0A94: E7 03 ; 1  0 Coin Drop
0A96: 32 04 ; 2  0 Plane Fire
0A98: 62 04 ; 3  0 1910 Bomb
0A9A: 9A 04 ; 4  1 Missile launch
0A9C: D9 04 ; 5  0 Missile (continuous)
0A9E: 0A 05 ; 6  0 UFO shot
0AA0: 4D 05 ; 7  0 User Fire
0AA2: 88 05 ; 8  1 Enemy Explosion Component (thud)
0AA4: C8 05 ; 9  1 Enemy Explosion Component (white-noise)
0AA6: 1B 06 ; A  0 Tracker or Bomb Explosion
0AA8: 5E 06 ; B  0 Squad Appears
0AAA: 95 06 ; C  1 1st Boss
0AAC: D9 06 ; D  1 2nd Boss
0AAE: 15 07 ; E  1 3rd Boss
0AB0: 5C 07 ; F  1 4th Boss
0AB2: 8A 07 ; 10 1 5th Boss
0AB4: C6 07 ; 11 1 User Explosion Component
0AB6: 0B 08 ; 12 1 User Explosion Component
0AB8: 57 08 ; 13 2 User Explosion Component
0ABA: D0 08 ; 14 2 User Explosion Component
0ABC: 44 09 ; 15 1 User Explosion Component
0ABE: 9C 09 ; 16 0 Pickup Parachute
0AC0: D1 09 ; 17 1 Free Man
0AC2: 02 0A ; 18 0 Time Jump 1
0AC4: 4B 0A ; 19 0 Time Jump 2
0AC6: 16 0B ; 1A 0 Initialize song 2
0AC8: 1A 0B ; 1B 1 Initialize song 1
0ACA: 3B 0B ; 1C 0 Initialize music D1
0ACC: 3B 0B ; 1D 0 Initialize music D2
0ACE: 3B 0B ; 1E 0 Initialize music D3
0AD0: 3B 0B ; 1F 0 Initialize music D4
0AD2: 3B 0B ; 20 0 Initialize music D5

; Continue sound routines
0AD4: 00 00 ; 0 Place holder for stop-all-commands
0AD6: 02 04 ; 1
0AD8: 4B 04 ; 2
0ADA: 7A 04 ; 3 
0ADC: B3 04 ; 4 
0ADE: F5 04 ; 5
0AE0: 28 05 ; 6
0AE2: 6C 05 ; 7
0AE4: A4 05 ; 8
0AE6: EA 05 ; 9
0AE8: 3A 06 ; A
0AEA: 77 06 ; B
0AEC: B4 06 ; C
0AEE: F6 06 ; D
0AF0: 32 07 ; E
0AF2: 74 07 ; F
0AF4: AA 07 ; 10
0AF6: E5 07 ; 11
0AF8: 29 08 ; 12
0AFA: 7F 08 ; 13
0AFC: F8 08 ; 14
0AFE: 66 09 ; 15
0B00: BC 09 ; 16
0B02: F1 09 ; 17
0B04: 20 0A ; 18
0B06: 6A 0A ; 19
0B08: 00 00 ; 1A -- Playing song 0 (never kept in buffer)
0B0A: 00 00 ; 1B -- Playing song 1 (never kept in buffer)
0B0C: 41 0B ; 1C Continue music D1
0B0E: 4A 0B ; 1D Continue music D2
0B10: 53 0B ; 1E Continue music D3
0B12: 5C 0B ; 1F Continue music D4
0B14: 65 0B ; 20 Continue music D5
```

# Command 1A

```code
Command1A: 
; Initialization Routine Vector 1A
0B16: AF              XOR     A                   ; Play song 0
0B17: C3 1C 0B        JP      $0B1C               ; Play it
```

# Command 1B

```code
Command1B: 
; Initialization Routine Vector 1B
0B1A: 3E 01           LD      A,$01               ; Play song 1
0B1C: CD 7E 03        CALL    $037E               ; Initialize music descriptors
0B1F: 11 00 30        LD      DE,$3000            ; Command table
0B22: 21 2F 0B        LD      HL,$0B2F            ; Fill ...
0B25: 01 0C 00        LD      BC,$000C            ; ... simultaneous
0B28: ED B0           LDIR                        ; ... commands
0B2A: E1              POP     HL                  ; Clean ...
0B2B: E1              POP     HL                  ; ... stack frame
0B2C: C3 BF 00        JP      $00BF               ;{MainLoop} Goto main loop

; Play song command buffer
0B2F: 1C 00 ; All five music processors playing
0B31: 1D 00 ; ...
0B33: 1E 00 ; ...
0B35: 1F 00 ; ...
0B37: 20 00 ; ...
0B39: 00 00 ;

; Initialization Routine Vector 1C,1D,1E,1F,20 Music
; Do nothing.
0B3B: AF              XOR     A                   ;
0B3C: CD C8 01        CALL    $01C8               ; Set the filter caps
0B3F: AF              XOR     A                   ; Initialized
0B40: C9              RET                         ; Done

; Continue Sound Routine Vector 1C
0B41: DD 21 0F 30     LD      IX,$300F            ; Descriptor 1
0B45: CD FC 01        CALL    $01FC               ;{MusicProcessing} Process
0B48: AF              XOR     A                   ; Continue flag
0B49: C9              RET                         ; Done

; Continue Sound Routine Vector 1D
0B4A: DD 21 19 30     LD      IX,$3019            ; Descriptor 2
0B4E: CD FC 01        CALL    $01FC               ;{MusicProcessing} Process
0B51: AF              XOR     A                   ; Continue flag
0B52: C9              RET                         ; Done

; Continue Sound Routine Vector 1E
0B53: DD 21 23 30     LD      IX,$3023            ; Descriptor 3
0B57: CD FC 01        CALL    $01FC               ;{MusicProcessing} Process
0B5A: AF              XOR     A                   ; Continue flag
0B5B: C9              RET                         ; Done

; Continue Sound Routine Vector 1F
0B5C: DD 21 2D 30     LD      IX,$302D            ; Descriptor 4
0B60: CD FC 01        CALL    $01FC               ;{MusicProcessing} Process
0B63: AF              XOR     A                   ; Continue flag
0B64: C9              RET                         ; Done

; Continue Sound Routine Vector 20
0B65: DD 21 37 30     LD      IX,$3037            ; Descriptor 5
0B69: CD FC 01        CALL    $01FC               ;{MusicProcessing} Process
0B6C: AF              XOR     A                   ; Continue flag
0B6D: C9              RET                         ; Done
```

# Music Data

```code
MusicData: 
; Music pointers for songs (10 bytes each)
; Song 0 (Start of game)
0B6E: 82 0B 
0B70: B2 0B 
0B72: E2 0B 
0B74: 08 0C 
0B76: 2D 0C
 
; Song 1 (Enter you initials)
0B78: 2E 0C 
0B7A: 70 0C 
0B7C: AD 0C 
0B7E: EB 0C 
0B80: 04 0D 

;Song data

; Start of game song

; Song 0 Descriptor 0
0B82: 1F 0E ; MusCmd0: Set base note pointer to 0326 (C4)
0B84: 3F 16 ; MusCmd1: Set base delay to 16
0B86: 5F 00 ; MusCmd2: Set initial note volume to 00
0B88: 81    ; delay=4, note=C4+0:  C4
0B89: 60    ; delay=3, note=rest
0B8A: 5F 08 ; MusCmd2: Set initial note volume to 08
0B8C: 66    ; delay=3, note=C4+5:  F4
0B8D: A8    ; delay=5, note=C4+7:  G4
0B8E: AD    ; delay=5, note=C4+12: C5
0B8F: 92    ; delay=4, note=C4+17: F5
0B90: 7F 00 ; MusCmd3: Set volume modification to 0
0B92: B1    ; delay=5, note=C4+16: E5
0B93: 91    ; delay=4, note=C4+16: E5
0B94: 7F FF ; MusCmd3: Set volume modification to -1
0B96: B1    ; delay=5, note=C4+16: E5
0B97: B2    ; delay=5, note=C4+17: F5
0B98: 91    ; delay=4, note=C4+16: E5
0B99: 7F 00 ; MusCmd3: Set volume modification to 0
0B9B: D4    ; delay=6, note=C4+19: G5
0B9C: B4    ; delay=5, note=C4+19: G5
0B9D: 7F FF ; MusCmd3: Set volume modification to -1
0B9F: B4    ; delay=5, note=C4+19: G5
0BA0: 60    ; delay=3, note=rest
0BA1: 74    ; delay=3, note=C4+19: G5
0BA2: 3F 13 ; MusCmd1: Set base delay to 13
0BA4: 77    ; delay=3, note=C4+22: A#5
0BA5: 76    ; delay=3, note=C4+21: A5
0BA6: 74    ; delay=3, note=C4+19: G5
0BA7: 74    ; delay=3, note=C4+19: G5
0BA8: 73    ; delay=3, note=C4+18: F#5
0BA9: 71    ; delay=3, note=C4+16: E5
0BAA: 71    ; delay=3, note=C4+16: E5
0BAB: 70    ; delay=3, note=C4+15: D#5
0BAC: 6D    ; delay=3, note=C4+12: C5
0BAD: 6D    ; delay=3, note=C4+12: C5
0BAE: 70    ; delay=3, note=C4+15: D#5
0BAF: 71    ; delay=3, note=C4+16: E5
0BB0: AD    ; delay=5, note=C4+12: C5
0BB1: FF    ; END

; Song 0 Descriptor 1
0BB2: 1F 02 ; MusCmd0: Set base note pointer to 02F6 (C2)
0BB4: 3F 16 ; MusCmd1: Set base delay to 16
0BB6: 5F 00 ; MusCmd2: Set initial note volume to 00
0BB8: 81    ; delay=4, note=C2+0:  C2
0BB9: 60    ; delay=3, note=rest
0BBA: 5F 08 ; MusCmd2: Set initial note volume to 08
0BBC: 66    ; delay=3, note=C2+5:  F2
0BBD: A8    ; delay=5, note=C2+7:  G2
0BBE: AD    ; delay=5, note=C2+12: C3
0BBF: 92    ; delay=4, note=C2+17: F3
0BC0: 7F 00 ; MusCmd3: Set volume modification to 0
0BC2: B1    ; delay=5, note=C2+16: E3
0BC3: 91    ; delay=4, note=C2+16: E3
0BC4: 7F FF ; MusCmd3: Set volume modification to -1
0BC6: B1    ; delay=5, note=C2+16: E3
0BC7: B2    ; delay=5, note=C2+17: F3
0BC8: 91    ; delay=4, note=C2+16: E3
0BC9: 7F 00 ; MusCmd3: Set volume modification to 0
0BCB: D4    ; delay=6, note=C2+19: G3
0BCC: B4    ; delay=5, note=C2+19: G3
0BCD: 7F FF ; MusCmd3: Set volume modification to -1
0BCF: B4    ; delay=5, note=C2+19: G3
0BD0: 60    ; delay=3, note=rest
0BD1: 74    ; delay=3, note=C2+19: G3
0BD2: 3F 13 ; MusCmd1: Set base delay to 13
0BD4: 77    ; delay=3, note=C2+22: A#3
0BD5: 76    ; delay=3, note=C2+21: A3
0BD6: 74    ; delay=3, note=C2+19: G3
0BD7: 74    ; delay=3, note=C2+19: G3
0BD8: 73    ; delay=3, note=C2+18: F#3
0BD9: 71    ; delay=3, note=C2+16: E3
0BDA: 71    ; delay=3, note=C2+16: E3
0BDB: 70    ; delay=3, note=C2+15: D#3
0BDC: 6D    ; delay=3, note=C2+12: C3
0BDD: 6D    ; delay=3, note=C2+12: C3
0BDE: 70    ; delay=3, note=C2+15: D#3
0BDF: 71    ; delay=3, note=C2+16: E3
0BE0: AD    ; delay=5, note=C2+12: C3
0BE1: FF    ; END

; Song 0 Descriptor 2
0BE2: 1F 0E ; MusCmd0: Set base note pointer to 0326 (C4)
0BE4: 3F 13 ; MusCmd1: Set base delay to 13
0BE6: 5F 08 ; MusCmd2: Set initial note volume to 08
0BE8: 8D    ; delay=4, note=C4+12: C5
0BE9: 6D    ; delay=3, note=C4+12: C5
0BEA: 8D    ; delay=4, note=C4+12: C5
0BEB: 6D    ; delay=3, note=C4+12: C5
0BEC: 8D    ; delay=4, note=C4+12: C5
0BED: 6D    ; delay=3, note=C4+12: C5
0BEE: 8D    ; delay=4, note=C4+12: C5
0BEF: 6D    ; delay=3, note=C4+12: C5
0BF0: 8D    ; delay=4, note=C4+12: C5
0BF1: 6D    ; delay=3, note=C4+12: C5
0BF2: 8D    ; delay=4, note=C4+12: C5
0BF3: 6D    ; delay=3, note=C4+12: C5
0BF4: 8D    ; delay=4, note=C4+12: C5
0BF5: 6D    ; delay=3, note=C4+12: C5
0BF6: 8D    ; delay=4, note=C4+12: C5
0BF7: 6D    ; delay=3, note=C4+12: C5
0BF8: 88    ; delay=4, note=C4+7:  G4
0BF9: 68    ; delay=3, note=C4+7:  G4
0BFA: 85    ; delay=4, note=C4+4:  E4
0BFB: 60    ; delay=3, note=rest
0BFC: 86    ; delay=4, note=C4+5:  F4
0BFD: 60    ; delay=3, note=rest
0BFE: 87    ; delay=4, note=C4+6:  F#4
0BFF: 60    ; delay=3, note=rest
0C00: 7F 00 ; MusCmd3: Set volume modification to 0
0C02: CB    ; delay=6, note=C4+10: A#4
0C03: 7F FF ; MusCmd3: Set volume modification to -1
0C05: AB    ; delay=5, note=C4+10: A#4
0C06: AD    ; delay=5, note=C4+12: C5
0C07: FF    ; END

; Song 0 Descriptor 3
0C08: 1F 02 ; MusCmd0: Set base note pointer to 02F6 (C2)
0C0A: 3F 13 ; MusCmd1: Set base delay to 13
0C0C: 5F 08 ; MusCmd2: Set initial note volume to 08
0C0E: 8D    ; delay=4, note=C2+12: C3
0C0F: 6D    ; delay=3, note=C2+12: C3
0C10: 8D    ; delay=4, note=C2+12: C3
0C11: 6D    ; delay=3, note=C2+12: C3
0C12: 8D    ; delay=4, note=C2+12: C3
0C13: 6D    ; delay=3, note=C2+12: C3
0C14: 8D    ; delay=4, note=C2+12: C3
0C15: 6D    ; delay=3, note=C2+12: C3
0C16: 8D    ; delay=4, note=C2+12: C3
0C17: 6D    ; delay=3, note=C2+12: C3
0C18: 8D    ; delay=4, note=C2+12: C3
0C19: 6D    ; delay=3, note=C2+12: C3
0C1A: 8D    ; delay=4, note=C2+12: C3
0C1B: 6D    ; delay=3, note=C2+12: C3
0C1C: 8D    ; delay=4, note=C2+12: C3
0C1D: 6D    ; delay=3, note=C2+12: C3
0C1E: 88    ; delay=4, note=C2+7:  G2
0C1F: 68    ; delay=3, note=C2+7:  G2
0C20: 85    ; delay=4, note=C2+4:  E2
0C21: 60    ; delay=3, note=rest
0C22: 86    ; delay=4, note=C2+5:  F2
0C23: 60    ; delay=3, note=rest
0C24: 87    ; delay=4, note=C2+6:  F#2
0C25: 60    ; delay=3, note=rest
0C26: 7F 00 ; MusCmd3: Set volume modification to 0
0C28: CB    ; delay=6, note=C2+10: A#2
0C29: 7F FF ; MusCmd3: Set volume modification to -1
0C2B: AB    ; delay=5, note=C2+10: A#2
0C2C: AD    ; delay=5, note=C2+12: C3

; Song 0 Descriptor 4
0C2D: FF    ; END

; Enter-your-initials song. This loops.

; Song 1 Descriptor 0
0C2E: 1F 0E ; MusCmd0: Set base note pointer to 0326 (C4 middle C)
0C30: 3F 15 ; MusCmd1: Set base delay to 15
0C32: 5F 00 ; MusCmd2: Set initial note volume to 00
0C34: 81    ; delay=4, note=C4+0:  C4
0C35: 5F 07 ; MusCmd2: Set initial note volume to 07
0C37: 65    ; delay=3, note=C4+4:  E4
0C38: 65    ; delay=3, note=C4+4:  E4
0C39: 25    ; delay=1, note=C4+4:  E4
0C3A: 25    ; delay=1, note=C4+4:  E4
0C3B: 25    ; delay=1, note=C4+4:  E4
0C3C: 25    ; delay=1, note=C4+4:  E4
0C3D: A5    ; delay=5, note=C4+4:  E4
0C3E: 85    ; delay=4, note=C4+4:  E4
0C3F: 65    ; delay=3, note=C4+4:  E4
0C40: 85    ; delay=4, note=C4+4:  E4
0C41: 65    ; delay=3, note=C4+4:  E4
0C42: 65    ; delay=3, note=C4+4:  E4
0C43: 80    ; delay=4, note=rest
0C44: 65    ; delay=3, note=C4+4:  E4
0C45: 65    ; delay=3, note=C4+4:  E4
0C46: 25    ; delay=1, note=C4+4:  E4
0C47: 25    ; delay=1, note=C4+4:  E4
0C48: 25    ; delay=1, note=C4+4:  E4
0C49: 25    ; delay=1, note=C4+4:  E4
0C4A: A5    ; delay=5, note=C4+4:  E4
0C4B: 85    ; delay=4, note=C4+4:  E4
0C4C: 65    ; delay=3, note=C4+4:  E4
0C4D: 61    ; delay=3, note=C4+0:  C4
0C4E: 68    ; delay=3, note=C4+7:  G4
0C4F: 6C    ; delay=3, note=C4+11: B4
0C50: 6F    ; delay=3, note=C4+14: D5
0C51: 80    ; delay=4, note=rest
0C52: 6A    ; delay=3, note=C4+9:  A4
0C53: 6A    ; delay=3, note=C4+9:  A4
0C54: 2A    ; delay=1, note=C4+9:  A4
0C55: 2A    ; delay=1, note=C4+9:  A4
0C56: 2A    ; delay=1, note=C4+9:  A4
0C57: 2A    ; delay=1, note=C4+9:  A4
0C58: AA    ; delay=5, note=C4+9:  A4
0C59: 8A    ; delay=4, note=C4+9:  A4
0C5A: 6A    ; delay=3, note=C4+9:  A4
0C5B: 8A    ; delay=4, note=C4+9:  A4
0C5C: 6A    ; delay=3, note=C4+9:  A4
0C5D: 6A    ; delay=3, note=C4+9:  A4
0C5E: 80    ; delay=4, note=rest
0C5F: 6A    ; delay=3, note=C4+9:  A4
0C60: 6A    ; delay=3, note=C4+9:  A4
0C61: 2A    ; delay=1, note=C4+9:  A4
0C62: 2A    ; delay=1, note=C4+9:  A4
0C63: 2A    ; delay=1, note=C4+9:  A4
0C64: 2A    ; delay=1, note=C4+9:  A4
0C65: AA    ; delay=5, note=C4+9:  A4
0C66: 8A    ; delay=4, note=C4+9:  A4
0C67: 68    ; delay=3, note=C4+7:  G4
0C68: 68    ; delay=3, note=C4+7:  G4
0C69: 68    ; delay=3, note=C4+7:  G4
0C6A: 6A    ; delay=3, note=C4+9:  A4
0C6B: 6A    ; delay=3, note=C4+9:  A4
0C6C: 80    ; delay=4, note=rest
0C6D: DF 37 0C ; MusCmd6: GOTO 0C37

; Song 1 Descriptor 1
0C70: 1F 0E ; MusCmd0: Set base note pointer to 0326 (C4 middle C)
0C72: 3F 15 ; MusCmd1: Set base delay to 15
0C74: 5F 00 ; MusCmd2: Set initial note volume to 00
0C76: 81    ; delay=4, note=C4+0:  C4
0C77: 5F 07 ; MusCmd2: Set initial note volume to 07
0C79: 68    ; delay=3, note=C4+7:  G4
0C7A: 68    ; delay=3, note=C4+7:  G4
0C7B: 28    ; delay=1, note=C4+7:  G4
0C7C: 28    ; delay=1, note=C4+7:  G4
0C7D: 28    ; delay=1, note=C4+7:  G4
0C7E: 28    ; delay=1, note=C4+7:  G4
0C7F: A8    ; delay=5, note=C4+7:  G4
0C80: 88    ; delay=4, note=C4+7:  G4
0C81: 68    ; delay=3, note=C4+7:  G4
0C82: 88    ; delay=4, note=C4+7:  G4
0C83: 68    ; delay=3, note=C4+7:  G4
0C84: 68    ; delay=3, note=C4+7:  G4
0C85: 80    ; delay=4, note=rest
0C86: 68    ; delay=3, note=C4+7:  G4
0C87: 68    ; delay=3, note=C4+7:  G4
0C88: 28    ; delay=1, note=C4+7:  G4
0C89: 28    ; delay=1, note=C4+7:  G4
0C8A: 28    ; delay=1, note=C4+7:  G4
0C8B: 28    ; delay=1, note=C4+7:  G4
0C8C: A8    ; delay=5, note=C4+7:  G4
0C8D: 88    ; delay=4, note=C4+7:  G4
0C8E: A8    ; delay=5, note=C4+7:  G4
0C8F: 60    ; delay=3, note=rest
0C90: 80    ; delay=4, note=rest
0C91: 6D    ; delay=3, note=C4+12: C5
0C92: 6D    ; delay=3, note=C4+12: C5
0C93: 2D    ; delay=1, note=C4+12: C5
0C94: 2D    ; delay=1, note=C4+12: C5
0C95: 2D    ; delay=1, note=C4+12: C5
0C96: 2D    ; delay=1, note=C4+12: C5
0C97: AD    ; delay=5, note=C4+12: C5
0C98: 8D    ; delay=4, note=C4+12: C5
0C99: 6D    ; delay=3, note=C4+12: C5
0C9A: 8D    ; delay=4, note=C4+12: C5
0C9B: 6D    ; delay=3, note=C4+12: C5
0C9C: 6D    ; delay=3, note=C4+12: C5
0C9D: 80    ; delay=4, note=rest
0C9E: 6D    ; delay=3, note=C4+12: C5
0C9F: 6D    ; delay=3, note=C4+12: C5
0CA0: 2D    ; delay=1, note=C4+12: C5
0CA1: 2D    ; delay=1, note=C4+12: C5
0CA2: 2D    ; delay=1, note=C4+12: C5
0CA3: 2D    ; delay=1, note=C4+12: C5
0CA4: AD    ; delay=5, note=C4+12: C5
0CA5: 8D    ; delay=4, note=C4+12: C5
0CA6: 6D    ; delay=3, note=C4+12: C5
0CA7: 6D    ; delay=3, note=C4+12: C5
0CA8: 6D    ; delay=3, note=C4+12: C5
0CA9: AD    ; delay=5, note=C4+12: C5
0CAA: DF 79 0C ; MusCmd6: GOTO 0C79

; Song 1 Descriptor 2
0CAD: 1F 0E ; MusCmd0: Set base note pointer to 0326 (C4 middle C)
0CAF: 3F 15 ; MusCmd1: Set base delay to 15
0CB1: 5F 00 ; MusCmd2: Set initial note volume to 00
0CB3: 81    ; delay=4, note=C4+0: C4
0CB4: 5F 07 ; MusCmd2: Set initial note volume to 07
0CB6: 6C    ; delay=3, note=C4+11: B4
0CB7: 6C    ; delay=3, note=C4+11: B4
0CB8: 2C    ; delay=1, note=C4+11: B4
0CB9: 2C    ; delay=1, note=C4+11: B4
0CBA: 2C    ; delay=1, note=C4+11: B4
0CBB: 2C    ; delay=1, note=C4+11: B4
0CBC: AC    ; delay=5, note=C4+11: B4
0CBD: 8C    ; delay=4, note=C4+11: B4
0CBE: 6C    ; delay=3, note=C4+11: B4
0CBF: 8C    ; delay=4, note=C4+11: B4
0CC0: 6C    ; delay=3, note=C4+11: B4
0CC1: 6C    ; delay=3, note=C4+11: B4
0CC2: 80    ; delay=4, note=rest
0CC3: 6C    ; delay=3, note=C4+11: B4
0CC4: 6C    ; delay=3, note=C4+11: B4
0CC5: 2C    ; delay=1, note=C4+11: B4
0CC6: 2C    ; delay=1, note=C4+11: B4
0CC7: 2C    ; delay=1, note=C4+11: B4
0CC8: 2C    ; delay=1, note=C4+11: B4
0CC9: AC    ; delay=5, note=C4+11: B4
0CCA: 8C    ; delay=4, note=C4+11: B4
0CCB: AC    ; delay=5, note=C4+11: B4
0CCC: 60    ; delay=3, note=rest
0CCD: 80    ; delay=4, note=rest
0CCE: 72    ; delay=3, note=C4+17: F5
0CCF: 72    ; delay=3, note=C4+17: F5
0CD0: 32    ; delay=1, note=C4+17: F5
0CD1: 32    ; delay=1, note=C4+17: F5
0CD2: 32    ; delay=1, note=C4+17: F5
0CD3: 32    ; delay=1, note=C4+17: F5
0CD4: B2    ; delay=5, note=C4+17: F5
0CD5: 92    ; delay=4, note=C4+17: F5
0CD6: 72    ; delay=3, note=C4+17: F5
0CD7: 92    ; delay=4, note=C4+17: F5
0CD8: 72    ; delay=3, note=C4+17: F5
0CD9: 72    ; delay=3, note=C4+17: F5
0CDA: 80    ; delay=4, note=rest
0CDB: 72    ; delay=3, note=C4+17: F5
0CDC: 72    ; delay=3, note=C4+17: F5
0CDD: 32    ; delay=1, note=C4+17: F5
0CDE: 32    ; delay=1, note=C4+17: F5
0CDF: 32    ; delay=1, note=C4+17: F5
0CE0: 32    ; delay=1, note=C4+17: F5
0CE1: B2    ; delay=5, note=C4+17: F5
0CE2: 92    ; delay=4, note=C4+17: F5
0CE3: 72    ; delay=3, note=C4+17: F5
0CE4: 72    ; delay=3, note=C4+17: F5
0CE5: 72    ; delay=3, note=C4+17: F5
0CE6: 92    ; delay=4, note=C4+17: F5
0CE7: 80    ; delay=4, note=rest
0CE8: DF B6 0C ; MusCmd6: GOTO 0CB6

; Song 1 Descriptor 3
0CEB: 1F 0E ; MusCmd0: Set base note pointer to 0326 (C4 middle C)
0CED: 3F 15 ; MusCmd1: Set base delay to 15
0CEF: 5F 00 ; MusCmd2: Set initial note volume to 00
0CF1: E1    ; delay=7, note=C4+0: C4
0CF2: E0    ; delay=7, note=rest
0CF3: E0    ; delay=7, note=rest
0CF4: C0    ; delay=6, note=rest
0CF5: A0    ; delay=5, note=rest
0CF6: 5F 07 ; MusCmd2: Set initial note volume to 07
0CF8: 78    ; delay=3, note=C4+23: B5
0CF9: 74    ; delay=3, note=C4+19: G5
0CFA: 79    ; delay=3, note=C4+24: C6
0CFB: 76    ; delay=3, note=C4+21: A5
0CFC: E0    ; delay=7, note=rest
0CFD: E0    ; delay=7, note=rest
0CFE: E0    ; delay=7, note=rest
0CFF: C0    ; delay=6, note=rest
0D00: A0    ; delay=5, note=rest
0D01: DF F8 0C ; MusCmd6: GOTO 0CF8

; Song 1 Descriptor 4
0D04: 1F 02 ; MusCmd0: Set base note pointer to 02F6 (C2)
0D06: 3F 15 ; MusCmd1: Set base delay to 15
0D08: 5F 07 ; MusCmd2: Set initial note volume to 07
0D0A: 8D    ; delay=4, note=C2+12: C3
0D0B: 60    ; delay=3, note=rest
0D0C: 6D    ; delay=3, note=C2+12: C3
0D0D: 88    ; delay=4, note=C2+7:  G2
0D0E: 60    ; delay=3, note=rest
0D0F: 6D    ; delay=3, note=C2+12: C3
0D10: 60    ; delay=3, note=rest
0D11: 6D    ; delay=3, note=C2+12: C3
0D12: 60    ; delay=3, note=rest
0D13: 6D    ; delay=3, note=C2+12: C3
0D14: 28    ; delay=1, note=C2+7:  G2
0D15: 28    ; delay=1, note=C2+7:  G2
0D16: 28    ; delay=1, note=C2+7:  G2
0D17: 28    ; delay=1, note=C2+7:  G2
0D18: 88    ; delay=4, note=C2+7:  G2
0D19: 60    ; delay=3, note=rest
0D1A: 8D    ; delay=4, note=C2+12: C3
0D1B: 60    ; delay=3, note=rest
0D1C: 6D    ; delay=3, note=C2+12: C3
0D1D: 88    ; delay=4, note=C2+7:  G2
0D1E: 60    ; delay=3, note=rest
0D1F: 6D    ; delay=3, note=C2+12: C3
0D20: 60    ; delay=3, note=rest
0D21: 6D    ; delay=3, note=C2+12: C3
0D22: 60    ; delay=3, note=rest
0D23: 6D    ; delay=3, note=C2+12: C3
0D24: 88    ; delay=4, note=C2+7:  G2
0D25: 6D    ; delay=3, note=C2+12: C3
0D26: 68    ; delay=3, note=C2+7:  G2
0D27: 8F    ; delay=4, note=C2+14: D3
0D28: 60    ; delay=3, note=rest
0D29: 6F    ; delay=3, note=C2+14: D3
0D2A: 8A    ; delay=4, note=C2+9:  A2
0D2B: 60    ; delay=3, note=rest
0D2C: 6F    ; delay=3, note=C2+14: D3
0D2D: 60    ; delay=3, note=rest
0D2E: 6F    ; delay=3, note=C2+14: D3
0D2F: 60    ; delay=3, note=rest
0D30: 6F    ; delay=3, note=C2+14: D3
0D31: 2A    ; delay=1, note=C2+9:  A2
0D32: 2A    ; delay=1, note=C2+9:  A2
0D33: 2A    ; delay=1, note=C2+9:  A2
0D34: 2A    ; delay=1, note=C2+9:  A2
0D35: 8A    ; delay=4, note=C2+9:  A2
0D36: 60    ; delay=3, note=rest
0D37: 8F    ; delay=4, note=C2+14: D3
0D38: 60    ; delay=3, note=rest
0D39: 6F    ; delay=3, note=C2+14: D3
0D3A: 8A    ; delay=4, note=C2+9:  A2
0D3B: 60    ; delay=3, note=rest
0D3C: 8F    ; delay=4, note=C2+14: D3
0D3D: 8F    ; delay=4, note=C2+14: D3
0D3E: 6F    ; delay=3, note=C2+14: D3
0D3F: 6A    ; delay=3, note=C2+9:  A2
0D40: 6F    ; delay=3, note=C2+14: D3
0D41: 6A    ; delay=3, note=C2+9:  A2
0D42: 6E    ; delay=3, note=C2+13: C#3
0D43: DF 0A 0D ; MusCmd6: GOTO 0D0A
      
; ?? Is this a song fragment left over from something else?
; ?? It reference sound command 5, which has been removed to
; ?? end-of-song.
0D46: 1F 0E ; MusCmd0: Set base note pointer to 0326 (C4 middle C)
0D48: 3F 16 ; MusCmd1: Set base delay to 16
0D4A: 5F 09 ; MusCmd2: Set initial note volume to 09
0D4C: BF B3 ; MusCmd5: ??? B3
; These are probably not notes. They are probably data bytes for command 5?
0D4E: B2    ; delay=5, note=C4+17: F5
0D4F: A9    ; delay=5, note=C4+8: G#4
0D50: B0    ; delay=5, note=C4+15: D#5
0D51: B9    ; delay=5, note=C4+24: C6
0D52: BB    ; delay=5, note=C4+26: D6
0D53: BA    ; delay=5, note=C4+25: C#6
0D54: AE    ; delay=5, note=C4+13: C#5
0D55: E2    ; delay=7, note=C4+1: C#4
0D56: B7    ; delay=5, note=C4+22: A#5
0D57: B3    ; delay=5, note=C4+18: F#5
0D58: B4    ; delay=5, note=C4+19: G5
0D59: C1    ; delay=6, note=C4+0: C4
0D5A: B5    ; delay=5, note=C4+20: G#5
0D5B: B9    ; delay=5, note=C4+24: C6
0D5C: FF    ; END

; Not used (space on the end of the ROM)

0D5D: FF FF FF
0D60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0D70: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0D80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0D90: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0DA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0DB0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0DC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0DD0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0DE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0DF0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

0E00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0E10: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0E20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0E30: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0E40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0E50: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0E60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0E70: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0E80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0E90: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0EA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0EB0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0EC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0ED0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0EE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0EF0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

0F00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0F10: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0F20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0F30: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0F40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0F50: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0F60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0F70: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0F80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0F90: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0FA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0FB0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0FC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0FD0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0FE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0FF0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
```