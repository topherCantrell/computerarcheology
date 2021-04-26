![CPU3](Galaga.jpg)

# CPU3 Sound Processor

>>> cpu Z80

>>> binary 0000:roms/3700g.bin

```code
; Sound processor

; Restart comes here
0000: 31 00 9B        LD      SP,$9B00            ; Initialize stack
0003: C3 7B 00        JP      $007B               ; {} Continue processing
0006: FF              RST     0X38                ; Filler for RST
0007: FF              RST     0X38                ; Filler for RST

; Add A*2 to HL. (If A is zero, add 0x100 to HL)
0008: 87              ADD     A,A                 ; A *2
0009: 30 05           JR      NC,$10              ; {} Not zero
000B: 24              INC     H                   ; If zero ...
000C: 18 02           JR      $10                 ; {} ... add 100 instead
000E: FF              RST     0X38                ; Filler
000F: FF              RST     0X38                ; Filler

; Add A to HL
0010: 85              ADD     A,L                 ; Offset L by A
0011: 6F              LD      L,A                 ; Overflow?
0012: D0              RET     NC                  ; No - HL is fine
0013: 24              INC     H                   ; Yes - carry into H
0014: C9              RET                         ; Done
0015: FF              RST     0X38                ; Filler
0016: FF              RST     0X38                ; Filler
0017: FF              RST     0X38                ; Filler

; 
0018: 77              LD      (HL),A              ; 
0019: 23              INC     HL                  ; 
001A: 10 FC           DJNZ    $18                 ; {}
001C: C9              RET                         ; 

001D: FF FF FF
0020: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0030: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0040: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0050: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0060: FF FF FF FF FF FF 

; IRQ comes here
; Acknowledge the interrupt and preserve registers across 00B1 call
0066: F5              PUSH    AF                  ; Hold ...
0067: C5              PUSH    BC                  ; ...
0068: D5              PUSH    DE                  ; ...
0069: E5              PUSH    HL                  ; ... all registers
006A: 3E 01           LD      A,$01               ; Acknowledge ...
006C: 32 22 68        LD      ($6822),A           ; ... IRQ delivery
006F: AF              XOR     A                   ; Disable ...
0070: 32 22 68        LD      ($6822),A           ; ... IRQ delivery
0073: CD B1 00        CALL    $00B1               ; {} Handle the request
0076: E1              POP     HL                  ; Restore ...
0077: D1              POP     DE                  ; ...
0078: C1              POP     BC                  ; ...
0079: F1              POP     AF                  ; ... all registers
007A: C9              RET                         ; Done

; Initialization
; Disable NMI
; Wait for CLEAR, send checksum results, and wait for CLEAR.
; Enable NMI
; Clear memory from 9A00 - 9AFF
; Endless loop of NMI processing
007B: 3E 01           LD      A,$01               ; Disable ...
007D: 32 22 68        LD      ($6822),A           ; ... NMI
0080: 11 01 91        LD      DE,$9101            ; Semaphore
0083: 1A              LD      A,(DE)              ; Wait for ...
0084: A7              AND     A                   ; ... CPU1 to ...
0085: 20 FC           JR      NZ,$83              ; {} ... initialize
0087: 67              LD      H,A                 ; Zero H
0088: 6F              LD      L,A                 ; Zero L
0089: 01 10 00        LD      BC,$0010            ; Checksum ...
008C: 86              ADD     A,(HL)              ; ... first ...
008D: 23              INC     HL                  ; ... 1000 ...
008E: 10 FC           DJNZ    $8C                 ; {} ... bytes ...
0090: 0D              DEC     C                   ; ...
0091: 20 F9           JR      NZ,$8C              ; {} ... of ROM
0093: FE FF           CP      $FF                 ; ROM checksum looks good?
0095: 28 02           JR      Z,$99               ; {} Yes ... store FF
0097: 3E 21           LD      A,$21               ; Code for bad checksum
0099: 12              LD      (DE),A              ; Tell CPU1
009A: 1A              LD      A,(DE)              ; Wait ...
009B: A7              AND     A                   ; ... for ...
009C: 20 FC           JR      NZ,$9A              ; {} ... acknowledgement
009E: AF              XOR     A                   ; Enable ...
009F: 32 22 68        LD      ($6822),A           ; ... NMI
00A2: 21 00 9A        LD      HL,$9A00            ; Clear memory from ...
00A5: 36 00           LD      (HL),$00            ; ... 9A00 ...
00A7: 11 01 9A        LD      DE,$9A01            ; ... to ...
00AA: 01 FF 00        LD      BC,$00FF            ; ...
00AD: ED B0           LDIR                        ; ... 9AFF
00AF: 18 FE           JR      $AF                 ; {} Process Interrupts

; IRQ processing
00B1: 3A B8 9A        LD      A,($9AB8)           ; 
00B4: A7              AND     A                   ; 
00B5: C2 A1 06        JP      NZ,$06A1            ; {} TOPHER Initialize memory for something -- where from there?
00B8: 21 60 9A        LD      HL,$9A60            ; Clear ...
00BB: 36 00           LD      (HL),$00            ; ... 16 bytes from 9A60-9A70 ...
00BD: 11 61 9A        LD      DE,$9A61            ; ...
00C0: 01 0F 00        LD      BC,$000F            ; ...
00C3: ED B0           LDIR                        ; .
00C5: 3A B7 9A        LD      A,($9AB7)           ; 
00C8: A7              AND     A                   ; 
00C9: C2 42 03        JP      NZ,$0342            ; {}
00CC: 3A 79 9A        LD      A,($9A79)           ; 
00CF: A7              AND     A                   ; 
00D0: 28 09           JR      Z,$DB               ; {}
00D2: 21 A8 9A        LD      HL,$9AA8            ; 
00D5: 86              ADD     A,(HL)              ; 
00D6: 77              LD      (HL),A              ; 
00D7: AF              XOR     A                   ; 
00D8: 32 79 9A        LD      ($9A79),A           ; 
00DB: 3A A0 9A        LD      A,($9AA0)           ; 
00DE: A7              AND     A                   ; 
00DF: 28 6F           JR      Z,$150              ; {}
00E1: 3A 11 92        LD      A,($9211)           ; 
00E4: 21 80 9A        LD      HL,$9A80            ; 
00E7: BE              CP      (HL)                ; 
00E8: 28 20           JR      Z,$10A              ; {}
00EA: 32 80 9A        LD      ($9A80),A           ; 
00ED: 3C              INC     A                   ; 
00EE: 28 0C           JR      Z,$FC               ; {}
00F0: 21 EA 06        LD      HL,$06EA            ; 
00F3: 22 82 9A        LD      ($9A82),HL          ; 
00F6: AF              XOR     A                   ; 
00F7: 32 00 9A        LD      ($9A00),A           ; 
00FA: 18 09           JR      $105                ; {}
00FC: 21 FA 06        LD      HL,$06FA            ; 
00FF: 22 82 9A        LD      ($9A82),HL          ; 
0102: 32 00 9A        LD      ($9A00),A           ; 
0105: 32 81 9A        LD      ($9A81),A           ; 
0108: 18 12           JR      $11C                ; {}
010A: 21 00 9A        LD      HL,$9A00            ; 
010D: 34              INC     (HL)                ; 
010E: 7E              LD      A,(HL)              ; 
010F: FE 22           CP      $22                 ; 
0111: 20 1E           JR      NZ,$131             ; {}
0113: 36 00           LD      (HL),$00            ; 
0115: 3A 81 9A        LD      A,($9A81)           ; 
0118: 3C              INC     A                   ; 
0119: 32 81 9A        LD      ($9A81),A           ; 
011C: 2A 82 9A        LD      HL,($9A82)          ; 
011F: CF              RST     0X08                ; 
0120: 5E              LD      E,(HL)              ; 
0121: 23              INC     HL                  ; 
0122: 56              LD      D,(HL)              ; 
0123: ED 53 84 9A     LD      ($9A84),DE          ; 
0127: 3E 1F           LD      A,$1F               ; 
0129: D7              RST     0X10                ; 
012A: 5E              LD      E,(HL)              ; 
012B: 23              INC     HL                  ; 
012C: 56              LD      D,(HL)              ; 
012D: ED 53 86 9A     LD      ($9A86),DE          ; 
0131: 2A 86 9A        LD      HL,($9A86)          ; 
0134: ED 5B 84 9A     LD      DE,($9A84)          ; 
0138: 19              ADD     HL,DE               ; 
0139: 22 86 9A        LD      ($9A86),HL          ; 
013C: 7C              LD      A,H                 ; 
013D: 32 61 9A        LD      ($9A61),A           ; 
0140: 0F              RRCA                        ; 
0141: 0F              RRCA                        ; 
0142: 0F              RRCA                        ; 
0143: 0F              RRCA                        ; 
0144: 32 62 9A        LD      ($9A62),A           ; 
0147: 3E 0A           LD      A,$0A               ; 
0149: 32 65 9A        LD      ($9A65),A           ; 
014C: AF              XOR     A                   ; 
014D: 32 70 9A        LD      ($9A70),A           ; 
0150: 21 74 9A        LD      HL,$9A74            ; 
0153: 36 13           LD      (HL),$13            ; 
0155: 3A B3 9A        LD      A,($9AB3)           ; 
0158: A7              AND     A                   ; 
0159: 28 09           JR      Z,$164              ; {}
015B: AF              XOR     A                   ; 
015C: 32 B3 9A        LD      ($9AB3),A           ; 
015F: CD F9 03        CALL    $03F9               ; {}
0162: 18 09           JR      $16D                ; {}
0164: 3A D3 9A        LD      A,($9AD3)           ; 
0167: A7              AND     A                   ; 
0168: 28 03           JR      Z,$16D              ; {}
016A: CD 4F 04        CALL    $044F               ; {}
016D: 21 74 9A        LD      HL,$9A74            ; 
0170: 36 0F           LD      (HL),$0F            ; 
0172: 3A AF 9A        LD      A,($9AAF)           ; 
0175: A7              AND     A                   ; 
0176: 28 09           JR      Z,$181              ; {}
0178: AF              XOR     A                   ; 
0179: 32 AF 9A        LD      ($9AAF),A           ; 
017C: CD F9 03        CALL    $03F9               ; {}
017F: 18 09           JR      $18A                ; {}
0181: 3A CF 9A        LD      A,($9ACF)           ; 
0184: A7              AND     A                   ; 
0185: 28 03           JR      Z,$18A              ; {}
0187: CD 4F 04        CALL    $044F               ; {}
018A: 21 74 9A        LD      HL,$9A74            ; 
018D: 36 03           LD      (HL),$03            ; 
018F: 3A A3 9A        LD      A,($9AA3)           ; 
0192: A7              AND     A                   ; 
0193: 28 09           JR      Z,$19E              ; {}
0195: AF              XOR     A                   ; 
0196: 32 A3 9A        LD      ($9AA3),A           ; 
0199: CD F9 03        CALL    $03F9               ; {}
019C: 18 09           JR      $1A7                ; {}
019E: 3A C3 9A        LD      A,($9AC3)           ; 
01A1: A7              AND     A                   ; 
01A2: 28 03           JR      Z,$1A7              ; {}
01A4: CD 4F 04        CALL    $044F               ; {}
01A7: 21 74 9A        LD      HL,$9A74            ; 
01AA: 36 02           LD      (HL),$02            ; 
01AC: 3A A2 9A        LD      A,($9AA2)           ; 
01AF: A7              AND     A                   ; 
01B0: 28 09           JR      Z,$1BB              ; {}
01B2: AF              XOR     A                   ; 
01B3: 32 A2 9A        LD      ($9AA2),A           ; 
01B6: CD F9 03        CALL    $03F9               ; {}
01B9: 18 09           JR      $1C4                ; {}
01BB: 3A C2 9A        LD      A,($9AC2)           ; 
01BE: A7              AND     A                   ; 
01BF: 28 03           JR      Z,$1C4              ; {}
01C1: CD 4F 04        CALL    $044F               ; {}
01C4: 21 74 9A        LD      HL,$9A74            ; 
01C7: 36 04           LD      (HL),$04            ; 
01C9: 3A A4 9A        LD      A,($9AA4)           ; 
01CC: A7              AND     A                   ; 
01CD: 28 09           JR      Z,$1D8              ; {}
01CF: AF              XOR     A                   ; 
01D0: 32 A4 9A        LD      ($9AA4),A           ; 
01D3: CD F9 03        CALL    $03F9               ; {}
01D6: 18 09           JR      $1E1                ; {}
01D8: 3A C4 9A        LD      A,($9AC4)           ; 
01DB: A7              AND     A                   ; 
01DC: 28 03           JR      Z,$1E1              ; {}
01DE: CD 4F 04        CALL    $044F               ; {}
01E1: 21 74 9A        LD      HL,$9A74            ; 
01E4: 36 01           LD      (HL),$01            ; 
01E6: 3A A1 9A        LD      A,($9AA1)           ; 
01E9: A7              AND     A                   ; 
01EA: 28 09           JR      Z,$1F5              ; {}
01EC: AF              XOR     A                   ; 
01ED: 32 A1 9A        LD      ($9AA1),A           ; 
01F0: CD F9 03        CALL    $03F9               ; {}
01F3: 18 09           JR      $1FE                ; {}
01F5: 3A C1 9A        LD      A,($9AC1)           ; 
01F8: A7              AND     A                   ; 
01F9: 28 03           JR      Z,$1FE              ; {}
01FB: CD 4F 04        CALL    $044F               ; {}
01FE: 3A B2 9A        LD      A,($9AB2)           ; 
0201: A7              AND     A                   ; 
0202: 28 08           JR      Z,$20C              ; {}
0204: 21 74 9A        LD      HL,$9A74            ; 
0207: 36 12           LD      (HL),$12            ; 
0209: CD A7 04        CALL    $04A7               ; {}
020C: 3A A5 9A        LD      A,($9AA5)           ; 
020F: A7              AND     A                   ; 
0210: 28 2C           JR      Z,$23E              ; {}
0212: 21 74 9A        LD      HL,$9A74            ; 
0215: 36 05           LD      (HL),$05            ; 
0217: CD 7A 03        CALL    $037A               ; {}
021A: 21 7E 9A        LD      HL,$9A7E            ; 
021D: 34              INC     (HL)                ; 
021E: 3A 7E 9A        LD      A,($9A7E)           ; 
0221: FE 06           CP      $06                 ; 
0223: 38 11           JR      C,$236              ; {}
0225: 36 00           LD      (HL),$00            ; 
0227: 3A 7C 9A        LD      A,($9A7C)           ; 
022A: FE 04           CP      $04                 ; 
022C: 38 03           JR      C,$231              ; {}
022E: 3D              DEC     A                   ; 
022F: 18 02           JR      $233                ; {}
0231: 3E 0C           LD      A,$0C               ; 
0233: 32 7C 9A        LD      ($9A7C),A           ; 
0236: 3A 7C 9A        LD      A,($9A7C)           ; 
0239: 32 6F 9A        LD      ($9A6F),A           ; 
023C: 18 03           JR      $241                ; {}
023E: 32 C5 9A        LD      ($9AC5),A           ; 
0241: 3A A6 9A        LD      A,($9AA6)           ; 
0244: A7              AND     A                   ; 
0245: 28 24           JR      Z,$26B              ; {}
0247: 21 74 9A        LD      HL,$9A74            ; 
024A: 36 06           LD      (HL),$06            ; 
024C: CD 7A 03        CALL    $037A               ; {}
024F: 21 7F 9A        LD      HL,$9A7F            ; 
0252: 34              INC     (HL)                ; 
0253: 7E              LD      A,(HL)              ; 
0254: FE 1C           CP      $1C                 ; 
0256: 20 0B           JR      NZ,$263             ; {}
0258: AF              XOR     A                   ; 
0259: 32 7F 9A        LD      ($9A7F),A           ; 
025C: 3A 7D 9A        LD      A,($9A7D)           ; 
025F: 3C              INC     A                   ; 
0260: 32 7D 9A        LD      ($9A7D),A           ; 
0263: 3A 7D 9A        LD      A,($9A7D)           ; 
0266: 32 70 9A        LD      ($9A70),A           ; 
0269: 18 03           JR      $26E                ; {}
026B: 32 C6 9A        LD      ($9AC6),A           ; 
026E: 3A A9 9A        LD      A,($9AA9)           ; 
0271: A7              AND     A                   ; 
0272: 28 0A           JR      Z,$27E              ; {}
0274: 21 74 9A        LD      HL,$9A74            ; 
0277: 36 09           LD      (HL),$09            ; 
0279: CD 7A 03        CALL    $037A               ; {}
027C: 18 03           JR      $281                ; {}
027E: 32 C9 9A        LD      ($9AC9),A           ; 
0281: 3A A7 9A        LD      A,($9AA7)           ; 
0284: A7              AND     A                   ; 
0285: 28 0B           JR      Z,$292              ; {}
0287: 21 74 9A        LD      HL,$9A74            ; 
028A: 36 07           LD      (HL),$07            ; 
028C: CD A7 04        CALL    $04A7               ; {}
028F: C3 32 03        JP      $0332               ; {}
0292: 3A B1 9A        LD      A,($9AB1)           ; 
0295: A7              AND     A                   ; 
0296: 28 0A           JR      Z,$2A2              ; {}
0298: 21 74 9A        LD      HL,$9A74            ; 
029B: 36 11           LD      (HL),$11            ; 
029D: CD 7A 03        CALL    $037A               ; {}
02A0: 18 03           JR      $2A5                ; {}
02A2: 32 D1 9A        LD      ($9AD1),A           ; 
02A5: 3A AD 9A        LD      A,($9AAD)           ; 
02A8: A7              AND     A                   ; 
02A9: 28 08           JR      Z,$2B3              ; {}
02AB: 21 74 9A        LD      HL,$9A74            ; 
02AE: 36 0D           LD      (HL),$0D            ; 
02B0: CD A7 04        CALL    $04A7               ; {}
02B3: 3A AE 9A        LD      A,($9AAE)           ; 
02B6: A7              AND     A                   ; 
02B7: 28 12           JR      Z,$2CB              ; {}
02B9: 21 74 9A        LD      HL,$9A74            ; 
02BC: 36 0E           LD      (HL),$0E            ; 
02BE: CD A7 04        CALL    $04A7               ; {}
02C1: 3E 09           LD      A,$09               ; 
02C3: 32 6A 9A        LD      ($9A6A),A           ; 
02C6: 3E 06           LD      A,$06               ; 
02C8: 32 6F 9A        LD      ($9A6F),A           ; 
02CB: 3A B4 9A        LD      A,($9AB4)           ; 
02CE: A7              AND     A                   ; 
02CF: 28 08           JR      Z,$2D9              ; {}
02D1: 21 74 9A        LD      HL,$9A74            ; 
02D4: 36 14           LD      (HL),$14            ; 
02D6: CD A7 04        CALL    $04A7               ; {}
02D9: 3A B5 9A        LD      A,($9AB5)           ; 
02DC: A7              AND     A                   ; 
02DD: 28 08           JR      Z,$2E7              ; {}
02DF: 21 74 9A        LD      HL,$9A74            ; 
02E2: 36 15           LD      (HL),$15            ; 
02E4: CD A7 04        CALL    $04A7               ; {}
02E7: 3A AA 9A        LD      A,($9AAA)           ; 
02EA: A7              AND     A                   ; 
02EB: 28 08           JR      Z,$2F5              ; {}
02ED: 21 74 9A        LD      HL,$9A74            ; 
02F0: 36 0A           LD      (HL),$0A            ; 
02F2: CD A7 04        CALL    $04A7               ; {}
02F5: 3A AB 9A        LD      A,($9AAB)           ; 
02F8: A7              AND     A                   ; 
02F9: 28 08           JR      Z,$303              ; {}
02FB: 21 74 9A        LD      HL,$9A74            ; 
02FE: 36 0B           LD      (HL),$0B            ; 
0300: CD A7 04        CALL    $04A7               ; {}
0303: 3A B0 9A        LD      A,($9AB0)           ; 
0306: A7              AND     A                   ; 
0307: 28 0A           JR      Z,$313              ; {}
0309: 21 74 9A        LD      HL,$9A74            ; 
030C: 36 10           LD      (HL),$10            ; 
030E: CD 7A 03        CALL    $037A               ; {}
0311: 18 03           JR      $316                ; {}
0313: 32 D0 9A        LD      ($9AD0),A           ; 
0316: 3A AC 9A        LD      A,($9AAC)           ; 
0319: A7              AND     A                   ; 
031A: 28 08           JR      Z,$324              ; {}
031C: 21 74 9A        LD      HL,$9A74            ; 
031F: 36 0C           LD      (HL),$0C            ; 
0321: CD A7 04        CALL    $04A7               ; {}
0324: 3A B6 9A        LD      A,($9AB6)           ; 
0327: A7              AND     A                   ; 
0328: 28 08           JR      Z,$332              ; {}
032A: 21 74 9A        LD      HL,$9A74            ; 
032D: 36 16           LD      (HL),$16            ; 
032F: CD A7 04        CALL    $04A7               ; {}
0332: 3A A8 9A        LD      A,($9AA8)           ; 
0335: A7              AND     A                   ; 
0336: 28 08           JR      Z,$340              ; {}
0338: 21 74 9A        LD      HL,$9A74            ; 
033B: 36 08           LD      (HL),$08            ; 
033D: CD A7 04        CALL    $04A7               ; {}
0340: 18 1A           JR      $35C                ; {} Skip clears

0342: 21 A0 9A        LD      HL,$9AA0            ; Clear from ...
0345: 36 00           LD      (HL),$00            ; ... 9AA0 ...
0347: 11 A1 9A        LD      DE,$9AA1            ; ... to ...
034A: 01 15 00        LD      BC,$0015            ; ... 9AB5 ...
034D: ED B0           LDIR                        ; .

034F: 21 C0 9A        LD      HL,$9AC0            ; Clear from ...
0352: 36 00           LD      (HL),$00            ; ... 9AC0 ...
0354: 11 C1 9A        LD      DE,$9AC1            ; ... to ...
0357: 01 16 00        LD      BC,$0016            ; ... 9AD6
035A: ED B0           LDIR                        ; .

035C: 21 60 9A        LD      HL,$9A60            ; Sound chip mirror
035F: 11 10 68        LD      DE,$6810            ; Sound chip pointer
0362: 01 10 00        LD      BC,$0010            ; 16 Bytes of sound data
0365: ED B0           LDIR                        ; Set sound info
0367: 3A 70 9A        LD      A,($9A70)           ; From memory
036A: 32 05 68        LD      ($6805),A           ; Sound voice 1 waveform
036D: 3A 71 9A        LD      A,($9A71)           ; From memory
0370: 32 0A 68        LD      ($680A),A           ; Sound voice 1 waveform
0373: 3A 72 9A        LD      A,($9A72)           ; From memory
0376: 32 0F 68        LD      ($680F),A           ; Sound voice 1 waveform
0379: C9              RET                         ; Done
037A: 21 74 9A        LD      HL,$9A74            ; 
037D: 7E              LD      A,(HL)              ; 
037E: 87              ADD     A,A                 ; 
037F: 86              ADD     A,(HL)              ; 
0380: 21 2A 07        LD      HL,$072A            ; 
0383: D7              RST     0X10                ; 
0384: 11 75 9A        LD      DE,$9A75            ; 
0387: 01 03 00        LD      BC,$0003            ; 
038A: ED B0           LDIR                        ; 
038C: 3A 74 9A        LD      A,($9A74)           ; 
038F: FE 0E           CP      $0E                 ; 
0391: 20 18           JR      NZ,$3AB             ; {}
0393: 3A 4C 9A        LD      A,($9A4C)           ; 
0396: A7              AND     A                   ; 
0397: 28 0D           JR      Z,$3A6              ; {}
0399: 3D              DEC     A                   ; 
039A: 28 06           JR      Z,$3A2              ; {}
039C: 3A 4D 9A        LD      A,($9A4D)           ; 
039F: A7              AND     A                   ; 
03A0: 20 09           JR      NZ,$3AB             ; {}
03A2: 3E 02           LD      A,$02               ; 
03A4: 18 02           JR      $3A8                ; {}
03A6: 3E 01           LD      A,$01               ; 
03A8: 32 76 9A        LD      ($9A76),A           ; 
03AB: 21 C0 9A        LD      HL,$9AC0            ; 
03AE: 3A 74 9A        LD      A,($9A74)           ; 
03B1: 85              ADD     A,L                 ; 
03B2: 6F              LD      L,A                 ; 
03B3: 7E              LD      A,(HL)              ; 
03B4: A7              AND     A                   ; 
03B5: 20 1B           JR      NZ,$3D2             ; {}
03B7: 34              INC     (HL)                ; 
03B8: 21 76 9A        LD      HL,$9A76            ; 
03BB: 46              LD      B,(HL)              ; 
03BC: 48              LD      C,B                 ; 
03BD: 21 30 9A        LD      HL,$9A30            ; 
03C0: 3A 75 9A        LD      A,($9A75)           ; 
03C3: 85              ADD     A,L                 ; 
03C4: 6F              LD      L,A                 ; 
03C5: AF              XOR     A                   ; 
03C6: DF              RST     0X18                ; 
03C7: 41              LD      B,C                 ; 
03C8: 21 00 9A        LD      HL,$9A00            ; 
03CB: 3A 75 9A        LD      A,($9A75)           ; 
03CE: 85              ADD     A,L                 ; 
03CF: 6F              LD      L,A                 ; 
03D0: AF              XOR     A                   ; 
03D1: DF              RST     0X18                ; 
03D2: CD 77 05        CALL    $0577               ; {}
03D5: 21 76 9A        LD      HL,$9A76            ; 
03D8: 35              DEC     (HL)                ; 
03D9: 28 0A           JR      Z,$3E5              ; {}
03DB: 21 75 9A        LD      HL,$9A75            ; 
03DE: 34              INC     (HL)                ; 
03DF: 21 77 9A        LD      HL,$9A77            ; 
03E2: 34              INC     (HL)                ; 
03E3: 18 ED           JR      $3D2                ; {}
03E5: 3A 78 9A        LD      A,($9A78)           ; 
03E8: A7              AND     A                   ; 
03E9: C8              RET     Z                   ; 
03EA: AF              XOR     A                   ; 
03EB: 32 78 9A        LD      ($9A78),A           ; 
03EE: 21 C0 9A        LD      HL,$9AC0            ; 
03F1: 3A 74 9A        LD      A,($9A74)           ; 
03F4: 85              ADD     A,L                 ; 
03F5: 6F              LD      L,A                 ; 
03F6: 36 00           LD      (HL),$00            ; 
03F8: C9              RET                         ; 
03F9: 21 C0 9A        LD      HL,$9AC0            ; 
03FC: 3A 74 9A        LD      A,($9A74)           ; 
03FF: 85              ADD     A,L                 ; 
0400: 6F              LD      L,A                 ; 
0401: 34              INC     (HL)                ; 
0402: 21 74 9A        LD      HL,$9A74            ; 
0405: 7E              LD      A,(HL)              ; 
0406: 87              ADD     A,A                 ; 
0407: 86              ADD     A,(HL)              ; 
0408: 21 2A 07        LD      HL,$072A            ; 
040B: D7              RST     0X10                ; 
040C: 11 75 9A        LD      DE,$9A75            ; 
040F: 01 03 00        LD      BC,$0003            ; 
0412: ED B0           LDIR                        ; 
0414: 3A 74 9A        LD      A,($9A74)           ; 
0417: FE 0E           CP      $0E                 ; 
0419: 20 18           JR      NZ,$433             ; {}
041B: 3A 4C 9A        LD      A,($9A4C)           ; 
041E: A7              AND     A                   ; 
041F: 28 0D           JR      Z,$42E              ; {}
0421: 3D              DEC     A                   ; 
0422: 28 06           JR      Z,$42A              ; {}
0424: 3A 4D 9A        LD      A,($9A4D)           ; 
0427: A7              AND     A                   ; 
0428: 20 09           JR      NZ,$433             ; {}
042A: 3E 02           LD      A,$02               ; 
042C: 18 02           JR      $430                ; {}
042E: 3E 01           LD      A,$01               ; 
0430: 32 76 9A        LD      ($9A76),A           ; 
0433: 21 76 9A        LD      HL,$9A76            ; 
0436: 46              LD      B,(HL)              ; 
0437: 48              LD      C,B                 ; 
0438: 21 30 9A        LD      HL,$9A30            ; 
043B: 3A 75 9A        LD      A,($9A75)           ; 
043E: 85              ADD     A,L                 ; 
043F: 6F              LD      L,A                 ; 
0440: AF              XOR     A                   ; 
0441: DF              RST     0X18                ; 
0442: 41              LD      B,C                 ; 
0443: 21 00 9A        LD      HL,$9A00            ; 
0446: 3A 75 9A        LD      A,($9A75)           ; 
0449: 85              ADD     A,L                 ; 
044A: 6F              LD      L,A                 ; 
044B: AF              XOR     A                   ; 
044C: DF              RST     0X18                ; 
044D: 18 31           JR      $480                ; {}
044F: 21 74 9A        LD      HL,$9A74            ; 
0452: 7E              LD      A,(HL)              ; 
0453: 87              ADD     A,A                 ; 
0454: 86              ADD     A,(HL)              ; 
0455: 21 2A 07        LD      HL,$072A            ; 
0458: D7              RST     0X10                ; 
0459: 11 75 9A        LD      DE,$9A75            ; 
045C: 01 03 00        LD      BC,$0003            ; 
045F: ED B0           LDIR                        ; 
0461: 3A 74 9A        LD      A,($9A74)           ; 
0464: FE 0E           CP      $0E                 ; 
0466: 20 18           JR      NZ,$480             ; {}
0468: 3A 4C 9A        LD      A,($9A4C)           ; 
046B: A7              AND     A                   ; 
046C: 28 0D           JR      Z,$47B              ; {}
046E: 3D              DEC     A                   ; 
046F: 28 06           JR      Z,$477              ; {}
0471: 3A 4D 9A        LD      A,($9A4D)           ; 
0474: A7              AND     A                   ; 
0475: 20 09           JR      NZ,$480             ; {}
0477: 3E 02           LD      A,$02               ; 
0479: 18 02           JR      $47D                ; {}
047B: 3E 01           LD      A,$01               ; 
047D: 32 76 9A        LD      ($9A76),A           ; 
0480: CD 77 05        CALL    $0577               ; {}
0483: 21 76 9A        LD      HL,$9A76            ; 
0486: 35              DEC     (HL)                ; 
0487: 28 0A           JR      Z,$493              ; {}
0489: 21 75 9A        LD      HL,$9A75            ; 
048C: 34              INC     (HL)                ; 
048D: 21 77 9A        LD      HL,$9A77            ; 
0490: 34              INC     (HL)                ; 
0491: 18 ED           JR      $480                ; {}
0493: 3A 78 9A        LD      A,($9A78)           ; 
0496: A7              AND     A                   ; 
0497: C8              RET     Z                   ; 
0498: AF              XOR     A                   ; 
0499: 32 78 9A        LD      ($9A78),A           ; 
049C: 21 C0 9A        LD      HL,$9AC0            ; 
049F: 3A 74 9A        LD      A,($9A74)           ; 
04A2: 85              ADD     A,L                 ; 
04A3: 6F              LD      L,A                 ; 
04A4: 36 00           LD      (HL),$00            ; 
04A6: C9              RET                         ; 

04A7: 21 74 9A        LD      HL,$9A74            ; 
04AA: 7E              LD      A,(HL)              ; 
04AB: 87              ADD     A,A                 ; 
04AC: 86              ADD     A,(HL)              ; 
04AD: 21 2A 07        LD      HL,$072A            ; 
04B0: D7              RST     0X10                ; Add A to HL
04B1: 11 75 9A        LD      DE,$9A75            ; 
04B4: 01 03 00        LD      BC,$0003            ; 
04B7: ED B0           LDIR                        ; 
04B9: 3A 74 9A        LD      A,($9A74)           ; 
04BC: FE 0E           CP      $0E                 ; 
04BE: 20 18           JR      NZ,$4D8             ; {}
04C0: 3A 4C 9A        LD      A,($9A4C)           ; 
04C3: A7              AND     A                   ; 
04C4: 28 0D           JR      Z,$4D3              ; {}
04C6: 3D              DEC     A                   ; 
04C7: 28 06           JR      Z,$4CF              ; {}
04C9: 3A 4D 9A        LD      A,($9A4D)           ; 
04CC: A7              AND     A                   ; 
04CD: 20 09           JR      NZ,$4D8             ; {}
04CF: 3E 02           LD      A,$02               ; 
04D1: 18 02           JR      $4D5                ; {}
04D3: 3E 01           LD      A,$01               ; 
04D5: 32 76 9A        LD      ($9A76),A           ; 
04D8: 21 C0 9A        LD      HL,$9AC0            ; 
04DB: 3A 74 9A        LD      A,($9A74)           ; 
04DE: 85              ADD     A,L                 ; 
04DF: 6F              LD      L,A                 ; 
04E0: 7E              LD      A,(HL)              ; 
04E1: A7              AND     A                   ; 
04E2: 20 1B           JR      NZ,$4FF             ; {}
04E4: 34              INC     (HL)                ; 
04E5: 21 76 9A        LD      HL,$9A76            ; 
04E8: 46              LD      B,(HL)              ; 
04E9: 48              LD      C,B                 ; 
04EA: 21 30 9A        LD      HL,$9A30            ; 
04ED: 3A 75 9A        LD      A,($9A75)           ; 
04F0: 85              ADD     A,L                 ; 
04F1: 6F              LD      L,A                 ; 
04F2: AF              XOR     A                   ; 
04F3: DF              RST     0X18                ; 
04F4: 41              LD      B,C                 ; 
04F5: 21 00 9A        LD      HL,$9A00            ; 
04F8: 3A 75 9A        LD      A,($9A75)           ; 
04FB: 85              ADD     A,L                 ; 
04FC: 6F              LD      L,A                 ; 
04FD: AF              XOR     A                   ; 
04FE: DF              RST     0X18                ; 
04FF: CD 77 05        CALL    $0577               ; {}
0502: 21 76 9A        LD      HL,$9A76            ; 
0505: 35              DEC     (HL)                ; 
0506: 28 0A           JR      Z,$512              ; {}
0508: 21 75 9A        LD      HL,$9A75            ; 
050B: 34              INC     (HL)                ; 
050C: 21 77 9A        LD      HL,$9A77            ; 
050F: 34              INC     (HL)                ; 
0510: 18 ED           JR      $4FF                ; {}
0512: 3A 78 9A        LD      A,($9A78)           ; 
0515: A7              AND     A                   ; 
0516: C8              RET     Z                   ; 
0517: AF              XOR     A                   ; 
0518: 32 78 9A        LD      ($9A78),A           ; 
051B: 21 C0 9A        LD      HL,$9AC0            ; 
051E: 3A 74 9A        LD      A,($9A74)           ; 
0521: 85              ADD     A,L                 ; 
0522: 6F              LD      L,A                 ; 
0523: 36 00           LD      (HL),$00            ; 
0525: 21 A0 9A        LD      HL,$9AA0            ; 
0528: 3A 74 9A        LD      A,($9A74)           ; 
052B: 85              ADD     A,L                 ; 
052C: 6F              LD      L,A                 ; 
052D: 3A 74 9A        LD      A,($9A74)           ; 
0530: FE 08           CP      $08                 ; 
0532: 28 0F           JR      Z,$543              ; {}
0534: FE 0C           CP      $0C                 ; 
0536: 28 0D           JR      Z,$545              ; {}
0538: FE 14           CP      $14                 ; 
053A: 28 15           JR      Z,$551              ; {}
053C: FE 07           CP      $07                 ; 
053E: 28 19           JR      Z,$559              ; {}
0540: 36 00           LD      (HL),$00            ; 
0542: C9              RET                         ; 
0543: 35              DEC     (HL)                ; 
0544: C9              RET                         ; 
0545: 35              DEC     (HL)                ; 
0546: 28 03           JR      Z,$54B              ; {}
0548: CB 46           BIT     0,(HL)              ; 
054A: C8              RET     Z                   ; 
054B: 3E 01           LD      A,$01               ; 
054D: 32 B6 9A        LD      ($9AB6),A           ; 
0550: C9              RET                         ; 
0551: 36 00           LD      (HL),$00            ; 
0553: 21 B3 9A        LD      HL,$9AB3            ; 
0556: 36 01           LD      (HL),$01            ; 
0558: C9              RET                         ; 
0559: 36 00           LD      (HL),$00            ; 
055B: 21 A0 9A        LD      HL,$9AA0            ; 
055E: AF              XOR     A                   ; 
055F: 06 08           LD      B,$08               ; 
0561: DF              RST     0X18                ; 
0562: 23              INC     HL                  ; 
0563: 77              LD      (HL),A              ; 
0564: 23              INC     HL                  ; 
0565: 23              INC     HL                  ; 
0566: 06 0C           LD      B,$0C               ; 
0568: DF              RST     0X18                ; 
0569: 21 C0 9A        LD      HL,$9AC0            ; 
056C: 06 08           LD      B,$08               ; 
056E: DF              RST     0X18                ; 
056F: 23              INC     HL                  ; 
0570: 77              LD      (HL),A              ; 
0571: 23              INC     HL                  ; 
0572: 23              INC     HL                  ; 
0573: 06 0C           LD      B,$0C               ; 
0575: DF              RST     0X18                ; 
0576: C9              RET                         ; 
0577: 21 00 9A        LD      HL,$9A00            ; 
057A: 3A 75 9A        LD      A,($9A75)           ; 
057D: 85              ADD     A,L                 ; 
057E: 6F              LD      L,A                 ; 
057F: 34              INC     (HL)                ; 
0580: 3A 75 9A        LD      A,($9A75)           ; 
0583: 21 6F 07        LD      HL,$076F            ; 
0586: CF              RST     0X08                ; 
0587: 5E              LD      E,(HL)              ; 
0588: 23              INC     HL                  ; 
0589: 56              LD      D,(HL)              ; 
058A: EB              EX      DE,HL               ; 
058B: 11 88 9A        LD      DE,$9A88            ; 
058E: 01 03 00        LD      BC,$0003            ; 
0591: ED B0           LDIR                        ; 
0593: EB              EX      DE,HL               ; 
0594: 21 30 9A        LD      HL,$9A30            ; 
0597: 3A 75 9A        LD      A,($9A75)           ; 
059A: 85              ADD     A,L                 ; 
059B: 6F              LD      L,A                 ; 
059C: 7E              LD      A,(HL)              ; 
059D: EB              EX      DE,HL               ; 
059E: D7              RST     0X10                ; 
059F: 22 7A 9A        LD      ($9A7A),HL          ; 
05A2: 7E              LD      A,(HL)              ; 
05A3: 3C              INC     A                   ; 
05A4: CA B2 06        JP      Z,$06B2             ; {}
05A7: 11 D0 06        LD      DE,$06D0            ; 
05AA: 2A 7A 9A        LD      HL,($9A7A)          ; 
05AD: 7E              LD      A,(HL)              ; 
05AE: E6 0F           AND     $0F                 ; 
05B0: EB              EX      DE,HL               ; 
05B1: CF              RST     0X08                ; 
05B2: 4E              LD      C,(HL)              ; 
05B3: 23              INC     HL                  ; 
05B4: 46              LD      B,(HL)              ; 
05B5: EB              EX      DE,HL               ; 
05B6: 7E              LD      A,(HL)              ; 
05B7: 0F              RRCA                        ; 
05B8: 0F              RRCA                        ; 
05B9: 0F              RRCA                        ; 
05BA: 0F              RRCA                        ; 
05BB: E6 0F           AND     $0F                 ; 
05BD: 28 07           JR      Z,$5C6              ; {}
05BF: CB 38           SRL     B                   ; 
05C1: CB 19           RR      C                   ; 
05C3: 3D              DEC     A                   ; 
05C4: 20 F9           JR      NZ,$5BF             ; {}
05C6: 3A 77 9A        LD      A,($9A77)           ; 
05C9: A7              AND     A                   ; 
05CA: 28 0D           JR      Z,$5D9              ; {}
05CC: 3D              DEC     A                   ; 
05CD: 28 05           JR      Z,$5D4              ; {}
05CF: 21 6B 9A        LD      HL,$9A6B            ; 
05D2: 18 08           JR      $5DC                ; {}
05D4: 21 66 9A        LD      HL,$9A66            ; 
05D7: 18 03           JR      $5DC                ; {}
05D9: 21 61 9A        LD      HL,$9A61            ; 
05DC: 71              LD      (HL),C              ; 
05DD: 7E              LD      A,(HL)              ; 
05DE: 0F              RRCA                        ; 
05DF: 0F              RRCA                        ; 
05E0: 0F              RRCA                        ; 
05E1: 0F              RRCA                        ; 
05E2: 23              INC     HL                  ; 
05E3: 77              LD      (HL),A              ; 
05E4: 23              INC     HL                  ; 
05E5: 70              LD      (HL),B              ; 
05E6: 7E              LD      A,(HL)              ; 
05E7: 0F              RRCA                        ; 
05E8: 0F              RRCA                        ; 
05E9: 0F              RRCA                        ; 
05EA: 0F              RRCA                        ; 
05EB: 23              INC     HL                  ; 
05EC: 77              LD      (HL),A              ; 
05ED: 3A 77 9A        LD      A,($9A77)           ; 
05F0: A7              AND     A                   ; 
05F1: 28 0D           JR      Z,$600              ; {}
05F3: 3D              DEC     A                   ; 
05F4: 28 05           JR      Z,$5FB              ; {}
05F6: 11 6F 9A        LD      DE,$9A6F            ; 
05F9: 18 08           JR      $603                ; {}
05FB: 11 6A 9A        LD      DE,$9A6A            ; 
05FE: 18 03           JR      $603                ; {}
0600: 11 65 9A        LD      DE,$9A65            ; 
0603: 2A 7A 9A        LD      HL,($9A7A)          ; 
0606: 7E              LD      A,(HL)              ; 
0607: D6 0C           SUB     $0C                 ; 
0609: 28 44           JR      Z,$64F              ; {}
060B: 3A 88 9A        LD      A,($9A88)           ; 
060E: A7              AND     A                   ; 
060F: 28 23           JR      Z,$634              ; {}
0611: 3D              DEC     A                   ; 
0612: 28 10           JR      Z,$624              ; {}
0614: 21 00 9A        LD      HL,$9A00            ; 
0617: 3A 75 9A        LD      A,($9A75)           ; 
061A: 85              ADD     A,L                 ; 
061B: 6F              LD      L,A                 ; 
061C: 7E              LD      A,(HL)              ; 
061D: FE 06           CP      $06                 ; 
061F: 30 13           JR      NC,$634             ; {}
0621: 2F              CPL                         ; 
0622: 18 30           JR      $654                ; {}
0624: 21 00 9A        LD      HL,$9A00            ; 
0627: 3A 75 9A        LD      A,($9A75)           ; 
062A: 85              ADD     A,L                 ; 
062B: 6F              LD      L,A                 ; 
062C: 7E              LD      A,(HL)              ; 
062D: FE 06           CP      $06                 ; 
062F: 30 03           JR      NC,$634             ; {}
0631: 87              ADD     A,A                 ; 
0632: 18 20           JR      $654                ; {}
0634: 3A 89 9A        LD      A,($9A89)           ; 
0637: A7              AND     A                   ; 
0638: 28 18           JR      Z,$652              ; {}
063A: 47              LD      B,A                 ; 
063B: 21 00 9A        LD      HL,$9A00            ; 
063E: 3A 75 9A        LD      A,($9A75)           ; 
0641: 85              ADD     A,L                 ; 
0642: 6F              LD      L,A                 ; 
0643: 7E              LD      A,(HL)              ; 
0644: 90              SUB     B                   ; 
0645: 38 0B           JR      C,$652              ; {}
0647: D6 0A           SUB     $0A                 ; 
0649: 30 04           JR      NC,$64F             ; {}
064B: ED 44           NEG                         ; 
064D: 18 05           JR      $654                ; {}
064F: AF              XOR     A                   ; 
0650: 18 02           JR      $654                ; {}
0652: 3E 0A           LD      A,$0A               ; 
0654: 12              LD      (DE),A              ; 
0655: 21 70 9A        LD      HL,$9A70            ; 
0658: 3A 77 9A        LD      A,($9A77)           ; 
065B: 85              ADD     A,L                 ; 
065C: 6F              LD      L,A                 ; 
065D: 3A 8A 9A        LD      A,($9A8A)           ; 
0660: 77              LD      (HL),A              ; 
0661: 21 CD 07        LD      HL,$07CD            ; 
0664: 3A 74 9A        LD      A,($9A74)           ; 
0667: D7              RST     0X10                ; 
0668: 7E              LD      A,(HL)              ; 
0669: 2A 7A 9A        LD      HL,($9A7A)          ; 
066C: 23              INC     HL                  ; 
066D: 5E              LD      E,(HL)              ; 
066E: 16 00           LD      D,$00               ; 
0670: 21 00 00        LD      HL,$0000            ; 
0673: 06 08           LD      B,$08               ; 
0675: CB 3F           SRL     A                   ; 
0677: 30 01           JR      NC,$67A             ; {}
0679: 19              ADD     HL,DE               ; 
067A: CB 23           SLA     E                   ; 
067C: CB 12           RL      D                   ; 
067E: 10 F5           DJNZ    $675                ; {}
0680: 45              LD      B,L                 ; 
0681: 21 00 9A        LD      HL,$9A00            ; 
0684: 3A 75 9A        LD      A,($9A75)           ; 
0687: 85              ADD     A,L                 ; 
0688: 6F              LD      L,A                 ; 
0689: 78              LD      A,B                 ; 
068A: BE              CP      (HL)                ; 
068B: C0              RET     NZ                  ; 
068C: 21 30 9A        LD      HL,$9A30            ; 
068F: 3A 75 9A        LD      A,($9A75)           ; 
0692: 85              ADD     A,L                 ; 
0693: 6F              LD      L,A                 ; 
0694: 34              INC     (HL)                ; 
0695: 34              INC     (HL)                ; 
0696: 21 00 9A        LD      HL,$9A00            ; 
0699: 3A 75 9A        LD      A,($9A75)           ; 
069C: 85              ADD     A,L                 ; 
069D: 6F              LD      L,A                 ; 
069E: 36 00           LD      (HL),$00            ; 
06A0: C9              RET                         ; 

06A1: 21 00 9A        LD      HL,$9A00            ; Clear
06A4: 36 00           LD      (HL),$00            ; 
06A6: 11 01 9A        LD      DE,$9A01            ; 
06A9: 01 FF 00        LD      BC,$00FF            ; 
06AC: ED B0           LDIR                        ; 
06AE: 31 00 9B        LD      SP,$9B00            ; 
06B1: C9              RET                         ; 

06B2: 3A 77 9A        LD      A,($9A77)           ; 
06B5: A7              AND     A                   ; 
06B6: 28 0D           JR      Z,$6C5              ; {}
06B8: 3D              DEC     A                   ; 
06B9: 28 05           JR      Z,$6C0              ; {}
06BB: 21 6F 9A        LD      HL,$9A6F            ; 
06BE: 18 08           JR      $6C8                ; {}
06C0: 21 6A 9A        LD      HL,$9A6A            ; 
06C3: 18 03           JR      $6C8                ; {}
06C5: 21 65 9A        LD      HL,$9A65            ; 
06C8: 36 00           LD      (HL),$00            ; 
06CA: 3E 01           LD      A,$01               ; 
06CC: 32 78 9A        LD      ($9A78),A           ; 
06CF: C9              RET                         ; 
06D0: 50              LD      D,B                 ; 
06D1: 81              ADD     A,C                 ; 
06D2: 00              NOP                         ; 
06D3: 89              ADC     A,C                 ; 
06D4: 26 91           LD      H,$91               ; 
06D6: C8              RET     Z                   ; 
06D7: 99              SBC     C                   ; 
06D8: EC A2 9D        CALL    PE,$9DA2            ; 
06DB: AC              XOR     H                   ; 
06DC: E0              RET     PO                  ; 
06DD: B6              OR      (HL)                ; 
06DE: C0              RET     NZ                  ; 
06DF: C1              POP     BC                  ; 
06E0: 45              LD      B,L                 ; 
06E1: CD 7A D9        CALL    $D97A               ; 
06E4: 69              LD      L,C                 ; 
06E5: E6 1C           AND     $1C                 ; 
06E7: F4 00 00        CALL    P,$0000             ; {}
06EA: 30 01           JR      NC,$6ED             ; {}
06EC: 68              LD      L,B                 ; 
06ED: 01 36 01        LD      BC,$0136            ; 
06F0: A8              XOR     B                   ; 
06F1: 01 68 01        LD      BC,$0168            ; 
06F4: 00              NOP                         ; 
06F5: 02              LD      (BC),A              ; 
06F6: AC              XOR     H                   ; 
06F7: 01 08 02        LD      BC,$0208            ; 
06FA: 00              NOP                         ; 
06FB: FE 58           CP      $58                 ; 
06FD: FE 08           CP      $08                 ; 
06FF: FE 98           CP      $98                 ; 
0701: FE 58           CP      $58                 ; 
0703: FE D0           CP      $D0                 ; 
0705: FE 98           CP      $98                 ; 
0707: FE D6           CP      $D6                 ; 
0709: FE 00           CP      $00                 ; 
070B: 5B              LD      E,E                 ; 
070C: 00              NOP                         ; 
070D: 6C              LD      L,H                 ; 
070E: 00              NOP                         ; 
070F: 5B              LD      E,E                 ; 
0710: 00              NOP                         ; 
0711: 7E              LD      A,(HL)              ; 
0712: 00              NOP                         ; 
0713: 6C              LD      L,H                 ; 
0714: 00              NOP                         ; 
0715: 97              SUB     A                   ; 
0716: 00              NOP                         ; 
0717: 81              ADD     A,C                 ; 
0718: 00              NOP                         ; 
0719: 99              SBC     C                   ; 
071A: 00              NOP                         ; 
071B: D9              EXX                         ; 
071C: 00              NOP                         ; 
071D: B6              OR      (HL)                ; 
071E: 00              NOP                         ; 
071F: D9              EXX                         ; 
0720: 00              NOP                         ; 
0721: 97              SUB     A                   ; 
0722: 00              NOP                         ; 
0723: B6              OR      (HL)                ; 
0724: 00              NOP                         ; 
0725: 7E              LD      A,(HL)              ; 
0726: 00              NOP                         ; 
0727: 99              SBC     C                   ; 
0728: 00              NOP                         ; 
0729: 81              ADD     A,C                 ; 
072A: 00              NOP                         ; 
072B: 01 00 01        LD      BC,$0100            ; 
072E: 01 01 02        LD      BC,$0201            ; 
0731: 01 01 03        LD      BC,$0301            ; 
0734: 01 01 04        LD      BC,$0401            ; 
0737: 01 01 05        LD      BC,$0501            ; 
073A: 01 00 06        LD      BC,$0600            ; 
073D: 01 00 20        LD      BC,$2000            ; 
0740: 03              INC     BC                  ; 
0741: 00              NOP                         ; 
0742: 0A              LD      A,(BC)              ; 
0743: 03              INC     BC                  ; 
0744: 00              NOP                         ; 
0745: 0D              DEC     C                   ; 
0746: 03              INC     BC                  ; 
0747: 00              NOP                         ; 
0748: 07              RLCA                        ; 
0749: 03              INC     BC                  ; 
074A: 00              NOP                         ; 
074B: 13              INC     DE                  ; 
074C: 03              INC     BC                  ; 
074D: 00              NOP                         ; 
074E: 16 03           LD      D,$03               ; 
0750: 00              NOP                         ; 
0751: 19              ADD     HL,DE               ; 
0752: 03              INC     BC                  ; 
0753: 00              NOP                         ; 
0754: 1C              INC     E                   ; 
0755: 03              INC     BC                  ; 
0756: 00              NOP                         ; 
0757: 1F              RRA                         ; 
0758: 01 02 2C        LD      BC,$2C02            ; 
075B: 03              INC     BC                  ; 
075C: 00              NOP                         ; 
075D: 10 03           DJNZ    $762                ; {}
075F: 00              NOP                         ; 
0760: 23              INC     HL                  ; 
0761: 01 00 24        LD      BC,$2400            ; 
0764: 01 00 25        LD      BC,$2500            ; 
0767: 03              INC     BC                  ; 
0768: 00              NOP                         ; 
0769: 28 01           JR      Z,$76C              ; {}
076B: 00              NOP                         ; 
076C: 29              ADD     HL,HL               ; 
076D: 03              INC     BC                  ; 
076E: 00              NOP                         ; 
076F: E4 07 3B        CALL    PO,$3B07            ; 
0772: 08              EX      AF,AF'              ; 
0773: 19              ADD     HL,DE               ; 
0774: 08              EX      AF,AF'              ; 
0775: E5              PUSH    HL                  ; 
0776: 07              RLCA                        ; 
0777: 85              ADD     A,L                 ; 
0778: 08              EX      AF,AF'              ; 
0779: 9F              SBC     A                   ; 
077A: 08              EX      AF,AF'              ; 
077B: B3              OR      E                   ; 
077C: 08              EX      AF,AF'              ; 
077D: F9              LD      SP,HL               ; 
077E: 09              ADD     HL,BC               ; 
077F: 09              ADD     HL,BC               ; 
0780: 0A              LD      A,(BC)              ; 
0781: 19              ADD     HL,DE               ; 
0782: 0A              LD      A,(BC)              ; 
0783: C3 09 D5        JP      $D509               ; 
0786: 09              ADD     HL,BC               ; 
0787: E7              RST     0X20                ; 
0788: 09              ADD     HL,BC               ; 
0789: 29              ADD     HL,HL               ; 
078A: 0A              LD      A,(BC)              ; 
078B: 6D              LD      L,L                 ; 
078C: 0A              LD      A,(BC)              ; 
078D: B1              OR      C                   ; 
078E: 0A              LD      A,(BC)              ; 
078F: DD 0A           LD      A,(BC)              ; 
0791: 21 0B 65        LD      HL,$650B            ; 
0794: 0B              DEC     BC                  ; 
0795: C7              RST     0X00                ; 
0796: 08              EX      AF,AF'              ; 
0797: 13              INC     DE                  ; 
0798: 09              ADD     HL,BC               ; 
0799: 5D              LD      E,L                 ; 
079A: 09              ADD     HL,BC               ; 
079B: 83              ADD     A,E                 ; 
079C: 0C              INC     C                   ; 
079D: 11 0D 5F        LD      DE,$5F0D            ; 
07A0: 0D              DEC     C                   ; 
07A1: 8D              ADC     A,L                 ; 
07A2: 09              ADD     HL,BC               ; 
07A3: 9F              SBC     A                   ; 
07A4: 09              ADD     HL,BC               ; 
07A5: B1              OR      C                   ; 
07A6: 09              ADD     HL,BC               ; 
07A7: C7              RST     0X00                ; 
07A8: 08              EX      AF,AF'              ; 
07A9: C7              RST     0X00                ; 
07AA: 08              EX      AF,AF'              ; 
07AB: C7              RST     0X00                ; 
07AC: 08              EX      AF,AF'              ; 
07AD: 2F              CPL                         ; 
07AE: 0C              INC     C                   ; 
07AF: 91              SUB     C                   ; 
07B0: 0B              DEC     BC                  ; 
07B1: C7              RST     0X00                ; 
07B2: 0B              DEC     BC                  ; 
07B3: FD 0B           DEC     BC                  ; 
07B5: 1B              DEC     DE                  ; 
07B6: 0C              INC     C                   ; 
07B7: 2F              CPL                         ; 
07B8: 0C              INC     C                   ; 
07B9: 93              SUB     E                   ; 
07BA: 0D              DEC     C                   ; 
07BB: 07              RLCA                        ; 
07BC: 0E 83           LD      C,$83               ; 
07BE: 0E 85           LD      C,$85               ; 
07C0: 0D              DEC     C                   ; 
07C1: 07              RLCA                        ; 
07C2: 0D              DEC     C                   ; 
07C3: 55              LD      D,L                 ; 
07C4: 0D              DEC     C                   ; 
07C5: 7B              LD      A,E                 ; 
07C6: 0D              DEC     C                   ; 
07C7: C5              PUSH    BC                  ; 
07C8: 0E 01           LD      C,$01               ; 
07CA: 0F              RRCA                        ; 
07CB: 3D              DEC     A                   ; 
07CC: 0F              RRCA                        ; 
07CD: 04              INC     B                   ; 
07CE: 02              LD      (BC),A              ; 
07CF: 02              LD      (BC),A              ; 
07D0: 02              LD      (BC),A              ; 
07D1: 02              LD      (BC),A              ; 
07D2: 04              INC     B                   ; 
07D3: 04              INC     B                   ; 
07D4: 0A              LD      A,(BC)              ; 
07D5: 07              RLCA                        ; 
07D6: 0C              INC     C                   ; 
07D7: 0B              DEC     BC                  ; 
07D8: 04              INC     B                   ; 
07D9: 0A              LD      A,(BC)              ; 
07DA: 0D              DEC     C                   ; 
07DB: 04              INC     B                   ; 
07DC: 01 04 0C        LD      BC,$0C04            ; 
07DF: 02              LD      (BC),A              ; 
07E0: 06 05           LD      B,$05               ; 
07E2: 02              LD      (BC),A              ; 
07E3: 0A              LD      A,(BC)              ; 
07E4: FF              RST     0X38                ; 
07E5: 00              NOP                         ; 
07E6: 00              NOP                         ; 
07E7: 06 71           LD      B,$71               ; 
07E9: 01 72 01        LD      BC,$0172            ; 
07EC: 73              LD      (HL),E              ; 
07ED: 01 75 01        LD      BC,$0175            ; 
07F0: 74              LD      (HL),H              ; 
07F1: 01 73 01        LD      BC,$0173            ; 
07F4: 72              LD      (HL),D              ; 
07F5: 01 71 01        LD      BC,$0171            ; 
07F8: 70              LD      (HL),B              ; 
07F9: 01 8B 01        LD      BC,$018B            ; 
07FC: 8A              ADC     A,D                 ; 
07FD: 01 0C 04        LD      BC,$040C            ; 
0800: 86              ADD     A,(HL)              ; 
0801: 01 87 01        LD      BC,$0187            ; 
0804: 88              ADC     A,B                 ; 
0805: 01 89 01        LD      BC,$0189            ; 
0808: 8A              ADC     A,D                 ; 
0809: 01 89 01        LD      BC,$0189            ; 
080C: 88              ADC     A,B                 ; 
080D: 01 87 01        LD      BC,$0187            ; 
0810: 86              ADD     A,(HL)              ; 
0811: 01 85 01        LD      BC,$0185            ; 
0814: 84              ADD     A,H                 ; 
0815: 01 83 01        LD      BC,$0183            ; 
0818: FF              RST     0X38                ; 
0819: 00              NOP                         ; 
081A: 00              NOP                         ; 
081B: 04              INC     B                   ; 
081C: 88              ADC     A,B                 ; 
081D: 01 8A 01        LD      BC,$018A            ; 
0820: 70              LD      (HL),B              ; 
0821: 01 71 01        LD      BC,$0171            ; 
0824: 73              LD      (HL),E              ; 
0825: 01 75 01        LD      BC,$0175            ; 
0828: 77              LD      (HL),A              ; 
0829: 01 78 01        LD      BC,$0178            ; 
082C: 0C              INC     C                   ; 
082D: 06 74           LD      B,$74               ; 
082F: 01 73 01        LD      BC,$0173            ; 
0832: 72              LD      (HL),D              ; 
0833: 01 71 01        LD      BC,$0171            ; 
0836: 70              LD      (HL),B              ; 
0837: 01 8B 01        LD      BC,$018B            ; 
083A: FF              RST     0X38                ; 
083B: 00              NOP                         ; 
083C: 00              NOP                         ; 
083D: 07              RLCA                        ; 
083E: 89              ADC     A,C                 ; 
083F: 01 8A 01        LD      BC,$018A            ; 
0842: 8B              ADC     A,E                 ; 
0843: 01 0C 01        LD      BC,$010C            ; 
0846: 70              LD      (HL),B              ; 
0847: 01 71 01        LD      BC,$0171            ; 
084A: 72              LD      (HL),D              ; 
084B: 01 0C 01        LD      BC,$010C            ; 
084E: 73              LD      (HL),E              ; 
084F: 01 74 01        LD      BC,$0174            ; 
0852: 75              LD      (HL),L              ; 
0853: 01 0C 03        LD      BC,$030C            ; 
0856: 8B              ADC     A,E                 ; 
0857: 01 70 01        LD      BC,$0170            ; 
085A: 71              LD      (HL),C              ; 
085B: 01 0C 01        LD      BC,$010C            ; 
085E: 72              LD      (HL),D              ; 
085F: 01 73 01        LD      BC,$0173            ; 
0862: 74              LD      (HL),H              ; 
0863: 01 0C 01        LD      BC,$010C            ; 
0866: 75              LD      (HL),L              ; 
0867: 01 76 01        LD      BC,$0176            ; 
086A: 77              LD      (HL),A              ; 
086B: 01 0C 03        LD      BC,$030C            ; 
086E: 71              LD      (HL),C              ; 
086F: 01 72 01        LD      BC,$0172            ; 
0872: 73              LD      (HL),E              ; 
0873: 01 0C 01        LD      BC,$010C            ; 
0876: 74              LD      (HL),H              ; 
0877: 01 75 01        LD      BC,$0175            ; 
087A: 76              HALT                        ; 
087B: 01 0C 01        LD      BC,$010C            ; 
087E: 77              LD      (HL),A              ; 
087F: 01 78 01        LD      BC,$0178            ; 
0882: 79              LD      A,C                 ; 
0883: 01 FF 00        LD      BC,$00FF            ; 
0886: 00              NOP                         ; 
0887: 05              DEC     B                   ; 
0888: 71              LD      (HL),C              ; 
0889: 01 72 01        LD      BC,$0172            ; 
088C: 73              LD      (HL),E              ; 
088D: 01 0C 01        LD      BC,$010C            ; 
0890: 74              LD      (HL),H              ; 
0891: 01 75 01        LD      BC,$0175            ; 
0894: 76              HALT                        ; 
0895: 01 0C 01        LD      BC,$010C            ; 
0898: 77              LD      (HL),A              ; 
0899: 01 78 01        LD      BC,$0178            ; 
089C: 79              LD      A,C                 ; 
089D: 01 FF 00        LD      BC,$00FF            ; 
08A0: 00              NOP                         ; 
08A1: 04              INC     B                   ; 
08A2: 61              LD      H,C                 ; 
08A3: 01 7A 01        LD      BC,$017A            ; 
08A6: 60              LD      H,B                 ; 
08A7: 01 78 01        LD      BC,$0178            ; 
08AA: 7A              LD      A,D                 ; 
08AB: 01 76 01        LD      BC,$0176            ; 
08AE: 78              LD      A,B                 ; 
08AF: 01 75 01        LD      BC,$0175            ; 
08B2: FF              RST     0X38                ; 
08B3: 00              NOP                         ; 
08B4: 00              NOP                         ; 
08B5: 00              NOP                         ; 
08B6: 76              HALT                        ; 
08B7: 01 79 01        LD      BC,$0179            ; 
08BA: 60              LD      H,B                 ; 
08BB: 01 63 01        LD      BC,$0163            ; 
08BE: 66              LD      H,(HL)              ; 
08BF: 01 63 01        LD      BC,$0163            ; 
08C2: 60              LD      H,B                 ; 
08C3: 01 79 01        LD      BC,$0179            ; 
08C6: FF              RST     0X38                ; 
08C7: 00              NOP                         ; 
08C8: 00              NOP                         ; 
08C9: 07              RLCA                        ; 
08CA: 81              ADD     A,C                 ; 
08CB: 08              EX      AF,AF'              ; 
08CC: 81              ADD     A,C                 ; 
08CD: 01 86 03        LD      BC,$0386            ; 
08D0: 88              ADC     A,B                 ; 
08D1: 09              ADD     HL,BC               ; 
08D2: 8B              ADC     A,E                 ; 
08D3: 03              INC     BC                  ; 
08D4: 8A              ADC     A,D                 ; 
08D5: 09              ADD     HL,BC               ; 
08D6: 86              ADD     A,(HL)              ; 
08D7: 03              INC     BC                  ; 
08D8: 88              ADC     A,B                 ; 
08D9: 09              ADD     HL,BC               ; 
08DA: 73              LD      (HL),E              ; 
08DB: 03              INC     BC                  ; 
08DC: 71              LD      (HL),C              ; 
08DD: 09              ADD     HL,BC               ; 
08DE: 86              ADD     A,(HL)              ; 
08DF: 03              INC     BC                  ; 
08E0: 88              ADC     A,B                 ; 
08E1: 09              ADD     HL,BC               ; 
08E2: 8B              ADC     A,E                 ; 
08E3: 03              INC     BC                  ; 
08E4: 8A              ADC     A,D                 ; 
08E5: 09              ADD     HL,BC               ; 
08E6: 86              ADD     A,(HL)              ; 
08E7: 03              INC     BC                  ; 
08E8: 71              LD      (HL),C              ; 
08E9: 09              ADD     HL,BC               ; 
08EA: 75              LD      (HL),L              ; 
08EB: 03              INC     BC                  ; 
08EC: 76              HALT                        ; 
08ED: 09              ADD     HL,BC               ; 
08EE: 74              LD      (HL),H              ; 
08EF: 03              INC     BC                  ; 
08F0: 72              LD      (HL),D              ; 
08F1: 09              ADD     HL,BC               ; 
08F2: 71              LD      (HL),C              ; 
08F3: 03              INC     BC                  ; 
08F4: 8B              ADC     A,E                 ; 
08F5: 09              ADD     HL,BC               ; 
08F6: 89              ADC     A,C                 ; 
08F7: 03              INC     BC                  ; 
08F8: 88              ADC     A,B                 ; 
08F9: 09              ADD     HL,BC               ; 
08FA: 84              ADD     A,H                 ; 
08FB: 03              INC     BC                  ; 
08FC: 74              LD      (HL),H              ; 
08FD: 09              ADD     HL,BC               ; 
08FE: 76              HALT                        ; 
08FF: 03              INC     BC                  ; 
0900: 74              LD      (HL),H              ; 
0901: 09              ADD     HL,BC               ; 
0902: 71              LD      (HL),C              ; 
0903: 03              INC     BC                  ; 
0904: 73              LD      (HL),E              ; 
0905: 04              INC     B                   ; 
0906: 8B              ADC     A,E                 ; 
0907: 04              INC     B                   ; 
0908: 88              ADC     A,B                 ; 
0909: 04              INC     B                   ; 
090A: 71              LD      (HL),C              ; 
090B: 04              INC     B                   ; 
090C: 8A              ADC     A,D                 ; 
090D: 04              INC     B                   ; 
090E: 88              ADC     A,B                 ; 
090F: 04              INC     B                   ; 
0910: 0C              INC     C                   ; 
0911: 10 FF           DJNZ    $912                ; {}
0913: 00              NOP                         ; 
0914: 00              NOP                         ; 
0915: 06 8A           LD      B,$8A               ; 
0917: 09              ADD     HL,BC               ; 
0918: 81              ADD     A,C                 ; 
0919: 03              INC     BC                  ; 
091A: 88              ADC     A,B                 ; 
091B: 09              ADD     HL,BC               ; 
091C: 83              ADD     A,E                 ; 
091D: 03              INC     BC                  ; 
091E: 86              ADD     A,(HL)              ; 
091F: 09              ADD     HL,BC               ; 
0920: 81              ADD     A,C                 ; 
0921: 03              INC     BC                  ; 
0922: 83              ADD     A,E                 ; 
0923: 09              ADD     HL,BC               ; 
0924: 85              ADD     A,L                 ; 
0925: 03              INC     BC                  ; 
0926: 8A              ADC     A,D                 ; 
0927: 09              ADD     HL,BC               ; 
0928: 81              ADD     A,C                 ; 
0929: 03              INC     BC                  ; 
092A: 88              ADC     A,B                 ; 
092B: 09              ADD     HL,BC               ; 
092C: 83              ADD     A,E                 ; 
092D: 03              INC     BC                  ; 
092E: 86              ADD     A,(HL)              ; 
092F: 09              ADD     HL,BC               ; 
0930: 81              ADD     A,C                 ; 
0931: 03              INC     BC                  ; 
0932: 88              ADC     A,B                 ; 
0933: 09              ADD     HL,BC               ; 
0934: 71              LD      (HL),C              ; 
0935: 03              INC     BC                  ; 
0936: 72              LD      (HL),D              ; 
0937: 09              ADD     HL,BC               ; 
0938: 71              LD      (HL),C              ; 
0939: 03              INC     BC                  ; 
093A: 8B              ADC     A,E                 ; 
093B: 09              ADD     HL,BC               ; 
093C: 89              ADC     A,C                 ; 
093D: 03              INC     BC                  ; 
093E: 88              ADC     A,B                 ; 
093F: 09              ADD     HL,BC               ; 
0940: 86              ADD     A,(HL)              ; 
0941: 03              INC     BC                  ; 
0942: 84              ADD     A,H                 ; 
0943: 09              ADD     HL,BC               ; 
0944: 88              ADC     A,B                 ; 
0945: 03              INC     BC                  ; 
0946: 89              ADC     A,C                 ; 
0947: 09              ADD     HL,BC               ; 
0948: 8B              ADC     A,E                 ; 
0949: 03              INC     BC                  ; 
094A: 89              ADC     A,C                 ; 
094B: 09              ADD     HL,BC               ; 
094C: 86              ADD     A,(HL)              ; 
094D: 03              INC     BC                  ; 
094E: 8B              ADC     A,E                 ; 
094F: 04              INC     B                   ; 
0950: 88              ADC     A,B                 ; 
0951: 04              INC     B                   ; 
0952: 83              ADD     A,E                 ; 
0953: 04              INC     B                   ; 
0954: 88              ADC     A,B                 ; 
0955: 04              INC     B                   ; 
0956: 85              ADD     A,L                 ; 
0957: 04              INC     B                   ; 
0958: 83              ADD     A,E                 ; 
0959: 04              INC     B                   ; 
095A: 0C              INC     C                   ; 
095B: 10 FF           DJNZ    $95C                ; {}
095D: 00              NOP                         ; 
095E: 00              NOP                         ; 
095F: 07              RLCA                        ; 
0960: 81              ADD     A,C                 ; 
0961: 0C              INC     C                   ; 
0962: 83              ADD     A,E                 ; 
0963: 09              ADD     HL,BC               ; 
0964: 86              ADD     A,(HL)              ; 
0965: 03              INC     BC                  ; 
0966: 85              ADD     A,L                 ; 
0967: 0C              INC     C                   ; 
0968: 81              ADD     A,C                 ; 
0969: 0C              INC     C                   ; 
096A: 86              ADD     A,(HL)              ; 
096B: 0C              INC     C                   ; 
096C: 88              ADC     A,B                 ; 
096D: 09              ADD     HL,BC               ; 
096E: 8B              ADC     A,E                 ; 
096F: 03              INC     BC                  ; 
0970: 8A              ADC     A,D                 ; 
0971: 0C              INC     C                   ; 
0972: 88              ADC     A,B                 ; 
0973: 0C              INC     C                   ; 
0974: 89              ADC     A,C                 ; 
0975: 0C              INC     C                   ; 
0976: 88              ADC     A,B                 ; 
0977: 09              ADD     HL,BC               ; 
0978: 86              ADD     A,(HL)              ; 
0979: 03              INC     BC                  ; 
097A: 84              ADD     A,H                 ; 
097B: 0C              INC     C                   ; 
097C: 89              ADC     A,C                 ; 
097D: 0C              INC     C                   ; 
097E: 74              LD      (HL),H              ; 
097F: 0C              INC     C                   ; 
0980: 71              LD      (HL),C              ; 
0981: 09              ADD     HL,BC               ; 
0982: 89              ADC     A,C                 ; 
0983: 03              INC     BC                  ; 
0984: 88              ADC     A,B                 ; 
0985: 0C              INC     C                   ; 
0986: 71              LD      (HL),C              ; 
0987: 09              ADD     HL,BC               ; 
0988: 8A              ADC     A,D                 ; 
0989: 03              INC     BC                  ; 
098A: 0C              INC     C                   ; 
098B: 10 FF           DJNZ    $98C                ; {}
098D: 02              LD      (BC),A              ; 
098E: 00              NOP                         ; 
098F: 03              INC     BC                  ; 
0990: 78              LD      A,B                 ; 
0991: 02              LD      (BC),A              ; 
0992: 0C              INC     C                   ; 
0993: 01 78 01        LD      BC,$0178            ; 
0996: 79              LD      A,C                 ; 
0997: 01 7B 01        LD      BC,$017B            ; 
099A: 61              LD      H,C                 ; 
099B: 03              INC     BC                  ; 
099C: 0C              INC     C                   ; 
099D: 03              INC     BC                  ; 
099E: FF              RST     0X38                ; 
099F: 02              LD      (BC),A              ; 
09A0: 00              NOP                         ; 
09A1: 03              INC     BC                  ; 
09A2: 73              LD      (HL),E              ; 
09A3: 02              LD      (BC),A              ; 
09A4: 0C              INC     C                   ; 
09A5: 01 73 01        LD      BC,$0173            ; 
09A8: 74              LD      (HL),H              ; 
09A9: 01 76 01        LD      BC,$0176            ; 
09AC: 78              LD      A,B                 ; 
09AD: 03              INC     BC                  ; 
09AE: 0C              INC     C                   ; 
09AF: 02              LD      (BC),A              ; 
09B0: FF              RST     0X38                ; 
09B1: 02              LD      (BC),A              ; 
09B2: 00              NOP                         ; 
09B3: 03              INC     BC                  ; 
09B4: 70              LD      (HL),B              ; 
09B5: 02              LD      (BC),A              ; 
09B6: 0C              INC     C                   ; 
09B7: 01 70 01        LD      BC,$0170            ; 
09BA: 71              LD      (HL),C              ; 
09BB: 01 73 01        LD      BC,$0173            ; 
09BE: 75              LD      (HL),L              ; 
09BF: 03              INC     BC                  ; 
09C0: 0C              INC     C                   ; 
09C1: 02              LD      (BC),A              ; 
09C2: FF              RST     0X38                ; 
09C3: 01 00 04        LD      BC,$0400            ; 
09C6: 78              LD      A,B                 ; 
09C7: 01 7A 01        LD      BC,$017A            ; 
09CA: 63              LD      H,E                 ; 
09CB: 01 78 01        LD      BC,$0178            ; 
09CE: 7A              LD      A,D                 ; 
09CF: 01 63 01        LD      BC,$0163            ; 
09D2: 65              LD      H,L                 ; 
09D3: 03              INC     BC                  ; 
09D4: FF              RST     0X38                ; 
09D5: 01 00 05        LD      BC,$0500            ; 
09D8: 73              LD      (HL),E              ; 
09D9: 01 78 01        LD      BC,$0178            ; 
09DC: 7A              LD      A,D                 ; 
09DD: 01 73 01        LD      BC,$0173            ; 
09E0: 78              LD      A,B                 ; 
09E1: 01 7A 01        LD      BC,$017A            ; 
09E4: 60              LD      H,B                 ; 
09E5: 03              INC     BC                  ; 
09E6: FF              RST     0X38                ; 
09E7: 01 00 07        LD      BC,$0700            ; 
09EA: 8A              ADC     A,D                 ; 
09EB: 01 73 01        LD      BC,$0173            ; 
09EE: 78              LD      A,B                 ; 
09EF: 01 8A 01        LD      BC,$018A            ; 
09F2: 73              LD      (HL),E              ; 
09F3: 01 78 01        LD      BC,$0178            ; 
09F6: 7A              LD      A,D                 ; 
09F7: 03              INC     BC                  ; 
09F8: FF              RST     0X38                ; 
09F9: 01 06 04        LD      BC,$0406            ; 
09FC: 7A              LD      A,D                 ; 
09FD: 01 78 01        LD      BC,$0178            ; 
0A00: 7A              LD      A,D                 ; 
0A01: 01 61 01        LD      BC,$0161            ; 
0A04: 65              LD      H,L                 ; 
0A05: 01 68 03        LD      BC,$0368            ; 
0A08: FF              RST     0X38                ; 
0A09: 01 06 04        LD      BC,$0406            ; 
0A0C: 78              LD      A,B                 ; 
0A0D: 01 75 01        LD      BC,$0175            ; 
0A10: 78              LD      A,B                 ; 
0A11: 01 7A 01        LD      BC,$017A            ; 
0A14: 61              LD      H,C                 ; 
0A15: 01 65 03        LD      BC,$0365            ; 
0A18: FF              RST     0X38                ; 
0A19: 01 06 04        LD      BC,$0406            ; 
0A1C: 75              LD      (HL),L              ; 
0A1D: 01 71 01        LD      BC,$0171            ; 
0A20: 75              LD      (HL),L              ; 
0A21: 01 78 01        LD      BC,$0178            ; 
0A24: 7A              LD      A,D                 ; 
0A25: 01 60 03        LD      BC,$0360            ; 
0A28: FF              RST     0X38                ; 
0A29: 02              LD      (BC),A              ; 
0A2A: 04              INC     B                   ; 
0A2B: 03              INC     BC                  ; 
0A2C: 7A              LD      A,D                 ; 
0A2D: 01 76 01        LD      BC,$0176            ; 
0A30: 78              LD      A,B                 ; 
0A31: 01 75 01        LD      BC,$0175            ; 
0A34: 76              HALT                        ; 
0A35: 01 73 01        LD      BC,$0173            ; 
0A38: 75              LD      (HL),L              ; 
0A39: 01 72 01        LD      BC,$0172            ; 
0A3C: 73              LD      (HL),E              ; 
0A3D: 01 8A 01        LD      BC,$018A            ; 
0A40: 8B              ADC     A,E                 ; 
0A41: 01 88 01        LD      BC,$0188            ; 
0A44: 86              ADD     A,(HL)              ; 
0A45: 01 85 01        LD      BC,$0185            ; 
0A48: 83              ADD     A,E                 ; 
0A49: 01 82 01        LD      BC,$0182            ; 
0A4C: 83              ADD     A,E                 ; 
0A4D: 01 86 01        LD      BC,$0186            ; 
0A50: 85              ADD     A,L                 ; 
0A51: 01 88 01        LD      BC,$0188            ; 
0A54: 86              ADD     A,(HL)              ; 
0A55: 01 8A 01        LD      BC,$018A            ; 
0A58: 88              ADC     A,B                 ; 
0A59: 01 8B 01        LD      BC,$018B            ; 
0A5C: 8A              ADC     A,D                 ; 
0A5D: 01 73 01        LD      BC,$0173            ; 
0A60: 72              LD      (HL),D              ; 
0A61: 01 73 01        LD      BC,$0173            ; 
0A64: 75              LD      (HL),L              ; 
0A65: 01 8A 01        LD      BC,$018A            ; 
0A68: 70              LD      (HL),B              ; 
0A69: 01 72 01        LD      BC,$0172            ; 
0A6C: FF              RST     0X38                ; 
0A6D: 02              LD      (BC),A              ; 
0A6E: 04              INC     B                   ; 
0A6F: 03              INC     BC                  ; 
0A70: 76              HALT                        ; 
0A71: 01 73 01        LD      BC,$0173            ; 
0A74: 75              LD      (HL),L              ; 
0A75: 01 72 01        LD      BC,$0172            ; 
0A78: 73              LD      (HL),E              ; 
0A79: 01 70 01        LD      BC,$0170            ; 
0A7C: 72              LD      (HL),D              ; 
0A7D: 01 8A 01        LD      BC,$018A            ; 
0A80: 8B              ADC     A,E                 ; 
0A81: 01 86 01        LD      BC,$0186            ; 
0A84: 88              ADC     A,B                 ; 
0A85: 01 85 01        LD      BC,$0185            ; 
0A88: 83              ADD     A,E                 ; 
0A89: 01 82 01        LD      BC,$0182            ; 
0A8C: 80              ADD     A,B                 ; 
0A8D: 01 9A 01        LD      BC,$019A            ; 
0A90: 9A              SBC     D                   ; 
0A91: 01 83 01        LD      BC,$0183            ; 
0A94: 82              ADD     A,D                 ; 
0A95: 01 85 01        LD      BC,$0185            ; 
0A98: 83              ADD     A,E                 ; 
0A99: 01 86 01        LD      BC,$0186            ; 
0A9C: 85              ADD     A,L                 ; 
0A9D: 01 88 01        LD      BC,$0188            ; 
0AA0: 86              ADD     A,(HL)              ; 
0AA1: 01 8A 01        LD      BC,$018A            ; 
0AA4: 88              ADC     A,B                 ; 
0AA5: 01 8B 01        LD      BC,$018B            ; 
0AA8: 8A              ADC     A,D                 ; 
0AA9: 01 88 01        LD      BC,$0188            ; 
0AAC: 86              ADD     A,(HL)              ; 
0AAD: 01 85 01        LD      BC,$0185            ; 
0AB0: FF              RST     0X38                ; 
0AB1: 02              LD      (BC),A              ; 
0AB2: 10 03           DJNZ    $AB7                ; {}
0AB4: 93              SUB     E                   ; 
0AB5: 02              LD      (BC),A              ; 
0AB6: 9A              SBC     D                   ; 
0AB7: 02              LD      (BC),A              ; 
0AB8: 83              ADD     A,E                 ; 
0AB9: 03              INC     BC                  ; 
0ABA: 9A              SBC     D                   ; 
0ABB: 01 98 01        LD      BC,$0198            ; 
0ABE: 96              SUB     (HL)                ; 
0ABF: 01 95 01        LD      BC,$0195            ; 
0AC2: 93              SUB     E                   ; 
0AC3: 02              LD      (BC),A              ; 
0AC4: 95              SUB     L                   ; 
0AC5: 03              INC     BC                  ; 
0AC6: 96              SUB     (HL)                ; 
0AC7: 02              LD      (BC),A              ; 
0AC8: 98              SBC     B                   ; 
0AC9: 02              LD      (BC),A              ; 
0ACA: 9A              SBC     D                   ; 
0ACB: 02              LD      (BC),A              ; 
0ACC: 9B              SBC     E                   ; 
0ACD: 02              LD      (BC),A              ; 
0ACE: 9A              SBC     D                   ; 
0ACF: 02              LD      (BC),A              ; 
0AD0: 98              SBC     B                   ; 
0AD1: 01 96 01        LD      BC,$0196            ; 
0AD4: 95              SUB     L                   ; 
0AD5: 01 92 01        LD      BC,$0192            ; 
0AD8: 93              SUB     E                   ; 
0AD9: 01 95 01        LD      BC,$0195            ; 
0ADC: FF              RST     0X38                ; 
0ADD: 02              LD      (BC),A              ; 
0ADE: 04              INC     B                   ; 
0ADF: 03              INC     BC                  ; 
0AE0: 7A              LD      A,D                 ; 
0AE1: 01 77 01        LD      BC,$0177            ; 
0AE4: 78              LD      A,B                 ; 
0AE5: 01 75 01        LD      BC,$0175            ; 
0AE8: 77              LD      (HL),A              ; 
0AE9: 01 73 01        LD      BC,$0173            ; 
0AEC: 75              LD      (HL),L              ; 
0AED: 01 72 01        LD      BC,$0172            ; 
0AF0: 73              LD      (HL),E              ; 
0AF1: 01 8A 01        LD      BC,$018A            ; 
0AF4: 80              ADD     A,B                 ; 
0AF5: 01 88 01        LD      BC,$0188            ; 
0AF8: 87              ADD     A,A                 ; 
0AF9: 01 85 01        LD      BC,$0185            ; 
0AFC: 83              ADD     A,E                 ; 
0AFD: 01 82 01        LD      BC,$0182            ; 
0B00: 83              ADD     A,E                 ; 
0B01: 01 87 01        LD      BC,$0187            ; 
0B04: 85              ADD     A,L                 ; 
0B05: 01 88 01        LD      BC,$0188            ; 
0B08: 87              ADD     A,A                 ; 
0B09: 01 8A 01        LD      BC,$018A            ; 
0B0C: 88              ADC     A,B                 ; 
0B0D: 01 80 01        LD      BC,$0180            ; 
0B10: 8A              ADC     A,D                 ; 
0B11: 01 73 01        LD      BC,$0173            ; 
0B14: 72              LD      (HL),D              ; 
0B15: 01 73 01        LD      BC,$0173            ; 
0B18: 75              LD      (HL),L              ; 
0B19: 01 8A 01        LD      BC,$018A            ; 
0B1C: 70              LD      (HL),B              ; 
0B1D: 01 72 01        LD      BC,$0172            ; 
0B20: FF              RST     0X38                ; 
0B21: 02              LD      (BC),A              ; 
0B22: 04              INC     B                   ; 
0B23: 03              INC     BC                  ; 
0B24: 77              LD      (HL),A              ; 
0B25: 01 73 01        LD      BC,$0173            ; 
0B28: 75              LD      (HL),L              ; 
0B29: 01 72 01        LD      BC,$0172            ; 
0B2C: 73              LD      (HL),E              ; 
0B2D: 01 70 01        LD      BC,$0170            ; 
0B30: 72              LD      (HL),D              ; 
0B31: 01 8A 01        LD      BC,$018A            ; 
0B34: 80              ADD     A,B                 ; 
0B35: 01 87 01        LD      BC,$0187            ; 
0B38: 88              ADC     A,B                 ; 
0B39: 01 85 01        LD      BC,$0185            ; 
0B3C: 83              ADD     A,E                 ; 
0B3D: 01 82 01        LD      BC,$0182            ; 
0B40: 80              ADD     A,B                 ; 
0B41: 01 9A 01        LD      BC,$019A            ; 
0B44: 9A              SBC     D                   ; 
0B45: 01 83 01        LD      BC,$0183            ; 
0B48: 82              ADD     A,D                 ; 
0B49: 01 85 01        LD      BC,$0185            ; 
0B4C: 83              ADD     A,E                 ; 
0B4D: 01 87 01        LD      BC,$0187            ; 
0B50: 85              ADD     A,L                 ; 
0B51: 01 88 01        LD      BC,$0188            ; 
0B54: 87              ADD     A,A                 ; 
0B55: 01 8A 01        LD      BC,$018A            ; 
0B58: 88              ADC     A,B                 ; 
0B59: 01 80 01        LD      BC,$0180            ; 
0B5C: 8A              ADC     A,D                 ; 
0B5D: 01 88 01        LD      BC,$0188            ; 
0B60: 87              ADD     A,A                 ; 
0B61: 01 85 01        LD      BC,$0185            ; 
0B64: FF              RST     0X38                ; 
0B65: 02              LD      (BC),A              ; 
0B66: 10 03           DJNZ    $B6B                ; {}
0B68: 93              SUB     E                   ; 
0B69: 02              LD      (BC),A              ; 
0B6A: 9A              SBC     D                   ; 
0B6B: 02              LD      (BC),A              ; 
0B6C: 83              ADD     A,E                 ; 
0B6D: 03              INC     BC                  ; 
0B6E: 9A              SBC     D                   ; 
0B6F: 01 98 01        LD      BC,$0198            ; 
0B72: 97              SUB     A                   ; 
0B73: 01 95 01        LD      BC,$0195            ; 
0B76: 93              SUB     E                   ; 
0B77: 02              LD      (BC),A              ; 
0B78: 95              SUB     L                   ; 
0B79: 03              INC     BC                  ; 
0B7A: 97              SUB     A                   ; 
0B7B: 02              LD      (BC),A              ; 
0B7C: 98              SBC     B                   ; 
0B7D: 02              LD      (BC),A              ; 
0B7E: 9A              SBC     D                   ; 
0B7F: 02              LD      (BC),A              ; 
0B80: 90              SUB     B                   ; 
0B81: 02              LD      (BC),A              ; 
0B82: 9A              SBC     D                   ; 
0B83: 02              LD      (BC),A              ; 
0B84: 98              SBC     B                   ; 
0B85: 01 97 01        LD      BC,$0197            ; 
0B88: 95              SUB     L                   ; 
0B89: 01 92 01        LD      BC,$0192            ; 
0B8C: 93              SUB     E                   ; 
0B8D: 01 95 01        LD      BC,$0195            ; 
0B90: FF              RST     0X38                ; 
0B91: 02              LD      (BC),A              ; 
0B92: 04              INC     B                   ; 
0B93: 03              INC     BC                  ; 
0B94: 7A              LD      A,D                 ; 
0B95: 01 76 01        LD      BC,$0176            ; 
0B98: 78              LD      A,B                 ; 
0B99: 01 75 01        LD      BC,$0175            ; 
0B9C: 76              HALT                        ; 
0B9D: 01 73 01        LD      BC,$0173            ; 
0BA0: 75              LD      (HL),L              ; 
0BA1: 01 72 01        LD      BC,$0172            ; 
0BA4: 73              LD      (HL),E              ; 
0BA5: 01 8A 01        LD      BC,$018A            ; 
0BA8: 8A              ADC     A,D                 ; 
0BA9: 01 88 01        LD      BC,$0188            ; 
0BAC: 86              ADD     A,(HL)              ; 
0BAD: 01 85 01        LD      BC,$0185            ; 
0BB0: 83              ADD     A,E                 ; 
0BB1: 01 82 01        LD      BC,$0182            ; 
0BB4: 83              ADD     A,E                 ; 
0BB5: 01 85 01        LD      BC,$0185            ; 
0BB8: 86              ADD     A,(HL)              ; 
0BB9: 01 88 01        LD      BC,$0188            ; 
0BBC: 86              ADD     A,(HL)              ; 
0BBD: 01 8A 01        LD      BC,$018A            ; 
0BC0: 70              LD      (HL),B              ; 
0BC1: 01 72 01        LD      BC,$0172            ; 
0BC4: 73              LD      (HL),E              ; 
0BC5: 04              INC     B                   ; 
0BC6: FF              RST     0X38                ; 
0BC7: 02              LD      (BC),A              ; 
0BC8: 04              INC     B                   ; 
0BC9: 03              INC     BC                  ; 
0BCA: 76              HALT                        ; 
0BCB: 01 73 01        LD      BC,$0173            ; 
0BCE: 75              LD      (HL),L              ; 
0BCF: 01 72 01        LD      BC,$0172            ; 
0BD2: 73              LD      (HL),E              ; 
0BD3: 01 70 01        LD      BC,$0170            ; 
0BD6: 72              LD      (HL),D              ; 
0BD7: 01 8A 01        LD      BC,$018A            ; 
0BDA: 8A              ADC     A,D                 ; 
0BDB: 01 86 01        LD      BC,$0186            ; 
0BDE: 86              ADD     A,(HL)              ; 
0BDF: 01 85 01        LD      BC,$0185            ; 
0BE2: 83              ADD     A,E                 ; 
0BE3: 01 82 01        LD      BC,$0182            ; 
0BE6: 80              ADD     A,B                 ; 
0BE7: 01 9A 01        LD      BC,$019A            ; 
0BEA: 9A              SBC     D                   ; 
0BEB: 01 8B 01        LD      BC,$018B            ; 
0BEE: 80              ADD     A,B                 ; 
0BEF: 01 82 01        LD      BC,$0182            ; 
0BF2: 83              ADD     A,E                 ; 
0BF3: 01 85 01        LD      BC,$0185            ; 
0BF6: 86              ADD     A,(HL)              ; 
0BF7: 01 88 01        LD      BC,$0188            ; 
0BFA: 8A              ADC     A,D                 ; 
0BFB: 04              INC     B                   ; 
0BFC: FF              RST     0X38                ; 
0BFD: 02              LD      (BC),A              ; 
0BFE: 10 03           DJNZ    $C03                ; {}
0C00: 73              LD      (HL),E              ; 
0C01: 02              LD      (BC),A              ; 
0C02: 75              LD      (HL),L              ; 
0C03: 02              LD      (BC),A              ; 
0C04: 76              HALT                        ; 
0C05: 02              LD      (BC),A              ; 
0C06: 75              LD      (HL),L              ; 
0C07: 02              LD      (BC),A              ; 
0C08: 73              LD      (HL),E              ; 
0C09: 02              LD      (BC),A              ; 
0C0A: 72              LD      (HL),D              ; 
0C0B: 02              LD      (BC),A              ; 
0C0C: 70              LD      (HL),B              ; 
0C0D: 02              LD      (BC),A              ; 
0C0E: 72              LD      (HL),D              ; 
0C0F: 02              LD      (BC),A              ; 
0C10: 73              LD      (HL),E              ; 
0C11: 02              LD      (BC),A              ; 
0C12: 8B              ADC     A,E                 ; 
0C13: 02              LD      (BC),A              ; 
0C14: 8A              ADC     A,D                 ; 
0C15: 02              LD      (BC),A              ; 
0C16: 86              ADD     A,(HL)              ; 
0C17: 02              LD      (BC),A              ; 
0C18: 83              ADD     A,E                 ; 
0C19: 04              INC     B                   ; 
0C1A: FF              RST     0X38                ; 
0C1B: 00              NOP                         ; 
0C1C: 00              NOP                         ; 
0C1D: 04              INC     B                   ; 
0C1E: 71              LD      (HL),C              ; 
0C1F: 04              INC     B                   ; 
0C20: 73              LD      (HL),E              ; 
0C21: 04              INC     B                   ; 
0C22: 71              LD      (HL),C              ; 
0C23: 04              INC     B                   ; 
0C24: 73              LD      (HL),E              ; 
0C25: 04              INC     B                   ; 
0C26: 76              HALT                        ; 
0C27: 04              INC     B                   ; 
0C28: 78              LD      A,B                 ; 
0C29: 04              INC     B                   ; 
0C2A: 76              HALT                        ; 
0C2B: 04              INC     B                   ; 
0C2C: 78              LD      A,B                 ; 
0C2D: 04              INC     B                   ; 
0C2E: FF              RST     0X38                ; 
0C2F: 00              NOP                         ; 
0C30: 00              NOP                         ; 
0C31: 06 56           LD      B,$56               ; 
0C33: 01 55 01        LD      BC,$0155            ; 
0C36: 54              LD      D,H                 ; 
0C37: 01 53 01        LD      BC,$0153            ; 
0C3A: 52              LD      D,D                 ; 
0C3B: 01 51 01        LD      BC,$0151            ; 
0C3E: 50              LD      D,B                 ; 
0C3F: 01 6B 01        LD      BC,$016B            ; 
0C42: 6A              LD      L,D                 ; 
0C43: 01 69 01        LD      BC,$0169            ; 
0C46: 68              LD      L,B                 ; 
0C47: 01 67 01        LD      BC,$0167            ; 
0C4A: 66              LD      H,(HL)              ; 
0C4B: 01 65 01        LD      BC,$0165            ; 
0C4E: 64              LD      H,H                 ; 
0C4F: 01 63 01        LD      BC,$0163            ; 
0C52: 62              LD      H,D                 ; 
0C53: 01 61 01        LD      BC,$0161            ; 
0C56: 60              LD      H,B                 ; 
0C57: 01 7B 01        LD      BC,$017B            ; 
0C5A: 7A              LD      A,D                 ; 
0C5B: 01 79 01        LD      BC,$0179            ; 
0C5E: 78              LD      A,B                 ; 
0C5F: 01 77 01        LD      BC,$0177            ; 
0C62: 76              HALT                        ; 
0C63: 01 75 01        LD      BC,$0175            ; 
0C66: 74              LD      (HL),H              ; 
0C67: 01 73 01        LD      BC,$0173            ; 
0C6A: 72              LD      (HL),D              ; 
0C6B: 01 71 01        LD      BC,$0171            ; 
0C6E: 70              LD      (HL),B              ; 
0C6F: 01 8B 01        LD      BC,$018B            ; 
0C72: 8A              ADC     A,D                 ; 
0C73: 01 89 01        LD      BC,$0189            ; 
0C76: 88              ADC     A,B                 ; 
0C77: 01 87 01        LD      BC,$0187            ; 
0C7A: 86              ADD     A,(HL)              ; 
0C7B: 01 85 01        LD      BC,$0185            ; 
0C7E: 84              ADD     A,H                 ; 
0C7F: 01 83 01        LD      BC,$0183            ; 
0C82: FF              RST     0X38                ; 
0C83: 02              LD      (BC),A              ; 
0C84: 04              INC     B                   ; 
0C85: 05              DEC     B                   ; 
0C86: 60              LD      H,B                 ; 
0C87: 01 78 01        LD      BC,$0178            ; 
0C8A: 75              LD      (HL),L              ; 
0C8B: 01 71 01        LD      BC,$0171            ; 
0C8E: 60              LD      H,B                 ; 
0C8F: 01 78 01        LD      BC,$0178            ; 
0C92: 75              LD      (HL),L              ; 
0C93: 01 71 01        LD      BC,$0171            ; 
0C96: 60              LD      H,B                 ; 
0C97: 01 78 01        LD      BC,$0178            ; 
0C9A: 75              LD      (HL),L              ; 
0C9B: 01 71 01        LD      BC,$0171            ; 
0C9E: 60              LD      H,B                 ; 
0C9F: 01 78 01        LD      BC,$0178            ; 
0CA2: 75              LD      (HL),L              ; 
0CA3: 01 71 01        LD      BC,$0171            ; 
0CA6: 60              LD      H,B                 ; 
0CA7: 01 78 01        LD      BC,$0178            ; 
0CAA: 75              LD      (HL),L              ; 
0CAB: 01 71 01        LD      BC,$0171            ; 
0CAE: 60              LD      H,B                 ; 
0CAF: 01 78 01        LD      BC,$0178            ; 
0CB2: 75              LD      (HL),L              ; 
0CB3: 01 71 01        LD      BC,$0171            ; 
0CB6: 60              LD      H,B                 ; 
0CB7: 01 0C 01        LD      BC,$010C            ; 
0CBA: 78              LD      A,B                 ; 
0CBB: 01 7A 01        LD      BC,$017A            ; 
0CBE: 75              LD      (HL),L              ; 
0CBF: 01 78 01        LD      BC,$0178            ; 
0CC2: 73              LD      (HL),E              ; 
0CC3: 01 75 01        LD      BC,$0175            ; 
0CC6: 61              LD      H,C                 ; 
0CC7: 01 7A 01        LD      BC,$017A            ; 
0CCA: 76              HALT                        ; 
0CCB: 01 73 01        LD      BC,$0173            ; 
0CCE: 61              LD      H,C                 ; 
0CCF: 01 7A 01        LD      BC,$017A            ; 
0CD2: 76              HALT                        ; 
0CD3: 01 73 01        LD      BC,$0173            ; 
0CD6: 61              LD      H,C                 ; 
0CD7: 01 7A 01        LD      BC,$017A            ; 
0CDA: 76              HALT                        ; 
0CDB: 01 73 01        LD      BC,$0173            ; 
0CDE: 61              LD      H,C                 ; 
0CDF: 01 7A 01        LD      BC,$017A            ; 
0CE2: 76              HALT                        ; 
0CE3: 01 73 01        LD      BC,$0173            ; 
0CE6: 61              LD      H,C                 ; 
0CE7: 01 79 01        LD      BC,$0179            ; 
0CEA: 76              HALT                        ; 
0CEB: 01 73 01        LD      BC,$0173            ; 
0CEE: 61              LD      H,C                 ; 
0CEF: 01 79 01        LD      BC,$0179            ; 
0CF2: 76              HALT                        ; 
0CF3: 01 73 01        LD      BC,$0173            ; 
0CF6: 61              LD      H,C                 ; 
0CF7: 01 0C 01        LD      BC,$010C            ; 
0CFA: 79              LD      A,C                 ; 
0CFB: 01 61 01        LD      BC,$0161            ; 
0CFE: 78              LD      A,B                 ; 
0CFF: 01 79 01        LD      BC,$0179            ; 
0D02: 75              LD      (HL),L              ; 
0D03: 01 78 01        LD      BC,$0178            ; 
0D06: FF              RST     0X38                ; 
0D07: 02              LD      (BC),A              ; 
0D08: 02              LD      (BC),A              ; 
0D09: 05              DEC     B                   ; 
0D0A: 60              LD      H,B                 ; 
0D0B: 01 60 01        LD      BC,$0160            ; 
0D0E: 60              LD      H,B                 ; 
0D0F: 01 FF 02        LD      BC,$02FF            ; 
0D12: 04              INC     B                   ; 
0D13: 05              DEC     B                   ; 
0D14: 61              LD      H,C                 ; 
0D15: 02              LD      (BC),A              ; 
0D16: 78              LD      A,B                 ; 
0D17: 02              LD      (BC),A              ; 
0D18: 78              LD      A,B                 ; 
0D19: 02              LD      (BC),A              ; 
0D1A: 61              LD      H,C                 ; 
0D1B: 02              LD      (BC),A              ; 
0D1C: 78              LD      A,B                 ; 
0D1D: 02              LD      (BC),A              ; 
0D1E: 78              LD      A,B                 ; 
0D1F: 02              LD      (BC),A              ; 
0D20: 61              LD      H,C                 ; 
0D21: 02              LD      (BC),A              ; 
0D22: 78              LD      A,B                 ; 
0D23: 02              LD      (BC),A              ; 
0D24: 78              LD      A,B                 ; 
0D25: 02              LD      (BC),A              ; 
0D26: 61              LD      H,C                 ; 
0D27: 02              LD      (BC),A              ; 
0D28: 78              LD      A,B                 ; 
0D29: 02              LD      (BC),A              ; 
0D2A: 78              LD      A,B                 ; 
0D2B: 02              LD      (BC),A              ; 
0D2C: 61              LD      H,C                 ; 
0D2D: 02              LD      (BC),A              ; 
0D2E: 78              LD      A,B                 ; 
0D2F: 02              LD      (BC),A              ; 
0D30: 7A              LD      A,D                 ; 
0D31: 02              LD      (BC),A              ; 
0D32: 75              LD      (HL),L              ; 
0D33: 02              LD      (BC),A              ; 
0D34: 63              LD      H,E                 ; 
0D35: 02              LD      (BC),A              ; 
0D36: 7A              LD      A,D                 ; 
0D37: 02              LD      (BC),A              ; 
0D38: 7A              LD      A,D                 ; 
0D39: 02              LD      (BC),A              ; 
0D3A: 63              LD      H,E                 ; 
0D3B: 02              LD      (BC),A              ; 
0D3C: 7A              LD      A,D                 ; 
0D3D: 02              LD      (BC),A              ; 
0D3E: 7A              LD      A,D                 ; 
0D3F: 02              LD      (BC),A              ; 
0D40: 63              LD      H,E                 ; 
0D41: 02              LD      (BC),A              ; 
0D42: 7A              LD      A,D                 ; 
0D43: 02              LD      (BC),A              ; 
0D44: 79              LD      A,C                 ; 
0D45: 02              LD      (BC),A              ; 
0D46: 63              LD      H,E                 ; 
0D47: 02              LD      (BC),A              ; 
0D48: 79              LD      A,C                 ; 
0D49: 02              LD      (BC),A              ; 
0D4A: 79              LD      A,C                 ; 
0D4B: 02              LD      (BC),A              ; 
0D4C: 63              LD      H,E                 ; 
0D4D: 02              LD      (BC),A              ; 
0D4E: 79              LD      A,C                 ; 
0D4F: 02              LD      (BC),A              ; 
0D50: 76              HALT                        ; 
0D51: 02              LD      (BC),A              ; 
0D52: 73              LD      (HL),E              ; 
0D53: 02              LD      (BC),A              ; 
0D54: FF              RST     0X38                ; 
0D55: 02              LD      (BC),A              ; 
0D56: 02              LD      (BC),A              ; 
0D57: 05              DEC     B                   ; 
0D58: 78              LD      A,B                 ; 
0D59: 01 78 01        LD      BC,$0178            ; 
0D5C: 78              LD      A,B                 ; 
0D5D: 01 FF 02        LD      BC,$02FF            ; 
0D60: 10 05           DJNZ    $D67                ; {}
0D62: 85              ADD     A,L                 ; 
0D63: 06 85           LD      B,$85               ; 
0D65: 06 85           LD      B,$85               ; 
0D67: 06 85           LD      B,$85               ; 
0D69: 06 85           LD      B,$85               ; 
0D6B: 04              INC     B                   ; 
0D6C: 85              ADD     A,L                 ; 
0D6D: 04              INC     B                   ; 
0D6E: 86              ADD     A,(HL)              ; 
0D6F: 06 86           LD      B,$86               ; 
0D71: 06 86           LD      B,$86               ; 
0D73: 06 86           LD      B,$86               ; 
0D75: 06 86           LD      B,$86               ; 
0D77: 04              INC     B                   ; 
0D78: 86              ADD     A,(HL)              ; 
0D79: 04              INC     B                   ; 
0D7A: FF              RST     0X38                ; 
0D7B: 02              LD      (BC),A              ; 
0D7C: 04              INC     B                   ; 
0D7D: 05              DEC     B                   ; 
0D7E: 81              ADD     A,C                 ; 
0D7F: 01 81 01        LD      BC,$0181            ; 
0D82: 81              ADD     A,C                 ; 
0D83: 01 FF 02        LD      BC,$02FF            ; 
0D86: 00              NOP                         ; 
0D87: 07              RLCA                        ; 
0D88: 65              LD      H,L                 ; 
0D89: 01 0C 01        LD      BC,$010C            ; 
0D8C: 61              LD      H,C                 ; 
0D8D: 01 0C 01        LD      BC,$010C            ; 
0D90: 63              LD      H,E                 ; 
0D91: 01 FF 02        LD      BC,$02FF            ; 
0D94: 00              NOP                         ; 
0D95: 05              DEC     B                   ; 
0D96: 7A              LD      A,D                 ; 
0D97: 05              DEC     B                   ; 
0D98: 0C              INC     C                   ; 
0D99: 01 7A 01        LD      BC,$017A            ; 
0D9C: 0C              INC     C                   ; 
0D9D: 01 7A 03        LD      BC,$037A            ; 
0DA0: 0C              INC     C                   ; 
0DA1: 01 78 07        LD      BC,$0778            ; 
0DA4: 0C              INC     C                   ; 
0DA5: 01 78 07        LD      BC,$0778            ; 
0DA8: 0C              INC     C                   ; 
0DA9: 01 78 03        LD      BC,$0378            ; 
0DAC: 0C              INC     C                   ; 
0DAD: 01 7B 05        LD      BC,$057B            ; 
0DB0: 0C              INC     C                   ; 
0DB1: 01 7B 01        LD      BC,$017B            ; 
0DB4: 0C              INC     C                   ; 
0DB5: 01 7B 03        LD      BC,$037B            ; 
0DB8: 0C              INC     C                   ; 
0DB9: 01 7A 07        LD      BC,$077A            ; 
0DBC: 0C              INC     C                   ; 
0DBD: 01 7A 07        LD      BC,$077A            ; 
0DC0: 0C              INC     C                   ; 
0DC1: 01 7A 03        LD      BC,$037A            ; 
0DC4: 0C              INC     C                   ; 
0DC5: 01 7B 01        LD      BC,$017B            ; 
0DC8: 0C              INC     C                   ; 
0DC9: 01 7B 01        LD      BC,$017B            ; 
0DCC: 0C              INC     C                   ; 
0DCD: 03              INC     BC                  ; 
0DCE: 7B              LD      A,E                 ; 
0DCF: 01 0C 01        LD      BC,$010C            ; 
0DD2: 7B              LD      A,E                 ; 
0DD3: 03              INC     BC                  ; 
0DD4: 0C              INC     C                   ; 
0DD5: 01 61 01        LD      BC,$0161            ; 
0DD8: 0C              INC     C                   ; 
0DD9: 01 61 01        LD      BC,$0161            ; 
0DDC: 0C              INC     C                   ; 
0DDD: 03              INC     BC                  ; 
0DDE: 61              LD      H,C                 ; 
0DDF: 01 0C 01        LD      BC,$010C            ; 
0DE2: 61              LD      H,C                 ; 
0DE3: 03              INC     BC                  ; 
0DE4: 0C              INC     C                   ; 
0DE5: 01 61 03        LD      BC,$0361            ; 
0DE8: 0C              INC     C                   ; 
0DE9: 01 61 03        LD      BC,$0361            ; 
0DEC: 0C              INC     C                   ; 
0DED: 01 63 01        LD      BC,$0163            ; 
0DF0: 0C              INC     C                   ; 
0DF1: 01 63 01        LD      BC,$0163            ; 
0DF4: 0C              INC     C                   ; 
0DF5: 03              INC     BC                  ; 
0DF6: 63              LD      H,E                 ; 
0DF7: 01 0C 01        LD      BC,$010C            ; 
0DFA: 63              LD      H,E                 ; 
0DFB: 03              INC     BC                  ; 
0DFC: 0C              INC     C                   ; 
0DFD: 01 63 03        LD      BC,$0363            ; 
0E00: 0C              INC     C                   ; 
0E01: 01 63 03        LD      BC,$0363            ; 
0E04: 0C              INC     C                   ; 
0E05: 01 FF 02        LD      BC,$02FF            ; 
0E08: 00              NOP                         ; 
0E09: 03              INC     BC                  ; 
0E0A: 86              ADD     A,(HL)              ; 
0E0B: 02              LD      (BC),A              ; 
0E0C: 8A              ADC     A,D                 ; 
0E0D: 02              LD      (BC),A              ; 
0E0E: 71              LD      (HL),C              ; 
0E0F: 02              LD      (BC),A              ; 
0E10: 76              HALT                        ; 
0E11: 02              LD      (BC),A              ; 
0E12: 86              ADD     A,(HL)              ; 
0E13: 02              LD      (BC),A              ; 
0E14: 8A              ADC     A,D                 ; 
0E15: 02              LD      (BC),A              ; 
0E16: 71              LD      (HL),C              ; 
0E17: 02              LD      (BC),A              ; 
0E18: 76              HALT                        ; 
0E19: 02              LD      (BC),A              ; 
0E1A: 86              ADD     A,(HL)              ; 
0E1B: 02              LD      (BC),A              ; 
0E1C: 8A              ADC     A,D                 ; 
0E1D: 02              LD      (BC),A              ; 
0E1E: 71              LD      (HL),C              ; 
0E1F: 02              LD      (BC),A              ; 
0E20: 76              HALT                        ; 
0E21: 02              LD      (BC),A              ; 
0E22: 86              ADD     A,(HL)              ; 
0E23: 02              LD      (BC),A              ; 
0E24: 8A              ADC     A,D                 ; 
0E25: 02              LD      (BC),A              ; 
0E26: 71              LD      (HL),C              ; 
0E27: 02              LD      (BC),A              ; 
0E28: 76              HALT                        ; 
0E29: 02              LD      (BC),A              ; 
0E2A: 86              ADD     A,(HL)              ; 
0E2B: 02              LD      (BC),A              ; 
0E2C: 8A              ADC     A,D                 ; 
0E2D: 02              LD      (BC),A              ; 
0E2E: 71              LD      (HL),C              ; 
0E2F: 02              LD      (BC),A              ; 
0E30: 76              HALT                        ; 
0E31: 02              LD      (BC),A              ; 
0E32: 86              ADD     A,(HL)              ; 
0E33: 02              LD      (BC),A              ; 
0E34: 8A              ADC     A,D                 ; 
0E35: 02              LD      (BC),A              ; 
0E36: 71              LD      (HL),C              ; 
0E37: 02              LD      (BC),A              ; 
0E38: 76              HALT                        ; 
0E39: 02              LD      (BC),A              ; 
0E3A: 86              ADD     A,(HL)              ; 
0E3B: 02              LD      (BC),A              ; 
0E3C: 8A              ADC     A,D                 ; 
0E3D: 02              LD      (BC),A              ; 
0E3E: 71              LD      (HL),C              ; 
0E3F: 02              LD      (BC),A              ; 
0E40: 76              HALT                        ; 
0E41: 02              LD      (BC),A              ; 
0E42: 86              ADD     A,(HL)              ; 
0E43: 02              LD      (BC),A              ; 
0E44: 8A              ADC     A,D                 ; 
0E45: 02              LD      (BC),A              ; 
0E46: 71              LD      (HL),C              ; 
0E47: 02              LD      (BC),A              ; 
0E48: 76              HALT                        ; 
0E49: 02              LD      (BC),A              ; 
0E4A: 77              LD      (HL),A              ; 
0E4B: 01 0C 01        LD      BC,$010C            ; 
0E4E: 77              LD      (HL),A              ; 
0E4F: 01 0C 03        LD      BC,$030C            ; 
0E52: 77              LD      (HL),A              ; 
0E53: 01 0C 01        LD      BC,$010C            ; 
0E56: 77              LD      (HL),A              ; 
0E57: 03              INC     BC                  ; 
0E58: 0C              INC     C                   ; 
0E59: 01 69 01        LD      BC,$0169            ; 
0E5C: 0C              INC     C                   ; 
0E5D: 01 69 01        LD      BC,$0169            ; 
0E60: 0C              INC     C                   ; 
0E61: 03              INC     BC                  ; 
0E62: 69              LD      L,C                 ; 
0E63: 01 0C 01        LD      BC,$010C            ; 
0E66: 69              LD      L,C                 ; 
0E67: 03              INC     BC                  ; 
0E68: 0C              INC     C                   ; 
0E69: 01 69 03        LD      BC,$0369            ; 
0E6C: 0C              INC     C                   ; 
0E6D: 01 69 03        LD      BC,$0369            ; 
0E70: 0C              INC     C                   ; 
0E71: 01 8B 02        LD      BC,$028B            ; 
0E74: 73              LD      (HL),E              ; 
0E75: 02              LD      (BC),A              ; 
0E76: 76              HALT                        ; 
0E77: 02              LD      (BC),A              ; 
0E78: 7B              LD      A,E                 ; 
0E79: 02              LD      (BC),A              ; 
0E7A: 7B              LD      A,E                 ; 
0E7B: 02              LD      (BC),A              ; 
0E7C: 76              HALT                        ; 
0E7D: 02              LD      (BC),A              ; 
0E7E: 73              LD      (HL),E              ; 
0E7F: 02              LD      (BC),A              ; 
0E80: 8B              ADC     A,E                 ; 
0E81: 02              LD      (BC),A              ; 
0E82: FF              RST     0X38                ; 
0E83: 00              NOP                         ; 
0E84: 00              NOP                         ; 
0E85: 02              LD      (BC),A              ; 
0E86: 86              ADD     A,(HL)              ; 
0E87: 08              EX      AF,AF'              ; 
0E88: 81              ADD     A,C                 ; 
0E89: 08              EX      AF,AF'              ; 
0E8A: 86              ADD     A,(HL)              ; 
0E8B: 08              EX      AF,AF'              ; 
0E8C: 81              ADD     A,C                 ; 
0E8D: 08              EX      AF,AF'              ; 
0E8E: 86              ADD     A,(HL)              ; 
0E8F: 08              EX      AF,AF'              ; 
0E90: 81              ADD     A,C                 ; 
0E91: 08              EX      AF,AF'              ; 
0E92: 86              ADD     A,(HL)              ; 
0E93: 08              EX      AF,AF'              ; 
0E94: 81              ADD     A,C                 ; 
0E95: 08              EX      AF,AF'              ; 
0E96: 82              ADD     A,D                 ; 
0E97: 01 0C 01        LD      BC,$010C            ; 
0E9A: 82              ADD     A,D                 ; 
0E9B: 01 0C 03        LD      BC,$030C            ; 
0E9E: 82              ADD     A,D                 ; 
0E9F: 01 0C 01        LD      BC,$010C            ; 
0EA2: 82              ADD     A,D                 ; 
0EA3: 03              INC     BC                  ; 
0EA4: 0C              INC     C                   ; 
0EA5: 01 84 01        LD      BC,$0184            ; 
0EA8: 0C              INC     C                   ; 
0EA9: 01 84 01        LD      BC,$0184            ; 
0EAC: 0C              INC     C                   ; 
0EAD: 03              INC     BC                  ; 
0EAE: 84              ADD     A,H                 ; 
0EAF: 01 0C 01        LD      BC,$010C            ; 
0EB2: 84              ADD     A,H                 ; 
0EB3: 03              INC     BC                  ; 
0EB4: 0C              INC     C                   ; 
0EB5: 01 84 03        LD      BC,$0384            ; 
0EB8: 0C              INC     C                   ; 
0EB9: 01 84 03        LD      BC,$0384            ; 
0EBC: 0C              INC     C                   ; 
0EBD: 01 7B 08        LD      BC,$087B            ; 
0EC0: 76              HALT                        ; 
0EC1: 04              INC     B                   ; 
0EC2: 8B              ADC     A,E                 ; 
0EC3: 04              INC     B                   ; 
0EC4: FF              RST     0X38                ; 
0EC5: 00              NOP                         ; 
0EC6: 0C              INC     C                   ; 
0EC7: 05              DEC     B                   ; 
0EC8: 75              LD      (HL),L              ; 
0EC9: 0C              INC     C                   ; 
0ECA: 71              LD      (HL),C              ; 
0ECB: 0C              INC     C                   ; 
0ECC: 8A              ADC     A,D                 ; 
0ECD: 0C              INC     C                   ; 
0ECE: 86              ADD     A,(HL)              ; 
0ECF: 0C              INC     C                   ; 
0ED0: 0C              INC     C                   ; 
0ED1: 09              ADD     HL,BC               ; 
0ED2: 75              LD      (HL),L              ; 
0ED3: 03              INC     BC                  ; 
0ED4: 71              LD      (HL),C              ; 
0ED5: 09              ADD     HL,BC               ; 
0ED6: 8A              ADC     A,D                 ; 
0ED7: 03              INC     BC                  ; 
0ED8: 86              ADD     A,(HL)              ; 
0ED9: 04              INC     B                   ; 
0EDA: 8A              ADC     A,D                 ; 
0EDB: 04              INC     B                   ; 
0EDC: 71              LD      (HL),C              ; 
0EDD: 04              INC     B                   ; 
0EDE: 89              ADC     A,C                 ; 
0EDF: 04              INC     B                   ; 
0EE0: 70              LD      (HL),B              ; 
0EE1: 04              INC     B                   ; 
0EE2: 73              LD      (HL),E              ; 
0EE3: 04              INC     B                   ; 
0EE4: 8B              ADC     A,E                 ; 
0EE5: 0C              INC     C                   ; 
0EE6: 73              LD      (HL),E              ; 
0EE7: 0C              INC     C                   ; 
0EE8: 76              HALT                        ; 
0EE9: 0C              INC     C                   ; 
0EEA: 78              LD      A,B                 ; 
0EEB: 0C              INC     C                   ; 
0EEC: 0C              INC     C                   ; 
0EED: 09              ADD     HL,BC               ; 
0EEE: 79              LD      A,C                 ; 
0EEF: 03              INC     BC                  ; 
0EF0: 76              HALT                        ; 
0EF1: 09              ADD     HL,BC               ; 
0EF2: 72              LD      (HL),D              ; 
0EF3: 03              INC     BC                  ; 
0EF4: 8B              ADC     A,E                 ; 
0EF5: 04              INC     B                   ; 
0EF6: 89              ADC     A,C                 ; 
0EF7: 04              INC     B                   ; 
0EF8: 86              ADD     A,(HL)              ; 
0EF9: 04              INC     B                   ; 
0EFA: 72              LD      (HL),D              ; 
0EFB: 04              INC     B                   ; 
0EFC: 89              ADC     A,C                 ; 
0EFD: 04              INC     B                   ; 
0EFE: 76              HALT                        ; 
0EFF: 04              INC     B                   ; 
0F00: FF              RST     0X38                ; 
0F01: 00              NOP                         ; 
0F02: 0C              INC     C                   ; 
0F03: 05              DEC     B                   ; 
0F04: 71              LD      (HL),C              ; 
0F05: 0C              INC     C                   ; 
0F06: 8A              ADC     A,D                 ; 
0F07: 0C              INC     C                   ; 
0F08: 86              ADD     A,(HL)              ; 
0F09: 0C              INC     C                   ; 
0F0A: 85              ADD     A,L                 ; 
0F0B: 0C              INC     C                   ; 
0F0C: 0C              INC     C                   ; 
0F0D: 09              ADD     HL,BC               ; 
0F0E: 81              ADD     A,C                 ; 
0F0F: 03              INC     BC                  ; 
0F10: 8A              ADC     A,D                 ; 
0F11: 09              ADD     HL,BC               ; 
0F12: 86              ADD     A,(HL)              ; 
0F13: 03              INC     BC                  ; 
0F14: 85              ADD     A,L                 ; 
0F15: 04              INC     B                   ; 
0F16: 86              ADD     A,(HL)              ; 
0F17: 04              INC     B                   ; 
0F18: 8A              ADC     A,D                 ; 
0F19: 04              INC     B                   ; 
0F1A: 86              ADD     A,(HL)              ; 
0F1B: 04              INC     B                   ; 
0F1C: 89              ADC     A,C                 ; 
0F1D: 04              INC     B                   ; 
0F1E: 8B              ADC     A,E                 ; 
0F1F: 04              INC     B                   ; 
0F20: 88              ADC     A,B                 ; 
0F21: 0C              INC     C                   ; 
0F22: 8B              ADC     A,E                 ; 
0F23: 0C              INC     C                   ; 
0F24: 73              LD      (HL),E              ; 
0F25: 0C              INC     C                   ; 
0F26: 76              HALT                        ; 
0F27: 0C              INC     C                   ; 
0F28: 0C              INC     C                   ; 
0F29: 09              ADD     HL,BC               ; 
0F2A: 76              HALT                        ; 
0F2B: 03              INC     BC                  ; 
0F2C: 72              LD      (HL),D              ; 
0F2D: 09              ADD     HL,BC               ; 
0F2E: 8B              ADC     A,E                 ; 
0F2F: 03              INC     BC                  ; 
0F30: 8A              ADC     A,D                 ; 
0F31: 04              INC     B                   ; 
0F32: 86              ADD     A,(HL)              ; 
0F33: 04              INC     B                   ; 
0F34: 82              ADD     A,D                 ; 
0F35: 04              INC     B                   ; 
0F36: 8B              ADC     A,E                 ; 
0F37: 04              INC     B                   ; 
0F38: 89              ADC     A,C                 ; 
0F39: 04              INC     B                   ; 
0F3A: 82              ADD     A,D                 ; 
0F3B: 04              INC     B                   ; 
0F3C: FF              RST     0X38                ; 
0F3D: 00              NOP                         ; 
0F3E: 00              NOP                         ; 
0F3F: 03              INC     BC                  ; 
0F40: 75              LD      (HL),L              ; 
0F41: 18 75           JR      $FB8                ; {}
0F43: 18 75           JR      $FBA                ; {}
0F45: 18 71           JR      $FB8                ; {}
0F47: 0C              INC     C                   ; 
0F48: 75              LD      (HL),L              ; 
0F49: 0C              INC     C                   ; 
0F4A: 73              LD      (HL),E              ; 
0F4B: 18 73           JR      $FC0                ; {}
0F4D: 18 72           JR      $FC1                ; {}
0F4F: 18 76           JR      $FC7                ; {}
0F51: 0C              INC     C                   ; 
0F52: 78              LD      A,B                 ; 
0F53: 0C              INC     C                   ; 
0F54: FF              RST     0X38                ; 
0F55: FB              EI                          ; 

0F56: FF FF FF FF FF FF FF FF FF FF
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

