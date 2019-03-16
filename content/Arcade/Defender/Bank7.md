![Defender Bank 7](Defender.jpg)

>>> cpu 6809

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](Hardware.md)

# Bank7
 
(write 7 to $D000)

```plainCode
C000: 7E C0 15      JMP   $C015              ;
C003: 7E C0 92      JMP   $C092              ;
C006: 7E C2 62      JMP   $C262              ;
C009: 7E C2 9A      JMP   $C29A              ;
C00C: C4 50                                  ;address?
C00E: 7E C5 D0      JMP   $C5D0              ;
C011: C6 BA                                  ;address?
C013: C7 72                                  ;address?

C015: DC 20         LDD   <$20               ;
C017: C4 E0         ANDB  #$E0               ;
C019: DD 17         STD   <$17               ;
C01B: C3 26 10      ADDD  #$2610             ;
C01E: DD 15         STD   <$15               ;
C020: 0F 0F         CLR   <$0F               ;
C022: 8E C3 4F      LDX   #$C34F             ;
C025: 9F 09         STX   <$09               ;
C027: 86 E0         LDA   #$E0               ;
C029: 97 11         STA   <$11               ;
C02B: BD C2 AA      JSR   $C2AA              ;
C02E: 8E 00 10      LDX   #$0010             ;
C031: 9C 15         CMPX  <$15               ;
C033: 27 12         BEQ   $C047              ;
C035: 96 0D         LDA   <$0D               ;
C037: 2A 04         BPL   $C03D              ;
C039: 0A 11         DEC   <$11               ;
C03B: 20 02         BRA   $C03F              ;
C03D: 0C 11         INC   <$11               ;
C03F: BD C2 AA      JSR   $C2AA              ;
C042: 30 88 20      LEAX  $20,X              ;
C045: 20 EA         BRA   $C031              ;
C047: DC 09         LDD   <$09               ;
C049: DD 03         STD   <$03               ;
C04B: 96 0F         LDA   <$0F               ;
C04D: 97 00         STA   <$00               ;
C04F: 96 0D         LDA   <$0D               ;
C051: 97 01         STA   <$01               ;
C053: 96 11         LDA   <$11               ;
C055: 97 02         STA   <$02               ;
C057: 8E B7 00      LDX   #$B700             ;
C05A: 9F 05         STX   <$05               ;
C05C: 8E BA 90      LDX   #$BA90             ;
C05F: 9F 07         STX   <$07               ;
C061: DC 15         LDD   <$15               ;
C063: 83 00 20      SUBD  #$0020             ;
C066: DD 15         STD   <$15               ;
C068: 10 93 17      CMPD  <$17               ;
C06B: 2B 05         BMI   $C072              ;
C06D: BD C1 2C      JSR   $C12C              ;
C070: 20 EF         BRA   $C061              ;
C072: DC 03         LDD   <$03               ;
C074: DD 0B         STD   <$0B               ;
C076: 96 00         LDA   <$00               ;
C078: 97 10         STA   <$10               ;
C07A: 96 01         LDA   <$01               ;
C07C: 97 0E         STA   <$0E               ;
C07E: 96 02         LDA   <$02               ;
C080: 97 12         STA   <$12               ;
C082: 10 8E BE 20   LDY   #$BE20             ;
C086: 8E 00 00      LDX   #$0000             ;
C089: AF A1         STX   ,Y++               ;
C08B: 10 8C BF 50   CMPY  #$BF50             ;
C08F: 26 F8         BNE   $C089              ;
C091: 39            RTS                      ;

C092: DC 20         LDD   <$20               ;
C094: C4 E0         ANDB  #$E0               ;
C096: 93 15         SUBD  <$15               ;
C098: 58            ASLB                     ;
C099: 49            ROLA                     ;
C09A: 58            ASLB                     ;
C09B: 49            ROLA                     ;
C09C: 58            ASLB                     ;
C09D: 49            ROLA                     ;
C09E: 97 00         STA   <$00               ;
C0A0: 27 20         BEQ   $C0C2              ;
C0A2: 2B 10         BMI   $C0B4              ;
C0A4: DC 15         LDD   <$15               ;
C0A6: C3 00 20      ADDD  #$0020             ;
C0A9: DD 15         STD   <$15               ;
C0AB: BD C1 CD      JSR   $C1CD              ;
C0AE: 0A 00         DEC   <$00               ;
C0B0: 26 F2         BNE   $C0A4              ;
C0B2: 20 0E         BRA   $C0C2              ;
C0B4: DC 15         LDD   <$15               ;
C0B6: 83 00 20      SUBD  #$0020             ;
C0B9: DD 15         STD   <$15               ;
C0BB: BD C1 2C      JSR   $C12C              ;
C0BE: 0C 00         INC   <$00               ;
C0C0: 26 F2         BNE   $C0B4              ;
C0C2: DC 20         LDD   <$20               ;
C0C4: C4 E0         ANDB  #$E0               ;
C0C6: DD 15         STD   <$15               ;
C0C8: 8E 00 00      LDX   #$0000             ;
C0CB: 10 8E BE 20   LDY   #$BE20             ;
C0CF: 10 DF 13      STS   <$13               ;
C0D2: 10 DE 05      LDS   <$05               ;
C0D5: C5 20         BITB  #$20               ;
C0D7: 26 03         BNE   $C0DC              ;
C0D9: 10 DE 07      LDS   <$07               ;
C0DC: 86 98         LDA   #$98               ;
C0DE: AF B4         STX   [,Y]               ;
C0E0: 35 44         PULS  B,U                ;
C0E2: ED A4         STD   ,Y                 ;
C0E4: EF B1         STU   [,Y++]             ;
C0E6: 4A            DECA                     ;
C0E7: AF B4         STX   [,Y]               ;
C0E9: 35 44         PULS  B,U                ;
C0EB: ED A4         STD   ,Y                 ;
C0ED: EF B1         STU   [,Y++]             ;
C0EF: 4A            DECA                     ;
C0F0: AF B4         STX   [,Y]               ;
C0F2: 35 44         PULS  B,U                ;
C0F4: ED A4         STD   ,Y                 ;
C0F6: EF B1         STU   [,Y++]             ;
C0F8: 4A            DECA                     ;
C0F9: AF B4         STX   [,Y]               ;
C0FB: 35 44         PULS  B,U                ;
C0FD: ED A4         STD   ,Y                 ;
C0FF: EF B1         STU   [,Y++]             ;
C101: 4A            DECA                     ;
C102: AF B4         STX   [,Y]               ;
C104: 35 44         PULS  B,U                ;
C106: ED A4         STD   ,Y                 ;
C108: EF B1         STU   [,Y++]             ;
C10A: 4A            DECA                     ;
C10B: AF B4         STX   [,Y]               ;
C10D: 35 44         PULS  B,U                ;
C10F: ED A4         STD   ,Y                 ;
C111: EF B1         STU   [,Y++]             ;
C113: 4A            DECA                     ;
C114: AF B4         STX   [,Y]               ;
C116: 35 44         PULS  B,U                ;
C118: ED A4         STD   ,Y                 ;
C11A: EF B1         STU   [,Y++]             ;
C11C: 4A            DECA                     ;
C11D: AF B4         STX   [,Y]               ;
C11F: 35 44         PULS  B,U                ;
C121: ED A4         STD   ,Y                 ;
C123: EF B1         STU   [,Y++]             ;
C125: 4A            DECA                     ;
C126: 26 B6         BNE   $C0DE              ;
C128: 10 DE 13      LDS   <$13               ;
C12B: 39            RTS                      ;

;SUBRTN
C12C: BD C3 23      JSR   $C323              ;
C12F: 2B 04         BMI   $C135              ;
C131: 0A 12         DEC   <$12               ;
C133: 20 02         BRA   $C137              ;
C135: 0C 12         INC   <$12               ;
C137: 86 20         LDA   #$20               ;
C139: 95 16         BITA  <$16               ;
C13B: 26 48         BNE   $C185              ;
C13D: 9E 07         LDX   <$07               ;
C13F: BD C2 F6      JSR   $C2F6              ;
C142: 2B 20         BMI   $C164              ;
C144: 0A 11         DEC   <$11               ;
C146: 96 11         LDA   <$11               ;
C148: A7 84         STA   ,X                 ;
C14A: A7 89 01 C8   STA   $01C8,X            ;
C14E: CC 70 07      LDD   #$7007             ;
C151: ED 01         STD   1,X                ;
C153: ED 89 01 C9   STD   $01C9,X            ;
C157: 30 03         LEAX  3,X                ;
C159: 8C BC 58      CMPX  #$BC58             ;
C15C: 26 03         BNE   $C161              ;
C15E: 8E BA 90      LDX   #$BA90             ;
C161: 9F 07         STX   <$07               ;
C163: 39            RTS                      ;
C164: 96 11         LDA   <$11               ;
C166: A7 84         STA   ,X                 ;
C168: A7 89 01 C8   STA   $01C8,X            ;
C16C: 4C            INCA                     ;
C16D: 97 11         STA   <$11               ;
C16F: CC 07 70      LDD   #$0770             ;
C172: ED 01         STD   1,X                ;
C174: ED 89 01 C9   STD   $01C9,X            ;
C178: 30 03         LEAX  3,X                ;
C17A: 8C BC 58      CMPX  #$BC58             ;
C17D: 26 03         BNE   $C182              ;
C17F: 8E BA 90      LDX   #$BA90             ;
C182: 9F 07         STX   <$07               ;
C184: 39            RTS                      ;
C185: 9E 05         LDX   <$05               ;
C187: BD C2 F6      JSR   $C2F6              ;
C18A: 2B 20         BMI   $C1AC              ;
C18C: 0A 11         DEC   <$11               ;
C18E: 96 11         LDA   <$11               ;
C190: A7 84         STA   ,X                 ;
C192: A7 89 01 C8   STA   $01C8,X            ;
C196: CC 70 07      LDD   #$7007             ;
C199: ED 01         STD   1,X                ;
C19B: ED 89 01 C9   STD   $01C9,X            ;
C19F: 30 03         LEAX  3,X                ;
C1A1: 8C B8 C8      CMPX  #$B8C8             ;
C1A4: 26 03         BNE   $C1A9              ;
C1A6: 8E B7 00      LDX   #$B700             ;
C1A9: 9F 05         STX   <$05               ;
C1AB: 39            RTS                      ;
C1AC: 96 11         LDA   <$11               ;
C1AE: A7 84         STA   ,X                 ;
C1B0: A7 89 01 C8   STA   $01C8,X            ;
C1B4: 4C            INCA                     ;
C1B5: 97 11         STA   <$11               ;
C1B7: CC 07 70      LDD   #$0770             ;
C1BA: ED 01         STD   1,X                ;
C1BC: ED 89 01 C9   STD   $01C9,X            ;
C1C0: 30 03         LEAX  3,X                ;
C1C2: 8C B8 C8      CMPX  #$B8C8             ;
C1C5: 26 03         BNE   $C1CA              ;
C1C7: 8E B7 00      LDX   #$B700             ;
C1CA: 9F 05         STX   <$05               ;
C1CC: 39            RTS                      ;

;SUBRTN
C1CD: 96 0D         LDA   <$0D               ;
C1CF: 2A 04         BPL   $C1D5              ;
C1D1: 0A 11         DEC   <$11               ;
C1D3: 20 02         BRA   $C1D7              ;
C1D5: 0C 11         INC   <$11               ;
C1D7: BD C2 AA      JSR   $C2AA              ;
C1DA: 86 20         LDA   #$20               ;
C1DC: 95 16         BITA  <$16               ;
C1DE: 27 41         BEQ   $C221              ;
C1E0: 9E 07         LDX   <$07               ;
C1E2: 30 1D         LEAX  -3,X               ;
C1E4: 8C BA 8D      CMPX  #$BA8D             ;
C1E7: 26 03         BNE   $C1EC              ;
C1E9: 8E BC 55      LDX   #$BC55             ;
C1EC: 9F 07         STX   <$07               ;
C1EE: 96 0E         LDA   <$0E               ;
C1F0: 2A 17         BPL   $C209              ;
C1F2: 0A 12         DEC   <$12               ;
C1F4: 96 12         LDA   <$12               ;
C1F6: A7 84         STA   ,X                 ;
C1F8: A7 89 01 C8   STA   $01C8,X            ;
C1FC: CC 07 70      LDD   #$0770             ;
C1FF: ED 01         STD   1,X                ;
C201: ED 89 01 C9   STD   $01C9,X            ;
C205: BD C2 D0      JSR   $C2D0              ;
C208: 39            RTS                      ;
C209: 96 12         LDA   <$12               ;
C20B: A7 84         STA   ,X                 ;
C20D: A7 89 01 C8   STA   $01C8,X            ;
C211: 4C            INCA                     ;
C212: 97 12         STA   <$12               ;
C214: CC 70 07      LDD   #$7007             ;
C217: ED 01         STD   1,X                ;
C219: ED 89 01 C9   STD   $01C9,X            ;
C21D: BD C2 D0      JSR   $C2D0              ;
C220: 39            RTS                      ;
C221: 9E 05         LDX   <$05               ;
C223: 30 1D         LEAX  -3,X               ;
C225: 8C B6 FD      CMPX  #$B6FD             ;
C228: 26 03         BNE   $C22D              ;
C22A: 8E B8 C5      LDX   #$B8C5             ;
C22D: 9F 05         STX   <$05               ;
C22F: 96 0E         LDA   <$0E               ;
C231: 2A 17         BPL   $C24A              ;
C233: 0A 12         DEC   <$12               ;
C235: 96 12         LDA   <$12               ;
C237: A7 84         STA   ,X                 ;
C239: A7 89 01 C8   STA   $01C8,X            ;
C23D: CC 07 70      LDD   #$0770             ;
C240: ED 01         STD   1,X                ;
C242: ED 89 01 C9   STD   $01C9,X            ;
C246: BD C2 D0      JSR   $C2D0              ;
C249: 39            RTS                      ;
C24A: 96 12         LDA   <$12               ;
C24C: A7 84         STA   ,X                 ;
C24E: A7 89 01 C8   STA   $01C8,X            ;
C252: 4C            INCA                     ;
C253: 97 12         STA   <$12               ;
C255: CC 70 07      LDD   #$7007             ;
C258: ED 01         STD   1,X                ;
C25A: ED 89 01 C9   STD   $01C9,X            ;
C25E: BD C2 D0      JSR   $C2D0              ;
C261: 39            RTS                      ;

C262: 8E C3 50      LDX   #$C350             ;
C265: 9F 0B         STX   <$0B               ;
C267: A6 84         LDA   ,X                 ;
C269: 97 0E         STA   <$0E               ;
C26B: 86 07         LDA   #$07               ;
C26D: 97 10         STA   <$10               ;
C26F: 86 E0         LDA   #$E0               ;
C271: 97 12         STA   <$12               ;
C273: 8E B3 00      LDX   #$B300             ;
C276: 96 12         LDA   <$12               ;
C278: A7 80         STA   ,X+                ;
C27A: 96 0E         LDA   <$0E               ;
C27C: 2A 04         BPL   $C282              ;
C27E: 0A 12         DEC   <$12               ;
C280: 20 02         BRA   $C284              ;
C282: 0C 12         INC   <$12               ;
C284: BD C2 D0      JSR   $C2D0              ;
C287: 96 0E         LDA   <$0E               ;
C289: 2A 04         BPL   $C28F              ;
C28B: 0A 12         DEC   <$12               ;
C28D: 20 02         BRA   $C291              ;
C28F: 0C 12         INC   <$12               ;
C291: BD C2 D0      JSR   $C2D0              ;
C294: 8C B7 00      CMPX  #$B700             ;
C297: 26 DD         BNE   $C276              ;
C299: 39            RTS                      ;

C29A: 8E 00 00      LDX   #$0000             ;
C29D: 10 8E BE 20   LDY   #$BE20             ;
C2A1: AF B1         STX   [,Y++]             ;
C2A3: 10 8C BF 50   CMPY  #$BF50             ;
C2A7: 26 F8         BNE   $C2A1              ;
C2A9: 39            RTS                      ;

;SUBRTN
C2AA: 96 0F         LDA   <$0F               ;
C2AC: 27 0A         BEQ   $C2B8              ;
C2AE: 0A 0F         DEC   <$0F               ;
C2B0: 96 0D         LDA   <$0D               ;
C2B2: 48            ASLA                     ;
C2B3: 89 00         ADCA  #$00               ;
C2B5: 97 0D         STA   <$0D               ;
C2B7: 39            RTS                      ;
C2B8: DE 09         LDU   <$09               ;
C2BA: 33 41         LEAU  1,U                ;
C2BC: 11 83 C4 50   CMPU  #$C450             ;
C2C0: 26 03         BNE   $C2C5              ;
C2C2: CE C3 50      LDU   #$C350             ;
C2C5: DF 09         STU   <$09               ;
C2C7: 86 07         LDA   #$07               ;
C2C9: 97 0F         STA   <$0F               ;
C2CB: A6 C4         LDA   ,U                 ;
C2CD: 97 0D         STA   <$0D               ;
C2CF: 39            RTS                      ;
;SUBRTN
C2D0: 96 10         LDA   <$10               ;
C2D2: 27 0A         BEQ   $C2DE              ;
C2D4: 0A 10         DEC   <$10               ;
C2D6: 96 0E         LDA   <$0E               ;
C2D8: 48            ASLA                     ;
C2D9: 89 00         ADCA  #$00               ;
C2DB: 97 0E         STA   <$0E               ;
C2DD: 39            RTS                      ;
C2DE: DE 0B         LDU   <$0B               ;
C2E0: 33 41         LEAU  1,U                ;
C2E2: 11 83 C4 50   CMPU  #$C450             ;
C2E6: 26 03         BNE   $C2EB              ;
C2E8: CE C3 50      LDU   #$C350             ;
C2EB: DF 0B         STU   <$0B               ;
C2ED: 86 07         LDA   #$07               ;
C2EF: 97 10         STA   <$10               ;
C2F1: A6 C4         LDA   ,U                 ;
C2F3: 97 0E         STA   <$0E               ;
C2F5: 39            RTS                      ;

;SUBRTN
C2F6: 96 0F         LDA   <$0F               ;
C2F8: 81 07         CMPA  #$07               ;
C2FA: 27 0C         BEQ   $C308              ;
C2FC: 0C 0F         INC   <$0F               ;
C2FE: 96 0D         LDA   <$0D               ;
C300: 44            LSRA                     ;
C301: 24 02         BCC   $C305              ;
C303: 8B 80         ADDA  #$80               ;
C305: 97 0D         STA   <$0D               ;
C307: 39            RTS                      ;
C308: DE 09         LDU   <$09               ;
C30A: 11 83 C3 50   CMPU  #$C350             ;
C30E: 26 03         BNE   $C313              ;
C310: CE C4 50      LDU   #$C450             ;
C313: 33 5F         LEAU  -1,U               ;
C315: DF 09         STU   <$09               ;
C317: 0F 0F         CLR   <$0F               ;
C319: A6 C4         LDA   ,U                 ;
C31B: 44            LSRA                     ;
C31C: 24 02         BCC   $C320              ;
C31E: 8B 80         ADDA  #$80               ;
C320: 97 0D         STA   <$0D               ;
C322: 39            RTS                      ;

;SUBRTN
C323: 96 10         LDA   <$10               ;
C325: 81 07         CMPA  #$07               ;
C327: 27 0C         BEQ   $C335              ;
C329: 0C 10         INC   <$10               ;
C32B: 96 0E         LDA   <$0E               ;
C32D: 44            LSRA                     ;
C32E: 24 02         BCC   $C332              ;
C330: 8B 80         ADDA  #$80               ;
C332: 97 0E         STA   <$0E               ;
C334: 39            RTS                      ;
C335: DE 0B         LDU   <$0B               ;
C337: 11 83 C3 50   CMPU  #$C350             ;
C33B: 26 03         BNE   $C340              ;
C33D: CE C4 50      LDU   #$C450             ;
C340: 33 5F         LEAU  -1,U               ;
C342: DF 0B         STU   <$0B               ;
C344: 0F 10         CLR   <$10               ;
C346: A6 C4         LDA   ,U                 ;
C348: 44            LSRA                     ;
C349: 24 02         BCC   $C34D              ;
C34B: 8B 80         ADDA  #$80               ;
C34D: 97 0E         STA   <$0E               ;
C34F: 39            RTS                      ;

  ;DATA? Definitely.
C350: 2A AA         BPL   $C2FC              ;
C352: AA 
C353: AA 
C354: AA 
C355: AA AB         ORA   D,Y                ;
C357: A1 D5         CMPA  [B,U]              ;
C359: 55 
C35A: 55 
C35B: 55 
C35C: 55 
C35D: 55 
C35E: AA BF FF FF   ORA   [$FFFF]            ;
C362: FF C0 00      STU   $C000              ;
C365: 00 00         NEG   <$00               ;
C367: 55 
C368: 55 
C369: 57            ASRB                     ;
C36A: FF C0 01      STU   $C001              ;
C36D: 55 
C36E: 55 
C36F: 55 
C370: 55 
C371: 55 
C372: 55 
C373: 5F            CLRB                     ;
C374: E0 15         SUBB  -11,X              ;
C376: 55 
C377: 55 
C378: 57            ASRB                     ;
C379: FF F0 00      STU   $F000              ;
C37C: 15 
C37D: 55 
C37E: 5F            CLRB                     ;
C37F: FF FF FF      STU   $FFFF              ;
C382: FF 00 00      STU   $0000              ;
C385: 00 00         NEG   <$00               ;
C387: 05 
C388: 55 
C389: 7F FF E0      CLR   $FFE0              ;
C38C: 00 05         NEG   <$05               ;
C38E: 55 
C38F: 55 
C390: 55 
C391: 55 
C392: FC 05 55      LDD   $0555              ;
C395: 55 
C396: 50            NEGB                     ;
C397: 01 
C398: FF FF FF      STU   $FFFF              ;
C39B: C0 00         SUBB  #$00               ;
C39D: 0A AA         DEC   <$AA               ;
C39F: AA 
C3A0: AA FF 00 00   ORA   [$0000]            ;
C3A4: FF FF FF      STU   $FFFF              ;
C3A7: FF F0 00      STU   $F000              ;
C3AA: 00 1F         NEG   <$1F               ;
C3AC: E0 00         SUBB  0,X                ;
C3AE: 55 
C3AF: 55 
C3B0: 55 
C3B1: 40            NEGA                     ;
C3B2: AA 
C3B3: AA 
C3B4: AA 
C3B5: AA 
C3B6: AA 
C3B7: AA B5         ORA   [B,Y]              ;
C3B9: 57            ASRB                     ;
C3BA: AA 
C3BB: AA 
C3BC: AA F5         ORA   [B,S]              ;
C3BE: 7F D5 55      CLR   $D555              ;
C3C1: 55 
C3C2: 57            ASRB                     ;
C3C3: FF 80 07      STU   $8007              ;
C3C6: E0 7F         SUBB  -1,S               ;
C3C8: F1 55 7F      CMPB  $557F              ;
C3CB: FF FF 00      STU   $FF00              ;
C3CE: 00 00         NEG   <$00               ;
C3D0: 00 00         NEG   <$00               ;
C3D2: 0F EF         CLR   <$EF               ;
C3D4: 76 91 11      ROR   $9111              ;
C3D7: 11 
C3D8: 5E 
C3D9: DB E9         ADDB  <$E9               ;
C3DB: 84 77         ANDA  #$77               ;
C3DD: EC C4         LDD   ,U                 ;
C3DF: 87 
C3E0: 47            ASRA                     ;
C3E1: 98 08         EORA  <$08               ;
C3E3: 98 3F         EORA  <$3F               ;
C3E5: C3 CB DB      ADDD  #$CBDB             ;
C3E8: 9F C7         STX   <$C7               ;
C3EA: 5F            CLRB                     ;
C3EB: 2F C7         BLE   $C3B4              ;
C3ED: 7D EF BF      TST   $EFBF              ;
C3F0: FA 4C 57      ORB   $4C57              ;
C3F3: 2B 61         BMI   $C456              ;
C3F5: EF 
C3F6: EF FB         STU   [D,S]              ;
C3F8: F7 E8 00      STB   $E800              ;
C3FB: 20 40         BRA   $C43D              ;
C3FD: 00 14         NEG   <$14               ;
C3FF: 04 04         LSR   <$04               ;
C401: 3C 06         CWAI  $06                ;
C403: 00 1D         NEG   <$1D               ;
C405: 07 3C         ASR   <$3C               ;
C407: E1 A5         CMPB  B,Y                ;
C409: 55 
C40A: 55 
C40B: 45 
C40C: 2A AA         BPL   $C3B8              ;
C40E: AA 
C40F: AA A8 55      ORA   $55,Y              ;
C412: 55 
C413: 55 
C414: 55 
C415: 55 
C416: 55 
C417: 55 
C418: 55 
C419: 55 
C41A: 55 
C41B: 56            RORB                     ;
C41C: AA 
C41D: AA 
C41E: FE AA AA      LDU   $AAAA              ;
C421: AA 
C422: AA 
C423: AA 
C424: AA 
C425: AA 
C426: AA 
C427: EA 
C428: AA 
C429: AA A8 02      ORA   $02,Y              ;
C42C: AA 
C42D: AA 
C42E: AA 
C42F: AA BF BE 3E   ORA   [$BE3E]            ;
C433: 63 FF E0 D8   COM   [$E0D8]            ;
C437: 1C 18         ANDCC #$18               ;
C439: 2A AB         BPL   $C3E6              ;
C43B: 1E 77         EXG   ?,?                ;
C43D: 7A AF A8      DEC   $AFA8              ;
C440: 40            NEGA                     ;
C441: 70 7D 40      NEG   $7D40              ;
C444: 0B 
C445: FB FA FF      ADDB  $FAFF              ;
C448: C1 53         CMPB  #$53               ;
C44A: 54            LSRB                     ;
C44B: 75 
C44C: 70 03 00      NEG   $0300              ;
C44F: 00 25         NEG   <$25               ;
C451: 70 07 26      NEG   $0726              ;
C454: 77 00 26      ASR   $0026              ;
C457: 07 70         ASR   <$70               ;
C459: 24 07         BCC   $C462              ;
C45B: 70 23 07      NEG   $2307              ;
C45E: 70 23 70      NEG   $2370              ;
C461: 07 24         ASR   <$24               ;
C463: 07 70         ASR   <$70               ;
C465: 25 70         BCS   $C4D7              ;
C467: 07 26         ASR   <$26               ;
C469: 77 00 25      ASR   $0025              ;
C46C: 07 70         ASR   <$70               ;
C46E: 24 07         BCC   $C477              ;
C470: 70 23 07      NEG   $2307              ;
C473: 70 21 07      NEG   $2107              ;
C476: 70 22 70      NEG   $2270              ;
C479: 07 24         ASR   <$24               ;
C47B: 77 00 24      ASR   $0024              ;
C47E: 70 07 26      NEG   $0726              ;
C481: 77 00 26      ASR   $0026              ;
C484: 77 00 25      ASR   $0025              ;
C487: 77 00 25      ASR   $0025              ;
C48A: 70 07 26      NEG   $0726              ;
C48D: 77 00 24      ASR   $0024              ;
C490: 07 70         ASR   <$70               ;
C492: 23 70         BLS   $C504              ;
C494: 07 25         ASR   <$25               ;
C496: 77 00 26      ASR   $0026              ;
C499: 70 07 26      NEG   $0726              ;
C49C: 77 00 26      ASR   $0026              ;
C49F: 77 00 25      ASR   $0025              ;
C4A2: 07 70         ASR   <$70               ;
C4A4: 23 07         BLS   $C4AD              ;
C4A6: 70 22 07      NEG   $2207              ;
C4A9: 70 21 77      NEG   $2177              ;
C4AC: 00 21         NEG   <$21               ;
C4AE: 70 07 23      NEG   $0723              ;
C4B1: 70 07 25      NEG   $0725              ;
C4B4: 70 07 25      NEG   $0725              ;
C4B7: 07 70         ASR   <$70               ;
C4B9: 25 77         BCS   $C532              ;
C4BB: 00 25         NEG   <$25               ;
C4BD: 77 00 24      ASR   $0024              ;
C4C0: 77 00 22      ASR   $0022              ;
C4C3: 07 70         ASR   <$70               ;
C4C5: 20 07         BRA   $C4CE              ;
C4C7: 70 1E 07      NEG   $1E07              ;
C4CA: 70 1C 07      NEG   $1C07              ;
C4CD: 70 1D 70      NEG   $1D70              ;
C4D0: 07 1F         ASR   <$1F               ;
C4D2: 70 07 21      NEG   $0721              ;
C4D5: 70 07 22      NEG   $0722              ;
C4D8: 70 07 24      NEG   $0724              ;
C4DB: 70 07 26      NEG   $0726              ;
C4DE: 70 07 26      NEG   $0726              ;
C4E1: 77 00 26      ASR   $0026              ;
C4E4: 77 00 26      ASR   $0026              ;
C4E7: 77 00 26      ASR   $0026              ;
C4EA: 77 00 26      ASR   $0026              ;
C4ED: 77 00 25      ASR   $0025              ;
C4F0: 77 00 25      ASR   $0025              ;
C4F3: 70 07 26      NEG   $0726              ;
C4F6: 77 00 24      ASR   $0024              ;
C4F9: 07 70         ASR   <$70               ;
C4FB: 23 77         BLS   $C574              ;
C4FD: 00 24         NEG   <$24               ;
C4FF: 77 00 22      ASR   $0022              ;
C502: 07 70         ASR   <$70               ;
C504: 23 70         BLS   $C576              ;
C506: 07 22         ASR   <$22               ;
C508: 07 70         ASR   <$70               ;
C50A: 21 70         BRN   $C57C              ;
C50C: 07 23         ASR   <$23               ;
C50E: 70 07 25      NEG   $0725              ;
C511: 70 07 26      NEG   $0726              ;
C514: 77 00 26      ASR   $0026              ;
C517: 07 70         ASR   <$70               ;
C519: 24 07         BCC   $C522              ;
C51B: 70 23 07      NEG   $2307              ;
C51E: 70 23 70      NEG   $2370              ;
C521: 07 24         ASR   <$24               ;
C523: 07 70         ASR   <$70               ;
C525: 25 70         BCS   $C597              ;
C527: 07 26         ASR   <$26               ;
C529: 77 00 25      ASR   $0025              ;
C52C: 07 70         ASR   <$70               ;
C52E: 24 07         BCC   $C537              ;
C530: 70 23 07      NEG   $2307              ;
C533: 70 21 07      NEG   $2107              ;
C536: 70 22 70      NEG   $2270              ;
C539: 07 24         ASR   <$24               ;
C53B: 77 00 24      ASR   $0024              ;
C53E: 70 07 26      NEG   $0726              ;
C541: 77 00 26      ASR   $0026              ;
C544: 77 00 25      ASR   $0025              ;
C547: 77 00 25      ASR   $0025              ;
C54A: 70 07 26      NEG   $0726              ;
C54D: 77 00 24      ASR   $0024              ;
C550: 07 70         ASR   <$70               ;
C552: 23 70         BLS   $C5C4              ;
C554: 07 25         ASR   <$25               ;
C556: 77 00 26      ASR   $0026              ;
C559: 70 07 26      NEG   $0726              ;
C55C: 77 00 26      ASR   $0026              ;
C55F: 77 00 25      ASR   $0025              ;
C562: 07 70         ASR   <$70               ;
C564: 23 07         BLS   $C56D              ;
C566: 70 22 07      NEG   $2207              ;
C569: 70 21 77      NEG   $2177              ;
C56C: 00 21         NEG   <$21               ;
C56E: 70 07 23      NEG   $0723              ;
C571: 70 07 25      NEG   $0725              ;
C574: 70 07 25      NEG   $0725              ;
C577: 07 70         ASR   <$70               ;
C579: 25 77         BCS   $C5F2              ;
C57B: 00 25         NEG   <$25               ;
C57D: 77 00 24      ASR   $0024              ;
C580: 77 00 22      ASR   $0022              ;
C583: 07 70         ASR   <$70               ;
C585: 20 07         BRA   $C58E              ;
C587: 70 1E 07      NEG   $1E07              ;
C58A: 70 1C 07      NEG   $1C07              ;
C58D: 70 1D 70      NEG   $1D70              ;
C590: 07 1F         ASR   <$1F               ;
C592: 70 07 21      NEG   $0721              ;
C595: 70 07 22      NEG   $0722              ;
C598: 70 07 24      NEG   $0724              ;
C59B: 70 07 26      NEG   $0726              ;
C59E: 70 07 26      NEG   $0726              ;
C5A1: 77 00 26      ASR   $0026              ;
C5A4: 77 00 26      ASR   $0026              ;
C5A7: 77 00 26      ASR   $0026              ;
C5AA: 77 00 26      ASR   $0026              ;
C5AD: 77 00 25      ASR   $0025              ;
C5B0: 77 00 25      ASR   $0025              ;
C5B3: 70 07 26      NEG   $0726              ;
C5B6: 77 00 24      ASR   $0024              ;
C5B9: 07 70         ASR   <$70               ;
C5BB: 23 77         BLS   $C634              ;
C5BD: 00 24         NEG   <$24               ;
C5BF: 77 00 22      ASR   $0022              ;
C5C2: 07 70         ASR   <$70               ;
C5C4: 23 70         BLS   $C636              ;
C5C6: 07 22         ASR   <$22               ;
C5C8: 07 70         ASR   <$70               ;
C5CA: 21 70         BRN   $C63C              ;
C5CC: 07 23         ASR   <$23               ;
C5CE: 70 07

;SUBRTN
C5D0: 35 06         PULS  A,B                ;
C5D2: ED 49         STD   9,U                ;
C5D4: 9F 00         STX   <$00               ;
C5D6: CC 08 08      LDD   #$0808             ;
C5D9: DD 04         STD   <$04               ;
C5DB: CC 17 32      LDD   #$1732             ;
C5DE: DD 06         STD   <$06               ;
C5E0: 10 8E B3 00   LDY   #$B300             ;
C5E4: 96 00         LDA   <$00               ;
C5E6: 5F            CLRB                     ;
C5E7: ED 22         STD   2,Y                ;
C5E9: 96 01         LDA   <$01               ;
C5EB: ED 24         STD   4,Y                ;
C5ED: 96 05         LDA   <$05               ;
C5EF: 44            LSRA                     ;
C5F0: 98 05         EORA  <$05               ;
C5F2: 44            LSRA                     ;
C5F3: 44            LSRA                     ;
C5F4: 06 04         ROR   <$04               ;
C5F6: 06 05         ROR   <$05               ;
C5F8: 96 04         LDA   <$04               ;
C5FA: 84 01         ANDA  #$01               ;
C5FC: 80 01         SUBA  #$01               ;
C5FE: D6 05         LDB   <$05               ;
C600: ED 26         STD   6,Y                ;
C602: 2A 02         BPL   $C606              ;
C604: 43            COMA                     ;
C605: 53            COMB                     ;
C606: 34 06         PSHS  B,A                ;
C608: 96 07         LDA   <$07               ;
C60A: 44            LSRA                     ;
C60B: 98 07         EORA  <$07               ;
C60D: 44            LSRA                     ;
C60E: 44            LSRA                     ;
C60F: 06 06         ROR   <$06               ;
C611: 06 07         ROR   <$07               ;
C613: 96 06         LDA   <$06               ;
C615: 84 03         ANDA  #$03               ;
C617: 80 02         SUBA  #$02               ;
C619: D6 07         LDB   <$07               ;
C61B: ED 28         STD   8,Y                ;
C61D: 2A 02         BPL   $C621              ;
C61F: 43            COMA                     ;
C620: 53            COMB                     ;
C621: 44            LSRA                     ;
C622: 56            RORB                     ;
C623: E3 E1         ADDD  ,S++               ;
C625: 10 83 01 6A   CMPD  #$016A             ;
C629: 24 B9         BCC   $C5E4              ;
C62B: 8E 00 00      LDX   #$0000             ;
C62E: AF A4         STX   ,Y                 ;
C630: 31 2A         LEAY  10,Y               ;
C632: 10 8C B8 00   CMPY  #$B800             ;
C636: 26 AC         BNE   $C5E4              ;
C638: 8E C6 AB      LDX   #$C6AB             ;
C63B: 9F 02         STX   <$02               ;
C63D: 86 38         LDA   #$38               ;
C63F: 97 01         STA   <$01               ;
C641: 86 01         LDA   #$01               ;
C643: 8E C6 49      LDX   #$C649             ;
C646: 7E FF D1      JMP   InsEventLnkPgSavX  ;
C649: 8E 00 00      LDX   #$0000             ;
C64C: 10 8E B3 00   LDY   #$B300             ;
C650: A6 9F A0 02   LDA   [$A002]            ;
C654: 97 31         STA   <$31               ;
C656: 27 50         BEQ   $C6A8              ;
C658: EE A4         LDU   ,Y                 ;
C65A: AF C4         STX   ,U                 ;
C65C: AF C9 01 00   STX   $0100,U            ;
C660: EC 28         LDD   8,Y                ;
C662: E3 24         ADDD  4,Y                ;
C664: 81 2A         CMPA  #$2A               ;
C666: 25 28         BCS   $C690              ;
C668: ED 24         STD   4,Y                ;
C66A: A7 21         STA   1,Y                ;
C66C: EC 26         LDD   6,Y                ;
C66E: E3 22         ADDD  2,Y                ;
C670: 81 98         CMPA  #$98               ;
C672: 22 1C         BHI   $C690              ;
C674: ED 22         STD   2,Y                ;
C676: A7 A4         STA   ,Y                 ;
C678: 5D            TSTB                     ;
C679: 2B 07         BMI   $C682              ;
C67B: CC BB BB      LDD   #$BBBB             ;
C67E: ED B4         STD   [,Y]               ;
C680: 20 0E         BRA   $C690              ;
C682: EE A4         LDU   ,Y                 ;
C684: CC 0B 0B      LDD   #$0B0B             ;
C687: ED C4         STD   ,U                 ;
C689: CC B0 B0      LDD   #$B0B0             ;
C68C: ED C9 01 00   STD   $0100,U            ;
C690: 31 2A         LEAY  10,Y               ;
C692: 10 8C B8 00   CMPY  #$B800             ;
C696: 26 C0         BNE   $C658              ;
C698: 0A 01         DEC   <$01               ;
C69A: 26 A5         BNE   $C641              ;
C69C: DE 02         LDU   <$02               ;
C69E: 33 41         LEAU  1,U                ;
C6A0: DF 02         STU   <$02               ;
C6A2: 86 04         LDA   #$04               ;
C6A4: 97 01         STA   <$01               ;
C6A6: 20 99         BRA   $C641              ;
C6A8: 6E D8 09      JMP   [$09,U]            ;

  ;DATA? Seems likely.
C6AB: FF 7F 3F      STU   $7F3F              ;
C6AE: 37 2F         PULU  CC,A,B,DP,Y        ;
C6B0: 27 1F         BEQ   $C6D1              ;
C6B2: 17 07 06      LBSR  $CDBB              ;???
C6B5: 05 
C6B6: 04 03         LSR   <$03               ;
C6B8: 02 
C6B9: 00 14         NEG   <$14               ;
C6BB: 00 00         NEG   <$00               ;
C6BD: 00 0F         NEG   <$0F               ;
C6BF: 14 
C6C0: 14 
C6C1: 14 
C6C2: 03 00         COM   <$00               ;
C6C4: 00 00         NEG   <$00               ;
C6C6: 00 03         NEG   <$03               ;
C6C8: 04 05         LSR   <$05               ;
C6CA: 06 00         ROR   <$00               ;
C6CC: 00 00         NEG   <$00               ;
C6CE: 00 01         NEG   <$01               ;
C6D0: 03 04         COM   <$04               ;
C6D2: 0A 00         DEC   <$00               ;
C6D4: 00 00         NEG   <$00               ;
C6D6: 00 00         NEG   <$00               ;
C6D8: 00 00         NEG   <$00               ;
C6DA: 0A 00         DEC   <$00               ;
C6DC: 00 00         NEG   <$00               ;
C6DE: 00 00         NEG   <$00               ;
C6E0: 00 00         NEG   <$00               ;
C6E2: 1E 00         EXG   D,D                ;
C6E4: 00 00         NEG   <$00               ;
C6E6: 1E 19         EXG   X,B                ;
C6E8: 14 
C6E9: 10 
C6EA: 05 
C6EB: 00 00         NEG   <$00               ;
C6ED: 00 05         NEG   <$05               ;
C6EF: 05 
C6F0: 05 
C6F1: 05 
C6F2: 60 00         NEG   0,X                ;
C6F4: 03 02         COM   <$02               ;
C6F6: 16 1E 26      LBRA  $E51F              ;
C6F9: 2E 01         BGT   $C6FC              ;
C6FB: 00 00         NEG   <$00               ;
C6FD: 00 00         NEG   <$00               ;
C6FF: 00 01         NEG   <$01               ;
C701: 01 
C702: FF 00 10      STU   $0010              ;
C705: 00 70         NEG   <$70               ;
C707: B0 00 00      SUBA  $0000              ;
C70A: 80 10         SUBA  #$10               ;
C70C: FC FE 4A      LDD   $FE4A              ;
C70F: 3A            ABX                      ;
C710: 2A 2A         BPL   $C73C              ;
C712: 30 00         LEAX  0,X                ;
C714: 00 00         NEG   <$00               ;
C716: 20 28         BRA   $C740              ;
C718: 2C 30         BGE   $C74A              ;
C71A: 02 
C71B: 00 00         NEG   <$00               ;
C71D: 00 01         NEG   <$01               ;
C71F: 01 
C720: 02 
C721: 02 
C722: 01 
C723: 00 00         NEG   <$00               ;
C725: 00 00         NEG   <$00               ;
C727: 00 01         NEG   <$01               ;
C729: 01 
C72A: FF 00 08      STU   $0008              ;
C72D: 06 62         ROR   <$62               ;
C72F: E0 02         SUBB  2,X                ;
C731: 12            NOP                      ;
C732: 60 00         NEG   0,X                ;
C734: 08 04         LSL   <$04               ;
C736: 0C 1C         INC   <$1C               ;
C738: 24 28         BCC   $C762              ;
C73A: FF 08 FE      STU   $08FE              ;
C73D: FE 2A 22      LDU   $2A22              ;
C740: 1E 1C         EXG   X,?                ;
C742: 60 00         NEG   0,X                ;
C744: 08 02         LSL   <$02               ;
C746: 16 1E 20      LBRA  $E569              ;
C749: 22 28         BHI   $C773              ;
C74B: 0A FE         DEC   <$FE               ;
C74D: FF 19 19      STU   $1919              ;
C750: 19            DAA                      ;
C751: 19            DAA                      ;
C752: 3F            SWI                      ;
C753: 00 00         NEG   <$00               ;
C755: 00 1F         NEG   <$1F               ;
C757: 1F 1F         TFR   X,?                ;
C759: 3F            SWI                      ;
C75A: C0 18         SUBB  #$18               ;
C75C: F4 FC D4      ANDB  $FCD4              ;
C75F: C4 A4         ANDB  #$A4               ;
C761: 94 0A         ANDA  <$0A               ;
C763: 03 FF         COM   <$FF               ;
C765: FF 0F 0D      STU   $0F0D              ;
C768: 0C 0A         INC   <$0A               ;
C76A: C8 28         EORB  #$28               ;
C76C: F4 F8 F0      ANDB  $F8F0              ;
C76F: DC C8         LDD   <$C8               ;
C771: C8 00         EORB  #$00               ;
C773: 00 00         NEG   <$00               ;
C775: 00 00         NEG   <$00               ;
C777: 00 03         NEG   <$03               ;
C779: 8E C0 0C      LDX   #$C00C             ;
C77C: 7E C0 36      JMP   $C036              ;
C77F: C6 28         LDB   #$28               ;
C781: 20 F1         BRA   $C774              ;
C783: C6 80         LDB   #$80               ;
C785: 20 ED         BRA   $C774              ;
C787: 10 8E C9 FE   LDY   #$C9FE             ;
C78B: BD CA 97      JSR   $CA97              ;
C78E: 7E CB 3B      JMP   $CB3B              ;
C791: C6 A5         LDB   #$A5               ;
C793: 8E C0 01      LDX   #$C001             ;
C796: 7E C0 36      JMP   $C036              ;
C799: BD CA 69      JSR   $CA69              ;
C79C: BD CA 2A      JSR   $CA2A              ;
C79F: 8D F0         BSR   $C791              ;
C7A1: CE C0 D7      LDU   #$C0D7             ;
C7A4: 8E 28 20      LDX   #$2820             ;
C7A7: BD CA 69      JSR   $CA69              ;
C7AA: BD C0 3C      JSR   $C03C              ;
C7AD: 10 8E C0 61   LDY   #$C061             ;
C7B1: BD C0 6D      JSR   $C06D              ;
C7B4: 10 8E 05 DC   LDY   #$05DC             ;
C7B8: BD CA 44      JSR   $CA44              ;
C7BB: 0D 49         TST   <$49               ;
C7BD: 26 60         BNE   $C81F              ;
C7BF: 0F 3C         CLR   <$3C               ;
C7C1: 86 01         LDA   #$01               ;
C7C3: 97 3B         STA   <$3B               ;
C7C5: 32 E8 E0      LEAS  $-20,S             ;
C7C8: BD FF BC      JSR   $FFBC              ;
C7CB: CE C0 D7      LDU   #$C0D7             ;
C7CE: 8E 28 20      LDX   #$2820             ;
C7D1: BD CA 69      JSR   $CA69              ;
C7D4: BD C0 3C      JSR   $C03C              ;
C7D7: 0F 3A         CLR   <$3A               ;
C7D9: 10 8E C0 65   LDY   #$C065             ;
C7DD: BD C0 66      JSR   $C066              ;
C7E0: BD CA 69      JSR   $CA69              ;
C7E3: 86 20         LDA   #$20               ;
C7E5: 1F 89         TFR   A,B                ;
C7E7: 5A            DECB                     ;
C7E8: 30 E4         LEAX  ,S                 ;
C7EA: A7 80         STA   ,X+                ;
C7EC: 5A            DECB                     ;
C7ED: 26 FB         BNE   $C7EA              ;
C7EF: 86 17         LDA   #$17               ;
C7F1: A7 80         STA   ,X+                ;
C7F3: 30 E4         LEAX  ,S                 ;
C7F5: BD CA 57      JSR   $CA57              ;
C7F8: 8E CC 00      LDX   #$CC00             ;
C7FB: BD C0 39      JSR   $C039              ;
C7FE: C5 02         BITB  #$02               ;
```
