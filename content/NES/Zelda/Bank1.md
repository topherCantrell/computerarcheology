![Bank 1](Zelda.jpg)

# Bank 1

>>> cpu 6502

>>> binary 8000:Zelda.nes[4010:8010]

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](Hardware.md)

```html
<script src="/NES/Zelda/zelda.js"></script>
<script src="/js/BinaryData.js"></script>
<script src="/js/TileEngine.js"></script>
<script src="/js/CANVAS.js"></script>
```

# String Table

```code
StringTable: 
8000: 4C 80     ; __IT'S DANGEROUS TO GO____ALONE! TAKE THIS.
8002: 77 80     ; __MASTER USING IT AND___YOU CAN HAVE THIS.
8004: A1 80     ; _TAKE ANY ROAD YOU WANT.
8006: B9 80     ; _SECRET IS IN THE TREE____AT THE DEAD-END.
8008: E3 80     ; ___LET'S PLAY MONEY___MAKING GAME.
800A: 05 81     ; __PAY ME FOR THE DOOR_____REPAIR CHARGE.
800C: 2D 81     ; ____SHOW THIS TO THE_______OLD WOMAN.
800E: 52 81     ; ____MEET THE OLD MAN______AT THE GRAVE.
8010: 79 81     ; __BUY MEDICINE BEFORE__YOU GO.
8012: 97 81     ; __PAY ME AND I'LL TALK.
8014: AE 81     ; ___THIS AIN'T ENOUGH________TO TALK.
8016: D2 81     ; _______GO UP,UP,___THE MOUNTAIN AHEAD.
8018: F8 81     ; __GO NORTH,WEST,SOUTH,__WEST TO THE FOREST  OF MAZE.
801A: 2C 82     ; ____BOY, YOU'RE RICH!
801C: 41 82     ; _BUY SOMETHIN' WILL YA!
801E: 58 82     ; _____BOY, THIS IS___REALLY EXPENSIVE!
8020: 7D 82     ; _TAKE ANY ONE YOU WANT.
8022: 94 82     ; _____IT'S A SECRET_____TO EVERYBODY.
8024: B8 82     ; ___GRUMBLE,GRUMBLE...
8026: CD 82     ; __EASTMOST PENNINSULA_____IS THE SECRET.
8028: F5 82     ; _DODONGO DISLIKES SMOKE.
802A: 0D 83     ; _DID YOU GET THE SWORD_FROM THE OLD MAN ON_TOP OF THE WATERFALL?
802C: 4D 83     ; _____WALK INTO THE_______WATERFALL.
802E: 70 83     ; __SECRET POWER IS SAID___TO BE IN THE ARROW.
8030: 9C 83     ; ____DIGDOGGER HATES_CERTAIN KIND OF SOUND.
8032: C6 83     ; ____I BET YOU'D LIKE___TO HAVE MORE BOMBS.
8034: F0 83     ; ____IF YOU GO IN THE_DIRECTION OF THE ARROW.
8036: 1C 84     ; ____LEAVE YOUR LIFE_______OR MONEY.
8038: 3F 84     ; _THERE ARE SECRETS WHERE___FAIRIES DON'T LIVE.
803A: 6D 84     ; ____AIM AT THE EYES_______OF GOHMA.
803C: 90 84     ; __SOUTH OF ARROW MARK____HIDES A SECRET.
803E: B8 84     ; __THERE'S A SECRET IN__THE TIP OF THE NOSE.
8040: E3 84     ; ___SPECTACLE ROCK IS__AN ENTRANCE TO DEATH.
8042: 0E 85     ; 10TH ENEMY HAS THE BOMB.
8044: 26 85     ; _ONES WHO DOES NOT HAVE_TRIFORCE CAN'T GO IN.
8046: 53 85     ; ___PATRA HAS THE MAP.
8048: 68 85     ; __GO TO THE NEXT ROOM.
804A: 7E 85     ; _____EYES OF SKULL_____HAS A SECRET.
```

# Strings

```code
Strings: 
804C: 25 25 12 1D 2A 1C 24 0D 0A 17 10 0E                       ; "__IT'S DANGEROUS TO GO"
8058: 1B 18 1E 1C 24 1D 18 24 10 98                             ; .
8062: 25 25 25 25 0A 15 18 17 0E 29 24 1D                       ; "____ALONE! TAKE THIS."
806E: 0A 14 0E 24 1D 11 12 1C EC                                ; .

8077: 25 25 16 0A 1C 1D 0E 1B 24 1E 1C 12                       ; "__MASTER USING IT AND"
8083: 17 10 24 12 1D 24 0A 17 8D                                ; .
808C: 25 25 25 22 18 1E 24 0C 0A 17 24 11                       ; "___YOU CAN HAVE THIS."
8098: 0A 1F 0E 24 1D 11 12 1C EC                                ; .

80A1: 25 1D 0A 14 0E 24 0A 17 22 24 1B 18                       ; "_TAKE ANY ROAD YOU WANT."
80AD: 0A 0D 24 22 18 1E 24 20 0A 17 1D EC                       ; .

80B9: 25 1C 0E 0C 1B 0E 1D 24 12 1C 24 12                       ; "_SECRET IS IN THE TREE"
80C5: 17 24 1D 11 0E 24 1D 1B 0E 8E                             ; .
80CF: 25 25 25 25 0A 1D 24 1D 11 0E 24 0D                       ; "____AT THE DEAD-END."
80DB: 0E 0A 0D 2F 0E 17 0D EC                                   ; .

80E3: 25 25 25 15 0E 1D 2A 1C 24 19 15 0A                       ; "___LET'S PLAY MONEY"
80EF: 22 24 16 18 17 0E A2                                      ; .
80F6: 25 25 25 16 0A 14 12 17 10 24 10 0A                       ; "___MAKING GAME."
8102: 16 0E EC                                                  ; .

8105: 25 25 19 0A 22 24 16 0E 24 0F 18 1B                       ; "__PAY ME FOR THE DOOR"
8111: 24 1D 11 0E 24 0D 18 18 9B                                ; .
811A: 25 25 25 25 25 1B 0E 19 0A 12 1B 24                       ; "_____REPAIR CHARGE."
8126: 0C 11 0A 1B 10 0E EC                                      ; .

812D: 25 25 25 25 1C 11 18 20 24 1D 11 12                       ; "____SHOW THIS TO THE"
8139: 1C 24 1D 18 24 1D 11 8E                                   ; .
8141: 25 25 25 25 25 25 25 18 15 0D 24 20                       ; "_______OLD WOMAN."
814D: 18 16 0A 17 EC                                            ; .

8152: 25 25 25 25 16 0E 0E 1D 24 1D 11 0E                       ; "____MEET THE OLD MAN"
815E: 24 18 15 0D 24 16 0A 97                                   ; .
8166: 25 25 25 25 25 25 0A 1D 24 1D 11 0E                       ; "______AT THE GRAVE."
8172: 24 10 1B 0A 1F 0E EC                                      ; .

8179: 25 25 0B 1E 22 24 16 0E 0D 12 0C 12                       ; "__BUY MEDICINE BEFORE"
8185: 17 0E 24 0B 0E 0F 18 1B 8E                                ; .
818E: 25 25 22 18 1E 24 10 18 EC                                ; "__YOU GO."

8197: 25 25 19 0A 22 24 16 0E 24 0A 17 0D                       ; "__PAY ME AND I'LL TALK."
81A3: 24 12 2A 15 15 24 1D 0A 15 14 EC                          ; .

81AE: 25 25 25 1D 11 12 1C 24 0A 12 17 2A                       ; "___THIS AIN'T ENOUGH"
81BA: 1D 24 0E 17 18 1E 10 91                                   ; .
81C2: 25 25 25 25 25 25 25 25 1D 18 24 1D                       ; "________TO TALK."
81CE: 0A 15 14 EC                                               ; .

81D2: 25 25 25 25 25 25 25 10 18 24 1E 19                       ; "_______GO UP,UP,"
81DE: 28 1E 19 A8                                               ; .
81E2: 25 25 25 1D 11 0E 24 16 18 1E 17 1D                       ; "___THE MOUNTAIN AHEAD."
81EE: 0A 12 17 24 0A 11 0E 0A 0D EC                             ; .

81F8: 25 25 10 18 24 17 18 1B 1D 11 28 20                       ; "__GO NORTH,WEST,SOUTH,"
8204: 0E 1C 1D 28 1C 18 1E 1D 11 A8                             ; .
820E: 25 25 20 0E 1C 1D 24 1D 18 24 1D 11                       ; "__WEST TO THE FOREST  OF MAZE."
821A: 0E 24 0F 18 1B 0E 1C 5D 24 24 18 0F                       ; .
8226: 24 16 0A 23 0E EC                                         ; .

822C: 25 25 25 25 0B 18 22 28 24 22 18 1E                       ; "____BOY, YOU'RE RICH!"
8238: 2A 1B 0E 24 1B 12 0C 11 E9                                ; .

8241: 25 0B 1E 22 24 1C 18 16 0E 1D 11 12                       ; "_BUY SOMETHIN' WILL YA!"
824D: 17 2A 24 20 12 15 15 24 22 0A E9                          ; .

8258: 25 25 25 25 25 0B 18 22 28 24 1D 11                       ; "_____BOY, THIS IS"
8264: 12 1C 24 12 9C                                            ; .
8269: 25 25 25 1B 0E 0A 15 15 22 24 0E 21                       ; "___REALLY EXPENSIVE!"
8275: 19 0E 17 1C 12 1F 0E E9                                   ; .

827D: 25 1D 0A 14 0E 24 0A 17 22 24 18 17                       ; "_TAKE ANY ONE YOU WANT."
8289: 0E 24 22 18 1E 24 20 0A 17 1D EC                          ; .

8294: 25 25 25 25 25 12 1D 2A 1C 24 0A 24                       ; "_____IT'S A SECRET"
82A0: 1C 0E 0C 1B 0E 9D                                         ; .
82A6: 25 25 25 25 25 1D 18 24 0E 1F 0E 1B                       ; "_____TO EVERYBODY."
82B2: 22 0B 18 0D 22 EC                                         ; .

82B8: 25 25 25 10 1B 1E 16 0B 15 0E 28 10                       ; "___GRUMBLE,GRUMBLE..."
82C4: 1B 1E 16 0B 15 0E 2C 2C EC                                ; .

82CD: 25 25 0E 0A 1C 1D 16 18 1C 1D 24 19                       ; "__EASTMOST PENNINSULA"
82D9: 0E 17 17 12 17 1C 1E 15 8A                                ; .
82E2: 25 25 25 25 25 12 1C 24 1D 11 0E 24                       ; "_____IS THE SECRET."
82EE: 1C 0E 0C 1B 0E 1D EC                                      ; .

82F5: 25 0D 18 0D 18 17 10 18 24 0D 12 1C                       ; "_DODONGO DISLIKES SMOKE."
8301: 15 12 14 0E 1C 24 1C 16 18 14 0E EC                       ; .

830D: 25 0D 12 0D 24 22 18 1E 24 10 0E 1D                       ; "_DID YOU GET THE SWORD"
8319: 24 1D 11 0E 24 1C 20 18 1B 8D                             ; .
8323: 25 0F 1B 18 16 24 1D 11 0E 24 18 15                       ; "_FROM THE OLD MAN ON_TOP OF THE WATERFALL?"
832F: 0D 24 16 0A 17 24 18 57 25 1D 18 19                       ; .
833B: 24 18 0F 24 1D 11 0E 24 20 0A 1D 0E                       ; .
8347: 1B 0F 0A 15 15 EE                                         ; .

834D: 25 25 25 25 25 20 0A 15 14 24 12 17                       ; "_____WALK INTO THE"
8359: 1D 18 24 1D 11 8E                                         ; .
835F: 25 25 25 25 25 25 25 20 0A 1D 0E 1B                       ; "_______WATERFALL."
836B: 0F 0A 15 15 EC                                            ; .

8370: 25 25 1C 0E 0C 1B 0E 1D 24 19 18 20                       ; "__SECRET POWER IS SAID"
837C: 0E 1B 24 12 1C 24 1C 0A 12 8D                             ; .
8386: 25 25 25 1D 18 24 0B 0E 24 12 17 24                       ; "___TO BE IN THE ARROW."
8392: 1D 11 0E 24 0A 1B 1B 18 20 EC                             ; .

839C: 25 25 25 25 0D 12 10 0D 18 10 10 0E                       ; "____DIGDOGGER HATES"
83A8: 1B 24 11 0A 1D 0E 9C                                      ; .
83AF: 25 0C 0E 1B 1D 0A 12 17 24 14 12 17                       ; "_CERTAIN KIND OF SOUND."
83BB: 0D 24 18 0F 24 1C 18 1E 17 0D EC                          ; .

83C6: 25 25 25 25 12 24 0B 0E 1D 24 22 18                       ; "____I BET YOU'D LIKE"
83D2: 1E 2A 0D 24 15 12 14 8E                                   ; .
83DA: 25 25 25 1D 18 24 11 0A 1F 0E 24 16                       ; "___TO HAVE MORE BOMBS."
83E6: 18 1B 0E 24 0B 18 16 0B 1C EC                             ; .

83F0: 25 25 25 25 12 0F 24 22 18 1E 24 10                       ; "____IF YOU GO IN THE"
83FC: 18 24 12 17 24 1D 11 8E                                   ; .
8404: 25 0D 12 1B 0E 0C 1D 12 18 17 24 18                       ; "_DIRECTION OF THE ARROW."
8410: 0F 24 1D 11 0E 24 0A 1B 1B 18 20 EC                       ; .

841C: 25 25 25 25 15 0E 0A 1F 0E 24 22 18                       ; "____LEAVE YOUR LIFE"
8428: 1E 1B 24 15 12 0F 8E                                      ; .
842F: 25 25 25 25 25 25 25 18 1B 24 16 18                       ; "_______OR MONEY."
843B: 17 0E 22 EC                                               ; .

843F: 25 1D 11 0E 1B 0E 24 0A 1B 0E 24 1C                       ; "_THERE ARE SECRETS WHERE"
844B: 0E 0C 1B 0E 1D 1C 24 20 11 0E 1B 8E                       ; .
8457: 25 25 25 0F 0A 12 1B 12 0E 1C 24 0D                       ; "___FAIRIES DON'T LIVE."
8463: 18 17 2A 1D 24 15 12 1F 0E EC                             ; .

846D: 25 25 25 25 0A 12 16 24 0A 1D 24 1D                       ; "____AIM AT THE EYES"
8479: 11 0E 24 0E 22 0E 9C                                      ; .
8480: 25 25 25 25 25 25 25 18 0F 24 10 18                       ; "_______OF GOHMA."
848C: 11 16 0A EC                                               ; .

8490: 25 25 1C 18 1E 1D 11 24 18 0F 24 0A                       ; "__SOUTH OF ARROW MARK"
849C: 1B 1B 18 20 24 16 0A 1B 94                                ; .
84A5: 25 25 25 25 11 12 0D 0E 1C 24 0A 24                       ; "____HIDES A SECRET."
84B1: 1C 0E 0C 1B 0E 1D EC                                      ; .

84B8: 25 25 1D 11 0E 1B 0E 2A 1C 24 0A 24                       ; "__THERE'S A SECRET IN"
84C4: 1C 0E 0C 1B 0E 1D 24 12 97                                ; .
84CD: 25 25 1D 11 0E 24 1D 12 19 24 18 0F                       ; "__THE TIP OF THE NOSE."
84D9: 24 1D 11 0E 24 17 18 1C 0E EC                             ; .

84E3: 25 25 25 1C 19 0E 0C 1D 0A 0C 15 0E                       ; "___SPECTACLE ROCK IS"
84EF: 24 1B 18 0C 14 24 12 9C                                   ; .
84F7: 25 25 0A 17 24 0E 17 1D 1B 0A 17 0C                       ; "__AN ENTRANCE TO DEATH."
8503: 0E 24 1D 18 24 0D 0E 0A 1D 11 EC                          ; .

850E: 01 00 1D 11 24 0E 17 0E 16 22 24 11                       ; "10TH ENEMY HAS THE BOMB."
851A: 0A 1C 24 1D 11 0E 24 0B 18 16 0B EC                       ; .

8526: 25 18 17 0E 1C 24 20 11 18 24 0D 18                       ; "_ONES WHO DOES NOT HAVE"
8532: 0E 1C 24 17 18 1D 24 11 0A 1F 8E                          ; .
853D: 25 1D 1B 12 0F 18 1B 0C 0E 24 0C 0A                       ; "_TRIFORCE CAN'T GO IN."
8549: 17 2A 1D 24 10 18 24 12 17 EC                             ; .

8553: 25 25 25 19 0A 1D 1B 0A 24 11 0A 1C                       ; "___PATRA HAS THE MAP."
855F: 24 1D 11 0E 24 16 0A 19 EC                                ; .

8568: 25 25 10 18 24 1D 18 24 1D 11 0E 24                       ; "__GO TO THE NEXT ROOM."
8574: 17 0E 21 1D 24 1B 18 18 16 EC                             ; .

857E: 25 25 25 25 25 0E 22 0E 1C 24 18 0F                       ; "_____EYES OF SKULL"
858A: 24 1C 14 1E 15 95                                         ; .
8590: 25 25 25 25 25 11 0A 1C 24 0A 24 1C                       ; "_____HAS A SECRET."
859C: 0E 0C 1B 0E 1D EC                                         ; .

85A2: 40            RTI                       ;
85A3: 60            RTS                       ;
85A4: 42                              ;
85A5: 42                              ;
85A6: 04                              ;
85A7: 06 48         ASL   <$48                ; 
85A9: 0A            ASL   A                   ;
85AA: 4C 0E D0      JMP   $D00E               ; 
85AD: D2                              ;
85AE: D2                              ;
85AF: DC                              ;
85B0: DC                              ;
85B1: DE DE 62      DEC   $62DE,X             ;
85B4: 62                              ;
85B5: 62                              ;
85B6: 0A            ASL   A                   ;
85B7: 28            PLP                       ;
85B8: 00            BRK                       ;
85B9: 01 02         ORA   ($02,X)             ;
85BB: 01 02         ORA   ($02,X)             ;
85BD: 00            BRK                       ;
85BE: 02                              ;
85BF: 00            BRK                       ;
85C0: 01 00         ORA   ($00,X)             ;
85C2: 02                              ;
85C3: 01 02         ORA   ($02,X)             ;
85C5: 01 00         ORA   ($00,X)             ;
85C7: 01 00         ORA   ($00,X)             ;
85C9: 02                              ;
85CA: 02                              ;
85CB: 05 08         ORA   <$08                ; 
85CD: 0B                              ;
85CE: 0E 11 A9      ASL   $A911               ; 


85D1: 78            SEI                       ;
85D2: A0 80         LDY   #$80                ;
85D4: 20 A3 86      JSR   $86A3               ; 
85D7: AD 50 03      LDA   $0350               ; 
85DA: C9 72         CMP   #$72                ;
85DC: F0 0C         BEQ   $85EA               ; 
85DE: C9 71         CMP   #$71                ;
85E0: F0 08         BEQ   $85EA               ; 
85E2: C9 7B         CMP   #$7B                ;
85E4: B0 04         BCS   $85EA               ; 
85E6: C9 6E         CMP   #$6E                ;
85E8: B0 0F         BCS   $85F9               ; 
85EA: 20 14 73      JSR   $7314               ; 
85ED: F0 0A         BEQ   $85F9               ; 
85EF: A9 00         LDA   #$00                ;
85F1: 8D 50 03      STA   $0350               ; 
85F4: A9 00         LDA   #$00                ;
85F6: 85 AC         STA   <$AC                ; 
85F8: 60            RTS                       ;
85F9: AD 50 03      LDA   $0350               ; 
85FC: 38            SEC                       ;
85FD: E9 6A         SBC   #$6A                ;
85FF: A8            TAY                       ;
8600: B9 A2 85      LDA   $85A2,Y             ;
8603: 48            PHA                       ;
8604: 29 3F         AND   #$3F                ;
8606: 8D 15 04      STA   $0415               ; 
8609: 68            PLA                       ;
860A: 29 C0         AND   #$C0                ;
860C: 85 03         STA   <$03                ; 
860E: A9 FD         LDA   #$FD                ;
8610: 18            CLC                       ;
8611: 69 03         ADC   #$03                ;
8613: 88            DEY                       ;
8614: 10 FA         BPL   $8610               ; 
8616: A8            TAY                       ;
8617: A2 00         LDX   #$00                ;
8619: B9 7E 6A      LDA   $6A7E,Y             ;
861C: 9D 22 04      STA   $0422,X             ;
861F: 29 C0         AND   #$C0                ;
8621: 95 00         STA   $00,X               ;
8623: B9 BA 6A      LDA   $6ABA,Y             ;
8626: 9D 30 04      STA   $0430,X             ;
8629: C8            INY                       ;
862A: E8            INX                       ;
862B: E0 03         CPX   #$03                ;
862D: D0 EA         BNE   $8619               ; 
862F: A5 03         LDA   <$03                ; 
8631: 0A            ASL   A                   ;
8632: 2A            ROL   A                   ;
8633: 2A            ROL   A                   ;
8634: 05 00         ORA   <$00                ; 
8636: 85 00         STA   <$00                ; 
8638: A5 02         LDA   <$02                ; 
863A: 4A            LSR   A                   ;
863B: 4A            LSR   A                   ;
863C: 4A            LSR   A                   ;
863D: 4A            LSR   A                   ;
863E: 05 00         ORA   <$00                ; 
8640: 85 00         STA   <$00                ; 
8642: A5 01         LDA   <$01                ; 
8644: 4A            LSR   A                   ;
8645: 4A            LSR   A                   ;
8646: 05 00         ORA   <$00                ; 
8648: 8D 13 04      STA   $0413               ; 
864B: 29 20         AND   #$20                ;
864D: F0 48         BEQ   $8697               ; 
864F: A9 FF         LDA   #$FF                ;
8651: A0 06         LDY   #$06                ;
8653: C5 19         CMP   <$19                ; 
8655: 90 06         BCC   $865D               ; 
8657: 38            SEC                       ;
8658: E9 2B         SBC   #$2B                ;
865A: 88            DEY                       ;
865B: D0 F6         BNE   $8653               ; 
865D: BE CA 85      LDX   $85CA,Y             ;
8660: A0 02         LDY   #$02                ;
8662: BD B8 85      LDA   $85B8,X             ;
8665: 99 6C 04      STA   $046C,Y             ;
8668: CA            DEX                       ;
8669: 88            DEY                       ;
866A: 10 F6         BPL   $8662               ; 
866C: A5 1A         LDA   <$1A                ; 
866E: 29 01         AND   #$01                ;
8670: A8            TAY                       ;
8671: B9 B6 85      LDA   $85B6,Y             ;
8674: 8D 6F 04      STA   $046F               ; 
8677: A9 0A         LDA   #$0A                ;
8679: 8D 70 04      STA   $0470               ; 
867C: A0 14         LDY   #$14                ;
867E: A5 1A         LDA   <$1A                ; 
8680: 29 02         AND   #$02                ;
8682: F0 02         BEQ   $8686               ; 
8684: A0 32         LDY   #$32                ;
8686: 8C 71 04      STY   $0471               ; 
8689: A2 02         LDX   #$02                ;
868B: BC 6C 04      LDY   $046C,X             ;
868E: B9 6F 04      LDA   $046F,Y             ;
8691: 9D 48 04      STA   $0448,X             ;
8694: CA            DEX                       ;
8695: 10 F4         BPL   $868B               ; 
8697: A9 00         LDA   #$00                ; Clear string ...
8699: 8D 16 04      STA   $0416               ; ... pointer cursor
869C: AD 14 88      LDA   $8814               ; 
869F: 8D 5F 04      STA   $045F               ; 
86A2: 60            RTS                       ;

86A3: 95 70         STA   $70,X               ;
86A5: 94 84         STY   $84,X               ;
86A7: A9 00         LDA   #$00                ;
86A9: 9D 85 04      STA   $0485,X             ;
86AC: A9 81         LDA   #$81                ;
86AE: 9D BF 04      STA   $04BF,X             ;
86B1: A9 40         LDA   #$40                ;
86B3: 85 AC         STA   <$AC                ; 
86B5: A9 40         LDA   #$40                ;
86B7: 8D 51 03      STA   $0351               ; 
86BA: 8D 52 03      STA   $0352               ; 
86BD: A9 48         LDA   #$48                ;
86BF: 95 71         STA   $71,X               ;
86C1: A9 A8         LDA   #$A8                ;
86C3: 95 72         STA   $72,X               ;
86C5: 94 85         STY   $85,X               ;
86C7: 94 86         STY   $86,X               ;
86C9: 60            RTS                       ;


86CA: 22                              ;
86CB: C8            INY                       ;
86CC: 0D 21 24      ORA   $2421               ; 
86CF: 24 24         BIT   <$24                ; 
86D1: 24 24         BIT   <$24                ; 
86D3: 24 24         BIT   <$24                ; 
86D5: 24 24         BIT   <$24                ; 
86D7: 24 24         BIT   <$24                ; 
86D9: 24 FF         BIT   <$FF                ; 


86DB: A5 AD         LDA   <$AD                ; 
86DD: C9 04         CMP   #$04                ;
86DF: D0 06         BNE   $86E7               ; 
86E1: A5 15         LDA   <$15                ; 
86E3: 29 01         AND   #$01                ;
86E5: D0 38         BNE   $871F               ; 
86E7: 20 36 87      JSR   $8736               ; 
86EA: AD 50 03      LDA   $0350               ; 
86ED: C9 74         CMP   #$74                ;
86EF: D0 2B         BNE   $871C               ; 
86F1: AD 66 06      LDA   $0666               ; 
86F4: C9 02         CMP   #$02                ;
86F6: F0 24         BEQ   $871C               ; 
86F8: AC 56 06      LDY   $0656               ; 
86FB: C0 0F         CPY   #$0F                ;
86FD: D0 06         BNE   $8705               ; 
86FF: A5 F8         LDA   <$F8                ; 
8701: 29 40         AND   #$40                ;
8703: D0 0A         BNE   $870F               ; 
8705: A5 AC         LDA   <$AC                ; 
8707: C9 40         CMP   #$40                ;
8709: D0 03         BNE   $870E               ; 
870B: 20 F4 85      JSR   $85F4               ; 
870E: 60            RTS                       ;
870F: A9 04         LDA   #$04                ;
8711: 8D 02 06      STA   $0602               ; 
8714: EE 66 06      INC   $0666               ; 
8717: A9 07         LDA   #$07                ;
8719: 8D 56 06      STA   $0656               ; 
871C: 20 49 87      JSR   $8749               ; 
871F: A5 AD         LDA   <$AD                ; 
8721: 20 E2 E5      JSR   $E5E2               ; 

8724: 8B                              ;
8725: 87                              ;
8726: 15 88         ORA   $88,X               ;
8728: 7A                              ;
8729: 88            DEY                       ;
872A: F7                              ;
872B: 89                              ;
872C: 33                              ;
872D: 89                              ;
872E: 41 89         EOR   ($89,X)             ;
8730: F7                              ;
8731: 89                              ;

8732: 15 88         ORA   $88,X               ;
8734: F6 89         INC   $89,X               ;
8736: 20 93 FA      JSR   $FA93               ; 
8739: AC 50 03      LDY   $0350               ; 
873C: C0 7B         CPY   #$7B                ;
873E: B0 03         BCS   $8743               ; 
8740: 4C DB 77      JMP   $77DB               ; 
8743: 4C DF 77      JMP   $77DF               ; 
8746: 58            CLI                       ;
8747: 78            SEI                       ;
8748: 98            TYA                       ;
8749: AD 13 04      LDA   $0413               ; 
874C: 29 04         AND   #$04                ;
874E: F0 24         BEQ   $8774               ; 
8750: A9 02         LDA   #$02                ;
8752: 8D 21 04      STA   $0421               ; 
8755: AE 21 04      LDX   $0421               ; 
8758: BD 46 87      LDA   $8746,X             ;
875B: 85 83         STA   <$83                ; 
875D: A9 98         LDA   #$98                ;
875F: 85 97         STA   <$97                ; 
8761: BD 22 04      LDA   $0422,X             ;
8764: 29 3F         AND   #$3F                ;
8766: C9 3F         CMP   #$3F                ;
8768: F0 05         BEQ   $876F               ; 
876A: A2 13         LDX   #$13                ;
876C: 20 0E E7      JSR   $E70E               ; 
876F: CE 21 04      DEC   $0421               ; 
8772: 10 E1         BPL   $8755               ; 
8774: AD 13 04      LDA   $0413               ; 
8777: 29 08         AND   #$08                ;
8779: F0 0F         BEQ   $878A               ; 
877B: A9 30         LDA   #$30                ;
877D: 85 83         STA   <$83                ; 
877F: A9 AB         LDA   #$AB                ;
8781: 85 97         STA   <$97                ; 
8783: A9 18         LDA   #$18                ;
8785: A2 13         LDX   #$13                ;
8787: 20 0E E7      JSR   $E70E               ; 
878A: 60            RTS                       ;
878B: AD 13 04      LDA   $0413               ; 
878E: 29 08         AND   #$08                ;
8790: F0 62         BEQ   $87F4               ; 
8792: 20 01 88      JSR   $8801               ; 
8795: A9 21         LDA   #$21                ;
8797: 8D 05 03      STA   $0305               ; 
879A: A2 00         LDX   #$00                ;
879C: 8E 2E 04      STX   $042E               ; 
879F: 8E 2F 04      STX   $042F               ; 
87A2: BD 30 04      LDA   $0430,X             ;
87A5: D0 0B         BNE   $87B2               ; 
87A7: A2 24         LDX   #$24                ;
87A9: 86 01         STX   <$01                ; 
87AB: 86 02         STX   <$02                ; 
87AD: 86 03         STX   <$03                ; 
87AF: 4C BF 87      JMP   $87BF               ; 
87B2: 20 55 6E      JSR   $6E55               ; 
87B5: A2 24         LDX   #$24                ;
87B7: AD 13 04      LDA   $0413               ; 
87BA: 0A            ASL   A                   ;
87BB: 90 02         BCC   $87BF               ; 
87BD: A2 62         LDX   #$62                ;
87BF: 86 04         STX   <$04                ; 
87C1: AC 2F 04      LDY   $042F               ; 
87C4: A5 02         LDA   <$02                ; 
87C6: 20 F7 87      JSR   $87F7               ; 
87C9: 99 08 03      STA   $0308,Y             ;
87CC: A5 01         LDA   <$01                ; 
87CE: 20 F7 87      JSR   $87F7               ; 
87D1: 99 07 03      STA   $0307,Y             ;
87D4: A5 03         LDA   <$03                ; 
87D6: 99 09 03      STA   $0309,Y             ;
87D9: AD 2F 04      LDA   $042F               ; 
87DC: 18            CLC                       ;
87DD: 69 04         ADC   #$04                ;
87DF: 8D 2F 04      STA   $042F               ; 
87E2: EE 2E 04      INC   $042E               ; 
87E5: AE 2E 04      LDX   $042E               ; 
87E8: E0 03         CPX   #$03                ;
87EA: D0 B6         BNE   $87A2               ; 
87EC: A9 0A         LDA   #$0A                ;
87EE: 85 29         STA   <$29                ; 
87F0: D0 02         BNE   $87F4               ; 
87F2: 85 14         STA   <$14                ; 
87F4: E6 AD         INC   <$AD                ; 
87F6: 60            RTS                       ;
87F7: C9 24         CMP   #$24                ;
87F9: D0 05         BNE   $8800               ; 
87FB: AA            TAX                       ;
87FC: A5 04         LDA   <$04                ; 
87FE: 86 04         STX   <$04                ; 
8800: 60            RTS                       ;
8801: A0 10         LDY   #$10                ;
8803: B9 CA 86      LDA   $86CA,Y             ;
8806: 99 02 03      STA   $0302,Y             ;
8809: 88            DEY                       ;
880A: 10 F7         BPL   $8803               ; 
880C: 60            RTS                       ;


880D: 21 A4         AND   ($A4,X)             ;
880F: 01 24         ORA   ($24,X)             ;
8811: FF                              ;
8812: C4 E4         CPY   <$E4                ; 
8814: A4 20         LDY   <$20                ; 
8816: 1B                              ;
8817: F2                              ;


8818: A5 29         LDA   <$29                ; 
881A: D0 5D         BNE   $8879               ; 
881C: A9 06         LDA   #$06                ;
881E: 85 29         STA   <$29                ; 
8820: A0 04         LDY   #$04                ;
8822: B9 0D 88      LDA   $880D,Y             ;
8825: 99 02 03      STA   $0302,Y             ;
8828: 88            DEY                       ;
8829: 10 F7         BPL   $8822               ; 
882B: AD 5F 04      LDA   $045F               ; 
882E: 8D 03 03      STA   $0303               ; 
8831: EE 5F 04      INC   $045F               ; 
8834: AC 15 04      LDY   $0415               ; String pointer
8837: B9 00 80      LDA   $8000,Y             ; Get ...
883A: 85 00         STA   <$00                ; ... LSB
883C: C8            INY                       ; Next byte in pointer
883D: B9 00 80      LDA   $8000,Y             ; Get ...
8840: 85 01         STA   <$01                ; ... MSB
8842: AC 16 04      LDY   $0416               ; Get string pointer cursor
8845: EE 16 04      INC   $0416               ; Increment pointer
8848: B1 00         LDA   ($00),Y             ; Get next in string
884A: 29 3F         AND   #$3F                ; Drop top two bits
884C: C9 25         CMP   #$25                ;
884E: F0 DB         BEQ   $882B               ; 
8850: 8D 05 03      STA   $0305               ; 
8853: A9 10         LDA   #$10                ;
8855: 8D 04 06      STA   $0604               ; 
8858: B1 00         LDA   ($00),Y             ;
885A: 29 C0         AND   #$C0                ;
885C: F0 1B         BEQ   $8879               ; 
885E: A0 02         LDY   #$02                ;
8860: C9 C0         CMP   #$C0                ;
8862: F0 06         BEQ   $886A               ; 
8864: 88            DEY                       ;
8865: C9 40         CMP   #$40                ;
8867: F0 01         BEQ   $886A               ; 
8869: 88            DEY                       ;
886A: B9 12 88      LDA   $8812,Y             ;
886D: 8D 5F 04      STA   $045F               ; 
8870: C0 02         CPY   #$02                ;
8872: D0 05         BNE   $8879               ; 
8874: E6 AD         INC   <$AD                ; 
8876: 20 F4 85      JSR   $85F4               ; 
8879: 60            RTS                       ;

887A: AD 13 04      LDA   $0413               ; 
887D: 4A            LSR   A                   ;
887E: B0 18         BCS   $8898               ; 
8880: A9 08         LDA   #$08                ;
8882: 85 AD         STA   <$AD                ; 
8884: AD 50 03      LDA   $0350               ; 
8887: C9 71         CMP   #$71                ;
8889: D0 0C         BNE   $8897               ; 
888B: AD 7E 06      LDA   $067E               ; 
888E: 18            CLC                       ;
888F: 69 14         ADC   #$14                ;
8891: 8D 7E 06      STA   $067E               ; 
8894: 20 0C 73      JSR   $730C               ; 
8897: 60            RTS                       ;
8898: AD 7E 06      LDA   $067E               ; 
889B: D0 FA         BNE   $8897               ; 
889D: A2 02         LDX   #$02                ;
889F: BD 22 04      LDA   $0422,X             ;
88A2: 29 3F         AND   #$3F                ;
88A4: C9 3F         CMP   #$3F                ;
88A6: F0 13         BEQ   $88BB               ; 
88A8: A5 70         LDA   <$70                ; 
88AA: DD 46 87      CMP   $8746,X             ;
88AD: D0 0C         BNE   $88BB               ; 
88AF: A5 84         LDA   <$84                ; 
88B1: 38            SEC                       ;
88B2: E9 98         SBC   #$98                ;
88B4: 20 1F 70      JSR   $701F               ; 
88B7: C9 06         CMP   #$06                ;
88B9: 90 04         BCC   $88BF               ; 
88BB: CA            DEX                       ;
88BC: 10 E1         BPL   $889F               ; 
88BE: 60            RTS                       ;
88BF: 8E 38 04      STX   $0438               ; 
88C2: AD 13 04      LDA   $0413               ; 
88C5: 29 30         AND   #$30                ;
88C7: F0 17         BEQ   $88E0               ; 
88C9: 29 10         AND   #$10                ;
88CB: F0 0E         BEQ   $88DB               ; 
88CD: AD 6D 06      LDA   $066D               ; 
88D0: DD 30 04      CMP   $0430,X             ;
88D3: 90 5D         BCC   $8932               ; 
88D5: BD 30 04      LDA   $0430,X             ;
88D8: 20 DE 89      JSR   $89DE               ; 
88DB: A9 05         LDA   #$05                ;
88DD: 85 AD         STA   <$AD                ; 
88DF: 60            RTS                       ;
88E0: AD 13 04      LDA   $0413               ; 
88E3: 29 02         AND   #$02                ;
88E5: F0 0E         BEQ   $88F5               ; 
88E7: AD 6D 06      LDA   $066D               ; 
88EA: DD 30 04      CMP   $0430,X             ;
88ED: 90 43         BCC   $8932               ; 
88EF: BD 30 04      LDA   $0430,X             ;
88F2: 20 DE 89      JSR   $89DE               ; 
88F5: AD 13 04      LDA   $0413               ; 
88F8: 29 40         AND   #$40                ;
88FA: F0 13         BEQ   $890F               ; 
88FC: A0 40         LDY   #$40                ;
88FE: AD 50 03      LDA   $0350               ; 
8901: C9 6C         CMP   #$6C                ;
8903: F0 02         BEQ   $8907               ; 
8905: A0 B0         LDY   #$B0                ;
8907: CC 6F 06      CPY   $066F               ; 
890A: F0 03         BEQ   $890F               ; 
890C: 90 01         BCC   $890F               ; 
890E: 60            RTS                       ;
890F: 20 0C 73      JSR   $730C               ; 
8912: BD 22 04      LDA   $0422,X             ;
8915: 29 3F         AND   #$3F                ;
8917: 48            PHA                       ;
8918: A9 FF         LDA   #$FF                ;
891A: 9D 22 04      STA   $0422,X             ;
891D: 68            PLA                       ;
891E: 20 70 73      JSR   $7370               ; 
8921: A9 1E         LDA   #$1E                ;
8923: 20 F2 87      JSR   $87F2               ; 
8926: A9 40         LDA   #$40                ;
8928: 85 29         STA   <$29                ; 
892A: AD 13 04      LDA   $0413               ; 
892D: 29 F7         AND   #$F7                ;
892F: 8D 13 04      STA   $0413               ; 
8932: 60            RTS                       ;
8933: A5 29         LDA   <$29                ; 
8935: D0 03         BNE   $893A               ; 
8937: 8D 50 03      STA   $0350               ; 
893A: 60            RTS                       ;


893B: 14                              ;
893C: 14                              ;
893D: 16 14         ASL   $14,X               ;
893F: 18            CLC                       ;
8940: 1A                              ;


8941: AD 13 04      LDA   $0413               ; 
8944: 29 10         AND   #$10                ;
8946: F0 29         BEQ   $8971               ; 
8948: A9 00         LDA   #$00                ;
894A: AC 50 03      LDY   $0350               ; 
894D: C0 75         CPY   #$75                ;
894F: F0 02         BEQ   $8953               ; 
8951: A9 03         LDA   #$03                ;
8953: 18            CLC                       ;
8954: 6D 38 04      ADC   $0438               ; 
8957: A8            TAY                       ;
8958: B9 3B 89      LDA   $893B,Y             ;
895B: 8D 15 04      STA   $0415               ; 
895E: AD 14 88      LDA   $8814               ; 
8961: 8D 5F 04      STA   $045F               ; 
8964: A9 00         LDA   #$00                ;
8966: 8D 16 04      STA   $0416               ; 
8969: 20 2A 89      JSR   $892A               ; 
896C: A9 1E         LDA   #$1E                ;
896E: 4C F2 87      JMP   $87F2               ; 
8971: AD 50 03      LDA   $0350               ; 
8974: C9 7B         CMP   #$7B                ;
8976: 90 1A         BCC   $8992               ; 
8978: 20 01 88      JSR   $8801               ; 
897B: A9 24         LDA   #$24                ;
897D: 20 97 87      JSR   $8797               ; 
8980: A9 08         LDA   #$08                ;
8982: 8D 04 06      STA   $0604               ; 
8985: 20 0C 73      JSR   $730C               ; 
8988: A9 08         LDA   #$08                ;
898A: 85 AD         STA   <$AD                ; 
898C: AD 31 04      LDA   $0431               ; 
898F: 4C D6 89      JMP   $89D6               ; 
8992: AD 6D 06      LDA   $066D               ; 
8995: C9 0A         CMP   #$0A                ;
8997: 90 A1         BCC   $893A               ; 
8999: A9 08         LDA   #$08                ;
899B: 8D 04 06      STA   $0604               ; 
899E: A0 02         LDY   #$02                ;
89A0: B9 48 04      LDA   $0448,Y             ;
89A3: 99 30 04      STA   $0430,Y             ;
89A6: 88            DEY                       ;
89A7: 10 F7         BPL   $89A0               ; 
89A9: 20 92 87      JSR   $8792               ; 
89AC: A9 08         LDA   #$08                ;
89AE: 85 AD         STA   <$AD                ; 
89B0: A0 01         LDY   #$01                ;
89B2: AD 48 04      LDA   $0448               ; 
89B5: 20 E6 89      JSR   $89E6               ; 
89B8: A0 05         LDY   #$05                ;
89BA: AD 49 04      LDA   $0449               ; 
89BD: 20 E6 89      JSR   $89E6               ; 
89C0: A0 09         LDY   #$09                ;
89C2: AD 4A 04      LDA   $044A               ; 
89C5: 20 E6 89      JSR   $89E6               ; 
89C8: AE 38 04      LDX   $0438               ; 
89CB: BD 48 04      LDA   $0448,X             ;
89CE: C9 14         CMP   #$14                ;
89D0: F0 04         BEQ   $89D6               ; 
89D2: C9 32         CMP   #$32                ;
89D4: D0 08         BNE   $89DE               ; 
89D6: 18            CLC                       ;
89D7: 6D 7D 06      ADC   $067D               ; 
89DA: 8D 7D 06      STA   $067D               ; 
89DD: 60            RTS                       ;
89DE: 18            CLC                       ;
89DF: 6D 7E 06      ADC   $067E               ; 
89E2: 8D 7E 06      STA   $067E               ; 
89E5: 60            RTS                       ;
89E6: A2 64         LDX   #$64                ;
89E8: C9 14         CMP   #$14                ;
89EA: F0 06         BEQ   $89F2               ; 
89EC: C9 32         CMP   #$32                ;
89EE: F0 02         BEQ   $89F2               ; 
89F0: A2 62         LDX   #$62                ;
89F2: 8A            TXA                       ;
89F3: 99 06 03      STA   $0306,Y             ;
89F6: 60            RTS                       ;
89F7: A9 2A         LDA   #$2A                ;
89F9: 4C F2 87      JMP   $87F2               ; 
89FC: AD 14 88      LDA   $8814               ; 
89FF: 8D 5F 04      STA   $045F               ; 
8A02: A5 10         LDA   <$10                ; 
8A04: 20 E2 E5      JSR   $E5E2               ; 
8A07: AD 8C 23      LDA   $238C               ; 
8A0A: 8A            TXA                       ;
8A0B: 23                              ;
8A0C: 8A            TXA                       ;
8A0D: 69 8A         ADC   #$8A                ;
8A0F: 69 8A         ADC   #$8A                ;
8A11: 23                              ;
8A12: 8A            TXA                       ;
8A13: 69 8A         ADC   #$8A                ;
8A15: 23                              ;
8A16: 8A            TXA                       ;
8A17: 69 8A         ADC   #$8A                ;
8A19: 84 8A         STY   <$8A                ; 
8A1B: 28            PLP                       ;
8A1C: 26 2E         ROL   <$2E                ; 
8A1E: 30 32         BMI   $8A52               ; 
8A20: 3E 3E 34      ROL   $343E,X             ;
8A23: A9 78         LDA   #$78                ;
8A25: A0 80         LDY   #$80                ;
8A27: 20 A3 86      JSR   $86A3               ; 
8A2A: BD 4F 03      LDA   $034F,X             ;
8A2D: 38            SEC                       ;
8A2E: E9 4B         SBC   #$4B                ;
8A30: A8            TAY                       ;
8A31: B9 1B 8A      LDA   $8A1B,Y             ;
8A34: 8D 15 04      STA   $0415               ; 
8A37: AD 50 03      LDA   $0350               ; 
8A3A: C9 4F         CMP   #$4F                ;
8A3C: D0 20         BNE   $8A5E               ; 
8A3E: F0 12         BEQ   $8A52               ; 
8A40: A9 78         LDA   #$78                ;
8A42: A0 80         LDY   #$80                ;
8A44: 20 A3 86      JSR   $86A3               ; 
8A47: A9 36         LDA   #$36                ;
8A49: 8D 15 04      STA   $0415               ; 
8A4C: AD 14 88      LDA   $8814               ; 
8A4F: 8D 5F 04      STA   $045F               ; 
8A52: 20 14 73      JSR   $7314               ; 
8A55: F0 07         BEQ   $8A5E               ; 
8A57: A9 00         LDA   #$00                ;
8A59: 85 AC         STA   <$AC                ; 
8A5B: 4C B1 FE      JMP   $FEB1               ; 
8A5E: 4C D3 8A      JMP   $8AD3               ; 


8A61: 2A            ROL   A                   ;
8A62: 38            SEC                       ;
8A63: 3A                              ;
8A64: 2C 40 42      BIT   $4240               ; 
8A67: 42                              ;
8A68: 3C                              ;
8A69: A9 78         LDA   #$78                ;
8A6B: A0 80         LDY   #$80                ;
8A6D: 20 A3 86      JSR   $86A3               ; 
8A70: BD 4F 03      LDA   $034F,X             ;
8A73: 38            SEC                       ;
8A74: E9 4B         SBC   #$4B                ;
8A76: A8            TAY                       ;
8A77: B9 61 8A      LDA   $8A61,Y             ;
8A7A: 8D 15 04      STA   $0415               ; 
8A7D: 4C D3 8A      JMP   $8AD3               ; 
8A80: 44                              ;
8A81: 46 48         LSR   <$48                ; 
8A83: 4A            LSR   A                   ;
8A84: A9 78         LDA   #$78                ;
8A86: A0 80         LDY   #$80                ;
8A88: 20 A3 86      JSR   $86A3               ; 
8A8B: 20 D3 8A      JSR   $8AD3               ; 
8A8E: BD 4F 03      LDA   $034F,X             ;
8A91: 48            PHA                       ;
8A92: 38            SEC                       ;
8A93: E9 4B         SBC   #$4B                ;
8A95: A8            TAY                       ;
8A96: B9 80 8A      LDA   $8A80,Y             ;
8A99: 8D 15 04      STA   $0415               ; 
8A9C: 68            PLA                       ;
8A9D: C9 4B         CMP   #$4B                ;
8A9F: D0 12         BNE   $8AB3               ; 
8AA1: AD 71 06      LDA   $0671               ; 
8AA4: C9 FF         CMP   #$FF                ;
8AA6: D0 0B         BNE   $8AB3               ; 
8AA8: A9 01         LDA   #$01                ;
8AAA: 8D CE 04      STA   $04CE               ; 
8AAD: 4A            LSR   A                   ;
8AAE: 85 AC         STA   <$AC                ; 
8AB0: 20 B1 FE      JSR   $FEB1               ; 
8AB3: 60            RTS                       ;
8AB4: A9 78         LDA   #$78                ;
8AB6: A0 80         LDY   #$80                ;
8AB8: 20 A3 86      JSR   $86A3               ; 
8ABB: A9 24         LDA   #$24                ;
8ABD: 8D 15 04      STA   $0415               ; 
8AC0: AD 14 88      LDA   $8814               ; 
8AC3: 8D 5F 04      STA   $045F               ; 
8AC6: 20 14 73      JSR   $7314               ; 
8AC9: F0 08         BEQ   $8AD3               ; 
8ACB: A9 00         LDA   #$00                ;
8ACD: 85 AC         STA   <$AC                ; 
8ACF: 8D 50 03      STA   $0350               ; 
8AD2: 60            RTS                       ;
8AD3: A9 08         LDA   #$08                ;
8AD5: 8D 02 06      STA   $0602               ; 
8AD8: 60            RTS                       ;
8AD9: A5 10         LDA   <$10                ; 
8ADB: C9 03         CMP   #$03                ;
8ADD: 90 08         BCC   $8AE7               ; 
8ADF: C9 05         CMP   #$05                ;
8AE1: F0 04         BEQ   $8AE7               ; 
8AE3: C9 07         CMP   #$07                ;
8AE5: D0 03         BNE   $8AEA               ; 
8AE7: 4C 11 8B      JMP   $8B11               ; 
8AEA: 20 9D 8B      JSR   $8B9D               ; 
8AED: A5 AD         LDA   <$AD                ; 
8AEF: 20 E2 E5      JSR   $E5E2               ; 
8AF2: F8            SED                       ;
8AF3: 8A            TXA                       ;
8AF4: 15 88         ORA   $88,X               ;
8AF6: FF                              ;
8AF7: 8A            TXA                       ;
8AF8: A9 00         LDA   #$00                ;
8AFA: 8D 16 04      STA   $0416               ; 
8AFD: E6 AD         INC   <$AD                ; 
8AFF: 60            RTS                       ;
8B00: 20 D0 79      JSR   $79D0               ; 
8B03: AD 06 04      LDA   $0406               ; 
8B06: F0 08         BEQ   $8B10               ; 
8B08: 8D CC 04      STA   $04CC               ; 
8B0B: A9 00         LDA   #$00                ;
8B0D: 8D 06 04      STA   $0406               ; 
8B10: 60            RTS                       ;
8B11: A5 AD         LDA   <$AD                ; 
8B13: C9 04         CMP   #$04                ;
8B15: D0 06         BNE   $8B1D               ; 
8B17: A5 15         LDA   <$15                ; 
8B19: 29 01         AND   #$01                ;
8B1B: D0 19         BNE   $8B36               ; 
8B1D: 20 9D 8B      JSR   $8B9D               ; 
8B20: AD 50 03      LDA   $0350               ; 
8B23: C9 4F         CMP   #$4F                ;
8B25: D0 0F         BNE   $8B36               ; 
8B27: A9 78         LDA   #$78                ;
8B29: 85 83         STA   <$83                ; 
8B2B: A9 98         LDA   #$98                ;
8B2D: 85 97         STA   <$97                ; 
8B2F: A9 18         LDA   #$18                ;
8B31: A2 13         LDX   #$13                ;
8B33: 20 0E E7      JSR   $E70E               ; 
8B36: A5 AD         LDA   <$AD                ; 
8B38: 20 E2 E5      JSR   $E5E2               ; 
8B3B: 45 8B         EOR   <$8B                ; 
8B3D: 15 88         ORA   $88,X               ;
8B3F: 57                              ;
8B40: 8B                              ;
8B41: F7                              ;
8B42: 89                              ;
8B43: 95 8B         STA   $8B,X               ;
8B45: AD 50 03      LDA   $0350               ; 
8B48: C9 4F         CMP   #$4F                ;
8B4A: D0 04         BNE   $8B50               ; 
8B4C: A9 6C         LDA   #$6C                ;
8B4E: 85 14         STA   <$14                ; 
8B50: A9 0A         LDA   #$0A                ;
8B52: 85 29         STA   <$29                ; 
8B54: E6 AD         INC   <$AD                ; 
8B56: 60            RTS                       ;
8B57: AD 50 03      LDA   $0350               ; 
8B5A: C9 4F         CMP   #$4F                ;
8B5C: D0 12         BNE   $8B70               ; 
8B5E: A5 70         LDA   <$70                ; 
8B60: C9 78         CMP   #$78                ;
8B62: D0 0C         BNE   $8B70               ; 
8B64: A5 84         LDA   <$84                ; 
8B66: 38            SEC                       ;
8B67: E9 98         SBC   #$98                ;
8B69: 20 1F 70      JSR   $701F               ; 
8B6C: C9 06         CMP   #$06                ;
8B6E: 90 01         BCC   $8B71               ; 
8B70: 60            RTS                       ;
8B71: A9 64         LDA   #$64                ;
8B73: CD 6D 06      CMP   $066D               ; 
8B76: F0 02         BEQ   $8B7A               ; 
8B78: B0 F6         BCS   $8B70               ; 
8B7A: 18            CLC                       ;
8B7B: 6D 7E 06      ADC   $067E               ; 
8B7E: 8D 7E 06      STA   $067E               ; 
8B81: A9 08         LDA   #$08                ;
8B83: 8D 04 06      STA   $0604               ; 
8B86: AD 7C 06      LDA   $067C               ; 
8B89: 18            CLC                       ;
8B8A: 69 04         ADC   #$04                ;
8B8C: 8D 7C 06      STA   $067C               ; 
8B8F: 8D 58 06      STA   $0658               ; 
8B92: 4C 8D 8C      JMP   $8C8D               ; 
8B95: A5 29         LDA   <$29                ; 
8B97: D0 03         BNE   $8B9C               ; 
8B99: 8D 50 03      STA   $0350               ; 
8B9C: 60            RTS                       ;
8B9D: 20 00 8B      JSR   $8B00               ; 
8BA0: 20 93 FA      JSR   $FA93               ; 
8BA3: 4C DB 77      JMP   $77DB               ; 
8BA6: A5 AD         LDA   <$AD                ; 
8BA8: C9 04         CMP   #$04                ;
8BAA: D0 06         BNE   $8BB2               ; 
8BAC: A5 15         LDA   <$15                ; 
8BAE: 29 01         AND   #$01                ;
8BB0: D0 06         BNE   $8BB8               ; 
8BB2: 20 9D 8B      JSR   $8B9D               ; 
8BB5: 20 CB 8B      JSR   $8BCB               ; 
8BB8: A5 AD         LDA   <$AD                ; 
8BBA: 20 E2 E5      JSR   $E5E2               ; 
8BBD: E6 8B         INC   <$8B                ; 
8BBF: 15 88         ORA   $88,X               ;
8BC1: EF                              ;
8BC2: 8B                              ;
8BC3: F7                              ;
8BC4: 89                              ;
8BC5: 95 8B         STA   $8B,X               ;
8BC7: 58            CLI                       ;
8BC8: 98            TYA                       ;
8BC9: 1A                              ;
8BCA: 18            CLC                       ;
8BCB: A2 01         LDX   #$01                ;
8BCD: 8A            TXA                       ;
8BCE: 48            PHA                       ;
8BCF: BD C7 8B      LDA   $8BC7,X             ;
8BD2: 85 83         STA   <$83                ; 
8BD4: A9 98         LDA   #$98                ;
8BD6: 85 97         STA   <$97                ; 
8BD8: BD C9 8B      LDA   $8BC9,X             ;
8BDB: A2 13         LDX   #$13                ;
8BDD: 20 0E E7      JSR   $E70E               ; 
8BE0: 68            PLA                       ;
8BE1: AA            TAX                       ;
8BE2: CA            DEX                       ;
8BE3: 10 E8         BPL   $8BCD               ; 
8BE5: 60            RTS                       ;
8BE6: A9 0A         LDA   #$0A                ;
8BE8: 85 29         STA   <$29                ; 
8BEA: A9 76         LDA   #$76                ;
8BEC: 4C F2 87      JMP   $87F2               ; 
8BEF: A2 01         LDX   #$01                ;
8BF1: A5 70         LDA   <$70                ; 
8BF3: DD C7 8B      CMP   $8BC7,X             ;
8BF6: D0 0C         BNE   $8C04               ; 
8BF8: A5 84         LDA   <$84                ; 
8BFA: 38            SEC                       ;
8BFB: E9 98         SBC   #$98                ;
8BFD: 20 1F 70      JSR   $701F               ; 
8C00: C9 06         CMP   #$06                ;
8C02: 90 04         BCC   $8C08               ; 
8C04: CA            DEX                       ;
8C05: 10 EA         BPL   $8BF1               ; 
8C07: 60            RTS                       ;
8C08: E0 00         CPX   #$00                ;
8C0A: F0 13         BEQ   $8C1F               ; 
8C0C: A9 32         LDA   #$32                ;
8C0E: CD 6D 06      CMP   $066D               ; 
8C11: F0 02         BEQ   $8C15               ; 
8C13: B0 F2         BCS   $8C07               ; 
8C15: 18            CLC                       ;
8C16: 6D 7E 06      ADC   $067E               ; 
8C19: 8D 7E 06      STA   $067E               ; 
8C1C: 4C 4D 8C      JMP   $8C4D               ; 
8C1F: AD 6F 06      LDA   $066F               ; 
8C22: 29 F0         AND   #$F0                ;
8C24: C9 30         CMP   #$30                ;
8C26: B0 0B         BCS   $8C33               ; 
8C28: 8D 6F 06      STA   $066F               ; 
8C2B: A9 00         LDA   #$00                ;
8C2D: 8D 70 06      STA   $0670               ; 
8C30: 4C 4D 8C      JMP   $8C4D               ; 
8C33: AD 6F 06      LDA   $066F               ; 
8C36: 48            PHA                       ;
8C37: 29 F0         AND   #$F0                ;
8C39: 38            SEC                       ;
8C3A: E9 10         SBC   #$10                ;
8C3C: 85 00         STA   <$00                ; 
8C3E: 68            PLA                       ;
8C3F: 29 0F         AND   #$0F                ;
8C41: 38            SEC                       ;
8C42: E9 01         SBC   #$01                ;
8C44: 10 02         BPL   $8C48               ; 
8C46: A9 00         LDA   #$00                ;
8C48: 05 00         ORA   <$00                ; 
8C4A: 8D 6F 06      STA   $066F               ; 
8C4D: A9 08         LDA   #$08                ;
8C4F: 8D 04 06      STA   $0604               ; 
8C52: A9 01         LDA   #$01                ;
8C54: 8D CE 04      STA   $04CE               ; 
8C57: 4C 8D 8C      JMP   $8C8D               ; 
8C5A: A5 AD         LDA   <$AD                ; 
8C5C: C9 03         CMP   #$03                ;
8C5E: D0 06         BNE   $8C66               ; 
8C60: A5 15         LDA   <$15                ; 
8C62: 29 01         AND   #$01                ;
8C64: D0 09         BNE   $8C6F               ; 
8C66: 20 00 8B      JSR   $8B00               ; 
8C69: 20 93 FA      JSR   $FA93               ; 
8C6C: 20 DF 77      JSR   $77DF               ; 
8C6F: A5 AD         LDA   <$AD                ; 
8C71: 20 E2 E5      JSR   $E5E2               ; 
8C74: 15 88         ORA   $88,X               ;
8C76: 7C                              ;
8C77: 8C F7 89      STY   $89F7               ; 
8C7A: 99 8C A0      STA   $A08C,Y             ;
8C7D: 0F                              ;
8C7E: B9 AC 00      LDA   $00AC,Y             ;
8C81: 0A            ASL   A                   ;
8C82: 90 29         BCC   $8CAD               ; 
8C84: A9 40         LDA   #$40                ;
8C86: 85 AC         STA   <$AC                ; 
8C88: A9 04         LDA   #$04                ;
8C8A: 8D 02 06      STA   $0602               ; 
8C8D: 20 0C 73      JSR   $730C               ; 
8C90: A9 40         LDA   #$40                ;
8C92: 85 29         STA   <$29                ; 
8C94: A9 1E         LDA   #$1E                ;
8C96: 4C F2 87      JMP   $87F2               ; 
8C99: 20 23 F2      JSR   $F223               ; 
8C9C: A5 29         LDA   <$29                ; 
8C9E: D0 0D         BNE   $8CAD               ; 
8CA0: A0 0F         LDY   #$0F                ;
8CA2: 99 AC 00      STA   $00AC,Y             ;
8CA5: 8D 5D 06      STA   $065D               ; 
8CA8: 85 AC         STA   <$AC                ; 
8CAA: 8D 50 03      STA   $0350               ; 
8CAD: 60            RTS                       ;
8CAE: FF                              ;
8CAF: FF                              ;
8CB0: FF                              ;
8CB1: FF                              ;
8CB2: FF                              ;
8CB3: FF                              ;
8CB4: FF                              ;
8CB5: FF                              ;
8CB6: FF                              ;
8CB7: FF                              ;
8CB8: FF                              ;
8CB9: FF                              ;
8CBA: FF                              ;
8CBB: FF                              ;
8CBC: FF                              ;
8CBD: FF                              ;
8CBE: FF                              ;
8CBF: FF                              ;
8CC0: FF                              ;
8CC1: FF                              ;
8CC2: FF                              ;
8CC3: FF                              ;
8CC4: FF                              ;
8CC5: FF                              ;
8CC6: FF                              ;
8CC7: FF                              ;
8CC8: FF                              ;
8CC9: FF                              ;
8CCA: FF                              ;
8CCB: FF                              ;
8CCC: FF                              ;
8CCD: FF                              ;
8CCE: FF                              ;
8CCF: FF                              ;
8CD0: FF                              ;
8CD1: FF                              ;
8CD2: FF                              ;
8CD3: FF                              ;
8CD4: FF                              ;
8CD5: FF                              ;
8CD6: FF                              ;
8CD7: FF                              ;
8CD8: FF                              ;
8CD9: FF                              ;
8CDA: FF                              ;
8CDB: FF                              ;
8CDC: FF                              ;
8CDD: FF                              ;
8CDE: FF                              ;
8CDF: FF                              ;
8CE0: FF                              ;
8CE1: FF                              ;
8CE2: FF                              ;
8CE3: FF                              ;
8CE4: FF                              ;
8CE5: FF                              ;
8CE6: FF                              ;
8CE7: FF                              ;
8CE8: FF                              ;
8CE9: FF                              ;
8CEA: FF                              ;
8CEB: FF                              ;
8CEC: FF                              ;
8CED: FF                              ;
8CEE: FF                              ;
8CEF: FF                              ;
8CF0: FF                              ;
8CF1: FF                              ;
8CF2: FF                              ;
8CF3: FF                              ;
8CF4: FF                              ;
8CF5: FF                              ;
8CF6: FF                              ;
8CF7: FF                              ;
8CF8: FF                              ;
8CF9: FF                              ;
8CFA: FF                              ;
8CFB: FF                              ;
8CFC: FF                              ;
8CFD: FF                              ;
8CFE: FF                              ;
8CFF: FF                              ;


8D00: A9 00         LDA   #$00                ;
8D02: 85 00         STA   <$00                ; 
8D04: A9 A5         LDA   #$A5                ;
8D06: 85 01         STA   <$01                ; 
8D08: A9 90         LDA   #$90                ;
8D0A: 85 02         STA   <$02                ; 
8D0C: A9 6C         LDA   #$6C                ;
8D0E: 85 03         STA   <$03                ; 
8D10: A0 00         LDY   #$00                ;
8D12: B1 00         LDA   ($00),Y             ;
8D14: 91 02         STA   ($02),Y             ;
8D16: A5 00         LDA   <$00                ; 
8D18: 18            CLC                       ;
8D19: 69 01         ADC   #$01                ;
8D1B: 85 00         STA   <$00                ; 
8D1D: A5 01         LDA   <$01                ; 
8D1F: 69 00         ADC   #$00                ;
8D21: 85 01         STA   <$01                ; 
8D23: A5 02         LDA   <$02                ; 
8D25: 18            CLC                       ;
8D26: 69 01         ADC   #$01                ;
8D28: 85 02         STA   <$02                ; 
8D2A: A5 03         LDA   <$03                ; 
8D2C: 69 00         ADC   #$00                ;
8D2E: 85 03         STA   <$03                ; 
8D30: C9 7F         CMP   #$7F                ;
8D32: D0 DE         BNE   $8D12               ; 
8D34: A5 02         LDA   <$02                ; 
8D36: C9 00         CMP   #$00                ;
8D38: D0 D8         BNE   $8D12               ; 
8D3A: 60            RTS                       ;

; Splash tile set information

; ROM Pointers
8D3B: B4 8D  ; Sprites
8D3D: B4 96  ; Background
;
; Counts
8D3F: 09 00  ; Sprites 144 tiles
8D41: 08 20  ; Background 130 tiles
;
; VRAM address
8D43: 07 00  ; Sprites   
8D45: 17 00  ; Background
```

