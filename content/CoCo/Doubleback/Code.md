
 ```
C000: 0F BB           CLR     $BB                   ; First RESET comes here ???
C002: 0F BC           CLR     $BC                   ; ???
C004: 12              NOP                         ; Required by RESET handler
C005: 1A 50           ORCC    #$50                  
C007: 10 CE 01 50     LDS     #$0150                  
C00B: 30 8C F6        LEAX    $C004,PC                ; RESET button ...
C00E: 9F 72           STX     $72                   ; ... now comes to C004
C010: 8E 03 80        LDX     #$0380                  
C013: 5F              CLRB                        
C014: 34 04           PSHS    $04                   
C016: A6 E4           LDA     ,S                  
C018: E6 E4           LDB     ,S                  
C01A: C4 AA           ANDB    #$AA                  
C01C: 54              LSRB                        
C01D: E7 86           STB     A,X                 
C01F: E6 E4           LDB     ,S                  
C021: C4 55           ANDB    #$55                  
C023: 58              LSRB
C024: EA 86           ORB     A,X                 
C026: EA E4           ORB     ,S                  
C028: 53              COMB                        
C029: E7 86           STB     A,X                 
C02B: 6C E4           INC     ,S                  
C02D: 26 E7           BNE     $C016                   
C02F: 35 04           PULS    $04                   
C031: 17 0A 1E        LBSR    $0A1E                   
C034: 17 0A 98        LBSR    $0A98                   
C037: CC 1C 46        LDD     #$1C46                  
C03A: 33 8D 0D 33     LEAU    $CD71,PC                
C03E: 17 09 02        LBSR    $0902                   
C041: CC 14 4E        LDD     #$144E                  
C044: 33 8D 0D 3A     LEAU    $CD82,PC                
C048: 17 08 F8        LBSR    $08F8                   
C04B: CC 14 56        LDD     #$1456                  
C04E: 33 8D 0D D1     LEAU    $CE23,PC                
C052: 17 08 EE        LBSR    $08EE                   
C055: 8E 00 E4        LDX     #$00E4                  
C058: 86 1F           LDA     #$1F                  
C05A: A7 84           STA     ,X                  
C05C: 86 18           LDA     #$18                  
C05E: A7 02           STA     2,X                 
C060: 33 8D 0E 5F     LEAU    $CEC3,PC                
C064: 34 04           PSHS    $04                   
C066: C6 05           LDB     #$05                  
C068: E7 E4           STB     ,S                  
C06A: EC C1           LDD     ,U++                
C06C: 27 42           BEQ     $C0B0                   
C06E: 34 06           PSHS    $06                   
C070: C4 07           ANDB    #$07                  
C072: 58              LSRB
C073: 31 8D 0E B6     LEAY    $CF2D,PC                
C077: EC A5           LDD     B,Y                 
C079: AB 84           ADDA    ,X                  
C07B: EB 02           ADDB    2,X                 
C07D: A7 84           STA     ,X                  
C07F: E7 02           STB     2,X                 
C081: 40              NEGA                        
C082: 8B 80           ADDA    #$80                  
C084: A7 01           STA     1,X                 
C086: 50              NEGB                        
C087: CB 3C           ADDB    #$3C                  
C089: E7 03           STB     3,X                 
C08B: 34 50           PSHS    $50                   
C08D: 17 08 CF        LBSR    $08CF                   
C090: 30 01           LEAX    1,X                 
C092: 17 08 CA        LBSR    $08CA                   
C095: E6 84           LDB     ,X                  
C097: C4 01           ANDB    #$01                  
C099: 26 03           BNE     $C09E                   
C09B: 17 0A 51        LBSR    $0A51                   
C09E: 35 50           PULS    $50                   
C0A0: 35 06           PULS    $06                   
C0A2: 6A E4           DEC     ,S                  
C0A4: 27 C0           BEQ     $C066                   
C0A6: 44              LSRA                        
C0A7: 56              RORB                        
C0A8: 44              LSRA                        
C0A9: 56              RORB                        
C0AA: 44              LSRA                        
C0AB: 56              RORB                        
C0AC: 34 06           PSHS    $06                   
C0AE: 20 C0           BRA     $C070                   
C0B0: 35 04           PULS    $04                   
C0B2: CC 28 3A        LDD     #$283A                  
C0B5: 33 8D 0C 57     LEAU    $CD10,PC                
C0B9: 17 08 87        LBSR    $0887                   
C0BC: AD 9F A0 0A     JSR     [$A00A]                 
C0C0: 0F B4           CLR     $B4                   
C0C2: CE 0C 2A        LDU     #$0C2A                  
C0C5: 6F C4           CLR     ,U                  
C0C7: 6F 43           CLR     3,U                 
C0C9: B6 01 5A        LDA     $015A                   
C0CC: 81 1F           CMPA    #$1F                  
C0CE: 2F 04           BLE     $C0D4                   
C0D0: 0C B4           INC     $B4                   
C0D2: 33 43           LEAU    3,U                 
C0D4: 6A C4           DEC     ,U                  
C0D6: 17 0A 16        LBSR    $0A16                   
C0D9: F6 FF 00        LDB     $FF00                   
C0DC: C4 01           ANDB    #$01                  
C0DE: 26 DC           BNE     $C0BC                   
C0E0: 0F B7           CLR     $B7                   
C0E2: 0F B8           CLR     $B8                   
C0E4: 0F B9           CLR     $B9                   
C0E6: 0F BA           CLR     $BA                   
C0E8: C6 03           LDB     #$03                  
C0EA: D7 B5           STB     $B5                   
C0EC: 0F B6           CLR     $B6                   
C0EE: 17 00 3E        LBSR    $003E                   
C0F1: 0D B4           TST     $B4                   
C0F3: 27 05           BEQ     $C0FA                   
C0F5: 0C B6           INC     $B6                   
C0F7: 17 00 35        LBSR    $0035                   
C0FA: 0A B5           DEC     $B5                   
C0FC: 26 EE           BNE     $C0EC                   
C0FE: DC B7           LDD     $B7                   
C100: 10 93 BB        CMPD    $BB                   
C103: 23 02           BLS     $C107                   
C105: DD BB           STD     $BB                   
C107: DC B9           LDD     $B9                   
C109: 10 93 BB        CMPD    $BB                   
C10C: 23 02           BLS     $C110                   
C10E: DD BB           STD     $BB                   
C110: DC BB           LDD     $BB                   
C112: CE 04 EE        LDU     #$04EE                  
C115: 17 05 13        LBSR    $0513                   
C118: CC 2C 28        LDD     #$2C28                  
C11B: 33 8D 0B A0     LEAU    $CCBF,PC                
C11F: 17 08 21        LBSR    $0821                   
C122: 17 09 9B        LBSR    $099B                   
C125: F6 FF 00        LDB     $FF00                   
C128: C4 01           ANDB    #$01                  
C12A: 26 F6           BNE     $C122                   
C12C: 16 FF 02        LBRA    $C031                   
C12F: C6 FF           LDB     #$FF                  
C131: 17 09 1F        LBSR    $091F                   
C134: 0F BE           CLR     $BE                   
C136: 0F D1           CLR     $D1                   
C138: 0F CE           CLR     $CE                   
C13A: 0F D0           CLR     $D0                   
C13C: 0F C7           CLR     $C7                   
C13E: 0F D6           CLR     $D6                   
C140: 0F CF           CLR     $CF                   
C142: C6 28           LDB     #$28                  
C144: D7 D5           STB     $D5                   
C146: CC 2C 28        LDD     #$2C28                  
C149: 33 8D 0A FF     LEAU    $CC4C,PC                
C14D: 17 07 F3        LBSR    $07F3                   
C150: CC 44 28        LDD     #$4428                  
C153: 33 8D 0B 26     LEAU    $CC7D,PC                
C157: 0D B6           TST     $B6                   
C159: 27 06           BEQ     $C161                   
C15B: 86 46           LDA     #$46                  
C15D: 33 8D 0B 3D     LEAU    $CC9E,PC                
C161: 17 07 DF        LBSR    $07DF                   
C164: D6 B5           LDB     $B5                   
C166: 33 8D 0E 1B     LEAU    $CF85,PC                
C16A: 5A              DECB                        
C16B: 27 0B           BEQ     $C178                   
C16D: 33 8D 0D F0     LEAU    $CF61,PC                
C171: 5A              DECB                        
C172: 27 04           BEQ     $C178                   
C174: 33 8D 0D C5     LEAU    $CF3D,PC                
C178: 17 09 03        LBSR    $0903                   
C17B: 17 08 E5        LBSR    $08E5                   
C17E: C6 02           LDB     #$02                  
C180: 34 04           PSHS    $04                   
C182: 8E 00 E4        LDX     #$00E4                  
C185: C1 56           CMPB    #$56                  
C187: 2E 12           BGT     $C19B                   
C189: E7 02           STB     2,X                 
C18B: C6 02           LDB     #$02                  
C18D: E7 84           STB     ,X                  
C18F: 17 07 CD        LBSR    $07CD                   
C192: C6 7E           LDB     #$7E                  
C194: E7 84           STB     ,X                  
C196: 17 07 C6        LBSR    $07C6                   
C199: E6 02           LDB     2,X                 
C19B: E7 84           STB     ,X                  
C19D: C6 02           LDB     #$02                  
C19F: E7 02           STB     2,X                 
C1A1: 17 07 BB        LBSR    $07BB                   
C1A4: C6 56           LDB     #$56                  
C1A6: E7 02           STB     2,X                 
C1A8: 17 07 B4        LBSR    $07B4                   
C1AB: 6C E4           INC     ,S                  
C1AD: E6 E4           LDB     ,S                  
C1AF: C1 7E           CMPB    #$7E                  
C1B1: 23 CF           BLS     $C182                   
C1B3: 35 04           PULS    $04                   
C1B5: 4F              CLRA                        
C1B6: C6 58           LDB     #$58                  
C1B8: 33 8D 0A 90     LEAU    $CC4C,PC                
C1BC: 17 07 84        LBSR    $0784                   
C1BF: CC 18 58        LDD     #$1858                  
C1C2: 33 8D 0A B7     LEAU    $CC7D,PC                
C1C6: 17 07 7A        LBSR    $077A                   
C1C9: 0D B4           TST     $B4                   
C1CB: 27 0A           BEQ     $C1D7                   
C1CD: CC 52 58        LDD     #$5258                  
C1D0: 33 8D 0A CA     LEAU    $CC9E,PC                
C1D4: 17 07 6C        LBSR    $076C                   
C1D7: 17 04 36        LBSR    $0436                   
C1DA: 8E 00 E4        LDX     #$00E4                  
C1DD: 6F 02           CLR     2,X                 
C1DF: C6 33           LDB     #$33                  
C1E1: E7 84           STB     ,X                  
C1E3: 33 8D 0A 33     LEAU    $CC1A,PC                
C1E7: D6 B5           LDB     $B5                   
C1E9: C1 03           CMPB    #$03                  
C1EB: 27 04           BEQ     $C1F1                   
C1ED: 33 8D 0A 19     LEAU    $CC0A,PC                
C1F1: 17 05 69        LBSR    $0569                   
C1F4: C6 3D           LDB     #$3D                  
C1F6: E7 84           STB     ,X                  
C1F8: 33 8D 0A 1E     LEAU    $CC1A,PC                
C1FC: D6 B5           LDB     $B5                   
C1FE: C1 02           CMPB    #$02                  
C200: 27 04           BEQ     $C206                   
C202: 33 8D 0A 04     LEAU    $CC0A,PC                
C206: 17 05 54        LBSR    $0554                   
C209: C6 47           LDB     #$47                  
C20B: E7 84           STB     ,X                  
C20D: 33 8D 0A 09     LEAU    $CC1A,PC                
C211: D6 B5           LDB     $B5                   
C213: C1 01           CMPB    #$01                  
C215: 27 04           BEQ     $C21B                   
C217: 33 8D 09 EF     LEAU    $CC0A,PC                
C21B: 17 05 3F        LBSR    $053F                   
C21E: 8E 00 D8        LDX     #$00D8                  
C221: 86 40           LDA     #$40                  
C223: A7 84           STA     ,X                  
C225: A7 02           STA     2,X                 
C227: 8E 02 00        LDX     #$0200                  
C22A: 5F              CLRB                        
C22B: A7 80           STA     ,X+                 
C22D: 5A              DECB                        
C22E: 26 FB           BNE     $C22B                   
C230: 8E 01 60        LDX     #$0160                  
C233: C6 A0           LDB     #$A0                  
C235: 6F 80           CLR     ,X+                 
C237: 5A              DECB                        
C238: 26 FB           BNE     $C235                   
C23A: 0F BD           CLR     $BD                   
C23C: 17 00 16        LBSR    $0016                   
C23F: 0D BD           TST     $BD                   
C241: 27 F9           BEQ     $C23C                   
C243: C6 F0           LDB     #$F0                  
C245: F7 FF 22        STB     $FF22                   
C248: 33 8D 0D 59     LEAU    $CFA5,PC                
C24C: 17 08 2F        LBSR    $082F                   
C24F: C6 F8           LDB     #$F8                  
C251: F7 FF 22        STB     $FF22                   
C254: 39              RTS                         
C255: 17 08 68        LBSR    $0868                   
C258: 8E 02 00        LDX     #$0200                  
C25B: D6 BE           LDB     $BE                   
C25D: 3A              ABX                         
C25E: EC 84           LDD     ,X                  
C260: 8E 00 DE        LDX     #$00DE                  
C263: A7 84           STA     ,X                  
C265: E7 02           STB     2,X                 
C267: 17 07 48        LBSR    $0748                   
C26A: 17 07 29        LBSR    $0729                   
C26D: 0C D4           INC     $D4                   
C26F: 8E 01 60        LDX     #$0160                  
C272: 6D 06           TST     6,X                 
C274: 10 27 01 17     LBEQ    $C38F                   
C278: 30 08           LEAX    8,X                 
C27A: 1F 10           TFR     $10                   
C27C: 54              LSRB                        
C27D: 54              LSRB                        
C27E: 54              LSRB                        
C27F: DB D4           ADDB    $D4                   
C281: C4 07           ANDB    #$07                  
C283: 26 ED           BNE     $C272                   
C285: 30 18           LEAX    -8,X                
C287: E6 06           LDB     6,X                 ; Object type
C289: 5A              DECB                        ; 1=APPLE?
C28A: 26 0A           BNE     $C296               ; No ... check other types    
C28C: 33 8D 08 6A     LEAU    $CAFA,PC            ; Apple graphic
C290: 17 04 CA        LBSR    $04CA               ; Draw apple    
C293: 16 00 F0        LBRA    $C386               ; Next object
;
C296: 5A              DECB                        ; 2=CHERRY
C297: 26 0A           BNE     $C2A3               ; No ... check other types
C299: 33 8D 08 6D     LEAU    $CB0A,PC            ; Cherry graphic    
C29D: 17 04 BD        LBSR    $04BD               ; Draw cherry    
C2A0: 16 00 E3        LBRA    $C386               ; Next object    
;
C2A3: 5A              DECB                        ; 3=MAGNET
C2A4: 26 17           BNE     $C2BD                   ; No ... check other types
C2A6: 33 8D 08 70     LEAU    $CB1A,PC                
C2AA: 17 05 AE        LBSR    $05AE                   
C2AD: CC 10 10        LDD     #$1010                  
C2B0: 17 07 4C        LBSR    $074C                   
C2B3: 33 8D 08 63     LEAU    $CB1A,PC                
C2B7: 17 04 A3        LBSR    $04A3                   
C2BA: 16 00 C9        LBRA    $C386                   

C2BD: 5A              DECB                        ; 4=SKATE
C2BE: 26 24           BNE     $C2E4                   ; No ... check other types
C2C0: 8D 13           BSR     $C2D5                   
C2C2: 17 05 96        LBSR    $0596                   
C2C5: 6C 07           INC     7,X                 
C2C7: 86 10           LDA     #$10                  
C2C9: 5F              CLRB                        
C2CA: 17 07 32        LBSR    $0732                   
C2CD: 8D 06           BSR     $C2D5                   
C2CF: 17 04 8B        LBSR    $048B                   
C2D2: 16 00 B1        LBRA    $C386                   
;
C2D5: 33 8D 08 51     LEAU    $CB2A,PC                ; Skate graphic 1
C2D9: E6 07           LDB     7,X                 
C2DB: C4 01           ANDB    #$01                  
C2DD: 26 04           BNE     $C2E3                   
C2DF: 33 8D 08 57     LEAU    $CB3A,PC                ; Skate graphic 2
C2E3: 39              RTS                         ; Done

C2E4: 5A              DECB                        ; 5=YoYo 
C2E5: 26 3C           BNE     $C323               ; No ... check other types
C2E7: 33 8D 08 9F     LEAU    $CB8A,PC            ; 
C2EB: 17 05 6D        LBSR    $056D                   
C2EE: 4F              CLRA                        
C2EF: A7 04           STA     4,X                 
C2F1: C6 20           LDB     #$20                  
C2F3: 6D 07           TST     7,X                 
C2F5: 27 01           BEQ     $C2F8                   
C2F7: 50              NEGB                        
C2F8: E7 05           STB     5,X                 
C2FA: 17 06 CB        LBSR    $06CB                   
C2FD: E6 02           LDB     2,X                 
C2FF: C1 0C           CMPB    #$0C                  
C301: 24 ; ????
C302: 04 6F           LSR     $6F                   
C304: 07 C6           ASR     $C6                   
C306: 0C C1           INC     $C1                   
C308: 42 ; ????
C309: 25 ; ????
C30A: 04 6C           LSR     $6C                   
C30C: 07 C6           ASR     $C6                   
C30E: 42 ; ????
C30F: E7 02           STB     2,X                 
C311: 33 8D 08 35     LEAU    $CB4A,PC                ; YoYo images
C315: C4 03           ANDB    #$03                    ; 4 of them
C317: 58              LSRB                            ; 16 ...
C318: 58              LSRB                            ; ... bytes ...
C319: 58              LSRB                            ; ... each ...
C31A: 58              LSRB                            ; ... image
C31B: 33 C5           LEAU    B,U                     ; Point to current image
C31D: 17 04 3D        LBSR    $043D                   
C320: 16 00 63        LBRA    $C386                   

C323: 5A              DECB                        ; 6=??
C324: 26 09           BNE     $C32F               ; No ... check other types    
C326: 33 8D 08 90     LEAU    $CBBA,PC                
C32A: 17 04 30        LBSR    $0430                   
C32D: 20 57           BRA     $C386                   

C32F: 5A              DECB                        ; 7=??
C330: 26 21           BNE     $C353               ; No ... check other types    
C332: 8D 10           BSR     $C344                   
C334: 17 05 24        LBSR    $0524                   
C337: CC 30 30        LDD     #$3030                  
C33A: 17 06 C2        LBSR    $06C2                   
C33D: 8D 05           BSR     $C344                   
C33F: 17 04 1B        LBSR    $041B                   
C342: 20 42           BRA     $C386                 
;
C344: 33 8D 08 82     LEAU    $CBCA,PC                
C348: E6 02           LDB     2,X                 
C34A: C4 01           ANDB    #$01                  
C34C: 26 04           BNE     $C352                   
C34E: 33 8D 08 88     LEAU    $CBDA,PC                
C352: 39              RTS                         

C353: 5A              DECB                        ; 8=??
C354: 26 09           BNE     $C35F               ; No ... check other types   
C356: 33 8D 08 50     LEAU    $CBAA,PC                
C35A: 17 04 00        LBSR    $0400                   
C35D: 20 27           BRA     $C386                   

C35F: 5A              DECB                        ; 9=??
C360: 26 24           BNE     $C386               ; No. Anything but 0-9 ... skip.
C362: 8D 13           BSR     $C377                   
C364: 17 04 F4        LBSR    $04F4                   
C367: 6C 07           INC     7,X                 
C369: CC 7F 7F        LDD     #$7F7F                  
C36C: 17 06 90        LBSR    $0690                   
C36F: 8D 06           BSR     $C377                   
C371: 17 03 E9        LBSR    $03E9                   
C374: 16 00 0F        LBRA    $C386                   
;
C377: 33 8D 08 6F     LEAU    $CBEA,PC                
C37B: E6 07           LDB     7,X                 
C37D: C4 01           ANDB    #$01                  
C37F: 26 04           BNE     $C385                   
C381: 33 8D 08 75     LEAU    $CBFA,PC                
C385: 39              RTS                         

; Next object
C386: 6F 04           CLR     4,X                 
C388: 6F 05           CLR     5,X                 
C38A: 30 08           LEAX    8,X                 
C38C: 16 FE E3        LBRA    $C272                   
C38F: 9F D2           STX     $D2                   
C391: AD 9F A0 0A     JSR     [$A00A]                 
C395: 8E 00 D8        LDX     #$00D8                  
C398: 10 8E 01 5A     LDY     #$015A                  
C39C: D6 B6           LDB     $B6                   
C39E: 58              LSRB
C39F: 31 A5           LEAY    B,Y                 
C3A1: E6 A4           LDB     ,Y                  
C3A3: A6 A4           LDA     ,Y                  
C3A5: 9B D7           ADDA    $D7                   
C3A7: 97 D7           STA     $D7                   
C3A9: C0 20           SUBB    #$20                  
C3AB: E7 04           STB     4,X                 
C3AD: E6 21           LDB     1,Y                 
C3AF: C0 20           SUBB    #$20                  
C3B1: E7 05           STB     5,X                 
C3B3: 17 06 12        LBSR    $0612                   
C3B6: 17 03 66        LBSR    $0366                   
C3B9: 8E 00 D8        LDX     #$00D8                  
C3BC: 17 05 A0        LBSR    $05A0                   
C3BF: D7 BF           STB     $BF                   
C3C1: 17 03 4F        LBSR    $034F                   
C3C4: 0F C3           CLR     $C3                   
C3C6: D6 BE           LDB     $BE                   
C3C8: D7 C0           STB     $C0                   
C3CA: D6 C0           LDB     $C0                   
C3CC: C0 02           SUBB    #$02                  
C3CE: D7 C0           STB     $C0                   
C3D0: D1 BE           CMPB    $BE                   
C3D2: 10 27 01 24     LBEQ    $C4FA                   
C3D6: 8E 02 00        LDX     #$0200                  
C3D9: 3A              ABX                         
C3DA: EC 84           LDD     ,X                  
C3DC: 8E 00 D8        LDX     #$00D8                  
C3DF: A0 84           SUBA    ,X                  
C3E1: 4C              INCA                        
C3E2: 81 02           CMPA    #$02                  
C3E4: 22 07           BHI     $C3ED                   
C3E6: E0 02           SUBB    2,X                 
C3E8: 5C              INCB                        
C3E9: C1 02           CMPB    #$02                  
C3EB: 23 04           BLS     $C3F1                   
C3ED: 0C C3           INC     $C3                   
C3EF: 20 D9           BRA     $C3CA                   
C3F1: 10 83 01 01     CMPD    #$0101                  
C3F5: 26 02           BNE     $C3F9                   
C3F7: 0F BF           CLR     $BF                   
C3F9: 0D C3           TST     $C3                   
C3FB: 27 CD           BEQ     $C3CA                   
C3FD: 0F BF           CLR     $BF                   
C3FF: D6 C0           LDB     $C0                   
C401: D7 C1           STB     $C1                   
C403: D6 BE           LDB     $BE                   
C405: D7 C0           STB     $C0                   
C407: D6 C0           LDB     $C0                   
C409: C0 02           SUBB    #$02                  
C40B: D7 C0           STB     $C0                   
C40D: 8E 02 00        LDX     #$0200                  
C410: 3A              ABX                         
C411: EC 84           LDD     ,X                  
C413: C0 03           SUBB    #$03                  
C415: D7 C2           STB     $C2                   
C417: 80 03           SUBA    #$03                  
C419: 8E 01 60        LDX     #$0160                  
C41C: 6D 06           TST     6,X                 
C41E: 27 15           BEQ     $C435                   
C420: D6 C2           LDB     $C2                   
C422: E0 02           SUBB    2,X                 
C424: 54              LSRB                        
C425: 26 0A           BNE     $C431                   
C427: A1 84           CMPA    ,X                  
C429: 22 04           BHI     $C42F                   
C42B: 6C 04           INC     4,X                 
C42D: 20 02           BRA     $C431                   
C42F: 6C 05           INC     5,X                 
C431: 30 08           LEAX    8,X                 
C433: 20 E7           BRA     $C41C                   
C435: D6 C0           LDB     $C0                   
C437: D1 C1           CMPB    $C1                   
C439: 26 CC           BNE     $C407                   
C43B: 8E 01 60        LDX     #$0160                  
C43E: 0F C4           CLR     $C4                   
C440: 0F C8           CLR     $C8                   
C442: 0F C9           CLR     $C9                   
C444: E6 06           LDB     6,X                 
C446: 27 5D           BEQ     $C4A5                   
C448: 6D 04           TST     4,X                 
C44A: 27 55           BEQ     $C4A1                   
C44C: 6D 05           TST     5,X                 
C44E: 27 51           BEQ     $C4A1                   
C450: C1 08           CMPB    #$08                  
C452: 27 4D           BEQ     $C4A1                   
C454: 0C C4           INC     $C4                   
C456: 0C D0           INC     $D0                   
C458: 0A CE           DEC     $CE                   
C45A: 33 8D 0B 4B     LEAU    $CFA9,PC                
C45E: E6 C5           LDB     B,U                 
C460: 1D              SEX                         
C461: D3 C8           ADDD    $C8                   
C463: DD C8           STD     $C8                   
C465: CE 00 EA        LDU     #$00EA                  
C468: E6 84           LDB     ,X                  
C46A: E7 C4           STB     ,U                  
C46C: E6 02           LDB     2,X                 
C46E: E7 42           STB     2,U                 
C470: 33 8D 07 B7     LEAU    $CC2B,PC                
C474: 17 03 E4        LBSR    $03E4                   
C477: E6 06           LDB     6,X                 
C479: C1 05           CMPB    #$05                  
C47B: 26 11           BNE     $C48E                   
C47D: 33 8D 07 19     LEAU    $CB9A,PC                
C481: 17 03 D7        LBSR    $03D7                   
C484: E6 02           LDB     2,X                 
C486: C0 04           SUBB    #$04                  
C488: E7 02           STB     2,X                 
C48A: C1 03           CMPB    #$03                  
C48C: 2E F3           BGT     $C481                   
C48E: 1F 13           TFR     $13                   
C490: C6 08           LDB     #$08                  
C492: DF D2           STU     $D2                   
C494: A6 48           LDA     8,U                 
C496: A7 C0           STA     ,U+                 
C498: 5A              DECB                        
C499: 26 F9           BNE     $C494                   
C49B: 6D 46           TST     6,U                 
C49D: 26 F1           BNE     $C490                   
C49F: 20 A3           BRA     $C444                   
C4A1: 30 08           LEAX    8,X                 
C4A3: 20 9F           BRA     $C444                   
C4A5: 0D C4           TST     $C4                   
C4A7: 27 51           BEQ     $C4FA                   
C4A9: 17 02 73        LBSR    $0273                   
C4AC: 4F              CLRA                        
C4AD: 5F              CLRB                        
C4AE: D3 C8           ADDD    $C8                   
C4B0: 0A C4           DEC     $C4                   
C4B2: 26 FA           BNE     $C4AE                   
C4B4: DD CA           STD     $CA                   
C4B6: 0D B6           TST     $B6                   
C4B8: 26 06           BNE     $C4C0                   
C4BA: D3 B7           ADDD    $B7                   
C4BC: DD B7           STD     $B7                   
C4BE: 20 04           BRA     $C4C4                   
C4C0: D3 B9           ADDD    $B9                   
C4C2: DD B9           STD     $B9                   
C4C4: C6 3C           LDB     #$3C                  
C4C6: D7 C6           STB     $C6                   
C4C8: 8E 00 EA        LDX     #$00EA                  
C4CB: E6 84           LDB     ,X                  
C4CD: C1 60           CMPB    #$60                  
C4CF: 2F 02           BLE     $C4D3                   
C4D1: C6 60           LDB     #$60                  
C4D3: E7 84           STB     ,X                  
C4D5: 17 04 DA        LBSR    $04DA                   
C4D8: DF CC           STU     $CC                   
C4DA: 0C C7           INC     $C7                   
C4DC: 17 01 31        LBSR    $0131                   
C4DF: 7F FF 20        CLR     $FF20                   
C4E2: BD A9 76        JSR     $A976                   
C4E5: C6 80           LDB     #$80                  
C4E7: 1F 98           TFR     $98                   
C4E9: 4A              DECA                        
C4EA: 26 FD           BNE     $C4E9                   
C4EC: F7 FF 20        STB     $FF20                   
C4EF: 1F 98           TFR     $98                   
C4F1: 4A              DECA                        
C4F2: 26 FD           BNE     $C4F1                   
C4F4: 7F FF 20        CLR     $FF20                   
C4F7: 5A              DECB                        
C4F8: 26 ED           BNE     $C4E7                   
C4FA: 8E 02 00        LDX     #$0200                  
C4FD: D6 BE           LDB     $BE                   
C4FF: 3A              ABX                         
C500: CE 00 D8        LDU     #$00D8                  
C503: A6 C4           LDA     ,U                  
C505: E6 42           LDB     2,U                 
C507: ED 84           STD     ,X                  
C509: D6 BF           LDB     $BF                   
C50B: DB BD           ADDB    $BD                   
C50D: D7 BD           STB     $BD                   
C50F: 0C BE           INC     $BE                   
C511: 0C BE           INC     $BE                   
C513: 0C D1           INC     $D1                   
C515: 10 26 00 B3     LBNE    $C5CC                   
C519: D6 CE           LDB     $CE                   
C51B: C1 13           CMPB    #$13                  
C51D: 10 2C 00 AB     LBGE    $C5CC                   
C521: 0C CE           INC     $CE                   
C523: 33 8D 0A 7A     LEAU    $CFA1,PC                
C527: 17 05 54        LBSR    $0554                   
C52A: 96 D0           LDA     $D0                   
C52C: 48 ; ????
C52D: 48 ; ????
C52E: 8E 00 B7        LDX     #$00B7                  
C531: D6 B6           LDB     $B6                   
C533: 58              LSRB
C534: AB 85           ADDA    B,X                 
C536: 94 D7           ANDA    $D7                   
C538: 97 D1           STA     $D1                   
C53A: A6 85           LDA     B,X                 
C53C: 8B 04           ADDA    #$04                  
C53E: D6 D7           LDB     $D7                   
C540: 3D              MUL                         
C541: 84 07           ANDA    #$07                  
C543: 4C              INCA                        
C544: 81 08           CMPA    #$08                  
C546: 26 09           BNE     $C551                   
C548: 0C CF           INC     $CF                   
C54A: D6 CF           LDB     $CF                   
C54C: C1 0A           CMPB    #$0A                  
C54E: 23 01           BLS     $C551                   
C550: 4C              INCA                        
C551: 9E D2           LDX     $D2                   
C553: A7 06           STA     6,X                 
C555: 6F 07           CLR     7,X                 
C557: 96 D7           LDA     $D7                   
C559: 1F 89           TFR     $89                   
C55B: 54              LSRB                        
C55C: 46              RORA                        
C55D: 54              LSRB                        
C55E: 46              RORA                        
C55F: 97 D7           STA     $D7                   
C561: 54              LSRB                        
C562: 46              RORA                        
C563: 54              LSRB                        
C564: 46              RORA                        
C565: C6 44           LDB     #$44                  
C567: 3D              MUL                         
C568: 8B 08           ADDA    #$08                  
C56A: A7 02           STA     2,X                 
C56C: 96 D7           LDA     $D7                   
C56E: C6 60           LDB     #$60                  
C570: 3D              MUL                         
C571: 84 FC           ANDA    #$FC                  
C573: 8B 0C           ADDA    #$0C                  
C575: 8B 04           ADDA    #$04                  
C577: 81 6C           CMPA    #$6C                  
C579: 24 ; ????
C57A: FA 81 10        ORB     $8110                   
C57D: 23 F6           BLS     $C575                   
C57F: A7 84           STA     ,X                  
C581: E6 02           LDB     2,X                 
C583: CE 00 D8        LDU     #$00D8                  
C586: E0 42           SUBB    2,U                 
C588: CB 14           ADDB    #$14                  
C58A: C1 28           CMPB    #$28                  
C58C: 24 ; ????
C58D: 0C A0           INC     $A0                   
C58F: C4 8B           ANDB    #$8B                  
C591: 14 ; ????
C592: 81 28           CMPA    #$28                  
C594: 24 ; ????
C595: 04 A6           LSR     $A6                   
C597: 84 20           ANDA    #$20                  
C599: DB 1F           ADDB    $1F                   
C59B: 13              SYNC                        
C59C: 11 83 01 60     CMPU    #$0160                  
C5A0: 27 2A           BEQ     $C5CC                   
C5A2: 33 58           LEAU    -8,U                
C5A4: E6 46           LDB     6,U                 
C5A6: E1 06           CMPB    6,X                 
C5A8: 26 F2           BNE     $C59C                   
C5AA: E6 84           LDB     ,X                  
C5AC: E0 C4           SUBB    ,U                  
C5AE: CB 08           ADDB    #$08                  
C5B0: C1 10           CMPB    #$10                  
C5B2: 22 E8           BHI     $C59C                   
C5B4: E6 02           LDB     2,X                 
C5B6: E0 42           SUBB    2,U                 
C5B8: CB 08           ADDB    #$08                  
C5BA: C1 10           CMPB    #$10                  
C5BC: 22 DE           BHI     $C59C                   
C5BE: E6 02           LDB     2,X                 
C5C0: CB 15           ADDB    #$15                  
C5C2: C1 4C           CMPB    #$4C                  
C5C4: 2D 02           BLT     $C5C8                   
C5C6: C0 44           SUBB    #$44                  
C5C8: E7 02           STB     2,X                 
C5CA: 20 CA           BRA     $C596                   
C5CC: 17 05 20        LBSR    $0520                   
C5CF: 0D C7           TST     $C7                   
C5D1: 27 09           BEQ     $C5DC                   
C5D3: 0A C6           DEC     $C6                   
C5D5: 26 05           BNE     $C5DC                   
C5D7: 17 01 45        LBSR    $0145                   
C5DA: 0F C7           CLR     $C7                   
C5DC: 0A D5           DEC     $D5                   
C5DE: 26 2F           BNE     $C60F                   
C5E0: C6 28           LDB     #$28                  
C5E2: D7 D5           STB     $D5                   
C5E4: C6 58           LDB     #$58                  
C5E6: 0D B6           TST     $B6                   
C5E8: 26 12           BNE     $C5FC                   
C5EA: 86 18           LDA     #$18                  
C5EC: 03 D6           COM     $D6                   
C5EE: 26 06           BNE     $C5F6                   
C5F0: 33 8D 06 89     LEAU    $CC7D,PC                
C5F4: 20 16           BRA     $C60C                   
C5F6: 33 8D 06 31     LEAU    $CC2B,PC                
C5FA: 20 10           BRA     $C60C                   
C5FC: 86 52           LDA     #$52                  
C5FE: 03 D6           COM     $D6                   
C600: 26 06           BNE     $C608                   
C602: 33 8D 06 98     LEAU    $CC9E,PC                
C606: 20 04           BRA     $C60C                   
C608: 33 8D 06 1F     LEAU    $CC2B,PC                
C60C: 17 03 34        LBSR    $0334                   
C60F: 39              RTS                         
C610: C6 FF           LDB     #$FF                  
C612: D7 C5           STB     $C5                   
C614: DC B7           LDD     $B7                   
C616: CE 0F 2B        LDU     #$0F2B                  
C619: 17 00 0F        LBSR    $000F                   
C61C: 0D B4           TST     $B4                   
C61E: 27 08           BEQ     $C628                   
C620: DC B9           LDD     $B9                   
C622: CE 0F 3A        LDU     #$0F3A                  
C625: 17 00 03        LBSR    $0003                   
C628: 0F C5           CLR     $C5                   
C62A: 39              RTS                         
C62B: 10 83 27 10     CMPD    #$2710                  
C62F: 24 ; ????
C630: 14 ; ????
C631: 10 83 03 E8     CMPD    #$03E8                  
C635: 24 ; ????
C636: 13              SYNC                        
C637: 10 83 00 64     CMPD    #$0064                  
C63B: 24 ; ????
C63C: 12              NOP                         
C63D: 10 83 00 0A     CMPD    #$000A                  
C641: 24 ; ????
C642: 11 ; ????
C643: 20 14           BRA     $C659                   
C645: 8E 27 10        LDX     #$2710                  
C648: 8D 19           BSR     $C663                   
C64A: 8E 03 E8        LDX     #$03E8                  
C64D: 8D 14           BSR     $C663                   
C64F: 8E 00 64        LDX     #$0064                  
C652: 8D 0F           BSR     $C663                   
C654: 8E 00 0A        LDX     #$000A                  
C657: 8D 0A           BSR     $C663                   
C659: 8E 00 01        LDX     #$0001                  
C65C: 8D 05           BSR     $C663                   
C65E: 4F              CLRA                        
C65F: 5F              CLRB                        
C660: 8D 01           BSR     $C663                   
C662: 39              RTS                         
C663: 34 10           PSHS    $10                   
C665: 30 8D 00 78     LEAX    $C6E1,PC                
C669: A3 E4           SUBD    ,S                  
C66B: 25 ; ????
C66C: 46              RORA                        
C66D: 30 8D 00 75     LEAX    $C6E6,PC                
C671: A3 E4           SUBD    ,S                  
C673: 25 ; ????
C674: 3E              RESET                       
C675: 30 8D 00 72     LEAX    $C6EB,PC                
C679: A3 E4           SUBD    ,S                  
C67B: 25 ; ????
C67C: 36 30           PSHU    $30                   
C67E: 8D 00           BSR     $C680                   
C680: 6F A3           CLR     ,--Y                
C682: E4 25           ANDB    5,Y                 
C684: 2E 30           BGT     $C6B6                   
C686: 8D 00           BSR     $C688                   
C688: 6C A3           INC     ,--Y                
C68A: E4 25           ANDB    5,Y                 
C68C: 26 30           BNE     $C6BE                   
C68E: 8D 00           BSR     $C690                   
C690: 69 A3           ROL     ,--Y                
C692: E4 25           ANDB    5,Y                 
C694: 1E 30           EXG     $30                   
C696: 8D 00           BSR     $C698                   
C698: 66 A3           ROR     ,--Y                
C69A: E4 25           ANDB    5,Y                 
C69C: 16 30 8D        LBRA    $F72C                   
C69F: 00 63           NEG     $63                   
C6A1: A3 E4           SUBD    ,S                  
C6A3: 25 ; ????
C6A4: 0E 30           JMP     $30                   
C6A6: 8D 00           BSR     $C6A8                   
C6A8: 60 A3           NEG     ,--Y                
C6AA: E4 25           ANDB    5,Y                 
C6AC: 06 30           ROR     $30                   
C6AE: 8D 00           BSR     $C6B0                   
C6B0: 5D              TSTB                        
C6B1: A3 E4           SUBD    ,S                  
C6B3: E3 E4           ADDD    ,S                  
C6B5: 34 06           PSHS    $06                   
C6B7: E6 84           LDB     ,X                  
C6B9: 54              LSRB                        
C6BA: D8 C5           EORB    $C5                   
C6BC: E7 C0           STB     ,U+                 
C6BE: E6 01           LDB     1,X                 
C6C0: 54              LSRB                        
C6C1: D8 C5           EORB    $C5                   
C6C3: E7 C8 1F        STB     $1F,U                 
C6C6: E6 02           LDB     2,X                 
C6C8: 54              LSRB                        
C6C9: D8 C5           EORB    $C5                   
C6CB: E7 C8 3F        STB     $3F,U                 
C6CE: E6 03           LDB     3,X                 
C6D0: 54              LSRB                        
C6D1: D8 C5           EORB    $C5                   
C6D3: E7 C8 5F        STB     $5F,U                 
C6D6: E6 04           LDB     4,X                 
C6D8: 54              LSRB                        
C6D9: D8 C5           EORB    $C5                   
C6DB: E7 C8 7F        STB     $7F,U                 
C6DE: 35 16           PULS    $16                   
C6E0: 39              RTS                         
C6E1: 20 88           BRA     $C66B                   
C6E3: 88 88           EORA    #$88                  
C6E5: 20 20           BRA     $C707                   
C6E7: A0 20           SUBA    0,Y                 
C6E9: 20 A8           BRA     $C693                   
C6EB: 20 88           BRA     $C675                   
C6ED: 08 ; ????
C6EE: 20 A8           BRA     $C698                   
C6F0: A8 08           EORA    8,X                 
C6F2: 28 08           BVC     $C6FC                   
C6F4: A8 80           EORA    ,X+                 
C6F6: 88 88           EORA    #$88                  
C6F8: A8 08           EORA    8,X                 
C6FA: A8 80           EORA    ,X+                 
C6FC: 20 08           BRA     $C706                   
C6FE: A0 A8 80        SUBA    $80,Y                 
C701: A8 88 A8        EORA    $A8,X                 
C704: A8 08           EORA    8,X                 
C706: 08 ; ????
C707: 20 20           BRA     $C729                   
C709: A8 88 A8        EORA    $A8,X                 
C70C: 88 A8           EORA    #$A8                  
C70E: 20 88           BRA     $C698                   
C710: 28 08           BVC     $C71A                   
C712: A0 0D           SUBA    13,X                
C714: C7 ; ????
C715: 27 07           BEQ     $C71E                   
C717: DE CC           LDU     $CC                   
C719: DC CA           LDD     $CA                   
C71B: 17 FF 0D        LBSR    $FF0D                   
C71E: 39              RTS                         
C71F: 0D C7           TST     $C7                   
C721: 27 2A           BEQ     $C74D                   
C723: DE CC           LDU     $CC                   
C725: DC CA           LDD     $CA                   
C727: 10 83 27 10     CMPD    #$2710                  
C72B: 24 ; ????
C72C: 14 ; ????
C72D: 10 83 03 E8     CMPD    #$03E8                  
C731: 24 ; ????
C732: 10 ; ????
C733: 10 83 00 64     CMPD    #$0064                  
C737: 24 ; ????
C738: 0C 10           INC     $10                   
C73A: 83 00 0A        SUBD    #$000A                  
C73D: 24 ; ????
C73E: 08 ; ????
C73F: 20 08           BRA     $C749                   
C741: 8D 0B           BSR     $C74E                   
C743: 8D 09           BSR     $C74E                   
C745: 8D 07           BSR     $C74E                   
C747: 8D 05           BSR     $C74E                   
C749: 8D 03           BSR     $C74E                   
C74B: 8D 01           BSR     $C74E                   
C74D: 39              RTS                         
C74E: 6F C0           CLR     ,U+                 
C750: 6F C8 1F        CLR     $1F,U                 
C753: 6F C8 3F        CLR     $3F,U                 
C756: 6F C8 5F        CLR     $5F,U                 
C759: 6F C8 7F        CLR     $7F,U                 
C75C: 39              RTS                         

C75D: C6 08           LDB     #$08                  
C75F: 34 54           PSHS    $54                   
C761: 17 02 4E        LBSR    $024E                   
C764: 10 8E 03 80     LDY     #$0380                  
C768: AE 63           LDX     3,S                 
C76A: 5D              TSTB                        
C76B: 10 27 00 CA     LBEQ    $C839                   
C76F: 5A              DECB                        
C770: 10 27 00 88     LBEQ    $C7FC                   
C774: 5A              DECB                        
C775: 10 27 00 3E     LBEQ    $C7B7                   
C779: E6 80           LDB     ,X+                 
C77B: 4F              CLRA                        
C77C: 58              LSRB
C77D: 49              ROLA                        
C77E: 58              LSRB
C77F: 49              ROLA                        
C780: 34 06           PSHS    $06                   
C782: E6 80           LDB     ,X+                 
C784: 4F              CLRA                        
C785: 58              LSRB
C786: 49              ROLA                        
C787: 58              LSRB
C788: 49              ROLA                        
C789: AB 61           ADDA    1,S                 
C78B: A7 61           STA     1,S                 
C78D: 34 04           PSHS    $04                   
C78F: A6 A5           LDA     B,Y                 
C791: A4 42           ANDA    2,U                 
C793: AB E4           ADDA    ,S                  
C795: A7 42           STA     2,U                 
C797: E6 62           LDB     2,S                 
C799: A6 A5           LDA     B,Y                 
C79B: A4 41           ANDA    1,U                 
C79D: AB 62           ADDA    2,S                 
C79F: A7 41           STA     1,U                 
C7A1: E6 61           LDB     1,S                 
C7A3: A6 A5           LDA     B,Y                 
C7A5: A4 C4           ANDA    ,U                  
C7A7: AB 61           ADDA    1,S                 
C7A9: A7 C4           STA     ,U                  
C7AB: 32 63           LEAS    3,S                 
C7AD: 33 C8 20        LEAU    $20,U                 
C7B0: 6A E4           DEC     ,S                  
C7B2: 26 C5           BNE     $C779                   
C7B4: 16 00 A1        LBRA    $C858                   
C7B7: E6 80           LDB     ,X+                 
C7B9: 4F              CLRA                        
C7BA: 54              LSRB                        
C7BB: 46              RORA                        
C7BC: 54              LSRB                        
C7BD: 46              RORA                        
C7BE: 54              LSRB                        
C7BF: 46              RORA                        
C7C0: 54              LSRB                        
C7C1: 46              RORA                        
C7C2: 34 06           PSHS    $06                   
C7C4: E6 80           LDB     ,X+                 
C7C6: 4F              CLRA                        
C7C7: 54              LSRB                        
C7C8: 46              RORA                        
C7C9: 54              LSRB                        
C7CA: 46              RORA                        
C7CB: 54              LSRB                        
C7CC: 46              RORA                        
C7CD: 54              LSRB                        
C7CE: 46              RORA                        
C7CF: EB E4           ADDB    ,S                  
C7D1: E7 E4           STB     ,S                  
C7D3: 34 02           PSHS    $02                   
C7D5: A6 A6           LDA     A,Y                 
C7D7: A4 42           ANDA    2,U                 
C7D9: AB E4           ADDA    ,S                  
C7DB: A7 42           STA     2,U                 
C7DD: E6 61           LDB     1,S                 
C7DF: A6 A5           LDA     B,Y                 
C7E1: A4 41           ANDA    1,U                 
C7E3: AB 61           ADDA    1,S                 
C7E5: A7 41           STA     1,U                 
C7E7: E6 62           LDB     2,S                 
C7E9: A6 A5           LDA     B,Y                 
C7EB: A4 C4           ANDA    ,U                  
C7ED: AB 62           ADDA    2,S                 
C7EF: A7 C4           STA     ,U                  
C7F1: 32 63           LEAS    3,S                 
C7F3: 33 C8 20        LEAU    $20,U                 
C7F6: 6A E4           DEC     ,S                  
C7F8: 26 BD           BNE     $C7B7                   
C7FA: 20 5C           BRA     $C858                   
C7FC: E6 80           LDB     ,X+                 
C7FE: 4F              CLRA                        
C7FF: 54              LSRB                        
C800: 46              RORA                        
C801: 54              LSRB                        
C802: 46              RORA                        
C803: 34 06           PSHS    $06                   
C805: E6 80           LDB     ,X+                 
C807: 4F              CLRA                        
C808: 54              LSRB                        
C809: 46              RORA                        
C80A: 54              LSRB                        
C80B: 46              RORA                        
C80C: EB E4           ADDB    ,S                  
C80E: E7 E4           STB     ,S                  
C810: 34 02           PSHS    $02                   
C812: A6 A6           LDA     A,Y                 
C814: A4 42           ANDA    2,U                 
C816: AB E4           ADDA    ,S                  
C818: A7 42           STA     2,U                 
C81A: E6 61           LDB     1,S                 
C81C: A6 A5           LDA     B,Y                 
C81E: A4 41           ANDA    1,U                 
C820: AB 61           ADDA    1,S                 
C822: A7 41           STA     1,U                 
C824: E6 62           LDB     2,S                 
C826: A6 A5           LDA     B,Y                 
C828: A4 C4           ANDA    ,U                  
C82A: AB 62           ADDA    2,S                 
C82C: A7 C4           STA     ,U                  
C82E: 32 63           LEAS    3,S                 
C830: 33 C8 20        LEAU    $20,U                 
C833: 6A E4           DEC     ,S                  
C835: 26 C5           BNE     $C7FC                   
C837: 20 1F           BRA     $C858                   
C839: EC 81           LDD     ,X++                
C83B: 34 06           PSHS    $06                   
C83D: A6 A6           LDA     A,Y                 
C83F: A4 C4           ANDA    ,U                  
C841: AB E4           ADDA    ,S                  
C843: A7 C4           STA     ,U                  
C845: E6 61           LDB     1,S                 
C847: A6 A5           LDA     B,Y                 
C849: A4 41           ANDA    1,U                 
C84B: AB 61           ADDA    1,S                 
C84D: A7 41           STA     1,U                 
C84F: 32 62           LEAS    2,S                 
C851: 33 C8 20        LEAU    $20,U                 
C854: 6A E4           DEC     ,S                  
C856: 26 E1           BNE     $C839                   
C858: 35 54           PULS    $54                   
C85A: 39              RTS                         
C85B: C6 08           LDB     #$08                  
C85D: 34 54           PSHS    $54                   
C85F: 17 01 50        LBSR    $0150                   
C862: 10 8E 03 80     LDY     #$0380                  
C866: AE 63           LDX     3,S                 
C868: 5D              TSTB                        
C869: 10 27 00 B8     LBEQ    $C925                   
C86D: 5A              DECB                        
C86E: 10 27 00 7C     LBEQ    $C8EE                   
C872: 5A              DECB                        
C873: 10 27 00 38     LBEQ    $C8AF                   
C877: E6 80           LDB     ,X+                 
C879: 4F              CLRA                        
C87A: 58              LSRB
C87B: 49              ROLA                        
C87C: 58              LSRB
C87D: 49              ROLA                        
C87E: 34 06           PSHS    $06                   
C880: E6 80           LDB     ,X+                 
C882: 4F              CLRA                        
C883: 58              LSRB
C884: 49              ROLA                        
C885: 58              LSRB
C886: 49              ROLA                        
C887: AB 61           ADDA    1,S                 
C889: A7 61           STA     1,S                 
C88B: 34 04           PSHS    $04                   
C88D: A6 A5           LDA     B,Y                 
C88F: A4 42           ANDA    2,U                 
C891: A7 42           STA     2,U                 
C893: E6 62           LDB     2,S                 
C895: A6 A5           LDA     B,Y                 
C897: A4 41           ANDA    1,U                 
C899: A7 41           STA     1,U                 
C89B: E6 61           LDB     1,S                 
C89D: A6 A5           LDA     B,Y                 
C89F: A4 C4           ANDA    ,U                  
C8A1: A7 C4           STA     ,U                  
C8A3: 32 63           LEAS    3,S                 
C8A5: 33 C8 20        LEAU    $20,U                 
C8A8: 6A E4           DEC     ,S                  
C8AA: 26 CB           BNE     $C877                   
C8AC: 16 00 91        LBRA    $C940                   
C8AF: E6 80           LDB     ,X+                 
C8B1: 4F              CLRA                        
C8B2: 54              LSRB                        
C8B3: 46              RORA                        
C8B4: 54              LSRB                        
C8B5: 46              RORA                        
C8B6: 54              LSRB                        
C8B7: 46              RORA                        
C8B8: 54              LSRB                        
C8B9: 46              RORA                        
C8BA: 34 06           PSHS    $06                   
C8BC: E6 80           LDB     ,X+                 
C8BE: 4F              CLRA                        
C8BF: 54              LSRB                        
C8C0: 46              RORA                        
C8C1: 54              LSRB                        
C8C2: 46              RORA                        
C8C3: 54              LSRB                        
C8C4: 46              RORA                        
C8C5: 54              LSRB                        
C8C6: 46              RORA                        
C8C7: EB E4           ADDB    ,S                  
C8C9: E7 E4           STB     ,S                  
C8CB: 34 02           PSHS    $02                   
C8CD: A6 A6           LDA     A,Y                 
C8CF: A4 42           ANDA    2,U                 
C8D1: A7 42           STA     2,U                 
C8D3: E6 61           LDB     1,S                 
C8D5: A6 A5           LDA     B,Y                 
C8D7: A4 41           ANDA    1,U                 
C8D9: A7 41           STA     1,U                 
C8DB: E6 62           LDB     2,S                 
C8DD: A6 A5           LDA     B,Y                 
C8DF: A4 C4           ANDA    ,U                  
C8E1: A7 C4           STA     ,U                  
C8E3: 32 63           LEAS    3,S                 
C8E5: 33 C8 20        LEAU    $20,U                 
C8E8: 6A E4           DEC     ,S                  
C8EA: 26 C3           BNE     $C8AF                   
C8EC: 20 52           BRA     $C940                   
C8EE: E6 80           LDB     ,X+                 
C8F0: 4F              CLRA                        
C8F1: 54              LSRB                        
C8F2: 46              RORA                        
C8F3: 54              LSRB                        
C8F4: 46              RORA                        
C8F5: 34 06           PSHS    $06                   
C8F7: E6 80           LDB     ,X+                 
C8F9: 4F              CLRA                        
C8FA: 54              LSRB                        
C8FB: 46              RORA                        
C8FC: 54              LSRB                        
C8FD: 46              RORA                        
C8FE: EB E4           ADDB    ,S                  
C900: E7 E4           STB     ,S                  
C902: 34 02           PSHS    $02                   
C904: A6 A6           LDA     A,Y                 
C906: A4 42           ANDA    2,U                 
C908: A7 42           STA     2,U                 
C90A: E6 61           LDB     1,S                 
C90C: A6 A5           LDA     B,Y                 
C90E: A4 41           ANDA    1,U                 
C910: A7 41           STA     1,U                 
C912: E6 62           LDB     2,S                 
C914: A6 A5           LDA     B,Y                 
C916: A4 C4           ANDA    ,U                  
C918: A7 C4           STA     ,U                  
C91A: 32 63           LEAS    3,S                 
C91C: 33 C8 20        LEAU    $20,U                 
C91F: 6A E4           DEC     ,S                  
C921: 26 CB           BNE     $C8EE                   
C923: 20 1B           BRA     $C940                   
C925: EC 81           LDD     ,X++                
C927: 34 06           PSHS    $06                   
C929: A6 A6           LDA     A,Y                 
C92B: A4 C4           ANDA    ,U                  
C92D: A7 C4           STA     ,U                  
C92F: E6 61           LDB     1,S                 
C931: A6 A5           LDA     B,Y                 
C933: A4 41           ANDA    1,U                 
C935: A7 41           STA     1,U                 
C937: 32 62           LEAS    2,S                 
C939: 33 C8 20        LEAU    $20,U                 
C93C: 6A E4           DEC     ,S                  
C93E: 26 E5           BNE     $C925                   
C940: 35 54           PULS    $54                   
C942: 39              RTS                         
C943: 8E 00 E4        LDX     #$00E4                  
C946: A7 84           STA     ,X                  
C948: E7 02           STB     2,X                 
C94A: E6 5F           LDB     -1,U                
C94C: E7 04           STB     4,X                 
C94E: 17 FE 0C        LBSR    $FE0C                   
C951: 33 C8 10        LEAU    $10,U                 
C954: A6 84           LDA     ,X                  
C956: 8B 08           ADDA    #$08                  
C958: A7 84           STA     ,X                  
C95A: 6A 04           DEC     4,X                 
C95C: 26 F0           BNE     $C94E                   
C95E: 39              RTS                         
C95F: 17 00 50        LBSR    $0050                   
C962: A6 C4           LDA     ,U                  
C964: 5D              TSTB                        
C965: 26 0A           BNE     $C971                   
C967: 84 3F           ANDA    #$3F                  
C969: 1F 89           TFR     $89                   
C96B: E0 C4           SUBB    ,U                  
C96D: 8A 80           ORA     #$80                  
C96F: 20 22           BRA     $C993                   
C971: 5A              DECB                        
C972: 26 0A           BNE     $C97E                   
C974: 84 CF           ANDA    #$CF                  
C976: 1F 89           TFR     $89                   
C978: E0 C4           SUBB    ,U                  
C97A: 8A 20           ORA     #$20                  
C97C: 20 15           BRA     $C993                   
C97E: 5A              DECB                        
C97F: 26 0A           BNE     $C98B                   
C981: 84 F3           ANDA    #$F3                  
C983: 1F 89           TFR     $89                   
C985: E0 C4           SUBB    ,U                  
C987: 8A 08           ORA     #$08                  
C989: 20 08           BRA     $C993                   
C98B: 84 FC           ANDA    #$FC                  
C98D: 1F 89           TFR     $89                   
C98F: E0 C4           SUBB    ,U                  
C991: 8A 02           ORA     #$02                  
C993: A7 C4           STA     ,U                  
C995: 39              RTS                         
C996: A6 C4           LDA     ,U                  
C998: 5D              TSTB                        
C999: 26 04           BNE     $C99F                   
C99B: 84 3F           ANDA    #$3F                  
C99D: 20 10           BRA     $C9AF                   
C99F: 5A              DECB                        
C9A0: 26 04           BNE     $C9A6                   
C9A2: 84 CF           ANDA    #$CF                  
C9A4: 20 09           BRA     $C9AF                   
C9A6: 5A              DECB                        
C9A7: 26 04           BNE     $C9AD                   
C9A9: 84 F3           ANDA    #$F3                  
C9AB: 20 02           BRA     $C9AF                   
C9AD: 84 FC           ANDA    #$FC                  
C9AF: A7 C4           STA     ,U                  
C9B1: 39              RTS                         
C9B2: E6 84           LDB     ,X                  
C9B4: A6 02           LDA     2,X                 
C9B6: 58              LSRB
C9B7: 47              ASRA                        
C9B8: 56              RORB                        
C9B9: 47              ASRA                        
C9BA: 56              RORB                        
C9BB: 47              ASRA                        
C9BC: 56              RORB                        
C9BD: 10 8E 04 00     LDY     #$0400                  
C9C1: 33 AB           LEAU    D,Y                 
C9C3: E6 84           LDB     ,X                  
C9C5: C4 03           ANDB    #$03                  
C9C7: 39              RTS                         
C9C8: E6 04           LDB     4,X                 
C9CA: 1D              SEX                         
C9CB: 58              LSRB
C9CC: 49              ROLA                        
C9CD: 58              LSRB
C9CE: 49              ROLA                        
C9CF: 58              LSRB
C9D0: 49              ROLA                        
C9D1: E3 84           ADDD    ,X                  
C9D3: 80 03           SUBA    #$03                  
C9D5: 81 7B           CMPA    #$7B                  
C9D7: 25 ; ????
C9D8: 07 86           ASR     $86                   
C9DA: 7A 6D 04        DEC     $6D04                   
C9DD: 2A 01           BPL     $C9E0                   
C9DF: 4F              CLRA                        
C9E0: 8B 03           ADDA    #$03                  
C9E2: ED 84           STD     ,X                  
C9E4: E6 05           LDB     5,X                 
C9E6: 1D              SEX                         
C9E7: 58              LSRB
C9E8: 58              LSRB
C9E9: 58              LSRB
C9EA: 49              ROLA                        
C9EB: E3 02           ADDD    2,X                 
C9ED: 80 03           SUBA    #$03                  
C9EF: 81 53           CMPA    #$53                  
C9F1: 25 ; ????
C9F2: 07 86           ASR     $86                   
C9F4: 52 ; ????
C9F5: 6D 05           TST     5,X                 
C9F7: 2A 01           BPL     $C9FA                   
C9F9: 4F              CLRA                        
C9FA: 8B 03           ADDA    #$03                  
C9FC: ED 02           STD     2,X                 
C9FE: 39              RTS                         
C9FF: A7 04           STA     4,X                 
CA01: E7 05           STB     5,X                 
CA03: CE 00 D8        LDU     #$00D8                  
CA06: A6 84           LDA     ,X                  
CA08: 8B 04           ADDA    #$04                  
CA0A: A7 84           STA     ,X                  
CA0C: A0 C4           SUBA    ,U                  
CA0E: 2B 07           BMI     $CA17                   
CA10: 60 04           NEG     4,X                 
CA12: 4D              TSTA                        
CA13: 26 02           BNE     $CA17                   
CA15: 6F 04           CLR     4,X                 
CA17: E6 04           LDB     4,X                 
CA19: A6 02           LDA     2,X                 
CA1B: 8B 04           ADDA    #$04                  
CA1D: A7 02           STA     2,X                 
CA1F: A0 42           SUBA    2,U                 
CA21: 2B 07           BMI     $CA2A                   
CA23: 60 05           NEG     5,X                 
CA25: 4D              TSTA                        
CA26: 26 02           BNE     $CA2A                   
CA28: 6F 05           CLR     5,X                 
CA2A: 17 FF 9B        LBSR    $FF9B                   
CA2D: A6 84           LDA     ,X                  
CA2F: 80 04           SUBA    #$04                  
CA31: 81 03           CMPA    #$03                  
CA33: 2C 02           BGE     $CA37                   
CA35: 86 03           LDA     #$03                  
CA37: 81 76           CMPA    #$76                  
CA39: 2F 02           BLE     $CA3D                   
CA3B: 86 76           LDA     #$76                  
CA3D: A7 84           STA     ,X                  
CA3F: A6 02           LDA     2,X                 
CA41: 80 04           SUBA    #$04                  
CA43: 81 03           CMPA    #$03                  
CA45: 2C 02           BGE     $CA49                   
CA47: 86 03           LDA     #$03                  
CA49: 81 4E           CMPA    #$4E                  
CA4B: 2F 02           BLE     $CA4F                   
CA4D: 86 4E           LDA     #$4E                  
CA4F: A7 02           STA     2,X                 
CA51: 39              RTS                         
CA52: 5F              CLRB                        
CA53: CE 04 00        LDU     #$0400                  
CA56: 33 C9 0C 00     LEAU    $0C00,U                 
CA5A: E7 C2           STB     ,-U                 
CA5C: 11 83 04 00     CMPU    #$0400                  
CA60: 22 F8           BHI     $CA5A                   
CA62: 39              RTS                         
CA63: CE 04 00        LDU     #$0400                  
CA66: 33 C8 60        LEAU    $60,U                 
CA69: 86 53           LDA     #$53                  
CA6B: C6 F0           LDB     #$F0                  
CA6D: E7 C0           STB     ,U+                 
CA6F: C6 1E           LDB     #$1E                  
CA71: 6F C0           CLR     ,U+                 
CA73: 5A              DECB                        
CA74: 26 FB           BNE     $CA71                   
CA76: C6 0F           LDB     #$0F                  
CA78: E7 C0           STB     ,U+                 
CA7A: 4A              DECA                        
CA7B: 26 EE           BNE     $CA6B                   
CA7D: 39              RTS                         
CA7E: 7F FF 20        CLR     $FF20                   
CA81: BD A9 76        JSR     $A976                   
CA84: 17 00 39        LBSR    $0039                   
CA87: EC C1           LDD     ,U++                
CA89: 27 34           BEQ     $CABF                   
CA8B: 34 06           PSHS    $06                   
CA8D: 1F 98           TFR     $98                   
CA8F: 4A              DECA                        
CA90: 1E 11           EXG     $11                   
CA92: 1E 11           EXG     $11                   
CA94: 1E 11           EXG     $11                   
CA96: 1E 11           EXG     $11                   
CA98: 26 F5           BNE     $CA8F                   
CA9A: 86 3C           LDA     #$3C                  
CA9C: B7 FF 20        STA     $FF20                   
CA9F: 1F 98           TFR     $98                   
CAA1: A0 61           SUBA    1,S                 
CAA3: 43              COMA                        
CAA4: 4A              DECA                        
CAA5: 1E 11           EXG     $11                   
CAA7: 1E 11           EXG     $11                   
CAA9: 1E 11           EXG     $11                   
CAAB: 1E 11           EXG     $11                   
CAAD: 26 F5           BNE     $CAA4                   
CAAF: 7F FF 20        CLR     $FF20                   
CAB2: 5A              DECB                        
CAB3: 26 02           BNE     $CAB7                   
CAB5: E6 61           LDB     1,S                 
CAB7: 6A E4           DEC     ,S                  
CAB9: 26 D2           BNE     $CA8D                   
CABB: 35 06           PULS    $06                   
CABD: 20 BF           BRA     $CA7E                   
CABF: 39              RTS                         
CAC0: C6 FB           LDB     #$FB                  
CAC2: F7 FF 02        STB     $FF02                   
CAC5: F6 FF 00        LDB     $FF00                   
CAC8: C4 40           ANDB    #$40                  
CACA: 10 27 F5 36     LBEQ    $C004                   
CACE: 39              RTS                         
CACF: 8D 1E           BSR     $CAEF                   
CAD1: 8E FF C6        LDX     #$FFC6                  
CAD4: E7 84           STB     ,X                  
CAD6: E7 03           STB     3,X                 
CAD8: E7 04           STB     4,X                 
CADA: E7 06           STB     6,X                 
CADC: E7 08           STB     8,X                 
CADE: E7 0A           STB     10,X                
CAE0: F7 FF C0        STB     $FFC0                   
CAE3: F7 FF C2        STB     $FFC2                   
CAE6: F7 FF C5        STB     $FFC5                   
CAE9: C6 F8           LDB     #$F8                  
CAEB: F7 FF 22        STB     $FF22                   
CAEE: 39              RTS                         
CAEF: 7D FF 02        TST     $FF02                   
CAF2: 0C D7           INC     $D7                   
CAF4: 7D FF 03        TST     $FF03                   
CAF7: 2A F9           BPL     $CAF2                   
CAF9: 39              RTS                         

; DATA from here down



; The colors bleed a bit in the used mode
;
; .. BLACK
; .X RED
; X. BLUE
; XX WHITE

; APPLE
; .. .. .. .. X. .. .. ..
; .. .X .X X. .X .X .. ..
; .X .X .X .X .X .X .X ..
; .X .X .X .X XX .X .X ..
; .X .X .X .X XX .X .X ..
; .. .X .X .X .X .X .. ..
; .. .. .X .X .X .. .. ..
; .. .. .. .. .. .. .. .. 
;
CAFA: 00 80           NEG     $80                   
CAFC: 16 50 55        LBRA    $11B54                   
CAFF: 54              LSRB                        
CB00: 55 ; ????
CB01: D4 55           ANDB    $55                   
CB03: D4 15           ANDB    $15                   
CB05: 50              NEGB                        
CB06: 05 ; ????
CB07: 40              NEGA                        
CB08: 00 00           NEG     $00              

; CHERRY
; 00 20 ........ ..X.....
; 00 80 ........ X.......
; 02 20 ......X. ..X.....
; 08 14 ....X... ...X.X..
; 14 5D ...X.X.. .X.X.X.X
; 5D 55 .X.XXX.X .X.X.X.X
; 55 14 .X.X.X.X ...X.X..
; 14 00 ...X.X.. ........
;
CB0A: 00 20           NEG     $20                   
CB0C: 00 80           NEG     $80                   
CB0E: 02 ; ????
CB0F: 20 08           BRA     $CB19                   
CB11: 14 ; ????
CB12: 14 ; ????
CB13: 5D              TSTB                        
CB14: 5D              TSTB                        
CB15: 55 ; ????
CB16: 55 ; ????
CB17: 14 ; ????
CB18: 14 ; ????
CB19: 00 

; MAGNET
; 0A A0 ....X.X. X.X.....
; 2A A8 ..X.X.X. X.X.X...
; A8 2A X.X.X... ..X.X.X.
; A0 0A X.X..... ....X.X.
; A0 0A X.X..... ....X.X.
; A0 0A X.X..... ....X.X.
; 28 28 ..X.X... ..X.X...
; 28 28 ..X.X... ..X.X...
;
CB1A: 0A           NEG     $0A                   
CB1B: A0 2A           SUBA    10,Y                
CB1D: A8 A8 2A        EORA    $2A,Y                 
CB20: A0 0A           SUBA    10,X                
CB22: A0 0A           SUBA    10,X                
CB24: A0 0A           SUBA    10,X                
CB26: 28 28           BVC     $CB50                   
CB28: 28 28           BVC     $CB52    

; SKATE (2 images)
; FC 00 XXXXXX.. ........
; F7 00 XXXX.XXX ........
; FF 74 XXXXXXXX .XXX.X..
; FF FF XXXXXXXX XXXXXXXX
; 55 55 .X.X.X.X .X.X.X.X
; 10 04 ...X.... .....X..
; 54 15 .X.X.X.. ...X.X.X
; 10 04 ...X.... .....X..
;
CB2A: FC 00 F7        LDD     $00F7                   
CB2D: 00 FF           NEG     $FF                   
CB2F: 74 FF FF        LSR     $FFFF                   
CB32: 55 ; ????
CB33: 55 ; ????
CB34: 10 ; ????
CB35: 04 54           LSR     $54                   
CB37: 15 ; ????
CB38: 10 ; ????
CB39: 04 
;
; FC 00 XXXXXX.. ........
; F7 00 XXXX.XXX ........
; FF 74 XXXXXXXX .XXX.X..
; FF FF XXXXXXXX XXXXXXXX
; 55 55 .X.X.X.X .X.X.X.X
; 44 11 .X...X.. ...X...X
; 10 04 ...X.... .....X..
; 44 11 .X...X.. ...X...X
;
CB3A: FC           LSR     $FC                   
CB3B: 00 F7           NEG     $F7                   
CB3D: 00 FF           NEG     $FF                   
CB3F: 74 FF FF        LSR     $FFFF                   
CB42: 55 ; ????
CB43: 55 ; ????
CB44: 44              LSRA                        
CB45: 11 ; ????
CB46: 10 ; ????
CB47: 04 44           LSR     $44                   
CB49: 11 ; ????

; YO YO (3 images)
; 00 10 ........ ...X....
; 0A 90 ....X.X. X..X....
; 2A A0 ..X.X.X. X.X.....
; AA A8 X.X.X.X. X.X.X...
; FF FC XXXXXXXX XXXXXX..
; AA A8 X.X.X.X. X.X.X...
; 2A A0 ..X.X.X. X.X.....
; 0A 80 ....X.X. X.......
;
CB4A: 00 10           NEG     $10                   
CB4C: 0A 90           DEC     $90                   
CB4E: 2A A0           BPL     $CAF0                   
CB50: AA A8 FF        ORA     $FF,Y                 
CB53: FC AA A8        LDD     $AAA8                   
CB56: 2A A0           BPL     $CAF8                   
CB58: 0A 80           DEC     $80                   
;
; 00 10 ........ ...X....
; 0A 90 ....X.X. X..X....
; 2A B0 ..X.X.X. X.XX....
; AA E8 X.X.X.X. XXX.X...
; AB A8 X.X.X.XX X.X.X...
; AE A8 X.X.XXX. X.X.X...
; 3A A0 ..XXX.X. X.X.....
; 0A 80 ....X.X. X.......
;
CB5A: 00 10           NEG     $10                   
CB5C: 0A 90           DEC     $90                   
CB5E: 2A B0           BPL     $CB10                   
CB60: AA E8 AB        ORA     $AB,S                 
CB63: A8 ; ????
CB64: AE A8 3A        LDX     $3A,Y                 
CB67: A0 0A           SUBA    10,X                
CB69: 80 
;
; 00 10 ........ ...X....
; 0B 90 ....X.XX X..X....
; 2B A0 ..X.X.XX X.X.....
; AB A8 X.X.X.XX X.X.X...
; AB A8 X.X.X.XX X.X.X...
; AB A8 X.X.X.XX X.X.X...
; 2B A0 ..X.X.XX X.X.....
; 0B 80 ....X.XX X.......
;
CB6A: 00           SUBA    #$00                  
CB6B: 10 ; ????
CB6C: 0B ; ????
CB6D: 90 2B           SUBA    $2B                   
CB6F: A0 AB           SUBA    D,Y                 
CB71: A8 AB           EORA    D,Y                 
CB73: A8 AB           EORA    D,Y                 
CB75: A8 2B           EORA    11,Y                
CB77: A0 0B           SUBA    11,X                
CB79: 80 
;
; 00 10
; 0A 90
; 3A A0
; AE A8
; AB A8
; AA E8
; 2A B0
; 0A 80
;
CB7A: 00           SUBA    #$00                  
CB7B: 10 ; ????
CB7C: 0A 90           DEC     $90                   
CB7E: 3A              ABX                         
CB7F: A0 ; ????
CB80: AE A8 AB        LDX     $AB,Y                 
CB83: A8 ; ????
CB84: AA E8 2A        ORA     $2A,S                 
CB87: B0 0A 80        SUBA    $0A80        

;
; 00 00 ........ ........
; 0A 80 ....X.X. X.......
; 2A A0 ..X.X.X. X.X.....
; AA A8 X.X.X.X. X.X.X...
; AA A8 X.X.X.X. X.X.X...
; AA A8 X.X.X.X. X.X.X...
; 2A A0 ..X.X.X. X.X.....
; A0 80 X.X..... X.......
;
CB8A: 00 00           NEG     $00                   
CB8C: 0A 80           DEC     $80                   
CB8E: 2A A0           BPL     $CB30                   
CB90: AA A8 AA        ORA     $AA,Y                 
CB93: A8 ; ????
CB94: AA A8 2A        ORA     $2A,Y                 
CB97: A0 0A           SUBA    10,X                
CB99: 80 

;
; 00 30 ........ ..XX....
; 00 30 ........ ..XX....
; 00 30 ........ ..XX....
; 00 30 ........ ..XX....
; 00 30 ........ ..XX....
; 00 30 ........ ..XX....
; 00 30 ........ ..XX....
; 0F C0 ....XXXX XX......
; 
CB9A: 00           SUBA    #$00                  
CB9B: 30 00           LEAX    0,X                 
CB9D: 30 00           LEAX    0,X                 
CB9F: 30 00           LEAX    0,X                 
CBA1: 30 00           LEAX    0,X                 
CBA3: 30 00           LEAX    0,X                 
CBA5: 30 00           LEAX    0,X                 
CBA7: 30 00           LEAX    0,X                 
CBA9: 30 0F           LEAX    15,X                
CBAB: C0 

CBAB: 3F           SUBB    #$3F                  
CBAD: F0 37 70        SUBB    $3770                   
CBB0: 3F              SWI                         
CBB1: F0 0F C0        SUBB    $0FC0                   
CBB4: CF ; ????
CBB5: CC 30 30        LDD     #$3030                  
CBB8: C0 0C           SUBB    #$0C                  
CBBA: 00 10           NEG     $10                   
CBBC: 00 40           NEG     $40                   
CBBE: 00 C0           NEG     $C0                   
CBC0: 03 C0           COM     $C0                   
CBC2: 0F F0           CLR     $F0                   
CBC4: 3F              SWI                         
CBC5: F0 3F F0        SUBB    $3FF0                   
CBC8: 0F C0           CLR     $C0                   
CBCA: 04 10           LSR     $10                   
CBCC: 44              LSRA                        
CBCD: 11 ; ????
CBCE: 12              NOP                         
CBCF: 84 06           ANDA    #$06                  
CBD1: 90 06           SUBA    $06                   
CBD3: 90 12           SUBA    $12                   
CBD5: 84 42           ANDA    #$42                  
CBD7: 81 40           CMPA    #$40                  
CBD9: 01 ; ????
CBDA: 04 10           LSR     $10                   
CBDC: 04 10           LSR     $10                   
CBDE: 02 ; ????
CBDF: 80 56           SUBA    #$56                  
CBE1: 95 02           BITA    $02                   
CBE3: 80 16           SUBA    #$16                  
CBE5: 94 42           ANDA    $42                   
CBE7: 81 00           CMPA    #$00                  
CBE9: 00 00           NEG     $00                   
CBEB: 00 00           NEG     $00                   
CBED: 00 08           NEG     $08                   
CBEF: 20 02           BRA     $CBF3                   
CBF1: 80 02           SUBA    #$02                  
CBF3: 80 08           SUBA    #$08                  
CBF5: 20 00           BRA     $CBF7                   
CBF7: 00 00           NEG     $00                   
CBF9: 00 80           NEG     $80                   
CBFB: 02 ; ????
CBFC: 20 08           BRA     $CC06                   
CBFE: 08 ; ????
CBFF: 20 02           BRA     $CC03                   
CC01: 80 02           SUBA    #$02                  
CC03: 80 08           SUBA    #$08                  
CC05: 20 20           BRA     $CC27                   
CC07: 08 ; ????
CC08: 80 02           SUBA    #$02                  
CC0A: AA 80           ORA     ,X+                 
CC0C: 00 00           NEG     $00                   
CC0E: 00 00           NEG     $00                   
CC10: 00 00           NEG     $00                   
CC12: 00 00           NEG     $00                   
CC14: 00 00           NEG     $00                   
CC16: 00 00           NEG     $00                   
CC18: 00 00           NEG     $00                   
CC1A: 55 ; ????
CC1B: 40              NEGA                        
CC1C: 00 00           NEG     $00                   
CC1E: 00 00           NEG     $00                   
CC20: 00 00           NEG     $00                   
CC22: 00 00           NEG     $00                   
CC24: 00 00           NEG     $00                   
CC26: 00 00           NEG     $00                   
CC28: 00 00           NEG     $00                   
CC2A: 02 ; ????
CC2B: FF FF FF        STU     $FFFF                   
CC2E: FF FF FF        STU     $FFFF                   
CC31: FF FF FF        STU     $FFFF                   
CC34: FF FF FF        STU     $FFFF                   
CC37: FF FF FF        STU     $FFFF                   
CC3A: FF FF FF        STU     $FFFF                   
CC3D: FF FF FF        STU     $FFFF                   
CC40: FF FF FF        STU     $FFFF                   
CC43: FF FF FF        STU     $FFFF                   
CC46: FF FF FF        STU     $FFFF                   
CC49: FF FF 03        STU     $FF03                   
CC4C: 00 10           NEG     $10                   
CC4E: 00 10           NEG     $10                   
CC50: 54              LSRB                        
CC51: 10 ; ????
CC52: 41 ; ????
CC53: 10 ; ????
CC54: 41 ; ????
CC55: 11 ; ????
CC56: 54              LSRB                        
CC57: 11 ; ????
CC58: 40              NEGA                        
CC59: 00 40           NEG     $40                   
CC5B: 00 00           NEG     $00                   
CC5D: 00 00           NEG     $00                   
CC5F: 00 50           NEG     $50                   
CC61: 00 11           NEG     $11                   
CC63: 04 51           LSR     $51                   
CC65: 04 50           LSR     $50                   
CC67: 54              LSRB                        
CC68: 00 04           NEG     $04                   
CC6A: 01 ; ????
CC6B: 50              NEGB                        
CC6C: 00 00           NEG     $00                   
CC6E: 00 00           NEG     $00                   
CC70: 14 ; ????
CC71: 15 ; ????
CC72: 55 ; ????
CC73: 10 ; ????
CC74: 40              NEGA                        
CC75: 10 ; ????
CC76: 14 ; ????
CC77: 10 ; ????
CC78: 00 00           NEG     $00                   
CC7A: 00 00           NEG     $00                   
CC7C: 02 ; ????
CC7D: 00 00           NEG     $00                   
CC7F: 00 00           NEG     $00                   
CC81: 01 ; ????
CC82: 41 ; ????
CC83: 04 11           LSR     $11                   
CC85: 04 11           LSR     $11                   
CC87: 01 ; ????
CC88: 41 ; ????
CC89: 00 00           NEG     $00                   
CC8B: 00 00           NEG     $00                   
CC8D: 00 00           NEG     $00                   
CC8F: 00 00           NEG     $00                   
CC91: 50              NEGB                        
CC92: 14 ; ????
CC93: 04 55           LSR     $55                   
CC95: 04 40           LSR     $40                   
CC97: 04 14           LSR     $14                   
CC99: 00 00           NEG     $00                   
CC9B: 00 00           NEG     $00                   
CC9D: 02 ; ????
CC9E: 00 00           NEG     $00                   
CCA0: 10 ; ????
CCA1: 00 54           NEG     $54                   
CCA3: 10 ; ????
CCA4: 10 ; ????
CCA5: 10 ; ????
CCA6: 11 ; ????
CCA7: 15 ; ????
CCA8: 04 15           LSR     $15                   
CCAA: 00 00           NEG     $00                   
CCAC: 00 00           NEG     $00                   
CCAE: 00 00           NEG     $00                   
CCB0: 00 00           NEG     $00                   
CCB2: 41 ; ????
CCB3: 40              NEGA                        
CCB4: 44              LSRA                        
CCB5: 10 ; ????
CCB6: 44              LSRA                        
CCB7: 10 ; ????
CCB8: 41 ; ????
CCB9: 40              NEGA                        
CCBA: 00 00           NEG     $00                   
CCBC: 00 00           NEG     $00                   
CCBE: 05 ; ????
CCBF: 0F FF           CLR     $FF                   
CCC1: 3F              SWI                         
CCC2: FF FA FE        STU     $FAFE                   
CCC5: EF BF EF BA     STU     [$EFBA]                 
CCC9: FA BA 3F        ORB     $BA3F                   
CCCC: BF 2A FF        STX     $2AFF                   
CCCF: FF FF FF        STU     $FFFF                   
CCD2: FF BA AF        STU     $BAAF                   
CCD5: BA AE BB        ORA     $AEBB                   
CCD8: EE BB           LDU     [D,Y]               
CCDA: EF FF FF FF     STU     [$FFFF]                 
CCDE: FF FF FF        STU     $FFFF                   
CCE1: FF FF AF        STU     $FFAF                   
CCE4: FE AB FB        LDU     $ABFB                   
CCE7: FF FB AF        STU     $FBAF                   
CCEA: FE FF FF        LDU     $FFFF                   
CCED: FF FF FF        STU     $FFFF                   
CCF0: FF FF FF        STU     $FFFF                   
CCF3: BE EF EE        LDX     $EFEE                   
CCF6: EE ; ????
CCF7: EF ; ????
CCF8: BE BF BF        LDX     $BFBF                   
CCFB: FF FF FF        STU     $FFFF                   
CCFE: FF FF C0        STU     $FFC0                   
CD01: FF F0 AF        STU     $F0AF                   
CD04: A8 AB           EORA    D,Y                 
CD06: BC FF BC        CMPX    $FFBC                   
CD09: AF BC FF        STX     [$CD0B,PC]              
CD0C: F0 FF C0        SUBB    $FFC0                   
CD0F: 06 30           ROR     $30                   
CD11: 00 F0           NEG     $F0                   
CD13: 54              LSRB                        
CD14: 30 44           LEAX    4,U                 
CD16: 30 44           LEAX    4,U                 
CD18: 30 54           LEAX    -12,U               
CD1A: FC 00 00        LDD     $0000                   
CD1D: 00 00           NEG     $00                   
CD1F: 00 00           NEG     $00                   
CD21: 3C 50           CWAI    $50                   
CD23: C3 40 0C        ADDD    #$400C                  
CD26: 40              NEGA                        
CD27: 30 40           LEAX    0,U                 
CD29: C0 00           SUBB    #$00                  
CD2B: FF 00 00        STU     $0000                   
CD2E: 00 00           NEG     $00                   
CD30: 00 00           NEG     $00                   
CD32: 01 ; ????
CD33: 50              NEGB                        
CD34: 01 ; ????
CD35: 04 01           LSR     $01                   
CD37: 04 01           LSR     $01                   
CD39: 04 01           LSR     $01                   
CD3B: 50              NEGB                        
CD3C: 01 ; ????
CD3D: 00 01           NEG     $01                   
CD3F: 00 40           NEG     $40                   
CD41: 00 40           NEG     $40                   
CD43: 00 41           NEG     $41                   
CD45: 44              LSRA                        
CD46: 40              NEGA                        
CD47: 44              LSRA                        
CD48: 45 ; ????
CD49: 44              LSRA                        
CD4A: 45 ; ????
CD4B: 41 ; ????
CD4C: 00 00           NEG     $00                   
CD4E: 00 01           NEG     $01                   
CD50: 00 00           NEG     $00                   
CD52: 00 00           NEG     $00                   
CD54: 10 ; ????
CD55: 50              NEGB                        
CD56: 11 ; ????
CD57: 54              LSRB                        
CD58: 11 ; ????
CD59: 00 50           NEG     $50                   
CD5B: 50              NEGB                        
CD5C: 10 ; ????
CD5D: 00 50           NEG     $50                   
CD5F: 00 00           NEG     $00                   
CD61: 00 00           NEG     $00                   
CD63: 00 54           NEG     $54                   
CD65: 14 ; ????
CD66: 40              NEGA                        
CD67: 40              NEGA                        
CD68: 40              NEGA                        
CD69: 14 ; ????
CD6A: 40              NEGA                        
CD6B: 50              NEGB                        
CD6C: 00 00           NEG     $00                   
CD6E: 00 00           NEG     $00                   
CD70: 01 ; ????
CD71: 00 00           NEG     $00                   
CD73: 00 00           NEG     $00                   
CD75: 00 00           NEG     $00                   
CD77: 00 00           NEG     $00                   
CD79: 00 00           NEG     $00                   
CD7B: 00 00           NEG     $00                   
CD7D: 2A 80           BPL     $CCFF                   
CD7F: 80 20           SUBA    #$20                  
CD81: 0A 00           DEC     $00                   
CD83: 02 ; ????
CD84: 00 02           NEG     $02                   
CD86: 00 02           NEG     $02                   
CD88: 00 02           NEG     $02                   
CD8A: 00 00           NEG     $00                   
CD8C: 00 00           NEG     $00                   
CD8E: 00 00           NEG     $00                   
CD90: 80 82           SUBA    #$82                  
CD92: 0A 08           DEC     $08                   
CD94: 20 08           BRA     $CD9E                   
CD96: 20 08           BRA     $CDA0                   
CD98: 0A 08           DEC     $08                   
CD9A: 80 20           SUBA    #$20                  
CD9C: 2A 80           BPL     $CD1E                   
CD9E: 00 00           NEG     $00                   
CDA0: 8A 88           ORA     #$88                  
CDA2: 20 A0           BRA     $CD44                   
CDA4: A2 08           SBCA    8,X                 
CDA6: 20 A8           BRA     $CD50                   
CDA8: 20 08           BRA     $CDB2                   
CDAA: A8 A0           EORA    ,Y+                 
CDAC: 00 00           NEG     $00                   
CDAE: 00 00           NEG     $00                   
CDB0: 20 A2           BRA     $CD54                   
CDB2: 28 0A           BVC     $CDBE                   
CDB4: 82 20           SBCA    #$20                  
CDB6: 28 02           BVC     $CDBA                   
CDB8: 82 08           SBCA    #$08                  
CDBA: 28 2A           BVC     $CDE6                   
CDBC: 00 00           NEG     $00                   
CDBE: 00 00           NEG     $00                   
CDC0: A2 80           SBCA    ,X+                 
CDC2: 00 00           NEG     $00                   
CDC4: 80 02           SUBA    #$02                  
CDC6: 00 02           NEG     $02                   
CDC8: 00 02           NEG     $02                   
CDCA: 80 02           SUBA    #$02                  
CDCC: 00 00           NEG     $00                   
CDCE: 00 00           NEG     $00                   
CDD0: A8 20           EORA    0,Y                 
CDD2: 00 00           NEG     $00                   
CDD4: 80 82           SUBA    #$82                  
CDD6: 22 22           BHI     $CDFA                   
CDD8: 22 A2           BHI     $CD7C                   
CDDA: 82 22           SBCA    #$22                  
CDDC: 00 00           NEG     $00                   
CDDE: AA ; ????
CDDF: 8A 08           ORA     #$08                  
CDE1: 20 00           BRA     $CDE3                   
CDE3: 00 02           NEG     $02                   
CDE5: A0 02           SUBA    2,X                 
CDE7: 00 02           NEG     $02                   
CDE9: 80 A2           SUBA    #$A2                  
CDEB: A0 00           SUBA    0,X                 
CDED: 00 08           NEG     $08                   
CDEF: 22 8A           BHI     $CD7B                   
CDF1: 22 00           BHI     $CDF3                   
CDF3: 00 20           NEG     $20                   
CDF5: 2A 20           BPL     $CE17                   
CDF7: 20 20           BRA     $CE19                   
CDF9: 28 2A           BVC     $CE25                   
CDFB: 2A 00           BPL     $CDFD                   
CDFD: 00 A0           NEG     $A0                   
CDFF: 88 08           EORA    #$08                  
CE01: 88 00           EORA    #$00                  
CE03: 00 08           NEG     $08                   
CE05: 28 22           BVC     $CE29                   
CE07: 22 2A           BHI     $CE33                   
CE09: 28 22           BVC     $CE2D                   
CE0B: 22 00           BHI     $CE0D                   
CE0D: 00 00           NEG     $00                   
CE0F: 00 0A           NEG     $0A                   
CE11: 08 ; ????
CE12: 00 00           NEG     $00                   
CE14: 00 00           NEG     $00                   
CE16: 00 00           NEG     $00                   
CE18: 00 00           NEG     $00                   
CE1A: 00 00           NEG     $00                   
CE1C: 00 00           NEG     $00                   
CE1E: 00 00           NEG     $00                   
CE20: 28 28           BVC     $CE4A                   
CE22: 0A 80           DEC     $80                   
CE24: 88 80           EORA    #$80                  
CE26: 88 A8           EORA    #$A8                  
CE28: 82 00           SBCA    #$00                  
CE2A: 00 00           NEG     $00                   
CE2C: 02 ; ????
CE2D: 00 08           NEG     $08                   
CE2F: 00 0A           NEG     $0A                   
CE31: 00 08           NEG     $08                   
CE33: 08 ; ????
CE34: 0A 0A           DEC     $0A                   
CE36: 08 ; ????
CE37: 8A 88           ORA     #$88                  
CE39: 00 00           NEG     $00                   
CE3B: 08 ; ????
CE3C: 08 ; ????
CE3D: 88 08           EORA    #$08                  
CE3F: 88 08           EORA    #$08                  
CE41: 8A 8A           ORA     #$8A                  
CE43: 22 02           BHI     $CE47                   
CE45: A0 A2           SUBA    ,-Y                 
CE47: 22 82           BHI     $CDCB                   
CE49: 00 00           NEG     $00                   
CE4B: 00 A0           NEG     $A0                   
CE4D: 00 88           NEG     $88                   
CE4F: 00 A0           NEG     $A0                   
CE51: 80 88           SUBA    #$88                  
CE53: 02 ; ????
CE54: 20 82           BRA     $CDD8                   
CE56: 20 A2           BRA     $CDFA                   
CE58: 80 00           SUBA    #$00                  
CE5A: 00 82           NEG     $82                   
CE5C: 88 88           EORA    #$88                  
CE5E: 08 ; ????
CE5F: 88 8A           EORA    #$8A                  
CE61: 82 88           SBCA    #$88                  
CE63: 20 88           BRA     $CDED                   
CE65: 20 88           BRA     $CDEF                   
CE67: 20 20           BRA     $CE89                   
CE69: 00 00           NEG     $00                   
CE6B: 8A 82           ORA     #$82                  
CE6D: 82 08           SBCA    #$08                  
CE6F: 82 02           SBCA    #$02                  
CE71: 82 0A           SBCA    #$0A                  
CE73: 08 ; ????
CE74: 20 08           BRA     $CE7E                   
CE76: 2A 08           BPL     $CE80                   
CE78: 20 00           BRA     $CE7A                   
CE7A: 00 80           NEG     $80                   
CE7C: A0 00           SUBA    0,X                 
CE7E: 88 80           EORA    #$80                  
CE80: A0 00           SUBA    0,X                 
CE82: 88 8A           EORA    #$8A                  
CE84: 22 88           BHI     $CE0E                   
CE86: A2 88 A2        SBCA    $A2,X                 
CE89: 00 00           NEG     $00                   
CE8B: A8 28           EORA    8,Y                 
CE8D: 80 80           SUBA    #$80                  
CE8F: A0 28           SUBA    8,Y                 
CE91: A8 A0           EORA    ,Y+                 
CE93: 08 ; ????
CE94: A8 08           EORA    8,X                 
CE96: 20 A0           BRA     $CE38                   
CE98: 20 00           BRA     $CE9A                   
CE9A: 00 A8           NEG     $A8                   
CE9C: A0 80           SUBA    ,X+                 
CE9E: 88 A0           EORA    #$A0                  
CEA0: A0 A8 88        SUBA    $88,Y                 
CEA3: 20 22           BRA     $CEC7                   
CEA5: 20 22           BRA     $CEC9                   
CEA7: 0A 08           DEC     $08                   
CEA9: 00 00           NEG     $00                   
CEAB: 88 A8           EORA    #$A8                  
CEAD: 88 80           EORA    #$80                  
CEAF: 88 A0           EORA    #$A0                  
CEB1: 20 A8           BRA     $CE5B                   
CEB3: 22 22           BHI     $CED7                   
CEB5: 28 28           BVC     $CEDF                   
CEB7: 22 20           BHI     $CED9                   
CEB9: 00 00           NEG     $00                   
CEBB: A0 00           SUBA    0,X                 
CEBD: 88 00           EORA    #$00                  
CEBF: 88 00           EORA    #$00                  
CEC1: A0 00           SUBA    0,X                 
CEC3: 6D B6           TST     [A,Y]               
CEC5: 27 6D           BEQ     $CF34                   
CEC7: 12              NOP                         
CEC8: 52 ; ????
CEC9: 12              NOP                         
CECA: 49              ROLA                        
CECB: 5A              DECB                        
CECC: 49              ROLA                        
CECD: 5B ; ????
CECE: 6D 29           TST     9,Y                 
CED0: 25 ; ????
CED1: 12              NOP                         
CED2: 4A              DECA                        
CED3: 5D              TSTB                        
CED4: 92 24           SBCA    $24                   
CED6: E5 30           BITB    -16,Y               
CED8: 09 52           ROL     $52                   
CEDA: 53              COMB                        
CEDB: 24 ; ????
CEDC: E5 52           BITB    -14,U               
CEDE: 49              ROLA                        
CEDF: 24 ; ????
CEE0: ED 12           STD     -14,X               
CEE2: 52 ; ????
CEE3: 10 ; ????
CEE4: 49              ROLA                        
CEE5: 5C              INCB                        
CEE6: 00 4B           NEG     $4B                   
CEE8: 2D 39           BLT     $CF23                   
CEEA: 25 ; ????
CEEB: 70 52 24        NEG     $5224                   
CEEE: 93 02           SUBD    $02                   
CEF0: 49              ROLA                        
CEF1: 60 01           NEG     1,X                 
CEF3: 59              ROLB                        
CEF4: 6D 49           TST     9,U                 
CEF6: 2C 24           BGE     $CF1C                   
CEF8: 93 02           SUBD    $02                   
CEFA: 4A              DECA                        
CEFB: 49              ROLA                        
CEFC: 76 24 93        ROR     $2493                   
CEFF: 12              NOP                         
CF00: 92 02           SBCA    $02                   
CF02: 49              ROLA                        
CF03: 60 01           NEG     1,X                 
CF05: 59              ROLB                        
CF06: 6D 49           TST     9,U                 
CF08: 2C 02           BGE     $CF0C                   
CF0A: 93 14           SUBD    $14                   
CF0C: 9F 64           STX     $64                   
CF0E: 8A 39           ORA     #$39                  
CF10: 6E 40           JMP     0,U                 
CF12: 4A              DECA                        
CF13: 14 ; ????
CF14: 9D 24           JSR     $24                   
CF16: 49              ROLA                        
CF17: 6D ; ????
CF18: DA 39           ORB     $39                   
CF1A: 2E 24           BGT     $CF40                   
CF1C: 92 12           SBCA    $12                   
CF1E: 49              ROLA                        
CF1F: 00 41           NEG     $41                   
CF21: 5B ; ????
CF22: 70 4B 2C        NEG     $4B2C                   
CF25: 24 ; ????
CF26: 4C              INCA                        
CF27: 37 AB           PULU    $AB                   
CF29: 12              NOP                         
CF2A: 52 ; ????
CF2B: 00 00           NEG     $00                   
CF2D: 00 FF           NEG     $FF                   
CF2F: 01 ; ????
CF30: FF 01 00        STU     $0100                   
CF33: 01 ; ????
CF34: 01 ; ????
CF35: 00 01           NEG     $01                   
CF37: FF 01 FF        STU     $01FF                   
CF3A: 00 FF           NEG     $FF                   
CF3C: FF 28 80        STU     $2880                   
CF3F: 40              NEGA                        
CF40: 40              NEGA                        
CF41: 28 80           BVC     $CEC3                   
CF43: 40              NEGA                        
CF44: 40              NEGA                        
CF45: 28 80           BVC     $CEC7                   
CF47: 40              NEGA                        
CF48: 40              NEGA                        
CF49: 28 80           BVC     $CECB                   
CF4B: 40              NEGA                        
CF4C: 40              NEGA                        
CF4D: 19              DAA                         
CF4E: 5F              CLRB                        
CF4F: 19              DAA                         
CF50: 64 19           LSR     -7,X                
CF52: 5F              CLRB                        
CF53: 1A 55           ORCC    #$55                  
CF55: 1C 4B           ANDCC   #$4B                  
CF57: 1C 55           ANDCC   #$55                  
CF59: 1C 4B           ANDCC   #$4B                  
CF5B: 1C 43           ANDCC   #$43                  
CF5D: 40              NEGA                        
CF5E: 40              NEGA                        
CF5F: 00 00           NEG     $00                   
CF61: 28 80           BVC     $CEE3                   
CF63: 40              NEGA                        
CF64: 40              NEGA                        
CF65: 40              NEGA                        
CF66: 43              COMA                        
CF67: 40              NEGA                        
CF68: 40              NEGA                        
CF69: 37 5F           PULU    $5F                   
CF6B: 37 4B           PULU    $4B                   
CF6D: 37 55           PULU    $55                   
CF6F: 37 4B           PULU    $4B                   
CF71: 19              DAA                         
CF72: 5F              CLRB                        
CF73: 19              DAA                         
CF74: 64 19           LSR     -7,X                
CF76: 5F              CLRB                        
CF77: 1A 55           ORCC    #$55                  
CF79: 1C 4B           ANDCC   #$4B                  
CF7B: 1C 55           ANDCC   #$55                  
CF7D: 1C 4B           ANDCC   #$4B                  
CF7F: 1C 43           ANDCC   #$43                  
CF81: 40              NEGA                        
CF82: 40              NEGA                        
CF83: 00 00           NEG     $00                   
CF85: 28 80           BVC     $CF07                   
CF87: 40              NEGA                        
CF88: 40              NEGA                        
CF89: 40              NEGA                        
CF8A: 43              COMA                        
CF8B: 3C 4B           CWAI    $4B                   
CF8D: 39              RTS                         
CF8E: 55 ; ????
CF8F: 37 5F           PULU    $5F                   
CF91: 37 64           PULU    $64                   
CF93: 37 5F           PULU    $5F                   
CF95: 39              RTS                         
CF96: 55 ; ????
CF97: 3C 4B           CWAI    $4B                   
CF99: 40              NEGA                        
CF9A: 43              COMA                        
CF9B: 39              RTS                         
CF9C: 55 ; ????
CF9D: 40              NEGA                        
CF9E: 40              NEGA                        
CF9F: 00 00           NEG     $00                   
CFA1: 14 ; ????
CFA2: 1E 00           EXG     $00                   
CFA4: 00 FF           NEG     $FF                   
CFA6: FF 00 00        STU     $0000                   
CFA9: 00 07           NEG     $07                   
CFAB: 0A 0F           DEC     $0F                   
CFAD: 14 ; ????
CFAE: 19              DAA                         
CFAF: 1E 32           EXG     $32                   
CFB1: 00 64           NEG     $64                   
CFB3: 43              COMA                        
CFB4: 4F              CLRA                        
CFB5: 50              NEGB                        
CFB6: 59              ROLB                        
CFB7: 52 ; ????
CFB8: 49              ROLA                        
CFB9: 47              ASRA                        
CFBA: 48 ; ????
CFBB: 54              LSRB                        
CFBC: 20 31           BRA     $CFEF                   
CFBE: 39              RTS                         
CFBF: 38 ; ????
CFC0: 32 20           LEAS    0,Y                 
CFC2: 44              LSRA                        
CFC3: 41 ; ????
CFC4: 4C              INCA                        
CFC5: 45 ; ????
CFC6: 20 41           BRA     $D009                   
CFC8: 2E 20           BGT     $CFEA                   
CFCA: 4C              INCA                        
CFCB: 45 ; ????
CFCC: 41 ; ????
CFCD: 52 ; ????
CFCE: 20 41           BRA     $D011                   
CFD0: 4C              INCA                        
CFD1: 4C              INCA                        
CFD2: 20 52           BRA     $D026                   
CFD4: 49              ROLA                        
CFD5: 47              ASRA                        
CFD6: 48 ; ????
CFD7: 54              LSRB                        
CFD8: 53              COMB                        
CFD9: 20 52           BRA     $D02D                   
CFDB: 45 ; ????
CFDC: 53              COMB                        
CFDD: 45 ; ????
CFDE: 52 ; ????
CFDF: 56              RORB                        
CFE0: 45 ; ????
CFE1: 44              LSRA                        
CFE2: 20 4C           BRA     $D030                   
CFE4: 49              ROLA                        
CFE5: 43              COMA                        
CFE6: 45 ; ????
CFE7: 4E ; ????
CFE8: 53              COMB                        
CFE9: 45 ; ????
CFEA: 44              LSRA                        
CFEB: 20 54           BRA     $D041                   
CFED: 4F              CLRA                        
CFEE: 20 54           BRA     $D044                   
CFF0: 41 ; ????
CFF1: 4E ; ????
CFF2: 44              LSRA                        
CFF3: 59              ROLB                        
CFF4: 20 43           BRA     $D039                   
CFF6: 4F              CLRA                        
CFF7: 52 ; ????
CFF8: 50              NEGB                        
CFF9: 4F              CLRA                        
CFFA: 52 ; ????
CFFB: 41 ; ????
CFFC: 54              LSRB                        
CFFD: 49              ROLA                        
CFFE: 4F              CLRA                        
CFFF: 4E ; ????
```
