._CPU = 6809

.SAM_ALL_RAM = 0xFFDE

; Tape access (ZSAVE, ZLOAD) from C192 - C1F4

0xC12E:
        LDU     #StartObjs

0xC192: ; Doesn't matter ... it is relocatable

        LDX     #ALLRAM           ; ALLRAM routine
        LDU     #0x400            ; Start of screen memory
        LDY     #StartObjs-ALLRAM ; Number of bytes to copy
Copy1:
        LDA     ,X+            ; Copy the ...
        STA     ,U+            ; ... ALLRAM ...
        LEAY    -1,Y           ; ... to ...
        BNE     Copy1          ; ... RAM (on the screen)
        JMP     0x400          ; Execute the ALLRAM and return

ALLRAM:
        PSHS    CC             ; Save interrupt status
        ORCC    #0x50          ; Turn off interrupts
        LDX     #0x8000        ; Start of ROM
AR_1:
        STA     SAM_ALL_RAM    ; Switch ROM bank ON
        LDA     ,X             ; Get value from ROM
        STA     SAM_ALL_RAM+1  ; Switch ROM bank OFF
        STA     ,X+            ; Store value to RAM under ROM bank
        CMPX    #0xFF00        ; Reached the end of ROM?
        BNE     AR_1           ; No ... go back for more
        PULS    CC             ; Restore interrupts
        RTS

; Start with a variety of objects. Use them for fun or drop them for the "real" experience.

StartObjs:

        .byte 0x11 ; Wooden sword
        .byte 0x0F ; Pine torch
        ;
        .byte 0x02 ; Elvish sword
        .byte 0x03 ; Mithril shield
        .byte 0x04 ; Seer scroll
        .byte 0x05 ; Thews flask
        .byte 0x05 ; Thews flask
        .byte 0x05 ; Thews flask
        .byte 0x05 ; Thews flask
        .byte 0x0A ; Solar torch
        ;
        .byte 0xFF