# Init VRAM

```code
InitVRAM: 
; Duplicated in 1:8012
;
; Copy tile images for splash screen. The text characters are already in the tile
; memory from 1000-16FF. The first 700 bytes of each VRAM tile bank are untouched.
; VRAM 0000-06FF Untouched (common sprites)
; VRAM 0700-0FFF Splash sprite tiles
; VRAM 1000-16FF Untouched (common background)
; VRAM 1700-1F1F Splash background
;
8D47: 20 25 E6      JSR   $E625               ; Turn off all video
8D4A: AD 02 20      LDA   $2002               ; Clear address latch (and scroll)
8D4D: AD 1D 05      LDA   $051D               ; Set pointer
8D50: 0A            ASL   A                   ; *2 bytes per structure per set
8D51: AA            TAX                       ; Index register
8D52: BD 3B 8D      LDA   $8D3B,X             ; Read LSB of ...
8D55: 85 00         STA   <$00                ; ... ROM pointer
8D57: BD 3F 8D      LDA   $8D3F,X             ; Read MSB of ...
8D5A: 85 02         STA   <$02                ; ... count
8D5C: BD 43 8D      LDA   $8D43,X             ; Read MSB of ...
8D5F: 8D 06 20      STA   $2006               ; ... VRAM address
8D62: E8            INX                       ; Next in 2 byte pointer
8D63: BD 3B 8D      LDA   $8D3B,X             ; Read MSB of ...
8D66: 85 01         STA   <$01                ; ... ROM pointer
8D68: BD 3F 8D      LDA   $8D3F,X             ; Read LSB of ...
8D6B: 85 03         STA   <$03                ; ... count
8D6D: BD 43 8D      LDA   $8D43,X             ; Read LSB of VRAM address
8D70: 20 84 8D      JSR   $8D84               ; Do the copy (51D is incremented in routine)
8D73: AD 1D 05      LDA   $051D               ; Set count
8D76: C9 02         CMP   #$02                ; All done?
8D78: D0 D3         BNE   $8D4D               ; No ... do all sets
8D7A: A9 A5         LDA   #$A5                ; Make note that ...
8D7C: 85 F6         STA   <$F6                ; ... these tiles have been set
8D7E: A9 00         LDA   #$00                ; Reset set ...
8D80: 8D 1D 05      STA   $051D               ; ... counter
8D83: 60            RTS                       ; Done
```

# Copy to VRAM

```code
CopyToVRAM: 
;
; Block copy from (00:01) to VRAM (address MSB in A, latch LSB is 0).
; Length in (03:02)
;
8D84: 8D 06 20      STA   $2006               ; VRAM address MSB
8D87: A0 00         LDY   #$00                ; Straight offset from Y coming up
8D89: B1 00         LDA   ($00),Y             ; Byte from pointer ...
8D8B: 8D 07 20      STA   $2007               ; ... to next VRAM address
8D8E: A5 00         LDA   <$00                ; Increment ...
8D90: 18            CLC                       ; ... two ...
8D91: 69 01         ADC   #$01                ; ... byte ...
8D93: 85 00         STA   <$00                ; ... pointer ...
8D95: A5 01         LDA   <$01                ; ... at ...
8D97: 69 00         ADC   #$00                ; ... 00 and ...
8D99: 85 01         STA   <$01                ; ... 01
;
8D9B: A5 03         LDA   <$03                ; Decrement ...
8D9D: 38            SEC                       ; ... two ...
8D9E: E9 01         SBC   #$01                ; ... byte ...
8DA0: 85 03         STA   <$03                ; ... count ...
8DA2: A5 02         LDA   <$02                ; ... at ...
8DA4: E9 00         SBC   #$00                ; ... 02 and ...
8DA6: 85 02         STA   <$02                ; ... 03
;
8DA8: A5 02         LDA   <$02                ; More to do?
8DAA: D0 DD         BNE   $8D89               ; Yes ... go move all
8DAC: A5 03         LDA   <$03                ; More to do?
8DAE: D0 D9         BNE   $8D89               ; Yes ... go move all
8DB0: EE 1D 05      INC   $051D               ; Next set
8DB3: 60            RTS                       ; Done
```

```html
<canvas data-canvasFunction="TileEngine.handleTileCanvas" data-getTileDataFunction="Zelda.getMergedData" width="0" height="0" data-colorsName="GreenTanBrown" data-colors='["#606060","#80D010","#FC9838","#C84C0C"]'></canvas>
<canvas width="0" height="0" data-colorsName="RedOrangeWhite" data-colors='["#606060","#B53120","#F9BC22","#F0F0F0"]'></canvas>
<canvas width="0" height="0" data-colorsName="BlueBlueWhite" data-colors='["#606060","0000BC","#6B8EFF","#FFFFFF"]'></canvas>
```

# Tiles_S_Splash

```code
Tiles_S_Splash: 
;
; Copied to VRAM 0700

; 70-8D are kept in game play. These include the step ladder. The remainder are used for static pictures in the
; splash screen.
; 
; These images must have been developed "on top of" the memory for TileSetC (ROM bank 1) because
; some of the tiles "show through" into undefined slots here: 9C, 9D, 9E, 9F and D8, D9, DA, DB.
```

# Tiles_S_Splash70

