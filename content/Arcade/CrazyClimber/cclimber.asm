
; Crazy climber memory map
#include "Mem_Map.inc"

; Crazy climber character encode table
#include "CharEnc.inc"


;=============================================================================
; Program entry point
;=============================================================================
        .org     0000H

; Note: These first two instructions seem like a waste of time, but
; the SOUND_DECODE routine has pointers that initialize to $0000 (here).
; They look to decode sound, and these two instructions do not fit a
; normal sound decode pattern, so the routine believes this is
; uninitialized...

STARTUP1:
        EX      DE,HL                   ; 0000 EB       .    DE <-> HL
        CP      $FF                     ; 0001 FEFF     ..   Compare accumulator with $FF

        XOR     A                       ; 0003 AF       .    Clear A
        LD      (NMI_MASK_WR),A         ; 0004 3200A0   2D.  Disable NMI interrupts
        LD      (HINV_WR),A             ; 0007 3201A0   2._  Set horizontal invert to 0 (normal)
        LD      (VINV_WR),A             ; 000A 3202A0   2..  Set vertical invert to 0 (normal)
        LD      (SOUND_CS_WR),A         ; 000D 3207A0   2F_  Enable the sound chip select
        JP      INIT_RAM                ; 0010 C3AC00   ..D  Initialize RAM

        NOP                             ; 0013 00       .
        NOP                             ; 0014 00       .
        NOP                             ; 0015 00       .
        NOP                             ; 0016 00       .
        NOP                             ; 0017 00       .
        NOP                             ; 0018 00       .
        NOP                             ; 0019 00       .
        NOP                             ; 001A 00       .
        NOP                             ; 001B 00       .
        NOP                             ; 001C 00       .
        NOP                             ; 001D 00       .
        NOP                             ; 001E 00       .
        NOP                             ; 001F 00       .

Lb158:  LD      A,(MACH_VER)            ; 0020 3A7C80   :,. Get the machine version
        OR      A                       ; 0023 B7       .   Check the value
        JP      NZ,Lb1                  ; 0024 C2B30B   ... Value is not zero (Upright), go here

        LD      A,(CURRENT_PLAYER)      ; 0027 3A8180   :.. Get the current player number
        OR      A                       ; 002A B7       .
        JP      NZ,Lb2                  ; 002B C2B80B   ..[ If player 2, go here
        JP      Lb1                     ; 002E C3B30B   ... Player 1, go here
        NOP                             ; 0031 00       .
        NOP                             ; 0032 00       .
        NOP                             ; 0033 00       .
        NOP                             ; 0034 00       .
        NOP                             ; 0035 00       .
        NOP                             ; 0036 00       .
        NOP                             ; 0037 00       .
        NOP                             ; 0038 00       .
        NOP                             ; 0039 00       .
        NOP                             ; 003A 00       .
        NOP                             ; 003B 00       .
        NOP                             ; 003C 00       .
        NOP                             ; 003D 00       .
        NOP                             ; 003E 00       .
        NOP                             ; 003F 00       .
        NOP                             ; 0040 00       .
        NOP                             ; 0041 00       .
        NOP                             ; 0042 00       .
        NOP                             ; 0043 00       .
        NOP                             ; 0044 00       .
        NOP                             ; 0045 00       .
        NOP                             ; 0046 00       .
        NOP                             ; 0047 00       .
        NOP                             ; 0048 00       .
        NOP                             ; 0049 00       .
        NOP                             ; 004A 00       .
        NOP                             ; 004B 00       .
        NOP                             ; 004C 00       .
        NOP                             ; 004D 00       .
        NOP                             ; 004E 00       .
        NOP                             ; 004F 00       .
        NOP                             ; 0050 00       .
        NOP                             ; 0051 00       .
        NOP                             ; 0052 00       .
        NOP                             ; 0053 00       .
        NOP                             ; 0054 00       .
        NOP                             ; 0055 00       .
        NOP                             ; 0056 00       .
        NOP                             ; 0057 00       .
        NOP                             ; 0058 00       .
        NOP                             ; 0059 00       .
        NOP                             ; 005A 00       .
        NOP                             ; 005B 00       .
        NOP                             ; 005C 00       .
        NOP                             ; 005D 00       .
        NOP                             ; 005E 00       .
        NOP                             ; 005F 00       .
        NOP                             ; 0060 00       .
        NOP                             ; 0061 00       .
        NOP                             ; 0062 00       .
        NOP                             ; 0063 00       .
        NOP                             ; 0064 00       .
        NOP                             ; 0065 00       .

;=============================================================================
; Called when an interrupt occurs (every vertical blank)
; (Mode 0 - originates at 0066H)
;=============================================================================
        .org    0066H                   ; Beginning of interrupt (vector 0066H)

ISR_1:
        PUSH    AF                      ; 0066 F5       .    Save A and flags register
        LD      A,(MACH_SW_RD)          ; 0067 3A00B8   :D.  Pet the watchdog
        XOR     A                       ; 006A AF       .    Clear A
        LD      (NMI_MASK_WR),A         ; 006B 3200A0   2D_  Disable NMI interrupts
        POP     AF                      ; 006E F1       .    Restore A and flags
        JP      ISR_2                   ; 006F C3D900   ..D  Continue interrupt service processing


; Part of the "startup" sequence, but is called during normal operation as well
STARTUP2:
        LD      A,(MACH_SW_RD)          ; 0072 3A00B8   :D.  Pet the watchdog
        XOR     A                       ; 0075 AF       .    Clear A
        LD      (NMI_MASK_WR),A         ; 0076 3200A0   2D.  Disable NMI interrupts

; Mark the ISR index as not initialized
        LD      HL,$FF                  ; 0079 21FF00   !.D  
        LD      (ISR_INDEX),HL          ; 007C 224080   "..

        LD      SP,RAM_END_SP           ; 007F 310084   1D.  Set the stack pointer to end of RAM

; Set the ISR jump pointer to the beginning of the jump table
        CALL    SET_JUMP_TABLE_PTR      ; 0082 CD4301   .V.  Save pointer to NMI ISR data table

; The player has died
Lb20:   XOR     A                       ; 0085 AF       .    
        LD      (KEEP_SAME_ISR_FLAG),A  ; 0086 324480   2..  Process the next ISR table location
        LD      HL,ISR_FLAG_TABLE+5     ; 0089 216280   !c.  This is the ISR flag, index 5
        LD      (HL),$40                ; 008C 3640     6.   Write $40 to the ISR flag table
        CALL    UPDATE_ISR_FLAG_TABLE   ; 008E CDCB00   ..D  Update the ISR flag table
        JP      ISR_3                   ; 0091 C33702   .&.  Continue



;-----------------------------------------------------------------------------
; Continue with ISR jump 4
;-----------------------------------------------------------------------------
;---------------------------------
; Initialize the ISR flag table
;
; I need to find out what each bit means
;
; ISR_FLAG_TABLE	Value
; $805D				$00
; $805E				$00
; $805F				$00
; $8060				$00
; $8061				$20
;---------------------------------
INIT_ISR_FLAG_TABLE:
        XOR     A                       ; 0094 AF       .    Clear A
        LD      (NMI_MASK_WR),A         ; 0095 3200A0   2D_  Disable NMI interrupts
        XOR     A                       ; 0098 AF       .
        LD      (KEEP_SAME_ISR_FLAG),A  ; 0099 324480   2@.  Process the next ISR table location
        

		LD      HL,ISR_FLAG_TABLE       ; 009C 215D80   !..  Point to the ISR flag table
        LD      A,$04                   ; 009F 3E04     >T   Clear 4 bytes

Lb7:    LD      (HL),$00                ; 00A1 3600     6D   Clear byte
        INC     HL                      ; 00A3 23       #    Go to next location
        DEC     A                       ; 00A4 3D       =    Decrement loop counter
        JR      NZ,Lb7                  ; 00A5 20FA      .   Done? Nope, keep looping

        LD      (HL),$20                ; 00A7 3620     6d   Write $20 to last location
        JP      ISR_3                   ; 00A9 C33702   .&.  Continue

;-----------------------------------------------------------------------------
; Clear system RAM
; Writes $00 to $8000 - $83FF
; Sets the stack pointer to $8400
;-----------------------------------------------------------------------------
INIT_RAM:
        LD      HL,RAM_START            ; 00AC 210080   !D. Point to start of RAM
        LD      DE,$400                 ; 00AF 110004   .D. $400 (1024) bytes

INIT_RAM_LOOP:    
        LD      (HL),$00                ; 00B2 3600     6D  Clear RAM address
        INC     HL                      ; 00B4 23       #   Go to next address
        DEC     DE                      ; 00B5 1B       .   Decrement counter
        LD      A,D                     ; 00B6 7A       z   Check MSByte of counter
        OR      E                       ; 00B7 B3       .   OR with LSByte of counter
        JR      NZ,INIT_RAM_LOOP        ; 00B8 20F8      .  Not zero, not done yet

        LD      SP,RAM_END_SP           ; 00BA 310084   1D. Set stack pointer to end of RAM

;-----------------------------------------------------------------------------
; Write to mixer (register 7) of sound chip and disable all mixer inputs
;-----------------------------------------------------------------------------
        LD      A,$07                   ; 00BD 3E07     >F  Select register 7 of sound chip
        OUT     (IO_SOUND_CTRL),A       ; 00BF D308     .L
        LD      A,$FF                   ; 00C1 3EFF     >.  Write $FF to register 7
        OUT     (IO_SND_W),A            ; 00C3 D309     ..

; Set machine configuration
        CALL    CK_MACH_CONFIG          ; 00C5 CDA303   ..S Check the machine configuration
 
        JP      STARTUP2                ; 00C8 C37200   .'D Continue here with the startup


;=============================================================================
; Initialize the ISR flag table
; Write data to the following address locations:
;
; $805D  $20
; $805E  $20
; $805F  $20
; $8060  $20
; $8061  $40
;=============================================================================
UPDATE_ISR_FLAG_TABLE:
        LD      HL,ISR_FLAG_TABLE       ; 00CB 215D80   !..  Point to the ISR flag table
        LD      A,$04                   ; 00CE 3E04     >.   Set 1st 4 flags

Lb11:   LD      (HL),$20                ; 00D0 3620     6d   Set flag to $20
        INC     HL                      ; 00D2 23       #    Go to next byte
        DEC     A                       ; 00D3 3D       =    Decrement counter
        JR      NZ,Lb11                 ; 00D4 20FA      .   A = 0? Nope, keep looping

        LD      (HL),$40                ; 00D6 3640     6.   Set last flag to $40
        RET                             ; 00D8 C9       .    End UPDATE_ISR_FLAG_TABLE


;------------------------------------
; Continue with interrupt processing
;------------------------------------
ISR_2:  
        PUSH    AF                      ; 00D9 F5       .   Save all registers
        PUSH    BC                      ; 00DA C5       .
        PUSH    DE                      ; 00DB D5       .
        PUSH    HL                      ; 00DC E5       .
        PUSH    IX                      ; 00DD DDE5     ..
        PUSH    IY                      ; 00DF FDE5     ..

        CALL    SAVE_STACK_PTR          ; 00E1 CD4A01   .K. Save the stack pointer

        LD      A,(MACH_SW_RD)          ; 00E4 3A00B8   :D. Pet watchdog
        LD      SP,RAM_END_SP           ; 00E7 310084   1D. Set stack pointer to end of RAM
        LD      A,(PLAY_PER_COIN)       ; 00EA 3A7A80   :/. Read plays per coin
        CP      $04                     ; 00ED FE04     .T  Is it a free play?
        JR      NZ,Lb13                 ; 00EF 2003      .  Nope, continue

        LD      (NUM_CREDITS),A         ; 00F1 327280   2#. Save number of credits

; Increment ISR counter each time the ISR is called
Lb13:   NOP                             ; 00F4 00       .
        LD      HL,ISR_COUNTER          ; 00F5 214580   !U. Point to the interrupt counter
        INC     (HL)                    ; 00F8 34       4   Increment the counter
        LD      A,(HL)                  ; 00F9 7E       ~   Check for overflow
        OR      A                       ; 00FA B7       .   Is least significant byte 0?
        JP      NZ,Lb14                 ; 00FB C20001   .D. Nope, continue

; Least significant counter byte overflow, update most significant counter byte
        INC     HL                      ; 00FE 23       #   Increment most significant counter byte
        INC     (HL)                    ; 00FF 34       4

Lb14:   CALL    CHECK_COIN_INPUTS       ; 0100 CD6301   .v. Check coin inputs

        CALL    UPDATE_SOUND            ; 0103 CD0040   .D. Update the sound
        LD      A,(GAME_IN_PROGRESS)    ; 0106 3A7580   :%. Is a game in progress?
        AND     A                       ; 0109 A7       .   
        JR      NZ,Lb17                 ; 010A 2023      s  Yes, go here

; No game in progress
; Check cocktail / upright machine type
        LD      A,(MACH_SW_RD)          ; 010C 3A00B8   :D. Read the machine switches / pet watchdog
        BIT     4,A                     ; 010F CB67     .g  Check cocktail / upright
        JR      NZ,Lb18                 ; 0111 2007      F  Cocktail? Go here

; Upright 
        LD      A,$01                   ; 0113 3E01     >.
        LD      (CURRENT_FIELD_FLAG),A  ; 0115 32B482   2.} Set current field to normal
        JR      Lb17                    ; 0118 1815     .Q

; Cocktail
Lb18:   LD      A,(CURRENT_FIELD_FLAG)  ; 011A 3AB482   :K. Read current field setting
        AND     A                       ; 011D A7       .   Is field already inverted?
        JR      Z,Lb17                  ; 011E 280F     (.  Yes, continue

; Play a sample sound
        LD      HL,$4CC0                ; 0120 21C04C   !.H
        LD      (SNDS_DATA_PTR),HL      ; 0123 222480   "t. Set the sample data pointer
        LD      A,$84                   ; 0126 3E84     >.
        LD      (SNDS_INIT_CNT),A       ; 0128 322780   2". Initialize the sample sound counter
        XOR     A                       ; 012B AF       .   Set current field to inverted
        LD      (CURRENT_FIELD_FLAG),A  ; 012C 32B482   2K.

Lb17:   CALL    CHECK_ISR_TIMERS        ; 012F CDE301   ... Check/update time-slice timers
        LD      A,(PLAYER_DIED_FLAG)    ; 0132 3A7380   :.. Get the player died flag
        AND     $01                     ; 0135 E601     ..  Has player died?
        JP      NZ,Lb20                 ; 0137 C28500   ..D Yes, go here

        CALL    Lb21                    ; 013A CDFC01   ... Handle setting bit 6
        CALL    Lb21                    ; 013D CDFC01   ... Handle setting bit 6
        JP      ISR_3                   ; 0140 C33702   .wG


;=============================================================================
; Saves the location of the ISR jump table to the ISR_JUMP_TABLE_PTR variable.
;=============================================================================
SET_JUMP_TABLE_PTR:    
        LD      HL,ISR_JUMP_TABLE       ; 0143 218903   !.S  Point to ISR jump table
        LD      (ISR_JUMP_TABLE_PTR),HL ; 0146 224280   "..  Save this value
        RET                             ; 0149 C9       .    End SET_JUMP_TABLE_PTR



;=============================================================================
; SAVE_STACK_POINTER
;
; Saves the current stack pointer in the stack pointer table.  The index to
; this table is ISR_INDEX (interrupt service routine index).
;
; If ISR_INDEX is $FF, then it is uninitialized, and the stack pointer is
; not saved.
;
; If is not $FF, then the stack pointer is saved at 
;
;              SP_SAVE_TABLE + 2 * Index
;=============================================================================
SAVE_STACK_PTR:
        PUSH    AF                      ; 014A F5       .   Save A and flags
        LD      HL,(ISR_INDEX)          ; 014B 2A4080   *Q. Get the ISR index value
        LD      A,L                     ; 014E 7D       }   
        CP      $FF                     ; 014F FEFF     ..  Is the ISR index not initialized?
        JR      Z,Lb22                  ; 0151 280E     (.  Yes, exit routine

        LD      DE,SP_SAVE_TABLE        ; 0153 114980   ... DE = start of stack pointer save table
        ADD     HL,HL                   ; 0156 29       )   HL = 2 * ISR_INDEX
        ADD     HL,DE                   ; 0157 19       .   HL = SP_SAVE_TABLE + (2*ISR_INDEX)
        EX      DE,HL                   ; 0158 EB       .   DE = SP_SAVE_TABLE + (2*ISR_INDEX)
        LD      HL,$04                  ; 0159 210400   !TD HL = $04
        ADD     HL,SP                   ; 015C 39       9   HL = SP + $04
        EX      DE,HL                   ; 015D EB       .   HL <-> DE
        LD      (HL),E                  ; 015E 73       s   Write contents of SP + $04 to SP_SAVE_TABLE + (2*ISR_INDEX)
        INC     HL                      ; 015F 23       #
        LD      (HL),D                  ; 0160 72       r

Lb22:   POP     AF                      ; 0161 F1       .   
        RET                             ; 0162 C9       .   End SAVE_STACK_PTR


;=============================================================================
; Checks the coin machine switches.
;
; COIN_PRESENT - Set to 1 if a coin is present, 0 otherwise
;
; If COIN_PRESENT = 1, then COIN_SLOT should be looked at.  If COIN_SLOT = 0,
; then the coin was from slot 1.  If COIN_SLOT = 1, the coin was from slot 2.
;=============================================================================
CHECK_COIN_INPUTS:
        LD      A,(MACH_SW_RD)          ; 0163 3A00B8   :D. Read the machine switches
        AND     $01                     ; 0166 E601     ..  Look at coin 1 switch
        JP      NZ,Lb23                 ; 0168 C2CD01   ... Got a coin? Go here

        LD      A,(MACH_SW_RD)          ; 016B 3A00B8   :D. Read the machine switches
        AND     $02                     ; 016E E602     ..  Look at coin 2 switch
        JP      NZ,Lb24                 ; 0170 C2D801   ... Got a coin? Go here

        LD      A,(COIN_PRESENT)        ; 0173 3A7180   :$. Coin present?
        OR      A                       ; 0176 B7       .   
        RET     Z                       ; 0177 C8       .   Nope, end CHECK_COIN_INPUTS

; Got a coin - Check the coin slot
        LD      A,(COIN_SLOT)           ; 0178 3A7780   :#. Check which coin slot
        OR      A                       ; 017B B7       .   Is in slot 1?
        JR      Z,Lb25                  ; 017C 2820     (d  Yes, go here

; Coin in slot 2
        LD      A,(NUM_CREDITS)         ; 017E 3A7280   :'. Read number of credits
        CP      $50                     ; 0181 FE50     .E  Equal to $50 (50) plays?
        JR      NZ,Lb26                 ; 0183 3009     0.  Nope, continue

        LD      B,A                     ; 0185 47       G
        LD      A,(PLAY_PER_COIN)       ; 0186 3A7A80   :/. Read plays per coin
        ADD     A,B                     ; 0189 80       .   Add this to number of plays
        DAA                             ; 018A 27       '   Decimal adjust A, so value is shown in decimal, not hex
        LD      (NUM_CREDITS),A         ; 018B 327280   2#. Save number of credits

Lb26:   XOR     A                       ; 018E AF       .   
        LD      (COIN_PRESENT),A        ; 018F 327180   2$. Clear coin present flag
        LD      A,(GAME_IN_PROGRESS)    ; 0192 3A7580   :%. Is a game in progress?
        OR      A                       ; 0195 B7       .
        RET     NZ                      ; 0196 C0       .   Yes, end CHECK_COIN_INPUTS

; No game in progress
        XOR     A                       ; 0197 AF       .
        LD      (KEEP_SAME_ISR_FLAG),A  ; 0198 324480   2.. Process the next ISR table location
        JP      STARTUP2                ; 019B C37200   .#D

; Coin in slot 1
Lb25:   LD      A,(COINS_INSERTED)      ; 019E 3A7980   :|. Increment number of coins inserted
        INC     A                       ; 01A1 3C       <
        LD      (COINS_INSERTED),A      ; 01A2 327980   2|.
        LD      B,A                     ; 01A5 47       G   B = # coins inserted

        XOR     A                       ; 01A6 AF       .
        LD      (COIN_PRESENT),A        ; 01A7 327180   2$. Clear coin present flag

        LD      A,(COIN_PER_PLAY)       ; 01AA 3A7880   :). Get the number of coins per play
        CP      B                       ; 01AD B8       .   # coins inserted = # coins per play?
        RET     NZ                      ; 01AE C0       .   Nope, end CHECK_COIN_INPUTS

; Got enough coins inserted to begin play
        LD      A,$00                   ; 01AF 3E00     >D  Clear # coins inserted
        LD      (COINS_INSERTED),A      ; 01B1 327980   2,.

        LD      A,(NUM_CREDITS)         ; 01B4 3A7280   :'. Get number of credits
        CP      $50                     ; 01B7 FE50     .E  Equal to 50? (Decimal adjusted...)
        JR      NZ,Lb27                 ; 01B9 3006     0.  Nope, continue

        ADD     A,$01                   ; 01BB C601     ..  Add one to number of credits 
        DAA                             ; 01BD 27       '   Decimal adjust, so value is not in hex
        LD      (NUM_CREDITS),A         ; 01BE 327280   2'. Save number of credits

Lb27:   LD      A,(GAME_IN_PROGRESS)    ; 01C1 3A7580   :5. Is a game in progress?
        OR      A                       ; 01C4 B7       .
        RET     NZ                      ; 01C5 C0       .   Yes, end CHECK_COIN_INPUTS

; No game in progress
        XOR     A                       ; 01C6 AF       .
        LD      (KEEP_SAME_ISR_FLAG),A  ; 01C7 324480   2@. Process the next ISR table location
        JP      STARTUP2                ; 01CA C37200   .'D

; Got a coin in slot 1
Lb23:   LD      A,$00                   ; 01CD 3E00     >D
        LD      (COIN_SLOT),A           ; 01CF 327780   2". Coin in slot 1
        LD      A,$01                   ; 01D2 3E01     >.
        LD      (COIN_PRESENT),A        ; 01D4 327180   2t. A coin is present
        RET                             ; 01D7 C9       .   End CHECK_COIN_INPUTS

; Got a coin in slot 2
Lb24:   LD      A,$01                   ; 01D8 3E01     >.
        LD      (COIN_SLOT),A           ; 01DA 327780   2#. Coin in slot 2
        LD      A,$01                   ; 01DD 3E01     >.
        LD      (COIN_PRESENT),A        ; 01DF 327180   2$. A coin is present
        RET                             ; 01E2 C9       .   End CHECK_COIN_INPUTS



;=============================================================================
; Name:		CHECK_ISR_TIMERS
;
; Description:
;
; This subroutine checks the time-slice timers.  If a timer counts down to
; zero, the corresponding ISR flags' bit 4 is cleared, indicating that it is
; time to run that location's routines.
;=============================================================================
CHECK_ISR_TIMERS:
        LD      B,$0A                   ; 01E3 060A     .O  Check 10 locations
        LD      HL,ISR_TIMER_TABLE      ; 01E5 216780   !b. ISR timer table
        LD      DE,ISR_FLAG_TABLE       ; 01E8 115D80   ... Point DE to the ISR flag table

Lb30:   XOR     A                       ; 01EB AF       .
        CP      (HL)                    ; 01EC BE       .   Is timer zero?
        JR      Z,Lb28                  ; 01ED 2803     (.  Yes, go here

        DEC     (HL)                    ; 01EF 35       5   Decrement timer?
        JR      NZ,Lb29                 ; 01F0 2004      .  Timer zero? Nope, continue here

; Clears bit 4 from the ISR flag (Timer counted down to zero)
Lb28:   LD      A,(DE)                  ; 01F2 1A       .
        AND     $EF                     ; 01F3 E6EF     ..  Clear bit 4 from the flag
        LD      (DE),A                  ; 01F5 12       .

Lb29:   INC     HL                      ; 01F6 23       #   Go to next timer
        INC     DE                      ; 01F7 13       .   Go to next flag
        DEC     B                       ; 01F8 05       .   Decrement counter
        JR      NZ,Lb30                 ; 01F9 20F0      .  Done? Nope, keep looping
        RET                             ; 01FB C9       .   End CHECK_ISR_TIMERS



;=============================================================================
; Handle ISR flag's bit 6 setting for the first 4 locations.
;
; Location	Comments for ISR flag
; --------	----------------------------------
; 0			Bit 6 is always set
; 1			Set bit 6 on every third interrupt (ISR_COUNTER mod 3)
; 2			Bit 6 is always set
; 3			Set bit 6 if ISR_COUNTER is even (every 2nd interrupt)
;=============================================================================
; Check ISR flag 0
Lb21:   LD      HL,ISR_FLAG_TABLE       ; 01FC 215D80   !.. Point to the ISR flag table
        LD      A,(ISR_COUNTER)         ; 01FF 3A4580   :U. Get ISR counter
        AND     $00                     ; 0202 E600     .D  A = 0
        CP      $00                     ; 0204 FE00     .D  Always true
        JR      NZ,Lb31                 ; 0206 2004      .  Never branches

        LD      A,(HL)                  ; 0208 7E       ~
        OR      $40                     ; 0209 F640     .Q  Set bit 6 of the ISR flag
        LD      (HL),A                  ; 020B 77       w

; Check ISR flag 1
Lb31:   INC     HL                      ; 020C 23       #   Go to next ISR flag
        LD      A,(ISR_COUNTER)         ; 020D 3A4580   :U. Get ISR counter
        AND     $03                     ; 0210 E603     .S  Isolate bits 0 and 1
        CP      $03                     ; 0212 FE03     .S  Are bits 0 & 1 set?
        JR      NZ,Lb32                 ; 0214 2004      .  Nope, continue

        LD      A,(HL)                  ; 0216 7E       ~
        OR      $40                     ; 0217 F640     .Q  Set bit 6 of the ISR flag
        LD      (HL),A                  ; 0219 77       w

; Check ISR flag 2
Lb32:   INC     HL                      ; 021A 23       #   Go to next ISR flag
        LD      A,(ISR_COUNTER)         ; 021B 3A4580   :U. Get ISR counter
        AND     $00                     ; 021E E600     .D  A = 0
        CP      $00                     ; 0220 FE00     .D  
        JR      NZ,Lb33                 ; 0222 2004      .  Never branches

        LD      A,(HL)                  ; 0224 7E       ~
        OR      $40                     ; 0225 F640     .Q  Set bit 6 of the ISR flag
        LD      (HL),A                  ; 0227 77       w

; Check ISR flag 3
Lb33:   INC     HL                      ; 0228 23       #   Go to next ISR flag
        LD      A,(ISR_COUNTER)         ; 0229 3A4580   :U. Get ISR counter
        AND     $01                     ; 022C E601     ..  Isolate bit 0
        CP      $00                     ; 022E FE00     .D  Is bit 0 clear?
        JR      NZ,Lb34                 ; 0230 2004      .  Yes, continue

        LD      A,(HL)                  ; 0232 7E       ~
        OR      $40                     ; 0233 F640     .Q  Set bit 6 of the ISR flag
        LD      (HL),A                  ; 0235 77       w

Lb34:   RET                             ; 0236 C9       .


;-----------------------------------------------------------------------------
; Complete ISR processing
;-----------------------------------------------------------------------------
ISR_3:
        LD      A,(MACH_SW_RD)          ; 0237 3A00B8   :D. Pet the watchdog
        LD      A,(KEEP_SAME_ISR_FLAG)  ; 023A 3A4480   :.. Get exit ISR flag value
        OR      A                       ; 023D B7       .   Keep the current ISR table value to process?
        JR      NZ,END_ISR              ; 023E 2032      f  Yes, end the ISR

; Search the ISR table for the next "time slice" to process
        LD      A,$FF                   ; 0240 3EFF     >.
        LD      (ISR_INDEX),A           ; 0242 324080   2..  Set the ISR index to not initialized

Lb39:   XOR     A                       ; 0245 AF       .    
        LD      (NMI_MASK_WR),A         ; 0246 3200A0   2D.  Disable NMI interrupts
        LD      A,$01                   ; 0249 3E01     >.   
        LD      (NMI_MASK_WR),A         ; 024B 3200A0   2D_  Enable NMI interrupts


;----------------------------------------------------------------
; Search through the flag table
; If bits 6 or 7 are set, then the we exit the loop
; (This may mark the end of the ISR list)
; C will contain the index into the table when we exit the loop 
;----------------------------------------------------------------
        LD      BC,$A00                 ; 024E 01000A   .DO B = 10 table locations, C = 0 (current index)
        LD      HL,ISR_FLAG_TABLE       ; 0251 215D80   !.. Point to the ISR flag table

Lb38:   LD      A,(HL)                  ; 0254 7E       ~   Get the flag
        AND     $30                     ; 0255 E630     .1  Are bits 4 or 5 set?
        JR      NZ,Lb36                 ; 0257 2005      .  Yes, continue looping

; Look for the end flag?
        LD      A,(HL)                  ; 0259 7E       ~   Get the flag
        AND     $C0                     ; 025A E6C0     ..  Are bits 6 or 7 set?
        JR      NZ,Lb37                 ; 025C 2007      .  Yes - exit loop

Lb36:   INC     HL                      ; 025E 23       #   Go to next flag byte in table
        INC     C                       ; 025F 0C       .   Increment our index
        DEC     B                       ; 0260 05       .   Decrement loop counter
        JR      NZ,Lb38                 ; 0261 20F1      .  Done? Nope, keep looping

; At end of table, but could not find proper flags set.
        JR      Lb39                    ; 0263 18E0     ..  Try again...


; Done searching the ISR flag table
;
; C contains the flag table index
Lb37:   XOR     A                       ; 0265 AF       .   Clear A
        LD      (NMI_MASK_WR),A         ; 0266 3200A0   2D. Disable NMI interrupts
        LD      A,C                     ; 0269 79       y 
        LD      (ISR_INDEX),A           ; 026A 324080   2.. Save the new ISR index value
        LD      A,(HL)                  ; 026D 7E       ~   Get current flag value
        AND     $80                     ; 026E E680     ..  Check bit 7
        JR      Z,Lb40                  ; 0270 2820     (d  Zero? Yup, go here

;--------------------------------------------------------------------
; Retrieve the stack pointer that was saved at the start of the ISR
;
END_ISR:
        LD      HL,(ISR_INDEX)          ; 0272 2A4080   *.. Get the ISR index value
        LD      DE,SP_SAVE_TABLE        ; 0275 114980   ... Base of the ISR stack pointer table
        ADD     HL,HL                   ; 0278 29       )   
        ADD     HL,DE                   ; 0279 19       .   HL = SP_SAVE_TABLE + (2*ISR_INDEX)
        LD      E,(HL)                  ; 027A 5E       ^   Retrieve the address saved here
        INC     HL                      ; 027B 23       #
        LD      D,(HL)                  ; 027C 56       V
        EX      DE,HL                   ; 027D EB       .   DE contains the saved stack value
        LD      SP,HL                   ; 027E F9       .   Point stack to proper return address

        POP     IY                      ; 027F FDE1     ..  Restore all registers except A
        POP     IX                      ; 0281 DDE1     ..
        POP     HL                      ; 0283 E1       .
        POP     DE                      ; 0284 D1       .
        POP     BC                      ; 0285 C1       .
        XOR     A                       ; 0286 AF       .   Clear A
        LD      (NMI_MASK_WR),A         ; 0287 3200A0   2D_ Disable NMI interrupts
        LD      A,$01                   ; 028A 3E01     >.  A = 1
        LD      (NMI_MASK_WR),A         ; 028C 3200A0   2D. Enable NMI interrupts
        POP     AF                      ; 028F F1       .   Restore AF
        RETN                            ; 0290 ED45     .E  Return from NMI (and restores flags)


; HL points to the ISR flag table
Lb40:   LD      (HL),$80                ; 0292 3680     6.  Set flag to $80 (end of table, initialized?)

; Set the stack pointer with the proper value in the stack set table
        LD      HL,(ISR_INDEX)          ; 0294 2A4080   *.. Get the ISR index value
        LD      DE,ISR_STACK_SET_TABLE  ; 0297 119503   ..S Point to ISR stack pointer table
        ADD     HL,HL                   ; 029A 29       )
        ADD     HL,DE                   ; 029B 19       .   HL = ISR_STACK_SET_TABLE + (2 * ISR_INDEX)
        LD      E,(HL)                  ; 029C 5E       ^   Get the value
        INC     HL                      ; 029D 23       #
        LD      D,(HL)                  ; 029E 56       V
        EX      DE,HL                   ; 029F EB       .
        LD      SP,HL                   ; 02A0 F9       .   Set stack pointer for return

; Get jump address from the ISR jump table
        LD      HL,(ISR_INDEX)          ; 02A1 2A4080   *Q. Get the ISR index value
        EX      DE,HL                   ; 02A4 EB       .
        LD      HL,(ISR_JUMP_TABLE_PTR) ; 02A5 2A4280   *C. HL points to the ISR jump table
        ADD     HL,DE                   ; 02A8 19       .
        ADD     HL,DE                   ; 02A9 19       .   HL = ISR_JUMP_TABLE_PTR + (2 * ISR_INDEX)
        LD      E,(HL)                  ; 02AA 5E       ^   Load DE with the jump address
        INC     HL                      ; 02AB 23       #
        LD      D,(HL)                  ; 02AC 56       V
        EX      DE,HL                   ; 02AD EB       .   Load HL with the jump address
        XOR     A                       ; 02AE AF       .   
        LD      (NMI_MASK_WR),A         ; 02AF 3200A0   2D_ Disable NMI interrupts
        LD      A,$01                   ; 02B2 3E01     >.  
        LD      (NMI_MASK_WR),A         ; 02B4 3200A0   2D. Enable NMI interrupts

; Jump to the proper address
        JP      (HL)                    ; 02B7 E9       .   (On startup, this goes to $0572)



;=============================================================================
; Delay routine
;
; Input:
;
;	A - Delay loops
;
;=============================================================================
DELAY:   
        PUSH    AF                      ; 02B8 F5       .
        XOR     A                       ; 02B9 AF       .   Clear A
        LD      (NMI_MASK_WR),A         ; 02BA 3200A0   2D. Disable NMI interrupts
        POP     AF                      ; 02BD F1       .

        PUSH    AF                      ; 02BE F5       .   Save registers used
        PUSH    BC                      ; 02BF C5       .
        PUSH    DE                      ; 02C0 D5       .
        PUSH    HL                      ; 02C1 E5       .
        PUSH    IX                      ; 02C2 DDE5     ..
        PUSH    IY                      ; 02C4 FDE5     ..

        PUSH    AF                      ; 02C6 F5       .   Save AF

        LD      A,(KEEP_SAME_ISR_FLAG)  ; 02C7 3A4480   :@. Get ISR exit flag
        OR      A                       ; 02CA B7       .   
        JR      Lb41                    ; 02CB 181D     .X

; Unreachable code?
        POP     AF                      ; 02CD F1       .   Restore AF

        CALL    SAVE_STACK_PTR          ; 02CE CD4A01   ... Save the stack pointer

        LD      SP,RAM_END_SP           ; 02D1 310084   1D. Set stack pointer to end of RAM
        LD      HL,(ISR_INDEX)          ; 02D4 2A4080   *.. Get the ISR index value
        LD      DE,ISR_TIMER_TABLE      ; 02D7 116780   .b. Point to the ISR timer table
        ADD     HL,DE                   ; 02DA 19       .
        LD      (HL),A                  ; 02DB 77       w
        LD      HL,(ISR_INDEX)          ; 02DC 2A4080   *.. Get the ISR index value
        LD      DE,ISR_FLAG_TABLE       ; 02DF 115D80   ... Point DE to the ISR flag table
        ADD     HL,DE                   ; 02E2 19       .

; Set bit 4 of the ISR flag
        LD      A,(HL)                  ; 02E3 7E       ~
        OR      $10                     ; 02E4 F610     ..  Set bit 4 of the ISR flag 
        LD      (HL),A                  ; 02E6 77       w

        JP      ISR_3                   ; 02E7 C33702   .&. Finish ISR routine


Lb41:   XOR     A                       ; 02EA AF       .   Clear A
        LD      (NMI_MASK_WR),A         ; 02EB 3200A0   2D_ Disable NMI interrupts
        LD      A,$01                   ; 02EE 3E01     >.  A = 1
        LD      (NMI_MASK_WR),A         ; 02F0 3200A0   2D. Enable NMI interrupts
        POP     AF                      ; 02F3 F1       .   Restore AF

; A decrement loop
Lb44:   SUB     $01                     ; 02F4 D601     ..  Decrement A
        JR      C,Lb42                  ; 02F6 380E     8O  < 0?  Yes, done with delay

        PUSH    AF                      ; 02F8 F5       .   Save AF
        LD      HL,$100                 ; 02F9 210001   !D. HL is the loop counter (256 loops)

; Timing loop
Lb43:   PUSH    HL                      ; 02FC E5       .   Waste some time
        POP     HL                      ; 02FD E1       .
        DEC     HL                      ; 02FE 2B       +   Decrement counter
        LD      A,H                     ; 02FF 7C       |   
        OR      L                       ; 0300 B5       .
        JR      NZ,Lb43                 ; 0301 20F9      .  Not done? Keep looping

        POP     AF                      ; 0303 F1       .   Restore AF
        JR      Lb44                    ; 0304 18EE     ..  Keep looping

Lb42:   POP     IY                      ; 0306 FDE1     ..  Restore registers used
        POP     IX                      ; 0308 DDE1     ..
        POP     HL                      ; 030A E1       .
        POP     DE                      ; 030B D1       .
        POP     BC                      ; 030C C1       .
        POP     AF                      ; 030D F1       .
        RET                             ; 030E C9       .   Done with delay


;=============================================================================
; Does not return from call.  It goes back to the ISR end processing
;
; This routine clears bit 7 of the current ISR flag.
;=============================================================================
Lb208:  XOR     A                       ; 030F AF       .   Clear A
        LD      (NMI_MASK_WR),A         ; 0310 3200A0   2D. Disable NMI interrupts
        LD      HL,(ISR_INDEX)          ; 0313 2A4080   *Q. Get the ISR index value
        LD      DE,ISR_FLAG_TABLE       ; 0316 115D80   ... DE points to the ISR flag table
        ADD     HL,DE                   ; 0319 19       .   Index into the ISR flag table

; Clear bit 7 of the current ISR flag
        LD      A,(HL)                  ; 031A 7E       ~   
        AND     $7F                     ; 031B E67F     .*  Clear bit 7 of ISR flag value
        LD      (HL),A                  ; 031D 77       w   
        JP      ISR_3                   ; 031E C33702   .wG Continue end of ISR processing



;=============================================================================
; Sets bit 5 in the ISR flag table
;=============================================================================
Lb255:  PUSH    AF                      ; 0321 F5       .
        XOR     A                       ; 0322 AF       .   Clear A
        LD      (NMI_MASK_WR),A         ; 0323 3200A0   2D_ Disable NMI interrupts
        POP     AF                      ; 0326 F1       .
        PUSH    AF                      ; 0327 F5       .
        PUSH    BC                      ; 0328 C5       .
        PUSH    DE                      ; 0329 D5       .
        PUSH    HL                      ; 032A E5       .
        PUSH    IX                      ; 032B DDE5     ..
        PUSH    IY                      ; 032D FDE5     ..
        CALL    SAVE_STACK_PTR          ; 032F CD4A01   .K. Save the stack pointer
        LD      SP,RAM_END_SP           ; 0332 310084   1D. Set stack pointer to end of RAM
        LD      HL,ISR_FLAG_TABLE       ; 0335 215D80   !..
        LD      D,$00                   ; 0338 1600     .D
        LD      E,A                     ; 033A 5F       _
        ADD     HL,DE                   ; 033B 19       .
        LD      A,(HL)                  ; 033C 7E       ~
        OR      $20                     ; 033D F620     .d
        LD      (HL),A                  ; 033F 77       w
        JP      ISR_3                   ; 0340 C33702   .wG


; Sets bit 6 in the ISR flag table (never executed?)
        PUSH    AF                      ; 0343 F5       .
        XOR     A                       ; 0344 AF       .   Clear A
        LD      (NMI_MASK_WR),A         ; 0345 3200A0   2D_ Disable NMI interrupts
        POP     AF                      ; 0348 F1       .
        PUSH    AF                      ; 0349 F5       .
        PUSH    BC                      ; 034A C5       .
        PUSH    DE                      ; 034B D5       .
        PUSH    HL                      ; 034C E5       .
        PUSH    IX                      ; 034D DDE5     ..
        PUSH    IY                      ; 034F FDE5     ..
        CALL    SAVE_STACK_PTR          ; 0351 CD4A01   .K. Save the stack pointer
        LD      SP,RAM_END_SP           ; 0354 310084   1D. Set stack pointer to end of RAM
        LD      HL,ISR_FLAG_TABLE       ; 0357 215D80   !..
        LD      D,$00                   ; 035A 1600     .D
        LD      E,A                     ; 035C 5F       _
        ADD     HL,DE                   ; 035D 19       .
        LD      A,(HL)                  ; 035E 7E       ~
        OR      $40                     ; 035F F640     .Q
        LD      (HL),A                  ; 0361 77       w
        JP      ISR_3                   ; 0362 C33702   .wG

;=============================================================================
; Clears bit 5 in the ISR flag table
;=============================================================================
Lb223:  PUSH    AF                      ; 0365 F5       .
        XOR     A                       ; 0366 AF       .   Clear A
        LD      (NMI_MASK_WR),A         ; 0367 3200A0   2D_ Disable NMI interrupts
        POP     AF                      ; 036A F1       .
        PUSH    AF                      ; 036B F5       .
        PUSH    BC                      ; 036C C5       .
        PUSH    DE                      ; 036D D5       .
        PUSH    HL                      ; 036E E5       .
        PUSH    IX                      ; 036F DDE5     ..
        PUSH    IY                      ; 0371 FDE5     ..
        CALL    SAVE_STACK_PTR          ; 0373 CD4A01   .K.  Save the stack pointer
        LD      SP,RAM_END_SP           ; 0376 310084   1D.  Set stack pointer to end of RAM
        LD      HL,ISR_FLAG_TABLE       ; 0379 215D80   !..
        LD      D,$00                   ; 037C 1600     .D
        LD      E,A                     ; 037E 5F       _
        ADD     HL,DE                   ; 037F 19       .
        LD      A,(HL)                  ; 0380 7E       ~
        AND     $DF                     ; 0381 E6DF     ..
        LD      (HL),A                  ; 0383 77       w
        JP      ISR_3                   ; 0384 C33702   .wG

;-------------------------------------------------------------------------------
; Data Start
; Range: $0387 - $03A2
;-------------------------------------------------------------------------------

        .db     $C7, $FB								; Start data block

; ($0389) - Jump address table
ISR_JUMP_TABLE:
		.db     $20, $10		; $1020 - Index 0 (ISR_JUMP0)
		.db     $90, $13		; $1390 - Index 1 (ISR_JUMP1)
		.db     $40, $1B		; $1B40 - Index 2 (ISR_JUMP2)
		.db     $10, $28		; $2810 - Index 3 (ISR_JUMP3)
		.db     $72, $05		; $0572 - Index 4 (ISR_JUMP4)
		.db     $54, $04		; $0454 - Index 5 (ISR_JUMP5) - Increment Counter

; ($0395) - Return Address table
ISR_STACK_SET_TABLE:
		.db     $E0, $83		; $83E0 - Index 0
		.db     $A8, $83		; $83A8 - Index 1
		.db     $70, $83		; $8370 - Index 2
		.db     $38, $83		; $8338 - Index 3
		.db     $E0, $83		; $83E0 - Index 4
		.db     $00, $83		; $8300 - Index 5

		.db     $C7, $F3								; End data block



;=============================================================================
; Check machine configuration
;=============================================================================
CK_MACH_CONFIG:

; Read dip switches 1 & 2 (# lives)
        NOP                             ; 03A3 00       .
        LD      A,(DIP_SW_RD)           ; 03A4 3A00B0   :D. Read the DIP switches
        AND     $03                     ; 03A7 E603     ..  Isolate the number of lives
        ADD     A,$03                   ; 03A9 C603     ..  Add three to this value (range 3 - 6)
        LD      (MAX_LIVES),A           ; 03AB 327E80   2.. Save maximum number of lives

        LD      A,(MACH_SW_RD)          ; 03AE 3A00B8   :D. Read the machine switches
        AND     $10                     ; 03B1 E610     ..  Isolate Table/upright bit
        JR      NZ,Lb46                 ; 03B3 2007      F  If 1, then upright -- go here

; Table version
        LD      A,$00                   ; 03B5 3E00     >D  A = 0
        LD      (MACH_VER),A            ; 03B7 327C80   2). Save table version (0)
        JR      Lb47                    ; 03BA 1805     .U

; Upright version
Lb46:   LD      A,$01                   ; 03BC 3E01     >.  A = 1 
        LD      (MACH_VER),A            ; 03BE 327C80   2,. Save upright version (1)

;---------------------------------------------------------
; Read dip switch 3 (Extra life bonus) (30,000 or 50,000)
;---------------------------------------------------------
Lb47:   LD      A,(DIP_SW_RD)           ; 03C1 3A00B0   :D. Read the DIP switches
        AND     $04                     ; 03C4 E604     ..  Isolate extra climber bonus
        JR      NZ,Lb48                 ; 03C6 2007      .  Not zero -- goto 50,000 climber bonus

; 30,000 climber bonus
        LD      A,$00                   ; 03C8 3E00     >D  A = 0
        LD      (BONUS_LIFE),A          ; 03CA 327680   26. Save for 30,000 bonus
        JR      Lb49                    ; 03CD 1805     ..  Continue

; 50,000 climber bonus
Lb48:   LD      A,$01                   ; 03CF 3E01     >.  A = 1
        LD      (BONUS_LIFE),A          ; 03D1 327680   2w. Save for 50,000 bonus

;-----------------------------------------------------------------------------
; Check Dip switch 7
;
; Note: This is a bug in the code.  Dip switch 3 (bit 2) is supposed to be
; used for extra lives.  When off, an extra life is given at 30,000, and when
; on, at 50,000 points.
;
; BONUS_LIFE is set properly above: 0 for 30,000 and 1 for 50,000 -- but this
; value is not used anywhere in the code after this point.
;
; The following code ANDs the dip switch value with $40, instead of $04.  This
; isolates the wrong bit!  If dip switch 7 (bit 6) is set OFF, then a bonus
; life will be awarded at 30,000 (Note: this would be coin slot #2 with 1 or
; 3 plays per coin).   If this switch is ON, then a bonus life would be
; awarded at 50,000 (Note: This would be coin slot #2 with 2 plays per coin
; or a free play).
;
; As it is now, it does not matter what the position of dip switch 3 is, it
; is overridden by dip switch 7!
;-----------------------------------------------------------------------------
Lb49:   LD      A,(DIP_SW_RD)           ; 03D4 3A00B0   :D. Read the DIP switches

; !!This should be AND $04 here!!
        AND     $40                     ; 03D7 E640     .Q  Isolate bit 6 of plays per credit
        JR      NZ,Lb50                 ; 03D9 2007      F  

        LD      A,$03                   ; 03DB 3E03     >.  Write 3 if bit 6 is OFF (1play/coin or 3play/coin)
        LD      (BONUS_LIFE_SCORE),A    ; 03DD 327D80   2=. (Bonus life at 30,000)
        JR      Lb51                    ; 03E0 1805     .U

Lb50:   LD      A,$05                   ; 03E2 3E05     >U  Write 5 if bin 6 is ON (2plays/coin or free play)
        LD      (BONUS_LIFE_SCORE),A    ; 03E4 327D80   2-. (Bonus life at 50,000)

;-------------------------------------------------------------------
; Check dip switches  5 & 6 - Coin slot selector 1 (Coins per play)
;-------------------------------------------------------------------
Lb51:   LD      A,(DIP_SW_RD)           ; 03E7 3A00B0   :D. Read the DIP switches
        RRCA                            ; 03EA 0F       .
        RRCA                            ; 03EB 0F       .
        RRCA                            ; 03EC 0F       .
        RRCA                            ; 03ED 0F       .
        AND     $03                     ; 03EE E603     .S  Isolate the coins per credit
        ADD     A,$01                   ; 03F0 C601     ..  Add one (Range 1 - 4)
        LD      (COIN_PER_PLAY),A       ; 03F2 327880   2). Save coins per play

;----------------------------------------------------------------
; Check dip switches 7 & 8 - Coin selector 2 (Plays per coin)
;----------------------------------------------------------------
        LD      A,(DIP_SW_RD)           ; 03F5 3A00B0   :D. Read the DIP switches
        RRCA                            ; 03F8 0F       .
        RRCA                            ; 03F9 0F       .
        RRCA                            ; 03FA 0F       .   
        RRCA                            ; 03FB 0F       .
        RRCA                            ; 03FC 0F       .
        RRCA                            ; 03FD 0F       .
        AND     $03                     ; 03FE E603     .S  Isolate the plays per coin
        ADD     A,$01                   ; 0400 C601     ..  Add one to the value (range 1 - 4, 4 is a free play)
        LD      (PLAY_PER_COIN),A       ; 0402 327A80   2/. Save the value

;-----------------------------------------------------------------------------
; Initialize the high score table names
;
; Writes data from the HI_SCORE_INIT_DATA region to the high score table
; 
; 5 high score locations
; 10 bytes of info in each
;
; The initialized data is "Nichibutsu  " for the character data
;
; Source         Destination    # bytes
; -------------  -------------  -------
; $043E - $0447  $8095 - $809E  10       Name 1
; $043E - $0447  $80A3 - $80AC  10       Name 2
; $043E - $0447  $80B1 - $80BA  10       Name 3
; $043E - $0447  $80BF - $80C8  10       Name 4
; $043E - $0447  $80CD - $80D6  10       Name 5
;-----------------------------------------------------------------------------
        LD      HL,HS_NAME1             ; 0405 219580   !..  Point to the 1st high score name
        LD      B,$05                   ; 0408 0605     .U   5 high score locations

Lb53:   LD      C,$0A                   ; 040A 0E0A     ..   10 bytes per high score location
        LD      IX,HI_SCORE_INIT_DATA   ; 040C DD213E04 .!{. Point to high score init data

Lb52:   LD      A,(IX+$00)              ; 0410 DD7E00   .~D  Get initialization data
        LD      (HL),A                  ; 0413 77       w    Save to high score table
        INC     HL                      ; 0414 23       #    Go to next table location
        INC     IX                      ; 0415 DD23     .#   Go to next init data location
        DEC     C                       ; 0417 0D       .    Decrement byte counter
        JR      NZ,Lb52                 ; 0418 20F6      .   Done?  Nope, keep looping

        INC     HL                      ; 041A 23       #    Done with this location
        INC     HL                      ; 041B 23       #    Point to the next name location (4 bytes away)
        INC     HL                      ; 041C 23       #    
        INC     HL                      ; 041D 23       #    
        DEC     B                       ; 041E 05       .    Decrement location counter
        JR      NZ,Lb53                 ; 041F 20E9      .   Done? Nope, keep looping


;-----------------------------------------------------------------------------
; Initialize the high score table scores
;
; Set score to 20,000 for each high score.
;
; Source data     Destination address
; -------------   -------------------
; $02, $00, $00   $8083 - $8085 (High score 1)
; $02, $00, $00   $8086 - $8088 (High score 2)
; $02, $00, $00   $8089 - $808B (High score 3)
; $02, $00, $00   $808C - $808E (High score 4)
; $02, $00, $00   $808F - $8091 (High score 5)
;-----------------------------------------------------------------------------
        LD      HL,HI_SCORE_VAL1        ; 0421 218380   !.. Set destination address in RAM
        LD      B,$05                   ; 0424 0605     .U  5 high scores

Lb54:   LD      (HL),$02                ; 0426 3602     6.  Write $02 00 00 (20000) in BCD
        INC     HL                      ; 0428 23       #   
        LD      (HL),$00                ; 0429 3600     6D  
        INC     HL                      ; 042B 23       #   
        LD      (HL),$00                ; 042C 3600     6D  
        INC     HL                      ; 042E 23       #   Go to next dest address
        DEC     B                       ; 042F 05       .   Decrement loop counter
        JR      NZ,Lb54                 ; 0430 20F4      .  Done?  Nope, keep looping

        LD      A,(PLAY_PER_COIN)       ; 0432 3A7A80   :/. Get plays per coin
        CP      $04                     ; 0435 FE04     .T  Free play?
        RET     NZ                      ; 0437 C0       .   No, return (CK_MACH_CONFIG)

; Save number of credits
        LD      (NUM_CREDITS),A         ; 0438 327280   2'. Write 4 to free play location
        RET                             ; 043B C9       .   Return (CK_MACH_CONFIG)


;-----------------------------------------------------------------------------
; Data area
; $043C - $0449
;
; The high score table is initialized with this data
; This is the character map for "Nichibutsu  "  
;-----------------------------------------------------------------------------

        .db     $C7, $FB				; Data marker start
HI_SCORE_INIT_DATA:
        .db     "01234567RR"			; Characters data for "Nichibutsu  "
        .db     $C7, $F3				; Data marker end



;=============================================================================
; Copies a block of data 
;
; Input:
; HL - source address
; DE - destination address
; BC - number of bytes to move
;
; Output:
; DE points one past end of block copy
; HL points one past end of block copy
;
; Destroys:
; A, HL, DE, BC, Flags
;=============================================================================
BLOCK_COPY:
        LD      A,(HL)                  ; 044A 7E       ~  Get data pointed to by HL
        LD      (DE),A                  ; 044B 12       .  Copy it to the location pointed to by DE
        INC     HL                      ; 044C 23       #  Increment HL (source)
        INC     DE                      ; 044D 13       .  Increment DE (dest)
        DEC     BC                      ; 044E 0B       .  Decrement loop counter
        LD      A,C                     ; 044F 79       y  Check BC
        OR      B                       ; 0450 B0       .  Is BC = 0?
        JR      NZ,BLOCK_COPY           ; 0451 20F7      . Nope, continue
        RET                             ; 0453 C9       .  End BLOCK_COPY
; End of BLOCK_COPY



;-----------------------------------------------------------------------------
; Continually adds 1 to the general purpose counter at $8122
; This would generate a pseudo-random number if this value is read during
; interrupts
;
; Destroys:
;    None
; 
; Note:
;	This is a forever loop
;
; This is also called from $02B7
; (Index 5 in the jump table - Address $0454). This is called on startup, 
; right after the high scores are displayed.
;-----------------------------------------------------------------------------
ISR_JUMP5:
        NOP                             ; 0454 00       .
        PUSH    AF                      ; 0455 F5       .   Save AF
        PUSH    HL                      ; 0456 E5       .   Save HL
        LD      HL,RANDOM_NUMBER        ; 0457 212281   !g. 
        LD      A,(HL)                  ; 045A 7E       ~   Get value in $8122
        ADD     A,$01                   ; 045B C601     ..  Increment value
        LD      (HL),A                  ; 045D 77       w   Store new value
        POP     HL                      ; 045E E1       .   Restore HL
        POP     AF                      ; 045F F1       .   Restore AF
        NOP                             ; 0460 00       .
        JR      ISR_JUMP5               ; 0461 18F1     ..  Keep looping forever


;=============================================================================
; Initializes color RAM by writing $0A to each location
;
; Writes 1024 bytes of $0A to $9C00 - $9FFF (Color RAM)
;=============================================================================
INIT_COLOR_RAM:  
        LD      HL,COLOR_RAM            ; 0463 21009C   !Dc Point to color RAM
        LD      BC,COLOR_RAM_SIZE       ; 0466 010004   .DT # bytes to write

Lb57:   LD      (HL),$0A                ; 0469 360A     6O  Write $0A to address
        INC     HL                      ; 046B 23       #   Go to next address
        DEC     BC                      ; 046C 0B       .   Decrement counter
        LD      A,B                     ; 046D 78       x   Is counter = 0?
        OR      C                       ; 046E B1       .
        JR      NZ,Lb57                 ; 046F 20F8      .  Nope, keep looping
        RET                             ; 0471 C9       .   End INIT_COLOR_RAM



;=============================================================================
; Name:		WRITE_CHARS
;
; Type:		Subroutine
;
; Description:	Screen character write subroutine.  DE is assumed to point to
;				the screen data that is to be written to the screen.
;
; Input:		DE points to the data set location
;
; Destroys:		None
;
; 
; The data set is organized as follows:
;
; DE + 0 - Color of characters (Note: if this is NOCHANGE_CHAR_COLOR ($FF),
;          the color ram is not written to)
; DE + 1 - Row
; DE + 2 - Column
; DE + 3 - 1st value to write
; DE + 4 - 2nd value to write
; ...
; DE + N - $FF (Termination value)
;=============================================================================
WRITE_CHARS:  
        NOP                             ; 0472 00       .
        PUSH    IY                      ; 0473 FDE5     ..  Save registers
        PUSH    IX                      ; 0475 DDE5     ..
        PUSH    AF                      ; 0477 F5       .
        PUSH    BC                      ; 0478 C5       .
        PUSH    DE                      ; 0479 D5       .
        PUSH    HL                      ; 047A E5       .

        PUSH    DE                      ; 047B D5       .
        POP     IX                      ; 047C DDE1     ..  IX = DE

; Set proper row
        LD      HL,SCREEN_RAM           ; 047E 210090   !D.  Point to screen ram
        LD      IY,COLOR_RAM            ; 0481 FD21009C .!D. Point to color ram
        LD      BC,$20                  ; 0485 012000   .dD  32 characters per row
        LD      A,(IX+$01)              ; 0488 DD7E01   .~.  Get row value
        OR      A                       ; 048B B7       .
        JR      Z,Lb58                  ; 048C 2806     (G   Zero? Go here

; Set proper row location
Lb59:   ADD     HL,BC                   ; 048E 09       .    Add each row value
        ADD     IY,BC                   ; 048F FD09     ..
        DEC     A                       ; 0491 3D       =
        JR      NZ,Lb59                 ; 0492 20FA      .   Not done? Keep looping

; Set proper column
Lb58:   LD      C,(IX+$02)              ; 0494 DD4E02   .NG  Get column value
        LD      B,$00                   ; 0497 0600     .D   Clear Most significant byte
        ADD     HL,BC                   ; 0499 09       .    Add to screen ram ptr
        ADD     IY,BC                   ; 049A FD09     ..   Add to color ram ptr

        LD      B,(IX+$00)              ; 049C DD4600   .FD  Get the color value
        INC     IX                      ; 049F DD23     .#   Go to next set of data
        INC     IX                      ; 04A1 DD23     .#
        INC     IX                      ; 04A3 DD23     .#

Lb62:   LD      A,(IX+$00)              ; 04A5 DD7E00   .~D  Read value to write
        CP      $FF                     ; 04A8 FEFF     ..   Termination value?
        JR      Z,Lb60                  ; 04AA 2810     (.   Yes, exit routine

        LD      (HL),A                  ; 04AC 77       w    Write value to screen ram
        LD      A,B                     ; 04AD 78       x    Get color
        CP      NOCHANGE_CHAR_COLOR     ; 04AE FEFF     ..   Do not change color?
        JR      Z,Lb61                  ; 04B0 2803     (S   Yes, skip color set

        LD      (IY+$00),B              ; 04B2 FD7000   .pD  Set color

Lb61:   INC     HL                      ; 04B5 23       #    Go to next screen ram location
        INC     IX                      ; 04B6 DD23     .#   Go to next input data set location
        INC     IY                      ; 04B8 FD23     .#   Go to next screen color location
        JR      Lb62                    ; 04BA 18E9     ..   Continue looping

Lb60:   POP     HL                      ; 04BC E1       .    Restore registers
        POP     DE                      ; 04BD D1       .
        POP     BC                      ; 04BE C1       .
        POP     AF                      ; 04BF F1       .
        POP     IX                      ; 04C0 DDE1     ..
        POP     IY                      ; 04C2 FDE1     ..
        RET                             ; 04C4 C9       .    End screen character write routine


;=============================================================================
; Writes a number value to the screen
;
; Destroys:
;	None
;
; Input:
;	DE points to the data set location
;
; The data set is organized as follows:
;
; DE + 0 - Color of digits (Note: if this is NOCHANGE_CHAR_COLOR ($FF), the color ram
;          is not written to)
; DE + 1 - Row
; DE + 2 - Column
; DE + 3, DE + 4 - Pointer to location of number to write
; DE + 5 - Number of digits in the number
;=============================================================================
WRITE_DIGITS:
        NOP                             ; 04C5 00       .
        PUSH    IY                      ; 04C6 FDE5     ..   Save registers used
        PUSH    IX                      ; 04C8 DDE5     ..
        PUSH    AF                      ; 04CA F5       .
        PUSH    BC                      ; 04CB C5       .
        PUSH    DE                      ; 04CC D5       .
        PUSH    HL                      ; 04CD E5       .

        PUSH    DE                      ; 04CE D5       .
        POP     IX                      ; 04CF DDE1     ..   IX = DE

        LD      HL,SCREEN_RAM           ; 04D1 210090   !D.  HL points to screen RAM
        LD      IY,COLOR_RAM            ; 04D4 FD21009C .!Dc IY points to color RAM
        LD      BC,$20                  ; 04D8 012000   .dD  32 characters per row
        LD      A,(IX+$01)              ; 04DB DD7E01   .~.  Get the row number
        OR      A                       ; 04DE B7       .
        JR      Z,Lb63                  ; 04DF 2806     (.

; Set proper row
Lb64:   ADD     HL,BC                   ; 04E1 09       .    Add characters per row to screen RAM ptr
        ADD     IY,BC                   ; 04E2 FD09     ..   Add characters per row to screen color ptr
        DEC     A                       ; 04E4 3D       =    Decrement row counter
        JR      NZ,Lb64                 ; 04E5 20FA      .   Not done?  Keep looping

; Set the proper column
Lb63:   LD      C,(IX+$02)              ; 04E7 DD4E02   .N. Get the column number
        LD      B,$00                   ; 04EA 0600     .D  Clear most significant byte
        ADD     HL,BC                   ; 04EC 09       .   Add column to screen RAM pointer
        ADD     IY,BC                   ; 04ED FD09     ..  Add column to screen color pointer

        LD      B,(IX+$00)              ; 04EF DD4600   .FD Get the color
        LD      C,(IX+$05)              ; 04F2 DD4E05   .N. Get number of digits
        LD      D,(IX+$04)              ; 04F5 DD5604   .V. DE points to where the value is located
        LD      E,(IX+$03)              ; 04F8 DD5E03   .^.

Lb68:   BIT     0,C                     ; 04FB CB41     .A  Is C even?
        JR      Z,Lb65                  ; 04FD 2807     (F  Yes, go to here

; Handle odd byte  (Least significant nibble)
        LD      A,(DE)                  ; 04FF 1A       .   Read byte from value pointer
        AND     $0F                     ; 0500 E60F     ..  Clear most significant nibble
        LD      (HL),A                  ; 0502 77       w   Write value to screen
        INC     DE                      ; 0503 13       .   Go to next byte
        JR      Lb66                    ; 0504 1808     .L  Continue

; Handle even byte (Most significant nibble)
Lb65:   LD      A,(DE)                  ; 0506 1A       .   Read byte from value pointer
        RRCA                            ; 0507 0F       .   Rotate right 4X
        RRCA                            ; 0508 0F       .
        RRCA                            ; 0509 0F       .
        RRCA                            ; 050A 0F       .
        AND     $0F                     ; 050B E60F     .N  Mask off most significant nibble
        LD      (HL),A                  ; 050D 77       w   Write value to screen

Lb66:   LD      A,B                     ; 050E 78       x   Get the color
        CP      NOCHANGE_CHAR_COLOR     ; 050F FEFF     ..  Do not change the color?
        JR      Z,Lb67                  ; 0511 2803     (.  Yes, skip color set

        LD      (IY+$00),B              ; 0513 FD7000   .pD Set the color

Lb67:   INC     IY                      ; 0516 FD23     .#  Increment color RAM pointer
        INC     HL                      ; 0518 23       #   Increment screen RAM pointer
        DEC     C                       ; 0519 0D       .   Decrement # digits counter
        JR      NZ,Lb68                 ; 051A 20DF      .  Not done?  Keep looping

        POP     HL                      ; 051C E1       .   Restore registers used
        POP     DE                      ; 051D D1       .
        POP     BC                      ; 051E C1       .
        POP     AF                      ; 051F F1       .
        POP     IX                      ; 0520 DDE1     ..
        POP     IY                      ; 0522 FDE1     ..
        RET                             ; 0524 C9       .


;=============================================================================
; Initialize the machine's Video
; Subroutine
;-----------------------------------------------------------------------------
; Writes $52 to the screen RAM ($9000 - $93FF)
;=============================================================================
INIT_VIDEO:
        NOP                             ; 0525 00       .
        LD      HL,SCREEN_RAM           ; 0526 210090   !D.  Start of screen RAM
        LD      BC,SCREEN_RAM_SIZE      ; 0529 010004   .D.  Write 1024 bytes

Lb69:   LD      (HL),$52                ; 052C 3652     6.   Write $52 to each location
        INC     HL                      ; 052E 23       #    Go to next location
        DEC     BC                      ; 052F 0B       .    Decrement counter
        LD      A,B                     ; 0530 78       x    Is counter = 0?
        OR      C                       ; 0531 B1       .
        JR      NZ,Lb69                 ; 0532 20F8      .   Nope, continue looping

;------------------------------------------------------
; Initializes column smooth scrolling position
; $9800 - $981F Initialized to $00  (32 columns)
;
;
; Unknown
; $9820 - $987F Initialized to $00
;
;
; Initialize sprite controls (8 groups of 4 bytes)
; $9880 - $989F Initialized to $00
; Byte 0
;	Bits 5 - 0  Sprite Code
;	Bit 6       X invert
;	Bit 7  	    Y invert
;
; Byte 1
;	Bits 3 - 0	Color (0-15 color palette)
;	Bit 4		0 - Charset1, 1 - Charset2
;
; Byte 2: Y position
; Byte 3: X position
;------------------------------------------------------
        NOP                             ; 0534 00       .
        LD      HL,COLUMN_SCROLL        ; 0535 210098   !D.  Start at the column smooth scrolling position
        LD      BC,$A0                  ; 0538 01A000   ._D  Write to 160 locations

Lb70:   LD      (HL),$00                ; 053B 3600     6D   Write $00 to each location
        INC     HL                      ; 053D 23       #    Go to next location
        DEC     BC                      ; 053E 0B       .    Decrement counter
        LD      A,B                     ; 053F 78       x    Is counter = 0?
        OR      C                       ; 0540 B1       .
        JR      NZ,Lb70                 ; 0541 20F8      .   Nope, continue looping

        CALL    INIT_BIG_SPRITE_RAM     ; 0543 CD4705   .BU  Initialize big sprite RAM
        RET                             ; 0546 C9       .    End INIT_VIDEO


;=============================================================================
; Initialize big sprite RAM (256 bytes) to $00
; Subroutine
;=============================================================================
INIT_BIG_SPRITE_RAM:
        NOP                             ; 0547 00       .
        LD      HL,BIG_SPRITE_RAM       ; 0548 210088   !D.  Point HL to start of Big Sprite RAM
        LD      BC,BIG_SPRITE_RAM_SIZE  ; 054B 010001   .D.  256 locations

Lb72:   LD      (HL),$00                ; 054E 3600     6D  Write $00 to each location
        INC     HL                      ; 0550 23       #   Go to next location
        DEC     BC                      ; 0551 0B       .   Decrement counter
        LD      A,B                     ; 0552 78       x   Is counter = 0?
        OR      C                       ; 0553 B1       .
        JR      NZ,Lb72                 ; 0554 20F8      .  Nope, keep looping

;------------------------------------------------------------------------------
; Initialize Big sprite attributes
;
; Initialize $98DC - $98DF to $00
;
; $98DC
;	Bit 0:	0 - More priority over other spries, 1 - less priority
;
; $98DD
;	Bit 0-2: Big sprite colour.
;	Bit 3  ??
;	Bit   4: x invert.
;	Bit   5: y invert.
;
; $98DE - Y position
; $98DF - X position
;------------------------------------------------------------------------------
        LD      HL,BIG_SPRITE_CTRL      ; 0556 21DC98   !..  Big sprite attribute location
        LD      B,$04                   ; 0559 0604     .T   4 big sprite attribute bytes

Lb73:   LD      (HL),$00                ; 055B 3600     6D   Initialize to $00
        INC     HL                      ; 055D 23       #    Go to next location
        DEC     B                       ; 055E 05       .    Decrement counter
        JR      NZ,Lb73                 ; 055F 20FA      .   Counter 0? Nope, keep looping
        RET                             ; 0561 C9       .    End INIT_BIG_SPRITE_RAM




;=============================================================================
; Clears memory $8130 - $82F0
;
; Clears all game state variables
;=============================================================================
Lb96:   NOP                             ; 0562 00       .
        LD      HL,$8130                ; 0563 213081   !1. Start address
        LD      BC,$1C0                 ; 0566 01C001   ... 448 bytes

Lb74:   LD      (HL),$00                ; 0569 3600     6D  Clear location
        INC     HL                      ; 056B 23       #   Go to next location
        DEC     BC                      ; 056C 0B       .   Decrement counter
        LD      A,B                     ; 056D 78       x
        OR      C                       ; 056E B1       .
        JR      NZ,Lb74                 ; 056F 20F8      .  Done? Nope, keep looping
        RET                             ; 0571 C9       .   Finished


;-----------------------------------------------------------------------------
; Called from $02B7 on startup....
; (Index 4 in the jump table, called once on startup)
;
; This section of code checks the number of credits.  If != 0, then the
; state is changed to "game in progress".
;-----------------------------------------------------------------------------
ISR_JUMP4:
        NOP                             ; 0572 00       .
        LD      A,$01                   ; 0573 3E01     >.
        LD      (KEEP_SAME_ISR_FLAG),A  ; 0575 324480   2@. Keep processing the same ISR table location
        LD      A,(PLAYER_DIED_FLAG)    ; 0578 3A7380   :.. Get the player died flag
        OR      A                       ; 057B B7       .   Has player died?
        JP      NZ,ISR_JUMP4_DEAD_PLAYER ; 057C C25F06   ... Yes, go here

;----------------------------------------------------------------------
; Determines if a game is "in progress" by checking number of credits

        LD      B,$00                   ; 057F 0600     .D  Clear B
        LD      A,(NUM_CREDITS)         ; 0581 3A7280   :#. Read number of credits
        OR      A                       ; 0584 B7       .    
        JR      Z,Lb76                  ; 0585 2801     (.  Zero credits?  No game in progress

        INC     B                       ; 0587 04       .   B = 1 (Game in progress)

Lb76:   LD      A,B                     ; 0588 78       x   Get Value of B
        LD      (GAME_IN_PROGRESS),A    ; 0589 327580   25. Save the game in progress flag
        CALL    Lb77                    ; 058C CDD005   ...	Check credits and start a game

        LD      A,$01                   ; 058F 3E01     >.
        LD      ($8074),A               ; 0591 327480   2!.
        LD      A,$01                   ; 0594 3E01     >.
        LD      (KEEP_SAME_ISR_FLAG),A  ; 0596 324480   2..  Keep processing the same ISR table location
        JP      INIT_ISR_FLAG_TABLE     ; 0599 C39400   ..D  Continue here and initialize the ISR flag table


;=============================================================================
; Compares screen RAM ($9362 - $936D) to the following data
;
; $17 $12 $11 $18 $17 $52 $0B $1E $1C $1C $0A $17
; N   I   H   O   N       B   U   S   S   A   N
; (That data is located at $05C2, but $10 is added to each value)
;
; This will add 5 credits if the values are not equal.  This may be some sort
; of software copy protection -- if this value was not previously written to
; screen RAM, then 5 credits would be added, and the counterfeit software
; would not make any $$?
;=============================================================================
CHECK_NIHON_BUSSAN:
        NOP                             ; 059C 00       .
        LD      HL,ISR_FLAG_TABLE+5     ; 059D 216280   !c.
        LD      DE,$1300                ; 05A0 110013   .DR
        ADD     HL,DE                   ; 05A3 19       .    HL = ISR_FLAG_TABLE+5 + $1300 = $9362 (Screen RAM)
        LD      DE,$5C2                 ; 05A4 11C205   ...  DE = $05C2 (ROM data just below...)
        LD      B,$0C                   ; 05A7 060C     .\   Loop counter (12 bytes)

Lb80:   LD      C,(HL)                  ; 05A9 4E       N    Read screen RAM
        LD      A,(DE)                  ; 05AA 1A       .    Read ROM address
        ADD     A,$10                   ; 05AB C610     ..   Add $10
        CP      C                       ; 05AD B9       .    Are values equal?
        JR      NZ,Lb79                 ; 05AE 2006      G   Nope, add credits

        INC     HL                      ; 05B0 23       #    Values are equal, go to next screen address
        INC     DE                      ; 05B1 13       .    Go to next ROM address
        DEC     B                       ; 05B2 05       .    Decrement loop counter
        JR      NZ,Lb80                 ; 05B3 20F4      .   Not done? Continue looping
        RET                             ; 05B5 C9       .    Done CHECK_NIHON_BUSSAN

; Add 5 credits
Lb79:   LD      A,(NUM_CREDITS)         ; 05B6 3A7280   :'.  Get number of credits
        ADD     A,$05                   ; 05B9 C605     ..
        DAA                             ; 05BB 27       '    Decimal adjust value
        LD      (NUM_CREDITS),A         ; 05BC 327280   2'.  Save number of credits
        RET                             ; 05BF C9       .    Done CHECK_NIHON_BUSSAN



;-------------------------------------------------------------------------------
; Data for "NIHON BUSSAN"
;
; Range: $05C0 - $05CF
;-------------------------------------------------------------------------------

        .db     $C7, $FB								; Data marker start

; The following data has $10 added to each byte.
; The resulting character text is "NIHON BUSSAN"
		.db     $07, $02, $01, $08, $07, $42, $FB, $0E
		.db     $0C, $0C, $FA, $07

		.db     $C7, $F3								; Data marker end

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------


;=============================================================================
;=============================================================================
Lb77:   NOP                             ; 05D0 00       .
        LD      A,$01                   ; 05D1 3E01     >.
        LD      (NUM_PLAYERS),A         ; 05D3 328080   2..  Set to 2 player game
        CALL    INIT_VIDEO              ; 05D6 CD2505   .u.  Initialize the video

        LD      A,(GAME_IN_PROGRESS)    ; 05D9 3A7580   :5.  Is there a game in progress?
        OR      A                       ; 05DC B7       .
        JR      NZ,Lb82                 ; 05DD 2019      I   Yes, go here

; No game in progress
        CALL    DISPLAY_TITLE_SCREEN    ; 05DF CDF407   ...  Display the title screen

        CALL    CHECK_NIHON_BUSSAN      ; 05E2 CD9C05   .c.  Compare screen to NIHON BUSSAN

        CALL    SHOW_HI_SCORE_TABLE     ; 05E5 CD370E   .&O  Show high score table

        LD      A,$FF                   ; 05E8 3EFF     >.
        CALL    DELAY                   ; 05EA CDB802   ..G  Delay

        LD      A,$FF                   ; 05ED 3EFF     >.
        CALL    DELAY                   ; 05EF CDB802   ...  Delay

        XOR     A                       ; 05F2 AF       .
        LD      (NUM_PLAYERS),A         ; 05F3 328080   2..  Set to 1 player game
        JR      GAME_START              ; 05F6 1851     .T

; A game is in progress
Lb82:   CALL    SHOW_HI_SCORE_TABLE     ; 05F8 CD370E   .w. Show high score table

; See if we have 1 credit
Lb95:   LD      A,(NUM_CREDITS)         ; 05FB 3A7280   :#. Get number of credits
        CP      $01                     ; 05FE FE01     ..  Do we have 1 credit?
        JR      NZ,Lb88                 ; 0600 2008      L  No, go here

; We have 1 credit
        CALL    SHOW_P1_BUTTON          ; 0602 CD300A   . O Show player 1 button press only
        CALL    SHOW_CREDITS            ; 0605 CDF809   ... Show credits
        JR      Lb91                    ; 0608 1806     .G

; Something other than one credit
Lb88:   CALL    SHOW_P1_P2_BUTTON       ; 060A CD6B0A   .~O Show player 1 or player 2 press
        CALL    SHOW_CREDITS            ; 060D CDF809   ... Show credits

Lb91:   NOP                             ; 0610 00       .
        LD      A,(MACH_SW_RD)          ; 0611 3A00B8   :D. Read the machine switches
        AND     $08                     ; 0614 E608     .L  Isolate player 2 start bit
        CP      $08                     ; 0616 FE08     .L  Player 2 start pressed?
        JR      Z,Lb93                  ; 0618 280B     ([  Yes, go here

        LD      A,(MACH_SW_RD)          ; 061A 3A00B8   :D. Read the machine switches
        AND     $04                     ; 061D E604     .T  Isolate player 1 start bit
        CP      $04                     ; 061F FE04     .T  Player 1 start pressed?
        JR      Z,Lb94                  ; 0621 2819     (I  Yes, go here

        JR      Lb95                    ; 0623 18D6     ..  Keep looping

;-------------------------------
; Player 2 start button pressed

; See if we have at least 2 credit to start a game
Lb93:   LD      A,(NUM_CREDITS)         ; 0625 3A7280   :#. Get number of credits
        CP      $02                     ; 0628 FE02     ..  Less than 2 credits?
        JR      C,Lb95                  ; 062A 38CF     8.  Yes, go here (not enough credits)

; >= 2 credits...
        LD      A,$01                   ; 062C 3E01     >.  
        LD      (NUM_PLAYERS),A         ; 062E 328080   2.. Set flag for two players
        LD      A,(NUM_CREDITS)         ; 0631 3A7280   :#. Read number of credits

; This subtracts 2 from number of credits.
;
; Example: A = 2.  Add $98 to that gives $9A.
; When you decimal adjust, the A (10 is set to 0,
; carries 1 and adds to the 9, which gives 0 with a carry.
; The final result is $00
        ADD     A,$98                   ; 0634 C698     ..
        DAA                             ; 0636 27       '
        LD      (NUM_CREDITS),A         ; 0637 327280   2#. Store number of credits
        JR      GAME_START              ; 063A 180D     .]  Continue for 2 player game

;-------------------------------
; Player 1 start button pressed
Lb94:   XOR     A                       ; 063C AF       .   
        LD      (NUM_PLAYERS),A         ; 063D 328080   2.. Clear flag for one player
        LD      A,(NUM_CREDITS)         ; 0640 3A7280   :'. Read number of credits

; This subtracts 1 from number of credits
        ADD     A,$99                   ; 0643 C699     ..
        DAA                             ; 0645 27       '
        LD      (NUM_CREDITS),A          ; 0646 327280   2'. Save number of credits


;---------------------
; Game Start!
;---------------------
GAME_START:
        CALL    Lb96                    ; 0649 CD6205   .cU
        CALL    Lb97                    ; 064C CD3607   ..F
        XOR     A                       ; 064F AF       .   Player 1
        CALL    SAVE_PLAYER_STATE       ; 0650 CDF706   ... Save player state

        LD      A,$01                   ; 0653 3E01     >.  Player 2
        CALL    SAVE_PLAYER_STATE       ; 0655 CDF706   ..G Save player state

        LD      A,(P2_NUM_LIVES)        ; 0658 3AFC80   :.. Save player 2 # lives
        LD      (OTHER_PLAYER_LIVES),A  ; 065B 328280   2..
        RET                             ; 065E C9       .


; The player has died
ISR_JUMP4_DEAD_PLAYER:
        NOP                             ; 065F 00       .
        XOR     A                       ; 0660 AF       .   
        LD      (PLAYER_DIED_FLAG),A    ; 0661 327380   2v. Clear player died flag
        CALL    INIT_VIDEO              ; 0664 CD2505   .u. Initialize the video

; Subtract 1 life
        LD      A,(CUR_NUM_LIVES)       ; 0667 3AD880   :.. Read number of lives
        DEC     A                       ; 066A 3D       =   Subtract 1
        LD      (CUR_NUM_LIVES),A       ; 066B 32D880   2.. Save the value

        LD      A,(CURRENT_PLAYER)      ; 066E 3A8180   :.. Get current player
        CALL    SAVE_PLAYER_STATE       ; 0671 CDF706   ..G Save player state

        LD      A,(CUR_NUM_LIVES)       ; 0674 3AD880   :.. Read number of lives
        OR      A                       ; 0677 B7       .   Is value 0?
        JR      Z,Lb99                  ; 0678 2843     (V  Yes, end game

        LD      A,(NUM_PLAYERS)         ; 067A 3A8080   :.. Get number of players flag
        OR      A                       ; 067D B7       .
        JR      Z,Lb100                 ; 067E 282C     (=  1 player game - go here

; 2 player game
Lb197:  LD      A,(OTHER_PLAYER_LIVES)  ; 0680 3A8280   :}. Get other player's # lives
        OR      A                       ; 0683 B7       .   Are they zero?
        JR      Z,Lb100                 ; 0684 2826     (g  Yes, go here

; Toggle current player
TOGGLE_PLAYER:  
        LD      A,(CURRENT_PLAYER)      ; 0686 3A8180   :.. Get current player
        INC     A                       ; 0689 3C       <   Toggle current player
        AND     $01                     ; 068A E601     ..
        LD      (CURRENT_PLAYER),A      ; 068C 328180   2.. Save result

        LD      A,(MACH_VER)            ; 068F 3A7C80   :). Get the machine version
        OR      A                       ; 0692 B7       .   Check the value
        JR      NZ,Lb100                ; 0693 2017      .  If upright (1), go here

        LD      A,(CURRENT_PLAYER)      ; 0695 3A8180   :.. Check current player
        OR      A                       ; 0698 B7       .
        JR      Z,Lb101                 ; 0699 280A     (O  Player 1, go here

; Player 2 is current player
; Invert the monitor
        LD      A,$01                   ; 069B 3E01     >.  A = 1
        LD      (HINV_WR),A             ; 069D 3201A0   2._ Invert the monitor horizontal
        LD      (VINV_WR),A             ; 06A0 3202A0   2.. Invert the monitor vertical
        JR      Lb100                   ; 06A3 1807     .F

; Player 1 is current player
; Set monitor to regular (no inversion)
Lb101:  XOR     A                       ; 06A5 AF       .   Clear A
        LD      (HINV_WR),A             ; 06A6 3201A0   2.. Normal horizontal
        LD      (VINV_WR),A             ; 06A9 3202A0   2G_ Normal vertical

; 1 player game - Get current player sate
Lb100:  CALL    Lb96                    ; 06AC CD6205   .3.
        LD      A,(CURRENT_PLAYER)      ; 06AF 3A8180   :..  Get current player
        CALL    GET_PLAYER_STATE        ; 06B2 CD0D07   .]F

        LD      A,$01                   ; 06B5 3E01     >.
        LD      (KEEP_SAME_ISR_FLAG),A  ; 06B7 324480   2@.  Keep processing the same ISR table location

        JP      INIT_ISR_FLAG_TABLE     ; 06BA C39400   .kD  Continue here and initialize the ISR flag table


; No more lives
Lb99:   LD      A,(GAME_IN_PROGRESS)    ; 06BD 3A7580   :5.  Is a game in progress?
        OR      A                       ; 06C0 B7       .
        JP      Z,STARTUP2              ; 06C1 CA7200   .#D  Nope, go here

; A game is in progress
        CALL    SHOW_PLAYER_OVER        ; 06C4 CDA90A   ..O  Show the player is done
        CALL    CHECK_HIGH_SCORES       ; 06C7 CD180B   ..[  Check the current score agains the high scores
        LD      A,(NUM_PLAYERS)         ; 06CA 3A8080   :..  Get number of players flag
        OR      A                       ; 06CD B7       .
        JR      Z,Lb105                 ; 06CE 2806     (G   1 player - go here

; 2 players
        LD      A,(OTHER_PLAYER_LIVES)  ; 06D0 3A8280   :}.  Get other player's # lives
        OR      A                       ; 06D3 B7       .    Are they zero?
        JR      NZ,TOGGLE_PLAYER        ; 06D4 20B0      .   Nope, go here (toggle player)

; 1 player Initialize
Lb105:  CALL    SHOW_GAME_OVER          ; 06D6 CDF20A   ..O Show game over on screen
        XOR     A                       ; 06D9 AF       .   Clear A
        LD      (PLAYER_DIED_FLAG),A    ; 06DA 327380   2.. Clear player died flag
        LD      ($8074),A               ; 06DD 327480   2!.

        LD      (GAME_IN_PROGRESS),A    ; 06E0 327580   2%. No game in progress
        LD      (CURRENT_PLAYER),A      ; 06E3 328180   2.. Set current player to player 1
        LD      (NUM_PLAYERS),A         ; 06E6 328080   2.. 1 player
        LD      (HINV_WR),A             ; 06E9 3201A0   2._ Normal horizontal
        LD      (VINV_WR),A             ; 06EC 3202A0   2.. Normal vertical
        LD      A,$01                   ; 06EF 3E01     >.
        LD      (KEEP_SAME_ISR_FLAG),A  ; 06F1 324480   2@. Keep processing the same ISR table location
        JP      STARTUP2                ; 06F4 C37200   .'D


;=============================================================================
; Saves the current player state
;
; Input:
;	A contains the player flag (0 - Player 1, != 0 - Player 2)
;=============================================================================
SAVE_PLAYER_STATE:
        NOP                             ; 06F7 00       .
        OR      A                       ; 06F8 B7       .   Check player number
        JR      NZ,Lb108                ; 06F9 2005      .  Player 2, go here

; Player 1 selected
        LD      DE,P1_DATA              ; 06FB 11EA80   ... Dest. address - player 1 data
        JR      Lb109                   ; 06FE 1803     .S

; Player 2 selected
Lb108:  LD      DE,P2_DATA              ; 0700 11FC80   ... Dest. address - player 2 data

Lb109:  LD      HL,CURRENT_DATA         ; 0703 21D880   !.. Source address is current working data
        LD      BC,$12                  ; 0706 011200   .FD Copy 18 bytes of data
        CALL    BLOCK_COPY              ; 0709 CD4A04   .K. Block copy routine
        RET                             ; 070C C9       .   End SAVE_PLAYER_STATE


;=============================================================================
; Gets the player state
;
; Input:
;	A contains the current player flag (0 - Player 1, != 0 - Player 2)
;=============================================================================
GET_PLAYER_STATE:
        NOP                             ; 070D 00       .
        OR      A                       ; 070E B7       .   Check player number
        JR      NZ,Lb110                ; 070F 200B      .  Player2? Yes, go here

; Player 1 selected
        LD      A,(P2_NUM_LIVES)        ; 0711 3AFC80   :.. Save player 2 # lives
        LD      (OTHER_PLAYER_LIVES),A  ; 0714 328280   2}.
        LD      HL,P1_DATA              ; 0717 21EA80   !.. Source - Player 1 info
        JR      Lb111                   ; 071A 1809     ..

; Player 2 selected
Lb110:  LD      A,(P1_NUM_LIVES)        ; 071C 3AEA80   :.. Save player 1 # lives
        LD      (OTHER_PLAYER_LIVES),A  ; 071F 328280   2..
        LD      HL,P2_DATA              ; 0722 21FC80   !.. Source - Player 2 info

Lb111:  LD      DE,CURRENT_DATA         ; 0725 11D880   ... Destination - Current working data
        LD      BC,$12                  ; 0728 011200   .FD Copy 18 bytes of data
        CALL    BLOCK_COPY              ; 072B CD4A04   .K. Block copy routine

        XOR     A                       ; 072E AF       .	Clear ISR decrement counters
        LD      (ISR_JUMP3_CNTR1),A     ; 072F 322081   2d.
        LD      (ISR_JUMP3_CNTR2),A     ; 0732 322181   20.
        RET                             ; 0735 C9       .   End GET_PLAYER_STATE


;=============================================================================
;=============================================================================
Lb97:   NOP                             ; 0736 00       .
        LD      A,(MAX_LIVES)           ; 0737 3A7E80   :.. Read max number of lives (at game start)
        LD      (CUR_NUM_LIVES),A       ; 073A 32D880   2.. Save here

; Clear score
        XOR     A                       ; 073D AF       .   Clear A
        LD      (CUR_SCORE),A               ; 073E 32D980   2.. Clear Score
        LD      (CUR_SCORE+1),A             ; 0741 32DA80   2..
        LD      (CUR_SCORE+2),A             ; 0744 32DB80   2..

        LD      A,$00                   ; 0747 3E00     >D  Clear A
        LD      (FLOOR_GROUP_IDX),A     ; 0749 32DC80   2.. Start at the beginning floor group of the building
        LD      (FLOOR_IDX),A           ; 074C 32DD80   2.. Start at the 1st floor in the floor group

        XOR     A                       ; 074F AF       .   Clear A
        LD      (XTRA_LIFE_FLAG),A      ; 0750 32DE80   2.. No extra life yet
        LD      (ISR_JUMP3_CNTR1),A     ; 0753 322081   2d.	Clear ISR decrement counters
        LD      (ISR_JUMP3_CNTR2),A     ; 0756 322181   20.
        LD      (BUILDING_NUMBER),A     ; 0759 32DF80   2.. Building number 0 (1st building)
        LD      (CUR_FLOOR_NUM),A       ; 075C 32E880   2.. Clear the current floor number
        LD      (CUR_FLOOR_GROUP),A     ; 075F 32E980   2.. Clear the current floor group
        RET                             ; 0762 C9       .


;=============================================================================
; Name:		UPDATE_GAME_SCORES
;
; Type:		Subroutine
;
; Description:	Updates the game scores.  The updated items are:
;
; High score text
; High score value
;
; Player 1 score text
; Player 1 score value
;
; Player 2 score text   (Note: This is blanked if a one player game)
; Player 2 score value  (Note: This is blanked if a one player game)
;=============================================================================

UPDATE_GAME_SCORES:  
        NOP                             ; 0763 00       .
        LD      DE,P1_SCORE_TEXT        ; 0764 11CD07   ..F Point to player 1 score text (SCORE1)
        CALL    WRITE_CHARS             ; 0767 CD7204   .#. Write characters to screen

        LD      DE,HS_HIGH_TEXT         ; 076A 11D707   ..F Point to high score text (HIGH)
        CALL    WRITE_CHARS             ; 076D CD7204   .#. Write characters to screen

        LD      DE,HS_SCORE_TEXT        ; 0770 11DF07   ..F Point to high score text (SCORE)
        CALL    WRITE_CHARS             ; 0773 CD7204   .#. Write characters to screen

        LD      DE,P2_SCORE_TEXT        ; 0776 11E807   ..F Point to player 2 score text (SCORE2)
        CALL    WRITE_CHARS             ; 0779 CD7204   .#. Write characters to screen

; Show Player 1 score
        LD      DE,P1_SCORE_VAL         ; 077C 11A707   ..F Point to player 1 score value
        CALL    WRITE_DIGITS            ; 077F CDC504   .:. Write digits to the screen

; Show high score
        LD      DE,HS_SCORE_VAL         ; 0782 11AD07   ..F Point to high score value
        CALL    WRITE_DIGITS            ; 0785 CDC504   .:. Write digits to the screen

; Show player 2 score
        LD      DE,P2_SCORE_VAL         ; 0788 11B307   ..F Point to player 2 score value
        CALL    WRITE_DIGITS            ; 078B CDC504   .:. Write digits to the screen

        LD      A,(NUM_PLAYERS)         ; 078E 3A8080   :.. Get number of players flag
        OR      A                       ; 0791 B7       .
        RET     NZ                      ; 0792 C0       .   Return if a two player

; 1 player
        LD      A,(GAME_IN_PROGRESS)    ; 0793 3A7580   :5. Is a game in progress?
        OR      A                       ; 0796 B7       .
        RET     Z                       ; 0797 C8       .   Nope, end UPDATE_GAME_SCORES

; Game in progress, only 1 player
; Blank player 2 score text and value
        LD      DE,BLANK_P2_SCORE_TXT   ; 0798 11B907   ..F Point to blanking P2 score text
        CALL    WRITE_CHARS             ; 079B CD7204   .#. Write characters to screen

        LD      DE,BLANK_P2_SCORE_VAL   ; 079E 11C307   ..F Point to blanking P2 score value
        CALL    WRITE_CHARS             ; 07A1 CD7204   .#. Write characters to screen 
        RET                             ; 07A4 C9       .   End UPDATE_GAME_SCORES



;-------------------------------------------------------------------------------
; Data Start
; Range: $07A5 - $07F3
;-------------------------------------------------------------------------------

        .db     $C7, $FB                ; Start data marker

; Player 1 score value ($07A7)
P1_SCORE_VAL:
		.db     NOCHANGE_CHAR_COLOR					; Do not change color
		.db     $09									; Row 9
		.db     $02									; Column 2
		.db     $EB, $80							; Value Address: $80EB
		.db     $06									; 6 digits

; High score value ($07AD)
HS_SCORE_VAL:
        .db     NOCHANGE_CHAR_COLOR					; Do not change color
		.db     $05									; Row 5
		.db     $02									; Column 2
		.db     $83, $80							; Value address: $8083
		.db     $06									; 6 digits

; Player 2 score value ($07B3)
P2_SCORE_VAL:
		.db     NOCHANGE_CHAR_COLOR					; Do not change color
		.db     $0D									; Row 13
		.db     $02									; Column 2
		.db     $FD, $80							; Value address: $80FD
		.db     $06                                          ; 6 digits

; Blank player 2 score text ($07B9)
BLANK_P2_SCORE_TXT:
		.db     NOCHANGE_CHAR_COLOR					; Do not change color
		.db     $0C									; Row 12
		.db     $02									; Column 2
		.db     SP_EN, SP_EN, SP_EN, SP_EN, SP_EN, SP_EN     ; "      "
		.db     $FF									; Terminator


; Blank player 2 score value ($07C3)
BLANK_P2_SCORE_VAL:
		.db     NOCHANGE_CHAR_COLOR					; Do not change color
		.db     $0D									; Row 13
        .db     $02									; Column 2
		.db     SP_EN, SP_EN, SP_EN, SP_EN, SP_EN, SP_EN     ; "      "
		.db     $FF									; Terminator

; Player 1 score text ($07CD)
P1_SCORE_TEXT:
        .db     NOCHANGE_CHAR_COLOR					; Do not change color
		.db     $08									; Row 8
		.db     $02									; Column 2
		.db     S_EN, C_EN, O_EN, R_EN, E_EN, DIG1_EN        ; "SCORE1"
		.db     $FF									; Terminator

; High (of high score) text ($07D7)
HS_HIGH_TEXT:
		.db     NOCHANGE_CHAR_COLOR					; Do not change color
		.db     $03									; Row 3
		.db     $02									; Column 2
		.db     H_EN, I_EN, G_EN, H_EN				; "HIGH"
		.db     $FF									; Terminator

; SCORE (of high score) text ($07DF)
HS_SCORE_TEXT:
		.db     NOCHANGE_CHAR_COLOR					; Do not change color
		.db     $04									; Row 4
		.db     $02									; Column 2
		.db     S_EN, C_EN, O_EN, R_EN, E_EN		; "SCORE" 
		.db     $FF									; Terminator

; Player 2 score text ($07E8)
P2_SCORE_TEXT:
		.db     NOCHANGE_CHAR_COLOR					; Do not change color
		.db     $0C									; Row 12
		.db     $02									; Column 2
		.db     S_EN, C_EN, O_EN, R_EN, E_EN, DIG2_EN	; "SCORE2"
		.db     $FF									; Terminator

		.db     $C7, $F3                ; End data marker

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------


;=============================================================================
; Display the title screen
;
;=============================================================================
DISPLAY_TITLE_SCREEN:   
        NOP                             ; 07F4 00       .
        CALL    INIT_COLOR_RAM          ; 07F5 CD6304   .6.  Initialize color RAM
        LD      HL,COLUMN_SCROLL        ; 07F8 210098   !D.  Column smooth scroll position
        LD      B,$20                   ; 07FB 0620     .d   32 columns

; Center each smooth scroll column position
Lb119:  LD      (HL),$80                ; 07FD 3680     6.   Write $80 to each column
        INC     HL                      ; 07FF 23       #    Go to next position
        DEC     B                       ; 0800 05       .    Decrement counter
        JR      NZ,Lb119                ; 0801 20FA      .   Counter = 0? Nope, keep looping
        JP      DISPLAY_TITLE_SCREEN1   ; 0803 C30010   .D.

; JP DISPLAY_TITLE_SCREEN1 returns back to DISPLAY_TITLE_SCREEN2.
; It points IX to the startup text pointer table
; It sets the smooth scroll position to $80 (middle)
;
;
; There is a table of 8 pointers.  Each pointer points to some character data
; for the startup screen.
;
; IX points to the text pointer table
; B is the index for these text pointers (8 - 0)
; C contains the number of rows to scroll
;

        NOP                             ; 0806 00       .
DISPLAY_TITLE_SCREEN2:
        LD      B,$08                   ; 0807 0608     .L  8 pointers in the text table

Lb127:  LD      A,B                     ; 0809 78       x
        CP      $01                     ; 080A FE01     ..
        JR      Z,Lb121                 ; 080C 281A     (N  Is pointer index = 1?  Yes, do not copy any more data

        CP      $07                     ; 080E FE07     ..  Is pointer index = 7?
        JR      NZ,Lb122                ; 0810 200D      ]  Nope, go here

; Pointer index is 7 -- write out two lines (the double high text)
        LD      E,(IX+$00)              ; 0812 DD5E00   .^D DE points to character data
        LD      D,(IX+$01)              ; 0815 DD5601   .V.
        CALL    WRITE_CHARS             ; 0818 CD7204   .'T Write characters to screen

        INC     IX                      ; 081B DD23     .#  Go to next pointer
        INC     IX                      ; 081D DD23     .#

Lb122:  LD      E,(IX+$00)              ; 081F DD5E00   .^D DE points to character data
        LD      D,(IX+$01)              ; 0822 DD5601   .V.
        CALL    WRITE_CHARS             ; 0825 CD7204   .#. Write characters to screen

Lb121:  LD      C,$10                   ; 0828 0E10     ..  16 rows to scroll

Lb126:  JP      DISPLAY_TITLE_SCREEN3   ; 082A C31010   ... This updates the scroll position


;----------------------------------------------------------------------
; JP to DISPLAY_TITLE_SCREEN3 returns back to DISPLAY_TITLE_SCREEN4.
; A contains the scroll position
; HL points to the start of the column smooth scroll position address
;----------------------------------------------------------------------
DISPLAY_TITLE_SCREEN4:
        LD      D,$20                   ; 082D 1620     .d  32 characters in the line

; Write new scroll position to color RAM
Lb124:  LD      (HL),A                  ; 082F 77       w   Write scroll pos. to color RAM
        INC     HL                      ; 0830 23       #   Go to next color RAM pos.
        DEC     D                       ; 0831 15       .   Decrement the counter
        JR      NZ,Lb124                ; 0832 20FB      .  Not done, keep looping

; Handle moving the "Crazy Climber" big sprite
        CALL    TITLE_HANDLE_BIGSPRITE  ; 0834 CD4809   ...

        LD      A,$08                   ; 0837 3E08     >L
        CALL    DELAY                   ; 0839 CDB802   ... Delay

        DEC     C                       ; 083C 0D       .   Decrement row counter
        JR      NZ,Lb126                ; 083D 20EB      .  Not done? Keep looping

        INC     IX                      ; 083F DD23     .#  Go to next text pointer
        INC     IX                      ; 0841 DD23     .#
        DEC     B                       ; 0843 05       .   Decrement pointer index
        JR      NZ,Lb127                ; 0844 20C3      .  Not done?  Keep looping

        LD      A,$FF                   ; 0846 3EFF     >.
        CALL    DELAY                   ; 0848 CDB802   ..G Delay

        LD      A,$FF                   ; 084B 3EFF     >.
        CALL    DELAY                   ; 084D CDB802   ... Delay

        LD      A,$FF                   ; 0850 3EFF     >.
        CALL    DELAY                   ; 0852 CDB802   ..G Delay

        RET                             ; 0855 C9       .   Finished with title screen


;-------------------------------------------------------------------------------
; Data for Title screen text
; Range: $0856 - $0947
;-------------------------------------------------------------------------------

        .db     $C7, $FB									; Start of data block

; Table of pointers to startup screen text ($0858)
STARTUP_TXT_PTR_TBL:
        .db     $68, $08									; $0868
		.db     $7C, $08									; $087C
		.db     $99, $08									; $0899
		.db     $B6, $08									; $08B6
		.db     $CE, $08									; $08CE
		.db     $EE, $08									; $08EE
		.db     $0F, $09									; $090F
		.db     $2D, $09									; $092D


; COPYRIGHT 1980 ($0868)
        .db     GREEN_CHAR_COLOR							; Color
		.db     $0E											; Row  14
		.db     $02											; Column 2
		.db     C_EN, O_EN, P_EN, Y_EN, R_EN, I_EN, G_EN
		.db     H_EN, T_EN, SP_EN, SP_EN, SP_EN
		.db     DIG1_EN, DIG9_EN, DIG8_EN, DIG0_EN
		.db     $FF											; Terminator

; Top half of Nihon Bussan Co.,Ltd.  ($087C)
		.db     PURPLE_CHAR_COLOR							; Color
		.db     $10											; Row 16
		.db     $02											; Column 2
		.db     $C0, $C1, $C4, $C5, $C8, $C9, $CC, $CD
		.db     $D0, $D1, $D4, $D5, $D8, $D9, $DC, $DD
		.db     $4F, $E0, $E1, $E4, $E5, $E8, $E9, $EC, $ED
        .db     $FF											; Terminator

; Bottom half of Nihon Bussan Co.,Ltd.  ($0899)
		.db     PURPLE_CHAR_COLOR							; Color
		.db     $11											; Row 17
		.db     $02											; Column 2
		.db     $C2, $C3, $C6, $C7
        .db     $CA, $CB, $CE, $CF, $D2, $D3, $D6, $D7
        .db     $DA, $DB, $DE, $DF, $4F, $E2, $E3, $E6
        .db     $E7, $EA, $EB, $EE, $EF
		.db     $FF											; Terminator

; ALL RIGHTS RESERVED. ($08B6)
		.db     TAN_CHAR_COLOR								; Color (Tan)
		.db     $13											; Row 19
        .db     $02											; Column 2
		.db     $0A, $15, $15, $52, $1B, $12, $10
        .db     $11, $1D, $1C, $52, $1B, $0E, $1C, $0E
        .db     $1B, $1F, $0E, $0D, $2C
		.db     $FF											; Terminator

; NO PART OF THIS SOFTWARE MAY ($08CE)
		.db     TAN_CHAR_COLOR								; Color (Tan)
		.db     $15											; Row 21
        .db     $02											; Column 2
		.db     $17, $18, $52, $19, $0A, $1B, $1D
        .db     $52, $18, $0F, $52, $1D, $11, $12, $1C
        .db     $52, $1C, $18, $0F, $1D, $20, $0A, $1B
        .db     $0E, $52, $16, $0A, $22
		.db     $FF											; Terminator
		
; BE COPIED OR USED WITHOUT THE  ($08EE)
		.db     TAN_CHAR_COLOR								; Color (Tan)
		.db     $17											; Row 23
        .db     $02											; Column 2
		.db     $0B, $0E, $52, $0C, $18, $19, $12
        .db     $0E, $0D, $52, $18, $1B, $52, $1E, $1C
        .db     $0E, $0D, $52, $20, $12, $1D, $11, $18
        .db     $1E, $1D, $52, $1D, $11, $0E
		.db     $FF											; Terminator
		
; EXPRESS WRITTEN CONSENT OF ($090F)
		.db     TAN_CHAR_COLOR								; Color (Tan)
		.db     $19											; Row 25
        .db     $02											; Column 2
		.db     $0E, $21, $19, $1B, $0E, $1C
        .db     $1C, $52, $20, $1B, $12, $1D, $1D, $0E
        .db     $17, $52, $0C, $18, $17, $1C, $0E, $17
        .db     $1D, $52, $18, $0F
		.db     $FF											; Terminator
		
; NIHON BUSSAN CO., LTD.  ($090F)
		.db     TAN_CHAR_COLOR								; Color (Tan)
		.db     $1B											; Row 27
        .db     $02											; Column 2
        .db     $17, $12, $11, $18, $17, $52, $0B, $1E
        .db     $1C, $1C, $0A, $17, $52, $0C, $18, $2F
        .db     $52, $15, $1D, $0D, $2C
		.db     $FF											; Terminator

        .db     $C7, $F3									; End of data block


;=============================================================================
; Title screen big sprite ("Crazy Climber") movement
;
; This section of code moves the "Crazy Climber" big sprite during the
; title screen.  This is acomplished by altering the big sprite's Y position.
; This value starts at 240 (top of screen), and is decremented (moves sprite
; down) until it reaches 145.  It's direction is then reversed.
;
; There is one more wrinkle -- the big sprite is 5 lines of 10 bytes per line.
; Upon initialization, only 4 lines are written to big sprite RAM.  As the 
; big sprite moves down, the last line of data needs to be written to the
; screen.  This happens when Y = 224.
;
; There are two flags that are set when these events occur:
;
; GP_82B1:0 - The sprite has not been initialized yet
;         1 - The sprite has been initialized (1st 4 lines copied to big
;             sprite RAM).
;
; GP_82AF:0 - Whole big sprite not on screen yet
;         1 - Whole sprite on screen (still moving down)
;         2 - Sprite reached Y = 145 and is now moving up
;
;=============================================================================
TITLE_HANDLE_BIGSPRITE:  
        PUSH    IY                      ; 0948 FDE5     ..  Save registers used
        PUSH    HL                      ; 094A E5       .
        PUSH    DE                      ; 094B D5       .
        PUSH    BC                      ; 094C C5       .

        LD      IY,BIG_SPRITE_CTRL      ; 094D FD21DC98 .!.. Point to big sprite control

; Is whole sprite on screen?
        LD      A,(GP_82AF)             ; 0951 3AAF82   :P}  
        AND     A                       ; 0954 A7       .    Is Sprite Progress != 0?
        JR      NZ,Lb134                ; 0955 204D      ]   Yes, go to check sprite progress

; Have we initialized this big sprite?
        LD      A,(GP_82B1)             ; 0957 3AB182   :.}  
        AND     A                       ; 095A A7       .	 Is Initialized flag != 0 (initialized)?
        JR      NZ,Lb135                ; 095B 202F      n   Yes, go to check Y position at E0

; Initialize big sprite
        LD      (IY+$01),$03            ; 095D FD360103 .6.. Big sprite color
        LD      (IY+$02),$F0            ; 0961 FD3602F0 .6.. Y position (240 - Top of screen)
        LD      (IY+$03),$40            ; 0965 FD360340 .6SQ X position (64)
        LD      (IY+$00),$04            ; 0969 FD360004 .6DT Priority (4)

;-----------------------------------------
; Copy big sprite data to big sprite RAM
; This copies the following data:
;
; Source      Destination   # Bytes
; ----------  ------------  --------
; $9C4        $88F3         10
; $9D4        $88E3         10
; $9E4        $88D3         10
; $9F4        $88C3         10
;-----------------------------------------
        LD      HL,TITLE_GFX_DATA       ; 096D 21C409   !..  "Crazy Climber" big sprite data (source for copy)
        LD      DE,$88F3                ; 0970 11F388   ...  Big sprite RAM (destination for copy)

Lb136:  LD      BC,$0A                  ; 0973 010A00   .OD  Copy 10 bytes of data
        CALL    BLOCK_COPY              ; 0976 CD4A04   ..T  Block copy routine

;
; Adjust destination (DE) in big sprite ram
; Note: after the block copy, the address is +10 bytes.
; Adding $FFE6 to this is really subtracting 26.  The
; net effect is subtracting 16 each loop.
;
        LD      BC,$FFE6                ; 0979 01E6FF   ...  ($FFE6 = -26)
        EX      DE,HL                   ; 097C EB       .
        ADD     HL,BC                   ; 097D 09       .    
        EX      DE,HL                   ; 097E EB       .    DE = DE - 26
        DEC     (IY+$00)                ; 097F FD3500   .5D  Decrement priority
        JR      NZ,Lb136                ; 0982 20EF      .   Not done, keep looping

        LD      A,$01                   ; 0984 3E01     >.   
        LD      (GP_82B1),A             ; 0986 32B182   2..  Set the sprite initialized flag
        JP      Lb137                   ; 0989 C3BC09   ...  Exit routine

; Check Y position E0
Lb135:  LD      A,(IY+$02)              ; 098C FD7E02   .~G  Get Y position
        CP      $E0                     ; 098F FEE0     ..	 Is Y != 224 (one line scrolled down)?
        JR      NZ,Lb134                ; 0991 3011     0A   Yes, continue

; Y = 224  -- Time to copy last line of sprite data coming onto screen
        LD      HL,TITLE_GFX_TOP_DATA   ; 0993 21EC09   !.. Last line of "Crazy Climber" big sprite data
        LD      DE,$88B3                ; 0996 11B388   ... Big sprite RAM
        LD      BC,$0A                  ; 0999 010A00   .OD Copy 10 bytes of data
        CALL    BLOCK_COPY              ; 099C CD4A04   ..T Block copy routine

        LD      A,$01                   ; 099F 3E01     >.  Mark flag whole sprite on screen
        LD      (GP_82AF),A             ; 09A1 32AF82   2P}

; Check sprite progress
Lb134:  CP      $02                     ; 09A4 FE02     ..  Is sprite progress flag = 2?
        JR      Z,Lb138                 ; 09A6 2811     (A  Yes, scroll up

; Scroll big sprite down
        DEC     (IY+$02)                ; 09A8 FD3502   .5G Decrement Y position
        LD      A,(IY+$02)              ; 09AB FD7E02   .~. Get Y position
        CP      $91                     ; 09AE FE91     ..  Is Y = 145?
        JR      NZ,Lb137                ; 09B0 300A     0.  Nope, exit routine

; See if we have scrolled down enough
        LD      A,$02                   ; 09B2 3E02     >.  Yes, set flag to reverse it's direction
        LD      (GP_82AF),A             ; 09B4 32AF82   2..
        JR      Lb137                   ; 09B7 1803     ..  Exit routine

; Scroll big sprite up
Lb138:  INC     (IY+$02)                ; 09B9 FD3402   .4. Increment the sprite's Y position

Lb137:  POP     BC                      ; 09BC C1       .   Restore registers used
        POP     DE                      ; 09BD D1       .
        POP     HL                      ; 09BE E1       .
        POP     IY                      ; 09BF FDE1     ..
        RET                             ; 09C1 C9       .	End TITLE_HANDLE_BIGSPRITE


;-------------------------------------------------------------------------------
; Title screen "Crazy Climber" Big sprite data
;
; Data Start
; Range: $09C2 - $09F7
;-------------------------------------------------------------------------------

        .db     $C7, $FB											; Data block start

; $09C4
TITLE_GFX_DATA:
        .db     $94, $95, $B4, $B5, $D4, $D5, $F4, $F5, $F5, $CB	; Bottom of sprite
		.db     $92, $93, $B2, $B3, $D2, $D3, $F2, $F3, $EA, $EB
		.db     $90, $91, $B0, $B1, $D0, $D1, $F0, $F1, $E8, $E9
		.db     $8E, $8F, $AE, $AF, $CE, $CF, $EE, $EF, $CA, $C9
; $09EC
TITLE_GFX_TOP_DATA:
        .db     $8C, $8D, $AC, $AD, $CC, $CD, $EC, $ED, $C8, $C9	; Top of sprite

        .db     $C7, $F3											; Data block end

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------


;=============================================================================
; Show number of credits or "FREE" for free play
;=============================================================================
SHOW_CREDITS:   
        NOP                             ; 09F8 00       .
        LD      A,(PLAY_PER_COIN)       ; 09F9 3A7A80   :+. Read plays per coin
        CP      $04                     ; 09FC FE04     ..  Free play?
        JR      Z,Lb143                 ; 09FE 280D     (]  Yes, go here

; No free play
        LD      DE,CREDIT_TEXT          ; 0A00 111E0A   ..O Point to "CREDIT"
        CALL    WRITE_CHARS             ; 0A03 CD7204   .#. Write characters to screen

        LD      DE,CREDIT_VALUE         ; 0A06 11280A   .lO Point to credit digit info
        CALL    WRITE_DIGITS            ; 0A09 CDC504   .:. Write digits to the screen
        RET                             ; 0A0C C9       .

; Free play
Lb143:  LD      DE,FREE_TEXT            ; 0A0D 11160A   .S. Point to "FREE"
        CALL    WRITE_CHARS             ; 0A10 CD7204   .'T Write characters to screen
        RET                             ; 0A13 C9       .   End SHOW_CREDITS


;-------------------------------------------------------------------------------
; Credit data start
; Range: $0A14 - $0A2F
;-------------------------------------------------------------------------------

        .db     $C7, $FB								; Start data block

; "FREE" ($0A16)
FREE_TEXT:
        .db     TAN_CHAR_COLOR							; Color (Tan)
		.db     $1C										; Row (28)
		.db     $01										; Column (1)
		.db     F_EN, R_EN, E_EN, E_EN					; "FREE"
		.db     $FF										; Terminator

; "CREDIT" ($0A1E)
CREDIT_TEXT:
        .db     TAN_CHAR_COLOR							; Color (Tan)
		.db     $1C										; Row (28)
		.db     $01										; Column (1)
		.db     C_EN, R_EN, E_EN, D_EN, I_EN, T_EN		; "CREDIT"
		.db     $FF										; Terminator
		
; Credit digits ($0A28)
CREDIT_VALUE:
		.db     TAN_CHAR_COLOR							; Color (Tan)
		.db     $1D										; Row (29)
		.db     $04										; Column (4)
		.db     $72, $80								; Address of value
		.db     $02										; 2 digits

        .db     $C7, $F3								; End data block

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------



;=============================================================================
; Show 
;               PUSH
; 
;          1 PLAYER BUTTON
;
;               ONLY
;=============================================================================
SHOW_P1_BUTTON:
        NOP                             ; 0A30 00       .
        LD      DE,PUSH_TEXT1           ; 0A31 11460A   ... Point to "PUSH" data
        CALL    WRITE_CHARS             ; 0A34 CD7204   .'T Write characters to screen

        LD      DE,P1_BUTTON_TEXT       ; 0A37 114E0A   ... Point to "1 PLAYER BUTTON" data
        CALL    WRITE_CHARS             ; 0A3A CD7204   .'T Write characters to screen

        LD      DE,ONLY_TEXT            ; 0A3D 11610A   . . Point to "ONLY" data
        CALL    WRITE_CHARS             ; 0A40 CD7204   .'T Write characters to screen
        RET                             ; 0A43 C9       .   End SHOW_P1_BUTTON


;-------------------------------------------------------------------------------
; Push 1 player button only data
;
; Range: $0A44 - $0A6A
;-------------------------------------------------------------------------------

        .db     $C7, $FB								; Start data block

; "PUSH" ($0A46)
PUSH_TEXT1:
        .db     GREEN_CHAR_COLOR						; Color
		.db     $10										; Row (16)
		.db     $0C										; Column (12)
		.db     P_EN, U_EN, S_EN, H_EN					; "PUSH"
		.db     $FF										; Terminator

; "1 PLAYER BUTTON" ($0A4E)
P1_BUTTON_TEXT:
        .db     GREEN_CHAR_COLOR						; Color
		.db     $12										; Row (18)
		.db     $07										; Column (7)
		.db     DIG1_EN, SP_EN, P_EN, L_EN, A_EN, Y_EN, E_EN, R_EN	; "1 PLAYER BUTTON"
		.db     SP_EN, B_EN, U_EN, T_EN, T_EN, O_EN, N_EN
		.db     $FF										; Terminator
		
; "ONLY" ($0A61)
ONLY_TEXT:
		.db     GREEN_CHAR_COLOR						; Color
		.db     $14										; Row (20)
		.db     $0C										; Column (12)
		.db     O_EN, N_EN, L_EN, Y_EN					; "ONLY"
		.db     $FF										; Terminator

        .db     $C7, $F3								; End data block

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------


;=============================================================================
; Show 
;               PUSH
; 
;          1 OR 2 PLAYERS
;
;              BUTTON
;=============================================================================
SHOW_P1_P2_BUTTON:
        NOP                             ; 0A6B 00       .
        LD      DE,PUSH_TEXT2           ; 0A6C 11810A   ..O Point to "PUSH" data
        CALL    WRITE_CHARS             ; 0A6F CD7204   .#. Write characters to screen

        LD      DE,P1_P2_BUTTON_TEXT    ; 0A72 11890A   ..O Point to "1 OR 2 PLAYERS  " data
        CALL    WRITE_CHARS             ; 0A75 CD7204   .#. Write characters to screen

        LD      DE,BUTTON_TEXT          ; 0A78 119D0A   ..O Point to "BUTTON" data
        CALL    WRITE_CHARS             ; 0A7B CD7204   .#. Write characters to screen

        RET                             ; 0A7E C9       .   End SHOW_P1_P2_BUTTON


;-------------------------------------------------------------------------------
; Data for Player 1 or player 2 button press text
;
; Range: $0A7F - $0AA8
;-------------------------------------------------------------------------------

        .db     $C7, $FB								; Start data block

; "PUSH" ($0A81)
PUSH_TEXT2:
        .db     GREEN_CHAR_COLOR						; Color
		.db     $10										; Row (16)
		.db     $0C										; Column (12)
		.db     P_EN, U_EN, S_EN, H_EN					; "PUSH"
		.db     $FF										; Terminator

; "1 OR 2 PLAYERS  " ($0A89)
P1_P2_BUTTON_TEXT:
        .db     GREEN_CHAR_COLOR						; Color
		.db     $12										; Row (18)
		.db     $07										; Column (7)
		.db     DIG1_EN, SP_EN, O_EN, R_EN, SP_EN		; "1 OR 2 PLAYERS  "
        .db     DIG2_EN, SP_EN, P_EN, L_EN, A_EN, Y_EN
		.db     E_EN, R_EN, S_EN, SP_EN, SP_EN
		.db     $FF										; Terminator

; "BUTTON" ($0A9D)
BUTTON_TEXT:
		.db     GREEN_CHAR_COLOR						; Color
		.db     $14										; Row (20)
		.db     $0B										; Column (11)
		.db     B_EN, U_EN, T_EN, T_EN, O_EN, N_EN		; "BUTTON"
		.db     $FF										; Terminator

        .db     $C7, $F3								; End data block

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------


;=============================================================================
; Shows the player's game is over
;=============================================================================
SHOW_PLAYER_OVER:
        NOP                             ; 0AA9 00       .
        CALL    INIT_COLOR_RAM          ; 0AAA CD6304   .vT Initialize color RAM
        LD      A,(CURRENT_PLAYER)      ; 0AAD 3A8180   :.. Check current player number
        OR      A                       ; 0AB0 B7       .
        JR      NZ,Lb147                ; 0AB1 2005      .  Player 2, go here

; Player 1
        LD      DE,P1_OVER_TEXT         ; 0AB3 11CE0A   ... Point to player 1 over data
        JR      Lb148                   ; 0AB6 1803     .S  Continue

; Player 2
Lb147:  LD      DE,P2_OVER_TEXT         ; 0AB8 11DF0A   ..O Point to player 2 over data

Lb148:  CALL    WRITE_CHARS             ; 0ABB CD7204   .#. Write characters to screen

        CALL    UPDATE_GAME_SCORES      ; 0ABE CD6307   .vF Update the game scores

        LD      A,$FF                   ; 0AC1 3EFF     >.
        CALL    DELAY                   ; 0AC3 CDB802   ... Delay

        LD      A,$FF                   ; 0AC6 3EFF     >.
        CALL    DELAY                   ; 0AC8 CDB802   ..G Delay
        RET                             ; 0ACB C9       .   Done SHOW_PLAYER_OVER


;-------------------------------------------------------------------------------
; Data 
;
; Player 1 Over
; Player 2 Over
;
; Range: $0ACC - $0AF1
;-------------------------------------------------------------------------------

        .db     $C7, $FB								; Start data block

; "PLAYER 1 OVER" ($0ACE)
P1_OVER_TEXT:
        .db     GREEN_CHAR_COLOR						; Color
		.db     $0D										; Row 13
		.db     $0A										; Column 10
		.db     P_EN, L_EN, A_EN, Y_EN, E_EN, R_EN		; "PLAYER 1 OVER"
		.db     SP_EN, DIG1_EN, SP_EN, O_EN, V_EN
		.db     E_EN, R_EN
		.db     $FF										; Terminator

; "PLAYER 2 OVER" ($0ADF)
P2_OVER_TEXT:
        .db     GREEN_CHAR_COLOR						; Color
		.db     $0D										; Row 13
		.db     $0A										; Column 10
		.db     P_EN, L_EN, A_EN, Y_EN, E_EN, R_EN		; "PLAYER 2 OVER"
        .db     SP_EN, DIG2_EN, SP_EN, O_EN, V_EN
		.db     E_EN, R_EN
		.db     $FF										; Terminator

        .db     $C7, $F3								; End data block


;=============================================================================
; Shows "GAME OVER" and updates the game scores
; 
; Type:		Subroutine
;=============================================================================
SHOW_GAME_OVER:
        NOP                             ; 0AF2 00       .
        LD      DE,GAME_OVER_TEXT       ; 0AF3 11090B   ..[ Point to "GAME OVER" data
        CALL    WRITE_CHARS             ; 0AF6 CD7204   .'T Write characters to screen

        CALL    UPDATE_GAME_SCORES      ; 0AF9 CD6307   .6. Update the game scores

        LD      A,$FF                   ; 0AFC 3EFF     >.
        CALL    DELAY                   ; 0AFE CDB802   ..G Delay

        LD      A,$FF                   ; 0B01 3EFF     >. 
        CALL    DELAY                   ; 0B03 CDB802   ... Delay
        RET                             ; 0B06 C9       .   End SHOW_GAME_OVER

;-------------------------------------------------------------------------------
; Data for "GAME OVER" text
; Range: $0B07 - $0B17
;-------------------------------------------------------------------------------
        .db     $C7, $FB								; Start data block

GAME_OVER_TEXT:
        .db     GREEN_CHAR_COLOR						; Color
		.db     $11										; Row 17
		.db     $0C										; Column 12
		.db     G_EN, A_EN, M_EN, E_EN, SP_EN			; "GAME OVER"
		.db     O_EN, V_EN, E_EN, R_EN
		.db     $FF										; Terminator

        .db     $C7, $F3								; End data block


;=============================================================================
; Name:		CHECK_HIGH_SCORES
;
; Type:		Subroutine
;
; Checks the user's current score against the high score table.
;
; The score is recorded if it is higher than any of the high score 
; table values.
;
; Note: L keeps track of the high score table index (0 - 4).
;=============================================================================

CHECK_HIGH_SCORES:
        NOP                             ; 0B18 00       .
        LD      IX,CUR_SCORE            ; 0B19 DD21D980 .!..  Point to the current score
        LD      IY,HI_SCORE_VAL1        ; 0B1D FD218380 .!|.  Point IY to high score table (5 high scores, data in sets of 3 bytes)
        LD      H,$05                   ; 0B21 2605     &.    5 high score locations
        LD      L,$00                   ; 0B23 2E00     .D    Start at location 0

; Check byte 1
Lb153:  LD      A,(IX+$00)              ; 0B25 DD7E00   .~D   Get current score byte 1
        SUB     (IY+$00)                ; 0B28 FD9600   ..D   Subtract from high score
        JR      C,Lb151                 ; 0B2B 3818     8.    Score < high score? Yes, check next high score
        JR      NZ,Lb152                ; 0B2D 2021      4    Score > high score? Yes, record this score

; Check byte 2
        LD      A,(IX+$01)              ; 0B2F DD7E01   .~.   Get current score byte 2
        SUB     (IY+$01)                ; 0B32 FD9601   ...   Subtract from high score
        JR      C,Lb151                 ; 0B35 380E     8.    Score < high score? Yes, check next high score
        JR      NZ,Lb152                ; 0B37 2017      .    Score > high score? Yes, record this score

; Check byte 3
        LD      A,(IX+$02)              ; 0B39 DD7E02   .~.   Get current score byte 3
        SUB     (IY+$02)                ; 0B3C FD9602   ..G   Subtract from high score
        JR      C,Lb151                 ; 0B3F 3804     8T    Score < high score? Yes, check next high score
        JR      Z,Lb151                 ; 0B41 2802     (G    Score equal, check next high score

        JR      Lb152                   ; 0B43 180B     ..    (Score > high score), record this score

Lb151:  INC     IY                      ; 0B45 FD23     .#  Go to next high score in the table
        INC     IY                      ; 0B47 FD23     .#
        INC     IY                      ; 0B49 FD23     .#
        INC     L                       ; 0B4B 2C       ,   Keep track of high score location index
        DEC     H                       ; 0B4C 25       %   Decrement high score table counter
        JR      NZ,Lb153                ; 0B4D 20D6      .  Not done? Keep looping
        RET                             ; 0B4F C9       .   Finished -- not high enough to record score

; Record score in high score table
Lb152:  LD      A,L                     ; 0B50 7D       }   A = High score table index (0 - 4)
        LD      (HS_TABLE_IDX),A        ; 0B51 321F81   2.. Save high score table index
        CALL    USER_HAS_HIGH_SCORE     ; 0B54 CD790B   .|. User has high score
        RET                             ; 0B57 C9       .   End CHECK_HIGH_SCORES


;=============================================================================
; Clears a line of video memory
;
; Input:
;	A - Contains the row to clear
;=============================================================================
CLEAR_ROW:  
        NOP                             ; 0B58 00       .
        PUSH    AF                      ; 0B59 F5       .  Save registers used
        PUSH    BC                      ; 0B5A C5       .
        PUSH    DE                      ; 0B5B D5       .
        PUSH    HL                      ; 0B5C E5       .

; Calculate offset into screen RAM
        LD      HL,SCREEN_RAM           ; 0B5D 210090   !D. Point to screen ram
        RLCA                            ; 0B60 07       .   A = A * 8
        RLCA                            ; 0B61 07       .
        RLCA                            ; 0B62 07       .
; Make sure A is multiple of 8
        AND     $F8                     ; 0B63 E6F8     ..  Mask A with 1111 1000
        LD      E,A                     ; 0B65 5F       _
        LD      D,$00                   ; 0B66 1600     .D
        ADD     HL,DE                   ; 0B68 19       .   HL = SCREEN_RAM + (32 * A)
        ADD     HL,DE                   ; 0B69 19       .
        ADD     HL,DE                   ; 0B6A 19       .
        ADD     HL,DE                   ; 0B6B 19       .

        LD      B,$20                   ; 0B6C 0620     .d  B = 32 columns per row

; Clear row
Lb155:  LD      (HL),$52                ; 0B6E 3652     6.  Clear space
        INC     HL                      ; 0B70 23       #   Go to next value
        DEC     B                       ; 0B71 05       .   
        JR      NZ,Lb155                ; 0B72 20FA      .  Is column counter = 0?  Nope, keep looping

        POP     HL                      ; 0B74 E1       .  Restore registers used
        POP     DE                      ; 0B75 D1       .
        POP     BC                      ; 0B76 C1       .
        POP     AF                      ; 0B77 F1       .
        RET                             ; 0B78 C9       .
;-----------------------------------------------------------------------------


;-----------------------------------------------------------------------------
; User has a high score
; 
;-----------------------------------------------------------------------------
USER_HAS_HIGH_SCORE:
        NOP                             ; 0B79 00       .

        CALL    SHOW_HI_SCORE_TABLE     ; 0B7A CD370E   .w. Show high score table

        CALL    SHOW_NAME_REG_SCREEN    ; 0B7D CD6A0F   .k. Show name registration info

; Set registration timeout to 59:1
        LD      A,$59                   ; 0B80 3E59     >\
        LD      (REG_TIME_SEC_VAL),A    ; 0B82 32B282   2.. 59 seconds
        LD      A,$10                   ; 0B85 3E10     >.
        LD      (REG_TIME_TENTHS_VAL),A ; 0B87 32B382   2.} 10 tenths

        LD      DE,REG_TIME_TXT         ; 0B8A 11180E   ... "REG TIME"
        CALL    WRITE_CHARS             ; 0B8D CD7204   .#. Write characters to screen

        LD      DE,REG_TIME_COLON       ; 0B90 11240E   .5. ":" for time
        CALL    WRITE_CHARS             ; 0B93 CD7204   .#. Write characters to screen

        LD      DE,REG_TIME_SECONDS     ; 0B96 11290E   .8. Seconds digits
        CALL    WRITE_DIGITS            ; 0B99 CDC504   .:. Write digits to the screen

        LD      DE,REG_TIME_TENTHS      ; 0B9C 112F0E   .*. Tenths digits
        CALL    WRITE_DIGITS            ; 0B9F CDC504   .:. Write digits to the screen

        XOR     A                       ; 0BA2 AF       .
        LD      (HS_CURSOR_POS),A       ; 0BA3 321C81   2.. Clear high score cursor position
        XOR     A                       ; 0BA6 AF       .
        LD      (HS_NUM_CHARS),A        ; 0BA7 321D81   2X. Zero high score characters entered
        JP      MOVE_CURSOR_SPRITE      ; 0BAA C3EF0B   ... Move cursor spirte

Lb173:  JP      Lb158                   ; 0BAD C32000   .dD

        OR      A                       ; 0BB0 B7       .
        JR      NZ,Lb2                  ; 0BB1 2005      .


; Look at controls to enter high score name

; Current player is player 1
Lb1:    LD      A,(PL1_CONT_RD)         ; 0BB3 3A00A0   :D_ Read player 1 controls
        JR      Lb159                   ; 0BB6 1803     .S

; Current player is player 2
Lb2:    LD      A,(PL2_CONT_RD)         ; 0BB8 3A00A8   :D. Read player 2 controls

Lb159:  LD      (CUR_PLAYER_INPUT),A    ; 0BBB 325481   2.. Save player input
        AND     $04                     ; 0BBE E604     ..  Left control, Left direction
        JR      NZ,Lb160                ; 0BC0 2012      F  Yes, go here

        LD      A,(CUR_PLAYER_INPUT)    ; 0BC2 3A5481   :.. Get player input
        AND     $08                     ; 0BC5 E608     .L  Left control, Right direction
        JR      NZ,Lb161                ; 0BC7 2018      .  Yes, go here

Lb164:  LD      A,(CUR_PLAYER_INPUT)    ; 0BC9 3A5481   :.. Get player input
        AND     $F0                     ; 0BCC E6F0     ..  Any right control directions?
        JP      NZ,Lb162                ; 0BCE C2650C   .p\ Yes, go here
        JP      REGISTRATION_TICK       ; 0BD1 C3DA0C   ... Nope, continue 

; Left control, Left direction
Lb160:  LD      A,(HS_CURSOR_POS)       ; 0BD4 3A1C81   :H. Get the high score cursor position
        OR      A                       ; 0BD7 B7       .
        JP      Z,REGISTRATION_TICK     ; 0BD8 CADA0C   ..\ If zero, continue

        DEC     A                       ; 0BDB 3D       =   Decrement cursor position
        LD      (HS_CURSOR_POS),A       ; 0BDC 321C81   2H. Save value
        JR      MOVE_CURSOR_SPRITE      ; 0BDF 180E     ..  Move cursor sprite

; Left control, Right direction
Lb161:  LD      A,(HS_CURSOR_POS)       ; 0BE1 3A1C81   :.. Get the high score cursor position
        CP      $1C                     ; 0BE4 FE1C     .H  Is value 28?
        JP      Z,REGISTRATION_TICK     ; 0BE6 CADA0C   ..\ Yes, continue

        INC     A                       ; 0BE9 3C       <   Increment cursor position
        LD      (HS_CURSOR_POS),A       ; 0BEA 321C81   2H. Save value
        JR      MOVE_CURSOR_SPRITE      ; 0BED 1800     .D  Move cursor sprite

;-----------------------------------------------------------------------------
; Move Cursor sprite
;-----------------------------------------------------------------------------
MOVE_CURSOR_SPRITE:
        LD      IX,SPRITE_CTRL          ; 0BEF DD218098 .!.. Point IX to the sprite control space
        LD      HL,HS_CURSOR_XY_DATA    ; 0BF3 21290C   !<.  Point HL to the high score cursor data
        LD      A,(HS_CURSOR_POS)       ; 0BF6 3A1C81   :H.  Get the cursor position
        RLCA                            ; 0BF9 07       .    Multiply by 2
        AND     $FE                     ; 0BFA E6FE     ..   
        LD      E,A                     ; 0BFC 5F       _
        LD      D,$00                   ; 0BFD 1600     .D   HL = HL + 2 * (cursor position)
        ADD     HL,DE                   ; 0BFF 19       .

; Get X data byte from table and decode
        LD      A,(HL)                  ; 0C00 7E       ~    Get X value for cursor
        LD      B,$12                   ; 0C01 0612     ..   B = 18
        SUB     B                       ; 0C03 90       .    A = A - 18
        LD      (IX+$03),A              ; 0C04 DD7703   .w.  Set X position

; Get Y data byte from table and decode
        INC     HL                      ; 0C07 23       #    Go to next cursor position point
        LD      B,(HL)                  ; 0C08 46       F    Get Y value for cursor
        LD      A,$F2                   ; 0C09 3EF2     >.   A = 242 
        SUB     B                       ; 0C0B 90       .    A = 242 - Y value from table
        LD      (IX+$02),A              ; 0C0C DD7702   .wG  Set Y position

        LD      (IX+$00),SPRITE_HS_CURSOR ; 0C0F DD36000E .6D. $0E is the high score cursor sprite
        LD      (IX+$01),$02            ; 0C13 DD360102 .6.G Set color (2)
        LD      A,(CURRENT_PLAYER)      ; 0C17 3A8180   :..  Get current player number
        OR      A                       ; 0C1A B7       .
        JP      Z,Lb164                 ; 0C1B CAC90B   ..[  Player 1, go here

; Player 2 is current player
        DEC     (IX+$02)                ; 0C1E DD3502   .5G  Subtract 2 from Y position
        DEC     (IX+$02)                ; 0C21 DD3502   .5.
        JP      Lb164                   ; 0C24 C3C90B   ...


;-------------------------------------------------------------------------------
; Data for high score cursor X and Y position
; Range: $0C27 - $0C64
;-------------------------------------------------------------------------------

        .db     $C7, $FB									; Start data block

; High score cursor sprite position ($0C29)
;
; Data is given in (X, Y) values
; It is decoded after it is read from the table.  These decoded values are
; used to move the cursor sprite around
;
; X decoded = (X table) - 18
; Y decoded = 242 - (Y table)
;
HS_CURSOR_XY_DATA:
                                ; First row
        .db     $35, $9C		; A   ( 35, 86)
		.db     $45, $9C		; B   ( 51, 86)
		.db     $55, $9C		; C   ( 67, 86)
		.db     $65, $9C		; D   ( 83, 86)
        .db     $75, $9C		; E   ( 99, 86)
		.db     $85, $9C		; F   (115, 86)
		.db     $95, $9C		; G   (131, 86)
		.db     $A5, $9C		; H   (147, 86)
        .db     $B5, $9C		; I   (163, 86)

                                ; Second Row
		.db     $35, $AC		; J   ( 35, 70)
		.db     $45, $AC		; K   ( 51, 70)
		.db     $55, $AC		; L   ( 67, 70)
        .db     $65, $AC		; M   ( 83, 70)
		.db     $75, $AC		; N   ( 99, 70)
		.db     $85, $AC		; O   (115, 70)
		.db     $95, $AC		; P   (131, 70)
        .db     $A5, $AC		; Q   (147, 70)
		.db     $B5, $AC		; R   (162, 70)
		.db     $C9, $AC		; Rub (183, 70)

                                ; Third row
		.db     $35, $BC		; S   ( 35, 54)
        .db     $45, $BC		; T   ( 51, 54)
		.db     $55, $BC		; U   ( 67, 54)
		.db     $65, $BC		; V   ( 83, 54)
		.db     $75, $BC		; W   ( 99, 54)
        .db     $85, $BC		; X   (115, 54)
		.db     $95, $BC		; Y   (131, 54)
		.db     $A5, $BC		; Z   (147, 54)
		.db     $B5, $BC		; .   (162, 54)
        .db     $C7, $BC		; End (181, 54)

        .db     $C7, $F3									; End data block

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------


; Right control movement
Lb162:  LD      A,(HS_CURSOR_POS)       ; 0C65 3A1C81   :.. Get the cursor position
        CP      $1C                     ; 0C68 FE1C     .H  User chose End?
        JP      Z,REGISTRATION_COMPLETE ; 0C6A CA1A0D   .N. Yes, complete registration

        CP      $12                     ; 0C6D FE12     ..  User chose Rub?
        JR      Z,Lb166                 ; 0C6F 2830     (1  Yes, go here

        CP      $12                     ; 0C71 FE12     ..  Is choice < Rub?
        JR      C,Lb167                 ; 0C73 3808     8L  Yes, go here

        CP      $1B                     ; 0C75 FE1B     .Z  Is choice period?
        JR      Z,Lb168                 ; 0C77 2808     (L  Yes, go here

;--------------------------------------------------------
; Selection is S - Z
; Convert cursor position to an encoded character value
;
; Cursor position	Selection	Encoded value
; ---------------	---------	-------------
; $13				S			$1C
; 1					B			$0B
; ...				...			...
; $11				R			$1B
        ADD     A,$09                   ; 0C79 C609     ..  Convert cursor position to encoded character 
        JR      Lb169                   ; 0C7B 1806     ..  Continue

;--------------------------------------------------------
; Choice is less than Rub (i.e. A - R)
; Convert cursor position to an encoded character value
;
; Cursor position	Selection	Encoded value
; ---------------	---------	-------------
; 0					A			$0A
; 1					B			$0B
; ...				...			...
; $11				R			$1B
Lb167:  ADD     A,$0A                   ; 0C7D C60A     .O  Convert cursor position to encoded character
        JR      Lb169                   ; 0C7F 1802     .G  Continue

;--------------------
; User chose period
Lb168:  LD      A,PERIOD_EN             ; 0C81 3E2C     >|  A = encoded period character


;-----------------------------------------
; Add chosen character to high score name
; A contains the character to set
Lb169:  LD      (HS_CHOSEN_CHAR),A      ; 0C83 321E81   2[. Save chosen character
        LD      A,(HS_NUM_CHARS)        ; 0C86 3A1D81   :Y. Get number of high score name characters
        CP      $03                     ; 0C89 FE03     ..  Equal to 3?
        JR      NZ,REGISTRATION_TICK    ; 0C8B 304D     0]  No, continue with registration

        LD      HL,USER_HS_NAME         ; 0C8D 211181   !A. Point to user high score name
        LD      E,A                     ; 0C90 5F       _   DE = index into high score name
        LD      D,$00                   ; 0C91 1600     .D
        ADD     HL,DE                   ; 0C93 19       .   HL points to proper location in H.S. name
        LD      A,(HS_CHOSEN_CHAR)      ; 0C94 3A1E81   :.. Get chosen character
        LD      (HL),A                  ; 0C97 77       w   Store it in the High score name
        LD      A,(HS_NUM_CHARS)        ; 0C98 3A1D81   :Y. Increment # characters entered
        INC     A                       ; 0C9B 3C       <
        LD      (HS_NUM_CHARS),A        ; 0C9C 321D81   2Y.
        JR      DISPLAY_HS_NAME         ; 0C9F 181A     ..  Display the high score name

;--------------------------------
; User wants to rub a character
Lb166:  LD      A,SP_EN                 ; 0CA1 3E52     >.  Write space character to rub chosen character
        LD      (HS_CHOSEN_CHAR),A      ; 0CA3 321E81   2[. 
        LD      A,(HS_NUM_CHARS)        ; 0CA6 3A1D81   :Y. Get number of high score name characters
        OR      A                       ; 0CA9 B7       .
        JR      Z,REGISTRATION_TICK     ; 0CAA 282E     (o  Zero?  Continue

        DEC     A                       ; 0CAC 3D       =   Decrement number of characters entered
        LD      (HS_NUM_CHARS),A        ; 0CAD 321D81   2X.
        LD      HL,USER_HS_NAME         ; 0CB0 211181   !A. Point to user high score name
        LD      E,A                     ; 0CB3 5F       _   DE = index into high score name
        LD      D,$00                   ; 0CB4 1600     .D
        ADD     HL,DE                   ; 0CB6 19       .   HL points to proper store location in H.S. name
        LD      A,(HS_CHOSEN_CHAR)      ; 0CB7 3A1E81   :[. Get current chosen character
        LD      (HL),A                  ; 0CBA 77       w   Save it

;--------------------------------------------------
; This displays the high score name on the screen
;
; Note: The data section works like this:
;
; $810E - Color (Green)
; $810F - Row (18)
; $8110 - Column (11)
; $8111 - Start of the saved high score name (up to 10 characters)
; ...
; $811A - End of saved high score name
; $811B - $FF (terminator)

DISPLAY_HS_NAME:
        LD      IX,HS_NAME_REG_DATA     ; 0CBB DD210E81 .!O. Location of high score name registration data
        LD      (IX+$00),GREEN_CHAR_COLOR ; 0CBF DD36000B .6D. Set color
        LD      (IX+$01),$12            ; 0CC3 DD360112 .6.. Set row = 18
        LD      (IX+$02),$0B            ; 0CC7 DD36020B .6.. Set column = 11
        LD      (IX+$0D),$FF            ; 0CCB DD360DFF .6]. Data - termination at end of H.S. name

        LD      DE,HS_NAME_REG_DATA     ; 0CCF 110E81   ...  Point to high score name registration data
        CALL    WRITE_CHARS             ; 0CD2 CD7204   .'T  Write characters to screen

        LD      A,$50                   ; 0CD5 3E50     >E
        CALL    DELAY                   ; 0CD7 CDB802   ... Delay

;-----------------------------------------------------------------------------
; Subtract a tenth from the registration timeout after a delay
;
REGISTRATION_TICK:

; Delay 
        LD      A,$30                   ; 0CDA 3E30     > 
        CALL    DELAY                   ; 0CDC CDB802   ..G Delay

; Subtract a tenth
        LD      HL,REG_TIME_TENTHS_VAL  ; 0CDF 21B382   !.} Get registration timeout tenths
        LD      A,(HL)                  ; 0CE2 7E       ~ 
        SUB     $01                     ; 0CE3 D601     ..  Subtract one
        DAA                             ; 0CE5 27       '   Decimal adjust
        LD      (HL),A                  ; 0CE6 77       w   Store value
        JR      NZ,Lb171                ; 0CE7 2008      L  Not zero, continue

; Tenths are zero - subtract a second
        LD      (HL),$10                ; 0CE9 3610     6.  Re-load tenths
        DEC     HL                      ; 0CEB 2B       +   Point to seconds (previous memory location)
        LD      A,(HL)                  ; 0CEC 7E       ~   Get seconds
        SUB     $01                     ; 0CED D601     ..  Subtract 1
        DAA                             ; 0CEF 27       '   Decimal adjust
        LD      (HL),A                  ; 0CF0 77       w   Store value

;-----------------------------------------------------------------------------
; Check for registration timeout

Lb171:  LD      HL,REG_TIME_SEC_VAL     ; 0CF1 21B282   !.} Get registration seconds left
        LD      A,(HL)                  ; 0CF4 7E       ~
        CP      $00                     ; 0CF5 FE00     .D  Zero?
        JR      NZ,Lb172                ; 0CF7 2012      .  Nope, continue

        INC     HL                      ; 0CF9 23       #   Check tenths (next memory location)
        LD      A,(HL)                  ; 0CFA 7E       ~  
        CP      $01                     ; 0CFB FE01     ..  Is value 1?
        JR      NZ,Lb172                ; 0CFD 200C      \  Nope, continue

        XOR     A                       ; 0CFF AF       .
        LD      (REG_TIME_TENTHS_VAL),A ; 0D00 32B382   2.. Clear tenths

; Registration timeout
        LD      DE,REG_TIME_TENTHS      ; 0D03 112F0E   .nO Tenths digits
        CALL    WRITE_DIGITS            ; 0D06 CDC504   ..T Write digits to the screen
        JR      REGISTRATION_COMPLETE   ; 0D09 180F     .N  Complete registration due to timeout


; Update registration time display
Lb172:  LD      DE,REG_TIME_SECONDS     ; 0D0B 11290E   .<O Seconds digits
        CALL    WRITE_DIGITS            ; 0D0E CDC504   ..T Write digits to the screen

        LD      DE,REG_TIME_TENTHS      ; 0D11 112F0E   .nO Tenths digits
        CALL    WRITE_DIGITS            ; 0D14 CDC504   ..T Write digits to the screen

        JP      Lb173                   ; 0D17 C3AD0B   ..[

; Registration complete
REGISTRATION_COMPLETE:

;-----------------------------------------------------------------------------
; This section of code figures out where our high score will be, and moves all
; high score values under it one space down the list.
;-----------------------------------------------------------------------------
;
; Note: HS_TABLE_IDX = 0 for the highest high score, 4 for the lowest high score
;
        LD      A,(HS_TABLE_IDX)        ; 0D1A 3A1F81   :_. Get the high score index value
        LD      B,A                     ; 0D1D 47       G   Subtract that value from 4
        LD      A,$04                   ; 0D1E 3E04     >.
        SUB     B                       ; 0D20 90       .
        LD      B,A                     ; 0D21 47       G   B is the result (4 - HS_TABLE_IDX)
        OR      A                       ; 0D22 B7       .   Is result zero (last high score value)?
        JP      Z,Lb174                 ; 0D23 CA700D   .e] Yes, continue here (no need to move any values)

        LD      IX,HI_SCORE_VAL4        ; 0D26 DD218C80 .!.. IX points to next to last high score value
        LD      IY,HI_SCORE_VAL5        ; 0D2A FD218F80 .!p. IY points to last high score value
        LD      DE,-6                   ; 0D2E 11FAFF   ...  Used to adjust pointers later...

Lb176:  LD      C,$03                   ; 0D31 0E03     ..   3 bytes per high score value

; Moves the high score down one position
Lb175:  LD      A,(IX+$00)              ; 0D33 DD7E00   .~D  Get higher high score byte
        LD      (IY+$00),A              ; 0D36 FD7700   .wD  Copy to lower high score byte
        INC     IX                      ; 0D39 DD23     .#   Go to next byte
        INC     IY                      ; 0D3B FD23     .#   Go to next byte
        DEC     C                       ; 0D3D 0D       .    Decrement byte count
        JR      NZ,Lb175                ; 0D3E 20F3      .   Done? Nope, continue looping

; Go to next high score to move
        ADD     IX,DE                   ; 0D40 DD19     ..   Add a -6 to IX
        ADD     IY,DE                   ; 0D42 FD19     ..   Add a -6 to IY
        DEC     B                       ; 0D44 05       .    Decrement table counter
        JR      NZ,Lb176                ; 0D45 20EA      .   Done? Nope, keep moving

;-----------------------------------------------------------------------------
; This section of code figures out where our high score will be, and moves all
; high score names under it one space down the list.
;-----------------------------------------------------------------------------
;
; Note: HS_TABLE_IDX = 0 for the highest high score, 4 for the lowest high score
;
        LD      A,(HS_TABLE_IDX)        ; 0D47 3A1F81   :..  Get the high score index value
        LD      B,A                     ; 0D4A 47       G    Subtract that value from 4
        LD      A,$04                   ; 0D4B 3E04     >T
        SUB     B                       ; 0D4D 90       .
        LD      B,A                     ; 0D4E 47       G    B is the result (4 - HS_TABLE_IDX)
        LD      IX,HS_NAME4             ; 0D4F DD21BF80 .!.. IX points to the next to last name
        LD      IY,HS_NAME5             ; 0D53 FD21CD80 .!.. IY points to the last name

Lb178:  LD      C,$0A                   ; 0D57 0E0A     .O   Copy 10 bytes (the name)

; Moves the high score name down one position
Lb177:  LD      A,(IX+$00)              ; 0D59 DD7E00   .~D  Get the higher high score name byte
        LD      (IY+$00),A              ; 0D5C FD7700   .wD  Store in the lower high score name byte
        INC     IX                      ; 0D5F DD23     .#   Go to next name byte
        INC     IY                      ; 0D61 FD23     .#   Go to next name byte
        DEC     C                       ; 0D63 0D       .    Decrement byte counter
        JR      NZ,Lb177                ; 0D64 20F3      .   Done? Nope, keep looping

        LD      DE,-24                  ; 0D66 11E8FF   ...  Used to adjust pointers
; Point to next high scores to move (source and destination)
        ADD     IX,DE                   ; 0D69 DD19     ..   Add a -24 to IX
        ADD     IY,DE                   ; 0D6B FD19     ..   Add a -24 to IY
        DEC     B                       ; 0D6D 05       .    Decrement table counter
        JR      NZ,Lb178                ; 0D6E 20E7      .   Done? Nope, continue looping

; Locate proper place in the table to put the new high score
Lb174:  LD      A,(HS_TABLE_IDX)        ; 0D70 3A1F81   :_.  Get the table index
        LD      B,A                     ; 0D73 47       G    Store in B
        LD      C,A                     ; 0D74 4F       O    Store in C
        LD      IY,HI_SCORE_VAL1        ; 0D75 FD218380 .!|. Point to the high score table
        OR      A                       ; 0D79 B7       .    Is table index = 0?
        JR      Z,Lb179                 ; 0D7A 2809     (.   Yes, continue here

Lb180:  INC     IY                      ; 0D7C FD23     .#   Go to next score
        INC     IY                      ; 0D7E FD23     .#
        INC     IY                      ; 0D80 FD23     .#
        DEC     B                       ; 0D82 05       .    Decrement counter
        JR      NZ,Lb180                ; 0D83 20F7      .   Not done? continue looping


;-----------------------------------------------------------------------------
; Copies the score to high score table
; C contains the high score index value
; IY points to the proper location in the high score table
;-----------------------------------------------------------------------------
Lb179:  LD      IX,CUR_SCORE            ; 0D85 DD21D980 .!.. Point to the current score
        LD      B,$03                   ; 0D89 0603     ..   Loop three times

Lb181:  LD      A,(IX+$00)              ; 0D8B DD7E00   .~D  Read score bytes
        LD      (IY+$00),A              ; 0D8E FD7700   .wD  Copy to IY location
        INC     IX                      ; 0D91 DD23     .#   Go to next byte
        INC     IY                      ; 0D93 FD23     .#   Go to next bytes
        DEC     B                       ; 0D95 05       .    Decrement loop counter
        JR      NZ,Lb181                ; 0D96 20F3      .   Not done? continue looping

        LD      IY,HS_NAME1             ; 0D98 FD219580 .!.. Point to the 1st high score name
        LD      A,C                     ; 0D9C 79       y    Is the High score index = 0 (highest score)?
        OR      A                       ; 0D9D B7       .
        JR      Z,CHECK_JORDAN_LTD      ; 0D9E 2808     (L   Yes, check JORDAN.LTD easter egg

; Point IY to proper high score location
        LD      DE,$0E                  ; 0DA0 110E00   .OD  14 bytes in each name location
Lb183:  ADD     IY,DE                   ; 0DA3 FD19     ..   Go to next high score location
        DEC     C                       ; 0DA5 0D       .    Decrement counter
        JR      NZ,Lb183                ; 0DA6 20FB      .   Done? Nope, keep looping



;-----------------------------------------------------------------------------
; Easter Egg
;
; Compares the user's entered high score name to "JORDAN.LTD"
; If it matches, two credits are added
;
;-----------------------------------------------------------------------------
CHECK_JORDAN_LTD:
        LD      HL,JORDAN_LTD_TXT       ; 0DA8 210E0E   !O.  Point to "JORDAN.LTD"
        LD      IX,USER_HS_NAME         ; 0DAB DD211181 .!A. Point to user's high score name
        LD      B,$0A                   ; 0DAF 060A     .O   Compare 10 characters

Lb185:  LD      C,(HL)                  ; 0DB1 4E       N    Read Jordan byte
        LD      A,(IX+$00)              ; 0DB2 DD7E00   .~D  Read user's byte
        CP      C                       ; 0DB5 B9       .    Compare values
        JR      NZ,Lb184                ; 0DB6 201F      _   Not equal - continue

        INC     HL                      ; 0DB8 23       #    Go to next Jordan byte
        INC     IX                      ; 0DB9 DD23     .#   Go to next user byte
        DEC     B                       ; 0DBB 05       .    Decrement counter
        JR      NZ,Lb185                ; 0DBC 20F3      .   Not done? Keep looping

;
; User's high score matches the easter egg!
; Add two credits
;
        LD      A,(NUM_CREDITS)         ; 0DBE 3A7280   :'. Get number of credits
        ADD     A,$02                   ; 0DC1 C602     .G  Add two credits
        DAA                             ; 0DC3 27       '   Decimal adjust
        LD      (NUM_CREDITS),A         ; 0DC4 327280   2'. Update number of credits

;-----------------------------------------------------------------------------
; Remove last four characters of high score.  This is required so credits are
; not given every time this is checked.
;
; "JORDAN.LTD" -> "JORDAN    "
;
; Note: IX is pointing just past last HS value...
;-----------------------------------------------------------------------------
        LD      (IX-1),SP_EN            ; 0DC7 DD36FF52 .... Put space at IX - 1
		LD      (IX-2),SP_EN            ; 0DCB DD36FE52 .... Put space at IX - 2
		LD      (IX-3),SP_EN            ; 0DCF DD36FD52 .... Put space at IX - 3
		LD      (IX-4),SP_EN            ; 0DD3 DD36FC52 .... Put space at IX - 4
; Done checking JORDAN.LTD easter egg


;-----------------------------------------------------------------------------
; Copy user's name to high score table
; IY should point to the proper location in the high score table
;-----------------------------------------------------------------------------
Lb184:  LD      IX,USER_HS_NAME         ; 0DD7 DD211181 .!A. Point to user high score name
        LD      C,$0A                   ; 0DDB 0E0A     .O   10 characters to copy

Lb186:  LD      A,(IX+$00)              ; 0DDD DD7E00   .~D  Get user high score name byte
        LD      (IY+$00),A              ; 0DE0 FD7700   .wD  Copy to high score table
        INC     IX                      ; 0DE3 DD23     .#   Go to next byte
        INC     IY                      ; 0DE5 FD23     .#   Go to next byte
        DEC     C                       ; 0DE7 0D       .    Decrement byte counter
        JR      NZ,Lb186                ; 0DE8 20F3      .   Done?  Nope, keep looping

        CALL    SHOW_HI_SCORE_TABLE     ; 0DEA CD370E   .w.  Show high score table

;-----------------------------------------------------------------------------
; Zero the Y position of the cursor sprite (to move it off of the screen)
; $9880 is the cursor sprite
; $9880 + 2 is the Y position
;-----------------------------------------------------------------------------
        XOR     A                       ; 0DED AF       .
        LD      ($9882),A               ; 0DEE 328298   2}.

        LD      A,$FF                   ; 0DF1 3EFF     >.
        CALL    DELAY                   ; 0DF3 CDB802   ... Delay

        LD      A,$FF                   ; 0DF6 3EFF     >.
        CALL    DELAY                   ; 0DF8 CDB802   ..G Delay

        LD      A,$FF                   ; 0DFB 3EFF     >.
        CALL    DELAY                   ; 0DFD CDB802   ... Delay

; Clear rows on screen
        LD      B,$1C                   ; 0E00 061C     .H  Clear 28 rows
        LD      A,$02                   ; 0E02 3E02     >.  Start a row 2

Lb188:  CALL    CLEAR_ROW               ; 0E04 CD580B   ... Clear row of data
        INC     A                       ; 0E07 3C       <   Go to next row
        DEC     B                       ; 0E08 05       .   Decrement counter
        JR      NZ,Lb188                ; 0E09 20F9      .  Done? Nope - keep looping

        RET                             ; 0E0B C9       .   End USER_HAS_HIGH_SCORE subroutine



;-------------------------------------------------------------------------------
; Data for JORDAN.LTD easter egg
;      -and-
; registration time
;
; Range: $0E0C - $0E36
;-------------------------------------------------------------------------------

        .db     $C7, $FB								; Start data block

; "JORDAN.LTD" at $0E0E
JORDAN_LTD_TXT:
        .db     J_EN, O_EN, R_EN, D_EN, A_EN, N_EN
		.db     PERIOD_EN, L_EN, T_EN, D_EN

; $0E18
REG_TIME_TXT:
        .db     TAN_CHAR_COLOR							; Color
		.db     $1A										; Row 26
		.db     $07										; Column 7
		.db     R_EN, E_EN, G_EN, SP_EN					; "REG TIME"
		.db     T_EN, I_EN, M_EN, E_EN
		.db     $FF										; Terminator

; $0E24
REG_TIME_COLON:
        .db     TAN_CHAR_COLOR							; Color
		.db     $1C										; Row 28
		.db     $0C										; Column 12
		.db     COLON_EN								; ":"
		.db     $FF										; Terminator

; Time left seconds
; $0E29
REG_TIME_SECONDS:
        .db     TAN_CHAR_COLOR							; Color
		.db     $1C										; Row 28
		.db     $0A										; Column 10
		.db     $B2, $82								; Address $82B2
		.db     $02										; 2 digits

; Time left tenths
; $0E2F
REG_TIME_TENTHS:
        .db     TAN_CHAR_COLOR							; Color
		.db     $1C										; Row 28
		.db     $0D										; Column 13
		.db     $B3, $82								; Address $82B3
		.db     $01										; 1 digit

        .db     $C7, $F3								; End data block



;=============================================================================
; Name:			SHOW_HI_SCORE_TABLE
;
; Description:	Show high score table
;
;=============================================================================
SHOW_HI_SCORE_TABLE:
        NOP                             ; 0E37 00       .
        CALL    INIT_BIG_SPRITE_RAM     ; 0E38 CD4705   .B. Initialize big sprite RAM

        CALL    INIT_COLOR_RAM          ; 0E3B CD6304   .6. Initialize color RAM

; Clear rows on screen
        LD      A,$02                   ; 0E3E 3E02     >.  Start at row 2
        LD      B,$34                   ; 0E40 0634     .`  Clear 52 rows
Lb190:  CALL    CLEAR_ROW               ; 0E42 CD580B   ... Clear row of data
        INC     A                       ; 0E45 3C       <   Go to next row
        DEC     B                       ; 0E46 05       .   Decrement counter
        JR      NZ,Lb190                ; 0E47 20F9      .  Done? Nope - keep looping


; Write "SCORE    NAME" to screen
        LD      DE,HS_SCORE_NAME        ; 0E49 11100F   ... Point to "SCORE     NAME" data
        CALL    WRITE_CHARS             ; 0E4C CD7204   .'T Write characters to screen


; Hi score location 1
        LD      DE,HS_NO1               ; 0E4F 11220F   .g. Write "NO1:" to screen
        CALL    WRITE_CHARS             ; 0E52 CD7204   .'T Write characters to screen

        LD      DE,HS_VAL1              ; 0E55 114A0F   .K.  Point to high score value 1
        CALL    WRITE_DIGITS            ; 0E58 CDC504   ..T  Write digits to the screen

        LD      IX,HS_NAME_DATA1        ; 0E5B DD219280 .!.. Point to high score name data 1
        LD      (IX+$00),TAN_CHAR_COLOR ; 0E5F DD36000A .6DO Color
        LD      (IX+$01),$05            ; 0E63 DD360105 .6.. Row 5
        LD      (IX+$02),$11            ; 0E67 DD360211 .6.A Column 17
        LD      (IX+$0D),$FF            ; 0E6B DD360DFF .6]. Set terminator at end of name data
        LD      DE,HS_NAME_DATA1        ; 0E6F 119280   ...  Point to name data set
        CALL    WRITE_CHARS             ; 0E72 CD7204   .'T  Write characters to screen

; Hi score location 2
        LD      DE,HS_NO2               ; 0E75 112A0F   .o.  Write "NO2:" to screen
        CALL    WRITE_CHARS             ; 0E78 CD7204   .'T  Write characters to screen

        LD      DE,HS_VAL2              ; 0E7B 11500F   .E.  Point to high score value 2
        CALL    WRITE_DIGITS            ; 0E7E CDC504   ..T  Write digits to the screen

        LD      IX,HS_NAME_DATA2        ; 0E81 DD21A080 .!_. Point to high score name data 2 
        LD      (IX+$00),TAN_CHAR_COLOR ; 0E85 DD36000A .6DO Color
        LD      (IX+$01),$07            ; 0E89 DD360107 .6.F Row 7
        LD      (IX+$02),$11            ; 0E8D DD360211 .6.A Column 17
        LD      (IX+$0D),$FF            ; 0E91 DD360DFF .6]. Set terminator at end of name data
        LD      DE,HS_NAME_DATA2        ; 0E95 11A080   ...  Point to name data set
        CALL    WRITE_CHARS             ; 0E98 CD7204   .'T  Write characters to screen

; Hi score location 3
        LD      DE,HS_NO3               ; 0E9B 11320F   .'.  Write "NO3:" to screen
        CALL    WRITE_CHARS             ; 0E9E CD7204   .'T  Write characters to screen

        LD      DE,HS_VAL3              ; 0EA1 11560F   .W.  Point to high score value 3
        CALL    WRITE_DIGITS            ; 0EA4 CDC504   ..T  Write digits to the screen

        LD      IX,HS_NAME_DATA3        ; 0EA7 DD21AE80 .!.. Point to high score name data 3
        LD      (IX+$00),TAN_CHAR_COLOR ; 0EAB DD36000A .6DO Color
        LD      (IX+$01),$09            ; 0EAF DD360109 .6.. Row 9
        LD      (IX+$02),$11            ; 0EB3 DD360211 .6.A Column 17
        LD      (IX+$0D),$FF            ; 0EB7 DD360DFF .6]. Set terminator at end of name data
        LD      DE,HS_NAME_DATA3        ; 0EBB 11AE80   ...  Point to name data set
        CALL    WRITE_CHARS             ; 0EBE CD7204   .'T  Write characters to screen

; Hi score location 4
        LD      DE,HS_NO4               ; 0EC1 113A0F   ./.  Write "NO4:" to screen
        CALL    WRITE_CHARS             ; 0EC4 CD7204   .'T  Write characters to screen

        LD      DE,HS_VAL4              ; 0EC7 115C0F   ...  Point to high score value 4
        CALL    WRITE_DIGITS            ; 0ECA CDC504   ..T  Write digits to the screen

        LD      IX,HS_NAME_DATA4        ; 0ECD DD21BC80 .!C. Point to high score name data 4
        LD      (IX+$00),TAN_CHAR_COLOR ; 0ED1 DD36000A .6DO Color
        LD      (IX+$01),$0B            ; 0ED5 DD36010B .6.. Row 11
        LD      (IX+$02),$11            ; 0ED9 DD360211 .6.A Column 17
        LD      (IX+$0D),$FF            ; 0EDD DD360DFF .6]. Set terminator at end of name data
        LD      DE,HS_NAME_DATA4        ; 0EE1 11BC80   ...  Point to name data set
        CALL    WRITE_CHARS             ; 0EE4 CD7204   .'T  Write characters to screen

; Hi score location 5
        LD      DE,HS_NO5               ; 0EE7 11420F   .C.  Write "NO5:" to screen
        CALL    WRITE_CHARS             ; 0EEA CD7204   .'T  Write characters to screen

        LD      DE,HS_VAL5              ; 0EED 11620F   .c.  Point to high score value 5
        CALL    WRITE_DIGITS            ; 0EF0 CDC504   ..T  Write digits to the screen

        LD      IX,HS_NAME_DATA5        ; 0EF3 DD21CA80 .!.. Point to high score name data 5
        LD      (IX+$00),TAN_CHAR_COLOR ; 0EF7 DD36000A .6DO Color
        LD      (IX+$01),$0D            ; 0EFB DD36010D .6.. Row 13
        LD      (IX+$02),$11            ; 0EFF DD360211 .6.A Column 17
        LD      (IX+$0D),$FF            ; 0F03 DD360DFF .6]. Set terminator at end of name data
        LD      DE,HS_NAME_DATA5        ; 0F07 11CA80   ...  Point to name data set
        CALL    WRITE_CHARS             ; 0F0A CD7204   .'T  Write characters to screen
        RET                             ; 0F0D C9       .    End SHOW_HI_SCORE_TABLE



;-------------------------------------------------------------------------------
; Data for high score table
; Range: $0F0E - $0F69
;-------------------------------------------------------------------------------

        .db     $C7, $FB                                 ; Start data block

; High score table data
HS_SCORE_NAME:
        .db     TAN_CHAR_COLOR							; Color
		.db     $03										; Row 3
		.db     $0A										; Column 10
		.db     S_EN, C_EN, O_EN, R_EN, E_EN			; "SCORE     NAME"
		.db     SP_EN, SP_EN, SP_EN, SP_EN, SP_EN
		.db     N_EN, A_EN, M_EN, E_EN
		.db     $FF										; Terminator

HS_NO1:
		.db     TAN_CHAR_COLOR							; Color
		.db     $05										; Row 5
		.db     $04										; Column 4
		.db     N_EN, O_EN, DIG1_EN, COLON_EN			; "NO1:"
		.db     $FF										; Terminator

HS_NO2:
		.db     TAN_CHAR_COLOR							; Color
		.db     $07										; Row 7
		.db     $04										; Column 4
		.db     N_EN, O_EN, DIG2_EN, COLON_EN			; "NO2:"
		.db     $FF										; Terminator

HS_NO3:
		.db     TAN_CHAR_COLOR							; Color
		.db     $09										; Row 9
		.db     $04										; Column 4
		.db     N_EN, O_EN, DIG3_EN, COLON_EN			; "NO3:"
		.db     $FF										; Terminator
		
HS_NO4:
		.db     TAN_CHAR_COLOR							; Color
		.db     $0B										; Row 11
		.db     $04										; Column 4
		.db     N_EN, O_EN, DIG4_EN, COLON_EN			; "NO4:"
		.db     $FF										; Terminator
		
HS_NO5:
		.db     TAN_CHAR_COLOR							; Color
		.db     $0D										; Row 13
		.db     $04										; Column 4
		.db     N_EN, O_EN, DIG5_EN, COLON_EN			; "NO5:"
		.db     $FF										; Terminator

; High score, value 1
HS_VAL1:
		.db     TAN_CHAR_COLOR		; Color
		.db     $05					; Row 5
		.db     $09					; Column 9
		.db     $83, $80			; Address of value: $8083
		.db     $06					; 6 digits
		
; High score, value 2
HS_VAL2:
		.db     TAN_CHAR_COLOR		; Color
		.db     $07					; Row 7
		.db     $09					; Column 9
		.db     $86, $80			; Address of value: $8086
		.db     $06					; 6 digits
		
; High score, value 3
HS_VAL3:
		.db     TAN_CHAR_COLOR		; Color
		.db     $09					; Row 9
		.db     $09					; Column 9
		.db     $89, $80			; Address of value: $8089
		.db     $06					; 6 digits
		
; High score, value 4
HS_VAL4:
		.db     TAN_CHAR_COLOR		; Color
		.db     $0B					; Row 11
		.db     $09					; Column 9
		.db     $8C, $80			; Address of value: $808C
		.db     $06					; 6 digits
		
; High score, value 5
HS_VAL5:
		.db     TAN_CHAR_COLOR		; Color
		.db     $0D					; Row 13
		.db     $09					; Column 9
		.db     $8F, $80			; Address of value: $808F
		.db     $06					; 6 digits
		
        .db     $C7, $F3								; End data block


;=============================================================================
; Name:		SHOW_NAME_REG_SCREEN
;
; Type:		Subroutine
;
; Description:	Shows the name registration information.
;
;=============================================================================
SHOW_NAME_REG_SCREEN:
        NOP				                ; 0F6A 00       .
        LD      DE,REG_NAME_REG_TEXT    ; 0F6B 11980F   ... "NAME REGISTRATION"
        CALL    WRITE_CHARS             ; 0F6E CD7204   .'T Write characters to screen

        LD      DE,REG_NAME_TEXT        ; 0F71 11AD0F   ... "NAME:"
        CALL    WRITE_CHARS             ; 0F74 CD7204   .'T Write characters to screen

        LD      DE,REG_ROW1             ; 0F77 11B60F   ... Row 1 of registration chars
        CALL    WRITE_CHARS             ; 0F7A CD7204   .'T Write characters to screen

        LD      DE,REG_ROW2             ; 0F7D 11CC0F   ... Row 2 of registration chars
        CALL    WRITE_CHARS             ; 0F80 CD7204   .'T Write characters to screen

        LD      DE,REG_ROW3             ; 0F83 11E40F   ... Row 3 of registration chars
        CALL    WRITE_CHARS             ; 0F86 CD7204   .'T Write characters to screen

; Clear the user's high score name
        LD      HL,USER_HS_NAME         ; 0F89 211181   !A. Point to user high score name
        LD      B,$0A                   ; 0F8C 060A     ..  10 characters in name

Lb199:  LD      (HL),$52                ; 0F8E 3652     6.  Write space to location
        INC     HL                      ; 0F90 23       #   Go to next HS byte
        DEC     B                       ; 0F91 05       .   
        JP      NZ,Lb199                ; 0F92 C28E0F   ..N Done? Nope, keep looping
        RET                             ; 0F95 C9       .   End SHOW_NAME_REG_SCREEN

;-------------------------------------------------------------------------------
; Data for high score name registration
; Range: $0F96 - $0FFD
;-------------------------------------------------------------------------------

        .db     $C7, $FB									; Start data block

; $0F98
REG_NAME_REG_TEXT:
        .db     TAN_CHAR_COLOR								; Color
		.db     $10											; Row 16
		.db     $06											; Column 6
		.db     N_EN, A_EN, M_EN, E_EN						; "NAME REGISTRATION"
		.db     SP_EN, R_EN, E_EN, G_EN
		.db     I_EN, S_EN, T_EN, R_EN
		.db     A_EN, T_EN, I_EN, O_EN, N_EN
        .db     $FF											; Terminator

; $FAD
REG_NAME_TEXT:
        .db     TAN_CHAR_COLOR								; Color
		.db     $12											; Row 18
		.db     $05											; Column 5
        .db     N_EN, A_EN, M_EN, E_EN, COLON_EN			; "NAME:"
        .db     $FF											; Terminator

; $FB6
REG_ROW1:
        .db     TAN_CHAR_COLOR								; Color
		.db     $14											; Row 20
        .db     $05											; Column 5
		.db     A_EN, SP_EN, B_EN, SP_EN					; "A B C D E F G H I "
		.db     C_EN, SP_EN, D_EN, SP_EN
		.db     E_EN, SP_EN, F_EN, SP_EN
		.db     G_EN, SP_EN, H_EN, SP_EN
		.db     I_EN, SP_EN
        .db     $FF											; Terminator

; $FCC
REG_ROW2:
        .db     TAN_CHAR_COLOR								; Color
		.db     $16											; Row 22
		.db     $05											; Column 5
		.db     J_EN, SP_EN, K_EN, SP_EN					; "J K L M N O P Q R <Rub>"
		.db     L_EN, SP_EN, M_EN, SP_EN					; Note: <Rub> is made up of two characters
		.db     N_EN, SP_EN, O_EN, SP_EN					; that spell Rub
		.db     P_EN, SP_EN, Q_EN, SP_EN
		.db     R_EN, SP_EN, RUBL_EN, RUBR_EN
        .db     $FF											; Terminator

; $FE4
REG_ROW3:
        .db     TAN_CHAR_COLOR								; Color
		.db     $18											; Row 24
		.db     $05											; Column 5
		.db     S_EN, SP_EN, T_EN, SP_EN					; "S T U V W X Y Z . <End>"
		.db     U_EN, SP_EN, V_EN, SP_EN					; Note: <End> is made up of two characters
		.db     W_EN, SP_EN, X_EN, SP_EN					; that spell End
		.db     Y_EN, SP_EN, Z_EN, SP_EN
		.db     PERIOD_EN, SP_EN, ENDL_EN, ENDR_EN
        .db     $FF											; Terminator

        .db     $C7, $F3									; End data block



;=============================================================================
; Title screen initialization
;=============================================================================
        NOP                             ; 0FFE 00
        NOP                             ; 0FFF 00
DISPLAY_TITLE_SCREEN1:
        LD      IX,STARTUP_TXT_PTR_TBL  ; 1000 DD215808 .!ML Point to startup text pointer table
        LD      A,$80                   ; 1004 3E80     >.   Initialize column position to $80 (middle)
        LD      ($8131),A               ; 1006 323181   2a.  Note: $8131 is used differently later in code...
        JP      DISPLAY_TITLE_SCREEN2   ; 1009 C30708   .FL



;=============================================================================
; Title screen -- scrolling
;=============================================================================
        NOP                             ; 100C 00       .
        NOP                             ; 100D 00       .
        NOP                             ; 100E 00       .
        NOP                             ; 100F 00       .
DISPLAY_TITLE_SCREEN3:
        LD      HL,COLUMN_SCROLL        ; 1010 210098   !D.  HL points to column smooth scroll memory
; Note: $8131 is used differently later in the code...
        LD      A,($8131)               ; 1013 3A3181   :a.  Get current scroll position
        INC     A                       ; 1016 3C       <    Scroll one line
        LD      ($8131),A               ; 1017 323181   2a.  Store new scroll position
        JP      DISPLAY_TITLE_SCREEN4   ; 101A C32D08   .}L


        NOP                             ; 101D 00       .
        NOP                             ; 101E 00       .
        NOP                             ; 101F 00       .

;=============================================================================
; Called from $02B7
; (Index 0 in the jump table)
;
; Address $1020
;=============================================================================
ISR_JUMP0:
        NOP                             ; 1020 00       .
        CALL    Lb207                   ; 1021 CD2710   .f.
        CALL    Lb208                   ; 1024 CD0F03   ...  Does not return from this call

;=============================================================================
;
; See if the UNKNOWN_815C table needs some entries cleared
; for (i= 0; i < 32; i+= 8)
; {
;	if( UNKNOWN_815C[i+0] == 0 || UNKNOWN_815C[i+3] == 7 )
;	{
;		for (j = 0; j < 8; j++ ) UNKNOWN_815C[i+j] = 0;
;	}
; } 
;
; Copy UNKNOWN_815C into SPRITE_CTRL (4 items)
; for (i= 0; i < 32; i+= 8)
; {
;	if( UNKNOWN_815C[i+0] != $F0 )
;	{
;		for (j = 0; j < 4; j++ ) 
;			SPRITE_CTRL[j] = UNKNOWN_815C[i+j+1];
;	}
; }
;
; See if UNKNOWN_8283 needs entries cleared
; for (i= 0; i < 32; i+= 8)
; {
;	if( UNKNOWN_815C[i+0] == 0 && UNKNOWN_8283[6] != 1 )
;	{
;		for (j = 0; j < 8; j++ ) 
;			UNKNOWN_8283[i+j] = 0;
;	}
; }    
;=============================================================================
Lb207:  LD      IX,UNKNOWN_815C         ; 1027 DD215C81 .!..	Start of table
        LD      DE,$08                  ; 102B 110800   .LD		Item byte length
        LD      H,$04                   ; 102E 2604     &.		4 items in table

Lb213:  LD      A,(IX+$00)              ; 1030 DD7E00   .~D		A = UNKNOWN_815C[i]
        CP      $00                     ; 1033 FE00     .D		Is A zero?
        JR      Z,Lb209                 ; 1035 2807     (F		Yes, goto here (clear 8 bytes)

        LD      A,(IX+$03)              ; 1037 DD7E03   .~S		A = UNKNOWN_815C[i+3]
        CP      $07                     ; 103A FE07     ..		Is A != 7?
        JR      NZ,Lb210                ; 103C 300D     0]		Yes, goto here

; Clear the next 8 bytes pointed to by IX
Lb209:  LD      L,$08                   ; 103E 2E08     .L		# bytes in each item

Lb211:  LD      (IX+$00),$00            ; 1040 DD360000 .6DD	UNKNOWN_815C[i+j] = 0
        INC     IX                      ; 1044 DD23     .#		j++
        DEC     L                       ; 1046 2D       -		L--
        JR      NZ,Lb211                ; 1047 20F7      .		Is L != 0? Yes, go here
        JR      Lb212                   ; 1049 1802     .G		Go here

Lb210:  ADD     IX,DE                   ; 104B DD19     ..		Go to the next item in the table (i+=8)

Lb212:  DEC     H                       ; 104D 25       %		Decrement # items in table variable
        JR      NZ,Lb213                ; 104E 20E0      .		Done? No, loop here

        LD      IX,UNKNOWN_815C         ; 1050 DD215C81 .!..	IX = Start of table


; Copy over UNKNOWN_815C items to SPRITE_CTRL (4 sprites). 
; Only copy if UNKNOWN_815C[0] != $F0 for each item
Lb264:  LD      IY,SPRITE_CTRL          ; 1054 FD218098 .!..	Point IY to sprite control
        LD      DE,$08                  ; 1058 110800   .LD
        LD      BC,$04                  ; 105B 010400   .TD
        LD      H,$04                   ; 105E 2604     &.		4 sprites to set up

Lb217:  LD      A,(IX+$00)              ; 1060 DD7E00   .~D		A = UNKNOWN_815C[0]
        CP      $F0                     ; 1063 FEF0     ..		Is A = $F0?
        JR      Z,Lb214                 ; 1065 2819     (I		Yes, go here (do not copy sprite item)


; Copy 4 bytes from UNKNOWN_815C[1] -> SPRITE_CTRL[0]
        LD      L,$04                   ; 1067 2E04     .T		# bytes to copy
        INC     IX                      ; 1069 DD23     .#		IX = &UNKNOWN_815C[1]

Lb215:  LD      A,(IX+$00)              ; 106B DD7E00   .~D		A = *IX
        LD      (IY+$00),A              ; 106E FD7700   .wD		SPRITE_CTRL[i] = A
        INC     IX                      ; 1071 DD23     .#		
        INC     IY                      ; 1073 FD23     .#		Go to next byte
        DEC     L                       ; 1075 2D       -		Decrement # bytes to copy
        JR      NZ,Lb215                ; 1076 20F3      .		Keep looping until copied

        INC     IX                      ; 1078 DD23     .#		Point to next UNKNOWN_815C item
        INC     IX                      ; 107A DD23     .#
        INC     IX                      ; 107C DD23     .#
        JR      Lb216                   ; 107E 1804     ..

Lb214:  ADD     IX,DE                   ; 1080 DD19     ..		Go to next UNKNOWN_815C item
        ADD     IY,BC                   ; 1082 FD09     ..		Go to next SPRITE_CTRL item

Lb216:  DEC     H                       ; 1084 25       %		Go to the next sprite
        JR      NZ,Lb217                ; 1085 20D9      .		Done? Nope, go here


; If UNKNOWN_815C[0] == 0 and UNKNOWN_8283[6] != 1, clear UNKNOWN_8283 item.
; Do this for the four items
        LD      IX,UNKNOWN_815C         ; 1087 DD215C81 .!..
        LD      IY,UNKNOWN_8283         ; 108B FD218382 .!|.
        LD      B,$04                   ; 108F 0604     .T		B = 4 items to process

Lb221:  LD      A,(IX+$00)              ; 1091 DD7E00   .~D		
        AND     A                       ; 1094 A7       .		is UNKNOWN_815C[0] != 0?
        JR      NZ,Lb218                ; 1095 2014      .		Yes, go here (skip processing this item)

        LD      A,(IY+$06)              ; 1097 FD7E06   .~G		
        CP      $01                     ; 109A FE01     ..		is UNKNOWN_8283[6] = 1?
        JR      Z,Lb218                 ; 109C 280D     (]		Yes, go here (skip processing this item)


; Clear the next 8 bytes of UNKNOWN_8283
        LD      C,$08                   ; 109E 0E08     .L		C = 8
        XOR     A                       ; 10A0 AF       .		Clear A

Lb219:  LD      (IY+$00),A              ; 10A1 FD7700   .wD		UNKNOWN_8283[j] = 0
        INC     IY                      ; 10A4 FD23     .#		j++
        DEC     C                       ; 10A6 0D       .		C--
        JR      NZ,Lb219                ; 10A7 20F8      .		Is C!= 0? Yes, go here

        JR      Lb220                   ; 10A9 1802     .G		Go here

Lb218:  ADD     IY,DE                   ; 10AB FD19     ..		Go to next UNKNOWN_8283 item

Lb220:  ADD     IX,DE                   ; 10AD DD19     ..		Go to next UNKNOWN_815C item
        DEC     B                       ; 10AF 05       .		B--
        JR      NZ,Lb221                ; 10B0 20DF      .		Is B != 0? Yes, go here
        RET                             ; 10B2 C9       .		Finished with subroutine


;=============================================================================
; Go to next building
;=============================================================================
GOTO_NEXT_BLDG:
        LD      A,$01                   ; 10B3 3E01     >.
        LD      (KEEP_SAME_ISR_FLAG),A  ; 10B5 324480   2@. Keep processing the same ISR table location

; Wait for song to end?
Lb222:  LD      HL,(SNDA_DATA_PTR)      ; 10B8 2A0080   *D. Get channel A sound data pointer
        LD      A,(HL)                  ; 10BB 7E       ~   Read value
        CP      $FF                     ; 10BC FEFF     ..  Is sound data = $FF?
        JR      NZ,Lb222                ; 10BE 20F8      .  No, keep looking

; Go to next building
        LD      A,(BUILDING_NUMBER)     ; 10C0 3ADF80   :..
        ADD     A,$01                   ; 10C3 C601     ..
        AND     $03                     ; 10C5 E603     ..  Limit range from 0 - 3
        LD      (BUILDING_NUMBER),A     ; 10C7 32DF80   2..

        CALL    Lb96                    ; 10CA CD6205   .3.
        XOR     A                       ; 10CD AF       .
        LD      (FLOOR_GROUP_IDX),A     ; 10CE 32DC80   2.. Start at the beginning floor group of the building
        LD      (FLOOR_IDX),A           ; 10D1 32DD80   2". Start at the 1st floor in the floor group
        LD      HL,$00                  ; 10D4 210000   !DD
        LD      (CUR_FLOOR_NUM),HL      ; 10D7 22E880   ".. Zero the current floor number and group (two values)
        LD      A,$01                   ; 10DA 3E01     >.
        CALL    Lb223                   ; 10DC CD6503   .p.

        LD      A,$FF                   ; 10DF 3EFF     >.
        CALL    DELAY                   ; 10E1 CDB802   ... Delay

        LD      A,$00                   ; 10E4 3E00     >D
        LD      (KEEP_SAME_ISR_FLAG),A  ; 10E6 324480   2.. Process the next ISR table location
        RET                             ; 10E9 C9       .   End GOTO_NEXT_BLDG



;=============================================================================
; Called when the player has died
;=============================================================================
PLAYER_DIED:
        LD      A,$01                   ; 10EA 3E01     >.
        LD      (KEEP_SAME_ISR_FLAG),A  ; 10EC 324480   2.. Keep processing the same ISR table location

        LD      A,$FF                   ; 10EF 3EFF     >.
        CALL    DELAY                   ; 10F1 CDB802   ... Delay

        CALL    Lb96                    ; 10F4 CD6205   .3.
        XOR     A                       ; 10F7 AF       .
        LD      (FLOOR_GROUP_IDX),A     ; 10F8 32DC80   2.. Start of the beginning of the building floor groups
        LD      (FLOOR_IDX),A           ; 10FB 32DD80   2". Start at the 1st floor in the floor group
        LD      A,$01                   ; 10FE 3E01     >.  
        LD      (PLAYER_DIED_FLAG),A    ; 1100 327380   2.. Set player died flag

        LD      A,$80                   ; 1103 3E80     >.
        CALL    DELAY                   ; 1105 CDB802   ... Delay

        RET                             ; 1108 C9       .   End PLAYER_DIED

;=============================================================================
;=============================================================================
Lb577:  LD      A,(BONUS_RATE3)         ; 1109 3AE680   :..
        LD      C,A                     ; 110C 4F       O
        LD      A,(BONUS_RATE2)         ; 110D 3AE580   :..
        LD      B,A                     ; 1110 47       G
        LD      A,(BONUS_RATE1)         ; 1111 3AE480   :..
        OR      B                       ; 1114 B0       .
        OR      C                       ; 1115 B1       .
        RET     Z                       ; 1116 C8       .

; Load BC with bonus rate decrement value
        LD      A,(DEC_BONUS_RATE2)     ; 1117 3AE380   :..
        LD      C,A                     ; 111A 4F       O
        LD      A,(DEC_BONUS_RATE1)     ; 111B 3AE280   :..
        LD      B,A                     ; 111E 47       G
        PUSH    BC                      ; 111F C5       .    Store BC
        CALL    Lb224                   ; 1120 CDA527   ..f
        CALL    SHOW_CURRENT_SCORE      ; 1123 CDDD27   .""  Show the current scores on screen
        POP     BC                      ; 1126 C1       .    Restore BC
        CALL    DECREMENT_BONUS_RATE    ; 1127 CD5D11   ..A  Decrement bonus rate
        LD      A,$01                   ; 112A 3E01     >.
        RET                             ; 112C C9       .


;=============================================================================
; Initialize the bonus rate to 3,000 and show it
;=============================================================================
BONUS_RATE_3000:
        LD      HL,$30                  ; 112D 213000   !1D	Set the bonus rate to 3,000
        LD      (BONUS_RATE2),HL        ; 1130 22E580   "..
        XOR     A                       ; 1133 AF       .
        LD      (BONUS_RATE1),A         ; 1134 32E480   2..
        LD      DE,BONUS_RATE_VALUE     ; 1137 115F1F   .._	 Point to the bonus rate data
        CALL    WRITE_DIGITS            ; 113A CDC504   ..T  Write digits to the screen
        RET                             ; 113D C9       .	 End BONUS_RATE_3000

;=============================================================================
; Update the bonus rate. This will only decrement if the bonus rate is > 3000.
;=============================================================================
UPDATE_BONUS_RATE:
        LD      A,(BONUS_RATE1)         ; 113E 3AE480   :..
        OR      A                       ; 1141 B7       .
        JR      NZ,Lb227                ; 1142 200D      ]	Is BONUS_RATE1 != 0? Yes, go here

        LD      A,(BONUS_RATE3)         ; 1144 3AE680   :..
        LD      L,A                     ; 1147 6F       o
        LD      A,(BONUS_RATE2)         ; 1148 3AE580   :..
        LD      H,A                     ; 114B 67       g	HL = BONUS_RATE2 BONUS_RATE1
        LD      DE,$CFF0                ; 114C 11F0CF   ...	This limits the bonus rate to
        ADD     HL,DE                   ; 114F 19       .	3000. If this would be less than
        RET     NC                      ; 1150 D0       .	3000, nothing else is decremented

; Load BC with bonus rate decrement value
Lb227:  LD      A,(DEC_BONUS_RATE2)     ; 1151 3AE380   :..	Decrement the bonus rate
        LD      C,A                     ; 1154 4F       O
        LD      A,(DEC_BONUS_RATE1)     ; 1155 3AE280   :..
        LD      B,A                     ; 1158 47       G
        CALL    DECREMENT_BONUS_RATE    ; 1159 CD5D11   ..A	Decrement the bonus rate
        RET                             ; 115C C9       .	End UPDATE_BONUS_RATE


;=============================================================================
; Decrement bonus rate (due to time)
;
; The bonus rate is in BCD and has the following digits
;
; BONUS_RATE1 BONUS_RATE2 BONUS_RATE3
; (1 digit)   (2 digits)  (2 digits)
; 
; Input:
;	BC - The decimal adjusted value to subtract from the current bonus rate.
;=============================================================================
DECREMENT_BONUS_RATE:
        LD      A,(GAME_IN_PROGRESS)    ; 115D 3A7580   :5. Is a game in progress?
        AND     A                       ; 1160 A7       .
        RET     Z                       ; 1161 C8       .   No, end DECREMENT_BONUS_RATE

; Game in progress

; Subtract least significant digits
        LD      A,(BONUS_RATE3)         ; 1162 3AE680   :..	Subtract C from BONUS_RATE3
        SUB     C                       ; 1165 91       .
        DAA                             ; 1166 27       '
        LD      (BONUS_RATE3),A         ; 1167 32E680   2..

; Subtract next significant digits
        LD      A,(BONUS_RATE2)         ; 116A 3AE580   :.. Subtract the carry from BONUS_RATE2
        SBC     A,B                     ; 116D 98       .
        DAA                             ; 116E 27       '
        LD      (BONUS_RATE2),A         ; 116F 32E580   2..	

; Subtract most significant digits
        LD      A,(BONUS_RATE1)         ; 1172 3AE480   :..	Subtract the carry from BONUS_RATE1
        LD      B,$00                   ; 1175 0600     .D
        SBC     A,B                     ; 1177 98       .
        DAA                             ; 1178 27       '
        LD      (BONUS_RATE1),A         ; 1179 32E480   2..

        LD      DE,BONUS_RATE_VALUE     ; 117C 115F1F   ... Point to the bonus rate data
        CALL    WRITE_DIGITS            ; 117F CDC504   .:. Write digits to the screen
        RET                             ; 1182 C9       .	End DECREMENT_BONUS_RATE


;=============================================================================
; Checks to see if the field should be inverted
;
; Output:
;	A = 0 -- Cocktail machine and current player is player 2
;	A = 1 -- Upright machine 
;	             - or -
;	         Cocktail machine and current player is player 1
;=============================================================================
CHECK_FIELD_INVERSION:
        LD      A,(MACH_VER)            ; 1183 3A7C80   :). Get the machine version
        AND     A                       ; 1186 A7       .   Check the value
        JR      NZ,Lb228                ; 1187 2008      L  If Upright (1), go here

; Cocktail machine
        LD      A,(CURRENT_PLAYER)      ; 1189 3A8180   :.. Check current player
        AND     A                       ; 118C A7       .
        JR      Z,Lb228                 ; 118D 2802     (G  Player 1, go here

; Player 2 is current player & it is a cocktail machine
        XOR     A                       ; 118F AF       .   Clear A
        RET                             ; 1190 C9       .   End CHECK_FIELD_INVERSION

; Player 1 is current player or it is an upright machine
Lb228:  LD      A,$01                   ; 1191 3E01     >.  A = 1
        RET                             ; 1193 C9       .   End CHECK_FIELD_INVERSION



;=============================================================================
; Initializes the ISR_JUMP3 counters using the following table.
; Loads ISR_JUMP3_CNTR1 and ISR_JUMP3_CNTR2 with the values in the following
; table.  The table index is the current building number.
;=============================================================================
INIT_ISR_JUMP3_COUNTERS:
        LD      A,(BUILDING_NUMBER)     ; 1194 3ADF80   :.. Get the building number
        RLCA                            ; 1197 07       .   Multiply by 2
        LD      E,A                     ; 1198 5F       _
        LD      D,$00                   ; 1199 1600     .D	DE = $00, BUILDING_NUMBER*2
        LD      HL,$11A9                ; 119B 21A911   !.A
        ADD     HL,DE                   ; 119E 19       .   HL = $11A9 + (2 * BldgNumber)
        LD      E,(HL)                  ; 119F 5E       ^
        INC     HL                      ; 11A0 23       #
        LD      D,(HL)                  ; 11A1 56       V
        EX      DE,HL                   ; 11A2 EB       .
        LD      (ISR_JUMP3_CNTR1),HL    ; 11A3 222081   "d. Save value to both counters
        RET                             ; 11A6 C9       .	End INIT_ISR_JUMP3_COUNTERS

;-------------------------------------------------------------------------------
; Data Start
; Range: $11A7 - $11BA
;-------------------------------------------------------------------------------

        .db     $C7, $FB								; Start data block

; $11A9
;							Building #	Value for ISR_JUMP3 counters
;							----------	-------------------------
        .db     $00, $20	; 1			$2000
		.db     $00, $28	; 2			$2800
		.db     $00, $30	; 3			$3000
		.db     $00, $38	; 4			$3800
        .db     $00, $40	; 5			$4000
		.db     $00, $48	; 6			$4800
		.db     $00, $50	; 7			$5000
		.db     $00, $58	; 8			$5800

        .db     $C7, $F3								; End data block

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------


;=============================================================================
; Loads data to initiate a sound sequence
;
; Input:
;	B - Type of sound sequence
;	    1 - Uses sound channels B & C
;	    2 - Uses sound channesl A & B
;	    3 - Uses the sound sample data path
;	    4 - Uses sound channels A, B, C and the sample data path
;	C - Index into the respective sound init table
;=============================================================================
LOAD_SOUND_DATA:
        LD      A,(GAME_IN_PROGRESS)    ; 11BB 3A7580   :5. Is a game in progress?
        AND     A                       ; 11BE A7       .
        RET     Z                       ; 11BF C8       .   Nope, return

; Game in progress
        PUSH    IX                      ; 11C0 DDE5     ..  Save registers used
        PUSH    HL                      ; 11C2 E5       .

; Check the value of B
        LD      A,B                     ; 11C3 78       x
        LD      B,$00                   ; 11C4 0600     .D  Clear B
        CP      $04                     ; 11C6 FE04     ..  Is B = 4?
        JR      Z,Lb229                 ; 11C8 287A     (/  Yes, go here

        CP      $03                     ; 11CA FE03     .S  Is B = 3
        JR      Z,Lb230                 ; 11CC 285B     (.  Yes, go here

        CP      $02                     ; 11CE FE02     ..  Is B = 2?
        JR      Z,Lb231                 ; 11D0 282C     (=  Yes, go here


;-----------------------------------------------------------------------------
; B = 1
; C contains the index (0 or 1)
;
; Source address = SOUND_TABLE1 + (8*C)
;
; Destination Base $8000
;
; Dest. Offset	Source Offset	Purpose
; ------------	-------------	-------	
; C				1				Channel B sound data pointer
; D				0				
;
; F				2				Initial count flag B
;
; 18			5				Channel C sound data pointer
; 19			4
;
; 1B			6				Initial count flag C
;-----------------------------------------------------------------------------
        LD      A,C                     ; 11D2 79       y    Get index
        RLCA                            ; 11D3 07       .    Multiply by 8 (8 values per table entry)
        RLCA                            ; 11D4 07       .
        RLCA                            ; 11D5 07       .
        LD      C,A                     ; 11D6 4F       O
        LD      IX,SOUND_TABLE1         ; 11D7 DD216E13 .!zR Base address for sound table 1
        ADD     IX,BC                   ; 11DB DD09     ..   IX = SOUND_TABLE1 + (8 * index)

        LD      H,(IX+$00)              ; 11DD DD6600   .fD
        LD      L,(IX+$01)              ; 11E0 DD6E01   .n.
        LD      (SNDB_DATA_PTR),HL      ; 11E3 220C80   "\.  Channel B data pointer

        LD      A,(IX+$02)              ; 11E6 DD7E02   .~G
        LD      (SNDB_INIT_CNT),A       ; 11E9 320F80   2N.  Channel B initial count

        LD      H,(IX+$04)              ; 11EC DD6604   .fT
        LD      L,(IX+$05)              ; 11EF DD6E05   .nU
        LD      (SNDC_DATA_PTR),HL      ; 11F2 221880   "..  Channel C data pointer

        LD      A,(IX+$06)              ; 11F5 DD7E06   .~G 
        LD      (SNDC_INIT_CNT),A       ; 11F8 321B80   2..  Channel C initial count

        JP      Lb232                   ; 11FB C38C12   ..F  Finish routine

;-----------------------------------------------------------------------------
; B = 2 on entry of routine
; C contains the index
;
; Source address = SOUND_TABLE2 + (8*C)
; Destination Base $8000
;
; Dest. Offset	Source Offset	Purpose
; ------------	-------------	-------	
; 0				1				Sound channel A data pointer
; 1				0				
;
; 3				2				Initial count flag A
;
; C				5				Sound channel B data pointer
; D				4
;
; F				6				Initial count flag B
;-----------------------------------------------------------------------------
Lb231:
        LD      A,C                     ; 11FE 79       y    Get value of C (index)
        RLCA                            ; 11FF 07       .    Multiply by 8 (8 bytes per table entry)
        RLCA                            ; 1200 07       .
        RLCA                            ; 1201 07       .
        LD      C,A                     ; 1202 4F       O
        LD      IX,SOUND_TABLE2         ; 1203 DD219212 .!.. Base address for sound table 2
        ADD     IX,BC                   ; 1207 DD09     ..   IX = SOUND_TABLE2 + (8 * index)

        LD      H,(IX+$00)              ; 1209 DD6600   .fD
        LD      L,(IX+$01)              ; 120C DD6E01   .n.
        LD      (RAM_START),HL          ; 120F 220080   "D.

        LD      A,(IX+$02)              ; 1212 DD7E02   .~G
        LD      (SNDA_INIT_CNT),A       ; 1215 320380   2..  Channel A initial count

        LD      H,(IX+$04)              ; 1218 DD6604   .fT
        LD      L,(IX+$05)              ; 121B DD6E05   .nU
        LD      (SNDB_DATA_PTR),HL      ; 121E 220C80   "..  Channel B data pointer

        LD      A,(IX+$06)              ; 1221 DD7E06   .~G
        LD      (SNDB_INIT_CNT),A       ; 1224 320F80   2..  Channel B initial count
        JR      Lb232                   ; 1227 1863     .6   Finish routine


;-----------------------------------------------------------------------------
; B = 3
; C = Index
;
; Source address = SOUND_TABLE3 + (4*C)
; Destination Base $8000
;
; Dest. Offset	Source Offset	Purpose
; ------------	-------------	-------	
; 24			1				Sample data pointer
; 25			0
;
; 27			2				Initial count flag samples
;-----------------------------------------------------------------------------
Lb230:  LD      A,C                     ; 1229 79       y   Get index
        RLCA                            ; 122A 07       .   Multiply by 4 (4 bytes per table entry)
        RLCA                            ; 122B 07       .
        LD      C,A                     ; 122C 4F       O

        LD      IX,SOUND_TABLE3         ; 122D DD21AA12 .!U. Base address
        ADD     IX,BC                   ; 1231 DD09     ..   IX = SOUND_TABLE3 + (2 * index)

        LD      H,(IX+$00)              ; 1233 DD6600   .fD
        LD      L,(IX+$01)              ; 1236 DD6E01   .n.
        LD      (SNDS_DATA_PTR),HL      ; 1239 222480   "t.  Set the sample data pointer

        LD      A,(IX+$02)              ; 123C DD7E02   .~G
        LD      (SNDS_INIT_CNT),A       ; 123F 322780   2f.  Set the sample initial counter

        JR      Lb232                   ; 1242 1848     ..   Finish routine

;-----------------------------------------------------------------------------
; B = 4
; C = Index
;
; Source address = SOUND_TABLE4 + (16*C)
; Destination Base $8000
;
; Dest. Offset	Source Offset	Purpose
; ------------	-------------	-------	
; 0				1				Sound channel A data pointer
; 1				0
;
; 3				2				Initial count flag A
;
; C				5				Sound channel B data pointer
; D				4
;
; F				6				Initial count flag B
;
; 18			9				Sound channel C data pointer
; 19			8
;
; 1B			A				Initial count flag C
;
; 24			D				Sample data pointer
; 25			C
;
; 27			E				Initial count flag samples
;-----------------------------------------------------------------------------
Lb229:  LD      A,C                     ; 1244 79       y    Get index value
        RLCA                            ; 1245 07       .    Multiply by 16 (16 bytes per table entry)
        RLCA                            ; 1246 07       .
        RLCA                            ; 1247 07       .
        RLCA                            ; 1248 07       .
        LD      C,A                     ; 1249 4F       O
        LD      IX,SOUND_TABLE4         ; 124A DD21CE12 .!.F Base address
        ADD     IX,BC                   ; 124E DD09     ..   IX = SOUND_TABLE4 + (16 * index)

        LD      H,(IX+$00)              ; 1250 DD6600   .fD
        LD      L,(IX+$01)              ; 1253 DD6E01   .n.
        LD      (RAM_START),HL          ; 1256 220080   "D.

        LD      A,(IX+$02)              ; 1259 DD7E02   .~.
        LD      (SNDA_INIT_CNT),A       ; 125C 320380   2S. Channel A initial count

        LD      H,(IX+$04)              ; 125F DD6604   .f.
        LD      L,(IX+$05)              ; 1262 DD6E05   .n.
        LD      (SNDB_DATA_PTR),HL      ; 1265 220C80   "\. Channel B data pointer

        LD      A,(IX+$06)              ; 1268 DD7E06   .~.
        LD      (SNDB_INIT_CNT),A       ; 126B 320F80   2N. Channel B initial count

        LD      H,(IX+$08)              ; 126E DD6608   .fL
        LD      L,(IX+$09)              ; 1271 DD6E09   .n.
        LD      (SNDC_DATA_PTR),HL      ; 1274 221880   ".. Channel C data pointer

        LD      A,(IX+$0A)              ; 1277 DD7E0A   .~.
        LD      (SNDC_INIT_CNT),A       ; 127A 321B80   2.. Channel C initial count

        LD      H,(IX+$0C)              ; 127D DD660C   .f.
        LD      L,(IX+$0D)              ; 1280 DD6E0D   .n.
        LD      (SNDS_DATA_PTR),HL      ; 1283 222480   "t. Set the sample sound data pointer

        LD      A,(IX+$0E)              ; 1286 DD7E0E   .~.
        LD      (SNDS_INIT_CNT),A       ; 1289 322780   2f. Set the sample initial count

Lb232:  POP     HL                      ; 128C E1       .   Restore registers used
        POP     IX                      ; 128D DDE1     ..
        RET                             ; 128F C9       .   End LOAD_SOUND_DATA

;-------------------------------------------------------------------------------
; Data for sound data initialization
; Range: $1290 - $137F
;-------------------------------------------------------------------------------

        .db     $C7, $FB								; Start data block

;-----------------------
; B = 2, C = index
; $1292
;               Ch A                Ch B
;               Data Ptr  Cnt       Data Ptr  Cnt
;               --------  ---       --------  ---
SOUND_TABLE2:
        .db     $4B, $10, $81, $00, $4B, $10, $81, $00	; Index 0 - Helicopter Hovering
        .db     $4D, $20, $90, $00, $4D, $50, $90, $00	; Index 1 - Balloon Music
        .db     $46, $E0, $82, $00, $46, $E0, $82, $00	; Index 2 - Electric sign Music

;-----------------------
; B = 3, C = index
; $12AA (4 values)
;               Sample
;               Data Ptr  Cnt
;               --------  ---
SOUND_TABLE3:
        .db     $48, $A0, $81, $00		; Index 0 - Climb up a floor sound 1
		.db     $48, $C0, $81, $00		; Index 1 - Climb up a floor sound 2
        .db     $48, $E0, $81, $00		; Index 2 - Hit by a pot
		.db     $4D, $10, $84, $00		; Index 3 - Hit by dumbell/girder
        .db     $4A, $20, $81, $00		; Index 4 - Bird poop sound
		.db     $4A, $F4, $81, $00		; Index 5 - King kong chirp sound
        .db     $4E, $80, $80, $00		; Index 6 - Electric sign sparking sound
		.db     $4E, $90, $80, $00		; Index 7 - Electric sign shocking player sound
        .db     $00, $00, $00, $00		; Index 8 - Not used


;-----------------------
; B = 4, C = index
; $12CE (16 values)
;               Ch A                Ch B
;               Data Ptr  Cnt       Data Ptr  Cnt
;               --------  ---       --------  ---
; (next row)
;               Ch C                Sample
;               Data Ptr  Cnt       Data Ptr  Cnt
;               --------  ---       --------  ---
SOUND_TABLE4:
		.db     $48, $00, $82, $00, $48, $40, $82, $00	; Index 0 Start building music
		.db     $48, $60, $82, $00, $48, $80, $82, $00

		.db     $4A, $40, $84, $00, $4A, $80, $84, $00	; Index 1 King Kong music
		.db     $4A, $C0, $84, $00, $4A, $F4, $84, $00

		.db     $4B, $30, $82, $00, $4B, $80, $82, $00	; Index 2 End of building 1
		.db     $4B, $C0, $82, $00, $4B, $E0, $82, $00

		.db     $4C, $00, $83, $00, $4C, $38, $83, $00	; Index 3 End of building 2
		.db     $4C, $68, $83, $00, $4C, $90, $83, $00

		.db     $4E, $A0, $87, $00, $4E, $E8, $87, $00	; Index 4 End of building 3
		.db     $4F, $48, $87, $00, $4F, $A8, $87, $00
		
		.db     $45, $00, $80, $00, $45, $80, $80, $00	; Index 5 End of building 4
		.db     $45, $E0, $80, $00, $46, $10, $80, $00
		
		.db     $49, $00, $86, $00, $49, $50, $86, $00	; Index 6 Bird Music
		.db     $49, $A0, $86, $00, $4A, $00, $86, $00
		
		.db     $4C, $A0, $84, $00, $4C, $C0, $84, $00	; Index 7 Player falling
		.db     $4C, $E0, $84, $00, $4D, $00, $84, $00
		
		.db     $4D, $70, $82, $00, $4D, $E0, $82, $00	; Index 8 Caught Balloon
		.db     $4E, $38, $82, $00, $4F, $A8, $82, $00
		
		.db     $4F, $B8, $80, $00, $4F, $C0, $80, $00	; Index 9 Falling Sign
		.db     $4F, $C8, $80, $00, $4F, $D0, $80, $00



;-----------------------------------
; B = 1,  C = index
; $136E (8 values)
;               Ch B                Ch C
;               Data Ptr  Cnt       Data Ptr  Cnt
;               --------  ---       --------  ---
SOUND_TABLE1:
		.db     $4F, $E0, $80, $00, $4F, $F0, $80, $00	; Index 0 - Add a life
		.db     $46, $40, $83, $00, $46, $90, $83, $00	; Index 1 - Falling dumbell/girder

        .db     $C7, $F3								; End data block




        NOP                             ; 1380 00       .
        NOP                             ; 1381 00       .
        NOP                             ; 1382 00       .
        NOP                             ; 1383 00       .
        NOP                             ; 1384 00       .
        NOP                             ; 1385 00       .
        NOP                             ; 1386 00       .
        NOP                             ; 1387 00       .
        NOP                             ; 1388 00       .
        NOP                             ; 1389 00       .
        NOP                             ; 138A 00       .
        NOP                             ; 138B 00       .
        NOP                             ; 138C 00       .
        NOP                             ; 138D 00       .
        NOP                             ; 138E 00       .
        NOP                             ; 138F 00       .

;=============================================================================
; Called from $02B7
; (Index 1 in the jump table)
;
; Address $1390
;=============================================================================
ISR_JUMP1:
        NOP                             ; 1390 00       .
        LD      A,(ISR_MODE_IDX)        ; 1391 3A5B81   :^.	Get ISR mode index
        CP      $00                     ; 1394 FE00     .D
        CALL    Z,Lb208                 ; 1396 CC0F03   ...  Does not return from this call

        CP      $01                     ; 1399 FE01     ..
        CALL    Z,START_BUILDING	    ; 139B CC2514   .0@	Start a building

        CP      $02                     ; 139E FE02     ..
        CALL    NZ,Lb208                ; 13A0 C40F03   ...  Does not return from this call

        LD      A,($814C)               ; 13A3 3A4C81   :H.
        CP      $00                     ; 13A6 FE00     .D
        CALL    NZ,Lb208                ; 13A8 C40F03   ...  Does not return from this call

        CALL    SHOW_CLIMBER            ; 13AB CD4415   .@Q  Show climber on screen

        LD      A,($8281)               ; 13AE 3A8182   :..
        CP      $FF                     ; 13B1 FEFF     ..
        JR      Z,Lb244                 ; 13B3 2818     (.

        CALL    CHECK_ALLOWED_HAND_MOVES ; 13B5 CD771A   ."N

        LD      A,($8282)               ; 13B8 3A8282   :}.
        AND     A                       ; 13BB A7       .
        JR      NZ,Lb246                ; 13BC 2009      .

        CALL    Lb247                   ; 13BE CD5215   ..P

        CALL    Lb248                   ; 13C1 CD2D16   .8.

        CALL    Lb208                   ; 13C4 CD0F03   ... Does not return from this call

Lb246:  CALL    Lb249                   ; 13C7 CD2E18   .;.

        CALL    Lb208                   ; 13CA CD0F03   ... Does not return from this call

Lb244:  LD      A,$FB                   ; 13CD 3EFB     >.
        CALL    MOVE_CLIMBER_Y          ; 13CF CDD118   ... Move climber down -5

        LD      A,(GAME_IN_PROGRESS)    ; 13D2 3A7580   :%. Get the game in progress flag
        PUSH    AF                      ; 13D5 F5       .   Save this original value
        AND     A                       ; 13D6 A7       .   Check value
        LD      (GAME_IN_PROGRESS),A    ; 13D7 327580   25. Store the game in progress flag
        CALL    Lb247                   ; 13DA CD5215   ..P

        POP     AF                      ; 13DD F1       .   Restore the original game in progress flag
        LD      (GAME_IN_PROGRESS),A    ; 13DE 327580   2%. Save it
        CALL    ANIMATE_CLIMBER         ; 13E1 CDF018   ... Animate the climber

        LD      A,($8134)               ; 13E4 3A3481   :`. Climbers left leg sprite Y position
        CP      $F0                     ; 13E7 FEF0     ..  Compare with 240
; Call routine if Y position is < 240
        CALL    C,Lb208                 ; 13E9 DC0F03   .NS Does not return from this call

        CP      $F8                     ; 13EC FEF8     ..
; Call routine if Y position is >= 248
        CALL    NC,Lb208                ; 13EE D40F03   ... Does not return from this call

        LD      A,$FF                   ; 13F1 3EFF     >.
        LD      ($82AB),A               ; 13F3 32AB82   2.}

; Clear the climber sprites
        LD      HL,$9890                ; 13F6 219098   !.. Point to start of climber sprite control (sprite 5)
        LD      B,$10                   ; 13F9 0610     ..  Loop 16 times (for sprites 5 - 7 - the climber)

Lb252:  LD      (HL),$00                ; 13FB 3600     6D  Clear value
        INC     HL                      ; 13FD 23       #   Go to next byte
        DEC     B                       ; 13FE 05       .   Decrement counter
        JR      NZ,Lb252                ; 13FF 20FA      .  Done? Nope, keep looping

        CALL    PLAYER_DIED             ; 1401 CDEA10   ... The player has died

        CALL    Lb208                   ; 1404 CD0F03   ... Does not return from this call

Lb296:  LD      A,($813D)               ; 1407 3A3D81   :x. Climber left arm sprite X position
        LD      (CLIMBER_X_POS),A       ; 140A 32E780   2..
        LD      A,(FLOOR_NUM)           ; 140D 3A3181   :a. Get the working floor number
        LD      (CUR_FLOOR_NUM),A       ; 1410 32E880   2.. Save the current floor number
        LD      A,(FLOOR_GROUP)         ; 1413 3A3081   :1. Get the working floor group
        LD      (CUR_FLOOR_GROUP),A     ; 1416 32E980   2.. Save the current floor group
        LD      A,$FF                   ; 1419 3EFF     >.
        LD      ($8281),A               ; 141B 328182   2.}

        LD      BC,$407                 ; 141E 010704   ..T	 Play Player falling music
        CALL    LOAD_SOUND_DATA         ; 1421 CDBB11   ..A
        RET                             ; 1424 C9       .    End ISR subroutine for index 2

;=============================================================================
; Starts a building
;	Initializes and starts a building
;
; Input:
;	None
;=============================================================================
START_BUILDING:
        LD      A,$02                   ; 1425 3E02     >G
        CALL    Lb255                   ; 1427 CD2103   .4S
        LD      A,$03                   ; 142A 3E03     >S
        CALL    Lb255                   ; 142C CD2103   .0.


; Initialize the climber sprite control (4 sprites)
        LD      HL,INIT_CLIMBER_SPRITE_DATA ; 142F 21AD14   !.@  Source: climber sprite initial data table
        LD      DE,CLIMBER_SPRITE_CTRL  ; 1432 113281   .f.  Destination: Sprite control data working area
        LD      BC,$10                  ; 1435 011000   ..D  Copy 16 bytes of data
        CALL    BLOCK_COPY              ; 1438 CD4A04   ..T  Block copy routine

; Initialize climber movement flags
        LD      HL,$14BD                ; 143B 21BD14   !.@  Source address
        LD      DE,$8146                ; 143E 114681   .R.  Destination address
        LD      BC,$06                  ; 1441 010600   ..D  Copy 6 bytes of data
        CALL    BLOCK_COPY              ; 1444 CD4A04   ..T  Block copy routine

        CALL    SHOW_CLIMBER            ; 1447 CD4415   .@Q  Show climber on screen

        LD      A,$20                   ; 144A 3E20     >d
        CALL    DELAY                   ; 144C CDB802   ..G  Delay

        LD      BC,$400                 ; 144F 010004   .D.	Play start building music
        CALL    LOAD_SOUND_DATA         ; 1452 CDBB11   ..A

Lb258:  NOP                             ; 1455 00       .
        CALL    SHOW_CLIMBER            ; 1456 CD4415   ..P  Show climber on screen
        CALL    CHECK_ALLOWED_HAND_MOVES ; 1459 CD771A   ."N
        LD      A,($82AA)               ; 145C 3AAA82   :U.
        BIT     6,A                     ; 145F CB77     .w
        JR      Z,Lb256                 ; 1461 2810     (.
        LD      A,$02                   ; 1463 3E02     >G	Set the ISR mode index to 2
        LD      (ISR_MODE_IDX),A        ; 1465 325B81   2^.
        LD      A,$02                   ; 1468 3E02     >.
        CALL    Lb223                   ; 146A CD6503   .p.
        LD      A,$03                   ; 146D 3E03     >.
        CALL    Lb223                   ; 146F CD6503   .uS
        RET                             ; 1472 C9       .

Lb256:  NOP                             ; 1473 00       .
        LD      A,(SCRIPTED_INPUT_IDX)  ; 1474 3A5581   :..  Get scripted input index value
        LD      E,A                     ; 1477 5F       _
        LD      D,$00                   ; 1478 1600     .D
        INC     A                       ; 147A 3C       <
        AND     $0F                     ; 147B E60F     .N   Limit range (0 - 15)
        LD      (SCRIPTED_INPUT_IDX),A  ; 147D 325581   2..  Save index

        LD      HL,$14C3                ; 1480 21C314   !..  Point to pointer table data below
        ADD     HL,DE                   ; 1483 19       .    Add offset
        LD      A,(HL)                  ; 1484 7E       ~    Read pointer value at given address
        LD      (CUR_PLAYER_INPUT),A    ; 1485 325481   2..  Save current player input
        CALL    PROCESS_INPUT           ; 1488 CDBA15   ..P  Process input
        CALL    Lb248                   ; 148B CD2D16   .8.
        LD      A,($814C)               ; 148E 3A4C81   :..
        CPL                             ; 1491 2F       /

        ADD     A,$01                   ; 1492 C601     ..
        CALL    MOVE_CLIMBER_Y          ; 1494 CDD118   ...  Move climber up 1

        XOR     A                       ; 1497 AF       .
        LD      ($814C),A               ; 1498 324C81   2..

        LD      A,$0A                   ; 149B 3E0A     >O  
        CALL    DELAY                   ; 149D CDB802   ... Delay

        LD      A,($82AA)               ; 14A0 3AAA82   :U.
        ADD     A,$01                   ; 14A3 C601     ..
        LD      ($82AA),A               ; 14A5 32AA82   2.}
        JP      Lb258                   ; 14A8 C35514   ...

;-------------------------------------------------------------------------------
; Data for the Crazy Climber Guy
; Range: $14AB - $14D4
;-------------------------------------------------------------------------------

        .db     $C7, $FB

; ($14AD) - Sprite control data.  Copied to CLIMBER_SPRITE_CTRL
; Attributes, Color, Y position, X position
INIT_CLIMBER_SPRITE_DATA:
        .db     $7B, $06, $12, $A8		; Left leg (sprite #59, x axis inverted)
		.db     $3B, $06, $12, $B8		; Right leg (sprite #59, x axis not inverted)
        .db     $79, $06, $22, $A8		; Left arm (sprite #57, x axis inverted)
		.db     $39, $06, $22, $B8		; Right arm (sprite #57)

; ($14BD) - Copied to $8146
        .db     $01, $01, $04, $01, $04, $00

; ($14C3)
		.db     $22, $22
        .db     $22, $22
		.db     $80, $10
		.db     $10, $10
		.db     $10, $40
        .db     $04, $01
		.db     $01, $01
		.db     $01, $08

        .db     $C7, $F3

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------



;=============================================================================
;=============================================================================
Lb358:  NOP                             ; 14D5 00       .

;------------------
; Set default left leg position
        LD      HL,INIT_CLIMBER_SPRITE_DATA ; 14D6 21AD14   !..  Source address for block copy
        LD      DE,CLIMBER_LLEG_CTRL    ; 14D9 113281   .'.  Destination - Climber left leg control
        LD      BC,$0001                ; 14DC 011000   ...  Copy 1 byte
        CALL    BLOCK_COPY              ; 14DF CD4A04   .K.  Block copy routine

;------------------
; Move climber up 
        LD      HL,CLIMBER_SPRITE_CTRL  ; 14E2 213281   !f.  Point to climber sprite control
        LD      B,$04                   ; 14E5 0604     .T   Loop 4X

Lb265:  INC     HL                      ; 14E7 23       #    Point to Y position
        INC     HL                      ; 14E8 23       #
        LD      A,(HL)                  ; 14E9 7E       ~    Add $40 to Y position
        ADD     A,$40                   ; 14EA C640     ..
        LD      (HL),A                  ; 14EC 77       w
        INC     HL                      ; 14ED 23       #    Go to next sprite
        INC     HL                      ; 14EE 23       #
        DEC     B                       ; 14EF 05       .    Decrement counter
        JR      NZ,Lb265                ; 14F0 20F5      .   Done? Nope, keep looping

;------------------
; Adjust X position of climber
        LD      A,(CLIMBER_X_POS)       ; 14F2 3AE780   :..  Get index value (X position)
        SUB     $40                     ; 14F5 D640     .Q
        RRCA                            ; 14F7 0F       .
        RRCA                            ; 14F8 0F       .
        RRCA                            ; 14F9 0F       .
        AND     $1F                     ; 14FA E61F     ._
        LD      HL,CLIMBER_SCRNX_DATA   ; 14FC 213015   ! P  Point to X screen positions table
        LD      E,A                     ; 14FF 5F       _
        LD      D,$00                   ; 1500 1600     .D
        ADD     HL,DE                   ; 1502 19       .    HL = (Index-$40) / 8
        LD      B,(HL)                  ; 1503 46       F    B = Table value
        LD      A,$10                   ; 1504 3E10     >.
        ADD     A,B                     ; 1506 80       .
        LD      C,A                     ; 1507 4F       O    C = B + $10 (next column to right)
        LD      IX,CLIMBER_SPRITE_CTRL  ; 1508 DD213281 .!'. Point to climber sprite control
        LD      (IX+$03),B              ; 150C DD7003   .p.  Left leg X pos. = B
        LD      (IX+$07),C              ; 150F DD7107   .q.  Right leg X pos. = B + $10 (next column)
        LD      (IX+$0B),B              ; 1512 DD700B   .p.  Left arm X pos. = B
        LD      (IX+$0F),C              ; 1515 DD710F   .q.  Right arm X pos. = B + $10 (next column)

; Initialize climber movement flags
        LD      HL,$14BD                ; 1518 21BD14   !..  Source address
        LD      DE,$8146                ; 151B 114681   ...  Destination address
        LD      BC,$06                  ; 151E 010600   .GD  Copy 6 bytes of data
        CALL    BLOCK_COPY              ; 1521 CD4A04   .K.  Block copy routine

        CALL    SHOW_CLIMBER            ; 1524 CD4415   ..P  Show climber on screen

        LD      BC,$400                 ; 1527 010004   .D.	 Play start building music
        CALL    LOAD_SOUND_DATA         ; 152A CDBB11   ..A
        RET                             ; 152D C9       .

;-------------------------------------------------------------------------------
; Data for the X screen positions of climber (6 possible positions)
; Range: $152E - $1543
;-------------------------------------------------------------------------------

        .db     $C7, $FB				; Start data block

; $1530
CLIMBER_SCRNX_DATA:
        .db     $48, $48, $48
		.db     $60, $60, $60
		.db     $78, $78, $78
		.db     $90, $90, $90
		.db     $A8, $A8, $A8
		.db     $C0, $C0, $C0


        .db     $C7, $F3				; End data block

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------


;=============================================================================
; Draws the climber character on the screen
;
; Copies 16 bytes of data from CLIMBER_SPRITE_CTRL to $9890 (sprite control)
; This copies sprite 5, 6, 7, and 8 sprite controls (which make up the climber).
;
;=============================================================================
SHOW_CLIMBER:
        NOP                             ; 1544 00       .
        LD      HL,CLIMBER_SPRITE_CTRL  ; 1545 213281   !'.  Source - climber sprite control
        LD      DE,$9890                ; 1548 119098   ...  Destination address
        LD      BC,$10                  ; 154B 011000   ..D  Copy 16 bytes of data
        CALL    BLOCK_COPY              ; 154E CD4A04   ..T  Block copy routine
        RET                             ; 1551 C9       .    End SHOW_CLIMBER


;=============================================================================
;=============================================================================
Lb247:  NOP                             ; 1552 00       .
        LD      A,(GAME_IN_PROGRESS)    ; 1553 3A7580   :5. Is there a game in progress?
        OR      A                       ; 1556 B7       .
        JR      Z,Lb268                 ; 1557 281D     (X  Nope, go here

; Game in progress
        LD      A,(MACH_VER)            ; 1559 3A7C80   :). Get the machine version
        OR      A                       ; 155C B7       .   Check the value
        JR      NZ,Lb269                ; 155D 2006      .  If upright (1), go here

        LD      A,(CURRENT_PLAYER)      ; 155F 3A8180   :.. Check current player
        OR      A                       ; 1562 B7       .
        JR      NZ,Lb270                ; 1563 2008      L  Player 2, go here

; Player 1 is current player
Lb269:  LD      A,(PL1_CONT_RD)         ; 1565 3A00A0   :D_ Read player 1 controls
        LD      (CUR_PLAYER_INPUT),A    ; 1568 325481   2.. Save player input
        JR      PROCESS_INPUT           ; 156B 184D     .]  Process input

; Player 2 is current player
Lb270:  NOP                             ; 156D 00       .
        LD      A,(PL2_CONT_RD)         ; 156E 3A00A8   :D. Read player 2 controls
        LD      (CUR_PLAYER_INPUT),A    ; 1571 325481   2.. Save player input
        JR      PROCESS_INPUT           ; 1574 1844     ..  Process input

; No game in progress
Lb268:  LD      A,(ISR_COUNTER)         ; 1576 3A4580   :P. Read ISR counter
        AND     $1F                     ; 1579 E61F     ..  Are bits 4 - 0 zero?
        JR      NZ,Lb271                ; 157B 2006      .  Nope, continue

; Run this section every 32nd time the ISR is called
        XOR     A                       ; 157D AF       .
        LD      (CUR_PLAYER_INPUT),A    ; 157E 325481   2.. Clear player input
        JR      Lb272                   ; 1581 1814     ..

;----------------------------------------
; Run scripted "input" for attract mode
Lb271:  LD      A,(SCRIPTED_INPUT_IDX)  ; 1583 3A5581   :.. Get script input index
        INC     A                       ; 1586 3C       <   Go to next index value
        AND     $3F                     ; 1587 E63F     ..  Limit range from (0 - 63)
        LD      (SCRIPTED_INPUT_IDX),A  ; 1589 325581   2.. Save script input index value
        LD      E,A                     ; 158C 5F       _
        LD      D,$00                   ; 158D 1600     .D
        LD      HL,SCRIPTED_INPUT_TABLE ; 158F 21E315   !.Q Point to input script table
        ADD     HL,DE                   ; 1592 19       .   HL = $15E3 + script_index
        LD      A,(HL)                  ; 1593 7E       ~   Get scripted input
        LD      (CUR_PLAYER_INPUT),A    ; 1594 325481   2.. Save as player input

Lb272:  LD      A,(MACH_SW_RD)          ; 1597 3A00B8   :D. Read the machine switches
        BIT     4,A                     ; 159A CB67     .g  Check machine type
        JR      NZ,Lb273                ; 159C 2007      .  Cocktail, go here

; Upright machine
        LD      A,$01                   ; 159E 3E01     >.
        LD      (CURRENT_FIELD_FLAG),A  ; 15A0 32B482   2K. Set current field to normal
        JR      PROCESS_INPUT           ; 15A3 1815     .P  Process input

; Cocktail machine
Lb273:  LD      A,(CURRENT_FIELD_FLAG)  ; 15A5 3AB482   :.} What is the current field setting?
        AND     A                       ; 15A8 A7       .   Is is inverted?
        JR      Z,PROCESS_INPUT         ; 15A9 280F     (N  Yes, continue

; Play a sample
        LD      HL,$4CC0                ; 15AB 21C04C   !.. 
        LD      (SNDS_DATA_PTR),HL      ; 15AE 222480   "5. Set the sample sound data pointer
        LD      A,$84                   ; 15B1 3E84     >.
        LD      (SNDS_INIT_CNT),A       ; 15B3 322780   2f. Set the sample initial counter
        XOR     A                       ; 15B6 AF       .   Set current field to cocktail
        LD      (CURRENT_FIELD_FLAG),A  ; 15B7 32B482   2.} 


;=============================================================================
; Set flags for current player input
;
; $8142 - Right stick left/right movement flag
; $8143 - Right stick up/down movement flag
; $8144 - Left stick left/right movement flag
; $8145 - Left stick up/down movement flag
;=============================================================================
PROCESS_INPUT:
        NOP                             ; 15BA 00       .
        LD      D,$00                   ; 15BB 1600     .D   Clear D
        LD      C,$04                   ; 15BD 0E04     .T   4 flags to set
        LD      IX,$8145                ; 15BF DD214581 .!P. Point to end of flags
        LD      A,(CUR_PLAYER_INPUT)    ; 15C3 3A5481   :..  Get player input

Lb275:  LD      B,A                     ; 15C6 47       G    Save value
        AND     $03                     ; 15C7 E603     ..   Decode 2 bits at a time
        LD      E,A                     ; 15C9 5F       _
        LD      HL,INPUT_FLAG_ENCODE_TABLE ; 15CA 21DF15 !.P  Point to input flag encode table
        ADD     HL,DE                   ; 15CD 19       .    HL = $15DF + bit index (0, 1, 2, or 3)
        LD      A,(HL)                  ; 15CE 7E       ~    Get table value
        LD      (IX+$00),A              ; 15CF DD7700   .wD  Save flag
        DEC     C                       ; 15D2 0D       .    Decrement counter
        JR      Z,Lb274                 ; 15D3 2807     (F   Done?  Nope, continue looping

        DEC     IX                      ; 15D5 DD2B     .+   Go to previous flag
        LD      A,B                     ; 15D7 78       x    Get value
        RRCA                            ; 15D8 0F       .    Get next two bits
        RRCA                            ; 15D9 0F       .
        JR      Lb275                   ; 15DA 18EA     ..   Loop

Lb274:  RET                             ; 15DC C9       .    End PROCESS_INPUT


;-------------------------------------------------------------------------------
; Data for input flag setting
;
; Data for scripted input in attract mode
;
; Range: $15DD - $162C
;-------------------------------------------------------------------------------

        .db     $C7, $FB				; Start data block

; $15DF - Input flag decode table
INPUT_FLAG_ENCODE_TABLE:
        .db     $00			; 0 - No input
		.db     $01			; 1 - Up or Left (depending on flag address)
		.db     $FF			; 2 - Down or Right (depending on flag address)
		.db     $00			; 3 - No input

; $15E3 - Attract mode scripted input
SCRIPTED_INPUT_TABLE:
		.db     $21, $21, $21, $21
        .db     $21, $21, $21, $15
		.db     $12, $12, $12, $12
        .db     $12, $12, $12, $12
		.db     $01, $01, $01, $01
        .db     $01, $01, $01, $01
		.db     $22, $22, $22, $22
        .db     $22, $22, $22, $22
		.db     $21, $21, $21, $21
        .db     $21, $21, $21, $21
		.db     $44, $44, $44, $44
        .db     $44, $44, $00, $00
		.db     $12, $12, $12, $12
        .db     $12, $12, $12, $12
		.db     $88, $88, $88, $88
        .db     $88, $88, $00, $00
		.db     $00, $00, $00, $00
        .db     $00, $00, $00, $00

        .db     $C7, $F3				; End data block

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------



;=============================================================================
;=============================================================================
Lb248:  LD      A,(LHAND_MOVEMENT_FLAG) ; 162D 3A4681   :.. Get left hand allowed movement flag
        LD      B,A                     ; 1630 47       G
        LD      A,(RHAND_MOVEMENT_FLAG) ; 1631 3A4781   :B. Get right hand allowed movement flag
        ADD     A,B                     ; 1634 80       .
        JR      Z,Lb289                 ; 1635 2827     (f  Allowed to move either hand? Nope, go here

        LD      B,A                     ; 1637 47       G
        LD      A,(RINPUT_Y_FLAG)       ; 1638 3A4381   :V. Get right stick Y input flag
        AND     A                       ; 163B A7       .   Any motion?
        JR      NZ,Lb290                ; 163C 2006      G  Yes, go here

        LD      A,(LINPUT_Y_FLAG)       ; 163E 3A4581   :P. Get left stick Y input flag
        AND     A                       ; 1641 A7       .   Any motion?
        JR      Z,Lb291                 ; 1642 2804     (.  Nope, go here

; Left and/or Right stick Y movement
Lb290:  NOP                             ; 1644 00       .   B contains addition of Y movement flags
        CALL    PROCESS_Y_STICKS        ; 1645 CD6316   .6.

;---------------------------------------
; Check right stick left/right movement
Lb291:  NOP                             ; 1648 00       .
        LD      A,(RINPUT_X_FLAG)       ; 1649 3A4281   :C. Get right stick X input flag
        AND     A                       ; 164C A7       .
        JR      NZ,Lb293                ; 164D 2006      .  Got movement? Yes, go here

;--------------------------------------
; Check left stick left/right movement
        LD      A,(LINPUT_X_FLAG)       ; 164F 3A4481   :@. Get left stick X input flag
        AND     A                       ; 1652 A7       .   
        JR      Z,Lb294                 ; 1653 2804     (T  No movement? Yes, go here

; Left and/or Right stick X movement
Lb293:  NOP                             ; 1655 00       .
        CALL    Lb295                   ; 1656 CD5417   ...


Lb294:  NOP                             ; 1659 00       .
        CALL    ANIMATE_CLIMBER         ; 165A CDF018   ... Animate the climber
        RET                             ; 165D C9       .

Lb289:  NOP                             ; 165E 00       .
        CALL    Lb296                   ; 165F CD0714   .F@
        RET                             ; 1662 C9       .

;=============================================================================
; We have Y stick movement from the left and/or right sticks
;
; $82AC is set to +4 or -4 if movement was successful?
;
; Input:
;	B - Contains addition of Left and right stick movement Y flags
;=============================================================================
PROCESS_Y_STICKS:
        NOP                             ; 1663 00       .
        LD      A,B                     ; 1664 78       x   Get addition of left/right stick Y flags
        CP      $02                     ; 1665 FE02     .G  Are both up?
        JR      NZ,Lb297                ; 1667 205C      .  Nope, go here


; Both sticks are up
        LD      A,(L_CLIMBER_ANIM_IDX1) ; 1669 3A4A81   :K. Left side climber animation sequence index
        LD      C,A                     ; 166C 4F       O
        LD      A,(R_CLIMBER_ANIM_IDX1) ; 166D 3A4881   :Y. Right side climber animation sequence index
        CP      C                       ; 1670 B9       .
        JP      NZ,Lb298                ; 1671 C22917   .<W Are both indexes equal? Nope, go here

        LD      A,(LINPUT_Y_FLAG)       ; 1674 3A4581   :P.
        LD      B,A                     ; 1677 47       G
        LD      A,(RINPUT_Y_FLAG)       ; 1678 3A4381   :V.
        ADD     A,B                     ; 167B 80       .
        JR      Z,Lb299                 ; 167C 2803     (S  Are sticks opposite direction? Yes, go here

        JP      P,Lb300                 ; 167E F29616   ..S Nope, must be both down.  Go here

; Sticks opposite direction (one up, one down)
Lb299:  NOP                             ; 1681 00       .
        XOR     A                       ; 1682 AF       .
        LD      (LHAND_MOVEMENT_FLAG),A ; 1683 324681   2.. Do not allow hand movements
        LD      (RHAND_MOVEMENT_FLAG),A ; 1686 324781   2B.
        NOP                             ; 1689 00       .
        LD      A,(L_CLIMBER_ANIM_IDX1) ; 168A 3A4A81   :.. Left side climber animation sequence index
        CP      $00                     ; 168D FE00     .D  At zero?
        RET     Z                       ; 168F C8       .   Yes, done

        LD      A,$FC                   ; 1690 3EFC     >.  Nope - Y movement down
        LD      ($814C),A               ; 1692 324C81   2..
        RET                             ; 1695 C9       .

Lb300:  NOP                             ; 1696 00       .
        CP      $02                     ; 1697 FE02     .G
        JR      Z,Lb301                 ; 1699 280E     (.  Are both sticks up?  Yes, go here

; Sticks are down
        LD      A,(L_CLIMBER_ANIM_IDX1) ; 169B 3A4A81   :K. Left side climber animation sequence index
        CP      $04                     ; 169E FE04     ..  Is index 4?
        RET     Z                       ; 16A0 C8       .   Yes, return

        XOR     A                       ; 16A1 AF       .   Do not allow hand movements
        LD      (LHAND_MOVEMENT_FLAG),A ; 16A2 324681   2R. 
        LD      (RHAND_MOVEMENT_FLAG),A ; 16A5 324781   2B.
        RET                             ; 16A8 C9       .   Done

; Both sticks up
Lb301:  NOP                             ; 16A9 00       .
        LD      A,($82AC)               ; 16AA 3AAC82   :.. Check room to move up?
        CP      $00                     ; 16AD FE00     .D
        JR      Z,Lb302                 ; 16AF 2808     (L  Yes, continue

        XOR     A                       ; 16B1 AF       .
        LD      (RINPUT_Y_FLAG),A       ; 16B2 324381   2V. Clear stick movement flags
        LD      (LINPUT_Y_FLAG),A       ; 16B5 324581   2U.
        RET                             ; 16B8 C9       .   Done


Lb302:  LD      A,(L_CLIMBER_ANIM_IDX1) ; 16B9 3A4A81   :K. Left side climber animation sequence index
        CP      $04                     ; 16BC FE04     ..
        RET     Z                       ; 16BE C8       .

        LD      A,$04                   ; 16BF 3E04     >T  Y movement up?
        LD      ($814C),A               ; 16C1 324C81   2H.
        RET                             ; 16C4 C9       .

; Both sticks up
Lb297:  NOP                             ; 16C5 00       .
        LD      A,(RHAND_MOVEMENT_FLAG) ; 16C6 3A4781   :B. Get right hand movement allowed flag
        AND     A                       ; 16C9 A7       .   Movement allowed?
        JR      Z,Lb303                 ; 16CA 282E     (o  Nope, go here

        LD      A,(LINPUT_Y_FLAG)       ; 16CC 3A4581   :P. Check left input Y flag
        CP      $00                     ; 16CF FE00     .D  Is value 0?
        RET     Z                       ; 16D1 C8       .   Yes, no movement.  Exit

; We have left stick movement
        JP      P,Lb304                 ; 16D2 F2E116   ..S Left up? Yes, go here

; Left stick down
        LD      A,(L_CLIMBER_ANIM_IDX1) ; 16D5 3A4A81   :K. Left side climber animation sequence index
        CP      $00                     ; 16D8 FE00     .D  Is index 0?
        RET     Z                       ; 16DA C8       .   Yes, exit

        LD      A,$FC                   ; 16DB 3EFC     >.  Y movement down?
        LD      ($814C),A               ; 16DD 324C81   2H.
        RET                             ; 16E0 C9       .   Done

; Left stick up
Lb304:  NOP                             ; 16E1 00       .
        LD      A,($82AC)               ; 16E2 3AAC82   :.. Check room to move up?
        CP      $00                     ; 16E5 FE00     .D
        JR      Z,Lb305                 ; 16E7 2805     (.  Yes, continue

        XOR     A                       ; 16E9 AF       .
        LD      (LINPUT_Y_FLAG),A       ; 16EA 324581   2P. Clear left input stick Y movement flag
        RET                             ; 16ED C9       .

Lb305:  LD      A,(L_CLIMBER_ANIM_IDX1) ; 16EE 3A4A81   :.. Left side climber animation sequence index
        CP      $04                     ; 16F1 FE04     .T  Is index 4?
        RET     Z                       ; 16F3 C8       .   Yes, done

        LD      A,$04                   ; 16F4 3E04     >.  Y movement up?
        LD      ($814C),A               ; 16F6 324C81   2..
        RET                             ; 16F9 C9       .

; Check Right stick
Lb303:  NOP                             ; 16FA 00       .
        LD      A,(RINPUT_Y_FLAG)       ; 16FB 3A4381   :.. Check right stick Y input flag
        CP      $00                     ; 16FE FE00     .D  Any movement?
        RET     Z                       ; 1700 C8       .   Nope, return

        JP      P,Lb306                 ; 1701 F21017   ..W Right stick up? Yes, go here

;------------------
; Right stick down
        LD      A,(R_CLIMBER_ANIM_IDX1) ; 1704 3A4881   :.. Right side climber animation sequence index
        CP      $00                     ; 1707 FE00     .D  Is right arm fully down?
        RET     Z                       ; 1709 C8       .   Yes - nothing to move.  Exit

        LD      A,$FC                   ; 170A 3EFC     >.  Y movement down?
        LD      ($814C),A               ; 170C 324C81   2..
        RET                             ; 170F C9       .

;----------------
; Right stick up
Lb306:  NOP                             ; 1710 00       .
        LD      A,($82AC)               ; 1711 3AAC82   :.} Check room to move up?
        CP      $00                     ; 1714 FE00     .D
        JR      Z,Lb307                 ; 1716 2805     (U  OK to move, go here

        XOR     A                       ; 1718 AF       .
        LD      (RINPUT_Y_FLAG),A       ; 1719 324381   2.. Clear right stick Y movement flag
        RET                             ; 171C C9       .   Done

Lb307:  LD      A,(R_CLIMBER_ANIM_IDX1) ; 171D 3A4881   :Y. Right side climber animation sequence index
        CP      $04                     ; 1720 FE04     ..  Is right arm fully up?
        RET     Z                       ; 1722 C8       .   Yes - nothing to move. Exit

        LD      A,$04                   ; 1723 3E04     >T  Y movement up?
        LD      ($814C),A               ; 1725 324C81   2H.
        RET                             ; 1728 C9       .   Done

; Both sticks are up, but animation sequences are not equal
Lb298:  NOP                             ; 1729 00       .
        LD      A,(L_CLIMBER_ANIM_IDX1) ; 172A 3A4A81   :.. Left side climber animation sequence index
        CP      $04                     ; 172D FE04     .T  Is value = 4?
        JR      NZ,Lb308                ; 172F 200C      \  Nope, go here

        XOR     A                       ; 1731 AF       .   Yes, can't move any more
        LD      (LHAND_MOVEMENT_FLAG),A ; 1732 324681   2R. Do not allow left hand movement
        LD      A,(LINPUT_Y_FLAG)       ; 1735 3A4581   :U. Check left stick Y input flag
        CP      $FF                     ; 1738 FEFF     ..  Is down?
        RET     NZ                      ; 173A C0       .   Nope, return

        JR      Lb309                   ; 173B 1811     .A  Yes, go here

Lb308:  NOP                             ; 173D 00       .
        LD      A,(R_CLIMBER_ANIM_IDX1) ; 173E 3A4881   :.. Right side climber animation sequence index
        CP      $04                     ; 1741 FE04     .T  Is right arm fully up?
        RET     NZ                      ; 1743 C0       .   Nope, exit

        XOR     A                       ; 1744 AF       .   Yes, can't move any more
        LD      (RHAND_MOVEMENT_FLAG),A ; 1745 324781   2B. Clear right movement flag
        LD      A,(RINPUT_Y_FLAG)       ; 1748 3A4381   :V. Get right stick Y input flag
        CP      $FF                     ; 174B FEFF     ..  Is stick down?
        RET     NZ                      ; 174D C0       .   Nope, return

Lb309:  LD      A,$FC                   ; 174E 3EFC     >.
        LD      ($814C),A               ; 1750 324C81   2.. Y movement down?
        RET                             ; 1753 C9       .

;=============================================================================
;=============================================================================
Lb295:  NOP                             ; 1754 00       .
        LD      A,(LINPUT_X_FLAG)       ; 1755 3A4481   :@. Get left stick X input flag
        LD      B,A                     ; 1758 47       G
        LD      A,(RINPUT_X_FLAG)       ; 1759 3A4281   :C. Get right stick X input flag
        ADD     A,B                     ; 175C 80       .   Add values
        JR      Z,Lb310                 ; 175D 2805     (.  Zero? Yes, go here

        JP      P,Lb311                 ; 175F F28217   ..W Positive? Yes, go here
        JR      Lb312                   ; 1762 1815     .Q  Must be negative... go here

; Sticks are opposite directions (left/right -or- right/left combo)
Lb310:  LD      A,(RHAND_MOVEMENT_FLAG) ; 1764 3A4781   :B. Get right hand movement allowed flag
        AND     A                       ; 1767 A7       .   Movement allowed?
        JR      Z,Lb313                 ; 1768 2808     (L  Nope, go here

        XOR     A                       ; 176A AF       .   No input for left X stick
        LD      (LINPUT_X_FLAG),A       ; 176B 324481   2@. Set left stick X input flag
        CALL    TRY_MOVE_RIGHT_HAND     ; 176E CDDD17   ...
        RET                             ; 1771 C9       .

; Note: A = 0 if this branch is taken
Lb313:  LD      (RINPUT_X_FLAG),A       ; 1772 324281   2.. No input for right X stick
        CALL    TRY_MOVE_LEFT_HAND      ; 1775 CD8B17   ..W
        RET                             ; 1778 C9       .


; One / both sticks are left
Lb312:  CALL    TRY_MOVE_RIGHT_HAND     ; 1779 CDDD17   ."W 
        AND     A                       ; 177C A7       .   Successful?
        RET     NZ                      ; 177D C0       .   Yes, return

        CALL    TRY_MOVE_LEFT_HAND      ; 177E CD8B17   .t. Not successful, try left hand
        RET                             ; 1781 C9       .


; One / both sticks are right
Lb311:  CALL    TRY_MOVE_LEFT_HAND      ; 1782 CD8B17   .t. 
        AND     A                       ; 1785 A7       .   Successful?
        RET     NZ                      ; 1786 C0       .   Yes, return

        CALL    TRY_MOVE_RIGHT_HAND     ; 1787 CDDD17   ."W Not successful, try right hand
        RET                             ; 178A C9       .

;=============================================================================
; Attempts to move the climber in the X position based on the left hand?
;
; If a move is successful, A will be $FF, else $00.
;
; LHAND_MOVEMENT_FLAG - 0 - Do not allow left hand movement
;         != 0 - Allow left hand movement
;
; RHAND_MOVEMENT_FLAG - 0 - Do not allow right hand movement
;         != 0 - Allow right hand movement
;
; Output:
;	A = 0 - Nothing moved
;	A = $FF - Movement
;=============================================================================
TRY_MOVE_LEFT_HAND:
        LD      A,(LINPUT_X_FLAG)       ; 178B 3A4481   :@. Get left stick X input flag
        AND     A                       ; 178E A7       .   Got input?
        JR      Z,Lb316                 ; 178F 284A     (K  Nope, exit routine (returns 0)

        NOP                             ; 1791 00       .
        LD      A,(LHAND_MOVEMENT_FLAG) ; 1792 3A4681   :R. Get left hand movement flag
        AND     A                       ; 1795 A7       .   Left hand movement allowed?
        JR      NZ,Lb317                ; 1796 2006      G  Yes, continue

        XOR     A                       ; 1798 AF       .   No movement allowed
        LD      (LINPUT_X_FLAG),A       ; 1799 324481   2@. Set to no movement for left input X flag
        JR      Lb316                   ; 179C 183D     .y  Exit routine (returns $00)

;-------------------
; Move climber left
Lb317:  LD      A,(LINPUT_X_FLAG)       ; 179E 3A4481   :.. Get left stick X input flag
        CP      $01                     ; 17A1 FE01     ..  Moved left?
        JR      NZ,Lb318                ; 17A3 201A      .  Nope, move climber right

        LD      A,(L_CLIMBER_ANIM_IDX2) ; 17A5 3A4B81   :.. Left side climber arm in/out index
        CP      $00                     ; 17A8 FE00     .D  Is left arm in?
        JR      Z,Lb316                 ; 17AA 282F     (*  Yes, exit routine (return $00)

        LD      A,(R_CLIMBER_ANIM_IDX2) ; 17AC 3A4981   :M. Right side climber arm in/out index
        CP      $00                     ; 17AF FE00     .D  Is right arm out?
        JR      Z,Lb316                 ; 17B1 2828     (l  Yes, exit routine (return $00)

        LD      A,$F8                   ; 17B3 3EF8     >.
        CALL    MOVE_CLIMBER_X          ; 17B5 CDB218   ... Move climber to the left 8

        LD      A,$FF                   ; 17B8 3EFF     >.  Set to right input
        LD      (RINPUT_X_FLAG),A       ; 17BA 324281   2.. Set right stick X input flag
        JR      Lb320                   ; 17BD 1819     .I  Exit routine (returns $FF)

;-------------------
; Move climber right
Lb318:  NOP                             ; 17BF 00       .
        LD      A,(L_CLIMBER_ANIM_IDX2) ; 17C0 3A4B81   :^. Left side climber arm in/out index
        CP      $01                     ; 17C3 FE01     ..  Is left arm out?
        JR      Z,Lb316                 ; 17C5 2814     (.  Yes, exit routine (return $00)

        LD      A,(R_CLIMBER_ANIM_IDX2) ; 17C7 3A4981   :.. Right side climber arm in/out index
        CP      $01                     ; 17CA FE01     ..  Is right arm in?
        JR      Z,Lb316                 ; 17CC 280D     (]  Yes, exit routine (return $00)

        LD      A,$08                   ; 17CE 3E08     >L
        CALL    MOVE_CLIMBER_X          ; 17D0 CDB218   ... Move climber to the right 8

        LD      A,$01                   ; 17D3 3E01     >.  Set to left input
        LD      (RINPUT_X_FLAG),A       ; 17D5 324281   2C. Set right stick X input flag

Lb320:  LD      A,$FF                   ; 17D8 3EFF     >.  Exit with A = $FF (got movement)
        RET                             ; 17DA C9       .   End TRY_MOVE_LEFT_HAND

Lb316:  XOR     A                       ; 17DB AF       .   Exit with A = 0 (no movement)
        RET                             ; 17DC C9       .   End TRY_MOVE_LEFT_HAND


;=============================================================================
; Attempts to move the climber in the X position based on the right hand?
;
; If a move is successful, A will be $FF, else $00.
;
; Output:
;	A = 0 - Nothing moved
;	A = $FF - Movement
;=============================================================================
TRY_MOVE_RIGHT_HAND:
        LD      A,(RINPUT_X_FLAG)       ; 17DD 3A4281   :C. Get right stick X input flag
        AND     A                       ; 17E0 A7       .
        JR      Z,Lb321                 ; 17E1 2849     (.  No input? Return 0

        LD      A,(RHAND_MOVEMENT_FLAG) ; 17E3 3A4781   :B. Get right hand movement allowed flag
        AND     A                       ; 17E6 A7       .   Movement allowed?
        JR      NZ,Lb322                ; 17E7 2006      .  Yes, go here

        XOR     A                       ; 17E9 AF       .   No input
        LD      (RINPUT_X_FLAG),A       ; 17EA 324281   2.. Set right stick X input flag
        JR      Lb321                   ; 17ED 183D     .x  Exit (return 0)

;-------------------
; Move climber left
Lb322:  LD      A,(RINPUT_X_FLAG)       ; 17EF 3A4281   :C. Get right stick X input flag
        CP      $01                     ; 17F2 FE01     ..  Left input?
        JR      NZ,Lb323                ; 17F4 201A      N  Nope, move right

        LD      A,(R_CLIMBER_ANIM_IDX2) ; 17F6 3A4981   :M. Right side climber arm in/out index
        CP      $00                     ; 17F9 FE00     .D  Is right arm out?
        JR      Z,Lb321                 ; 17FB 282F     (n  Yes, can't move, exit

        LD      A,(L_CLIMBER_ANIM_IDX2) ; 17FD 3A4B81   :.. Left side climber arm in/out index
        CP      $00                     ; 1800 FE00     .D  Is left arm in?
        JR      Z,Lb321                 ; 1802 2828     (l  Yes, can't move, exit

        LD      A,$F8                   ; 1804 3EF8     >.
        CALL    MOVE_CLIMBER_X          ; 1806 CDB218   ... Move climber to the left 8

; Successful move
        LD      A,$FF                   ; 1809 3EFF     >.  Set right input
        LD      (LINPUT_X_FLAG),A       ; 180B 324481   2@. Set left stick X input flag
        JR      Lb324                   ; 180E 1819     .I  Exit (return $FF)

;--------------------
; Move climber right
Lb323:  NOP                             ; 1810 00       .
        LD      A,(R_CLIMBER_ANIM_IDX2) ; 1811 3A4981   :.. Right side climber arm in/out index
        CP      $01                     ; 1814 FE01     ..  Is right arm in?
        JR      Z,Lb321                 ; 1816 2814     (@  Yes, can't move, exit

        LD      A,(L_CLIMBER_ANIM_IDX2) ; 1818 3A4B81   :^. Left side climber arm in/out index
        CP      $01                     ; 181B FE01     ..  Is left arm out?
        JR      Z,Lb321                 ; 181D 280D     (.  Yes, can't move, exit

        LD      A,$08                   ; 181F 3E08     >L
        CALL    MOVE_CLIMBER_X          ; 1821 CDB218   ... Move climber to the right 8

; Successful move
        LD      A,$01                   ; 1824 3E01     >.  Set left input
        LD      (LINPUT_X_FLAG),A       ; 1826 324481   2.. Set left stick X input flag

Lb324:  LD      A,$FF                   ; 1829 3EFF     >.
        RET                             ; 182B C9       .   End TRY_MOVE_RIGHT_HAND

Lb321:  XOR     A                       ; 182C AF       .
        RET                             ; 182D C9       .   End TRY_MOVE_RIGHT_HAND


;=============================================================================
;=============================================================================
Lb249:  NOP                             ; 182E 00       .
        LD      A,(LHAND_MOVEMENT_FLAG) ; 182F 3A4681   :.. Get left hand movement allowed flag
        LD      B,A                     ; 1832 47       G
        LD      A,(RHAND_MOVEMENT_FLAG) ; 1833 3A4781   :B. Get right hand movement allowed flag
        ADD     A,B                     ; 1836 80       .   Add values
        CP      $02                     ; 1837 FE02     .G  Are both hands allowed to move?
        JR      NZ,Lb325                ; 1839 3004     0T  Nope, go here

; Both hands allowed to move
        CALL    Lb296                   ; 183B CD0714   .F@ 
        RET                             ; 183E C9       .

Lb325:  NOP                             ; 183F 00       .
        LD      A,($8282)               ; 1840 3A8282   :}.
        AND     $80                     ; 1843 E680     ..
        JR      NZ,Lb326                ; 1845 2022      g

        XOR     A                       ; 1847 AF       .
        LD      (LHAND_MOVEMENT_FLAG),A ; 1848 324681   2R. No movement allowed for left hand
        LD      A,(R_CLIMBER_ANIM_IDX1) ; 184B 3A4881   :Y. Right side climber animation sequence index
        CP      $00                     ; 184E FE00     .D  Is right arm fully down?
        JR      NZ,Lb327                ; 1850 200B      [  Nope, exit

; Right arm fully down
        LD      A,(L_CLIMBER_ANIM_IDX1) ; 1852 3A4A81   :.. Left side climber animation sequence index
        CP      $04                     ; 1855 FE04     .T  Is left arm fully up?
        JR      NZ,Lb327                ; 1857 2004      T  Nope, go here

; Left arm fully up
        LD      A,$01                   ; 1859 3E01     >.  Set right Y input to UP
        JR      Lb328                   ; 185B 1802     .G

Lb327:  LD      A,$FF                   ; 185D 3EFF     >.  Set right Y input to DOWN

Lb328:  LD      (RINPUT_Y_FLAG),A       ; 185F 324381   2.. Set rigth Y input
        LD      A,$01                   ; 1862 3E01     >.
        LD      (LINPUT_Y_FLAG),A       ; 1864 324581   2P. Set left Y input to UP
        JR      Lb329                   ; 1867 1821     .4

Lb326:  XOR     A                       ; 1869 AF       .
        LD      (RHAND_MOVEMENT_FLAG),A ; 186A 324781   2B. Do not allow right hand movement
        LD      A,(L_CLIMBER_ANIM_IDX1) ; 186D 3A4A81   :K. Left side climber animation sequence index
        CP      $00                     ; 1870 FE00     .D
        JR      NZ,Lb330                ; 1872 200C      .

        LD      A,(R_CLIMBER_ANIM_IDX1) ; 1874 3A4881   :.. Right side climber animation sequence index
        CP      $04                     ; 1877 FE04     .T  Is right arm fully up?
        JR      NZ,Lb330                ; 1879 2005      .  Nope, go here

; Right arm fully up
        LD      A,$01                   ; 187B 3E01     >.  Set left Y input to UP
        JP      Lb331                   ; 187D C38218   ...

Lb330:  LD      A,$FF                   ; 1880 3EFF     >.  Set left Y input to DOWN

Lb331:  LD      (LINPUT_Y_FLAG),A       ; 1882 324581   2P. Set left Y input
        LD      A,$01                   ; 1885 3E01     >.
        LD      (RINPUT_Y_FLAG),A       ; 1887 324381   2.. Set right Y input to DOWN

Lb329:  NOP                             ; 188A 00       .
        CALL    Lb248                   ; 188B CD2D16   .8.
        CALL    SHOW_CLIMBER            ; 188E CD4415   ..P Show climber on screen
        LD      A,($8282)               ; 1891 3A8282   :.}
        ADD     A,$FF                   ; 1894 C6FF     ..
        LD      C,A                     ; 1896 4F       O
        AND     $0F                     ; 1897 E60F     .N
        JR      Z,Lb332                 ; 1899 280F     (N

        LD      A,C                     ; 189B 79       y
        LD      ($8282),A               ; 189C 328282   2}.

        LD      A,$05                   ; 189F 3E05     >.
        CALL    DELAY                   ; 18A1 CDB802   ... Delay

        CALL    CHECK_ALLOWED_HAND_MOVES ; 18A4 CD771A   .#.
        JP      Lb325                   ; 18A7 C33F18   ...

Lb332:  CALL    UPDATE_BONUS_RATE       ; 18AA CD3E11   ..A	Update (decrement) the bonus rate
        XOR     A                       ; 18AD AF       .
        LD      ($8282),A               ; 18AE 328282   2}.
        RET                             ; 18B1 C9       .

;=============================================================================
; Moves climber in the X position
;
; $8135  X pos. sprite 5 - left leg
; $8139  X pos. sprite 6 - right leg
; $813D  X pos. sprite 7 - left arm
; $8141  X pos. sprite 8 - right arm
;
; Input:
;	A - Value to move in X direction (relative)
;=============================================================================
MOVE_CLIMBER_X:
        NOP                             ; 18B2 00       .
        LD      B,A                     ; 18B3 47       G   B = X position to move

        LD      A,($8141)               ; 18B4 3A4181   :E. Climber right arm sprite X position
        ADD     A,B                     ; 18B7 80       .
        LD      ($8141),A               ; 18B8 324181   2E.

        LD      A,($8139)               ; 18BB 3A3981   :i. Climber right leg X position
        ADD     A,B                     ; 18BE 80       .
        LD      ($8139),A               ; 18BF 323981   2i.

        LD      A,($813D)               ; 18C2 3A3D81   :y. Climber left arm sprite X position
        ADD     A,B                     ; 18C5 80       .
        LD      ($813D),A               ; 18C6 323D81   2y.

        LD      A,($8135)               ; 18C9 3A3581   :p. Climber left leg sprite X position
        ADD     A,B                     ; 18CC 80       .
        LD      ($8135),A               ; 18CD 323581   2p.
        RET                             ; 18D0 C9       .   End MOVE_CLIMBER_X


;=============================================================================
; Moves the climber in the Y position
;
; $8134  Y pos. sprite 5 - left leg
; $8138  Y pos. sprite 6 - right leg
; $813C  Y pos. sprite 7 - left arm
; $8140  Y pos. sprite 8 - right arm
;
; Input:
;	A - Value to move in Y direction (relative)
;=============================================================================
MOVE_CLIMBER_Y:
        NOP                             ; 18D1 00       .
        LD      B,A                     ; 18D2 47       G  B = input value

        LD      A,($8140)               ; 18D3 3A4081   :Q.  Climber right arm Y position
        ADD     A,B                     ; 18D6 80       .
        LD      ($8140),A               ; 18D7 324081   2Q.

        LD      A,($8138)               ; 18DA 3A3881   :(.  Climber right left Y position
        ADD     A,B                     ; 18DD 80       .
        LD      ($8138),A               ; 18DE 323881   2(.

        LD      A,($813C)               ; 18E1 3A3C81   :-.  Climber left arm Y position
        ADD     A,B                     ; 18E4 80       .
        LD      ($813C),A               ; 18E5 323C81   2-.

        LD      A,($8134)               ; 18E8 3A3481   :`.  Climbers left leg sprite Y position
        ADD     A,B                     ; 18EB 80       .
        LD      ($8134),A               ; 18EC 323481   2`.
        RET                             ; 18EF C9       .    End MOVE_CLIMBER_Y



;=============================================================================
; Animates the climber
;
; Right half of climber animation is based on the following:
; R_CLIMBER_ANIM_IDX1 (0 - 4), 0 is fully down, 4 is fully up
; R_CLIMBER_ANIM_IDX2 (0, 1) 0 is arm out, 1 is arm in

; Right joystick inputs:
; RINPUT_X_FLAG (-1 = left, 0 = no input, 1 - right)
; RINPUT_Y_FLAG (-1 = down, 0 = no input, 1 - up)
;
; Left half of climber animation is based on the following:
; L_CLIMBER_ANIM_IDX1 (0 - 4), 0 is fully down, 4 is fully up
; L_CLIMBER_ANIM_IDX2 (0, 1) 0 is arm in, 1 is arm out
;
; Left joystick inputs:
; LINPUT_X_FLAG (-1 = left, 0 = no input, 1 - right)
; LINPUT_Y_FLAG (-1 = down, 0 = no input, 1 - up)
;=============================================================================
ANIMATE_CLIMBER:

;-------------------------
; Check right arm up/down
        LD      A,(R_CLIMBER_ANIM_IDX1) ; 18F0 3A4881   :.. Right side climber animation sequence index
        LD      B,A                     ; 18F3 47       G
        LD      A,(RINPUT_Y_FLAG)       ; 18F4 3A4381   :V.
        ADD     A,B                     ; 18F7 80       .   Add values
        LD      B,A                     ; 18F8 47       G
; Note: This will only jump if right arm is fully down (index - 0), and right input is down (-1)
        JP      M,Lb334                 ; 18F9 FA2F19   .nI Is value negative? Yes, go here

; Note: This will only jump if right arm is fully up (index = 4), and right input is up (+1)
        SUB     $05                     ; 18FC D605     .U  Subtract 5
        JP      P,Lb334                 ; 18FE F22F19   .*I Is value positive? Yes, go here

        LD      A,B                     ; 1901 78       x   Is value = 1?
        CP      $01                     ; 1902 FE01     ..
        JR      NZ,Lb335                ; 1904 2011      A  Nope, go here

; Right arm fully down (idx1 = 0) and input up (1) -or- Right arm past middle (idx1 = 2) and input down (-1)
        LD      A,(R_CLIMBER_ANIM_IDX1) ; 1906 3A4881   :.. Right side climber animation sequence index
        CP      $00                     ; 1909 FE00     .D  Is right arm fully down?
        JR      NZ,Lb336                ; 190B 201E      [  Nope, go here

; Right arm fully down and input up
        LD      A,($8140)               ; 190D 3A4081   :Q. Climber right arm Y position
        ADD     A,$04                   ; 1910 C604     ..  Move up 4
        LD      ($8140),A               ; 1912 324081   2..
        JR      Lb336                   ; 1915 1814     ..

Lb335:  LD      A,B                     ; 1917 78       x
        CP      $00                     ; 1918 FE00     .D
        JR      NZ,Lb336                ; 191A 200F      .

; Right arm fully down and no movement or right arm 
        LD      A,(R_CLIMBER_ANIM_IDX1) ; 191C 3A4881   :.. Right side climber animation sequence index
        CP      $01                     ; 191F FE01     ..  Is right arm in the middle?
        JR      NZ,Lb336                ; 1921 2008      L  Nope, go here

; Right arm in the middle
        LD      A,($8140)               ; 1923 3A4081   :Q. Climber right arm Y position
        SUB     $04                     ; 1926 D604     ..  Move down 4
        LD      ($8140),A               ; 1928 324081   2..

; Update animation index
Lb336:  LD      A,B                     ; 192B 78       x
        LD      (R_CLIMBER_ANIM_IDX1),A ; 192C 324881   2.. Right side climber animation sequence index


;-----------------------------------------------------------------
; Now check to see if the climber's right arm should be out or in
Lb334:  NOP                             ; 192F 00       .
        LD      A,(R_CLIMBER_ANIM_IDX2) ; 1930 3A4981   :M. Right side climber arm in/out index
        LD      B,A                     ; 1933 47       G
        LD      A,(RINPUT_X_FLAG)       ; 1934 3A4281   :.. Get right stick X input flag
        ADD     A,B                     ; 1937 80       .
        LD      B,A                     ; 1938 47       G
; Note: This will only jump if the right arm is out (idx2 = 0) and right input is left (-1)
        JP      M,Lb337                 ; 1939 FA4519   .UI

; Note: This will only jump if right arm is in (idx2 = 1) and right input is right (1)
        SUB     $02                     ; 193C D602     ..
        JP      P,Lb337                 ; 193E F24519   .PI

; Update right arm out/in index
        LD      A,B                     ; 1941 78       x
        LD      (R_CLIMBER_ANIM_IDX2),A ; 1942 324981   2M. Right side climber arm in/out index


;-------------------------
; Check left arm up/down
Lb337:  LD      A,(L_CLIMBER_ANIM_IDX1) ; 1945 3A4A81   :K. Left side climber animation sequence index
        LD      B,A                     ; 1948 47       G
        LD      A,(LINPUT_Y_FLAG)       ; 1949 3A4581   :U.
        ADD     A,B                     ; 194C 80       .
        LD      B,A                     ; 194D 47       G
; Note: This will only jump if the left arm is fully down (idx1 = 0) and the left input is down (-1)
        JP      M,Lb338                 ; 194E FA8419   ..I

; Note: This will only jump if the left arm is fully up (idx1 = 4) and the left input is up (1)
        SUB     $05                     ; 1951 D605     ..
        JP      P,Lb338                 ; 1953 F28419   ..I

        LD      A,B                     ; 1956 78       x
        CP      $01                     ; 1957 FE01     ..  Passing through middle arm movement?
        JR      NZ,Lb339                ; 1959 2011      A

; Passing through middle arm movement up
        LD      A,(L_CLIMBER_ANIM_IDX1) ; 195B 3A4A81   :K. Left side climber animation sequence index
        CP      $00                     ; 195E FE00     .D  Is the left arm fully down?
        JR      NZ,Lb340                ; 1960 201E      .  Nope, go here

; Move left arm sprite up 4
        LD      A,($813C)               ; 1962 3A3C81   :h. Climber left arm Y position
        ADD     A,$04                   ; 1965 C604     .T
        LD      ($813C),A               ; 1967 323C81   2-.
        JR      Lb340                   ; 196A 1814     .@

Lb339:  LD      A,B                     ; 196C 78       x
        CP      $00                     ; 196D FE00     .D
        JR      NZ,Lb340                ; 196F 200F      N

; Passing through middle arm movement down
        LD      A,(L_CLIMBER_ANIM_IDX1) ; 1971 3A4A81   :K. Left side climber animation sequence index
        CP      $01                     ; 1974 FE01     ..  Is left arm in the middle?
        JR      NZ,Lb340                ; 1976 2008      L  Nope, go here

; Move left arm sprite down 4
        LD      A,($813C)               ; 1978 3A3C81   :h. Climber left arm Y position
        SUB     $04                     ; 197B D604     .T
        LD      ($813C),A               ; 197D 323C81   2-. 

Lb340:  LD      A,B                     ; 1980 78       x
        LD      (L_CLIMBER_ANIM_IDX1),A ; 1981 324A81   2K. Left side climber animation sequence index

;-----------------------------------------------------------------
; Now check to see if the climber's left arm should be out or in
Lb338:  LD      A,(L_CLIMBER_ANIM_IDX2) ; 1984 3A4B81   :^. Left side climber arm in/out index
        LD      B,A                     ; 1987 47       G
        LD      A,(LINPUT_X_FLAG)       ; 1988 3A4481   :.. Get left stick X input flag
        ADD     A,B                     ; 198B 80       .
        LD      B,A                     ; 198C 47       G
; Note: This will only jump if the left arm is in (idx2 = 0) and left input is left (-1)
        JP      M,Lb341                 ; 198D FA9919   ..I

; Note: This will only jump if left arm is out (idx2 = 1) and left input is right (1)
        SUB     $02                     ; 1990 D602     ..
        JP      P,Lb341                 ; 1992 F29919   ..I

; Update the left arm in/out index
        LD      A,B                     ; 1995 78       x
        LD      (L_CLIMBER_ANIM_IDX2),A ; 1996 324B81   2^. Left side climber animation sequence index


;---------------------------
; Climber sprite animation
Lb341:  NOP                             ; 1999 00       .

; Right side animation
        LD      A,(R_CLIMBER_ANIM_IDX1) ; 199A 3A4881   :..  Idx1 - Right side climber animation sequence index1
        RLCA                            ; 199D 07       .
        RLCA                            ; 199E 07       .
        LD      C,A                     ; 199F 4F       O    C = 4 * Idx1
        LD      A,(R_CLIMBER_ANIM_IDX2) ; 19A0 3A4981   :M.  Idx2 - Right side climber arm in/out index
        RLCA                            ; 19A3 07       .
        ADD     A,C                     ; 19A4 81       .    
        LD      C,A                     ; 19A5 4F       O    C = (4*Idx1) + (2*Idx2)
        LD      B,$00                   ; 19A6 0600     .D
        LD      HL,CC_RIGHT_ANIMATION_DATA ; 19A8 21D319 !.I Point to right animation data table
        ADD     HL,BC                   ; 19AB 09       .    HL = $19D3 + (4*Idx1) + (2*Idx2)

        LD      A,(HL)                  ; 19AC 7E       ~
        LD      (CLIMBER_RARM_CTRL),A   ; 19AD 323E81   2{.  Save right arm code / inversion value
        INC     HL                      ; 19B0 23       #
        LD      A,(HL)                  ; 19B1 7E       ~
        LD      (CLIMBER_RLEG_CTRL),A   ; 19B2 323681   2..  Save right leg code / inversion value

; Left side animation
        LD      A,(L_CLIMBER_ANIM_IDX1) ; 19B5 3A4A81   :K. Idx1 - Left side climber animation sequence index1
        RLCA                            ; 19B8 07       .
        RLCA                            ; 19B9 07       .
        LD      C,A                     ; 19BA 4F       O   C = 4 * Idx1
        LD      A,(L_CLIMBER_ANIM_IDX2) ; 19BB 3A4B81   :.. Idx2 - Left side climber arm in/out index
        RLCA                            ; 19BE 07       . 
        ADD     A,C                     ; 19BF 81       .
        LD      C,A                     ; 19C0 4F       O   C = (4*Idx1) + (2*Idx2)
        LD      B,$00                   ; 19C1 0600     .D
        LD      HL,CC_LEFT_ANIMATION_DATA ; 19C3 21E719 !.I Point to left animation data table
        ADD     HL,BC                   ; 19C6 09       .   HL = $19E7 + (4*Idx1) + (2*Idx2)
        LD      A,(HL)                  ; 19C7 7E       ~
        LD      (CLIMBER_LARM_CTRL),A   ; 19C8 323A81   2n. Save left arm code / inversion value
        INC     HL                      ; 19CB 23       #
        LD      A,(HL)                  ; 19CC 7E       ~
        LD      (CLIMBER_LLEG_CTRL),A   ; 19CD 323281   2'. Save left leg code / inversion value
        RET                             ; 19D0 C9       .   End ANIMATE_CLIMBER


;-------------------------------------------------------------------------------
; Data for climber animation
; Range: $19D1 - $19FC
;-------------------------------------------------------------------------------

        .db     $C7, $FB		; Start data block

; $19D3 - Right climber animation sprite codes
CC_RIGHT_ANIMATION_DATA:
								; Idx1	Idx2	Arm position
								; ----	----	-----------------
        .db     $30, $3A		; 0		0		Fully down, out
		.db     $35, $3B		; 0		1		Fully down, in

		.db     $31, $3C		; 1		0		Middle, out
		.db     $36, $3D		; 1		1		Middle, in

        .db     $32, $3E		; 2		0		Up more, out
		.db     $37, $3F		; 2		1		Up more, in

		.db     $33, $3E		; 3		0		Up even more, out
		.db     $38, $3D		; 3		1		Up even more, in

        .db     $34, $3C		; 4		0		Fully up, out
		.db     $39, $3B		; 4		1		Fully up, in

; $19E7 - Left climber animation sprite codes (same as above, but x-inverted
CC_LEFT_ANIMATION_DATA:
								; Idx1	Idx2	Arm position
								; ----	----	-----------------
		.db     $75, $7B		; 0		0		Fully down, in
		.db     $70, $7A		; 0		1		Fully down, out

        .db     $76, $7D		; 1		0		Middle, in
		.db     $71, $7C		; 1		1		Middle, out

		.db     $77, $7F		; 2		0		Up more, in
		.db     $72, $7E		; 2		1		Up more, out

        .db     $78, $7D		; 3		0		Up even more, in
		.db     $73, $7E		; 3		1		Up even more, out

		.db     $79, $7B		; 4		0		Fully up, in
		.db     $74, $7C		; 4		1		Fully up, out

        .db     $C7, $F3		; End data block



;=============================================================================
; Checks the new possible hand 
;
; Input:
;	B - Contains new possible arm Y position
;	C - Contains new possible arm X position
;
; Output:
;	A - 0 - Could not go to new position
;	A - 1 - Could move to new position
;=============================================================================
Lb348:  NOP                             ; 19FD 00       .
        LD      A,(FLOOR_NUM)           ; 19FE 3A3181   :a. Get the working floor number
        SUB     B                       ; 1A01 90       .   Subtract new Y position
        LD      B,A                     ; 1A02 47       G
        AND     $0F                     ; 1A03 E60F     .N  Is value = 0?
        JR      NZ,Lb344                ; 1A05 2042      C  Nope, return (A = 0)

        LD      A,(RANDOM_NUMBER)        ; 1A07 3A2281   :g. Get random number
        BIT     0,A                     ; 1A0A CB47     .G	Is it even?
        JR      Z,Lb345                 ; 1A0C 280A     (.	Yes, go here


; Update the row value in the window update FIFO
        LD      A,B                     ; 1A0E 78       x   Get value
        RRCA                            ; 1A0F 0F       .   Divide by 16
        RRCA                            ; 1A10 0F       .
        RRCA                            ; 1A11 0F       .
        RRCA                            ; 1A12 0F       .
        AND     $0F                     ; 1A13 E60F     .N
        LD      (WINDOW_ROW_COL_FIFO+$1E),A ; 1A15 32D982   2.}	Put new row in the FIFO

Lb345:  LD      A,B                     ; 1A18 78       x   Get value
        RRCA                            ; 1A19 0F       .   Divide by 2
        AND     $F8                     ; 1A1A E6F8     ..  Mask bits 0 - 2
        LD      B,A                     ; 1A1C 47       G   

        LD      A,C                     ; 1A1D 79       y   Get new sprite X position
        RRCA                            ; 1A1E 0F       .   Divide by 8
        RRCA                            ; 1A1F 0F       .
        RRCA                            ; 1A20 0F       .
        AND     $1F                     ; 1A21 E61F     ..
        LD      HL,$1A55                ; 1A23 21551A   !.N Point to table
        LD      E,A                     ; 1A26 5F       _
        LD      D,$00                   ; 1A27 1600     .D
        ADD     HL,DE                   ; 1A29 19       .   HL = $1A55 + (NewXPos / 8)
        LD      A,(HL)                  ; 1A2A 7E       ~
        LD      C,(HL)                  ; 1A2B 4E       N

; Check for a valid X position
        CP      $FF                     ; 1A2C FEFF     ..  Is table value $FF?
        JR      Z,Lb344                 ; 1A2E 2819     (I  Yes, return (A = 0)

        LD      HL,PLAYFIELD			; 1A30 218181   !..	Point to the playfield
        LD      A,B                     ; 1A33 78       x
        LD      E,A                     ; 1A34 5F       _
        LD      D,$00                   ; 1A35 1600     .D
        ADD     HL,DE                   ; 1A37 19       .   HL = PLAYFIELD + offset into playfield
        LD      E,C                     ; 1A38 59       Y
        ADD     HL,DE                   ; 1A39 19       .
        LD      A,(HL)                  ; 1A3A 7E       ~   Get value from table

; If the window value is $05 - $0B or $FF, we cannot go there, return 0
; Otherwise, save the C

        CP      $FF                     ; 1A3B FEFF     ..  Is value $FF?
        JR      Z,Lb344                 ; 1A3D 280A     (O  Yes, return with A = 0

        CP      $05                     ; 1A3F FE05     ..  Is value < 5?
        JP      M,Lb346                 ; 1A41 FA4C1A   .HN Yes, return with A = 1

        CP      $0C                     ; 1A44 FE0C     ..  Is value >= 12?
        JP      P,Lb346                 ; 1A46 F24C1A   ... Yes, return with A = 1

Lb344:  LD      A,$00                   ; 1A49 3E00     >D  Return with A = 0
        RET                             ; 1A4B C9       .

; Update the column value in the window update FIFO
Lb346:  LD      A,C                     ; 1A4C 79       y   Get valid window column (1 - 6)
        LD      (WINDOW_ROW_COL_FIFO+$1F),A ; 1A4D 32DA82   2.} Put new column in the FIFO
        LD      A,$01                   ; 1A50 3E01     >.  Return with A = 1
        RET                             ; 1A52 C9       .

;-------------------------------------------------------------------------------
; Data Start
; Range: $1A53 - $1A76
;-------------------------------------------------------------------------------

        .db     $C7, $FB

; $1A55 - Valid window location mask?
; $FF's are invalid values
; There are 6 valid columns of windows possible
; 1 - far left, 6 - far right
;
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF
		.db     $01, $01		; Index 10, 11 (X position 80, 88)
		.db     $FF
		.db     $02, $02		; Index 13, 14 (X pos. 104, 112)
		.db     $FF
        .db     $03, $03		; Index 16, 17 (X pos. 128, 136)
		.db     $FF
		.db     $04, $04		; Index 19, 20 (X pos. 152, 160)
		.db     $FF
		.db     $05, $05		; Index 22, 23 (X pos. 176, 184)
		.db     $FF
		.db     $06, $06		; Index 25, 26 (X pos. 200, 208)
		.db     $FF, $FF, $FF, $FF, $FF


        .db     $C7, $F3

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------


;=============================================================================
; Checks the allowed movement for each climber hand and sets the
; RHAND_MOVEMENT_FLAG & LHAND_MOVEMENT_FLAG properly.
;
;=============================================================================
CHECK_ALLOWED_HAND_MOVES:

;-----------------
; Check left hand
        NOP                             ; 1A77 00       .
        LD      IX,$9898                ; 1A78 DD219898 .!.. Point to sprite control for climber left arm

; Note: The sprite code for the climber's arm should range from $30 - $39
; This would be an index of 0 - 9 when anded with $0F
        LD      A,(IX+$00)              ; 1A7C DD7E00   .~D  Get the sprite number
        AND     $0F                     ; 1A7F E60F     .N   Mask off bits 0 - 3 (Range 0 - 9)
        RLCA                            ; 1A81 07       .    Multiply by 2
        AND     $1E                     ; 1A82 E61E     ..   
        LD      IY,$1AE9                ; 1A84 FD21E91A .!.N Point to table
        LD      E,A                     ; 1A88 5F       _
        LD      D,$00                   ; 1A89 1600     .D
        ADD     IY,DE                   ; 1A8B FD19     ..   IY = $1AE9 + (2*IDX)

        LD      A,(IX+$02)              ; 1A8D DD7E02   .~.  Get left arm Y position
        ADD     A,(IY+$00)              ; 1A90 FD8600   ..D  Add it to the table value
        LD      B,A                     ; 1A93 47       G
        LD      A,(IX+$03)              ; 1A94 DD7E03   .~.  Get left arm X position
        ADD     A,(IY+$01)              ; 1A97 FD8601   ...  Add it to the next table value
        LD      C,A                     ; 1A9A 4F       O
        CALL    Lb348                   ; 1A9B CDFD19   ..I  Check new position (returns A = 1 if it is OK to move there)

        LD      (RHAND_MOVEMENT_FLAG),A ; 1A9E 324781   2B.  Save allowed to move flag

        LD      A,(RANDOM_NUMBER)       ; 1AA1 3A2281   :g.  Get a random number
        ADD     A,$01                   ; 1AA4 C601     ..   Increment value
        LD      (RANDOM_NUMBER),A       ; 1AA6 322281   2&.  Save new value


;------------------
; Check right hand
        LD      IX,$989C                ; 1AA9 DD219C98 .!c. Point to sprite control for climber right arm

; Note: The sprite code for the climber's arm should range from $30 - $39
; This would be an index of 0 - 9 when anded with $0F
        LD      A,(IX+$00)              ; 1AAD DD7E00   .~D  Get the sprite number
        AND     $0F                     ; 1AB0 E60F     ..   Mask off bits 0 - 3
        RLCA                            ; 1AB2 07       .    Multiply by 2
        AND     $1E                     ; 1AB3 E61E     .[
        LD      IY,$1AD5                ; 1AB5 FD21D51A .!.. Point to table
        LD      E,A                     ; 1AB9 5F       _
        LD      D,$00                   ; 1ABA 1600     .D
        ADD     IY,DE                   ; 1ABC FD19     ..   IY = $1AD5 + (2*IDX)

        LD      A,(IX+$02)              ; 1ABE DD7E02   .~G  Get right arm Y position
        ADD     A,(IY+$00)              ; 1AC1 FD8600   ..D  Add it to the table value
        LD      B,A                     ; 1AC4 47       G
        LD      A,(IX+$03)              ; 1AC5 DD7E03   .~S  Get right arm X position
        ADD     A,(IY+$01)              ; 1AC8 FD8601   ...  Add it to the next table value
        LD      C,A                     ; 1ACB 4F       O

        CALL    Lb348                   ; 1ACC CDFD19   ..I  Check new position (return A = 1 if it is OK to move there)

        LD      (LHAND_MOVEMENT_FLAG),A ; 1ACF 324681   2..  Save allowed to move flag
        RET                             ; 1AD2 C9       .    End CHECK_ALLOWED_HAND_MOVES


;-------------------------------------------------------------------------------
; Data Start
; Range: $1AD3 - $1AFE
;-------------------------------------------------------------------------------

        .db     $C7, $FB		; Start data block

; $1AD5 - Right arm Y, X additive offsets
        .db     $02, $0B	; Index 0  Arm fully down, out
		.db     $02, $0B	; Index 1  Arm extending, out
		.db     $06, $0B	; Index 2  ...
		.db     $0A, $0B	; Index 3  ...
        .db     $0E, $0B	; Index 4  Arm fully up, out

		.db     $02, $03	; Index 5  Arm fully down, in
		.db     $02, $03	; Index 6  Arm extending, in
		.db     $06, $03	; Index 7  ...
        .db     $0A, $03	; index 8  ...
		.db     $0E, $03	; Index 9  Arm fully up, in


; $1AE9 - Left arm Y, X additive offsets
		.db     $02, $04	; Index 0  Arm fully down, out
		.db     $02, $04	; Index 1  Arm extending, out
        .db     $06, $04	; Index 2  ...
		.db     $0A, $04	; Index 3  ...
		.db     $0E, $04	; Index 4  Arm fully up, out

		.db     $02, $0C	; Index 5  Arm fully down, in
        .db     $02, $0C	; Index 6  Arm extending, in
		.db     $06, $0C	; Index 7  ...
		.db     $0A, $0C	; Index 8  ...
		.db     $0E, $0C	; Index 9  Arm fully up, in

        .db     $C7, $F3		; End data block

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------


        NOP                             ; 1AFF 00       .
        NOP                             ; 1B00 00       .
        NOP                             ; 1B01 00       .
        NOP                             ; 1B02 00       .
        NOP                             ; 1B03 00       .
        NOP                             ; 1B04 00       .
        NOP                             ; 1B05 00       .
        NOP                             ; 1B06 00       .
        NOP                             ; 1B07 00       .
        NOP                             ; 1B08 00       .
        NOP                             ; 1B09 00       .
        NOP                             ; 1B0A 00       .
        NOP                             ; 1B0B 00       .
        NOP                             ; 1B0C 00       .
        NOP                             ; 1B0D 00       .
        NOP                             ; 1B0E 00       .
        NOP                             ; 1B0F 00       .
        NOP                             ; 1B10 00       .
        NOP                             ; 1B11 00       .
        NOP                             ; 1B12 00       .
        NOP                             ; 1B13 00       .
        NOP                             ; 1B14 00       .
        NOP                             ; 1B15 00       .
        NOP                             ; 1B16 00       .
        NOP                             ; 1B17 00       .
        NOP                             ; 1B18 00       .
        NOP                             ; 1B19 00       .
        NOP                             ; 1B1A 00       .
        NOP                             ; 1B1B 00       .
        NOP                             ; 1B1C 00       .
        NOP                             ; 1B1D 00       .
        NOP                             ; 1B1E 00       .
        NOP                             ; 1B1F 00       .
        NOP                             ; 1B20 00       .
        NOP                             ; 1B21 00       .
        NOP                             ; 1B22 00       .
        NOP                             ; 1B23 00       .
        NOP                             ; 1B24 00       .
        NOP                             ; 1B25 00       .
        NOP                             ; 1B26 00       .
        NOP                             ; 1B27 00       .
        NOP                             ; 1B28 00       .
        NOP                             ; 1B29 00       .
        NOP                             ; 1B2A 00       .
        NOP                             ; 1B2B 00       .
        NOP                             ; 1B2C 00       .
        NOP                             ; 1B2D 00       .
        NOP                             ; 1B2E 00       .
        NOP                             ; 1B2F 00       .
        NOP                             ; 1B30 00       .
        NOP                             ; 1B31 00       .
        NOP                             ; 1B32 00       .
        NOP                             ; 1B33 00       .
        NOP                             ; 1B34 00       .
        NOP                             ; 1B35 00       .
        NOP                             ; 1B36 00       .
        NOP                             ; 1B37 00       .
        NOP                             ; 1B38 00       .
        NOP                             ; 1B39 00       .
        NOP                             ; 1B3A 00       .
        NOP                             ; 1B3B 00       .
        NOP                             ; 1B3C 00       .
        NOP                             ; 1B3D 00       .
        NOP                             ; 1B3E 00       .
        NOP                             ; 1B3F 00       .

;-----------------------------------------------------------------------------
; Called from $02B7
; (Index 2 in the jump table)
;
; Address $1B40
;-----------------------------------------------------------------------------
ISR_JUMP2:
        NOP                             ; 1B40 00       .
        LD      A,(ISR_MODE_IDX)        ; 1B41 3A5B81   :^.	Get the ISR mode index
        CP      $01                     ; 1B44 FE01     ..	Are we starting to climb a building?
        JR      Z,Lb349                 ; 1B46 282A     (.	Yes, go here

        CP      $02                     ; 1B48 FE02     ..
        JP      Z,Lb350                 ; 1B4A CA211C   .0.

        LD      A,$01                   ; 1B4D 3E01     >.
        CALL    Lb255                   ; 1B4F CD2103   .4S

        LD      A,$03                   ; 1B52 3E03     >S
        CALL    Lb255                   ; 1B54 CD2103   .0.

        CALL    INIT_VIDEO              ; 1B57 CD2505   .0U  Initialize the video

        LD      A,$10                   ; 1B5A 3E10     >.
        LD      ($82AD),A               ; 1B5C 32AD82   2..
        LD      A,$F8                   ; 1B5F 3EF8     >.
        LD      ($817E),A               ; 1B61 327E81   2..

        CALL    SHOW_START_BLDG_SCREEN  ; 1B64 CD141D   .@X

        CALL    SHOW_BLDG_NAME          ; 1B67 CD941C   ..H  Display the building sign

        LD      A,$01                   ; 1B6A 3E01     >.	Set the mode index to start climbing a building
        LD      (ISR_MODE_IDX),A        ; 1B6C 325B81   2..	

        CALL    Lb208                   ; 1B6F CD0F03   .NS Does not return from this call


Lb349:  LD      HL,(CUR_FLOOR_NUM)      ; 1B72 2AE880   *.. Get the current floor number and group (2 values)
        LD      DE,$FF00                ; 1B75 1100FF   .D.
        ADD     HL,DE                   ; 1B78 19       .
        LD      A,L                     ; 1B79 7D       }
        AND     $F0                     ; 1B7A E6F0     ..
        LD      L,A                     ; 1B7C 6F       o
        LD      (CUR_FLOOR_NUM),HL      ; 1B7D 22E880   ".. Update the current floor number and group (2 values)
        LD      A,L                     ; 1B80 7D       }
        CPL                             ; 1B81 2F       /
        AND     H                       ; 1B82 A4       .
        CP      $FF                     ; 1B83 FEFF     ..
        JP      Z,Lb353                 ; 1B85 CA141C   ..H

        LD      A,(CUR_FLOOR_GROUP)     ; 1B88 3AE980   :.. Get the current floor group
        CP      $F4                     ; 1B8B FEF4     ..
        JR      NZ,Lb354                ; 1B8D 3006     0.

        LD      HL,$F3D0                ; 1B8F 21D0F3   !..
        LD      (CUR_FLOOR_NUM),HL      ; 1B92 22E880   ".. Update the current floor number and group (2 values)

Lb354:  LD      A,$FF                   ; 1B95 3EFF     >.
        LD      ($814C),A               ; 1B97 324C81   2H.

        CALL    Lb355                   ; 1B9A CDDE26   ..3

        CALL    SCROLL_BUILDING         ; 1B9D CDD026   ..g Scroll the building

        CALL    UPDATE_BIG_SPRITE_Y_POS ; 1BA0 CDFB1C   ...

        LD      A,$00                   ; 1BA3 3E00     >D
        CALL    DELAY                   ; 1BA5 CDB802   ... Delay

        LD      HL,(CUR_FLOOR_NUM)      ; 1BA8 2AE880   *.. Get the current floor number and group (2 values)
        INC     HL                      ; 1BAB 23       #
        LD      (CUR_FLOOR_NUM),HL      ; 1BAC 22E880   ".. Update the current floor number and group (2 values)
        LD      A,H                     ; 1BAF 7C       |
        OR      L                       ; 1BB0 B5       .
        JR      NZ,Lb354                ; 1BB1 20E2      .

        CALL    Lb358                   ; 1BB3 CDD514   .*@

        CALL    CHECK_ALLOWED_HAND_MOVES ; 1BB6 CD771A   .#.

        LD      A,(LHAND_MOVEMENT_FLAG) ; 1BB9 3A4681   :.. Is left hand allowed to move?
        AND     A                       ; 1BBC A7       .
        JR      NZ,Lb359                ; 1BBD 2012      .  Yes, go here

        LD      B,$10                   ; 1BBF 0610     ..  Nope - Loop 16 times

Lb360:  PUSH    BC                      ; 1BC1 C5       .   Save BC
        LD      A,$01                   ; 1BC2 3E01     >.
        LD      ($814C),A               ; 1BC4 324C81   2..

        CALL    Lb355                   ; 1BC7 CDDE26   ..g

        CALL    SCROLL_BUILDING         ; 1BCA CDD026   ..3 Scroll the building

        POP     BC                      ; 1BCD C1       .   Restore BC (B is loop counter)
        DEC     B                       ; 1BCE 05       .   Decrement counter
        JR      NZ,Lb360                ; 1BCF 20F0      .  Done? Nope, keep looping

; Left hand allowed to move
Lb359:  XOR     A                       ; 1BD1 AF       .
        LD      ($814C),A               ; 1BD2 324C81   2..

        CALL    CHECK_ALLOWED_HAND_MOVES ; 1BD5 CD771A   ."N

        LD      A,(LHAND_MOVEMENT_FLAG) ; 1BD8 3A4681   :R. Is left hand allowed to move?
        AND     A                       ; 1BDB A7       .
        JR      NZ,Lb361                ; 1BDC 2020      d  Yes, go here

; Left hand not allowed to move
        LD      A,$48                   ; 1BDE 3E48     >.
        LD      (CLIMBER_X_POS),A       ; 1BE0 32E780   2..  Set climber X position
        LD      B,$06                   ; 1BE3 0606     ..   Loop 6 times

Lb362:  PUSH    BC                      ; 1BE5 C5       .    Save BC

        CALL    Lb358                   ; 1BE6 CDD514   ...

        CALL    CHECK_ALLOWED_HAND_MOVES ; 1BE9 CD771A   ."N

        LD      A,(LHAND_MOVEMENT_FLAG) ; 1BEC 3A4681   :R.  Is left hand allowed to move?
        AND     A                       ; 1BEF A7       .
        JR      NZ,Lb361                ; 1BF0 200C      .   Yes, go here (break out of loop)

; Move climber to right
        LD      A,(CLIMBER_X_POS)       ; 1BF2 3AE780   :..
        ADD     A,$18                   ; 1BF5 C618     ..
        LD      (CLIMBER_X_POS),A       ; 1BF7 32E780   2..
        POP     BC                      ; 1BFA C1       .   Restore BC (B is loop counter)
        DEC     B                       ; 1BFB 05       .   Decrement counter
        JR      NZ,Lb362                ; 1BFC 20E7      .  Done? Nope, keep looping

Lb361:  LD      A,$02                   ; 1BFE 3E02     >.
        LD      (ISR_MODE_IDX),A        ; 1C00 325B81   2..
        LD      A,(FLOOR_GROUP_IDX)     ; 1C03 3ADC80   :.. Get the current floor group
        RRCA                            ; 1C06 0F       .
        RRCA                            ; 1C07 0F       .
        AND     $3F                     ; 1C08 E63F     ..
        ADD     A,$01                   ; 1C0A C601     ..
        LD      ($82DB),A               ; 1C0C 32DB82   2..
        LD      A,$FF                   ; 1C0F 3EFF     >.
        LD      ($82AD),A               ; 1C11 32AD82   2.}

Lb353:  LD      A,$01                   ; 1C14 3E01     >.

        CALL    Lb223                   ; 1C16 CD6503   .p.

        LD      A,$03                   ; 1C19 3E03     >.
        CALL    Lb223                   ; 1C1B CD6503   .uS

        CALL    Lb208                   ; 1C1E CD0F03   ... Does not return from this call

Lb350:  CALL    UPDATE_BIG_SPRITE_Y_POS ; 1C21 CDFB1C   ..H

        LD      A,($82AD)               ; 1C24 3AAD82   :..
        DEC     A                       ; 1C27 3D       =
        JR      NZ,Lb363                ; 1C28 200A      .

        CALL    UPDATE_WINDOWS          ; 1C2A CD7225   .'0	Update the playfiled windows

        LD      A,(BUILDING_NUMBER)     ; 1C2D 3ADF80   :..
        CPL                             ; 1C30 2F       /
        AND     $03                     ; 1C31 E603     ..
        INC     A                       ; 1C33 3C       <

Lb363:  LD      ($82AD),A               ; 1C34 32AD82   2..
        LD      A,$01                   ; 1C37 3E01     >.
        LD      (KEEP_SAME_ISR_FLAG),A  ; 1C39 324480   2@. Keep processing the same ISR table location
        CALL    Lb355                   ; 1C3C CDDE26   ..3
        CALL    SCROLL_BUILDING         ; 1C3F CDD026   ..g Scroll the building
        CALL    Lb365                   ; 1C42 CDA426   ..3

        XOR     A                       ; 1C45 AF       .
        LD      (KEEP_SAME_ISR_FLAG),A  ; 1C46 324480   2.. Process the next ISR table location
        LD      A,(ISR_COUNTER)         ; 1C49 3A4580   :U. Get ISR counter
        AND     $1F                     ; 1C4C E61F     ._  Are bits 4 - 0 zero?
        JR      NZ,Lb366                ; 1C4E 200F      .  Nope, continue

; Called every 0, 32, 64, 96, 128, 160, 192, 224 interrupt
        LD      A,(ISR_COUNTER)         ; 1C50 3A4580   :P. Get the ISR counter
        AND     $20                     ; 1C53 E620     .d  Is bit 5 set?
        JR      NZ,Lb367                ; 1C55 2005      .  Yes, go here

; Called every 0, 64, 128, 192 interrupt
        CALL    Lb368                   ; 1C57 CD6C1E   .h.
        JR      Lb366                   ; 1C5A 1803     .S

; Called every 32, 96, 160, 224 interrupt
Lb367:  CALL    Lb369                   ; 1C5C CD441E   ..[

Lb366:  LD      A,(GAME_IN_PROGRESS)    ; 1C5F 3A7580   :5. Is there a game in progress?
        OR      A                       ; 1C62 B7       .
        JR      Z,Lb370                 ; 1C63 2819     (I  Nope, go here

; Game in progress
        LD      A,(DIP_SW_RD)           ; 1C65 3A00B0   :D. Read the DIP switches
        AND     $08                     ; 1C68 E608     .L  Isolate test pattern bit
        JR      Z,Lb370                 ; 1C6A 2812     (F  Normal? Yes, go here

;-------------------------------------
; Rack test
; Continually go to the next building
;-------------------------------------
        LD      A,$01                   ; 1C6C 3E01     >.
        LD      (KEEP_SAME_ISR_FLAG),A  ; 1C6E 324480   2.. Keep processing the same ISR table location
        LD      B,$03                   ; 1C71 0603     ..
        CALL    PLAY_END_BLDG_SOUND     ; 1C73 CD811C   ..H Play the end of building sound

        LD      A,$01                   ; 1C76 3E01     >.
        LD      ($82AB),A               ; 1C78 32AB82   2T.
        CALL    GOTO_NEXT_BLDG          ; 1C7B CDB310   ... Go to next building

; No game in progress
Lb370:  CALL    Lb208                   ; 1C7E CD0F03   ... Does not return from this call


;=============================================================================
; Plays the end of building sound
;
; Loads a sound based on the building number.  Only bits 0 & 1 are used, so 
; the index ranges from 0 - 3.
;=============================================================================
PLAY_END_BLDG_SOUND:
        NOP                             ; 1C81 00       .
        LD      HL,$402                 ; 1C82 210204   !.T  Load HL
        LD      A,(BUILDING_NUMBER)     ; 1C85 3ADF80   :..  Get the building number
        AND     $03                     ; 1C88 E603     .S   Isolate bits 0 & 1 (Range: 0 - 3)
        LD      E,A                     ; 1C8A 5F       _    
        LD      D,$00                   ; 1C8B 1600     .D
        ADD     HL,DE                   ; 1C8D 19       .    HL = $0402 + ($03 & Building number)

        LD      B,H                     ; 1C8E 44       D    B = $04
        LD      C,L                     ; 1C8F 4D       M    C = 2, 3, 4, or 5
        CALL    LOAD_SOUND_DATA         ; 1C90 CDBB11   ..A  Load sound data
        RET                             ; 1C93 C9       .    End PLAY_END_BLDG_SOUND


;=============================================================================
; Shows the building name sign (at the bottom of each building).
; 
;=============================================================================
SHOW_BLDG_NAME:
        LD      IY,BIG_SPRITE_CTRL      ; 1C94 FD21DC98 .!.. Point to big sprite control
        LD      (IY+$00),$01            ; 1C98 FD360001 .6D. Sprite number / priority = 1
        LD      A,(BUILDING_NUMBER)     ; 1C9C 3ADF80   :..  Get the building number
        LD      E,A                     ; 1C9F 5F       _   
        LD      D,$00                   ; 1CA0 1600     .D
        LD      HL,BLDG_SIGN_COLOR_DATA ; 1CA2 21E11C   !..  Point to the building sign color data table
        ADD     HL,DE                   ; 1CA5 19       .    HL = BLDG_SIGN_COLOR_DATA + Building number
        LD      A,(HL)                  ; 1CA6 7E       ~    Get color value from table
        LD      (IY+$01),A              ; 1CA7 FD7701   .w.  Set big sprite color

; Copy image to big sprite RAM
        LD      A,(BUILDING_NUMBER)     ; 1CAA 3ADF80   :..  Get building number
        AND     $03                     ; 1CAD E603     ..   Set range from 0 - 3
        RLCA                            ; 1CAF 07       .    Multiply by 4
        RLCA                            ; 1CB0 07       .
        LD      E,A                     ; 1CB1 5F       _
        LD      HL,BLDG_SIGN_DATA       ; 1CB2 21E91C   !..  Building sign data table
        ADD     HL,DE                   ; 1CB5 19       .    Source: BLDG_SIGN_DATA + 4 * BuildingNumber
        LD      DE,$88F6                ; 1CB6 11F688   ...  Dest = $88F6 (Big sprite RAM)
        LD      B,$04                   ; 1CB9 0604     .T   Loop 4 times

Lb373:  LD      A,(HL)                  ; 1CBB 7E       ~    Get value from table
        LD      (DE),A                  ; 1CBC 12       .    Copy to destination
        INC     HL                      ; 1CBD 23       #    Go to next table location
        INC     DE                      ; 1CBE 13       .    Go to next RAM location
        DEC     B                       ; 1CBF 05       .    Decrement counter
        JR      NZ,Lb373                ; 1CC0 20F9      .   Done? No, keep looping

        LD      (IY+$02),$36            ; 1CC2 FD360236 .6G. Set big sprite Y position
        CALL    CHECK_FIELD_INVERSION   ; 1CC6 CD8311   .|A  See if the field is inverted
        AND     A                       ; 1CC9 A7       .
        JR      NZ,Lb375                ; 1CCA 200E      O   Normal field, go here

; Field is inverted
        LD      A,(IY+$01)              ; 1CCC FD7E01   .~.  Invert Y axis
        OR      $10                     ; 1CCF F610     ..   
        LD      (IY+$01),A              ; 1CD1 FD7701   .w.  
        LD      (IY+$03),$5B            ; 1CD4 FD36035B .6.. Set big sprite X position
        JR      Lb376                   ; 1CD8 1804     ..

; Normal field
Lb375:  LD      (IY+$03),$34            ; 1CDA FD360334 .6.` Set big sprite X position

Lb376:  RET                             ; 1CDE C9       .    End SHOW_BLDG_NAME


;-------------------------------------------------------------------------------
; Data for big sprite building name
;
; Each of these big sprites are used for showing the building sign at the
; start of the building.
; 
; Range: $1CDF - $1CFA
;-------------------------------------------------------------------------------

        .db     $C7, $FB									; Start data block

; $1CE1 - Sign colors
BLDG_SIGN_COLOR_DATA:
        .db     $07						; Building 1
		.db     $06						; Building 2
		.db     $05						; Building 3
		.db     $04						; Building 4
		.db     $04						; Building 5
		.db     $05						; Building 6
		.db     $06						; Building 7
		.db     $07						; Building 8

; $1CE9 - Table for building names
BLDG_SIGN_DATA:
        .db     $C0, $C1, $E0, $E1		; Building 1 - Nichibutsu
		.db     $C2, $C3, $E2, $E3		; Building 2 - Nichibutsu Leisure
        .db     $C4, $C5, $E4, $E5		; Building 3 - Nichibutsu USA CO.LTD
		.db     $C6, $C7, $E6, $E7		; Building 4 - Nichibutsu UK.LIMITED

        .db     $C7, $F3									; End data block




;=============================================================================
; Update Big Sprite Y position
;=============================================================================
UPDATE_BIG_SPRITE_Y_POS:  
        LD      A,(FLOOR_GROUP_IDX)     ; 1CFB 3ADC80   :.. Get the current floor group
        CP      $05                     ; 1CFE FE05     .U	Is the floor group <= 5?
        RET     NC                      ; 1D00 D0       .	Yes, return from UPDATE_BIG_SPRITE_Y_POS

        LD      IY,BIG_SPRITE_CTRL      ; 1D01 FD21DC98 .!.. Point to big sprite control
        LD      A,(IY+$02)              ; 1D05 FD7E02   .~.
        CP      $06                     ; 1D08 FE06     .G	Is the big sprite Y position <= 6?
        RET     NC                      ; 1D0A D0       .	Yes, return from UPDATE_BIG_SPRITE_Y_POS

        LD      (IY+$00),$00            ; 1D0B FD360000 .6DD	Priority? is zero
        LD      (IY+$02),$F0            ; 1D0F FD3602F0 .6..	Y position is -8?
        RET                             ; 1D13 C9       .	Done with UPDATE_BIG_SPRITE_Y_POS


;=============================================================================
; Shows the start building screen
;=============================================================================
SHOW_START_BLDG_SCREEN:
        NOP                             ; 1D14 00       .
        XOR     A                       ; 1D15 AF       .   
        LD      (FLOOR_NUM),A           ; 1D16 323181   2a. Clear the working floor number
        LD      (FLOOR_GROUP),A         ; 1D19 323081   21. Clear the working floor group
        LD      HL,COLOR_RAM            ; 1D1C 21009C   !D. Point to color RAM
        LD      BC,COLOR_RAM_SIZE       ; 1D1F 010004   .D. # bytes in color RAM

; Set building color
Lb379:  LD      A,(BUILDING_NUMBER)     ; 1D22 3ADF80   :.. Get building number
        RLCA                            ; 1D25 07       .   Multiply by 8
        RLCA                            ; 1D26 07       .
        RLCA                            ; 1D27 07       .
        AND     $08                     ; 1D28 E608     .L  Isolate bit 3
        OR      $07                     ; 1D2A F607     ..  Add 7 (Value is 7 or 15)
        LD      (HL),A                  ; 1D2C 77       w   Write color to color RAM
        INC     HL                      ; 1D2D 23       #   Go to next color ram byte
        DEC     BC                      ; 1D2E 0B       .   Decrement counter
        LD      A,B                     ; 1D2F 78       x
        OR      C                       ; 1D30 B1       .
        JR      NZ,Lb379                ; 1D31 20EF      .  Counter = 0?  Nope, keep looping

        CALL    UPDATE_GAME_SCORES      ; 1D33 CD6307   .6. Update the game scores
        CALL    SHOW_CURRENT_SCORE      ; 1D36 CDDD27   ..f Show the current scores on screen

; Display 1st 32 floors of the building (some are not visible)
        LD      C,$20                   ; 1D39 0E20     .d  Loop 32 times

Lb381:  LD      A,(FLOOR_NUM)           ; 1D3B 3A3181   :a. Subtract 8 from the working floor position
        SUB     $08                     ; 1D3E D608     .L
        LD      (FLOOR_NUM),A           ; 1D40 323181   2a. Save value
        PUSH    BC                      ; 1D43 C5       .   Save BC
        CALL    DRAW_BLDG_FLOOR         ; 1D44 CDFC1F   ... Draws the next building floor
        POP     BC                      ; 1D47 C1       .   Restore BC
        DEC     C                       ; 1D48 0D       .   Decrement loop counter
        JR      NZ,Lb381                ; 1D49 20F0      .  Done? Nope, keep looping

; Note: FLOOR_NUM is back to 0 at this point...

        CALL    DISPLAY_BORDER          ; 1D4B CDAF1F   .P_ Display border on left and right edges
        CALL    DISPLAY_BLDG_LEVEL      ; 1D4E CD671F   .b. Display the building number (flower pots)
        CALL    DISPLAY_LIVES           ; 1D51 CDDD1F   ."_ Display number of lives
        CALL    SHOW_BLDG_MAP           ; 1D54 CD2C1E   .=[ Show the building map on left side of screen
        LD      A,(CUR_FLOOR_GROUP)     ; 1D57 3AE980   :.. Get the current floor group
        OR      A                       ; 1D5A B7       .   Is it the beginning group?
        JR      NZ,Lb386                ; 1D5B 2003      .  Nope, continue

        CALL    SET_GAME_POINT_VALUES   ; 1D5D CDB01E   ... Set point values (step point, etc)

Lb386:  CALL    SHOW_STEP_PT_BONUS_RATE ; 1D60 CD0F1F   ...
        RET                             ; 1D63 C9       .


;=============================================================================
; Shows the requested building tile for the building map on the left of the
; play screen.  The building is 25 characters high.
;
; Input:
;	B - Offset into building, starting from ground floor (0 is bottom, 
;	    24 is top)
;=============================================================================
SHOW_BLDG_MAP_TILE:
        NOP                             ; 1D64 00       .
        PUSH    BC                      ; 1D65 C5       .    Save B and C
        LD      IX,BUILDING_MAP_TABLE   ; 1D66 DD21A61D .!.Y Point to the building map table
        LD      A,(BUILDING_NUMBER)     ; 1D6A 3ADF80   :..  Get the building number
        RLCA                            ; 1D6D 07       .    Multiply by 4
        RLCA                            ; 1D6E 07       .
        AND     $1F                     ; 1D6F E61F     ..   Limit to 31 max
        LD      E,A                     ; 1D71 5F       _    
        LD      D,$00                   ; 1D72 1600     .D
        ADD     IX,DE                   ; 1D74 DD19     ..   IX = BUILDING_MAP_TABLE + (4 * BuildingNumber)

; Get HL pointer from table
        LD      L,(IX+$00)              ; 1D76 DD6E00   .nD  
        LD      H,(IX+$01)              ; 1D79 DD6601   .f.

; Get map color value
        LD      C,(IX+$02)              ; 1D7C DD4E02   .NG

        LD      IX,$9380                ; 1D7F DD218093 .!.. IX = Bottom left of screen ram for the building map
        LD      IY,$9F80                ; 1D83 FD21809F .!.` IY = Bottom left of Screen Color for the building map
        LD      DE,-32                  ; 1D87 11E0FF   ...  Get ready to subtract 32 (for each row)
        LD      A,B                     ; 1D8A 78       x    Get B value
        OR      A                       ; 1D8B B7       .    Is B = 0?
        JR      Z,Lb389                 ; 1D8C 2808     (L   Yes, continue

; Each loop goes up one row
Lb390:  ADD     IX,DE                   ; 1D8E DD19     ..  Subtract 32 from IX
        ADD     IY,DE                   ; 1D90 FD19     ..  Subtract 32 from IY
        INC     HL                      ; 1D92 23       #   Go to next location
        DEC     B                       ; 1D93 05       .   Decrement counter
        JR      NZ,Lb390                ; 1D94 20F8      .  Done? Nope, keep looping

; Decode value at HL
Lb389:  LD      A,(HL)                  ; 1D96 7E       ~   Get value at HL
        RLCA                            ; 1D97 07       .   Multiply by 2
        AND     $06                     ; 1D98 E606     .G  Isolate bits 1 and 2
        ADD     A,-8                    ; 1D9A C6F8     ..  Subtract 8
        LD      (IX+$00),A              ; 1D9C DD7700   .wD Write building tile to screen RAM
        LD      (IY+$00),C              ; 1D9F FD7100   .qD Write color to screen RAM

        POP     BC                      ; 1DA2 C1       .   Restore B and C
        RET                             ; 1DA3 C9       .   Return


;-------------------------------------------------------------------------------
; Data for the building maps
;
; Range: $1DA4 - $1E2B
;-------------------------------------------------------------------------------

        .db     $C7, $FB				; Start data block

;-------------------------------------------------------------------------------
; 1DA6 - Building master table
;
; Each entry is 4 bytes long
; Offset	Comment
; ------	--------------------------------------------
; 0, 1		Pointer to the beginning of a building table
; 2			Color of building map
; 3			Always 0
;-------------------------------------------------------------------------------
BUILDING_MAP_TABLE:
        .db     $C6, $1D, $14, $00		; Building 1
		.db     $DF, $1D, $1C, $00		; Building 2
        .db     $F8, $1D, $14, $00		; Building 3
		.db     $11, $1E, $1C, $00		; Building 4
        .db     $C6, $1D, $14, $00		; Building 5
		.db     $DF, $1D, $1C, $00		; Building 6
        .db     $F8, $1D, $14, $00		; Building 7
		.db     $11, $1E, $1C, $00		; Building 8 (this loops around again to 1)

; $1DC6 - Building 1 & 5 (1st value is bottom of building)
        .db     $00, $00, $03, $00, $00, $02, $00, $00
        .db     $00, $03, $00, $00, $00, $03, $00, $00
        .db     $00, $02, $02, $00, $00, $03, $00, $00
        .db     $00

; $1DDF - Building 2 & 6
		.db     $00, $01, $02, $02, $02, $02, $01, $00
		.db     $03, $03, $03, $03, $01, $01, $01, $01
		.db     $03, $03, $01, $01, $01, $01, $01, $01
		.db     $01

; $1DF8 - Building 3 & 7
		.db     $00, $00, $00, $03, $03, $03, $00, $03
		.db     $00, $00, $03, $01, $01, $01, $01, $01
		.db     $01, $02, $02, $02, $02, $02, $02, $02
		.db     $02
		
; $1E11 - Building 4 & 8
		.db     $00, $03, $00, $03, $03, $03, $03, $00
		.db     $00, $02, $02, $00, $00, $00, $01, $01
		.db     $02, $01, $03, $03, $03, $03, $03, $03
		.db     $03

        .db     $C7, $F3				; End data block

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------

;=============================================================================
; Shows the entire building map
;=============================================================================
SHOW_BLDG_MAP:
        NOP                             ; 1E2C 00       .
        LD      B,$00                   ; 1E2D 0600     .D  Start at bottom of building

Lb403:  CALL    SHOW_BLDG_MAP_TILE      ; 1E2F CD641D   .`Y Show tile
        INC     B                       ; 1E32 04       .   Go to next tile (move up building)
        LD      A,B                     ; 1E33 78       x
        CP      $19                     ; 1E34 FE19     .I  At 25th tile?
        JR      NZ,Lb403                ; 1E36 20F7      .  Nope, keep looping

; Clear 2 spaces above, 1 below building map
        LD      A,$4E                   ; 1E38 3E4E     >Z  Blank character
        LD      ($9040),A               ; 1E3A 324090   2.. Save at top left
        LD      ($9060),A               ; 1E3D 326090   2q. Next row, left
        LD      ($93A0),A               ; 1E40 32A093   2_. Bottom, left
        RET                             ; 1E43 C9       .   End SHOW_BLDG_MAP


;=============================================================================
; Displays the current user position on the building map???
;=============================================================================
Lb369:  NOP                             ; 1E44 00       .
        LD      A,(FLOOR_NUM)           ; 1E45 3A3181   :a. Get the working floor number
        NEG                             ; 1E48 ED44     .D	Make this a negative number
        LD      L,A                     ; 1E4A 6F       o	L = -FLOOR_NUM
        LD      A,(FLOOR_GROUP)         ; 1E4B 3A3081   :1. Get the working floor group
        NEG                             ; 1E4E ED44     .D	Make this a negative number
        LD      H,A                     ; 1E50 67       g	H = -FLOOR_GROUP
        LD      DE,$40                  ; 1E51 114000   .QD	DE = $40 (64)
        ADD     HL,DE                   ; 1E54 19       .	L = -FLOOR_NUM + $40
        LD      A,L                     ; 1E55 7D       }	A = -FLOOR_NUM + $40
        RLCA                            ; 1E56 07       .	A = 2 * ($40 - FLOOR_NUM)
        AND     $01                     ; 1E57 E601     ..	A = A & $01
        LD      D,A                     ; 1E59 57       W	D = A
        LD      A,H                     ; 1E5A 7C       |	A = -FLOOR_GROUP
        RLCA                            ; 1E5B 07       .	A = 2 * (-FLOOR_GROUP)
        AND     $1E                     ; 1E5C E61E     ..	Limit to 30
        ADD     A,D                     ; 1E5E 82       .	A = A + D
        LD      B,A                     ; 1E5F 47       G	B = A
        OR      A                       ; 1E60 B7       .	is A Zero?
        JR      Z,Lb404                 ; 1E61 2805     (.	Yes, go here

        DEC     B                       ; 1E63 05       .	B = B -1
        CALL    SHOW_BLDG_MAP_TILE      ; 1E64 CD641D   .1X	Show this tile
        INC     B                       ; 1E67 04       .	B = B + 1

Lb404:  CALL    SHOW_BLDG_MAP_TILE      ; 1E68 CD641D   .1X	Show this tile (B is the tile)
        RET                             ; 1E6B C9       .


;=============================================================================
; Input:
;	IX
;	IY
;=============================================================================
Lb368:  NOP                             ; 1E6C 00       .
        CALL    Lb369                   ; 1E6D CD441E   .@.
        LD      A,(FLOOR_NUM)           ; 1E70 3A3181   :a. Get the working floor number
        NEG                             ; 1E73 ED44     .D
        ADD     A,$40                   ; 1E75 C640     .Q  A = A - (FLOOR_NUM)
        RRCA                            ; 1E77 0F       .   Divide by 16
        RRCA                            ; 1E78 0F       .
        RRCA                            ; 1E79 0F       .
        RRCA                            ; 1E7A 0F       .
        AND     $06                     ; 1E7B E606     ..  Isolate bits 1 & 2
        LD      E,A                     ; 1E7D 5F       _   
        LD      A,(IX+$00)              ; 1E7E DD7E00   .~D
        SUB     $F8                     ; 1E81 D6F8     ..
        RLCA                            ; 1E83 07       .
        RLCA                            ; 1E84 07       .
        AND     $18                     ; 1E85 E618     ..
        ADD     A,E                     ; 1E87 83       .
        ADD     A,$60                   ; 1E88 C660     .4
        LD      (IX+$00),A              ; 1E8A DD7700   .wD
        LD      A,($8141)               ; 1E8D 3A4181   :.. Climber right arm sprite X position
        CP      $7C                     ; 1E90 FE7C     .,  Is position < 124?
        RET     C                       ; 1E92 D8       .   Yes, return

        CP      $94                     ; 1E93 FE94     ..  Is position < 148?
        JR      C,Lb405                 ; 1E95 3815     8P  Yes, go here

        CP      $AC                     ; 1E97 FEAC     ..  Is position < 172?
        JR      C,Lb406                 ; 1E99 3809     8.  Yes, go here

        LD      A,(IY+$00)              ; 1E9B FD7E00   .~D 
        OR      $40                     ; 1E9E F640     ..
        LD      (IY+$00),A              ; 1EA0 FD7700   .wD
        RET                             ; 1EA3 C9       .

Lb406:  LD      A,(IY+$00)              ; 1EA4 FD7E00   .~D
        OR      $40                     ; 1EA7 F640     .Q
        LD      (IY+$00),A              ; 1EA9 FD7700   .wD

Lb405:  INC     (IX+$00)                ; 1EAC DD3400   .4D
        RET                             ; 1EAF C9       .

;=============================================================================
; Set game point values, based on the building number
;
; Point values set:
; Step Point
; Bonus Rate
; Bonus Rate Decrement
;=============================================================================
SET_GAME_POINT_VALUES:  
        NOP                             ; 1EB0 00       .
        LD      HL,$1EED                ; 1EB1 21ED1E   !..
        LD      A,(BUILDING_NUMBER)     ; 1EB4 3ADF80   :.. Get building number
        RLCA                            ; 1EB7 07       .   Multiply by 4
        RLCA                            ; 1EB8 07       .
        AND     $FC                     ; 1EB9 E6FC     ..  Modulo 4
        LD      D,$00                   ; 1EBB 1600     .D
        LD      E,A                     ; 1EBD 5F       _
        ADD     HL,DE                   ; 1EBE 19       .   HL = $1EED + (4 * (BldgNumber & $FC))

; Get step point from table
        LD      A,(HL)                  ; 1EBF 7E       ~   
        LD      (STEP_POINT1),A         ; 1EC0 32E080   2.. 
        INC     HL                      ; 1EC3 23       #   
        LD      A,(HL)                  ; 1EC4 7E       ~
        LD      (STEP_POINT2),A         ; 1EC5 32E180   2..

; Get bonus rate from table
        INC     HL                      ; 1EC8 23       #
        LD      A,(HL)                  ; 1EC9 7E       ~
        LD      (BONUS_RATE1),A         ; 1ECA 32E480   2..
        XOR     A                       ; 1ECD AF       .
        LD      (BONUS_RATE2),A         ; 1ECE 32E580   2..
        LD      (BONUS_RATE3),A         ; 1ED1 32E680   2..

; Get bonus rate decrement value from table
        INC     HL                      ; 1ED4 23       #
        LD      A,(HL)                  ; 1ED5 7E       ~
        LD      (DEC_BONUS_RATE1),A     ; 1ED6 32E280   2..
        XOR     A                       ; 1ED9 AF       .
        LD      (DEC_BONUS_RATE2),A     ; 1EDA 32E380   2.. Clear least significant byte

; ???
        LD      A,(BUILDING_NUMBER)     ; 1EDD 3ADF80   :..
        LD      (ISR_JUMP3_CNTR3),A     ; 1EE0 32BA82   2..  Initialize with the building number (used for window speed)?
        XOR     A                       ; 1EE3 AF       .
        LD      (FLOOR_NUM),A           ; 1EE4 323181   2a.  Clear the working floor number
        LD      (FLOOR_GROUP),A         ; 1EE7 323081   21.  Clear the working floor group
        RET                             ; 1EEA C9       .    End SET_GAME_POINT_VALUES

;-------------------------------------------------------------------------------
; Data for game point values
; Range: $1EEB - $1F0E
;-------------------------------------------------------------------------------

        .db     $C7, $FB					; Start data block

; $1EED
;
; Offset	Comment
; ------	--------------------------------
; 0, 1		Step point value
; 2			Bonus rate (most sig. byte only)
; 3			Bonus rate decrement (most sig. byte only)
;
										; Building	Step Point	Bonus Rate	Bonus Rate Decrement
										; --------	----------	----------	--------------------
        .db     $01, $00, $01, $01		; 1			100			10000		100
		.db     $01, $50, $02, $01		; 2			150			20000		100
        .db     $02, $00, $03, $02		; 3			200			30000		200
		.db     $02, $50, $04, $02		; 4			250			40000		200
        .db     $03, $00, $05, $02		; 5			300			50000		200
		.db     $03, $00, $05, $02		; 6			300			50000		200
        .db     $03, $00, $05, $02		; 7			300			50000		200
		.db     $03, $00, $05, $02		; 8			300			50000		200

        .db     $C7, $F3					; End data block



;=============================================================================
; Displays Step Point and Bonus Rate values
;=============================================================================
SHOW_STEP_PT_BONUS_RATE:
        NOP                             ; 1F0F 00       .
        LD      DE,STEP_TEXT            ; 1F10 11371F   .w.
        CALL    WRITE_CHARS             ; 1F13 CD7204   .#. Write characters to screen

        LD      DE,POINT_TEXT           ; 1F16 113F1F   ...
        CALL    WRITE_CHARS             ; 1F19 CD7204   .#. Write characters to screen

        LD      DE,BONUS_TEXT           ; 1F1C 11481F   ...
        CALL    WRITE_CHARS             ; 1F1F CD7204   .#. Write characters to screen

        LD      DE,RATE_TEXT            ; 1F22 11511F   .T.
        CALL    WRITE_CHARS             ; 1F25 CD7204   .#. Write characters to screen

; Show step point value
        LD      DE,STEP_POINT_VALUE     ; 1F28 11591F   .\.
        CALL    WRITE_DIGITS            ; 1F2B CDC504   .:. Write digits to the screen

; Show bonus rate value
        LD      DE,BONUS_RATE_VALUE     ; 1F2E 115F1F   ... Point to the bonus rate data
        CALL    WRITE_DIGITS            ; 1F31 CDC504   .:. Write digits to the screen

        RET                             ; 1F34 C9       .   End SHOW_STEP_PT_BONUS_RATE


;-------------------------------------------------------------------------------
; Data for Step Point and Bonus Rate text and data
; Range: $1F35 - $1F66
;-------------------------------------------------------------------------------

        .db     $C7, $FB						; Start data block

; $1F37
STEP_TEXT:
        .db     NOCHANGE_CHAR_COLOR				; Do not change color
		.db     $12								; Row 18
		.db     $02								; Column 2
		.db     S_EN, T_EN, E_EN, P_EN			; "STEP"	
		.db     $FF								; Terminator

; $1F3F
POINT_TEXT:
        .db     NOCHANGE_CHAR_COLOR				; Do not change color
		.db     $13								; Row 19
		.db     $02								; Column 2
		.db     P_EN, O_EN, I_EN, N_EN, T_EN	; "POINT"
		.db     $FF								; Terminator

; $1F48
BONUS_TEXT:
        .db     NOCHANGE_CHAR_COLOR				; Do not change color
		.db     $16								; Row 22
		.db     $02								; Column 2
		.db     B_EN, O_EN, N_EN, U_EN, S_EN	; "BONUS"
		.db     $FF								; Terminator

; $1F51
RATE_TEXT:
        .db     NOCHANGE_CHAR_COLOR				; Do not change color
		.db     $17								; Row 23
		.db     $02								; Column 2
		.db     R_EN, A_EN, T_EN, E_EN			; "RATE"
		.db     $FF								; Terminator
		
; $1F59
STEP_POINT_VALUE:
        .db     NOCHANGE_CHAR_COLOR				; Do not change color
		.db     $14								; Row 20
		.db     $03								; Column 3
		.db     $E0, $80						; Address: $80E0
		.db     $03								; 3 digits

; $1F5F
BONUS_RATE_VALUE:
        .db     NOCHANGE_CHAR_COLOR				; Do not change color
		.db     $18								; Row 24
		.db     $02								; Column 2
		.db     $E4, $80						; Address: $80E4 (BONUS_RATE1) digits
		.db     $05								; 5 digits

        .db     $C7, $F3						; End data block



;=============================================================================
; Shows the building number by displaying different flower pots in the lower
; right-hand corner of the screen.
;=============================================================================
DISPLAY_BLDG_LEVEL:  
        NOP                             ; 1F67 00       .
        LD      A,(BUILDING_NUMBER)     ; 1F68 3ADF80   :..  Get the building number (base 0)
        INC     A                       ; 1F6B 3C       <    Add one (base 1 number now)
        LD      IX,$939E                ; 1F6C DD219E93 .!.. IX points to bottom right screen RAM
        LD      IY,$9F9E                ; 1F70 FD219E9F .!.. IY points to bottom right color RAM
        LD      HL,LEVEL_INDICATOR_DATA ; 1F74 219D1F   !..  HL points to the flower pot level indicator table
        LD      BC,-64                  ; 1F77 01C0FF   ...  Amount to decrement IX and IY pointers

Lb411:  LD      D,(HL)                  ; 1F7A 56       V    Get value from table
        LD      (IX+$00),D              ; 1F7B DD7200   .rD  Upper left
        INC     D                       ; 1F7E 14       .    Go to next character
        LD      (IX+$01),D              ; 1F7F DD7201   .r.  Upper right
        INC     D                       ; 1F82 14       .    Go to next character
        LD      (IX+$20),D              ; 1F83 DD7220   .rd  Lower left
        INC     D                       ; 1F86 14       .    Go to next character
        LD      (IX+$21),D              ; 1F87 DD7221   .r0  Lower right
        INC     HL                      ; 1F8A 23       #    Go to next table value
        LD      D,(HL)                  ; 1F8B 56       V    Get color value
        LD      (IY+$00),D              ; 1F8C FD7200   .rD  Save color value
        LD      (IY+$01),D              ; 1F8F FD7201   .r.
        INC     HL                      ; 1F92 23       #    Go to next table value
        ADD     IX,BC                   ; 1F93 DD09     ..   Move up to next screen location
        ADD     IY,BC                   ; 1F95 FD09     ..   Move up to next color location
        DEC     A                       ; 1F97 3D       =    Decrement counter
        JR      NZ,Lb411                ; 1F98 20E0      .   Done? Nope, keep looping
        RET                             ; 1F9A C9       .    DISPLAY_BLDG_LEVEL

;-------------------------------------------------------------------------------
; Data for the flower pots.  These four flower pots are used to show the level.
;
; Range: $1F9B - $1FAE
;-------------------------------------------------------------------------------

        .db     $C7, $FB			; Start data block

; $1F9D - Flower pot level indicators
; Characters, color
LEVEL_INDICATOR_DATA:
        .db     $80, $03	; Building 1 flower pot
		.db     $84, $00	; Building 2 flower pot
		.db     $88, $00	; Building 3 flower pot
		.db     $8C, $03	; Building 4 flower pot

; These are never used...
		.db     $80, $03	; Building 5 flower pot
		.db     $84, $00	; Building 6 flower pot
		.db     $88, $00	; Building 7 flower pot
		.db     $8C, $03	; Building 8 flower pot


        .db     $C7, $F3			; End data block



;=============================================================================
; Displays the border on each edge of the screen
;=============================================================================
DISPLAY_BORDER:
        NOP                             ; 1FAF 00       .
        LD      IX,SCREEN_RAM           ; 1FB0 DD210090 .!D.  Point to screen RAM
        LD      IY,COLOR_RAM            ; 1FB4 FD21009C .!Dc  Point to color RAM
        LD      DE,$20                  ; 1FB8 112000   .dD   Steps down rows
        LD      B,$20                   ; 1FBB 0620     .d    32 rows of border

Lb412:  LD      (IX+$01),LBORDER_EN     ; 1FBD DD36017E .6..  Left border
        LD      (IX+$1E),RBORDER1_EN    ; 1FC1 DD361E7C .6.)  Right border (left of the two)
        LD      (IX+$1F),RBORDER2_EN    ; 1FC5 DD361F7D .6_=  Right border (right of the two)
        ADD     IX,DE                   ; 1FC9 DD19     ..    Go to next screen row

        LD      (IY+$01),$02            ; 1FCB FD360102 .6.G  Set color
        LD      (IY+$1E),$02            ; 1FCF FD361E02 .6.G
        LD      (IY+$1F),$02            ; 1FD3 FD361F02 .6_G
        ADD     IY,DE                   ; 1FD7 FD19     ..    Go to next color row

        DEC     B                       ; 1FD9 05       .     Decrement loop counter
        JR      NZ,Lb412                ; 1FDA 20E1      .    Done? Nope, keep looping
        RET                             ; 1FDC C9       .     End DISPLAY_BORDER


;=============================================================================
; Display number of lives left
;=============================================================================
DISPLAY_LIVES:
        NOP                             ; 1FDD 00       .
        LD      A,(CUR_NUM_LIVES)       ; 1FDE 3AD880   :.. Read current number of lives
        DEC     A                       ; 1FE1 3D       =   Decrement (because one life is being used)
        OR      A                       ; 1FE2 B7       .   Check value
        RET     Z                       ; 1FE3 C8       .   Return if zero

; Lives to display
        LD      IX,$9382                ; 1FE4 DD218293 .!.. Point to screen RAM
        LD      IY,$9F82                ; 1FE8 FD21829F .!.. Point to screen color RAM

; Display each life
Lb413:  LD      (IX+$00),PLAYER_EN      ; 1FEC DD36007F .6D+ Print out life character
        LD      (IY+$00),$0D            ; 1FF0 FD36000D .6D] Life color
        INC     IX                      ; 1FF4 DD23     .#   Move to right
        INC     IY                      ; 1FF6 FD23     .#   Move to right
        DEC     A                       ; 1FF8 3D       =    Decrement number of lives
        JR      NZ,Lb413                ; 1FF9 20F1      .   Done? Nope, keep looping

        RET                             ; 1FFB C9       .    End DISPLAY_LIVES


;=============================================================================
; Draws the current floor of the building
; 
; It keeps track of the current position within the building
;
; It plays the "climbing" sound as the climber advances a floor (one of two
; different sounds)
;
; Input:
;	BUILDING_NUMBER - The current building number
;	FLOOR_GROUP_IDX - Current floor group index
;	FLOOR_IDX - Current floor index (within the floor group)
;	FLOOR_NUM - Working floor number
;
; Misc:
;	BLDG_GROUP_IDX - Index into the building floor group pointer list 
;		(Note:  This is not used anywhere else)
;	BLDG_CHAR_TBL_IDX - Index into our character row table.
;		(Note:  This is not used anywhere else)
;=============================================================================
DRAW_BLDG_FLOOR:  
        NOP                             ; 1FFC 00       .

;------------------------------------
; Calculate index into the 1st table
; This table contains the floor groups for the building
;
; HL = $20E6 + (BldgNum * 32) + (FLOOR_GROUP_IDX)
; TblVal1 = (HL)
;
        LD      A,(BUILDING_NUMBER)     ; 1FFD 3ADF80   :.. Get the building number
        RLCA                            ; 2000 07       .   Multiply by 32
        RLCA                            ; 2001 07       .
        RLCA                            ; 2002 07       .
        RLCA                            ; 2003 07       .
        RLCA                            ; 2004 07       .
        AND     $60                     ; 2005 E660     .q  Index mod 96 
        LD      E,A                     ; 2007 5F       _
        LD      A,(FLOOR_GROUP_IDX)     ; 2008 3ADC80   :.. Get the current floor grouping index
        LD      HL,$20E6                ; 200B 21E620   !.d Point to base table
        ADD     A,E                     ; 200E 83       .   Offset for floor number
        LD      E,A                     ; 200F 5F       _
        LD      D,$00                   ; 2010 1600     .D  
        ADD     HL,DE                   ; 2012 19       .   HL = $20E6 + ((BldgNum * 32) + FLOOR_GROUP_IDX)
        LD      A,(HL)                  ; 2013 7E       ~   Get table value (TblVal1)
        CP      $FF                     ; 2014 FEFF     ..  Is value $FF? (This should not happen)
        RET     Z                       ; 2016 C8       .   Yes, end DRAW_BLDG_FLOOR

;------------------------------------
; Calculate index into the 2nd table
; This is the building group pointer list
;
; IX = $2166 + (2*TblVal1)
; HL = (IX) + (FLOOR_IDX)
; TblVal2 = (HL)
;
        LD      (BLDG_GROUP_IDX),A      ; 2017 324F81   2J.  Save the building group index value
        LD      IX,$2166                ; 201A DD216621 .!70 Point to the jump pointer table
        LD      A,(BLDG_GROUP_IDX)      ; 201E 3A4F81   :J.  Get the building group index value
        RLCA                            ; 2021 07       .    TblVal1 = TblVal1 * 2
        AND     $FE                     ; 2022 E6FE     ..   
        LD      E,A                     ; 2024 5F       _
        LD      D,$00                   ; 2025 1600     .D
        ADD     IX,DE                   ; 2027 DD19     ..   IX = $2166 + (2*TblVal1)
        LD      L,(IX+$00)              ; 2029 DD6E00   .nD  HL = Pointer to the floor groups
        LD      H,(IX+$01)              ; 202C DD6601   .f.
        LD      A,(FLOOR_IDX)           ; 202F 3ADD80   :".  Get the current floor index
        LD      E,A                     ; 2032 5F       _
        LD      D,$00                   ; 2033 1600     .D
        ADD     HL,DE                   ; 2035 19       .    HL = HL + FLOOR_IDX
        LD      A,(HL)                  ; 2036 7E       ~    Get Table value 2 (TblVal2)


;-------------------------------
; Calculate index into table 3
; This table contains character rows of the buildings
;
; IX = $2260 + (21 * (TblVal2))
; IX will point to a row of the building

; Save our TblVal2 value in BLDG_CHAR_TBL_IDX 
        LD      (BLDG_CHAR_TBL_IDX),A   ; 2037 325181   2..  This is our offset index into the character row table
        LD      IX,$2260                ; 203A DD216022 .!q& This points to the building character rows table
        OR      A                       ; 203E B7       .    Is our loop counter = 0?
        JR      Z,Lb414                 ; 203F 2808     (L   Yes, skip loop

        LD      DE,$15                  ; 2041 111500   .PD  21 values in each table entry

Lb415:  ADD     IX,DE                   ; 2044 DD19     ..   Increment our table pointer
        DEC     A                       ; 2046 3D       =    Decrement our loop counter
        JR      NZ,Lb415                ; 2047 20FB      .   Done? Nope, continue looping

;----------------------------
; Setup for write to screen
; This finds the proper row on the screen to start drawing the row
;
; Note: FLOOR_NUM is a mod 8 value,
;
Lb414:  LD      IY,$9008                ; 2049 FD210890 .!L. IY points to screen RAM
        LD      A,(FLOOR_NUM)           ; 204D 3A3181   :a.  Get the current floor number
        LD      E,A                     ; 2050 5F       _
        LD      D,$00                   ; 2051 1600     .D
        ADD     IY,DE                   ; 2053 FD19     ..   IY = $9008 + ((FLOOR_NUM) * 4)
        ADD     IY,DE                   ; 2055 FD19     ..
        ADD     IY,DE                   ; 2057 FD19     ..
        ADD     IY,DE                   ; 2059 FD19     ..

;---------------------------------
; Get building color value
; That is located in table $2BDE
        PUSH    HL                      ; 205B E5       .    Save HL (points to table 2 value)
        LD      HL,BUILDING_COLOR_DATA  ; 205C 21DE2B   !.:
        LD      A,(BUILDING_NUMBER)     ; 205F 3ADF80   :..
        LD      E,A                     ; 2062 5F       _
        LD      D,$00                   ; 2063 1600     .D
        ADD     HL,DE                   ; 2065 19       .    HL = BUILDING_COLOR_DATA + BldgNumber
        LD      C,(HL)                  ; 2066 4E       N    Get color value from table

        PUSH    IY                      ; 2067 FDE5     ..   Save IY (points to screen ram)
        POP     HL                      ; 2069 E1       .    HL = IY (points to screen ram)
        LD      DE,$C00                 ; 206A 11000C   .D\  Offset to color RAM
        ADD     HL,DE                   ; 206D 19       .    HL = HL + $0C00 (point to color RAM)

;------------------------------------------------
; Write out a building row to the screen
; IX points to the row of characters to display
; IY points to the screen RAM
; HL points to the color RAM
; C contains the building color
        LD      B,$15                   ; 206E 0615     .Q   21 columns to display

Lb416:  LD      A,(IX+$00)              ; 2070 DD7E00   .~D  Get the building character to display
        LD      (IY+$00),A              ; 2073 FD7700   .wD  Write it to the screen
        LD      (HL),C                  ; 2076 71       q    Save color value in color RAM
        INC     HL                      ; 2077 23       #    Go to next color RAM location
        INC     IX                      ; 2078 DD23     .#   Go to next building character
        INC     IY                      ; 207A FD23     .#   Go to next screen RAM location
        DEC     B                       ; 207C 05       .    Decrement loop counter
        JR      NZ,Lb416                ; 207D 20F1      .   Done? Nope, keep looping

;-------------------------------------
; Set up window open/close modifiers?
; IX = $2497 + (8 * (BLDG_CHAR_TBL_IDX))
		POP     HL                      ; 207F E1       .    Point again to the table 2 group
        LD      A,(BLDG_CHAR_TBL_IDX)   ; 2080 3A5181   :T.  Get the offset index into the character row table
        LD      IX,$2497                ; 2083 DD219724 .!.t Base of table 4
        RLCA                            ; 2087 07       .    Multiply index by 8
        RLCA                            ; 2088 07       .
        RLCA                            ; 2089 07       .
        AND     $F8                     ; 208A E6F8     ..
        LD      E,A                     ; 208C 5F       _
        LD      D,$00                   ; 208D 1600     .D
        ADD     IX,DE                   ; 208F DD19     ..   IX = $2497 + (8 * (BLDG_CHAR_TBL_IDX))
        LD      IY,PLAYFIELD            ; 2091 FD218181 .!.. IY points to the playfield
        LD      A,(FLOOR_NUM)           ; 2095 3A3181   :a.  Get the working floor number 
        AND     $F8                     ; 2098 E6F8     ..
        BIT     3,A                     ; 209A CB5F     ._   Is bit 3 0?
        JP      Z,Lb417                 ; 209C CAA320   .\d  Yes, continue

        RES     3,A                     ; 209F CB9F     ..   Set bit 3 to 0
        ADD     A,$10                   ; 20A1 C610     ..   Add 16

Lb417:  RRCA                            ; 20A3 0F       .    Divide A by 2
        AND     $7F                     ; 20A4 E67F     .+   
        LD      E,A                     ; 20A6 5F       _
        LD      D,$00                   ; 20A7 1600     .D
        ADD     IY,DE                   ; 20A9 FD19     ..   IY = PLAYFIELD + (FLOOR_NUM / 2)


;-------------------------------------------------
; Sets up 8 window table values?
; IY points to the window open/close table?
; IX points to table 4 (window modifiers?)
; C contains the building color
        LD      B,$08                   ; 20AB 0608     .L   Loop 8 times

Lb418:  LD      A,(IX+$00)              ; 20AD DD7E00   .~D  Get value from table
        LD      (IY+$00),A              ; 20B0 FD7700   .wD  Save it to the window table
        INC     IX                      ; 20B3 DD23     .#   Go to next table value
        INC     IY                      ; 20B5 FD23     .#   Go to next window
        DEC     B                       ; 20B7 05       .    Decrement loop counter
        JR      NZ,Lb418                ; 20B8 20F3      .   Done? Nope, continue

; Alternate sounds
        LD      A,(FLOOR_NUM)           ; 20BA 3A3181   :a.  Get the working floor number
        LD      BC,$300                 ; 20BD 010003   .DS  Sound group 3, index 0
        BIT     4,A                     ; 20C0 CB67     .g   Is bit 4 = 0?
        JR      Z,Lb419                 ; 20C2 2803     (S   Yes, continue

        LD      BC,$301                 ; 20C4 010103   ...  Sound group 3, index 1 (climbing sound)

; Play climbing sound
Lb419:  CALL    LOAD_SOUND_DATA         ; 20C7 CDBB11   ..A  Play climbing sound
        LD      A,(FLOOR_IDX)           ; 20CA 3ADD80   :..  Go to the next floor
        ADD     A,$01                   ; 20CD C601     ..
        LD      (FLOOR_IDX),A           ; 20CF 32DD80   2".

        INC     HL                      ; 20D2 23       #    Advance in table 2 group
        LD      A,(HL)                  ; 20D3 7E       ~    Get table value
        CP      $FF                     ; 20D4 FEFF     ..   Is value = $FF (end of table entry)?
        RET     NZ                      ; 20D6 C0       .    Nope, end DRAW_BLDG_FLOOR

; End of building group -- advance to next floor group
        LD      A,(FLOOR_GROUP_IDX)     ; 20D7 3ADC80   :..  Go to the next building floor group
        ADD     A,$01                   ; 20DA C601     ..
        LD      (FLOOR_GROUP_IDX),A     ; 20DC 32DC80   2..

; Start at the beginning of this floor group
        XOR     A                       ; 20DF AF       .    Clear FLOOR_IDX
        LD      (FLOOR_IDX),A           ; 20E0 32DD80   2..

        RET                             ; 20E3 C9       .    End DRAW_BLDG_FLOOR

;-------------------------------------------------------------------------------
; Data that defines the building floors
;
; Range: $20E4 - $2571
; Number of bytes: 1166
;-------------------------------------------------------------------------------

        .db     $C7, $FB		; Start data block

; $20E6 - Building number 0
;         (Note: FLOOR_GROUP_IDX indexes into this table)
        .db     $00, $01, $02, $01, $01, $05, $01, $01
        .db     $01, $02, $01, $01, $01, $02, $01, $01
        .db     $01, $05, $05, $01, $01, $02, $01, $01
        .db     $08, $0B, $0B, $0B, $0B, $0B, $0B, $0B
; $2106 - Building number 1
;         (Note: FLOOR_GROUP_IDX indexes into this table)
        .db     $00, $03, $05, $05, $05, $05, $03, $01
        .db     $02, $02, $02, $02, $03, $04, $04, $04
        .db     $02, $02, $03, $04, $04, $04, $04, $04
        .db     $09, $0B, $0B, $0B, $0B, $0B, $0B, $0B
; $2126 - Building number 2
;         (Note: FLOOR_GROUP_IDX indexes into this table)
        .db     $00, $01, $01, $02, $02, $02, $01, $02
        .db     $01, $01, $02, $03, $04, $04, $04, $04
        .db     $04, $05, $05, $06, $07, $05, $06, $06
        .db     $0A, $0B, $0B, $0B, $0B, $0B, $0B, $0B
; $2146 - Building number 3
;         (Note: FLOOR_GROUP_IDX indexes into this table)
        .db     $00, $02, $01, $02, $02, $02, $02, $01
        .db     $01, $05, $05, $01, $01, $01, $03, $01
        .db     $05, $03, $02, $02, $02, $02, $02, $02
        .db     $0C, $0B, $0B, $0B, $0B, $0B, $0B, $0B


;----------------------------------------
; Table 2 - Jump pointer table
; The index value is from table 1 above
;
; Jump to the value in the following jump table, then
; index forward by (FLOOR_IDX)
;
; $2166
        .db     $80, $21	; Index 0
		.db     $94, $21	; Index 1
		.db     $A5, $21	; Index 2
		.db     $B6, $21	; Index 3
        .db     $C7, $21	; Index 4
		.db     $D8, $21	; Index 5
		.db     $E9, $21	; Index 6
		.db     $FA, $21	; Index 7
        .db     $0B, $22	; Index 8
		.db     $1C, $22	; Index 9
		.db     $2D, $22	; Index A
		.db     $3E, $22	; Index B
        .db     $4F, $22	; Index C


;-------------------------------------------------
; Locations jumped to by the jump table (Table 2)
; Note: Index into these tables is made by adding FLOOR_IDX
; $2180
		.db     $0E, $0E, $00, $01, $02, $01, $03, $0B
		.db     $08, $0B, $08, $0B, $08, $0B, $08, $0B
		.db     $08, $0B, $08, $FF

; $2194
		.db     $0B, $08, $0B, $08, $0B, $08, $0B, $08
		.db     $0B, $08, $0B, $08, $0B, $08, $0B, $08
		.db     $FF

; $21A5
		.db     $04, $0C, $06, $07, $06, $07, $06, $07
		.db     $06, $07, $06, $07, $06, $07, $06, $07
		.db     $FF
; $21B6
        .db     $10, $11, $12, $13, $12, $13, $12, $13
        .db     $12, $13, $12, $13, $12, $13, $12, $13
        .db     $FF

; $21C7
		.db     $12, $13, $12, $13, $12, $13, $12, $13
		.db     $12, $13, $12, $13, $12, $13, $12, $13
		.db     $FF

; $21D8
		.db     $05, $0A, $09, $0A, $09, $0A, $09, $0A
		.db     $09, $0A, $09, $0A, $09, $0A, $05, $0D
		.db     $FF
		
; $21E9
		.db     $14, $15, $16, $17, $16, $17, $16, $17
		.db     $16, $17, $16, $17, $16, $17, $16, $17
		.db     $FF
		
; $21FA
		.db     $16, $17, $16, $17, $16, $17, $16, $17
		.db     $16, $17, $16, $17, $16, $17, $16, $17
		.db     $FF
		
; $220B
		.db     $0B, $08, $0B, $08, $0B, $08, $0B, $08
		.db     $0B, $08, $0B, $08, $0B, $08, $0B, $0E
		.db     $FF
		
; $221C
		.db     $12, $13, $12, $13, $12, $13, $12, $13
		.db     $12, $13, $12, $13, $12, $13, $12, $18
		.db     $FF
		
; $222D
		.db     $16, $17, $16, $17, $16, $17, $16, $17
		.db     $16, $17, $16, $17, $16, $17, $16, $19
		.db     $FF

; $223E
        .db     $0F, $0F, $0F, $0F, $0F, $0F, $0F, $0F
        .db     $0F, $0F, $0F, $0F, $0F, $0F, $0F, $0F
        .db     $FF
		
; $224F
		.db     $06, $07, $06, $07, $06, $07, $06, $07
		.db     $06, $07, $06, $07, $06, $07, $06, $1A
		.db     $FF
		


;----------------------------------------
; Table 3 - Building rows
;
; This table is indexed by 21 * TblVal2
;
; These are the rows of windows for the buildings
;
; $2260 - Index = $00
        .db     $51, $53, $51, $51, $53, $51, $51, $53		; Row 1, bldg 1 / 4 (Bottom of doors)
		.db     $58, $59, $5E, $59, $5F, $53, $51, $51
		.db     $53, $51, $51, $53, $51
		
; $2275 - Index = $01
		.db     $51, $53, $42, $43, $53, $42, $43, $53		; Row 2, bldg 1 / 4 (Middle doors 1)
		.db     $56, $52, $5C, $52, $5D, $53, $42, $43
		.db     $53, $42, $43, $53, $51

; $228A - Index = $02
		.db     $51, $53, $4E, $4F, $53, $4E, $4F, $53		; Row 3, bldg 1 / 4 (Middle doors 2)
		.db     $56, $57, $5C, $57, $5D, $53, $4E, $4F
		.db     $53, $4E, $4F, $53, $51

; $229F - Index = $03
		.db     $51, $53, $4E, $4F, $53, $4E, $4F, $53		; Row 4, bldg 1 / 4 (Top doors)
		.db     $54, $55, $5A, $55, $5B, $53, $4E, $4F
		.db     $53, $4E, $4F, $53, $51
		
; $22B4 - Index = $04
		.db     $51, $53, $42, $43, $53, $42, $43, $53
		.db     $51, $51, $53, $51, $51, $53, $42, $43
		.db     $53, $42, $43, $53, $51

; $22C9 - Index = $05
		.db     $51, $53, $51, $51, $53, $51, $51, $53
		.db     $42, $43, $53, $42, $43, $53, $51, $51
		.db     $53, $51, $51, $53, $51

; $22DE - Index = $06
        .db     $51, $53, $42, $43, $53, $42, $43, $53
        .db     $52, $52, $52, $52, $52, $53, $42, $43
        .db     $53, $42, $43, $53, $51
	
; $22F3 - Index = $07
		.db     $51, $53, $4E, $4F, $53, $4E, $4F, $53
		.db     $52, $52, $52, $52, $52, $53, $4E, $4F
		.db     $53, $4E, $4F, $53, $51
	
; $2308 - Index = $08
		.db     $51, $53, $4E, $4F, $53, $4E, $4F, $53
		.db     $4E, $4F, $53, $4E, $4F, $53, $4E, $4F
		.db     $53, $4E, $4F, $53, $51
	
; $231D - Index = $09
		.db     $51, $53, $52, $52, $52, $52, $52, $53
		.db     $42, $43, $53, $42, $43, $53, $52, $52
		.db     $52, $52, $52, $53, $51
		
; $2332 - Index = $0A
		.db     $51, $53, $52, $52, $52, $52, $52, $53
		.db     $4E, $4F, $53, $4E, $4F, $53, $52, $52
		.db     $52, $52, $52, $53, $51
		
; $2347 - Index = $0B
		.db     $51, $53, $42, $43, $53, $42, $43, $53
		.db     $42, $43, $53, $42, $43, $53, $42, $43
		.db     $53, $42, $43, $53, $51

; $235C - Index = $0C
		.db     $51, $53, $4E, $4F, $53, $4E, $4F, $53
		.db     $51, $51, $53, $51, $51, $53, $4E, $4F
		.db     $53, $4E, $4F, $53, $51

; $2371 - Index = $0D
		.db     $51, $53, $51, $51, $53 ,$51, $51, $53
		.db     $4E, $4F, $53, $4E, $4F ,$53, $51, $51
		.db     $53, $51, $51, $53, $51

; $2386 - Index = $0E
		.db     $50, $50, $50, $50, $50, $50, $50, $50
		.db     $50, $50, $50, $50, $50, $50, $50, $50
		.db     $50, $50, $50, $50, $50
		
; $239B - Index = $0F
		.db     $52, $52, $52 ,$52, $52, $52, $52, $52
		.db     $52, $52, $52 ,$52, $52, $52, $52, $52
		.db     $52, $52, $52 ,$52, $52
		
; $23B0 - Index = $10
		.db     $51, $53, $51, $51, $53, $42 ,$43, $53
		.db     $42, $43, $53, $42, $43, $53, $42, $43
		.db     $53, $51, $51, $53, $51
		
; $23C5 - Index = $11
		.db     $51, $53, $51, $51, $53, $4E, $4F, $53
		.db     $4E, $4F, $53, $4E, $4F, $53, $4E, $4F
		.db     $53, $51, $51, $53, $51
		
; $23DA - Index = $12
		.db     $52, $52, $52, $51, $53, $42, $43, $53
		.db     $42, $43, $53, $42, $43, $53, $42, $43
		.db     $53, $51, $52, $52, $52
		
; $23EF - Index = $13
		.db     $52, $52, $52, $51, $53, $4E, $4F, $53
		.db     $4E, $4F, $53, $4E, $4F, $53, $4E, $4F
		.db     $53, $51, $52, $52, $52
		
; $2404 - Index = $14
		.db     $52, $52, $52, $51, $53, $51, $51, $53
		.db     $42, $43, $53, $42, $43, $53, $51, $51
		.db     $53, $51, $52, $52, $52
		
; $2419 - Index = $15
		.db     $52, $52, $52, $51, $53, $51, $51, $53
		.db     $4E, $4F, $53, $4E, $4F, $53, $51, $51
		.db     $53, $51, $52, $52, $52
		
; $242E - Index = $16
		.db     $52, $52, $52, $52, $52, $52, $51, $53
		.db     $42, $43, $53, $42, $43, $53, $51, $52
		.db     $52, $52, $52, $52, $52
		
; $2443 - Index = $17
		.db     $52, $52, $52, $52, $52, $52, $51, $53
		.db     $4E, $4F, $53, $4E, $4F, $53, $51, $52
		.db     $52, $52, $52, $52, $52
		
; $2458 - Index = $18
		.db     $52, $52, $52, $50, $50, $50, $50, $50
		.db     $50, $50, $50, $50, $50, $50, $50, $50
		.db     $50, $50, $52, $52, $52
		
; $246D - Index = $19
		.db     $52, $52, $52, $52, $52, $52, $50, $50
		.db     $50, $50, $50, $50, $50, $50, $50, $52
		.db     $52, $52, $52, $52, $52
		
; $2482 - Index = $1A
		.db     $50, $50, $50, $50, $50, $50, $50, $50
		.db     $52, $52, $52, $52, $52, $50, $50, $50
		.db     $50, $50, $50, $50, $50
		
		
;----------------------------------------
; Table 4 - Window open/close modifiers?
;
		
; $2497 - Index = $00
		.db     $FF, $00, $00, $FF, $FF, $00, $00, $FF

; $249F - Index = $01
		.db     $FF, $00, $00, $FF, $FF, $00, $00, $FF

; $24A7 - Index = $02
		.db     $FF, $00, $00, $FF, $FF, $00, $00, $FF

; $24AF - Index = $03
		.db     $FF, $00, $00, $FF, $FF, $00, $00, $FF

; $24B7 - Index = $04
		.db     $FF, $00, $00, $FF, $FF, $00, $00, $FF

; $24BF - Index = $05
		.db     $FF, $FF, $FF, $00, $00, $FF, $FF, $FF

; $24C7 - Index = $06
		.db     $FF, $80, $80, $FF, $FF, $80, $80, $FF

; $24CF - Index = $07
		.db     $FF, $00, $00, $FF, $FF, $00, $00, $FF

; $24D7 - Index = $08
		.db     $FF, $00, $00, $00, $00, $00, $00, $FF

; $24DF - Index = $09
		.db     $FF, $FF, $FF, $00, $00, $FF, $FF, $FF

; $24E7 - Index = $0A
		.db     $FF, $FF, $FF, $00, $00, $FF, $FF, $FF

; $24EF - Index = $0B
		.db     $FF, $80, $80, $80, $80, $80, $80, $FF

; $24F7 - Index = $0C
		.db     $FF, $00, $00, $FF, $FF, $00, $00, $FF

; $24FF - Index = $0D
		.db     $FF, $FF, $FF, $00, $00, $FF, $FF, $FF

; $2507 - Index = $0E
		.db     $FF, $80, $80, $80, $80, $80, $80, $FF

; $250F - Index = $0F
		.db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF

; $2517 - Index = $10
		.db     $FF, $FF, $00, $00, $00, $00, $FF, $FF

; $251F - Index = $11
		.db     $FF, $FF, $00, $00, $00, $00, $FF, $FF

; $2527 - Index = $12
		.db     $FF, $FF, $80, $80, $80, $80, $FF, $FF

; $252F - Index = $13
		.db     $FF, $FF, $00, $00, $00, $00, $FF, $FF

; $2537 - Index = $14
		.db     $FF, $FF, $FF, $00, $00, $FF, $FF, $FF

; $253F - Index = $15
		.db     $FF, $FF, $FF, $00, $00, $FF, $FF, $FF

; $2547 - Index = $16
		.db     $FF, $FF, $FF, $80, $80, $FF, $FF, $FF

; $254F - Index = $17
		.db     $FF, $FF, $FF, $00, $00, $FF, $FF, $FF

; $2557 - Index = $18
		.db     $FF, $FF, $80, $80, $80, $80, $FF, $FF

; $255F - Index = $19
		.db     $FF, $FF, $FF, $80, $80, $FF, $FF, $FF

; $2567 - Index = $1A
		.db     $FF, $80, $80, $FF, $FF, $80, $80, $FF

; $256F - Index = $1B
		.db     $FF

        .db     $C7, $F3		; End data block

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------


;=============================================================================
; Updates the windows
;=============================================================================
UPDATE_WINDOWS:
        LD      A,($8156)               ; 2572 3A5681   :..  Get index
        LD      B,A                     ; 2575 47       G    Multiply index by 3
        RLCA                            ; 2576 07       .    
        ADD     A,B                     ; 2577 80       .    
        LD      E,A                     ; 2578 5F       _
        LD      D,$00                   ; 2579 1600     .D
        LD      IY,$8201                ; 257B FD210182 .!..
        ADD     IY,DE                   ; 257F FD19     ..   IY = $8201 + (3*index)
        LD      A,(IY+$00)              ; 2581 FD7E00   .~D  Get value at IY
        CP      $00                     ; 2584 FE00     .D   Is value = 0 (not opening or closing)?
        JR      Z,Lb448                 ; 2586 2818     (.   Yes, continue

;
; Calculate the playfield and screen addresses
; In: 
;	C = row
;	B = column
;
; Out: 
;	HL points to the playfield address
;	IX points to the proper screen location
        LD      C,(IY+$01)              ; 2588 FD4E01   .N.	Row of playfield
        LD      B,(IY+$02)              ; 258B FD4602   .F.	Column of playfield
        CALL    CALC_PLAYFIELD_SCREEN   ; 258E CD3B26   .:3	Calculate the playfield and screen addresses

        LD      A,(HL)                  ; 2591 7E       ~   Get playfield value
        CP      $00                     ; 2592 FE00     .D  Is value 0?
        JR      Z,Lb448                 ; 2594 280A     (.  Yes, continue

        CP      $80                     ; 2596 FE80     ..  Is value = $80?
        JR      Z,Lb448                 ; 2598 2806     (G  Yes, continue

        CP      $FF                     ; 259A FEFF     ..  Is value = $FF?
        JR      Z,Lb448                 ; 259C 2802     (.  Yes, continue

; We are already opening / closing this window
        JR      Lb450                   ; 259E 1856     ..  Some other value, go here


; The window is not opening or closing
Lb448:  LD      A,(RANDOM_NUMBER)       ; 25A0 3A2281   :&.  Get a random number
        AND     $01                     ; 25A3 E601     ..   Is value odd?
        JR      NZ,Lb451                ; 25A5 201E      [   Yes, jump here

; Update the current table row/column
        LD      BC,(WINDOW_ROW_COL_FIFO); 25A7 ED4BBB82 .K..  Get a new row/column combination from the window update FIFO
        LD      (IY+$01),C              ; 25AB FD7101   .q.  Save new row
        LD      (IY+$02),B              ; 25AE FD7002   .pG  Save new column


; Update the FIFO by shifting all values up two bytes
        PUSH    HL                      ; 25B1 E5       .	Save used registers
        PUSH    DE                      ; 25B2 D5       .
        PUSH    BC                      ; 25B3 C5       .
        LD      HL,WINDOW_ROW_COL_FIFO+2 ; 25B4 21BD82   !..  Source address
        LD      DE,WINDOW_ROW_COL_FIFO  ; 25B7 11BB82   ..}  Destination address
        LD      BC,$1E                  ; 25BA 011E00   ..D  Copy 30 bytes of data
        CALL    BLOCK_COPY              ; 25BD CD4A04   .K.  Block copy routine

        POP     BC                      ; 25C0 C1       .	Restore used registers
        POP     DE                      ; 25C1 D1       .
        POP     HL                      ; 25C2 E1       .
        JR      Lb452                   ; 25C3 1815     .P	Continue


; Create a new random row and column
Lb451:  LD      A,(RANDOM_NUMBER)       ; 25C5 3A2281   :g. Get a random number
        LD      B,A                     ; 25C8 47       G
        LD      A,(ISR_COUNTER)         ; 25C9 3A4580   :U. Get the interrupt counter
        XOR     B                       ; 25CC A8       .
        AND     $0F                     ; 25CD E60F     .N
        LD      C,A                     ; 25CF 4F       O	Set the playfield column
        LD      (IY+$01),C              ; 25D0 FD7101   .q.	Save the column
        LD      A,B                     ; 25D3 78       x
        AND     $07                     ; 25D4 E607     ..
        LD      B,A                     ; 25D6 47       G	Set the playfield row
        LD      (IY+$02),B              ; 25D7 FD7002   .p.	Save the row

;
; Calculate the playfield and screen addresses
; In: 
;	C = row
;	B = column
;
; Out: 
;	HL points to the playfield address
;	IX points to the proper screen location
Lb452:  CALL    CALC_PLAYFIELD_SCREEN   ; 25DA CD3B26   .:3	Calculate the playfield and screen addresses

        LD      A,(HL)                  ; 25DD 7E       ~	Get the playfield location value
        CP      $80                     ; 25DE FE80     ..	Is it $80?
        JR      Z,Lb453                 ; 25E0 2806     (G	Yes, go here

        CP      $FF                     ; 25E2 FEFF     ..	Is it $FF (can't move there)?
        JR      Z,Lb453                 ; 25E4 2802     (.	Yes, go here

        JR      Lb450                   ; 25E6 180E     .O	; This is an active location

Lb453:  LD      (IY+$00),$00            ; 25E8 FD360000 .6DD	Not an active location?
        LD      (IY+$01),$00            ; 25EC FD360100 .6.D	Remove row from table
        LD      (IY+$02),$00            ; 25F0 FD360200 .6GD	Remove column from table
        JR      Lb454                   ; 25F4 182B     .{

; Cycle the window position
Lb450:  INC     A                       ; 25F6 3C       <	Advance window position
        AND     $0F                     ; 25F7 E60F     .N   Range from 0 - $F
        LD      (HL),A                  ; 25F9 77       w    Save new window position
        LD      (IY+$00),$01            ; 25FA FD360001 .6D. This is an active location now

;---------------------------------------------------------------------------------
; Get the proper window animation characters from the WINDOW_ANIMATION_TBL table
; Write the window animation to the screen
; IX points to the screen for the current window

        LD      IY,WINDOW_ANIMATION_TBL ; 25FE FD216226 .!cg  Point to the window animation table
        RLCA                            ; 2602 07       .     Multiply the window position by 4 (4 characters per animation)
        RLCA                            ; 2603 07       .
        LD      E,A                     ; 2604 5F       _
        LD      D,$00                   ; 2605 1600     .D
        ADD     IY,DE                   ; 2607 FD19     ..  IY = WINDOW_ANIMATION_TBL + (Index*4)
        LD      A,(IY+$00)              ; 2609 FD7E00   .~D Get top left window character
        LD      (IX+$00),A              ; 260C DD7700   .wD Write top left
        LD      A,(IY+$01)              ; 260F FD7E01   .~. Get top right window character
        LD      (IX+$01),A              ; 2612 DD7701   .w. Write top right
        LD      A,(IY+$02)              ; 2615 FD7E02   .~. Get bottom left window character
        LD      (IX+$20),A              ; 2618 DD7720   .wd Write bottom left (on next row)
        LD      A,(IY+$03)              ; 261B FD7E03   .~S Get bottom right window character
        LD      (IX+$21),A              ; 261E DD7721   .w4 Write bottom right (on next row)

Lb454:  LD      B,$14                   ; 2621 0614     ..	Load B with 20
        LD      A,(FLOOR_GROUP_IDX)     ; 2623 3ADC80   :.. Get the current building floor group
        RRCA                            ; 2626 0F       .	
        AND     $0F                     ; 2627 E60F     .N	
        ADD     A,B                     ; 2629 80       .	
        LD      B,A                     ; 262A 47       G	B = 20 + (FLOOR_GROUP_IDX/2) & 0x0F
        LD      A,($8156)               ; 262B 3A5681   :W.	Get the routine counter	
        INC     A                       ; 262E 3C       <	Increment
        CP      B                       ; 262F B8       .	Is B = A?
        JR      Z,Lb455                 ; 2630 2804     (.	Yes, go here

        CP      $28                     ; 2632 FE28     .l	
        JR      C,Lb456                 ; 2634 3801     8.	Is A < 40?  Yes, go here.

Lb455:  XOR     A                       ; 2636 AF       .	Clear A

Lb456:  LD      ($8156),A               ; 2637 325681   2W.	Save the routine counter
        RET                             ; 263A C9       .	End UPDATE_WINDOWS



;=============================================================================
; Calculates the playfield table address and screen address for the given
; playfiled location.
;
; Note the screen pointer starts at $93E7.  This is 25 values less than the
; start of the screen address ($9400).  Note the screen address wraps is
; repeated -- $9000 - $93FF is the same as $9400 - $97FF.
;
; Input:
;	B - Column
;	C - Row
;
; Output:
;
;	HL - Points to proper memory location
;		 PLAYFIELD + (Row * 8) + Column
;
;	IX - Points to proper screen location
;		 $93E7 + (Row * $40) + (Column * 3)
;=============================================================================
CALC_PLAYFIELD_SCREEN:
        LD      HL,PLAYFIELD            ; 263B 218181   !..	 HL will point to the playfield
		LD      IX,$93E7                ; 263E DD21E793 .!.. IX will point to the screen
        LD      A,C                     ; 2642 79       y    A = Row
        OR      A                       ; 2643 B7       .    Is Row = 0?
        JR      Z,Lb457                 ; 2644 280C     (.   Yes, skip copy

; Loop for each Row
Lb458:  LD      DE,$08                  ; 2646 110800   .LD	
        ADD     HL,DE                   ; 2649 19       .	HL += 8  (playfield location advanced by row)
        LD      DE,$40                  ; 264A 114000   ..D
        ADD     IX,DE                   ; 264D DD19     ..	IX += 64 (2 screen lines per row)
        DEC     A                       ; 264F 3D       =	Decrement Row counter
        JR      NZ,Lb458                ; 2650 20F4      .	Are we done?  Nope, keep looping

Lb457:  LD      A,B                     ; 2652 78       x    A = Column
        OR      A                       ; 2653 B7       .    Is column = 0?
        JR      Z,Lb459                 ; 2654 2809     (.   Yes, exit
        LD      DE,$03                  ; 2656 110300   .SD

; Loop for each column
Lb460:  INC     HL                      ; 2659 23       #	HL += 1 (playfield location advanced by column)
        ADD     IX,DE                   ; 265A DD19     ..	IX += 3 (screen advanced by column)
        DEC     A                       ; 265C 3D       =	Decrement column counter
        JR      NZ,Lb460                ; 265D 20FA      .	Are we done?  Nope, keep looping

Lb459:  RET                             ; 265F C9       .	end of CALC_PLAYFIELD_SCREEN


;-------------------------------------------------------------------------------
; Data for Window closing / opening animation
;
; Range: $2660 - $26A3
; Number of bytes: 68
;-------------------------------------------------------------------------------

        .db     $C7, $FB			; Data block start

; $2662
WINDOW_ANIMATION_TBL:
        .db     $4E, $4F, $42, $43	; Index 0 - Open window
		.db     $4C, $4D, $42, $43	; Index 1 - Closing window 1
        .db     $4A, $4B, $42, $43	; Index 2 - Closing window 2
		.db     $48, $49, $42, $43	; Index 3 - Closing window 3
        .db     $46, $47, $42, $43	; Index 4 - Closing window 4
		.db     $44, $45, $40, $41	; Index 5 - Closed window
        .db     $44, $45, $40, $41	; Index 6 - Closed window
		.db     $44, $45, $40, $41	; Index 7 - Closed window
        .db     $44, $45, $40, $41	; Index 8 - Closed window
		.db     $44, $45, $40, $41	; Index 9 - Closed window
        .db     $44, $45, $40, $41	; Index A - Closed window
		.db     $44, $45, $40, $41	; Index B - Closed window
        .db     $46, $47, $42, $43	; Index C - Opening window 1
		.db     $48, $49, $42, $43	; Index D - Opening window 2
        .db     $4A, $4B, $42, $43	; Index E - Opening window 3
		.db     $4C, $4D, $42, $43	; Index F - Opening window 4


        .db     $C7, $F3			; Data block end

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------



;=============================================================================
;=============================================================================
Lb365:  NOP                             ; 26A4 00       .
        LD      HL,$9892                ; 26A5 219298   !.. Left climber arm, Y position
        LD      B,$04                   ; 26A8 0604     ..

Lb463:  LD      A,($814C)               ; 26AA 3A4C81   :..
        CP      $00                     ; 26AD FE00     .D
        RET     Z                       ; 26AF C8       .

        AND     $80                     ; 26B0 E680     ..
        JR      Z,Lb461                 ; 26B2 2803     (S
        DEC     (HL)                    ; 26B4 35       5
        JR      Lb462                   ; 26B5 1801     ..

Lb461:  INC     (HL)                    ; 26B7 34       4

Lb462:  INC     HL                      ; 26B8 23       #
        INC     HL                      ; 26B9 23       #
        INC     HL                      ; 26BA 23       #
        INC     HL                      ; 26BB 23       #
        DEC     B                       ; 26BC 05       .
        JR      NZ,Lb463                ; 26BD 20EB      .
        LD      A,($814C)               ; 26BF 3A4C81   :H.
        BIT     7,A                     ; 26C2 CB7F     ..
        JR      NZ,Lb464                ; 26C4 2004      .
        SUB     $01                     ; 26C6 D601     ..
        JR      Lb465                   ; 26C8 1802     ..

Lb464:  ADD     A,$01                   ; 26CA C601     ..

Lb465:  LD      ($814C),A               ; 26CC 324C81   2..
        RET                             ; 26CF C9       .

;=============================================================================
; Scrolls the building by the value contained in FLOOR_NUM
;=============================================================================
SCROLL_BUILDING:  
        LD      HL,$9808                ; 26D0 210898   !L. Point to column scrolling RAM
        LD      C,$15                   ; 26D3 0E15     .P  21 columns (the building width)
        LD      A,(FLOOR_NUM)           ; 26D5 3A3181   :a. Get the working floor number

Lb466:  LD      (HL),A                  ; 26D8 77       w   Scroll this column
        INC     HL                      ; 26D9 23       #   Go to next column
        DEC     C                       ; 26DA 0D       .   Decrement counter
        JR      NZ,Lb466                ; 26DB 20FB      .  Done? Nope, keep looping

        RET                             ; 26DD C9       .   End SCROLL_BUILDING

;=============================================================================
;=============================================================================
Lb355:  LD      A,(FLOOR_GROUP)         ; 26DE 3A3081   : . Get the working floor group
        CP      $F5                     ; 26E1 FEF5     ..
        JR      NZ,Lb467                ; 26E3 3007     0F

        LD      A,$01                   ; 26E5 3E01     >.
        LD      ($82AC),A               ; 26E7 32AC82   2.}
        JR      Lb468                   ; 26EA 1819     .I

Lb467:  LD      C,$19                   ; 26EC 0E19     .I
        LD      A,(FLOOR_GROUP_IDX)     ; 26EE 3ADC80   :.. Get the current building floor group
        CP      $02                     ; 26F1 FE02     .G
        JR      NZ,Lb469                ; 26F3 2002      G

        LD      C,$08                   ; 26F5 0E08     .L

Lb469:  LD      A,($817E)               ; 26F7 3A7E81   :..
        LD      B,A                     ; 26FA 47       G
        LD      A,(FLOOR_NUM)           ; 26FB 3A3181   :a. Get the working floor number
        SUB     B                       ; 26FE 90       .
        CP      C                       ; 26FF B9       .
        LD      A,$01                   ; 2700 3E01     >.
        JR      NZ,Lb468                ; 2702 3001     0.

        XOR     A                       ; 2704 AF       .

Lb468:  LD      ($82AC),A               ; 2705 32AC82   2.}
        LD      A,($814C)               ; 2708 3A4C81   :..
        CP      $00                     ; 270B FE00     .D
        JR      Z,Lb470                 ; 270D 2832     ('

        JP      M,Lb471                 ; 270F FA1627   .S"

        LD      B,$01                   ; 2712 0601     ..	Move the sprites up one
        JR      Lb472                   ; 2714 1802     ..

Lb471:  LD      B,$FF                   ; 2716 06FF     ..	Move the sprites down one

Lb472:  CALL    MOVE_SPRITES_Y          ; 2718 CD4227   ..f
        LD      A,(FLOOR_NUM)           ; 271B 3A3181   :a. Get the working floor number
        ADD     A,B                     ; 271E 80       .
        LD      (FLOOR_NUM),A           ; 271F 323181   2a. Save the new working floor number
        LD      B,A                     ; 2722 47       G
        LD      A,($817E)               ; 2723 3A7E81   :..
        CP      B                       ; 2726 B8       .
        JR      NZ,Lb470                ; 2727 2018      .

        SUB     $08                     ; 2729 D608     .L
        LD      ($817E),A               ; 272B 327E81   2..
        CALL    DRAW_BLDG_FLOOR         ; 272E CDFC1F   ... Draw the next building floor
        CALL    Lb474                   ; 2731 CD8A27   .."
        LD      A,(FLOOR_NUM)           ; 2734 3A3181   :a. Get the working floor number
        AND     A                       ; 2737 A7       .   Are we back to the start?
        JR      NZ,Lb470                ; 2738 2007      .  Yes, then we are not finished with the group

; Go to next floor group
        LD      A,(FLOOR_GROUP)         ; 273A 3A3081   : . Get the working floor group
        DEC     A                       ; 273D 3D       =   Decrement value
        LD      (FLOOR_GROUP),A         ; 273E 323081   2 . Save the new working floor group

Lb470:  RET                             ; 2741 C9       .

;=============================================================================
; Updates the Y position of the BIG_SPRITE_CONTROL by adding the current
; Y position with B (input). It also updates the UNKNOWN_815C sprite Y 
; positions the same way, if UNKNOWN_815C[0] != 0.
;
; Input:
;	B contains the Y position change for sprite item 0
;=============================================================================
MOVE_SPRITES_Y:  
        LD      HL,UNKNOWN_815C         ; 2742 215C81   !..
        LD      DE,SPRITE_CTRL          ; 2745 118098   ...  Destination address for block copy - sprite control
        LD      IX,$815F                ; 2748 DD215F81 .!.. Y Position in item 0 of UNKNOWN_815C
        LD      C,$04                   ; 274C 0E04     ..	 4 Sprites to update

Lb478:  LD      A,(HL)                  ; 274E 7E       ~
        CP      $00                     ; 274F FE00     .D	is UNKNOWN_815C[0] = 0?
        JR      Z,Lb475                 ; 2751 2807     (F	Yes, go here

        LD      A,(IX+$00)              ; 2753 DD7E00   .~D	Add B to the Y position of UNKNOWN_815C (item 0)
        ADD     A,B                     ; 2756 80       .	
        LD      (IX+$00),A              ; 2757 DD7700   .wD

Lb475:  PUSH    BC                      ; 275A C5       .	Save BC
        LD      A,(HL)                  ; 275B 7E       ~
        CP      $F0                     ; 275C FEF0     ..	is UNKNOWN_815C[0] != $F0?
        INC     HL                      ; 275E 23       #   Source address for block copy UNKNOWN_815C[1]
        JR      NZ,Lb476                ; 275F 2009      .  Is HL != 0? Yup, continue and copy data

        LD      BC,$04                  ; 2761 010400   .TD
        ADD     HL,BC                   ; 2764 09       .	HL = UNKNOWN_815C[5]
        EX      DE,HL                   ; 2765 EB       .	HL = SPRITE_CTRL
        ADD     HL,BC                   ; 2766 09       .	Go to next SPRITE_CTRL
        EX      DE,HL                   ; 2767 EB       .	DE = Next SPRITE_CTRL
        JR      Lb477                   ; 2768 1806     .G	Go here

; Copy data to sprite control (8 groups of 4 bytes)
Lb476:  LD      BC,$04                  ; 276A 010400   ..D  Copy 4 bytes of data
        CALL    BLOCK_COPY              ; 276D CD4A04   .K.  Block copy routine

Lb477:  LD      BC,$03                  ; 2770 010300   .SD
        ADD     HL,BC                   ; 2773 09       .	HL = UNKNOWN_815C[5+3] (next item)
        LD      BC,$08                  ; 2774 010800   .LD
        ADD     IX,BC                   ; 2777 DD09     ..	IX = Y position of the next UNKNOWN_815C item
        POP     BC                      ; 2779 C1       .	Restore BC
        DEC     C                       ; 277A 0D       .	Have we processed the 4 sprites?
        JR      NZ,Lb478                ; 277B 20D1      .	No, go here

        LD      A,(BIG_SPRITE_CTRL)     ; 277D 3ADC98   :..  Read big sprite number (priority?)
        AND     A                       ; 2780 A7       .	Is it zero?
        RET     Z                       ; 2781 C8       .	yes, return MOVE_SPRITES_Y

        LD      A,($98DE)               ; 2782 3ADE98   :..	BIG_SPRITE_CONTROL, Y position
        ADD     A,B                     ; 2785 80       .	Add B to the Y position
        LD      ($98DE),A               ; 2786 32DE98   2..
        RET                             ; 2789 C9       .	Done with MOVE_SPRITES_Y


;=============================================================================
;=============================================================================
Lb474:  LD      A,(ISR_MODE_IDX)        ; 278A 3A5B81   :..	Get ISR mode index
        CP      $01                     ; 278D FE01     ..	Are we starting to climb a building?
        RET     Z                       ; 278F C8       .	Yes, return

        LD      A,($817E)               ; 2790 3A7E81   :>.
        AND     $0F                     ; 2793 E60F     .N
        RET     NZ                      ; 2795 C0       .

        LD      A,(STEP_POINT1)         ; 2796 3AE080   :..
        LD      B,A                     ; 2799 47       G
        LD      A,(STEP_POINT2)         ; 279A 3AE180   :..
        LD      C,A                     ; 279D 4F       O
        CALL    Lb224                   ; 279E CDA527   ..f
        CALL    SHOW_CURRENT_SCORE      ; 27A1 CDDD27   ."" Show the current scores on screen
        RET                             ; 27A4 C9       .

;=============================================================================
;=============================================================================
Lb224:  LD      A,(GAME_IN_PROGRESS)    ; 27A5 3A7580   :5. Is there a game in progress?
        OR      A                       ; 27A8 B7       .
        RET     Z                       ; 27A9 C8       .   Nope, return

; Game in progress
        LD      HL,$80DB                ; 27AA 21DB80   !..
        LD      A,C                     ; 27AD 79       y
        ADD     A,(HL)                  ; 27AE 86       .
        DAA                             ; 27AF 27       '
        LD      (HL),A                  ; 27B0 77       w
        DEC     HL                      ; 27B1 2B       +
        LD      A,B                     ; 27B2 78       x
        ADC     A,(HL)                  ; 27B3 8E       .
        DAA                             ; 27B4 27       '
        LD      (HL),A                  ; 27B5 77       w
        DEC     HL                      ; 27B6 2B       +
        LD      A,$00                   ; 27B7 3E00     >D
        ADC     A,(HL)                  ; 27B9 8E       .
        DAA                             ; 27BA 27       '
        LD      (HL),A                  ; 27BB 77       w

        LD      A,(XTRA_LIFE_FLAG)      ; 27BC 3ADE80   :.. Get extra life flag
        OR      A                       ; 27BF B7       .   Have we got an extra life yet?
        RET     NZ                      ; 27C0 C0       .   Yes, return

; Check score for an extra life
        LD      A,(BONUS_LIFE_SCORE)    ; 27C1 3A7D80   :=. Read bonus life score value
        LD      B,A                     ; 27C4 47       G   B = A
        LD      A,(CUR_SCORE)           ; 27C5 3AD980   :.. Read the current score value (most sig. byte)
        CP      B                       ; 27C8 B8       .   Current score < extra life score?
        RET     C                       ; 27C9 D8       .   Yes, return

;------------
; Add a life
;------------
        LD      HL,CUR_NUM_LIVES        ; 27CA 21D880   !.. Point to current number of lives
        INC     (HL)                    ; 27CD 34       4   Increment number of lives
        CALL    DISPLAY_LIVES           ; 27CE CDDD1F   ... Display number of lives

        LD      BC,$100                 ; 27D1 010001   .D.	Play new life sound
        CALL    LOAD_SOUND_DATA         ; 27D4 CDBB11   ..A

        LD      A,$01                   ; 27D7 3E01     >.
        LD      (XTRA_LIFE_FLAG),A      ; 27D9 32DE80   2.. Mark flag - we have our extra life
        RET                             ; 27DC C9       .


;=============================================================================
; Shows the current score in the proper player 1 or player 2 spot on screen.
;
;=============================================================================
SHOW_CURRENT_SCORE:  
        LD      A,(CURRENT_PLAYER)      ; 27DD 3A8180   :.. Check current player
        OR      A                       ; 27E0 B7       .
        JR      NZ,Lb479                ; 27E1 2007      F  Player 2, go here

; Show current score in player 1 position
        LD      DE,$27F3                ; 27E3 11F327   .." Point to player 1 score value
        CALL    WRITE_DIGITS            ; 27E6 CDC504   ..T Write digits to the screen
        RET                             ; 27E9 C9       .

; Show current score in player 2 position
Lb479:  LD      DE,$27F9                ; 27EA 11F927   ..f Point to player 2 score value
        CALL    WRITE_DIGITS            ; 27ED CDC504   .:. Write digits to the screen

        RET                             ; 27F0 C9       .   End SHOW_CURRENT_SCORE


;-------------------------------------------------------------------------------
; Data for displaying the current score in the player 1 or player 2 location
; Range: $27F1 - $2800
; Number of bytes: 16
;-------------------------------------------------------------------------------

        .db     $C7, $FB						; Start data block

; $27F3 - Shows current score in player 1 position
        .db     NOCHANGE_CHAR_COLOR				; Do not change color
		.db     $09								; Row 9
		.db     $02								; Column 2
		.db     $D9, $80						; Address $80D9 - Current score
		.db     $06								; 6 digits
		
; $27F9	- Show current score in player 2 position
        .db     NOCHANGE_CHAR_COLOR				; Do not change color
		.db     $0D								; Row 13
        .db     $02								; Column 2
		.db     $D9, $80						; Address $80D9 - Current score
		.db     $06								; 6 digits

        .db     $C7, $F3						; End data block

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------

        NOP                             ; 2801 00       .
        NOP                             ; 2802 00       .
        NOP                             ; 2803 00       .
        NOP                             ; 2804 00       .
        NOP                             ; 2805 00       .
        NOP                             ; 2806 00       .
        NOP                             ; 2807 00       .
        NOP                             ; 2808 00       .
        NOP                             ; 2809 00       .
        NOP                             ; 280A 00       .
        NOP                             ; 280B 00       .
        NOP                             ; 280C 00       .
        NOP                             ; 280D 00       .
        NOP                             ; 280E 00       .
        NOP                             ; 280F 00       .

;-----------------------------------------------------------------------------
; Called from $02B7
; (Index 3 in the jump table)
;
; Checks and services various building actions like:
; Dr. Droppers
; King Kong
; Evil Bird
; Helicopter
; Balloon
; Electric Sign
; Falling Sign
;
; Address $2810
;-----------------------------------------------------------------------------
ISR_JUMP3:
        LD      A,(ISR_JUMP3_CNTR1)     ; 2810 3A2081   :d.	Decrement ISR counter 1
        DEC     A                       ; 2813 3D       =
        LD      (ISR_JUMP3_CNTR1),A     ; 2814 322081   2d.
        JR      NZ,Lb481                ; 2817 201A      .	Is this != 0? Yes, go here

        CALL    UPDATE_BONUS_RATE       ; 2819 CD3E11   .{A	Update (decrement) the bonus rate
        LD      A,(ISR_JUMP3_CNTR2)     ; 281C 3A2181   :0.	Decrement ISR counter 2
        DEC     A                       ; 281F 3D       =
        LD      (ISR_JUMP3_CNTR2),A     ; 2820 322181   20.
        JR      NZ,Lb481                ; 2823 200E      .	Is this != 0? Yes, go here

        CALL    INIT_ISR_JUMP3_COUNTERS ; 2825 CD9411   ..A	Re-initialize the ISR counters
        LD      A,(ISR_JUMP3_CNTR3)     ; 2828 3ABA82   :..
        CP      $07                     ; 282B FE07     .F	Is ISR_JUMP3_CNTR3 = 7?
        JR      Z,Lb481                 ; 282D 2804     (T	Yes, continue

        INC     A                       ; 282F 3C       <	No, increment ISR_JUMP3_CNTR3
        LD      (ISR_JUMP3_CNTR3),A     ; 2830 32BA82   2..

Lb481:  LD      A,($82B8)               ; 2833 3AB882   :.}	Is $82B8 = 0?
        CP      $00                     ; 2836 FE00     .D
        JP      Z,Lb483                 ; 2838 CA6328   .vl	Yes, go here (do not execute a building action)

        CP      $FF                     ; 283B FEFF     ..	Is $82B8 = $FF?
        JP      Z,Lb484                 ; 283D CA9828   ..l	Yes, go here (do not execute a building action)

        CALL    Lb485                   ; 2840 CD702A   .!o	???
        LD      A,(FLOOR_GROUP_IDX)     ; 2843 3ADC80   :.. A = FLOOR_GROUP_IDX / 4
        RRCA                            ; 2846 0F       .	
        RRCA                            ; 2847 0F       .
        AND     $3F                     ; 2848 E63F     ..	Limit to <= 63
        LD      B,A                     ; 284A 47       G	B = FLOOR_GROUP_IDX / 4
        LD      A,($82DB)               ; 284B 3ADB82   :.}	Is $82DB = 7?
        CP      $07                     ; 284E FE07     ..
        JR      Z,Lb486                 ; 2850 2809     (.	Yes, go here

        CP      B                       ; 2852 B8       .	Is (FLOOR_GROUP_IDX / 4) = 0?
        JR      Z,Lb486                 ; 2853 2806     (.	Yes, go here

        CALL    CHECK_DUMBELLS          ; 2855 CD8B33   ..2	Check dumbells / girders
        JP      Lb488                   ; 2858 C3A328   .\l	Go to end of ISR_JUMP3

;-----------------------------------------------------------------------------------------
; Execute the building action code (King kong, helicopter, bird, falling signs, etc)
;
; Note this jumps to the action code.  The action code has a return, so the
; return uses the $28A3 return value pushed onto the stack. This goes to the end
; of the ISR_JUMP3 ISR.
;-----------------------------------------------------------------------------------------
Lb486:  LD      HL,(ISR_JUMP3_ACTION)   ; 285B 2ADC82   *.}	HL = ISR_JUMP3_ACTION
        LD      DE,$28A3                ; 285E 11A328   .\l
        PUSH    DE                      ; 2861 D5       .	Push $28A3 (end of ISR_JUMP3)
        JP      (HL)                    ; 2862 E9       .	Jump to (ISR_JUMP3_ACTION)

Lb483:  LD      A,(FLOOR_GROUP_IDX)     ; 2863 3ADC80   :.. A = FLOOR_GROUP_IDX / 4
        RRCA                            ; 2866 0F       .
        RRCA                            ; 2867 0F       .
        AND     $3F                     ; 2868 E63F     ..	Limit to <= 63
        LD      B,A                     ; 286A 47       G	B = FLOOR_GROUP_IDX / 4
        LD      A,($82DB)               ; 286B 3ADB82   :.}
        CP      B                       ; 286E B8       .	Is ($82DB) = FLOOR_GROUP_IDX / 4?
        JR      NZ,Lb489                ; 286F 3004     0T	No, go here

        LD      A,B                     ; 2871 78       x	($82DB) = FLOOR_GROUP_IDX / 4
        LD      ($82DB),A               ; 2872 32DB82   2..	

Lb489:  LD      E,A                     ; 2875 5F       _	E = FLOOR_GROUP_IDX / 4
        LD      D,$00                   ; 2876 1600     .D	D = 0
        LD      A,(BUILDING_NUMBER)     ; 2878 3ADF80   :.. A = 8 * BUILDING_NUMBER
        RLCA                            ; 287B 07       .
        RLCA                            ; 287C 07       .
        RLCA                            ; 287D 07       .
        ADD     A,E                     ; 287E 83       .	A = (8 * BUILDING_NUMBER) + (FLOOR_GROUP_IDX / 4)
        LD      E,A                     ; 287F 5F       _	E = A (Offset)
        LD      HL,ISR_JUMP3_OFFSET_TBL ; 2880 21C028   !.l Point to the offset table
        ADD     HL,DE                   ; 2883 19       .	HL = Table + Offset
        LD      E,(HL)                  ; 2884 5E       ^	E = (HL)

        LD      HL,ISR_JUMP3_ACTION_TBL ; 2885 21A828   !.l Point to action table
        ADD     HL,DE                   ; 2888 19       .	HL = Table + Offset
        LD      E,(HL)                  ; 2889 5E       ^	E = (HL)
        INC     HL                      ; 288A 23       #	HL++
        LD      D,(HL)                  ; 288B 56       V	D = (HL)
        EX      DE,HL                   ; 288C EB       .	DE <-> HL (swap)
        LD      (ISR_JUMP3_ACTION),HL   ; 288D 22DC82   ".} ISR_JUMP3_ACTION = HL
        LD      A,$01                   ; 2890 3E01     >.
        LD      ($82B8),A               ; 2892 32B882   2..	($82B8) = 1
        JP      Lb488                   ; 2895 C3A328   ..l	Go to end of ISR

Lb484:  XOR     A                       ; 2898 AF       .
        LD      ($82B8),A               ; 2899 32B882   2.}	($82B8) = 0
        LD      A,($82DB)               ; 289C 3ADB82   :..	Increment ($82DB)
        INC     A                       ; 289F 3C       <
        LD      ($82DB),A               ; 28A0 32DB82   2..

Lb488:  CALL    Lb208                   ; 28A3 CD0F03   .NS Does not return from this call


;-------------------------------------------------------------------------------
; Data Start
; Range: $28A6 - $2901
; Number of bytes: 92
;-------------------------------------------------------------------------------

        .db     $C7, $FB			; Start data block

;-------------------------------------------------------------------------------
; This jump table corresponds to actions encountered when climbing up the 
; building.  The actual jump is defined in the ISR_JUMP3_OFFSET_TBL table
; below.
;
; $28A8
;-------------------------------------------------------------------------------
ISR_JUMP3_ACTION_TBL:
        .db     $02, $29			; 00 ISR_JUMP3_DROP_1 (one Dr. Dropper)
		.db		$08, $29			; 02 ISR_JUMP3_DROP_2 (two Dr. Droppers)
		.db		$0E, $29			; 04 ISR_JUMP3_DROP_3 (three Dr. Droppers)
		.db		$9A, $33			; 06 ISR_JUMP3_BIRD
        .db     $EB, $2E			; 08 ISR_JUMP3_KING_KONG
		.db		$30, $37			; 0A ISR_JUMP3_DUMBELLS
		.db		$30, $37			; 0C ISR_JUMP3_DUMBELLS
		.db		$DB, $38			; 0E ISR_JUMP3_BALLOON
        .db     $66, $3B			; 10 ISR_JUMP3_ELECTRIC_SIGN
		.db		$04, $3E			; 12 ISR_JUMP3_FALLING_SIGN
		.db		$1A, $2C			; 14 ISR_JUMP3_HELICOPTER
		.db		$80, $33			; 16 ISR_JUMP3_DELAY

;-------------------------------------------------------------------------------
; Location for this offset table is calculated as:
; (8 * BUILDING_NUMBER) + (FLOOR_GROUP_IDX / 4)
;
; The value selected is used as an offset into in the action table above.
; $28C0
;-------------------------------------------------------------------------------
ISR_JUMP3_OFFSET_TBL:
        .db     $16, $00, $06, $02, $08, $04, $14, $14	; Building 1
        .db     $16, $04, $0A, $06, $10, $0E, $14, $14	; Building 2
        .db     $16, $04, $0C, $12, $08, $0E, $14, $14	; Building 3
        .db     $16, $10, $06, $04, $0C, $12, $14, $14	; Building 4
        .db     $16, $0A, $04, $0C, $08, $12, $14, $14	; Building 5
        .db     $16, $04, $06, $12, $10, $0E, $14, $14	; Building 6
        .db     $16, $04, $06, $0C, $12, $0E, $14, $14	; Building 7
        .db     $16, $10, $12, $06, $0C, $10, $14, $14	; Building 8

        .db     $C7, $F3			; End data block

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------


;-------------------------------------------------------------------------------
; Set up Dr. Droppers (1, 2 or 3)
;-------------------------------------------------------------------------------
ISR_JUMP3_DROP_1:
        LD      A,$0A                   ; 2902 3E0A     >.
        LD      B,$01                   ; 2904 0601     ..	; 1 Dr. Dropper?
        JR      Lb495                   ; 2906 180A     ..

;-------------------------------------------------------------------------------
;-------------------------------------------------------------------------------
ISR_JUMP3_DROP_2:
        LD      A,$08                   ; 2908 3E08     >L
        LD      B,$02                   ; 290A 0602     ..	; 2 Dr. Droppers?
        JR      Lb495                   ; 290C 1804     ..

;-------------------------------------------------------------------------------
;-------------------------------------------------------------------------------
ISR_JUMP3_DROP_3:        
		LD      A,$05                   ; 290E 3E05     >U
        LD      B,$03                   ; 2910 0603     .S	; 3 Dr. Droppers?

Lb495:  LD      ($82A3),A               ; 2912 32A382   2\.
        LD      A,(ISR_JUMP3_CNTR3)     ; 2915 3ABA82   :.}
        AND     $04                     ; 2918 E604     ..	Is ISR_JUMP3_CNTR3 = 4?
        JR      Z,Lb496                 ; 291A 2801     (.	Yes, go here

        INC     B                       ; 291C 04       .	B = B+1 (# droppers)

Lb496:  LD      A,B                     ; 291D 78       x
        LD      ($82A4),A               ; 291E 32A482   2.. ($82A4) = B
        NOP                             ; 2921 00       .
        LD      A,(FLOOR_GROUP_IDX)     ; 2922 3ADC80   :.. Get the current building floor group
        AND     $03                     ; 2925 E603     ..	Limit floor group to <= 3
        CP      $03                     ; 2927 FE03     ..	Is floor group != 3?
        JR      NZ,Lb499                ; 2929 2006      .	Yes, go here

        LD      A,$FF                   ; 292B 3EFF     >.	($82B8) = $FF
        LD      ($82B8),A               ; 292D 32B882   2.}
        RET                             ; 2930 C9       .

Lb499:  CALL    HANDLE_DROPPERS         ; 2931 CD3529   .p8
        RET                             ; 2934 C9       .

;-------------------------------------------------------------------------------
; Handle Droppers
;-------------------------------------------------------------------------------
HANDLE_DROPPERS:
        LD      A,$01                   ; 2935 3E01     >.
        LD      (KEEP_SAME_ISR_FLAG),A  ; 2937 324480   2@.  Keep processing the same ISR table location
        LD      A,(FLOOR_NUM)           ; 293A 3A3181   :a.  Get the working floor number
        AND     $0F                     ; 293D E60F     .N	 Is FLOOR_NUM != 0?
        JP      NZ,Lb501                ; 293F C26B2A   .>.	 Yes, done processing

        LD      A,($82A4)               ; 2942 3AA482   :..	 C = # droppers + 1 (loop counter)
        LD      C,A                     ; 2945 4F       O
        LD      IX,UNKNOWN_815C         ; 2946 DD215C81 .!..
        LD      IY,UNKNOWN_8283         ; 294A FD218382 .!.}	IY = $8283

; Loop
Lb504:  LD      A,(IX+$00)              ; 294E DD7E00   .~D
        CP      $00                     ; 2951 FE00     .D	 Is ($815C+$00) != 0?
        JR      NZ,Lb502                ; 2953 2007      F	 Yes, go here

        LD      A,(IY+$06)              ; 2955 FD7E06   .~G	 
        CP      $01                     ; 2958 FE01     ..	 Is ($8283+$06) != 1?
        JR      NZ,Lb503                ; 295A 200D      ]	 Yes, go here (create a new dropper?)

Lb502:  DEC     C                       ; 295C 0D       .	 Decrement loop counter (# droppers+1)
        JP      Z,Lb501                 ; 295D CA6B2A   .>.	 Are we done? Yes, done processing

        LD      DE,$08                  ; 2960 110800   .LD	 Go to next group
        ADD     IX,DE                   ; 2963 DD19     ..
        ADD     IY,DE                   ; 2965 FD19     ..
        JR      Lb504                   ; 2967 18E5     ..	 Keep looping

; Create a new dropper?
Lb503:  PUSH    BC                      ; 2969 C5       .	Save BC - C is the loop counter
        LD      HL,PLAYFIELD            ; 296A 218181   !..	Point to the playfield
        LD      A,(FLOOR_NUM)           ; 296D 3A3181   :a. Get the working floor number
        AND     $F0                     ; 2970 E6F0     ..	A = FLOOR_NUM & $F0
        ADD     A,$10                   ; 2972 C610     ..	A = (FLOOR_NUM & $F0) + $10
        RRCA                            ; 2974 0F       .	A = ((FLOOR_NUM & $F0) + $10) / 2
        LD      B,A                     ; 2975 47       G	B = ((FLOOR_NUM & $F0) + $10) / 2
        LD      A,(RANDOM_NUMBER)       ; 2976 3A2281   :&. Get a random number
        AND     $07                     ; 2979 E607     .F	Isolate bits 0, 1, and 2
        RLCA                            ; 297B 07       .	A = (RANDOM & $07) * 8
        RLCA                            ; 297C 07       .
        RLCA                            ; 297D 07       .
        LD      C,A                     ; 297E 4F       O	C = (RANDOM & $07) * 8
        ADD     A,B                     ; 297F 80       .	A = ((RANDOM & $07) * 8) + ((FLOOR_NUM & $F0) + $10) / 2
        AND     $7F                     ; 2980 E67F     .+	A = $7F & (((RANDOM & $07) * 8) + ((FLOOR_NUM & $F0) + $10) / 2)
        LD      E,A                     ; 2982 5F       _	E = $7F & (((RANDOM & $07) * 8) + ((FLOOR_NUM & $F0) + $10) / 2)
        LD      D,$00                   ; 2983 1600     .D
        ADD     HL,DE                   ; 2985 19       .	HL = PLAYFIELD + ($7F & (((RANDOM & $07) * 8) + ((FLOOR_NUM & $F0) + $10) / 2))
        PUSH    HL                      ; 2986 E5       .	Save HL
        LD      A,C                     ; 2987 79       y	A = (RANDOM & $07) * 8
        RLCA                            ; 2988 07       .	A = (RANDOM & $07) * 16
        LD      C,A                     ; 2989 4F       O	C = (RANDOM & $07) * 16
        LD      A,$F0                   ; 298A 3EF0     >.
        SUB     C                       ; 298C 91       .	A = $F0 - ((RANDOM & $07) * 16)
        LD      (IX+$03),A              ; 298D DD7703   .wS	($815C+$03) = $F0 - ((RANDOM & $07) * 16)
        LD      A,(FLOOR_NUM)           ; 2990 3A3181   :a. Get the working floor number
        ADD     A,C                     ; 2993 81       .	A = FLOOR_NUM + ((RANDOM & $07) * 16)
        LD      E,A                     ; 2994 5F       _	E = FLOOR_NUM + ((RANDOM & $07) * 16)
        LD      D,$00                   ; 2995 1600     .D
        LD      HL,$9027                ; 2997 212790   !f.	Point to screen ram (non-visible area)
        ADD     HL,DE                   ; 299A 19       .	HL = 4 * (FLOOR_NUM + ((RANDOM & $07) * 16))
        ADD     HL,DE                   ; 299B 19       .
        ADD     HL,DE                   ; 299C 19       .
        ADD     HL,DE                   ; 299D 19       .
        LD      (IY+$01),L              ; 299E FD7501   .u.	($8283+$01) = Calculated screen position 
        LD      (IY+$02),H              ; 29A1 FD7402   .t.	($8283+$02) = Calculated screen position
        POP     HL                      ; 29A4 E1       .	Restore HL
        POP     BC                      ; 29A5 C1       .	Restore BC
        DEC     C                       ; 29A6 0D       .	Decrement our counter (# droppers)
        JP      NZ,Lb505                ; 29A7 C2BA29   ..8 Not done? Go here

; Find the climber right-leg X position. We start at $60 and keep incrementing by $18
; until it is found. The count is C (i.e. C = 1 if it was $60, C = 2 if it was $78, etc)
        LD      C,$01                   ; 29AA 0E01     ..	C = 1
        LD      A,($8139)               ; 29AC 3A3981   :i. Climber right leg X position
        LD      B,A                     ; 29AF 47       G	B = RightLegXPosition
        LD      A,$60                   ; 29B0 3E60     >4	A = $60 (starting position to check

Lb507:  CP      B                       ; 29B2 B8       .	Is RightLegXPosition = A?
        JR      NZ,Lb506                ; 29B3 300E     0.	No, go here
        ADD     A,$18                   ; 29B5 C618     ..	A = A + $18
        INC     C                       ; 29B7 0C       .	Keep count
        JR      Lb507                   ; 29B8 18F8     ..	Keep looping

Lb505:  LD      A,(RANDOM_NUMBER)       ; 29BA 3A2281   :&. Get a random number
        RLCA                            ; 29BD 07       .	A = RANDOM_NUMBER * 4
        RLCA                            ; 29BE 07       .
        AND     $03                     ; 29BF E603     ..	A = $03 & (RANDOM_NUMBER * 4)
        INC     A                       ; 29C1 3C       <	A = 1 + ($03 & (RANDOM_NUMBER * 4))
        LD      C,A                     ; 29C2 4F       O	C = 1 + ($03 & (RANDOM_NUMBER * 4))

Lb506:  LD      B,$00                   ; 29C3 0600     .D

Lb510:  LD      A,(HL)                  ; 29C5 7E       ~	Get value at the playfiled location
        CP      $00                     ; 29C6 FE00     .D	Is value zero?
        JR      Z,Lb508                 ; 29C8 2809     (.	Yes, go here

Lb511:  INC     HL                      ; 29CA 23       #	Go to next playfield location
        INC     D                       ; 29CB 14       .	D += 1
        LD      A,$07                   ; 29CC 3E07     >.	A = $07
        CP      D                       ; 29CE BA       .	Is D = A?
        JR      Z,Lb509                 ; 29CF 280C     (\	Yes, go here
        JR      Lb510                   ; 29D1 18F2     ..	No, go here

Lb508:  LD      B,D                     ; 29D3 42       B
        LD      (IY+$03),L              ; 29D4 FD7503   .u.
        LD      (IY+$04),H              ; 29D7 FD7404   .t.
        DEC     C                       ; 29DA 0D       .
        JR      NZ,Lb511                ; 29DB 20ED      .

Lb509:  XOR     A                       ; 29DD AF       .
        CP      B                       ; 29DE B8       .
        JP      Z,Lb501                 ; 29DF CA6B2A   .>.
        LD      L,(IY+$03)              ; 29E2 FD6E03   .n.
        LD      H,(IY+$04)              ; 29E5 FD6604   .f.
        LD      (HL),$FF                ; 29E8 36FF     6.
        LD      A,B                     ; 29EA 78       x
        RLCA                            ; 29EB 07       .
        RLCA                            ; 29EC 07       .
        RLCA                            ; 29ED 07       .
        LD      C,A                     ; 29EE 4F       O
        RLCA                            ; 29EF 07       .
        ADD     A,C                     ; 29F0 81       .
        ADD     A,$38                   ; 29F1 C638     .9
        LD      (IX+$04),A              ; 29F3 DD7704   .w.
        LD      A,B                     ; 29F6 78       x
        RLCA                            ; 29F7 07       .
        ADD     A,B                     ; 29F8 80       .
        LD      B,(IY+$01)              ; 29F9 FD4601   .F.
        ADD     A,B                     ; 29FC 80       .
        LD      (IY+$01),A              ; 29FD FD7701   .w.
        LD      (IX+$00),$F0            ; 2A00 DD3600F0 .6D.
        LD      (IX+$06),$05            ; 2A04 DD360605 .6.U
        LD      (IX+$07),$01            ; 2A08 DD360701 .6F.
        LD      A,($82A3)               ; 2A0C 3AA382   :\.
        LD      (IY+$00),A              ; 2A0F FD7700   .wD
        LD      (IY+$07),$01            ; 2A12 FD360701 .6F.
        LD      A,(RANDOM_NUMBER)       ; 2A16 3A2281   :&.  Get a random number
        AND     $03                     ; 2A19 E603     ..
        LD      B,A                     ; 2A1B 47       G
        LD      A,$20                   ; 2A1C 3E20     >d
        ADD     A,B                     ; 2A1E 80       .
        LD      (IX+$01),A              ; 2A1F DD7701   .w.
        INC     B                       ; 2A22 04       .
        BIT     1,B                     ; 2A23 CB48     .H
        LD      B,$03                   ; 2A25 0603     ..
        JR      Z,Lb512                 ; 2A27 2802     (G
        LD      B,$00                   ; 2A29 0600     .D

Lb512:  LD      A,(BUILDING_NUMBER)     ; 2A2B 3ADF80   :..
        BIT     0,A                     ; 2A2E CB47     .G
        LD      A,B                     ; 2A30 78       x
        JR      Z,Lb513                 ; 2A31 2802     (G
        ADD     A,$10                   ; 2A33 C610     ..

Lb513:  LD      (IX+$02),A              ; 2A35 DD7702   .w.
        LD      (IY+$06),$01            ; 2A38 FD360601 .6..
        LD      (IY+$05),$00            ; 2A3C FD360500 .6.D
        LD      A,(BUILDING_NUMBER)     ; 2A40 3ADF80   :..	DE = BUILDING_NUMBER
        LD      E,A                     ; 2A43 5F       _
        LD      D,$00                   ; 2A44 1600     .D
        LD      HL,$2BE6                ; 2A46 21E62B   !.:	
        ADD     HL,DE                   ; 2A49 19       .	HL = $2BE6 + BUILDING_NUMBER
        LD      C,(HL)                  ; 2A4A 4E       N	C = (HL) (read table)
        LD      L,(IY+$01)              ; 2A4B FD6E01   .n.
        LD      H,(IY+$02)              ; 2A4E FD6602   .fG
        PUSH    HL                      ; 2A51 E5       .
        POP     IX                      ; 2A52 DDE1     ..	IX = HL
        LD      DE,$C00                 ; 2A54 11000C   .D\
        ADD     HL,DE                   ; 2A57 19       .	HL = $0C00 + ??
        LD      (HL),C                  ; 2A58 71       q
        INC     HL                      ; 2A59 23       #
        LD      (HL),C                  ; 2A5A 71       q
        LD      (IX+$00),$90            ; 2A5B DD360090 .6D.
        LD      (IX+$01),$91            ; 2A5F DD360191 .6..
        LD      (IX+$20),$92            ; 2A63 DD362092 .6d.
        LD      (IX+$21),$93            ; 2A67 DD362193 .60.

; Done processing
Lb501:  XOR     A                       ; 2A6B AF       .
        LD      (KEEP_SAME_ISR_FLAG),A  ; 2A6C 324480   2.. Process the next ISR table location
        RET                             ; 2A6F C9       .	End HANDLE_DROPPERS

;-------------------------------------------------------------------------------
;-------------------------------------------------------------------------------
Lb485:  LD      IX,UNKNOWN_815C         ; 2A70 DD215C81 .!..
        LD      IY,UNKNOWN_8283         ; 2A74 FD218382 .!.}
        LD      B,$04                   ; 2A78 0604     ..

Lb521:  PUSH    BC                      ; 2A7A C5       .
        LD      A,(IX+$00)              ; 2A7B DD7E00   .~D
        CP      $00                     ; 2A7E FE00     .D
        JR      NZ,Lb514                ; 2A80 2007      .
        LD      A,(IY+$06)              ; 2A82 FD7E06   .~.
        CP      $01                     ; 2A85 FE01     ..
        JR      NZ,Lb515                ; 2A87 201C      .

Lb514:  LD      A,(IY+$07)              ; 2A89 FD7E07   .~.
        CP      $01                     ; 2A8C FE01     ..
        JR      NZ,Lb516                ; 2A8E 2005      U
        CALL    Lb517                   ; 2A90 CDB12A   ..o
        JR      Lb515                   ; 2A93 1810     ..

Lb516:  CP      $02                     ; 2A95 FE02     .G
        JR      NZ,Lb518                ; 2A97 2005      .
        CALL    Lb519                   ; 2A99 CD7C35   .)q
        JR      Lb515                   ; 2A9C 1807     ..

Lb518:  CP      $03                     ; 2A9E FE03     .S
        JR      NZ,Lb515                ; 2AA0 2003      S
        CALL    Lb520                   ; 2AA2 CD5E37   ..&

Lb515:  POP     BC                      ; 2AA5 C1       .
        DEC     B                       ; 2AA6 05       .
        RET     Z                       ; 2AA7 C8       .

        LD      DE,$08                  ; 2AA8 110800   .LD
        ADD     IX,DE                   ; 2AAB DD19     ..
        ADD     IY,DE                   ; 2AAD FD19     ..
        JR      Lb521                   ; 2AAF 18C9     ..

;=============================================================================
;=============================================================================
Lb517:  LD      A,(IY+$06)              ; 2AB1 FD7E06   .~G
        CP      $01                     ; 2AB4 FE01     ..
        JP      NZ,Lb522                ; 2AB6 C2342B   .`:
        LD      A,(IY+$00)              ; 2AB9 FD7E00   .~D
        SUB     $01                     ; 2ABC D601     ..
        LD      (IY+$00),A              ; 2ABE FD7700   .wD
        JP      NZ,Lb522                ; 2AC1 C2342B   .%{
        LD      A,($82A3)               ; 2AC4 3AA382   :\.
        LD      (IY+$00),A              ; 2AC7 FD7700   .wD
        LD      L,(IY+$01)              ; 2ACA FD6E01   .n.
        LD      H,(IY+$02)              ; 2ACD FD6602   .f.
        PUSH    IX                      ; 2AD0 DDE5     ..
        PUSH    HL                      ; 2AD2 E5       .
        POP     IX                      ; 2AD3 DDE1     ..
        LD      HL,$2C10                ; 2AD5 21102C   !.=
        LD      E,(IY+$05)              ; 2AD8 FD5E05   .^.
        LD      D,$00                   ; 2ADB 1600     .D
        ADD     HL,DE                   ; 2ADD 19       .
        LD      A,(HL)                  ; 2ADE 7E       ~
        LD      (IX+$00),A              ; 2ADF DD7700   .wD
        INC     A                       ; 2AE2 3C       <
        LD      (IX+$01),A              ; 2AE3 DD7701   .w.
        INC     A                       ; 2AE6 3C       <
        CP      $50                     ; 2AE7 FE50     .E
        JR      NZ,Lb523                ; 2AE9 2002      G
        LD      A,$42                   ; 2AEB 3E42     >C

Lb523:  LD      (IX+$20),A              ; 2AED DD7720   .wd
        INC     A                       ; 2AF0 3C       <
        LD      (IX+$21),A              ; 2AF1 DD7721   .w0
        POP     IX                      ; 2AF4 DDE1     ..
        LD      A,(IY+$05)              ; 2AF6 FD7E05   .~.
        INC     A                       ; 2AF9 3C       <
        LD      (IY+$05),A              ; 2AFA FD7705   .w.
        CP      $04                     ; 2AFD FE04     .T
        JR      Z,Lb524                 ; 2AFF 282A     (o
        CP      $08                     ; 2B01 FE08     .L
        JR      NZ,Lb522                ; 2B03 202F      n
        LD      A,(BUILDING_NUMBER)     ; 2B05 3ADF80   :..
        LD      E,A                     ; 2B08 5F       _
        LD      D,$00                   ; 2B09 1600     .D
        LD      HL,BUILDING_COLOR_DATA  ; 2B0B 21DE2B   !.{	Building color data
        ADD     HL,DE                   ; 2B0E 19       .	HL = BUILDING_COLOR_DATA + BldgNumber
        LD      C,(HL)                  ; 2B0F 4E       N	Get color data
        LD      L,(IY+$01)              ; 2B10 FD6E01   .n.
        LD      H,(IY+$02)              ; 2B13 FD6602   .f.
        LD      DE,$C00                 ; 2B16 11000C   .D\
        ADD     HL,DE                   ; 2B19 19       .
        LD      (HL),C                  ; 2B1A 71       q
        INC     HL                      ; 2B1B 23       #
        LD      (HL),C                  ; 2B1C 71       q
        LD      L,(IY+$03)              ; 2B1D FD6E03   .nS
        LD      H,(IY+$04)              ; 2B20 FD6604   .fT
        LD      (HL),$00                ; 2B23 3600     6D
        LD      (IY+$06),$00            ; 2B25 FD360600 .6GD
        JR      Lb522                   ; 2B29 1809     ..

Lb524:  LD      (IX+$05),$01            ; 2B2B DD360501 .6U.
        LD      (IX+$00),$01            ; 2B2F DD360001 .6D.
        RET                             ; 2B33 C9       .

Lb522:  LD      A,(IX+$05)              ; 2B34 DD7E05   .~.
        CP      $02                     ; 2B37 FE02     .G
        JP      Z,Lb525                 ; 2B39 CAA12B   ..{
        CP      $01                     ; 2B3C FE01     ..
        RET     NZ                      ; 2B3E C0       .

        LD      B,(IX+$03)              ; 2B3F DD4603   .FS
        LD      A,(IX+$04)              ; 2B42 DD7E04   .~T
        ADD     A,$05                   ; 2B45 C605     ..
        LD      C,A                     ; 2B47 4F       O
        CALL    Lb526                   ; 2B48 CDC032   ..'
        AND     A                       ; 2B4B A7       .
        JR      NZ,Lb527                ; 2B4C 200A      .
        LD      A,C                     ; 2B4E 79       y
        ADD     A,$05                   ; 2B4F C605     ..
        LD      C,A                     ; 2B51 4F       O
        CALL    Lb526                   ; 2B52 CDC032   ..'
        AND     A                       ; 2B55 A7       .
        JR      Z,Lb528                 ; 2B56 281D     (Y

Lb527:  AND     $80                     ; 2B58 E680     ..
        JR      Z,Lb529                 ; 2B5A 280A     (.
        LD      (IX+$07),$80            ; 2B5C DD360780 .6F.
        LD      (IX+$05),$02            ; 2B60 DD360502 .6..
        JR      Lb530                   ; 2B64 1808     .L

Lb529:  LD      (IX+$07),$00            ; 2B66 DD360700 .6FD
        LD      (IX+$05),$02            ; 2B6A DD360502 .6..

Lb530:  LD      BC,$302                 ; 2B6E 010203   ...	Play Hit by a pot sound
        CALL    LOAD_SOUND_DATA         ; 2B71 CDBB11   ..A
        RET                             ; 2B74 C9       .

Lb528:  DEC     (IX+$06)                ; 2B75 DD3506   .5G
        JR      NZ,Lb531                ; 2B78 200E      O
        LD      (IX+$06),$08            ; 2B7A DD360608 .6.L
        LD      A,(IX+$07)              ; 2B7E DD7E07   .~F
        CP      $04                     ; 2B81 FE04     .T
        JR      NZ,Lb531                ; 2B83 3003     0.
        INC     (IX+$07)                ; 2B85 DD3407   .4.

Lb531:  LD      A,(IX+$03)              ; 2B88 DD7E03   .~.
        SUB     (IX+$07)                ; 2B8B DD9607   ...
        LD      (IX+$03),A              ; 2B8E DD7703   .w.
        LD      A,(IX+$06)              ; 2B91 DD7E06   .~G
        AND     $03                     ; 2B94 E603     .S
        JR      NZ,Lb532                ; 2B96 2043      V
        LD      A,(IX+$01)              ; 2B98 DD7E01   .~.
        XOR     $40                     ; 2B9B EE40     .Q
        LD      (IX+$01),A              ; 2B9D DD7701   .w.
        RET                             ; 2BA0 C9       .

Lb525:  LD      A,(IX+$07)              ; 2BA1 DD7E07   .~.
        BIT     7,A                     ; 2BA4 CB7F     ..
        LD      HL,$2BEE                ; 2BA6 21EE2B   !.:
        JP      Z,Lb533                 ; 2BA9 CAAF2B   .P{
        LD      HL,$2BFF                ; 2BAC 21FF2B   !.:

Lb533:  RLCA                            ; 2BAF 07       .
        AND     $FE                     ; 2BB0 E6FE     ..
        LD      E,A                     ; 2BB2 5F       _
        LD      D,$00                   ; 2BB3 1600     .D
        ADD     HL,DE                   ; 2BB5 19       .
        LD      A,(HL)                  ; 2BB6 7E       ~
        CP      $FF                     ; 2BB7 FEFF     ..
        JR      Z,Lb534                 ; 2BB9 2814     (.
        LD      C,(IX+$03)              ; 2BBB DD4E03   .NS
        ADD     A,C                     ; 2BBE 81       .
        LD      (IX+$03),A              ; 2BBF DD7703   .wS
        INC     HL                      ; 2BC2 23       #
        LD      A,(HL)                  ; 2BC3 7E       ~
        LD      C,(IX+$04)              ; 2BC4 DD4E04   .NT
        ADD     A,C                     ; 2BC7 81       .
        LD      (IX+$04),A              ; 2BC8 DD7704   .wT
        INC     (IX+$07)                ; 2BCB DD3407   .4.
        RET                             ; 2BCE C9       .

Lb534:  LD      (IX+$05),$01            ; 2BCF DD360501 .6U.
        LD      (IX+$06),$05            ; 2BD3 DD360605 .6G.
        LD      (IX+$07),$03            ; 2BD7 DD360703 .6..

Lb532:  RET                             ; 2BDB C9       .



;-------------------------------------------------------------------------------
; Data Start
; Range: $2BDC - $2C19
; Number of bytes: 62
;-------------------------------------------------------------------------------

        .db     $C7, $FB
		
;------------------------------------------------------------------------------
; Building color RAM values
;------------------------------------------------------------------------------
; $2BDE
BUILDING_COLOR_DATA:
        .db     $07		; Building 1, character set 1, palette 7
		.db     $1F		; Building 2, character set 2, palette 15
		.db     $17		; Building 3, character set 2, palette 7
		.db     $0F		; Building 4, character set 1, palette 15
		.db     $17		; Building 5, character set 2, palette 7
		.db     $0F		; Building 6, character set 1, palette 15
		.db     $07		; Building 7, character set 1, palette 7
		.db     $1F		; Building 8, character set 2, palette 15

; $2BE6
        .db     $01
		.db		$19
		.db		$11
		.db		$09
		.db		$11, $09, $01, $19
        .db     $04, $03, $04, $03, $03, $02, $02, $02
        .db     $01, $01, $FE, $02, $FE, $03, $FE, $04
        .db     $FF, $04, $FD, $04, $FD, $03, $FE, $02
        .db     $FE, $01, $FF, $FE, $FE, $FE, $FD, $FE
        .db     $FC, $FF, $90, $94, $98, $9C, $98, $94
        .db     $90, $4E
        .db     $C7, $F3

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------


;-------------------------------------------------------------------------------
; Handles the helicopter:
;	Creation when we are close to the top of the building - also sets a timeout
;	Drawing & blade animation
;	Movement
;	Timeout - took too long to grab the helicopter skid
;-------------------------------------------------------------------------------
; $2C1A
ISR_JUMP3_HELICOPTER:
        LD      A,(COPTER_STATE)        ; 2C1A 3AA582   :..
        CP      $02                     ; 2C1D FE02     .G	Is COPTER_STATE >= 2?
        JP      NC,Lb540                ; 2C1F D2B82C   ..=	Yes, go here (move and animate the helicopter)

        CP      $00                     ; 2C22 FE00     .D	Is COPTER_STATE != 0?
        JR      NZ,Lb541                ; 2C24 2017      W	Yes, go here

        LD      HL,$300                 ; 2C26 210003   !D.	Set timer for how long the helicopter stays
        LD      (HELO_BALLOON_TIMER),HL ; 2C29 22B582   ".}
        LD      A,$01                   ; 2C2C 3E01     >.
        LD      (COPTER_STATE),A        ; 2C2E 32A582   2..	COPTER_STATE = 1 (initialized)

        LD      BC,$200                 ; 2C31 010002   .D.	Play helicopter sound
        CALL    LOAD_SOUND_DATA         ; 2C34 CDBB11   ..A

        LD      A,$F0                   ; 2C37 3EF0     >.
        LD      ($98DE),A               ; 2C39 32DE98   2..
        RET                             ; 2C3C C9       .

Lb541:  LD      A,(FLOOR_GROUP_IDX)     ; 2C3D 3ADC80   :.. Get the current building floor group
        AND     $03                     ; 2C40 E603     .S
        CP      $00                     ; 2C42 FE00     .D	is FLOOR_GROUP_IDX = 0?
        JP      Z,Lb542                 ; 2C44 CAD92C   ..|	Yes, go here

        CP      $02                     ; 2C47 FE02     .G	is FLOOR_GROUP_IDX != 2?
        JR      NZ,Lb543                ; 2C49 3008     0L	Yes, go here

        LD      A,(FLOOR_IDX)           ; 2C4B 3ADD80   :". Get the current floor index
        CP      $0A                     ; 2C4E FE0A     ..	is FLOOR_IDX < $0A?
        JP      C,Lb542                 ; 2C50 DAD92C   ..|	yes, go here

Lb543:  LD      IY,BIG_SPRITE_CTRL      ; 2C53 FD21DC98 .!..  Point to big sprite control
        LD      (IY+$02),$F0            ; 2C57 FD3602F0 .6..  Big sprite Y position
        LD      (IY+$03),$50            ; 2C5B FD360350 .6SE  Big sprite X position
        LD      (IY+$00),$01            ; 2C5F FD360001 .6D.  Big sprite priority
        LD      A,(RANDOM_NUMBER)       ; 2C63 3A2281   :g.   Get a random number
        AND     $01                     ; 2C66 E601     ..	  Direction of helicopter?
        JR      NZ,Lb544                ; 2C68 2006      G

        LD      (IY+$01),$00            ; 2C6A FD360100 .6.D  Color index 0, no inversion
        JR      DRAW_HELICOPTER_BODY    ; 2C6E 1804     ..

Lb544:  LD      (IY+$01),$10            ; 2C70 FD360110 .6..  Color index 0, Invert X axis (turn helicopter around)

;-----------------------------
; Draw body of the helicopter
;-----------------------------
DRAW_HELICOPTER_BODY:
; Bottom half
        LD      HL,HELO_BODY_2X2_DATA   ; 2C74 21282E   !l;   Source - Helicopter Body
        LD      IX,$88E6                ; 2C77 DD21E688 .!..  Destination - Big sprite screen RAM
        CALL    COPY_BIGSPRITE_2X2      ; 2C7B CD4F35   .Jq   Copy 2x2 big sprite

        INC     HL                      ; 2C7E 23       #     Go to next body 2x2 data byte
        LD      IX,$88E8                ; 2C7F DD21E888 .!..  Destination - Big sprite screen RAM
        CALL    COPY_BIGSPRITE_2X2      ; 2C83 CD4F35   .Jq   Copy 2x2 big sprite

        INC     HL                      ; 2C86 23       #     Go to next body 2x2 data byte
        LD      IX,$88EA                ; 2C87 DD21EA88 .!..  Destination - Big sprite screen RAM
        CALL    COPY_BIGSPRITE_2X2      ; 2C8B CD4F35   .Jq   Copy 2x2 big sprite

; Top half
        INC     HL                      ; 2C8E 23       #     Go to next body 2x2 data byte
        LD      IX,$88C6                ; 2C8F DD21C688 .!..  Destination - Big sprite screen RAM
        CALL    COPY_BIGSPRITE_2X2      ; 2C93 CD4F35   .Jq   Copy 2x2 big sprite

        INC     HL                      ; 2C96 23       #     Go to next body 2x2 data byte
        LD      IX,$88C8                ; 2C97 DD21C888 .!..  Destination - Big sprite screen RAM
        CALL    COPY_BIGSPRITE_2X2      ; 2C9B CD4F35   .Jq   Copy 2x2 big sprite

        INC     HL                      ; 2C9E 23       #     Go to next body 2x2 data byte
        LD      IX,$88CA                ; 2C9F DD21CA88 .!..  Destination - Big sprite screen RAM
        CALL    COPY_BIGSPRITE_2X2      ; 2CA3 CD4F35   .Jq   Copy 2x2 big sprite

        LD      A,$02                   ; 2CA6 3E02     >.
        CALL    DELAY                   ; 2CA8 CDB802   ..G   Delay

        LD      A,$02                   ; 2CAB 3E02     >G
        LD      (COPTER_STATE),A        ; 2CAD 32A582   2.}	  COPTER_STATE = 2 (ready to move the helicopter)
        LD      (COPTER_BLADE1_TIMING),A ; 2CB0 32A882   2W.  Helicopter top blade movement timing counter (2)
        LD      (COPTER_BLADE2_TIMING),A ; 2CB3 32A982   2.}  Helicopter tail blade movement timing counter (2)
        JR      Lb542                   ; 2CB6 1821     .0

Lb540:  CALL    COPTER_BLADE_ANIMATION  ; 2CB8 CD9E2D   ..8
        CALL    MOVE_HELICOPTER         ; 2CBB CDF82C   ..=
        LD      A,($82AB)               ; 2CBE 3AAB82   :T.
        CP      $02                     ; 2CC1 FE02     .G
        JR      Z,Lb549                 ; 2CC3 282C     (|

        LD      A,$01                   ; 2CC5 3E01     >.
        CALL    Lb255                   ; 2CC7 CD2103   .4S
        CALL    Lb550                   ; 2CCA CD302E   . ;
        LD      A,($82AB)               ; 2CCD 3AAB82   :.}
        CP      $01                     ; 2CD0 FE01     ..
        JR      Z,Lb549                 ; 2CD2 281D     (Y

        LD      A,$01                   ; 2CD4 3E01     >.
        CALL    Lb223                   ; 2CD6 CD6503   .p.

; Update and check the helicopter fly timer
Lb542:  LD      HL,(HELO_BALLOON_TIMER) ; 2CD9 2AB582   *.}	Decrement counter for how long the helicopter stays
        DEC     HL                      ; 2CDC 2B       +
        LD      (HELO_BALLOON_TIMER),HL ; 2CDD 22B582   ".}
        LD      A,L                     ; 2CE0 7D       }
        OR      H                       ; 2CE1 B4       .
        RET     NZ                      ; 2CE2 C0       .	Not zero? return

; The helicopter timed out - end the building
        LD      A,$02                   ; 2CE3 3E02     >G	Counter is zero (timeout)
        LD      ($82AB),A               ; 2CE5 32AB82   2.}

        LD      BC,$407                 ; 2CE8 010704   ..T	Play Player died sound
        CALL    LOAD_SOUND_DATA         ; 2CEB CDBB11   ..A

        CALL    BONUS_RATE_3000         ; 2CEE CD2D11   .}A	Set the bonus rate to 3000 and display it

Lb549:  CALL    Lb552                   ; 2CF1 CD702E   .eo
        CALL    GOTO_NEXT_BLDG          ; 2CF4 CDB310   ...  Go to next building
        RET                             ; 2CF7 C9       .

;=============================================================================
; Moves the helicopter
;
; Handles moving the helicopter left, right, up and down.
;=============================================================================
MOVE_HELICOPTER:
        LD      IY,BIG_SPRITE_CTRL      ; 2CF8 FD21DC98 .!.. Point to big sprite control
        CP      C                       ; 2CFC B9
        RL      H                       ; 2CFD CB14     ..	???
        LD      (HL),D                  ; 2CFF 72       r	???
        LD      A,(IY+$03)              ; 2D00 FD7E03   .~. Read big sprite X position
        JR      NZ,Lb553                ; 2D03 2006      .	Is X pos. != 0? Yes, go here

        CP      $80                     ; 2D05 FE80     ..	Is X position != $80?
        JR      NZ,Lb554                ; 2D07 3008     0L	Yes, change helicopter direction

        JR      Lb555                   ; 2D09 180E     ..  Go here (do not change direction)

Lb553:  CP      $04                     ; 2D0B FE04     .T	Is X Pos < 4?
        JR      C,Lb554                 ; 2D0D 3802     8G	Yes, go here (change direction)
        JR      Lb555                   ; 2D0F 1808     .L	No, do not change direction

; Change helicopter direction (flip or no-flip X axis, bit 4 of color/attribute))
Lb554:  LD      A,(IY+$01)              ; 2D11 FD7E01   .~.  
        XOR     $10                     ; 2D14 EE10     ..	 
        LD      (IY+$01),A              ; 2D16 FD7701   .w.
		  
Lb555:  LD      A,(COPTER_STATE)        ; 2D19 3AA582   :.}
        BIT     0,A                     ; 2D1C CB47     .G	Is this an odd number?
        JR      NZ,Lb556                ; 2D1E 2049      M	Yes, go here

        LD      A,(FLOOR_IDX)           ; 2D20 3ADD80   :..  Get the current floor index
        CP      $02                     ; 2D23 FE02     .G	Is FLOOR_IDX < 2?
        JR      C,Lb557                 ; 2D25 3804     8T	Yes, go here

        CP      $04                     ; 2D27 FE04     .T	Is FLOOR_IDX < 4?
        JR      C,Lb558                 ; 2D29 3809     8.	Yes, go here

Lb557:  LD      A,(IY+$02)              ; 2D2B FD7E02   .~.  Read big sprite Y position
        CP      $B0                     ; 2D2E FEB0     ..	Is Y position != $B0?
        JR      NZ,Lb559                ; 2D30 3012     0F	Yes, go here (move helicopter down)
        JR      Lb560                   ; 2D32 1807     ..	Go here

Lb558:  LD      A,(IY+$02)              ; 2D34 FD7E02   .~G
        CP      $70                     ; 2D37 FE70     .e  Is Y position != $70?
        JR      NZ,Lb559                ; 2D39 3009     0.	Yes, go here (move helicopter down)

Lb560:  LD      A,(COPTER_STATE)        ; 2D3B 3AA582   :.}	Set bit 0 of COPTER_STATE to 1
        SET     0,A                     ; 2D3E CBC7     ..
        LD      (COPTER_STATE),A        ; 2D40 32A582   2..
        RET                             ; 2D43 C9       .	Done with MOVE_HELICOPTER

; Move helicopter down
Lb559:  LD      A,(IY+$02)              ; 2D44 FD7E02   .~G  Decrement the big sprite Y position by 2
        SUB     $02                     ; 2D47 D602     .G
        LD      (IY+$02),A              ; 2D49 FD7702   .w.

        LD      A,(ISR_COUNTER)         ; 2D4C 3A4580   :P.  Get the interrupt counter
        AND     $03                     ; 2D4F E603     ..
        JR      NZ,Lb561                ; 2D51 2015      P

        CP      B                       ; 2D53 B8
        RL      B                       ; 2D54 CB10     ..
        SCF                             ; 2D56 37       7
        LD      A,(IY+$03)              ; 2D57 FD7E03   .~S	Read big sprite X position
        JR      NZ,Lb562                ; 2D5A 2007      .	if X pos != 0, go here

        ADD     A,$01                   ; 2D5C C601     ..	Increment X position by 1
        LD      (IY+$03),A              ; 2D5E FD7703   .w.  
        JR      Lb561                   ; 2D61 1805     ..	Go here

Lb562:  SUB     $01                     ; 2D63 D601     ..	Decrement X position by 1
        LD      (IY+$03),A              ; 2D65 FD7703   .wS
Lb561:  RET                             ; 2D68 C9       .	Done with MOVE_HELICOPTER


Lb556:  LD      A,(IY+$02)              ; 2D69 FD7E02   .~. Read big sprite Y position
        CP      $C0                     ; 2D6C FEC0     ..	Is Y position < $C0?
        JR      C,Lb563                 ; 2D6E 3809     8.	Yes, go here

        LD      A,(COPTER_STATE)        ; 2D70 3AA582   :..	Set bit 0 of COPTER_STATE to 0
        RES     0,A                     ; 2D73 CB87     ..
        LD      (COPTER_STATE),A        ; 2D75 32A582   2.}
        RET                             ; 2D78 C9       .	Done with MOVE_HELICOPTER

Lb563:  LD      A,(ISR_COUNTER)         ; 2D79 3A4580   :U. Get the interrupt counter
        AND     $03                     ; 2D7C E603     .S
        JR      NZ,Lb564                ; 2D7E 2015      Q	Yes, go here (move helicopter up)

        CP      C                       ; 2D80 B9
        RL      H                       ; 2D81 CB14     ..
        LD      (HL),D                  ; 2D83 72       r
        LD      A,(IY+$03)              ; 2D84 FD7E03   .~.	Read big sprite X position
        JR      NZ,Lb565                ; 2D87 2007      F	Is X position != 0? Yes, go here (move helicopter left)

; Move helicopter right
        ADD     A,$01                   ; 2D89 C601     ..	Increment the X position by 1
        LD      (IY+$03),A              ; 2D8B FD7703   .wS
        JR      Lb564                   ; 2D8E 1805     .U	Go here (move helicopter up)

; Move helicopter left
Lb565:  SUB     $01                     ; 2D90 D601     ..	Decrement the X position by 1
        LD      (IY+$03),A              ; 2D92 FD7703   .w.

; Move helicopter up
Lb564:  LD      A,(IY+$02)              ; 2D95 FD7E02   .~.	Increment Y position by 2
        ADD     A,$02                   ; 2D98 C602     ..	
        LD      (IY+$02),A              ; 2D9A FD7702   .wG
        RET                             ; 2D9D C9       .	Done with MOVE_HELICOPTER 


;=============================================================================
; 
; Handles helicopter top and tail rotor blade animation
;
;=============================================================================
COPTER_BLADE_ANIMATION:
        LD      A,(COPTER_BLADE1_TIMING) ; 2D9E 3AA882   :W.  Get helicopter top blade timing counter
        SUB     $01                     ; 2DA1 D601     ..   Subtract 1
        CP      $00                     ; 2DA3 FE00     .D   At zero?
        JR      NZ,Lb566                ; 2DA5 2025      0   Nope, skip helicopter top blade movement

;--------------------------------------
; Handle helicopter top blade movement
; (Big sprites)
;--------------------------------------
        LD      A,(COPTER_BLADE1_INDEX) ; 2DA7 3AA682   :.}  Get index value for helicopter top rotor blades graphics
        RLCA                            ; 2DAA 07       .    
        LD      E,A                     ; 2DAB 5F       _
        RLCA                            ; 2DAC 07       .
        ADD     A,E                     ; 2DAD 83       .
        LD      E,A                     ; 2DAE 5F       _
        LD      D,$00                   ; 2DAF 1600     .D   DE = 6 * Index  (6 bytes in each graphic)
        LD      HL,HELO_TOP_BLADE_DATA  ; 2DB1 21FE2D   !.}  Base address for top blade data

        ADD     HL,DE                   ; 2DB4 19       .    Source = Base + DE (offset)
        LD      DE,$88C5                ; 2DB5 11C588   .:w  Destination in big sprite RAM
        LD      BC,$06                  ; 2DB8 010600   .GD  Copy 6 bytes
        CALL    BLOCK_COPY              ; 2DBB CD4A04   .K.  Block copy routine

; Update blade index
        LD      A,(COPTER_BLADE1_INDEX) ; 2DBE 3AA682   :..  Get helicopter top blade index
        INC     A                       ; 2DC1 3C       <    Increment index (for motion)
        CP      $06                     ; 2DC2 FE06     .G   Is value < 6?
        JR      C,Lb567                 ; 2DC4 3801     8.   Yes, continue
        XOR     A                       ; 2DC6 AF       .    Clear index

Lb567:  LD      (COPTER_BLADE1_INDEX),A ; 2DC7 32A682   2.}  Save helicopter top blade index
        LD      A,$01                   ; 2DCA 3E01     >.

;---------------------------------------
; Handle helicopter tail blade movement
; (Big sprites)
;---------------------------------------
Lb566:  LD      (COPTER_BLADE1_TIMING),A ; 2DCC 32A882   2W.  Save countdown value
        LD      A,(COPTER_BLADE2_TIMING) ; 2DCF 3AA982   :.}  Get helicopter tail blade timing counter
        SUB     $01                     ; 2DD2 D601     ..   Subtract 1
        CP      $00                     ; 2DD4 FE00     .D   At zero?
        JR      NZ,Lb568                ; 2DD6 2020      d   Nope, skip helicopter tail blade movement

        LD      A,(COPTER_BLADE2_INDEX) ; 2DD8 3AA782   :..  Get tail blade movement index
        LD      E,A                     ; 2DDB 5F       _
        LD      D,$00                   ; 2DDC 1600     .D
        LD      HL,HELO_TAIL_2X2_DATA   ; 2DDE 21222E   !&;  Base address for tail blade data
        ADD     HL,DE                   ; 2DE1 19       .    Source data is Base + tail index
        LD      IX,$88CC                ; 2DE2 DD21CC88 .!.w Destination in big sprite RAM
        CALL    COPY_BIGSPRITE_2X2      ; 2DE6 CD4F35   .Jp  Copy 2x2 big sprite

        LD      A,(COPTER_BLADE2_INDEX) ; 2DE9 3AA782   :X}  Get tail blade movement index
        INC     A                       ; 2DEC 3C       <    Increment value
        CP      $06                     ; 2DED FE06     ..   Is value < 6?
        JP      C,Lb569                 ; 2DEF DAF32D   ..}  Yes, continue
        XOR     A                       ; 2DF2 AF       .    Nope, zero index

Lb569:  LD      (COPTER_BLADE2_INDEX),A ; 2DF3 32A782   2X}  Save new tail blade movement index
        LD      A,$01                   ; 2DF6 3E01     >.   Set tial blade movement timing counter

Lb568:  LD      (COPTER_BLADE2_TIMING),A ; 2DF8 32A982   2.. Save new tial movement countdown timer
        RET                             ; 2DFB C9       .    End COPTER_BLADE_ANIMATION


;-------------------------------------------------------------------------------
; Data for helicopter rotor blades and body
;
; This is big sprite data
;
; Range: $2DFC - $2E2F
; Number of bytes: 52
;-------------------------------------------------------------------------------

        .db     $C7, $FB						; Start data block

; $2DFE - Top blade position 1
HELO_TOP_BLADE_DATA:
        .db     $00, $00, $08, $09, $28, $29

; $2E04 - Top blade position 2
		.db     $00, $00, $0A, $0B, $2A, $2B

; $2E0A - Top blade position 3
		.db     $0C, $0D, $2C, $2D, $00, $00

; $2E10 - Top blade position 4
		.db     $0E, $0F, $2E, $2F, $00, $00

; $2E16 - Top blade position 5
        .db     $0C, $0D, $2C, $2D, $00, $00

; $2E1C - Top blade position 6
		.db     $00, $00, $0A, $0B, $2A, $2B


; $2E22 - Tail blade 2x2 values (each value is the start of a quad series)
; (i.e. $48 is $48, $49, $4A, and $4B)
;
HELO_TAIL_2X2_DATA:
		.db     $48, $4C, $60, $64, $68, $6C


; $2E28 - Helicopter body 2x2 values
HELO_BODY_2X2_DATA:
        .db     $04, $24, $44, $00, $20, $40

        .db     $C7, $F3						; End data block

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------


;=============================================================================
;=============================================================================
Lb550:  LD      A,($98DE)               ; 2E30 3ADE98   :..
        LD      B,A                     ; 2E33 47       G
        CALL    CHECK_FIELD_INVERSION   ; 2E34 CD8311   .|A Check to see if the field is inverted
        AND     A                       ; 2E37 A7       .
        JR      NZ,Lb572                ; 2E38 2007      .  Normal field, go here

; Inverted field
        LD      A,($98DF)               ; 2E3A 3ADF98   :..
        ADD     A,$40                   ; 2E3D C640     .Q
        JR      Lb573                   ; 2E3F 1807     .F

; Normal field
Lb572:  LD      A,($98DF)               ; 2E41 3ADF98   :..
        NEG                             ; 2E44 ED44     .D
        SUB     $31                     ; 2E46 D631     .a

Lb573:  LD      C,A                     ; 2E48 4F       O
        CALL    Lb526                   ; 2E49 CDC032   ..f
        AND     A                       ; 2E4C A7       .
        JR      NZ,Lb574                ; 2E4D 2013      R
        LD      A,C                     ; 2E4F 79       y
        SUB     $08                     ; 2E50 D608     .L
        LD      C,A                     ; 2E52 4F       O
        CALL    Lb526                   ; 2E53 CDC032   ..f
        AND     A                       ; 2E56 A7       .
        JR      NZ,Lb574                ; 2E57 2009      .
        LD      A,C                     ; 2E59 79       y
        SUB     $08                     ; 2E5A D608     .L
        LD      C,A                     ; 2E5C 4F       O
        CALL    Lb526                   ; 2E5D CDC032   ..f
        AND     A                       ; 2E60 A7       .
        RET     Z                       ; 2E61 C8       .

Lb574:  CALL    SHOW_CLIMBER            ; 2E62 CD4415   ..P  Show climber on screen
        LD      A,$01                   ; 2E65 3E01     >.
        LD      ($82AB),A               ; 2E67 32AB82   2.}
        LD      B,$00                   ; 2E6A 0600     .D
        CALL    PLAY_END_BLDG_SOUND     ; 2E6C CD811C   ...  Play the end of building sound
        RET                             ; 2E6F C9       .

;=============================================================================
;=============================================================================
Lb552:  LD      IX,BIG_SPRITE_CTRL      ; 2E70 DD21DC98 .!..  Point to big sprite control
        LD      (IX+$00),$00            ; 2E74 DD360000 .6DD  Set sprite number (priority?)

Lb583:  LD      IX,BIG_SPRITE_CTRL      ; 2E78 DD21DC98 .!..  Point to big sprite control
        LD      A,(COPTER_STATE)        ; 2E7C 3AA582   :..
        CP      $00                     ; 2E7F FE00     .D	  Is COPTER_STATE = 0?
        JR      Z,Lb575                 ; 2E81 2814     (.	  Yes, go here

        LD      A,(IX+$02)              ; 2E83 DD7E02   .~.   Read big sprite Y pos.
        ADD     A,$01                   ; 2E86 C601     ..
        LD      (IX+$02),A              ; 2E88 DD7702   .wG   Write big sprite Y pos.
        CP      $EC                     ; 2E8B FEEC     ..
        JR      C,Lb575                 ; 2E8D 3808     8L
        XOR     A                       ; 2E8F AF       .
        LD      (COPTER_STATE),A        ; 2E90 32A582   2..	  COPTER_STATE = 0
        LD      (IX+$02),$F0            ; 2E93 DD3602F0 .6..  Write big sprite Y pos.

Lb575:  LD      A,($82AB)               ; 2E97 3AAB82   :.}
        CP      $01                     ; 2E9A FE01     ..
        JR      Z,Lb576                 ; 2E9C 280B     ([

        CALL    Lb577                   ; 2E9E CD0911   ..A
        LD      A,(COPTER_STATE)        ; 2EA1 3AA582   :.}
        AND     A                       ; 2EA4 A7       .	  Is COPTER_STATE != 0?
        JR      NZ,Lb578                ; 2EA5 2027      f	  Yes, go here
        JR      Lb579                   ; 2EA7 1836     .s

Lb576:  LD      HL,$9892                ; 2EA9 219298   !..  Left climber arm, Y position
        LD      B,$04                   ; 2EAC 0604     ..
        LD      A,(HL)                  ; 2EAE 7E       ~
        CP      $EC                     ; 2EAF FEEC     ..
        JR      C,Lb580                 ; 2EB1 380D     8.

; Erases the climber
        LD      HL,$9890                ; 2EB3 219098   !..  Point to sprite control 5 (climber is 5 - 8)
        LD      B,$10                   ; 2EB6 0610     ..   Copy 16 bytes (for the 4 sprites
Lb581:  LD      (HL),$00                ; 2EB8 3600     6D   Clear value
        INC     HL                      ; 2EBA 23       #    Go to next sprite control value
        DEC     B                       ; 2EBB 05       .    Decrement counter
        JR      NZ,Lb581                ; 2EBC 20FA      .   Done? Nope, keep looping

        JR      Lb579                   ; 2EBE 181F     ._

Lb580:  LD      A,(HL)                  ; 2EC0 7E       ~
        ADD     A,$01                   ; 2EC1 C601     ..
        LD      (HL),A                  ; 2EC3 77       w
        INC     HL                      ; 2EC4 23       #
        INC     HL                      ; 2EC5 23       #
        INC     HL                      ; 2EC6 23       #
        INC     HL                      ; 2EC7 23       #
        DEC     B                       ; 2EC8 05       .
        JR      NZ,Lb580                ; 2EC9 20F5      .
        CALL    Lb577                   ; 2ECB CD0911   ..A

Lb578:  LD      B,$04                   ; 2ECE 0604     ..

Lb582:  PUSH    BC                      ; 2ED0 C5       .

        LD      A,$02                   ; 2ED1 3E02     >G
        CALL    DELAY                   ; 2ED3 CDB802   ... Delay

        CALL    COPTER_BLADE_ANIMATION  ; 2ED6 CD9E2D   ..8
        POP     BC                      ; 2ED9 C1       .
        DEC     B                       ; 2EDA 05       .
        JR      NZ,Lb582                ; 2EDB 20F3      .
        JR      Lb583                   ; 2EDD 1899     ..

Lb579:  LD      A,$0A                   ; 2EDF 3E0A     >O
        CALL    DELAY                   ; 2EE1 CDB802   ... Delay

        CALL    Lb577                   ; 2EE4 CD0911   ..A
        AND     A                       ; 2EE7 A7       .
        JR      NZ,Lb579                ; 2EE8 20F5      .
        RET                             ; 2EEA C9       .

;-------------------------------------------------------------------------------
;-------------------------------------------------------------------------------
ISR_JUMP3_KING_KONG:
        LD      A,($817F)               ; 2EEB 3A7F81   :*.
        AND     A                       ; 2EEE A7       .
        JR      NZ,Lb584                ; 2EEF 200C      \
        LD      A,(FLOOR_GROUP_IDX)     ; 2EF1 3ADC80   :.. Get the current building floor group
        AND     $03                     ; 2EF4 E603     .S
        CP      $01                     ; 2EF6 FE01     ..
        RET     NZ                      ; 2EF8 C0       .

        CALL    Lb585                   ; 2EF9 CD012F   ..*
        RET                             ; 2EFC C9       .

Lb584:  CALL    Lb586                   ; 2EFD CD2C30   .| 
        RET                             ; 2F00 C9       .

;=============================================================================
;=============================================================================
Lb585:  NOP                             ; 2F01 00       .
        LD      A,(FLOOR_IDX)           ; 2F02 3ADD80   :.. Get the current floor index
        CP      $03                     ; 2F05 FE03     ..	Is it < 3?
        JP      C,Lb587                 ; 2F07 DA212F   .4*	Yes, go here

        CP      $09                     ; 2F0A FE09     ..	Is it = 9?
        JR      NZ,Lb588                ; 2F0C 3048     0.	Yes, go here

        SUB     $03                     ; 2F0E D603     .S	Subtract 3 from the floor index
        LD      B,A                     ; 2F10 47       G	B = Floor IDX - 3
        LD      A,$01                   ; 2F11 3E01     >.
        LD      (KEEP_SAME_ISR_FLAG),A  ; 2F13 324480   2@.  Keep processing the same ISR table location

        CALL    Lb589                   ; 2F16 CD602F   .4n

        CALL    Lb590                   ; 2F19 CDD42F   ..*

        XOR     A                       ; 2F1C AF       .
        LD      (KEEP_SAME_ISR_FLAG),A  ; 2F1D 324480   2@.  Process the next ISR table location
        RET                             ; 2F20 C9       .

Lb587:  NOP                             ; 2F21 00       .
        LD      A,(GP_82AF)             ; 2F22 3AAF82   :..  Get counter value
        AND     A                       ; 2F25 A7       .    Is value zero?
        RET     NZ                      ; 2F26 C0       .    Nope, return

        LD      A,(RANDOM_NUMBER)       ; 2F27 3A2281   :g.  Get a random number
        RLCA                            ; 2F2A 07       .
        AND     $01                     ; 2F2B E601     ..
        LD      ($8158),A               ; 2F2D 325881   2M.
        XOR     A                       ; 2F30 AF       .
        LD      ($8180),A               ; 2F31 328081   2..
        LD      ($815A),A               ; 2F34 325A81   2..
        LD      ($8159),A               ; 2F37 325981   2..

        LD      HL,UNKNOWN_815C         ; 2F3A 215C81   !..	Clear 32 bytes at UNKNOWN_815C
        LD      DE,UNKNOWN_8283         ; 2F3D 118382   ..} and UNKNOWN_8283
        LD      B,$20                   ; 2F40 0620     .d	32 bytes
Lb591:  XOR     A                       ; 2F42 AF       .	Clear A
        LD      (HL),A                  ; 2F43 77       w	
        LD      (DE),A                  ; 2F44 12       .
        INC     HL                      ; 2F45 23       #	Go to next byte
        INC     DE                      ; 2F46 13       .	Go to next byte
        DEC     B                       ; 2F47 05       .	Decrement counter
        JR      NZ,Lb591                ; 2F48 20F8      .	Not done, keep looping

        LD      BC,$401                 ; 2F4A 010104   ..T	Play King Kong Music
        CALL    LOAD_SOUND_DATA         ; 2F4D CDBB11   ..A

        LD      A,$01                   ; 2F50 3E01     >.
        LD      (GP_82AF),A             ; 2F52 32AF82   2..  Set counter to 1
        RET                             ; 2F55 C9       .

Lb588:  LD      A,$01                   ; 2F56 3E01     >.
        LD      ($817F),A               ; 2F58 327F81   2+.
        XOR     A                       ; 2F5B AF       .
        LD      (GP_82AF),A             ; 2F5C 32AF82   2..  Clear counter
        RET                             ; 2F5F C9       .

;=============================================================================
; B = FLOOR_IDX value - 3.
;=============================================================================
Lb589:  NOP                             ; 2F60 00       .
        LD      A,($8180)               ; 2F61 3A8081   :..
        CP      B                       ; 2F64 B8       .	Is (FLOOR_IDX - 3) != ($8180)?
        RET     NZ                      ; 2F65 C0       .	Yes, return

        LD      A,B                     ; 2F66 78       x	A = FLOOR_IDX-3
        RLCA                            ; 2F67 07       .	A = A * 2
        AND     $FE                     ; 2F68 E6FE     ..	Clear bit 0
        LD      C,A                     ; 2F6A 4F       O	C = A
        LD      B,$00                   ; 2F6B 0600     .D	B = 0
        LD      A,(FLOOR_NUM)           ; 2F6D 3A3181   :a. A = Working floor number
        AND     $F8                     ; 2F70 E6F8     ..	Clear bits 2-0
        LD      E,A                     ; 2F72 5F       _	E = A
        LD      D,$00                   ; 2F73 1600     .D	D = 0
        CP      $F8                     ; 2F75 FEF8     ..	Is A != $F8?
        JR      NZ,Lb592                ; 2F77 2003      .	Yes, go here

        LD      DE,$FFF8                ; 2F79 11F8FF   ...	DE = $FFF8 (-8)

Lb592:  LD      A,($8158)               ; 2F7C 3A5881   :..
        AND     A                       ; 2F7F A7       .	Is $8158 != 0?
        JR      NZ,Lb593                ; 2F80 2006      G	Yes, go here

		; Point to screen RAM
        LD      IX,$902B                ; 2F82 DD212B90 .!:. IX = $902B
        JR      Lb594                   ; 2F86 1804     ..	 Go here
Lb593:  LD      IX,$9036                ; 2F88 DD213690 .!s. IX = $9036


Lb594:  NOP                             ; 2F8C 00       .
        ADD     IX,DE                   ; 2F8D DD19     ..	IX = 4 * DE
        ADD     IX,DE                   ; 2F8F DD19     ..
        ADD     IX,DE                   ; 2F91 DD19     ..
        ADD     IX,DE                   ; 2F93 DD19     ..
        LD      IY,$31EC                ; 2F95 FD21EC31 .!.a IY = Data Table
        ADD     IY,BC                   ; 2F99 FD09     ..	 IY = IY + BC
        LD      L,(IY+$00)              ; 2F9B FD6E00   .nD  HL = (IY)
        LD      H,(IY+$01)              ; 2F9E FD6601   .f.
        PUSH    IX                      ; 2FA1 DDE5     ..
        POP     IY                      ; 2FA3 FDE1     ..	IY = IX
        LD      DE,$C00                 ; 2FA5 11000C   .D.	DE = $0C00 (3072)
        ADD     IY,DE                   ; 2FA8 FD19     ..	IY = IY + $0C00

Lb596:  NOP                             ; 2FAA 00       .
        LD      A,(HL)                  ; 2FAB 7E       ~	Load A from the table pointer
        CP      $FF                     ; 2FAC FEFF     ..	Is A = $FF?
        JR      Z,Lb595                 ; 2FAE 280E     (O	Yes, go here
        LD      (IX+$00),A              ; 2FB0 DD7700   .wD	 Draw to the screen
        LD      (IY+$00),$17            ; 2FB3 FD360017 .6D. 
        INC     IY                      ; 2FB7 FD23     .#
        INC     HL                      ; 2FB9 23       #
        INC     IX                      ; 2FBA DD23     .#
        JR      Lb596                   ; 2FBC 18EC     ..

Lb595:  LD      A,($8180)               ; 2FBE 3A8081   :..
        ADD     A,$01                   ; 2FC1 C601     ..
        LD      ($8180),A               ; 2FC3 328081   2..
        CP      $06                     ; 2FC6 FE06     .G
        JR      NZ,Lb597                ; 2FC8 2009      .

        LD      A,$01                   ; 2FCA 3E01     >.
        LD      ($817F),A               ; 2FCC 327F81   2+.
        XOR     A                       ; 2FCF AF       .
        LD      (GP_82AF),A             ; 2FD0 32AF82   2..  Clear counter

Lb597:  RET                             ; 2FD3 C9       .


;=============================================================================
;=============================================================================
Lb590:  NOP                             ; 2FD4 00       .
        LD      A,($8180)               ; 2FD5 3A8081   :..
        CP      $04                     ; 2FD8 FE04     ..
        JR      Z,Lb598                 ; 2FDA 2832     (f
        CP      $02                     ; 2FDC FE02     ..
        JR      Z,Lb599                 ; 2FDE 2806     (G	Yes, check King Kong
        CP      $05                     ; 2FE0 FE05     .U
        CALL    NC,Lb586                ; 2FE2 D42C30   .=1
        RET                             ; 2FE5 C9       .

Lb599:  LD      A,(UNKNOWN_815C)        ; 2FE6 3A5C81   :..	
        CP      $01                     ; 2FE9 FE01     ..
        RET     Z                       ; 2FEB C8       .	 Do not draw King Kong

; This section of code will draw King Kong's arms and eyes
        LD      A,($8158)               ; 2FEC 3A5881   :..	Random 1 or 0
        AND     A                       ; 2FEF A7       .
        LD      HL,$3276                ; 2FF0 217632   !6'  Source address for copy
        JR      NZ,Lb600                ; 2FF3 2003      .
        LD      HL,$3296                ; 2FF5 219632   !.f  Source address for copy
Lb600:  NOP                             ; 2FF8 00       .
        LD      DE,UNKNOWN_815C         ; 2FF9 115C81   ...  Destination address
        LD      BC,$10                  ; 2FFC 011000   ..D  Copy 16 bytes of data
        CALL    BLOCK_COPY              ; 2FFF CD4A04   .K.  Block copy routine

        LD      BC,$08                  ; 3002 010800   .LD  Copy 8 bytes of data
        ADD     HL,BC                   ; 3005 09       .    Change source address
        LD      DE,$8174                ; 3006 117481   .$.  Destination address UNKNOWN_815C[3][0]
        CALL    BLOCK_COPY              ; 3009 CD4A04   .K.  Block copy routine

        JR      Lb601                   ; 300C 181C     .H
Lb598:  NOP                             ; 300E 00       .
        LD      A,($816C)               ; 300F 3A6C81   :h.	UNKNOWN_815C[2][0]
        CP      $01                     ; 3012 FE01     ..
        RET     Z                       ; 3014 C8       .

        LD      A,($8158)               ; 3015 3A5881   :M.
        AND     A                       ; 3018 A7       .
        LD      HL,$3286                ; 3019 218632   !.f  Source address
        JR      NZ,Lb602                ; 301C 2003      S
        LD      HL,$32A6                ; 301E 21A632   !.'  Source address
Lb602:  LD      DE,$816C                ; 3021 116C81   .h.  Destination address UNKNOWN_815C[2][0]
        LD      BC,$08                  ; 3024 010800   .LD  Copy 8 bytes of data
        CALL    BLOCK_COPY              ; 3027 CD4A04   .K.  Block copy routine

Lb601:  NOP                             ; 302A 00       .
        RET                             ; 302B C9       .

Lb586:  NOP                             ; 302C 00       .
        LD      A,($816C)               ; 302D 3A6C81   :h.
        AND     A                       ; 3030 A7       .
        JR      NZ,Lb603                ; 3031 200D      .
        XOR     A                       ; 3033 AF       .
        LD      ($817F),A               ; 3034 327F81   2+.
        LD      (GP_82AF),A             ; 3037 32AF82   2P}  Clear counter
        LD      A,$FF                   ; 303A 3EFF     >.
        LD      ($82B8),A               ; 303C 32B882   2..
        RET                             ; 303F C9       .

Lb603:  NOP                             ; 3040 00       .
        LD      A,($8159)               ; 3041 3A5981   :..
        AND     A                       ; 3044 A7       .
        JR      Z,Lb604                 ; 3045 2805     (.
        DEC     A                       ; 3047 3D       =
        LD      ($8159),A               ; 3048 325981   2\.
        RET                             ; 304B C9       .

Lb604:  NOP                             ; 304C 00       .
        LD      A,(BUILDING_NUMBER)     ; 304D 3ADF80   :..
        LD      E,A                     ; 3050 5F       _
        LD      D,$00                   ; 3051 1600     .D
        LD      HL,$32B6                ; 3053 21B632   !.f
        ADD     HL,DE                   ; 3056 19       .
        LD      A,(HL)                  ; 3057 7E       ~
        LD      ($8159),A               ; 3058 325981   2\.
        LD      A,($815A)               ; 305B 3A5A81   :..
        RLCA                            ; 305E 07       .
        LD      E,A                     ; 305F 5F       _
        LD      D,$00                   ; 3060 1600     .D
        LD      A,($8158)               ; 3062 3A5881   :..
        AND     A                       ; 3065 A7       .
        LD      IX,$3216                ; 3066 DD211632 .!Sf
        JR      NZ,Lb605                ; 306A 2004      .
        LD      IX,$3246                ; 306C DD214632 .!.f
Lb605:  NOP                             ; 3070 00       .
        ADD     IX,DE                   ; 3071 DD19     ..
        LD      L,(IX+$00)              ; 3073 DD6E00   .nD
        LD      H,(IX+$01)              ; 3076 DD6601   .f.
        LD      A,(HL)                  ; 3079 7E       ~
        LD      ($815D),A               ; 307A 325D81   2..
        INC     HL                      ; 307D 23       #
        LD      A,(HL)                  ; 307E 7E       ~
        LD      ($8165),A               ; 307F 326581   2u.
        INC     HL                      ; 3082 23       #
        LD      A,(HL)                  ; 3083 7E       ~
        LD      ($816D),A               ; 3084 326D81   2x.
        INC     HL                      ; 3087 23       #
        LD      A,(HL)                  ; 3088 7E       ~
        LD      ($8175),A               ; 3089 327581   25.
        LD      A,($815A)               ; 308C 3A5A81   :..
        ADD     A,$01                   ; 308F C601     ..
        AND     $07                     ; 3091 E607     .F
        LD      ($815A),A               ; 3093 325A81   2..
        CP      $03                     ; 3096 FE03     .S
        JR      NZ,Lb606                ; 3098 2040      .

        LD      BC,$305                 ; 309A 010503   .U.	Play king kong chirp sound
        CALL    LOAD_SOUND_DATA         ; 309D CDBB11   ..A

        LD      A,($8158)               ; 30A0 3A5881   :..
        AND     A                       ; 30A3 A7       .
        JR      NZ,Lb607                ; 30A4 2018      .
        LD      A,($815F)               ; 30A6 3A5F81   :..
        ADD     A,$0A                   ; 30A9 C60A     .O
        LD      B,A                     ; 30AB 47       G
        LD      A,($8160)               ; 30AC 3A6081   :4.
        ADD     A,$0E                   ; 30AF C60E     ..
        LD      C,A                     ; 30B1 4F       O
        CALL    Lb526                   ; 30B2 CDC032   ..'
        LD      A,C                     ; 30B5 79       y
        SUB     $04                     ; 30B6 D604     ..
        LD      C,A                     ; 30B8 4F       O
        CALL    Lb526                   ; 30B9 CDC032   ..f
        JR      Lb608                   ; 30BC 1816     ..
Lb607:  LD      A,($815F)               ; 30BE 3A5F81   :..
        ADD     A,$0A                   ; 30C1 C60A     .O
        LD      B,A                     ; 30C3 47       G
        LD      A,($8160)               ; 30C4 3A6081   :4.
        ADD     A,$02                   ; 30C7 C602     .G
        LD      C,A                     ; 30C9 4F       O
        CALL    Lb526                   ; 30CA CDC032   ..'
        LD      A,C                     ; 30CD 79       y
        ADD     A,$04                   ; 30CE C604     ..
        LD      C,A                     ; 30D0 4F       O
        CALL    Lb526                   ; 30D1 CDC032   ..f

Lb608:  LD      A,$30                   ; 30D4 3E30     > 
        CALL    DELAY                   ; 30D6 CDB802   ..G Delay

        RET                             ; 30D9 C9       .

Lb606:  LD      A,($815F)               ; 30DA 3A5F81   :..
        LD      B,A                     ; 30DD 47       G
        LD      A,$C0                   ; 30DE 3EC0     >.
        CP      B                       ; 30E0 B8       .
        RET     C                       ; 30E1 D8       .

        LD      A,(BUILDING_NUMBER)     ; 30E2 3ADF80   :..
        AND     $02                     ; 30E5 E602     .G
        LD      A,$4F                   ; 30E7 3E4F     >J
        JR      Z,Lb609                 ; 30E9 2802     (G
        LD      A,$3F                   ; 30EB 3E3F     >.
Lb609:  CP      B                       ; 30ED B8       .
        RET     NC                      ; 30EE D0       .

        LD      A,($815A)               ; 30EF 3A5A81   :..
        CP      $05                     ; 30F2 FE05     .U
        RET     NZ                      ; 30F4 C0       .

        LD      A,(FLOOR_NUM)           ; 30F5 3A3181   :a. Get the working floor number
        AND     $0F                     ; 30F8 E60F     ..
        RET     NZ                      ; 30FA C0       .

        CALL    Lb610                   ; 30FB CDFF30   .. 
        RET                             ; 30FE C9       .

;=============================================================================
;=============================================================================

Lb610:  LD      A,$01                   ; 30FF 3E01     >.
        LD      (KEEP_SAME_ISR_FLAG),A  ; 3101 324480   2@.  Keep processing the same ISR table location
        LD      IX,UNKNOWN_815C         ; 3104 DD215C81 .!..
        LD      BC,$08                  ; 3108 010800   .LD
        LD      D,$18                   ; 310B 1618     ..
        LD      A,($8158)               ; 310D 3A5881   :M.
        XOR     $01                     ; 3110 EE01     ..
        LD      ($8158),A               ; 3112 325881   2..

Lb613:  NOP                             ; 3115 00       .
        LD      A,(IX+$01)              ; 3116 DD7E01   .~.
        XOR     $40                     ; 3119 EE40     .Q
        LD      (IX+$01),A              ; 311B DD7701   .w.
        LD      A,($8158)               ; 311E 3A5881   :..
        CP      $01                     ; 3121 FE01     ..
        LD      A,(IX+$04)              ; 3123 DD7E04   .~.
        JR      NZ,Lb611                ; 3126 2003      S

        ADD     A,D                     ; 3128 82       .
        JR      Lb612                   ; 3129 1801     ..

Lb611:  SUB     D                       ; 312B 92       .

Lb612:  NOP                             ; 312C 00       .
        LD      (IX+$04),A              ; 312D DD7704   .w.
        ADD     IX,BC                   ; 3130 DD09     ..
        LD      A,$20                   ; 3132 3E20     >d
        ADD     A,D                     ; 3134 82       .
        LD      D,A                     ; 3135 57       W
        CP      $98                     ; 3136 FE98     ..
        JR      NZ,Lb613                ; 3138 20DB      .

        LD      A,($815F)               ; 313A 3A5F81   :..
        LD      B,A                     ; 313D 47       G
        LD      A,($3279)               ; 313E 3A7932   :|'
        ADD     A,$10                   ; 3141 C610     ..
        SUB     B                       ; 3143 90       .
        AND     $F8                     ; 3144 E6F8     ..
        LD      B,A                     ; 3146 47       G
        LD      A,(FLOOR_NUM)           ; 3147 3A3181   :a. Get the working floor number
        AND     $F8                     ; 314A E6F8     ..
        ADD     A,B                     ; 314C 80       .
        LD      E,A                     ; 314D 5F       _
        LD      D,$00                   ; 314E 1600     .D
        LD      A,($8158)               ; 3150 3A5881   :..
        AND     A                       ; 3153 A7       .
        JR      NZ,Lb614                ; 3154 200A      .

        LD      IX,$940B                ; 3156 DD210B94 .!.k
        LD      IY,$9416                ; 315A FD211694 .!Sk
        JR      Lb615                   ; 315E 1808     .L

Lb614:  LD      IX,$9416                ; 3160 DD211694 .!Sk
        LD      IY,$940B                ; 3164 FD210B94 .!.k

Lb615:  NOP                             ; 3168 00       .
        ADD     IX,DE                   ; 3169 DD19     ..  IX = IX + (4 * DE)
        ADD     IX,DE                   ; 316B DD19     ..
        ADD     IX,DE                   ; 316D DD19     ..
        ADD     IX,DE                   ; 316F DD19     ..

        ADD     IY,DE                   ; 3171 FD19     ..  IY = IY + (4 * DE)
        ADD     IY,DE                   ; 3173 FD19     ..
        ADD     IY,DE                   ; 3175 FD19     ..
        ADD     IY,DE                   ; 3177 FD19     ..

        PUSH    IX                      ; 3179 DDE5     ..
        PUSH    IX                      ; 317B DDE5     ..

        PUSH    IY                      ; 317D FDE5     ..
        POP     IX                      ; 317F DDE1     ..  IX = IY
        LD      BC,$800                 ; 3181 010008   .DL
        ADD     IX,BC                   ; 3184 DD09     ..
        LD      HL,$2BDE                ; 3186 21DE2B   !.: Point to table
        LD      A,(BUILDING_NUMBER)     ; 3189 3ADF80   :..
        LD      E,A                     ; 318C 5F       _
        LD      D,$00                   ; 318D 1600     .D
        ADD     HL,DE                   ; 318F 19       .   HL = $2BDE + BuildingNumber
        LD      B,(HL)                  ; 3190 46       F
        LD      C,$52                   ; 3191 0E52     ..
        LD      L,$06                   ; 3193 2E06     ..
        LD      DE,$FFE0                ; 3195 11E0FF   ...

Lb616:  LD      (IY+$00),C              ; 3198 FD7100   .qD
        LD      (IY+$01),C              ; 319B FD7101   .q.
        LD      (IY+$02),C              ; 319E FD7102   .qG
        LD      (IY+$03),C              ; 31A1 FD7103   .qS
        ADD     IY,DE                   ; 31A4 FD19     ..
        LD      (IX+$00),B              ; 31A6 DD7000   .pD
        LD      (IX+$01),B              ; 31A9 DD7001   .p.
        LD      (IX+$02),B              ; 31AC DD7002   .pG
        LD      (IX+$03),B              ; 31AF DD7003   .pS
        ADD     IX,DE                   ; 31B2 DD19     ..
        DEC     L                       ; 31B4 2D       -
        JR      NZ,Lb616                ; 31B5 20E1      .


        POP     IX                      ; 31B7 DDE1     ..
        POP     IY                      ; 31B9 FDE1     ..
        LD      BC,$800                 ; 31BB 010008   .DL
        ADD     IY,BC                   ; 31BE FD09     ..
        LD      HL,$31F8                ; 31C0 21F831   !.a
        LD      B,$06                   ; 31C3 0606     ..
        LD      DE,$FFDC                ; 31C5 11DCFF   ...

Lb619:  LD      C,$04                   ; 31C8 0E04     ..

Lb617:  LD      (IY+$00),$17            ; 31CA FD360017 .6DW
        LD      A,(HL)                  ; 31CE 7E       ~
        LD      (IX+$00),A              ; 31CF DD7700   .wD
        INC     HL                      ; 31D2 23       #
        INC     IY                      ; 31D3 FD23     .#
        INC     IX                      ; 31D5 DD23     .#
        DEC     C                       ; 31D7 0D       .
        JR      NZ,Lb617                ; 31D8 20F0      .

        DEC     B                       ; 31DA 05       .
        JR      Z,Lb618                 ; 31DB 2807     (F

        INC     HL                      ; 31DD 23       #
        ADD     IX,DE                   ; 31DE DD19     ..
        ADD     IY,DE                   ; 31E0 FD19     ..
        JR      Lb619                   ; 31E2 18E4     ..

Lb618:  NOP                             ; 31E4 00       .
        XOR     A                       ; 31E5 AF       .
        LD      (KEEP_SAME_ISR_FLAG),A  ; 31E6 324480   2..  Process the next ISR table location
        RET                             ; 31E9 C9       .


;-------------------------------------------------------------------------------
; Data Start
; Range: $31EA - $32BF
; Number of bytes: 214
;-------------------------------------------------------------------------------

        .db     $C7, $FB

; $31EC - Pointers into this data table
; Index	Address
; 0		$31F8
; 1		$31FD
; 2		$3202
; 3		$3207
; 4		$320C
; 5		$3211
        .db     $F8, $31
		.db		$FD, $31
		.db		$02, $32
		.db		$07, $32
        .db     $0C, $32
		.db		$11, $32
		.db		$0A, $0B, $2A, $2B, $FF					; $31F8 index 0
		.db		$08, $09, $28, $29, $FF					; $31FD index 1
		.db		$06, $07, $26, $27, $FF					; $3202 index 2
		.db		$04, $05, $24, $25, $FF					; $3207 index 3
        .db     $02, $03, $22, $23, $FF					; $320C index 4
		.db		$00, $01, $20, $21, $FF					; $3211 index 5

		.db		$26, $32, $2A, $32, $2E, $32			; $3216
        .db     $32, $32, $36, $32, $3A, $32, $3E, $32	; $321C
        .db     $42, $32, $4B, $43, $06, $04, $4C, $44	; $3224
        .db     $0F, $03, $4D, $45, $06, $04, $4C, $44	; $322C
        .db     $07, $03, $4B, $43, $47, $04, $4C, $44	; $3234
        .db     $0E, $03, $4B, $43, $07, $04, $4C, $44	; $323C
        .db     $4E, $03, $56, $32, $5A, $32, $5E, $32	; $3244
        .db     $62, $32, $66, $32, $6A, $32, $6E, $32	; $324C
        .db     $72, $32, $0B, $03, $46, $44, $0C, $04	; $3254
        .db     $4F, $43, $0D, $05, $46, $44, $0C, $04	; $325C
        .db     $47, $43, $0B, $03, $07, $44, $0C, $04	; $3264
        .db     $4E, $43, $0B, $03, $47, $44, $0C, $04	; $326C
        .db     $0E, $43								; $3274

		.db		$01, $4B, $15, $F0, $98, $00, $00, $00	; $3276	- to UNKNOWN_815C[0]
        .db     $01, $43, $15, $F0, $A8, $00, $00, $00	; $327E	- to UNKNOWN_815C[1]
        .db     $01, $04, $15, $F0, $B8, $00, $00, $00	; $3286 - to UNKNOWN_815C[2]
        .db     $01, $04, $15, $F0, $C8, $00, $00, $00	; $328E	- to UNKNOWN_815C[3]

        .db     $01, $0B, $15, $F0, $80, $00, $00, $00	; $3296	- to UNKNOWN_815C[0]
        .db     $01, $03, $15, $F0, $70, $00, $00, $00	; $329E	- to UNKNOWN_815C[1]
        .db     $01, $46, $15, $F0, $60, $00, $00, $00	; $32A6 - to UNKNOWN_815C[2]
        .db     $01, $44, $15, $F0, $50, $00, $00, $00	; $32AE	- to UNKNOWN_815C[3]

        .db     $04, $04, $03, $03, $02, $02, $01, $01	; $32B6
        .db     $C7, $F3								; $32BE

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------



;=============================================================================
;=============================================================================
Lb526:  PUSH    IX                      ; 32C0 DDE5     ..
        PUSH    HL                      ; 32C2 E5       .
        PUSH    DE                      ; 32C3 D5       .
        LD      IX,CLIMBER_SPRITE_CTRL  ; 32C4 DD213281 .!'. Point to the climber sprite control area
        LD      H,$04                   ; 32C8 2604     &.

Lb630:  LD      D,(IX+$02)              ; 32CA DD5602   .VG
        LD      A,B                     ; 32CD 78       x
        SUB     D                       ; 32CE 92       .
        JP      C,Lb624                 ; 32CF DA2C33   .|2
        CP      $10                     ; 32D2 FE10     ..
        JP      NC,Lb624                ; 32D4 D22C33   .=r

        RRCA                            ; 32D7 0F       .
        RRCA                            ; 32D8 0F       .
        AND     $3F                     ; 32D9 E63F     ..
        LD      D,A                     ; 32DB 57       W
        LD      E,(IX+$03)              ; 32DC DD5E03   .^.
        LD      A,C                     ; 32DF 79       y
        SUB     E                       ; 32E0 93       .
        JP      C,Lb624                 ; 32E1 DA2C33   .|2

        CP      $10                     ; 32E4 FE10     ..
        JP      NC,Lb624                ; 32E6 D22C33   .=r

        RRCA                            ; 32E9 0F       .
        RRCA                            ; 32EA 0F       .
        AND     $3F                     ; 32EB E63F     ..
        LD      E,A                     ; 32ED 5F       _
        LD      HL,$333E                ; 32EE 213E33   !.r
        LD      A,(IX+$00)              ; 32F1 DD7E00   .~D
        AND     $0F                     ; 32F4 E60F     ..
        RLCA                            ; 32F6 07       .
        RLCA                            ; 32F7 07       .
        ADD     A,D                     ; 32F8 82       .
        PUSH    DE                      ; 32F9 D5       .
        LD      E,A                     ; 32FA 5F       _
        LD      D,$00                   ; 32FB 1600     .D
        ADD     HL,DE                   ; 32FD 19       .
        POP     DE                      ; 32FE D1       .
        SBC     A,B                     ; 32FF 98       .
        BIT     0,H                     ; 3300 CB44     .D
        LD      (HL),A                  ; 3302 77       w
        JR      Z,Lb625                 ; 3303 2805     (.

        LD      A,E                     ; 3305 7B       {
        CPL                             ; 3306 2F       /
        AND     $03                     ; 3307 E603     ..
        LD      E,A                     ; 3309 5F       _

Lb625:  LD      A,(HL)                  ; 330A 7E       ~
        INC     E                       ; 330B 1C       .

Lb626:  RRA                             ; 330C 1F       .
        DEC     E                       ; 330D 1D       .
        JR      NZ,Lb626                ; 330E 20FC      .

        JR      NZ,Lb627                ; 3310 3016     0.

        SBC     A,C                     ; 3312 99       .
        BIT     0,H                     ; 3313 CB44     .D
        LD      (HL),$69                ; 3315 3669     6(
        DEC     D                       ; 3317 15       .
        LD      E,$81                   ; 3318 1E81     ..
        JR      Lb628                   ; 331A 1802     ..

        LD      E,$01                   ; 331C 1E01     ..

Lb628:  LD      A,($8282)               ; 331E 3A8282   :}.
        ADD     A,E                     ; 3321 83       .
        LD      ($8282),A               ; 3322 328282   2}.
        LD      A,E                     ; 3325 7B       {
        JR      Lb629                   ; 3326 180F     ..

Lb627:  LD      A,$00                   ; 3328 3E00     >D
        JR      Lb629                   ; 332A 180B     .[

Lb624:  DEC     H                       ; 332C 25       %
        JR      Z,Lb627                 ; 332D 28F9     (.

        LD      DE,$04                  ; 332F 110400   .TD
        ADD     IX,DE                   ; 3332 DD19     ..
        JP      Lb630                   ; 3334 C3CA32   ..'

Lb629:  POP     DE                      ; 3337 D1       .
        POP     HL                      ; 3338 E1       .
        POP     IX                      ; 3339 DDE1     ..
        RET                             ; 333B C9       .

;-------------------------------------------------------------------------------
; Data Start
; Range: $333C - $337F
; Number of bytes: 68
;-------------------------------------------------------------------------------

        .db     $C7, $FB

; $333E
        .db     $0F, $07, $01, $01, $0F, $01, $01, $00
        .db     $07, $0D, $01, $00, $07, $05, $0D, $00
        .db     $01, $03, $07, $0C, $03, $03, $01, $01
        .db     $03, $01, $01, $00, $07, $03, $01, $00
        .db     $03, $03, $03, $00, $03, $03, $03, $03
        .db     $04, $06, $03, $01, $02, $02, $01, $01
        .db     $03, $01, $03, $01, $00, $03, $03, $01
        .db     $00, $01, $02, $03, $00, $00, $07, $03
        .db     $C7, $F3

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------

;-------------------------------------------------------------------------------
; Wastes some time (delay)
;-------------------------------------------------------------------------------
ISR_JUMP3_DELAY:
        LD      A,$FF                   ; 3380 3EFF     >.
        CALL    DELAY                   ; 3382 CDB802   ..G Delay

        LD      A,$FF                   ; 3385 3EFF     >.
        LD      ($82B8),A               ; 3387 32B882   2.}	$82B8 = FF
        RET                             ; 338A C9       .

;=============================================================================
;=============================================================================
CHECK_DUMBELLS:
        LD      A,(ISR_JUMP3_CNTR3)     ; 338B 3ABA82   :.}	ISR_JUMP3_CNTR3 is limited to <= 3
        AND     $03                     ; 338E E603     .S
        AND     A                       ; 3390 A7       .	Is ISR_JUMP3_CNTR3 zero?
        RET     Z                       ; 3391 C8       .	Yes, return

        INC     A                       ; 3392 3C       <	
        LD      ($82A4),A               ; 3393 32A482   2.}	$82A4 = (ISR_JUMP3_CNTR3 & 0x03) + 1
        CALL    CREATE_DUMBELLS         ; 3396 CD4E38   .Z9 
        RET                             ; 3399 C9       .	End CHECK_DUMBELLS


;=============================================================================
; Handle the evil bird
; 
; This routine checks to see if the bird is spawned. Once it is, the bird music
; begins to play and the bird is animated and moved.  Finally, a routine is
; called that checks services the bird poop.
;=============================================================================
ISR_JUMP3_BIRD:
        LD      A,(GP_82AF)             ; 339A 3AAF82   :..	Get counter
        AND     A                       ; 339D A7       .	Is value zero?
        JR      NZ,Lb642                ; 339E 201D      Y	Nope, go here

        LD      A,(FLOOR_GROUP_IDX)     ; 33A0 3ADC80   :..	Get the current building floor group
        AND     $03                     ; 33A3 E603     ..
        CP      $03                     ; 33A5 FE03     ..	Is the FLOOR_GROUP_IDX != 3?
        JR      NZ,Lb643                ; 33A7 2006      .	Yes, go here

        LD      A,$FF                   ; 33A9 3EFF     >.	FLOOR_GROUP_IDX is 3
        LD      ($82B8),A               ; 33AB 32B882   2.}	$82B8 = $FF
        RET                             ; 33AE C9       .

Lb643:  CP      $00                     ; 33AF FE00     .D	Is FLOOR_GROUP_IDX != 0?
        JR      NZ,Lb644                ; 33B1 2006      .	Yes, go here

; We found the bird!
        LD      BC,$406                 ; 33B3 010604   ...	Play Bird Music
        CALL    LOAD_SOUND_DATA         ; 33B6 CDBB11   ..A

Lb644:  CALL    INIT_BIRD_GFX           ; 33B9 CDE033   ..2	Initialize the bird graphics
        RET                             ; 33BC C9       .

Lb642:  LD      A,(FLOOR_GROUP_IDX)     ; 33BD 3ADC80   :..	Get the current building floor group
        AND     $03                     ; 33C0 E603     .S
        CP      $03                     ; 33C2 FE03     .S	Is FLOOR_GROUP_IDX= 3
        JR      Z,Lb646                 ; 33C4 2813     (.	Yes, go here

        LD      A,(GP_82AF)             ; 33C6 3AAF82   :..	Get counter value
        CP      $09                     ; 33C9 FE09     ..	Is counter = 9?
        JR      NZ,Lb646                ; 33CB 300C     0\	Nope, go here

        BIT     0,A                     ; 33CD CB47     .G	Is counter even?
        CALL    Z,CHECK_BIRD_POOP       ; 33CF CCEA35   ..q	Yes, check bird poop

        CALL    MOVE_BIRD1              ; 33D2 CD4534   .P%
        CALL    BIRD_ANIMATION          ; 33D5 CD0435   .Tq	Animate the bird
        RET                             ; 33D8 C9       .

Lb646:  CALL    BIRD_ANIMATION          ; 33D9 CD0435   .Tq	Animate the bird
        CALL    MOVE_BIRD2              ; 33DC CDBA34   ..%
        RET                             ; 33DF C9       .	End ISR_JUMP3_BIRD

;-------------------------------------------------------------------------------
; Initialize the evil bird bigsprite graphics
;-------------------------------------------------------------------------------
INIT_BIRD_GFX:
        LD      IY,BIG_SPRITE_CTRL      ; 33E0 FD21DC98 .!..  Point to big sprite control
        LD      (IY+$00),$00            ; 33E4 FD360000 .6DD  Set big sprite number (priority?)
        LD      (IY+$02),$F0            ; 33E8 FD3602F0 .6G.  Set big sprite Y position
        LD      A,(BIGSPRITE_DIRECTION) ; 33EC 3AAE82   :..	  Change the bigsprite direction
        XOR     $01                     ; 33EF EE01     ..	  
        AND     $01                     ; 33F1 E601     ..	  
        LD      (BIGSPRITE_DIRECTION),A ; 33F3 32AE82   2.}	  
        JR      NZ,Lb651                ; 33F6 200A      .	  Are we moving left? go here

; Set bird facing left (normal - no X-axis inversion)
        LD      (IY+$01),$02            ; 33F8 FD360102 .6..  Set big sprite color
        LD      (IY+$03),$F0            ; 33FC FD3603F0 .6..  Set big sprite x position
        JR      Lb652                   ; 3400 1808     .L

; Set bird facing right (invert X axis)
Lb651:  LD      (IY+$01),$12            ; 3402 FD360112 .6.F Set big sprite color (2) and invert X
        LD      (IY+$03),$90            ; 3406 FD360390 .6.. Set big sprite x position

Lb652:  CALL    CHECK_FIELD_INVERSION   ; 340A CD8311   .|A   Check to see if field is inverted
        AND     A                       ; 340D A7       .
        JR      NZ,Lb653                ; 340E 2008      L    Normal field, go here

; Inverted field
        LD      A,(IY+$03)              ; 3410 FD7E03   .~.	  Y = $F0
        ADD     A,$20                   ; 3413 C620     .d	  Y = $F0 + $20 = $10
        LD      (IY+$03),A              ; 3415 FD7703   .wS	  Set sprite x position for inverted field

;------------------------
; Set up bigsprite RAM for the bird
;------------------------
Lb653:  LD      IX,$88C6                ; 3418 DD21C688 .!.w  Dest - Big sprite RAM
        LD      HL,BIRD_DATA            ; 341C 216235   !3p   Source - Bird Data
        CALL    COPY_BIGSPRITE_2X2      ; 341F CD4F35   .Jq   Copy 2x2 big sprite

        LD      IX,$88C8                ; 3422 DD21C888 .!.w  Dest - Big sprite RAM
        INC     HL                      ; 3426 23       #     Source - Go to next data location
        CALL    COPY_BIGSPRITE_2X2      ; 3427 CD4F35   .Jq   Copy 2x2 big sprite

        LD      IX,$88E6                ; 342A DD21E688 .!.w  Dest - Big sprite RAM
        INC     HL                      ; 342E 23       #     Source - Go to next data location
        CALL    COPY_BIGSPRITE_2X2      ; 342F CD4F35   .Jq   Copy 2x2 big sprite

        LD      IX,$88E8                ; 3432 DD21E888 .!.w  Dest - Big sprite RAM
        INC     HL                      ; 3436 23       #     Source - Go to next data location
        CALL    COPY_BIGSPRITE_2X2      ; 3437 CD4F35   .Jq   Copy 2x2 big sprite

        LD      A,$30                   ; 343A 3E30     > 
        LD      (GP_TIMING),A           ; 343C 32B082   2..   Used to time the bird animation
        LD      A,$01                   ; 343F 3E01     >.
        LD      (GP_82AF),A             ; 3441 32AF82   2P}   Set counter to 1
        RET                             ; 3444 C9       .	  End INIT_BIRD_GFX


;=============================================================================
; Moves the Bird left/right and up/down.
;=============================================================================
MOVE_BIRD1:
        LD      IY,BIG_SPRITE_CTRL      ; 3445 FD21DC98 .!.. Point to big sprite control
        LD      A,(GP_82AF)             ; 3449 3AAF82   :P}  Get counter value
        BIT     0,A                     ; 344C CB47     .G   Is counter even?
        JR      Z,Lb654                 ; 344E 2835     (q   Yes, go here (check Y limit)

        LD      A,(IY+$02)              ; 3450 FD7E02   .~G	Get Y position
        CP      $B0                     ; 3453 FEB0     ..	is Y = $B0?
        JR      NZ,Lb655                ; 3455 3009     0.	No, go here

        LD      A,(GP_82AF)             ; 3457 3AAF82   :P}  Add 1 to counter
        ADD     A,$01                   ; 345A C601     ..
        LD      (GP_82AF),A             ; 345C 32AF82   2..
        RET                             ; 345F C9       .	End MOVE_BIRD1

Lb655:  LD      A,(ISR_COUNTER)         ; 3460 3A4580   :P.  Get the interrupt counter
        AND     $03                     ; 3463 E603     ..	Is ISR_COUNTER != 3?
        JR      NZ,Lb656                ; 3465 2015      P	Yes, go here (move down)

; Check direction and move accordingly
        LD      A,(BIGSPRITE_DIRECTION) ; 3467 3AAE82   :.}	Get direction
        AND     A                       ; 346A A7       .
        LD      A,(IY+$03)              ; 346B FD7E03   .~S	A = X position
        JR      NZ,Lb657                ; 346E 2007      .	If direction is left, move left

; Move right
        ADD     A,$01                   ; 3470 C601     ..	X = X + 1
        LD      (IY+$03),A              ; 3472 FD7703   .w.
        JR      Lb656                   ; 3475 1805     ..	Continue

; Move left
Lb657:  SUB     $01                     ; 3477 D601     ..	X = X - 1
        LD      (IY+$03),A              ; 3479 FD7703   .wS	Save X position

; Move down
Lb656:  LD      A,(IY+$02)              ; 347C FD7E02   .~G	Y position
        SUB     $01                     ; 347F D601     ..
        LD      (IY+$02),A              ; 3481 FD7702   .w.
        RET                             ; 3484 C9       .	End MOVE_BIRD1

; Check Y limit
Lb654:  LD      A,(IY+$02)              ; 3485 FD7E02   .~.	Y position
        CP      $D0                     ; 3488 FED0     ..	Is Y < $D0?
        JR      C,Lb658                 ; 348A 3809     8.	Yes, go here

        LD      A,(GP_82AF)             ; 348C 3AAF82   :..  Add 1 to counter
        ADD     A,$01                   ; 348F C601     ..
        LD      (GP_82AF),A             ; 3491 32AF82   2P}
        RET                             ; 3494 C9       .	End MOVE_BIRD1

Lb658:  LD      A,(ISR_COUNTER)         ; 3495 3A4580   :U.	Get the interrupt counter
        AND     $03                     ; 3498 E603     .S	Is ISR_COUINTER != 3? 
        JR      NZ,Lb659                ; 349A 2015      Q	Yes, move up

        LD      A,(BIGSPRITE_DIRECTION) ; 349C 3AAE82   :..	Check the direction
        AND     A                       ; 349F A7       .
        LD      A,(IY+$03)              ; 34A0 FD7E03   .~.	A = X position
        JR      NZ,Lb660                ; 34A3 2007      F	Go here if we are moving left

; Move right
        ADD     A,$01                   ; 34A5 C601     ..	X = X + 1
        LD      (IY+$03),A              ; 34A7 FD7703   .wS
        JR      Lb659                   ; 34AA 1805     .U	Continue

; Move left
Lb660:  SUB     $01                     ; 34AC D601     ..	X = X - 1
        LD      (IY+$03),A              ; 34AE FD7703   .w.

; Move up
Lb659:  LD      A,(IY+$02)              ; 34B1 FD7E02   .~.	Y position
        ADD     A,$01                   ; 34B4 C601     ..	Y = Y + 1
        LD      (IY+$02),A              ; 34B6 FD7702   .wG
        RET                             ; 34B9 C9       .	End MOVE_BIRD1


;=============================================================================
; Moves the bird, but first checks the Y position. If the Y position is
; >= $E8, the Y position is set to $F0 and the top half of the bird is
; cleared (clears the bird?) I don't know why the bottom half of the bird is
; still left in BigSprite RAM though...
;
; This will move the bird left/right and up (not down). 
;=============================================================================
MOVE_BIRD2:
        LD      IY,BIG_SPRITE_CTRL      ; 34BA FD21DC98 .!.. Point to big sprite control
        LD      A,(IY+$02)              ; 34BE FD7E02   .~G	Y Position
        CP      $E8                     ; 34C1 FEE8     ..	Is Y < $E8?
        JR      C,Lb661                 ; 34C3 381A     8.	Yes, go here

; The bird's Y position is >= $E8
        XOR     A                       ; 34C5 AF       .
        LD      (GP_82B1),A             ; 34C6 32B182   2..	Clear bird animation index
        LD      (GP_82AF),A             ; 34C9 32AF82   2P}	Clear counter
        LD      (IY+$02),$F0            ; 34CC FD3602F0 .6G. Y position = $F0
        LD      (IY+$00),$00            ; 34D0 FD360000 .6DD Priority? = 0

; This clears the top-half of the bird, but not the bottom half
; Clear 16 bytes of bigsprite RAM at offset $C0
        LD      A,$C0                   ; 34D4 3EC0     >.  
        CALL    CLR_16_BSPRITE_RAM      ; 34D6 CD1E3F   ...

; Clear 16 bytes of bigsprite RAM at offset $D0
        LD      A,$D0                   ; 34D9 3ED0     >.
        CALL    CLR_16_BSPRITE_RAM      ; 34DB CD1E3F   .[.
        RET                             ; 34DE C9       .	End MOVE_BIRD2

Lb661:  LD      A,(ISR_COUNTER)         ; 34DF 3A4580   :U.	Get the interrupt counter
        AND     $03                     ; 34E2 E603     .S	Is ISR_COUNTER != 3?
        JR      NZ,Lb663                ; 34E4 2015      Q	Yes, go here (move up)

        LD      A,(BIGSPRITE_DIRECTION) ; 34E6 3AAE82   :..	Check the bigsprite direction
        AND     A                       ; 34E9 A7       .
        LD      A,(IY+$03)              ; 34EA FD7E03   .~.	A = X direction
        JR      NZ,Lb664                ; 34ED 2007      F	Go here if we are moving left

; Move right
        ADD     A,$01                   ; 34EF C601     ..	X = X + 1
        LD      (IY+$03),A              ; 34F1 FD7703   .wS
        JR      Lb663                   ; 34F4 1805     .U	Continue

; Move left
Lb664:  SUB     $01                     ; 34F6 D601     ..	X = X - 1
        LD      (IY+$03),A              ; 34F8 FD7703   .w.

; Move up
Lb663:  LD      A,(IY+$02)              ; 34FB FD7E02   .~.	Y = Y + 1
        ADD     A,$01                   ; 34FE C601     ..
        LD      (IY+$02),A              ; 3500 FD7702   .wG
        RET                             ; 3503 C9       .	End MOVE_BIRD2


;=============================================================================
; Animates the bird
;=============================================================================
BIRD_ANIMATION:
        LD      A,(GP_TIMING)           ; 3504 3AB082   :..  Get bird animation counter
        AND     A                       ; 3507 A7       .    Equal to zero?
        JR      Z,Lb665                 ; 3508 2805     (U   Yes, time to animate
        DEC     A                       ; 350A 3D       =    Nope, decrement counter
        LD      (GP_TIMING),A           ; 350B 32B082   2.}  Save new value
        RET                             ; 350E C9       .    End BIRD_ANIMATION

; Time to animate the bird
Lb665:  LD      A,(GP_82B1)             ; 350F 3AB182   :.}  Get bird animation index
        RLCA                            ; 3512 07       .    Multiply by 4 (4 bytes of data per animation)
        RLCA                            ; 3513 07       .
        LD      E,A                     ; 3514 5F       _
        LD      D,$00                   ; 3515 1600     .D
        LD      HL,BIRD_DATA            ; 3517 216235   !cq  Point to bird data
        ADD     HL,DE                   ; 351A 19       .    Source = BIRD_DATA + (4 * index)
        LD      IX,$88C6                ; 351B DD21C688 .!.. Destination
        CALL    COPY_BIGSPRITE_2X2      ; 351F CD4F35   .Jq  Copy 2x2 big sprite

        INC     HL                      ; 3522 23       #    Source
        LD      IX,$88C8                ; 3523 DD21C888 .!.. Destination
        CALL    COPY_BIGSPRITE_2X2      ; 3527 CD4F35   .Jq  Copy 2x2 big sprite

        INC     HL                      ; 352A 23       #    Source
        LD      IX,$88E6                ; 352B DD21E688 .!.. Destination
        CALL    COPY_BIGSPRITE_2X2      ; 352F CD4F35   .Jq  Copy 2x2 big sprite

        INC     HL                      ; 3532 23       #    Source
        LD      IX,$88E8                ; 3533 DD21E888 .!.. Destination
        CALL    COPY_BIGSPRITE_2X2      ; 3537 CD4F35   .Jq  Copy 2x2 big sprite

        LD      A,(GP_82AF)             ; 353A 3AAF82   :..  Get counter
        AND     $01                     ; 353D E601     ..   Isolate bit 0
        LD      (GP_TIMING),A           ; 353F 32B082   2.}  Save value for bird timing

        LD      A,(GP_82B1)             ; 3542 3AB182   :..  Get bird animation index
        INC     A                       ; 3545 3C       <    Go to next index
        CP      $06                     ; 3546 FE06     .G   Is index < 6?
        JR      C,Lb666                 ; 3548 3801     8.   Yes, continue

        XOR     A                       ; 354A AF       .    Cycle bird animation index
Lb666:  LD      (GP_82B1),A             ; 354B 32B182   2.}  Save new bird animation index
        RET                             ; 354E C9       .    End BIRD_ANIMATION


;=============================================================================
; Description:
;
; Copies 4 big sprite data bytes to big sprite RAM.  They are copied to the
; screen in a 2 x 2 block. Note: Each row of big sprite RAM is 16 bytes.
;
; 1 2
; 3 4
;
; The starting value is read at (HL).  This value is the top left value.  The
; next values at 2 (top right), 3 (bottom left) and 4 (bottom right) are 
; incremental values from the given first value.
;
; Input:
; HL contains the location where the first value is read
; IX points to the desired big sprite RAM space
;
; Destroys:
;	A
;=============================================================================
COPY_BIGSPRITE_2X2:
        LD      A,(HL)                  ; 354F 7E       ~   Get the 1st value
        LD      (IX+$00),A              ; 3550 DD7700   .wD Top left
        INC     A                       ; 3553 3C       <   Next in series
        LD      (IX+$01),A              ; 3554 DD7701   .w. Top right
        INC     A                       ; 3557 3C       <   Next in series
        LD      (IX+$10),A              ; 3558 DD7710   .w. Next row, below 1st value
        INC     A                       ; 355B 3C       <   Next in series
        LD      (IX+$11),A              ; 355C DD7711   .wA Below 2nd value
        RET                             ; 355F C9       .   End COPY_BIGSPRITE_2X2

;-------------------------------------------------------------------------------
; Data Start
; Range: $3560 - $357B
; Number of bytes: 28
;-------------------------------------------------------------------------------

        .db     $C7, $FB								; Start data block

; $3562 - Bird data (animated sequence)
BIRD_DATA:
        .db     $10, $30, $14, $34			; Index 0
		.db     $18, $38, $1C, $3C			; Index 1
        .db     $50, $70, $54, $74			; Index 2
		.db     $58, $78, $5C, $7C			; Index 3
        .db     $50, $70, $54, $74			; Index 4
		.db     $18, $38, $1C, $3C			; Index 5

        .db     $C7, $F3								; End data block



;=============================================================================
;=============================================================================
Lb519:  LD      A,(IX+$05)              ; 357C DD7E05   .~.
        CP      $01                     ; 357F FE01     ..
        JR      Z,Lb670                 ; 3581 281A     (.

        DEC     (IX+$06)                ; 3583 DD3506   .5G
        RET     NZ                      ; 3586 C0       .

        LD      A,(IX+$01)              ; 3587 DD7E01   .~.
        INC     A                       ; 358A 3C       <
        LD      C,A                     ; 358B 4F       O
        AND     $03                     ; 358C E603     .S
        JR      NZ,Lb669                ; 358E 2005      U

        LD      (IX+$00),$00            ; 3590 DD360000 .6DD
        RET                             ; 3594 C9       .

Lb669:  LD      (IX+$01),C              ; 3595 DD7101   .q.
        LD      (IX+$06),$03            ; 3598 DD360603 .6.S
        RET                             ; 359C C9       .

Lb670:  LD      B,(IX+$03)              ; 359D DD4603   .FS
        LD      A,(IX+$04)              ; 35A0 DD7E04   .~T
        ADD     A,$08                   ; 35A3 C608     .L
        LD      C,A                     ; 35A5 4F       O
        CALL    Lb526                   ; 35A6 CDC032   ..'
        AND     A                       ; 35A9 A7       .
        JR      Z,Lb671                 ; 35AA 280B     ([

        NOP                             ; 35AC 00       .
        NOP                             ; 35AD 00       .
        NOP                             ; 35AE 00       .
        NOP                             ; 35AF 00       .
        NOP                             ; 35B0 00       .
        NOP                             ; 35B1 00       .
        LD      (IX+$05),$02            ; 35B2 DD360502 .6..
        RET                             ; 35B6 C9       .

Lb671:  DEC     (IY+$02)                ; 35B7 FD3502   .5.
        JR      NZ,Lb672                ; 35BA 2010      .
        LD      A,(IY+$05)              ; 35BC FD7E05   .~.
        LD      (IY+$02),A              ; 35BF FD7702   .w.
        LD      A,$05                   ; 35C2 3E05     >U
        CP      (IY+$03)                ; 35C4 FDBE03   ...
        JR      C,Lb672                 ; 35C7 3803     8.

        INC     (IY+$03)                ; 35C9 FD3403   .4S

Lb672:  LD      A,(IX+$03)              ; 35CC DD7E03   .~.
        SUB     (IY+$03)                ; 35CF FD9603   ..S
        LD      (IX+$03),A              ; 35D2 DD7703   .w.
        DEC     (IY+$00)                ; 35D5 FD3500   .5D
        JR      NZ,Lb673                ; 35D8 200F      .

        LD      A,(IX+$04)              ; 35DA DD7E04   .~T
        ADD     A,(IY+$01)              ; 35DD FD8601   ...
        LD      (IX+$04),A              ; 35E0 DD7704   .wT
        LD      A,(IY+$04)              ; 35E3 FD7E04   .~.
        LD      (IY+$00),A              ; 35E6 FD7700   .wD

Lb673:  RET                             ; 35E9 C9       .


;=============================================================================
; Checks and handles the bird poop
;=============================================================================
CHECK_BIRD_POOP:
        LD      A,(ISR_JUMP3_CNTR1)     ; 35EA 3A2081   :d.
        AND     $07                     ; 35ED E607     .F
        RET     NZ                      ; 35EF C0       .	End CHECK_BIRD_POOP

        LD      A,(ISR_JUMP3_CNTR3)     ; 35F0 3ABA82   :..
        AND     $02                     ; 35F3 E602     .G
        ADD     A,$02                   ; 35F5 C602     .G
        LD      B,A                     ; 35F7 47       G
        LD      IX,UNKNOWN_815C         ; 35F8 DD215C81 .!..
        LD      IY,UNKNOWN_8283         ; 35FC FD218382 .!.}
        LD      DE,$08                  ; 3600 110800   .LD

Lb676:  LD      A,(IX+$00)              ; 3603 DD7E00   .~D
        AND     A                       ; 3606 A7       .
        JR      NZ,Lb674                ; 3607 2007      F
        LD      A,(IY+$06)              ; 3609 FD7E06   .~G
        CP      $01                     ; 360C FE01     ..
        JR      NZ,Lb675                ; 360E 2008      L	Yes, go to bird pooping

Lb674:  DEC     B                       ; 3610 05       .
        RET     Z                       ; 3611 C8       .	End CHECK_BIRD_POOP

        ADD     IX,DE                   ; 3612 DD19     ..
        ADD     IY,DE                   ; 3614 FD19     ..
        JR      Lb676                   ; 3616 18EB     ..

; Bird poops here
Lb675:  LD      BC,$304                 ; 3618 010403   ...	Play Bird poop sound
        CALL    LOAD_SOUND_DATA         ; 361B CDBB11   ..A

        LD      A,($8135)               ; 361E 3A3581   :q. Climber left leg sprite X position
        LD      D,A                     ; 3621 57       W
        LD      A,($98DF)               ; 3622 3ADF98   :..
        LD      E,A                     ; 3625 5F       _
        LD      A,(BIGSPRITE_DIRECTION) ; 3626 3AAE82   :..
        AND     A                       ; 3629 A7       .	Is the bigsprite moving left?
        JR      NZ,Lb677                ; 362A 202D      }	Yes, go here

        LD      A,(CURRENT_PLAYER)      ; 362C 3A8180   :.. Check current player
        AND     A                       ; 362F A7       .
        LD      A,E                     ; 3630 7B       {
        JR      Z,Lb678                 ; 3631 2802     (G

        ADD     A,$80                   ; 3633 C680     ..

Lb678:  NEG                             ; 3635 ED44     .D
        SUB     $50                     ; 3637 D650     .E
        SUB     D                       ; 3639 92       .
        LD      E,$03                   ; 363A 1E03     .S
        JR      C,Lb679                 ; 363C 380B     8[

Lb680:  CP      $18                     ; 363E FE18     ..
        JR      C,Lb679                 ; 3640 3807     8.

        DEC     E                       ; 3642 1D       .
        JR      Z,Lb679                 ; 3643 2804     (T

        SUB     $10                     ; 3645 D610     ..
        JR      Lb680                   ; 3647 18F5     ..

Lb679:  CALL    CHECK_FIELD_INVERSION   ; 3649 CD8311   ..A Check to see if field is inverted
        AND     A                       ; 364C A7       .
        JR      NZ,Lb681                ; 364D 2005      .  Normal field, go here

; Inverted field
        LD      HL,$36F4                ; 364F 21F436   !..  Point to data area
        JR      Lb682                   ; 3652 1831     .a

; Normal field
Lb681:  LD      HL,$3704                ; 3654 210437   !.&
        JR      Lb682                   ; 3657 182C     .|

Lb677:  CALL    CHECK_FIELD_INVERSION   ; 3659 CD8311   ..A  Check to see if field is inverted
        AND     A                       ; 365C A7       .    A = 0 means inverted, 1 = normal
        LD      A,E                     ; 365D 7B       {
        JR      NZ,Lb683                ; 365E 2003      S

        SUB     $80                     ; 3660 D680     ..
        LD      E,A                     ; 3662 5F       _

Lb683:  NEG                             ; 3663 ED44     .D
        SUB     $30                     ; 3665 D630     .1
        SUB     D                       ; 3667 92       .
        LD      E,$03                   ; 3668 1E03     .S
        JR      NZ,Lb684                ; 366A 300B     0[

Lb685:  CP      $D8                     ; 366C FED8     ..
        JR      NZ,Lb684                ; 366E 3007     0.

        DEC     E                       ; 3670 1D       .
        JR      Z,Lb684                 ; 3671 2804     (T

        ADD     A,$10                   ; 3673 C610     ..
        JR      Lb685                   ; 3675 18F5     ..

Lb684:  CALL    CHECK_FIELD_INVERSION   ; 3677 CD8311   ..A Check to see if field is inverted
        AND     A                       ; 367A A7       .
        JR      NZ,Lb686                ; 367B 2005      .  Normal field, go here

; Inverted field
        LD      HL,$3704                ; 367D 210437   !Tw
        JR      Lb682                   ; 3680 1803     .S

; Normal field
Lb686:  LD      HL,$36F4                ; 3682 21F436   !.s

Lb682:  LD      A,E                     ; 3685 7B       {
        RLCA                            ; 3686 07       .
        RLCA                            ; 3687 07       .
        LD      E,A                     ; 3688 5F       _
        LD      D,$00                   ; 3689 1600     .D
        ADD     HL,DE                   ; 368B 19       .

        LD      A,(HL)                  ; 368C 7E       ~
        LD      (IY+$00),A              ; 368D FD7700   .wD
        LD      (IY+$04),A              ; 3690 FD7704   .wT
        INC     HL                      ; 3693 23       #
        LD      A,(HL)                  ; 3694 7E       ~
        LD      (IY+$01),A              ; 3695 FD7701   .w.
        INC     HL                      ; 3698 23       #
        LD      A,(HL)                  ; 3699 7E       ~
        LD      (IY+$02),A              ; 369A FD7702   .wG
        LD      (IY+$05),A              ; 369D FD7705   .wU
        LD      (IY+$03),$01            ; 36A0 FD360301 .6..
        LD      (IY+$06),$00            ; 36A4 FD360600 .6.D
        LD      (IY+$07),$02            ; 36A8 FD360702 .6F.
        LD      (IX+$00),$01            ; 36AC DD360001 .6D.
        LD      A,(RANDOM_NUMBER)       ; 36B0 3A2281   :&.  Get random value
        BIT     5,A                     ; 36B3 CB6F     .o

        JR      Z,Lb687                 ; 36B5 280A     (O
        LD      (IX+$01),$28            ; 36B7 DD360128 .6.l
        LD      (IX+$02),$03            ; 36BB DD360203 .6..
        JR      Lb688                   ; 36BF 1808     .L

Lb687:  LD      (IX+$01),$2C            ; 36C1 DD36012C .6.|
        LD      (IX+$02),$05            ; 36C5 DD360205 .6..

Lb688:  LD      (IX+$05),$01            ; 36C9 DD360501 .6U.
        LD      (IX+$06),$03            ; 36CD DD360603 .6G.
        LD      (IX+$07),$00            ; 36D1 DD360700 .6.D
        LD      A,($98DE)               ; 36D5 3ADE98   :..
        LD      (IX+$03),A              ; 36D8 DD7703   .w.

        CALL    CHECK_FIELD_INVERSION   ; 36DB CD8311   ..A Check to see if field is inverted
        AND     A                       ; 36DE A7       .
        LD      A,($98DF)               ; 36DF 3ADF98   :..
        JR      Z,Lb689                 ; 36E2 2808     (L

        NEG                             ; 36E4 ED44     .D
        SUB     $40                     ; 36E6 D640     ..
        LD      (IX+$04),A              ; 36E8 DD7704   .wT
        RET                             ; 36EB C9       .	End CHECK_BIRD_POOP

Lb689:  ADD     A,$30                   ; 36EC C630     . 
        LD      (IX+$04),A              ; 36EE DD7704   .wT
        RET                             ; 36F1 C9       .	End CHECK_BIRD_POOP


;-------------------------------------------------------------------------------
; Data Start
; Range: $36F2 - $3715
; Number of bytes: 36
;-------------------------------------------------------------------------------

        .db     $C7, $FB

; $36F4
        .db     $01, $01, $08, $00, $02, $02, $08, $00
        .db     $02, $01, $08, $00, $01, $00, $08, $00
        .db     $01, $FF, $08, $00, $02, $FE, $08, $00
        .db     $02, $FF, $08, $00, $01, $00, $08, $00
        .db     $C7, $F3

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------

        NOP                             ; 3716 00       .
        NOP                             ; 3717 00       .
        NOP                             ; 3718 00       .
        NOP                             ; 3719 00       .
        NOP                             ; 371A 00       .
        NOP                             ; 371B 00       .
        NOP                             ; 371C 00       .
        NOP                             ; 371D 00       .
        NOP                             ; 371E 00       .
        NOP                             ; 371F 00       .
        NOP                             ; 3720 00       .
        NOP                             ; 3721 00       .
        NOP                             ; 3722 00       .
        NOP                             ; 3723 00       .
        NOP                             ; 3724 00       .
        NOP                             ; 3725 00       .
        NOP                             ; 3726 00       .
        NOP                             ; 3727 00       .
        NOP                             ; 3728 00       .
        NOP                             ; 3729 00       .
        NOP                             ; 372A 00       .
        NOP                             ; 372B 00       .
        NOP                             ; 372C 00       .
        NOP                             ; 372D 00       .
        NOP                             ; 372E 00       .
        NOP                             ; 372F 00       .


;-------------------------------------------------------------------------------
;-------------------------------------------------------------------------------
ISR_JUMP3_DUMBELLS:
        LD      A,(FLOOR_GROUP_IDX)     ; 3730 3ADC80   :.. Get the current building floor group
        AND     $03                     ; 3733 E603     ..
        CP      $03                     ; 3735 FE03     ..
        JR      NZ,Lb692                ; 3737 2006      .

        LD      A,$FF                   ; 3739 3EFF     >.
        LD      ($82B8),A               ; 373B 32B882   2.}
        RET                             ; 373E C9       .

Lb692:  LD      A,(ISR_JUMP3_CNTR3)     ; 373F 3ABA82   :.}
        RLCA                            ; 3742 07       .   Offset = Offset * 2
        LD      E,A                     ; 3743 5F       _
        LD      D,$00                   ; 3744 1600     .D  
        LD      HL,DUMBELL_GIRDER_DATA  ; 3746 21323F   !f. Start of dumbell/girder animation data?
        ADD     HL,DE                   ; 3749 19       .   Add offset

        LD      A,(HL)                  ; 374A 7E       ~   Get data value
        LD      ($82A3),A               ; 374B 32A382   2.}
        LD      B,A                     ; 374E 47       G
        LD      A,(ISR_JUMP3_CNTR1)     ; 374F 3A2081   :d.
        AND     B                       ; 3752 A0       .
        JR      NZ,Lb693                ; 3753 2008      L

        INC     HL                      ; 3755 23       #
        LD      A,(HL)                  ; 3756 7E       ~
        LD      ($82A4),A               ; 3757 32A482   2.}
        CALL    CREATE_DUMBELLS         ; 375A CD4E38   .Z9

Lb693:  RET                             ; 375D C9       .


;=============================================================================
;=============================================================================
Lb520:  LD      A,(IX+$05)              ; 375E DD7E05   .~.
        CP      $01                     ; 3761 FE01     ..
        RET     NZ                      ; 3763 C0       .

        LD      A,(IX+$03)              ; 3764 DD7E03   .~.
        CP      $90                     ; 3767 FE90     ..
        JR      NZ,Lb694                ; 3769 3037     0&

        CP      $50                     ; 376B FE50     .E
        JR      C,Lb695                 ; 376D 3847     8B

        LD      A,(IX+$01)              ; 376F DD7E01   .~.
        AND     $03                     ; 3772 E603     .S
        RLCA                            ; 3774 07       .
        LD      B,A                     ; 3775 47       G
        RLCA                            ; 3776 07       .
        ADD     A,B                     ; 3777 80       .
        LD      E,A                     ; 3778 5F       _
        LD      D,$00                   ; 3779 1600     .D
        LD      HL,$3F4A                ; 377B 214A3F   !K.
        ADD     HL,DE                   ; 377E 19       .
        LD      E,$03                   ; 377F 1E03     ..

Lb696:  LD      A,(IX+$03)              ; 3781 DD7E03   .~S
        ADD     A,(HL)                  ; 3784 86       .
        LD      B,A                     ; 3785 47       G
        INC     HL                      ; 3786 23       #
        LD      A,(IX+$04)              ; 3787 DD7E04   .~.
        ADD     A,(HL)                  ; 378A 86       .
        LD      C,A                     ; 378B 4F       O
        CALL    Lb526                   ; 378C CDC032   ..'
        DEC     E                       ; 378F 1D       .
        INC     HL                      ; 3790 23       #
        JR      NZ,Lb696                ; 3791 20EE      .

        LD      A,($8282)               ; 3793 3A8282   :.}
        AND     $0E                     ; 3796 E60E     .O
        JR      Z,Lb695                 ; 3798 281C     (H

        LD      BC,$303                 ; 379A 010303   .S.	Play Hit by dumbell sound
        CALL    LOAD_SOUND_DATA         ; 379D CDBB11   ..A

        JR      Lb695                   ; 37A0 1814     .@

Lb694:  DEC     (IY+$00)                ; 37A2 FD3500   .5D
        JR      NZ,Lb695                ; 37A5 200F      N

        LD      A,(IX+$04)              ; 37A7 DD7E04   .~.
        ADD     A,(IY+$01)              ; 37AA FD8601   ...
        LD      (IX+$04),A              ; 37AD DD7704   .w.
        LD      A,(IY+$04)              ; 37B0 FD7E04   .~T
        LD      (IY+$00),A              ; 37B3 FD7700   .wD

Lb695:  LD      A,(IX+$03)              ; 37B6 DD7E03   .~.
        ADD     A,(IY+$03)              ; 37B9 FD8603   ..S
        LD      (IX+$03),A              ; 37BC DD7703   .w.
        DEC     (IY+$02)                ; 37BF FD3502   .5.
        JR      NZ,Lb697                ; 37C2 202C      =

        LD      A,(IY+$05)              ; 37C4 FD7E05   .~.
        LD      (IY+$02),A              ; 37C7 FD7702   .w.
        LD      A,$FB                   ; 37CA 3EFB     >.
        DEC     (IY+$03)                ; 37CC FD3503   .5.
        CP      (IY+$03)                ; 37CF FDBE03   ..S
        JR      C,Lb697                 ; 37D2 381C     8H

        LD      BC,$101                 ; 37D4 010101   ...	Play falling dumbell/girder sound
        CALL    LOAD_SOUND_DATA         ; 37D7 CDBB11   ..A

        LD      A,(IX+$03)              ; 37DA DD7E03   .~.
        CP      $90                     ; 37DD FE90     ..
        JR      C,Lb698                 ; 37DF 380B     8.

        LD      A,(IX+$04)              ; 37E1 DD7E04   .~.
        CP      $48                     ; 37E4 FE48     ..
        JR      C,Lb698                 ; 37E6 3804     8.

        CP      $C8                     ; 37E8 FEC8     ..
        JR      C,Lb699                 ; 37EA 383A     8n

Lb698:  LD      (IY+$03),$FC            ; 37EC FD3603FC .6..

Lb697:  DEC     (IX+$06)                ; 37F0 DD3506   .5.
        JR      NZ,Lb700                ; 37F3 2030      1

        LD      E,(IX+$07)              ; 37F5 DD5E07   .^.
        LD      D,$00                   ; 37F8 1600     .D
        LD      HL,$3F62                ; 37FA 21623F   !3.
        ADD     HL,DE                   ; 37FD 19       .
        LD      A,(IX+$01)              ; 37FE DD7E01   .~.
        BIT     2,A                     ; 3801 CB57     .W
        LD      A,(HL)                  ; 3803 7E       ~
        JR      Z,Lb701                 ; 3804 2802     (.

        ADD     A,$04                   ; 3806 C604     ..

Lb701:  LD      (IX+$01),A              ; 3808 DD7701   .w.
        INC     E                       ; 380B 1C       .
        LD      A,$06                   ; 380C 3E06     >G
        CP      E                       ; 380E BB       .
        JR      NZ,Lb702                ; 380F 2001      .

        LD      E,D                     ; 3811 5A       Z

Lb702:  LD      (IX+$07),E              ; 3812 DD7307   .sF
        LD      A,(RANDOM_NUMBER)       ; 3815 3A2281   :g.  Get random number
        AND     $07                     ; 3818 E607     ..
        LD      E,A                     ; 381A 5F       _
        LD      D,$00                   ; 381B 1600     .D
        LD      HL,$3F68                ; 381D 21683F   !y.
        ADD     HL,DE                   ; 3820 19       .
        LD      A,(HL)                  ; 3821 7E       ~
        LD      (IX+$06),A              ; 3822 DD7706   .w.

Lb700:  RET                             ; 3825 C9       .

Lb699:  LD      A,(RANDOM_NUMBER)       ; 3826 3A2281   :&. Get random number
        AND     $07                     ; 3829 E607     .F
        RLCA                            ; 382B 07       .
        RLCA                            ; 382C 07       .
        LD      E,A                     ; 382D 5F       _
        LD      D,$00                   ; 382E 1600     .D
        LD      HL,$3F70                ; 3830 21703F   !!.
        ADD     HL,DE                   ; 3833 19       .
        LD      A,(HL)                  ; 3834 7E       ~
        LD      (IY+$00),A              ; 3835 FD7700   .wD
        LD      (IY+$04),A              ; 3838 FD7704   .wT
        INC     HL                      ; 383B 23       #
        LD      A,(HL)                  ; 383C 7E       ~
        LD      (IY+$01),A              ; 383D FD7701   .w.
        INC     HL                      ; 3840 23       #
        LD      A,(HL)                  ; 3841 7E       ~
        LD      (IY+$02),A              ; 3842 FD7702   .wG
        LD      (IY+$05),A              ; 3845 FD7705   .wU
        INC     HL                      ; 3848 23       #
        LD      A,(HL)                  ; 3849 7E       ~
        LD      (IY+$03),A              ; 384A FD7703   .w.
        RET                             ; 384D C9       .

;=============================================================================
; Create girders / dumbells falling?
;=============================================================================
CREATE_DUMBELLS:
        LD      A,($82A4)               ; 384E 3AA482   :..
        LD      B,A                     ; 3851 47       G
        LD      IX,UNKNOWN_815C         ; 3852 DD215C81 .!..
        LD      IY,UNKNOWN_8283         ; 3856 FD218382 .!.}
        LD      DE,$08                  ; 385A 110800   .LD

Lb705:  LD      A,(IX+$00)              ; 385D DD7E00   .~D
        AND     A                       ; 3860 A7       .
        JR      NZ,Lb703                ; 3861 2007      F

        LD      A,(IY+$06)              ; 3863 FD7E06   .~G
        CP      $01                     ; 3866 FE01     ..
        JR      NZ,Lb704                ; 3868 2008      L

Lb703:  DEC     B                       ; 386A 05       .
        RET     Z                       ; 386B C8       .	

        ADD     IX,DE                   ; 386C DD19     ..
        ADD     IY,DE                   ; 386E FD19     ..
        JR      Lb705                   ; 3870 18EB     ..

Lb704:  LD      BC,$101                 ; 3872 010101   ...	Play falling dumbell/girder sound
        CALL    LOAD_SOUND_DATA         ; 3875 CDBB11   ..A

        LD      A,$01                   ; 3878 3E01     >.
        LD      (KEEP_SAME_ISR_FLAG),A  ; 387A 324480   2..  Keep processing the same ISR table location
        LD      (IX+$00),$01            ; 387D DD360001 .6D.
        LD      (IX+$02),$18            ; 3881 DD360218 .6..
        LD      (IX+$03),$F0            ; 3885 DD3603F0 .6S.
        LD      (IX+$05),$01            ; 3889 DD360501 .6U.
        LD      A,(ISR_JUMP3_CNTR1)     ; 388D 3A2081   :d.
        BIT     0,A                     ; 3890 CB47     .G
        JR      NZ,Lb706                ; 3892 2006      G

        LD      (IX+$01),$28            ; 3894 DD360128 .6.l
        JR      Lb707                   ; 3898 1804     ..

Lb706:  LD      (IX+$01),$2C            ; 389A DD36012C .6.=

Lb707:  LD      A,(RANDOM_NUMBER)       ; 389E 3A2281   :&.  Get random number
        AND     $07                     ; 38A1 E607     .F
        LD      E,A                     ; 38A3 5F       _
        LD      D,$00                   ; 38A4 1600     .D
        LD      HL,$3F42                ; 38A6 21423F   !..
        ADD     HL,DE                   ; 38A9 19       .
        LD      A,(HL)                  ; 38AA 7E       ~
        LD      (IX+$04),A              ; 38AB DD7704   .w.
        LD      HL,$3F68                ; 38AE 21683F   !<.
        ADD     HL,DE                   ; 38B1 19       .
        LD      A,(HL)                  ; 38B2 7E       ~
        LD      (IX+$06),A              ; 38B3 DD7706   .wG
        LD      (IY+$02),$08            ; 38B6 FD360208 .6GL
        LD      (IY+$03),$FF            ; 38BA FD3603FF .6..
        LD      (IY+$05),$04            ; 38BE FD360504 .6..
        LD      (IY+$07),$03            ; 38C2 FD360703 .6FS
        XOR     A                       ; 38C6 AF       .
        LD      (IX+$07),A              ; 38C7 DD7707   .w.
        LD      (IY+$00),A              ; 38CA FD7700   .wD
        LD      (IY+$01),A              ; 38CD FD7701   .w.
        LD      (IY+$04),A              ; 38D0 FD7704   .wT
        LD      (IY+$06),A              ; 38D3 FD7706   .wG
        XOR     A                       ; 38D6 AF       .
        LD      (KEEP_SAME_ISR_FLAG),A  ; 38D7 324480   2@.  Process the next ISR table location
        RET                             ; 38DA C9       .	 End CREATE_DUMBELLS


;---------------------------------------------------------------------------------------
; Create Balloon
;---------------------------------------------------------------------------------------
ISR_JUMP3_BALLOON:
        LD      IY,BIG_SPRITE_CTRL      ; 38DB FD21DC98 .!.. Point to big sprite control
        LD      A,($82B8)               ; 38DF 3AB882   :.}
        CP      $01                     ; 38E2 FE01     ..   Is value = 1?
        JR      Z,Lb708                 ; 38E4 2814     (@   Yes, go here (draws balloon)

        CP      $02                     ; 38E6 FE02     ..   Is value = 2?
        JR      Z,Lb709                 ; 38E8 2808     (L   Yes, go here

        CP      $03                     ; 38EA FE03     .S   Is value = 3?
        JR      Z,Lb710                 ; 38EC 2808     (L   Yes, go here

        CALL    Lb711                   ; 38EE CD143B   .@z

        RET                             ; 38F1 C9       .    End

Lb709:  CALL    Lb712                   ; 38F2 CDAA39   .Ui
        RET                             ; 38F5 C9       .

Lb710:  CALL    Lb713                   ; 38F6 CDCD3A   ../
        RET                             ; 38F9 C9       .

Lb708:  CALL    DRAW_BALLOON            ; 38FA CDFE38   ..9  Draw the balloon
        RET                             ; 38FD C9       .

;=============================================================================
; Draws the balloon
;
; The balloon starts at the top of the screen.  It has three sections -- the
; bottom, middle, and top.  The first part showing is the bottom.  GP_82B1
; contains the state of what we should be working on with the balloon:
;
; GP_82B1:  0 - Initialize the balloon values
;           1 - Work on the balloon middle
;           2 - Work on the balloon top
;           All other values - Initialze the balloon values
;=============================================================================
DRAW_BALLOON:
        LD      A,$01                   ; 38FE 3E01     >.	 Keep processing the balloon
        LD      (KEEP_SAME_ISR_FLAG),A  ; 3900 324480   2..  Keep processing the same ISR table location

        LD      A,(GP_82B1)             ; 3903 3AB182   :.}  Get balloon progress value
        AND     A                       ; 3906 A7       .    Is value zero?
        JR      Z,INIT_BALLOON          ; 3907 2807     (F   Yes, initialize balloon big sprite

        DEC     A                       ; 3909 3D       =    Decrement value
        JR      Z,BALLOON_MIDDLE        ; 390A 283A     (n   Is value zero?  Yes, work on middle of balloon

        DEC     A                       ; 390C 3D       =    Decrement value
        JP      Z,BALLOON_TOP           ; 390D CA6139   . i  Is value zero?  Yes, work on top of balloon

; Initialize and draw top
INIT_BALLOON:
        LD      BC,$201                 ; 3910 010102   ..G	 Play Balloon Music 
        CALL    LOAD_SOUND_DATA         ; 3913 CDBB11   ..A

        LD      (IY+$00),$01            ; 3916 FD360001 .6D. Sprite has priority
        LD      (IY+$01),$01            ; 391A FD360101 .6.. Color 1, no inversion
        LD      (IY+$02),$F0            ; 391E FD3602F0 .6G. Y position starts at 240 (top of screen)

        LD      A,(RANDOM_NUMBER)       ; 3922 3A2281   :&.  Get random number
        AND     $3F                     ; 3925 E63F     ..   Mask of bits 5 - 0 (Range 0 - 63)
        ADD     A,$40                   ; 3927 C640     .Q   Add 64 to X position
        LD      (IY+$03),A              ; 3929 FD7703   .wS  Set X position

        LD      HL,$C01                 ; 392C 21010C   !.\  Set timer for how long the balloon stays
        LD      (HELO_BALLOON_TIMER),HL ; 392F 22B582   ".}

;------------------------------
; Draw balloon bottom (string)
        LD      IX,$88E6                ; 3932 DD21E688 .!.w Destination
        LD      HL,BALLOON_BOTTOM_DATA  ; 3936 21903F   !..  Source - Balloon bottom
        CALL    COPY_BIGSPRITE_2X2      ; 3939 CD4F35   .Jq  Copy 2x2 big sprite

        INC     IX                      ; 393C DD23     .#
        INC     IX                      ; 393E DD23     .#   Destination
        INC     HL                      ; 3940 23       #    Source - Go to next data location
        CALL    COPY_BIGSPRITE_2X2      ; 3941 CD4F35   .Jq  Copy 2x2 big sprite
        JR      Lb718                   ; 3944 183F     ..   Done drawing bottom, continue

; Draw middle
BALLOON_MIDDLE:
        LD      A,(IY+$02)              ; 3946 FD7E02   .~G  Get Y position
        CP      $E6                     ; 3949 FEE6     ..   Is value = 230?
        JR      NZ,Lb719                ; 394B 303F     0.   Nope, continue

;---------------------
; Draw balloon middle
        LD      IX,$88C6                ; 394D DD21C688 .!.. Destination
        LD      HL,BALLOON_MIDDLE_DATA  ; 3951 21923F   !..  Source - Balloon middle
        CALL    COPY_BIGSPRITE_2X2      ; 3954 CD4F35   .Jp  Copy 2x2 big sprite

        INC     IX                      ; 3957 DD23     .#
        INC     IX                      ; 3959 DD23     .#   Destination
        INC     HL                      ; 395B 23       #    Source - Go to next data location
        CALL    COPY_BIGSPRITE_2X2      ; 395C CD4F35   .Jp  Copy 2x2 big sprite

        JR      Lb718                   ; 395F 1824     .t

; Draw top
BALLOON_TOP:
        LD      A,(IY+$02)              ; 3961 FD7E02   .~.  Get Y position
        CP      $D6                     ; 3964 FED6     ..   Is value = 214?
        JR      NZ,Lb719                ; 3966 3024     05   Nope, continue

;------------------
; Draw balloon top
        LD      IX,$88A6                ; 3968 DD21A688 .!.w Destination
        LD      HL,BALLOON_TOP_DATA     ; 396C 21943F   !k.  Source - Balloon top
        CALL    COPY_BIGSPRITE_2X2      ; 396F CD4F35   .Jq  Copy 2x2 big sprite

        INC     IX                      ; 3972 DD23     .#
        INC     IX                      ; 3974 DD23     .#   Destination
        INC     HL                      ; 3976 23       #    Source - Go to next data location
        CALL    COPY_BIGSPRITE_2X2      ; 3977 CD4F35   .Jq  Copy 2x2 big sprite

        LD      A,$02                   ; 397A 3E02     >.
        LD      ($82B8),A               ; 397C 32B882   2..  Go to next item, we are "done" with the balloon
        XOR     A                       ; 397F AF       .
        LD      (GP_82B1),A             ; 3980 32B182   2..  Clear the general purpose flag
        JR      Lb720                   ; 3983 1818     ..

Lb718:  LD      A,(GP_82B1)             ; 3985 3AB182   :.}  Increment "progress" of balloon
        INC     A                       ; 3988 3C       <
        LD      (GP_82B1),A             ; 3989 32B182   2.}

Lb719:  LD      B,$02                   ; 398C 0602     ..	Amount to move the bigsprite in X direction
        CALL    MOVE_BIGSPRITE_X        ; 398E CD913A   ../

        LD      B,$01                   ; 3991 0601     ..
        CALL    Lb722                   ; 3993 CD4B3A   ..n

        LD      (IY+$00),$00            ; 3996 FD360000 .6DD  Set priority to zero
        JP      Lb723                   ; 399A C3A539   ..i

Lb720:  LD      (IY+$00),$01            ; 399D FD360001 .6D.  Set priority to one
        NOP                             ; 39A1 00       .
        NOP                             ; 39A2 00       .
        NOP                             ; 39A3 00       .
        NOP                             ; 39A4 00       .

Lb723:  XOR     A                       ; 39A5 AF       .	 We are done with the balloon
        LD      (KEEP_SAME_ISR_FLAG),A  ; 39A6 324480   2..  Process the next ISR table location
        RET                             ; 39A9 C9       .    End DRAW_BALLOON


;=============================================================================
; Handle Balloon?
;=============================================================================
Lb712:  LD      A,(FLOOR_GROUP_IDX)     ; 39AA 3ADC80   :.. Get the current building floor group
        AND     $03                     ; 39AD E603     ..
        CP      $02                     ; 39AF FE02     .G
        JR      NZ,Lb724                ; 39B1 300B     0.

; Update and check the balloon timer
        LD      HL,(HELO_BALLOON_TIMER) ; 39B3 2AB582   *.}
        DEC     HL                      ; 39B6 2B       +
        LD      (HELO_BALLOON_TIMER),HL ; 39B7 22B582   ".}
        LD      A,L                     ; 39BA 7D       }
        OR      H                       ; 39BB B4       .
        JR      NZ,Lb725                ; 39BC 2008      L	Is the timer zero? No, go here

Lb724:  LD      A,$04                   ; 39BE 3E04     >.	The balloon timed out
        LD      ($82B8),A               ; 39C0 32B882   2..
        JP      Lb726                   ; 39C3 C3463A   ..n

Lb725:  LD      B,(IY+$02)              ; 39C6 FD4602   .FG
        CALL    CHECK_FIELD_INVERSION   ; 39C9 CD8311   ..A Check to see if field is inverted
        AND     A                       ; 39CC A7       .
        JR      NZ,Lb727                ; 39CD 2009      .  Normal field, go here

; Inverted field
        LD      D,$00                   ; 39CF 1600     .D
        LD      A,(IY+$03)              ; 39D1 FD7E03   .~S
        ADD     A,$38                   ; 39D4 C638     .(
        JR      Lb728                   ; 39D6 1809     ..

; Normal field
Lb727:  LD      D,$01                   ; 39D8 1601     ..
        LD      A,(IY+$03)              ; 39DA FD7E03   .~.
        NEG                             ; 39DD ED44     .D
        SUB     $3A                     ; 39DF D63A     ./

Lb728:  LD      C,A                     ; 39E1 4F       O
        LD      A,$01                   ; 39E2 3E01     >.
        CALL    Lb255                   ; 39E4 CD2103   .0.
        CALL    Lb526                   ; 39E7 CDC032   ..f
        AND     A                       ; 39EA A7       .
        JR      Z,Lb729                 ; 39EB 2846     (.

        BIT     7,A                     ; 39ED CB7F     ..
        JR      NZ,Lb730                ; 39EF 2012      .

        LD      A,(CLIMBER_RARM_CTRL)   ; 39F1 3A3E81   :{.  Get climber right arm sprite code
        AND     $0F                     ; 39F4 E60F     ..
        CP      $05                     ; 39F6 FE05     .U
        LD      A,($8141)               ; 39F8 3A4181   :E.  Climber right arm sprite X position
        JR      NZ,Lb731                ; 39FB 3002     0G   Is value != 0?  Yes, go here

        ADD     A,$08                   ; 39FD C608     .L   Add 8 to Y value

Lb731:  ADD     A,$04                   ; 39FF C604     .T   Add 4 to Y value
        JR      Lb732                   ; 3A01 1810     ..

Lb730:  LD      A,(CLIMBER_LARM_CTRL)   ; 3A03 3A3A81   :/.  Get climber left arm sprite code
        AND     $0F                     ; 3A06 E60F     ..
        CP      $05                     ; 3A08 FE05     .U
        LD      A,($813D)               ; 3A0A 3A3D81   :y.  Climber left arm sprite X position
        JR      C,Lb733                 ; 3A0D 3802     8G

        ADD     A,$08                   ; 3A0F C608     .L

Lb733:  ADD     A,$04                   ; 3A11 C604     .T

Lb732:  DEC     D                       ; 3A13 15       .
        JR      Z,Lb734                 ; 3A14 2804     (.
        SUB     $38                     ; 3A16 D638     .(
        JR      Lb735                   ; 3A18 1804     ..

Lb734:  NEG                             ; 3A1A ED44     .D
        SUB     $3A                     ; 3A1C D63A     .n

Lb735:  LD      (IY+$03),A              ; 3A1E FD7703   .w.

        LD      BC,$408                 ; 3A21 010804   .L.	Play Caught Balloon Music
        CALL    LOAD_SOUND_DATA         ; 3A24 CDBB11   ..A

        LD      A,$03                   ; 3A27 3E03     >.
        LD      ($82B8),A               ; 3A29 32B882   2.}
        LD      A,$80                   ; 3A2C 3E80     >.
        LD      (GP_82B1),A             ; 3A2E 32B182   2..
        JR      Lb726                   ; 3A31 1813     .R

Lb729:  LD      A,$01                   ; 3A33 3E01     >.
        CALL    Lb223                   ; 3A35 CD6503   .uS
        LD      B,$01                   ; 3A38 0601     ..
        CALL    Lb722                   ; 3A3A CD4B3A   .^/
        LD      B,$01                   ; 3A3D 0601     ..	Amount to move the bigsprite in X direction
        CALL    MOVE_BIGSPRITE_X        ; 3A3F CD913A   ..n
        CALL    CHECK_DUMBELLS          ; 3A42 CD8B33   .tr	Check dumbells/girders
        RET                             ; 3A45 C9       .

Lb726:  XOR     A                       ; 3A46 AF       .
        LD      (BIG_SPRITE_CTRL),A     ; 3A47 32DC98   2..  Clear the big sprite number (priority?)
        RET                             ; 3A4A C9       .


;=============================================================================
;=============================================================================
Lb722:  LD      A,(HELO_BALLOON_TIMER)  ; 3A4B 3AB582   :.}
        BIT     0,A                     ; 3A4E CB47     .G	Is the helicopter/balloon timer bit 0 = 0?
        RET     Z                       ; 3A50 C8       .	Yes, go here

        LD      A,(GP_82AF)             ; 3A51 3AAF82   :P}  Get counter
        BIT     0,A                     ; 3A54 CB47     .G   Is value odd?
        JR      NZ,Lb736                ; 3A56 2014      @   Yes, go here

        LD      A,(HELO_BALLOON_TIMER)  ; 3A58 3AB582   :..
        BIT     6,A                     ; 3A5B CB77     .w	Is the helicopter/balloon timer bit 6 != 0?
        JR      NZ,Lb737                ; 3A5D 201A      .	Yes, go here

        LD      A,(IY+$02)              ; 3A5F FD7E02   .~.
        SUB     B                       ; 3A62 90       .
        LD      (IY+$02),A              ; 3A63 FD7702   .w.
        CP      $6E                     ; 3A66 FE6E     .z
        JR      C,Lb737                 ; 3A68 380F     8.

        JR      Lb738                   ; 3A6A 1814     .@

Lb736:  LD      A,(IY+$02)              ; 3A6C FD7E02   .~G
        CP      $90                     ; 3A6F FE90     ..
        JR      NZ,Lb737                ; 3A71 3006     0.

        ADD     A,B                     ; 3A73 80       .
        LD      (IY+$02),A              ; 3A74 FD7702   .wG
        JR      Lb738                   ; 3A77 1807     .F

Lb737:  LD      A,(GP_82AF)             ; 3A79 3AAF82   :P}  Increment counter
        INC     A                       ; 3A7C 3C       <
        LD      (GP_82AF),A             ; 3A7D 32AF82   2P}

Lb738:  LD      A,(IY+$02)              ; 3A80 FD7E02   .~G
        CP      $80                     ; 3A83 FE80     ..
        JR      NZ,Lb739                ; 3A85 3005     0.

        LD      (IY+$00),$00            ; 3A87 FD360000 .6DD
        RET                             ; 3A8B C9       .

Lb739:  LD      (IY+$00),$01            ; 3A8C FD360001 .6D.
        RET                             ; 3A90 C9       .

;=============================================================================
; MOVE_BIGSPRITE_X
; Moves the bigsprite in the X direction. The direction is either left or 
; right and depends on the BIGSPRITE_DIRECTION flag (0, move right, != 0, move
; left). When the limits are reached, the direction is toggled.  Here are the
; limits:
;
; Moving left - if the final position >= $F0, the direction is reversed
;
; Moving right - if the final position >= $80 ($A0 for an inverted field), the
;                direction is reversed
; 
; Input:
;	IY points to the bigsprite control 
;	B = amount to move the bigsprite
;=============================================================================
MOVE_BIGSPRITE_X:
        LD      A,(HELO_BALLOON_TIMER)  ; 3A91 3AB582   :.}	
        BIT     0,A                     ; 3A94 CB47     .G	Is the helicopter/balloon timer bit 0 != 0?
        RET     NZ                      ; 3A96 C0       .	Yes, return

        LD      A,(BIGSPRITE_DIRECTION) ; 3A97 3AAE82   :.}	Check direction flag
        AND     A                       ; 3A9A A7       .	Is BIGSPRITE_DIRECTION != 0
        JR      NZ,Lb740                ; 3A9B 2020      d	Yes, go here (move left)

; Move bigsprite right B positions
        LD      A,(IY+$03)              ; 3A9D FD7E03   .~S	Update X position
        ADD     A,B                     ; 3AA0 80       .	X = X + B
        LD      (IY+$03),A              ; 3AA1 FD7703   .wS

        CALL    CHECK_FIELD_INVERSION   ; 3AA4 CD8311   .|A Check to see if field is inverted
        AND     A                       ; 3AA7 A7       .   
        JR      NZ,Lb741                ; 3AA8 2004      .  Normal field, go here

; Inverted field
        LD      C,$A0                   ; 3AAA 0EA0     ._	C = $A0 for an inverted field
        JR      Lb742                   ; 3AAC 1802     ..

; Normal field
Lb741:  LD      C,$80                   ; 3AAE 0E80     ..	C = $80 for a normal field

; Check bigsprite X position
Lb742:  LD      A,(IY+$03)              ; 3AB0 FD7E03   .~.	Get X position
        CP      C                       ; 3AB3 B9       .	Is X < C ($A0 inverted, $80 regular field)
        JR      C,Lb743                 ; 3AB4 3816     8.	Yes, go here

; Change direction (right to left)
        LD      A,$01                   ; 3AB6 3E01     >.	
        LD      (BIGSPRITE_DIRECTION),A ; 3AB8 32AE82   2..	We are now moving left
        JR      Lb743                   ; 3ABB 180F     .N

; Move bigsprite left
Lb740:  LD      A,(IY+$03)              ; 3ABD FD7E03   .~S	Update X position
        SUB     B                       ; 3AC0 90       .	X = X - B
        LD      (IY+$03),A              ; 3AC1 FD7703   .wS

; Check for overflow (wraparound)
        CP      $F0                     ; 3AC4 FEF0     ..	Is position < $F0 moving left?
        JR      C,Lb743                 ; 3AC6 3804     8.	Yes, go here

; Change direction (left to right)
        XOR     A                       ; 3AC8 AF       .
        LD      (BIGSPRITE_DIRECTION),A ; 3AC9 32AE82   2.}	We are now moving right

Lb743:  RET                             ; 3ACC C9       .	End MOVE_BIGSPRITE_X


;=============================================================================
;=============================================================================
Lb713:  CALL    SHOW_CLIMBER            ; 3ACD CD4415   .@Q  Show climber on screen
        LD      A,(GP_82B1)             ; 3AD0 3AB182   :..
        AND     A                       ; 3AD3 A7       .
        JR      NZ,Lb744                ; 3AD4 2024      5

        CALL    CHECK_ALLOWED_HAND_MOVES ; 3AD6 CD771A   .#.
        LD      A,(LHAND_MOVEMENT_FLAG) ; 3AD9 3A4681   :..  Get left hand movement allowed flag
        LD      B,A                     ; 3ADC 47       G
        LD      A,(RHAND_MOVEMENT_FLAG) ; 3ADD 3A4781   :B.  Get right hand movement allowed flag
        ADD     A,B                     ; 3AE0 80       .
        JR      Z,Lb745                 ; 3AE1 2829     (<   Allowed to move either hand? Nope, go here

        XOR     A                       ; 3AE3 AF       .
        LD      ($8281),A               ; 3AE4 328182   2..
        LD      ($8282),A               ; 3AE7 328282   2.}
        LD      A,$04                   ; 3AEA 3E04     >.
        LD      ($82B8),A               ; 3AEC 32B882   2..
        LD      A,$80                   ; 3AEF 3E80     >.
        LD      (PLAYFIELD),A           ; 3AF1 328181   2..	Change the playfield location
        LD      A,$01                   ; 3AF4 3E01     >.
        CALL    Lb223                   ; 3AF6 CD6503   .p.
        RET                             ; 3AF9 C9       .

Lb744:  LD      A,($814C)               ; 3AFA 3A4C81   :..
        AND     A                       ; 3AFD A7       .
        JR      NZ,Lb745                ; 3AFE 200C      .

        LD      A,$FF                   ; 3B00 3EFF     >.
        LD      ($814C),A               ; 3B02 324C81   2..

        LD      A,(GP_82B1)             ; 3B05 3AB182   :.}
        DEC     A                       ; 3B08 3D       =
        LD      (GP_82B1),A             ; 3B09 32B182   2.}

Lb745:  LD      A,$04                   ; 3B0C 3E04     >.
        CALL    DELAY                   ; 3B0E CDB802   ..G Delay

        JP      Lb713                   ; 3B11 C3CD3A   .2n

;=============================================================================
;=============================================================================
Lb711:  LD      A,(IY+$02)              ; 3B14 FD7E02   .~G
        ADD     A,$02                   ; 3B17 C602     .G
        LD      (IY+$02),A              ; 3B19 FD7702   .w.
        LD      A,(GP_82B1)             ; 3B1C 3AB182   :..
        CP      $00                     ; 3B1F FE00     .D
        LD      A,(IY+$02)              ; 3B21 FD7E02   .~.
        JR      NZ,Lb746                ; 3B24 2015      Q

        CP      $D8                     ; 3B26 FED8     ..
        JR      C,Lb747                 ; 3B28 382E     8o

; Clear 16 bytes of bigsprite RAM at offset $A0
        LD      A,$A0                   ; 3B2A 3EA0     >_
        CALL    CLR_16_BSPRITE_RAM      ; 3B2C CD1E3F   ...

; Clear 16 bytes of bigsprite RAM at offset $B0
        LD      A,$B0                   ; 3B2F 3EB0     >.
        CALL    CLR_16_BSPRITE_RAM      ; 3B31 CD1E3F   .[.

        LD      A,$01                   ; 3B34 3E01     >.
        LD      (GP_82B1),A             ; 3B36 32B182   2..
        JR      Lb747                   ; 3B39 181D     .X

Lb746:  CP      $EC                     ; 3B3B FEEC     ..
        JR      C,Lb747                 ; 3B3D 3819     8I

        LD      (IY+$02),$F0            ; 3B3F FD3602F0 .6..
        LD      A,$FF                   ; 3B43 3EFF     >.
        LD      ($82B8),A               ; 3B45 32B882   2.}
        XOR     A                       ; 3B48 AF       .
        LD      (GP_82AF),A             ; 3B49 32AF82   2P}  Clear counter

; Clear 16 bytes of bigsprite RAM at offset $C0
        LD      A,$C0                   ; 3B4C 3EC0     >.
        CALL    CLR_16_BSPRITE_RAM      ; 3B4E CD1E3F   ...

; Clear 16 bytes of bigsprite RAM at offset $D0
        LD      A,$D0                   ; 3B51 3ED0     >.
        CALL    CLR_16_BSPRITE_RAM      ; 3B53 CD1E3F   .[.

        JR      Lb748                   ; 3B56 180D     .]

Lb747:  LD      B,$02                   ; 3B58 0602     ..	Amount to move the bigsprite in X direction
        CALL    MOVE_BIGSPRITE_X        ; 3B5A CD913A   ../

        LD      A,(HELO_BALLOON_TIMER)  ; 3B5D 3AB582   :.}	Toggle bit 0 of the helicopter/balloon timer
        XOR     $01                     ; 3B60 EE01     ..
        LD      (HELO_BALLOON_TIMER),A  ; 3B62 32B582   2..

Lb748:  RET                             ; 3B65 C9       .


;-------------------------------------------------------------------------------
; Handles the electrified sign with sparking cables
;-------------------------------------------------------------------------------
ISR_JUMP3_ELECTRIC_SIGN:
        LD      A,($82B8)               ; 3B66 3AB882   :..
        CP      $01                     ; 3B69 FE01     ..	Is $82B8 != 1?
        JR      NZ,Lb749                ; 3B6B 2004      T	Yes, service the electric sign

        CALL    INIT_ELECTRIC_SIGN      ; 3B6D CD753B   .5:	$82B8 = 1, intitialize the electric sign
        RET                             ; 3B70 C9       .	End ISR_JUMP3_ELECTRIC_SIGN

Lb749:  CALL    SERVICE_ELECTRIC_SIGN   ; 3B71 CD653C   .uh	Service the electric sign
        RET                             ; 3B74 C9       .	End ISR_JUMP3_ELECTRIC_SIGN


;-------------------------------------------------------------------------------
; Initializes the electrified Nichibutsu sign
; It sets up the bigsprite used to display the sign. It also starts playing
; the electric sign music and initializes the sparking electric cables.
; Once everything is initialized, $82B8 is set to 2.
;-------------------------------------------------------------------------------
INIT_ELECTRIC_SIGN:
        LD      IY,BIG_SPRITE_CTRL      ; 3B75 FD21DC98 .!.. Point to big sprite control
        LD      A,(FLOOR_GROUP_IDX)     ; 3B79 3ADC80   :..  Get the current building floor group
        AND     $03                     ; 3B7C E603     .S   Mask off bits 0 and 1
        CP      $01                     ; 3B7E FE01     ..   Is value = 1?
        RET     NZ                      ; 3B80 C0       .    Nope, end INIT_ELECTRIC_SIGN

        LD      BC,$202                 ; 3B81 010202   .G.  Play Electric sign music
        CALL    LOAD_SOUND_DATA         ; 3B84 CDBB11   ..A

        LD      A,$01                   ; 3B87 3E01     >.
        LD      (KEEP_SAME_ISR_FLAG),A  ; 3B89 324480   2@.  Keep processing the same ISR table location
        LD      (GP_TIMING),A           ; 3B8C 32B082   2..  
        LD      (IY+$00),$01            ; 3B8F FD360001 .6D. Bigsprite priority? set to 1

        CALL    CHECK_FIELD_INVERSION   ; 3B93 CD8311   ..A  Check to see if field is inverted
        AND     A                       ; 3B96 A7       .
        LD      (IY+$01),$05            ; 3B97 FD360105 .6.. Bigsprite color
        JR      NZ,Lb752                ; 3B9B 2004      T   Normal field, go here

; Inverted field
        LD      (IY+$01),$15            ; 3B9D FD360115 .6.P Bigsprite color 5, invert X axis

; Normal field
Lb752:  LD      (IY+$02),$F0            ; 3BA1 FD3602F0 .6.. Y position is top of the screen
        LD      A,(BUILDING_NUMBER)     ; 3BA5 3ADF80   :..
        AND     $03                     ; 3BA8 E603     .S
        LD      E,A                     ; 3BAA 5F       _
        LD      D,$00                   ; 3BAB 1600     .D	DE = BUILDING_NUMBER & $03

        CALL    CHECK_FIELD_INVERSION   ; 3BAD CD8311   ..A  Check to see if field is inverted
        AND     A                       ; 3BB0 A7       .
        JR      NZ,Lb753                ; 3BB1 2007      F   Normal field, go here

; Inverted field
        LD      HL,ELECTRIC_CABLE_DATA  ; 3BB3 21B23F   !..	Electric sign cable data?
        LD      C,$02                   ; 3BB6 0E02     ..
        JR      Lb754                   ; 3BB8 1805     .U

; Normal field
Lb753:  LD      HL,ELECTRIC_SIGN_X_POS  ; 3BBA 21B63F   !..	Table for X position based on building number
        LD      C,$01                   ; 3BBD 0E01     ..	Used in INIT_ELEC_CABLES

Lb754:  ADD     HL,DE                   ; 3BBF 19       .	HL = ELECTRIC_SIGN_X_POS + (BUILDING_NUMBER & $03)
        LD      A,(HL)                  ; 3BC0 7E       ~	Get X position based on building #
        LD      (IY+$03),A              ; 3BC1 FD7703   .wS
        LD      IX,$88E4                ; 3BC4 DD21E488 .!.w Destination
        LD      HL,ELECTRIC_SIGN_DATA   ; 3BC8 21AE3F   !..  Source - Electric Sign big sprite data
        LD      B,$04                   ; 3BCB 0604     .T   4 2x2 big sprites

Lb755:  CALL    COPY_BIGSPRITE_2X2      ; 3BCD CD4F35   .Jq  Copy 2x2 big sprite
        INC     HL                      ; 3BD0 23       #    Go to next data byte
        INC     IX                      ; 3BD1 DD23     .#   Advance two columns
        INC     IX                      ; 3BD3 DD23     .#   
        DEC     B                       ; 3BD5 05       .    Decrement counter
        JR      NZ,Lb755                ; 3BD6 20F5      .   Done? Nope, continue looping

        LD      HL,INIT_ELEC_CABLES_DATA ; 3BD8 21BA3F   !..
        ADD     HL,DE                   ; 3BDB 19       .	HL = INIT_ELEC_CABLES_DATA + (BUILDING_NUMBER & $03)
        LD      B,(HL)                  ; 3BDC 46       F	B = table value
        CALL    INIT_ELEC_CABLES        ; 3BDD CDEA3B   ..:	Initialize the electric cables?

        LD      A,$02                   ; 3BE0 3E02     >.	$82B8 = $02
        LD      ($82B8),A               ; 3BE2 32B882   2..
        XOR     A                       ; 3BE5 AF       .	We are done setting up the electric sign
        LD      (KEEP_SAME_ISR_FLAG),A  ; 3BE6 324480   2.. Process the next ISR table location
        RET                             ; 3BE9 C9       .   End INIT_ELECTRIC_SIGN


;=============================================================================
; Initializes the electric cables for the electric sign?
;
; Input:
;	B = (INIT_ELEC_CABLES_DATA + BUILDING_NUMBER & $03), which is always $80 
;	C = $01
;=============================================================================
INIT_ELEC_CABLES:
        LD      IX,UNKNOWN_815C         ; 3BEA DD215C81 .!..
        LD      IY,UNKNOWN_8283         ; 3BEE FD218382 .!.}

Lb761:  LD      (IX+$00),$01            ; 3BF2 DD360001 .6D.
        LD      (IX+$01),$18            ; 3BF6 DD360118 .6..
        LD      (IX+$02),$02            ; 3BFA DD360202 .6G.
        LD      (IX+$03),$F0            ; 3BFE DD3603F0 .6..
        LD      (IX+$06),$03            ; 3C02 DD360603 .6.S
        LD      (IY+$07),$04            ; 3C06 FD360704 .6F.
        LD      A,B                     ; 3C0A 78       x
        AND     $01                     ; 3C0B E601     ..	Isolate bit 0
        LD      (IY+$00),A              ; 3C0D FD7700   .wD
        BIT     0,C                     ; 3C10 CB41     .A	Is bit 0 of C = 0?
        LD      A,($98DF)               ; 3C12 3ADF98   :..	A = Bigsprite X (electric sign)
        JR      Z,Lb757                 ; 3C15 2816     (S	Yes, go here

        NEG                             ; 3C17 ED44     .D	A = -X Position
        BIT     0,B                     ; 3C19 CB40     .@	Is bit 0 of B = 0?
        JR      Z,Lb758                 ; 3C1B 280C     (\	Yes, go here

        SUB     $19                     ; 3C1D D619     .I	 A = -X - $19
        LD      (IX+$01),$58            ; 3C1F DD360158 .6.M 
        LD      (IX+$07),$0C            ; 3C23 DD36070C .6.\
        JR      Lb759                   ; 3C27 1816     .S

Lb758:  SUB     $69                     ; 3C29 D669     .(	 A = -X - $69
        JR      Lb759                   ; 3C2B 1812     ..	

Lb757:  BIT     0,B                     ; 3C2D CB40     .@	Is bit 0 of B != 0?
        JR      NZ,Lb760                ; 3C2F 2004      T	Yes, go here

        ADD     A,$09                   ; 3C31 C609     ..	A = A + 9
        JR      Lb759                   ; 3C33 180A     .O

Lb760:  ADD     A,$59                   ; 3C35 C659     ..	 Add $59 to the sign X position
        LD      (IX+$01),$58            ; 3C37 DD360158 .6.M
        LD      (IX+$07),$0C            ; 3C3B DD36070C .6.\

Lb759:  LD      (IX+$04),A              ; 3C3F DD7704   .w.	 Save the sign X position and offset
        LD      (IX+$08),$01            ; 3C42 DD360801 .6L.
        LD      (IX+$09),$1D            ; 3C46 DD36091D .6.Y
        LD      (IX+$0A),$03            ; 3C4A DD360A03 .6OS
        LD      (IX+$0B),$F0            ; 3C4E DD360BF0 .6..
        LD      (IY+$0F),$04            ; 3C52 FD360F04 .6N.
        BIT     7,B                     ; 3C56 CB78     .x	 Is bit 7 of B = 0?
        RET     Z                       ; 3C58 C8       .	 Yes, End INIT_ELEC_CABLES

        LD      B,$01                   ; 3C59 0601     ..	 This will exit next loop
        LD      DE,$10                  ; 3C5B 111000   ..D	 Add 16 to each pointer
        ADD     IX,DE                   ; 3C5E DD19     ..	 IX += $10
        ADD     IY,DE                   ; 3C60 FD19     ..	 IY += $10
        JP      Lb761                   ; 3C62 C3F23B   ..z	 Loop back through


;=============================================================================
; Changes the electric sign color once the General purpose timing (GP_TIMING)
; value counts down to zero.  Once it is zero:
;	GP_TIMING is set back to 2
;	The sign color counts up from 4 to 7, then back to 4 again.
;
; $82B9 is checked. If it is != $0C, the climber color is not set to default.
; If the sign Y value is != $20, the climber color is not set to default.
;
; When the climber color is set to default, $82B9 is also set to $80.
;
; If the sign Y position < $6
;	The sign will stop being displayed
;	$82B8 is set to $FF
;	The routine returns
;
; If the sign Y position < $E4, ??? is called.
;=============================================================================
SERVICE_ELECTRIC_SIGN:
        LD      IY,BIG_SPRITE_CTRL      ; 3C65 FD21DC98 .!.. Point to big sprite control
        LD      A,(GP_TIMING)           ; 3C69 3AB082   :.}
        DEC     A                       ; 3C6C 3D       =    Count down
        LD      (GP_TIMING),A           ; 3C6D 32B082   2.}  
        JR      NZ,Lb762                ; 3C70 201A      N   Not zero? Continue

; Change the electric sign color. Cycle from 4 -> 7, then back to 4 again
        LD      A,$02                   ; 3C72 3E02     >.
        LD      (GP_TIMING),A           ; 3C74 32B082   2..  Set to 2
        LD      A,(IY+$01)              ; 3C77 FD7E01   .~.	 Get the current color
        LD      B,A                     ; 3C7A 47       G	 Save it in B
        AND     $0F                     ; 3C7B E60F     .N	 Keep only the color bits
        INC     A                       ; 3C7D 3C       <	 Go to next color
        CP      $08                     ; 3C7E FE08     .L	 Is the color = 8?
        JR      NZ,Lb763                ; 3C80 2002      .	 No, go here

        LD      A,$04                   ; 3C82 3E04     >.	 Color overflow - go back to 4

Lb763:  LD      C,A                     ; 3C84 4F       O	 C = our new color
        LD      A,B                     ; 3C85 78       x	 Get our last color
        AND     $10                     ; 3C86 E610     ..	 Isolate the X invert bit
        OR      C                       ; 3C88 B1       .	 Combine our new color with the X-invert value
        LD      (IY+$01),A              ; 3C89 FD7701   .w.	 Set the new color

Lb762:  LD      A,($82B9)               ; 3C8C 3AB982   :..	 
        CP      $0C                     ; 3C8F FE0C     .\	 Is $82B9 != $0C?
        JR      NZ,Lb764                ; 3C91 301A     0.	 Yes, skip setting default climber color

        LD      A,(IY+$02)              ; 3C93 FD7E02   .~.	 Get the electric sign Y position
        CP      $20                     ; 3C96 FE20     .d	 Is it != $20?
        JR      NZ,Lb764                ; 3C98 3013     0.	 Yes, skip setting default climber color

        LD      A,$80                   ; 3C9A 3E80     >.	 $82B9 = $80
        LD      ($82B9),A               ; 3C9C 32B982   2..

; Set climber color to default (not "shocked")
        LD      A,$06                   ; 3C9F 3E06     >.
        LD      ($8133),A               ; 3CA1 323381   2r.  Climbers left leg color/character set
        LD      ($8137),A               ; 3CA4 323781   2w.  Climbers right leg color/character set
        LD      ($813B),A               ; 3CA7 323B81   2z.  Climbers left arm color/character set
        LD      ($813F),A               ; 3CAA 323F81   2..  Climbers right arm color/character set

Lb764:  LD      A,(IY+$02)              ; 3CAD FD7E02   .~.	 Get the sign Y position
        CP      $06                     ; 3CB0 FE06     .G	 Is the sign Y position < 6?
        JR      C,Lb765                 ; 3CB2 3806     8G	 Yes, we are done with the electric sign

        CP      $E4                     ; 3CB4 FEE4     ..	 Is the Y sign position < $E4?
        CALL    C,Lb766                 ; 3CB6 DCD23C   ..-	 Yes, go here ??? What is this call ???
        RET                             ; 3CB9 C9       .	 End SERVICE_ELECTRIC_SIGN

; Stop displaying the electric sign
Lb765:  LD      (IY+$00),$00            ; 3CBA FD360000 .6DD Set priority? to zero
        LD      (IY+$02),$F0            ; 3CBE FD3602F0 .6G. Set sign Y position to top of the screen
        LD      A,$FF                   ; 3CC2 3EFF     >.	 $82B8 = $FF (shows the electric sign is done)
        LD      ($82B8),A               ; 3CC4 32B882   2..

; Erase the sign bigsprite data
        LD      A,$E0                   ; 3CC7 3EE0     >.	 Clear 16 bytes of bigsprite RAM at $88E0
        CALL    CLR_16_BSPRITE_RAM      ; 3CC9 CD1E3F   .[.
        LD      A,$F0                   ; 3CCC 3EF0     >.	 Clear 16 bytes of bigsprite RAM at $88F0
        CALL    CLR_16_BSPRITE_RAM      ; 3CCE CD1E3F   ...
        RET                             ; 3CD1 C9       .	 End SERVICE_ELECTRIC_SIGN


;=============================================================================
;
; Input:
;
;=============================================================================
Lb766:  LD      IX,UNKNOWN_815C         ; 3CD2 DD215C81 .!..
        LD      IY,UNKNOWN_8283         ; 3CD6 FD218382 .!.}
        LD      B,$02                   ; 3CDA 0602     ..	B = 2 loops

Lb768:  PUSH    BC                      ; 3CDC C5       .	Save B
        LD      A,(IY+$07)              ; 3CDD FD7E07   .~.
        CP      $04                     ; 3CE0 FE04     ..	Is value = $04?
        JR      Z,Lb767                 ; 3CE2 280C     (.	Yes, go here

Lb778:  LD      DE,$10                  ; 3CE4 111000   ..D	Go to next group of values
        ADD     IX,DE                   ; 3CE7 DD19     ..
        ADD     IY,DE                   ; 3CE9 FD19     ..
        POP     BC                      ; 3CEB C1       .	Get B, # of loops
        DEC     B                       ; 3CEC 05       .	Decrement # loops
        JR      NZ,Lb768                ; 3CED 20ED      .	Are we done? No, keep looping

        RET                             ; 3CEF C9       .	End Lb766

Lb767:  LD      A,($82B9)               ; 3CF0 3AB982   :..
        BIT     7,A                     ; 3CF3 CB7F     ..	Is bit 7 of $82B9 != 0?
        JR      NZ,Lb769                ; 3CF5 2025      0	Yes, go here

        LD      A,$01                   ; 3CF7 3E01     >.
        CALL    Lb255                   ; 3CF9 CD2103   .4S	Go here ???

        LD      A,(IX+$0B)              ; 3CFC DD7E0B   .~.	A = $F0
        ADD     A,$08                   ; 3CFF C608     .L	A = $F8
        LD      B,A                     ; 3D01 47       G	B = $F8
        LD      A,(IX+$0C)              ; 3D02 DD7E0C   .~\	A = ?
        ADD     A,$08                   ; 3D05 C608     .L	
        LD      C,A                     ; 3D07 4F       O	C =
        CALL    Lb526                   ; 3D08 CDC032   ..'
        AND     A                       ; 3D0B A7       .	Is A = 0?
        JR      Z,Lb770                 ; 3D0C 2809     (.	Yes, no collision

; The sign shocked the player
        LD      BC,$307                 ; 3D0E 010703   ...	Play electric sign shocking player sound
        CALL    LOAD_SOUND_DATA         ; 3D11 CDBB11   ..A
        CALL    CLIMBER_SHOCKED         ; 3D14 CDB73D   ..x	The climber was shocked (change color)

Lb770:  LD      A,$01                   ; 3D17 3E01     >.	A = 1
        CALL    Lb223                   ; 3D19 CD6503   .uS

Lb769:  DEC     (IX+$06)                ; 3D1C DD3506   .5.	Decrement counter
        JP      NZ,Lb772                ; 3D1F C2933D   ..y	Counter != 0? Yes, go here

; Set a new random loop counter
        LD      A,(RANDOM_NUMBER)        ; 3D22 3A2281   :&.  Get random number
        AND     $07                     ; 3D25 E607     .F	A = RAND % 7
        LD      E,A                     ; 3D27 5F       _	E = random number 0-7
        LD      D,$00                   ; 3D28 1600     .D	D = 0
        LD      HL,Lb766_RND_LOOP_COUNTS ; 3D2A 21BE3F   !..
        ADD     HL,DE                   ; 3D2D 19       .
        LD      A,(HL)                  ; 3D2E 7E       ~	A = table value
        LD      (IX+$06),A              ; 3D2F DD7706   .wG	Save new loop counter

        LD      A,(IX+$07)              ; 3D32 DD7E07   .~F	(IX+$07) += 1
        INC     A                       ; 3D35 3C       <
        AND     $0F                     ; 3D36 E60F     ..	(IX+$07) &= $0F
        LD      (IX+$07),A              ; 3D38 DD7707   .wF
        LD      E,A                     ; 3D3B 5F       _	E = (IX+$07), offset into $3FC6 table below
        CP      $05                     ; 3D3C FE05     .U	(IX+$07) != $05?
        JR      NZ,Lb773                ; 3D3E 200A      .	Yes, go here

        LD      A,(IX+$03)              ; 3D40 DD7E03   .~.	(IX+$03) += $10
        ADD     A,$10                   ; 3D43 C610     ..
        LD      (IX+$03),A              ; 3D45 DD7703   .wS
        JR      Lb774                   ; 3D48 180C     ..

Lb773:  CP      $0C                     ; 3D4A FE0C     ..	Is (IX+$07) != $0C?
        JR      NZ,Lb774                ; 3D4C 2008      L	Yes, go here

        LD      A,(IX+$03)              ; 3D4E DD7E03   .~.	(IX+$07) -= $10
        SUB     $10                     ; 3D51 D610     ..
        LD      (IX+$03),A              ; 3D53 DD7703   .wS

Lb774:  LD      HL,$3FC6                ; 3D56 21C63F   !..
        ADD     HL,DE                   ; 3D59 19       .
        LD      A,(HL)                  ; 3D5A 7E       ~	
        LD      (IX+$01),A              ; 3D5B DD7701   .w.	(IX+$01) = Table Value
        LD      A,E                     ; 3D5E 7B       {
        RLCA                            ; 3D5F 07       .
        LD      E,A                     ; 3D60 5F       _	E = E * 2

        LD      HL,$3FD6                ; 3D61 21D63F   !..
        ADD     HL,DE                   ; 3D64 19       .
        CP      C                       ; 3D65 B9               ; Added
        BIT     0,H                     ; 3D66 CB44     .D
        RLA                             ; 3D68 17       .
        JR      Z,Lb775                 ; 3D69 2817     (.

        SET     4,(IX+$01)              ; 3D6B DDCB10F6 .... Set bit 4 of (IX+$01)
        LD      A,(IX+$04)              ; 3D6F DD7E04   .~.	 
        LD      B,(HL)                  ; 3D72 46       F	 Get $3FD6 table value
        SUB     B                       ; 3D73 90       .
        LD      (IX+$0C),A              ; 3D74 DD770C   .w\	 (IX+$0C) = (IX+$04) - Table Value[0]
        INC     HL                      ; 3D77 23       #
        LD      B,(HL)                  ; 3D78 46       F	 Get next table value
        LD      A,(IX+$03)              ; 3D79 DD7E03   .~S
        ADD     A,B                     ; 3D7C 80       .
        LD      (IX+$0B),A              ; 3D7D DD770B   .w[	 (IX+$0B) = (IX+$03) + Table Value[1]
        JR      Lb772                   ; 3D80 1811     .A

Lb775:  LD      A,(IX+$04)              ; 3D82 DD7E04   .~T
        LD      B,(HL)                  ; 3D85 46       F
        ADD     A,B                     ; 3D86 80       .
        LD      (IX+$0C),A              ; 3D87 DD770C   .w.	 (IX+$0C) = (IX+$04) + Table Value[0]
        INC     HL                      ; 3D8A 23       #
        LD      A,(IX+$03)              ; 3D8B DD7E03   .~S
        LD      B,(HL)                  ; 3D8E 46       F
        ADD     A,B                     ; 3D8F 80       .
        LD      (IX+$0B),A              ; 3D90 DD770B   .w.	 (IX+$0B) = (IX+$03) + Table Value[1]

Lb772:  INC     (IX+$0E)                ; 3D93 DD340E   .4O	 (IX+$0E) += 1
        RL      (IX+$0E)                ; 3D96 DDCB1B56 .... (IX+$0E) Rotate Left
        LD      (IX+$09),$1D            ; 3D9A DD36091D .6.Y (IX+$09) = $1D
        JR      NZ,Lb776                ; 3D9E 200A      .	 Is Value != 0? Yes, go here

; Play sparking sound
        LD      (IX+$09),$1E            ; 3DA0 DD36091E .6.. (IX+$09) = $1E        
		LD      BC,$306                 ; 3DA4 010603   .G.	 Play electric sign sparking sound
        CALL    LOAD_SOUND_DATA         ; 3DA7 CDBB11   ..A

Lb776:  CP      C                       ; 3DAA B9       .      
        BIT     0,H                     ; 3DAB CB44     .D	 Is Bit 0 of H = 0?
        LD      D,D                     ; 3DAD 52       R
        JR      Z,Lb777                 ; 3DAE 2804     (.	 Yes, go here

        SBC     A,H                     ; 3DB0 9C       .      Added
        RR      H                       ; 3DB1 CB1C     ..
        OR      D                       ; 3DB3 B2       .

Lb777:  JP      Lb778                   ; 3DB4 C3E43C   ..-


;------------------------------------------------------------------------------
; The electric sign shocked the player
;
; $8282 = 0
; If $82B9 = $0D
;	$82B9 = $80
;	Loop the climber color from $09 to $01
;	$8282 = $03
; else
;	climber color = $82B9
;	$82B9 += 1
;------------------------------------------------------------------------------
CLIMBER_SHOCKED:
        XOR     A                       ; 3DB7 AF       .
        LD      ($8282),A               ; 3DB8 328282   2}.	Clear $8282
        LD      A,($82B9)               ; 3DBB 3AB982   :.}
        CP      $0D                     ; 3DBE FE0D     .]	Is $82B9 != $0D?
        JR      NZ,Lb779                ; 3DC0 301B     0.	Yes, go here

; Set climber color
        LD      ($8133),A               ; 3DC2 323381   22.  Climbers left leg color/character set
        LD      ($8137),A               ; 3DC5 323781   2&.  Climbers right leg color/character set
        LD      ($813B),A               ; 3DC8 323B81   2:.  Climbers left arm color/character set
        LD      ($813F),A               ; 3DCB 323F81   2..  Climbers right arm color/character set

        INC     A                       ; 3DCE 3C       <	$82B9 += 1 (go to next color)
        LD      ($82B9),A               ; 3DCF 32B982   2.}

        LD      A,$01                   ; 3DD2 3E01     >.
        CALL    Lb223                   ; 3DD4 CD6503   .p.

        LD      A,$03                   ; 3DD7 3E03     >.
        CALL    DELAY                   ; 3DD9 CDB802   ... Delay
        RET                             ; 3DDC C9       .	End CLIMBER_SHOCKED

; Color overflow, change the climber color from $09 to $01 in a loop
Lb779:  LD      C,$09                   ; 3DDD 0E09     ..	New color

; Set climber color in a loop
Lb780:  LD      A,C                     ; 3DDF 79       y
        LD      ($8133),A               ; 3DE0 323381   22. Climbers left leg color/character set
        LD      ($8137),A               ; 3DE3 323781   2&. Climbers right leg color/character set
        LD      ($813B),A               ; 3DE6 323B81   2:. Climbers left arm color/character set
        LD      ($813F),A               ; 3DE9 323F81   2.. Climbers right arm color/character set

        LD      A,$08                   ; 3DEC 3E08     >L
        CALL    DELAY                   ; 3DEE CDB802   ..G Delay

        DEC     C                       ; 3DF1 0D       .	Color -= 1
        JR      NZ,Lb780                ; 3DF2 20EB      .	Is color != 0? Yes, keep looping

        LD      A,$80                   ; 3DF4 3E80     >.
        LD      ($82B9),A               ; 3DF6 32B982   2..	$82B9 = $80
        LD      A,$03                   ; 3DF9 3E03     >.
        LD      ($8282),A               ; 3DFB 328282   2.}	$8282 = 3

        LD      A,$01                   ; 3DFE 3E01     >.
        CALL    Lb223                   ; 3E00 CD6503   .p.
        RET                             ; 3E03 C9       .	End CLIMBER_SHOCKED


;-------------------------------------------------------------------------------
; Handles the falling sign
;-------------------------------------------------------------------------------
ISR_JUMP3_FALLING_SIGN:
        LD      A,($82B8)               ; 3E04 3AB882   :..
        CP      $01                     ; 3E07 FE01     ..
        JR      NZ,Lb781                ; 3E09 2018      .

        LD      A,(FLOOR_GROUP_IDX)     ; 3E0B 3ADC80   :.. Get the current building floor group
        AND     $03                     ; 3E0E E603     .S
        CP      $03                     ; 3E10 FE03     .S
        JR      NZ,Lb782                ; 3E12 2006      G

        LD      A,$FF                   ; 3E14 3EFF     >.
        LD      ($82B8),A               ; 3E16 32B882   2..
        RET                             ; 3E19 C9       .

Lb782:  CALL    UPDATE_FALLING_SIGN     ; 3E1A CD273E   ."{
        LD      A,$02                   ; 3E1D 3E02     >G
        LD      ($82B8),A               ; 3E1F 32B882   2.}
        RET                             ; 3E22 C9       .

Lb781:  CALL    CHECK_SIGN_COLLISION    ; 3E23 CD443E   .@.
        RET                             ; 3E26 C9       .


;-----------------------------------------------------------------------------
; Updates the falling sign by setting a random color and drawing it to big
; sprite RAM
;-----------------------------------------------------------------------------
UPDATE_FALLING_SIGN:  
        LD      IY,BIG_SPRITE_CTRL      ; 3E27 FD21DC98 .!.. Point to big sprite control
        CALL    DRAW_FALLING_SIGN       ; 3E2B CDEB3E   ...  Draw the falling sign

; Set X Position
        LD      A,(RANDOM_NUMBER)       ; 3E2E 3A2281   :&.  Get random number
        AND     $07                     ; 3E31 E607     .F   Set range 0 - 7
        RLCA                            ; 3E33 07       .    Multiply by 16
        RLCA                            ; 3E34 07       .
        RLCA                            ; 3E35 07       .
        RLCA                            ; 3E36 07       .
        LD      (IY+$03),A              ; 3E37 FD7703   .wS  Set the X Position

        LD      A,$08                   ; 3E3A 3E08     >L
        LD      (GP_TIMING),A           ; 3E3C 32B082   2..  Set to 8

        XOR     A                       ; 3E3F AF       .
        LD      ($82B7),A               ; 3E40 32B782   2..
        RET                             ; 3E43 C9       .    End UPDATE_FALLING_SIGN


;-----------------------------------------------------------------------------
; Did the falling sign collide with the climber?
;-----------------------------------------------------------------------------
CHECK_SIGN_COLLISION:
        LD      IY,BIG_SPRITE_CTRL      ; 3E44 FD21DC98 .!.. Point to big sprite control
        LD      B,(IY+$02)              ; 3E48 FD4602   .FG	Get Y position
        LD      A,B                     ; 3E4B 78       x
        CP      $90                     ; 3E4C FE90     ..	Is Y != $90?
        JR      NZ,Lb786                ; 3E4E 3047     0B	Yes, go here

        CP      $40                     ; 3E50 FE40     ..	Is Y < $40?
        JR      C,Lb786                 ; 3E52 3843     8V	Yes, go here

        CALL    CHECK_FIELD_INVERSION   ; 3E54 CD8311   .|A  Check to see if field is inverted
        AND     A                       ; 3E57 A7       .
        JR      Z,Lb787                 ; 3E58 2809     (.   Field is inverted, go here

; Normal field
        LD      A,(IY+$03)              ; 3E5A FD7E03   .~.	Get X position
        NEG                             ; 3E5D ED44     .D
        SUB     $38                     ; 3E5F D638     .9
        JR      Lb788                   ; 3E61 1805     ..

; Inverted field
Lb787:  LD      A,(IY+$03)              ; 3E63 FD7E03   .~S	Get X position
        ADD     A,$40                   ; 3E66 C640     ..

Lb788:  LD      C,A                     ; 3E68 4F       O
        LD      A,($8141)               ; 3E69 3A4181   :.. Climber right arm sprite X position
        CP      C                       ; 3E6C B9       .
        LD      D,$04                   ; 3E6D 1604     .T
        JR      NZ,Lb789                ; 3E6F 3002     0G

        LD      D,$FC                   ; 3E71 16FC     ..

Lb789:  LD      E,$07                   ; 3E73 1E07     .F

Lb790:  LD      A,C                     ; 3E75 79       y
        ADD     A,D                     ; 3E76 82       .
        LD      C,A                     ; 3E77 4F       O
        CALL    Lb526                   ; 3E78 CDC032   ..'
        DEC     E                       ; 3E7B 1D       .
        JR      NZ,Lb790                ; 3E7C 20F7      .

        LD      E,$05                   ; 3E7E 1E05     .U

Lb791:  LD      A,B                     ; 3E80 78       x
        ADD     A,$04                   ; 3E81 C604     .T
        LD      B,A                     ; 3E83 47       G
        CALL    Lb526                   ; 3E84 CDC032   ..'
        DEC     E                       ; 3E87 1D       .
        JR      NZ,Lb791                ; 3E88 20F6      .

        LD      A,($8282)               ; 3E8A 3A8282   :}.
        AND     $0E                     ; 3E8D E60E     ..
        JR      Z,Lb786                 ; 3E8F 2806     (.

        LD      BC,$303                 ; 3E91 010303   ..S	Play Hit by dumbell/girder sound
        CALL    LOAD_SOUND_DATA         ; 3E94 CDBB11   ..A

Lb786:  LD      A,($82B7)               ; 3E97 3AB782   :H}
        RLCA                            ; 3E9A 07       .
        LD      E,A                     ; 3E9B 5F       _
        LD      D,$00                   ; 3E9C 1600     .D
        LD      HL,$3F9E				; 3E9E 219E3F   !..	Dumbell/Girder data?
        ADD     HL,DE                   ; 3EA1 19       .
        LD      A,(HL)                  ; 3EA2 7E       ~
        ADD     A,(IY+$02)              ; 3EA3 FD8602   ...
        LD      (IY+$02),A              ; 3EA6 FD7702   .wG
        CP      $F1                     ; 3EA9 FEF1     ..
        JR      C,Lb792                 ; 3EAB 381C     8.

        CP      $F8                     ; 3EAD FEF8     ..
        JR      NZ,Lb792                ; 3EAF 3018     0.
        XOR     A                       ; 3EB1 AF       .
        LD      (IY+$00),A              ; 3EB2 FD7700   .wD
        LD      A,$01                   ; 3EB5 3E01     >.
        LD      ($82B8),A               ; 3EB7 32B882   2.}
        LD      (IY+$02),$F0            ; 3EBA FD3602F0 .6G.

; Clear 16 bytes of bigsprite RAM at offset $C0
        LD      A,$C0                   ; 3EBE 3EC0     >.

Lb793:  CALL    CLR_16_BSPRITE_RAM      ; 3EC0 CD1E3F   ...
        ADD     A,$10                   ; 3EC3 C610     ..
        JR      NZ,Lb793                ; 3EC5 20F9      .

        JR      Lb794                   ; 3EC7 1821     .4

Lb792:  LD      A,(GP_TIMING)           ; 3EC9 3AB082   :.}  
        DEC     A                       ; 3ECC 3D       =    Count down
        LD      (GP_TIMING),A           ; 3ECD 32B082   2.}  
        JR      NZ,Lb794                ; 3ED0 2018      .   Not zero? Continue

        LD      A,($82B7)               ; 3ED2 3AB782   :..
        INC     A                       ; 3ED5 3C       <
        AND     $07                     ; 3ED6 E607     ..
        LD      ($82B7),A               ; 3ED8 32B782   2..
        CP      $04                     ; 3EDB FE04     .T
        JR      NZ,Lb795                ; 3EDD 2006      .

        LD      BC,$409                 ; 3EDF 010904   ...	Play Falling Sign Sound
        CALL    LOAD_SOUND_DATA         ; 3EE2 CDBB11   ..A

Lb795:  INC     HL                      ; 3EE5 23       #
        LD      A,(HL)                  ; 3EE6 7E       ~
        LD      (GP_TIMING),A           ; 3EE7 32B082   2.}  Save value

Lb794:  RET                             ; 3EEA C9       .	End CHECK_SIGN_COLLISION


;-----------------------------------------------------------------------------
; Draws the falling sign in bigsprite RAM
;-----------------------------------------------------------------------------
DRAW_FALLING_SIGN:
        LD      (IY+$02),$F0            ; 3EEB FD3602F0 .6.. Set Y position
        LD      (IY+$00),$01            ; 3EEF FD360001 .6D. Priority? 1

        CALL    CHECK_FIELD_INVERSION   ; 3EF3 CD8311   ..A Check to see if field is inverted
        AND     A                       ; 3EF6 A7       .
        LD      A,$06                   ; 3EF7 3E06     >.
        JR      NZ,Lb796                ; 3EF9 2002      G

        LD      A,$16                   ; 3EFB 3E16     >S

Lb796:  LD      IX,$88E4                ; 3EFD DD21E488 .!.. Destination
        LD      HL,FALLING_SIGN_DATA    ; 3F01 21963F   !..  Source - Point to table
        LD      BC,$204                 ; 3F04 010402   ..G  B = 2, C = 4

Lb797:  CALL    COPY_BIGSPRITE_2X2      ; 3F07 CD4F35   .Jq  Copy 2x2 big sprite
        INC     HL                      ; 3F0A 23       #    Go to next table location
        INC     IX                      ; 3F0B DD23     .#   Advance 2 columns
        INC     IX                      ; 3F0D DD23     .#   
        DEC     C                       ; 3F0F 0D       .    Decrement counter
        JR      NZ,Lb797                ; 3F10 20F5      .   Done? Nope, keep looping

        DEC     B                       ; 3F12 05       .    Decrement other counter
        JR      Z,Lb798                 ; 3F13 2808     (L   Zero? exit

        LD      IX,$88D4                ; 3F15 DD21D488 .!.. Go up one row
        LD      C,$04                   ; 3F19 0E04     .T   4 values 
        JR      Lb797                   ; 3F1B 18EA     ..   Continue looping

Lb798:  RET                             ; 3F1D C9       .    End DRAW_FALLING_SIGN


;-----------------------------------------------------------------------------
; Clear section of Big sprite RAM (16 bytes).  A
; contains the offset into the bigsprite RAM area
; to clear.  16 bytes are set to $00.
;
; Input:
; A - Offset into bigsprite RAM to clear
;
; Destroys:
; None
;-----------------------------------------------------------------------------
CLR_16_BSPRITE_RAM:  
        PUSH    HL                      ; 3F1E E5       .    Save registers used
        PUSH    AF                      ; 3F1F F5       .    

        LD      HL,BIG_SPRITE_RAM       ; 3F20 210088   !D.  Point HL to the start of Big Sprite RAM
        ADD     A,L                     ; 3F23 85       .    HL = HL + A
        LD      L,A                     ; 3F24 6F       o
        LD      A,$10                   ; 3F25 3E10     >.   Clear 16 bytes

Lb799:  LD      (HL),$00                ; 3F27 3600     6D   Write $00 to location
        INC     L                       ; 3F29 2C       ,    Go to next memory location
        DEC     A                       ; 3F2A 3D       =    Decrement counter
        JR      NZ,Lb799                ; 3F2B 20FA      .   Counter = 0? Nope, keep looping

        POP     AF                      ; 3F2D F1       .    Restore registers used
        POP     HL                      ; 3F2E E1       .
        RET                             ; 3F2F C9       .    End CLR_16_BSPRITE_RAM

;-------------------------------------------------------------------------------
; Data Start
; Range: $3F30 - $3FF7
; Number of bytes: 200
;-------------------------------------------------------------------------------

        .db     $C7, $FB									; Start of dat area

; $3F32 - Dumbell/Girder animation data?
DUMBELL_GIRDER_DATA:
        .db     $00, $01, $00, $01, $0F, $02, $1F, $02
        .db     $00, $03, $1F, $03, $0F, $04, $00, $04
; $3F42
        .db     $50, $80, $C0, $70, $90, $B0, $60, $A0
        .db     $02, $00, $02, $08, $02, $10, $00, $02
; $3F52
        .db     $04, $08, $0C, $0E, $00, $02, $00, $08
        .db     $0C, $08, $00, $04, $00, $0A, $0C, $08
; $3F62
        .db     $28, $29, $2A, $2B, $6A, $69, $01, $02
        .db     $01, $01, $02, $03, $01, $02, $02, $FE
; $3F72
        .db     $08, $FF, $02, $02, $08, $FF, $01, $00
        .db     $08, $FF, $01, $00, $08, $FF, $01, $00
; $3F82
        .db     $02, $01, $01, $00, $02, $01, $02, $FE
        .db     $02, $01, $02, $02, $02, $01

;------------------------
; $3F90 - Balloon Data
BALLOON_BOTTOM_DATA:
		.db     $88, $A8								; Balloon string (bottom)
; $3F92
BALLOON_MIDDLE_DATA:
        .db     $84, $A4								; Balloon middle
; $3F94
BALLOON_TOP_DATA:
		.db     $80, $A0								; Balloon top
;------------------------


; $3F96 - Falling crazy climber sign
FALLING_SIGN_DATA:
		.db     $9C, $BC, $DC, $FC						; Bottom of sign
        .db     $9A, $BA, $DA, $FA						; Top of sign

; Dumbell / Girder?
; $3F9E
		.db     $FF, $03, $FE, $05, $FD, $07, $FC, $01
		.db     $03, $02, $02, $02, $01, $02, $00, $04
		
; $3FAE - Electric Sign
ELECTRIC_SIGN_DATA:
		.db     $96, $B6, $D6, $F6

; $3FB2 - Electric Sign animated electric cables?
ELECTRIC_CABLE_DATA:
        .db     $67, $67, $67, $67

; $3FB6 - The position of the electric sign based on building number (anded with $03)
ELECTRIC_SIGN_X_POS:
		.db     $28, $28, $30, $30

; $3FBA - Used as the B value in INIT_ELEC_CABLES
INIT_ELEC_CABLES_DATA:
        .db     $80, $80, $80, $80

; $3FBE - Indexed by a random number 0-7
Lb766_RND_LOOP_COUNTS:
		.db     $01, $03, $05, $02, $01, $03, $02, $01	; Used as a loop counter in Lb766

; $3FC6
		.db     $18, $19, $1A, $1B, $1C, $9B, $9A, $99

; $3FCE
		.db     $98, $99, $9A, $9B
        .db     $1C, $1B, $1A, $19

; $3FD6
		.db     $07, $F8, $00, $F8, $F8, $F8, $F8, $00
		.db     $F8, $07, $F8, $00, $F8, $07, $00, $07
		.db		$07, $07, $00, $07, $F8, $07, $F8, $00
		.db     $F8, $07, $F8, $00, $F8, $F8, $00, $F8

        .db     $C7, $F3

;-------------------------------------------------------------------------------
; Data End
;-------------------------------------------------------------------------------
 
 
        NOP                             ; 3FF8 00       .
        NOP                             ; 3FF9 00       .
        NOP                             ; 3FFA 00       .
        NOP                             ; 3FFB 00       .
        NOP                             ; 3FFC 00       .
        NOP                             ; 3FFD 00       .
        NOP                             ; 3FFE 00       .
        NOP                             ; 3FFF 00       .

;=============================================================================
; Called periodically to update the sound channels
;
;=============================================================================
UPDATE_SOUND:
        LD      IX,(RAM_START)          ; 4000 DD2A0080 .*D. Sound channel A data
        LD      IY,RAM_START            ; 4004 FD210080 .!D.
        LD      B,$00                   ; 4008 0600     .D
        CALL    SOUND_DECODE            ; 400A CD3540   .qQ

        LD      IX,(SNDB_DATA_PTR)      ; 400D DD2A0C80 .*.. Sound channel B data
        LD      IY,SNDB_DATA_PTR        ; 4011 FD210C80 .!..
        LD      B,$01                   ; 4015 0601     ..
        CALL    SOUND_DECODE            ; 4017 CD3540   .p.

        LD      IX,(SNDC_DATA_PTR)      ; 401A DD2A1880 .*.. Sound channel C data
        LD      IY,SNDC_DATA_PTR        ; 401E FD211880 .!..
        LD      B,$02                   ; 4022 0602     ..
        CALL    SOUND_DECODE            ; 4024 CD3540   .qQ

        LD      IX,(SNDS_DATA_PTR)      ; 4027 DD2A2480 .*5. Sound sample data
        LD      IY,SNDS_DATA_PTR        ; 402B FD212480 .!5.
        LD      B,$03                   ; 402F 0603     ..
        CALL    SOUND_DECODE            ; 4031 CD3540   .p.

        RET                             ; 4034 C9       .    End UPDATE_SOUND

;=============================================================================
; Decodes the sound data
;
; Input:
;	IX - Points to sound data
;	IY - The channel data pointer
;	B - Data group
;		0 - Sound channel A
;		1 - Sound channel B
;		2 - Sound channel C
;		3 - Sample channel?
;
; Data decode operations:
;
; $00 - $7F, Sound data
; ----------------------
; If normal mode, then:
; $XX $YY would set the Coarse, then Fine tone value
; If alternate mode, then:
; $XX
; $XX is multiplied by 2, then used as an offset into the decode table.  Then
; two values from that table are used to set the coarse and fine tone value.
;
; $80 - Do nothing
; ----------------
; Skips this value and goes on to the next
;
; $81 - $BF - Load delay counter
; ------------------------------
; $81 - shortest delay
; ...
; $BF - Longest delay
;
; $F0 - Set normal Address Decode
; --------------------------------
; Sets the address mode to go to the normal mode (no decode table used)
;
; $F1 - Set Alternate Address Decode
; -----------------------------------
; Sets the address mode to go to the decode table.
;
; $F2 - Set amplitude control
; ---------------------------
; Comes in the form $F2 $XX
; Where $XX is the amplitude value to set
;
; $F3 - Set envelope / cycle and envelope period
; ----------------------------------------------
; Comes in the form $F3 $XX $YY $ZZ
; Where
; $XX is the envelop cycle control
; $YY is the coarse envelope period
; $ZZ is the fine envelope period
;
; $F4 - Turn noise ON/OFF
; -----------------------
; $F4 $XX
; Where
; $XX - if bit 7 is set, noise is turned ON
;       if bit 7 is clear, noise is turned OFF 
;
; $F5 - Set sample volume (Data group 3 only)
; -------------------------------------------
; $F5 $XX
; Where
; $XX is the sample volume
;
; $F6 - Set sample rate (Data group 3 only)
; -----------------------------------------
; $F6 $XX
; Where
; $XX is the new sample rate
;
; $F7 - Trigger a sample (Data group 3 only)
; ------------------------------------------
; Triggers a sample
;
; $F8 - Do not trigger a sample
; -----------------------------
; Clears the sample trigger
;
; $F9 (If data group = 3) - Load decode Mode
; -------------------------------------------
; $F9 $XX
; Where:
; $XX is loaded into the alternate decode mode register (0 - normal, != 0 - alternate mode)
;
; $F9 (If data group != 3) - Set amplitude / envelope control
; -----------------------------------------------------------
; Amplitude set to mode 1, 0 amplitude, Envelope set to $0D (ramp down)
;
; $FA / $FB - Repeat Block
; ------------------------
; $FA $NN ... $FB
; This will repeat whatever is in between $NN and $FB $NN number of times.
; For example:
; $FA $03 $09 $10 $00 $60 $90 $FB
; This will repeat the $09 $10 $00 $60 $90 block 3 times
;
; $FC / $FD - Repeat Block
; ------------------------
; (Note: This is just like the $FA / $FC repeat, but is included so nested
;  repeat blocks can be used)
; $FC $NN ... $FD
; This will repeat whatever is in between $NN and $FD $NN number of times.
; For example:
; $FC $08 $09 $10 $00 $60 $90 $FD
; This will repeat the $09 $10 $00 $60 $90 block 8 times
;
; $FE - Turn off channel (or set sample volume to 0)
; --------------------------------------------------
; If data group 0 - 2, it will turn off the mixer channel (A - C)
; If sample, then it will set the sample volume to 0
;
; $FF - End Sound
; ---------------
; Ends the current sound channel
;=============================================================================
SOUND_DECODE:
        LD      A,(IX+$00)              ; 4035 DD7E00   .~D Get data value
        CP      $80                     ; 4038 FE80     ..  Is value = $80?
        JP      Z,Lb818                 ; 403A CA3342   .2C Yes, increment data pointer and re-start

        JP      SOUND_DECODE1           ; 403D C37E42   ... Nope, continue w/ sound decode

HANDLE_F_CODES:
        LD      A,(IX+$00)              ; 4040 DD7E00   .~D Get data value
        CP      $F8                     ; 4043 FEF8     ..  Is value >= $F8?
        JP      NC,Lb820                ; 4045 D20B41   ..E Yes, go here

; Check for data group 3
        LD      A,B                     ; 4048 78       x   Get data group
        CP      $03                     ; 4049 FE03     ..  Is group = 3?
        JP      Z,Lb821                 ; 404B CAF541   ..E Yes, go here

;---------------------------------------------------------------------
; Handle data codes $F0 - $F4 for data groups 0 - 2 (Channels A - C)
;---------------------------------------------------------------------
        LD      A,(IX+$00)              ; 404E DD7E00   .~D Get data value
        CP      $F0                     ; 4051 FEF0     ..  Is value = $F0?
        JR      NZ,Lb822                ; 4053 2008      L  Nope, continue

; Value = $F0, data group 0 - 2: Set regular address mode
        LD      A,$00                   ; 4055 3E00     >D  
        LD      (IY+$02),A              ; 4057 FD7702   .w. Regular address for data pointer
        JP      Lb818                   ; 405A C33342   .2C Increment data pointer and re-start

Lb822:  CP      $F1                     ; 405D FEF1     ..
        JR      NZ,Lb823                ; 405F 2008      L

; Value = $F1, data group 0 - 2: Set alternate address mode
        LD      A,$01                   ; 4061 3E01     >.
        LD      (IY+$02),A              ; 4063 FD7702   .w. Alternate address for data pointer
        JP      Lb818                   ; 4066 C33342   .2C Increment data pointer and re-start

Lb823:  CP      $F2                     ; 4069 FEF2     ..
        JR      NZ,Lb824                ; 406B 200F      N

; Value = $F2, data group 0 - 2: Set amplitude control
        LD      A,B                     ; 406D 78       x   Get data group
        OR      $08                     ; 406E F608     .L  Pick amplitude control register (channels A - C)
        OUT     (IO_SOUND_CTRL),A       ; 4070 D308     .L
        LD      A,(IX+$01)              ; 4072 DD7E01   .~. Get data value
        AND     $0F                     ; 4075 E60F     .N  Set amplitude for channel
        OUT     (IO_SND_W),A            ; 4077 D309     ..
        JP      Lb825                   ; 4079 C33B42   .z. Increment data pointer 2X and restart

Lb824:  CP      $F3                     ; 407C FEF3     ..  Is value = $F3?
        JR      NZ,Lb826                ; 407E 2027      "  Nope, continue

; Value = $F3, data group 0 - 2: Set amplitude control, envelope/cycle, and envelope period
        LD      A,B                     ; 4080 78       x   Get data group (0 - 2)
        OR      $08                     ; 4081 F608     .L  Pick amplitude control register (channels A - C)
        OUT     (IO_SOUND_CTRL),A       ; 4083 D308     .L
        LD      A,$10                   ; 4085 3E10     >.  Set amplitude to mode 1
        OUT     (IO_SND_W),A            ; 4087 D309     ..

        LD      A,$0D                   ; 4089 3E0D     >.  Select envelope / cycle control
        OUT     (IO_SOUND_CTRL),A       ; 408B D308     .L
        LD      A,(IX+$01)              ; 408D DD7E01   .~. Get data value
        OUT     (IO_SND_W),A            ; 4090 D309     ..  Set envelope / cycle control

        LD      A,$0C                   ; 4092 3E0C     >.  Select coarse envelope period register
        OUT     (IO_SOUND_CTRL),A       ; 4094 D308     .L
        LD      A,(IX+$02)              ; 4096 DD7E02   .~G Get data value
        OUT     (IO_SND_W),A            ; 4099 D309     ..  Set coarse envelope period

        LD      A,$0B                   ; 409B 3E0B     >.  Select fine envelope period register
        OUT     (IO_SOUND_CTRL),A       ; 409D D308     .L
        LD      A,(IX+$03)              ; 409F DD7E03   .~S Get data value
        OUT     (IO_SND_W),A            ; 40A2 D309     ..  Set fine envelope period register
        JP      Lb827                   ; 40A4 C34B42   .^C Increment data pointer 4X and restart

Lb826:  CP      $F4                     ; 40A7 FEF4     ..  Is value = $F4?
        JP      NZ,Lb828                ; 40A9 C2C543   .:V Nope, exit subroutine

; Value = $F4, data group 0 - 3: Turn noise ON/OFF
        LD      A,$07                   ; 40AC 3E07     >.  Select mixer control register 
        OUT     (IO_SOUND_CTRL),A       ; 40AE D308     .L
        LD      A,(IX+$01)              ; 40B0 DD7E01   .~.
        AND     $80                     ; 40B3 E680     ..  Is bit 7 set?
        JR      NZ,Lb829                ; 40B5 2025      0  Nope, turn noise off

;-----------------------------------------------------------------------------
; Turns on noise channels A - C, depending on data group (0 - 2)
        LD      A,B                     ; 40B7 78       x   Get data group
        CP      $00                     ; 40B8 FE00     .D
        JR      NZ,Lb830                ; 40BA 2008      L  Is data group = 0? Nope, continue

; Data group 0 - Enable channel A noise
        IN      A,(IO_SND_R)            ; 40BC DB0C     ..  Read mixer control value
        AND     $F7                     ; 40BE E6F7     ..  Clear bit 3 (enable channel A noise)
        OUT     (IO_SND_W),A            ; 40C0 D309     ..  Set mixer control
        JR      SET_NOISE_GENERATOR     ; 40C2 183B     .:  Continue

Lb830:  CP      $01                     ; 40C4 FE01     ..  Is data group = 1?
        JR      NZ,Lb832                ; 40C6 2008      L  Nope, continue

; Data group 1 - Enable channel B noise
        IN      A,(IO_SND_R)            ; 40C8 DB0C     ..  Read mixer control value
        AND     $EF                     ; 40CA E6EF     ..  Clear bit 4 (enable channel B noise)
        OUT     (IO_SND_W),A            ; 40CC D309     ..  Set mixer control
        JR      SET_NOISE_GENERATOR     ; 40CE 182F     .*  Continue

Lb832:  CP      $02                     ; 40D0 FE02     ..  Is data group = 2?
        JR      NZ,Lb833                ; 40D2 2021      0  Nope, continue

; Data group 2 - Enable channel C noise
        IN      A,(IO_SND_R)            ; 40D4 DB0C     ..  Read mixer control value
        AND     $DF                     ; 40D6 E6DF     ..  Clear bit 5 (enable channel C noise)
        OUT     (IO_SND_W),A            ; 40D8 D309     ..  Set mixer control
        JR      SET_NOISE_GENERATOR     ; 40DA 1823     .s  Continue

;-----------------------------------------------------------------------------
; Turns off noise for channels A - C, depending on the data group (0 - 2)
Lb829:  LD      A,B                     ; 40DC 78       x   Get data group
        CP      $00                     ; 40DD FE00     .D  
        JR      NZ,Lb834                ; 40DF 2008      L  Is group = 0? Nope, continue

; Data group 0 - Disable noise for channel A
        IN      A,(IO_SND_R)            ; 40E1 DB0C     .\  Read mixer value
        OR      $08                     ; 40E3 F608     .L  Set bit 3 (disable noise channel A)
        OUT     (IO_SND_W),A            ; 40E5 D309     ..  Set mixer
        JR      SET_NOISE_GENERATOR     ; 40E7 1816     .S  Continue

Lb834:  CP      $01                     ; 40E9 FE01     ..  Is data group = 1?
        JR      NZ,Lb833                ; 40EB 2008      L  Nope, continue

; Data group 1 - Disable noise for channel B
        IN      A,(IO_SND_R)            ; 40ED DB0C     .\  Read mixer value
        OR      $10                     ; 40EF F610     ..  Set bit 4 (disable noise channel B)
        OUT     (IO_SND_W),A            ; 40F1 D309     ..  Set mixer value
        JR      SET_NOISE_GENERATOR     ; 40F3 180A     .O  Continue

Lb833:  CP      $02                     ; 40F5 FE02     .G  Is data group = 2?
        JR      NZ,Lb833                ; 40F7 20FC      .  Nope, continue

; Data group 2 - Disable noise for channel C
        IN      A,(IO_SND_R)            ; 40F9 DB0C     .\  Read mixer value
        OR      $20                     ; 40FB F620     .d  Set bit 5 (disable noise channel C)
        OUT     (IO_SND_W),A            ; 40FD D309     ..  Set mixer value


;-----------------------------------------------------------------------------
; Sets the noise generator register
SET_NOISE_GENERATOR:
        LD      A,$06                   ; 40FF 3E06     >.  Select noise generator register
        OUT     (IO_SOUND_CTRL),A       ; 4101 D308     .L
        LD      A,(IX+$01)              ; 4103 DD7E01   .~. Read data value
        OUT     (IO_SND_W),A            ; 4106 D309     ..  Set noise generator
        JP      Lb825                   ; 4108 C33B42   .:C Increment data pointer 2X and restart


;---------------------------------------------------------------------
; Handle data codes $F8 - $FE
;---------------------------------------------------------------------
Lb820:  CP      $F8                     ; 410B FEF8     ..  Is data value = $F8?
        JR      NZ,Lb835                ; 410D 2008      L  Nope, continue

; Value = $F8 - Do not trigger a sample
        LD      A,$01                   ; 410F 3E01     >.  A = 1
        LD      (SMPL_TRIG_WR),A        ; 4111 3204A0   2T_ Do not trigger a sample
        JP      Lb818                   ; 4114 C33342   .2C Increment data pointer and re-start

Lb835:  CP      $F9                     ; 4117 FEF9     ..  Is value = $F9?
        JR      NZ,Lb836                ; 4119 2022      g  Nope, continue

; Value = $F9
        LD      A,B                     ; 411B 78       x   Get data group
        CP      $03                     ; 411C FE03     .S  Is data group = 3?  
        JR      NZ,Lb837                ; 411E 2009      .  Nope, continue

;-----------------------------------------------------------------------------
; Value = $F9
; Data group = 3
; Load the alternate decode mode flag
        LD      A,(IX+$01)              ; 4120 DD7E01   .~. Get next data value
        LD      (IY+$02),A              ; 4123 FD7702   .w. Load into the alternate decode mode flag
        JP      Lb825                   ; 4126 C33B42   .:C Increment data pointer 2X and restart

;-----------------------------------------------------------------------------
; Value = $F9
; Data group 0 - 2 (Sound channel A - C)
;
; Set channel amplitude
Lb837:  LD      A,B                     ; 4129 78       x   Get data group
        OR      $08                     ; 412A F608     .L  Select amplitude control reg. (channels A - C)  
        OUT     (IO_SOUND_CTRL),A       ; 412C D308     .L
        LD      A,$10                   ; 412E 3E10     >.  Set amplitude mode to 1, 0 volume
        OUT     (IO_SND_W),A            ; 4130 D309     ..

        LD      A,$0D                   ; 4132 3E0D     >]  Select envelope/cycle control register.
        OUT     (IO_SOUND_CTRL),A       ; 4134 D308     .L
        LD      A,$09                   ; 4136 3E09     >.  Envelope ramps down, then silence
        OUT     (IO_SND_W),A            ; 4138 D309     ..  Set envelope/cycle control

        JP      Lb818                   ; 413A C33342   .2C Increment data pointer and re-start

Lb836:  CP      $FA                     ; 413D FEFA     ..  Is value = $FA?
        JR      NZ,Lb838                ; 413F 2017      .  Nope, continue

; Value = $FA
;
; Takes the current data pointer and increment it by 2.
; This pointer is saved at BASE_PTR+6
; The next data value is saved at BASE_PTR+8
;
        LD      L,(IY+$00)              ; 4141 FD6E00   .nD Get data pointer
        LD      H,(IY+$01)              ; 4144 FD6601   .f.
        INC     HL                      ; 4147 23       #   Increment pointer by 2
        INC     HL                      ; 4148 23       #
        LD      (IY+$06),L              ; 4149 FD7506   .uG Save pointer value
        LD      (IY+$07),H              ; 414C FD7407   .tF

        LD      A,(IX+$01)              ; 414F DD7E01   .~. Get next data value
        LD      (IY+$08),A              ; 4152 FD7708   .wL Store data value
        JP      Lb825                   ; 4155 C33B42   .z. Increment data pointer 2X and restart

Lb838:  CP      $FB                     ; 4158 FEFB     ..  Is value = $FB
        JR      NZ,Lb839                ; 415A 201B      .  Nope, continue

; Value = $FB
; Looks at the saved count value (from $FA operation).  If this value is !=0,
; then the value is decremented, and the saved data pointer (from $FA operation)
; is loaded as the data pointer.  This is where we left off...
        LD      A,(IY+$08)              ; 415C FD7E08   .~L Get counter
        DEC     A                       ; 415F 3D       =   Decrement value
        CP      $FF                     ; 4160 FEFF     ..  Is value $FF?
        JP      Z,Lb818                 ; 4162 CA3342   .2C Yes, increment data pointer and re-start

        DEC     (IY+$08)                ; 4165 FD3508   .5L Decrement counter
        LD      L,(IY+$06)              ; 4168 FD6E06   .n. Get saved pointer (With $FA operation)
        LD      H,(IY+$07)              ; 416B FD6607   .f.

        LD      (IY+$00),L              ; 416E FD7500   .uD This is our new pointer
        LD      (IY+$01),H              ; 4171 FD7401   .t.
        JP      Lb840                   ; 4174 C35D42   ..C Keep current pointer and re-start

Lb839:  CP      $FC                     ; 4177 FEFC     ..  Is value = $FC?
        JR      NZ,Lb841                ; 4179 2017      .  Nope, continue

; Value = $FC
;
; Takes the current data pointer and increment it by 2.
; This pointer is saved at BASE_PTR+9
; The next data value is saved at BASE_PTR+B
        LD      L,(IY+$00)              ; 417B FD6E00   .nD Get current data pointer
        LD      H,(IY+$01)              ; 417E FD6601   .f.
        INC     HL                      ; 4181 23       #   Increment it by 2
        INC     HL                      ; 4182 23       #
        LD      (IY+$09),L              ; 4183 FD7509   .u. Save new pointer
        LD      (IY+$0A),H              ; 4186 FD740A   .tO
        LD      A,(IX+$01)              ; 4189 DD7E01   .~. Get next data value
        LD      (IY+$0B),A              ; 418C FD770B   .w. Save value
        JP      Lb825                   ; 418F C33B42   .z. Increment data pointer 2X and restart

Lb841:  CP      $FD                     ; 4192 FEFD     ..  Is value = $FD?
        JR      NZ,Lb842                ; 4194 201B      .  Nope, continue

; Value = $FD
; Looks at the saved count value (from $FC operation).  If this value is !=0,
; then the value is decremented, and the saved data pointer (from $FC operation)
; is loaded as the data pointer.  This is where we left off...
        LD      A,(IY+$0B)              ; 4196 FD7E0B   .~. Get counter from $FC operation
        DEC     A                       ; 4199 3D       =   Decrement counter
        CP      $FF                     ; 419A FEFF     ..  Is value = $FF?
        JP      Z,Lb818                 ; 419C CA3342   .2C Yes, increment data pointer and re-start

        DEC     (IY+$0B)                ; 419F FD350B   .5[ Decrement counter
        LD      L,(IY+$09)              ; 41A2 FD6E09   .n. Get saved data pointer
        LD      H,(IY+$0A)              ; 41A5 FD660A   .f. 
        LD      (IY+$00),L              ; 41A8 FD7500   .uD This is our new data pointer
        LD      (IY+$01),H              ; 41AB FD7401   .t. 
        JP      Lb840                   ; 41AE C35D42   ..C Keep current pointer and re-start

Lb842:  CP      $FE                     ; 41B1 FEFE     ..  Is value = $FE?
        JP      NZ,Lb828                ; 41B3 C2C543   .:V Nope, exit subroutine

;-----------------------------------------------------------------------------
; Value = $FE - Turns off tone channels A - C, depending on data group 0 - 2
        LD      A,$07                   ; 41B6 3E07     >.   Select mixer register
        OUT     (IO_SOUND_CTRL),A       ; 41B8 D308     .L

        LD      A,B                     ; 41BA 78       x    Get data group
        CP      $00                     ; 41BB FE00     .D   Is group = 0?
        JR      NZ,Lb843                ; 41BD 2009      .   Nope, continue

; Data group 0 - Turn off tone channel A
        IN      A,(IO_SND_R)            ; 41BF DB0C     .\   Read mixer
        OR      $01                     ; 41C1 F601     ..   Set bit 0 (turn off channel A tone)
        OUT     (IO_SND_W),A            ; 41C3 D309     ..   Set mixer
        JP      Lb844                   ; 41C5 C3E541   ..E

Lb843:  CP      $01                     ; 41C8 FE01     ..   Is data group = 1?
        JR      NZ,Lb845                ; 41CA 2008      L   Nope, continue

; Data group 1 - Turn off tone channel B
        IN      A,(IO_SND_R)            ; 41CC DB0C     ..   Read mixer
        OR      $02                     ; 41CE F602     ..   Set bit 1 (turn off channel B tone)
        OUT     (IO_SND_W),A            ; 41D0 D309     ..   Set mixer
        JR      Lb844                   ; 41D2 1811     .A

Lb845:  CP      $02                     ; 41D4 FE02     ..  Is data group = 2?
        JR      NZ,Lb846                ; 41D6 2008      L  Nope, continue

; Data group 2 - Turn off tone channel C
        IN      A,(IO_SND_R)            ; 41D8 DB0C     ..  Read mixer
        OR      $04                     ; 41DA F604     ..  Set bit 2 (turn off channel C tone)
        OUT     (IO_SND_W),A            ; 41DC D309     ..  Set mixer
        JR      Lb844                   ; 41DE 1805     .U

;----------------------------
; Turn off the sample volume
Lb846:  LD      A,$00                   ; 41E0 3E00     >D  A = 0
        LD      (SMPL_VOL_WR),A         ; 41E2 3200B0   2D. Set the sample volume

; Update data pointer
Lb844:  LD      L,(IY+$00)              ; 41E5 FD6E00   .nD
        LD      H,(IY+$01)              ; 41E8 FD6601   .f.
        INC     HL                      ; 41EB 23       #   Go to next byte
        LD      (IY+$00),L              ; 41EC FD7500   .uD
        LD      (IY+$01),H              ; 41EF FD7401   .t.
        JP      Lb828                   ; 41F2 C3C543   ... Exit subroutine

;---------------------------------------------------------------------
; Handle data codes $F5 - $F7 for data group 3
;---------------------------------------------------------------------
Lb821:  LD      A,(IX+$00)              ; 41F5 DD7E00   .~D Get data value
        CP      $F5                     ; 41F8 FEF5     ..  Is value = $F5?
        JR      NZ,Lb847                ; 41FA 200D      ]  Nope, continue

; Value = $F5, Data group 3 - Set sample volume
        LD      A,(IX+$01)              ; 41FC DD7E01   .~. Get next data value
        OR      $10                     ; 41FF F610     ..  Set bit 4
        LD      (IY+$0C),A              ; 4201 FD770C   .w. Save sample volume
        LD      (SMPL_VOL_WR),A         ; 4204 3200B0   2D. Set the sample volume
        JR      Lb825                   ; 4207 1832     .'  Increment data pointer 2X and restart

Lb847:  CP      $F6                     ; 4209 FEF6     ..  Is value = $F6?
        JR      NZ,Lb848                ; 420B 2008      L  Nope, continue

; Value = $F6, data group 3 - Set sample rate
        LD      A,(IX+$01)              ; 420D DD7E01   .~. Get next data value
        LD      (SMPL_RATE_WR),A        ; 4210 3200A8   2D. Set sound sample rate
        JR      Lb825                   ; 4213 1826     .3  Increment data pointer 2X and restart

Lb848:  CP      $F7                     ; 4215 FEF7     ..  Is value = $F7?
        JP      NZ,Lb828                ; 4217 C2C543   .:V Nope, exit subroutine

; Value = $F7, data group 3
        LD      A,$00                   ; 421A 3E00     >D  A = 0
        LD      (SMPL_TRIG_WR),A        ; 421C 3204A0   2.. Trigger a sample

;-----------------------
; Write to sound port A
        LD      A,$0E                   ; 421F 3E0E     >.  Select sound port A
        OUT     (IO_SOUND_CTRL),A       ; 4221 D308     .L
        LD      A,(IX+$01)              ; 4223 DD7E01   .~. Get next data value
        OUT     (IO_SND_W),A            ; 4226 D309     ..  Write to sound port A

;-----------------------
; Write to sound port B
        LD      A,$0F                   ; 4228 3E0F     >.  Select sound port B
        OUT     (IO_SOUND_CTRL),A       ; 422A D308     .L
        LD      A,(IX+$02)              ; 422C DD7E02   .~G Get next next data value
        OUT     (IO_SND_W),A            ; 422F D309     ..  Write to sound port B
        JR      Lb849                   ; 4231 1810     ..  Increment data pointer 3X and restart


;-------------------------------------------------------------
; Updates the data pointer and re-starts (loops) the routine

Lb818:  LD      L,(IY+$00)              ; 4233 FD6E00   .nD  Load data pointer
        LD      H,(IY+$01)              ; 4236 FD6601   .f.
        JR      Lb850                   ; 4239 181B     .Z   Increment data pointer by 1 and restart

Lb825:  LD      L,(IY+$00)              ; 423B FD6E00   .nD  Load data pointer
        LD      H,(IY+$01)              ; 423E FD6601   .f.
        JR      Lb851                   ; 4241 1812     ..   Increment data pointer by 2 and restart

Lb849:  LD      L,(IY+$00)              ; 4243 FD6E00   .nD  Load data pointer
        LD      H,(IY+$01)              ; 4246 FD6601   .f.
        JR      Lb852                   ; 4249 1809     ..   Increment data pointer by 3 and restart

Lb827:  LD      L,(IY+$00)              ; 424B FD6E00   .nD  Load data pointer
        LD      H,(IY+$01)              ; 424E FD6601   .f.
        JR      Lb853                   ; 4251 1800     .D   Increment data pointer by 4 and restart

; Increment pointer 4X
Lb853:  INC     HL                      ; 4253 23       #

; Increment pointer 3X
Lb852:  INC     HL                      ; 4254 23       #

: Increment pointer 2X
Lb851:  INC     HL                      ; 4255 23       #

; Increment pointer and save
Lb850:  INC     HL                      ; 4256 23       #
        LD      (IY+$00),L              ; 4257 FD7500   .uD
        LD      (IY+$01),H              ; 425A FD7401   .t.

Lb840:  PUSH    HL                      ; 425D E5       .
        POP     IX                      ; 425E DDE1     ..   IX = HL
        LD      A,$80                   ; 4260 3E80     >.   Mark as a control byte?
        LD      (IY+$04),A              ; 4262 FD7704   .wT
        LD      (IY+$05),A              ; 4265 FD7705   .wU
        JP      SOUND_DECODE            ; 4268 C33540   .qQ  Go back to start of routine

; Increment data pointer
Lb855:  LD      L,(IY+$00)              ; 426B FD6E00   .nD
        LD      H,(IY+$01)              ; 426E FD6601   .f.
        INC     HL                      ; 4271 23       #
        LD      (IY+$00),L              ; 4272 FD7500   .uD
        LD      (IY+$01),H              ; 4275 FD7401   .t.
; Set IX equal to pointer
        PUSH    HL                      ; 4278 E5       .
        POP     IX                      ; 4279 DDE1     ..
        JP      SOUND_DECODE            ; 427B C33540   .p.  Go back to start of routine

;----------------------------------------------------------------
; ... Continuing with the sound decode (from the routine start)
SOUND_DECODE1:
        AND     $C0                     ; 427E E6C0     ..   And value with $C0
        CP      $80                     ; 4280 FE80     ..   Is value != $80?
        JR      NZ,Lb854                ; 4282 200C      .   Yes, go here

;-------------------------------------------------------
; Data is $81 - $BF - This is a counter data value
; (Remember $80 values are skipped before calling this)
        LD      A,(IX+$00)              ; 4284 DD7E00   .~D Get sound data
        AND     $3F                     ; 4287 E63F     ..  Clear bits 6 & 7
        OR      $80                     ; 4289 F680     ..  Set bit 7
        LD      (IY+$05),A              ; 428B FD7705   .wU Store 2nd counter
        JR      Lb855                   ; 428E 18DB     ..  Increment data pointer and start routine over

Lb854:  DEC     (IY+$04)                ; 4290 FD3504   .5T Decrement working counter
        LD      A,(IY+$04)              ; 4293 FD7E04   .~. Get counter
        CP      $80                     ; 4296 FE80     ..  Is value >= $80?
        JP      NC,Lb828                ; 4298 D2C543   ... Yes, exit subroutine

; Working counter needs re-initialized
        LD      A,(IY+$03)              ; 429B FD7E03   .~S Get sound init flag
        LD      (IY+$04),A              ; 429E FD7704   .wT Save to working sound flag

        LD      A,(IY+$05)              ; 42A1 FD7E05   .~U Get 2nd counter
        CP      $82                     ; 42A4 FE82     .}  Is 2nd counter < $82?
        JP      C,Lb856                 ; 42A6 DAC242   ..C Yes, go here

        DEC     (IY+$05)                ; 42A9 FD3505   .5U Decrement second counter
        LD      A,B                     ; 42AC 78       x   Get data group
        CP      $03                     ; 42AD FE03     ..  Is this data group 3?
        JP      NZ,Lb828                ; 42AF C2C543   .:V Nope, exit subroutine

        LD      A,(IY+$05)              ; 42B2 FD7E05   .~. Get 2nd counter
        CP      $82                     ; 42B5 FE82     ..  Is value >= $82?
        JP      NC,Lb828                ; 42B7 D2C543   .:V Yes, Exit subroutine

        LD      A,$00                   ; 42BA 3E00     >D  A = 0
        LD      (SMPL_TRIG_WR),A        ; 42BC 3204A0   2.. Trigger a sample
        JP      Lb828                   ; 42BF C3C543   .:V Exit subroutine

Lb856:  LD      A,(IX+$00)              ; 42C2 DD7E00   .~D Get data value
        CP      $F0                     ; 42C5 FEF0     ..  Is value >= $F0?
        JP      NC,HANDLE_F_CODES       ; 42C7 D24040   .Q. Yes, handle the $F0 - $FF codes

; Data value is < $F0
        LD      A,(IY+$02)              ; 42CA FD7E02   .~G Get pointer addressing flag
        CP      $00                     ; 42CD FE00     .D  Is value = 0?
        JR      NZ,ALT_SND_ADDRESSING   ; 42CF 2069      (  Nope, go to alternate addressing mode


;-----------------------------------------------------------------------------
; Normal addressing mode
;-----------------------------------------------------------------------------

;-----------------------------------------------------------------------------
; Data groups 0 - 2:
; Write to sound tone generator 
;
; Data group 3:
; Write to sound data ports A & B  and set the sample rate
;
; Note: IX is the sound data pointer
;
; Data group	Comments
; ----------	-----------------------------------------------
; 0				Sets Coarse (IX), Fine tone generator channel A (IX+1)
; 1				Sets Coarse (IX), Fine tone generator channel B (IX+1)
; 2				Sets Coarse (IX), Fine tone generator channel C (IX+1)
; 3				Write to data port A (IX), Write $3F to data port B, and 
;				set sample rate (IX+1)
;-----------------------------------------------------------------------------
        LD      A,B                     ; 42D1 78       x   Get data group
        CP      $00                     ; 42D2 FE00     .D  
        JR      NZ,Lb859                ; 42D4 2004      .  DataGroup != $00? Yes, go here

; Data group = 0
        LD      A,$01                   ; 42D6 3E01     >.  
        JR      Lb860                   ; 42D8 180E     .O  Write value to sound register 1 (Coarse tone channel A)


Lb859:  CP      $01                     ; 42DA FE01     ..  Is data group 1?
        JR      NZ,Lb861                ; 42DC 2004      .  Nope, go here

; Data group 1
        LD      A,$03                   ; 42DE 3E03     >S
        JR      Lb860                   ; 42E0 1806     .G  Write value to sound register 3 (Coarse tone channel B)

Lb861:  CP      $02                     ; 42E2 FE02     ..  Is data group 2?
        JR      NZ,Lb862                ; 42E4 202C      =  Nope, go here

; Data group 2
        LD      A,$05                   ; 42E6 3E05     >U  Write value to sound register 5 (Coarse tone channel C)

;-------------------------------
; Write to coarse tone channels
Lb860:  OUT     (IO_SOUND_CTRL),A       ; 42E8 D308     .L  Select sound chip register
        LD      A,(IX+$00)              ; 42EA DD7E00   .~D Get data value
        OUT     (IO_SND_W),A            ; 42ED D309     ..  Write data value to sound chip register
        JR      Lb863                   ; 42EF 1800     .D  Continue

Lb863:  LD      A,B                     ; 42F1 78       x
        CP      $00                     ; 42F2 FE00     .D
        JR      NZ,Lb864                ; 42F4 2004      .  Not data group 0? Go here

; Data group 0
        LD      A,$00                   ; 42F6 3E00     >D
        JR      Lb865                   ; 42F8 180E     .O  Write value to sound reg. 0 (Fine tone channel A)

Lb864:  CP      $01                     ; 42FA FE01     ..
        JR      NZ,Lb866                ; 42FC 2004      .  Not data group 1? Go here

; Data group 1
        LD      A,$02                   ; 42FE 3E02     >.  
        JR      Lb865                   ; 4300 1806     .G  Write value to sound reg 2 (Fine tone channel B)

Lb866:  CP      $02                     ; 4302 FE02     ..
        JR      NZ,ALT_SND_ADDRESSING   ; 4304 2034      `  Not data group 2? Go to alternate sound addressing mode
        LD      A,$04                   ; 4306 3E04     >.  Write value to sound reg 4 (Fine tone channel C)


;------------------------------
; Write to fine tone channels
Lb865:  OUT     (IO_SOUND_CTRL),A       ; 4308 D308     .L
        LD      A,(IX+$01)              ; 430A DD7E01   .~.
        OUT     (IO_SND_W),A            ; 430D D309     ..
        JP      Lb867                   ; 430F C32943   .<V

;---------------------------------------------
; Data group 3 - Write to data ports A and B & set sample rate
Lb862:  LD      A,$0E                   ; 4312 3E0E     >O  Select data port A
        OUT     (IO_SOUND_CTRL),A       ; 4314 D308     .L
        LD      A,(IX+$00)              ; 4316 DD7E00   .~D Get data value
        OUT     (IO_SND_W),A            ; 4319 D309     ..  Write to port A

        LD      A,$0F                   ; 431B 3E0F     >N  Select data port B
        OUT     (IO_SOUND_CTRL),A       ; 431D D308     .L
        LD      A,$3F                   ; 431F 3E3F     >.  Value to write is $3F
        OUT     (IO_SND_W),A            ; 4321 D309     ..  Write to port B

        LD      A,(IX+$01)              ; 4323 DD7E01   .~.
        LD      (SMPL_RATE_WR),A        ; 4326 3200A8   2D. Set sound sample rate

; Increment sound data pointer
Lb867:  LD      L,(IY+$00)              ; 4329 FD6E00   .nD
        LD      H,(IY+$01)              ; 432C FD6601   .f.
        INC     HL                      ; 432F 23       #
        INC     HL                      ; 4330 23       #
        LD      (IY+$00),L              ; 4331 FD7500   .uD
        LD      (IY+$01),H              ; 4334 FD7401   .t.
        JP      SET_MIXER_VOLUME        ; 4337 C39043   ..V Set mixer / volume



;-----------------------------------------------------------------------------
; This is an alternate sound data addressing mode.  It is called when the
; alternate addressing mode flag is != 0.
;
; In this "mode", the least significant byte of the current sound data pointer
; is multiplied by 2 and added to ALT_SND_TABLE.  This is the new data pointer.
;-----------------------------------------------------------------------------
ALT_SND_ADDRESSING:
        LD      L,(IX+$00)              ; 433A DD6E00   .nD Get least significant byte from data pointer
        LD      H,$00                   ; 433D 2600     &D  Make this an offset
        ADD     HL,HL                   ; 433F 29       )   Offset = Offset * 2
        LD      DE,ALT_SND_TABLE        ; 4340 11C843   ... Point to data start
        ADD     HL,DE                   ; 4343 19       .   HL = ALT_SND_TABLE + offset

;-----------------------------------------------------------------------------
; Set tone generator (fine) control
        LD      A,B                     ; 4344 78       x   Get data group
        CP      $00                     ; 4345 FE00     .D  Group = 0? 
        JR      NZ,Lb869                ; 4347 2004      T  Nope, continue

; Data group 0 - Channel A fine tone control
        LD      A,$00                   ; 4349 3E00     >D  Select tone channel A (fine)
        JR      Lb870                   ; 434B 180E     ..

Lb869:  CP      $01                     ; 434D FE01     ..  Data group = 1?
        JR      NZ,Lb871                ; 434F 2004      T  Nope, continue

; Data group 1 - Channel B fine tone control
        LD      A,$02                   ; 4351 3E02     >G  Select tone channel B (fine)
        JR      Lb870                   ; 4353 1806     ..  

Lb871:  CP      $02                     ; 4355 FE02     .G  Data group = 2?
        JR      NZ,Lb872                ; 4357 2027      f  Nope, continue - Write to sound data ports A & B & set sample rate

; Data group 2 - Channel C fine tone control
        LD      A,$04                   ; 4359 3E04     >T  Select tone channel C (fine)

Lb870:  OUT     (IO_SOUND_CTRL),A       ; 435B D308     .L  Select fine tone channel control register
        LD      A,(HL)                  ; 435D 7E       ~   Read data
        OUT     (IO_SND_W),A            ; 435E D309     ..  Set fine tone channel control

;-----------------------------------------------------------------------------
; Set tone generator (coarse) control
        LD      A,B                     ; 4360 78       x   Get data group
        CP      $00                     ; 4361 FE00     .D  Is group = 0?
        JR      NZ,Lb873                ; 4363 2004      T  Nope, continue

; Data group 0 - Channel A coarse tone control
        LD      A,$01                   ; 4365 3E01     >.  Select tone channel A (coarse)
        JR      Lb874                   ; 4367 180E     ..  

Lb873:  CP      $01                     ; 4369 FE01     ..  Is group = 1?
        JR      NZ,Lb875                ; 436B 2004      T  Nope, continue

; Data group 1 - Channel A coarse tone control
        LD      A,$03                   ; 436D 3E03     >.  Select tone channel B (coarse)
        JR      Lb874                   ; 436F 1806     ..

Lb875:  CP      $02                     ; 4371 FE02     .G  Is group = 2?
        JR      NZ,Lb872                ; 4373 200B      .  Nope, continue - Write to sound data ports A & B & set sample rate

; Data group 2 - Channel A coarse tone control
        LD      A,$05                   ; 4375 3E05     >.  Select tone channel C (coarse)

Lb874:  OUT     (IO_SOUND_CTRL),A       ; 4377 D308     .L  Select coarse tone channel control register
        INC     HL                      ; 4379 23       #   Go to next byte
        LD      A,(HL)                  ; 437A 7E       ~   Get data value
        OUT     (IO_SND_W),A            ; 437B D309     ..  Set coarse tone channel control
        JP      Lb876                   ; 437D C38343   ..V

Lb872:  JP      Lb862                   ; 4380 C31243   .F. Write to sound data ports A & B & set sample rate


; Point to next data value
Lb876:  LD      L,(IY+$00)              ; 4383 FD6E00   .nD
        LD      H,(IY+$01)              ; 4386 FD6601   .f.
        INC     HL                      ; 4389 23       #
        LD      (IY+$00),L              ; 438A FD7500   .uD
        LD      (IY+$01),H              ; 438D FD7401   .t.


;---------------------------------------------------
; Select the sound mixer register of the sound chip
SET_MIXER_VOLUME:
        LD      A,$07                   ; 4390 3E07     >.
        OUT     (IO_SOUND_CTRL),A       ; 4392 D308     .L  Select Mixer control I/O enable

        LD      A,B                     ; 4394 78       x   Get data group
        CP      $00                     ; 4395 FE00     .D
        JR      NZ,Lb877                ; 4397 2006      .  Is data group != 0? Yes, go here

; Data group 0
        IN      A,(IO_SND_R)            ; 4399 DB0C     .\  Read mixer
        AND     $FE                     ; 439B E6FE     ..  Clear bit 0 (Enable tone channel A)
        JR      Lb878                   ; 439D 1812     ..  Write back to mixer

Lb877:  CP      $01                     ; 439F FE01     ..
        JR      NZ,Lb879                ; 43A1 2006      .  Is data group != 1? Yes, go here

; Data group 1
        IN      A,(IO_SND_R)            ; 43A3 DB0C     .\  Read mixer
        AND     $FD                     ; 43A5 E6FD     ..  Clear bit 1 (Enable tone channel B)
        JR      Lb878                   ; 43A7 1808     .L  Write back to mixer

Lb879:  CP      $02                     ; 43A9 FE02     .G  
        JR      NZ,Lb880                ; 43AB 2008      L  Is data group != 2? Yes, go here

; Data group 2
        IN      A,(IO_SND_R)            ; 43AD DB0C     .\  Read mixer
        AND     $FB                     ; 43AF E6FB     ..  Clear bit 2 (Enable tone channel C)

Lb878:  OUT     (IO_SND_W),A            ; 43B1 D309     ..  Write mixer value back to sound chip register
        JR      Lb828                   ; 43B3 1810     ..  Exit subroutine


; Data group 3 - Update sample volume & trigger a sample
Lb880:  LD      A,(IY+$0C)              ; 43B5 FD7E0C   .~. Get value
        OR      $10                     ; 43B8 F610     ..  Set bit 4
        LD      (IY+$0C),A              ; 43BA FD770C   .w\ Save value
        LD      (SMPL_VOL_WR),A         ; 43BD 3200B0   2D. Set the sample volume
        LD      A,$01                   ; 43C0 3E01     >.  A = 1

Lb882:  LD      (SMPL_TRIG_WR),A        ; 43C2 3204A0   2.. Trigger a sample

Lb828:  RET                             ; 43C5 C9       .   End SOUND_DECODE

;-------------------------------------------------------------------------------
; Data Start
; Range: $43C6 - $4FFF
; Number of bytes: 3130
;-------------------------------------------------------------------------------

        .db     $C7, $FB			; Start data block

; $43C8
ALT_SND_TABLE:
        .db     $5D, $0D, $9C, $0C, $E7, $0B, $3C, $0B
        .db     $9B, $0A, $02, $0A, $73, $09, $EB, $08
        .db     $6B, $08, $F2, $07, $80, $07, $14, $07
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $AE, $06, $4E, $06, $F4, $05, $9E, $05
        .db     $4D, $05, $01, $05, $B9, $04, $75, $04
        .db     $35, $04, $F9, $03, $C0, $03, $8A, $03
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $57, $03, $27, $03, $FA, $02, $CF, $02
        .db     $A7, $02, $81, $02, $5D, $02, $3B, $02
        .db     $1B, $02, $FC, $01, $E0, $01, $C5, $01
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $AC, $01, $94, $01, $7D, $01, $68, $01
        .db     $53, $01, $40, $01, $2E, $01, $1D, $01
        .db     $0D, $01, $FE, $00, $F0, $00, $E2, $00
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $D6, $00, $CA, $00, $BE, $00, $B4, $00
        .db     $AA, $00, $A0, $00, $97, $00, $8F, $00
        .db     $87, $00, $7F, $00, $78, $00, $71, $00
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $6B, $00, $65, $00, $5F, $00, $5A, $00
        .db     $55, $00, $50, $00, $4C, $00, $47, $00
        .db     $43, $00, $40, $00, $3C, $00, $39, $00
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF

; Offset $0C0         
		.db     $35, $00, $32, $00, $30, $00, $2D, $00
        .db     $2A, $00, $28, $00, $26, $00, $24, $00
        .db     $22, $00, $20, $00, $1E, $00, $1C, $00
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $1B, $00, $19, $00, $18, $00, $16, $00
        .db     $15, $00, $14, $00, $13, $00, $12, $00
        .db     $11, $00, $10, $00, $0F, $00, $0E, $00
        .db     $08, $08, $00, $02, $05, $10, $01, $00

; Offset $100     
	    .db     $18, $04, $00, $00, $00, $00, $01, $01
        .db     $09, $06, $02, $00, $80, $84, $00, $01
        .db     $00, $00, $18, $08, $01, $05, $05, $00
        .db     $09, $00, $00, $02, $00, $0D, $00, $00
        
; Offset $120
		.db     $08, $06, $0C, $00, $01, $04, $08, $00
        .db     $48, $00, $04, $00, $02, $84, $25, $00
        .db     $04, $00, $00, $05, $0E, $06, $00, $01


; $4500 - Type 4, Index 5 - End of building 4 sound (Channel A)
        .db     $A0, $F2, $0D, $FA, $01, $50, $8A, $FE
        .db     $82, $50, $83, $FE, $81, $50, $8A, $FE
        .db     $82, $4A, $83, $FE, $81, $50, $8A, $FE
        .db     $82, $50, $83, $FE, $81, $53, $8A, $FE
        .db     $82, $50, $83, $FE, $81, $50, $8A, $FE
        .db     $82, $4A, $83, $FE, $81, $47, $8A, $FE
        .db     $82, $45, $83, $FE, $01, $47, $90, $FE
        .db     $90, $45, $8A, $FE, $82, $43, $83, $FE
        .db     $81, $45, $8A, $FE, $82, $43, $83, $FE
        .db     $81, $45, $8A, $FE, $82, $43, $83, $FE
        .db     $81, $45, $8A, $FE, $82, $47, $83, $FE
        .db     $81, $4A, $8A, $FE, $82, $47, $83, $FE
        .db     $81, $4A, $8A, $FE, $82, $53, $84, $50
        .db     $94, $FE, $88, $4A, $84, $50, $88, $FE
        .db     $84, $4A, $84, $50, $88, $FE, $84, $4A
        .db     $84, $50, $98, $FE, $98, $FB, $FE, $FF

; $4580 - Type 4, Index 5 - End of building 4 sound (Channel B)
        .db     $A0, $FE, $F3, $09, $20, $00, $FA, $01
        .db     $30, $F9, $9C, $2A, $F9, $84, $30, $F9
        .db     $A0, $27, $F9, $9C, $25, $F9, $84, $27
        .db     $F9, $A0, $25, $F9, $9C, $23, $F9, $84
        .db     $25, $F9, $A0, $27, $F9, $9C, $2A, $F9
        .db     $84, $30, $F9, $A0, $30, $F9, $90, $30
        .db     $F9, $90, $30, $F9, $B0, $FB, $FE, $FF
        .db     $A0, $27, $F3, $09, $20, $00, $9C, $2A
        .db     $F3, $09, $20, $00, $84, $30, $F3, $09
        .db     $20, $00, $A0, $30, $F3, $09, $20, $00
        .db     $90, $30, $F3, $09, $20, $00, $90, $30
        .db     $F3, $09, $20, $00, $B0, $FB, $FE, $FF

; $45E0 - Type 4, Index 5 - End of building 4 sound (Channel C)
        .db     $FE, $FF, $F2, $0C, $FA, $01, $FE, $82
        .db     $2B, $84, $FE, $84, $27, $84, $FE, $84
        .db     $30, $84, $FE, $84, $30, $84, $FE, $84
        .db     $30, $84, $27, $82, $1B, $84, $22, $82
        .db     $1B, $84, $20, $84, $FE, $84, $FB, $FF
        .db     $00, $00, $00, $00, $00, $00, $00, $00
        
; $4610 - Type 4, Index 5 - End of building 4 sound (Samples)
		.db     $80, $F5, $0E, $F6, $80, $F7, $80, $BF
        .db     $82, $F8, $9E, $FC, $01, $F5, $0E, $F6
        .db     $C0, $FA, $06, $8E, $F7, $70, $7F, $82
        .db     $F8, $94, $FB, $98, $FA, $02, $F7, $F8
        .db     $FF, $82, $F8, $92, $FB, $9E, $FD, $FF
        .db     $00, $00, $00, $00, $00, $00, $00, $00

; $4640 - Type 1, Index 1 - Falling dumbell/girder (Channel B)
        .db     $80, $F1, $F3, $09, $80, $00, $6B, $6A
        .db     $69, $68, $67, $66, $65, $64, $63, $62
        .db     $61, $60, $5B, $5A, $59, $58, $57, $56
        .db     $55, $54, $53, $52, $51, $50, $4B, $4A
        .db     $49, $48, $47, $46, $45, $43, $42, $41
        .db     $40, $3B, $3A, $39, $38, $37, $36, $35
        .db     $34, $32, $31, $30, $2B, $2A, $29, $28
        .db     $27, $26, $25, $24, $23, $22, $21, $20
        .db     $1B, $1A, $19, $18, $17, $16, $15, $14
        .db     $13, $12, $11, $10, $FE, $FF, $00, $00
        
; $4690 - Type 1, Index 1 - Falling dumbell/girder (Channel C)
		.db     $80, $F1, $F3, $09, $80, $00, $69, $68
        .db     $67, $66, $65, $64, $63, $62, $61, $60
        .db     $5B, $5A, $59, $58, $57, $56, $55, $54
        .db     $53, $52, $51, $50, $4B, $4A, $49, $48
        .db     $47, $46, $45, $43, $42, $41, $40, $3B
        .db     $3A, $39, $38, $37, $36, $35, $34, $33
        .db     $32, $31, $30, $2B, $2A, $29, $28, $27
        .db     $26, $25, $24, $23, $22, $21, $20, $1B
        .db     $1A, $19, $18, $17, $16, $15, $14, $13
        .db     $12, $11, $10, $F2, $00, $FE, $FF, $00

; $46E0 - Type 2, Index 2 - Electric Sign Music (Channel A)
; $46E0 - Type 2, Index 2 - Electric Sign Music (Channel B)
        .db     $80, $F1, $F2, $0C, $FC, $01, $FA, $07
        .db     $59, $66, $52, $59, $66, $59, $56, $62
        .db     $69, $62, $57, $62, $6B, $62, $5B, $67
        .db     $51, $57, $64, $57, $54, $61, $67, $61
        .db     $56, $61, $69, $61, $FB, $F3, $09, $FF

; $4708
        .db     $FF, $FD, $FE, $FF, $00, $00, $00, $00
; $4710
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
        .db     $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF

; $4800 - Type 4, Index 0 - Start Building Music (Channel A)
        .db     $80, $F4, $FF, $F1, $F2, $0C, $FA, $00
        .db     $40, $84, $FE, $81, $44, $81, $FE, $81
        .db     $47, $84, $FE, $81, $50, $83, $53, $81
        .db     $54, $83, $FE, $81, $52, $83, $FE, $81
        .db     $50, $83, $FE, $81, $49, $83, $FE, $81
        .db     $46, $90, $47, $82, $FE, $8E, $FB, $FF
        .db     $00, $00, $00, $00, $00, $00, $00, $00
        .db     $00, $00, $00, $00, $00, $00, $00, $00

; $4840 - Type 4, Index 0 - Start Building Music (Channel B)
        .db     $80, $F4, $FF, $F1, $F2, $0C, $FA, $02
        .db     $27, $88, $2A, $84, $2B, $84, $FB, $FE
        .db     $FF, $00, $00, $00, $00, $00, $00, $00
        .db     $00, $00, $00, $00, $00, $00, $00, $00

; $4860 - Type 4, Index 0 - Start Building Music (Channel C)
        .db     $80, $F4, $FF, $F1, $FA, $01, $F3, $09
        .db     $30, $00, $22, $90, $F3, $09, $30, $00
        .db     $17, $90, $FB, $FF, $00, $00, $00, $00
        .db     $00, $00, $00, $00, $00, $00, $00, $00

; $4880 - Type 4, Index 0 - Start Building Music (Sample)
        .db     $80, $F5, $0E, $F6, $B0, $FA, $03, $F7
        .db     $F8, $FF, $82, $F8, $88, $F7, $70, $7F
        .db     $82, $F8, $88, $FB, $F6, $50, $FA, $03
        .db     $A0, $F7, $00, $3F, $82, $F8, $FB, $FF

; $48A0 - Type 3, Index 0 - Climbing sound 1 (Sample)
        .db     $80, $F5, $0C, $F6, $90, $F7, $B8, $BF
        .db     $82, $F8, $B8, $F5, $0E, $B0, $F6, $70
        .db     $B0, $F7, $00, $3F, $82, $F8, $FF, $00
        .db     $00, $00, $00, $00, $00, $00, $00, $00

; $48C0 - Type 3, Index 1 - Climbing sound 2 (Sample)
        .db     $80, $F5, $0C, $F6, $70, $F7, $B8, $BF
        .db     $82, $F8, $B0, $F5, $0E, $B0, $F6, $60
        .db     $B0, $F7, $00, $3F, $82, $F8, $FF, $00
        .db     $00, $00, $00, $00, $00, $00, $00, $00

; $48E0 - Type 3, Index 2 - Hit by a pot (Sample)
        .db     $80, $F5, $0E, $F6, $90, $F7, $F8, $FF
        .db     $82, $F8, $88, $F5, $0F, $F6, $90, $F7
        .db     $40, $7F, $82, $F8, $FF, $00, $00, $00
        .db     $00, $00, $00, $00, $00, $00, $00, $00

; $4900 - Type 4, Index 6 - Bird Music (Channel A)
        .db     $80, $82, $FA, $00, $F1, $F2, $0C, $45
        .db     $83, $FE, $81, $47, $82, $45, $82, $47
        .db     $83, $FE, $81, $48, $83, $FE, $81, $50
        .db     $83, $FE, $81, $51, $82, $50, $82, $48
        .db     $83, $FE, $81, $50, $83, $FE, $81, $51
        .db     $81, $FE, $81, $55, $81, $FE, $81, $55
        .db     $82, $58, $82, $57, $82, $55, $82, $51
        .db     $83, $FE, $81, $50, $90, $FB, $FE, $FF
        .db     $00, $00, $00, $00, $00, $00, $00, $00
        .db     $00, $00, $00, $00, $00, $00, $00, $00

; $4950 - Type 4, Index 6 - Bird Music (Channel B)
        .db     $80, $82, $F1, $F2, $0C, $FE, $90, $FA
        .db     $00, $55, $83, $FE, $81, $57, $82, $55
        .db     $82, $57, $83, $FE, $81, $58, $83, $FE
        .db     $81, $60, $83, $FE, $81, $61, $82, $60
        .db     $82, $58, $83, $FE, $81, $60, $83, $FE
        .db     $81, $61, $81, $FE, $81, $65, $81, $FE
        .db     $81, $65, $82, $68, $82, $67, $82, $65
        .db     $82, $61, $83, $FE, $81, $60, $90, $FB
        .db     $FE, $FF, $00, $00, $00, $00, $00, $00
        .db     $00, $00, $00, $00, $00, $00, $00, $00

; $49A0 - Type 4, Index 6 - Bird Music (Channel C)
        .db     $80, $82, $F1, $F2, $0C, $FE, $A0, $FA
        .db     $00, $25, $83, $FE, $81, $27, $82, $25
        .db     $82, $27, $83, $FE, $81, $28, $83, $FE
        .db     $81, $30, $83, $FE, $81, $31, $82, $30
        .db     $82, $28, $83, $FE, $81, $30, $83, $FE
        .db     $81, $31, $81, $FE, $81, $35, $81, $FE
        .db     $81, $35, $82, $38, $82, $37, $82, $35
        .db     $82, $31, $83, $FE, $81, $30, $87, $FE
        .db     $81, $30, $82, $2A, $82, $28, $82, $27
        .db     $82, $FB, $F3, $09, $20, $00, $25, $90
        .db     $FE, $FF, $00, $00, $00, $00, $00, $00
        .db     $00, $00, $00, $00, $00, $00, $00, $00
        
; $4A00 - Type 4, Index 6 - Bird Music (Sample)
		.db     $80, $F5, $0E, $F6, $B0, $FA, $0A, $F7
        .db     $30, $3F, $82, $F8, $84, $F7, $30, $3F
        .db     $82, $F8, $82, $F7, $30, $3F, $82, $F8
        .db     $88, $FB, $FF, $00, $00, $00, $00, $00

; $4A20 - Type 3, Index 4 - Bird Poop Sound (Sample)
        .db     $80, $F5, $0E, $F6, $B0, $F7, $30, $3F
        .db     $82, $F8, $88, $F6, $B4, $F7, $28, $3F
        .db     $82, $F8, $90, $FF, $00, $00, $00, $00
        .db     $00, $00, $00, $00, $00, $00, $00, $00

; $4A40 - Type 4, Index 1 - King Kong Music (Channel A)
        .db     $80, $F1, $F2, $0C, $FA, $02, $43, $83
        .db     $FE, $81, $F3, $09, $20, $00, $44, $8C
        .db     $F2, $0C, $46, $83, $FE, $81, $F3, $09
        .db     $20, $00, $47, $8C, $F2, $0C, $43, $83
        .db     $FE, $81, $44, $83, $FE, $82, $46, $83
        .db     $FE, $81, $47, $83, $FE, $82, $50, $83
        .db     $FE, $81, $4B, $87, $FE, $81, $4A, $84
        .db     $FE, $81, $FB, $FF, $00, $00, $00, $00

; $4A80 - Type 4, Index 1 - King Kong Music (Channel B)
        .db     $80, $F1, $F3, $09, $20, $00, $FA, $02
        .db     $2A, $F9, $84, $2B, $F9, $8C, $21, $F9
        .db     $84, $22, $F9, $8C, $2A, $F9, $84, $2B
        .db     $F9, $84, $21, $F9, $84, $22, $F9, $85
        .db     $27, $F9, $84, $26, $F9, $88, $2A, $F9
        .db     $86, $FB, $FF, $00, $00, $00, $00, $00
        .db     $00, $00, $00, $00, $00, $00, $00, $00
        .db     $00, $00, $00, $00, $00, $00, $00, $00

; $4AC0 - Type 4, Index 1 - King Kong Music (Channel C)
        .db     $80, $F1, $F2, $0C, $FA, $02, $33, $83
        .db     $FE, $81, $34, $88, $FE, $84, $36, $83
        .db     $FE, $81, $37, $88, $FE, $84, $33, $83
        .db     $FE, $81, $34, $83, $FE, $81, $36, $83
        .db     $FE, $81, $37, $83, $FE, $82, $40, $83
        .db     $FE, $81, $3B, $87, $FE, $81, $3A, $84
        .db     $FE, $82, $FB, $FF

; $4AF4 - Type 3, Index 5 - King Kong chirp sound (Sample)		
; $4AF4 - Type 4, Index 1 - King Kong Music (Sample)		
		.db     $80, $F5, $0E, $F6
        .db     $60, $F7, $30, $3F, $82, $F8, $A0, $FF
        .db     $80, $FE, $FF, $FF, $00, $00, $00, $00
        .db     $00, $00, $00, $00, $00, $00, $00, $00

; $4B10 - Type 2, Index 0 - Helicopter (Channel A)
; $4B10 - Type 2, Index 0 - Helicopter (Channel B)
        .db     $80, $F1, $F2, $0C, $FE, $80, $FA, $FF
        .db     $21, $82, $1A, $81, $18, $81, $21, $81
        .db     $FE, $81, $1A, $81, $18, $81, $FB, $FE
        .db     $FF, $00, $00, $00, $00, $00, $00, $00

; $4B30 - Type 4, Index 2 - End building 1 (Channel A)
        .db     $80, $8C, $F1, $F2, $0C, $FC, $01, $FA
        .db     $01, $45, $83, $FE, $81, $45, $83, $FE
        .db     $81, $45, $83, $FE, $81, $45, $83, $FE
        .db     $81, $45, $82, $44, $82, $45, $83, $FE
        .db     $81, $46, $83, $FE, $81, $45, $83, $FE
        .db     $81, $FB, $FA, $01, $46, $82, $45, $82
        .db     $46, $83, $FE, $81, $47, $83, $FE, $81
        .db     $48, $83, $FE, $81, $FB, $51, $88, $FE
        .db     $88, $FD, $FF, $00, $00, $00, $00, $00
        .db     $00, $00, $00, $00, $00, $00, $00, $00

; $4B80 - Type 4, Index 2 - End building 1 (Channel B)
        .db     $80, $8C, $F1, $F2, $0C, $FC, $01, $FA
        .db     $03, $21, $84, $1A, $82, $18, $82, $21
        .db     $83, $FE, $81, $1A, $82, $18, $82, $FB
        .db     $FA, $01, $26, $82, $25, $82, $26, $83
        .db     $FE, $81, $27, $83, $FE, $81, $28, $83
        .db     $FE, $81, $FB, $31, $88, $FE, $82, $FE
        .db     $82, $FE, $82, $FE, $82, $FD, $FE, $FF
        .db     $00, $00, $00, $00, $00, $00, $00, $00

; $4BC0 - Type 4, Index 2 - End building 1 (Channel C)
        .db     $80, $8C, $F1, $FC, $01, $FA, $03, $F3
        .db     $09, $20, $00, $21, $90, $FB, $FA, $03
        .db     $FE, $90, $FB, $FD, $FF, $00, $00, $00
        .db     $00, $00, $00, $00, $00, $00, $00, $00

; $4BE0 - Type 4, Index 2 - End building 1 (Sample)
        .db     $80, $F5, $0E, $F6, $80, $F7, $80, $BF
        .db     $82, $F8, $F8, $92, $F5, $0E, $F6, $C0
        .db     $FA, $0D, $F7, $F8, $FF, $82, $F8, $88
        .db     $F7, $70, $7F, $82, $F8, $88, $FB, $FF

; $4C00 - Type 4, Index 3 - End building 2 (Channel A)
        .db     $88, $F1, $F2, $0E, $FA, $02, $FE, $82
        .db     $42, $82, $43, $82, $44, $82, $50, $84
        .db     $44, $82, $50, $84, $44, $82, $50, $87
        .db     $FE, $81, $50, $82, $52, $82, $53, $82
        .db     $54, $82, $50, $82, $52, $82, $54, $84
        .db     $4B, $82, $52, $84, $50, $84, $FE, $84
        .db     $FB, $FF, $90, $FB, $FD, $FF, $00, $00

; $4C38 - Type 4, Index 3 - End building 2 (Channel B)
        .db     $88, $F1, $F1, $F2, $0E, $FA, $02, $FE
        .db     $82, $27, $84, $30, $84, $34, $84, $30
        .db     $84, $37, $84, $35, $84, $39, $84, $30
        .db     $84, $34, $84, $37, $82, $2B, $84, $32
        .db     $82, $2B, $84, $30, $84, $FE, $84, $FB
        .db     $FF, $00, $00, $00, $00, $00, $00, $00

; $4C68 - Type 4, Index 3 - End building 2 (Channel C)
        .db     $88, $F1, $F2, $08, $FA, $02, $FE, $82
        .db     $2B, $84, $FE, $84, $27, $84, $FE, $84
        .db     $30, $84, $FE, $84, $30, $84, $FE, $84
        .db     $30, $84, $27, $82, $1B, $84, $22, $82
        .db     $1B, $84, $20, $84, $FE, $84, $FB, $FF

; $4C90 - Type 4, Index 3 - End building 2 (Sample)
        .db     $80, $F5, $0E, $F6, $80, $FA, $00, $F7
        .db     $80, $BF, $82, $F8, $FB, $FF, $00, $00

; $4CA0 - Type 4, Index 7 - Player Falling (Channel A)
        .db     $88, $F1, $F2, $0C, $FE, $82, $FA, $01
        .db     $40, $82, $3B, $82, $39, $82, $37, $82
        .db     $FB, $F3, $09, $20, $00, $40, $FF, $00
        .db     $00, $00, $00, $00, $00, $00, $00, $00

; $4CC0 - Type 4, Index 7 - Player Falling (Channel B)
        .db     $88, $F1, $F2, $0C, $FE, $86, $FA, $01
        .db     $39, $82, $37, $82, $35, $82, $34, $82
        .db     $FB, $F3, $09, $20, $00, $39, $FF, $00
        .db     $00, $00, $00, $00, $00, $00, $00, $00

; $4CE0 - Type 4, Index 7 - Player Falling (Channel C)
        .db     $88, $F1, $F2, $0C, $FE, $8A, $FA, $01
        .db     $35, $82, $34, $82, $32, $82, $30, $82
        .db     $FB, $F3, $09, $20, $00, $35, $FF, $00
        .db     $00, $00, $00, $00, $00, $00, $00, $00

; $4D00 - Type 4, Index 7 - Player Falling (Oh No!!) (Sample)
        .db     $84, $F5, $0E, $F6, $50, $F7, $C0, $FF
        .db     $82, $F8, $FF, $00, $00, $00, $00, $00

; $4D10 - Type 3, Index 3 - Hit by dumbell (Sample)
        .db     $80, $F5, $0E, $F6, $00, $F7, $70, $7F
        .db     $82, $F8, $FF, $00, $00, $00, $00, $00

; $4D20 - Type 2, Index 1 - Balloon Music (Channel A)
        .db     $80, $F1, $F2, $0C, $FC, $01, $FA, $01
        .db     $34, $38, $3B, $44, $2B, $33, $36, $3B
        .db     $31, $34, $38, $41, $28, $2B, $33, $38
        .db     $29, $31, $34, $39, $21, $24, $28, $34
        .db     $26, $29, $34, $39, $2B, $33, $36, $3B
        .db     $FB, $F3, $09, $FF, $FF, $FD, $FE, $FF

; $4D50 - Type 2, Index 1 - Balloon Music (Channel B)
        .db     $80, $F1, $F2, $0C, $FC, $01, $FA, $01
        .db     $21, $84, $18, $84, $19, $84, $14, $84
        .db     $16, $84, $11, $84, $16, $84, $18, $84
        .db     $FB, $F3, $09, $FF, $FF, $FD, $FE, $FF

; $4D70 - Type 4, Index 8 - Caught Balloon (Channel A)
        .db     $81, $F1, $F2, $0C, $FA, $01, $39, $84
        .db     $FE, $82, $42, $FE, $42, $84, $FE, $82
        .db     $46, $FE, $4B, $84, $FE, $82, $46, $FE
        .db     $49, $84, $FE, $82, $FE, $82, $49, $84
        .db     $FE, $82, $4B, $FE, $49, $84, $FE, $82
        .db     $46, $FE, $47, $84, $FE, $82, $46, $FE
        .db     $44, $84, $FE, $82, $FE, $82, $3B, $84
        .db     $FE, $82, $44, $FE, $44, $84, $FE, $82
        .db     $47, $FE, $51, $84, $FE, $82, $51, $FE
        .db     $4B, $84, $FE, $82, $49, $FE, $47, $84
        .db     $FE, $82, $47, $FE, $46, $84, $FE, $82
        .db     $44, $FE, $41, $86, $FE, $82, $44, $86
        .db     $FE, $82, $42, $8E, $FE, $82, $FB, $FF
        .db     $00, $00, $00, $00, $00, $00, $00, $00

; $4DE0 - Type 4, Index 8 - Caught Balloon (Channel B)
        .db     $81, $F1, $F2, $0C, $FA, $01, $39, $84
        .db     $FE, $82, $36, $84, $FE, $84, $32, $84
        .db     $FE, $84, $32, $84, $FE, $84, $36, $FE
        .db     $39, $84, $FE, $82, $36, $84, $FE, $84
        .db     $32, $84, $FE, $84, $31, $84, $FE, $84
        .db     $31, $FE, $37, $84, $FE, $82, $2B, $84
        .db     $FE, $84, $2B, $84, $FE, $84, $31, $84
        .db     $FE, $84, $31, $84, $FE, $84, $34, $84
        .db     $FE, $84, $28, $84, $FE, $84, $31, $84
        .db     $FE, $84, $31, $FE, $36, $8E, $FE, $82
        .db     $FB, $FF, $00, $00, $00, $00, $00, $00

; $4E38 - Type 4, Index 8 - Caught Balloon (Channel C)
        .db     $80, $F1, $FE, $F3, $09, $20, $00, $FA
        .db     $01, $1B, $F9, $88, $19, $F9, $88, $17
        .db     $F9, $88, $16, $F9, $88, $1B, $F9, $88
        .db     $16, $F9, $88, $21, $F9, $88, $16, $F9
        .db     $88, $21, $F9, $88, $11, $F9, $88, $16
        .db     $F9, $88, $16, $F9, $88, $21, $F9, $88
        .db     $11, $F9, $88, $16, $F9, $88, $16, $F9
        .db     $88, $1B, $F9, $88, $0B, $F9, $88, $FB
        .db     $12, $F9, $88, $FE, $FF, $00, $00, $00

; $4E80 - Type 3, Index 6 - Electric sign spark (Sample)
        .db     $80, $F5, $0F, $F6, $F0, $FA, $02, $F7
        .db     $70, $7F, $82, $F8, $84, $FB, $FF, $00

; $4E90 - Type 3, Index 7 - Electric sign shocking player (Sample)
        .db     $80, $F5, $0F, $F6, $A0, $F7, $30, $3F
        .db     $82, $F8, $88, $FE, $FF, $00, $00, $00

; $4EA0 - Type 4, Index 4 - End building 3 (Channel A)
        .db     $80, $F1, $F2, $0C, $FA, $01, $FE, $32
        .db     $36, $3B, $39, $36, $42, $32, $36, $41
        .db     $32, $36, $3B, $32, $36, $39, $32, $36
        .db     $39, $2B, $34, $37, $2B, $36, $37, $2B
        .db     $34, $2B, $34, $37, $FE, $31, $34, $39
        .db     $37, $34, $41, $31, $34, $3B, $31, $34
        .db     $39, $31, $34, $37, $31, $34, $37, $29
        .db     $32, $36, $29, $35, $36, $29, $32, $29
        .db     $FE, $FE, $FB, $FF, $00, $00, $00, $00

; $4EE8 - Type 4, Index 4 - End building 3 (Channel B)
        .db     $80, $F1, $F2, $0C, $FA, $01, $FE, $86
        .db     $26, $83, $29, $83, $26, $83, $29, $83
        .db     $1B, $83, $27, $83, $17, $86, $21, $84
        .db     $FE, $82, $21, $83, $27, $83, $21, $83
        .db     $27, $83, $26, $83, $21, $83, $26, $83
        .db     $29, $2B, $31, $FB, $FE, $FF, $F9, $82
        .db     $32, $F9, $82, $2B, $F9, $82, $37, $F9
        .db     $84, $21, $F9, $82, $27, $F9, $82, $34
        .db     $F9, $82, $27, $F9, $82, $24, $F9, $82
        .db     $31, $F9, $82, $37, $F9, $82, $31, $F9
        .db     $82, $26, $F9, $82, $31, $F9, $82, $39
        .db     $F9, $82, $31, $F9, $82, $FB, $FF, $00
        
; $4F48 - Type 4, Index 3 - End of building 3 (Channel C)
		.db     $80, $F1, $F2, $08, $FA, $01, $FE, $8C
        .db     $31, $83, $FE, $83, $31, $83, $FE, $83
        .db     $2B, $83, $FE, $86, $FE, $86, $2B, $83
        .db     $FE, $83, $2B, $83, $FE, $8C, $FB, $FE
        .db     $FF, $39, $F9, $82, $32, $F9, $82, $27
        .db     $F9, $82, $32, $F9, $82, $3B, $F9, $82
        .db     $32, $F9, $82, $2B, $F9, $82, $37, $F9
        .db     $84, $21, $F9, $82, $27, $F9, $82, $34
        .db     $F9, $82, $27, $F9, $82, $24, $F9, $82
        .db     $31, $F9, $82, $37, $F9, $82, $31, $F9
        .db     $82, $26, $F9, $82, $31, $F9, $82, $39
        .db     $F9, $82, $31, $F9, $82, $FB, $FF, $00

; $4FA8 - Type 4, Index 4 - End of building 3 (Sample)
; $4FA8 - Type 4, Index 8 - Caught Balloon (Sample)
        .db     $80, $F5, $0E, $F6, $80, $F7, $80, $BF
        .db     $82, $F8, $FF, $00, $00, $00, $00, $00

; $4FB8 - Type 4, Index 9 - Falling Sign (Channel A)
        .db     $80, $F1, $F3, $09, $30, $00, $20, $FF

; $4FC0 - Type 4, Index 9 - Falling Sign (Channel B)
        .db     $80, $F1, $F3, $09, $30, $00, $22, $FF

; $4FC8 - Type 4, Index 9 - Falling Sign (Channel C)
        .db     $80, $F1, $F3, $09, $30, $00, $24, $FF

; $4FD0 - Type 4, Index 9 - Falling Sign (Sample)
        .db     $80, $F5, $0E, $F6, $00, $F7, $70, $7F
        .db     $82, $F8, $FF, $00, $00, $00, $00, $00

; $4FE0 - Type 1, Index 0 - Add a life (Channel B)
        .db     $80, $F1, $FA, $07, $F3, $09, $10, $00
        .db     $60, $90, $FB, $FF, $00, $00, $00, $00
    
; $4FF0 - Type 1, Index 0 - Add a life (Channel C)
	    .db     $80, $F1, $FA, $07, $F3, $09, $10, $00
        .db     $62, $90, $FB, $FF, $00, $00


        .db     $C7, $F3		; End data block


.end		; End crazy climber source
