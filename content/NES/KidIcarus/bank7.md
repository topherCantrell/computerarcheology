![Bank 7](KidIcarus.jpg)

# Bank 7

>>> cpu 6502

>>> binary C000:roms/KidIcarus.nes[1C010:20010]

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](Hardware.md)

```code
C000: 78              SEI                         
C001: D8              CLD                         
C002: A9 00           LDA     #$00                
C004: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
C007: 8D 01 20        STA     $2001               ; {hard.P_CNTRL_2}
C00A: 8D 00 01        STA     $0100               
C00D: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
C010: 10 FB           BPL     $C00D               ; {}
C012: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
C015: 10 FB           BPL     $C012               ; {}
C017: A2 FF           LDX     #$FF                
C019: 9A              TXS                         
C01A: A9 03           LDA     #$03                
C01C: 8D FA 6F        STA     $6FFA               
C01F: A9 7F           LDA     #$7F                
C021: 8D FB 6F        STA     $6FFB               
C024: 20 07 EB        JSR     $EB07               ; {}
C027: A2 00           LDX     #$00                
C029: BD 81 F0        LDA     $F081,X             ; {}
C02C: 9D 00 60        STA     $6000,X             
C02F: E8              INX                         
C030: D0 F7           BNE     $C029               ; {}
C032: A9 00           LDA     #$00                
C034: AA              TAX                         
C035: 9D 00 01        STA     $0100,X             
C038: 9D 00 02        STA     $0200,X             
C03B: 9D 00 03        STA     $0300,X             
C03E: 9D 00 04        STA     $0400,X             
C041: 9D 00 05        STA     $0500,X             
C044: 9D 00 06        STA     $0600,X             
C047: 9D 00 07        STA     $0700,X             
C04A: E8              INX                         
C04B: D0 E8           BNE     $C035               ; {}
C04D: A9 F0           LDA     #$F0                
C04F: 20 3D C2        JSR     $C23D               ; {}
C052: A2 F2           LDX     #$F2                
C054: 95 00           STA     $00,X               ; {ram.GP_00}
C056: E8              INX                         
C057: E0 FA           CPX     #$FA                
C059: 90 F9           BCC     $C054               ; {}
C05B: 85 AD           STA     $AD                 
C05D: 85 AE           STA     $AE                 
C05F: 85 70           STA     $70                 
C061: 85 72           STA     $72                 
C063: 85 73           STA     $73                 
C065: 85 A2           STA     $A2                 
C067: 20 46 C8        JSR     $C846               ; {}
C06A: 20 6A EE        JSR     $EE6A               ; {}
C06D: A9 00           LDA     #$00                
C06F: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
C072: 8D 01 20        STA     $2001               ; {hard.P_CNTRL_2}
C075: 8D 00 01        STA     $0100               
C078: A5 38           LDA     $38                 
C07A: 30 11           BMI     $C08D               ; {}
C07C: 29 0F           AND     #$0F                
C07E: F0 03           BEQ     $C083               ; {}
C080: 4C D4 C1        JMP     $C1D4               ; {}
C083: A5 A0           LDA     $A0                 
C085: 20 C9 C0        JSR     $C0C9               ; {}
C088: A9 A0           LDA     #$A0                
C08A: 20 3D C2        JSR     $C23D               ; {}
C08D: A5 A0           LDA     $A0                 
C08F: C9 09           CMP     #$09                
C091: F0 03           BEQ     $C096               ; {}
C093: 20 31 C3        JSR     $C331               ; {}
C096: 20 4A C2        JSR     $C24A               ; {}
C099: A9 00           LDA     #$00                
C09B: 85 38           STA     $38                 
C09D: 4C 00 7F        JMP     $7F00               
C0A0: A5 A0           LDA     $A0                 
C0A2: 85 AC           STA     $AC                 
C0A4: A9 01           LDA     #$01                
C0A6: 85 37           STA     $37                 
C0A8: A9 00           LDA     #$00                
C0AA: 85 14           STA     $14                 
C0AC: 85 15           STA     $15                 
C0AE: A9 80           LDA     #$80                
C0B0: 8D 84 03        STA     $0384               
C0B3: A5 14           LDA     $14                 
C0B5: C9 60           CMP     #$60                
C0B7: 90 FA           BCC     $C0B3               ; {}
C0B9: 20 F0 EE        JSR     $EEF0               ; {}
C0BC: 20 50 C4        JSR     $C450               ; {}
C0BF: 20 4B C4        JSR     $C44B               ; {}
C0C2: A9 03           LDA     #$03                
C0C4: 85 38           STA     $38                 
C0C6: 4C 6D C0        JMP     $C06D               ; {}
C0C9: A9 00           LDA     #$00                
C0CB: A8              TAY                         
C0CC: 85 00           STA     $00                 ; {ram.GP_00}
C0CE: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
C0D1: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
C0D4: 20 7F C1        JSR     $C17F               ; {}
C0D7: A5 A0           LDA     $A0                 
C0D9: D0 0B           BNE     $C0E6               ; {}
C0DB: A9 A0           LDA     #$A0                
C0DD: 85 01           STA     $01                 
C0DF: A2 20           LDX     #$20                
C0E1: 20 70 C1        JSR     $C170               ; {}
C0E4: F0 3A           BEQ     $C120               ; {}
C0E6: A9 80           LDA     #$80                
C0E8: 85 01           STA     $01                 
C0EA: A2 20           LDX     #$20                
C0EC: 20 70 C1        JSR     $C170               ; {}
C0EF: A5 A0           LDA     $A0                 
C0F1: AA              TAX                         
C0F2: BD 52 C1        LDA     $C152,X             ; {}
C0F5: C9 80           CMP     #$80                
C0F7: F0 27           BEQ     $C120               ; {}
C0F9: 29 BF           AND     #$BF                
C0FB: 85 01           STA     $01                 
C0FD: A9 01           LDA     #$01                
C0FF: 20 7F C1        JSR     $C17F               ; {}
C102: A9 0C           LDA     #$0C                
C104: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
C107: A9 00           LDA     #$00                
C109: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
C10C: A2 04           LDX     #$04                
C10E: 20 70 C1        JSR     $C170               ; {}
C111: A9 1C           LDA     #$1C                
C113: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
C116: A9 00           LDA     #$00                
C118: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
C11B: A2 04           LDX     #$04                
C11D: 20 70 C1        JSR     $C170               ; {}
C120: A5 A0           LDA     $A0                 
C122: 0A              ASL     A                   
C123: A8              TAY                         
C124: B9 5C C1        LDA     $C15C,Y             ; {}
C127: 85 00           STA     $00                 ; {ram.GP_00}
C129: B9 5D C1        LDA     $C15D,Y             ; {}
C12C: 85 01           STA     $01                 
C12E: A0 00           LDY     #$00                
C130: B1 00           LDA     ($00),Y             ; {ram.GP_00}
C132: 85 BE           STA     $BE                 
C134: 20 7F C1        JSR     $C17F               ; {}
C137: C8              INY                         
C138: B1 00           LDA     ($00),Y             ; {ram.GP_00}
C13A: 48              PHA                         
C13B: C8              INY                         
C13C: B1 00           LDA     ($00),Y             ; {ram.GP_00}
C13E: 85 01           STA     $01                 
C140: 68              PLA                         
C141: 85 00           STA     $00                 ; {ram.GP_00}
C143: A0 59           LDY     #$59                
C145: B1 00           LDA     ($00),Y             ; {ram.GP_00}
C147: 99 00 7F        STA     $7F00,Y             
C14A: 88              DEY                         
C14B: 10 F8           BPL     $C145               ; {}
C14D: A9 10           LDA     #$10                
C14F: 4C 90 CA        JMP     $CA90               ; {}
C152: A0 80           LDY     #$80                
C154: C0 C0           CPY     #$C0                
C156: C8              INY                         
C157: C8              INY                         
C158: D0 D0           BNE     $C12A               ; {}
C15A: D8              CLD                         
C15B: 80 ; ????
C15C: A8              TAY                         
C15D: C1 AB           CMP     ($AB,X)             
C15F: C1 AE           CMP     ($AE,X)             
C161: C1 B1           CMP     ($B1,X)             
C163: C1 B4           CMP     ($B4,X)             
C165: C1 B7           CMP     ($B7,X)             
C167: C1 BA           CMP     ($BA,X)             
C169: C1 BD           CMP     ($BD,X)             
C16B: C1 C0           CMP     ($C0,X)             
C16D: C1 C3           CMP     ($C3,X)             
C16F: C1 B1           CMP     ($B1,X)             
C171: 00              BRK                         
C172: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
C175: E6 00           INC     $00                 ; {ram.GP_00}
C177: D0 F7           BNE     $C170               ; {}
C179: E6 01           INC     $01                 
C17B: CA              DEX                         
C17C: D0 F2           BNE     $C170               ; {}
C17E: 60              RTS                         

C17F: 48              PHA                         
C180: AD 00 01        LDA     $0100               
C183: 29 7F           AND     #$7F                
C185: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
C188: 68              PLA                         
C189: 85 B6           STA     $B6                 
C18B: 8D FF FF        STA     $FFFF               ; 
C18E: 4A              LSR     A                   
C18F: 8D FF FF        STA     $FFFF               ; 
C192: 4A              LSR     A                   
C193: 8D FF FF        STA     $FFFF               ; 
C196: 4A              LSR     A                   
C197: 8D FF FF        STA     $FFFF               ; 
C19A: 4A              LSR     A                   
C19B: 8D FF FF        STA     $FFFF               ; 
C19E: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
C1A1: AD 00 01        LDA     $0100               
C1A4: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
C1A7: 60              RTS                         

C1A8: 01 00           ORA     ($00,X)             ; {ram.GP_00}
C1AA: A0 01           LDY     #$01                
C1AC: 00              BRK                         
C1AD: A0 02           LDY     #$02                
C1AF: 00              BRK                         
C1B0: 80 ; ????
C1B1: 05 00           ORA     $00                 ; {ram.GP_00}
C1B3: 80 ; ????
C1B4: 02 ; ????
C1B5: A0 99           LDY     #$99                
C1B7: 05 00           ORA     $00                 ; {ram.GP_00}
C1B9: 80 ; ????
C1BA: 03 ; ????
C1BB: 00              BRK                         
C1BC: 80 ; ????
C1BD: 05 00           ORA     $00                 ; {ram.GP_00}
C1BF: 80 ; ????
C1C0: 03 ; ????
C1C1: 30 9C           BMI     $C15F               ; {}
C1C3: 04 ; ????
C1C4: 00              BRK                         
C1C5: 80 ; ????
C1C6: A0 00           LDY     #$00                
C1C8: A6 AF           LDX     $AF                 
C1CA: F0 07           BEQ     $C1D3               ; {}
C1CC: A0 27           LDY     #$27                
C1CE: CA              DEX                         
C1CF: F0 02           BEQ     $C1D3               ; {}
C1D1: A0 4E           LDY     #$4E                
C1D3: 60              RTS                         
C1D4: 20 F0 EE        JSR     $EEF0               ; {}
C1D7: A9 10           LDA     #$10                
C1D9: 8D 00 01        STA     $0100               
C1DC: 20 6F C2        JSR     $C26F               ; {}
C1DF: A5 38           LDA     $38                 
C1E1: 20 A0 C2        JSR     $C2A0               ; {}
C1E4: A5 38           LDA     $38                 
C1E6: C9 04           CMP     #$04                
C1E8: D0 00           BNE     $C1EA               ; {}
C1EA: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
C1ED: 10 FB           BPL     $C1EA               ; {}
C1EF: 20 42 EE        JSR     $EE42               ; {}
C1F2: 20 2E EB        JSR     $EB2E               ; {}
C1F5: 20 01 EF        JSR     $EF01               ; {}
C1F8: A5 A3           LDA     $A3                 
C1FA: D0 FC           BNE     $C1F8               ; {}
C1FC: A9 10           LDA     #$10                
C1FE: 8D 00 01        STA     $0100               
C201: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
C204: A9 03           LDA     #$03                
C206: 8D FA 6F        STA     $6FFA               
C209: A9 7F           LDA     #$7F                
C20B: 8D FB 6F        STA     $6FFB               
C20E: 4C 6D C0        JMP     $C06D               ; {}
C211: 48              PHA                         
C212: 20 4A C2        JSR     $C24A               ; {}
C215: 20 F0 EE        JSR     $EEF0               ; {}
C218: 68              PLA                         
C219: 48              PHA                         
C21A: 29 F0           AND     #$F0                
C21C: 4A              LSR     A                   
C21D: 4A              LSR     A                   
C21E: 4A              LSR     A                   
C21F: 4A              LSR     A                   
C220: 8D 10 07        STA     $0710               
C223: 68              PLA                         
C224: 29 0F           AND     #$0F                
C226: 8D 11 07        STA     $0711               
C229: A2 00           LDX     #$00                
C22B: BD 2D C3        LDA     $C32D,X             ; {}
C22E: 9D 0C 07        STA     $070C,X             
C231: E8              INX                         
C232: E0 04           CPX     #$04                
C234: D0 F5           BNE     $C22B               ; {}
C236: A9 05           LDA     #$05                
C238: 85 38           STA     $38                 
C23A: 4C 6D C0        JMP     $C06D               ; {}
C23D: 85 F1           STA     $F1                 
C23F: A2 00           LDX     #$00                
C241: 8A              TXA                         
C242: 95 00           STA     $00,X               ; {ram.GP_00}
C244: E8              INX                         
C245: E4 F1           CPX     $F1                 
C247: 90 F9           BCC     $C242               ; {}
C249: 60              RTS                         
C24A: A9 10           LDA     #$10                
C24C: 8D 00 01        STA     $0100               
C24F: A9 1E           LDA     #$1E                
C251: 85 FF           STA     $FF                 
C253: 60              RTS                         
C254: 85 00           STA     $00                 ; {ram.GP_00}
C256: C6 00           DEC     $00                 ; {ram.GP_00}
C258: A5 00           LDA     $00                 ; {ram.GP_00}
C25A: 0A              ASL     A                   
C25B: 0A              ASL     A                   
C25C: 18              CLC                         
C25D: 65 00           ADC     $00                 ; {ram.GP_00}
C25F: AA              TAX                         
C260: A0 00           LDY     #$00                
C262: BD EA C2        LDA     $C2EA,X             ; {}
C265: 99 41 00        STA     $0041,Y             
C268: E8              INX                         
C269: C8              INY                         
C26A: C0 05           CPY     #$05                
C26C: D0 F4           BNE     $C262               ; {}
C26E: 60              RTS                         
C26F: A2 00           LDX     #$00                
C271: A9 39           LDA     #$39                
C273: 8D FA 6F        STA     $6FFA               
C276: A9 C3           LDA     #$C3                
C278: 8D FB 6F        STA     $6FFB               
C27B: A9 FF           LDA     #$FF                
C27D: 85 A3           STA     $A3                 
C27F: 20 73 EF        JSR     $EF73               ; {}
C282: 20 F9 E3        JSR     $E3F9               ; {}
C285: 20 CD C2        JSR     $C2CD               ; {}
C288: 20 E5 EE        JSR     $EEE5               ; {}
C28B: A9 00           LDA     #$00                
C28D: 85 82           STA     $82                 
C28F: 85 14           STA     $14                 
C291: 85 15           STA     $15                 
C293: 85 18           STA     $18                 
C295: E6 1A           INC     $1A                 
C297: A5 38           LDA     $38                 
C299: C9 03           CMP     #$03                
C29B: F0 D1           BEQ     $C26E               ; {}
C29D: 4C 31 C3        JMP     $C331               ; {}
C2A0: 20 54 C2        JSR     $C254               ; {}
C2A3: 20 B3 C2        JSR     $C2B3               ; {}
C2A6: A5 38           LDA     $38                 
C2A8: C9 04           CMP     #$04                
C2AA: D0 20           BNE     $C2CC               ; {}
C2AC: 20 8A C3        JSR     $C38A               ; {}
C2AF: 20 A1 C8        JSR     $C8A1               ; {}
C2B2: 60              RTS                         
C2B3: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
C2B6: A5 42           LDA     $42                 
C2B8: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
C2BB: A5 41           LDA     $41                 
C2BD: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
C2C0: A0 00           LDY     #$00                
C2C2: B1 43           LDA     ($43),Y             
C2C4: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
C2C7: C8              INY                         
C2C8: C4 45           CPY     $45                 
C2CA: D0 F6           BNE     $C2C2               ; {}
C2CC: 60              RTS                         
C2CD: A0 00           LDY     #$00                
C2CF: A2 04           LDX     #$04                
C2D1: B9 E2 C2        LDA     $C2E2,Y             ; {}
C2D4: 99 90 03        STA     $0390,Y             
C2D7: B9 E6 C2        LDA     $C2E6,Y             ; {}
C2DA: 99 A0 03        STA     $03A0,Y             
C2DD: C8              INY                         
C2DE: CA              DEX                         
C2DF: D0 F0           BNE     $C2D1               ; {}
C2E1: 60              RTS                         
C2E2: 0F ; ????
C2E3: 30 2C           BMI     $C311               ; {}
C2E5: 30 0F           BMI     $C2F6               ; {}
C2E7: 27 ; ????
C2E8: 26 06           ROL     $06                 
C2EA: E8              INX                         
C2EB: 21 00           AND     ($00,X)             ; {ram.GP_00}
C2ED: 00              BRK                         
C2EE: 0F ; ????
C2EF: E8              INX                         
C2F0: 21 00           AND     ($00,X)             ; {ram.GP_00}
C2F2: 00              BRK                         
C2F3: 0F ; ????
C2F4: EA              NOP                         
C2F5: 21 0D           AND     ($0D,X)             
C2F7: C3 ; ????
C2F8: 0D AA 21        ORA     $21AA               
C2FB: 1A ; ????
C2FC: C3 ; ????
C2FD: 0C ; ????
C2FE: ED 21 0C        SBC     $0C21               
C301: 07 ; ????
C302: 06 CC           ASL     $CC                 
C304: 21 00           AND     ($00,X)             ; {ram.GP_00}
C306: 00              BRK                         
C307: 08              PHP                         
C308: 2B ; ????
C309: 22 ; ????
C30A: 26 C3           ROL     $C3                 
C30C: 07 ; ????
C30D: 1E 10 22        ASL     $2210,X             
C310: 12 ; ????
C311: 1B ; ????
C312: 1E 23 1E        ASL     $1E23,X             
C315: 28              PLP                         
C316: 1D 1A 19        ORA     $191A,X             
C319: 0E 28 16        ASL     $1628               
C31C: 18              CLC                         
C31D: 27 ; ????
C31E: 1A ; ????
C31F: 19 12 2C        ORA     $2C12,Y             
C322: 24 27           BIT     $27                 
C324: 19 28 23        ORA     $2328,Y             
C327: 0F ; ????
C328: 31 10           AND     ($10),Y             
C32A: 12 ; ????
C32B: 22 ; ????
C32C: 3E 1A 27        ROL     $271A,X             
C32F: 27 ; ????
C330: 0D A9 01        ORA     $01A9               
C333: 8D 80 03        STA     $0380               
C336: 4C 56 C8        JMP     $C856               ; {}
C339: 8A              TXA                         
C33A: 48              PHA                         
C33B: 98              TYA                         
C33C: 48              PHA                         
C33D: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
C340: 20 2E EB        JSR     $EB2E               ; {}
C343: 20 42 EE        JSR     $EE42               ; {}
C346: 20 57 C3        JSR     $C357               ; {}
C349: 20 6A EE        JSR     $EE6A               ; {}
C34C: 20 94 EE        JSR     $EE94               ; {}
C34F: 20 56 C8        JSR     $C856               ; {}
C352: 68              PLA                         
C353: A8              TAY                         
C354: 68              PLA                         
C355: AA              TAX                         
C356: 60              RTS                         
C357: A5 38           LDA     $38                 
C359: 20 2B EE        JSR     $EE2B               ; {}
C35C: 7E C3 7E        ROR     $7EC3,X             
C35F: C3 ; ????
C360: 7E C3 6A        ROR     $6AC3,X             
C363: C3 ; ????
C364: 7F ; ????
C365: C3 ; ????
C366: 7E C3 7E        ROR     $7EC3,X             
C369: C3 ; ????
C36A: A5 14           LDA     $14                 
C36C: C9 80           CMP     #$80                
C36E: 90 0E           BCC     $C37E               ; {}
C370: E6 AD           INC     $AD                 
C372: D0 02           BNE     $C376               ; {}
C374: E6 AE           INC     $AE                 
C376: A9 04           LDA     #$04                
C378: 85 38           STA     $38                 
C37A: A9 00           LDA     #$00                
C37C: 85 A3           STA     $A3                 
C37E: 60              RTS                         
C37F: A5 18           LDA     $18                 
C381: 29 10           AND     #$10                
C383: F0 F9           BEQ     $C37E               ; {}
C385: A9 00           LDA     #$00                
C387: 4C 78 C3        JMP     $C378               ; {}
C38A: 20 C6 C1        JSR     $C1C6               ; {}
C38D: A5 A0           LDA     $A0                 
C38F: 99 28 60        STA     $6028,Y             
C392: A5 AB           LDA     $AB                 
C394: 6A              ROR     A                   
C395: B0 27           BCS     $C3BE               ; {}
C397: E6 AB           INC     $AB                 
C399: AD 30 01        LDA     $0130               
C39C: 99 29 60        STA     $6029,Y             
C39F: A6 AC           LDX     $AC                 
C3A1: 24 AB           BIT     $AB                 
C3A3: 70 07           BVS     $C3AC               ; {}
C3A5: A9 00           LDA     #$00                
C3A7: 99 29 60        STA     $6029,Y             
C3AA: A2 02           LDX     #$02                
C3AC: 8A              TXA                         
C3AD: 99 28 60        STA     $6028,Y             
C3B0: A2 00           LDX     #$00                
C3B2: BD 57 01        LDA     $0157,X             
C3B5: 99 0D 60        STA     $600D,Y             
C3B8: C8              INY                         
C3B9: E8              INX                         
C3BA: E0 1B           CPX     #$1B                
C3BC: D0 F4           BNE     $C3B2               ; {}
C3BE: 60              RTS                         
C3BF: A9 90           LDA     #$90                
C3C1: 9D 01 07        STA     $0701,X             
C3C4: A9 00           LDA     #$00                
C3C6: 9D 04 07        STA     $0704,X             
C3C9: A9 00           LDA     #$00                
C3CB: 9D 08 07        STA     $0708,X             
C3CE: 85 1C           STA     $1C                 
C3D0: 85 1D           STA     $1D                 
C3D2: 85 1E           STA     $1E                 
C3D4: 85 1F           STA     $1F                 
C3D6: 85 3E           STA     $3E                 
C3D8: 60              RTS                         
C3D9: A2 20           LDX     #$20                
C3DB: A9 14           LDA     #$14                
C3DD: 4C E0 DC        JMP     $DCE0               ; {}
C3E0: AD 52 01        LDA     $0152               
C3E3: 29 07           AND     #$07                
C3E5: C9 05           CMP     #$05                
C3E7: 90 0C           BCC     $C3F5               ; {}
C3E9: AD 52 01        LDA     $0152               
C3EC: 29 F8           AND     #$F8                
C3EE: 09 04           ORA     #$04                
C3F0: 8D 52 01        STA     $0152               
C3F3: 29 07           AND     #$07                
C3F5: 0A              ASL     A                   
C3F6: A8              TAY                         
C3F7: B9 09 C4        LDA     $C409,Y             ; {}
C3FA: 8D A1 03        STA     $03A1               
C3FD: A9 26           LDA     #$26                
C3FF: 8D A2 03        STA     $03A2               
C402: B9 0A C4        LDA     $C40A,Y             ; {}
C405: 8D A3 03        STA     $03A3               
C408: 60              RTS                         
C409: 20 07 39        JSR     $3907               
C40C: 0A              ASL     A                   
C40D: 32 ; ????
C40E: 13 ; ????
C40F: 34 ; ????
C410: 05 3C           ORA     $3C                 
C412: 11 A9           ORA     ($A9),Y             
C414: 00              BRK                         
C415: 8D 2F 01        STA     $012F               
C418: 85 36           STA     $36                 
C41A: 8D 4A 01        STA     $014A               
C41D: 8D 4B 01        STA     $014B               
C420: 85 A5           STA     $A5                 
C422: A9 00           LDA     #$00                
C424: 8D 30 01        STA     $0130               
C427: 4C 4B C4        JMP     $C44B               ; {}
C42A: A9 00           LDA     #$00                
C42C: 85 AB           STA     $AB                 
C42E: 85 14           STA     $14                 
C430: 85 15           STA     $15                 
C432: 85 37           STA     $37                 
C434: 85 3A           STA     $3A                 
C436: 85 3F           STA     $3F                 
C438: 85 40           STA     $40                 
C43A: 85 41           STA     $41                 
C43C: 85 42           STA     $42                 
C43E: 85 45           STA     $45                 
C440: 85 5C           STA     $5C                 
C442: 85 19           STA     $19                 
C444: 85 A5           STA     $A5                 
C446: 85 A7           STA     $A7                 
C448: 85 72           STA     $72                 
C44A: 60              RTS                         
C44B: A9 0F           LDA     #$0F                
C44D: 85 A6           STA     $A6                 
C44F: 60              RTS                         
C450: 4C A2 EA        JMP     $EAA2               ; {}
C453: A0 00           LDY     #$00                
C455: 20 6D C4        JSR     $C46D               ; {}
C458: C8              INY                         
C459: 20 6D C4        JSR     $C46D               ; {}
C45C: C8              INY                         
C45D: 20 6D C4        JSR     $C46D               ; {}
C460: A0 00           LDY     #$00                
C462: 20 86 C4        JSR     $C486               ; {}
C465: C8              INY                         
C466: 20 86 C4        JSR     $C486               ; {}
C469: C8              INY                         
C46A: 4C 86 C4        JMP     $C486               ; {}
C46D: B9 3E 01        LDA     $013E,Y             
C470: 30 0C           BMI     $C47E               ; {}
C472: 29 02           AND     #$02                
C474: F0 08           BEQ     $C47E               ; {}
C476: A5 A5           LDA     $A5                 
C478: 19 C4 C4        ORA     $C4C4,Y             ; {}
C47B: 85 A5           STA     $A5                 
C47D: 60              RTS                         
C47E: A5 A5           LDA     $A5                 
C480: 39 C7 C4        AND     $C4C7,Y             ; {}
C483: 85 A5           STA     $A5                 
C485: 60              RTS                         
C486: A5 A6           LDA     $A6                 
C488: D9 CA C4        CMP     $C4CA,Y             ; {}
C48B: B0 16           BCS     $C4A3               ; {}
C48D: A5 AA           LDA     $AA                 
C48F: D0 23           BNE     $C4B4               ; {}
C491: 20 B5 C4        JSR     $C4B5               ; {}
C494: F0 1E           BEQ     $C4B4               ; {}
C496: AA              TAX                         
C497: CA              DEX                         
C498: BD 3E 01        LDA     $013E,X             
C49B: 29 80           AND     #$80                
C49D: 09 01           ORA     #$01                
C49F: 9D 3E 01        STA     $013E,X             
C4A2: 60              RTS                         
C4A3: 20 B5 C4        JSR     $C4B5               ; {}
C4A6: F0 0C           BEQ     $C4B4               ; {}
C4A8: AA              TAX                         
C4A9: CA              DEX                         
C4AA: BD 3E 01        LDA     $013E,X             
C4AD: 29 80           AND     #$80                
C4AF: 09 02           ORA     #$02                
C4B1: 9D 3E 01        STA     $013E,X             
C4B4: 60              RTS                         
C4B5: B9 41 01        LDA     $0141,Y             
C4B8: 10 07           BPL     $C4C1               ; {}
C4BA: 29 30           AND     #$30                
C4BC: 4A              LSR     A                   
C4BD: 4A              LSR     A                   
C4BE: 4A              LSR     A                   
C4BF: 4A              LSR     A                   
C4C0: 60              RTS                         
C4C1: 29 03           AND     #$03                
C4C3: 60              RTS                         
C4C4: 01 02           ORA     ($02,X)             
C4C6: 04 ; ????
C4C7: FE FD FB        INC     $FBFD,X             ; {}
C4CA: 0F ; ????
C4CB: 17 ; ????
C4CC: 1F ; ????
C4CD: 10 03           BPL     $C4D2               ; {}
C4CF: 4C 67 C6        JMP     $C667               ; {}
C4D2: 20 29 C5        JSR     $C529               ; {}
C4D5: BD 00 07        LDA     $0700,X             
C4D8: 85 01           STA     $01                 
C4DA: BD 03 07        LDA     $0703,X             
C4DD: 85 02           STA     $02                 
C4DF: E0 20           CPX     #$20                
C4E1: D0 0B           BNE     $C4EE               ; {}
C4E3: BD 02 07        LDA     $0702,X             
C4E6: 10 06           BPL     $C4EE               ; {}
C4E8: A5 03           LDA     $03                 
C4EA: 09 20           ORA     #$20                
C4EC: 85 03           STA     $03                 
C4EE: C8              INY                         
C4EF: 8A              TXA                         
C4F0: 48              PHA                         
C4F1: 98              TYA                         
C4F2: 48              PHA                         
C4F3: A5 00           LDA     $00                 ; {ram.GP_00}
C4F5: 0A              ASL     A                   
C4F6: A8              TAY                         
C4F7: B9 31 C7        LDA     $C731,Y             ; {}
C4FA: 85 04           STA     $04                 
C4FC: B9 32 C7        LDA     $C732,Y             ; {}
C4FF: 85 05           STA     $05                 
C501: 68              PLA                         
C502: A8              TAY                         
C503: A5 01           LDA     $01                 
C505: 18              CLC                         
C506: 65 04           ADC     $04                 
C508: 9D 00 02        STA     $0200,X             
C50B: E8              INX                         
C50C: B1 06           LDA     ($06),Y             
C50E: 9D 00 02        STA     $0200,X             
C511: C8              INY                         
C512: E8              INX                         
C513: A5 03           LDA     $03                 
C515: 9D 00 02        STA     $0200,X             
C518: E8              INX                         
C519: A5 02           LDA     $02                 
C51B: 18              CLC                         
C51C: 65 05           ADC     $05                 
C51E: 9D 00 02        STA     $0200,X             
C521: E8              INX                         
C522: C6 00           DEC     $00                 ; {ram.GP_00}
C524: 10 CB           BPL     $C4F1               ; {}
C526: 68              PLA                         
C527: AA              TAX                         
C528: 60              RTS                         
C529: 48              PHA                         
C52A: 4A              LSR     A                   
C52B: 4A              LSR     A                   
C52C: 4A              LSR     A                   
C52D: 4A              LSR     A                   
C52E: 0A              ASL     A                   
C52F: A8              TAY                         
C530: B9 42 7F        LDA     $7F42,Y             
C533: 85 06           STA     $06                 
C535: B9 43 7F        LDA     $7F43,Y             
C538: 85 07           STA     $07                 
C53A: B9 21 C7        LDA     $C721,Y             ; {}
C53D: 85 00           STA     $00                 ; {ram.GP_00}
C53F: B9 22 C7        LDA     $C722,Y             ; {}
C542: C9 F0           CMP     #$F0                
C544: B0 15           BCS     $C55B               ; {}
C546: 85 03           STA     $03                 
C548: 68              PLA                         
C549: 48              PHA                         
C54A: 4A              LSR     A                   
C54B: 90 06           BCC     $C553               ; {}
C54D: A5 03           LDA     $03                 
C54F: 09 40           ORA     #$40                
C551: 85 03           STA     $03                 
C553: 68              PLA                         
C554: 29 0F           AND     #$0F                
C556: 0A              ASL     A                   
C557: 0A              ASL     A                   
C558: A8              TAY                         
C559: 88              DEY                         
C55A: 60              RTS                         
C55B: 68              PLA                         
C55C: 29 0F           AND     #$0F                
C55E: 0A              ASL     A                   
C55F: 0A              ASL     A                   
C560: 0A              ASL     A                   
C561: A8              TAY                         
C562: B1 06           LDA     ($06),Y             
C564: 85 03           STA     $03                 
C566: 60              RTS                         
C567: 00              BRK                         
C568: 00              BRK                         
C569: 01 10           ORA     ($10,X)             
C56B: 11 20           ORA     ($20),Y             
C56D: 21 00           AND     ($00,X)             ; {ram.GP_00}
C56F: 40              RTI                         
C570: 01 00           ORA     ($00,X)             ; {ram.GP_00}
C572: 11 10           ORA     ($10),Y             
C574: 21 20           AND     ($20,X)             
C576: 00              BRK                         
C577: 00              BRK                         
C578: 00              BRK                         
C579: 01 10           ORA     ($10,X)             
C57B: 11 22           ORA     ($22),Y             
C57D: 23 ; ????
C57E: 00              BRK                         
C57F: 40              RTI                         
C580: 01 00           ORA     ($00,X)             ; {ram.GP_00}
C582: 11 10           ORA     ($10),Y             
C584: 23 ; ????
C585: 22 ; ????
C586: 00              BRK                         
C587: 00              BRK                         
C588: 00              BRK                         
C589: 01 10           ORA     ($10,X)             
C58B: 11 24           ORA     ($24),Y             
C58D: 25 00           AND     $00                 ; {ram.GP_00}
C58F: 40              RTI                         
C590: 01 00           ORA     ($00,X)             ; {ram.GP_00}
C592: 11 10           ORA     ($10),Y             
C594: 25 24           AND     $24                 
C596: 00              BRK                         
C597: 00              BRK                         
C598: 00              BRK                         
C599: 01 10           ORA     ($10,X)             
C59B: 11 28           ORA     ($28),Y             
C59D: 29 00           AND     #$00                
C59F: 40              RTI                         
C5A0: 01 00           ORA     ($00,X)             ; {ram.GP_00}
C5A2: 11 10           ORA     ($10),Y             
C5A4: 29 28           AND     #$28                
C5A6: 00              BRK                         
C5A7: 00              BRK                         
C5A8: 00              BRK                         
C5A9: 01 14           ORA     ($14,X)             
C5AB: 15 40           ORA     $40,X               
C5AD: 41 00           EOR     ($00,X)             ; {ram.GP_00}
C5AF: 40              RTI                         
C5B0: 01 00           ORA     ($00,X)             ; {ram.GP_00}
C5B2: 15 14           ORA     $14,X               
C5B4: 41 40           EOR     ($40,X)             
C5B6: 00              BRK                         
C5B7: 00              BRK                         
C5B8: 00              BRK                         
C5B9: 01 14           ORA     ($14,X)             
C5BB: 0B ; ????
C5BC: 40              RTI                         
C5BD: 41 00           EOR     ($00,X)             ; {ram.GP_00}
C5BF: 40              RTI                         
C5C0: 01 00           ORA     ($00,X)             ; {ram.GP_00}
C5C2: 0B ; ????
C5C3: 14 ; ????
C5C4: 41 40           EOR     ($40,X)             
C5C6: 00              BRK                         
C5C7: 00              BRK                         
C5C8: 0C ; ????
C5C9: 0D 1C 1D        ORA     $1D1C               
C5CC: 2C 2D 00        BIT     $002D               
C5CF: 40              RTI                         
C5D0: 0D 0C 1D        ORA     $1D0C               
C5D3: 1C ; ????
C5D4: 2D 2C 00        AND     $002C               
C5D7: 00              BRK                         
C5D8: 00              BRK                         
C5D9: 01 14           ORA     ($14,X)             
C5DB: 15 24           ORA     $24,X               
C5DD: 25 00           AND     $00                 ; {ram.GP_00}
C5DF: 40              RTI                         
C5E0: 01 00           ORA     ($00,X)             ; {ram.GP_00}
C5E2: 15 14           ORA     $14,X               
C5E4: 25 24           AND     $24                 
C5E6: 00              BRK                         
C5E7: 00              BRK                         
C5E8: 00              BRK                         
C5E9: 01 18           ORA     ($18,X)             
C5EB: 19 20 21        ORA     $2120,Y             
C5EE: 00              BRK                         
C5EF: 40              RTI                         
C5F0: 01 00           ORA     ($00,X)             ; {ram.GP_00}
C5F2: 19 18 21        ORA     $2118,Y             
C5F5: 20 00 00        JSR     $0000               ; {ram.GP_00}
C5F8: 00              BRK                         
C5F9: 01 18           ORA     ($18,X)             
C5FB: 19 22 23        ORA     $2322,Y             
C5FE: 00              BRK                         
C5FF: 40              RTI                         
C600: 01 00           ORA     ($00,X)             ; {ram.GP_00}
C602: 19 18 23        ORA     $2318,Y             
C605: 22 ; ????
C606: 00              BRK                         
C607: 00              BRK                         
C608: 00              BRK                         
C609: 01 10           ORA     ($10,X)             
C60B: 11 24           ORA     ($24),Y             
C60D: 25 00           AND     $00                 ; {ram.GP_00}
C60F: 40              RTI                         
C610: 01 00           ORA     ($00,X)             ; {ram.GP_00}
C612: 11 10           ORA     ($10),Y             
C614: 25 24           AND     $24                 
C616: 00              BRK                         
C617: 00              BRK                         
C618: 00              BRK                         
C619: 01 18           ORA     ($18,X)             
C61B: 19 28 29        ORA     $2928,Y             
C61E: 00              BRK                         
C61F: 40              RTI                         
C620: 01 00           ORA     ($00,X)             ; {ram.GP_00}
C622: 19 18 29        ORA     $2918,Y             
C625: 28              PLP                         
C626: 00              BRK                         
C627: 00              BRK                         
C628: 00              BRK                         
C629: 01 1A           ORA     ($1A,X)             
C62B: 1B ; ????
C62C: 40              RTI                         
C62D: 41 00           EOR     ($00,X)             ; {ram.GP_00}
C62F: 40              RTI                         
C630: 01 00           ORA     ($00,X)             ; {ram.GP_00}
C632: 1B ; ????
C633: 1A ; ????
C634: 41 40           EOR     ($40,X)             
C636: 00              BRK                         
C637: 00              BRK                         
C638: 00              BRK                         
C639: 01 1A           ORA     ($1A,X)             
C63B: 2B ; ????
C63C: 40              RTI                         
C63D: 41 00           EOR     ($00,X)             ; {ram.GP_00}
C63F: 40              RTI                         
C640: 01 00           ORA     ($00,X)             ; {ram.GP_00}
C642: 2B ; ????
C643: 1A ; ????
C644: 41 40           EOR     ($40,X)             
C646: 00              BRK                         
C647: 00              BRK                         
C648: 0C ; ????
C649: 0F ; ????
C64A: 1C ; ????
C64B: 1F ; ????
C64C: 2C 2D 00        BIT     $002D               
C64F: 40              RTI                         
C650: 0F ; ????
C651: 0C ; ????
C652: 1F ; ????
C653: 1C ; ????
C654: 2D 2C 00        AND     $002C               
C657: 00              BRK                         
C658: 00              BRK                         
C659: 01 1A           ORA     ($1A,X)             
C65B: 1B ; ????
C65C: 24 25           BIT     $25                 
C65E: 00              BRK                         
C65F: 40              RTI                         
C660: 01 00           ORA     ($00,X)             ; {ram.GP_00}
C662: 1B ; ????
C663: 1A ; ????
C664: 25 24           AND     $24                 
C666: 00              BRK                         
C667: 29 7F           AND     #$7F                
C669: 20 B2 C6        JSR     $C6B2               ; {}
C66C: 0A              ASL     A                   
C66D: 0A              ASL     A                   
C66E: 0A              ASL     A                   
C66F: 0A              ASL     A                   
C670: A8              TAY                         
C671: A9 03           LDA     #$03                
C673: 85 00           STA     $00                 ; {ram.GP_00}
C675: BD 00 07        LDA     $0700,X             
C678: 85 01           STA     $01                 
C67A: BD 03 07        LDA     $0703,X             
C67D: 85 02           STA     $02                 
C67F: 8A              TXA                         
C680: 48              PHA                         
C681: B1 03           LDA     ($03),Y             
C683: C9 7F           CMP     #$7F                
C685: D0 04           BNE     $C68B               ; {}
C687: A9 F8           LDA     #$F8                
C689: D0 03           BNE     $C68E               ; {}
C68B: 18              CLC                         
C68C: 65 01           ADC     $01                 
C68E: 9D 00 02        STA     $0200,X             
C691: C8              INY                         
C692: E8              INX                         
C693: B1 03           LDA     ($03),Y             
C695: 9D 00 02        STA     $0200,X             
C698: C8              INY                         
C699: E8              INX                         
C69A: B1 03           LDA     ($03),Y             
C69C: 9D 00 02        STA     $0200,X             
C69F: C8              INY                         
C6A0: E8              INX                         
C6A1: B1 03           LDA     ($03),Y             
C6A3: 18              CLC                         
C6A4: 65 02           ADC     $02                 
C6A6: 9D 00 02        STA     $0200,X             
C6A9: E8              INX                         
C6AA: C8              INY                         
C6AB: C6 00           DEC     $00                 ; {ram.GP_00}
C6AD: 10 D2           BPL     $C681               ; {}
C6AF: 68              PLA                         
C6B0: AA              TAX                         
C6B1: 60              RTS                         
C6B2: 48              PHA                         
C6B3: 4A              LSR     A                   
C6B4: 4A              LSR     A                   
C6B5: 4A              LSR     A                   
C6B6: 4A              LSR     A                   
C6B7: 0A              ASL     A                   
C6B8: A8              TAY                         
C6B9: B9 52 7F        LDA     $7F52,Y             
C6BC: 85 03           STA     $03                 
C6BE: B9 53 7F        LDA     $7F53,Y             
C6C1: 85 04           STA     $04                 
C6C3: 68              PLA                         
C6C4: 60              RTS                         
C6C5: A8              TAY                         
C6C6: A9 05           LDA     #$05                
C6C8: 85 00           STA     $00                 ; {ram.GP_00}
C6CA: BD 00 07        LDA     $0700,X             
C6CD: 85 01           STA     $01                 
C6CF: BD 03 07        LDA     $0703,X             
C6D2: 85 02           STA     $02                 
C6D4: BD 02 07        LDA     $0702,X             
C6D7: 85 03           STA     $03                 
C6D9: 8A              TXA                         
C6DA: 48              PHA                         
C6DB: B9 3D C7        LDA     $C73D,Y             ; {}
C6DE: C9 7F           CMP     #$7F                
C6E0: D0 04           BNE     $C6E6               ; {}
C6E2: A9 F8           LDA     #$F8                
C6E4: D0 03           BNE     $C6E9               ; {}
C6E6: 18              CLC                         
C6E7: 65 01           ADC     $01                 
C6E9: 9D 00 02        STA     $0200,X             
C6EC: C8              INY                         
C6ED: E8              INX                         
C6EE: B9 3D C7        LDA     $C73D,Y             ; {}
C6F1: 9D 00 02        STA     $0200,X             
C6F4: C8              INY                         
C6F5: E8              INX                         
C6F6: 20 0D C7        JSR     $C70D               ; {}
C6F9: C8              INY                         
C6FA: E8              INX                         
C6FB: B9 3D C7        LDA     $C73D,Y             ; {}
C6FE: 18              CLC                         
C6FF: 65 02           ADC     $02                 
C701: 9D 00 02        STA     $0200,X             
C704: E8              INX                         
C705: C8              INY                         
C706: C6 00           DEC     $00                 ; {ram.GP_00}
C708: 10 D1           BPL     $C6DB               ; {}
C70A: 68              PLA                         
C70B: AA              TAX                         
C70C: 60              RTS                         
C70D: A5 03           LDA     $03                 
C70F: 10 09           BPL     $C71A               ; {}
C711: B9 3D C7        LDA     $C73D,Y             ; {}
C714: 09 20           ORA     #$20                
C716: 9D 00 02        STA     $0200,X             
C719: 60              RTS                         
C71A: B9 3D C7        LDA     $C73D,Y             ; {}
C71D: 9D 00 02        STA     $0200,X             
C720: 60              RTS                         
C721: 05 FF           ORA     $FF                 
C723: 05 FF           ORA     $FF                 
C725: 05 FF           ORA     $FF                 
C727: 03 ; ????
C728: 01 03           ORA     ($03,X)             
C72A: 02 ; ????
C72B: 03 ; ????
C72C: 03 ; ????
C72D: 03 ; ????
C72E: 00              BRK                         
C72F: 05 FF           ORA     $FF                 
C731: FF ; ????
C732: 04 ; ????
C733: FF ; ????
C734: FC ; ????
C735: F7 ; ????
C736: 04 ; ????
C737: F7 ; ????
C738: FC ; ????
C739: EF ; ????
C73A: 04 ; ????
C73B: EF ; ????
C73C: FC ; ????
C73D: 7F ; ????
C73E: 5F ; ????
C73F: 00              BRK                         
C740: 00              BRK                         
C741: 7F ; ????
C742: 5F ; ????
C743: 00              BRK                         
C744: 00              BRK                         
C745: F8              SED                         
C746: 04 ; ????
C747: 00              BRK                         
C748: FC ; ????
C749: F8              SED                         
C74A: 04 ; ????
C74B: 40              RTI                         
C74C: 03 ; ????
C74D: 00              BRK                         
C74E: 05 00           ORA     $00                 ; {ram.GP_00}
C750: FC ; ????
C751: 00              BRK                         
C752: 05 40           ORA     $40                 
C754: 03 ; ????
C755: F0 06           BEQ     $C75D               ; {}
C757: 00              BRK                         
C758: FC ; ????
C759: F0 06           BEQ     $C761               ; {}
C75B: 40              RTI                         
C75C: 03 ; ????
C75D: F8              SED                         
C75E: 07 ; ????
C75F: 00              BRK                         
C760: FC ; ????
C761: F8              SED                         
C762: 07 ; ????
C763: 40              RTI                         
C764: 03 ; ????
C765: 00              BRK                         
C766: 08              PHP                         
C767: 00              BRK                         
C768: FC ; ????
C769: 00              BRK                         
C76A: 08              PHP                         
C76B: 40              RTI                         
C76C: 03 ; ????
C76D: BD 03 07        LDA     $0703,X             
C770: C5 08           CMP     $08                 
C772: B0 0E           BCS     $C782               ; {}
C774: BD 02 07        LDA     $0702,X             
C777: 85 00           STA     $00                 ; {ram.GP_00}
C779: 20 AD C7        JSR     $C7AD               ; {}
C77C: A5 00           LDA     $00                 ; {ram.GP_00}
C77E: 9D 02 07        STA     $0702,X             
C781: 60              RTS                         
C782: BD 02 07        LDA     $0702,X             
C785: 29 F0           AND     #$F0                
C787: 09 0A           ORA     #$0A                
C789: 9D 02 07        STA     $0702,X             
C78C: 60              RTS                         
C78D: BD 03 07        LDA     $0703,X             
C790: C5 08           CMP     $08                 
C792: 90 0E           BCC     $C7A2               ; {}
C794: BD 02 07        LDA     $0702,X             
C797: 85 00           STA     $00                 ; {ram.GP_00}
C799: 20 AD C7        JSR     $C7AD               ; {}
C79C: A5 00           LDA     $00                 ; {ram.GP_00}
C79E: 9D 02 07        STA     $0702,X             
C7A1: 60              RTS                         
C7A2: BD 02 07        LDA     $0702,X             
C7A5: 29 F0           AND     #$F0                
C7A7: 09 05           ORA     #$05                
C7A9: 9D 02 07        STA     $0702,X             
C7AC: 60              RTS                         
C7AD: A5 00           LDA     $00                 ; {ram.GP_00}
C7AF: 29 F0           AND     #$F0                
C7B1: 30 11           BMI     $C7C4               ; {}
C7B3: BD 00 07        LDA     $0700,X             
C7B6: C5 0A           CMP     $0A                 
C7B8: B0 01           BCS     $C7BB               ; {}
C7BA: 60              RTS                         
C7BB: A5 00           LDA     $00                 ; {ram.GP_00}
C7BD: 29 0F           AND     #$0F                
C7BF: 09 B0           ORA     #$B0                
C7C1: 85 00           STA     $00                 ; {ram.GP_00}
C7C3: 60              RTS                         
C7C4: BD 00 07        LDA     $0700,X             
C7C7: C5 09           CMP     $09                 
C7C9: 90 01           BCC     $C7CC               ; {}
C7CB: 60              RTS                         
C7CC: A5 00           LDA     $00                 ; {ram.GP_00}
C7CE: 29 0F           AND     #$0F                
C7D0: 09 40           ORA     #$40                
C7D2: 85 00           STA     $00                 ; {ram.GP_00}
C7D4: 60              RTS                         
C7D5: BD 00 07        LDA     $0700,X             
C7D8: 9D 00 02        STA     $0200,X             
C7DB: 38              SEC                         
C7DC: E9 08           SBC     #$08                
C7DE: 9D 04 02        STA     $0204,X             
C7E1: BD 03 07        LDA     $0703,X             
C7E4: 9D 03 02        STA     $0203,X             
C7E7: A8              TAY                         
C7E8: A5 14           LDA     $14                 
C7EA: 29 0C           AND     #$0C                
C7EC: F0 1A           BEQ     $C808               ; {}
C7EE: 4A              LSR     A                   
C7EF: 4A              LSR     A                   
C7F0: 85 00           STA     $00                 ; {ram.GP_00}
C7F2: BD 02 07        LDA     $0702,X             
C7F5: 29 0F           AND     #$0F                
C7F7: C9 08           CMP     #$08                
C7F9: B0 08           BCS     $C803               ; {}
C7FB: 98              TYA                         
C7FC: 18              CLC                         
C7FD: 65 00           ADC     $00                 ; {ram.GP_00}
C7FF: A8              TAY                         
C800: 4C 08 C8        JMP     $C808               ; {}
C803: 98              TYA                         
C804: 38              SEC                         
C805: E5 00           SBC     $00                 ; {ram.GP_00}
C807: A8              TAY                         
C808: 98              TYA                         
C809: 9D 07 02        STA     $0207,X             
C80C: A9 02           LDA     #$02                
C80E: 9D 02 02        STA     $0202,X             
C811: 9D 06 02        STA     $0206,X             
C814: A0 8C           LDY     #$8C                
C816: A5 14           LDA     $14                 
C818: 29 08           AND     #$08                
C81A: D0 02           BNE     $C81E               ; {}
C81C: A0 8D           LDY     #$8D                
C81E: 98              TYA                         
C81F: 9D 01 02        STA     $0201,X             
C822: 38              SEC                         
C823: E9 02           SBC     #$02                
C825: 9D 05 02        STA     $0205,X             
C828: BD 02 07        LDA     $0702,X             
C82B: 29 0F           AND     #$0F                
C82D: C9 08           CMP     #$08                
C82F: B0 0B           BCS     $C83C               ; {}
C831: BD 02 02        LDA     $0202,X             
C834: 09 40           ORA     #$40                
C836: 9D 02 02        STA     $0202,X             
C839: 9D 06 02        STA     $0206,X             
C83C: 60              RTS                         
C83D: 20 39 EF        JSR     $EF39               ; {}
C840: 20 06 7F        JSR     $7F06               
C843: 4C C9 EB        JMP     $EBC9               ; {}
C846: A5 B6           LDA     $B6                 
C848: 48              PHA                         
C849: A9 04           LDA     #$04                
C84B: 20 7F C1        JSR     $C17F               ; {}
C84E: 20 00 A0        JSR     $A000               
C851: 68              PLA                         
C852: 20 7F C1        JSR     $C17F               ; {}
C855: 60              RTS                         
C856: A5 B6           LDA     $B6                 
C858: 48              PHA                         
C859: A9 04           LDA     #$04                
C85B: 20 7F C1        JSR     $C17F               ; {}
C85E: 20 03 A0        JSR     $A003               
C861: 68              PLA                         
C862: 20 7F C1        JSR     $C17F               ; {}
C865: 60              RTS                         
```

# NMI

```code
NMI:
C866: 48              PHA                         
C867: A5 B6           LDA     $B6                 
C869: 48              PHA                         
C86A: A9 C8           LDA     #$C8                
C86C: 48              PHA                         
C86D: A9 77           LDA     #$77                
C86F: 48              PHA                         
C870: A5 BE           LDA     $BE                 
C872: 20 7F C1        JSR     $C17F               ; {}
C875: 6C FA 6F        JMP     ($6FFA)             
C878: AD 00 01        LDA     $0100               
C87B: 29 7F           AND     #$7F                
C87D: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
C880: 68              PLA                         
C881: 85 B6           STA     $B6                 
C883: 8D FF FF        STA     $FFFF               ; 
C886: 4A              LSR     A                   
C887: 8D FF FF        STA     $FFFF               ; 
C88A: 4A              LSR     A                   
C88B: 8D FF FF        STA     $FFFF               ; 
C88E: 4A              LSR     A                   
C88F: 8D FF FF        STA     $FFFF               ; 
C892: 4A              LSR     A                   
C893: 8D FF FF        STA     $FFFF               ; 
C896: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
C899: AD 00 01        LDA     $0100               
C89C: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
C89F: 68              PLA                         
C8A0: 40              RTI                         
```

```code
C8A1: 20 B1 C8        JSR     $C8B1               ; {}
C8A4: 20 8A C9        JSR     $C98A               ; {}
C8A7: 20 75 C9        JSR     $C975               ; {}
C8AA: 20 C6 C8        JSR     $C8C6               ; {}
C8AD: 20 2B C9        JSR     $C92B               ; {}
C8B0: 60              RTS                         
C8B1: A2 2F           LDX     #$2F                
C8B3: A9 00           LDA     #$00                
C8B5: 9D 31 60        STA     $6031,X             
C8B8: CA              DEX                         
C8B9: 10 FA           BPL     $C8B5               ; {}
C8BB: A2 11           LDX     #$11                
C8BD: A9 00           LDA     #$00                
C8BF: 9D 61 60        STA     $6061,X             
C8C2: CA              DEX                         
C8C3: 10 FA           BPL     $C8BF               ; {}
C8C5: 60              RTS                         
C8C6: A9 00           LDA     #$00                
C8C8: A8              TAY                         
C8C9: B9 61 60        LDA     $6061,Y             
C8CC: 20 12 C9        JSR     $C912               ; {}
C8CF: 20 09 C9        JSR     $C909               ; {}
C8D2: 20 22 C9        JSR     $C922               ; {}
C8D5: C8              INY                         
C8D6: C0 12           CPY     #$12                
C8D8: B0 25           BCS     $C8FF               ; {}
C8DA: B9 61 60        LDA     $6061,Y             
C8DD: 20 1A C9        JSR     $C91A               ; {}
C8E0: 20 09 C9        JSR     $C909               ; {}
C8E3: 20 1A C9        JSR     $C91A               ; {}
C8E6: C8              INY                         
C8E7: C0 12           CPY     #$12                
C8E9: B0 14           BCS     $C8FF               ; {}
C8EB: B9 61 60        LDA     $6061,Y             
C8EE: 20 22 C9        JSR     $C922               ; {}
C8F1: 20 09 C9        JSR     $C909               ; {}
C8F4: 20 12 C9        JSR     $C912               ; {}
C8F7: 20 09 C9        JSR     $C909               ; {}
C8FA: C8              INY                         
C8FB: C0 12           CPY     #$12                
C8FD: 90 CA           BCC     $C8C9               ; {}
C8FF: 60              RTS                         
C900: A2 17           LDX     #$17                
C902: 7E 31 60        ROR     $6031,X             
C905: CA              DEX                         
C906: 10 FA           BPL     $C902               ; {}
C908: 60              RTS                         
C909: 18              CLC                         
C90A: 20 00 C9        JSR     $C900               ; {}
C90D: 18              CLC                         
C90E: 20 00 C9        JSR     $C900               ; {}
C911: 60              RTS                         
C912: 4A              LSR     A                   
C913: 20 00 C9        JSR     $C900               ; {}
C916: 4A              LSR     A                   
C917: 20 00 C9        JSR     $C900               ; {}
C91A: 4A              LSR     A                   
C91B: 20 00 C9        JSR     $C900               ; {}
C91E: 4A              LSR     A                   
C91F: 20 00 C9        JSR     $C900               ; {}
C922: 4A              LSR     A                   
C923: 20 00 C9        JSR     $C900               ; {}
C926: 4A              LSR     A                   
C927: 20 00 C9        JSR     $C900               ; {}
C92A: 60              RTS                         
C92B: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
C92E: A9 22           LDA     #$22                
C930: A0 89           LDY     #$89                
C932: A2 00           LDX     #$00                
C934: 20 59 C9        JSR     $C959               ; {}
C937: 20 60 C9        JSR     $C960               ; {}
C93A: A9 22           LDA     #$22                
C93C: A0 91           LDY     #$91                
C93E: 20 59 C9        JSR     $C959               ; {}
C941: 20 60 C9        JSR     $C960               ; {}
C944: A9 22           LDA     #$22                
C946: A0 C9           LDY     #$C9                
C948: 20 59 C9        JSR     $C959               ; {}
C94B: 20 60 C9        JSR     $C960               ; {}
C94E: A9 22           LDA     #$22                
C950: A0 D1           LDY     #$D1                
C952: 20 59 C9        JSR     $C959               ; {}
C955: 20 60 C9        JSR     $C960               ; {}
C958: 60              RTS                         
C959: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
C95C: 8C 06 20        STY     $2006               ; {hard.P_VRAM_ADDR}
C95F: 60              RTS                         
C960: A0 05           LDY     #$05                
C962: 98              TYA                         
C963: 48              PHA                         
C964: BD 31 60        LDA     $6031,X             
C967: A8              TAY                         
C968: B9 50 CA        LDA     $CA50,Y             ; {}
C96B: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
C96E: 68              PLA                         
C96F: A8              TAY                         
C970: E8              INX                         
C971: 88              DEY                         
C972: 10 EE           BPL     $C962               ; {}
C974: 60              RTS                         
C975: A2 00           LDX     #$00                
C977: 86 00           STX     $00                 ; {ram.GP_00}
C979: A5 00           LDA     $00                 ; {ram.GP_00}
C97B: 18              CLC                         
C97C: 7D 61 60        ADC     $6061,X             
C97F: 85 00           STA     $00                 ; {ram.GP_00}
C981: E8              INX                         
C982: E0 11           CPX     #$11                
C984: 90 F3           BCC     $C979               ; {}
C986: 9D 61 60        STA     $6061,X             
C989: 60              RTS                         
C98A: A0 02           LDY     #$02                
C98C: B9 0D 60        LDA     $600D,Y             
C98F: 29 F3           AND     #$F3                
C991: 85 00           STA     $00                 ; {ram.GP_00}
C993: B9 10 60        LDA     $6010,Y             
C996: 29 03           AND     #$03                
C998: 0A              ASL     A                   
C999: 0A              ASL     A                   
C99A: 05 00           ORA     $00                 ; {ram.GP_00}
C99C: 99 61 60        STA     $6061,Y             
C99F: 88              DEY                         
C9A0: 10 EA           BPL     $C98C               ; {}
C9A2: AD 13 60        LDA     $6013               
C9A5: 8D 64 60        STA     $6064               
C9A8: AD 14 60        LDA     $6014               
C9AB: 8D 65 60        STA     $6065               
C9AE: AD 15 60        LDA     $6015               
C9B1: 8D 66 60        STA     $6066               
C9B4: AD 19 60        LDA     $6019               
C9B7: 8D 67 60        STA     $6067               
C9BA: AD 1A 60        LDA     $601A               
C9BD: 29 0F           AND     #$0F                
C9BF: 85 00           STA     $00                 ; {ram.GP_00}
C9C1: AD 1B 60        LDA     $601B               
C9C4: 8D 69 60        STA     $6069               
C9C7: AD 1C 60        LDA     $601C               
C9CA: 29 0F           AND     #$0F                
C9CC: 0A              ASL     A                   
C9CD: 0A              ASL     A                   
C9CE: 0A              ASL     A                   
C9CF: 0A              ASL     A                   
C9D0: 05 00           ORA     $00                 ; {ram.GP_00}
C9D2: 8D 68 60        STA     $6068               
C9D5: A5 26           LDA     $26                 
C9D7: 29 FE           AND     #$FE                
C9D9: 85 00           STA     $00                 ; {ram.GP_00}
C9DB: AD 1D 60        LDA     $601D               
C9DE: 29 01           AND     #$01                
C9E0: 05 00           ORA     $00                 ; {ram.GP_00}
C9E2: 8D 6A 60        STA     $606A               
C9E5: AD 1E 60        LDA     $601E               
C9E8: 8D 6B 60        STA     $606B               
C9EB: AD 1F 60        LDA     $601F               
C9EE: 8D 6C 60        STA     $606C               
C9F1: AD 20 60        LDA     $6020               
C9F4: 8D 6D 60        STA     $606D               
C9F7: AD 21 60        LDA     $6021               
C9FA: 0A              ASL     A                   
C9FB: 0A              ASL     A                   
C9FC: 0A              ASL     A                   
C9FD: 0A              ASL     A                   
C9FE: 85 00           STA     $00                 ; {ram.GP_00}
CA00: AD 26 60        LDA     $6026               
CA03: 29 0F           AND     #$0F                
CA05: 05 00           ORA     $00                 ; {ram.GP_00}
CA07: 8D 6E 60        STA     $606E               
CA0A: AD 22 60        LDA     $6022               
CA0D: 29 03           AND     #$03                
CA0F: 85 00           STA     $00                 ; {ram.GP_00}
CA11: AD 23 60        LDA     $6023               
CA14: 29 03           AND     #$03                
CA16: 0A              ASL     A                   
CA17: 0A              ASL     A                   
CA18: 05 00           ORA     $00                 ; {ram.GP_00}
CA1A: 85 00           STA     $00                 ; {ram.GP_00}
CA1C: AD 24 60        LDA     $6024               
CA1F: 29 03           AND     #$03                
CA21: 0A              ASL     A                   
CA22: 0A              ASL     A                   
CA23: 0A              ASL     A                   
CA24: 0A              ASL     A                   
CA25: 05 00           ORA     $00                 ; {ram.GP_00}
CA27: 8D 6F 60        STA     $606F               
CA2A: AD 25 60        LDA     $6025               
CA2D: 8D 70 60        STA     $6070               
CA30: AD 28 60        LDA     $6028               
CA33: 0A              ASL     A                   
CA34: 0A              ASL     A                   
CA35: 0A              ASL     A                   
CA36: 0A              ASL     A                   
CA37: 85 00           STA     $00                 ; {ram.GP_00}
CA39: AD 29 60        LDA     $6029               
CA3C: 29 07           AND     #$07                
CA3E: 05 00           ORA     $00                 ; {ram.GP_00}
CA40: 85 00           STA     $00                 ; {ram.GP_00}
CA42: AD 2A 60        LDA     $602A               
CA45: 0A              ASL     A                   
CA46: 0A              ASL     A                   
CA47: 0A              ASL     A                   
CA48: 29 08           AND     #$08                
CA4A: 05 00           ORA     $00                 ; {ram.GP_00}
CA4C: 8D 71 60        STA     $6071               
CA4F: 60              RTS                         
CA50: 00              BRK                         
CA51: 01 02           ORA     ($02,X)             
CA53: 03 ; ????
CA54: 04 ; ????
CA55: 05 06           ORA     $06                 
CA57: 07 ; ????
CA58: 08              PHP                         
CA59: 09 16           ORA     #$16                
CA5B: 17 ; ????
CA5C: 18              CLC                         
CA5D: 19 1A 1B        ORA     $1B1A,Y             
CA60: 1C ; ????
CA61: 1D 1E 1F        ORA     $1F1E,X             
CA64: 20 21 22        JSR     $2221               
CA67: 23 ; ????
CA68: 24 25           BIT     $25                 
CA6A: 26 27           ROL     $27                 
CA6C: 28              PLP                         
CA6D: 29 2A           AND     #$2A                
CA6F: 2B ; ????
CA70: 2C 2D 2E        BIT     $2E2D               
CA73: 2F ; ????
CA74: 30 31           BMI     $CAA7               ; {}
CA76: 32 ; ????
CA77: 33 ; ????
CA78: 34 ; ????
CA79: 35 36           AND     $36,X               
CA7B: 37 ; ????
CA7C: 38              SEC                         
CA7D: 39 3A 3B        AND     $3B3A,Y             
CA80: 3C ; ????
CA81: 3D 3E 3F        AND     $3F3E,X             
CA84: 40              RTI                         
CA85: 41 42           EOR     ($42,X)             
CA87: 43 ; ????
CA88: 44 ; ????
CA89: 45 46           EOR     $46                 
CA8B: 47 ; ????
CA8C: 48              PHA                         
CA8D: 49 0A           EOR     #$0A                
CA8F: 0E 48 AD        ASL     $AD48               
CA92: 00              BRK                         
CA93: 01 29           ORA     ($29,X)             
CA95: 7F ; ????
CA96: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
CA99: 68              PLA                         
CA9A: 85 BC           STA     $BC                 
CA9C: A5 B6           LDA     $B6                 
CA9E: 48              PHA                         
CA9F: A9 CA           LDA     #$CA                
CAA1: 48              PHA                         
CAA2: A9 C6           LDA     #$C6                
CAA4: 48              PHA                         
CAA5: A9 80           LDA     #$80                
CAA7: 85 BD           STA     $BD                 
CAA9: A9 06           LDA     #$06                
CAAB: 85 B6           STA     $B6                 
CAAD: 8D FF FF        STA     $FFFF               ; 
CAB0: 4A              LSR     A                   
CAB1: 8D FF FF        STA     $FFFF               ; 
CAB4: 4A              LSR     A                   
CAB5: 8D FF FF        STA     $FFFF               ; 
CAB8: 4A              LSR     A                   
CAB9: 8D FF FF        STA     $FFFF               ; 
CABC: 4A              LSR     A                   
CABD: 8D FF FF        STA     $FFFF               ; 
CAC0: A9 6C           LDA     #$6C                
CAC2: 85 BB           STA     $BB                 
CAC4: 4C BB 00        JMP     $00BB               
CAC7: 48              PHA                         
CAC8: AD 00 01        LDA     $0100               
CACB: 29 7F           AND     #$7F                
CACD: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
CAD0: 68              PLA                         
CAD1: 85 B8           STA     $B8                 
CAD3: 68              PLA                         
CAD4: 85 B6           STA     $B6                 
CAD6: 8D FF FF        STA     $FFFF               ; 
CAD9: 4A              LSR     A                   
CADA: 8D FF FF        STA     $FFFF               ; 
CADD: 4A              LSR     A                   
CADE: 8D FF FF        STA     $FFFF               ; 
CAE1: 4A              LSR     A                   
CAE2: 8D FF FF        STA     $FFFF               ; 
CAE5: 4A              LSR     A                   
CAE6: 8D FF FF        STA     $FFFF               ; 
CAE9: A5 B8           LDA     $B8                 
CAEB: 48              PHA                         
CAEC: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
CAEF: AD 00 01        LDA     $0100               
CAF2: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
CAF5: 68              PLA                         
CAF6: 60              RTS                         
CAF7: 48              PHA                         
CAF8: AD 00 01        LDA     $0100               
CAFB: 29 7F           AND     #$7F                
CAFD: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
CB00: 68              PLA                         
CB01: 85 B8           STA     $B8                 
CB03: 68              PLA                         
CB04: 85 C1           STA     $C1                 
CB06: 68              PLA                         
CB07: 85 C2           STA     $C2                 
CB09: 68              PLA                         
CB0A: 85 C3           STA     $C3                 
CB0C: 68              PLA                         
CB0D: 85 C4           STA     $C4                 
CB0F: A5 C2           LDA     $C2                 
CB11: 48              PHA                         
CB12: A5 C1           LDA     $C1                 
CB14: 48              PHA                         
CB15: A9 06           LDA     #$06                
CB17: 48              PHA                         
CB18: A9 CA           LDA     #$CA                
CB1A: 48              PHA                         
CB1B: A9 C6           LDA     #$C6                
CB1D: 48              PHA                         
CB1E: A5 C4           LDA     $C4                 
CB20: 48              PHA                         
CB21: A5 C3           LDA     $C3                 
CB23: 48              PHA                         
CB24: A5 BE           LDA     $BE                 
CB26: 85 B6           STA     $B6                 
CB28: 8D FF FF        STA     $FFFF               ; 
CB2B: 4A              LSR     A                   
CB2C: 8D FF FF        STA     $FFFF               ; 
CB2F: 4A              LSR     A                   
CB30: 8D FF FF        STA     $FFFF               ; 
CB33: 4A              LSR     A                   
CB34: 8D FF FF        STA     $FFFF               ; 
CB37: 4A              LSR     A                   
CB38: 8D FF FF        STA     $FFFF               ; 
CB3B: A5 B8           LDA     $B8                 
CB3D: 48              PHA                         
CB3E: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
CB41: AD 00 01        LDA     $0100               
CB44: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
CB47: 68              PLA                         
CB48: 60              RTS                         
CB49: A5 BE           LDA     $BE                 
CB4B: 4C 7F C1        JMP     $C17F               ; {}
CB4E: A5 BE           LDA     $BE                 
CB50: 20 7F C1        JSR     $C17F               ; {}
CB53: 20 33 7F        JSR     $7F33               
CB56: 20 36 7F        JSR     $7F36               
CB59: 20 39 7F        JSR     $7F39               
CB5C: 20 3C 7F        JSR     $7F3C               
CB5F: A9 06           LDA     #$06                
CB61: 4C 7F C1        JMP     $C17F               ; {}
CB64: A9 02           LDA     #$02                
CB66: D0 20           BNE     $CB88               ; {}
CB68: A9 04           LDA     #$04                
CB6A: D0 1C           BNE     $CB88               ; {}
CB6C: A9 08           LDA     #$08                
CB6E: D0 18           BNE     $CB88               ; {}
CB70: A5 3A           LDA     $3A                 
CB72: F0 1F           BEQ     $CB93               ; {}
CB74: C9 10           CMP     #$10                
CB76: 90 2E           BCC     $CBA6               ; {}
CB78: AC 2F 01        LDY     $012F               
CB7B: A5 46           LDA     $46                 
CB7D: D9 90 CB        CMP     $CB90,Y             ; {}
CB80: F0 0A           BEQ     $CB8C               ; {}
CB82: C9 1B           CMP     #$1B                
CB84: D0 05           BNE     $CB8B               ; {}
CB86: A9 40           LDA     #$40                
CB88: 8D 85 03        STA     $0385               
CB8B: 60              RTS                         
CB8C: A9 20           LDA     #$20                
CB8E: D0 F8           BNE     $CB88               ; {}
CB90: 37 ; ????
CB91: 2E 07 AD        ROL     $AD07               
CB94: 2F ; ????
CB95: 01 C9           ORA     ($C9,X)             
CB97: 01 F0           ORA     ($F0,X)             
CB99: CA              DEX                         
CB9A: C9 02           CMP     #$02                
CB9C: F0 CA           BEQ     $CB68               ; {}
CB9E: C9 03           CMP     #$03                
CBA0: F0 CA           BEQ     $CB6C               ; {}
CBA2: A9 01           LDA     #$01                
CBA4: D0 E2           BNE     $CB88               ; {}
CBA6: A4 3B           LDY     $3B                 
CBA8: C0 22           CPY     #$22                
CBAA: F0 E0           BEQ     $CB8C               ; {}
CBAC: C0 23           CPY     #$23                
CBAE: F0 DC           BEQ     $CB8C               ; {}
CBB0: A9 01           LDA     #$01                
CBB2: 8D 80 03        STA     $0380               
CBB5: 60              RTS                         
CBB6: 20 09 7F        JSR     $7F09               
CBB9: A2 20           LDX     #$20                
CBBB: BD 01 07        LDA     $0701,X             
CBBE: 10 7A           BPL     $CC3A               ; {}
CBC0: 29 70           AND     #$70                
CBC2: F0 03           BEQ     $CBC7               ; {}
CBC4: 4C 54 CC        JMP     $CC54               ; {}
CBC7: BD 00 07        LDA     $0700,X             
CBCA: C9 E8           CMP     #$E8                
CBCC: 90 03           BCC     $CBD1               ; {}
CBCE: 4C 7B CC        JMP     $CC7B               ; {}
CBD1: C9 10           CMP     #$10                
CBD3: B0 05           BCS     $CBDA               ; {}
CBD5: A9 10           LDA     #$10                
CBD7: 9D 00 07        STA     $0700,X             
CBDA: 20 B8 DF        JSR     $DFB8               ; {}
CBDD: 20 AB E0        JSR     $E0AB               ; {}
CBE0: 20 B3 CC        JSR     $CCB3               ; {}
CBE3: BD 01 07        LDA     $0701,X             
CBE6: 29 0F           AND     #$0F                
CBE8: 20 2B EE        JSR     $EE2B               ; {}
CBEB: F9 CC F9        SBC     $F9CC,Y             ; {}
CBEE: CC F9 CC        CPY     $CCF9               ; {}
CBF1: F9 CC 5B        SBC     $5BCC,Y             
CBF4: CD 5B CD        CMP     $CD5B               ; {}
CBF7: 5B ; ????
CBF8: CD 5B CD        CMP     $CD5B               ; {}
CBFB: 3E CD 3E        ROL     $3ECD,X             
CBFE: CD 3E CD        CMP     $CD3E               ; {}
CC01: 3E CD 55        ROL     $55CD,X             
CC04: CD 55 CD        CMP     $CD55               ; {}
CC07: 55 CD           EOR     $CD,X               
CC09: 55 CD           EOR     $CD,X               
CC0B: 4C 1D E1        JMP     $E11D               ; {}
CC0E: 4C 2D E1        JMP     $E12D               ; {}
CC11: 4C 35 E1        JMP     $E135               ; {}
CC14: 4C 55 E1        JMP     $E155               ; {}
CC17: A9 04           LDA     #$04                
CC19: 85 37           STA     $37                 
CC1B: A9 07           LDA     #$07                
CC1D: 20 CD C4        JSR     $C4CD               ; {}
CC20: FE 04 07        INC     $0704,X             
CC23: BD 04 07        LDA     $0704,X             
CC26: C9 10           CMP     #$10                
CC28: 60              RTS                         
CC29: 20 17 CC        JSR     $CC17               ; {}
CC2C: 90 DD           BCC     $CC0B               ; {}
CC2E: C9 20           CMP     #$20                
CC30: 90 DC           BCC     $CC0E               ; {}
CC32: C9 30           CMP     #$30                
CC34: 90 DB           BCC     $CC11               ; {}
CC36: A9 80           LDA     #$80                
CC38: 85 AB           STA     $AB                 
CC3A: 60              RTS                         
CC3B: 20 17 CC        JSR     $CC17               ; {}
CC3E: 90 CE           BCC     $CC0E               ; {}
CC40: C9 20           CMP     #$20                
CC42: 90 C7           BCC     $CC0B               ; {}
CC44: C9 30           CMP     #$30                
CC46: 90 CC           BCC     $CC14               ; {}
CC48: A9 80           LDA     #$80                
CC4A: 9D 01 07        STA     $0701,X             
CC4D: 0A              ASL     A                   
CC4E: 9D 04 07        STA     $0704,X             
CC51: 85 37           STA     $37                 
CC53: 60              RTS                         
CC54: C9 10           CMP     #$10                
CC56: F0 E3           BEQ     $CC3B               ; {}
CC58: C9 20           CMP     #$20                
CC5A: F0 CD           BEQ     $CC29               ; {}
CC5C: BD 05 07        LDA     $0705,X             
CC5F: D0 4A           BNE     $CCAB               ; {}
CC61: BD 00 07        LDA     $0700,X             
CC64: C9 F8           CMP     #$F8                
CC66: B0 13           BCS     $CC7B               ; {}
CC68: BD 02 07        LDA     $0702,X             
CC6B: 29 7F           AND     #$7F                
CC6D: 9D 02 07        STA     $0702,X             
CC70: FE 00 07        INC     $0700,X             
CC73: FE 00 07        INC     $0700,X             
CC76: A9 18           LDA     #$18                
CC78: 4C C5 C6        JMP     $C6C5               ; {}
CC7B: CE 50 01        DEC     $0150               
CC7E: 10 13           BPL     $CC93               ; {}
CC80: A9 00           LDA     #$00                
CC82: 9D 01 07        STA     $0701,X             
CC85: 20 2B DD        JSR     $DD2B               ; {}
CC88: 9D 10 02        STA     $0210,X             
CC8B: 9D 14 02        STA     $0214,X             
CC8E: A9 40           LDA     #$40                
CC90: 85 AB           STA     $AB                 
CC92: 60              RTS                         
CC93: A5 A5           LDA     $A5                 
CC95: 09 08           ORA     #$08                
CC97: 85 A5           STA     $A5                 
CC99: A9 FF           LDA     #$FF                
CC9B: 85 A7           STA     $A7                 
CC9D: A9 C0           LDA     #$C0                
CC9F: 85 1D           STA     $1D                 
CCA1: BD 00 07        LDA     $0700,X             
CCA4: 38              SEC                         
CCA5: E9 04           SBC     #$04                
CCA7: 9D 00 07        STA     $0700,X             
CCAA: 60              RTS                         
CCAB: DE 05 07        DEC     $0705,X             
CCAE: A9 18           LDA     #$18                
CCB0: 4C C5 C6        JMP     $C6C5               ; {}
CCB3: A5 A5           LDA     $A5                 
CCB5: 29 0F           AND     #$0F                
CCB7: 85 00           STA     $00                 ; {ram.GP_00}
CCB9: BD 01 07        LDA     $0701,X             
CCBC: 29 F0           AND     #$F0                
CCBE: 05 00           ORA     $00                 ; {ram.GP_00}
CCC0: 9D 01 07        STA     $0701,X             
CCC3: 60              RTS                         
CCC4: A5 A7           LDA     $A7                 
CCC6: C9 40           CMP     #$40                
CCC8: B0 08           BCS     $CCD2               ; {}
CCCA: C9 20           CMP     #$20                
CCCC: B0 05           BCS     $CCD3               ; {}
CCCE: C9 01           CMP     #$01                
CCD0: B0 1F           BCS     $CCF1               ; {}
CCD2: 60              RTS                         
CCD3: A5 14           LDA     $14                 
CCD5: 29 08           AND     #$08                
CCD7: D0 F9           BNE     $CCD2               ; {}
CCD9: A0 05           LDY     #$05                
CCDB: 8A              TXA                         
CCDC: 48              PHA                         
CCDD: BD 02 02        LDA     $0202,X             
CCE0: 29 FC           AND     #$FC                
CCE2: 09 01           ORA     #$01                
CCE4: 9D 02 02        STA     $0202,X             
CCE7: E8              INX                         
CCE8: E8              INX                         
CCE9: E8              INX                         
CCEA: E8              INX                         
CCEB: 88              DEY                         
CCEC: 10 EF           BPL     $CCDD               ; {}
CCEE: 68              PLA                         
CCEF: AA              TAX                         
CCF0: 60              RTS                         
CCF1: A5 14           LDA     $14                 
CCF3: 29 02           AND     #$02                
CCF5: D0 DB           BNE     $CCD2               ; {}
CCF7: F0 E0           BEQ     $CCD9               ; {}
CCF9: 20 48 CF        JSR     $CF48               ; {}
CCFC: 20 A9 CF        JSR     $CFA9               ; {}
CCFF: 20 24 CD        JSR     $CD24               ; {}
CD02: 4C 0C 7F        JMP     $7F0C               
CD05: A5 A5           LDA     $A5                 
CD07: 29 04           AND     #$04                
CD09: D0 13           BNE     $CD1E               ; {}
CD0B: BD 01 07        LDA     $0701,X             
CD0E: 29 40           AND     #$40                
CD10: D0 09           BNE     $CD1B               ; {}
CD12: 20 B8 DF        JSR     $DFB8               ; {}
CD15: 20 48 CF        JSR     $CF48               ; {}
CD18: 4C A9 CF        JMP     $CFA9               ; {}
CD1B: 4C 5C CC        JMP     $CC5C               ; {}
CD1E: 20 0B CD        JSR     $CD0B               ; {}
CD21: 4C 62 CD        JMP     $CD62               ; {}
CD24: AD D5 04        LDA     $04D5               
CD27: A8              TAY                         
CD28: 29 F0           AND     #$F0                
CD2A: C9 20           CMP     #$20                
CD2C: F0 0B           BEQ     $CD39               ; {}
CD2E: AD D6 04        LDA     $04D6               
CD31: A8              TAY                         
CD32: 29 F0           AND     #$F0                
CD34: C9 20           CMP     #$20                
CD36: F0 01           BEQ     $CD39               ; {}
CD38: 60              RTS                         
CD39: A9 04           LDA     #$04                
CD3B: 4C 90 CA        JMP     $CA90               ; {}
CD3E: C6 A7           DEC     $A7                 
CD40: F0 0C           BEQ     $CD4E               ; {}
CD42: 20 48 CF        JSR     $CF48               ; {}
CD45: 20 72 CD        JSR     $CD72               ; {}
CD48: 20 0C 7F        JSR     $7F0C               
CD4B: 4C C4 CC        JMP     $CCC4               ; {}
CD4E: A5 A5           LDA     $A5                 
CD50: 29 F7           AND     #$F7                
CD52: 85 A5           STA     $A5                 
CD54: 60              RTS                         
CD55: 20 3E CD        JSR     $CD3E               ; {}
CD58: 4C 62 CD        JMP     $CD62               ; {}
CD5B: A5 A5           LDA     $A5                 
CD5D: 30 0B           BMI     $CD6A               ; {}
CD5F: 20 F9 CC        JSR     $CCF9               ; {}
CD62: 8A              TXA                         
CD63: 48              PHA                         
CD64: 20 B7 D8        JSR     $D8B7               ; {}
CD67: 68              PLA                         
CD68: AA              TAX                         
CD69: 60              RTS                         
CD6A: 8A              TXA                         
CD6B: 48              PHA                         
CD6C: 20 87 D8        JSR     $D887               ; {}
CD6F: 68              PLA                         
CD70: AA              TAX                         
CD71: 60              RTS                         
CD72: 20 8F CD        JSR     $CD8F               ; {}
CD75: 20 C8 CE        JSR     $CEC8               ; {}
CD78: A5 14           LDA     $14                 
CD7A: 29 1F           AND     #$1F                
CD7C: D0 05           BNE     $CD83               ; {}
CD7E: A9 04           LDA     #$04                
CD80: 8D 80 03        STA     $0380               
CD83: BD 00 07        LDA     $0700,X             
CD86: C9 D0           CMP     #$D0                
CD88: 90 04           BCC     $CD8E               ; {}
CD8A: A9 D0           LDA     #$D0                
CD8C: 85 1D           STA     $1D                 
CD8E: 60              RTS                         
CD8F: EA              NOP                         
CD90: EA              NOP                         
CD91: EA              NOP                         
CD92: 20 41 CE        JSR     $CE41               ; {}
CD95: 20 6E CE        JSR     $CE6E               ; {}
CD98: 20 9E CD        JSR     $CD9E               ; {}
CD9B: 4C D3 CD        JMP     $CDD3               ; {}
CD9E: A5 16           LDA     $16                 
CDA0: 4A              LSR     A                   
CDA1: B0 14           BCS     $CDB7               ; {}
CDA3: 4A              LSR     A                   
CDA4: B0 1C           BCS     $CDC2               ; {}
CDA6: A5 1C           LDA     $1C                 
CDA8: F0 0C           BEQ     $CDB6               ; {}
CDAA: C9 FF           CMP     #$FF                
CDAC: F0 08           BEQ     $CDB6               ; {}
CDAE: A5 1C           LDA     $1C                 
CDB0: 30 0D           BMI     $CDBF               ; {}
CDB2: 10 16           BPL     $CDCA               ; {}
CDB4: C6 1C           DEC     $1C                 
CDB6: 60              RTS                         
CDB7: A5 1C           LDA     $1C                 
CDB9: 30 04           BMI     $CDBF               ; {}
CDBB: C9 08           CMP     #$08                
CDBD: B0 02           BCS     $CDC1               ; {}
CDBF: E6 1C           INC     $1C                 
CDC1: 60              RTS                         
CDC2: A5 1C           LDA     $1C                 
CDC4: 10 04           BPL     $CDCA               ; {}
CDC6: C9 F8           CMP     #$F8                
CDC8: 90 F7           BCC     $CDC1               ; {}
CDCA: C6 1C           DEC     $1C                 
CDCC: 60              RTS                         
CDCD: A5 14           LDA     $14                 
CDCF: 4A              LSR     A                   
CDD0: B0 11           BCS     $CDE3               ; {}
CDD2: 60              RTS                         
CDD3: A5 1C           LDA     $1C                 
CDD5: F0 28           BEQ     $CDFF               ; {}
CDD7: C9 FF           CMP     #$FF                
CDD9: F0 24           BEQ     $CDFF               ; {}
CDDB: C9 08           CMP     #$08                
CDDD: 90 EE           BCC     $CDCD               ; {}
CDDF: C9 F8           CMP     #$F8                
CDE1: B0 EA           BCS     $CDCD               ; {}
CDE3: A5 1C           LDA     $1C                 
CDE5: 30 19           BMI     $CE00               ; {}
CDE7: AD 2F 01        LDA     $012F               
CDEA: C9 03           CMP     #$03                
CDEC: F0 0E           BEQ     $CDFC               ; {}
CDEE: AD D5 04        LDA     $04D5               
CDF1: C9 50           CMP     #$50                
CDF3: B0 0A           BCS     $CDFF               ; {}
CDF5: AD D7 04        LDA     $04D7               
CDF8: C9 50           CMP     #$50                
CDFA: B0 03           BCS     $CDFF               ; {}
CDFC: FE 03 07        INC     $0703,X             
CDFF: 60              RTS                         
CE00: BD 03 07        LDA     $0703,X             
CE03: C9 08           CMP     #$08                
CE05: 90 F8           BCC     $CDFF               ; {}
CE07: AD 2F 01        LDA     $012F               
CE0A: C9 03           CMP     #$03                
CE0C: F0 19           BEQ     $CE27               ; {}
CE0E: AD D6 04        LDA     $04D6               
CE11: C9 50           CMP     #$50                
CE13: B0 EA           BCS     $CDFF               ; {}
CE15: AD D8 04        LDA     $04D8               
CE18: C9 50           CMP     #$50                
CE1A: B0 E3           BCS     $CDFF               ; {}
CE1C: AD 2F 01        LDA     $012F               
CE1F: 29 01           AND     #$01                
CE21: D0 04           BNE     $CE27               ; {}
CE23: DE 03 07        DEC     $0703,X             
CE26: 60              RTS                         
CE27: BD 03 07        LDA     $0703,X             
CE2A: C9 06           CMP     #$06                
CE2C: B0 F5           BCS     $CE23               ; {}
CE2E: 60              RTS                         
CE2F: A5 16           LDA     $16                 
CE31: 4A              LSR     A                   
CE32: 4A              LSR     A                   
CE33: 4A              LSR     A                   
CE34: B0 17           BCS     $CE4D               ; {}
CE36: 4A              LSR     A                   
CE37: B0 1F           BCS     $CE58               ; {}
CE39: A5 14           LDA     $14                 
CE3B: 29 10           AND     #$10                
CE3D: D0 0E           BNE     $CE4D               ; {}
CE3F: F0 17           BEQ     $CE58               ; {}
CE41: AD 2F 01        LDA     $012F               
CE44: C9 03           CMP     #$03                
CE46: F0 E7           BEQ     $CE2F               ; {}
CE48: A5 16           LDA     $16                 
CE4A: 0A              ASL     A                   
CE4B: B0 0B           BCS     $CE58               ; {}
CE4D: A5 1D           LDA     $1D                 
CE4F: 30 04           BMI     $CE55               ; {}
CE51: C9 08           CMP     #$08                
CE53: B0 02           BCS     $CE57               ; {}
CE55: E6 1D           INC     $1D                 
CE57: 60              RTS                         
CE58: A5 1D           LDA     $1D                 
CE5A: 10 04           BPL     $CE60               ; {}
CE5C: C9 F8           CMP     #$F8                
CE5E: 90 F7           BCC     $CE57               ; {}
CE60: C6 1D           DEC     $1D                 
CE62: 60              RTS                         
CE63: A9 00           LDA     #$00                
CE65: 85 1D           STA     $1D                 
CE67: 60              RTS                         
CE68: A5 14           LDA     $14                 
CE6A: 4A              LSR     A                   
CE6B: B0 11           BCS     $CE7E               ; {}
CE6D: 60              RTS                         
CE6E: A5 1D           LDA     $1D                 
CE70: F0 2B           BEQ     $CE9D               ; {}
CE72: C9 FF           CMP     #$FF                
CE74: F0 27           BEQ     $CE9D               ; {}
CE76: C9 08           CMP     #$08                
CE78: 90 EE           BCC     $CE68               ; {}
CE7A: C9 F8           CMP     #$F8                
CE7C: B0 EA           BCS     $CE68               ; {}
CE7E: A5 1D           LDA     $1D                 
CE80: 30 1C           BMI     $CE9E               ; {}
CE82: AD 2F 01        LDA     $012F               
CE85: C9 03           CMP     #$03                
CE87: F0 11           BEQ     $CE9A               ; {}
CE89: 20 87 D2        JSR     $D287               ; {}
CE8C: AD D3 04        LDA     $04D3               
CE8F: C9 40           CMP     #$40                
CE91: B0 0A           BCS     $CE9D               ; {}
CE93: AD D4 04        LDA     $04D4               
CE96: C9 40           CMP     #$40                
CE98: B0 03           BCS     $CE9D               ; {}
CE9A: FE 00 07        INC     $0700,X             
CE9D: 60              RTS                         
CE9E: AD 2F 01        LDA     $012F               
CEA1: C9 03           CMP     #$03                
CEA3: F0 07           BEQ     $CEAC               ; {}
CEA5: AD D9 04        LDA     $04D9               
CEA8: C9 50           CMP     #$50                
CEAA: B0 04           BCS     $CEB0               ; {}
CEAC: DE 00 07        DEC     $0700,X             
CEAF: 60              RTS                         
CEB0: A9 10           LDA     #$10                
CEB2: 85 1D           STA     $1D                 
CEB4: BD 00 07        LDA     $0700,X             
CEB7: 18              CLC                         
CEB8: 69 04           ADC     #$04                
CEBA: 9D 00 07        STA     $0700,X             
CEBD: 60              RTS                         
CEBE: A5 14           LDA     $14                 
CEC0: 29 08           AND     #$08                
CEC2: D0 1D           BNE     $CEE1               ; {}
CEC4: A0 0A           LDY     #$0A                
CEC6: D0 19           BNE     $CEE1               ; {}
CEC8: AD 2F 01        LDA     $012F               
CECB: C9 03           CMP     #$03                
CECD: F0 1E           BEQ     $CEED               ; {}
CECF: A0 08           LDY     #$08                
CED1: A5 1D           LDA     $1D                 
CED3: 10 0C           BPL     $CEE1               ; {}
CED5: C9 F0           CMP     #$F0                
CED7: B0 E5           BCS     $CEBE               ; {}
CED9: A5 14           LDA     $14                 
CEDB: 29 10           AND     #$10                
CEDD: D0 02           BNE     $CEE1               ; {}
CEDF: A0 0A           LDY     #$0A                
CEE1: A5 1C           LDA     $1C                 
CEE3: 30 01           BMI     $CEE6               ; {}
CEE5: C8              INY                         
CEE6: 98              TYA                         
CEE7: 20 F0 D2        JSR     $D2F0               ; {}
CEEA: 4C EF CF        JMP     $CFEF               ; {}
CEED: A9 00           LDA     #$00                
CEEF: A4 1C           LDY     $1C                 
CEF1: 30 02           BMI     $CEF5               ; {}
CEF3: A9 01           LDA     #$01                
CEF5: 20 8C D3        JSR     $D38C               ; {}
CEF8: A0 28           LDY     #$28                
CEFA: A5 1D           LDA     $1D                 
CEFC: 10 17           BPL     $CF15               ; {}
CEFE: C9 F0           CMP     #$F0                
CF00: 90 0B           BCC     $CF0D               ; {}
CF02: A5 14           LDA     $14                 
CF04: 29 08           AND     #$08                
CF06: D0 0D           BNE     $CF15               ; {}
CF08: A0 2A           LDY     #$2A                
CF0A: 4C 15 CF        JMP     $CF15               ; {}
CF0D: A5 14           LDA     $14                 
CF0F: 29 10           AND     #$10                
CF11: D0 02           BNE     $CF15               ; {}
CF13: A0 2A           LDY     #$2A                
CF15: A5 1C           LDA     $1C                 
CF17: 30 01           BMI     $CF1A               ; {}
CF19: C8              INY                         
CF1A: 98              TYA                         
CF1B: 20 CD C4        JSR     $C4CD               ; {}
CF1E: A5 1C           LDA     $1C                 
CF20: 10 13           BPL     $CF35               ; {}
CF22: BD 10 02        LDA     $0210,X             
CF25: 38              SEC                         
CF26: E9 10           SBC     #$10                
CF28: 9D 10 02        STA     $0210,X             
CF2B: BD 13 02        LDA     $0213,X             
CF2E: 18              CLC                         
CF2F: 69 10           ADC     #$10                
CF31: 9D 13 02        STA     $0213,X             
CF34: 60              RTS                         
CF35: BD 14 02        LDA     $0214,X             
CF38: 38              SEC                         
CF39: E9 10           SBC     #$10                
CF3B: 9D 14 02        STA     $0214,X             
CF3E: BD 17 02        LDA     $0217,X             
CF41: 38              SEC                         
CF42: E9 10           SBC     #$10                
CF44: 9D 17 02        STA     $0217,X             
CF47: 60              RTS                         
CF48: A5 1F           LDA     $1F                 
CF4A: D0 0B           BNE     $CF57               ; {}
CF4C: A5 18           LDA     $18                 
CF4E: 0A              ASL     A                   
CF4F: 0A              ASL     A                   
CF50: 90 13           BCC     $CF65               ; {}
CF52: A9 10           LDA     #$10                
CF54: 85 1F           STA     $1F                 
CF56: 60              RTS                         
CF57: AD 2F 01        LDA     $012F               
CF5A: C9 03           CMP     #$03                
CF5C: D0 05           BNE     $CF63               ; {}
CF5E: A5 14           LDA     $14                 
CF60: 4A              LSR     A                   
CF61: 90 02           BCC     $CF65               ; {}
CF63: C6 1F           DEC     $1F                 
CF65: 60              RTS                         
CF66: AD D5 04        LDA     $04D5               
CF69: 29 F8           AND     #$F8                
CF6B: C9 38           CMP     #$38                
CF6D: F0 05           BEQ     $CF74               ; {}
CF6F: C9 30           CMP     #$30                
CF71: F0 1E           BEQ     $CF91               ; {}
CF73: 60              RTS                         
CF74: A5 14           LDA     $14                 
CF76: 29 1F           AND     #$1F                
CF78: D0 F9           BNE     $CF73               ; {}
CF7A: A5 AA           LDA     $AA                 
CF7C: 18              CLC                         
CF7D: 69 01           ADC     #$01                
CF7F: 0A              ASL     A                   
CF80: 0A              ASL     A                   
CF81: 0A              ASL     A                   
CF82: 38              SEC                         
CF83: E9 01           SBC     #$01                
CF85: C5 A6           CMP     $A6                 
CF87: 90 EA           BCC     $CF73               ; {}
CF89: E6 A6           INC     $A6                 
CF8B: A9 01           LDA     #$01                
CF8D: 8D 81 03        STA     $0381               
CF90: 60              RTS                         
CF91: A5 14           LDA     $14                 
CF93: 29 1F           AND     #$1F                
CF95: D0 DC           BNE     $CF73               ; {}
CF97: 8A              TXA                         
CF98: A8              TAY                         
CF99: A9 7F           LDA     #$7F                
CF9B: 9D 08 07        STA     $0708,X             
CF9E: A9 80           LDA     #$80                
CFA0: 8D 81 03        STA     $0381               
CFA3: C6 A6           DEC     $A6                 
CFA5: 4C 69 DA        JMP     $DA69               ; {}
CFA8: 60              RTS                         
CFA9: 20 A8 CF        JSR     $CFA8               ; {}
CFAC: 20 66 CF        JSR     $CF66               ; {}
CFAF: 24 1E           BIT     $1E                 
CFB1: 30 11           BMI     $CFC4               ; {}
CFB3: 70 2F           BVS     $CFE4               ; {}
CFB5: 20 E5 D1        JSR     $D1E5               ; {}
CFB8: 20 06 D1        JSR     $D106               ; {}
CFBB: 20 CA D2        JSR     $D2CA               ; {}
CFBE: 20 E0 D2        JSR     $D2E0               ; {}
CFC1: 4C 69 D1        JMP     $D169               ; {}
CFC4: 20 39 D2        JSR     $D239               ; {}
CFC7: A0 08           LDY     #$08                
CFC9: A5 1D           LDA     $1D                 
CFCB: 30 02           BMI     $CFCF               ; {}
CFCD: A0 0E           LDY     #$0E                
CFCF: A5 1C           LDA     $1C                 
CFD1: 30 01           BMI     $CFD4               ; {}
CFD3: C8              INY                         
CFD4: 98              TYA                         
CFD5: 20 E0 D2        JSR     $D2E0               ; {}
CFD8: 20 EF CF        JSR     $CFEF               ; {}
CFDB: 20 5B D1        JSR     $D15B               ; {}
CFDE: 20 0C D0        JSR     $D00C               ; {}
CFE1: 4C 9E D2        JMP     $D29E               ; {}
CFE4: 20 39 D2        JSR     $D239               ; {}
CFE7: A9 00           LDA     #$00                
CFE9: 20 C5 C6        JSR     $C6C5               ; {}
CFEC: 4C DB CF        JMP     $CFDB               ; {}
CFEF: A9 02           LDA     #$02                
CFF1: 24 1C           BIT     $1C                 
CFF3: 10 02           BPL     $CFF7               ; {}
CFF5: A9 FE           LDA     #$FE                
CFF7: 85 00           STA     $00                 ; {ram.GP_00}
CFF9: BD 03 02        LDA     $0203,X             
CFFC: 18              CLC                         
CFFD: 65 00           ADC     $00                 ; {ram.GP_00}
CFFF: 9D 03 02        STA     $0203,X             
D002: BD 07 02        LDA     $0207,X             
D005: 18              CLC                         
D006: 65 00           ADC     $00                 ; {ram.GP_00}
D008: 9D 07 02        STA     $0207,X             
D00B: 60              RTS                         
D00C: 20 0F 7F        JSR     $7F0F               
D00F: A5 1C           LDA     $1C                 
D011: C9 FE           CMP     #$FE                
D013: B0 1B           BCS     $D030               ; {}
D015: C9 02           CMP     #$02                
D017: 90 17           BCC     $D030               ; {}
D019: C9 F8           CMP     #$F8                
D01B: B0 17           BCS     $D034               ; {}
D01D: C9 08           CMP     #$08                
D01F: 90 06           BCC     $D027               ; {}
D021: C9 80           CMP     #$80                
D023: B0 0C           BCS     $D031               ; {}
D025: 90 06           BCC     $D02D               ; {}
D027: A5 14           LDA     $14                 
D029: 29 01           AND     #$01                
D02B: D0 03           BNE     $D030               ; {}
D02D: 20 85 D1        JSR     $D185               ; {}
D030: 60              RTS                         
D031: 4C B9 D1        JMP     $D1B9               ; {}
D034: A5 14           LDA     $14                 
D036: 29 01           AND     #$01                
D038: D0 F6           BNE     $D030               ; {}
D03A: F0 F5           BEQ     $D031               ; {}
D03C: A9 FF           LDA     #$FF                
D03E: D0 10           BNE     $D050               ; {}
D040: A9 FF           LDA     #$FF                
D042: D0 02           BNE     $D046               ; {}
D044: A9 00           LDA     #$00                
D046: 85 1C           STA     $1C                 
D048: DE 03 07        DEC     $0703,X             
D04B: 68              PLA                         
D04C: 68              PLA                         
D04D: 60              RTS                         
D04E: A9 00           LDA     #$00                
D050: 85 1C           STA     $1C                 
D052: FE 03 07        INC     $0703,X             
D055: 68              PLA                         
D056: 68              PLA                         
D057: 60              RTS                         
D058: A9 4F           LDA     #$4F                
D05A: CD D5 04        CMP     $04D5               
D05D: 90 24           BCC     $D083               ; {}
D05F: CD D6 04        CMP     $04D6               
D062: 90 23           BCC     $D087               ; {}
D064: A9 70           LDA     #$70                
D066: CD D5 04        CMP     $04D5               
D069: B0 17           BCS     $D082               ; {}
D06B: CD D6 04        CMP     $04D6               
D06E: B0 12           BCS     $D082               ; {}
D070: A5 16           LDA     $16                 
D072: 29 04           AND     #$04                
D074: D0 0C           BNE     $D082               ; {}
D076: A9 4F           LDA     #$4F                
D078: CD D7 04        CMP     $04D7               
D07B: 90 06           BCC     $D083               ; {}
D07D: CD D8 04        CMP     $04D8               
D080: 90 05           BCC     $D087               ; {}
D082: 60              RTS                         
D083: DE 03 07        DEC     $0703,X             
D086: 60              RTS                         
D087: FE 03 07        INC     $0703,X             
D08A: 60              RTS                         
D08B: A5 16           LDA     $16                 
D08D: 4A              LSR     A                   
D08E: B0 2D           BCS     $D0BD               ; {}
D090: 4A              LSR     A                   
D091: B0 46           BCS     $D0D9               ; {}
D093: A5 1C           LDA     $1C                 
D095: F0 14           BEQ     $D0AB               ; {}
D097: C9 FF           CMP     #$FF                
D099: F0 1C           BEQ     $D0B7               ; {}
D09B: C9 30           CMP     #$30                
D09D: 90 0A           BCC     $D0A9               ; {}
D09F: C9 D0           CMP     #$D0                
D0A1: B0 12           BCS     $D0B5               ; {}
D0A3: A5 1C           LDA     $1C                 
D0A5: 30 1E           BMI     $D0C5               ; {}
D0A7: 10 38           BPL     $D0E1               ; {}
D0A9: C6 1C           DEC     $1C                 
D0AB: 68              PLA                         
D0AC: 68              PLA                         
D0AD: A9 07           LDA     #$07                
D0AF: 20 E0 D2        JSR     $D2E0               ; {}
D0B2: 4C 64 D1        JMP     $D164               ; {}
D0B5: E6 1C           INC     $1C                 
D0B7: 68              PLA                         
D0B8: 68              PLA                         
D0B9: A9 06           LDA     #$06                
D0BB: D0 F2           BNE     $D0AF               ; {}
D0BD: A5 1C           LDA     $1C                 
D0BF: 30 07           BMI     $D0C8               ; {}
D0C1: C9 40           CMP     #$40                
D0C3: B0 02           BCS     $D0C7               ; {}
D0C5: E6 1C           INC     $1C                 
D0C7: 60              RTS                         
D0C8: 68              PLA                         
D0C9: 68              PLA                         
D0CA: E6 1C           INC     $1C                 
D0CC: E6 1C           INC     $1C                 
D0CE: 20 CA D2        JSR     $D2CA               ; {}
D0D1: 49 01           EOR     #$01                
D0D3: 20 E0 D2        JSR     $D2E0               ; {}
D0D6: 4C 64 D1        JMP     $D164               ; {}
D0D9: A5 1C           LDA     $1C                 
D0DB: 10 07           BPL     $D0E4               ; {}
D0DD: C9 C0           CMP     #$C0                
D0DF: 90 E6           BCC     $D0C7               ; {}
D0E1: C6 1C           DEC     $1C                 
D0E3: 60              RTS                         
D0E4: 68              PLA                         
D0E5: 68              PLA                         
D0E6: C6 1C           DEC     $1C                 
D0E8: C6 1C           DEC     $1C                 
D0EA: 4C CE D0        JMP     $D0CE               ; {}
D0ED: A5 1C           LDA     $1C                 
D0EF: C9 08           CMP     #$08                
D0F1: 90 06           BCC     $D0F9               ; {}
D0F3: 30 05           BMI     $D0FA               ; {}
D0F5: A9 08           LDA     #$08                
D0F7: 85 1C           STA     $1C                 
D0F9: 60              RTS                         
D0FA: C9 F8           CMP     #$F8                
D0FC: B0 FB           BCS     $D0F9               ; {}
D0FE: A9 F8           LDA     #$F8                
D100: 85 1C           STA     $1C                 
D102: 60              RTS                         
D103: 4C 8B D0        JMP     $D08B               ; {}
D106: AD D3 04        LDA     $04D3               
D109: 29 F8           AND     #$F8                
D10B: C9 48           CMP     #$48                
D10D: F0 F4           BEQ     $D103               ; {}
D10F: AD D4 04        LDA     $04D4               
D112: 29 F8           AND     #$F8                
D114: C9 48           CMP     #$48                
D116: F0 EB           BEQ     $D103               ; {}
D118: 20 ED D0        JSR     $D0ED               ; {}
D11B: A5 16           LDA     $16                 
D11D: 4A              LSR     A                   
D11E: B0 25           BCS     $D145               ; {}
D120: 4A              LSR     A                   
D121: B0 2D           BCS     $D150               ; {}
D123: A5 1C           LDA     $1C                 
D125: F0 18           BEQ     $D13F               ; {}
D127: C9 FF           CMP     #$FF                
D129: F0 17           BEQ     $D142               ; {}
D12B: C9 02           CMP     #$02                
D12D: 90 0A           BCC     $D139               ; {}
D12F: C9 FE           CMP     #$FE                
D131: B0 09           BCS     $D13C               ; {}
D133: A5 1C           LDA     $1C                 
D135: 30 16           BMI     $D14D               ; {}
D137: 10 1F           BPL     $D158               ; {}
D139: 4C A9 D0        JMP     $D0A9               ; {}
D13C: 4C B5 D0        JMP     $D0B5               ; {}
D13F: 4C AB D0        JMP     $D0AB               ; {}
D142: 4C B7 D0        JMP     $D0B7               ; {}
D145: A5 1C           LDA     $1C                 
D147: 30 04           BMI     $D14D               ; {}
D149: C9 08           CMP     #$08                
D14B: B0 02           BCS     $D14F               ; {}
D14D: E6 1C           INC     $1C                 
D14F: 60              RTS                         
D150: A5 1C           LDA     $1C                 
D152: 10 04           BPL     $D158               ; {}
D154: C9 F8           CMP     #$F8                
D156: 90 F7           BCC     $D14F               ; {}
D158: C6 1C           DEC     $1C                 
D15A: 60              RTS                         
D15B: A5 16           LDA     $16                 
D15D: 4A              LSR     A                   
D15E: B0 E5           BCS     $D145               ; {}
D160: 4A              LSR     A                   
D161: B0 ED           BCS     $D150               ; {}
D163: 60              RTS                         
D164: A5 14           LDA     $14                 
D166: 4A              LSR     A                   
D167: B0 18           BCS     $D181               ; {}
D169: 20 58 D0        JSR     $D058               ; {}
D16C: A5 16           LDA     $16                 
D16E: 29 08           AND     #$08                
D170: D0 0F           BNE     $D181               ; {}
D172: A5 1C           LDA     $1C                 
D174: F0 0B           BEQ     $D181               ; {}
D176: C9 FF           CMP     #$FF                
D178: F0 07           BEQ     $D181               ; {}
D17A: A5 1C           LDA     $1C                 
D17C: 30 04           BMI     $D182               ; {}
D17E: 20 85 D1        JSR     $D185               ; {}
D181: 60              RTS                         
D182: 4C B9 D1        JMP     $D1B9               ; {}
D185: AD D5 04        LDA     $04D5               
D188: C9 50           CMP     #$50                
D18A: B0 25           BCS     $D1B1               ; {}
D18C: AD D7 04        LDA     $04D7               
D18F: C9 70           CMP     #$70                
D191: B0 04           BCS     $D197               ; {}
D193: C9 50           CMP     #$50                
D195: B0 1B           BCS     $D1B2               ; {}
D197: FE 03 07        INC     $0703,X             
D19A: A5 3A           LDA     $3A                 
D19C: F0 13           BEQ     $D1B1               ; {}
D19E: C9 10           CMP     #$10                
D1A0: B0 0F           BCS     $D1B1               ; {}
D1A2: A5 1E           LDA     $1E                 
D1A4: D0 0B           BNE     $D1B1               ; {}
D1A6: A5 14           LDA     $14                 
D1A8: 29 0F           AND     #$0F                
D1AA: D0 05           BNE     $D1B1               ; {}
D1AC: A9 08           LDA     #$08                
D1AE: 8D 80 03        STA     $0380               
D1B1: 60              RTS                         
D1B2: A5 16           LDA     $16                 
D1B4: 29 04           AND     #$04                
D1B6: D0 DF           BNE     $D197               ; {}
D1B8: 60              RTS                         
D1B9: AD D6 04        LDA     $04D6               
D1BC: C9 50           CMP     #$50                
D1BE: B0 F1           BCS     $D1B1               ; {}
D1C0: AD D8 04        LDA     $04D8               
D1C3: C9 70           CMP     #$70                
D1C5: B0 11           BCS     $D1D8               ; {}
D1C7: C9 50           CMP     #$50                
D1C9: B0 13           BCS     $D1DE               ; {}
D1CB: AD 2F 01        LDA     $012F               
D1CE: 4A              LSR     A                   
D1CF: 90 07           BCC     $D1D8               ; {}
D1D1: BD 03 07        LDA     $0703,X             
D1D4: C9 06           CMP     #$06                
D1D6: 90 D9           BCC     $D1B1               ; {}
D1D8: DE 03 07        DEC     $0703,X             
D1DB: 4C 9A D1        JMP     $D19A               ; {}
D1DE: A5 16           LDA     $16                 
D1E0: 29 04           AND     #$04                
D1E2: D0 F4           BNE     $D1D8               ; {}
D1E4: 60              RTS                         
D1E5: A5 16           LDA     $16                 
D1E7: 4A              LSR     A                   
D1E8: 4A              LSR     A                   
D1E9: 4A              LSR     A                   
D1EA: B0 2D           BCS     $D219               ; {}
D1EC: 4A              LSR     A                   
D1ED: B0 20           BCS     $D20F               ; {}
D1EF: AD D3 04        LDA     $04D3               
D1F2: C9 40           CMP     #$40                
D1F4: B0 07           BCS     $D1FD               ; {}
D1F6: AD D4 04        LDA     $04D4               
D1F9: C9 40           CMP     #$40                
D1FB: 90 13           BCC     $D210               ; {}
D1FD: A5 18           LDA     $18                 
D1FF: 0A              ASL     A                   
D200: 90 0D           BCC     $D20F               ; {}
D202: A9 E5           LDA     #$E5                
D204: 85 1D           STA     $1D                 
D206: A9 80           LDA     #$80                
D208: 85 1E           STA     $1E                 
D20A: A9 02           LDA     #$02                
D20C: 8D 81 03        STA     $0381               
D20F: 60              RTS                         
D210: A9 00           LDA     #$00                
D212: 85 1D           STA     $1D                 
D214: A9 80           LDA     #$80                
D216: 85 1E           STA     $1E                 
D218: 60              RTS                         
D219: AD D3 04        LDA     $04D3               
D21C: C9 50           CMP     #$50                
D21E: B0 EF           BCS     $D20F               ; {}
D220: AD D4 04        LDA     $04D4               
D223: C9 50           CMP     #$50                
D225: B0 E8           BCS     $D20F               ; {}
D227: BD 00 07        LDA     $0700,X             
D22A: 18              CLC                         
D22B: 69 04           ADC     #$04                
D22D: 9D 00 07        STA     $0700,X             
D230: A9 00           LDA     #$00                
D232: 85 1D           STA     $1D                 
D234: A9 40           LDA     #$40                
D236: 85 1E           STA     $1E                 
D238: 60              RTS                         
D239: A5 1D           LDA     $1D                 
D23B: 10 2F           BPL     $D26C               ; {}
D23D: BD 00 07        LDA     $0700,X             
D240: C9 0C           CMP     #$0C                
D242: 90 23           BCC     $D267               ; {}
D244: AD D9 04        LDA     $04D9               
D247: C9 70           CMP     #$70                
D249: B0 0F           BCS     $D25A               ; {}
D24B: C9 50           CMP     #$50                
D24D: B0 18           BCS     $D267               ; {}
D24F: A5 16           LDA     $16                 
D251: 29 80           AND     #$80                
D253: D0 02           BNE     $D257               ; {}
D255: E6 1D           INC     $1D                 
D257: E6 1D           INC     $1D                 
D259: 60              RTS                         
D25A: BD 00 07        LDA     $0700,X             
D25D: 18              CLC                         
D25E: 69 08           ADC     #$08                
D260: 18              CLC                         
D261: 65 FD           ADC     $FD                 
D263: 29 0C           AND     #$0C                
D265: D0 E8           BNE     $D24F               ; {}
D267: A9 00           LDA     #$00                
D269: 85 1D           STA     $1D                 
D26B: 60              RTS                         
D26C: AD D3 04        LDA     $04D3               
D26F: C9 FF           CMP     #$FF                
D271: F0 24           BEQ     $D297               ; {}
D273: C9 40           CMP     #$40                
D275: B0 1B           BCS     $D292               ; {}
D277: AD D4 04        LDA     $04D4               
D27A: C9 40           CMP     #$40                
D27C: B0 14           BCS     $D292               ; {}
D27E: A5 1D           LDA     $1D                 
D280: C9 60           CMP     #$60                
D282: B0 02           BCS     $D286               ; {}
D284: E6 1D           INC     $1D                 
D286: 60              RTS                         
D287: BD 00 07        LDA     $0700,X             
D28A: 18              CLC                         
D28B: 65 FD           ADC     $FD                 
D28D: 29 0C           AND     #$0C                
D28F: C9 08           CMP     #$08                
D291: 60              RTS                         
D292: 20 87 D2        JSR     $D287               ; {}
D295: D0 E7           BNE     $D27E               ; {}
D297: A9 00           LDA     #$00                
D299: 85 1E           STA     $1E                 
D29B: 85 1D           STA     $1D                 
D29D: 60              RTS                         
D29E: A5 1D           LDA     $1D                 
D2A0: 10 12           BPL     $D2B4               ; {}
D2A2: C9 F8           CMP     #$F8                
D2A4: B0 0A           BCS     $D2B0               ; {}
D2A6: C9 F0           CMP     #$F0                
D2A8: B0 03           BCS     $D2AD               ; {}
D2AA: DE 00 07        DEC     $0700,X             
D2AD: DE 00 07        DEC     $0700,X             
D2B0: DE 00 07        DEC     $0700,X             
D2B3: 60              RTS                         
D2B4: C9 08           CMP     #$08                
D2B6: 90 11           BCC     $D2C9               ; {}
D2B8: C9 10           CMP     #$10                
D2BA: 90 0A           BCC     $D2C6               ; {}
D2BC: C9 18           CMP     #$18                
D2BE: 90 03           BCC     $D2C3               ; {}
D2C0: FE 00 07        INC     $0700,X             
D2C3: FE 00 07        INC     $0700,X             
D2C6: FE 00 07        INC     $0700,X             
D2C9: 60              RTS                         
D2CA: A5 14           LDA     $14                 
D2CC: 4A              LSR     A                   
D2CD: 4A              LSR     A                   
D2CE: 29 03           AND     #$03                
D2D0: A8              TAY                         
D2D1: B9 DC D2        LDA     $D2DC,Y             ; {}
D2D4: A8              TAY                         
D2D5: 24 1C           BIT     $1C                 
D2D7: 30 01           BMI     $D2DA               ; {}
D2D9: C8              INY                         
D2DA: 98              TYA                         
D2DB: 60              RTS                         
D2DC: 00              BRK                         
D2DD: 02 ; ????
D2DE: 04 ; ????
D2DF: 02 ; ????
D2E0: 48              PHA                         
D2E1: A5 16           LDA     $16                 
D2E3: 4A              LSR     A                   
D2E4: 4A              LSR     A                   
D2E5: 4A              LSR     A                   
D2E6: B0 50           BCS     $D338               ; {}
D2E8: 4A              LSR     A                   
D2E9: 90 06           BCC     $D2F1               ; {}
D2EB: 68              PLA                         
D2EC: 29 01           AND     #$01                
D2EE: 09 0C           ORA     #$0C                
D2F0: 48              PHA                         
D2F1: A5 1F           LDA     $1F                 
D2F3: D0 37           BNE     $D32C               ; {}
D2F5: 68              PLA                         
D2F6: 48              PHA                         
D2F7: 20 CD C4        JSR     $C4CD               ; {}
D2FA: 68              PLA                         
D2FB: C9 02           CMP     #$02                
D2FD: F0 05           BEQ     $D304               ; {}
D2FF: C9 03           CMP     #$03                
D301: F0 15           BEQ     $D318               ; {}
D303: 60              RTS                         
D304: 8A              TXA                         
D305: 48              PHA                         
D306: A0 03           LDY     #$03                
D308: FE 00 02        INC     $0200,X             
D30B: DE 03 02        DEC     $0203,X             
D30E: E8              INX                         
D30F: E8              INX                         
D310: E8              INX                         
D311: E8              INX                         
D312: 88              DEY                         
D313: 10 F3           BPL     $D308               ; {}
D315: 68              PLA                         
D316: AA              TAX                         
D317: 60              RTS                         
D318: 8A              TXA                         
D319: 48              PHA                         
D31A: A0 03           LDY     #$03                
D31C: FE 00 02        INC     $0200,X             
D31F: FE 03 02        INC     $0203,X             
D322: E8              INX                         
D323: E8              INX                         
D324: E8              INX                         
D325: E8              INX                         
D326: 88              DEY                         
D327: 10 F3           BPL     $D31C               ; {}
D329: 68              PLA                         
D32A: AA              TAX                         
D32B: 60              RTS                         
D32C: 68              PLA                         
D32D: 48              PHA                         
D32E: 20 5A D3        JSR     $D35A               ; {}
D331: 68              PLA                         
D332: 09 10           ORA     #$10                
D334: 20 CD C4        JSR     $C4CD               ; {}
D337: 60              RTS                         
D338: 68              PLA                         
D339: A9 00           LDA     #$00                
D33B: 20 C5 C6        JSR     $C6C5               ; {}
D33E: A9 00           LDA     #$00                
D340: 85 1F           STA     $1F                 
D342: 60              RTS                         
D343: A2 38           LDX     #$38                
D345: 20 4A D3        JSR     $D34A               ; {}
D348: A2 3C           LDX     #$3C                
D34A: A9 F8           LDA     #$F8                
D34C: 9D 00 07        STA     $0700,X             
D34F: A9 00           LDA     #$00                
D351: 9D 01 07        STA     $0701,X             
D354: 60              RTS                         
D355: A5 A5           LDA     $A5                 
D357: 29 07           AND     #$07                
D359: 60              RTS                         
D35A: 48              PHA                         
D35B: 20 8C D3        JSR     $D38C               ; {}
D35E: 20 55 D3        JSR     $D355               ; {}
D361: 20 2B EE        JSR     $EE2B               ; {}
D364: A1 D3           LDA     ($D3,X)             
D366: E1 D3           SBC     ($D3,X)             
D368: A1 D3           LDA     ($D3,X)             
D36A: E1 D3           SBC     ($D3,X)             
D36C: A1 D3           LDA     ($D3,X)             
D36E: E1 D3           SBC     ($D3,X)             
D370: A1 D3           LDA     ($D3,X)             
D372: E1 D3           SBC     ($D3,X)             
D374: A0 38           LDY     #$38                
D376: 68              PLA                         
D377: 29 0F           AND     #$0F                
D379: C9 0E           CMP     #$0E                
D37B: B0 04           BCS     $D381               ; {}
D37D: C9 0C           CMP     #$0C                
D37F: B0 0A           BCS     $D38B               ; {}
D381: A9 10           LDA     #$10                
D383: 99 02 07        STA     $0702,Y             
D386: A9 40           LDA     #$40                
D388: 8D 81 03        STA     $0381               
D38B: 60              RTS                         
D38C: 48              PHA                         
D38D: A5 1F           LDA     $1F                 
D38F: C9 10           CMP     #$10                
D391: D0 0E           BNE     $D3A1               ; {}
D393: A5 3C           LDA     $3C                 
D395: D0 DD           BNE     $D374               ; {}
D397: AD 39 07        LDA     $0739               
D39A: 10 07           BPL     $D3A3               ; {}
D39C: AD 3D 07        LDA     $073D               
D39F: 10 16           BPL     $D3B7               ; {}
D3A1: 68              PLA                         
D3A2: 60              RTS                         
D3A3: A0 38           LDY     #$38                
D3A5: 68              PLA                         
D3A6: 20 12 D4        JSR     $D412               ; {}
D3A9: 20 CF D3        JSR     $D3CF               ; {}
D3AC: 99 02 07        STA     $0702,Y             
D3AF: 20 BC D3        JSR     $D3BC               ; {}
D3B2: A9 00           LDA     #$00                
D3B4: 4C 37 E3        JMP     $E337               ; {}
D3B7: A0 3C           LDY     #$3C                
D3B9: 4C A5 D3        JMP     $D3A5               ; {}
D3BC: AD 2F 01        LDA     $012F               
D3BF: C9 03           CMP     #$03                
D3C1: F0 06           BEQ     $D3C9               ; {}
D3C3: A9 10           LDA     #$10                
D3C5: 8D 80 03        STA     $0380               
D3C8: 60              RTS                         
D3C9: A9 02           LDA     #$02                
D3CB: 8D 80 03        STA     $0380               
D3CE: 60              RTS                         
D3CF: A5 3A           LDA     $3A                 
D3D1: C9 10           CMP     #$10                
D3D3: B0 09           BCS     $D3DE               ; {}
D3D5: A5 A5           LDA     $A5                 
D3D7: 29 02           AND     #$02                
D3D9: F0 03           BEQ     $D3DE               ; {}
D3DB: A9 7F           LDA     #$7F                
D3DD: 60              RTS                         
D3DE: A9 10           LDA     #$10                
D3E0: 60              RTS                         
D3E1: A5 1F           LDA     $1F                 
D3E3: C9 10           CMP     #$10                
D3E5: D0 0A           BNE     $D3F1               ; {}
D3E7: AD 41 07        LDA     $0741               
D3EA: 10 07           BPL     $D3F3               ; {}
D3EC: AD 45 07        LDA     $0745               
D3EF: 10 0B           BPL     $D3FC               ; {}
D3F1: 68              PLA                         
D3F2: 60              RTS                         
D3F3: A0 40           LDY     #$40                
D3F5: 68              PLA                         
D3F6: 48              PHA                         
D3F7: 20 4A D4        JSR     $D44A               ; {}
D3FA: 68              PLA                         
D3FB: 60              RTS                         
D3FC: A0 44           LDY     #$44                
D3FE: 68              PLA                         
D3FF: 48              PHA                         
D400: 20 4A D4        JSR     $D44A               ; {}
D403: A0 3C           LDY     #$3C                
D405: 68              PLA                         
D406: 48              PHA                         
D407: 20 12 D4        JSR     $D412               ; {}
D40A: 20 CF D3        JSR     $D3CF               ; {}
D40D: 99 02 07        STA     $0702,Y             
D410: 68              PLA                         
D411: 60              RTS                         
D412: 29 0F           AND     #$0F                
D414: C9 0E           CMP     #$0E                
D416: B0 04           BCS     $D41C               ; {}
D418: C9 0C           CMP     #$0C                
D41A: B0 19           BCS     $D435               ; {}
D41C: 29 01           AND     #$01                
D41E: D0 04           BNE     $D424               ; {}
D420: A9 8C           LDA     #$8C                
D422: D0 13           BNE     $D437               ; {}
D424: A9 84           LDA     #$84                
D426: 99 01 07        STA     $0701,Y             
D429: BD 03 07        LDA     $0703,X             
D42C: 18              CLC                         
D42D: 69 04           ADC     #$04                
D42F: 99 03 07        STA     $0703,Y             
D432: 4C 40 D4        JMP     $D440               ; {}
D435: A9 80           LDA     #$80                
D437: 99 01 07        STA     $0701,Y             
D43A: BD 03 07        LDA     $0703,X             
D43D: 99 03 07        STA     $0703,Y             
D440: BD 00 07        LDA     $0700,X             
D443: 38              SEC                         
D444: E9 08           SBC     #$08                
D446: 99 00 07        STA     $0700,Y             
D449: 60              RTS                         
D44A: 29 0F           AND     #$0F                
D44C: C9 0E           CMP     #$0E                
D44E: B0 04           BCS     $D454               ; {}
D450: C9 0C           CMP     #$0C                
D452: B0 2F           BCS     $D483               ; {}
D454: 29 01           AND     #$01                
D456: D0 1D           BNE     $D475               ; {}
D458: A9 8C           LDA     #$8C                
D45A: 99 01 07        STA     $0701,Y             
D45D: BD 03 07        LDA     $0703,X             
D460: 38              SEC                         
D461: E9 08           SBC     #$08                
D463: 99 03 07        STA     $0703,Y             
D466: BD 00 07        LDA     $0700,X             
D469: 38              SEC                         
D46A: E9 08           SBC     #$08                
D46C: 99 00 07        STA     $0700,Y             
D46F: A9 00           LDA     #$00                
D471: 99 02 07        STA     $0702,Y             
D474: 60              RTS                         
D475: A9 84           LDA     #$84                
D477: 99 01 07        STA     $0701,Y             
D47A: BD 03 07        LDA     $0703,X             
D47D: 99 03 07        STA     $0703,Y             
D480: 4C 66 D4        JMP     $D466               ; {}
D483: A9 80           LDA     #$80                
D485: 99 01 07        STA     $0701,Y             
D488: BD 03 07        LDA     $0703,X             
D48B: 99 03 07        STA     $0703,Y             
D48E: BD 00 07        LDA     $0700,X             
D491: 38              SEC                         
D492: E9 18           SBC     #$18                
D494: 99 00 07        STA     $0700,Y             
D497: A9 40           LDA     #$40                
D499: 99 02 07        STA     $0702,Y             
D49C: 60              RTS                         
D49D: 20 A1 D4        JSR     $D4A1               ; {}
D4A0: 68              PLA                         
D4A1: 60              RTS                         
D4A2: AD 2F 01        LDA     $012F               
D4A5: C9 03           CMP     #$03                
D4A7: F0 48           BEQ     $D4F1               ; {}
D4A9: 20 60 D6        JSR     $D660               ; {}
D4AC: 20 55 D3        JSR     $D355               ; {}
D4AF: 20 2B EE        JSR     $EE2B               ; {}
D4B2: D2 ; ????
D4B3: D4 ; ????
D4B4: C2 ; ????
D4B5: D4 ; ????
D4B6: D2 ; ????
D4B7: D4 ; ????
D4B8: C2 ; ????
D4B9: D4 ; ????
D4BA: C8              INY                         
D4BB: D4 ; ????
D4BC: 20 D7 C8        JSR     $C8D7               ; {}
D4BF: D4 ; ????
D4C0: 20 D7 20        JSR     $20D7               
D4C3: 20 D7 4C        JSR     $4CD7               
D4C6: DC ; ????
D4C7: D4 ; ????
D4C8: A2 40           LDX     #$40                
D4CA: 20 E3 D4        JSR     $D4E3               ; {}
D4CD: A2 44           LDX     #$44                
D4CF: 4C E3 D4        JMP     $D4E3               ; {}
D4D2: A2 40           LDX     #$40                
D4D4: 20 E3 D4        JSR     $D4E3               ; {}
D4D7: A2 44           LDX     #$44                
D4D9: 20 E3 D4        JSR     $D4E3               ; {}
D4DC: A2 48           LDX     #$48                
D4DE: 20 E3 D4        JSR     $D4E3               ; {}
D4E1: A2 4C           LDX     #$4C                
D4E3: A9 00           LDA     #$00                
D4E5: 9D 01 07        STA     $0701,X             
D4E8: A9 F8           LDA     #$F8                
D4EA: 9D 00 02        STA     $0200,X             
D4ED: 9D 00 07        STA     $0700,X             
D4F0: 60              RTS                         
D4F1: 20 60 D6        JSR     $D660               ; {}
D4F4: A2 38           LDX     #$38                
D4F6: 20 01 D5        JSR     $D501               ; {}
D4F9: A2 3C           LDX     #$3C                
D4FB: 20 01 D5        JSR     $D501               ; {}
D4FE: 4C 3C D5        JMP     $D53C               ; {}
D501: BD 01 07        LDA     $0701,X             
D504: 10 30           BPL     $D536               ; {}
D506: BD 00 02        LDA     $0200,X             
D509: 9D 08 02        STA     $0208,X             
D50C: A9 7F           LDA     #$7F                
D50E: 9D 09 02        STA     $0209,X             
D511: A9 01           LDA     #$01                
D513: 9D 0A 02        STA     $020A,X             
D516: A9 7F           LDA     #$7F                
D518: 9D 01 02        STA     $0201,X             
D51B: BD 01 07        LDA     $0701,X             
D51E: 29 08           AND     #$08                
D520: F0 0A           BEQ     $D52C               ; {}
D522: BD 03 02        LDA     $0203,X             
D525: 18              CLC                         
D526: 69 08           ADC     #$08                
D528: 9D 0B 02        STA     $020B,X             
D52B: 60              RTS                         
D52C: BD 03 02        LDA     $0203,X             
D52F: 38              SEC                         
D530: E9 08           SBC     #$08                
D532: 9D 0B 02        STA     $020B,X             
D535: 60              RTS                         
D536: A9 F0           LDA     #$F0                
D538: 9D 08 02        STA     $0208,X             
D53B: 60              RTS                         
D53C: A5 1F           LDA     $1F                 
D53E: D0 4F           BNE     $D58F               ; {}
D540: 8A              TXA                         
D541: 48              PHA                         
D542: 98              TYA                         
D543: 48              PHA                         
D544: A2 20           LDX     #$20                
D546: A0 00           LDY     #$00                
D548: A5 1C           LDA     $1C                 
D54A: 10 07           BPL     $D553               ; {}
D54C: A9 F8           LDA     #$F8                
D54E: 9D 08 02        STA     $0208,X             
D551: D0 07           BNE     $D55A               ; {}
D553: A9 F8           LDA     #$F8                
D555: 9D 0C 02        STA     $020C,X             
D558: A0 08           LDY     #$08                
D55A: A9 02           LDA     #$02                
D55C: 85 00           STA     $00                 ; {ram.GP_00}
D55E: AD 20 07        LDA     $0720               
D561: 18              CLC                         
D562: 79 9E D5        ADC     $D59E,Y             ; {}
D565: 9D 28 02        STA     $0228,X             
D568: B9 9F D5        LDA     $D59F,Y             ; {}
D56B: 9D 29 02        STA     $0229,X             
D56E: B9 A0 D5        LDA     $D5A0,Y             ; {}
D571: 9D 2A 02        STA     $022A,X             
D574: AD 23 07        LDA     $0723               
D577: 18              CLC                         
D578: 79 A1 D5        ADC     $D5A1,Y             ; {}
D57B: 9D 2B 02        STA     $022B,X             
D57E: C8              INY                         
D57F: C8              INY                         
D580: C8              INY                         
D581: C8              INY                         
D582: E8              INX                         
D583: E8              INX                         
D584: E8              INX                         
D585: E8              INX                         
D586: C6 00           DEC     $00                 ; {ram.GP_00}
D588: D0 D4           BNE     $D55E               ; {}
D58A: 68              PLA                         
D58B: A8              TAY                         
D58C: 68              PLA                         
D58D: AA              TAX                         
D58E: 60              RTS                         
D58F: 8A              TXA                         
D590: 48              PHA                         
D591: A2 20           LDX     #$20                
D593: A9 F8           LDA     #$F8                
D595: 9D 28 02        STA     $0228,X             
D598: 9D 2C 02        STA     $022C,X             
D59B: 68              PLA                         
D59C: AA              TAX                         
D59D: 60              RTS                         
D59E: F8              SED                         
D59F: 9D 01 FC        STA     $FC01,X             ; {}
D5A2: 00              BRK                         
D5A3: 9E ; ????
D5A4: 01 FC           ORA     ($FC,X)             
D5A6: F8              SED                         
D5A7: 9D 41 04        STA     $0441,X             
D5AA: 00              BRK                         
D5AB: 9E ; ????
D5AC: 41 04           EOR     ($04,X)             
D5AE: 20 20 D7        JSR     $D720               ; {}
D5B1: 4C 40 D9        JMP     $D940               ; {}
D5B4: BD 02 07        LDA     $0702,X             
D5B7: F0 5C           BEQ     $D615               ; {}
D5B9: DE 02 07        DEC     $0702,X             
D5BC: A5 1C           LDA     $1C                 
D5BE: 10 3F           BPL     $D5FF               ; {}
D5C0: B9 03 07        LDA     $0703,Y             
D5C3: 38              SEC                         
D5C4: E9 10           SBC     #$10                
D5C6: 9D 03 07        STA     $0703,X             
D5C9: 9D 03 02        STA     $0203,X             
D5CC: 18              CLC                         
D5CD: 69 08           ADC     #$08                
D5CF: 9D 07 02        STA     $0207,X             
D5D2: A9 01           LDA     #$01                
D5D4: 9D 02 02        STA     $0202,X             
D5D7: 9D 06 02        STA     $0206,X             
D5DA: B9 00 07        LDA     $0700,Y             
D5DD: 38              SEC                         
D5DE: E9 08           SBC     #$08                
D5E0: 9D 00 07        STA     $0700,X             
D5E3: 9D 00 02        STA     $0200,X             
D5E6: 9D 04 02        STA     $0204,X             
D5E9: A9 AC           LDA     #$AC                
D5EB: 9D 01 02        STA     $0201,X             
D5EE: A9 AD           LDA     #$AD                
D5F0: 9D 05 02        STA     $0205,X             
D5F3: 60              RTS                         
D5F4: A2 38           LDX     #$38                
D5F6: A0 20           LDY     #$20                
D5F8: A9 80           LDA     #$80                
D5FA: 9D 01 07        STA     $0701,X             
D5FD: D0 B5           BNE     $D5B4               ; {}
D5FF: B9 03 07        LDA     $0703,Y             
D602: 18              CLC                         
D603: 69 10           ADC     #$10                
D605: 9D 03 07        STA     $0703,X             
D608: 9D 03 02        STA     $0203,X             
D60B: 38              SEC                         
D60C: E9 08           SBC     #$08                
D60E: 9D 07 02        STA     $0207,X             
D611: A9 41           LDA     #$41                
D613: D0 BF           BNE     $D5D4               ; {}
D615: A5 1C           LDA     $1C                 
D617: 10 34           BPL     $D64D               ; {}
D619: B9 03 07        LDA     $0703,Y             
D61C: 38              SEC                         
D61D: E9 06           SBC     #$06                
D61F: 9D 03 07        STA     $0703,X             
D622: 9D 03 02        STA     $0203,X             
D625: 9D 07 02        STA     $0207,X             
D628: A9 01           LDA     #$01                
D62A: 9D 02 02        STA     $0202,X             
D62D: 9D 06 02        STA     $0206,X             
D630: B9 00 07        LDA     $0700,Y             
D633: 38              SEC                         
D634: E9 16           SBC     #$16                
D636: 9D 00 07        STA     $0700,X             
D639: 9D 00 02        STA     $0200,X             
D63C: 18              CLC                         
D63D: 69 08           ADC     #$08                
D63F: 9D 04 02        STA     $0204,X             
D642: A9 AA           LDA     #$AA                
D644: 9D 01 02        STA     $0201,X             
D647: A9 AB           LDA     #$AB                
D649: 9D 05 02        STA     $0205,X             
D64C: 60              RTS                         
D64D: B9 03 07        LDA     $0703,Y             
D650: 18              CLC                         
D651: 69 06           ADC     #$06                
D653: 9D 03 07        STA     $0703,X             
D656: 9D 03 02        STA     $0203,X             
D659: 9D 07 02        STA     $0207,X             
D65C: A9 41           LDA     #$41                
D65E: D0 CA           BNE     $D62A               ; {}
D660: A5 3C           LDA     $3C                 
D662: D0 90           BNE     $D5F4               ; {}
D664: A2 38           LDX     #$38                
D666: 20 6B D6        JSR     $D66B               ; {}
D669: A2 3C           LDX     #$3C                
D66B: A9 F8           LDA     #$F8                
D66D: 9D 00 02        STA     $0200,X             
D670: BD 01 07        LDA     $0701,X             
D673: 10 27           BPL     $D69C               ; {}
D675: BD 03 07        LDA     $0703,X             
D678: C9 FC           CMP     #$FC                
D67A: B0 21           BCS     $D69D               ; {}
D67C: BD 00 07        LDA     $0700,X             
D67F: C9 F0           CMP     #$F0                
D681: B0 1A           BCS     $D69D               ; {}
D683: DE 02 07        DEC     $0702,X             
D686: 30 15           BMI     $D69D               ; {}
D688: AD 2F 01        LDA     $012F               
D68B: C9 03           CMP     #$03                
D68D: F0 07           BEQ     $D696               ; {}
D68F: 20 35 E0        JSR     $E035               ; {}
D692: C9 40           CMP     #$40                
D694: B0 07           BCS     $D69D               ; {}
D696: 20 AB D6        JSR     $D6AB               ; {}
D699: 20 F1 D6        JSR     $D6F1               ; {}
D69C: 60              RTS                         
D69D: A9 00           LDA     #$00                
D69F: 9D 01 07        STA     $0701,X             
D6A2: A9 F8           LDA     #$F8                
D6A4: 9D 00 07        STA     $0700,X             
D6A7: 9D 00 02        STA     $0200,X             
D6AA: 60              RTS                         
D6AB: BD 01 07        LDA     $0701,X             
D6AE: 29 0E           AND     #$0E                
D6B0: A8              TAY                         
D6B1: A5 A5           LDA     $A5                 
D6B3: 29 02           AND     #$02                
D6B5: F0 05           BEQ     $D6BC               ; {}
D6B7: 98              TYA                         
D6B8: 18              CLC                         
D6B9: 69 10           ADC     #$10                
D6BB: A8              TAY                         
D6BC: B9 D1 D6        LDA     $D6D1,Y             ; {}
D6BF: 18              CLC                         
D6C0: 7D 00 07        ADC     $0700,X             
D6C3: 9D 00 07        STA     $0700,X             
D6C6: B9 D2 D6        LDA     $D6D2,Y             ; {}
D6C9: 18              CLC                         
D6CA: 7D 03 07        ADC     $0703,X             
D6CD: 9D 03 07        STA     $0703,X             
D6D0: 60              RTS                         
D6D1: FD 00 FD        SBC     $FD00,X             ; {}
D6D4: 03 ; ????
D6D5: 00              BRK                         
D6D6: 03 ; ????
D6D7: 03 ; ????
D6D8: 03 ; ????
D6D9: 03 ; ????
D6DA: 00              BRK                         
D6DB: 03 ; ????
D6DC: FD 00 FD        SBC     $FD00,X             ; {}
D6DF: FD FD FC        SBC     $FCFD,X             ; {}
D6E2: 00              BRK                         
D6E3: FC ; ????
D6E4: 04 ; ????
D6E5: 00              BRK                         
D6E6: 04 ; ????
D6E7: 04 ; ????
D6E8: 04 ; ????
D6E9: 04 ; ????
D6EA: 00              BRK                         
D6EB: 04 ; ????
D6EC: FC ; ????
D6ED: 00              BRK                         
D6EE: FC ; ????
D6EF: FC ; ????
D6F0: FC ; ????
D6F1: BD 01 07        LDA     $0701,X             
D6F4: 29 0E           AND     #$0E                
D6F6: A8              TAY                         
D6F7: B9 10 D7        LDA     $D710,Y             ; {}
D6FA: 9D 01 02        STA     $0201,X             
D6FD: B9 11 D7        LDA     $D711,Y             ; {}
D700: 9D 02 02        STA     $0202,X             
D703: BD 00 07        LDA     $0700,X             
D706: 9D 00 02        STA     $0200,X             
D709: BD 03 07        LDA     $0703,X             
D70C: 9D 03 02        STA     $0203,X             
D70F: 60              RTS                         
D710: 4C 00 5C        JMP     $5C00               
D713: 40              RTI                         
D714: 3C ; ????
D715: 40              RTI                         
D716: 5C ; ????
D717: C0 4C           CPY     #$4C                
D719: 80 ; ????
D71A: 5C ; ????
D71B: 80 ; ????
D71C: 3C ; ????
D71D: 00              BRK                         
D71E: 5C ; ????
D71F: 00              BRK                         
D720: A2 40           LDX     #$40                
D722: A0 38           LDY     #$38                
D724: 20 2B D7        JSR     $D72B               ; {}
D727: A2 44           LDX     #$44                
D729: A0 3C           LDY     #$3C                
D72B: A5 3A           LDA     $3A                 
D72D: C9 10           CMP     #$10                
D72F: B0 2B           BCS     $D75C               ; {}
D731: BD 01 07        LDA     $0701,X             
D734: 10 29           BPL     $D75F               ; {}
D736: B9 01 07        LDA     $0701,Y             
D739: 10 21           BPL     $D75C               ; {}
D73B: BD 03 07        LDA     $0703,X             
D73E: C9 F8           CMP     #$F8                
D740: B0 1A           BCS     $D75C               ; {}
D742: BD 00 07        LDA     $0700,X             
D745: C9 F0           CMP     #$F0                
D747: B0 13           BCS     $D75C               ; {}
D749: 20 00 D8        JSR     $D800               ; {}
D74C: BD 02 07        LDA     $0702,X             
D74F: 18              CLC                         
D750: 69 10           ADC     #$10                
D752: 9D 02 07        STA     $0702,X             
D755: 20 B2 D7        JSR     $D7B2               ; {}
D758: 20 5B D8        JSR     $D85B               ; {}
D75B: 60              RTS                         
D75C: 4C 9D D6        JMP     $D69D               ; {}
D75F: A5 14           LDA     $14                 
D761: 4A              LSR     A                   
D762: 29 06           AND     #$06                
D764: A8              TAY                         
D765: B9 7F D8        LDA     $D87F,Y             ; {}
D768: 24 1F           BIT     $1F                 
D76A: F0 02           BEQ     $D76E               ; {}
D76C: A9 5F           LDA     #$5F                
D76E: 9D 01 02        STA     $0201,X             
D771: B9 80 D8        LDA     $D880,Y             ; {}
D774: 9D 02 02        STA     $0202,X             
D777: A5 16           LDA     $16                 
D779: 29 08           AND     #$08                
D77B: D0 21           BNE     $D79E               ; {}
D77D: AD 20 07        LDA     $0720               
D780: 38              SEC                         
D781: E9 08           SBC     #$08                
D783: 9D 00 02        STA     $0200,X             
D786: A5 1C           LDA     $1C                 
D788: 30 0A           BMI     $D794               ; {}
D78A: AD 23 07        LDA     $0723               
D78D: 18              CLC                         
D78E: 69 0A           ADC     #$0A                
D790: 9D 03 02        STA     $0203,X             
D793: 60              RTS                         
D794: AD 23 07        LDA     $0723               
D797: 38              SEC                         
D798: E9 0A           SBC     #$0A                
D79A: 9D 03 02        STA     $0203,X             
D79D: 60              RTS                         
D79E: A5 A5           LDA     $A5                 
D7A0: 30 DB           BMI     $D77D               ; {}
D7A2: AD 20 07        LDA     $0720               
D7A5: 38              SEC                         
D7A6: E9 18           SBC     #$18                
D7A8: 9D 00 02        STA     $0200,X             
D7AB: AD 23 07        LDA     $0723               
D7AE: 9D 03 02        STA     $0203,X             
D7B1: 60              RTS                         
D7B2: BD 01 07        LDA     $0701,X             
D7B5: 29 0F           AND     #$0F                
D7B7: C9 03           CMP     #$03                
D7B9: 90 0C           BCC     $D7C7               ; {}
D7BB: C9 07           CMP     #$07                
D7BD: 90 1B           BCC     $D7DA               ; {}
D7BF: C9 0B           CMP     #$0B                
D7C1: 90 29           BCC     $D7EC               ; {}
D7C3: C9 0E           CMP     #$0E                
D7C5: 90 26           BCC     $D7ED               ; {}
D7C7: A5 A5           LDA     $A5                 
D7C9: 29 02           AND     #$02                
D7CB: F0 03           BEQ     $D7D0               ; {}
D7CD: DE 00 07        DEC     $0700,X             
D7D0: DE 00 07        DEC     $0700,X             
D7D3: DE 00 07        DEC     $0700,X             
D7D6: DE 00 07        DEC     $0700,X             
D7D9: 60              RTS                         
D7DA: A5 A5           LDA     $A5                 
D7DC: 29 02           AND     #$02                
D7DE: F0 03           BEQ     $D7E3               ; {}
D7E0: FE 03 07        INC     $0703,X             
D7E3: FE 03 07        INC     $0703,X             
D7E6: FE 03 07        INC     $0703,X             
D7E9: FE 03 07        INC     $0703,X             
D7EC: 60              RTS                         
D7ED: A5 A5           LDA     $A5                 
D7EF: 29 02           AND     #$02                
D7F1: F0 03           BEQ     $D7F6               ; {}
D7F3: DE 03 07        DEC     $0703,X             
D7F6: DE 03 07        DEC     $0703,X             
D7F9: DE 03 07        DEC     $0703,X             
D7FC: DE 03 07        DEC     $0703,X             
D7FF: 60              RTS                         
D800: BD 02 07        LDA     $0702,X             
D803: C9 C0           CMP     #$C0                
D805: B0 41           BCS     $D848               ; {}
D807: C9 80           CMP     #$80                
D809: B0 2A           BCS     $D835               ; {}
D80B: C9 40           CMP     #$40                
D80D: B0 13           BCS     $D822               ; {}
D80F: BD 00 07        LDA     $0700,X             
D812: 38              SEC                         
D813: E9 04           SBC     #$04                
D815: 9D 00 07        STA     $0700,X             
D818: BD 03 07        LDA     $0703,X             
D81B: 18              CLC                         
D81C: 69 02           ADC     #$02                
D81E: 9D 03 07        STA     $0703,X             
D821: 60              RTS                         
D822: BD 00 07        LDA     $0700,X             
D825: 18              CLC                         
D826: 69 04           ADC     #$04                
D828: 9D 00 07        STA     $0700,X             
D82B: BD 03 07        LDA     $0703,X             
D82E: 18              CLC                         
D82F: 69 02           ADC     #$02                
D831: 9D 03 07        STA     $0703,X             
D834: 60              RTS                         
D835: BD 00 07        LDA     $0700,X             
D838: 18              CLC                         
D839: 69 04           ADC     #$04                
D83B: 9D 00 07        STA     $0700,X             
D83E: BD 03 07        LDA     $0703,X             
D841: 38              SEC                         
D842: E9 02           SBC     #$02                
D844: 9D 03 07        STA     $0703,X             
D847: 60              RTS                         
D848: BD 00 07        LDA     $0700,X             
D84B: 38              SEC                         
D84C: E9 04           SBC     #$04                
D84E: 9D 00 07        STA     $0700,X             
D851: BD 03 07        LDA     $0703,X             
D854: 38              SEC                         
D855: E9 02           SBC     #$02                
D857: 9D 03 07        STA     $0703,X             
D85A: 60              RTS                         
D85B: BD 02 07        LDA     $0702,X             
D85E: 4A              LSR     A                   
D85F: 4A              LSR     A                   
D860: 4A              LSR     A                   
D861: 4A              LSR     A                   
D862: 4A              LSR     A                   
D863: 4A              LSR     A                   
D864: 0A              ASL     A                   
D865: A8              TAY                         
D866: B9 7F D8        LDA     $D87F,Y             ; {}
D869: 9D 01 02        STA     $0201,X             
D86C: B9 80 D8        LDA     $D880,Y             ; {}
D86F: 9D 02 02        STA     $0202,X             
D872: BD 00 07        LDA     $0700,X             
D875: 9D 00 02        STA     $0200,X             
D878: BD 03 07        LDA     $0703,X             
D87B: 9D 03 02        STA     $0203,X             
D87E: 60              RTS                         
D87F: 3B ; ????
D880: 01 3A           ORA     ($3A,X)             
D882: C1 3B           CMP     ($3B,X)             
D884: C1 3A           CMP     ($3A,X)             
D886: 01 A2           ORA     ($A2,X)             
D888: 48              PHA                         
D889: A0 00           LDY     #$00                
D88B: A9 F0           LDA     #$F0                
D88D: 20 96 D8        JSR     $D896               ; {}
D890: A2 4C           LDX     #$4C                
D892: A0 0C           LDY     #$0C                
D894: A9 10           LDA     #$10                
D896: 18              CLC                         
D897: 6D 20 07        ADC     $0720               
D89A: 38              SEC                         
D89B: E9 08           SBC     #$08                
D89D: 9D 00 07        STA     $0700,X             
D8A0: 9D 00 02        STA     $0200,X             
D8A3: 98              TYA                         
D8A4: 9D 02 07        STA     $0702,X             
D8A7: AD 23 07        LDA     $0723               
D8AA: 9D 03 07        STA     $0703,X             
D8AD: 9D 03 02        STA     $0203,X             
D8B0: A9 80           LDA     #$80                
D8B2: 9D 01 07        STA     $0701,X             
D8B5: D0 4E           BNE     $D905               ; {}
D8B7: A2 48           LDX     #$48                
D8B9: 20 BE D8        JSR     $D8BE               ; {}
D8BC: A2 4C           LDX     #$4C                
D8BE: A5 3A           LDA     $3A                 
D8C0: C9 10           CMP     #$10                
D8C2: 90 03           BCC     $D8C7               ; {}
D8C4: 4C 9D D6        JMP     $D69D               ; {}
D8C7: A5 A5           LDA     $A5                 
D8C9: 29 04           AND     #$04                
D8CB: F0 42           BEQ     $D90F               ; {}
D8CD: BD 01 07        LDA     $0701,X             
D8D0: 10 B5           BPL     $D887               ; {}
D8D2: A5 14           LDA     $14                 
D8D4: 4A              LSR     A                   
D8D5: 90 03           BCC     $D8DA               ; {}
D8D7: FE 02 07        INC     $0702,X             
D8DA: BD 02 07        LDA     $0702,X             
D8DD: C9 18           CMP     #$18                
D8DF: 90 05           BCC     $D8E6               ; {}
D8E1: A9 00           LDA     #$00                
D8E3: 9D 02 07        STA     $0702,X             
D8E6: 0A              ASL     A                   
D8E7: A8              TAY                         
D8E8: AD 20 07        LDA     $0720               
D8EB: 18              CLC                         
D8EC: 79 10 D9        ADC     $D910,Y             ; {}
D8EF: 38              SEC                         
D8F0: E9 08           SBC     #$08                
D8F2: 9D 00 07        STA     $0700,X             
D8F5: 9D 00 02        STA     $0200,X             
D8F8: AD 23 07        LDA     $0723               
D8FB: 18              CLC                         
D8FC: 79 11 D9        ADC     $D911,Y             ; {}
D8FF: 9D 03 07        STA     $0703,X             
D902: 9D 03 02        STA     $0203,X             
D905: A9 99           LDA     #$99                
D907: 9D 01 02        STA     $0201,X             
D90A: A9 00           LDA     #$00                
D90C: 9D 02 02        STA     $0202,X             
D90F: 60              RTS                         
D910: F0 00           BEQ     $D912               ; {}
D912: F0 05           BEQ     $D919               ; {}
D914: F2 ; ????
D915: 08              PHP                         
D916: F4 ; ????
D917: 0B ; ????
D918: F8              SED                         
D919: 0E FC 10        ASL     $10FC               
D91C: 00              BRK                         
D91D: 10 04           BPL     $D923               ; {}
D91F: 10 08           BPL     $D929               ; {}
D921: 0E 0C 0D        ASL     $0D0C               
D924: 0E 08 10        ASL     $1008               
D927: 04 ; ????
D928: 10 00           BPL     $D92A               ; {}
D92A: 0F ; ????
D92B: FB ; ????
D92C: 0E F8 0B        ASL     $0BF8               
D92F: F5 08           SBC     $08,X               
D931: F2 ; ????
D932: 04 ; ????
D933: F1 00           SBC     ($00),Y             ; {ram.GP_00}
D935: F0 FB           BEQ     $D932               ; {}
D937: F1 F8           SBC     ($F8),Y             
D939: F2 ; ????
D93A: F4 ; ????
D93B: F5 F2           SBC     $F2,X               
D93D: F8              SED                         
D93E: F0 FC           BEQ     $D93C               ; {}
D940: 60              RTS                         
D941: B9 01 07        LDA     $0701,Y             
D944: 29 F8           AND     #$F8                
D946: F0 3C           BEQ     $D984               ; {}
D948: B9 00 07        LDA     $0700,Y             
D94B: 18              CLC                         
D94C: 69 06           ADC     #$06                
D94E: 38              SEC                         
D94F: FD 00 07        SBC     $0700,X             
D952: B0 02           BCS     $D956               ; {}
D954: 49 FF           EOR     #$FF                
D956: C9 0E           CMP     #$0E                
D958: B0 29           BCS     $D983               ; {}
D95A: 90 16           BCC     $D972               ; {}
D95C: B9 01 07        LDA     $0701,Y             
D95F: 29 F8           AND     #$F8                
D961: F0 21           BEQ     $D984               ; {}
D963: B9 00 07        LDA     $0700,Y             
D966: 38              SEC                         
D967: FD 00 07        SBC     $0700,X             
D96A: B0 02           BCS     $D96E               ; {}
D96C: 49 FF           EOR     #$FF                
D96E: C9 0C           CMP     #$0C                
D970: B0 11           BCS     $D983               ; {}
D972: B9 03 07        LDA     $0703,Y             
D975: 38              SEC                         
D976: FD 03 07        SBC     $0703,X             
D979: B0 02           BCS     $D97D               ; {}
D97B: 49 FF           EOR     #$FF                
D97D: C9 08           CMP     #$08                
D97F: B0 02           BCS     $D983               ; {}
D981: 68              PLA                         
D982: 68              PLA                         
D983: 60              RTS                         
D984: 38              SEC                         
D985: 60              RTS                         
D986: 20 5C D9        JSR     $D95C               ; {}
D989: 60              RTS                         
D98A: A0 20           LDY     #$20                
D98C: 20 63 D9        JSR     $D963               ; {}
D98F: 60              RTS                         
D990: A5 3C           LDA     $3C                 
D992: D0 15           BNE     $D9A9               ; {}
D994: A0 38           LDY     #$38                
D996: 20 5C D9        JSR     $D95C               ; {}
D999: A0 3C           LDY     #$3C                
D99B: 20 5C D9        JSR     $D95C               ; {}
D99E: A0 40           LDY     #$40                
D9A0: 20 5C D9        JSR     $D95C               ; {}
D9A3: A0 44           LDY     #$44                
D9A5: 20 5C D9        JSR     $D95C               ; {}
D9A8: 60              RTS                         
D9A9: AD 3A 07        LDA     $073A               
D9AC: C9 04           CMP     #$04                
D9AE: D0 D4           BNE     $D984               ; {}
D9B0: A0 38           LDY     #$38                
D9B2: 20 86 D9        JSR     $D986               ; {}
D9B5: B0 CD           BCS     $D984               ; {}
D9B7: 20 D5 D9        JSR     $D9D5               ; {}
D9BA: 18              CLC                         
D9BB: 60              RTS                         
D9BC: A5 3C           LDA     $3C                 
D9BE: D0 E9           BNE     $D9A9               ; {}
D9C0: A0 38           LDY     #$38                
D9C2: 20 41 D9        JSR     $D941               ; {}
D9C5: A0 3C           LDY     #$3C                
D9C7: 20 41 D9        JSR     $D941               ; {}
D9CA: A0 40           LDY     #$40                
D9CC: 20 41 D9        JSR     $D941               ; {}
D9CF: A0 44           LDY     #$44                
D9D1: 20 41 D9        JSR     $D941               ; {}
D9D4: 60              RTS                         
D9D5: CE 4F 01        DEC     $014F               
D9D8: AD 4F 01        LDA     $014F               
D9DB: F0 02           BEQ     $D9DF               ; {}
D9DD: 10 07           BPL     $D9E6               ; {}
D9DF: A9 00           LDA     #$00                
D9E1: 85 3C           STA     $3C                 
D9E3: 8D 4F 01        STA     $014F               
D9E6: 60              RTS                         
D9E7: A5 3E           LDA     $3E                 
D9E9: D0 0B           BNE     $D9F6               ; {}
D9EB: A0 48           LDY     #$48                
D9ED: 20 5C D9        JSR     $D95C               ; {}
D9F0: A0 4C           LDY     #$4C                
D9F2: 20 5C D9        JSR     $D95C               ; {}
D9F5: 60              RTS                         
D9F6: 38              SEC                         
D9F7: 60              RTS                         
D9F8: A5 16           LDA     $16                 
D9FA: 29 04           AND     #$04                
D9FC: D0 03           BNE     $DA01               ; {}
D9FE: A9 0F           LDA     #$0F                
DA00: 60              RTS                         
DA01: A9 07           LDA     #$07                
DA03: 60              RTS                         
DA04: 28              PLP                         
DA05: 38              SEC                         
DA06: A9 FF           LDA     #$FF                
DA08: 60              RTS                         
DA09: A5 A2           LDA     $A2                 
DA0B: 30 F8           BMI     $DA05               ; {}
DA0D: A0 20           LDY     #$20                
DA0F: B9 08 07        LDA     $0708,Y             
DA12: D0 F1           BNE     $DA05               ; {}
DA14: B9 01 07        LDA     $0701,Y             
DA17: 29 40           AND     #$40                
DA19: D0 EA           BNE     $DA05               ; {}
DA1B: 20 F8 D9        JSR     $D9F8               ; {}
DA1E: 85 00           STA     $00                 ; {ram.GP_00}
DA20: B9 00 07        LDA     $0700,Y             
DA23: 38              SEC                         
DA24: E9 04           SBC     #$04                
DA26: 38              SEC                         
DA27: FD 00 07        SBC     $0700,X             
DA2A: B0 02           BCS     $DA2E               ; {}
DA2C: 49 FF           EOR     #$FF                
DA2E: C5 00           CMP     $00                 ; {ram.GP_00}
DA30: B0 D3           BCS     $DA05               ; {}
DA32: B9 03 07        LDA     $0703,Y             
DA35: 38              SEC                         
DA36: FD 03 07        SBC     $0703,X             
DA39: 08              PHP                         
DA3A: B0 02           BCS     $DA3E               ; {}
DA3C: 49 FF           EOR     #$FF                
DA3E: C9 08           CMP     #$08                
DA40: B0 C2           BCS     $DA04               ; {}
DA42: 28              PLP                         
DA43: E0 F0           CPX     #$F0                
DA45: B0 04           BCS     $DA4B               ; {}
DA47: A5 3E           LDA     $3E                 
DA49: D0 54           BNE     $DA9F               ; {}
DA4B: 20 39 DB        JSR     $DB39               ; {}
DA4E: A9 00           LDA     #$00                
DA50: 9D 04 07        STA     $0704,X             
DA53: A9 7F           LDA     #$7F                
DA55: 99 08 07        STA     $0708,Y             
DA58: A9 80           LDA     #$80                
DA5A: 8D 81 03        STA     $0381               
DA5D: 98              TYA                         
DA5E: 48              PHA                         
DA5F: A9 03           LDA     #$03                
DA61: 20 37 E3        JSR     $E337               ; {}
DA64: 68              PLA                         
DA65: A8              TAY                         
DA66: 20 16 DB        JSR     $DB16               ; {}
DA69: A5 A6           LDA     $A6                 
DA6B: D0 2E           BNE     $DA9B               ; {}
DA6D: AD 51 01        LDA     $0151               
DA70: 29 3F           AND     #$3F                
DA72: D0 14           BNE     $DA88               ; {}
DA74: A9 00           LDA     #$00                
DA76: 99 08 07        STA     $0708,Y             
DA79: B9 01 07        LDA     $0701,Y             
DA7C: 09 40           ORA     #$40                
DA7E: 99 01 07        STA     $0701,Y             
DA81: A9 20           LDA     #$20                
DA83: 99 05 07        STA     $0705,Y             
DA86: 18              CLC                         
DA87: 60              RTS                         
DA88: 38              SEC                         
DA89: E9 01           SBC     #$01                
DA8B: 85 00           STA     $00                 ; {ram.GP_00}
DA8D: AD 51 01        LDA     $0151               
DA90: 29 C0           AND     #$C0                
DA92: 05 00           ORA     $00                 ; {ram.GP_00}
DA94: 8D 51 01        STA     $0151               
DA97: A9 07           LDA     #$07                
DA99: 85 A6           STA     $A6                 
DA9B: A9 00           LDA     #$00                
DA9D: 38              SEC                         
DA9E: 60              RTS                         
DA9F: A9 F8           LDA     #$F8                
DAA1: 9D 00 07        STA     $0700,X             
DAA4: A9 00           LDA     #$00                
DAA6: 9D 01 07        STA     $0701,X             
DAA9: A9 10           LDA     #$10                
DAAB: 8D 81 03        STA     $0381               
DAAE: 4C C6 EA        JMP     $EAC6               ; {}
DAB1: B9 00 07        LDA     $0700,Y             
DAB4: 38              SEC                         
DAB5: E9 0C           SBC     #$0C                
DAB7: 38              SEC                         
DAB8: FD 00 07        SBC     $0700,X             
DABB: B0 02           BCS     $DABF               ; {}
DABD: 49 FF           EOR     #$FF                
DABF: C9 04           CMP     #$04                
DAC1: B0 0F           BCS     $DAD2               ; {}
DAC3: B9 03 07        LDA     $0703,Y             
DAC6: 38              SEC                         
DAC7: FD 03 07        SBC     $0703,X             
DACA: B0 02           BCS     $DACE               ; {}
DACC: 49 FF           EOR     #$FF                
DACE: C9 10           CMP     #$10                
DAD0: B0 01           BCS     $DAD3               ; {}
DAD2: 60              RTS                         
DAD3: B9 03 07        LDA     $0703,Y             
DAD6: C9 0C           CMP     #$0C                
DAD8: 90 06           BCC     $DAE0               ; {}
DADA: C9 F4           CMP     #$F4                
DADC: B0 02           BCS     $DAE0               ; {}
DADE: 38              SEC                         
DADF: 60              RTS                         
DAE0: BD 03 07        LDA     $0703,X             
DAE3: C9 0C           CMP     #$0C                
DAE5: 90 06           BCC     $DAED               ; {}
DAE7: C9 F4           CMP     #$F4                
DAE9: B0 02           BCS     $DAED               ; {}
DAEB: 38              SEC                         
DAEC: 60              RTS                         
DAED: 18              CLC                         
DAEE: 60              RTS                         
DAEF: A0 20           LDY     #$20                
DAF1: 20 F8 D9        JSR     $D9F8               ; {}
DAF4: 85 00           STA     $00                 ; {ram.GP_00}
DAF6: B9 00 07        LDA     $0700,Y             
DAF9: 38              SEC                         
DAFA: E9 04           SBC     #$04                
DAFC: 38              SEC                         
DAFD: FD 00 07        SBC     $0700,X             
DB00: B0 02           BCS     $DB04               ; {}
DB02: 49 FF           EOR     #$FF                
DB04: C5 00           CMP     $00                 ; {ram.GP_00}
DB06: B0 0D           BCS     $DB15               ; {}
DB08: B9 03 07        LDA     $0703,Y             
DB0B: 38              SEC                         
DB0C: FD 03 07        SBC     $0703,X             
DB0F: B0 02           BCS     $DB13               ; {}
DB11: 49 FF           EOR     #$FF                
DB13: C9 08           CMP     #$08                
DB15: 60              RTS                         
DB16: 98              TYA                         
DB17: 48              PHA                         
DB18: AD 58 7F        LDA     $7F58               
DB1B: 85 00           STA     $00                 ; {ram.GP_00}
DB1D: AD 59 7F        LDA     $7F59               
DB20: 85 01           STA     $01                 
DB22: BD 01 07        LDA     $0701,X             
DB25: 29 F8           AND     #$F8                
DB27: 4A              LSR     A                   
DB28: 4A              LSR     A                   
DB29: 4A              LSR     A                   
DB2A: A8              TAY                         
DB2B: A5 A6           LDA     $A6                 
DB2D: 38              SEC                         
DB2E: F1 00           SBC     ($00),Y             ; {ram.GP_00}
DB30: B0 02           BCS     $DB34               ; {}
DB32: A9 00           LDA     #$00                
DB34: 85 A6           STA     $A6                 
DB36: 68              PLA                         
DB37: A8              TAY                         
DB38: 60              RTS                         
DB39: 90 13           BCC     $DB4E               ; {}
DB3B: B9 03 07        LDA     $0703,Y             
DB3E: 18              CLC                         
DB3F: 69 04           ADC     #$04                
DB41: 99 03 07        STA     $0703,Y             
DB44: BD 03 07        LDA     $0703,X             
DB47: 38              SEC                         
DB48: E9 04           SBC     #$04                
DB4A: 9D 03 07        STA     $0703,X             
DB4D: 60              RTS                         
DB4E: B9 03 07        LDA     $0703,Y             
DB51: C9 0C           CMP     #$0C                
DB53: 90 13           BCC     $DB68               ; {}
DB55: B9 03 07        LDA     $0703,Y             
DB58: 38              SEC                         
DB59: E9 04           SBC     #$04                
DB5B: 99 03 07        STA     $0703,Y             
DB5E: BD 03 07        LDA     $0703,X             
DB61: 18              CLC                         
DB62: 69 04           ADC     #$04                
DB64: 9D 03 07        STA     $0703,X             
DB67: 60              RTS                         
DB68: A9 08           LDA     #$08                
DB6A: 99 03 07        STA     $0703,Y             
DB6D: 60              RTS                         
DB6E: BD 02 07        LDA     $0702,X             
DB71: 29 F0           AND     #$F0                
DB73: 18              CLC                         
DB74: 69 80           ADC     #$80                
DB76: 85 00           STA     $00                 ; {ram.GP_00}
DB78: A0 08           LDY     #$08                
DB7A: BD 05 07        LDA     $0705,X             
DB7D: 20 A1 DB        JSR     $DBA1               ; {}
DB80: A5 02           LDA     $02                 
DB82: 9D 05 07        STA     $0705,X             
DB85: BD 02 07        LDA     $0702,X             
DB88: 29 0F           AND     #$0F                
DB8A: 0A              ASL     A                   
DB8B: 0A              ASL     A                   
DB8C: 0A              ASL     A                   
DB8D: 0A              ASL     A                   
DB8E: 18              CLC                         
DB8F: 69 80           ADC     #$80                
DB91: 85 00           STA     $00                 ; {ram.GP_00}
DB93: A0 02           LDY     #$02                
DB95: BD 04 07        LDA     $0704,X             
DB98: 20 A1 DB        JSR     $DBA1               ; {}
DB9B: A5 02           LDA     $02                 
DB9D: 9D 04 07        STA     $0704,X             
DBA0: 60              RTS                         
DBA1: 84 01           STY     $01                 
DBA3: 85 02           STA     $02                 
DBA5: 18              CLC                         
DBA6: 69 80           ADC     #$80                
DBA8: 29 FC           AND     #$FC                
DBAA: C5 00           CMP     $00                 ; {ram.GP_00}
DBAC: F0 09           BEQ     $DBB7               ; {}
DBAE: 90 08           BCC     $DBB8               ; {}
DBB0: A5 02           LDA     $02                 
DBB2: 38              SEC                         
DBB3: E5 01           SBC     $01                 
DBB5: 85 02           STA     $02                 
DBB7: 60              RTS                         
DBB8: A5 02           LDA     $02                 
DBBA: 18              CLC                         
DBBB: 65 01           ADC     $01                 
DBBD: 85 02           STA     $02                 
DBBF: 60              RTS                         
DBC0: 20 6E DB        JSR     $DB6E               ; {}
DBC3: 20 DA DB        JSR     $DBDA               ; {}
DBC6: 4C C9 DB        JMP     $DBC9               ; {}
DBC9: BD 03 07        LDA     $0703,X             
DBCC: 85 00           STA     $00                 ; {ram.GP_00}
DBCE: BD 04 07        LDA     $0704,X             
DBD1: 20 EB DB        JSR     $DBEB               ; {}
DBD4: A5 00           LDA     $00                 ; {ram.GP_00}
DBD6: 9D 03 07        STA     $0703,X             
DBD9: 60              RTS                         
DBDA: BD 00 07        LDA     $0700,X             
DBDD: 85 00           STA     $00                 ; {ram.GP_00}
DBDF: BD 05 07        LDA     $0705,X             
DBE2: 20 EB DB        JSR     $DBEB               ; {}
DBE5: A5 00           LDA     $00                 ; {ram.GP_00}
DBE7: 9D 00 07        STA     $0700,X             
DBEA: 60              RTS                         
DBEB: 29 FC           AND     #$FC                
DBED: C9 04           CMP     #$04                
DBEF: 90 3F           BCC     $DC30               ; {}
DBF1: C9 FC           CMP     #$FC                
DBF3: B0 3B           BCS     $DC30               ; {}
DBF5: 29 F0           AND     #$F0                
DBF7: 4A              LSR     A                   
DBF8: 4A              LSR     A                   
DBF9: 4A              LSR     A                   
DBFA: A8              TAY                         
DBFB: B9 08 DC        LDA     $DC08,Y             ; {}
DBFE: 85 01           STA     $01                 
DC00: B9 09 DC        LDA     $DC09,Y             ; {}
DC03: 85 02           STA     $02                 
DC05: 6C 01 00        JMP     ($0001)             
DC08: 28              PLP                         
DC09: DC ; ????
DC0A: 31 DC           AND     ($DC),Y             
DC0C: 35 DC           AND     $DC,X               
DC0E: 39 DC 2E        AND     $2EDC,Y             
DC11: DC ; ????
DC12: 47 ; ????
DC13: DC ; ????
DC14: 45 DC           EOR     $DC                 
DC16: 43 ; ????
DC17: DC ; ????
DC18: 4C DC 4E        JMP     $4EDC               
DC1B: DC ; ????
DC1C: 50 DC           BVC     $DBFA               ; {}
DC1E: 52 ; ????
DC1F: DC ; ????
DC20: 55 DC           EOR     $DC,X               
DC22: 5B ; ????
DC23: DC ; ????
DC24: 62 ; ????
DC25: DC ; ????
DC26: 66 DC           ROR     $DC                 
DC28: A9 0F           LDA     #$0F                
DC2A: 25 14           AND     $14                 
DC2C: D0 02           BNE     $DC30               ; {}
DC2E: E6 00           INC     $00                 ; {ram.GP_00}
DC30: 60              RTS                         
DC31: A9 07           LDA     #$07                
DC33: D0 F5           BNE     $DC2A               ; {}
DC35: A9 03           LDA     #$03                
DC37: D0 F1           BNE     $DC2A               ; {}
DC39: A9 01           LDA     #$01                
DC3B: D0 ED           BNE     $DC2A               ; {}
DC3D: A5 14           LDA     $14                 
DC3F: 4A              LSR     A                   
DC40: 90 EC           BCC     $DC2E               ; {}
DC42: 60              RTS                         
DC43: E6 00           INC     $00                 ; {ram.GP_00}
DC45: E6 00           INC     $00                 ; {ram.GP_00}
DC47: E6 00           INC     $00                 ; {ram.GP_00}
DC49: E6 00           INC     $00                 ; {ram.GP_00}
DC4B: 60              RTS                         
DC4C: C6 00           DEC     $00                 ; {ram.GP_00}
DC4E: C6 00           DEC     $00                 ; {ram.GP_00}
DC50: C6 00           DEC     $00                 ; {ram.GP_00}
DC52: C6 00           DEC     $00                 ; {ram.GP_00}
DC54: 60              RTS                         
DC55: A5 14           LDA     $14                 
DC57: 4A              LSR     A                   
DC58: 90 F8           BCC     $DC52               ; {}
DC5A: 60              RTS                         
DC5B: A9 03           LDA     #$03                
DC5D: 25 14           AND     $14                 
DC5F: F0 F1           BEQ     $DC52               ; {}
DC61: 60              RTS                         
DC62: A9 07           LDA     #$07                
DC64: D0 F7           BNE     $DC5D               ; {}
DC66: A9 0F           LDA     #$0F                
DC68: D0 F3           BNE     $DC5D               ; {}
DC6A: A0 00           LDY     #$00                
DC6C: 48              PHA                         
DC6D: 29 F8           AND     #$F8                
DC6F: 85 00           STA     $00                 ; {ram.GP_00}
DC71: B9 3F 00        LDA     $003F,Y             
DC74: 29 F8           AND     #$F8                
DC76: C5 00           CMP     $00                 ; {ram.GP_00}
DC78: D0 18           BNE     $DC92               ; {}
DC7A: B9 3F 00        LDA     $003F,Y             
DC7D: 29 07           AND     #$07                
DC7F: C9 03           CMP     #$03                
DC81: B0 0B           BCS     $DC8E               ; {}
DC83: B9 3F 00        LDA     $003F,Y             
DC86: 18              CLC                         
DC87: 69 01           ADC     #$01                
DC89: 99 3F 00        STA     $003F,Y             
DC8C: 68              PLA                         
DC8D: 60              RTS                         
DC8E: 68              PLA                         
DC8F: 68              PLA                         
DC90: 68              PLA                         
DC91: 60              RTS                         
DC92: A5 00           LDA     $00                 ; {ram.GP_00}
DC94: 99 3F 00        STA     $003F,Y             
DC97: 68              PLA                         
DC98: 60              RTS                         
DC99: A0 01           LDY     #$01                
DC9B: D0 CF           BNE     $DC6C               ; {}
DC9D: A0 02           LDY     #$02                
DC9F: D0 CB           BNE     $DC6C               ; {}
DCA1: A0 03           LDY     #$03                
DCA3: D0 C7           BNE     $DC6C               ; {}
DCA5: A9 05           LDA     #$05                
DCA7: D0 14           BNE     $DCBD               ; {}
DCA9: BD 08 07        LDA     $0708,X             
DCAC: D0 25           BNE     $DCD3               ; {}
DCAE: 98              TYA                         
DCAF: 48              PHA                         
DCB0: A5 3C           LDA     $3C                 
DCB2: D0 F1           BNE     $DCA5               ; {}
DCB4: AD 52 01        LDA     $0152               
DCB7: 29 07           AND     #$07                
DCB9: A8              TAY                         
DCBA: B9 D6 DC        LDA     $DCD6,Y             ; {}
DCBD: 85 00           STA     $00                 ; {ram.GP_00}
DCBF: 68              PLA                         
DCC0: A8              TAY                         
DCC1: BD 07 07        LDA     $0707,X             
DCC4: 38              SEC                         
DCC5: E5 00           SBC     $00                 ; {ram.GP_00}
DCC7: F0 0C           BEQ     $DCD5               ; {}
DCC9: 90 0A           BCC     $DCD5               ; {}
DCCB: 9D 07 07        STA     $0707,X             
DCCE: A9 10           LDA     #$10                
DCD0: 9D 08 07        STA     $0708,X             
DCD3: 68              PLA                         
DCD4: 68              PLA                         
DCD5: 60              RTS                         
DCD6: 01 02           ORA     ($02,X)             
DCD8: 03 ; ????
DCD9: 04 ; ????
DCDA: 05 06           ORA     $06                 
DCDC: 06 06           ASL     $06                 
DCDE: A9 0C           LDA     #$0C                
DCE0: 85 02           STA     $02                 
DCE2: BD 08 07        LDA     $0708,X             
DCE5: F0 EE           BEQ     $DCD5               ; {}
DCE7: DE 08 07        DEC     $0708,X             
DCEA: 29 03           AND     #$03                
DCEC: 85 00           STA     $00                 ; {ram.GP_00}
DCEE: 8A              TXA                         
DCEF: 85 01           STA     $01                 
DCF1: 18              CLC                         
DCF2: 65 02           ADC     $02                 
DCF4: A8              TAY                         
DCF5: B9 02 02        LDA     $0202,Y             
DCF8: 29 FC           AND     #$FC                
DCFA: 05 00           ORA     $00                 ; {ram.GP_00}
DCFC: 99 02 02        STA     $0202,Y             
DCFF: 88              DEY                         
DD00: 88              DEY                         
DD01: 88              DEY                         
DD02: 88              DEY                         
DD03: C4 01           CPY     $01                 
DD05: B0 EE           BCS     $DCF5               ; {}
DD07: 60              RTS                         
DD08: BD 03 07        LDA     $0703,X             
DD0B: C9 F8           CMP     #$F8                
DD0D: B0 08           BCS     $DD17               ; {}
DD0F: BD 00 07        LDA     $0700,X             
DD12: C9 F8           CMP     #$F8                
DD14: B0 01           BCS     $DD17               ; {}
DD16: 60              RTS                         
DD17: 20 1D DD        JSR     $DD1D               ; {}
DD1A: 68              PLA                         
DD1B: 68              PLA                         
DD1C: 60              RTS                         
DD1D: A9 00           LDA     #$00                
DD1F: 9D 01 07        STA     $0701,X             
DD22: 9D 02 07        STA     $0702,X             
DD25: 9D 03 07        STA     $0703,X             
DD28: 9D 09 07        STA     $0709,X             
DD2B: A9 F8           LDA     #$F8                
DD2D: 9D 00 07        STA     $0700,X             
DD30: 9D 00 02        STA     $0200,X             
DD33: 9D 04 02        STA     $0204,X             
DD36: 9D 08 02        STA     $0208,X             
DD39: 9D 0C 02        STA     $020C,X             
DD3C: 60              RTS                         
DD3D: BD 00 07        LDA     $0700,X             
DD40: 9D 08 02        STA     $0208,X             
DD43: 9D 0C 02        STA     $020C,X             
DD46: 38              SEC                         
DD47: E9 08           SBC     #$08                
DD49: 9D 00 02        STA     $0200,X             
DD4C: 9D 04 02        STA     $0204,X             
DD4F: BD 03 07        LDA     $0703,X             
DD52: 38              SEC                         
DD53: E9 04           SBC     #$04                
DD55: 9D 03 02        STA     $0203,X             
DD58: 9D 0B 02        STA     $020B,X             
DD5B: 18              CLC                         
DD5C: 69 08           ADC     #$08                
DD5E: 9D 07 02        STA     $0207,X             
DD61: 9D 0F 02        STA     $020F,X             
DD64: 60              RTS                         
DD65: 20 08 DD        JSR     $DD08               ; {}
DD68: BD 02 07        LDA     $0702,X             
DD6B: F0 1C           BEQ     $DD89               ; {}
DD6D: DE 02 07        DEC     $0702,X             
DD70: C9 E8           CMP     #$E8                
DD72: 90 1E           BCC     $DD92               ; {}
DD74: C9 F0           CMP     #$F0                
DD76: 90 09           BCC     $DD81               ; {}
DD78: C9 F8           CMP     #$F8                
DD7A: 90 09           BCC     $DD85               ; {}
DD7C: A9 32           LDA     #$32                
DD7E: 4C CD C4        JMP     $C4CD               ; {}
DD81: A9 30           LDA     #$30                
DD83: D0 F9           BNE     $DD7E               ; {}
DD85: A9 31           LDA     #$31                
DD87: D0 F5           BNE     $DD7E               ; {}
DD89: 4C 1D DD        JMP     $DD1D               ; {}
DD8C: A9 00           LDA     #$00                
DD8E: 9D 02 07        STA     $0702,X             
DD91: 60              RTS                         
DD92: 20 1B 7F        JSR     $7F1B               
DD95: F0 F5           BEQ     $DD8C               ; {}
DD97: 85 08           STA     $08                 
DD99: C9 05           CMP     #$05                
DD9B: B0 25           BCS     $DDC2               ; {}
DD9D: C9 03           CMP     #$03                
DD9F: B0 17           BCS     $DDB8               ; {}
DDA1: 20 8A D9        JSR     $D98A               ; {}
DDA4: 90 05           BCC     $DDAB               ; {}
DDA6: A9 00           LDA     #$00                
DDA8: 4C 67 C6        JMP     $C667               ; {}
DDAB: A9 10           LDA     #$10                
DDAD: 8D 81 03        STA     $0381               
DDB0: 20 89 DD        JSR     $DD89               ; {}
DDB3: A5 08           LDA     $08                 
DDB5: 4C CC DD        JMP     $DDCC               ; {}
DDB8: 20 8A D9        JSR     $D98A               ; {}
DDBB: 90 EE           BCC     $DDAB               ; {}
DDBD: A9 01           LDA     #$01                
DDBF: 4C 67 C6        JMP     $C667               ; {}
DDC2: 20 8A D9        JSR     $D98A               ; {}
DDC5: 90 E4           BCC     $DDAB               ; {}
DDC7: A9 1A           LDA     #$1A                
DDC9: 4C 67 C6        JMP     $C667               ; {}
DDCC: 85 08           STA     $08                 
DDCE: 20 EC DD        JSR     $DDEC               ; {}
DDD1: C9 03           CMP     #$03                
DDD3: 90 12           BCC     $DDE7               ; {}
DDD5: AD 4A 01        LDA     $014A               
DDD8: C9 E7           CMP     #$E7                
DDDA: 90 0B           BCC     $DDE7               ; {}
DDDC: A9 03           LDA     #$03                
DDDE: 8D 4B 01        STA     $014B               
DDE1: A9 E7           LDA     #$E7                
DDE3: 8D 4A 01        STA     $014A               
DDE6: 60              RTS                         
DDE7: A5 08           LDA     $08                 
DDE9: 4C F0 E2        JMP     $E2F0               ; {}
DDEC: 20 41 DE        JSR     $DE41               ; {}
DDEF: 48              PHA                         
DDF0: AD 4C 01        LDA     $014C               
DDF3: D0 16           BNE     $DE0B               ; {}
DDF5: AD 4D 01        LDA     $014D               
DDF8: D0 11           BNE     $DE0B               ; {}
DDFA: 68              PLA                         
DDFB: 18              CLC                         
DDFC: 6D 4A 01        ADC     $014A               
DDFF: 8D 4A 01        STA     $014A               
DE02: AD 4B 01        LDA     $014B               
DE05: 69 00           ADC     #$00                
DE07: 8D 4B 01        STA     $014B               
DE0A: 60              RTS                         
DE0B: 68              PLA                         
DE0C: 8D 28 01        STA     $0128               
DE0F: 38              SEC                         
DE10: AD 4C 01        LDA     $014C               
DE13: ED 28 01        SBC     $0128               
DE16: 8D 2A 01        STA     $012A               
DE19: 90 04           BCC     $DE1F               ; {}
DE1B: 8D 4C 01        STA     $014C               
DE1E: 60              RTS                         
DE1F: AD 4D 01        LDA     $014D               
DE22: E9 00           SBC     #$00                
DE24: 90 0A           BCC     $DE30               ; {}
DE26: 8D 4D 01        STA     $014D               
DE29: AD 2A 01        LDA     $012A               
DE2C: 8D 4C 01        STA     $014C               
DE2F: 60              RTS                         
DE30: 38              SEC                         
DE31: AD 28 01        LDA     $0128               
DE34: ED 4C 01        SBC     $014C               
DE37: 8D 28 01        STA     $0128               
DE3A: A9 00           LDA     #$00                
DE3C: 8D 4C 01        STA     $014C               
DE3F: F0 BA           BEQ     $DDFB               ; {}
DE41: C9 05           CMP     #$05                
DE43: B0 07           BCS     $DE4C               ; {}
DE45: C9 03           CMP     #$03                
DE47: B0 06           BCS     $DE4F               ; {}
DE49: A9 01           LDA     #$01                
DE4B: 60              RTS                         
DE4C: A9 0A           LDA     #$0A                
DE4E: 60              RTS                         
DE4F: A9 05           LDA     #$05                
DE51: 60              RTS                         
DE52: 20 5A DE        JSR     $DE5A               ; {}
DE55: A5 08           LDA     $08                 
DE57: 4C 37 E3        JMP     $E337               ; {}
DE5A: 85 08           STA     $08                 
DE5C: AD 4C 01        LDA     $014C               
DE5F: D0 17           BNE     $DE78               ; {}
DE61: AD 4D 01        LDA     $014D               
DE64: D0 12           BNE     $DE78               ; {}
DE66: AD 4A 01        LDA     $014A               
DE69: 38              SEC                         
DE6A: E5 08           SBC     $08                 
DE6C: 8D 4A 01        STA     $014A               
DE6F: AD 4B 01        LDA     $014B               
DE72: E9 00           SBC     #$00                
DE74: 8D 4B 01        STA     $014B               
DE77: 60              RTS                         
DE78: 18              CLC                         
DE79: AD 4C 01        LDA     $014C               
DE7C: 65 08           ADC     $08                 
DE7E: 8D 4C 01        STA     $014C               
DE81: AD 4D 01        LDA     $014D               
DE84: 69 00           ADC     #$00                
DE86: 8D 4D 01        STA     $014D               
DE89: AD 4C 01        LDA     $014C               
DE8C: C9 E7           CMP     #$E7                
DE8E: 90 11           BCC     $DEA1               ; {}
DE90: AD 4D 01        LDA     $014D               
DE93: C9 03           CMP     #$03                
DE95: 90 0A           BCC     $DEA1               ; {}
DE97: A9 E7           LDA     #$E7                
DE99: 8D 4C 01        STA     $014C               
DE9C: A9 03           LDA     #$03                
DE9E: 8D 4D 01        STA     $014D               
DEA1: 60              RTS                         
DEA2: E6 AA           INC     $AA                 
DEA4: A5 AA           LDA     $AA                 
DEA6: 18              CLC                         
DEA7: 69 01           ADC     #$01                
DEA9: 0A              ASL     A                   
DEAA: 0A              ASL     A                   
DEAB: 0A              ASL     A                   
DEAC: 38              SEC                         
DEAD: E9 01           SBC     #$01                
DEAF: 85 A6           STA     $A6                 
DEB1: 60              RTS                         
DEB2: 20 1E DF        JSR     $DF1E               ; {}
DEB5: BD 00 07        LDA     $0700,X             
DEB8: 9D 04 02        STA     $0204,X             
DEBB: 38              SEC                         
DEBC: E9 08           SBC     #$08                
DEBE: 9D 00 02        STA     $0200,X             
DEC1: BD 03 07        LDA     $0703,X             
DEC4: 9D 03 02        STA     $0203,X             
DEC7: 9D 07 02        STA     $0207,X             
DECA: BD 02 07        LDA     $0702,X             
DECD: F0 60           BEQ     $DF2F               ; {}
DECF: DE 02 07        DEC     $0702,X             
DED2: C9 E8           CMP     #$E8                
DED4: 90 1F           BCC     $DEF5               ; {}
DED6: C9 F0           CMP     #$F0                
DED8: 90 11           BCC     $DEEB               ; {}
DEDA: C9 F8           CMP     #$F8                
DEDC: 90 09           BCC     $DEE7               ; {}
DEDE: A9 4A           LDA     #$4A                
DEE0: 9D 01 02        STA     $0201,X             
DEE3: 9D 05 02        STA     $0205,X             
DEE6: 60              RTS                         
DEE7: A9 5A           LDA     #$5A                
DEE9: D0 F5           BNE     $DEE0               ; {}
DEEB: A9 4B           LDA     #$4B                
DEED: D0 F1           BNE     $DEE0               ; {}
DEEF: A9 00           LDA     #$00                
DEF1: 9D 02 07        STA     $0702,X             
DEF4: 60              RTS                         
DEF5: A0 20           LDY     #$20                
DEF7: 20 86 D9        JSR     $D986               ; {}
DEFA: 90 15           BCC     $DF11               ; {}
DEFC: 20 1B 7F        JSR     $7F1B               
DEFF: 85 08           STA     $08                 
DF01: A9 27           LDA     #$27                
DF03: 9D 01 02        STA     $0201,X             
DF06: A9 5F           LDA     #$5F                
DF08: 9D 05 02        STA     $0205,X             
DF0B: A9 01           LDA     #$01                
DF0D: 9D 02 02        STA     $0202,X             
DF10: 60              RTS                         
DF11: A9 10           LDA     #$10                
DF13: 8D 81 03        STA     $0381               
DF16: 20 2F DF        JSR     $DF2F               ; {}
DF19: A9 01           LDA     #$01                
DF1B: 4C CC DD        JMP     $DDCC               ; {}
DF1E: BD 00 07        LDA     $0700,X             
DF21: C9 F8           CMP     #$F8                
DF23: B0 08           BCS     $DF2D               ; {}
DF25: BD 03 07        LDA     $0703,X             
DF28: C9 F8           CMP     #$F8                
DF2A: B0 01           BCS     $DF2D               ; {}
DF2C: 60              RTS                         
DF2D: 68              PLA                         
DF2E: 68              PLA                         
DF2F: A9 00           LDA     #$00                
DF31: 9D 01 07        STA     $0701,X             
DF34: A9 F8           LDA     #$F8                
DF36: 9D 00 07        STA     $0700,X             
DF39: 9D 00 02        STA     $0200,X             
DF3C: 9D 04 02        STA     $0204,X             
DF3F: 60              RTS                         
DF40: A5 3E           LDA     $3E                 
DF42: D0 01           BNE     $DF45               ; {}
DF44: 60              RTS                         
DF45: A5 14           LDA     $14                 
DF47: 29 3F           AND     #$3F                
DF49: D0 05           BNE     $DF50               ; {}
DF4B: A9 40           LDA     #$40                
DF4D: 8D 83 03        STA     $0383               
DF50: A5 14           LDA     $14                 
DF52: 29 01           AND     #$01                
DF54: D0 EE           BNE     $DF44               ; {}
DF56: C6 3E           DEC     $3E                 
DF58: 60              RTS                         
DF59: A9 F8           LDA     #$F8                
DF5B: 9D 08 02        STA     $0208,X             
DF5E: 9D 0C 02        STA     $020C,X             
DF61: 60              RTS                         
DF62: 20 59 DF        JSR     $DF59               ; {}
DF65: A5 3E           LDA     $3E                 
DF67: F0 3D           BEQ     $DFA6               ; {}
DF69: C9 01           CMP     #$01                
DF6B: F0 3A           BEQ     $DFA7               ; {}
DF6D: BD 00 07        LDA     $0700,X             
DF70: C9 F8           CMP     #$F8                
DF72: B0 33           BCS     $DFA7               ; {}
DF74: A9 AA           LDA     #$AA                
DF76: 9D 01 02        STA     $0201,X             
DF79: A9 AB           LDA     #$AB                
DF7B: 9D 05 02        STA     $0205,X             
DF7E: A9 01           LDA     #$01                
DF80: 9D 02 02        STA     $0202,X             
DF83: 9D 06 02        STA     $0206,X             
DF86: A5 14           LDA     $14                 
DF88: 29 03           AND     #$03                
DF8A: D0 03           BNE     $DF8F               ; {}
DF8C: FE 00 07        INC     $0700,X             
DF8F: BD 00 07        LDA     $0700,X             
DF92: 9D 00 02        STA     $0200,X             
DF95: 18              CLC                         
DF96: 69 08           ADC     #$08                
DF98: 9D 04 02        STA     $0204,X             
DF9B: BD 03 07        LDA     $0703,X             
DF9E: 9D 03 02        STA     $0203,X             
DFA1: 9D 07 02        STA     $0207,X             
DFA4: 68              PLA                         
DFA5: 68              PLA                         
DFA6: 60              RTS                         
DFA7: A9 00           LDA     #$00                
DFA9: 9D 01 07        STA     $0701,X             
DFAC: A9 F8           LDA     #$F8                
DFAE: 9D 00 02        STA     $0200,X             
DFB1: 9D 04 02        STA     $0204,X             
DFB4: 9D 00 07        STA     $0700,X             
DFB7: 60              RTS                         
DFB8: BD 03 07        LDA     $0703,X             
DFBB: 18              CLC                         
DFBC: 69 08           ADC     #$08                
DFBE: A8              TAY                         
DFBF: BD 00 07        LDA     $0700,X             
DFC2: 18              CLC                         
DFC3: 69 08           ADC     #$08                
DFC5: 20 12 7F        JSR     $7F12               
DFC8: 8D D3 04        STA     $04D3               
DFCB: A5 00           LDA     $00                 ; {ram.GP_00}
DFCD: 85 12           STA     $12                 
DFCF: A5 01           LDA     $01                 
DFD1: 85 13           STA     $13                 
DFD3: BD 03 07        LDA     $0703,X             
DFD6: 38              SEC                         
DFD7: E9 00           SBC     #$00                
DFD9: A8              TAY                         
DFDA: BD 00 07        LDA     $0700,X             
DFDD: 18              CLC                         
DFDE: 69 08           ADC     #$08                
DFE0: 20 12 7F        JSR     $7F12               
DFE3: 8D D4 04        STA     $04D4               
DFE6: BD 03 07        LDA     $0703,X             
DFE9: 18              CLC                         
DFEA: 69 0A           ADC     #$0A                
DFEC: A8              TAY                         
DFED: BD 00 07        LDA     $0700,X             
DFF0: 20 12 7F        JSR     $7F12               
DFF3: 8D D5 04        STA     $04D5               
DFF6: BD 03 07        LDA     $0703,X             
DFF9: 38              SEC                         
DFFA: E9 02           SBC     #$02                
DFFC: A8              TAY                         
DFFD: BD 00 07        LDA     $0700,X             
E000: 20 12 7F        JSR     $7F12               
E003: 8D D6 04        STA     $04D6               
E006: BD 03 07        LDA     $0703,X             
E009: 18              CLC                         
E00A: 69 07           ADC     #$07                
E00C: 20 2B E0        JSR     $E02B               ; {}
E00F: 8D D7 04        STA     $04D7               
E012: BD 03 07        LDA     $0703,X             
E015: 18              CLC                         
E016: 69 01           ADC     #$01                
E018: 20 2B E0        JSR     $E02B               ; {}
E01B: 8D D8 04        STA     $04D8               
E01E: BD 03 07        LDA     $0703,X             
E021: 18              CLC                         
E022: 69 04           ADC     #$04                
E024: 20 2B E0        JSR     $E02B               ; {}
E027: 8D D9 04        STA     $04D9               
E02A: 60              RTS                         
E02B: A8              TAY                         
E02C: BD 00 07        LDA     $0700,X             
E02F: 38              SEC                         
E030: E9 10           SBC     #$10                
E032: 4C 12 7F        JMP     $7F12               
E035: BD 03 07        LDA     $0703,X             
E038: 18              CLC                         
E039: 69 04           ADC     #$04                
E03B: A8              TAY                         
E03C: BD 00 07        LDA     $0700,X             
E03F: 18              CLC                         
E040: 69 06           ADC     #$06                
E042: 20 12 7F        JSR     $7F12               
E045: 8D D3 04        STA     $04D3               
E048: 60              RTS                         
E049: A9 18           LDA     #$18                
E04B: 85 04           STA     $04                 
E04D: A9 10           LDA     #$10                
E04F: 85 05           STA     $05                 
E051: D0 08           BNE     $E05B               ; {}
E053: A9 08           LDA     #$08                
E055: 85 04           STA     $04                 
E057: A9 00           LDA     #$00                
E059: 85 05           STA     $05                 
E05B: BD 03 07        LDA     $0703,X             
E05E: 18              CLC                         
E05F: 65 04           ADC     $04                 
E061: 20 7D E0        JSR     $E07D               ; {}
E064: 8D D5 04        STA     $04D5               
E067: A0 10           LDY     #$10                
E069: B1 00           LDA     ($00),Y             ; {ram.GP_00}
E06B: 8D D3 04        STA     $04D3               
E06E: BD 03 07        LDA     $0703,X             
E071: 38              SEC                         
E072: E5 05           SBC     $05                 
E074: 20 7D E0        JSR     $E07D               ; {}
E077: 8D D6 04        STA     $04D6               
E07A: 4C A3 E0        JMP     $E0A3               ; {}
E07D: A8              TAY                         
E07E: BD 00 07        LDA     $0700,X             
E081: 38              SEC                         
E082: E9 07           SBC     #$07                
E084: 4C 12 7F        JMP     $7F12               
E087: BD 03 07        LDA     $0703,X             
E08A: 18              CLC                         
E08B: 69 08           ADC     #$08                
E08D: 20 7D E0        JSR     $E07D               ; {}
E090: 8D D5 04        STA     $04D5               
E093: A0 10           LDY     #$10                
E095: B1 00           LDA     ($00),Y             ; {ram.GP_00}
E097: 8D D3 04        STA     $04D3               
E09A: BD 03 07        LDA     $0703,X             
E09D: 20 7D E0        JSR     $E07D               ; {}
E0A0: 8D D6 04        STA     $04D6               
E0A3: A0 10           LDY     #$10                
E0A5: B1 00           LDA     ($00),Y             ; {ram.GP_00}
E0A7: 8D D4 04        STA     $04D4               
E0AA: 60              RTS                         
E0AB: A0 60           LDY     #$60                
E0AD: 20 BC E0        JSR     $E0BC               ; {}
E0B0: A0 70           LDY     #$70                
E0B2: 20 BC E0        JSR     $E0BC               ; {}
E0B5: A0 80           LDY     #$80                
E0B7: 20 BC E0        JSR     $E0BC               ; {}
E0BA: A0 90           LDY     #$90                
E0BC: B9 01 07        LDA     $0701,Y             
E0BF: 29 F8           AND     #$F8                
E0C1: C9 78           CMP     #$78                
E0C3: D0 31           BNE     $E0F6               ; {}
E0C5: 20 B1 DA        JSR     $DAB1               ; {}
E0C8: B0 2C           BCS     $E0F6               ; {}
E0CA: A9 FF           LDA     #$FF                
E0CC: 8D D3 04        STA     $04D3               
E0CF: 8D D4 04        STA     $04D4               
E0D2: 98              TYA                         
E0D3: 48              PHA                         
E0D4: BD 03 07        LDA     $0703,X             
E0D7: 85 00           STA     $00                 ; {ram.GP_00}
E0D9: B9 04 07        LDA     $0704,Y             
E0DC: 20 EB DB        JSR     $DBEB               ; {}
E0DF: A5 00           LDA     $00                 ; {ram.GP_00}
E0E1: 9D 03 07        STA     $0703,X             
E0E4: 68              PLA                         
E0E5: A8              TAY                         
E0E6: BD 00 07        LDA     $0700,X             
E0E9: 85 00           STA     $00                 ; {ram.GP_00}
E0EB: B9 05 07        LDA     $0705,Y             
E0EE: 20 EB DB        JSR     $DBEB               ; {}
E0F1: A5 00           LDA     $00                 ; {ram.GP_00}
E0F3: 9D 00 07        STA     $0700,X             
E0F6: 60              RTS                         
E0F7: A5 37           LDA     $37                 
E0F9: 09 04           ORA     #$04                
E0FB: 85 37           STA     $37                 
E0FD: EE 24 07        INC     $0724               
E100: AD 24 07        LDA     $0724               
E103: C9 10           CMP     #$10                
E105: 90 16           BCC     $E11D               ; {}
E107: C9 20           CMP     #$20                
E109: 90 22           BCC     $E12D               ; {}
E10B: C9 30           CMP     #$30                
E10D: 90 26           BCC     $E135               ; {}
E10F: A5 37           LDA     $37                 
E111: 29 FB           AND     #$FB                
E113: 85 37           STA     $37                 
E115: A9 00           LDA     #$00                
E117: 8D 24 07        STA     $0724               
E11A: E6 3A           INC     $3A                 
E11C: 60              RTS                         
E11D: A9 10           LDA     #$10                
E11F: A2 17           LDX     #$17                
E121: A0 07           LDY     #$07                
E123: 8D A1 03        STA     $03A1               
E126: 8E A2 03        STX     $03A2               
E129: 8C A3 03        STY     $03A3               
E12C: 60              RTS                         
E12D: A9 00           LDA     #$00                
E12F: A2 07           LDX     #$07                
E131: A0 08           LDY     #$08                
E133: D0 EE           BNE     $E123               ; {}
E135: A9 0F           LDA     #$0F                
E137: AA              TAX                         
E138: A8              TAY                         
E139: D0 E8           BNE     $E123               ; {}
E13B: EE 24 07        INC     $0724               
E13E: AD 24 07        LDA     $0724               
E141: C9 10           CMP     #$10                
E143: 90 E8           BCC     $E12D               ; {}
E145: C9 20           CMP     #$20                
E147: 90 D4           BCC     $E11D               ; {}
E149: C9 30           CMP     #$30                
E14B: 90 08           BCC     $E155               ; {}
E14D: E6 3A           INC     $3A                 
E14F: A9 00           LDA     #$00                
E151: 8D 24 07        STA     $0724               
E154: 60              RTS                         
E155: A9 30           LDA     #$30                
E157: A2 28           LDX     #$28                
E159: A0 17           LDY     #$17                
E15B: D0 C6           BNE     $E123               ; {}
E15D: A5 AB           LDA     $AB                 
E15F: 29 C0           AND     #$C0                
E161: D0 1F           BNE     $E182               ; {}
E163: AD E2 04        LDA     $04E2               
E166: D0 1A           BNE     $E182               ; {}
E168: 20 83 E4        JSR     $E483               ; {}
E16B: A5 38           LDA     $38                 
E16D: F0 14           BEQ     $E183               ; {}
E16F: 20 87 E1        JSR     $E187               ; {}
E172: A9 03           LDA     #$03                
E174: 85 00           STA     $00                 ; {ram.GP_00}
E176: A5 18           LDA     $18                 
E178: 29 10           AND     #$10                
E17A: F0 06           BEQ     $E182               ; {}
E17C: A5 00           LDA     $00                 ; {ram.GP_00}
E17E: 85 38           STA     $38                 
E180: 85 DF           STA     $DF                 
E182: 60              RTS                         
E183: A9 01           LDA     #$01                
E185: D0 ED           BNE     $E174               ; {}
E187: A5 3A           LDA     $3A                 
E189: 29 F0           AND     #$F0                
E18B: C9 10           CMP     #$10                
E18D: D0 1C           BNE     $E1AB               ; {}
E18F: A5 38           LDA     $38                 
E191: C9 02           CMP     #$02                
E193: D0 16           BNE     $E1AB               ; {}
E195: 4C 66 E2        JMP     $E266               ; {}
E198: A5 AB           LDA     $AB                 
E19A: 29 C0           AND     #$C0                
E19C: D0 0D           BNE     $E1AB               ; {}
E19E: A5 38           LDA     $38                 
E1A0: C9 01           CMP     #$01                
E1A2: F0 0E           BEQ     $E1B2               ; {}
E1A4: C9 03           CMP     #$03                
E1A6: D0 03           BNE     $E1AB               ; {}
E1A8: 4C 2E E2        JMP     $E22E               ; {}
E1AB: 60              RTS                         
E1AC: 4C 71 E3        JMP     $E371               ; {}
E1AF: 4C 90 E3        JMP     $E390               ; {}
E1B2: 20 F0 EE        JSR     $EEF0               ; {}
E1B5: A9 02           LDA     #$02                
E1B7: 85 38           STA     $38                 
E1B9: 85 DF           STA     $DF                 
E1BB: 20 5B E2        JSR     $E25B               ; {}
E1BE: A5 3A           LDA     $3A                 
E1C0: C9 10           CMP     #$10                
E1C2: B0 2C           BCS     $E1F0               ; {}
E1C4: 20 AC E1        JSR     $E1AC               ; {}
E1C7: A0 1F           LDY     #$1F                
E1C9: B9 0E E2        LDA     $E20E,Y             ; {}
E1CC: 99 90 03        STA     $0390,Y             
E1CF: 88              DEY                         
E1D0: 10 F7           BPL     $E1C9               ; {}
E1D2: 20 F6 E1        JSR     $E1F6               ; {}
E1D5: 20 42 EE        JSR     $EE42               ; {}
E1D8: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
E1DB: A9 00           LDA     #$00                
E1DD: 8D 05 20        STA     $2005               ; {hard.P_BKG_SCROLL}
E1E0: 8D 05 20        STA     $2005               ; {hard.P_BKG_SCROLL}
E1E3: AD 00 01        LDA     $0100               
E1E6: 29 FC           AND     #$FC                
E1E8: 8D 00 01        STA     $0100               
E1EB: 68              PLA                         
E1EC: 68              PLA                         
E1ED: 4C 24 7F        JMP     $7F24               
E1F0: 20 AF E1        JSR     $E1AF               ; {}
E1F3: 4C C7 E1        JMP     $E1C7               ; {}
E1F6: A5 3A           LDA     $3A                 
E1F8: C9 10           CMP     #$10                
E1FA: B0 0C           BCS     $E208               ; {}
E1FC: A9 0F           LDA     #$0F                
E1FE: 8D 95 03        STA     $0395               
E201: 8D 96 03        STA     $0396               
E204: 8D 97 03        STA     $0397               
E207: 60              RTS                         
E208: AD 3D 01        LDA     $013D               
E20B: F0 EF           BEQ     $E1FC               ; {}
E20D: 60              RTS                         
E20E: 0F ; ????
E20F: 20 22 02        JSR     $0222               
E212: 0F ; ????
E213: 2A              ROL     A                   
E214: 17 ; ????
E215: 07 ; ????
E216: 0F ; ????
E217: 37 ; ????
E218: 10 00           BPL     $E21A               ; {}
E21A: 0F ; ????
E21B: 31 27           AND     ($27),Y             
E21D: 15 0F           ORA     $0F,X               
E21F: 20 26 07        JSR     $0726               
E222: 0F ; ????
E223: 31 02           AND     ($02),Y             
E225: 15 0F           ORA     $0F,X               
E227: 11 25           ORA     ($25),Y             
E229: 31 0F           AND     ($0F),Y             
E22B: 20 00 10        JSR     $1000               
E22E: 20 F0 EE        JSR     $EEF0               ; {}
E231: A9 00           LDA     #$00                
E233: 85 38           STA     $38                 
E235: 85 DF           STA     $DF                 
E237: 20 5B E2        JSR     $E25B               ; {}
E23A: A5 3A           LDA     $3A                 
E23C: C9 10           CMP     #$10                
E23E: B0 0F           BCS     $E24F               ; {}
E240: 20 18 7F        JSR     $7F18               
E243: 20 21 7F        JSR     $7F21               
E246: 20 42 EE        JSR     $EE42               ; {}
E249: 20 C9 EB        JSR     $EBC9               ; {}
E24C: 4C EB E1        JMP     $E1EB               ; {}
E24F: 20 1E 7F        JSR     $7F1E               
E252: 20 21 7F        JSR     $7F21               
E255: 20 C9 EB        JSR     $EBC9               ; {}
E258: 4C EB E1        JMP     $E1EB               ; {}
E25B: A0 00           LDY     #$00                
E25D: A9 F8           LDA     #$F8                
E25F: 99 00 02        STA     $0200,Y             
E262: C8              INY                         
E263: D0 FA           BNE     $E25F               ; {}
E265: 60              RTS                         
E266: A2 04           LDX     #$04                
E268: AD 3A 01        LDA     $013A               
E26B: F0 28           BEQ     $E295               ; {}
E26D: A5 14           LDA     $14                 
E26F: 29 08           AND     #$08                
E271: D0 22           BNE     $E295               ; {}
E273: A5 46           LDA     $46                 
E275: 29 07           AND     #$07                
E277: 0A              ASL     A                   
E278: 0A              ASL     A                   
E279: 0A              ASL     A                   
E27A: 18              CLC                         
E27B: 69 A0           ADC     #$A0                
E27D: 9D 03 02        STA     $0203,X             
E280: A5 46           LDA     $46                 
E282: 29 F8           AND     #$F8                
E284: 18              CLC                         
E285: 69 1F           ADC     #$1F                
E287: 9D 00 02        STA     $0200,X             
E28A: A9 0A           LDA     #$0A                
E28C: 9D 01 02        STA     $0201,X             
E28F: A9 01           LDA     #$01                
E291: 9D 02 02        STA     $0202,X             
E294: 60              RTS                         
E295: A9 F8           LDA     #$F8                
E297: 9D 00 02        STA     $0200,X             
E29A: 60              RTS                         
E29B: A2 41           LDX     #$41                
E29D: A9 00           LDA     #$00                
E29F: 9D 31 01        STA     $0131,X             
E2A2: CA              DEX                         
E2A3: 10 FA           BPL     $E29F               ; {}
E2A5: 60              RTS                         
E2A6: A0 00           LDY     #$00                
E2A8: C9 00           CMP     #$00                
E2AA: D0 01           BNE     $E2AD               ; {}
E2AC: 60              RTS                         
E2AD: A0 07           LDY     #$07                
E2AF: C9 80           CMP     #$80                
E2B1: B0 1A           BCS     $E2CD               ; {}
E2B3: 88              DEY                         
E2B4: C9 40           CMP     #$40                
E2B6: B0 15           BCS     $E2CD               ; {}
E2B8: 88              DEY                         
E2B9: C9 20           CMP     #$20                
E2BB: B0 10           BCS     $E2CD               ; {}
E2BD: 88              DEY                         
E2BE: C9 10           CMP     #$10                
E2C0: B0 0B           BCS     $E2CD               ; {}
E2C2: 88              DEY                         
E2C3: C9 05           CMP     #$05                
E2C5: B0 06           BCS     $E2CD               ; {}
E2C7: 88              DEY                         
E2C8: C9 03           CMP     #$03                
E2CA: B0 01           BCS     $E2CD               ; {}
E2CC: 88              DEY                         
E2CD: 98              TYA                         
E2CE: 0A              ASL     A                   
E2CF: A8              TAY                         
E2D0: 60              RTS                         
E2D1: 0A              ASL     A                   
E2D2: 00              BRK                         
E2D3: 64 ; ????
E2D4: 00              BRK                         
E2D5: 2C 01 F4        BIT     $F401               ; {}
E2D8: 01 E8           ORA     ($E8,X)             
E2DA: 03 ; ????
E2DB: D0 07           BNE     $E2E4               ; {}
E2DD: A0 0F           LDY     #$0F                
E2DF: 40              RTI                         
E2E0: 1F ; ????
E2E1: 48              PHA                         
E2E2: 20 AD E2        JSR     $E2AD               ; {}
E2E5: 8A              TXA                         
E2E6: 48              PHA                         
E2E7: A2 00           LDX     #$00                
E2E9: 20 FA E2        JSR     $E2FA               ; {}
E2EC: 68              PLA                         
E2ED: AA              TAX                         
E2EE: 68              PLA                         
E2EF: 60              RTS                         
E2F0: 48              PHA                         
E2F1: 20 AD E2        JSR     $E2AD               ; {}
E2F4: 8A              TXA                         
E2F5: 48              PHA                         
E2F6: A2 03           LDX     #$03                
E2F8: D0 EF           BNE     $E2E9               ; {}
E2FA: B9 D1 E2        LDA     $E2D1,Y             ; {}
E2FD: 18              CLC                         
E2FE: 7D 31 01        ADC     $0131,X             
E301: 9D 31 01        STA     $0131,X             
E304: B9 D2 E2        LDA     $E2D2,Y             ; {}
E307: 7D 32 01        ADC     $0132,X             
E30A: 9D 32 01        STA     $0132,X             
E30D: BD 33 01        LDA     $0133,X             
E310: 69 00           ADC     #$00                
E312: 9D 33 01        STA     $0133,X             
E315: C9 98           CMP     #$98                
E317: 90 1D           BCC     $E336               ; {}
E319: BD 32 01        LDA     $0132,X             
E31C: C9 96           CMP     #$96                
E31E: 90 16           BCC     $E336               ; {}
E320: BD 31 01        LDA     $0131,X             
E323: C9 80           CMP     #$80                
E325: 90 0F           BCC     $E336               ; {}
E327: A9 7F           LDA     #$7F                
E329: 9D 31 01        STA     $0131,X             
E32C: A9 96           LDA     #$96                
E32E: 9D 32 01        STA     $0132,X             
E331: A9 98           LDA     #$98                
E333: 9D 33 01        STA     $0133,X             
E336: 60              RTS                         
E337: 20 A6 E2        JSR     $E2A6               ; {}
E33A: AD 34 01        LDA     $0134               
E33D: 38              SEC                         
E33E: F9 D1 E2        SBC     $E2D1,Y             ; {}
E341: 8D 28 01        STA     $0128               
E344: AD 35 01        LDA     $0135               
E347: F9 D2 E2        SBC     $E2D2,Y             ; {}
E34A: 8D 29 01        STA     $0129               
E34D: AD 36 01        LDA     $0136               
E350: E9 00           SBC     #$00                
E352: 8D 2A 01        STA     $012A               
E355: B0 0C           BCS     $E363               ; {}
E357: A9 00           LDA     #$00                
E359: A0 02           LDY     #$02                
E35B: 99 34 01        STA     $0134,Y             
E35E: 88              DEY                         
E35F: 10 FA           BPL     $E35B               ; {}
E361: 30 0B           BMI     $E36E               ; {}
E363: A0 02           LDY     #$02                
E365: B9 28 01        LDA     $0128,Y             
E368: 99 34 01        STA     $0134,Y             
E36B: 88              DEY                         
E36C: 10 F7           BPL     $E365               ; {}
E36E: A5 08           LDA     $08                 
E370: 60              RTS                         
E371: A9 72           LDA     #$72                
E373: 85 08           STA     $08                 
E375: A9 E6           LDA     #$E6                
E377: 85 09           STA     $09                 
E379: 20 9F E3        JSR     $E39F               ; {}
E37C: 20 CB E7        JSR     $E7CB               ; {}
E37F: 20 E7 E3        JSR     $E3E7               ; {}
E382: AD E2 04        LDA     $04E2               
E385: 48              PHA                         
E386: A9 08           LDA     #$08                
E388: 20 90 CA        JSR     $CA90               ; {}
E38B: 68              PLA                         
E38C: 8D E2 04        STA     $04E2               
E38F: 60              RTS                         
E390: A9 77           LDA     #$77                
E392: 85 08           STA     $08                 
E394: A9 E6           LDA     #$E6                
E396: 85 09           STA     $09                 
E398: A9 20           LDA     #$20                
E39A: 85 00           STA     $00                 ; {ram.GP_00}
E39C: 4C 79 E3        JMP     $E379               ; {}
E39F: 20 A6 E3        JSR     $E3A6               ; {}
E3A2: 20 C5 E3        JSR     $E3C5               ; {}
E3A5: 60              RTS                         
E3A6: A0 00           LDY     #$00                
E3A8: B9 2F 01        LDA     $012F,Y             
E3AB: AA              TAX                         
E3AC: E8              INX                         
E3AD: D0 01           BNE     $E3B0               ; {}
E3AF: CA              DEX                         
E3B0: 8A              TXA                         
E3B1: 99 38 01        STA     $0138,Y             
E3B4: C8              INY                         
E3B5: C0 02           CPY     #$02                
E3B7: 90 EF           BCC     $E3A8               ; {}
E3B9: A5 3A           LDA     $3A                 
E3BB: C9 10           CMP     #$10                
E3BD: 90 05           BCC     $E3C4               ; {}
E3BF: A9 04           LDA     #$04                
E3C1: 8D 39 01        STA     $0139               
E3C4: 60              RTS                         
E3C5: A9 00           LDA     #$00                
E3C7: 85 05           STA     $05                 
E3C9: AD 51 01        LDA     $0151               
E3CC: AA              TAX                         
E3CD: 4A              LSR     A                   
E3CE: 4A              LSR     A                   
E3CF: 4A              LSR     A                   
E3D0: 4A              LSR     A                   
E3D1: 4A              LSR     A                   
E3D2: 4A              LSR     A                   
E3D3: A8              TAY                         
E3D4: 8A              TXA                         
E3D5: 29 1F           AND     #$1F                
E3D7: D9 E3 E3        CMP     $E3E3,Y             ; {}
E3DA: 90 03           BCC     $E3DF               ; {}
E3DC: B9 E3 E3        LDA     $E3E3,Y             ; {}
E3DF: 8D 3C 01        STA     $013C               
E3E2: 60              RTS                         
E3E3: 01 08           ORA     ($08,X)             
E3E5: 08              PHP                         
E3E6: 08              PHP                         
E3E7: 20 F9 E3        JSR     $E3F9               ; {}
E3EA: 20 07 E4        JSR     $E407               ; {}
E3ED: 20 4D E4        JSR     $E44D               ; {}
E3F0: 20 62 E4        JSR     $E462               ; {}
E3F3: 20 7D E4        JSR     $E47D               ; {}
E3F6: 4C 68 E5        JMP     $E568               ; {}
E3F9: A9 F8           LDA     #$F8                
E3FB: A2 00           LDX     #$00                
E3FD: 9D 00 02        STA     $0200,X             
E400: E8              INX                         
E401: E8              INX                         
E402: E8              INX                         
E403: E8              INX                         
E404: D0 F7           BNE     $E3FD               ; {}
E406: 60              RTS                         
E407: A9 00           LDA     #$00                
E409: A8              TAY                         
E40A: AA              TAX                         
E40B: A9 08           LDA     #$08                
E40D: 85 03           STA     $03                 
E40F: 98              TYA                         
E410: 0A              ASL     A                   
E411: 18              CLC                         
E412: 69 41           ADC     #$41                
E414: 85 C5           STA     $C5                 
E416: A9 E4           LDA     #$E4                
E418: 69 00           ADC     #$00                
E41A: 85 C6           STA     $C6                 
E41C: 84 BA           STY     $BA                 
E41E: A0 00           LDY     #$00                
E420: B1 C5           LDA     ($C5),Y             
E422: 85 C7           STA     $C7                 
E424: C8              INY                         
E425: B1 C5           LDA     ($C5),Y             
E427: 85 C8           STA     $C8                 
E429: 88              DEY                         
E42A: B1 C7           LDA     ($C7),Y             
E42C: F0 06           BEQ     $E434               ; {}
E42E: BD B2 E5        LDA     $E5B2,X             ; {}
E431: 9D 40 02        STA     $0240,X             
E434: E8              INX                         
E435: C6 03           DEC     $03                 
E437: D0 F1           BNE     $E42A               ; {}
E439: A4 BA           LDY     $BA                 
E43B: C8              INY                         
E43C: C0 06           CPY     #$06                
E43E: 90 CB           BCC     $E40B               ; {}
E440: 60              RTS                         
E441: 4E 01 4F        LSR     $4F01               
E444: 01 50           ORA     ($50,X)             
E446: 01 3A           ORA     ($3A,X)             
E448: 01 3B           ORA     ($3B,X)             
E44A: 01 51           ORA     ($51,X)             
E44C: 01 AD           ORA     ($AD,X)             
E44E: 51 01           EOR     ($01),Y             
E450: 29 C0           AND     #$C0                
E452: F0 0D           BEQ     $E461               ; {}
E454: A2 00           LDX     #$00                
E456: BD E2 E5        LDA     $E5E2,X             ; {}
E459: 9D 68 02        STA     $0268,X             
E45C: E8              INX                         
E45D: E0 10           CPX     #$10                
E45F: D0 F5           BNE     $E456               ; {}
E461: 60              RTS                         
E462: AE 52 01        LDX     $0152               
E465: E8              INX                         
E466: E0 05           CPX     #$05                
E468: 90 02           BCC     $E46C               ; {}
E46A: A2 05           LDX     #$05                
E46C: 8A              TXA                         
E46D: 0A              ASL     A                   
E46E: 0A              ASL     A                   
E46F: A8              TAY                         
E470: A2 00           LDX     #$00                
E472: BD F2 E5        LDA     $E5F2,X             ; {}
E475: 9D 78 02        STA     $0278,X             
E478: E8              INX                         
E479: 88              DEY                         
E47A: D0 F6           BNE     $E472               ; {}
E47C: 60              RTS                         
E47D: 20 83 E4        JSR     $E483               ; {}
E480: 4C FC E4        JMP     $E4FC               ; {}
E483: A9 00           LDA     #$00                
E485: 85 07           STA     $07                 
E487: A6 07           LDX     $07                 
E489: A9 E4           LDA     #$E4                
E48B: 48              PHA                         
E48C: A9 97           LDA     #$97                
E48E: 48              PHA                         
E48F: BD 3E 01        LDA     $013E,X             
E492: F0 0D           BEQ     $E4A1               ; {}
E494: 10 2E           BPL     $E4C4               ; {}
E496: 30 09           BMI     $E4A1               ; {}
E498: E6 07           INC     $07                 
E49A: A5 07           LDA     $07                 
E49C: C9 03           CMP     #$03                
E49E: 90 E7           BCC     $E487               ; {}
E4A0: 60              RTS                         
E4A1: E8              INX                         
E4A2: 86 01           STX     $01                 
E4A4: CA              DEX                         
E4A5: A0 00           LDY     #$00                
E4A7: B9 41 01        LDA     $0141,Y             
E4AA: C5 01           CMP     $01                 
E4AC: F0 06           BEQ     $E4B4               ; {}
E4AE: C8              INY                         
E4AF: C0 03           CPY     #$03                
E4B1: 90 F4           BCC     $E4A7               ; {}
E4B3: 60              RTS                         
E4B4: BD 65 E5        LDA     $E565,X             ; {}
E4B7: 85 01           STA     $01                 
E4B9: BD 3E 01        LDA     $013E,X             
E4BC: 29 03           AND     #$03                
E4BE: 05 01           ORA     $01                 
E4C0: 99 41 01        STA     $0141,Y             
E4C3: 60              RTS                         
E4C4: E8              INX                         
E4C5: 86 01           STX     $01                 
E4C7: CA              DEX                         
E4C8: BD 65 E5        LDA     $E565,X             ; {}
E4CB: 85 02           STA     $02                 
E4CD: A0 00           LDY     #$00                
E4CF: B9 41 01        LDA     $0141,Y             
E4D2: C5 01           CMP     $01                 
E4D4: F0 25           BEQ     $E4FB               ; {}
E4D6: 29 F0           AND     #$F0                
E4D8: C5 02           CMP     $02                 
E4DA: F0 12           BEQ     $E4EE               ; {}
E4DC: C8              INY                         
E4DD: C0 03           CPY     #$03                
E4DF: 90 EE           BCC     $E4CF               ; {}
E4E1: A0 00           LDY     #$00                
E4E3: B9 41 01        LDA     $0141,Y             
E4E6: F0 0E           BEQ     $E4F6               ; {}
E4E8: C8              INY                         
E4E9: C0 03           CPY     #$03                
E4EB: 90 F6           BCC     $E4E3               ; {}
E4ED: 60              RTS                         
E4EE: B9 41 01        LDA     $0141,Y             
E4F1: 29 0F           AND     #$0F                
E4F3: 9D 3E 01        STA     $013E,X             
E4F6: A5 01           LDA     $01                 
E4F8: 99 41 01        STA     $0141,Y             
E4FB: 60              RTS                         
E4FC: A9 00           LDA     #$00                
E4FE: 85 00           STA     $00                 ; {ram.GP_00}
E500: 85 01           STA     $01                 
E502: 85 04           STA     $04                 
E504: A6 00           LDX     $00                 ; {ram.GP_00}
E506: BD 41 01        LDA     $0141,X             
E509: F0 59           BEQ     $E564               ; {}
E50B: 30 4D           BMI     $E55A               ; {}
E50D: A8              TAY                         
E50E: 88              DEY                         
E50F: 84 05           STY     $05                 
E511: B9 3E 01        LDA     $013E,Y             
E514: 29 03           AND     #$03                
E516: A2 00           LDX     #$00                
E518: C9 01           CMP     #$01                
E51A: F0 08           BEQ     $E524               ; {}
E51C: A5 3A           LDA     $3A                 
E51E: C9 10           CMP     #$10                
E520: B0 02           BCS     $E524               ; {}
E522: A2 03           LDX     #$03                
E524: 86 06           STX     $06                 
E526: 18              CLC                         
E527: A5 05           LDA     $05                 
E529: 65 06           ADC     $06                 
E52B: A8              TAY                         
E52C: B9 06 E6        LDA     $E606,Y             ; {}
E52F: AA              TAX                         
E530: A4 01           LDY     $01                 
E532: 84 03           STY     $03                 
E534: A9 08           LDA     #$08                
E536: 85 02           STA     $02                 
E538: BD 0F E6        LDA     $E60F,X             ; {}
E53B: 99 8C 02        STA     $028C,Y             
E53E: E8              INX                         
E53F: C8              INY                         
E540: C6 02           DEC     $02                 
E542: D0 F4           BNE     $E538               ; {}
E544: 84 01           STY     $01                 
E546: A4 04           LDY     $04                 
E548: B9 0C E6        LDA     $E60C,Y             ; {}
E54B: A4 03           LDY     $03                 
E54D: C8              INY                         
E54E: C8              INY                         
E54F: C8              INY                         
E550: 99 8C 02        STA     $028C,Y             
E553: C8              INY                         
E554: C8              INY                         
E555: C8              INY                         
E556: C8              INY                         
E557: 99 8C 02        STA     $028C,Y             
E55A: E6 04           INC     $04                 
E55C: E6 00           INC     $00                 ; {ram.GP_00}
E55E: A5 00           LDA     $00                 ; {ram.GP_00}
E560: C9 03           CMP     #$03                
E562: 90 A0           BCC     $E504               ; {}
E564: 60              RTS                         
E565: 90 A0           BCC     $E507               ; {}
E567: B0 A2           BCS     $E50B               ; {}
E569: 00              BRK                         
E56A: 86 00           STX     $00                 ; {ram.GP_00}
E56C: 86 01           STX     $01                 
E56E: BD 53 01        LDA     $0153,X             
E571: 20 7D E5        JSR     $E57D               ; {}
E574: E6 00           INC     $00                 ; {ram.GP_00}
E576: A6 00           LDX     $00                 ; {ram.GP_00}
E578: E0 03           CPX     #$03                
E57A: 90 F2           BCC     $E56E               ; {}
E57C: 60              RTS                         
E57D: F0 2B           BEQ     $E5AA               ; {}
E57F: A0 00           LDY     #$00                
E581: C9 01           CMP     #$01                
E583: F0 08           BEQ     $E58D               ; {}
E585: A5 3A           LDA     $3A                 
E587: C9 10           CMP     #$10                
E589: B0 02           BCS     $E58D               ; {}
E58B: A0 03           LDY     #$03                
E58D: 84 06           STY     $06                 
E58F: 18              CLC                         
E590: 8A              TXA                         
E591: 65 06           ADC     $06                 
E593: AA              TAX                         
E594: BD 06 E6        LDA     $E606,X             ; {}
E597: A8              TAY                         
E598: A9 08           LDA     #$08                
E59A: 85 02           STA     $02                 
E59C: A6 01           LDX     $01                 
E59E: B9 42 E6        LDA     $E642,Y             ; {}
E5A1: 9D A4 02        STA     $02A4,X             
E5A4: E8              INX                         
E5A5: C8              INY                         
E5A6: C6 02           DEC     $02                 
E5A8: D0 F4           BNE     $E59E               ; {}
E5AA: A5 01           LDA     $01                 
E5AC: 18              CLC                         
E5AD: 69 08           ADC     #$08                
E5AF: 85 01           STA     $01                 
E5B1: 60              RTS                         
E5B2: 87 ; ????
E5B3: 32 ; ????
E5B4: 21 CC           AND     ($CC,X)             
E5B6: 8F ; ????
E5B7: 33 ; ????
E5B8: 21 CC           AND     ($CC,X)             
E5BA: AF ; ????
E5BB: AA              TAX                         
E5BC: 21 54           AND     ($54,X)             
E5BE: B7 ; ????
E5BF: AB ; ????
E5C0: 21 54           AND     ($54,X)             
E5C2: AF ; ????
E5C3: 9F ; ????
E5C4: 20 7C B7        JSR     $B77C               
E5C7: AF ; ????
E5C8: 20 7C AF        JSR     $AF7C               
E5CB: 8E 21 A4        STX     $A421               
E5CE: B7 ; ????
E5CF: 8F ; ????
E5D0: 20 A4 AF        JSR     $AFA4               
E5D3: 34 ; ????
E5D4: 21 CC           AND     ($CC,X)             
E5D6: B7 ; ????
E5D7: 55 21           EOR     $21,X               
E5D9: CC AF 49        CPY     $49AF               
E5DC: 21 2C           AND     ($2C,X)             
E5DE: B7 ; ????
E5DF: 59 21 2C        EOR     $2C21,Y             
E5E2: AF ; ????
E5E3: 50 20           BVC     $E605               ; {}
E5E5: 28              PLP                         
E5E6: AF ; ????
E5E7: 50 60           BVC     $E649               ; {}
E5E9: 30 B7           BMI     $E5A2               ; {}
E5EB: 51 20           EOR     ($20),Y             
E5ED: 28              PLP                         
E5EE: B7 ; ????
E5EF: 51 60           EOR     ($60),Y             
E5F1: 30 5F           BMI     $E652               ; {}
E5F3: 09 20           ORA     #$20                
E5F5: 68              PLA                         
E5F6: 5F ; ????
E5F7: 09 20           ORA     #$20                
E5F9: 70 5F           BVS     $E65A               ; {}
E5FB: 09 20           ORA     #$20                
E5FD: 78              SEI                         
E5FE: 5F ; ????
E5FF: 09 20           ORA     #$20                
E601: 80 ; ????
E602: 5F ; ????
E603: 09 20           ORA     #$20                
E605: 88              DEY                         
E606: 00              BRK                         
E607: 08              PHP                         
E608: 10 18           BPL     $E622               ; {}
E60A: 20 28 2C        JSR     $2C28               
E60D: 40              RTI                         
E60E: 54 ; ????
E60F: 87 ; ????
E610: 9B ; ????
E611: 23 ; ????
E612: 2C 8F 9C        BIT     $9C8F               
E615: 23 ; ????
E616: 2C 87 3E        BIT     $3E87               
E619: 23 ; ????
E61A: 40              RTI                         
E61B: 8F ; ????
E61C: 3E A3 40        ROL     $40A3,X             
E61F: 87 ; ????
E620: 95 23           STA     $23,X               
E622: 54 ; ????
E623: 8F ; ????
E624: 96 23           STX     $23,Y               
E626: 54 ; ????
E627: 87 ; ????
E628: 9B ; ????
E629: 21 2C           AND     ($2C,X)             
E62B: 8F ; ????
E62C: 9C ; ????
E62D: 21 2C           AND     ($2C,X)             
E62F: 87 ; ????
E630: 3E 20 40        ROL     $4020,X             
E633: 8F ; ????
E634: 3E A0 40        ROL     $40A0,X             
E637: 87 ; ????
E638: 95 21           STA     $21,X               
E63A: 54 ; ????
E63B: 8F ; ????
E63C: 96 21           STX     $21,Y               
E63E: 54 ; ????
E63F: 7C ; ????
E640: 90 A4           BCC     $E5E6               ; {}
E642: 87 ; ????
E643: 38              SEC                         
E644: 20 7C 8F        JSR     $8F7C               
E647: 39 20 7C        AND     $7C20,Y             
E64A: 87 ; ????
E64B: 38              SEC                         
E64C: 20 90 8F        JSR     $8F90               
E64F: 39 20 90        AND     $9020,Y             
E652: 87 ; ????
E653: 38              SEC                         
E654: 20 A4 8F        JSR     $8FA4               
E657: 39 20 A4        AND     $A420,Y             
E65A: 87 ; ????
E65B: 9D 21 7C        STA     $7C21,X             
E65E: 8F ; ????
E65F: 9E ; ????
E660: 21 7C           AND     ($7C,X)             
E662: 87 ; ????
E663: 12 ; ????
E664: 21 90           AND     ($90,X)             
E666: 8F ; ????
E667: 13 ; ????
E668: 21 90           AND     ($90,X)             
E66A: 87 ; ????
E66B: 30 20           BMI     $E68D               ; {}
E66D: A4 8F           LDY     $8F                 
E66F: 31 20           AND     ($20),Y             
E671: A4 01           LDY     $01                 
E673: 20 12 8B        JSR     $8B12               
E676: E7 ; ????
E677: 06 00           ASL     $00                 ; {ram.GP_00}
E679: 00              BRK                         
E67A: 10 4E           BPL     $E6CA               ; {}
E67C: 4F ; ????
E67D: 06 20           ASL     $20                 
E67F: 00              BRK                         
E680: 10 4F           BPL     $E6D1               ; {}
E682: 4E 06 80        LSR     $8006               
E685: 03 ; ????
E686: 10 4E           BPL     $E6D6               ; {}
E688: 4F ; ????
E689: 06 A0           ASL     $A0                 
E68B: 03 ; ????
E68C: 10 4F           BPL     $E6DD               ; {}
E68E: 4E 07 40        LSR     $4007               ; {hard.S_SQR2_D}
E691: 00              BRK                         
E692: 02 ; ????
E693: 8F ; ????
E694: 07 ; ????
E695: 5E 00 02        LSR     $0200,X             
E698: 8F ; ????
E699: 05 60           ORA     $60                 
E69B: 00              BRK                         
E69C: 98              TYA                         
E69D: 91 05           STA     ($05),Y             
E69F: 61 00           ADC     ($00,X)             ; {ram.GP_00}
E6A1: 98              TYA                         
E6A2: 92 ; ????
E6A3: 05 7E           ORA     $7E                 
E6A5: 00              BRK                         
E6A6: 98              TYA                         
E6A7: 91 05           STA     ($05),Y             
E6A9: 7F ; ????
E6AA: 00              BRK                         
E6AB: 98              TYA                         
E6AC: 92 ; ????
E6AD: 07 ; ????
E6AE: 60              RTS                         
E6AF: 03 ; ????
E6B0: 02 ; ????
E6B1: 6D 07 7E        ADC     $7E07               
E6B4: 03 ; ????
E6B5: 02 ; ????
E6B6: 6D 05 E3        ADC     $E305               ; {}
E6B9: 01 1A           ORA     ($1A,X)             
E6BB: 6F ; ????
E6BC: 05 83           ORA     $83                 
E6BE: 02 ; ????
E6BF: 1A ; ????
E6C0: 6F ; ????
E6C1: 05 43           ORA     $43                 
E6C3: 03 ; ????
E6C4: 1A ; ????
E6C5: 6F ; ????
E6C6: 05 03           ORA     $03                 
E6C8: 02 ; ????
E6C9: 8A              TXA                         
E6CA: 6F ; ????
E6CB: 05 A8           ORA     $A8                 
E6CD: 02 ; ????
E6CE: 85 6F           STA     $6F                 
E6D0: 05 0D           ORA     $0D                 
E6D2: 02 ; ????
E6D3: 8A              TXA                         
E6D4: 6F ; ????
E6D5: 05 B2           ORA     $B2                 
E6D7: 02 ; ????
E6D8: 85 6F           STA     $6F                 
E6DA: 05 17           ORA     $17                 
E6DC: 02 ; ????
E6DD: 8A              TXA                         
E6DE: 6F ; ????
E6DF: 05 1C           ORA     $1C                 
E6E1: 02 ; ????
E6E2: 8A              TXA                         
E6E3: 6F ; ????
E6E4: 03 ; ????
E6E5: 87 ; ????
E6E6: 00              BRK                         
E6E7: 05 7C           ORA     $7C                 
E6E9: E7 ; ????
E6EA: 03 ; ????
E6EB: C7 ; ????
E6EC: 00              BRK                         
E6ED: 05 81           ORA     $81                 
E6EF: E7 ; ????
E6F0: 04 ; ????
E6F1: 05 01           ORA     $01                 
E6F3: 07 ; ????
E6F4: 7B ; ????
E6F5: 12 ; ????
E6F6: 1D 1A 16        ORA     $161A,X             
E6F9: 27 ; ????
E6FA: 29 04           AND     #$04                
E6FC: 43 ; ????
E6FD: 01 09           ORA     ($09,X)             
E6FF: 1A ; ????
E700: 23 ; ????
E701: 19 2A 27        ORA     $272A,Y             
E704: 16 23           ASL     $23,X               
E706: 18              CLC                         
E707: 1A ; ????
E708: 04 ; ????
E709: 84 01           STY     $01                 
E70B: 08              PHP                         
E70C: 28              PLP                         
E70D: 29 27           AND     #$27                
E70F: 1A ; ????
E710: 23 ; ????
E711: 1C ; ????
E712: 29 1D           AND     #$1D                
E714: 03 ; ????
E715: B4 01           LDY     $01,X               
E717: 05 86           ORA     $86                 
E719: E7 ; ????
E71A: 04 ; ????
E71B: E4 01           CPX     $01                 
E71D: 08              PHP                         
E71E: 6F ; ????
E71F: 2C 1A 16        BIT     $161A               
E722: 25 24           AND     $24                 
E724: 23 ; ????
E725: 28              PLP                         
E726: 04 ; ????
E727: EE 01 09        INC     $0901               
E72A: 29 27           AND     #$27                
E72C: 1A ; ????
E72D: 16 28           ASL     $28,X               
E72F: 2A              ROL     A                   
E730: 27 ; ????
E731: 1A ; ????
E732: 28              PLP                         
E733: 10 8C           BPL     $E6C1               ; {}
E735: 00              BRK                         
E736: 07 ; ????
E737: 44 ; ????
E738: 01 12           ORA     ($12,X)             
E73A: 10 CC           BPL     $E708               ; {}
E73C: 00              BRK                         
E73D: 07 ; ????
E73E: 31 01           AND     ($01),Y             
E740: 12 ; ????
E741: 10 0D           BPL     $E750               ; {}
E743: 01 03           ORA     ($03,X)             
E745: 4A              LSR     A                   
E746: 01 12           ORA     ($12,X)             
E748: 10 B9           BPL     $E703               ; {}
E74A: 01 01           ORA     ($01,X)             
E74C: 38              SEC                         
E74D: 01 12           ORA     ($12,X)             
E74F: 10 BB           BPL     $E70C               ; {}
E751: 01 01           ORA     ($01,X)             
E753: 39 01 00        AND     $0001,Y             
E756: 02 ; ????
E757: BA              TSX                         
E758: 01 0F           ORA     ($0F,X)             
E75A: 10 05           BPL     $E761               ; {}
E75C: 03 ; ????
E75D: 02 ; ????
E75E: 3C ; ????
E75F: 01 12           ORA     ($12,X)             
E761: 10 0A           BPL     $E76D               ; {}
E763: 03 ; ????
E764: 02 ; ????
E765: 4F ; ????
E766: 01 12           ORA     ($12,X)             
E768: 10 0F           BPL     $E779               ; {}
E76A: 03 ; ????
E76B: 02 ; ????
E76C: 50 01           BVC     $E76F               ; {}
E76E: 12 ; ????
E76F: 04 ; ????
E770: 74 ; ????
E771: 00              BRK                         
E772: 08              PHP                         
E773: 12 ; ????
E774: 22 ; ????
E775: 12 ; ????
E776: 16 12           ASL     $12,X               
E778: 25 12           AND     $12                 
E77A: 12 ; ????
E77B: 00              BRK                         
E77C: 29 24           AND     #$24                
E77E: 29 16           AND     #$16                
E780: 21 28           AND     ($28,X)             
E782: 18              CLC                         
E783: 24 27           BIT     $27                 
E785: 1A ; ????
E786: 28              PLP                         
E787: 29 16           AND     #$16                
E789: 1C ; ????
E78A: 1A ; ????
E78B: 2A              ROL     A                   
E78C: 0A              ASL     A                   
E78D: 0A              ASL     A                   
E78E: 0A              ASL     A                   
E78F: 0A              ASL     A                   
E790: 0A              ASL     A                   
E791: 0A              ASL     A                   
E792: 8A              TXA                         
E793: 22 ; ????
E794: 88              DEY                         
E795: AA              TAX                         
E796: 00              BRK                         
E797: 00              BRK                         
E798: 55 55           EOR     $55,X               
E79A: 88              DEY                         
E79B: E2 ; ????
E79C: FF ; ????
E79D: FF ; ????
E79E: 00              BRK                         
E79F: 00              BRK                         
E7A0: 55 55           EOR     $55,X               
E7A2: 88              DEY                         
E7A3: A2 AF           LDX     #$AF                
E7A5: AF ; ????
E7A6: A0 A0           LDY     #$A0                
E7A8: A0 A0           LDY     #$A0                
E7AA: A8              TAY                         
E7AB: AA              TAX                         
E7AC: 00              BRK                         
E7AD: 00              BRK                         
E7AE: 22 ; ????
E7AF: 00              BRK                         
E7B0: 88              DEY                         
E7B1: 00              BRK                         
E7B2: AA              TAX                         
E7B3: AA              TAX                         
E7B4: 0A              ASL     A                   
E7B5: 2A              ROL     A                   
E7B6: 2A              ROL     A                   
E7B7: 8A              TXA                         
E7B8: 8A              TXA                         
E7B9: 0A              ASL     A                   
E7BA: AA              TAX                         
E7BB: AA              TAX                         
E7BC: A0 A2           LDY     #$A2                
E7BE: A2 A8           LDX     #$A8                
E7C0: A8              TAY                         
E7C1: A0 AA           LDY     #$AA                
E7C3: 0A              ASL     A                   
E7C4: 0A              ASL     A                   
E7C5: 0A              ASL     A                   
E7C6: 0A              ASL     A                   
E7C7: 0A              ASL     A                   
E7C8: 0A              ASL     A                   
E7C9: 0A              ASL     A                   
E7CA: 0A              ASL     A                   
E7CB: A0 00           LDY     #$00                
E7CD: 20 4B EA        JSR     $EA4B               ; {}
E7D0: D0 0F           BNE     $E7E1               ; {}
E7D2: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
E7D5: AD 00 01        LDA     $0100               
E7D8: 29 FB           AND     #$FB                
E7DA: 8D 00 01        STA     $0100               
E7DD: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
E7E0: 60              RTS                         
E7E1: 30 EA           BMI     $E7CD               ; {}
E7E3: 38              SEC                         
E7E4: E9 01           SBC     #$01                
E7E6: 0A              ASL     A                   
E7E7: AA              TAX                         
E7E8: BD FB E7        LDA     $E7FB,X             ; {}
E7EB: 85 0A           STA     $0A                 
E7ED: BD FC E7        LDA     $E7FC,X             ; {}
E7F0: 85 0B           STA     $0B                 
E7F2: A9 E7           LDA     #$E7                
E7F4: 48              PHA                         
E7F5: A9 CC           LDA     #$CC                
E7F7: 48              PHA                         
E7F8: 6C 0A 00        JMP     ($000A)             
E7FB: 1B ; ????
E7FC: E8              INX                         
E7FD: 68              PLA                         
E7FE: E8              INX                         
E7FF: 72 ; ????
E800: E8              INX                         
E801: 8C E8 9D        STY     $9DE8               
E804: E8              INX                         
E805: AE E8 CD        LDX     $CDE8               ; {}
E808: E8              INX                         
E809: E1 E8           SBC     ($E8,X)             
E80B: 03 ; ????
E80C: E9 1C           SBC     #$1C                
E80E: E9 3C           SBC     #$3C                
E810: E9 3C           SBC     #$3C                
E812: E9 3C           SBC     #$3C                
E814: E9 3C           SBC     #$3C                
E816: E9 3C           SBC     #$3C                
E818: E9 79           SBC     #$79                
E81A: E9 20           SBC     #$20                
E81C: 4B ; ????
E81D: EA              NOP                         
E81E: 85 00           STA     $00                 ; {ram.GP_00}
E820: AE 02 20        LDX     $2002               ; {hard.P_STATUS}
E823: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
E826: A9 00           LDA     #$00                
E828: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
E82B: 20 4B EA        JSR     $EA4B               ; {}
E82E: 20 3B E8        JSR     $E83B               ; {}
E831: 20 4B EA        JSR     $EA4B               ; {}
E834: AA              TAX                         
E835: 20 4B EA        JSR     $EA4B               ; {}
E838: 4C 4B E8        JMP     $E84B               ; {}
E83B: A2 00           LDX     #$00                
E83D: 20 61 E8        JSR     $E861               ; {}
E840: 20 61 E8        JSR     $E861               ; {}
E843: 20 61 E8        JSR     $E861               ; {}
E846: A2 C0           LDX     #$C0                
E848: 4C 61 E8        JMP     $E861               ; {}
E84B: 86 0C           STX     $0C                 
E84D: 85 0D           STA     $0D                 
E84F: 84 01           STY     $01                 
E851: A2 40           LDX     #$40                
E853: A0 00           LDY     #$00                
E855: B1 0C           LDA     ($0C),Y             
E857: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
E85A: C8              INY                         
E85B: CA              DEX                         
E85C: D0 F7           BNE     $E855               ; {}
E85E: A4 01           LDY     $01                 
E860: 60              RTS                         
E861: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
E864: CA              DEX                         
E865: D0 FA           BNE     $E861               ; {}
E867: 60              RTS                         
E868: 20 3D E9        JSR     $E93D               ; {}
E86B: 20 4B EA        JSR     $EA4B               ; {}
E86E: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
E871: 60              RTS                         
E872: 20 3D E9        JSR     $E93D               ; {}
E875: 20 51 E9        JSR     $E951               ; {}
E878: 20 6E E9        JSR     $E96E               ; {}
E87B: 84 01           STY     $01                 
E87D: A0 00           LDY     #$00                
E87F: B1 0C           LDA     ($0C),Y             
E881: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
E884: C8              INY                         
E885: C6 02           DEC     $02                 
E887: D0 F6           BNE     $E87F               ; {}
E889: A4 01           LDY     $01                 
E88B: 60              RTS                         
E88C: 20 3D E9        JSR     $E93D               ; {}
E88F: 20 51 E9        JSR     $E951               ; {}
E892: AA              TAX                         
E893: 20 4B EA        JSR     $EA4B               ; {}
E896: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
E899: CA              DEX                         
E89A: D0 F7           BNE     $E893               ; {}
E89C: 60              RTS                         
E89D: 20 3D E9        JSR     $E93D               ; {}
E8A0: 20 51 E9        JSR     $E951               ; {}
E8A3: AA              TAX                         
E8A4: 20 4B EA        JSR     $EA4B               ; {}
E8A7: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
E8AA: CA              DEX                         
E8AB: D0 FA           BNE     $E8A7               ; {}
E8AD: 60              RTS                         
E8AE: 20 3D E9        JSR     $E93D               ; {}
E8B1: 20 51 E9        JSR     $E951               ; {}
E8B4: AA              TAX                         
E8B5: 20 4B EA        JSR     $EA4B               ; {}
E8B8: 85 04           STA     $04                 
E8BA: 20 4B EA        JSR     $EA4B               ; {}
E8BD: 85 05           STA     $05                 
E8BF: A5 04           LDA     $04                 
E8C1: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
E8C4: A5 05           LDA     $05                 
E8C6: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
E8C9: CA              DEX                         
E8CA: D0 F3           BNE     $E8BF               ; {}
E8CC: 60              RTS                         
E8CD: 20 3D E9        JSR     $E93D               ; {}
E8D0: 20 51 E9        JSR     $E951               ; {}
E8D3: AA              TAX                         
E8D4: 20 4B EA        JSR     $EA4B               ; {}
E8D7: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
E8DA: 18              CLC                         
E8DB: 69 01           ADC     #$01                
E8DD: CA              DEX                         
E8DE: D0 F7           BNE     $E8D7               ; {}
E8E0: 60              RTS                         
E8E1: 20 3D E9        JSR     $E93D               ; {}
E8E4: 20 51 E9        JSR     $E951               ; {}
E8E7: 20 6E E9        JSR     $E96E               ; {}
E8EA: 20 4B EA        JSR     $EA4B               ; {}
E8ED: AA              TAX                         
E8EE: 84 01           STY     $01                 
E8F0: A0 00           LDY     #$00                
E8F2: B1 0C           LDA     ($0C),Y             
E8F4: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
E8F7: C8              INY                         
E8F8: 8A              TXA                         
E8F9: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
E8FC: C6 02           DEC     $02                 
E8FE: D0 F2           BNE     $E8F2               ; {}
E900: A4 01           LDY     $01                 
E902: 60              RTS                         
E903: 20 3D E9        JSR     $E93D               ; {}
E906: 20 51 E9        JSR     $E951               ; {}
E909: 20 4B EA        JSR     $EA4B               ; {}
E90C: AA              TAX                         
E90D: 20 4B EA        JSR     $EA4B               ; {}
E910: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
E913: 8A              TXA                         
E914: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
E917: C6 02           DEC     $02                 
E919: D0 F2           BNE     $E90D               ; {}
E91B: 60              RTS                         
E91C: 20 3D E9        JSR     $E93D               ; {}
E91F: 20 51 E9        JSR     $E951               ; {}
E922: 20 4B EA        JSR     $EA4B               ; {}
E925: 85 03           STA     $03                 
E927: 20 4B EA        JSR     $EA4B               ; {}
E92A: 85 04           STA     $04                 
E92C: A5 03           LDA     $03                 
E92E: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
E931: E6 03           INC     $03                 
E933: A5 04           LDA     $04                 
E935: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
E938: C6 02           DEC     $02                 
E93A: D0 F0           BNE     $E92C               ; {}
E93C: 60              RTS                         
E93D: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
E940: 20 4B EA        JSR     $EA4B               ; {}
E943: AA              TAX                         
E944: 20 4B EA        JSR     $EA4B               ; {}
E947: 18              CLC                         
E948: 65 00           ADC     $00                 ; {ram.GP_00}
E94A: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
E94D: 8E 06 20        STX     $2006               ; {hard.P_VRAM_ADDR}
E950: 60              RTS                         
E951: 20 4B EA        JSR     $EA4B               ; {}
E954: AA              TAX                         
E955: 29 80           AND     #$80                
E957: 08              PHP                         
E958: AD 00 01        LDA     $0100               
E95B: 29 FB           AND     #$FB                
E95D: 28              PLP                         
E95E: F0 02           BEQ     $E962               ; {}
E960: 09 04           ORA     #$04                
E962: 8D 00 01        STA     $0100               
E965: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
E968: 8A              TXA                         
E969: 29 7F           AND     #$7F                
E96B: 85 02           STA     $02                 
E96D: 60              RTS                         
E96E: 20 4B EA        JSR     $EA4B               ; {}
E971: 85 0C           STA     $0C                 
E973: 20 4B EA        JSR     $EA4B               ; {}
E976: 85 0D           STA     $0D                 
E978: 60              RTS                         
E979: 20 94 E9        JSR     $E994               ; {}
E97C: 84 01           STY     $01                 
E97E: 20 CF E9        JSR     $E9CF               ; {}
E981: B0 05           BCS     $E988               ; {}
E983: 20 E6 E9        JSR     $E9E6               ; {}
E986: B0 03           BCS     $E98B               ; {}
E988: 20 1C EA        JSR     $EA1C               ; {}
E98B: 20 27 EA        JSR     $EA27               ; {}
E98E: 20 3B EA        JSR     $EA3B               ; {}
E991: A4 01           LDY     $01                 
E993: 60              RTS                         
E994: A9 00           LDA     #$00                
E996: 85 05           STA     $05                 
E998: 85 06           STA     $06                 
E99A: 85 07           STA     $07                 
E99C: 20 3D E9        JSR     $E93D               ; {}
E99F: 20 4B EA        JSR     $EA4B               ; {}
E9A2: 85 02           STA     $02                 
E9A4: AA              TAX                         
E9A5: 20 4B EA        JSR     $EA4B               ; {}
E9A8: 85 0C           STA     $0C                 
E9AA: 20 4B EA        JSR     $EA4B               ; {}
E9AD: 85 0D           STA     $0D                 
E9AF: 20 4B EA        JSR     $EA4B               ; {}
E9B2: 85 03           STA     $03                 
E9B4: BD 55 EA        LDA     $EA55,X             ; {}
E9B7: 84 01           STY     $01                 
E9B9: A8              TAY                         
E9BA: B1 0C           LDA     ($0C),Y             
E9BC: 99 05 00        STA     $0005,Y             
E9BF: 88              DEY                         
E9C0: 10 F8           BPL     $E9BA               ; {}
E9C2: A4 01           LDY     $01                 
E9C4: A2 06           LDX     #$06                
E9C6: A9 00           LDA     #$00                
E9C8: 9D 28 01        STA     $0128,X             
E9CB: CA              DEX                         
E9CC: 10 FA           BPL     $E9C8               ; {}
E9CE: 60              RTS                         
E9CF: A6 02           LDX     $02                 
E9D1: BD 65 EA        LDA     $EA65,X             ; {}
E9D4: AA              TAX                         
E9D5: 38              SEC                         
E9D6: A5 05           LDA     $05                 
E9D8: FD 6D EA        SBC     $EA6D,X             ; {}
E9DB: A5 06           LDA     $06                 
E9DD: FD 6E EA        SBC     $EA6E,X             ; {}
E9E0: A5 07           LDA     $07                 
E9E2: FD 6F EA        SBC     $EA6F,X             ; {}
E9E5: 60              RTS                         
E9E6: A2 00           LDX     #$00                
E9E8: A0 00           LDY     #$00                
E9EA: 20 F6 E9        JSR     $E9F6               ; {}
E9ED: E8              INX                         
E9EE: C8              INY                         
E9EF: C8              INY                         
E9F0: C8              INY                         
E9F1: E0 07           CPX     #$07                
E9F3: 90 F5           BCC     $E9EA               ; {}
E9F5: 60              RTS                         
E9F6: 38              SEC                         
E9F7: A5 05           LDA     $05                 
E9F9: F9 70 EA        SBC     $EA70,Y             ; {}
E9FC: 85 0D           STA     $0D                 
E9FE: A5 06           LDA     $06                 
EA00: F9 71 EA        SBC     $EA71,Y             ; {}
EA03: 85 0E           STA     $0E                 
EA05: A5 07           LDA     $07                 
EA07: F9 72 EA        SBC     $EA72,Y             ; {}
EA0A: 90 0F           BCC     $EA1B               ; {}
EA0C: 85 07           STA     $07                 
EA0E: A5 0E           LDA     $0E                 
EA10: 85 06           STA     $06                 
EA12: A5 0D           LDA     $0D                 
EA14: 85 05           STA     $05                 
EA16: FE 28 01        INC     $0128,X             
EA19: D0 DB           BNE     $E9F6               ; {}
EA1B: 60              RTS                         
EA1C: A2 06           LDX     #$06                
EA1E: A9 09           LDA     #$09                
EA20: 9D 28 01        STA     $0128,X             
EA23: CA              DEX                         
EA24: 10 FA           BPL     $EA20               ; {}
EA26: 60              RTS                         
EA27: A2 00           LDX     #$00                
EA29: BD 28 01        LDA     $0128,X             
EA2C: C9 00           CMP     #$00                
EA2E: D0 0A           BNE     $EA3A               ; {}
EA30: A5 03           LDA     $03                 
EA32: 9D 28 01        STA     $0128,X             
EA35: E8              INX                         
EA36: E0 06           CPX     #$06                
EA38: 90 EF           BCC     $EA29               ; {}
EA3A: 60              RTS                         
EA3B: A6 02           LDX     $02                 
EA3D: BD 5D EA        LDA     $EA5D,X             ; {}
EA40: A8              TAY                         
EA41: B9 28 01        LDA     $0128,Y             
EA44: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
EA47: C8              INY                         
EA48: CA              DEX                         
EA49: D0 F6           BNE     $EA41               ; {}
EA4B: B1 08           LDA     ($08),Y             
EA4D: 08              PHP                         
EA4E: C8              INY                         
EA4F: D0 02           BNE     $EA53               ; {}
EA51: E6 09           INC     $09                 
EA53: 28              PLP                         
EA54: 60              RTS                         
EA55: 00              BRK                         
EA56: 00              BRK                         
EA57: 00              BRK                         
EA58: 01 01           ORA     ($01,X)             
EA5A: 02 ; ????
EA5B: 02 ; ????
EA5C: 02 ; ????
EA5D: 07 ; ????
EA5E: 06 05           ASL     $05                 
EA60: 04 ; ????
EA61: 03 ; ????
EA62: 02 ; ????
EA63: 01 00           ORA     ($00,X)             ; {ram.GP_00}
EA65: 15 12           ORA     $12,X               
EA67: 0F ; ????
EA68: 0C ; ????
EA69: 09 06           ORA     #$06                
EA6B: 03 ; ????
EA6C: 00              BRK                         
EA6D: 80 ; ????
EA6E: 96 98           STX     $98,Y               
EA70: 40              RTI                         
EA71: 42 ; ????
EA72: 0F ; ????
EA73: A0 86           LDY     #$86                
EA75: 01 10           ORA     ($10,X)             
EA77: 27 ; ????
EA78: 00              BRK                         
EA79: E8              INX                         
EA7A: 03 ; ????
EA7B: 00              BRK                         
EA7C: 64 ; ????
EA7D: 00              BRK                         
EA7E: 00              BRK                         
EA7F: 0A              ASL     A                   
EA80: 00              BRK                         
EA81: 00              BRK                         
EA82: 01 00           ORA     ($00,X)             ; {ram.GP_00}
EA84: 00              BRK                         
EA85: A0 04           LDY     #$04                
EA87: D0 05           BNE     $EA8E               ; {}
EA89: 20 BB EA        JSR     $EABB               ; {}
EA8C: A0 17           LDY     #$17                
EA8E: B9 3E 01        LDA     $013E,Y             
EA91: 99 57 01        STA     $0157,Y             
EA94: 88              DEY                         
EA95: 10 F7           BPL     $EA8E               ; {}
EA97: A5 AA           LDA     $AA                 
EA99: 8D 70 01        STA     $0170               
EA9C: A5 A6           LDA     $A6                 
EA9E: 8D 71 01        STA     $0171               
EAA1: 60              RTS                         
EAA2: 20 BB EA        JSR     $EABB               ; {}
EAA5: A0 17           LDY     #$17                
EAA7: B9 57 01        LDA     $0157,Y             
EAAA: 99 3E 01        STA     $013E,Y             
EAAD: 88              DEY                         
EAAE: 10 F7           BPL     $EAA7               ; {}
EAB0: AD 70 01        LDA     $0170               
EAB3: 85 AA           STA     $AA                 
EAB5: AD 71 01        LDA     $0171               
EAB8: 85 A6           STA     $A6                 
EABA: 60              RTS                         
EABB: A0 0C           LDY     #$0C                
EABD: A9 00           LDA     #$00                
EABF: 99 31 01        STA     $0131,Y             
EAC2: 88              DEY                         
EAC3: 10 FA           BPL     $EABF               ; {}
EAC5: 60              RTS                         
EAC6: AD 4F 01        LDA     $014F               
EAC9: C9 63           CMP     #$63                
EACB: B0 09           BCS     $EAD6               ; {}
EACD: EE 4F 01        INC     $014F               
EAD0: A9 01           LDA     #$01                
EAD2: 20 F0 E2        JSR     $E2F0               ; {}
EAD5: 18              CLC                         
EAD6: 60              RTS                         
EAD7: A5 3A           LDA     $3A                 
EAD9: 29 F0           AND     #$F0                
EADB: D0 F9           BNE     $EAD6               ; {}
EADD: A5 3B           LDA     $3B                 
EADF: 29 0F           AND     #$0F                
EAE1: AA              TAX                         
EAE2: A5 3A           LDA     $3A                 
EAE4: 29 0F           AND     #$0F                
EAE6: C9 02           CMP     #$02                
EAE8: F0 09           BEQ     $EAF3               ; {}
EAEA: C9 05           CMP     #$05                
EAEC: F0 05           BEQ     $EAF3               ; {}
EAEE: DD F8 EA        CMP     $EAF8,X             ; {}
EAF1: D0 E3           BNE     $EAD6               ; {}
EAF3: A9 00           LDA     #$00                
EAF5: 4C 90 CA        JMP     $CA90               ; {}
EAF8: 0B ; ????
EAF9: 0B ; ????
EAFA: 0A              ASL     A                   
EAFB: 0D 0B 0B        ORA     $0B0B               
EAFE: 0B ; ????
EAFF: 0A              ASL     A                   
EB00: 00              BRK                         
EB01: AD 2F 01        LDA     $012F               
EB04: 4A              LSR     A                   
EB05: B0 16           BCS     $EB1D               ; {}
EB07: A9 0F           LDA     #$0F                
EB09: 8D FF 9F        STA     $9FFF               
EB0C: 4A              LSR     A                   
EB0D: 8D FF 9F        STA     $9FFF               
EB10: 4A              LSR     A                   
EB11: 8D FF 9F        STA     $9FFF               
EB14: 4A              LSR     A                   
EB15: 8D FF 9F        STA     $9FFF               
EB18: 4A              LSR     A                   
EB19: 8D FF 9F        STA     $9FFF               
EB1C: 60              RTS                         
EB1D: A9 0E           LDA     #$0E                
EB1F: D0 E8           BNE     $EB09               ; {}
EB21: A5 26           LDA     $26                 
EB23: 6A              ROR     A                   
EB24: 6A              ROR     A                   
EB25: 18              CLC                         
EB26: 69 03           ADC     #$03                
EB28: 18              CLC                         
EB29: 69 20           ADC     #$20                
EB2B: 85 26           STA     $26                 
EB2D: 60              RTS                         
EB2E: A9 00           LDA     #$00                
EB30: 8D 03 20        STA     $2003               ; {hard.P_SPR_ADDR}
EB33: A9 02           LDA     #$02                
EB35: 8D 14 40        STA     $4014               ; {hard.P_SPR_DMA}
EB38: 60              RTS                         
EB39: A2 01           LDX     #$01                
EB3B: 8E 16 40        STX     $4016               ; {hard.4016}
EB3E: CA              DEX                         
EB3F: 8E 16 40        STX     $4016               ; {hard.4016}
EB42: A2 08           LDX     #$08                
EB44: AD 16 40        LDA     $4016               ; {hard.4016}
EB47: 4A              LSR     A                   
EB48: 26 F6           ROL     $F6                 
EB4A: 4A              LSR     A                   
EB4B: 26 00           ROL     $00                 ; {ram.GP_00}
EB4D: AD 17 40        LDA     $4017               ; {hard.S_FrameCntr}
EB50: 4A              LSR     A                   
EB51: 26 F7           ROL     $F7                 
EB53: 4A              LSR     A                   
EB54: 26 01           ROL     $01                 
EB56: CA              DEX                         
EB57: D0 EB           BNE     $EB44               ; {}
EB59: A5 00           LDA     $00                 ; {ram.GP_00}
EB5B: 05 F6           ORA     $F6                 
EB5D: 85 F6           STA     $F6                 
EB5F: A5 01           LDA     $01                 
EB61: 05 F7           ORA     $F7                 
EB63: 85 F7           STA     $F7                 
EB65: A2 01           LDX     #$01                
EB67: B5 F6           LDA     $F6,X               
EB69: A8              TAY                         
EB6A: 55 F8           EOR     $F8,X               
EB6C: 35 F6           AND     $F6,X               
EB6E: 95 F6           STA     $F6,X               
EB70: 94 F8           STY     $F8,X               
EB72: CA              DEX                         
EB73: 10 F2           BPL     $EB67               ; {}
EB75: 60              RTS                         
EB76: 85 00           STA     $00                 ; {ram.GP_00}
EB78: 86 01           STX     $01                 
EB7A: 84 02           STY     $02                 
EB7C: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
EB7F: AD 00 01        LDA     $0100               
EB82: 29 FB           AND     #$FB                
EB84: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
EB87: A5 00           LDA     $00                 ; {ram.GP_00}
EB89: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
EB8C: A0 00           LDY     #$00                
EB8E: 8C 06 20        STY     $2006               ; {hard.P_VRAM_ADDR}
EB91: A2 04           LDX     #$04                
EB93: C9 20           CMP     #$20                
EB95: B0 02           BCS     $EB99               ; {}
EB97: A6 02           LDX     $02                 
EB99: A0 00           LDY     #$00                
EB9B: A5 01           LDA     $01                 
EB9D: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
EBA0: 88              DEY                         
EBA1: D0 FA           BNE     $EB9D               ; {}
EBA3: CA              DEX                         
EBA4: D0 F7           BNE     $EB9D               ; {}
EBA6: A4 02           LDY     $02                 
EBA8: A5 00           LDA     $00                 ; {ram.GP_00}
EBAA: C9 20           CMP     #$20                
EBAC: 90 12           BCC     $EBC0               ; {}
EBAE: 69 02           ADC     #$02                
EBB0: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
EBB3: A9 C0           LDA     #$C0                
EBB5: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
EBB8: A2 40           LDX     #$40                
EBBA: 8C 07 20        STY     $2007               ; {hard.P_VRAM_DATA}
EBBD: CA              DEX                         
EBBE: D0 FA           BNE     $EBBA               ; {}
EBC0: A6 01           LDX     $01                 
EBC2: AD 00 01        LDA     $0100               
EBC5: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
EBC8: 60              RTS                         
EBC9: AD 02 20        LDA     $2002               ; {hard.P_STATUS}
EBCC: A5 FE           LDA     $FE                 
EBCE: 8D 05 20        STA     $2005               ; {hard.P_BKG_SCROLL}
EBD1: A5 FD           LDA     $FD                 
EBD3: 8D 05 20        STA     $2005               ; {hard.P_BKG_SCROLL}
EBD6: A5 1B           LDA     $1B                 
EBD8: 29 01           AND     #$01                
EBDA: 85 00           STA     $00                 ; {ram.GP_00}
EBDC: A5 1A           LDA     $1A                 
EBDE: 49 FF           EOR     #$FF                
EBE0: 29 01           AND     #$01                
EBE2: 0A              ASL     A                   
EBE3: 05 00           ORA     $00                 ; {ram.GP_00}
EBE5: 85 00           STA     $00                 ; {ram.GP_00}
EBE7: AD 00 01        LDA     $0100               
EBEA: 29 FC           AND     #$FC                
EBEC: 05 00           ORA     $00                 ; {ram.GP_00}
EBEE: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
EBF1: 8D 00 01        STA     $0100               
EBF4: 60              RTS                         
EBF5: A9 00           LDA     #$00                
EBF7: 85 04           STA     $04                 
EBF9: 85 05           STA     $05                 
EBFB: A5 00           LDA     $00                 ; {ram.GP_00}
EBFD: 38              SEC                         
EBFE: E9 10           SBC     #$10                
EC00: 85 02           STA     $02                 
EC02: A5 01           LDA     $01                 
EC04: E9 27           SBC     #$27                
EC06: 90 08           BCC     $EC10               ; {}
EC08: 85 01           STA     $01                 
EC0A: A5 02           LDA     $02                 
EC0C: 85 00           STA     $00                 ; {ram.GP_00}
EC0E: B0 EB           BCS     $EBFB               ; {}
EC10: A5 00           LDA     $00                 ; {ram.GP_00}
EC12: 38              SEC                         
EC13: E9 E8           SBC     #$E8                
EC15: 85 02           STA     $02                 
EC17: A5 01           LDA     $01                 
EC19: E9 03           SBC     #$03                
EC1B: 90 0E           BCC     $EC2B               ; {}
EC1D: 85 01           STA     $01                 
EC1F: A5 02           LDA     $02                 
EC21: 85 00           STA     $00                 ; {ram.GP_00}
EC23: A5 05           LDA     $05                 
EC25: 69 0F           ADC     #$0F                
EC27: 85 05           STA     $05                 
EC29: D0 E5           BNE     $EC10               ; {}
EC2B: A5 00           LDA     $00                 ; {ram.GP_00}
EC2D: 38              SEC                         
EC2E: E9 64           SBC     #$64                
EC30: 85 02           STA     $02                 
EC32: A5 01           LDA     $01                 
EC34: E9 00           SBC     #$00                
EC36: 90 0E           BCC     $EC46               ; {}
EC38: 85 01           STA     $01                 
EC3A: A5 02           LDA     $02                 
EC3C: 85 00           STA     $00                 ; {ram.GP_00}
EC3E: A5 05           LDA     $05                 
EC40: 69 00           ADC     #$00                
EC42: 85 05           STA     $05                 
EC44: D0 E5           BNE     $EC2B               ; {}
EC46: A5 00           LDA     $00                 ; {ram.GP_00}
EC48: 38              SEC                         
EC49: E9 0A           SBC     #$0A                
EC4B: 85 02           STA     $02                 
EC4D: A5 01           LDA     $01                 
EC4F: E9 00           SBC     #$00                
EC51: 90 0E           BCC     $EC61               ; {}
EC53: 85 01           STA     $01                 
EC55: A5 02           LDA     $02                 
EC57: 85 00           STA     $00                 ; {ram.GP_00}
EC59: A5 04           LDA     $04                 
EC5B: 69 0F           ADC     #$0F                
EC5D: 85 04           STA     $04                 
EC5F: D0 E5           BNE     $EC46               ; {}
EC61: A5 00           LDA     $00                 ; {ram.GP_00}
EC63: 05 04           ORA     $04                 
EC65: 85 04           STA     $04                 
EC67: 60              RTS                         
EC68: A2 38           LDX     #$38                
EC6A: A0 05           LDY     #$05                
EC6C: A9 00           LDA     #$00                
EC6E: 9D 01 07        STA     $0701,X             
EC71: A9 F8           LDA     #$F8                
EC73: 9D 00 02        STA     $0200,X             
EC76: 9D 00 07        STA     $0700,X             
EC79: E8              INX                         
EC7A: E8              INX                         
EC7B: E8              INX                         
EC7C: E8              INX                         
EC7D: 88              DEY                         
EC7E: 10 EC           BPL     $EC6C               ; {}
EC80: 60              RTS                         
EC81: A5 18           LDA     $18                 
EC83: 29 20           AND     #$20                
EC85: F0 0C           BEQ     $EC93               ; {}
EC87: E6 A5           INC     $A5                 
EC89: A5 A5           LDA     $A5                 
EC8B: 09 80           ORA     #$80                
EC8D: 85 A5           STA     $A5                 
EC8F: 20 68 EC        JSR     $EC68               ; {}
EC92: 60              RTS                         
EC93: A5 A5           LDA     $A5                 
EC95: 29 7F           AND     #$7F                
EC97: 85 A5           STA     $A5                 
EC99: 60              RTS                         
EC9A: A0 00           LDY     #$00                
EC9C: B9 EE ED        LDA     $EDEE,Y             ; {}
EC9F: 9D 00 02        STA     $0200,X             
ECA2: E8              INX                         
ECA3: E8              INX                         
ECA4: E8              INX                         
ECA5: C8              INY                         
ECA6: B9 EE ED        LDA     $EDEE,Y             ; {}
ECA9: 9D 00 02        STA     $0200,X             
ECAC: E8              INX                         
ECAD: C8              INY                         
ECAE: E0 20           CPX     #$20                
ECB0: 90 EA           BCC     $EC9C               ; {}
ECB2: 60              RTS                         
ECB3: A2 FC           LDX     #$FC                
ECB5: A0 04           LDY     #$04                
ECB7: 20 1C ED        JSR     $ED1C               ; {}
ECBA: A5 14           LDA     $14                 
ECBC: 29 03           AND     #$03                
ECBE: F0 03           BEQ     $ECC3               ; {}
ECC0: 4C 10 ED        JMP     $ED10               ; {}
ECC3: A2 00           LDX     #$00                
ECC5: A0 10           LDY     #$10                
ECC7: 20 9C EC        JSR     $EC9C               ; {}
ECCA: A9 D0           LDA     #$D0                
ECCC: 4C FC EC        JMP     $ECFC               ; {}
ECCF: 20 10 ED        JSR     $ED10               ; {}
ECD2: 20 F5 EC        JSR     $ECF5               ; {}
ECD5: 20 EE EC        JSR     $ECEE               ; {}
ECD8: 60              RTS                         
ECD9: AD 2F 01        LDA     $012F               
ECDC: C9 03           CMP     #$03                
ECDE: F0 EF           BEQ     $ECCF               ; {}
ECE0: A5 14           LDA     $14                 
ECE2: 29 07           AND     #$07                
ECE4: F0 2A           BEQ     $ED10               ; {}
ECE6: C9 01           CMP     #$01                
ECE8: F0 10           BEQ     $ECFA               ; {}
ECEA: C9 02           CMP     #$02                
ECEC: F0 07           BEQ     $ECF5               ; {}
ECEE: A2 FC           LDX     #$FC                
ECF0: A0 00           LDY     #$00                
ECF2: 4C 1C ED        JMP     $ED1C               ; {}
ECF5: A2 00           LDX     #$00                
ECF7: 20 9A EC        JSR     $EC9A               ; {}
ECFA: A9 18           LDA     #$18                
ECFC: 85 04           STA     $04                 
ECFE: A2 0C           LDX     #$0C                
ED00: A5 AA           LDA     $AA                 
ED02: 85 02           STA     $02                 
ED04: A5 A6           LDA     $A6                 
ED06: 85 03           STA     $03                 
ED08: 20 74 ED        JSR     $ED74               ; {}
ED0B: A5 03           LDA     $03                 
ED0D: 85 A6           STA     $A6                 
ED0F: 60              RTS                         
ED10: A2 00           LDX     #$00                
ED12: 4C 3D ED        JMP     $ED3D               ; {}
ED15: 20 FC EC        JSR     $ECFC               ; {}
ED18: 20 10 ED        JSR     $ED10               ; {}
ED1B: 60              RTS                         
ED1C: B9 35 ED        LDA     $ED35,Y             ; {}
ED1F: 9D 00 02        STA     $0200,X             
ED22: B9 36 ED        LDA     $ED36,Y             ; {}
ED25: 9D 01 02        STA     $0201,X             
ED28: B9 37 ED        LDA     $ED37,Y             ; {}
ED2B: 9D 02 02        STA     $0202,X             
ED2E: B9 38 ED        LDA     $ED38,Y             ; {}
ED31: 9D 03 02        STA     $0203,X             
ED34: 60              RTS                         
ED35: 10 27           BPL     $ED5E               ; {}
ED37: 01 18           ORA     ($18,X)             
ED39: C8              INY                         
ED3A: 27 ; ????
ED3B: 01 78           ORA     ($78,X)             
ED3D: AD 4A 01        LDA     $014A               
ED40: 85 00           STA     $00                 ; {ram.GP_00}
ED42: AD 4B 01        LDA     $014B               
ED45: 85 01           STA     $01                 
ED47: 20 F5 EB        JSR     $EBF5               ; {}
ED4A: A5 04           LDA     $04                 
ED4C: 48              PHA                         
ED4D: 29 F0           AND     #$F0                
ED4F: 20 26 EE        JSR     $EE26               ; {}
ED52: 09 60           ORA     #$60                
ED54: 9D 05 02        STA     $0205,X             
ED57: 68              PLA                         
ED58: 29 0F           AND     #$0F                
ED5A: 09 60           ORA     #$60                
ED5C: 9D 09 02        STA     $0209,X             
ED5F: A5 05           LDA     $05                 
ED61: 29 0F           AND     #$0F                
ED63: 09 60           ORA     #$60                
ED65: 9D 01 02        STA     $0201,X             
ED68: A9 01           LDA     #$01                
ED6A: 9D 02 02        STA     $0202,X             
ED6D: 9D 06 02        STA     $0206,X             
ED70: 9D 0A 02        STA     $020A,X             
ED73: 60              RTS                         
ED74: 8A              TXA                         
ED75: 48              PHA                         
ED76: A4 02           LDY     $02                 
ED78: C0 05           CPY     #$05                
ED7A: 90 02           BCC     $ED7E               ; {}
ED7C: A0 04           LDY     #$04                
ED7E: 84 00           STY     $00                 ; {ram.GP_00}
ED80: A5 04           LDA     $04                 
ED82: 9D 00 02        STA     $0200,X             
ED85: E8              INX                         
ED86: A9 87           LDA     #$87                
ED88: 9D 00 02        STA     $0200,X             
ED8B: E8              INX                         
ED8C: A9 01           LDA     #$01                
ED8E: 9D 00 02        STA     $0200,X             
ED91: E8              INX                         
ED92: E8              INX                         
ED93: 88              DEY                         
ED94: 10 EA           BPL     $ED80               ; {}
ED96: A5 03           LDA     $03                 
ED98: 4A              LSR     A                   
ED99: 4A              LSR     A                   
ED9A: 4A              LSR     A                   
ED9B: C5 00           CMP     $00                 ; {ram.GP_00}
ED9D: 90 0F           BCC     $EDAE               ; {}
ED9F: F0 0D           BEQ     $EDAE               ; {}
EDA1: A5 00           LDA     $00                 ; {ram.GP_00}
EDA3: 18              CLC                         
EDA4: 69 01           ADC     #$01                
EDA6: 0A              ASL     A                   
EDA7: 0A              ASL     A                   
EDA8: 0A              ASL     A                   
EDA9: 38              SEC                         
EDAA: E9 01           SBC     #$01                
EDAC: 85 03           STA     $03                 
EDAE: 68              PLA                         
EDAF: AA              TAX                         
EDB0: A9 80           LDA     #$80                
EDB2: A4 03           LDY     $03                 
EDB4: C0 08           CPY     #$08                
EDB6: 90 20           BCC     $EDD8               ; {}
EDB8: C0 10           CPY     #$10                
EDBA: 90 19           BCC     $EDD5               ; {}
EDBC: C0 18           CPY     #$18                
EDBE: 90 12           BCC     $EDD2               ; {}
EDC0: C0 20           CPY     #$20                
EDC2: 90 0B           BCC     $EDCF               ; {}
EDC4: C0 28           CPY     #$28                
EDC6: 90 04           BCC     $EDCC               ; {}
EDC8: A0 27           LDY     #$27                
EDCA: 84 03           STY     $03                 
EDCC: 9D 0D 02        STA     $020D,X             
EDCF: 9D 09 02        STA     $0209,X             
EDD2: 9D 05 02        STA     $0205,X             
EDD5: 9D 01 02        STA     $0201,X             
EDD8: 98              TYA                         
EDD9: 29 38           AND     #$38                
EDDB: 4A              LSR     A                   
EDDC: 85 00           STA     $00                 ; {ram.GP_00}
EDDE: 8A              TXA                         
EDDF: 18              CLC                         
EDE0: 65 00           ADC     $00                 ; {ram.GP_00}
EDE2: AA              TAX                         
EDE3: 98              TYA                         
EDE4: 49 FF           EOR     #$FF                
EDE6: 29 07           AND     #$07                
EDE8: 09 80           ORA     #$80                
EDEA: 9D 01 02        STA     $0201,X             
EDED: 60              RTS                         
EDEE: 10 20           BPL     $EE10               ; {}
EDF0: 10 28           BPL     $EE1A               ; {}
EDF2: 10 30           BPL     $EE24               ; {}
EDF4: F8              SED                         
EDF5: 18              CLC                         
EDF6: F8              SED                         
EDF7: 20 F8 28        JSR     $28F8               
EDFA: F8              SED                         
EDFB: 30 F8           BMI     $EDF5               ; {}
EDFD: 38              SEC                         
EDFE: C8              INY                         
EDFF: 80 ; ????
EE00: C8              INY                         
EE01: 88              DEY                         
EE02: C8              INY                         
EE03: 90 F8           BCC     $EDFD               ; {}
EE05: 78              SEI                         
EE06: F8              SED                         
EE07: 80 ; ????
EE08: F8              SED                         
EE09: 88              DEY                         
EE0A: F8              SED                         
EE0B: 90 F8           BCC     $EE05               ; {}
EE0D: 98              TYA                         
EE0E: A2 0C           LDX     #$0C                
EE10: A9 68           LDA     #$68                
EE12: A0 4F           LDY     #$4F                
EE14: 9D 03 02        STA     $0203,X             
EE17: 18              CLC                         
EE18: 69 08           ADC     #$08                
EE1A: E8              INX                         
EE1B: E8              INX                         
EE1C: E8              INX                         
EE1D: E8              INX                         
EE1E: E0 20           CPX     #$20                
EE20: 90 F2           BCC     $EE14               ; {}
EE22: 98              TYA                         
EE23: 4C 15 ED        JMP     $ED15               ; {}
EE26: 4A              LSR     A                   
EE27: 4A              LSR     A                   
EE28: 4A              LSR     A                   
EE29: 4A              LSR     A                   
EE2A: 60              RTS                         
EE2B: 0A              ASL     A                   
EE2C: A8              TAY                         
EE2D: C8              INY                         
EE2E: 68              PLA                         
EE2F: 85 00           STA     $00                 ; {ram.GP_00}
EE31: 68              PLA                         
EE32: 85 01           STA     $01                 
EE34: B1 00           LDA     ($00),Y             ; {ram.GP_00}
EE36: 48              PHA                         
EE37: C8              INY                         
EE38: B1 00           LDA     ($00),Y             ; {ram.GP_00}
EE3A: 85 01           STA     $01                 
EE3C: 68              PLA                         
EE3D: 85 00           STA     $00                 ; {ram.GP_00}
EE3F: 6C 00 00        JMP     ($0000)             ; {ram.GP_00}
EE42: A9 3F           LDA     #$3F                
EE44: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
EE47: A0 00           LDY     #$00                
EE49: 8C 06 20        STY     $2006               ; {hard.P_VRAM_ADDR}
EE4C: B9 90 03        LDA     $0390,Y             
EE4F: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
EE52: C8              INY                         
EE53: C0 20           CPY     #$20                
EE55: 90 F5           BCC     $EE4C               ; {}
EE57: A9 3F           LDA     #$3F                
EE59: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
EE5C: A9 00           LDA     #$00                
EE5E: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
EE61: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
EE64: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
EE67: 4C C9 EB        JMP     $EBC9               ; {}
EE6A: AD 16 40        LDA     $4016               ; {hard.4016}
EE6D: 29 04           AND     #$04                
EE6F: 85 73           STA     $73                 
EE71: 20 39 EB        JSR     $EB39               ; {}
EE74: A5 F8           LDA     $F8                 
EE76: 85 16           STA     $16                 
EE78: 85 17           STA     $17                 
EE7A: A5 F6           LDA     $F6                 
EE7C: 85 18           STA     $18                 
EE7E: 85 19           STA     $19                 
EE80: 60              RTS                         
EE81: AD 16 40        LDA     $4016               ; {hard.4016}
EE84: 29 04           AND     #$04                
EE86: 85 73           STA     $73                 
EE88: 20 39 EB        JSR     $EB39               ; {}
EE8B: A5 F8           LDA     $F8                 
EE8D: 85 17           STA     $17                 
EE8F: A5 F6           LDA     $F6                 
EE91: 85 19           STA     $19                 
EE93: 60              RTS                         
EE94: E6 14           INC     $14                 
EE96: D0 02           BNE     $EE9A               ; {}
EE98: E6 15           INC     $15                 
EE9A: 60              RTS                         
EE9B: A2 60           LDX     #$60                
EE9D: A4 43           LDY     $43                 
EE9F: A9 1F           LDA     #$1F                
EEA1: 85 00           STA     $00                 ; {ram.GP_00}
EEA3: BD 00 02        LDA     $0200,X             
EEA6: 48              PHA                         
EEA7: B9 00 02        LDA     $0200,Y             
EEAA: 9D 00 02        STA     $0200,X             
EEAD: 68              PLA                         
EEAE: 99 00 02        STA     $0200,Y             
EEB1: E8              INX                         
EEB2: C8              INY                         
EEB3: C6 00           DEC     $00                 ; {ram.GP_00}
EEB5: 10 EC           BPL     $EEA3               ; {}
EEB7: 60              RTS                         
EEB8: A5 43           LDA     $43                 
EEBA: 18              CLC                         
EEBB: 69 20           ADC     #$20                
EEBD: C9 60           CMP     #$60                
EEBF: B0 02           BCS     $EEC3               ; {}
EEC1: A9 60           LDA     #$60                
EEC3: 85 43           STA     $43                 
EEC5: A8              TAY                         
EEC6: A2 60           LDX     #$60                
EEC8: D0 D5           BNE     $EE9F               ; {}
EECA: A9 00           LDA     #$00                
EECC: AA              TAX                         
EECD: 9D 00 02        STA     $0200,X             
EED0: 9D 00 07        STA     $0700,X             
EED3: E8              INX                         
EED4: D0 F7           BNE     $EECD               ; {}
EED6: A9 F8           LDA     #$F8                
EED8: 9D 00 02        STA     $0200,X             
EEDB: 9D 00 07        STA     $0700,X             
EEDE: E8              INX                         
EEDF: E8              INX                         
EEE0: E8              INX                         
EEE1: E8              INX                         
EEE2: D0 F4           BNE     $EED8               ; {}
EEE4: 60              RTS                         
EEE5: A9 00           LDA     #$00                
EEE7: 85 FD           STA     $FD                 
EEE9: 85 1A           STA     $1A                 
EEEB: 85 FE           STA     $FE                 
EEED: 85 1B           STA     $1B                 
EEEF: 60              RTS                         
EEF0: AD 00 01        LDA     $0100               
EEF3: 29 7F           AND     #$7F                
EEF5: 8D 00 01        STA     $0100               
EEF8: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
EEFB: A9 00           LDA     #$00                
EEFD: 8D 01 20        STA     $2001               ; {hard.P_CNTRL_2}
EF00: 60              RTS                         
EF01: AD 00 01        LDA     $0100               
EF04: 09 80           ORA     #$80                
EF06: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
EF09: 8D 00 01        STA     $0100               
EF0C: A5 FF           LDA     $FF                 
EF0E: 8D 01 20        STA     $2001               ; {hard.P_CNTRL_2}
EF11: 60              RTS                         
EF12: E6 00           INC     $00                 ; {ram.GP_00}
EF14: D0 02           BNE     $EF18               ; {}
EF16: E6 01           INC     $01                 
EF18: 60              RTS                         
EF19: E6 02           INC     $02                 
EF1B: D0 02           BNE     $EF1F               ; {}
EF1D: E6 03           INC     $03                 
EF1F: 60              RTS                         
EF20: A9 20           LDA     #$20                
EF22: 20 27 EF        JSR     $EF27               ; {}
EF25: A9 24           LDA     #$24                
EF27: A2 12           LDX     #$12                
EF29: A0 00           LDY     #$00                
EF2B: 4C 76 EB        JMP     $EB76               ; {}
EF2E: A0 7F           LDY     #$7F                
EF30: A9 00           LDA     #$00                
EF32: 99 B0 03        STA     $03B0,Y             
EF35: 88              DEY                         
EF36: 10 FA           BPL     $EF32               ; {}
EF38: 60              RTS                         
EF39: A9 23           LDA     #$23                
EF3B: 20 5A EF        JSR     $EF5A               ; {}
EF3E: BD B0 03        LDA     $03B0,X             
EF41: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
EF44: E8              INX                         
EF45: E0 40           CPX     #$40                
EF47: 90 F5           BCC     $EF3E               ; {}
EF49: A9 2B           LDA     #$2B                
EF4B: 20 5A EF        JSR     $EF5A               ; {}
EF4E: BD F0 03        LDA     $03F0,X             
EF51: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA}
EF54: E8              INX                         
EF55: E0 40           CPX     #$40                
EF57: 90 F5           BCC     $EF4E               ; {}
EF59: 60              RTS                         
EF5A: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
EF5D: A9 C0           LDA     #$C0                
EF5F: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR}
EF62: A2 00           LDX     #$00                
EF64: 60              RTS                         
EF65: A5 00           LDA     $00                 ; {ram.GP_00}
EF67: 18              CLC                         
EF68: 69 20           ADC     #$20                
EF6A: 85 00           STA     $00                 ; {ram.GP_00}
EF6C: A5 01           LDA     $01                 
EF6E: 69 00           ADC     #$00                
EF70: 85 01           STA     $01                 
EF72: 60              RTS                         
EF73: A9 20           LDA     #$20                
EF75: D0 05           BNE     $EF7C               ; {}
EF77: 20 73 EF        JSR     $EF73               ; {}
EF7A: A9 28           LDA     #$28                
EF7C: A2 12           LDX     #$12                
EF7E: A0 00           LDY     #$00                
EF80: 4C 76 EB        JMP     $EB76               ; {}
EF83: A9 00           LDA     #$00                
EF85: F0 02           BEQ     $EF89               ; {}
EF87: A9 1E           LDA     #$1E                
EF89: 8D 01 20        STA     $2001               ; {hard.P_CNTRL_2}
EF8C: 60              RTS                         
EF8D: 05 07           ORA     $07                 
EF8F: 08              PHP                         
EF90: 06 07           ASL     $07                 
EF92: 08              PHP                         
EF93: 05 06           ORA     $06                 
EF95: 08              PHP                         
EF96: 0A              ASL     A                   
EF97: 05 09           ORA     $09                 
EF99: 05 07           ORA     $07                 
EF9B: 06 06           ASL     $06                 
EF9D: 04 ; ????
EF9E: 08              PHP                         
EF9F: 00              BRK                         
EFA0: 01 02           ORA     ($02,X)             
EFA2: 21 10           AND     ($10,X)             
EFA4: 40              RTI                         
EFA5: 35 27           AND     $27,X               
EFA7: 76 02           ROR     $02,X               
EFA9: 01 05           ORA     ($05,X)             
EFAB: 39 15 63        AND     $6315,Y             
EFAE: 12 ; ????
EFAF: 07 ; ????
EFB0: 20 18 10        JSR     $1018               
EFB3: 25 48           AND     $48                 
EFB5: 50 45           BVC     $EFFC               ; {}
EFB7: 60              RTS                         
EFB8: 50 70           BVC     $F02A               ; {}
EFBA: 01 00           ORA     ($00,X)             ; {ram.GP_00}
EFBC: 00              BRK                         
EFBD: 00              BRK                         
EFBE: 00              BRK                         
EFBF: 01 01           ORA     ($01,X)             
EFC1: 00              BRK                         
EFC2: 00              BRK                         
EFC3: 00              BRK                         
EFC4: 01 01           ORA     ($01,X)             
EFC6: 01 00           ORA     ($00,X)             ; {ram.GP_00}
EFC8: 00              BRK                         
EFC9: 00              BRK                         
EFCA: 01 AE           ORA     ($AE,X)             
EFCC: 24 00           BIT     $00                 ; {ram.GP_00}
EFCE: 06 93           ASL     $93                 
EFD0: 22 ; ????
EFD1: 00              BRK                         
EFD2: 07 ; ????
EFD3: AB ; ????
EFD4: 20 01 01        JSR     $0101               
EFD7: 71 22           ADC     ($22),Y             
EFD9: 01 03           ORA     ($03,X)             
EFDB: D8              CLD                         
EFDC: 26 01           ROL     $01                 
EFDE: 04 ; ????
EFDF: 99 22 01        STA     $0122,Y             
EFE2: 06 B1           ASL     $B1                 
EFE4: 25 01           AND     $01                 
EFE6: 0C ; ????
EFE7: 2C 24 02        BIT     $0224               
EFEA: 02 ; ????
EFEB: 8E 22 02        STX     $0222               
EFEE: 04 ; ????
EFEF: 43 ; ????
EFF0: 25 02           AND     $02                 
EFF2: 06 27           ASL     $27                 
EFF4: 20 02 0D        JSR     $0D02               
EFF7: 01 26           ORA     ($26,X)             
EFF9: 02 ; ????
EFFA: 11 46           ORA     ($46),Y             
EFFC: 23 ; ????
EFFD: FF ; ????
EFFE: FF ; ????
EFFF: 00              BRK                         
F000: 01 AF           ORA     ($AF,X)             
F002: 25 00           AND     $00                 ; {ram.GP_00}
F004: 03 ; ????
F005: AA              TAX                         
F006: 27 ; ????
F007: 00              BRK                         
F008: 05 AD           ORA     $AD                 
F00A: 22 ; ????
F00B: 00              BRK                         
F00C: 0A              ASL     A                   
F00D: 8C 26 00        STY     $0026               
F010: 0D 76 20        ORA     $2076               
F013: 00              BRK                         
F014: 11 76           ORA     ($76),Y             
F016: 24 00           BIT     $00                 ; {ram.GP_00}
F018: 14 ; ????
F019: A8              TAY                         
F01A: 25 00           AND     $00                 ; {ram.GP_00}
F01C: 17 ; ????
F01D: 1E 23 00        ASL     $0023,X             
F020: 19 AA 24        ORA     $24AA,Y             
F023: 01 00           ORA     ($00,X)             ; {ram.GP_00}
F025: A5 20           LDA     $20                 
F027: 01 01           ORA     ($01,X)             
F029: A4 22           LDY     $22                 
F02B: 01 02           ORA     ($02,X)             
F02D: A4 22           LDY     $22                 
F02F: 01 03           ORA     ($03,X)             
F031: A4 24           LDY     $24                 
F033: 01 04           ORA     ($04,X)             
F035: 6A              ROR     A                   
F036: 27 ; ????
F037: 01 07           ORA     ($07,X)             
F039: 89 ; ????
F03A: 22 ; ????
F03B: 01 10           ORA     ($10,X)             
F03D: 9A              TXS                         
F03E: 26 01           ROL     $01                 
F040: 17 ; ????
F041: 9C ; ????
F042: 22 ; ????
F043: 01 1A           ORA     ($1A,X)             
F045: 9C ; ????
F046: 26 02           ROL     $02                 
F048: 07 ; ????
F049: A8              TAY                         
F04A: 20 02 0A        JSR     $0A02               
F04D: AB ; ????
F04E: 23 ; ????
F04F: 02 ; ????
F050: 0F ; ????
F051: AE 25 02        LDX     $0225               
F054: 13 ; ????
F055: 9F ; ????
F056: 22 ; ????
F057: 02 ; ????
F058: 15 AE           ORA     $AE,X               
F05A: 26 FF           ROL     $FF                 
F05C: FF ; ????
F05D: 00              BRK                         
F05E: 00              BRK                         
F05F: BE 27 00        LDX     $0027,Y             
F062: 09 03           ORA     #$03                
F064: 24 01           BIT     $01                 
F066: 03 ; ????
F067: 16 23           ASL     $23,X               
F069: 01 05           ORA     ($05,X)             
F06B: DC ; ????
F06C: 25 01           AND     $01                 
F06E: 09 88           ORA     #$88                
F070: 26 01           ROL     $01                 
F072: 0C ; ????
F073: 49 27           EOR     #$27                
F075: 02 ; ????
F076: 05 5E           ORA     $5E                 
F078: 26 02           ROL     $02                 
F07A: 0F ; ????
F07B: B2 ; ????
F07C: 25 FF           AND     $FF                 
F07E: FF ; ????
F07F: FF ; ????
F080: FF ; ????
F081: 00              BRK                         
F082: 00              BRK                         
F083: 00              BRK                         
F084: 00              BRK                         
F085: 80 ; ????
F086: 12 ; ????
F087: 12 ; ????
F088: 25 1E           AND     $1E                 
F08A: 29 12           AND     #$12                
F08C: 12 ; ????
F08D: 12 ; ????
F08E: 00              BRK                         
F08F: 00              BRK                         
F090: 00              BRK                         
F091: 00              BRK                         
F092: 00              BRK                         
F093: 00              BRK                         
F094: 00              BRK                         
F095: 00              BRK                         
F096: 00              BRK                         
F097: 00              BRK                         
F098: 00              BRK                         
F099: 00              BRK                         
F09A: 00              BRK                         
F09B: 00              BRK                         
F09C: 00              BRK                         
F09D: 00              BRK                         
F09E: 00              BRK                         
F09F: 00              BRK                         
F0A0: 00              BRK                         
F0A1: 00              BRK                         
F0A2: 00              BRK                         
F0A3: 00              BRK                         
F0A4: 00              BRK                         
F0A5: 00              BRK                         
F0A6: 00              BRK                         
F0A7: 00              BRK                         
F0A8: 00              BRK                         
F0A9: 02 ; ????
F0AA: 00              BRK                         
F0AB: 00              BRK                         
F0AC: 00              BRK                         
F0AD: 00              BRK                         
F0AE: 00              BRK                         
F0AF: 00              BRK                         
F0B0: 00              BRK                         
F0B1: 00              BRK                         
F0B2: 00              BRK                         
F0B3: 00              BRK                         
F0B4: 00              BRK                         
F0B5: 00              BRK                         
F0B6: 00              BRK                         
F0B7: 00              BRK                         
F0B8: 00              BRK                         
F0B9: 00              BRK                         
F0BA: 00              BRK                         
F0BB: 00              BRK                         
F0BC: 00              BRK                         
F0BD: 00              BRK                         
F0BE: 00              BRK                         
F0BF: 00              BRK                         
F0C0: 00              BRK                         
F0C1: 00              BRK                         
F0C2: 00              BRK                         
F0C3: 00              BRK                         
F0C4: 00              BRK                         
F0C5: 00              BRK                         
F0C6: 00              BRK                         
F0C7: 00              BRK                         
F0C8: 00              BRK                         
F0C9: 00              BRK                         
F0CA: 00              BRK                         
F0CB: 00              BRK                         
F0CC: 00              BRK                         
F0CD: 00              BRK                         
F0CE: 00              BRK                         
F0CF: 00              BRK                         
F0D0: 00              BRK                         
F0D1: 00              BRK                         
F0D2: 00              BRK                         
F0D3: 00              BRK                         
F0D4: 00              BRK                         
F0D5: 00              BRK                         
F0D6: 00              BRK                         
F0D7: 00              BRK                         
F0D8: 00              BRK                         
F0D9: 00              BRK                         
F0DA: 00              BRK                         
F0DB: 00              BRK                         
F0DC: 00              BRK                         
F0DD: 00              BRK                         
F0DE: 00              BRK                         
F0DF: 00              BRK                         
F0E0: 00              BRK                         
F0E1: 00              BRK                         
F0E2: 44 ; ????
F0E3: 61 00           ADC     ($00,X)             ; {ram.GP_00}
F0E5: 84 DA           STY     $DA                 
F0E7: 00              BRK                         
F0E8: B2 ; ????
F0E9: 00              BRK                         
F0EA: 00              BRK                         
F0EB: 00              BRK                         
F0EC: 00              BRK                         
F0ED: 0E 00 01        ASL     $0100               
F0F0: 01 00           ORA     ($00,X)             ; {ram.GP_00}
F0F2: 00              BRK                         
F0F3: 00              BRK                         
F0F4: 00              BRK                         
F0F5: 01 03           ORA     ($03,X)             
F0F7: 06 00           ASL     $00                 ; {ram.GP_00}
F0F9: 00              BRK                         
F0FA: 20 29 21        JSR     $2129               
F0FD: 0E 0E 0E        ASL     $0E0E               
F100: 0E 0E B0        ASL     $B00E               
F103: 0C ; ????
F104: 07 ; ????
F105: 12 ; ????
F106: 12 ; ????
F107: 12 ; ????
F108: 12 ; ????
F109: 12 ; ????
F10A: 12 ; ????
F10B: 12 ; ????
F10C: 12 ; ????
F10D: 00              BRK                         
F10E: 00              BRK                         
F10F: 00              BRK                         
F110: 12 ; ????
F111: 12 ; ????
F112: 12 ; ????
F113: 12 ; ????
F114: 12 ; ????
F115: 12 ; ????
F116: 12 ; ????
F117: 12 ; ????
F118: 00              BRK                         
F119: 00              BRK                         
F11A: 00              BRK                         
F11B: 12 ; ????
F11C: 12 ; ????
F11D: 12 ; ????
F11E: 12 ; ????
F11F: 12 ; ????
F120: 12 ; ????
F121: 12 ; ????
F122: 12 ; ????
F123: 00              BRK                         
F124: 00              BRK                         
F125: 00              BRK                         
F126: 12 ; ????
F127: 12 ; ????
F128: 12 ; ????
F129: 12 ; ????
F12A: 12 ; ????
F12B: 12 ; ????
F12C: 12 ; ????
F12D: 12 ; ????
F12E: 00              BRK                         
F12F: 00              BRK                         
F130: 00              BRK                         
F131: 00              BRK                         
F132: 00              BRK                         
F133: 00              BRK                         
F134: 00              BRK                         
F135: 00              BRK                         
F136: 00              BRK                         
F137: 00              BRK                         
F138: 00              BRK                         
F139: 00              BRK                         
F13A: 00              BRK                         
F13B: 00              BRK                         
F13C: 00              BRK                         
F13D: 00              BRK                         
F13E: 00              BRK                         
F13F: 00              BRK                         
F140: 00              BRK                         
F141: 00              BRK                         
F142: 00              BRK                         
F143: 00              BRK                         
F144: 00              BRK                         
F145: 00              BRK                         
F146: 00              BRK                         
F147: 00              BRK                         
F148: 00              BRK                         
F149: 00              BRK                         
F14A: 00              BRK                         
F14B: 00              BRK                         
F14C: 00              BRK                         
F14D: 00              BRK                         
F14E: 00              BRK                         
F14F: 00              BRK                         
F150: 00              BRK                         
F151: 00              BRK                         
F152: 00              BRK                         
F153: 00              BRK                         
F154: 00              BRK                         
F155: 00              BRK                         
F156: 00              BRK                         
F157: 00              BRK                         
F158: 00              BRK                         
F159: 00              BRK                         
F15A: 00              BRK                         
F15B: 00              BRK                         
F15C: 00              BRK                         
F15D: 00              BRK                         
F15E: 00              BRK                         
F15F: 00              BRK                         
F160: 00              BRK                         
F161: 00              BRK                         
F162: 00              BRK                         
F163: 00              BRK                         
F164: 00              BRK                         
F165: 00              BRK                         
F166: 00              BRK                         
F167: 00              BRK                         
F168: 00              BRK                         
F169: 00              BRK                         
F16A: 00              BRK                         
F16B: 00              BRK                         
F16C: 00              BRK                         
F16D: 00              BRK                         
F16E: 00              BRK                         
F16F: 00              BRK                         
F170: 00              BRK                         
F171: 00              BRK                         
F172: 00              BRK                         
F173: 00              BRK                         
F174: 00              BRK                         
F175: 00              BRK                         
F176: 00              BRK                         
F177: 00              BRK                         
F178: 00              BRK                         
F179: 00              BRK                         
F17A: 00              BRK                         
F17B: 00              BRK                         
F17C: 00              BRK                         
F17D: 00              BRK                         
F17E: 00              BRK                         
F17F: 00              BRK                         
F180: 00              BRK                         
F181: 00              BRK                         
F182: 00              BRK                         
F183: 00              BRK                         
F184: 00              BRK                         
F185: 00              BRK                         
F186: 00              BRK                         
F187: 00              BRK                         
F188: 00              BRK                         
F189: 00              BRK                         
F18A: 00              BRK                         
F18B: 00              BRK                         
F18C: 00              BRK                         
F18D: 00              BRK                         
F18E: 00              BRK                         
F18F: 00              BRK                         
F190: 00              BRK                         
F191: 00              BRK                         
F192: 00              BRK                         
F193: 00              BRK                         
F194: 00              BRK                         
F195: 00              BRK                         
F196: 00              BRK                         
F197: 00              BRK                         
F198: 00              BRK                         
F199: 00              BRK                         
F19A: 00              BRK                         
F19B: 00              BRK                         
F19C: 00              BRK                         
F19D: 00              BRK                         
F19E: 00              BRK                         
F19F: 00              BRK                         
F1A0: 00              BRK                         
F1A1: 00              BRK                         
F1A2: 00              BRK                         
F1A3: 00              BRK                         
F1A4: 00              BRK                         
F1A5: 00              BRK                         
F1A6: 00              BRK                         
F1A7: 00              BRK                         
F1A8: 00              BRK                         
F1A9: 00              BRK                         
F1AA: 00              BRK                         
F1AB: 00              BRK                         
F1AC: 00              BRK                         
F1AD: 00              BRK                         
F1AE: 00              BRK                         
F1AF: 01 00           ORA     ($00,X)             ; {ram.GP_00}
F1B1: 00              BRK                         
F1B2: 00              BRK                         
F1B3: 00              BRK                         
F1B4: 00              BRK                         
F1B5: 00              BRK                         
F1B6: 00              BRK                         
F1B7: 00              BRK                         
F1B8: 00              BRK                         
F1B9: 00              BRK                         
F1BA: 00              BRK                         
F1BB: 00              BRK                         
F1BC: 00              BRK                         
F1BD: 00              BRK                         
F1BE: 11 08           ORA     ($08),Y             
F1C0: 00              BRK                         
F1C1: 00              BRK                         
F1C2: 00              BRK                         
F1C3: 00              BRK                         
F1C4: 00              BRK                         
F1C5: 00              BRK                         
F1C6: 00              BRK                         
F1C7: 00              BRK                         
F1C8: 00              BRK                         
F1C9: 00              BRK                         
F1CA: 00              BRK                         
F1CB: 00              BRK                         
F1CC: 00              BRK                         
F1CD: 00              BRK                         
F1CE: 00              BRK                         
F1CF: 00              BRK                         
F1D0: 00              BRK                         
F1D1: 00              BRK                         
F1D2: 00              BRK                         
F1D3: 00              BRK                         
F1D4: 00              BRK                         
F1D5: 00              BRK                         
F1D6: 00              BRK                         
F1D7: 00              BRK                         
F1D8: 00              BRK                         
F1D9: 00              BRK                         
F1DA: 00              BRK                         
F1DB: 00              BRK                         
F1DC: 00              BRK                         
F1DD: 00              BRK                         
F1DE: 02 ; ????
F1DF: 01 00           ORA     ($00,X)             ; {ram.GP_00}
F1E1: 00              BRK                         
F1E2: 00              BRK                         
F1E3: 00              BRK                         
F1E4: 00              BRK                         
F1E5: 00              BRK                         
F1E6: 00              BRK                         
F1E7: 00              BRK                         
F1E8: 00              BRK                         
F1E9: 00              BRK                         
F1EA: 00              BRK                         
F1EB: 00              BRK                         
F1EC: 00              BRK                         
F1ED: 00              BRK                         
F1EE: 01 02           ORA     ($02,X)             
F1F0: 00              BRK                         
F1F1: 00              BRK                         
F1F2: 00              BRK                         
F1F3: 00              BRK                         
F1F4: 00              BRK                         
F1F5: 00              BRK                         
F1F6: 00              BRK                         
F1F7: 00              BRK                         
F1F8: 00              BRK                         
F1F9: 00              BRK                         
F1FA: 00              BRK                         
F1FB: 00              BRK                         
F1FC: 05 00           ORA     $00                 ; {ram.GP_00}
F1FE: BE 3E FF        LDX     $FF3E,Y             ; {}
F201: FF ; ????
F202: FF ; ????
F203: FF ; ????
F204: FF ; ????
F205: FF ; ????
F206: FF ; ????
F207: FF ; ????
F208: FF ; ????
F209: FF ; ????
F20A: FF ; ????
F20B: FF ; ????
F20C: FF ; ????
F20D: FF ; ????
F20E: FF ; ????
F20F: FF ; ????
F210: FF ; ????
F211: FF ; ????
F212: FF ; ????
F213: FF ; ????
F214: FF ; ????
F215: FF ; ????
F216: FF ; ????
F217: FF ; ????
F218: FF ; ????
F219: FF ; ????
F21A: FF ; ????
F21B: FF ; ????
F21C: FF ; ????
F21D: FF ; ????
F21E: FF ; ????
F21F: FF ; ????
F220: FF ; ????
F221: FF ; ????
F222: FF ; ????
F223: FF ; ????
F224: FF ; ????
F225: FF ; ????
F226: FF ; ????
F227: FF ; ????
F228: FF ; ????
F229: FF ; ????
F22A: FF ; ????
F22B: FF ; ????
F22C: FF ; ????
F22D: FF ; ????
F22E: FF ; ????
F22F: FF ; ????
F230: FF ; ????
F231: FF ; ????
F232: FF ; ????
F233: FF ; ????
F234: FF ; ????
F235: DF ; ????
F236: FF ; ????
F237: FF ; ????
F238: FF ; ????
F239: FF ; ????
F23A: FF ; ????
F23B: FF ; ????
F23C: FF ; ????
F23D: FF ; ????
F23E: FF ; ????
F23F: FF ; ????
F240: FF ; ????
F241: FF ; ????
F242: FF ; ????
F243: FF ; ????
F244: FF ; ????
F245: FF ; ????
F246: FF ; ????
F247: FF ; ????
F248: FF ; ????
F249: FF ; ????
F24A: FF ; ????
F24B: FF ; ????
F24C: FF ; ????
F24D: FF ; ????
F24E: FF ; ????
F24F: FF ; ????
F250: FF ; ????
F251: FF ; ????
F252: FF ; ????
F253: FF ; ????
F254: FF ; ????
F255: FF ; ????
F256: FF ; ????
F257: FF ; ????
F258: FF ; ????
F259: FF ; ????
F25A: FF ; ????
F25B: FF ; ????
F25C: FF ; ????
F25D: FF ; ????
F25E: FF ; ????
F25F: FF ; ????
F260: FF ; ????
F261: FF ; ????
F262: FF ; ????
F263: FF ; ????
F264: FF ; ????
F265: FF ; ????
F266: FF ; ????
F267: FF ; ????
F268: FF ; ????
F269: FF ; ????
F26A: FF ; ????
F26B: FF ; ????
F26C: FF ; ????
F26D: FF ; ????
F26E: FF ; ????
F26F: FF ; ????
F270: FF ; ????
F271: FF ; ????
F272: FF ; ????
F273: FF ; ????
F274: FF ; ????
F275: BF ; ????
F276: FF ; ????
F277: FF ; ????
F278: FF ; ????
F279: FF ; ????
F27A: FF ; ????
F27B: FF ; ????
F27C: FF ; ????
F27D: FF ; ????
F27E: FF ; ????
F27F: FF ; ????
F280: FF ; ????
F281: FF ; ????
F282: FF ; ????
F283: FF ; ????
F284: FF ; ????
F285: FF ; ????
F286: FF ; ????
F287: FF ; ????
F288: FF ; ????
F289: FF ; ????
F28A: FF ; ????
F28B: FF ; ????
F28C: FF ; ????
F28D: FF ; ????
F28E: FF ; ????
F28F: FF ; ????
F290: FF ; ????
F291: FF ; ????
F292: FF ; ????
F293: FF ; ????
F294: FF ; ????
F295: FF ; ????
F296: FF ; ????
F297: FF ; ????
F298: FF ; ????
F299: FF ; ????
F29A: FF ; ????
F29B: FF ; ????
F29C: BF ; ????
F29D: FF ; ????
F29E: FF ; ????
F29F: FF ; ????
F2A0: FF ; ????
F2A1: FF ; ????
F2A2: FF ; ????
F2A3: FF ; ????
F2A4: FF ; ????
F2A5: BF ; ????
F2A6: FF ; ????
F2A7: FF ; ????
F2A8: FF ; ????
F2A9: FF ; ????
F2AA: FF ; ????
F2AB: FF ; ????
F2AC: FF ; ????
F2AD: FF ; ????
F2AE: FF ; ????
F2AF: FF ; ????
F2B0: FF ; ????
F2B1: FF ; ????
F2B2: FF ; ????
F2B3: FF ; ????
F2B4: FF ; ????
F2B5: FF ; ????
F2B6: FF ; ????
F2B7: FF ; ????
F2B8: FF ; ????
F2B9: FF ; ????
F2BA: FF ; ????
F2BB: FF ; ????
F2BC: FF ; ????
F2BD: FF ; ????
F2BE: FF ; ????
F2BF: FF ; ????
F2C0: FF ; ????
F2C1: FF ; ????
F2C2: FF ; ????
F2C3: FF ; ????
F2C4: FF ; ????
F2C5: FF ; ????
F2C6: FF ; ????
F2C7: FF ; ????
F2C8: FF ; ????
F2C9: FF ; ????
F2CA: FF ; ????
F2CB: FF ; ????
F2CC: FF ; ????
F2CD: FF ; ????
F2CE: FF ; ????
F2CF: FF ; ????
F2D0: FF ; ????
F2D1: FF ; ????
F2D2: FF ; ????
F2D3: FF ; ????
F2D4: FF ; ????
F2D5: FF ; ????
F2D6: FF ; ????
F2D7: FF ; ????
F2D8: FF ; ????
F2D9: FF ; ????
F2DA: FF ; ????
F2DB: FF ; ????
F2DC: FF ; ????
F2DD: FF ; ????
F2DE: FF ; ????
F2DF: FF ; ????
F2E0: FF ; ????
F2E1: FF ; ????
F2E2: FF ; ????
F2E3: FF ; ????
F2E4: FF ; ????
F2E5: FF ; ????
F2E6: FF ; ????
F2E7: FF ; ????
F2E8: FF ; ????
F2E9: FF ; ????
F2EA: FF ; ????
F2EB: FF ; ????
F2EC: FF ; ????
F2ED: FF ; ????
F2EE: FF ; ????
F2EF: FF ; ????
F2F0: FF ; ????
F2F1: FF ; ????
F2F2: FF ; ????
F2F3: FF ; ????
F2F4: FF ; ????
F2F5: FF ; ????
F2F6: FF ; ????
F2F7: FF ; ????
F2F8: FF ; ????
F2F9: FF ; ????
F2FA: FF ; ????
F2FB: FF ; ????
F2FC: FF ; ????
F2FD: BF ; ????
F2FE: FF ; ????
F2FF: FF ; ????
F300: 00              BRK                         
F301: 00              BRK                         
F302: 00              BRK                         
F303: 00              BRK                         
F304: 00              BRK                         
F305: 00              BRK                         
F306: 00              BRK                         
F307: 00              BRK                         
F308: 00              BRK                         
F309: 00              BRK                         
F30A: 00              BRK                         
F30B: 00              BRK                         
F30C: 00              BRK                         
F30D: 00              BRK                         
F30E: 00              BRK                         
F30F: 00              BRK                         
F310: 00              BRK                         
F311: 00              BRK                         
F312: 00              BRK                         
F313: 00              BRK                         
F314: 00              BRK                         
F315: 00              BRK                         
F316: 00              BRK                         
F317: 00              BRK                         
F318: 00              BRK                         
F319: 00              BRK                         
F31A: 00              BRK                         
F31B: 00              BRK                         
F31C: 00              BRK                         
F31D: 00              BRK                         
F31E: 00              BRK                         
F31F: 00              BRK                         
F320: 00              BRK                         
F321: 00              BRK                         
F322: 00              BRK                         
F323: 00              BRK                         
F324: 00              BRK                         
F325: 00              BRK                         
F326: 00              BRK                         
F327: 00              BRK                         
F328: 00              BRK                         
F329: 00              BRK                         
F32A: 00              BRK                         
F32B: 00              BRK                         
F32C: 00              BRK                         
F32D: 00              BRK                         
F32E: 00              BRK                         
F32F: 00              BRK                         
F330: 00              BRK                         
F331: 00              BRK                         
F332: 00              BRK                         
F333: 00              BRK                         
F334: 00              BRK                         
F335: 00              BRK                         
F336: 00              BRK                         
F337: 00              BRK                         
F338: 00              BRK                         
F339: 00              BRK                         
F33A: 00              BRK                         
F33B: 00              BRK                         
F33C: 00              BRK                         
F33D: 00              BRK                         
F33E: 00              BRK                         
F33F: 00              BRK                         
F340: 00              BRK                         
F341: 00              BRK                         
F342: 00              BRK                         
F343: 00              BRK                         
F344: 00              BRK                         
F345: 00              BRK                         
F346: 00              BRK                         
F347: 00              BRK                         
F348: 00              BRK                         
F349: 00              BRK                         
F34A: 00              BRK                         
F34B: 00              BRK                         
F34C: 00              BRK                         
F34D: 00              BRK                         
F34E: 00              BRK                         
F34F: 00              BRK                         
F350: 00              BRK                         
F351: 00              BRK                         
F352: 00              BRK                         
F353: 00              BRK                         
F354: 00              BRK                         
F355: 00              BRK                         
F356: 00              BRK                         
F357: 00              BRK                         
F358: 00              BRK                         
F359: 00              BRK                         
F35A: 00              BRK                         
F35B: 00              BRK                         
F35C: 00              BRK                         
F35D: 00              BRK                         
F35E: 00              BRK                         
F35F: 00              BRK                         
F360: 00              BRK                         
F361: 00              BRK                         
F362: 00              BRK                         
F363: 00              BRK                         
F364: 00              BRK                         
F365: 00              BRK                         
F366: 00              BRK                         
F367: 00              BRK                         
F368: 00              BRK                         
F369: 00              BRK                         
F36A: 00              BRK                         
F36B: 00              BRK                         
F36C: 00              BRK                         
F36D: 00              BRK                         
F36E: 00              BRK                         
F36F: 00              BRK                         
F370: 00              BRK                         
F371: 00              BRK                         
F372: 00              BRK                         
F373: 00              BRK                         
F374: 00              BRK                         
F375: 00              BRK                         
F376: 00              BRK                         
F377: 00              BRK                         
F378: 00              BRK                         
F379: 00              BRK                         
F37A: 00              BRK                         
F37B: 00              BRK                         
F37C: 00              BRK                         
F37D: 00              BRK                         
F37E: 00              BRK                         
F37F: 00              BRK                         
F380: 00              BRK                         
F381: 00              BRK                         
F382: 00              BRK                         
F383: 00              BRK                         
F384: 00              BRK                         
F385: 00              BRK                         
F386: 00              BRK                         
F387: 00              BRK                         
F388: 00              BRK                         
F389: 00              BRK                         
F38A: 00              BRK                         
F38B: 00              BRK                         
F38C: 00              BRK                         
F38D: 00              BRK                         
F38E: 00              BRK                         
F38F: 00              BRK                         
F390: 00              BRK                         
F391: 00              BRK                         
F392: 00              BRK                         
F393: 00              BRK                         
F394: 00              BRK                         
F395: 00              BRK                         
F396: 00              BRK                         
F397: 00              BRK                         
F398: 00              BRK                         
F399: 00              BRK                         
F39A: 00              BRK                         
F39B: 00              BRK                         
F39C: 00              BRK                         
F39D: 00              BRK                         
F39E: 00              BRK                         
F39F: 00              BRK                         
F3A0: 00              BRK                         
F3A1: 00              BRK                         
F3A2: 00              BRK                         
F3A3: 00              BRK                         
F3A4: 00              BRK                         
F3A5: 00              BRK                         
F3A6: 00              BRK                         
F3A7: 00              BRK                         
F3A8: 01 00           ORA     ($00,X)             ; {ram.GP_00}
F3AA: 00              BRK                         
F3AB: 00              BRK                         
F3AC: 00              BRK                         
F3AD: 00              BRK                         
F3AE: 00              BRK                         
F3AF: 00              BRK                         
F3B0: 00              BRK                         
F3B1: 00              BRK                         
F3B2: 00              BRK                         
F3B3: 00              BRK                         
F3B4: 00              BRK                         
F3B5: 00              BRK                         
F3B6: 00              BRK                         
F3B7: 00              BRK                         
F3B8: 00              BRK                         
F3B9: 00              BRK                         
F3BA: 00              BRK                         
F3BB: 00              BRK                         
F3BC: 00              BRK                         
F3BD: 00              BRK                         
F3BE: 00              BRK                         
F3BF: 00              BRK                         
F3C0: 00              BRK                         
F3C1: 00              BRK                         
F3C2: 00              BRK                         
F3C3: 00              BRK                         
F3C4: 00              BRK                         
F3C5: 00              BRK                         
F3C6: 00              BRK                         
F3C7: 00              BRK                         
F3C8: 00              BRK                         
F3C9: 00              BRK                         
F3CA: 00              BRK                         
F3CB: 00              BRK                         
F3CC: 00              BRK                         
F3CD: 00              BRK                         
F3CE: 00              BRK                         
F3CF: 00              BRK                         
F3D0: 00              BRK                         
F3D1: 00              BRK                         
F3D2: 00              BRK                         
F3D3: 00              BRK                         
F3D4: 00              BRK                         
F3D5: 00              BRK                         
F3D6: 00              BRK                         
F3D7: 00              BRK                         
F3D8: 00              BRK                         
F3D9: 00              BRK                         
F3DA: 00              BRK                         
F3DB: 00              BRK                         
F3DC: 00              BRK                         
F3DD: 00              BRK                         
F3DE: 00              BRK                         
F3DF: 00              BRK                         
F3E0: 00              BRK                         
F3E1: 00              BRK                         
F3E2: 00              BRK                         
F3E3: 00              BRK                         
F3E4: 00              BRK                         
F3E5: 00              BRK                         
F3E6: 00              BRK                         
F3E7: 00              BRK                         
F3E8: 00              BRK                         
F3E9: 00              BRK                         
F3EA: 00              BRK                         
F3EB: 00              BRK                         
F3EC: 00              BRK                         
F3ED: 00              BRK                         
F3EE: 00              BRK                         
F3EF: 00              BRK                         
F3F0: 00              BRK                         
F3F1: 00              BRK                         
F3F2: 00              BRK                         
F3F3: 00              BRK                         
F3F4: 00              BRK                         
F3F5: 00              BRK                         
F3F6: 00              BRK                         
F3F7: 00              BRK                         
F3F8: 00              BRK                         
F3F9: 00              BRK                         
F3FA: 00              BRK                         
F3FB: 00              BRK                         
F3FC: 00              BRK                         
F3FD: 00              BRK                         
F3FE: 00              BRK                         
F3FF: 00              BRK                         
F400: FF ; ????
F401: FF ; ????
F402: FF ; ????
F403: FF ; ????
F404: FF ; ????
F405: FF ; ????
F406: FF ; ????
F407: FF ; ????
F408: FF ; ????
F409: FF ; ????
F40A: FF ; ????
F40B: FF ; ????
F40C: FF ; ????
F40D: EE FF FF        INC     $FFFF               ; 
F410: FF ; ????
F411: FF ; ????
F412: FF ; ????
F413: FF ; ????
F414: FF ; ????
F415: FF ; ????
F416: FF ; ????
F417: FF ; ????
F418: FF ; ????
F419: FF ; ????
F41A: EC F7 FF        CPX     $FFF7               ; {}
F41D: AA              TAX                         
F41E: FF ; ????
F41F: FF ; ????
F420: FF ; ????
F421: FF ; ????
F422: FF ; ????
F423: FF ; ????
F424: FB ; ????
F425: F7 ; ????
F426: FF ; ????
F427: FF ; ????
F428: FF ; ????
F429: FF ; ????
F42A: FF ; ????
F42B: FF ; ????
F42C: FF ; ????
F42D: F6 FF           INC     $FF,X               
F42F: FF ; ????
F430: FF ; ????
F431: FF ; ????
F432: FF ; ????
F433: FF ; ????
F434: FF ; ????
F435: FD FF FF        SBC     $FFFF,X             ; 
F438: FE 2F 31        INC     $312F,X             
F43B: 4D FF AE        EOR     $AEFF               
F43E: FF ; ????
F43F: FF ; ????
F440: FF ; ????
F441: FF ; ????
F442: FF ; ????
F443: FF ; ????
F444: FF ; ????
F445: 7F ; ????
F446: FF ; ????
F447: FF ; ????
F448: FF ; ????
F449: FF ; ????
F44A: FF ; ????
F44B: FF ; ????
F44C: FF ; ????
F44D: FF ; ????
F44E: FF ; ????
F44F: FF ; ????
F450: FF ; ????
F451: FF ; ????
F452: FF ; ????
F453: FF ; ????
F454: FF ; ????
F455: FF ; ????
F456: FF ; ????
F457: FF ; ????
F458: 7F ; ????
F459: F4 ; ????
F45A: ED DF FF        SBC     $FFDF               ; {}
F45D: BB ; ????
F45E: FF ; ????
F45F: FF ; ????
F460: FF ; ????
F461: FF ; ????
F462: FF ; ????
F463: FB ; ????
F464: FF ; ????
F465: FF ; ????
F466: FF ; ????
F467: FB ; ????
F468: FF ; ????
F469: FF ; ????
F46A: FF ; ????
F46B: F7 ; ????
F46C: FF ; ????
F46D: FE FF FF        INC     $FFFF,X             ; 
F470: FF ; ????
F471: FF ; ????
F472: EF ; ????
F473: FF ; ????
F474: FF ; ????
F475: FE FF FF        INC     $FFFF,X             ; 
F478: 9B ; ????
F479: 3D E1 50        AND     $50E1,X             
F47C: FF ; ????
F47D: AA              TAX                         
F47E: FF ; ????
F47F: FF ; ????
F480: FF ; ????
F481: FF ; ????
F482: FF ; ????
F483: FF ; ????
F484: FF ; ????
F485: FF ; ????
F486: FF ; ????
F487: FF ; ????
F488: FF ; ????
F489: FF ; ????
F48A: FF ; ????
F48B: FF ; ????
F48C: FF ; ????
F48D: FE FF FF        INC     $FFFF,X             ; 
F490: FF ; ????
F491: FF ; ????
F492: FF ; ????
F493: FF ; ????
F494: FF ; ????
F495: EF ; ????
F496: FF ; ????
F497: FF ; ????
F498: FF ; ????
F499: F9 EE F4        SBC     $F4EE,Y             ; {}
F49C: FF ; ????
F49D: FA ; ????
F49E: FF ; ????
F49F: FF ; ????
F4A0: FF ; ????
F4A1: FF ; ????
F4A2: FF ; ????
F4A3: FF ; ????
F4A4: DF ; ????
F4A5: FF ; ????
F4A6: BF ; ????
F4A7: FF ; ????
F4A8: FF ; ????
F4A9: FF ; ????
F4AA: FE DD FF        INC     $FFDD,X             ; {}
F4AD: FE FF FF        INC     $FFFF,X             ; 
F4B0: FF ; ????
F4B1: FF ; ????
F4B2: FF ; ????
F4B3: FF ; ????
F4B4: FF ; ????
F4B5: FF ; ????
F4B6: FF ; ????
F4B7: FF ; ????
F4B8: BF ; ????
F4B9: EC 70 E9        CPX     $E970               ; {}
F4BC: FF ; ????
F4BD: AA              TAX                         
F4BE: FF ; ????
F4BF: FF ; ????
F4C0: FF ; ????
F4C1: FF ; ????
F4C2: FF ; ????
F4C3: FF ; ????
F4C4: FF ; ????
F4C5: FF ; ????
F4C6: FF ; ????
F4C7: FF ; ????
F4C8: FF ; ????
F4C9: EF ; ????
F4CA: EF ; ????
F4CB: FF ; ????
F4CC: FF ; ????
F4CD: FA ; ????
F4CE: FF ; ????
F4CF: FF ; ????
F4D0: FF ; ????
F4D1: FF ; ????
F4D2: FF ; ????
F4D3: FF ; ????
F4D4: FF ; ????
F4D5: FF ; ????
F4D6: FF ; ????
F4D7: FF ; ????
F4D8: AB ; ????
F4D9: F5 ED           SBC     $ED,X               
F4DB: FD FF AA        SBC     $AAFF,X             
F4DE: FF ; ????
F4DF: FF ; ????
F4E0: FF ; ????
F4E1: 7F ; ????
F4E2: FF ; ????
F4E3: FF ; ????
F4E4: FF ; ????
F4E5: FF ; ????
F4E6: FF ; ????
F4E7: FF ; ????
F4E8: 7F ; ????
F4E9: FD FF FF        SBC     $FFFF,X             ; 
F4EC: FF ; ????
F4ED: FA ; ????
F4EE: FF ; ????
F4EF: FF ; ????
F4F0: FF ; ????
F4F1: FF ; ????
F4F2: FF ; ????
F4F3: FF ; ????
F4F4: FF ; ????
F4F5: FE FF FF        INC     $FFFF,X             ; 
F4F8: EE 5A DA        INC     $DA5A               ; {}
F4FB: C0 FF           CPY     #$FF                
F4FD: AA              TAX                         
F4FE: FF ; ????
F4FF: FF ; ????
F500: 00              BRK                         
F501: 00              BRK                         
F502: 00              BRK                         
F503: 00              BRK                         
F504: 00              BRK                         
F505: 00              BRK                         
F506: 00              BRK                         
F507: 00              BRK                         
F508: 00              BRK                         
F509: 00              BRK                         
F50A: 00              BRK                         
F50B: 00              BRK                         
F50C: 00              BRK                         
F50D: 00              BRK                         
F50E: 01 00           ORA     ($00,X)             ; {ram.GP_00}
F510: 00              BRK                         
F511: 00              BRK                         
F512: 00              BRK                         
F513: 00              BRK                         
F514: 00              BRK                         
F515: 00              BRK                         
F516: 00              BRK                         
F517: 00              BRK                         
F518: 00              BRK                         
F519: 00              BRK                         
F51A: 00              BRK                         
F51B: 00              BRK                         
F51C: 00              BRK                         
F51D: 00              BRK                         
F51E: 00              BRK                         
F51F: 00              BRK                         
F520: 00              BRK                         
F521: 00              BRK                         
F522: 00              BRK                         
F523: 00              BRK                         
F524: 00              BRK                         
F525: 00              BRK                         
F526: 00              BRK                         
F527: 00              BRK                         
F528: 00              BRK                         
F529: 00              BRK                         
F52A: 00              BRK                         
F52B: 00              BRK                         
F52C: 00              BRK                         
F52D: 00              BRK                         
F52E: 00              BRK                         
F52F: 00              BRK                         
F530: 00              BRK                         
F531: 00              BRK                         
F532: 00              BRK                         
F533: 00              BRK                         
F534: 00              BRK                         
F535: 00              BRK                         
F536: 00              BRK                         
F537: 00              BRK                         
F538: 00              BRK                         
F539: 00              BRK                         
F53A: 00              BRK                         
F53B: 00              BRK                         
F53C: 00              BRK                         
F53D: 00              BRK                         
F53E: 00              BRK                         
F53F: 00              BRK                         
F540: 00              BRK                         
F541: 00              BRK                         
F542: 00              BRK                         
F543: 00              BRK                         
F544: 00              BRK                         
F545: 00              BRK                         
F546: 00              BRK                         
F547: 00              BRK                         
F548: 00              BRK                         
F549: 00              BRK                         
F54A: 00              BRK                         
F54B: 00              BRK                         
F54C: 00              BRK                         
F54D: 00              BRK                         
F54E: 00              BRK                         
F54F: 00              BRK                         
F550: 00              BRK                         
F551: 00              BRK                         
F552: 00              BRK                         
F553: 00              BRK                         
F554: 00              BRK                         
F555: 00              BRK                         
F556: 00              BRK                         
F557: 00              BRK                         
F558: 00              BRK                         
F559: 00              BRK                         
F55A: 00              BRK                         
F55B: 00              BRK                         
F55C: 00              BRK                         
F55D: 00              BRK                         
F55E: 00              BRK                         
F55F: 00              BRK                         
F560: 00              BRK                         
F561: 00              BRK                         
F562: 00              BRK                         
F563: 00              BRK                         
F564: 00              BRK                         
F565: 00              BRK                         
F566: 00              BRK                         
F567: 00              BRK                         
F568: 00              BRK                         
F569: 00              BRK                         
F56A: 00              BRK                         
F56B: 00              BRK                         
F56C: 00              BRK                         
F56D: 00              BRK                         
F56E: 00              BRK                         
F56F: 00              BRK                         
F570: 00              BRK                         
F571: 00              BRK                         
F572: 00              BRK                         
F573: 00              BRK                         
F574: 00              BRK                         
F575: 00              BRK                         
F576: 00              BRK                         
F577: 00              BRK                         
F578: 00              BRK                         
F579: 00              BRK                         
F57A: 00              BRK                         
F57B: 00              BRK                         
F57C: 00              BRK                         
F57D: 00              BRK                         
F57E: 00              BRK                         
F57F: 00              BRK                         
F580: 00              BRK                         
F581: 00              BRK                         
F582: 00              BRK                         
F583: 00              BRK                         
F584: 00              BRK                         
F585: 00              BRK                         
F586: 00              BRK                         
F587: 00              BRK                         
F588: 00              BRK                         
F589: 00              BRK                         
F58A: 00              BRK                         
F58B: 00              BRK                         
F58C: 00              BRK                         
F58D: 00              BRK                         
F58E: 00              BRK                         
F58F: 00              BRK                         
F590: 00              BRK                         
F591: 00              BRK                         
F592: 00              BRK                         
F593: 00              BRK                         
F594: 00              BRK                         
F595: 00              BRK                         
F596: 00              BRK                         
F597: 00              BRK                         
F598: 00              BRK                         
F599: 00              BRK                         
F59A: 00              BRK                         
F59B: 00              BRK                         
F59C: 00              BRK                         
F59D: 00              BRK                         
F59E: 10 00           BPL     $F5A0               ; {}
F5A0: 00              BRK                         
F5A1: 00              BRK                         
F5A2: 00              BRK                         
F5A3: 00              BRK                         
F5A4: 00              BRK                         
F5A5: 00              BRK                         
F5A6: 00              BRK                         
F5A7: 00              BRK                         
F5A8: 00              BRK                         
F5A9: 00              BRK                         
F5AA: 00              BRK                         
F5AB: 00              BRK                         
F5AC: 00              BRK                         
F5AD: 00              BRK                         
F5AE: 00              BRK                         
F5AF: 00              BRK                         
F5B0: 00              BRK                         
F5B1: 00              BRK                         
F5B2: 00              BRK                         
F5B3: 00              BRK                         
F5B4: 00              BRK                         
F5B5: 00              BRK                         
F5B6: 00              BRK                         
F5B7: 00              BRK                         
F5B8: 00              BRK                         
F5B9: 00              BRK                         
F5BA: 00              BRK                         
F5BB: 00              BRK                         
F5BC: 00              BRK                         
F5BD: 00              BRK                         
F5BE: 01 00           ORA     ($00,X)             ; {ram.GP_00}
F5C0: 00              BRK                         
F5C1: 00              BRK                         
F5C2: 00              BRK                         
F5C3: 00              BRK                         
F5C4: 00              BRK                         
F5C5: 00              BRK                         
F5C6: 00              BRK                         
F5C7: 00              BRK                         
F5C8: 00              BRK                         
F5C9: 00              BRK                         
F5CA: 00              BRK                         
F5CB: 00              BRK                         
F5CC: 00              BRK                         
F5CD: 00              BRK                         
F5CE: 00              BRK                         
F5CF: 00              BRK                         
F5D0: 00              BRK                         
F5D1: 00              BRK                         
F5D2: 00              BRK                         
F5D3: 00              BRK                         
F5D4: 00              BRK                         
F5D5: 00              BRK                         
F5D6: 00              BRK                         
F5D7: 00              BRK                         
F5D8: 00              BRK                         
F5D9: 00              BRK                         
F5DA: 00              BRK                         
F5DB: 00              BRK                         
F5DC: 00              BRK                         
F5DD: 00              BRK                         
F5DE: 00              BRK                         
F5DF: 00              BRK                         
F5E0: 00              BRK                         
F5E1: 00              BRK                         
F5E2: 00              BRK                         
F5E3: 00              BRK                         
F5E4: 00              BRK                         
F5E5: 00              BRK                         
F5E6: 00              BRK                         
F5E7: 00              BRK                         
F5E8: 00              BRK                         
F5E9: 00              BRK                         
F5EA: 00              BRK                         
F5EB: 00              BRK                         
F5EC: 00              BRK                         
F5ED: 00              BRK                         
F5EE: 00              BRK                         
F5EF: 00              BRK                         
F5F0: 00              BRK                         
F5F1: 00              BRK                         
F5F2: 00              BRK                         
F5F3: 00              BRK                         
F5F4: 00              BRK                         
F5F5: 00              BRK                         
F5F6: 00              BRK                         
F5F7: 00              BRK                         
F5F8: 00              BRK                         
F5F9: 00              BRK                         
F5FA: 00              BRK                         
F5FB: 00              BRK                         
F5FC: 00              BRK                         
F5FD: 00              BRK                         
F5FE: 6F ; ????
F5FF: 2A              ROL     A                   
F600: FF ; ????
F601: FF ; ????
F602: FF ; ????
F603: FF ; ????
F604: FF ; ????
F605: FF ; ????
F606: FF ; ????
F607: FF ; ????
F608: FF ; ????
F609: FF ; ????
F60A: FF ; ????
F60B: FF ; ????
F60C: FF ; ????
F60D: FF ; ????
F60E: FF ; ????
F60F: FF ; ????
F610: FF ; ????
F611: FF ; ????
F612: FF ; ????
F613: FF ; ????
F614: FF ; ????
F615: FF ; ????
F616: FF ; ????
F617: FF ; ????
F618: FF ; ????
F619: FF ; ????
F61A: FF ; ????
F61B: FF ; ????
F61C: FF ; ????
F61D: FF ; ????
F61E: FF ; ????
F61F: FF ; ????
F620: FF ; ????
F621: FF ; ????
F622: FF ; ????
F623: FF ; ????
F624: FF ; ????
F625: FF ; ????
F626: FF ; ????
F627: FF ; ????
F628: FF ; ????
F629: FF ; ????
F62A: F7 ; ????
F62B: FF ; ????
F62C: FF ; ????
F62D: FF ; ????
F62E: FF ; ????
F62F: FF ; ????
F630: FF ; ????
F631: FF ; ????
F632: FF ; ????
F633: FF ; ????
F634: FF ; ????
F635: FF ; ????
F636: FF ; ????
F637: FF ; ????
F638: FF ; ????
F639: FF ; ????
F63A: FF ; ????
F63B: FF ; ????
F63C: FF ; ????
F63D: FF ; ????
F63E: FF ; ????
F63F: FF ; ????
F640: FF ; ????
F641: FF ; ????
F642: FF ; ????
F643: FF ; ????
F644: FF ; ????
F645: FF ; ????
F646: FF ; ????
F647: FF ; ????
F648: FF ; ????
F649: FF ; ????
F64A: FF ; ????
F64B: FF ; ????
F64C: FF ; ????
F64D: FF ; ????
F64E: FF ; ????
F64F: FF ; ????
F650: FF ; ????
F651: FF ; ????
F652: FF ; ????
F653: FF ; ????
F654: FF ; ????
F655: FF ; ????
F656: FF ; ????
F657: FF ; ????
F658: FF ; ????
F659: FF ; ????
F65A: FF ; ????
F65B: FF ; ????
F65C: FF ; ????
F65D: FF ; ????
F65E: FF ; ????
F65F: FF ; ????
F660: FF ; ????
F661: FF ; ????
F662: FF ; ????
F663: FF ; ????
F664: FF ; ????
F665: FF ; ????
F666: FF ; ????
F667: FF ; ????
F668: FF ; ????
F669: FF ; ????
F66A: FF ; ????
F66B: FF ; ????
F66C: FF ; ????
F66D: FF ; ????
F66E: FF ; ????
F66F: FF ; ????
F670: FF ; ????
F671: FF ; ????
F672: FF ; ????
F673: FF ; ????
F674: FF ; ????
F675: FF ; ????
F676: FF ; ????
F677: FF ; ????
F678: FE FF FF        INC     $FFFF,X             ; 
F67B: FF ; ????
F67C: FF ; ????
F67D: FF ; ????
F67E: FF ; ????
F67F: FF ; ????
F680: FF ; ????
F681: FF ; ????
F682: FF ; ????
F683: FF ; ????
F684: FF ; ????
F685: FF ; ????
F686: FF ; ????
F687: FF ; ????
F688: FF ; ????
F689: FF ; ????
F68A: FF ; ????
F68B: FF ; ????
F68C: FF ; ????
F68D: FF ; ????
F68E: FF ; ????
F68F: FF ; ????
F690: FF ; ????
F691: FF ; ????
F692: FF ; ????
F693: FF ; ????
F694: FF ; ????
F695: FF ; ????
F696: FF ; ????
F697: FF ; ????
F698: FF ; ????
F699: FF ; ????
F69A: FF ; ????
F69B: FF ; ????
F69C: FF ; ????
F69D: FF ; ????
F69E: FF ; ????
F69F: FF ; ????
F6A0: FF ; ????
F6A1: FF ; ????
F6A2: FF ; ????
F6A3: FF ; ????
F6A4: FF ; ????
F6A5: FF ; ????
F6A6: FF ; ????
F6A7: FF ; ????
F6A8: FF ; ????
F6A9: FF ; ????
F6AA: FF ; ????
F6AB: FF ; ????
F6AC: FF ; ????
F6AD: FF ; ????
F6AE: FF ; ????
F6AF: FF ; ????
F6B0: FF ; ????
F6B1: FF ; ????
F6B2: FF ; ????
F6B3: FF ; ????
F6B4: F7 ; ????
F6B5: FF ; ????
F6B6: FF ; ????
F6B7: FF ; ????
F6B8: FF ; ????
F6B9: FF ; ????
F6BA: FF ; ????
F6BB: FF ; ????
F6BC: FF ; ????
F6BD: FF ; ????
F6BE: FF ; ????
F6BF: FF ; ????
F6C0: FF ; ????
F6C1: FF ; ????
F6C2: FF ; ????
F6C3: FF ; ????
F6C4: FF ; ????
F6C5: FF ; ????
F6C6: FF ; ????
F6C7: FF ; ????
F6C8: FF ; ????
F6C9: FF ; ????
F6CA: FF ; ????
F6CB: FF ; ????
F6CC: FF ; ????
F6CD: FF ; ????
F6CE: FF ; ????
F6CF: FF ; ????
F6D0: FF ; ????
F6D1: FF ; ????
F6D2: FF ; ????
F6D3: FF ; ????
F6D4: FF ; ????
F6D5: FF ; ????
F6D6: FF ; ????
F6D7: FF ; ????
F6D8: FF ; ????
F6D9: FF ; ????
F6DA: FF ; ????
F6DB: FF ; ????
F6DC: FF ; ????
F6DD: FF ; ????
F6DE: FF ; ????
F6DF: FF ; ????
F6E0: FF ; ????
F6E1: FF ; ????
F6E2: FF ; ????
F6E3: FF ; ????
F6E4: FF ; ????
F6E5: FF ; ????
F6E6: FF ; ????
F6E7: FF ; ????
F6E8: FF ; ????
F6E9: FF ; ????
F6EA: FF ; ????
F6EB: FF ; ????
F6EC: FF ; ????
F6ED: FF ; ????
F6EE: FF ; ????
F6EF: FF ; ????
F6F0: FF ; ????
F6F1: FF ; ????
F6F2: FF ; ????
F6F3: FF ; ????
F6F4: FF ; ????
F6F5: FF ; ????
F6F6: FF ; ????
F6F7: FF ; ????
F6F8: FF ; ????
F6F9: FF ; ????
F6FA: FF ; ????
F6FB: FF ; ????
F6FC: FF ; ????
F6FD: BF ; ????
F6FE: FF ; ????
F6FF: FF ; ????
F700: 00              BRK                         
F701: 00              BRK                         
F702: 00              BRK                         
F703: 00              BRK                         
F704: 00              BRK                         
F705: 00              BRK                         
F706: 00              BRK                         
F707: 00              BRK                         
F708: 00              BRK                         
F709: 00              BRK                         
F70A: 00              BRK                         
F70B: 00              BRK                         
F70C: 00              BRK                         
F70D: 00              BRK                         
F70E: 00              BRK                         
F70F: 00              BRK                         
F710: 00              BRK                         
F711: 00              BRK                         
F712: 00              BRK                         
F713: 00              BRK                         
F714: 00              BRK                         
F715: 00              BRK                         
F716: 00              BRK                         
F717: 00              BRK                         
F718: 00              BRK                         
F719: 00              BRK                         
F71A: 00              BRK                         
F71B: 00              BRK                         
F71C: 00              BRK                         
F71D: 00              BRK                         
F71E: 00              BRK                         
F71F: 00              BRK                         
F720: 00              BRK                         
F721: 00              BRK                         
F722: 00              BRK                         
F723: 00              BRK                         
F724: 00              BRK                         
F725: 00              BRK                         
F726: 00              BRK                         
F727: 00              BRK                         
F728: 00              BRK                         
F729: 00              BRK                         
F72A: 00              BRK                         
F72B: 00              BRK                         
F72C: 00              BRK                         
F72D: 00              BRK                         
F72E: 00              BRK                         
F72F: 00              BRK                         
F730: 00              BRK                         
F731: 00              BRK                         
F732: 00              BRK                         
F733: 00              BRK                         
F734: 00              BRK                         
F735: 00              BRK                         
F736: 00              BRK                         
F737: 00              BRK                         
F738: 00              BRK                         
F739: 00              BRK                         
F73A: 00              BRK                         
F73B: 00              BRK                         
F73C: 00              BRK                         
F73D: 00              BRK                         
F73E: 00              BRK                         
F73F: 00              BRK                         
F740: 00              BRK                         
F741: 00              BRK                         
F742: 00              BRK                         
F743: 00              BRK                         
F744: 00              BRK                         
F745: 00              BRK                         
F746: 00              BRK                         
F747: 00              BRK                         
F748: 00              BRK                         
F749: 00              BRK                         
F74A: 00              BRK                         
F74B: 00              BRK                         
F74C: 00              BRK                         
F74D: 00              BRK                         
F74E: 00              BRK                         
F74F: 00              BRK                         
F750: 00              BRK                         
F751: 00              BRK                         
F752: 00              BRK                         
F753: 00              BRK                         
F754: 00              BRK                         
F755: 00              BRK                         
F756: 00              BRK                         
F757: 00              BRK                         
F758: 00              BRK                         
F759: 00              BRK                         
F75A: 00              BRK                         
F75B: 00              BRK                         
F75C: 00              BRK                         
F75D: 00              BRK                         
F75E: 00              BRK                         
F75F: 00              BRK                         
F760: 00              BRK                         
F761: 00              BRK                         
F762: 00              BRK                         
F763: 00              BRK                         
F764: 00              BRK                         
F765: 00              BRK                         
F766: 00              BRK                         
F767: 00              BRK                         
F768: 00              BRK                         
F769: 00              BRK                         
F76A: 00              BRK                         
F76B: 00              BRK                         
F76C: 00              BRK                         
F76D: 00              BRK                         
F76E: 00              BRK                         
F76F: 00              BRK                         
F770: 00              BRK                         
F771: 00              BRK                         
F772: 00              BRK                         
F773: 00              BRK                         
F774: 00              BRK                         
F775: 00              BRK                         
F776: 00              BRK                         
F777: 00              BRK                         
F778: 00              BRK                         
F779: 00              BRK                         
F77A: 00              BRK                         
F77B: 00              BRK                         
F77C: 00              BRK                         
F77D: 00              BRK                         
F77E: 00              BRK                         
F77F: 00              BRK                         
F780: 00              BRK                         
F781: 00              BRK                         
F782: 00              BRK                         
F783: 00              BRK                         
F784: 00              BRK                         
F785: 00              BRK                         
F786: 00              BRK                         
F787: 00              BRK                         
F788: 00              BRK                         
F789: 00              BRK                         
F78A: 00              BRK                         
F78B: 00              BRK                         
F78C: 00              BRK                         
F78D: 00              BRK                         
F78E: 00              BRK                         
F78F: 00              BRK                         
F790: 00              BRK                         
F791: 00              BRK                         
F792: 00              BRK                         
F793: 00              BRK                         
F794: 00              BRK                         
F795: 00              BRK                         
F796: 00              BRK                         
F797: 00              BRK                         
F798: 00              BRK                         
F799: 00              BRK                         
F79A: 00              BRK                         
F79B: 00              BRK                         
F79C: 00              BRK                         
F79D: 00              BRK                         
F79E: 00              BRK                         
F79F: 00              BRK                         
F7A0: 00              BRK                         
F7A1: 00              BRK                         
F7A2: 00              BRK                         
F7A3: 00              BRK                         
F7A4: 00              BRK                         
F7A5: 00              BRK                         
F7A6: 00              BRK                         
F7A7: 00              BRK                         
F7A8: 00              BRK                         
F7A9: 00              BRK                         
F7AA: 00              BRK                         
F7AB: 00              BRK                         
F7AC: 00              BRK                         
F7AD: 00              BRK                         
F7AE: 00              BRK                         
F7AF: 00              BRK                         
F7B0: 00              BRK                         
F7B1: 00              BRK                         
F7B2: 00              BRK                         
F7B3: 00              BRK                         
F7B4: 00              BRK                         
F7B5: 00              BRK                         
F7B6: 00              BRK                         
F7B7: 00              BRK                         
F7B8: 00              BRK                         
F7B9: 00              BRK                         
F7BA: 00              BRK                         
F7BB: 00              BRK                         
F7BC: 00              BRK                         
F7BD: 00              BRK                         
F7BE: 00              BRK                         
F7BF: 00              BRK                         
F7C0: 00              BRK                         
F7C1: 00              BRK                         
F7C2: 00              BRK                         
F7C3: 00              BRK                         
F7C4: 00              BRK                         
F7C5: 00              BRK                         
F7C6: 00              BRK                         
F7C7: 00              BRK                         
F7C8: 00              BRK                         
F7C9: 00              BRK                         
F7CA: 00              BRK                         
F7CB: 00              BRK                         
F7CC: 00              BRK                         
F7CD: 00              BRK                         
F7CE: 00              BRK                         
F7CF: 00              BRK                         
F7D0: 00              BRK                         
F7D1: 00              BRK                         
F7D2: 00              BRK                         
F7D3: 00              BRK                         
F7D4: 00              BRK                         
F7D5: 00              BRK                         
F7D6: 00              BRK                         
F7D7: 00              BRK                         
F7D8: 00              BRK                         
F7D9: 00              BRK                         
F7DA: 00              BRK                         
F7DB: 00              BRK                         
F7DC: 00              BRK                         
F7DD: 00              BRK                         
F7DE: 00              BRK                         
F7DF: 00              BRK                         
F7E0: 00              BRK                         
F7E1: 00              BRK                         
F7E2: 00              BRK                         
F7E3: 00              BRK                         
F7E4: 00              BRK                         
F7E5: 00              BRK                         
F7E6: 00              BRK                         
F7E7: 00              BRK                         
F7E8: 00              BRK                         
F7E9: 00              BRK                         
F7EA: 00              BRK                         
F7EB: 00              BRK                         
F7EC: 00              BRK                         
F7ED: 00              BRK                         
F7EE: 00              BRK                         
F7EF: 00              BRK                         
F7F0: 00              BRK                         
F7F1: 00              BRK                         
F7F2: 00              BRK                         
F7F3: 00              BRK                         
F7F4: 00              BRK                         
F7F5: 00              BRK                         
F7F6: 00              BRK                         
F7F7: 00              BRK                         
F7F8: 00              BRK                         
F7F9: 00              BRK                         
F7FA: 00              BRK                         
F7FB: 00              BRK                         
F7FC: 00              BRK                         
F7FD: 00              BRK                         
F7FE: 00              BRK                         
F7FF: 00              BRK                         
F800: FF ; ????
F801: FF ; ????
F802: FF ; ????
F803: FF ; ????
F804: FF ; ????
F805: FF ; ????
F806: FF ; ????
F807: FF ; ????
F808: FF ; ????
F809: FF ; ????
F80A: FF ; ????
F80B: FF ; ????
F80C: FF ; ????
F80D: FF ; ????
F80E: FF ; ????
F80F: FF ; ????
F810: FF ; ????
F811: FF ; ????
F812: FF ; ????
F813: FF ; ????
F814: FF ; ????
F815: FF ; ????
F816: FF ; ????
F817: FF ; ????
F818: FF ; ????
F819: FF ; ????
F81A: FF ; ????
F81B: FF ; ????
F81C: FF ; ????
F81D: FF ; ????
F81E: FF ; ????
F81F: FF ; ????
F820: FF ; ????
F821: FF ; ????
F822: FF ; ????
F823: FF ; ????
F824: FF ; ????
F825: EF ; ????
F826: FF ; ????
F827: FF ; ????
F828: FF ; ????
F829: FF ; ????
F82A: FF ; ????
F82B: FF ; ????
F82C: FF ; ????
F82D: FF ; ????
F82E: FF ; ????
F82F: FF ; ????
F830: FF ; ????
F831: FF ; ????
F832: FF ; ????
F833: FF ; ????
F834: FF ; ????
F835: FF ; ????
F836: FF ; ????
F837: FF ; ????
F838: FF ; ????
F839: F9 FD FF        SBC     $FFFD,Y             ; {}
F83C: FF ; ????
F83D: FF ; ????
F83E: FF ; ????
F83F: FF ; ????
F840: FE FF FF        INC     $FFFF,X             ; 
F843: FF ; ????
F844: FF ; ????
F845: FF ; ????
F846: FF ; ????
F847: FF ; ????
F848: FF ; ????
F849: FF ; ????
F84A: FF ; ????
F84B: FF ; ????
F84C: FF ; ????
F84D: FF ; ????
F84E: FF ; ????
F84F: FF ; ????
F850: FF ; ????
F851: FF ; ????
F852: FF ; ????
F853: FF ; ????
F854: FF ; ????
F855: FF ; ????
F856: FF ; ????
F857: FF ; ????
F858: FF ; ????
F859: FF ; ????
F85A: FF ; ????
F85B: FF ; ????
F85C: FF ; ????
F85D: FF ; ????
F85E: FF ; ????
F85F: FF ; ????
F860: FF ; ????
F861: FF ; ????
F862: FF ; ????
F863: FF ; ????
F864: FF ; ????
F865: FF ; ????
F866: FF ; ????
F867: FF ; ????
F868: FF ; ????
F869: FF ; ????
F86A: FF ; ????
F86B: FF ; ????
F86C: FF ; ????
F86D: FF ; ????
F86E: FF ; ????
F86F: FF ; ????
F870: FF ; ????
F871: FF ; ????
F872: FF ; ????
F873: FF ; ????
F874: FF ; ????
F875: FF ; ????
F876: FF ; ????
F877: FF ; ????
F878: FF ; ????
F879: FB ; ????
F87A: FC ; ????
F87B: FD FF FF        SBC     $FFFF,X             ; 
F87E: FF ; ????
F87F: FF ; ????
F880: FF ; ????
F881: FF ; ????
F882: FF ; ????
F883: FF ; ????
F884: FF ; ????
F885: FF ; ????
F886: FF ; ????
F887: FF ; ????
F888: FF ; ????
F889: FF ; ????
F88A: FF ; ????
F88B: FF ; ????
F88C: FF ; ????
F88D: FF ; ????
F88E: FF ; ????
F88F: FF ; ????
F890: FF ; ????
F891: FF ; ????
F892: FF ; ????
F893: FF ; ????
F894: FF ; ????
F895: FF ; ????
F896: FF ; ????
F897: FF ; ????
F898: FF ; ????
F899: FF ; ????
F89A: FF ; ????
F89B: FE FF FF        INC     $FFFF,X             ; 
F89E: FF ; ????
F89F: FF ; ????
F8A0: FF ; ????
F8A1: FF ; ????
F8A2: FF ; ????
F8A3: FF ; ????
F8A4: FF ; ????
F8A5: 7F ; ????
F8A6: FF ; ????
F8A7: FF ; ????
F8A8: FF ; ????
F8A9: FF ; ????
F8AA: FF ; ????
F8AB: FF ; ????
F8AC: FF ; ????
F8AD: FF ; ????
F8AE: FF ; ????
F8AF: FF ; ????
F8B0: FF ; ????
F8B1: FF ; ????
F8B2: FF ; ????
F8B3: FF ; ????
F8B4: FF ; ????
F8B5: FF ; ????
F8B6: FF ; ????
F8B7: FF ; ????
F8B8: FF ; ????
F8B9: FF ; ????
F8BA: FB ; ????
F8BB: FF ; ????
F8BC: FF ; ????
F8BD: FF ; ????
F8BE: FF ; ????
F8BF: FF ; ????
F8C0: FF ; ????
F8C1: FF ; ????
F8C2: FF ; ????
F8C3: FF ; ????
F8C4: FF ; ????
F8C5: FF ; ????
F8C6: FF ; ????
F8C7: FF ; ????
F8C8: FF ; ????
F8C9: FF ; ????
F8CA: FF ; ????
F8CB: FF ; ????
F8CC: FF ; ????
F8CD: FF ; ????
F8CE: FF ; ????
F8CF: FF ; ????
F8D0: FF ; ????
F8D1: FF ; ????
F8D2: FF ; ????
F8D3: FF ; ????
F8D4: FF ; ????
F8D5: FF ; ????
F8D6: FF ; ????
F8D7: FF ; ????
F8D8: FF ; ????
F8D9: FF ; ????
F8DA: F7 ; ????
F8DB: FF ; ????
F8DC: FF ; ????
F8DD: FF ; ????
F8DE: FF ; ????
F8DF: FF ; ????
F8E0: FF ; ????
F8E1: FF ; ????
F8E2: FF ; ????
F8E3: FF ; ????
F8E4: FF ; ????
F8E5: FF ; ????
F8E6: FF ; ????
F8E7: FF ; ????
F8E8: FF ; ????
F8E9: FF ; ????
F8EA: FF ; ????
F8EB: FF ; ????
F8EC: FF ; ????
F8ED: FF ; ????
F8EE: FF ; ????
F8EF: FF ; ????
F8F0: FF ; ????
F8F1: FF ; ????
F8F2: FF ; ????
F8F3: FF ; ????
F8F4: FF ; ????
F8F5: FF ; ????
F8F6: FF ; ????
F8F7: FF ; ????
F8F8: FF ; ????
F8F9: FE FE FF        INC     $FFFE,X             ; {}
F8FC: DF ; ????
F8FD: FF ; ????
F8FE: FF ; ????
F8FF: FF ; ????
F900: 00              BRK                         
F901: 00              BRK                         
F902: 00              BRK                         
F903: 00              BRK                         
F904: 00              BRK                         
F905: 00              BRK                         
F906: 00              BRK                         
F907: 00              BRK                         
F908: 00              BRK                         
F909: 00              BRK                         
F90A: 00              BRK                         
F90B: 00              BRK                         
F90C: 00              BRK                         
F90D: 00              BRK                         
F90E: 00              BRK                         
F90F: 00              BRK                         
F910: 00              BRK                         
F911: 00              BRK                         
F912: 00              BRK                         
F913: 00              BRK                         
F914: 00              BRK                         
F915: 00              BRK                         
F916: 00              BRK                         
F917: 00              BRK                         
F918: 00              BRK                         
F919: 00              BRK                         
F91A: 00              BRK                         
F91B: 00              BRK                         
F91C: 00              BRK                         
F91D: 00              BRK                         
F91E: 00              BRK                         
F91F: 00              BRK                         
F920: 00              BRK                         
F921: 00              BRK                         
F922: 00              BRK                         
F923: 00              BRK                         
F924: 00              BRK                         
F925: 00              BRK                         
F926: 00              BRK                         
F927: 00              BRK                         
F928: 00              BRK                         
F929: 00              BRK                         
F92A: 00              BRK                         
F92B: 00              BRK                         
F92C: 00              BRK                         
F92D: 00              BRK                         
F92E: 00              BRK                         
F92F: 00              BRK                         
F930: 00              BRK                         
F931: 00              BRK                         
F932: 00              BRK                         
F933: 00              BRK                         
F934: 00              BRK                         
F935: 00              BRK                         
F936: 00              BRK                         
F937: 00              BRK                         
F938: 00              BRK                         
F939: 00              BRK                         
F93A: 00              BRK                         
F93B: 00              BRK                         
F93C: 00              BRK                         
F93D: 00              BRK                         
F93E: 00              BRK                         
F93F: 00              BRK                         
F940: 00              BRK                         
F941: 00              BRK                         
F942: 00              BRK                         
F943: 00              BRK                         
F944: 00              BRK                         
F945: 00              BRK                         
F946: 00              BRK                         
F947: 00              BRK                         
F948: 00              BRK                         
F949: 00              BRK                         
F94A: 00              BRK                         
F94B: 00              BRK                         
F94C: 00              BRK                         
F94D: 00              BRK                         
F94E: 00              BRK                         
F94F: 00              BRK                         
F950: 00              BRK                         
F951: 00              BRK                         
F952: 00              BRK                         
F953: 00              BRK                         
F954: 00              BRK                         
F955: 00              BRK                         
F956: 00              BRK                         
F957: 00              BRK                         
F958: 00              BRK                         
F959: 00              BRK                         
F95A: 00              BRK                         
F95B: 00              BRK                         
F95C: 00              BRK                         
F95D: 00              BRK                         
F95E: 00              BRK                         
F95F: 00              BRK                         
F960: 00              BRK                         
F961: 00              BRK                         
F962: 00              BRK                         
F963: 00              BRK                         
F964: 00              BRK                         
F965: 00              BRK                         
F966: 00              BRK                         
F967: 00              BRK                         
F968: 00              BRK                         
F969: 00              BRK                         
F96A: 00              BRK                         
F96B: 00              BRK                         
F96C: 00              BRK                         
F96D: 00              BRK                         
F96E: 00              BRK                         
F96F: 00              BRK                         
F970: 00              BRK                         
F971: 00              BRK                         
F972: 00              BRK                         
F973: 00              BRK                         
F974: 00              BRK                         
F975: 00              BRK                         
F976: 00              BRK                         
F977: 00              BRK                         
F978: 00              BRK                         
F979: 00              BRK                         
F97A: 00              BRK                         
F97B: 00              BRK                         
F97C: 00              BRK                         
F97D: 00              BRK                         
F97E: 00              BRK                         
F97F: 00              BRK                         
F980: 00              BRK                         
F981: 00              BRK                         
F982: 00              BRK                         
F983: 00              BRK                         
F984: 00              BRK                         
F985: 00              BRK                         
F986: 00              BRK                         
F987: 00              BRK                         
F988: 00              BRK                         
F989: 00              BRK                         
F98A: 00              BRK                         
F98B: 00              BRK                         
F98C: 00              BRK                         
F98D: 00              BRK                         
F98E: 00              BRK                         
F98F: 00              BRK                         
F990: 00              BRK                         
F991: 00              BRK                         
F992: 00              BRK                         
F993: 00              BRK                         
F994: 00              BRK                         
F995: 00              BRK                         
F996: 00              BRK                         
F997: 00              BRK                         
F998: 00              BRK                         
F999: 00              BRK                         
F99A: 00              BRK                         
F99B: 00              BRK                         
F99C: 00              BRK                         
F99D: 00              BRK                         
F99E: 00              BRK                         
F99F: 00              BRK                         
F9A0: 00              BRK                         
F9A1: 00              BRK                         
F9A2: 00              BRK                         
F9A3: 00              BRK                         
F9A4: 00              BRK                         
F9A5: 00              BRK                         
F9A6: 00              BRK                         
F9A7: 00              BRK                         
F9A8: 00              BRK                         
F9A9: 00              BRK                         
F9AA: 00              BRK                         
F9AB: 00              BRK                         
F9AC: 00              BRK                         
F9AD: 00              BRK                         
F9AE: 00              BRK                         
F9AF: 00              BRK                         
F9B0: 00              BRK                         
F9B1: 00              BRK                         
F9B2: 00              BRK                         
F9B3: 00              BRK                         
F9B4: 00              BRK                         
F9B5: 00              BRK                         
F9B6: 00              BRK                         
F9B7: 00              BRK                         
F9B8: 00              BRK                         
F9B9: 00              BRK                         
F9BA: 00              BRK                         
F9BB: 00              BRK                         
F9BC: 00              BRK                         
F9BD: 00              BRK                         
F9BE: 00              BRK                         
F9BF: 00              BRK                         
F9C0: 00              BRK                         
F9C1: 00              BRK                         
F9C2: 00              BRK                         
F9C3: 00              BRK                         
F9C4: 00              BRK                         
F9C5: 00              BRK                         
F9C6: 00              BRK                         
F9C7: 00              BRK                         
F9C8: 00              BRK                         
F9C9: 00              BRK                         
F9CA: 00              BRK                         
F9CB: 00              BRK                         
F9CC: 00              BRK                         
F9CD: 00              BRK                         
F9CE: 00              BRK                         
F9CF: 00              BRK                         
F9D0: 00              BRK                         
F9D1: 00              BRK                         
F9D2: 00              BRK                         
F9D3: 00              BRK                         
F9D4: 00              BRK                         
F9D5: 00              BRK                         
F9D6: 00              BRK                         
F9D7: 00              BRK                         
F9D8: 00              BRK                         
F9D9: 00              BRK                         
F9DA: 00              BRK                         
F9DB: 00              BRK                         
F9DC: 00              BRK                         
F9DD: 00              BRK                         
F9DE: 00              BRK                         
F9DF: 00              BRK                         
F9E0: 00              BRK                         
F9E1: 00              BRK                         
F9E2: 00              BRK                         
F9E3: 00              BRK                         
F9E4: 00              BRK                         
F9E5: 00              BRK                         
F9E6: 00              BRK                         
F9E7: 00              BRK                         
F9E8: 00              BRK                         
F9E9: 00              BRK                         
F9EA: 00              BRK                         
F9EB: 00              BRK                         
F9EC: 00              BRK                         
F9ED: 00              BRK                         
F9EE: 00              BRK                         
F9EF: 00              BRK                         
F9F0: 00              BRK                         
F9F1: 00              BRK                         
F9F2: 00              BRK                         
F9F3: 00              BRK                         
F9F4: 00              BRK                         
F9F5: 00              BRK                         
F9F6: 00              BRK                         
F9F7: 00              BRK                         
F9F8: 00              BRK                         
F9F9: 00              BRK                         
F9FA: 00              BRK                         
F9FB: 00              BRK                         
F9FC: 00              BRK                         
F9FD: 00              BRK                         
F9FE: 05 00           ORA     $00                 ; {ram.GP_00}
FA00: FF ; ????
FA01: FF ; ????
FA02: FF ; ????
FA03: FF ; ????
FA04: FF ; ????
FA05: FF ; ????
FA06: FF ; ????
FA07: FF ; ????
FA08: FF ; ????
FA09: FF ; ????
FA0A: FF ; ????
FA0B: FF ; ????
FA0C: FF ; ????
FA0D: FF ; ????
FA0E: FF ; ????
FA0F: FF ; ????
FA10: FF ; ????
FA11: FF ; ????
FA12: FF ; ????
FA13: FF ; ????
FA14: FF ; ????
FA15: BF ; ????
FA16: FF ; ????
FA17: FF ; ????
FA18: FF ; ????
FA19: FF ; ????
FA1A: FF ; ????
FA1B: FF ; ????
FA1C: FF ; ????
FA1D: FF ; ????
FA1E: FF ; ????
FA1F: FF ; ????
FA20: FF ; ????
FA21: FF ; ????
FA22: FF ; ????
FA23: FF ; ????
FA24: FF ; ????
FA25: FF ; ????
FA26: FF ; ????
FA27: FF ; ????
FA28: FF ; ????
FA29: FF ; ????
FA2A: FF ; ????
FA2B: FF ; ????
FA2C: FF ; ????
FA2D: FF ; ????
FA2E: FF ; ????
FA2F: FF ; ????
FA30: FF ; ????
FA31: FF ; ????
FA32: FF ; ????
FA33: FF ; ????
FA34: FF ; ????
FA35: FF ; ????
FA36: FF ; ????
FA37: FF ; ????
FA38: FF ; ????
FA39: FF ; ????
FA3A: FF ; ????
FA3B: FF ; ????
FA3C: FF ; ????
FA3D: FF ; ????
FA3E: FF ; ????
FA3F: FF ; ????
FA40: FF ; ????
FA41: FF ; ????
FA42: FF ; ????
FA43: FF ; ????
FA44: FF ; ????
FA45: FF ; ????
FA46: FF ; ????
FA47: FF ; ????
FA48: FF ; ????
FA49: FF ; ????
FA4A: FF ; ????
FA4B: FF ; ????
FA4C: FF ; ????
FA4D: FF ; ????
FA4E: FF ; ????
FA4F: FF ; ????
FA50: FF ; ????
FA51: FF ; ????
FA52: FF ; ????
FA53: FF ; ????
FA54: FF ; ????
FA55: FF ; ????
FA56: FF ; ????
FA57: FF ; ????
FA58: FF ; ????
FA59: FF ; ????
FA5A: FF ; ????
FA5B: FF ; ????
FA5C: FF ; ????
FA5D: FF ; ????
FA5E: FF ; ????
FA5F: FF ; ????
FA60: FF ; ????
FA61: FF ; ????
FA62: FF ; ????
FA63: FF ; ????
FA64: FF ; ????
FA65: FF ; ????
FA66: FF ; ????
FA67: FF ; ????
FA68: FF ; ????
FA69: FF ; ????
FA6A: FF ; ????
FA6B: FF ; ????
FA6C: FF ; ????
FA6D: FF ; ????
FA6E: FF ; ????
FA6F: FF ; ????
FA70: FF ; ????
FA71: FF ; ????
FA72: FF ; ????
FA73: FF ; ????
FA74: FF ; ????
FA75: FF ; ????
FA76: FF ; ????
FA77: FF ; ????
FA78: FF ; ????
FA79: FF ; ????
FA7A: FF ; ????
FA7B: FF ; ????
FA7C: FF ; ????
FA7D: FF ; ????
FA7E: FF ; ????
FA7F: FF ; ????
FA80: FF ; ????
FA81: FF ; ????
FA82: FF ; ????
FA83: FF ; ????
FA84: FF ; ????
FA85: FF ; ????
FA86: FF ; ????
FA87: FF ; ????
FA88: FF ; ????
FA89: FF ; ????
FA8A: FF ; ????
FA8B: FF ; ????
FA8C: FF ; ????
FA8D: EF ; ????
FA8E: FF ; ????
FA8F: FF ; ????
FA90: FF ; ????
FA91: FF ; ????
FA92: FF ; ????
FA93: FF ; ????
FA94: FF ; ????
FA95: FF ; ????
FA96: FF ; ????
FA97: FF ; ????
FA98: FF ; ????
FA99: FF ; ????
FA9A: FF ; ????
FA9B: FF ; ????
FA9C: FF ; ????
FA9D: FF ; ????
FA9E: FF ; ????
FA9F: FF ; ????
FAA0: FF ; ????
FAA1: FF ; ????
FAA2: FF ; ????
FAA3: FF ; ????
FAA4: FF ; ????
FAA5: FF ; ????
FAA6: FF ; ????
FAA7: FF ; ????
FAA8: FF ; ????
FAA9: FF ; ????
FAAA: FF ; ????
FAAB: FF ; ????
FAAC: FF ; ????
FAAD: FF ; ????
FAAE: FF ; ????
FAAF: FF ; ????
FAB0: FF ; ????
FAB1: FF ; ????
FAB2: FF ; ????
FAB3: FF ; ????
FAB4: FF ; ????
FAB5: FF ; ????
FAB6: FF ; ????
FAB7: FF ; ????
FAB8: FF ; ????
FAB9: FF ; ????
FABA: FF ; ????
FABB: FF ; ????
FABC: FF ; ????
FABD: FF ; ????
FABE: FF ; ????
FABF: FF ; ????
FAC0: FF ; ????
FAC1: FF ; ????
FAC2: FF ; ????
FAC3: FF ; ????
FAC4: FF ; ????
FAC5: FF ; ????
FAC6: FF ; ????
FAC7: FF ; ????
FAC8: FF ; ????
FAC9: FF ; ????
FACA: FF ; ????
FACB: FF ; ????
FACC: DF ; ????
FACD: FF ; ????
FACE: FF ; ????
FACF: FF ; ????
FAD0: FF ; ????
FAD1: FF ; ????
FAD2: FF ; ????
FAD3: FF ; ????
FAD4: FF ; ????
FAD5: FF ; ????
FAD6: FF ; ????
FAD7: FF ; ????
FAD8: FF ; ????
FAD9: FF ; ????
FADA: FF ; ????
FADB: FF ; ????
FADC: BF ; ????
FADD: F6 FF           INC     $FF,X               
FADF: FF ; ????
FAE0: FF ; ????
FAE1: FF ; ????
FAE2: FF ; ????
FAE3: FF ; ????
FAE4: EF ; ????
FAE5: FF ; ????
FAE6: FF ; ????
FAE7: FF ; ????
FAE8: FF ; ????
FAE9: FF ; ????
FAEA: FF ; ????
FAEB: FF ; ????
FAEC: FF ; ????
FAED: 7F ; ????
FAEE: FF ; ????
FAEF: FF ; ????
FAF0: FF ; ????
FAF1: FF ; ????
FAF2: FF ; ????
FAF3: FF ; ????
FAF4: FF ; ????
FAF5: FF ; ????
FAF6: FF ; ????
FAF7: FF ; ????
FAF8: FF ; ????
FAF9: FF ; ????
FAFA: FF ; ????
FAFB: FF ; ????
FAFC: FF ; ????
FAFD: FF ; ????
FAFE: FF ; ????
FAFF: FF ; ????
FB00: 00              BRK                         
FB01: 00              BRK                         
FB02: 00              BRK                         
FB03: 00              BRK                         
FB04: 00              BRK                         
FB05: 00              BRK                         
FB06: 00              BRK                         
FB07: 00              BRK                         
FB08: 00              BRK                         
FB09: 00              BRK                         
FB0A: 00              BRK                         
FB0B: 00              BRK                         
FB0C: 00              BRK                         
FB0D: 00              BRK                         
FB0E: 00              BRK                         
FB0F: 00              BRK                         
FB10: 00              BRK                         
FB11: 00              BRK                         
FB12: 00              BRK                         
FB13: 00              BRK                         
FB14: 00              BRK                         
FB15: 00              BRK                         
FB16: 00              BRK                         
FB17: 00              BRK                         
FB18: 00              BRK                         
FB19: 00              BRK                         
FB1A: 00              BRK                         
FB1B: 00              BRK                         
FB1C: 00              BRK                         
FB1D: 00              BRK                         
FB1E: 00              BRK                         
FB1F: 00              BRK                         
FB20: 00              BRK                         
FB21: 00              BRK                         
FB22: 00              BRK                         
FB23: 00              BRK                         
FB24: 00              BRK                         
FB25: 00              BRK                         
FB26: 00              BRK                         
FB27: 00              BRK                         
FB28: 00              BRK                         
FB29: 00              BRK                         
FB2A: 00              BRK                         
FB2B: 00              BRK                         
FB2C: 00              BRK                         
FB2D: 00              BRK                         
FB2E: 00              BRK                         
FB2F: 00              BRK                         
FB30: 00              BRK                         
FB31: 00              BRK                         
FB32: 00              BRK                         
FB33: 00              BRK                         
FB34: 00              BRK                         
FB35: 00              BRK                         
FB36: 00              BRK                         
FB37: 00              BRK                         
FB38: 00              BRK                         
FB39: 00              BRK                         
FB3A: 00              BRK                         
FB3B: 00              BRK                         
FB3C: 00              BRK                         
FB3D: 00              BRK                         
FB3E: 00              BRK                         
FB3F: 00              BRK                         
FB40: 00              BRK                         
FB41: 00              BRK                         
FB42: 00              BRK                         
FB43: 00              BRK                         
FB44: 00              BRK                         
FB45: 00              BRK                         
FB46: 00              BRK                         
FB47: 00              BRK                         
FB48: 00              BRK                         
FB49: 00              BRK                         
FB4A: 00              BRK                         
FB4B: 00              BRK                         
FB4C: 00              BRK                         
FB4D: 00              BRK                         
FB4E: 00              BRK                         
FB4F: 00              BRK                         
FB50: 00              BRK                         
FB51: 00              BRK                         
FB52: 00              BRK                         
FB53: 00              BRK                         
FB54: 00              BRK                         
FB55: 00              BRK                         
FB56: 00              BRK                         
FB57: 00              BRK                         
FB58: 00              BRK                         
FB59: 00              BRK                         
FB5A: 00              BRK                         
FB5B: 00              BRK                         
FB5C: 00              BRK                         
FB5D: 00              BRK                         
FB5E: 00              BRK                         
FB5F: 00              BRK                         
FB60: 00              BRK                         
FB61: 00              BRK                         
FB62: 00              BRK                         
FB63: 00              BRK                         
FB64: 00              BRK                         
FB65: 00              BRK                         
FB66: 00              BRK                         
FB67: 00              BRK                         
FB68: 00              BRK                         
FB69: 00              BRK                         
FB6A: 00              BRK                         
FB6B: 00              BRK                         
FB6C: 00              BRK                         
FB6D: 00              BRK                         
FB6E: 00              BRK                         
FB6F: 00              BRK                         
FB70: 00              BRK                         
FB71: 00              BRK                         
FB72: 00              BRK                         
FB73: 00              BRK                         
FB74: 00              BRK                         
FB75: 00              BRK                         
FB76: 00              BRK                         
FB77: 00              BRK                         
FB78: 00              BRK                         
FB79: 00              BRK                         
FB7A: 00              BRK                         
FB7B: 00              BRK                         
FB7C: 00              BRK                         
FB7D: 00              BRK                         
FB7E: 00              BRK                         
FB7F: 00              BRK                         
FB80: 00              BRK                         
FB81: 00              BRK                         
FB82: 00              BRK                         
FB83: 00              BRK                         
FB84: 00              BRK                         
FB85: 00              BRK                         
FB86: 00              BRK                         
FB87: 00              BRK                         
FB88: 00              BRK                         
FB89: 00              BRK                         
FB8A: 00              BRK                         
FB8B: 00              BRK                         
FB8C: 00              BRK                         
FB8D: 00              BRK                         
FB8E: 00              BRK                         
FB8F: 00              BRK                         
FB90: 00              BRK                         
FB91: 00              BRK                         
FB92: 00              BRK                         
FB93: 00              BRK                         
FB94: 00              BRK                         
FB95: 00              BRK                         
FB96: 00              BRK                         
FB97: 00              BRK                         
FB98: 00              BRK                         
FB99: 00              BRK                         
FB9A: 00              BRK                         
FB9B: 00              BRK                         
FB9C: 00              BRK                         
FB9D: 00              BRK                         
FB9E: 00              BRK                         
FB9F: 00              BRK                         
FBA0: 00              BRK                         
FBA1: 00              BRK                         
FBA2: 00              BRK                         
FBA3: 00              BRK                         
FBA4: 00              BRK                         
FBA5: 00              BRK                         
FBA6: 00              BRK                         
FBA7: 00              BRK                         
FBA8: 00              BRK                         
FBA9: 00              BRK                         
FBAA: 00              BRK                         
FBAB: 00              BRK                         
FBAC: 00              BRK                         
FBAD: 00              BRK                         
FBAE: 00              BRK                         
FBAF: 00              BRK                         
FBB0: 00              BRK                         
FBB1: 00              BRK                         
FBB2: 00              BRK                         
FBB3: 00              BRK                         
FBB4: 00              BRK                         
FBB5: 00              BRK                         
FBB6: 00              BRK                         
FBB7: 00              BRK                         
FBB8: 00              BRK                         
FBB9: 00              BRK                         
FBBA: 00              BRK                         
FBBB: 00              BRK                         
FBBC: 00              BRK                         
FBBD: 00              BRK                         
FBBE: 00              BRK                         
FBBF: 00              BRK                         
FBC0: 00              BRK                         
FBC1: 00              BRK                         
FBC2: 00              BRK                         
FBC3: 00              BRK                         
FBC4: 00              BRK                         
FBC5: 00              BRK                         
FBC6: 00              BRK                         
FBC7: 00              BRK                         
FBC8: 00              BRK                         
FBC9: 00              BRK                         
FBCA: 00              BRK                         
FBCB: 00              BRK                         
FBCC: 00              BRK                         
FBCD: 00              BRK                         
FBCE: 00              BRK                         
FBCF: 00              BRK                         
FBD0: 00              BRK                         
FBD1: 00              BRK                         
FBD2: 00              BRK                         
FBD3: 00              BRK                         
FBD4: 00              BRK                         
FBD5: 00              BRK                         
FBD6: 00              BRK                         
FBD7: 00              BRK                         
FBD8: 00              BRK                         
FBD9: 00              BRK                         
FBDA: 00              BRK                         
FBDB: 00              BRK                         
FBDC: 00              BRK                         
FBDD: 00              BRK                         
FBDE: 00              BRK                         
FBDF: 00              BRK                         
FBE0: 00              BRK                         
FBE1: 00              BRK                         
FBE2: 00              BRK                         
FBE3: 00              BRK                         
FBE4: 00              BRK                         
FBE5: 00              BRK                         
FBE6: 00              BRK                         
FBE7: 00              BRK                         
FBE8: 00              BRK                         
FBE9: 00              BRK                         
FBEA: 00              BRK                         
FBEB: 00              BRK                         
FBEC: 00              BRK                         
FBED: 00              BRK                         
FBEE: 00              BRK                         
FBEF: 00              BRK                         
FBF0: 00              BRK                         
FBF1: 00              BRK                         
FBF2: 00              BRK                         
FBF3: 00              BRK                         
FBF4: 00              BRK                         
FBF5: 00              BRK                         
FBF6: 00              BRK                         
FBF7: 00              BRK                         
FBF8: 42 ; ????
FBF9: 41 00           EOR     ($00,X)             ; {ram.GP_00}
FBFB: 80 ; ????
FBFC: 0C ; ????
FBFD: 04 ; ????
FBFE: 02 ; ????
FBFF: 00              BRK                         
FC00: FF ; ????
FC01: FF ; ????
FC02: FF ; ????
FC03: FF ; ????
FC04: FF ; ????
FC05: FF ; ????
FC06: FF ; ????
FC07: FF ; ????
FC08: FF ; ????
FC09: FF ; ????
FC0A: FF ; ????
FC0B: FF ; ????
FC0C: FF ; ????
FC0D: FF ; ????
FC0E: FF ; ????
FC0F: FF ; ????
FC10: FF ; ????
FC11: FF ; ????
FC12: FF ; ????
FC13: FF ; ????
FC14: FF ; ????
FC15: FF ; ????
FC16: FF ; ????
FC17: FF ; ????
FC18: FF ; ????
FC19: FF ; ????
FC1A: FF ; ????
FC1B: FF ; ????
FC1C: FF ; ????
FC1D: FF ; ????
FC1E: FF ; ????
FC1F: FF ; ????
FC20: FF ; ????
FC21: FF ; ????
FC22: FF ; ????
FC23: FF ; ????
FC24: FF ; ????
FC25: FF ; ????
FC26: FF ; ????
FC27: FF ; ????
FC28: FF ; ????
FC29: FF ; ????
FC2A: FF ; ????
FC2B: FF ; ????
FC2C: FF ; ????
FC2D: FF ; ????
FC2E: FF ; ????
FC2F: FF ; ????
FC30: FF ; ????
FC31: FF ; ????
FC32: FF ; ????
FC33: FF ; ????
FC34: FF ; ????
FC35: FF ; ????
FC36: FF ; ????
FC37: FF ; ????
FC38: FF ; ????
FC39: FE FF FF        INC     $FFFF,X             ; 
FC3C: FF ; ????
FC3D: FF ; ????
FC3E: FF ; ????
FC3F: FF ; ????
FC40: FF ; ????
FC41: FF ; ????
FC42: FF ; ????
FC43: FF ; ????
FC44: FF ; ????
FC45: FF ; ????
FC46: FF ; ????
FC47: FF ; ????
FC48: FF ; ????
FC49: FF ; ????
FC4A: FF ; ????
FC4B: FF ; ????
FC4C: FF ; ????
FC4D: FF ; ????
FC4E: FF ; ????
FC4F: FF ; ????
FC50: FF ; ????
FC51: FF ; ????
FC52: FF ; ????
FC53: FF ; ????
FC54: FF ; ????
FC55: FF ; ????
FC56: FF ; ????
FC57: FF ; ????
FC58: FF ; ????
FC59: FF ; ????
FC5A: FF ; ????
FC5B: FF ; ????
FC5C: FF ; ????
FC5D: FF ; ????
FC5E: FF ; ????
FC5F: FF ; ????
FC60: FF ; ????
FC61: FF ; ????
FC62: FF ; ????
FC63: FF ; ????
FC64: FF ; ????
FC65: FF ; ????
FC66: FF ; ????
FC67: FF ; ????
FC68: FF ; ????
FC69: FF ; ????
FC6A: FF ; ????
FC6B: FF ; ????
FC6C: FF ; ????
FC6D: FF ; ????
FC6E: FF ; ????
FC6F: FF ; ????
FC70: FF ; ????
FC71: FF ; ????
FC72: FF ; ????
FC73: FF ; ????
FC74: FF ; ????
FC75: FF ; ????
FC76: FF ; ????
FC77: FF ; ????
FC78: FE FF 7F        INC     $7FFF,X             
FC7B: FE FF FB        INC     $FBFF,X             ; {}
FC7E: FF ; ????
FC7F: FF ; ????
FC80: FF ; ????
FC81: FF ; ????
FC82: FF ; ????
FC83: FF ; ????
FC84: FF ; ????
FC85: FF ; ????
FC86: FF ; ????
FC87: FF ; ????
FC88: FF ; ????
FC89: FF ; ????
FC8A: FF ; ????
FC8B: FF ; ????
FC8C: FF ; ????
FC8D: FF ; ????
FC8E: FF ; ????
FC8F: FF ; ????
FC90: FF ; ????
FC91: FF ; ????
FC92: FF ; ????
FC93: FF ; ????
FC94: FF ; ????
FC95: FF ; ????
FC96: FF ; ????
FC97: FF ; ????
FC98: FF ; ????
FC99: FF ; ????
FC9A: FF ; ????
FC9B: FF ; ????
FC9C: FF ; ????
FC9D: FF ; ????
FC9E: FF ; ????
FC9F: FF ; ????
FCA0: FF ; ????
FCA1: FF ; ????
FCA2: FF ; ????
FCA3: FF ; ????
FCA4: FD FF FF        SBC     $FFFF,X             ; 
FCA7: FF ; ????
FCA8: FE FF FF        INC     $FFFF,X             ; 
FCAB: FF ; ????
FCAC: FF ; ????
FCAD: FF ; ????
FCAE: FF ; ????
FCAF: FF ; ????
FCB0: FF ; ????
FCB1: FF ; ????
FCB2: FF ; ????
FCB3: FF ; ????
FCB4: FF ; ????
FCB5: FF ; ????
FCB6: FF ; ????
FCB7: FF ; ????
FCB8: FF ; ????
FCB9: FF ; ????
FCBA: FD FF FF        SBC     $FFFF,X             ; 
FCBD: FF ; ????
FCBE: FF ; ????
FCBF: FF ; ????
FCC0: FF ; ????
FCC1: FF ; ????
FCC2: FF ; ????
FCC3: FF ; ????
FCC4: FF ; ????
FCC5: FF ; ????
FCC6: FF ; ????
FCC7: FF ; ????
FCC8: FF ; ????
FCC9: FF ; ????
FCCA: FF ; ????
FCCB: FF ; ????
FCCC: FF ; ????
FCCD: FF ; ????
FCCE: FF ; ????
FCCF: FF ; ????
FCD0: FF ; ????
FCD1: FF ; ????
FCD2: FF ; ????
FCD3: FF ; ????
FCD4: FF ; ????
FCD5: FF ; ????
FCD6: FF ; ????
FCD7: FF ; ????
FCD8: FF ; ????
FCD9: FF ; ????
FCDA: FF ; ????
FCDB: FE FF FF        INC     $FFFF,X             ; 
FCDE: FF ; ????
FCDF: FF ; ????
FCE0: FF ; ????
FCE1: FF ; ????
FCE2: FF ; ????
FCE3: FF ; ????
FCE4: FF ; ????
FCE5: FF ; ????
FCE6: FF ; ????
FCE7: FF ; ????
FCE8: FF ; ????
FCE9: FF ; ????
FCEA: FF ; ????
FCEB: FF ; ????
FCEC: FF ; ????
FCED: FF ; ????
FCEE: FF ; ????
FCEF: FF ; ????
FCF0: FF ; ????
FCF1: FF ; ????
FCF2: FF ; ????
FCF3: FF ; ????
FCF4: FF ; ????
FCF5: FF ; ????
FCF6: FF ; ????
FCF7: FF ; ????
FCF8: FF ; ????
FCF9: FF ; ????
FCFA: FF ; ????
FCFB: FF ; ????
FCFC: DF ; ????
FCFD: FE FF FF        INC     $FFFF,X             ; 
FD00: 00              BRK                         
FD01: 00              BRK                         
FD02: 00              BRK                         
FD03: 00              BRK                         
FD04: 00              BRK                         
FD05: 00              BRK                         
FD06: 00              BRK                         
FD07: 00              BRK                         
FD08: 00              BRK                         
FD09: 00              BRK                         
FD0A: 00              BRK                         
FD0B: 00              BRK                         
FD0C: 00              BRK                         
FD0D: 00              BRK                         
FD0E: 00              BRK                         
FD0F: 00              BRK                         
FD10: 00              BRK                         
FD11: 00              BRK                         
FD12: 00              BRK                         
FD13: 00              BRK                         
FD14: 00              BRK                         
FD15: 00              BRK                         
FD16: 00              BRK                         
FD17: 00              BRK                         
FD18: 00              BRK                         
FD19: 00              BRK                         
FD1A: 00              BRK                         
FD1B: 00              BRK                         
FD1C: 00              BRK                         
FD1D: 00              BRK                         
FD1E: 00              BRK                         
FD1F: 00              BRK                         
FD20: 00              BRK                         
FD21: 00              BRK                         
FD22: 00              BRK                         
FD23: 00              BRK                         
FD24: 00              BRK                         
FD25: 00              BRK                         
FD26: 00              BRK                         
FD27: 00              BRK                         
FD28: 00              BRK                         
FD29: 00              BRK                         
FD2A: 00              BRK                         
FD2B: 00              BRK                         
FD2C: 00              BRK                         
FD2D: 00              BRK                         
FD2E: 00              BRK                         
FD2F: 00              BRK                         
FD30: 00              BRK                         
FD31: 00              BRK                         
FD32: 00              BRK                         
FD33: 00              BRK                         
FD34: 00              BRK                         
FD35: 00              BRK                         
FD36: 00              BRK                         
FD37: 00              BRK                         
FD38: 00              BRK                         
FD39: 00              BRK                         
FD3A: 00              BRK                         
FD3B: 00              BRK                         
FD3C: 00              BRK                         
FD3D: 00              BRK                         
FD3E: 00              BRK                         
FD3F: 00              BRK                         
FD40: 00              BRK                         
FD41: 00              BRK                         
FD42: 00              BRK                         
FD43: 00              BRK                         
FD44: 00              BRK                         
FD45: 00              BRK                         
FD46: 00              BRK                         
FD47: 00              BRK                         
FD48: 00              BRK                         
FD49: 00              BRK                         
FD4A: 00              BRK                         
FD4B: 00              BRK                         
FD4C: 00              BRK                         
FD4D: 00              BRK                         
FD4E: 00              BRK                         
FD4F: 00              BRK                         
FD50: 00              BRK                         
FD51: 00              BRK                         
FD52: 00              BRK                         
FD53: 00              BRK                         
FD54: 00              BRK                         
FD55: 00              BRK                         
FD56: 00              BRK                         
FD57: 00              BRK                         
FD58: 00              BRK                         
FD59: 00              BRK                         
FD5A: 00              BRK                         
FD5B: 00              BRK                         
FD5C: 00              BRK                         
FD5D: 00              BRK                         
FD5E: 00              BRK                         
FD5F: 00              BRK                         
FD60: 00              BRK                         
FD61: 00              BRK                         
FD62: 00              BRK                         
FD63: 00              BRK                         
FD64: 00              BRK                         
FD65: 00              BRK                         
FD66: 00              BRK                         
FD67: 00              BRK                         
FD68: 00              BRK                         
FD69: 00              BRK                         
FD6A: 00              BRK                         
FD6B: 00              BRK                         
FD6C: 00              BRK                         
FD6D: 00              BRK                         
FD6E: 00              BRK                         
FD6F: 00              BRK                         
FD70: 00              BRK                         
FD71: 00              BRK                         
FD72: 00              BRK                         
FD73: 00              BRK                         
FD74: 00              BRK                         
FD75: 00              BRK                         
FD76: 00              BRK                         
FD77: 00              BRK                         
FD78: 00              BRK                         
FD79: 00              BRK                         
FD7A: 00              BRK                         
FD7B: 00              BRK                         
FD7C: 00              BRK                         
FD7D: 00              BRK                         
FD7E: 04 ; ????
FD7F: 00              BRK                         
FD80: 00              BRK                         
FD81: 00              BRK                         
FD82: 00              BRK                         
FD83: 00              BRK                         
FD84: 00              BRK                         
FD85: 00              BRK                         
FD86: 00              BRK                         
FD87: 00              BRK                         
FD88: 00              BRK                         
FD89: 00              BRK                         
FD8A: 00              BRK                         
FD8B: 00              BRK                         
FD8C: 00              BRK                         
FD8D: 00              BRK                         
FD8E: 00              BRK                         
FD8F: 00              BRK                         
FD90: 00              BRK                         
FD91: 00              BRK                         
FD92: 00              BRK                         
FD93: 00              BRK                         
FD94: 00              BRK                         
FD95: 00              BRK                         
FD96: 00              BRK                         
FD97: 00              BRK                         
FD98: 00              BRK                         
FD99: 00              BRK                         
FD9A: 00              BRK                         
FD9B: 00              BRK                         
FD9C: 00              BRK                         
FD9D: 00              BRK                         
FD9E: 00              BRK                         
FD9F: 00              BRK                         
FDA0: 00              BRK                         
FDA1: 00              BRK                         
FDA2: 00              BRK                         
FDA3: 00              BRK                         
FDA4: 00              BRK                         
FDA5: 00              BRK                         
FDA6: 00              BRK                         
FDA7: 00              BRK                         
FDA8: 00              BRK                         
FDA9: 00              BRK                         
FDAA: 00              BRK                         
FDAB: 00              BRK                         
FDAC: 00              BRK                         
FDAD: 00              BRK                         
FDAE: 00              BRK                         
FDAF: 00              BRK                         
FDB0: 00              BRK                         
FDB1: 00              BRK                         
FDB2: 00              BRK                         
FDB3: 00              BRK                         
FDB4: 00              BRK                         
FDB5: 00              BRK                         
FDB6: 00              BRK                         
FDB7: 00              BRK                         
FDB8: 00              BRK                         
FDB9: 00              BRK                         
FDBA: 00              BRK                         
FDBB: 00              BRK                         
FDBC: 00              BRK                         
FDBD: 00              BRK                         
FDBE: 00              BRK                         
FDBF: 00              BRK                         
FDC0: 00              BRK                         
FDC1: 00              BRK                         
FDC2: 00              BRK                         
FDC3: 00              BRK                         
FDC4: 00              BRK                         
FDC5: 00              BRK                         
FDC6: 00              BRK                         
FDC7: 00              BRK                         
FDC8: 00              BRK                         
FDC9: 00              BRK                         
FDCA: 00              BRK                         
FDCB: 00              BRK                         
FDCC: 00              BRK                         
FDCD: 00              BRK                         
FDCE: 00              BRK                         
FDCF: 00              BRK                         
FDD0: 00              BRK                         
FDD1: 00              BRK                         
FDD2: 00              BRK                         
FDD3: 00              BRK                         
FDD4: 00              BRK                         
FDD5: 00              BRK                         
FDD6: 00              BRK                         
FDD7: 00              BRK                         
FDD8: 00              BRK                         
FDD9: 00              BRK                         
FDDA: 00              BRK                         
FDDB: 00              BRK                         
FDDC: 00              BRK                         
FDDD: 00              BRK                         
FDDE: 00              BRK                         
FDDF: 00              BRK                         
FDE0: 00              BRK                         
FDE1: 00              BRK                         
FDE2: 00              BRK                         
FDE3: 00              BRK                         
FDE4: 00              BRK                         
FDE5: 00              BRK                         
FDE6: 00              BRK                         
FDE7: 00              BRK                         
FDE8: 00              BRK                         
FDE9: 00              BRK                         
FDEA: 00              BRK                         
FDEB: 00              BRK                         
FDEC: 00              BRK                         
FDED: 00              BRK                         
FDEE: 00              BRK                         
FDEF: 00              BRK                         
FDF0: 00              BRK                         
FDF1: 00              BRK                         
FDF2: 00              BRK                         
FDF3: 00              BRK                         
FDF4: 00              BRK                         
FDF5: 00              BRK                         
FDF6: 00              BRK                         
FDF7: 00              BRK                         
FDF8: 00              BRK                         
FDF9: 00              BRK                         
FDFA: 00              BRK                         
FDFB: 00              BRK                         
FDFC: 00              BRK                         
FDFD: 00              BRK                         
FDFE: 00              BRK                         
FDFF: 00              BRK                         
FE00: FF ; ????
FE01: FF ; ????
FE02: FF ; ????
FE03: FF ; ????
FE04: FF ; ????
FE05: FF ; ????
FE06: FF ; ????
FE07: FF ; ????
FE08: FF ; ????
FE09: FF ; ????
FE0A: FF ; ????
FE0B: FF ; ????
FE0C: FF ; ????
FE0D: FF ; ????
FE0E: FF ; ????
FE0F: FF ; ????
FE10: FF ; ????
FE11: FF ; ????
FE12: FF ; ????
FE13: FF ; ????
FE14: FF ; ????
FE15: FF ; ????
FE16: FF ; ????
FE17: FF ; ????
FE18: FF ; ????
FE19: FF ; ????
FE1A: FF ; ????
FE1B: FF ; ????
FE1C: FF ; ????
FE1D: FF ; ????
FE1E: FF ; ????
FE1F: FF ; ????
FE20: FF ; ????
FE21: FF ; ????
FE22: FF ; ????
FE23: FF ; ????
FE24: FF ; ????
FE25: FF ; ????
FE26: FF ; ????
FE27: FF ; ????
FE28: FF ; ????
FE29: FF ; ????
FE2A: FF ; ????
FE2B: FF ; ????
FE2C: FF ; ????
FE2D: FF ; ????
FE2E: FF ; ????
FE2F: FF ; ????
FE30: FF ; ????
FE31: FF ; ????
FE32: FF ; ????
FE33: FF ; ????
FE34: FF ; ????
FE35: FF ; ????
FE36: FF ; ????
FE37: FF ; ????
FE38: FF ; ????
FE39: FF ; ????
FE3A: FF ; ????
FE3B: FF ; ????
FE3C: FF ; ????
FE3D: FF ; ????
FE3E: FF ; ????
FE3F: FF ; ????
FE40: FF ; ????
FE41: FF ; ????
FE42: FF ; ????
FE43: FF ; ????
FE44: FF ; ????
FE45: FF ; ????
FE46: FF ; ????
FE47: FF ; ????
FE48: FF ; ????
FE49: FF ; ????
FE4A: FF ; ????
FE4B: FF ; ????
FE4C: FF ; ????
FE4D: FF ; ????
FE4E: FF ; ????
FE4F: FB ; ????
FE50: FF ; ????
FE51: FF ; ????
FE52: FF ; ????
FE53: FF ; ????
FE54: FF ; ????
FE55: FF ; ????
FE56: FF ; ????
FE57: FF ; ????
FE58: FF ; ????
FE59: FF ; ????
FE5A: FF ; ????
FE5B: FF ; ????
FE5C: FF ; ????
FE5D: FF ; ????
FE5E: FF ; ????
FE5F: FF ; ????
FE60: FF ; ????
FE61: FF ; ????
FE62: FF ; ????
FE63: FF ; ????
FE64: FF ; ????
FE65: FF ; ????
FE66: FF ; ????
FE67: FF ; ????
FE68: FF ; ????
FE69: FF ; ????
FE6A: FF ; ????
FE6B: FF ; ????
FE6C: FF ; ????
FE6D: FF ; ????
FE6E: FF ; ????
FE6F: FF ; ????
FE70: FF ; ????
FE71: FF ; ????
FE72: FF ; ????
FE73: FF ; ????
FE74: FF ; ????
FE75: FF ; ????
FE76: FF ; ????
FE77: FF ; ????
FE78: FF ; ????
FE79: FF ; ????
FE7A: FF ; ????
FE7B: FF ; ????
FE7C: FF ; ????
FE7D: FF ; ????
FE7E: FF ; ????
FE7F: FF ; ????
FE80: FF ; ????
FE81: FF ; ????
FE82: FF ; ????
FE83: FF ; ????
FE84: FF ; ????
FE85: FF ; ????
FE86: FF ; ????
FE87: FF ; ????
FE88: FF ; ????
FE89: FF ; ????
FE8A: FF ; ????
FE8B: FF ; ????
FE8C: FF ; ????
FE8D: FF ; ????
FE8E: FF ; ????
FE8F: FF ; ????
FE90: FF ; ????
FE91: FF ; ????
FE92: FF ; ????
FE93: FF ; ????
FE94: FF ; ????
FE95: FF ; ????
FE96: FF ; ????
FE97: FF ; ????
FE98: FD FF FF        SBC     $FFFF,X             ; 
FE9B: FF ; ????
FE9C: FF ; ????
FE9D: FF ; ????
FE9E: FF ; ????
FE9F: FF ; ????
FEA0: FF ; ????
FEA1: FF ; ????
FEA2: 7F ; ????
FEA3: FF ; ????
FEA4: FF ; ????
FEA5: FF ; ????
FEA6: FF ; ????
FEA7: FF ; ????
FEA8: FF ; ????
FEA9: FF ; ????
FEAA: FF ; ????
FEAB: FF ; ????
FEAC: FF ; ????
FEAD: FF ; ????
FEAE: FF ; ????
FEAF: FF ; ????
FEB0: FF ; ????
FEB1: FF ; ????
FEB2: FF ; ????
FEB3: FF ; ????
FEB4: FF ; ????
FEB5: FF ; ????
FEB6: FF ; ????
FEB7: FF ; ????
FEB8: FF ; ????
FEB9: FF ; ????
FEBA: FF ; ????
FEBB: FF ; ????
FEBC: FF ; ????
FEBD: FF ; ????
FEBE: FF ; ????
FEBF: FF ; ????
FEC0: FF ; ????
FEC1: FF ; ????
FEC2: FF ; ????
FEC3: FF ; ????
FEC4: FF ; ????
FEC5: FF ; ????
FEC6: FF ; ????
FEC7: FF ; ????
FEC8: FF ; ????
FEC9: FF ; ????
FECA: FF ; ????
FECB: FF ; ????
FECC: FF ; ????
FECD: FF ; ????
FECE: FF ; ????
FECF: FF ; ????
FED0: FF ; ????
FED1: FF ; ????
FED2: FF ; ????
FED3: FF ; ????
FED4: FF ; ????
FED5: FF ; ????
FED6: FF ; ????
FED7: FF ; ????
FED8: FF ; ????
FED9: FF ; ????
FEDA: FF ; ????
FEDB: FF ; ????
FEDC: FF ; ????
FEDD: FF ; ????
FEDE: FF ; ????
FEDF: FF ; ????
FEE0: FF ; ????
FEE1: FF ; ????
FEE2: FF ; ????
FEE3: FF ; ????
FEE4: FF ; ????
FEE5: FF ; ????
FEE6: FF ; ????
FEE7: FF ; ????
FEE8: FF ; ????
FEE9: FF ; ????
FEEA: FF ; ????
FEEB: FF ; ????
FEEC: FF ; ????
FEED: FF ; ????
FEEE: FF ; ????
FEEF: FF ; ????
FEF0: FF ; ????
FEF1: FF ; ????
FEF2: FF ; ????
FEF3: FF ; ????
FEF4: FF ; ????
FEF5: FF ; ????
FEF6: FF ; ????
FEF7: FF ; ????
FEF8: FF ; ????
FEF9: FF ; ????
FEFA: FF ; ????
FEFB: FF ; ????
FEFC: FF ; ????
FEFD: FF ; ????
FEFE: FF ; ????
FEFF: FF ; ????
FF00: 00              BRK                         
FF01: 00              BRK                         
FF02: 00              BRK                         
FF03: 00              BRK                         
FF04: 00              BRK                         
FF05: 00              BRK                         
FF06: 00              BRK                         
FF07: 00              BRK                         
FF08: 00              BRK                         
FF09: 00              BRK                         
FF0A: 00              BRK                         
FF0B: 00              BRK                         
FF0C: 00              BRK                         
FF0D: 00              BRK                         
FF0E: 00              BRK                         
FF0F: 00              BRK                         
FF10: 00              BRK                         
FF11: 00              BRK                         
FF12: 00              BRK                         
FF13: 00              BRK                         
FF14: 00              BRK                         
FF15: 00              BRK                         
FF16: 00              BRK                         
FF17: 00              BRK                         
FF18: 00              BRK                         
FF19: 00              BRK                         
FF1A: 00              BRK                         
FF1B: 00              BRK                         
FF1C: 00              BRK                         
FF1D: 00              BRK                         
FF1E: 00              BRK                         
FF1F: 00              BRK                         
FF20: 00              BRK                         
FF21: 00              BRK                         
FF22: 00              BRK                         
FF23: 00              BRK                         
FF24: 00              BRK                         
FF25: 00              BRK                         
FF26: 00              BRK                         
FF27: 00              BRK                         
FF28: 00              BRK                         
FF29: 00              BRK                         
FF2A: 00              BRK                         
FF2B: 00              BRK                         
FF2C: 00              BRK                         
FF2D: 00              BRK                         
FF2E: 00              BRK                         
FF2F: 00              BRK                         
FF30: 00              BRK                         
FF31: 00              BRK                         
FF32: 00              BRK                         
FF33: 00              BRK                         
FF34: 00              BRK                         
FF35: 00              BRK                         
FF36: 00              BRK                         
FF37: 00              BRK                         
FF38: 00              BRK                         
FF39: 00              BRK                         
FF3A: 00              BRK                         
FF3B: 00              BRK                         
FF3C: 00              BRK                         
FF3D: 00              BRK                         
FF3E: 00              BRK                         
FF3F: 00              BRK                         
FF40: 00              BRK                         
FF41: 00              BRK                         
FF42: 00              BRK                         
FF43: 00              BRK                         
FF44: 00              BRK                         
FF45: 00              BRK                         
FF46: 00              BRK                         
FF47: 00              BRK                         
FF48: 00              BRK                         
FF49: 00              BRK                         
FF4A: 00              BRK                         
FF4B: 00              BRK                         
FF4C: 00              BRK                         
FF4D: 00              BRK                         
FF4E: 00              BRK                         
FF4F: 00              BRK                         
FF50: 00              BRK                         
FF51: 00              BRK                         
FF52: 00              BRK                         
FF53: 00              BRK                         
FF54: 00              BRK                         
FF55: 00              BRK                         
FF56: 00              BRK                         
FF57: 00              BRK                         
FF58: 00              BRK                         
FF59: 00              BRK                         
FF5A: 00              BRK                         
FF5B: 00              BRK                         
FF5C: 00              BRK                         
FF5D: 00              BRK                         
FF5E: 00              BRK                         
FF5F: 00              BRK                         
FF60: 00              BRK                         
FF61: 00              BRK                         
FF62: 00              BRK                         
FF63: 00              BRK                         
FF64: 00              BRK                         
FF65: 00              BRK                         
FF66: 00              BRK                         
FF67: 00              BRK                         
FF68: 00              BRK                         
FF69: 00              BRK                         
FF6A: 00              BRK                         
FF6B: 00              BRK                         
FF6C: 00              BRK                         
FF6D: 00              BRK                         
FF6E: 00              BRK                         
FF6F: 00              BRK                         
FF70: 00              BRK                         
FF71: 00              BRK                         
FF72: 00              BRK                         
FF73: 00              BRK                         
FF74: 00              BRK                         
FF75: 00              BRK                         
FF76: 00              BRK                         
FF77: 00              BRK                         
FF78: 00              BRK                         
FF79: 00              BRK                         
FF7A: 00              BRK                         
FF7B: 00              BRK                         
FF7C: 00              BRK                         
FF7D: 00              BRK                         
FF7E: 00              BRK                         
FF7F: 00              BRK                         
```

# RESET

```code
RESET:
FF80: A9 00           LDA     #$00                
FF82: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1}
FF85: A9 FF           LDA     #$FF                
FF87: 8D FF FF        STA     $FFFF               ; 
FF8A: A9 0F           LDA     #$0F                
FF8C: 8D FF 9F        STA     $9FFF               
FF8F: 4A              LSR     A                   
FF90: 8D FF 9F        STA     $9FFF               
FF93: 4A              LSR     A                   
FF94: 8D FF 9F        STA     $9FFF               
FF97: 4A              LSR     A                   
FF98: 8D FF 9F        STA     $9FFF               
FF9B: 4A              LSR     A                   
FF9C: 8D FF 9F        STA     $9FFF               
FF9F: A9 00           LDA     #$00                
FFA1: 8D FF BF        STA     $BFFF               
FFA4: 4A              LSR     A                   
FFA5: 8D FF BF        STA     $BFFF               
FFA8: 4A              LSR     A                   
FFA9: 8D FF BF        STA     $BFFF               
FFAC: 4A              LSR     A                   
FFAD: 8D FF BF        STA     $BFFF               
FFB0: 4A              LSR     A                   
FFB1: 8D FF BF        STA     $BFFF               
FFB4: A9 00           LDA     #$00                
FFB6: 8D FF DF        STA     $DFFF               ; {}
FFB9: 4A              LSR     A                   
FFBA: 8D FF DF        STA     $DFFF               ; {}
FFBD: 4A              LSR     A                   
FFBE: 8D FF DF        STA     $DFFF               ; {}
FFC1: 4A              LSR     A                   
FFC2: 8D FF DF        STA     $DFFF               ; {}
FFC5: 4A              LSR     A                   
FFC6: 8D FF DF        STA     $DFFF               ; {}
FFC9: 4C 00 C0        JMP     $C000               ; {}
```

# IRQ and BRK

```code
IRQBRK:
FFCC: 40              RTI                         
```

```code
FFCD: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00                       
FFE0: FF FF FF FF FF FF 

FFE6: 4B 49 44 20 49 43 41 52 55 53 ; KID_ICARUS
FFF0: C0 FA 00 00 38 04 01 09 01 B9
```

# Vectors

```code
FFFA: 66 C8    ; NMI to C866
FFFC: 80 FF    ; RESET to FF80
FFFE: CC FF    ; IRQ/BRK to FFCC
```