```html
 <canvas width="900" height="150"
     data-labelColor="#00C0FF"
     data-pixWidth="8" 
     data-pixHeight="8"
     data-gap="0.25"
     data-colors='GreenTanBrown'
     data-gridPad="1"
     data-address="86b4"
     data-command=":2x2:70,H70,71,H71,+x,:2x2:72,H72,73,H73,+x,:2x2:74,H74,75,H75,+x,:2x2:76,H76,77,H77,+x,:2x2:78,H78,79,H79,+x,:2x2:7A,H7A,7B,H7B">
 </canvas>
<br>
 <canvas width="900" height="150"
     data-command=":1x2:7C,7D,+x,:1x2:7E,7F,+x,:1x2:80,81,+x,:1x2:82,83,+x,:1x2:84,85,+x,:1x2:86,87,+x,:1x2:88,89,+x,:1x2:8A,8B,+x,:1x2:8C,8D">
 </canvas>
```

```code
Tiles_S_Splash70: 
Common2: 
 ;   .....333    70
 ;   ....3333
 ;   ..333333
 ;   .3332333
 ;   .3323333
 ;   .3323333
 ;   33323333
 ;   33332333
8db4: 07 0F 3F 77 6F 6F EF F7 07 0F 3F 7F 7F 7F FF FF

 ;   33333333    71
 ;   33333333
 ;   .3333333
 ;   .3233233
 ;   ..233223
 ;   ..233322
 ;   ...23333
 ;   ....333.
8dc4: FF FF 7F 5B 19 1C 0F 0E FF FF 7F 7F 3F 3F 1F 0E

 ;   ......33    72
 ;   ....333.
 ;   ..3.3.23
 ;   ..3...33
 ;   ...3...3
 ;   ..33....
 ;   .333.33.
 ;   3..3.3..
8dd4: 03 0E 29 23 11 30 76 94 03 0E 2B 23 11 30 76 94

 ;   323.3...    73
 ;   .23.3.23
 ;   ..3...33
 ;   .33.3.33
 ;   ..33...3
 ;   ...33...
 ;   ...3.333
 ;   ....3.3.
8de4: A8 29 23 6B 31 18 17 0A E8 6B 23 6B 31 18 17 0A

 ;   ......3.    74
 ;   ........
 ;   ....3...
 ;   ..3.....
 ;   ......33
 ;   ...3....
 ;   ..3.....
 ;   ....3.3.
8df4: 02 00 08 20 03 10 20 0A 02 00 08 20 03 10 20 0A

 ;   3.......    75
 ;   ....3..3
 ;   ..3.....
 ;   .......3
 ;   ..3.....
 ;   .....3..
 ;   .......3
 ;   .....33.
8e04: 80 09 20 01 20 04 01 06 80 09 20 01 20 04 01 06

 ;   222.....    76
 ;   33322222
 ;   33333333
 ;   333.....
 ;   333.....
 ;   33322222
 ;   33333333
 ;   333.....
8e14: 00 E0 FF E0 E0 E0 FF E0 E0 FF FF E0 E0 FF FF E0

 ;   333.....    77
 ;   33322222
 ;   33333333
 ;   333.....
 ;   333.....
 ;   33322222
 ;   33333333
 ;   333.....
8e24: E0 E0 FF E0 E0 E0 FF E0 E0 FF FF E0 E0 FF FF E0

 ;   .22...11    78
 ;   .222.133
 ;   .33.1333
 ;   .3323212
 ;   .3322232
 ;   ..332222
 ;   ..333223
 ;   ..333123
8e34: 03 07 6F 6A 62 30 39 3D 60 73 67 7D 7F 3F 3F 3B

 ;   ...31111    79
 ;   ...31111
 ;   ...11133
 ;   ...33331
 ;   ...11133
 ;   ...11111
 ;   ....333.
 ;   ....333.
8e44: 1F 1F 1F 1F 1F 1F 0E 0E 10 10 03 1E 03 00 0E 0E

 ;   .....111    7A
 ;   ...11111
 ;   ..111111
 ;   .111....
 ;   .1......
 ;   1....222
 ;   ...22222
 ;   ..2222..
8e54: 07 1F 3F 70 40 80 00 00 00 00 00 00 00 07 1F 3C

 ;   .22.....    7B
 ;   .2....11
 ;   ....1111
 ;   ...11...
 ;   ..1....2
 ;   .....222
 ;   ....22..
 ;   ...2....
8e64: 00 03 0F 18 20 00 00 00 60 40 00 00 01 07 0C 10

 ;   ........    7C
 ;   ......22
 ;   ...1...2
 ;   2...1...
 ;   .2..11..
 ;   .22..1..
 ;   ..2..11.
 ;   ..22.11.
8e74: 00 00 10 08 0C 04 06 06 00 03 01 80 40 60 20 30

 ;   ..22.11.    7D
 ;   ..2..11.
 ;   .22..1..
 ;   .2..11..
 ;   2...1...
 ;   ...1...2
 ;   ......22
 ;   ........
8e84: 06 06 04 0C 08 10 00 00 30 20 60 40 80 01 03 00

 ;   ..1.....    7E
 ;   ...11...
 ;   2...11..
 ;   22..111.
 ;   22...11.
 ;   222..111
 ;   .22..111
 ;   .22..111
8e94: 20 18 0C 0E 06 07 07 07 00 00 80 C0 C0 E0 60 60

 ;   .22..111    7F
 ;   .22..111
 ;   222..111
 ;   22...11.
 ;   22..111.
 ;   2...11..
 ;   ...11...
 ;   ..1.....
8ea4: 07 07 07 06 0E 0C 18 20 60 60 E0 C0 C0 80 00 00

 ;   ........    80
 ;   1.......
 ;   3333....
 ;   33333...
 ;   3333.33.
 ;   2212.33.
 ;   2232232.
 ;   2222.32.
8eb4: 00 80 F0 F8 F6 26 24 04 00 00 F0 F8 F6 D6 FE F6

 ;   2222.32.    81
 ;   2233232.
 ;   2213232.
 ;   2113.32.
 ;   113..32.
 ;   3331.32.
 ;   1113333.
 ;   .333.33.
8ec4: 04 34 34 74 E4 F4 FE 76 F6 FE DE 96 26 E6 1E 76

 ;   ........    82
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ...11...
 ;   ....1...
 ;   12121333
8ed4: 00 00 00 00 00 18 08 AF 00 00 00 00 00 00 00 57

 ;   12121333    83
 ;   12121333
 ;   ....1...
 ;   ...11...
 ;   ........
 ;   ........
 ;   ........
 ;   ........
8ee4: AF AF 08 18 00 00 00 00 57 57 00 00 00 00 00 00

 ;   ........    84
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   3333333.
8ef4: 00 00 00 00 00 00 00 FE 00 00 00 00 00 00 00 FE

 ;   33333333    85
 ;   3333333.
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
8f04: FF FE 00 00 00 00 00 00 FF FE 00 00 00 00 00 00

 ;   ........    86
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   3.3.3...
 ;   .3.3.3..
 ;   11111111
8f14: 00 00 00 00 00 A8 54 FF 00 00 00 00 00 A8 54 00

 ;   .3.3.3..    87
 ;   3.3.3...
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
8f24: 54 A8 00 00 00 00 00 00 54 A8 00 00 00 00 00 00

 ;   ........    88
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ....22..
 ;   11111222
8f34: 00 00 00 00 00 00 00 F8 00 00 00 00 00 00 0C 07

 ;   ....22..    89
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
8f44: 00 00 00 00 00 00 00 00 0C 00 00 00 00 00 00 00

 ;   ........    8A
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   22222222
8f54: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 FF

 ;   22222222    8B
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
8f64: 00 00 00 00 00 00 00 00 FF 00 00 00 00 00 00 00

 ;   ........    8C
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ....311.
 ;   23231131
8f74: 00 00 00 00 00 00 0E 5F 00 00 00 00 00 00 08 F2

 ;   23231111    8D
 ;   ....311.
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
8f84: 5F 0E 00 00 00 00 00 00 F0 08 00 00 00 00 00 00
```

# Tiles_S_Splash8E

```html
<br>
 <canvas width="900" height="150"
     data-command=":6x2:8E,8F,90,91,92,93,94,95,96,97,98,99,+x,:1x2:9A,9B,+x,:2x2:9C,H9C,9D,H9D,+x,:1x2:9E,9F">
 </canvas>
```

```code
Tiles_S_Splash8E: 
Unused1: 
 ;   ........    8E
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
8f94: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   ........    8F
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
8fa4: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   ........    90
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
8fb4: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   ........    91
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
8fc4: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   ........    92
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
8fd4: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   ........    93
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
8fe4: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   ........    94
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
8ff4: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   ........    95
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
9004: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   ........    96
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
9014: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   ........    97
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
9024: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   ........    98
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
9034: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   ........    99
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
9044: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   22223...    9A
 ;   ..233...
 ;   .22233..
 ;   222233..
 ;   2222233.
 ;   2222223.
 ;   2222223.
 ;   .2222223
9054: 08 18 0C 0C 06 02 02 01 F8 38 7C FC FE FE FE 7F

 ;   ........    9B
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
9064: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

; Duplicates of TileSetC in bank 1: 9C, 9D, 9E, 9F

 ;   ....3333    9C
 ;   ...33333
 ;   ...332.2
 ;   ...232.2
 ;   ...23322
 ;   ..322322
 ;   ..313333
 ;   .3311333
9074: 0F 1F 18 08 0C 24 3F 7F 0F 1F 1D 1D 1F 3F 2F 67

 ;   .3331111    9D
 ;   .3221111
 ;   .3222113
 ;   .2223333
 ;   .2211113
 ;   ...33111
 ;   ...3333.
 ;   ....33..
9084: 7F 4F 47 0F 1F 1F 1E 0C 70 70 79 7F 61 18 1E 0C

 ;   ........    9E
 ;   ........
 ;   ..223...
 ;   .33223..
 ;   3232233.
 ;   3222333.
 ;   32322323
 ;   22232323
9094: 00 00 08 64 A6 8E A5 15 00 00 38 7C FE FE FF FF

 ;   22223333    9F
 ;   2322333.
 ;   .333333.
 ;   ...33...
 ;   ........
 ;   ........
 ;   ........
 ;   ........
90a4: 0F 4E 7E 18 00 00 00 00 FF FE 7E 18 00 00 00 00
```

# Sword Overlap

```html
<br>
 <canvas width="900" height="150"
     data-command=":1x2:A0,A1">
 </canvas>
```

```code
SwordOverlap: 
;
; Part of sword that overlaps ZELDA
 ;   ........    A0
 ;   ........
 ;   ........
 ;   11111111
 ;   22222222
 ;   11111111
 ;   11111111
 ;   ........
90b4: 00 00 00 FF 00 FF FF 00 00 00 00 00 FF 00 00 00

 ;   ........    A1
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
90c4: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```

# Water Above

```html
<br>
 <canvas width="900" height="150"
     data-command=":1x2:A2,A3,+x,:1x2:A4,A5,+x,:1x2:A6,A7,+x,:1x2:A8,A9,+x,:1x2:AA,AB,+x,:1x2:AC,AD,+x,:1x2:AE,AF,+x,:1x2:B0,B1">
 </canvas>
```

```code
WaterAbove: 
;
; Splashing water above the waterfall
 ;   ........    A2
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
90d4: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   ..1.....    A3
 ;   1.....1.
 ;   ........
 ;   .1..1...
 ;   ........
 ;   ....2222
 ;   ..222222
 ;   .2222222
90e4: 20 82 00 48 00 00 00 00 00 00 00 00 00 0F 3F 7F

 ;   ........    A4
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
90f4: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   .....1..    A5
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   22.....2
 ;   22222222
 ;   22222222
9104: 04 00 00 00 00 00 00 00 00 00 00 00 00 C1 FF FF

 ;   ........    A6
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
9114: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   ........    A7
 ;   .1......
 ;   ........
 ;   ........
 ;   .2222...
 ;   22222222
 ;   22222222
 ;   22222222
9124: 00 40 00 00 00 00 00 00 00 00 00 00 78 FF FF FF

 ;   ........    A8
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
9134: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   .1....1.    A9
 ;   ........
 ;   ..1..1..
 ;   ........
 ;   ..222..1
 ;   2222222.
 ;   22222222
 ;   22222222
9144: 42 00 24 00 01 00 00 00 00 00 00 00 38 FE FF FF

 ;   ........    AA
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
9154: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   ....1...    AB
 ;   ........
 ;   ..1...1.
 ;   ........
 ;   1..22222
 ;   .2222222
 ;   22222222
 ;   22222222
9164: 08 00 22 00 80 00 00 00 00 00 00 00 1F 7F FF FF

 ;   ........    AC
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
9174: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   .1......    AD
 ;   ........
 ;   ....1...
 ;   ........
 ;   2222....
 ;   22222222
 ;   22222222
 ;   22222222
9184: 40 00 08 00 00 00 00 00 00 00 00 00 F0 FF FF FF

 ;   ........    AE
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
9194: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   ..1.....    AF
 ;   ........
 ;   ........
 ;   .1......
 ;   ........
 ;   22222...
 ;   22222222
 ;   22222222
91a4: 20 00 00 40 00 00 00 00 00 00 00 00 00 F8 FF FF

 ;   ........    B0
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
91b4: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   .....1..    B1
 ;   ...1....
 ;   .......1
 ;   1.......
 ;   ........
 ;   ..2222..
 ;   2222222.
 ;   22222222
91c4: 04 10 01 80 00 00 00 00 00 00 00 00 00 3C FE FF
```

# Water Falling

```html
<br>
 <canvas width="900" height="150"
     data-command=":1x2:B2,B3,+x,:1x2:B4,B5,+x,:1x2:B6,B7,+x,:1x2:B8,B9,+x,:1x2:BA,BB,+x,:1x2:BC,BD,+x,:1x2:BE,BF,+x,:1x2:C2,C3,+x,:1x2:C4,C5,+x,:1x2:C6,C7,+x,:1x2:C8,C9">
 </canvas>
```

```code
WaterFalling: 
;
; Water falling down the waterfall
 ;   ...11111    B2
 ;   .1111111
 ;   11111111
 ;   11111111
 ;   .1111111
 ;   ...11111
 ;   .....111
 ;   .......1
91d4: 1F 7F FF FF 7F 1F 07 01 00 00 00 00 00 00 00 00

 ;   ........    B3
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
91e4: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   1111....    B4
 ;   11111111
 ;   11111111
 ;   11111111
 ;   11111111
 ;   11111111
 ;   111...11
 ;   1.......
91f4: F0 FF FF FF FF FF E3 80 00 00 00 00 00 00 00 00

 ;   ........    B5
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
9204: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   ........    B6
 ;   11111...
 ;   11111111
 ;   11111111
 ;   11111111
 ;   11111111
 ;   11111111
 ;   11111...
9214: 00 F8 FF FF FF FF FF F8 00 00 00 00 00 00 00 00

 ;   ........    B7
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
9224: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   ........    B8
 ;   ..1111..
 ;   1111111.
 ;   11111111
 ;   11111111
 ;   111111..
 ;   11......
 ;   ........
9234: 00 3C FE FF FF FC C0 00 00 00 00 00 00 00 00 00

 ;   ........    B9
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
9244: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   1.......    BA
 ;   1111....
 ;   11111111
 ;   11111111
 ;   .1111111
 ;   ...11111
 ;   ....1111
 ;   .....111
9254: 80 F0 FF FF 7F 1F 0F 07 00 00 00 00 00 00 00 00

 ;   .....111    BB
 ;   ......11
 ;   .......1
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
9264: 07 03 01 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   ........    BC
 ;   .11111..
 ;   11111111
 ;   11111111
 ;   11111111
 ;   11111111
 ;   11111111
 ;   11111111
9274: 00 7C FF FF FF FF FF FF 00 00 00 00 00 00 00 00

 ;   11111111    BD
 ;   1111111.
 ;   1111....
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
9284: FF FE F0 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   ........    BE
 ;   ........
 ;   ......11
 ;   11111111
 ;   11111111
 ;   111.1111
 ;   111..111
 ;   11...111
9294: 00 00 03 FF FF EF E7 C7 00 00 00 00 00 00 00 00

 ;   1.....11    BF
 ;   ......11
 ;   .......1
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
92a4: 83 03 01 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   .....111    C0
 ;   .111111.
 ;   1111111.
 ;   111111..
 ;   111111..
 ;   111111..
 ;   11111...
 ;   11111...
92b4: 07 7E FE FC FC FC F8 F8 00 00 00 00 00 00 00 00

 ;   11111...    C1
 ;   1111....
 ;   1111....
 ;   111.....
 ;   ........
 ;   ........
 ;   ........
 ;   ........
92c4: F8 F0 F0 E0 00 00 00 00 00 00 00 00 00 00 00 00

 ;   11......    C2
 ;   .111....
 ;   .1111...
 ;   ..111...
 ;   ..1111..
 ;   ...111..
 ;   ...1111.
 ;   ....1111
92d4: C0 70 78 38 3C 1C 1E 0F 00 00 00 00 00 00 00 00

 ;   ....1111    C3
 ;   ....1111
 ;   .....111
 ;   .....111
 ;   .....111
 ;   ......11
 ;   .......1
 ;   ........
92e4: 0F 0F 07 07 07 03 01 00 00 00 00 00 00 00 00 00

 ;   ........    C4
 ;   ........
 ;   ........
 ;   ......11
 ;   ....1111
 ;   ...11111
 ;   ..111111
 ;   11111111
92f4: 00 00 00 03 0F 1F 3F FF 00 00 00 00 00 00 00 00

 ;   11111111    C5
 ;   111111..
 ;   11111...
 ;   11111...
 ;   11111...
 ;   1111....
 ;   111.....
 ;   ........
9304: FF FC F8 F8 F8 F0 E0 00 00 00 00 00 00 00 00 00

 ;   ........    C6
 ;   ........
 ;   ........
 ;   1111....
 ;   1111111.
 ;   11111111
 ;   11111111
 ;   1.111111
9314: 00 00 00 F0 FE FF FF BF 00 00 00 00 00 00 00 00

 ;   ...11111    C7
 ;   ...11111
 ;   ....1111
 ;   ....1111
 ;   ....1111
 ;   .....111
 ;   .....111
 ;   ......11
9324: 1F 1F 0F 0F 0F 07 07 03 00 00 00 00 00 00 00 00

 ;   .......1    C8
 ;   ......11
 ;   .....111
 ;   ....111.
 ;   ..11111.
 ;   1111111.
 ;   111111..
 ;   111111..
9334: 01 03 07 0E 3E FE FC FC 00 00 00 00 00 00 00 00

 ;   111111..    C9
 ;   111111..
 ;   11111...
 ;   11111...
 ;   11111...
 ;   1111....
 ;   111.....
 ;   1.......
9344: FC FC F8 F8 F8 F0 E0 80 00 00 00 00 00 00 00 00
```

# Vines

```html
<br>
 <canvas width="900" height="150"
     data-command=":1x2:CA,CB,+x,:1x2:CC,CD,+x,:1x2:CE,CF,+x,:1x2:D2,D3,+x,:1x2:D4,D5,+x,:1x2:D6,D7">
 </canvas>
```

```code
Vines: 
;
; These are pieces of vine hanging around the inner boarder on the splash screen
 ;   ........    CA
 ;   ..3.....
 ;   ..3....1
 ;   .3.....1
 ;   .3.333.1
 ;   ..32222.
 ;   ..111222
 ;   ..111122
9354: 00 20 21 41 5D 20 38 3C 00 20 20 40 5C 3E 07 03

 ;   ...11112    CB
 ;   ....3.12
 ;   .....3.2
 ;   ...1.3.3
 ;   ..1123.3
 ;   .112233.
 ;   222223..
 ;   ....33..
9364: 1E 0A 04 15 35 66 04 0C 01 09 05 05 0D 1E FC 0C

 ;   ........    CC
 ;   12..33..
 ;   2223..3.
 ;   2...112.
 ;   ...11222
 ;   .3111222
 ;   3.33222.
 ;   23...2..
9374: 00 8C 12 0C 18 78 B0 40 00 4C F2 82 07 47 BE C4

 ;   23......    CD
 ;   3.3322..
 ;   3..211..
 ;   ...2111.
 ;   .....11.
 ;   ........
 ;   ........
 ;   ........
9384: 40 B0 8C 0E 06 00 00 00 C0 BC 90 10 00 00 00 00

 ;   ........    CE
 ;   .....11.
 ;   ..121122
 ;   .1222222
 ;   .1211222
 ;   .1.1222.
 ;   ...1223.
 ;   ....2.33
9394: 00 06 2C 40 58 50 12 03 00 00 13 3F 27 0E 0E 0B

 ;   ..11...3    CF
 ;   .11223.3
 ;   .1122233
 ;   .1122231
 ;   .1222.31
 ;   ..22...1
 ;   ..2.....
 ;   ........
93a4: 31 65 63 63 43 01 00 00 01 1D 1F 1E 3A 30 20 00

 ;   .2......    D0
 ;   .12.11..
 ;   .32.122.
 ;   23..3122
 ;   2122....
 ;   11122...
 ;   11122.1.
 ;   11222.11
93b4: 00 4C 48 4C 40 E0 E2 C3 40 20 66 CB B0 18 18 38

 ;   .1222321    D1
 ;   .3223..2
 ;   12.2....
 ;   122.....
 ;   112.....
 ;   112.....
 ;   112.....
 ;   .1......
93c4: 45 48 80 80 C0 C0 C0 40 3E 79 50 60 20 20 20 00

 ;   ..112...    D2
 ;   .11222..
 ;   1112223.
 ;   11222.33
 ;   11223123
 ;   .1223112
 ;   .12..312
 ;   ..2...32
93d4: 30 60 E2 C3 CD 4E 46 02 08 1C 1E 3B 3B 39 25 23

 ;   ........    D3
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
93e4: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   .112....    D4
 ;   11222...
 ;   11222...
 ;   .122....
 ;   3222.11.
 ;   3.23.321
 ;   ...33..2
 ;   ........
93f4: 60 C0 C0 40 86 95 18 00 10 38 38 30 F0 B6 19 00

 ;   ........    D5
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
9404: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 ;   .2.11...    D6
 ;   2211..2.
 ;   .1331222
 ;   11131122
 ;   1.112122
 ;   .221.22.
 ;   22222...
 ;   .222....
9414: 18 30 78 FC B4 10 00 00 40 C2 37 13 0B 66 F8 70

 ;   ........    D7
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
 ;   ........
9424: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```

```html
<br>
 <canvas width="900" height="150"
     data-command=":1x2:D8,D9,+x,:1x2:DA,DB">
 </canvas>
```

```code
Unused2: 
;
; Duplicates of TileSetC in bank 1: D8, D9, DA, DB.
 ;   11.2....    D8
 ;   1112....
 ;   3112....
 ;   321.....
 ;   22122...
 ;   121222..
 ;   212222..
 ;   1221111.
9434: C0 E0 E0 A0 20 A0 40 9E 10 10 90 C0 D8 5C BC 60

 ;   2221331.    D9
 ;   112133..
 ;   111133..
 ;   111133..
 ;   111133..
 ;   111113..
 ;   .1111...
 ;   .111....
9444: 1E DC FC FC FC FC 78 70 EC 2C 0C 0C 0C 04 00 00

 ;   ...2.111    DA
 ;   ...21111
 ;   ...21111
 ;   ....1111
 ;   ....1111
 ;   .2222122
 ;   22222222
 ;   22221221
9454: 07 0F 0F 0F 0F 04 00 09 10 10 10 00 00 7B FF F6

 ;   22221211    DB
 ;   .2212211
 ;   ..111121
 ;   ..111111
 ;   ..111111
 ;   ..111111
 ;   ...111..
 ;   ........
9464: 0B 13 3D 3F 3F 3F 1C 00 F4 6C 02 00 00 00 00 00
```

# Sign

```html
<br>
 <canvas width="500" height="400"
     data-command=":6x6:E4,E2,EC,EE,F8,FA,E4,E3,ED,EF,F9,FB,E4,E6,F0,F2,FC,FE,E5,E7,F1,F3,FD,FF,E8,EA,F4,F6,DC,DE,E9,EB,F5,F7,DD,DF">
 </canvas>
```

```code
Sign: 
;
; The sign at the end of the treasure info that says:
; PLEASE LOOK UP THE MANUAL FOR DETAILS.
 ;   .2...2.2    DC
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22.22.22
 ;   22.22.22
 ;   22.22.22
9474: 00 00 00 00 00 00 00 00 45 FF FF FF FF DB DB DB

 ;   22.22.22    DD
 ;   22.22.22
 ;   22.22.22
 ;   22.22...
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
9484: 00 00 00 00 00 00 00 00 DB DB DB D8 FF FF FF FF

 ;   .2...222    DE
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
 ;   2...2222
 ;   2.222222
 ;   2..22222
9494: 00 00 00 00 00 00 00 00 47 FF FF FF FF 8F BF 9F

 ;   22..2222    DF
 ;   222.2222
 ;   222.2222
 ;   2...2.22
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
94a4: 00 00 00 00 00 00 00 00 CF EF EF 8B FF FF FF FF

 ;   22222222    E0
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
94b4: 00 00 00 00 00 00 00 00 FF FF FF FF FF FF FF FF

 ;   22222222    E1
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
94c4: 00 00 00 00 00 00 00 00 FF FF FF FF FF FF FF FF

 ;   22222222    E2
 ;   22222222
 ;   22222222
 ;   22222222
 ;   2222...2
 ;   2222.2.2
 ;   2222.2.2
 ;   2222...2
94d4: 00 00 00 00 00 00 00 00 FF FF FF FF F1 F5 F5 F1

 ;   2222.222    E3
 ;   2222.222
 ;   2222.222
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22.222..
94e4: 00 00 00 00 00 00 00 00 F7 F7 F7 FF FF FF FF DC

 ;   22222222    E4
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
94f4: 00 00 00 00 00 00 00 00 FF FF FF FF FF FF FF FF

 ;   22222222    E5
 ;   22222222
 ;   2222...2
 ;   22222.22
 ;   22222.22
 ;   22222.22
 ;   22222.22
 ;   22222.22
9504: 00 00 00 00 00 00 00 00 FF FF F1 FB FB FB FB FB

 ;   22.222.2    E6
 ;   22.222.2
 ;   22.222.2
 ;   22.222.2
 ;   22.222.2
 ;   22...2..
 ;   22222222
 ;   22222222
9514: 00 00 00 00 00 00 00 00 DD DD DD DD DD C4 FF FF

 ;   22222222    E7
 ;   22222222
 ;   .2.2...2
 ;   .2.2.222
 ;   .2.2.222
 ;   ...2...2
 ;   .2.2.222
 ;   .2.2.222
9524: 00 00 00 00 00 00 00 00 FF FF 51 57 57 11 57 57

 ;   22222.22    E8
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22...2..
 ;   22.222.2
 ;   22.222.2
9534: 00 00 00 00 00 00 00 00 FB FF FF FF FF C4 DD DD

 ;   22...2.2    E9
 ;   22.222.2
 ;   22.222.2
 ;   22.222..
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
9544: 00 00 00 00 00 00 00 00 C5 DD DD DC FF FF FF FF

 ;   .2.2...2    EA
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
 ;   .2...222
 ;   .2.2.222
 ;   .2.2.222
9554: 00 00 00 00 00 00 00 00 51 FF FF FF FF 47 57 57

 ;   .2.2.222    EB
 ;   .2..2222
 ;   .2.2.222
 ;   .2.2.222
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
9564: 00 00 00 00 00 00 00 00 57 4F 57 57 FF FF FF FF

 ;   22222222    EC
 ;   22222222
 ;   22222222
 ;   22222222
 ;   .222...2
 ;   .222.222
 ;   .222.222
 ;   .222...2
9574: 00 00 00 00 00 00 00 00 FF FF FF FF 71 77 77 71

 ;   .222.222    ED
 ;   .222.222
 ;   ...2...2
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
 ;   .2...2.2
9584: 00 00 00 00 00 00 00 00 77 77 11 FF FF FF FF 45

 ;   22222222    EE
 ;   22222222
 ;   22222222
 ;   22222222
 ;   2.22...2
 ;   ...2.222
 ;   .2.2..22
 ;   .2.22..2
9594: 00 00 00 00 00 00 00 00 FF FF FF FF B1 17 53 59

 ;   ...222.2    EF
 ;   .2.222.2
 ;   .2.2...2
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
 ;   2.22222.
95a4: 00 00 00 00 00 00 00 00 1D 5D 51 FF FF FF FF BE

 ;   .2.2.2.2    F0
 ;   .2.2.2..
 ;   .2.2.2.2
 ;   .2.2.2.2
 ;   .2.2.2.2
 ;   .2...2.2
 ;   22222222
 ;   22222222
95b4: 00 00 00 00 00 00 00 00 55 54 55 55 55 45 FF FF

 ;   22222222    F1
 ;   22222222
 ;   2222..2.
 ;   2222.2.2
 ;   2222.2.2
 ;   2222.2.2
 ;   2222.2.2
 ;   2222.2.2
95c4: 00 00 00 00 00 00 00 00 FF FF F2 F5 F5 F5 F5 F5

 ;   .222222.    F2
 ;   2222222.
 ;   .222222.
 ;   .222222.
 ;   2.22222.
 ;   2.22222.
 ;   22222222
 ;   22222222
95d4: 00 00 00 00 00 00 00 00 7E FE 7E 7E BE BE FF FF

 ;   22222222    F3
 ;   22222222
 ;   222.22..
 ;   .2...2.2
 ;   .2.2.2.2
 ;   .2.2.2.2
 ;   .2...2.2
 ;   .2.2.2.2
95e4: 00 00 00 00 00 00 00 00 FF FF EC 45 55 55 45 55

 ;   2222.2.2    F4
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
 ;   2..22...
 ;   2.2.2.22
 ;   2.2.2.22
95f4: 00 00 00 00 00 00 00 00 F5 FF FF FF FF 98 AB AB

 ;   2.2.2...    F5
 ;   2.2.2.22
 ;   2.2.2.22
 ;   2..22...
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
9604: 00 00 00 00 00 00 00 00 A8 AB AB 98 FF FF FF FF

 ;   .2.2.2.2    F6
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
 ;   2...22.2
 ;   22.22...
 ;   22.22.2.
9614: 00 00 00 00 00 00 00 00 55 FF FF FF FF 8D D8 DA

 ;   22.22.2.    F7
 ;   22.22...
 ;   22.22.2.
 ;   22.22.2.
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
9624: 00 00 00 00 00 00 00 00 DA D8 DA DA FF FF FF FF

 ;   2222223.    F8
 ;   22222223
 ;   22222222
 ;   22222222
 ;   ...22222
 ;   .2222222
 ;   .2222222
 ;   ...22222
9634: 02 01 00 00 00 00 00 00 FE FF FF FF 1F 7F 7F 1F

 ;   .2222222    F9
 ;   .2222222
 ;   ...22222
 ;   22222222
 ;   22222222
 ;   22222222
 ;   22222222
 ;   2.2...22
9644: 00 00 00 00 00 00 00 00 7F 7F 1F FF FF FF FF A3

 ;   3.......    FA
 ;   333.....
 ;   2333..3.
 ;   2223.32.
 ;   2223.322
 ;   22223222
 ;   22222222
 ;   22222223
9654: 80 E0 72 14 14 08 00 01 80 E0 F2 F6 F7 FF FF FF

 ;   22222223    FB
 ;   2222223.
 ;   222323..
 ;   223.2333
 ;   23..3222
 ;   23.32233
 ;   233223..
 ;   2222223.
9664: 01 02 14 27 48 53 64 02 FF FE FC EF CF DF FC FE

 ;   2.2.2.22    FC
 ;   2.2.2.22
 ;   2.2...22
 ;   2.2.2222
 ;   2.2.2222
 ;   ..2.2222
 ;   22222222
 ;   22222222
9674: 00 00 00 00 00 00 00 00 AB AB A3 AF AF 2F FF FF

 ;   22222222    FD
 ;   22222222
 ;   22.2.22.
 ;   .2.2.2..
 ;   .2.2.2.2
 ;   .2.2.2.2
 ;   .2.2.2..
 ;   .2.2.2.2
9684: 00 00 00 00 00 00 00 00 FF FF D6 54 55 55 54 55

 ;   22222222    FE
 ;   22222223
 ;   22222233
 ;   2222233.
 ;   2222333.
 ;   222233..
 ;   222233..
 ;   222223..
9694: 00 01 03 06 0E 0C 0C 04 FF FF FF FE FE FC FC FC

 ;   2222223.    FF
 ;   22222223
 ;   22.22223
 ;   .2.22222
 ;   .2.22222
 ;   .2.22222
 ;   .2.22222
 ;   .2.22222
96a4: 02 01 01 00 00 00 00 00 FE FF DF 5F 5F 5F 5F 5F
```

# Tiles_B_Splash

