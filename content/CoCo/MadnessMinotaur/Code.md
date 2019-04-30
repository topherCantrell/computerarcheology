![Code](Madness.jpg)

# Code

>>> cpu 6809

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

# Start

Patch BASIC for our own use.

```code
START:
0300: 1A 50               ORCC    #$50                      ; Disable IRQ, FIRQ
0302: BD A7 EB            JSR     $A7EB                     ; Turns motor off (leave IRQ and FIRQ off) (BASIC)
0305: 8E 03 2D            LDX     #$032D                    ; Print character code (relocatable)
0308: CE 00 A5            LDU     #$00A5                    ; Destination (over BASIC's GETCCH routine)
030B: A6 80               LDA     ,X+                       ; Copy ...
030D: A7 C0               STA     ,U+                       ; ... the ...
030F: 8C 03 75            CMPX    #$0375                    ; ... print character ...
0312: 25 F7               BCS     $30B                      ; ... routine
0314: CE 01 1D            LDU     #$011D                    ; Tape-write routine
0317: A6 80               LDA     ,X+                       ; Copy ...
0319: A7 C0               STA     ,U+                       ; ... the ...
031B: 8C 03 E8            CMPX    #$03E8                    ; ... tape-write ...
031E: 23 F7               BLS     $317                      ; ... routine
0320: CE 0C E0            LDU     #$0CE0                    ; Start address
0323: EF E3               STU     ,--S                      ; To stack
0325: C6 60               LDB     #$60                      ; Space character
0327: 8E 02 00            LDX     #$0200                    ; Start of screen
032A: 7E A9 2F            JMP     $A92F                     ; Clear screen (leave cursor alone) and to 0CE0 (BASIC)
;
; BASIC's GETCCH routine ... do nothing (lets call to CLOADM succeed)
032D: 39                  RTS                               ; To A5
```

# Print a Character

 A6 -- Print character in A with scrolling. This screen is TWO screens long
 so that the user can use UP and DOWN to switch between screens. This replaces
 BASIC's one-screen print.

```code
PrintChar:
032E: 34 16               PSHS    X,B,A                     ; Save parameters
0330: 9E 88               LDX     <$88                      ; {ram:scrCursor} Cursor
0332: 81 08               CMPA    #$08                      ; Printing a backspace?
0334: 26 0B               BNE     $341                      ; No ... move on
0336: 8C 02 00            CMPX    #$0200                    ; Already at top of screen (double screen)
0339: 27 38               BEQ     $373                      ; Yes ... ignore it (done)
033B: 86 60               LDA     #$60                      ; Space
033D: A7 82               STA     ,-X                       ; Over last in buffer
033F: 20 25               BRA     $366                      ; Store new cursor and out
;
0341: 81 0D               CMPA    #$0D                      ; CR?
0343: 26 0C               BNE     $351                      ; No ... move on
0345: 86 60               LDA     #$60                      ; Space
0347: A7 80               STA     ,X+                       ; Fill ...
0349: 1F 10               TFR     X,D                       ; ... out rest ...
034B: C5 1F               BITB    #$1F                      ; ... of line ...
034D: 26 F6               BNE     $345                      ; with spaces
034F: 20 15               BRA     $366                      ; Store new cursor and out
;
0351: 81 20               CMPA    #$20                      ; Less than space?
0353: 25 1E               BCS     $373                      ; Yes ... just ignore
0355: 4D                  TSTA                              ; Special character?
0356: 2B 0C               BMI     $364                      ; Yes ... just store
0358: 81 40               CMPA    #$40                      ; Make ...
035A: 25 06               BCS     $362                      ; ... sure ...
035C: 81 60               CMPA    #$60                      ; .... to print ...
035E: 25 04               BCS     $364                      ; .... correct ...
0360: 84 DF               ANDA    #$DF                      ; .... case ...
0362: 88 40               EORA    #$40                      ; .... (black on green background)
0364: A7 80               STA     ,X+                       ; Store the character to screen, advance cursor
0366: 9F 88               STX     <$88                      ; {ram:scrCursor} New cursor
0368: 8C 05 FF            CMPX    #$05FF                    ; At the end of the line?
036B: 23 06               BLS     $373                      ; No ... out
036D: 8E 02 00            LDX     #$0200                    ; Scroll both ...
0370: 7E A3 4E            JMP     $A34E                     ; ... screens and out (sets cursor to last line) (BASIC)
0373: 35 96               PULS    A,B,X,PC                  ; Done
```

# Save to Tape

Before calling this, the QUIET routine copies 0000-00FF to 0240-033F.
Then we write two binary files here:
  * 0240-05FF (engine data and screen)
  * 3BC1-3FFF (tables) 

2111 (decimal) bytes written/read.

 1D1 -- Write game engine data from 0240-05FF (includes lower 256 bytes at 240).<br>
 This also gets the screen. Empty filename.<br>

 The game uses two screens to display the game: 0200-03FF and 0400-05FF (latter is the normal one).
 The player can switch between upper (past) and lower (current) screens with the up and down arrows.
 The SAVE process copies the game variables (the first 1K) into the upper screen's memory. It
 skips a few lines in the buffer because the QUIET command and OK will scroll. After you save
 or load you can see the sate of the game variables on the upper screen ... looks like garbage. I'm
 sure that was to 1) get the vars out with one save and 2) allow for debugging. That's the magic
 of the $240 address. 

```code
SaveToTape:

0375: 8E 01 D1            LDX     #$01D1                    ; 011D: Filename buffer
0378: 6F 80               CLR     ,X+                       ; 0120: Zero first byte of name
037A: CC 20 08            LDD     #$2008                    ; 0122: Write 20 (space) ...
037D: A7 80               STA     ,X+                       ; 0125: ... to next
037F: 5A                  DECB                              ; 0127: ... 8 ...
0380: 26 FB               BNE     $37D                      ; 0128: ... bytes
0382: 8E 02 40            LDX     #$0240                    ; 012A: Write buffer start (lower vars)
0385: BF 01 E7            STX     $01E7                     ; 012D: Hold for later
0388: 8E 05 FF            LDX     #$05FF                    ; 0130: End of write
038B: 9F 54               STX     <$54                      ; {ram:m54} 0133: Store end
038D: 8D 0B               BSR     $39A                      ; 0135: Do write
;
; Write game state from 3BC1 to 3FFF. Don't mess with filename.
038F: 8E 3B C1            LDX     #$3BC1                    ; 0137: Write buffer start (game state)
0392: BF 01 E7            STX     $01E7                     ; 013A: Hold for later
0395: 8E 3F FF            LDX     #$3FFF                    ; 013D: End of write
0398: 9F 54               STX     <$54                      ; {ram:m54} 0140: Store end
;
039A: 86 02               LDA     #$02                      ; 0142: File type: machine
039C: 9E 8A               LDX     <$8A                      ; {ram:zeroWord} 0144: ASCII flag and mode (00 00)
039E: BD A6 5F            JSR     $A65F                     ; 0146: Write header block to tape (BASIC)
03A1: 0F 78               CLR     <$78                      ; {ram:m67} 0149: File closed
03A3: 0C 7C               INC     <$7C                      ; {ram:m67} 014B: Bump block type (from HEADER to DATA)
03A5: BD A7 D8            JSR     $A7D8                     ; 014D: Send 55s to tape (BASIC)
03A8: 20 08               BRA     $3B2                      ; 0150: Skip over keyboard buffer

03AA: 00 00 00 00 00 00 00 00                 ; 0152: 8 bytes of keyboard buffer used by BASIC ... skip that

03B2: BE 01 E7            LDX     $01E7                     ; 015A: Remembered buffer
03B5: 9F 7E               STX     <$7E                      ; {ram:m67} 015D: Buffer pointer for IO
03B7: 86 FF               LDA     #$FF                      ; 015F: Block count ...
03B9: 97 7D               STA     <$7D                      ; {ram:m67} 0161: ... 255 (the max)
03BB: DC 54               LDD     <$54                      ; {ram:m54} 0163: End address
03BD: 93 7E               SUBD    <$7E                      ; {ram:m67} 0165: Subtract start (get length)
03BF: 24 0A               BCC     $3CB                      ; 0167: More to do ... go write another block
03C1: 00 7C               NEG     <$7C                      ; {ram:m67} 0169: Block type FF ... EOF
03C3: 0F 7D               CLR     <$7D                      ; {ram:m67} 016B: Block length 0
03C5: BD A7 F4            JSR     $A7F4                     ; 016D: BLKOUT ... write EOF (BASIC)
03C8: 7E A7 EB            JMP     $A7EB                     ; 0170: Turn off motor (leave IRQ and FIRQ alone) and out (BASIC)
;
03CB: 10 83 00 FF         CMPD    #$00FF                    ; 0173: More than 255 bytes remaining
03CF: 24 03               BCC     $3D4                      ; 0177: Yes ... use 255
03D1: 5C                  INCB                              ; 0179: Remainder ...
03D2: D7 7D               STB     <$7D                      ; {ram:m67} 017A: ... data size
03D4: BD A7 F4            JSR     $A7F4                     ; 017C: BLKOUT (BASIC)
03D7: 20 DC               BRA     $3B5                      ; 017F: Do all blocks

03D9: 00 00 00 00 00 FF 7F 3F 1F 0F 07 03 01 ; 0181: 

03E6: 7E 17 37            JMP     $1737                     ; 018E: ON ERROR GOTO COMMAND VECTOR (Normally prints two-char error code)

; Padding to get to fill up to screen memory
03E9: 00 00 00 00 00 00 00 00           
03F1: 00 00 00 00 00 00 00 00          
03F9: 00 00 00 00 00 00 00 
```

# Splash Screen

This is loaded from tape directly to the screen as the program loads.

```code
Splash:
0400: E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5
0420: E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5 E5
0440: E1 E1 E1 E1 E1 E1 E1 E1 E1 E1 E1 E1 E1 E1 E1 E1 E1 E1 E1 E1 E1 E1 E1 E1 E1 E1 E1 E1 E1 E1 E1 E1
0460: B1 B3 B1 B3 B0 B0 B3 B3 B0 B1 B3 B3 B2 B0 B3 B0 B0 B1 B1 B3 B3 B3 B0 B1 B3 B3 B2 B0 B3 B3 B3 B0
0480: BA B0 BA B0 BA B6 B0 B0 B9 B5 B0 B0 B4 B2 BA B9 B2 B5 B5 B0 B0 B0 B0 BA B0 B0 B4 B5 B0 B0 B0 B8
04A0: BA B0 B0 B0 BA BE BC BC BD B5 B0 B0 B0 BA BA B0 BA B5 B5 BC BC B0 B0 B4 BC BC B9 B0 BC BC BC B2
04C0: BA B0 B0 B0 BA BA B0 B0 B5 B5 B3 B3 B6 B0 BA B0 B4 B7 B5 B3 B3 B3 B2 B9 B3 B3 B6 B4 B3 B3 B3 B8
04E0: 90 90 90 90 90 90 91 93 90 92 90 92 93 93 90 90 F0 F1 F3 F3 F1 F0 F1 F1 F3 F2 F0 F0 F0 F0 F0 F0
0500: 90 90 90 90 90 90 9B 93 9A 9E 92 9A 9A 90 9A 90 F0 F0 F5 F0 F5 F3 F7 F5 F3 F0 F0 F0 F0 F0 F0 F0
0520: 90 90 90 90 90 90 9A 90 9A 9A 94 9A 9B 93 98 90 F0 F0 F5 F0 F5 F0 F5 F5 F3 F3 F0 F0 F0 F0 F0 F0
0540: A2 A0 A0 A2 A1 A3 A3 A0 A2 A0 A0 A2 A1 A3 A3 A0 A3 A3 A3 A2 A0 A3 A2 A0 A2 A0 A0 A2 A3 A3 A3 A0
0560: AE A2 A6 AA A0 A5 A0 A0 AE A2 A0 AA AA A0 A0 AA A0 A5 A0 A0 A6 A0 A4 A2 AA A0 A0 AA AA A0 A0 AA
0580: AA A4 A0 AA A0 A5 A0 A0 AA A4 A2 AA AA A0 A0 AA A0 A5 A0 A0 AE AC AC AA AA A0 A0 AA AE AC AE A0
05A0: AA A0 A0 AA A1 A7 A3 A0 AA A0 A4 AA A9 A3 A3 A8 A0 A5 A0 A0 AA A0 A0 AA A4 A3 A6 A0 AA A0 A4 A2
05C0: 43 4F 50 52 6E 60 71 79 78 71 60 53 50 45 43 54 52 41 4C 60 41 53 53 4F 43 49 41 54 45 53 60 60
05E0: 60 4C 49 43 45 4E 53 45 44 60 54 4F 60 54 41 4E 44 59 60 43 4F 52 50 4F 52 41 54 49 4F 4E 60 60

; The following display is a representation of the 64x32 block screen
; created by the alpha-graphics characters. The last two lines are
; normal text characters.

;  g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g
;  g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g
;  g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g
;  g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g
;                                                                 
;  g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g
;                                                                 
;  ddd ddd    dddd   dddddd   dd     d ddddddd   dddddd   dddddd  
; d   d   d  d    d  d     d  d d    d d        d      d d      d 
; d   d   d d      d d      d d  dd  d d        d        d        
; d       d dddddddd d      d d   d  d ddddd     dddddd   dddddd  
; d       d d      d d      d d   d  d d               d        d 
; d       d d      d d     d  d    d d d        d      d d      d 
; d       d d      d dddddd   d     dd dddddddd  dddddd   dddddd  
;                                                                 
;              bbb  b   b bbbb       hhhhh h   h hhhh             
;             b   b bb  b b   b        h   h   h h                
;             bbbbb b b b b   b        h   hhhhh hhh              
;             b   b b  bb b   b        h   h   h h                
;             b   b b   b bbbb         h   h   h hhhhh            
;                                                                 
; c     c  ccccc  c     c  ccccc  ccccccc   ccc   c     c cccccc  
; cc   cc    c    cc    c c     c    c     c   c  c     c c     c 
; c c c c    c    c c   c c     c    c    c     c c     c c     c 
; c  c  c    c    c  c  c c     c    c    ccccccc c     c cccccc  
; c     c    c    c   c c c     c    c    c     c c     c c   c   
; c     c    c    c    cc c     c    c    c     c  c   c  c    c  
; c     c  ccccc  c     c  ccccc     c    c     c   ccc   c     c 

; COPR. 1981 SPECTRAL ASSOCIATES    
;  LICENSED TO TANDY CORPORATION    

; TODO How about a visual of the CoCo screen
```
 
# Print with Wrapping

 Print character A to screen and handle word wrapping. This function remembers and spaces on the
 end of the line and drops them.
 
```code
PrintWrap:
0600: 34 36               PSHS    Y,X,B,A                   ; Save params
0602: 81 08               CMPA    #$08                      ; Backspace?
0604: 27 53               BEQ     $659                      ; Yes ... either forget last space or print it
0606: 81 20               CMPA    #$20                      ; Anything below 20 ...
0608: 25 4B               BCS     $655                      ; ... just print
060A: D6 89               LDB     <$89                      ; {ram:scrCursor} Cursor LSB
060C: C4 1F               ANDB    #$1F                      ; Are we at the end of a row?
060E: 26 41               BNE     $651                      ; No ... move on
0610: 81 60               CMPA    #$60                      ; Space at the end of a row?
0612: 27 04               BEQ     $618                      ; Yes ... just count it
0614: 81 20               CMPA    #$20                      ; Lower case space?
0616: 26 04               BNE     $61C                      ; No ... not a space
0618: 0C 0B               INC     <$0B                      ; {ram:spacesOnEnd} Note the space ...
061A: 20 3B               BRA     $657                      ; ... and out
;
061C: D6 0B               LDB     <$0B                      ; {ram:spacesOnEnd} Last printed was a space on the end of the row?
061E: 26 31               BNE     $651                      ; Yes ... print this character
0620: 9E 88               LDX     <$88                      ; {ram:scrCursor} Screen cursor
0622: A6 1F               LDA     -1,X                      ; Back up one space
0624: 81 60               CMPA    #$60                      ; A space last?
0626: 27 29               BEQ     $651                      ; Yes ... print this
0628: 8C 04 00            CMPX    #$0400                    ; Top of screen?
062B: 27 24               BEQ     $651                      ; Yes ... print this
;
; Move what we have of the word from the end of the line to next line
; Assumes no word is larger than 16 characters (buffer overflow)
062D: 86 60               LDA     #$60                      ; Space
062F: 10 8E 00 66         LDY     #$0066                    ; Buffer for auto-word wrap and decode
0633: E6 82               LDB     ,-X                       ; Get the last character
0635: C1 60               CMPB    #$60                      ; Is it a space?
0637: 27 06               BEQ     $63F                      ; Yes ... got all the word
0639: A7 84               STA     ,X                        ; Clear the character
063B: E7 A2               STB     ,-Y                       ; Put the character in the buffer
063D: 20 F4               BRA     $633                      ; Get the whole last word
063F: A6 A0               LDA     ,Y+                       ; Get the character fromt the buffer
0641: 81 5F               CMPA    #$5F                      ; Make ...
0643: 23 02               BLS     $647                      ; ... upper ...
0645: 80 40               SUBA    #$40                      ; ... case
0647: 10 8C 00 67         CMPY    #$0067                    ; Moved them all?
064B: 27 06               BEQ     $653                      ; Yes ... move on
064D: 9D A6               JSR     <$A6                      ; {ram:m8C} Print character to screen
064F: 20 EE               BRA     $63F                      ; Keep printing wrapping word
0651: 0F 0B               CLR     <$0B                      ; {ram:spacesOnEnd} No space on end of line
0653: A6 E4               LDA     ,S                        ; Restore A (character)
0655: 9D A6               JSR     <$A6                      ; {ram:m8C} Print it
0657: 35 B6               PULS    A,B,X,Y,PC                ; Done
;
0659: D6 0B               LDB     <$0B                      ; {ram:spacesOnEnd} Any trailing space waiting from before?
065B: 27 F6               BEQ     $653                      ; No ... print the backspace
065D: 0F 0B               CLR     <$0B                      ; {ram:spacesOnEnd} Just drop the held space ...
065F: 20 F6               BRA     $657                      ; ... and done
```

# Random Numbers
 
 Get next "random" number to B. This is a neat idea. It uses
 the BASIC ROM as a table of random bytes. Every call advances
 the ROM pointer to the next byte and rolls back around to the 
 start.

```code
Random:
0661: 34 10               PSHS    X                         ; Save parameters
0663: 9E 18               LDX     <$18                      ; {ram:randPoint} Get pointer to ROM area
0665: 30 01               LEAX    1,X                       ; Next byte in ROM
0667: 8C C0 00            CMPX    #$C000                    ; Reached the end of ROM?
066A: 25 03               BCS     $66F                      ; No ... use this
066C: 8E A0 00            LDX     #$A000                    ; Restart at the top of ROM (BASIC)
066F: 9F 18               STX     <$18                      ; {ram:randPoint} New pointer
0671: E6 84               LDB     ,X                        ; Get byte
0673: E8 04               EORB    4,X                       ; Mangle it with a later byte
0675: 35 90               PULS    X,PC                      ; Done

; Get random valid direction from room (X=pointer to dir pattern)
0677: 34 12               PSHS    X,A                       ; Save params
0679: BD 0F 95            JSR     $0F95                     ; Get doors for ...
067C: A6 84               LDA     ,X                        ; ... room B
067E: 84 3F               ANDA    #$3F                      ; Ignore upper two bits
0680: 27 0B               BEQ     $68D                      ; No passages out of room
0682: 86 1E               LDA     #$1E                      ; Try 30 times
0684: 8D 29               BSR     $6AF                      ; Get random direction
0686: E5 84               BITB    ,X                        ; Can we go in that direction?
0688: 26 04               BNE     $68E                      ; Yes ... out (Z=0)
068A: 4A                  DECA                              ; Try all ...
068B: 26 F7               BNE     $684                      ; ... 30 times
068D: 5F                  CLRB                              ; Z=1
068E: 35 92               PULS    A,X,PC                    ; Done

RandB:
; Get a random number less than B
0690: 34 12               PSHS    X,A                       ; Save params
0692: D7 3D               STB     <$3D                      ; {ram:m3D} Hold max value
0694: 8E 01 85            LDX     #$0185                    ;
0697: 43                  COMA                              ; Set the C flag
0698: 1F 98               TFR     B,A                       ;
069A: 30 01               LEAX    1,X                       ;
069C: 49                  ROLA                              ;
069D: 27 0E               BEQ     $6AD                      ; 
069F: 24 F9               BCC     $69A                      ; 
06A1: 8D BE               BSR     $661                      ; {Random} Get random number
06A3: E4 84               ANDB    ,X                        ;
06A5: D1 3D               CMPB    <$3D                      ; {ram:m3D} 
06A7: 23 04               BLS     $6AD                      ; 
06A9: D6 3D               LDB     <$3D                      ; {ram:m3D} 
06AB: 20 E7               BRA     $694                      ; 
06AD: 35 92               PULS    A,X,PC                    ; Done

; Get random direction
06AF: 34 10               PSHS    X                         ; Save params
06B1: 8D AE               BSR     $661                      ; {Random} Get random number
06B3: C4 07               ANDB    #$07                      ; Lower 3 bits
06B5: C1 06               CMPB    #$06                      ; Ignore ...
06B7: 24 F8               BCC     $6B1                      ; ... 6 or 7
06B9: 30 8D 00 04         LEAX    $0004,PC                  ; Bit table
06BD: E6 85               LDB     B,X                       ; Get bit-set value
06BF: 35 90               PULS    X,PC                      ; Done
;
06C1: 01  ; --000001  SOUTH
06C2: 02  ; --000010  WEST             
06C3: 04  ; --000100  EAST
06C4: 08  ; --001000  NORTH         
06C5: 10  ; --010000  DOWN
06C6: 20  ; --100000  UP
             
06C7: 34 36               PSHS    Y,X,B,A                   ; Save params
06C9: 10 8E 3B BD         LDY     #$3BBD                    ; Spell data
06CD: 4F                  CLRA                              ; Spell zero
06CE: 31 24               LEAY    4,Y                       ; Next spell
06D0: E6 23               LDB     3,Y                       ; Learned - flag
06D2: 27 07               BEQ     $6DB                      ; {LearnSpell} Go process if not learned
06D4: 4C                  INCA                              ; Next spell
06D5: 81 08               CMPA    #$08                      ; All 8 done?
06D7: 25 F5               BCS     $6CE                      ; No ... do next
06D9: 35 B6               PULS    A,B,X,Y,PC                ; Done
```

# Learn Spell

```code
LearnSpell:
; Learn spell if we have the right stuff
06DB: E6 A4               LDB     ,Y                        ; 1st required object
06DD: BD 18 85            JSR     $1885                     ; {InPack} Object in pack?
06E0: 24 F7               BCC     $6D9                      ; No ... out
06E2: E6 21               LDB     1,Y                       ; 2nd required object ...
06E4: BD 18 85            JSR     $1885                     ; {InPack} ... in pack?
06E7: 24 F0               BCC     $6D9                      ; No ... out
06E9: E6 22               LDB     2,Y                       ; Is the spell even ...
06EB: D1 00               CMPB    <$00                      ; {ram:curRoom} ... in this room?
06ED: 26 EA               BNE     $6D9                      ; No ... out
06EF: 8B 37               ADDA    #$37                      ; Spell number to object number
06F1: 1F 89               TFR     A,B                       ; To B for call
06F3: BD 1A 5A            JSR     $1A5A                     ; {GetObject} Get object
06F6: 8D 23               BSR     $71B                      ; {PickUpObject} Move object to pack
06F8: 8E 2E 1D            LDX     #$2E1D                    ; "YOU NOW KNOW THE SECRET OF THE MAGIC SPELL"
06FB: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
06FE: 1F 89               TFR     A,B                       ; Name of spell
0700: BD 18 6D            JSR     $186D                     ; Print spell name
0703: C1 3E               CMPB    #$3E                      ; Last spell?
0705: 27 0B               BEQ     $712                      ; No more to learn ... skip the hint
0707: 8E 2E 47            LDX     #$2E47                    ; "- YOU WILL DISCOVER THE SECRET OF THE NEXT SPELL IF YOU POSSESS THE"
070A: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
070D: E6 24               LDB     4,Y                       ; 1st object from next spell slot
070F: BD 18 6D            JSR     $186D                     ; Print it
0712: BD 10 3F            JSR     $103F                     ; Remove the period and space
0715: 86 80               LDA     #$80                      ; Mark ...
0717: A7 23               STA     3,Y                       ; ... spell learned
0719: 20 BE               BRA     $6D9                      ; Done
```

# Pick up an Object

```code  
PickUpObject:
; Move object at X to pack.
071B: 34 02               PSHS    A                         ; Save A
071D: A6 02               LDA     2,X                       ; Get flags
071F: 8A 80               ORA     #$80                      ; Put in ...
0721: A7 02               STA     2,X                       ; ... pack
0723: 35 82               PULS    A,PC                      ; Out
      
; Clear counters associated with being in MYSTERIOUS FOG room.
0725: 0F 32               CLR     <$32                      ; {ram:enteredFog} Not in MYSTERIOUS FOG room.
0727: 0F 45               CLR     <$45                      ; {ram:fogClock} Fog time to 0
0729: 39                  RTS                               ; Out

; Init the interrupt service routine
072A: 86 7E               LDA     #$7E                      ; JMP ...
072C: B7 01 0C            STA     $010C                     ; ... to ...
072F: CC 07 45            LDD     #$0745                    ; ... IRQ service ...
0732: FD 01 0D            STD     $010D                     ; ... routine
0735: 8E FF 01            LDX     #$FF01                    ;  HSYNC interrupt control
0738: A6 84               LDA     ,X                        ; Disable ...
073A: 84 FC               ANDA    #$FC                      ; ... HSYNC (fast) ...
073C: A7 81               STA     ,X++                      ; ... interrupt
073E: A6 84               LDA     ,X                        ; Enable ...
0740: 8A 01               ORA     #$01                      ; ... VSYNC (60Hz) ...
0742: A7 84               STA     ,X                        ; ... interrupt
0744: 39                  RTS                               ; Done
```

# Interrupt Service

The HSYNC (fast) interrupt is turned off. This routine is called 60 times a second, but it only
performs work once a second.

Emulators can call 0751 once a second instead of 0745 60-times-a-second.

```code
InterruptService:
0745: B6 FF 02            LDA     $FF02                     ; {hard:PIA0_DB} Strobe hardware to re-enable interrupt
0748: 0C 3F               INC     <$3F                      ; {ram:ticksTillSec} Interrupt ...
074A: 96 3F               LDA     <$3F                      ; {ram:ticksTillSec} ... divisor
074C: 81 3C               CMPA    #$3C                      ; Once ...
074E: 24 01               BCC     $751                      ; ... a second
0750: 3B                  RTI                               ; Return from interrupt
;
0751: BD 0A 1F            JSR     $0A1F                     ; {MINOTAURAttack} Handle creatures that attack
0754: 96 45               LDA     <$45                      ; {ram:fogClock} Time spent with MYSTERIOUS FOG
0756: 81 06               CMPA    #$06                      ; Fog counter reached 6 seconds?
0758: 27 19               BEQ     $773                      ; Yes ... warn the player
075A: 25 21               BCS     $77D                      ; Less than 6 ... just move on
075C: 81 0A               CMPA    #$0A                      ; Counter reached 10 seconds?
075E: 25 1D               BCS     $77D                      ; No ... keep waiting
0760: 96 32               LDA     <$32                      ; {ram:enteredFog} In MYSTERIOUS FOG room?
0762: 27 19               BEQ     $77D                      ; No skip processing
;
0764: 8D BF               BSR     $725                      ; Clear MYSTERIOUS FOG flag and fog time
0766: 96 09               LDA     <$09                      ; {ram:stingCount} Scorpion sting count
0768: 26 13               BNE     $77D                      ; Scorpion poison trumps ... handle later
076A: 8E 31 53            LDX     #$3153                    ; "THE POISON FOG HAS KILLED YOU!"
076D: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
0770: 7E 0D 5C            JMP     $0D5C                     ; {CommandUNCLE} Command "UNCLE" ... end game
;
0773: 96 32               LDA     <$32                      ; {ram:enteredFog} Have we passed through MYSTERIOUS FOG?
0775: 27 06               BEQ     $77D                      ; No ... skip
0777: 8E 31 72            LDX     #$3172                    ; "IT'S POISONOUS!!"
077A: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
;
077D: 96 45               LDA     <$45                      ; {ram:fogClock} Fog clock running?
077F: 27 02               BEQ     $783                      ; No ... skip it
0781: 0C 45               INC     <$45                      ; {ram:fogClock} Increment the fog clock
;
0783: 96 0A               LDA     <$0A                      ; {ram:lampOn} Lamp status
0785: 27 12               BEQ     $799                      ; Lap is off ... skip timing it
0787: 9E 38               LDX     <$38                      ; {ram:lampOil} Oil remaining
0789: 27 06               BEQ     $791                      ; No oil ... lamp now goes out
078B: 30 1F               LEAX    -1,X                      ; Decrement the oil level
078D: 9F 38               STX     <$38                      ; {ram:lampOil} New oil level
078F: 20 08               BRA     $799                      ; Move on
0791: 0F 0A               CLR     <$0A                      ; {ram:lampOn} Lamp off
0793: 8E 2B 97            LDX     #$2B97                    ; "YOUR LAMP HAS JUST GONE OFF."
0796: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
0799: 9E 4C               LDX     <$4C                      ; {ram:secsInRoom} Count time in room
079B: 8C 00 0F            CMPX    #$000F                    ; 15?
079E: 24 04               BCC     $7A4                      ; Leave counter at 15
07A0: 30 01               LEAX    1,X                       ; Bump ...
07A2: 9F 4C               STX     <$4C                      ; {ram:secsInRoom} ... counter
07A4: 9E 4A               LDX     <$4A                      ; {ram:seconds} Bump ...
07A6: 30 01               LEAX    1,X                       ; ... continual ...
07A8: 9F 4A               STX     <$4A                      ; {ram:seconds} ... counter (nobody uses it)
07AA: 0F 3F               CLR     <$3F                      ; {ram:ticksTillSec} Clear interrupt divisor
07AC: 0C 40               INC     <$40                      ; {ram:secsTillMin} Sub divisor for 1 minute ticks
07AE: 96 40               LDA     <$40                      ; {ram:secsTillMin} Get minute count
07B0: 81 3C               CMPA    #$3C                      ; Reached a minute?
07B2: 25 5A               BCS     $80E                      ; No ... out
07B4: 0F 40               CLR     <$40                      ; {ram:secsTillMin} Reset minute count
```

# One Minute Tick

 Things that happen on minute ticks.

```code
OneMinTick:
; If we are invulnerable, count down the time. When it expires move the
; SCARAB to a random room.
07B6: 96 46               LDA     <$46                      ; {ram:akhiromMins} AKHIROM made us invulnerable?
07B8: 27 12               BEQ     $7CC                      ; No ... skip
07BA: 0A 46               DEC     <$46                      ; {ram:akhiromMins} Count down invulnerability time
07BC: 26 0E               BNE     $7CC                      ; Not time to move SCARAB
07BE: BD 0B 3E            JSR     $0B3E                     ; Sound effect
07C1: C6 15               LDB     #$15                      ; Move SCARAB from pack ...
07C3: BD 12 B8            JSR     $12B8                     ; ... to random room
07C6: BD 06 61            JSR     $0661                     ; {Random} Random number
07C9: F7 3D 38            STB     $3D38                     ; SCARABs to random room ... again

07CC: 96 3E               LDA     <$3E                      ; {ram:drinkTimer} Count down since drinking water
07CE: 27 02               BEQ     $7D2                      ; No count ... skip
07D0: 0A 3E               DEC     <$3E                      ; {ram:drinkTimer} Time down till we can drink again
07D2: 96 09               LDA     <$09                      ; {ram:stingCount} Scorpion stings
07D4: 27 15               BEQ     $7EB                      ; Not stung ... continue
07D6: C6 05               LDB     #$05                      ;
07D8: 3D                  MUL                               ; B = numStings * 5
07D9: 1F 98               TFR     B,A                       ;
07DB: D0 05               SUBB    <$05                      ; {ram:condition} Enough to kill us?
07DD: 25 09               BCS     $7E8                      ; No ... move on
07DF: 8E 34 B4            LDX     #$34B4                    ; "YOU HAVE DIED FROM A SCORPION BITE."
07E2: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
07E5: 7E 0D 5C            JMP     $0D5C                     ; {CommandUNCLE} Command "UNCLE" ... end of game
;
07E8: BD 1A 2F            JSR     $1A2F                     ; Drop physical condition and out
;
07EB: 9E 38               LDX     <$38                      ; {ram:lampOil} Oil in lamp
07ED: 8C 01 2C            CMPX    #$012C                    ; Begins to flicker at 300
07F0: 22 11               BHI     $803                      ; Not time to flicker
07F2: 96 0A               LDA     <$0A                      ; {ram:lampOn} Lamp status
07F4: 27 0D               BEQ     $803                      ; Lamp not on ... can't flicker
07F6: C6 0C               LDB     #$0C                      ; "LAMP"
07F8: BD 18 85            JSR     $1885                     ; {InPack} Check pack
07FB: 24 06               BCC     $803                      ; Skip if not in pack
07FD: 8E 32 EF            LDX     #$32EF                    ; "THE LAMP IS FLICKERING."
0800: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
;
0803: 96 13               LDA     <$13                      ; {ram:auraTimer} Enchanted aura counter
0805: 27 02               BEQ     $809                      ; Timed out? Skip
0807: 0A 13               DEC     <$13                      ; {ram:auraTimer} Count down until we can heal again
;
0809: 8D 04               BSR     $80F                      ; Ground might shake
080B: BD 09 6E            JSR     $096E                     ; {MoveMinotaur} Move creatures once every minute
080E: 3B                  RTI                               ; Out
 
; Shaking ground ... here once a minute
080F: 34 76               PSHS    U,Y,X,B,A                 ; Save params
0811: BD 06 61            JSR     $0661                     ; {Random} Get random number
0814: C1 40               CMPB    #$40                      ; Skip the quake ...
0816: 24 2E               BCC     $846                      ; ... 3/4ths of the time
0818: 8E 2E 8A            LDX     #$2E8A                    ; "THE GROUND IS SHAKING!"
081B: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message

081E: 10 8E 3E 38         LDY     #$3E38                    ; Start of floor 3
0822: 8E 00 F3            LDX     #$00F3                    ; Shanking-ground blocked passage queue
```

 Maintains a list of the last 12 rooms that were blocked. As new rooms are blocked
 they go on the end of the list and the rooms at the beginning of the list are 
 pulled off the list and opened. Thus "shaking ground" only affects 12 rooms at a time.

```code 
0825: 86 03               LDA     #$03                      ; 3 times
;
0827: BD 06 61            JSR     $0661                     ; {Random} Get random number (0-255)
082A: 33 A5               LEAU    B,Y                       ; Offset from floor 3 (this is signed ... no overflow)
082C: E7 E2               STB     ,-S                       ; Hold this room .... going on end of list
082E: BD 06 61            JSR     $0661                     ; {Random} Get random ...
0831: C4 3F               ANDB    #$3F                      ; ... direction bits
0833: E7 C9 01 00         STB     $0100,U                   ; Block passages
0837: E6 84               LDB     ,X                        ; From shift table
0839: 33 A5               LEAU    B,Y                       ; Offset from floor 3 (this is signed ... no overflow)
083B: 6F C9 01 00         CLR     $0100,U                   ; Remove blocked passages
083F: E6 E0               LDB     ,S+                       ; 12 byte shift left ...
0841: 8D 05               BSR     $848                      ; ... with B put on end (13th place)
0843: 4A                  DECA                              ; All done?
0844: 26 E1               BNE     $827                      ; No ... back for more
0846: 35 F6               PULS    A,B,X,Y,U,PC              ; Done

; Shift the 12 bytes at X left one byte. The byte at X gets lost. The value of
; B goes on the end 13th entry.
0848: 34 16               PSHS    X,B,A                     ; Save params
084A: C6 0C               LDB     #$0C                      ; 12 times
084C: A6 01               LDA     1,X                       ; Shift bytes ...
084E: A7 80               STA     ,X+                       ; ... left at X
0850: 5A                  DECB                              ; 12 bytes ...
0851: 26 F9               BNE     $84C                      ; ... shifted
0853: E6 61               LDB     1,S                       ; B from stack
0855: E7 84               STB     ,X                        ; Store it at the end
0857: 35 96               PULS    A,B,X,PC                  ; Done
```
 
# Handle User Input

 Arrows flip the screens. $3B holds the screen pointer to the input. 
 $03 is the length of input. After 32 characters the routine automatically
 takes the input as complete.

```code
UserInput:
0859: BD 10 90            JSR     $1090                     ; {PrintCR} Print CR
085C: 0F 03               CLR     <$03                      ; {ram:inpLen} Clear character count
085E: DC 88               LDD     <$88                      ; {ram:scrCursor} Current cursor
0860: DD 3B               STD     <$3B                      ; {ram:m3B} Hold it for now
0862: 1C EF               ANDCC   #$EF                      ; Interrupts on while waiting
0864: BD A1 B1            JSR     $A1B1                     ; Blink cursor and wait for key (BASIC)
0867: 1A 50               ORCC    #$50                      ; Interrupts off while processing
0869: 8E FF C6            LDX     #$FFC6                    ;  Graphics offset register
086C: 81 5E               CMPA    #$5E                      ; UP ARROW
086E: 27 09               BEQ     $879                      ; Yes ... switch to upper page
0870: 81 0A               CMPA    #$0A                      ; DOWN ARROW
0872: 26 09               BNE     $87D                      ; No ... on.
0874: A7 84               STA     ,X                        ; F0 = 0
0876: A7 03               STA     3,X                       ; F1 = 1 (Address $0400)
0878: 8C ED 01            CMPX    #$ED01                    ; (STD +$01,X) at 0879 (Address $0200)
087B: 20 E5               BRA     $862                      ; Back for another key
;
087D: 81 0D               CMPA    #$0D                      ; CR?
087F: 27 36               BEQ     $8B7                      ; Done
0881: 81 08               CMPA    #$08                      ; Backspace?
0883: 27 14               BEQ     $899                      ; Go handle
0885: 81 20               CMPA    #$20                      ; Lower bounds
0887: 25 D9               BCS     $862                      ; Ignore invalid character
0889: 81 5A               CMPA    #$5A                      ; Upper bounds
088B: 22 D5               BHI     $862                      ; Ignore invalid character
088D: 0C 03               INC     <$03                      ; {ram:inpLen} Increment the character count
088F: C6 1E               LDB     #$1E                      ; Reached the ...
0891: D1 03               CMPB    <$03                      ; {ram:inpLen} ... Max?
0893: 23 22               BLS     $8B7                      ; Yes ... out
0895: 9D A6               JSR     <$A6                      ; {ram:m8C} Print character
0897: 20 C9               BRA     $862                      ; Back for more
;        
0899: 0A 03               DEC     <$03                      ; {ram:inpLen} Take a character away
089B: 2A F8               BPL     $895                      ; Yes ... it was there ... take it off the screen
089D: 0F 03               CLR     <$03                      ; {ram:inpLen} Otherwise ignore ...
089F: 20 C1               BRA     $862                      ; ... the backspace

; Parse two words from input (off of screen) and fill 2A and 2B. Error and back to
; top of game loop if unknown verb.
08A1: 9E 3B               LDX     <$3B                      ; {ram:m3B} Start of input buffer
08A3: 86 FF               LDA     #$FF                      ; Clear ...
08A5: 97 2B               STA     <$2B                      ; {ram:nounNum} ... NOUN
08A7: 8D 1B               BSR     $8C4                      ; Parse the first word
08A9: 8D 60               BSR     $90B                      ; Match the VERB
08AB: 24 0B               BCC     $8B8                      ; Didn't know the verb ... error
08AD: A6 84               LDA     ,X                        ; Next in input
08AF: 81 0D               CMPA    #$0D                      ; CR?
08B1: 27 04               BEQ     $8B7                      ; Yes ... no NOUN
08B3: 8D 0F               BSR     $8C4                      ; Parse the second word
08B5: 8D 70               BSR     $927                      ; Match the NOUN
08B7: 39                  RTS                               ; Done
; Unknown VERB
08B8: 8E 2A 81            LDX     #$2A81                    ; "I DON'T UNDERSTAND THAT."
08BB: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
08BE: BD 10 90            JSR     $1090                     ; {PrintCR} Print CR
08C1: 7E 0D 36            JMP     $0D36                     ; {MainGameLoop} Next command cycle
  
; Copy word from X into parse buffer at 0056. Up to 16 characters are copied, and
; the buffer is blanked with 16 spaces first.
08C4: 10 8E 00 56         LDY     #$0056                    ; Input buffer
08C8: C6 0F               LDB     #$0F                      ; Clear out 16 spaces ...
08CA: 8D 34               BSR     $900                      ; ... for verb
08CC: A6 80               LDA     ,X+                       ; Next from screen
08CE: 81 60               CMPA    #$60                      ; Space?
08D0: 27 FA               BEQ     $8CC                      ; Yes ... ignore leading spaces
08D2: A7 A0               STA     ,Y+                       ; Store char
08D4: 5A                  DECB                              ; 16 stored?
08D5: 27 06               BEQ     $8DD                      ; Yes ... out
08D7: A6 80               LDA     ,X+                       ; Get next
08D9: 81 60               CMPA    #$60                      ; Is it a space?
08DB: 26 F5               BNE     $8D2                      ; No ... keep storing up to 16
08DD: 39                  RTS                               ; Done

; Check input buffer (at 0056) against word at X. Return
; C=0 if no match or C=1 if match. X is guaranteed to
; be before end marker if not matching.
08DE: 34 06               PSHS    B,A                       ; Hold params
08E0: 10 8E 00 56         LDY     #$0056                    ; Buffer to match
08E4: A6 80               LDA     ,X+                       ; Byte from potential
08E6: 2B 07               BMI     $8EF                      ; End of potential
08E8: A1 A0               CMPA    ,Y+                       ; Matches the input buffer?
08EA: 27 F8               BEQ     $8E4                      ; Yes ... keep looking
08EC: 4F                  CLRA                              ; No ...
08ED: 20 0F               BRA     $8FE                      ; ... return C=0
08EF: 84 7F               ANDA    #$7F                      ; Drop upper bit (end marker)
08F1: 30 1F               LEAX    -1,X                      ; Back up to end marker
08F3: A1 A0               CMPA    ,Y+                       ; Last character matches?
08F5: 26 F5               BNE     $8EC                      ; No ... return not-matched
08F7: E6 A4               LDB     ,Y                        ; Next in input buffer
08F9: C1 60               CMPB    #$60                      ; A Space?
08FB: 26 EF               BNE     $8EC                      ; No ... return not-matched
08FD: 43                  COMA                              ; A is NOT 00 ... C=1 here
08FE: 35 86               PULS    A,B,PC                    ; Done

; Fill buffer Y with B spaces.
0900: 34 26               PSHS    Y,B,A                     ; Save params
0902: 86 60               LDA     #$60                      ; Space character
0904: A7 A0               STA     ,Y+                       ; Store space
0906: 5A                  DECB                              ; All done?
0907: 26 FB               BNE     $904                      ; No ... do all
0909: 35 A6               PULS    A,B,Y,PC                  ; Done

; Match input buffer with VERB word. 
; Interesting: this looks for 65 matches but there are only 45 actual commands.
; C=0 if not found
; C=1 and B=string number if found (also to $2A).
090B: 34 30               PSHS    Y,X                       ; Save params
090D: C6 FF               LDB     #$FF                      ; Will be 0 ... first string
090F: 8E 27 26            LDX     #$2726                    ; Command word table
0912: 5C                  INCB                              ; String number points to
0913: C1 40               CMPB    #$40                      ; All tested?
0915: 22 0D               BHI     $924                      ; No matching word ... CLRA and return
0917: 8D C5               BSR     $8DE                      ; Check match
0919: 25 05               BCS     $920                      ; Got a match
091B: BD 10 7D            JSR     $107D                     ; Skip to the end of the string
091E: 20 F2               BRA     $912                      ; Keep going
0920: D7 2A               STB     <$2A                      ; {ram:verbNum} Command number
0922: 43                  COMA                              ; Set C=1
0923: 21 4F               BRN     $974                      ; (CLRA at 924 ... C=0)
0925: 35 B0               PULS    X,Y,PC                    ; Done

; Match input buffer with NOUN word. 
; C=0 if not found
; C=1 and B=string number if found (also to $2B).
0927: 34 30               PSHS    Y,X                       ; Save params
0929: C6 FF               LDB     #$FF                      ; Will be 0 ... first string
092B: 8E 35 C6            LDX     #$35C6                    ; Noun strings
092E: 5C                  INCB                              ; String number X points to
092F: C1 FE               CMPB    #$FE                      ; FF ... we didn't find a match
0931: 22 0D               BHI     $940                      ; No matching word ... CLRA and return
0933: 8D A9               BSR     $8DE                      ; Check match
0935: 25 05               BCS     $93C                      ; C=1 ... we found a match
0937: BD 10 7D            JSR     $107D                     ; Skip to end of string
093A: 20 F2               BRA     $92E                      ; Keep looking
093C: D7 2B               STB     <$2B                      ; {ram:nounNum} Store string number
093E: 43                  COMA                              ; C=1
093F: 21 4F               BRN     $990                      ; (CLRA at 940 ... C=0)
0941: 35 B0               PULS    X,Y,PC                    ; Done

IsObjInRoom:
; See if object A is in room.
; C=0 not in room
; C=1 in room
0943: 34 16               PSHS    X,B,A                     ; Save params
0945: 1F 89               TFR     A,B                       ; To B for the check
0947: BD 1A 5A            JSR     $1A5A                     ; {GetObject} Get the object's descriptor
094A: A6 84               LDA     ,X                        ; Get the object's room
094C: 91 00               CMPA    <$00                      ; {ram:curRoom} Is object in room?
094E: 27 05               BEQ     $955                      ; Yes ... check it furter
0950: 4F                  CLRA                              ; C=0 ... not in room
0951: 21 43               BRN     $996                      ; COMA from 952 ... C=1
0953: 35 96               PULS    A,B,X,PC                  ; Out
0955: A6 02               LDA     2,X                       ; Flags
0957: 84 03               ANDA    #$03                      ; Is this a visible object?
0959: 26 F5               BNE     $950                      ; No .... not in room
095B: 20 F5               BRA     $952                      ; Yes ... set C=1 found in room
      
; If object is in room print description and set C=1.
095D: 34 16               PSHS    X,B,A                     ; Save params
095F: 1F 89               TFR     A,B                       ; To B
0961: 8D E0               BSR     $943                      ; {IsObjInRoom} Is object in room?
0963: 24 07               BCC     $96C                      ; No ... out
0965: BD 0E 46            JSR     $0E46                     ; Print description for object.
0968: BD 10 90            JSR     $1090                     ; {PrintCR} Print CR
096B: 43                  COMA                              ; C=1
096C: 35 96               PULS    A,B,X,PC                  ; Done
```

# Move Creatures

 All the creatures move once every minute.

## Minotaur

 Moves to a random room from current position ignoring passages. <br>
 May not move to 1st floor.

```code
MoveCreatures:
MoveMinotaur: 
096E: BD 06 AF            JSR     $06AF                     ; Get random direction
0971: B6 3D 53            LDA     $3D53                     ; Minotaur room
0974: BD 0F 71            JSR     $0F71                     ; Calculate target room
0977: 81 40               CMPA    #$40                      ; Minotaur moving to 1st floor?
0979: 25 03               BCS     $97E                      ; {MoveOracle} Yes ... don't let it
097B: B7 3D 53            STA     $3D53                     ; New room
```

## Oracle 

 Moves to a random room from current position ignoring passages.

```code
MoveOracle:
097E: BD 06 AF            JSR     $06AF                     ; Get random direction
0981: B6 3D 56            LDA     $3D56                     ; Oracle room
0984: BD 0F 71            JSR     $0F71                     ; Calculate target room
0987: B7 3D 56            STA     $3D56                     ; New room
```

## Troglodyte

 Moves to a random room from current position but must follow unblocked passages.<br>
 May not move to 4th floor.

```code
MoveTroglodyte:
098A: F6 3D 47            LDB     $3D47                     ; Troglodyte room
098D: BD 06 77            JSR     $0677                     ; Get random direction (following passages)
0990: B6 3D 47            LDA     $3D47                     ; Troglodyte room
0993: BD 0F 71            JSR     $0F71                     ; Calculate target room
0996: 81 C0               CMPA    #$C0                      ; Troglodyte moving to 4th floor?
0998: 24 03               BCC     $99D                      ; {MoveSatyr} Yes ... don't let it
099A: B7 3D 47            STA     $3D47                     ; New room
```

## Satyr 

 Moves to a random room from current position but must follow unblocked passages.<br>
 May not move to 1st floor.

```code
MoveSatyr:
099D: F6 3D 50            LDB     $3D50                     ; Satyr room
09A0: BD 06 77            JSR     $0677                     ; Get random direction (following passages)
09A3: B6 3D 50            LDA     $3D50                     ; Satyr room
09A6: BD 0F 71            JSR     $0F71                     ; Calculate target room
09A9: 81 40               CMPA    #$40                      ; Satyr moving to 1st floor?
09AB: 25 03               BCS     $9B0                      ; {MoveSprite} Yes ... don't let it
09AD: B7 3D 50            STA     $3D50                     ; New room
```

## Sprite

 Does not move if dead (since it slings objects). Moves to random room from current position
 but must follow unblocked passages. It moves all movable objects in the new room to random
 rooms. It may NOT move to the 4th floor except for the treasure room (where it will redistribute 
 the hard earned treasure objects).

```code
MoveSprite:
09B0: F6 3D 46            LDB     $3D46                     ; Sprite flags
09B3: C5 02               BITB    #$02                      ; Dead?
09B5: 26 3A               BNE     $9F1                      ; {MoveScorpion} Yes ... move on
09B7: F6 3D 44            LDB     $3D44                     ; Sprite room
09BA: BD 06 77            JSR     $0677                     ; Get random direction (following passages)
09BD: B6 3D 44            LDA     $3D44                     ; Sprite room
09C0: BD 0F 71            JSR     $0F71                     ; Calculate target room
09C3: 81 CA               CMPA    #$CA                      ; Moving to treasure room?
09C5: 27 04               BEQ     $9CB                      ; Yes ... allow it
09C7: 81 C0               CMPA    #$C0                      ; Moving to 4th floor?
09C9: 24 26               BCC     $9F1                      ; {MoveScorpion} Don't let it
09CB: B7 3D 44            STA     $3D44                     ; New room
09CE: B1 3D 26            CMPA    $3D26                     ; Same room as the vial?
09D1: 27 1E               BEQ     $9F1                      ; {MoveScorpion} Yes ... move on
09D3: B1 3C F5            CMPA    $3CF5                     ; Same room as music?
09D6: 27 19               BEQ     $9F1                      ; {MoveScorpion} Yes ... move on
09D8: 8E 3C FC            LDX     #$3CFC                    ; Object table
09DB: A1 84               CMPA    ,X                        ; Object in this room?
09DD: 26 0B               BNE     $9EA                      ; No ... next object
09DF: C6 D3               LDB     #$D3                      ; Object ...
09E1: E5 02               BITB    2,X                       ; ... relocatable
09E3: 26 05               BNE     $9EA                      ; No ... next object
09E5: BD 06 61            JSR     $0661                     ; {Random} Random room
09E8: E7 84               STB     ,X                        ; Move object to random room
09EA: 30 03               LEAX    3,X                       ; Next object
09EC: 8C 3D 8C            CMPX    #$3D8C                    ; All done (not spells)?
09EF: 25 EA               BCS     $9DB                      ; No ... keep going
```

## Scorpion
 
 Moves to random room from current position ignoring passages.

```code
MoveScorpion:
09F1: BD 06 AF            JSR     $06AF                     ; Random direction
09F4: B6 3D 4A            LDA     $3D4A                     ; Scorpion room
09F7: BD 0F 71            JSR     $0F71                     ; Calculate target room
09FA: B7 3D 4A            STA     $3D4A                     ; New room
```

## Nymph

 Moves to random room from current position but must follow unblocked passages.

```code
MoveNymph:
09FD: F6 3D 4D            LDB     $3D4D                     ; Nymph room
0A00: BD 06 77            JSR     $0677                     ; Random direction (following passages)
0A03: B6 3D 4D            LDA     $3D4D                     ; Nymph room
0A06: BD 0F 71            JSR     $0F71                     ; Move nymph
0A09: B7 3D 4D            STA     $3D4D                     ; New room
0A0C: 39                  RTS                               ; Out

; Return C=1 if object is active. C=0 if object is out of game.
0A0D: 34 16               PSHS    X,B,A                     ; Save params
0A0F: 1F 89               TFR     A,B                       ; Get ...
0A11: BD 1A 5A            JSR     $1A5A                     ; {GetObject} ... object B
0A14: A6 02               LDA     2,X                       ; Get the flagslook
0A16: 84 03               ANDA    #$03                      ; Is this object active?
0A18: 26 02               BNE     $A1C                      ; No ... C=0
0A1A: 43                  COMA                              ; C=1
0A1B: 21 4F               BRN     $A6C                      ; CLRA
0A1D: 35 96               PULS    A,B,X,PC                  ; Out
```
   
# Creatures Attack

 Only the Minotaur, Troglodyte, Satyr, and Scorpion.<br>
 The Nymph and Sprite do not attack.

## Minotaur 
 Minotaur attack is on a 10 second count.<br> 
 1st second ... print "MINOTAUR IS HERE".<br> 
 10th second ... Minotaur attacks. Minotaur hits with 0-70 damage.

```code
CreaturesAttack:
MINOTAURAttack:
0A1F: 86 1E               LDA     #$1E                      ; MINOTAUR
0A21: 8D EA               BSR     $A0D                      ; Is the MINOTAUR alive?
0A23: 24 38               BCC     $A5D                      ; {TROGLODYTEAttack} No Minotaur ... move on
0A25: D6 41               LDB     <$41                      ; {ram:minotaurTimer} Minotaur timer
0A27: 27 08               BEQ     $A31                      ; Count ==0 ... print description if in room and continue
0A29: C1 0A               CMPB    #$0A                      ; Count == 10
0A2B: 27 10               BEQ     $A3D                      ; Yes ... minotaur attacks!
0A2D: 0C 41               INC     <$41                      ; {ram:minotaurTimer} Next in count
0A2F: 20 2C               BRA     $A5D                      ; {TROGLODYTEAttack} Continue
;
0A31: BD 09 5D            JSR     $095D                     ; Print description if minotaur is in room
0A34: 24 27               BCC     $A5D                      ; {TROGLODYTEAttack} Not in room
0A36: BD 0B 03            JSR     $0B03                     ; {SweepSounds} Sound effect
0A39: 0C 41               INC     <$41                      ; {ram:minotaurTimer} Increment count
0A3B: 20 20               BRA     $A5D                      ; {TROGLODYTEAttack} Move on
;
0A3D: BD 09 43            JSR     $0943                     ; {IsObjInRoom} Is Minotaur in room with us?
0A40: 24 19               BCC     $A5B                      ; No ... clear count and move on
0A42: C6 03               LDB     #$03                      ; "THE MINOTAUR IS ATTACKING."
0A44: BD 10 48            JSR     $1048                     ; Print message
0A47: BD 10 90            JSR     $1090                     ; {PrintCR} Print CR
0A4A: C6 46               LDB     #$46                      ; Random number from 0 ...
0A4C: BD 06 90            JSR     $0690                     ; {RandB} ... to 70
0A4F: 1F 98               TFR     B,A                       ; Damage to A
0A51: BD 1A 2F            JSR     $1A2F                     ; Hit!
0A54: C1 20               CMPB    #$20                      ; Only a little damage?
0A56: 25 03               BCS     $A5B                      ; Just a little ... move on
0A58: BD 0B 70            JSR     $0B70                     ; Lot of damage ... "OUCH THAT HURT"
0A5B: 0F 41               CLR     <$41                      ; {ram:minotaurTimer} Restart 10 second count
```

## Troglodyte 
 TROGLODYTE is on an 12 second counter. 
 On first second it attacks and hits with 60 damage ... when it hits. 

 Whether it hits or not depends on a random number compared to the current
 room. The "earlier" the room the less chance of hitting.

```code
TROGLODYTEAttack:
0A5D: 86 1A               LDA     #$1A                      ; TROGLODYTE
0A5F: 8D AC               BSR     $A0D                      ; Is Troglodyte alive?
0A61: 24 33               BCC     $A96                      ; No ... reset counter and move on
0A63: D6 42               LDB     <$42                      ; {ram:trogTimer} Timer
0A65: 27 06               BEQ     $A6D                      ; Count 0 ... attack
0A67: C1 0C               CMPB    #$0C                      ; Count 12 ?
0A69: 26 28               BNE     $A93                      ; No ... just move on
0A6B: 0F 42               CLR     <$42                      ; {ram:trogTimer} Reset to 0 and attack
;
0A6D: BD 09 43            JSR     $0943                     ; {IsObjInRoom} Is Troglodyte in room with us?
0A70: 24 24               BCC     $A96                      ; No ... clear count and move on
0A72: BD 0B 03            JSR     $0B03                     ; {SweepSounds} Sound effect
0A75: BD 06 61            JSR     $0661                     ; {Random} Random number
0A78: C4 7F               ANDB    #$7F                      ; Random number not on 4th floor
0A7A: F1 3D 47            CMPB    $3D47                     ; Compare to current room
0A7D: 24 14               BCC     $A93                      ; New room is later than current ... move on
0A7F: C6 04               LDB     #$04                      ; "THE TROGLODYTE IS ATTACKING"
0A81: BD 10 48            JSR     $1048                     ; Print message
0A84: BD 10 90            JSR     $1090                     ; {PrintCR} Print CR
0A87: C6 3C               LDB     #$3C                      ; TROGLODYTE does ...
0A89: BD 1A 2A            JSR     $1A2A                     ; ... 60 damage
0A8C: C1 20               CMPB    #$20                      ; Only a little damage?
0A8E: 24 03               BCC     $A93                      ; Just a little ... move on
0A90: BD 0B 70            JSR     $0B70                     ; Lot of damage ... "OUCH THAT HURT"
;
0A93: 0C 42               INC     <$42                      ; {ram:trogTimer} Next in cycle
0A95: 8C 0F 42            CMPX    #$0F42                    ; Reset Troglodyte counter
```

## Satyr 
 SATYRA is on an 15 second counter.
 On first second it always hits with 30 damage.

```code
SATYRAttack:
0A98: 86 1D               LDA     #$1D                      ; Is SATYR ...
0A9A: BD 0A 0D            JSR     $0A0D                     ; ... alive?
0A9D: 24 21               BCC     $AC0                      ; No ... reset counter and move on
0A9F: D6 43               LDB     <$43                      ; {ram:satyrTimer} Satyr counter
0AA1: 27 06               BEQ     $AA9                      ; Attack on 0
0AA3: C1 0F               CMPB    #$0F                      ; Count 15?
0AA5: 26 16               BNE     $ABD                      ; No ... bump and move on
0AA7: 0F 43               CLR     <$43                      ; {ram:satyrTimer} Reset to 0
;
0AA9: BD 09 43            JSR     $0943                     ; {IsObjInRoom} Is Satyr in room with us?
0AAC: 24 12               BCC     $AC0                      ; No ... reset counter and move on
0AAE: 8D 53               BSR     $B03                      ; {SweepSounds} Sound effect
0AB0: C6 05               LDB     #$05                      ; THE SATYR IS ATTACKING
0AB2: BD 10 48            JSR     $1048                     ; Print message
0AB5: BD 10 90            JSR     $1090                     ; {PrintCR} Print CR
0AB8: C6 1E               LDB     #$1E                      ; Always hit with ...
0ABA: BD 1A 2A            JSR     $1A2A                     ; ... 30 damage
0ABD: 0C 43               INC     <$43                      ; {ram:satyrTimer} Next in cycle
0ABF: 8C 0F 43            CMPX    #$0F43                    ; Reset cycle
```
     
## Scorpion 
 SCORPION is on an 15 second counter. <br> 
 On second 0 it jumps the count to a random value 1-14.<br> 
 On second 15 it takes action. Half the time it vanishes for 16 seconds. The other
 half of the the time it adds one poision sting count. Scorpion poison damages
 the player at 5*N per minute (N is number of stings accumulated). It starts to add up.

```code
SCORPIONAttack:
0AC2: 86 1B               LDA     #$1B                      ; Is SCORPION ...
0AC4: BD 0A 0D            JSR     $0A0D                     ; ... alive?
0AC7: 24 1F               BCC     $AE8                      ; No ... reset counter and move on
0AC9: BD 09 43            JSR     $0943                     ; {IsObjInRoom} Is Scorpion in room with us?
0ACC: 24 1A               BCC     $AE8                      ; No ... reset counter and move on
0ACE: D6 44               LDB     <$44                      ; {ram:scorpTimer} Scorpion timer
0AD0: 27 26               BEQ     $AF8                      ; On 0 ... attack and random count
0AD2: C1 0F               CMPB    #$0F                      ; Count F?
0AD4: 26 0F               BNE     $AE5                      ; No ... next count and move on
0AD6: BD 06 61            JSR     $0661                     ; {Random} Random value
0AD9: 2B 10               BMI     $AEB                      ; 1/2 the time it vanishes for 16 seconds
0ADB: 8E 34 94            LDX     #$3494                    ; "THE SCORPION HAS JUST STUNG YOU."
0ADE: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
0AE1: 0C 09               INC     <$09                      ; {ram:stingCount} Add scorption sting count
0AE3: 20 0E               BRA     $AF3                      ; Vanish for 16 seconds
0AE5: 0C 44               INC     <$44                      ; {ram:scorpTimer} Next count
0AE7: 8C 0F 44            CMPX    #$0F44                    ; Clear count
0AEA: 39                  RTS                               ; Done
;
0AEB: C6 0A               LDB     #$0A                      ; Print ...
0AED: BD 10 48            JSR     $1048                     ; ... "THE SCORPION DISAPPEARS."
0AF0: BD 10 90            JSR     $1090                     ; {PrintCR} Print CR
0AF3: 86 F0               LDA     #$F0                      ; Vanish for ...
0AF5: 97 44               STA     <$44                      ; {ram:scorpTimer} ... 16 seconds
0AF7: 39                  RTS                               ; Done
;
0AF8: C6 0D               LDB     #$0D                      ; Random 0 ...
0AFA: BD 06 90            JSR     $0690                     ; {RandB} ... to 13
0AFD: 5C                  INCB                              ; 1 to 14
0AFE: D7 44               STB     <$44                      ; {ram:scorpTimer} Next scorpion count
0B00: 8D 01               BSR     $B03                      ; {SweepSounds} Sound effect
0B02: 39                  RTS                               ; Done
```

# Play Sounds 
 Simple 15-repeat sweep sound effect

```code
SweepSounds:
0B03: 34 16               PSHS    X,B,A                     ; Store params
0B05: 86 0F               LDA     #$0F                      ; Count ...
0B07: 97 53               STA     <$53                      ; {ram:m53} ... of 15
0B09: C6 A2               LDB     #$A2                      ; High value = 101000_10
0B0B: 86 6F               LDA     #$6F                      ; Delay
0B0D: C0 14               SUBB    #$14                      ; Drop volume
0B0F: 8E 00 50            LDX     #$0050                    ; 50 cycles
0B12: 8D 0E               BSR     $B22                      ; Play tone
0B14: 30 05               LEAX    5,X                       ; Next time ... 5 more cycles
0B16: 80 05               SUBA    #$05                      ; Raise frequency
0B18: 81 14               CMPA    #$14                      ; Still acceptibly low ...
0B1A: 22 F6               BHI     $B12                      ; ... use it
0B1C: 0A 53               DEC     <$53                      ; {ram:m53} Sweep count
0B1E: 26 E9               BNE     $B09                      ; Do all sweeps
0B20: 35 96               PULS    A,B,X,PC                  ; Out

; Do X cycles of a square wave. B is "high" value. 0 is the "low" value. Pause
; for count of A for high and low.
0B22: 34 06               PSHS    B,A                       ; Save params
0B24: A6 E4               LDA     ,S                        ; Delay
0B26: E6 61               LDB     1,S                       ; Sound value
0B28: F7 FF 20            STB     $FF20                     ; {hard:PIA1_DA} Store sound
0B2B: 4A                  DECA                              ; Do ...
0B2C: 26 FD               BNE     $B2B                      ; ... delay
0B2E: A6 E4               LDA     ,S                        ; Delay value again
0B30: C6 02               LDB     #$02                      ; Minimum ...
0B32: F7 FF 20            STB     $FF20                     ; {hard:PIA1_DA} ... sound level
0B35: 4A                  DECA                              ; Do ...
0B36: 26 FD               BNE     $B35                      ; ... delay
0B38: 30 1F               LEAX    -1,X                      ; Cycle count
0B3A: 26 E8               BNE     $B24                      ; Do all cycles
0B3C: 35 86               PULS    A,B,PC                    ; Out

; Sound effect
0B3E: 34 16               PSHS    X,B,A                     ; Save params
0B40: C6 1E               LDB     #$1E                      ; Random ...
0B42: BD 06 90            JSR     $0690                     ; {RandB} ... value 0-30
0B45: CB 0F               ADDB    #$0F                      ; Value 15-45
0B47: 86 14               LDA     #$14                      ; Number of ...
0B49: D7 53               STB     <$53                      ; {ram:m53} ... cycles
0B4B: C6 1F               LDB     #$1F                      ; Random ...
0B4D: BD 06 90            JSR     $0690                     ; {RandB} ... 0 to 31
0B50: 58                  ASLB                              ; Now 0 to 62
0B51: CB 10               ADDB    #$10                      ; Now 16 to 78
0B53: 34 04               PSHS    B                         ; Hold delay
0B55: 86 FF               LDA     #$FF                      ;
0B57: 54                  LSRB                              ;
0B58: 27 03               BEQ     $B5D                      ; 
0B5A: 44                  LSRA                              ; TO DO:
0B5B: 20 FA               BRA     $B57                      ; Figure out the sound ...
0B5D: C6 10               LDB     #$10                      ; ... details
0B5F: 3D                  MUL                               ;
0B60: 1F 01               TFR     D,X                       ;
0B62: 30 08               LEAX    8,X                       ;
0B64: 35 02               PULS    A                         ; Get delay
0B66: C6 A2               LDB     #$A2                      ; Volume
0B68: 8D B8               BSR     $B22                      ; Play tone
0B6A: 0A 53               DEC     <$53                      ; {ram:m53} All cycles?
0B6C: 26 DD               BNE     $B4B                      ; No ... back to do them all
0B6E: 35 96               PULS    A,B,X,PC                  ; Out

0B70: 34 10               PSHS    X                         ; Save params
0B72: 8E 34 82            LDX     #$3482                    ; "OUCH!! THAT HURT."
0B75: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
0B78: 35 90               PULS    X,PC                      ; Out
```

# Game Init 

```code
; Count number of list configuration possibilities
0B7A: 34 12               PSHS    X,A                       ; Save params
0B7C: 5F                  CLRB                              ; Start with B=0
0B7D: A6 80               LDA     ,X+                       ; Get protected object number
0B7F: 81 FF               CMPA    #$FF                      ; End of list?
0B81: 27 07               BEQ     $B8A                      ; Yes ... out
0B83: 81 80               CMPA    #$80                      ; 80?
0B85: 26 F6               BNE     $B7D                      ; No ... don't count this
0B87: 5C                  INCB                              ; Next
0B88: 20 F3               BRA     $B7D                      ; Keep looking for FF
0B8A: 35 92               PULS    A,X,PC                    ; Out

ConfigureProtected:
; Configure all protected object from random picks of pre-defined
; configurations (ensures never a no-win configuration).
0B8C: 34 30               PSHS    Y,X                       ; Save params
0B8E: 10 8E 3F B8         LDY     #$3FB8                    ; Protected object list
0B92: 8E 1D 4D            LDX     #$1D4D                    ; Protected configurations table
0B95: 8D E3               BSR     $B7A                      ; Count objects in list
0B97: 5D                  TSTB                              ; Empty list?
0B98: 27 2C               BEQ     $BC6                      ; Yes ... end
0B9A: BD 06 90            JSR     $0690                     ; {RandB} Random number 0 to num slots
0B9D: A6 80               LDA     ,X+                       ; Copy target object ...
0B9F: A7 A0               STA     ,Y+                       ; ... number
0BA1: 5D                  TSTB                              ; Found the right configuration?
0BA2: 27 09               BEQ     $BAD                      ; Yes ... go copy it
0BA4: A6 80               LDA     ,X+                       ; Look ...
0BA6: 81 80               CMPA    #$80                      ; ... for next ...
0BA8: 26 FA               BNE     $BA4                      ; ... configuration
0BAA: 5A                  DECB                              ; Count this
0BAB: 20 F4               BRA     $BA1                      ; Find right list
;    
0BAD: A6 80               LDA     ,X+                       ; Get required object
0BAF: 81 80               CMPA    #$80                      ; End of sublist?
0BB1: 27 08               BEQ     $BBB                      ; Yes ... out
0BB3: 81 FF               CMPA    #$FF                      ; End of sublists?
0BB5: 27 04               BEQ     $BBB                      ; Yes ... out
0BB7: A7 A0               STA     ,Y+                       ; Save object
0BB9: 20 F2               BRA     $BAD                      ; Do all in sub list
;
0BBB: 86 FF               LDA     #$FF                      ; Terminate this ...
0BBD: A7 A0               STA     ,Y+                       ; ... built list
0BBF: 30 1F               LEAX    -1,X                      ; Make sure we aren't on terminator
0BC1: BD 10 84            JSR     $1084                     ; Find FF terminator
0BC4: 20 CF               BRA     $B95                      ; Keep going
;
0BC6: 86 FF               LDA     #$FF                      ; Put FF ...
0BC8: A7 A4               STA     ,Y                        ; ... on end of list
0BCA: 35 B0               PULS    X,Y,PC                    ; Done

InitializeObjects:
0BCC: 34 76               PSHS    U,Y,X,B,A                 ; Save params
0BCE: 10 8E 3C F9         LDY     #$3CF9                    ; Object table
0BD2: 8E 20 D5            LDX     #$20D5                    ; Placement script
0BD5: CE 20 C5            LDU     #$20C5                    ; 16 possible protected-object rooms
;      
0BD8: 31 23               LEAY    3,Y                       ; Next object
0BDA: A6 80               LDA     ,X+                       ; Get placement command
0BDC: 81 55               CMPA    #$55                      ; End flag
0BDE: 27 40               BEQ     $C20                      ; Out
0BE0: E6 22               LDB     2,Y                       ; Object flags
0BE2: C4 7C               ANDB    #$7C                      ; Make it active ...
0BE4: E7 22               STB     2,Y                       ; ... and not in pack
0BE6: 4D                  TSTA                              ; Placement command
0BE7: 2B 16               BMI     $BFF                      ; If upper bit set ... place protected object
0BE9: 4A                  DECA                              ; Placement command
0BEA: 27 24               BEQ     $C10                      ; If 1 ... set invisible flag
0BEC: 4A                  DECA                              ; Placement command
0BED: 27 29               BEQ     $C18                      ; If 2 ... set spell
;
; (TYPE) Lower Upper Mask
0BEF: E6 01               LDB     1,X                       ; Upper bounds ...
0BF1: E0 81               SUBB    ,X++                      ; ... minus lower
0BF3: BD 06 90            JSR     $0690                     ; {RandB} Get a random room in range
0BF6: E4 80               ANDB    ,X+                       ; Additional masking
0BF8: EB 1D               ADDB    -3,X                      ; Add to lower bounds
0BFA: 4A                  DECA                              ; Placement command
0BFB: 27 09               BEQ     $C06                      ; If 3 ... also set protected
0BFD: 20 0D               BRA     $C0C                      ; Assign room to plain old object
;   
0BFF: C6 0F               LDB     #$0F                      ; 0-15 (16 entries)
0C01: BD 06 90            JSR     $0690                     ; {RandB} Get random ...
0C04: E6 C5               LDB     B,U                       ; ... valid room for a protected object
0C06: A6 22               LDA     2,Y                       ; Make ...
0C08: 8A 10               ORA     #$10                      ; ... object ...
0C0A: A7 22               STA     2,Y                       ; ... protected
0C0C: E7 A4               STB     ,Y                        ; Assign room
0C0E: 20 C8               BRA     $BD8                      ; Keep going
;    
0C10: A6 22               LDA     2,Y                       ; Get flags
0C12: 8A 01               ORA     #$01                      ; Make ...
0C14: A7 22               STA     2,Y                       ; ... invisible
0C16: 20 C0               BRA     $BD8                      ; Next object
  
0C18: A6 22               LDA     2,Y                       ; Flags
0C1A: 8A 42               ORA     #$42                      ; Set ...
0C1C: A7 22               STA     2,Y                       ; ... for spells
0C1E: 20 B8               BRA     $BD8                      ; Next object
;
0C20: 35 F6               PULS    A,B,X,Y,U,PC              ; Done

;
; Initialize lamp full of oil
0C22: CC 07 08            LDD     #$0708                    ; Init oil level ..
0C25: DD 38               STD     <$38                      ; {ram:lampOil} ... to 1800 second (30 minutes)
;
; Initialize Oracle's advice
0C27: 8E 1E 43            LDX     #$1E43                    ; Objects oracle gives advice on
0C2A: CE 00 1B            LDU     #$001B                    ; Flags in memory for advice
0C2D: A6 80               LDA     ,X+                       ; Advice from table
0C2F: 27 04               BEQ     $C35                      ; End of table ... move on
0C31: A7 C0               STA     ,U+                       ; Store advice object
0C33: 20 F8               BRA     $C2D                      ; Do them all
;
; Initialize Urn and Bottle
0C35: 86 0C               LDA     #$0C                      ; Full
0C37: B7 3D 2B            STA     $3D2B                     ; Urn flags ... full
0C3A: B7 3D 01            STA     $3D01                     ; Bottle flags ... full
0C3D: C6 06               LDB     #$06                      ; Original value
0C3F: F7 3D C1            STB     $3DC1                     ; OPEN DRAPES changes this to 7
;
; Initialize Packrat's trigger treasure
0C42: 8E 3C 6F            LDX     #$3C6F                    ; Treasure-held-by table
0C45: C6 0F               LDB     #$0F                      ; Random ...
0C47: BD 06 90            JSR     $0690                     ; {RandB} ... value 0-15
0C4A: 58                  ASLB                              ; Offset to treasure
0C4B: 5C                  INCB                              ; Treasure word
0C4C: A6 85               LDA     B,X                       ; Set packrat's ...
0C4E: 97 2C               STA     <$2C                      ; {ram:ratObject} ... trigger object
0C50: 39                  RTS                               ; Done

AssignHolders:
; Assign the 16 "held" treasures to an owner. Note that there are 17 possible
; owners. One of the creatures (not Minotaur) is selected at random to be "empty".
0C51: C6 05               LDB     #$05                      ; Get random ..
0C53: BD 06 90            JSR     $0690                     ; {RandB} ... value 0 to 5
0C56: CB 19               ADDB    #$19                      ; 25 - 30 (One of the creatures)
0C58: D7 2F               STB     <$2F                      ; {ram:temporary} Hold "empty" creature
0C5A: CE 3C 5F            LDU     #$3C5F                    ; List of owners
0C5D: 8E 3C 8F            LDX     #$3C8F                    ; End of "held by" table
0C60: 86 10               LDA     #$10                      ; 16 things held
0C62: 6F 83               CLR     ,--X                      ; Clear owner
0C64: 4A                  DECA                              ; All done?
0C65: 26 FB               BNE     $C62                      ; No ... clear all owners
0C67: 86 0F               LDA     #$0F                      ; 15
0C69: A7 E2               STA     ,-S                       ; Count on stack
0C6B: C6 0F               LDB     #$0F                      ; Random value ...
0C6D: BD 06 90            JSR     $0690                     ; {RandB} ... from 0 to 15
0C70: 58                  ASLB                              ; Offset in "held by" table
0C71: 6D 85               TST     B,X                       ; Object already held?
0C73: 26 F6               BNE     $C6B                      ; Yes ... find an object not held
0C75: A6 C6               LDA     A,U                       ; Next owner
0C77: 91 2F               CMPA    <$2F                      ; {ram:temporary} Is this the "empty" creature?
0C79: 26 02               BNE     $C7D                      ; No ... assign it
0C7B: 86 0B               LDA     #$0B                      ; Assign object to enter-room-r instead
0C7D: A7 85               STA     B,X                       ; New owner
0C7F: A6 E0               LDA     ,S+                       ; Get counter
0C81: 4A                  DECA                              ; Do all ...
0C82: 2A E5               BPL     $C69                      ; ... 16 objects
;    
PlaceSpells:
; Randomly place the 8 spells ... within the limits of a range-table.
0C84: 8E 1D 3D            LDX     #$1D3D                    ; Spell location-limit table
0C87: 10 8E 3B C3         LDY     #$3BC3                    ; Location of 1st spell
0C8B: 86 08               LDA     #$08                      ; 8 spells
0C8D: E6 01               LDB     1,X                       ; Upper room bounds
0C8F: E0 84               SUBB    ,X                        ; Lower room bounds
0C91: BD 06 90            JSR     $0690                     ; {RandB} Get random room ...
0C94: EB 81               ADDB    ,X++                      ; Between lower and upper inclusive
0C96: E7 A4               STB     ,Y                        ; Room of spell
0C98: 6F 21               CLR     1,Y                       ; Make sure spell is NOT learned
0C9A: 31 24               LEAY    4,Y                       ; Next spell
0C9C: 4A                  DECA                              ; All spells placed?
0C9D: 26 EE               BNE     $C8D                      ; No ... do all
0C9F: 39                  RTS                               ; Out

PlaceEnterRoomActions:
0CA0: 10 8E 3C 8C         LDY     #$3C8C                    ; Entering-room action table
0CA4: 8E 1D E6            LDX     #$1DE6                    ; Placement range table
0CA7: 86 1E               LDA     #$1E                      ; 30 actions to place
0CA9: 31 23               LEAY    3,Y                       ; Next action to place
0CAB: 30 03               LEAX    3,X                       ; Next range
0CAD: E6 01               LDB     1,X                       ; Get random ...
0CAF: E0 84               SUBB    ,X                        ; ... room ...
0CB1: BD 06 90            JSR     $0690                     ; {RandB} ... in ...
0CB4: EB 84               ADDB    ,X                        ; ... range
0CB6: E4 02               ANDB    2,X                       ; Additional placement mask
0CB8: E7 A4               STB     ,Y                        ; Store handler
0CBA: 4A                  DECA                              ; Do ...
0CBB: 26 EC               BNE     $CA9                      ; ... all handlers
;
; Place HYDRA with its action
0CBD: B6 3C A1            LDA     $3CA1                     ; We just placed the HYDRA action
0CC0: 97 33               STA     <$33                      ; {ram:hydraRoom} Put the HYDRA there
;
; Place SMALL PIT and JUMP to 39 with its action
0CC2: B6 3C E6            LDA     $3CE6                     ; We just placed the SMALL PIT action
0CC5: 97 35               STA     <$35                      ; {ram:smallPitRoom} Put the SMALL PIT there
0CC7: B7 3C 59            STA     $3C59                     ; {CodeBug6} Put the "JUMP DOWN" to room 39 with the pit
;
; Count on ISHTAR
0CCA: BD 06 61            JSR     $0661                     ; {Random} Random number
0CCD: C4 03               ANDB    #$03                      ; 0-3
0CCF: D7 34               STB     <$34                      ; {ram:ishtarUses} ISHTAR can be used 1-4 times
;
0CD1: CB 04               ADDB    #$04                      ; 4-7
0CD3: D7 3A               STB     <$3A                      ; {ram:lampFills} Number of refills in the OIL ROOM (action _v)
;
0CD5: C6 17               LDB     #$17                      ; Random ...
0CD7: BD 06 90            JSR     $0690                     ; {RandB} ... value 0 to 23
0CDA: CB 10               ADDB    #$10                      ; Value 16 to 39
0CDC: F7 3C F5            STB     $3CF5                     ; Set enter-action-bb
0CDF: 39                  RTS                               ; Done
```

# Game Entry Point
 Game starts here

```code
GameInit:
0CE0: 20 01               BRA     $CE3                      ; Three bytes to change to a jump ...
0CE2: FF                                      ; ... when debugging, I bet.

0CE3: 10 CE 01 FF         LDS     #$01FF                    ; Stack
0CE7: BD A9 28            JSR     $A928                     ; {hard:CLRSCREEN} Clear screen (BASIC)
0CEA: BD A9 76            JSR     $A976                     ; Enables sound (BASIC)
0CED: 5F                  CLRB                              ; 0
0CEE: 9E 8A               LDX     <$8A                      ; {ram:zeroWord} Always 0
0CF0: 6F 80               CLR     ,X+                       ; Clear out ...
0CF2: 8C 00 66            CMPX    #$0066                    ; ... RAM ...
0CF5: 23 F9               BLS     $CF0                      ; ... up through 66
;
0CF7: 8E 3E B8            LDX     #$3EB8                    ; Clear ...
0CFA: 6F 80               CLR     ,X+                       ; ... blocked ...
0CFC: 5A                  DECB                              ; ... pasasge ...
0CFD: 26 FB               BNE     $CFA                      ; ... table
;
0CFF: BD A9 A2            JSR     $A9A2                     ; SNDSEL ... sound source is DAC (BASIC)
0D02: 0F 68               CLR     <$68                      ; {ram:m67} Current line # of BASIC program. Don't know why we are setting this.
0D04: 0F 78               CLR     <$78                      ; {ram:m67} BASIC file status flag (set to closed). Don't know why we are setting this.
0D06: 0A 18               DEC     <$18                      ; {ram:randPoint} Force random number to reseed
0D08: 8E 2A D7            LDX     #$2AD7                    ; "WELCOME TO THE LABYRINTH!! BEWARE OF THE MINOTAUR AND GOOD LUCK."
0D0B: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
0D0E: BD 06 61            JSR     $0661                     ; {Random} Advance random number
0D11: BD A1 C1            JSR     $A1C1                     ; {hard:GETKEY} Get a key (BASIC)
0D14: 27 F8               BEQ     $D0E                      ; Keep waiting
0D16: BD 0B 8C            JSR     $0B8C                     ; {ConfigureProtected} Configure protected objects
0D19: BD 0B CC            JSR     $0BCC                     ; {InitializeObjects} Initialize all objects
0D1C: BD 0C 22            JSR     $0C22                     ; Init lamp oil (0708)
0D1F: BD 0C 51            JSR     $0C51                     ; {AssignHolders} Assign treasures to holders
0D22: BD 0C A0            JSR     $0CA0                     ; {PlaceEnterRoomActions} Place the enter-room-actions
0D25: 0A 05               DEC     <$05                      ; {ram:condition} Physical condition at max
0D27: 86 0A               LDA     #$0A                      ; Start in ...
0D29: 97 00               STA     <$00                      ; {ram:curRoom} ... Room 10
0D2B: 97 01               STA     <$01                      ; {ram:lastRoom} Last room is Room 10
0D2D: BD A9 28            JSR     $A928                     ; {hard:CLRSCREEN} Clear screen (BASIC)
0D30: BD 0E 27            JSR     $0E27                     ; Print room description
0D33: BD 07 2A            JSR     $072A                     ; Init ISR
```

# Main Loop 

```code
MainGameLoop:
0D36: 10 CE 01 FF         LDS     #$01FF                    ; Reset stack
0D3A: BD 08 59            JSR     $0859                     ; {UserInput} Get user input (3B points to screen where it starts)
0D3D: BD 08 A1            JSR     $08A1                     ; Get VERB (validate) and NOUN (don't validate)
0D40: BD 16 A7            JSR     $16A7                     ; {CalculateScore} Calculate score (detects win)
0D43: BD 10 90            JSR     $1090                     ; {PrintCR} Print CR
0D46: 8D 23               BSR     $D6B                      ; Execute command
0D48: 96 05               LDA     <$05                      ; {ram:condition} Physical condition
0D4A: 81 28               CMPA    #$28                      ; Is condition 40 or better
0D4C: 24 06               BCC     $D54                      ; Yes .. skip message
0D4E: 8E 2A 44            LDX     #$2A44                    ; YOUR SIGHT IS DIM
;
```

CodeBug8

 Joe Hagen found this bug. The code here calls 1066 (PrintMess). The "YOUR SIGHT IS DIM" 
 message at 2A44, however, is packed. The call should be to 102F (PrintPacked). The
 message never appears in the game. Joe modified the code and verified the fix in the
 emulator. Good job, Joe.
 
```code 
0D51: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
0D54: BD 06 C7            JSR     $06C7                     ; Learn any spell in our room that we can
0D57: BD 16 A7            JSR     $16A7                     ; {CalculateScore} Calculate score again
0D5A: 20 DE               BRA     $D3A                      ; Next command cycle
```

# Individual Commands  

## UNCLE 
 Print score and start a new game.

```code
CommandUNCLE:
0D5C: 8E 34 D8            LDX     #$34D8                    ; "YOU PUT UP A GOOD FIGHT, BETTER LUCK NEXT TIME."
0D5F: BD 10 66            JSR     $1066                     ; {PrintMess} Print message
0D62: BD 16 F8            JSR     $16F8                     ; {CommandSCORE} Print score
0D65: BD A1 B1            JSR     $A1B1                     ; Blink cursor and wait for key (BASIC)
0D68: 7E 0C E0            JMP     $0CE0                     ; {GameInit} Start game

0D6B: 8E 27 D4            LDX     #$27D4                    ; Command table
0D6E: 96 2A               LDA     <$2A                      ; {ram:verbNum} Command number
0D70: 48                  ASLA                              ; Two bytes per entry
0D71: 6E 96               JMP     [A,X]                     ; Execute the command
  
; Get bit number for set bit.
; Get the bit number of the first bit set from the left
0D73: 86 FF               LDA     #$FF                      ; Start at 0
0D75: 4C                  INCA                              ; Next bit number
0D76: 54                  LSRB                              ; Shift to right
0D77: 24 FC               BCC     $D75                      ; Not a 1 ... keep going
0D79: 39                  RTS                               ; Done
      
; Get reverse direction for dir-bits in B
0D7A: 34 12               PSHS    X,A                       ; Save params
0D7C: 8E 0D 85            LDX     #$0D85                    ; Reverse direction table
0D7F: 8D F2               BSR     $D73                      ; Direction bit to number
0D81: E6 86               LDB     A,X                       ; Get opposite direction
0D83: 35 92               PULS    A,X,PC                    ; Done

; Reverse direction table
0D85: 08  ; South -> North
0D86: 04  ; West -> East                     
0D87: 02  ; East -> West                              
0D88: 01  ; North -> South                             
0D89: 20  ; Down -> Up
0D8A: 10  ; Up -> Down                 

; Can we see (lamp is on and in room or pack)?
; C=1 yes
; C=0 no
0D8B: 34 16               PSHS    X,B,A                     ; Save params
0D8D: C6 0C               LDB     #$0C                      ; Lamp
0D8F: BD 1A 5A            JSR     $1A5A                     ; {GetObject} Get data
0D92: A6 02               LDA     2,X                       ; Flags
0D94: 2B 06               BMI     $D9C                      ; In pack ... yes it is here
0D96: A6 84               LDA     ,X                        ; Is lamp in ...
0D98: 91 00               CMPA    <$00                      ; {ram:curRoom} ... current room
0D9A: 26 04               BNE     $DA0                      ; No ... not here ... C=0 and out
0D9C: 96 0A               LDA     <$0A                      ; {ram:lampOn} Lamp status
0D9E: 26 03               BNE     $DA3                      ; Lamp is on ... Z=0
0DA0: 4F                  CLRA                              ; C=0 ... not glowing
0DA1: 20 01               BRA     $DA4                      ; Out
0DA3: 43                  COMA                              ; C=1 ... is glowing
0DA4: 35 96               PULS    A,B,X,PC                  ; Out

; If we can't see, print message and return C=1. There is also an increasing chance
; of dieing with each step in darkness.
0DA6: 34 36               PSHS    Y,X,B,A                   ; Save params
0DA8: 8D E1               BSR     $D8B                      ; Can we see?
0DAA: 25 2A               BCS     $DD6                      ; Yes ... out
0DAC: 96 00               LDA     <$00                      ; {ram:curRoom} Current room
0DAE: 81 28               CMPA    #$28                      ; First 40 room ..
0DB0: 25 24               BCS     $DD6                      ; ... have ambient light
0DB2: 81 CA               CMPA    #$CA                      ; The forest ...
0DB4: 27 20               BEQ     $DD6                      ; ... has ambient light
0DB6: BD 06 61            JSR     $0661                     ; {Random} Random number
0DB9: BD 10 90            JSR     $1090                     ; {PrintCR} Print CR
0DBC: D1 08               CMPB    <$08                      ; {ram:fallOdds} Random number smaller than current value?
0DBE: 25 0E               BCS     $DCE                      ; Yes ... we died
0DC0: 8E 2B 26            LDX     #$2B26                    ; "IT'S DARK AND YOU CAN'T SEE - IF YOU CONTINUE, YOU MAY FALL."
0DC3: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
0DC6: D6 08               LDB     <$08                      ; {ram:fallOdds} Current value
0DC8: CB 1F               ADDB    #$1F                      ; Odds are 0 then 1/8 then 2/8 then 3/8 ... (each step better chance of falling)
0DCA: D7 08               STB     <$08                      ; {ram:fallOdds} New value
0DCC: 20 0C               BRA     $DDA                      ; Return with C=1 (can't see)
;
0DCE: 8E 2B 62            LDX     #$2B62                    ; "YOU HAVE JUST FALLEN INTO A PIT AND KILLED YOURSELF."
0DD1: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
0DD4: 20 86               BRA     $D5C                      ; {CommandUNCLE} UNCLE ... new game
;    
0DD6: 0F 08               CLR     <$08                      ; {ram:fallOdds} Reset moving in darkness
0DD8: 4F                  CLRA                              ; C=0
0DD9: 21 43               BRN     $E1E                      ; COMA
0DDB: 35 B6               PULS    A,B,X,Y,PC                ; Out
```

## BACK 
 Move to last room if we haven't been here for 16 seconds. We turn off the
 "in poison room" flag if we move.

```code
CommandBACK:
0DDD: 9E 4C               LDX     <$4C                      ; {ram:secsInRoom} Too late to ...
0DDF: 8C 00 0F            CMPX    #$000F                    ; ... go back?
0DE2: 24 43               BCC     $E27                      ; Yes ... print room description and out
0DE4: 96 01               LDA     <$01                      ; {ram:lastRoom} Last room ...
0DE6: 97 00               STA     <$00                      ; {ram:curRoom} ... to current room
0DE8: BD 07 25            JSR     $0725                     ; Now out of the MYSTERIOUS FOG
0DEB: 20 3A               BRA     $E27                      ; Print room description and out
```

## MOVE 
 Move player from room to room.

 In addition to "natural" passages, there is a table of blocks. Passages may become blocked or
 ublbocked over time.

``` 
 1 Clear mysterious fog flag and HYDRA-pushed-us flags<br>
 2 If direction is not natural stay here<br>
 3 Execute any handlers between rooms<br>
 4 If handler didn't deny move then make the move to the new room<br>
 5 If passage is blocked don't do anything (having the powerring lets you walk through blocks)<br>
 6 Print room description (includes picking up spells)
```

```code
CommandUP:
CommandDOWN:
CommandNORTH:
CommandEAST:
CommandSOUTH:
CommandWEST:
0DED: 86 20               LDA     #$20                      ; UP
0DEF: 8C 86 10            CMPX    #$8610                    ; DOWN
0DF2: 8C 86 08            CMPX    #$8608                    ; NORTH
0DF5: 8C 86 04            CMPX    #$8604                    ; EAST
0DF8: 8C 86 02            CMPX    #$8602                    ; SOUTH
0DFB: 8C 86 01            CMPX    #$8601                    ; WEST
0DFE: 97 02               STA     <$02                      ; {ram:dirBits} Hold the bit pattern
0E00: 0F 14               CLR     <$14                      ; {ram:lampStripped} We've moved. VETAR will not work.
0E02: BD 07 25            JSR     $0725                     ; Now out of the MYSTERIOUS FOG
0E05: 0F 0F               CLR     <$0F                      ; {ram:hydraPushed} HYDRA is no longer here
0E07: BD 0F 93            JSR     $0F93                     ; Get doors in this room
0E0A: 96 02               LDA     <$02                      ; {ram:dirBits} Direction bit pattern
0E0C: A4 84               ANDA    ,X                        ; Can we go in that direction?
0E0E: 26 06               BNE     $E16                      ; Yes ... go
0E10: 96 00               LDA     <$00                      ; {ram:curRoom} Current room ...
0E12: 97 01               STA     <$01                      ; {ram:lastRoom} ... is last room
0E14: 20 11               BRA     $E27                      ; Print room description

0E16: 0F 0C               CLR     <$0C                      ; {ram:downFail} Clear the flag for "don't move us"
0E18: BD 0F 27            JSR     $0F27                     ; Execute any handler when moving between rooms
0E1B: 96 0C               LDA     <$0C                      ; {ram:downFail} Did handler tell us to skip moving?
0E1D: 26 08               BNE     $E27                      ; Yes ... bypass moving
0E1F: 17 00 B4            LBSR    $0ED6                     ; Open path or wearing powerring?
0E22: 25 03               BCS     $E27                      ; No ... bypass moving
0E24: BD 0F 84            JSR     $0F84                     ; Change rooms
  
; Print description
0E27: BD 0F E0            JSR     $0FE0                     ; Print "CRACKLING WITH ENCHANTMENT" if a spell is here
0E2A: BD 0D A6            JSR     $0DA6                     ; Check for darkness (maybe die)
0E2D: 25 05               BCS     $E34                      ; Dark ... nothing more to see.
0E2F: BD 0F 09            JSR     $0F09                     ; Print current room description
0E32: 8D 78               BSR     $EAC                      ; {PrintObjectsInRoom} Print objects in room
0E34: BD 0E EC            JSR     $0EEC                     ; Process enter-room actions
0E37: 39                  RTS                               ; Done
               
; Look for noun in pack
0E38: 34 02               PSHS    A                         ; Save params
0E3A: BD 18 CD            JSR     $18CD                     ; Convert noun to object
0E3D: 1F 89               TFR     A,B                       ; To B
0E3F: 24 03               BCC     $E44                      ; Not valid ... return not valid
0E41: BD 18 85            JSR     $1885                     ; {InPack} Return is-in-pack
0E44: 35 82               PULS    A,PC                      ; Out
  
; Print description for object B
0E46: 34 10               PSHS    X                         ; Save parameters
0E48: 8E 1E 51            LDX     #$1E51                    ; Object descriptions
0E4B: 8D 05               BSR     $E52                      ; Find right description
0E4D: BD 10 2F            JSR     $102F                     ; {PrintPacked} Print description
0E50: 35 90               PULS    X,PC                      ; Out
      
0E52: 34 04               PSHS    B                         ; Save object
0E54: A6 80               LDA     ,X+                       ; Object number
0E56: A1 E4               CMPA    ,S                        ; The one we want?
0E58: 27 0E               BEQ     $E68                      ; Yes ... return it
0E5A: 81 FF               CMPA    #$FF                      ; End of list?
0E5C: 27 04               BEQ     $E62                      ; Yes ... next object
0E5E: A6 80               LDA     ,X+                       ; Skip ...
0E60: 20 F8               BRA     $E5A                      ; ... to end
0E62: A6 80               LDA     ,X+                       ; Next object
0E64: 81 FF               CMPA    #$FF                      ; End of list?
0E66: 26 EE               BNE     $E56                      ; No ... keep looking
0E68: 35 84               PULS    B,PC                      ; Out

; Find any object "held" by the given owner A. If A has a "held" object,
; B returns that object number. If not, B returns 0.
0E6A: 34 12               PSHS    X,A                       ; Params
0E6C: 8E 3C 6F            LDX     #$3C6F                    ; Holding table
0E6F: C6 10               LDB     #$10                      ; 16 words
0E71: A6 81               LDA     ,X++                      ; Does it ...
0E73: A1 E4               CMPA    ,S                        ; ... match?
0E75: 27 05               BEQ     $E7C                      ; Yes ... get held object and out
0E77: 5A                  DECB                              ; All 16 done?
0E78: 26 F7               BNE     $E71                      ; No ... keep going
0E7A: 35 92               PULS    A,X,PC                    ; Out
;
0E7C: E6 1F               LDB     -1,X                      ; Get held object
0E7E: 20 FA               BRA     $E7A                      ; Out
 
DropHeldObj:
;Drop object "held" by A into current room.
; C=1 if dropped
; C=0 if not dropped
0E80: 34 16               PSHS    X,B,A                     ; Save params
0E82: 8D E6               BSR     $E6A                      ; Find object held by A
0E84: 5D                  TSTB                              ; Any object held?
0E85: 27 1F               BEQ     $EA6                      ; No ... NOTHING SPECIAL and out
0E87: BD 1A 5A            JSR     $1A5A                     ; {GetObject} Get pointer to object
0E8A: E6 02               LDB     2,X                       ; Flags
0E8C: C5 01               BITB    #$01                      ; Held object already visible?
0E8E: 27 16               BEQ     $EA6                      ; Yes ... NOTHING SPECIAL and out
0E90: C4 FC               ANDB    #$FC                      ; Make the held object visible and not in pack
0E92: E7 02               STB     2,X                       ; Reset flags
0E94: 96 00               LDA     <$00                      ; {ram:curRoom} Current room
0E96: A7 84               STA     ,X                        ; To held object's location
0E98: E6 01               LDB     1,X                       ; Object description
0E9A: BD 18 6D            JSR     $186D                     ; Print object name
0E9D: 8E 33 63            LDX     #$3363                    ; "IS NOW LAYING AT YOUR FEET!"
0EA0: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
0EA3: 43                  COMA                              ; C=1
0EA4: 35 96               PULS    A,B,X,PC                  ; Done

0EA6: BD 10 1E            JSR     $101E                     ; "NOTHING SPECIAL HAPPENS"
0EA9: 4F                  CLRA                              ; C=0
0EAA: 35 96               PULS    A,B,X,PC                  ; Done

PrintObjectsInRoom:
0EAC: 8E 3C F9            LDX     #$3CF9                    ; Object data
0EAF: 30 03               LEAX    3,X                       ; Next object
0EB1: EC 84               LDD     ,X                        ; A=Room, B=name
0EB3: C1 FF               CMPB    #$FF                      ; End of table?
0EB5: 27 1E               BEQ     $ED5                      ; Yes ... out
0EB7: 91 00               CMPA    <$00                      ; {ram:curRoom} Object in room?
0EB9: 26 F4               BNE     $EAF                      ; No ... keep looking
0EBB: A6 02               LDA     2,X                       ; Get flags
0EBD: 2B F0               BMI     $EAF                      ; Already in pack ... ignore
0EBF: 46                  RORA                              ; Object invisible?
0EC0: 25 ED               BCS     $EAF                      ; Yes ... skip it
0EC2: 46                  RORA                              ; Object invisible?
0EC3: 25 EA               BCS     $EAF                      ; Yes ... skip it
0EC5: 5F                  CLRB                              ; Zero offset (for non protected)
0EC6: A6 02               LDA     2,X                       ; Flags again
0EC8: 84 10               ANDA    #$10                      ; Protected?
0ECA: 27 02               BEQ     $ECE                      ; No ... use zero offset
0ECC: C6 80               LDB     #$80                      ; Wrap around for protected objects
0ECE: EB 01               ADDB    1,X                       ; Get name of object
0ED0: BD 0E 46            JSR     $0E46                     ; Print description of object
0ED3: 20 DA               BRA     $EAF                      ; Keep going
0ED5: 39                  RTS                               ; Done
       
; Return C=0 if path is open or powerring is in pack. C=1 if blocked and no powerring.
0ED6: 34 10               PSHS    X                         ; Save params
0ED8: 96 02               LDA     <$02                      ; {ram:dirBits} Direction bits
0EDA: A4 89 01 00         ANDA    $0100,X                   ; Check block
0EDE: 27 09               BEQ     $EE9                      ; No blocks ... return C=0
0EE0: C6 2A               LDB     #$2A                      ; Powerring ...
0EE2: BD 18 85            JSR     $1885                     ; {InPack} ... in pack?
0EE5: 25 02               BCS     $EE9                      ; Yes ... return C=0
0EE7: 43                  COMA                              ; C=1
0EE8: 21 4F               BRN     $F39                      ; CLRA C=0
0EEA: 35 90               PULS    X,PC                      ; Out

0EEC: 34 16               PSHS    X,B,A                     ; Save params
0EEE: 8E 3C 8F            LDX     #$3C8F                    ; Enter-room actions
0EF1: 96 00               LDA     <$00                      ; {ram:curRoom} Current room
0EF3: A1 84               CMPA    ,X                        ; Found an entry for this room?
0EF5: 27 09               BEQ     $F00                      ; Yes ... do routine
0EF7: 30 03               LEAX    3,X                       ; Next entry
0EF9: 8C 3C FB            CMPX    #$3CFB                    ; All done?
0EFC: 25 F3               BCS     $EF1                      ; No ... keep looking
0EFE: 35 96               PULS    A,B,X,PC                  ; Out
0F00: 34 16               PSHS    X,B,A                     ; Save params
0F02: AD 98 01            JSR     [$01,X]                   ; Do the routine
0F05: 35 16               PULS    A,B,X                     ; Restore
0F07: 20 EE               BRA     $EF7                      ; Keep looking for more
  
; Find current room description and print
0F09: 34 10               PSHS    X                         ; Save params
0F0B: 8E 21 65            LDX     #$2165                    ; Room description list
0F0E: D6 00               LDB     <$00                      ; {ram:curRoom} Current room number
0F10: 8D 05               BSR     $F17                      ; Get the right description
0F12: BD 0F 9A            JSR     $0F9A                     ; Print it
0F15: 35 90               PULS    X,PC                      ; Out

; Find desired string B (terminated by FF)
0F17: 34 06               PSHS    B,A                       ; Save params
0F19: C6 FF               LDB     #$FF                      ; Start count with 0
0F1B: 5C                  INCB                              ; Next string
0F1C: E1 61               CMPB    1,S                       ; Is this the one we are looking for?
0F1E: 27 05               BEQ     $F25                      ; Yes ... out
0F20: BD 10 84            JSR     $1084                     ; Find FF terminator
0F23: 20 F6               BRA     $F1B                      ; Keep looking
0F25: 35 86               PULS    A,B,PC                    ; Done

; Execute any handler between the room and target room in either direction
0F27: 34 10               PSHS    X                         ; Store params
0F29: 30 8D 2C 1D         LEAX    $2C1D,PC                  ; 3B4A
0F2D: 96 00               LDA     <$00                      ; {ram:curRoom} Current room
0F2F: D6 02               LDB     <$02                      ; {ram:dirBits} Direction pattern
0F31: 8D 07               BSR     $F3A                      ; Look for a handler between the rooms
0F33: 24 03               BCC     $F38                      ; No handler ... out
0F35: AD 98 02            JSR     [$02,X]                   ; Do the handler
0F38: 35 90               PULS    X,PC                      ; Restore and out
;
; Look for match for Room/Direction or TargetRoom/ReverseDirection
; C=0 if not found
; C=1 if found
0F3A: 34 46               PSHS    U,B,A                     ; Save params
0F3C: 1F 13               TFR     X,U                       ; Hold X for a moment
0F3E: 8D 1C               BSR     $F5C                      ; Look for room/direction action
0F40: 25 18               BCS     $F5A                      ; Z=0 ... found ... out
0F42: EC E4               LDD     ,S                        ; Room A, direction B
0F44: 8D 2B               BSR     $F71                      ; Get target room
0F46: BD 0D 7A            JSR     $0D7A                     ; Get reverse direction
0F49: 1E 89               EXG     A,B                       ; A to B
0F4B: 8D 48               BSR     $F95                      ; Get passages for room B
0F4D: A5 84               BITA    ,X                        ; Reverse direction open?
0F4F: 27 08               BEQ     $F59                      ; No ... Z=1 and out
0F51: 1E 89               EXG     A,B                       ; New room A, reverse direction B
0F53: 1F 31               TFR     U,X                       ; Restore original room
0F55: 8D 05               BSR     $F5C                      ; Look for match
0F57: 20 01               BRA     $F5A                      ; Return match or not
0F59: 4F                  CLRA                              ; Z=1 ... not found
0F5A: 35 C6               PULS    A,B,U,PC                  ; Done
;
0F5C: 10 A3 84            CMPD    ,X                        ; A=room, B=direction
0F5F: 27 08               BEQ     $F69                      ; Found ... Z=0
0F61: 30 04               LEAX    4,X                       ; Try next
0F63: 6D 01               TST     1,X                       ; All done?
0F65: 26 F5               BNE     $F5C                      ; No .... keep looking
0F67: 4F                  CLRA                              ; C=0 not found
0F68: 21 43               BRN     $FAD                      ; COMA at F69
0F6A: 39                  RTS                               ; Out
                 
; Geometry of room connections
0F6B: 08 ; SOUTH  +8
0F6C: FF ; WEST   -1                   
0F6D: 01 ; EAST   +1                          
0F6E: F8 ; NORTH  -8
0F6F: 40 ; DOWN   +64
0F70: C0 ; UP     -64           

; Calculate target room from A in direction B 
0F71: 34 16               PSHS    X,B,A                     ; Save params
0F73: 5D                  TSTB                              ; Any direction bits set?
0F74: 27 0C               BEQ     $F82                      ; No ... out
0F76: 8E 0F 6B            LDX     #$0F6B                    ; Offset for directions
0F79: BD 0D 73            JSR     $0D73                     ; Get number of set bit
0F7C: A6 86               LDA     A,X                       ; Get the offset
0F7E: AB E0               ADDA    ,S+                       ; Add to current room
0F80: 35 94               PULS    B,X,PC                    ; Done
;
0F82: 35 96               PULS    A,B,X,PC                  ; Done

; Change rooms based on direction
0F84: 96 00               LDA     <$00                      ; {ram:curRoom} Current room ...
0F86: 97 01               STA     <$01                      ; {ram:lastRoom} ... to last room
0F88: D6 02               LDB     <$02                      ; {ram:dirBits} Direction bits
0F8A: 8D E5               BSR     $F71                      ; Offset room number based on direction
0F8C: 97 00               STA     <$00                      ; {ram:curRoom} New current room
0F8E: 0F 4C               CLR     <$4C                      ; {ram:secsInRoom} Clear room ...
0F90: 0F 4D               CLR     <$4D                      ; {ram:secsInRoom} ... timer for BACK
0F92: 39                  RTS                               ; Done
            
; Get room doors
0F93: D6 00               LDB     <$00                      ; {ram:curRoom} Current room number
0F95: 8E 3D B8            LDX     #$3DB8                    ; Room door table
0F98: 3A                  ABX                               ; Offset into table
0F99: 39                  RTS                               ; Done
   
; Print "YOU ARE "+room description (with random door descriptions).
0F9A: 34 16               PSHS    X,B,A                     ; Save params
0F9C: 86 82               LDA     #$82                      ; "YOU ARE
0F9E: BD 10 54            JSR     $1054                     ; {PrintWord} Print ... all room descriptions start with "YOU ARE"
0FA1: BD 10 2F            JSR     $102F                     ; {PrintPacked} Get current room description
0FA4: 8D ED               BSR     $F93                      ; Get doors (pointed to by X)
0FA6: 10 8E 3B 3E         LDY     #$3B3E                    ; Direction description table
0FAA: 86 01               LDA     #$01                      ; Bit 1
0FAC: 20 03               BRA     $FB1                      ; Skip over loop increment
0FAE: 48                  ASLA                              ; Next direction
0FAF: 31 22               LEAY    2,Y                       ; Next in table;
0FB1: 81 40               CMPA    #$40                      ; All directions checked?
0FB3: 27 29               BEQ     $FDE                      ; Yes ... out
0FB5: A5 84               BITA    ,X                        ; This direction open?
0FB7: 27 F5               BEQ     $FAE                      ; No ... skip
0FB9: 34 16               PSHS    X,B,A                     ; Save params
0FBB: BD 06 61            JSR     $0661                     ; {Random} Random number
0FBE: C4 07               ANDB    #$07                      ; 0-7
0FC0: D7 17               STB     <$17                      ; {ram:randPass} Hold
0FC2: AE A4               LDX     ,Y                        ; Pointer to passage in directions
0FC4: 86 FF               LDA     #$FF                      ; Get ...
0FC6: 4C                  INCA                              ; ... the ...
0FC7: 91 17               CMPA    <$17                      ; {ram:randPass} ... right
0FC9: 27 05               BEQ     $FD0                      ; ... message
0FCB: 17 00 B6            LBSR    $1084                     ; Find the FF terminator
0FCE: 20 F6               BRA     $FC6                      ; Keep going
0FD0: 8D 5D               BSR     $102F                     ; {PrintPacked} Print the direction string
0FD2: 35 16               PULS    A,B,X                     ; Restore
;
0FD4: A5 89 01 00         BITA    $0100,X                   ; Checked "blocked" table
0FD8: 27 D4               BEQ     $FAE                      ; Directin not blocked ... keep our description
0FDA: 8D 23               BSR     $FFF                      ; Append ", BUT IT IS BLOCKED"
0FDC: 20 D0               BRA     $FAE                      ; Next direction
;
0FDE: 35 96               PULS    A,B,X,PC                  ; Done
  
0FE0: 34 16               PSHS    X,B,A                     ; Save params
0FE2: 8E 3B BD            LDX     #$3BBD                    ; Spell data
0FE5: 86 08               LDA     #$08                      ; Eight spells
0FE7: 30 04               LEAX    4,X                       ; Next spell
0FE9: E6 02               LDB     2,X                       ; Rooms
0FEB: D1 00               CMPB    <$00                      ; {ram:curRoom} Spell in current room?
0FED: 26 0B               BNE     $FFA                      ; No ... keep looking
0FEF: E6 03               LDB     3,X                       ; Learned flags
0FF1: 2B 07               BMI     $FFA                      ; We already know it ... skip
0FF3: 8E 32 C9            LDX     #$32C9                    ; "THE AIR IS CRACKLING WITH ENCHANTMENT."
0FF6: 8D 6E               BSR     $1066                     ; {PrintMess} Print the message
0FF8: 20 03               BRA     $FFD                      ; Out
0FFA: 4A                  DECA                              ; All spells checked?
0FFB: 26 EA               BNE     $FE7                      ; No ... check all
0FFD: 35 96               PULS    A,B,X,PC                  ; Done
  
0FFF: 34 16               PSHS    X,B,A                     ; Save params
1001: 9E 88               LDX     <$88                      ; {ram:scrCursor} Cursor
1003: 86 6C               LDA     #$6C                      ; ","
1005: D6 0B               LDB     <$0B                      ; {ram:spacesOnEnd} Any skipped space
1007: C0 02               SUBB    #$02                      ; Back up two characters to the period
1009: A7 85               STA     B,X                       ; Replace period with a coma
100B: 5F                  CLRB                              ; Message 0 is ...
100C: 8D 3A               BSR     $1048                     ; ... BUT IT IS BLOCKED
100E: 35 96               PULS    A,B,X,PC                  ; Done
 
1010: 34 10               PSHS    X                         ; Align stack for return
1012: 8E 2C 85            LDX     #$2C85                    ; "I DON'T SEE ANYTHING INTERESTING."
1015: 20 13               BRA     $102A                     ; Print and out

1017: 34 10               PSHS    X                         ; Align stack for return
1019: 8E 2A 79            LDX     #$2A79                    ; "OK"
101C: 20 0C               BRA     $102A                     ; Print and out

101E: 34 10               PSHS    X                         ; Align stack for return
1020: 8E 31 F1            LDX     #$31F1                    ; "NOTHING SPECIAL HAPPENS."
1023: 20 05               BRA     $102A                     ; Print and out

1025: 34 10               PSHS    X                         ; Align stack for return
1027: 8E 2C 7B            LDX     #$2C7B                    ; "WITH WHAT?"
102A: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
102D: 35 90               PULS    X,PC                      ; Done
     
PrintPacked:
; Print list of words pointed to by X.
102F: 34 06               PSHS    B,A                       ; Save params
1031: A6 80               LDA     ,X+                       ; Get next word token
1033: 81 FF               CMPA    #$FF                      ; Are we done?
1035: 27 04               BEQ     $103B                     ; Yes ... clean up
1037: 8D 1B               BSR     $1054                     ; {PrintWord} Print word
1039: 20 F6               BRA     $1031                     ; Continue
;
103B: 8D 02               BSR     $103F                     ; Backup over last space after word and print period.
103D: 35 86               PULS    A,B,PC                    ; Done

103F: 34 10               PSHS    X                         ; Save param
1041: 8E 2A D5            LDX     #$2AD5                    ; Backspace over space and period
1044: 8D 20               BSR     $1066                     ; {PrintMess} Print the message
1046: 35 90               PULS    X,PC                      ; Out
     
1048: 34 16               PSHS    X,B,A                     ; Save params
104A: 8E 29 C8            LDX     #$29C8                    ; Message (BUT IT IS BLOCKED)
104D: BD 0F 17            JSR     $0F17                     ; Find string
1050: 8D DD               BSR     $102F                     ; {PrintPacked} Print message
1052: 35 96               PULS    A,B,X,PC                  ; Done
   
PrintWord:
; Print word number A followed by space
1054: 34 16               PSHS    X,B,A                     ; Save params
1056: 8E 35 C6            LDX     #$35C6                    ; Start of word list
1059: 97 2F               STA     <$2F                      ; {ram:temporary} Hold word number
105B: C6 FF               LDB     #$FF                      ; Start count at 0
105D: 5C                  INCB                              ; Current word number
105E: D1 2F               CMPB    <$2F                      ; {ram:temporary} Have we found it?
1060: 27 06               BEQ     $1068                     ; Yes ... go print word
1062: 8D 19               BSR     $107D                     ; No ... skip word
1064: 20 F7               BRA     $105D                     ; Keep looking

PrintMess:
; Print message pointed to by X and then a black block character (space).
1066: 34 16               PSHS    X,B,A                     ; Save params
1068: A6 80               LDA     ,X+                       ; Get character from string
106A: 2B 05               BMI     $1071                     ; End? Go handle end and out
106C: BD 06 00            JSR     $0600                     ; {PrintWrap} Print character
106F: 20 F7               BRA     $1068                     ; Keep going
1071: 84 7F               ANDA    #$7F                      ; Strip of terminator bit
1073: BD 06 00            JSR     $0600                     ; {PrintWrap} Print last character
1076: 86 20               LDA     #$20                      ; Print black ...
1078: BD 06 00            JSR     $0600                     ; {PrintWrap} ... cursor character (space)
107B: 35 96               PULS    A,B,X,PC                  ; Done

; Skip to the end of the message
107D: 6D 80               TST     ,X+                       ; Find the ...
107F: 2B 02               BMI     $1083                     ; ... end of ...
1081: 20 FA               BRA     $107D                     ; ... the message
1083: 39                  RTS                               ; Done

; Find the FF terminator
1084: 34 06               PSHS    B,A                       ; Save params
1086: A6 80               LDA     ,X+                       ; Get the next byte
1088: 81 FF               CMPA    #$FF                      ; Found the FF?
108A: 27 02               BEQ     $108E                     ; Yes ... out
108C: 20 F8               BRA     $1086                     ; No ... keep looking
108E: 35 86               PULS    A,B,PC                    ; Done

PrintCR:
; Print a CR
1090: 34 02               PSHS    A                         ; Save params
1092: 86 0D               LDA     #$0D                      ; CR
1094: BD 06 00            JSR     $0600                     ; {PrintWrap} Print CR
1097: 35 82               PULS    A,PC                      ; Done

ComWHAT:
; Print command + " WHAT?"
1099: 8E 27 26            LDX     #$2726                    ; Command words
109C: 86 FF               LDA     #$FF                      ; Start with 0
109E: 4C                  INCA                              ; Next command word
109F: 91 2A               CMPA    <$2A                      ; {ram:verbNum} This is the input word?
10A1: 27 04               BEQ     $10A7                     ; Yes ... go handle it
10A3: 8D D8               BSR     $107D                     ; Skip to end of command word
10A5: 20 F7               BRA     $109E                     ; Keep looking
10A7: 8D BD               BSR     $1066                     ; {PrintMess} Print the command word (and space)
10A9: 8E 34 1B            LDX     #$341B                    ; "WHAT?"
10AC: 20 4D               BRA     $10FB                     ; Print and return

10AE: 34 16               PSHS    X,B,A                     ; Save params
10B0: 8E 2B 17            LDX     #$2B17                    ; "YOU DROPPED THE"
10B3: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
10B6: BD 18 6D            JSR     $186D                     ; Print object
10B9: BD 10 3F            JSR     $103F                     ; Backspace and period
10BC: 35 96               PULS    A,B,X,PC                  ; Out
```

## DROP 
 Drop object in current room and adjust pack weight.

```code
CommandDROPTHROW:
10BE: 0F 2F               CLR     <$2F                      ; {ram:temporary} Clear found-flag
10C0: 96 2B               LDA     <$2B                      ; {ram:nounNum} Noun
10C2: 81 FF               CMPA    #$FF                      ; Was there a noun?
10C4: 26 02               BNE     $10C8                     ; Yes ... continue
10C6: 20 D1               BRA     $1099                     ; {ComWHAT} No ... "THROW WHAT?"
;
10C8: BD 18 CD            JSR     $18CD                     ; Convert to object number
10CB: 24 F9               BCC     $10C6                     ; Invalid
10CD: 81 37               CMPA    #$37                      ; Is this a real object (not ...
10CF: 24 F5               BCC     $10C6                     ; ... a spell or other?) No ... error
10D1: 8E 3C F9            LDX     #$3CF9                    ; Object data
10D4: 30 03               LEAX    3,X                       ; Next object
10D6: A6 01               LDA     1,X                       ; Get the word
10D8: 81 FF               CMPA    #$FF                      ; End of list
10DA: 27 18               BEQ     $10F4                     ; Yes ... error out
10DC: 91 07               CMPA    <$07                      ; {ram:nounObjNum} Matches our noun?
10DE: 26 F4               BNE     $10D4                     ; No ... keep looking
10E0: A6 02               LDA     2,X                       ; Flags
10E2: 2A F0               BPL     $10D4                     ; Not in pack ... next
10E4: 0C 2F               INC     <$2F                      ; {ram:temporary} Flag we found it
10E6: D6 00               LDB     <$00                      ; {ram:curRoom} Current room
10E8: E7 84               STB     ,X                        ; To object's location
10EA: E6 02               LDB     2,X                       ; Mask off ...
10EC: C4 7F               ANDB    #$7F                      ; ... in pack
10EE: E7 02               STB     2,X                       ; Update flags
10F0: 8D 11               BSR     $1103                     ; Update bulk/weight
10F2: 20 E0               BRA     $10D4                     ; Do all objects
;
10F4: 96 2F               LDA     <$2F                      ; {ram:temporary} Did we find one?
10F6: 26 06               BNE     $10FE                     ; Yes ... print OK
10F8: 8E 2A AB            LDX     #$2AAB                    ; "YOU DON'T HAVE THAT."
10FB: 7E 10 66            JMP     $1066                     ; {PrintMess} Print and return
;
10FE: 8E 2A 79            LDX     #$2A79                    ; "OK"
1101: 20 F8               BRA     $10FB                     ; Print and return

; Readjust carry weight/bulk for dropped object in $07
1103: 34 26               PSHS    Y,B,A                     ; Save params
1105: BD 19 8C            JSR     $198C                     ; Get buld/weight for object
1108: 96 04               LDA     <$04                      ; {ram:weight} Subtract ...
110A: A0 A0               SUBA    ,Y+                       ; ... dropped weight
110C: 24 01               BCC     $110F                     ; Still something
110E: 4F                  CLRA                              ; Zero if negative weight
110F: 97 04               STA     <$04                      ; {ram:weight} Store new weight
1111: 96 06               LDA     <$06                      ; {ram:bulk} Subtract ...
1113: A0 A4               SUBA    ,Y                        ; ... dropped bulk
1115: 24 01               BCC     $1118                     ; Still something
1117: 4F                  CLRA                              ; Zero if negative bulk
1118: 97 06               STA     <$06                      ; {ram:bulk} New bulk
111A: 35 A6               PULS    A,B,Y,PC                  ; Out

; Open scroll   
; On 3rd or 4th floor it brings the Troglodyte to us.
111C: C6 12               LDB     #$12                      ; Do we have ...
111E: BD 18 85            JSR     $1885                     ; {InPack} ... the scroll?
1121: 24 36               BCC     $1159                     ; No ... "OPEN WHAT?"
1123: 96 00               LDA     <$00                      ; {ram:curRoom} Current room
1125: 2A 70               BPL     $1197                     ; On floor 1 or 2 ... "Nothing interesting" and out
1127: B7 3D 47            STA     $3D47                     ; Bring Trodlodyte to us
112A: 20 68               BRA     $1194                     ; "OK" and out

; Open jewlbox     
; If opened in Minotaur's lair then the Minotaur comes.
112C: C6 16               LDB     #$16                      ; Do we haave ...
112E: BD 18 85            JSR     $1885                     ; {InPack} ... the jewlbox
1131: 24 26               BCC     $1159                     ; No ... "OPEN WHAT?"
1133: 96 00               LDA     <$00                      ; {ram:curRoom} Current room
1135: 81 9E               CMPA    #$9E                      ; In room 158 (Minotaur's lair)
1137: 26 5E               BNE     $1197                     ; No ... "Nothing interesting" and out
1139: B7 3D 53            STA     $3D53                     ; Bring the Minotaur to us
113C: 20 56               BRA     $1194                     ; "OK" and out
```

## OPEN 

```code
CommandOPEN:
113E: 96 2B               LDA     <$2B                      ; {ram:nounNum} Noun
1140: 81 74               CMPA    #$74                      ; "CRYPT" ?
1142: 27 18               BEQ     $115C                     ; {OpenCrypt} Yes ... go handle crypt
1144: 81 33               CMPA    #$33                      ; "DRAPES" ?
1146: 27 34               BEQ     $117C                     ; {OpenDrapes} Yes ... go handle drapes
1148: 81 B7               CMPA    #$B7                      ; "SCROLL" ?
114A: 27 D0               BEQ     $111C                     ; Yes ... go handle scroll
114C: 81 E5               CMPA    #$E5                      ; "JEWLBOX" ?
114E: 27 DC               BEQ     $112C                     ; Yes ... go handle jewlbox
1150: 81 FF               CMPA    #$FF                      ; Is it even valid?
1152: 26 05               BNE     $1159                     ; Yes ... "OPEN WHAT?"
1154: 8E 2A C0            LDX     #$2AC0                    ; "DON'T BE RIDICULOUS."
1157: 20 20               BRA     $1179                     ; Print and return
;
1159: 7E 10 99            JMP     $1099                     ; {ComWHAT} command+" WHAT?"

OpenCrypt:
; If pys-weight is 250 or better the treasure falls out.
115C: 96 00               LDA     <$00                      ; {ram:curRoom} Current room
115E: 81 43               CMPA    #$43                      ; Are we in the crypt room?
1160: 26 38               BNE     $119A                     ; {OpenCryptKing} May be in the crypt of the king
;
1162: 96 05               LDA     <$05                      ; {ram:condition} Physical condition ...
1164: 90 04               SUBA    <$04                      ; {ram:weight} ... less than weight?
1166: 25 0E               BCS     $1176                     ; Yes ... can't open it
1168: 81 FA               CMPA    #$FA                      ; Physical condition ...
116A: 25 0A               BCS     $1176                     ; ... must be 250 to open
116C: 86 01               LDA     #$01                      ; Owner 1 is the crypt
116E: BD 0E 80            JSR     $0E80                     ; {DropHeldObj} Drop any object owned by the crypt
1171: 8E 2E B6            LDX     #$2EB6                    ; "A CLOUD OF SMOKE FILLS THE ROOM AND AN EERIE HOWL ECHOS OFF THE WALLS AS THE TOP FALLS SHUT."
1174: 20 03               BRA     $1179                     ; Print and return
1176: 8E 2E A1            LDX     #$2EA1                    ; "THE TOP WON'T BUDGE."
1179: 7E 10 66            JMP     $1066                     ; {PrintMess} Print and return

OpenDrapes:
; Open drapes (1/4th chance of opening passage leading south from room 9 ... we only
; get one shot at opening).
117C: 96 00               LDA     <$00                      ; {ram:curRoom} Current room
117E: 81 09               CMPA    #$09                      ; Right room?
1180: 26 D7               BNE     $1159                     ; No ... "OPEN WHAT?"
1182: 96 12               LDA     <$12                      ; {ram:drapesOpen} Already tried passage?
1184: 26 11               BNE     $1197                     ; Yes ... error message
1186: 0C 12               INC     <$12                      ; {ram:drapesOpen} Now we have tried (whether we succeeded or not)
1188: BD 06 61            JSR     $0661                     ; {Random} Random number
118B: C1 40               CMPB    #$40                      ; 3/4 th of the time ...
118D: 24 08               BCC     $1197                     ; ... nothing happens
118F: C6 07               LDB     #$07                      ; --UDNEWS = --000111 ...
1191: F7 3D C1            STB     $3DC1                     ; ... (open passage to south)
1194: 7E 10 17            JMP     $1017                     ; Print "OK" and return
;    
1197: 7E 10 10            JMP     $1010                     ; Print "I DON'T SEE ANYTHING INTERESTING" and return
    
OpenCryptKing:
; If phys- bulk is 250 or better or have the Powerring treasure falls out.
119A: 81 66               CMPA    #$66                      ; Crypt of the ancient king?
119C: 26 BB               BNE     $1159                     ; No ... "OPEN WHAT?"
119E: C6 2A               LDB     #$2A                      ; Got the ...
11A0: BD 18 85            JSR     $1885                     ; {InPack} ... powerring?
11A3: 25 0A               BCS     $11AF                     ; Yes ... automatically get the treasure
11A5: 96 05               LDA     <$05                      ; {ram:condition} Physical condition ...
11A7: 90 06               SUBA    <$06                      ; {ram:bulk} ... less than bulk?
11A9: 25 CB               BCS     $1176                     ; Yes ... can't open
11AB: 81 FA               CMPA    #$FA                      ; Takes physical condition of 250 to open
11AD: 25 C7               BCS     $1176                     ; Not strong enough ... error and out
11AF: 86 02               LDA     #$02                      ; Drop treasure held by ...
11B1: BD 0E 80            JSR     $0E80                     ; {DropHeldObj} ... crypt of the kings
11B4: 20 BB               BRA     $1171                     ; Print the message of the object appearing
```

## ASK 
 Print the list of "required objects" for a protected object and move oracle to a random
 room.

```code
CommandASK:
11B6: 96 2B               LDA     <$2B                      ; {ram:nounNum} Noun
11B8: 81 AE               CMPA    #$AE                      ; "ASK ORACLE" ?
11BA: 27 03               BEQ     $11BF                     ; Yes ... go do it
11BC: 7E 10 99            JMP     $1099                     ; {ComWHAT} "ASK WHAT?" and out
11BF: B6 3D 56            LDA     $3D56                     ; Oracle's room
11C2: 91 00               CMPA    <$00                      ; {ram:curRoom} Oracle in current room
11C4: 27 06               BEQ     $11CC                     ; Yes ... "ASK" is OK
11C6: 8E 2B B5            LDX     #$2BB5                    ; "ASK WHO?" error
11C9: 7E 10 66            JMP     $1066                     ; {PrintMess} Print the message
;
11CC: 10 8E 00 1B         LDY     #$001B                    ; Flags that advice has been given and for what objects
11D0: C6 0D               LDB     #$0D                      ; Number of advices given so far.
11D2: D1 1A               CMPB    <$1A                      ; {ram:numAdviceGiven} Compare 13 to number given so far
11D4: 22 0C               BHI     $11E2                     ; Number given is less than 13 ... still have ungiven
;
11D6: 0F 1A               CLR     <$1A                      ; {ram:numAdviceGiven} Reset number of advices
11D8: 5A                  DECB                              ; Reset ...
11D9: A6 A5               LDA     B,Y                       ; ... all ...
11DB: 84 7F               ANDA    #$7F                      ; ... advice ...
11DD: A7 A5               STA     B,Y                       ; ... given ...
11DF: 5A                  DECB                              ; ... flags ...
11E0: 2A F7               BPL     $11D9                     ; ... to start over with advice
;
11E2: 0C 1A               INC     <$1A                      ; {ram:numAdviceGiven} Number of advices given
;
11E4: C6 0C               LDB     #$0C                      ; Number of advices (0 to C ... 13 advices)
11E6: BD 06 90            JSR     $0690                     ; {RandB} Random advice slot
11E9: D7 51               STB     <$51                      ; {ram:m51} Hold it
11EB: A6 A5               LDA     B,Y                       ; This advice already been given?
11ED: 2B F5               BMI     $11E4                     ; Yes ... try again
;
11EF: 8E 2B BD            LDX     #$2BBD                    ; "A MYSTERIOUS CALM SETTLES OVER THE ROOM AS THE ORACLE SPEAKS..."
11F2: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
11F5: 8E 2C A7            LDX     #$2CA7                    ; "TO LEARN THE SECRET OF THE"
11F8: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
11FB: E6 A5               LDB     B,Y                       ; Object
11FD: BD 18 6D            JSR     $186D                     ; Get the word
1200: 8E 2B FC            LDX     #$2BFC                    ; "YOU MUST POSSESS THE"
1203: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
1206: D6 51               LDB     <$51                      ; {ram:m51} Protected object number
1208: 8D 16               BSR     $1220                     ; Print the list of required
120A: A6 A5               LDA     B,Y                       ; Advice flag
120C: 8A 80               ORA     #$80                      ; Advice has been given
120E: A7 A5               STA     B,Y                       ; Store flag
1210: C6 07               LDB     #$07                      ; "THE ORACLE VANISHES"
1212: BD 10 48            JSR     $1048                     ; Print message
1215: BD 06 61            JSR     $0661                     ; {Random} Random room
1218: C4 DF               ANDB    #$DF                      ; 1st half of whichever floor
121A: F7 3D 56            STB     $3D56                     ; New room for oracle
121D: 7E 0B 3E            JMP     $0B3E                     ; Sound efect

1220: 34 16               PSHS    X,B,A                     ; Save params
1222: 8E 3F B8            LDX     #$3FB8                    ; Protected list
1225: BD 0F 17            JSR     $0F17                     ; Find desired list
1228: 30 01               LEAX    1,X                       ; Skip target object number
122A: E6 80               LDB     ,X+                       ; Get next object
122C: C4 3F               ANDB    #$3F                      ; Mask off bits
122E: BD 18 6D            JSR     $186D                     ; Print object name
1231: E6 84               LDB     ,X                        ; End of ...
1233: 5C                  INCB                              ; ... list?
1234: 27 07               BEQ     $123D                     ; Yes .. add period and out
1236: 86 2F               LDA     #$2F                      ; "AND"
1238: BD 10 54            JSR     $1054                     ; {PrintWord} Print AND
123B: 20 ED               BRA     $122A                     ; Continue
;
123D: BD 10 3F            JSR     $103F                     ; Backspace over space and period and print
1240: BD 10 90            JSR     $1090                     ; {PrintCR} Print a CR
1243: 35 96               PULS    A,B,X,PC                  ; Done
```

## EAT 

```code
CommandEAT:
1245: 96 2B               LDA     <$2B                      ; {ram:nounNum} Noun
1247: 81 94               CMPA    #$94                      ; Is it FOOD?
1249: 27 1E               BEQ     $1269                     ; {EatFood} Handle food
124B: 81 CA               CMPA    #$CA                      ; Is it MUSHROOM?
124D: 27 3F               BEQ     $128E                     ; {EatMushroom} Handle mushroom
124F: 81 B4               CMPA    #$B4                      ; Powder
1251: 27 05               BEQ     $1258                     ; {EatPowder} Handle powder
1253: 8E 2A C0            LDX     #$2AC0                    ; "DON'T BE RIDICULOUS."
1256: 20 33               BRA     $128B                     ; Print and out
;
EatPowder:
; Powder goes to random room. URN and BOTTLE come to this room.
1258: C6 27               LDB     #$27                      ; Powder object
125A: 8D 5C               BSR     $12B8                     ; Move it to random room if we have it
125C: 24 0F               BCC     $126D                     ; Didn't have it ... error and out
125E: 96 00               LDA     <$00                      ; {ram:curRoom} Current room
1260: B7 3D 29            STA     $3D29                     ; Move the URN here
1263: B7 3C FF            STA     $3CFF                     ; Move the BOTTLE here
1266: 7E 10 17            JMP     $1017                     ; "OK" and out
;
EatFood:
; Move the food to a random room and add 30 to physical condition.
1269: 8D 42               BSR     $12AD                     ; Check for object in pack
126B: 25 05               BCS     $1272                     ; Got it .. go eat it
126D: 8E 2A AB            LDX     #$2AAB                    ; "YOU DON'T HAVE THAT."
1270: 20 19               BRA     $128B                     ; Print and out
1272: 86 01               LDA     #$01                      ; Object FOOD
1274: BD 06 61            JSR     $0661                     ; {Random} Random value (new place for food)
1277: C4 5F               ANDB    #$5F                      ; Limit destination (not maze ... 1st and 2nd floor)
1279: 1E 98               EXG     B,A                       ; Align parameters
127B: BD 12 C6            JSR     $12C6                     ; Drop food from pack to room A
127E: 86 1E               LDA     #$1E                      ; Add 30 ...
1280: BD 1A 4E            JSR     $1A4E                     ; ... to physical condition
1283: 8E 2C 10            LDX     #$2C10                    ; "THANK YOU, I NEEDED THAT."
1286: 8D 03               BSR     $128B                     ; Print message
1288: 8E 2C 2A            LDX     #$2C2A                    ; "IT WAS YUMMY."
128B: 7E 10 66            JMP     $1066                     ; {PrintMess} Print the message and out
;
EatMushroom:
; 1/32 chance it is poison and we die. Otherwise adds 60 to physical condition.
128E: 8D 1D               BSR     $12AD                     ; Find object in pack
1290: 24 DB               BCC     $126D                     ; Didn't find it ... YOU DON'T HAVE THAT
1292: BD 06 61            JSR     $0661                     ; {Random} Random number
1295: C1 08               CMPB    #$08                      ; 1/32 chance of no damage
1297: 24 09               BCC     $12A2                     ; No damage
1299: 8E 31 72            LDX     #$3172                    ; "IT'S POISONOUS!!"
129C: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
129F: 7E 0D 5C            JMP     $0D5C                     ; {CommandUNCLE} UNCLE and new game
;
12A2: 86 3C               LDA     #$3C                      ; Add 60 ...
12A4: BD 1A 4E            JSR     $1A4E                     ; ... to health
12A7: C6 09               LDB     #$09                      ; Move mushroom ...
12A9: 8D 0D               BSR     $12B8                     ; ... from pack to random room
12AB: 20 D6               BRA     $1283                     ; I NEEDED THAT

12AD: BD 18 CD            JSR     $18CD                     ; Convert noun to object number
12B0: 24 05               BCC     $12B7                     ; Not valid ... out
12B2: D6 07               LDB     <$07                      ; {ram:nounObjNum} Get object number
12B4: BD 18 85            JSR     $1885                     ; {InPack} Check for object in pack
12B7: 39                  RTS                               ; Done

12B8: BD 18 85            JSR     $1885                     ; {InPack} Object B in pack?
12BB: 24 FA               BCC     $12B7                     ; No ... out
12BD: 34 04               PSHS    B                         ; Hold object
12BF: BD 06 61            JSR     $0661                     ; {Random} Random number ...
12C2: 1F 98               TFR     B,A                       ; ... to A
12C4: 35 04               PULS    B                         ; Object number again
;
12C6: D7 07               STB     <$07                      ; {ram:nounObjNum} To parameter
12C8: BD 11 03            JSR     $1103                     ; Adjust weight in pack for dropping B
12CB: 34 16               PSHS    X,B,A                     ; Save all
12CD: BD 1A 5A            JSR     $1A5A                     ; {GetObject} Get object data
12D0: E6 02               LDB     2,X                       ; Flags
12D2: C4 7F               ANDB    #$7F                      ; Not in pack anymore
12D4: E7 02               STB     2,X                       ; New flags
12D6: A7 84               STA     ,X                        ; New room
12D8: 43                  COMA                              ; Set C=1
12D9: 35 96               PULS    A,B,X,PC                  ; Out
```

## DRINK 

```code
CommandDRINK:
12DB: 96 2B               LDA     <$2B                      ; {ram:nounNum} Noun word
12DD: 81 2D               CMPA    #$2D                      ; "WATER"
12DF: 27 4A               BEQ     $132B                     ; {DrinkWater} Go drink the water
12E1: 81 BA               CMPA    #$BA                      ; "SPRITE"
12E3: 27 0F               BEQ     $12F4                     ; {DrinkSPRITE} Error for drinking the sprite (get it? the soda?)
12E5: 81 B6               CMPA    #$B6                      ; "POTION"
12E7: 27 17               BEQ     $1300                     ; {CodeBug1} Yes ... go handle potion
12E9: 81 FF               CMPA    #$FF                      ; No noun?
12EB: 10 27 FD AA         LBEQ    $1099                     ; {ComWHAT} No noun ... "DRINK WHAT?" and out
12EF: 8E 2A C0            LDX     #$2AC0                    ; "DON'T BE RIDICULOUS."
12F2: 20 41               BRA     $1335                     ; Print and out
;
DrinkSPRITE:
; Get it ... as in the soda? Nothing happens.      
12F4: B6 3D 44            LDA     $3D44                     ; Sprite's location
12F7: 91 00               CMPA    <$00                      ; {ram:curRoom} Is sprite in current room?
12F9: 26 62               BNE     $135D                     ; No ... "DRINK WHAT?"
12FB: 8E 34 6D            LDX     #$346D                    ; "YOU MUST BE KIDDING!"
12FE: 20 35               BRA     $1335                     ; Print and out
;
DirnkPotion:
; Drop potion to random room. Add 200 to physical condition. If stung by scorpion, there is 7/8 
; chance of healing it.
CodeBug1:
; Drink POTION 
; Nice bug in code here. If you don't have the POTION but try and drink it you'll
; get the error "THE BOTTLE IS EMPTY." Intersting that the bug comes in a routine
; that starts at unlucky 1300.
1300: 8D AB               BSR     $12AD                     ; Check for POTION in pack
1302: 24 50               BCC     $1354                     ; Not there ... "THE BOTTLE IS EMPTY" Bug!
1304: 1F 98               TFR     B,A                       ; Align parameters
1306: BD 06 61            JSR     $0661                     ; {Random} Random number
1309: CA 80               ORB     #$80                      ; Set upper bit
130B: 1E 98               EXG     B,A                       ; Align parameters
130D: 8D B7               BSR     $12C6                     ; Drop to random room
130F: 86 C8               LDA     #$C8                      ; Add 200 to ...
1311: BD 1A 4E            JSR     $1A4E                     ; ... physical condition
1314: D6 09               LDB     <$09                      ; {ram:stingCount} Scorpion sting count
1316: 26 05               BNE     $131D                     ; If stung ... there is good chance of healing
1318: 8E 2C 5D            LDX     #$2C5D                    ; "THAT IS VERY STRONG MEDICINE."
131B: 20 18               BRA     $1335                     ; Print message and out
131D: BD 06 61            JSR     $0661                     ; {Random} Random number
1320: C1 20               CMPB    #$20                      ; There is a 1/8 chance ...
1322: 25 F4               BCS     $1318                     ; ... of doing nothing
1324: 0F 09               CLR     <$09                      ; {ram:stingCount} Remove sting
1326: 8E 2C 38            LDX     #$2C38                    ; "THE SCORPION'S STING HAS BEEN CURED."
1329: 20 0A               BRA     $1335                     ; Print and out

DrinkWater:
; Empties the bottle and adds 32 to our physical condition. We can only heal this way once
; every 16 minutes.
132B: C6 02               LDB     #$02                      ; Is bottle ...
132D: BD 18 85            JSR     $1885                     ; {InPack} ... in pack?
1330: 25 06               BCS     $1338                     ; Yes
1332: 8E 2A AB            LDX     #$2AAB                    ; "YOU DON'T HAVE THAT."
1335: 7E 10 66            JMP     $1066                     ; {PrintMess} Print the message and out
1338: BD 1A 5A            JSR     $1A5A                     ; {GetObject} Get object
133B: E6 02               LDB     2,X                       ; Get data
133D: C5 0C               BITB    #$0C                      ; Empty or full?
133F: 27 13               BEQ     $1354                     ; The bottle is empty
1341: C4 F3               ANDB    #$F3                      ; Now ...
1343: E7 02               STB     2,X                       ; ... it is empty
1345: D6 3E               LDB     <$3E                      ; {ram:drinkTimer} Enough time passed since last drinking?
1347: 26 08               BNE     $1351                     ; No ... skip healing
1349: 86 20               LDA     #$20                      ; Heal ...
134B: BD 1A 4E            JSR     $1A4E                     ; ... by 32 points
134E: 44                  LSRA                              ; Must wait ...
134F: 97 3E               STA     <$3E                      ; {ram:drinkTimer} ... 16 minutes
1351: 7E 10 17            JMP     $1017                     ; Print "OK" and continue
;
1354: C6 0E               LDB     #$0E                      ; "THE BOTTLE IS EMPTY."
1356: 7E 10 48            JMP     $1048                     ; Print and  out
```

## CLIMB 
 If the LEDGE is here and we have the rope, drop the treasure. 

```code
CommandCLIMB:    
1359: 96 2B               LDA     <$2B                      ; {ram:nounNum} Noun
135B: 81 FD               CMPA    #$FD                      ; "LEDGE"?
135D: 10 26 FD 38         LBNE    $1099                     ; {ComWHAT} No .... Command+" WHAT?"
1361: 96 36               LDA     <$36                      ; {ram:ledgeRoom} Room of ledge
1363: 91 00               CMPA    <$00                      ; {ram:curRoom} Current room
1365: 10 26 05 7C         LBNE    $18E5                     ; "I DO NOT SEE ANY LEDGE" and out
1369: C6 18               LDB     #$18                      ; See if rope ...
136B: BD 18 85            JSR     $1885                     ; {InPack} ... is in pack
136E: 10 24 FC B3         LBCC    $1025                     ; "WITH WHAT?" and out
1372: 86 06               LDA     #$06                      ; Drop treasure held ...
1374: 7E 0E 80            JMP     $0E80                     ; {DropHeldObj} ... by ledge at feet
```

## TIE
 If tieing HYDRA and it just pushed us back and we have the rope then bind 
 it with the rope. The rope is dropped from our pack and bound to the HYDRA.

```code
CommandTIE:      
1377: 96 2B               LDA     <$2B                      ; {ram:nounNum} Noun
1379: 81 FC               CMPA    #$FC                      ; "HYDRA" ?
137B: 27 03               BEQ     $1380                     ; Yes .... handle
137D: 7E 10 99            JMP     $1099                     ; {ComWHAT} "TIE WHAT?" and out
1380: 96 0F               LDA     <$0F                      ; {ram:hydraPushed} Did HYDRA just push us?
1382: 27 22               BEQ     $13A6                     ; No ... I DO NOT SEE and out
1384: C6 18               LDB     #$18                      ; See if ...
1386: D7 07               STB     <$07                      ; {ram:nounObjNum} ... rope ...
1388: BD 18 85            JSR     $1885                     ; {InPack} ... is in pack
138B: 24 16               BCC     $13A3                     ; No ... "WITH WHAT" and out
138D: BD 10 17            JSR     $1017                     ; "OK"
1390: BD 1A 5A            JSR     $1A5A                     ; {GetObject} Get rope object
1393: E6 02               LDB     2,X                       ; Get flags
1395: C4 7F               ANDB    #$7F                      ; No longer in pack
1397: CA 01               ORB     #$01                      ; No longer accessible
1399: E7 02               STB     2,X                       ; New flags
139B: BD 11 03            JSR     $1103                     ; Readjust pack weight/bulk for dropped rope
139E: 86 AA               LDA     #$AA                      ; Set HYDRA status to ...
13A0: 97 0E               STA     <$0E                      ; {ram:hydraStatus} ... tied up
13A2: 39                  RTS                               ; Out
;
13A3: 7E 10 25            JMP     $1025                     ; "WITH WHAT?" and out
13A6: 7E 18 E5            JMP     $18E5                     ; "I DO NOT SEE ANY" and out
```

## HELP
 Just a comical message. 

```code
CommandHELP:      
13A9: 8E 32 60            LDX     #$3260                    ; "DON'T ASK ME FOR HELP - YOU GOT YOURSELF INTO THIS MESS!"
13AC: 7E 10 66            JMP     $1066                     ; {PrintMess} Print the message
```

## STAB 
 If stabbing HYDRA we must be in room with it (so it must be bound). Sword requires physical
 condition of 200. Dagger requires 240. MACE and AX both miss. If physical condition is met
 then HYDRA dies and it drops treasure and rope.

```code
CommandSTAB:
13AF: 96 2B               LDA     <$2B                      ; {ram:nounNum} Get noun
13B1: 81 FC               CMPA    #$FC                      ; Stabbing the "HYDRA" ?
13B3: 27 03               BEQ     $13B8                     ; Yes ... go stap hydra
13B5: 7E 10 99            JMP     $1099                     ; {ComWHAT} Command+"WHAT?"
13B8: 96 33               LDA     <$33                      ; {ram:hydraRoom} Hydra's room
13BA: 91 00               CMPA    <$00                      ; {ram:curRoom} Current room
13BC: 26 E8               BNE     $13A6                     ; "I DO NOT SEE ANY" and out
13BE: C6 06               LDB     #$06                      ; Sword in ...
13C0: BD 18 85            JSR     $1885                     ; {InPack} ... pack?
13C3: 25 23               BCS     $13E8                     ; Yes .... go stab with sword
13C5: C6 03               LDB     #$03                      ; Dagger in ...
13C7: BD 18 85            JSR     $1885                     ; {InPack} ... pack?
13CA: 24 0C               BCC     $13D8                     ; No ... move on
13CC: 96 05               LDA     <$05                      ; {ram:condition} Physical condition
13CE: 81 F0               CMPA    #$F0                      ; Must be 240 of 256 to hit Hydra with dagger
13D0: 24 1C               BCC     $13EE                     ; We are ... go do it
13D2: 8E 2E 11            LDX     #$2E11                    ; "YOU MISSED."
13D5: 7E 10 66            JMP     $1066                     ; {PrintMess} Print the message
13D8: C6 04               LDB     #$04                      ; Mace in ...
13DA: BD 18 85            JSR     $1885                     ; {InPack} ... pack?
13DD: 25 F3               BCS     $13D2                     ; Yes ... missed with mace
13DF: C6 05               LDB     #$05                      ; Ax in ...
13E1: BD 18 85            JSR     $1885                     ; {InPack} ... pack?
13E4: 25 EC               BCS     $13D2                     ; Yes ... missed with ax
13E6: 20 BB               BRA     $13A3                     ; "WITH WHAT?" and out
;
; Stab hydra with sword.
13E8: 96 05               LDA     <$05                      ; {ram:condition} Physical condition
13EA: 81 C8               CMPA    #$C8                      ; Must be 200 to hit Hydra with sword
13EC: 25 E4               BCS     $13D2                     ; MISSED and out
13EE: 20 00               BRA     $13F0                     ; Got it
;
; Hydra dies
13F0: 86 01               LDA     #$01                      ; HYDRA is ...
13F2: 97 0E               STA     <$0E                      ; {ram:hydraStatus} ... dead
13F4: C6 18               LDB     #$18                      ; Get object ...
13F6: BD 1A 5A            JSR     $1A5A                     ; {GetObject} ... "ROPE"
13F9: A6 02               LDA     2,X                       ; Flags
13FB: 85 01               BITA    #$01                      ; Is flag in use on hydra?
13FD: 27 08               BEQ     $1407                     ; No ... leave it alone
13FF: 84 7E               ANDA    #$7E                      ; Not in pack or in use
1401: A7 02               STA     2,X                       ; New status
1403: 96 33               LDA     <$33                      ; {ram:hydraRoom} Drop rope ...
1405: A7 84               STA     ,X                        ; ... where HYDRA was
1407: 8E 33 07            LDX     #$3307                    ; "THE HYDRA IS DEAD!"
140A: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
140D: 86 07               LDA     #$07                      ; Drop the ...
140F: 7E 0E 80            JMP     $0E80                     ; {DropHeldObj} ... 7th object (Hydra was carying in)
```

## Use Spell

### VETAR 
 Take 10 damage. GET LAMP immediately after it has been blown away. 
 Note the SCROLL can be used to retrieve the lamp on the 4th floor.

```code
CommandVETAR:
1412: 8D 3F               BSR     $1453                     ; Make sure spell has been learned
1414: 24 3B               BCC     $1451                     ; "NOTHING SPECIAL HAPPENS"
1416: 96 14               LDA     <$14                      ; {ram:lampStripped} Has VETAR been temporarily enabled?
1418: 27 37               BEQ     $1451                     ; No ... "NOTHING SPECIAL HAPPENS"
141A: 86 A6               LDA     #$A6                      ; "LAMP" word
141C: 97 2B               STA     <$2B                      ; {ram:nounNum} As if typed (for GET in a sec)
141E: 96 00               LDA     <$00                      ; {ram:curRoom} Current room
1420: B7 3D 1D            STA     $3D1D                     ; Move lamp to this room
1423: 7E 18 F7            JMP     $18F7                     ; {CommandGETTAKEGRAB} "GET LAMP"
```

### MITR 
 Take 12 damage. Remove scorpion sting.

```code
CommandMITR: 
1426: 8D 2B               BSR     $1453                     ; Make sure spell has been learned
1428: 24 27               BCC     $1451                     ; "NOTHING SPECIAL HAPPENS"
142A: 96 09               LDA     <$09                      ; {ram:stingCount} Poison sting
142C: 27 23               BEQ     $1451                     ; Not stung ... "NOTHING SPECIAL HAPPENS"
142E: 7E 13 24            JMP     $1324                     ; Remove scorpion sting
;
1431: 39                  RTS                               ; Done
```

### OKKAN
 Take 14 damage. Get treasure from "pile of rocks" if it is here.

```code
CommandOKKAN:             
1432: 8D 1F               BSR     $1453                     ; Make sure spell has been learned
1434: 24 1B               BCC     $1451                     ; "NOTHING SPECIAL HAPPENS"
1436: 96 11               LDA     <$11                      ; {ram:rocksExposed} Already done this?
1438: 26 F7               BNE     $1431                     ; Out
143A: 96 10               LDA     <$10                      ; {ram:rocksMoved} Has pile of rocks been moved to us?
143C: 27 13               BEQ     $1451                     ; No ... "NOTHING SPECIAL HAPPENS"
143E: 96 37               LDA     <$37                      ; {ram:rocksRoom} Location of "pile of rocks"
1440: 91 00               CMPA    <$00                      ; {ram:curRoom} Current room
1442: 26 0D               BNE     $1451                     ; "NOTHING SPECIAL HAPPENS"
1444: 8E 31 AB            LDX     #$31AB                    ; "THE LIGHT GROWS STRONGER UNTIL THE ENTIRE ROOM IS BATHED IN ITS GLOW."
1447: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
144A: 86 08               LDA     #$08                      ; Drop treasure held ...
144C: 0C 11               INC     <$11                      ; {ram:rocksExposed} ... by ...
144E: 7E 0E 80            JMP     $0E80                     ; {DropHeldObj} ... pile of rocks
;
1451: 20 31               BRA     $1484                     ; "NOTHING SPECIAL HAPPENS"
    
; Make sure we have learned the spell. If we have take damage like this:
; VETAR=5*2, MITRA=6*2, OKKAN=7*2, AKHIROM=8*2, NERGAL=9*2, BELROG=10*2,
; CROM=11*2, ISHTAR=12*2
1453: D6 2A               LDB     <$2A                      ; {ram:verbNum} Verb word (spell)
1455: CB D3               ADDB    #$D3                      ; Convert verb word to word list
1457: D7 2B               STB     <$2B                      ; {ram:nounNum} Noun
1459: BD 0E 38            JSR     $0E38                     ; Look for noun in pack
145C: 24 07               BCC     $1465                     ; Dont have it ... out
145E: C0 32               SUBB    #$32                      ; (5 for VETAR)
1460: 58                  ASLB                              ; * 2
1461: BD 1A 2A            JSR     $1A2A                     ; Take damage for using spell
1464: 43                  COMA                              ; C=1
1465: 39                  RTS                               ; Out
```

### AKHIROM 
 Take 16 damage. If SCARAB is in pack, make us invulnerable for 3 minutes. At the 
 end of that if the scarab is in the pack, move it to a random room. So be sure 
 and drop the scarab while you are invulnerable or you'll have to look for it 
 to do it again. Also kill the HYDRA if it is in the room (no SCARAB required).

```code
CommandAKHIROM:
1466: 8D EB               BSR     $1453                     ; Make sure spell has been learned
1468: 24 1A               BCC     $1484                     ; "NOTHING SPECIAL HAPPENS"
146A: 96 33               LDA     <$33                      ; {ram:hydraRoom} Is HYDRA ...
146C: 91 00               CMPA    <$00                      ; {ram:curRoom} ... in current room?
146E: 26 03               BNE     $1473                     ; No ... skip
1470: BD 13 F0            JSR     $13F0                     ; Kill HYDRA
1473: D6 46               LDB     <$46                      ; {ram:akhiromMins} Invulnerability count
1475: 26 0D               BNE     $1484                     ; already invulnerable ... "NOTHING SPECIAL HAPPENS"
1477: C6 15               LDB     #$15                      ; Is the SCARAB ...
1479: BD 18 85            JSR     $1885                     ; {InPack} ... in the pack?
147C: 24 06               BCC     $1484                     ; No ... "NOTHING SPECIAL HAPPENS"
147E: 86 03               LDA     #$03                      ; Invulnerable ...
1480: 97 46               STA     <$46                      ; {ram:akhiromMins} ... for 3 minutes
1482: 20 0F               BRA     $1493                     ; "OK"
1484: 7E 10 1E            JMP     $101E                     ; "NOTHING SPECIAL HAPPENS"
```

### NERGAL 
 Take 18 damage. Allows us to stay in poison room.

```code
CommandNERGAL:     
1487: 8D CA               BSR     $1453                     ; Make sure spell has been learned
1489: 24 F9               BCC     $1484                     ; "NOTHING SPECIAL HAPPENS"
148B: 96 45               LDA     <$45                      ; {ram:fogClock} Poision fog clock running?
148D: 27 F5               BEQ     $1484                     ; "NOTHING SPECIAL HAPPENS"
148F: 0F 32               CLR     <$32                      ; {ram:enteredFog} Clear in-fog-room
1491: 0F 45               CLR     <$45                      ; {ram:fogClock} Clear time in poison fog
1493: 7E 10 17            JMP     $1017                     ; "OK"

```
### BELROG 
 Take 20 damage. Make JUMP from this room without failing.

```code
CommandBELROG:
1496: 8D BB               BSR     $1453                     ; Make sure spell has been learned
1498: 24 EA               BCC     $1484                     ; "NOTHING SPECIAL HAPPENS"
149A: BD 19 9B            JSR     $199B                     ; Get any JUMP information
149D: 4D                  TSTA                              ; Any jump from this room?
149E: 27 E4               BEQ     $1484                     ; No ... "NOTHING SPECIAL HAPPENS"
14A0: A6 43               LDA     3,U                       ; Get jump destination
14A2: 97 00               STA     <$00                      ; {ram:curRoom} Make jump
14A4: 7E 0E 27            JMP     $0E27                     ; Print room description
```

### CROM 
 Take 22 damage. Unblocks all passages. 

```code
CommandCROM: 
14A7: 8D AA               BSR     $1453                     ; Make sure spell has been learned
14A9: 24 D9               BCC     $1484                     ; "NOTHING SPECIAL HAPPENS"
14AB: BD 0F 93            JSR     $0F93                     ; Get room doors for current room
14AE: A6 89 01 00         LDA     $0100,X                   ; Blocks
14B2: A4 84               ANDA    ,X                        ; Any blocks in place?
14B4: 27 CE               BEQ     $1484                     ; No ... "NOTHING SPECIAL HAPPENS"
14B6: 6F 89 01 00         CLR     $0100,X                   ; Remove all blocks
14BA: 8E 34 41            LDX     #$3441                    ; "A BOLT OF LIGHTNING UNBLOCKS THE PASSAGE!!!"
14BD: 7E 10 66            JMP     $1066                     ; {PrintMess} Print the message
```

### ISHTAR 
 Take 24 damage. Move to "exit" point where we drop treasure. This has a limited 
 number of uses (randomized at start to 1-4) so use it wisely.

```code
CommandISHTAR:
14C0: BD 14 53            JSR     $1453                     ; Make sure spell has been learned
14C3: 24 BF               BCC     $1484                     ; "NOTHING SPECIAL HAPPENS"
14C5: 0D 34               TST     <$34                      ; {ram:ishtarUses} Still have an ISHTAR to use?
14C7: 2B BB               BMI     $1484                     ; "NOTHING SPECIAL HAPPENS"
14C9: 0A 34               DEC     <$34                      ; {ram:ishtarUses} One used up
14CB: 86 CA               LDA     #$CA                      ; Move to treasure room 202 ...
14CD: 97 00               STA     <$00                      ; {ram:curRoom} ... "NEAR A GREAT FOREST"
14CF: 97 01               STA     <$01                      ; {ram:lastRoom} Back as well
```

CodeBug3

 All the other leave-room commands reset the MYSTERIOUS FOG counters. This does not.
 If you use ISHTAR to leave the poison fog the count goes on as if you are there.
 
```code
14D1: 7E 10 17            JMP     $1017                     ; "OK"
```

## RUN 
 If the pack weight is greater than 7 then drop the heaviest object. Pick a random number
 of steps (1-9) and take random directions from each room in turn. No handlers or processing
 of the rooms are done of any kind except the final room. In the end we get the description
 of the last room and pick up any spells. 

```code
CommandRUN:  
14D4: BD 07 25            JSR     $0725                     ; Out of the MYSTERIOUS FOG
14D7: 86 07               LDA     #$07                      ; Is pack weight ...
14D9: 91 04               CMPA    <$04                      ; {ram:weight} ... less than 8
14DB: 24 03               BCC     $14E0                     ; Yes ... don't drop anything
14DD: BD 19 FE            JSR     $19FE                     ; Drop the heaviest object in pack
14E0: C6 08               LDB     #$08                      ; Get random value ...
14E2: BD 06 90            JSR     $0690                     ; {RandB} 0-8
14E5: 5C                  INCB                              ; Make it 1-9
14E6: E7 E2               STB     ,-S                       ; Store count
14E8: 96 00               LDA     <$00                      ; {ram:curRoom} Current room
14EA: 1F 89               TFR     A,B                       ; Align parameter
14EC: BD 06 77            JSR     $0677                     ; Get random valid direction
14EF: BD 0F 71            JSR     $0F71                     ; Make move
14F2: 6A E4               DEC     ,S                        ; All steps taken?
14F4: 26 F4               BNE     $14EA                     ; No .. do all
14F6: 97 00               STA     <$00                      ; {ram:curRoom} New current room
14F8: 97 01               STA     <$01                      ; {ram:lastRoom} And last room
14FA: BD 0E 27            JSR     $0E27                     ; Print room description (maybe fall if dark)
14FD: BD 0F E0            JSR     $0FE0                     ; Check for spells again. Not sure why.
1500: 35 82               PULS    A,PC                      ; Out
```

## FILL 

```code
CommandFILL:
1502: 96 2B               LDA     <$2B                      ; {ram:nounNum} Fill ...
1504: 81 A6               CMPA    #$A6                      ; ... LAMP?
1506: 27 10               BEQ     $1518                     ; {FillLamp} Yes ... handle
1508: 81 B8               CMPA    #$B8                      ; Fill BOTTLE?
150A: 27 47               BEQ     $1553                     ; Yes ... handle
150C: 81 A9               CMPA    #$A9                      ; FILL URN?
150E: 10 27 00 7B         LBEQ    $158D                     ; {FillURN} Yes ... handle
;
1512: 8E 2A C0            LDX     #$2AC0                    ; "DON'T BE RIDICULOUS."
1515: 7E 10 66            JMP     $1066                     ; {PrintMess} Print the message
;
FillLamp:
; The lamp can be refilled if it is in the pack or current room. The lamp can be filled from the URN or
; the oil-room. The oil room appears after you know ISHTAR. The URN starts with 4 fills. Either the 
; URN or the lamp can be filled from the oil room. The oil room has a fixed number of refills (4-7).
; After you fill from the oil room it moves to a random room on another floor.
1518: BD 0E 38            JSR     $0E38                     ; Look for noun in pack
151B: 25 07               BCS     $1524                     ; Got it
151D: F6 3D 1D            LDB     $3D1D                     ; LAMP's room
1520: D1 00               CMPB    <$00                      ; {ram:curRoom} In current room?
1522: 26 3B               BNE     $155F                     ; I DO NOT SEE ... and out
1524: B6 3C D7            LDA     $3CD7                     ; Action _v ... the oil room
1527: 91 00               CMPA    <$00                      ; {ram:curRoom} In current room?
1529: 26 09               BNE     $1534                     ; No ... try URN
152B: BD 1C F8            JSR     $1CF8                     ; Can the lamp be refilled?
CodeBug7:
; If you try to fill from the URN in this room and the oil is not visible yet, you will fail.
152E: 27 04               BEQ     $1534                     ; No ... error
1530: 0A 3A               DEC     <$3A                      ; {ram:lampFills} One less refill from oil room
1532: 20 0E               BRA     $1542                     ; Go restore lamp
1534: B6 3D 2B            LDA     $3D2B                     ; URN flags
1537: 2A 51               BPL     $158A                     ; Not in pack ... WITH WHAT
1539: 85 0C               BITA    #$0C                      ; Fill flags
153B: 27 4D               BEQ     $158A                     ; No oil in urn ... WITH WHAT
153D: 80 04               SUBA    #$04                      ; Take one of the 4 refills from the 0000_XX00 bits
153F: B7 3D 2B            STA     $3D2B                     ; New fill status
1542: 8E 07 08            LDX     #$0708                    ; 1800 is 30 minutes
1545: 9F 38               STX     <$38                      ; {ram:lampOil} New oil level
1547: C6 BF               LDB     #$BF                      ; Random number ...
1549: BD 06 90            JSR     $0690                     ; {RandB} 0 to 191
154C: CB 40               ADDB    #$40                      ; 64 to 255
154E: F7 3C D7            STB     $3CD7                     ; Move the oil room to a random room different floor
1551: 20 33               BRA     $1586                     ; OK and out
;
1553: BD 0E 38            JSR     $0E38                     ; Look for noun in pack
1556: 25 0B               BCS     $1563                     ; {FillBottle} Got it
1558: F6 3C FF            LDB     $3CFF                     ; Is bottle in ...
155B: D1 00               CMPB    <$00                      ; {ram:curRoom} ... current room
155D: 27 04               BEQ     $1563                     ; {FillBottle} Yes ... do it
155F: BD 18 E5            JSR     $18E5                     ; I DO NOT SEE ANY
1562: 39                  RTS                               ; Out
;
FillBottle:
; The bottle can be refilled over and over. It has two levels ... filled and empty. There
; are several rooms with water: 0, 74, 16, 17, and 130. Note the missing word from the
; error message here: "THERE IS NO HERE" ... no WATER.
1563: 96 00               LDA     <$00                      ; {ram:curRoom} Our ...current room
1565: 81 00               CMPA    #$00                      ; Room 0?
1567: 27 15               BEQ     $157E                     ; Yes ... has water
1569: 81 4A               CMPA    #$4A                      ; Room 74?
156B: 27 11               BEQ     $157E                     ; Yes ... has water
156D: 81 10               CMPA    #$10                      ; Room 16?
156F: 27 0D               BEQ     $157E                     ; Yes ... has water
1571: 81 11               CMPA    #$11                      ; Room 17?
1573: 27 09               BEQ     $157E                     ; Yes ... has water
1575: 81 82               CMPA    #$82                      ; Room 130?
1577: 27 05               BEQ     $157E                     ; Yes ... has water
1579: C6 11               LDB     #$11                      ; THERE IS NO HERE (message missing a word)
157B: 7E 10 48            JMP     $1048                     ; Print error
;
157E: B6 3D 01            LDA     $3D01                     ; Bottle flags
1581: 8A 0C               ORA     #$0C                      ; Fille up
1583: B7 3D 01            STA     $3D01                     ; New flags
1586: BD 10 17            JSR     $1017                     ; OK
1589: 39                  RTS                               ; Out
158A: 7E 10 25            JMP     $1025                     ; WITH WHAT and out

FillURN:
; The urn must be in the pack to be refilled. The URN holds up to 4 refills
; from the OIL ROOM. The OIL ROOM is initialized with a random number of fills (URN or LAMP). 
; It works out to 4-7 times. When we fill from the OIL ROOM it moves to a random room on
; another floor. If we are in the OIL ROOM and we fill but the URN is full, we get an OK
; but nothing happens (the OIL ROOM stays).
158D: B6 3D 2B            LDA     $3D2B                     ; URN flags
1590: 2A CD               BPL     $155F                     ; Not in pack ... "I DO NOT SEE ANY" and out
1592: F6 3C D7            LDB     $3CD7                     ; Are we in ..
1595: D1 00               CMPB    <$00                      ; {ram:curRoom} ... the oil room
1597: 26 F1               BNE     $158A                     ; No ... WITH WHAT and out
1599: BD 1C F8            JSR     $1CF8                     ; Can we refill the lamp?
159C: 27 EC               BEQ     $158A                     ; No ... WITH WHAT and out
159E: 1F 89               TFR     A,B                       ; Hold flags
15A0: 84 0C               ANDA    #$0C                      ; Is the ...
15A2: 81 0C               CMPA    #$0C                      ; ... URN full?
15A4: 27 E0               BEQ     $1586                     ; Say OK but do nothing
15A6: 0A 3A               DEC     <$3A                      ; {ram:lampFills} Remove one refill from the OIL ROOM
15A8: CB 04               ADDB    #$04                      ; Add one refill to the URN
15AA: F7 3D 2B            STB     $3D2B                     ; New flags
15AD: 20 98               BRA     $1547                     ; Move the OIL ROOM to another floor

LookScarab:
; If we are invulnerable for 3 minutes because of ISHTAR then the SCARAB is glowing.
; At the end of the 3 minutes if the scarab is in the pack it moves to a rancom
; room -- this must be a hint to drop it before then.
15AF: BD 0E 38            JSR     $0E38                     ; Look for noun in pack
15B2: 24 62               BCC     $1616                     ; No ... "LOOK WHAT?"
15B4: 96 46               LDA     <$46                      ; {ram:akhiromMins} Currently invulnerable?
15B6: 27 38               BEQ     $15F0                     ; No ... "I DON'T SEE ANYTING INTERESTING"
15B8: C6 12               LDB     #$12                      ; THE SCARAB IS GLOWING
15BA: 7E 10 48            JMP     $1048                     ; Print and out

LookTablet:
; If we have the tablet in our pack it goes to a random room. If we are in room 19 (ancient
; carvings on the wall) then the ORACLE comes to us. 
15BD: C6 17               LDB     #$17                      ; TABLET
15BF: BD 12 B8            JSR     $12B8                     ; Move to random room if in pack
15C2: 24 52               BCC     $1616                     ; Not in pack ... "LOOK WHAT?" and out
15C4: D6 00               LDB     <$00                      ; {ram:curRoom} Current room
15C6: C1 13               CMPB    #$13                      ; Are we in room 19?
15C8: 26 26               BNE     $15F0                     ; No ... I DON'T SEE ANYTHING INTERESTING
15CA: F7 3D 56            STB     $3D56                     ; Bring the ORACLE to this room
15CD: 39                  RTS                               ; Out
```

## LOOK 

```code
CommandLOOK:
15CE: 96 2B               LDA     <$2B                      ; {ram:nounNum} Noun
15D0: 81 C4               CMPA    #$C4                      ; TABLET?
15D2: 27 E9               BEQ     $15BD                     ; {LookTablet} Yes ... go handle tablet
15D4: 81 C7               CMPA    #$C7                      ; SCARAB?
15D6: 27 D7               BEQ     $15AF                     ; {LookScarab} Yes ... go handle scarab
15D8: 81 2C               CMPA    #$2C                      ; POOL?
15DA: 27 1A               BEQ     $15F6                     ; {LookPool} Yes ... go handle pool
15DC: 81 A9               CMPA    #$A9                      ; URN?
15DE: 27 5B               BEQ     $163B                     ; {LookUrn} Yes ... go handle urn
15E0: 81 6D               CMPA    #$6D                      ; PIT?
15E2: 27 40               BEQ     $1624                     ; {LookPit} Yes ... go handle pit
15E4: 81 B8               CMPA    #$B8                      ; BOTTLE?
15E6: 27 72               BEQ     $165A                     ; {LookBottle} Yes ... go handle bottle
15E8: 81 FF               CMPA    #$FF                      ; Nothing?
15EA: 27 07               BEQ     $15F3                     ; Yes ... just print room description
15EC: 81 A7               CMPA    #$A7                      ; PARCHMENT?
15EE: 27 29               BEQ     $1619                     ; {LookParchment} Yes ... go handle parchment
15F0: 7E 10 10            JMP     $1010                     ; I DON'T SEE ANYTHING INTERESTING
;
15F3: 7E 0E 27            JMP     $0E27                     ; Reprint room and out
 
LookPool:
; If we look into the pool in room 0 we see the instructions for getting the SPELLBOOK.
; The oracle doesn't give info on the SPELLBOOK ... this completes all we need to know. 
15F6: 0D 00               TST     <$00                      ; {ram:curRoom} In room 0 (pool of water)
15F8: 26 F6               BNE     $15F0                     ; No ... "I DON'T SEE ANYTHING INTERESTING".
15FA: 8E 2C C1            LDX     #$2CC1                    ; "IN A REFLECTION IN THE POOL YOU CAN READ THE FOLLOWING WORDS ON THE CEILING..."
15FD: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
1600: 8E 2C A7            LDX     #$2CA7                    ; "TO LEARN THE SECRET OF THE"
1603: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
1606: C6 23               LDB     #$23                      ; Print ...
1608: BD 18 6D            JSR     $186D                     ; ... "SPELLBOOK"
160B: 8E 2B FC            LDX     #$2BFC                    ; "YOU MUST POSSESS THE"
160E: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
1611: C6 0D               LDB     #$0D                      ; Spell book object in managed-lists
1613: 7E 12 20            JMP     $1220                     ; Print required-object list for object D (spell book)
;
1616: 7E 10 99            JMP     $1099                     ; {ComWHAT} Command+" WHAT?"

LookParchment:
; If we have the parchment we see it has a musical score on it.
1619: BD 0E 38            JSR     $0E38                     ; Look for parchment in pack
161C: 24 F8               BCC     $1616                     ; Not there ... "LOOK WHAT?"
161E: 8E 34 21            LDX     #$3421                    ; "THE PARCHMENT HAS A SCORE ON IT."
1621: 7E 10 66            JMP     $1066                     ; {PrintMess} Print the message

LookPit:
; We have to be able to see. Then 1/2 the time the treasure held by the pit will
; appear. Be persistent ... it may take a few LOOKs to get the treasure.
1624: BD 0D 8B            JSR     $0D8B                     ; Can we see?
1627: 24 2F               BCC     $1658                     ; No ...
1629: 96 00               LDA     <$00                      ; {ram:curRoom} Current room
162B: 91 35               CMPA    <$35                      ; {ram:smallPitRoom} Is the PIT in this room?
162D: 26 26               BNE     $1655                     ; No ... nothing interesting
162F: BD 06 61            JSR     $0661                     ; {Random} Random
1632: C1 80               CMPB    #$80                      ; We see it ...
1634: 24 1F               BCC     $1655                     ; ... 1/2 the time
1636: 86 05               LDA     #$05                      ; Drop object held by the pit ...
1638: 7E 0E 80            JMP     $0E80                     ; {DropHeldObj} ... and out

LookUrn:
; If the urn is in the pack or room we can see if there is oil in it.
163B: BD 0E 38            JSR     $0E38                     ; Is urn in pack?
163E: 25 07               BCS     $1647                     ; Yes .. handle
1640: B6 3D 29            LDA     $3D29                     ; Urn in ...
1643: 91 00               CMPA    <$00                      ; {ram:curRoom} ... current room
1645: 26 CF               BNE     $1616                     ; No ... "LOOK WHAT?" and out
1647: BD 1A 5A            JSR     $1A5A                     ; {GetObject} Get object data
164A: A6 02               LDA     2,X                       ; Get flags
164C: 84 0C               ANDA    #$0C                      ; Any oil in it?
164E: 27 1E               BEQ     $166E                     ; No ... THERE IS NOTHING IN URN
1650: C6 09               LDB     #$09                      ; THE URN IS FILLED WITH OIL
1652: 7E 10 48            JMP     $1048                     ; Print and out
1655: 7E 10 10            JMP     $1010                     ; "I DON'T SEE ANYTHING INTERESTING."

1658: 20 1D               BRA     $1677                     ; Print "YOU CAN NOT SEE IN THE DIM LIGHT" and out

LookBottle:
; If the bottle is in the pack (not room) we can see if there is water in it.
165A: BD 0E 38            JSR     $0E38                     ; Is in pack?
165D: 24 B7               BCC     $1616                     ; No ... "LOOK WHAT?" and out
165F: BD 1A 5A            JSR     $1A5A                     ; {GetObject} Get object data
1662: A6 02               LDA     2,X                       ; Get flags
1664: 84 0C               ANDA    #$0C                      ; Any water in it?
1666: 26 03               BNE     $166B                     ; Yes ... THE BOTTLE IS FILLED WITH WATER
1668: C6 0B               LDB     #$0B                      ; THE BOTTLE IS EMPTY
166A: 8C C6 0C            CMPX    #$C60C                    ; THE BOTTLE IS FILLED WITH WATER
166D: 8C C6 08            CMPX    #$C608                    ; THERE IS NOTHING IN URN
1670: 20 E0               BRA     $1652                     ; Do message

; This helper function prints the status of the urn. It is not called from
; anyhwere.
1672: B6 3D 2B            LDA     $3D2B                     ; Get URN flags
1675: 20 D5               BRA     $164C                     ; Print urn status

1677: C6 0D               LDB     #$0D                      ; "YOU CAN NOT SEE IN THE DIM LIGHT."
1679: 20 D7               BRA     $1652                     ; Print and out

```
## PLAY 
 We can play the flute anytime without error. But if we are in the room with action_e and
 we have the parchment then the LEDGE appears. (The LEDGE holds a treasure).

```code
CommandPLAY: 
167B: 96 2B               LDA     <$2B                      ; {ram:nounNum} Get noun
167D: 81 24               CMPA    #$24                      ; FLUTE?
167F: 10 26 01 10         LBNE    $1793                     ; No ... DON'T BE REDICULOUS
1683: BD 0E 38            JSR     $0E38                     ; Is in pack?
1686: 25 03               BCS     $168B                     ; Yes ... handle it
1688: 7E 10 99            JMP     $1099                     ; {ComWHAT} "PLAY WHAT?"
168B: BD 0B 3E            JSR     $0B3E                     ; Sound effect
168E: C6 0E               LDB     #$0E                      ; Parchment
1690: BD 18 85            JSR     $1885                     ; {InPack} Is it in pack?
1693: 24 0F               BCC     $16A4                     ; No ... just toot along
1695: 96 00               LDA     <$00                      ; {ram:curRoom} Current room
1697: B1 3C 9B            CMPA    $3C9B                     ; action _e room ?
169A: 26 08               BNE     $16A4                     ; No ... just toot along
169C: 97 36               STA     <$36                      ; {ram:ledgeRoom} Bring the LEDGE here
169E: 8E 2F 95            LDX     #$2F95                    ; "BY PLAYING THE FLUTE ACCORDING TO A SONG ON THE PARCHMENT, A SECRET LEDGE HAS BEEN EXPOSED."
16A1: 7E 10 66            JMP     $1066                     ; {PrintMess} Print message and return
16A4: 7E 10 17            JMP     $1017                     ; OK (not really an error .. we can toot along anytime)

CalculateScore:
; Calculate score
; The score goes like this. There are 8 spells. We get 10 points for learning each.
; There are 16 treasures. We get 5 points if in pack OR 10 points if at entrance.
; 8*10 + 16*10 = 240 points max.
;
; The catch is that the treasure must be on the ground outside to get full credit.
;
16A7: 34 10               PSHS    X                         ; Save params
16A9: 0F 28               CLR     <$28                      ; {ram:score} Score tally
16AB: 8E 3B BD            LDX     #$3BBD                    ; Spell data
16AE: C6 08               LDB     #$08                      ; Eight spells
16B0: 30 04               LEAX    4,X                       ; Skip to next spell
16B2: A6 03               LDA     3,X                       ; Skip if not ...
16B4: 2A 06               BPL     $16BC                     ; ... learned
16B6: 96 28               LDA     <$28                      ; {ram:score} Score tally
16B8: 8B 0A               ADDA    #$0A                      ; +10 for learned spells (up to 8)
16BA: 97 28               STA     <$28                      ; {ram:score} New score
16BC: 5A                  DECB                              ; All done?
16BD: 26 F1               BNE     $16B0                     ; No ... check all spells
;
16BF: 8E 3D 56            LDX     #$3D56                    ; Treasure table
16C2: C6 10               LDB     #$10                      ; 16 treasures
16C4: 30 03               LEAX    3,X                       ; Next treasure
16C6: A6 02               LDA     2,X         
16C8: 85 03               BITA    #$03        
16CA: 26 27               BNE     $16F3                     ; No ... skip it completely
16CC: 4D                  TSTA                              ; Is this in backpack?
16CD: 2A 06               BPL     $16D5                     ; No .... maybe in the forrest?
16CF: 96 28               LDA     <$28                      ; {ram:score} Score tally
16D1: 8B 05               ADDA    #$05                      ; +5 for holding treasure (up to 16)
16D3: 20 0A               BRA     $16DF                     ; Check for win (can't be if holding ... why check?)
16D5: A6 84               LDA     ,X                        ; Get location
;
; Note ... treasure must be on the ground for full 10 points!
;
16D7: 81 CA               CMPA    #$CA                      ; Outside in forest?
16D9: 26 18               BNE     $16F3                     ; No ... skip
16DB: 96 28               LDA     <$28                      ; {ram:score} Score tally
16DD: 8B 0A               ADDA    #$0A                      ; +10 for treasures at entrance (up to 16)
16DF: 81 F0               CMPA    #$F0                      ; Reached 240?
16E1: 25 0E               BCS     $16F1                     ; Less than ... keep going

Win:
16E3: BD A9 28            JSR     $A928                     ; {hard:CLRSCREEN} Clear screen (BASIC)
16E6: 8E 33 FF            LDX     #$33FF                    ; "CONGRATULATIONS!!! YOU WIN!"
16E9: 8D B6               BSR     $16A1                     ; Short way to JSR PrintMessage
16EB: BD 0B 3E            JSR     $0B3E                     ; Sound effect
16EE: 7E 0D 65            JMP     $0D65                     ; Blink cursor and wait for key and start game again
16F1: 97 28               STA     <$28                      ; {ram:score} Score tally
16F3: 5A                  DECB                              ; All checked?
16F4: 26 CE               BNE     $16C4                     ; No ... back for more
16F6: 35 90               PULS    X,PC                      ; Done
```

## SCORE 

```code
CommandSCORE:
16F8: 34 10               PSHS    X                         ; Save parameters
16FA: 8D AB               BSR     $16A7                     ; {CalculateScore} Calculate score
16FC: 8E 2D 27            LDX     #$2D27                    ; "YOU HAVE SCORED"
16FF: BD 10 66            JSR     $1066                     ; {PrintMess} Print message
1702: D6 28               LDB     <$28                      ; {ram:score} Score
1704: 8D 0F               BSR     $1715                     ; Print number
1706: 8E 2D 36            LDX     #$2D36                    ; " POINTS OUT OF A TOTAL OF 240 POINTS. PHYS COND = "
1709: BD 10 66            JSR     $1066                     ; {PrintMess} Print message
170C: D6 05               LDB     <$05                      ; {ram:condition} Physical condition
170E: 8D 05               BSR     $1715                     ; Print number
1710: BD 10 90            JSR     $1090                     ; {PrintCR} Print CR
1713: 35 90               PULS    X,PC                      ; Done

; Convert number in B to string and print
1715: 34 16               PSHS    X,B,A                     ; Save params
1717: 4F                  CLRA                              ; MSB 0
1718: 6F E2               CLR     ,-S                       ; End of message marker on stack
171A: 8E FF FF            LDX     #$FFFF                    ; -1
171D: 83 00 0A            SUBD    #$000A                    ; Count ...
1720: 30 01               LEAX    1,X                       ; ... next ...
1722: 24 F9               BCC     $171D                     ; ... digit
1724: 34 04               PSHS    B                         ; Save converted digit
1726: 1F 10               TFR     X,D                       ; Continue ...
1728: 26 F0               BNE     $171A                     ; ... until 0
172A: A6 E0               LDA     ,S+                       ; Next in messaage
172C: 27 07               BEQ     $1735                     ; Yes ... out
172E: 8B 3A               ADDA    #$3A                      ; Offset from screen character '0'
1730: BD 06 00            JSR     $0600                     ; {PrintWrap} Print character
1733: 20 F5               BRA     $172A                     ; Keep going
1735: 35 96               PULS    A,B,X,PC                  ; Done

; Tape I/O error
; Vectored here by ROM ... ON ERROR GOTO COMMAND
; This is the QUIET command.
1737: C0 20               SUBB    #$20                      ; Should be inverse H (IO error) or other
1739: F7 04 1F            STB     $041F                     ; Upper right corner of screen
173C: BD A7 EB            JSR     $A7EB                     ; CASOFF ... Motor off (BASIC)
```

## QUIET 
 Remember ... interrupts are only turned on during regular user input. They are off now.
 This allows us to just pause the game or SAVE or LOAD.

```code
CommandQUIET:
173F: BD A1 B1            JSR     $A1B1                     ; Blink cursor and wait for keystroke (BASIC)
1742: 10 CE 02 37         LDS     #$0237                    ; Need to relocate stack while we work with the area
1746: 0F 78               CLR     <$78                      ; {ram:m67} File status: CLOSED
1748: 81 57               CMPA    #$57                      ; 'W'
174A: 27 1B               BEQ     $1767                     ; 'W' ... return to game loop
174C: 81 21               CMPA    #$21                      ; '!' ...
174E: 27 1A               BEQ     $176A                     ; ... Save engine state to tape
1750: 81 29               CMPA    #$29                      ; ' ')' ... reload game data
1752: 26 EB               BNE     $173F                     ; {CommandQUIET} Unknown action ... go back and get a valid one
;
; Load
1754: BD A5 00            JSR     $A500                     ; CLOADM Load engine state (BASIC)
1757: BD A5 00            JSR     $A500                     ; CLOADM Load game state (BASIC)
175A: 8E 02 40            LDX     #$0240                    ; Restore 1st 256 bytes
175D: DE 8A               LDU     <$8A                      ; {ram:zeroWord} PV DUMMY - THESE TWO BYTES ARE ALWAYS ZERO
175F: 5F                  CLRB                              ; Move ...
1760: A6 80               LDA     ,X+                       ; ... 256 ...
1762: A7 C0               STA     ,U+                       ; ... bytes ...
1764: 5A                  DECB                              ; ... from 240 to ...
1765: 26 F9               BNE     $1760                     ; ... 0
1767: 7E 0D 36            JMP     $0D36                     ; {MainGameLoop} Continue near top of game loop
;
; Save
176A: 8E 02 40            LDX     #$0240                    ; Engine state
176D: 5F                  CLRB                              ; Move ...
176E: DE 8A               LDU     <$8A                      ; {ram:zeroWord} ... 256 ...
1770: A6 C0               LDA     ,U+                       ; ... bytes ...
1772: A7 80               STA     ,X+                       ; ... from ....
1774: 5A                  DECB                              ; 0 to ...
1775: 26 F9               BNE     $1770                     ; ... 240
1777: BD 01 1D            JSR     $011D                     ;  Write to tape (two files ... engine state and game state)
177A: 20 EB               BRA     $1767                     ; Continue near top of game loop
```

## KILL 

```code
CommandKILL:
177C: 96 2B               LDA     <$2B                      ; {ram:nounNum} Noun
177E: 81 FC               CMPA    #$FC                      ; "HYDRA?"
1780: 27 3D               BEQ     $17BF                     ; {KillHydra} Yes ... go attack HYDRA
1782: BD 18 CD            JSR     $18CD                     ; Noun to object number
1785: 24 11               BCC     $1798                     ; Not an object ... "KILL WHAT?" and out
1787: 81 1E               CMPA    #$1E                      ; Higher than "MINOTAUR"?
1789: 22 04               BHI     $178F                     ; Yes ... invalid
178B: 81 19               CMPA    #$19                      ; Lower than "SPRITE" ?
178D: 24 0C               BCC     $179B                     ; {KillCreature} No ... something to attack
;
178F: 81 1F               CMPA    #$1F                      ; Killing the "ORACLE"?
1791: 27 1B               BEQ     $17AE                     ; {CodeBug2} Yes ... error message (code bug)
1793: 8E 2A C0            LDX     #$2AC0                    ; "DON'T BE RIDICULOUS."
1796: 20 40               BRA     $17D8                     ; Print and out
1798: 7E 10 99            JMP     $1099                     ; {ComWHAT} "KILL WHAT?" and out

KillCreature:
; Every creature has a combination of objects you need to kill. If you don't have that
; combo you take 50 damage and miss. Otherwise the creature dies and drops its
; treasure.
179B: BD 09 43            JSR     $0943                     ; {IsObjInRoom} Is creature in room?
179E: 24 F8               BCC     $1798                     ; No ... "KILL WHAT?" and out
17A0: BD 0A 0D            JSR     $0A0D                     ; Creature visible?
17A3: 24 F3               BCC     $1798                     ; No ... "KILL WHAT?" and out
17A5: 8D 7F               BSR     $1826                     ; Check required items to kill
17A7: 24 27               BCC     $17D0                     ; Didn't have the combo ... 50 from phys, YOU MISSED and out
17A9: BD 0B 3E            JSR     $0B3E                     ; Play sound effect
17AC: 20 2D               BRA     $17DB                     ; Kill the creature
       
CodeBug2:
; Trying to kill oracle 
; If the Oracle is in the room and you try and kill it, you get
; 9:"THE URN IS FILLED WITH OIL." instead of 7:".. ORACLE DISAPPEARS."
17AE: BD 09 43            JSR     $0943                     ; {IsObjInRoom} Is oracle in this room?
17B1: 24 E5               BCC     $1798                     ; No ... "KILL WHAT?" and out
17B3: C6 09               LDB     #$09                      ; "THE URN IS FILLED WITH OIL". ?What?
17B5: BD 10 48            JSR     $1048                     ; Print message
17B8: BD 06 61            JSR     $0661                     ; {Random} Random number
17BB: F7 3D 56            STB     $3D56                     ; Oracles new room
17BE: 39                  RTS                               ; Done

KillHydra:
; You kill the HYDRA by stabbing it with the sword or dagger. Killing it here just lopps
; off a head and it grows back. Note the HYDRA must be in this room which means it was
; previously tied up with the rope.
17BF: 96 0E               LDA     <$0E                      ; {ram:hydraStatus} Is HYDRA ...
17C1: 81 01               CMPA    #$01                      ; ... status: dead?
17C3: 27 D3               BEQ     $1798                     ; Yes ... "KILL WHAT?" and out
17C5: 96 33               LDA     <$33                      ; {ram:hydraRoom} Is Hydra in ...
17C7: 91 00               CMPA    <$00                      ; {ram:curRoom} ... current room?
17C9: 26 CD               BNE     $1798                     ; No ... "KILL WHAT?" and out
17CB: 8E 30 8C            LDX     #$308C                    ; "ONE OF THE HYDRA'S HEADS IS LOPPED OFF, BUT ANOTHER ONE TAKES ITS PLACE AND SNEERS AT YOU."
17CE: 20 08               BRA     $17D8                     ; Print message and out

17D0: 86 32               LDA     #$32                      ; Takes 50 from physical condition to not-kill
17D2: BD 1A 2F            JSR     $1A2F                     ; Adjust physical condition
17D5: 8E 2E 11            LDX     #$2E11                    ; "YOU MISSED."
17D8: 7E 10 66            JMP     $1066                     ; {PrintMess} Print the message

17DB: 34 16               PSHS    X,B,A                     ; Save params
17DD: 8E 3C 6F            LDX     #$3C6F                    ; Random object translation
17E0: C6 10               LDB     #$10                      ; 16 to check
17E2: A6 81               LDA     ,X++                      ; Get holder
17E4: A1 E4               CMPA    ,S                        ; Is this us?
17E6: 27 08               BEQ     $17F0                     ; Yes ...
17E8: 5A                  DECB                              ; All done?
17E9: 26 F7               BNE     $17E2                     ; No ... keep looking
17EB: BD 10 1E            JSR     $101E                     ; Nothing special happens
17EE: 35 96               PULS    A,B,X,PC                  ; Done
 
17F0: E6 1F               LDB     -1,X                      ; Object number
17F2: D7 52               STB     <$52                      ; {ram:m52} Hold for now
17F4: BD 1A 5A            JSR     $1A5A                     ; {GetObject} Get descriptor for object
17F7: A6 02               LDA     2,X                       ; Flags
17F9: 84 7C               ANDA    #$7C                      ; Not pack, not invisible
17FB: A7 02               STA     2,X                       ; Set flags
17FD: D6 00               LDB     <$00                      ; {ram:curRoom} Current room
17FF: BD 06 77            JSR     $0677                     ; Random valid direction
1802: 96 00               LDA     <$00                      ; {ram:curRoom} Current room
1804: BD 0F 71            JSR     $0F71                     ; Calculate target room
1807: A7 84               STA     ,X                        ; Object thrown to here
1809: 8E 2D A9            LDX     #$2DA9                    ; "IN HIS DYING EFFORT THE"
180C: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
180F: E6 E4               LDB     ,S                        ; Print name ...
1811: BD 18 6D            JSR     $186D                     ; ... of the creature
1814: 8E 2D C0            LDX     #$2DC0                    ; "PULLS THE"
1817: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
181A: D6 52               LDB     <$52                      ; {ram:m52} Print name of ...
181C: 8D 4F               BSR     $186D                     ; ... object
181E: 8E 2D C9            LDX     #$2DC9                    ; "FROM A BAG AND THROWS IT BEFORE HE DISAPPEARS IN A PUFF OF PURPLE SMOKE."
1821: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
1824: 20 C8               BRA     $17EE                     ; Done

; Check the list of objects required to kill the creature. If they are all in the backpack,
; kill the creature.
; C=1 if creature killed
; C=0 if failed
1826: 34 36               PSHS    Y,X,B,A                   ; Save params
1828: BD 1A DD            JSR     $1ADD                     ; Get list of things for protected item
182B: 24 0C               BCC     $1839                     ; No list
182D: E6 A0               LDB     ,Y+                       ; Object from list
182F: C1 FF               CMPB    #$FF                      ; End of list?
1831: 27 09               BEQ     $183C                     ; Yes ... finish
1833: C4 3F               ANDB    #$3F                      ; Make sure it is a valid object
1835: 8D 4E               BSR     $1885                     ; {InPack} Is it in backpack?
1837: 25 F4               BCS     $182D                     ; Yes ... keep checking
1839: 5F                  CLRB                              ; C=0 (failed)
183A: 20 0C               BRA     $1848                     ; Out
183C: E6 E4               LDB     ,S                        ; Object
183E: BD 1A 5A            JSR     $1A5A                     ; {GetObject} Find object
1841: E6 02               LDB     2,X                       ; Set ...
1843: CA 02               ORB     #$02                      ; ... bit ...
1845: E7 02               STB     2,X                       ; ... 1 in flags
1847: 53                  COMB                              ; C=1
1848: 35 B6               PULS    A,B,X,Y,PC                ; Done
```

## INV(inventory)
 Print what we have in our pack.

```code
CommandINV:
184A: 8E 2A 9B            LDX     #$2A9B                    ; "YOU ARE HOLDING:"
184D: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
1850: 0F 31               CLR     <$31                      ; {ram:m31} Nothing in pack so far
1852: C6 FF               LDB     #$FF                      ; Start with 0
1854: 5C                  INCB                              ; Next object number
1855: C1 3F               CMPB    #$3F                      ; All done?
1857: 24 08               BCC     $1861                     ; Yes ... out
1859: 8D 2A               BSR     $1885                     ; {InPack} Check for word in pack
185B: 24 F7               BCC     $1854                     ; Not in pack ... skip
185D: 8D 0E               BSR     $186D                     ; Print object name
185F: 20 F3               BRA     $1854                     ; Next object
1861: 96 31               LDA     <$31                      ; {ram:m31} Did we find at least one?
1863: 26 05               BNE     $186A                     ; Yes ... skip "nothing"
1865: 86 93               LDA     #$93                      ; "NOTHING"
1867: BD 10 54            JSR     $1054                     ; {PrintWord} Print word
186A: 7E 10 90            JMP     $1090                     ; {PrintCR} CR and out
  
; Print object name
186D: 34 16               PSHS    X,B,A                     ; Save params
186F: C1 3F               CMPB    #$3F                      ; Valid object
1871: 23 08               BLS     $187B                     ; Yes ... print it
1873: 8E 2A 7C            LDX     #$2A7C                    ; No ... "ERROR"
1876: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
1879: 20 08               BRA     $1883                     ; Out
;       
187B: 8E 35 08            LDX     #$3508                    ; Noun-to-word table
187E: A6 85               LDA     B,X                       ; Get word
1880: BD 10 54            JSR     $1054                     ; {PrintWord} Print object name
1883: 35 96               PULS    A,B,X,PC                  ; Done

InPack:
; Look for object described by word B in the backpack.
; Return C=0 if not found
; Return C=1 if found
1885: 34 16               PSHS    X,B,A                     ; Sava parameters
1887: 0F 2F               CLR     <$2F                      ; {ram:temporary} Strange ...
1889: 0F 30               CLR     <$30                      ; {ram:m30} ... flagging
188B: 8E 3C F9            LDX     #$3CF9                    ; Object data
188E: 30 03               LEAX    3,X                       ; Next object
1890: A6 02               LDA     2,X                       ; Flags
1892: 2A 0E               BPL     $18A2                     ; Object not in pack ... next word
1894: A6 61               LDA     1,S                       ; Is this ...
1896: A1 01               CMPA    1,X                       ; ... our object word?
1898: 26 0A               BNE     $18A4                     ; No ... next word
189A: 0C 31               INC     <$31                      ; {ram:m31} Flag found object (increment if counting)
189C: DC 2F               LDD     <$2F                      ; {ram:temporary} Strange ...
189E: E3 02               ADDD    2,X                       ; ... way ...
18A0: DD 2F               STD     <$2F                      ; {ram:temporary} ... to flag things
18A2: A6 01               LDA     1,X                       ; Description
18A4: 81 FF               CMPA    #$FF                      ; End of list marker?
18A6: 26 E6               BNE     $188E                     ; No ... keep looking
18A8: DC 2F               LDD     <$2F                      ; {ram:temporary} Did we find the object?
18AA: 27 03               BEQ     $18AF                     ; Yes ... Z=1
18AC: 43                  COMA                              ; C=1... found
18AD: 20 01               BRA     $18B0                     ; Out
18AF: 4F                  CLRA                              ; C=0 ... not found
18B0: 35 96               PULS    A,B,X,PC                  ; Out

; Look for object matching Room=B, Word=A
; C=0 if found
; C=1 if not found
18B2: 8E 3C F9            LDX     #$3CF9                    ; Object data
18B5: 30 03               LEAX    3,X                       ; Next object
18B7: E1 84               CMPB    ,X                        ; Room matches B?
18B9: 26 06               BNE     $18C1                     ; No ... next
18BB: A1 01               CMPA    1,X                       ; Word matches A?
18BD: 26 02               BNE     $18C1                     ; No next
18BF: 4F                  CLRA                              ; C=0 ... found
18C0: 39                  RTS                               ; Done
;             
18C1: 34 02               PSHS    A                         ; Hold A
18C3: A6 01               LDA     1,X                       ; End of ...
18C5: 81 FF               CMPA    #$FF                      ; ... list?
18C7: 35 02               PULS    A                         ; Restore A
18C9: 26 EA               BNE     $18B5                     ; No ... keep looking
18CB: 43                  COMA                              ; C=1 ... not found
18CC: 39                  RTS                               ; Done
     
; Convert noun to object number      
18CD: 34 10               PSHS    X                         ; Save params
18CF: 8E 35 08            LDX     #$3508                    ; Noun-to-object map
18D2: 86 FF               LDA     #$FF                      ; First is 0
18D4: 4C                  INCA                              ; Next object number
18D5: E6 80               LDB     ,X+                       ; Get noun number
18D7: 27 09               BEQ     $18E2                     ; End of map ... error and out
18D9: D1 2B               CMPB    <$2B                      ; {ram:nounNum} Is this our word?
18DB: 26 F7               BNE     $18D4                     ; No keep looking
18DD: 97 07               STA     <$07                      ; {ram:nounObjNum} Yes ... hold object number
18DF: 53                  COMB                              ; Z=0
18E0: 35 90               PULS    X,PC                      ; Done
18E2: 5F                  CLRB                              ; Z=1
18E3: 20 FB               BRA     $18E0                     ; Out

; Print "I DO NOT SEE ANY "+valid noun word.
18E5: 34 10               PSHS    X                         ; Save params
18E7: 8E 2A 49            LDX     #$2A49                    ; "I DO NOT SEE ANY"
18EA: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
18ED: 96 2B               LDA     <$2B                      ; {ram:nounNum} Nound word
18EF: BD 10 54            JSR     $1054                     ; {PrintWord} Print word
18F2: BD 10 90            JSR     $1090                     ; {PrintCR} Print CR
18F5: 35 90               PULS    X,PC                      ; Out
```
 
## GET 
 Get and Take and Grab. If the object is protected, you must have the right combination
 of items. If the object+packWeight is too bulky or too heavy then you can't carry it.

```code
CommandGETTAKEGRAB:
18F7: 34 10               PSHS    X                         ; Save params
18F9: 96 2B               LDA     <$2B                      ; {ram:nounNum} Nound word
18FB: 81 FF               CMPA    #$FF                      ; If there is a noun ...
18FD: 26 05               BNE     $1904                     ; ... go handle it
18FF: BD 10 99            JSR     $1099                     ; {ComWHAT} Command+what ... "GET WHAT?"
1902: 20 7C               BRA     $1980                     ; Out
     
1904: 8D C7               BSR     $18CD                     ; Convert noun to object number
1906: 24 7F               BCC     $1987                     ; Invalid word ... DON'T BE REDICULOUS
1908: D6 00               LDB     <$00                      ; {ram:curRoom} Current room
190A: 8D A6               BSR     $18B2                     ; Look for object B=room, A=word (no flags check)
190C: 24 04               BCC     $1912                     ; Found it ... handle it
;
190E: 8D D5               BSR     $18E5                     ; "I DO NOT SEE ANY "+word
1910: 20 6E               BRA     $1980                     ; Done
;
1912: A6 02               LDA     2,X                       ; Flags
1914: 2B 71               BMI     $1987                     ; Already got it ... "DON'T BE REDICULOUS" and out
1916: 85 40               BITA    #$40                      ; Spell or creature?
1918: 26 6D               BNE     $1987                     ; Yes ... print "DON'T BE REDICULOUS" and out
191A: 85 01               BITA    #$01                      ; Object being carried by something (creature or room action)?
191C: 26 F0               BNE     $190E                     ; Yes ... print "I DO NOT SEE ANY "+word and out
191E: 85 02               BITA    #$02                      ; Spell or dead creature?
1920: 26 EC               BNE     $190E                     ; Yes ... print "I DO NOT SEE ANY "+word and out
1922: 85 10               BITA    #$10                      ; Protected?
1924: 27 21               BEQ     $1947                     ; No ... we can do it
1926: 96 07               LDA     <$07                      ; {ram:nounObjNum} Object number
1928: BD 1A DD            JSR     $1ADD                     ; Get list of required objects
192B: 24 1A               BCC     $1947                     ; There are none ... get it
192D: E6 A0               LDB     ,Y+                       ; Next required object
192F: C1 FF               CMPB    #$FF                      ; End of list?
1931: 27 14               BEQ     $1947                     ; Yes ... we can do it
1933: C4 3F               ANDB    #$3F                      ; Mask off for safety
1935: BD 18 85            JSR     $1885                     ; {InPack} Object in pack?
1938: 25 F3               BCS     $192D                     ; Yes ... check them all
193A: 8E 20 74            LDX     #$2074                    ; Protected messages
193D: D6 07               LDB     <$07                      ; {ram:nounObjNum} Object number
193F: BD 0E 52            JSR     $0E52                     ; Get message for protection
1942: BD 10 2F            JSR     $102F                     ; {PrintPacked} Print protection phrase
1945: 20 39               BRA     $1980                     ; Out
     
1947: 8D 43               BSR     $198C                     ; Get object weight/buld
1949: 96 04               LDA     <$04                      ; {ram:weight} Current weight
194B: AB A4               ADDA    ,Y                        ; Add object weight
194D: 25 33               BCS     $1982                     ; Over 255 is "TOO HEAVY"
194F: 91 05               CMPA    <$05                      ; {ram:condition} Physical condition
1951: 22 2F               BHI     $1982                     ; Not strong enough to carry it
1953: D6 06               LDB     <$06                      ; {ram:bulk} Bulk
1955: EB 21               ADDB    1,Y                       ; Add object bulk
1957: 25 04               BCS     $195D                     ; Over 255 is "TOO BULKY"
1959: D1 05               CMPB    <$05                      ; {ram:condition} Physical condition
195B: 23 05               BLS     $1962                     ; OK
;
195D: 8E 2A 59            LDX     #$2A59                    ; "IT'S TOO BULKY."
1960: 20 1B               BRA     $197D                     ; Print message and out
;
1962: 97 2F               STA     <$2F                      ; {ram:temporary} Hold weight
1964: A6 02               LDA     2,X                       ; Flags
1966: 85 40               BITA    #$40                      ; Spells, creatures, protected things?
1968: 26 1D               BNE     $1987                     ; "DON'T BE REDICULOUS."
196A: 85 10               BITA    #$10                      ; Protected?
196C: 27 02               BEQ     $1970                     ; No ... skip
196E: 84 EF               ANDA    #$EF                      ; Turn off protection
1970: 8A 80               ORA     #$80                      ; Now in pack
1972: A7 02               STA     2,X                       ; New flags
1974: 96 2F               LDA     <$2F                      ; {ram:temporary} New weight
1976: 97 04               STA     <$04                      ; {ram:weight} Store new weight
1978: D7 06               STB     <$06                      ; {ram:bulk} Store new bulk
197A: 8E 2A 79            LDX     #$2A79                    ; "OK"
197D: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
1980: 35 90               PULS    X,PC                      ; Done

1982: 8E 2A 69            LDX     #$2A69                    ; "IT'S TOO HEAVY."
1985: 20 F6               BRA     $197D                     ; Print message and out
       
1987: 8E 2A C0            LDX     #$2AC0                    ; "DON'T BE RIDICULOUS."
198A: 20 F1               BRA     $197D                     ; Print message and out

; Y points to weight/bulk for object number in $07
198C: 34 06               PSHS    B,A                       ; Save params
198E: 96 07               LDA     <$07                      ; {ram:nounObjNum} Object number
1990: C6 02               LDB     #$02                      ; Two byes ...
1992: 3D                  MUL                               ; ... per entry
1993: 10 8E 35 48         LDY     #$3548                    ; Weight/bulk
1997: 31 AB               LEAY    D,Y                       ; Point Y
1999: 35 86               PULS    A,B,PC                    ; Out
    
; Find jump-info entry for current room.
199B: CE 3B DC            LDU     #$3BDC                    ; Jump info table
199E: 33 45               LEAU    5,U                       ; Next entry
19A0: A6 C4               LDA     ,U                        ; Get "from" room
19A2: 27 04               BEQ     $19A8                     ; End of list ... out
19A4: 91 00               CMPA    <$00                      ; {ram:curRoom} Matches our room?
19A6: 26 F6               BNE     $199E                     ; No ... next entry
19A8: 39                  RTS                               ; Out

19A9: 7E 10 99            JMP     $1099                     ; {ComWHAT} Command + " WHAT?"
```

## JUMP 
 There is a table of jump info that describes the jumps from various room and
 where they go. Each jump has a dexterity associated with it. If your phys-weight
 is less than value you fail the jump. If your phys-bulk is less than value you
 leave the heaviest object behind as you jump. Each jump describes what to do
 if the jump fails. Could be a fixed damage. Could be a fumble. Could be death.

```code 
CommandJUMP:
19AC: BD 0D A6            JSR     $0DA6                     ; Make sure we can see
19AF: 24 04               BCC     $19B5                     ; Yes ... skip the hurt
19B1: 86 20               LDA     #$20                      ; Jumping in the dark ...
19B3: 8D 7A               BSR     $1A2F                     ; ... take 32 damage
19B5: 8D E4               BSR     $199B                     ; Look for entry in table
19B7: 4D                  TSTA                              ; Is there one?
19B8: 27 EF               BEQ     $19A9                     ; No ... "JUMP WHAT?" and out
19BA: A6 44               LDA     4,U                       ; Thing we are jumping
19BC: 91 2B               CMPA    <$2B                      ; {ram:nounNum} Did we ask to jump it?
19BE: 26 E9               BNE     $19A9                     ; No ... "JUMP WHAT?" and out
19C0: 96 05               LDA     <$05                      ; {ram:condition} Physical condition ...
19C2: 90 04               SUBA    <$04                      ; {ram:weight} ... minus weight of pack
19C4: 25 17               BCS     $19DD                     ; Phys cond less ... bad jump
19C6: A1 41               CMPA    1,U                       ; Required extra to make jump
19C8: 23 13               BLS     $19DD                     ; Not enough ... bad jump
19CA: 96 05               LDA     <$05                      ; {ram:condition} Physical condition ...
19CC: 90 06               SUBA    <$06                      ; {ram:bulk} ... minus bulk of pack
19CE: 25 26               BCS     $19F6                     ; Phys cond less ... jump but drop heaviest
19D0: A1 41               CMPA    1,U                       ; Required extra to make jump
19D2: 23 22               BLS     $19F6                     ; Not enough ... jump but drop heaviest
19D4: A6 43               LDA     3,U                       ; Get target room
19D6: 97 01               STA     <$01                      ; {ram:lastRoom} Set last room ...
19D8: 97 00               STA     <$00                      ; {ram:curRoom} ... and current room
19DA: 7E 0E 27            JMP     $0E27                     ; Print room description and out

; Failed jump
19DD: A6 42               LDA     2,U                       ; Failed jump flags
19DF: 26 09               BNE     $19EA                     ; Not death
;
; Fall
19E1: 8E 33 B0            LDX     #$33B0                    ; "YOUR JUMPING ABILITY IS NOT AS GOOD AS IT ONCE WAS - YOU HAVE FALLEN AND DIED."
19E4: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
19E7: 7E 0D 5C            JMP     $0D5C                     ; {CommandUNCLE} UNCLE ... new game
;
19EA: 2B 0A               BMI     $19F6                     ; Upper bit ... fumble (make jump but drop heaviest)
;
; Stumble ... take damage and go nowhere
19EC: 8E 2F 13            LDX     #$2F13                    ; "YOU HAVE STUMBLED AND FALLEN."
19EF: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
19F2: 8D 3B               BSR     $1A2F                     ; Value is damage ... take damage
19F4: 20 E4               BRA     $19DA                     ; Print room description (stay in room)

; Fumble ... make jump but drop heaviest
19F6: 8D 06               BSR     $19FE                     ; Drop heaviest object
19F8: 86 06               LDA     #$06                      ; Take ...
19FA: 8D 33               BSR     $1A2F                     ; ... 6 damage
19FC: 20 D6               BRA     $19D4                     ; Land in target room

; Drop the heaviest object in pack. If it is an incidental object then
; there is a 1/8th chance of it getting lost forever.   
19FE: 34 16               PSHS    X,B,A                     ; Save params
1A00: 8D 6C               BSR     $1A6E                     ; Find heaviest and bulkiest in pack
1A02: 5D                  TSTB                              ; Pack empty?
1A03: 27 23               BEQ     $1A28                     ; No ... out
1A05: 1F 89               TFR     A,B                       ; Weightiest object
1A07: C1 0C               CMPB    #$0C                      ; Is it the lamp?
1A09: 26 02               BNE     $1A0D                     ; No
1A0B: 0C 14               INC     <$14                      ; {ram:lampStripped} Flag lamp has been torn from player
1A0D: 96 00               LDA     <$00                      ; {ram:curRoom} Current room
1A0F: BD 12 C6            JSR     $12C6                     ; Adjust pack for dropping object
1A12: BD 10 AE            JSR     $10AE                     ; Drop the object
1A15: 8D 43               BSR     $1A5A                     ; {GetObject} Get the object data
1A17: A6 02               LDA     2,X                       ; Flags
1A19: 85 20               BITA    #$20                      ; Is this object required
1A1B: 27 0B               BEQ     $1A28                     ; Yes ... can't lose it
1A1D: BD 06 61            JSR     $0661                     ; {Random} Random number
1A20: C1 20               CMPB    #$20                      ; 7/8 of time ...
1A22: 22 04               BHI     $1A28                     ; ... nothing happens
1A24: 8A 01               ORA     #$01                      ; Remove object ...
1A26: A7 02               STA     2,X                       ; ... from game
1A28: 35 96               PULS    A,B,X,PC                  ; Done

; Take random damage 0 to B and drop heaviest object
1A2A: BD 06 90            JSR     $0690                     ; {RandB} Random number 0 to B
1A2D: 1F 98               TFR     B,A                       ; Damage to A
;
; Take damage and drop heaviest object
1A2F: 34 02               PSHS    A                         ; Hold adjustment
1A31: 96 46               LDA     <$46                      ; {ram:akhiromMins} Temporarily invulnerable (AKHIROM)?
1A33: 26 17               BNE     $1A4C                     ; Yes ... no damage
1A35: 96 05               LDA     <$05                      ; {ram:condition} Current physical condition
1A37: A0 E4               SUBA    ,S                        ; Subtract adjustment
1A39: 24 09               BCC     $1A44                     ; Still OK ... continue
1A3B: 8E 2F 30            LDX     #$2F30                    ; "YOU HAVE DIED FROM EXHAUSTION AND WOUNDS."
1A3E: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
1A41: 7E 0D 5C            JMP     $0D5C                     ; {CommandUNCLE} Command "UNCLE" ... end of game
1A44: 97 05               STA     <$05                      ; {ram:condition} New physical condition
1A46: 91 04               CMPA    <$04                      ; {ram:weight} Compare to weight of pack
1A48: 24 02               BCC     $1A4C                     ; Still OK
1A4A: 8D B2               BSR     $19FE                     ; Drop heaviest object in pack
1A4C: 35 82               PULS    A,PC                      ; Done
       
; Add to physical condition (max out at 255)
1A4E: 34 02               PSHS    A                         ; Save params
1A50: 9B 05               ADDA    <$05                      ; {ram:condition} Increase the physical condition
1A52: 24 02               BCC     $1A56                     ; OK to use
1A54: 86 FF               LDA     #$FF                      ; Max out at 255
1A56: 97 05               STA     <$05                      ; {ram:condition} New physical condition
1A58: 35 82               PULS    A,PC                      ; Done
        
GetObject:
; Get 3-byte descriptor for object B
1A5A: 34 06               PSHS    B,A                       ; Save params
1A5C: 5D                  TSTB                              ; Object ...
1A5D: 27 0D               BEQ     $1A6C                     ; ... invalid ... out
1A5F: C1 3F               CMPB    #$3F                      ; Object ...
1A61: 22 09               BHI     $1A6C                     ; ... invalid ... out
1A63: 5A                  DECB                              ; Object are base 1
1A64: 86 03               LDA     #$03                      ; 3 bytes per ...
1A66: 3D                  MUL                               ; ... object
1A67: 8E 3C FC            LDX     #$3CFC                    ; Offset into ...
1A6A: 30 8B               LEAX    D,X                       ; ... object table
1A6C: 35 86               PULS    A,B,PC                    ; Out

;Find heaviest (A) and bulkiest (B) objects in pack.
1A6E: 34 30               PSHS    Y,X                       ; Save params
1A70: 32 7C               LEAS    -4,S                      ; Reserve 4 params
1A72: 6F E4               CLR     ,S                        ; Current heaviest object
1A74: 6F 61               CLR     1,S                       ; Current bulkiest object
1A76: 6F 62               CLR     2,S                       ; Heaviest object
1A78: 6F 63               CLR     3,S                       ; Bulkiest object
1A7A: 5F                  CLRB                              ; Start with 1
1A7B: 5C                  INCB                              ; Next object
1A7C: C1 3F               CMPB    #$3F                      ; All done?
1A7E: 24 20               BCC     $1AA0                     ; Yes ... return what we found
1A80: BD 18 85            JSR     $1885                     ; {InPack} Is object in pack?
1A83: 24 F6               BCC     $1A7B                     ; No ... next object
1A85: D7 07               STB     <$07                      ; {ram:nounObjNum} Param
1A87: BD 19 8C            JSR     $198C                     ; Get object weight/bulk
1A8A: A6 A4               LDA     ,Y                        ; Weight
1A8C: A1 E4               CMPA    ,S                        ; Compare to current highest
1A8E: 23 04               BLS     $1A94                     ; Lighter ... move on
1A90: E7 62               STB     2,S                       ; New heaviest object
1A92: A7 E4               STA     ,S                        ; New heaviest weight
1A94: A6 21               LDA     1,Y                       ; Get bulk
1A96: A1 61               CMPA    1,S                       ; Compare to current bulkiest
1A98: 23 E1               BLS     $1A7B                     ; Not as bulkiy ... move on
1A9A: E7 63               STB     3,S                       ; New bulkiest objet
1A9C: A7 61               STA     1,S                       ; New bulkiest bulk
1A9E: 20 DB               BRA     $1A7B                     ; Continue
;
1AA0: EC 62               LDD     2,S                       ; A=heaviest, B=bulkiest
1AA2: 32 64               LEAS    4,S                       ; Remove params from stack
1AA4: 35 B0               PULS    X,Y,PC                    ; Out
```

## LAMP
 Turn lamp on or off.

```code
CommandLAMP:
1AA6: B6 3D 1F            LDA     $3D1F                     ; Lamp in pack?
1AA9: 2B 0E               BMI     $1AB9                     ; Yes ... we can fiddle with it
1AAB: 96 00               LDA     <$00                      ; {ram:curRoom} Current room
1AAD: B1 3D 1D            CMPA    $3D1D                     ; Lamp in this room?
1AB0: 27 07               BEQ     $1AB9                     ; yes ... we can fiddle with it
1AB2: 86 A6               LDA     #$A6                      ; "LAMP"
1AB4: 97 2B               STA     <$2B                      ; {ram:nounNum} To noun
1AB6: 7E 18 E5            JMP     $18E5                     ; "I DON'T SEE ANY LAMP HERE." and out
1AB9: 96 2B               LDA     <$2B                      ; {ram:nounNum} Input token
1ABB: 81 8F               CMPA    #$8F                      ; "OFF"
1ABD: 27 0A               BEQ     $1AC9                     ; Yes ... OFF
1ABF: 81 34               CMPA    #$34                      ; "ON"
1AC1: 27 0C               BEQ     $1ACF                     ; Yes ... ON
1AC3: 8E 2A 81            LDX     #$2A81                    ; "I DON'T UNDERSTAND THAT."
1AC6: 7E 10 66            JMP     $1066                     ; {PrintMess} Print the message and out
; Lamp off
1AC9: 0F 0A               CLR     <$0A                      ; {ram:lampOn} Lamp off
1ACB: C6 01               LDB     #$01                      ; "THE LAMP IS OFF"
1ACD: 20 0B               BRA     $1ADA                     ; Print and out
; Lamp on
1ACF: 9E 38               LDX     <$38                      ; {ram:lampOil} Oil in lamp
1AD1: 27 05               BEQ     $1AD8                     ; No oil left ... error and out
1AD3: 97 0A               STA     <$0A                      ; {ram:lampOn} Non-zero value
1AD5: C6 02               LDB     #$02                      ; "THE LAMP IS ON"
1AD7: 8C C6 06            CMPX    #$C606                    ; "THERE IS NO OIL IN THE LAMP"
1ADA: 7E 10 48            JMP     $1048                     ; Print and out
    
; Get list of things needed for protected item  
1ADD: 34 02               PSHS    A                         ; Save params
1ADF: 10 8E 3F B8         LDY     #$3FB8                    ; Built in memory
1AE3: A6 A0               LDA     ,Y+                       ; Get item number
1AE5: A1 E4               CMPA    ,S                        ; Is this our list?
1AE7: 27 0F               BEQ     $1AF8                     ; Yes. C=1 ... found
1AE9: A6 A0               LDA     ,Y+                       ; Skip ....
1AEB: 81 FF               CMPA    #$FF                      ; ... to ...
1AED: 26 FA               BNE     $1AE9                     ; ... end
1AEF: A6 A4               LDA     ,Y                        ; End of all ...
1AF1: 81 FF               CMPA    #$FF                      ; ... lists?
1AF3: 26 EE               BNE     $1AE3                     ; No ... keep looking
1AF5: 4F                  CLRA                              ; C=0 ... not found
1AF6: 35 82               PULS    A,PC                      ; Done
1AF8: 43                  COMA                              ; C=1 ... found
1AF9: 20 FB               BRA     $1AF6                     ; Done
```
     
# Between Room Actions

```code
BetweenRoomA:
; If phys minus weight is less than random 64-191 then a climb-up fails.

BetweenRoomC:
; If phys minus weight is less than 192 then a climb-up fails.

BetweenRoomD:
; If phys minus weight is less than 64 then a climb-up fails.

BetweenRoomE:
; If phys minus weight is less than 128 then a climb-up fails.
1AFB: BD 06 61            JSR     $0661                     ; {Random} Random number
1AFE: C4 7F               ANDB    #$7F                      ; 0 - 7F
1B00: CB 40               ADDB    #$40                      ; 40 - BF
;
1B02: 8C C6 C0            CMPX    #$C6C0                    ; LDB #$C0  Handler C
1B05: 8C C6 40            CMPX    #$C640                    ; LDB #$40  Handler D
1B08: 8C C6 80            CMPX    #$C680                    ; LDB #$80  Handler E
1B0B: D7 2E               STB     <$2E                      ; {ram:holderACDE} Hold handler value
1B0D: 96 02               LDA     <$02                      ; {ram:dirBits} Direction bit pattern
1B0F: 81 20               CMPA    #$20                      ; Up into this room?
1B11: 26 0C               BNE     $1B1F                     ; No ... do nothing
1B13: 96 05               LDA     <$05                      ; {ram:condition} Compare ...
1B15: 90 04               SUBA    <$04                      ; {ram:weight} ... phys - weight
CodeBug4:
; I think if we are overburdeoned it should jump to 1B1D and fail the move.
1B17: 25 06               BCS     $1B1F                     ; Overburdoned ... nothing happens
1B19: 91 2E               CMPA    <$2E                      ; {ram:holderACDE} Compare excess phys to value
1B1B: 24 02               BCC     $1B1F                     ; Excess is greater than value ... do nothing
1B1D: 0C 0C               INC     <$0C                      ; {ram:downFail} Flag for main handler to skip moving us
1B1F: 39                  RTS                               ; Done

BetweenRoomB:
; Most of time this moves us to room 10 ... the start room. But there is a 20% chance that 
; it moves us to a random room 0-F. Either way we tell the game loop to skip moving us
1B20: BD 06 61            JSR     $0661                     ; {Random} Random number
1B23: C1 D0               CMPB    #$D0                      ; Compare to 208 ... less than?
1B25: 25 05               BCS     $1B2C                     ; Most likely so ... move to room 10 (start)
1B27: C4 0F               ANDB    #$0F                      ; Random room 0-15
1B29: 1F 98               TFR     B,A                       ; Align params
1B2B: 8C 86 0A            CMPX    #$860A                    ; LDA #$0A  Handler
1B2E: 97 00               STA     <$00                      ; {ram:curRoom} Current room ...
1B30: 97 01               STA     <$01                      ; {ram:lastRoom} ... and last room
1B32: 20 E9               BRA     $1B1D                     ; Flag for skipping moving us

BetweenRoomF:
; If the lamp is in our pack this moves us to a totally random room.     
1B34: C6 0C               LDB     #$0C                      ; Is lamp ...
1B36: BD 18 85            JSR     $1885                     ; {InPack} ... in pack?
1B39: 24 07               BCC     $1B42                     ; No ... out
1B3B: BD 06 61            JSR     $0661                     ; {Random} Random number
1B3E: D7 00               STB     <$00                      ; {ram:curRoom} Current room ...
1B40: D7 01               STB     <$01                      ; {ram:lastRoom} ... and last room
1B42: 39                  RTS                               ; Done
 
BetweenRoomH:
; There is a 21/32 chance of going to a random room in the maze on a random floor. We flag the main
; routine to skip movement.
1B43: BD 06 61            JSR     $0661                     ; {Random} Random number
1B46: C4 1F               ANDB    #$1F                      ; Greatly increase our odds of not going to the maze
1B48: 20 03               BRA     $1B4D                     ; Go to the maze if the odds are right

BetweenRoomI:
; There is a 244 in 255 chance of moving to a random room in the maze on a random floor. 
; We flag the main routine to skip movement.
1B4A: BD 06 61            JSR     $0661                     ; {Random} Random number
1B4D: C1 0B               CMPB    #$0B                      ; Slim chance ...
1B4F: 23 0D               BLS     $1B5E                     ; ... of doing nothing
1B51: BD 06 61            JSR     $0661                     ; {Random} Random room
1B54: C4 CF               ANDB    #$CF                      ; Limt to 1st 16 rooms of any floor
1B56: CA 30               ORB     #$30                      ; Make it random room in maze
1B58: D7 00               STB     <$00                      ; {ram:curRoom} Current room
1B5A: D7 01               STB     <$01                      ; {ram:lastRoom} Last room
1B5C: 0C 0C               INC     <$0C                      ; {ram:downFail} Flag main to skip movement
1B5E: 39                  RTS                               ; Out

BetweenRoomG:
; There is a 50/50 chance of moving to a random room in the first half of the last floor.
1B5F: BD 06 61            JSR     $0661                     ; {Random} Random number
1B62: 2B FA               BMI     $1B5E                     ; Half the time do nothing
1B64: BD 06 61            JSR     $0661                     ; {Random} Random floor
1B67: C4 DF               ANDB    #$DF                      ; 1st half of whichever floor
1B69: CA C0               ORB     #$C0                      ; Floor 3 and 4
1B6B: 20 EB               BRA     $1B58                     ; Move and flag skip movement
```
    
# Entering Room Actions 

```code
EnteringRoomAction_a:
; _a Cave in to next floor (32 damage) if pack heavier than 192. If so move a and b to random rooms.

EnteringRoomAction_b:
; _b Cave in to next floor (32 damage) if pack heavier than 128. If so move a and b to random rooms.

EnteringRoomAction_c:
; _c Cave in to next floor (32 damage) if pack heavier than 95. If so move a and b to random rooms.
1B6D: 86 C0               LDA     #$C0                      ; Weight  192
1B6F: 8C 86 80            CMPX    #$8680                    ; 128
1B72: 8C 86 5F            CMPX    #$865F                    ; 95
1B75: 91 04               CMPA    <$04                      ; {ram:weight} Pack weighs more?
1B77: 23 01               BLS     $1B7A                     ; Yes ... fall to next level
1B79: 39                  RTS                               ; No ... done
;
1B7A: 96 00               LDA     <$00                      ; {ram:curRoom} Current room
1B7C: 8B 40               ADDA    #$40                      ; Drop a level
1B7E: 97 00               STA     <$00                      ; {ram:curRoom} Current room ...
1B80: 97 01               STA     <$01                      ; {ram:lastRoom} ... and last room
1B82: BD 06 61            JSR     $0661                     ; {Random} Random
1B85: F7 3C 8F            STB     $3C8F                     ; {ActionWhenEnteringRoom} Move first handler to another room
1B88: BD 06 61            JSR     $0661                     ; {Random} Random
1B8B: F7 3C 92            STB     $3C92                     ; Move second handler to another room
1B8E: 86 20               LDA     #$20                      ; Caved-in floor ...
1B90: BD 1A 2F            JSR     $1A2F                     ; ... takes 32 from physical condition
1B93: 8E 2D 68            LDX     #$2D68                    ; "THE FLOOR UNDER YOU HAS JUST CAVED IN!!"
1B96: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
1B99: 7E 19 FE            JMP     $19FE                     ; Drop heaviest object and out

EnteringRoomAction_d:
; _d If we have VETAR make the pile-of-rocks appear in this room (it stays here).
1B9C: C6 37               LDB     #$37                      ; Do we have ...
1B9E: BD 18 85            JSR     $1885                     ; {InPack} ... VETAR?
1BA1: 24 55               BCC     $1BF8                     ; No ... ignore
1BA3: 96 11               LDA     <$11                      ; {ram:rocksExposed} Have we already exposed the pile of rocks?
1BA5: 26 51               BNE     $1BF8                     ; Yes ... ignore
1BA7: 0C 10               INC     <$10                      ; {ram:rocksMoved} Mark pile of rocks moved to us
1BA9: 96 00               LDA     <$00                      ; {ram:curRoom} Current room
1BAB: 97 37               STA     <$37                      ; {ram:rocksRoom} Room of "pile of rocks"
1BAD: 8E 2F 59            LDX     #$2F59                    ; "A DULL, EERIE GLOW IS EMANATING FROM BEHIND A PILE OF ROCKS."
1BB0: 7E 10 66            JMP     $1066                     ; {PrintMess} Print the message

EnteringRoomAction_e:
; _e Play sound effect (same as bb). If we play the flute and have the parchment then the LEDGE appears here.
1BB3: 4F                  CLRA                              ; Something int the code taken out? This has no effect in sound routine.

EnteringRoomAction_z:
; _z Room with music (init to room 16 to 39). The sprite can't move objects here.
1BB4: 7E 0B 3E            JMP     $0B3E                     ; Sound effect

EnteringRoomAction_f:
; _f Powerful gust blows lamp out of grasp. 
;    No lamp in pack ... do nothing. Otherwise:
;    1/2 the time do nothing. The other half:
;    - Take 30 from physical condition
;    - Move the lamp to a neighboring room
;    - Spill 256 seconds of oil from the lamp
;    - Turn the lamp off
;    - Enable VETAR until next move
;    - 1/4th of the time move the handler to a room on level 0,1, or 2
1BB7: C6 0C               LDB     #$0C                      ; Is lamp ...
1BB9: BD 18 85            JSR     $1885                     ; {InPack} ... in pack?
1BBC: 24 3A               BCC     $1BF8                     ; No ... out
1BBE: BD 06 61            JSR     $0661                     ; {Random} Random
1BC1: 2B 35               BMI     $1BF8                     ; Do nothing 1/2 the time
1BC3: C6 1E               LDB     #$1E                      ; Take 30 from ...
1BC5: BD 1A 2A            JSR     $1A2A                     ; ... physical condition
1BC8: D6 00               LDB     <$00                      ; {ram:curRoom} Current room
1BCA: BD 06 77            JSR     $0677                     ; Get a valid direction out of this room
1BCD: 96 00               LDA     <$00                      ; {ram:curRoom} Current room
1BCF: BD 0F 71            JSR     $0F71                     ; Get target room in random direction
1BD2: C6 0C               LDB     #$0C                      ; Drop ...
1BD4: BD 12 C6            JSR     $12C6                     ; ... the lamp in target room
1BD7: 8E 2F F1            LDX     #$2FF1                    ; "A POWERFUL GUST OF WIND HAS BLOWN THE LAMP OUT OF YOUR GRASP."
1BDA: 0C 14               INC     <$14                      ; {ram:lampStripped} VETAR will work until next move
1BDC: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
1BDF: BD 06 61            JSR     $0661                     ; {Random} Random
1BE2: C1 3F               CMPB    #$3F                      ; 1/4th of the time ...
1BE4: 22 05               BHI     $1BEB                     ; ... room stays here
1BE6: CB 40               ADDB    #$40                      ; New room is NOT on bottom floor
1BE8: F7 3C 9E            STB     $3C9E                     ; New location for this handler
1BEB: DC 38               LDD     <$38                      ; {ram:lampOil} Oil level
1BED: 83 01 00            SUBD    #$0100                    ; This spills 256 seconds (4.3 minutes) from the lamp
1BF0: 24 02               BCC     $1BF4                     ; Didn't underflow
1BF2: 4F                  CLRA                              ; All ...
1BF3: 5F                  CLRB                              ; ... oil ...
1BF4: DD 38               STD     <$38                      ; {ram:lampOil} ... from lamp
1BF6: 0F 0A               CLR     <$0A                      ; {ram:lampOn} Lamp off
1BF8: 39                  RTS                               ; Done

EnteringRoomAction_g:
; _g Hydra is here. If it is free it pushes us back to last room. 
1BF9: 96 0E               LDA     <$0E                      ; {ram:hydraStatus} Hydra status ... free?
1BFB: 26 0E               BNE     $1C0B                     ; No ... see if it is dead
1BFD: 0C 0F               INC     <$0F                      ; {ram:hydraPushed} HYDRA is now in current room
1BFF: 8E 30 2F            LDX     #$302F                    ; "A NINE-HEADED HYDRA BLOCKS YOUR PASSAGE."
1C02: 0C 0D               INC     <$0D                      ; {ram:pushedBack} ? nobody ever uses this ?
1C04: 96 01               LDA     <$01                      ; {ram:lastRoom} Move back ...
1C06: 97 00               STA     <$00                      ; {ram:curRoom} ... to last room
1C08: 7E 10 66            JMP     $1066                     ; {PrintMess} Print the message
1C0B: 81 AA               CMPA    #$AA                      ; Is HYDRA tied up?
1C0D: 26 E9               BNE     $1BF8                     ; No ... must be dead ... out
1C0F: 8E 32 0A            LDX     #$320A                    ; "A VERY MAD HYDRA IS TIED UP HERE."
1C12: 7E 10 66            JMP     $1066                     ; {PrintMess} Print the message

EnteringRoomAction_h:
; _h If we know VETAR or have the SCEPTER, nothing happens. Otherwise we do command RUN.
1C15: C6 37               LDB     #$37                      ; Do we know ...
1C17: BD 18 85            JSR     $1885                     ; {InPack} ... VETAR?
1C1A: 25 DC               BCS     $1BF8                     ; Yes ... out
1C1C: C6 0B               LDB     #$0B                      ; Do we have ...
1C1E: BD 18 85            JSR     $1885                     ; {InPack} ... the scepter?
1C21: 25 D5               BCS     $1BF8                     ; Yes ... out
1C23: 8E 30 E7            LDX     #$30E7                    ; "A VERY POWERFUL MAGIC FORCE STRIKES YOU AND DRIVES YOU BACK."
1C26: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
1C29: 7E 14 D4            JMP     $14D4                     ; {CommandRUN} Command RUN

EnteringRoomAction_i:
; _i Do nothing if we have VETAR. If random number > phys condition or 1/2 the time we RUN and take 5 damage.

EnteringRoomAction_j:
; _j Do nothing if we have MITRA. If random number > phys condition or 1/2 the time we RUN and take 5 damage.

EnteringRoomAction_k:
; _k Do nothing if we have OKKAN. If random number > phys condition or 1/2 the time we RUN and take 5 damage.

EnteringRoomAction_l:
; _l Do nothing if we have AKHIROM. If random number > phys condition or 1/2 the time we RUN and take 5 damage.

EnteringRoomAction_m:
; _m Do nothing if we have NERGAL. If random number > phys condition or 1/2 the time we RUN and take 5 damage.

EnteringRoomAction_n:
; _n Do nothing if we have BELROG. If random number > phys condition or 1/2 the time we RUN and take 5 damage.

EnteringRoomAction_o:
; _o Do nothing if we have CROM. If random number > phys condition or 1/2 the time we RUN and take 5 damage.

EnteringRoomAction_p:
; _p Do nothing if we have ISHTAR. If random number > phys condition or 1/2 the time we RUN and take 5 damage.

; If we have the right spell, this does nothing. If a random number is greater than 
; physical condition, we get pushed back. Otherwise we get pushed back 1/2 the time.
; Pushing backs takes us to last room and subtracts 5 from physical condition.
1C2C: C6 37               LDB     #$37                      ; VETAR
1C2E: 8C C6 38            CMPX    #$C638                    ; MITRA
1C31: 8C C6 39            CMPX    #$C639                    ; OKKAN
1C34: 8C C6 3A            CMPX    #$C63A                    ; AKHIROM
1C37: 8C C6 3B            CMPX    #$C63B                    ; NERGAL
1C3A: 8C C6 3C            CMPX    #$C63C                    ; BELROG
1C3D: 8C C6 3D            CMPX    #$C63D                    ; CROM
1C40: 8C C6 3E            CMPX    #$C63E                    ; ISHTAR
1C43: BD 18 85            JSR     $1885                     ; {InPack} Do we know the spell?
1C46: 25 31               BCS     $1C79                     ; Yes ... nothing happens
1C48: BD 06 61            JSR     $0661                     ; {Random} Random number
1C4B: D0 04               SUBB    <$04                      ; {ram:weight} Random number greater than physical condition
1C4D: 25 04               BCS     $1C53                     ; Yes ... push back
1C4F: C1 80               CMPB    #$80                      ; 1/2 the time ...
1C51: 24 26               BCC     $1C79                     ; ... do nothing
1C53: 96 01               LDA     <$01                      ; {ram:lastRoom} Last room
1C55: 91 00               CMPA    <$00                      ; {ram:curRoom} Moved back to last room?
1C57: 27 20               BEQ     $1C79                     ; Yes ... that's OK
1C59: 8E 30 58            LDX     #$3058                    ; "A MAGIC SPELL HAS PUSHED YOU BACK OUT OF THIS ROOM."
1C5C: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
1C5F: 0C 0D               INC     <$0D                      ; {ram:pushedBack} ? Nobody ever checks this ?
1C61: 97 00               STA     <$00                      ; {ram:curRoom} Back to last room
1C63: C6 05               LDB     #$05                      ; Take ...
1C65: 7E 1A 2A            JMP     $1A2A                     ; ... damage of 5

EnteringRoomAction_q:
; _q Start the poison clock (we can't stay here long). 1/3 of the time we give the clock an extra tick.
1C68: 8E 31 24            LDX     #$3124                    ; "A MYSTERIOUS FOG BEGINS RISING FROM THE FLOOR!"
1C6B: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
1C6E: 0C 45               INC     <$45                      ; {ram:fogClock} Start poison time count
1C70: BD 06 61            JSR     $0661                     ; {Random} Random number
1C73: C1 55               CMPB    #$55                      ; 2/3 of the time ...
1C75: 24 02               BCC     $1C79                     ; ... nothing happens
1C77: 0C 32               INC     <$32                      ; {ram:enteredFog} 1/3 of the time give it a double increment
1C79: 39                  RTS                               ; Out
 
EnteringRoomAction_r:
; _r When we enter this room 3 times the treasure is released.
1C7A: 96 15               LDA     <$15                      ; {ram:treas0BReleased} Has treasure "$0B" been released?
1C7C: 26 FB               BNE     $1C79                     ; Yes ... ignore
1C7E: 0C 47               INC     <$47                      ; {ram:enterRcount} Increment count entering this room
1C80: 96 47               LDA     <$47                      ; {ram:enterRcount} Have we been here ...
1C82: 81 03               CMPA    #$03                      ; ... three times now?
1C84: 25 F3               BCS     $1C79                     ; No ... out
1C86: 0C 15               INC     <$15                      ; {ram:treas0BReleased} Flag treaure released
1C88: 86 0B               LDA     #$0B                      ; Drop ...
1C8A: 7E 0E 80            JMP     $0E80                     ; {DropHeldObj} .... treasure "$0B"

EnteringRoomAction_s:
; _s If we have the lamp and it is off then the room drops its treasure.
;    If the lamp is on we see the walls are a strange color.
1C8D: C6 0C               LDB     #$0C                      ; Is lamp ...
1C8F: BD 18 85            JSR     $1885                     ; {InPack} ... in pack?
1C92: 24 6B               BCC     $1CFF                     ; No ... out
1C94: 96 0A               LDA     <$0A                      ; {ram:lampOn} Lamp status
1C96: 26 0B               BNE     $1CA3                     ; Lamp is on ... can't see the glow
1C98: 8E 32 2C            LDX     #$322C                    ; "AN EERIE PHOSPHORESCENT GLOW FILLS THE ENTIRE ROOM!"
1C9B: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
1C9E: 86 09               LDA     #$09                      ; Drop treasure held by ...
1CA0: 7E 0E 80            JMP     $0E80                     ; {DropHeldObj} ... eerie phosphorescent glow
;
1CA3: 8E 33 7F            LDX     #$337F                    ; "THE WALLS OF THIS ROOM ARE A VERY STRANGE COLOR!"
1CA6: 7E 10 66            JMP     $1066                     ; {PrintMess} Print the message

EnteringRoomAction_t:
; _t If we are holding the packrat's trigger treasure (randomized at start) then the
;    packrat drops his treasure. If the packrat holds his own trigger then he
;    drops it immediately.
1CA9: 86 0A               LDA     #$0A                      ; Get object ...
1CAB: BD 0E 6A            JSR     $0E6A                     ; ... held by packrat
1CAE: D1 2C               CMPB    <$2C                      ; {ram:ratObject} Is its treasure the trigger?
1CB0: 27 0D               BEQ     $1CBF                     ; Yes ... go drop treasure
1CB2: D6 2C               LDB     <$2C                      ; {ram:ratObject} Is trigger object ...
1CB4: BD 18 85            JSR     $1885                     ; {InPack} ... in backpack?
1CB7: 25 06               BCS     $1CBF                     ; Yes ... go drop treasure
1CB9: 8E 33 1A            LDX     #$331A                    ; "A PACKRAT SCURRIES INTO A SMALL HOLE."
1CBC: 7E 10 66            JMP     $1066                     ; {PrintMess} Print the message
;
1CBF: 86 0A               LDA     #$0A                      ; Drop treasure ...
1CC1: BD 0E 80            JSR     $0E80                     ; {DropHeldObj} ... held by rat
1CC4: 24 39               BCC     $1CFF                     ; Nothing held ... out
1CC6: 8E 33 3F            LDX     #$333F                    ; "THANK THE PACKRAT FOR THIS TREASURE!"
1CC9: 7E 10 66            JMP     $1066                     ; {PrintMess} Print the message

EnteringRoomAction_u:
; _u If we can see you instantly get the treasure.
1CCC: BD 0D 8B            JSR     $0D8B                     ; Can we see?
1CCF: 24 2E               BCC     $1CFF                     ; No move on
1CD1: 86 03               LDA     #$03                      ; Drop the ...
1CD3: 7E 0E 80            JMP     $0E80                     ; {DropHeldObj} ... treasure

EnteringRoomAction_33:
; _33 If we can see you instantly get the treasure.
1CD6: BD 0D 8B            JSR     $0D8B                     ; Can we see?
1CD9: 24 24               BCC     $1CFF                     ; No move on
1CDB: 86 04               LDA     #$04                      ; Drop the ...
1CDD: 7E 0E 80            JMP     $0E80                     ; {DropHeldObj} ... treasure

EnteringRoomAction_32:
; _32 If we can't see we take 30 damage.
1CE0: BD 0D 8B            JSR     $0D8B                     ; Can we see?
1CE3: 25 1A               BCS     $1CFF                     ; Yes ... out
1CE5: 8E 2F 13            LDX     #$2F13                    ; "YOU HAVE STUMBLED AND FALLEN."
1CE8: BD 10 66            JSR     $1066                     ; {PrintMess} Print the message
1CEB: C6 1E               LDB     #$1E                      ; Take damage ...
1CED: 7E 1A 2A            JMP     $1A2A                     ; ... of 30

EnteringRoomAction_v:
; _v Print POOL OF OIL if the pool has oil in it. 
;    There are a limited number of refills (number chosen at init) and 
;    the oil does not appear until we know ISHTAR.
1CF0: 8D 06               BSR     $1CF8                     ; Get number of times left to refill lamp
1CF2: 27 0B               BEQ     $1CFF                     ; None ... out
1CF4: C6 10               LDB     #$10                      ; Print ...
1CF6: 20 2C               BRA     $1D24                     ; ... POOL OF OIL
;      
1CF8: F6 3B E0            LDB     $3BE0                     ; ISHTAR flags
1CFB: 27 02               BEQ     $1CFF                     ; Have not learned it ... out
1CFD: D6 3A               LDB     <$3A                      ; {ram:lampFills} Number of times lamp can be refilled
1CFF: 39                  RTS                               ; Out

EnteringRoomAction_x:
; _x Add 40 to health and move us a short distance away. 10 minutes must pass before again.   
1D00: 96 13               LDA     <$13                      ; {ram:auraTimer} Have we recently visited healed up here?
1D02: 26 FB               BNE     $1CFF                     ; Yes ... not again
1D04: 86 0A               LDA     #$0A                      ; Can heal again ...
1D06: 97 13               STA     <$13                      ; {ram:auraTimer} ... in 10 seconds
1D08: BD 06 61            JSR     $0661                     ; {Random} Random room number
1D0B: C4 3F               ANDB    #$3F                      ; 00-3F
1D0D: C0 1F               SUBB    #$1F                      ; Offset from -1F to 20
1D0F: DB 00               ADDB    <$00                      ; {ram:curRoom} Move to new room
1D11: C4 DF               ANDB    #$DF                      ; 1st half of whichever floor
1D13: D7 00               STB     <$00                      ; {ram:curRoom} Current room
1D15: D7 01               STB     <$01                      ; {ram:lastRoom} And last room
1D17: 86 28               LDA     #$28                      ; Add 40 to ...
1D19: BD 1A 4E            JSR     $1A4E                     ; ... health
1D1C: 8E 32 99            LDX     #$3299                    ; "YOU HAVE JUST WALKED THROUGH AN ENCHANTED AURA."
1D1F: 7E 10 66            JMP     $1066                     ; {PrintMess} Print the message

EnteringRoomAction_203:
; _203 Print SMALL PIT IN CORNER OF ROOM.
1D22: C6 0F               LDB     #$0F                      ; "THERE IS A SMALL PIT IN THE CORNER OF THE ROOM."
1D24: 7E 10 48            JMP     $1048                     ; Print the mesage

EnteringRoomAction_213:
; _213 Print LAYER OF MIST EAST WALL.
1D27: 8E 31 83            LDX     #$3183                    ; "A LAYER OF MIST OBSCURES THE EAST WALL."
1D2A: 7E 10 66            JMP     $1066                     ; {PrintMess} Print the message

EnteringRoomAction_232:
; _232 If we came south to this room and we are carying the pendant then move the 
;      pendant to a random room and move us to (or near) the start.
1D2D: 96 02               LDA     <$02                      ; {ram:dirBits} Direction we took to get here
1D2F: 81 08               CMPA    #$08                      ; Did we come south to this room?
1D31: 26 09               BNE     $1D3C                     ; No ... out
1D33: C6 0A               LDB     #$0A                      ; Move the pandant ...
1D35: BD 12 B8            JSR     $12B8                     ; ... from pack to a random room
1D38: 10 25 FD E4         LBCS    $1B20                     ; {BetweenRoomB} If we did move pendant do BetweenRoomB ... move us to or near start
1D3C: 39                  RTS                               ; Done
```

# DATA SECTION
 
## Spell Placement 
 This table describes where a spell can be placed at random. The last 24
 rooms on floors 1-3 and all of 4th floor is the maze (except for exit
 room on 4th floor). The given spell must be placed between the start and
 stop values (inclusive).

```code
SpellLocationLimits:
1D3D: 00 27 ; VETRA     0 -  39  1st floor (except last 24 rooms ... the maze)
1D3F: 40 67 ; MITRA    64 - 103  2nd floor (except last 24 rooms ... the maze)
1D41: 40 67 ; OKKAN    64 - 103  2nd floor (except last 24 rooms ... the maze)
1D43: 40 67 ; AKHIROM  64 - 103  2nd floor (except last 24 rooms ... the maze)
1D45: 80 A7 ; NERGAL  128 - 167  3rd floor (except last 24 rooms ... the maze) 
1D47: 80 A7 ; BELROG  128 - 167  3rd floor (except last 24 rooms ... the maze)
1D49: 80 FF ; CROM    128 - 255  anywhere on 3rd or 4th floor
1D4B: 80 FF ; ISHTAR  128 - 255  anywhere on 3rd or 4th floor       
```

## Protected Objects Lists     
 There are 14 objects in the game that require us to have a combination
 of objects to kill/get. This table lists a number of configurations
 for each of these objects. On initialization, a random list is chosen
 from the possibile lists for each object. 

 Note that none of these are treasures, so the game can't be unwinnable because a
 creature carries the object needed to kill it.

 These lists are carefully constructed so that we can never have an unwinnable
 game because two objects require one another to get.

```code
ProtectedObjectConfiguration:
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

## Entering-Room Placement
 The first 30 entering-room-actions are placed using this table. The first two
 bytes are the lower and upper bounds of room numbers (inclusive) it can appear.

 The third byte is ANDed with the room number.

 The DF limits the room to the 1st half of the floor (away from the maze).

```code
EnteringRoomActionPlacment:
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
;
; This room could be placed with room 203b. That would mean that
; there are 2 pits in the same room.
;
; _213
; _32b
; _33
; _203b
; _z (music room that sprite can't go in) Random 16 - 39
; _232
```

 This table lists the objects the Oracle will give advice on. They are
 all protected objects listed in the order they appear in the config
 table. Note that the spellbook is missing.

```code
OracleAdviceTable:
1E43: 1A ; TROGLODYTE           
1E44: 1D ; SATYR                                
1E45: 1E ; MINOTAUR
1E46: 1B ; SCORPION                     
1E47: 1C ; NYMPH
1E48: 19 ; SPRITE                      
1E49: 06 ; SWORD
1E4A: 0F ; VIAL          
1E4B: 07 ; SHIELD
1E4C: 14 ; SKULL                  
1E4D: 2A ; POWERRING
1E4E: 2B ; LIGHTRING                   
1E4F: 2C ; TRUTHRING
         ; Missing SPELLBOOK ... advice seen by looking in pool in room 0
1E50: 00      
```

## Item Descriptions       

```code       
ItemDescriptions:
1E51: 00 FF  ; Message 0 ""
1E53: 01 30 8C 94 85 FF  ; Message 1 "THERE IS FOOD HERE."
1E59: 02 64 B8 8C 89 34 35 40 FF  ; Message 2 "A BOTTLE IS RESTING ON THE FLOOR."
1E62: 03 64 1D 26 8C 34 35 40 FF  ; Message 3 "A SMALL DAGGER IS ON THE FLOOR."
1E6B: 04 64 C9 8C 22 35 10 67 35 C8 FF  ; Message 4 "A MACE IS IN THE CENTER OF THE PATH."
1E76: 05 64 29 5F 8C 21 22 35 40 FF  ; Message 5 "A GREAT AX IS STUCK IN THE FLOOR."
1E80: 06 64 8E 52 8C 85 FF  ; Message 6 "A BRONZE SWORD IS HERE."
1E87: 07 64 87 53 8C 92 91 8A FF  ; Message 7 "A LEATHER SHIELD IS AT YOUR FEET."
1E90: 08 64 81 24 88 22 35 0F FF  ; Message 8 "A GOLD FLUTE SITS IN THE CORNER."
1E99: 09 30 08 CA 34 35 40 FF  ; Message 9 "THERE IS A MUSHROOM ON THE FLOOR."
1EA1: 0A 64 A4 8C 22 64 1D 9F A0 95 35 0C FF  ; Message 10 "A PENDANT IS IN A SMALL HOLE RECESSED INTO THE WALL."
1EAE: 0B 30 8C 64 A5 34 35 40 FF  ; Message 11 "THERE IS A SCEPTER ON THE FLOOR."
1EB7: 0C 30 8C 64 1D A6 89 8B 35 0C FF  ; Message 12 "THERE IS A SMALL LAMP RESTING AGAINST THE WALL."
1EC2: 0D 64 27 8C 22 35 10 67 35 40 FF  ; Message 13 "A BASKET IS IN THE CENTER OF THE FLOOR."
1ECD: 0E EE 65 A7 8C 89 34 64 2A FF  ; Message 14 "AN ANCIENT PARCHMENT IS RESTING ON A STONE."
1ED7: 0F 64 1D A8 88 22 35 0F FF  ; Message 15 "A SMALL VIAL SITS IN THE CORNER."
1EE0: 10 EE A9 8C 89 34 64 1E 79 2A FF  ; Message 16 "AN URN IS RESTING ON A LARGE SMOOTH STONE."
1EEB: 11 64 23 C1 88 34 35 70 67 35 CD FF  ; Message 17 "A MAGIC TALISMAN SITS ON THE EDGE OF THE PATH."
1EF7: 12 64 4A B7 8C 89 8B 35 0C FF  ; Message 18 "A MUSTY SCROLL IS RESTING AGAINST THE WALL."
1F01: 13 30 8C 64 C2 34 35 40 FF  ; Message 19 "THERE IS A GOBLET ON THE FLOOR."
1F0A: 14 64 66 88 22 64 1D 9F 22 35 40 FF  ; Message 20 "A SKULL SITS IN A SMALL HOLE IN THE FLOOR."
1F16: 15 64 81 C7 8C CB 22 35 CC 14 FF  ; Message 21 "A GOLD SCARAB IS SPARKLING IN THE DIM LIGHT."
1F21: 16 EE 65 E5 D0 84 35 D1 67 64 CD FF  ; Message 22 "AN ANCIENT JEWELBOX LAYS TO THE SIDE OF A PATH."
1F2D: 17 64 4D 7A C4 8C 9C 89 8B 64 2A FF  ; Message 23 "A BROKEN MARBLE TABLET IS GENTLY RESTING AGAINST A STONE."
1F39: 18 64 20 CE 8C 34 35 40 FF  ; Message 24 "A LONG ROPE IS ON THE FLOOR."
1F42: 19 64 BA 88 34 64 3A 22 35 0F 67 35 3C FF  ; Message 25 "A SPRITE SITS ON A CHAIR IN THE CORNER OF THE ROOM."
1F50: 1A 64 1E BB 8C 22 35 3C FF  ; Message 26 "A LARGE TROGLODYTE IS IN THE ROOM."
1F59: 1B 35 AB 8C 85 FF  ; Message 27 "THE SCORPION IS HERE."
1F5F: 1C 35 AC 8C 85 FF  ; Message 28 "THE NYMPH IS HERE."
1F65: 1D 35 AD 8C 85 FF  ; Message 29 "THE SATYR IS HERE."
1F6B: 1E 35 7F 8C 85 FF  ; Message 30 "THE MINOTAUR IS HERE."
1F71: 1F 35 AE 8C 85 FF  ; Message 31 "THE ORACLE IS HERE."
1F77: 20 30 8C 81 34 35 40 FF  ; Message 32 "THERE IS GOLD ON THE FLOOR."
1F7F: 21 64 8D 67 25 8C 85 FF  ; Message 33 "A BAG OF SILVER IS HERE."
1F87: 22 CB AF 8C 22 64 1D 9F 22 35 0C FF  ; Message 34 "A SPARKLING DIAMOND IS IN A SMALL HOLE IN THE WALL."
1F93: 23 35 B0 8C 85 FF  ; Message 35 "THE SPELLBOOK IS HERE."
1F99: 24 64 1E BF D0 84 35 D1 67 35 CD 22 35 CF FF  ; Message 36 "A LARGE RUBY LAYS TO THE SIDE OF THE PATH IN THE DIRT."
1FA8: 25 64 81 B2 D0 34 64 1D 39 FF  ; Message 37 "A GOLD FLEECE LAYS ON A SMALL TABLE."
1FB2: 26 64 1D 25 B3 D0 34 35 40 FF  ; Message 38 "A SMALL SILVER TIARA LAYS ON THE FLOOR."
1FBC: 27 64 8D 67 23 B4 8C 34 64 39 FF  ; Message 39 "A BAG OF MAGIC POWDER IS ON A TABLE."
1FC7: 28 64 1D B5 8C 34 35 40 FF  ; Message 40 "A SMALL AMULET IS ON THE FLOOR."
1FD0: 29 64 1D B8 38 64 23 B6 22 D2 8C 85 FF  ; Message 41 "A SMALL BOTTLE WITH A MAGIC POTION IN IT IS HERE."
1FDD: 2A 35 BC 8C CB 34 35 90 FF  ; Message 42 "THE POWERRING IS SPARKLING ON THE TRAIL."
1FE6: 2B 35 BD 8C CB 34 35 CD FF  ; Message 43 "THE LIGHTRING IS SPARKLING ON THE PATH."
1FEF: 2C 35 BE 8C CB 34 35 40 FF  ; Message 44 "THE TRUTHRING IS SPARKLING ON THE FLOOR."
1FF8: 2D 64 81 C0 8C 89 22 64 3E 67 CF FF  ; Message 45 "A GOLD CROWN IS RESTING IN A PILE OF DIRT."
2004: 2E 64 1E FA 8C CB 22 35 14 FF  ; Message 46 "A LARGE OPAL IS SPARKLING IN THE LIGHT."
200E: 2F 64 1E FB D0 8B 35 70 67 64 2A FF  ; Message 47 "A LARGE SAPPHIRE LAYS AGAINST THE EDGE OF A STONE."
201A: 86 64 23 52 8C 21 22 64 1E 2A FF  ; Message 134 "A MAGIC SWORD IS STUCK IN A LARGE STONE."
2025: 87 64 87 53 8C DA 34 35 0C FF  ; Message 135 "A LEATHER SHIELD IS HANGING ON THE WALL."
202F: 8F 64 60 A8 8C DB 22 35 D3 FF  ; Message 143 "A GLASS VIAL IS SUSPENDED IN THE AIR."
2039: 94 64 66 8C 89 22 35 10 67 64 66 39 FF  ; Message 148 "A SKULL IS RESTING IN THE CENTER OF A SKULL TABLE."
2046: A3 64 23 B0 88 34 35 70 67 64 0B 39 FF  ; Message 163 "A MAGIC SPELLBOOK SITS ON THE EDGE OF A SHALLOW TABLE."
2053: AA 35 BC 8C 34 64 D4 3A FF  ; Message 170 "THE POWERRING IS ON A VELVET CHAIR."
205C: AB 35 BD 88 34 64 3E 67 3F FF  ; Message 171 "THE LIGHTRING SITS ON A PILE OF BONES."
2066: AC 35 BE 8C DC 22 35 10 67 64 60 2A FF  ; Message 172 "THE TRUTHRING IS BURIED IN THE CENTER OF A GLASS STONE."
2073: FF

ItemProtectedMessages:
; Item-is-protected Messages
2074: 06 35 52 E4 D5 E1 FF  ; Message 6 "THE SWORD WILL NOT MOVE."
207B: 07 9B DE D5 D6 35 53 FF  ; Message 7 "YOU CAN NOT REACH THE SHIELD."
2083: 0F 35 A8 8C 9E 67 D6 FF  ; Message 15 "THE VIAL IS OUT OF REACH."
208B: 14 64 23 D9 DF 9B D7 35 66 FF  ; Message 20 "A MAGIC FORCE KEEPS YOU FROM THE SKULL."
2095: 23 35 B0 E0 9E 67 D6 DD 9B E1 E2 D2 FF  ; Message 35 "THE SPELLBOOK FLOATS OUT OF REACH WHEN YOU MOVE NEAR IT."
20A2: 2A 35 BC 97 DD 9B E1 E2 D2 FF  ; Message 42 "THE POWERRING DISAPPEARS WHEN YOU MOVE NEAR IT."
20AC: 2B 64 17 86 05 D7 35 3F 2F DF 9B D7 35 BD FF  ; Message 43 "A SKELETON SPRINGS UP FROM THE BONES AND KEEPS YOU FROM THE LIGHTRING."
20BB: 2C 35 60 2A 8C E3 D8 23 FF  ; Message 44 "THE GLASS STONE IS PROTECTED BY MAGIC."
20C4: FF
```
         
## Object Placement 
 16 different rooms that protected objects may be placed in. It is likely that
 multiple protected objects will be dropped in the same room.

```code
PossibleProtectedObjectLocations:
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

 This script controls how objects are placed and how the flags are initialized.
 For range placment the room is ((u-l)&mask)+lower. Table for table placement
 is above. Protection does OR #$10. Invisible object does OR #$01.
 Weights and Bulk values are copied from the table at 354A.

```code
ObjectPlacementScript:
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
;
2155: 02              ;        unused
2156: 02              ;        unused
2157: 02              ;        unused
2158: 02              ;        unused    
2159: 02              ;        unused
215A: 02              ;        unused
215B: 02              ;        unused
;
215C: 02              ; VETAR      OR with 0x42 SPELL
215D: 02              ; MITRA      OR with 0x42 SPELL
215E: 02              ; OKKAN      OR with 0x42 SPELL
215F: 02              ; AKHIROM    OR with 0x42 SPELL
2160: 02              ; NERGAL     OR with 0x42 SPELL
2161: 02              ; BELROG     OR with 0x42 SPELL
2162: 02              ; CROM       OR with 0x42 SPELL
2163: 02              ; ISHTAR     OR with 0x42 SPELL             
2164: 55  ; End of list   
```

## Room Descriptions 
 List of base room descriptions

```code
BaseRoomDescriptions:

; Room 0
; [YOU ARE] IN A GREAT STONE TOWER WITH A LOW BROKEN CEILING
; AND A POOL OF WATER IN THE CORNER.
2165: 22 64 29 2A 2B 38 64 0E 4D 0A 2F 64 2C 67 2D 22 35 0F FF

; Room 1
; [YOU ARE] IN A SMALL EMPTY ROOM WITH A BROKEN FLOOR.
2178: 22 64 1D 47 3C 38 64 4D 40 FF

; Room 2
; [YOU ARE] IN THE GUARD ROOM WITH A GREAT WOOD PILE.
2182: 22 35 3B 3C 38 64 29 3D 3E FF

; Room 3
; [YOU ARE] IN THE CENTER OF A NARROW HALL WAY AND THERE IS A
; PILE OF BONES ON THE FLOOR.
218C: 22 35 10 67 64 28 37 1C 2F 30 8C 64 3E 67 3F 34 35 40 FF

; Room 4
; [YOU ARE] IN A SMALL CLEAN ROOM WITH A TORCH HIGH ON THE
; WALL.
219F: 22 64 1D 42 3C 38 64 16 0D 34 35 0C FF

; Room 5
; [YOU ARE] IN THE TROPHY ROOM WITH A LARGE WOOD PILE IN THE
; CORNER.
21AC: 22 35 46 3C 38 64 1E 3D 3E 22 35 0F FF

; Room 6
; [YOU ARE] IN AN EMPTY CLOSET.
21B9: 22 EE 47 48 FF

; Room 7
; [YOU ARE] IN A GREAT SLOPING SHAFT.
21BE: 22 64 29 9D 71 FF

; Room 8
; [YOU ARE] ON A NARROW PASSAGE WAY WITH A MARBLE FLOOR.
21C4: 34 64 28 1B 1C 38 64 7A 40 FF

; Room 9
; [YOU ARE] IN A SMALL ROOM WITH DRAPES ON THE SOUTH WALL AND
; NARCISSUS PLANTS IN THE CORNER.
21CE: 22 64 1D 3C 38 33 34 35 02 0C 2F 18 19 22 35 0F FF

; Room 10
; [YOU ARE] IN A NARROW HALL WAY WITH A TABLE AND CHAIR.
21DF: 22 64 28 37 1C 38 64 39 2F 3A FF

; Room 11
; [YOU ARE] IN A PASSAGE WAY WITH A GREAT PAINTING ON THE
; NORTH WALL.
21EA: 22 64 1B 1C 38 64 29 49 34 35 01 0C FF

; Room 12
; [YOU ARE] IN A MUSTY ROOM FILLED WITH RATS AND BROKEN GLASS.
21F7: 22 64 4A 3C 36 38 4C 2F 4D 60 FF

; Room 13
; [YOU ARE] IN A GLASS HALL WAY WITH BROKEN TILES ON THE
; FLOOR.
2202: 22 64 60 37 1C 38 4D 4E 34 35 40 FF

; Room 14
; [YOU ARE] IN THE ROYAL BED ROOM WITH A SHALLOW CEILING.
220E: 22 35 4F 50 3C 38 64 0B 0A FF

; Room 15
; [YOU ARE] IN A SMALL DARK CHAMBER WITH NO WINDOWS.
2218: 22 64 1D 15 5C 38 44 45 FF

; Room 16
; [YOU ARE] AT THE WEST END OF A GREAT POOL OF WATER.
2221: 92 35 03 77 67 64 29 2C 67 2D FF

; Room 17
; [YOU ARE] AT THE EAST END OF A GREAT POOL OF WATER.
222C: 92 35 04 77 67 64 29 2C 67 2D FF

; Room 18
; [YOU ARE] IN A SMALL LIBRARY.
2237: 22 64 1D 54 FF

; Room 19
; [YOU ARE] IN A NARROW DAMP MUSTY CHAMBER WITH ANCIENT
; CARVINGS HIGH ON THE WALL.
223C: 22 64 28 63 4A 5C 38 65 13 0D 34 35 0C FF

; Room 20
; [YOU ARE] IN A GREEN MARBLE HALL.
224A: 22 64 32 7A 37 FF

; Room 21
; [YOU ARE] IN A WINE CELLAR.
2250: 22 64 55 56 FF

; Room 22
; [YOU ARE] IN THE CENTER OF THE CHAMBER OF THE KING.
2255: 22 35 10 67 35 5C 67 35 75 FF

; Room 23
; [YOU ARE] IN A DAMP CHILL HALL WAY WITH MIST SWIRLING ON THE
; FLOOR.
225F: 22 64 63 6A 37 1C 38 6B 6C 34 35 40 FF

; Room 24
; [YOU ARE] IN A WIDE HALL WAY WITH A GREAT WOOD TABLE AND A
; GLASS OF WINE.
226C: 22 64 1A 37 1C 38 64 29 3D 39 2F 64 60 67 55 FF

; Room 25
; [YOU ARE] AT THE EAST END OF A GREAT MARBLE PORTAL.
227C: 92 35 04 77 67 64 29 7A 57 FF

; Room 26
; [YOU ARE] IN A GREAT ROYAL COURT YARD.
2286: 22 64 29 4F 58 59 FF

; Room 27
; [YOU ARE] IN A CLOISTER HALL AND THE VOICES OF THE DEAD ARE
; NEAR.
228D: 22 64 5A 37 2F 35 C6 67 35 76 31 E2 FF

; Room 28
; [YOU ARE] IN A SMALL DARK CHAMBER.
229A: 22 64 1D 15 5C FF

; Room 29
; [YOU ARE] IN A DAMP PASSAGE WAY WITH GREEN MIST SWIRLING
; DOWN THE WALL.
22A0: 22 64 63 1B 1C 38 32 6B 6C 06 35 0C FF

; Room 30
; [YOU ARE] IN A LARGE BED ROOM WITH A LONG BROKEN SHADOW
; STRETCHING ACROSS THE FLOOR.
22AD: 22 64 1E 50 3C 38 64 20 4D EC ED EB 35 40 FF

; Room 31
; [YOU ARE] IN A LARGE PASSAGE WAY AND THE CEILING IS GENTLY
; SLOPING OUT OF SIGHT.
22BC: 22 64 1E 1B 1C 2F 35 0A 8C 9C 9D 9E 67 96 FF

; Room 32
; [YOU ARE] IN A NARROW TWISTING STAIR WAY WITH NO WINDOWS.
22CB: 22 64 28 2E 61 1C 38 44 45 FF

; Room 33
; [YOU ARE] IN A DARK SMALL TOWER ROOM WITH NO WINDOWS.
22D5: 22 64 15 1D 2B 3C 38 44 45 FF

; Room 34
; [YOU ARE] IN A ROOM WITH A LOW SLOPING CEILING AND A DARK
; SUNKEN PIT AT THE EAST END.
22DF: 22 64 3C 38 64 0E 9D 0A 2F 64 15 6E 6D 92 35 04 77 FF

; Room 35
; [YOU ARE] IN A DARK SERVANT CHAMBER WITH A LOW CEILING AND A
; SHALLOW HOLE AT THE WEST END.
22F1: 22 64 15 5B 5C 38 64 0E 0A 2F 64 0B 9F 92 35 03 77 FF

; Room 36
; [YOU ARE] IN A PANTRY FILLED WITH RATS AND BROKEN GLASS.
2303: 22 64 5D 36 38 4C 2F 4D 60 FF

; Room 37
; [YOU ARE] IN THE GREAT BEER HALL.
230D: 22 35 29 5E 37 FF

; Room 38
; [YOU ARE] IN A LARGE EMPTY CHAMBER AND THE WALL DISAPPEARS
; INTO THE MIST.
2313: 22 64 1E 47 5C 2F 35 0C 97 95 35 6B FF

; Room 39
; [YOU ARE] IN THE TEMPLE OF ZEUS.
2320: 22 35 E6 67 E7 FF

; Room 40
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2326: E8 FF

; Room 41
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2328: E8 FF

; Room 42
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
232A: E8 FF

; Room 43
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
232C: E8 FF

; Room 44
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS AND THERE IS A SMALL PIT WHICH DISAPPEARS
; INTO THE MIST.
232E: E8 2F 30 8C 64 1D 6D C5 97 95 35 6B FF

; Room 45
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
233B: E8 FF

; Room 46
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
233D: E8 FF

; Room 47
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
233F: E8 FF

; Room 48
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2341: E8 FF

; Room 49
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2343: E8 FF

; Room 50
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2345: E8 FF

; Room 51
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2347: E8 FF

; Room 52
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2349: E8 FF

; Room 53
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
234B: E8 FF

; Room 54
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
234D: E8 FF

; Room 55
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
234F: E8 FF

; Room 56
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2351: E8 FF

; Room 57
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2353: E8 FF

; Room 58
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2355: E8 FF

; Room 59
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2357: E8 FF

; Room 60
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2359: E8 FF

; Room 61
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
235B: E8 FF

; Room 62
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
235D: E8 FF

; Room 63
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
235F: E8 FF

; Room 64
; [YOU ARE] IN A LARGE CHAMBER WITH A GREAT PIT STRETCHING
; ACROSS THE SOUTH WALL.
2361: 22 64 1E 5C 38 64 29 6D ED EB 35 02 0C FF

; Room 65
; [YOU ARE] IN A NARROW CORRIDOR WITH A STONE WALL.
236F: 22 64 28 11 38 64 2A 0C FF

; Room 66
; [YOU ARE] IN A SMALL ROOM WITH A HIGH CEILING.
2378: 22 64 1D 3C 38 64 0D 0A FF

; Room 67
; [YOU ARE] IN A DAMP ROOM WITH A WOOD FLOOR AND A GREAT CRYPT
; IN THE CENTER.
2381: 22 64 63 3C 38 64 3D 40 2F 64 29 74 22 35 10 FF

; Room 68
; [YOU ARE] IN A STONE PASSAGE WAY WITH BONES IN THE WALL.
2391: 22 64 2A 1B 1C 38 3F 22 35 0C FF

; Room 69
; [YOU ARE] IN A GREAT LONG HALL WITH A CHILL MIST FLOWING
; DOWN THE EAST WALL.
239C: 22 64 29 20 37 38 64 6A 6B 7D 06 35 04 0C FF

; Room 70
; [YOU ARE] IN A LARGE ROOM WITH A FOUL SMELLING SUNKEN PIT AT
; THE NORTH END.
23AB: 22 64 1E 3C 38 64 7B 7C 6E 6D 92 35 01 77 FF

; Room 71
; [YOU ARE] AT THE EDGE OF A GREAT STONE SHAFT.
23BA: 92 35 70 67 64 29 2A 71 FF

; Room 72
; [YOU ARE] IN THE HALL OF THE ROYAL COURT.
23C3: 22 35 37 67 35 4F 58 FF

; Room 73
; [YOU ARE] IN A GREAT EMPTY CHAMBER.
23CB: 22 64 29 47 5C FF

; Room 74
; [YOU ARE] IN A ROOM WITH A LARGE POOL OF WATER.
23D1: 22 64 3C 38 64 1E 2C 67 2D FF

; Room 75
; [YOU ARE] IN A LARGE CAVERN WITH A CHILL MIST SWIRLING ON
; THE FLOOR.
23DB: 22 64 1E 68 38 64 6A 6B 6C 34 35 40 FF

; Room 76
; [YOU ARE] IN A NARROW TWISTING PASSAGE WHICH GENTLY WINDS
; INTO A GREAT CAVERN.
23E8: 22 64 28 2E 1B C5 9C 99 95 64 29 68 FF

; Room 77
; [YOU ARE] IN A SMALL ROOM WITH A SHALLOW HOLE.
23F5: 22 64 1D 3C 38 64 0B 9F FF

; Room 78
; [YOU ARE] IN A DAMP SUNKEN ROOM WITH A DARK STONE WALL AND A
; CHASM AT THE SOUTH END.
23FE: 22 64 63 6E 3C 38 64 15 2A 0C 2F 64 41 92 35 02 77 FF

; Room 79
; [YOU ARE] IN A CHAMBER WITH A HIGH STONE CEILING AND
; CARVINGS ON THE EAST WALL.
2410: 22 64 5C 38 64 0D 2A 0A 2F 13 34 35 04 0C FF

; Room 80
; [YOU ARE] IN A TWISTING MUSTY CORRIDOR.
241F: 22 64 2E 4A 11 FF

; Room 81
; [YOU ARE] IN A SUNKEN ROOM WITH GREAT A STONE TABLE.
2425: 22 64 6E 3C 38 29 64 2A 39 FF

; Room 82
; [YOU ARE] IN A LARGE CORRIDOR WITH A BROKEN STONE WALL AND A
; CHILL DAMP FLOOR.
242F: 22 64 1E 11 38 64 4D 2A 0C 2F 64 6A 63 40 FF

; Room 83
; [YOU ARE] IN A CAVERN WITH A LOW STONE CEILING.
243E: 22 64 68 38 64 0E 2A 0A FF

; Room 84
; [YOU ARE] IN A NARROW WINDING PASSAGE.
2447: 22 64 28 6F 1B FF

; Room 85
; [YOU ARE] IN A TWISTING WINDING PASSAGE.
244D: 22 64 2E 6F 1B FF

; Room 86
; [YOU ARE] IN A SMALL CHAMBER WITH A CHASM AT THE NORTH END.
2453: 22 64 1D 5C 38 64 41 92 35 01 77 FF

; Room 87
; [YOU ARE] IN A CAVE WITH A LARGE SHALLOW PIT IN THE CENTER.
245F: 22 64 69 38 64 1E 0B 6D 22 35 10 FF

; Room 88
; [YOU ARE] IN A MUSTY TWISTING CORRIDOR.
246B: 22 64 4A 2E 11 FF

; Room 89
; [YOU ARE] ON A TWISTING PASSAGE WAY ON THE EDGE OF A GREAT
; SHAFT.
2471: 34 64 2E 1B 1C 34 35 70 67 64 29 71 FF

; Room 90
; [YOU ARE] IN A TOMB OF THE SKULL.
247E: 22 64 72 67 35 66 FF

; Room 91
; [YOU ARE] IN A PASSAGE OF STONE TILES.
2485: 22 64 1B 67 2A 4E FF

; Room 92
; [YOU ARE] IN A WIDE ROOM WITH A SMALL PIT IN THE CENTER.
248C: 22 64 1A 3C 38 64 1D 6D 22 35 10 FF

; Room 93
; [YOU ARE] IN A WOOD PASSAGE WAY.
2498: 22 64 3D 1B 1C FF

; Room 94
; [YOU ARE] IN A WIDE HALL WAY WITH A SMALL PIT IN THE CORNER.
249E: 22 64 1A 37 1C 38 64 1D 6D 22 35 0F FF

; Room 95
; [YOU ARE] IN THE CENTER OF A WINDING STONE TUNNEL.
24AB: 22 35 10 67 64 6F 2A 78 FF

; Room 96
; [YOU ARE] IN A TWISTING MUSTY PASSAGE WAY.
24B4: 22 64 2E 4A 1B 1C FF

; Room 97
; [YOU ARE] IN A MUSTY TWISTING PASSAGE WAY.
24BB: 22 64 4A 2E 1B 1C FF

; Room 98
; [YOU ARE] IN A TWISTING MUSTY BROKEN PASSAGE.
24C2: 22 64 2E 4A 4D 1B FF

; Room 99
; [YOU ARE] IN A GREAT CAVERN WITH BROKEN STONE EVERYWHERE.
24C9: 22 64 29 68 38 4D 2A 73 FF

; Room 100
; [YOU ARE] IN A LONG DAMP TWISTING PASSAGE WITH A STONE
; CHAPEL ON THE SOUTH WALL.
24D2: 22 64 20 63 2E 1B 38 64 2A 43 34 35 02 0C FF

; Room 101
; [YOU ARE] IN A LONG PASSAGE WAY.
24E1: 22 64 20 1B 1C FF

; Room 102
; [YOU ARE] IN A CRYPT OF THE ANCIENT KING AND THE VOICES OF
; THE DEAD ARE HERE.
24E7: 22 64 74 67 35 65 75 2F 35 C6 67 35 76 31 85 FF

; Room 103
; [YOU ARE] IN A SMALL CAVE FILLED WITH VOICES.
24F7: 22 64 1D 69 36 38 C6 FF

; Room 104
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
24FF: E8 FF

; Room 105
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2501: E8 FF

; Room 106
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2503: E8 FF

; Room 107
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2505: E8 FF

; Room 108
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2507: E8 FF

; Room 109
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2509: E8 FF

; Room 110
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
250B: E8 FF

; Room 111
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
250D: E8 FF

; Room 112
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
250F: E8 FF

; Room 113
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2511: E8 FF

; Room 114
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2513: E8 FF

; Room 115
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2515: E8 FF

; Room 116
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2517: E8 FF

; Room 117
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2519: E8 FF

; Room 118
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
251B: E8 FF

; Room 119
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
251D: E8 FF

; Room 120
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
251F: E8 FF

; Room 121
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2521: E8 FF

; Room 122
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2523: E8 FF

; Room 123
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2525: E8 FF

; Room 124
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2527: E8 FF

; Room 125
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2529: E8 FF

; Room 126
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
252B: E8 FF

; Room 127
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
252D: E8 FF

; Room 128
; [YOU ARE] IN A NARROW TUNNEL.
252F: 22 64 28 78 FF

; Room 129
; [YOU ARE] IN A SMALL CHAMBER WITH A SMOOTH MARBLE WALL.
2534: 22 64 1D 5C 38 64 79 7A 0C FF

; Room 130
; [YOU ARE] IN A GREAT HALL WITH A POOL OF WATER IN THE
; CORNER.
253E: 22 64 29 37 38 64 2C 67 2D 22 35 0F FF

; Room 131
; [YOU ARE] IN A STONE CORRIDOR.
254B: 22 64 2A 11 FF

; Room 132
; [YOU ARE] IN A DAMP TUNNEL WITH A PATH OF TRACKS WHICH
; DISAPPEARS INTO MIST ON THE EAST WALL.
2550: 22 64 63 78 38 64 CD 67 E9 C5 97 95 6B 34 35 04 0C FF

; Room 133
; [YOU ARE] ON THE WEST EDGE OF A DEEP PIT FILLED WITH MIST.
2562: 34 35 03 70 67 64 EA 6D 36 38 6B FF

; Room 134
; [YOU ARE] IN A DEAD END CHAMBER.
256E: 22 64 76 77 5C FF

; Room 135
; [YOU ARE] IN A SMALL CAVE FILLED WITH MINOTAUR TRACKS.
2574: 22 64 1D 69 36 38 7F E9 FF

; Room 136
; [YOU ARE] IN A SMALL CAVERN.
257D: 22 64 1D 68 FF

; Room 137
; [YOU ARE] IN A GREAT STONE TUNNEL.
2582: 22 64 29 2A 78 FF

; Room 138
; [YOU ARE] IN A DARK CHAMBER.
2588: 22 64 15 5C FF

; Room 139
; [YOU ARE] IN A TWISTING WINDING NARROW TUNNEL.
258D: 22 64 2E 6F 28 78 FF

; Room 140
; [YOU ARE] IN A WINDING NARROW TWISTING TUNNEL.
2594: 22 64 6F 28 2E 78 FF

; Room 141
; [YOU ARE] IN A NARROW TWISTING WINDING TUNNEL.
259B: 22 64 28 2E 6F 78 FF

; Room 142
; [YOU ARE] IN A MUSTY CHAMBER WITH A PILE OF BONES
; EVERYWHERE.
25A2: 22 64 4A 5C 38 64 3E 67 3F 73 FF

; Room 143
; [YOU ARE] IN A SMALL CAVE ON THE NORTH SIDE OF A DEEP PIT.
25AD: 22 64 1D 69 34 35 01 D1 67 64 EA 6D FF

; Room 144
; [YOU ARE] ON A HIGH NARROW PATH AND THERE IS MIST
; EVERYWHERE.
25BA: 34 64 0D 28 CD 2F 30 8C 6B 73 FF

; Room 145
; [YOU ARE] IN A FOUL SMELLING MUSTY PASSAGE.
25C5: 22 64 7B 7C 4A 1B FF

; Room 146
; [YOU ARE] IN A NARROW TUNNEL WITH MIST FLOWING DOWN THE
; WALL.
25CC: 22 64 28 78 38 6B 7D 06 35 0C FF

; Room 147
; [YOU ARE] IN A NARROW TWISTING CORRIDOR.
25D7: 22 64 28 2E 11 FF

; Room 148
; [YOU ARE] IN A TWISTING WINDING TUNNEL.
25DD: 22 64 2E 6F 78 FF

; Room 149
; [YOU ARE] IN A NARROW WINDING TWISTING TUNNEL.
25E3: 22 64 28 6F 2E 78 FF

; Room 150
; [YOU ARE] IN THE LAIR OF THE DEAD.
25EA: 22 35 7E 67 35 76 FF

; Room 151
; [YOU ARE] IN A TWISTING HALL WAY ON THE SOUTH SIDE OF A DEEP
; PIT.
25F1: 22 64 2E 37 1C 34 35 02 D1 67 64 EA 6D FF

; Room 152
; [YOU ARE] IN A GREAT TUNNEL.
25FF: 22 64 29 78 FF

; Room 153
; [YOU ARE] IN A LARGE CAVERN.
2604: 22 64 1E 68 FF

; Room 154
; [YOU ARE] IN A GREAT STONE HALL WAY.
2609: 22 64 29 2A 37 1C FF

; Room 155
; [YOU ARE] IN A WIDE TWISTING CORRIDOR.
2610: 22 64 1A 2E 11 FF

; Room 156
; [YOU ARE] IN A LARGE CAVERN WITH BONES EVERYWHERE.
2616: 22 64 1E 68 38 3F 73 FF

; Room 157
; [YOU ARE] IN A WINDING TWISTING NARROW TUNNEL.
261E: 22 64 6F 2E 28 78 FF

; Room 158
; [YOU ARE] IN THE LAIR OF THE MINOTAUR.
2625: 22 35 7E 67 35 7F FF

; Room 159
; [YOU ARE] ON A GENTLY SLOPING TRAIL.
262C: 34 64 9C 9D 90 FF

; Room 160
; [YOU ARE] IN A GREAT TUNNEL WITH BROKEN BONES EVERYWHERE.
2632: 22 64 29 78 38 4D 3F 73 FF

; Room 161
; [YOU ARE] IN A LARGE STONE CHAMBER.
263B: 22 64 1E 2A 5C FF

; Room 162
; [YOU ARE] IN A HALL WITH A LARGE STONE CROSS IN THE CENTER.
2641: 22 64 37 38 64 1E 2A 1F 22 35 10 FF

; Room 163
; [YOU ARE] IN A LARGE WIDE CAVERN.
264D: 22 64 1E 1A 68 FF

; Room 164
; [YOU ARE] ON A NARROW PATH OVERLOOKING A GREAT PIT.
2653: 34 64 28 CD 80 64 29 6D FF

; Room 165
; [YOU ARE] AT THE EDGE OF A GREAT BURIED TEMPLE.
265C: 92 35 70 67 64 29 DC E6 FF

; Room 166
; [YOU ARE] IN A SHALLOW DARK CAVERN.
2665: 22 64 0B 15 68 FF

; Room 167
; [YOU ARE] IN A GREAT CAVERN FILLED WITH MIST.
266B: 22 64 29 68 36 38 6B FF

; Room 168
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2673: E8 FF

; Room 169
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2675: E8 FF

; Room 170
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2677: E8 FF

; Room 171
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2679: E8 FF

; Room 172
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
267B: E8 FF

; Room 173
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
267D: E8 FF

; Room 174
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
267F: E8 FF

; Room 175
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2681: E8 FF

; Room 176
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2683: E8 FF

; Room 177
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2685: E8 FF

; Room 178
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2687: E8 FF

; Room 179
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2689: E8 FF

; Room 180
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
268B: E8 FF

; Room 181
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
268D: E8 FF

; Room 182
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
268F: E8 FF

; Room 183
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2691: E8 FF

; Room 184
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2693: E8 FF

; Room 185
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2695: E8 FF

; Room 186
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2697: E8 FF

; Room 187
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2699: E8 FF

; Room 188
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
269B: E8 FF

; Room 189
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
269D: E8 FF

; Room 190
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
269F: E8 FF

; Room 191
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26A1: E8 FF

; Room 192
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26A3: E8 FF

; Room 193
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26A5: E8 FF

; Room 194
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26A7: E8 FF

; Room 195
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26A9: E8 FF

; Room 196
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26AB: E8 FF

; Room 197
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26AD: E8 FF

; Room 198
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26AF: E8 FF

; Room 199
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26B1: E8 FF

; Room 200
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26B3: E8 FF

; Room 201
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26B5: E8 FF

; Room 202
; [YOU ARE] NEAR A GREAT FOREST.
26B7: E2 64 29 B9 FF

; Room 203
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26BC: E8 FF

; Room 204
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26BE: E8 FF

; Room 205
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26C0: E8 FF

; Room 206
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26C2: E8 FF

; Room 207
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26C4: E8 FF

; Room 208
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26C6: E8 FF

; Room 209
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26C8: E8 FF

; Room 210
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26CA: E8 FF

; Room 211
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26CC: E8 FF

; Room 212
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26CE: E8 FF

; Room 213
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26D0: E8 FF

; Room 214
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26D2: E8 FF

; Room 215
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26D4: E8 FF

; Room 216
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26D6: E8 FF

; Room 217
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26D8: E8 FF

; Room 218
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26DA: E8 FF

; Room 219
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26DC: E8 FF

; Room 220
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26DE: E8 FF

; Room 221
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26E0: E8 FF

; Room 222
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26E2: E8 FF

; Room 223
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26E4: E8 FF

; Room 224
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26E6: E8 FF

; Room 225
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26E8: E8 FF

; Room 226
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26EA: E8 FF

; Room 227
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26EC: E8 FF

; Room 228
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26EE: E8 FF

; Room 229
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26F0: E8 FF

; Room 230
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26F2: E8 FF

; Room 231
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26F4: E8 FF

; Room 232
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26F6: E8 FF

; Room 233
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26F8: E8 FF

; Room 234
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26FA: E8 FF

; Room 235
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26FC: E8 FF

; Room 236
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
26FE: E8 FF

; Room 237
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2700: E8 FF

; Room 238
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2702: E8 FF

; Room 239
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2704: E8 FF

; Room 240
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2706: E8 FF

; Room 241
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2708: E8 FF

; Room 242
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
270A: E8 FF

; Room 243
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
270C: E8 FF

; Room 244
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
270E: E8 FF

; Room 245
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2710: E8 FF

; Room 246
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2712: E8 FF

; Room 247
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2714: E8 FF

; Room 248
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2716: E8 FF

; Room 249
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2718: E8 FF

; Room 250
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
271A: E8 FF

; Room 251
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
271C: E8 FF

; Room 252
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
271E: E8 FF

; Room 253
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2720: E8 FF

; Room 254
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2722: E8 FF

; Room 255
; [YOU ARE] IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN
; ALL DIRECTIONS.
2724: E8 FF
```

## Command Words 

```code
CommandWords:
2726:  D5  ; 0 "U"
2727:  C4  ; 1 "D"
2728:  CE  ; 2 "N"
2729:  C5  ; 3 "E"
272A:  D7  ; 4 "W"
272B:  D3  ; 5 "S"
272C:  55 D0  ; 6 "UP"
272E:  44 4F 57 CE  ; 7 "DOWN"
2732:  4E 4F 52 54 C8  ; 8 "NORTH"
2737:  45 41 53 D4  ; 9 "EAST"
273B:  57 45 53 D4  ; 10 "WEST"
273F:  53 4F 55 54 C8  ; 11 "SOUTH"
2744:  47 45 D4  ; 12 "GET"
2747:  49 4E D6  ; 13 "INV"
274A:  44 52 4F D0  ; 14 "DROP"
274E:  42 41 43 CB  ; 15 "BACK"
2752:  4A 55 4D D0  ; 16 "JUMP"
2756:  4C 41 4D D0  ; 17 "LAMP"
275A:  44 52 49 4E CB  ; 18 "DRINK"
275F:  45 41 D4  ; 19 "EAT"
2762:  46 49 4C CC  ; 20 "FILL"
2766:  41 53 CB  ; 21 "ASK"
2769:  4C 4F 4F CB  ; 22 "LOOK"
276D:  53 43 4F 52 C5  ; 23 "SCORE"
2772:  4B 49 4C CC  ; 24 "KILL"
2776:  52 55 CE  ; 25 "RUN"
2779:  4F 50 45 CE  ; 26 "OPEN"
277D:  48 45 4C D0  ; 27 "HELP"
2781:  43 4C 49 4D C2  ; 28 "CLIMB"
2786:  54 49 C5  ; 29 "TIE"
2789:  53 54 41 C2  ; 30 "STAB"
278D:  56 45 54 41 D2  ; 31 "VETAR"
2792:  4D 49 54 52 C1  ; 32 "MITRA"
2797:  4F 4B 4B 41 CE  ; 33 "OKKAN"
279C:  41 4B 48 49 52 4F CD  ; 34 "AKHIROM"
27A3:  4E 45 52 47 41 CC  ; 35 "NERGAL"
27A9:  42 45 4C 52 4F C7  ; 36 "BELROG"
27AF:  43 52 4F CD  ; 37 "CROM"
27B3:  49 53 48 54 41 D2  ; 38 "ISHTAR"
27B9:  50 4C 41 D9  ; 39 "PLAY"
27BD:  54 48 52 4F D7  ; 40 "THROW"
27C2:  54 41 4B C5  ; 41 "TAKE"
27C6:  47 52 41 C2  ; 42 "GRAB"
27CA:  51 55 49 45 D4  ; 43 "QUIET"
27CF:  55 4E 43 4C C5  ; 44 "UNCLE"

CommandTable:
; Pointers to commands
27D4: 0D ED  ; U
27D6: 0D F0  ; D
27D8: 0D F3  ; N
27DA: 0D F6  ; E
27DC: 0D F9  ; W
27DE: 0D FC  ; S
27E0: 0D ED  ; UP
27E2: 0D F0  ; DOWN
27E4: 0D F3  ; NORTH
27E6: 0D F6  ; EAST
27E8: 0D F9  ; WEST
27EA: 0D FC  ; SOUTH
27EC: 18 F7  ; GET
27EE: 18 4A  ; INV
27F0: 10 BE  ; DROP
27F2: 0D DD  ; BACK
27F4: 19 AC  ; JUMP
27F6: 1A A6  ; LAMP
27F8: 12 DB  ; DRINK
27FA: 12 45  ; EAT
27FC: 15 02  ; FILL
27FE: 11 B6  ; ASK
2800: 15 CE  ; LOOK
2802: 16 F8  ; SCORE
2804: 17 7C  ; KILL
2806: 14 D4  ; RUN
2808: 11 3E  ; OPEN
280A: 13 A9  ; HELP
280C: 13 59  ; CLIMB
280E: 13 77  ; TIE
2810: 13 AF  ; STAB
2812: 14 12  ; VETAR
2814: 14 26  ; MITRA
2816: 14 32  ; OKKAN
2818: 14 66  ; AKHIROM
281A: 14 87  ; NERGAL
281C: 14 96  ; BELROG
281E: 14 A7  ; CROM
2820: 14 C0  ; ISHTAR
2822: 16 7B  ; PLAY
2824: 10 BE  ; THROW
2826: 18 F7  ; TAKE
2828: 18 F7  ; GRAB
282A: 17 3F  ; QUIET
282C: 0D 5C  ; UNCLE
```

## Passage Descriptions 
 Descriptions of all the passages out of a room ... the one used is random

```code
PassageDescriptions:

; Message 0
; A SMALL OPENING WINDS OUT OF SIGHT TO THE
; SOUTH.
282E: 64 1D 9A 99 9E 67 96 84 35 02 FF

; Message 1
; A GREAT DOORWAY IS ON THE SOUTH WALL.
2839: 64 29 00 8C 34 35 02 0C FF

; Message 2
; A GENTLY SLOPING TRAIL WINDS SOUTH.
2842: 64 9C 9D 90 99 02 FF

; Message 3
; THERE IS A PASSAGE WAY TO THE SOUTH.
2849: 30 8C 64 1B 1C 84 35 02 FF

; Message 4
; A LARGE DOORWAY IS RECESSED INTO THE SOUTH WALL.
2852: 64 1E 00 8C A0 95 35 02 0C FF

; Message 5
; A DOORWAY TO THE SOUTH WINDS INTO A CHAMBER.
285C: 64 00 84 35 02 99 95 64 5C FF

; Message 6
; A SLOPING PASSAGE LEADS TO THE SOUTH.
2866: 64 9D 1B 98 84 35 02 FF

; Message 7
; A WINDING PASSAGE DISAPPEARS TO THE SOUTH.
286E: 64 6F 1B 97 84 35 02 FF

; Message 8
; A GREAT DOORWAY IS ON THE WEST WALL.
2876: 64 29 00 8C 34 35 03 0C FF

; Message 9
; THERE IS A NARROW PASSAGE WAY TO THE WEST.
287F: 30 8C 64 28 1B 1C 84 35 03 FF

; Message 10
; THERE IS A PASSAGE WAY TO THE WEST.
2889: 30 8C 64 1B 1C 84 35 03 FF

; Message 11
; A BROKEN TRAIL LEADS WEST.
2892: 64 4D 90 98 03 FF

; Message 12
; A DOORWAY TO THE WEST WINDS INTO A CHAMBER.
2898: 64 00 84 35 03 99 95 64 5C FF

; Message 13
; SWIRLING MIST WINDS OUT OF A DOORWAY TO THE WEST.
28A2: 6C 6B 99 9E 67 64 00 84 35 03 FF

; Message 14
; A WINDING PASSAGE DISAPPEARS TO THE WEST.
28AD: 64 6F 1B 97 84 35 03 FF

; Message 15
; A TWISTING TRAIL LEADS WEST.
28B5: 64 2E 90 98 03 FF

; Message 16
; THERE IS A NARROW PASSAGE WAY TO THE EAST.
28BB: 30 8C 64 28 1B 1C 84 35 04 FF

; Message 17
; THERE IS A GREAT HOLE IN THE EAST WALL.
28C5: 30 8C 64 29 9F 22 35 04 0C FF

; Message 18
; A BROKEN TRAIL LEADS EAST.
28CF: 64 4D 90 98 04 FF

; Message 19
; A WIDE OPENING ON THE EAST WALL DISAPPEARS INTO THE DARK.
28D5: 64 1A 9A 34 35 04 0C 97 95 35 15 FF

; Message 20
; SWIRLING MIST WINDS OUT OF A DOORWAY TO THE EAST.
28E1: 6C 6B 99 9E 67 64 00 84 35 04 FF

; Message 21
; A GREAT HALL DISAPPEARS TO THE EAST.
28EC: 64 29 37 97 84 35 04 FF

; Message 22
; A TWISTING TRAIL LEADS EAST.
28F4: 64 2E 90 98 04 FF

; Message 23
; A SUNKEN TRAIL LEADS EAST.
28FA: 64 6E 90 98 04 FF

; Message 24
; A SMALL OPENING WINDS OUT OF SIGHT TO THE NORTH.
2900: 64 1D 9A 99 9E 67 96 84 35 01 FF

; Message 25
; THERE IS A GREAT HOLE IN THE NORTH WALL.
290B: 30 8C 64 29 9F 22 35 01 0C FF

; Message 26
; A GENTLY SLOPING TRAIL WINDS NORTH.
2915: 64 9C 9D 90 99 01 FF

; Message 27
; A WIDE OPENING ON THE NORTH WALL DISAPPEARS INTO THE DARK.
291C: 64 1A 9A 34 35 01 0C 97 95 35 15 FF

; Message 28
; A LARGE DOORWAY IS RECESSED INTO THE NORTH WALL.
2928: 64 1E 00 8C A0 95 35 01 0C FF

; Message 29
; A GREAT HALL DISAPPEARS TO THE NORTH.
2932: 64 29 37 97 84 35 01 FF

; Message 30
; A SLOPING PASSAGE LEADS TO THE NORTH.
293A: 64 9D 1B 98 84 35 01 FF

; Message 31
; A SUNKEN TRAIL LEADS NORTH.
2942: 64 6E 90 98 01 FF

; Message 32
; A SWIRLING MIST WINDS UP A STAIR WAY.
2948: 64 6C 6B 99 05 64 61 1C FF

; Message 33
; THERE IS A HOLE IN THE FLOOR.
2951: 30 8C 64 9F 22 35 40 FF

; Message 34
; THERE IS A LARGE OPENING IN THE FLOOR.
2959: 30 8C 64 1E 9A 22 35 40 FF

; Message 35
; A LARGE OPENING LEADS DOWN.
2962: 64 1E 9A 98 06 FF

; Message 36
; YOU ARE AT THE TOP OF A TWISTING STAIR WAY.
2968: 9B 31 92 35 A2 67 64 2E 61 1C FF

; Message 37
; A STAIR WAY LEADS DOWN.
2973: 64 61 1C 98 06 FF

; Message 38
; YOU ARE AT THE TOP OF A PIT.
2979: 9B 31 92 35 A2 67 64 6D FF

; Message 39
; A TWISTING TRAIL LEADS DOWN.
2982: 64 2E 90 98 06 FF

; Message 40
; A SWIRLING MIST WINDS DOWN A STAIR WAY.
2988: 64 6C 6B 99 06 64 61 1C FF

; Message 41
; THERE IS A HOLE IN THE CEILING.
2991: 30 8C 64 9F 22 35 0A FF

; Message 42
; THERE IS A LARGE OPENING IN THE CEILING.
2999: 30 8C 64 1E 9A 22 35 0A FF

; Message 43
; A LARGE OPENING LEADS UP.
29A2: 64 1E 9A 98 05 FF

; Message 44
; YOU ARE AT THE BOTTOM OF A TWISTING STAIR WAY.
29A8: 9B 31 92 35 A1 67 64 2E 61 1C FF

; Message 45
; A STAIR WAY LEADS UP.
29B3: 64 61 1C 98 05 FF

; Message 46
; YOU ARE AT THE BOTTOM OF A PIT.
29B9: 9B 31 92 35 A1 67 64 6D FF

; Message 47
; A TWISTING TRAIL LEADS UP.
29C2: 64 2E 90 98 05 FF
```

## Misc Strings 

```code
MiscStrings:
; Misc Strings

; Message 0
; BUT IT IS BLOCKED.
29C8: 07 D2 8C 09 FF

; Message 1
; THE LAMP IS OFF.
29CD: 35 A6 8C 8F FF

; Message 2
; THE LAMP IS ON.
29D2: 35 A6 8C 34 FF

; Message 3
; THE MINOTAUR IS ATTACKING.
29D7: 35 7F 8C F0 FF

; Message 4
; THE TROGLODYTE IS ATTACKING.
29DC: 35 BB 8C F0 FF

; Message 5
; THE SATYR IS ATTACKING.
29E1: 35 AD 8C F0 FF

; Message 6
; THERE IS NO OIL IN THE LAMP.
29E6: 30 8C 44 F1 22 35 A6 FF

; Message 7
; THE ROOM IS FILLED WITH MIST AND THE ORACLE DISAPPEARS.
29EE: 35 3C 8C 36 38 6B 2F 35 AE 97 FF

; Message 8
; THERE IS NOTHING IN THE URN.
29F9: 30 8C 93 22 35 A9 FF

; Message 9
; THE URN IS FILLED WITH OIL.
2A00: 35 A9 8C 36 38 F1 FF

; Message 10
; THE SCORPION DISAPPEARS.
2A07: 35 AB 97 FF

; Message 11
; THE BOTTLE IS EMPTY.
2A0B: 35 B8 8C 47 FF

; Message 12
; THE BOTTLE IS FILLED WITH WATER.
2A10: 35 B8 8C 36 38 2D FF

; Message 13
; YOU CAN NOT SEE IN THE DIM LIGHT.
2A17: 9B DE D5 62 22 35 CC 14 FF

; Message 14
; THE BOTTLE IS EMPTY.
2A20: 35 B8 8C 47 FF

; Message 15
; THERE IS A SMALL PIT IN THE CORNER OF THE ROOM.
2A25: 30 8C 64 1D 6D 22 35 0F 67 35 3C FF

; Message 16
; THERE IS A POOL OF OIL ON THE FLOOR.
2A31: 30 08 2C 67 F1 34 35 40 FF

CodeBug5:
; This message is only used for "THERE IS NO WATER HERE." The
; word "WATER" was left out.
; Message 17
; THERE IS NO HERE.
2A3A: 30 8C 44 85 FF

; Message 18
; THE SCARAB IS GLOWING.
2A3F: 35 C7 8C EF FF

; Message 19
; YOUR SIGHT IS DIM.
2A44: 91 96 8C CC FF
```

## Phrase List 

```code
PhraseList:
2A49:  49 20 44 4F 20 4E 4F 54 20 53 45 45 20 41 4E D9  ; 0 "I DO NOT SEE ANY"
2A59:  49 54 27 53 20 54 4F 4F 20 42 55 4C 4B 59 2E 8D  ; 1 "IT'S TOO BULKY.*"
2A69:  49 54 27 53 20 54 4F 4F 20 48 45 41 56 59 2E 8D  ; 2 "IT'S TOO HEAVY.*"
2A79:  4F 4B 8D  ; 3 "OK*"
2A7C:  45 52 52 4F D2  ; 4 "ERROR"
2A81:  00 0D 49 20 44 4F 4E 27 54 20 55 4E 44 45 52 53 54 41 4E 44 20 54 48 41 54 AE  ; 5 "**I DON'T UNDERSTAND THAT."
2A9B:  59 4F 55 20 41 52 45 20 48 4F 4C 44 49 4E 47 BA  ; 6 "YOU ARE HOLDING:"
2AAB:  59 4F 55 20 44 4F 4E 27 54 20 48 41 56 45 20 54 48 41 54 2E 8D  ; 7 "YOU DON'T HAVE THAT.*"
2AC0:  44 4F 4E 27 54 20 42 45 20 52 49 44 49 43 55 4C 4F 55 53 2E 8D  ; 8 "DON'T BE RIDICULOUS.*"
2AD5:  08 AE  ; 9 "*."
2AD7:  57 45 4C 43 4F 4D 45 20 54 4F 20 54 48 45 20 4C 41 42 59 52 49 4E 54 48 21 21 20 42 45 57 41 52 45 20 4F 46 20 54 48 45 20 4D 49 4E 4F 54 41 55 52 20 41 4E 44 20 47 4F 4F 44 20 4C 55 43 4B AE  ; 10 "WELCOME TO THE LABYRINTH!! BEWARE OF THE MINOTAUR AND GOOD LUCK."
2B17:  59 4F 55 20 44 52 4F 50 50 45 44 20 54 48 C5  ; 11 "YOU DROPPED THE"
2B26:  49 54 27 53 20 44 41 52 4B 20 41 4E 44 20 59 4F 55 20 43 41 4E 27 54 20 53 45 45 20 2D 20 49 46 20 59 4F 55 20 43 4F 4E 54 49 4E 55 45 2C 20 59 4F 55 20 4D 41 59 20 46 41 4C 4C AE  ; 12 "IT'S DARK AND YOU CAN'T SEE - IF YOU CONTINUE, YOU MAY FALL."
2B62:  59 4F 55 20 48 41 56 45 20 4A 55 53 54 20 46 41 4C 4C 45 4E 20 49 4E 54 4F 20 41 20 50 49 54 20 41 4E 44 20 4B 49 4C 4C 45 44 20 59 4F 55 52 53 45 4C 46 2E 8D  ; 13 "YOU HAVE JUST FALLEN INTO A PIT AND KILLED YOURSELF.*"
2B97:  0D 59 4F 55 52 20 4C 41 4D 50 20 48 41 53 20 4A 55 53 54 20 47 4F 4E 45 20 4F 46 46 2E 8D  ; 14 "*YOUR LAMP HAS JUST GONE OFF.*"
2BB5:  41 53 4B 20 57 48 4F BF  ; 15 "ASK WHO?"
2BBD:  41 20 4D 59 53 54 45 52 49 4F 55 53 20 43 41 4C 4D 20 53 45 54 54 4C 45 53 20 4F 56 45 52 20 54 48 45 20 52 4F 4F 4D 20 41 53 20 54 48 45 20 4F 52 41 43 4C 45 20 53 50 45 41 4B 53 2E 2E AE  ; 16 "A MYSTERIOUS CALM SETTLES OVER THE ROOM AS THE ORACLE SPEAKS..."
2BFC:  59 4F 55 20 4D 55 53 54 20 50 4F 53 53 45 53 53 20 54 48 C5  ; 17 "YOU MUST POSSESS THE"
2C10:  54 48 41 4E 4B 20 59 4F 55 2C 20 49 20 4E 45 45 44 45 44 20 54 48 41 54 2E 8D  ; 18 "THANK YOU, I NEEDED THAT.*"
2C2A:  49 54 20 57 41 53 20 59 55 4D 4D 59 2E 8D  ; 19 "IT WAS YUMMY.*"
2C38:  54 48 45 20 53 43 4F 52 50 49 4F 4E 27 53 20 53 54 49 4E 47 20 48 41 53 20 42 45 45 4E 20 43 55 52 45 44 2E 8D  ; 20 "THE SCORPION'S STING HAS BEEN CURED.*"
2C5D:  54 48 41 54 20 49 53 20 56 45 52 59 20 53 54 52 4F 4E 47 20 4D 45 44 49 43 49 4E 45 2E 8D  ; 21 "THAT IS VERY STRONG MEDICINE.*"
2C7B:  57 49 54 48 20 57 48 41 54 BF  ; 22 "WITH WHAT?"
2C85:  49 20 44 4F 4E 27 54 20 53 45 45 20 41 4E 59 54 48 49 4E 47 20 49 4E 54 45 52 45 53 54 49 4E 47 2E 8D  ; 23 "I DON'T SEE ANYTHING INTERESTING.*"
2CA7:  54 4F 20 4C 45 41 52 4E 20 54 48 45 20 53 45 43 52 45 54 20 4F 46 20 54 48 C5  ; 24 "TO LEARN THE SECRET OF THE"
2CC1:  49 4E 20 41 20 52 45 46 4C 45 43 54 49 4F 4E 20 49 4E 20 54 48 45 20 50 4F 4F 4C 20 59 4F 55 20 43 41 4E 20 52 45 41 44 20 54 48 45 20 46 4F 4C 4C 4F 57 49 4E 47 20 57 4F 52 44 53 20 4F 4E 20 54 48 45 20 43 45 49 4C 49 4E 47 2E 2E AE  ; 25 "IN A REFLECTION IN THE POOL YOU CAN READ THE FOLLOWING WORDS ON THE CEILING..."
2D0F:  54 48 45 20 55 52 4E 20 49 53 20 46 55 4C 4C 20 4F 46 20 4F 49 4C 2E 8D  ; 26 "THE URN IS FULL OF OIL.*"
2D27:  59 4F 55 20 48 41 56 45 20 53 43 4F 52 45 C4  ; 27 "YOU HAVE SCORED"
2D36:  20 50 4F 49 4E 54 53 20 4F 55 54 20 4F 46 20 41 20 54 4F 54 41 4C 20 4F 46 20 32 34 30 20 50 4F 49 4E 54 53 2E 0D 50 48 59 53 20 43 4F 4E 44 20 3D A0  ; 28 " POINTS OUT OF A TOTAL OF 240 POINTS.*PHYS COND = "
2D68:  54 48 45 20 46 4C 4F 4F 52 20 55 4E 44 45 52 20 59 4F 55 20 48 41 53 20 4A 55 53 54 20 43 41 56 45 44 20 49 4E 21 21 8D  ; 29 "THE FLOOR UNDER YOU HAS JUST CAVED IN!!*"
2D90:  59 4F 55 20 44 4F 4E 27 54 20 48 41 56 45 20 54 48 45 20 4C 41 4D 50 2E 8D  ; 30 "YOU DON'T HAVE THE LAMP.*"
2DA9:  49 4E 20 48 49 53 20 44 59 49 4E 47 20 45 46 46 4F 52 54 20 54 48 C5  ; 31 "IN HIS DYING EFFORT THE"
2DC0:  50 55 4C 4C 53 20 54 48 C5  ; 32 "PULLS THE"
2DC9:  46 52 4F 4D 20 41 20 42 41 47 20 41 4E 44 20 54 48 52 4F 57 53 20 49 54 20 42 45 46 4F 52 45 20 48 45 20 44 49 53 41 50 50 45 41 52 53 20 49 4E 20 41 20 50 55 46 46 20 4F 46 20 50 55 52 50 4C 45 20 53 4D 4F 4B 45 AE  ; 33 "FROM A BAG AND THROWS IT BEFORE HE DISAPPEARS IN A PUFF OF PURPLE SMOKE."
2E11:  59 4F 55 20 4D 49 53 53 45 44 2E 8D  ; 34 "YOU MISSED.*"
2E1D:  59 4F 55 20 4E 4F 57 20 4B 4E 4F 57 20 54 48 45 20 53 45 43 52 45 54 20 4F 46 20 54 48 45 20 4D 41 47 49 43 20 53 50 45 4C CC  ; 35 "YOU NOW KNOW THE SECRET OF THE MAGIC SPELL"
2E47:  2D 20 59 4F 55 20 57 49 4C 4C 20 44 49 53 43 4F 56 45 52 20 54 48 45 20 53 45 43 52 45 54 20 4F 46 20 54 48 45 20 4E 45 58 54 20 53 50 45 4C 4C 20 49 46 20 59 4F 55 20 50 4F 53 53 45 53 53 20 54 48 C5  ; 36 "- YOU WILL DISCOVER THE SECRET OF THE NEXT SPELL IF YOU POSSESS THE"
2E8A:  54 48 45 20 47 52 4F 55 4E 44 20 49 53 20 53 48 41 4B 49 4E 47 21 8D  ; 37 "THE GROUND IS SHAKING!*"
2EA1:  54 48 45 20 54 4F 50 20 57 4F 4E 27 54 20 42 55 44 47 45 2E 8D  ; 38 "THE TOP WON'T BUDGE.*"
2EB6:  41 20 43 4C 4F 55 44 20 4F 46 20 53 4D 4F 4B 45 20 46 49 4C 4C 53 20 54 48 45 20 52 4F 4F 4D 20 41 4E 44 20 41 4E 20 45 45 52 49 45 20 48 4F 57 4C 20 45 43 48 4F 53 20 4F 46 46 20 54 48 45 20 57 41 4C 4C 53 20 41 53 20 54 48 45 20 54 4F 50 20 46 41 4C 4C 53 20 53 48 55 54 2E 8D  ; 39 "A CLOUD OF SMOKE FILLS THE ROOM AND AN EERIE HOWL ECHOS OFF THE WALLS AS THE TOP FALLS SHUT.*"
2F13:  59 4F 55 20 48 41 56 45 20 53 54 55 4D 42 4C 45 44 20 41 4E 44 20 46 41 4C 4C 45 4E AE  ; 40 "YOU HAVE STUMBLED AND FALLEN."
2F30:  59 4F 55 20 48 41 56 45 20 44 49 45 44 20 46 52 4F 4D 20 45 58 48 41 55 53 54 49 4F 4E 20 41 4E 44 20 57 4F 55 4E 44 53 AE  ; 41 "YOU HAVE DIED FROM EXHAUSTION AND WOUNDS."
2F59:  41 20 44 55 4C 4C 2C 20 45 45 52 49 45 20 47 4C 4F 57 20 49 53 20 45 4D 41 4E 41 54 49 4E 47 20 46 52 4F 4D 20 42 45 48 49 4E 44 20 41 20 50 49 4C 45 20 4F 46 20 52 4F 43 4B 53 AE  ; 42 "A DULL, EERIE GLOW IS EMANATING FROM BEHIND A PILE OF ROCKS."
2F95:  42 59 20 50 4C 41 59 49 4E 47 20 54 48 45 20 46 4C 55 54 45 20 41 43 43 4F 52 44 49 4E 47 20 54 4F 20 41 20 53 4F 4E 47 20 4F 4E 20 54 48 45 20 50 41 52 43 48 4D 45 4E 54 2C 20 41 20 53 45 43 52 45 54 20 4C 45 44 47 45 20 48 41 53 20 42 45 45 4E 20 45 58 50 4F 53 45 44 2E 8D  ; 43 "BY PLAYING THE FLUTE ACCORDING TO A SONG ON THE PARCHMENT, A SECRET LEDGE HAS BEEN EXPOSED.*"
2FF1:  41 20 50 4F 57 45 52 46 55 4C 20 47 55 53 54 20 4F 46 20 57 49 4E 44 20 48 41 53 20 42 4C 4F 57 4E 20 54 48 45 20 4C 41 4D 50 20 4F 55 54 20 4F 46 20 59 4F 55 52 20 47 52 41 53 50 2E 8D  ; 44 "A POWERFUL GUST OF WIND HAS BLOWN THE LAMP OUT OF YOUR GRASP.*"
302F:  41 20 4E 49 4E 45 2D 48 45 41 44 45 44 20 48 59 44 52 41 20 42 4C 4F 43 4B 53 20 59 4F 55 52 20 50 41 53 53 41 47 45 2E 8D  ; 45 "A NINE-HEADED HYDRA BLOCKS YOUR PASSAGE.*"
3058:  41 20 4D 41 47 49 43 20 53 50 45 4C 4C 20 48 41 53 20 50 55 53 48 45 44 20 59 4F 55 20 42 41 43 4B 20 4F 55 54 20 4F 46 20 54 48 49 53 20 52 4F 4F 4D 2E 8D  ; 46 "A MAGIC SPELL HAS PUSHED YOU BACK OUT OF THIS ROOM.*"
308C:  4F 4E 45 20 4F 46 20 54 48 45 20 48 59 44 52 41 27 53 20 48 45 41 44 53 20 49 53 20 4C 4F 50 50 45 44 20 4F 46 46 2C 20 42 55 54 20 41 4E 4F 54 48 45 52 20 4F 4E 45 20 54 41 4B 45 53 20 49 54 53 20 50 4C 41 43 45 20 41 4E 44 20 53 4E 45 45 52 53 20 41 54 20 59 4F 55 2E 8D  ; 47 "ONE OF THE HYDRA'S HEADS IS LOPPED OFF, BUT ANOTHER ONE TAKES ITS PLACE AND SNEERS AT YOU.*"
30E7:  41 20 56 45 52 59 20 50 4F 57 45 52 46 55 4C 20 4D 41 47 49 43 20 46 4F 52 43 45 20 53 54 52 49 4B 45 53 20 59 4F 55 20 41 4E 44 20 44 52 49 56 45 53 20 59 4F 55 20 42 41 43 4B 2E 8D  ; 48 "A VERY POWERFUL MAGIC FORCE STRIKES YOU AND DRIVES YOU BACK.*"
3124:  41 20 4D 59 53 54 45 52 49 4F 55 53 20 46 4F 47 20 42 45 47 49 4E 53 20 52 49 53 49 4E 47 20 46 52 4F 4D 20 54 48 45 20 46 4C 4F 4F 52 21 8D  ; 49 "A MYSTERIOUS FOG BEGINS RISING FROM THE FLOOR!*"
3153:  54 48 45 20 50 4F 49 53 4F 4E 20 46 4F 47 20 48 41 53 20 4B 49 4C 4C 45 44 20 59 4F 55 21 8D  ; 50 "THE POISON FOG HAS KILLED YOU!*"
3172:  49 54 27 53 20 50 4F 49 53 4F 4E 4F 55 53 21 21 8D  ; 51 "IT'S POISONOUS!!*"
3183:  41 20 4C 41 59 45 52 20 4F 46 20 4D 49 53 54 20 4F 42 53 43 55 52 45 53 20 54 48 45 20 45 41 53 54 20 57 41 4C 4C 2E 8D  ; 52 "A LAYER OF MIST OBSCURES THE EAST WALL.*"
31AB:  54 48 45 20 4C 49 47 48 54 20 47 52 4F 57 53 20 53 54 52 4F 4E 47 45 52 20 55 4E 54 49 4C 20 54 48 45 20 45 4E 54 49 52 45 20 52 4F 4F 4D 20 49 53 20 42 41 54 48 45 44 20 49 4E 20 49 54 53 20 47 4C 4F 57 2E 8D  ; 53 "THE LIGHT GROWS STRONGER UNTIL THE ENTIRE ROOM IS BATHED IN ITS GLOW.*"
31F1:  4E 4F 54 48 49 4E 47 20 53 50 45 43 49 41 4C 20 48 41 50 50 45 4E 53 2E 8D  ; 54 "NOTHING SPECIAL HAPPENS.*"
320A:  41 20 56 45 52 59 20 4D 41 44 20 48 59 44 52 41 20 49 53 20 54 49 45 44 20 55 50 20 48 45 52 45 2E 8D  ; 55 "A VERY MAD HYDRA IS TIED UP HERE.*"
322C:  41 4E 20 45 45 52 49 45 20 50 48 4F 53 50 48 4F 52 45 53 43 45 4E 54 20 47 4C 4F 57 20 46 49 4C 4C 53 20 54 48 45 20 45 4E 54 49 52 45 20 52 4F 4F 4D 21 8D  ; 56 "AN EERIE PHOSPHORESCENT GLOW FILLS THE ENTIRE ROOM!*"
3260:  44 4F 4E 27 54 20 41 53 4B 20 4D 45 20 46 4F 52 20 48 45 4C 50 20 2D 20 59 4F 55 20 47 4F 54 20 59 4F 55 52 53 45 4C 46 20 49 4E 54 4F 20 54 48 49 53 20 4D 45 53 53 21 8D  ; 57 "DON'T ASK ME FOR HELP - YOU GOT YOURSELF INTO THIS MESS!*"
3299:  59 4F 55 20 48 41 56 45 20 4A 55 53 54 20 57 41 4C 4B 45 44 20 54 48 52 4F 55 47 48 20 41 4E 20 45 4E 43 48 41 4E 54 45 44 20 41 55 52 41 2E 8D  ; 58 "YOU HAVE JUST WALKED THROUGH AN ENCHANTED AURA.*"
32C9:  54 48 45 20 41 49 52 20 49 53 20 43 52 41 43 4B 4C 49 4E 47 20 57 49 54 48 20 45 4E 43 48 41 4E 54 4D 45 4E 54 AE  ; 59 "THE AIR IS CRACKLING WITH ENCHANTMENT."
32EF:  54 48 45 20 4C 41 4D 50 20 49 53 20 46 4C 49 43 4B 45 52 49 4E 47 2E 8D  ; 60 "THE LAMP IS FLICKERING.*"
3307:  54 48 45 20 48 59 44 52 41 20 49 53 20 44 45 41 44 21 8D  ; 61 "THE HYDRA IS DEAD!*"
331A:  41 20 50 41 43 4B 52 41 54 20 53 43 55 52 52 49 45 53 20 49 4E 54 4F 20 41 20 53 4D 41 4C 4C 20 48 4F 4C 45 AE  ; 62 "A PACKRAT SCURRIES INTO A SMALL HOLE."
333F:  54 48 41 4E 4B 20 54 48 45 20 50 41 43 4B 52 41 54 20 46 4F 52 20 54 48 49 53 20 54 52 45 41 53 55 52 45 A1  ; 63 "THANK THE PACKRAT FOR THIS TREASURE!"
3363:  49 53 20 4E 4F 57 20 4C 41 59 49 4E 47 20 41 54 20 59 4F 55 52 20 46 45 45 54 21 8D  ; 64 "IS NOW LAYING AT YOUR FEET!*"
337F:  54 48 45 20 57 41 4C 4C 53 20 4F 46 20 54 48 49 53 20 52 4F 4F 4D 20 41 52 45 20 41 20 56 45 52 59 20 53 54 52 41 4E 47 45 20 43 4F 4C 4F 52 21 8D  ; 65 "THE WALLS OF THIS ROOM ARE A VERY STRANGE COLOR!*"
33B0:  59 4F 55 52 20 4A 55 4D 50 49 4E 47 20 41 42 49 4C 49 54 59 20 49 53 20 4E 4F 54 20 41 53 20 47 4F 4F 44 20 41 53 20 49 54 20 4F 4E 43 45 20 57 41 53 20 2D 20 59 4F 55 20 48 41 56 45 20 46 41 4C 4C 45 4E 20 41 4E 44 20 44 49 45 44 2E 8D  ; 66 "YOUR JUMPING ABILITY IS NOT AS GOOD AS IT ONCE WAS - YOU HAVE FALLEN AND DIED.*"
33FF:  43 4F 4E 47 52 41 54 55 4C 41 54 49 4F 4E 53 21 21 21 20 59 4F 55 20 57 49 4E 21 8D  ; 67 "CONGRATULATIONS!!! YOU WIN!*"
341B:  57 48 41 54 3F 8D  ; 68 "WHAT?*"
3421:  54 48 45 20 50 41 52 43 48 4D 45 4E 54 20 48 41 53 20 41 20 53 43 4F 52 45 20 4F 4E 20 49 54 AE  ; 69 "THE PARCHMENT HAS A SCORE ON IT."
3441:  41 20 42 4F 4C 54 20 4F 46 20 4C 49 47 48 54 4E 49 4E 47 20 55 4E 42 4C 4F 43 4B 53 20 54 48 45 20 50 41 53 53 41 47 45 21 21 21 8D  ; 70 "A BOLT OF LIGHTNING UNBLOCKS THE PASSAGE!!!*"
346D:  59 4F 55 20 4D 55 53 54 20 42 45 20 4B 49 44 44 49 4E 47 21 8D  ; 71 "YOU MUST BE KIDDING!*"
3482:  4F 55 43 48 21 21 20 54 48 41 54 20 48 55 52 54 2E 8D  ; 72 "OUCH!! THAT HURT.*"
3494:  54 48 45 20 53 43 4F 52 50 49 4F 4E 20 48 41 53 20 4A 55 53 54 20 53 54 55 4E 47 20 59 4F 55 AE  ; 73 "THE SCORPION HAS JUST STUNG YOU."
34B4:  59 4F 55 20 48 41 56 45 20 44 49 45 44 20 46 52 4F 4D 20 41 20 53 43 4F 52 50 49 4F 4E 20 42 49 54 45 2E 8D  ; 74 "YOU HAVE DIED FROM A SCORPION BITE.*"
34D8:  59 4F 55 20 50 55 54 20 55 50 20 41 20 47 4F 4F 44 20 46 49 47 48 54 2C 20 42 45 54 54 45 52 20 4C 55 43 4B 20 4E 45 58 54 20 54 49 4D 45 2E 8D  ; 75 "YOU PUT UP A GOOD FIGHT, BETTER LUCK NEXT TIME.*"
```

## Object Info 

```code
ObjectToNameMap:
; Object to name map
;
3508: FF ; 0 ""
3509: 94 ; 1 "FOOD"
350A: B8 ; 2 "BOTTLE"
350B: 26 ; 3 "DAGGER"
350C: C9 ; 4 "MACE"
350D: 5F ; 5 "AX"
350E: 52 ; 6 "SWORD"
350F: 53 ; 7 "SHIELD"
3510: 24 ; 8 "FLUTE"
3511: CA ; 9 "MUSHROOM"
3512: A4 ; 10 "PENDANT"
3513: A5 ; 11 "SCEPTER"
3514: A6 ; 12 "LAMP"
3515: 27 ; 13 "BASKET"
3516: A7 ; 14 "PARCHMENT"
3517: A8 ; 15 "VIAL"
3518: A9 ; 16 "URN"
3519: C1 ; 17 "TALISMAN"
351A: B7 ; 18 "SCROLL"
351B: C2 ; 19 "GOBLET"
351C: 66 ; 20 "SKULL"
351D: C7 ; 21 "SCARAB"
351E: E5 ; 22 "JEWELBOX"
351F: C4 ; 23 "TABLET"
3520: CE ; 24 "ROPE"
3521: BA ; 25 "SPRITE"
3522: BB ; 26 "TROGLODYTE"
3523: AB ; 27 "SCORPION"
3524: AC ; 28 "NYMPH"
3525: AD ; 29 "SATYR"
3526: 7F ; 30 "MINOTAUR"
3527: AE ; 31 "ORACLE"
3528: 81 ; 32 "GOLD"
3529: 25 ; 33 "SILVER"
352A: AF ; 34 "DIAMOND"
352B: B0 ; 35 "SPELLBOOK"
352C: BF ; 36 "RUBY"
352D: B2 ; 37 "FLEECE"
352E: B3 ; 38 "TIARA"
352F: B4 ; 39 "POWDER"
3530: B5 ; 40 "AMULET"
3531: B6 ; 41 "POTION"
3532: BC ; 42 "POWERRING"
3533: BD ; 43 "LIGHTRING"
3534: BE ; 44 "TRUTHRING"
3535: C0 ; 45 "CROWN"
3536: FA ; 46 "OPAL"
3537: FB ; 47 "SAPPHIRE"

3538: 01 ; 48 "NORTH"       ? Objects removed from code or never added ?
3539: 01 ; 49 "NORTH"      
353A: 01 ; 50 "NORTH"      
353B: 01 ; 51 "NORTH"      
353C: 01 ; 52 "NORTH"      
353D: 01 ; 53 "NORTH"      
353E: 01 ; 54 "NORTH"      

353F: F2 ; 55 "VETAR"
3540: F3 ; 56 "MITRA"
3541: F4 ; 57 "OKKAN"
3542: F5 ; 58 "AKHIROM"
3543: F6 ; 59 "NERGAL"
3544: F7 ; 60 "BELROG"
3545: F8 ; 61 "CROM"
3546: F9 ; 62 "ISHTAR"

3547: 00 00 00  
  
ObjectWeightAndBulk:
; Object weight and bulk table

;   Weight Bulk
354A: 07 07  ; "FOOD"       
354C: 07 07  ; "BOTTLE"     
354E: 28 14  ; "DAGGER"     
3550: 3C 3C  ; "MACE"       
3552: 3C 3C  ; "AX"         
3554: 46 28  ; "SWORD"           
3556: 3C 32  ; "SHIELD"        
3558: 1E 14  ; "FLUTE"      
355A: 32 1E  ; "MUSHROOM"   
355C: 1E 28  ; "PENDANT"    
355E: 32 41  ; "SCEPTER"    
3560: 06 06  ; "LAMP"       
3562: 14 00  ; "BASKET"     
3564: 23 28  ; "PARCHMENT"  
3566: 2D 32  ; "VIAL"                     
3568: 32 6E  ; "URN"        
356A: 28 28  ; "TALISMAN"   
356C: 28 32  ; "SCROLL"     
356E: 28 46  ; "GOBLET"     
3570: 28 28  ; "SKULL"      
3572: 1E 32  ; "SCARAB"     
3574: 1E 46  ; "JEWELBOX"   
3576: 32 55  ; "TABLET"     
3578: 28 3C  ; "ROPE"       
357A: 00 00  ; "SPRITE"     
357C: 00 00  ; "TROGLODYTE" 
357E: 00 00  ; "SCORPION"   
3580: 00 00  ; "NYMPH"      
3582: 00 00  ; "SATYR"      
3584: 00 00  ; "MINOTAUR"   
3586: 00 00  ; "ORACLE"     
3588: 64 1E  ; "GOLD"       
358A: 46 32  ; "SILVER"     
358C: 28 32  ; "DIAMOND"    
358E: 46 50  ; "SPELLBOOK"  
3590: 28 3C  ; "RUBY"      
3592: 5A 50  ; "FLEECE"     
3594: 32 37  ; "TIARA"      
3596: 3C 28  ; "POWDER"     
3598: 5A 2D  ; "AMULET"     
359A: 46 46  ; "POTION"     
359C: 5A 5A  ; "POWERRING"   
359E: 5A 5A  ; "LIGHTRING"                    
35A0: 5A 5A  ; "TRUTHRING"  
35A2: 50 32  ; "CROWN"      
35A4: 28 28  ; "OPAL"       
35A6: 3C 3C  ; "SAPPHIRE"   
;
35A8: 00 00  ; "NORTH"      ? Objects removed from code or never added ?
35AA: 00 00  ; "NORTH"
35AC: 00 00  ; "NORTH"
35AE: 00 00  ; "NORTH"
35B0: 00 00  ; "NORTH"
35B2: 00 00  ; "NORTH"
35B4: 00 00  ; "NORTH"
;
35B6: 00 00  ; "VETAR"
35B8: 00 00  ; "MITRA"
35BA: 00 00  ; "OKKAN"
35BC: 00 00  ; "AKHIROM"
35BE: 00 00  ; "NERGAL"
35C0: 00 00  ; "BELROG"
35C2: 00 00  ; "CROM"
35C4: 00 00  ; "ISHTAR"
```

## Word List 

```code
WordList:
35C6:  44 4F 4F 52 57 41 D9  ; 0 "DOORWAY"
35CD:  4E 4F 52 54 C8  ; 1 "NORTH"
35D2:  53 4F 55 54 C8  ; 2 "SOUTH"
35D7:  57 45 53 D4  ; 3 "WEST"
35DB:  45 41 53 D4  ; 4 "EAST"
35DF:  55 D0  ; 5 "UP"
35E1:  44 4F 57 CE  ; 6 "DOWN"
35E5:  42 55 D4  ; 7 "BUT"
35E8:  49 53 20 C1  ; 8 "IS A"
35EC:  42 4C 4F 43 4B 45 C4  ; 9 "BLOCKED"
35F3:  43 45 49 4C 49 4E C7  ; 10 "CEILING"
35FA:  53 48 41 4C 4C 4F D7  ; 11 "SHALLOW"
3601:  57 41 4C CC  ; 12 "WALL"
3605:  48 49 47 C8  ; 13 "HIGH"
3609:  4C 4F D7  ; 14 "LOW"
360C:  43 4F 52 4E 45 D2  ; 15 "CORNER"
3612:  43 45 4E 54 45 D2  ; 16 "CENTER"
3618:  43 4F 52 52 49 44 4F D2  ; 17 "CORRIDOR"
3620:  4C 45 56 45 CC  ; 18 "LEVEL"
3625:  43 41 52 56 49 4E 47 D3  ; 19 "CARVINGS"
362D:  4C 49 47 48 D4  ; 20 "LIGHT"
3632:  44 41 52 CB  ; 21 "DARK"
3636:  54 4F 52 43 C8  ; 22 "TORCH"
363B:  53 4B 45 4C 45 54 4F CE  ; 23 "SKELETON"
3643:  4E 41 52 43 49 53 53 55 D3  ; 24 "NARCISSUS"
364C:  50 4C 41 4E 54 D3  ; 25 "PLANTS"
3652:  57 49 44 C5  ; 26 "WIDE"
3656:  50 41 53 53 41 47 C5  ; 27 "PASSAGE"
365D:  57 41 D9  ; 28 "WAY"
3660:  53 4D 41 4C CC  ; 29 "SMALL"
3665:  4C 41 52 47 C5  ; 30 "LARGE"
366A:  43 52 4F 53 D3  ; 31 "CROSS"
366F:  4C 4F 4E C7  ; 32 "LONG"
3673:  53 54 55 43 CB  ; 33 "STUCK"
3678:  49 CE  ; 34 "IN"
367A:  4D 41 47 49 C3  ; 35 "MAGIC"
367F:  46 4C 55 54 C5  ; 36 "FLUTE"
3684:  53 49 4C 56 45 D2  ; 37 "SILVER"
368A:  44 41 47 47 45 D2  ; 38 "DAGGER"
3690:  42 41 53 4B 45 D4  ; 39 "BASKET"
3696:  4E 41 52 52 4F D7  ; 40 "NARROW"
369C:  47 52 45 41 D4  ; 41 "GREAT"
36A1:  53 54 4F 4E C5  ; 42 "STONE"
36A6:  54 4F 57 45 D2  ; 43 "TOWER"
36AB:  50 4F 4F CC  ; 44 "POOL"
36AF:  57 41 54 45 D2  ; 45 "WATER"
36B4:  54 57 49 53 54 49 4E C7  ; 46 "TWISTING"
36BC:  41 4E C4  ; 47 "AND"
36BF:  54 48 45 52 C5  ; 48 "THERE"
36C4:  41 52 C5  ; 49 "ARE"
36C7:  47 52 45 45 CE  ; 50 "GREEN"
36CC:  44 52 41 50 45 D3  ; 51 "DRAPES"
36D2:  4F CE  ; 52 "ON"
36D4:  54 48 C5  ; 53 "THE"
36D7:  46 49 4C 4C 45 C4  ; 54 "FILLED"
36DD:  48 41 4C CC  ; 55 "HALL"
36E1:  57 49 54 C8  ; 56 "WITH"
36E5:  54 41 42 4C C5  ; 57 "TABLE"
36EA:  43 48 41 49 D2  ; 58 "CHAIR"
36EF:  47 55 41 52 C4  ; 59 "GUARD"
36F4:  52 4F 4F CD  ; 60 "ROOM"
36F8:  57 4F 4F C4  ; 61 "WOOD"
36FC:  50 49 4C C5  ; 62 "PILE"
3700:  42 4F 4E 45 D3  ; 63 "BONES"
3705:  46 4C 4F 4F D2  ; 64 "FLOOR"
370A:  43 48 41 53 CD  ; 65 "CHASM"
370F:  43 4C 45 41 CE  ; 66 "CLEAN"
3714:  43 48 41 50 45 CC  ; 67 "CHAPEL"
371A:  4E CF  ; 68 "NO"
371C:  57 49 4E 44 4F 57 D3  ; 69 "WINDOWS"
3723:  54 52 4F 50 48 D9  ; 70 "TROPHY"
3729:  45 4D 50 54 D9  ; 71 "EMPTY"
372E:  43 4C 4F 53 45 D4  ; 72 "CLOSET"
3734:  50 41 49 4E 54 49 4E C7  ; 73 "PAINTING"
373C:  4D 55 53 54 D9  ; 74 "MUSTY"
3741:  4B 49 54 43 48 45 CE  ; 75 "KITCHEN"
3748:  52 41 54 D3  ; 76 "RATS"
374C:  42 52 4F 4B 45 CE  ; 77 "BROKEN"
3752:  54 49 4C 45 D3  ; 78 "TILES"
3757:  52 4F 59 41 CC  ; 79 "ROYAL"
375C:  42 45 C4  ; 80 "BED"
375F:  41 52 4D 4F 52 D9  ; 81 "ARMORY"
3765:  53 57 4F 52 C4  ; 82 "SWORD"
376A:  53 48 49 45 4C C4  ; 83 "SHIELD"
3770:  4C 49 42 52 41 52 D9  ; 84 "LIBRARY"
3777:  57 49 4E C5  ; 85 "WINE"
377B:  43 45 4C 4C 41 D2  ; 86 "CELLAR"
3781:  50 4F 52 54 41 CC  ; 87 "PORTAL"
3787:  43 4F 55 52 D4  ; 88 "COURT"
378C:  59 41 52 C4  ; 89 "YARD"
3790:  43 4C 4F 49 53 54 45 D2  ; 90 "CLOISTER"
3798:  53 45 52 56 41 4E D4  ; 91 "SERVANT"
379F:  43 48 41 4D 42 45 D2  ; 92 "CHAMBER"
37A6:  50 41 4E 54 52 D9  ; 93 "PANTRY"
37AC:  42 45 45 D2  ; 94 "BEER"
37B0:  41 D8  ; 95 "AX"
37B2:  47 4C 41 53 D3  ; 96 "GLASS"
37B7:  53 54 41 49 D2  ; 97 "STAIR"
37BC:  53 45 C5  ; 98 "SEE"
37BF:  44 41 4D D0  ; 99 "DAMP"
37C3:  C1  ; 100 "A"
37C4:  41 4E 43 49 45 4E D4  ; 101 "ANCIENT"
37CB:  53 4B 55 4C CC  ; 102 "SKULL"
37D0:  4F C6  ; 103 "OF"
37D2:  43 41 56 45 52 CE  ; 104 "CAVERN"
37D8:  43 41 56 C5  ; 105 "CAVE"
37DC:  43 48 49 4C CC  ; 106 "CHILL"
37E1:  4D 49 53 D4  ; 107 "MIST"
37E5:  53 57 49 52 4C 49 4E C7  ; 108 "SWIRLING"
37ED:  50 49 D4  ; 109 "PIT"
37F0:  53 55 4E 4B 45 CE  ; 110 "SUNKEN"
37F6:  57 49 4E 44 49 4E C7  ; 111 "WINDING"
37FD:  45 44 47 C5  ; 112 "EDGE"
3801:  53 48 41 46 D4  ; 113 "SHAFT"
3806:  54 4F 4D C2  ; 114 "TOMB"
380A:  45 56 45 52 59 57 48 45 52 C5  ; 115 "EVERYWHERE"
3814:  43 52 59 50 D4  ; 116 "CRYPT"
3819:  4B 49 4E C7  ; 117 "KING"
381D:  44 45 41 C4  ; 118 "DEAD"
3821:  45 4E C4  ; 119 "END"
3824:  54 55 4E 4E 45 CC  ; 120 "TUNNEL"
382A:  53 4D 4F 4F 54 C8  ; 121 "SMOOTH"
3830:  4D 41 52 42 4C C5  ; 122 "MARBLE"
3836:  46 4F 55 CC  ; 123 "FOUL"
383A:  53 4D 45 4C 4C 49 4E C7  ; 124 "SMELLING"
3842:  46 4C 4F 57 49 4E C7  ; 125 "FLOWING"
3849:  4C 41 49 D2  ; 126 "LAIR"
384D:  4D 49 4E 4F 54 41 55 D2  ; 127 "MINOTAUR"
3855:  4F 56 45 52 4C 4F 4F 4B 49 4E C7  ; 128 "OVERLOOKING"
3860:  47 4F 4C C4  ; 129 "GOLD"
3864:  59 4F 55 20 41 52 C5  ; 130 "YOU ARE"
386B:  57 48 41 D4  ; 131 "WHAT"
386F:  54 CF  ; 132 "TO"
3871:  48 45 52 C5  ; 133 "HERE"
3875:  53 50 52 49 4E 47 D3  ; 134 "SPRINGS"
387C:  4C 45 41 54 48 45 D2  ; 135 "LEATHER"
3883:  53 49 54 D3  ; 136 "SITS"
3887:  52 45 53 54 49 4E C7  ; 137 "RESTING"
388E:  46 45 45 D4  ; 138 "FEET"
3892:  41 47 41 49 4E 53 D4  ; 139 "AGAINST"
3899:  49 D3  ; 140 "IS"
389B:  42 41 C7  ; 141 "BAG"
389E:  42 52 4F 4E 5A C5  ; 142 "BRONZE"
38A4:  4F 46 C6  ; 143 "OFF"
38A7:  54 52 41 49 CC  ; 144 "TRAIL"
38AC:  59 4F 55 D2  ; 145 "YOUR"
38B0:  41 D4  ; 146 "AT"
38B2:  4E 4F 54 48 49 4E C7  ; 147 "NOTHING"
38B9:  46 4F 4F C4  ; 148 "FOOD"
38BD:  49 4E 54 CF  ; 149 "INTO"
38C1:  53 49 47 48 D4  ; 150 "SIGHT"
38C6:  44 49 53 41 50 50 45 41 52 D3  ; 151 "DISAPPEARS"
38D0:  4C 45 41 44 D3  ; 152 "LEADS"
38D5:  57 49 4E 44 D3  ; 153 "WINDS"
38DA:  4F 50 45 4E 49 4E C7  ; 154 "OPENING"
38E1:  59 4F D5  ; 155 "YOU"
38E4:  47 45 4E 54 4C D9  ; 156 "GENTLY"
38EA:  53 4C 4F 50 49 4E C7  ; 157 "SLOPING"
38F1:  4F 55 D4  ; 158 "OUT"
38F4:  48 4F 4C C5  ; 159 "HOLE"
38F8:  52 45 43 45 53 53 45 C4  ; 160 "RECESSED"
3900:  42 4F 54 54 4F CD  ; 161 "BOTTOM"
3906:  54 4F D0  ; 162 "TOP"
3909:  4B 4E 49 46 C5  ; 163 "KNIFE"
390E:  50 45 4E 44 41 4E D4  ; 164 "PENDANT"
3915:  53 43 45 50 54 45 D2  ; 165 "SCEPTER"
391C:  4C 41 4D D0  ; 166 "LAMP"
3920:  50 41 52 43 48 4D 45 4E D4  ; 167 "PARCHMENT"
3929:  56 49 41 CC  ; 168 "VIAL"
392D:  55 52 CE  ; 169 "URN"
3930:  53 50 45 4C CC  ; 170 "SPELL"
3935:  53 43 4F 52 50 49 4F CE  ; 171 "SCORPION"
393D:  4E 59 4D 50 C8  ; 172 "NYMPH"
3942:  53 41 54 59 D2  ; 173 "SATYR"
3947:  4F 52 41 43 4C C5  ; 174 "ORACLE"
394D:  44 49 41 4D 4F 4E C4  ; 175 "DIAMOND"
3954:  53 50 45 4C 4C 42 4F 4F CB  ; 176 "SPELLBOOK"
395D:  52 49 4E C7  ; 177 "RING"
3961:  46 4C 45 45 43 C5  ; 178 "FLEECE"
3967:  54 49 41 52 C1  ; 179 "TIARA"
396C:  50 4F 57 44 45 D2  ; 180 "POWDER"
3972:  41 4D 55 4C 45 D4  ; 181 "AMULET"
3978:  50 4F 54 49 4F CE  ; 182 "POTION"
397E:  53 43 52 4F 4C CC  ; 183 "SCROLL"
3984:  42 4F 54 54 4C C5  ; 184 "BOTTLE"
398A:  46 4F 52 45 53 D4  ; 185 "FOREST"
3990:  53 50 52 49 54 C5  ; 186 "SPRITE"
3996:  54 52 4F 47 4C 4F 44 59 54 C5  ; 187 "TROGLODYTE"
39A0:  50 4F 57 45 52 52 49 4E C7  ; 188 "POWERRING"
39A9:  4C 49 47 48 54 52 49 4E C7  ; 189 "LIGHTRING"
39B2:  54 52 55 54 48 52 49 4E C7  ; 190 "TRUTHRING"
39BB:  52 55 42 D9  ; 191 "RUBY"
39BF:  43 52 4F 57 CE  ; 192 "CROWN"
39C4:  54 41 4C 49 53 4D 41 CE  ; 193 "TALISMAN"
39CC:  47 4F 42 4C 45 D4  ; 194 "GOBLET"
39D2:  4A 41 D2  ; 195 "JAR"
39D5:  54 41 42 4C 45 D4  ; 196 "TABLET"
39DB:  57 48 49 43 C8  ; 197 "WHICH"
39E0:  56 4F 49 43 45 D3  ; 198 "VOICES"
39E6:  53 43 41 52 41 C2  ; 199 "SCARAB"
39EC:  50 41 54 C8  ; 200 "PATH"
39F0:  4D 41 43 C5  ; 201 "MACE"
39F4:  4D 55 53 48 52 4F 4F CD  ; 202 "MUSHROOM"
39FC:  53 50 41 52 4B 4C 49 4E C7  ; 203 "SPARKLING"
3A05:  44 49 CD  ; 204 "DIM"
3A08:  50 41 54 C8  ; 205 "PATH"
3A0C:  52 4F 50 C5  ; 206 "ROPE"
3A10:  44 49 52 D4  ; 207 "DIRT"
3A14:  4C 41 59 D3  ; 208 "LAYS"
3A18:  53 49 44 C5  ; 209 "SIDE"
3A1C:  49 D4  ; 210 "IT"
3A1E:  41 49 D2  ; 211 "AIR"
3A21:  56 45 4C 56 45 D4  ; 212 "VELVET"
3A27:  4E 4F D4  ; 213 "NOT"
3A2A:  52 45 41 43 C8  ; 214 "REACH"
3A2F:  46 52 4F CD  ; 215 "FROM"
3A33:  42 D9  ; 216 "BY"
3A35:  46 4F 52 43 C5  ; 217 "FORCE"
3A3A:  48 41 4E 47 49 4E C7  ; 218 "HANGING"
3A41:  53 55 53 50 45 4E 44 45 C4  ; 219 "SUSPENDED"
3A4A:  42 55 52 49 45 C4  ; 220 "BURIED"
3A50:  57 48 45 CE  ; 221 "WHEN"
3A54:  43 41 CE  ; 222 "CAN"
3A57:  4B 45 45 50 D3  ; 223 "KEEPS"
3A5C:  46 4C 4F 41 54 D3  ; 224 "FLOATS"
3A62:  4D 4F 56 C5  ; 225 "MOVE"
3A66:  4E 45 41 D2  ; 226 "NEAR"
3A6A:  50 52 4F 54 45 43 54 45 C4  ; 227 "PROTECTED"
3A73:  57 49 4C CC  ; 228 "WILL"
3A77:  4A 45 57 45 4C 42 4F D8  ; 229 "JEWELBOX"
3A7F:  54 45 4D 50 4C C5  ; 230 "TEMPLE"
3A85:  5A 45 55 D3  ; 231 "ZEUS"
3A89:  49 4E 20 41 20 4D 41 5A 45 20 4F 46 20 54 55 4E 4E 45 4C 53 20 53 54 52 45 54 43 48 49 4E 47 20 4F 55 54 20 4F 46 20 53 49 47 48 54 20 49 4E 20 41 4C 4C 20 44 49 52 45 43 54 49 4F 4E D3  ; 232 "IN A MAZE OF TUNNELS STRETCHING OUT OF SIGHT IN ALL DIRECTIONS"
3AC7:  54 52 41 43 4B D3  ; 233 "TRACKS"
3ACD:  44 45 45 D0  ; 234 "DEEP"
3AD1:  41 43 52 4F 53 D3  ; 235 "ACROSS"
3AD7:  53 48 41 44 4F D7  ; 236 "SHADOW"
3ADD:  53 54 52 45 54 43 48 49 4E C7  ; 237 "STRETCHING"
3AE7:  41 CE  ; 238 "AN"
3AE9:  47 4C 4F 57 49 4E C7  ; 239 "GLOWING"
3AF0:  41 54 54 41 43 4B 49 4E C7  ; 240 "ATTACKING"
3AF9:  4F 49 CC  ; 241 "OIL"
3AFC:  56 45 54 41 D2  ; 242 "VETAR"
3B01:  4D 49 54 52 C1  ; 243 "MITRA"
3B06:  4F 4B 4B 41 CE  ; 244 "OKKAN"
3B0B:  41 4B 48 49 52 4F CD  ; 245 "AKHIROM"
3B12:  4E 45 52 47 41 CC  ; 246 "NERGAL"
3B18:  42 45 4C 52 4F C7  ; 247 "BELROG"
3B1E:  43 52 4F CD  ; 248 "CROM"
3B22:  49 53 48 54 41 D2  ; 249 "ISHTAR"
3B28:  4F 50 41 CC  ; 250 "OPAL"
3B2C:  53 41 50 50 48 49 52 C5  ; 251 "SAPPHIRE"
3B34:  48 59 44 52 C1  ; 252 "HYDRA"
3B39:  4C 45 44 47 C5  ; 253 "LEDGE"
```

## Direction Table 

```code
DirectionDescriptionTable:
; Each direction has 8 messages that describe and open path in that
; direction. The table below points to the 1st of 8 for each.
3B3E: 28 2E  ; South (--000001)
3B40: 28 76  ; West  (--000010)
3B42: 28 BB  ; East  (--000100)          
3B44: 29 00  ; North (--001000)         
3B46: 29 48  ; Down  (--010000)         
3B48: 29 88  ; Up    (--100000)
```

## Between Room Handlers 
 Between room handlers
 4 byte entries. 1st byte is room, 2nd byte is direction,
 and 3rd and 4th are routine.
 The code searches the entire list top to bottom with the room/direction we are moving. If no list is
 found then it runs the list again from the target room and backwards direction. There are two handlers
 for 10<->202 UP/DOWN. If you are climbing down you sometimes land in a random room. If you are climbing
 up you have to be in good physical condition. But there is only one handler between 74->75 EAST/WEST. It
 will trigger in either direction.

```code         
BetweenRoomHandler:
3B4A: 4A 04 1A FB ; 1:2:1 --EAST:WEST-- 1:3:1    ; A  If excess physical condition is less than random 40-BF then a climb-up fails.
3B4E: 53 04 1A FB ; 1:3:2 --EAST:WEST-- 1:4:2    ; A  see above
;
3B52: CA 10 1B 20 ; 3:2:1 --DOWN:UP-- 0:2:1      ; B  Moves us to start room 10 (or infrequently in a room near the start).
3B56: 0A 20 1B 03 ; 0:2:1 --UP:DOWN-- 3:2:1      ; C  If excess physical condition is less than 192 then a climb-up fails.
;
3B5A: 40 20 1B 06 ; 1:0:0 --UP:DOWN-- 0:0:0      ; D  If excess physical condition is less than 64 then a climb-up fails.
3B5E: D9 01 1A FB ; 3:1:3 --SOUTH:NORTH-- 3:1:4  ; A  see above
3B62: 44 20 1B 06 ; 1:4:0 --UP:DOWN-- 0:4:0      ; D  see above
3B66: 47 20 1A FB ; 1:7:0 --UP:DOWN-- 0:7:0      ; A  see above
3B6A: 53 20 1B 09 ; 1:3:2 --UP:DOWN-- 0:3:2      ; E  If excess physical condition is less than 128 then a climb-up fails.
3B6E: 12 01 1B 34 ; 0:2:2 --SOUTH:NORTH-- 0:2:3  ; F  If the lamp is in our pack this moves us to a totally random room. 
3B72: 59 20 1A FB ; 1:1:3 --UP:DOWN-- 0:1:3      ; A  see above
3B76: 42 20 1A FB ; 1:2:0 --UP:DOWN-- 0:2:0      ; A  see above
3B7A: 82 20 1B 06 ; 2:2:0 --UP:DOWN-- 1:2:0      ; D  see above
3B7E: 87 20 1B 06 ; 2:7:0 --UP:DOWN-- 1:7:0      ; D  see above
3B82: 96 20 1A FB ; 2:6:2 --UP:DOWN-- 1:6:2      ; A  see above
3B86: 99 20 1A FB ; 2:1:3 --UP:DOWN-- 1:1:3      ; A  see above
3B8A: 9C 20 1B 03 ; 2:4:3 --UP:DOWN-- 1:4:3      ; C  see above
3B8E: 8A 04 1B 5F ; 2:2:1 --EAST:WEST-- 2:3:1    ; G  There is a 50/50 chance of moving to a random room in the first half of the last two floors.
3B92: D4 08 1B 09 ; 3:4:2 --NORTH:SOUTH-- 3:4:1  ; E  see above
3B96: 4D 08 1B 03 ; 1:5:1 --NORTH:SOUTH-- 1:5:0  ; C  see above
3B9A: F3 20 1B 34 ; 3:3:6 --UP:DOWN-- 2:3:6      ; F  see above
3B9E: F3 10 1B 34 ; 3:3:6 --DOWN:UP-- 0:3:6      ; F  see above
3BA2: AF 08 1B 43 ; 2:7:5 --NORTH:SOUTH-- 2:7:4  ; H  There is a 50/50 chance of going to a random room in the maze on a random floor.
3BA6: 69 08 1B 43 ; 1:1:5 --NORTH:SOUTH-- 1:1:4  ; H  see above
3BAA: AE 04 1B 4A ; 2:6:5 --EAST:WEST-- 2:7:5    ; I  Move to a random room in the maze on a random floor (1 in 36 chance of doing nothing).
3BAE: 68 04 1B 4A ; 1:0:5 --EAST:WEST-- 1:1:5    ; I  see above
3BB2: 6A 02 1B 4A ; 1:2:5 --WEST:EAST-- 1:1:5    ; I  see above
3BB6: B0 02 1B 4A ; 2:0:6 --WEST:EAST-- 2:7:5    ; I  see above
3BBA: E0 01 1B 5F ; 3:0:4 --SOUTH:NORTH-- 3:0:5  ; G  see above

3BBE: 00 00 00 

TapeSavePoint:
;
; From 3BC1 to 3FFF is saved/restored to tape with SAVE/LOAD
```

## Learning Spells

```code
SpellData:
; Spell data
;   AA BB CC DD
;   AA = 1st required object to learn spell
;   BB = 2nd required object to learn spell
;   CC = room spell is in (not learned)
;   DD = $80 if learned, 0 if not
;
;                      Spell    Must have to learn
3BC1: 09 01 00 00    ; VETRA:   MUSHROOM and FOOD                   
3BC5: 0E 37 00 00    ; MITRA:   PARCHMENT and  VETRA                   
3BC9: 11 38 00 00    ; OKKAN:   TALISMAN and MITRA              
3BCD: 18 39 00 00    ; AKHIROM: ROPE and OKKAN                   
3BD1: 0B 3A 00 00    ; NERGAL:  SCEPTER and AKHIROM               
3BD5: 0F 3B 00 00    ; BELROG:  VIAL and NERGAL               
3BD9: 0A 3C 00 00    ; CROM:    PENDANT and BELROG             
3BDD: 23 3D 00 00    ; ISHTAR:  SPELLBOOK and CROM
```
    
## Jump Info 

```code
JumpInfoTable:
;
; Describes places where you can JUMP.
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
```

CodeBug6

 The source for this last jump is set by the code at 0CC7. This jump is given to the
 same room where the RoomEnterAction_203 (SMALL PIT IN CORNER OF ROOM). A JUMP DOWN
 (into the pit) lands you in room 39 -- The Temple of Zeus. REA_203 is placed at
 random anywhere on the 4th floor. The code that reads this table (19AC) only finds
 the first entry in this list for a room. If there is a second jump then it will
 never get discovered. If the RAE_203 is placed in a room with an existing jump then
 the jump to the Temple of Zeus doesn't work.
 
```code
3C59: 10 8C 80 27 06; From 16  "JUMP DOWN"  to 39.  Required=140 or FUMBLE
3C5E: 00            
```
 
## Who Holds What
 List of owners to hold objects

```code
WhoHolds:
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
;
;     0B ; Entering-room-r


; 1=crypt, 2=crypt-kings, 3=_u, 4=_33, 5=pit,6=ledge, 7=hydra, 8=pile-of-rocks,  9=_s, 10=_t(rat), 11=_r, >12creature number
; Held-by table. Treasures are carried by creatures or "held" by a room. This
; table maps the holder to the treasure.
;  AA BB
;   A = owner (see list above)
;   B = held object
;
3C6F: 00 2E  ; 46 "OPAL"
3C71: 00 2F  ; 47 "SAPPHIRE"
3C73: 00 12  ; 18 "SCROLL"                  
3C75: 00 15  ; 21 "SCARAB"            
3C77: 00 16  ; 22 "JEWLBOX"            
3C79: 00 17  ; 23 "TABLET"            
3C7B: 00 20  ; 32 "GOLD"            
3C7D: 00 21  ; 33 "SILVER"            
3C7F: 00 22  ; 34 "DIAMOND"           
3C81: 00 24  ; 36 "RUBY"           
3C83: 00 25  ; 37 "FLEECE"            
3C85: 00 26  ; 38 "TIARA"           
3C87: 00 27  ; 39 "POWDER"           
3C89: 00 28  ; 40 "AMULET"            
3C8B: 00 29  ; 41 "POTION"           
3C8D: 00 2D  ; 45 "CROWN"           
```

## Enter Room Table 

```code
ActionWhenEnteringRoom:
3C8F: 00 1B 6D  ; 0    _a     ; Cave in to next floor if pack heavier than 192. If so move a nd b to random rooms.
3C92: 00 1B 70  ; 0    _b     ; Cave in to next floor if pack heavier than 128. If so move a nd b to random rooms.
3C95: 00 1B 73  ; 0    _c     ; Cave in to next floor if pack heavier than 95. If so move a nd b to random rooms.
3C98: 00 1B 9C  ; 0    _d     ; # If we have VETAR make the pile-of-rocks appear in this room (it stays here).
3C9B: 00 1B B3  ; 0    _e     ; # Play sound effect. If we play the flute and have the parchment then the LEDGE appears here.
3C9E: 00 1B B7  ; 0    _f     ; Powerful gust blows lamp out of grasp. 
3CA1: 00 1B F9  ; 0    _g     ; # Hydra is here. If it is free it pushes us back to last room. 
3CA4: 00 1C 15  ; 0    _h     ; If we know VETAR or have the SCEPTER, nothing happens. Otherwise we RUN.
3CA7: 00 1C 2C  ; 0    _i     ; Pushed back if we don't have VETAR.
3CAA: 00 1C 2F  ; 0    _j     ; Pushed back if we don't have MITRA.
3CAD: 00 1C 32  ; 0    _k     ; Pushed back if we don't have OKKAN.
3CB0: 00 1C 35  ; 0    _l     ; Pushed back if we don't have AKHIROM.
3CB3: 00 1C 38  ; 0    _m     ; Pushed back if we don't have NERGAL.
3CB6: 00 1C 3B  ; 0    _n     ; Pushed back if we don't have BELROG.
3CB9: 00 1C 3E  ; 0    _o     ; Pushed back if we don't have CROM.
3CBC: 00 1C 41  ; 0    _p     ; Pushed back if we don't have ISHTAR.
3CBF: 00 1C 68  ; 0    _q     ; Start the poison clock (we can't stay here long). 1/3 of the time we give the clock an extra tick.
3CC2: 00 1C 7A  ; 0    _r     ; # When we enter this room 3 times the treasure is released.
3CC5: 00 1C 68  ; 0    _q     ; see above 
3CC8: 00 1C 68  ; 0    _q     ; see above
3CCB: 00 1C 8D  ; 0    _s     ; # If we have the lamp and it is off then the room drops its treasure. (Strange color walls)
3CCE: 00 1C A9  ; 0    _t     ; # If we are holding the packrat's trigger treasure (randomized at start) then the packrat drops his treasure.
3CD1: 00 1C 68  ; 0    _q     ; see above
3CD4: 00 1C CC  ; 0    _u     ; # If we can see you instantly get the treasure.
3CD7: 00 1C F0  ; 0    _v     ; Print POOL OF OIL if the lamp can be refilled.
3CDA: 00 1B B7  ; 0    _f     ; see above
3CDD: 00 1C E0  ; 0    _32    ; (Same as 32 below)
3CE0: 00 1D 00  ; 0    _x     ; Add 40 to health and move us a short distance away. 10 minutes must pass before again. 
3CE3: 00 1D 00  ; 0    _x     ; see above
3CE6: 00 1D 22  ; 0    _203   ; # Print "SMALL PIT IN CORNER OF ROOM"
;
3CE9: D5 1D 27  ; 213  _213     ; Print "LAYER OF MIST EAST WALL"
3CEC: 20 1C E0  ; 32   _32      ; If we can't see we take 30 damage.
3CEF: 21 1C D6  ; 33   _33      ; # If we can see you instantly get the treasure.
3CF2: CB 1D 22  ; 203  _203     ; Print SMALL PIT IN CORNER OF ROOM.
3CF5: 00 1B B4  ; 0    _z       ; Room with music (init to room 16 to 39). The sprite can't move objects here.
3CF8: E8 1D 2D  ; 232  _232     ; _232 If we came south to this room and carrying pendant move us near start and random room for pendant.

3CFB: 00
```

## Object Data 

```code
ObjectData:
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
3CFC: 00 01 00  ; 1 "FOOD"
3CFF: 08 02 00  ; 2 "BOTTLE"
3D02: 28 03 00  ; 3 "DAGGER"
3D05: 01 04 00  ; 4 "MACE"
3D08: 01 05 00  ; 5 "AX"
3D0B: 04 06 10  ; 6 "SWORD"
3D0E: 08 07 10  ; 7 "SHIELD"
3D11: 00 08 00  ; 8 "FLUTE"
3D14: 02 09 00  ; 9 "MUSHROOM"
3D17: 00 0A 00  ; 10 "PENDANT"
3D1A: 02 0B 00  ; 11 "SCEPTER"
3D1D: 02 0C 00  ; 12 "LAMP"
3D20: 04 0D 00  ; 13 "BASKET"
3D23: 04 0E 01  ; 14 "PARCHMENT"
3D26: 04 0F 10  ; 15 "VIAL"
3D29: 06 10 00  ; 16 "URN"
3D2C: 06 11 01  ; 17 "TALISMAN"
3D2F: 0C 12 01  ; 18 "SCROLL"
3D32: 0C 13 00  ; 19 "GOBLET"
3D35: 0C 14 10  ; 20 "SKULL"
3D38: 0C 15 01  ; 21 "SCARAB"
3D3B: 0D 16 01  ; 22 "JEWELBOX"
3D3E: 0D 17 01  ; 23 "TABLET"
3D41: 0D 18 00  ; 24 "ROPE"
3D44: 0D 19 40  ; 25 "SPRITE"
3D47: 0E 1A 40  ; 26 "TROGLODYTE"
3D4A: 0A 1B 40  ; 27 "SCORPION"
3D4D: 0B 1C 40  ; 28 "NYMPH"
3D50: 0C 1D 40  ; 29 "SATYR"
3D53: 9E 1E 40  ; 30 "MINOTAUR"
3D56: 9E 1F 40  ; 31 "ORACLE"
3D59: 00 20 01  ; 32 "GOLD"
3D5C: 00 21 01  ; 33 "SILVER"
3D5F: 40 22 01  ; 34 "DIAMOND"
3D62: 40 23 10  ; 35 "SPELLBOOK"
3D65: 44 24 01  ; 36 "RUBY"
3D68: 44 25 01  ; 37 "FLEECE"
3D6B: 00 26 01  ; 38 "TIARA"
3D6E: 1D 27 01  ; 39 "POWDER"
3D71: 1D 28 01  ; 40 "AMULET"
3D74: 43 29 01  ; 41 "POTION"
3D77: 11 2A 10  ; 42 "POWERRING"
3D7A: 11 2B 10  ; 43 "LIGHTRING"
3D7D: 11 2C 10  ; 44 "TRUTHRING"
3D80: 12 2D 01  ; 45 "CROWN"
3D83: 00 2E 01  ; 46 "OPAL"
3D86: 00 2F 01  ; 47 "SAPPHIRE"
3D89: 00 00 42  ; 48 "NORTH"    
3D8C: 00 00 42  ; 49 "NORTH"
3D8F: 00 00 42  ; 50 "NORTH"
3D92: 00 00 42  ; 51 "NORTH"
3D95: 00 00 42  ; 52 "NORTH"
3D98: 00 00 42  ; 53 "NORTH"
3D9B: 00 00 42  ; 54 "NORTH"
3D9E: 00 37 42  ; 55 "VETAR"
3DA1: 00 38 42  ; 56 "MITRA"
3DA4: 00 39 42  ; 57 "OKKAN"
3DA7: 00 3A 42  ; 58 "AKHIROM"
3DAA: 00 3B 42  ; 59 "NERGAL"
3DAD: 00 3C 42  ; 60 "BELROG"
3DB0: 00 3D 42  ; 61 "CROM"
3DB3: 00 3E 42  ; 62 "ISHTAR"
;
3DB6: 00 FF     ; End of list marker
```

## Passage Configuration 
 Room door paths for 256 rooms <br>
 --UDNEWS

```code   
PassageConfigurations:      

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

## Blocked Passages

```code
; 3EB8 - 3FB7 ... blocked table (same pattern as natural-passage). Cleared at init.
```
             
## Protection Lists 
 3FB8 the lists of things needed for protected objects is built here. The form is protected
 object number followed by a list of required items (FF ends list). Then next protected
 number and so on until FF ends the list.

