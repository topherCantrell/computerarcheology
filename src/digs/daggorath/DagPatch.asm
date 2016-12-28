
; Assembled all-RAM code
;
;E02C: 34 01      PSHS    CC             ; Save interrupt status
;E02E: 1A 50      ORCC    #0x50          ; Turn off interrupts
;E030: 8E 80 00   LDX     #0x8000        ; Start of ROM
;E033: B7 FF DE   STA     $FFDE          ; Switch ROM bank ON
;E036: A6 84      LDA     ,X             ; Get value from ROM
;E038: B7 FF DF   STA     $FFDF          ; Switch ROM bank OFF
;E03B: A7 80      STA     ,X+            ; Store value to RAM under ROM bank
;E03D: 8C FF 00   CMPX    #0xFF00        ; Reached the end of ROM?
;E040: 26 F1      BNE     $E033          ; No ... go back for more
;E042: 35 01      PULS    CC             ; Restore interrupts
;E044: 39         RTS                    ; Back to caller


; All of the cassette save/load is from D7B7 - D7D4
; You can use this area if you never type ZSAVE and ZLOAD

D7B7: 34 01 1A 50 8E 80 00 B7 FF DE A6 84 B7 FF DF A7 80 8C FF 00 26 F1 35 01 39

C130: D5 ; from D9 to D5 (use demo list in game play)
D7D7: 04 ; from 10 to 04 (seer scroll in demo objects)
D0F8: 21 ; from 8D to 21 (skip moving creatures)
D101: 21 ; from 8D to 21 (skip moving creatures)
D091: 20 ; from 2B to 20 (skip hitting player)