```code
; ........  ........  ........  ........  .....222  22222222  22222222  22222222  22222222  22222222  22222222  22......  ........  ...11111  11111111  11111111  
; ........  ........  ........  ........  ....2222  22222222  22222222  22222222  22222222  22222222  22222222  222.....  ........  ..111111  11111111  11111113  
; ........  ...333.3  ..3.3333  ....3...  .3333223  33233332  33322333  22222233  22333322  22222222  22222222  223.....  ........  .1111111  11111111  11111133  
; ........  ....3..3  ..3.3...  ....3...  .3..2232  22232222  32232322  32222322  32322222  22222222  22222222  233.....  ........  11111111  11111111  11111333  
; ........  ....3..3  333.333.  ....3...  .3332232  33233322  32232322  32222322  32333223  33333333  33333222  23......  .......1  11111111  11111111  11113333  
; ........  ....3..3  ..3.3...  ....3...  .3...232  23232222  32232322  32222322  32322222  22222222  22232222  33......  ......11  11111111  11111111  11133333  
; ........  ....3..3  ..3.3333  ....3333  .3333.33  33233332  32232333  22222233  22322222  22222222  22232222  3.......  .....111  11111111  11111111  11333333  
; ........  ........  ........  ........  .......2  22222222  22222222  22222222  22222222  22222222  22322222  3.......  ....1111  33333333  11111111  13333333  
;
Tiles_B_Splash: 
; Copied to VRAM 1700
96B4: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
96C4: 00 00 1D 09 09 09 09 00 00 00 1D 09 09 09 09 00 
96D4: 00 00 2F 28 EE 28 2F 00 00 00 2F 28 EE 28 2F 00 
96E4: 00 00 08 08 08 08 0F 00 00 00 08 08 08 08 0F 00 
96F4: 00 00 79 42 72 42 7B 00 07 0F 7F 4F 7F 47 7B 01 
9704: 00 00 DE 10 DC 50 DE 00 FF FF FF FF FF FF FF FF 
9714: 00 00 E7 94 94 94 97 00 FF FF FF FF FF FF FF FF 
9724: 00 00 03 84 84 84 03 00 FF FF FF FF FF FF FF FF 
9734: 00 00 3C A0 B9 A0 20 00 FF FF FF FF FF FF FF FF 
9744: 00 00 00 00 FF 00 00 00 FF FF FF FF FF FF FF FF 
9754: 00 00 00 00 F8 10 10 20 FF FF FF FF FF FF FF FF 
9764: 00 00 20 60 40 C0 80 80 C0 E0 E0 E0 C0 C0 80 80 
9774: 00 00 00 00 01 03 07 0F 00 00 00 00 00 00 00 00 
9784: 1F 3F 7F FF FF FF FF FF 00 00 00 00 00 00 00 FF 
9794: FF FF FF FF FF FF FF FF 00 00 00 00 00 00 00 00 
97A4: FF FF FF FF FF FF FF FF 00 01 03 07 0F 1F 3F 7F 


; .1111111  11111111  11111111  11222111  11111122  22221111  11111111  11111111  11112223  ....3111  1111....  ........  ...11333  33333331  11111111  33333333  
; 3.111111  11111111  11111111  11322111  11111332  22223311  11111111  11111111  11111123  ..333111  11111...  ........  ....3333  33333311  11111113  3333333.  
; 33111111  11111111  11111111  11332111  11113333  22233333  11111111  11111111  11111111  .3333111  111111..  ........  .....333  33333111  11111133  333333..  
; 33111111  11111111  11111111  13333111  11113333  32333333  31111111  11111111  11111111  13333111  1111111.  ........  ......33  33331111  11111333  33333...  
; 33311111  11111111  11111111  13331111  11133333  32223333  31111111  11111111  11111111  13333111  11111111  ........  .......3  3..11111  11113333  3333....  
; 33311111  11111111  11111111  13331111  11133333  22222333  33111111  11111111  11111111  11333311  11111111  1.......  ........  ..111111  11133333  333.....  
; 33111111  11111111  11111111  33331111  11133332  22222333  33111111  11111111  11111111  11133311  11111111  11......  ........  .1111111  11333333  33......  
; 3.111111  11333333  33333311  33331111  11133332  22222233  33111111  11333333  31111111  11133311  11111111  111.....  ........  11111111  13333333  3.......  
;
97B4: 7F BF FF FF FF FF FF BF 00 80 C0 C0 E0 E0 C0 80 
97C4: FF FF FF FF FF FF FF FF 00 00 00 00 00 00 00 3F 
97D4: FF FF FF FF FF FF FF FF 00 00 00 00 00 00 00 FC 
97E4: C7 E7 F7 FF FF FF FF FF 38 38 38 78 70 70 F0 F0 
97F4: FC FE FF FF FF FF FE FE 03 07 0F 0F 1F 1F 1F 1F 
9804: 0F 0F 1F BF 8F 07 07 03 F0 FC FF FF FF FF FF FF 
9814: FF FF FF FF FF FF FF FF 00 00 00 80 80 C0 C0 C0 
9824: FF FF FF FF FF FF FF FF 00 00 00 00 00 00 00 3F 
9834: F1 FD FF FF FF FF FF FF 0F 03 00 00 00 00 00 80 
9844: 0F 3F 7F FF FF FF FF FF 08 38 78 78 78 3C 1C 1C 
9854: F0 F8 FC FE FF FF FF FF 00 00 00 00 00 00 00 00 
9864: 00 00 00 00 00 80 C0 E0 00 00 00 00 00 00 00 00 
9874: 1F 0F 07 03 01 00 00 00 07 0F 07 03 01 00 00 00 
9884: FF FF FF FF 9F 3F 7F FF FE FC F8 F0 80 00 00 00 
9894: FF FF FF FF FF FF FF FF 00 01 03 07 0F 1F 3F 7F 
98A4: FF FE FC F8 F0 E0 C0 80 FF FE FC F8 F0 E0 C0 80 


; ..111111  11333333  33333331  33311111  11333322  22222233  33111111  11333333  33311111  11113311  11111111  1111....  ........  .......1  11111111  33333333  
; ..111111  13333333  33333333  33311111  11333322  22222223  33311111  11133333  33331111  11113311  11111111  11111...  ........  ......11  11111113  3333333.  
; .1111111  11111111  11333333  33311111  11333322  22222223  33311111  11133333  33333111  11111331  11111111  111111..  ........  .....111  11111133  333333..  
; .1111111  11111111  11322222  22311111  11333322  22222223  33311111  11123233  33333111  11111331  11111111  1111111.  ........  ....1111  11111333  33333...  
; .1111111  11111111  11332222  22111111  13333222  22222223  33311111  11123222  33333311  11111331  11111111  11111111  ........  ...11111  11111111  11111111  
; 11111111  11111111  13333222  22111111  13333222  22222222  33331111  11112222  23333311  11111331  11111131  11111111  1.......  ..111111  11111111  11111111  
; 11111111  11111111  13333322  22111111  13333222  22222222  33331111  11112222  23333311  11111131  11111133  11111111  11......  .1111111  11111111  11111111  
; 11111111  11111111  13333322  22111111  13333222  22222222  33331111  11112222  33333311  11111131  11111133  31111111  111.....  11111111  11111111  11111111  
;
98B4: 3F 3F 7F 7F 7F FF FF FF 00 00 00 00 00 00 00 00 
98C4: FF FF FF FF FF FF FF FF 3F 7F 00 00 00 00 00 00 
98D4: FF FF FF E0 F0 F8 FC FC FE FF 3F 3F 3F 7F 7F 7F 
98E4: FF FF FF 3F 3F 3F 3F 3F E0 E0 E0 E0 C0 C0 C0 C0 
98F4: FC FC FC FC F8 F8 F8 F8 3F 3F 3F 3F 7F 7F 7F 7F 
9904: 03 01 01 01 01 00 00 00 FF FF FF FF FF FF FF FF 
9914: FF FF FF FF FF FF FF FF C0 E0 E0 E0 E0 F0 F0 F0 
9924: FF FF FF EB E8 F0 F0 F0 3F 1F 1F 1F 1F 0F 0F 0F 
9934: FF FF FF FF FF 7F 7F FF E0 F0 F8 F8 FC FC FC FC 
9944: FF FF FF FF FF FF FF FF 0C 0C 06 06 06 06 02 02 
9954: FF FF FF FF FF FF FF FF 00 00 00 00 00 02 03 03 
9964: F0 F8 FC FE FF FF FF FF 00 00 00 00 00 00 00 80 
9974: 00 00 00 00 00 80 C0 E0 00 00 00 00 00 00 00 00 
9984: 01 03 07 0F 1F 3F 7F FF 00 00 00 00 00 00 00 00 
9994: FF FF FF FF FF FF FF FF 00 01 03 07 00 00 00 00 
99A4: FF FE FC F8 FF FF FF FF FF FE FC F8 00 00 00 00 


; ........  11111113  33333333  33333322  21111111  33332222  22222222  33331111  11112222  3.333311  11111133  11111113  33111111  1111....  ........  11111111  
; .......1  11111113  33333333  33333222  21111111  33332222  22222222  23333111  11112223  3..33311  11111133  11111113  33311111  11111...  ........  11111111  
; .....1.1  11111133  33333333  33333212  21111111  33332222  22222221  23333111  11111223  ...33111  11111133  1111111.  33331111  111111..  ........  11111111  
; ...11131  11111133  33333333  33333113  21111111  33332222  22222211  23333111  11111233  ...31111  11111133  11111111  11111111  1111111.  ........  11111111  
; 11111331  11111111  11111111  11111113  11111111  11111111  11111111  13333111  11111111  11111111  11111133  11111111  11111111  11111111  ........  33333333  
; 11111311  11111111  11111111  11111113  11111111  11111111  11111111  12333311  11111111  11111111  11111133  31111111  11111111  11111111  1.......  33333333  
; 11113311  11111111  11111111  11111133  11111111  11111111  11111111  12333311  11111111  11111111  11111333  31111111  11111111  11111111  11......  .3333333  
; 11113311  11111111  11111111  11111133  11111111  11111111  11111111  12333311  11111111  11111111  11111333  31111111  11111111  11111111  111.....  ...33333  
;
99B4: 00 01 05 1F FF FF FF FF 00 00 00 02 06 04 0C 0C 
99C4: FF FF FF FF FF FF FF FF 01 01 03 03 00 00 00 00 
99D4: FF FF FF FF FF FF FF FF FF FF FF FF 00 00 00 00 
99E4: FC F8 FA FF FF FF FF FF FF FF FD F9 01 01 03 03 
99F4: 7F 7F 7F 7F FF FF FF FF 80 80 80 80 00 00 00 00 
9A04: F0 F0 F0 F0 FF FF FF FF FF FF FF FF 00 00 00 00 
9A14: 00 00 01 03 FF FF FF FF FF FF FE FC 00 00 00 00 
9A24: FF 7F 7F 7F FF BF BF BF F0 F8 F8 F8 78 7C 7C 7C 
9A34: F0 F1 F9 FB FF FF FF FF 0F 0F 07 07 00 00 00 00 
9A44: BF 9F 1F 1F FF FF FF FF BC 9C 18 10 00 00 00 00 
9A54: FF FF FF FF FF FF FF FF 03 03 03 03 03 03 07 07 
9A64: FF FF FE FF FF FF FF FF 01 01 00 00 00 80 80 80 
9A74: FF FF FF FF FF FF FF FF C0 E0 F0 00 00 00 00 00 
9A84: F0 F8 FC FE FF FF FF FF 00 00 00 00 00 00 00 00 
9A94: 00 00 00 00 00 80 C0 E0 00 00 00 00 00 00 00 00 
9AA4: FF FF FF FF FF FF 7F 1F 00 00 00 00 FF FF 7F 1F 


; 11111111  11111111  11133111  11111111  11111111  11111131  11111111  11111111  11111111  12333311  11111111  11111111  11113333  31111111  11111111  11111111  
; 11111111  11111111  11133111  11111111  11111111  11111331  11111111  11111111  11111111  11233111  11111111  11111111  11133333  31111111  11111111  11111111  
; 11111111  11111111  11331111  11111111  11111111  11111331  11111111  11111111  11111111  11233111  11111111  11111111  11.33333  11111111  13333333  33331111  
; 11111111  11111111  11311111  11111111  11111111  11111331  11111111  11111111  11111111  11131111  11111111  11111113  3..33331  11111111  13333333  33333111  
; 33333333  33333333  33333333  33333333  33333333  33333333  33333333  33333333  33333333  33333333  33333333  33333333  ...33333  33333333  33333333  33333333  
; 33333333  33333333  33333333  33333333  33333333  33333333  33333333  33333333  33333333  33333333  33333333  3333333.  ...33333  33333333  33333333  33333333  
; 33333333  33333333  33333333  33333333  33333333  33333333  33333333  33333333  33333333  33333333  33333333  333333..  ..333333  333.....  ......33  33333333  
; 33333333  33333333  333333.3  33333333  33333333  33333333  23333333  33333333  33333333  32333333  33333333  3333....  .3333333  333.....  .......3  33333333  
;
9AB4: FF FF FF FF FF FF FF FF 00 00 00 00 FF FF FF FF 
9AC4: FF FF FF FF FF FF FF FF 00 00 00 00 FF FF FF FF 
9AD4: FF FF FF FF FF FF FF FD 18 18 30 20 FF FF FF FD 
9AE4: FF FF FF FF FF FF FF FF 00 00 00 00 FF FF FF FF 
9AF4: FF FF FF FF FF FF FF FF 00 00 00 00 FF FF FF FF 
9B04: FF FF FF FF FF FF FF FF 02 06 06 06 FF FF FF FF 
9B14: FF FF FF FF FF FF FF 7F 00 00 00 00 FF FF FF FF 
9B24: FF FF FF FF FF FF FF FF 00 00 00 00 FF FF FF FF 
9B34: FF FF FF FF FF FF FF FF 00 00 00 00 FF FF FF FF 
9B44: BF DF DF FF FF FF FF BF 7C 38 38 10 FF FF FF FF 
9B54: FF FF FF FF FF FF FF FF 00 00 00 00 FF FF FF FF 
9B64: FF FF FF FF FF FE FC F0 00 00 00 01 FF FE FC F0 
9B74: FF FF DF 9F 1F 1F 3F 7F 0F 1F 1F 9E 1F 1F 3F 7F 
9B84: FF FF FF FF FF FF E0 E0 80 80 00 00 FF FF E0 E0 
9B94: FF FF FF FF FF FF 03 01 00 00 7F 7F FF FF 03 01 
9BA4: FF FF FF FF FF FF FF FF 00 00 F0 F8 FF FF FF FF 


; 1111....  .......2  22233222  22222222  22222222  22322223  ........  ........  ........  ........  ...22223  32222222  22222232  2223....  22233222  22322223  
; 11111...  ........  22223222  22222222  22222222  23222233  ........  ........  ........  ........  ....2222  32222222  22222322  2233....  22223222  23222233  
; 111111..  ........  22223322  22222222  22222222  2322223.  ........  ........  ........  ........  ....2222  33222222  22222322  223.....  22223322  2322223.  
; 1111111.  ........  .2222322  22222222  22222222  3222233.  .1111111  11111111  11111111  ........  .....222  23222222  22223222  233.....  .2222322  3222233.  
; 3333333.  ........  .2222332  22222222  22222222  322223..  11111111  11111111  22222222  ........  .....222  23322222  22223222  23......  .2222332  322223..  
; 33333...  ........  ..222232  22222222  22222223  222233..  ...11111  11111111  11111111  ........  ......22  22322222  22232222  33......  ..222233  222233..  
; 333.....  ........  ..222233  22222222  22222223  22223...  ........  ........  11111111  ........  ......22  22332222  22232222  3.......  ..222222  22223...  
; 3.......  ........  ...22223  22222222  22222232  22233...  ........  ........  ........  ........  .......2  22232222  22322223  3.......  ...22222  22233...  
;
9BB4: F0 F8 FC FE FE F8 E0 80 00 00 00 00 FE F8 E0 80 
9BC4: 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 
9BD4: 18 08 0C 04 06 02 03 01 FF FF FF 7F 7F 3F 3F 1F 
9BE4: 00 00 00 00 00 00 00 00 FF FF FF FF FF FF FF FF 
9BF4: 00 00 00 00 00 01 01 02 FF FF FF FF FF FF FF FF 
9C04: 21 43 42 86 84 0C 08 18 FF FF FE FE FC FC F8 F8 
9C14: 00 00 00 7F FF 1F 00 00 00 00 00 00 00 00 00 00 
9C24: 00 00 00 FF FF FF 00 00 00 00 00 00 00 00 00 00 
9C34: 00 00 00 FF 00 FF FF 00 00 00 00 00 FF 00 00 00 
9C44: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
9C54: 01 00 00 00 00 00 00 00 1F 0F 0F 07 07 03 03 01 
9C64: 80 80 C0 40 60 20 30 10 FF FF FF FF FF FF FF FF 
9C74: 02 04 04 08 08 10 10 21 FF FF FF FF FF FF FF FF 
9C84: 10 30 20 60 40 C0 80 80 F0 F0 E0 E0 C0 C0 80 80 
9C94: 18 08 0C 04 06 03 00 00 FF FF FF 7F 7F 3F 3F 1F 
9CA4: 21 43 42 86 84 0C 08 18 FF FF FE FE FC FC F8 F8 


; ........  ...22222  2223....  ........  ..333333  ........  33333221  1111111.  21233112  23333222  23333222  11111112  23322331  11121112  33333232  22111112  
; ........  ....2222  2233....  .....2..  .3333333  33333...  33332221  1111111.  12333311  33333222  22233332  11111112  23333311  12111112  33332332  21111122  
; ........  ....2222  223.....  1.11.22.  .3333333  313111..  .3333211  111111..  12333333  33311222  22333322  21111122  33333222  33111112  23332322  21121112  
; ........  .....222  233.....  12112223  33333333  111111..  .3333221  111111..  13333322  33111112  23333322  22111122  33333223  22211111  23332322  21122112  
; .....111  .....222  23......  12112223  33333322  1111111.  .3332222  2111111.  33332222  21111112  23333322  21111112  33322332  11221111  22323222  21112111  
; .....1.1  ......22  33......  12112223  33333322  2111111.  .3333222  2211111.  33333222  11111111  23332222  21111112  33222322  21121111  22323222  22112211  
; .....111  ......22  3.......  12112223  33333322  11111111  ..333322  21111111  33333222  11111111  23333222  11111111  33222232  21111111  23333322  21122111  
; ........  .......3  3.......  1.11.22.  33333222  11111111  .3333322  21111111  33332222  21111111  33333322  11111111  33332232  22111111  33332322  21121111  
;
9CB4: 00 00 00 00 07 05 07 00 00 00 00 00 00 00 00 00 
9CC4: 00 00 00 00 00 00 00 01 1F 0F 0F 07 07 03 03 01 
9CD4: 10 30 20 60 40 C0 80 80 F0 F0 E0 E0 C0 C0 80 80 
9CE4: 00 00 B0 B1 B1 B1 B1 B0 00 04 06 4F 4F 4F 4F 06 
9CF4: 3F 7F 7F FF FC FC FC F8 3F 7F 7F FF FF FF FF FF 
9D04: 00 F8 FC FC FE 7E FF FF 00 F8 A0 00 00 80 00 00 
9D14: F9 F1 7B 79 70 78 3C 7C FE FE 7C 7E 7F 7F 3F 7F 
9D24: FE FE FC FC 7E 3E 7F 7F 00 00 00 00 80 C0 80 80 
9D34: 5E BF BF FC F0 F8 F8 F0 B9 7C 7F 7F FF FF FF FF 
9D44: 78 F8 F8 FE 7E FF FF 7F FF FF E7 C1 81 00 00 80 
9D54: 78 1E 3C 7C 7C 70 78 FC FF FF FF FF FF FF FF FF 
9D64: FE FE 7C 3C 7E 7E FF FF 01 01 83 C3 81 81 00 00 
9D74: 67 7F F8 F9 E6 C4 C2 F2 FE FC FF FF FF FF FF FF 
9D84: EE BE FE 1F CF 6F 7F 3F 11 41 C1 E0 30 90 80 C0 
9D94: FA F6 74 74 28 28 7C F4 FF FF FF FF FF FF FF FF 
9DA4: 3E 7C 6E 66 77 33 67 6F C1 83 91 99 88 CC 98 90 


; ......33  33131233  .123312.  .321....  ........  ........  .....1..  ........  ...2.333  3.......  ..222...  .33.3...  .....22.  22111112  22111111  ........  
; 333..333  31113333  .12321..  3222....  2133322.  ..233...  33.312.2  ........  ..2233..  33......  ..222.33  3.333...  .....22.  22211112  221111..  3333....  
; 33113333  11133333  .21.2...  .23.1...  133132..  .233122.  .1332211  ........  33233.11  .33.11.1  ...2333.  33323...  ....222.  22211122  21111...  32321...  
; 33113331  11133233  2222..3.  32.13222  33321312  .23122.2  2232.1..  ........  13221211  21321121  ...222..  .3212...  ....22..  22111122  211.....  222211..  
; 31133221  11113222  ..132133  3.33122.  .32221.1  13122.31  .322.23.  ........  11233333  21331121  ....222.  ..323...  ...222..  21111112  211.....  2221111.  
; 23332222  22113222  .331223.  ..332122  .2..222.  2322.12.  .2312223  ..1.....  31221213  31131121  ....2222  ...333..  .2222...  21111112  221111..  2111111.  
; 22232222  22112222  3331232.  ..321212  ..12.22.  .12..22.  .2331222  ..11....  33221211  33131121  .....222  22233322  2222....  21111111  22111111  1111111.  
; 22222222  22222222  ..31....  ....1..2  .22.....  ........  ..1312..  ..11....  33221.11  .31331.1  .......2  22223222  22......  11111111  22211111  111111..  
;
9DB4: 03 E7 FF FF F9 70 10 00 03 E7 CF CE 9E FF FF FF 
9DC4: FB FF FF FB F8 38 30 00 D7 8F 1F 1F 0F CF CF FF 
9DD4: 5C 54 20 02 37 72 F4 30 3A 38 48 F2 1B 6E EE 20 
9DE4: 50 80 28 98 B8 34 2A 08 60 F0 60 CF B6 3B 35 01 
9DF4: 00 78 F8 EE 45 00 20 00 00 BE 6C F5 78 4E 16 60 
9E04: 00 18 38 30 E3 44 40 00 00 38 76 6D 5A F2 26 00 
9E14: 04 D8 73 24 42 31 38 38 00 D5 3C F0 76 6F 77 14 
9E24: 00 00 00 00 00 20 30 30 00 00 00 00 00 00 00 00 
9E34: 07 0C DB CB DF CB CB CB 17 3C F8 74 3F B5 F4 F0 
9E44: 80 C0 6D 6D 7D FD FD 7D 80 C0 60 B2 B2 92 D2 58 
9E54: 00 03 0E 00 00 00 00 00 38 3B 1E 1C 0E 0F 07 01 
9E64: 68 B8 E8 50 28 1C 1C 08 68 B8 F8 68 38 1C FF FF 
9E74: 00 00 00 00 00 00 00 00 06 06 0E 0C 1C 78 F0 C0 
9E84: 3E 1E 1C 3C 7E 7E 7F FF C1 E1 E3 C3 81 81 80 00 
9E94: 3F 3C 78 60 60 3C 3F 1F C0 C0 80 80 80 C0 C0 E0 
9EA4: 00 F0 A8 0C 1E 7E FE FC 00 F0 F0 F0 E0 80 00 00 


; ..1111..  33333333
; .1....1.  33333333
; 1..11..1  33333333
; 1.1....1  33333333
; 1.1....1  33333333
; 1..11..1  33333333
; .1....1.  33333333 
; ..1111..  33333333
;
9EB4: 3C 42 99 A1 A1 99 42 3C 00 00 00 00 00 00 00 00 
9EC4: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 


9ED4: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
9EE4: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
9EF4: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
9F04: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
9F14: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
9F24: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
9F34: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
9F44: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
9F54: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
9F64: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
9F74: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
9F84: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
9F94: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
9FA4: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
9FB4: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
9FC4: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
9FD4: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
9FE4: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
9FF4: FF FF FF FF FF FF FF FF FF FF FF FF 

A000: 85 84         STA   <$84                ; 
A002: A5 84         LDA   <$84                ; 
A004: 95 84         STA   $84,X               ;
A006: A9 00         LDA   #$00                ;
A008: 95 70         STA   $70,X               ;
A00A: A9 2E         LDA   #$2E                ;
A00C: 9D 4F 03      STA   $034F,X             ;
A00F: 60            RTS                       ;
A010: 36 3B         ROL   $3B,X               ;
A012: 73                              ;
A013: 44                              ;
A014: 0A            ASL   A                   ;
A015: 21 41         AND   ($41,X)             ;
A017: 6C A5 AC      JMP   ($ACA5)             ; 
A01A: 29 40         AND   #$40                ;
A01C: A8            TAY                       ;
A01D: A9 02         LDA   #$02                ;
A01F: 18            CLC                       ;
A020: 75 70         ADC   <$70,X              ;
A022: 95 70         STA   $70,X               ;
A024: C0 40         CPY   #$40                ;
A026: D0 21         BNE   $A049               ; 
A028: AC 22 05      LDY   $0522               ; 
A02B: F0 1C         BEQ   $A049               ; 
A02D: 85 70         STA   <$70                ; 
A02F: 88            DEY                       ;
A030: F0 43         BEQ   $A075               ; 
A032: C9 80         CMP   #$80                ;
A034: D0 3F         BNE   $A075               ; 
A036: 0A            ASL   A                   ;
A037: 85 AC         STA   <$AC                ; 
A039: 8D 22 05      STA   $0522               ; 
A03C: 9D 4F 03      STA   $034F,X             ;
A03F: 8A            TXA                       ;
A040: 48            PHA                       ;
A041: 20 DE 71      JSR   $71DE               ; 
A044: 68            PLA                       ;
A045: AA            TAX                       ;
A046: 4C 8A A0      JMP   $A08A               ; 
A049: 20 A7 7A      JSR   $7AA7               ; 
A04C: A5 06         LDA   <$06                ; 
A04E: F0 25         BEQ   $A075               ; 
A050: A9 01         LDA   #$01                ;
A052: 85 98         STA   <$98                ; 
A054: 4A            LSR   A                   ;
A055: 85 C0         STA   <$C0                ; 
A057: 85 D3         STA   <$D3                ; 
A059: 85 5A         STA   <$5A                ; 
A05B: A9 40         LDA   #$40                ;
A05D: 85 AC         STA   <$AC                ; 
A05F: A9 F8         LDA   #$F8                ;
A061: 8D 48 02      STA   $0248               ; 
A064: 8D 4C 02      STA   $024C               ; 
A067: AD 23 05      LDA   $0523               ; 
A06A: 29 07         AND   #$07                ;
A06C: A8            TAY                       ;
A06D: B9 10 A0      LDA   $A010,Y             ;
A070: 85 EA         STA   <$EA                ; 
A072: EE 22 05      INC   $0522               ; 
A075: B5 70         LDA   $70,X               ;
A077: C9 F0         CMP   #$F0                ;
A079: 90 0F         BCC   $A08A               ; 
A07B: 20 8D A0      JSR   $A08D               ; 
A07E: AD 22 05      LDA   $0522               ; 
A081: F0 07         BEQ   $A08A               ; 
A083: 8A            TXA                       ;
A084: 48            PHA                       ;
A085: 20 82 F1      JSR   $F182               ; 
A088: 68            PLA                       ;
A089: AA            TAX                       ;
A08A: 4C 05 A1      JMP   $A105               ; 
A08D: A9 00         LDA   #$00                ;
A08F: 9D 4F 03      STA   $034F,X             ;
A092: 95 C0         STA   $C0,X               ;
A094: 95 D3         STA   $D3,X               ;
A096: 95 28         STA   $28,X               ;
A098: 95 AC         STA   $AC,X               ;
A09A: 9D F0 04      STA   $04F0,X             ;
A09D: A9 FF         LDA   #$FF                ;
A09F: 9D 92 04      STA   $0492,X             ;
A0A2: A9 01         LDA   #$01                ;
A0A4: 9D 05 04      STA   $0405,X             ;
A0A7: 60            RTS                       ;
A0A8: A5 12         LDA   <$12                ; 
A0AA: C9 05         CMP   #$05                ;
A0AC: D0 56         BNE   $A104               ; 
A0AE: 20 F5 A0      JSR   $A0F5               ; 
A0B1: AD 23 05      LDA   $0523               ; 
A0B4: 29 07         AND   #$07                ;
A0B6: A8            TAY                       ;
A0B7: B9 BE E6      LDA   $E6BE,Y             ;
A0BA: 85 00         STA   <$00                ; 
A0BC: AD 71 06      LDA   $0671               ; 
A0BF: F0 43         BEQ   $A104               ; 
A0C1: 24 00         BIT   <$00                ; 
A0C3: D0 1B         BNE   $A0E0               ; 
A0C5: 20 F5 A0      JSR   $A0F5               ; 
A0C8: A5 98         LDA   <$98                ; 
A0CA: 29 09         AND   #$09                ;
A0CC: F0 09         BEQ   $A0D7               ; 
A0CE: 06 00         ASL   <$00                ; 
A0D0: 90 EA         BCC   $A0BC               ; 
A0D2: 26 00         ROL   <$00                ; 
A0D4: 4C BC A0      JMP   $A0BC               ; 
A0D7: 46 00         LSR   <$00                ; 
A0D9: 90 E1         BCC   $A0BC               ; 
A0DB: 66 00         ROR   <$00                ; 
A0DD: 4C BC A0      JMP   $A0BC               ; 
A0E0: AD 08 05      LDA   $0508               ; 
A0E3: 0D 22 05      ORA   $0522               ; 
A0E6: D0 1C         BNE   $A104               ; 
A0E8: 20 BB FE      JSR   $FEBB               ; 
A0EB: F0 17         BEQ   $A104               ; 
A0ED: EE 08 05      INC   $0508               ; 
A0F0: 98            TYA                       ;
A0F1: AA            TAX                       ;
A0F2: 4C 02 A0      JMP   $A002               ; 
A0F5: EE 23 05      INC   $0523               ; 
A0F8: A5 98         LDA   <$98                ; 
A0FA: 29 09         AND   #$09                ;
A0FC: D0 06         BNE   $A104               ; 
A0FE: CE 23 05      DEC   $0523               ; 
A101: CE 23 05      DEC   $0523               ; 
A104: 60            RTS                       ;
A105: A9 01         LDA   #$01                ;
A107: 20 89 FA      JSR   $FA89               ; 
A10A: A5 15         LDA   <$15                ; 
A10C: 29 03         AND   #$03                ;
A10E: 20 88 79      JSR   $7988               ; 
A111: 20 72 FA      JSR   $FA72               ; 
A114: A9 00         LDA   #$00                ;
A116: 4C DF 77      JMP   $77DF               ; 
A119: 8D AD 8D      STA   $8DAD               ; 
A11C: 8D AD 8D      STA   $8DAD               ; 
A11F: AD 5D AD      LDA   $AD5D               ; 
A122: 22                              ;
A123: 05 F0         ORA   <$F0                ; 
A125: 15 EE         ORA   $EE,X               ;
A127: 22                              ;
A128: 05 A9         ORA   <$A9                ; 
A12A: 40            RTI                       ;
A12B: 85 AC         STA   <$AC                ; 
A12D: A2 09         LDX   #$09                ;
A12F: AD 23 05      LDA   $0523               ; 
A132: 29 07         AND   #$07                ;
A134: A8            TAY                       ;
A135: B9 19 A1      LDA   $A119,Y             ;
A138: 20 00 A0      JSR   $A000               ; 
A13B: 4C 90 6C      JMP   $6C90               ; 
A13E: A2 0C         LDX   #$0C                ;
A140: BD 4F 03      LDA   $034F,X             ;
A143: C9 68         CMP   #$68                ;
A145: F0 0C         BEQ   $A153               ; 
A147: C9 62         CMP   #$62                ;
A149: F0 08         BEQ   $A153               ; 
A14B: C9 65         CMP   #$65                ;
A14D: F0 04         BEQ   $A153               ; 
A14F: C9 66         CMP   #$66                ;
A151: D0 25         BNE   $A178               ; 
A153: B5 AC         LDA   $AC,X               ;
A155: C9 01         CMP   #$01                ;
A157: D0 1F         BNE   $A178               ; 
A159: A5 70         LDA   <$70                ; 
A15B: 38            SEC                       ;
A15C: F5 70         SBC   $70,X               ;
A15E: 20 1F 70      JSR   $701F               ; 
A161: C9 10         CMP   #$10                ;
A163: B0 13         BCS   $A178               ; 
A165: A5 84         LDA   <$84                ; 
A167: 18            CLC                       ;
A168: 69 03         ADC   #$03                ;
A16A: 38            SEC                       ;
A16B: F5 84         SBC   $84,X               ;
A16D: 20 1F 70      JSR   $701F               ; 
A170: C9 10         CMP   #$10                ;
A172: B0 04         BCS   $A178               ; 
A174: A9 00         LDA   #$00                ;
A176: 85 0F         STA   <$0F                ; 
A178: CA            DEX                       ;
A179: D0 C5         BNE   $A140               ; 
A17B: 60            RTS                       ;
A17C: AD 09 05      LDA   $0509               ; 
A17F: F0 2F         BEQ   $A1B0               ; 
A181: A5 28         LDA   <$28                ; 
A183: F0 18         BEQ   $A19D               ; 
A185: A0 18         LDY   #$18                ;
A187: A5 28         LDA   <$28                ; 
A189: F0 0B         BEQ   $A196               ; 
A18B: 29 07         AND   #$07                ;
A18D: C9 04         CMP   #$04                ;
A18F: 90 02         BCC   $A193               ; 
A191: A0 78         LDY   #$78                ;
A193: 84 14         STY   <$14                ; 
A195: 60            RTS                       ;
A196: A9 02         LDA   #$02                ;
A198: 85 63         STA   <$63                ; 
A19A: E6 13         INC   <$13                ; 
A19C: 60            RTS                       ;
A19D: 20 D6 A1      JSR   $A1D6               ; 
A1A0: A9 20         LDA   #$20                ;
A1A2: 8D 00 06      STA   $0600               ; 
A1A5: A9 01         LDA   #$01                ;
A1A7: 8D 72 06      STA   $0672               ; 
A1AA: 4A            LSR   A                   ;
A1AB: 85 AC         STA   <$AC                ; 
A1AD: 8D 09 05      STA   $0509               ; 
A1B0: 60            RTS                       ;
A1B1: EE 09 05      INC   $0509               ; 
A1B4: A9 C0         LDA   #$C0                ;
A1B6: 85 28         STA   <$28                ; 
A1B8: A9 40         LDA   #$40                ;
A1BA: 85 AC         STA   <$AC                ; 
A1BC: 60            RTS                       ;
A1BD: 3F                              ;
A1BE: 1C                              ;
A1BF: 04                              ;
A1C0: 0F                              ;
A1C1: 07                              ;
A1C2: 17                              ;
A1C3: 27                              ;
A1C4: FF                              ;
A1C5: 07                              ;
A1C6: 17                              ;
A1C7: 30 16         BMI   $A1DF               ; 
A1C9: 2C 3C 27      BIT   $273C               ; 
A1CC: 06 16         ASL   <$16                ; 
A1CE: A0 02         LDY   #$02                ;
A1D0: D0 06         BNE   $A1D8               ; 
A1D2: A0 05         LDY   #$05                ;
A1D4: D0 02         BNE   $A1D8               ; 
A1D6: A0 08         LDY   #$08                ;
A1D8: 98            TYA                       ;
A1D9: 48            PHA                       ;
A1DA: AE 01 03      LDX   $0301               ; 
A1DD: A0 00         LDY   #$00                ;
A1DF: B9 BD A1      LDA   $A1BD,Y             ;
A1E2: 9D 02 03      STA   $0302,X             ;
A1E5: E8            INX                       ;
A1E6: C8            INY                       ;
A1E7: C0 08         CPY   #$08                ;
A1E9: D0 F4         BNE   $A1DF               ; 
A1EB: 8E 01 03      STX   $0301               ; 
A1EE: 68            PLA                       ;
A1EF: A8            TAY                       ;
A1F0: A2 02         LDX   #$02                ;
A1F2: B9 C5 A1      LDA   $A1C5,Y             ;
A1F5: 9D 06 03      STA   $0306,X             ;
A1F8: 88            DEY                       ;
A1F9: CA            DEX                       ;
A1FA: 10 F6         BPL   $A1F2               ; 
A1FC: AE 40 03      LDX   $0340               ; 
A1FF: 60            RTS                       ;
A200: 20 93 FA      JSR   $FA93               ; 
A203: A9 0B         LDA   #$0B                ;
A205: 4C DF 77      JMP   $77DF               ; 
A208: A5 BF         LDA   <$BF                ; 
A20A: F0 0E         BEQ   $A21A               ; 
A20C: 20 14 73      JSR   $7314               ; 
A20F: D0 09         BNE   $A21A               ; 
A211: A9 00         LDA   #$00                ;
A213: 85 BF         STA   <$BF                ; 
A215: A9 02         LDA   #$02                ;
A217: 8D 02 06      STA   $0602               ; 
A21A: 60            RTS                       ;
A21B: 00            BRK                       ;
A21C: 00            BRK                       ;
A21D: F0 10         BEQ   $A22F               ; 
A21F: FB                              ;
A220: 13                              ;
A221: 03                              ;
A222: 03                              ;
A223: AD 94 03      LDA   $0394               ; 
A226: D0 13         BNE   $A23B               ; 
A228: AD F8 03      LDA   $03F8               ; 
A22B: F0 0E         BEQ   $A23B               ; 
A22D: A9 BB         LDA   #$BB                ;
A22F: 85 02         STA   <$02                ; 
A231: A2 08         LDX   #$08                ;
A233: AD 9E 04      LDA   $049E               ; 
A236: E6 02         INC   <$02                ; 
A238: CA            DEX                       ;
A239: 10 03         BPL   $A23E               ; 
A23B: A2 00         LDX   #$00                ;
A23D: 60            RTS                       ;
A23E: C5 02         CMP   <$02                ; 
A240: D0 F4         BNE   $A236               ; 
A242: A5 70         LDA   <$70                ; 
A244: 85 00         STA   <$00                ; 
A246: A5 84         LDA   <$84                ; 
A248: 85 01         STA   <$01                ; 
A24A: A5 98         LDA   <$98                ; 
A24C: 29 0C         AND   #$0C                ;
A24E: F0 15         BEQ   $A265               ; 
A250: A5 02         LDA   <$02                ; 
A252: 29 03         AND   #$03                ;
A254: A8            TAY                       ;
A255: A5 00         LDA   <$00                ; 
A257: C0 02         CPY   #$02                ;
A259: B0 03         BCS   $A25E               ; 
A25B: 18            CLC                       ;
A25C: 69 08         ADC   #$08                ;
A25E: 29 F0         AND   #$F0                ;
A260: 85 00         STA   <$00                ; 
A262: 4C 71 A2      JMP   $A271               ; 
A265: A5 02         LDA   <$02                ; 
A267: 4A            LSR   A                   ;
A268: B0 07         BCS   $A271               ; 
A26A: A5 01         LDA   <$01                ; 
A26C: 18            CLC                       ;
A26D: 69 08         ADC   #$08                ;
A26F: 85 01         STA   <$01                ; 
A271: 20 BB FE      JSR   $FEBB               ; 
A274: F0 55         BEQ   $A2CB               ; 
A276: A6 59         LDX   <$59                ; 
A278: A5 98         LDA   <$98                ; 
A27A: 20 13 70      JSR   $7013               ; 
A27D: A5 00         LDA   <$00                ; 
A27F: 18            CLC                       ;
A280: 79 1B A2      ADC   $A21B,Y             ;
A283: 95 70         STA   $70,X               ;
A285: A5 01         LDA   <$01                ; 
A287: 18            CLC                       ;
A288: 79 1F A2      ADC   $A21F,Y             ;
A28B: 95 84         STA   $84,X               ;
A28D: BD 92 04      LDA   $0492,X             ;
A290: F0 39         BEQ   $A2CB               ; 
A292: A0 0B         LDY   #$0B                ;
A294: 86 03         STX   <$03                ; 
A296: C4 03         CPY   <$03                ; 
A298: F0 1A         BEQ   $A2B4               ; 
A29A: B9 70 00      LDA   $0070,Y             ;
A29D: D5 70         CMP   $70,X               ;
A29F: D0 13         BNE   $A2B4               ; 
A2A1: B9 84 00      LDA   $0084,Y             ;
A2A4: D5 84         CMP   $84,X               ;
A2A6: D0 0C         BNE   $A2B4               ; 
A2A8: B9 4F 03      LDA   $034F,Y             ;
A2AB: D0 1E         BNE   $A2CB               ; 
A2AD: B9 92 04      LDA   $0492,Y             ;
A2B0: F0 19         BEQ   $A2CB               ; 
A2B2: D0 03         BNE   $A2B7               ; 
A2B4: 88            DEY                       ;
A2B5: D0 DF         BNE   $A296               ; 
A2B7: A9 1E         LDA   #$1E                ;
A2B9: A4 02         LDY   <$02                ; 
A2BB: C0 C0         CPY   #$C0                ;
A2BD: B0 02         BCS   $A2C1               ; 
A2BF: A9 22         LDA   #$22                ;
A2C1: 9D 4F 03      STA   $034F,X             ;
A2C4: 20 DA FE      JSR   $FEDA               ; 
A2C7: A9 3F         LDA   #$3F                ;
A2C9: 95 28         STA   $28,X               ;
A2CB: A2 00         LDX   #$00                ;
A2CD: 60            RTS                       ;
A2CE: 78            SEI                       ;
A2CF: 70 80         BVS   $A251               ; 
A2D1: 60            RTS                       ;
A2D2: 70 80         BVS   $A254               ; 
A2D4: 90 70         BCC   $A346               ; 
A2D6: 80                              ;
A2D7: 78            SEI                       ;
A2D8: 70 80         BVS   $A25A               ; 
A2DA: 80                              ;
A2DB: 90 90         BCC   $A26D               ; 
A2DD: 90 90         BCC   $A26F               ; 
A2DF: A0 A0         LDY   #$A0                ;
A2E1: B0 BD         BCS   $A2A0               ; 
A2E3: BF                              ;
A2E4: 04                              ;
A2E5: 85 01         STA   <$01                ; 
A2E7: A9 35         LDA   #$35                ;
A2E9: 85 00         STA   <$00                ; 
A2EB: A2 0A         LDX   #$0A                ;
A2ED: 20 FE A2      JSR   $A2FE               ; 
A2F0: BD CD A2      LDA   $A2CD,X             ;
A2F3: 95 70         STA   $70,X               ;
A2F5: BD D7 A2      LDA   $A2D7,X             ;
A2F8: 95 84         STA   $84,X               ;
A2FA: CA            DEX                       ;
A2FB: D0 F0         BNE   $A2ED               ; 
A2FD: 60            RTS                       ;
A2FE: A5 00         LDA   <$00                ; 
A300: 9D 4F 03      STA   $034F,X             ;
A303: A9 00         LDA   #$00                ;
A305: 9D 92 04      STA   $0492,X             ;
A308: A5 01         LDA   <$01                ; 
A30A: 9D BF 04      STA   $04BF,X             ;
A30D: 60            RTS                       ;
A30E: 20 20 D0      JSR   $D020               ; 
A311: D0 40         BNE   $A353               ; 
A313: B0 5D         BCS   $A372               ; 
A315: BD 5D BD      LDA   $BD5D,X             ;
A318: 8D 8D BD      STA   $BD8D               ; 
A31B: BF                              ;
A31C: 04                              ;
A31D: 85 01         STA   <$01                ; 
A31F: A0 05         LDY   #$05                ;
A321: A9 49         LDA   #$49                ;
A323: 85 00         STA   <$00                ; 
A325: DD 4F 03      CMP   $034F,X             ;
A328: F0 02         BEQ   $A32C               ; 
A32A: A0 03         LDY   #$03                ;
A32C: 98            TYA                       ;
A32D: 18            CLC                       ;
A32E: 6D 40 03      ADC   $0340               ; 
A331: AA            TAX                       ;
A332: B9 0E A3      LDA   $A30E,Y             ;
A335: 95 70         STA   $70,X               ;
A337: B9 14 A3      LDA   $A314,Y             ;
A33A: 95 84         STA   $84,X               ;
A33C: 20 FE A2      JSR   $A2FE               ; 
A33F: CA            DEX                       ;
A340: 88            DEY                       ;
A341: 10 E9         BPL   $A32C               ; 
A343: 60            RTS                       ;
A344: 05 09         ORA   <$09                ; 
A346: 06 0A         ASL   <$0A                ; 
A348: 01 02         ORA   ($02,X)             ;
A34A: B5 AC         LDA   $AC,X               ;
A34C: D0 4B         BNE   $A399               ; 
A34E: A5 84         LDA   <$84                ; 
A350: 38            SEC                       ;
A351: F5 84         SBC   $84,X               ;
A353: 20 1F 70      JSR   $701F               ; 
A356: C9 0E         CMP   #$0E                ;
A358: B0 23         BCS   $A37D               ; 
A35A: A0 01         LDY   #$01                ;
A35C: A5 70         LDA   <$70                ; 
A35E: D5 70         CMP   $70,X               ;
A360: F0 1B         BEQ   $A37D               ; 
A362: B0 02         BCS   $A366               ; 
A364: A0 02         LDY   #$02                ;
A366: B5 70         LDA   $70,X               ;
A368: 9D 80 03      STA   $0380,X             ;
A36B: 98            TYA                       ;
A36C: 95 98         STA   $98,X               ;
A36E: 3D 43 A3      AND   $A343,X             ;
A371: F0 07         BEQ   $A37A               ; 
A373: F6 AC         INC   $AC,X               ;
A375: A9 70         LDA   #$70                ;
A377: 9D BC 03      STA   $03BC,X             ;
A37A: 4C EB A3      JMP   $A3EB               ; 
A37D: A5 70         LDA   <$70                ; 
A37F: 38            SEC                       ;
A380: F5 70         SBC   $70,X               ;
A382: 20 1F 70      JSR   $701F               ; 
A385: C9 0E         CMP   #$0E                ;
A387: B0 F1         BCS   $A37A               ; 
A389: A0 04         LDY   #$04                ;
A38B: A5 84         LDA   <$84                ; 
A38D: D5 84         CMP   $84,X               ;
A38F: F0 E9         BEQ   $A37A               ; 
A391: B0 02         BCS   $A395               ; 
A393: A0 08         LDY   #$08                ;
A395: B5 84         LDA   $84,X               ;
A397: D0 CF         BNE   $A368               ; 
A399: B5 98         LDA   $98,X               ;
A39B: 85 0F         STA   <$0F                ; 
A39D: 20 8D F0      JSR   $F08D               ; 
A3A0: BD 94 03      LDA   $0394,X             ;
A3A3: 29 0F         AND   #$0F                ;
A3A5: D0 03         BNE   $A3AA               ; 
A3A7: 9D 94 03      STA   $0394,X             ;
A3AA: 20 A7 7A      JSR   $7AA7               ; 
A3AD: B4 70         LDY   $70,X               ;
A3AF: A9 78         LDA   #$78                ;
A3B1: 85 00         STA   <$00                ; 
A3B3: B5 98         LDA   $98,X               ;
A3B5: 29 0C         AND   #$0C                ;
A3B7: F0 06         BEQ   $A3BF               ; 
A3B9: B4 84         LDY   $84,X               ;
A3BB: A9 90         LDA   #$90                ;
A3BD: 85 00         STA   <$00                ; 
A3BF: B5 AC         LDA   $AC,X               ;
A3C1: 29 01         AND   #$01                ;
A3C3: F0 1C         BEQ   $A3E1               ; 
A3C5: 98            TYA                       ;
A3C6: 38            SEC                       ;
A3C7: E5 00         SBC   <$00                ; 
A3C9: 20 1F 70      JSR   $701F               ; 
A3CC: C9 05         CMP   #$05                ;
A3CE: B0 0E         BCS   $A3DE               ; 
A3D0: B5 98         LDA   $98,X               ;
A3D2: 20 13 70      JSR   $7013               ; 
A3D5: 95 98         STA   $98,X               ;
A3D7: A9 20         LDA   #$20                ;
A3D9: 9D BC 03      STA   $03BC,X             ;
A3DC: F6 AC         INC   $AC,X               ;
A3DE: 4C EB A3      JMP   $A3EB               ; 
A3E1: 98            TYA                       ;
A3E2: DD 80 03      CMP   $0380,X             ;
A3E5: D0 04         BNE   $A3EB               ; 
A3E7: A9 00         LDA   #$00                ;
A3E9: 95 AC         STA   $AC,X               ;
A3EB: 4C BA 79      JMP   $79BA               ; 
A3EE: 8A            TXA                       ;
A3EF: 48            PHA                       ;
A3F0: A5 84         LDA   <$84                ; 
A3F2: 38            SEC                       ;
A3F3: F5 84         SBC   $84,X               ;
A3F5: 20 1F 70      JSR   $701F               ; 
A3F8: C9 09         CMP   #$09                ;
A3FA: B0 1A         BCS   $A416               ; 
A3FC: A5 70         LDA   <$70                ; 
A3FE: 38            SEC                       ;
A3FF: F5 70         SBC   $70,X               ;
A401: 20 1F 70      JSR   $701F               ; 
A404: C9 09         CMP   #$09                ;
A406: B0 0E         BCS   $A416               ; 
A408: 20 A3 74      JSR   $74A3               ; 
A40B: 20 B1 FE      JSR   $FEB1               ; 
A40E: A9 00         LDA   #$00                ;
A410: 8D 4E 03      STA   $034E               ; 
A413: 4C 20 A4      JMP   $A420               ; 
A416: 20 93 FA      JSR   $FA93               ; 
A419: A2 16         LDX   #$16                ;
A41B: A0 16         LDY   #$16                ;
A41D: 20 35 E7      JSR   $E735               ; 
A420: 68            PLA                       ;
A421: AA            TAX                       ;
A422: 60            RTS                       ;

A423: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A440: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A460: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A480: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A4A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A4C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A4E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 

A500: A9 00         LDA   #$00                ;
A502: 85 13         STA   <$13                ; 
A504: E6 11         INC   <$11                ; 
A506: 60            RTS                       ;
A507: 20 B6 08      JSR   $08B6               ; 
A50A: 24 24         BIT   <$24                ; 
A50C: 24 24         BIT   <$24                ; 
A50E: 24 24         BIT   <$24                ; 
A510: 24 24         BIT   <$24                ; 
A512: 20 D6 08      JSR   $08D6               ; 
A515: 24 24         BIT   <$24                ; 
A517: 24 24         BIT   <$24                ; 
A519: 24 24         BIT   <$24                ; 
A51B: 24 24         BIT   <$24                ; 
A51D: 20 6C 03      JSR   $036C               ; 
A520: 21 00         AND   ($00,X)             ;
A522: 24 20         BIT   <$20                ; 
A524: AC 03 21      LDY   $2103               ; 
A527: 00            BRK                       ;
A528: 24 20         BIT   <$20                ; 
A52A: CC 03 21      CPY   $2103               ; 
A52D: 00            BRK                       ;
A52E: 24 FF         BIT   <$FF                ; 
A530: A5 14         LDA   <$14                ; 
A532: D0 D2         BNE   $A506               ; 
A534: AD 02 03      LDA   $0302               ; 
A537: 10 CD         BPL   $A506               ; 
A539: A0 27         LDY   #$27                ;
A53B: AD 6D 06      LDA   $066D               ; 
A53E: F0 06         BEQ   $A546               ; 
A540: A0 26         LDY   #$26                ;
A542: C9 FF         CMP   #$FF                ;
A544: D0 05         BNE   $A54B               ; 
A546: A9 00         LDA   #$00                ;
A548: 99 57 06      STA   $0657,Y             ;
A54B: A5 15         LDA   <$15                ; 
A54D: 4A            LSR   A                   ;
A54E: B0 B6         BCS   $A506               ; 
A550: AD 7D 06      LDA   $067D               ; 
A553: F0 0B         BEQ   $A560               ; 
A555: CE 7D 06      DEC   $067D               ; 
A558: EE 6D 06      INC   $066D               ; 
A55B: A9 10         LDA   #$10                ;
A55D: 8D 04 06      STA   $0604               ; 
A560: AD 7E 06      LDA   $067E               ; 
A563: F0 0B         BEQ   $A570               ; 
A565: CE 7E 06      DEC   $067E               ; 
A568: CE 6D 06      DEC   $066D               ; 
A56B: A9 10         LDA   #$10                ;
A56D: 8D 04 06      STA   $0604               ; 
A570: A0 28         LDY   #$28                ;
A572: B9 97 6C      LDA   $6C97,Y             ;
A575: 99 02 03      STA   $0302,Y             ;
A578: 88            DEY                       ;
A579: 10 F7         BPL   $A572               ; 
A57B: A0 03         LDY   #$03                ;
A57D: AD 6F 06      LDA   $066F               ; 
A580: 85 0E         STA   <$0E                ; 
A582: AD 70 06      LDA   $0670               ; 
A585: 85 0F         STA   <$0F                ; 
A587: 20 79 6E      JSR   $6E79               ; 
A58A: A2 02         LDX   #$02                ;
A58C: AD 6D 06      LDA   $066D               ; 
A58F: A0 1B         LDY   #$1B                ;
A591: 20 50 6D      JSR   $6D50               ; 
A594: A0 21         LDY   #$21                ;
A596: AD 64 06      LDA   $0664               ; 
A599: F0 13         BEQ   $A5AE               ; 
A59B: 84 00         STY   <$00                ; 
A59D: A9 21         LDA   #$21                ;
A59F: 85 01         STA   <$01                ; 
A5A1: A9 0A         LDA   #$0A                ;
A5A3: 20 75 6D      JSR   $6D75               ; 
A5A6: A2 08         LDX   #$08                ;
A5A8: 20 55 6D      JSR   $6D55               ; 
A5AB: 4C 46 6D      JMP   $6D46               ; 
A5AE: A2 08         LDX   #$08                ;
A5B0: AD 6E 06      LDA   $066E               ; 
A5B3: 20 50 6D      JSR   $6D50               ; 
A5B6: A2 0E         LDX   #$0E                ;
A5B8: AD 58 06      LDA   $0658               ; 
A5BB: A0 27         LDY   #$27                ;
A5BD: 4C 50 6D      JMP   $6D50               ; 
A5C0: 84 00         STY   <$00                ; 
A5C2: 20 64 6D      JSR   $6D64               ; 
A5C5: A0 02         LDY   #$02                ;
A5C7: A6 00         LDX   <$00                ; 
A5C9: B9 01 00      LDA   $0001,Y             ;
A5CC: 9D 02 03      STA   $0302,X             ;
A5CF: CA            DEX                       ;
A5D0: 88            DEY                       ;
A5D1: 10 F6         BPL   $A5C9               ; 
A5D3: 60            RTS                       ;
A5D4: 20 55 6E      JSR   $6E55               ; 
A5D7: C0 24         CPY   #$24                ;
A5D9: D0 02         BNE   $A5DD               ; 
A5DB: A0 21         LDY   #$21                ;
A5DD: 84 01         STY   <$01                ; 
A5DF: C9 24         CMP   #$24                ;
A5E1: D0 08         BNE   $A5EB               ; 
A5E3: A5 03         LDA   <$03                ; 
A5E5: 85 02         STA   <$02                ; 
A5E7: A9 24         LDA   #$24                ;
A5E9: 85 03         STA   <$03                ; 
A5EB: 60            RTS                       ;
A5EC: A0 01         LDY   #$01                ;
A5EE: D0 02         BNE   $A5F2               ; 
A5F0: A0 03         LDY   #$03                ;
A5F2: 19 00 06      ORA   $0600,Y             ;
A5F5: 99 00 06      STA   $0600,Y             ;
A5F8: 60            RTS                       ;
A5F9: A5 13         LDA   <$13                ; 
A5FB: 48            PHA                       ;
A5FC: 20 C6 87      JSR   $87C6               ; 
A5FF: 20 B6 B0      JSR   $B0B6               ; 
A602: A9 70         LDA   #$70                ;
A604: 85 70         STA   <$70                ; 
A606: A9 DD         LDA   #$DD                ;
A608: 85 84         STA   <$84                ; 
A60A: A9 08         LDA   #$08                ;
A60C: 85 98         STA   <$98                ; 
A60E: 20 3C F2      JSR   $F23C               ; 
A611: 20 CB EA      JSR   $EACB               ; 
A614: 68            PLA                       ;
A615: 85 13         STA   <$13                ; 
A617: A9 00         LDA   #$00                ;
A619: 85 11         STA   <$11                ; 
A61B: E6 13         INC   <$13                ; 
A61D: A9 30         LDA   #$30                ;
A61F: 8D 94 03      STA   $0394               ; 
A622: A9 01         LDA   #$01                ;
A624: 85 5A         STA   <$5A                ; 
A626: 60            RTS                       ;
A627: A9 00         LDA   #$00                ;
A629: 8D 2B 05      STA   $052B               ; 
A62C: 8D 2C 05      STA   $052C               ; 
A62F: 8D 2D 05      STA   $052D               ; 
A632: 60            RTS                       ;
A633: 08            PHP                       ;
A634: 04                              ;
A635: 02                              ;
A636: 01 1A         ORA   ($1A,X)             ;
A638: 60            RTS                       ;
A639: 92                              ;
A63A: 60            RTS                       ;
A63B: 02                              ;
A63C: 60            RTS                       ;
A63D: 12                              ;
A63E: 65 15         ADC   <$15                ; 
A640: 65 18         ADC   <$18                ; 
A642: 65 1B         ADC   <$1B                ; 
A644: 65 42         ADC   <$42                ; 
A646: 60            RTS                       ;
A647: 12                              ;
A648: 62                              ;
A649: 0A            ASL   A                   ;
A64A: 60            RTS                       ;
A64B: 13                              ;
A64C: 65 16         ADC   <$16                ; 
A64E: 65 19         ADC   <$19                ; 
A650: 65 1C         ADC   <$1C                ; 
A652: 65 6A         ADC   <$6A                ; 
A654: 60            RTS                       ;
A655: 92                              ;
A656: 63                              ;
A657: 12                              ;
A658: 60            RTS                       ;
A659: 14                              ;
A65A: 65 17         ADC   <$17                ; 
A65C: 65 1A         ADC   <$1A                ; 
A65E: 65 1D         ADC   <$1D                ; 
A660: 65 A9         ADC   <$A9                ; 
A662: FF                              ;
A663: A4 16         LDY   <$16                ; 
A665: 18            CLC                       ;
A666: 69 0E         ADC   #$0E                ;
A668: 88            DEY                       ;
A669: 10 FA         BPL   $A665               ; 
A66B: A8            TAY                       ;
A66C: A2 0D         LDX   #$0D                ;
A66E: B9 C7 6D      LDA   $6DC7,Y             ;
A671: 95 00         STA   $00,X               ;
A673: 88            DEY                       ;
A674: CA            DEX                       ;
A675: 10 F7         BPL   $A66E               ; 
A677: A9 7F         LDA   #$7F                ;
A679: 85 0E         STA   <$0E                ; 
A67B: A9 06         LDA   #$06                ;
A67D: 85 0F         STA   <$0F                ; 
A67F: 60            RTS                       ;
A680: A5 3B         LDA   <$3B                ; 
A682: D0 08         BNE   $A68C               ; 
A684: 98            TYA                       ;
A685: 20 80 6D      JSR   $6D80               ; 
A688: A9 0A         LDA   #$0A                ;
A68A: 85 3B         STA   <$3B                ; 
A68C: 60            RTS                       ;
A68D: A2 60         LDX   #$60                ;
A68F: A9 F8         LDA   #$F8                ;
A691: 9D 00 02      STA   $0200,X             ;
A694: E8            INX                       ;
A695: E8            INX                       ;
A696: E8            INX                       ;
A697: E8            INX                       ;
A698: E0 00         CPX   #$00                ;
A69A: D0 F5         BNE   $A691               ; 
A69C: AD 42 03      LDA   $0342               ; 
A69F: 20 39 6E      JSR   $6E39               ; 
A6A2: 8D 42 03      STA   $0342               ; 
A6A5: 60            RTS                       ;
A6A6: AD 41 03      LDA   $0341               ; 
A6A9: 18            CLC                       ;
A6AA: 69 01         ADC   #$01                ;
A6AC: C9 28         CMP   #$28                ;
A6AE: D0 02         BNE   $A6B2               ; 
A6B0: A9 00         LDA   #$00                ;
A6B2: 8D 41 03      STA   $0341               ; 
A6B5: 60            RTS                       ;
A6B6: A5 84         LDA   <$84                ; 
A6B8: C9 8E         CMP   #$8E                ;
A6BA: B0 F9         BCS   $A6B5               ; 
A6BC: A5 0F         LDA   <$0F                ; 
A6BE: 29 08         AND   #$08                ;
A6C0: F0 F3         BEQ   $A6B5               ; 
A6C2: 4C 49 F1      JMP   $F149               ; 
A6C5: 20 6E 6E      JSR   $6E6E               ; 
A6C8: 85 03         STA   <$03                ; 
A6CA: 98            TYA                       ;
A6CB: 20 6E 6E      JSR   $6E6E               ; 
A6CE: C0 00         CPY   #$00                ;
A6D0: D0 07         BNE   $A6D9               ; 
A6D2: A0 24         LDY   #$24                ;
A6D4: C9 00         CMP   #$00                ;
A6D6: D0 01         BNE   $A6D9               ; 
A6D8: 98            TYA                       ;
A6D9: 85 02         STA   <$02                ; 
A6DB: 84 01         STY   <$01                ; 
A6DD: 60            RTS                       ;
A6DE: A0 00         LDY   #$00                ;
A6E0: C9 0A         CMP   #$0A                ;
A6E2: 90 F9         BCC   $A6DD               ; 
A6E4: E9 0A         SBC   #$0A                ;
A6E6: C8            INY                       ;
A6E7: D0 F7         BNE   $A6E0               ; 
A6E9: 84 0D         STY   <$0D                ; 
A6EB: A5 0E         LDA   <$0E                ; 
A6ED: 48            PHA                       ;
A6EE: 29 0F         AND   #$0F                ;
A6F0: 85 00         STA   <$00                ; 
A6F2: A9 0F         LDA   #$0F                ;
A6F4: 38            SEC                       ;
A6F5: E5 00         SBC   <$00                ; 
A6F7: 85 00         STA   <$00                ; 
A6F9: 68            PLA                       ;
A6FA: 4A            LSR   A                   ;
A6FB: 4A            LSR   A                   ;
A6FC: 4A            LSR   A                   ;
A6FD: 4A            LSR   A                   ;
A6FE: 85 01         STA   <$01                ; 
A700: A9 0F         LDA   #$0F                ;
A702: 38            SEC                       ;
A703: E5 01         SBC   <$01                ; 
A705: 85 01         STA   <$01                ; 
A707: A2 00         LDX   #$00                ;
A709: 98            TYA                       ;
A70A: 18            CLC                       ;
A70B: 69 07         ADC   #$07                ;
A70D: 85 0B         STA   <$0B                ; 
A70F: A0 07         LDY   #$07                ;
A711: C0 FF         CPY   #$FF                ;
A713: D0 09         BNE   $A71E               ; 
A715: A5 0D         LDA   <$0D                ; 
A717: 18            CLC                       ;
A718: 69 12         ADC   #$12                ;
A71A: 85 0B         STA   <$0B                ; 
A71C: A0 12         LDY   #$12                ;
A71E: A5 0E         LDA   <$0E                ; 
A720: F0 04         BEQ   $A726               ; 
A722: E4 01         CPX   <$01                ; 
A724: B0 04         BCS   $A72A               ; 
A726: A9 24         LDA   #$24                ;
A728: D0 1D         BNE   $A747               ; 
A72A: E4 00         CPX   <$00                ; 
A72C: F0 06         BEQ   $A734               ; 
A72E: 90 15         BCC   $A745               ; 
A730: A9 F2         LDA   #$F2                ;
A732: D0 13         BNE   $A747               ; 
A734: A5 0F         LDA   <$0F                ; 
A736: F0 0D         BEQ   $A745               ; 
A738: C9 80         CMP   #$80                ;
A73A: B0 F4         BCS   $A730               ; 
A73C: A9 00         LDA   #$00                ;
A73E: 8D 29 05      STA   $0529               ; 
A741: A9 65         LDA   #$65                ;
A743: D0 02         BNE   $A747               ; 
A745: A9 66         LDA   #$66                ;
A747: 84 0C         STY   <$0C                ; 
A749: A4 0B         LDY   <$0B                ; 
A74B: 99 02 03      STA   $0302,Y             ;
A74E: C6 0B         DEC   <$0B                ; 
A750: A4 0C         LDY   <$0C                ; 
A752: 88            DEY                       ;
A753: E8            INX                       ;
A754: E0 10         CPX   #$10                ;
A756: D0 B9         BNE   $A711               ; 
A758: 60            RTS                       ;
A759: A9 80         LDA   #$80                ;
A75B: 8D 04 06      STA   $0604               ; 
A75E: 8D 03 06      STA   $0603               ; 
A761: 0A            ASL   A                   ;
A762: 8D 05 06      STA   $0605               ; 
A765: 8D 07 06      STA   $0607               ; 
A768: 60            RTS                       ;
A769: 08            PHP                       ;
A76A: 00            BRK                       ;
A76B: A0 0A         LDY   #$0A                ;
A76D: A2 00         LDX   #$00                ;
A76F: B5 70         LDA   $70,X               ;
A771: 85 00         STA   <$00                ; 
A773: A2 01         LDX   #$01                ;
A775: A5 00         LDA   <$00                ; 
A777: 18            CLC                       ;
A778: 7D F9 6E      ADC   $6EF9,X             ;
A77B: C9 E9         CMP   #$E9                ;
A77D: B0 04         BCS   $A783               ; 
A77F: C9 10         CMP   #$10                ;
A781: B0 08         BCS   $A78B               ; 
A783: B9 40 02      LDA   $0240,Y             ;
A786: 09 20         ORA   #$20                ;
A788: 99 40 02      STA   $0240,Y             ;
A78B: C8            INY                       ;
A78C: C8            INY                       ;
A78D: C8            INY                       ;
A78E: C8            INY                       ;
A78F: C0 00         CPY   #$00                ;
A791: D0 02         BNE   $A795               ; 
A793: A0 20         LDY   #$20                ;
A795: CA            DEX                       ;
A796: 10 DD         BPL   $A775               ; 
A798: 60            RTS                       ;
A799: A0 02         LDY   #$02                ;
A79B: B5 70         LDA   $70,X               ;
A79D: 85 00         STA   <$00                ; 
A79F: E0 00         CPX   #$00                ;
A7A1: F0 12         BEQ   $A7B5               ; 
A7A3: E0 0D         CPX   #$0D                ;
A7A5: B0 07         BCS   $A7AE               ; 
A7A7: BD 4F 03      LDA   $034F,X             ;
A7AA: C9 5C         CMP   #$5C                ;
A7AC: D0 07         BNE   $A7B5               ; 
A7AE: A5 00         LDA   <$00                ; 
A7B0: 18            CLC                       ;
A7B1: 69 0B         ADC   #$0B                ;
A7B3: 85 00         STA   <$00                ; 
A7B5: A5 00         LDA   <$00                ; 
A7B7: CD 46 03      CMP   $0346               ; 
A7BA: 90 1F         BCC   $A7DB               ; 
A7BC: E0 00         CPX   #$00                ;
A7BE: F0 12         BEQ   $A7D2               ; 
A7C0: E0 0D         CPX   #$0D                ;
A7C2: B0 07         BCS   $A7CB               ; 
A7C4: BD 4F 03      LDA   $034F,X             ;
A7C7: C9 5C         CMP   #$5C                ;
A7C9: D0 07         BNE   $A7D2               ; 
A7CB: A5 00         LDA   <$00                ; 
A7CD: 38            SEC                       ;
A7CE: E9 17         SBC   #$17                ;
A7D0: 85 00         STA   <$00                ; 
A7D2: A0 01         LDY   #$01                ;
A7D4: A5 00         LDA   <$00                ; 
A7D6: CD 47 03      CMP   $0347               ; 
A7D9: 90 4A         BCC   $A825               ; 
A7DB: 98            TYA                       ;
A7DC: 25 0F         AND   <$0F                ; 
A7DE: F0 45         BEQ   $A825               ; 
A7E0: 4C 49 F1      JMP   $F149               ; 
A7E3: A0 08         LDY   #$08                ;
A7E5: B5 84         LDA   $84,X               ;
A7E7: 85 00         STA   <$00                ; 
A7E9: E0 00         CPX   #$00                ;
A7EB: F0 12         BEQ   $A7FF               ; 
A7ED: E0 0D         CPX   #$0D                ;
A7EF: B0 07         BCS   $A7F8               ; 
A7F1: BD 4F 03      LDA   $034F,X             ;
A7F4: C9 5C         CMP   #$5C                ;
A7F6: D0 07         BNE   $A7FF               ; 
A7F8: A5 00         LDA   <$00                ; 
A7FA: 18            CLC                       ;
A7FB: 69 0F         ADC   #$0F                ;
A7FD: 85 00         STA   <$00                ; 
A7FF: A5 00         LDA   <$00                ; 
A801: CD 48 03      CMP   $0348               ; 
A804: 90 D5         BCC   $A7DB               ; 
A806: E0 00         CPX   #$00                ;
A808: F0 12         BEQ   $A81C               ; 
A80A: E0 0D         CPX   #$0D                ;
A80C: B0 07         BCS   $A815               ; 
A80E: BD 4F 03      LDA   $034F,X             ;
A811: C9 5C         CMP   #$5C                ;
A813: D0 07         BNE   $A81C               ; 
A815: A5 00         LDA   <$00                ; 
A817: 38            SEC                       ;
A818: E9 21         SBC   #$21                ;
A81A: 85 00         STA   <$00                ; 
A81C: A0 04         LDY   #$04                ;
A81E: A5 00         LDA   <$00                ; 
A820: CD 49 03      CMP   $0349               ; 
A823: B0 B6         BCS   $A7DB               ; 
A825: 60            RTS                       ;
A826: 85 0F         STA   <$0F                ; 
A828: 20 29 6F      JSR   $6F29               ; 
A82B: 20 73 6F      JSR   $6F73               ; 
A82E: A5 0F         LDA   <$0F                ; 
A830: 60            RTS                       ;
A831: BD A8 03      LDA   $03A8,X             ;
A834: 18            CLC                       ;
A835: 7D BC 03      ADC   $03BC,X             ;
A838: 9D A8 03      STA   $03A8,X             ;
A83B: 08            PHP                       ;
A83C: BD 94 03      LDA   $0394,X             ;
A83F: CD 0E 01      CMP   $010E               ; 
A842: F0 05         BEQ   $A849               ; 
A844: CD 0F 01      CMP   $010F               ; 
A847: D0 03         BNE   $A84C               ; 
A849: 28            PLP                       ;
A84A: 18            CLC                       ;
A84B: 08            PHP                       ;
A84C: 28            PLP                       ;
A84D: 08            PHP                       ;
A84E: BD 94 03      LDA   $0394,X             ;
A851: 69 00         ADC   #$00                ;
A853: 9D 94 03      STA   $0394,X             ;
A856: 28            PLP                       ;
A857: 60            RTS                       ;
A858: BD A8 03      LDA   $03A8,X             ;
A85B: 38            SEC                       ;
A85C: FD BC 03      SBC   $03BC,X             ;
A85F: 9D A8 03      STA   $03A8,X             ;
A862: 08            PHP                       ;
A863: BD 94 03      LDA   $0394,X             ;
A866: CD 0E 01      CMP   $010E               ; 
A869: F0 05         BEQ   $A870               ; 
A86B: CD 0F 01      CMP   $010F               ; 
A86E: D0 03         BNE   $A873               ; 
A870: 28            PLP                       ;
A871: 38            SEC                       ;
A872: 08            PHP                       ;
A873: 28            PLP                       ;
A874: 08            PHP                       ;
A875: BD 94 03      LDA   $0394,X             ;
A878: E9 00         SBC   #$00                ;
A87A: 9D 94 03      STA   $0394,X             ;
A87D: 28            PLP                       ;
A87E: 60            RTS                       ;
A87F: 04                              ;
A880: 08            PHP                       ;
A881: 01 02         ORA   ($02,X)             ;
A883: A0 03         LDY   #$03                ;
A885: 4A            LSR   A                   ;
A886: B0 03         BCS   $A88B               ; 
A888: 88            DEY                       ;
A889: 10 FA         BPL   $A885               ; 
A88B: B9 0F 70      LDA   $700F,Y             ;
A88E: 60            RTS                       ;
A88F: 10 05         BPL   $A896               ; 
A891: 49 FF         EOR   #$FF                ;
A893: 18            CLC                       ;
A894: 69 01         ADC   #$01                ;
A896: 60            RTS                       ;
A897: 20 B6 6F      JSR   $6FB6               ; 
A89A: F0 19         BEQ   $A8B5               ; 
A89C: BD 94 03      LDA   $0394,X             ;
A89F: 48            PHA                       ;
A8A0: A9 00         LDA   #$00                ;
A8A2: 9D 94 03      STA   $0394,X             ;
A8A5: 20 8D F0      JSR   $F08D               ; 
A8A8: 68            PLA                       ;
A8A9: A4 0E         LDY   <$0E                ; 
A8AB: D0 04         BNE   $A8B1               ; 
A8AD: 18            CLC                       ;
A8AE: 7D 94 03      ADC   $0394,X             ;
A8B1: 9D 94 03      STA   $0394,X             ;
A8B4: 60            RTS                       ;
A8B5: A9 80         LDA   #$80                ;
A8B7: 85 0E         STA   <$0E                ; 
A8B9: 60            RTS                       ;
A8BA: 48            PHA                       ;
A8BB: A8            TAY                       ;
A8BC: A9 02         LDA   #$02                ;
A8BE: 85 0A         STA   <$0A                ; 
A8C0: B9 70 00      LDA   $0070,Y             ;
A8C3: B4 70         LDY   $70,X               ;
A8C5: 20 C3 70      JSR   $70C3               ; 
A8C8: 85 03         STA   <$03                ; 
A8CA: A5 0A         LDA   <$0A                ; 
A8CC: 85 0B         STA   <$0B                ; 
A8CE: 68            PLA                       ;
A8CF: A8            TAY                       ;
A8D0: A9 08         LDA   #$08                ;
A8D2: 85 0A         STA   <$0A                ; 
A8D4: B9 84 00      LDA   $0084,Y             ;
A8D7: B4 84         LDY   $84,X               ;
A8D9: 20 C3 70      JSR   $70C3               ; 
A8DC: 85 04         STA   <$04                ; 
A8DE: 60            RTS                       ;
A8DF: 84 00         STY   <$00                ; 
A8E1: A9 FF         LDA   #$FF                ;
A8E3: 85 01         STA   <$01                ; 
A8E5: A5 03         LDA   <$03                ; 
A8E7: C5 04         CMP   <$04                ; 
A8E9: B0 0C         BCS   $A8F7               ; 
A8EB: 48            PHA                       ;
A8EC: A5 04         LDA   <$04                ; 
A8EE: 85 03         STA   <$03                ; 
A8F0: 68            PLA                       ;
A8F1: 85 04         STA   <$04                ; 
A8F3: A9 01         LDA   #$01                ;
A8F5: 85 01         STA   <$01                ; 
A8F7: A5 03         LDA   <$03                ; 
A8F9: 38            SEC                       ;
A8FA: E5 04         SBC   <$04                ; 
A8FC: C9 08         CMP   #$08                ;
A8FE: 90 18         BCC   $A918               ; 
A900: A5 00         LDA   <$00                ; 
A902: 18            CLC                       ;
A903: 65 01         ADC   <$01                ; 
A905: 85 00         STA   <$00                ; 
A907: F0 0F         BEQ   $A918               ; 
A909: C9 08         CMP   #$08                ;
A90B: F0 0B         BEQ   $A918               ; 
A90D: A5 03         LDA   <$03                ; 
A90F: 38            SEC                       ;
A910: E5 04         SBC   <$04                ; 
A912: 85 03         STA   <$03                ; 
A914: C5 04         CMP   <$04                ; 
A916: B0 E8         BCS   $A900               ; 
A918: A4 00         LDY   <$00                ; 
A91A: 60            RTS                       ;
A91B: 9D BC 03      STA   $03BC,X             ;
A91E: B5 AC         LDA   $AC,X               ;
A920: 29 F0         AND   #$F0                ;
A922: C9 40         CMP   #$40                ;
A924: D0 0C         BNE   $A932               ; 
A926: 5E BC 03      LSR   $03BC,X             ;
A929: DE 80 03      DEC   $0380,X             ;
A92C: D0 04         BNE   $A932               ; 
A92E: A9 50         LDA   #$50                ;
A930: 95 AC         STA   $AC,X               ;
A932: 60            RTS                       ;
A933: 85 01         STA   <$01                ; 
A935: 84 02         STY   <$02                ; 
A937: C4 01         CPY   <$01                ; 
A939: B0 06         BCS   $A941               ; 
A93B: 85 02         STA   <$02                ; 
A93D: 84 01         STY   <$01                ; 
A93F: 46 0A         LSR   <$0A                ; 
A941: A5 02         LDA   <$02                ; 
A943: 38            SEC                       ;
A944: E5 01         SBC   <$01                ; 
A946: C9 09         CMP   #$09                ;
A948: B0 02         BCS   $A94C               ; 
A94A: E6 00         INC   <$00                ; 
A94C: 60            RTS                       ;
A94D: AD 58 06      LDA   $0658               ; 
A950: F0 FA         BEQ   $A94C               ; 
A952: A2 10         LDX   #$10                ;
A954: B5 AC         LDA   $AC,X               ;
A956: F0 11         BEQ   $A969               ; 
A958: 29 F0         AND   #$F0                ;
A95A: C9 10         CMP   #$10                ;
A95C: D0 0B         BNE   $A969               ; 
A95E: E8            INX                       ;
A95F: B5 AC         LDA   $AC,X               ;
A961: F0 06         BEQ   $A969               ; 
A963: 29 F0         AND   #$F0                ;
A965: C9 10         CMP   #$10                ;
A967: F0 42         BEQ   $A9AB               ; 
A969: 8A            TXA                       ;
A96A: 49 01         EOR   #$01                ;
A96C: A8            TAY                       ;
A96D: B9 AC 00      LDA   $00AC,Y             ;
A970: F0 04         BEQ   $A976               ; 
A972: C9 13         CMP   #$13                ;
A974: 90 35         BCC   $A9AB               ; 
A976: CE 58 06      DEC   $0658               ; 
A979: A9 20         LDA   #$20                ;
A97B: 8D 04 06      STA   $0604               ; 
A97E: A9 00         LDA   #$00                ;
A980: 95 28         STA   $28,X               ;
A982: A9 11         LDA   #$11                ;
A984: 95 AC         STA   $AC,X               ;
A986: A9 01         LDA   #$01                ;
A988: 8D D0 03      STA   $03D0               ; 
A98B: A9 10         LDA   #$10                ;
A98D: 85 AC         STA   <$AC                ; 
A98F: A0 F0         LDY   #$F0                ;
A991: 85 01         STA   <$01                ; 
A993: 84 02         STY   <$02                ; 
A995: A5 98         LDA   <$98                ; 
A997: 95 98         STA   $98,X               ;
A999: 20 3C 71      JSR   $713C               ; 
A99C: 65 70         ADC   <$70                ; 
A99E: 95 70         STA   $70,X               ;
A9A0: A5 98         LDA   <$98                ; 
A9A2: 4A            LSR   A                   ;
A9A3: 4A            LSR   A                   ;
A9A4: 20 3C 71      JSR   $713C               ; 
A9A7: 65 84         ADC   <$84                ; 
A9A9: 95 84         STA   $84,X               ;
A9AB: 60            RTS                       ;
A9AC: A0 00         LDY   #$00                ;
A9AE: 84 00         STY   <$00                ; 
A9B0: 29 03         AND   #$03                ;
A9B2: F0 06         BEQ   $A9BA               ; 
A9B4: C8            INY                       ;
A9B5: 29 01         AND   #$01                ;
A9B7: D0 01         BNE   $A9BA               ; 
A9B9: C8            INY                       ;
A9BA: B9 00 00      LDA   $0000,Y             ;
A9BD: 18            CLC                       ;
A9BE: 60            RTS                       ;
A9BF: A2 10         LDX   #$10                ;
A9C1: B5 AC         LDA   $AC,X               ;
A9C3: F0 05         BEQ   $A9CA               ; 
A9C5: E8            INX                       ;
A9C6: B5 AC         LDA   $AC,X               ;
A9C8: D0 F4         BNE   $A9BE               ; 
A9CA: AD 5B 06      LDA   $065B               ; 
A9CD: C9 01         CMP   #$01                ;
A9CF: D0 05         BNE   $A9D6               ; 
A9D1: AD 13 05      LDA   $0513               ; 
A9D4: D0 E8         BNE   $A9BE               ; 
A9D6: A9 01         LDA   #$01                ;
A9D8: 8D 13 05      STA   $0513               ; 
A9DB: A9 00         LDA   #$00                ;
A9DD: 9D 94 03      STA   $0394,X             ;
A9E0: 9D A8 03      STA   $03A8,X             ;
A9E3: A9 20         LDA   #$20                ;
A9E5: 9D BC 03      STA   $03BC,X             ;
A9E8: A9 21         LDA   #$21                ;
A9EA: 95 AC         STA   $AC,X               ;
A9EC: A9 04         LDA   #$04                ;
A9EE: 20 80 6D      JSR   $6D80               ; 
A9F1: A9 04         LDA   #$04                ;
A9F3: 9D D0 03      STA   $03D0,X             ;
A9F6: 20 1B 71      JSR   $711B               ; 
A9F9: 60            RTS                       ;
A9FA: A4 EB         LDY   <$EB                ; 
A9FC: B9 FE 6A      LDA   $6AFE,Y             ;
A9FF: 29 30         AND   #$30                ;
AA01: 4A            LSR   A                   ;
AA02: 4A            LSR   A                   ;
AA03: 4A            LSR   A                   ;
AA04: 4A            LSR   A                   ;
AA05: A8            TAY                       ;
AA06: B9 A7 6B      LDA   $6BA7,Y             ;
AA09: 48            PHA                       ;
AA0A: 29 0F         AND   #$0F                ;
AA0C: 0A            ASL   A                   ;
AA0D: 0A            ASL   A                   ;
AA0E: 0A            ASL   A                   ;
AA0F: 0A            ASL   A                   ;
AA10: A8            TAY                       ;
AA11: 68            PLA                       ;
AA12: 29 F0         AND   #$F0                ;
AA14: 60            RTS                       ;
AA15: 95 C0         STA   $C0,X               ;
AA17: 95 D3         STA   $D3,X               ;
AA19: 95 28         STA   $28,X               ;
AA1B: 95 AC         STA   $AC,X               ;
AA1D: 9D F0 04      STA   $04F0,X             ;
AA20: A9 FF         LDA   #$FF                ;
AA22: 9D 92 04      STA   $0492,X             ;
AA25: A9 01         LDA   #$01                ;
AA27: 9D 05 04      STA   $0405,X             ;
AA2A: 60            RTS                       ;
AA2B: B5 AC         LDA   $AC,X               ;
AA2D: C9 13         CMP   #$13                ;
AA2F: D0 1C         BNE   $AA4D               ; 
AA31: A5 FE         LDA   <$FE                ; 
AA33: 4A            LSR   A                   ;
AA34: B4 28         LDY   $28,X               ;
AA36: C0 16         CPY   #$16                ;
AA38: F0 04         BEQ   $AA3E               ; 
AA3A: C0 11         CPY   #$11                ;
AA3C: D0 04         BNE   $AA42               ; 
AA3E: 2A            ROL   A                   ;
AA3F: 4C DB 71      JMP   $71DB               ; 
AA42: C0 12         CPY   #$12                ;
AA44: F0 04         BEQ   $AA4A               ; 
AA46: C0 0D         CPY   #$0D                ;
AA48: D0 03         BNE   $AA4D               ; 
AA4A: 0A            ASL   A                   ;
AA4B: 85 FE         STA   <$FE                ; 
AA4D: 60            RTS                       ;
AA4E: A5 12         LDA   <$12                ; 
AA50: C9 09         CMP   #$09                ;
AA52: F0 5B         BEQ   $AAAF               ; 
AA54: AE 22 05      LDX   $0522               ; 
AA57: D0 56         BNE   $AAAF               ; 
AA59: A5 EB         LDA   <$EB                ; 
AA5B: A2 00         LDX   #$00                ;
AA5D: 48            PHA                       ;
AA5E: 29 70         AND   #$70                ;
AA60: 4A            LSR   A                   ;
AA61: 4A            LSR   A                   ;
AA62: 69 17         ADC   #$17                ;
AA64: 9D 54 02      STA   $0254,X             ;
AA67: A9 11         LDA   #$11                ;
AA69: A4 10         LDY   <$10                ; 
AA6B: F0 02         BEQ   $AA6F               ; 
AA6D: A9 12         LDA   #$12                ;
AA6F: 85 00         STA   <$00                ; 
AA71: 68            PLA                       ;
AA72: 29 0F         AND   #$0F                ;
AA74: C0 00         CPY   #$00                ;
AA76: F0 01         BEQ   $AA79               ; 
AA78: 0A            ASL   A                   ;
AA79: 0A            ASL   A                   ;
AA7A: 0A            ASL   A                   ;
AA7B: 65 00         ADC   <$00                ; 
AA7D: 6D AC 6B      ADC   $6BAC               ; 
AA80: 9D 57 02      STA   $0257,X             ;
AA83: A9 3E         LDA   #$3E                ;
AA85: 9D 55 02      STA   $0255,X             ;
AA88: A9 00         LDA   #$00                ;
AA8A: E0 00         CPX   #$00                ;
AA8C: F0 1E         BEQ   $AAAC               ; 
AA8E: A9 03         LDA   #$03                ;
AA90: 48            PHA                       ;
AA91: A4 10         LDY   <$10                ; 
AA93: C0 09         CPY   #$09                ;
AA95: F0 08         BEQ   $AA9F               ; 
AA97: AD 71 06      LDA   $0671               ; 
AA9A: 39 BD E6      AND   $E6BD,Y             ;
AA9D: D0 0C         BNE   $AAAB               ; 
AA9F: A5 15         LDA   <$15                ; 
AAA1: 29 1F         AND   #$1F                ;
AAA3: C9 10         CMP   #$10                ;
AAA5: B0 04         BCS   $AAAB               ; 
AAA7: 68            PLA                       ;
AAA8: A9 02         LDA   #$02                ;
AAAA: 48            PHA                       ;
AAAB: 68            PLA                       ;
AAAC: 9D 56 02      STA   $0256,X             ;
AAAF: 60            RTS                       ;
AAB0: 20 48 72      JSR   $7248               ; 
AAB3: A9 02         LDA   #$02                ;
AAB5: 4C AC BF      JMP   $BFAC               ; 
AAB8: A5 28         LDA   <$28                ; 
AABA: D0 27         BNE   $AAE3               ; 
AABC: A9 01         LDA   #$01                ;
AABE: 85 0A         STA   <$0A                ; 
AAC0: A6 0A         LDX   <$0A                ; 
AAC2: B5 7C         LDA   $7C,X               ;
AAC4: 85 E8         STA   <$E8                ; 
AAC6: A9 05         LDA   #$05                ;
AAC8: 20 AC BF      JSR   $BFAC               ; 
AACB: A9 0E         LDA   #$0E                ;
AACD: 20 98 BF      JSR   $BF98               ; 
AAD0: 20 DE A8      JSR   $A8DE               ; 
AAD3: C6 0A         DEC   <$0A                ; 
AAD5: 10 E9         BPL   $AAC0               ; 
AAD7: A9 FF         LDA   #$FF                ;
AAD9: 85 E8         STA   <$E8                ; 
AADB: A9 05         LDA   #$05                ;
AADD: 85 28         STA   <$28                ; 
AADF: C6 7C         DEC   <$7C                ; 
AAE1: E6 7D         INC   <$7D                ; 
AAE3: 60            RTS                       ;
AAE4: A9 01         LDA   #$01                ;
AAE6: 18            CLC                       ;
AAE7: 65 00         ADC   <$00                ; 
AAE9: 85 00         STA   <$00                ; 
AAEB: 90 02         BCC   $AAEF               ; 
AAED: E6 01         INC   <$01                ; 
AAEF: 60            RTS                       ;
AAF0: A9 01         LDA   #$01                ;
AAF2: 18            CLC                       ;
AAF3: 65 02         ADC   <$02                ; 
AAF5: 85 02         STA   <$02                ; 
AAF7: 90 02         BCC   $AAFB               ; 
AAF9: E6 03         INC   <$03                ; 
AAFB: 60            RTS                       ;
AAFC: A9 01         LDA   #$01                ;
AAFE: 18            CLC                       ;
AAFF: 65 04         ADC   <$04                ; 
AB01: 85 04         STA   <$04                ; 
AB03: 90 02         BCC   $AB07               ; 
AB05: E6 05         INC   <$05                ; 
AB07: 60            RTS                       ;
AB08: A5 04         LDA   <$04                ; 
AB0A: 38            SEC                       ;
AB0B: E9 01         SBC   #$01                ;
AB0D: 85 04         STA   <$04                ; 
AB0F: B0 02         BCS   $AB13               ; 
AB11: C6 05         DEC   <$05                ; 
AB13: 60            RTS                       ;
AB14: 01 00         ORA   ($00,X)             ;
AB16: 00            BRK                       ;
AB17: 00            BRK                       ;
AB18: 06 05         ASL   <$05                ; 
AB1A: 04                              ;
AB1B: 04                              ;
AB1C: 02                              ;
AB1D: 02                              ;
AB1E: 03                              ;
AB1F: 0D 09 0C      ORA   $0C09               ; 
AB22: 1B                              ;
AB23: 1C                              ;
AB24: 08            PHP                       ;
AB25: 0A            ASL   A                   ;
AB26: 0B                              ;
AB27: 0B                              ;
AB28: 0E 0F 10      ASL   $100F               ; 
AB2B: 11 16         ORA   ($16),Y             ;
AB2D: 17                              ;
AB2E: 18            CLC                       ;
AB2F: 1A                              ;
AB30: 1F                              ;
AB31: 1D 1E 07      ORA   $071E,X             ;
AB34: 07                              ;
AB35: 15 19         ORA   $19,X               ;
AB37: 14                              ;
AB38: 14                              ;
AB39: 21 22         AND   ($22,X)             ;
AB3B: 23                              ;
AB3C: 01 01         ORA   ($01,X)             ;
AB3E: 21 22         AND   ($22,X)             ;
AB40: 21 22         AND   ($22,X)             ;
AB42: 01 01         ORA   ($01,X)             ;
AB44: 01 01         ORA   ($01,X)             ;
AB46: 01 15         ORA   ($15,X)             ;
AB48: 01 01         ORA   ($01,X)             ;
AB4A: 21 22         AND   ($22,X)             ;
AB4C: 01 01         ORA   ($01,X)             ;
AB4E: 01 01         ORA   ($01,X)             ;
AB50: 11 11         ORA   ($11),Y             ;
AB52: 10 01         BPL   $AB55               ; 
AB54: 01 01         ORA   ($01,X)             ;
AB56: 01 11         ORA   ($11,X)             ;
AB58: 22                              ;
AB59: 01 10         ORA   ($10,X)             ;
AB5B: 12                              ;
AB5C: FF                              ;
AB5D: 01 FF         ORA   ($FF,X)             ;
AB5F: 00            BRK                       ;
AB60: 00            BRK                       ;
AB61: 02                              ;
AB62: 02                              ;
AB63: 00            BRK                       ;
AB64: 01 00         ORA   ($00,X)             ;
AB66: 02                              ;
AB67: 00            BRK                       ;
AB68: 00            BRK                       ;
AB69: 02                              ;
AB6A: 02                              ;
AB6B: 01 02         ORA   ($02,X)             ;
AB6D: 02                              ;
AB6E: 02                              ;
AB6F: 02                              ;
AB70: 02                              ;
AB71: 02                              ;
AB72: 02                              ;
AB73: 02                              ;
AB74: 02                              ;
AB75: 02                              ;
AB76: 02                              ;
AB77: 02                              ;
AB78: 01 00         ORA   ($00,X)             ;
AB7A: 01 00         ORA   ($00,X)             ;
AB7C: 20 CE E6      JSR   $E6CE               ; 
AB7F: 09 10         ORA   #$10                ;
AB81: 91 00         STA   ($00),Y             ;
AB83: 60            RTS                       ;
AB84: AD AF 6B      LDA   $6BAF               ; 
AB87: 85 08         STA   <$08                ; 
AB89: AD B0 6B      LDA   $6BB0               ; 
AB8C: 85 09         STA   <$09                ; 
AB8E: A4 EB         LDY   <$EB                ; 
AB90: B1 08         LDA   ($08),Y             ;
AB92: 29 10         AND   #$10                ;
AB94: 60            RTS                       ;
AB95: 29 32         AND   #$32                ;
AB97: 16 A5         ASL   $A5,X               ;
AB99: AC 29 C0      LDY   $C029               ; 
AB9C: C9 40         CMP   #$40                ;
AB9E: F0 F4         BEQ   $AB94               ; 
ABA0: 20 14 73      JSR   $7314               ; 
ABA3: D0 EF         BNE   $AB94               ; 
ABA5: A2 13         LDX   #$13                ;
ABA7: B5 AC         LDA   $AC,X               ;
ABA9: 30 E9         BMI   $AB94               ; 
ABAB: B5 98         LDA   $98,X               ;
ABAD: 85 04         STA   <$04                ; 
ABAF: BD A8 03      LDA   $03A8,X             ;
ABB2: C9 F0         CMP   #$F0                ;
ABB4: B0 72         BCS   $AC28               ; 
ABB6: A5 84         LDA   <$84                ; 
ABB8: 18            CLC                       ;
ABB9: 69 03         ADC   #$03                ;
ABBB: 38            SEC                       ;
ABBC: F5 84         SBC   $84,X               ;
ABBE: 20 1F 70      JSR   $701F               ; 
ABC1: C9 09         CMP   #$09                ;
ABC3: B0 63         BCS   $AC28               ; 
ABC5: A5 70         LDA   <$70                ; 
ABC7: 38            SEC                       ;
ABC8: F5 70         SBC   $70,X               ;
ABCA: 20 1F 70      JSR   $701F               ; 
ABCD: C9 09         CMP   #$09                ;
ABCF: B0 57         BCS   $AC28               ; 
ABD1: A9 FF         LDA   #$FF                ;
ABD3: 95 AC         STA   $AC,X               ;
ABD5: 95 84         STA   $84,X               ;
ABD7: E0 13         CPX   #$13                ;
ABD9: D0 03         BNE   $ABDE               ; 
ABDB: 20 0C 73      JSR   $730C               ; 
ABDE: A5 04         LDA   <$04                ; 
ABE0: A2 08         LDX   #$08                ;
ABE2: 8E 02 06      STX   $0602               ; 
ABE5: C9 0E         CMP   #$0E                ;
ABE7: D0 05         BNE   $ABEE               ; 
ABE9: A2 02         LDX   #$02                ;
ABEB: 8E 02 06      STX   $0602               ; 
ABEE: A6 12         LDX   <$12                ; 
ABF0: E0 05         CPX   #$05                ;
ABF2: F0 0D         BEQ   $AC01               ; 
ABF4: A2 80         LDX   #$80                ;
ABF6: 8E 06 05      STX   $0506               ; 
ABF9: A2 08         LDX   #$08                ;
ABFB: 8E 00 06      STX   $0600               ; 
ABFE: 8D 05 05      STA   $0505               ; 
AC01: AA            TAX                       ;
AC02: BD A4 72      LDA   $72A4,X             ;
AC05: A8            TAY                       ;
AC06: BD C8 72      LDA   $72C8,X             ;
AC09: 48            PHA                       ;
AC0A: 29 0F         AND   #$0F                ;
AC0C: 85 0A         STA   <$0A                ; 
AC0E: 68            PLA                       ;
AC0F: 29 F0         AND   #$F0                ;
AC11: D0 1F         BNE   $AC32               ; 
AC13: C0 11         CPY   #$11                ;
AC15: F0 72         BEQ   $AC89               ; 
AC17: C0 10         CPY   #$10                ;
AC19: F0 6E         BEQ   $AC89               ; 
AC1B: C0 1A         CPY   #$1A                ;
AC1D: F0 6A         BEQ   $AC89               ; 
AC1F: C0 1B         CPY   #$1B                ;
AC21: F0 66         BEQ   $AC89               ; 
AC23: A5 0A         LDA   <$0A                ; 
AC25: 99 57 06      STA   $0657,Y             ;
AC28: 60            RTS                       ;
AC29: A0 04         LDY   #$04                ;
AC2B: 20 A3 74      JSR   $74A3               ; 
AC2E: 88            DEY                       ;
AC2F: 10 FA         BPL   $AC2B               ; 
AC31: 60            RTS                       ;
AC32: C9 10         CMP   #$10                ;
AC34: D0 4D         BNE   $AC83               ; 
AC36: C0 18         CPY   #$18                ;
AC38: F0 3A         BEQ   $AC74               ; 
AC3A: C0 1C         CPY   #$1C                ;
AC3C: F0 EB         BEQ   $AC29               ; 
AC3E: C0 16         CPY   #$16                ;
AC40: F0 3E         BEQ   $AC80               ; 
AC42: C0 19         CPY   #$19                ;
AC44: F0 75         BEQ   $ACBB               ; 
AC46: C0 17         CPY   #$17                ;
AC48: D0 03         BNE   $AC4D               ; 
AC4A: 20 AC 74      JSR   $74AC               ; 
AC4D: C0 14         CPY   #$14                ;
AC4F: F0 6D         BEQ   $ACBE               ; 
AC51: A5 0A         LDA   <$0A                ; 
AC53: 18            CLC                       ;
AC54: 79 57 06      ADC   $0657,Y             ;
AC57: 90 02         BCC   $AC5B               ; 
AC59: A9 FF         LDA   #$FF                ;
AC5B: C0 07         CPY   #$07                ;
AC5D: D0 06         BNE   $AC65               ; 
AC5F: C9 03         CMP   #$03                ;
AC61: 90 02         BCC   $AC65               ; 
AC63: A9 02         LDA   #$02                ;
AC65: C0 01         CPY   #$01                ;
AC67: D0 08         BNE   $AC71               ; 
AC69: CD 7C 06      CMP   $067C               ; 
AC6C: 90 03         BCC   $AC71               ; 
AC6E: AD 7C 06      LDA   $067C               ; 
AC71: 4C B5 73      JMP   $73B5               ; 
AC74: B9 57 06      LDA   $0657,Y             ;
AC77: C9 F0         CMP   #$F0                ;
AC79: B0 AD         BCS   $AC28               ; 
AC7B: 69 11         ADC   #$11                ;
AC7D: 4C B5 73      JMP   $73B5               ; 
AC80: 4C A3 74      JMP   $74A3               ; 
AC83: C9 20         CMP   #$20                ;
AC85: D0 D2         BNE   $AC59               ; 
AC87: F0 6B         BEQ   $ACF4               ; 
AC89: A5 10         LDA   <$10                ; 
AC8B: F0 2D         BEQ   $ACBA               ; 
AC8D: C0 1B         CPY   #$1B                ;
AC8F: F0 5B         BEQ   $ACEC               ; 
AC91: C0 11         CPY   #$11                ;
AC93: D0 05         BNE   $AC9A               ; 
AC95: A2 01         LDX   #$01                ;
AC97: 8E E5 04      STX   $04E5               ; 
AC9A: 38            SEC                       ;
AC9B: E9 01         SBC   #$01                ;
AC9D: C9 08         CMP   #$08                ;
AC9F: 90 02         BCC   $ACA3               ; 
ACA1: C8            INY                       ;
ACA2: C8            INY                       ;
ACA3: 29 07         AND   #$07                ;
ACA5: AA            TAX                       ;
ACA6: B9 57 06      LDA   $0657,Y             ;
ACA9: 1D BE E6      ORA   $E6BE,X             ;
ACAC: 99 57 06      STA   $0657,Y             ;
ACAF: C0 1A         CPY   #$1A                ;
ACB1: D0 07         BNE   $ACBA               ; 
ACB3: 20 A3 EB      JSR   $EBA3               ; 
ACB6: A9 12         LDA   #$12                ;
ACB8: 85 12         STA   <$12                ; 
ACBA: 60            RTS                       ;
ACBB: 20 AC 74      JSR   $74AC               ; 
ACBE: A5 0A         LDA   <$0A                ; 
ACC0: 85 01         STA   <$01                ; 
ACC2: 20 6C 74      JSR   $746C               ; 
ACC5: D0 07         BNE   $ACCE               ; 
ACC7: AE 70 06      LDX   $0670               ; 
ACCA: E8            INX                       ;
ACCB: D0 09         BNE   $ACD6               ; 
ACCD: 60            RTS                       ;
ACCE: EE 6F 06      INC   $066F               ; 
ACD1: C6 01         DEC   <$01                ; 
ACD3: 10 ED         BPL   $ACC2               ; 
ACD5: 60            RTS                       ;
ACD6: A9 FF         LDA   #$FF                ;
ACD8: 8D 70 06      STA   $0670               ; 
ACDB: 60            RTS                       ;
ACDC: AD 6F 06      LDA   $066F               ; 
ACDF: 48            PHA                       ;
ACE0: 29 0F         AND   #$0F                ;
ACE2: 85 00         STA   <$00                ; 
ACE4: 68            PLA                       ;
ACE5: 4A            LSR   A                   ;
ACE6: 4A            LSR   A                   ;
ACE7: 4A            LSR   A                   ;
ACE8: 4A            LSR   A                   ;
ACE9: C5 00         CMP   <$00                ; 
ACEB: 60            RTS                       ;
ACEC: A9 01         LDA   #$01                ;
ACEE: 20 AC BF      JSR   $BFAC               ; 
ACF1: 4C B1 A1      JMP   $A1B1               ; 
ACF4: A5 0A         LDA   <$0A                ; 
ACF6: D9 57 06      CMP   $0657,Y             ;
ACF9: 90 20         BCC   $AD1B               ; 
ACFB: 99 57 06      STA   $0657,Y             ;
ACFE: C0 0B         CPY   #$0B                ;
AD00: D0 19         BNE   $AD1B               ; 
AD02: A6 16         LDX   <$16                ; 
AD04: AC 62 06      LDY   $0662               ; 
AD07: B9 25 73      LDA   $7325,Y             ;
AD0A: BC 0E EA      LDY   $EA0E,X             ;
AD0D: 99 04 68      STA   $6804,Y             ;
AD10: 4C 2B EA      JMP   $EA2B               ; 
AD13: A9 01         LDA   #$01                ;
AD15: 8D 02 06      STA   $0602               ; 
AD18: EE 7D 06      INC   $067D               ; 
AD1B: 60            RTS                       ;
AD1C: A9 00         LDA   #$00                ;
AD1E: 8D 02 06      STA   $0602               ; 
AD21: A9 08         LDA   #$08                ;
AD23: 8D 04 06      STA   $0604               ; 
AD26: 60            RTS                       ;
AD27: A5 34         LDA   <$34                ; 
AD29: D0 4B         BNE   $AD76               ; 
AD2B: AD 1C 05      LDA   $051C               ; 
AD2E: 10 02         BPL   $AD32               ; 
AD30: 49 83         EOR   #$83                ;
AD32: 85 00         STA   <$00                ; 
AD34: 0A            ASL   A                   ;
AD35: 0A            ASL   A                   ;
AD36: 0A            ASL   A                   ;
AD37: 18            CLC                       ;
AD38: 65 00         ADC   <$00                ; 
AD3A: 29 FC         AND   #$FC                ;
AD3C: A8            TAY                       ;
AD3D: AE 01 03      LDX   $0301               ; 
AD40: A9 3F         LDA   #$3F                ;
AD42: 9D 02 03      STA   $0302,X             ;
AD45: E8            INX                       ;
AD46: A9 08         LDA   #$08                ;
AD48: 9D 02 03      STA   $0302,X             ;
AD4B: E8            INX                       ;
AD4C: 9D 02 03      STA   $0302,X             ;
AD4F: 85 00         STA   <$00                ; 
AD51: E8            INX                       ;
AD52: B9 FA 6B      LDA   $6BFA,Y             ;
AD55: 9D 02 03      STA   $0302,X             ;
AD58: C8            INY                       ;
AD59: E8            INX                       ;
AD5A: C6 00         DEC   <$00                ; 
AD5C: D0 F4         BNE   $AD52               ; 
AD5E: A9 FF         LDA   #$FF                ;
AD60: 9D 02 03      STA   $0302,X             ;
AD63: 8E 01 03      STX   $0301               ; 
AD66: EE 1C 05      INC   $051C               ; 
AD69: AD 1C 05      LDA   $051C               ; 
AD6C: 29 0F         AND   #$0F                ;
AD6E: C9 04         CMP   #$04                ;
AD70: F0 05         BEQ   $AD77               ; 
AD72: A9 0A         LDA   #$0A                ;
AD74: 85 34         STA   <$34                ; 
AD76: 60            RTS                       ;
AD77: A9 00         LDA   #$00                ;
AD79: 60            RTS                       ;
AD7A: 3D 1C 20      AND   $201C,X             ;
AD7D: 00            BRK                       ;
AD7E: DD 1C 20      CMP   $201C,X             ;
AD81: 00            BRK                       ;
AD82: A0 00         LDY   #$00                ;
AD84: A2 00         LDX   #$00                ;
AD86: BD 0A 75      LDA   $750A,X             ;
AD89: 99 00 02      STA   $0200,Y             ;
AD8C: E8            INX                       ;
AD8D: 8A            TXA                       ;
AD8E: 29 07         AND   #$07                ;
AD90: AA            TAX                       ;
AD91: C8            INY                       ;
AD92: C0 40         CPY   #$40                ;
AD94: D0 F0         BNE   $AD86               ; 
AD96: 60            RTS                       ;
AD97: 08            PHP                       ;
AD98: 02                              ;
AD99: 04                              ;
AD9A: 02                              ;
AD9B: 08            PHP                       ;
AD9C: 08            PHP                       ;
AD9D: 08            PHP                       ;
AD9E: 08            PHP                       ;
AD9F: AE 2F 05      LDX   $052F               ; 
ADA2: A5 98         LDA   <$98                ; 
ADA4: A4 EB         LDY   <$EB                ; 
ADA6: C0 61         CPY   #$61                ;
ADA8: D0 1E         BNE   $ADC8               ; 
ADAA: DD 27 75      CMP   $7527,X             ;
ADAD: D0 10         BNE   $ADBF               ; 
ADAF: E0 03         CPX   #$03                ;
ADB1: F0 27         BEQ   $ADDA               ; 
ADB3: EE 2F 05      INC   $052F               ; 
ADB6: 84 EC         STY   <$EC                ; 
ADB8: 60            RTS                       ;
ADB9: A9 00         LDA   #$00                ;
ADBB: 8D 2F 05      STA   $052F               ; 
ADBE: 60            RTS                       ;
ADBF: C9 01         CMP   #$01                ;
ADC1: F0 F5         BEQ   $ADB8               ; 
ADC3: 20 49 75      JSR   $7549               ; 
ADC6: F0 EE         BEQ   $ADB6               ; 
ADC8: C0 1B         CPY   #$1B                ;
ADCA: D0 ED         BNE   $ADB9               ; 
ADCC: DD 2B 75      CMP   $752B,X             ;
ADCF: F0 05         BEQ   $ADD6               ; 
ADD1: C9 02         CMP   #$02                ;
ADD3: D0 EE         BNE   $ADC3               ; 
ADD5: 60            RTS                       ;
ADD6: E0 03         CPX   #$03                ;
ADD8: D0 D9         BNE   $ADB3               ; 
ADDA: A9 04         LDA   #$04                ;
ADDC: 8D 02 06      STA   $0602               ; 
ADDF: 60            RTS                       ;
ADE0: A9 08         LDA   #$08                ;
ADE2: 85 00         STA   <$00                ; 
ADE4: A5 02         LDA   <$02                ; 
ADE6: 0A            ASL   A                   ;
ADE7: 26 00         ROL   <$00                ; 
ADE9: 0A            ASL   A                   ;
ADEA: 26 00         ROL   <$00                ; 
ADEC: 29 E0         AND   #$E0                ;
ADEE: 85 01         STA   <$01                ; 
ADF0: A5 03         LDA   <$03                ; 
ADF2: 4A            LSR   A                   ;
ADF3: 4A            LSR   A                   ;
ADF4: 4A            LSR   A                   ;
ADF5: 05 01         ORA   <$01                ; 
ADF7: 85 01         STA   <$01                ; 
ADF9: 60            RTS                       ;
ADFA: FF                              ;
ADFB: FF                              ;
ADFC: FF                              ;
ADFD: FF                              ;
ADFE: FF                              ;
ADFF: FF                              ;
AE00: FF                              ;
AE01: FF                              ;
AE02: FF                              ;
AE03: FF                              ;
AE04: 00            BRK                       ;
AE05: 08            PHP                       ;
AE06: 0B                              ;
AE07: 0F                              ;
AE08: 13                              ;
AE09: 17                              ;
AE0A: 5C                              ;
AE0B: 60            RTS                       ;
AE0C: 1B                              ;
AE0D: 1B                              ;
AE0E: 21 21         AND   ($21,X)             ;
AE10: 64                              ;
AE11: 6A            ROR   A                   ;
AE12: 27                              ;
AE13: 29 2B         AND   #$2B                ;
AE15: 35 3F         AND   $3F,X               ;
AE17: 70 74         BVS   $AE8D               ; 
AE19: 76 76         ROR   <$76,X              ;
AE1B: 78            SEI                       ;
AE1C: 7A                              ;
AE1D: 7E 80 49      ROR   $4980,X             ;
AE20: 82                              ;
AE21: 84 86         STY   <$86                ; 
AE23: 4B                              ;
AE24: 4F                              ;
AE25: 4F                              ;
AE26: 51 51         EOR   ($51),Y             ;
AE28: 88            DEY                       ;
AE29: 8C 90 90      STY   $9090               ; 
AE2C: 92                              ;
AE2D: 94 96         STY   $96,X               ;
AE2F: 98            TYA                       ;
AE30: 99 99 99      STA   $9999,Y             ;
AE33: 53                              ;
AE34: 54                              ;
AE35: 9A            TXS                       ;
AE36: 9B                              ;
AE37: 9B                              ;
AE38: A5 A5         LDA   <$A5                ; 
AE3A: AB                              ;
AE3B: AB                              ;
AE3C: AC AE AE      LDY   $AEAE               ; 
AE3F: AF                              ;
AE40: AF                              ;
AE41: B2                              ;
AE42: B8            CLV                       ;
AE43: B8            CLV                       ;
AE44: 08            PHP                       ;
AE45: 08            PHP                       ;
AE46: C6 C6         DEC   <$C6                ; 
AE48: C6 C6         DEC   <$C6                ; 
AE4A: C6 C6         DEC   <$C6                ; 
AE4C: C8            INY                       ;
AE4D: C8            INY                       ;
AE4E: C9 C9         CMP   #$C9                ;
AE50: CA            DEX                       ;
AE51: CA            DEX                       ;
AE52: CA            DEX                       ;
AE53: CA            DEX                       ;
AE54: CA            DEX                       ;
AE55: CA            DEX                       ;
AE56: CA            DEX                       ;
AE57: CA            DEX                       ;
AE58: 09 09         ORA   #$09                ;
AE5A: 0A            ASL   A                   ;
AE5B: 0A            ASL   A                   ;
AE5C: 0B                              ;
AE5D: 0B                              ;
AE5E: 0B                              ;
AE5F: 0B                              ;
AE60: 0B                              ;
AE61: 0B                              ;
AE62: CB                              ;
AE63: 55 55         EOR   $55,X               ;
AE65: 55 55         EOR   $55,X               ;
AE67: 55 55         EOR   $55,X               ;
AE69: 55 56         EOR   $56,X               ;
AE6B: 57                              ;
AE6C: 57                              ;
AE6D: CB                              ;
AE6E: CC 58 58      CPY   $5858               ; 
AE71: 58            CLI                       ;
AE72: 58            CLI                       ;
AE73: 58            CLI                       ;
AE74: 58            CLI                       ;
AE75: 58            CLI                       ;
AE76: 58            CLI                       ;
AE77: 58            CLI                       ;
AE78: 59 59 59      EOR   $5959,Y             ;
AE7B: 59 5A 5A      EOR   $5A5A,Y             ;
AE7E: 5A                              ;
AE7F: 5A                              ;
AE80: 5B                              ;
AE81: 5B                              ;
AE82: 5B                              ;
AE83: 00            BRK                       ;
AE84: 04                              ;
AE85: 08            PHP                       ;
AE86: 0C                              ;
AE87: 10 10         BPL   $AE99               ; 
AE89: 14                              ;
AE8A: 18            CLC                       ;
AE8B: 5C                              ;
AE8C: 9E                              ;
AE8D: 44                              ;
AE8E: CE D2 D6      DEC   $D6D2               ; 
AE91: DA                              ;
AE92: CE D2 D6      DEC   $D6D2               ; 
AE95: DA                              ;
AE96: F0 F4         BEQ   $AE8C               ; 
AE98: F8            SED                       ;
AE99: FC                              ;
AE9A: F0 F4         BEQ   $AE90               ; 
AE9C: F8            SED                       ;
AE9D: FC                              ;
AE9E: B4 B0         LDY   $B0,X               ;
AEA0: B0 B8         BCS   $AE5A               ; 
AEA2: B2                              ;
AEA3: B2                              ;
AEA4: B4 B0         LDY   $B0,X               ;
AEA6: B0 B8         BCS   $AE60               ; 
AEA8: B2                              ;
AEA9: B2                              ;
AEAA: CA            DEX                       ;
AEAB: CC CA CC      CPY   $CCCA               ; 
AEAE: BC BE C0      LDY   $C0BE,X             ;
AEB1: C0 C2         CPY   #$C2                ;
AEB3: C4 C0         CPY   <$C0                ; 
AEB5: C0 BC         CPY   #$BC                ;
AEB7: BE BC BE      LDX   $BEBC,Y             ;
AEBA: C0 C0         CPY   #$C0                ;
AEBC: C2                              ;
AEBD: C4 C0         CPY   <$C0                ; 
AEBF: C0 BC         CPY   #$BC                ;
AEC1: BE BC BE      LDX   $BEBC,Y             ;
AEC4: EC EE EC      CPX   $ECEE               ; 
AEC7: EE EC EE      INC   $EEEC               ; 
AECA: BC BE C6      LDY   $C6BE,X             ;
AECD: C8            INY                       ;
AECE: A0 A8         LDY   #$A8                ;
AED0: A4 AC         LDY   <$AC                ; 
AED2: 90 E8         BCC   $AEBC               ; 
AED4: E4 E0         CPX   <$E0                ; 
AED6: 94 F3         STY   $F3,X               ;
AED8: C9 BD         CMP   #$BD                ;
AEDA: C1 98         CMP   ($98,X)             ;
AEDC: 9A            TXS                       ;
AEDD: 9C                              ;
AEDE: F8            SED                       ;
AEDF: B8            CLV                       ;
AEE0: BC B0 B4      LDY   $B4B0,X             ;
AEE3: B8            CLV                       ;
AEE4: BC B0 B4      LDY   $B4B0,X             ;
AEE7: B8            CLV                       ;
AEE8: AC B4 BC      LDY   $BCB4               ; 
AEEB: B0 B4         BCS   $AEA1               ; 
AEED: B8            CLV                       ;
AEEE: AC B4 BC      LDY   $BCB4               ; 
AEF1: B0 B4         BCS   $AEA7               ; 
AEF3: AC AE B0      LDY   $B0AE               ; 
AEF6: B2                              ;
AEF7: A8            TAY                       ;
AEF8: AA            TAX                       ;
AEF9: 92                              ;
AEFA: 94 A0         STY   $A0,X               ;
AEFC: A2 A6         LDX   #$A6                ;
AEFE: A4 A2         LDY   <$A2                ; 
AF00: A4 D8         LDY   <$D8                ; 
AF02: DA                              ;
AF03: 00            BRK                       ;
AF04: 00            BRK                       ;
AF05: 9A            TXS                       ;
AF06: 9C                              ;
AF07: 9A            TXS                       ;
AF08: 9C                              ;
AF09: 9A            TXS                       ;
AF0A: 9C                              ;
AF0B: B4 B8         LDY   $B8,X               ;
AF0D: BC BE B4      LDY   $B4BE,X             ;
AF10: B8            CLV                       ;
AF11: BC BE FC      LDY   $FCBE,X             ;
AF14: FE AC 9C      INC   $9CAC,X             ;
AF17: A0 A4         LDY   #$A4                ;
AF19: A0 A4         LDY   #$A4                ;
AF1B: A8            TAY                       ;
AF1C: 8E A4 DC      STX   $DCA4               ; 
AF1F: E0 E4         CPX   #$E4                ;
AF21: E8            INX                       ;
AF22: EC F0 F4      CPX   $F4F0               ; 
AF25: F8            SED                       ;
AF26: FA                              ;
AF27: FE F4 F6      INC   $F6F4,X             ;
AF2A: FE FC F0      INC   $F0FC,X             ;
AF2D: F8            SED                       ;
AF2E: B0 F6         BCS   $AF26               ; 
AF30: F0 D4         BEQ   $AF06               ; 
AF32: FC                              ;
AF33: FE F8 E8      INC   $E8F8,X             ;
AF36: EA            NOP                       ;
AF37: E0 E4         CPX   #$E4                ;
AF39: EC EC D0      CPX   $D0EC               ; 
AF3C: D4                              ;
AF3D: D8            CLD                       ;
AF3E: DC                              ;
AF3F: E0 E4         CPX   #$E4                ;
AF41: C0 C8         CPY   #$C8                ;
AF43: C4 CC         CPY   <$CC                ; 
AF45: E8            INX                       ;
AF46: EA            NOP                       ;
AF47: 72                              ;
AF48: 74                              ;
AF49: DE EE F8      DEC   $F8EE,X             ;
AF4C: 96 98         STX   $98,Y               ;
AF4E: B1 00         LDA   ($00),Y             ;
AF50: 00            BRK                       ;
AF51: 00            BRK                       ;
AF52: 00            BRK                       ;
AF53: 00            BRK                       ;
AF54: 00            BRK                       ;
AF55: 00            BRK                       ;
AF56: 00            BRK                       ;
AF57: 02                              ;
AF58: 00            BRK                       ;
AF59: 00            BRK                       ;
AF5A: 01 01         ORA   ($01,X)             ;
AF5C: 01 01         ORA   ($01,X)             ;
AF5E: 02                              ;
AF5F: 02                              ;
AF60: 02                              ;
AF61: 02                              ;
AF62: 03                              ;
AF63: 03                              ;
AF64: 03                              ;
AF65: 03                              ;
AF66: 02                              ;
AF67: 02                              ;
AF68: 02                              ;
AF69: 02                              ;
AF6A: 02                              ;
AF6B: 82                              ;
AF6C: 02                              ;
AF6D: 02                              ;
AF6E: 82                              ;
AF6F: 02                              ;
AF70: 01 81         ORA   ($81,X)             ;
AF72: 01 01         ORA   ($01,X)             ;
AF74: 81 01         STA   ($01,X)             ;
AF76: 01 01         ORA   ($01,X)             ;
AF78: 02                              ;
AF79: 02                              ;
AF7A: 02                              ;
AF7B: 02                              ;
AF7C: 01 01         ORA   ($01,X)             ;
AF7E: 01 01         ORA   ($01,X)             ;
AF80: 01 01         ORA   ($01,X)             ;
AF82: 02                              ;
AF83: 02                              ;
AF84: 02                              ;
AF85: 02                              ;
AF86: 02                              ;
AF87: 02                              ;
AF88: 02                              ;
AF89: 02                              ;
AF8A: 02                              ;
AF8B: 02                              ;
AF8C: 02                              ;
AF8D: 02                              ;
AF8E: 03                              ;
AF8F: 03                              ;
AF90: 03                              ;
AF91: 03                              ;
AF92: 03                              ;
AF93: 03                              ;
AF94: 03                              ;
AF95: 03                              ;
AF96: 03                              ;
AF97: 03                              ;
AF98: 02                              ;
AF99: 02                              ;
AF9A: 02                              ;
AF9B: 02                              ;
AF9C: 02                              ;
AF9D: 02                              ;
AF9E: 02                              ;
AF9F: 02                              ;
AFA0: 01 01         ORA   ($01,X)             ;
AFA2: 01 02         ORA   ($02,X)             ;
AFA4: 03                              ;
AFA5: 03                              ;
AFA6: 03                              ;
AFA7: 02                              ;
AFA8: 02                              ;
AFA9: 00            BRK                       ;
AFAA: 02                              ;
AFAB: 01 01         ORA   ($01,X)             ;
AFAD: 01 01         ORA   ($01,X)             ;
AFAF: 02                              ;
AFB0: 02                              ;
AFB1: 02                              ;
AFB2: 02                              ;
AFB3: 02                              ;
AFB4: 02                              ;
AFB5: 02                              ;
AFB6: 02                              ;
AFB7: 02                              ;
AFB8: 02                              ;
AFB9: 01 01         ORA   ($01,X)             ;
AFBB: 01 01         ORA   ($01,X)             ;
AFBD: 01 01         ORA   ($01,X)             ;
AFBF: 01 01         ORA   ($01,X)             ;
AFC1: 01 01         ORA   ($01,X)             ;
AFC3: 03                              ;
AFC4: 03                              ;
AFC5: 03                              ;
AFC6: 03                              ;
AFC7: 00            BRK                       ;
AFC8: 00            BRK                       ;
AFC9: 02                              ;
AFCA: 02                              ;
AFCB: 02                              ;
AFCC: 02                              ;
AFCD: 03                              ;
AFCE: 03                              ;
AFCF: 03                              ;
AFD0: 03                              ;
AFD1: 01 01         ORA   ($01,X)             ;
AFD3: 02                              ;
AFD4: 02                              ;
AFD5: 03                              ;
AFD6: 03                              ;
AFD7: 01 01         ORA   ($01,X)             ;
AFD9: 01 01         ORA   ($01,X)             ;
AFDB: 02                              ;
AFDC: 02                              ;
AFDD: 02                              ;
AFDE: 02                              ;
AFDF: 01 01         ORA   ($01,X)             ;
AFE1: 01 01         ORA   ($01,X)             ;
AFE3: 02                              ;
AFE4: 02                              ;
AFE5: 02                              ;
AFE6: 02                              ;
AFE7: 02                              ;
AFE8: 02                              ;
AFE9: 01 03         ORA   ($03,X)             ;
AFEB: 03                              ;
AFEC: 03                              ;
AFED: 03                              ;
AFEE: 03                              ;
AFEF: 03                              ;
AFF0: 03                              ;
AFF1: 03                              ;
AFF2: 03                              ;
AFF3: 03                              ;
AFF4: 01 01         ORA   ($01,X)             ;
AFF6: 01 01         ORA   ($01,X)             ;
AFF8: 01 01         ORA   ($01,X)             ;
AFFA: 02                              ;
AFFB: 00            BRK                       ;
AFFC: 00            BRK                       ;
AFFD: 03                              ;
AFFE: 01 01         ORA   ($01,X)             ;
B000: 01 01         ORA   ($01,X)             ;
B002: 01 01         ORA   ($01,X)             ;
B004: 01 01         ORA   ($01,X)             ;
B006: 01 03         ORA   ($03,X)             ;
B008: 03                              ;
B009: 03                              ;
B00A: 03                              ;
B00B: 03                              ;
B00C: 03                              ;
B00D: 03                              ;
B00E: 03                              ;
B00F: 03                              ;
B010: 03                              ;
B011: 03                              ;
B012: 03                              ;
B013: 03                              ;
B014: 03                              ;
B015: 02                              ;
B016: 02                              ;
B017: 01 01         ORA   ($01,X)             ;
B019: 02                              ;
B01A: 03                              ;
B01B: 60            RTS                       ;
B01C: BC 64 B8      LDY   $B864,X             ;
B01F: 68            PLA                       ;
B020: B4 6C         LDY   $6C,X               ;
B022: B0 70         BCS   $B094               ; 
B024: CC 74 C8      CPY   $C874               ; 
B027: 78            SEI                       ;
B028: C4 7C         CPY   <$7C                ; 
B02A: C0 80         CPY   #$80                ;
B02C: DC                              ;
B02D: 84 D8         STY   <$D8                ; 
B02F: 88            DEY                       ;
B030: D4                              ;
B031: 8C D0 90      STY   $90D0               ; 
B034: EC 94 E8      CPX   $E894               ; 
B037: 98            TYA                       ;
B038: E4 9C         CPX   <$9C                ; 
B03A: E0 A0         CPX   #$A0                ;
B03C: FC                              ;
B03D: A4 F8         LDY   <$F8                ; 
B03F: A8            TAY                       ;
B040: F4                              ;
B041: AC F0 60      LDY   $60F0               ; 
B044: 20 4F FA      JSR   $FA4F               ; 
B047: 98            TYA                       ;
B048: 4C DF 77      JMP   $77DF               ; 
B04B: A0 01         LDY   #$01                ;
B04D: D0 02         BNE   $B051               ; 
B04F: A0 00         LDY   #$00                ;
B051: 84 0C         STY   <$0C                ; 
B053: BC 4F 03      LDY   $034F,X             ;
B056: C8            INY                       ;
B057: 85 0D         STA   <$0D                ; 
B059: 84 0E         STY   <$0E                ; 
B05B: 86 08         STX   <$08                ; 
B05D: AC 41 03      LDY   $0341               ; 
B060: B9 AB 77      LDA   $77AB,Y             ;
B063: 8D 43 03      STA   $0343               ; 
B066: B9 AC 77      LDA   $77AC,Y             ;
B069: E0 00         CPX   #$00                ;
B06B: D0 07         BNE   $B074               ; 
B06D: A9 48         LDA   #$48                ;
B06F: 8D 43 03      STA   $0343               ; 
B072: A9 4C         LDA   #$4C                ;
B074: 8D 44 03      STA   $0344               ; 
B077: A4 0E         LDY   <$0E                ; 
B079: A9 01         LDA   #$01                ;
B07B: 85 07         STA   <$07                ; 
B07D: A9 08         LDA   #$08                ;
B07F: 85 0A         STA   <$0A                ; 
B081: B9 94 75      LDA   $7594,Y             ;
B084: 18            CLC                       ;
B085: 65 0D         ADC   <$0D                ; 
B087: A8            TAY                       ;
B088: B9 13 76      LDA   $7613,Y             ;
B08B: 85 02         STA   <$02                ; 
B08D: 18            CLC                       ;
B08E: 69 02         ADC   #$02                ;
B090: 85 03         STA   <$03                ; 
B092: E0 00         CPX   #$00                ;
B094: F0 12         BEQ   $B0A8               ; 
B096: E0 0D         CPX   #$0D                ;
B098: B0 0E         BCS   $B0A8               ; 
B09A: BD BF 04      LDA   $04BF,X             ;
B09D: 29 02         AND   #$02                ;
B09F: D0 18         BNE   $B0B9               ; 
B0A1: BD BF 04      LDA   $04BF,X             ;
B0A4: 29 08         AND   #$08                ;
B0A6: D0 06         BNE   $B0AE               ; 
B0A8: B9 DF 76      LDA   $76DF,Y             ;
B0AB: 20 88 79      JSR   $7988               ; 
B0AE: E0 00         CPX   #$00                ;
B0B0: F0 0C         BEQ   $B0BE               ; 
B0B2: A4 0C         LDY   <$0C                ; 
B0B4: F0 08         BEQ   $B0BE               ; 
B0B6: 4C 79 79      JMP   $7979               ; 
B0B9: C6 07         DEC   <$07                ; 
B0BB: 4C 68 78      JMP   $7868               ; 
B0BE: A5 0F         LDA   <$0F                ; 
B0C0: F0 16         BEQ   $B0D8               ; 
B0C2: A5 02         LDA   <$02                ; 
B0C4: 48            PHA                       ;
B0C5: A5 03         LDA   <$03                ; 
B0C7: 85 02         STA   <$02                ; 
B0C9: 68            PLA                       ;
B0CA: 85 03         STA   <$03                ; 
B0CC: A5 04         LDA   <$04                ; 
B0CE: 49 40         EOR   #$40                ;
B0D0: 85 04         STA   <$04                ; 
B0D2: A5 05         LDA   <$05                ; 
B0D4: 49 40         EOR   #$40                ;
B0D6: 85 05         STA   <$05                ; 
B0D8: BC F0 04      LDY   $04F0,X             ;
B0DB: F0 18         BEQ   $B0F5               ; 
B0DD: A0 01         LDY   #$01                ;
B0DF: B9 04 00      LDA   $0004,Y             ;
B0E2: 29 FC         AND   #$FC                ;
B0E4: 99 04 00      STA   $0004,Y             ;
B0E7: BD F0 04      LDA   $04F0,X             ;
B0EA: 29 03         AND   #$03                ;
B0EC: 19 04 00      ORA   $0004,Y             ;
B0EF: 99 04 00      STA   $0004,Y             ;
B0F2: 88            DEY                       ;
B0F3: 10 EA         BPL   $B0DF               ; 
B0F5: AE 43 03      LDX   $0343               ; 
B0F8: A0 00         LDY   #$00                ;
B0FA: B9 02 00      LDA   $0002,Y             ;
B0FD: 9D 01 02      STA   $0201,X             ;
B100: A5 01         LDA   <$01                ; 
B102: 9D 00 02      STA   $0200,X             ;
B105: A5 00         LDA   <$00                ; 
B107: 9D 03 02      STA   $0203,X             ;
B10A: 18            CLC                       ;
B10B: 65 0A         ADC   <$0A                ; 
B10D: 85 00         STA   <$00                ; 
B10F: B9 04 00      LDA   $0004,Y             ;
B112: 9D 02 02      STA   $0202,X             ;
B115: AE 44 03      LDX   $0344               ; 
B118: A5 08         LDA   <$08                ; 
B11A: F0 03         BEQ   $B11F               ; 
B11C: 20 36 6E      JSR   $6E36               ; 
B11F: C8            INY                       ;
B120: C6 07         DEC   <$07                ; 
B122: 10 D6         BPL   $B0FA               ; 
B124: A6 08         LDX   <$08                ; 
B126: 60            RTS                       ;
B127: 00            BRK                       ;
B128: 03                              ;
B129: 07                              ;
B12A: 0A            ASL   A                   ;
B12B: 0B                              ;
B12C: 0C                              ;
B12D: 0D 0E 0F      ORA   $0F0E               ; 
B130: 11 12         ORA   ($12),Y             ;
B132: 13                              ;
B133: 14                              ;
B134: 15 16         ORA   $16,X               ;
B136: 17                              ;
B137: 18            CLC                       ;
B138: 17                              ;
B139: 18            CLC                       ;
B13A: 17                              ;
B13B: 19 1B 1C      ORA   $1C1B,Y             ;
B13E: 1D 1E 1F      ORA   $1F1E,X             ;
B141: 20 21 1C      JSR   $1C21               ; 
B144: 22                              ;
B145: 22                              ;
B146: 26 27         ROL   <$27                ; 
B148: 28            PLP                       ;
B149: 29 2B         AND   #$2B                ;
B14B: 2E 20 82      ROL   $8220               ; 
B14E: 3C                              ;
B14F: 34                              ;
B150: 70 72         BVS   $B1C4               ; 
B152: 74                              ;
B153: 28            PLP                       ;
B154: 86 3C         STX   <$3C                ; 
B156: 2A            ROL   A                   ;
B157: 26 24         ROL   <$24                ; 
B159: 22                              ;
B15A: 40            RTI                       ;
B15B: 4A            LSR   A                   ;
B15C: 8A            TXA                       ;
B15D: 6C 42 46      JMP   ($4642)             ; 
B160: 76 2C         ROR   <$2C,X              ;
B162: 4E 4C 6A      LSR   $6A4C               ; 
B165: 50 52         BVC   $B1B9               ; 
B167: 66 32         ROR   <$32                ; 
B169: 2E 68 F3      ROL   $F368               ; 
B16C: 6E F2 36      ROR   $36F2               ; 
B16F: 38            SEC                       ;
B170: 3A                              ;
B171: 3C                              ;
B172: 56 48         LSR   $48,X               ;
B174: 78            SEI                       ;
B175: 20 82 7A      JSR   $7A82               ; 
B178: 7C                              ;
B179: 30 64         BMI   $B1DF               ; 
B17B: 62                              ;
B17C: 20 88 79      JSR   $7988               ; 
B17F: A9 00         LDA   #$00                ;
B181: 85 0F         STA   <$0F                ; 
B183: 85 0C         STA   <$0C                ; 
B185: 98            TYA                       ;
B186: 48            PHA                       ;
B187: A9 00         LDA   #$00                ;
B189: 85 52         STA   <$52                ; 
B18B: AC 41 03      LDY   $0341               ; 
B18E: B9 AB 77      LDA   $77AB,Y             ;
B191: 8D 43 03      STA   $0343               ; 
B194: B9 AC 77      LDA   $77AC,Y             ;
B197: 8D 44 03      STA   $0344               ; 
B19A: 68            PLA                       ;
B19B: A8            TAY                       ;
B19C: 86 08         STX   <$08                ; 
B19E: A9 01         LDA   #$01                ;
B1A0: 85 07         STA   <$07                ; 
B1A2: A9 08         LDA   #$08                ;
B1A4: 85 0A         STA   <$0A                ; 
B1A6: B9 B7 78      LDA   $78B7,Y             ;
B1A9: 18            CLC                       ;
B1AA: 65 0C         ADC   <$0C                ; 
B1AC: A8            TAY                       ;
B1AD: B9 DC 78      LDA   $78DC,Y             ;
B1B0: 85 02         STA   <$02                ; 
B1B2: 18            CLC                       ;
B1B3: 69 02         ADC   #$02                ;
B1B5: 85 03         STA   <$03                ; 
B1B7: A5 02         LDA   <$02                ; 
B1B9: C9 F3         CMP   #$F3                ;
B1BB: F0 08         BEQ   $B1C5               ; 
B1BD: C9 20         CMP   #$20                ;
B1BF: 90 19         BCC   $B1DA               ; 
B1C1: C9 62         CMP   #$62                ;
B1C3: B0 15         BCS   $B1DA               ; 
B1C5: AD 04 05      LDA   $0504               ; 
B1C8: D0 07         BNE   $B1D1               ; 
B1CA: A5 00         LDA   <$00                ; 
B1CC: 18            CLC                       ;
B1CD: 69 04         ADC   #$04                ;
B1CF: 85 00         STA   <$00                ; 
B1D1: E6 52         INC   <$52                ; 
B1D3: A9 00         LDA   #$00                ;
B1D5: 85 07         STA   <$07                ; 
B1D7: 4C 68 78      JMP   $7868               ; 
B1DA: C9 6C         CMP   #$6C                ;
B1DC: 90 07         BCC   $B1E5               ; 
B1DE: C9 7C         CMP   #$7C                ;
B1E0: 90 07         BCC   $B1E9               ; 
B1E2: 4C 4E 78      JMP   $784E               ; 
B1E5: A9 07         LDA   #$07                ;
B1E7: 85 0A         STA   <$0A                ; 
B1E9: A5 02         LDA   <$02                ; 
B1EB: 85 03         STA   <$03                ; 
B1ED: A5 05         LDA   <$05                ; 
B1EF: 49 40         EOR   #$40                ;
B1F1: 85 05         STA   <$05                ; 
B1F3: 4C 68 78      JMP   $7868               ; 
B1F6: A9 02         LDA   #$02                ;
B1F8: 85 04         STA   <$04                ; 
B1FA: 85 05         STA   <$05                ; 
B1FC: 60            RTS                       ;
B1FD: A0 03         LDY   #$03                ;
B1FF: 84 03         STY   <$03                ; 
B201: 48            PHA                       ;
B202: BD F0 04      LDA   $04F0,X             ;
B205: F0 06         BEQ   $B20D               ; 
B207: A5 15         LDA   <$15                ; 
B209: 29 03         AND   #$03                ;
B20B: 85 03         STA   <$03                ; 
B20D: AC 41 03      LDY   $0341               ; 
B210: B9 AB 77      LDA   $77AB,Y             ;
B213: A8            TAY                       ;
B214: 68            PLA                       ;
B215: 99 01 02      STA   $0201,Y             ;
B218: B5 70         LDA   $70,X               ;
B21A: 99 03 02      STA   $0203,Y             ;
B21D: B5 84         LDA   $84,X               ;
B21F: 99 00 02      STA   $0200,Y             ;
B222: A5 03         LDA   <$03                ; 
B224: 99 02 02      STA   $0202,Y             ;
B227: 4C 36 6E      JMP   $6E36               ; 
B22A: 20 D0 79      JSR   $79D0               ; 
B22D: AD 06 04      LDA   $0406               ; 
B230: F0 08         BEQ   $B23A               ; 
B232: 8D CC 04      STA   $04CC               ; 
B235: A9 00         LDA   #$00                ;
B237: 8D 06 04      STA   $0406               ; 
B23A: 20 93 FA      JSR   $FA93               ; 
B23D: 4C DB 77      JMP   $77DB               ; 
B240: 20 2D 7A      JSR   $7A2D               ; 
B243: BD BF 04      LDA   $04BF,X             ;
B246: 29 20         AND   #$20                ;
B248: D0 23         BNE   $B26D               ; 
B24A: BD F0 04      LDA   $04F0,X             ;
B24D: D0 3D         BNE   $B28C               ; 
B24F: A0 0F         LDY   #$0F                ;
B251: 20 C2 7B      JSR   $7BC2               ; 
B254: A0 0E         LDY   #$0E                ;
B256: 20 9D 7C      JSR   $7C9D               ; 
B259: A0 10         LDY   #$10                ;
B25B: 20 DC 7C      JSR   $7CDC               ; 
B25E: A0 11         LDY   #$11                ;
B260: 20 DC 7C      JSR   $7CDC               ; 
B263: A0 0D         LDY   #$0D                ;
B265: 20 29 7D      JSR   $7D29               ; 
B268: A0 12         LDY   #$12                ;
B26A: 20 5F 7D      JSR   $7D5F               ; 
B26D: 20 A7 7A      JSR   $7AA7               ; 
B270: BD 4F 03      LDA   $034F,X             ;
B273: BC 05 04      LDY   $0405,X             ;
B276: F0 15         BEQ   $B28D               ; 
B278: C9 05         CMP   #$05                ;
B27A: F0 04         BEQ   $B280               ; 
B27C: C9 06         CMP   #$06                ;
B27E: D0 0C         BNE   $B28C               ; 
B280: B5 AC         LDA   $AC,X               ;
B282: 10 08         BPL   $B28C               ; 
B284: BC 2C 04      LDY   $042C,X             ;
B287: A9 00         LDA   #$00                ;
B289: 99 4F 03      STA   $034F,Y             ;
B28C: 60            RTS                       ;
B28D: C9 27         CMP   #$27                ;
B28F: F0 04         BEQ   $B295               ; 
B291: C9 17         CMP   #$17                ;
B293: D0 07         BNE   $B29C               ; 
B295: A5 0C         LDA   <$0C                ; 
B297: F0 03         BEQ   $B29C               ; 
B299: FE 2C 04      INC   $042C,X             ;
B29C: 60            RTS                       ;
B29D: A9 08         LDA   #$08                ;
B29F: 85 02         STA   <$02                ; 
B2A1: 85 03         STA   <$03                ; 
B2A3: BD BF 04      LDA   $04BF,X             ;
B2A6: 29 40         AND   #$40                ;
B2A8: F0 02         BEQ   $B2AC               ; 
B2AA: 46 02         LSR   <$02                ; 
B2AC: B5 70         LDA   $70,X               ;
B2AE: 18            CLC                       ;
B2AF: 65 02         ADC   <$02                ; 
B2B1: 85 02         STA   <$02                ; 
B2B3: B5 84         LDA   $84,X               ;
B2B5: 18            CLC                       ;
B2B6: 65 03         ADC   <$03                ; 
B2B8: 85 03         STA   <$03                ; 
B2BA: 60            RTS                       ;
B2BB: 02                              ;
B2BC: 01 80         ORA   ($80,X)             ;
B2BE: 80                              ;
B2BF: 01 80         ORA   ($80,X)             ;
B2C1: 80                              ;
B2C2: 80                              ;
B2C3: 80                              ;
B2C4: 80                              ;
B2C5: 01 02         ORA   ($02,X)             ;
B2C7: 80                              ;
B2C8: 80                              ;
B2C9: 01 80         ORA   ($80,X)             ;
B2CB: 80                              ;
B2CC: 01 01         ORA   ($01,X)             ;
B2CE: 80                              ;
B2CF: 80                              ;
B2D0: 02                              ;
B2D1: 01 02         ORA   ($02,X)             ;
B2D3: 00            BRK                       ;
B2D4: 80                              ;
B2D5: 80                              ;
B2D6: 80                              ;
B2D7: 80                              ;
B2D8: 01 80         ORA   ($80,X)             ;
B2DA: 80                              ;
B2DB: 01 01         ORA   ($01,X)             ;
B2DD: 02                              ;
B2DE: 01 02         ORA   ($02,X)             ;
B2E0: 02                              ;
B2E1: 80                              ;
B2E2: 80                              ;
B2E3: 80                              ;
B2E4: 80                              ;
B2E5: 00            BRK                       ;
B2E6: 00            BRK                       ;
B2E7: 00            BRK                       ;
B2E8: 00            BRK                       ;
B2E9: 00            BRK                       ;
B2EA: 02                              ;
B2EB: 01 01         ORA   ($01,X)             ;
B2ED: 02                              ;
B2EE: 02                              ;
B2EF: 00            BRK                       ;
B2F0: 00            BRK                       ;
B2F1: 00            BRK                       ;
B2F2: 02                              ;
B2F3: 02                              ;
B2F4: 02                              ;
B2F5: 02                              ;
B2F6: 01 01         ORA   ($01,X)             ;
B2F8: 04                              ;
B2F9: 80                              ;
B2FA: 80                              ;
B2FB: 80                              ;
B2FC: 01 01         ORA   ($01,X)             ;
B2FE: 01 01         ORA   ($01,X)             ;
B300: 01 02         ORA   ($02,X)             ;
B302: 02                              ;
B303: 01 01         ORA   ($01,X)             ;
B305: 00            BRK                       ;
B306: 00            BRK                       ;
B307: 00            BRK                       ;
B308: 00            BRK                       ;
B309: 00            BRK                       ;
B30A: 00            BRK                       ;
B30B: 00            BRK                       ;
B30C: 00            BRK                       ;
B30D: 80                              ;
B30E: 80                              ;
B30F: 80                              ;
B310: 01 02         ORA   ($02,X)             ;
B312: 02                              ;
B313: 04                              ;
B314: 04                              ;
B315: 80                              ;
B316: 01 20         ORA   ($20,X)             ;
B318: 2D 7A A9      AND   $A97A               ; 
B31B: 00            BRK                       ;
B31C: 8D 4B 03      STA   $034B               ; 
B31F: 85 06         STA   <$06                ; 
B321: 85 09         STA   <$09                ; 
B323: 85 0C         STA   <$0C                ; 
B325: A0 00         LDY   #$00                ;
B327: 84 00         STY   <$00                ; 
B329: AD F0 04      LDA   $04F0               ; 
B32C: 0D 6C 06      ORA   $066C               ; 
B32F: 05 3D         ORA   <$3D                ; 
B331: 15 3D         ORA   $3D,X               ;
B333: D0 74         BNE   $B3A9               ; 
B335: A5 AC         LDA   <$AC                ; 
B337: C9 40         CMP   #$40                ;
B339: F0 6E         BEQ   $B3A9               ; 
B33B: AD 12 05      LDA   $0512               ; 
B33E: D0 69         BNE   $B3A9               ; 
B340: BD 4F 03      LDA   $034F,X             ;
B343: C9 53         CMP   #$53                ;
B345: 90 08         BCC   $B34F               ; 
B347: B5 AC         LDA   $AC,X               ;
B349: 29 F0         AND   #$F0                ;
B34B: C9 10         CMP   #$10                ;
B34D: D0 5A         BNE   $B3A9               ; 
B34F: A5 70         LDA   <$70                ; 
B351: 18            CLC                       ;
B352: 69 08         ADC   #$08                ;
B354: 85 04         STA   <$04                ; 
B356: A5 84         LDA   <$84                ; 
B358: 18            CLC                       ;
B359: 69 08         ADC   #$08                ;
B35B: 85 05         STA   <$05                ; 
B35D: A9 09         LDA   #$09                ;
B35F: 20 FB 7D      JSR   $7DFB               ; 
B362: F0 45         BEQ   $B3A9               ; 
B364: BD 4F 03      LDA   $034F,X             ;
B367: C9 53         CMP   #$53                ;
B369: 90 3F         BCC   $B3AA               ; 
B36B: EE 4B 03      INC   $034B               ; 
B36E: C9 56         CMP   #$56                ;
B370: F0 38         BEQ   $B3AA               ; 
B372: C9 5A         CMP   #$5A                ;
B374: F0 34         BEQ   $B3AA               ; 
B376: A5 AC         LDA   <$AC                ; 
B378: 29 F0         AND   #$F0                ;
B37A: D0 2E         BNE   $B3AA               ; 
B37C: A5 98         LDA   <$98                ; 
B37E: 15 98         ORA   $98,X               ;
B380: 29 0C         AND   #$0C                ;
B382: C9 0C         CMP   #$0C                ;
B384: F0 0A         BEQ   $B390               ; 
B386: A5 98         LDA   <$98                ; 
B388: 15 98         ORA   $98,X               ;
B38A: 29 03         AND   #$03                ;
B38C: C9 03         CMP   #$03                ;
B38E: D0 1A         BNE   $B3AA               ; 
B390: BD 4F 03      LDA   $034F,X             ;
B393: C9 55         CMP   #$55                ;
B395: 90 09         BCC   $B3A0               ; 
B397: C9 5B         CMP   #$5B                ;
B399: B0 05         BCS   $B3A0               ; 
B39B: AD 76 06      LDA   $0676               ; 
B39E: F0 0A         BEQ   $B3AA               ; 
B3A0: A9 01         LDA   #$01                ;
B3A2: 8D 04 06      STA   $0604               ; 
B3A5: A9 00         LDA   #$00                ;
B3A7: 85 06         STA   <$06                ; 
B3A9: 60            RTS                       ;
B3AA: 20 26 7E      JSR   $7E26               ; 
B3AD: E6 0C         INC   <$0C                ; 
B3AF: BC 4F 03      LDY   $034F,X             ;
B3B2: B9 4A 7A      LDA   $7A4A,Y             ;
B3B5: 48            PHA                       ;
B3B6: 29 0F         AND   #$0F                ;
B3B8: 85 0D         STA   <$0D                ; 
B3BA: 68            PLA                       ;
B3BB: 29 F0         AND   #$F0                ;
B3BD: 85 0E         STA   <$0E                ; 
B3BF: BC 4F 03      LDY   $034F,X             ;
B3C2: C0 2E         CPY   #$2E                ;
B3C4: F0 05         BEQ   $B3CB               ; 
B3C6: A9 08         LDA   #$08                ;
B3C8: 20 7C 6D      JSR   $6D7C               ; 
B3CB: AC 62 06      LDY   $0662               ; 
B3CE: F0 07         BEQ   $B3D7               ; 
B3D0: 46 0D         LSR   <$0D                ; 
B3D2: 66 0E         ROR   <$0E                ; 
B3D4: 88            DEY                       ;
B3D5: D0 F9         BNE   $B3D0               ; 
B3D7: A9 00         LDA   #$00                ;
B3D9: 8D 27 06      STA   $0627               ; 
B3DC: 85 50         STA   <$50                ; 
B3DE: 85 51         STA   <$51                ; 
B3E0: AD 70 06      LDA   $0670               ; 
B3E3: C5 0E         CMP   <$0E                ; 
B3E5: 90 19         BCC   $B400               ; 
B3E7: 38            SEC                       ;
B3E8: E5 0E         SBC   <$0E                ; 
B3EA: 8D 70 06      STA   $0670               ; 
B3ED: AD 6F 06      LDA   $066F               ; 
B3F0: 29 0F         AND   #$0F                ;
B3F2: C5 0D         CMP   <$0D                ; 
B3F4: 90 23         BCC   $B419               ; 
B3F6: AD 6F 06      LDA   $066F               ; 
B3F9: 38            SEC                       ;
B3FA: E5 0D         SBC   <$0D                ; 
B3FC: 8D 6F 06      STA   $066F               ; 
B3FF: 60            RTS                       ;
B400: A5 0E         LDA   <$0E                ; 
B402: 38            SEC                       ;
B403: ED 70 06      SBC   $0670               ; 
B406: 85 0E         STA   <$0E                ; 
B408: AD 6F 06      LDA   $066F               ; 
B40B: 29 0F         AND   #$0F                ;
B40D: F0 0A         BEQ   $B419               ; 
B40F: CE 6F 06      DEC   $066F               ; 
B412: A9 FF         LDA   #$FF                ;
B414: 8D 70 06      STA   $0670               ; 
B417: D0 BE         BNE   $B3D7               ; 
B419: AD 6F 06      LDA   $066F               ; 
B41C: 29 F0         AND   #$F0                ;
B41E: 8D 6F 06      STA   $066F               ; 
B421: 20 A3 EB      JSR   $EBA3               ; 
B424: 8D 70 06      STA   $0670               ; 
B427: 85 AC         STA   <$AC                ; 
B429: A9 11         LDA   #$11                ;
B42B: 85 12         STA   <$12                ; 
B42D: A9 04         LDA   #$04                ;
B42F: 85 98         STA   <$98                ; 
B431: 60            RTS                       ;
B432: B9 AC 00      LDA   $00AC,Y             ;
B435: 0A            ASL   A                   ;
B436: B0 F9         BCS   $B431               ; 
B438: 84 00         STY   <$00                ; 
B43A: A9 02         LDA   #$02                ;
B43C: 85 09         STA   <$09                ; 
B43E: A9 0A         LDA   #$0A                ;
B440: 85 0D         STA   <$0D                ; 
B442: 85 0E         STA   <$0E                ; 
B444: B9 70 00      LDA   $0070,Y             ;
B447: 18            CLC                       ;
B448: 69 04         ADC   #$04                ;
B44A: 85 04         STA   <$04                ; 
B44C: B9 84 00      LDA   $0084,Y             ;
B44F: 18            CLC                       ;
B450: 69 08         ADC   #$08                ;
B452: 85 05         STA   <$05                ; 
B454: A9 00         LDA   #$00                ;
B456: 85 06         STA   <$06                ; 
B458: A4 00         LDY   <$00                ; 
B45A: B9 AC 00      LDA   $00AC,Y             ;
B45D: F0 79         BEQ   $B4D8               ; 
B45F: 20 FF 7D      JSR   $7DFF               ; 
B462: F0 74         BEQ   $B4D8               ; 
B464: C0 0F         CPY   #$0F                ;
B466: D0 1E         BNE   $B486               ; 
B468: BD B2 04      LDA   $04B2,X             ;
B46B: 25 09         AND   <$09                ; 
B46D: F0 03         BEQ   $B472               ; 
B46F: 20 C5 7D      JSR   $7DC5               ; 
B472: A9 50         LDA   #$50                ;
B474: 99 AC 00      STA   $00AC,Y             ;
B477: BD B2 04      LDA   $04B2,X             ;
B47A: 25 09         AND   <$09                ; 
B47C: D0 5A         BNE   $B4D8               ; 
B47E: A9 00         LDA   #$00                ;
B480: 85 07         STA   <$07                ; 
B482: A9 10         LDA   #$10                ;
B484: 95 3D         STA   $3D,X               ;
B486: BD B2 04      LDA   $04B2,X             ;
B489: 25 09         AND   <$09                ; 
B48B: D0 4C         BNE   $B4D9               ; 
B48D: BD 4F 03      LDA   $034F,X             ;
B490: C9 33         CMP   #$33                ;
B492: F0 04         BEQ   $B498               ; 
B494: C9 34         CMP   #$34                ;
B496: D0 03         BNE   $B49B               ; 
B498: 4C 40 A4      JMP   $A440               ; 
B49B: C9 13         CMP   #$13                ;
B49D: F0 04         BEQ   $B4A3               ; 
B49F: C9 12         CMP   #$12                ;
B4A1: D0 0C         BNE   $B4AF               ; 
B4A3: C0 0F         CPY   #$0F                ;
B4A5: F0 1D         BEQ   $B4C4               ; 
B4A7: B9 98 00      LDA   $0098,Y             ;
B4AA: 95 98         STA   $98,X               ;
B4AC: 4C 54 7C      JMP   $7C54               ; 
B4AF: C9 0B         CMP   #$0B                ;
B4B1: F0 04         BEQ   $B4B7               ; 
B4B3: C9 0C         CMP   #$0C                ;
B4B5: D0 0D         BNE   $B4C4               ; 
B4B7: B9 98 00      LDA   $0098,Y             ;
B4BA: 15 98         ORA   $98,X               ;
B4BC: C9 0C         CMP   #$0C                ;
B4BE: F0 19         BEQ   $B4D9               ; 
B4C0: C9 03         CMP   #$03                ;
B4C2: F0 15         BEQ   $B4D9               ; 
B4C4: A9 02         LDA   #$02                ;
B4C6: 8D 04 06      STA   $0604               ; 
B4C9: BD 85 04      LDA   $0485,X             ;
B4CC: C5 07         CMP   <$07                ; 
B4CE: 90 16         BCC   $B4E6               ; 
B4D0: 38            SEC                       ;
B4D1: E5 07         SBC   <$07                ; 
B4D3: 9D 85 04      STA   $0485,X             ;
B4D6: F0 0E         BEQ   $B4E6               ; 
B4D8: 60            RTS                       ;
B4D9: A5 09         LDA   <$09                ; 
B4DB: C9 20         CMP   #$20                ;
B4DD: F0 F9         BEQ   $B4D8               ; 
B4DF: C9 08         CMP   #$08                ;
B4E1: F0 F5         BEQ   $B4D8               ; 
B4E3: 4C C5 7D      JMP   $7DC5               ; 
B4E6: EE 27 06      INC   $0627               ; 
B4E9: A5 50         LDA   <$50                ; 
B4EB: C9 0A         CMP   #$0A                ;
B4ED: B0 10         BCS   $B4FF               ; 
B4EF: E6 50         INC   <$50                ; 
B4F1: A5 50         LDA   <$50                ; 
B4F3: C9 0A         CMP   #$0A                ;
B4F5: D0 08         BNE   $B4FF               ; 
B4F7: A5 09         LDA   <$09                ; 
B4F9: C9 08         CMP   #$08                ;
B4FB: D0 02         BNE   $B4FF               ; 
B4FD: E6 51         INC   <$51                ; 
B4FF: 20 A6 FE      JSR   $FEA6               ; 
B502: A9 00         LDA   #$00                ;
B504: 95 3D         STA   $3D,X               ;
B506: 20 E6 EE      JSR   $EEE6               ; 
B509: 9D F0 04      STA   $04F0,X             ;
B50C: 60            RTS                       ;
B50D: 84 00         STY   <$00                ; 
B50F: A9 10         LDA   #$10                ;
B511: 85 09         STA   <$09                ; 
B513: B9 AC 00      LDA   $00AC,Y             ;
B516: 4A            LSR   A                   ;
B517: B0 32         BCS   $B54B               ; 
B519: A9 0C         LDA   #$0C                ;
B51B: 85 0D         STA   <$0D                ; 
B51D: B9 AC 00      LDA   $00AC,Y             ;
B520: A0 20         LDY   #$20                ;
B522: 0A            ASL   A                   ;
B523: B0 15         BCS   $B53A               ; 
B525: A9 01         LDA   #$01                ;
B527: 85 09         STA   <$09                ; 
B529: A0 40         LDY   #$40                ;
B52B: AD 57 06      LDA   $0657               ; 
B52E: C9 03         CMP   #$03                ;
B530: F0 08         BEQ   $B53A               ; 
B532: A0 20         LDY   #$20                ;
B534: C9 02         CMP   #$02                ;
B536: F0 02         BEQ   $B53A               ; 
B538: A0 10         LDY   #$10                ;
B53A: 98            TYA                       ;
B53B: 20 86 7D      JSR   $7D86               ; 
B53E: A5 06         LDA   <$06                ; 
B540: F0 09         BEQ   $B54B               ; 
B542: 8A            TXA                       ;
B543: 48            PHA                       ;
B544: A2 0E         LDX   #$0E                ;
B546: 20 D4 F3      JSR   $F3D4               ; 
B549: 68            PLA                       ;
B54A: AA            TAX                       ;
B54B: 60            RTS                       ;
B54C: 84 00         STY   <$00                ; 
B54E: A9 20         LDA   #$20                ;
B550: 85 09         STA   <$09                ; 
B552: A9 10         LDA   #$10                ;
B554: 85 07         STA   <$07                ; 
B556: A9 0E         LDA   #$0E                ;
B558: 85 0D         STA   <$0D                ; 
B55A: B9 AC 00      LDA   $00AC,Y             ;
B55D: C9 20         CMP   #$20                ;
B55F: B0 10         BCS   $B571               ; 
B561: C9 13         CMP   #$13                ;
B563: D0 30         BNE   $B595               ; 
B565: A9 08         LDA   #$08                ;
B567: 85 09         STA   <$09                ; 
B569: A9 40         LDA   #$40                ;
B56B: 85 07         STA   <$07                ; 
B56D: A9 18         LDA   #$18                ;
B56F: 85 0D         STA   <$0D                ; 
B571: B9 70 00      LDA   $0070,Y             ;
B574: 18            CLC                       ;
B575: 69 08         ADC   #$08                ;
B577: 85 04         STA   <$04                ; 
B579: B9 84 00      LDA   $0084,Y             ;
B57C: 18            CLC                       ;
B57D: 69 08         ADC   #$08                ;
B57F: 85 05         STA   <$05                ; 
B581: A5 0D         LDA   <$0D                ; 
B583: 20 FB 7D      JSR   $7DFB               ; 
B586: F0 0D         BEQ   $B595               ; 
B588: 20 16 7C      JSR   $7C16               ; 
B58B: BD B2 04      LDA   $04B2,X             ;
B58E: 25 09         AND   <$09                ; 
B590: D0 03         BNE   $B595               ; 
B592: 20 26 7E      JSR   $7E26               ; 
B595: 60            RTS                       ;
B596: 10 20         BPL   $B5B8               ; 
B598: 40            RTI                       ;
B599: 84 00         STY   <$00                ; 
B59B: A9 01         LDA   #$01                ;
B59D: 85 09         STA   <$09                ; 
B59F: B9 AC 00      LDA   $00AC,Y             ;
B5A2: C9 02         CMP   #$02                ;
B5A4: D0 EF         BNE   $B595               ; 
B5A6: AC 57 06      LDY   $0657               ; 
B5A9: B9 25 7D      LDA   $7D25,Y             ;
B5AC: 85 07         STA   <$07                ; 
B5AE: A5 98         LDA   <$98                ; 
B5B0: 29 0C         AND   #$0C                ;
B5B2: F0 09         BEQ   $B5BD               ; 
B5B4: A9 0C         LDA   #$0C                ;
B5B6: 85 0D         STA   <$0D                ; 
B5B8: A9 10         LDA   #$10                ;
B5BA: 4C 53 7D      JMP   $7D53               ; 
B5BD: A9 10         LDA   #$10                ;
B5BF: 85 0D         STA   <$0D                ; 
B5C1: A9 0C         LDA   #$0C                ;
B5C3: 85 0E         STA   <$0E                ; 
B5C5: 20 D1 7D      JSR   $7DD1               ; 
B5C8: A5 06         LDA   <$06                ; 
B5CA: F0 C9         BEQ   $B595               ; 
B5CC: 4C AA 7D      JMP   $7DAA               ; 
B5CF: 84 00         STY   <$00                ; 
B5D1: B9 AC 00      LDA   $00AC,Y             ;
B5D4: C9 30         CMP   #$30                ;
B5D6: 90 08         BCC   $B5E0               ; 
B5D8: A9 01         LDA   #$01                ;
B5DA: 85 09         STA   <$09                ; 
B5DC: A9 20         LDA   #$20                ;
B5DE: D0 CC         BNE   $B5AC               ; 
B5E0: C9 20         CMP   #$20                ;
B5E2: B0 56         BCS   $B63A               ; 
B5E4: A9 04         LDA   #$04                ;
B5E6: 85 09         STA   <$09                ; 
B5E8: A9 20         LDA   #$20                ;
B5EA: AC 59 06      LDY   $0659               ; 
B5ED: C0 01         CPY   #$01                ;
B5EF: F0 01         BEQ   $B5F2               ; 
B5F1: 0A            ASL   A                   ;
B5F2: A0 0B         LDY   #$0B                ;
B5F4: 84 0D         STY   <$0D                ; 
B5F6: 20 CB 7D      JSR   $7DCB               ; 
B5F9: A5 06         LDA   <$06                ; 
B5FB: F0 3D         BEQ   $B63A               ; 
B5FD: C0 12         CPY   #$12                ;
B5FF: D0 19         BNE   $B61A               ; 
B601: BD 4F 03      LDA   $034F,X             ;
B604: C9 16         CMP   #$16                ;
B606: D0 08         BNE   $B610               ; 
B608: A9 00         LDA   #$00                ;
B60A: 9D 85 04      STA   $0485,X             ;
B60D: 4C 54 7C      JMP   $7C54               ; 
B610: A9 20         LDA   #$20                ;
B612: 99 AC 00      STA   $00AC,Y             ;
B615: A9 03         LDA   #$03                ;
B617: 99 D0 03      STA   $03D0,Y             ;
B61A: BD 4F 03      LDA   $034F,X             ;
B61D: C9 0B         CMP   #$0B                ;
B61F: F0 04         BEQ   $B625               ; 
B621: C9 0C         CMP   #$0C                ;
B623: D0 0D         BNE   $B632               ; 
B625: B9 98 00      LDA   $0098,Y             ;
B628: 15 98         ORA   $98,X               ;
B62A: C9 0C         CMP   #$0C                ;
B62C: F0 07         BEQ   $B635               ; 
B62E: C9 03         CMP   #$03                ;
B630: F0 03         BEQ   $B635               ; 
B632: 4C 26 7E      JMP   $7E26               ; 
B635: A9 01         LDA   #$01                ;
B637: 8D 04 06      STA   $0604               ; 
B63A: 60            RTS                       ;
B63B: 85 07         STA   <$07                ; 
B63D: A5 0D         LDA   <$0D                ; 
B63F: 85 0E         STA   <$0E                ; 
B641: A4 00         LDY   <$00                ; 
B643: A5 98         LDA   <$98                ; 
B645: 29 0C         AND   #$0C                ;
B647: F0 11         BEQ   $B65A               ; 
B649: B9 70 00      LDA   $0070,Y             ;
B64C: 18            CLC                       ;
B64D: 69 06         ADC   #$06                ;
B64F: 85 04         STA   <$04                ; 
B651: B9 84 00      LDA   $0084,Y             ;
B654: 18            CLC                       ;
B655: 69 08         ADC   #$08                ;
B657: 4C F8 7D      JMP   $7DF8               ; 
B65A: B9 70 00      LDA   $0070,Y             ;
B65D: 18            CLC                       ;
B65E: 69 08         ADC   #$08                ;
B660: 85 04         STA   <$04                ; 
B662: B9 84 00      LDA   $0084,Y             ;
B665: 18            CLC                       ;
B666: 69 06         ADC   #$06                ;
B668: 4C E2 7B      JMP   $7BE2               ; 
B66B: 85 0D         STA   <$0D                ; 
B66D: 85 0E         STA   <$0E                ; 
B66F: A9 00         LDA   #$00                ;
B671: 85 06         STA   <$06                ; 
B673: A4 00         LDY   <$00                ; 
B675: A5 02         LDA   <$02                ; 
B677: 38            SEC                       ;
B678: E5 04         SBC   <$04                ; 
B67A: 20 1F 70      JSR   $701F               ; 
B67D: 85 0A         STA   <$0A                ; 
B67F: C5 0D         CMP   <$0D                ; 
B681: B0 10         BCS   $B693               ; 
B683: A5 03         LDA   <$03                ; 
B685: 38            SEC                       ;
B686: E5 05         SBC   <$05                ; 
B688: 20 1F 70      JSR   $701F               ; 
B68B: 85 0B         STA   <$0B                ; 
B68D: C5 0E         CMP   <$0E                ; 
B68F: B0 02         BCS   $B693               ; 
B691: E6 06         INC   <$06                ; 
B693: A5 06         LDA   <$06                ; 
B695: 60            RTS                       ;
B696: A4 00         LDY   <$00                ; 
B698: E0 0D         CPX   #$0D                ;
B69A: B0 07         BCS   $B6A3               ; 
B69C: BD B2 04      LDA   $04B2,X             ;
B69F: 25 09         AND   <$09                ; 
B6A1: D0 6A         BNE   $B70D               ; 
B6A3: A9 08         LDA   #$08                ;
B6A5: 85 08         STA   <$08                ; 
B6A7: B5 84         LDA   $84,X               ;
B6A9: 85 04         STA   <$04                ; 
B6AB: B9 84 00      LDA   $0084,Y             ;
B6AE: 85 05         STA   <$05                ; 
B6B0: C0 00         CPY   #$00                ;
B6B2: D0 0D         BNE   $B6C1               ; 
B6B4: AD 94 03      LDA   $0394               ; 
B6B7: F0 08         BEQ   $B6C1               ; 
B6B9: A5 98         LDA   <$98                ; 
B6BB: 29 03         AND   #$03                ;
B6BD: D0 08         BNE   $B6C7               ; 
B6BF: F0 13         BEQ   $B6D4               ; 
B6C1: A5 0B         LDA   <$0B                ; 
B6C3: C9 04         CMP   #$04                ;
B6C5: B0 0D         BCS   $B6D4               ; 
B6C7: A9 02         LDA   #$02                ;
B6C9: 85 08         STA   <$08                ; 
B6CB: B5 70         LDA   $70,X               ;
B6CD: 85 04         STA   <$04                ; 
B6CF: B9 70 00      LDA   $0070,Y             ;
B6D2: 85 05         STA   <$05                ; 
B6D4: A5 04         LDA   <$04                ; 
B6D6: C5 05         CMP   <$05                ; 
B6D8: B0 02         BCS   $B6DC               ; 
B6DA: 46 08         LSR   <$08                ; 
B6DC: C0 00         CPY   #$00                ;
B6DE: D0 2E         BNE   $B70E               ; 
B6E0: AD F0 04      LDA   $04F0               ; 
B6E3: D0 28         BNE   $B70D               ; 
B6E5: A5 08         LDA   <$08                ; 
B6E7: 09 80         ORA   #$80                ;
B6E9: 85 C0         STA   <$C0                ; 
B6EB: A9 18         LDA   #$18                ;
B6ED: 8D F0 04      STA   $04F0               ; 
B6F0: A9 20         LDA   #$20                ;
B6F2: 85 D3         STA   <$D3                ; 
B6F4: E0 0D         CPX   #$0D                ;
B6F6: B0 15         BCS   $B70D               ; 
B6F8: BD BF 04      LDA   $04BF,X             ;
B6FB: 29 80         AND   #$80                ;
B6FD: D0 0E         BNE   $B70D               ; 
B6FF: BD 4F 03      LDA   $034F,X             ;
B702: C9 12         CMP   #$12                ;
B704: F0 07         BEQ   $B70D               ; 
B706: B5 98         LDA   $98,X               ;
B708: 20 13 70      JSR   $7013               ; 
B70B: 95 98         STA   $98,X               ;
B70D: 60            RTS                       ;
B70E: B9 98 00      LDA   $0098,Y             ;
B711: 85 08         STA   <$08                ; 
B713: BD BF 04      LDA   $04BF,X             ;
B716: 29 80         AND   #$80                ;
B718: F0 06         BEQ   $B720               ; 
B71A: A5 08         LDA   <$08                ; 
B71C: 09 40         ORA   #$40                ;
B71E: 85 08         STA   <$08                ; 
B720: BD F0 04      LDA   $04F0,X             ;
B723: D0 2B         BNE   $B750               ; 
B725: BD 4F 03      LDA   $034F,X             ;
B728: C9 33         CMP   #$33                ;
B72A: F0 04         BEQ   $B730               ; 
B72C: C9 34         CMP   #$34                ;
B72E: D0 11         BNE   $B741               ; 
B730: A5 0F         LDA   <$0F                ; 
B732: C9 03         CMP   #$03                ;
B734: F0 04         BEQ   $B73A               ; 
B736: C9 04         CMP   #$04                ;
B738: D0 16         BNE   $B750               ; 
B73A: BD 6B 04      LDA   $046B,X             ;
B73D: C9 03         CMP   #$03                ;
B73F: D0 0F         BNE   $B750               ; 
B741: A5 08         LDA   <$08                ; 
B743: 09 80         ORA   #$80                ;
B745: 95 C0         STA   $C0,X               ;
B747: A9 40         LDA   #$40                ;
B749: 95 D3         STA   $D3,X               ;
B74B: A9 10         LDA   #$10                ;
B74D: 9D F0 04      STA   $04F0,X             ;
B750: 60            RTS                       ;

B751: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B760: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B780: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B7A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B7C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B7E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B800: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B820: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B840: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B860: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B880: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B8A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B8C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B8E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B900: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B920: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B940: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B960: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B980: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B9A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B9C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B9E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BA00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BA20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BA40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BA60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BA80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BAA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BAC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BAE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BB00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BB20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BB40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BB60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BB80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BBA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BBC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BBE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BC00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BC20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BC40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BC60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BC80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BCA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BCC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BCE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BD00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BD20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BD40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BD60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BD80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BDA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BDC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BDE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BE00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BE20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BE40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BE60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BE80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BEA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BEC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BEE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BF00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BF20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BF40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 

; From here down is the same in all banks (except for the origin
; difference in bank 7). 
```

