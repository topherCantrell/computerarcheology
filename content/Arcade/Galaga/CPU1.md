![CPU1 (Main)](Galaga.jpg)

# CPU1

>>> cpu Z80

>>> binary 0000:roms/3200a.bin + roms/3300b.bin + roms/3400c.bin + roms/3500d.bin

```code
; 3N + 3M + 3L + 3K

;======================================================================
0000: 3E 10           LD      A,$10               ; Send command ...
0002: 32 00 71        LD      ($7100),A           ; ... to IO processor
0005: C3 C4 02        JP      $02C4               ; {} Continue
;======================================================================
; Add A*2 to HL.
; If A=0, add 0x100 to HL
0008: 87              ADD     A,A                 ; A*2
0009: 30 05           JR      NC,$10              ; {} Not a special
000B: 24              INC     H                   ; Else HL+=0x100
000C: C3 10 00        JP      $0010               ; {} Continue
000F: FF              RST     0X38                ; Filler
;======================================================================
; Add A to HL
0010: 85              ADD     A,L                 ; Add offset to HL ...
0011: 6F              LD      L,A                 ; ... LSB
0012: D0              RET     NC                  ; No overflow
0013: 24              INC     H                   ; Else add in overvlow
0014: C9              RET                         ; Out
0015: FF              RST     0X38                ; Filler
0016: FF              RST     0X38                ; Filler
0017: FF              RST     0X38                ; Filler
;======================================================================
; Fill buffer with value in A HL = pointer B = length
0018: 77              LD      (HL),A              ; Fill byte in buffer
0019: 23              INC     HL                  ; Next byte
001A: 10 FC           DJNZ    $18                 ; {} Do until done
001C: C9              RET                         ; Done
001D: FF              RST     0X38                ; Filler
001E: FF              RST     0X38                ; Filler
001F: FF              RST     0X38                ; Filler
;======================================================================
; Subtract 0x20 from DE
; Subtracting 20 moves to the right one character on the screen
0020: 7B              LD      A,E                 ; LSB
0021: D6 20           SUB     $20                 ; Subtract 0x20
0023: 5F              LD      E,A                 ; Back to LSB
0024: D0              RET     NC                  ; No overflow
0025: 15              DEC     D                   ; Else borrow
0026: C9              RET                         ; Done
0027: FF              RST     0X38                ; Filler
;======================================================================
; Clear 0xF0 bytes starting at 9100 (bee space)
0028: 21 00 91        LD      HL,$9100            ; Bee space
002B: 06 F0           LD      B,$F0               ; Count
002D: AF              XOR     A                   ; Clear value
002E: DF              RST     0X18                ; Clear the bee buffer
002F: C9              RET                         ; Done
;======================================================================
0030: 37              SCF                         ; Set carry flag
0031: 08              EX      AF,AF'              ; Switch register bank
0032: C3 B5 13        JP      $13B5               ; {}
0035: FF              RST     0X38                ; Filler
0036: FF              RST     0X38                ; Filler
0037: FF              RST     0X38                ; Filler
;======================================================================
; Interrupt comes here
0038: C3 37 02        JP      $0237               ; {} Revector interrupt

;======================================================================
003B: E9              JP      (HL)                ; Indirection to HL

;======================================================================
; Clear 80 byte buffers at 9300 and 9B00
; Fill 8800 80 bytes with #80
; (All sprites available, all shot slots available)
003C: 21 00 93        LD      HL,$9300            ; Clear ...
003F: 06 80           LD      B,$80               ; ... 0x80 bytes ...
0041: AF              XOR     A                   ; ... starting at ...
0042: DF              RST     0X18                ; ... 9300
0043: 21 00 9B        LD      HL,$9B00            ; 
0046: 06 80           LD      B,$80               ; 
0048: DF              RST     0X18                ; 
0049: 21 00 88        LD      HL,$8800            ; 
004C: 3E 80           LD      A,$80               ; 
004E: 06 80           LD      B,$80               ; 
0050: DF              RST     0X18                ; 
0051: C9              RET                         ; 

0052: FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0060: FF FF FF FF FF FF

;======================================================================
; An interrupt comes here
0066: D9              EXX                         ; Switch to our bank
0067: ED A0           LDI                         ; Block load (backwards)
0069: EA 8F 00        JP      PE,$008F            ; {}
006C: F5              PUSH    AF                  ; 
006D: 21 00 71        LD      HL,$7100            ; 
0070: 36 10           LD      (HL),$10            ; 
0072: 3A B9 9A        LD      A,($9AB9)           ; 
0075: A7              AND     A                   ; 
0076: 28 16           JR      Z,$8E               ; {}
0078: AF              XOR     A                   ; 
0079: 32 B9 9A        LD      ($9AB9),A           ; 
007C: 21 92 00        LD      HL,$0092            ; 
007F: 11 00 70        LD      DE,$7000            ; 
0082: 01 04 00        LD      BC,$0004            ; 
0085: D9              EXX                         ; 
0086: 3E A8           LD      A,$A8               ; 
0088: 32 00 71        LD      ($7100),A           ; 
008B: F1              POP     AF                  ; 
008C: ED 45           RETN                        ; 
008E: F1              POP     AF                  ; 
008F: D9              EXX                         ; Switch bank back out
0090: ED 45           RETN                        ; 

0092: 10 10       ; # What in the world ...
0094: 20 20       ; # ... are these?

; Play functions called from ISR
0096: 3A 08       ;00:RET
0098: 3B 08       ;01:Draw player
009A: B2 17       ;02:?
009C: 00 17       ;03:? 
009E: 86 1A       ;04:?
00A0: 6A 08       ;05:?
00A2: 3A 08       ;06:RET
00A4: 3A 08       ;07:RET
00A6: 24 29       ;08:No bees come out on screen
00A8: EC 1D       ;09:No bees come out on screen
00AA: 9E 2A       ;0A:Explosion sequence for dead bee
00AC: B9 1D       ;0B:Bees freeze when shot and when entering block formation
00AE: EB 23       ;0C:Bees freak out when they leave their initial spin
00B0: AA 1E       ;0D:MOVE BEE FIRE
00B2: 38 1D       ;0E:?
00B4: 48 09       ;0F:Bees never leave the block formation
00B6: 6B 1B       ;10:Start attack patterns 
00B8: B2 19       ;11:Pause game for "Fighter Captured" and handle fighter to top
00BA: 7C 1D       ;12:?
00BC: 3A 08       ;13:RET
00BE: 8B 1F       ;14:Move player left or right
00C0: 0A 1F       ;15:Initiate player fire
00C2: 3A 08       ;16:RET
00C4: D8 1D       ;17:?Display icon and STAGE message at start of wave?
00C6: 30 22       ;18:Initiate tractor beam
00C8: D9 21       ;19:?More of tractor beam?
00CA: 3A 08       ;1A:RET
00CC: 3A 08       ;1B:RET
00CE: F2 20       ;1C:Fighter becomes "captured"
00D0: 00 20       ;1D:Coordinate free-fighter sequence
00D2: 3A 08       ;1E:RET
00D4: 8A 09       ;1F:Process inputs (coins)

;======================================================================
00D6: 11 ED 83        LD      DE,$83ED            ; 
00D9: 21 B9 02        LD      HL,$02B9            ; 
00DC: 01 05 00        LD      BC,$0005            ; 
00DF: ED B0           LDIR                        ; 
00E1: 1E CB           LD      E,$CB               ; 
00E3: 21 EB 00        LD      HL,$00EB            ; 
00E6: 0E 11           LD      C,$11               ; 
00E8: ED B0           LDIR                        ; 
00EA: C9              RET                         ; 

00EB: 0E 1B           LD      C,$1B               ; #
00ED: 18 0C           JR      $FB                 ; {} #
00EF: 1C              INC     E                   ; #
00F0: 24              INC     H                   ; #
00F1: 11 10 12        LD      DE,$1210            ; #
00F4: 11 24 24        LD      DE,$2424            ; #
00F7: 24              INC     H                   ; #
00F8: 24              INC     H                   ; #
00F9: 19              ADD     HL,DE               ; #
00FA: 1E 01           LD      E,$01               ; #
00FC: FF              RST     0X38                ; #
00FD: FF              RST     0X38                ; #
00FE: FF              RST     0X38                ; #
00FF: FF              RST     0X38                ; #
;
0100: 14              INC     D                   ; #
0101: 06 14           LD      B,$14               ; #
0103: 0C              INC     C                   ; #
0104: 14              INC     D                   ; #
0105: 08              EX      AF,AF'              ; #
0106: 14              INC     D                   ; #
0107: 0A              LD      A,(BC)              ; #
0108: 1C              INC     E                   ; #
0109: 00              NOP                         ; #
010A: 1C              INC     E                   ; #
010B: 12              LD      (DE),A              ; #
010C: 1E 00           LD      E,$00               ; #
010E: 1E 12           LD      E,$12               ; #
0110: 1C              INC     E                   ; #
0111: 02              LD      (BC),A              ; #
0112: 1C              INC     E                   ; #
0113: 10 1E           DJNZ    $133                ; {} #
0115: 02              LD      (BC),A              ; #
0116: 1E 10           LD      E,$10               ; #
0118: 1C              INC     E                   ; #
0119: 04              INC     B                   ; #
011A: 1C              INC     E                   ; #
011B: 0E 1E           LD      C,$1E               ; #
011D: 04              INC     B                   ; #
011E: 1E 0E           LD      E,$0E               ; #
0120: 1C              INC     E                   ; #
0121: 06 1C           LD      B,$1C               ; #
0123: 0C              INC     C                   ; #
0124: 1E 06           LD      E,$06               ; #
0126: 1E 0C           LD      E,$0C               ; #
0128: 1C              INC     E                   ; #
0129: 08              EX      AF,AF'              ; #
012A: 1C              INC     E                   ; #
012B: 0A              LD      A,(BC)              ; #
012C: 1E 08           LD      E,$08               ; #
012E: 1E 0A           LD      E,$0A               ; #
0130: 16 06           LD      D,$06               ; #
0132: 16 0C           LD      D,$0C               ; #
0134: 16 08           LD      D,$08               ; #
0136: 16 0A           LD      D,$0A               ; #
0138: 18 00           JR      $13A                ; {} #
013A: 18 12           JR      $14E                ; {} #
013C: 1A              LD      A,(DE)              ; #
013D: 00              NOP                         ; #
013E: 1A              LD      A,(DE)              ; #
013F: 12              LD      (DE),A              ; #
0140: 18 02           JR      $144                ; {} #
0142: 18 10           JR      $154                ; {} #
0144: 1A              LD      A,(DE)              ; #
0145: 02              LD      (BC),A              ; #
0146: 1A              LD      A,(DE)              ; #
0147: 10 18           DJNZ    $161                ; {} #
0149: 04              INC     B                   ; #
014A: 18 0E           JR      $15A                ; {} #
014C: 1A              LD      A,(DE)              ; #
014D: 04              INC     B                   ; #
014E: 1A              LD      A,(DE)              ; #
014F: 0E 18           LD      C,$18               ; #
0151: 06 18           LD      B,$18               ; #
0153: 0C              INC     C                   ; #
0154: 1A              LD      A,(DE)              ; #
0155: 06 1A           LD      B,$1A               ; #
0157: 0C              INC     C                   ; #
0158: 18 08           JR      $162                ; {} #
015A: 18 0A           JR      $166                ; {} #
015C: 1A              LD      A,(DE)              ; #
015D: 08              EX      AF,AF'              ; #
015E: 1A              LD      A,(DE)              ; #
015F: 0A              LD      A,(BC)              ; #

0160: 21 40 80        LD      HL,$8040            ; 
0163: 11 41 80        LD      DE,$8041            ; 
0166: 01 7F 03        LD      BC,$037F            ; 
0169: 36 24           LD      (HL),$24            ; 
016B: ED B0           LDIR                        ; 
016D: 21 40 84        LD      HL,$8440            ; 
0170: 11 41 84        LD      DE,$8441            ; 
0173: 01 7F 03        LD      BC,$037F            ; 
0176: 36 00           LD      (HL),$00            ; 
0178: ED B0           LDIR                        ; 
017A: 3E 04           LD      A,$04               ; 
017C: 06 20           LD      B,$20               ; 
017E: DF              RST     0X18                ; 
017F: 3E 4E           LD      A,$4E               ; 
0181: 06 20           LD      B,$20               ; 
0183: DF              RST     0X18                ; 
0184: C9              RET                         ; 

0185: 21 21 98        LD      HL,$9821            ; 
0188: 34              INC     (HL)                ; 
0189: 7E              LD      A,(HL)              ; 
018A: 3C              INC     A                   ; 
018B: E6 03           AND     $03                 ; 
018D: 32 25 98        LD      ($9825),A           ; 
0190: 28 10           JR      Z,$1A2              ; {}
0192: 0E 06           LD      C,$06               ; 
0194: F7              RST     0X30                ; 
0195: EB              EX      DE,HL               ; 
0196: 3A 21 98        LD      A,($9821)           ; 
0199: 6F              LD      L,A                 ; 
019A: 26 00           LD      H,$00               ; 
019C: CD 66 0A        CALL    $0A66               ; {}
019F: AF              XOR     A                   ; 
01A0: 18 0A           JR      $1AC                ; {}
01A2: 0E 07           LD      C,$07               ; 
01A4: F7              RST     0X30                ; 
01A5: 3E 01           LD      A,$01               ; 
01A7: 32 AD 9A        LD      ($9AAD),A           ; 
01AA: 3E 08           LD      A,$08               ; 
01AC: 32 A8 92        LD      ($92A8),A           ; 
01AF: 3E 03           LD      A,$03               ; 
01B1: 32 AE 92        LD      ($92AE),A           ; 
01B4: 32 0B 92        LD      ($920B),A           ; Three shots!
01B7: 3A 25 98        LD      A,($9825)           ; 
01BA: A7              AND     A                   ; 
01BB: 08              EX      AF,AF'              ; 
01BC: CD 7F 11        CALL    $117F               ; {}
01BF: 3A AE 92        LD      A,($92AE)           ; 
01C2: A7              AND     A                   ; 
01C3: 20 FA           JR      NZ,$1BF             ; {}
01C5: 3E 78           LD      A,$78               ; 
01C7: 32 AE 92        LD      ($92AE),A           ; 
01CA: CD A4 28        CALL    $28A4               ; {}
01CD: CD B0 25        CALL    $25B0               ; {}
01D0: 3E 02           LD      A,$02               ; 
01D2: 32 AC 92        LD      ($92AC),A           ; 
01D5: AF              XOR     A                   ; 
01D6: CD D5 12        CALL    $12D5               ; {}
01D9: AF              XOR     A                   ; 
01DA: 06 30           LD      B,$30               ; 
01DC: 21 00 92        LD      HL,$9200            ; 
01DF: 77              LD      (HL),A              ; 
01E0: 2C              INC     L                   ; 
01E1: 2C              INC     L                   ; 
01E2: 10 FB           DJNZ    $1DF                ; {}
01E4: 32 09 90        LD      ($9009),A           ; 0's
01E7: 32 10 90        LD      ($9010),A           ; 
01EA: 32 04 90        LD      ($9004),A           ; 
01ED: 32 88 92        LD      ($9288),A           ; 
01F0: 32 2C 98        LD      ($982C),A           ; 
01F3: 32 41 98        LD      ($9841),A           ; 
01F6: 32 42 98        LD      ($9842),A           ; 
01F9: 32 26 98        LD      ($9826),A           ; 
01FC: 32 B0 99        LD      ($99B0),A           ; 
01FF: 32 24 98        LD      ($9824),A           ; 
0202: 3C              INC     A                   ; 
0203: 32 2D 98        LD      ($982D),A           ; 1's
0206: 32 6D 98        LD      ($986D),A           ; 
0209: 32 28 98        LD      ($9828),A           ; 
020C: 32 0B 90        LD      ($900B),A           ; 
020F: 32 08 90        LD      ($9008),A           ; 
0212: 32 0A 90        LD      ($900A),A           ; 
0215: CD 00 2C        CALL    $2C00               ; {}
0218: 21 30 98        LD      HL,$9830            ; 
021B: 11 B5 01        LD      DE,$01B5            ; 
021E: 06 04           LD      B,$04               ; 
0220: 72              LD      (HL),D              ; 
0221: 2C              INC     L                   ; 
0222: 73              LD      (HL),E              ; 
0223: 2C              INC     L                   ; 
0224: 10 FA           DJNZ    $220                ; {}
0226: 3A 05 68        LD      A,($6805)           ; 
0229: CB 4F           BIT     1,A                 ; 
022B: C0              RET     NZ                  ; 
022C: 0E 0B           LD      C,$0B               ; 
022E: 21 B0 83        LD      HL,$83B0            ; 
0231: CD B3 13        CALL    $13B3               ; {}
0234: C3 85 01        JP      $0185               ; {}

; Interrupt vectors here
0237: F5              PUSH    AF                  ; Save ...
0238: 08              EX      AF,AF'              ; ...
0239: F5              PUSH    AF                  ; ...
023A: C5              PUSH    BC                  ; ...
023B: D5              PUSH    DE                  ; ...
023C: E5              PUSH    HL                  ; ...
023D: DD E5           PUSH    IX                  ; ...
023F: FD E5           PUSH    IY                  ; ... Everyting
0241: 3A 04 68        LD      A,($6804)           ; Bit 5s
0244: 57              LD      D,A                 ; Hold it.
0245: 3A A0 92        LD      A,($92A0)           ; 
0248: E6 1C           AND     $1C                 ; 
024A: 4F              LD      C,A                 ; 
024B: 0F              RRCA                        ; 
024C: A9              XOR     C                   ; 
024D: E6 18           AND     $18                 ; 
024F: 4F              LD      C,A                 ; 
0250: 3A BE 99        LD      A,($99BE)           ; 
0253: CB 4A           BIT     1,D                 ; Rack test?
0255: 20 02           JR      NZ,$259             ; {} No
0257: 3E 07           LD      A,$07               ; If rack test, set all bits
0259: E6 07           AND     $07                 ; Mask all but lower
025B: B1              OR      C                   ; 
025C: 06 05           LD      B,$05               ; 
025E: 21 00 A0        LD      HL,$A000            ; 
0261: 77              LD      (HL),A              ; 
0262: 2C              INC     L                   ; 
0263: 0F              RRCA                        ; 
0264: 10 FB           DJNZ    $261                ; {}
0266: 32 30 68        LD      ($6830),A           ; Watchdog reset
0269: AF              XOR     A                   ; 0 will ...
026A: 32 20 68        LD      ($6820),A           ; ... disable interrupt
026D: CB 4A           BIT     1,D                 ; 
026F: CA A8 02        JP      Z,$02A8             ; {}
0272: 4F              LD      C,A                 ; 
0273: 21 00 90        LD      HL,$9000            ; 
0276: 79              LD      A,C                 ; 
0277: 85              ADD     A,L                 ; 
0278: 6F              LD      L,A                 ; 
0279: 7E              LD      A,(HL)              ; 
027A: A7              AND     A                   ; 
027B: 20 03           JR      NZ,$280             ; {}
027D: 0C              INC     C                   ; 
027E: 18 F3           JR      $273                ; {}
0280: 47              LD      B,A                 ; 
0281: 21 96 00        LD      HL,$0096            ; Jump table
0284: 79              LD      A,C                 ; 
0285: CB 27           SLA     A                   ; 
0287: 85              ADD     A,L                 ; 
0288: 6F              LD      L,A                 ; 
0289: 5E              LD      E,(HL)              ; 
028A: 23              INC     HL                  ; 
028B: 56              LD      D,(HL)              ; 
028C: EB              EX      DE,HL               ; 
028D: C5              PUSH    BC                  ; 
028E: CD 3B 00        CALL    $003B               ; {} Redirection to HL
0291: C1              POP     BC                  ; 
0292: 78              LD      A,B                 ; 
0293: 81              ADD     A,C                 ; 
0294: 4F              LD      C,A                 ; 
0295: E6 E0           AND     $E0                 ; 
0297: 28 DA           JR      Z,$273              ; {}
0299: 21 00 70        LD      HL,$7000            ; 
029C: 11 B5 99        LD      DE,$99B5            ; 
029F: 01 03 00        LD      BC,$0003            ; 
02A2: D9              EXX                         ; 
02A3: 3E 71           LD      A,$71               ; 
02A5: 32 00 71        LD      ($7100),A           ; 
02A8: 3E 01           LD      A,$01               ; 
02AA: 32 20 68        LD      ($6820),A           ; 
02AD: FD E1           POP     IY                  ; Pop ...
02AF: DD E1           POP     IX                  ; ...
02B1: E1              POP     HL                  ; ...
02B2: D1              POP     DE                  ; ...
02B3: C1              POP     BC                  ; ...
02B4: F1              POP     AF                  ; ...
02B5: 08              EX      AF,AF'              ; ...
02B6: F1              POP     AF                  ; ... Everything
02B7: FB              EI                          ; Enable interrups
02B8: C9              RET                         ; Done

02B9: 00              NOP                         ; 
02BA: 00              NOP                         ; 
02BB: 00              NOP                         ; 
02BC: 00              NOP                         ; 
02BD: 02              LD      (BC),A              ; 
02BE: 24              INC     H                   ; 
02BF: 17              RLA                         ; 
02C0: 0A              LD      A,(BC)              ; 
02C1: 16 0C           LD      D,$0C               ; 
02C3: 18          

; Initialization
02C4: ED 56           IM      1                   ; 
02C6: AF              XOR     A                   ; 
02C7: 21 E0 99        LD      HL,$99E0            ; 
02CA: 06 10           LD      B,$10               ; 
02CC: 77              LD      (HL),A              ; 
02CD: 23              INC     HL                  ; 
02CE: 10 FC           DJNZ    $2CC                ; {}
02D0: C3 6C 33        JP      $336C               ; {}
02D3: 31 A0 90        LD      SP,$90A0            ; 
02D6: AF              XOR     A                   ; 
02D7: 21 AC 92        LD      HL,$92AC            ; 
02DA: 06 04           LD      B,$04               ; 
02DC: DF              RST     0X18                ; 
02DD: 21 A0 9A        LD      HL,$9AA0            ; 
02E0: 06 20           LD      B,$20               ; 
02E2: DF              RST     0X18                ; 
02E3: 32 07 A0        LD      ($A007),A           ; 
02E6: 32 15 92        LD      ($9215),A           ; 
02E9: 32 B9 99        LD      ($99B9),A           ; 
02EC: 3D              DEC     A                   ; 
02ED: 21 CA 92        LD      HL,$92CA            ; 
02F0: 06 10           LD      B,$10               ; 
02F2: DF              RST     0X18                ; 
02F3: 3E 01           LD      A,$01               ; 
02F5: 32 20 68        LD      ($6820),A           ; 
02F8: 21 C0 83        LD      HL,$83C0            ; 
02FB: 06 40           LD      B,$40               ; 
02FD: 3E 24           LD      A,$24               ; 
02FF: DF              RST     0X18                ; 
0300: 26 80           LD      H,$80               ; 
0302: 06 40           LD      B,$40               ; 
0304: DF              RST     0X18                ; 
0305: 21 00 84        LD      HL,$8400            ; 
0308: 06 40           LD      B,$40               ; 
030A: 3E 03           LD      A,$03               ; 
030C: DF              RST     0X18                ; 
030D: CD 60 01        CALL    $0160               ; {}
0310: 11 20 8A        LD      DE,$8A20            ; 
0313: 3E 05           LD      A,$05               ; 
0315: 06 00           LD      B,$00               ; 
0317: 21 B9 02        LD      HL,$02B9            ; 
031A: 0E 06           LD      C,$06               ; 
031C: ED B0           LDIR                        ; 
031E: 3D              DEC     A                   ; 
031F: 20 F6           JR      NZ,$317             ; {}
0321: 21 BF 02        LD      HL,$02BF            ; 
0324: 3E 2A           LD      A,$2A               ; 
0326: 06 05           LD      B,$05               ; 
0328: 0E FF           LD      C,$FF               ; 
032A: ED A0           LDI                         ; 
032C: 2B              DEC     HL                  ; 
032D: 12              LD      (DE),A              ; 
032E: 1C              INC     E                   ; 
032F: ED A0           LDI                         ; 
0331: 10 F7           DJNZ    $32A                ; {}
0333: 3E 01           LD      A,$01               ; 
0335: 32 01 92        LD      ($9201),A           ; 
0338: 21 05 A0        LD      HL,$A005            ; 
033B: 36 00           LD      (HL),$00            ; 
033D: 77              LD      (HL),A              ; 
033E: CD 3C 00        CALL    $003C               ; {}
0341: CD D6 00        CALL    $00D6               ; {}
0344: CD 42 12        CALL    $1242               ; {}
0347: EF              RST     0X28                ; 
0348: 3E 20           LD      A,$20               ; 
034A: 32 1E 90        LD      ($901E),A           ; 
034D: 3A B5 99        LD      A,($99B5)           ; 
0350: 32 B8 99        LD      ($99B8),A           ; 
0353: AF              XOR     A                   ; 
0354: 32 1E 90        LD      ($901E),A           ; 
0357: 32 20 90        LD      ($9020),A           ; 
035A: AF              XOR     A                   ; 
035B: 32 07 A0        LD      ($A007),A           ; 
035E: 32 15 92        LD      ($9215),A           ; 
0361: 32 12 90        LD      ($9012),A           ; 
0364: 06 80           LD      B,$80               ; 
0366: 21 00 92        LD      HL,$9200            ; 
0369: DF              RST     0X18                ; 
036A: 3E 06           LD      A,$06               ; 
036C: 32 BE 99        LD      ($99BE),A           ; 
036F: EF              RST     0X28                ; 
0370: CD 3C 00        CALL    $003C               ; {}
0373: CD 42 12        CALL    $1242               ; {}
0376: 3A B8 99        LD      A,($99B8)           ; 
0379: A7              AND     A                   ; 
037A: 3E 01           LD      A,$01               ; 
037C: 28 02           JR      Z,$380              ; {}
037E: 3E 02           LD      A,$02               ; 
0380: 32 01 92        LD      ($9201),A           ; 
0383: 20 18           JR      NZ,$39D             ; {}
0385: AF              XOR     A                   ; 
0386: 32 03 92        LD      ($9203),A           ; 
0389: 3C              INC     A                   ; 
038A: 32 02 90        LD      ($9002),A           ; 
038D: 3A 01 92        LD      A,($9201)           ; 
0390: 3D              DEC     A                   ; 
0391: 28 FA           JR      Z,$38D              ; {}
0393: CD 42 12        CALL    $1242               ; {}
0396: CD 60 01        CALL    $0160               ; {}
0399: EF              RST     0X28                ; 
039A: CD 3C 00        CALL    $003C               ; {}
039D: AF              XOR     A                   ; 
039E: 32 0B 92        LD      ($920B),A           ; Disables fire
03A1: 0E 13           LD      C,$13               ; 
03A3: F7              RST     0X30                ; 
03A4: 0E 01           LD      C,$01               ; 
03A6: F7              RST     0X30                ; 
03A7: 21 52 04        LD      HL,$0452            ; 
03AA: 22 80 92        LD      ($9280),HL          ; 
03AD: 3A 80 99        LD      A,($9980)           ; 
03B0: FE FF           CP      $FF                 ; 
03B2: 28 24           JR      Z,$3D8              ; {}
03B4: 5F              LD      E,A                 ; 
03B5: 0E 1B           LD      C,$1B               ; 
03B7: CD 3D 04        CALL    $043D               ; {}
03BA: 3A 81 99        LD      A,($9981)           ; 
03BD: FE FF           CP      $FF                 ; 
03BF: 28 17           JR      Z,$3D8              ; {}
03C1: E6 7F           AND     $7F                 ; 
03C3: 5F              LD      E,A                 ; 
03C4: 0E 1C           LD      C,$1C               ; 
03C6: CD 3D 04        CALL    $043D               ; {}
03C9: 3A 81 99        LD      A,($9981)           ; 
03CC: CB 7F           BIT     7,A                 ; 
03CE: 20 08           JR      NZ,$3D8             ; {}
03D0: E6 7F           AND     $7F                 ; 
03D2: 5F              LD      E,A                 ; 
03D3: 0E 1D           LD      C,$1D               ; 
03D5: CD 3D 04        CALL    $043D               ; {}
03D8: 3A 01 92        LD      A,($9201)           ; 
03DB: FE 02           CP      $02                 ; 
03DD: 28 F9           JR      Z,$3D8              ; {}
03DF: 32 B7 9A        LD      ($9AB7),A           ; 
03E2: CD 60 01        CALL    $0160               ; {}
03E5: CD 3C 00        CALL    $003C               ; {}
03E8: 21 05 A0        LD      HL,$A005            ; 
03EB: 36 00           LD      (HL),$00            ; 
03ED: 36 01           LD      (HL),$01            ; 
03EF: 21 20 98        LD      HL,$9820            ; 
03F2: AF              XOR     A                   ; 
03F3: 06 A0           LD      B,$A0               ; 
03F5: DF              RST     0X18                ; 
03F6: 32 B7 9A        LD      ($9AB7),A           ; 
03F9: 32 B9 99        LD      ($99B9),A           ; 
03FC: 3C              INC     A                   ; 
03FD: 32 AB 9A        LD      ($9AAB),A           ; 
0400: 32 12 90        LD      ($9012),A           ; 
0403: 32 F2 98        LD      ($98F2),A           ; 
0406: CD 66 04        CALL    $0466               ; {}
0409: CD 7B 12        CALL    $127B               ; {}
040C: 0E 04           LD      C,$04               ; 
040E: F7              RST     0X30                ; 
040F: 21 AF 92        LD      HL,$92AF            ; 
0412: 36 08           LD      (HL),$08            ; 
0414: 7E              LD      A,(HL)              ; 
0415: A7              AND     A                   ; 
0416: 20 FC           JR      NZ,$414             ; {}
0418: 21 90 92        LD      HL,$9290            ; 
041B: 06 10           LD      B,$10               ; 
041D: DF              RST     0X18                ; 
041E: 06 30           LD      B,$30               ; 
0420: 21 B0 98        LD      HL,$98B0            ; 
0423: DF              RST     0X18                ; 
0424: 21 B0 83        LD      HL,$83B0            ; 
0427: 0E 0B           LD      C,$0B               ; 
0429: CD B3 13        CALL    $13B3               ; {}
042C: 3E 01           LD      A,$01               ; 
042E: 32 80 98        LD      ($9880),A           ; 
0431: 3A 80 99        LD      A,($9980)           ; 
0434: 32 3E 98        LD      ($983E),A           ; 
0437: 32 7E 98        LD      ($987E),A           ; 

043A: C3 22 06        JP      $0622               ; {}
043D: F7              RST     0X30                ; 
043E: EB              EX      DE,HL               ; 
043F: 7B              LD      A,E                 ; 
0440: C6 40           ADD     $40                 ; 
0442: 5F              LD      E,A                 ; 
0443: 26 00           LD      H,$00               ; 

0445: CD 66 0A        CALL    $0A66               ; {}
0448: EB              EX      DE,HL               ; 
0449: 0E 1E           LD      C,$1E               ; 
044B: CD B3 13        CALL    $13B3               ; {}
044E: CD 9E 12        CALL    $129E               ; {}
0451: C9              RET                         ; 
0452: 00              NOP                         ; 
0453: 81              ADD     A,C                 ; 
0454: 19              ADD     HL,DE               ; 
0455: 56              LD      D,(HL)              ; 
0456: 02              LD      (BC),A              ; 
0457: 81              ADD     A,C                 ; 
0458: 19              ADD     HL,DE               ; 
0459: 62              LD      H,D                 ; 
045A: 04              INC     B                   ; 
045B: 81              ADD     A,C                 ; 
045C: 19              ADD     HL,DE               ; 
045D: 6E              LD      L,(HL)              ; 
045E: CD 3B 07        CALL    $073B               ; {}

0461: CD 1E 08        CALL    $081E               ; {}
0464: 18 F8           JR      $45E                ; {}
0466: 3A 00 68        LD      A,($6800)           ; 
0469: 4F              LD      C,A                 ; 
046A: 21 B3 99        LD      HL,$99B3            ; 
046D: 3A 82 99        LD      A,($9982)           ; 
0470: CB 46           BIT     0,(HL)              ; 
0472: 28 08           JR      Z,$47C              ; {}
0474: CB 49           BIT     1,C                 ; 
0476: 20 04           JR      NZ,$47C             ; {}
0478: 3C              INC     A                   ; 
0479: 87              ADD     A,A                 ; 
047A: 36 00           LD      (HL),$00            ; 
047C: 32 20 98        LD      ($9820),A           ; 
047F: 32 60 98        LD      ($9860),A           ; 
0482: 11 F8 83        LD      DE,$83F8            ; 
0485: 21 A8 04        LD      HL,$04A8            ; 
0488: CD 99 04        CALL    $0499               ; {}
048B: 11 E3 83        LD      DE,$83E3            ; 
048E: 21 A8 04        LD      HL,$04A8            ; 
0491: 3A B3 99        LD      A,($99B3)           ; 
0494: A7              AND     A                   ; 
0495: 20 02           JR      NZ,$499             ; {}
0497: 23              INC     HL                  ; 
0498: 23              INC     HL                  ; 
0499: 0E 07           LD      C,$07               ; 
049B: ED B0           LDIR                        ; 
049D: 21 AA 04        LD      HL,$04AA            ; 
04A0: 11 C3 83        LD      DE,$83C3            ; 
04A3: 0E 04           LD      C,$04               ; 
04A5: ED B0           LDIR                        ; 
04A7: C9              RET                         ; 

04A8: 00              NOP                         ; #
04A9: 00              NOP                         ; #
04AA: 24              INC     H                   ; #
04AB: 24              INC     H                   ; #
04AC: 24              INC     H                   ; #
04AD: 24              INC     H                   ; #
04AE: 24              INC     H                   ; #
04AF: 24              INC     H                   ; #
04B0: 24              INC     H                   ; #
04B1: E1              POP     HL                  ; #

04B2: 21 AF 92        LD      HL,$92AF            ; 
04B5: 36 04           LD      (HL),$04            ; 
04B7: 3A 1D 90        LD      A,($901D)           ; 
04BA: A7              AND     A                   ; 
04BB: 28 17           JR      Z,$4D4              ; {}
04BD: AF              XOR     A                   ; 
04BE: 32 13 92        LD      ($9213),A           ; 
04C1: 3C              INC     A                   ; 
04C2: 32 25 90        LD      ($9025),A           ; 
04C5: 3A A7 92        LD      A,($92A7)           ; 
04C8: A7              AND     A                   ; 
04C9: C2 5E 04        JP      NZ,$045E            ; {}
04CC: 3A 1D 90        LD      A,($901D)           ; 
04CF: A7              AND     A                   ; 
04D0: 20 FA           JR      NZ,$4CC             ; {}
04D2: 18 1B           JR      $4EF                ; {}
04D4: 7E              LD      A,(HL)              ; 
04D5: A7              AND     A                   ; 
04D6: 20 DF           JR      NZ,$4B7             ; {}
04D8: CD 3B 07        CALL    $073B               ; {}
04DB: 3A A7 92        LD      A,($92A7)           ; 
04DE: 32 43 98        LD      ($9843),A           ; 
04E1: 4F              LD      C,A                 ; 
04E2: 3A 13 92        LD      A,($9213)           ; 
04E5: B1              OR      C                   ; 
04E6: 20 0D           JR      NZ,$4F5             ; {}
04E8: 3A 25 98        LD      A,($9825)           ; 
04EB: A7              AND     A                   ; 
04EC: CA 63 06        JP      Z,$0663             ; {}
04EF: CD 85 01        CALL    $0185               ; {}
04F2: C3 45 06        JP      $0645               ; {}
04F5: 21 20 98        LD      HL,$9820            ; 
04F8: 7E              LD      A,(HL)              ; 
04F9: 35              DEC     (HL)                ; 
04FA: A7              AND     A                   ; 
04FB: C2 8C 05        JP      NZ,$058C            ; {}
04FE: 3A B3 99        LD      A,($99B3)           ; 
0501: A7              AND     A                   ; 
0502: 28 0C           JR      Z,$510              ; {}
0504: 21 4E 82        LD      HL,$824E            ; 
0507: 3A 40 98        LD      A,($9840)           ; 
050A: C6 04           ADD     $04                 ; 
050C: 4F              LD      C,A                 ; 
050D: CD B3 13        CALL    $13B3               ; {}
0510: 0E 02           LD      C,$02               ; 
0512: F7              RST     0X30                ; 
0513: CD 31 13        CALL    $1331               ; {}
0516: CD 31 13        CALL    $1331               ; {}
0519: 21 18 90        LD      HL,$9018            ; 
051C: 7E              LD      A,(HL)              ; 
051D: A7              AND     A                   ; 
051E: 20 FC           JR      NZ,$51C             ; {}
0520: EF              RST     0X28                ; 
0521: CD 3C 00        CALL    $003C               ; {}
0524: CD 60 01        CALL    $0160               ; {}
0527: 0E 15           LD      C,$15               ; 
0529: F7              RST     0X30                ; 
052A: 0E 16           LD      C,$16               ; 
052C: F7              RST     0X30                ; 
052D: 11 32 81        LD      DE,$8132            ; 
0530: 2A 46 98        LD      HL,($9846)          ; 
0533: CD 66 0A        CALL    $0A66               ; {}
0536: 0E 18           LD      C,$18               ; 
0538: F7              RST     0X30                ; 
0539: 11 35 81        LD      DE,$8135            ; 
053C: 2A 44 98        LD      HL,($9844)          ; 
053F: CD 66 0A        CALL    $0A66               ; {}
0542: 0E 19           LD      C,$19               ; 
0544: F7              RST     0X30                ; 
0545: CD 85 0A        CALL    $0A85               ; {}
0548: EB              EX      DE,HL               ; 
0549: 0E 1A           LD      C,$1A               ; 
054B: CD B3 13        CALL    $13B3               ; {}
054E: 21 AE 92        LD      HL,$92AE            ; 
0551: 36 0E           LD      (HL),$0E            ; 
0553: 7E              LD      A,(HL)              ; 
0554: A7              AND     A                   ; 
0555: 20 FC           JR      NZ,$553             ; {}
0557: CD 60 01        CALL    $0160               ; {}
055A: CD 00 30        CALL    $3000               ; {}
055D: AF              XOR     A                   ; 
055E: 32 B0 9A        LD      ($9AB0),A           ; 
0561: 21 AC 9A        LD      HL,$9AAC            ; 
0564: 11 B6 9A        LD      DE,$9AB6            ; 
0567: 1A              LD      A,(DE)              ; 
0568: 46              LD      B,(HL)              ; 
0569: B0              OR      B                   ; 
056A: 28 09           JR      Z,$575              ; {}
056C: 04              INC     B                   ; 
056D: 05              DEC     B                   ; 
056E: 28 02           JR      Z,$572              ; {}
0570: 36 01           LD      (HL),$01            ; 
0572: 76              HALT                        ; 
0573: 18 F2           JR      $567                ; {}
0575: CD 60 01        CALL    $0160               ; {}
0578: 3A B3 99        LD      A,($99B3)           ; 
057B: A7              AND     A                   ; 
057C: CA F1 06        JP      Z,$06F1             ; {} Halt
057F: 3A 60 98        LD      A,($9860)           ; 
0582: 3C              INC     A                   ; 
0583: CA F1 06        JP      Z,$06F1             ; {} Halt
0586: 3A 13 92        LD      A,($9213)           ; 
0589: 3D              DEC     A                   ; 
058A: 20 15           JR      NZ,$5A1             ; {}
058C: 3A B3 99        LD      A,($99B3)           ; 
058F: A7              AND     A                   ; 
0590: CA 17 06        JP      Z,$0617             ; {}
0593: 3A 60 98        LD      A,($9860)           ; 
0596: 3C              INC     A                   ; 
0597: CA 25 06        JP      Z,$0625             ; {}
059A: 3A 13 92        LD      A,($9213)           ; 
059D: 3D              DEC     A                   ; 
059E: C2 25 06        JP      NZ,$0625            ; {}
05A1: 3A A7 92        LD      A,($92A7)           ; 
05A4: A7              AND     A                   ; 
05A5: 28 06           JR      Z,$5AD              ; {}
05A7: 3A 87 92        LD      A,($9287)           ; 
05AA: A7              AND     A                   ; 
05AB: 20 FA           JR      NZ,$5A7             ; {}
05AD: AF              XOR     A                   ; 
05AE: 32 B4 99        LD      ($99B4),A           ; 
05B1: 3C              INC     A                   ; 
05B2: 21 0E 90        LD      HL,$900E            ; 
05B5: 77              LD      (HL),A              ; 
05B6: 7E              LD      A,(HL)              ; 
05B7: A7              AND     A                   ; 
05B8: 20 FC           JR      NZ,$5B6             ; {}
05BA: 3A A0 9A        LD      A,($9AA0)           ; 
05BD: 32 48 98        LD      ($9848),A           ; 
05C0: 3A AE 92        LD      A,($92AE)           ; 
05C3: 32 3F 98        LD      ($983F),A           ; 
05C6: CD 0C 11        CALL    $110C               ; {}
05C9: CD 00 2C        CALL    $2C00               ; {}
05CC: 3A 3F 98        LD      A,($983F)           ; 
05CF: 32 AE 92        LD      ($92AE),A           ; 
05D2: 3A 48 98        LD      A,($9848)           ; 
05D5: 32 A0 9A        LD      ($9AA0),A           ; 
05D8: CD 7E 13        CALL    $137E               ; {}
05DB: 3A 43 98        LD      A,($9843)           ; 
05DE: A7              AND     A                   ; 
05DF: 28 03           JR      Z,$5E4              ; {}
05E1: CD B0 25        CALL    $25B0               ; {}
05E4: 3A 40 98        LD      A,($9840)           ; 
05E7: 4F              LD      C,A                 ; 
05E8: 3A 83 99        LD      A,($9983)           ; 
05EB: A1              AND     C                   ; 
05EC: 32 07 A0        LD      ($A007),A           ; 
05EF: 32 15 92        LD      ($9215),A           ; 
05F2: 3E 3F           LD      A,$3F               ; 
05F4: CD D5 12        CALL    $12D5               ; {}
05F7: 37              SCF                         ; 
05F8: 08              EX      AF,AF'              ; 
05F9: CD 7F 11        CALL    $117F               ; {}
05FC: 3A 43 98        LD      A,($9843)           ; 
05FF: A7              AND     A                   ; 
0600: 28 20           JR      Z,$622              ; {}
0602: 0E 03           LD      C,$03               ; 
0604: F7              RST     0X30                ; 
0605: 3E 80           LD      A,$80               ; 
0607: 32 B4 99        LD      ($99B4),A           ; 
060A: 21 0E 90        LD      HL,$900E            ; 
060D: 3E 01           LD      A,$01               ; 
060F: 77              LD      (HL),A              ; 
0610: 7E              LD      A,(HL)              ; 
0611: A7              AND     A                   ; 
0612: 20 FC           JR      NZ,$610             ; {}
0614: C3 25 06        JP      $0625               ; {}
0617: 3A 43 98        LD      A,($9843)           ; 
061A: A7              AND     A                   ; 
061B: 20 14           JR      NZ,$631             ; {}
061D: CD 85 01        CALL    $0185               ; {}
0620: 18 0F           JR      $631                ; {}
0622: CD 85 01        CALL    $0185               ; {}
0625: 3A 40 98        LD      A,($9840)           ; 
0628: C6 04           ADD     $04                 ; 
062A: 4F              LD      C,A                 ; 
062B: 21 6E 82        LD      HL,$826E            ; 
062E: CD B3 13        CALL    $13B3               ; {}
0631: CD 3D 13        CALL    $133D               ; {}
0634: 3A AE 92        LD      A,($92AE)           ; 
0637: C6 1E           ADD     $1E                 ; 
0639: FE 78           CP      $78                 ; 
063B: 38 02           JR      C,$63F              ; {}
063D: 3E 78           LD      A,$78               ; 
063F: 32 AE 92        LD      ($92AE),A           ; 
0642: CD 31 13        CALL    $1331               ; {}
0645: 3E 01           LD      A,$01               ; 
0647: 32 15 90        LD      ($9015),A           ; 
064A: 32 25 90        LD      ($9025),A           ; 
064D: 32 42 98        LD      ($9842),A           ; 
0650: 0E 0B           LD      C,$0B               ; 
0652: 21 B0 83        LD      HL,$83B0            ; 
0655: CD B3 13        CALL    $13B3               ; {}
0658: 0E 0B           LD      C,$0B               ; 
065A: 21 AE 83        LD      HL,$83AE            ; 
065D: CD B3 13        CALL    $13B3               ; {}
0660: C3 5E 04        JP      $045E               ; {}
0663: 3A 88 92        LD      A,($9288)           ; 
0666: 5F              LD      E,A                 ; 
0667: 21 AE 9A        LD      HL,$9AAE            ; 
066A: FE 28           CP      $28                 ; 
066C: 20 03           JR      NZ,$671             ; {}
066E: 21 B4 9A        LD      HL,$9AB4            ; 
0671: 36 01           LD      (HL),$01            ; 
0673: CD 31 13        CALL    $1331               ; {}
0676: 0E 08           LD      C,$08               ; 
0678: F7              RST     0X30                ; 
0679: CD 31 13        CALL    $1331               ; {}
067C: 6B              LD      L,E                 ; 
067D: 26 00           LD      H,$00               ; 
067F: 11 10 81        LD      DE,$8110            ; 
0682: CD 66 0A        CALL    $0A66               ; {}
0685: CD 31 13        CALL    $1331               ; {}
0688: 3A 88 92        LD      A,($9288)           ; 
068B: FE 28           CP      $28                 ; 
068D: 28 1D           JR      Z,$6AC              ; {}
068F: 0E 09           LD      C,$09               ; 
0691: F7              RST     0X30                ; 
0692: CD 31 13        CALL    $1331               ; {}
0695: EB              EX      DE,HL               ; 
0696: 3A 88 92        LD      A,($9288)           ; 
0699: A7              AND     A                   ; 
069A: 28 0A           JR      Z,$6A6              ; {}
069C: 6F              LD      L,A                 ; 
069D: 26 00           LD      H,$00               ; 
069F: CD 66 0A        CALL    $0A66               ; {}
06A2: AF              XOR     A                   ; 
06A3: 12              LD      (DE),A              ; 
06A4: E7              RST     0X20                ; 
06A5: AF              XOR     A                   ; 
06A6: 12              LD      (DE),A              ; 
06A7: 3A 88 92        LD      A,($9288)           ; 
06AA: 18 21           JR      $6CD                ; {}
06AC: 06 07           LD      B,$07               ; 
06AE: 3A A0 92        LD      A,($92A0)           ; 
06B1: E6 0F           AND     $0F                 ; 
06B3: 20 F9           JR      NZ,$6AE             ; {}
06B5: 0E 0B           LD      C,$0B               ; 
06B7: CB 40           BIT     0,B                 ; 
06B9: 28 01           JR      Z,$6BC              ; {}
06BB: 0C              INC     C                   ; 
06BC: C5              PUSH    BC                  ; 
06BD: F7              RST     0X30                ; 
06BE: C1              POP     BC                  ; 
06BF: 3A A0 92        LD      A,($92A0)           ; 
06C2: E6 0F           AND     $0F                 ; 
06C4: 28 F9           JR      Z,$6BF              ; {}
06C6: 10 E6           DJNZ    $6AE                ; {}
06C8: 0E 0D           LD      C,$0D               ; 
06CA: F7              RST     0X30                ; 
06CB: 3E 64           LD      A,$64               ; 
06CD: 21 9F 92        LD      HL,$929F            ; 
06D0: 86              ADD     A,(HL)              ; 
06D1: 77              LD      (HL),A              ; 
06D2: CD 3B 07        CALL    $073B               ; {}
06D5: CD 31 13        CALL    $1331               ; {}
06D8: CD 31 13        CALL    $1331               ; {}
06DB: 21 B0 83        LD      HL,$83B0            ; 
06DE: 0E 0B           LD      C,$0B               ; 
06E0: CD B3 13        CALL    $13B3               ; {}
06E3: 21 B3 83        LD      HL,$83B3            ; 
06E6: 0E 0B           LD      C,$0B               ; 
06E8: CD B3 13        CALL    $13B3               ; {}
06EB: 0E 0B           LD      C,$0B               ; 
06ED: F7              RST     0X30                ; 
06EE: C3 EF 04        JP      $04EF               ; {}
06F1: 76              HALT                        ; 

06F2: F3              DI                          ; 
06F3: 3A 00 71        LD      A,($7100)           ; 
06F6: FE 10           CP      $10                 ; 
06F8: 20 F9           JR      NZ,$6F3             ; {}
06FA: 21 38 07        LD      HL,$0738            ; 
06FD: 11 00 70        LD      DE,$7000            ; 
0700: 01 03 00        LD      BC,$0003            ; 
0703: D9              EXX                         ; 
0704: 3E 61           LD      A,$61               ; 
0706: 32 00 71        LD      ($7100),A           ; 
0709: 76              HALT                        ; 
070A: AF              XOR     A                   ; 
070B: CD 4F 09        CALL    $094F               ; {}
070E: FB              EI                          ; 
070F: AF              XOR     A                   ; 
0710: 06 20           LD      B,$20               ; 
0712: 21 A0 9A        LD      HL,$9AA0            ; 
0715: DF              RST     0X18                ; 
0716: 11 F9 83        LD      DE,$83F9            ; 
0719: CD 3A 0A        CALL    $0A3A               ; {}
071C: 11 E4 83        LD      DE,$83E4            ; 
071F: CD 3A 0A        CALL    $0A3A               ; {}
0722: 3A B3 99        LD      A,($99B3)           ; 
0725: 3C              INC     A                   ; 
0726: 21 E1 99        LD      HL,$99E1            ; 
0729: 86              ADD     A,(HL)              ; 
072A: 27              DAA                         ; 
072B: 77              LD      (HL),A              ; 
072C: D2 5A 03        JP      NC,$035A            ; {}
072F: 2B              DEC     HL                  ; 
0730: 7E              LD      A,(HL)              ; 
0731: C6 01           ADD     $01                 ; 
0733: 27              DAA                         ; 
0734: 77              LD      (HL),A              ; 
0735: C3 5A 03        JP      $035A               ; {}
0738: 02              LD      (BC),A              ; 
0739: 02              LD      (BC),A              ; 
073A: 02              LD      (BC),A              ; 
073B: 3A 40 98        LD      A,($9840)           ; 
073E: A7              AND     A                   ; 
073F: 3E F9           LD      A,$F9               ; 
0741: 28 02           JR      Z,$745              ; {}
0743: 3E E4           LD      A,$E4               ; 
0745: DD 6F           LD      IXL,A               ; 
0747: 06 10           LD      B,$10               ; 
0749: 21 90 92        LD      HL,$9290            ; 
074C: EB              EX      DE,HL               ; 
074D: 21 0D 08        LD      HL,$080D            ; 
0750: 78              LD      A,B                 ; 
0751: D7              RST     0X10                ; 
0752: 4E              LD      C,(HL)              ; 
0753: EB              EX      DE,HL               ; 
0754: 7E              LD      A,(HL)              ; 
0755: A7              AND     A                   ; 
0756: 28 1D           JR      Z,$775              ; {}
0758: 35              DEC     (HL)                ; 
0759: EB              EX      DE,HL               ; 
075A: 26 83           LD      H,$83               ; 
075C: DD 7D           LD      A,IXL               ; 
075E: 6F              LD      L,A                 ; 
075F: 79              LD      A,C                 ; 
0760: E6 0F           AND     $0F                 ; 
0762: CD EB 07        CALL    $07EB               ; {}
0765: DD 7D           LD      A,IXL               ; 
0767: 3C              INC     A                   ; 
0768: 6F              LD      L,A                 ; 
0769: 79              LD      A,C                 ; 
076A: 07              RLCA                        ; 
076B: 07              RLCA                        ; 
076C: 07              RLCA                        ; 
076D: 07              RLCA                        ; 
076E: E6 0F           AND     $0F                 ; 
0770: CD EB 07        CALL    $07EB               ; {}
0773: 18 DE           JR      $753                ; {}
0775: 2C              INC     L                   ; 
0776: 10 D4           DJNZ    $74C                ; {}
0778: DD 7D           LD      A,IXL               ; 
077A: C6 04           ADD     $04                 ; 
077C: 5F              LD      E,A                 ; 
077D: 21 F2 83        LD      HL,$83F2            ; 
0780: 16 83           LD      D,$83               ; 
0782: 06 06           LD      B,$06               ; 
0784: 1A              LD      A,(DE)              ; 
0785: 96              SUB     (HL)                ; 
0786: C6 09           ADD     $09                 ; 
0788: FE E5           CP      $E5                 ; 
078A: 30 0F           JR      NC,$79B             ; {}
078C: D6 0A           SUB     $0A                 ; 
078E: FE 09           CP      $09                 ; 
0790: 38 09           JR      C,$79B              ; {}
0792: 3C              INC     A                   ; 
0793: 20 0C           JR      NZ,$7A1             ; {}
0795: 2D              DEC     L                   ; 
0796: 1D              DEC     E                   ; 
0797: 10 EB           DJNZ    $784                ; {}
0799: 18 06           JR      $7A1                ; {}
079B: 1A              LD      A,(DE)              ; 
079C: 77              LD      (HL),A              ; 
079D: 2D              DEC     L                   ; 
079E: 1D              DEC     E                   ; 
079F: 10 FA           DJNZ    $79B                ; {}
07A1: DD 7D           LD      A,IXL               ; 
07A3: C6 04           ADD     $04                 ; 
07A5: 6F              LD      L,A                 ; 
07A6: 7E              LD      A,(HL)              ; 
07A7: FE 24           CP      $24                 ; 
07A9: 20 01           JR      NZ,$7AC             ; {}
07AB: AF              XOR     A                   ; 
07AC: E6 3F           AND     $3F                 ; 
07AE: 07              RLCA                        ; 
07AF: 4F              LD      C,A                 ; 
07B0: 07              RLCA                        ; 
07B1: 07              RLCA                        ; 
07B2: 81              ADD     A,C                 ; 
07B3: 4F              LD      C,A                 ; 
07B4: 2D              DEC     L                   ; 
07B5: 7E              LD      A,(HL)              ; 
07B6: FE 24           CP      $24                 ; 
07B8: 20 01           JR      NZ,$7BB             ; {}
07BA: AF              XOR     A                   ; 
07BB: 81              ADD     A,C                 ; 
07BC: 21 3E 98        LD      HL,$983E            ; 
07BF: BE              CP      (HL)                ; 
07C0: C0              RET     NZ                  ; 
07C1: 3A 81 99        LD      A,($9981)           ; 
07C4: 47              LD      B,A                 ; 
07C5: E6 7F           AND     $7F                 ; 
07C7: 4F              LD      C,A                 ; 
07C8: 7E              LD      A,(HL)              ; 
07C9: B9              CP      C                   ; 
07CA: 30 03           JR      NC,$7CF             ; {}
07CC: 79              LD      A,C                 ; 
07CD: 18 01           JR      $7D0                ; {}
07CF: 80              ADD     A,B                 ; 
07D0: 77              LD      (HL),A              ; 
07D1: 32 AA 9A        LD      ($9AAA),A           ; 
07D4: 21 20 98        LD      HL,$9820            ; 
07D7: 34              INC     (HL)                ; 
07D8: CD 7E 13        CALL    $137E               ; {}
07DB: 21 EB 99        LD      HL,$99EB            ; 
07DE: 7E              LD      A,(HL)              ; 
07DF: C6 01           ADD     $01                 ; 
07E1: 27              DAA                         ; 
07E2: 77              LD      (HL),A              ; 
07E3: D0              RET     NC                  ; 
07E4: 2D              DEC     L                   ; 
07E5: 7E              LD      A,(HL)              ; 
07E6: C6 01           ADD     $01                 ; 
07E8: 27              DAA                         ; 
07E9: 77              LD      (HL),A              ; 
07EA: C9              RET                         ; 
07EB: A7              AND     A                   ; 
07EC: C8              RET     Z                   ; 
07ED: 86              ADD     A,(HL)              ; 
07EE: FE 24           CP      $24                 ; 
07F0: 38 02           JR      C,$7F4              ; {}
07F2: D6 24           SUB     $24                 ; 
07F4: FE 0A           CP      $0A                 ; 
07F6: 30 02           JR      NC,$7FA             ; {}
07F8: 77              LD      (HL),A              ; 
07F9: C9              RET                         ; 
07FA: D6 0A           SUB     $0A                 ; 
07FC: 77              LD      (HL),A              ; 
07FD: 2C              INC     L                   ; 
07FE: 7E              LD      A,(HL)              ; 
07FF: FE 24           CP      $24                 ; 
0801: 20 01           JR      NZ,$804             ; {}
0803: AF              XOR     A                   ; 
0804: FE 09           CP      $09                 ; 
0806: 28 03           JR      Z,$80B              ; {}
0808: 3C              INC     A                   ; 
0809: 77              LD      (HL),A              ; 
080A: C9              RET                         ; 
080B: AF              XOR     A                   ; 
080C: 18 EE           JR      $7FC                ; {}

080E: 10 00           DJNZ    $810                ; {}
0810: 00              NOP                         ; 
0811: 00              NOP                         ; 
0812: 00              NOP                         ; 
0813: 00              NOP                         ; 
0814: 00              NOP                         ; 
0815: 00              NOP                         ; 
0816: 50              LD      D,B                 ; 
0817: 08              EX      AF,AF'              ; 
0818: 08              EX      AF,AF'              ; 
0819: 08              EX      AF,AF'              ; 
081A: 05              DEC     B                   ; 
081B: 08              EX      AF,AF'              ; 
081C: 15              DEC     D                   ; 
081D: 00              NOP                         ; 
081E: 3A 08 90        LD      A,($9008)           ; 
0821: 47              LD      B,A                 ; 
0822: 3A A7 92        LD      A,($92A7)           ; 
0825: B0              OR      B                   ; 
0826: 20 06           JR      NZ,$82E             ; {}
0828: 32 A0 9A        LD      ($9AA0),A           ; 
082B: C3 B1 04        JP      $04B1               ; {}
082E: 3A 13 92        LD      A,($9213)           ; 
0831: A7              AND     A                   ; 
0832: C8              RET     Z                   ; 
0833: AF              XOR     A                   ; 
0834: 32 42 98        LD      ($9842),A           ; 
0837: C3 B1 04        JP      $04B1               ; {}
083A: C9              RET                         ; 

;======================================================================
; PLAY COMMAND 01 (Draw Player)
;
083B: 3E 01           LD      A,$01               ; Flag CPU2 05EB to ...
083D: 32 D6 92        LD      ($92D6),A           ; ... continue
0840: 21 40 8B        LD      HL,$8B40            ; 
0843: 11 C0 8B        LD      DE,$8BC0            ; 
0846: 01 40 00        LD      BC,$0040            ; 
0849: ED B0           LDIR                        ; 
084B: 21 40 93        LD      HL,$9340            ; 
084E: 11 C0 93        LD      DE,$93C0            ; 
0851: 0E 40           LD      C,$40               ; 
0853: ED B0           LDIR                        ; 
0855: 21 40 9B        LD      HL,$9B40            ; 
0858: 11 C0 9B        LD      DE,$9BC0            ; 
085B: 0E 40           LD      C,$40               ; 
085D: ED B0           LDIR                        ; 
085F: AF              XOR     A                   ; Flag CPU2 05EB to ...
0860: 32 D6 92        LD      ($92D6),A           ; ... wait
0863: 3A D7 92        LD      A,($92D7)           ; Wait for CPU2 05C1 ...
0866: 3D              DEC     A                   ; ... to go to ...
0867: 28 FA           JR      Z,$863              ; {} ... 01
0869: C9              RET                         ; ... Done

;======================================================================
; PLAY COMMAND 05 (??)
;
086A: 3A AE 92        LD      A,($92AE)           ; 
086D: 47              LD      B,A                 ; 
086E: FE 3C           CP      $3C                 ; 
0870: 30 06           JR      NC,$878             ; {}
0872: 3A C5 99        LD      A,($99C5)           ; 
0875: 32 C4 99        LD      ($99C4),A           ; 
0878: 3A A7 92        LD      A,($92A7)           ; 
087B: 4F              LD      C,A                 ; 
087C: 3A C0 99        LD      A,($99C0)           ; 
087F: 21 1C 09        LD      HL,$091C            ; 
0882: CD D1 08        CALL    $08D1               ; {}
0885: 32 C8 92        LD      ($92C8),A           ; 
0888: 3A AA 92        LD      A,($92AA)           ; 
088B: A7              AND     A                   ; 
088C: 28 0D           JR      Z,$89B              ; {}
088E: 21 C4 92        LD      HL,$92C4            ; 
0891: 3E 02           LD      A,$02               ; 
0893: 06 03           LD      B,$03               ; 
0895: DF              RST     0X18                ; 
0896: AF              XOR     A                   ; 
0897: 32 A0 9A        LD      ($9AA0),A           ; 
089A: C9              RET                         ; 
089B: 3A C1 99        LD      A,($99C1)           ; 
089E: 21 3C 09        LD      HL,$093C            ; 
08A1: CD D1 08        CALL    $08D1               ; {}
08A4: 32 C4 92        LD      ($92C4),A           ; 
08A7: 3A C2 99        LD      A,($99C2)           ; 
08AA: 21 E0 08        LD      HL,$08E0            ; 
08AD: CD C0 08        CALL    $08C0               ; {}
08B0: 32 C5 92        LD      ($92C5),A           ; 
08B3: 3A C3 99        LD      A,($99C3)           ; 
08B6: 21 FE 08        LD      HL,$08FE            ; 
08B9: CD C0 08        CALL    $08C0               ; {}
08BC: 32 C6 92        LD      ($92C6),A           ; 
08BF: C9              RET                         ; 
08C0: 5F              LD      E,A                 ; 
08C1: CB 27           SLA     A                   ; 
08C3: 83              ADD     A,E                 ; 
08C4: D7              RST     0X10                ; 
08C5: 78              LD      A,B                 ; 
08C6: FE 28           CP      $28                 ; 
08C8: 30 01           JR      NC,$8CB             ; {}
08CA: 23              INC     HL                  ; 
08CB: A7              AND     A                   ; 
08CC: 20 01           JR      NZ,$8CF             ; {}
08CE: 23              INC     HL                  ; 
08CF: 7E              LD      A,(HL)              ; 
08D0: C9              RET                         ; 
;
08D1: CB 27           SLA     A                   ; 
08D3: CF              RST     0X08                ; 
08D4: EB              EX      DE,HL               ; 
08D5: 61              LD      H,C                 ; 
08D6: 3E 0A           LD      A,$0A               ; 
08D8: CD 61 10        CALL    $1061               ; {}
08DB: EB              EX      DE,HL               ; 
08DC: 7A              LD      A,D                 ; 
08DD: D7              RST     0X10                ; 
08DE: 7E              LD      A,(HL)              ; 
08DF: C9              RET                         ; 
;
08E0: 09              ADD     HL,BC               ; #
08E1: 07              RLCA                        ; #
08E2: 05              DEC     B                   ; #
08E3: 08              EX      AF,AF'              ; #
08E4: 06 04           LD      B,$04               ; #
08E6: 07              RLCA                        ; #
08E7: 05              DEC     B                   ; #
08E8: 04              INC     B                   ; #
08E9: 06 04           LD      B,$04               ; #
08EB: 03              INC     BC                  ; #
08EC: 05              DEC     B                   ; #
08ED: 03              INC     BC                  ; #
08EE: 03              INC     BC                  ; #
08EF: 04              INC     B                   ; #
08F0: 03              INC     BC                  ; #
08F1: 03              INC     BC                  ; #
08F2: 04              INC     B                   ; #
08F3: 02              LD      (BC),A              ; #
08F4: 02              LD      (BC),A              ; #
08F5: 03              INC     BC                  ; #
08F6: 03              INC     BC                  ; #
08F7: 02              LD      (BC),A              ; #
08F8: 03              INC     BC                  ; #
08F9: 02              LD      (BC),A              ; #
08FA: 02              LD      (BC),A              ; #
08FB: 02              LD      (BC),A              ; #
08FC: 02              LD      (BC),A              ; #
08FD: 02              LD      (BC),A              ; #
08FE: 06 05           LD      B,$05               ; #
0900: 04              INC     B                   ; #
0901: 05              DEC     B                   ; #
0902: 04              INC     B                   ; #
0903: 03              INC     BC                  ; #
0904: 05              DEC     B                   ; #
0905: 03              INC     BC                  ; #
0906: 03              INC     BC                  ; #
0907: 04              INC     B                   ; #
0908: 03              INC     BC                  ; #
0909: 02              LD      (BC),A              ; #
090A: 04              INC     B                   ; #
090B: 02              LD      (BC),A              ; #
090C: 02              LD      (BC),A              ; #
090D: 03              INC     BC                  ; #
090E: 03              INC     BC                  ; #
090F: 02              LD      (BC),A              ; #
0910: 03              INC     BC                  ; #
0911: 02              LD      (BC),A              ; #
0912: 01 02 02        LD      BC,$0202            ; #
0915: 01 02 01        LD      BC,$0102            ; #
0918: 01 01 01        LD      BC,$0101            ; #
091B: 01 03 03        LD      BC,$0303            ; #
091E: 01 01 03        LD      BC,$0301            ; #
0921: 03              INC     BC                  ; #
0922: 03              INC     BC                  ; #
0923: 01 07 03        LD      BC,$0307            ; #
0926: 03              INC     BC                  ; #
0927: 01 07 03        LD      BC,$0307            ; #
092A: 03              INC     BC                  ; #
092B: 03              INC     BC                  ; #
092C: 07              RLCA                        ; #
092D: 07              RLCA                        ; #
092E: 03              INC     BC                  ; #
092F: 03              INC     BC                  ; #
0930: 0F              RRCA                        ; #
0931: 07              RLCA                        ; #
0932: 03              INC     BC                  ; #
0933: 03              INC     BC                  ; #
0934: 0F              RRCA                        ; #
0935: 07              RLCA                        ; #
0936: 07              RLCA                        ; #
0937: 03              INC     BC                  ; #
0938: 0F              RRCA                        ; #
0939: 07              RLCA                        ; #
093A: 07              RLCA                        ; #
093B: 07              RLCA                        ; #
093C: 06 0A           LD      B,$0A               ; #
093E: 0F              RRCA                        ; #
093F: 0F              RRCA                        ; #
0940: 04              INC     B                   ; #
0941: 08              EX      AF,AF'              ; #
0942: 0D              DEC     C                   ; #
0943: 0D              DEC     C                   ; #
0944: 04              INC     B                   ; #
0945: 06 0A           LD      B,$0A               ; #
0947: 0A              LD      A,(BC)              ; #

;======================================================================
; PLAY COMMAND 0F (??)
;
0948: 3A A0 92        LD      A,($92A0)           ; 
094B: 07              RLCA                        ; 
094C: 07              RLCA                        ; 
094D: 07              RLCA                        ; 
094E: 07              RLCA                        ; 
094F: 4F              LD      C,A                 ; 
0950: 3A 01 92        LD      A,($9201)           ; 
0953: FE 03           CP      $03                 ; 
0955: C0              RET     NZ                  ; 
0956: 3A 40 98        LD      A,($9840)           ; 
0959: 47              LD      B,A                 ; 
095A: 2F              CPL                         ; 
095B: A1              AND     C                   ; 
095C: 21 81 09        LD      HL,$0981            ; 
095F: 11 D9 83        LD      DE,$83D9            ; 
0962: CD 72 09        CALL    $0972               ; {}
0965: 3A B3 99        LD      A,($99B3)           ; 
0968: A7              AND     A                   ; 
0969: C8              RET     Z                   ; 
096A: 78              LD      A,B                 ; 
096B: A1              AND     C                   ; 
096C: 21 84 09        LD      HL,$0984            ; 
096F: 11 C4 83        LD      DE,$83C4            ; 
0972: C5              PUSH    BC                  ; 
0973: E6 01           AND     $01                 ; 
0975: 28 03           JR      Z,$97A              ; {}
0977: 21 87 09        LD      HL,$0987            ; 
097A: 01 03 00        LD      BC,$0003            ; 
097D: ED B0           LDIR                        ; 
097F: C1              POP     BC                  ; 
0980: C9              RET                         ; 
;
0981: 19              ADD     HL,DE               ; #
0982: 1E 01           LD      E,$01               ; #
0984: 19              ADD     HL,DE               ; #
0985: 1E 02           LD      E,$02               ; #
0987: 24              INC     H                   ; #
0988: 24              INC     H                   ; #
0989: 24              INC     H                   ; #

;======================================================================
; PLAY COMMAND 1F Process inputs (like coins)
;
098A: 3A B5 99        LD      A,($99B5)           ; 
098D: FE BB           CP      $BB                 ; 
098F: CA 6C 33        JP      Z,$336C             ; {}
0992: 3A 01 92        LD      A,($9201)           ; 
0995: FE 03           CP      $03                 ; 
0997: 20 19           JR      NZ,$9B2             ; {}
0999: 21 E9 99        LD      HL,$99E9            ; 
099C: 7E              LD      A,(HL)              ; 
099D: C6 01           ADD     $01                 ; 
099F: 27              DAA                         ; 
09A0: FE 60           CP      $60                 ; 
09A2: 20 01           JR      NZ,$9A5             ; {}
09A4: AF              XOR     A                   ; 
09A5: 06 04           LD      B,$04               ; 
09A7: 3F              CCF                         ; 
09A8: 77              LD      (HL),A              ; 
09A9: 2D              DEC     L                   ; 
09AA: 7E              LD      A,(HL)              ; 
09AB: CE 00           ADC     $00                 ; 
09AD: 27              DAA                         ; 
09AE: 10 F8           DJNZ    $9A8                ; {}
09B0: 18 42           JR      $9F4                ; {}
09B2: 3A B8 99        LD      A,($99B8)           ; 
09B5: FE A0           CP      $A0                 ; 
09B7: 11 3C 80        LD      DE,$803C            ; 
09BA: 28 30           JR      Z,$9EC              ; {}
09BC: 3A B5 99        LD      A,($99B5)           ; 
09BF: 21 E2 09        LD      HL,$09E2            ; 
09C2: 01 06 00        LD      BC,$0006            ; 
09C5: ED B8           LDDR                        ; 
09C7: 1D              DEC     E                   ; 
09C8: 4F              LD      C,A                 ; 
09C9: 07              RLCA                        ; 
09CA: 07              RLCA                        ; 
09CB: 07              RLCA                        ; 
09CC: 07              RLCA                        ; 
09CD: E6 0F           AND     $0F                 ; 
09CF: 28 02           JR      Z,$9D3              ; {}
09D1: 12              LD      (DE),A              ; 
09D2: 1D              DEC     E                   ; 
09D3: 79              LD      A,C                 ; 
09D4: E6 0F           AND     $0F                 ; 
09D6: 12              LD      (DE),A              ; 
09D7: 1D              DEC     E                   ; 
09D8: 3E 24           LD      A,$24               ; 
09DA: 12              LD      (DE),A              ; 
09DB: 18 17           JR      $9F4                ; {}
09DD: 1D              DEC     E                   ; 
09DE: 12              LD      (DE),A              ; 
09DF: 0D              DEC     C                   ; 
09E0: 0E 1B           LD      C,$1B               ; 
09E2: 0C              INC     C                   ; 
09E3: 22 0A 15        LD      ($150A),HL          ; {}
09E6: 19              ADD     HL,DE               ; 
09E7: 24              INC     H                   ; 
09E8: 0E 0E           LD      C,$0E               ; 
09EA: 1B              DEC     DE                  ; 
09EB: 0F              RRCA                        ; 
09EC: 21 EB 09        LD      HL,$09EB            ; 
09EF: 01 09 00        LD      BC,$0009            ; 
09F2: ED B8           LDDR                        ; 
09F4: 3A 01 92        LD      A,($9201)           ; 
09F7: A7              AND     A                   ; 
09F8: C8              RET     Z                   ; 
09F9: 3D              DEC     A                   ; 
09FA: 20 16           JR      NZ,$A12             ; {}
09FC: 3A B5 99        LD      A,($99B5)           ; 
09FF: A7              AND     A                   ; 
0A00: 28 10           JR      Z,$A12              ; {}
0A02: 3E 02           LD      A,$02               ; 
0A04: 32 01 92        LD      ($9201),A           ; 
0A07: AF              XOR     A                   ; 
0A08: 21 A0 9A        LD      HL,$9AA0            ; 
0A0B: 06 08           LD      B,$08               ; 
0A0D: DF              RST     0X18                ; 
0A0E: 2C              INC     L                   ; 
0A0F: 06 0F           LD      B,$0F               ; 
0A11: DF              RST     0X18                ; 
0A12: 3A B5 99        LD      A,($99B5)           ; 
0A15: 4F              LD      C,A                 ; 
0A16: 3A B8 99        LD      A,($99B8)           ; 
0A19: 47              LD      B,A                 ; 
0A1A: 91              SUB     C                   ; 
0A1B: C8              RET     Z                   ; 
0A1C: 38 0F           JR      C,$A2D              ; {}
0A1E: 27              DAA                         ; 
0A1F: 3D              DEC     A                   ; 
0A20: 32 B3 99        LD      ($99B3),A           ; 
0A23: 79              LD      A,C                 ; 
0A24: 32 B8 99        LD      ($99B8),A           ; 
0A27: 3E 03           LD      A,$03               ; 
0A29: 32 01 92        LD      ($9201),A           ; 
0A2C: C9              RET                         ; 
0A2D: 79              LD      A,C                 ; 
0A2E: 32 B8 99        LD      ($99B8),A           ; 
0A31: FE A0           CP      $A0                 ; 
0A33: C8              RET     Z                   ; 
0A34: 90              SUB     B                   ; 
0A35: 27              DAA                         ; 
0A36: 32 79 9A        LD      ($9A79),A           ; 
0A39: C9              RET                         ; 
0A3A: 21 03 91        LD      HL,$9103            ; 
0A3D: 06 05           LD      B,$05               ; 
0A3F: 1A              LD      A,(DE)              ; 
0A40: 1C              INC     E                   ; 
0A41: FE 24           CP      $24                 ; 
0A43: 20 01           JR      NZ,$A46             ; {}
0A45: AF              XOR     A                   ; 
0A46: ED 67           RRD                         ; 
0A48: CB 40           BIT     0,B                 ; 
0A4A: 20 01           JR      NZ,$A4D             ; {}
0A4C: 2D              DEC     L                   ; 
0A4D: 10 F0           DJNZ    $A3F                ; {}
0A4F: AF              XOR     A                   ; 
0A50: ED 67           RRD                         ; 
0A52: 2D              DEC     L                   ; 
0A53: 36 00           LD      (HL),$00            ; 
0A55: 2E 03           LD      L,$03               ; 
0A57: 11 E5 99        LD      DE,$99E5            ; 
0A5A: 06 04           LD      B,$04               ; 
0A5C: A7              AND     A                   ; 
0A5D: 1A              LD      A,(DE)              ; 
0A5E: 8E              ADC     A,(HL)              ; 
0A5F: 27              DAA                         ; 
0A60: 12              LD      (DE),A              ; 
0A61: 1D              DEC     E                   ; 
0A62: 2D              DEC     L                   ; 
0A63: 10 F8           DJNZ    $A5D                ; {}
0A65: C9              RET                         ; 
0A66: 06 01           LD      B,$01               ; 
0A68: 25              DEC     H                   ; 
0A69: 24              INC     H                   ; 
0A6A: 20 05           JR      NZ,$A71             ; {}
0A6C: 7D              LD      A,L                 ; 
0A6D: FE 0A           CP      $0A                 ; 
0A6F: 38 0A           JR      C,$A7B              ; {}
0A71: 3E 0A           LD      A,$0A               ; 
0A73: CD 61 10        CALL    $1061               ; {}
0A76: F5              PUSH    AF                  ; 
0A77: 04              INC     B                   ; 
0A78: 18 EE           JR      $A68                ; {}
0A7A: F1              POP     AF                  ; 
0A7B: CD 81 0A        CALL    $0A81               ; {}
0A7E: 10 FA           DJNZ    $A7A                ; {}
0A80: C9              RET                         ; 
0A81: 12              LD      (DE),A              ; 
0A82: C3 20 00        JP      $0020               ; {}
0A85: 2A 44 98        LD      HL,($9844)          ; 
0A88: ED 5B 46 98     LD      DE,($9846)          ; 
0A8C: 7A              LD      A,D                 ; 
0A8D: B3              OR      E                   ; 
0A8E: 20 05           JR      NZ,$A95             ; {}
0A90: 11 00 00        LD      DE,$0000            ; 
0A93: 18 51           JR      $AE6                ; {}
0A95: CB 7A           BIT     7,D                 ; 
0A97: 20 0A           JR      NZ,$AA3             ; {}
0A99: CB 7C           BIT     7,H                 ; 
0A9B: 20 06           JR      NZ,$AA3             ; {}
0A9D: 29              ADD     HL,HL               ; 
0A9E: EB              EX      DE,HL               ; 
0A9F: 29              ADD     HL,HL               ; 
0AA0: EB              EX      DE,HL               ; 
0AA1: 18 F2           JR      $A95                ; {}
0AA3: 7A              LD      A,D                 ; 
0AA4: CD 61 10        CALL    $1061               ; {}
0AA7: E5              PUSH    HL                  ; 
0AA8: 67              LD      H,A                 ; 
0AA9: 2E 00           LD      L,$00               ; 
0AAB: 7A              LD      A,D                 ; 
0AAC: CD 61 10        CALL    $1061               ; {}
0AAF: E3              EX      (SP),HL             ; 
0AB0: 11 B0 99        LD      DE,$99B0            ; 
0AB3: 06 04           LD      B,$04               ; 
0AB5: 7C              LD      A,H                 ; 
0AB6: 26 00           LD      H,$00               ; 
0AB8: EB              EX      DE,HL               ; 
0AB9: ED 6F           RLD                         ; 
0ABB: CB 40           BIT     0,B                 ; 
0ABD: 28 01           JR      Z,$AC0              ; {}
0ABF: 2C              INC     L                   ; 
0AC0: EB              EX      DE,HL               ; 
0AC1: CD 19 0B        CALL    $0B19               ; {}
0AC4: 08              EX      AF,AF'              ; 
0AC5: E3              EX      (SP),HL             ; 
0AC6: CD 19 0B        CALL    $0B19               ; {}
0AC9: E3              EX      (SP),HL             ; 
0ACA: D7              RST     0X10                ; 
0ACB: 08              EX      AF,AF'              ; 
0ACC: 84              ADD     A,H                 ; 
0ACD: 26 00           LD      H,$00               ; 
0ACF: 10 E7           DJNZ    $AB8                ; {}
0AD1: D1              POP     DE                  ; 
0AD2: FE 05           CP      $05                 ; 
0AD4: 38 14           JR      C,$AEA              ; {}
0AD6: ED 5B B0 99     LD      DE,($99B0)          ; 
0ADA: 7A              LD      A,D                 ; 
0ADB: C6 01           ADD     $01                 ; 
0ADD: 27              DAA                         ; 
0ADE: 57              LD      D,A                 ; 
0ADF: 30 05           JR      NC,$AE6             ; {}
0AE1: 7B              LD      A,E                 ; 
0AE2: C6 01           ADD     $01                 ; 
0AE4: 27              DAA                         ; 
0AE5: 5F              LD      E,A                 ; 
0AE6: ED 53 B0 99     LD      ($99B0),DE          ; 
0AEA: 06 04           LD      B,$04               ; 
0AEC: 0E 00           LD      C,$00               ; 
0AEE: 21 B0 99        LD      HL,$99B0            ; 
0AF1: 11 38 81        LD      DE,$8138            ; 
0AF4: 05              DEC     B                   ; 
0AF5: 20 04           JR      NZ,$AFB             ; {}
0AF7: 3E 2A           LD      A,$2A               ; 
0AF9: 12              LD      (DE),A              ; 
0AFA: E7              RST     0X20                ; 
0AFB: 04              INC     B                   ; 
0AFC: AF              XOR     A                   ; 
0AFD: ED 6F           RLD                         ; 
0AFF: CB 40           BIT     0,B                 ; 
0B01: 28 01           JR      Z,$B04              ; {}
0B03: 2C              INC     L                   ; 
0B04: A7              AND     A                   ; 
0B05: 20 04           JR      NZ,$B0B             ; {}
0B07: CB 41           BIT     0,C                 ; 
0B09: 28 04           JR      Z,$B0F              ; {}
0B0B: CB C1           SET     0,C                 ; 
0B0D: 12              LD      (DE),A              ; 
0B0E: E7              RST     0X20                ; 
0B0F: 78              LD      A,B                 ; 
0B10: FE 03           CP      $03                 ; 
0B12: 20 02           JR      NZ,$B16             ; {}
0B14: CB C1           SET     0,C                 ; 
0B16: 10 DC           DJNZ    $AF4                ; {}
0B18: C9              RET                         ; 
0B19: 3E 0A           LD      A,$0A               ; 
0B1B: CD 4E 10        CALL    $104E               ; {}
0B1E: 7C              LD      A,H                 ; 
0B1F: 26 00           LD      H,$00               ; 
0B21: C9              RET                         ; 

0B22: FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0B30: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0B40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0B50: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0B60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0B70: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0B80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0B90: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0BA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0BB0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0BC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0BD0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0BE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0BF0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

0C00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0C10: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0C20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0C30: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0C40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0C50: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0C60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0C70: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0C80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0C90: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0CA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0CB0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0CC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0CD0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0CE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0CF0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

0D00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0D10: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0D20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0D30: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0D40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0D50: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
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
0FF0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

0FFF: C4                              ;       

1000: E5              PUSH    HL                  ; 
1001: ED 5F           LD      A,R                 ; 
1003: 67              LD      H,A                 ; 
1004: 3A A0 92        LD      A,($92A0)           ; 
1007: 84              ADD     A,H                 ; 
1008: 6F              LD      L,A                 ; 
1009: 26 01           LD      H,$01               ; 
100B: 7E              LD      A,(HL)              ; 
100C: 67              LD      H,A                 ; 
100D: ED 5F           LD      A,R                 ; 
100F: 84              ADD     A,H                 ; 
1010: E1              POP     HL                  ; 
1011: C9              RET                         ; 
1012: C5              PUSH    BC                  ; 
1013: D5              PUSH    DE                  ; 
1014: 7B              LD      A,E                 ; 
1015: 95              SUB     L                   ; 
1016: 06 00           LD      B,$00               ; 
1018: 30 04           JR      NC,$101E            ; {}
101A: CB C0           SET     0,B                 ; 
101C: ED 44           NEG                         ; 
101E: 4F              LD      C,A                 ; 
101F: 7A              LD      A,D                 ; 
1020: 94              SUB     H                   ; 
1021: 30 0A           JR      NC,$102D            ; {}
1023: 57              LD      D,A                 ; 
1024: 78              LD      A,B                 ; 
1025: EE 01           XOR     $01                 ; 
1027: F6 02           OR      $02                 ; 
1029: 47              LD      B,A                 ; 
102A: 7A              LD      A,D                 ; 
102B: ED 44           NEG                         ; 
102D: B9              CP      C                   ; 
102E: F5              PUSH    AF                  ; 
102F: 17              RLA                         ; 
1030: A8              XOR     B                   ; 
1031: 1F              RRA                         ; 
1032: 3F              CCF                         ; 
1033: CB 10           RL      B                   ; 
1035: F1              POP     AF                  ; 
1036: 30 03           JR      NC,$103B            ; {}
1038: 51              LD      D,C                 ; 
1039: 4F              LD      C,A                 ; 
103A: 7A              LD      A,D                 ; 
103B: 61              LD      H,C                 ; 
103C: 2E 00           LD      L,$00               ; 
103E: CD 61 10        CALL    $1061               ; {}
1041: 7C              LD      A,H                 ; 
1042: A8              XOR     B                   ; 
1043: E6 01           AND     $01                 ; 
1045: 28 03           JR      Z,$104A             ; {}
1047: 7D              LD      A,L                 ; 
1048: 2F              CPL                         ; 
1049: 6F              LD      L,A                 ; 
104A: 60              LD      H,B                 ; 
104B: D1              POP     DE                  ; 
104C: C1              POP     BC                  ; 
104D: C9              RET                         ; 
104E: D5              PUSH    DE                  ; 
104F: EB              EX      DE,HL               ; 
1050: 21 00 00        LD      HL,$0000            ; 
1053: CB 3F           SRL     A                   ; 
1055: 30 01           JR      NC,$1058            ; {}
1057: 19              ADD     HL,DE               ; 
1058: CB 23           SLA     E                   ; 
105A: CB 12           RL      D                   ; 
105C: A7              AND     A                   ; 
105D: 20 F4           JR      NZ,$1053            ; {}
105F: D1              POP     DE                  ; 
1060: C9              RET                         ; 

1061: C5              PUSH    BC                  ; 
1062: 4F              LD      C,A                 ; 
1063: AF              XOR     A                   ; 
1064: 06 11           LD      B,$11               ; 
1066: 8F              ADC     A,A                 ; 
1067: 38 0B           JR      C,$1074             ; {}
1069: B9              CP      C                   ; 
106A: 38 01           JR      C,$106D             ; {}
106C: 91              SUB     C                   ; 
106D: 3F              CCF                         ; 
106E: ED 6A           ADC     HL,HL               ; 
1070: 10 F4           DJNZ    $1066               ; {}
1072: C1              POP     BC                  ; 
1073: C9              RET                         ; 
1074: 91              SUB     C                   ; 
1075: 37              SCF                         ; 
1076: C3 6E 10        JP      $106E               ; {}

; Process next moving bee (After they have setup)
1079: 7D              LD      A,L                 ; 
107A: E6 80           AND     $80                 ; 
107C: 3C              INC     A                   ; 
107D: 08              EX      AF,AF'              ; 
107E: CB BD           RES     7,L                 ; 
1080: C3 8A 10        JP      $108A               ; {}

1083: 7D              LD      A,L                 ; 
1084: 0F              RRCA                        ; 
1085: 0F              RRCA                        ; 
1086: E6 80           AND     $80                 ; 
1088: 3C              INC     A                   ; 
1089: 08              EX      AF,AF'              ; 
108A: D5              PUSH    DE                  ; Hold DE
108B: 11 14 00        LD      DE,$0014            ; 14 Bytes per bee
108E: 06 0C           LD      B,$0C               ; 12 bees to process
1090: DD 21 00 91     LD      IX,$9100            ; Bee memory
1094: DD CB 13 46     BIT     0,(IX+$13)          ; Bee alive?
1098: 28 06           JR      Z,$10A0             ; {} Yes -- handle it
109A: DD 19           ADD     IX,DE               ; Next bee
109C: 10 F6           DJNZ    $1094               ; {} Check all bees
109E: D1              POP     DE                  ; Restore DE
109F: C9              RET                         ; Out
10A0: D1              POP     DE                  ; 
10A1: DD 73 08        LD      (IX+$08),E          ; 
10A4: DD 72 09        LD      (IX+$09),D          ; 
10A7: DD 36 0D 01     LD      (IX+$0D),$01        ; 
10AB: DD 36 04 00     LD      (IX+$04),$00        ; 
10AF: DD 36 05 01     LD      (IX+$05),$01        ; 
10B3: 4D              LD      C,L                 ; 
10B4: DD 71 10        LD      (IX+$10),C          ; 
10B7: 08              EX      AF,AF'              ; 
10B8: 57              LD      D,A                 ; 
10B9: 36 09           LD      (HL),$09            ; Crashes as soon as all are out.
10BB: DD 7D           LD      A,IXL               ; 
10BD: 2C              INC     L                   ; 
10BE: 77              LD      (HL),A              ; 
10BF: 3A 15 92        LD      A,($9215)           ; 
10C2: 5F              LD      E,A                 ; 
10C3: 69              LD      L,C                 ; 
10C4: 26 93           LD      H,$93               ; Sprite position
10C6: 4E              LD      C,(HL)              ; 
10C7: 2C              INC     L                   ; 
10C8: 46              LD      B,(HL)              ; 
10C9: 26 9B           LD      H,$9B               ; Sprite control
10CB: 7E              LD      A,(HL)              ; 
10CC: 0F              RRCA                        ; 
10CD: CB 18           RR      B                   ; 
10CF: CB 43           BIT     0,E                 ; 
10D1: 20 09           JR      NZ,$10DC            ; {}
10D3: 08              EX      AF,AF'              ; 
10D4: 78              LD      A,B                 ; 
10D5: C6 50           ADD     $50                 ; 
10D7: ED 44           NEG                         ; 
10D9: 47              LD      B,A                 ; 
10DA: 08              EX      AF,AF'              ; 
10DB: 3F              CCF                         ; 
10DC: DD 70 01        LD      (IX+$01),B          ; Y coordinate
10DF: 1F              RRA                         ; /2
10E0: E6 80           AND     $80                 ; 
10E2: DD 77 00        LD      (IX+$00),A          ; X coordinate
10E5: 79              LD      A,C                 ; 
10E6: CB 43           BIT     0,E                 ; 
10E8: 28 03           JR      Z,$10ED             ; {}
10EA: C6 0D           ADD     $0D                 ; 
10EC: 2F              CPL                         ; 
10ED: CB 3F           SRL     A                   ; 
10EF: DD 77 03        LD      (IX+$03),A          ; 
10F2: 1F              RRA                         ; 
10F3: E6 80           AND     $80                 ; 
10F5: DD 77 02        LD      (IX+$02),A          ; 
10F8: DD 72 13        LD      (IX+$13),D          ; 
10FB: DD 36 0E 1E     LD      (IX+$0E),$1E        ; Prepare shot delay
10FF: 3A 0B 92        LD      A,($920B)           ; 
1102: A7              AND     A                   ; 
1103: 28 03           JR      Z,$1108             ; {}
1105: 3A C8 92        LD      A,($92C8)           ; 
1108: DD 77 0F        LD      (IX+$0F),A          ; Shots
110B: C9              RET                         ; 

110C: 3E 1F           LD      A,$1F               ; 
110E: 32 00 90        LD      ($9000),A           ; 
1111: 32 E0 98        LD      ($98E0),A           ; 
1114: 21 20 98        LD      HL,$9820            ; 
1117: 11 60 98        LD      DE,$9860            ; 
111A: 06 40           LD      B,$40               ; 
111C: 4E              LD      C,(HL)              ; 
111D: 1A              LD      A,(DE)              ; 
111E: 77              LD      (HL),A              ; 
111F: 79              LD      A,C                 ; 
1120: 12              LD      (DE),A              ; 
1121: 2C              INC     L                   ; 
1122: 1C              INC     E                   ; 
1123: 10 F7           DJNZ    $111C               ; {}
1125: 21 00 88        LD      HL,$8800            ; 
1128: 11 B0 98        LD      DE,$98B0            ; 
112B: 06 30           LD      B,$30               ; 0x30 to check
112D: 7E              LD      A,(HL)              ; Next bee
112E: 4F              LD      C,A                 ; 
112F: 26 8B           LD      H,$8B               ; Sprite color
1131: 7E              LD      A,(HL)              ; 
1132: E6 7F           AND     $7F                 ; Mask out upper bit
1134: 0D              DEC     C                   ; 
1135: 20 0B           JR      NZ,$1142            ; {}
1137: E6 78           AND     $78                 ; 
1139: 4F              LD      C,A                 ; 
113A: 2C              INC     L                   ; 
113B: 7E              LD      A,(HL)              ; 
113C: 2D              DEC     L                   ; 
113D: E6 07           AND     $07                 ; 
113F: B1              OR      C                   ; 
1140: F6 80           OR      $80                 ; Set upper bit
1142: EB              EX      DE,HL               ; 
1143: 4E              LD      C,(HL)              ; 
1144: 77              LD      (HL),A              ; 
1145: EB              EX      DE,HL               ; 
1146: CB 79           BIT     7,C                 ; 
1148: 28 10           JR      Z,$115A             ; {}
114A: 79              LD      A,C                 ; 
114B: E6 78           AND     $78                 ; 
114D: C6 06           ADD     $06                 ; 
114F: 77              LD      (HL),A              ; 
1150: 2C              INC     L                   ; 
1151: 79              LD      A,C                 ; 
1152: E6 07           AND     $07                 ; 
1154: 77              LD      (HL),A              ; 
1155: 2D              DEC     L                   ; 
1156: 3E 01           LD      A,$01               ; 
1158: 18 07           JR      $1161               ; {}
115A: 71              LD      (HL),C              ; 
115B: 26 93           LD      H,$93               ; Sprite control
115D: 36 00           LD      (HL),$00            ; Turn off sprite
115F: 3E 80           LD      A,$80               ; Flag no longer active FA NOPE
1161: 26 88           LD      H,$88               ; Bee memory
1163: 77              LD      (HL),A              ; 
1164: 13              INC     DE                  ; 
1165: 2C              INC     L                   ; 
1166: 2C              INC     L                   ; 
1167: 10 C4           DJNZ    $112D               ; {}
1169: 21 00 90        LD      HL,$9000            ; 
116C: 11 E0 98        LD      DE,$98E0            ; 
116F: 06 20           LD      B,$20               ; 
1171: 4E              LD      C,(HL)              ; 
1172: 1A              LD      A,(DE)              ; 
1173: 77              LD      (HL),A              ; 
1174: 79              LD      A,C                 ; 
1175: 12              LD      (DE),A              ; 
1176: 2C              INC     L                   ; 
1177: 1C              INC     E                   ; 
1178: 10 F7           DJNZ    $1171               ; {}
117A: AF              XOR     A                   ; 
117B: 32 00 90        LD      ($9000),A           ; 
117E: C9              RET                         ; 

117F: 21 02 80        LD      HL,$8002            ; 
1182: 06 12           LD      B,$12               ; 
1184: 7E              LD      A,(HL)              ; 
1185: FE 4A           CP      $4A                 ; 
1187: 30 02           JR      NC,$118B            ; {}
1189: 36 24           LD      (HL),$24            ; 
118B: 2C              INC     L                   ; 
118C: 10 F6           DJNZ    $1184               ; {}
118E: 2E 22           LD      L,$22               ; 
1190: 06 12           LD      B,$12               ; 
1192: 7E              LD      A,(HL)              ; 
1193: FE 4A           CP      $4A                 ; 
1195: 30 02           JR      NC,$1199            ; {}
1197: 36 24           LD      (HL),$24            ; 
1199: 2C              INC     L                   ; 
119A: 10 F6           DJNZ    $1192               ; {}
119C: 3A 21 98        LD      A,($9821)           ; 
119F: 06 00           LD      B,$00               ; 
11A1: 21 01 80        LD      HL,$8001            ; 
11A4: FE 32           CP      $32                 ; 
11A6: 38 07           JR      C,$11AF             ; {}
11A8: D6 32           SUB     $32                 ; 
11AA: 04              INC     B                   ; 
11AB: 2C              INC     L                   ; 
11AC: 2C              INC     L                   ; 
11AD: 18 F5           JR      $11A4               ; {}
11AF: EB              EX      DE,HL               ; 
11B0: 6F              LD      L,A                 ; 
11B1: 26 00           LD      H,$00               ; 
11B3: 3E 0A           LD      A,$0A               ; 
11B5: CD 61 10        CALL    $1061               ; {}
11B8: 67              LD      H,A                 ; 
11B9: E5              PUSH    HL                  ; 
11BA: EB              EX      DE,HL               ; 
11BB: FE 05           CP      $05                 ; 
11BD: 38 02           JR      C,$11C1             ; {}
11BF: D6 04           SUB     $04                 ; 
11C1: 4F              LD      C,A                 ; 
11C2: 7B              LD      A,E                 ; 
11C3: CB 47           BIT     0,A                 ; 
11C5: 28 02           JR      Z,$11C9             ; {}
11C7: 3E 02           LD      A,$02               ; 
11C9: 81              ADD     A,C                 ; 
11CA: D7              RST     0X10                ; 
11CB: 04              INC     B                   ; 
11CC: 10 20           DJNZ    $11EE               ; {}
11CE: C1              POP     BC                  ; 
11CF: 79              LD      A,C                 ; 
11D0: CD F5 11        CALL    $11F5               ; {}
11D3: 78              LD      A,B                 ; 
11D4: FE 05           CP      $05                 ; 
11D6: 38 08           JR      C,$11E0             ; {}
11D8: 16 38           LD      D,$38               ; 
11DA: CD 13 12        CALL    $1213               ; {}
11DD: 78              LD      A,B                 ; 
11DE: D6 05           SUB     $05                 ; 
11E0: 47              LD      B,A                 ; 
11E1: 04              INC     B                   ; 
11E2: 10 03           DJNZ    $11E7               ; {}
11E4: C3 7E 13        JP      $137E               ; {}
11E7: 16 36           LD      D,$36               ; 
11E9: CD 13 12        CALL    $1213               ; {}
11EC: 18 F4           JR      $11E2               ; {}
11EE: 3E 04           LD      A,$04               ; 
11F0: CD FB 11        CALL    $11FB               ; {}
11F3: 18 D7           JR      $11CC               ; {}
11F5: A7              AND     A                   ; 
11F6: C8              RET     Z                   ; 
11F7: FE 04           CP      $04                 ; 
11F9: 28 07           JR      Z,$1202             ; {}
11FB: 07              RLCA                        ; 
11FC: 07              RLCA                        ; 
11FD: C6 36           ADD     $36                 ; 
11FF: 57              LD      D,A                 ; 
1200: 18 0A           JR      $120C               ; {}
1202: 16 42           LD      D,$42               ; 
1204: CD 13 12        CALL    $1213               ; {}
1207: CD 28 12        CALL    $1228               ; {}
120A: 16 3A           LD      D,$3A               ; 
120C: CD 13 12        CALL    $1213               ; {}
120F: CD 28 12        CALL    $1228               ; {}
1212: C9              RET                         ; 
1213: 08              EX      AF,AF'              ; 
1214: 38 11           JR      C,$1227             ; {}
1216: 08              EX      AF,AF'              ; 
1217: 3A A0 92        LD      A,($92A0)           ; 
121A: C6 08           ADD     $08                 ; 
121C: 5F              LD      E,A                 ; 
121D: 3A A0 92        LD      A,($92A0)           ; 
1220: 93              SUB     E                   ; 
1221: 20 FA           JR      NZ,$121D            ; {}
1223: 08              EX      AF,AF'              ; 
1224: 32 B5 9A        LD      ($9AB5),A           ; 
1227: 08              EX      AF,AF'              ; 

1228: 72              LD      (HL),D              ; 
1229: 14              INC     D                   ; 
122A: CB ED           SET     5,L                 ; 
122C: 72              LD      (HL),D              ; 
122D: 14              INC     D                   ; 
122E: CB D4           SET     2,H                 ; 
1230: 7A              LD      A,D                 ; 
1231: E6 0C           AND     $0C                 ; 
1233: FE 08           CP      $08                 ; 
1235: 3E 01           LD      A,$01               ; 
1237: 28 01           JR      Z,$123A             ; {}
1239: 3C              INC     A                   ; 
123A: 77              LD      (HL),A              ; 
123B: CB AD           RES     5,L                 ; 
123D: 77              LD      (HL),A              ; 
123E: CB 94           RES     2,H                 ; 
1240: 2D              DEC     L                   ; 
1241: C9              RET                         ; 

1242: 21 5B 12        LD      HL,$125B            ; 
1245: 11 00 90        LD      DE,$9000            ; 
1248: 01 20 00        LD      BC,$0020            ; 
124B: C5              PUSH    BC                  ; 
124C: E5              PUSH    HL                  ; 
124D: ED B0           LDIR                        ; 
124F: E1              POP     HL                  ; 
1250: C1              POP     BC                  ; 
1251: 11 E0 98        LD      DE,$98E0            ; 
1254: ED B0           LDIR                        ; 
1256: AF              XOR     A                   ; 
1257: 32 00 90        LD      ($9000),A           ; 
125A: C9              RET                         ; 

125B: 1F              RRA                         ; 
125C: 01 00 00        LD      BC,$0000            ; 
125F: 00              NOP                         ; 
1260: 01 00 00        LD      BC,$0000            ; 
1263: 00              NOP                         ; 
1264: 00              NOP                         ; 
1265: 00              NOP                         ; 
1266: 00              NOP                         ; 
1267: 01 01 00        LD      BC,$0001            ; 
126A: 01 00 00        LD      BC,$0000            ; 
126D: 00              NOP                         ; 
126E: 00              NOP                         ; 
126F: 00              NOP                         ; 
1270: 00              NOP                         ; 
1271: 00              NOP                         ; 
1272: 01 00 00        LD      BC,$0000            ; 
1275: 00              NOP                         ; 
1276: 00              NOP                         ; 
1277: 00              NOP                         ; 
1278: 00              NOP                         ; 
1279: 00              NOP                         ; 
127A: 0A              LD      A,(BC)              ; 

; Something to do with drawing shot sprites
127B: 21 64 8B        LD      HL,$8B64            ; 
127E: 11 30 09        LD      DE,$0930            ; Player
1281: 0E 00           LD      C,$00               ; Player
1283: 06 0A           LD      B,$0A               ; Loop 10 times
1285: 73              LD      (HL),E              ; Set to color 30
1286: 26 93           LD      H,$93               ; Sprite position
1288: 36 00           LD      (HL),$00            ; 
128A: 26 9B           LD      H,$9B               ; 
128C: 71              LD      (HL),C              ; Sprite control = 0 (or 1)
128D: 26 8B           LD      H,$8B               ; Sprite color
128F: 2C              INC     L                   ; 
1290: 72              LD      (HL),D              ; #09 (or 0B)
1291: 2C              INC     L                   ; 
1292: 78              LD      A,B                 ; 
1293: FE 09           CP      $09                 ; 
1295: 20 04           JR      NZ,$129B            ; {} No -- do it
1297: 0E 01           LD      C,$01               ; Bee ...
1299: 16 0B           LD      D,$0B               ; ... shots
129B: 10 E8           DJNZ    $1285               ; {} Do all shots
129D: C9              RET                         ; 

;
129E: 26 8B           LD      H,$8B               ; 
12A0: ED 5B 80 92     LD      DE,($9280)          ; 
12A4: 1A              LD      A,(DE)              ; 
12A5: 6F              LD      L,A                 ; 
12A6: 13              INC     DE                  ; 
12A7: 1A              LD      A,(DE)              ; 
12A8: 4F              LD      C,A                 ; 
12A9: E6 78           AND     $78                 ; 
12AB: C6 06           ADD     $06                 ; 
12AD: 77              LD      (HL),A              ; 
12AE: 2C              INC     L                   ; 
12AF: 79              LD      A,C                 ; 
12B0: E6 07           AND     $07                 ; 
12B2: CB 79           BIT     7,C                 ; 
12B4: 28 02           JR      Z,$12B8             ; {}
12B6: F6 08           OR      $08                 ; 
12B8: 77              LD      (HL),A              ; 
12B9: 13              INC     DE                  ; 
12BA: 2D              DEC     L                   ; 
12BB: 26 88           LD      H,$88               ; Bee descriptors
12BD: 36 01           LD      (HL),$01            ; 
12BF: 26 93           LD      H,$93               ; Sprite control
12C1: 1A              LD      A,(DE)              ; 
12C2: 77              LD      (HL),A              ; 
12C3: 13              INC     DE                  ; 
12C4: 2C              INC     L                   ; 
12C5: 1A              LD      A,(DE)              ; 
12C6: CB 27           SLA     A                   ; 
12C8: 77              LD      (HL),A              ; 
12C9: 3E 00           LD      A,$00               ; 
12CB: 17              RLA                         ; 
12CC: 26 9B           LD      H,$9B               ; Sprite color
12CE: 77              LD      (HL),A              ; 
12CF: 13              INC     DE                  ; 
12D0: ED 53 80 92     LD      ($9280),DE          ; 
12D4: C9              RET                         ; 

12D5: DD 6F           LD      IXL,A               ; 
12D7: 3A 15 92        LD      A,($9215)           ; 
12DA: 4F              LD      C,A                 ; 
12DB: 21 00 99        LD      HL,$9900            ; 
12DE: 11 21 13        LD      DE,$1321            ; 
12E1: 06 10           LD      B,$10               ; 
12E3: 36 00           LD      (HL),$00            ; 
12E5: 2C              INC     L                   ; 
12E6: 1A              LD      A,(DE)              ; 
12E7: 13              INC     DE                  ; 
12E8: 77              LD      (HL),A              ; 
12E9: 2C              INC     L                   ; 
12EA: 10 F7           DJNZ    $12E3               ; {}
12EC: 21 00 98        LD      HL,$9800            ; 
12EF: 11 21 13        LD      DE,$1321            ; 
12F2: 06 0A           LD      B,$0A               ; 
12F4: 1A              LD      A,(DE)              ; 
12F5: 13              INC     DE                  ; 
12F6: CB 41           BIT     0,C                 ; 
12F8: 28 03           JR      Z,$12FD             ; {}
12FA: C6 0D           ADD     $0D                 ; 
12FC: 2F              CPL                         ; 
12FD: 77              LD      (HL),A              ; 
12FE: 2C              INC     L                   ; 
12FF: 2C              INC     L                   ; 
1300: 10 F2           DJNZ    $12F4               ; {}
1302: 06 06           LD      B,$06               ; 
1304: 1A              LD      A,(DE)              ; 
1305: DD 85           ADD     A,IXL               ; 
1307: 13              INC     DE                  ; 
1308: CB 41           BIT     0,C                 ; 
130A: 20 03           JR      NZ,$130F            ; {}
130C: C6 4F           ADD     $4F                 ; 
130E: 2F              CPL                         ; 
130F: CB 27           SLA     A                   ; 
1311: 77              LD      (HL),A              ; 
1312: 2C              INC     L                   ; 
1313: 3E 00           LD      A,$00               ; 
1315: 17              RLA                         ; 
1316: 77              LD      (HL),A              ; 
1317: 2C              INC     L                   ; 
1318: 10 EA           DJNZ    $1304               ; {}
131A: 3A 15 92        LD      A,($9215)           ; 
131D: 32 0F 92        LD      ($920F),A           ; 
1320: C9              RET                         ; 
1321: 31 41 51        LD      SP,$5141            ; 
1324: 61              LD      H,C                 ; 
1325: 71              LD      (HL),C              ; 
1326: 81              ADD     A,C                 ; 
1327: 91              SUB     C                   ; 
1328: A1              AND     C                   ; 
1329: B1              OR      C                   ; 
132A: C1              POP     BC                  ; 
132B: 92              SUB     D                   ; 
132C: 8A              ADC     A,D                 ; 
132D: 82              ADD     A,D                 ; 
132E: 7C              LD      A,H                 ; 
132F: 76              HALT                        ; 
1330: 70              LD      (HL),B              ; 
1331: E5              PUSH    HL                  ; 
1332: 21 AF 92        LD      HL,$92AF            ; 
1335: 36 03           LD      (HL),$03            ; 
1337: 7E              LD      A,(HL)              ; 
1338: A7              AND     A                   ; 
1339: 20 FC           JR      NZ,$1337            ; {}
133B: E1              POP     HL                  ; 
133C: C9              RET                         ; 
133D: 3E 01           LD      A,$01               ; 
133F: 32 14 90        LD      ($9014),A           ; 
1342: 3A 70 82        LD      A,($8270)           ; 
1345: FE 24           CP      $24                 ; 
1347: 20 03           JR      NZ,$134C            ; {}
1349: 0E 03           LD      C,$03               ; 
134B: F7              RST     0X30                ; 

134C: 3A 87 92        LD      A,($9287)           ; 
134F: A7              AND     A                   ; 
1350: 20 FA           JR      NZ,$134C            ; {}
1352: CD 7E 13        CALL    $137E               ; {}
1355: 21 06 09        LD      HL,$0906            ; 
1358: 22 62 8B        LD      ($8B62),HL          ; 
135B: 21 62 93        LD      HL,$9362            ; 
135E: 3A 15 92        LD      A,($9215)           ; 
1361: E6 01           AND     $01                 ; 
1363: 3E 29           LD      A,$29               ; 
1365: 0E 01           LD      C,$01               ; 
1367: 28 03           JR      Z,$136C             ; {}
1369: C6 0E           ADD     $0E                 ; 
136B: 0D              DEC     C                   ; 
136C: 36 7A           LD      (HL),$7A            ; 
136E: 2C              INC     L                   ; 
136F: 77              LD      (HL),A              ; 
1370: 26 9B           LD      H,$9B               ; 
1372: 71              LD      (HL),C              ; 
1373: 2D              DEC     L                   ; 
1374: AF              XOR     A                   ; 
1375: 77              LD      (HL),A              ; 
1376: 32 13 92        LD      ($9213),A           ; 
1379: 3C              INC     A                   ; 
137A: 32 B9 99        LD      ($99B9),A           ; 
137D: C9              RET                         ; 

137E: 3A 20 98        LD      A,($9820)           ; 
1381: 2F              CPL                         ; 
1382: C6 09           ADD     $09                 ; 
1384: 5F              LD      E,A                 ; 
1385: 16 49           LD      D,$49               ; 
1387: 21 1D 80        LD      HL,$801D            ; 
138A: CD 98 13        CALL    $1398               ; {}
138D: 2D              DEC     L                   ; 
138E: CD 98 13        CALL    $1398               ; {}
1391: CB ED           SET     5,L                 ; 
1393: 2C              INC     L                   ; 
1394: CD 98 13        CALL    $1398               ; {}
1397: 2D              DEC     L                   ; 
1398: E5              PUSH    HL                  ; 
1399: 14              INC     D                   ; 
139A: 4A              LD      C,D                 ; 
139B: 06 08           LD      B,$08               ; 
139D: 78              LD      A,B                 ; 
139E: BB              CP      E                   ; 
139F: 20 02           JR      NZ,$13A3            ; {}
13A1: 0E 24           LD      C,$24               ; 
13A3: 7E              LD      A,(HL)              ; 
13A4: FE 36           CP      $36                 ; 
13A6: 38 04           JR      C,$13AC             ; {}
13A8: FE 4A           CP      $4A                 ; 
13AA: 38 01           JR      C,$13AD             ; {}
13AC: 71              LD      (HL),C              ; 
13AD: 2D              DEC     L                   ; 
13AE: 2D              DEC     L                   ; 
13AF: 10 EC           DJNZ    $139D               ; {}
13B1: E1              POP     HL                  ; 
13B2: C9              RET                         ; 

; 
13B3: A7              AND     A                   ; 
13B4: 08              EX      AF,AF'              ; 
13B5: D5              PUSH    DE                  ; 
13B6: EB              EX      DE,HL               ; 
13B7: 79              LD      A,C                 ; 
13B8: 21 EF 13        LD      HL,$13EF            ; Vector into giant data block
13BB: CF              RST     0X08                ; Add A*2 to HL (add 100 it A=0)
13BC: 7E              LD      A,(HL)              ; 
13BD: 23              INC     HL                  ; 
13BE: 66              LD      H,(HL)              ; 
13BF: 6F              LD      L,A                 ; 
13C0: 08              EX      AF,AF'              ; 
13C1: 30 06           JR      NC,$13C9            ; {}
13C3: 2B              DEC     HL                  ; 
13C4: 2B              DEC     HL                  ; 
13C5: 5E              LD      E,(HL)              ; 
13C6: 23              INC     HL                  ; 
13C7: 56              LD      D,(HL)              ; 
13C8: 23              INC     HL                  ; 
13C9: 4E              LD      C,(HL)              ; 
13CA: 23              INC     HL                  ; 
13CB: EB              EX      DE,HL               ; 
13CC: 1A              LD      A,(DE)              ; 
13CD: FE 2F           CP      $2F                 ; 
13CF: 28 1E           JR      Z,$13EF             ; {}
13D1: D6 30           SUB     $30                 ; 
13D3: 30 04           JR      NC,$13D9            ; {}
13D5: 3E 24           LD      A,$24               ; 
13D7: 18 06           JR      $13DF               ; {}
13D9: FE 11           CP      $11                 ; 
13DB: 38 02           JR      C,$13DF             ; {}
13DD: D6 07           SUB     $07                 ; 
13DF: 77              LD      (HL),A              ; 
13E0: CB D4           SET     2,H                 ; 
13E2: 71              LD      (HL),C              ; 
13E3: CB 94           RES     2,H                 ; 
13E5: 13              INC     DE                  ; 
13E6: 7D              LD      A,L                 ; 
13E7: D6 20           SUB     $20                 ; 
13E9: 6F              LD      L,A                 ; 
13EA: 30 E0           JR      NC,$13CC            ; {}
13EC: 25              DEC     H                   ; 
13ED: 18 DD           JR      $13CC               ; {}
13EF: D1              POP     DE                  ; 
13F0: C9              RET                         ; 

; Looks like a giant data block
;
13F1: 2F              CPL                         ; #
13F2: 14              INC     D                   ; #
13F3: 44              LD      B,H                 ; #
13F4: 14              INC     D                   ; #
13F5: 51              LD      D,C                 ; #
13F6: 14              INC     D                   ; #
13F7: 5C              LD      E,H                 ; #
13F8: 14              INC     D                   ; #
13F9: 66              LD      H,(HL)              ; #
13FA: 14              INC     D                   ; #
13FB: 72              LD      (HL),D              ; #
13FC: 14              INC     D                   ; #
13FD: 7C              LD      A,H                 ; #
13FE: 14              INC     D                   ; #
13FF: 91              SUB     C                   ; #
1400: 14              INC     D                   ; #
1401: A3              AND     E                   ; #
1402: 14              INC     D                   ; #
1403: AE              XOR     (HL)                ; #
1404: 14              INC     D                   ; #
1405: C2 14 E1        JP      NZ,$E114            ; #
1408: 14              INC     D                   ; #
1409: EE 14           XOR     $14                 ; #
140B: 09              ADD     HL,BC               ; #
140C: 15              DEC     D                   ; #
140D: 13              INC     DE                  ; #
140E: 15              DEC     D                   ; #
140F: 22 15 2F        LD      ($2F15),HL          ; {} #
1412: 15              DEC     D                   ; #
1413: 3C              INC     A                   ; #
1414: 15              DEC     D                   ; #
1415: 40              LD      B,B                 ; #
1416: 15              DEC     D                   ; #
1417: 59              LD      E,C                 ; #
1418: 15              DEC     D                   ; #
1419: 5D              LD      E,L                 ; #
141A: 15              DEC     D                   ; #
141B: 6A              LD      L,D                 ; #
141C: 15              DEC     D                   ; #
141D: 81              ADD     A,C                 ; #
141E: 15              DEC     D                   ; #
141F: 8F              ADC     A,A                 ; #
1420: 15              DEC     D                   ; #
1421: A8              XOR     B                   ; #
1422: 15              DEC     D                   ; #
1423: BF              CP      A                   ; #
1424: 15              DEC     D                   ; #
1425: C5              PUSH    BC                  ; #
1426: 15              DEC     D                   ; #
1427: D9              EXX                         ; #
1428: 15              DEC     D                   ; #
1429: ED 15                               ; #
142B: FF              RST     0X38                ; #
142C: 15              DEC     D                   ; #
142D: EB              EX      DE,HL               ; #
142E: 82              ADD     A,D                 ; #
142F: 00              NOP                         ; #
1430: 50              LD      D,B                 ; #
1431: 55              LD      D,L                 ; #
1432: 53              LD      D,E                 ; #
1433: 48              LD      C,B                 ; #
1434: 20 53           JR      NZ,$1489            ; {} #
1436: 54              LD      D,H                 ; #
1437: 41              LD      B,C                 ; #
1438: 52              LD      D,D                 ; #
1439: 54              LD      D,H                 ; #
143A: 20 42           JR      NZ,$147E            ; {} #
143C: 55              LD      D,L                 ; #
143D: 54              LD      D,H                 ; #
143E: 54              LD      D,H                 ; #
143F: 4F              LD      C,A                 ; #
1440: 4E              LD      C,(HL)              ; #
1441: 2F              CPL                         ; #
1442: 70              LD      (HL),B              ; #
1443: 82              ADD     A,D                 ; #
1444: 00              NOP                         ; #
1445: 47              LD      B,A                 ; #
1446: 41              LD      B,C                 ; #
1447: 4D              LD      C,L                 ; #
1448: 45              LD      B,L                 ; #
1449: 20 4F           JR      NZ,$149A            ; {} #
144B: 56              LD      D,(HL)              ; #
144C: 45              LD      B,L                 ; #
144D: 52              LD      D,D                 ; #
144E: 2F              CPL                         ; #
144F: 70              LD      (HL),B              ; #
1450: 82              ADD     A,D                 ; #
1451: 00              NOP                         ; #
1452: 52              LD      D,D                 ; #
1453: 45              LD      B,L                 ; #
1454: 41              LD      B,C                 ; #
1455: 44              LD      B,H                 ; #
1456: 59              LD      E,C                 ; #
1457: 20 21           JR      NZ,$147A            ; {} #
1459: 2F              CPL                         ; #
145A: 50              LD      D,B                 ; #
145B: 82              ADD     A,D                 ; #
145C: 00              NOP                         ; #
145D: 50              LD      D,B                 ; #
145E: 4C              LD      C,H                 ; #
145F: 41              LD      B,C                 ; #
1460: 59              LD      E,C                 ; #
1461: 45              LD      B,L                 ; #
1462: 52              LD      D,D                 ; #
1463: 20 31           JR      NZ,$1496            ; {} #
1465: 2F              CPL                         ; #
1466: 00              NOP                         ; #
1467: 50              LD      D,B                 ; #
1468: 4C              LD      C,H                 ; #
1469: 41              LD      B,C                 ; #
146A: 59              LD      E,C                 ; #
146B: 45              LD      B,L                 ; #
146C: 52              LD      D,D                 ; #
146D: 20 32           JR      NZ,$14A1            ; {} #
146F: 2F              CPL                         ; #
1470: 70              LD      (HL),B              ; #
1471: 82              ADD     A,D                 ; #
1472: 00              NOP                         ; #
1473: 53              LD      D,E                 ; #
1474: 54              LD      D,H                 ; #
1475: 41              LD      B,C                 ; #
1476: 47              LD      B,A                 ; #
1477: 45              LD      B,L                 ; #
1478: 20 2F           JR      NZ,$14A9            ; {} #
147A: 10 83           DJNZ    $13FF               ; {} #
147C: 00              NOP                         ; #
147D: 43              LD      B,E                 ; #
147E: 48              LD      C,B                 ; #
147F: 41              LD      B,C                 ; #
1480: 4C              LD      C,H                 ; #
1481: 4C              LD      C,H                 ; #
1482: 45              LD      B,L                 ; #
1483: 4E              LD      C,(HL)              ; #
1484: 47              LD      B,A                 ; #
1485: 49              LD      C,C                 ; #
1486: 4E              LD      C,(HL)              ; #
1487: 47              LD      B,A                 ; #
1488: 20 53           JR      NZ,$14DD            ; {} #
148A: 54              LD      D,H                 ; #
148B: 41              LD      B,C                 ; #
148C: 47              LD      B,A                 ; #
148D: 45              LD      B,L                 ; #
148E: 2F              CPL                         ; #
148F: 10 83           DJNZ    $1414               ; {} #
1491: 00              NOP                         ; #
1492: 4E              LD      C,(HL)              ; #
1493: 55              LD      D,L                 ; #
1494: 4D              LD      C,L                 ; #
1495: 42              LD      B,D                 ; #
1496: 45              LD      B,L                 ; #
1497: 52              LD      D,D                 ; #
1498: 20 4F           JR      NZ,$14E9            ; {} #
149A: 46              LD      B,(HL)              ; #
149B: 20 48           JR      NZ,$14E5            ; {} #
149D: 49              LD      C,C                 ; #
149E: 54              LD      D,H                 ; #
149F: 53              LD      D,E                 ; #
14A0: 2F              CPL                         ; #
14A1: B3              OR      E                   ; #
14A2: 82              ADD     A,D                 ; #
14A3: 00              NOP                         ; #
14A4: 42              LD      B,D                 ; #
14A5: 4F              LD      C,A                 ; #
14A6: 4E              LD      C,(HL)              ; #
14A7: 55              LD      D,L                 ; #
14A8: 53              LD      D,E                 ; #
14A9: 20 20           JR      NZ,$14CB            ; {} #
14AB: 2F              CPL                         ; #
14AC: F1              POP     AF                  ; #
14AD: 82              ADD     A,D                 ; #
14AE: 04              INC     B                   ; #
14AF: 46              LD      B,(HL)              ; #
14B0: 49              LD      C,C                 ; #
14B1: 47              LD      B,A                 ; #
14B2: 48              LD      C,B                 ; #
14B3: 54              LD      D,H                 ; #
14B4: 45              LD      B,L                 ; #
14B5: 52              LD      D,D                 ; #
14B6: 20 43           JR      NZ,$14FB            ; {} #
14B8: 41              LD      B,C                 ; #
14B9: 50              LD      D,B                 ; #
14BA: 54              LD      D,H                 ; #
14BB: 55              LD      D,L                 ; #
14BC: 52              LD      D,D                 ; #
14BD: 45              LD      B,L                 ; #
14BE: 44              LD      B,H                 ; #
14BF: 2F              CPL                         ; #
14C0: AD              XOR     L                   ; #
14C1: 83              ADD     A,E                 ; #
14C2: 00              NOP                         ; #
14C3: 20 20           JR      NZ,$14E5            ; {} #
14C5: 20 20           JR      NZ,$14E7            ; {} #
14C7: 20 20           JR      NZ,$14E9            ; {} #
14C9: 20 20           JR      NZ,$14EB            ; {} #
14CB: 20 20           JR      NZ,$14ED            ; {} #
14CD: 20 20           JR      NZ,$14EF            ; {} #
14CF: 20 20           JR      NZ,$14F1            ; {} #
14D1: 20 20           JR      NZ,$14F3            ; {} #
14D3: 20 20           JR      NZ,$14F5            ; {} #
14D5: 20 20           JR      NZ,$14F7            ; {} #
14D7: 20 20           JR      NZ,$14F9            ; {} #
14D9: 20 20           JR      NZ,$14FB            ; {} #
14DB: 20 20           JR      NZ,$14FD            ; {} #
14DD: 20 2F           JR      NZ,$150E            ; {} #
14DF: 6D              LD      L,L                 ; #
14E0: 82              ADD     A,D                 ; #
14E1: 04              INC     B                   ; #
14E2: 50              LD      D,B                 ; #
14E3: 45              LD      B,L                 ; #
14E4: 52              LD      D,D                 ; #
14E5: 46              LD      B,(HL)              ; #
14E6: 45              LD      B,L                 ; #
14E7: 43              LD      B,E                 ; #
14E8: 54              LD      D,H                 ; #
14E9: 20 63           JR      NZ,$154E            ; {} #
14EB: 2F              CPL                         ; #
14EC: 73              LD      (HL),E              ; #
14ED: 83              ADD     A,E                 ; #
14EE: 05              DEC     B                   ; #
14EF: 53              LD      D,E                 ; #
14F0: 50              LD      D,B                 ; #
14F1: 45              LD      B,L                 ; #
14F2: 43              LD      B,E                 ; #
14F3: 49              LD      C,C                 ; #
14F4: 41              LD      B,C                 ; #
14F5: 4C              LD      C,H                 ; #
14F6: 20 42           JR      NZ,$153A            ; {} #
14F8: 4F              LD      C,A                 ; #
14F9: 4E              LD      C,(HL)              ; #
14FA: 55              LD      D,L                 ; #
14FB: 53              LD      D,E                 ; #
14FC: 20 31           JR      NZ,$152F            ; {} #
14FE: 30 30           JR      NC,$1530            ; {} #
1500: 30 30           JR      NC,$1532            ; {} #
1502: 20 50           JR      NZ,$1554            ; {} #
1504: 54              LD      D,H                 ; #
1505: 53              LD      D,E                 ; #
1506: 2F              CPL                         ; #
1507: 42              LD      B,D                 ; #
1508: 82              ADD     A,D                 ; #
1509: 00              NOP                         ; #
150A: 47              LD      B,A                 ; #
150B: 41              LD      B,C                 ; #
150C: 4C              LD      C,H                 ; #
150D: 41              LD      B,C                 ; #
150E: 47              LD      B,A                 ; #
150F: 41              LD      B,C                 ; #
1510: 2F              CPL                         ; #
1511: A5              AND     L                   ; #
1512: 82              ADD     A,D                 ; #
1513: 00              NOP                         ; #
1514: 5D              LD      E,L                 ; #
1515: 5D              LD      E,L                 ; #
1516: 20 53           JR      NZ,$156B            ; {} #
1518: 43              LD      B,E                 ; #
1519: 4F              LD      C,A                 ; #
151A: 52              LD      D,D                 ; #
151B: 45              LD      B,L                 ; #
151C: 20 5D           JR      NZ,$157B            ; {} #
151E: 5D              LD      E,L                 ; #
151F: 2F              CPL                         ; #
1520: 28 82           JR      Z,$14A4             ; {} #
1522: 00              NOP                         ; #
1523: 35              DEC     (HL)                ; #
1524: 30 20           JR      NC,$1546            ; {} #
1526: 20 20           JR      NZ,$1548            ; {} #
1528: 20 31           JR      NZ,$155B            ; {} #
152A: 30 30           JR      NC,$155C            ; {} #
152C: 2F              CPL                         ; #
152D: 2A 82 00        LD      HL,($0082)          ; {} #
1530: 38 30           JR      C,$1562             ; {} #
1532: 20 20           JR      NZ,$1554            ; {} #
1534: 20 20           JR      NZ,$1556            ; {} #
1536: 31 36 30        LD      SP,$3036            ; #
1539: 2F              CPL                         ; #
153A: 2B              DEC     HL                  ; #
153B: 82              ADD     A,D                 ; #
153C: 00              NOP                         ; #
153D: 2F              CPL                         ; #
153E: 3B              DEC     SP                  ; #
153F: 83              ADD     A,E                 ; #
1540: 03              INC     BC                  ; #
1541: 65              LD      H,L                 ; #
1542: 20 31           JR      NZ,$1575            ; {} #
1544: 39              ADD     HL,SP               ; #
1545: 38 31           JR      C,$1578             ; {} #
1547: 20 4D           JR      NZ,$1596            ; {} #
1549: 49              LD      C,C                 ; #
154A: 44              LD      B,H                 ; #
154B: 57              LD      D,A                 ; #
154C: 41              LD      B,C                 ; #
154D: 59              LD      E,C                 ; #
154E: 20 4D           JR      NZ,$159D            ; {} #
1550: 46              LD      B,(HL)              ; #
1551: 47              LD      B,A                 ; #
1552: 61              LD      H,C                 ; #
1553: 43              LD      B,E                 ; #
1554: 4F              LD      C,A                 ; #
1555: 61              LD      H,C                 ; #
1556: 2F              CPL                         ; #
1557: 5E              LD      E,(HL)              ; #
1558: 82              ADD     A,D                 ; #
1559: 04              INC     B                   ; #
155A: 2F              CPL                         ; #
155B: 8F              ADC     A,A                 ; #
155C: 82              ADD     A,D                 ; #
155D: 04              INC     B                   ; #
155E: 5D              LD      E,L                 ; #
155F: 52              LD      D,D                 ; #
1560: 45              LD      B,L                 ; #
1561: 53              LD      D,E                 ; #
1562: 55              LD      D,L                 ; #
1563: 4C              LD      C,H                 ; #
1564: 54              LD      D,H                 ; #
1565: 53              LD      D,E                 ; #
1566: 5D              LD      E,L                 ; #
1567: 2F              CPL                         ; #
1568: 32 83 05        LD      ($0583),A           ; {} #
156B: 53              LD      D,E                 ; #
156C: 48              LD      C,B                 ; #
156D: 4F              LD      C,A                 ; #
156E: 54              LD      D,H                 ; #
156F: 53              LD      D,E                 ; #
1570: 20 46           JR      NZ,$15B8            ; {} #
1572: 49              LD      C,C                 ; #
1573: 52              LD      D,D                 ; #
1574: 45              LD      B,L                 ; #
1575: 44              LD      B,H                 ; #
1576: 20 20           JR      NZ,$1598            ; {} #
1578: 20 20           JR      NZ,$159A            ; {} #
157A: 20 20           JR      NZ,$159C            ; {} #
157C: 20 20           JR      NZ,$159E            ; {} #
157E: 20 20           JR      NZ,$15A0            ; {} #
1580: 2F              CPL                         ; #
1581: 05              DEC     B                   ; #
1582: 20 20           JR      NZ,$15A4            ; {} #
1584: 4D              LD      C,L                 ; #
1585: 49              LD      C,C                 ; #
1586: 53              LD      D,E                 ; #
1587: 53              LD      D,E                 ; #
1588: 49              LD      C,C                 ; #
1589: 4C              LD      C,H                 ; #
158A: 45              LD      B,L                 ; #
158B: 53              LD      D,E                 ; #
158C: 2F              CPL                         ; #
158D: 35              DEC     (HL)                ; #
158E: 83              ADD     A,E                 ; #
158F: 05              DEC     B                   ; #
1590: 4E              LD      C,(HL)              ; #
1591: 55              LD      D,L                 ; #
1592: 4D              LD      C,L                 ; #
1593: 42              LD      B,D                 ; #
1594: 45              LD      B,L                 ; #
1595: 52              LD      D,D                 ; #
1596: 20 4F           JR      NZ,$15E7            ; {} #
1598: 46              LD      B,(HL)              ; #
1599: 20 48           JR      NZ,$15E3            ; {} #
159B: 49              LD      C,C                 ; #
159C: 54              LD      D,H                 ; #
159D: 53              LD      D,E                 ; #
159E: 20 20           JR      NZ,$15C0            ; {} #
15A0: 20 20           JR      NZ,$15C2            ; {} #
15A2: 20 20           JR      NZ,$15C4            ; {} #
15A4: 20 2F           JR      NZ,$15D5            ; {} #
15A6: 38 83           JR      C,$152B             ; {} #
15A8: 03              INC     BC                  ; #
15A9: 48              LD      C,B                 ; #
15AA: 49              LD      C,C                 ; #
15AB: 54              LD      D,H                 ; #
15AC: 5D              LD      E,L                 ; #
15AD: 4D              LD      C,L                 ; #
15AE: 49              LD      C,C                 ; #
15AF: 53              LD      D,E                 ; #
15B0: 53              LD      D,E                 ; #
15B1: 20 52           JR      NZ,$1605            ; {} #
15B3: 41              LD      B,C                 ; #
15B4: 54              LD      D,H                 ; #
15B5: 49              LD      C,C                 ; #
15B6: 4F              LD      C,A                 ; #
15B7: 20 20           JR      NZ,$15D9            ; {} #
15B9: 20 20           JR      NZ,$15DB            ; {} #
15BB: 20 20           JR      NZ,$15DD            ; {} #
15BD: 20 2F           JR      NZ,$15EE            ; {} #
15BF: 03              INC     BC                  ; #
15C0: 24              INC     H                   ; #
15C1: 60              LD      H,B                 ; #
15C2: 2F              CPL                         ; #
15C3: 2F              CPL                         ; #
15C4: 83              ADD     A,E                 ; #
15C5: 05              DEC     B                   ; #
15C6: 31 53 54        LD      SP,$5453            ; #
15C9: 20 42           JR      NZ,$160D            ; {} #
15CB: 4F              LD      C,A                 ; #
15CC: 4E              LD      C,(HL)              ; #
15CD: 55              LD      D,L                 ; #
15CE: 53              LD      D,E                 ; #
15CF: 20 46           JR      NZ,$1617            ; {} #
15D1: 4F              LD      C,A                 ; #
15D2: 52              LD      D,D                 ; #
15D3: 20 20           JR      NZ,$15F5            ; {} #
15D5: 20 2F           JR      NZ,$1606            ; {} #
15D7: 32 83 05        LD      ($0583),A           ; {} #
15DA: 32 4E 44        LD      ($444E),A           ; #
15DD: 20 42           JR      NZ,$1621            ; {} #
15DF: 4F              LD      C,A                 ; #
15E0: 4E              LD      C,(HL)              ; #
15E1: 55              LD      D,L                 ; #
15E2: 53              LD      D,E                 ; #
15E3: 20 46           JR      NZ,$162B            ; {} #
15E5: 4F              LD      C,A                 ; #
15E6: 52              LD      D,D                 ; #
15E7: 20 20           JR      NZ,$1609            ; {} #
15E9: 20 2F           JR      NZ,$161A            ; {} #
15EB: 35              DEC     (HL)                ; #
15EC: 83              ADD     A,E                 ; #
15ED: 05              DEC     B                   ; #
15EE: 41              LD      B,C                 ; #
15EF: 4E              LD      C,(HL)              ; #
15F0: 44              LD      B,H                 ; #
15F1: 20 46           JR      NZ,$1639            ; {} #
15F3: 4F              LD      C,A                 ; #
15F4: 52              LD      D,D                 ; #
15F5: 20 45           JR      NZ,$163C            ; {} #
15F7: 56              LD      D,(HL)              ; #
15F8: 45              LD      B,L                 ; #
15F9: 52              LD      D,D                 ; #
15FA: 59              LD      E,C                 ; #
15FB: 20 20           JR      NZ,$161D            ; {} #
15FD: 20 2F           JR      NZ,$162E            ; {} #
15FF: 05              DEC     B                   ; #
1600: 30 30           JR      NC,$1632            ; {} #
1602: 30 30           JR      NC,$1634            ; {} #
1604: 20 50           JR      NZ,$1656            ; {} #
1606: 54              LD      D,H                 ; #
1607: 53              LD      D,E                 ; #
1608: 2F              CPL                         ; #

1609: FF FF FF FF FF FF FF

1610: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
1620: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
1630: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
1640: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
1650: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
1660: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
1670: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
1680: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
1690: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
16A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
16B0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
16C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
16D0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
16E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
16F0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

; PLAY COMMAND 03 (??)
1700: ED 5B 82 92     LD      DE,($9282)          ; 
1704: 1A              LD      A,(DE)              ; 
1705: 07              RLCA                        ; 
1706: 07              RLCA                        ; 
1707: 07              RLCA                        ; 
1708: E6 07           AND     $07                 ; 
170A: 21 13 17        LD      HL,$1713            ; 
170D: CF              RST     0X08                ; 
170E: 7E              LD      A,(HL)              ; 
170F: 23              INC     HL                  ; 
1710: 66              LD      H,(HL)              ; 
1711: 6F              LD      L,A                 ; 
1712: E9              JP      (HL)                ; Sub command

1713: 66 17        ; # These have something to do with
1715: 66 17        ; # The demo play.
1717: 1F 17        ; #
1719: 66 17        ; #
171B: 34 17        ; #
171D: 2D 17        ; #

; Subcommand 02
171F: 3A A0 92        LD      A,($92A0)           ; 
1722: E6 0F           AND     $0F                 ; 
1724: C0              RET     NZ                  ; 
1725: 21 07 92        LD      HL,$9207            ; 
1728: 35              DEC     (HL)                ; 
1729: C0              RET     NZ                  ; 
172A: C3 66 17        JP      $1766               ; {}

; Subcommand 05
172D: CD 15 1F        CALL    $1F15               ; {}
1730: ED 5B 82 92     LD      DE,($9282)          ; 

; Subcommand 04
1734: 1A              LD      A,(DE)              ; 
1735: 21 27 98        LD      HL,$9827            ; 
1738: 5E              LD      E,(HL)              ; 
1739: CB 47           BIT     0,A                 ; 
173B: 20 04           JR      NZ,$1741            ; {}
173D: E6 0A           AND     $0A                 ; 
173F: 18 14           JR      $1755               ; {}
1741: 3A 09 92        LD      A,($9209)           ; 
1744: 6F              LD      L,A                 ; 
1745: 26 93           LD      H,$93               ; 
1747: 3A 62 93        LD      A,($9362)           ; 
174A: 96              SUB     (HL)                ; 
174B: 3E 0A           LD      A,$0A               ; 
174D: 28 06           JR      Z,$1755             ; {}
174F: 3E 08           LD      A,$08               ; 
1751: 38 02           JR      C,$1755             ; {}
1753: 3E 02           LD      A,$02               ; 
1755: CD 98 1F        CALL    $1F98               ; {}
1758: 3A A0 92        LD      A,($92A0)           ; 
175B: E6 03           AND     $03                 ; 
175D: C0              RET     NZ                  ; 
175E: 21 07 92        LD      HL,$9207            ; 
1761: 35              DEC     (HL)                ; 
1762: C0              RET     NZ                  ; 
1763: CD 15 1F        CALL    $1F15               ; {}

; Subcommand 00,01,03
1766: ED 5B 82 92     LD      DE,($9282)          ; 
176A: 1A              LD      A,(DE)              ; 
176B: E6 C0           AND     $C0                 ; 
176D: FE 80           CP      $80                 ; 
176F: 20 01           JR      NZ,$1772            ; {}
1771: 13              INC     DE                  ; 
1772: 13              INC     DE                  ; 
1773: 1A              LD      A,(DE)              ; 
1774: ED 53 82 92     LD      ($9282),DE          ; 
1778: 07              RLCA                        ; 
1779: 07              RLCA                        ; 
177A: 07              RLCA                        ; 
177B: E6 07           AND     $07                 ; 
177D: 21 86 17        LD      HL,$1786            ; 
1780: CF              RST     0X08                ; 
1781: 7E              LD      A,(HL)              ; 
1782: 23              INC     HL                  ; 
1783: 66              LD      H,(HL)              ; 
1784: 6F              LD      L,A                 ; 
1785: E9              JP      (HL)                ; 

1786: 94 17                               ; #
1788: 94 17                               ; #
178A: A1 17                               ; #
178C: A8 17                               ; #
178E: AE 17                              ; #
1790: AE 17                              ; #
1792: 9C 17                              ; #

; Secondsubcommand 00,01
1794: 1A              LD      A,(DE)              ; 
1795: 07              RLCA                        ; 
1796: E6 7E           AND     $7E                 ; 
1798: 32 09 92        LD      ($9209),A           ; 
179B: C9              RET                         ; 

; Secondsubcommand 06
179C: AF              XOR     A                   ; 
179D: 32 03 90        LD      ($9003),A           ; 
17A0: C9              RET                         ; 

; Secondsubcommand 02
17A1: 1A              LD      A,(DE)              ; 
17A2: E6 1F           AND     $1F                 ; 
17A4: 32 07 92        LD      ($9207),A           ; 
17A7: C9              RET                         ; 

; Secondsubcommand 03
17A8: 1A              LD      A,(DE)              ; 
17A9: E6 1F           AND     $1F                 ; 
17AB: 4F              LD      C,A                 ; 
17AC: F7              RST     0X30                ; 
17AD: C9              RET                         ; 

; Secondsubcommand 04,05
17AE: 13              INC     DE                  ; 
17AF: 1A              LD      A,(DE)              ; 
17B0: 18 F2           JR      $17A4               ; {}

; PLAY COMMAND 02 (??)
17B2: 3A 01 92        LD      A,($9201)           ; 
17B5: 3D              DEC     A                   ; 
17B6: C0              RET     NZ                  ; 
17B7: 3A 03 92        LD      A,($9203)           ; 
17BA: 21 C3 17        LD      HL,$17C3            ; 
17BD: CF              RST     0X08                ; 
17BE: 5E              LD      E,(HL)              ; 
17BF: 23              INC     HL                  ; 
17C0: 56              LD      D,(HL)              ; 
17C1: EB              EX      DE,HL               ; 
17C2: E9              JP      (HL)                ; 

17C3: 40 19       ; # Looks like more demo 
17C5: 48 19       ; # routines
17C7: 84 19       ; #
17C9: D9 18       ; #
17CB: D1 18       ; #
17CD: AC 18       ; #
17CF: 40 19       ; #
17D1: F5 17       ; #
17D3: 52 18       ; #
17D5: D1 18       ; #
17D7: 08 18       ; #
17D9: D1 18       ; #
17DB: 40 18       ; #
17DD: 40 19       ; #
17DF: E1 17       ; # Do High Score stuff

17E1: 3A AF 92        LD      A,($92AF)           ; 
17E4: A7              AND     A                   ; 
17E5: 28 05           JR      Z,$17EC             ; {}
17E7: 3D              DEC     A                   ; 
17E8: CA A7 19        JP      Z,$19A7             ; {}
17EB: C9              RET                         ; 

17EC: CD 14 32        CALL    $3214               ; {}
17EF: 3E 0A           LD      A,$0A               ; 
17F1: 32 AF 92        LD      ($92AF),A           ; 
17F4: C9              RET                         ; 

17F5: 3A A0 92        LD      A,($92A0)           ; 
17F8: E6 1F           AND     $1F                 ; 
17FA: FE 1F           CP      $1F                 ; 
17FC: C0              RET     NZ                  ; 
17FD: 3E 01           LD      A,$01               ; 
17FF: 32 05 90        LD      ($9005),A           ; 
1802: 0E 02           LD      C,$02               ; 
1804: F7              RST     0X30                ; 
1805: C3 A7 19        JP      $19A7               ; {}

1808: CD 4C 13        CALL    $134C               ; {}
180B: 21 1F 18        LD      HL,$181F            ; 
180E: 22 82 92        LD      ($9282),HL          ; 
1811: 3E 01           LD      A,$01               ; 
1813: 32 03 90        LD      ($9003),A           ; 
1816: 32 15 90        LD      ($9015),A           ; 
1819: 32 25 90        LD      ($9025),A           ; 
181C: C3 A7 19        JP      $19A7               ; {}

181F: 08              EX      AF,AF'              ; 
1820: 18 8A           JR      $17AC               ; {}

1822: 08              EX      AF,AF'              ; 
1823: 88              ADC     A,B                 ; 
1824: 06 81           LD      B,$81               ; 
1826: 28 81           JR      Z,$17A9             ; {}
1828: 05              DEC     B                   ; 
1829: 54              LD      D,H                 ; 
182A: 1A              LD      A,(DE)              ; 
182B: 88              ADC     A,B                 ; 
182C: 12              LD      (DE),A              ; 
182D: 81              ADD     A,C                 ; 
182E: 0F              RRCA                        ; 
182F: A2              AND     D                   ; 
1830: 16 AA           LD      D,$AA               ; 
1832: 14              INC     D                   ; 
1833: 88              ADC     A,B                 ; 
1834: 18 88           JR      $17BE               ; {}
1836: 10 43           DJNZ    $187B               ; {}
1838: 82              ADD     A,D                 ; 
1839: 10 88           DJNZ    $17C3               ; {}
183B: 06 A2           LD      B,$A2               ; 
183D: 20 56           JR      NZ,$1895            ; {}
183F: C0              RET     NZ                  ; 
1840: EF              RST     0X28                ; 
1841: CD 42 12        CALL    $1242               ; {}
1844: AF              XOR     A                   ; 
1845: 32 10 90        LD      ($9010),A           ; 
1848: 32 0B 92        LD      ($920B),A           ; Disable shots
184B: 3C              INC     A                   ; 
184C: 32 02 90        LD      ($9002),A           ; 
184F: C3 A7 19        JP      $19A7               ; {}
1852: AF              XOR     A                   ; 
1853: 32 2B 98        LD      ($982B),A           ; 
1856: 3C              INC     A                   ; 
1857: 32 B7 9A        LD      ($9AB7),A           ; 
185A: 32 21 98        LD      ($9821),A           ; 
185D: 32 03 90        LD      ($9003),A           ; 
1860: 32 15 90        LD      ($9015),A           ; 
1863: 32 25 98        LD      ($9825),A           ; 
1866: 21 87 18        LD      HL,$1887            ; 
1869: 22 82 92        LD      ($9282),HL          ; 
186C: CD C5 01        CALL    $01C5               ; {}
186F: CD 4C 13        CALL    $134C               ; {}
1872: 3E 01           LD      A,$01               ; 
1874: 32 0B 92        LD      ($920B),A           ; One shot
1877: 32 42 98        LD      ($9842),A           ; 
187A: 32 2C 98        LD      ($982C),A           ; 
187D: 3C              INC     A                   ; 
187E: 32 C4 99        LD      ($99C4),A           ; 
1881: 32 C5 99        LD      ($99C5),A           ; 
1884: C3 A7 19        JP      $19A7               ; {}
1887: 02              LD      (BC),A              ; 
1888: 8A              ADC     A,D                 ; 
1889: 04              INC     B                   ; 
188A: 82              ADD     A,D                 ; 
188B: 07              RLCA                        ; 
188C: AA              XOR     D                   ; 
188D: 28 88           JR      Z,$1817             ; {}
188F: 10 AA           DJNZ    $183B               ; {}
1891: 38 82           JR      C,$1815             ; {}
1893: 12              LD      (DE),A              ; 
1894: AA              XOR     D                   ; 
1895: 20 88           JR      NZ,$181F            ; {}
1897: 14              INC     D                   ; 
1898: AA              XOR     D                   ; 
1899: 20 82           JR      NZ,$181D            ; {}
189B: 06 A8           LD      B,$A8               ; 
189D: 0E A2           LD      C,$A2               ; 
189F: 17              RLA                         ; 
18A0: 88              ADC     A,B                 ; 
18A1: 12              LD      (DE),A              ; 
18A2: A2              AND     D                   ; 
18A3: 14              INC     D                   ; 
18A4: 18 88           JR      $182E               ; {}
18A6: 1B              DEC     DE                  ; 
18A7: 81              ADD     A,C                 ; 
18A8: 2A 5F 4C        LD      HL,($4C5F)          ; 
18AB: C0              RET     NZ                  ; 
18AC: 3A AE 92        LD      A,($92AE)           ; 
18AF: A7              AND     A                   ; 
18B0: 28 09           JR      Z,$18BB             ; {}
18B2: 3D              DEC     A                   ; 
18B3: CA A7 19        JP      Z,$19A7             ; {}
18B6: FE 05           CP      $05                 ; 
18B8: 28 0C           JR      Z,$18C6             ; {}
18BA: C9              RET                         ; 

18BB: 3E 34           LD      A,$34               ; 
18BD: 32 34 92        LD      ($9234),A           ; 
18C0: 3E 09           LD      A,$09               ; 
18C2: 32 AE 92        LD      ($92AE),A           ; 
18C5: C9              RET                         ; 

18C6: AF              XOR     A                   ; 
18C7: 32 62 93        LD      ($9362),A           ; 
18CA: 0E 13           LD      C,$13               ; 
18CC: F7              RST     0X30                ; 
18CD: 0E 14           LD      C,$14               ; 
18CF: F7              RST     0X30                ; 
18D0: C9              RET                         ; 

18D1: 3A 03 90        LD      A,($9003)           ; 
18D4: A7              AND     A                   ; 
18D5: CA A7 19        JP      Z,$19A7             ; {}
18D8: C9              RET                         ; 

18D9: 06 07           LD      B,$07               ; Do this ...
18DB: CD 9E 12        CALL    $129E               ; {} ...
18DE: 10 FB           DJNZ    $18DB               ; {} ... seven times.
18E0: AF              XOR     A                   ; 
18E1: 32 20 98        LD      ($9820),A           ; 
18E4: 32 05 90        LD      ($9005),A           ; 
18E7: CD 4C 13        CALL    $134C               ; {}
18EA: 21 0D FF        LD      HL,$FF0D            ; 
18ED: 22 C5 92        LD      ($92C5),HL          ; 
18F0: 22 C4 92        LD      ($92C4),HL          ; 
18F3: 22 C1 92        LD      ($92C1),HL          ; 
18F6: 22 C0 92        LD      ($92C0),HL          ; 
18F9: 21 28 19        LD      HL,$1928            ; 
18FC: 22 82 92        LD      ($9282),HL          ; 
18FF: AF              XOR     A                   ; 
1900: 06 10           LD      B,$10               ; 
1902: 21 CA 92        LD      HL,$92CA            ; 
1905: DF              RST     0X18                ; 
1906: 32 27 98        LD      ($9827),A           ; 
1909: 32 0B 92        LD      ($920B),A           ; Disable shots
190C: 3C              INC     A                   ; 
190D: 32 2B 98        LD      ($982B),A           ; 
1910: 32 10 90        LD      ($9010),A           ; 
1913: 32 0B 90        LD      ($900B),A           ; 
1916: 32 03 90        LD      ($9003),A           ; 
1919: 3A 03 68        LD      A,($6803)           ; 
191C: 0F              RRCA                        ; 
191D: E6 01           AND     $01                 ; 
191F: 32 B7 9A        LD      ($9AB7),A           ; 
1922: CD 7B 12        CALL    $127B               ; {}
1925: C3 A7 19        JP      $19A7               ; {}

1928: 08              EX      AF,AF'              ; 
1929: 1B              DEC     DE                  ; 
192A: 81              ADD     A,C                 ; 
192B: 3D              DEC     A                   ; 
192C: 81              ADD     A,C                 ; 
192D: 0A              LD      A,(BC)              ; 
192E: 42              LD      B,D                 ; 
192F: 19              ADD     HL,DE               ; 
1930: 81              ADD     A,C                 ; 
1931: 28 81           JR      Z,$18B4             ; {}
1933: 08              EX      AF,AF'              ; 
1934: 18 81           JR      $18B7               ; {}

1936: 2E 81           LD      L,$81               ; 
1938: 03              INC     BC                  ; 
1939: 1A              LD      A,(DE)              ; 
193A: 81              ADD     A,C                 ; 
193B: 11 81 05        LD      DE,$0581            ; 
193E: 42              LD      B,D                 ; 
193F: C0              RET     NZ                  ; 
1940: CD 60 01        CALL    $0160               ; {}
1943: CD 3C 00        CALL    $003C               ; {}
1946: 18 5F           JR      $19A7               ; {}
1948: 21 5C 19        LD      HL,$195C            ; 
194B: 22 80 92        LD      ($9280),HL          ; 
194E: AF              XOR     A                   ; 
194F: 32 05 92        LD      ($9205),A           ; 
1952: 32 A8 92        LD      ($92A8),A           ; 
1955: 3E 02           LD      A,$02               ; 
1957: 32 AE 92        LD      ($92AE),A           ; 
195A: 18 4B           JR      $19A7               ; {}

195C: 08              EX      AF,AF'              ; 
195D: 1B              DEC     DE                  ; 
195E: 44              LD      B,H                 ; 
195F: 3A 0A 12        LD      A,($120A)           ; {}
1962: 44              LD      B,H                 ; 
1963: 42              LD      B,D                 ; 
1964: 0C              INC     C                   ; 
1965: 08              EX      AF,AF'              ; 
1966: 7C              LD      A,H                 ; 
1967: 50              LD      D,B                 ; 
1968: 34              INC     (HL)                ; 
1969: 08              EX      AF,AF'              ; 
196A: 34              INC     (HL)                ; 
196B: 5C              LD      E,H                 ; 
196C: 30 08           JR      NC,$1976            ; {}
196E: 64              LD      H,H                 ; 
196F: 5C              LD      E,H                 ; 
1970: 32 08 94        LD      ($9408),A           ; 
1973: 5C              LD      E,H                 ; 
1974: 4A              LD      C,D                 ; 
1975: 12              LD      (DE),A              ; 
1976: A4              AND     H                   ; 
1977: 64              LD      H,H                 ; 
1978: 36 08           LD      (HL),$08            ; 
197A: C4 5C 58        CALL    NZ,$585C            ; 
197D: 12              LD      (DE),A              ; 
197E: B4              OR      H                   ; 
197F: 64              LD      H,H                 ; 
1980: 52              LD      D,D                 ; 

1981: 12              LD      (DE),A              ; 
1982: D4 64 3A        CALL    NC,$3A64            ; {}
1985: AE              XOR     (HL)                ; 
1986: 92              SUB     D                   ; 
1987: A7              AND     A                   ; 
1988: C0              RET     NZ                  ; 
1989: 3E 02           LD      A,$02               ; 
198B: 32 AE 92        LD      ($92AE),A           ; 
198E: 3A 05 92        LD      A,($9205)           ; 
1991: FE 05           CP      $05                 ; 
1993: 28 12           JR      Z,$19A7             ; {}
1995: 3C              INC     A                   ; 
1996: 32 05 92        LD      ($9205),A           ; 
1999: C6 0D           ADD     $0D                 ; 
199B: 4F              LD      C,A                 ; 
199C: F7              RST     0X30                ; 
199D: 3A 05 92        LD      A,($9205)           ; 
19A0: FE 03           CP      $03                 ; 
19A2: D8              RET     C                   ; 
19A3: CD 9E 12        CALL    $129E               ; {}
19A6: C9              RET                         ; 
19A7: 21 03 92        LD      HL,$9203            ; 
19AA: 34              INC     (HL)                ; 
19AB: 7E              LD      A,(HL)              ; 
19AC: FE 0F           CP      $0F                 ; 
19AE: C0              RET     NZ                  ; 
19AF: 36 00           LD      (HL),$00            ; 
19B1: C9              RET                         ; 

;======================================================================
; PLAY COMMAND 11
;
19B2: 3A 8E 92        LD      A,($928E)           ; 
19B5: A7              AND     A                   ; 
19B6: 20 1A           JR      NZ,$19D2            ; {}
19B8: 21 AD 92        LD      HL,$92AD            ; 
19BB: B6              OR      (HL)                ; 
19BC: 28 28           JR      Z,$19E6             ; {}
19BE: FE 04           CP      $04                 ; 
19C0: 20 05           JR      NZ,$19C7            ; {}
19C2: 3D              DEC     A                   ; 
19C3: 77              LD      (HL),A              ; 
19C4: 32 A9 9A        LD      ($9AA9),A           ; 
19C7: 3A 29 98        LD      A,($9829)           ; 
19CA: C6 0D           ADD     $0D                 ; 
19CC: 6F              LD      L,A                 ; 
19CD: 26 91           LD      H,$91               ; 
19CF: 36 04           LD      (HL),$04            ; 
19D1: C9              RET                         ; 

19D2: 0E 0A           LD      C,$0A               ; 
19D4: F7              RST     0X30                ; 
19D5: 3E 06           LD      A,$06               ; 
19D7: 32 AD 92        LD      ($92AD),A           ; 
19DA: 3C              INC     A                   ; 
19DB: 32 63 8B        LD      ($8B63),A           ; 
19DE: AF              XOR     A                   ; 
19DF: 32 8B 92        LD      ($928B),A           ; 
19E2: 32 8E 92        LD      ($928E),A           ; 
19E5: C9              RET                         ; 

19E6: 3A D1 82        LD      A,($82D1)           ; 
19E9: FE 24           CP      $24                 ; 
19EB: 28 29           JR      Z,$1A16             ; {}
19ED: 21 62 93        LD      HL,$9362            ; 
19F0: 3A 28 98        LD      A,($9828)           ; 
19F3: E6 07           AND     $07                 ; 
19F5: 5F              LD      E,A                 ; 
19F6: 54              LD      D,H                 ; 
19F7: 7E              LD      A,(HL)              ; 
19F8: 12              LD      (DE),A              ; 
19F9: 36 00           LD      (HL),$00            ; 
19FB: 2C              INC     L                   ; 
19FC: 1C              INC     E                   ; 
19FD: 7E              LD      A,(HL)              ; 
19FE: 12              LD      (DE),A              ; 
19FF: 26 9B           LD      H,$9B               ; 
1A01: 54              LD      D,H                 ; 
1A02: ED A8           LDD                         ; 
1A04: ED A0           LDI                         ; 
1A06: 26 8B           LD      H,$8B               ; 
1A08: 6B              LD      L,E                 ; 
1A09: 36 07           LD      (HL),$07            ; 
1A0B: 2D              DEC     L                   ; 
1A0C: 36 07           LD      (HL),$07            ; 
1A0E: 0E 0B           LD      C,$0B               ; 
1A10: 21 B1 83        LD      HL,$83B1            ; 
1A13: CD B3 13        CALL    $13B3               ; {}
1A16: 3A 28 98        LD      A,($9828)           ; 
1A19: 6F              LD      L,A                 ; 
1A1A: E6 07           AND     $07                 ; 
1A1C: 5F              LD      E,A                 ; 
1A1D: 26 88           LD      H,$88               ; 
1A1F: 3A 15 92        LD      A,($9215)           ; 
1A22: 4F              LD      C,A                 ; 
1A23: 7E              LD      A,(HL)              ; 
1A24: FE 09           CP      $09                 ; 
1A26: 20 1D           JR      NZ,$1A45            ; {}
1A28: 26 93           LD      H,$93               ; 
1A2A: 54              LD      D,H                 ; 
1A2B: 7E              LD      A,(HL)              ; 
1A2C: 12              LD      (DE),A              ; 
1A2D: 2C              INC     L                   ; 
1A2E: 1C              INC     E                   ; 
1A2F: 3E 10           LD      A,$10               ; 
1A31: CB 41           BIT     0,C                 ; 
1A33: 28 02           JR      Z,$1A37             ; {}
1A35: ED 44           NEG                         ; 
1A37: 47              LD      B,A                 ; 
1A38: 86              ADD     A,(HL)              ; 
1A39: 12              LD      (DE),A              ; 
1A3A: 1F              RRA                         ; 
1A3B: A8              XOR     B                   ; 
1A3C: 07              RLCA                        ; 
1A3D: E6 01           AND     $01                 ; 
1A3F: 26 9B           LD      H,$9B               ; 
1A41: 54              LD      D,H                 ; 
1A42: AE              XOR     (HL)                ; FA NOPE
1A43: 12              LD      (DE),A              ; 
1A44: C9              RET                         ; 
1A45: 21 8B 92        LD      HL,$928B            ; 
1A48: 7E              LD      A,(HL)              ; 
1A49: A7              AND     A                   ; 
1A4A: 20 05           JR      NZ,$1A51            ; {}
1A4C: 16 8B           LD      D,$8B               ; 
1A4E: 3E 06           LD      A,$06               ; 
1A50: 12              LD      (DE),A              ; 
1A51: 34              INC     (HL)                ; 
1A52: FE 24           CP      $24                 ; 
1A54: 28 1A           JR      Z,$1A70             ; {}
1A56: 06 01           LD      B,$01               ; 
1A58: CB 41           BIT     0,C                 ; 
1A5A: 20 02           JR      NZ,$1A5E            ; {}
1A5C: 05              DEC     B                   ; 
1A5D: 05              DEC     B                   ; 
1A5E: 6B              LD      L,E                 ; 
1A5F: 2C              INC     L                   ; 
1A60: 26 93           LD      H,$93               ; 
1A62: 78              LD      A,B                 ; 
1A63: 86              ADD     A,(HL)              ; 
1A64: 77              LD      (HL),A              ; 
1A65: 1F              RRA                         ; 
1A66: A8              XOR     B                   ; 
1A67: 07              RLCA                        ; 
1A68: D0              RET     NC                  ; 
1A69: 26 9B           LD      H,$9B               ; 
1A6B: 7E              LD      A,(HL)              ; 
1A6C: EE 01           XOR     $01                 ; 
1A6E: 77              LD      (HL),A              ; 
1A6F: C9              RET                         ; 
1A70: AF              XOR     A                   ; 
1A71: 32 11 90        LD      ($9011),A           ; 
1A74: 32 A9 9A        LD      ($9AA9),A           ; 
1A77: 16 88           LD      D,$88               ; 
1A79: 3C              INC     A                   ; 
1A7A: 12              LD      (DE),A              ; 
1A7B: 32 28 98        LD      ($9828),A           ; 
1A7E: 32 B9 99        LD      ($99B9),A           ; 
1A81: 3C              INC     A                   ; 
1A82: 32 13 92        LD      ($9213),A           ; 
1A85: C9              RET                         ; 

; PLAY COMMAND 04 (??)
1A86: 3A CA 99        LD      A,($99CA)           ; 
1A89: 4F              LD      C,A                 ; 
1A8A: 3A A7 92        LD      A,($92A7)           ; 
1A8D: B9              CP      C                   ; 
1A8E: D0              RET     NC                  ; 
1A8F: 3A 41 98        LD      A,($9841)           ; 
1A92: A7              AND     A                   ; 
1A93: 20 46           JR      NZ,$1ADB            ; {}
1A95: 21 07 88        LD      HL,$8807            ; 
1A98: 01 FF 14        LD      BC,$14FF            ; 
1A9B: 3E 01           LD      A,$01               ; 
1A9D: 2C              INC     L                   ; 
1A9E: ED A1           CPI                         ; 
1AA0: 28 0F           JR      Z,$1AB1             ; {}
1AA2: 10 F9           DJNZ    $1A9D               ; {}
1AA4: 21 3F 88        LD      HL,$883F            ; 
1AA7: 06 10           LD      B,$10               ; 
1AA9: 2C              INC     L                   ; 
1AAA: ED A1           CPI                         ; 
1AAC: 28 03           JR      Z,$1AB1             ; {}
1AAE: 10 F9           DJNZ    $1AA9               ; {}
1AB0: C9              RET                         ; 
1AB1: 3E C0           LD      A,$C0               ; 
1AB3: 32 41 98        LD      ($9841),A           ; 
1AB6: 2D              DEC     L                   ; 
1AB7: 5D              LD      E,L                 ; 
1AB8: 16 8B           LD      D,$8B               ; 
1ABA: 1C              INC     E                   ; 
1ABB: 1A              LD      A,(DE)              ; 
1ABC: 1D              DEC     E                   ; 
1ABD: 4F              LD      C,A                 ; 
1ABE: 3A 21 98        LD      A,($9821)           ; 
1AC1: CB 3F           SRL     A                   ; 
1AC3: CB 3F           SRL     A                   ; 
1AC5: 6F              LD      L,A                 ; 
1AC6: 26 00           LD      H,$00               ; 
1AC8: 3E 03           LD      A,$03               ; 
1ACA: CD 61 10        CALL    $1061               ; {}
1ACD: C6 04           ADD     $04                 ; 
1ACF: 21 2D 98        LD      HL,$982D            ; 
1AD2: 73              LD      (HL),E              ; 
1AD3: 2C              INC     L                   ; 
1AD4: 71              LD      (HL),C              ; 
1AD5: 2C              INC     L                   ; 
1AD6: 77              LD      (HL),A              ; 
1AD7: 32 B2 9A        LD      ($9AB2),A           ; 
1ADA: C9              RET                         ; 
1ADB: 3C              INC     A                   ; 
1ADC: 28 1C           JR      Z,$1AFA             ; {}
1ADE: 32 41 98        LD      ($9841),A           ; 
1AE1: 08              EX      AF,AF'              ; 
1AE2: 21 2D 98        LD      HL,$982D            ; 
1AE5: 5E              LD      E,(HL)              ; 
1AE6: 16 88           LD      D,$88               ; 
1AE8: 1A              LD      A,(DE)              ; 
1AE9: 3D              DEC     A                   ; 
1AEA: C2 5A 1B        JP      NZ,$1B5A            ; {}
1AED: 16 8B           LD      D,$8B               ; 
1AEF: 2C              INC     L                   ; 
1AF0: 08              EX      AF,AF'              ; 
1AF1: CB 67           BIT     4,A                 ; 
1AF3: 28 01           JR      Z,$1AF6             ; {}
1AF5: 2C              INC     L                   ; 
1AF6: 7E              LD      A,(HL)              ; 
1AF7: 1C              INC     E                   ; 
1AF8: 12              LD      (DE),A              ; 
1AF9: C9              RET                         ; 
1AFA: 3A 15 90        LD      A,($9015)           ; 
1AFD: A7              AND     A                   ; 
1AFE: 20 06           JR      NZ,$1B06            ; {}
1B00: 3E E0           LD      A,$E0               ; 
1B02: 32 41 98        LD      ($9841),A           ; 
1B05: C9              RET                         ; 
1B06: 3A 2D 98        LD      A,($982D)           ; 
1B09: 6F              LD      L,A                 ; 
1B0A: 26 88           LD      H,$88               ; 
1B0C: 7E              LD      A,(HL)              ; 
1B0D: 3D              DEC     A                   ; 
1B0E: 20 4A           JR      NZ,$1B5A            ; {}
1B10: 26 92           LD      H,$92               ; 
1B12: 7E              LD      A,(HL)              ; 
1B13: CB 7F           BIT     7,A                 ; 
1B15: 20 43           JR      NZ,$1B5A            ; {}
1B17: 3A 2F 98        LD      A,($982F)           ; 
1B1A: D6 04           SUB     $04                 ; 
1B1C: 21 5F 1B        LD      HL,$1B5F            ; 
1B1F: CF              RST     0X08                ; 
1B20: 11 B0 99        LD      DE,$99B0            ; 
1B23: 3E 03           LD      A,$03               ; 
1B25: 12              LD      (DE),A              ; 
1B26: 1C              INC     E                   ; 
1B27: ED A0           LDI                         ; 
1B29: ED A0           LDI                         ; 
1B2B: 3A 2F 98        LD      A,($982F)           ; 
1B2E: D6 04           SUB     $04                 ; 
1B30: E6 0F           AND     $0F                 ; 
1B32: 4F              LD      C,A                 ; 
1B33: 21 65 1B        LD      HL,$1B65            ; 
1B36: CF              RST     0X08                ; 
1B37: 5E              LD      E,(HL)              ; 
1B38: 23              INC     HL                  ; 
1B39: 56              LD      D,(HL)              ; 
1B3A: 26 8B           LD      H,$8B               ; 
1B3C: 3A 2D 98        LD      A,($982D)           ; 
1B3F: 6F              LD      L,A                 ; 
1B40: 79              LD      A,C                 ; 
1B41: 07              RLCA                        ; 
1B42: 07              RLCA                        ; 
1B43: 07              RLCA                        ; 
1B44: C6 56           ADD     $56                 ; 
1B46: 4E              LD      C,(HL)              ; 
1B47: 77              LD      (HL),A              ; 
1B48: 79              LD      A,C                 ; 
1B49: E6 F8           AND     $F8                 ; 
1B4B: 4F              LD      C,A                 ; 
1B4C: 3A 2E 98        LD      A,($982E)           ; 
1B4F: E6 07           AND     $07                 ; 
1B51: B1              OR      C                   ; 
1B52: 32 2E 98        LD      ($982E),A           ; 
1B55: 26 88           LD      H,$88               ; 
1B57: CD 83 10        CALL    $1083               ; {} Process next moving bee
1B5A: AF              XOR     A                   ; 
1B5B: 32 04 90        LD      ($9004),A           ; 
1B5E: C9              RET                         ; 
1B5F: 1E BD           LD      E,$BD               ; 
1B61: 0A              LD      A,(BC)              ; 
1B62: B8              CP      B                   ; 
1B63: 14              INC     D                   ; 
1B64: BC              CP      H                   ; 
1B65: EA 04 73        JP      PE,$7304            ; #
1B68: 04              INC     B                   ; 
1B69: AB              XOR     E                   ; 
1B6A: 04              INC     B                   ; 

;======================================================================
; PLAY COMMAND 10
;
1B6B: 3A 0B 92        LD      A,($920B)           ; 
1B6E: A7              AND     A                   ; 
1B6F: 28 0A           JR      Z,$1B7B             ; {}
1B71: 3A 15 90        LD      A,($9015)           ; 
1B74: 4F              LD      C,A                 ; 
1B75: 3A 1D 90        LD      A,($901D)           ; 
1B78: 2F              CPL                         ; 
1B79: A1              AND     C                   ; 
1B7A: C8              RET     Z                   ; 
1B7B: 06 04           LD      B,$04               ; 
1B7D: 21 CA 92        LD      HL,$92CA            ; 
1B80: 7E              LD      A,(HL)              ; 
1B81: 3C              INC     A                   ; 
1B82: 20 0D           JR      NZ,$1B91            ; {}
1B84: 2C              INC     L                   ; 
1B85: 2C              INC     L                   ; 
1B86: 2C              INC     L                   ; 
1B87: 10 F7           DJNZ    $1B80               ; {}
1B89: 3A A0 92        LD      A,($92A0)           ; 
1B8C: E6 0F           AND     $0F                 ; 
1B8E: 28 1E           JR      Z,$1BAE             ; {}
1B90: C9              RET                         ; 
1B91: 36 FF           LD      (HL),$FF            ; 
1B93: 3D              DEC     A                   ; 
1B94: 16 88           LD      D,$88               ; 
1B96: 5F              LD      E,A                 ; 
1B97: CB BB           RES     7,E                 ; 
1B99: 08              EX      AF,AF'              ; 
1B9A: 1A              LD      A,(DE)              ; 
1B9B: 3D              DEC     A                   ; 
1B9C: C0              RET     NZ                  ; 
1B9D: 2C              INC     L                   ; 
1B9E: 5E              LD      E,(HL)              ; 
1B9F: 2C              INC     L                   ; 
1BA0: 56              LD      D,(HL)              ; 
1BA1: 08              EX      AF,AF'              ; 
1BA2: 6F              LD      L,A                 ; 
1BA3: 26 88           LD      H,$88               ; 
1BA5: CD 79 10        CALL    $1079               ; {}
1BA8: 3E 01           LD      A,$01               ; 
1BAA: 32 B3 9A        LD      ($9AB3),A           ; 
1BAD: C9              RET                         ; 
1BAE: 21 C0 92        LD      HL,$92C0            ; 
1BB1: 06 03           LD      B,$03               ; 
1BB3: 35              DEC     (HL)                ; 
1BB4: 28 04           JR      Z,$1BBA             ; {}
1BB6: 2C              INC     L                   ; 
1BB7: 10 FA           DJNZ    $1BB3               ; {}
1BB9: C9              RET                         ; 
1BBA: 3A C4 99        LD      A,($99C4)           ; 
1BBD: 4F              LD      C,A                 ; 
1BBE: 3A 87 92        LD      A,($9287)           ; 
1BC1: B9              CP      C                   ; 
1BC2: 38 02           JR      C,$1BC6             ; {}
1BC4: 34              INC     (HL)                ; 
1BC5: C9              RET                         ; 
1BC6: CB D5           SET     2,L                 ; 
1BC8: 7E              LD      A,(HL)              ; 
1BC9: CB 95           RES     2,L                 ; 
1BCB: 77              LD      (HL),A              ; 
1BCC: 78              LD      A,B                 ; 
1BCD: 3D              DEC     A                   ; 
1BCE: 21 D7 1B        LD      HL,$1BD7            ; 
1BD1: CF              RST     0X08                ; 
1BD2: 7E              LD      A,(HL)              ; 
1BD3: 23              INC     HL                  ; 
1BD4: 66              LD      H,(HL)              ; 
1BD5: 6F              LD      L,A                 ; 
1BD6: E9              JP      (HL)                ; 
1BD7: DD 1B           DEC     DE                  ; 
1BD9: FD 1B           DEC     DE                  ; 
1BDB: 07              RLCA                        ; 
1BDC: 1C              INC     E                   ; 
1BDD: 06 14           LD      B,$14               ; 
1BDF: 21 08 88        LD      HL,$8808            ; 
1BE2: 11 4F 03        LD      DE,$034F            ; 
1BE5: 3A 2D 98        LD      A,($982D)           ; 
1BE8: 4F              LD      C,A                 ; 
1BE9: 7E              LD      A,(HL)              ; 
1BEA: 3D              DEC     A                   ; 
1BEB: 20 04           JR      NZ,$1BF1            ; {}
1BED: 79              LD      A,C                 ; 
1BEE: BD              CP      L                   ; 
1BEF: 20 05           JR      NZ,$1BF6            ; {}
1BF1: 2C              INC     L                   ; 
1BF2: 2C              INC     L                   ; 
1BF3: 10 F4           DJNZ    $1BE9               ; {}
1BF5: C9              RET                         ; 
1BF6: 32 B3 9A        LD      ($9AB3),A           ; 
1BF9: CD 83 10        CALL    $1083               ; {} Process next moving bee
1BFC: C9              RET                         ; 
1BFD: 06 10           LD      B,$10               ; 
1BFF: 21 40 88        LD      HL,$8840            ; 
1C02: 11 A9 03        LD      DE,$03A9            ; 
1C05: 18 DE           JR      $1BE5               ; {}
1C07: 3A 2B 98        LD      A,($982B)           ; 
1C0A: A7              AND     A                   ; 
1C0B: 20 29           JR      NZ,$1C36            ; {}
1C0D: 21 2C 98        LD      HL,$982C            ; 
1C10: 34              INC     (HL)                ; 
1C11: CB 46           BIT     0,(HL)              ; 
1C13: 20 21           JR      NZ,$1C36            ; {}
1C15: DD 2E 02        LD      IXL,$02             ; 
1C18: FD 21 54 04     LD      IY,$0454            ; 
1C1C: 11 30 88        LD      DE,$8830            ; 
1C1F: 06 04           LD      B,$04               ; 
1C21: 1A              LD      A,(DE)              ; 
1C22: 3D              DEC     A                   ; 
1C23: 28 05           JR      Z,$1C2A             ; {}
1C25: 1C              INC     E                   ; 
1C26: 1C              INC     E                   ; 
1C27: 10 F8           DJNZ    $1C21               ; {}
1C29: C9              RET                         ; 
1C2A: 3E 01           LD      A,$01               ; 
1C2C: 32 2B 98        LD      ($982B),A           ; 
1C2F: 7B              LD      A,E                 ; 
1C30: 32 28 98        LD      ($9828),A           ; 
1C33: C3 B4 1C        JP      $1CB4               ; {}
1C36: 21 32 1D        LD      HL,$1D32            ; 
1C39: 16 88           LD      D,$88               ; 
1C3B: 01 00 06        LD      BC,$0600            ; 
1C3E: 5E              LD      E,(HL)              ; 
1C3F: 23              INC     HL                  ; 
1C40: 3A 2D 98        LD      A,($982D)           ; 
1C43: BB              CP      E                   ; 
1C44: 28 04           JR      Z,$1C4A             ; {}
1C46: 1A              LD      A,(DE)              ; 
1C47: 3D              DEC     A                   ; 
1C48: D6 01           SUB     $01                 ; 
1C4A: CB 11           RL      C                   ; 
1C4C: 10 F0           DJNZ    $1C3E               ; {}
1C4E: DD 2E 00        LD      IXL,$00             ; 
1C51: 06 04           LD      B,$04               ; 
1C53: DD 61           LD      IXH,C               ; 
1C55: 79              LD      A,C                 ; 
1C56: E6 07           AND     $07                 ; 
1C58: FE 04           CP      $04                 ; 
1C5A: 28 05           JR      Z,$1C61             ; {}
1C5C: FE 03           CP      $03                 ; 
1C5E: D4 93 1C        CALL    NC,$1C93            ; {}
1C61: CB 19           RR      C                   ; 
1C63: 10 F0           DJNZ    $1C55               ; {}
1C65: DD 2C           INC     IXL                 ; 
1C67: DD 4C           LD      C,IXH               ; 
1C69: 06 04           LD      B,$04               ; 
1C6B: 79              LD      A,C                 ; 
1C6C: E6 07           AND     $07                 ; 
1C6E: C4 93 1C        CALL    NZ,$1C93            ; {}
1C71: CB 19           RR      C                   ; 
1C73: 10 F6           DJNZ    $1C6B               ; {}
1C75: DD 2C           INC     IXL                 ; 
1C77: 11 30 88        LD      DE,$8830            ; 
1C7A: 06 04           LD      B,$04               ; 
1C7C: 1A              LD      A,(DE)              ; 
1C7D: 3D              DEC     A                   ; 
1C7E: 28 26           JR      Z,$1CA6             ; {}
1C80: 1C              INC     E                   ; 
1C81: 1C              INC     E                   ; 
1C82: 10 F8           DJNZ    $1C7C               ; {}
1C84: 21 00 88        LD      HL,$8800            ; 
1C87: 06 04           LD      B,$04               ; 
1C89: 7E              LD      A,(HL)              ; 
1C8A: 3D              DEC     A                   ; 
1C8B: CA 2B 1D        JP      Z,$1D2B             ; {}
1C8E: 2C              INC     L                   ; 
1C8F: 2C              INC     L                   ; 
1C90: 10 F7           DJNZ    $1C89               ; {}
1C92: C9              RET                         ; 
1C93: 78              LD      A,B                 ; 
1C94: CB 4F           BIT     1,A                 ; 
1C96: 28 02           JR      Z,$1C9A             ; {}
1C98: EE 01           XOR     $01                 ; 
1C9A: E6 03           AND     $03                 ; 
1C9C: CB 27           SLA     A                   ; 
1C9E: C6 30           ADD     $30                 ; 
1CA0: 5F              LD      E,A                 ; 
1CA1: 1A              LD      A,(DE)              ; 
1CA2: FE 01           CP      $01                 ; 
1CA4: C0              RET     NZ                  ; 
1CA5: E1              POP     HL                  ; 
1CA6: FD 21 11 04     LD      IY,$0411            ; 
1CAA: 3A 0B 92        LD      A,($920B)           ; 
1CAD: A7              AND     A                   ; 
1CAE: 20 04           JR      NZ,$1CB4            ; {}
1CB0: FD 21 F1 00     LD      IY,$00F1            ; 
1CB4: 7B              LD      A,E                 ; 
1CB5: 0F              RRCA                        ; 
1CB6: 0F              RRCA                        ; 
1CB7: 7B              LD      A,E                 ; 
1CB8: 17              RLA                         ; 
1CB9: 0F              RRCA                        ; 
1CBA: 32 CA 92        LD      ($92CA),A           ; 
1CBD: 08              EX      AF,AF'              ; 
1CBE: FD 22 CB 92     LD      ($92CB),IY          ; 
1CC2: 04              INC     B                   ; 
1CC3: 7B              LD      A,E                 ; 
1CC4: E6 07           AND     $07                 ; 
1CC6: 21 30 98        LD      HL,$9830            ; 
1CC9: D7              RST     0X10                ; 
1CCA: DD 7D           LD      A,IXL               ; 
1CCC: EB              EX      DE,HL               ; 
1CCD: 21 03 1D        LD      HL,$1D03            ; 
1CD0: CF              RST     0X08                ; 
1CD1: 7E              LD      A,(HL)              ; 
1CD2: 12              LD      (DE),A              ; 
1CD3: 23              INC     HL                  ; 
1CD4: 1C              INC     E                   ; 
1CD5: 7E              LD      A,(HL)              ; 
1CD6: 12              LD      (DE),A              ; 
1CD7: DD 7D           LD      A,IXL               ; 
1CD9: FE 02           CP      $02                 ; 
1CDB: 28 0C           JR      Z,$1CE9             ; {}
1CDD: 11 CD 92        LD      DE,$92CD            ; 
1CE0: 3D              DEC     A                   ; 
1CE1: 28 03           JR      Z,$1CE6             ; {}
1CE3: CD 09 1D        CALL    $1D09               ; {}
1CE6: CD 09 1D        CALL    $1D09               ; {}
1CE9: 3A CA 92        LD      A,($92CA)           ; 
1CEC: E6 07           AND     $07                 ; 
1CEE: 6F              LD      L,A                 ; 
1CEF: 26 88           LD      H,$88               ; 
1CF1: 7E              LD      A,(HL)              ; 
1CF2: 3D              DEC     A                   ; 
1CF3: C0              RET     NZ                  ; 
1CF4: 4D              LD      C,L                 ; 
1CF5: 21 CA 92        LD      HL,$92CA            ; 
1CF8: 2C              INC     L                   ; 
1CF9: 2C              INC     L                   ; 
1CFA: 2C              INC     L                   ; 
1CFB: 7E              LD      A,(HL)              ; 
1CFC: 3C              INC     A                   ; 
1CFD: 20 F9           JR      NZ,$1CF8            ; {}
1CFF: 08              EX      AF,AF'              ; 
1D00: 79              LD      A,C                 ; 
1D01: 18 19           JR      $1D1C               ; {}
1D03: 0D              DEC     C                   ; 
1D04: BA              CP      D                   ; 
1D05: 05              DEC     B                   ; 
1D06: B7              OR      A                   ; 
1D07: 01 B5 CB        LD      BC,$CBB5            ; 
1D0A: 09              ADD     HL,BC               ; 
1D0B: 38 06           JR      C,$1D13             ; {}
1D0D: 05              DEC     B                   ; 
1D0E: CB 09           RRC     C                   ; 
1D10: 38 01           JR      C,$1D13             ; {}
1D12: 05              DEC     B                   ; 
1D13: 78              LD      A,B                 ; 
1D14: 05              DEC     B                   ; 
1D15: 21 32 1D        LD      HL,$1D32            ; 
1D18: D7              RST     0X10                ; 
1D19: 08              EX      AF,AF'              ; 
1D1A: 7E              LD      A,(HL)              ; 
1D1B: EB              EX      DE,HL               ; 
1D1C: 17              RLA                         ; 
1D1D: 0F              RRCA                        ; 
1D1E: 77              LD      (HL),A              ; 
1D1F: 08              EX      AF,AF'              ; 
1D20: 2C              INC     L                   ; 
1D21: FD 7D           LD      A,IYL               ; 
1D23: 77              LD      (HL),A              ; 
1D24: 2C              INC     L                   ; 
1D25: FD 7C           LD      A,IYH               ; 
1D27: 77              LD      (HL),A              ; 
1D28: 2C              INC     L                   ; 
1D29: EB              EX      DE,HL               ; 
1D2A: C9              RET                         ; 

1D2B: 11 44 04        LD      DE,$0444            ; 
1D2E: CD 83 10        CALL    $1083               ; {} Process next moving bee
1D31: C9              RET                         ; 

1D32: 4A              LD      C,D                 ; 
1D33: 52              LD      D,D                 ; 
1D34: 5A              LD      E,D                 ; 
1D35: 58              LD      E,B                 ; 
1D36: 50              LD      D,B                 ; 
1D37: 48              LD      C,B                 ; 

; PLAY COMMAND 0E (??)
1D38: 21 B4 99        LD      HL,$99B4            ; 
1D3B: 7E              LD      A,(HL)              ; 
1D3C: E6 7F           AND     $7F                 ; 
1D3E: D6 7E           SUB     $7E                 ; 
1D40: 28 36           JR      Z,$1D78             ; {}
1D42: 4E              LD      C,(HL)              ; 
1D43: 34              INC     (HL)                ; 
1D44: 3A 15 92        LD      A,($9215)           ; 
1D47: CB 01           RLC     C                   ; 
1D49: A9              XOR     C                   ; 
1D4A: 0F              RRCA                        ; 
1D4B: 3E 01           LD      A,$01               ; 
1D4D: 38 02           JR      C,$1D51             ; {}
1D4F: ED 44           NEG                         ; 
1D51: 4F              LD      C,A                 ; 
1D52: 21 14 98        LD      HL,$9814            ; 
1D55: 06 06           LD      B,$06               ; 
1D57: 7E              LD      A,(HL)              ; 
1D58: 81              ADD     A,C                 ; 
1D59: 77              LD      (HL),A              ; 
1D5A: 1F              RRA                         ; 
1D5B: A9              XOR     C                   ; 
1D5C: 2C              INC     L                   ; 
1D5D: 07              RLCA                        ; 
1D5E: 30 04           JR      NC,$1D64            ; {}
1D60: 7E              LD      A,(HL)              ; 
1D61: EE 01           XOR     $01                 ; 
1D63: 77              LD      (HL),A              ; 
1D64: 2C              INC     L                   ; 
1D65: 10 F0           DJNZ    $1D57               ; {}
1D67: 3A A0 92        LD      A,($92A0)           ; 
1D6A: E6 FC           AND     $FC                 ; 
1D6C: 3C              INC     A                   ; 
1D6D: F5              PUSH    AF                  ; 
1D6E: CD EE 23        CALL    $23EE               ; {}
1D71: F1              POP     AF                  ; 
1D72: C6 02           ADD     $02                 ; 
1D74: CD EE 23        CALL    $23EE               ; {}
1D77: C9              RET                         ; 
1D78: 32 0E 90        LD      ($900E),A           ; 
1D7B: C9              RET                         ; 

;======================================================================
; PLAY COMMAND 12
;
1D7C: 3A 15 92        LD      A,($9215)           ; 
1D7F: 47              LD      B,A                 ; 
1D80: 21 B9 99        LD      HL,$99B9            ; 
1D83: 7E              LD      A,(HL)              ; 
1D84: 2C              INC     L                   ; 
1D85: A7              AND     A                   ; 
1D86: 28 26           JR      Z,$1DAE             ; {}
1D88: 7E              LD      A,(HL)              ; 
1D89: A7              AND     A                   ; 
1D8A: 3E FD           LD      A,$FD               ; 
1D8C: 20 13           JR      NZ,$1DA1            ; {}
1D8E: 2C              INC     L                   ; 
1D8F: 7E              LD      A,(HL)              ; 
1D90: 2C              INC     L                   ; 
1D91: BE              CP      (HL)                ; 
1D92: 28 01           JR      Z,$1D95             ; {}
1D94: 34              INC     (HL)                ; 
1D95: 7E              LD      A,(HL)              ; 
1D96: 2C              INC     L                   ; 
1D97: 86              ADD     A,(HL)              ; 
1D98: 4F              LD      C,A                 ; 
1D99: E6 3F           AND     $3F                 ; 
1D9B: 77              LD      (HL),A              ; 
1D9C: 79              LD      A,C                 ; 
1D9D: 07              RLCA                        ; 
1D9E: 07              RLCA                        ; 
1D9F: E6 03           AND     $03                 ; 
1DA1: CB 40           BIT     0,B                 ; 
1DA3: 20 02           JR      NZ,$1DA7            ; {}
1DA5: ED 44           NEG                         ; 
1DA7: 3D              DEC     A                   ; 
1DA8: E6 07           AND     $07                 ; 
1DAA: 32 BE 99        LD      ($99BE),A           ; 
1DAD: C9              RET                         ; 
1DAE: AF              XOR     A                   ; 
1DAF: 77              LD      (HL),A              ; 
1DB0: 2C              INC     L                   ; 
1DB1: 2C              INC     L                   ; 
1DB2: 77              LD      (HL),A              ; 
1DB3: 2C              INC     L                   ; 
1DB4: 77              LD      (HL),A              ; 
1DB5: 3E 07           LD      A,$07               ; 
1DB7: 18 F1           JR      $1DAA               ; {}

; PLAY COMMAND 0B
1DB9: 21 00 92        LD      HL,$9200            ; 
1DBC: 06 30           LD      B,$30               ; 
1DBE: CB 7E           BIT     7,(HL)              ; 
1DC0: 20 05           JR      NZ,$1DC7            ; {}
1DC2: 2C              INC     L                   ; 
1DC3: 2C              INC     L                   ; 
1DC4: 10 F8           DJNZ    $1DBE               ; {}
1DC6: C9              RET                         ; 
1DC7: CB BE           RES     7,(HL)              ; 
1DC9: 26 88           LD      H,$88               ; 
1DCB: 36 04           LD      (HL),$04            ; 
1DCD: 2C              INC     L                   ; 
1DCE: 36 40           LD      (HL),$40            ; 
1DD0: 26 8B           LD      H,$8B               ; 
1DD2: 36 0A           LD      (HL),$0A            ; 
1DD4: 26 92           LD      H,$92               ; 
1DD6: 18 EB           JR      $1DC3               ; {}

;======================================================================
; PLAY COMMAND 17
;
1DD8: 3A A2 92        LD      A,($92A2)           ; 
1DDB: E6 01           AND     $01                 ; 
1DDD: C0              RET     NZ                  ; 
1DDE: 21 AC 92        LD      HL,$92AC            ; 
1DE1: 06 04           LD      B,$04               ; 
1DE3: 7E              LD      A,(HL)              ; 
1DE4: A7              AND     A                   ; 
1DE5: 28 01           JR      Z,$1DE8             ; {}
1DE7: 35              DEC     (HL)                ; 
1DE8: 2C              INC     L                   ; 
1DE9: 10 F8           DJNZ    $1DE3               ; {}
1DEB: C9              RET                         ; 

; PLAY COMMAND 09 (??)
1DEC: 3A A0 92        LD      A,($92A0)           ; 
1DEF: E6 03           AND     $03                 ; 
1DF1: C0              RET     NZ                  ; 
1DF2: 21 0F 92        LD      HL,$920F            ; 
1DF5: 7E              LD      A,(HL)              ; 
1DF6: 5F              LD      E,A                 ; 
1DF7: 16 FF           LD      D,$FF               ; 
1DF9: CB 7F           BIT     7,A                 ; 
1DFB: 20 05           JR      NZ,$1E02            ; {}
1DFD: 14              INC     D                   ; 
1DFE: 14              INC     D                   ; 
1DFF: 34              INC     (HL)                ; 
1E00: 18 01           JR      $1E03               ; {}
1E02: 35              DEC     (HL)                ; 
1E03: FE 1F           CP      $1F                 ; 
1E05: 20 02           JR      NZ,$1E09            ; {}
1E07: CB FE           SET     7,(HL)              ; 
1E09: FE 81           CP      $81                 ; 
1E0B: 20 02           JR      NZ,$1E0F            ; {}
1E0D: CB BE           RES     7,(HL)              ; 
1E0F: 4E              LD      C,(HL)              ; 
1E10: E6 07           AND     $07                 ; 
1E12: 7A              LD      A,D                 ; 
1E13: 32 11 92        LD      ($9211),A           ; 
1E16: 7B              LD      A,E                 ; 
1E17: 20 10           JR      NZ,$1E29            ; {}
1E19: 21 6A 1E        LD      HL,$1E6A            ; 
1E1C: 79              LD      A,C                 ; 
1E1D: E6 18           AND     $18                 ; 
1E1F: CF              RST     0X08                ; 
1E20: 7B              LD      A,E                 ; 
1E21: 11 20 99        LD      DE,$9920            ; 
1E24: 01 10 00        LD      BC,$0010            ; 
1E27: ED B0           LDIR                        ; 
1E29: 21 15 92        LD      HL,$9215            ; 
1E2C: 07              RLCA                        ; 
1E2D: AE              XOR     (HL)                ; 
1E2E: 0F              RRCA                        ; 
1E2F: 21 20 99        LD      HL,$9920            ; 
1E32: 11 00 99        LD      DE,$9900            ; 
1E35: 30 05           JR      NC,$1E3C            ; {}
1E37: 01 FF 01        LD      BC,$01FF            ; 
1E3A: 18 03           JR      $1E3F               ; {}
1E3C: 01 01 FF        LD      BC,$FF01            ; 
1E3F: DD 2E 05        LD      IXL,$05             ; 
1E42: CD 49 1E        CALL    $1E49               ; {}
1E45: 41              LD      B,C                 ; 
1E46: DD 2E 0B        LD      IXL,$0B             ; 
1E49: CB 0E           RRC     (HL)                ; 
1E4B: 30 15           JR      NC,$1E62            ; {}
1E4D: 1A              LD      A,(DE)              ; 
1E4E: 80              ADD     A,B                 ; 
1E4F: 12              LD      (DE),A              ; 
1E50: 16 98           LD      D,$98               ; 
1E52: 1A              LD      A,(DE)              ; 
1E53: 80              ADD     A,B                 ; 
1E54: 12              LD      (DE),A              ; 
1E55: 1F              RRA                         ; 
1E56: A8              XOR     B                   ; 
1E57: 07              RLCA                        ; 
1E58: 30 06           JR      NC,$1E60            ; {}
1E5A: 1C              INC     E                   ; 
1E5B: 1A              LD      A,(DE)              ; 
1E5C: EE 01           XOR     $01                 ; 
1E5E: 12              LD      (DE),A              ; 
1E5F: 1D              DEC     E                   ; 
1E60: 16 99           LD      D,$99               ; 
1E62: 1C              INC     E                   ; 
1E63: 1C              INC     E                   ; 
1E64: 2C              INC     L                   ; 
1E65: DD 2D           DEC     IXL                 ; 
1E67: 20 E0           JR      NZ,$1E49            ; {}
1E69: C9              RET                         ; 
1E6A: FF              RST     0X38                ; 
1E6B: 77              LD      (HL),A              ; 
1E6C: 55              LD      D,L                 ; 
1E6D: 14              INC     D                   ; 
1E6E: 10 10           DJNZ    $1E80               ; {}
1E70: 14              INC     D                   ; 
1E71: 55              LD      D,L                 ; 
1E72: 77              LD      (HL),A              ; 
1E73: FF              RST     0X38                ; 
1E74: 00              NOP                         ; 
1E75: 10 14           DJNZ    $1E8B               ; {}
1E77: 55              LD      D,L                 ; 
1E78: 77              LD      (HL),A              ; 
1E79: FF              RST     0X38                ; 
1E7A: FF              RST     0X38                ; 
1E7B: 77              LD      (HL),A              ; 
1E7C: 55              LD      D,L                 ; 
1E7D: 51              LD      D,C                 ; 
1E7E: 10 10           DJNZ    $1E90               ; {}
1E80: 51              LD      D,C                 ; 
1E81: 55              LD      D,L                 ; 
1E82: 77              LD      (HL),A              ; 
1E83: FF              RST     0X38                ; 
1E84: 00              NOP                         ; 
1E85: 10 51           DJNZ    $1ED8               ; {}
1E87: 55              LD      D,L                 ; 
1E88: 77              LD      (HL),A              ; 
1E89: FF              RST     0X38                ; 
1E8A: FF              RST     0X38                ; 
1E8B: 77              LD      (HL),A              ; 
1E8C: 57              LD      D,A                 ; 
1E8D: 15              DEC     D                   ; 
1E8E: 10 10           DJNZ    $1EA0               ; {}
1E90: 15              DEC     D                   ; 
1E91: 57              LD      D,A                 ; 
1E92: 77              LD      (HL),A              ; 
1E93: FF              RST     0X38                ; 
1E94: 00              NOP                         ; 
1E95: 10 15           DJNZ    $1EAC               ; {}
1E97: 57              LD      D,A                 ; 
1E98: 77              LD      (HL),A              ; 
1E99: FF              RST     0X38                ; 
1E9A: FF              RST     0X38                ; 
1E9B: F7              RST     0X30                ; 
1E9C: D5              PUSH    DE                  ; 
1E9D: 91              SUB     C                   ; 
1E9E: 10 10           DJNZ    $1EB0               ; {}
1EA0: 91              SUB     C                   ; 
1EA1: D5              PUSH    DE                  ; 
1EA2: F7              RST     0X30                ; 
1EA3: FF              RST     0X38                ; 
1EA4: 00              NOP                         ; 
1EA5: 10 91           DJNZ    $1E38               ; {}
1EA7: D5              PUSH    DE                  ; 
1EA8: F7              RST     0X30                ; 
1EA9: FF              RST     0X38                ; 

;======================================================================
; PLAY COMMAND 0D (Move Bee Fire)
1EAA: 3A A0 92        LD      A,($92A0)           ; 
1EAD: E6 01           AND     $01                 ; 
1EAF: C6 02           ADD     $02                 ; 
1EB1: 47              LD      B,A                 ; 
1EB2: 3A 15 92        LD      A,($9215)           ; 0 = shots move up
1EB5: A7              AND     A                   ; 
1EB6: 78              LD      A,B                 ; 
1EB7: 28 02           JR      Z,$1EBB             ; {} Jump if 9215 is zero
1EB9: ED 44           NEG                         ; Shots moving down!
1EBB: DD 67           LD      IXH,A               ; 
1EBD: 2E 68           LD      L,$68               ; Offset to fire space
1EBF: 11 B0 92        LD      DE,$92B0            ; X and Y velocity
1EC2: DD 2E 08        LD      IXL,$08             ; Eight shots to do
;
; Loop Here
1EC5: 26 8B           LD      H,$8B               ; Sprite color code
1EC7: 7E              LD      A,(HL)              ; Get sprite color
1EC8: FE 30           CP      $30                 ; Sprite color of a bee shot?
1ECA: 20 39           JR      NZ,$1F05            ; {} Not 30 - skip moving it
;
1ECC: 26 93           LD      H,$93               ; Sprite position
1ECE: 7E              LD      A,(HL)              ; Get position
1ECF: A7              AND     A                   ; Set flags
1ED0: 28 33           JR      Z,$1F05             ; {} If it is 0, skip moving it
;
1ED2: EB              EX      DE,HL               ; 
1ED3: 46              LD      B,(HL)              ; Get X velocity
1ED4: 78              LD      A,B                 ; 
1ED5: E6 7E           AND     $7E                 ; 
1ED7: 2C              INC     L                   ; 
1ED8: 86              ADD     A,(HL)              ; 
1ED9: 4F              LD      C,A                 ; 
1EDA: E6 1F           AND     $1F                 ; 
1EDC: 77              LD      (HL),A              ; 
1EDD: 2C              INC     L                   ; 
1EDE: 79              LD      A,C                 ; 
1EDF: 07              RLCA                        ; 
1EE0: 07              RLCA                        ; 
1EE1: 07              RLCA                        ; 
1EE2: E6 07           AND     $07                 ; 
1EE4: CB 78           BIT     7,B                 ; Left or right?
1EE6: 28 02           JR      Z,$1EEA             ; {} Right -- keep it
1EE8: ED 44           NEG                         ; Shots move to left
1EEA: EB              EX      DE,HL               ; 
1EEB: 86              ADD     A,(HL)              ; Offset X coordinate
1EEC: 77              LD      (HL),A              ; New X coordinate
1EED: 2C              INC     L                   ; Y coordinate
1EEE: 7E              LD      A,(HL)              ; Get Y coordinate
1EEF: DD 84           ADD     A,IXH               ; Offset Y coordinate
1EF1: 77              LD      (HL),A              ; New Y coordinate
1EF2: 1F              RRA                         ; 
1EF3: DD AC           XOR     IXH                 ; 
1EF5: 07              RLCA                        ; 
1EF6: 30 07           JR      NC,$1EFF            ; {}
;
; Here if shot is close to bottom of screen
1EF8: 26 9B           LD      H,$9B               ; Sprite control
1EFA: CB 0E           RRC     (HL)                ; Rotate Right Circular
1EFC: 3F              CCF                         ; 
1EFD: CB 16           RL      (HL)                ; Rotate Left (through carry)
;
1EFF: 2C              INC     L                   ; Point ...
1F00: DD 2D           DEC     IXL                 ; ... to next shot (before)
1F02: 20 C1           JR      NZ,$1EC5            ; {} Process next shot
1F04: C9              RET                         ; Done
;
1F05: 2C              INC     L                   ; 
1F06: 1C              INC     E                   ; 
1F07: 1C              INC     E                   ; 
1F08: 18 F5           JR      $1EFF               ; {} Next shot
;======================================================================

;======================================================================
; PLAY COMMAND 15 Initiate Player Fire
;
1F0A: 3A 15 92        LD      A,($9215)           ; 
1F0D: C6 B6           ADD     $B6                 ; 
1F0F: 6F              LD      L,A                 ; 
1F10: 26 99           LD      H,$99               ; 
1F12: CB 66           BIT     4,(HL)              ; 
1F14: C0              RET     NZ                  ; 
1F15: 21 64 93        LD      HL,$9364            ; 
1F18: 11 A4 92        LD      DE,$92A4            ; 
1F1B: AF              XOR     A                   ; 
1F1C: BE              CP      (HL)                ; 
1F1D: 28 05           JR      Z,$1F24             ; {}
1F1F: 2E 66           LD      L,$66               ; 
1F21: 1C              INC     E                   ; 
1F22: BE              CP      (HL)                ; 
1F23: C0              RET     NZ                  ; 
1F24: D5              PUSH    DE                  ; 
1F25: EB              EX      DE,HL               ; 
1F26: 21 63 9B        LD      HL,$9B63            ; 
1F29: 54              LD      D,H                 ; 
1F2A: 1C              INC     E                   ; 
1F2B: CB 56           BIT     2,(HL)              ; 
1F2D: 28 02           JR      Z,$1F31             ; {}
1F2F: D1              POP     DE                  ; 
1F30: C9              RET                         ; 
1F31: ED A8           LDD                         ; 
1F33: 26 93           LD      H,$93               ; 
1F35: 54              LD      D,H                 ; 
1F36: ED A0           LDI                         ; 
1F38: ED A8           LDD                         ; 
1F3A: 26 9B           LD      H,$9B               ; 
1F3C: 54              LD      D,H                 ; 
1F3D: 46              LD      B,(HL)              ; 
1F3E: EB              EX      DE,HL               ; 
1F3F: 3A 27 98        LD      A,($9827)           ; 
1F42: E6 01           AND     $01                 ; 
1F44: 07              RLCA                        ; 
1F45: 07              RLCA                        ; 
1F46: 07              RLCA                        ; 
1F47: B0              OR      B                   ; 
1F48: 77              LD      (HL),A              ; 
1F49: 16 8B           LD      D,$8B               ; 
1F4B: 1A              LD      A,(DE)              ; 
1F4C: 62              LD      H,D                 ; 
1F4D: E6 07           AND     $07                 ; 
1F4F: 0E 30           LD      C,$30               ; 
1F51: FE 05           CP      $05                 ; 
1F53: 30 07           JR      NC,$1F5C            ; {}
1F55: 0C              INC     C                   ; 
1F56: FE 02           CP      $02                 ; 
1F58: 30 02           JR      NC,$1F5C            ; {}
1F5A: 0C              INC     C                   ; 
1F5B: 0C              INC     C                   ; 
1F5C: 71              LD      (HL),C              ; 
1F5D: FE 04           CP      $04                 ; 
1F5F: 38 03           JR      C,$1F64             ; {}
1F61: 2F              CPL                         ; 
1F62: C6 47           ADD     $47                 ; 
1F64: CB 27           SLA     A                   ; 
1F66: 4F              LD      C,A                 ; 
1F67: 78              LD      A,B                 ; 
1F68: 0F              RRCA                        ; 
1F69: 0F              RRCA                        ; 
1F6A: 0F              RRCA                        ; 
1F6B: E6 60           AND     $60                 ; 
1F6D: 47              LD      B,A                 ; 
1F6E: 3A 15 92        LD      A,($9215)           ; 
1F71: A7              AND     A                   ; 
1F72: 78              LD      A,B                 ; 
1F73: 20 02           JR      NZ,$1F77            ; {}
1F75: EE 60           XOR     $60                 ; 
;
; Add player shot to buffers
1F77: B1              OR      C                   ; 
1F78: D1              POP     DE                  ; 
1F79: 12              LD      (DE),A              ; 
1F7A: 26 88           LD      H,$88               ; Shot slots
1F7C: 36 06           LD      (HL),$06            ; Add players shot
1F7E: 3E 01           LD      A,$01               ; 
1F80: 32 AF 9A        LD      ($9AAF),A           ; 
1F83: 2A 46 98        LD      HL,($9846)          ; 
1F86: 23              INC     HL                  ; 
1F87: 22 46 98        LD      ($9846),HL          ; 
1F8A: C9              RET                         ; 
;======================================================================

;======================================================================
; PLAY COMMAND 14 (Move player left or right)
;
1F8B: 3A 27 98        LD      A,($9827)           ; 
1F8E: 5F              LD      E,A                 ; 
1F8F: 3A 15 92        LD      A,($9215)           ; 
1F92: C6 B6           ADD     $B6                 ; 
1F94: 6F              LD      L,A                 ; 
1F95: 26 99           LD      H,$99               ; 
1F97: 7E              LD      A,(HL)              ; 
1F98: E6 0A           AND     $0A                 ; 
1F9A: FE 0A           CP      $0A                 ; 
1F9C: 28 37           JR      Z,$1FD5             ; {}
1F9E: 21 15 92        LD      HL,$9215            ; 
1FA1: CB 46           BIT     0,(HL)              ; 
1FA3: 28 02           JR      Z,$1FA7             ; {}
1FA5: EE 0A           XOR     $0A                 ; 
1FA7: 21 A3 92        LD      HL,$92A3            ; 
1FAA: 47              LD      B,A                 ; 
1FAB: 0E 01           LD      C,$01               ; 
1FAD: 7E              LD      A,(HL)              ; 
1FAE: EE 01           XOR     $01                 ; 
1FB0: 77              LD      (HL),A              ; 
1FB1: 20 01           JR      NZ,$1FB4            ; {}
1FB3: 0C              INC     C                   ; 
1FB4: 21 62 93        LD      HL,$9362            ; 
1FB7: 7E              LD      A,(HL)              ; 
1FB8: A7              AND     A                   ; 
1FB9: C8              RET     Z                   ; 
1FBA: CB 48           BIT     1,B                 ; 
1FBC: 20 0F           JR      NZ,$1FCD            ; {}
1FBE: 7E              LD      A,(HL)              ; 
1FBF: FE D1           CP      $D1                 ; 
1FC1: 38 03           JR      C,$1FC6             ; {}
1FC3: CB 43           BIT     0,E                 ; 
1FC5: C0              RET     NZ                  ; 
1FC6: FE E1           CP      $E1                 ; 
1FC8: D0              RET     NC                  ; 
1FC9: 81              ADD     A,C                 ; 
1FCA: 77              LD      (HL),A              ; 
1FCB: 18 0D           JR      $1FDA               ; {}
1FCD: 7E              LD      A,(HL)              ; 
1FCE: FE 12           CP      $12                 ; 
1FD0: D8              RET     C                   ; 
1FD1: 91              SUB     C                   ; 
1FD2: 77              LD      (HL),A              ; 
1FD3: 18 05           JR      $1FDA               ; {}
1FD5: AF              XOR     A                   ; 
1FD6: 32 A3 92        LD      ($92A3),A           ; 
1FD9: C9              RET                         ; 
1FDA: CB 43           BIT     0,E                 ; 
1FDC: C8              RET     Z                   ; 
1FDD: C6 0F           ADD     $0F                 ; 
1FDF: 32 60 93        LD      ($9360),A           ; 
1FE2: C9              RET                         ; 
;======================================================================

1FE3: FF FF FF FF FF FF FF FF FF FF FF FF FF 
1FF0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 80

;======================================================================
; PLAY COMMAND 1D Coordinate Free-fighter sequence
;
2000: 3A 28 98        LD      A,($9828)           ; 
2003: 6F              LD      L,A                 ; 
2004: 26 88           LD      H,$88               ; 
2006: 7E              LD      A,(HL)              ; 
2007: A7              AND     A                   ; 
2008: C2 BF 20        JP      NZ,$20BF            ; {} Turn off "freed music" and return
200B: 3A 8B 92        LD      A,($928B)           ; 
200E: A7              AND     A                   ; 
200F: CA C7 20        JP      Z,$20C7             ; {}
2012: 3D              DEC     A                   ; 
2013: CA D1 20        JP      Z,$20D1             ; {}
2016: 26 93           LD      H,$93               ; 
2018: 7E              LD      A,(HL)              ; 
2019: FE 80           CP      $80                 ; 
201B: 28 09           JR      Z,$2026             ; {}
201D: F2 23 20        JP      P,$2023             ; {}
2020: 34              INC     (HL)                ; 
2021: 18 3B           JR      $205E               ; {}
2023: 35              DEC     (HL)                ; 
2024: 18 38           JR      $205E               ; {}
2026: 2C              INC     L                   ; 
2027: 3A 15 92        LD      A,($9215)           ; 
202A: A7              AND     A                   ; 
202B: 20 1F           JR      NZ,$204C            ; {}
202D: 7E              LD      A,(HL)              ; 
202E: FE 29           CP      $29                 ; 
2030: 20 0F           JR      NZ,$2041            ; {}
2032: 26 9B           LD      H,$9B               ; 
2034: 7E              LD      A,(HL)              ; 
2035: 26 93           LD      H,$93               ; 
2037: 3D              DEC     A                   ; 
2038: 20 07           JR      NZ,$2041            ; {}
203A: 3E 03           LD      A,$03               ; 
203C: 32 8B 92        LD      ($928B),A           ; 
203F: 18 1D           JR      $205E               ; {}
2041: 34              INC     (HL)                ; 
2042: 20 1A           JR      NZ,$205E            ; {}
2044: 26 9B           LD      H,$9B               ; 
2046: 7E              LD      A,(HL)              ; 
2047: EE 01           XOR     $01                 ; 
2049: 77              LD      (HL),A              ; 
204A: 18 12           JR      $205E               ; {}
204C: 7E              LD      A,(HL)              ; 
204D: FE 37           CP      $37                 ; 
204F: 20 08           JR      NZ,$2059            ; {}
2051: 26 9B           LD      H,$9B               ; 
2053: 7E              LD      A,(HL)              ; 
2054: 26 93           LD      H,$93               ; 
2056: A7              AND     A                   ; 
2057: 28 E1           JR      Z,$203A             ; {}
2059: 35              DEC     (HL)                ; 
205A: 7E              LD      A,(HL)              ; 
205B: 3C              INC     A                   ; 
205C: 28 E6           JR      Z,$2044             ; {}
205E: 21 62 8B        LD      HL,$8B62            ; 
2061: 7E              LD      A,(HL)              ; 
2062: D6 06           SUB     $06                 ; 
2064: 4F              LD      C,A                 ; 
2065: 26 93           LD      H,$93               ; 
2067: 20 0C           JR      NZ,$2075            ; {}
2069: 7E              LD      A,(HL)              ; 
206A: FE 71           CP      $71                 ; 
206C: 28 07           JR      Z,$2075             ; {}
206E: F2 73 20        JP      P,$2073             ; {}
2071: 34              INC     (HL)                ; 
2072: C9              RET                         ; 
2073: 35              DEC     (HL)                ; 
2074: C9              RET                         ; 
2075: 3A 8B 92        LD      A,($928B)           ; 
2078: FE 03           CP      $03                 ; 
207A: C0              RET     NZ                  ; 
207B: 3A 28 98        LD      A,($9828)           ; 
207E: 6F              LD      L,A                 ; 
207F: 36 00           LD      (HL),$00            ; 
2081: 2C              INC     L                   ; 
2082: 0D              DEC     C                   ; 
2083: 0C              INC     C                   ; 
2084: 28 09           JR      Z,$208F             ; {}
2086: 11 63 93        LD      DE,$9363            ; 
2089: AF              XOR     A                   ; 
208A: 32 2B 98        LD      ($982B),A           ; 
208D: 18 08           JR      $2097               ; {}
208F: 3E 01           LD      A,$01               ; 
2091: 32 27 98        LD      ($9827),A           ; 
2094: 11 61 93        LD      DE,$9361            ; 
2097: 7E              LD      A,(HL)              ; 
2098: 12              LD      (DE),A              ; 
2099: 26 9B           LD      H,$9B               ; 
209B: 54              LD      D,H                 ; 
209C: 7E              LD      A,(HL)              ; 
209D: 12              LD      (DE),A              ; 
209E: 2D              DEC     L                   ; 
209F: 26 88           LD      H,$88               ; 
20A1: 36 80           LD      (HL),$80            ; 
20A3: 26 8B           LD      H,$8B               ; 
20A5: 6B              LD      L,E                 ; 
20A6: 2D              DEC     L                   ; 
20A7: 36 06           LD      (HL),$06            ; 
20A9: 2C              INC     L                   ; 
20AA: 36 09           LD      (HL),$09            ; This is in a section that hits
20AC: 2D              DEC     L                   ; ... as soon as second fighter drops
20AD: 26 93           LD      H,$93               ; ... with first for dual.
20AF: 36 80           LD      (HL),$80            ; 
20B1: 3E 01           LD      A,$01               ; 
20B3: 32 14 90        LD      ($9014),A           ; 
20B6: 32 15 90        LD      ($9015),A           ; 
20B9: 32 25 90        LD      ($9025),A           ; 
20BC: 32 B9 99        LD      ($99B9),A           ; 
;
20BF: AF              XOR     A                   ; Flag freed music ...
20C0: 32 1D 90        LD      ($901D),A           ; ... turned ...
20C3: 32 B1 9A        LD      ($9AB1),A           ; ... off
20C6: C9              RET                         ; out
;
20C7: 3C              INC     A                   ; Initiate ...
20C8: 32 8B 92        LD      ($928B),A           ; ... moving freed ship ...
20CB: 3E 02           LD      A,$02               ; ... down to bottom ...
20CD: 32 AD 92        LD      ($92AD),A           ; ... with current
20D0: C9              RET                         ; out
;
20D1: 26 9B           LD      H,$9B               ; 
20D3: 3A AD 92        LD      A,($92AD)           ; 
20D6: 5F              LD      E,A                 ; 
20D7: 3A 87 92        LD      A,($9287)           ; 
20DA: B3              OR      E                   ; 
20DB: 32 8D 92        LD      ($928D),A           ; 
20DE: CD 96 21        CALL    $2196               ; {}
20E1: 05              DEC     B                   ; 
20E2: C0              RET     NZ                  ; 
20E3: 32 14 90        LD      ($9014),A           ; 
20E6: 32 15 90        LD      ($9015),A           ; 
20E9: 32 25 90        LD      ($9025),A           ; 
20EC: 3E 02           LD      A,$02               ; 
20EE: 32 8B 92        LD      ($928B),A           ; 
20F1: C9              RET                         ; 

;======================================================================
; PLAY COMMAND 1C
;
20F2: 21 62 8B        LD      HL,$8B62            ; 
20F5: 7E              LD      A,(HL)              ; 
20F6: FE 40           CP      $40                 ; 
20F8: 38 08           JR      C,$2102             ; {}
20FA: AF              XOR     A                   ; 
20FB: 32 1C 90        LD      ($901C),A           ; 
20FE: 32 BA 99        LD      ($99BA),A           ; 
2101: C9              RET                         ; 
2102: 26 9B           LD      H,$9B               ; 
2104: CD 96 21        CALL    $2196               ; {}
2107: CB 40           BIT     0,B                 ; 
2109: 20 54           JR      NZ,$215F            ; {}
210B: 3A 8B 92        LD      A,($928B)           ; 
210E: CB 7F           BIT     7,A                 ; 
2110: 20 59           JR      NZ,$216B            ; {}
2112: 3A 8D 92        LD      A,($928D)           ; 
2115: A7              AND     A                   ; 
2116: C8              RET     Z                   ; 
2117: 26 93           LD      H,$93               ; 
2119: 3A 28 98        LD      A,($9828)           ; 
211C: 5F              LD      E,A                 ; 
211D: 54              LD      D,H                 ; 
211E: 1A              LD      A,(DE)              ; 
211F: BE              CP      (HL)                ; 
2120: 28 07           JR      Z,$2129             ; {}
2122: F2 28 21        JP      P,$2128             ; {}
2125: 35              DEC     (HL)                ; 
2126: 18 01           JR      $2129               ; {}
2128: 34              INC     (HL)                ; 
2129: 2C              INC     L                   ; 
212A: 3A 15 92        LD      A,($9215)           ; 
212D: A7              AND     A                   ; 
212E: 28 0B           JR      Z,$213B             ; {}
2130: 34              INC     (HL)                ; 
2131: 7E              LD      A,(HL)              ; 
2132: FE 7A           CP      $7A                 ; 
2134: 28 24           JR      Z,$215A             ; {}
2136: FE 80           CP      $80                 ; 
2138: 28 16           JR      Z,$2150             ; {}
213A: C9              RET                         ; 
213B: 35              DEC     (HL)                ; 
213C: 7E              LD      A,(HL)              ; 
213D: 3C              INC     A                   ; 
213E: 20 08           JR      NZ,$2148            ; {}
2140: 26 9B           LD      H,$9B               ; 
2142: 7E              LD      A,(HL)              ; 
2143: EE 01           XOR     $01                 ; 
2145: 77              LD      (HL),A              ; 
2146: 26 93           LD      H,$93               ; 
2148: 7E              LD      A,(HL)              ; 
2149: FE E6           CP      $E6                 ; 
214B: 28 0D           JR      Z,$215A             ; {}
214D: FE E0           CP      $E0                 ; 
214F: C0              RET     NZ                  ; 
2150: AF              XOR     A                   ; 
2151: 32 8D 92        LD      ($928D),A           ; 
2154: 3E 07           LD      A,$07               ; 
2156: 32 63 8B        LD      ($8B63),A           ; 
2159: C9              RET                         ; 
215A: AF              XOR     A                   ; 
215B: 32 15 90        LD      ($9015),A           ; 
215E: C9              RET                         ; 
215F: 3A 15 90        LD      A,($9015)           ; 
2162: A7              AND     A                   ; 
2163: 20 06           JR      NZ,$216B            ; {}
2165: 3C              INC     A                   ; 
2166: 32 0D 92        LD      ($920D),A           ; 
2169: 18 22           JR      $218D               ; {}
216B: 26 93           LD      H,$93               ; 
216D: 2C              INC     L                   ; 
216E: 3A 15 92        LD      A,($9215)           ; 
2171: A7              AND     A                   ; 
2172: 28 07           JR      Z,$217B             ; {}
2174: 7E              LD      A,(HL)              ; 
2175: FE 37           CP      $37                 ; 
2177: 28 12           JR      Z,$218B             ; {}
2179: 35              DEC     (HL)                ; 
217A: C9              RET                         ; 
217B: 7E              LD      A,(HL)              ; 
217C: FE 29           CP      $29                 ; 
217E: 28 0B           JR      Z,$218B             ; {}
2180: 34              INC     (HL)                ; 
2181: C0              RET     NZ                  ; 
2182: 26 9B           LD      H,$9B               ; 
2184: 7E              LD      A,(HL)              ; 
2185: EE 01           XOR     $01                 ; 
2187: 77              LD      (HL),A              ; 
2188: 26 93           LD      H,$93               ; 
218A: C9              RET                         ; 
218B: 05              DEC     B                   ; 
218C: C0              RET     NZ                  ; 
218D: AF              XOR     A                   ; 
218E: 32 1C 90        LD      ($901C),A           ; 
2191: 3C              INC     A                   ; 
2192: 32 25 90        LD      ($9025),A           ; 
2195: C9              RET                         ; 
2196: 7E              LD      A,(HL)              ; 
2197: 4F              LD      C,A                 ; 
2198: CB 3F           SRL     A                   ; 
219A: A9              XOR     C                   ; 
219B: 4F              LD      C,A                 ; 
219C: 26 8B           LD      H,$8B               ; 
219E: 06 00           LD      B,$00               ; 
21A0: 7E              LD      A,(HL)              ; 
21A1: E6 07           AND     $07                 ; 
21A3: FE 06           CP      $06                 ; 
21A5: 20 0E           JR      NZ,$21B5            ; {}
21A7: 0D              DEC     C                   ; 
21A8: 0C              INC     C                   ; 
21A9: 20 0A           JR      NZ,$21B5            ; {}
21AB: 08              EX      AF,AF'              ; 
21AC: 3A 8D 92        LD      A,($928D)           ; 
21AF: A7              AND     A                   ; 
21B0: 20 02           JR      NZ,$21B4            ; {}
21B2: 04              INC     B                   ; 
21B3: C9              RET                         ; 
21B4: 08              EX      AF,AF'              ; 
21B5: CB 41           BIT     0,C                 ; 
21B7: 20 07           JR      NZ,$21C0            ; {}
21B9: FE 06           CP      $06                 ; 
21BB: 28 09           JR      Z,$21C6             ; {}
21BD: 34              INC     (HL)                ; 
21BE: 18 0E           JR      $21CE               ; {}
21C0: A7              AND     A                   ; 
21C1: 28 03           JR      Z,$21C6             ; {}
21C3: 35              DEC     (HL)                ; 
21C4: 18 08           JR      $21CE               ; {}
21C6: 0D              DEC     C                   ; 
21C7: F2 B5 21        JP      P,$21B5             ; {}
21CA: 0E 03           LD      C,$03               ; 
21CC: 18 E7           JR      $21B5               ; {}
21CE: 79              LD      A,C                 ; 
21CF: CB 4F           BIT     1,A                 ; 
21D1: 28 02           JR      Z,$21D5             ; {}
21D3: EE 01           XOR     $01                 ; 
21D5: 26 9B           LD      H,$9B               ; 
21D7: 77              LD      (HL),A              ; 
21D8: C9              RET                         ; 

;======================================================================
; PLAY COMMAND 19
;
21D9: 21 28 98        LD      HL,$9828            ; 
21DC: 5E              LD      E,(HL)              ; 
21DD: 16 88           LD      D,$88               ; 
21DF: 1A              LD      A,(DE)              ; 
21E0: FE 09           CP      $09                 ; 
21E2: 20 44           JR      NZ,$2228            ; {}
21E4: 2C              INC     L                   ; 
21E5: 7E              LD      A,(HL)              ; 
21E6: DD 6F           LD      IXL,A               ; 
21E8: DD 26 91        LD      IXH,$91             ; 
21EB: DD 7E 0A        LD      A,(IX+$0A)          ; 
21EE: A7              AND     A                   ; 
21EF: C0              RET     NZ                  ; 
21F0: 3E 0C           LD      A,$0C               ; 
21F2: DD CB 05 46     BIT     0,(IX+$05)          ; 
21F6: 28 02           JR      Z,$21FA             ; {}
21F8: ED 44           NEG                         ; 
21FA: DD 77 0C        LD      (IX+$0C),A          ; 
21FD: DD 7E 05        LD      A,(IX+$05)          ; 
2200: 0F              RRCA                        ; 
2201: DD 7E 04        LD      A,(IX+$04)          ; 
2204: 1F              RRA                         ; 
2205: D6 78           SUB     $78                 ; 
2207: FE 10           CP      $10                 ; 
2209: D0              RET     NC                  ; 
220A: 3A C6 99        LD      A,($99C6)           ; 
220D: 32 2A 98        LD      ($982A),A           ; 
2210: AF              XOR     A                   ; 
2211: DD 77 0C        LD      (IX+$0C),A          ; 
2214: 32 19 90        LD      ($9019),A           ; 
2217: 32 8B 92        LD      ($928B),A           ; 
221A: 32 0D 92        LD      ($920D),A           ; 
221D: 3C              INC     A                   ; 
221E: 32 18 90        LD      ($9018),A           ; 
2221: 32 8C 92        LD      ($928C),A           ; 
2224: 32 8D 92        LD      ($928D),A           ; 
2227: C9              RET                         ; 
2228: AF              XOR     A                   ; 
2229: 32 19 90        LD      ($9019),A           ; 
222C: 32 2B 98        LD      ($982B),A           ; 
222F: C9              RET                         ; 

;======================================================================
; PLAY COMMAND 18
;
2230: 3A A0 92        LD      A,($92A0)           ; 
2233: 4F              LD      C,A                 ; 
2234: E6 03           AND     $03                 ; 
2236: 20 2D           JR      NZ,$2265            ; {}
2238: 3A 8A 92        LD      A,($928A)           ; 
223B: ED 44           NEG                         ; 
223D: D6 18           SUB     $18                 ; 
223F: 26 21           LD      H,$21               ; 
2241: 07              RLCA                        ; 
2242: CB 14           RL      H                   ; 
2244: 07              RLCA                        ; 
2245: CB 14           RL      H                   ; 
2247: E6 E0           AND     $E0                 ; 
2249: C6 15           ADD     $15                 ; 
224B: 6F              LD      L,A                 ; 
224C: 79              LD      A,C                 ; 
224D: 0F              RRCA                        ; 
224E: 0F              RRCA                        ; 
224F: E6 03           AND     $03                 ; 
2251: 20 01           JR      NZ,$2254            ; {}
2253: 3C              INC     A                   ; 
2254: C6 17           ADD     $17                 ; 
2256: 11 16 00        LD      DE,$0016            ; 
2259: 0E 06           LD      C,$06               ; 
225B: 06 0A           LD      B,$0A               ; 
225D: 77              LD      (HL),A              ; 
225E: 2C              INC     L                   ; 
225F: 10 FC           DJNZ    $225D               ; {}
2261: 19              ADD     HL,DE               ; 
2262: 0D              DEC     C                   ; 
2263: 20 F6           JR      NZ,$225B            ; {}
2265: 21 8B 92        LD      HL,$928B            ; 
2268: CB 7E           BIT     7,(HL)              ; 
226A: 20 0C           JR      NZ,$2278            ; {}
226C: 3A 28 98        LD      A,($9828)           ; 
226F: 5F              LD      E,A                 ; 
2270: 16 88           LD      D,$88               ; 
2272: 1A              LD      A,(DE)              ; 
2273: FE 09           CP      $09                 ; 
2275: C2 35 23        JP      NZ,$2335            ; {}
2278: 21 8C 92        LD      HL,$928C            ; 
227B: 35              DEC     (HL)                ; 
227C: C2 4B 23        JP      NZ,$234B            ; {}
227F: 3A 2A 98        LD      A,($982A)           ; 
2282: 77              LD      (HL),A              ; 
2283: 21 8B 92        LD      HL,$928B            ; 
2286: CB 7E           BIT     7,(HL)              ; 
2288: 20 2F           JR      NZ,$22B9            ; {}
228A: 32 A5 9A        LD      ($9AA5),A           ; 
228D: 3A 29 98        LD      A,($9829)           ; 
2290: C6 0D           ADD     $0D                 ; 
2292: 5F              LD      E,A                 ; 
2293: 16 91           LD      D,$91               ; 
2295: 3E FF           LD      A,$FF               ; 
2297: 12              LD      (DE),A              ; 
2298: 34              INC     (HL)                ; 
2299: 7E              LD      A,(HL)              ; 
229A: E6 0F           AND     $0F                 ; 
229C: FE 0B           CP      $0B                 ; 
229E: 28 40           JR      Z,$22E0             ; {}
22A0: CB 76           BIT     6,(HL)              ; 
22A2: 20 2B           JR      NZ,$22CF            ; {}
22A4: F5              PUSH    AF                  ; 
22A5: 4F              LD      C,A                 ; 
22A6: 07              RLCA                        ; 
22A7: 81              ADD     A,C                 ; 
22A8: 21 A9 23        LD      HL,$23A9            ; 
22AB: CF              RST     0X08                ; 
22AC: F1              POP     AF                  ; 
22AD: CD 98 23        CALL    $2398               ; {}
22B0: 06 06           LD      B,$06               ; 
22B2: 7E              LD      A,(HL)              ; 
22B3: 12              LD      (DE),A              ; 
22B4: 23              INC     HL                  ; 
22B5: E7              RST     0X20                ; 
22B6: 10 FA           DJNZ    $22B2               ; {}
22B8: C9              RET                         ; 

22B9: 34              INC     (HL)                ; 
22BA: 7E              LD      A,(HL)              ; 
22BB: E6 0F           AND     $0F                 ; 
22BD: FE 0B           CP      $0B                 ; 
22BF: 20 12           JR      NZ,$22D3            ; {}
22C1: AF              XOR     A                   ; 
22C2: 32 18 90        LD      ($9018),A           ; 
22C5: 32 A5 9A        LD      ($9AA5),A           ; 
22C8: 32 A6 9A        LD      ($9AA6),A           ; 
22CB: 32 2B 98        LD      ($982B),A           ; 
22CE: C9              RET                         ; 

22CF: ED 44           NEG                         ; 
22D1: C6 0B           ADD     $0B                 ; 
22D3: CD 98 23        CALL    $2398               ; {}
22D6: 06 06           LD      B,$06               ; 
22D8: 0E 24           LD      C,$24               ; 
22DA: 79              LD      A,C                 ; 
22DB: 12              LD      (DE),A              ; 
22DC: E7              RST     0X20                ; 
22DD: 10 FB           DJNZ    $22DA               ; {}
22DF: C9              RET                         ; 

22E0: CB 76           BIT     6,(HL)              ; 
22E2: 28 46           JR      Z,$232A             ; {}
22E4: 3A 0D 92        LD      A,($920D)           ; 
22E7: A7              AND     A                   ; 
22E8: 28 07           JR      Z,$22F1             ; {}
22EA: CB 6E           BIT     5,(HL)              ; 
22EC: 20 03           JR      NZ,$22F1            ; {}
22EE: 36 68           LD      (HL),$68            ; 
22F0: C9              RET                         ; 

22F1: AF              XOR     A                   ; 
22F2: 32 18 90        LD      ($9018),A           ; 
22F5: 32 A5 9A        LD      ($9AA5),A           ; 
22F8: 32 A6 9A        LD      ($9AA6),A           ; 
22FB: 3A 0D 92        LD      A,($920D)           ; 
22FE: A7              AND     A                   ; 
22FF: 3A 29 98        LD      A,($9829)           ; 
2302: 20 0F           JR      NZ,$2313            ; {}
2304: C6 0D           ADD     $0D                 ; 
2306: 5F              LD      E,A                 ; 
2307: 16 91           LD      D,$91               ; 
2309: AF              XOR     A                   ; 
230A: 32 2B 98        LD      ($982B),A           ; 
230D: 3C              INC     A                   ; 
230E: 32 28 98        LD      ($9828),A           ; 
2311: 12              LD      (DE),A              ; 
2312: C9              RET                         ; 
2313: C6 08           ADD     $08                 ; 
2315: 6F              LD      L,A                 ; 
2316: 26 91           LD      H,$91               ; 
2318: 11 6B 04        LD      DE,$046B            ; 
231B: 73              LD      (HL),E              ; 
231C: 2C              INC     L                   ; 
231D: 72              LD      (HL),D              ; 
231E: AF              XOR     A                   ; 
231F: 32 BA 99        LD      ($99BA),A           ; 
2322: 3C              INC     A                   ; 
2323: 32 11 90        LD      ($9011),A           ; 
2326: 32 8E 92        LD      ($928E),A           ; 
2329: C9              RET                         ; 

232A: 3E 40           LD      A,$40               ; 
232C: 32 8C 92        LD      ($928C),A           ; 
232F: 3E 40           LD      A,$40               ; 
2331: 32 8B 92        LD      ($928B),A           ; 
2334: C9              RET                         ; 

2335: 3E 03           LD      A,$03               ; 
2337: 32 2A 98        LD      ($982A),A           ; 
233A: 36 80           LD      (HL),$80            ; 
233C: AF              XOR     A                   ; 
233D: 32 8D 92        LD      ($928D),A           ; 
2340: 32 BA 99        LD      ($99BA),A           ; 
2343: 3C              INC     A                   ; 
2344: 32 8C 92        LD      ($928C),A           ; 
2347: 32 14 90        LD      ($9014),A           ; 
234A: C9              RET                         ; 

234B: 3A 8B 92        LD      A,($928B)           ; 
234E: FE 40           CP      $40                 ; 
2350: C0              RET     NZ                  ; 
2351: 3A 15 92        LD      A,($9215)           ; 
2354: 4F              LD      C,A                 ; 
2355: 3A 62 93        LD      A,($9362)           ; 
2358: CB 41           BIT     0,C                 ; 
235A: 28 04           JR      Z,$2360             ; {}
235C: C6 0E           ADD     $0E                 ; 
235E: ED 44           NEG                         ; 
2360: 47              LD      B,A                 ; 
2361: 3A 8A 92        LD      A,($928A)           ; 
2364: 90              SUB     B                   ; 
2365: C6 1B           ADD     $1B                 ; 
2367: FE 36           CP      $36                 ; 
2369: D0              RET     NC                  ; 
236A: 3A 01 92        LD      A,($9201)           ; 
236D: 3D              DEC     A                   ; 
236E: 28 0B           JR      Z,$237B             ; {}
2370: 3A 14 90        LD      A,($9014)           ; 
2373: 4F              LD      C,A                 ; 
2374: 3A 13 92        LD      A,($9213)           ; 
2377: EE 01           XOR     $01                 ; 
2379: A1              AND     C                   ; 
237A: C8              RET     Z                   ; 
237B: AF              XOR     A                   ; 
237C: 32 14 90        LD      ($9014),A           ; 
237F: 32 A5 9A        LD      ($9AA5),A           ; 
2382: 32 25 90        LD      ($9025),A           ; 
2385: 32 13 92        LD      ($9213),A           ; 
2388: 3C              INC     A                   ; 
2389: 32 1C 90        LD      ($901C),A           ; 
238C: 32 A6 9A        LD      ($9AA6),A           ; 
238F: 32 BA 99        LD      ($99BA),A           ; 
2392: 3E 0A           LD      A,$0A               ; 
2394: 32 2A 98        LD      ($982A),A           ; 
2397: C9              RET                         ; 
2398: 4F              LD      C,A                 ; 
2399: 3A 8A 92        LD      A,($928A)           ; 
239C: ED 44           NEG                         ; 
239E: C6 10           ADD     $10                 ; 
23A0: 16 20           LD      D,$20               ; 
23A2: 07              RLCA                        ; 
23A3: CB 12           RL      D                   ; 
23A5: 07              RLCA                        ; 
23A6: CB 12           RL      D                   ; 
23A8: E6 E0           AND     $E0                 ; 
23AA: C6 14           ADD     $14                 ; 
23AC: 81              ADD     A,C                 ; 
23AD: 5F              LD      E,A                 ; 
23AE: C9              RET                         ; 
23AF: 24              INC     H                   ; 
23B0: 4E              LD      C,(HL)              ; 
23B1: 4F              LD      C,A                 ; 
23B2: 50              LD      D,B                 ; 
23B3: 51              LD      D,C                 ; 
23B4: 24              INC     H                   ; 
23B5: 24              INC     H                   ; 
23B6: 52              LD      D,D                 ; 
23B7: 53              LD      D,E                 ; 
23B8: 54              LD      D,H                 ; 
23B9: 55              LD      D,L                 ; 
23BA: 24              INC     H                   ; 
23BB: 24              INC     H                   ; 
23BC: 56              LD      D,(HL)              ; 
23BD: 57              LD      D,A                 ; 
23BE: 58              LD      E,B                 ; 
23BF: 59              LD      E,C                 ; 
23C0: 24              INC     H                   ; 
23C1: 24              INC     H                   ; 
23C2: 5A              LD      E,D                 ; 
23C3: 5B              LD      E,E                 ; 
23C4: 5C              LD      E,H                 ; 
23C5: 5D              LD      E,L                 ; 
23C6: 24              INC     H                   ; 
23C7: 24              INC     H                   ; 
23C8: 5E              LD      E,(HL)              ; 
23C9: 5F              LD      E,A                 ; 
23CA: 60              LD      H,B                 ; 
23CB: 61              LD      H,C                 ; 
23CC: 24              INC     H                   ; 
23CD: 62              LD      H,D                 ; 
23CE: 63              LD      H,E                 ; 
23CF: 64              LD      H,H                 ; 
23D0: 65              LD      H,L                 ; 
23D1: 66              LD      H,(HL)              ; 
23D2: 67              LD      H,A                 ; 
23D3: 68              LD      L,B                 ; 
23D4: 69              LD      L,C                 ; 
23D5: 6A              LD      L,D                 ; 
23D6: 6B              LD      L,E                 ; 
23D7: 6C              LD      L,H                 ; 
23D8: 6D              LD      L,L                 ; 
23D9: 6E              LD      L,(HL)              ; 
23DA: 6F              LD      L,A                 ; 
23DB: 70              LD      (HL),B              ; 
23DC: 71              LD      (HL),C              ; 
23DD: 72              LD      (HL),D              ; 
23DE: 73              LD      (HL),E              ; 
23DF: 74              LD      (HL),H              ; 
23E0: 75              LD      (HL),L              ; 
23E1: 76              HALT                        ; 
23E2: 77              LD      (HL),A              ; 
23E3: 78              LD      A,B                 ; 
23E4: 79              LD      A,C                 ; 
23E5: 7A              LD      A,D                 ; 
23E6: 7B              LD      A,E                 ; 
23E7: 7C              LD      A,H                 ; 
23E8: 7D              LD      A,L                 ; 
23E9: 7E              LD      A,(HL)              ; 
23EA: 7F              LD      A,A                 ; 

;======================================================================
; PLAY COMMAND 0C (Something to do with erasing dead things)
;
23EB: 3A A0 92        LD      A,($92A0)           ; 
23EE: CB 47           BIT     0,A                 ; 
23F0: CA A4 25        JP      Z,$25A4             ; {}
23F3: E6 02           AND     $02                 ; 
23F5: 5F              LD      E,A                 ; 
23F6: 3A A6 92        LD      A,($92A6)           ; 
23F9: DD 6F           LD      IXL,A               ; 
23FB: 06 20           LD      B,$20               ; Count is 64
;
23FD: 16 88           LD      D,$88               ; Slots
23FF: 1A              LD      A,(DE)              ; Get byte
2400: CB 27           SLA     A                   ; *2 bytes (and check upper bit)
2402: 38 20           JR      C,$2424             ; {} Skip command (an empty slot would skip)
2404: 21 0D 24        LD      HL,$240D            ; Jump table
2407: D7              RST     0X10                ; Add A to HL
2408: 7E              LD      A,(HL)              ; Get LS
2409: 23              INC     HL                  ; Next
240A: 66              LD      H,(HL)              ; Get MSB
240B: 6F              LD      L,A                 ; To HL
240C: E9              JP      (HL)                ; Jump to routine
;
; JUMP TABLE
240D: 24 24       ; 01:Do next
240F: 96 24       ; 02:??? Bees pulsing in formatin ???
2411: 6D 24       ; 03:??? Bees straightening up into formatin ???
2413: 5B 25       ; 04:?? Couldn't tell
2415: C0 24       ; 05:?? Initiate explosion removal of bee
2417: 43 25       ; 06:Remove score from screen
2419: 5B 25       ; 07:
241B: 9E 25       ; 08:?? Couldn't tell
241D: 4A 24       ; 09:?? Couldn't tell
241F: 30 24       ; 0A:?? Couldn't tell
;
;============
2421: 1D              DEC     E                   ; 
2422: DD 2C           INC     IXL                 ; 
;
;============
; Jump01:Do next
;
2424: 3E 04           LD      A,$04               ; 
2426: 83              ADD     A,E                 ; 
2427: 5F              LD      E,A                 ; 
2428: 10 D3           DJNZ    $23FD               ; {}
242A: DD 7D           LD      A,IXL               ; 
242C: 32 A6 92        LD      ($92A6),A           ; 
242F: C9              RET                         ; 
;
;============
; Jump0A:
2430: 6B              LD      L,E                 ; 
2431: 26 01           LD      H,$01               ; 
2433: 4E              LD      C,(HL)              ; 
2434: 2C              INC     L                   ; 
2435: 6E              LD      L,(HL)              ; 
2436: 26 99           LD      H,$99               ; 
2438: 7E              LD      A,(HL)              ; 
2439: 08              EX      AF,AF'              ; 
243A: 69              LD      L,C                 ; 
243B: 4E              LD      C,(HL)              ; 
243C: 1C              INC     E                   ; 
243D: 1A              LD      A,(DE)              ; 
243E: C6 11           ADD     $11                 ; 
2440: 6F              LD      L,A                 ; 
2441: 26 91           LD      H,$91               ; 
2443: 08              EX      AF,AF'              ; 
2444: 77              LD      (HL),A              ; 
2445: 2C              INC     L                   ; 
2446: 71              LD      (HL),C              ; 
2447: C3 21 24        JP      $2421               ; {}
;
;============
; Jump09:
244A: 26 8B           LD      H,$8B               ; 
244C: 6B              LD      L,E                 ; 
244D: 1C              INC     E                   ; 
244E: 1A              LD      A,(DE)              ; 
244F: 3D              DEC     A                   ; 
2450: 28 0D           JR      Z,$245F             ; {}
2452: 12              LD      (DE),A              ; 
2453: 1D              DEC     E                   ; 
2454: E6 03           AND     $03                 ; 
2456: 20 CC           JR      NZ,$2424            ; {}
2458: 7E              LD      A,(HL)              ; 
2459: C6 04           ADD     $04                 ; 
245B: 77              LD      (HL),A              ; 
245C: C3 24 24        JP      $2424               ; {}
245F: 26 93           LD      H,$93               ; 
2461: AF              XOR     A                   ; 
2462: 77              LD      (HL),A              ; 
2463: 26 9B           LD      H,$9B               ; 
2465: 77              LD      (HL),A              ; 
2466: 1D              DEC     E                   ; 
2467: 3E 80           LD      A,$80               ; 
2469: 12              LD      (DE),A              ; 
246A: C3 24 24        JP      $2424               ; {}
;
;============
; Jump03:
246D: 26 9B           LD      H,$9B               ; 
246F: 6B              LD      L,E                 ; 
2470: 7E              LD      A,(HL)              ; 
2471: E6 01           AND     $01                 ; 
2473: 26 8B           LD      H,$8B               ; 
2475: 20 0A           JR      NZ,$2481            ; {}
2477: 7E              LD      A,(HL)              ; 
2478: E6 07           AND     $07                 ; 
247A: FE 06           CP      $06                 ; 
247C: 28 13           JR      Z,$2491             ; {}
247E: 34              INC     (HL)                ; 
247F: 18 28           JR      $24A9               ; {}
2481: 7E              LD      A,(HL)              ; 
2482: E6 07           AND     $07                 ; 
2484: 20 08           JR      NZ,$248E            ; {}
2486: 26 9B           LD      H,$9B               ; 
2488: CB 86           RES     0,(HL)              ; 
248A: 26 8B           LD      H,$8B               ; 
248C: 18 1B           JR      $24A9               ; {}
248E: 35              DEC     (HL)                ; 
248F: 18 18           JR      $24A9               ; {}
2491: 3E 01           LD      A,$01               ; 
2493: 12              LD      (DE),A              ; 
2494: 18 13           JR      $24A9               ; {}
;
;============
; Jump02:
2496: 26 8B           LD      H,$8B               ; 
2498: 6B              LD      L,E                 ; 
2499: 3A A2 92        LD      A,($92A2)           ; 
249C: CB 0E           RRC     (HL)                ; 
249E: 0F              RRCA                        ; 
249F: 0F              RRCA                        ; 
24A0: CB 16           RL      (HL)                ; 
24A2: 3A 0B 92        LD      A,($920B)           ; 
24A5: A7              AND     A                   ; 
24A6: CA 22 24        JP      Z,$2422             ; {}
24A9: 26 01           LD      H,$01               ; 
24AB: 4E              LD      C,(HL)              ; 
24AC: 2C              INC     L                   ; 
24AD: 6E              LD      L,(HL)              ; 
24AE: 26 98           LD      H,$98               ; 
24B0: 7E              LD      A,(HL)              ; 
24B1: 16 93           LD      D,$93               ; 
24B3: 12              LD      (DE),A              ; 
24B4: 1C              INC     E                   ; 
24B5: 69              LD      L,C                 ; 
24B6: 7E              LD      A,(HL)              ; 
24B7: 12              LD      (DE),A              ; 
24B8: 16 9B           LD      D,$9B               ; 
24BA: 2C              INC     L                   ; 
24BB: 7E              LD      A,(HL)              ; 
24BC: 12              LD      (DE),A              ; 
24BD: C3 21 24        JP      $2421               ; {}
;
;============
; Jump05:
24C0: 6B              LD      L,E                 ; 
24C1: 1C              INC     E                   ; 
24C2: 1A              LD      A,(DE)              ; 
24C3: FE 45           CP      $45                 ; 
24C5: 28 2D           JR      Z,$24F4             ; {}
24C7: 3C              INC     A                   ; 
24C8: 12              LD      (DE),A              ; 
24C9: 1D              DEC     E                   ; 
24CA: FE 45           CP      $45                 ; 
24CC: 20 02           JR      NZ,$24D0            ; {}
24CE: C6 03           ADD     $03                 ; 
24D0: FE 44           CP      $44                 ; 
24D2: 20 1A           JR      NZ,$24EE            ; {}
24D4: 26 93           LD      H,$93               ; 
24D6: 08              EX      AF,AF'              ; 
24D7: 7E              LD      A,(HL)              ; 
24D8: D6 08           SUB     $08                 ; 
24DA: 77              LD      (HL),A              ; 
24DB: 2C              INC     L                   ; 
24DC: 7E              LD      A,(HL)              ; 
24DD: D6 08           SUB     $08                 ; 
24DF: 77              LD      (HL),A              ; 
24E0: 30 06           JR      NC,$24E8            ; {}
24E2: 26 9B           LD      H,$9B               ; 
24E4: 7E              LD      A,(HL)              ; 
24E5: EE 01           XOR     $01                 ; 
24E7: 77              LD      (HL),A              ; 
24E8: 2D              DEC     L                   ; 
24E9: 26 9B           LD      H,$9B               ; 
24EB: 36 0C           LD      (HL),$0C            ; 
24ED: 08              EX      AF,AF'              ; 
24EE: 26 8B           LD      H,$8B               ; 
24F0: 77              LD      (HL),A              ; 
24F1: C3 24 24        JP      $2424               ; {}
24F4: 1D              DEC     E                   ; 
24F5: 26 92           LD      H,$92               ; 
24F7: 7E              LD      A,(HL)              ; 
24F8: FE 01           CP      $01                 ; 
24FA: 20 0F           JR      NZ,$250B            ; {}
24FC: 26 93           LD      H,$93               ; 
24FE: 36 00           LD      (HL),$00            ; 
2500: 26 9B           LD      H,$9B               ; 
2502: 36 00           LD      (HL),$00            ; 
2504: 26 88           LD      H,$88               ; 
2506: 36 80           LD      (HL),$80            ; After explosion, free ship from active duty
2508: C3 24 24        JP      $2424               ; {}
250B: 26 8B           LD      H,$8B               ; 
250D: 77              LD      (HL),A              ; 
250E: FE 37           CP      $37                 ; 
2510: 38 0A           JR      C,$251C             ; {}
2512: 0E 0D           LD      C,$0D               ; 
2514: 2C              INC     L                   ; 
2515: FE 3A           CP      $3A                 ; 
2517: 38 01           JR      C,$251A             ; {}
2519: 0C              INC     C                   ; 
251A: 71              LD      (HL),C              ; 
251B: 2D              DEC     L                   ; 
251C: 26 93           LD      H,$93               ; 
251E: 0E 08           LD      C,$08               ; 
2520: FE 3B           CP      $3B                 ; 
2522: 30 06           JR      NC,$252A            ; {}
2524: 0E 00           LD      C,$00               ; 
2526: 7E              LD      A,(HL)              ; 
2527: C6 08           ADD     $08                 ; 
2529: 77              LD      (HL),A              ; 
252A: 2C              INC     L                   ; 
252B: 7E              LD      A,(HL)              ; 
252C: C6 08           ADD     $08                 ; 
252E: 77              LD      (HL),A              ; 
252F: 26 9B           LD      H,$9B               ; 
2531: 30 04           JR      NC,$2537            ; {}
2533: 7E              LD      A,(HL)              ; 
2534: EE 01           XOR     $01                 ; 
2536: 77              LD      (HL),A              ; 
2537: 2D              DEC     L                   ; 
2538: 71              LD      (HL),C              ; 
2539: 26 88           LD      H,$88               ; 
253B: 36 05           LD      (HL),$05            ; 
253D: 2C              INC     L                   ; 
253E: 36 13           LD      (HL),$13            ; 
2540: C3 24 24        JP      $2424               ; {}
;
;============
; Jump06:
; Time down and remove score indicator from screen.
2543: 6B              LD      L,E                 ; 
2544: 2C              INC     L                   ; Second byte
2545: 62              LD      H,D                 ; 
2546: 35              DEC     (HL)                ; Decrement time
2547: C2 24 24        JP      NZ,$2424            ; {} Not time yet
254A: 2D              DEC     L                   ; Restore pointer
254B: 36 80           LD      (HL),$80            ; This section ...
254D: 26 93           LD      H,$93               ; ... removes score ...
254F: 36 00           LD      (HL),$00            ; ... indicator from ...
2551: 26 9B           LD      H,$9B               ; ... screen.
2553: 36 00           LD      (HL),$00            ; '
2555: 3E 80           LD      A,$80               ; '
2557: 12              LD      (DE),A              ; '
2558: C3 24 24        JP      $2424               ; {} Do next
;
;============
; Jump04,07:
; Remove item if Y coordinate is too close to bottom or top of screen.
255B: 26 93           LD      H,$93               ; Coordinates
255D: 6B              LD      L,E                 ; 
255E: CB FD           SET     7,L                 ; ?
2560: 7E              LD      A,(HL)              ; [00] Get X coordinate
2561: FE F4           CP      $F4                 ; => F4 ?
2563: 30 1A           JR      NC,$257F            ; {} Yes ... Remove from duty
2565: 2C              INC     L                   ; Point to Y
2566: 4E              LD      C,(HL)              ; [74] Get Y coordinate
2567: 26 9B           LD      H,$9B               ; This gets set as a special in the movement code
2569: 7E              LD      A,(HL)              ; [00]
256A: 2D              DEC     L                   ; Restore pointer
256B: 0F              RRCA                        ; [C=0]
256C: 79              LD      A,C                 ; [74] Y coordinate
256D: 1F              RRA                         ; 
256E: FE 0B           CP      $0B                 ; If Y coordinate is too close to top of screen ...
2570: 38 0D           JR      C,$257F             ; {} ... remove it (Y< 0B).
2572: FE A5           CP      $A5                 ; If Y coordinate is too close to bottom of screen ...
2574: 30 09           JR      NC,$257F            ; {} ... remove it (Y>= A5).
2576: 1A              LD      A,(DE)              ; Get type
2577: FE 06           CP      $06                 ; Bee shot?
2579: C2 22 24        JP      NZ,$2422            ; {} Not a bee shot ... do something and next
257C: C3 24 24        JP      $2424               ; {} Do next
; Remove item from active duty
257F: CB BD           RES     7,L                 ; 
2581: 1A              LD      A,(DE)              ; Type
2582: FE 03           CP      $03                 ; 
2584: 28 0A           JR      Z,$2590             ; {}
2586: 3E 80           LD      A,$80               ; Flag free slot
2588: 12              LD      (DE),A              ; Here it is -- shots are erased here.
2589: 26 93           LD      H,$93               ; Free ...
258B: 36 00           LD      (HL),$00            ; ... sprite
258D: C3 24 24        JP      $2424               ; {} Do next
;
; Additional processing and remove from duty
2590: 1C              INC     E                   ; 2nd byte
2591: 1A              LD      A,(DE)              ; Get ???
2592: 1D              DEC     E                   ; Restore pointer
2593: C6 13           ADD     $13                 ; 
2595: 6F              LD      L,A                 ; 
2596: 26 91           LD      H,$91               ; 
2598: 36 00           LD      (HL),$00            ; 
259A: 6B              LD      L,E                 ; 
259B: C3 86 25        JP      $2586               ; {} Continue removing from active duty
;
;============
; Jump08:
259E: 3E 03           LD      A,$03               ; 
25A0: 12              LD      (DE),A              ; 
25A1: C3 22 24        JP      $2422               ; {}
25A4: CB 4F           BIT     1,A                 ; 
25A6: C8              RET     Z                   ; 
25A7: 21 A6 92        LD      HL,$92A6            ; 
25AA: 7E              LD      A,(HL)              ; 
25AB: 36 00           LD      (HL),$00            ; 
25AD: 2C              INC     L                   ; 
25AE: 77              LD      (HL),A              ; 
25AF: C9              RET                         ; 

;======================================================================
;
25B0: 21 7C 28        LD      HL,$287C            ; 
25B3: 22 E0 92        LD      ($92E0),HL          ; 
25B6: 3A 21 98        LD      A,($9821)           ; 
25B9: 4F              LD      C,A                 ; 
25BA: FE 17           CP      $17                 ; 
25BC: 38 04           JR      C,$25C2             ; {}
25BE: D6 04           SUB     $04                 ; 
25C0: 18 F8           JR      $25BA               ; {}
25C2: 47              LD      B,A                 ; 
25C3: 3C              INC     A                   ; 
25C4: E6 03           AND     $03                 ; 
25C6: 28 19           JR      Z,$25E1             ; {}
25C8: 3A 84 99        LD      A,($9984)           ; 
25CB: 2E 11           LD      L,$11               ; 
25CD: CD 4E 10        CALL    $104E               ; {}
25D0: 7D              LD      A,L                 ; 
25D1: 21 B6 26        LD      HL,$26B6            ; 
25D4: D7              RST     0X10                ; 
25D5: 11 02 27        LD      DE,$2702            ; 
25D8: 78              LD      A,B                 ; 
25D9: CB 38           SRL     B                   ; 
25DB: CB 38           SRL     B                   ; 
25DD: 90              SUB     B                   ; 
25DE: 3D              DEC     A                   ; 
25DF: 18 0D           JR      $25EE               ; {}
25E1: 21 FA 26        LD      HL,$26FA            ; 
25E4: 79              LD      A,C                 ; 
25E5: CB 3F           SRL     A                   ; 
25E7: CB 3F           SRL     A                   ; 
25E9: E6 07           AND     $07                 ; 
25EB: 11 EC 27        LD      DE,$27EC            ; 
25EE: D7              RST     0X10                ; 
25EF: 7E              LD      A,(HL)              ; 
25F0: EB              EX      DE,HL               ; 
25F1: D7              RST     0X10                ; 
25F2: 7E              LD      A,(HL)              ; 
25F3: 23              INC     HL                  ; 
25F4: 32 E2 92        LD      ($92E2),A           ; 
25F7: 7E              LD      A,(HL)              ; 
25F8: 23              INC     HL                  ; 
25F9: 32 E3 92        LD      ($92E3),A           ; 
25FC: 11 20 89        LD      DE,$8920            ; 
25FF: 3E 7E           LD      A,$7E               ; 
2601: 12              LD      (DE),A              ; 
2602: 1C              INC     E                   ; 
2603: 7E              LD      A,(HL)              ; 
2604: 23              INC     HL                  ; 
2605: FE FF           CP      $FF                 ; 
2607: CA 8F 26        JP      Z,$268F             ; {}
260A: 4F              LD      C,A                 ; 
260B: D5              PUSH    DE                  ; 
260C: E5              PUSH    HL                  ; 
260D: 21 00 91        LD      HL,$9100            ; Bee space
2610: 3E FF           LD      A,$FF               ; 
2612: 06 10           LD      B,$10               ; 
2614: DF              RST     0X18                ; Fill first 16 bytes with FF?
2615: 79              LD      A,C                 ; 
2616: E6 0F           AND     $0F                 ; 
2618: 28 2A           JR      Z,$2644             ; {}
261A: 47              LD      B,A                 ; 
261B: CB 3F           SRL     A                   ; 
261D: C6 04           ADD     $04                 ; 
261F: 5F              LD      E,A                 ; 
2620: CD 00 10        CALL    $1000               ; {}
2623: 6F              LD      L,A                 ; 
2624: 26 00           LD      H,$00               ; 
2626: 7B              LD      A,E                 ; 
2627: CD 61 10        CALL    $1061               ; {}
262A: CB 40           BIT     0,B                 ; 
262C: 28 02           JR      Z,$2630             ; {}
262E: CB DF           SET     3,A                 ; 
2630: 26 91           LD      H,$91               ; 
2632: 6F              LD      L,A                 ; 
2633: 7E              LD      A,(HL)              ; 
2634: 3C              INC     A                   ; 
2635: 20 E9           JR      NZ,$2620            ; {}
2637: 78              LD      A,B                 ; 
2638: 07              RLCA                        ; 
2639: CB 01           RLC     C                   ; 
263B: 30 02           JR      NC,$263F            ; {}
263D: F6 40           OR      $40                 ; 
263F: F6 38           OR      $38                 ; 
2641: 77              LD      (HL),A              ; 
2642: 10 DC           DJNZ    $2620               ; {}
;
2644: 21 00 91        LD      HL,$9100            ; 
2647: ED 5B E0 92     LD      DE,($92E0)          ; 
264B: 06 08           LD      B,$08               ; 
264D: 7E              LD      A,(HL)              ; 
264E: FE FF           CP      $FF                 ; 
2650: 28 03           JR      Z,$2655             ; {}
2652: 23              INC     HL                  ; 
2653: 18 F8           JR      $264D               ; {} Find first FF starting at 9100
2655: 1A              LD      A,(DE)              ; 
2656: 77              LD      (HL),A              ; 
2657: 13              INC     DE                  ; 
2658: 23              INC     HL                  ; 
2659: 78              LD      A,B                 ; 
265A: FE 05           CP      $05                 ; 
265C: 20 02           JR      NZ,$2660            ; {}
265E: 2E 08           LD      L,$08               ; 
2660: 10 EB           DJNZ    $264D               ; {}
2662: ED 53 E0 92     LD      ($92E0),DE          ; 
2666: E1              POP     HL                  ; 
2667: D1              POP     DE                  ; 
2668: 46              LD      B,(HL)              ; 
2669: 23              INC     HL                  ; 
266A: 4E              LD      C,(HL)              ; 
266B: 23              INC     HL                  ; 
266C: E5              PUSH    HL                  ; 
266D: 21 00 91        LD      HL,$9100            ; 
2670: 78              LD      A,B                 ; 
2671: 12              LD      (DE),A              ; 
2672: 7E              LD      A,(HL)              ; 
2673: FE FF           CP      $FF                 ; 
2675: 28 10           JR      Z,$2687             ; {}
2677: 1C              INC     E                   ; 
2678: 12              LD      (DE),A              ; 
2679: 1C              INC     E                   ; 
267A: 79              LD      A,C                 ; 
267B: 12              LD      (DE),A              ; 
267C: 1C              INC     E                   ; 
267D: CB DD           SET     3,L                 ; 
267F: 7E              LD      A,(HL)              ; 
2680: 12              LD      (DE),A              ; 
2681: 1C              INC     E                   ; 
2682: CB 9D           RES     3,L                 ; 
2684: 23              INC     HL                  ; 
2685: 18 E9           JR      $2670               ; {}
2687: 3E 7E           LD      A,$7E               ; 
2689: 12              LD      (DE),A              ; 
268A: 1C              INC     E                   ; 
268B: E1              POP     HL                  ; 
268C: C3 03 26        JP      $2603               ; {}
268F: 1D              DEC     E                   ; 
2690: 3A 2B 98        LD      A,($982B)           ; 
2693: 47              LD      B,A                 ; 
2694: 3A 27 98        LD      A,($9827)           ; 
2697: 3D              DEC     A                   ; 
2698: A0              AND     B                   ; 
2699: 28 17           JR      Z,$26B2             ; {}
269B: 3A 25 98        LD      A,($9825)           ; 
269E: A7              AND     A                   ; 
269F: 28 11           JR      Z,$26B2             ; {}
26A1: 62              LD      H,D                 ; 
26A2: 7B              LD      A,E                 ; 
26A3: D6 04           SUB     $04                 ; 
26A5: 6F              LD      L,A                 ; 
26A6: 7E              LD      A,(HL)              ; 
26A7: 12              LD      (DE),A              ; 
26A8: 1C              INC     E                   ; 
26A9: 3E 04           LD      A,$04               ; 
26AB: 12              LD      (DE),A              ; 
26AC: 1C              INC     E                   ; 
26AD: 3E 87           LD      A,$87               ; 
26AF: 32 04 8B        LD      ($8B04),A           ; 
26B2: 3E 7F           LD      A,$7F               ; 
26B4: 12              LD      (DE),A              ; 
26B5: C9              RET                         ; 

26B6: 00              NOP                         ; #
26B7: 12              LD      (DE),A              ; #
26B8: 24              INC     H                   ; #
26B9: 36 00           LD      (HL),$00            ; #
26BB: 48              LD      C,B                 ; #
26BC: 6C              LD      L,H                 ; #
26BD: 5A              LD      E,D                 ; #
26BE: 48              LD      C,B                 ; #
26BF: 6C              LD      L,H                 ; #
26C0: 00              NOP                         ; #
26C1: 7E              LD      A,(HL)              ; #
26C2: A2              AND     D                   ; #
26C3: 90              SUB     B                   ; #
26C4: B4              OR      H                   ; #
26C5: D8              RET     C                   ; #
26C6: C6 00           ADD     $00                 ; #
26C8: 12              LD      (DE),A              ; #
26C9: 48              LD      C,B                 ; #
26CA: 6C              LD      L,H                 ; #
26CB: 5A              LD      E,D                 ; #
26CC: 7E              LD      A,(HL)              ; #
26CD: A2              AND     D                   ; #
26CE: 00              NOP                         ; #
26CF: 7E              LD      A,(HL)              ; #
26D0: D8              RET     C                   ; #
26D1: C6 B4           ADD     $B4                 ; #
26D3: D8              RET     C                   ; #
26D4: C6 B4           ADD     $B4                 ; #
26D6: D8              RET     C                   ; #
26D7: C6 00           ADD     $00                 ; #
26D9: 12              LD      (DE),A              ; #
26DA: 7E              LD      A,(HL)              ; #
26DB: A2              AND     D                   ; #
26DC: 90              SUB     B                   ; #
26DD: 7E              LD      A,(HL)              ; #
26DE: D8              RET     C                   ; #
26DF: C6 B4           ADD     $B4                 ; #
26E1: D8              RET     C                   ; #
26E2: C6 B4           ADD     $B4                 ; #
26E4: D8              RET     C                   ; #
26E5: C6 B4           ADD     $B4                 ; #
26E7: D8              RET     C                   ; #
26E8: C6 00           ADD     $00                 ; #
26EA: 12              LD      (DE),A              ; #
26EB: 48              LD      C,B                 ; #
26EC: 36 24           LD      (HL),$24            ; #
26EE: 48              LD      C,B                 ; #
26EF: 6C              LD      L,H                 ; #
26F0: 00              NOP                         ; #
26F1: 7E              LD      A,(HL)              ; #
26F2: A2              AND     D                   ; #
26F3: 90              SUB     B                   ; #
26F4: B4              OR      H                   ; #
26F5: D8              RET     C                   ; #
26F6: 00              NOP                         ; #
26F7: B4              OR      H                   ; #
26F8: D8              RET     C                   ; #
26F9: C6 00           ADD     $00                 ; #
26FB: 12              LD      (DE),A              ; #
26FC: 24              INC     H                   ; #
26FD: 36 48           LD      (HL),$48            ; #
26FF: 5A              LD      E,D                 ; #
2700: 6C              LD      L,H                 ; #
2701: 7E              LD      A,(HL)              ; #
;
2702: 14              INC     D                   ; #
2703: 00              NOP                         ; #
2704: 00              NOP                         ; #
2705: 00              NOP                         ; #
2706: C0              RET     NZ                  ; #
2707: 00              NOP                         ; #
2708: 01 01 00        LD      BC,$0001            ; #
270B: 41              LD      B,C                 ; #
270C: 41              LD      B,C                 ; #
270D: 00              NOP                         ; #
270E: 40              LD      B,B                 ; #
270F: 40              LD      B,B                 ; #
2710: 00              NOP                         ; #
2711: 00              NOP                         ; #
2712: 00              NOP                         ; #
2713: FF              RST     0X38                ; #
2714: 14              INC     D                   ; #
2715: 01 00 42        LD      BC,$4200            ; #
2718: 82              ADD     A,D                 ; #
2719: 00              NOP                         ; #
271A: 03              INC     BC                  ; #
271B: 85              ADD     A,L                 ; #
271C: 00              NOP                         ; #
271D: 43              LD      B,E                 ; #
271E: C5              PUSH    BC                  ; #
271F: 00              NOP                         ; #
2720: 42              LD      B,D                 ; #
2721: C4 00 02        CALL    NZ,$0200            ; {} #
2724: 84              ADD     A,H                 ; #
2725: FF              RST     0X38                ; #
2726: 14              INC     D                   ; #
2727: 01 82 00        LD      BC,$0082            ; #
272A: C0              RET     NZ                  ; #
272B: 00              NOP                         ; #
272C: 01 01 00        LD      BC,$0001            ; #
272F: 41              LD      B,C                 ; #
2730: 41              LD      B,C                 ; #
2731: 02              LD      (BC),A              ; #
2732: 40              LD      B,B                 ; #
2733: 40              LD      B,B                 ; #
2734: 02              LD      (BC),A              ; #
2735: 00              NOP                         ; #
2736: 00              NOP                         ; #
2737: FF              RST     0X38                ; #
2738: 14              INC     D                   ; #
2739: 01 82 02        LD      BC,$0282            ; #
273C: C2 00 03        JP      NZ,$0300            ; {} #
273F: 85              ADD     A,L                 ; #
2740: 00              NOP                         ; #
2741: 43              LD      B,E                 ; #
2742: C5              PUSH    BC                  ; #
2743: 02              LD      (BC),A              ; #
2744: 42              LD      B,D                 ; #
2745: C4 02 02        CALL    NZ,$0202            ; {} #
2748: 84              ADD     A,H                 ; #
2749: FF              RST     0X38                ; #
274A: 14              INC     D                   ; #
274B: 01 82 00        LD      BC,$0082            ; #
274E: C0              RET     NZ                  ; #
274F: 00              NOP                         ; #
2750: 01 C1 00        LD      BC,$00C1            ; #
2753: 41              LD      B,C                 ; #
2754: 81              ADD     A,C                 ; #
2755: 02              LD      (BC),A              ; #
2756: 40              LD      B,B                 ; #
2757: 80              ADD     A,B                 ; #
2758: 02              LD      (BC),A              ; #
2759: 40              LD      B,B                 ; #
275A: 80              ADD     A,B                 ; #
275B: FF              RST     0X38                ; #
275C: 14              INC     D                   ; #
275D: 01 82 00        LD      BC,$0082            ; #
2760: C0              RET     NZ                  ; #
2761: 42              LD      B,D                 ; #
2762: 01 01 F2        LD      BC,$F201            ; #
2765: 41              LD      B,C                 ; #
2766: 41              LD      B,C                 ; #
2767: 02              LD      (BC),A              ; #
2768: 40              LD      B,B                 ; #
2769: 40              LD      B,B                 ; #
276A: 02              LD      (BC),A              ; #
276B: 00              NOP                         ; #
276C: 00              NOP                         ; #
276D: FF              RST     0X38                ; #
276E: 14              INC     D                   ; #
276F: 01 A4 02        LD      BC,$02A4            ; #
2772: C2 52 03        JP      NZ,$0352            ; {} #
2775: 85              ADD     A,L                 ; #
2776: F2 43 C5        JP      P,$C543             ; #
2779: 02              LD      (BC),A              ; #
277A: 42              LD      B,D                 ; #
277B: C4 02 02        CALL    NZ,$0202            ; {} #
277E: 84              ADD     A,H                 ; #
277F: FF              RST     0X38                ; #
2780: 14              INC     D                   ; #
2781: 01 82 00        LD      BC,$0082            ; #
2784: C0              RET     NZ                  ; #
2785: 52              LD      D,D                 ; #
2786: 01 C1 F2        LD      BC,$F2C1            ; #
2789: 41              LD      B,C                 ; #
278A: 81              ADD     A,C                 ; #
278B: 02              LD      (BC),A              ; #
278C: 40              LD      B,B                 ; #
278D: 80              ADD     A,B                 ; #
278E: 02              LD      (BC),A              ; #
278F: 40              LD      B,B                 ; #
2790: 80              ADD     A,B                 ; #
2791: FF              RST     0X38                ; #
2792: 14              INC     D                   ; #
2793: 01 A4 00        LD      BC,$00A4            ; #
2796: C0              RET     NZ                  ; #
2797: 42              LD      B,D                 ; #
2798: 01 01 F4        LD      BC,$F401            ; #
279B: 41              LD      B,C                 ; #
279C: 41              LD      B,C                 ; #
279D: 04              INC     B                   ; #
279E: 40              LD      B,B                 ; #
279F: 40              LD      B,B                 ; #
27A0: 04              INC     B                   ; #
27A1: 00              NOP                         ; #
27A2: 00              NOP                         ; #
27A3: FF              RST     0X38                ; #
27A4: 14              INC     D                   ; #
27A5: 01 A4 02        LD      BC,$02A4            ; #
27A8: C2 52 03        JP      NZ,$0352            ; {} #
27AB: 85              ADD     A,L                 ; #
27AC: F4 43 C5        CALL    P,$C543             ; #
27AF: 04              INC     B                   ; #
27B0: 42              LD      B,D                 ; #
27B1: C4 04 02        CALL    NZ,$0204            ; {} #
27B4: 84              ADD     A,H                 ; #
27B5: FF              RST     0X38                ; #
27B6: 14              INC     D                   ; #
27B7: 03              INC     BC                  ; #
27B8: A4              AND     H                   ; #
27B9: 00              NOP                         ; #
27BA: C0              RET     NZ                  ; #
27BB: 54              LD      D,H                 ; #
27BC: 01 C1 F4        LD      BC,$F4C1            ; #
27BF: 41              LD      B,C                 ; #
27C0: 81              ADD     A,C                 ; #
27C1: 04              INC     B                   ; #
27C2: 40              LD      B,B                 ; #
27C3: 80              ADD     A,B                 ; #
27C4: 04              INC     B                   ; #
27C5: 40              LD      B,B                 ; #
27C6: 80              ADD     A,B                 ; #
27C7: FF              RST     0X38                ; #
27C8: 14              INC     D                   ; #
27C9: 03              INC     BC                  ; #
27CA: A4              AND     H                   ; #
27CB: 00              NOP                         ; #
27CC: C0              RET     NZ                  ; #
27CD: 54              LD      D,H                 ; #
27CE: 01 01 F4        LD      BC,$F401            ; #
27D1: 41              LD      B,C                 ; #
27D2: 41              LD      B,C                 ; #
27D3: 04              INC     B                   ; #
27D4: 40              LD      B,B                 ; #
27D5: 40              LD      B,B                 ; #
27D6: 04              INC     B                   ; #
27D7: 00              NOP                         ; #
27D8: 00              NOP                         ; #
27D9: FF              RST     0X38                ; #
27DA: 14              INC     D                   ; #
27DB: 03              INC     BC                  ; #
27DC: A4              AND     H                   ; #
27DD: 02              LD      (BC),A              ; #
27DE: C2 54 03        JP      NZ,$0354            ; {} #
27E1: 85              ADD     A,L                 ; #
27E2: F4 43 C5        CALL    P,$C543             ; #
27E5: 04              INC     B                   ; #
27E6: 42              LD      B,D                 ; #
27E7: C4 04 02        CALL    NZ,$0204            ; {} #
27EA: 84              ADD     A,H                 ; #
27EB: FF              RST     0X38                ; #
27EC: FF              RST     0X38                ; #
27ED: 00              NOP                         ; #
27EE: 00              NOP                         ; #
27EF: 06 C6           LD      B,$C6               ; #
27F1: 00              NOP                         ; #
27F2: 07              RLCA                        ; #
27F3: 07              RLCA                        ; #
27F4: 00              NOP                         ; #
27F5: 47              LD      B,A                 ; #
27F6: 47              LD      B,A                 ; #
27F7: 00              NOP                         ; #
27F8: 46              LD      B,(HL)              ; #
27F9: 46              LD      B,(HL)              ; #
27FA: 00              NOP                         ; #
27FB: 06 06           LD      B,$06               ; #
27FD: FF              RST     0X38                ; #
27FE: FF              RST     0X38                ; #
27FF: 00              NOP                         ; #
2800: 00              NOP                         ; #
2801: 08              EX      AF,AF'              ; #
2802: C8              RET     Z                   ; #
2803: 00              NOP                         ; #
2804: 09              ADD     HL,BC               ; #
2805: C9              RET                         ; #
2806: 00              NOP                         ; #
2807: 09              ADD     HL,BC               ; #
2808: C9              RET                         ; #
2809: 00              NOP                         ; #
280A: 48              LD      C,B                 ; #
280B: 48              LD      C,B                 ; #
280C: 00              NOP                         ; #
280D: 08              EX      AF,AF'              ; #
280E: 08              EX      AF,AF'              ; #
280F: FF              RST     0X38                ; #
2810: FF              RST     0X38                ; #
2811: 00              NOP                         ; #
2812: 00              NOP                         ; #
2813: 0A              LD      A,(BC)              ; #
2814: 4A              LD      C,D                 ; #
2815: 00              NOP                         ; #
2816: 0B              DEC     BC                  ; #
2817: CB 00           RLC     B                   ; #
2819: 0B              DEC     BC                  ; #
281A: CB 00           RLC     B                   ; #
281C: 0A              LD      A,(BC)              ; #
281D: 4A              LD      C,D                 ; #
281E: 00              NOP                         ; #
281F: 16 56           LD      D,$56               ; #
2821: FF              RST     0X38                ; #
2822: FF              RST     0X38                ; #
2823: 00              NOP                         ; #
2824: 00              NOP                         ; #
2825: 0C              INC     C                   ; #
2826: CC 00 0D        CALL    Z,$0D00             ; {} #
2829: 0D              DEC     C                   ; #
282A: 00              NOP                         ; #
282B: 4D              LD      C,L                 ; #
282C: 4D              LD      C,L                 ; #
282D: 00              NOP                         ; #
282E: 0C              INC     C                   ; #
282F: CC 00 17        CALL    Z,$1700             ; {} #
2832: D7              RST     0X10                ; #
2833: FF              RST     0X38                ; #
2834: FF              RST     0X38                ; #
2835: 00              NOP                         ; #
2836: 00              NOP                         ; #
2837: 0E 0E           LD      C,$0E               ; #
2839: 00              NOP                         ; #
283A: 0F              RRCA                        ; #
283B: 0F              RRCA                        ; #
283C: 00              NOP                         ; #
283D: 4F              LD      C,A                 ; #
283E: 4F              LD      C,A                 ; #
283F: 00              NOP                         ; #
2840: 0E 0E           LD      C,$0E               ; #
2842: 00              NOP                         ; #
2843: 4E              LD      C,(HL)              ; #
2844: 4E              LD      C,(HL)              ; #
2845: FF              RST     0X38                ; #
2846: FF              RST     0X38                ; #
2847: 00              NOP                         ; #
2848: 00              NOP                         ; #
2849: 10 10           DJNZ    $285B               ; {} #
284B: 00              NOP                         ; #
284C: 11 D1 00        LD      DE,$00D1            ; #
284F: 11 D1 00        LD      DE,$00D1            ; #
2852: 50              LD      D,B                 ; #
2853: 50              LD      D,B                 ; #
2854: 00              NOP                         ; #
2855: 10 10           DJNZ    $2867               ; {} #
2857: FF              RST     0X38                ; #
2858: FF              RST     0X38                ; #
2859: 00              NOP                         ; #
285A: 00              NOP                         ; #
285B: 12              LD      (DE),A              ; #
285C: 12              LD      (DE),A              ; #
285D: 00              NOP                         ; #
285E: 13              INC     DE                  ; #
285F: 13              INC     DE                  ; #
2860: 00              NOP                         ; #
2861: 53              LD      D,E                 ; #
2862: 53              LD      D,E                 ; #
2863: 00              NOP                         ; #
2864: 52              LD      D,D                 ; #
2865: 52              LD      D,D                 ; #
2866: 00              NOP                         ; #
2867: 12              LD      (DE),A              ; #
2868: 12              LD      (DE),A              ; #
2869: FF              RST     0X38                ; #
286A: FF              RST     0X38                ; #
286B: 00              NOP                         ; #
286C: 00              NOP                         ; #
286D: 14              INC     D                   ; #
286E: D4 00 15        CALL    NC,$1500            ; {} #
2871: 15              DEC     D                   ; #
2872: 00              NOP                         ; #
2873: 55              LD      D,L                 ; #
2874: 55              LD      D,L                 ; #
2875: 00              NOP                         ; #
2876: 14              INC     D                   ; #
2877: D4 00 14        CALL    NC,$1400            ; {} #
287A: D4 FF 58        CALL    NC,$58FF            ; #
287D: 5A              LD      E,D                 ; #
287E: 5C              LD      E,H                 ; #
287F: 5E              LD      E,(HL)              ; #
2880: 28 2A           JR      Z,$28AC             ; {} #
2882: 2C              INC     L                   ; #
2883: 2E 30           LD      L,$30               ; #
2885: 34              INC     (HL)                ; #
2886: 36 32           LD      (HL),$32            ; #
2888: 50              LD      D,B                 ; #
2889: 52              LD      D,D                 ; #
288A: 54              LD      D,H                 ; #
288B: 56              LD      D,(HL)              ; #
288C: 42              LD      B,D                 ; #
288D: 46              LD      B,(HL)              ; #
288E: 40              LD      B,B                 ; #
288F: 44              LD      B,H                 ; #
2890: 4A              LD      C,D                 ; #
2891: 4E              LD      C,(HL)              ; #
2892: 48              LD      C,B                 ; #
2893: 4C              LD      C,H                 ; #
2894: 1A              LD      A,(DE)              ; #
2895: 1E 20           LD      E,$20               ; #
2897: 24              INC     H                   ; #
2898: 22 26 18        LD      ($1826),HL          ; {} #
289B: 1C              INC     E                   ; #
289C: 08              EX      AF,AF'              ; #
289D: 0C              INC     C                   ; #
289E: 12              LD      (DE),A              ; #
289F: 16 10           LD      D,$10               ; #
28A1: 14              INC     D                   ; #
28A2: 0A              LD      A,(BC)              ; #
28A3: 0E 21           LD      C,$21               ; #
28A5: 20 89           JR      NZ,$2830            ; {} #

28A7: 22 22 98        LD      ($9822),HL          ; 
28AA: FD 21 16 29     LD      IY,$2916            ; 
28AE: 3A 25 98        LD      A,($9825)           ; 
28B1: A7              AND     A                   ; 
28B2: 20 27           JR      NZ,$28DB            ; {}
28B4: 3A 21 98        LD      A,($9821)           ; 
28B7: 0F              RRCA                        ; 
28B8: 0F              RRCA                        ; 
28B9: 4F              LD      C,A                 ; 
28BA: 0F              RRCA                        ; 
28BB: 47              LD      B,A                 ; 
28BC: E6 1C           AND     $1C                 ; 
28BE: 78              LD      A,B                 ; 
28BF: 28 02           JR      Z,$28C3             ; {}
28C1: 3E 03           LD      A,$03               ; 
28C3: E6 03           AND     $03                 ; 
28C5: 21 0E 29        LD      HL,$290E            ; Data block after routine
28C8: CF              RST     0X08                ; HL=HL+A*2
28C9: 11 84 92        LD      DE,$9284            ; 
28CC: 79              LD      A,C                 ; 
28CD: ED A0           LDI                         ; 
28CF: ED A0           LDI                         ; 
28D1: 21 1C 29        LD      HL,$291C            ; 
28D4: E6 07           AND     $07                 ; 
28D6: D7              RST     0X10                ; 
28D7: 56              LD      D,(HL)              ; 
28D8: 5A              LD      E,D                 ; 
28D9: 18 03           JR      $28DE               ; {}
28DB: 11 24 36        LD      DE,$3624            ; 
28DE: 21 08 8B        LD      HL,$8B08            ; 
28E1: DD 2E 01        LD      IXL,$01             ; 
28E4: 06 14           LD      B,$14               ; 
28E6: DD 62           LD      IXH,D               ; 
28E8: CD F7 28        CALL    $28F7               ; {}
28EB: 06 08           LD      B,$08               ; 
28ED: DD 26 10        LD      IXH,$10             ; 
28F0: CD F7 28        CALL    $28F7               ; {}
28F3: 06 10           LD      B,$10               ; 
28F5: DD 63           LD      IXH,E               ; 
28F7: DD 2D           DEC     IXL                 ; 
28F9: 20 08           JR      NZ,$2903            ; {}
28FB: FD 4E 00        LD      C,(IY+$00)          ; 
28FE: FD 23           INC     IY                  ; 
2900: DD 2E 08        LD      IXL,$08             ; 
2903: CB 01           RLC     C                   ; 
2905: DD 7C           LD      A,IXH               ; 
2907: 1F              RRA                         ; 
2908: 77              LD      (HL),A              ; 
2909: 2C              INC     L                   ; 
290A: 2C              INC     L                   ; 
290B: 10 EA           DJNZ    $28F7               ; {}
290D: C9              RET                         ; 
;
290E: 0A B8       ;
2910: 0F B9       ;
2912: 14 BC       ;
2914: 1E BD       ;
2916: A5 5A       ;
2918: A9 0F       ;
291A: 0A 50       ;
291C: 36 24       ;
291E: D4 BA       ;
2920: E4 CC       ;
2922: A8 F4       ;

;======================================================================
; PLAY COMMAND 08 ??
;
2924: 2A 22 98        LD      HL,($9822)          ; 
2927: 7E              LD      A,(HL)              ; 
2928: FE 7F           CP      $7F                 ; 
292A: CA 37 2A        JP      Z,$2A37             ; {}
292D: FE 7E           CP      $7E                 ; 
292F: 20 30           JR      NZ,$2961            ; {}
2931: 3A 42 98        LD      A,($9842)           ; 
2934: A7              AND     A                   ; 
2935: C8              RET     Z                   ; 
2936: 3A 87 92        LD      A,($9287)           ; 
2939: A7              AND     A                   ; 
293A: 20 1F           JR      NZ,$295B            ; {}
293C: 3A 25 98        LD      A,($9825)           ; 
293F: 47              LD      B,A                 ; 
2940: A7              AND     A                   ; 
2941: 20 0F           JR      NZ,$2952            ; {}
2943: 3A AC 92        LD      A,($92AC)           ; 
2946: FE 01           CP      $01                 ; 
2948: 20 06           JR      NZ,$2950            ; {}
294A: 3E 08           LD      A,$08               ; 
294C: 32 A8 92        LD      ($92A8),A           ; 
294F: C9              RET                         ; 
2950: A7              AND     A                   ; 
2951: C0              RET     NZ                  ; 
2952: 23              INC     HL                  ; 
2953: 22 22 98        LD      ($9822),HL          ; 
2956: 21 26 98        LD      HL,$9826            ; 
2959: 34              INC     (HL)                ; 
295A: C9              RET                         ; 
295B: 3E 02           LD      A,$02               ; 
295D: 32 AC 92        LD      ($92AC),A           ; 
2960: C9              RET                         ; 
2961: 4F              LD      C,A                 ; 
2962: CB 7F           BIT     7,A                 ; 
2964: 20 06           JR      NZ,$296C            ; {}
2966: 3A A0 92        LD      A,($92A0)           ; 
2969: E6 07           AND     $07                 ; 
296B: C0              RET     NZ                  ; 
296C: CB 21           SLA     C                   ; 
296E: 06 0C           LD      B,$0C               ; 
2970: 11 14 00        LD      DE,$0014            ; 14 Bytes per bee
2973: DD 21 00 91     LD      IX,$9100            ; Bee space
2977: DD CB 13 46     BIT     0,(IX+$13)          ; Process this?
297B: 28 05           JR      Z,$2982             ; {} Yes ...
297D: DD 19           ADD     IX,DE               ; Else next bee
297F: 10 F6           DJNZ    $2977               ; {} Keep going
2981: C9              RET                         ; Done

2982: 23              INC     HL                  ; 
2983: 7E              LD      A,(HL)              ; 
2984: 47              LD      B,A                 ; 
2985: E6 78           AND     $78                 ; 
2987: FE 78           CP      $78                 ; 
2989: 78              LD      A,B                 ; 
298A: 20 02           JR      NZ,$298E            ; {}
298C: CB B7           RES     6,A                 ; 
298E: DD 77 10        LD      (IX+$10),A          ; 
2991: 23              INC     HL                  ; 
2992: 22 22 98        LD      ($9822),HL          ; 
2995: 26 88           LD      H,$88               ; 
2997: 6F              LD      L,A                 ; 
2998: 36 07           LD      (HL),$07            ; 
299A: 2C              INC     L                   ; 
299B: DD 5D           LD      E,IXL               ; 
299D: 73              LD      (HL),E              ; 
299E: 26 93           LD      H,$93               ; 
29A0: E6 38           AND     $38                 ; 
29A2: FE 38           CP      $38                 ; 
29A4: 28 1B           JR      Z,$29C1             ; {}
29A6: 2D              DEC     L                   ; 
29A7: 26 8B           LD      H,$8B               ; 
29A9: 7E              LD      A,(HL)              ; 
29AA: 57              LD      D,A                 ; 
29AB: E6 78           AND     $78                 ; 
29AD: 77              LD      (HL),A              ; 
29AE: 2C              INC     L                   ; 
29AF: 7A              LD      A,D                 ; 
29B0: E6 07           AND     $07                 ; 
29B2: CB 7A           BIT     7,D                 ; 
29B4: 77              LD      (HL),A              ; 
29B5: 3E 00           LD      A,$00               ; 
29B7: 28 03           JR      Z,$29BC             ; {}
29B9: 3A E3 92        LD      A,($92E3)           ; 
29BC: DD 77 0F        LD      (IX+$0F),A          ; 
29BF: 18 1E           JR      $29DF               ; {}
29C1: 11 10 02        LD      DE,$0210            ; 
29C4: CB 70           BIT     6,B                 ; 
29C6: 20 0D           JR      NZ,$29D5            ; {}
29C8: 11 18 03        LD      DE,$0318            ; 
29CB: 3A 26 98        LD      A,($9826)           ; 
29CE: FE 02           CP      $02                 ; 
29D0: 20 03           JR      NZ,$29D5            ; {}
29D2: 11 08 00        LD      DE,$0008            ; 
29D5: 26 8B           LD      H,$8B               ; 
29D7: 72              LD      (HL),D              ; 
29D8: 2D              DEC     L                   ; 
29D9: 73              LD      (HL),E              ; 
29DA: 2C              INC     L                   ; 
29DB: DD 36 0F 00     LD      (IX+$0F),$00        ; No firing
29DF: 51              LD      D,C                 ; 
29E0: CB B9           RES     7,C                 ; 
29E2: 06 08           LD      B,$08               ; 
29E4: CB 49           BIT     1,C                 ; 
29E6: 28 02           JR      Z,$29EA             ; {}
29E8: 06 44           LD      B,$44               ; 
29EA: DD 70 0E        LD      (IX+$0E),B          ; 
29ED: 06 00           LD      B,$00               ; 
29EF: 21 4A 2A        LD      HL,$2A4A            ; 
29F2: 09              ADD     HL,BC               ; 
29F3: 7E              LD      A,(HL)              ; 
29F4: 23              INC     HL                  ; 
29F5: DD 77 08        LD      (IX+$08),A          ; 
29F8: AF              XOR     A                   ; 
29F9: ED 6F           RLD                         ; 
29FB: 47              LD      B,A                 ; 
29FC: 7E              LD      A,(HL)              ; 
29FD: E6 1F           AND     $1F                 ; 
29FF: DD 77 09        LD      (IX+$09),A          ; 
2A02: 78              LD      A,B                 ; 
2A03: E6 0E           AND     $0E                 ; 
2A05: 47              LD      B,A                 ; 
2A06: 07              RLCA                        ; 
2A07: 80              ADD     A,B                 ; 
2A08: 21 7A 2A        LD      HL,$2A7A            ; 
2A0B: D7              RST     0X10                ; 
2A0C: CB 7A           BIT     7,D                 ; 
2A0E: 28 03           JR      Z,$2A13             ; {}
2A10: 23              INC     HL                  ; 
2A11: 23              INC     HL                  ; 
2A12: 23              INC     HL                  ; 
2A13: 7E              LD      A,(HL)              ; 
2A14: 23              INC     HL                  ; 
2A15: DD 77 01        LD      (IX+$01),A          ; 
2A18: 7E              LD      A,(HL)              ; 
2A19: 23              INC     HL                  ; 
2A1A: DD 77 03        LD      (IX+$03),A          ; 
2A1D: 7E              LD      A,(HL)              ; 
2A1E: 23              INC     HL                  ; 
2A1F: DD 77 05        LD      (IX+$05),A          ; 
2A22: AF              XOR     A                   ; 
2A23: DD 77 00        LD      (IX+$00),A          ; 
2A26: DD 77 02        LD      (IX+$02),A          ; 
2A29: DD 77 04        LD      (IX+$04),A          ; 
2A2C: 3C              INC     A                   ; 
2A2D: DD 77 0D        LD      (IX+$0D),A          ; 
2A30: B2              OR      D                   ; 
2A31: E6 81           AND     $81                 ; 
2A33: DD 77 13        LD      (IX+$13),A          ; 
2A36: C9              RET                         ; 

2A37: 3A 87 92        LD      A,($9287)           ; 
2A3A: A7              AND     A                   ; 
2A3B: C0              RET     NZ                  ; 
2A3C: 32 08 90        LD      ($9008),A           ; 
2A3F: 3C              INC     A                   ; 
2A40: 32 04 90        LD      ($9004),A           ; 
2A43: 32 10 90        LD      ($9010),A           ; 
2A46: 32 24 98        LD      ($9824),A           ; 
2A49: C9              RET                         ; 

2A4A: 1D              DEC     E                   ; #
2A4B: 00              NOP                         ; #
2A4C: 67              LD      H,A                 ; #
2A4D: 20 9F           JR      NZ,$29EE            ; {} #
2A4F: 40              LD      B,B                 ; #
2A50: D4 20 7B        CALL    NC,$7B20            ; #
2A53: 01 B0 61        LD      BC,$61B0            ; #
2A56: E8              RET     PE                  ; #
2A57: 01 F5 21        LD      BC,$21F5            ; #
2A5A: 0B              DEC     BC                  ; #
2A5B: 02              LD      (BC),A              ; #
2A5C: 1B              DEC     DE                  ; #
2A5D: 22 2B 82        LD      ($822B),HL          ; #
2A60: 41              LD      B,C                 ; #
2A61: 22 5D 82        LD      ($825D),HL          ; #
2A64: 79              LD      A,C                 ; #
2A65: 22 9E 02        LD      ($029E),HL          ; {} #
2A68: BA              CP      D                   ; #
2A69: 22 D9 02        LD      ($02D9),HL          ; {} #
2A6C: FB              EI                          ; #
2A6D: 22 1D 03        LD      ($031D),HL          ; {} #
2A70: 33              INC     SP                  ; #
2A71: 23              INC     HL                  ; #
2A72: DA 0F F0        JP      C,$F00F             ; #
2A75: 2F              CPL                         ; #
2A76: 2B              DEC     HL                  ; #
2A77: A2              AND     D                   ; #
2A78: 5D              LD      E,L                 ; #
2A79: A2              AND     D                   ; #
2A7A: 9B              SBC     E                   ; #
2A7B: 34              INC     (HL)                ; #
2A7C: 03              INC     BC                  ; #
2A7D: 9B              SBC     E                   ; #
2A7E: 44              LD      B,H                 ; #
2A7F: 03              INC     BC                  ; #
2A80: 23              INC     HL                  ; #
2A81: 00              NOP                         ; #
2A82: 00              NOP                         ; #
2A83: 23              INC     HL                  ; #
2A84: 78              LD      A,B                 ; #
2A85: 02              LD      (BC),A              ; #
2A86: 9B              SBC     E                   ; #
2A87: 2C              INC     L                   ; #
2A88: 03              INC     BC                  ; #
2A89: 9B              SBC     E                   ; #
2A8A: 4C              LD      C,H                 ; #
2A8B: 03              INC     BC                  ; #
2A8C: 2B              DEC     HL                  ; #
2A8D: 00              NOP                         ; #
2A8E: 00              NOP                         ; #
2A8F: 2B              DEC     HL                  ; #
2A90: 78              LD      A,B                 ; #
2A91: 02              LD      (BC),A              ; #
2A92: 9B              SBC     E                   ; #
2A93: 34              INC     (HL)                ; #
2A94: 03              INC     BC                  ; #
2A95: 9B              SBC     E                   ; #
2A96: 34              INC     (HL)                ; #
2A97: 03              INC     BC                  ; #
2A98: 9B              SBC     E                   ; #
2A99: 44              LD      B,H                 ; #
2A9A: 03              INC     BC                  ; #
2A9B: 9B              SBC     E                   ; #
2A9C: 44              LD      B,H                 ; #
2A9D: 03              INC     BC                  ; #

;======================================================================
; PLAY COMMAND 0A (?Explosion sequence for bee?)
;
2A9E: 3A A0 92        LD      A,($92A0)           ; 
2AA1: 3D              DEC     A                   ; 
2AA2: E6 03           AND     $03                 ; 
2AA4: C0              RET     NZ                  ; 
2AA5: 3A A7 92        LD      A,($92A7)           ; 
2AA8: 47              LD      B,A                 ; 
2AA9: 3A 08 90        LD      A,($9008)           ; 
2AAC: B0              OR      B                   ; 
2AAD: 28 48           JR      Z,$2AF7             ; {}
2AAF: 3A 0F 92        LD      A,($920F)           ; 
2AB2: A7              AND     A                   ; 
2AB3: 0E 01           LD      C,$01               ; 
2AB5: 28 02           JR      Z,$2AB9             ; {}
2AB7: 0D              DEC     C                   ; 
2AB8: 0D              DEC     C                   ; 
2AB9: 2E 00           LD      L,$00               ; 
2ABB: 06 0A           LD      B,$0A               ; 
2ABD: 26 99           LD      H,$99               ; 
2ABF: 7E              LD      A,(HL)              ; 
2AC0: 81              ADD     A,C                 ; 
2AC1: 77              LD      (HL),A              ; 
2AC2: 26 98           LD      H,$98               ; 
2AC4: 7E              LD      A,(HL)              ; 
2AC5: 81              ADD     A,C                 ; 
2AC6: 77              LD      (HL),A              ; 
2AC7: 2C              INC     L                   ; 
2AC8: 2C              INC     L                   ; 
2AC9: 10 F2           DJNZ    $2ABD               ; {}
2ACB: 3A 24 98        LD      A,($9824)           ; 
2ACE: A7              AND     A                   ; 
2ACF: 3A 00 99        LD      A,($9900)           ; 
2AD2: 28 03           JR      Z,$2AD7             ; {}
2AD4: A7              AND     A                   ; 
2AD5: 28 11           JR      Z,$2AE8             ; {}
2AD7: FE 20           CP      $20                 ; 
2AD9: 20 06           JR      NZ,$2AE1            ; {}
2ADB: 3E 01           LD      A,$01               ; 
2ADD: 32 0F 92        LD      ($920F),A           ; 
2AE0: C9              RET                         ; 
;
2AE1: D6 E0           SUB     $E0                 ; 
2AE3: C0              RET     NZ                  ; 
2AE4: 32 0F 92        LD      ($920F),A           ; 
2AE7: C9              RET                         ; 
;
2AE8: AF              XOR     A                   ; 
2AE9: 32 0F 92        LD      ($920F),A           ; 
2AEC: 32 0A 90        LD      ($900A),A           ; 
2AEF: 3C              INC     A                   ; 
2AF0: 32 A0 9A        LD      ($9AA0),A           ; 
2AF3: 32 09 90        LD      ($9009),A           ; 
2AF6: C9              RET                         ; 
;
2AF7: 32 0A 90        LD      ($900A),A           ; 
2AFA: C9              RET                         ; 



2AFB: FF FF FF FF FF

2B00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2B10: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2B20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2B30: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2B40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2B50: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2B60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2B70: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2B80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2B90: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2BA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2BB0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2BC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2BD0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2BE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2BF0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

;======================================================================
;
2C00: 3A 21 98        LD      A,($9821)           ; 
2C03: FE 1B           CP      $1B                 ; 
2C05: 38 04           JR      C,$2C0B             ; {}
2C07: D6 04           SUB     $04                 ; 
2C09: 18 F8           JR      $2C03               ; {}
2C0B: 3D              DEC     A                   ; 
2C0C: 6F              LD      L,A                 ; 
2C0D: 07              RLCA                        ; 
2C0E: 07              RLCA                        ; 
2C0F: 85              ADD     A,L                 ; 
2C10: 5F              LD      E,A                 ; 
2C11: 3A 84 99        LD      A,($9984)           ; 
2C14: 21 65 2C        LD      HL,$2C65            ; 
2C17: CF              RST     0X08                ; 
2C18: 7E              LD      A,(HL)              ; 
2C19: 23              INC     HL                  ; 
2C1A: 66              LD      H,(HL)              ; 
2C1B: 6F              LD      L,A                 ; 
2C1C: 7B              LD      A,E                 ; 
2C1D: D7              RST     0X10                ; 
2C1E: 11 C0 99        LD      DE,$99C0            ; 
2C21: 06 05           LD      B,$05               ; 
2C23: 7E              LD      A,(HL)              ; 
2C24: 4F              LD      C,A                 ; 
2C25: 07              RLCA                        ; 
2C26: 07              RLCA                        ; 
2C27: 07              RLCA                        ; 
2C28: 07              RLCA                        ; 
2C29: E6 0F           AND     $0F                 ; 
2C2B: 12              LD      (DE),A              ; 
2C2C: 1C              INC     E                   ; 
2C2D: 79              LD      A,C                 ; 
2C2E: E6 0F           AND     $0F                 ; 
2C30: 12              LD      (DE),A              ; 
2C31: 1C              INC     E                   ; 
2C32: 23              INC     HL                  ; 
2C33: 10 EE           DJNZ    $2C23               ; {}
2C35: 3A 21 98        LD      A,($9821)           ; 
2C38: FE 03           CP      $03                 ; 
2C3A: 30 03           JR      NC,$2C3F            ; {}
2C3C: AF              XOR     A                   ; 
2C3D: 18 07           JR      $2C46               ; {}
2C3F: F6 FC           OR      $FC                 ; 
2C41: 3C              INC     A                   ; 
2C42: 28 02           JR      Z,$2C46             ; {}
2C44: 3E 0A           LD      A,$0A               ; 
2C46: 12              LD      (DE),A              ; 
2C47: 01 16 02        LD      BC,$0216            ; 
2C4A: ED 43 C1 92     LD      ($92C1),BC          ; 
2C4E: ED 43 C0 92     LD      ($92C0),BC          ; 
2C52: 3A 21 98        LD      A,($9821)           ; 
2C55: FE 10           CP      $10                 ; 
2C57: 38 02           JR      C,$2C5B             ; {}
2C59: 3E 10           LD      A,$10               ; 
2C5B: 07              RLCA                        ; 
2C5C: 07              RLCA                        ; 
2C5D: E6 70           AND     $70                 ; 
2C5F: C6 40           ADD     $40                 ; 
2C61: 32 BB 99        LD      ($99BB),A           ; 
2C64: C9              RET                         ; 

;======================================================================
;
2C65: EF              RST     0X28                ; #
2C66: 2C              INC     L                   ; #
2C67: 71              LD      (HL),C              ; #
2C68: 2D              DEC     L                   ; #
2C69: F3              DI                          ; #
2C6A: 2D              DEC     L                   ; #
2C6B: 6D              LD      L,L                 ; #
2C6C: 2C              INC     L                   ; #
2C6D: 00              NOP                         ; #
2C6E: 00              NOP                         ; #
2C6F: 22 C6 00        LD      ($00C6),HL          ; {} #
2C72: 00              NOP                         ; #
2C73: 11 23 C7        LD      DE,$C723            ; #
2C76: 00              NOP                         ; #
2C77: 00              NOP                         ; #
2C78: 00              NOP                         ; #
2C79: 00              NOP                         ; #
2C7A: C0              RET     NZ                  ; #
2C7B: 00              NOP                         ; #
2C7C: 11 12 23        LD      DE,$2312            ; #
2C7F: 97              SUB     A                   ; #
2C80: 00              NOP                         ; #
2C81: 11 23 23        LD      DE,$2323            ; #
2C84: 98              SBC     B                   ; #
2C85: 00              NOP                         ; #
2C86: 21 24 33        LD      HL,$3324            ; #
2C89: 98              SBC     B                   ; #
2C8A: 00              NOP                         ; #
2C8B: 00              NOP                         ; #
2C8C: 00              NOP                         ; #
2C8D: 00              NOP                         ; #
2C8E: 90              SUB     B                   ; #
2C8F: 00              NOP                         ; #
2C90: 22 25 33        LD      ($3325),HL          ; {} #
2C93: 99              SBC     C                   ; #
2C94: 10 22           DJNZ    $2CB8               ; {} #
2C96: 36 34           LD      (HL),$34            ; #
2C98: 69              LD      L,C                 ; #
2C99: 10 10           DJNZ    $2CAB               ; {} #
2C9B: 11 23 97        LD      DE,$9723            ; #
2C9E: 00              NOP                         ; #
2C9F: 00              NOP                         ; #
2CA0: 00              NOP                         ; #
2CA1: 00              NOP                         ; #
2CA2: 60              LD      H,B                 ; #
2CA3: 00              NOP                         ; #
2CA4: 32 46 34        LD      ($3446),A           ; {} #
2CA7: 67              LD      H,A                 ; #
2CA8: 11 32 67        LD      DE,$6732            ; #
2CAB: 44              LD      B,H                 ; #
2CAC: 68              LD      L,B                 ; #
2CAD: 11 32 67        LD      DE,$6732            ; #
2CB0: 45              LD      B,L                 ; #
2CB1: 68              LD      L,B                 ; #
2CB2: 11 00 00        LD      DE,$0000            ; #
2CB5: 00              NOP                         ; #
2CB6: 60              LD      H,B                 ; #
2CB7: 00              NOP                         ; #
2CB8: 42              LD      B,D                 ; #
2CB9: 78              LD      A,B                 ; #
2CBA: 45              LD      B,L                 ; #
2CBB: 69              LD      L,C                 ; #
2CBC: 11 42 78        LD      DE,$7842            ; #
2CBF: 45              LD      B,L                 ; #
2CC0: 69              LD      L,C                 ; #
2CC1: 11 11 22        LD      DE,$2211            ; #
2CC4: 23              INC     HL                  ; #
2CC5: 97              SUB     A                   ; #
2CC6: 11 00 00        LD      DE,$0000            ; #
2CC9: 00              NOP                         ; #
2CCA: 60              LD      H,B                 ; #
2CCB: 00              NOP                         ; #
2CCC: 52              LD      D,D                 ; #
2CCD: 88              ADC     A,B                 ; #
2CCE: 46              LD      B,(HL)              ; #
2CCF: 3A 11 52        LD      A,($5211)           ; #
2CD2: 88              ADC     A,B                 ; #
2CD3: 56              LD      D,(HL)              ; #
2CD4: 3A 11 52        LD      A,($5211)           ; #
2CD7: 88              ADC     A,B                 ; #
2CD8: 56              LD      D,(HL)              ; #
2CD9: 3C              INC     A                   ; #
2CDA: 11 00 00        LD      DE,$0000            ; #
2CDD: 00              NOP                         ; #
2CDE: 30 00           JR      NC,$2CE0            ; {} #
2CE0: 62              LD      H,D                 ; #
2CE1: 89              ADC     A,C                 ; #
2CE2: 57              LD      D,A                 ; #
2CE3: 3C              INC     A                   ; #
2CE4: 11 62 99        LD      DE,$9962            ; #
2CE7: 57              LD      D,A                 ; #
2CE8: 3C              INC     A                   ; #
2CE9: 11 62 99        LD      DE,$9962            ; #
2CEC: 57              LD      D,A                 ; #
2CED: 3C              INC     A                   ; #
2CEE: 11 00 00        LD      DE,$0000            ; #
2CF1: 12              LD      (DE),A              ; #
2CF2: C6 00           ADD     $00                 ; #
2CF4: 00              NOP                         ; #
2CF5: 11 22 C6        LD      DE,$C622            ; #
2CF8: 00              NOP                         ; #
2CF9: 00              NOP                         ; #
2CFA: 00              NOP                         ; #
2CFB: 00              NOP                         ; #
2CFC: C0              RET     NZ                  ; #
2CFD: 00              NOP                         ; #
2CFE: 11 12 23        LD      DE,$2312            ; #
2D01: 97              SUB     A                   ; #
2D02: 00              NOP                         ; #
2D03: 11 12 23        LD      DE,$2312            ; #
2D06: 97              SUB     A                   ; #
2D07: 00              NOP                         ; #
2D08: 00              NOP                         ; #
2D09: 11 23 C7        LD      DE,$C723            ; #
2D0C: 00              NOP                         ; #
2D0D: 00              NOP                         ; #
2D0E: 00              NOP                         ; #
2D0F: 00              NOP                         ; #
2D10: 90              SUB     B                   ; #
2D11: 00              NOP                         ; #
2D12: 21 23 33        LD      HL,$3323            ; #
2D15: 98              SBC     B                   ; #
2D16: 10 21           DJNZ    $2D39               ; {} #
2D18: 24              INC     H                   ; #
2D19: 33              INC     SP                  ; #
2D1A: 98              SBC     B                   ; #
2D1B: 10 21           DJNZ    $2D3E               ; {} #
2D1D: 25              DEC     H                   ; #
2D1E: 34              INC     (HL)                ; #
2D1F: 98              SBC     B                   ; #
2D20: 10 00           DJNZ    $2D22               ; {} #
2D22: 00              NOP                         ; #
2D23: 00              NOP                         ; #
2D24: 60              LD      H,B                 ; #
2D25: 00              NOP                         ; #
2D26: 22 25 34        LD      ($3425),HL          ; {} #
2D29: 68              LD      L,B                 ; #
2D2A: 11 32 36        LD      DE,$3632            ; #
2D2D: 44              LD      B,H                 ; #
2D2E: 68              LD      L,B                 ; #
2D2F: 11 11 11        LD      DE,$1111            ; #
2D32: 23              INC     HL                  ; #
2D33: 67              LD      H,A                 ; #
2D34: 01 00 00        LD      BC,$0000            ; #
2D37: 00              NOP                         ; #
2D38: 60              LD      H,B                 ; #
2D39: 00              NOP                         ; #
2D3A: 32 36 45        LD      ($4536),A           ; #
2D3D: 68              LD      L,B                 ; #
2D3E: 11 32 46        LD      DE,$4632            ; #
2D41: 45              LD      B,L                 ; #
2D42: 69              LD      L,C                 ; #
2D43: 11 32 67        LD      DE,$6732            ; #
2D46: 45              LD      B,L                 ; #
2D47: 69              LD      L,C                 ; #
2D48: 11 00 00        LD      DE,$0000            ; #
2D4B: 00              NOP                         ; #
2D4C: 60              LD      H,B                 ; #
2D4D: 00              NOP                         ; #
2D4E: 42              LD      B,D                 ; #
2D4F: 67              LD      H,A                 ; #
2D50: 46              LD      B,(HL)              ; #
2D51: 3A 11 42        LD      A,($4211)           ; #
2D54: 78              LD      A,B                 ; #
2D55: 56              LD      D,(HL)              ; #
2D56: 3A 11 52        LD      A,($5211)           ; #
2D59: 78              LD      A,B                 ; #
2D5A: 56              LD      D,(HL)              ; #
2D5B: 3A 11 00        LD      A,($0011)           ; {} #
2D5E: 00              NOP                         ; #
2D5F: 00              NOP                         ; #
2D60: 30 00           JR      NC,$2D62            ; {} #
2D62: 52              LD      D,D                 ; #
2D63: 88              ADC     A,B                 ; #
2D64: 56              LD      D,(HL)              ; #
2D65: 3C              INC     A                   ; #
2D66: 11 62 99        LD      DE,$9962            ; #
2D69: 57              LD      D,A                 ; #
2D6A: 3C              INC     A                   ; #
2D6B: 11 62 99        LD      DE,$9962            ; #
2D6E: 57              LD      D,A                 ; #
2D6F: 3C              INC     A                   ; #
2D70: 11 00 00        LD      DE,$0000            ; #
2D73: 23              INC     HL                  ; #
2D74: C6 00           ADD     $00                 ; #
2D76: 10 11           DJNZ    $2D89               ; {} #
2D78: 23              INC     HL                  ; #
2D79: 97              SUB     A                   ; #
2D7A: 00              NOP                         ; #
2D7B: 00              NOP                         ; #
2D7C: 00              NOP                         ; #
2D7D: 00              NOP                         ; #
2D7E: C0              RET     NZ                  ; #
2D7F: 00              NOP                         ; #
2D80: 11 12 33        LD      DE,$3312            ; #
2D83: 98              SBC     B                   ; #
2D84: 00              NOP                         ; #
2D85: 21 23 34        LD      HL,$3423            ; #
2D88: 68              LD      L,B                 ; #
2D89: 00              NOP                         ; #
2D8A: 21 24 34        LD      HL,$3424            ; #
2D8D: 68              LD      L,B                 ; #
2D8E: 00              NOP                         ; #
2D8F: 00              NOP                         ; #
2D90: 00              NOP                         ; #
2D91: 00              NOP                         ; #
2D92: 90              SUB     B                   ; #
2D93: 00              NOP                         ; #
2D94: 32 36 34        LD      ($3436),A           ; {} #
2D97: 67              LD      H,A                 ; #
2D98: 10 32           DJNZ    $2DCC               ; {} #
2D9A: 46              LD      B,(HL)              ; #
2D9B: 44              LD      B,H                 ; #
2D9C: 68              LD      L,B                 ; #
2D9D: 10 11           DJNZ    $2DB0               ; {} #
2D9F: 11 23 97        LD      DE,$9723            ; #
2DA2: 10 00           DJNZ    $2DA4               ; {} #
2DA4: 00              NOP                         ; #
2DA5: 00              NOP                         ; #
2DA6: 60              LD      H,B                 ; #
2DA7: 00              NOP                         ; #
2DA8: 42              LD      B,D                 ; #
2DA9: 67              LD      H,A                 ; #
2DAA: 45              LD      B,L                 ; #
2DAB: 68              LD      L,B                 ; #
2DAC: 11 42 67        LD      DE,$6742            ; #
2DAF: 45              LD      B,L                 ; #
2DB0: 69              LD      L,C                 ; #
2DB1: 11 42 78        LD      DE,$7842            ; #
2DB4: 46              LD      B,(HL)              ; #
2DB5: 69              LD      L,C                 ; #
2DB6: 11 00 00        LD      DE,$0000            ; #
2DB9: 00              NOP                         ; #
2DBA: 60              LD      H,B                 ; #
2DBB: 00              NOP                         ; #
2DBC: 52              LD      D,D                 ; #
2DBD: 78              LD      A,B                 ; #
2DBE: 46              LD      B,(HL)              ; #
2DBF: 3A 11 52        LD      A,($5211)           ; #
2DC2: 88              ADC     A,B                 ; #
2DC3: 56              LD      D,(HL)              ; #
2DC4: 3A 11 52        LD      A,($5211)           ; #
2DC7: 88              ADC     A,B                 ; #
2DC8: 56              LD      D,(HL)              ; #
2DC9: 3A 11 00        LD      A,($0011)           ; {} #
2DCC: 00              NOP                         ; #
2DCD: 00              NOP                         ; #
2DCE: 60              LD      H,B                 ; #
2DCF: 00              NOP                         ; #
2DD0: 62              LD      H,D                 ; #
2DD1: 88              ADC     A,B                 ; #
2DD2: 56              LD      D,(HL)              ; #
2DD3: 3C              INC     A                   ; #
2DD4: 11 62 89        LD      DE,$8962            ; #
2DD7: 57              LD      D,A                 ; #
2DD8: 3C              INC     A                   ; #
2DD9: 11 62 89        LD      DE,$8962            ; #
2DDC: 57              LD      D,A                 ; #
2DDD: 3E 11           LD      A,$11               ; #
2DDF: 00              NOP                         ; #
2DE0: 00              NOP                         ; #
2DE1: 00              NOP                         ; #
2DE2: 30 00           JR      NC,$2DE4            ; {} #
2DE4: 72              LD      (HL),D              ; #
2DE5: 99              SBC     C                   ; #
2DE6: 57              LD      D,A                 ; #
2DE7: 3E 11           LD      A,$11               ; #
2DE9: 72              LD      (HL),D              ; #
2DEA: 99              SBC     C                   ; #
2DEB: 68              LD      L,B                 ; #
2DEC: 3E 11           LD      A,$11               ; #
2DEE: 72              LD      (HL),D              ; #
2DEF: 99              SBC     C                   ; #
2DF0: 68              LD      L,B                 ; #
2DF1: 3E 11           LD      A,$11               ; #
2DF3: 00              NOP                         ; #
2DF4: 00              NOP                         ; #
2DF5: 23              INC     HL                  ; #
2DF6: C6 00           ADD     $00                 ; #
2DF8: 10 11           DJNZ    $2E0B               ; {} #
2DFA: 23              INC     HL                  ; #
2DFB: 97              SUB     A                   ; #
2DFC: 00              NOP                         ; #
2DFD: 00              NOP                         ; #
2DFE: 00              NOP                         ; #
2DFF: 00              NOP                         ; #
2E00: C0              RET     NZ                  ; #
2E01: 00              NOP                         ; #
2E02: 11 12 34        LD      DE,$3412            ; #
2E05: 98              SBC     B                   ; #
2E06: 00              NOP                         ; #
2E07: 21 23 34        LD      HL,$3423            ; #
2E0A: 68              LD      L,B                 ; #
2E0B: 00              NOP                         ; #
2E0C: 21 24 34        LD      HL,$3424            ; #
2E0F: 68              LD      L,B                 ; #
2E10: 00              NOP                         ; #
2E11: 00              NOP                         ; #
2E12: 00              NOP                         ; #
2E13: 00              NOP                         ; #
2E14: 90              SUB     B                   ; #
2E15: 00              NOP                         ; #
2E16: 32 36 45        LD      ($4536),A           ; #
2E19: 67              LD      H,A                 ; #
2E1A: 11 32 46        LD      DE,$4632            ; #
2E1D: 46              LD      B,(HL)              ; #
2E1E: 68              LD      L,B                 ; #
2E1F: 11 32 56        LD      DE,$5632            ; #
2E22: 46              LD      B,(HL)              ; #
2E23: 69              LD      L,C                 ; #
2E24: 11 00 00        LD      DE,$0000            ; #
2E27: 00              NOP                         ; #
2E28: 60              LD      H,B                 ; #
2E29: 00              NOP                         ; #
2E2A: 42              LD      B,D                 ; #
2E2B: 67              LD      H,A                 ; #
2E2C: 56              LD      D,(HL)              ; #
2E2D: 6A              LD      L,D                 ; #
2E2E: 11 42 67        LD      DE,$6742            ; #
2E31: 56              LD      D,(HL)              ; #
2E32: 6A              LD      L,D                 ; #
2E33: 11 42 78        LD      DE,$7842            ; #
2E36: 57              LD      D,A                 ; #
2E37: 6A              LD      L,D                 ; #
2E38: 11 00 00        LD      DE,$0000            ; #
2E3B: 00              NOP                         ; #
2E3C: 60              LD      H,B                 ; #
2E3D: 00              NOP                         ; #
2E3E: 52              LD      D,D                 ; #
2E3F: 78              LD      A,B                 ; #
2E40: 57              LD      D,A                 ; #
2E41: 3A 11 52        LD      A,($5211)           ; #
2E44: 88              ADC     A,B                 ; #
2E45: 57              LD      D,A                 ; #
2E46: 3A 11 52        LD      A,($5211)           ; #
2E49: 88              ADC     A,B                 ; #
2E4A: 68              LD      L,B                 ; #
2E4B: 3C              INC     A                   ; #
2E4C: 11 00 00        LD      DE,$0000            ; #
2E4F: 00              NOP                         ; #
2E50: 60              LD      H,B                 ; #
2E51: 00              NOP                         ; #
2E52: 62              LD      H,D                 ; #
2E53: 88              ADC     A,B                 ; #
2E54: 68              LD      L,B                 ; #
2E55: 3C              INC     A                   ; #
2E56: 11 62 89        LD      DE,$8962            ; #
2E59: 68              LD      L,B                 ; #
2E5A: 3C              INC     A                   ; #
2E5B: 11 62 89        LD      DE,$8962            ; #
2E5E: 68              LD      L,B                 ; #
2E5F: 3E 11           LD      A,$11               ; #
2E61: 00              NOP                         ; #
2E62: 00              NOP                         ; #
2E63: 00              NOP                         ; #
2E64: 30 00           JR      NC,$2E66            ; {} #
2E66: 72              LD      (HL),D              ; #
2E67: 99              SBC     C                   ; #
2E68: 68              LD      L,B                 ; #
2E69: 3E 11           LD      A,$11               ; #
2E6B: 72              LD      (HL),D              ; #
2E6C: 99              SBC     C                   ; #
2E6D: 68              LD      L,B                 ; #
2E6E: 3E 11           LD      A,$11               ; #
2E70: 72              LD      (HL),D              ; #
2E71: 99              SBC     C                   ; #
2E72: 68              LD      L,B                 ; #
2E73: 3E 11           LD      A,$11               ; #

2E75: FF FF FF FF FF FF FF FF FF FF FF
2E80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2E90: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2EA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2EB0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2EC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2ED0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2EE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2EF0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

2F00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2F10: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2F20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2F30: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2F40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2F50: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2F60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2F70: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2F80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2F90: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2FA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2FB0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2FC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2FD0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2FE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
2FF0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 

2FFF: 50              LD      D,B                 ; 

;======================================================================
;
3000: 21 FD 83        LD      HL,$83FD            ; 
3003: 3A 40 98        LD      A,($9840)           ; 
3006: A7              AND     A                   ; 
3007: 28 03           JR      Z,$300C             ; {}
3009: 21 E8 83        LD      HL,$83E8            ; 
300C: 22 00 8A        LD      ($8A00),HL          ; 
300F: 11 3D 8A        LD      DE,$8A3D            ; 
3012: CD F7 31        CALL    $31F7               ; {}
3015: D0              RET     NC                  ; 
3016: 11 37 8A        LD      DE,$8A37            ; 
3019: CD F7 31        CALL    $31F7               ; {}
301C: 3E 05           LD      A,$05               ; 
301E: 30 27           JR      NC,$3047            ; {}
3020: 11 31 8A        LD      DE,$8A31            ; 
3023: CD F7 31        CALL    $31F7               ; {}
3026: 3E 04           LD      A,$04               ; 
3028: 30 1D           JR      NC,$3047            ; {}
302A: 11 2B 8A        LD      DE,$8A2B            ; 
302D: CD F7 31        CALL    $31F7               ; {}
3030: 3E 03           LD      A,$03               ; 
3032: 30 13           JR      NC,$3047            ; {}
3034: 11 25 8A        LD      DE,$8A25            ; 
3037: CD F7 31        CALL    $31F7               ; {}
303A: 3E 02           LD      A,$02               ; 
303C: 30 09           JR      NC,$3047            ; {}
303E: 3E FF           LD      A,$FF               ; 
3040: 32 AC 9A        LD      ($9AAC),A           ; 
3043: 3E 01           LD      A,$01               ; 
3045: 18 03           JR      $304A               ; {}
3047: 32 B0 9A        LD      ($9AB0),A           ; 
304A: 32 11 8A        LD      ($8A11),A           ; 
304D: 21 A6 31        LD      HL,$31A6            ; 
3050: 3D              DEC     A                   ; 
3051: CF              RST     0X08                ; 
3052: CD 18 31        CALL    $3118               ; {}
3055: 3A 11 8A        LD      A,($8A11)           ; 
3058: 21 A1 31        LD      HL,$31A1            ; 
305B: 3D              DEC     A                   ; 
305C: D7              RST     0X10                ; 
305D: 7E              LD      A,(HL)              ; 
305E: 21 49 8A        LD      HL,$8A49            ; 
3061: 11 4C 8A        LD      DE,$8A4C            ; 
3064: A7              AND     A                   ; 
3065: 28 05           JR      Z,$306C             ; {}
3067: 4F              LD      C,A                 ; 
3068: 06 00           LD      B,$00               ; 
306A: ED B8           LDDR                        ; 
306C: 06 03           LD      B,$03               ; 
306E: 3E 24           LD      A,$24               ; 
3070: 22 04 8A        LD      ($8A04),HL          ; 
3073: 2C              INC     L                   ; 
3074: 77              LD      (HL),A              ; 
3075: 10 FC           DJNZ    $3073               ; {}
3077: 3E 49           LD      A,$49               ; 
3079: 32 10 8A        LD      ($8A10),A           ; 
307C: 21 7F 32        LD      HL,$327F            ; 
307F: CD 28 33        CALL    $3328               ; {}
3082: CD 1B 33        CALL    $331B               ; {}
3085: CD 28 33        CALL    $3328               ; {}
3088: 11 09 83        LD      DE,$8309            ; 
308B: 2A 00 8A        LD      HL,($8A00)          ; 
308E: CD 75 32        CALL    $3275               ; {}
3091: 21 49 81        LD      HL,$8149            ; 
3094: 11 E0 FF        LD      DE,$FFE0            ; 
3097: 36 0A           LD      (HL),$0A            ; 
3099: 19              ADD     HL,DE               ; 
309A: 36 0A           LD      (HL),$0A            ; 
309C: 19              ADD     HL,DE               ; 
309D: 36 0A           LD      (HL),$0A            ; 
309F: CD 1D 32        CALL    $321D               ; {}
30A2: CD 80 31        CALL    $3180               ; {}
30A5: 3E 04           LD      A,$04               ; 
30A7: 32 AE 92        LD      ($92AE),A           ; 
30AA: 3A AE 92        LD      A,($92AE)           ; 
30AD: A7              AND     A                   ; 
30AE: 20 FA           JR      NZ,$30AA            ; {}
30B0: 3E 28           LD      A,$28               ; 
30B2: 32 AE 92        LD      ($92AE),A           ; 
30B5: CD 1D 32        CALL    $321D               ; {}
30B8: CD 80 31        CALL    $3180               ; {}
30BB: 3A A0 92        LD      A,($92A0)           ; 
30BE: 4F              LD      C,A                 ; 
30BF: CD ED 32        CALL    $32ED               ; {}
30C2: 3A A0 92        LD      A,($92A0)           ; 
30C5: B9              CP      C                   ; 
30C6: 28 F7           JR      Z,$30BF             ; {}
30C8: 4F              LD      C,A                 ; 
30C9: E6 0F           AND     $0F                 ; 
30CB: CC 41 31        CALL    Z,$3141             ; {}
30CE: 21 B6 99        LD      HL,$99B6            ; 
30D1: 3A 15 92        LD      A,($9215)           ; 
30D4: A7              AND     A                   ; 
30D5: 28 01           JR      Z,$30D8             ; {}
30D7: 23              INC     HL                  ; 
30D8: CB 66           BIT     4,(HL)              ; 
30DA: CA 4C 31        JP      Z,$314C             ; {}
30DD: 7E              LD      A,(HL)              ; 
30DE: E6 0A           AND     $0A                 ; 
30E0: 21 02 8A        LD      HL,$8A02            ; 
30E3: 11 03 8A        LD      DE,$8A03            ; 
30E6: BE              CP      (HL)                ; 
30E7: 28 04           JR      Z,$30ED             ; {}
30E9: 77              LD      (HL),A              ; 
30EA: 3E FD           LD      A,$FD               ; 
30EC: 12              LD      (DE),A              ; 
30ED: 1A              LD      A,(DE)              ; 
30EE: 3C              INC     A                   ; 
30EF: 12              LD      (DE),A              ; 
30F0: E6 0F           AND     $0F                 ; 
30F2: 20 CB           JR      NZ,$30BF            ; {}
30F4: 7E              LD      A,(HL)              ; 
30F5: FE 08           CP      $08                 ; 
30F7: 28 24           JR      Z,$311D             ; {}
30F9: FE 02           CP      $02                 ; 
30FB: 20 C2           JR      NZ,$30BF            ; {}
30FD: 3E 28           LD      A,$28               ; 
30FF: 32 AE 92        LD      ($92AE),A           ; 
3102: 3A 10 8A        LD      A,($8A10)           ; 
3105: 6F              LD      L,A                 ; 
3106: 26 81           LD      H,$81               ; 
3108: 7E              LD      A,(HL)              ; 
3109: 3D              DEC     A                   ; 
310A: FE 09           CP      $09                 ; 
310C: CC 38 31        CALL    Z,$3138             ; {}
310F: FE 29           CP      $29                 ; 
3111: CC 3B 31        CALL    Z,$313B             ; {}
3114: 77              LD      (HL),A              ; 
3115: C3 BF 30        JP      $30BF               ; {}
3118: 7E              LD      A,(HL)              ; 
3119: 23              INC     HL                  ; 
311A: 66              LD      H,(HL)              ; 
311B: 6F              LD      L,A                 ; 
311C: E9              JP      (HL)                ; 
311D: 3A 10 8A        LD      A,($8A10)           ; 
3120: 6F              LD      L,A                 ; 
3121: 26 81           LD      H,$81               ; 
3123: 3E 28           LD      A,$28               ; 
3125: 32 AE 92        LD      ($92AE),A           ; 
3128: 7E              LD      A,(HL)              ; 
3129: 3C              INC     A                   ; 
312A: FE 2B           CP      $2B                 ; 
312C: CC 3E 31        CALL    Z,$313E             ; {}
312F: FE 25           CP      $25                 ; 
3131: CC 38 31        CALL    Z,$3138             ; {}
3134: 77              LD      (HL),A              ; 
3135: C3 BF 30        JP      $30BF               ; {}

3138: 3E 2A           LD      A,$2A               ; 
313A: C9              RET                         ; 

313B: 3E 24           LD      A,$24               ; 
313D: C9              RET                         ; 

313E: 3E 0A           LD      A,$0A               ; 
3140: C9              RET                         ; 

3141: 3A 10 8A        LD      A,($8A10)           ; 
3144: 6F              LD      L,A                 ; 
3145: 26 85           LD      H,$85               ; 
3147: 7E              LD      A,(HL)              ; 
3148: EE 05           XOR     $05                 ; 
314A: 77              LD      (HL),A              ; 
314B: C9              RET                         ; 

314C: 3A 10 8A        LD      A,($8A10)           ; 
314F: 6F              LD      L,A                 ; 
3150: 26 85           LD      H,$85               ; 
3152: 36 00           LD      (HL),$00            ; 
3154: 26 81           LD      H,$81               ; 
3156: 4E              LD      C,(HL)              ; 
3157: 3E 28           LD      A,$28               ; 
3159: 32 AE 92        LD      ($92AE),A           ; 
315C: 2A 04 8A        LD      HL,($8A04)          ; 
315F: 23              INC     HL                  ; 
3160: 71              LD      (HL),C              ; 
3161: 22 04 8A        LD      ($8A04),HL          ; 
3164: 21 10 8A        LD      HL,$8A10            ; 
3167: 7E              LD      A,(HL)              ; 
3168: D6 20           SUB     $20                 ; 
316A: 77              LD      (HL),A              ; 
316B: D2 B5 30        JP      NC,$30B5            ; {}
316E: CD 1D 32        CALL    $321D               ; {}
3171: CD 80 31        CALL    $3180               ; {}
3174: 3E 4C           LD      A,$4C               ; 
3176: 32 A0 92        LD      ($92A0),A           ; 
3179: 3A A0 92        LD      A,($92A0)           ; 
317C: A7              AND     A                   ; 
317D: 20 FA           JR      NZ,$3179            ; {}
317F: C9              RET                         ; 
3180: 3A 11 8A        LD      A,($8A11)           ; 
3183: 21 97 31        LD      HL,$3197            ; 
3186: 3D              DEC     A                   ; 
3187: CF              RST     0X08                ; 
3188: 7E              LD      A,(HL)              ; 
3189: 23              INC     HL                  ; 
318A: 66              LD      H,(HL)              ; 
318B: 6F              LD      L,A                 ; 
318C: 06 16           LD      B,$16               ; 
318E: 11 E0 FF        LD      DE,$FFE0            ; 
3191: 36 05           LD      (HL),$05            ; 
3193: 19              ADD     HL,DE               ; 
3194: 10 FB           DJNZ    $3191               ; {}
3196: C9              RET                         ; 
3197: 74              LD      (HL),H              ; 
3198: 87              ADD     A,A                 ; 
3199: 76              HALT                        ; 
319A: 87              ADD     A,A                 ; 
319B: 78              LD      A,B                 ; 
319C: 87              ADD     A,A                 ; 
319D: 7A              LD      A,D                 ; 
319E: 87              ADD     A,A                 ; 
319F: 7C              LD      A,H                 ; 
31A0: 87              ADD     A,A                 ; 
31A1: 0C              INC     C                   ; 
31A2: 09              ADD     HL,BC               ; 
31A3: 06 03           LD      B,$03               ; 
31A5: 00              NOP                         ; 
31A6: B0              OR      B                   ; 
31A7: 31 B4 31        LD      SP,$31B4            ; 
31AA: B8              CP      B                   ; 
31AB: 31 CE 31        LD      SP,$31CE            ; 
31AE: D9              EXX                         ; 
31AF: 31 3E 12        LD      SP,$123E            ; 
31B2: 18 06           JR      $31BA               ; {}
31B4: 3E 0C           LD      A,$0C               ; 
31B6: 18 02           JR      $31BA               ; {}
31B8: 3E 06           LD      A,$06               ; 
31BA: 21 37 8A        LD      HL,$8A37            ; 
31BD: 11 3D 8A        LD      DE,$8A3D            ; 
31C0: 01 06 00        LD      BC,$0006            ; 
31C3: ED B8           LDDR                        ; 
31C5: 11 37 8A        LD      DE,$8A37            ; 
31C8: 4F              LD      C,A                 ; 
31C9: ED B8           LDDR                        ; 
31CB: C3 D9 31        JP      $31D9               ; {}
31CE: 11 3D 8A        LD      DE,$8A3D            ; 
31D1: 21 37 8A        LD      HL,$8A37            ; 
31D4: 01 06 00        LD      BC,$0006            ; 
31D7: ED B8           LDDR                        ; 
31D9: 3A 11 8A        LD      A,($8A11)           ; 
31DC: 3D              DEC     A                   ; 
31DD: 21 ED 31        LD      HL,$31ED            ; 
31E0: CF              RST     0X08                ; 
31E1: 5E              LD      E,(HL)              ; 
31E2: 23              INC     HL                  ; 
31E3: 56              LD      D,(HL)              ; 
31E4: 2A 00 8A        LD      HL,($8A00)          ; 
31E7: 01 06 00        LD      BC,$0006            ; 
31EA: ED B8           LDDR                        ; 
31EC: C9              RET                         ; 
31ED: 25              DEC     H                   ; 
31EE: 8A              ADC     A,D                 ; 
31EF: 2B              DEC     HL                  ; 
31F0: 8A              ADC     A,D                 ; 
31F1: 31 8A 37        LD      SP,$378A            ; 
31F4: 8A              ADC     A,D                 ; 
31F5: 3D              DEC     A                   ; 
31F6: 8A              ADC     A,D                 ; 
31F7: 2A 00 8A        LD      HL,($8A00)          ; 
31FA: 06 06           LD      B,$06               ; 
31FC: 1A              LD      A,(DE)              ; 
31FD: FE 24           CP      $24                 ; 
31FF: 28 0D           JR      Z,$320E             ; {}
3201: 7E              LD      A,(HL)              ; 
3202: FE 24           CP      $24                 ; 
3204: C8              RET     Z                   ; 
3205: 1A              LD      A,(DE)              ; 
3206: BE              CP      (HL)                ; 
3207: C0              RET     NZ                  ; 
3208: 2D              DEC     L                   ; 
3209: 1D              DEC     E                   ; 
320A: 10 F0           DJNZ    $31FC               ; {}
320C: AF              XOR     A                   ; 
320D: C9              RET                         ; 
320E: BE              CP      (HL)                ; 
320F: 28 F7           JR      Z,$3208             ; {}
3211: AF              XOR     A                   ; 
3212: 18 F2           JR      $3206               ; {}
3214: 21 45 33        LD      HL,$3345            ; 
3217: CD 28 33        CALL    $3328               ; {}
321A: CD 28 33        CALL    $3328               ; {}
321D: 21 B4 32        LD      HL,$32B4            ; 
3220: CD 1B 33        CALL    $331B               ; {}
3223: 06 01           LD      B,$01               ; 
3225: CD 31 32        CALL    $3231               ; {}
3228: CD 31 32        CALL    $3231               ; {}
322B: CD 31 32        CALL    $3231               ; {}
322E: CD 31 32        CALL    $3231               ; {}
3231: 78              LD      A,B                 ; 
3232: 3D              DEC     A                   ; 
3233: 87              ADD     A,A                 ; 
3234: 87              ADD     A,A                 ; 
3235: 87              ADD     A,A                 ; 
3236: 21 C5 32        LD      HL,$32C5            ; 
3239: D7              RST     0X10                ; 
323A: 5E              LD      E,(HL)              ; 
323B: 23              INC     HL                  ; 
323C: 56              LD      D,(HL)              ; 
323D: 23              INC     HL                  ; 
323E: 78              LD      A,B                 ; 
323F: 12              LD      (DE),A              ; 
3240: CD 73 32        CALL    $3273               ; {}
3243: CD 70 32        CALL    $3270               ; {}
3246: CD 70 32        CALL    $3270               ; {}
3249: CD 73 32        CALL    $3273               ; {}
324C: CD 73 32        CALL    $3273               ; {}
324F: 7E              LD      A,(HL)              ; 
3250: 23              INC     HL                  ; 
3251: 4E              LD      C,(HL)              ; 
3252: 23              INC     HL                  ; 
3253: E5              PUSH    HL                  ; 
3254: 61              LD      H,C                 ; 
3255: 6F              LD      L,A                 ; 
3256: CD 75 32        CALL    $3275               ; {}
3259: 7B              LD      A,E                 ; 
325A: D6 C0           SUB     $C0                 ; 
325C: 5F              LD      E,A                 ; 
325D: 30 01           JR      NC,$3260            ; {}
325F: 15              DEC     D                   ; 
3260: E1              POP     HL                  ; 
3261: 7E              LD      A,(HL)              ; 
3262: 23              INC     HL                  ; 
3263: 66              LD      H,(HL)              ; 
3264: 6F              LD      L,A                 ; 
3265: CD 70 32        CALL    $3270               ; {}
3268: CD 70 32        CALL    $3270               ; {}
326B: CD 70 32        CALL    $3270               ; {}
326E: 04              INC     B                   ; 
326F: C9              RET                         ; 
3270: 7E              LD      A,(HL)              ; 
3271: 12              LD      (DE),A              ; 
3272: 23              INC     HL                  ; 
3273: E7              RST     0X20                ; 
3274: C9              RET                         ; 

3275: 0E 06           LD      C,$06               ; 
3277: 7E              LD      A,(HL)              ; 
3278: 12              LD      (DE),A              ; 
3279: 2B              DEC     HL                  ; 
327A: E7              RST     0X20                ; 
327B: 0D              DEC     C                   ; 
327C: 20 F9           JR      NZ,$3277            ; {}
327E: C9              RET                         ; 

327F: 24              INC     H                   ; #
3280: 83              ADD     A,E                 ; #
3281: 15              DEC     D                   ; #
3282: 04              INC     B                   ; #
3283: 0E 17           LD      C,$17               ; #
3285: 1D              DEC     E                   ; #
3286: 0E 1B           LD      C,$1B               ; #
3288: 24              INC     H                   ; #
3289: 22 18 1E        LD      ($1E18),HL          ; {} #
328C: 1B              DEC     DE                  ; #
328D: 24              INC     H                   ; #
328E: 12              LD      (DE),A              ; #
328F: 17              RLA                         ; #
3290: 12              LD      (DE),A              ; #
3291: 1D              DEC     E                   ; #
3292: 12              LD      (DE),A              ; #
3293: 0A              LD      A,(BC)              ; #
3294: 15              DEC     D                   ; #
3295: 1C              INC     E                   ; #
3296: 24              INC     H                   ; #
3297: 2C              INC     L                   ; #
3298: E7              RST     0X20                ; #
3299: 82              ADD     A,D                 ; #
329A: 10 1C           DJNZ    $32B8               ; {} #
329C: 0C              INC     C                   ; #
329D: 18 1B           JR      $32BA               ; {} #
329F: 0E 24           LD      C,$24               ; #
32A1: 24              INC     H                   ; #
32A2: 24              INC     H                   ; #
32A3: 24              INC     H                   ; #
32A4: 24              INC     H                   ; #
32A5: 24              INC     H                   ; #
32A6: 24              INC     H                   ; #
32A7: 17              RLA                         ; #
32A8: 0A              LD      A,(BC)              ; #
32A9: 16 0E           LD      D,$0E               ; #
32AB: 50              LD      D,B                 ; #
32AC: 82              ADD     A,D                 ; #
32AD: 05              DEC     B                   ; #
32AE: 04              INC     B                   ; #
32AF: 1D              DEC     E                   ; #
32B0: 18 19           JR      $32CB               ; {} #
32B2: 24              INC     H                   ; #
32B3: 05              DEC     B                   ; #
32B4: 92              SUB     D                   ; #
32B5: 82              ADD     A,D                 ; #
32B6: 0E 1C           LD      C,$1C               ; #
32B8: 0C              INC     C                   ; #
32B9: 18 1B           JR      $32D6               ; {} #
32BB: 0E 24           LD      C,$24               ; #
32BD: 24              INC     H                   ; #
32BE: 24              INC     H                   ; #
32BF: 24              INC     H                   ; #
32C0: 24              INC     H                   ; #
32C1: 17              RLA                         ; #
32C2: 0A              LD      A,(BC)              ; #
32C3: 16 0E           LD      D,$0E               ; #
32C5: 54              LD      D,H                 ; #
32C6: 83              ADD     A,E                 ; #
32C7: 1C              INC     E                   ; #
32C8: 1D              DEC     E                   ; #
32C9: 25              DEC     H                   ; #
32CA: 8A              ADC     A,D                 ; #
32CB: 3E 8A           LD      A,$8A               ; #
32CD: 56              LD      D,(HL)              ; #
32CE: 83              ADD     A,E                 ; #
32CF: 17              RLA                         ; #
32D0: 0D              DEC     C                   ; #
32D1: 2B              DEC     HL                  ; #
32D2: 8A              ADC     A,D                 ; #
32D3: 41              LD      B,C                 ; #
32D4: 8A              ADC     A,D                 ; #
32D5: 58              LD      E,B                 ; #
32D6: 83              ADD     A,E                 ; #
32D7: 1B              DEC     DE                  ; #
32D8: 0D              DEC     C                   ; #
32D9: 31 8A 44        LD      SP,$448A            ; #
32DC: 8A              ADC     A,D                 ; #
32DD: 5A              LD      E,D                 ; #
32DE: 83              ADD     A,E                 ; #
32DF: 1D              DEC     E                   ; #

32E0: 11 37 8A        LD      DE,$8A37            ; 
32E3: 47              LD      B,A                 ; 
32E4: 8A              ADC     A,D                 ; 
32E5: 5C              LD      E,H                 ; 
32E6: 83              ADD     A,E                 ; 
32E7: 1D              DEC     E                   ; 
32E8: 11 3D 8A        LD      DE,$8A3D            ; 
32EB: 4A              LD      C,D                 ; 
32EC: 8A              ADC     A,D                 ; 
32ED: 3A B5 99        LD      A,($99B5)           ; 
32F0: FE A0           CP      $A0                 ; 
32F2: 28 07           JR      Z,$32FB             ; {}
32F4: 47              LD      B,A                 ; 
32F5: 3A B8 99        LD      A,($99B8)           ; 
32F8: B8              CP      B                   ; 
32F9: 38 05           JR      C,$3300             ; {}
32FB: 3A AE 92        LD      A,($92AE)           ; 
32FE: A7              AND     A                   ; 
32FF: C0              RET     NZ                  ; 
3300: E1              POP     HL                  ; 
3301: 26 81           LD      H,$81               ; 
3303: 3A 10 8A        LD      A,($8A10)           ; 
3306: 6F              LD      L,A                 ; 
3307: ED 5B 04 8A     LD      DE,($8A04)          ; 
330B: 13              INC     DE                  ; 
330C: ED A0           LDI                         ; 
330E: 3E DF           LD      A,$DF               ; 
3310: 25              DEC     H                   ; 
3311: 85              ADD     A,L                 ; 
3312: 30 01           JR      NC,$3315            ; {}
3314: 24              INC     H                   ; 
3315: 6F              LD      L,A                 ; 
3316: CB 44           BIT     0,H                 ; 
3318: 20 F2           JR      NZ,$330C            ; {}
331A: C9              RET                         ; 

; Display message on screen.
; HL points to descriptor as follows:
; LSB,MSB of screen
; Length of message
; Message bytes
331B: 5E              LD      E,(HL)              ; LSB of screen start
331C: 23              INC     HL                  ; .
331D: 56              LD      D,(HL)              ; MSB of screen start
331E: 23              INC     HL                  ; .
331F: 46              LD      B,(HL)              ; Message length
3320: 23              INC     HL                  ; .
3321: 7E              LD      A,(HL)              ; Get byte
3322: 12              LD      (DE),A              ; To screen
3323: 23              INC     HL                  ; Next in buffer
3324: E7              RST     0X20                ; (DE=DE-20) Next on screen
3325: 10 FA           DJNZ    $3321               ; {} Do all
3327: C9              RET                         ; Done

; Message going down? No ...
3328: 5E              LD      E,(HL)              ; 
3329: 23              INC     HL                  ; 
332A: 56              LD      D,(HL)              ; 
332B: 23              INC     HL                  ; 
332C: 46              LD      B,(HL)              ; 
332D: 23              INC     HL                  ; 
332E: 4E              LD      C,(HL)              ; 
332F: 23              INC     HL                  ; 
3330: EB              EX      DE,HL               ; 
3331: 1A              LD      A,(DE)              ; From the buffer ...
3332: 77              LD      (HL),A              ; ... to the screen
3333: CB D4           SET     2,H                 ; 
3335: 71              LD      (HL),C              ; 
3336: CB 94           RES     2,H                 ; 
3338: 13              INC     DE                  ; 
3339: 3E E0           LD      A,$E0               ; 
333B: 25              DEC     H                   ; 
333C: 85              ADD     A,L                 ; 
333D: 30 01           JR      NC,$3340            ; {}
333F: 24              INC     H                   ; 
3340: 6F              LD      L,A                 ; 
3341: 10 EE           DJNZ    $3331               ; {}
3343: EB              EX      DE,HL               ; 
3344: C9              RET                         ; 

3345: 25              DEC     H                   ; #
3346: 83              ADD     A,E                 ; #
3347: 13              INC     DE                  ; #
3348: 02              LD      (BC),A              ; #
3349: 1D              DEC     E                   ; #
334A: 11 0E 24        LD      DE,$240E            ; #
334D: 10 0A           DJNZ    $3359               ; {} #
334F: 15              DEC     D                   ; #
3350: 0A              LD      A,(BC)              ; #
3351: 0C              INC     C                   ; #
3352: 1D              DEC     E                   ; #
3353: 12              LD      (DE),A              ; #
3354: 0C              INC     C                   ; #
3355: 24              INC     H                   ; #
3356: 11 0E 1B        LD      DE,$1B0E            ; #
3359: 18 0E           JR      $3369               ; {} #
335B: 1C              INC     E                   ; #
335C: CC 82 0C        CALL    Z,$0C82             ; {} #
335F: 04              INC     B                   ; #
3360: 26 26           LD      H,$26               ; #
3362: 24              INC     H                   ; #
3363: 0B              DEC     BC                  ; #
3364: 0E 1C           LD      C,$1C               ; #
3366: 1D              DEC     E                   ; #
3367: 24              INC     H                   ; #
3368: 05              DEC     B                   ; #
3369: 24              INC     H                   ; #
336A: 26 26           LD      H,$26               ; #

; Initialization comes here
336C: AF              XOR     A                   ; Zero
336D: 32 23 68        LD      ($6823),A           ; Halt CPUs 2 and 3
3370: 3C              INC     A                   ; Enable ...
3371: 32 22 68        LD      ($6822),A           ; ... NMI CPU 3
3374: F3              DI                          ; Disable local interrupt handling
3375: 32 30 68        LD      ($6830),A           ; Watchdog reset
3378: 06 0A           LD      B,$0A               ; 
337A: D9              EXX                         ; 
337B: 11 00 80        LD      DE,$8000            ; 
337E: 21 00 00        LD      HL,$0000            ; 
3381: 01 00 04        LD      BC,$0400            ; 
3384: 7D              LD      A,L                 ; 
3385: AC              XOR     H                   ; 
3386: 2F              CPL                         ; 
3387: 87              ADD     A,A                 ; 
3388: 87              ADD     A,A                 ; 
3389: ED 6A           ADC     HL,HL               ; 
338B: 7D              LD      A,L                 ; 
338C: 32 30 68        LD      ($6830),A           ; Watchdog reset
338F: 12              LD      (DE),A              ; 
3390: 13              INC     DE                  ; 
3391: 0B              DEC     BC                  ; 
3392: 78              LD      A,B                 ; 
3393: B1              OR      C                   ; 
3394: 20 EE           JR      NZ,$3384            ; {}
3396: 11 00 80        LD      DE,$8000            ; 
3399: 21 00 00        LD      HL,$0000            ; 
339C: 01 00 04        LD      BC,$0400            ; 
339F: 7D              LD      A,L                 ; 
33A0: AC              XOR     H                   ; 
33A1: 2F              CPL                         ; 
33A2: 87              ADD     A,A                 ; 
33A3: 87              ADD     A,A                 ; 
33A4: ED 6A           ADC     HL,HL               ; 
33A6: 1A              LD      A,(DE)              ; 
33A7: AD              XOR     L                   ; 
33A8: C2 C0 34        JP      NZ,$34C0            ; {}
33AB: 13              INC     DE                  ; 
33AC: 32 30 68        LD      ($6830),A           ; Watchdog
33AF: 0B              DEC     BC                  ; 
33B0: 78              LD      A,B                 ; 
33B1: B1              OR      C                   ; 
33B2: 20 EB           JR      NZ,$339F            ; {}
33B4: 11 00 80        LD      DE,$8000            ; 
33B7: 21 55 55        LD      HL,$5555            ; 
33BA: 01 00 04        LD      BC,$0400            ; 
33BD: 7D              LD      A,L                 ; 
33BE: AC              XOR     H                   ; 
33BF: 2F              CPL                         ; 
33C0: 87              ADD     A,A                 ; 
33C1: 87              ADD     A,A                 ; 
33C2: ED 6A           ADC     HL,HL               ; 
33C4: 7D              LD      A,L                 ; 
33C5: 32 30 68        LD      ($6830),A           ; Watchdog
33C8: 12              LD      (DE),A              ; 
33C9: 13              INC     DE                  ; 
33CA: 0B              DEC     BC                  ; 
33CB: 78              LD      A,B                 ; 
33CC: B1              OR      C                   ; 
33CD: 20 EE           JR      NZ,$33BD            ; {}
33CF: 11 00 80        LD      DE,$8000            ; 
33D2: 21 55 55        LD      HL,$5555            ; 
33D5: 01 00 04        LD      BC,$0400            ; 
33D8: 7D              LD      A,L                 ; 
33D9: AC              XOR     H                   ; 
33DA: 2F              CPL                         ; 
33DB: 87              ADD     A,A                 ; 
33DC: 87              ADD     A,A                 ; 
33DD: ED 6A           ADC     HL,HL               ; 
33DF: 1A              LD      A,(DE)              ; 
33E0: AD              XOR     L                   ; 
33E1: C2 C0 34        JP      NZ,$34C0            ; {}
33E4: 13              INC     DE                  ; 
33E5: 32 30 68        LD      ($6830),A           ; Watchdog
33E8: 0B              DEC     BC                  ; 
33E9: 78              LD      A,B                 ; 
33EA: B1              OR      C                   ; 
33EB: 20 EB           JR      NZ,$33D8            ; {}
33ED: 11 00 80        LD      DE,$8000            ; 
33F0: 21 AA AA        LD      HL,$AAAA            ; 
33F3: 01 00 04        LD      BC,$0400            ; 
33F6: 7D              LD      A,L                 ; 
33F7: AC              XOR     H                   ; 
33F8: 2F              CPL                         ; 
33F9: 87              ADD     A,A                 ; 
33FA: 87              ADD     A,A                 ; 
33FB: ED 6A           ADC     HL,HL               ; 
33FD: 7D              LD      A,L                 ; 
33FE: 32 30 68        LD      ($6830),A           ; Watchdog
3401: 12              LD      (DE),A              ; 
3402: 13              INC     DE                  ; 
3403: 0B              DEC     BC                  ; 
3404: 78              LD      A,B                 ; 
3405: B1              OR      C                   ; 
3406: 20 EE           JR      NZ,$33F6            ; {}
3408: 11 00 80        LD      DE,$8000            ; 
340B: 21 AA AA        LD      HL,$AAAA            ; 
340E: 01 00 04        LD      BC,$0400            ; 
3411: 7D              LD      A,L                 ; 
3412: AC              XOR     H                   ; 
3413: 2F              CPL                         ; 
3414: 87              ADD     A,A                 ; 
3415: 87              ADD     A,A                 ; 
3416: ED 6A           ADC     HL,HL               ; 
3418: 1A              LD      A,(DE)              ; 
3419: AD              XOR     L                   ; 
341A: C2 C0 34        JP      NZ,$34C0            ; {}
341D: 13              INC     DE                  ; 
341E: 32 30 68        LD      ($6830),A           ; Watchdog
3421: 0B              DEC     BC                  ; 
3422: 78              LD      A,B                 ; 
3423: B1              OR      C                   ; 
3424: 20 EB           JR      NZ,$3411            ; {}
3426: D9              EXX                         ; 
3427: 05              DEC     B                   ; 
3428: C2 7A 33        JP      NZ,$337A            ; {}
342B: 31 00 84        LD      SP,$8400            ; 
342E: 11 00 84        LD      DE,$8400            ; 
3431: CD 7F 34        CALL    $347F               ; {}
3434: 11 00 88        LD      DE,$8800            ; 
3437: CD 7F 34        CALL    $347F               ; {}
343A: 11 00 90        LD      DE,$9000            ; 
343D: CD 7F 34        CALL    $347F               ; {}
3440: 21 E0 99        LD      HL,$99E0            ; 
3443: 11 00 90        LD      DE,$9000            ; 
3446: 01 20 00        LD      BC,$0020            ; 
3449: ED B0           LDIR                        ; 
344B: 11 00 98        LD      DE,$9800            ; 
344E: CD 7F 34        CALL    $347F               ; {}
3451: 21 00 90        LD      HL,$9000            ; 
3454: 11 E0 99        LD      DE,$99E0            ; 
3457: 01 20 00        LD      BC,$0020            ; 
345A: ED B0           LDIR                        ; 
345C: 31 00 8B        LD      SP,$8B00            ; 
345F: 11 00 80        LD      DE,$8000            ; Start of RAM
3462: CD 7F 34        CALL    $347F               ; {}
3465: CD 58 39        CALL    $3958               ; {} Set RAM and screen
3468: 21 81 3B        LD      HL,$3B81            ; RAM Report message
346B: CD 1B 33        CALL    $331B               ; {} Print RAM report
346E: 32 30 68        LD      ($6830),A           ; Watchdog
3471: CD 3C 3A        CALL    $3A3C               ; {}
3474: 3E 07           LD      A,$07               ; 
3476: 32 20 90        LD      ($9020),A           ; 
3479: CD 72 39        CALL    $3972               ; {}
347C: C3 50 35        JP      $3550               ; {} Continue with ROM checks
347F: 06 1E           LD      B,$1E               ; 
3481: 21 00 00        LD      HL,$0000            ; 
3484: C5              PUSH    BC                  ; 
3485: CD 8C 34        CALL    $348C               ; {}
3488: C1              POP     BC                  ; 
3489: 10 F9           DJNZ    $3484               ; {}
348B: C9              RET                         ; 

348C: D5              PUSH    DE                  ; 
348D: E5              PUSH    HL                  ; 
348E: 01 00 04        LD      BC,$0400            ; 
3491: 7D              LD      A,L                 ; 
3492: AC              XOR     H                   ; 
3493: 2F              CPL                         ; 
3494: 87              ADD     A,A                 ; 
3495: 87              ADD     A,A                 ; 
3496: ED 6A           ADC     HL,HL               ; 
3498: 7D              LD      A,L                 ; 
3499: 32 30 68        LD      ($6830),A           ; Watchdog
349C: 12              LD      (DE),A              ; 
349D: 13              INC     DE                  ; 
349E: 0B              DEC     BC                  ; 
349F: 78              LD      A,B                 ; 
34A0: B1              OR      C                   ; 
34A1: 20 EE           JR      NZ,$3491            ; {}
34A3: E1              POP     HL                  ; 
34A4: D1              POP     DE                  ; 
34A5: D5              PUSH    DE                  ; 
34A6: 01 00 04        LD      BC,$0400            ; 
34A9: 7D              LD      A,L                 ; 
34AA: AC              XOR     H                   ; 
34AB: 2F              CPL                         ; 
34AC: 87              ADD     A,A                 ; 
34AD: 87              ADD     A,A                 ; 
34AE: ED 6A           ADC     HL,HL               ; 
34B0: 1A              LD      A,(DE)              ; 
34B1: AD              XOR     L                   ; 
34B2: C2 C0 34        JP      NZ,$34C0            ; {}
34B5: 13              INC     DE                  ; 
34B6: 32 30 68        LD      ($6830),A           ; Watchdog
34B9: 0B              DEC     BC                  ; 
34BA: 78              LD      A,B                 ; 
34BB: B1              OR      C                   ; 
34BC: 20 EB           JR      NZ,$34A9            ; {}
34BE: D1              POP     DE                  ; 
34BF: C9              RET                         ; 
34C0: 47              LD      B,A                 ; 
34C1: 7A              LD      A,D                 ; 
34C2: 1F              RRA                         ; 
34C3: 1F              RRA                         ; 
34C4: E6 07           AND     $07                 ; 
34C6: FE 04           CP      $04                 ; 
34C8: 38 01           JR      C,$34CB             ; {}
34CA: 3D              DEC     A                   ; 
34CB: FE 05           CP      $05                 ; 
34CD: 38 01           JR      C,$34D0             ; {}
34CF: 3D              DEC     A                   ; 
34D0: 5F              LD      E,A                 ; 
34D1: 78              LD      A,B                 ; 
34D2: 16 15           LD      D,$15               ; 
34D4: E6 0F           AND     $0F                 ; 
34D6: 20 02           JR      NZ,$34DA            ; {}
34D8: 16 11           LD      D,$11               ; 
34DA: 32 30 68        LD      ($6830),A           ; Watchdog
34DD: D9              EXX                         ; 
34DE: 21 00 80        LD      HL,$8000            ; 
34E1: 11 01 80        LD      DE,$8001            ; 
34E4: 01 00 04        LD      BC,$0400            ; 
34E7: 36 24           LD      (HL),$24            ; 
34E9: ED B0           LDIR                        ; 
34EB: 36 00           LD      (HL),$00            ; 
34ED: 01 FF 03        LD      BC,$03FF            ; 
34F0: ED B0           LDIR                        ; 
34F2: 32 30 68        LD      ($6830),A           ; 
34F5: D9              EXX                         ; 
34F6: 21 E2 82        LD      HL,$82E2            ; 
34F9: 36 1B           LD      (HL),$1B            ; 
34FB: 3E E0           LD      A,$E0               ; 
34FD: 25              DEC     H                   ; 
34FE: D7              RST     0X10                ; 
34FF: 36 0A           LD      (HL),$0A            ; 
3501: 3E E0           LD      A,$E0               ; 
3503: 25              DEC     H                   ; 
3504: D7              RST     0X10                ; 
3505: 36 16           LD      (HL),$16            ; 
3507: 3E A0           LD      A,$A0               ; 
3509: 25              DEC     H                   ; 
350A: D7              RST     0X10                ; 
350B: 73              LD      (HL),E              ; 
350C: 3E E0           LD      A,$E0               ; 
350E: 25              DEC     H                   ; 
350F: D7              RST     0X10                ; 
3510: 72              LD      (HL),D              ; 
3511: 21 80 93        LD      HL,$9380            ; 
3514: 06 80           LD      B,$80               ; 
3516: 36 F1           LD      (HL),$F1            ; 
3518: 23              INC     HL                  ; 
3519: 10 FB           DJNZ    $3516               ; {}
351B: 32 30 68        LD      ($6830),A           ; Infinte ...
351E: C3 1B 35        JP      $351B               ; {} ... loop

3521: E5              PUSH    HL                  ; 
3522: EB              EX      DE,HL               ; 
3523: 16 10           LD      D,$10               ; 
3525: AF              XOR     A                   ; 
3526: 47              LD      B,A                 ; 
3527: 86              ADD     A,(HL)              ; 
3528: 32 30 68        LD      ($6830),A           ; Watchdog
352B: 23              INC     HL                  ; 
352C: 10 F9           DJNZ    $3527               ; {}
352E: 15              DEC     D                   ; 
352F: 20 F6           JR      NZ,$3527            ; {}
3531: EB              EX      DE,HL               ; 
3532: E1              POP     HL                  ; 
3533: B9              CP      C                   ; 
3534: C8              RET     Z                   ; 

; Display ROM error report
3535: 21 8B 3B        LD      HL,$3B8B            ; "ROM  OK"
3538: CD 1B 33        CALL    $331B               ; {} Print message
353B: 11 44 82        LD      DE,$8244            ; Screen Location for error code
353E: 21 02 91        LD      HL,$9102            ; Get error code
3541: AF              XOR     A                   ; 0 to start
3542: ED 6F           RLD                         ; Rotate BCD first digit into A
3544: 12              LD      (DE),A              ; Store the first code
3545: E7              RST     0X20                ; Next spot
3546: AF              XOR     A                   ; 0 to start
3547: ED 6F           RLD                         ; Rotate BSC second digit into A
3549: 12              LD      (DE),A              ; Store to screen
354A: 32 30 68        LD      ($6830),A           ; Watchdog
354D: C3 4A 35        JP      $354A               ; {} Infinite loop if ROMs are wrong

; Make sure all ROMs are OK
3550: 21 00 91        LD      HL,$9100            ; Start CPU2 ...
3553: 36 00           LD      (HL),$00            ; ... checksum
3555: 23              INC     HL                  ; Start CPU3 ...
3556: 36 00           LD      (HL),$00            ; ... checksum
3558: 23              INC     HL                  ; 9102 = ...
3559: 36 01           LD      (HL),$01            ; ... 01
355B: AF              XOR     A                   ; 
355C: 32 70 92        LD      ($9270),A           ; 
355F: 3C              INC     A                   ; 
3560: 32 23 68        LD      ($6823),A           ; Watchdog
3563: 11 00 00        LD      DE,$0000            ; ROM area ...
3566: 0E 00           LD      C,$00               ; 
3568: CD 21 35        CALL    $3521               ; {} Checksum ROM 1
356B: 34              INC     (HL)                ; 
356C: 0E 00           LD      C,$00               ; 
356E: CD 21 35        CALL    $3521               ; {} Checksum ROM 2
3571: 34              INC     (HL)                ; 
3572: 0E 00           LD      C,$00               ; 
3574: CD 21 35        CALL    $3521               ; {} Checksum ROM 3
3577: 34              INC     (HL)                ; 
3578: 0E 00           LD      C,$00               ; 
357A: CD 21 35        CALL    $3521               ; {} Checksum ROM 4
357D: 36 FF           LD      (HL),$FF            ; 
357F: 3A 00 91        LD      A,($9100)           ; CPU2 ROMs
3582: 32 30 68        LD      ($6830),A           ; Watchdog reset
3585: A7              AND     A                   ; Wait ...
3586: 28 F7           JR      Z,$357F             ; {} ... For CPU 2
3588: 3C              INC     A                   ; OK?
3589: 28 07           JR      Z,$3592             ; {} Yes ... move on to CPU3
358B: 3D              DEC     A                   ; Restore error
358C: 32 02 91        LD      ($9102),A           ; Save error code
358F: C3 35 35        JP      $3535               ; {} Print ROM/RAM report
3592: 3A 01 91        LD      A,($9101)           ; CPU3 ROMs
3595: 32 30 68        LD      ($6830),A           ; Watchdog reset
3598: A7              AND     A                   ; Wait ...
3599: 28 F7           JR      Z,$3592             ; {} ... For CPU 3
359B: 3C              INC     A                   ; OK?
359C: 28 17           JR      Z,$35B5             ; {} Yes ... continue
359E: 3D              DEC     A                   ; Restore error
359F: 32 02 91        LD      ($9102),A           ; Save error code
35A2: C3 35 35        JP      $3535               ; {} Print ROM/RAM report

; Looks like data
35A5: 05              DEC     B                   ; #
35A6: 05              DEC     B                   ; #
35A7: 05              DEC     B                   ; #
35A8: 05              DEC     B                   ; #
35A9: 30 40           JR      NC,$35EB            ; {} #
35AB: 00              NOP                         ; #
35AC: 02              LD      (BC),A              ; #
35AD: DF              RST     0X18                ; #
35AE: 40              LD      B,B                 ; #
35AF: 30 30           JR      NC,$35E1            ; {} #
35B1: 03              INC     BC                  ; #
35B2: DF              RST     0X18                ; #
35B3: 10 20           DJNZ    $35D5               ; {} #

35B5: 21 8B 3B        LD      HL,$3B8B            ; Print some report
35B8: CD 1B 33        CALL    $331B               ; {}
35BB: CD F4 37        CALL    $37F4               ; {}
35BE: 21 00 91        LD      HL,$9100            ; Acknowledge ...
35C1: 06 03           LD      B,$03               ; ... slave ...
35C3: 36 00           LD      (HL),$00            ; ... checksum ...
35C5: 23              INC     HL                  ; ...
35C6: 10 FB           DJNZ    $35C3               ; {} ... Reports
35C8: 3E 20           LD      A,$20               ; 
35CA: 32 00 90        LD      ($9000),A           ; 
35CD: 21 A5 35        LD      HL,$35A5            ; 
35D0: 11 00 70        LD      DE,$7000            ; 
35D3: 01 04 00        LD      BC,$0004            ; 
35D6: D9              EXX                         ; 
35D7: 3E A1           LD      A,$A1               ; What command?
35D9: 32 00 71        LD      ($7100),A           ; Custom IO
35DC: 32 30 68        LD      ($6830),A           ; Watchdog
35DF: CD EC 37        CALL    $37EC               ; {}
35E2: AF              XOR     A                   ; 
35E3: 32 30 68        LD      ($6830),A           ; Watchdog
35E6: 32 A0 92        LD      ($92A0),A           ; 
35E9: 3A A0 92        LD      A,($92A0)           ; 
35EC: FE 02           CP      $02                 ; 
35EE: 20 F9           JR      NZ,$35E9            ; {}
35F0: 21 A9 35        LD      HL,$35A9            ; 
35F3: 11 00 70        LD      DE,$7000            ; 
35F6: 01 0C 00        LD      BC,$000C            ; 
35F9: D9              EXX                         ; 
35FA: 3E A8           LD      A,$A8               ; IO Command
35FC: 32 00 71        LD      ($7100),A           ; 
35FF: 32 30 68        LD      ($6830),A           ; 
3602: CD EC 37        CALL    $37EC               ; {}
3605: 32 30 68        LD      ($6830),A           ; 
3608: ED 56           IM      1                   ; 
360A: 21 20 68        LD      HL,$6820            ; 
360D: 36 00           LD      (HL),$00            ; 
360F: 36 01           LD      (HL),$01            ; 
3611: FB              EI                          ; 
3612: CD F2 39        CALL    $39F2               ; {}
3615: AF              XOR     A                   ; 
3616: 32 A0 92        LD      ($92A0),A           ; 
3619: 3A A0 92        LD      A,($92A0)           ; 
361C: E6 08           AND     $08                 ; 
361E: 28 F9           JR      Z,$3619             ; {}
3620: 3A A0 92        LD      A,($92A0)           ; 
3623: 4F              LD      C,A                 ; 
3624: 3A A0 92        LD      A,($92A0)           ; 
3627: B9              CP      C                   ; 
3628: 28 FA           JR      Z,$3624             ; {}
362A: 21 16 91        LD      HL,$9116            ; 
362D: 11 17 91        LD      DE,$9117            ; 
3630: 01 07 00        LD      BC,$0007            ; 
3633: ED B8           LDDR                        ; 
3635: EB              EX      DE,HL               ; 
3636: 11 B5 99        LD      DE,$99B5            ; 
3639: 1A              LD      A,(DE)              ; 
363A: CB 7F           BIT     7,A                 ; 
363C: C2 BA 36        JP      NZ,$36BA            ; {}
363F: 77              LD      (HL),A              ; 
3640: 23              INC     HL                  ; 
3641: B6              OR      (HL)                ; 
3642: 23              INC     HL                  ; 
3643: 2F              CPL                         ; 
3644: A6              AND     (HL)                ; 
3645: 23              INC     HL                  ; 
3646: A6              AND     (HL)                ; 
3647: 77              LD      (HL),A              ; 
3648: 47              LD      B,A                 ; 
3649: 23              INC     HL                  ; 
364A: 13              INC     DE                  ; 
364B: 1A              LD      A,(DE)              ; 
364C: 77              LD      (HL),A              ; 
364D: 23              INC     HL                  ; 
364E: B6              OR      (HL)                ; 
364F: 23              INC     HL                  ; 
3650: 2F              CPL                         ; 
3651: A6              AND     (HL)                ; 
3652: 23              INC     HL                  ; 
3653: A6              AND     (HL)                ; 
3654: 77              LD      (HL),A              ; 
3655: 6F              LD      L,A                 ; 
3656: 60              LD      H,B                 ; 
3657: 06 10           LD      B,$10               ; 
3659: 29              ADD     HL,HL               ; 
365A: DC D6 39        CALL    C,$39D6             ; {}
365D: 10 FA           DJNZ    $3659               ; {}
365F: CD F4 37        CALL    $37F4               ; {}
3662: 2A 72 92        LD      HL,($9272)          ; 
3665: 7C              LD      A,H                 ; 
3666: B5              OR      L                   ; 
3667: 28 09           JR      Z,$3672             ; {}
3669: 2B              DEC     HL                  ; 
366A: 22 72 92        LD      ($9272),HL          ; 
366D: 7C              LD      A,H                 ; 
366E: B5              OR      L                   ; 
366F: CC BB 39        CALL    Z,$39BB             ; {}
3672: 3A 10 91        LD      A,($9110)           ; 
3675: 1F              RRA                         ; 
3676: 30 07           JR      NC,$367F            ; {}
3678: AF              XOR     A                   ; 
3679: 32 71 92        LD      ($9271),A           ; 
367C: C3 20 36        JP      $3620               ; {}
367F: 3A 17 91        LD      A,($9117)           ; 
3682: E6 0F           AND     $0F                 ; 
3684: CA 20 36        JP      Z,$3620             ; {}
3687: 4F              LD      C,A                 ; 
3688: 21 82 37        LD      HL,$3782            ; 
368B: 11 71 92        LD      DE,$9271            ; 
368E: 1A              LD      A,(DE)              ; 
368F: D7              RST     0X10                ; 
3690: 7E              LD      A,(HL)              ; 
3691: B9              CP      C                   ; 
3692: 28 05           JR      Z,$3699             ; {}
3694: AF              XOR     A                   ; 
3695: 12              LD      (DE),A              ; 
3696: C3 20 36        JP      $3620               ; {}
3699: EB              EX      DE,HL               ; 
369A: 34              INC     (HL)                ; 
369B: 13              INC     DE                  ; 
369C: 1A              LD      A,(DE)              ; 
369D: 3C              INC     A                   ; 
369E: C2 20 36        JP      NZ,$3620            ; {}
36A1: CD 58 39        CALL    $3958               ; {}
36A4: CD 72 39        CALL    $3972               ; {}
36A7: 11 98 37        LD      DE,$3798            ; 
36AA: 21 42 80        LD      HL,$8042            ; 
36AD: 06 1C           LD      B,$1C               ; 
36AF: CD 66 37        CALL    $3766               ; {}
36B2: 10 FB           DJNZ    $36AF               ; {}
36B4: 3A B5 99        LD      A,($99B5)           ; 
36B7: 87              ADD     A,A                 ; 
36B8: 30 FA           JR      NC,$36B4            ; {}
36BA: AF              XOR     A                   ; 
36BB: 32 A0 92        LD      ($92A0),A           ; 
36BE: 3A A0 92        LD      A,($92A0)           ; 
36C1: FE 08           CP      $08                 ; 
36C3: 38 F9           JR      C,$36BE             ; {}
36C5: 3A B5 99        LD      A,($99B5)           ; 
36C8: 87              ADD     A,A                 ; 
36C9: D2 20 36        JP      NC,$3620            ; {}
36CC: CD 72 39        CALL    $3972               ; {}
36CF: 21 00 80        LD      HL,$8000            ; 
36D2: 06 10           LD      B,$10               ; 
36D4: 36 28           LD      (HL),$28            ; 
36D6: 23              INC     HL                  ; 
36D7: 36 27           LD      (HL),$27            ; 
36D9: 23              INC     HL                  ; 
36DA: 10 F8           DJNZ    $36D4               ; {}
36DC: 06 10           LD      B,$10               ; 
36DE: 36 2D           LD      (HL),$2D            ; 
36E0: 23              INC     HL                  ; 
36E1: 36 2B           LD      (HL),$2B            ; 
36E3: 23              INC     HL                  ; 
36E4: 10 F8           DJNZ    $36DE               ; {}
36E6: 06 10           LD      B,$10               ; 
36E8: 36 28           LD      (HL),$28            ; 
36EA: 23              INC     HL                  ; 
36EB: 36 2D           LD      (HL),$2D            ; 
36ED: 23              INC     HL                  ; 
36EE: 10 F8           DJNZ    $36E8               ; {}
36F0: 06 10           LD      B,$10               ; 
36F2: 36 27           LD      (HL),$27            ; 
36F4: 23              INC     HL                  ; 
36F5: 36 2B           LD      (HL),$2B            ; 
36F7: 23              INC     HL                  ; 
36F8: 10 F8           DJNZ    $36F2               ; {}
36FA: EB              EX      DE,HL               ; 
36FB: 21 40 80        LD      HL,$8040            ; 
36FE: 01 40 03        LD      BC,$0340            ; 
3701: ED B0           LDIR                        ; 
3703: 21 00 80        LD      HL,$8000            ; 
3706: 01 40 00        LD      BC,$0040            ; 
3709: ED B0           LDIR                        ; 
370B: AF              XOR     A                   ; 
370C: 32 A0 92        LD      ($92A0),A           ; 
370F: 3A A0 92        LD      A,($92A0)           ; 
3712: 87              ADD     A,A                 ; 
3713: 30 FA           JR      NC,$370F            ; {}
3715: 3A B5 99        LD      A,($99B5)           ; 
3718: 87              ADD     A,A                 ; 
3719: 30 FA           JR      NC,$3715            ; {}
371B: F3              DI                          ; 
371C: CD EC 37        CALL    $37EC               ; {}
371F: 3E FE           LD      A,$FE               ; 
3721: 32 A0 92        LD      ($92A0),A           ; 
3724: 3A A0 92        LD      A,($92A0)           ; 
3727: A7              AND     A                   ; 
3728: 20 FA           JR      NZ,$3724            ; {}
372A: 32 30 68        LD      ($6830),A           ; 
372D: 21 80 92        LD      HL,$9280            ; 
3730: 11 00 70        LD      DE,$7000            ; 
3733: 01 08 00        LD      BC,$0008            ; 
3736: D9              EXX                         ; 
3737: 3E E1           LD      A,$E1               ; 
3739: 32 00 71        LD      ($7100),A           ; IO Processor
373C: CD EC 37        CALL    $37EC               ; {}
373F: 21 00 70        LD      HL,$7000            ; 
3742: 11 88 92        LD      DE,$9288            ; 
3745: 01 03 00        LD      BC,$0003            ; 
3748: D9              EXX                         ; 
3749: 3E B1           LD      A,$B1               ; 
374B: 32 00 71        LD      ($7100),A           ; 
374E: CD EC 37        CALL    $37EC               ; {}
3751: 3A 88 92        LD      A,($9288)           ; 
3754: FE A1           CP      $A1                 ; 
3756: 30 D5           JR      NC,$372D            ; {}
3758: E6 0F           AND     $0F                 ; 
375A: FE 0A           CP      $0A                 ; 
375C: 30 CF           JR      NC,$372D            ; {}
375E: FB              EI                          ; 
375F: AF              XOR     A                   ; 
3760: 32 10 82        LD      ($8210),A           ; 
3763: C3 D3 02        JP      $02D3               ; {}
3766: CD 74 37        CALL    $3774               ; {}
3769: CD 74 37        CALL    $3774               ; {}
376C: CD 74 37        CALL    $3774               ; {}
376F: 3E 05           LD      A,$05               ; 
3771: C3 10 00        JP      $0010               ; {}
3774: 1A              LD      A,(DE)              ; 
3775: 0E 08           LD      C,$08               ; 
3777: 87              ADD     A,A                 ; 
3778: 30 01           JR      NC,$377B            ; {}
377A: 34              INC     (HL)                ; 
377B: 23              INC     HL                  ; 
377C: 0D              DEC     C                   ; 
377D: 20 F8           JR      NZ,$3777            ; {}
377F: 13              INC     DE                  ; 
3780: 23              INC     HL                  ; 
3781: C9              RET                         ; 

3782: 02              LD      (BC),A              ; #
3783: 02              LD      (BC),A              ; #
3784: 02              LD      (BC),A              ; #
3785: 02              LD      (BC),A              ; #
3786: 02              LD      (BC),A              ; #
3787: 08              EX      AF,AF'              ; #
3788: 08              EX      AF,AF'              ; #
3789: 08              EX      AF,AF'              ; #
378A: 08              EX      AF,AF'              ; #
378B: 08              EX      AF,AF'              ; #
378C: 08              EX      AF,AF'              ; #
378D: 02              LD      (BC),A              ; #
378E: 02              LD      (BC),A              ; #
378F: 02              LD      (BC),A              ; #
3790: 08              EX      AF,AF'              ; #
3791: 08              EX      AF,AF'              ; #
3792: 08              EX      AF,AF'              ; #
3793: 08              EX      AF,AF'              ; #
3794: 08              EX      AF,AF'              ; #
3795: 08              EX      AF,AF'              ; #
3796: 08              EX      AF,AF'              ; #
3797: FF              RST     0X38                ; #
3798: 01 3E 00        LD      BC,$003E            ; #
379B: 7F              LD      A,A                 ; #
379C: 41              LD      B,C                 ; #
379D: 00              NOP                         ; #
379E: 21 41 00        LD      HL,$0041            ; #
37A1: 00              NOP                         ; #
37A2: 41              LD      B,C                 ; #
37A3: 00              NOP                         ; #
37A4: 36 3E           LD      (HL),$3E            ; #
37A6: 00              NOP                         ; #
37A7: 49              LD      C,C                 ; #
37A8: 00              NOP                         ; #
37A9: 03              INC     BC                  ; #
37AA: 49              LD      C,C                 ; #
37AB: 22 03 49        LD      ($4903),HL          ; #
37AE: 41              LD      B,C                 ; #
37AF: 00              NOP                         ; #
37B0: 36 41           LD      (HL),$41            ; #
37B2: 3E 00           LD      A,$00               ; #
37B4: 3E 41           LD      A,$41               ; #
37B6: 3E 00           LD      A,$00               ; #
37B8: 41              LD      B,C                 ; #
37B9: 49              LD      C,C                 ; #
37BA: 7F              LD      A,A                 ; #
37BB: 41              LD      B,C                 ; #
37BC: 49              LD      C,C                 ; #
37BD: 20 7F           JR      NZ,$383E            ; {} #
37BF: 49              LD      C,C                 ; #
37C0: 18 00           JR      $37C2               ; {} #
37C2: 32 20 40        LD      ($4020),A           ; #
37C5: 00              NOP                         ; #
37C6: 7F              LD      A,A                 ; #
37C7: 40              LD      B,B                 ; #
37C8: 01 00 7F        LD      BC,$7F00            ; #
37CB: 7F              LD      A,A                 ; #
37CC: 3F              CCF                         ; #
37CD: 40              LD      B,B                 ; #
37CE: 21 44 40        LD      HL,$4044            ; #
37D1: 00              NOP                         ; #
37D2: 44              LD      B,H                 ; #
37D3: 00              NOP                         ; #
37D4: 3C              INC     A                   ; #
37D5: 44              LD      B,H                 ; #
37D6: 01 42 3F        LD      BC,$3F42            ; #
37D9: 01 81 00        LD      BC,$0081            ; #
37DC: 01 A5 7F        LD      BC,$7FA5            ; #
37DF: 01 A5 04        LD      BC,$04A5            ; #
37E2: 7F              LD      A,A                 ; #
37E3: 99              SBC     C                   ; #
37E4: 08              EX      AF,AF'              ; #
37E5: 00              NOP                         ; #
37E6: 42              LD      B,D                 ; #
37E7: 10 00           DJNZ    $37E9               ; {} #
37E9: 3C              INC     A                   ; #
37EA: 7F              LD      A,A                 ; #
37EB: 00              NOP                         ; #

; Wait for IO processor to complete
37EC: 3A 00 71        LD      A,($7100)           ; Status of IO processor.
37EF: FE 10           CP      $10                 ; Wait ...
37F1: C8              RET     Z                   ; ... for ...
37F2: 18 F8           JR      $37EC               ; {} ... status = 10

37F4: 3A 07 68        LD      A,($6807)           ; 
37F7: 1F              RRA                         ; 
37F8: 3C              INC     A                   ; 
37F9: E6 01           AND     $01                 ; 
37FB: 32 83 99        LD      ($9983),A           ; 
37FE: 21 CC 3A        LD      HL,$3ACC            ; 
3801: CF              RST     0X08                ; 
3802: CD 61 3A        CALL    $3A61               ; {}
3805: 3A B5 99        LD      A,($99B5)           ; 
3808: 0E 00           LD      C,$00               ; 
380A: E6 0C           AND     $0C                 ; 
380C: 20 01           JR      NZ,$380F            ; {}
380E: 0C              INC     C                   ; 
380F: 79              LD      A,C                 ; 
3810: 32 07 A0        LD      ($A007),A           ; 
3813: 21 01 68        LD      HL,$6801            ; 
3816: 7E              LD      A,(HL)              ; 
3817: 1F              RRA                         ; 
3818: E6 01           AND     $01                 ; 
381A: 4F              LD      C,A                 ; 
381B: 23              INC     HL                  ; 
381C: 7E              LD      A,(HL)              ; 
381D: E6 02           AND     $02                 ; 
381F: B1              OR      C                   ; 
3820: 32 84 99        LD      ($9984),A           ; 
3823: 21 68 3A        LD      HL,$3A68            ; 
3826: D7              RST     0X10                ; 
3827: 11 2C 82        LD      DE,$822C            ; 
382A: ED A0           LDI                         ; 
382C: 21 E4 3A        LD      HL,$3AE4            ; 
382F: CD 1B 33        CALL    $331B               ; {}
3832: 21 06 68        LD      HL,$6806            ; 
3835: 7E              LD      A,(HL)              ; 
3836: 23              INC     HL                  ; 
3837: 4E              LD      C,(HL)              ; 
3838: CB 19           RR      C                   ; 
383A: 8F              ADC     A,A                 ; 
383B: E6 03           AND     $03                 ; 
383D: 3C              INC     A                   ; 
383E: 32 82 99        LD      ($9982),A           ; 
3841: 3C              INC     A                   ; 
3842: 32 EA 82        LD      ($82EA),A           ; 
3845: 21 EB 3A        LD      HL,$3AEB            ; 
3848: CD 1B 33        CALL    $331B               ; {}
384B: 21 C4 3A        LD      HL,$3AC4            ; 
384E: 11 80 92        LD      DE,$9280            ; 
3851: 01 08 00        LD      BC,$0008            ; 
3854: ED B0           LDIR                        ; 
3856: 21 00 68        LD      HL,$6800            ; 
3859: 06 03           LD      B,$03               ; 
385B: AF              XOR     A                   ; 
385C: 4E              LD      C,(HL)              ; 
385D: CB 19           RR      C                   ; 
385F: 8F              ADC     A,A                 ; 
3860: 23              INC     HL                  ; 
3861: 10 F9           DJNZ    $385C               ; {}
3863: E6 07           AND     $07                 ; 
3865: 28 34           JR      Z,$389B             ; {}
3867: 3D              DEC     A                   ; 
3868: 87              ADD     A,A                 ; 
3869: 87              ADD     A,A                 ; 
386A: 87              ADD     A,A                 ; 
386B: 21 6C 3A        LD      HL,$3A6C            ; 
386E: D7              RST     0X10                ; 
386F: 11 81 92        LD      DE,$9281            ; 
3872: 01 04 00        LD      BC,$0004            ; 
3875: ED B0           LDIR                        ; 
3877: 11 E8 82        LD      DE,$82E8            ; 
387A: ED A0           LDI                         ; 
387C: 11 28 82        LD      DE,$8228            ; 
387F: ED A0           LDI                         ; 
3881: 11 E8 81        LD      DE,$81E8            ; 
3884: ED A0           LDI                         ; 
3886: 11 E8 80        LD      DE,$80E8            ; 
3889: ED A0           LDI                         ; 
388B: 3E 24           LD      A,$24               ; 
388D: 32 08 82        LD      ($8208),A           ; 
3890: 21 F6 3A        LD      HL,$3AF6            ; 
3893: CD 1B 33        CALL    $331B               ; {}
3896: CD 1B 33        CALL    $331B               ; {}
3899: 18 10           JR      $38AB               ; {}
389B: 21 81 92        LD      HL,$9281            ; 
389E: 06 04           LD      B,$04               ; 
38A0: 36 00           LD      (HL),$00            ; 
38A2: 23              INC     HL                  ; 
38A3: 10 FB           DJNZ    $38A0               ; {}
38A5: 21 07 3B        LD      HL,$3B07            ; 
38A8: CD 1B 33        CALL    $331B               ; {}
38AB: 21 03 68        LD      HL,$6803            ; 
38AE: 06 03           LD      B,$03               ; 
38B0: AF              XOR     A                   ; 
38B1: 4E              LD      C,(HL)              ; 
38B2: CB 19           RR      C                   ; 
38B4: 8F              ADC     A,A                 ; 
38B5: 23              INC     HL                  ; 
38B6: 10 F9           DJNZ    $38B1               ; {}
38B8: E6 07           AND     $07                 ; 
38BA: CA 2D 39        JP      Z,$392D             ; {}
38BD: 4F              LD      C,A                 ; 
38BE: 3A 82 99        LD      A,($9982)           ; 
38C1: E6 04           AND     $04                 ; 
38C3: 87              ADD     A,A                 ; 
38C4: 81              ADD     A,C                 ; 
38C5: 87              ADD     A,A                 ; 
38C6: 21 A4 3A        LD      HL,$3AA4            ; 
38C9: D7              RST     0X10                ; 
38CA: 11 80 99        LD      DE,$9980            ; 
38CD: ED A0           LDI                         ; 
38CF: ED A0           LDI                         ; 
38D1: 2B              DEC     HL                  ; 
38D2: 0E 01           LD      C,$01               ; 
38D4: CD DA 38        CALL    $38DA               ; {}
38D7: 2B              DEC     HL                  ; 
38D8: 0E 00           LD      C,$00               ; 
38DA: 7E              LD      A,(HL)              ; 
38DB: 3C              INC     A                   ; 
38DC: CA 3B 39        JP      Z,$393B             ; {}
38DF: 79              LD      A,C                 ; 
38E0: 87              ADD     A,A                 ; 
38E1: E5              PUSH    HL                  ; 
38E2: 21 1D 3B        LD      HL,$3B1D            ; 
38E5: D7              RST     0X10                ; 
38E6: 7E              LD      A,(HL)              ; 
38E7: 23              INC     HL                  ; 
38E8: 66              LD      H,(HL)              ; 
38E9: 6F              LD      L,A                 ; 
38EA: C5              PUSH    BC                  ; 
38EB: CD 1B 33        CALL    $331B               ; {}
38EE: CD 1B 33        CALL    $331B               ; {}
38F1: C1              POP     BC                  ; 
38F2: E1              POP     HL                  ; 
38F3: 7E              LD      A,(HL)              ; 
38F4: E6 7F           AND     $7F                 ; 
38F6: EB              EX      DE,HL               ; 
38F7: 21 F0 81        LD      HL,$81F0            ; 
38FA: 41              LD      B,C                 ; 
38FB: 10 02           DJNZ    $38FF               ; {}
38FD: 23              INC     HL                  ; 
38FE: 23              INC     HL                  ; 
38FF: CD 1E 39        CALL    $391E               ; {}
3902: EB              EX      DE,HL               ; 
3903: 0D              DEC     C                   ; 
3904: C0              RET     NZ                  ; 
3905: EB              EX      DE,HL               ; 
3906: 1A              LD      A,(DE)              ; 
3907: CB 7F           BIT     7,A                 ; 
3909: C2 49 39        JP      NZ,$3949            ; {}
390C: 21 F4 81        LD      HL,$81F4            ; 
390F: CD 1E 39        CALL    $391E               ; {}
3912: D5              PUSH    DE                  ; 
3913: 21 50 3B        LD      HL,$3B50            ; 
3916: CD 1B 33        CALL    $331B               ; {}
3919: CD 1B 33        CALL    $331B               ; {}
391C: E1              POP     HL                  ; 
391D: C9              RET                         ; 
391E: FE 0A           CP      $0A                 ; 
3920: 06 24           LD      B,$24               ; 
3922: 38 04           JR      C,$3928             ; {}
3924: 06 01           LD      B,$01               ; 
3926: D6 0A           SUB     $0A                 ; 
3928: 70              LD      (HL),B              ; 
3929: CB AD           RES     5,L                 ; 
392B: 77              LD      (HL),A              ; 
392C: C9              RET                         ; 
392D: 21 67 3B        LD      HL,$3B67            ; BONUS Report message
3930: CD 1B 33        CALL    $331B               ; {} Print message
3933: 21 80 99        LD      HL,$9980            ; 
3936: 36 FF           LD      (HL),$FF            ; 
3938: 23              INC     HL                  ; 
3939: 36 FF           LD      (HL),$FF            ; 
393B: EB              EX      DE,HL               ; 
393C: 21 32 83        LD      HL,$8332            ; 
393F: 06 16           LD      B,$16               ; 
3941: 36 24           LD      (HL),$24            ; 
3943: 3E E0           LD      A,$E0               ; 
3945: 25              DEC     H                   ; 
3946: D7              RST     0X10                ; 
3947: 10 F8           DJNZ    $3941               ; {}
3949: 21 34 83        LD      HL,$8334            ; 
394C: 06 16           LD      B,$16               ; 
394E: 36 24           LD      (HL),$24            ; 
3950: 3E E0           LD      A,$E0               ; 
3952: 25              DEC     H                   ; 
3953: D7              RST     0X10                ; 
3954: 10 F8           DJNZ    $394E               ; {}
3956: EB              EX      DE,HL               ; 
3957: C9              RET                         ; 

; Clear screen
3958: 21 00 80        LD      HL,$8000            ; Start of RAM
395B: 11 01 80        LD      DE,$8001            ; RAM +1
395E: 01 00 04        LD      BC,$0400            ; 400 bytes of screen
3961: 36 24           LD      (HL),$24            ; Space character
3963: ED B0           LDIR                        ; Clear screen
3965: 36 03           LD      (HL),$03            ; Next pattern 03
3967: 01 FF 03        LD      BC,$03FF            ; 3FF bytes
396A: ED B0           LDIR                        ; 
396C: 3E 07           LD      A,$07               ; 
396E: 32 BE 99        LD      ($99BE),A           ; 
3971: C9              RET                         ; 

3972: 21 80 93        LD      HL,$9380            ; 
3975: 06 80           LD      B,$80               ; 
3977: 36 F1           LD      (HL),$F1            ; 
3979: 23              INC     HL                  ; 
397A: 10 FB           DJNZ    $3977               ; {}
397C: C9              RET                         ; 

397D: 21 E0 99        LD      HL,$99E0            ; 
3980: 11 5E 83        LD      DE,$835E            ; 
3983: 0E 02           LD      C,$02               ; 
3985: 06 01           LD      B,$01               ; 
3987: CD 97 39        CALL    $3997               ; {}
398A: 06 03           LD      B,$03               ; 
398C: CD 97 39        CALL    $3997               ; {}
398F: 06 02           LD      B,$02               ; 
3991: CD 97 39        CALL    $3997               ; {}
3994: 23              INC     HL                  ; 
3995: 06 01           LD      B,$01               ; 
3997: CD AA 39        CALL    $39AA               ; {}
399A: CD A0 39        CALL    $39A0               ; {}
399D: 10 FB           DJNZ    $399A               ; {}
399F: C9              RET                         ; 
39A0: 3E 99           LD      A,$99               ; 
39A2: 96              SUB     (HL)                ; 
39A3: 1F              RRA                         ; 
39A4: 1F              RRA                         ; 
39A5: 1F              RRA                         ; 
39A6: 1F              RRA                         ; 
39A7: CD AE 39        CALL    $39AE               ; {}
39AA: 3E 99           LD      A,$99               ; 
39AC: 96              SUB     (HL)                ; 
39AD: 23              INC     HL                  ; 
39AE: E6 0F           AND     $0F                 ; 
39B0: 12              LD      (DE),A              ; 
39B1: E7              RST     0X20                ; 
39B2: 0D              DEC     C                   ; 
39B3: C0              RET     NZ                  ; 
39B4: 3E 2A           LD      A,$2A               ; 
39B6: 0E 04           LD      C,$04               ; 
39B8: 12              LD      (DE),A              ; 
39B9: E7              RST     0X20                ; 
39BA: C9              RET                         ; 
39BB: 21 5E 83        LD      HL,$835E            ; 
39BE: 06 17           LD      B,$17               ; 
39C0: 11 E0 FF        LD      DE,$FFE0            ; 
39C3: 36 24           LD      (HL),$24            ; 
39C5: 19              ADD     HL,DE               ; 
39C6: 10 FB           DJNZ    $39C3               ; {}
39C8: C9              RET                         ; 

39C9: E5              PUSH    HL                  ; 
39CA: CD 7D 39        CALL    $397D               ; {}
39CD: 21 84 03        LD      HL,$0384            ; 
39D0: 22 72 92        LD      ($9272),HL          ; 
39D3: E1              POP     HL                  ; 
39D4: C1              POP     BC                  ; 
39D5: C9              RET                         ; 

39D6: C5              PUSH    BC                  ; 
39D7: 78              LD      A,B                 ; 
39D8: FE 0F           CP      $0F                 ; 
39DA: 28 ED           JR      Z,$39C9             ; {}
39DC: FE 02           CP      $02                 ; 
39DE: 28 15           JR      Z,$39F5             ; {}
39E0: FE 04           CP      $04                 ; 
39E2: 20 3D           JR      NZ,$3A21            ; {}
39E4: 3A 70 92        LD      A,($9270)           ; 
39E7: D6 01           SUB     $01                 ; 
39E9: 30 02           JR      NC,$39ED            ; {}
39EB: 3E 11           LD      A,$11               ; 
39ED: 32 70 92        LD      ($9270),A           ; 
39F0: 18 0A           JR      $39FC               ; {}
39F2: C5              PUSH    BC                  ; 
39F3: 18 07           JR      $39FC               ; {}
39F5: 3A 70 92        LD      A,($9270)           ; 
39F8: 3C              INC     A                   ; 
39F9: 32 70 92        LD      ($9270),A           ; 
39FC: 3A 70 92        LD      A,($9270)           ; 
39FF: FE 12           CP      $12                 ; 
3A01: 38 01           JR      C,$3A04             ; {}
3A03: AF              XOR     A                   ; 
3A04: 32 70 92        LD      ($9270),A           ; 
3A07: E5              PUSH    HL                  ; 
3A08: 0E 00           LD      C,$00               ; 
3A0A: FE 0A           CP      $0A                 ; 
3A0C: 38 03           JR      C,$3A11             ; {}
3A0E: 0C              INC     C                   ; 
3A0F: D6 0A           SUB     $0A                 ; 
3A11: 21 2E 82        LD      HL,$822E            ; 
3A14: 71              LD      (HL),C              ; 
3A15: 2E 0E           LD      L,$0E               ; 
3A17: 77              LD      (HL),A              ; 
3A18: 21 47 3A        LD      HL,$3A47            ; 
3A1B: CD 1B 33        CALL    $331B               ; {}
3A1E: E1              POP     HL                  ; 
3A1F: C1              POP     BC                  ; 
3A20: C9              RET                         ; 

3A21: 3A 70 92        LD      A,($9270)           ; 
3A24: FE 12           CP      $12                 ; 
3A26: 38 01           JR      C,$3A29             ; {}
3A28: AF              XOR     A                   ; 
3A29: 32 70 92        LD      ($9270),A           ; 
3A2C: EB              EX      DE,HL               ; 
3A2D: CD 3C 3A        CALL    $3A3C               ; {}
3A30: 21 4F 3A        LD      HL,$3A4F            ; 
3A33: D7              RST     0X10                ; 
3A34: 6E              LD      L,(HL)              ; 
3A35: 26 9A           LD      H,$9A               ; 
3A37: 36 01           LD      (HL),$01            ; 
3A39: EB              EX      DE,HL               ; 
3A3A: C1              POP     BC                  ; 
3A3B: C9              RET                         ; 

3A3C: 21 A0 9A        LD      HL,$9AA0            ; 
3A3F: 06 40           LD      B,$40               ; 
3A41: 36 00           LD      (HL),$00            ; 
3A43: 23              INC     HL                  ; 
3A44: 10 FB           DJNZ    $3A41               ; {}
3A46: C9              RET                         ; 

3A47: EE 82           XOR     $82                 ; #
3A49: 05              DEC     B                   ; #
3A4A: 1C              INC     E                   ; #
3A4B: 18 1E           JR      $3A6B               ; {} #
3A4D: 17              RLA                         ; #
3A4E: 0D              DEC     C                   ; #
3A4F: A1              AND     C                   ; #
3A50: A2              AND     D                   ; #
3A51: A3              AND     E                   ; #
3A52: A4              AND     H                   ; #
3A53: A7              AND     A                   ; #
3A54: AA              XOR     D                   ; #
3A55: AB              XOR     E                   ; #
3A56: AC              XOR     H                   ; #
3A57: AD              XOR     L                   ; #
3A58: AE              XOR     (HL)                ; #
3A59: AF              XOR     A                   ; #
3A5A: B0              OR      B                   ; #
3A5B: B2              OR      D                   ; #
3A5C: B3              OR      E                   ; #
3A5D: B4              OR      H                   ; #
3A5E: B5              OR      L                   ; #
3A5F: B6              OR      (HL)                ; #
3A60: B9              CP      C                   ; #

3A61: 7E              LD      A,(HL)              ; 
3A62: 23              INC     HL                  ; 
3A63: 66              LD      H,(HL)              ; 

3A64: 6F              LD      L,A                 ; 
3A65: C3 1B 33        JP      $331B               ; {} Print message on screen

3A68: 0B              DEC     BC                  ; #
3A69: 0C              INC     C                   ; #
3A6A: 0D              DEC     C                   ; #
3A6B: 0A              LD      A,(BC)              ; #
3A6C: 04              INC     B                   ; #
3A6D: 01 04 01        LD      BC,$0104            ; #
3A70: 04              INC     B                   ; #
3A71: 1C              INC     E                   ; #
3A72: 01 24 03        LD      BC,$0324            ; #
3A75: 01 03 01        LD      BC,$0103            ; #
3A78: 03              INC     BC                  ; #
3A79: 1C              INC     E                   ; #
3A7A: 01 24 02        LD      BC,$0224            ; #
3A7D: 01 02 01        LD      BC,$0102            ; #
3A80: 02              LD      (BC),A              ; #
3A81: 1C              INC     E                   ; #
3A82: 01 24 02        LD      BC,$0224            ; #
3A85: 03              INC     BC                  ; #
3A86: 02              LD      (BC),A              ; #
3A87: 03              INC     BC                  ; #
3A88: 02              LD      (BC),A              ; #
3A89: 1C              INC     E                   ; #
3A8A: 03              INC     BC                  ; #
3A8B: 1C              INC     E                   ; #
3A8C: 01 03 01        LD      BC,$0103            ; #
3A8F: 03              INC     BC                  ; #
3A90: 01 24 03        LD      BC,$0324            ; #
3A93: 1C              INC     E                   ; #
3A94: 01 02 01        LD      BC,$0102            ; #
3A97: 02              LD      (BC),A              ; #
3A98: 01 24 02        LD      BC,$0224            ; #
3A9B: 1C              INC     E                   ; #
3A9C: 01 01 01        LD      BC,$0101            ; #
3A9F: 01 01 24        LD      BC,$2401            ; #
3AA2: 01 24 FF        LD      BC,$FF24            ; #
3AA5: FF              RST     0X38                ; #
3AA6: 02              LD      (BC),A              ; #
3AA7: 06 02           LD      B,$02               ; #
3AA9: 07              RLCA                        ; #
3AAA: 02              LD      (BC),A              ; #
3AAB: 08              EX      AF,AF'              ; #
3AAC: 03              INC     BC                  ; #
3AAD: 0A              LD      A,(BC)              ; #
3AAE: 03              INC     BC                  ; #
3AAF: 0C              INC     C                   ; #
3AB0: 02              LD      (BC),A              ; #
3AB1: 86              ADD     A,(HL)              ; #
3AB2: 03              INC     BC                  ; #
3AB3: 88              ADC     A,B                 ; #
3AB4: FF              RST     0X38                ; #
3AB5: FF              RST     0X38                ; #
3AB6: 03              INC     BC                  ; #
3AB7: 0A              LD      A,(BC)              ; #
3AB8: 03              INC     BC                  ; #
3AB9: 0C              INC     C                   ; #
3ABA: 03              INC     BC                  ; #
3ABB: 0F              RRCA                        ; #
3ABC: 03              INC     BC                  ; #
3ABD: 8A              ADC     A,D                 ; #
3ABE: 03              INC     BC                  ; #
3ABF: 8C              ADC     A,H                 ; #
3AC0: 03              INC     BC                  ; #
3AC1: 8F              ADC     A,A                 ; #
3AC2: 03              INC     BC                  ; #
3AC3: FF              RST     0X38                ; #
3AC4: 01 01 01        LD      BC,$0101            ; #
3AC7: 01 01 02        LD      BC,$0201            ; #
3ACA: 03              INC     BC                  ; #
3ACB: 00              NOP                         ; #
3ACC: D0              RET     NC                  ; #
3ACD: 3A DA 3A        LD      A,($3ADA)           ; {} #
3AD0: E6 82           AND     $82                 ; #
3AD2: 07              RLCA                        ; #
3AD3: 1E 19           LD      E,$19               ; #
3AD5: 1B              DEC     DE                  ; #
3AD6: 12              LD      (DE),A              ; #
3AD7: 10 11           DJNZ    $3AEA               ; {} #
3AD9: 1D              DEC     E                   ; #
3ADA: E6 82           AND     $82                 ; #
3ADC: 07              RLCA                        ; #
3ADD: 1D              DEC     E                   ; #
3ADE: 0A              LD      A,(BC)              ; #
3ADF: 0B              DEC     BC                  ; #
3AE0: 15              DEC     D                   ; #
3AE1: 0E 24           LD      C,$24               ; #
3AE3: 24              INC     H                   ; #
3AE4: EC 82 04        CALL    PE,$0482            ; {} #
3AE7: 1B              DEC     DE                  ; #
3AE8: 0A              LD      A,(BC)              ; #
3AE9: 17              RLA                         ; #
3AEA: 14              INC     D                   ; #
3AEB: AA              XOR     D                   ; #
3AEC: 82              ADD     A,D                 ; #
3AED: 08              EX      AF,AF'              ; #
3AEE: 0F              RRCA                        ; #
3AEF: 12              LD      (DE),A              ; #
3AF0: 10 11           DJNZ    $3B03               ; {} #
3AF2: 1D              DEC     E                   ; #
3AF3: 0E 1B           LD      C,$1B               ; #
3AF5: 1C              INC     E                   ; #
3AF6: C8              RET     Z                   ; #
3AF7: 82              ADD     A,D                 ; #
3AF8: 05              DEC     B                   ; #
3AF9: 24              INC     H                   ; #
3AFA: 0C              INC     C                   ; #
3AFB: 18 12           JR      $3B0F               ; {} #
3AFD: 17              RLA                         ; #
3AFE: A8              XOR     B                   ; #
3AFF: 81              ADD     A,C                 ; #
3B00: 06 0C           LD      B,$0C               ; #
3B02: 1B              DEC     DE                  ; #
3B03: 0E 0D           LD      C,$0D               ; #
3B05: 12              LD      (DE),A              ; #
3B06: 1D              DEC     E                   ; #
3B07: E8              RET     PE                  ; #
3B08: 82              ADD     A,D                 ; #
3B09: 12              LD      (DE),A              ; #
3B0A: 0F              RRCA                        ; #
3B0B: 1B              DEC     DE                  ; #
3B0C: 0E 0E           LD      C,$0E               ; #
3B0E: 24              INC     H                   ; #
3B0F: 19              ADD     HL,DE               ; #
3B10: 15              DEC     D                   ; #
3B11: 0A              LD      A,(BC)              ; #
3B12: 22 24 24        LD      ($2424),HL          ; {} #
3B15: 24              INC     H                   ; #
3B16: 24              INC     H                   ; #
3B17: 24              INC     H                   ; #
3B18: 24              INC     H                   ; #
3B19: 24              INC     H                   ; #
3B1A: 24              INC     H                   ; #
3B1B: 24              INC     H                   ; #
3B1C: 24              INC     H                   ; #
3B1D: 21 3B 39        LD      HL,$393B            ; #
3B20: 3B              DEC     SP                  ; #
3B21: 30 83           JR      NC,$3AA6            ; {} #
3B23: 0A              LD      A,(BC)              ; #
3B24: 01 1C 1D        LD      BC,$1D1C            ; #
3B27: 24              INC     H                   ; #
3B28: 0B              DEC     BC                  ; #
3B29: 18 17           JR      $3B42               ; {} #
3B2B: 1E 1C           LD      E,$1C               ; #
3B2D: 24              INC     H                   ; #
3B2E: B0              OR      B                   ; #
3B2F: 81              ADD     A,C                 ; #
3B30: 08              EX      AF,AF'              ; #
3B31: 00              NOP                         ; #
3B32: 00              NOP                         ; #
3B33: 00              NOP                         ; #
3B34: 00              NOP                         ; #
3B35: 24              INC     H                   ; #
3B36: 19              ADD     HL,DE               ; #
3B37: 1D              DEC     E                   ; #
3B38: 1C              INC     E                   ; #
3B39: 32 83 09        LD      ($0983),A           ; {} #
3B3C: 02              LD      (BC),A              ; #
3B3D: 17              RLA                         ; #
3B3E: 0D              DEC     C                   ; #
3B3F: 24              INC     H                   ; #
3B40: 0B              DEC     BC                  ; #
3B41: 18 17           JR      $3B5A               ; {} #
3B43: 1E 1C           LD      E,$1C               ; #
3B45: B2              OR      D                   ; #
3B46: 81              ADD     A,C                 ; #

3B47: 08          ;8
3B48: 00          ;0
3B49: 00          ;0
3B4A: 00          ;0
3B4B: 00          ;0
3B4C: 24          ;
3B4D: 19          ;P
3B4E: 1D          ;T
3B4F: 1C          ;S
3B50: 34          
3B51: 83          
3B52: 09          
3B53: 0A          ;A
3B54: 17          ;N
3B55: 0D          ;D
3B56: 24          ; 
3B57: 0E 1F       ;EV
3B59: 0E 1B       ;ER
3B5B: 22          ;Y

; Points display
3B5C: B4 81 08    ; Start on screen at 81B4 - 8 bytes
3B5F: 00          ;0
3B60: 00          ;0
3B61: 00          ;0
3B62: 00          ;0
3B63: 24          ;
3B64: 19          ;P
3B65: 1D          ;T
3B66: 1C          ;S

; Bonus report
3B67: 30 83 16    ; Start on screen at 8330 - 0x16 bytes
3B6A: 0B          ;B
3B6B: 18 17       ;ON
3B6D: 1E 1C       ;US
3B6F: 24          ;
3B70: 17          ;N
3B71: 18 1D       ;OT
3B73: 11 12 17    ;HIN
3B76: 10 24       ;G
3B78: 24          
3B79: 24          
3B7A: 24          
3B7B: 24          ;
3B7C: 24          
3B7D: 24          
3B7E: 24          
3B7F: 24          
3B80: 24          

; RAM Report
3B81: E2 82 07    ; Start on screen at 8207 - 7 bytes  
3B84: 1B          ;R 
3B85: 0A          ;A 
3B86: 16 24       ;M  
3B88: 24          ; 
3B89: 18 14       ;OK 

; ROM Report
3B8B: E4 82 07    ; Start on screen at 82E4 - 7 bytes
3B8E: 1B          ;R
3B8F: 18 16       ;OM
3B91: 24          ;
3B92: 24          ;
3B93: 18 14       ;OK

3B95: FF FF FF FF FF FF FF FF FF FF FF
3BA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3BB0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3BC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3BD0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3BE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3BF0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

3C00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3C10: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3C20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3C30: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3C40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3C50: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3C60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3C70: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3C80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3C90: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3CA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3CB0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3CC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3CD0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3CE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3CF0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

3D00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3D10: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3D20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3D30: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3D40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3D50: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3D60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3D70: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3D80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3D90: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3DA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3DB0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3DC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3DD0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3DE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3DF0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

3E00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3E10: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3E20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3E30: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3E40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3E50: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3E60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3E70: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3E80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3E90: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3EA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3EB0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3EC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3ED0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3EE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3EF0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

3F00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3F10: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3F20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3F30: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3F40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3F50: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3F60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3F70: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3F80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3F90: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3FA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3FB0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3FC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3FD0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3FE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
3FF0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
3FFF: D9
```

