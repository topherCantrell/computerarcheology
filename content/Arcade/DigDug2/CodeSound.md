[Dig Dug 2 Sound Board](digdug2.jpg)

# DigDug2 Sound Board

>>> cpu 6809

>>> binary E000:roms/d21_4.1k

>>> memoryTable hard 

[Hardware Info](HardwareSound.md)

>>> memoryTable ram 

[RAM Usage](RAMUseSound.md)

```code
E000: B7 20 00        STA     $2000               
E003: 8E 00 00        LDX     #$0000              
E006: CC 00 00        LDD     #$0000              
E009: ED 81           STD     ,X++                
E00B: 8C 04 00        CMPX    #$0400              
E00E: 26 F9           BNE     $E009               ; {}
E010: 10 CE 04 00     LDS     #$0400              
E014: 1C EF           ANDCC   #$EF                
E016: B7 20 07        STA     $2007               
E019: 96 B1           LDA     $B1                 
E01B: 10 26 01 B2     LBNE    $E1D1               ; {}
E01F: 96 B0           LDA     $B0                 
E021: 46              RORA                        
E022: 10 25 01 BB     LBCS    $E1E1               ; {}
E026: 0F A7           CLR     $A7                 
E028: 8E 00 40        LDX     #$0040              
E02B: A6 84           LDA     ,X                  
E02D: 27 07           BEQ     $E036               ; {}
E02F: 9F A7           STX     $A7                 
E031: BD E1 F1        JSR     $E1F1               ; {}
E034: 20 03           BRA     $E039               ; {}
E036: 6F 88 20        CLR     $20,X               
E039: 30 01           LEAX    1,X                 
E03B: A6 84           LDA     ,X                  
E03D: 27 07           BEQ     $E046               ; {}
E03F: 9F A7           STX     $A7                 
E041: BD E1 F1        JSR     $E1F1               ; {}
E044: 20 03           BRA     $E049               ; {}
E046: 6F 88 20        CLR     $20,X               
E049: 30 01           LEAX    1,X                 
E04B: A6 84           LDA     ,X                  
E04D: 27 07           BEQ     $E056               ; {}
E04F: 9F A7           STX     $A7                 
E051: BD E1 F1        JSR     $E1F1               ; {}
E054: 20 03           BRA     $E059               ; {}
E056: 6F 88 20        CLR     $20,X               
E059: 30 01           LEAX    1,X                 
E05B: A6 84           LDA     ,X                  
E05D: 27 07           BEQ     $E066               ; {}
E05F: 9F A7           STX     $A7                 
E061: BD E1 F1        JSR     $E1F1               ; {}
E064: 20 03           BRA     $E069               ; {}
E066: 6F 88 20        CLR     $20,X               
E069: 30 01           LEAX    1,X                 
E06B: A6 84           LDA     ,X                  
E06D: 27 07           BEQ     $E076               ; {}
E06F: 9F A7           STX     $A7                 
E071: BD E1 F1        JSR     $E1F1               ; {}
E074: 20 03           BRA     $E079               ; {}
E076: 6F 88 20        CLR     $20,X               
E079: 30 01           LEAX    1,X                 
E07B: A6 84           LDA     ,X                  
E07D: 26 07           BNE     $E086               ; {}
E07F: A6 88 20        LDA     $20,X               
E082: 26 10           BNE     $E094               ; {}
E084: 20 13           BRA     $E099               ; {}
E086: 9F A7           STX     $A7                 
E088: 6F 88 20        CLR     $20,X               
E08B: BD E1 F1        JSR     $E1F1               ; {}
E08E: 6F 9F 00 A7     CLR     [$00A7]             
E092: 20 05           BRA     $E099               ; {}
E094: 9F A7           STX     $A7                 
E096: BD E1 F1        JSR     $E1F1               ; {}
E099: 30 01           LEAX    1,X                 
E09B: A6 84           LDA     ,X                  
E09D: 27 07           BEQ     $E0A6               ; {}
E09F: 9F A7           STX     $A7                 
E0A1: BD E1 F1        JSR     $E1F1               ; {}
E0A4: 20 03           BRA     $E0A9               ; {}
E0A6: 6F 88 20        CLR     $20,X               
E0A9: 30 01           LEAX    1,X                 
E0AB: A6 84           LDA     ,X                  
E0AD: 27 07           BEQ     $E0B6               ; {}
E0AF: 9F A7           STX     $A7                 
E0B1: BD E1 F1        JSR     $E1F1               ; {}
E0B4: 20 03           BRA     $E0B9               ; {}
E0B6: 6F 88 20        CLR     $20,X               
E0B9: 30 01           LEAX    1,X                 
E0BB: A6 84           LDA     ,X                  
E0BD: 27 07           BEQ     $E0C6               ; {}
E0BF: 9F A7           STX     $A7                 
E0C1: BD E1 F1        JSR     $E1F1               ; {}
E0C4: 20 03           BRA     $E0C9               ; {}
E0C6: 6F 88 20        CLR     $20,X               
E0C9: 30 01           LEAX    1,X                 
E0CB: A6 84           LDA     ,X                  
E0CD: 26 07           BNE     $E0D6               ; {}
E0CF: A6 88 20        LDA     $20,X               
E0D2: 26 10           BNE     $E0E4               ; {}
E0D4: 20 13           BRA     $E0E9               ; {}
E0D6: 9F A7           STX     $A7                 
E0D8: 6F 88 20        CLR     $20,X               
E0DB: BD E1 F1        JSR     $E1F1               ; {}
E0DE: 6F 9F 00 A7     CLR     [$00A7]             
E0E2: 20 05           BRA     $E0E9               ; {}
E0E4: 9F A7           STX     $A7                 
E0E6: BD E1 F1        JSR     $E1F1               ; {}
E0E9: 30 01           LEAX    1,X                 
E0EB: A6 84           LDA     ,X                  
E0ED: 27 07           BEQ     $E0F6               ; {}
E0EF: 9F A7           STX     $A7                 
E0F1: BD E1 F1        JSR     $E1F1               ; {}
E0F4: 20 03           BRA     $E0F9               ; {}
E0F6: 6F 88 20        CLR     $20,X               
E0F9: 30 01           LEAX    1,X                 
E0FB: A6 84           LDA     ,X                  
E0FD: 27 07           BEQ     $E106               ; {}
E0FF: 9F A7           STX     $A7                 
E101: BD E1 F1        JSR     $E1F1               ; {}
E104: 20 03           BRA     $E109               ; {}
E106: 6F 88 20        CLR     $20,X               
E109: 30 01           LEAX    1,X                 
E10B: A6 84           LDA     ,X                  
E10D: 27 07           BEQ     $E116               ; {}
E10F: 9F A7           STX     $A7                 
E111: BD E1 F1        JSR     $E1F1               ; {}
E114: 20 03           BRA     $E119               ; {}
E116: 6F 88 20        CLR     $20,X               
E119: 30 01           LEAX    1,X                 
E11B: A6 84           LDA     ,X                  
E11D: 27 07           BEQ     $E126               ; {}
E11F: 9F A7           STX     $A7                 
E121: BD E1 F1        JSR     $E1F1               ; {}
E124: 20 03           BRA     $E129               ; {}
E126: 6F 88 20        CLR     $20,X               
E129: 30 01           LEAX    1,X                 
E12B: A6 84           LDA     ,X                  
E12D: 27 07           BEQ     $E136               ; {}
E12F: 9F A7           STX     $A7                 
E131: BD E1 F1        JSR     $E1F1               ; {}
E134: 20 03           BRA     $E139               ; {}
E136: 6F 88 20        CLR     $20,X               
E139: 30 01           LEAX    1,X                 
E13B: A6 84           LDA     ,X                  
E13D: 26 07           BNE     $E146               ; {}
E13F: A6 88 20        LDA     $20,X               
E142: 26 10           BNE     $E154               ; {}
E144: 20 13           BRA     $E159               ; {}
E146: 9F A7           STX     $A7                 
E148: 6F 88 20        CLR     $20,X               
E14B: BD E1 F1        JSR     $E1F1               ; {}
E14E: 6F 9F 00 A7     CLR     [$00A7]             
E152: 20 05           BRA     $E159               ; {}
E154: 9F A7           STX     $A7                 
E156: BD E1 F1        JSR     $E1F1               ; {}
E159: 30 01           LEAX    1,X                 
E15B: A6 84           LDA     ,X                  
E15D: 26 07           BNE     $E166               ; {}
E15F: A6 88 20        LDA     $20,X               
E162: 26 10           BNE     $E174               ; {}
E164: 20 13           BRA     $E179               ; {}
E166: 9F A7           STX     $A7                 
E168: 6F 88 20        CLR     $20,X               
E16B: BD E1 F1        JSR     $E1F1               ; {}
E16E: 6F 9F 00 A7     CLR     [$00A7]             
E172: 20 05           BRA     $E179               ; {}
E174: 9F A7           STX     $A7                 
E176: BD E1 F1        JSR     $E1F1               ; {}
E179: 30 01           LEAX    1,X                 
E17B: A6 84           LDA     ,X                  
E17D: 27 07           BEQ     $E186               ; {}
E17F: 9F A7           STX     $A7                 
E181: BD E1 F1        JSR     $E1F1               ; {}
E184: 20 03           BRA     $E189               ; {}
E186: 6F 88 20        CLR     $20,X               
E189: 30 01           LEAX    1,X                 
E18B: A6 84           LDA     ,X                  
E18D: 27 07           BEQ     $E196               ; {}
E18F: 9F A7           STX     $A7                 
E191: BD E1 F1        JSR     $E1F1               ; {}
E194: 20 03           BRA     $E199               ; {}
E196: 6F 88 20        CLR     $20,X               
E199: 30 01           LEAX    1,X                 
E19B: A6 84           LDA     ,X                  
E19D: 27 07           BEQ     $E1A6               ; {}
E19F: 9F A7           STX     $A7                 
E1A1: BD E1 F1        JSR     $E1F1               ; {}
E1A4: 20 03           BRA     $E1A9               ; {}
E1A6: 6F 88 20        CLR     $20,X               
E1A9: 30 01           LEAX    1,X                 
E1AB: A6 84           LDA     ,X                  
E1AD: 27 07           BEQ     $E1B6               ; {}
E1AF: 9F A7           STX     $A7                 
E1B1: BD E1 F1        JSR     $E1F1               ; {}
E1B4: 20 03           BRA     $E1B9               ; {}
E1B6: 6F 88 20        CLR     $20,X               
E1B9: 30 01           LEAX    1,X                 
E1BB: A6 84           LDA     ,X                  
E1BD: 27 07           BEQ     $E1C6               ; {}
E1BF: 9F A7           STX     $A7                 
E1C1: BD E1 F1        JSR     $E1F1               ; {}
E1C4: 20 03           BRA     $E1C9               ; {}
E1C6: 6F 88 20        CLR     $20,X               
E1C9: 30 01           LEAX    1,X                 
E1CB: B7 20 01        STA     $2001               
E1CE: 7E E3 81        JMP     $E381               ; {}
E1D1: CC 00 00        LDD     #$0000              
E1D4: 8E 00 80        LDX     #$0080              
E1D7: ED 81           STD     ,X++                
E1D9: 8C 00 A0        CMPX    #$00A0              
E1DC: 26 F9           BNE     $E1D7               ; {}
E1DE: 7E E3 81        JMP     $E381               ; {}
E1E1: 8E E0 00        LDX     #$E000              
E1E4: 4F              CLRA                        
E1E5: AB 80           ADDA    ,X+                 
E1E7: 8C FF FF        CMPX    #$FFFF              
E1EA: 26 F9           BNE     $E1E5               ; {}
E1EC: 97 B0           STA     $B0                 
E1EE: 7E E0 19        JMP     $E019               ; {}
E1F1: CE E4 AF        LDU     #$E4AF              
E1F4: DC A7           LDD     $A7                 
E1F6: C0 40           SUBB    #$40                
E1F8: 58              LSLB                        
E1F9: 33 D5           LEAU    [B,U]               
E1FB: DF A9           STU     $A9                 
E1FD: DF A3           STU     $A3                 
E1FF: 8E E4 6D        LDX     #$E46D              
E202: 30 85           LEAX    B,X                 
E204: EC 84           LDD     ,X                  
E206: DD AD           STD     $AD                 
E208: 9E AD           LDX     $AD                 
E20A: EC 84           LDD     ,X                  
E20C: 81 E0           CMPA    #$E0                
E20E: 10 27 00 C6     LBEQ    $E2D8               ; {}
E212: 96 AF           LDA     $AF                 
E214: 10 26 01 D6     LBNE    $E3EE               ; {}
E218: 9E A7           LDX     $A7                 
E21A: A6 88 20        LDA     $20,X               
E21D: 26 14           BNE     $E233               ; {}
E21F: 9E AD           LDX     $AD                 
E221: EC 81           LDD     ,X++                
E223: ED 9F 00 A3     STD     [$00A3]             
E227: A6 84           LDA     ,X                  
E229: DE A3           LDU     $A3                 
E22B: A7 4C           STA     12,U                
E22D: 6F 47           CLR     7,U                 
E22F: 6F 4D           CLR     13,U                
E231: 6F 4E           CLR     14,U                
E233: 10 AE 9F 00 A3  LDY     [$00A3]             
E238: A6 A4           LDA     ,Y                  
E23A: 81 F0           CMPA    #$F0                
E23C: 10 24 01 4A     LBHS    $E38A               ; {}
E240: 84 F0           ANDA    #$F0                
E242: 44              LSRA                        
E243: 44              LSRA                        
E244: 44              LSRA                        
E245: 44              LSRA                        
E246: 97 A0           STA     $A0                 
E248: 48              ASLA                        
E249: 9B A0           ADDA    $A0                 
E24B: DE A3           LDU     $A3                 
E24D: E6 4C           LDB     12,U                
E24F: C4 0F           ANDB    #$0F                
E251: 58              LSLB                        
E252: 8E E5 81        LDX     #$E581              
E255: 30 95           LEAX    [B,X]               
E257: 30 86           LEAX    A,X                 
E259: 33 42           LEAU    2,U                 
E25B: EC 81           LDD     ,X++                
E25D: ED C1           STD     ,U++                
E25F: A6 84           LDA     ,X                  
E261: A7 C4           STA     ,U                  
E263: 9E A3           LDX     $A3                 
E265: 30 02           LEAX    2,X                 
E267: A6 A0           LDA     ,Y+                 
E269: 84 0F           ANDA    #$0F                
E26B: 27 0C           BEQ     $E279               ; {}
E26D: 97 A0           STA     $A0                 
E26F: 64 84           LSR     ,X                  
E271: 66 01           ROR     1,X                 
E273: 66 02           ROR     2,X                 
E275: 0A A0           DEC     $A0                 
E277: 26 F6           BNE     $E26F               ; {}
E279: DE A3           LDU     $A3                 
E27B: E6 46           LDB     6,U                 
E27D: EA 80           ORB     ,X+                 
E27F: 33 42           LEAU    2,U                 
E281: E7 C0           STB     ,U+                 
E283: DE A3           LDU     $A3                 
E285: A6 47           LDA     7,U                 
E287: 26 28           BNE     $E2B1               ; {}
E289: A6 48           LDA     8,U                 
E28B: E6 A4           LDB     ,Y                  
E28D: 3D              MUL                         
E28E: E7 47           STB     7,U                 
E290: DE A3           LDU     $A3                 
E292: A6 4C           LDA     12,U                
E294: 84 F0           ANDA    #$F0                
E296: 26 19           BNE     $E2B1               ; {}
E298: E6 A2           LDB     ,-Y                 
E29A: C4 F0           ANDB    #$F0                
E29C: C1 C0           CMPB    #$C0                
E29E: 27 0C           BEQ     $E2AC               ; {}
E2A0: 8E E4 DB        LDX     #$E4DB              
E2A3: A6 49           LDA     9,U                 
E2A5: 48              ASLA                        
E2A6: 30 96           LEAX    [A,X]               
E2A8: AF 4A           STX     10,U                
E2AA: 20 0F           BRA     $E2BB               ; {}
E2AC: 4F              CLRA                        
E2AD: 31 21           LEAY    1,Y                 
E2AF: 20 10           BRA     $E2C1               ; {}
E2B1: E6 A2           LDB     ,-Y                 
E2B3: C4 F0           ANDB    #$F0                
E2B5: C1 C0           CMPB    #$C0                
E2B7: 27 F3           BEQ     $E2AC               ; {}
E2B9: AE 4A           LDX     10,U                
E2BB: A6 84           LDA     ,X                  
E2BD: 81 10           CMPA    #$10                
E2BF: 24 28           BHS     $E2E9               ; {}
E2C1: A7 45           STA     5,U                 
E2C3: 30 01           LEAX    1,X                 
E2C5: AF 4A           STX     10,U                
E2C7: 0C A2           INC     $A2                 
E2C9: DE A3           LDU     $A3                 
E2CB: 33 4F           LEAU    15,U                
E2CD: DF A3           STU     $A3                 
E2CF: 9E AD           LDX     $AD                 
E2D1: 30 03           LEAX    3,X                 
E2D3: 9F AD           STX     $AD                 
E2D5: 7E E2 0A        JMP     $E20A               ; {}
E2D8: D6 AF           LDB     $AF                 
E2DA: 26 08           BNE     $E2E4               ; {}
E2DC: 9E A7           LDX     $A7                 
E2DE: A7 88 20        STA     $20,X               
E2E1: 7E E3 32        JMP     $E332               ; {}
E2E4: 0F AF           CLR     $AF                 
E2E6: 7E E3 32        JMP     $E332               ; {}
E2E9: 84 0F           ANDA    #$0F                
E2EB: 48              ASLA                        
E2EC: 8E E2 F1        LDX     #$E2F1              
E2EF: 6E 96           JMP     [A,X]               
E2F1: E2 FB           SBCB    [D,S]               
E2F3: E3 01           ADDD    1,X                 
E2F5: E3 0C           ADDD    12,X                
E2F7: E3 18           ADDD    -8,X                
E2F9: E3 1B           ADDD    -5,X                
E2FB: AE 4A           LDX     10,U                
E2FD: A6 82           LDA     ,-X                 
E2FF: 20 C0           BRA     $E2C1               ; {}
E301: A6 45           LDA     5,U                 
E303: 4A              DECA                        
E304: AE 4A           LDX     10,U                
E306: A1 01           CMPA    1,X                 
E308: 27 B7           BEQ     $E2C1               ; {}
E30A: 20 22           BRA     $E32E               ; {}
E30C: E6 47           LDB     7,U                 
E30E: A6 45           LDA     5,U                 
E310: 97 A0           STA     $A0                 
E312: D1 A0           CMPB    $A0                 
E314: 23 13           BLS     $E329               ; {}
E316: 20 E3           BRA     $E2FB               ; {}
E318: 7E E2 90        JMP     $E290               ; {}
E31B: 86 10           LDA     #$10                
E31D: AA 4C           ORA     12,U                
E31F: A7 4C           STA     12,U                
E321: AE 4A           LDX     10,U                
E323: 30 01           LEAX    1,X                 
E325: AF 4A           STX     10,U                
E327: 20 92           BRA     $E2BB               ; {}
E329: A6 47           LDA     7,U                 
E32B: 4A              DECA                        
E32C: 20 00           BRA     $E32E               ; {}
E32E: A7 45           STA     5,U                 
E330: 20 95           BRA     $E2C7               ; {}
E332: 0C A2           INC     $A2                 
E334: 9E A9           LDX     $A9                 
E336: 9F A3           STX     $A3                 
E338: DC A7           LDD     $A7                 
E33A: C0 40           SUBB    #$40                
E33C: 8E E4 99        LDX     #$E499              
E33F: 30 85           LEAX    B,X                 
E341: A6 84           LDA     ,X                  
E343: C6 04           LDB     #$04                
E345: 3D              MUL                         
E346: C3 00 80        ADDD    #$0080              
E349: DD AB           STD     $AB                 
E34B: 0A A2           DEC     $A2                 
E34D: 27 2F           BEQ     $E37E               ; {}
E34F: C6 04           LDB     #$04                
E351: DE A3           LDU     $A3                 
E353: 33 42           LEAU    2,U                 
E355: 9E AB           LDX     $AB                 
E357: A6 C0           LDA     ,U+                 
E359: A7 80           STA     ,X+                 
E35B: 5A              DECB                        
E35C: 26 F9           BNE     $E357               ; {}
E35E: 9E A3           LDX     $A3                 
E360: 6A 07           DEC     7,X                 
E362: 27 0E           BEQ     $E372               ; {}
E364: 9E AB           LDX     $AB                 
E366: 30 04           LEAX    4,X                 
E368: 9F AB           STX     $AB                 
E36A: 9E A3           LDX     $A3                 
E36C: 30 0F           LEAX    15,X                
E36E: 9F A3           STX     $A3                 
E370: 20 D9           BRA     $E34B               ; {}
E372: EE 9F 00 A3     LDU     [$00A3]             
E376: 33 42           LEAU    2,U                 
E378: 9E A3           LDX     $A3                 
E37A: EF 84           STU     ,X                  
E37C: 20 E6           BRA     $E364               ; {}
E37E: 9E A7           LDX     $A7                 
E380: 39              RTS                         
E381: 96 A1           LDA     $A1                 
E383: 27 FC           BEQ     $E381               ; {}
E385: 0F A1           CLR     $A1                 
E387: 7E E0 19        JMP     $E019               ; {}
E38A: 8E E3 94        LDX     #$E394              
E38D: 84 0F           ANDA    #$0F                
E38F: 48              ASLA                        
E390: 31 21           LEAY    1,Y                 
E392: 6E 96           JMP     [A,X]               
E394: E3 A4           ADDD    ,Y                  
E396: E3 AC E3        ADDD    $E37C,PC            ; {}
E399: B4 E3 D7        ANDA    $E3D7               ; {}
E39C: E4 02           ANDB    2,X                 
E39E: E4 10           ANDB    -16,X               
E3A0: E4 20           ANDB    0,Y                 
E3A2: E3 BC A6        ADDD    [$E34B,PC]          ; {}
E3A5: A0 ; ????
E3A6: 9E A3           LDX     $A3                 
E3A8: A7 06           STA     6,X                 
E3AA: 20 1E           BRA     $E3CA               ; {}
E3AC: A6 A0           LDA     ,Y+                 
E3AE: 9E A3           LDX     $A3                 
E3B0: A7 09           STA     9,X                 
E3B2: 20 16           BRA     $E3CA               ; {}
E3B4: A6 A0           LDA     ,Y+                 
E3B6: DE A3           LDU     $A3                 
E3B8: A7 48           STA     8,U                 
E3BA: 20 0E           BRA     $E3CA               ; {}
E3BC: 86 0F           LDA     #$0F                
E3BE: A4 4C           ANDA    12,U                
E3C0: A7 4C           STA     12,U                
E3C2: EE 9F 00 A3     LDU     [$00A3]             
E3C6: 33 41           LEAU    1,U                 
E3C8: 20 06           BRA     $E3D0               ; {}
E3CA: EE 9F 00 A3     LDU     [$00A3]             
E3CE: 33 42           LEAU    2,U                 
E3D0: 9E A3           LDX     $A3                 
E3D2: EF 84           STU     ,X                  
E3D4: 7E E2 38        JMP     $E238               ; {}
E3D7: DC A7           LDD     $A7                 
E3D9: 10 83 00 54     CMPD    #$0054              
E3DD: 26 04           BNE     $E3E3               ; {}
E3DF: 0A 54           DEC     $54                 
E3E1: 20 04           BRA     $E3E7               ; {}
E3E3: 6F 9F 00 A7     CLR     [$00A7]             
E3E7: 9E A7           LDX     $A7                 
E3E9: 6F 88 20        CLR     $20,X               
E3EC: D7 AF           STB     $AF                 
E3EE: 9E A3           LDX     $A3                 
E3F0: 30 02           LEAX    2,X                 
E3F2: CC 00 00        LDD     #$0000              
E3F5: ED 81           STD     ,X++                
E3F7: ED 81           STD     ,X++                
E3F9: 30 06           LEAX    6,X                 
E3FB: ED 81           STD     ,X++                
E3FD: A7 84           STA     ,X                  
E3FF: 16 FE C5        LBRA    $E2C7               ; {}
E402: A6 A0           LDA     ,Y+                 
E404: 9E A3           LDX     $A3                 
E406: 30 0D           LEAX    13,X                
E408: 6C 84           INC     ,X                  
E40A: A1 84           CMPA    ,X                  
E40C: 27 1B           BEQ     $E429               ; {}
E40E: 20 10           BRA     $E420               ; {}
E410: A6 A0           LDA     ,Y+                 
E412: 9E A3           LDX     $A3                 
E414: 30 0E           LEAX    14,X                
E416: 6C 84           INC     ,X                  
E418: A1 84           CMPA    ,X                  
E41A: 26 0F           BNE     $E42B               ; {}
E41C: 6F 84           CLR     ,X                  
E41E: 20 00           BRA     $E420               ; {}
E420: EC A1           LDD     ,Y++                
E422: ED 9F 00 A3     STD     [$00A3]             
E426: 7E E2 33        JMP     $E233               ; {}
E429: 6F 84           CLR     ,X                  
E42B: EE 9F 00 A3     LDU     [$00A3]             
E42F: 33 44           LEAU    4,U                 
E431: 9E A3           LDX     $A3                 
E433: EF 84           STU     ,X                  
E435: 7E E2 33        JMP     $E233               ; {}
E438: B7 20 00        STA     $2000               
E43B: 8E 00 07        LDX     #$0007              
E43E: 9F A5           STX     $A5                 
E440: CE 00 80        LDU     #$0080              
E443: C6 04           LDB     #$04                
E445: A6 C0           LDA     ,U+                 
E447: A7 82           STA     ,-X                 
E449: 5A              DECB                        
E44A: 26 F9           BNE     $E445               ; {}
E44C: 9E A5           LDX     $A5                 
E44E: 30 08           LEAX    8,X                 
E450: 9F A5           STX     $A5                 
E452: 11 83 00 A0     CMPU    #$00A0              
E456: 24 02           BHS     $E45A               ; {}
E458: 20 E9           BRA     $E443               ; {}
E45A: CC 00 00        LDD     #$0000              
E45D: 8E 00 80        LDX     #$0080              
E460: ED 81           STD     ,X++                
E462: 8C 00 A0        CMPX    #$00A0              
E465: 25 F9           BCS     $E460               ; {}
E467: 0C A1           INC     $A1                 
E469: B7 20 01        STA     $2001               
E46C: 3B              RTI                         
E46D: F0 B3 E8        SUBB    $B3E8               
E470: 7B ; ????
E471: ED 6C           STD     12,S                
E473: EF BD F1 95     STU     [$D60C,PC]          
E477: EA ; ????
E478: EE EB           LDU     D,S                 
E47A: 8A F0           ORA     #$F0                
E47C: 6E F1           JMP     [,S++]              
E47E: 2E E9           BGT     $E469               ; {}
E480: E6 ; ????
E481: F2 33 E7        SBCB    $33E7               
E484: 5A              DECB                        
E485: EB 1A           ADDB    -6,X                
E487: ED 17           STD     -9,X                
E489: EC 39           LDD     -7,Y                
E48B: EF 3C           STU     -4,Y                
E48D: EC 12           LDD     -14,X               
E48F: EC 62           LDD     2,S                 
E491: E6 45           LDB     5,U                 
E493: EB ; ????
E494: CF ; ????
E495: EB 69           ADDB    9,S                 
E497: E5 FC 00        BITB    [$E49A,PC]          ; {}
E49A: 00 00           NEG     $00                 
E49C: 04 00           LSR     $00                 
E49E: 03 03           COM     $03                 
E4A0: 02 ; ????
E4A1: 04 00           LSR     $00                 
E4A3: 00 00           NEG     $00                 
E4A5: 03 00           COM     $00                 
E4A7: 06 02           ROR     $02                 
E4A9: 03 00           COM     $00                 
E4AB: 00 04           NEG     $04                 
E4AD: 00 04           NEG     $04                 
E4AF: 02 ; ????
E4B0: 3B              RTI                         
E4B1: 01 ; ????
E4B2: 00 01           NEG     $01                 
E4B4: C3 03 49        ADDD    #$0349              
E4B7: 01 ; ????
E4B8: 4B ; ????
E4B9: 03 85           COM     $85                 
E4BB: 02 ; ????
E4BC: B3 02 B3        SUBD    $02B3               
E4BF: 03 85           COM     $85                 
E4C1: 03 85           COM     $85                 
E4C3: 02 ; ????
E4C4: B3 02 B3        SUBD    $02B3               
E4C7: 03 C1           COM     $C1                 
E4C9: 01 ; ????
E4CA: 4B ; ????
E4CB: 03 0D           COM     $0D                 
E4CD: 03 2B           COM     $2B                 
E4CF: 03 85           COM     $85                 
E4D1: 02 ; ????
E4D2: 3B              RTI                         
E4D3: 01 ; ????
E4D4: 4B ; ????
E4D5: 01 ; ????
E4D6: FF 01 FF        STU     $01FF               
E4D9: 01 ; ????
E4DA: FF E5 05        STU     $E505               ; {}
E4DD: E5 07           BITB    7,X                 
E4DF: E5 09           BITB    9,X                 
E4E1: E5 0B           BITB    11,X                
E4E3: E5 0D           BITB    13,X                
E4E5: E5 0F           BITB    15,X                
E4E7: E5 11           BITB    -15,X               
E4E9: E5 13           BITB    -13,X               
E4EB: E5 19           BITB    -7,X                
E4ED: E5 1B           BITB    -5,X                
E4EF: E5 1F           BITB    -1,X                
E4F1: E5 27           BITB    7,Y                 
E4F3: E5 3B           BITB    -5,Y                
E4F5: E5 3D           BITB    -3,Y                
E4F7: E5 46           BITB    6,U                 
E4F9: E5 52           BITB    -14,U               
E4FB: E5 58           BITB    -8,U                
E4FD: E5 63           BITB    3,S                 
E4FF: E5 67           BITB    7,S                 
E501: E5 72           BITB    -14,S               
E503: E5 74           BITB    -12,S               
E505: 0F 10           CLR     $10                 
E507: 0C 10           INC     $10                 
E509: 0A 10           DEC     $10                 
E50B: 07 10           ASR     $10                 
E50D: 05 ; ????
E50E: 10 ; ????
E50F: 03 10           COM     $10                 
E511: 02 ; ????
E512: 10 ; ????
E513: 0A 11           DEC     $11                 
E515: 04 02           LSR     $02                 
E517: 00 10           NEG     $10                 
E519: 0F 12           CLR     $12                 
E51B: 0F 11           CLR     $11                 
E51D: 00 10           NEG     $10                 
E51F: 0F 0C           CLR     $0C                 
E521: 0A 07           DEC     $07                 
E523: 05 ; ????
E524: 03 00           COM     $00                 
E526: 10 ; ????
E527: 09 0A           ROL     $0A                 
E529: 0C 0E           INC     $0E                 
E52B: 0F 0F           CLR     $0F                 
E52D: 0F 0F           CLR     $0F                 
E52F: 0E 0E           JMP     $0E                 
E531: 0D 0D           TST     $0D                 
E533: 0C 0C           INC     $0C                 
E535: 0B ; ????
E536: 0B ; ????
E537: 0A 11           DEC     $11                 
E539: 00 10           NEG     $10                 
E53B: 0A 12           DEC     $12                 
E53D: 14 ; ????
E53E: 0F 0F           CLR     $0F                 
E540: 0E 0D           JMP     $0D                 
E542: 0B ; ????
E543: 0A 09           DEC     $09                 
E545: 10 ; ????
E546: 0F 11           CLR     $11                 
E548: 06 06           ROR     $06                 
E54A: 05 ; ????
E54B: 05 ; ????
E54C: 04 04           LSR     $04                 
E54E: 03 03           COM     $03                 
E550: 02 ; ????
E551: 10 ; ????
E552: 03 06           COM     $06                 
E554: 08 0A           LSL     $0A                 
E556: 0D 10           TST     $10                 
E558: 0D 0E           TST     $0E                 
E55A: 0F 0F           CLR     $0F                 
E55C: 0E 0E           JMP     $0E                 
E55E: 0D 0D           TST     $0D                 
E560: 11 ; ????
E561: 00 10           NEG     $10                 
E563: 0C 0D           INC     $0D                 
E565: 0E 12           JMP     $12                 
E567: 0B ; ????
E568: 0C 0D           INC     $0D                 
E56A: 0D 0C           TST     $0C                 
E56C: 0C 0B           INC     $0B                 
E56E: 0B ; ????
E56F: 11 ; ????
E570: 00 10           NEG     $10                 
E572: 08 12           LSL     $12                 
E574: 0E 0E           JMP     $0E                 
E576: 0E 0D           JMP     $0D                 
E578: 0D 0C           TST     $0C                 
E57A: 0A 08           DEC     $08                 
E57C: 06 04           ROR     $04                 
E57E: 02 ; ????
E57F: 00 10           NEG     $10                 
E581: E5 ; ????
E582: 87 ; ????
E583: E5 ; ????
E584: AE E5           LDX     B,S                 
E586: D5 02           BITB    $02                 
E588: 54              LSRB                        
E589: A8 02           EORA    2,X                 
E58B: 78 28 02        ASL     $2802               
E58E: 9D B4           JSR     $B4                 
E590: 02 ; ????
E591: C5 78           BITB    #$78                
E593: 02 ; ????
E594: EF CB           STU     D,U                 
E596: 03 1C           COM     $1C                 
E598: 82 03           SBCA    #$03                
E59A: 4B ; ????
E59B: C8 03           EORB    #$03                
E59D: 7D F6 03        TST     $F603               ; {}
E5A0: B3 35 03        SUBD    $3503               
E5A3: EB ; ????
E5A4: 87 ; ????
E5A5: 04 27           LSR     $27                 
E5A7: 17 04 66        LBSR    $EA10               ; {}
E5AA: 69 00           ROL     0,X                 
E5AC: 00 00           NEG     $00                 
E5AE: 02 ; ????
E5AF: 58              LSLB                        
E5B0: C0 02           SUBB    #$02                
E5B2: 7C 6C 02        INC     $6C02               
E5B5: A2 4F           SBCA    15,U                
E5B7: 02 ; ????
E5B8: CA 6B           ORB     #$6B                
E5BA: 02 ; ????
E5BB: F4 EA 03        ANDB    $EA03               ; {}
E5BE: 21 F8           BRN     $E5B8               ; {}
E5C0: 03 51           COM     $51                 
E5C2: 96 03           LDA     $03                 
E5C4: 84 1A           ANDA    #$1A                
E5C6: 03 B9           COM     $B9                 
E5C8: B1 03 F2        CMPA    $03F2               
E5CB: 5B ; ????
E5CC: 04 2E           LSR     $2E                 
E5CE: 6E 04           JMP     4,X                 
E5D0: 6E 17           JMP     -9,X                
E5D2: 00 00           NEG     $00                 
E5D4: 00 02           NEG     $02                 
E5D6: 5C              INCB                        
E5D7: D9 02           ADCB    $02                 
E5D9: 80 DC           SUBA    #$DC                
E5DB: 02 ; ????
E5DC: A6 EB           LDA     D,S                 
E5DE: 02 ; ????
E5DF: CF ; ????
E5E0: 5E ; ????
E5E1: 02 ; ????
E5E2: FA 08 03        ORB     $0803               
E5E5: 27 6E           BEQ     $E655               ; {}
E5E7: 03 57           COM     $57                 
E5E9: 63 03           COM     3,X                 
E5EB: 8A 3F           ORA     #$3F                
E5ED: 03 C0           COM     $C0                 
E5EF: 2E 03           BGT     $E5F4               ; {}
E5F1: F9 2E 04        ADCB    $2E04               
E5F4: 35 C5           PULS    CC,B,U,PC           
E5F6: 04 75           LSR     $75                 
E5F8: C5 00           BITB    #$00                
E5FA: 00 00           NEG     $00                 
E5FC: E6 09           LDB     9,X                 
E5FE: 00 E6           NEG     $E6                 
E600: 1E 00           EXG     D,D                 
E602: E6 2F           LDB     15,Y                
E604: 00 E6           NEG     $E6                 
E606: 40              NEGA                        
E607: 01 ; ????
E608: E0 ; ????
E609: F0 70 F1        SUBB    $70F1               
E60C: 14 ; ????
E60D: F2 05 A3        SBCB    $05A3               
E610: 01 ; ????
E611: 02 ; ????
E612: 01 ; ????
E613: A3 02           SUBD    2,X                 
E615: 73 02 33        COM     $0233               
E618: 02 ; ????
E619: F1 11 73        CMPB    $1173               
E61C: 08 F3           LSL     $F3                 
E61E: F0 60 F1        SUBB    $60F1               
E621: 14 ; ????
E622: F2 05 73        SBCB    $0573               
E625: 04 33           LSR     $33                 
E627: 02 ; ????
E628: A4 02           ANDA    2,X                 
E62A: F1 11 33        CMPB    $1133               
E62D: 08 F3           LSL     $F3                 
E62F: F0 60 F1        SUBB    $60F1               
E632: 14 ; ????
E633: F2 05 33        SBCB    $0533               
E636: 04 A4           LSR     $A4                 
E638: 02 ; ????
E639: 74 02 F1        LSR     $02F1               
E63C: 11 ; ????
E63D: A4 08           ANDA    8,X                 
E63F: F3 F0 30        ADDD    $F030               ; {}
E642: F6 E6 0B        LDB     $E60B               ; {}
E645: E6 58           LDB     -8,U                
E647: 00 E6           NEG     $E6                 
E649: 7F 00 E6        CLR     $00E6               
E64C: A6 00           LDA     0,X                 
E64E: E6 A6           LDB     A,Y                 
E650: 01 ; ????
E651: E6 B5           LDB     [B,Y]               
E653: 00 E6           NEG     $E6                 
E655: C4 00           ANDB    #$00                
E657: E0 ; ????
E658: F0 20 F1        SUBB    $20F1               
E65B: 0E F2           JMP     $F2                 
E65D: 08 93           LSL     $93                 
E65F: 01 ; ????
E660: A3 01           SUBD    1,X                 
E662: A3 01           SUBD    1,X                 
E664: 94 01           ANDA    $01                 
E666: A4 01           ANDA    1,X                 
E668: A4 01           ANDA    1,X                 
E66A: 95 01           BITA    $01                 
E66C: A5 01           BITA    1,X                 
E66E: A5 01           BITA    1,X                 
E670: A4 01           ANDA    1,X                 
E672: 03 01           COM     $01                 
E674: 23 01           BLS     $E677               ; {}
E676: 33 03           LEAU    3,X                 
E678: A4 02           ANDA    2,X                 
E67A: 34 07           PSHS    B,A,CC              
E67C: C0 03           SUBB    #$03                
E67E: F3 F0 00        ADDD    $F000               ; {}
E681: F1 0F F2        CMPB    $0FF2               
E684: 08 94           LSL     $94                 
E686: 01 ; ????
E687: A4 01           ANDA    1,X                 
E689: A4 01           ANDA    1,X                 
E68B: 95 01           BITA    $01                 
E68D: A5 01           BITA    1,X                 
E68F: A5 01           BITA    1,X                 
E691: 96 01           LDA     $01                 
E693: A6 01           LDA     1,X                 
E695: A6 01           LDA     1,X                 
E697: A5 01           BITA    1,X                 
E699: 04 01           LSR     $01                 
E69B: 24 01           BHS     $E69E               ; {}
E69D: 34 03           PSHS    A,CC                
E69F: A5 02           BITA    2,X                 
E6A1: 35 07           PULS    CC,A,B              
E6A3: C0 03           SUBB    #$03                
E6A5: F3 F0 40        ADDD    $F040               ; {}
E6A8: F1 0F F2        CMPB    $0FF2               
E6AB: 08 C0           LSL     $C0                 
E6AD: 0F 84           CLR     $84                 
E6AF: 02 ; ????
E6B0: 74 07 C0        LSR     $07C0               
E6B3: 03 F3           COM     $F3                 
E6B5: F0 40 F1        SUBB    $40F1               
E6B8: 0F F2           CLR     $F2                 
E6BA: 08 C0           LSL     $C0                 
E6BC: 0F 24           CLR     $24                 
E6BE: 02 ; ????
E6BF: 34 07           PSHS    B,A,CC              
E6C1: C0 03           SUBB    #$03                
E6C3: F3 F0 40        ADDD    $F040               ; {}
E6C6: F1 0F F2        CMPB    $0FF2               
E6C9: 08 C0           LSL     $C0                 
E6CB: 0F A6           CLR     $A6                 
E6CD: 02 ; ????
E6CE: 36 07           PSHU    B,A,CC              
E6D0: C0 03           SUBB    #$03                
E6D2: F3 E6 DA        ADDD    $E6DA               ; {}
E6D5: 00 E7           NEG     $E7                 
E6D7: 1D              SEX                         
E6D8: 00 E0           NEG     $E0                 
E6DA: F0 30 F1        SUBB    $30F1               
E6DD: 18 ; ????
E6DE: F2 0A C0        SBCB    $0AC0               
E6E1: 01 ; ????
E6E2: A3 01           SUBD    1,X                 
E6E4: A3 03           SUBD    3,X                 
E6E6: A3 01           SUBD    1,X                 
E6E8: A3 01           SUBD    1,X                 
E6EA: A3 01           SUBD    1,X                 
E6EC: F4 03 E6        ANDB    $03E6               
E6EF: E0 83           SUBB    ,--X                
E6F1: 01 ; ????
E6F2: 83 01 83        SUBD    #$0183              
E6F5: 01 ; ????
E6F6: 83 02 83        SUBD    #$0283              
E6F9: 01 ; ????
E6FA: 83 01 83        SUBD    #$0183              
E6FD: 01 ; ????
E6FE: C0 01           SUBB    #$01                
E700: 73 01 73        COM     $0173               
E703: 03 73           COM     $73                 
E705: 01 ; ????
E706: 73 01 73        COM     $0173               
E709: 01 ; ????
E70A: F4 03 E6        ANDB    $03E6               
E70D: FE 53 01        LDU     $5301               
E710: 53              COMB                        
E711: 01 ; ????
E712: 53              COMB                        
E713: 01 ; ????
E714: 73 02 A3        COM     $02A3               
E717: 01 ; ????
E718: A4 01           ANDA    1,X                 
E71A: A4 01           ANDA    1,X                 
E71C: F3 F0 40        ADDD    $F040               ; {}
E71F: F1 18 F2        CMPB    $18F2               
E722: 0A 35           DEC     $35                 
E724: 02 ; ????
E725: A6 01           LDA     1,X                 
E727: A6 01           LDA     1,X                 
E729: 35 01           PULS    CC                  
E72B: A6 02           LDA     2,X                 
E72D: 35 01           PULS    CC                  
E72F: 25 02           BCS     $E733               ; {}
E731: A6 01           LDA     1,X                 
E733: A6 01           LDA     1,X                 
E735: 25 01           BCS     $E738               ; {}
E737: A6 02           LDA     2,X                 
E739: 25 01           BCS     $E73C               ; {}
E73B: 15 ; ????
E73C: 02 ; ????
E73D: A6 01           LDA     1,X                 
E73F: A6 01           LDA     1,X                 
E741: 15 ; ????
E742: 01 ; ????
E743: A6 02           LDA     2,X                 
E745: 15 ; ????
E746: 01 ; ????
E747: B6 01 B6        LDA     $01B6               
E74A: 01 ; ????
E74B: B6 01 B6        LDA     $01B6               
E74E: 02 ; ????
E74F: A6 01           LDA     1,X                 
E751: 05 ; ????
E752: 01 ; ????
E753: 25 01           BCS     $E756               ; {}
E755: F4 02 E7        ANDB    $02E7               
E758: 23 F3           BLS     $E74D               ; {}
E75A: E7 6D           STB     13,S                
E75C: 00 E7           NEG     $E7                 
E75E: 8A 00           ORA     #$00                
E760: E7 ; ????
E761: A7 00           STA     0,X                 
E763: E7 C0           STB     ,U+                 
E765: 00 E7           NEG     $E7                 
E767: DD 00           STD     $00                 
E769: E7 ; ????
E76A: FA 01 E0        ORB     $01E0               
E76D: F0 20 F1        SUBB    $20F1               
E770: 09 F2           ROL     $F2                 
E772: 07 A4           ASR     $A4                 
E774: 01 ; ????
E775: B4 01 03        ANDA    $0103               
E778: 01 ; ????
E779: B4 01 03        ANDA    $0103               
E77C: 01 ; ????
E77D: 23 01           BLS     $E780               ; {}
E77F: 33 02           LEAU    2,X                 
E781: F0 70 F1        SUBB    $70F1               
E784: 11 ; ????
E785: 53              COMB                        
E786: 06 C0           ROR     $C0                 
E788: 06 F3           ROR     $F3                 
E78A: F0 00 F1        SUBB    $00F1               
E78D: 09 F2           ROL     $F2                 
E78F: 07 A4           ASR     $A4                 
E791: 01 ; ????
E792: B4 01 03        ANDA    $0103               
E795: 01 ; ????
E796: B4 01 03        ANDA    $0103               
E799: 01 ; ????
E79A: 23 01           BLS     $E79D               ; {}
E79C: 33 02           LEAU    2,X                 
E79E: F1 11 F0        CMPB    $11F0               
E7A1: 70 03 06        NEG     $0306               
E7A4: C0 06           SUBB    #$06                
E7A6: F3 F0 40        ADDD    $F040               ; {}
E7A9: F1 10 F2        CMPB    $10F2               
E7AC: 07 A5           ASR     $A5                 
E7AE: 03 F1           COM     $F1                 
E7B0: 09 A6           ROL     $A6                 
E7B2: 01 ; ????
E7B3: A6 01           LDA     1,X                 
E7B5: A6 01           LDA     1,X                 
E7B7: 35 02           PULS    A                   
E7B9: F1 11 35        CMPB    $1135               
E7BC: 06 C0           ROR     $C0                 
E7BE: 06 F3           ROR     $F3                 
E7C0: F0 20 F1        SUBB    $20F1               
E7C3: 09 F2           ROL     $F2                 
E7C5: 07 A4           ASR     $A4                 
E7C7: 01 ; ????
E7C8: 94 01           ANDA    $01                 
E7CA: 84 01           ANDA    #$01                
E7CC: 74 01 64        LSR     $0164               
E7CF: 01 ; ????
E7D0: 54              LSRB                        
E7D1: 01 ; ????
E7D2: 34 02           PSHS    A                   
E7D4: F1 11 F0        CMPB    $11F0               
E7D7: 70 A4 06        NEG     $A406               
E7DA: C0 06           SUBB    #$06                
E7DC: F3 F0 00        ADDD    $F000               ; {}
E7DF: F1 09 F2        CMPB    $09F2               
E7E2: 06 A4           ROR     $A4                 
E7E4: 01 ; ????
E7E5: 94 01           ANDA    $01                 
E7E7: 84 01           ANDA    #$01                
E7E9: 74 01 64        LSR     $0164               
E7EC: 01 ; ????
E7ED: 54              LSRB                        
E7EE: 01 ; ????
E7EF: 34 02           PSHS    A                   
E7F1: F1 11 F0        CMPB    $11F0               
E7F4: 70 74 06        NEG     $7406               
E7F7: C0 06           SUBB    #$06                
E7F9: F3 F0 60        ADDD    $F060               ; {}
E7FC: F6 E7 6F        LDB     $E76F               ; {}
E7FF: E8 12           EORB    -14,X               
E801: 00 E8           NEG     $E8                 
E803: 33 00           LEAU    0,X                 
E805: E8 54           EORB    -12,U               
E807: 00 E8           NEG     $E8                 
E809: 54              LSRB                        
E80A: 00 E8           NEG     $E8                 
E80C: 61 ; ????
E80D: 00 E8           NEG     $E8                 
E80F: 6E 00           JMP     0,X                 
E811: E0 ; ????
E812: F0 20 F1        SUBB    $20F1               
E815: 18 ; ????
E816: F2 08 A2        SBCB    $08A2               
E819: 03 A3           COM     $A3                 
E81B: 01 ; ????
E81C: A3 01           SUBD    1,X                 
E81E: A3 01           SUBD    1,X                 
E820: A3 01           SUBD    1,X                 
E822: A3 01           SUBD    1,X                 
E824: A3 01           SUBD    1,X                 
E826: A5 01           BITA    1,X                 
E828: 04 01           LSR     $01                 
E82A: 24 01           BHS     $E82D               ; {}
E82C: 34 03           PSHS    A,CC                
E82E: A5 02           BITA    2,X                 
E830: 35 07           PULS    CC,A,B              
E832: F3 F0 00        ADDD    $F000               ; {}
E835: F1 18 F2        CMPB    $18F2               
E838: 08 A3           LSL     $A3                 
E83A: 03 A4           COM     $A4                 
E83C: 01 ; ????
E83D: A4 01           ANDA    1,X                 
E83F: A4 01           ANDA    1,X                 
E841: A4 01           ANDA    1,X                 
E843: A4 01           ANDA    1,X                 
E845: A4 01           ANDA    1,X                 
E847: A6 01           LDA     1,X                 
E849: 05 ; ????
E84A: 01 ; ????
E84B: 25 01           BCS     $E84E               ; {}
E84D: 35 03           PULS    CC,A                
E84F: A6 02           LDA     2,X                 
E851: 36 07           PSHU    B,A,CC              
E853: F3 F0 40        ADDD    $F040               ; {}
E856: F1 19 F2        CMPB    $19F2               
E859: 08 C0           LSL     $C0                 
E85B: 0F 84           CLR     $84                 
E85D: 02 ; ????
E85E: 74 07 F3        LSR     $07F3               
E861: F0 40 F1        SUBB    $40F1               
E864: 19              DAA                         
E865: F2 08 C0        SBCB    $08C0               
E868: 0F 24           CLR     $24                 
E86A: 02 ; ????
E86B: 34 07           PSHS    B,A,CC              
E86D: F3 F0 40        ADDD    $F040               ; {}
E870: F1 19 F2        CMPB    $19F2               
E873: 08 C0           LSL     $C0                 
E875: 0F A6           CLR     $A6                 
E877: 02 ; ????
E878: 36 07           PSHU    B,A,CC              
E87A: F3 E8 88        ADDD    $E888               ; {}
E87D: 00 E9           NEG     $E9                 
E87F: B1 00 E8        CMPA    $00E8               
E882: EB 00           ADDB    0,X                 
E884: E9 4E           ADCB    14,U                
E886: 00 E0           NEG     $E0                 
E888: F0 30 F1        SUBB    $30F1               
E88B: 0E F2           JMP     $F2                 
E88D: 0A 93           DEC     $93                 
E88F: 01 ; ????
E890: A3 02           SUBD    2,X                 
E892: A3 02           SUBD    2,X                 
E894: A3 01           SUBD    1,X                 
E896: A3 01           SUBD    1,X                 
E898: 32 01           LEAS    1,X                 
E89A: 93 01           SUBD    $01                 
E89C: A3 02           SUBD    2,X                 
E89E: A3 02           SUBD    2,X                 
E8A0: A3 01           SUBD    1,X                 
E8A2: A3 01           SUBD    1,X                 
E8A4: 52 ; ????
E8A5: 01 ; ????
E8A6: 93 01           SUBD    $01                 
E8A8: A3 02           SUBD    2,X                 
E8AA: A3 02           SUBD    2,X                 
E8AC: A3 01           SUBD    1,X                 
E8AE: A3 01           SUBD    1,X                 
E8B0: A2 01           SBCA    1,X                 
E8B2: 82 02           SBCA    #$02                
E8B4: 82 02           SBCA    #$02                
E8B6: 72 ; ????
E8B7: 02 ; ????
E8B8: 52 ; ????
E8B9: 02 ; ????
E8BA: 63 01           COM     1,X                 
E8BC: 73 02 73        COM     $0273               
E8BF: 02 ; ????
E8C0: 73 01 73        COM     $0173               
E8C3: 01 ; ????
E8C4: 22 01           BHI     $E8C7               ; {}
E8C6: 63 01           COM     1,X                 
E8C8: 73 02 73        COM     $0273               
E8CB: 02 ; ????
E8CC: 73 01 73        COM     $0173               
E8CF: 01 ; ????
E8D0: 32 01           LEAS    1,X                 
E8D2: 63 01           COM     1,X                 
E8D4: 73 02 73        COM     $0273               
E8D7: 02 ; ????
E8D8: 73 01 73        COM     $0173               
E8DB: 01 ; ????
E8DC: 72 ; ????
E8DD: 01 ; ????
E8DE: 52 ; ????
E8DF: 01 ; ????
E8E0: 83 01 02        SUBD    #$0102              
E8E3: 01 ; ????
E8E4: 32 01           LEAS    1,X                 
E8E6: 72 ; ????
E8E7: 02 ; ????
E8E8: A2 02           SBCA    2,X                 
E8EA: F3 F0 30        ADDD    $F030               ; {}
E8ED: F1 0E F2        CMPB    $0EF2               
E8F0: 0A 63           DEC     $63                 
E8F2: 01 ; ????
E8F3: 73 02 73        COM     $0273               
E8F6: 02 ; ????
E8F7: 73 01 73        COM     $0173               
E8FA: 01 ; ????
E8FB: 32 01           LEAS    1,X                 
E8FD: 63 01           COM     1,X                 
E8FF: 73 02 73        COM     $0273               
E902: 02 ; ????
E903: 73 01 73        COM     $0173               
E906: 01 ; ????
E907: 52 ; ????
E908: 01 ; ????
E909: 63 01           COM     1,X                 
E90B: 73 02 73        COM     $0273               
E90E: 02 ; ????
E90F: 73 01 73        COM     $0173               
E912: 01 ; ????
E913: A2 01           SBCA    1,X                 
E915: 52 ; ????
E916: 02 ; ????
E917: 52 ; ????
E918: 02 ; ????
E919: 32 02           LEAS    2,X                 
E91B: 22 02           BHI     $E91F               ; {}
E91D: 23 01           BLS     $E920               ; {}
E91F: 33 02           LEAU    2,X                 
E921: 33 02           LEAU    2,X                 
E923: 33 01           LEAU    1,X                 
E925: 33 01           LEAU    1,X                 
E927: 22 01           BHI     $E92A               ; {}
E929: 23 01           BLS     $E92C               ; {}
E92B: 33 02           LEAU    2,X                 
E92D: 33 02           LEAU    2,X                 
E92F: 33 01           LEAU    1,X                 
E931: 33 01           LEAU    1,X                 
E933: 32 01           LEAS    1,X                 
E935: 23 01           BLS     $E938               ; {}
E937: 33 02           LEAU    2,X                 
E939: 33 02           LEAU    2,X                 
E93B: 33 01           LEAU    1,X                 
E93D: 33 01           LEAU    1,X                 
E93F: 72 ; ????
E940: 01 ; ????
E941: 32 01           LEAS    1,X                 
E943: 53              COMB                        
E944: 01 ; ????
E945: 83 01 02        SUBD    #$0102              
E948: 01 ; ????
E949: 32 02           LEAS    2,X                 
E94B: 72 ; ????
E94C: 02 ; ????
E94D: F3 F0 00        ADDD    $F000               ; {}
E950: F1 0F F2        CMPB    $0FF2               
E953: 0A 94           DEC     $94                 
E955: 01 ; ????
E956: A4 02           ANDA    2,X                 
E958: A4 02           ANDA    2,X                 
E95A: A4 01           ANDA    1,X                 
E95C: A4 01           ANDA    1,X                 
E95E: 33 01           LEAU    1,X                 
E960: 94 01           ANDA    $01                 
E962: A4 02           ANDA    2,X                 
E964: A4 02           ANDA    2,X                 
E966: A4 01           ANDA    1,X                 
E968: A4 01           ANDA    1,X                 
E96A: 53              COMB                        
E96B: 01 ; ????
E96C: 94 01           ANDA    $01                 
E96E: A4 02           ANDA    2,X                 
E970: A4 02           ANDA    2,X                 
E972: A4 01           ANDA    1,X                 
E974: A4 01           ANDA    1,X                 
E976: A3 01           SUBD    1,X                 
E978: 83 02 83        SUBD    #$0283              
E97B: 02 ; ????
E97C: 73 02 53        COM     $0253               
E97F: 02 ; ????
E980: 64 01           LSR     1,X                 
E982: 74 02 74        LSR     $0274               
E985: 02 ; ????
E986: 74 01 74        LSR     $0174               
E989: 01 ; ????
E98A: 23 01           BLS     $E98D               ; {}
E98C: 64 01           LSR     1,X                 
E98E: 74 02 74        LSR     $0274               
E991: 02 ; ????
E992: 74 01 74        LSR     $0174               
E995: 01 ; ????
E996: 33 01           LEAU    1,X                 
E998: 64 01           LSR     1,X                 
E99A: 74 02 74        LSR     $0274               
E99D: 02 ; ????
E99E: 74 01 74        LSR     $0174               
E9A1: 01 ; ????
E9A2: 73 01 53        COM     $0153               
E9A5: 01 ; ????
E9A6: 84 01           ANDA    #$01                
E9A8: 03 01           COM     $01                 
E9AA: 33 01           LEAU    1,X                 
E9AC: 73 02 A3        COM     $02A3               
E9AF: 02 ; ????
E9B0: F3 F0 40        ADDD    $F040               ; {}
E9B3: F1 0E F2        CMPB    $0EF2               
E9B6: 0A 35           DEC     $35                 
E9B8: 01 ; ????
E9B9: A6 01           LDA     1,X                 
E9BB: 35 01           PULS    CC                  
E9BD: A6 01           LDA     1,X                 
E9BF: 35 04           PULS    B                   
E9C1: 25 01           BCS     $E9C4               ; {}
E9C3: A6 01           LDA     1,X                 
E9C5: 25 01           BCS     $E9C8               ; {}
E9C7: A6 01           LDA     1,X                 
E9C9: 25 04           BCS     $E9CF               ; {}
E9CB: 15 ; ????
E9CC: 01 ; ????
E9CD: A6 01           LDA     1,X                 
E9CF: 15 ; ????
E9D0: 01 ; ????
E9D1: A6 01           LDA     1,X                 
E9D3: 15 ; ????
E9D4: 04 B6           LSR     $B6                 
E9D6: 01 ; ????
E9D7: B6 02 B6        LDA     $02B6               
E9DA: 02 ; ????
E9DB: A6 01           LDA     1,X                 
E9DD: 05 ; ????
E9DE: 01 ; ????
E9DF: 25 01           BCS     $E9E2               ; {}
E9E1: F4 02 E9        ANDB    $02E9               
E9E4: B7 F3 E9        STA     $F3E9               ; {}
E9E7: F9 00 EA        ADCB    $00EA               
E9EA: 1E 00           EXG     D,D                 
E9EC: EA 43           ORB     3,U                 
E9EE: 00 EA           NEG     $EA                 
E9F0: 43              COMA                        
E9F1: 00 EA           NEG     $EA                 
E9F3: 50              NEGB                        
E9F4: 00 EA           NEG     $EA                 
E9F6: 5D              TSTB                        
E9F7: 00 E0           NEG     $E0                 
E9F9: F0 20 F1        SUBB    $20F1               
E9FC: 0E F2           JMP     $F2                 
E9FE: 08 93           LSL     $93                 
EA00: 01 ; ????
EA01: A3 01           SUBD    1,X                 
EA03: A3 01           SUBD    1,X                 
EA05: 94 01           ANDA    $01                 
EA07: A4 01           ANDA    1,X                 
EA09: A4 01           ANDA    1,X                 
EA0B: 95 01           BITA    $01                 
EA0D: A5 01           BITA    1,X                 
EA0F: A5 01           BITA    1,X                 
EA11: 93 01           SUBD    $01                 
EA13: A3 01           SUBD    1,X                 
EA15: 02 ; ????
EA16: 01 ; ????
EA17: A3 03           SUBD    3,X                 
EA19: A4 02           ANDA    2,X                 
EA1B: 94 07           ANDA    $07                 
EA1D: F3 F0 00        ADDD    $F000               ; {}
EA20: F1 0F F2        CMPB    $0FF2               
EA23: 08 94           LSL     $94                 
EA25: 01 ; ????
EA26: A4 01           ANDA    1,X                 
EA28: A4 01           ANDA    1,X                 
EA2A: 95 01           BITA    $01                 
EA2C: A5 01           BITA    1,X                 
EA2E: A5 01           BITA    1,X                 
EA30: 96 01           LDA     $01                 
EA32: A6 01           LDA     1,X                 
EA34: A6 01           LDA     1,X                 
EA36: 94 01           ANDA    $01                 
EA38: A4 01           ANDA    1,X                 
EA3A: 03 01           COM     $01                 
EA3C: A4 03           ANDA    3,X                 
EA3E: A5 02           BITA    2,X                 
EA40: 95 07           BITA    $07                 
EA42: F3 F0 40        ADDD    $F040               ; {}
EA45: F1 0F F2        CMPB    $0FF2               
EA48: 08 C0           LSL     $C0                 
EA4A: 0F 74           CLR     $74                 
EA4C: 02 ; ????
EA4D: 64 07           LSR     7,X                 
EA4F: F3 F0 40        ADDD    $F040               ; {}
EA52: F1 0F F2        CMPB    $0FF2               
EA55: 08 C0           LSL     $C0                 
EA57: 0F 24           CLR     $24                 
EA59: 02 ; ????
EA5A: 24 07           BHS     $EA63               ; {}
EA5C: F3 F0 40        ADDD    $F040               ; {}
EA5F: F1 0F F2        CMPB    $0FF2               
EA62: 08 C0           LSL     $C0                 
EA64: 0F A5           CLR     $A5                 
EA66: 02 ; ????
EA67: A5 07           BITA    7,X                 
EA69: F3 EA 6E        ADDD    $EA6E               ; {}
EA6C: 00 E0           NEG     $E0                 
EA6E: F0 00 F1        SUBB    $00F1               
EA71: 07 F2           ASR     $F2                 
EA73: 01 ; ????
EA74: C0 02           SUBB    #$02                
EA76: F3 EA 81        ADDD    $EA81               ; {}
EA79: 00 EA           NEG     $EA                 
EA7B: 98 02           EORA    $02                 
EA7D: EA ; ????
EA7E: AF 01           STX     1,X                 
EA80: E0 ; ????
EA81: F0 60 F1        SUBB    $60F1               
EA84: 0C F2           INC     $F2                 
EA86: 01 ; ????
EA87: 85 01           BITA    #$01                
EA89: 74 01 85        LSR     $0185               
EA8C: 01 ; ????
EA8D: 74 01 85        LSR     $0185               
EA90: 01 ; ????
EA91: 74 01 65        LSR     $0165               
EA94: 01 ; ????
EA95: C0 02           SUBB    #$02                
EA97: F3 F0 20        ADDD    $F020               ; {}
EA9A: F1 0C F2        CMPB    $0CF2               
EA9D: 01 ; ????
EA9E: 93 01           SUBD    $01                 
EAA0: 84 01           ANDA    #$01                
EAA2: 93 01           SUBD    $01                 
EAA4: 84 01           ANDA    #$01                
EAA6: 93 01           SUBD    $01                 
EAA8: 84 01           ANDA    #$01                
EAAA: 73 01 C0        COM     $01C0               
EAAD: 02 ; ????
EAAE: F3 F0 60        ADDD    $F060               ; {}
EAB1: F1 0C F2        CMPB    $0CF2               
EAB4: 01 ; ????
EAB5: 84 01           ANDA    #$01                
EAB7: 73 01 84        COM     $0184               
EABA: 01 ; ????
EABB: 73 01 84        COM     $0184               
EABE: 01 ; ????
EABF: 73 01 64        COM     $0164               
EAC2: 01 ; ????
EAC3: C0 02           SUBB    #$02                
EAC5: F3 EA CD        ADDD    $EACD               ; {}
EAC8: 00 EA           NEG     $EA                 
EACA: CD ; ????
EACB: 02 ; ????
EACC: E0 ; ????
EACD: F0 00 F1        SUBB    $00F1               
EAD0: 00 F2           NEG     $F2                 
EAD2: 01 ; ????
EAD3: A4 01           ANDA    1,X                 
EAD5: 23 01           BLS     $EAD8               ; {}
EAD7: A4 01           ANDA    1,X                 
EAD9: 23 01           BLS     $EADC               ; {}
EADB: F1 02 A4        CMPB    $02A4               
EADE: 01 ; ????
EADF: 23 01           BLS     $EAE2               ; {}
EAE1: F1 03 A4        CMPB    $03A4               
EAE4: 01 ; ????
EAE5: 23 01           BLS     $EAE8               ; {}
EAE7: F1 04 A4        CMPB    $04A4               
EAEA: 01 ; ????
EAEB: 23 01           BLS     $EAEE               ; {}
EAED: F3 EA F5        ADDD    $EAF5               ; {}
EAF0: 00 EA           NEG     $EA                 
EAF2: F5 02 E0        BITB    $02E0               
EAF5: F0 00 F1        SUBB    $00F1               
EAF8: 01 ; ????
EAF9: F2 02 32        SBCB    $0232               
EAFC: 01 ; ????
EAFD: 52 ; ????
EAFE: 01 ; ????
EAFF: 72 ; ????
EB00: 01 ; ????
EB01: 92 01           SBCA    $01                 
EB03: C0 01           SUBB    #$01                
EB05: 62 ; ????
EB06: 01 ; ????
EB07: 82 01           SBCA    #$01                
EB09: A2 01           SBCA    1,X                 
EB0B: B1 01 C0        CMPA    $01C0               
EB0E: 01 ; ????
EB0F: 92 01           SBCA    $01                 
EB11: A2 01           SBCA    1,X                 
EB13: 01 ; ????
EB14: 01 ; ????
EB15: 21 01           BRN     $EB18               ; {}
EB17: C0 01           SUBB    #$01                
EB19: F3 EB 21        ADDD    $EB21               ; {}
EB1C: 01 ; ????
EB1D: EB 21           ADDB    1,Y                 
EB1F: 00 E0           NEG     $E0                 
EB21: F0 30 F1        SUBB    $30F1               
EB24: 0A F2           DEC     $F2                 
EB26: 04 22           LSR     $22                 
EB28: 01 ; ????
EB29: 32 01           LEAS    1,X                 
EB2B: 62 ; ????
EB2C: 01 ; ????
EB2D: 72 ; ????
EB2E: 01 ; ????
EB2F: 92 01           SBCA    $01                 
EB31: 01 ; ????
EB32: 01 ; ????
EB33: A2 01           SBCA    1,X                 
EB35: 72 ; ????
EB36: 01 ; ????
EB37: F3 EB 3C        ADDD    $EB3C               ; {}
EB3A: 00 E0           NEG     $E0                 
EB3C: F0 50 F1        SUBB    $50F1               
EB3F: 00 F2           NEG     $F2                 
EB41: 01 ; ????
EB42: 92 01           SBCA    $01                 
EB44: 21 01           BRN     $EB47               ; {}
EB46: A2 01           SBCA    1,X                 
EB48: 31 01           LEAY    1,X                 
EB4A: B2 01 41        SBCA    $0141               
EB4D: 01 ; ????
EB4E: 01 ; ????
EB4F: 01 ; ????
EB50: 51 ; ????
EB51: 01 ; ????
EB52: 11 ; ????
EB53: 01 ; ????
EB54: 61 ; ????
EB55: 01 ; ????
EB56: 21 01           BRN     $EB59               ; {}
EB58: 71 ; ????
EB59: 01 ; ????
EB5A: 31 01           LEAY    1,X                 
EB5C: 81 01           CMPA    #$01                
EB5E: 84 02           ANDA    #$02                
EB60: 74 02 64        LSR     $0264               
EB63: 02 ; ????
EB64: 54              LSRB                        
EB65: 02 ; ????
EB66: C0 02           SUBB    #$02                
EB68: F3 EB 73        ADDD    $EB73               ; {}
EB6B: 00 EB           NEG     $EB                 
EB6D: 73 01 EB        COM     $01EB               
EB70: 73 02 E0        COM     $02E0               
EB73: F0 30 F1        SUBB    $30F1               
EB76: 0A F2           DEC     $F2                 
EB78: 04 B4           LSR     $B4                 
EB7A: 01 ; ????
EB7B: 03 01           COM     $01                 
EB7D: 33 01           LEAU    1,X                 
EB7F: 73 01 A3        COM     $01A3               
EB82: 01 ; ????
EB83: 73 01 33        COM     $0133               
EB86: 01 ; ????
EB87: 03 01           COM     $01                 
EB89: F3 EB 97        ADDD    $EB97               ; {}
EB8C: 01 ; ????
EB8D: EB ; ????
EB8E: AE 02           LDX     2,X                 
EB90: EB C5           ADDB    B,U                 
EB92: 02 ; ????
EB93: EB ; ????
EB94: CA 00           ORB     #$00                
EB96: E0 ; ????
EB97: F0 30 F1        SUBB    $30F1               
EB9A: 00 F2           NEG     $F2                 
EB9C: 02 ; ????
EB9D: 13              SYNC                        
EB9E: 01 ; ????
EB9F: 53              COMB                        
EBA0: 01 ; ????
EBA1: 63 01           COM     1,X                 
EBA3: 83 01 13        SUBD    #$0113              
EBA6: 01 ; ????
EBA7: 53              COMB                        
EBA8: 01 ; ????
EBA9: 63 01           COM     1,X                 
EBAB: 82 01           SBCA    #$01                
EBAD: F3 F0 30        ADDD    $F030               ; {}
EBB0: F1 00 F2        CMPB    $00F2               
EBB3: 02 ; ????
EBB4: 14 ; ????
EBB5: 01 ; ????
EBB6: 54              LSRB                        
EBB7: 01 ; ????
EBB8: 64 01           LSR     1,X                 
EBBA: 84 01           ANDA    #$01                
EBBC: 14 ; ????
EBBD: 01 ; ????
EBBE: 54              LSRB                        
EBBF: 01 ; ????
EBC0: 64 01           LSR     1,X                 
EBC2: 83 01 F3        SUBD    #$01F3              
EBC5: F0 20 F6        SUBB    $20F6               
EBC8: EB ; ????
EBC9: 97 F0           STA     $F0                 
EBCB: 20 F6           BRA     $EBC3               ; {}
EBCD: EB ; ????
EBCE: AE EB           LDX     D,S                 
EBD0: DC 00           LDD     $00                 
EBD2: EB ; ????
EBD3: F7 00 EB        STB     $00EB               
EBD6: DC 01           LDD     $01                 
EBD8: EB ; ????
EBD9: F7 01 E0        STB     $01E0               
EBDC: F0 00 F1        SUBB    $00F1               
EBDF: 09 F2           ROL     $F2                 
EBE1: 07 33           ASR     $33                 
EBE3: 01 ; ????
EBE4: 53              COMB                        
EBE5: 01 ; ????
EBE6: 73 01 03        COM     $0103               
EBE9: 01 ; ????
EBEA: A4 01           ANDA    1,X                 
EBEC: C0 01           SUBB    #$01                
EBEE: 02 ; ????
EBEF: 01 ; ????
EBF0: C0 01           SUBB    #$01                
EBF2: F1 08 A3        CMPB    $08A3               
EBF5: 04 F3           LSR     $F3                 
EBF7: F0 00 F1        SUBB    $00F1               
EBFA: 09 F2           ROL     $F2                 
EBFC: 07 32           ASR     $32                 
EBFE: 01 ; ????
EBFF: 52 ; ????
EC00: 01 ; ????
EC01: 72 ; ????
EC02: 01 ; ????
EC03: 02 ; ????
EC04: 01 ; ????
EC05: A3 01           SUBD    1,X                 
EC07: C0 01           SUBB    #$01                
EC09: 01 ; ????
EC0A: 01 ; ????
EC0B: C0 01           SUBB    #$01                
EC0D: F1 08 A2        CMPB    $08A2               
EC10: 04 F3           LSR     $F3                 
EC12: EC 1C           LDD     -4,X                
EC14: 00 EC           NEG     $EC                 
EC16: 1C 02           ANDCC   #$02                
EC18: EC 1C           LDD     -4,X                
EC1A: 01 ; ????
EC1B: E0 ; ????
EC1C: F0 20 F1        SUBB    $20F1               
EC1F: 00 F2           NEG     $F2                 
EC21: 02 ; ????
EC22: 97 01           STA     $01                 
EC24: 46              RORA                        
EC25: 01 ; ????
EC26: B6 01 65        LDA     $0165               
EC29: 01 ; ????
EC2A: 14 ; ????
EC2B: 01 ; ????
EC2C: 84 01           ANDA    #$01                
EC2E: 33 01           LEAU    1,X                 
EC30: 23 01           BLS     $EC33               ; {}
EC32: 33 01           LEAU    1,X                 
EC34: 43              COMA                        
EC35: 01 ; ????
EC36: 33 01           LEAU    1,X                 
EC38: F3 EC 40        ADDD    $EC40               ; {}
EC3B: 00 EC           NEG     $EC                 
EC3D: 4F              CLRA                        
EC3E: 00 E0           NEG     $E0                 
EC40: F0 00 F1        SUBB    $00F1               
EC43: 02 ; ????
EC44: F2 01 22        SBCB    $0122               
EC47: 01 ; ????
EC48: 72 ; ????
EC49: 01 ; ????
EC4A: F4 0C EC        ANDB    $0CEC               
EC4D: 46              RORA                        
EC4E: F3 F0 10        ADDD    $F010               ; {}
EC51: F1 02 F2        CMPB    $02F2               
EC54: 01 ; ????
EC55: 96 04           LDA     $04                 
EC57: A6 04           LDA     4,X                 
EC59: B6 04 05        LDA     $0405               
EC5C: 04 15           LSR     $15                 
EC5E: 04 05           LSR     $05                 
EC60: 04 F3           LSR     $F3                 
EC62: EC 75           LDD     -11,S               
EC64: 00 EC           NEG     $EC                 
EC66: A6 00           LDA     0,X                 
EC68: EC ; ????
EC69: D7 00           STB     $00                 
EC6B: ED 08           STD     8,X                 
EC6D: 02 ; ????
EC6E: ED 0D           STD     13,X                
EC70: 02 ; ????
EC71: ED 12           STD     -14,X               
EC73: 02 ; ????
EC74: E0 ; ????
EC75: F0 20 F1        SUBB    $20F1               
EC78: 00 F2           NEG     $F2                 
EC7A: 03 A3           COM     $A3                 
EC7C: 01 ; ????
EC7D: 93 01           SUBD    $01                 
EC7F: 83 01 73        SUBD    #$0173              
EC82: 01 ; ????
EC83: 83 01 73        SUBD    #$0173              
EC86: 01 ; ????
EC87: 63 01           COM     1,X                 
EC89: 53              COMB                        
EC8A: 01 ; ????
EC8B: 63 01           COM     1,X                 
EC8D: 53              COMB                        
EC8E: 01 ; ????
EC8F: 43              COMA                        
EC90: 01 ; ????
EC91: 33 01           LEAU    1,X                 
EC93: 43              COMA                        
EC94: 01 ; ????
EC95: 33 01           LEAU    1,X                 
EC97: 23 01           BLS     $EC9A               ; {}
EC99: 13              SYNC                        
EC9A: 01 ; ????
EC9B: 03 01           COM     $01                 
EC9D: 83 01 43        SUBD    #$0143              
ECA0: 01 ; ????
ECA1: 02 ; ????
ECA2: 01 ; ????
ECA3: C0 14           SUBB    #$14                
ECA5: F3 F0 20        ADDD    $F020               ; {}
ECA8: F1 00 F2        CMPB    $00F2               
ECAB: 03 43           COM     $43                 
ECAD: 01 ; ????
ECAE: 33 01           LEAU    1,X                 
ECB0: 23 01           BLS     $ECB3               ; {}
ECB2: 13              SYNC                        
ECB3: 01 ; ????
ECB4: 23 01           BLS     $ECB7               ; {}
ECB6: 13              SYNC                        
ECB7: 01 ; ????
ECB8: 03 01           COM     $01                 
ECBA: B4 01 03        ANDA    $0103               
ECBD: 01 ; ????
ECBE: B4 01 A4        ANDA    $01A4               
ECC1: 01 ; ????
ECC2: 94 01           ANDA    $01                 
ECC4: A4 01           ANDA    1,X                 
ECC6: 94 01           ANDA    $01                 
ECC8: 84 01           ANDA    #$01                
ECCA: 74 01 64        LSR     $0164               
ECCD: 01 ; ????
ECCE: 23 01           BLS     $ECD1               ; {}
ECD0: A4 01           ANDA    1,X                 
ECD2: 63 01           COM     1,X                 
ECD4: C0 14           SUBB    #$14                
ECD6: F3 F0 20        ADDD    $F020               ; {}
ECD9: F1 00 F2        CMPB    $00F2               
ECDC: 03 13           COM     $13                 
ECDE: 01 ; ????
ECDF: 03 01           COM     $01                 
ECE1: B4 01 A4        ANDA    $01A4               
ECE4: 01 ; ????
ECE5: B4 01 A4        ANDA    $01A4               
ECE8: 01 ; ????
ECE9: 94 01           ANDA    $01                 
ECEB: 84 01           ANDA    #$01                
ECED: 94 01           ANDA    $01                 
ECEF: 84 01           ANDA    #$01                
ECF1: 74 01 64        LSR     $0164               
ECF4: 01 ; ????
ECF5: 74 01 64        LSR     $0164               
ECF8: 01 ; ????
ECF9: 54              LSRB                        
ECFA: 01 ; ????
ECFB: 44              LSRA                        
ECFC: 01 ; ????
ECFD: 34 01           PSHS    CC                  
ECFF: B4 01 74        ANDA    $0174               
ED02: 01 ; ????
ED03: 33 01           LEAU    1,X                 
ED05: C0 14           SUBB    #$14                
ED07: F3 F0 00        ADDD    $F000               ; {}
ED0A: F6 EC 77        LDB     $EC77               ; {}
ED0D: F0 00 F6        SUBB    $00F6               
ED10: EC A8 F0        LDD     $F0,Y               
ED13: 00 F6           NEG     $F6                 
ED15: EC D9 ED 2A     LDD     [$ED2A,U]           
ED19: 00 ED           NEG     $ED                 
ED1B: 3B              RTI                         
ED1C: 00 ED           NEG     $ED                 
ED1E: 4C              INCA                        
ED1F: 00 ED           NEG     $ED                 
ED21: 5D              TSTB                        
ED22: 02 ; ????
ED23: ED 62           STD     2,S                 
ED25: 02 ; ????
ED26: ED 67           STD     7,S                 
ED28: 02 ; ????
ED29: E0 ; ????
ED2A: F0 20 F1        SUBB    $20F1               
ED2D: 0A F2           DEC     $F2                 
ED2F: 04 43           LSR     $43                 
ED31: 01 ; ????
ED32: 83 01 02        SUBD    #$0102              
ED35: 01 ; ????
ED36: 32 01           LEAS    1,X                 
ED38: 43              COMA                        
ED39: 02 ; ????
ED3A: F3 F0 20        ADDD    $F020               ; {}
ED3D: F1 0A F2        CMPB    $0AF2               
ED40: 04 42           LSR     $42                 
ED42: 01 ; ????
ED43: 82 01           SBCA    #$01                
ED45: 01 ; ????
ED46: 01 ; ????
ED47: 31 01           LEAY    1,X                 
ED49: 42 ; ????
ED4A: 02 ; ????
ED4B: F3 F0 20        ADDD    $F020               ; {}
ED4E: F1 0A F2        CMPB    $0AF2               
ED51: 04 23           LSR     $23                 
ED53: 01 ; ????
ED54: A4 01           ANDA    1,X                 
ED56: 64 01           LSR     1,X                 
ED58: 34 01           PSHS    CC                  
ED5A: 23 02           BLS     $ED5E               ; {}
ED5C: F3 F0 00        ADDD    $F000               ; {}
ED5F: F6 ED 2C        LDB     $ED2C               ; {}
ED62: F0 00 F6        SUBB    $00F6               
ED65: ED 3D           STD     -3,Y                
ED67: F0 00 F6        SUBB    $00F6               
ED6A: ED 4E           STD     14,U                
ED6C: ED 79           STD     -7,S                
ED6E: 02 ; ????
ED6F: ED F9 02 EE     STD     [$02EE,S]           
ED73: 39              RTS                         
ED74: 02 ; ????
ED75: EE BD 02 E0     LDU     [$F059,PC]          ; {}
ED79: F0 50 F1        SUBB    $50F1               
ED7C: 09 F2           ROL     $F2                 
ED7E: 08 A3           LSL     $A3                 
ED80: 01 ; ????
ED81: 73 01 73        COM     $0173               
ED84: 01 ; ????
ED85: 73 01 B3        COM     $01B3               
ED88: 01 ; ????
ED89: 73 01 73        COM     $0173               
ED8C: 01 ; ????
ED8D: 73 01 02        COM     $0102               
ED90: 01 ; ????
ED91: 73 01 73        COM     $0173               
ED94: 01 ; ????
ED95: 73 05 F2        COM     $05F2               
ED98: 01 ; ????
ED99: F0 30 C0        SUBB    $30C0               
ED9C: 06 93           ROR     $93                 
ED9E: 06 A3           ROR     $A3                 
EDA0: 0C 02           INC     $02                 
EDA2: 0C A3           INC     $A3                 
EDA4: 06 93           ROR     $93                 
EDA6: 0C 93           INC     $93                 
EDA8: 06 A3           ROR     $A3                 
EDAA: 0C 02           INC     $02                 
EDAC: 0C A3           INC     $A3                 
EDAE: 06 93           ROR     $93                 
EDB0: 0C F1           INC     $F1                 
EDB2: 0A A3           DEC     $A3                 
EDB4: 03 C0           COM     $C0                 
EDB6: 03 F1           COM     $F1                 
EDB8: 09 A3           ROL     $A3                 
EDBA: 1E 93           EXG     B,U                 
EDBC: 0C F1           INC     $F1                 
EDBE: 0A A3           DEC     $A3                 
EDC0: 03 C0           COM     $C0                 
EDC2: 03 F1           COM     $F1                 
EDC4: 09 A3           ROL     $A3                 
EDC6: 1E 63           EXG     ?,U                 
EDC8: 0C 63           INC     $63                 
EDCA: 06 73           ROR     $73                 
EDCC: 0C 83           INC     $83                 
EDCE: 0C 73           INC     $73                 
EDD0: 06 63           ROR     $63                 
EDD2: 0C 63           INC     $63                 
EDD4: 06 73           ROR     $73                 
EDD6: 0C 83           INC     $83                 
EDD8: 0C 73           INC     $73                 
EDDA: 06 53           ROR     $53                 
EDDC: 0C F1           INC     $F1                 
EDDE: 0A A3           DEC     $A3                 
EDE0: 03 C0           COM     $C0                 
EDE2: 03 F1           COM     $F1                 
EDE4: 09 A3           ROL     $A3                 
EDE6: 1E 53           EXG     PC,U                
EDE8: 0C F1           INC     $F1                 
EDEA: 0A A3           DEC     $A3                 
EDEC: 03 C0           COM     $C0                 
EDEE: 03 F1           COM     $F1                 
EDF0: 09 A3           ROL     $A3                 
EDF2: 1E 93           EXG     B,U                 
EDF4: 06 F6           ROR     $F6                 
EDF6: ED 9B           STD     [D,X]               
EDF8: F3 F0 50        ADDD    $F050               ; {}
EDFB: F1 09 F2        CMPB    $09F2               
EDFE: 08 B4           LSL     $B4                 
EE00: 01 ; ????
EE01: A4 01           ANDA    1,X                 
EE03: F4 05 ED        ANDB    $05ED               
EE06: FF B4 01        STU     $B401               
EE09: A4 05           ANDA    5,X                 
EE0B: F0 40 F1        SUBB    $40F1               
EE0E: 07 F2           ASR     $F2                 
EE10: 06 34           ROR     $34                 
EE12: 02 ; ????
EE13: A5 02           BITA    2,X                 
EE15: F4 04 EE        ANDB    $04EE               
EE18: 11 ; ????
EE19: 24 02           BHS     $EE1D               ; {}
EE1B: A5 02           BITA    2,X                 
EE1D: F4 04 EE        ANDB    $04EE               
EE20: 19              DAA                         
EE21: 04 02           LSR     $02                 
EE23: 75 ; ????
EE24: 02 ; ????
EE25: F4 04 EE        ANDB    $04EE               
EE28: 21 A5           BRN     $EDCF               ; {}
EE2A: 02 ; ????
EE2B: 55 ; ????
EE2C: 02 ; ????
EE2D: F4 03 EE        ANDB    $03EE               
EE30: 29 04           BVS     $EE36               ; {}
EE32: 02 ; ????
EE33: 24 02           BHS     $EE37               ; {}
EE35: F6 EE 11        LDB     $EE11               ; {}
EE38: F3 F0 00        ADDD    $F000               ; {}
EE3B: F1 01 F2        CMPB    $01F2               
EE3E: 08 C0           LSL     $C0                 
EE40: 10 ; ????
EE41: F2 06 C0        SBCB    $06C0               
EE44: 01 ; ????
EE45: 73 01 F4        COM     $01F4               
EE48: 07 EE           ASR     $EE                 
EE4A: 43              COMA                        
EE4B: C0 01           SUBB    #$01                
EE4D: 53              COMB                        
EE4E: 01 ; ????
EE4F: F4 08 EE        ANDB    $08EE               
EE52: 4B ; ????
EE53: C0 01           SUBB    #$01                
EE55: 33 01           LEAU    1,X                 
EE57: F4 08 EE        ANDB    $08EE               
EE5A: 53              COMB                        
EE5B: C0 01           SUBB    #$01                
EE5D: 23 01           BLS     $EE60               ; {}
EE5F: C0 01           SUBB    #$01                
EE61: 53              COMB                        
EE62: 01 ; ????
EE63: C0 01           SUBB    #$01                
EE65: 53              COMB                        
EE66: 01 ; ????
EE67: C0 01           SUBB    #$01                
EE69: 53              COMB                        
EE6A: 01 ; ????
EE6B: F4 02 EE        ANDB    $02EE               
EE6E: 5B ; ????
EE6F: C0 01           SUBB    #$01                
EE71: 73 01 F6        COM     $01F6               
EE74: EE 43           LDU     3,U                 
EE76: C0 01           SUBB    #$01                
EE78: 73 01 73        COM     $0173               
EE7B: 02 ; ????
EE7C: 73 02 73        COM     $0273               
EE7F: 01 ; ????
EE80: 73 02 73        COM     $0273               
EE83: 01 ; ????
EE84: 73 02 73        COM     $0273               
EE87: 02 ; ????
EE88: 73 01 53        COM     $0153               
EE8B: 02 ; ????
EE8C: 53              COMB                        
EE8D: 01 ; ????
EE8E: 53              COMB                        
EE8F: 05 ; ????
EE90: 53              COMB                        
EE91: 02 ; ????
EE92: 53              COMB                        
EE93: 01 ; ????
EE94: 53              COMB                        
EE95: 05 ; ????
EE96: 33 02           LEAU    2,X                 
EE98: 33 01           LEAU    1,X                 
EE9A: 33 02           LEAU    2,X                 
EE9C: 33 02           LEAU    2,X                 
EE9E: 33 01           LEAU    1,X                 
EEA0: 33 02           LEAU    2,X                 
EEA2: 33 01           LEAU    1,X                 
EEA4: 33 02           LEAU    2,X                 
EEA6: 33 02           LEAU    2,X                 
EEA8: 33 01           LEAU    1,X                 
EEAA: 23 02           BLS     $EEAE               ; {}
EEAC: 53              COMB                        
EEAD: 01 ; ????
EEAE: 53              COMB                        
EEAF: 05 ; ????
EEB0: 23 02           BLS     $EEB4               ; {}
EEB2: 53              COMB                        
EEB3: 01 ; ????
EEB4: 53              COMB                        
EEB5: 05 ; ????
EEB6: 73 01 F6        COM     $01F6               
EEB9: EE 76           LDU     -10,S               
EEBB: F3 F3 F0        ADDD    $F3F0               ; {}
EEBE: 00 F1           NEG     $F1                 
EEC0: 01 ; ????
EEC1: F2 08 C0        SBCB    $08C0               
EEC4: 10 ; ????
EEC5: F2 06 C0        SBCB    $06C0               
EEC8: 01 ; ????
EEC9: 33 01           LEAU    1,X                 
EECB: F4 07 EE        ANDB    $07EE               
EECE: C7 ; ????
EECF: C0 01           SUBB    #$01                
EED1: 23 01           BLS     $EED4               ; {}
EED3: F4 08 EE        ANDB    $08EE               
EED6: CF ; ????
EED7: C0 01           SUBB    #$01                
EED9: 03 01           COM     $01                 
EEDB: F4 08 EE        ANDB    $08EE               
EEDE: D7 C0           STB     $C0                 
EEE0: 01 ; ????
EEE1: A4 01           ANDA    1,X                 
EEE3: C0 01           SUBB    #$01                
EEE5: 23 01           BLS     $EEE8               ; {}
EEE7: C0 01           SUBB    #$01                
EEE9: A4 01           ANDA    1,X                 
EEEB: C0 01           SUBB    #$01                
EEED: 23 01           BLS     $EEF0               ; {}
EEEF: F4 02 EE        ANDB    $02EE               
EEF2: DF C0           STU     $C0                 
EEF4: 01 ; ????
EEF5: 33 01           LEAU    1,X                 
EEF7: F6 EE C7        LDB     $EEC7               ; {}
EEFA: 33 02           LEAU    2,X                 
EEFC: 33 02           LEAU    2,X                 
EEFE: 33 01           LEAU    1,X                 
EF00: 33 02           LEAU    2,X                 
EF02: 33 01           LEAU    1,X                 
EF04: 33 02           LEAU    2,X                 
EF06: 33 02           LEAU    2,X                 
EF08: 33 01           LEAU    1,X                 
EF0A: 23 02           BLS     $EF0E               ; {}
EF0C: 23 01           BLS     $EF0F               ; {}
EF0E: 23 05           BLS     $EF15               ; {}
EF10: 23 02           BLS     $EF14               ; {}
EF12: 23 01           BLS     $EF15               ; {}
EF14: 23 05           BLS     $EF1B               ; {}
EF16: 03 02           COM     $02                 
EF18: 03 01           COM     $01                 
EF1A: 03 02           COM     $02                 
EF1C: 03 02           COM     $02                 
EF1E: 03 01           COM     $01                 
EF20: 03 02           COM     $02                 
EF22: 03 01           COM     $01                 
EF24: 03 02           COM     $02                 
EF26: 03 02           COM     $02                 
EF28: 03 01           COM     $01                 
EF2A: A4 02           ANDA    2,X                 
EF2C: 23 01           BLS     $EF2F               ; {}
EF2E: 23 05           BLS     $EF35               ; {}
EF30: A4 02           ANDA    2,X                 
EF32: 23 01           BLS     $EF35               ; {}
EF34: 23 05           BLS     $EF3B               ; {}
EF36: 33 01           LEAU    1,X                 
EF38: F6 EE 76        LDB     $EE76               ; {}
EF3B: F3 EF 43        ADDD    $EF43               ; {}
EF3E: 00 EF           NEG     $EF                 
EF40: 80 02           SUBA    #$02                
EF42: E0 ; ????
EF43: F0 30 F1        SUBB    $30F1               
EF46: 00 F2           NEG     $F2                 
EF48: 01 ; ????
EF49: A5 02           BITA    2,X                 
EF4B: 24 02           BHS     $EF4F               ; {}
EF4D: 54              LSRB                        
EF4E: 02 ; ????
EF4F: F1 01 94        CMPB    $0194               
EF52: 01 ; ????
EF53: A4 01           ANDA    1,X                 
EF55: 23 01           BLS     $EF58               ; {}
EF57: 53              COMB                        
EF58: 01 ; ????
EF59: C0 0E           SUBB    #$0E                
EF5B: F0 00 F1        SUBB    $00F1               
EF5E: 00 22           NEG     $22                 
EF60: 03 23           COM     $23                 
EF62: 01 ; ????
EF63: 13              SYNC                        
EF64: 01 ; ????
EF65: 03 02           COM     $02                 
EF67: C0 04           SUBB    #$04                
EF69: F1 02 22        CMPB    $0222               
EF6C: 03 23           COM     $23                 
EF6E: 01 ; ????
EF6F: 13              SYNC                        
EF70: 01 ; ????
EF71: 03 02           COM     $02                 
EF73: C0 04           SUBB    #$04                
EF75: F1 04 22        CMPB    $0422               
EF78: 03 23           COM     $23                 
EF7A: 01 ; ????
EF7B: 13              SYNC                        
EF7C: 01 ; ????
EF7D: 03 02           COM     $02                 
EF7F: F3 F0 30        ADDD    $F030               ; {}
EF82: F1 00 F2        CMPB    $00F2               
EF85: 01 ; ????
EF86: 54              LSRB                        
EF87: 02 ; ????
EF88: 64 02           LSR     2,X                 
EF8A: 74 02 F1        LSR     $02F1               
EF8D: 01 ; ????
EF8E: 84 01           ANDA    #$01                
EF90: 94 01           ANDA    $01                 
EF92: A4 01           ANDA    1,X                 
EF94: B4 01 C0        ANDA    $01C0               
EF97: 0E F0           JMP     $F0                 
EF99: 00 F1           NEG     $F1                 
EF9B: 00 12           NEG     $12                 
EF9D: 03 13           COM     $13                 
EF9F: 01 ; ????
EFA0: 03 01           COM     $01                 
EFA2: B4 02 C0        ANDA    $02C0               
EFA5: 04 F1           LSR     $F1                 
EFA7: 02 ; ????
EFA8: 12              NOP                         
EFA9: 03 13           COM     $13                 
EFAB: 01 ; ????
EFAC: 03 01           COM     $01                 
EFAE: B4 02 C0        ANDA    $02C0               
EFB1: 04 F1           LSR     $F1                 
EFB3: 04 13           LSR     $13                 
EFB5: 03 13           COM     $13                 
EFB7: 01 ; ????
EFB8: 03 01           COM     $01                 
EFBA: B4 02 F3        ANDA    $02F3               
EFBD: EF ; ????
EFBE: CA 00           ORB     #$00                
EFC0: F0 0D 02        SUBB    $0D02               
EFC3: F0 50 01        SUBB    $5001               
EFC6: F0 5F 01        SUBB    $5F01               
EFC9: E0 ; ????
EFCA: F0 70 F1        SUBB    $70F1               
EFCD: 00 F2           NEG     $F2                 
EFCF: 01 ; ????
EFD0: B6 01 05        LDA     $0105               
EFD3: 01 ; ????
EFD4: B6 01 05        LDA     $0105               
EFD7: 01 ; ????
EFD8: C0 02           SUBB    #$02                
EFDA: 15 ; ????
EFDB: 01 ; ????
EFDC: 05 ; ????
EFDD: 01 ; ????
EFDE: 15 ; ????
EFDF: 01 ; ????
EFE0: 05 ; ????
EFE1: 01 ; ????
EFE2: C0 02           SUBB    #$02                
EFE4: A6 01           LDA     1,X                 
EFE6: B6 01 A6        LDA     $01A6               
EFE9: 01 ; ????
EFEA: B6 01 C0        LDA     $01C0               
EFED: 02 ; ????
EFEE: 05 ; ????
EFEF: 01 ; ????
EFF0: B6 01 05        LDA     $0105               
EFF3: 01 ; ????
EFF4: B6 01 C0        LDA     $01C0               
EFF7: 02 ; ????
EFF8: 05 ; ????
EFF9: 01 ; ????
EFFA: 15 ; ????
EFFB: 01 ; ????
EFFC: 05 ; ????
EFFD: 01 ; ????
EFFE: 15 ; ????
EFFF: 01 ; ????
F000: C0 02           SUBB    #$02                
F002: 65 ; ????
F003: 01 ; ????
F004: 55 ; ????
F005: 01 ; ????
F006: 65 ; ????
F007: 01 ; ????
F008: 55 ; ????
F009: 01 ; ????
F00A: C0 02           SUBB    #$02                
F00C: F3 F0 70        ADDD    $F070               ; {}
F00F: F1 00 F2        CMPB    $00F2               
F012: 01 ; ????
F013: 15 ; ????
F014: 01 ; ????
F015: 25 01           BCS     $F018               ; {}
F017: 15 ; ????
F018: 01 ; ????
F019: 25 01           BCS     $F01C               ; {}
F01B: C0 02           SUBB    #$02                
F01D: 35 01           PULS    CC                  
F01F: 25 01           BCS     $F022               ; {}
F021: 35 01           PULS    CC                  
F023: 25 01           BCS     $F026               ; {}
F025: C0 02           SUBB    #$02                
F027: B6 01 05        LDA     $0105               
F02A: 01 ; ????
F02B: B6 01 05        LDA     $0105               
F02E: 01 ; ????
F02F: C0 02           SUBB    #$02                
F031: 15 ; ????
F032: 01 ; ????
F033: 25 01           BCS     $F036               ; {}
F035: 15 ; ????
F036: 01 ; ????
F037: 25 01           BCS     $F03A               ; {}
F039: C0 02           SUBB    #$02                
F03B: 35 01           PULS    CC                  
F03D: 25 01           BCS     $F040               ; {}
F03F: 35 01           PULS    CC                  
F041: 25 01           BCS     $F044               ; {}
F043: C0 02           SUBB    #$02                
F045: 85 01           BITA    #$01                
F047: 75 ; ????
F048: 01 ; ????
F049: 85 01           BITA    #$01                
F04B: 75 ; ????
F04C: 01 ; ????
F04D: C0 02           SUBB    #$02                
F04F: F3 F0 20        ADDD    $F020               ; {}
F052: F1 09 F2        CMPB    $09F2               
F055: 03 36           COM     $36                 
F057: 01 ; ????
F058: 56              RORB                        
F059: 01 ; ????
F05A: F4 06 F0        ANDB    $06F0               
F05D: 56              RORB                        
F05E: F3 F0 70        ADDD    $F070               ; {}
F061: F1 09 F2        CMPB    $09F2               
F064: 03 86           COM     $86                 
F066: 01 ; ????
F067: A6 01           LDA     1,X                 
F069: F4 06 F0        ANDB    $06F0               
F06C: 65 ; ????
F06D: F3 F0 81        ADDD    $F081               ; {}
F070: 00 F0           NEG     $F0                 
F072: 8A 02           ORA     #$02                
F074: F0 95 02        SUBB    $9502               
F077: F0 9A 00        SUBB    $9A00               
F07A: F0 9F 01        SUBB    $9F01               
F07D: F0 A8 01        SUBB    $A801               
F080: E0 ; ????
F081: F0 20 F1        SUBB    $20F1               
F084: 09 F2           ROL     $F2                 
F086: 01 ; ????
F087: B5 04 F3        BITA    $04F3               
F08A: F0 70 F1        SUBB    $70F1               
F08D: 00 F2           NEG     $F2                 
F08F: 02 ; ????
F090: A5 01           BITA    1,X                 
F092: B5 01 F3        BITA    $01F3               
F095: F0 70 F6        SUBB    $70F6               
F098: F0 83 F0        SUBB    $83F0               
F09B: 70 F6 F0        NEG     $F6F0               ; {}
F09E: 8C F0 00        CMPX    #$F000              
F0A1: F1 09 F2        CMPB    $09F2               
F0A4: 01 ; ????
F0A5: B3 04 F3        SUBD    $04F3               
F0A8: F0 20 F1        SUBB    $20F1               
F0AB: 00 F2           NEG     $F2                 
F0AD: 02 ; ????
F0AE: A3 01           SUBD    1,X                 
F0B0: B3 01 F3        SUBD    $01F3               
F0B3: F0 CC 00        SUBB    $CC00               
F0B6: F0 F3 00        SUBB    $F300               ; {}
F0B9: F1 1A 00        CMPB    $1A00               
F0BC: F1 1F 00        CMPB    $1F00               
F0BF: F1 24 00        CMPB    $2400               
F0C2: F1 29 00        CMPB    $2900               
F0C5: F1 29 01        CMPB    $2901               
F0C8: F1 29 02        CMPB    $2902               
F0CB: E0 ; ????
F0CC: F0 20 F1        SUBB    $20F1               
F0CF: 09 F2           ROL     $F2                 
F0D1: 08 34           LSL     $34                 
F0D3: 02 ; ????
F0D4: 34 02           PSHS    A                   
F0D6: A5 01           BITA    1,X                 
F0D8: 34 03           PSHS    A,CC                
F0DA: A5 01           BITA    1,X                 
F0DC: 34 02           PSHS    A                   
F0DE: A5 01           BITA    1,X                 
F0E0: 34 02           PSHS    A                   
F0E2: 34 01           PSHS    CC                  
F0E4: A5 02           BITA    2,X                 
F0E6: 04 02           LSR     $02                 
F0E8: 04 02           LSR     $02                 
F0EA: C0 01           SUBB    #$01                
F0EC: 75 ; ????
F0ED: 03 04           COM     $04                 
F0EF: 03 C0           COM     $C0                 
F0F1: 04 F3           LSR     $F3                 
F0F3: F0 20 F1        SUBB    $20F1               
F0F6: 09 F2           ROL     $F2                 
F0F8: 08 35           LSL     $35                 
F0FA: 02 ; ????
F0FB: 35 02           PULS    A                   
F0FD: 34 03           PSHS    A,CC                
F0FF: 35 01           PULS    CC                  
F101: C0 01           SUBB    #$01                
F103: 35 02           PULS    A                   
F105: 35 01           PULS    CC                  
F107: 34 01           PSHS    CC                  
F109: A5 01           BITA    1,X                 
F10B: C0 01           SUBB    #$01                
F10D: 35 01           PULS    CC                  
F10F: 75 ; ????
F110: 02 ; ????
F111: 75 ; ????
F112: 02 ; ????
F113: 76 03 75        ROR     $0375               
F116: 03 C0           COM     $C0                 
F118: 04 F3           LSR     $F3                 
F11A: F0 30 F6        SUBB    $30F6               
F11D: F0 CE F0        SUBB    $CEF0               
F120: 30 F6           LEAX    [A,S]               
F122: F0 F5 F0        SUBB    $F5F0               ; {}
F125: 50              NEGB                        
F126: F6 F0 CE        LDB     $F0CE               ; {}
F129: F0 50 F6        SUBB    $50F6               
F12C: F0 F5 F1        SUBB    $F5F1               ; {}
F12F: 3B              RTI                         
F130: 00 F1           NEG     $F1                 
F132: 68 00           ASL     0,X                 
F134: F1 3B 02        CMPB    $3B02               
F137: F1 68 02        CMPB    $6802               
F13A: E0 ; ????
F13B: F0 30 F1        SUBB    $30F1               
F13E: 00 F2           NEG     $F2                 
F140: 01 ; ????
F141: 54              LSRB                        
F142: 01 ; ????
F143: 64 01           LSR     1,X                 
F145: 84 01           ANDA    #$01                
F147: A4 01           ANDA    1,X                 
F149: 03 01           COM     $01                 
F14B: 33 02           LEAU    2,X                 
F14D: C0 0A           SUBB    #$0A                
F14F: 53              COMB                        
F150: 01 ; ????
F151: 33 01           LEAU    1,X                 
F153: 23 01           BLS     $F156               ; {}
F155: 03 02           COM     $02                 
F157: C0 08           SUBB    #$08                
F159: A4 01           ANDA    1,X                 
F15B: 94 01           ANDA    $01                 
F15D: 84 01           ANDA    #$01                
F15F: 74 01 64        LSR     $0164               
F162: 01 ; ????
F163: 54              LSRB                        
F164: 01 ; ????
F165: 44              LSRA                        
F166: 01 ; ????
F167: F3 F0 20        ADDD    $F020               ; {}
F16A: F1 00 F2        CMPB    $00F2               
F16D: 01 ; ????
F16E: 53              COMB                        
F16F: 01 ; ????
F170: 63 01           COM     1,X                 
F172: 83 01 A3        SUBD    #$01A3              
F175: 01 ; ????
F176: 02 ; ????
F177: 01 ; ????
F178: 32 02           LEAS    2,X                 
F17A: C0 0A           SUBB    #$0A                
F17C: 52 ; ????
F17D: 01 ; ????
F17E: 32 01           LEAS    1,X                 
F180: 22 01           BHI     $F183               ; {}
F182: 02 ; ????
F183: 02 ; ????
F184: C0 08           SUBB    #$08                
F186: A3 01           SUBD    1,X                 
F188: 93 01           SUBD    $01                 
F18A: 83 01 73        SUBD    #$0173              
F18D: 01 ; ????
F18E: 63 01           COM     1,X                 
F190: 53              COMB                        
F191: 01 ; ????
F192: 43              COMA                        
F193: 01 ; ????
F194: F3 F1 A8        ADDD    $F1A8               ; {}
F197: 00 F1           NEG     $F1                 
F199: C3 00 F1        ADDD    #$00F1              
F19C: DE 00           LDU     $00                 
F19E: F1 F3 00        CMPB    $F300               ; {}
F1A1: F2 06 00        SBCB    $0600               
F1A4: F1 C3 01        CMPB    $C301               
F1A7: E0 ; ????
F1A8: F0 20 F1        SUBB    $20F1               
F1AB: 0E F2           JMP     $F2                 
F1AD: 06 A3           ROR     $A3                 
F1AF: 02 ; ????
F1B0: 02 ; ????
F1B1: 01 ; ????
F1B2: 22 02           BHI     $F1B6               ; {}
F1B4: A3 01           SUBD    1,X                 
F1B6: B3 02 02        SUBD    $0202               
F1B9: 01 ; ????
F1BA: 22 03           BHI     $F1BF               ; {}
F1BC: 32 03           LEAS    3,X                 
F1BE: 32 02           LEAS    2,X                 
F1C0: 31 07           LEAY    7,X                 
F1C2: F3 F0 00        ADDD    $F000               ; {}
F1C5: F1 0E F2        CMPB    $0EF2               
F1C8: 06 A4           ROR     $A4                 
F1CA: 02 ; ????
F1CB: 03 01           COM     $01                 
F1CD: 23 02           BLS     $F1D1               ; {}
F1CF: A4 01           ANDA    1,X                 
F1D1: B4 02 03        ANDA    $0203               
F1D4: 01 ; ????
F1D5: 23 03           BLS     $F1DA               ; {}
F1D7: 33 03           LEAU    3,X                 
F1D9: 33 02           LEAU    2,X                 
F1DB: 32 07           LEAS    7,X                 
F1DD: F3 F0 40        ADDD    $F040               ; {}
F1E0: F1 0B F2        CMPB    $0BF2               
F1E3: 06 A5           ROR     $A5                 
F1E5: 03 85           COM     $85                 
F1E7: 03 75           COM     $75                 
F1E9: 03 55           COM     $55                 
F1EB: 03 35           COM     $35                 
F1ED: 03 A6           COM     $A6                 
F1EF: 02 ; ????
F1F0: 35 07           PULS    CC,A,B              
F1F2: F3 F0 60        ADDD    $F060               ; {}
F1F5: F1 09 F2        CMPB    $09F2               
F1F8: 06 C0           ROR     $C0                 
F1FA: 02 ; ????
F1FB: 03 01           COM     $01                 
F1FD: F4 04 F1        ANDB    $04F1               
F200: F9 A4 03        ADCB    $A403               
F203: C0 09           SUBB    #$09                
F205: F3 F0 60        ADDD    $F060               ; {}
F208: F1 09 F2        CMPB    $09F2               
F20B: 06 C0           ROR     $C0                 
F20D: 02 ; ????
F20E: A4 01           ANDA    1,X                 
F210: F4 04 F2        ANDB    $04F2               
F213: 0C 74           INC     $74                 
F215: 03 C0           COM     $C0                 
F217: 03 F1           COM     $F1                 
F219: 04 F0           LSR     $F0                 
F21B: 30 ; ????
F21C: F2 03 A2        SBCB    $03A2               
F21F: 01 ; ????
F220: 31 01           LEAY    1,X                 
F222: F4 02 F2        ANDB    $02F2               
F225: 1E F1           EXG     ?,X                 
F227: 05 ; ????
F228: A2 01           SBCA    1,X                 
F22A: 31 01           LEAY    1,X                 
F22C: F4 03 F2        ANDB    $03F2               
F22F: 28 C0           BVC     $F1F1               ; {}
F231: 02 ; ????
F232: F3 F2 4C        ADDD    $F24C               ; {}
F235: 00 F2           NEG     $F2                 
F237: A8 01           EORA    1,X                 
F239: F3 01 00        ADDD    $0100               
F23C: F3 37 00        ADDD    $3700               
F23F: F3 67 00        ADDD    $6700               
F242: F3 97 00        ADDD    $9700               
F245: F3 CF 00        ADDD    $CF00               
F248: F2 AD 01        SBCB    $AD01               
F24B: E0 ; ????
F24C: F0 30 F1        SUBB    $30F1               
F24F: 09 F2           ROL     $F2                 
F251: 06 A3           ROR     $A3                 
F253: 01 ; ????
F254: 02 ; ????
F255: 01 ; ????
F256: A3 02           SUBD    2,X                 
F258: 32 02           LEAS    2,X                 
F25A: A3 01           SUBD    1,X                 
F25C: 02 ; ????
F25D: 01 ; ????
F25E: A3 02           SUBD    2,X                 
F260: F1 0E 32        CMPB    $0E32               
F263: 06 F1           ROR     $F1                 
F265: 09 73           ROL     $73                 
F267: 02 ; ????
F268: F1 01 73        CMPB    $0173               
F26B: 02 ; ????
F26C: F1 09 63        CMPB    $0963               
F26F: 02 ; ????
F270: F1 0B 73        CMPB    $0B73               
F273: 08 F1           LSL     $F1                 
F275: 09 53           ROL     $53                 
F277: 01 ; ????
F278: 73 01 53        COM     $0153               
F27B: 02 ; ????
F27C: A3 02           SUBD    2,X                 
F27E: 53              COMB                        
F27F: 01 ; ????
F280: 73 01 53        COM     $0153               
F283: 02 ; ????
F284: F1 0E A4        CMPB    $0EA4               
F287: 08 F5           LSL     $F5                 
F289: 02 ; ????
F28A: F2 9B F1        SBCB    $9BF1               
F28D: 0C 73           INC     $73                 
F28F: 04 83           LSR     $83                 
F291: 04 93           LSR     $93                 
F293: 04 A3           LSR     $A3                 
F295: 04 F1           LSR     $F1                 
F297: 09 F6           ROL     $F6                 
F299: F2 52 F1        SBCB    $52F1               
F29C: 09 33           ROL     $33                 
F29E: 02 ; ????
F29F: 33 02           LEAU    2,X                 
F2A1: 33 02           LEAU    2,X                 
F2A3: 33 02           LEAU    2,X                 
F2A5: C0 08           SUBB    #$08                
F2A7: F3 F0 00        ADDD    $F000               ; {}
F2AA: F6 F2 4E        LDB     $F24E               ; {}
F2AD: F0 50 F1        SUBB    $50F1               
F2B0: 12              NOP                         
F2B1: F2 06 35        SBCB    $0635               
F2B4: 04 A6           LSR     $A6                 
F2B6: 04 F4           LSR     $F4                 
F2B8: 04 F2           LSR     $F2                 
F2BA: B3 25 04        SUBD    $2504               
F2BD: 15 ; ????
F2BE: 04 05           LSR     $05                 
F2C0: 04 A6           LSR     $A6                 
F2C2: 04 F5           LSR     $F5                 
F2C4: 02 ; ????
F2C5: F2 D6 F1        SBCB    $D6F1               
F2C8: 13              SYNC                        
F2C9: 35 04           PULS    B                   
F2CB: 45 ; ????
F2CC: 04 55           LSR     $55                 
F2CE: 04 A6           LSR     $A6                 
F2D0: 04 F1           LSR     $F1                 
F2D2: 12              NOP                         
F2D3: F6 F2 B3        LDB     $F2B3               ; {}
F2D6: F1 09 35        CMPB    $0935               
F2D9: 02 ; ????
F2DA: 35 02           PULS    A                   
F2DC: 35 02           PULS    A                   
F2DE: 35 02           PULS    A                   
F2E0: C0 02           SUBB    #$02                
F2E2: F2 02 F0        SBCB    $02F0               
F2E5: 20 F1           BRA     $F2D8               ; {}
F2E7: 00 97           NEG     $97                 
F2E9: 01 ; ????
F2EA: 46              RORA                        
F2EB: 01 ; ????
F2EC: B6 01 65        LDA     $0165               
F2EF: 01 ; ????
F2F0: 14 ; ????
F2F1: 01 ; ????
F2F2: 84 01           ANDA    #$01                
F2F4: 33 01           LEAU    1,X                 
F2F6: 23 01           BLS     $F2F9               ; {}
F2F8: 33 01           LEAU    1,X                 
F2FA: 43              COMA                        
F2FB: 01 ; ????
F2FC: 33 01           LEAU    1,X                 
F2FE: C0 07           SUBB    #$07                
F300: F3 F0 40        ADDD    $F040               ; {}
F303: F1 10 F2        CMPB    $10F2               
F306: 06 35           ROR     $35                 
F308: 04 A6           LSR     $A6                 
F30A: 04 F4           LSR     $F4                 
F30C: 04 F3           LSR     $F3                 
F30E: 07 25           ASR     $25                 
F310: 04 15           LSR     $15                 
F312: 04 05           LSR     $05                 
F314: 04 A6           LSR     $A6                 
F316: 04 F5           LSR     $F5                 
F318: 02 ; ????
F319: F3 2A F1        ADDD    $2AF1               
F31C: 0C 35           INC     $35                 
F31E: 04 45           LSR     $45                 
F320: 04 55           LSR     $55                 
F322: 04 A6           LSR     $A6                 
F324: 04 F1           LSR     $F1                 
F326: 10 ; ????
F327: F6 F3 07        LDB     $F307               ; {}
F32A: F1 09 35        CMPB    $0935               
F32D: 02 ; ????
F32E: 35 02           PULS    A                   
F330: 35 02           PULS    A                   
F332: 35 02           PULS    A                   
F334: C0 08           SUBB    #$08                
F336: F3 F0 60        ADDD    $F060               ; {}
F339: F1 09 F2        CMPB    $09F2               
F33C: 06 C0           ROR     $C0                 
F33E: 02 ; ????
F33F: 03 02           COM     $02                 
F341: F4 0C F3        ANDB    $0CF3               
F344: 3D              MUL                         
F345: F5 02 F3        BITB    $02F3               
F348: 5C              INCB                        
F349: C0 02           SUBB    #$02                
F34B: 03 02           COM     $02                 
F34D: C0 02           SUBB    #$02                
F34F: 13              SYNC                        
F350: 02 ; ????
F351: C0 02           SUBB    #$02                
F353: 23 02           BLS     $F357               ; {}
F355: C0 02           SUBB    #$02                
F357: 23 02           BLS     $F35B               ; {}
F359: F6 F3 3D        LDB     $F33D               ; {}
F35C: 03 02           COM     $02                 
F35E: 03 02           COM     $02                 
F360: 03 02           COM     $02                 
F362: 03 02           COM     $02                 
F364: C0 08           SUBB    #$08                
F366: F3 F0 60        ADDD    $F060               ; {}
F369: F1 09 F2        CMPB    $09F2               
F36C: 06 C0           ROR     $C0                 
F36E: 02 ; ????
F36F: A4 02           ANDA    2,X                 
F371: F4 0C F3        ANDB    $0CF3               
F374: 6D F5           TST     [B,S]               
F376: 02 ; ????
F377: F3 8C C0        ADDD    $8CC0               
F37A: 02 ; ????
F37B: A4 02           ANDA    2,X                 
F37D: C0 02           SUBB    #$02                
F37F: B4 02 C0        ANDA    $02C0               
F382: 02 ; ????
F383: 03 02           COM     $02                 
F385: C0 02           SUBB    #$02                
F387: 23 02           BLS     $F38B               ; {}
F389: F6 F3 6D        LDB     $F36D               ; {}
F38C: A4 02           ANDA    2,X                 
F38E: A4 02           ANDA    2,X                 
F390: A4 02           ANDA    2,X                 
F392: A4 02           ANDA    2,X                 
F394: C0 08           SUBB    #$08                
F396: F3 F0 60        ADDD    $F060               ; {}
F399: F1 09 F2        CMPB    $09F2               
F39C: 06 C0           ROR     $C0                 
F39E: 02 ; ????
F39F: 74 02 F4        LSR     $02F4               
F3A2: 08 F3           LSL     $F3                 
F3A4: 9D C0           JSR     $C0                 
F3A6: 02 ; ????
F3A7: 84 02           ANDA    #$02                
F3A9: F4 04 F3        ANDB    $04F3               
F3AC: A5 F5           BITA    [B,S]               
F3AE: 02 ; ????
F3AF: F3 C4 C0        ADDD    $C4C0               
F3B2: 02 ; ????
F3B3: 74 02 C0        LSR     $02C0               
F3B6: 02 ; ????
F3B7: 94 02           ANDA    $02                 
F3B9: C0 02           SUBB    #$02                
F3BB: 94 02           ANDA    $02                 
F3BD: C0 02           SUBB    #$02                
F3BF: A4 02           ANDA    2,X                 
F3C1: F6 F3 9D        LDB     $F39D               ; {}
F3C4: 74 02 74        LSR     $0274               
F3C7: 02 ; ????
F3C8: 74 02 74        LSR     $0274               
F3CB: 02 ; ????
F3CC: C0 08           SUBB    #$08                
F3CE: F3 F0 20        ADDD    $F020               ; {}
F3D1: F2 06 F1        SBCB    $06F1               
F3D4: 09 C0           ROL     $C0                 
F3D6: 10 ; ????
F3D7: A4 02           ANDA    2,X                 
F3D9: F1 01 A4        CMPB    $01A4               
F3DC: 02 ; ????
F3DD: F1 09 94        CMPB    $0994               
F3E0: 02 ; ????
F3E1: F1 0B A4        CMPB    $0BA4               
F3E4: 08 C0           LSL     $C0                 
F3E6: 12              NOP                         
F3E7: F5 02 F3        BITB    $02F3               
F3EA: F8 F1 0C        EORB    $F10C               ; {}
F3ED: A4 04           ANDA    4,X                 
F3EF: B4 04 03        ANDA    $0403               
F3F2: 04 23           LSR     $23                 
F3F4: 04 F6           LSR     $F6                 
F3F6: F3 D3 F1        ADDD    $D3F1               
F3F9: 09 74           ROL     $74                 
F3FB: 02 ; ????
F3FC: 74 02 74        LSR     $0274               
F3FF: 02 ; ????
F400: 74 02 C0        LSR     $02C0               
F403: 02 ; ????
F404: F2 02 F0        SBCB    $02F0               
F407: 20 F1           BRA     $F3FA               ; {}
F409: 00 97           NEG     $97                 
F40B: 01 ; ????
F40C: 46              RORA                        
F40D: 01 ; ????
F40E: B6 01 65        LDA     $0165               
F411: 01 ; ????
F412: 14 ; ????
F413: 01 ; ????
F414: 84 01           ANDA    #$01                
F416: 33 01           LEAU    1,X                 
F418: 23 01           BLS     $F41B               ; {}
F41A: 33 01           LEAU    1,X                 
F41C: 43              COMA                        
F41D: 01 ; ????
F41E: 33 01           LEAU    1,X                 
F420: C0 07           SUBB    #$07                
F422: F3 FF FF        ADDD    $FFFF               
F425: FF FF FF        STU     $FFFF               
F428: FF FF FF        STU     $FFFF               
F42B: FF FF FF        STU     $FFFF               
F42E: FF FF FF        STU     $FFFF               
F431: FF FF FF        STU     $FFFF               
F434: FF FF FF        STU     $FFFF               
F437: FF FF FF        STU     $FFFF               
F43A: FF FF FF        STU     $FFFF               
F43D: FF FF FF        STU     $FFFF               
F440: FF FF FF        STU     $FFFF               
F443: FF FF FF        STU     $FFFF               
F446: FF FF FF        STU     $FFFF               
F449: FF FF FF        STU     $FFFF               
F44C: FF FF FF        STU     $FFFF               
F44F: FF FF FF        STU     $FFFF               
F452: FF FF FF        STU     $FFFF               
F455: FF FF FF        STU     $FFFF               
F458: FF FF FF        STU     $FFFF               
F45B: FF FF FF        STU     $FFFF               
F45E: FF FF FF        STU     $FFFF               
F461: FF FF FF        STU     $FFFF               
F464: FF FF FF        STU     $FFFF               
F467: FF FF FF        STU     $FFFF               
F46A: FF FF FF        STU     $FFFF               
F46D: FF FF FF        STU     $FFFF               
F470: FF FF FF        STU     $FFFF               
F473: FF FF FF        STU     $FFFF               
F476: FF FF FF        STU     $FFFF               
F479: FF FF FF        STU     $FFFF               
F47C: FF FF FF        STU     $FFFF               
F47F: FF FF FF        STU     $FFFF               
F482: FF FF FF        STU     $FFFF               
F485: FF FF FF        STU     $FFFF               
F488: FF FF FF        STU     $FFFF               
F48B: FF FF FF        STU     $FFFF               
F48E: FF FF FF        STU     $FFFF               
F491: FF FF FF        STU     $FFFF               
F494: FF FF FF        STU     $FFFF               
F497: FF FF FF        STU     $FFFF               
F49A: FF FF FF        STU     $FFFF               
F49D: FF FF FF        STU     $FFFF               
F4A0: FF FF FF        STU     $FFFF               
F4A3: FF FF FF        STU     $FFFF               
F4A6: FF FF FF        STU     $FFFF               
F4A9: FF FF FF        STU     $FFFF               
F4AC: FF FF FF        STU     $FFFF               
F4AF: FF FF FF        STU     $FFFF               
F4B2: FF FF FF        STU     $FFFF               
F4B5: FF FF FF        STU     $FFFF               
F4B8: FF FF FF        STU     $FFFF               
F4BB: FF FF FF        STU     $FFFF               
F4BE: FF FF FF        STU     $FFFF               
F4C1: FF FF FF        STU     $FFFF               
F4C4: FF FF FF        STU     $FFFF               
F4C7: FF FF FF        STU     $FFFF               
F4CA: FF FF FF        STU     $FFFF               
F4CD: FF FF FF        STU     $FFFF               
F4D0: FF FF FF        STU     $FFFF               
F4D3: FF FF FF        STU     $FFFF               
F4D6: FF FF FF        STU     $FFFF               
F4D9: FF FF FF        STU     $FFFF               
F4DC: FF FF FF        STU     $FFFF               
F4DF: FF FF FF        STU     $FFFF               
F4E2: FF FF FF        STU     $FFFF               
F4E5: FF FF FF        STU     $FFFF               
F4E8: FF FF FF        STU     $FFFF               
F4EB: FF FF FF        STU     $FFFF               
F4EE: FF FF FF        STU     $FFFF               
F4F1: FF FF FF        STU     $FFFF               
F4F4: FF FF FF        STU     $FFFF               
F4F7: FF FF FF        STU     $FFFF               
F4FA: FF FF FF        STU     $FFFF               
F4FD: FF FF FF        STU     $FFFF               
F500: FF FF FF        STU     $FFFF               
F503: FF FF FF        STU     $FFFF               
F506: FF FF FF        STU     $FFFF               
F509: FF FF FF        STU     $FFFF               
F50C: FF FF FF        STU     $FFFF               
F50F: FF FF FF        STU     $FFFF               
F512: FF FF FF        STU     $FFFF               
F515: FF FF FF        STU     $FFFF               
F518: FF FF FF        STU     $FFFF               
F51B: FF FF FF        STU     $FFFF               
F51E: FF FF FF        STU     $FFFF               
F521: FF FF FF        STU     $FFFF               
F524: FF FF FF        STU     $FFFF               
F527: FF FF FF        STU     $FFFF               
F52A: FF FF FF        STU     $FFFF               
F52D: FF FF FF        STU     $FFFF               
F530: FF FF FF        STU     $FFFF               
F533: FF FF FF        STU     $FFFF               
F536: FF FF FF        STU     $FFFF               
F539: FF FF FF        STU     $FFFF               
F53C: FF FF FF        STU     $FFFF               
F53F: FF FF FF        STU     $FFFF               
F542: FF FF FF        STU     $FFFF               
F545: FF FF FF        STU     $FFFF               
F548: FF FF FF        STU     $FFFF               
F54B: FF FF FF        STU     $FFFF               
F54E: FF FF FF        STU     $FFFF               
F551: FF FF FF        STU     $FFFF               
F554: FF FF FF        STU     $FFFF               
F557: FF FF FF        STU     $FFFF               
F55A: FF FF FF        STU     $FFFF               
F55D: FF FF FF        STU     $FFFF               
F560: FF FF FF        STU     $FFFF               
F563: FF FF FF        STU     $FFFF               
F566: FF FF FF        STU     $FFFF               
F569: FF FF FF        STU     $FFFF               
F56C: FF FF FF        STU     $FFFF               
F56F: FF FF FF        STU     $FFFF               
F572: FF FF FF        STU     $FFFF               
F575: FF FF FF        STU     $FFFF               
F578: FF FF FF        STU     $FFFF               
F57B: FF FF FF        STU     $FFFF               
F57E: FF FF FF        STU     $FFFF               
F581: FF FF FF        STU     $FFFF               
F584: FF FF FF        STU     $FFFF               
F587: FF FF FF        STU     $FFFF               
F58A: FF FF FF        STU     $FFFF               
F58D: FF FF FF        STU     $FFFF               
F590: FF FF FF        STU     $FFFF               
F593: FF FF FF        STU     $FFFF               
F596: FF FF FF        STU     $FFFF               
F599: FF FF FF        STU     $FFFF               
F59C: FF FF FF        STU     $FFFF               
F59F: FF FF FF        STU     $FFFF               
F5A2: FF FF FF        STU     $FFFF               
F5A5: FF FF FF        STU     $FFFF               
F5A8: FF FF FF        STU     $FFFF               
F5AB: FF FF FF        STU     $FFFF               
F5AE: FF FF FF        STU     $FFFF               
F5B1: FF FF FF        STU     $FFFF               
F5B4: FF FF FF        STU     $FFFF               
F5B7: FF FF FF        STU     $FFFF               
F5BA: FF FF FF        STU     $FFFF               
F5BD: FF FF FF        STU     $FFFF               
F5C0: FF FF FF        STU     $FFFF               
F5C3: FF FF FF        STU     $FFFF               
F5C6: FF FF FF        STU     $FFFF               
F5C9: FF FF FF        STU     $FFFF               
F5CC: FF FF FF        STU     $FFFF               
F5CF: FF FF FF        STU     $FFFF               
F5D2: FF FF FF        STU     $FFFF               
F5D5: FF FF FF        STU     $FFFF               
F5D8: FF FF FF        STU     $FFFF               
F5DB: FF FF FF        STU     $FFFF               
F5DE: FF FF FF        STU     $FFFF               
F5E1: FF FF FF        STU     $FFFF               
F5E4: FF FF FF        STU     $FFFF               
F5E7: FF FF FF        STU     $FFFF               
F5EA: FF FF FF        STU     $FFFF               
F5ED: FF FF FF        STU     $FFFF               
F5F0: FF FF FF        STU     $FFFF               
F5F3: FF FF FF        STU     $FFFF               
F5F6: FF FF FF        STU     $FFFF               
F5F9: FF FF FF        STU     $FFFF               
F5FC: FF FF FF        STU     $FFFF               
F5FF: FF FF FF        STU     $FFFF               
F602: FF FF FF        STU     $FFFF               
F605: FF FF FF        STU     $FFFF               
F608: FF FF FF        STU     $FFFF               
F60B: FF FF FF        STU     $FFFF               
F60E: FF FF FF        STU     $FFFF               
F611: FF FF FF        STU     $FFFF               
F614: FF FF FF        STU     $FFFF               
F617: FF FF FF        STU     $FFFF               
F61A: FF FF FF        STU     $FFFF               
F61D: FF FF FF        STU     $FFFF               
F620: FF FF FF        STU     $FFFF               
F623: FF FF FF        STU     $FFFF               
F626: FF FF FF        STU     $FFFF               
F629: FF FF FF        STU     $FFFF               
F62C: FF FF FF        STU     $FFFF               
F62F: FF FF FF        STU     $FFFF               
F632: FF FF FF        STU     $FFFF               
F635: FF FF FF        STU     $FFFF               
F638: FF FF FF        STU     $FFFF               
F63B: FF FF FF        STU     $FFFF               
F63E: FF FF FF        STU     $FFFF               
F641: FF FF FF        STU     $FFFF               
F644: FF FF FF        STU     $FFFF               
F647: FF FF FF        STU     $FFFF               
F64A: FF FF FF        STU     $FFFF               
F64D: FF FF FF        STU     $FFFF               
F650: FF FF FF        STU     $FFFF               
F653: FF FF FF        STU     $FFFF               
F656: FF FF FF        STU     $FFFF               
F659: FF FF FF        STU     $FFFF               
F65C: FF FF FF        STU     $FFFF               
F65F: FF FF FF        STU     $FFFF               
F662: FF FF FF        STU     $FFFF               
F665: FF FF FF        STU     $FFFF               
F668: FF FF FF        STU     $FFFF               
F66B: FF FF FF        STU     $FFFF               
F66E: FF FF FF        STU     $FFFF               
F671: FF FF FF        STU     $FFFF               
F674: FF FF FF        STU     $FFFF               
F677: FF FF FF        STU     $FFFF               
F67A: FF FF FF        STU     $FFFF               
F67D: FF FF FF        STU     $FFFF               
F680: FF FF FF        STU     $FFFF               
F683: FF FF FF        STU     $FFFF               
F686: FF FF FF        STU     $FFFF               
F689: FF FF FF        STU     $FFFF               
F68C: FF FF FF        STU     $FFFF               
F68F: FF FF FF        STU     $FFFF               
F692: FF FF FF        STU     $FFFF               
F695: FF FF FF        STU     $FFFF               
F698: FF FF FF        STU     $FFFF               
F69B: FF FF FF        STU     $FFFF               
F69E: FF FF FF        STU     $FFFF               
F6A1: FF FF FF        STU     $FFFF               
F6A4: FF FF FF        STU     $FFFF               
F6A7: FF FF FF        STU     $FFFF               
F6AA: FF FF FF        STU     $FFFF               
F6AD: FF FF FF        STU     $FFFF               
F6B0: FF FF FF        STU     $FFFF               
F6B3: FF FF FF        STU     $FFFF               
F6B6: FF FF FF        STU     $FFFF               
F6B9: FF FF FF        STU     $FFFF               
F6BC: FF FF FF        STU     $FFFF               
F6BF: FF FF FF        STU     $FFFF               
F6C2: FF FF FF        STU     $FFFF               
F6C5: FF FF FF        STU     $FFFF               
F6C8: FF FF FF        STU     $FFFF               
F6CB: FF FF FF        STU     $FFFF               
F6CE: FF FF FF        STU     $FFFF               
F6D1: FF FF FF        STU     $FFFF               
F6D4: FF FF FF        STU     $FFFF               
F6D7: FF FF FF        STU     $FFFF               
F6DA: FF FF FF        STU     $FFFF               
F6DD: FF FF FF        STU     $FFFF               
F6E0: FF FF FF        STU     $FFFF               
F6E3: FF FF FF        STU     $FFFF               
F6E6: FF FF FF        STU     $FFFF               
F6E9: FF FF FF        STU     $FFFF               
F6EC: FF FF FF        STU     $FFFF               
F6EF: FF FF FF        STU     $FFFF               
F6F2: FF FF FF        STU     $FFFF               
F6F5: FF FF FF        STU     $FFFF               
F6F8: FF FF FF        STU     $FFFF               
F6FB: FF FF FF        STU     $FFFF               
F6FE: FF FF FF        STU     $FFFF               
F701: FF FF FF        STU     $FFFF               
F704: FF FF FF        STU     $FFFF               
F707: FF FF FF        STU     $FFFF               
F70A: FF FF FF        STU     $FFFF               
F70D: FF FF FF        STU     $FFFF               
F710: FF FF FF        STU     $FFFF               
F713: FF FF FF        STU     $FFFF               
F716: FF FF FF        STU     $FFFF               
F719: FF FF FF        STU     $FFFF               
F71C: FF FF FF        STU     $FFFF               
F71F: FF FF FF        STU     $FFFF               
F722: FF FF FF        STU     $FFFF               
F725: FF FF FF        STU     $FFFF               
F728: FF FF FF        STU     $FFFF               
F72B: FF FF FF        STU     $FFFF               
F72E: FF FF FF        STU     $FFFF               
F731: FF FF FF        STU     $FFFF               
F734: FF FF FF        STU     $FFFF               
F737: FF FF FF        STU     $FFFF               
F73A: FF FF FF        STU     $FFFF               
F73D: FF FF FF        STU     $FFFF               
F740: FF FF FF        STU     $FFFF               
F743: FF FF FF        STU     $FFFF               
F746: FF FF FF        STU     $FFFF               
F749: FF FF FF        STU     $FFFF               
F74C: FF FF FF        STU     $FFFF               
F74F: FF FF FF        STU     $FFFF               
F752: FF FF FF        STU     $FFFF               
F755: FF FF FF        STU     $FFFF               
F758: FF FF FF        STU     $FFFF               
F75B: FF FF FF        STU     $FFFF               
F75E: FF FF FF        STU     $FFFF               
F761: FF FF FF        STU     $FFFF               
F764: FF FF FF        STU     $FFFF               
F767: FF FF FF        STU     $FFFF               
F76A: FF FF FF        STU     $FFFF               
F76D: FF FF FF        STU     $FFFF               
F770: FF FF FF        STU     $FFFF               
F773: FF FF FF        STU     $FFFF               
F776: FF FF FF        STU     $FFFF               
F779: FF FF FF        STU     $FFFF               
F77C: FF FF FF        STU     $FFFF               
F77F: FF FF FF        STU     $FFFF               
F782: FF FF FF        STU     $FFFF               
F785: FF FF FF        STU     $FFFF               
F788: FF FF FF        STU     $FFFF               
F78B: FF FF FF        STU     $FFFF               
F78E: FF FF FF        STU     $FFFF               
F791: FF FF FF        STU     $FFFF               
F794: FF FF FF        STU     $FFFF               
F797: FF FF FF        STU     $FFFF               
F79A: FF FF FF        STU     $FFFF               
F79D: FF FF FF        STU     $FFFF               
F7A0: FF FF FF        STU     $FFFF               
F7A3: FF FF FF        STU     $FFFF               
F7A6: FF FF FF        STU     $FFFF               
F7A9: FF FF FF        STU     $FFFF               
F7AC: FF FF FF        STU     $FFFF               
F7AF: FF FF FF        STU     $FFFF               
F7B2: FF FF FF        STU     $FFFF               
F7B5: FF FF FF        STU     $FFFF               
F7B8: FF FF FF        STU     $FFFF               
F7BB: FF FF FF        STU     $FFFF               
F7BE: FF FF FF        STU     $FFFF               
F7C1: FF FF FF        STU     $FFFF               
F7C4: FF FF FF        STU     $FFFF               
F7C7: FF FF FF        STU     $FFFF               
F7CA: FF FF FF        STU     $FFFF               
F7CD: FF FF FF        STU     $FFFF               
F7D0: FF FF FF        STU     $FFFF               
F7D3: FF FF FF        STU     $FFFF               
F7D6: FF FF FF        STU     $FFFF               
F7D9: FF FF FF        STU     $FFFF               
F7DC: FF FF FF        STU     $FFFF               
F7DF: FF FF FF        STU     $FFFF               
F7E2: FF FF FF        STU     $FFFF               
F7E5: FF FF FF        STU     $FFFF               
F7E8: FF FF FF        STU     $FFFF               
F7EB: FF FF FF        STU     $FFFF               
F7EE: FF FF FF        STU     $FFFF               
F7F1: FF FF FF        STU     $FFFF               
F7F4: FF FF FF        STU     $FFFF               
F7F7: FF FF FF        STU     $FFFF               
F7FA: FF FF FF        STU     $FFFF               
F7FD: FF FF FF        STU     $FFFF               
F800: FF FF FF        STU     $FFFF               
F803: FF FF FF        STU     $FFFF               
F806: FF FF FF        STU     $FFFF               
F809: FF FF FF        STU     $FFFF               
F80C: FF FF FF        STU     $FFFF               
F80F: FF FF FF        STU     $FFFF               
F812: FF FF FF        STU     $FFFF               
F815: FF FF FF        STU     $FFFF               
F818: FF FF FF        STU     $FFFF               
F81B: FF FF FF        STU     $FFFF               
F81E: FF FF FF        STU     $FFFF               
F821: FF FF FF        STU     $FFFF               
F824: FF FF FF        STU     $FFFF               
F827: FF FF FF        STU     $FFFF               
F82A: FF FF FF        STU     $FFFF               
F82D: FF FF FF        STU     $FFFF               
F830: FF FF FF        STU     $FFFF               
F833: FF FF FF        STU     $FFFF               
F836: FF FF FF        STU     $FFFF               
F839: FF FF FF        STU     $FFFF               
F83C: FF FF FF        STU     $FFFF               
F83F: FF FF FF        STU     $FFFF               
F842: FF FF FF        STU     $FFFF               
F845: FF FF FF        STU     $FFFF               
F848: FF FF FF        STU     $FFFF               
F84B: FF FF FF        STU     $FFFF               
F84E: FF FF FF        STU     $FFFF               
F851: FF FF FF        STU     $FFFF               
F854: FF FF FF        STU     $FFFF               
F857: FF FF FF        STU     $FFFF               
F85A: FF FF FF        STU     $FFFF               
F85D: FF FF FF        STU     $FFFF               
F860: FF FF FF        STU     $FFFF               
F863: FF FF FF        STU     $FFFF               
F866: FF FF FF        STU     $FFFF               
F869: FF FF FF        STU     $FFFF               
F86C: FF FF FF        STU     $FFFF               
F86F: FF FF FF        STU     $FFFF               
F872: FF FF FF        STU     $FFFF               
F875: FF FF FF        STU     $FFFF               
F878: FF FF FF        STU     $FFFF               
F87B: FF FF FF        STU     $FFFF               
F87E: FF FF FF        STU     $FFFF               
F881: FF FF FF        STU     $FFFF               
F884: FF FF FF        STU     $FFFF               
F887: FF FF FF        STU     $FFFF               
F88A: FF FF FF        STU     $FFFF               
F88D: FF FF FF        STU     $FFFF               
F890: FF FF FF        STU     $FFFF               
F893: FF FF FF        STU     $FFFF               
F896: FF FF FF        STU     $FFFF               
F899: FF FF FF        STU     $FFFF               
F89C: FF FF FF        STU     $FFFF               
F89F: FF FF FF        STU     $FFFF               
F8A2: FF FF FF        STU     $FFFF               
F8A5: FF FF FF        STU     $FFFF               
F8A8: FF FF FF        STU     $FFFF               
F8AB: FF FF FF        STU     $FFFF               
F8AE: FF FF FF        STU     $FFFF               
F8B1: FF FF FF        STU     $FFFF               
F8B4: FF FF FF        STU     $FFFF               
F8B7: FF FF FF        STU     $FFFF               
F8BA: FF FF FF        STU     $FFFF               
F8BD: FF FF FF        STU     $FFFF               
F8C0: FF FF FF        STU     $FFFF               
F8C3: FF FF FF        STU     $FFFF               
F8C6: FF FF FF        STU     $FFFF               
F8C9: FF FF FF        STU     $FFFF               
F8CC: FF FF FF        STU     $FFFF               
F8CF: FF FF FF        STU     $FFFF               
F8D2: FF FF FF        STU     $FFFF               
F8D5: FF FF FF        STU     $FFFF               
F8D8: FF FF FF        STU     $FFFF               
F8DB: FF FF FF        STU     $FFFF               
F8DE: FF FF FF        STU     $FFFF               
F8E1: FF FF FF        STU     $FFFF               
F8E4: FF FF FF        STU     $FFFF               
F8E7: FF FF FF        STU     $FFFF               
F8EA: FF FF FF        STU     $FFFF               
F8ED: FF FF FF        STU     $FFFF               
F8F0: FF FF FF        STU     $FFFF               
F8F3: FF FF FF        STU     $FFFF               
F8F6: FF FF FF        STU     $FFFF               
F8F9: FF FF FF        STU     $FFFF               
F8FC: FF FF FF        STU     $FFFF               
F8FF: FF FF FF        STU     $FFFF               
F902: FF FF FF        STU     $FFFF               
F905: FF FF FF        STU     $FFFF               
F908: FF FF FF        STU     $FFFF               
F90B: FF FF FF        STU     $FFFF               
F90E: FF FF FF        STU     $FFFF               
F911: FF FF FF        STU     $FFFF               
F914: FF FF FF        STU     $FFFF               
F917: FF FF FF        STU     $FFFF               
F91A: FF FF FF        STU     $FFFF               
F91D: FF FF FF        STU     $FFFF               
F920: FF FF FF        STU     $FFFF               
F923: FF FF FF        STU     $FFFF               
F926: FF FF FF        STU     $FFFF               
F929: FF FF FF        STU     $FFFF               
F92C: FF FF FF        STU     $FFFF               
F92F: FF FF FF        STU     $FFFF               
F932: FF FF FF        STU     $FFFF               
F935: FF FF FF        STU     $FFFF               
F938: FF FF FF        STU     $FFFF               
F93B: FF FF FF        STU     $FFFF               
F93E: FF FF FF        STU     $FFFF               
F941: FF FF FF        STU     $FFFF               
F944: FF FF FF        STU     $FFFF               
F947: FF FF FF        STU     $FFFF               
F94A: FF FF FF        STU     $FFFF               
F94D: FF FF FF        STU     $FFFF               
F950: FF FF FF        STU     $FFFF               
F953: FF FF FF        STU     $FFFF               
F956: FF FF FF        STU     $FFFF               
F959: FF FF FF        STU     $FFFF               
F95C: FF FF FF        STU     $FFFF               
F95F: FF FF FF        STU     $FFFF               
F962: FF FF FF        STU     $FFFF               
F965: FF FF FF        STU     $FFFF               
F968: FF FF FF        STU     $FFFF               
F96B: FF FF FF        STU     $FFFF               
F96E: FF FF FF        STU     $FFFF               
F971: FF FF FF        STU     $FFFF               
F974: FF FF FF        STU     $FFFF               
F977: FF FF FF        STU     $FFFF               
F97A: FF FF FF        STU     $FFFF               
F97D: FF FF FF        STU     $FFFF               
F980: FF FF FF        STU     $FFFF               
F983: FF FF FF        STU     $FFFF               
F986: FF FF FF        STU     $FFFF               
F989: FF FF FF        STU     $FFFF               
F98C: FF FF FF        STU     $FFFF               
F98F: FF FF FF        STU     $FFFF               
F992: FF FF FF        STU     $FFFF               
F995: FF FF FF        STU     $FFFF               
F998: FF FF FF        STU     $FFFF               
F99B: FF FF FF        STU     $FFFF               
F99E: FF FF FF        STU     $FFFF               
F9A1: FF FF FF        STU     $FFFF               
F9A4: FF FF FF        STU     $FFFF               
F9A7: FF FF FF        STU     $FFFF               
F9AA: FF FF FF        STU     $FFFF               
F9AD: FF FF FF        STU     $FFFF               
F9B0: FF FF FF        STU     $FFFF               
F9B3: FF FF FF        STU     $FFFF               
F9B6: FF FF FF        STU     $FFFF               
F9B9: FF FF FF        STU     $FFFF               
F9BC: FF FF FF        STU     $FFFF               
F9BF: FF FF FF        STU     $FFFF               
F9C2: FF FF FF        STU     $FFFF               
F9C5: FF FF FF        STU     $FFFF               
F9C8: FF FF FF        STU     $FFFF               
F9CB: FF FF FF        STU     $FFFF               
F9CE: FF FF FF        STU     $FFFF               
F9D1: FF FF FF        STU     $FFFF               
F9D4: FF FF FF        STU     $FFFF               
F9D7: FF FF FF        STU     $FFFF               
F9DA: FF FF FF        STU     $FFFF               
F9DD: FF FF FF        STU     $FFFF               
F9E0: FF FF FF        STU     $FFFF               
F9E3: FF FF FF        STU     $FFFF               
F9E6: FF FF FF        STU     $FFFF               
F9E9: FF FF FF        STU     $FFFF               
F9EC: FF FF FF        STU     $FFFF               
F9EF: FF FF FF        STU     $FFFF               
F9F2: FF FF FF        STU     $FFFF               
F9F5: FF FF FF        STU     $FFFF               
F9F8: FF FF FF        STU     $FFFF               
F9FB: FF FF FF        STU     $FFFF               
F9FE: FF FF FF        STU     $FFFF               
FA01: FF FF FF        STU     $FFFF               
FA04: FF FF FF        STU     $FFFF               
FA07: FF FF FF        STU     $FFFF               
FA0A: FF FF FF        STU     $FFFF               
FA0D: FF FF FF        STU     $FFFF               
FA10: FF FF FF        STU     $FFFF               
FA13: FF FF FF        STU     $FFFF               
FA16: FF FF FF        STU     $FFFF               
FA19: FF FF FF        STU     $FFFF               
FA1C: FF FF FF        STU     $FFFF               
FA1F: FF FF FF        STU     $FFFF               
FA22: FF FF FF        STU     $FFFF               
FA25: FF FF FF        STU     $FFFF               
FA28: FF FF FF        STU     $FFFF               
FA2B: FF FF FF        STU     $FFFF               
FA2E: FF FF FF        STU     $FFFF               
FA31: FF FF FF        STU     $FFFF               
FA34: FF FF FF        STU     $FFFF               
FA37: FF FF FF        STU     $FFFF               
FA3A: FF FF FF        STU     $FFFF               
FA3D: FF FF FF        STU     $FFFF               
FA40: FF FF FF        STU     $FFFF               
FA43: FF FF FF        STU     $FFFF               
FA46: FF FF FF        STU     $FFFF               
FA49: FF FF FF        STU     $FFFF               
FA4C: FF FF FF        STU     $FFFF               
FA4F: FF FF FF        STU     $FFFF               
FA52: FF FF FF        STU     $FFFF               
FA55: FF FF FF        STU     $FFFF               
FA58: FF FF FF        STU     $FFFF               
FA5B: FF FF FF        STU     $FFFF               
FA5E: FF FF FF        STU     $FFFF               
FA61: FF FF FF        STU     $FFFF               
FA64: FF FF FF        STU     $FFFF               
FA67: FF FF FF        STU     $FFFF               
FA6A: FF FF FF        STU     $FFFF               
FA6D: FF FF FF        STU     $FFFF               
FA70: FF FF FF        STU     $FFFF               
FA73: FF FF FF        STU     $FFFF               
FA76: FF FF FF        STU     $FFFF               
FA79: FF FF FF        STU     $FFFF               
FA7C: FF FF FF        STU     $FFFF               
FA7F: FF FF FF        STU     $FFFF               
FA82: FF FF FF        STU     $FFFF               
FA85: FF FF FF        STU     $FFFF               
FA88: FF FF FF        STU     $FFFF               
FA8B: FF FF FF        STU     $FFFF               
FA8E: FF FF FF        STU     $FFFF               
FA91: FF FF FF        STU     $FFFF               
FA94: FF FF FF        STU     $FFFF               
FA97: FF FF FF        STU     $FFFF               
FA9A: FF FF FF        STU     $FFFF               
FA9D: FF FF FF        STU     $FFFF               
FAA0: FF FF FF        STU     $FFFF               
FAA3: FF FF FF        STU     $FFFF               
FAA6: FF FF FF        STU     $FFFF               
FAA9: FF FF FF        STU     $FFFF               
FAAC: FF FF FF        STU     $FFFF               
FAAF: FF FF FF        STU     $FFFF               
FAB2: FF FF FF        STU     $FFFF               
FAB5: FF FF FF        STU     $FFFF               
FAB8: FF FF FF        STU     $FFFF               
FABB: FF FF FF        STU     $FFFF               
FABE: FF FF FF        STU     $FFFF               
FAC1: FF FF FF        STU     $FFFF               
FAC4: FF FF FF        STU     $FFFF               
FAC7: FF FF FF        STU     $FFFF               
FACA: FF FF FF        STU     $FFFF               
FACD: FF FF FF        STU     $FFFF               
FAD0: FF FF FF        STU     $FFFF               
FAD3: FF FF FF        STU     $FFFF               
FAD6: FF FF FF        STU     $FFFF               
FAD9: FF FF FF        STU     $FFFF               
FADC: FF FF FF        STU     $FFFF               
FADF: FF FF FF        STU     $FFFF               
FAE2: FF FF FF        STU     $FFFF               
FAE5: FF FF FF        STU     $FFFF               
FAE8: FF FF FF        STU     $FFFF               
FAEB: FF FF FF        STU     $FFFF               
FAEE: FF FF FF        STU     $FFFF               
FAF1: FF FF FF        STU     $FFFF               
FAF4: FF FF FF        STU     $FFFF               
FAF7: FF FF FF        STU     $FFFF               
FAFA: FF FF FF        STU     $FFFF               
FAFD: FF FF FF        STU     $FFFF               
FB00: FF FF FF        STU     $FFFF               
FB03: FF FF FF        STU     $FFFF               
FB06: FF FF FF        STU     $FFFF               
FB09: FF FF FF        STU     $FFFF               
FB0C: FF FF FF        STU     $FFFF               
FB0F: FF FF FF        STU     $FFFF               
FB12: FF FF FF        STU     $FFFF               
FB15: FF FF FF        STU     $FFFF               
FB18: FF FF FF        STU     $FFFF               
FB1B: FF FF FF        STU     $FFFF               
FB1E: FF FF FF        STU     $FFFF               
FB21: FF FF FF        STU     $FFFF               
FB24: FF FF FF        STU     $FFFF               
FB27: FF FF FF        STU     $FFFF               
FB2A: FF FF FF        STU     $FFFF               
FB2D: FF FF FF        STU     $FFFF               
FB30: FF FF FF        STU     $FFFF               
FB33: FF FF FF        STU     $FFFF               
FB36: FF FF FF        STU     $FFFF               
FB39: FF FF FF        STU     $FFFF               
FB3C: FF FF FF        STU     $FFFF               
FB3F: FF FF FF        STU     $FFFF               
FB42: FF FF FF        STU     $FFFF               
FB45: FF FF FF        STU     $FFFF               
FB48: FF FF FF        STU     $FFFF               
FB4B: FF FF FF        STU     $FFFF               
FB4E: FF FF FF        STU     $FFFF               
FB51: FF FF FF        STU     $FFFF               
FB54: FF FF FF        STU     $FFFF               
FB57: FF FF FF        STU     $FFFF               
FB5A: FF FF FF        STU     $FFFF               
FB5D: FF FF FF        STU     $FFFF               
FB60: FF FF FF        STU     $FFFF               
FB63: FF FF FF        STU     $FFFF               
FB66: FF FF FF        STU     $FFFF               
FB69: FF FF FF        STU     $FFFF               
FB6C: FF FF FF        STU     $FFFF               
FB6F: FF FF FF        STU     $FFFF               
FB72: FF FF FF        STU     $FFFF               
FB75: FF FF FF        STU     $FFFF               
FB78: FF FF FF        STU     $FFFF               
FB7B: FF FF FF        STU     $FFFF               
FB7E: FF FF FF        STU     $FFFF               
FB81: FF FF FF        STU     $FFFF               
FB84: FF FF FF        STU     $FFFF               
FB87: FF FF FF        STU     $FFFF               
FB8A: FF FF FF        STU     $FFFF               
FB8D: FF FF FF        STU     $FFFF               
FB90: FF FF FF        STU     $FFFF               
FB93: FF FF FF        STU     $FFFF               
FB96: FF FF FF        STU     $FFFF               
FB99: FF FF FF        STU     $FFFF               
FB9C: FF FF FF        STU     $FFFF               
FB9F: FF FF FF        STU     $FFFF               
FBA2: FF FF FF        STU     $FFFF               
FBA5: FF FF FF        STU     $FFFF               
FBA8: FF FF FF        STU     $FFFF               
FBAB: FF FF FF        STU     $FFFF               
FBAE: FF FF FF        STU     $FFFF               
FBB1: FF FF FF        STU     $FFFF               
FBB4: FF FF FF        STU     $FFFF               
FBB7: FF FF FF        STU     $FFFF               
FBBA: FF FF FF        STU     $FFFF               
FBBD: FF FF FF        STU     $FFFF               
FBC0: FF FF FF        STU     $FFFF               
FBC3: FF FF FF        STU     $FFFF               
FBC6: FF FF FF        STU     $FFFF               
FBC9: FF FF FF        STU     $FFFF               
FBCC: FF FF FF        STU     $FFFF               
FBCF: FF FF FF        STU     $FFFF               
FBD2: FF FF FF        STU     $FFFF               
FBD5: FF FF FF        STU     $FFFF               
FBD8: FF FF FF        STU     $FFFF               
FBDB: FF FF FF        STU     $FFFF               
FBDE: FF FF FF        STU     $FFFF               
FBE1: FF FF FF        STU     $FFFF               
FBE4: FF FF FF        STU     $FFFF               
FBE7: FF FF FF        STU     $FFFF               
FBEA: FF FF FF        STU     $FFFF               
FBED: FF FF FF        STU     $FFFF               
FBF0: FF FF FF        STU     $FFFF               
FBF3: FF FF FF        STU     $FFFF               
FBF6: FF FF FF        STU     $FFFF               
FBF9: FF FF FF        STU     $FFFF               
FBFC: FF FF FF        STU     $FFFF               
FBFF: FF FF FF        STU     $FFFF               
FC02: FF FF FF        STU     $FFFF               
FC05: FF FF FF        STU     $FFFF               
FC08: FF FF FF        STU     $FFFF               
FC0B: FF FF FF        STU     $FFFF               
FC0E: FF FF FF        STU     $FFFF               
FC11: FF FF FF        STU     $FFFF               
FC14: FF FF FF        STU     $FFFF               
FC17: FF FF FF        STU     $FFFF               
FC1A: FF FF FF        STU     $FFFF               
FC1D: FF FF FF        STU     $FFFF               
FC20: FF FF FF        STU     $FFFF               
FC23: FF FF FF        STU     $FFFF               
FC26: FF FF FF        STU     $FFFF               
FC29: FF FF FF        STU     $FFFF               
FC2C: FF FF FF        STU     $FFFF               
FC2F: FF FF FF        STU     $FFFF               
FC32: FF FF FF        STU     $FFFF               
FC35: FF FF FF        STU     $FFFF               
FC38: FF FF FF        STU     $FFFF               
FC3B: FF FF FF        STU     $FFFF               
FC3E: FF FF FF        STU     $FFFF               
FC41: FF FF FF        STU     $FFFF               
FC44: FF FF FF        STU     $FFFF               
FC47: FF FF FF        STU     $FFFF               
FC4A: FF FF FF        STU     $FFFF               
FC4D: FF FF FF        STU     $FFFF               
FC50: FF FF FF        STU     $FFFF               
FC53: FF FF FF        STU     $FFFF               
FC56: FF FF FF        STU     $FFFF               
FC59: FF FF FF        STU     $FFFF               
FC5C: FF FF FF        STU     $FFFF               
FC5F: FF FF FF        STU     $FFFF               
FC62: FF FF FF        STU     $FFFF               
FC65: FF FF FF        STU     $FFFF               
FC68: FF FF FF        STU     $FFFF               
FC6B: FF FF FF        STU     $FFFF               
FC6E: FF FF FF        STU     $FFFF               
FC71: FF FF FF        STU     $FFFF               
FC74: FF FF FF        STU     $FFFF               
FC77: FF FF FF        STU     $FFFF               
FC7A: FF FF FF        STU     $FFFF               
FC7D: FF FF FF        STU     $FFFF               
FC80: FF FF FF        STU     $FFFF               
FC83: FF FF FF        STU     $FFFF               
FC86: FF FF FF        STU     $FFFF               
FC89: FF FF FF        STU     $FFFF               
FC8C: FF FF FF        STU     $FFFF               
FC8F: FF FF FF        STU     $FFFF               
FC92: FF FF FF        STU     $FFFF               
FC95: FF FF FF        STU     $FFFF               
FC98: FF FF FF        STU     $FFFF               
FC9B: FF FF FF        STU     $FFFF               
FC9E: FF FF FF        STU     $FFFF               
FCA1: FF FF FF        STU     $FFFF               
FCA4: FF FF FF        STU     $FFFF               
FCA7: FF FF FF        STU     $FFFF               
FCAA: FF FF FF        STU     $FFFF               
FCAD: FF FF FF        STU     $FFFF               
FCB0: FF FF FF        STU     $FFFF               
FCB3: FF FF FF        STU     $FFFF               
FCB6: FF FF FF        STU     $FFFF               
FCB9: FF FF FF        STU     $FFFF               
FCBC: FF FF FF        STU     $FFFF               
FCBF: FF FF FF        STU     $FFFF               
FCC2: FF FF FF        STU     $FFFF               
FCC5: FF FF FF        STU     $FFFF               
FCC8: FF FF FF        STU     $FFFF               
FCCB: FF FF FF        STU     $FFFF               
FCCE: FF FF FF        STU     $FFFF               
FCD1: FF FF FF        STU     $FFFF               
FCD4: FF FF FF        STU     $FFFF               
FCD7: FF FF FF        STU     $FFFF               
FCDA: FF FF FF        STU     $FFFF               
FCDD: FF FF FF        STU     $FFFF               
FCE0: FF FF FF        STU     $FFFF               
FCE3: FF FF FF        STU     $FFFF               
FCE6: FF FF FF        STU     $FFFF               
FCE9: FF FF FF        STU     $FFFF               
FCEC: FF FF FF        STU     $FFFF               
FCEF: FF FF FF        STU     $FFFF               
FCF2: FF FF FF        STU     $FFFF               
FCF5: FF FF FF        STU     $FFFF               
FCF8: FF FF FF        STU     $FFFF               
FCFB: FF FF FF        STU     $FFFF               
FCFE: FF FF FF        STU     $FFFF               
FD01: FF FF FF        STU     $FFFF               
FD04: FF FF FF        STU     $FFFF               
FD07: FF FF FF        STU     $FFFF               
FD0A: FF FF FF        STU     $FFFF               
FD0D: FF FF FF        STU     $FFFF               
FD10: FF FF FF        STU     $FFFF               
FD13: FF FF FF        STU     $FFFF               
FD16: FF FF FF        STU     $FFFF               
FD19: FF FF FF        STU     $FFFF               
FD1C: FF FF FF        STU     $FFFF               
FD1F: FF FF FF        STU     $FFFF               
FD22: FF FF FF        STU     $FFFF               
FD25: FF FF FF        STU     $FFFF               
FD28: FF FF FF        STU     $FFFF               
FD2B: FF FF FF        STU     $FFFF               
FD2E: FF FF FF        STU     $FFFF               
FD31: FF FF FF        STU     $FFFF               
FD34: FF FF FF        STU     $FFFF               
FD37: FF FF FF        STU     $FFFF               
FD3A: FF FF FF        STU     $FFFF               
FD3D: FF FF FF        STU     $FFFF               
FD40: FF FF FF        STU     $FFFF               
FD43: FF FF FF        STU     $FFFF               
FD46: FF FF FF        STU     $FFFF               
FD49: FF FF FF        STU     $FFFF               
FD4C: FF FF FF        STU     $FFFF               
FD4F: FF FF FF        STU     $FFFF               
FD52: FF FF FF        STU     $FFFF               
FD55: FF FF FF        STU     $FFFF               
FD58: FF FF FF        STU     $FFFF               
FD5B: FF FF FF        STU     $FFFF               
FD5E: FF FF FF        STU     $FFFF               
FD61: FF FF FF        STU     $FFFF               
FD64: FF FF FF        STU     $FFFF               
FD67: FF FF FF        STU     $FFFF               
FD6A: FF FF FF        STU     $FFFF               
FD6D: FF FF FF        STU     $FFFF               
FD70: FF FF FF        STU     $FFFF               
FD73: FF FF FF        STU     $FFFF               
FD76: FF FF FF        STU     $FFFF               
FD79: FF FF FF        STU     $FFFF               
FD7C: FF FF FF        STU     $FFFF               
FD7F: FF FF FF        STU     $FFFF               
FD82: FF FF FF        STU     $FFFF               
FD85: FF FF FF        STU     $FFFF               
FD88: FF FF FF        STU     $FFFF               
FD8B: FF FF FF        STU     $FFFF               
FD8E: FF FF FF        STU     $FFFF               
FD91: FF FF FF        STU     $FFFF               
FD94: FF FF FF        STU     $FFFF               
FD97: FF FF FF        STU     $FFFF               
FD9A: FF FF FF        STU     $FFFF               
FD9D: FF FF FF        STU     $FFFF               
FDA0: FF FF FF        STU     $FFFF               
FDA3: FF FF FF        STU     $FFFF               
FDA6: FF FF FF        STU     $FFFF               
FDA9: FF FF FF        STU     $FFFF               
FDAC: FF FF FF        STU     $FFFF               
FDAF: FF FF FF        STU     $FFFF               
FDB2: FF FF FF        STU     $FFFF               
FDB5: FF FF FF        STU     $FFFF               
FDB8: FF FF FF        STU     $FFFF               
FDBB: FF FF FF        STU     $FFFF               
FDBE: FF FF FF        STU     $FFFF               
FDC1: FF FF FF        STU     $FFFF               
FDC4: FF FF FF        STU     $FFFF               
FDC7: FF FF FF        STU     $FFFF               
FDCA: FF FF FF        STU     $FFFF               
FDCD: FF FF FF        STU     $FFFF               
FDD0: FF FF FF        STU     $FFFF               
FDD3: FF FF FF        STU     $FFFF               
FDD6: FF FF FF        STU     $FFFF               
FDD9: FF FF FF        STU     $FFFF               
FDDC: FF FF FF        STU     $FFFF               
FDDF: FF FF FF        STU     $FFFF               
FDE2: FF FF FF        STU     $FFFF               
FDE5: FF FF FF        STU     $FFFF               
FDE8: FF FF FF        STU     $FFFF               
FDEB: FF FF FF        STU     $FFFF               
FDEE: FF FF FF        STU     $FFFF               
FDF1: FF FF FF        STU     $FFFF               
FDF4: FF FF FF        STU     $FFFF               
FDF7: FF FF FF        STU     $FFFF               
FDFA: FF FF FF        STU     $FFFF               
FDFD: FF FF FF        STU     $FFFF               
FE00: FF FF FF        STU     $FFFF               
FE03: FF FF FF        STU     $FFFF               
FE06: FF FF FF        STU     $FFFF               
FE09: FF FF FF        STU     $FFFF               
FE0C: FF FF FF        STU     $FFFF               
FE0F: FF FF FF        STU     $FFFF               
FE12: FF FF FF        STU     $FFFF               
FE15: FF FF FF        STU     $FFFF               
FE18: FF FF FF        STU     $FFFF               
FE1B: FF FF FF        STU     $FFFF               
FE1E: FF FF FF        STU     $FFFF               
FE21: FF FF FF        STU     $FFFF               
FE24: FF FF FF        STU     $FFFF               
FE27: FF FF FF        STU     $FFFF               
FE2A: FF FF FF        STU     $FFFF               
FE2D: FF FF FF        STU     $FFFF               
FE30: FF FF FF        STU     $FFFF               
FE33: FF FF FF        STU     $FFFF               
FE36: FF FF FF        STU     $FFFF               
FE39: FF FF FF        STU     $FFFF               
FE3C: FF FF FF        STU     $FFFF               
FE3F: FF FF FF        STU     $FFFF               
FE42: FF FF FF        STU     $FFFF               
FE45: FF FF FF        STU     $FFFF               
FE48: FF FF FF        STU     $FFFF               
FE4B: FF FF FF        STU     $FFFF               
FE4E: FF FF FF        STU     $FFFF               
FE51: FF FF FF        STU     $FFFF               
FE54: FF FF FF        STU     $FFFF               
FE57: FF FF FF        STU     $FFFF               
FE5A: FF FF FF        STU     $FFFF               
FE5D: FF FF FF        STU     $FFFF               
FE60: FF FF FF        STU     $FFFF               
FE63: FF FF FF        STU     $FFFF               
FE66: FF FF FF        STU     $FFFF               
FE69: FF FF FF        STU     $FFFF               
FE6C: FF FF FF        STU     $FFFF               
FE6F: FF FF FF        STU     $FFFF               
FE72: FF FF FF        STU     $FFFF               
FE75: FF FF FF        STU     $FFFF               
FE78: FF FF FF        STU     $FFFF               
FE7B: FF FF FF        STU     $FFFF               
FE7E: FF FF FF        STU     $FFFF               
FE81: FF FF FF        STU     $FFFF               
FE84: FF FF FF        STU     $FFFF               
FE87: FF FF FF        STU     $FFFF               
FE8A: FF FF FF        STU     $FFFF               
FE8D: FF FF FF        STU     $FFFF               
FE90: FF FF FF        STU     $FFFF               
FE93: FF FF FF        STU     $FFFF               
FE96: FF FF FF        STU     $FFFF               
FE99: FF FF FF        STU     $FFFF               
FE9C: FF FF FF        STU     $FFFF               
FE9F: FF FF FF        STU     $FFFF               
FEA2: FF FF FF        STU     $FFFF               
FEA5: FF FF FF        STU     $FFFF               
FEA8: FF FF FF        STU     $FFFF               
FEAB: FF FF FF        STU     $FFFF               
FEAE: FF FF FF        STU     $FFFF               
FEB1: FF FF FF        STU     $FFFF               
FEB4: FF FF FF        STU     $FFFF               
FEB7: FF FF FF        STU     $FFFF               
FEBA: FF FF FF        STU     $FFFF               
FEBD: FF FF FF        STU     $FFFF               
FEC0: FF FF FF        STU     $FFFF               
FEC3: FF FF FF        STU     $FFFF               
FEC6: FF FF FF        STU     $FFFF               
FEC9: FF FF FF        STU     $FFFF               
FECC: FF FF FF        STU     $FFFF               
FECF: FF FF FF        STU     $FFFF               
FED2: FF FF FF        STU     $FFFF               
FED5: FF FF FF        STU     $FFFF               
FED8: FF FF FF        STU     $FFFF               
FEDB: FF FF FF        STU     $FFFF               
FEDE: FF FF FF        STU     $FFFF               
FEE1: FF FF FF        STU     $FFFF               
FEE4: FF FF FF        STU     $FFFF               
FEE7: FF FF FF        STU     $FFFF               
FEEA: FF FF FF        STU     $FFFF               
FEED: FF FF FF        STU     $FFFF               
FEF0: FF FF FF        STU     $FFFF               
FEF3: FF FF FF        STU     $FFFF               
FEF6: FF FF FF        STU     $FFFF               
FEF9: FF FF FF        STU     $FFFF               
FEFC: FF FF FF        STU     $FFFF               
FEFF: FF FF FF        STU     $FFFF               
FF02: FF FF FF        STU     $FFFF               
FF05: FF FF FF        STU     $FFFF               
FF08: FF FF FF        STU     $FFFF               
FF0B: FF FF FF        STU     $FFFF               
FF0E: FF FF FF        STU     $FFFF               
FF11: FF FF FF        STU     $FFFF               
FF14: FF FF FF        STU     $FFFF               
FF17: FF FF FF        STU     $FFFF               
FF1A: FF FF FF        STU     $FFFF               
FF1D: FF FF FF        STU     $FFFF               
FF20: FF FF FF        STU     $FFFF               
FF23: FF FF FF        STU     $FFFF               
FF26: FF FF FF        STU     $FFFF               
FF29: FF FF FF        STU     $FFFF               
FF2C: FF FF FF        STU     $FFFF               
FF2F: FF FF FF        STU     $FFFF               
FF32: FF FF FF        STU     $FFFF               
FF35: FF FF FF        STU     $FFFF               
FF38: FF FF FF        STU     $FFFF               
FF3B: FF FF FF        STU     $FFFF               
FF3E: FF FF FF        STU     $FFFF               
FF41: FF FF FF        STU     $FFFF               
FF44: FF FF FF        STU     $FFFF               
FF47: FF FF FF        STU     $FFFF               
FF4A: FF FF FF        STU     $FFFF               
FF4D: FF FF FF        STU     $FFFF               
FF50: FF FF FF        STU     $FFFF               
FF53: FF FF FF        STU     $FFFF               
FF56: FF FF FF        STU     $FFFF               
FF59: FF FF FF        STU     $FFFF               
FF5C: FF FF FF        STU     $FFFF               
FF5F: FF FF FF        STU     $FFFF               
FF62: FF FF FF        STU     $FFFF               
FF65: FF FF FF        STU     $FFFF               
FF68: FF FF FF        STU     $FFFF               
FF6B: FF FF FF        STU     $FFFF               
FF6E: FF FF FF        STU     $FFFF               
FF71: FF FF FF        STU     $FFFF               
FF74: FF FF FF        STU     $FFFF               
FF77: FF FF FF        STU     $FFFF               
FF7A: FF FF FF        STU     $FFFF               
FF7D: FF FF FF        STU     $FFFF               
FF80: FF FF FF        STU     $FFFF               
FF83: FF FF FF        STU     $FFFF               
FF86: FF FF FF        STU     $FFFF               
FF89: FF FF FF        STU     $FFFF               
FF8C: FF FF FF        STU     $FFFF               
FF8F: FF FF FF        STU     $FFFF               
FF92: FF FF FF        STU     $FFFF               
FF95: FF FF FF        STU     $FFFF               
FF98: FF FF FF        STU     $FFFF               
FF9B: FF FF FF        STU     $FFFF               
FF9E: FF FF FF        STU     $FFFF               
FFA1: FF FF FF        STU     $FFFF               
FFA4: FF FF FF        STU     $FFFF               
FFA7: FF FF FF        STU     $FFFF               
FFAA: FF FF FF        STU     $FFFF               
FFAD: FF FF FF        STU     $FFFF               
FFB0: FF FF FF        STU     $FFFF               
FFB3: FF FF FF        STU     $FFFF               
FFB6: FF FF FF        STU     $FFFF               
FFB9: FF FF FF        STU     $FFFF               
FFBC: FF FF FF        STU     $FFFF               
FFBF: FF FF FF        STU     $FFFF               
FFC2: FF FF FF        STU     $FFFF               
FFC5: FF FF FF        STU     $FFFF               
FFC8: FF FF FF        STU     $FFFF               
FFCB: FF FF FF        STU     $FFFF               
FFCE: FF FF FF        STU     $FFFF               
FFD1: FF FF FF        STU     $FFFF               
FFD4: FF FF FF        STU     $FFFF               
FFD7: FF FF FF        STU     $FFFF               
FFDA: FF FF FF        STU     $FFFF               
FFDD: FF FF FF        STU     $FFFF               
FFE0: FF FF FF        STU     $FFFF               
FFE3: FF FF FF        STU     $FFFF               
FFE6: FF FF FF        STU     $FFFF               
FFE9: FF FF FF        STU     $FFFF               
FFEC: FF FF FF        STU     $FFFF               
FFEF: FF FF FF        STU     $FFFF               
FFF2: FF FF FF        STU     $FFFF               
FFF5: FF FF FF        STU     $FFFF               
FFF8: E4 38           ANDB    -8,Y                
FFFA: FF FF FF        STU     $FFFF               
FFFD: FF E0 00        STU     $E000               ; {}
```code      