# RESET

```code
RESET: 
;
; Configure the MMC1 and jump to E440 (Bank 7) for startup.
;
BF50: 78            SEI                       ; Disable interrupts
BF51: D8            CLD                       ; Clear decimal flag
BF52: A9 00         LDA   #$00                ; Clear the PPU control register ...
BF54: 8D 00 20      STA   $2000               ; ... truns off NMIs
BF57: A2 FF         LDX   #$FF                ; Stack to ...
BF59: 9A            TXS                       ; ... 01FF
BF5A: AD 02 20      LDA   $2002               ; Wait ...
BF5D: 29 80         AND   #$80                ; ... for ...
BF5F: F0 F9         BEQ   $BF5A               ; ... VBLANK
BF61: AD 02 20      LDA   $2002               ; Wait ...
BF64: 29 80         AND   #$80                ; ... for another ...
BF66: F0 F9         BEQ   $BF61               ; ... VBLANK (1st might have been a leftover flag)
BF68: 09 FF         ORA   #$FF                ; Reset ...
BF6A: 8D 00 80      STA   $8000               ; ... ...
BF6D: 8D 00 A0      STA   $A000               ; ... all ...
BF70: 8D 00 C0      STA   $C000               ; ... four ...
BF73: 8D 00 E0      STA   $E000               ; ... MMC1 registers
BF76: A9 0F         LDA   #$0F                ; Set MMC control to 8K CHR ROM, fixed/bank 16K PRG pages, ...
BF78: 20 98 BF      JSR   $BF98               ; ... and horizontal mirroring (vertical scrolling)
BF7B: A9 00         LDA   #$00                ; Set MMC reg1 VROM bank
BF7D: 8D 00 A0      STA   $A000               ; The cartridge doesn't ...
BF80: 4A            LSR   A                   ; ... swap VROM pages. ...
BF81: 8D 00 A0      STA   $A000               ; ... Just ...
BF84: 4A            LSR   A                   ; ... set ...
BF85: 8D 00 A0      STA   $A000               ; ... to ...
BF88: 4A            LSR   A                   ; ...
BF89: 8D 00 A0      STA   $A000               ; ...
BF8C: 4A            LSR   A                   ; ...
BF8D: 8D 00 A0      STA   $A000               ; ... --00000
BF90: A9 07         LDA   #$07                ; Interesting! Put bank 7 ...
BF92: 20 AC BF      JSR   $BFAC               ; ... in the low ROM bank
BF95: 4C 40 E4      JMP   $E440               ; Start of game

; MMC1 Info
; R0 - Control ***CPPMM
;  C CHR ROM bank mode. Zelda uses 0: 8KB at a time
;  PP Program ROM switch mode. Zelda uses 3: 16K fixed, 16K switched banks
;  MM Name table mirroring. Zelda uses 2 or 3: vertical or horizontal
; R1 - CHR bank size ***CCCCC
;  Ignored in Zelda since R0.C is 0
; R2 - CHR bank select ***CCCCC
;  Ignored in Zelda since R0.C is 0
; R3 - PRG bank select ***RPPPP
;  R PRG RAM enabled. Zelda sends 0, but battery-backed RAM is always enabled.
;  PPPP bank select. Zelda switches banks 0-6.
```

