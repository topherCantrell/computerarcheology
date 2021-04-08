![Burger Time](A2600BT.jpg)

# Burger Time Bank 3

>>> cpu 6502

>>> memoryTable hard 
[Hardware Info](../Stella.md)

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

F000: 01 02           ORA     ($02,X)               
F002: 04 ; ????
F003: 08              PHP                         
F004: B6 F3           LDX     $F3,Y                 
F006: AE F4 B2        LDX     $B2F4                   
F009: F5 72           SBC     $72,X                 
F00B: F6 42           INC     $42,X                 
F00D: F7 ; ????
F00E: 6C F3 4A        JMP     ($4AF3)                 
F011: F4 ; ????
F012: 76 F5           ROR     $F5,X                 
F014: 2A              ROL     A                   
F015: F6 02           INC     $02,X                 
F017: F7 ; ????
F018: 91 F3           STA     ($F3),Y               
F01A: 7C ; ????
F01B: F4 ; ????
F01C: 94 F5           STY     $F5,X                 
F01E: 4E F6 22        LSR     $22F6                   
F021: F7 ; ????
F022: 08              PHP                         
F023: 05 00           ORA     $00                   
F025: FB ; ????
F026: F8              SED                         
F027: FB ; ????
F028: 00              BRK                         
F029: 05 08           ORA     $08                   
F02B: 00              BRK                         
F02C: 02 ; ????
F02D: 02 ; ????
F02E: 03 ; ????
F02F: 03 ; ????
F030: 04 ; ????
F031: 04 ; ????
F032: 04 ; ????
F033: 04 ; ????
F034: 60              RTS                         
F035: A5 DE           LDA     $DE                   
F037: 29 03           AND     #$03                  
F039: AA              TAX                         
F03A: AD 40 F9        LDA     $F940                   
F03D: 3D 00 F0        AND     $F000,X                 
F040: D0 F2           BNE     $F034                   
F042: AD 36 F9        LDA     $F936                   
F045: 3D 00 F0        AND     $F000,X                 
F048: D0 EA           BNE     $F034                   
F04A: 86 C7           STX     $C7                   
F04C: AD 55 F9        LDA     $F955                   
F04F: 0A              ASL     A                   
F050: AA              TAX                         
F051: 86 CB           STX     $CB                   
F053: BD 0E F0        LDA     $F00E,X                 
F056: 85 CD           STA     $CD                   
F058: BD 0F F0        LDA     $F00F,X                 
F05B: 85 CE           STA     $CE                   
F05D: BD 18 F0        LDA     $F018,X                 
F060: 85 CF           STA     $CF                   
F062: BD 19 F0        LDA     $F019,X                 
F065: 85 D0           STA     $D0                   
F067: A6 C7           LDX     $C7                   
F069: B5 BE           LDA     $BE,X                 
F06B: BC 51 F9        LDY     $F951,X                 
F06E: D1 CD           CMP     ($CD),Y               
F070: D0 4C           BNE     $F0BE                   
F072: B5 C3           LDA     $C3,X                 
F074: D1 CF           CMP     ($CF),Y               
F076: D0 46           BNE     $F0BE                   
F078: A6 CB           LDX     $CB                   
F07A: BD 04 F0        LDA     $F004,X                 
F07D: 85 CD           STA     $CD                   
F07F: BD 05 F0        LDA     $F005,X                 
F082: 85 CE           STA     $CE                   
F084: A6 C7           LDX     $C7                   
F086: 84 C9           STY     $C9                   
F088: 98              TYA                         
F089: 0A              ASL     A                   
F08A: 0A              ASL     A                   
F08B: 85 CA           STA     $CA                   
F08D: AD 87 F9        LDA     $F987                   
F090: 3D 00 F0        AND     $F000,X                 
F093: F0 06           BEQ     $F09B                   
F095: 20 32 F1        JSR     $F132                   
F098: 4C BE F0        JMP     $F0BE                   
F09B: 20 E1 F1        JSR     $F1E1                   
F09E: 29 03           AND     #$03                  
F0A0: 18              CLC                         
F0A1: 65 CA           ADC     $CA                   
F0A3: A8              TAY                         
F0A4: B1 CD           LDA     ($CD),Y               
F0A6: C9 FF           CMP     #$FF                  
F0A8: F0 10           BEQ     $F0BA                   
F0AA: A6 C7           LDX     $C7                   
F0AC: 9D 51 F8        STA     $F851,X                 
F0AF: AD 4A F9        LDA     $F94A                   
F0B2: 29 03           AND     #$03                  
F0B4: 0A              ASL     A                   
F0B5: 95 B9           STA     $B9,X                 
F0B7: 4C BE F0        JMP     $F0BE                   
F0BA: A9 FF           LDA     #$FF                  
F0BC: 95 B9           STA     $B9,X                 
F0BE: A6 C7           LDX     $C7                   
F0C0: B4 B9           LDY     $B9,X                 
F0C2: C0 FF           CPY     #$FF                  
F0C4: F0 5A           BEQ     $F120                   
F0C6: B9 22 F0        LDA     $F022,Y                 
F0C9: F0 11           BEQ     $F0DC                   
F0CB: 10 09           BPL     $F0D6                   
F0CD: A9 00           LDA     #$00                  
F0CF: 38              SEC                         
F0D0: ED 88 F9        SBC     $F988                   
F0D3: 4C D9 F0        JMP     $F0D9                   
F0D6: AD 88 F9        LDA     $F988                   
F0D9: 20 04 F2        JSR     $F204                   
F0DC: 18              CLC                         
F0DD: 75 BE           ADC     $BE,X                 
F0DF: 95 BE           STA     $BE,X                 
F0E1: 84 CA           STY     $CA                   
F0E3: A8              TAY                         
F0E4: E0 00           CPX     #$00                  
F0E6: F0 0D           BEQ     $F0F5                   
F0E8: 85 CB           STA     $CB                   
F0EA: BD 4D F9        LDA     $F94D,X                 
F0ED: A8              TAY                         
F0EE: B9 2C F0        LDA     $F02C,Y                 
F0F1: 18              CLC                         
F0F2: 65 CB           ADC     $CB                   
F0F4: A8              TAY                         
F0F5: 8A              TXA                         
F0F6: 18              CLC                         
F0F7: 69 B5           ADC     #$B5                  
F0F9: AA              TAX                         
F0FA: 98              TYA                         
F0FB: 20 1C F2        JSR     $F21C                   
F0FE: A6 C7           LDX     $C7                   
F100: B4 B9           LDY     $B9,X                 
F102: C0 FF           CPY     #$FF                  
F104: F0 1A           BEQ     $F120                   
F106: B9 24 F0        LDA     $F024,Y                 
F109: F0 15           BEQ     $F120                   
F10B: 10 08           BPL     $F115                   
F10D: A9 00           LDA     #$00                  
F10F: 38              SEC                         
F110: ED 89 F9        SBC     $F989                   
F113: D0 03           BNE     $F118                   
F115: AD 89 F9        LDA     $F989                   
F118: 20 04 F2        JSR     $F204                   
F11B: 18              CLC                         
F11C: 75 C3           ADC     $C3,X                 
F11E: 95 C3           STA     $C3,X                 
F120: A5 DE           LDA     $DE                   
F122: 29 0F           AND     #$0F                  
F124: 4A              LSR     A                   
F125: 18              CLC                         
F126: 65 C7           ADC     $C7                   
F128: 29 07           AND     #$07                  
F12A: 9D 4D F8        STA     $F84D,X                 
F12D: 60              RTS                         
F12E: 80 ; ????
F12F: 40              RTI                         
F130: 20 10 A5        JSR     $A510                   
F133: BD 38 F5        LDA     $F538,X                 
F136: BE 85 CB        LDX     $CB85,Y                 
F139: 10 05           BPL     $F140                   
F13B: A9 00           LDA     #$00                  
F13D: 38              SEC                         
F13E: E5 CB           SBC     $CB                   
F140: 85 CF           STA     $CF                   
F142: A5 C2           LDA     $C2                   
F144: 38              SEC                         
F145: F5 C3           SBC     $C3,X                 
F147: 85 CC           STA     $CC                   
F149: 10 05           BPL     $F150                   
F14B: A9 00           LDA     #$00                  
F14D: 38              SEC                         
F14E: E5 CC           SBC     $CC                   
F150: 85 D0           STA     $D0                   
F152: AD 87 F9        LDA     $F987                   
F155: 3D 2E F1        AND     $F12E,X                 
F158: F0 2A           BEQ     $F184                   
F15A: B5 B9           LDA     $B9,X                 
F15C: F0 15           BEQ     $F173                   
F15E: C9 04           CMP     #$04                  
F160: F0 11           BEQ     $F173                   
F162: 20 C5 F1        JSR     $F1C5                   
F165: 85 D6           STA     $D6                   
F167: 84 D7           STY     $D7                   
F169: 20 D3 F1        JSR     $F1D3                   
F16C: 85 D8           STA     $D8                   
F16E: 84 D9           STY     $D9                   
F170: 4C A9 F1        JMP     $F1A9                   
F173: 20 D3 F1        JSR     $F1D3                   
F176: 85 D6           STA     $D6                   
F178: 84 D7           STY     $D7                   
F17A: 20 C5 F1        JSR     $F1C5                   
F17D: 85 D8           STA     $D8                   
F17F: 84 D9           STY     $D9                   
F181: 4C A9 F1        JMP     $F1A9                   
F184: A5 D0           LDA     $D0                   
F186: C5 CF           CMP     $CF                   
F188: 90 11           BCC     $F19B                   
F18A: 20 D3 F1        JSR     $F1D3                   
F18D: 85 D6           STA     $D6                   
F18F: 84 D9           STY     $D9                   
F191: 20 C5 F1        JSR     $F1C5                   
F194: 85 D7           STA     $D7                   
F196: 84 D8           STY     $D8                   
F198: 4C A9 F1        JMP     $F1A9                   
F19B: 20 C5 F1        JSR     $F1C5                   
F19E: 85 D6           STA     $D6                   
F1A0: 84 D9           STY     $D9                   
F1A2: 20 D3 F1        JSR     $F1D3                   
F1A5: 85 D7           STA     $D7                   
F1A7: 84 D8           STY     $D8                   
F1A9: A2 FF           LDX     #$FF                  
F1AB: E8              INX                         
F1AC: B5 D6           LDA     $D6,X                 
F1AE: 85 CC           STA     $CC                   
F1B0: 18              CLC                         
F1B1: 65 CA           ADC     $CA                   
F1B3: A8              TAY                         
F1B4: B1 CD           LDA     ($CD),Y               
F1B6: C9 FF           CMP     #$FF                  
F1B8: F0 F1           BEQ     $F1AB                   
F1BA: A6 C7           LDX     $C7                   
F1BC: 9D 51 F8        STA     $F851,X                 
F1BF: A5 CC           LDA     $CC                   
F1C1: 0A              ASL     A                   
F1C2: 95 B9           STA     $B9,X                 
F1C4: 60              RTS                         
F1C5: A5 CB           LDA     $CB                   
F1C7: 30 05           BMI     $F1CE                   
F1C9: A9 00           LDA     #$00                  
F1CB: A0 02           LDY     #$02                  
F1CD: 60              RTS                         
F1CE: A9 02           LDA     #$02                  
F1D0: A0 00           LDY     #$00                  
F1D2: 60              RTS                         
F1D3: A5 CC           LDA     $CC                   
F1D5: 30 05           BMI     $F1DC                   
F1D7: A9 03           LDA     #$03                  
F1D9: A0 01           LDY     #$01                  
F1DB: 60              RTS                         
F1DC: A9 01           LDA     #$01                  
F1DE: A0 03           LDY     #$03                  
F1E0: 60              RTS                         
F1E1: AD 4A F9        LDA     $F94A                   
F1E4: 0A              ASL     A                   
F1E5: 0A              ASL     A                   
F1E6: 0A              ASL     A                   
F1E7: 0A              ASL     A                   
F1E8: 18              CLC                         
F1E9: 6D 4A F9        ADC     $F94A                   
F1EC: 0A              ASL     A                   
F1ED: 0A              ASL     A                   
F1EE: 0A              ASL     A                   
F1EF: 18              CLC                         
F1F0: 6D 4A F9        ADC     $F94A                   
F1F3: 18              CLC                         
F1F4: 69 95           ADC     #$95                  
F1F6: 8D 4A F8        STA     $F84A                   
F1F9: 60              RTS                         
F1FA: A5 B3           LDA     $B3                   
F1FC: 18              CLC                         
F1FD: 69 17           ADC     #$17                  
F1FF: 29 1F           AND     #$1F                  
F201: 85 B3           STA     $B3                   
F203: 60              RTS                         
F204: 18              CLC                         
F205: 65 B3           ADC     $B3                   
F207: 4A              LSR     A                   
F208: 4A              LSR     A                   
F209: 4A              LSR     A                   
F20A: 4A              LSR     A                   
F20B: 4A              LSR     A                   
F20C: 49 04           EOR     #$04                  
F20E: 38              SEC                         
F20F: E9 04           SBC     #$04                  
F211: 30 03           BMI     $F216                   
F213: 29 01           AND     #$01                  
F215: 60              RTS                         
F216: A9 FF           LDA     #$FF                  
F218: 60              RTS                         
F219: 38              SEC                         
F21A: E9 03           SBC     #$03                  
F21C: 48              PHA                         
F21D: 29 0F           AND     #$0F                  
F21F: 85 CC           STA     $CC                   
F221: 68              PLA                         
F222: 4A              LSR     A                   
F223: 4A              LSR     A                   
F224: 4A              LSR     A                   
F225: 4A              LSR     A                   
F226: 85 CD           STA     $CD                   
F228: 18              CLC                         
F229: 65 CC           ADC     $CC                   
F22B: C9 0F           CMP     #$0F                  
F22D: 90 04           BCC     $F233                   
F22F: E9 0F           SBC     #$0F                  
F231: E6 CD           INC     $CD                   
F233: 49 07           EOR     #$07                  
F235: 0A              ASL     A                   
F236: 0A              ASL     A                   
F237: 0A              ASL     A                   
F238: 0A              ASL     A                   
F239: 05 CD           ORA     $CD                   
F23B: 95 00           STA     $00,X                 
F23D: 60              RTS                         
F23E: A2 04           LDX     #$04                  
F240: 85 02           STA     $02                   
F242: B5 B4           LDA     $B4,X                 
F244: 95 20           STA     $20,X                 
F246: 29 0F           AND     #$0F                  
F248: A8              TAY                         
F249: A5 80           LDA     $80                   
F24B: 88              DEY                         
F24C: 10 FD           BPL     $F24B                   
F24E: 95 10           STA     $10,X                 
F250: 85 02           STA     $02                   
F252: CA              DEX                         
F253: 10 EB           BPL     $F240                   
F255: 85 02           STA     $02                   
F257: 85 2A           STA     $2A                   
F259: 60              RTS                         
F25A: 18              CLC                         
F25B: 60              RTS                         
F25C: AD 36 F9        LDA     $F936                   
F25F: F0 F9           BEQ     $F25A                   
F261: AD 55 F9        LDA     $F955                   
F264: 0A              ASL     A                   
F265: AA              TAX                         
F266: BD 0E F0        LDA     $F00E,X                 
F269: 85 CD           STA     $CD                   
F26B: BD 0F F0        LDA     $F00F,X                 
F26E: 85 CE           STA     $CE                   
F270: BD 18 F0        LDA     $F018,X                 
F273: 85 CF           STA     $CF                   
F275: BD 19 F0        LDA     $F019,X                 
F278: 85 D0           STA     $D0                   
F27A: BD 04 F0        LDA     $F004,X                 
F27D: 85 DA           STA     $DA                   
F27F: BD 05 F0        LDA     $F005,X                 
F282: 85 DB           STA     $DB                   
F284: A2 04           LDX     #$04                  
F286: CA              DEX                         
F287: 30 D2           BMI     $F25B                   
F289: AD 36 F9        LDA     $F936                   
F28C: 3D 00 F0        AND     $F000,X                 
F28F: F0 F5           BEQ     $F286                   
F291: AD 16 F9        LDA     $F916                   
F294: 3D 00 F0        AND     $F000,X                 
F297: D0 ED           BNE     $F286                   
F299: AD 17 F9        LDA     $F917                   
F29C: 3D 00 F0        AND     $F000,X                 
F29F: D0 E5           BNE     $F286                   
F2A1: AD 18 F9        LDA     $F918                   
F2A4: 3D 00 F0        AND     $F000,X                 
F2A7: D0 DD           BNE     $F286                   
F2A9: AD 19 F9        LDA     $F919                   
F2AC: 3D 00 F0        AND     $F000,X                 
F2AF: D0 D5           BNE     $F286                   
F2B1: BD 00 F0        LDA     $F000,X                 
F2B4: 49 FF           EOR     #$FF                  
F2B6: 85 CC           STA     $CC                   
F2B8: 2D 36 F9        AND     $F936                   
F2BB: 8D 36 F8        STA     $F836                   
F2BE: A5 CC           LDA     $CC                   
F2C0: 2D 40 F9        AND     $F940                   
F2C3: 8D 40 F8        STA     $F840                   
F2C6: 86 D1           STX     $D1                   
F2C8: A2 03           LDX     #$03                  
F2CA: A5 CC           LDA     $CC                   
F2CC: 3D 16 F9        AND     $F916,X                 
F2CF: 9D 16 F8        STA     $F816,X                 
F2D2: CA              DEX                         
F2D3: 10 F5           BPL     $F2CA                   
F2D5: A6 D1           LDX     $D1                   
F2D7: AD 38 F9        LDA     $F938                   
F2DA: 18              CLC                         
F2DB: 69 01           ADC     #$01                  
F2DD: C9 04           CMP     #$04                  
F2DF: D0 02           BNE     $F2E3                   
F2E1: A9 00           LDA     #$00                  
F2E3: 8D 38 F8        STA     $F838                   
F2E6: AD 55 F9        LDA     $F955                   
F2E9: 0A              ASL     A                   
F2EA: 0A              ASL     A                   
F2EB: 18              CLC                         
F2EC: 6D 38 F9        ADC     $F938                   
F2EF: A8              TAY                         
F2F0: B9 34 F3        LDA     $F334,Y                 
F2F3: A8              TAY                         
F2F4: B1 CD           LDA     ($CD),Y               
F2F6: 95 BE           STA     $BE,X                 
F2F8: B1 CF           LDA     ($CF),Y               
F2FA: 95 C3           STA     $C3,X                 
F2FC: AD 38 F9        LDA     $F938                   
F2FF: 0A              ASL     A                   
F300: 9D B9 00        STA     $00B9,X                 
F303: 98              TYA                         
F304: 0A              ASL     A                   
F305: 0A              ASL     A                   
F306: 18              CLC                         
F307: 6D 38 F9        ADC     $F938                   
F30A: A8              TAY                         
F30B: B1 DA           LDA     ($DA),Y               
F30D: 9D 51 F8        STA     $F851,X                 
F310: 4C 86 F2        JMP     $F286                   
F313: AE 55 F9        LDX     $F955                   
F316: BD 2A F3        LDA     $F32A,X                 
F319: 85 BD           STA     $BD                   
F31B: BD 2F F3        LDA     $F32F,X                 
F31E: 85 C2           STA     $C2                   
F320: BD 48 F3        LDA     $F348,X                 
F323: 8D 0F F8        STA     $F80F                   
F326: 8D 10 F8        STA     $F810                   
F329: 60              RTS                         
F32A: 4D 41 4D        EOR     $4D41                   
F32D: 4D 4C 69        EOR     $694C                   
F330: 69 5A           ADC     #$5A                  
F332: 69 69           ADC     #$69                  
F334: 01 19           ORA     ($19,X)               
F336: 21 09           AND     ($09,X)               
F338: 00              BRK                         
F339: 2C 31 05        BIT     $0531                   
F33C: 1A ; ????
F33D: 18              CLC                         
F33E: 1D 03 00        ORA     $0003,X                 
F341: 1D 20 05        ORA     $0520,X                 
F344: 00              BRK                         
F345: 1B ; ????
F346: 1F ; ????
F347: 05 00           ORA     $00                   
F349: 00              BRK                         
F34A: 0F ; ????
F34B: 00              BRK                         
F34C: 00              BRK                         
F34D: A9 0F           LDA     #$0F                  
F34F: 8D 40 F8        STA     $F840                   
F352: A9 00           LDA     #$00                  
F354: 8D 16 F8        STA     $F816                   
F357: 8D 17 F8        STA     $F817                   
F35A: 8D 18 F8        STA     $F818                   
F35D: 8D 19 F8        STA     $F819                   
F360: A9 0F           LDA     #$0F                  
F362: 8D 36 F8        STA     $F836                   
F365: 20 5C F2        JSR     $F25C                   
F368: 20 13 F3        JSR     $F313                   
F36B: 60              RTS                         
F36C: 4D 08 1D        EOR     $1D08                   
F36F: 2C 3C 4D        BIT     $4D3C                   
F372: 5D 6D 7D        EOR     $7D6D,X                 
F375: 91 08           STA     ($08),Y               
F377: 1D 2C 3C        ORA     $3C2C,X                 
F37A: 4D 5D 6D        EOR     $6D5D                   
F37D: 7D 91 08        ADC     $0891,X                 
F380: 1D 2C 6D        ORA     $6D2C,X                 
F383: 7D 91 08        ADC     $0891,X                 
F386: 1D 2C 3C        ORA     $3C2C,X                 
F389: 4D 5D 6D        EOR     $6D5D                   
F38C: 7D 91 3C        ADC     $3C91,X                 
F38F: 4D 5D 69        EOR     $695D                   
F392: 00              BRK                         
F393: 00              BRK                         
F394: 00              BRK                         
F395: 00              BRK                         
F396: 00              BRK                         
F397: 00              BRK                         
F398: 00              BRK                         
F399: 00              BRK                         
F39A: 00              BRK                         
F39B: 14 ; ????
F39C: 14 ; ????
F39D: 14 ; ????
F39E: 14 ; ????
F39F: 14 ; ????
F3A0: 14 ; ????
F3A1: 14 ; ????
F3A2: 14 ; ????
F3A3: 14 ; ????
F3A4: 28              PLP                         
F3A5: 28              PLP                         
F3A6: 28              PLP                         
F3A7: 28              PLP                         
F3A8: 28              PLP                         
F3A9: 28              PLP                         
F3AA: 3C ; ????
F3AB: 3C ; ????
F3AC: 3C ; ????
F3AD: 3C ; ????
F3AE: 3C ; ????
F3AF: 3C ; ????
F3B0: 3C ; ????
F3B1: 3C ; ????
F3B2: 3C ; ????
F3B3: 50 50           BVC     $F405                   
F3B5: 50 FF           BVC     $F3B6                   
F3B7: 23 ; ????
F3B8: FF ; ????
F3B9: FF ; ????
F3BA: 02 ; ????
F3BB: FF ; ????
F3BC: FF ; ????
F3BD: 0A              ASL     A                   
F3BE: 03 ; ????
F3BF: FF ; ????
F3C0: 01 0B           ORA     ($0B,X)               
F3C2: 04 ; ????
F3C3: FF ; ????
F3C4: 02 ; ????
F3C5: 0C ; ????
F3C6: 05 FF           ORA     $FF                   
F3C8: 03 ; ????
F3C9: 0D 06 FF        ORA     $FF06                   
F3CC: 04 ; ????
F3CD: 0E 07 FF        ASL     $FF07                   
F3D0: 05 0F           ORA     $0F                   
F3D2: 08              PHP                         
F3D3: FF ; ????
F3D4: 06 10           ASL     $10                   
F3D6: 09 FF           ORA     #$FF                  
F3D8: 07 ; ????
F3D9: 11 FF           ORA     ($FF),Y               
F3DB: FF ; ????
F3DC: 08              PHP                         
F3DD: 12 ; ????
F3DE: 0B ; ????
F3DF: 01 FF           ORA     ($FF,X)               
F3E1: 13 ; ????
F3E2: 0C ; ????
F3E3: 02 ; ????
F3E4: 0A              ASL     A                   
F3E5: 14 ; ????
F3E6: 0D 03 0B        ORA     $0B03                   
F3E9: 15 0E           ORA     $0E,X                 
F3EB: 04 ; ????
F3EC: 0C ; ????
F3ED: 1C ; ????
F3EE: 0F ; ????
F3EF: 05 0D           ORA     $0D                   
F3F1: 1D 10 06        ORA     $0610,X                 
F3F4: 0E 1E 11        ASL     $111E                   
F3F7: 07 ; ????
F3F8: 0F ; ????
F3F9: 16 12           ASL     $12,X                 
F3FB: 08              PHP                         
F3FC: 10 17           BPL     $F415                   
F3FE: FF ; ????
F3FF: 09 11           ORA     #$11                  
F401: 18              CLC                         
F402: 14 ; ????
F403: 0A              ASL     A                   
F404: FF ; ????
F405: 19 15 0B        ORA     $0B15,Y                 
F408: 13 ; ????
F409: 1A ; ????
F40A: FF ; ????
F40B: 0C ; ????
F40C: 14 ; ????
F40D: 1B ; ????
F40E: 17 ; ????
F40F: 10 FF           BPL     $F410                   
F411: 1F ; ????
F412: 18              CLC                         
F413: 11 16           ORA     ($16),Y               
F415: 20 FF 12        JSR     $12FF                   
F418: 17 ; ????
F419: 21 1A           AND     ($1A,X)               
F41B: 13 ; ????
F41C: FF ; ????
F41D: FF ; ????
F41E: 1B ; ????
F41F: 14 ; ????
F420: 19 FF 1C        ORA     $1CFF,Y                 
F423: 15 1A           ORA     $1A,X                 
F425: FF ; ????
F426: 1D 0D 1B        ORA     $1B0D,X                 
F429: 22 ; ????
F42A: 1E 0E 1C        ASL     $1C0E,X                 
F42D: 23 ; ????
F42E: 1F ; ????
F42F: 0F ; ????
F430: 1D 24 20        ORA     $2024,X                 
F433: 16 1E           ASL     $1E,X                 
F435: FF ; ????
F436: 21 17           AND     ($17,X)               
F438: 1F ; ????
F439: FF ; ????
F43A: FF ; ????
F43B: 18              CLC                         
F43C: 20 FF 23        JSR     $23FF                   
F43F: 1C ; ????
F440: FF ; ????
F441: FF ; ????
F442: 24 1D           BIT     $1D                   
F444: 22 ; ????
F445: 00              BRK                         
F446: FF ; ????
F447: 1E 23 FF        ASL     $FF23,X                 
F44A: 04 ; ????
F44B: 1D 35 55        ORA     $5535,X                 
F44E: 6D 85 98        ADC     $9885                   
F451: 04 ; ????
F452: 10 1D           BPL     $F471                   
F454: 29 35           AND     #$35                  
F456: 41 55           EOR     ($55,X)               
F458: 61 6D           ADC     ($6D,X)               
F45A: 79 85 91        ADC     $9185,Y                 
F45D: 04 ; ????
F45E: 10 1D           BPL     $F47D                   
F460: 29 35           AND     #$35                  
F462: 41 55           EOR     ($55,X)               
F464: 61 6D           ADC     ($6D,X)               
F466: 79 85 91        ADC     $9185,Y                 
F469: 04 ; ????
F46A: 10 1D           BPL     $F489                   
F46C: 29 35           AND     #$35                  
F46E: 41 55           EOR     ($55,X)               
F470: 61 6D           ADC     ($6D,X)               
F472: 79 85 91        ADC     $9185,Y                 
F475: 04 ; ????
F476: 10 29           BPL     $F4A1                   
F478: 41 61           EOR     ($61,X)               
F47A: 79 91 00        ADC     $0091,Y                 
F47D: 00              BRK                         
F47E: 00              BRK                         
F47F: 00              BRK                         
F480: 00              BRK                         
F481: 00              BRK                         
F482: 00              BRK                         
F483: 1E 1E 1E        ASL     $1E1E,X                 
F486: 1E 1E 1E        ASL     $1E1E,X                 
F489: 1E 1E 1E        ASL     $1E1E,X                 
F48C: 1E 1E 1E        ASL     $1E1E,X                 
F48F: 37 ; ????
F490: 37 ; ????
F491: 37 ; ????
F492: 37 ; ????
F493: 37 ; ????
F494: 37 ; ????
F495: 37 ; ????
F496: 37 ; ????
F497: 37 ; ????
F498: 37 ; ????
F499: 37 ; ????
F49A: 37 ; ????
F49B: 50 50           BVC     $F4ED                   
F49D: 50 50           BVC     $F4EF                   
F49F: 50 50           BVC     $F4F1                   
F4A1: 50 50           BVC     $F4F3                   
F4A3: 50 50           BVC     $F4F5                   
F4A5: 50 50           BVC     $F4F7                   
F4A7: 69 69           ADC     #$69                  
F4A9: 69 69           ADC     #$69                  
F4AB: 69 69           ADC     #$69                  
F4AD: 69 01           ADC     #$01                  
F4AF: FF ; ????
F4B0: FF ; ????
F4B1: 07 ; ????
F4B2: 02 ; ????
F4B3: FF ; ????
F4B4: 00              BRK                         
F4B5: 09 03           ORA     #$03                  
F4B7: FF ; ????
F4B8: 01 0B           ORA     ($0B,X)               
F4BA: 04 ; ????
F4BB: FF ; ????
F4BC: 02 ; ????
F4BD: 0D 05 FF        ORA     $FF05                   
F4C0: 03 ; ????
F4C1: 0F ; ????
F4C2: 06 FF           ASL     $FF                   
F4C4: 04 ; ????
F4C5: 11 FF           ORA     ($FF),Y               
F4C7: FF ; ????
F4C8: 05 FF           ORA     $FF                   
F4CA: 08              PHP                         
F4CB: 00              BRK                         
F4CC: FF ; ????
F4CD: FF ; ????
F4CE: 09 FF           ORA     #$FF                  
F4D0: 07 ; ????
F4D1: 14 ; ????
F4D2: 0A              ASL     A                   
F4D3: 01 08           ORA     ($08,X)               
F4D5: FF ; ????
F4D6: 0B ; ????
F4D7: FF ; ????
F4D8: 09 16           ORA     #$16                  
F4DA: 0C ; ????
F4DB: 02 ; ????
F4DC: 0A              ASL     A                   
F4DD: FF ; ????
F4DE: 0D FF 0B        ORA     $0BFF                   
F4E1: 18              CLC                         
F4E2: 0E 03 0C        ASL     $0C03                   
F4E5: FF ; ????
F4E6: 0F ; ????
F4E7: FF ; ????
F4E8: 0D 1A 10        ORA     $101A                   
F4EB: 04 ; ????
F4EC: 0E FF 11        ASL     $11FF                   
F4EF: FF ; ????
F4F0: 0F ; ????
F4F1: 1C ; ????
F4F2: 12 ; ????
F4F3: 05 10           ORA     $10                   
F4F5: FF ; ????
F4F6: FF ; ????
F4F7: FF ; ????
F4F8: 11 1E           ORA     ($1E),Y               
F4FA: 14 ; ????
F4FB: FF ; ????
F4FC: FF ; ????
F4FD: 1F ; ????
F4FE: 15 08           ORA     $08,X                 
F500: 13 ; ????
F501: FF ; ????
F502: 16 FF           ASL     $FF,X                 
F504: 14 ; ????
F505: 21 17           AND     ($17,X)               
F507: 0A              ASL     A                   
F508: 15 FF           ORA     $FF,X                 
F50A: 18              CLC                         
F50B: FF ; ????
F50C: 16 23           ASL     $23,X                 
F50E: 19 0C 17        ORA     $170C,Y                 
F511: FF ; ????
F512: 1A ; ????
F513: FF ; ????
F514: 18              CLC                         
F515: 25 1B           AND     $1B                   
F517: 0E 19 FF        ASL     $FF19                   
F51A: 1C ; ????
F51B: FF ; ????
F51C: 1A ; ????
F51D: 27 ; ????
F51E: 1D 10 1B        ORA     $1B10,X                 
F521: FF ; ????
F522: 1E FF 1C        ASL     $1CFF,X                 
F525: 29 FF           AND     #$FF                  
F527: 12 ; ????
F528: 1D FF 20        ORA     $20FF,X                 
F52B: 13 ; ????
F52C: FF ; ????
F52D: FF ; ????
F52E: 21 FF           AND     ($FF,X)               
F530: 1F ; ????
F531: 2C 22 15        BIT     $1522                   
F534: 20 FF 23        JSR     $23FF                   
F537: FF ; ????
F538: 21 2D           AND     ($2D,X)               
F53A: 24 17           BIT     $17                   
F53C: 22 ; ????
F53D: FF ; ????
F53E: 25 FF           AND     $FF                   
F540: 23 ; ????
F541: 2E 26 19        ROL     $1926                   
F544: 24 FF           BIT     $FF                   
F546: 27 ; ????
F547: FF ; ????
F548: 25 2F           AND     $2F                   
F54A: 28              PLP                         
F54B: 1B ; ????
F54C: 26 FF           ROL     $FF                   
F54E: 29 FF           AND     #$FF                  
F550: 27 ; ????
F551: 30 2A           BMI     $F57D                   
F553: 1D 28 FF        ORA     $FF28,X                 
F556: FF ; ????
F557: FF ; ????
F558: 29 31           AND     #$31                  
F55A: 2C FF FF        BIT     $FFFF                   
F55D: FF ; ????
F55E: 2D 20 2B        AND     $2B20                   
F561: FF ; ????
F562: 2E 22 2C        ROL     $2C22                   
F565: FF ; ????
F566: 2F ; ????
F567: 24 2D           BIT     $2D                   
F569: FF ; ????
F56A: 30 26           BMI     $F592                   
F56C: 2E FF 31        ROL     $31FF                   
F56F: 28              PLP                         
F570: 2F ; ????
F571: FF ; ????
F572: FF ; ????
F573: 2A              ROL     A                   
F574: 30 FF           BMI     $F575                   
F576: 24 3C           BIT     $3C                   
F578: 5D 75 24        EOR     $2475,X                 
F57B: 3C ; ????
F57C: 5D 75 24        EOR     $2475,X                 
F57F: 75 04           ADC     $04,X                 
F581: 95 24           STA     $24,X                 
F583: 3C ; ????
F584: 5D 75 04        EOR     $0475,X                 
F587: 24 75           BIT     $75                   
F589: 95 24           STA     $24,X                 
F58B: 3C ; ????
F58C: 5D 75 24        EOR     $2475,X                 
F58F: 75 03           ADC     $03,X                 
F591: 95 03           STA     $03,X                 
F593: 95 00           STA     $00,X                 
F595: 00              BRK                         
F596: 00              BRK                         
F597: 00              BRK                         
F598: 14 ; ????
F599: 14 ; ????
F59A: 14 ; ????
F59B: 14 ; ????
F59C: 23 ; ????
F59D: 23 ; ????
F59E: 23 ; ????
F59F: 23 ; ????
F5A0: 37 ; ????
F5A1: 37 ; ????
F5A2: 37 ; ????
F5A3: 37 ; ????
F5A4: 46 46           LSR     $46                   
F5A6: 46 46           LSR     $46                   
F5A8: 5A ; ????
F5A9: 5A ; ????
F5AA: 5A ; ????
F5AB: 5A ; ????
F5AC: 69 69           ADC     #$69                  
F5AE: 00              BRK                         
F5AF: 00              BRK                         
F5B0: 69 69           ADC     #$69                  
F5B2: FF ; ????
F5B3: FF ; ????
F5B4: 1A ; ????
F5B5: 04 ; ????
F5B6: 02 ; ????
F5B7: FF ; ????
F5B8: FF ; ????
F5B9: 05 FF           ORA     $FF                   
F5BB: FF ; ????
F5BC: 01 06           ORA     ($06,X)               
F5BE: 1B ; ????
F5BF: FF ; ????
F5C0: FF ; ????
F5C1: 07 ; ????
F5C2: 05 00           ORA     $00                   
F5C4: FF ; ????
F5C5: 08              PHP                         
F5C6: 06 01           ASL     $01                   
F5C8: 04 ; ????
F5C9: 0D 07 02        ORA     $0207                   
F5CC: 05 0E           ORA     $0E                   
F5CE: FF ; ????
F5CF: 03 ; ????
F5D0: 06 09           ASL     $09                   
F5D2: FF ; ????
F5D3: 04 ; ????
F5D4: 0A              ASL     A                   
F5D5: FF ; ????
F5D6: 0B ; ????
F5D7: 07 ; ????
F5D8: FF ; ????
F5D9: FF ; ????
F5DA: 08              PHP                         
F5DB: FF ; ????
F5DC: FF ; ????
F5DD: 10 FF           BPL     $F5DE                   
F5DF: FF ; ????
F5E0: 09 13           ORA     #$13                  
F5E2: 0D FF FF        ORA     $FFFF                   
F5E5: 11 0E           ORA     ($0E),Y               
F5E7: 05 0C           ORA     $0C                   
F5E9: 15 0F           ORA     $0F,X                 
F5EB: 06 0D           ASL     $0D                   
F5ED: 16 FF           ASL     $FF,X                 
F5EF: FF ; ????
F5F0: 0E 12 11        ASL     $1112                   
F5F3: 0A              ASL     A                   
F5F4: FF ; ????
F5F5: FF ; ????
F5F6: FF ; ????
F5F7: 0C ; ????
F5F8: 10 14           BPL     $F60E                   
F5FA: 13 ; ????
F5FB: 0F ; ????
F5FC: FF ; ????
F5FD: 17 ; ????
F5FE: FF ; ????
F5FF: 0B ; ????
F600: 12 ; ????
F601: FF ; ????
F602: 15 11           ORA     $11,X                 
F604: FF ; ????
F605: 18              CLC                         
F606: 16 0D           ASL     $0D,X                 
F608: 14 ; ????
F609: FF ; ????
F60A: 17 ; ????
F60B: 0E 15 FF        ASL     $FF15                   
F60E: FF ; ????
F60F: 12 ; ????
F610: 16 19           ASL     $19,X                 
F612: FF ; ????
F613: 14 ; ????
F614: 1C ; ????
F615: FF ; ????
F616: 1D 17 FF        ORA     $FF17,X                 
F619: FF ; ????
F61A: 00              BRK                         
F61B: FF ; ????
F61C: FF ; ????
F61D: FF ; ????
F61E: FF ; ????
F61F: FF ; ????
F620: 03 ; ????
F621: FF ; ????
F622: 18              CLC                         
F623: FF ; ????
F624: FF ; ????
F625: FF ; ????
F626: FF ; ????
F627: FF ; ????
F628: 19 FF 0C        ORA     $0CFF,Y                 
F62B: 2C 3C 5D        BIT     $5D3C                   
F62E: 6D 8D 0C        ADC     $0C8D                   
F631: 1D 2C 6D        ORA     $6D2C,X                 
F634: 8D 2C 3C        STA     $3C2C                   
F637: 5D 6D 0C        EOR     $0C6D,X                 
F63A: 1D 2C 6D        ORA     $6D2C,X                 
F63D: 7D 8D 0C        ADC     $0C8D,X                 
F640: 1D 2C 3C        ORA     $3C2C,X                 
F643: 5D 6D 7D        EOR     $7D6D,X                 
F646: 8D 0C 3C        STA     $3C0C                   
F649: 5D 8D 7D        EOR     $7D8D,X                 
F64C: 7D 1D 00        ADC     $001D,X                 
F64F: 00              BRK                         
F650: 00              BRK                         
F651: 00              BRK                         
F652: 00              BRK                         
F653: 00              BRK                         
F654: 19 19 19        ORA     $1919,Y                 
F657: 19 19 28        ORA     $2819,Y                 
F65A: 28              PLP                         
F65B: 28              PLP                         
F65C: 28              PLP                         
F65D: 37 ; ????
F65E: 37 ; ????
F65F: 37 ; ????
F660: 37 ; ????
F661: 37 ; ????
F662: 37 ; ????
F663: 50 50           BVC     $F6B5                   
F665: 50 50           BVC     $F6B7                   
F667: 50 50           BVC     $F6B9                   
F669: 50 50           BVC     $F6BB                   
F66B: 69 69           ADC     #$69                  
F66D: 69 69           ADC     #$69                  
F66F: 19 28 28        ORA     $2828,Y                 
F672: 01 FF           ORA     ($FF,X)               
F674: FF ; ????
F675: 06 02           ASL     $02                   
F677: FF ; ????
F678: 00              BRK                         
F679: 08              PHP                         
F67A: 03 ; ????
F67B: FF ; ????
F67C: 01 0C           ORA     ($0C,X)               
F67E: 04 ; ????
F67F: FF ; ????
F680: 02 ; ????
F681: 0D 05 FF        ORA     $FF05                   
F684: 03 ; ????
F685: 09 FF           ORA     #$FF                  
F687: FF ; ????
F688: 04 ; ????
F689: 0A              ASL     A                   
F68A: 07 ; ????
F68B: 00              BRK                         
F68C: FF ; ????
F68D: FF ; ????
F68E: 08              PHP                         
F68F: FF ; ????
F690: 06 23           ASL     $23                   
F692: FF ; ????
F693: 01 07           ORA     ($07,X)               
F695: 0B ; ????
F696: 21 04           AND     ($04,X)               
F698: FF ; ????
F699: 0E FF 05        ASL     $05FF                   
F69C: 21 FF           AND     ($FF,X)               
F69E: 0C ; ????
F69F: 08              PHP                         
F6A0: 23 ; ????
F6A1: 11 0D           ORA     ($0D),Y               
F6A3: 02 ; ????
F6A4: 0B ; ????
F6A5: FF ; ????
F6A6: 0E 03 0C        ASL     $0C03                   
F6A9: FF ; ????
F6AA: 22 ; ????
F6AB: 09 0D           ORA     #$0D                  
F6AD: 12 ; ????
F6AE: 10 FF           BPL     $F6AF                   
F6B0: FF ; ????
F6B1: 15 11           ORA     $11,X                 
F6B3: 23 ; ????
F6B4: 0F ; ????
F6B5: 16 FF           ASL     $FF,X                 
F6B7: 0B ; ????
F6B8: 10 17           BPL     $F6D1                   
F6BA: 13 ; ????
F6BB: 0E FF 1A        ASL     $1AFF                   
F6BE: 14 ; ????
F6BF: 22 ; ????
F6C0: 12 ; ????
F6C1: 1B ; ????
F6C2: FF ; ????
F6C3: FF ; ????
F6C4: 13 ; ????
F6C5: 1C ; ????
F6C6: 16 0F           ASL     $0F,X                 
F6C8: FF ; ????
F6C9: 1D 17 10        ORA     $1017,X                 
F6CC: 15 FF           ORA     $FF,X                 
F6CE: 18              CLC                         
F6CF: 11 16           ORA     ($16),Y               
F6D1: FF ; ????
F6D2: 19 FF 17        ORA     $17FF,Y                 
F6D5: 1E 1A FF        ASL     $FF1A,X                 
F6D8: 18              CLC                         
F6D9: 1F ; ????
F6DA: 1B ; ????
F6DB: 12 ; ????
F6DC: 19 FF 1C        ORA     $1CFF,Y                 
F6DF: 13 ; ????
F6E0: 1A ; ????
F6E1: FF ; ????
F6E2: FF ; ????
F6E3: 14 ; ????
F6E4: 1B ; ????
F6E5: 20 1E 15        JSR     $151E                   
F6E8: FF ; ????
F6E9: FF ; ????
F6EA: 1F ; ????
F6EB: 18              CLC                         
F6EC: 1D FF 20        ORA     $20FF,X                 
F6EF: 19 1E FF        ORA     $FF1E,Y                 
F6F2: FF ; ????
F6F3: 1C ; ????
F6F4: 1F ; ????
F6F5: FF ; ????
F6F6: 0A              ASL     A                   
F6F7: FF ; ????
F6F8: 09 22           ORA     #$22                  
F6FA: FF ; ????
F6FB: 21 0E           AND     ($0E,X)               
F6FD: 13 ; ????
F6FE: 0B ; ????
F6FF: 07 ; ????
F700: FF ; ????
F701: 10 04           BPL     $F707                   
F703: 2D 3C 5D        AND     $5D3C                   
F706: 6D 95 04        ADC     $0495                   
F709: 2D 3C 4C        AND     $4C3C                   
F70C: 5D 6D 95        EOR     $956D,X                 
F70F: 04 ; ????
F710: 2D 4C 6D        AND     $6D4C                   
F713: 95 04           STA     $04,X                 
F715: 1C ; ????
F716: 2D 6D 7D        AND     $7D6D                   
F719: 95 2D           STA     $2D,X                 
F71B: 4C 6D 1C        JMP     $1C6D                   
F71E: 2D 4C 6D        AND     $6D4C                   
F721: 7D 00 00        ADC     $0000,X                 
F724: 00              BRK                         
F725: 00              BRK                         
F726: 00              BRK                         
F727: 00              BRK                         
F728: 14 ; ????
F729: 14 ; ????
F72A: 14 ; ????
F72B: 14 ; ????
F72C: 14 ; ????
F72D: 14 ; ????
F72E: 14 ; ????
F72F: 28              PLP                         
F730: 28              PLP                         
F731: 28              PLP                         
F732: 28              PLP                         
F733: 28              PLP                         
F734: 3C ; ????
F735: 3C ; ????
F736: 3C ; ????
F737: 3C ; ????
F738: 3C ; ????
F739: 3C ; ????
F73A: 55 55           EOR     $55,X                 
F73C: 55 69           EOR     $69,X                 
F73E: 69 69           ADC     #$69                  
F740: 69 69           ADC     #$69                  
F742: 01 FF           ORA     ($FF,X)               
F744: FF ; ????
F745: 06 02           ASL     $02                   
F747: FF ; ????
F748: 00              BRK                         
F749: 07 ; ????
F74A: 03 ; ????
F74B: FF ; ????
F74C: 01 08           ORA     ($08,X)               
F74E: 04 ; ????
F74F: FF ; ????
F750: 02 ; ????
F751: 0A              ASL     A                   
F752: 05 FF           ORA     $FF                   
F754: 03 ; ????
F755: 0B ; ????
F756: FF ; ????
F757: FF ; ????
F758: 04 ; ????
F759: 0C ; ????
F75A: 07 ; ????
F75B: 00              BRK                         
F75C: FF ; ????
F75D: 0D 08 01        ORA     $0108                   
F760: 06 0E           ASL     $0E                   
F762: 09 02           ORA     #$02                  
F764: 07 ; ????
F765: FF ; ????
F766: 0A              ASL     A                   
F767: FF ; ????
F768: 08              PHP                         
F769: 0F ; ????
F76A: 0B ; ????
F76B: 03 ; ????
F76C: 09 FF           ORA     #$FF                  
F76E: 0C ; ????
F76F: 04 ; ????
F770: 0A              ASL     A                   
F771: 10 FF           BPL     $F772                   
F773: 05 0B           ORA     $0B                   
F775: 11 0E           ORA     ($0E),Y               
F777: 06 FF           ASL     $FF                   
F779: 12 ; ????
F77A: 0F ; ????
F77B: 07 ; ????
F77C: 0D 14 10        ORA     $1014                   
F77F: 09 0E           ORA     #$0E                  
F781: FF ; ????
F782: 11 0B           ORA     ($0B),Y               
F784: 0F ; ????
F785: 15 FF           ORA     $FF,X                 
F787: 0C ; ????
F788: 10 17           BPL     $F7A1                   
F78A: 13 ; ????
F78B: 0D FF FF        ORA     $FFFF                   
F78E: 14 ; ????
F78F: FF ; ????
F790: 12 ; ????
F791: 1B ; ????
F792: FF ; ????
F793: 0E 13 FF        ASL     $FF13                   
F796: 16 10           ASL     $10,X                 
F798: FF ; ????
F799: FF ; ????
F79A: 17 ; ????
F79B: FF ; ????
F79C: 15 1F           ORA     $1F,X                 
F79E: FF ; ????
F79F: 11 16           ORA     ($16),Y               
F7A1: FF ; ????
F7A2: 19 FF FF        ORA     $FFFF,Y                 
F7A5: 1C ; ????
F7A6: 1A ; ????
F7A7: FF ; ????
F7A8: 18              CLC                         
F7A9: 1D FF FF        ORA     $FFFF,X                 
F7AC: 19 1E 1C        ORA     $1C1E,Y                 
F7AF: 13 ; ????
F7B0: FF ; ????
F7B1: FF ; ????
F7B2: 1D 18 1B        ORA     $1B18,X                 
F7B5: FF ; ????
F7B6: 1E 19 1C        ASL     $1C19,X                 
F7B9: FF ; ????
F7BA: 1F ; ????
F7BB: 1A ; ????
F7BC: 1D FF FF        ORA     $FFFF,X                 
F7BF: 16 1E           ASL     $1E,X                 
F7C1: FF ; ????

F7C2: 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F7D0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F7E0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F7F0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00