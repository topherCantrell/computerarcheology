![Burger Time](A2600BT.jpg)

# Burger Time Bank 6

>>> cpu 6502

>>> binary F000:btBank6.bin

>>> memoryTable hard 

[Hardware Info](../Stella.md)

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

```code
F000: 08 04 02 01 

F004: 20 0B F0        JSR     $F00B               ; {}
F007: 20 63 F0        JSR     $F063               ; {}
F00A: 60              RTS                         
F00B: 20 0D F3        JSR     $F30D               ; {}
F00E: 90 52           BCC     $F062               ; {}
F010: AD 58 F9        LDA     $F958               
F013: D0 08           BNE     $F01D               ; {}
F015: A9 0C           LDA     #$0C                
F017: A0 01           LDY     #$01                
F019: 20 3F F3        JSR     $F33F               ; {}
F01C: 60              RTS                         
F01D: AD 56 F9        LDA     $F956               
F020: 29 01           AND     #$01                
F022: D0 3E           BNE     $F062               ; {}
F024: 8D 3F F8        STA     $F83F               
F027: A9 0A           LDA     #$0A                
F029: A0 01           LDY     #$01                
F02B: 20 3F F3        JSR     $F33F               ; {}
F02E: AD 48 F9        LDA     $F948               
F031: C9 FF           CMP     #$FF                
F033: D0 02           BNE     $F037               ; {}
F035: A9 00           LDA     #$00                
F037: 8D 39 F8        STA     $F839               
F03A: A5 BD           LDA     $BD                 ; {ram.mBD}
F03C: 8D 3A F8        STA     $F83A               
F03F: A5 C2           LDA     $C2                 ; {ram.mC2}
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
F063: 20 0E F2        JSR     $F20E               ; {}
F066: AD 56 F9        LDA     $F956               
F069: 29 01           AND     #$01                
F06B: D0 03           BNE     $F070               ; {}
F06D: 4C 20 F1        JMP     $F120               ; {}
F070: AD 3E F9        LDA     $F93E               
F073: 38              SEC                         
F074: E9 01           SBC     #$01                
F076: 8D 3E F8        STA     $F83E               
F079: F0 4D           BEQ     $F0C8               ; {}
F07B: A5 DE           LDA     $DE                 ; {ram.mDE}
F07D: 29 01           AND     #$01                
F07F: F0 53           BEQ     $F0D4               ; {}
F081: A2 03           LDX     #$03                
F083: A5 C7           LDA     $C7                 ; {ram.mC7}
F085: 6A              ROR     A                   
F086: 90 16           BCC     $F09E               ; {}
F088: AD 40 F9        LDA     $F940               
F08B: 3D 00 F0        AND     $F000,X             ; {}
F08E: D0 05           BNE     $F095               ; {}
F090: A9 BE           LDA     #$BE                
F092: 8D 41 F8        STA     $F841               
F095: AD 40 F9        LDA     $F940               
F098: 1D 00 F0        ORA     $F000,X             ; {}
F09B: 8D 40 F8        STA     $F840               
F09E: 46 C7           LSR     $C7                 ; {ram.mC7}
F0A0: CA              DEX                         
F0A1: 10 E0           BPL     $F083               ; {}
F0A3: A5 CC           LDA     $CC                 ; {ram.mCC}
F0A5: F0 07           BEQ     $F0AE               ; {}
F0A7: A9 0B           LDA     #$0B                
F0A9: A0 01           LDY     #$01                
F0AB: 20 3F F3        JSR     $F33F               ; {}
F0AE: AD 3A F9        LDA     $F93A               
F0B1: 85 BD           STA     $BD                 ; {ram.mBD}
F0B3: AD 3B F9        LDA     $F93B               
F0B6: 85 C2           STA     $C2                 ; {ram.mC2}
F0B8: AD 39 F9        LDA     $F939               
F0BB: 4A              LSR     A                   
F0BC: 8D 4C F8        STA     $F84C               
F0BF: A5 DF           LDA     $DF                 ; {ram.mDF}
F0C1: 29 F0           AND     #$F0                
F0C3: 09 03           ORA     #$03                
F0C5: 85 DF           STA     $DF                 ; {ram.mDF}
F0C7: 60              RTS                         
F0C8: AD 56 F9        LDA     $F956               
F0CB: 29 FE           AND     #$FE                
F0CD: 8D 56 F8        STA     $F856               
F0D0: 4C AE F0        JMP     $F0AE               ; {}
F0D3: 60              RTS                         
F0D4: 20 20 F1        JSR     $F120               ; {}
F0D7: AD 56 F9        LDA     $F956               
F0DA: 29 40           AND     #$40                
F0DC: D0 26           BNE     $F104               ; {}
F0DE: A9 04           LDA     #$04                
F0E0: 8D 4C F8        STA     $F84C               
F0E3: A9 08           LDA     #$08                
F0E5: 85 C7           STA     $C7                 ; {ram.mC7}
F0E7: A5 DF           LDA     $DF                 ; {ram.mDF}
F0E9: 29 F0           AND     #$F0                
F0EB: 09 03           ORA     #$03                
F0ED: 85 DF           STA     $DF                 ; {ram.mDF}
F0EF: AD 39 F9        LDA     $F939               
F0F2: F0 11           BEQ     $F105               ; {}
F0F4: C9 04           CMP     #$04                
F0F6: F0 16           BEQ     $F10E               ; {}
F0F8: C9 02           CMP     #$02                
F0FA: F0 1B           BEQ     $F117               ; {}
F0FC: AD 3B F9        LDA     $F93B               
F0FF: 18              CLC                         
F100: 65 C7           ADC     $C7                 ; {ram.mC7}
F102: 85 C2           STA     $C2                 ; {ram.mC2}
F104: 60              RTS                         
F105: AD 3A F9        LDA     $F93A               
F108: 18              CLC                         
F109: 65 C7           ADC     $C7                 ; {ram.mC7}
F10B: 85 BD           STA     $BD                 ; {ram.mBD}
F10D: 60              RTS                         
F10E: AD 3A F9        LDA     $F93A               
F111: 38              SEC                         
F112: E5 C7           SBC     $C7                 ; {ram.mC7}
F114: 85 BD           STA     $BD                 ; {ram.mBD}
F116: 60              RTS                         
F117: AD 3B F9        LDA     $F93B               
F11A: 38              SEC                         
F11B: E5 C7           SBC     $C7                 ; {ram.mC7}
F11D: 85 C2           STA     $C2                 ; {ram.mC2}
F11F: 60              RTS                         
F120: AD 40 F9        LDA     $F940               
F123: F0 10           BEQ     $F135               ; {}
F125: AD 41 F9        LDA     $F941               
F128: 38              SEC                         
F129: E9 01           SBC     #$01                
F12B: 8D 41 F8        STA     $F841               
F12E: D0 05           BNE     $F135               ; {}
F130: A9 00           LDA     #$00                
F132: 8D 40 F8        STA     $F840               
F135: A5 CC           LDA     $CC                 ; {ram.mCC}
F137: D0 0C           BNE     $F145               ; {}
F139: A5 DE           LDA     $DE                 ; {ram.mDE}
F13B: D0 05           BNE     $F142               ; {}
F13D: A9 00           LDA     #$00                
F13F: 8D 46 F8        STA     $F846               
F142: 4C D0 F1        JMP     $F1D0               ; {}
F145: A2 03           LDX     #$03                
F147: A5 C7           LDA     $C7                 ; {ram.mC7}
F149: 6A              ROR     A                   
F14A: 90 61           BCC     $F1AD               ; {}
F14C: AD 40 F9        LDA     $F940               
F14F: 3D 00 F0        AND     $F000,X             ; {}
F152: D0 59           BNE     $F1AD               ; {}
F154: AD 36 F9        LDA     $F936               
F157: 3D 00 F0        AND     $F000,X             ; {}
F15A: D0 51           BNE     $F1AD               ; {}
F15C: AD 46 F9        LDA     $F946               
F15F: 18              CLC                         
F160: 69 01           ADC     #$01                
F162: 8D 46 F8        STA     $F846               
F165: C9 08           CMP     #$08                
F167: D0 67           BNE     $F1D0               ; {}
F169: A9 0F           LDA     #$0F                
F16B: 8D 40 F8        STA     $F840               
F16E: 8D 36 F8        STA     $F836               
F171: AD 56 F9        LDA     $F956               
F174: 09 40           ORA     #$40                
F176: 8D 56 F8        STA     $F856               
F179: A5 DF           LDA     $DF                 ; {ram.mDF}
F17B: 29 0F           AND     #$0F                
F17D: 09 10           ORA     #$10                
F17F: 85 DF           STA     $DF                 ; {ram.mDF}
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
F1A1: D0 0F           BNE     $F1B2               ; {}
F1A3: AD 56 F9        LDA     $F956               
F1A6: 09 80           ORA     #$80                
F1A8: 8D 56 F8        STA     $F856               
F1AB: D0 05           BNE     $F1B2               ; {}
F1AD: 46 C7           LSR     $C7                 ; {ram.mC7}
F1AF: CA              DEX                         
F1B0: 10 95           BPL     $F147               ; {}
F1B2: AD 56 F9        LDA     $F956               
F1B5: 29 40           AND     #$40                
F1B7: F0 17           BEQ     $F1D0               ; {}
F1B9: AD 56 F9        LDA     $F956               
F1BC: 29 20           AND     #$20                
F1BE: D0 0F           BNE     $F1CF               ; {}
F1C0: A9 01           LDA     #$01                
F1C2: A0 01           LDY     #$01                
F1C4: 20 3F F3        JSR     $F33F               ; {}
F1C7: AD 56 F9        LDA     $F956               
F1CA: 09 20           ORA     #$20                
F1CC: 8D 56 F8        STA     $F856               
F1CF: 60              RTS                         
F1D0: AD 86 F9        LDA     $F986               
F1D3: C9 10           CMP     #$10                
F1D5: D0 F8           BNE     $F1CF               ; {}
F1D7: A9 FF           LDA     #$FF                
F1D9: 8D 40 F8        STA     $F840               
F1DC: 8D 36 F8        STA     $F836               
F1DF: AD 56 F9        LDA     $F956               
F1E2: 29 10           AND     #$10                
F1E4: D0 E9           BNE     $F1CF               ; {}
F1E6: AD 56 F9        LDA     $F956               
F1E9: 09 10           ORA     #$10                
F1EB: 8D 56 F8        STA     $F856               
F1EE: A9 02           LDA     #$02                
F1F0: A0 01           LDY     #$01                
F1F2: 20 43 F3        JSR     $F343               ; {}
F1F5: A9 00           LDA     #$00                
F1F7: 8D 16 F8        STA     $F816               
F1FA: 8D 17 F8        STA     $F817               
F1FD: 8D 18 F8        STA     $F818               
F200: 8D 19 F8        STA     $F819               
F203: 60              RTS                         
        
F204: 07 00 01 02 02 80 40 80 40 80

F20E: A9 00           LDA     #$00                
F210: 85 C7           STA     $C7                 ; {ram.mC7}
F212: A2 03           LDX     #$03                
F214: BC 04 F2        LDY     $F204,X             ; {}
F217: B9 00 00        LDA     $0000,Y             ; {hard.CXM0P}
F21A: 3D 09 F2        AND     $F209,X             ; {}
F21D: F0 03           BEQ     $F222               ; {}
F21F: 38              SEC                         
F220: B0 01           BCS     $F223               ; {}
F222: 18              CLC                         
F223: 26 C7           ROL     $C7                 ; {ram.mC7}
F225: CA              DEX                         
F226: 10 EC           BPL     $F214               ; {}
F228: A5 C7           LDA     $C7                 ; {ram.mC7}
F22A: 85 CC           STA     $CC                 ; {ram.mCC}
F22C: AD 4B F9        LDA     $F94B               
F22F: D0 03           BNE     $F234               ; {}
F231: 4C B8 F2        JMP     $F2B8               ; {}
F234: A5 DE           LDA     $DE                 ; {ram.mDE}
F236: 29 03           AND     #$03                
F238: D0 0E           BNE     $F248               ; {}
F23A: AD 4B F9        LDA     $F94B               
F23D: 38              SEC                         
F23E: E9 01           SBC     #$01                
F240: 8D 4B F8        STA     $F84B               
F243: F0 49           BEQ     $F28E               ; {}
F245: 4C B8 F2        JMP     $F2B8               ; {}
F248: A5 DE           LDA     $DE                 ; {ram.mDE}
F24A: 29 03           AND     #$03                
F24C: C9 03           CMP     #$03                
F24E: F0 3E           BEQ     $F28E               ; {}
F250: C9 01           CMP     #$01                
F252: F0 65           BEQ     $F2B9               ; {}
F254: A5 C7           LDA     $C7                 ; {ram.mC7}
F256: 29 01           AND     #$01                
F258: F0 5E           BEQ     $F2B8               ; {}
F25A: A5 C7           LDA     $C7                 ; {ram.mC7}
F25C: 29 FE           AND     #$FE                
F25E: 85 C7           STA     $C7                 ; {ram.mC7}
F260: 85 CC           STA     $CC                 ; {ram.mCC}
F262: F8              SED                         
F263: AD 58 F9        LDA     $F958               
F266: 18              CLC                         
F267: 69 01           ADC     #$01                
F269: 8D 58 F8        STA     $F858               
F26C: D8              CLD                         
F26D: A5 C7           LDA     $C7                 ; {ram.mC7}
F26F: 85 D6           STA     $D6                 ; {ram.mD6}
F271: A9 05           LDA     #$05                
F273: A0 01           LDY     #$01                
F275: 86 D7           STX     $D7                 ; {ram.mD7}
F277: 20 43 F3        JSR     $F343               ; {}
F27A: A5 D6           LDA     $D6                 ; {ram.mD6}
F27C: 85 CC           STA     $CC                 ; {ram.mCC}
F27E: 85 C7           STA     $C7                 ; {ram.mC7}
F280: A9 00           LDA     #$00                
F282: A2 05           LDX     #$05                
F284: 20 65 F3        JSR     $F365               ; {}
F287: A9 00           LDA     #$00                
F289: 8D 4B F8        STA     $F84B               
F28C: A6 D7           LDX     $D7                 ; {ram.mD7}
F28E: A5 C7           LDA     $C7                 ; {ram.mC7}
F290: 29 FE           AND     #$FE                
F292: 85 C7           STA     $C7                 ; {ram.mC7}
F294: A5 DF           LDA     $DF                 ; {ram.mDF}
F296: 29 0F           AND     #$0F                
F298: 0D 45 F9        ORA     $F945               
F29B: 85 DF           STA     $DF                 ; {ram.mDF}
F29D: AD 44 F9        LDA     $F944               
F2A0: 8D 4D F8        STA     $F84D               
F2A3: AD 42 F9        LDA     $F942               
F2A6: 85 BE           STA     $BE                 ; {ram.mBE}
F2A8: AD 43 F9        LDA     $F943               
F2AB: 85 C3           STA     $C3                 ; {ram.mC3}
F2AD: A2 B5           LDX     #$B5                
F2AF: A5 BE           LDA     $BE                 ; {ram.mBE}
F2B1: 20 8D F3        JSR     $F38D               ; {}
F2B4: A5 C7           LDA     $C7                 ; {ram.mC7}
F2B6: 85 CC           STA     $CC                 ; {ram.mCC}
F2B8: 60              RTS                         
F2B9: A5 DF           LDA     $DF                 ; {ram.mDF}
F2BB: 29 F0           AND     #$F0                
F2BD: 8D 45 F8        STA     $F845               
F2C0: AD 4D F9        LDA     $F94D               
F2C3: 8D 44 F8        STA     $F844               
F2C6: A5 BE           LDA     $BE                 ; {ram.mBE}
F2C8: 8D 42 F8        STA     $F842               
F2CB: A5 C3           LDA     $C3                 ; {ram.mC3}
F2CD: 8D 43 F8        STA     $F843               
F2D0: A5 DF           LDA     $DF                 ; {ram.mDF}
F2D2: 29 0F           AND     #$0F                
F2D4: AE 59 F9        LDX     $F959               
F2D7: 1D FB F2        ORA     $F2FB,X             ; {}
F2DA: 85 DF           STA     $DF                 ; {ram.mDF}
F2DC: BD FF F2        LDA     $F2FF,X             ; {}
F2DF: 8D 4D F8        STA     $F84D               
F2E2: AE 55 F9        LDX     $F955               
F2E5: BD 03 F3        LDA     $F303,X             ; {}
F2E8: 85 BE           STA     $BE                 ; {ram.mBE}
F2EA: BD 08 F3        LDA     $F308,X             ; {}
F2ED: 85 C3           STA     $C3                 ; {ram.mC3}
F2EF: A2 B5           LDX     #$B5                
F2F1: A5 BE           LDA     $BE                 ; {ram.mBE}
F2F3: 20 8D F3        JSR     $F38D               ; {}
F2F6: A5 C7           LDA     $C7                 ; {ram.mC7}
F2F8: 85 CC           STA     $CC                 ; {ram.mCC}
F2FA: 60              RTS                         

F2FB: 30 30 30 30 05 06 07 07 56 41 50 50 4C 14 1E 14
F30B: 28 14

F30D: A5 3C           LDA     $3C                 ; {hard.INPT4}
F30F: 30 13           BMI     $F324               ; {}
F311: AD 47 F9        LDA     $F947               
F314: F0 07           BEQ     $F31D               ; {}
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
F32E: A5 80           LDA     $80                 ; {ram.m80}
F330: 29 C0           AND     #$C0                
F332: D0 09           BNE     $F33D               ; {}
F334: AD F7 F9        LDA     $F9F7               
F337: 24 80           BIT     $80                 ; {ram.m80}
F339: 10 08           BPL     $F343               ; {}
F33B: 50 02           BVC     $F33F               ; {}
F33D: 38              SEC                         
F33E: 60              RTS                         
F33F: A2 01           LDX     #$01                
F341: D0 02           BNE     $F345               ; {}
F343: A2 00           LDX     #$00                
F345: 9D 00 F8        STA     $F800,X             
F348: 98              TYA                         
F349: 9D 06 F8        STA     $F806,X             
F34C: A9 00           LDA     #$00                
F34E: 9D 04 F8        STA     $F804,X             
F351: 9D 02 F8        STA     $F802,X             
F354: A4 80           LDY     $80                 ; {ram.m80}
F356: 8A              TXA                         
F357: F0 05           BEQ     $F35E               ; {}
F359: 98              TYA                         
F35A: 09 40           ORA     #$40                
F35C: D0 03           BNE     $F361               ; {}
F35E: 98              TYA                         
F35F: 09 80           ORA     #$80                
F361: 85 80           STA     $80                 ; {ram.m80}
F363: 18              CLC                         
F364: 60              RTS                         
F365: F8              SED                         
F366: 18              CLC                         
F367: 6D 71 F9        ADC     $F971               
F36A: 8D 71 F8        STA     $F871               
F36D: 8A              TXA                         
F36E: 6D 70 F9        ADC     $F970               
F371: 8D 70 F8        STA     $F870               
F374: 90 0A           BCC     $F380               ; {}
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
F390: 85 CC           STA     $CC                 ; {ram.mCC}
F392: 68              PLA                         
F393: 4A              LSR     A                   
F394: 4A              LSR     A                   
F395: 4A              LSR     A                   
F396: 4A              LSR     A                   
F397: 85 CD           STA     $CD                 ; {ram.mCD}
F399: 18              CLC                         
F39A: 65 CC           ADC     $CC                 ; {ram.mCC}
F39C: C9 0F           CMP     #$0F                
F39E: 90 04           BCC     $F3A4               ; {}
F3A0: E9 0F           SBC     #$0F                
F3A2: E6 CD           INC     $CD                 ; {ram.mCD}
F3A4: 49 07           EOR     #$07                
F3A6: 0A              ASL     A                   
F3A7: 0A              ASL     A                   
F3A8: 0A              ASL     A                   
F3A9: 0A              ASL     A                   
F3AA: 05 CD           ORA     $CD                 ; {ram.mCD}
F3AC: 95 00           STA     $00,X               ; {hard.VSYNC}
F3AE: 60              RTS                         
F3AF: A2 04           LDX     #$04                
F3B1: 85 02           STA     $02                 ; {hard.WSYNC}
F3B3: B5 B4           LDA     $B4,X               ; {ram.mB4}
F3B5: 95 20           STA     $20,X               ; {hard.HMP0}
F3B7: 29 0F           AND     #$0F                
F3B9: A8              TAY                         
F3BA: A5 80           LDA     $80                 ; {ram.m80}
F3BC: 88              DEY                         
F3BD: 10 FD           BPL     $F3BC               ; {}
F3BF: 95 10           STA     $10,X               ; {hard.RESP0}
F3C1: 85 02           STA     $02                 ; {hard.WSYNC}
F3C3: CA              DEX                         
F3C4: 10 EB           BPL     $F3B1               ; {}
F3C6: 85 02           STA     $02                 ; {hard.WSYNC}
F3C8: 85 2A           STA     $2A                 ; {hard.HMOVE}
F3CA: 60              RTS                         
F3CB: A5 BD           LDA     $BD                 ; {ram.mBD}
F3CD: A2 B4           LDX     #$B4                
F3CF: 20 8D F3        JSR     $F38D               ; {}
F3D2: 60              RTS                         
F3D3: A0 00           LDY     #$00                
F3D5: B1 DC           LDA     ($DC),Y             ; {ram.mDC}
F3D7: 30 0D           BMI     $F3E6               ; {}
F3D9: 95 15           STA     $15,X               ; {hard.AUDC0}
F3DB: C8              INY                         
F3DC: B1 DC           LDA     ($DC),Y             ; {ram.mDC}
F3DE: 95 17           STA     $17,X               ; {hard.AUDF0}
F3E0: C8              INY                         
F3E1: B1 DC           LDA     ($DC),Y             ; {ram.mDC}
F3E3: 95 19           STA     $19,X               ; {hard.AUDV0}
F3E5: 60              RTS                         
F3E6: BD 06 F9        LDA     $F906,X             
F3E9: 38              SEC                         
F3EA: E9 01           SBC     #$01                
F3EC: 9D 06 F8        STA     $F806,X             
F3EF: F0 0E           BEQ     $F3FF               ; {}
F3F1: A9 00           LDA     #$00                
F3F3: 9D 04 F8        STA     $F804,X             
F3F6: 9D 02 F8        STA     $F802,X             
F3F9: 20 50 F4        JSR     $F450               ; {}
F3FC: 4C D3 F3        JMP     $F3D3               ; {}
F3FF: A5 80           LDA     $80                 ; {ram.m80}
F401: 3D 07 F4        AND     $F407,X             ; {}
F404: 85 80           STA     $80                 ; {ram.m80}
F406: 60              RTS                         

F407: 7F BF

F409: 24 80           BIT     $80                 ; {ram.m80}
F40B: 10 05           BPL     $F412               ; {}
F40D: A2 00           LDX     #$00                
F40F: 20 1C F4        JSR     $F41C               ; {}
F412: 24 80           BIT     $80                 ; {ram.m80}
F414: 50 05           BVC     $F41B               ; {}
F416: A2 01           LDX     #$01                
F418: 20 1C F4        JSR     $F41C               ; {}
F41B: 60              RTS                         
F41C: BD 04 F9        LDA     $F904,X             
F41F: 18              CLC                         
F420: 69 01           ADC     #$01                
F422: 9D 04 F8        STA     $F804,X             
F425: 20 50 F4        JSR     $F450               ; {}
F428: BD 04 F9        LDA     $F904,X             
F42B: A0 03           LDY     #$03                
F42D: D1 DC           CMP     ($DC),Y             ; {ram.mDC}
F42F: 90 1E           BCC     $F44F               ; {}
F431: A9 00           LDA     #$00                
F433: 9D 04 F8        STA     $F804,X             
F436: BD 02 F9        LDA     $F902,X             
F439: 18              CLC                         
F43A: 69 04           ADC     #$04                
F43C: 9D 02 F8        STA     $F802,X             
F43F: A5 DC           LDA     $DC                 ; {ram.mDC}
F441: 18              CLC                         
F442: 69 04           ADC     #$04                
F444: 85 DC           STA     $DC                 ; {ram.mDC}
F446: A9 00           LDA     #$00                
F448: 65 DD           ADC     $DD                 ; {ram.mDD}
F44A: 85 DD           STA     $DD                 ; {ram.mDD}
F44C: 4C D3 F3        JMP     $F3D3               ; {}
F44F: 60              RTS                         
F450: 86 C7           STX     $C7                 ; {ram.mC7}
F452: BD 00 F9        LDA     $F900,X             
F455: 0A              ASL     A                   
F456: AA              TAX                         
F457: 86 C8           STX     $C8                 ; {ram.mC8}
F459: BD 70 F4        LDA     $F470,X             ; {}
F45C: 18              CLC                         
F45D: A6 C7           LDX     $C7                 ; {ram.mC7}
F45F: 7D 02 F9        ADC     $F902,X             
F462: 85 DC           STA     $DC                 ; {ram.mDC}
F464: A9 00           LDA     #$00                
F466: A6 C8           LDX     $C8                 ; {ram.mC8}
F468: 7D 71 F4        ADC     $F471,X             ; {}
F46B: 85 DD           STA     $DD                 ; {ram.mDD}
F46D: A6 C7           LDX     $C7                 ; {ram.mC7}
F46F: 60              RTS                         

F470: 2D F7 8A F4 DD F6 86 F5 41 F5 DF F4 04 F5 EF F5
F480: 49 F6 6E F6 2C F6 97 F6 C0 F6 0C 09 00 01 0C 09
F490: 0F 07 0C 13 0F 04 0C 07 0F 07 0C 13 0F 04 04 13
F4A0: 0F 07 0C 13 0F 04 0C 04 0F 07 0C 13 0F 04 04 13
F4B0: 0F 07 0C 13 0F 04 0C 07 0F 07 0C 13 0F 04 0C 09
F4C0: 0F 07 0C 13 0F 04 0C 07 0F 07 0C 13 0F 04 04 0F
F4D0: 0F 07 0C 13 0F 04 0C 04 0F 0E 0C 03 00 01 FF 0C
F4E0: 09 00 01 0C 09 0F 04 0C 09 00 02 0C 09 0F 04 0C
F4F0: 09 00 02 0C 07 0F 04 0C 07 00 02 04 13 0F 04 04
F500: 13 00 02 FF 0C 09 00 01 0C 09 0F 05 0C 09 00 02
F510: 0C 09 0F 05 0C 09 00 02 0C 0B 0F 05 0C 0B 00 02
F520: 0C 0B 0F 05 0C 0B 00 02 0C 0E 0F 05 0C 0E 00 02
F530: 0C 0E 0F 05 0C 0E 00 02 0C 0E 0F 05 0C 0E 00 01
F540: FF 0E 0A 00 01 0E 0A 0F 02 0E 0A 0E 02 0E 0A 0D
F550: 02 0E 0A 0C 02 0E 0A 0B 02 0E 0A 0A 02 0E 0A 09
F560: 02 0E 0A 08 02 0E 0A 07 02 0E 0A 06 02 0E 0A 05
F570: 02 0E 0A 04 02 0E 0A 03 02 0E 0A 02 02 0E 0A 01
F580: 02 0E 0A 00 01 FF 04 1F 00 01 04 1F 0F 14 0C 08
F590: 0F 15 0C 08 00 01 0C 08 0F 14 0C 09 0F 0A 04 1F
F5A0: 0F 0A 0C 09 0F 14 0C 07 0F 15 0C 07 00 01 0C 07
F5B0: 0F 14 0C 08 0F 0A 0C 09 0F 0A 0C 08 0F 14 0C 06
F5C0: 0F 15 0C 06 00 01 0C 06 0F 14 0C 08 0F 0A 0C 06
F5D0: 0F 0A 04 13 0F 0A 0C 08 0F 0A 0C 07 0F 0A 0C 08
F5E0: 0F 0B 0C 08 00 01 0C 08 0F 20 0C 08 00 01 FF 0C
F5F0: 04 00 01 0C 04 09 03 04 0F 09 03 04 10 09 03 04
F600: 11 09 03 04 12 09 03 04 13 09 03 0C 06 09 03 04
F610: 15 09 03 0C 07 09 03 04 18 09 03 04 1A 09 03 04
F620: 1B 09 03 04 1D 09 03 04 1D 00 01 FF 08 00 00 01
F630: 08 00 0F 01 08 00 00 04 08 00 0F 01 08 00 00 04
F640: 08 00 0F 01 08 00 00 01 FF 0C 13 00 01 0C 13 09
F650: 05 0C 13 00 02 0C 10 09 05 0C 10 00 02 0C 13 09
F660: 05 0C 13 00 02 0C 10 09 05 0C 10 00 01 FF 04 0F
F670: 00 01 04 0F 09 01 0C 04 09 01 0C 0C 09 01 04 0B
F680: 09 01 04 0A 09 01 04 09 09 01 0C 02 09 01 04 09
F690: 09 01 04 09 00 01 FF 0A 0F 00 01 0A 0F 0F 0A 0A
F6A0: 0E 0E 01 0A 0D 0D 01 0A 0C 0C 02 0A 0A 0A 02 0A
F6B0: 08 08 02 0A 06 06 02 0A 04 04 02 0A 02 00 03 FF
F6C0: 06 0D 00 01 06 0D 01 02 06 0D 03 02 06 0D 05 02
F6D0: 06 0D 0C 02 06 0D 0E 02 06 0D 00 02 FF 04 1F 00
F6E0: 01 04 1F 0F 1E 0C 08 0F 0F 0C 09 0F 08 04 1F 0F
F6F0: 08 0C 0B 0F 1E 0C 07 0F 0F 0C 08 0F 08 0C 09 0F
F700: 08 04 1F 0F 0F 0C 08 0F 0F 0C 07 0F 0F 0C 08 0F
F710: 0F 04 13 0F 0F 0C 08 0F 0F 04 13 0F 28 04 11 00
F720: 01 FF A9 00 A0 01 20 2B F3 20 63 F0 60 0C 1D 00
F730: 01 0C 1D 02 07 0C 1D 00 01 0C 1D 02 07 0C 1D 00
F740: 01 0C 1B 02 07 0C 1B 00 01 0C 1B 02 07 0C 1B 00
F750: 01 0C 1A 02 07 0C 1A 00 01 0C 1A 02 07 0C 1A 00
F760: 01 0C 18 02 07 0C 18 00 01 0C 18 02 07 0C 18 00
F770: 01 0C 17 02 10 0C 1F 02 10 0C 17 02 10 0C 1F 02
F780: 10 0C 1A 02 07 0C 13 02 07 0C 13 00 01 0C 14 02
F790: 07 0C 17 02 07 0C 17 00 01 0C 1A 02 07 0C 1A 00
F7A0: 01 0C 1B 02 07 0C 1B 00 01 0C 1A 02 07 0C 1A 00
F7B0: 01 0C 1B 02 07 0C 1B 00 01 0C 1A 02 10 0C 13 02
F7C0: 10 0C 1A 02 10 0C 13 02 10 0C 1A 02 10 0C 0F 02
F7D0: 10 0C 1A 02 10 0C 0F 02 10 0C 1D 02 10 0C 11 02
F7E0: 10 0C 1F 02 10 0C 13 02 10 0C 1D 02 10 0C 11 02
F7F0: 10 0C 1F 02 10 0C 13 02 10 0C 13 00 01 FF 00 00
```