# MMC Control

```code
MMC_Control: 
; Set the MMC Control register (0) to value in A
BF98: 8D 00 80      STA   $8000               ; MMC Register 0 (control): --edcba ...
BF9B: 4A            LSR   A                   ;  ... mirroring 
BF9C: 8D 00 80      STA   $8000               ;  ... mirroring 
BF9F: 4A            LSR   A                   ;  ... switch: c=0 high ROM, C=1 low ROM
BFA0: 8D 00 80      STA   $8000               ;  ... size: d=0 32K (full), D=1 16K (half)
BFA3: 4A            LSR   A                   ;  ... chrrom mode: e=0 8K banks, B=1 4K banks
BFA4: 8D 00 80      STA   $8000               ; The MMC is write-trigger (write to ROM ...
BFA7: 4A            LSR   A                   ; .. has no affect anyway).
BFA8: 8D 00 80      STA   $8000               ; Bits are written from LSB to MSB ...
BFAB: 60            RTS                       ; ... only 5 bits
```

# MMC Bank

```code
MMC_Bank: 
; Set the MMC Bank register (3) to value in A
BFAC: 8D 00 E0      STA   $E000               ; MMC Register 3 (ROM page switching): --edcba ...
BFAF: 4A            LSR   A                   ; ...
BFB0: 8D 00 E0      STA   $E000               ; ... Write the ...
BFB3: 4A            LSR   A                   ; ... switching ...
BFB4: 8D 00 E0      STA   $E000               ; ... page ...
BFB7: 4A            LSR   A                   ; ... number
BFB8: 8D 00 E0      STA   $E000               ; The MMC is write-trigger (write to ROM ...
BFBB: 4A            LSR   A                   ; .. has no affect anyway).
BFBC: 8D 00 E0      STA   $E000               ; Bits are written from LSB to MSB ...
BFBF: 60            RTS                       ; ... only 5 bits

BFC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
BFD0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
BFE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
BFF0: FF FF FF FF FF FF FF FF FF FF
```

# Vectors

```code
BFFA: 84 E4       ; NMI to E484
BFFC: 50 BF       ; RESET to BF50
BFFE: F0 BF       ; IRQ to BFF0 (this bank should never be at end)
```
