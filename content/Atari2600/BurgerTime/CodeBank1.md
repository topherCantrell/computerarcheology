![Burger Time](A2600BT.jpg)

# Burger Time Bank 1

>>> cpu 6502

>>> memoryTable hard 
[Hardware Info](../Stella.md)

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

Bank 1 and 3 have the same data.

```code
F000: 01 02 04 08 B6 F3 AE F4 B2 F5 72 F6 42 F7 6C F3
F010: 4A F4 76 F5 2A F6 02 F7 91 F3 7C F4 94 F5 4E F6
F020: 22 F7 08 05 00 FB F8 FB 00 05 08 00 02 02 03 03
F030: 04 04 04 04

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

F12E: 80  40                         

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

F32A: 4D 41 4D 4D 4C 69 69 5A 69 69 01 19 21 09 00 2C
F33A: 31 05 1A 18 1D 03 00 1D 20 05 00 1B 1F 05 00 00
F34A: 0F 00 00               

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

F36C: 4D 08 1D 2C 3C 4D 5D 6D 7D 91 08 1D 2C 3C 4D 5D
F37C: 6D 7D 91 08 1D 2C 6D 7D 91 08 1D 2C 3C 4D 5D 6D
F38C: 7D 91 3C 4D 5D 69 00 00 00 00 00 00 00 00 00 14
F39C: 14 14 14 14 14 14 14 14 28 28 28 28 28 28 3C 3C
F3AC: 3C 3C 3C 3C 3C 3C 3C 50 50 50 FF 23 FF FF 02 FF
F3BC: FF 0A 03 FF 01 0B 04 FF 02 0C 05 FF 03 0D 06 FF
F3CC: 04 0E 07 FF 05 0F 08 FF 06 10 09 FF 07 11 FF FF
F3DC: 08 12 0B 01 FF 13 0C 02 0A 14 0D 03 0B 15 0E 04
F3EC: 0C 1C 0F 05 0D 1D 10 06 0E 1E 11 07 0F 16 12 08
F3FC: 10 17 FF 09 11 18 14 0A FF 19 15 0B 13 1A FF 0C
F40C: 14 1B 17 10 FF 1F 18 11 16 20 FF 12 17 21 1A 13
F41C: FF FF 1B 14 19 FF 1C 15 1A FF 1D 0D 1B 22 1E 0E
F42C: 1C 23 1F 0F 1D 24 20 16 1E FF 21 17 1F FF FF 18
F43C: 20 FF 23 1C FF FF 24 1D 22 00 FF 1E 23 FF 04 1D
F44C: 35 55 6D 85 98 04 10 1D 29 35 41 55 61 6D 79 85
F45C: 91 04 10 1D 29 35 41 55 61 6D 79 85 91 04 10 1D
F46C: 29 35 41 55 61 6D 79 85 91 04 10 29 41 61 79 91
F47C: 00 00 00 00 00 00 00 1E 1E 1E 1E 1E 1E 1E 1E 1E
F48C: 1E 1E 1E 37 37 37 37 37 37 37 37 37 37 37 37 50
F49C: 50 50 50 50 50 50 50 50 50 50 50 69 69 69 69 69
F4AC: 69 69 01 FF FF 07 02 FF 00 09 03 FF 01 0B 04 FF
F4BC: 02 0D 05 FF 03 0F 06 FF 04 11 FF FF 05 FF 08 00
F4CC: FF FF 09 FF 07 14 0A 01 08 FF 0B FF 09 16 0C 02
F4DC: 0A FF 0D FF 0B 18 0E 03 0C FF 0F FF 0D 1A 10 04
F4EC: 0E FF 11 FF 0F 1C 12 05 10 FF FF FF 11 1E 14 FF
F4FC: FF 1F 15 08 13 FF 16 FF 14 21 17 0A 15 FF 18 FF
F50C: 16 23 19 0C 17 FF 1A FF 18 25 1B 0E 19 FF 1C FF
F51C: 1A 27 1D 10 1B FF 1E FF 1C 29 FF 12 1D FF 20 13
F52C: FF FF 21 FF 1F 2C 22 15 20 FF 23 FF 21 2D 24 17
F53C: 22 FF 25 FF 23 2E 26 19 24 FF 27 FF 25 2F 28 1B
F54C: 26 FF 29 FF 27 30 2A 1D 28 FF FF FF 29 31 2C FF
F55C: FF FF 2D 20 2B FF 2E 22 2C FF 2F 24 2D FF 30 26
F56C: 2E FF 31 28 2F FF FF 2A 30 FF 24 3C 5D 75 24 3C
F57C: 5D 75 24 75 04 95 24 3C 5D 75 04 24 75 95 24 3C
F58C: 5D 75 24 75 03 95 03 95 00 00 00 00 14 14 14 14
F59C: 23 23 23 23 37 37 37 37 46 46 46 46 5A 5A 5A 5A
F5AC: 69 69 00 00 69 69 FF FF 1A 04 02 FF FF 05 FF FF
F5BC: 01 06 1B FF FF 07 05 00 FF 08 06 01 04 0D 07 02
F5CC: 05 0E FF 03 06 09 FF 04 0A FF 0B 07 FF FF 08 FF
F5DC: FF 10 FF FF 09 13 0D FF FF 11 0E 05 0C 15 0F 06
F5EC: 0D 16 FF FF 0E 12 11 0A FF FF FF 0C 10 14 13 0F
F5FC: FF 17 FF 0B 12 FF 15 11 FF 18 16 0D 14 FF 17 0E
F60C: 15 FF FF 12 16 19 FF 14 1C FF 1D 17 FF FF 00 FF
F61C: FF FF FF FF 03 FF 18 FF FF FF FF FF 19 FF 0C 2C
F62C: 3C 5D 6D 8D 0C 1D 2C 6D 8D 2C 3C 5D 6D 0C 1D 2C
F63C: 6D 7D 8D 0C 1D 2C 3C 5D 6D 7D 8D 0C 3C 5D 8D 7D
F64C: 7D 1D 00 00 00 00 00 00 19 19 19 19 19 28 28 28
F65C: 28 37 37 37 37 37 37 50 50 50 50 50 50 50 50 69
F66C: 69 69 69 19 28 28 01 FF FF 06 02 FF 00 08 03 FF
F67C: 01 0C 04 FF 02 0D 05 FF 03 09 FF FF 04 0A 07 00
F68C: FF FF 08 FF 06 23 FF 01 07 0B 21 04 FF 0E FF 05
F69C: 21 FF 0C 08 23 11 0D 02 0B FF 0E 03 0C FF 22 09
F6AC: 0D 12 10 FF FF 15 11 23 0F 16 FF 0B 10 17 13 0E
F6BC: FF 1A 14 22 12 1B FF FF 13 1C 16 0F FF 1D 17 10
F6CC: 15 FF 18 11 16 FF 19 FF 17 1E 1A FF 18 1F 1B 12
F6DC: 19 FF 1C 13 1A FF FF 14 1B 20 1E 15 FF FF 1F 18
F6EC: 1D FF 20 19 1E FF FF 1C 1F FF 0A FF 09 22 FF 21
F6FC: 0E 13 0B 07 FF 10 04 2D 3C 5D 6D 95 04 2D 3C 4C
F70C: 5D 6D 95 04 2D 4C 6D 95 04 1C 2D 6D 7D 95 2D 4C
F71C: 6D 1C 2D 4C 6D 7D 00 00 00 00 00 00 14 14 14 14
F72C: 14 14 14 28 28 28 28 28 3C 3C 3C 3C 3C 3C 55 55
F73C: 55 69 69 69 69 69 01 FF FF 06 02 FF 00 07 03 FF
F74C: 01 08 04 FF 02 0A 05 FF 03 0B FF FF 04 0C 07 00
F75C: FF 0D 08 01 06 0E 09 02 07 FF 0A FF 08 0F 0B 03
F76C: 09 FF 0C 04 0A 10 FF 05 0B 11 0E 06 FF 12 0F 07
F77C: 0D 14 10 09 0E FF 11 0B 0F 15 FF 0C 10 17 13 0D
F78C: FF FF 14 FF 12 1B FF 0E 13 FF 16 10 FF FF 17 FF
F79C: 15 1F FF 11 16 FF 19 FF FF 1C 1A FF 18 1D FF FF
F7AC: 19 1E 1C 13 FF FF 1D 18 1B FF 1E 19 1C FF 1F 1A
F7BC: 1D FF FF 16 1E FF 00 00 00 00 00 00 00 00 00 00
F7CC: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F7DC: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F7EC: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F7FC: 00 00 00 00
```