![Burger Time](A2600BT.jpg)

# Burger Time Bank 0

>>> cpu 6502

>>> binary F000:btBank0.bin

>>> memoryTable hard 

[Hardware Info](../Stella.md)

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

Bank 0 and 2 have the same data.

```code
F000: 18              CLC                         
F001: 60              RTS                         
    
F002: AD 48 F9        LDA     $F948               
F005: F0 06           BEQ     $F00D               ; {}
F007: C9 04           CMP     #$04                
F009: F0 02           BEQ     $F00D               ; {}
F00B: 18              CLC                         
F00C: 60              RTS                         

F00D: A5 BD           LDA     $BD                 ; {ram.mBD}
F00F: 4A              LSR     A                   
F010: 4A              LSR     A                   
F011: 4A              LSR     A                   
F012: 4A              LSR     A                   
F013: F0 EB           BEQ     $F000               ; {}
F015: C9 05           CMP     #$05                
F017: F0 E7           BEQ     $F000               ; {}
F019: AA              TAX                         
F01A: BD 70 F1        LDA     $F170,X             ; {}
F01D: 85 C8           STA     $C8                 ; {ram.mC8}
F01F: AA              TAX                         
F020: BD 7A F1        LDA     $F17A,X             ; {}
F023: 85 CD           STA     $CD                 ; {ram.mCD}
F025: A9 00           LDA     #$00                
F027: 85 CE           STA     $CE                 ; {ram.mCE}
F029: 85 D0           STA     $D0                 ; {ram.mD0}
F02B: BD 7E F1        LDA     $F17E,X             ; {}
F02E: 85 CF           STA     $CF                 ; {ram.mCF}
F030: A0 00           LDY     #$00                
F032: 88              DEY                         
F033: C8              INY                         
F034: CC 15 F9        CPY     $F915               
F037: F0 C7           BEQ     $F000               ; {}
F039: A9 73           LDA     #$73                
F03B: 38              SEC                         
F03C: F1 CD           SBC     ($CD),Y             ; {ram.mCD}
F03E: 38              SEC                         
F03F: E5 C2           SBC     $C2                 ; {ram.mC2}
F041: F0 06           BEQ     $F049               ; {}
F043: C9 FB           CMP     #$FB                
F045: B0 02           BCS     $F049               ; {}
F047: 90 EA           BCC     $F033               ; {}
F049: A9 00           LDA     #$00                
F04B: 85 D6           STA     $D6                 ; {ram.mD6}
F04D: A5 BD           LDA     $BD                 ; {ram.mBD}
F04F: FD 82 F1        SBC     $F182,X             ; {}
F052: 4A              LSR     A                   
F053: 4A              LSR     A                   
F054: 85 C7           STA     $C7                 ; {ram.mC7}
F056: 8A              TXA                         
F057: 0A              ASL     A                   
F058: AA              TAX                         
F059: BD 86 F1        LDA     $F186,X             ; {}
F05C: 85 CA           STA     $CA                 ; {ram.mCA}
F05E: BD 87 F1        LDA     $F187,X             ; {}
F061: 85 CB           STA     $CB                 ; {ram.mCB}
F063: 84 C9           STY     $C9                 ; {ram.mC9}
F065: A4 C7           LDY     $C7                 ; {ram.mC7}
F067: B1 CA           LDA     ($CA),Y             ; {ram.mCA}
F069: 49 FF           EOR     #$FF                
F06B: A4 C9           LDY     $C9                 ; {ram.mC9}
F06D: 31 CF           AND     ($CF),Y             ; {ram.mCF}
F06F: F0 04           BEQ     $F075               ; {}
F071: A9 01           LDA     #$01                
F073: 85 D6           STA     $D6                 ; {ram.mD6}
F075: A4 C7           LDY     $C7                 ; {ram.mC7}
F077: B1 CA           LDA     ($CA),Y             ; {ram.mCA}
F079: A4 C9           LDY     $C9                 ; {ram.mC9}
F07B: 31 CF           AND     ($CF),Y             ; {ram.mCF}
F07D: 91 CF           STA     ($CF),Y             ; {ram.mCF}
F07F: F0 0E           BEQ     $F08F               ; {}
F081: A5 D6           LDA     $D6                 ; {ram.mD6}
F083: F0 07           BEQ     $F08C               ; {}
F085: A9 08           LDA     #$08                
F087: A0 01           LDY     #$01                
F089: 20 1A F6        JSR     $F61A               ; {}
F08C: 4C 00 F0        JMP     $F000               ; {}
F08F: AD 55 F9        LDA     $F955               
F092: 0A              ASL     A                   
F093: 0A              ASL     A                   
F094: 18              CLC                         
F095: 65 C8           ADC     $C8                 ; {ram.mC8}
F097: AA              TAX                         
F098: BD 9E F1        LDA     $F19E,X             ; {}
F09B: 91 CF           STA     ($CF),Y             ; {ram.mCF}
F09D: A6 C8           LDX     $C8                 ; {ram.mC8}
F09F: 8A              TXA                         
F0A0: 0A              ASL     A                   
F0A1: 0A              ASL     A                   
F0A2: 85 D1           STA     $D1                 ; {ram.mD1}
F0A4: 98              TYA                         
F0A5: 18              CLC                         
F0A6: 65 D1           ADC     $D1                 ; {ram.mD1}
F0A8: 9D 11 F8        STA     $F811,X             
F0AB: 18              CLC                         
F0AC: 65 C8           ADC     $C8                 ; {ram.mC8}
F0AE: AA              TAX                         
F0AF: 86 D1           STX     $D1                 ; {ram.mD1}
F0B1: A9 01           LDA     #$01                
F0B3: 9D 1A F8        STA     $F81A,X             
F0B6: B1 CD           LDA     ($CD),Y             ; {ram.mCD}
F0B8: 9D 5B F8        STA     $F85B,X             
F0BB: 38              SEC                         
F0BC: E9 05           SBC     #$05                
F0BE: A4 C9           LDY     $C9                 ; {ram.mC9}
F0C0: 91 CD           STA     ($CD),Y             ; {ram.mCD}
F0C2: A2 04           LDX     #$04                
F0C4: AD 55 F9        LDA     $F955               
F0C7: 0A              ASL     A                   
F0C8: 0A              ASL     A                   
F0C9: 85 D7           STA     $D7                 ; {ram.mD7}
F0CB: 18              CLC                         
F0CC: 65 C8           ADC     $C8                 ; {ram.mC8}
F0CE: 85 D7           STA     $D7                 ; {ram.mD7}
F0D0: A4 C8           LDY     $C8                 ; {ram.mC8}
F0D2: A9 00           LDA     #$00                
F0D4: 99 16 F8        STA     $F816,Y             
F0D7: 99 2E F8        STA     $F82E,Y             
F0DA: CA              DEX                         
F0DB: 30 41           BMI     $F11E               ; {}
F0DD: A5 C2           LDA     $C2                 ; {ram.mC2}
F0DF: 38              SEC                         
F0E0: F5 C3           SBC     $C3,X               ; {ram.mC3}
F0E2: 30 F6           BMI     $F0DA               ; {}
F0E4: C9 05           CMP     #$05                
F0E6: B0 F2           BCS     $F0DA               ; {}
F0E8: B5 BE           LDA     $BE,X               ; {ram.mBE}
F0EA: A4 D7           LDY     $D7                 ; {ram.mD7}
F0EC: D9 03 F5        CMP     $F503,Y             ; {}
F0EF: 90 E9           BCC     $F0DA               ; {}
F0F1: D9 17 F5        CMP     $F517,Y             ; {}
F0F4: B0 E4           BCS     $F0DA               ; {}
F0F6: A4 C8           LDY     $C8                 ; {ram.mC8}
F0F8: B9 16 F9        LDA     $F916,Y             
F0FB: 1D B2 F1        ORA     $F1B2,X             ; {}
F0FE: 99 16 F8        STA     $F816,Y             
F101: B9 2E F9        LDA     $F92E,Y             
F104: 18              CLC                         
F105: 69 01           ADC     #$01                
F107: 99 2E F8        STA     $F82E,Y             
F10A: AD 40 F9        LDA     $F940               
F10D: 1D B2 F1        ORA     $F1B2,X             ; {}
F110: 8D 40 F8        STA     $F840               
F113: AD 36 F9        LDA     $F936               
F116: 1D B2 F1        ORA     $F1B2,X             ; {}
F119: 8D 36 F8        STA     $F836               
F11C: D0 BC           BNE     $F0DA               ; {}
F11E: A4 C8           LDY     $C8                 ; {ram.mC8}
F120: B9 2E F9        LDA     $F92E,Y             
F123: F0 0B           BEQ     $F130               ; {}
F125: A9 07           LDA     #$07                
F127: A0 01           LDY     #$01                
F129: 20 22 F6        JSR     $F622               ; {}
F12C: A9 00           LDA     #$00                
F12E: 85 D6           STA     $D6                 ; {ram.mD6}
F130: A4 D1           LDY     $D1                 ; {ram.mD1}
F132: A6 C8           LDX     $C8                 ; {ram.mC8}
F134: 20 14 F3        JSR     $F314               ; {}
F137: 90 35           BCC     $F16E               ; {}
F139: BD 2E F9        LDA     $F92E,X             
F13C: F0 25           BEQ     $F163               ; {}
F13E: AA              TAX                         
F13F: BD E9 F3        LDA     $F3E9,X             ; {}
F142: 8D 33 F8        STA     $F833               
F145: AA              TAX                         
F146: A9 00           LDA     #$00                
F148: 8D 32 F8        STA     $F832               
F14B: 8D 34 F8        STA     $F834               
F14E: 20 C4 F3        JSR     $F3C4               ; {}
F151: A6 C8           LDX     $C8                 ; {ram.mC8}
F153: A9 00           LDA     #$00                
F155: 9D 16 F8        STA     $F816,X             
F158: 9D 2E F8        STA     $F82E,X             
F15B: A9 DC           LDA     #$DC                
F15D: 8D 35 F8        STA     $F835               
F160: 4C 6E F1        JMP     $F16E               ; {}
F163: A5 D6           LDA     $D6                 ; {ram.mD6}
F165: F0 07           BEQ     $F16E               ; {}
F167: A9 08           LDA     #$08                
F169: A0 01           LDY     #$01                
F16B: 20 1A F6        JSR     $F61A               ; {}
F16E: 38              SEC                         
F16F: 60              RTS                         

F170: FF 00 00 01 01 FF 02 02 03 03 8D 92 97 9C A1 A5
F180: A9 AD 10 30 60 80 96 F1 8E F1 96 F1 8E F1 FE FD
F190: FB F7 EF DF BF 7F 7F BF DF EF F7 FB FD FE 3C 3C
F1A0: 3C 78 3C 78 3C 78 F0 3C 0F 3C 3C 3C 3C 3C 3C 3C
F1B0: 3C 1E 01 02 04 08       

F1B6: A9 00           LDA     #$00                
F1B8: 8D 1E F8        STA     $F81E               
F1BB: 8D 23 F8        STA     $F823               
F1BE: 8D 28 F8        STA     $F828               
F1C1: 8D 2D F8        STA     $F82D               
F1C4: A5 DE           LDA     $DE                 ; {ram.mDE}
F1C6: 29 0F           AND     #$0F                
F1C8: 85 C9           STA     $C9                 ; {ram.mC9}
F1CA: 29 0C           AND     #$0C                
F1CC: 4A              LSR     A                   
F1CD: 4A              LSR     A                   
F1CE: AA              TAX                         
F1CF: 86 CA           STX     $CA                 ; {ram.mCA}
F1D1: 18              CLC                         
F1D2: 65 C9           ADC     $C9                 ; {ram.mC9}
F1D4: 85 C8           STA     $C8                 ; {ram.mC8}
F1D6: A8              TAY                         
F1D7: B9 1A F9        LDA     $F91A,Y             
F1DA: D0 03           BNE     $F1DF               ; {}
F1DC: 4C 4E F4        JMP     $F44E               ; {}
F1DF: C9 01           CMP     #$01                
F1E1: F0 6D           BEQ     $F250               ; {}
F1E3: C9 02           CMP     #$02                
F1E5: D0 03           BNE     $F1EA               ; {}
F1E7: 4C CC F2        JMP     $F2CC               ; {}
F1EA: B9 8D 00        LDA     $008D,Y             ; {ram.m8D}
F1ED: 38              SEC                         
F1EE: E9 05           SBC     #$05                
F1F0: 99 8D 00        STA     $008D,Y             ; {ram.m8D}
F1F3: 20 E0 F2        JSR     $F2E0               ; {}
F1F6: D9 5B F9        CMP     $F95B,Y             
F1F9: D0 54           BNE     $F24F               ; {}
F1FB: A5 C9           LDA     $C9                 ; {ram.mC9}
F1FD: DD 11 F9        CMP     $F911,X             
F200: D0 48           BNE     $F24A               ; {}
F202: BD 2E F9        LDA     $F92E,X             
F205: F0 3C           BEQ     $F243               ; {}
F207: 86 D1           STX     $D1                 ; {ram.mD1}
F209: AA              TAX                         
F20A: BD E9 F3        LDA     $F3E9,X             ; {}
F20D: 8D 33 F8        STA     $F833               
F210: AA              TAX                         
F211: A9 00           LDA     #$00                
F213: 8D 32 F8        STA     $F832               
F216: 8D 34 F8        STA     $F834               
F219: 20 C4 F3        JSR     $F3C4               ; {}
F21C: A9 DC           LDA     #$DC                
F21E: 8D 35 F8        STA     $F835               
F221: A6 D1           LDX     $D1                 ; {ram.mD1}
F223: A9 00           LDA     #$00                
F225: 9D 2E F8        STA     $F82E,X             
F228: B9 8D 00        LDA     $008D,Y             ; {ram.m8D}
F22B: F0 09           BEQ     $F236               ; {}
F22D: 99 5B F8        STA     $F85B,Y             
F230: 20 14 F3        JSR     $F314               ; {}
F233: 4C 3D F2        JMP     $F23D               ; {}
F236: A9 00           LDA     #$00                
F238: 99 8D 00        STA     $008D,Y             ; {ram.m8D}
F23B: F0 06           BEQ     $F243               ; {}
F23D: A9 01           LDA     #$01                
F23F: 99 1A F8        STA     $F81A,Y             
F242: 60              RTS                         
F243: A9 00           LDA     #$00                
F245: 9D 16 F8        STA     $F816,X             
F248: F0 00           BEQ     $F24A               ; {}
F24A: A9 00           LDA     #$00                
F24C: 99 1A F8        STA     $F81A,Y             
F24F: 60              RTS                         
F250: B9 8D 00        LDA     $008D,Y             ; {ram.m8D}
F253: D0 04           BNE     $F259               ; {}
F255: 20 38 F3        JSR     $F338               ; {}
F258: 60              RTS                         
F259: 38              SEC                         
F25A: E9 05           SBC     #$05                
F25C: 99 8D 00        STA     $008D,Y             ; {ram.m8D}
F25F: D0 04           BNE     $F265               ; {}
F261: 20 38 F3        JSR     $F338               ; {}
F264: 60              RTS                         
F265: 20 E0 F2        JSR     $F2E0               ; {}
F268: 38              SEC                         
F269: E9 05           SBC     #$05                
F26B: F0 F4           BEQ     $F261               ; {}
F26D: D9 8E 00        CMP     $008E,Y             ; {ram.m8E}
F270: F0 08           BEQ     $F27A               ; {}
F272: 90 06           BCC     $F27A               ; {}
F274: B9 8D 00        LDA     $008D,Y             ; {ram.m8D}
F277: 4C F6 F1        JMP     $F1F6               ; {}
F27A: A5 DE           LDA     $DE                 ; {ram.mDE}
F27C: 29 03           AND     #$03                
F27E: C9 03           CMP     #$03                
F280: D0 06           BNE     $F288               ; {}
F282: B9 8D 00        LDA     $008D,Y             ; {ram.m8D}
F285: 4C F6 F1        JMP     $F1F6               ; {}
F288: B9 8E 00        LDA     $008E,Y             ; {ram.m8E}
F28B: 99 5C F8        STA     $F85C,Y             
F28E: C8              INY                         
F28F: 20 14 F3        JSR     $F314               ; {}
F292: 90 0A           BCC     $F29E               ; {}
F294: A9 00           LDA     #$00                
F296: 99 8D 00        STA     $008D,Y             ; {ram.m8D}
F299: 99 1A F8        STA     $F81A,Y             
F29C: F0 0B           BEQ     $F2A9               ; {}
F29E: 38              SEC                         
F29F: E9 05           SBC     #$05                
F2A1: 99 8D 00        STA     $008D,Y             ; {ram.m8D}
F2A4: A9 01           LDA     #$01                
F2A6: 99 1A F8        STA     $F81A,Y             
F2A9: 88              DEY                         
F2AA: 86 D7           STX     $D7                 ; {ram.mD7}
F2AC: AD 55 F9        LDA     $F955               
F2AF: 0A              ASL     A                   
F2B0: 0A              ASL     A                   
F2B1: 18              CLC                         
F2B2: 65 D7           ADC     $D7                 ; {ram.mD7}
F2B4: AA              TAX                         
F2B5: BD 9E F1        LDA     $F19E,X             ; {}
F2B8: A6 D7           LDX     $D7                 ; {ram.mD7}
F2BA: A4 C9           LDY     $C9                 ; {ram.mC9}
F2BC: 99 A1 00        STA     $00A1,Y             ; {ram.mA1}
F2BF: 99 A2 00        STA     $00A2,Y             ; {ram.mA2}
F2C2: A4 C8           LDY     $C8                 ; {ram.mC8}
F2C4: A9 02           LDA     #$02                
F2C6: 99 1A F8        STA     $F81A,Y             
F2C9: 4C 4F F2        JMP     $F24F               ; {}
F2CC: B9 8D 00        LDA     $008D,Y             ; {ram.m8D}
F2CF: 18              CLC                         
F2D0: 69 05           ADC     #$05                
F2D2: 99 8D 00        STA     $008D,Y             ; {ram.m8D}
F2D5: 20 E5 F2        JSR     $F2E5               ; {}
F2D8: A9 03           LDA     #$03                
F2DA: 99 1A F8        STA     $F81A,Y             
F2DD: 4C 4F F2        JMP     $F24F               ; {}
F2E0: 48              PHA                         
F2E1: A9 05           LDA     #$05                
F2E3: D0 03           BNE     $F2E8               ; {}
F2E5: 48              PHA                         
F2E6: A9 FB           LDA     #$FB                
F2E8: 85 D1           STA     $D1                 ; {ram.mD1}
F2EA: A5 C9           LDA     $C9                 ; {ram.mC9}
F2EC: 84 CC           STY     $CC                 ; {ram.mCC}
F2EE: 86 CB           STX     $CB                 ; {ram.mCB}
F2F0: DD 11 F9        CMP     $F911,X             
F2F3: D0 19           BNE     $F30E               ; {}
F2F5: BD 16 F9        LDA     $F916,X             
F2F8: A2 FF           LDX     #$FF                
F2FA: E8              INX                         
F2FB: E0 04           CPX     #$04                
F2FD: F0 0F           BEQ     $F30E               ; {}
F2FF: 6A              ROR     A                   
F300: 90 F8           BCC     $F2FA               ; {}
F302: A8              TAY                         
F303: B5 C3           LDA     $C3,X               ; {ram.mC3}
F305: 18              CLC                         
F306: 65 D1           ADC     $D1                 ; {ram.mD1}
F308: 95 C3           STA     $C3,X               ; {ram.mC3}
F30A: 98              TYA                         
F30B: 4C FA F2        JMP     $F2FA               ; {}
F30E: A6 CB           LDX     $CB                 ; {ram.mCB}
F310: A4 CC           LDY     $CC                 ; {ram.mCC}
F312: 68              PLA                         
F313: 60              RTS                         
F314: 48              PHA                         
F315: 86 CB           STX     $CB                 ; {ram.mCB}
F317: 84 CC           STY     $CC                 ; {ram.mCC}
F319: AD 55 F9        LDA     $F955               
F31C: 0A              ASL     A                   
F31D: 0A              ASL     A                   
F31E: 0A              ASL     A                   
F31F: 85 DA           STA     $DA                 ; {ram.mDA}
F321: A5 CB           LDA     $CB                 ; {ram.mCB}
F323: 0A              ASL     A                   
F324: 18              CLC                         
F325: 65 DA           ADC     $DA                 ; {ram.mDA}
F327: AA              TAX                         
F328: BD EE F3        LDA     $F3EE,X             ; {}
F32B: 85 DA           STA     $DA                 ; {ram.mDA}
F32D: BD EF F3        LDA     $F3EF,X             ; {}
F330: 85 DB           STA     $DB                 ; {ram.mDB}
F332: B9 5B F9        LDA     $F95B,Y             
F335: 4C 98 F3        JMP     $F398               ; {}
F338: A6 CA           LDX     $CA                 ; {ram.mCA}
F33A: A9 FF           LDA     #$FF                
F33C: 99 72 F8        STA     $F872,Y             
F33F: A5 C9           LDA     $C9                 ; {ram.mC9}
F341: DD 11 F9        CMP     $F911,X             
F344: D0 29           BNE     $F36F               ; {}
F346: BD 2E F9        LDA     $F92E,X             
F349: F0 1C           BEQ     $F367               ; {}
F34B: 86 D1           STX     $D1                 ; {ram.mD1}
F34D: AA              TAX                         
F34E: BD E9 F3        LDA     $F3E9,X             ; {}
F351: 8D 33 F8        STA     $F833               
F354: AA              TAX                         
F355: A9 00           LDA     #$00                
F357: 8D 32 F8        STA     $F832               
F35A: 8D 34 F8        STA     $F834               
F35D: 20 C4 F3        JSR     $F3C4               ; {}
F360: A9 DC           LDA     #$DC                
F362: 8D 35 F8        STA     $F835               
F365: A6 D1           LDX     $D1                 ; {ram.mD1}
F367: A9 00           LDA     #$00                
F369: 9D 16 F8        STA     $F816,X             
F36C: 9D 2E F8        STA     $F82E,X             
F36F: A9 00           LDA     #$00                
F371: 99 1A F8        STA     $F81A,Y             
F374: 84 D6           STY     $D6                 ; {ram.mD6}
F376: 86 D7           STX     $D7                 ; {ram.mD7}
F378: A9 04           LDA     #$04                
F37A: A0 01           LDY     #$01                
F37C: 20 1A F6        JSR     $F61A               ; {}
F37F: A4 D6           LDY     $D6                 ; {ram.mD6}
F381: A6 D7           LDX     $D7                 ; {ram.mD7}
F383: A9 00           LDA     #$00                
F385: 99 8D 00        STA     $008D,Y             ; {ram.m8D}
F388: 99 5B F8        STA     $F85B,Y             
F38B: AD 86 F9        LDA     $F986               
F38E: 18              CLC                         
F38F: 69 01           ADC     #$01                
F391: 8D 86 F8        STA     $F886               
F394: 60              RTS                         
F395: 38              SEC                         
F396: B0 26           BCS     $F3BE               ; {}
F398: A0 FF           LDY     #$FF                
F39A: C8              INY                         
F39B: D1 DA           CMP     ($DA),Y             ; {ram.mDA}
F39D: D0 FB           BNE     $F39A               ; {}
F39F: C8              INY                         
F3A0: B1 DA           LDA     ($DA),Y             ; {ram.mDA}
F3A2: 4C AA F3        JMP     $F3AA               ; {}
F3A5: A4 CC           LDY     $CC                 ; {ram.mCC}
F3A7: 4C 38 F3        JMP     $F338               ; {}
F3AA: A4 CC           LDY     $CC                 ; {ram.mCC}
F3AC: 99 5B F8        STA     $F85B,Y             
F3AF: A9 50           LDA     #$50                
F3B1: A2 00           LDX     #$00                
F3B3: 20 C4 F3        JSR     $F3C4               ; {}
F3B6: A9 04           LDA     #$04                
F3B8: A0 01           LDY     #$01                
F3BA: 20 1A F6        JSR     $F61A               ; {}
F3BD: 18              CLC                         
F3BE: 68              PLA                         
F3BF: A6 CB           LDX     $CB                 ; {ram.mCB}
F3C1: A4 CC           LDY     $CC                 ; {ram.mCC}
F3C3: 60              RTS                         
F3C4: F8              SED                         
F3C5: 18              CLC                         
F3C6: 6D 71 F9        ADC     $F971               
F3C9: 8D 71 F8        STA     $F871               
F3CC: 8A              TXA                         
F3CD: 6D 70 F9        ADC     $F970               
F3D0: 8D 70 F8        STA     $F870               
F3D3: 90 0A           BCC     $F3DF               ; {}
F3D5: 18              CLC                         
F3D6: AD 57 F9        LDA     $F957               
F3D9: 69 01           ADC     #$01                
F3DB: 8D 57 F8        STA     $F857               
F3DE: 38              SEC                         
F3DF: A9 00           LDA     #$00                
F3E1: 6D 6F F9        ADC     $F96F               
F3E4: 8D 6F F8        STA     $F86F               
F3E7: D8              CLD                         
F3E8: 60              RTS                         

F3E9: 00 05 10 15 20 16 F4 1B F4 16 F4 16 F4 20 F4 20
F3F9: F4 20 F4 20 F4 26 F4 2B F4 2B F4 26 F4 30 F4 37
F409: F4 30 F4 48 F4 3C F4 42 F4 3C F4 3C F4 73 5F 4B
F419: 37 00 73 5F 37 23 00 73 55 3C 23 0A 00 73 50 2D
F429: 0A 00 73 5F 3C 19 00 73 5A 4B 3C 23 0A 00 73 4B
F439: 23 0A 00 73 5F 4B 37 0A 00 73 5F 4B 1E 0A 00 73
F449: 5A 3C 23 0A 00       

F44E: AC 37 F9        LDY     $F937               
F451: A2 10           LDX     #$10                
F453: CA              DEX                         
F454: 10 03           BPL     $F459               ; {}
F456: 4C E7 F4        JMP     $F4E7               ; {}
F459: 88              DEY                         
F45A: 10 02           BPL     $F45E               ; {}
F45C: A0 13           LDY     #$13                
F45E: B9 1A F9        LDA     $F91A,Y             
F461: F0 F0           BEQ     $F453               ; {}
F463: A2 04           LDX     #$04                
F465: A9 00           LDA     #$00                
F467: 85 D6           STA     $D6                 ; {ram.mD6}
F469: 84 D1           STY     $D1                 ; {ram.mD1}
F46B: A4 D1           LDY     $D1                 ; {ram.mD1}
F46D: CA              DEX                         
F46E: 30 68           BMI     $F4D8               ; {}
F470: AD 36 F9        LDA     $F936               
F473: 3D 2B F5        AND     $F52B,X             ; {}
F476: D0 F3           BNE     $F46B               ; {}
F478: A9 73           LDA     #$73                
F47A: 38              SEC                         
F47B: F9 8D 00        SBC     $008D,Y             ; {ram.m8D}
F47E: 38              SEC                         
F47F: F5 C3           SBC     $C3,X               ; {ram.mC3}
F481: F0 06           BEQ     $F489               ; {}
F483: 10 E6           BPL     $F46B               ; {}
F485: C9 F9           CMP     #$F9                
F487: 90 E2           BCC     $F46B               ; {}
F489: AD 55 F9        LDA     $F955               
F48C: 0A              ASL     A                   
F48D: 0A              ASL     A                   
F48E: 85 CC           STA     $CC                 ; {ram.mCC}
F490: B9 EB F4        LDA     $F4EB,Y             ; {}
F493: 18              CLC                         
F494: 65 CC           ADC     $CC                 ; {ram.mCC}
F496: A8              TAY                         
F497: B5 BE           LDA     $BE,X               ; {ram.mBE}
F499: D9 17 F5        CMP     $F517,Y             ; {}
F49C: B0 CD           BCS     $F46B               ; {}
F49E: D9 03 F5        CMP     $F503,Y             ; {}
F4A1: 90 C8           BCC     $F46B               ; {}
F4A3: A9 01           LDA     #$01                
F4A5: 85 D6           STA     $D6                 ; {ram.mD6}
F4A7: AD 40 F9        LDA     $F940               
F4AA: 1D 2B F5        ORA     $F52B,X             ; {}
F4AD: 8D 40 F8        STA     $F840               
F4B0: BD FF F4        LDA     $F4FF,X             ; {}
F4B3: 18              CLC                         
F4B4: 8D 33 F8        STA     $F833               
F4B7: 86 CC           STX     $CC                 ; {ram.mCC}
F4B9: AA              TAX                         
F4BA: A9 00           LDA     #$00                
F4BC: 8D 32 F8        STA     $F832               
F4BF: 8D 34 F8        STA     $F834               
F4C2: 20 C4 F3        JSR     $F3C4               ; {}
F4C5: A6 CC           LDX     $CC                 ; {ram.mCC}
F4C7: A9 78           LDA     #$78                
F4C9: 8D 35 F8        STA     $F835               
F4CC: AD 36 F9        LDA     $F936               
F4CF: 1D 2B F5        ORA     $F52B,X             ; {}
F4D2: 8D 36 F8        STA     $F836               
F4D5: 4C 6B F4        JMP     $F46B               ; {}
F4D8: A5 D6           LDA     $D6                 ; {ram.mD6}
F4DA: F0 0B           BEQ     $F4E7               ; {}
F4DC: 84 D6           STY     $D6                 ; {ram.mD6}
F4DE: A9 09           LDA     #$09                
F4E0: A0 01           LDY     #$01                
F4E2: 20 22 F6        JSR     $F622               ; {}
F4E5: A4 D6           LDY     $D6                 ; {ram.mD6}
F4E7: 8C 37 F8        STY     $F837               
F4EA: 60              RTS                         

F4EB: 00 00 00 00 00 01 01 01 01 01 02 02 02 02 02 03
F4FB: 03 03 03 03 02 01 01 02 18 38 68 8C 18 3C 68 8C
F50B: 10 38 70 88 18 38 68 88 18 38 68 84 27 47 77 9B
F51B: 27 4B 77 9B 1F 47 7F 97 27 47 77 97 27 47 77 93
F52B: 01 02 04 08 0F F0

F531: A9 01           LDA     #$01                
F533: AA              TAX                         
F534: 86 C8           STX     $C8                 ; {ram.mC8}
F536: A5 DF           LDA     $DF                 ; {ram.mDF}
F538: 3D 2F F5        AND     $F52F,X             ; {}
F53B: E0 01           CPX     #$01                
F53D: F0 04           BEQ     $F543               ; {}
F53F: 0A              ASL     A                   
F540: 0A              ASL     A                   
F541: 0A              ASL     A                   
F542: 0A              ASL     A                   
F543: 85 C7           STA     $C7                 ; {ram.mC7}
F545: BD 4C F9        LDA     $F94C,X             
F548: 0A              ASL     A                   
F549: 18              CLC                         
F54A: 65 C7           ADC     $C7                 ; {ram.mC7}
F54C: A8              TAY                         
F54D: B9 CE F5        LDA     $F5CE,Y             ; {}
F550: 18              CLC                         
F551: 75 C2           ADC     $C2,X               ; {ram.mC2}
F553: 85 C7           STA     $C7                 ; {ram.mC7}
F555: B9 CF F5        LDA     $F5CF,Y             ; {}
F558: 69 00           ADC     #$00                
F55A: 85 C9           STA     $C9                 ; {ram.mC9}
F55C: 8A              TXA                         
F55D: 0A              ASL     A                   
F55E: AA              TAX                         
F55F: A5 C7           LDA     $C7                 ; {ram.mC7}
F561: 95 E0           STA     $E0,X               ; {ram.mE0}
F563: A5 C9           LDA     $C9                 ; {ram.mC9}
F565: 95 E1           STA     $E1,X               ; {ram.mE1}
F567: A6 C8           LDX     $C8                 ; {ram.mC8}
F569: CA              DEX                         
F56A: 10 C8           BPL     $F534               ; {}
F56C: A2 01           LDX     #$01                
F56E: BD 4C F9        LDA     $F94C,X             
F571: 10 02           BPL     $F575               ; {}
F573: A9 07           LDA     #$07                
F575: A8              TAY                         
F576: B9 BE F5        LDA     $F5BE,Y             ; {}
F579: 85 C9           STA     $C9                 ; {ram.mC9}
F57B: BD 4E F9        LDA     $F94E,X             
F57E: 10 02           BPL     $F582               ; {}
F580: A9 07           LDA     #$07                
F582: A8              TAY                         
F583: B9 C6 F5        LDA     $F5C6,Y             ; {}
F586: 05 C9           ORA     $C9                 ; {ram.mC9}
F588: 95 F0           STA     $F0,X               ; {ram.mF0}
F58A: CA              DEX                         
F58B: 10 E1           BPL     $F56E               ; {}
F58D: A0 01           LDY     #$01                
F58F: A2 02           LDX     #$02                
F591: A9 79           LDA     #$79                
F593: 38              SEC                         
F594: F9 C2 00        SBC     $00C2,Y             ; {ram.mC2}
F597: 85 CC           STA     $CC                 ; {ram.mCC}
F599: A9 85           LDA     #$85                
F59B: 38              SEC                         
F59C: E5 CC           SBC     $CC                 ; {ram.mCC}
F59E: 95 E4           STA     $E4,X               ; {ram.mE4}
F5A0: A9 FA           LDA     #$FA                
F5A2: E9 00           SBC     #$00                
F5A4: 95 E5           STA     $E5,X               ; {ram.mE5}
F5A6: E8              INX                         
F5A7: E8              INX                         
F5A8: C8              INY                         
F5A9: C0 05           CPY     #$05                
F5AB: D0 E4           BNE     $F591               ; {}
F5AD: A5 E0           LDA     $E0                 ; {ram.mE0}
F5AF: 85 E4           STA     $E4                 ; {ram.mE4}
F5B1: A5 E1           LDA     $E1                 ; {ram.mE1}
F5B3: 85 E5           STA     $E5                 ; {ram.mE5}
F5B5: 60              RTS                         

F5B6: 20 20 40 40 80 80 80 80 00 00 00 00 00 00 00 00
F5C6: 30 30 20 20 10 10 00 00 79 F5 79 F5 79 F5 79 F5
F5D6: 79 F5 79 F5 79 F5 79 F5 00 F5 00 F5 00 F5 00 F5
F5E6: 00 F4 00 F4 00 F4 00 F4 79 F0 79 F0 79 F0 79 F0
F5F6: 79 F0 79 F0 79 F0 79 F0 79 F5 79 F2 79 F5 79 F0
F606: 00 F3 00 F0 00 F1 00 F2

F60E: 8D F8 F8        STA     $F8F8               
F611: A5 80           LDA     $80                 ; {ram.m80}
F613: 29 C0           AND     #$C0                
F615: D0 09           BNE     $F620               ; {}
F617: AD F8 F9        LDA     $F9F8               
F61A: 24 80           BIT     $80                 ; {ram.m80}
F61C: 10 08           BPL     $F626               ; {}
F61E: 50 02           BVC     $F622               ; {}
F620: 38              SEC                         
F621: 60              RTS                         
F622: A2 01           LDX     #$01                
F624: D0 02           BNE     $F628               ; {}
F626: A2 00           LDX     #$00                
F628: 9D 00 F8        STA     $F800,X             
F62B: 98              TYA                         
F62C: 9D 06 F8        STA     $F806,X             
F62F: A9 00           LDA     #$00                
F631: 9D 04 F8        STA     $F804,X             
F634: 9D 02 F8        STA     $F802,X             
F637: A4 80           LDY     $80                 ; {ram.m80}
F639: 8A              TXA                         
F63A: F0 05           BEQ     $F641               ; {}
F63C: 98              TYA                         
F63D: 09 40           ORA     #$40                
F63F: D0 03           BNE     $F644               ; {}
F641: 98              TYA                         
F642: 09 80           ORA     #$80                
F644: 85 80           STA     $80                 ; {ram.m80}
F646: 18              CLC                         
F647: 60              RTS                         

F648: FA  DC 

F64A: C8              INY                         
F64B: B4 A0           LDY     $A0,X               ; {ram.mA0}
F64D: AD 4B F9        LDA     $F94B               
F650: D0 54           BNE     $F6A6               ; {}
F652: AD 86 F9        LDA     $F986               
F655: F0 4F           BEQ     $F6A6               ; {}
F657: C9 10           CMP     #$10                
F659: F0 4B           BEQ     $F6A6               ; {}
F65B: 29 03           AND     #$03                
F65D: D0 47           BNE     $F6A6               ; {}
F65F: AD 86 F9        LDA     $F986               
F662: 29 0C           AND     #$0C                
F664: 4A              LSR     A                   
F665: 4A              LSR     A                   
F666: AA              TAX                         
F667: AD 5A F9        LDA     $F95A               
F66A: 3D A7 F6        AND     $F6A7,X             ; {}
F66D: D0 37           BNE     $F6A6               ; {}
F66F: BD A7 F6        LDA     $F6A7,X             ; {}
F672: 0D 5A F9        ORA     $F95A               
F675: 8D 5A F8        STA     $F85A               
F678: CA              DEX                         
F679: 8E 59 F8        STX     $F859               
F67C: A9 06           LDA     #$06                
F67E: A0 01           LDY     #$01                
F680: 20 26 F6        JSR     $F626               ; {}
F683: AE 55 F9        LDX     $F955               
F686: BD 48 F6        LDA     $F648,X             ; {}
F689: 8D 4B F8        STA     $F84B               
F68C: AD DF 00        LDA     $00DF               ; {ram.mDF}
F68F: 29 F0           AND     #$F0                
F691: 8D 45 F8        STA     $F845               
F694: AD 4D F9        LDA     $F94D               
F697: 8D 44 F8        STA     $F844               
F69A: AD BE 00        LDA     $00BE               ; {ram.mBE}
F69D: 8D 42 F8        STA     $F842               
F6A0: AD C3 00        LDA     $00C3               ; {ram.mC3}
F6A3: 8D 43 F8        STA     $F843               
F6A6: 60              RTS                         
 
F6A7: 01 02 04 08 FF FF 00 FF FF FF 04 FF 06 02 FF

F6B6: AD 49 F9        LDA     $F949               
F6B9: 18              CLC                         
F6BA: 69 01           ADC     #$01                
F6BC: 8D 49 F8        STA     $F849               
F6BF: AD 80 02        LDA     $0280               ; {hard.SWCHA}
F6C2: 4A              LSR     A                   
F6C3: 4A              LSR     A                   
F6C4: 4A              LSR     A                   
F6C5: 4A              LSR     A                   
F6C6: A8              TAY                         
F6C7: B9 A6 F6        LDA     $F6A6,Y             ; {}
F6CA: CD 48 F9        CMP     $F948               
F6CD: F0 0D           BEQ     $F6DC               ; {}
F6CF: 8D 48 F8        STA     $F848               
F6D2: 38              SEC                         
F6D3: A9 00           LDA     #$00                
F6D5: 8D 49 F8        STA     $F849               
F6D8: AD 48 F9        LDA     $F948               
F6DB: 60              RTS                         
F6DC: 18              CLC                         
F6DD: 60              RTS                         
                  
F6DE: 00 00

F6E0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F6F0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F700: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F710: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F720: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F730: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F740: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F750: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F760: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F770: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F780: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F790: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F7A0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F7B0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F7C0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F7D0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F7E0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F7F0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```

