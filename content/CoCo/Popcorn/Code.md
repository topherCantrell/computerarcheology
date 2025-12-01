![Code](popcorn.jpg)

# Popcorn Code

>>> cpu 6809

>>> binary C000:roms/popcorn.bin

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](../Hardware.md)

```code
C000: 7E C3 76        JMP     $C376               ; {}

C003: 34 04           PSHS    B                   
C005: C6 20           LDB     #$20                
C007: 3D              MUL                         
C008: 8B 04           ADDA    #$04                
C00A: 1F 01           TFR     D,X                 
C00C: E6 E4           LDB     ,S                  
C00E: 54              LSRB                        
C00F: 54              LSRB                        
C010: 3A              ABX                         
C011: E6 E0           LDB     ,S+                 
C013: C4 03           ANDB    #$03                
C015: 10 8E C0 1C     LDY     #$C01C              
C019: E6 A5           LDB     B,Y                 
C01B: 39              RTS                         

C01C: C0 30           SUBB    #$30                
C01E: 0C 03           INC     $03                 
C020: 34 40           PSHS    U                   
C022: CE C5 B7        LDU     #$C5B7              
C025: C6 07           LDB     #$07                
C027: 3D              MUL                         
C028: 33 CB           LEAU    D,U                 
C02A: DC EA           LDD     $EA                 
C02C: 8D D5           BSR     $C003               ; {}
C02E: 86 07           LDA     #$07                
C030: 97 FE           STA     $FE                 
C032: A6 C0           LDA     ,U+                 
C034: 34 16           PSHS    X,B,A               
C036: D7 FC           STB     $FC                 
C038: C6 06           LDB     #$06                
C03A: 96 FC           LDA     $FC                 
C03C: 43              COMA                        
C03D: A4 84           ANDA    ,X                  
C03F: 64 E4           LSR     ,S                  
C041: 24 08           BHS     $C04B               ; {}
C043: 34 02           PSHS    A                   
C045: 96 FC           LDA     $FC                 
C047: 94 E9           ANDA    $E9                 
C049: AA E0           ORA     ,S+                 
C04B: A7 84           STA     ,X                  
C04D: 04 FC           LSR     $FC                 
C04F: 04 FC           LSR     $FC                 
C051: 26 06           BNE     $C059               ; {}
C053: 30 01           LEAX    1,X                 
C055: 86 C0           LDA     #$C0                
C057: 97 FC           STA     $FC                 
C059: 5A              DECB                        
C05A: 26 DE           BNE     $C03A               ; {}
C05C: 35 16           PULS    A,B,X               
C05E: 30 88 20        LEAX    $20,X               
C061: 0A FE           DEC     $FE                 
C063: 26 CD           BNE     $C032               ; {}
C065: 35 C0           PULS    U,PC                
C067: D6 DD           LDB     $DD                 
C069: 8E 03 64        LDX     #$0364              
C06C: AE 85           LDX     B,X                 
C06E: CC AA 61        LDD     #$AA61              
C071: 20 03           BRA     $C076               ; {}
C073: CC 55 21        LDD     #$5521              
C076: 97 E9           STA     $E9                 
C078: D7 EB           STB     $EB                 
C07A: C6 58           LDB     #$58                
C07C: D7 EA           STB     $EA                 
C07E: 0F FD           CLR     $FD                 
C080: 34 10           PSHS    X                   
C082: 35 02           PULS    A                   
C084: 8D 02           BSR     $C088               ; {}
C086: 35 02           PULS    A                   
C088: 34 02           PSHS    A                   
C08A: 44              LSRA                        
C08B: 44              LSRA                        
C08C: 44              LSRA                        
C08D: 44              LSRA                        
C08E: 8D 13           BSR     $C0A3               ; {}
C090: 35 02           PULS    A                   
C092: D6 EB           LDB     $EB                 
C094: CB 06           ADDB    #$06                
C096: D7 EB           STB     $EB                 
C098: 84 0F           ANDA    #$0F                
C09A: 8D 07           BSR     $C0A3               ; {}
C09C: D6 EB           LDB     $EB                 
C09E: CB 06           ADDB    #$06                
C0A0: D7 EB           STB     $EB                 
C0A2: 39              RTS                         
C0A3: 8B 1C           ADDA    #$1C                
C0A5: 0D FD           TST     $FD                 
C0A7: 10 26 FF 75     LBNE    $C020               ; {}
C0AB: 97 FD           STA     $FD                 
C0AD: 81 1C           CMPA    #$1C                
C0AF: 10 26 FF 6D     LBNE    $C020               ; {}
C0B3: 86 1A           LDA     #$1A                
C0B5: 0F FD           CLR     $FD                 
C0B7: 7E C0 20        JMP     $C020               ; {}
C0BA: 0F DC           CLR     $DC                 
C0BC: 03 DC           COM     $DC                 
C0BE: 20 02           BRA     $C0C2               ; {}
C0C0: 0F DC           CLR     $DC                 
C0C2: A6 80           LDA     ,X+                 
C0C4: 84 7F           ANDA    #$7F                
C0C6: 81 20           CMPA    #$20                
C0C8: 25 37           BCS     $C101               ; {}
C0CA: 26 06           BNE     $C0D2               ; {}
C0CC: 0D DC           TST     $DC                 
C0CE: 27 02           BEQ     $C0D2               ; {}
C0D0: 03 E9           COM     $E9                 
C0D2: 81 22           CMPA    #$22                
C0D4: 24 04           BHS     $C0DA               ; {}
C0D6: 80 06           SUBA    #$06                
C0D8: 20 12           BRA     $C0EC               ; {}
C0DA: 81 30           CMPA    #$30                
C0DC: 25 23           BCS     $C101               ; {}
C0DE: 81 3A           CMPA    #$3A                
C0E0: 24 04           BHS     $C0E6               ; {}
C0E2: 80 14           SUBA    #$14                
C0E4: 20 06           BRA     $C0EC               ; {}
C0E6: 80 41           SUBA    #$41                
C0E8: 81 1A           CMPA    #$1A                
C0EA: 24 15           BHS     $C101               ; {}
C0EC: 34 10           PSHS    X                   
C0EE: BD C0 20        JSR     $C020               ; {}
C0F1: 35 10           PULS    X                   
C0F3: 96 EB           LDA     $EB                 
C0F5: 8B 06           ADDA    #$06                
C0F7: 97 EB           STA     $EB                 
C0F9: 0D DC           TST     $DC                 
C0FB: 27 C5           BEQ     $C0C2               ; {}
C0FD: 03 E9           COM     $E9                 
C0FF: 20 C1           BRA     $C0C2               ; {}
C101: 39              RTS                         
C102: 34 44           PSHS    U,B                 
C104: 4C              INCA                        
C105: C6 20           LDB     #$20                
C107: 3D              MUL                         
C108: 8B 04           ADDA    #$04                
C10A: 1F 01           TFR     D,X                 
C10C: E6 E0           LDB     ,S+                 
C10E: 54              LSRB                        
C10F: 54              LSRB                        
C110: 3A              ABX                         
C111: 10 8E C1 50     LDY     #$C150              
C115: 86 FF           LDA     #$FF                
C117: 97 FD           STA     $FD                 
C119: 96 FF           LDA     $FF                 
C11B: CE C5 9B        LDU     #$C59B              
C11E: C6 03           LDB     #$03                
C120: 3D              MUL                         
C121: 33 C5           LEAU    B,U                 
C123: 86 03           LDA     #$03                
C125: 97 FE           STA     $FE                 
C127: C6 02           LDB     #$02                
C129: A6 A0           LDA     ,Y+                 
C12B: 43              COMA                        
C12C: A4 84           ANDA    ,X                  
C12E: 0D FF           TST     $FF                 
C130: 27 0C           BEQ     $C13E               ; {}
C132: A8 84           EORA    ,X                  
C134: 27 02           BEQ     $C138               ; {}
C136: 0F FD           CLR     $FD                 
C138: A6 3F           LDA     -1,Y                
C13A: A4 C4           ANDA    ,U                  
C13C: AA 84           ORA     ,X                  
C13E: A7 80           STA     ,X+                 
C140: 5A              DECB                        
C141: 26 E6           BNE     $C129               ; {}
C143: 30 88 1E        LEAX    $1E,X               
C146: 33 41           LEAU    1,U                 
C148: 0A FE           DEC     $FE                 
C14A: 26 DB           BNE     $C127               ; {}
C14C: 03 FD           COM     $FD                 
C14E: 35 C0           PULS    U,PC                
C150: 0F C0           CLR     $C0                 
C152: 3F              SWI                         
C153: FC 03 F0        LDD     $03F0               
C156: A6 41           LDA     1,U                 
C158: 81 52           CMPA    #$52                
C15A: 24 5A           BHS     $C1B6               ; {}
C15C: 0F FF           CLR     $FF                 
C15E: EC 41           LDD     1,U                 
C160: 8D A0           BSR     $C102               ; {}
C162: 6C 41           INC     1,U                 
C164: E6 43           LDB     3,U                 
C166: D7 FF           STB     $FF                 
C168: EC 41           LDD     1,U                 
C16A: 8D 96           BSR     $C102               ; {}
C16C: 0D FD           TST     $FD                 
C16E: 27 45           BEQ     $C1B5               ; {}
C170: A6 C4           LDA     ,U                  
C172: 84 FE           ANDA    #$FE                
C174: A7 C4           STA     ,U                  
C176: BD C2 32        JSR     $C232               ; {}
C179: 0F FF           CLR     $FF                 
C17B: EC 41           LDD     1,U                 
C17D: BD C1 02        JSR     $C102               ; {}
C180: 0A FA           DEC     $FA                 
C182: DC E1           LDD     $E1                 
C184: 10 83 0A F0     CMPD    #$0AF0              
C188: 24 0F           BHS     $C199               ; {}
C18A: D6 F1           LDB     $F1                 
C18C: 58              LSLB                        
C18D: EB 43           ADDB    3,U                 
C18F: 86 C8           LDA     #$C8                
C191: 3D              MUL                         
C192: 1F 89           TFR     A,B                 
C194: 4F              CLRA                        
C195: D3 E1           ADDD    $E1                 
C197: DD E1           STD     $E1                 
C199: 96 FB           LDA     $FB                 
C19B: 9A FA           ORA     $FA                 
C19D: 26 16           BNE     $C1B5               ; {}
C19F: BD C2 F1        JSR     $C2F1               ; {}
C1A2: 86 6E           LDA     #$6E                
C1A4: 97 F6           STA     $F6                 
C1A6: 96 E3           LDA     $E3                 
C1A8: 4C              INCA                        
C1A9: 81 08           CMPA    #$08                
C1AB: 24 02           BHS     $C1AF               ; {}
C1AD: 97 E3           STA     $E3                 
C1AF: 0C F1           INC     $F1                 
C1B1: 26 02           BNE     $C1B5               ; {}
C1B3: 0A F1           DEC     $F1                 
C1B5: 39              RTS                         
C1B6: 10 8E 03 00     LDY     #$0300              
C1BA: 0F FF           CLR     $FF                 
C1BC: C6 05           LDB     #$05                
C1BE: A6 A4           LDA     ,Y                  
C1C0: 85 01           BITA    #$01                
C1C2: 27 0D           BEQ     $C1D1               ; {}
C1C4: 84 FE           ANDA    #$FE                
C1C6: A7 A4           STA     ,Y                  
C1C8: 34 24           PSHS    Y,B                 
C1CA: EC 21           LDD     1,Y                 
C1CC: BD C1 02        JSR     $C102               ; {}
C1CF: 35 24           PULS    B,Y                 
C1D1: 31 24           LEAY    4,Y                 
C1D3: 5A              DECB                        
C1D4: 26 E8           BNE     $C1BE               ; {}
C1D6: 0F FF           CLR     $FF                 
C1D8: 03 FF           COM     $FF                 
C1DA: BD C2 B6        JSR     $C2B6               ; {}
C1DD: A6 43           LDA     3,U                 
C1DF: 97 FF           STA     $FF                 
C1E1: EC 41           LDD     1,U                 
C1E3: BD C1 02        JSR     $C102               ; {}
C1E6: 86 80           LDA     #$80                
C1E8: A0 42           SUBA    2,U                 
C1EA: 97 F2           STA     $F2                 
C1EC: 86 96           LDA     #$96                
C1EE: 97 FE           STA     $FE                 
C1F0: 86 02           LDA     #$02                
C1F2: B7 FF 20        STA     $FF20               ; {hard.PIA1_DA}
C1F5: C6 05           LDB     #$05                
C1F7: 96 FE           LDA     $FE                 
C1F9: 4A              DECA                        
C1FA: 12              NOP                         
C1FB: 12              NOP                         
C1FC: 26 FB           BNE     $C1F9               ; {}
C1FE: B6 FF 20        LDA     $FF20               ; {hard.PIA1_DA}
C201: 88 FC           EORA    #$FC                
C203: B7 FF 20        STA     $FF20               ; {hard.PIA1_DA}
C206: 5A              DECB                        
C207: 26 EE           BNE     $C1F7               ; {}
C209: D6 FE           LDB     $FE                 
C20B: 5C              INCB                        
C20C: D7 FE           STB     $FE                 
C20E: C1 C8           CMPB    #$C8                
C210: 25 E3           BCS     $C1F5               ; {}
C212: 0D F2           TST     $F2                 
C214: 26 FC           BNE     $C212               ; {}
C216: DC E1           LDD     $E1                 
C218: 10 83 02 58     CMPD    #$0258              
C21C: 25 04           BCS     $C222               ; {}
C21E: 44              LSRA                        
C21F: 56              RORB                        
C220: DD E1           STD     $E1                 
C222: 0A E3           DEC     $E3                 
C224: 10 27 01 D6     LBEQ    $C3FE               ; {}
C228: 0F FA           CLR     $FA                 
C22A: BD C2 F1        JSR     $C2F1               ; {}
C22D: 0F FA           CLR     $FA                 
C22F: 7E C4 9B        JMP     $C49B               ; {}

C232: 86 02           LDA     #$02                
C234: B7 FF 20        STA     $FF20               ; {hard.PIA1_DA}
C237: C6 50           LDB     #$50                
C239: 1F 98           TFR     B,A                 
C23B: 4A              DECA                        
C23C: 26 FD           BNE     $C23B               ; {}
C23E: B6 FF 20        LDA     $FF20               ; {hard.PIA1_DA}
C241: 88 E0           EORA    #$E0                
C243: B7 FF 20        STA     $FF20               ; {hard.PIA1_DA}
C246: 5A              DECB                        
C247: C1 14           CMPB    #$14                
C249: 24 EE           BHS     $C239               ; {}
C24B: A6 43           LDA     3,U                 
C24D: 9B F0           ADDA    $F0                 
C24F: 19              DAA                         
C250: 97 F0           STA     $F0                 
C252: 96 EF           LDA     $EF                 
C254: 89 00           ADCA    #$00                
C256: 19              DAA                         
C257: 97 EF           STA     $EF                 
C259: 9E EF           LDX     $EF                 
C25B: 7E C0 73        JMP     $C073               ; {}
C25E: B6 FF 20        LDA     $FF20               ; {hard.PIA1_DA}
C261: F6 FF 23        LDB     $FF23               ; {hard.PIA1_CB}
C264: 34 46           PSHS    U,B,A               
C266: 17 E7 0B        LBSR    $A974               
C269: 8E 01 5B        LDX     #$015B              
C26C: 5F              CLRB                        
C26D: 17 E7 75        LBSR    $A9E5               
C270: 35 46           PULS    A,B,U               
C272: B7 FF 20        STA     $FF20               ; {hard.PIA1_DA}
C275: F7 FF 23        STB     $FF23               ; {hard.PIA1_CB}
C278: B6 01 5A        LDA     $015A               
C27B: 80 01           SUBA    #$01                
C27D: 24 02           BHS     $C281               ; {}
C27F: 4F              CLRA                        
C280: 39              RTS                         
C281: 81 3B           CMPA    #$3B                
C283: 25 02           BCS     $C287               ; {}
C285: 86 3A           LDA     #$3A                
C287: 39              RTS                         
C288: BD A1 C1        JSR     $A1C1               ; {hard.GETKEY}
C28B: 81 03           CMPA    #$03                
C28D: 10 27 01 6D     LBEQ    $C3FE               ; {}
C291: 81 20           CMPA    #$20                
C293: 26 0D           BNE     $C2A2               ; {}
C295: BD A1 C1        JSR     $A1C1               ; {hard.GETKEY}
C298: 81 03           CMPA    #$03                
C29A: 10 27 01 60     LBEQ    $C3FE               ; {}
C29E: 81 20           CMPA    #$20                
C2A0: 26 F3           BNE     $C295               ; {}
C2A2: 8D BA           BSR     $C25E               ; {}
C2A4: 91 E4           CMPA    $E4                 
C2A6: 27 0A           BEQ     $C2B2               ; {}
C2A8: 34 02           PSHS    A                   
C2AA: 0F FF           CLR     $FF                 
C2AC: 8D 08           BSR     $C2B6               ; {}
C2AE: 35 02           PULS    A                   
C2B0: 97 E4           STA     $E4                 
C2B2: 0F FF           CLR     $FF                 
C2B4: 03 FF           COM     $FF                 
C2B6: D6 E4           LDB     $E4                 
C2B8: 54              LSRB                        
C2B9: 8E 0E 20        LDX     #$0E20              
C2BC: 3A              ABX                         
C2BD: 86 F0           LDA     #$F0                
C2BF: C6 01           LDB     #$01                
C2C1: D5 E4           BITB    $E4                 
C2C3: 27 02           BEQ     $C2C7               ; {}
C2C5: 86 0F           LDA     #$0F                
C2C7: D6 E3           LDB     $E3                 
C2C9: 34 16           PSHS    X,B,A               
C2CB: 97 FC           STA     $FC                 
C2CD: C6 06           LDB     #$06                
C2CF: 96 FC           LDA     $FC                 
C2D1: 43              COMA                        
C2D2: A4 84           ANDA    ,X                  
C2D4: A7 E2           STA     ,-S                 
C2D6: 96 FC           LDA     $FC                 
C2D8: 94 FF           ANDA    $FF                 
C2DA: AA E0           ORA     ,S+                 
C2DC: A7 84           STA     ,X                  
C2DE: 03 FC           COM     $FC                 
C2E0: 2A 02           BPL     $C2E4               ; {}
C2E2: 30 01           LEAX    1,X                 
C2E4: 5A              DECB                        
C2E5: 26 E8           BNE     $C2CF               ; {}
C2E7: 35 16           PULS    A,B,X               
C2E9: 30 89 FF 00     LEAX    $FF00,X             
C2ED: 5A              DECB                        
C2EE: 26 D9           BNE     $C2C9               ; {}
C2F0: 39              RTS                         
C2F1: 8D 3B           BSR     $C32E               ; {}
C2F3: 8E 03 14        LDX     #$0314              
C2F6: 86 05           LDA     #$05                
C2F8: 97 FE           STA     $FE                 
C2FA: C6 50           LDB     #$50                
C2FC: D7 FB           STB     $FB                 
C2FE: 96 FE           LDA     $FE                 
C300: C6 10           LDB     #$10                
C302: A7 80           STA     ,X+                 
C304: 5A              DECB                        
C305: 26 FB           BNE     $C302               ; {}
C307: 0A FE           DEC     $FE                 
C309: 26 F3           BNE     $C2FE               ; {}
C30B: 4F              CLRA                        
C30C: 8E 03 14        LDX     #$0314              
C30F: 34 02           PSHS    A                   
C311: 5F              CLRB                        
C312: A6 80           LDA     ,X+                 
C314: 97 FF           STA     $FF                 
C316: A6 E4           LDA     ,S                  
C318: 34 14           PSHS    X,B                 
C31A: BD C1 02        JSR     $C102               ; {}
C31D: 35 14           PULS    B,X                 
C31F: CB 08           ADDB    #$08                
C321: C1 80           CMPB    #$80                
C323: 25 ED           BCS     $C312               ; {}
C325: A6 E0           LDA     ,S+                 
C327: 8B 04           ADDA    #$04                
C329: 81 14           CMPA    #$14                
C32B: 25 E2           BCS     $C30F               ; {}
C32D: 39              RTS                         
C32E: 8E 05 80        LDX     #$0580              
C331: CE 0F 00        LDU     #$0F00              
C334: 4F              CLRA                        
C335: 5F              CLRB                        
C336: ED C3           STD     ,--U                
C338: 30 1F           LEAX    -1,X                
C33A: 26 FA           BNE     $C336               ; {}
C33C: 39              RTS                         
C33D: 53              COMB                        
C33E: 43              COMA                        
C33F: 4F              CLRA                        
C340: 52 ; ????
C341: 45 ; ????
C342: 00 48           NEG     $48                 
C344: 49              ROLA                        
C345: 47              ASRA                        
C346: 48              ASLA                        
C347: 00 4C           NEG     $4C                 
C349: 45 ; ????
C34A: 56              RORB                        
C34B: 45 ; ????
C34C: 4C              INCA                        
C34D: 20 00           BRA     $C34F               ; {}
C34F: 96 E9           LDA     $E9                 
C351: D6 FE           LDB     $FE                 
C353: 34 06           PSHS    B,A                 
C355: 86 FF           LDA     #$FF                
C357: 97 E9           STA     $E9                 
C359: 8E C3 48        LDX     #$C348              
C35C: CC 4E 4E        LDD     #$4E4E              
C35F: DD EA           STD     $EA                 
C361: BD C0 C0        JSR     $C0C0               ; {}
C364: 96 DD           LDA     $DD                 
C366: 44              LSRA                        
C367: 8B 1D           ADDA    #$1D                
C369: BD C0 20        JSR     $C020               ; {}
C36C: BD C0 67        JSR     $C067               ; {}
C36F: 35 06           PULS    A,B                 
C371: D7 FE           STB     $FE                 
C373: 97 E9           STA     $E9                 
C375: 39              RTS                         
C376: 10 CE 02 FE     LDS     #$02FE              
C37A: BD C6 D7        JSR     $C6D7               ; {}
C37D: 12              NOP                         
C37E: 1A 50           ORCC    #$50                
C380: 8E C5 54        LDX     #$C554              
C383: BF 01 0D        STX     $010D               
C386: 86 E0           LDA     #$E0                
C388: 97 F3           STA     $F3                 
C38A: 86 34           LDA     #$34                
C38C: B7 FF 01        STA     $FF01               ; {hard.PIA0_CA}
C38F: B7 FF 21        STA     $FF21               ; {hard.PIA1_CA}
C392: B7 FF 23        STA     $FF23               ; {hard.PIA1_CB}
C395: 4C              INCA                        
C396: B7 FF 03        STA     $FF03               ; {hard.PIA0_CB}
C399: 8E C3 7D        LDX     #$C37D              
C39C: 9F 72           STX     $72                 
C39E: 86 55           LDA     #$55                
C3A0: 97 71           STA     $71                 
C3A2: 1C EF           ANDCC   #$EF                
C3A4: 86 35           LDA     #$35                
C3A6: B7 FF 03        STA     $FF03               ; {hard.PIA0_CB}
C3A9: 86 FF           LDA     #$FF                
C3AB: B7 FF 22        STA     $FF22               ; {hard.PIA1_DB}
C3AE: 8E 04 00        LDX     #$0400              
C3B1: 10 CE 02 FE     LDS     #$02FE              
C3B5: 6F 80           CLR     ,X+                 
C3B7: 8C 10 00        CMPX    #$1000              
C3BA: 25 F9           BCS     $C3B5               ; {}
C3BC: B7 FF C0        STA     $FFC0               ; {hard.dispMode}
C3BF: B7 FF C2        STA     $FFC2               ; {hard.dispMode+2}
C3C2: B7 FF C5        STA     $FFC5               ; {hard.dispMode+5}
C3C5: 8E C3 3D        LDX     #$C33D              
C3C8: 86 58           LDA     #$58                
C3CA: 97 EA           STA     $EA                 
C3CC: 86 01           LDA     #$01                
C3CE: 97 EB           STA     $EB                 
C3D0: 86 55           LDA     #$55                
C3D2: 97 E9           STA     $E9                 
C3D4: BD C0 C0        JSR     $C0C0               ; {}
C3D7: CC AA 47        LDD     #$AA47              
C3DA: 97 E9           STA     $E9                 
C3DC: D7 EB           STB     $EB                 
C3DE: 8E C3 43        LDX     #$C343              
C3E1: BD C0 C0        JSR     $C0C0               ; {}
C3E4: 4F              CLRA                        
C3E5: 5F              CLRB                        
C3E6: DD EF           STD     $EF                 
C3E8: 8E 03 64        LDX     #$0364              
C3EB: C6 12           LDB     #$12                
C3ED: 6F 80           CLR     ,X+                 
C3EF: 5A              DECB                        
C3F0: 26 FB           BNE     $C3ED               ; {}
C3F2: 0F DD           CLR     $DD                 
C3F4: BD C0 67        JSR     $C067               ; {}
C3F7: 86 1C           LDA     #$1C                
C3F9: BD C0 20        JSR     $C020               ; {}
C3FC: 0F DD           CLR     $DD                 
C3FE: 10 CE 02 FE     LDS     #$02FE              
C402: D6 DD           LDB     $DD                 
C404: 8E 03 64        LDX     #$0364              
C407: 3A              ABX                         
C408: DC EF           LDD     $EF                 
C40A: 10 A3 84        CMPD    ,X                  
C40D: 25 02           BCS     $C411               ; {}
C40F: ED 84           STD     ,X                  
C411: BD C3 2E        JSR     $C32E               ; {}
C414: BD C2 F1        JSR     $C2F1               ; {}
C417: BD C3 4F        JSR     $C34F               ; {}
C41A: 86 AA           LDA     #$AA                
C41C: 97 E9           STA     $E9                 
C41E: 86 0C           LDA     #$0C                
C420: 97 FE           STA     $FE                 
C422: 0A FE           DEC     $FE                 
C424: 26 18           BNE     $C43E               ; {}
C426: 8E C5 AD        LDX     #$C5AD              
C429: CC 23 24        LDD     #$2324              
C42C: DD EA           STD     $EA                 
C42E: 86 09           LDA     #$09                
C430: 34 02           PSHS    A                   
C432: BD C0 BA        JSR     $C0BA               ; {}
C435: 35 02           PULS    A                   
C437: 03 E9           COM     $E9                 
C439: 4A              DECA                        
C43A: 26 F4           BNE     $C430               ; {}
C43C: 20 E0           BRA     $C41E               ; {}
C43E: 17 DD 80        LBSR    $A1C1               ; {hard.GETKEY}
C441: 80 31           SUBA    #$31                
C443: 25 0A           BCS     $C44F               ; {}
C445: 81 09           CMPA    #$09                
C447: 24 06           BHS     $C44F               ; {}
C449: 48              ASLA                        
C44A: 97 DD           STA     $DD                 
C44C: BD C3 4F        JSR     $C34F               ; {}
C44F: 86 FF           LDA     #$FF                
C451: B7 FF 02        STA     $FF02               ; {hard.PIA0_DB}
C454: 13              SYNC                        
C455: B6 FF 00        LDA     $FF00               ; {hard.PIA0_DA}
C458: 85 01           BITA    #$01                
C45A: 26 C6           BNE     $C422               ; {}
C45C: BD C3 2E        JSR     $C32E               ; {}
C45F: BD C2 F1        JSR     $C2F1               ; {}
C462: 8E 00 00        LDX     #$0000              
C465: 9F EF           STX     $EF                 
C467: BD C0 73        JSR     $C073               ; {}
C46A: 86 1C           LDA     #$1C                
C46C: BD C0 20        JSR     $C020               ; {}
C46F: BD C0 67        JSR     $C067               ; {}
C472: 86 03           LDA     #$03                
C474: 97 EC           STA     $EC                 
C476: 86 20           LDA     #$20                
C478: 90 DD           SUBA    $DD                 
C47A: 97 F8           STA     $F8                 
C47C: 86 20           LDA     #$20                
C47E: 97 E4           STA     $E4                 
C480: 86 06           LDA     #$06                
C482: 97 E3           STA     $E3                 
C484: CC 09 CF        LDD     #$09CF              
C487: DD E5           STD     $E5                 
C489: 96 DD           LDA     $DD                 
C48B: C6 32           LDB     #$32                
C48D: 3D              MUL                         
C48E: C3 01 F4        ADDD    #$01F4              
C491: DD E1           STD     $E1                 
C493: 0F DE           CLR     $DE                 
C495: 0C DE           INC     $DE                 
C497: 96 DD           LDA     $DD                 
C499: 97 F1           STA     $F1                 
C49B: CE 03 00        LDU     #$0300              
C49E: 86 05           LDA     #$05                
C4A0: 6F C4           CLR     ,U                  
C4A2: 33 44           LEAU    4,U                 
C4A4: 4A              DECA                        
C4A5: 26 F9           BNE     $C4A0               ; {}
C4A7: 10 CE 02 FE     LDS     #$02FE              
C4AB: 86 6E           LDA     #$6E                
C4AD: 97 F6           STA     $F6                 
C4AF: 0F FA           CLR     $FA                 
C4B1: 86 64           LDA     #$64                
C4B3: 97 F5           STA     $F5                 
C4B5: B6 FF 23        LDA     $FF23               ; {hard.PIA1_CB}
C4B8: 8A 08           ORA     #$08                
C4BA: B7 FF 23        STA     $FF23               ; {hard.PIA1_CB}
C4BD: 0A F5           DEC     $F5                 
C4BF: 26 10           BNE     $C4D1               ; {}
C4C1: 96 E8           LDA     $E8                 
C4C3: 84 3F           ANDA    #$3F                
C4C5: 8B B4           ADDA    #$B4                
C4C7: 97 F5           STA     $F5                 
C4C9: 86 2E           LDA     #$2E                
C4CB: B8 FF 20        EORA    $FF20               ; {hard.PIA1_DA}
C4CE: B7 FF 20        STA     $FF20               ; {hard.PIA1_DA}
C4D1: DC E7           LDD     $E7                 
C4D3: D3 E5           ADDD    $E5                 
C4D5: DD E7           STD     $E7                 
C4D7: 24 03           BHS     $C4DC               ; {}
C4D9: BD C2 88        JSR     $C288               ; {}
C4DC: DC DF           LDD     $DF                 
C4DE: D3 E1           ADDD    $E1                 
C4E0: DD DF           STD     $DF                 
C4E2: 24 D9           BHS     $C4BD               ; {}
C4E4: CE 03 00        LDU     #$0300              
C4E7: C6 05           LDB     #$05                
C4E9: A6 C4           LDA     ,U                  
C4EB: 85 01           BITA    #$01                
C4ED: 27 07           BEQ     $C4F6               ; {}
C4EF: 34 04           PSHS    B                   
C4F1: BD C1 56        JSR     $C156               ; {}
C4F4: 35 04           PULS    B                   
C4F6: 33 44           LEAU    4,U                 
C4F8: 5A              DECB                        
C4F9: 26 EE           BNE     $C4E9               ; {}
C4FB: 0A F6           DEC     $F6                 
C4FD: 26 BE           BNE     $C4BD               ; {}
C4FF: 96 F8           LDA     $F8                 
C501: 97 F6           STA     $F6                 
C503: 96 FA           LDA     $FA                 
C505: 81 05           CMPA    #$05                
C507: 24 B4           BHS     $C4BD               ; {}
C509: 0D FB           TST     $FB                 
C50B: 27 B0           BEQ     $C4BD               ; {}
C50D: 10 8E 03 00     LDY     #$0300              
C511: C6 05           LDB     #$05                
C513: A6 A4           LDA     ,Y                  
C515: 85 01           BITA    #$01                
C517: 27 07           BEQ     $C520               ; {}
C519: 31 24           LEAY    4,Y                 
C51B: 5A              DECB                        
C51C: 26 F5           BNE     $C513               ; {}
C51E: 20 9D           BRA     $C4BD               ; {}
C520: 8A 01           ORA     #$01                
C522: A7 A4           STA     ,Y                  
C524: 96 FB           LDA     $FB                 
C526: 4A              DECA                        
C527: 84 F0           ANDA    #$F0                
C529: 1F 89           TFR     A,B                 
C52B: 96 FB           LDA     $FB                 
C52D: 4A              DECA                        
C52E: 84 0F           ANDA    #$0F                
C530: 94 E8           ANDA    $E8                 
C532: 8E 03 14        LDX     #$0314              
C535: 3A              ABX                         
C536: 54              LSRB                        
C537: 54              LSRB                        
C538: E7 21           STB     1,Y                 
C53A: C6 F8           LDB     #$F8                
C53C: CB 08           ADDB    #$08                
C53E: 6D 80           TST     ,X+                 
C540: 27 FA           BEQ     $C53C               ; {}
C542: 4A              DECA                        
C543: 2A F7           BPL     $C53C               ; {}
C545: E7 22           STB     2,Y                 
C547: A6 1F           LDA     -1,X                
C549: A7 23           STA     3,Y                 
C54B: 6F 1F           CLR     -1,X                
C54D: 0A FB           DEC     $FB                 
C54F: 0C FA           INC     $FA                 
C551: 7E C4 BD        JMP     $C4BD               ; {}
C554: 96 F3           LDA     $F3                 
C556: 1F 89           TFR     A,B                 
C558: 56              RORB                        
C559: 46              RORA                        
C55A: 0D F2           TST     $F2                 
C55C: 27 02           BEQ     $C560               ; {}
C55E: 56              RORB                        
C55F: 46              RORA                        
C560: 97 F3           STA     $F3                 
C562: C6 20           LDB     #$20                
C564: 8E 0E C0        LDX     #$0EC0              
C567: A7 80           STA     ,X+                 
C569: 5A              DECB                        
C56A: 26 FB           BNE     $C567               ; {}
C56C: 96 F2           LDA     $F2                 
C56E: 27 24           BEQ     $C594               ; {}
C570: 4A              DECA                        
C571: 97 F2           STA     $F2                 
C573: 86 03           LDA     #$03                
C575: 8E 0E 60        LDX     #$0E60              
C578: 34 02           PSHS    A                   
C57A: 86 02           LDA     #$02                
C57C: C6 20           LDB     #$20                
C57E: 34 10           PSHS    X                   
C580: 1C FE           ANDCC   #$FE                
C582: 66 80           ROR     ,X+                 
C584: 5A              DECB                        
C585: 26 FB           BNE     $C582               ; {}
C587: 35 10           PULS    X                   
C589: 4A              DECA                        
C58A: 26 F0           BNE     $C57C               ; {}
C58C: 35 02           PULS    A                   
C58E: 30 88 20        LEAX    $20,X               
C591: 4A              DECA                        
C592: 26 E4           BNE     $C578               ; {}
C594: B6 FF 02        LDA     $FF02               ; {hard.PIA0_DB}
C597: B6 FF 03        LDA     $FF03               ; {hard.PIA0_CB}
C59A: 3B              RTI                         
C59B: 00 00           NEG     $00                 
C59D: 00 FF           NEG     $FF                 
C59F: FF FF 55        STU     $FF55               
C5A2: 55 ; ????
C5A3: 55 ; ????
C5A4: 55 ; ????
C5A5: AA 55           ORA     -11,U               
C5A7: AA ; ????
C5A8: AA ; ????
C5A9: AA ; ????
C5AA: AA 55           ORA     -11,U               
C5AC: AA 47           ORA     7,U                 
C5AE: 41 ; ????
C5AF: 4D              TSTA                        
C5B0: 45 ; ????
C5B1: 20 4F           BRA     $C602               ; {}
C5B3: 56              RORB                        
C5B4: 45 ; ????
C5B5: 52 ; ????
C5B6: 00 04           NEG     $04                 
C5B8: 0A 11           DEC     $11                 
C5BA: 11 ; ????
C5BB: 1F 11           TFR     X,X                 
C5BD: 11 ; ????
C5BE: 0F 12           CLR     $12                 
C5C0: 12              NOP                         
C5C1: 0E 12           JMP     $12                 
C5C3: 12              NOP                         
C5C4: 0F 0E           CLR     $0E                 
C5C6: 11 ; ????
C5C7: 01 ; ????
C5C8: 01 ; ????
C5C9: 01 ; ????
C5CA: 11 ; ????
C5CB: 0E 0F           JMP     $0F                 
C5CD: 12              NOP                         
C5CE: 12              NOP                         
C5CF: 12              NOP                         
C5D0: 12              NOP                         
C5D1: 12              NOP                         
C5D2: 0F 1F           CLR     $1F                 
C5D4: 01 ; ????
C5D5: 01 ; ????
C5D6: 0F 01           CLR     $01                 
C5D8: 01 ; ????
C5D9: 1F 1F           TFR     X,?                 
C5DB: 01 ; ????
C5DC: 01 ; ????
C5DD: 07 01           ASR     $01                 
C5DF: 01 ; ????
C5E0: 01 ; ????
C5E1: 0E 11           JMP     $11                 
C5E3: 01 ; ????
C5E4: 19              DAA                         
C5E5: 11 ; ????
C5E6: 11 ; ????
C5E7: 0E 11           JMP     $11                 
C5E9: 11 ; ????
C5EA: 11 ; ????
C5EB: 1F 11           TFR     X,X                 
C5ED: 11 ; ????
C5EE: 11 ; ????
C5EF: 0E 04           JMP     $04                 
C5F1: 04 04           LSR     $04                 
C5F3: 04 04           LSR     $04                 
C5F5: 0E 1C           JMP     $1C                 
C5F7: 08 08           LSL     $08                 
C5F9: 08 09           LSL     $09                 
C5FB: 09 06           ROL     $06                 
C5FD: 11 ; ????
C5FE: 09 05           ROL     $05                 
C600: 03 05           COM     $05                 
C602: 09 11           ROL     $11                 
C604: 01 ; ????
C605: 01 ; ????
C606: 01 ; ????
C607: 01 ; ????
C608: 01 ; ????
C609: 01 ; ????
C60A: 1F 11           TFR     X,X                 
C60C: 1B ; ????
C60D: 15 ; ????
C60E: 15 ; ????
C60F: 11 ; ????
C610: 11 ; ????
C611: 11 ; ????
C612: 11 ; ????
C613: 13              SYNC                        
C614: 15 ; ????
C615: 19              DAA                         
C616: 11 ; ????
C617: 11 ; ????
C618: 11 ; ????
C619: 0E 11           JMP     $11                 
C61B: 11 ; ????
C61C: 11 ; ????
C61D: 11 ; ????
C61E: 11 ; ????
C61F: 0E 0F           JMP     $0F                 
C621: 11 ; ????
C622: 11 ; ????
C623: 0F 01           CLR     $01                 
C625: 01 ; ????
C626: 01 ; ????
C627: 0E 11           JMP     $11                 
C629: 11 ; ????
C62A: 11 ; ????
C62B: 15 ; ????
C62C: 09 16           ROL     $16                 
C62E: 0F 11           CLR     $11                 
C630: 11 ; ????
C631: 0F 05           CLR     $05                 
C633: 09 11           ROL     $11                 
C635: 0E 11           JMP     $11                 
C637: 01 ; ????
C638: 0E 10           JMP     $10                 
C63A: 11 ; ????
C63B: 0E 1F           JMP     $1F                 
C63D: 15 ; ????
C63E: 04 04           LSR     $04                 
C640: 04 04           LSR     $04                 
C642: 0E 11           JMP     $11                 
C644: 11 ; ????
C645: 11 ; ????
C646: 11 ; ????
C647: 11 ; ????
C648: 11 ; ????
C649: 0E 11           JMP     $11                 
C64B: 11 ; ????
C64C: 11 ; ????
C64D: 0A 0A           DEC     $0A                 
C64F: 04 04           LSR     $04                 
C651: 11 ; ????
C652: 11 ; ????
C653: 11 ; ????
C654: 11 ; ????
C655: 15 ; ????
C656: 15 ; ????
C657: 0A 11           DEC     $11                 
C659: 11 ; ????
C65A: 0A 04           DEC     $04                 
C65C: 0A 11           DEC     $11                 
C65E: 11 ; ????
C65F: 11 ; ????
C660: 11 ; ????
C661: 0A 04           DEC     $04                 
C663: 04 04           LSR     $04                 
C665: 04 1F           LSR     $1F                 
C667: 11 ; ????
C668: 08 04           LSL     $04                 
C66A: 02 ; ????
C66B: 11 ; ????
C66C: 1F 00           TFR     D,D                 
C66E: 00 00           NEG     $00                 
C670: 00 00           NEG     $00                 
C672: 00 00           NEG     $00                 
C674: 04 04           LSR     $04                 
C676: 04 04           LSR     $04                 
C678: 04 00           LSR     $00                 
C67A: 04 0E           LSR     $0E                 
C67C: 11 ; ????
C67D: 19              DAA                         
C67E: 15 ; ????
C67F: 13              SYNC                        
C680: 11 ; ????
C681: 0E 04           JMP     $04                 
C683: 06 04           ROR     $04                 
C685: 04 04           LSR     $04                 
C687: 04 0E           LSR     $0E                 
C689: 0E 11           JMP     $11                 
C68B: 10 ; ????
C68C: 0E 01           JMP     $01                 
C68E: 01 ; ????
C68F: 1F 0E           TFR     D,?                 
C691: 11 ; ????
C692: 10 ; ????
C693: 0C 10           INC     $10                 
C695: 11 ; ????
C696: 0E 08           JMP     $08                 
C698: 0C 0A           INC     $0A                 
C69A: 1F 08           TFR     D,A                 
C69C: 08 08           LSL     $08                 
C69E: 1F 01           TFR     D,X                 
C6A0: 01 ; ????
C6A1: 0F 10           CLR     $10                 
C6A3: 10 ; ????
C6A4: 0F 0C           CLR     $0C                 
C6A6: 02 ; ????
C6A7: 01 ; ????
C6A8: 0F 11           CLR     $11                 
C6AA: 11 ; ????
C6AB: 0E 1F           JMP     $1F                 
C6AD: 10 ; ????
C6AE: 08 04           LSL     $04                 
C6B0: 02 ; ????
C6B1: 01 ; ????
C6B2: 01 ; ????
C6B3: 0E 11           JMP     $11                 
C6B5: 11 ; ????
C6B6: 0E 11           JMP     $11                 
C6B8: 11 ; ????
C6B9: 0E 0E           JMP     $0E                 
C6BB: 11 ; ????
C6BC: 11 ; ????
C6BD: 1E 10           EXG     X,D                 
C6BF: 08 06           LSL     $06                 
C6C1: AE E1           LDX     ,S++                
C6C3: A6 80           LDA     ,X+                 
C6C5: 27 05           BEQ     $C6CC               ; {}
C6C7: 17 DC 40        LBSR    $A30A               ; {hard.PRINTCHAR}
C6CA: 20 F7           BRA     $C6C3               ; {}
C6CC: 6E 84           JMP     ,X                  
C6CE: 8B 10           ADDA    #$10                
C6D0: 8A 8F           ORA     #$8F                
C6D2: 81 8F           CMPA    #$8F                
C6D4: 27 F8           BEQ     $C6CE               ; {}
C6D6: 39              RTS                         
C6D7: 86 39           LDA     #$39                
C6D9: B7 01 67        STA     $0167               
C6DC: 17 E2 49        LBSR    $A928               ; {hard.CLRSCREEN}
C6DF: 86 0D           LDA     #$0D                
C6E1: B7 FF 22        STA     $FF22               ; {hard.PIA1_DB}
C6E4: BD C6 C1        JSR     $C6C1               ; {}
C6E7: 0D 0D           TST     $0D                 
C6E9: 0D 20           TST     $20                 
C6EB: 20 20           BRA     $C70D               ; {}
C6ED: 20 20           BRA     $C70F               ; {}
C6EF: 20 20           BRA     $C711               ; {}
C6F1: 20 20           BRA     $C713               ; {}
C6F3: 20 20           BRA     $C715               ; {}
C6F5: 20 50           BRA     $C747               ; {}
C6F7: 4F              CLRA                        
C6F8: 50              NEGB                        
C6F9: 43              COMA                        
C6FA: 4F              CLRA                        
C6FB: 52 ; ????
C6FC: 4E ; ????
C6FD: 0D 0D           TST     $0D                 
C6FF: 20 20           BRA     $C721               ; {}
C701: 20 20           BRA     $C723               ; {}
C703: 20 20           BRA     $C725               ; {}
C705: 20 20           BRA     $C727               ; {}
C707: 20 20           BRA     $C729               ; {}
C709: 20 20           BRA     $C72B               ; {}
C70B: 20 20           BRA     $C72D               ; {}
C70D: 20 42           BRA     $C751               ; {}
C70F: 59              ROLB                        
C710: 0D 20           TST     $20                 
C712: 20 20           BRA     $C734               ; {}
C714: 20 20           BRA     $C736               ; {}
C716: 20 20           BRA     $C738               ; {}
C718: 20 20           BRA     $C73A               ; {}
C71A: 20 53           BRA     $C76F               ; {}
C71C: 54              LSRB                        
C71D: 45 ; ????
C71E: 56              RORB                        
C71F: 45 ; ????
C720: 20 42           BRA     $C764               ; {}
C722: 4A              DECA                        
C723: 4F              CLRA                        
C724: 52 ; ????
C725: 4B ; ????
C726: 0D 0D           TST     $0D                 
C728: 20 20           BRA     $C74A               ; {}
C72A: 20 20           BRA     $C74C               ; {}
C72C: 20 20           BRA     $C74E               ; {}
C72E: 43              COMA                        
C72F: 4F              CLRA                        
C730: 50              NEGB                        
C731: 59              ROLB                        
C732: 52 ; ????
C733: 49              ROLA                        
C734: 47              ASRA                        
C735: 48              ASLA                        
C736: 54              LSRB                        
C737: 20 28           BRA     $C761               ; {}
C739: 43              COMA                        
C73A: 29 20           BVS     $C75C               ; {}
C73C: 31 39           LEAY    -7,Y                
C73E: 38 ; ????
C73F: 31 0D           LEAY    13,X                
C741: 20 20           BRA     $C763               ; {}
C743: 20 20           BRA     $C765               ; {}
C745: 20 20           BRA     $C767               ; {}
C747: 20 20           BRA     $C769               ; {}
C749: 20 44           BRA     $C78F               ; {}
C74B: 41 ; ????
C74C: 54              LSRB                        
C74D: 41 ; ????
C74E: 53              COMB                        
C74F: 4F              CLRA                        
C750: 46              RORA                        
C751: 54              LSRB                        
C752: 20 49           BRA     $C79D               ; {}
C754: 4E ; ????
C755: 43              COMA                        
C756: 2E 0D           BGT     $C765               ; {}
C758: 0D 0D           TST     $0D                 
C75A: 20 20           BRA     $C77C               ; {}
C75C: 20 20           BRA     $C77E               ; {}
C75E: 20 4C           BRA     $C7AC               ; {}
C760: 49              ROLA                        
C761: 43              COMA                        
C762: 45 ; ????
C763: 4E ; ????
C764: 53              COMB                        
C765: 45 ; ????
C766: 44              LSRA                        
C767: 20 54           BRA     $C7BD               ; {}
C769: 4F              CLRA                        
C76A: 20 54           BRA     $C7C0               ; {}
C76C: 41 ; ????
C76D: 4E ; ????
C76E: 44              LSRA                        
C76F: 59              ROLB                        
C770: 20 43           BRA     $C7B5               ; {}
C772: 4F              CLRA                        
C773: 52 ; ????
C774: 50              NEGB                        
C775: 2E 00           BGT     $C777               ; {}
C777: CC 9F 10        LDD     #$9F10              
C77A: 8E 04 00        LDX     #$0400              
C77D: A7 80           STA     ,X+                 
C77F: A7 80           STA     ,X+                 
C781: BD C6 CE        JSR     $C6CE               ; {}
C784: 5A              DECB                        
C785: 26 F6           BNE     $C77D               ; {}
C787: C6 0E           LDB     #$0E                
C789: 30 88 1F        LEAX    $1F,X               
C78C: A7 00           STA     0,X                 
C78E: A7 1F           STA     -1,X                
C790: 30 88 20        LEAX    $20,X               
C793: BD C6 CE        JSR     $C6CE               ; {}
C796: 5A              DECB                        
C797: 26 F3           BNE     $C78C               ; {}
C799: C6 10           LDB     #$10                
C79B: A7 84           STA     ,X                  
C79D: A7 1F           STA     -1,X                
C79F: 30 1E           LEAX    -2,X                
C7A1: BD C6 CE        JSR     $C6CE               ; {}
C7A4: 5A              DECB                        
C7A5: 26 F4           BNE     $C79B               ; {}
C7A7: 30 88 E1        LEAX    $E1,X               
C7AA: C6 0E           LDB     #$0E                
C7AC: A7 84           STA     ,X                  
C7AE: A7 01           STA     1,X                 
C7B0: 30 88 E0        LEAX    $E0,X               
C7B3: BD C6 CE        JSR     $C6CE               ; {}
C7B6: 5A              DECB                        
C7B7: 26 F3           BNE     $C7AC               ; {}
C7B9: 5F              CLRB                        
C7BA: 86 09           LDA     #$09                
C7BC: 7D FF 03        TST     $FF03               ; {hard.PIA0_CB}
C7BF: 2A FB           BPL     $C7BC               ; {}
C7C1: 7D FF 02        TST     $FF02               ; {hard.PIA0_DB}
C7C4: 4A              DECA                        
C7C5: 26 F5           BNE     $C7BC               ; {}
C7C7: 8E 04 00        LDX     #$0400              
C7CA: A6 80           LDA     ,X+                 
C7CC: 2A 0A           BPL     $C7D8               ; {}
C7CE: 80 10           SUBA    #$10                
C7D0: 8A 8F           ORA     #$8F                
C7D2: 81 8F           CMPA    #$8F                
C7D4: 27 F8           BEQ     $C7CE               ; {}
C7D6: A7 1F           STA     -1,X                
C7D8: 8C 06 00        CMPX    #$0600              
C7DB: 26 ED           BNE     $C7CA               ; {}
C7DD: 17 D9 E1        LBSR    $A1C1               ; {hard.GETKEY}
C7E0: 84 7F           ANDA    #$7F                
C7E2: 26 03           BNE     $C7E7               ; {}
C7E4: 5A              DECB                        
C7E5: 26 D3           BNE     $C7BA               ; {}
C7E7: 39              RTS                         
C7E8: 20 20           BRA     $C80A               
C7EA: 48              ASLA                        
C7EB: 49              ROLA                        
C7EC: 20 46           BRA     $C834               
C7EE: 52 ; ????
C7EF: 4F              CLRA                        
C7F0: 4D              TSTA                        
C7F1: 20 53           BRA     $C846               
C7F3: 54              LSRB                        
C7F4: 45 ; ????
C7F5: 56              RORB                        
C7F6: 45 ; ????
C7F7: 20 20           BRA     $C819               
C7F9: 20 00           BRA     $C7FB               ; {}
C7FB: 00 00           NEG     $00                 
C7FD: 00 00           NEG     $00                 
C7FF: 00 
```

