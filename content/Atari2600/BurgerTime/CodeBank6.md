![Burger Time](A2600BT.jpg)

# Burger Time Bank 6

>>> cpu 6502

>>> memoryTable hard 
[Hardware Info](../Stella.md)

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

```code
F000: 08              PHP                         
F001: 04 ; ????
F002: 02 ; ????
F003: 01 20           ORA     ($20,X)               
F005: 0B ; ????
F006: F0 20           BEQ     $F028                   
F008: 63 ; ????
F009: F0 60           BEQ     $F06B                   
F00B: 20 0D F3        JSR     $F30D                   
F00E: 90 52           BCC     $F062                   
F010: AD 58 F9        LDA     $F958                   
F013: D0 08           BNE     $F01D                   
F015: A9 0C           LDA     #$0C                  
F017: A0 01           LDY     #$01                  
F019: 20 3F F3        JSR     $F33F                   
F01C: 60              RTS                         
F01D: AD 56 F9        LDA     $F956                   
F020: 29 01           AND     #$01                  
F022: D0 3E           BNE     $F062                   
F024: 8D 3F F8        STA     $F83F                   
F027: A9 0A           LDA     #$0A                  
F029: A0 01           LDY     #$01                  
F02B: 20 3F F3        JSR     $F33F                   
F02E: AD 48 F9        LDA     $F948                   
F031: C9 FF           CMP     #$FF                  
F033: D0 02           BNE     $F037                   
F035: A9 00           LDA     #$00                  
F037: 8D 39 F8        STA     $F839                   
F03A: A5 BD           LDA     $BD                   
F03C: 8D 3A F8        STA     $F83A                   
F03F: A5 C2           LDA     $C2                   
F041: 8D 3B F8        STA     $F83B                   
F044: AD 4C F9        LDA     $F94C                   
F047: 8D 3D F8        STA     $F83D                   
F04A: AD 56 F9        LDA     $F956                   
F04D: 09 01           ORA     #$01                  
F04F: 8D 56 F8        STA     $F856                   
F052: A9 32           LDA     #$32                  
F054: 8D 3E F8        STA     $F83E                   
F057: F8              SED                         
F058: AD 58 F9        LDA     $F958                   
F05B: 38              SEC                         
F05C: E9 01           SBC     #$01                  
F05E: 8D 58 F8        STA     $F858                   
F061: D8              CLD                         
F062: 60              RTS                         
F063: 20 0E F2        JSR     $F20E                   
F066: AD 56 F9        LDA     $F956                   
F069: 29 01           AND     #$01                  
F06B: D0 03           BNE     $F070                   
F06D: 4C 20 F1        JMP     $F120                   
F070: AD 3E F9        LDA     $F93E                   
F073: 38              SEC                         
F074: E9 01           SBC     #$01                  
F076: 8D 3E F8        STA     $F83E                   
F079: F0 4D           BEQ     $F0C8                   
F07B: A5 DE           LDA     $DE                   
F07D: 29 01           AND     #$01                  
F07F: F0 53           BEQ     $F0D4                   
F081: A2 03           LDX     #$03                  
F083: A5 C7           LDA     $C7                   
F085: 6A              ROR     A                   
F086: 90 16           BCC     $F09E                   
F088: AD 40 F9        LDA     $F940                   
F08B: 3D 00 F0        AND     $F000,X                 
F08E: D0 05           BNE     $F095                   
F090: A9 BE           LDA     #$BE                  
F092: 8D 41 F8        STA     $F841                   
F095: AD 40 F9        LDA     $F940                   
F098: 1D 00 F0        ORA     $F000,X                 
F09B: 8D 40 F8        STA     $F840                   
F09E: 46 C7           LSR     $C7                   
F0A0: CA              DEX                         
F0A1: 10 E0           BPL     $F083                   
F0A3: A5 CC           LDA     $CC                   
F0A5: F0 07           BEQ     $F0AE                   
F0A7: A9 0B           LDA     #$0B                  
F0A9: A0 01           LDY     #$01                  
F0AB: 20 3F F3        JSR     $F33F                   
F0AE: AD 3A F9        LDA     $F93A                   
F0B1: 85 BD           STA     $BD                   
F0B3: AD 3B F9        LDA     $F93B                   
F0B6: 85 C2           STA     $C2                   
F0B8: AD 39 F9        LDA     $F939                   
F0BB: 4A              LSR     A                   
F0BC: 8D 4C F8        STA     $F84C                   
F0BF: A5 DF           LDA     $DF                   
F0C1: 29 F0           AND     #$F0                  
F0C3: 09 03           ORA     #$03                  
F0C5: 85 DF           STA     $DF                   
F0C7: 60              RTS                         
F0C8: AD 56 F9        LDA     $F956                   
F0CB: 29 FE           AND     #$FE                  
F0CD: 8D 56 F8        STA     $F856                   
F0D0: 4C AE F0        JMP     $F0AE                   
F0D3: 60              RTS                         
F0D4: 20 20 F1        JSR     $F120                   
F0D7: AD 56 F9        LDA     $F956                   
F0DA: 29 40           AND     #$40                  
F0DC: D0 26           BNE     $F104                   
F0DE: A9 04           LDA     #$04                  
F0E0: 8D 4C F8        STA     $F84C                   
F0E3: A9 08           LDA     #$08                  
F0E5: 85 C7           STA     $C7                   
F0E7: A5 DF           LDA     $DF                   
F0E9: 29 F0           AND     #$F0                  
F0EB: 09 03           ORA     #$03                  
F0ED: 85 DF           STA     $DF                   
F0EF: AD 39 F9        LDA     $F939                   
F0F2: F0 11           BEQ     $F105                   
F0F4: C9 04           CMP     #$04                  
F0F6: F0 16           BEQ     $F10E                   
F0F8: C9 02           CMP     #$02                  
F0FA: F0 1B           BEQ     $F117                   
F0FC: AD 3B F9        LDA     $F93B                   
F0FF: 18              CLC                         
F100: 65 C7           ADC     $C7                   
F102: 85 C2           STA     $C2                   
F104: 60              RTS                         
F105: AD 3A F9        LDA     $F93A                   
F108: 18              CLC                         
F109: 65 C7           ADC     $C7                   
F10B: 85 BD           STA     $BD                   
F10D: 60              RTS                         
F10E: AD 3A F9        LDA     $F93A                   
F111: 38              SEC                         
F112: E5 C7           SBC     $C7                   
F114: 85 BD           STA     $BD                   
F116: 60              RTS                         
F117: AD 3B F9        LDA     $F93B                   
F11A: 38              SEC                         
F11B: E5 C7           SBC     $C7                   
F11D: 85 C2           STA     $C2                   
F11F: 60              RTS                         
F120: AD 40 F9        LDA     $F940                   
F123: F0 10           BEQ     $F135                   
F125: AD 41 F9        LDA     $F941                   
F128: 38              SEC                         
F129: E9 01           SBC     #$01                  
F12B: 8D 41 F8        STA     $F841                   
F12E: D0 05           BNE     $F135                   
F130: A9 00           LDA     #$00                  
F132: 8D 40 F8        STA     $F840                   
F135: A5 CC           LDA     $CC                   
F137: D0 0C           BNE     $F145                   
F139: A5 DE           LDA     $DE                   
F13B: D0 05           BNE     $F142                   
F13D: A9 00           LDA     #$00                  
F13F: 8D 46 F8        STA     $F846                   
F142: 4C D0 F1        JMP     $F1D0                   
F145: A2 03           LDX     #$03                  
F147: A5 C7           LDA     $C7                   
F149: 6A              ROR     A                   
F14A: 90 61           BCC     $F1AD                   
F14C: AD 40 F9        LDA     $F940                   
F14F: 3D 00 F0        AND     $F000,X                 
F152: D0 59           BNE     $F1AD                   
F154: AD 36 F9        LDA     $F936                   
F157: 3D 00 F0        AND     $F000,X                 
F15A: D0 51           BNE     $F1AD                   
F15C: AD 46 F9        LDA     $F946                   
F15F: 18              CLC                         
F160: 69 01           ADC     #$01                  
F162: 8D 46 F8        STA     $F846                   
F165: C9 08           CMP     #$08                  
F167: D0 67           BNE     $F1D0                   
F169: A9 0F           LDA     #$0F                  
F16B: 8D 40 F8        STA     $F840                   
F16E: 8D 36 F8        STA     $F836                   
F171: AD 56 F9        LDA     $F956                   
F174: 09 40           ORA     #$40                  
F176: 8D 56 F8        STA     $F856                   
F179: A5 DF           LDA     $DF                   
F17B: 29 0F           AND     #$0F                  
F17D: 09 10           ORA     #$10                  
F17F: 85 DF           STA     $DF                   
F181: A9 04           LDA     #$04                  
F183: 8D 4D F8        STA     $F84D                   
F186: AD 56 F9        LDA     $F956                   
F189: 29 FE           AND     #$FE                  
F18B: 8D 56 F8        STA     $F856                   
F18E: A9 00           LDA     #$00                  
F190: 8D 3E F8        STA     $F83E                   
F193: 8D 4B F8        STA     $F84B                   
F196: F8              SED                         
F197: AD 57 F9        LDA     $F957                   
F19A: 38              SEC                         
F19B: E9 01           SBC     #$01                  
F19D: 8D 57 F8        STA     $F857                   
F1A0: D8              CLD                         
F1A1: D0 0F           BNE     $F1B2                   
F1A3: AD 56 F9        LDA     $F956                   
F1A6: 09 80           ORA     #$80                  
F1A8: 8D 56 F8        STA     $F856                   
F1AB: D0 05           BNE     $F1B2                   
F1AD: 46 C7           LSR     $C7                   
F1AF: CA              DEX                         
F1B0: 10 95           BPL     $F147                   
F1B2: AD 56 F9        LDA     $F956                   
F1B5: 29 40           AND     #$40                  
F1B7: F0 17           BEQ     $F1D0                   
F1B9: AD 56 F9        LDA     $F956                   
F1BC: 29 20           AND     #$20                  
F1BE: D0 0F           BNE     $F1CF                   
F1C0: A9 01           LDA     #$01                  
F1C2: A0 01           LDY     #$01                  
F1C4: 20 3F F3        JSR     $F33F                   
F1C7: AD 56 F9        LDA     $F956                   
F1CA: 09 20           ORA     #$20                  
F1CC: 8D 56 F8        STA     $F856                   
F1CF: 60              RTS                         
F1D0: AD 86 F9        LDA     $F986                   
F1D3: C9 10           CMP     #$10                  
F1D5: D0 F8           BNE     $F1CF                   
F1D7: A9 FF           LDA     #$FF                  
F1D9: 8D 40 F8        STA     $F840                   
F1DC: 8D 36 F8        STA     $F836                   
F1DF: AD 56 F9        LDA     $F956                   
F1E2: 29 10           AND     #$10                  
F1E4: D0 E9           BNE     $F1CF                   
F1E6: AD 56 F9        LDA     $F956                   
F1E9: 09 10           ORA     #$10                  
F1EB: 8D 56 F8        STA     $F856                   
F1EE: A9 02           LDA     #$02                  
F1F0: A0 01           LDY     #$01                  
F1F2: 20 43 F3        JSR     $F343                   
F1F5: A9 00           LDA     #$00                  
F1F7: 8D 16 F8        STA     $F816                   
F1FA: 8D 17 F8        STA     $F817                   
F1FD: 8D 18 F8        STA     $F818                   
F200: 8D 19 F8        STA     $F819                   
F203: 60              RTS                         
F204: 07 ; ????
F205: 00              BRK                         
F206: 01 02           ORA     ($02,X)               
F208: 02 ; ????
F209: 80 ; ????
F20A: 40              RTI                         
F20B: 80 ; ????
F20C: 40              RTI                         
F20D: 80 ; ????
F20E: A9 00           LDA     #$00                  
F210: 85 C7           STA     $C7                   
F212: A2 03           LDX     #$03                  
F214: BC 04 F2        LDY     $F204,X                 
F217: B9 00 00        LDA     $0000,Y                 
F21A: 3D 09 F2        AND     $F209,X                 
F21D: F0 03           BEQ     $F222                   
F21F: 38              SEC                         
F220: B0 01           BCS     $F223                   
F222: 18              CLC                         
F223: 26 C7           ROL     $C7                   
F225: CA              DEX                         
F226: 10 EC           BPL     $F214                   
F228: A5 C7           LDA     $C7                   
F22A: 85 CC           STA     $CC                   
F22C: AD 4B F9        LDA     $F94B                   
F22F: D0 03           BNE     $F234                   
F231: 4C B8 F2        JMP     $F2B8                   
F234: A5 DE           LDA     $DE                   
F236: 29 03           AND     #$03                  
F238: D0 0E           BNE     $F248                   
F23A: AD 4B F9        LDA     $F94B                   
F23D: 38              SEC                         
F23E: E9 01           SBC     #$01                  
F240: 8D 4B F8        STA     $F84B                   
F243: F0 49           BEQ     $F28E                   
F245: 4C B8 F2        JMP     $F2B8                   
F248: A5 DE           LDA     $DE                   
F24A: 29 03           AND     #$03                  
F24C: C9 03           CMP     #$03                  
F24E: F0 3E           BEQ     $F28E                   
F250: C9 01           CMP     #$01                  
F252: F0 65           BEQ     $F2B9                   
F254: A5 C7           LDA     $C7                   
F256: 29 01           AND     #$01                  
F258: F0 5E           BEQ     $F2B8                   
F25A: A5 C7           LDA     $C7                   
F25C: 29 FE           AND     #$FE                  
F25E: 85 C7           STA     $C7                   
F260: 85 CC           STA     $CC                   
F262: F8              SED                         
F263: AD 58 F9        LDA     $F958                   
F266: 18              CLC                         
F267: 69 01           ADC     #$01                  
F269: 8D 58 F8        STA     $F858                   
F26C: D8              CLD                         
F26D: A5 C7           LDA     $C7                   
F26F: 85 D6           STA     $D6                   
F271: A9 05           LDA     #$05                  
F273: A0 01           LDY     #$01                  
F275: 86 D7           STX     $D7                   
F277: 20 43 F3        JSR     $F343                   
F27A: A5 D6           LDA     $D6                   
F27C: 85 CC           STA     $CC                   
F27E: 85 C7           STA     $C7                   
F280: A9 00           LDA     #$00                  
F282: A2 05           LDX     #$05                  
F284: 20 65 F3        JSR     $F365                   
F287: A9 00           LDA     #$00                  
F289: 8D 4B F8        STA     $F84B                   
F28C: A6 D7           LDX     $D7                   
F28E: A5 C7           LDA     $C7                   
F290: 29 FE           AND     #$FE                  
F292: 85 C7           STA     $C7                   
F294: A5 DF           LDA     $DF                   
F296: 29 0F           AND     #$0F                  
F298: 0D 45 F9        ORA     $F945                   
F29B: 85 DF           STA     $DF                   
F29D: AD 44 F9        LDA     $F944                   
F2A0: 8D 4D F8        STA     $F84D                   
F2A3: AD 42 F9        LDA     $F942                   
F2A6: 85 BE           STA     $BE                   
F2A8: AD 43 F9        LDA     $F943                   
F2AB: 85 C3           STA     $C3                   
F2AD: A2 B5           LDX     #$B5                  
F2AF: A5 BE           LDA     $BE                   
F2B1: 20 8D F3        JSR     $F38D                   
F2B4: A5 C7           LDA     $C7                   
F2B6: 85 CC           STA     $CC                   
F2B8: 60              RTS                         
F2B9: A5 DF           LDA     $DF                   
F2BB: 29 F0           AND     #$F0                  
F2BD: 8D 45 F8        STA     $F845                   
F2C0: AD 4D F9        LDA     $F94D                   
F2C3: 8D 44 F8        STA     $F844                   
F2C6: A5 BE           LDA     $BE                   
F2C8: 8D 42 F8        STA     $F842                   
F2CB: A5 C3           LDA     $C3                   
F2CD: 8D 43 F8        STA     $F843                   
F2D0: A5 DF           LDA     $DF                   
F2D2: 29 0F           AND     #$0F                  
F2D4: AE 59 F9        LDX     $F959                   
F2D7: 1D FB F2        ORA     $F2FB,X                 
F2DA: 85 DF           STA     $DF                   
F2DC: BD FF F2        LDA     $F2FF,X                 
F2DF: 8D 4D F8        STA     $F84D                   
F2E2: AE 55 F9        LDX     $F955                   
F2E5: BD 03 F3        LDA     $F303,X                 
F2E8: 85 BE           STA     $BE                   
F2EA: BD 08 F3        LDA     $F308,X                 
F2ED: 85 C3           STA     $C3                   
F2EF: A2 B5           LDX     #$B5                  
F2F1: A5 BE           LDA     $BE                   
F2F3: 20 8D F3        JSR     $F38D                   
F2F6: A5 C7           LDA     $C7                   
F2F8: 85 CC           STA     $CC                   
F2FA: 60              RTS                         
F2FB: 30 30           BMI     $F32D                   
F2FD: 30 30           BMI     $F32F                   
F2FF: 05 06           ORA     $06                   
F301: 07 ; ????
F302: 07 ; ????
F303: 56 41           LSR     $41,X                 
F305: 50 50           BVC     $F357                   
F307: 4C 14 1E        JMP     $1E14                   
F30A: 14 ; ????
F30B: 28              PLP                         
F30C: 14 ; ????
F30D: A5 3C           LDA     $3C                   
F30F: 30 13           BMI     $F324                   
F311: AD 47 F9        LDA     $F947                   
F314: F0 07           BEQ     $F31D                   
F316: A9 01           LDA     #$01                  
F318: 8D 47 F8        STA     $F847                   
F31B: 18              CLC                         
F31C: 60              RTS                         
F31D: A9 01           LDA     #$01                  
F31F: 8D 47 F8        STA     $F847                   
F322: 38              SEC                         
F323: 60              RTS                         
F324: A9 00           LDA     #$00                  
F326: 8D 47 F8        STA     $F847                   
F329: 18              CLC                         
F32A: 60              RTS                         
F32B: 8D F7 F8        STA     $F8F7                   
F32E: A5 80           LDA     $80                   
F330: 29 C0           AND     #$C0                  
F332: D0 09           BNE     $F33D                   
F334: AD F7 F9        LDA     $F9F7                   
F337: 24 80           BIT     $80                   
F339: 10 08           BPL     $F343                   
F33B: 50 02           BVC     $F33F                   
F33D: 38              SEC                         
F33E: 60              RTS                         
F33F: A2 01           LDX     #$01                  
F341: D0 02           BNE     $F345                   
F343: A2 00           LDX     #$00                  
F345: 9D 00 F8        STA     $F800,X                 
F348: 98              TYA                         
F349: 9D 06 F8        STA     $F806,X                 
F34C: A9 00           LDA     #$00                  
F34E: 9D 04 F8        STA     $F804,X                 
F351: 9D 02 F8        STA     $F802,X                 
F354: A4 80           LDY     $80                   
F356: 8A              TXA                         
F357: F0 05           BEQ     $F35E                   
F359: 98              TYA                         
F35A: 09 40           ORA     #$40                  
F35C: D0 03           BNE     $F361                   
F35E: 98              TYA                         
F35F: 09 80           ORA     #$80                  
F361: 85 80           STA     $80                   
F363: 18              CLC                         
F364: 60              RTS                         
F365: F8              SED                         
F366: 18              CLC                         
F367: 6D 71 F9        ADC     $F971                   
F36A: 8D 71 F8        STA     $F871                   
F36D: 8A              TXA                         
F36E: 6D 70 F9        ADC     $F970                   
F371: 8D 70 F8        STA     $F870                   
F374: 90 0A           BCC     $F380                   
F376: 18              CLC                         
F377: AD 57 F9        LDA     $F957                   
F37A: 69 01           ADC     #$01                  
F37C: 8D 57 F8        STA     $F857                   
F37F: 38              SEC                         
F380: A9 00           LDA     #$00                  
F382: 6D 6F F9        ADC     $F96F                   
F385: 8D 6F F8        STA     $F86F                   
F388: D8              CLD                         
F389: 60              RTS                         
F38A: 38              SEC                         
F38B: E9 03           SBC     #$03                  
F38D: 48              PHA                         
F38E: 29 0F           AND     #$0F                  
F390: 85 CC           STA     $CC                   
F392: 68              PLA                         
F393: 4A              LSR     A                   
F394: 4A              LSR     A                   
F395: 4A              LSR     A                   
F396: 4A              LSR     A                   
F397: 85 CD           STA     $CD                   
F399: 18              CLC                         
F39A: 65 CC           ADC     $CC                   
F39C: C9 0F           CMP     #$0F                  
F39E: 90 04           BCC     $F3A4                   
F3A0: E9 0F           SBC     #$0F                  
F3A2: E6 CD           INC     $CD                   
F3A4: 49 07           EOR     #$07                  
F3A6: 0A              ASL     A                   
F3A7: 0A              ASL     A                   
F3A8: 0A              ASL     A                   
F3A9: 0A              ASL     A                   
F3AA: 05 CD           ORA     $CD                   
F3AC: 95 00           STA     $00,X                 
F3AE: 60              RTS                         
F3AF: A2 04           LDX     #$04                  
F3B1: 85 02           STA     $02                   
F3B3: B5 B4           LDA     $B4,X                 
F3B5: 95 20           STA     $20,X                 
F3B7: 29 0F           AND     #$0F                  
F3B9: A8              TAY                         
F3BA: A5 80           LDA     $80                   
F3BC: 88              DEY                         
F3BD: 10 FD           BPL     $F3BC                   
F3BF: 95 10           STA     $10,X                 
F3C1: 85 02           STA     $02                   
F3C3: CA              DEX                         
F3C4: 10 EB           BPL     $F3B1                   
F3C6: 85 02           STA     $02                   
F3C8: 85 2A           STA     $2A                   
F3CA: 60              RTS                         
F3CB: A5 BD           LDA     $BD                   
F3CD: A2 B4           LDX     #$B4                  
F3CF: 20 8D F3        JSR     $F38D                   
F3D2: 60              RTS                         
F3D3: A0 00           LDY     #$00                  
F3D5: B1 DC           LDA     ($DC),Y               
F3D7: 30 0D           BMI     $F3E6                   
F3D9: 95 15           STA     $15,X                 
F3DB: C8              INY                         
F3DC: B1 DC           LDA     ($DC),Y               
F3DE: 95 17           STA     $17,X                 
F3E0: C8              INY                         
F3E1: B1 DC           LDA     ($DC),Y               
F3E3: 95 19           STA     $19,X                 
F3E5: 60              RTS                         
F3E6: BD 06 F9        LDA     $F906,X                 
F3E9: 38              SEC                         
F3EA: E9 01           SBC     #$01                  
F3EC: 9D 06 F8        STA     $F806,X                 
F3EF: F0 0E           BEQ     $F3FF                   
F3F1: A9 00           LDA     #$00                  
F3F3: 9D 04 F8        STA     $F804,X                 
F3F6: 9D 02 F8        STA     $F802,X                 
F3F9: 20 50 F4        JSR     $F450                   
F3FC: 4C D3 F3        JMP     $F3D3                   
F3FF: A5 80           LDA     $80                   
F401: 3D 07 F4        AND     $F407,X                 
F404: 85 80           STA     $80                   
F406: 60              RTS                         
F407: 7F ; ????
F408: BF ; ????
F409: 24 80           BIT     $80                   
F40B: 10 05           BPL     $F412                   
F40D: A2 00           LDX     #$00                  
F40F: 20 1C F4        JSR     $F41C                   
F412: 24 80           BIT     $80                   
F414: 50 05           BVC     $F41B                   
F416: A2 01           LDX     #$01                  
F418: 20 1C F4        JSR     $F41C                   
F41B: 60              RTS                         
F41C: BD 04 F9        LDA     $F904,X                 
F41F: 18              CLC                         
F420: 69 01           ADC     #$01                  
F422: 9D 04 F8        STA     $F804,X                 
F425: 20 50 F4        JSR     $F450                   
F428: BD 04 F9        LDA     $F904,X                 
F42B: A0 03           LDY     #$03                  
F42D: D1 DC           CMP     ($DC),Y               
F42F: 90 1E           BCC     $F44F                   
F431: A9 00           LDA     #$00                  
F433: 9D 04 F8        STA     $F804,X                 
F436: BD 02 F9        LDA     $F902,X                 
F439: 18              CLC                         
F43A: 69 04           ADC     #$04                  
F43C: 9D 02 F8        STA     $F802,X                 
F43F: A5 DC           LDA     $DC                   
F441: 18              CLC                         
F442: 69 04           ADC     #$04                  
F444: 85 DC           STA     $DC                   
F446: A9 00           LDA     #$00                  
F448: 65 DD           ADC     $DD                   
F44A: 85 DD           STA     $DD                   
F44C: 4C D3 F3        JMP     $F3D3                   
F44F: 60              RTS                         
F450: 86 C7           STX     $C7                   
F452: BD 00 F9        LDA     $F900,X                 
F455: 0A              ASL     A                   
F456: AA              TAX                         
F457: 86 C8           STX     $C8                   
F459: BD 70 F4        LDA     $F470,X                 
F45C: 18              CLC                         
F45D: A6 C7           LDX     $C7                   
F45F: 7D 02 F9        ADC     $F902,X                 
F462: 85 DC           STA     $DC                   
F464: A9 00           LDA     #$00                  
F466: A6 C8           LDX     $C8                   
F468: 7D 71 F4        ADC     $F471,X                 
F46B: 85 DD           STA     $DD                   
F46D: A6 C7           LDX     $C7                   
F46F: 60              RTS                         
F470: 2D F7 8A        AND     $8AF7                   
F473: F4 ; ????
F474: DD F6 86        CMP     $86F6,X                 
F477: F5 41           SBC     $41,X                 
F479: F5 DF           SBC     $DF,X                 
F47B: F4 ; ????
F47C: 04 ; ????
F47D: F5 EF           SBC     $EF,X                 
F47F: F5 49           SBC     $49,X                 
F481: F6 6E           INC     $6E,X                 
F483: F6 2C           INC     $2C,X                 
F485: F6 97           INC     $97,X                 
F487: F6 C0           INC     $C0,X                 
F489: F6 0C           INC     $0C,X                 
F48B: 09 00           ORA     #$00                  
F48D: 01 0C           ORA     ($0C,X)               
F48F: 09 0F           ORA     #$0F                  
F491: 07 ; ????
F492: 0C ; ????
F493: 13 ; ????
F494: 0F ; ????
F495: 04 ; ????
F496: 0C ; ????
F497: 07 ; ????
F498: 0F ; ????
F499: 07 ; ????
F49A: 0C ; ????
F49B: 13 ; ????
F49C: 0F ; ????
F49D: 04 ; ????
F49E: 04 ; ????
F49F: 13 ; ????
F4A0: 0F ; ????
F4A1: 07 ; ????
F4A2: 0C ; ????
F4A3: 13 ; ????
F4A4: 0F ; ????
F4A5: 04 ; ????
F4A6: 0C ; ????
F4A7: 04 ; ????
F4A8: 0F ; ????
F4A9: 07 ; ????
F4AA: 0C ; ????
F4AB: 13 ; ????
F4AC: 0F ; ????
F4AD: 04 ; ????
F4AE: 04 ; ????
F4AF: 13 ; ????
F4B0: 0F ; ????
F4B1: 07 ; ????
F4B2: 0C ; ????
F4B3: 13 ; ????
F4B4: 0F ; ????
F4B5: 04 ; ????
F4B6: 0C ; ????
F4B7: 07 ; ????
F4B8: 0F ; ????
F4B9: 07 ; ????
F4BA: 0C ; ????
F4BB: 13 ; ????
F4BC: 0F ; ????
F4BD: 04 ; ????
F4BE: 0C ; ????
F4BF: 09 0F           ORA     #$0F                  
F4C1: 07 ; ????
F4C2: 0C ; ????
F4C3: 13 ; ????
F4C4: 0F ; ????
F4C5: 04 ; ????
F4C6: 0C ; ????
F4C7: 07 ; ????
F4C8: 0F ; ????
F4C9: 07 ; ????
F4CA: 0C ; ????
F4CB: 13 ; ????
F4CC: 0F ; ????
F4CD: 04 ; ????
F4CE: 04 ; ????
F4CF: 0F ; ????
F4D0: 0F ; ????
F4D1: 07 ; ????
F4D2: 0C ; ????
F4D3: 13 ; ????
F4D4: 0F ; ????
F4D5: 04 ; ????
F4D6: 0C ; ????
F4D7: 04 ; ????
F4D8: 0F ; ????
F4D9: 0E 0C 03        ASL     $030C                   
F4DC: 00              BRK                         
F4DD: 01 FF           ORA     ($FF,X)               
F4DF: 0C ; ????
F4E0: 09 00           ORA     #$00                  
F4E2: 01 0C           ORA     ($0C,X)               
F4E4: 09 0F           ORA     #$0F                  
F4E6: 04 ; ????
F4E7: 0C ; ????
F4E8: 09 00           ORA     #$00                  
F4EA: 02 ; ????
F4EB: 0C ; ????
F4EC: 09 0F           ORA     #$0F                  
F4EE: 04 ; ????
F4EF: 0C ; ????
F4F0: 09 00           ORA     #$00                  
F4F2: 02 ; ????
F4F3: 0C ; ????
F4F4: 07 ; ????
F4F5: 0F ; ????
F4F6: 04 ; ????
F4F7: 0C ; ????
F4F8: 07 ; ????
F4F9: 00              BRK                         
F4FA: 02 ; ????
F4FB: 04 ; ????
F4FC: 13 ; ????
F4FD: 0F ; ????
F4FE: 04 ; ????
F4FF: 04 ; ????
F500: 13 ; ????
F501: 00              BRK                         
F502: 02 ; ????
F503: FF ; ????
F504: 0C ; ????
F505: 09 00           ORA     #$00                  
F507: 01 0C           ORA     ($0C,X)               
F509: 09 0F           ORA     #$0F                  
F50B: 05 0C           ORA     $0C                   
F50D: 09 00           ORA     #$00                  
F50F: 02 ; ????
F510: 0C ; ????
F511: 09 0F           ORA     #$0F                  
F513: 05 0C           ORA     $0C                   
F515: 09 00           ORA     #$00                  
F517: 02 ; ????
F518: 0C ; ????
F519: 0B ; ????
F51A: 0F ; ????
F51B: 05 0C           ORA     $0C                   
F51D: 0B ; ????
F51E: 00              BRK                         
F51F: 02 ; ????
F520: 0C ; ????
F521: 0B ; ????
F522: 0F ; ????
F523: 05 0C           ORA     $0C                   
F525: 0B ; ????
F526: 00              BRK                         
F527: 02 ; ????
F528: 0C ; ????
F529: 0E 0F 05        ASL     $050F                   
F52C: 0C ; ????
F52D: 0E 00 02        ASL     $0200                   
F530: 0C ; ????
F531: 0E 0F 05        ASL     $050F                   
F534: 0C ; ????
F535: 0E 00 02        ASL     $0200                   
F538: 0C ; ????
F539: 0E 0F 05        ASL     $050F                   
F53C: 0C ; ????
F53D: 0E 00 01        ASL     $0100                   
F540: FF ; ????
F541: 0E 0A 00        ASL     $000A                   
F544: 01 0E           ORA     ($0E,X)               
F546: 0A              ASL     A                   
F547: 0F ; ????
F548: 02 ; ????
F549: 0E 0A 0E        ASL     $0E0A                   
F54C: 02 ; ????
F54D: 0E 0A 0D        ASL     $0D0A                   
F550: 02 ; ????
F551: 0E 0A 0C        ASL     $0C0A                   
F554: 02 ; ????
F555: 0E 0A 0B        ASL     $0B0A                   
F558: 02 ; ????
F559: 0E 0A 0A        ASL     $0A0A                   
F55C: 02 ; ????
F55D: 0E 0A 09        ASL     $090A                   
F560: 02 ; ????
F561: 0E 0A 08        ASL     $080A                   
F564: 02 ; ????
F565: 0E 0A 07        ASL     $070A                   
F568: 02 ; ????
F569: 0E 0A 06        ASL     $060A                   
F56C: 02 ; ????
F56D: 0E 0A 05        ASL     $050A                   
F570: 02 ; ????
F571: 0E 0A 04        ASL     $040A                   
F574: 02 ; ????
F575: 0E 0A 03        ASL     $030A                   
F578: 02 ; ????
F579: 0E 0A 02        ASL     $020A                   
F57C: 02 ; ????
F57D: 0E 0A 01        ASL     $010A                   
F580: 02 ; ????
F581: 0E 0A 00        ASL     $000A                   
F584: 01 FF           ORA     ($FF,X)               
F586: 04 ; ????
F587: 1F ; ????
F588: 00              BRK                         
F589: 01 04           ORA     ($04,X)               
F58B: 1F ; ????
F58C: 0F ; ????
F58D: 14 ; ????
F58E: 0C ; ????
F58F: 08              PHP                         
F590: 0F ; ????
F591: 15 0C           ORA     $0C,X                 
F593: 08              PHP                         
F594: 00              BRK                         
F595: 01 0C           ORA     ($0C,X)               
F597: 08              PHP                         
F598: 0F ; ????
F599: 14 ; ????
F59A: 0C ; ????
F59B: 09 0F           ORA     #$0F                  
F59D: 0A              ASL     A                   
F59E: 04 ; ????
F59F: 1F ; ????
F5A0: 0F ; ????
F5A1: 0A              ASL     A                   
F5A2: 0C ; ????
F5A3: 09 0F           ORA     #$0F                  
F5A5: 14 ; ????
F5A6: 0C ; ????
F5A7: 07 ; ????
F5A8: 0F ; ????
F5A9: 15 0C           ORA     $0C,X                 
F5AB: 07 ; ????
F5AC: 00              BRK                         
F5AD: 01 0C           ORA     ($0C,X)               
F5AF: 07 ; ????
F5B0: 0F ; ????
F5B1: 14 ; ????
F5B2: 0C ; ????
F5B3: 08              PHP                         
F5B4: 0F ; ????
F5B5: 0A              ASL     A                   
F5B6: 0C ; ????
F5B7: 09 0F           ORA     #$0F                  
F5B9: 0A              ASL     A                   
F5BA: 0C ; ????
F5BB: 08              PHP                         
F5BC: 0F ; ????
F5BD: 14 ; ????
F5BE: 0C ; ????
F5BF: 06 0F           ASL     $0F                   
F5C1: 15 0C           ORA     $0C,X                 
F5C3: 06 00           ASL     $00                   
F5C5: 01 0C           ORA     ($0C,X)               
F5C7: 06 0F           ASL     $0F                   
F5C9: 14 ; ????
F5CA: 0C ; ????
F5CB: 08              PHP                         
F5CC: 0F ; ????
F5CD: 0A              ASL     A                   
F5CE: 0C ; ????
F5CF: 06 0F           ASL     $0F                   
F5D1: 0A              ASL     A                   
F5D2: 04 ; ????
F5D3: 13 ; ????
F5D4: 0F ; ????
F5D5: 0A              ASL     A                   
F5D6: 0C ; ????
F5D7: 08              PHP                         
F5D8: 0F ; ????
F5D9: 0A              ASL     A                   
F5DA: 0C ; ????
F5DB: 07 ; ????
F5DC: 0F ; ????
F5DD: 0A              ASL     A                   
F5DE: 0C ; ????
F5DF: 08              PHP                         
F5E0: 0F ; ????
F5E1: 0B ; ????
F5E2: 0C ; ????
F5E3: 08              PHP                         
F5E4: 00              BRK                         
F5E5: 01 0C           ORA     ($0C,X)               
F5E7: 08              PHP                         
F5E8: 0F ; ????
F5E9: 20 0C 08        JSR     $080C                   
F5EC: 00              BRK                         
F5ED: 01 FF           ORA     ($FF,X)               
F5EF: 0C ; ????
F5F0: 04 ; ????
F5F1: 00              BRK                         
F5F2: 01 0C           ORA     ($0C,X)               
F5F4: 04 ; ????
F5F5: 09 03           ORA     #$03                  
F5F7: 04 ; ????
F5F8: 0F ; ????
F5F9: 09 03           ORA     #$03                  
F5FB: 04 ; ????
F5FC: 10 09           BPL     $F607                   
F5FE: 03 ; ????
F5FF: 04 ; ????
F600: 11 09           ORA     ($09),Y               
F602: 03 ; ????
F603: 04 ; ????
F604: 12 ; ????
F605: 09 03           ORA     #$03                  
F607: 04 ; ????
F608: 13 ; ????
F609: 09 03           ORA     #$03                  
F60B: 0C ; ????
F60C: 06 09           ASL     $09                   
F60E: 03 ; ????
F60F: 04 ; ????
F610: 15 09           ORA     $09,X                 
F612: 03 ; ????
F613: 0C ; ????
F614: 07 ; ????
F615: 09 03           ORA     #$03                  
F617: 04 ; ????
F618: 18              CLC                         
F619: 09 03           ORA     #$03                  
F61B: 04 ; ????
F61C: 1A ; ????
F61D: 09 03           ORA     #$03                  
F61F: 04 ; ????
F620: 1B ; ????
F621: 09 03           ORA     #$03                  
F623: 04 ; ????
F624: 1D 09 03        ORA     $0309,X                 
F627: 04 ; ????
F628: 1D 00 01        ORA     $0100,X                 
F62B: FF ; ????
F62C: 08              PHP                         
F62D: 00              BRK                         
F62E: 00              BRK                         
F62F: 01 08           ORA     ($08,X)               
F631: 00              BRK                         
F632: 0F ; ????
F633: 01 08           ORA     ($08,X)               
F635: 00              BRK                         
F636: 00              BRK                         
F637: 04 ; ????
F638: 08              PHP                         
F639: 00              BRK                         
F63A: 0F ; ????
F63B: 01 08           ORA     ($08,X)               
F63D: 00              BRK                         
F63E: 00              BRK                         
F63F: 04 ; ????
F640: 08              PHP                         
F641: 00              BRK                         
F642: 0F ; ????
F643: 01 08           ORA     ($08,X)               
F645: 00              BRK                         
F646: 00              BRK                         
F647: 01 FF           ORA     ($FF,X)               
F649: 0C ; ????
F64A: 13 ; ????
F64B: 00              BRK                         
F64C: 01 0C           ORA     ($0C,X)               
F64E: 13 ; ????
F64F: 09 05           ORA     #$05                  
F651: 0C ; ????
F652: 13 ; ????
F653: 00              BRK                         
F654: 02 ; ????
F655: 0C ; ????
F656: 10 09           BPL     $F661                   
F658: 05 0C           ORA     $0C                   
F65A: 10 00           BPL     $F65C                   
F65C: 02 ; ????
F65D: 0C ; ????
F65E: 13 ; ????
F65F: 09 05           ORA     #$05                  
F661: 0C ; ????
F662: 13 ; ????
F663: 00              BRK                         
F664: 02 ; ????
F665: 0C ; ????
F666: 10 09           BPL     $F671                   
F668: 05 0C           ORA     $0C                   
F66A: 10 00           BPL     $F66C                   
F66C: 01 FF           ORA     ($FF,X)               
F66E: 04 ; ????
F66F: 0F ; ????
F670: 00              BRK                         
F671: 01 04           ORA     ($04,X)               
F673: 0F ; ????
F674: 09 01           ORA     #$01                  
F676: 0C ; ????
F677: 04 ; ????
F678: 09 01           ORA     #$01                  
F67A: 0C ; ????
F67B: 0C ; ????
F67C: 09 01           ORA     #$01                  
F67E: 04 ; ????
F67F: 0B ; ????
F680: 09 01           ORA     #$01                  
F682: 04 ; ????
F683: 0A              ASL     A                   
F684: 09 01           ORA     #$01                  
F686: 04 ; ????
F687: 09 09           ORA     #$09                  
F689: 01 0C           ORA     ($0C,X)               
F68B: 02 ; ????
F68C: 09 01           ORA     #$01                  
F68E: 04 ; ????
F68F: 09 09           ORA     #$09                  
F691: 01 04           ORA     ($04,X)               
F693: 09 00           ORA     #$00                  
F695: 01 FF           ORA     ($FF,X)               
F697: 0A              ASL     A                   
F698: 0F ; ????
F699: 00              BRK                         
F69A: 01 0A           ORA     ($0A,X)               
F69C: 0F ; ????
F69D: 0F ; ????
F69E: 0A              ASL     A                   
F69F: 0A              ASL     A                   
F6A0: 0E 0E 01        ASL     $010E                   
F6A3: 0A              ASL     A                   
F6A4: 0D 0D 01        ORA     $010D                   
F6A7: 0A              ASL     A                   
F6A8: 0C ; ????
F6A9: 0C ; ????
F6AA: 02 ; ????
F6AB: 0A              ASL     A                   
F6AC: 0A              ASL     A                   
F6AD: 0A              ASL     A                   
F6AE: 02 ; ????
F6AF: 0A              ASL     A                   
F6B0: 08              PHP                         
F6B1: 08              PHP                         
F6B2: 02 ; ????
F6B3: 0A              ASL     A                   
F6B4: 06 06           ASL     $06                   
F6B6: 02 ; ????
F6B7: 0A              ASL     A                   
F6B8: 04 ; ????
F6B9: 04 ; ????
F6BA: 02 ; ????
F6BB: 0A              ASL     A                   
F6BC: 02 ; ????
F6BD: 00              BRK                         
F6BE: 03 ; ????
F6BF: FF ; ????
F6C0: 06 0D           ASL     $0D                   
F6C2: 00              BRK                         
F6C3: 01 06           ORA     ($06,X)               
F6C5: 0D 01 02        ORA     $0201                   
F6C8: 06 0D           ASL     $0D                   
F6CA: 03 ; ????
F6CB: 02 ; ????
F6CC: 06 0D           ASL     $0D                   
F6CE: 05 02           ORA     $02                   
F6D0: 06 0D           ASL     $0D                   
F6D2: 0C ; ????
F6D3: 02 ; ????
F6D4: 06 0D           ASL     $0D                   
F6D6: 0E 02 06        ASL     $0602                   
F6D9: 0D 00 02        ORA     $0200                   
F6DC: FF ; ????
F6DD: 04 ; ????
F6DE: 1F ; ????
F6DF: 00              BRK                         
F6E0: 01 04           ORA     ($04,X)               
F6E2: 1F ; ????
F6E3: 0F ; ????
F6E4: 1E 0C 08        ASL     $080C,X                 
F6E7: 0F ; ????
F6E8: 0F ; ????
F6E9: 0C ; ????
F6EA: 09 0F           ORA     #$0F                  
F6EC: 08              PHP                         
F6ED: 04 ; ????
F6EE: 1F ; ????
F6EF: 0F ; ????
F6F0: 08              PHP                         
F6F1: 0C ; ????
F6F2: 0B ; ????
F6F3: 0F ; ????
F6F4: 1E 0C 07        ASL     $070C,X                 
F6F7: 0F ; ????
F6F8: 0F ; ????
F6F9: 0C ; ????
F6FA: 08              PHP                         
F6FB: 0F ; ????
F6FC: 08              PHP                         
F6FD: 0C ; ????
F6FE: 09 0F           ORA     #$0F                  
F700: 08              PHP                         
F701: 04 ; ????
F702: 1F ; ????
F703: 0F ; ????
F704: 0F ; ????
F705: 0C ; ????
F706: 08              PHP                         
F707: 0F ; ????
F708: 0F ; ????
F709: 0C ; ????
F70A: 07 ; ????
F70B: 0F ; ????
F70C: 0F ; ????
F70D: 0C ; ????
F70E: 08              PHP                         
F70F: 0F ; ????
F710: 0F ; ????
F711: 04 ; ????
F712: 13 ; ????
F713: 0F ; ????
F714: 0F ; ????
F715: 0C ; ????
F716: 08              PHP                         
F717: 0F ; ????
F718: 0F ; ????
F719: 04 ; ????
F71A: 13 ; ????
F71B: 0F ; ????
F71C: 28              PLP                         
F71D: 04 ; ????
F71E: 11 00           ORA     ($00),Y               
F720: 01 FF           ORA     ($FF,X)               
F722: A9 00           LDA     #$00                  
F724: A0 01           LDY     #$01                  
F726: 20 2B F3        JSR     $F32B                   
F729: 20 63 F0        JSR     $F063                   
F72C: 60              RTS                         
F72D: 0C ; ????
F72E: 1D 00 01        ORA     $0100,X                 
F731: 0C ; ????
F732: 1D 02 07        ORA     $0702,X                 
F735: 0C ; ????
F736: 1D 00 01        ORA     $0100,X                 
F739: 0C ; ????
F73A: 1D 02 07        ORA     $0702,X                 
F73D: 0C ; ????
F73E: 1D 00 01        ORA     $0100,X                 
F741: 0C ; ????
F742: 1B ; ????
F743: 02 ; ????
F744: 07 ; ????
F745: 0C ; ????
F746: 1B ; ????
F747: 00              BRK                         
F748: 01 0C           ORA     ($0C,X)               
F74A: 1B ; ????
F74B: 02 ; ????
F74C: 07 ; ????
F74D: 0C ; ????
F74E: 1B ; ????
F74F: 00              BRK                         
F750: 01 0C           ORA     ($0C,X)               
F752: 1A ; ????
F753: 02 ; ????
F754: 07 ; ????
F755: 0C ; ????
F756: 1A ; ????
F757: 00              BRK                         
F758: 01 0C           ORA     ($0C,X)               
F75A: 1A ; ????
F75B: 02 ; ????
F75C: 07 ; ????
F75D: 0C ; ????
F75E: 1A ; ????
F75F: 00              BRK                         
F760: 01 0C           ORA     ($0C,X)               
F762: 18              CLC                         
F763: 02 ; ????
F764: 07 ; ????
F765: 0C ; ????
F766: 18              CLC                         
F767: 00              BRK                         
F768: 01 0C           ORA     ($0C,X)               
F76A: 18              CLC                         
F76B: 02 ; ????
F76C: 07 ; ????
F76D: 0C ; ????
F76E: 18              CLC                         
F76F: 00              BRK                         
F770: 01 0C           ORA     ($0C,X)               
F772: 17 ; ????
F773: 02 ; ????
F774: 10 0C           BPL     $F782                   
F776: 1F ; ????
F777: 02 ; ????
F778: 10 0C           BPL     $F786                   
F77A: 17 ; ????
F77B: 02 ; ????
F77C: 10 0C           BPL     $F78A                   
F77E: 1F ; ????
F77F: 02 ; ????
F780: 10 0C           BPL     $F78E                   
F782: 1A ; ????
F783: 02 ; ????
F784: 07 ; ????
F785: 0C ; ????
F786: 13 ; ????
F787: 02 ; ????
F788: 07 ; ????
F789: 0C ; ????
F78A: 13 ; ????
F78B: 00              BRK                         
F78C: 01 0C           ORA     ($0C,X)               
F78E: 14 ; ????
F78F: 02 ; ????
F790: 07 ; ????
F791: 0C ; ????
F792: 17 ; ????
F793: 02 ; ????
F794: 07 ; ????
F795: 0C ; ????
F796: 17 ; ????
F797: 00              BRK                         
F798: 01 0C           ORA     ($0C,X)               
F79A: 1A ; ????
F79B: 02 ; ????
F79C: 07 ; ????
F79D: 0C ; ????
F79E: 1A ; ????
F79F: 00              BRK                         
F7A0: 01 0C           ORA     ($0C,X)               
F7A2: 1B ; ????
F7A3: 02 ; ????
F7A4: 07 ; ????
F7A5: 0C ; ????
F7A6: 1B ; ????
F7A7: 00              BRK                         
F7A8: 01 0C           ORA     ($0C,X)               
F7AA: 1A ; ????
F7AB: 02 ; ????
F7AC: 07 ; ????
F7AD: 0C ; ????
F7AE: 1A ; ????
F7AF: 00              BRK                         
F7B0: 01 0C           ORA     ($0C,X)               
F7B2: 1B ; ????
F7B3: 02 ; ????
F7B4: 07 ; ????
F7B5: 0C ; ????
F7B6: 1B ; ????
F7B7: 00              BRK                         
F7B8: 01 0C           ORA     ($0C,X)               
F7BA: 1A ; ????
F7BB: 02 ; ????
F7BC: 10 0C           BPL     $F7CA                   
F7BE: 13 ; ????
F7BF: 02 ; ????
F7C0: 10 0C           BPL     $F7CE                   
F7C2: 1A ; ????
F7C3: 02 ; ????
F7C4: 10 0C           BPL     $F7D2                   
F7C6: 13 ; ????
F7C7: 02 ; ????
F7C8: 10 0C           BPL     $F7D6                   
F7CA: 1A ; ????
F7CB: 02 ; ????
F7CC: 10 0C           BPL     $F7DA                   
F7CE: 0F ; ????
F7CF: 02 ; ????
F7D0: 10 0C           BPL     $F7DE                   
F7D2: 1A ; ????
F7D3: 02 ; ????
F7D4: 10 0C           BPL     $F7E2                   
F7D6: 0F ; ????
F7D7: 02 ; ????
F7D8: 10 0C           BPL     $F7E6                   
F7DA: 1D 02 10        ORA     $1002,X                 
F7DD: 0C ; ????
F7DE: 11 02           ORA     ($02),Y               
F7E0: 10 0C           BPL     $F7EE                   
F7E2: 1F ; ????
F7E3: 02 ; ????
F7E4: 10 0C           BPL     $F7F2                   
F7E6: 13 ; ????
F7E7: 02 ; ????
F7E8: 10 0C           BPL     $F7F6                   
F7EA: 1D 02 10        ORA     $1002,X                 
F7ED: 0C ; ????
F7EE: 11 02           ORA     ($02),Y               
F7F0: 10 0C           BPL     $F7FE                   
F7F2: 1F ; ????
F7F3: 02 ; ????
F7F4: 10 0C           BPL     $F802                   
F7F6: 13 ; ????
F7F7: 02 ; ????
F7F8: 10 0C           BPL     $F806                   
F7FA: 13 ; ????
F7FB: 00              BRK                         
F7FC: 01 FF           ORA     ($FF,X)               
F7FE: 00              BRK                         
F7FF: 00              BRK                         
```
