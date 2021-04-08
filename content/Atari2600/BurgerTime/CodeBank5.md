![Burger Time](A2600BT.jpg)

# Burger Time Bank 5

>>> cpu 6502

>>> memoryTable hard 
[Hardware Info](../Stella.md)

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

```code
F000: AD E8 FF        LDA     $FFE8                   ; Switch in RAM bank 0
F003: A2 FD           LDX     #$FD                  ; Start clearing below the return address on the stack
F005: A9 00           LDA     #$00                  ; Set ...
F007: 8D 81 02        STA     $0281                   ; ... port A all inputs
F00A: 8D 83 02        STA     $0283                   ; ... port B all inputs
F00D: 95 00           STA     $00,X                 ; Clear ...
F00F: CA              DEX                         ; ... RAM and ...
F010: D0 FB           BNE     $F00D                   ; ... TIA
F012: A2 FF           LDX     #$FF                  
F014: 8E 48 F8        STX     $F848                   
F017: 20 56 F0        JSR     $F056                   
F01A: A9 00           LDA     #$00                  
F01C: 8D 55 F8        STA     $F855                   
F01F: 20 89 F0        JSR     $F089                   
F022: AE 55 F9        LDX     $F955                   
F025: BD FE F3        LDA     $F3FE,X                 
F028: 8D 0F F8        STA     $F80F                   
F02B: 85 2C           STA     $2C                   
F02D: A9 FF           LDA     #$FF                  
F02F: 85 DE           STA     $DE                   
F031: 20 D9 F2        JSR     $F2D9                   
F034: 20 FF F2        JSR     $F2FF                   
F037: 20 64 F5        JSR     $F564                   
F03A: AD 82 02        LDA     $0282                   
F03D: 8D 09 F8        STA     $F809                   
F040: A9 00           LDA     #$00                  
F042: 8D 08 F8        STA     $F808                   
F045: 20 0C F6        JSR     $F60C                   
F048: A9 01           LDA     #$01                  
F04A: 8D 08 F8        STA     $F808                   
F04D: 20 0C F6        JSR     $F60C                   
F050: A9 00           LDA     #$00                  
F052: 8D 08 F8        STA     $F808                   
F055: 60              RTS                         
F056: A2 FF           LDX     #$FF                  
F058: A9 00           LDA     #$00                  
F05A: 9D 00 F8        STA     $F800,X                 
F05D: CA              DEX                         
F05E: D0 FA           BNE     $F05A                   
F060: 8D 00 F8        STA     $F800                   
F063: A9 12           LDA     #$12                  
F065: 8D 88 F8        STA     $F888                   
F068: A9 0C           LDA     #$0C                  
F06A: 8D 89 F8        STA     $F889                   
F06D: A9 05           LDA     #$05                  
F06F: 8D 57 F8        STA     $F857                   
F072: 8D 58 F8        STA     $F858                   
F075: A9 00           LDA     #$00                  
F077: 8D 40 F8        STA     $F840                   
F07A: A9 10           LDA     #$10                  
F07C: 85 DF           STA     $DF                   
F07E: A9 04           LDA     #$04                  
F080: 8D 15 F8        STA     $F815                   
F083: A9 0F           LDA     #$0F                  
F085: 8D 87 F8        STA     $F887                   
F088: 60              RTS                         
F089: AE 55 F9        LDX     $F955                   
F08C: BD A7 F1        LDA     $F1A7,X                 
F08F: 85 B1           STA     $B1                   
F091: BD AC F1        LDA     $F1AC,X                 
F094: AA              TAX                         
F095: A0 0D           LDY     #$0D                  
F097: BD B1 F1        LDA     $F1B1,X                 
F09A: 99 B9 00        STA     $00B9,Y                 
F09D: CA              DEX                         
F09E: 88              DEY                         
F09F: 10 F6           BPL     $F097                   
F0A1: AC 55 F9        LDY     $F955                   
F0A4: BE A2 F1        LDX     $F1A2,Y                 
F0A7: A0 03           LDY     #$03                  
F0A9: BD F7 F1        LDA     $F1F7,X                 
F0AC: 99 51 F8        STA     $F851,Y                 
F0AF: CA              DEX                         
F0B0: 88              DEY                         
F0B1: 10 F6           BPL     $F0A9                   
F0B3: AE 55 F9        LDX     $F955                   
F0B6: A0 00           LDY     #$00                  
F0B8: BD 0B F2        LDA     $F20B,X                 
F0BB: 99 8D 00        STA     $008D,Y                 
F0BE: BD 10 F2        LDA     $F210,X                 
F0C1: 99 92 00        STA     $0092,Y                 
F0C4: BD 15 F2        LDA     $F215,X                 
F0C7: 99 97 00        STA     $0097,Y                 
F0CA: BD 1A F2        LDA     $F21A,X                 
F0CD: 99 9C 00        STA     $009C,Y                 
F0D0: 8A              TXA                         
F0D1: 18              CLC                         
F0D2: 69 14           ADC     #$14                  
F0D4: AA              TAX                         
F0D5: C8              INY                         
F0D6: C0 04           CPY     #$04                  
F0D8: D0 DE           BNE     $F0B8                   
F0DA: AE 55 F9        LDX     $F955                   
F0DD: BD 5B F2        LDA     $F25B,X                 
F0E0: 85 A1           STA     $A1                   
F0E2: 85 A2           STA     $A2                   
F0E4: 85 A3           STA     $A3                   
F0E6: 85 A4           STA     $A4                   
F0E8: BD 60 F2        LDA     $F260,X                 
F0EB: 85 A5           STA     $A5                   
F0ED: 85 A6           STA     $A6                   
F0EF: 85 A7           STA     $A7                   
F0F1: 85 A8           STA     $A8                   
F0F3: BD 65 F2        LDA     $F265,X                 
F0F6: 85 A9           STA     $A9                   
F0F8: 85 AA           STA     $AA                   
F0FA: 85 AB           STA     $AB                   
F0FC: 85 AC           STA     $AC                   
F0FE: BD 6A F2        LDA     $F26A,X                 
F101: 85 AD           STA     $AD                   
F103: 85 AE           STA     $AE                   
F105: 85 AF           STA     $AF                   
F107: 85 B0           STA     $B0                   
F109: A2 13           LDX     #$13                  
F10B: A9 00           LDA     #$00                  
F10D: 9D 72 F8        STA     $F872,X                 
F110: 9D 1A F8        STA     $F81A,X                 
F113: CA              DEX                         
F114: 10 F7           BPL     $F10D                   
F116: 8D 86 F8        STA     $F886                   
F119: 8D 36 F8        STA     $F836                   
F11C: 8D 40 F8        STA     $F840                   
F11F: 8D 5A F8        STA     $F85A                   
F122: 8D 4B F8        STA     $F84B                   
F125: 8D 59 F8        STA     $F859                   
F128: AE 55 F9        LDX     $F955                   
F12B: BD FE F3        LDA     $F3FE,X                 
F12E: 8D 0F F8        STA     $F80F                   
F131: 8D 10 F8        STA     $F810                   
F134: AE 8A F9        LDX     $F98A                   
F137: BD 89 F1        LDA     $F189,X                 
F13A: 8D 87 F8        STA     $F887                   
F13D: BD 57 F1        LDA     $F157,X                 
F140: 8D 88 F8        STA     $F888                   
F143: BD 70 F1        LDA     $F170,X                 
F146: 8D 89 F8        STA     $F889                   
F149: A5 DF           LDA     $DF                   
F14B: 29 0F           AND     #$0F                  
F14D: 09 10           ORA     #$10                  
F14F: 85 DF           STA     $DF                   
F151: A9 04           LDA     #$04                  
F153: 8D 4D F8        STA     $F84D                   
F156: 60              RTS                         
F157: 0F ; ????
F158: 12 ; ????
F159: 17 ; ????
F15A: 19 1C 1E        ORA     $1E1C,Y                 
F15D: 20 22 24        JSR     $2422                   
F160: 26 28           ROL     $28                   
F162: 2A              ROL     A                   
F163: 2C 2E 30        BIT     $302E                   
F166: 32 ; ????
F167: 34 ; ????
F168: 36 38           ROL     $38,X                 
F16A: 3A ; ????
F16B: 3A ; ????
F16C: 3A ; ????
F16D: 3A ; ????
F16E: 3A ; ????
F16F: 3A ; ????
F170: 0C ; ????
F171: 0F ; ????
F172: 12 ; ????
F173: 17 ; ????
F174: 19 1B 1D        ORA     $1D1B,Y                 
F177: 1F ; ????
F178: 21 23           AND     ($23,X)               
F17A: 25 27           AND     $27                   
F17C: 29 2B           AND     #$2B                  
F17E: 2D 2F 31        AND     $312F                   
F181: 33 ; ????
F182: 35 37           AND     $37,X                 
F184: 37 ; ????
F185: 37 ; ????
F186: 37 ; ????
F187: 37 ; ????
F188: 37 ; ????
F189: FF ; ????
F18A: 7F ; ????
F18B: 7F ; ????
F18C: 7F ; ????
F18D: 7F ; ????
F18E: 6F ; ????
F18F: 6F ; ????
F190: 6F ; ????
F191: 6F ; ????
F192: 6F ; ????
F193: 4F ; ????
F194: 4F ; ????
F195: 4F ; ????
F196: 4F ; ????
F197: 4F ; ????
F198: 0F ; ????
F199: 0F ; ????
F19A: 0F ; ????
F19B: 0F ; ????
F19C: 0F ; ????
F19D: F0 F0           BEQ     $F18F                   
F19F: F0 F0           BEQ     $F191                   
F1A1: 0F ; ????
F1A2: 03 ; ????
F1A3: 07 ; ????
F1A4: 0B ; ????
F1A5: 0F ; ????
F1A6: 13 ; ????
F1A7: 01 00           ORA     ($00,X)               
F1A9: 01 01           ORA     ($01,X)               
F1AB: 01 0D           ORA     ($0D,X)               
F1AD: 1B ; ????
F1AE: 29 37           AND     #$37                  
F1B0: 45 00           EOR     $00                   
F1B2: 06 06           ASL     $06                   
F1B4: 00              BRK                         
F1B5: 4D 08 4D        EOR     $4D08                   
F1B8: 7D 3C 69        ADC     $693C,X                 
F1BB: 14 ; ????
F1BC: 14 ; ????
F1BD: 14 ; ????
F1BE: 3C ; ????
F1BF: 00              BRK                         
F1C0: 02 ; ????
F1C1: 04 ; ????
F1C2: 04 ; ????
F1C3: 41 12           EOR     ($12,X)               
F1C5: 41 79           EOR     ($79,X)               
F1C7: 29 69           AND     #$69                  
F1C9: 00              BRK                         
F1CA: 37 ; ????
F1CB: 69 69           ADC     #$69                  
F1CD: 06 00           ASL     $00                   
F1CF: 02 ; ????
F1D0: 04 ; ????
F1D1: 4D 04 50        EOR     $5004                   
F1D4: 3C ; ????
F1D5: 95 5A           STA     $5A,X                 
F1D7: 3C ; ????
F1D8: 14 ; ????
F1D9: 5A ; ????
F1DA: 23 ; ????
F1DB: 00              BRK                         
F1DC: 00              BRK                         
F1DD: 06 04           ASL     $04                   
F1DF: 4D 0C 0C        EOR     $0C0C                   
F1E2: 6D 8D 69        ADC     $698D                   
F1E5: 69 19           ADC     #$19                  
F1E7: 19 69 00        ORA     $0069,Y                 
F1EA: 06 06           ASL     $06                   
F1EC: 04 ; ????
F1ED: 4C 04 04        JMP     $0404                   
F1F0: 95 95           STA     $95,X                 
F1F2: 69 3C           ADC     #$3C                  
F1F4: 14 ; ????
F1F5: 14 ; ????
F1F6: 3C ; ????
F1F7: 0B ; ????
F1F8: 1D 17 1D        ORA     $1D17,X                 
F1FB: 01 0C           ORA     ($0C,X)               
F1FD: 2F ; ????
F1FE: 2C 10 06        BIT     $0610                   
F201: 0D 09 1E        ORA     $1E09                   
F204: 07 ; ????
F205: 0E 1F 13        ASL     $131F                   
F208: 0D 11 16        ORA     $1611                   
F20B: 73 ; ????
F20C: 73 ; ????
F20D: 73 ; ????
F20E: 73 ; ????
F20F: 73 ; ????
F210: 73 ; ????
F211: 73 ; ????
F212: 73 ; ????
F213: 73 ; ????
F214: 73 ; ????
F215: 73 ; ????
F216: 73 ; ????
F217: 73 ; ????
F218: 73 ; ????
F219: 73 ; ????
F21A: 73 ; ????
F21B: 73 ; ????
F21C: 73 ; ????
F21D: 73 ; ????
F21E: 73 ; ????
F21F: 5F ; ????
F220: 55 50           EOR     $50,X                 
F222: 5A ; ????
F223: 5F ; ????
F224: 5F ; ????
F225: 55 5F           EOR     $5F,X                 
F227: 4B ; ????
F228: 5F ; ????
F229: 5F ; ????
F22A: 55 5F           EOR     $5F,X                 
F22C: 5A ; ????
F22D: 5F ; ????
F22E: 5F ; ????
F22F: 55 50           EOR     $50,X                 
F231: 5A ; ????
F232: 5F ; ????
F233: 4B ; ????
F234: 3C ; ????
F235: 2D 3C 37        AND     $373C                   
F238: 37 ; ????
F239: 3C ; ????
F23A: 3C ; ????
F23B: 23 ; ????
F23C: 4B ; ????
F23D: 4B ; ????
F23E: 3C ; ????
F23F: 3C ; ????
F240: 3C ; ????
F241: 37 ; ????
F242: 4B ; ????
F243: 3C ; ????
F244: 2D 23 37        AND     $3723                   
F247: 37 ; ????
F248: 23 ; ????
F249: 0A              ASL     A                   
F24A: 23 ; ????
F24B: 0A              ASL     A                   
F24C: 23 ; ????
F24D: 23 ; ????
F24E: 19 0A 1E        ORA     $1E0A,Y                 
F251: 37 ; ????
F252: 23 ; ????
F253: 19 23 0A        ORA     $0A23,Y                 
F256: 37 ; ????
F257: 23 ; ????
F258: 0A              ASL     A                   
F259: 0A              ASL     A                   
F25A: 0A              ASL     A                   
F25B: 3C ; ????
F25C: 3C ; ????
F25D: F0 3C           BEQ     $F29B                   
F25F: 3C ; ????
F260: 3C ; ????
F261: 78              SEI                         
F262: 3C ; ????
F263: 3C ; ????
F264: 3C ; ????
F265: 3C ; ????
F266: 3C ; ????
F267: 0F ; ????
F268: 3C ; ????
F269: 3C ; ????
F26A: 78              SEI                         
F26B: 78              SEI                         
F26C: 3C ; ????
F26D: 3C ; ????
F26E: 1E 97 F2        ASL     $F297,X                 
F271: 9C ; ????
F272: F2 ; ????
F273: 97 ; ????
F274: F2 ; ????
F275: 97 ; ????
F276: F2 ; ????
F277: A1 F2           LDA     ($F2,X)               
F279: A1 F2           LDA     ($F2,X)               
F27B: A1 F2           LDA     ($F2,X)               
F27D: A1 F2           LDA     ($F2,X)               
F27F: A7 ; ????
F280: F2 ; ????
F281: AC F2 AC        LDY     $ACF2                   
F284: F2 ; ????
F285: A7 ; ????
F286: F2 ; ????
F287: B1 F2           LDA     ($F2),Y               
F289: B8              CLV                         
F28A: F2 ; ????
F28B: B1 F2           LDA     ($F2),Y               
F28D: C9 F2           CMP     #$F2                  
F28F: BD F2 C3        LDA     $C3F2,X                 
F292: F2 ; ????
F293: BD F2 BD        LDA     $BDF2,X                 
F296: F2 ; ????
F297: 73 ; ????
F298: 5F ; ????
F299: 4B ; ????
F29A: 37 ; ????
F29B: 00              BRK                         
F29C: 73 ; ????
F29D: 5F ; ????
F29E: 37 ; ????
F29F: 23 ; ????
F2A0: 00              BRK                         
F2A1: 73 ; ????
F2A2: 55 3C           EOR     $3C,X                 
F2A4: 23 ; ????
F2A5: 0A              ASL     A                   
F2A6: 00              BRK                         
F2A7: 73 ; ????
F2A8: 50 2D           BVC     $F2D7                   
F2AA: 0A              ASL     A                   
F2AB: 00              BRK                         
F2AC: 73 ; ????
F2AD: 5F ; ????
F2AE: 3C ; ????
F2AF: 19 00 73        ORA     $7300,Y                 
F2B2: 5A ; ????
F2B3: 4B ; ????
F2B4: 3C ; ????
F2B5: 23 ; ????
F2B6: 0A              ASL     A                   
F2B7: 00              BRK                         
F2B8: 73 ; ????
F2B9: 4B ; ????
F2BA: 23 ; ????
F2BB: 0A              ASL     A                   
F2BC: 00              BRK                         
F2BD: 73 ; ????
F2BE: 5F ; ????
F2BF: 4B ; ????
F2C0: 37 ; ????
F2C1: 0A              ASL     A                   
F2C2: 00              BRK                         
F2C3: 73 ; ????
F2C4: 5F ; ????
F2C5: 4B ; ????
F2C6: 1E 0A 00        ASL     $000A,X                 
F2C9: 73 ; ????
F2CA: 5A ; ????
F2CB: 3C ; ????
F2CC: 23 ; ????
F2CD: 0A              ASL     A                   
F2CE: 00              BRK                         
F2CF: 1E 15 00        ASL     $0015,X                 
F2D2: EB ; ????
F2D3: E2 ; ????
F2D4: EB ; ????
F2D5: 00              BRK                         
F2D6: 15 10           ORA     $10,X                 
F2D8: 15 AD           ORA     $AD,X                 
F2DA: 48              PHA                         
F2DB: F9 30 0F        SBC     $0F30,Y                 
F2DE: A8              TAY                         
F2DF: B9 CF F2        LDA     $F2CF,Y                 
F2E2: 8D 0A F8        STA     $F80A                   
F2E5: B9 D1 F2        LDA     $F2D1,Y                 
F2E8: 0A              ASL     A                   
F2E9: 8D 0B F8        STA     $F80B                   
F2EC: 60              RTS                         
F2ED: A9 00           LDA     #$00                  
F2EF: 8D 0A F8        STA     $F80A                   
F2F2: 8D 0B F8        STA     $F80B                   
F2F5: 60              RTS                         
F2F6: 4C 82 F3        JMP     $F382                   
F2F9: 4C 7A F3        JMP     $F37A                   
F2FC: 4C FD F3        JMP     $F3FD                   
F2FF: A5 BD           LDA     $BD                   
F301: 8D C8 00        STA     $00C8                   
F304: AD 0A F9        LDA     $F90A                   
F307: 20 0D F4        JSR     $F40D                   
F30A: 18              CLC                         
F30B: 65 BD           ADC     $BD                   
F30D: 85 BD           STA     $BD                   
F30F: C9 02           CMP     #$02                  
F311: F0 E6           BEQ     $F2F9                   
F313: C9 9A           CMP     #$9A                  
F315: F0 E2           BEQ     $F2F9                   
F317: AD 48 F9        LDA     $F948                   
F31A: 30 E0           BMI     $F2FC                   
F31C: C9 04           CMP     #$04                  
F31E: F0 11           BEQ     $F331                   
F320: C9 02           CMP     #$02                  
F322: F0 D2           BEQ     $F2F6                   
F324: C9 06           CMP     #$06                  
F326: F0 CE           BEQ     $F2F6                   
F328: A5 BD           LDA     $BD                   
F32A: 18              CLC                         
F32B: 69 06           ADC     #$06                  
F32D: AA              TAX                         
F32E: 4C 33 F3        JMP     $F333                   
F331: A6 BD           LDX     $BD                   
F333: 38              SEC                         
F334: A9 69           LDA     #$69                  
F336: E5 C2           SBC     $C2                   
F338: A8              TAY                         
F339: CC 0F F9        CPY     $F90F                   
F33C: F0 37           BEQ     $F375                   
F33E: 38              SEC                         
F33F: ED 0F F9        SBC     $F90F                   
F342: 18              CLC                         
F343: 69 02           ADC     #$02                  
F345: C9 05           CMP     #$05                  
F347: 90 03           BCC     $F34C                   
F349: 4C 58 F3        JMP     $F358                   
F34C: A9 69           LDA     #$69                  
F34E: 38              SEC                         
F34F: ED 0F F9        SBC     $F90F                   
F352: 85 C2           STA     $C2                   
F354: A8              TAY                         
F355: 4C 75 F3        JMP     $F375                   
F358: CC 10 F9        CPY     $F910                   
F35B: F0 18           BEQ     $F375                   
F35D: 98              TYA                         
F35E: 38              SEC                         
F35F: ED 10 F9        SBC     $F910                   
F362: 18              CLC                         
F363: 69 02           ADC     #$02                  
F365: C9 05           CMP     #$05                  
F367: 90 03           BCC     $F36C                   
F369: 4C F9 F2        JMP     $F2F9                   
F36C: A9 69           LDA     #$69                  
F36E: 38              SEC                         
F36F: ED 10 F9        SBC     $F910                   
F372: A8              TAY                         
F373: 85 C2           STA     $C2                   
F375: 20 6C F4        JSR     $F46C                   
F378: B0 05           BCS     $F37F                   
F37A: AD C8 00        LDA     $00C8                   
F37D: 85 BD           STA     $BD                   
F37F: 4C FD F3        JMP     $F3FD                   
F382: A5 C2           LDA     $C2                   
F384: 8D C8 00        STA     $00C8                   
F387: AD 0B F9        LDA     $F90B                   
F38A: 20 0D F4        JSR     $F40D                   
F38D: 18              CLC                         
F38E: 65 C2           ADC     $C2                   
F390: 85 C2           STA     $C2                   
F392: AD 48 F9        LDA     $F948                   
F395: 30 66           BMI     $F3FD                   
F397: C9 02           CMP     #$02                  
F399: F0 2D           BEQ     $F3C8                   
F39B: 38              SEC                         
F39C: A9 69           LDA     #$69                  
F39E: ED C8 00        SBC     $00C8                   
F3A1: CD 0F F9        CMP     $F90F                   
F3A4: F0 08           BEQ     $F3AE                   
F3A6: CD 10 F9        CMP     $F910                   
F3A9: D0 52           BNE     $F3FD                   
F3AB: 8D 0F F8        STA     $F80F                   
F3AE: AD 0F F9        LDA     $F90F                   
F3B1: C9 00           CMP     #$00                  
F3B3: D0 0A           BNE     $F3BF                   
F3B5: A9 05           LDA     #$05                  
F3B7: 8D 10 F8        STA     $F810                   
F3BA: A9 73           LDA     #$73                  
F3BC: 4C E4 F3        JMP     $F3E4                   
F3BF: 38              SEC                         
F3C0: E9 05           SBC     #$05                  
F3C2: 8D 10 F8        STA     $F810                   
F3C5: 4C E4 F3        JMP     $F3E4                   
F3C8: 38              SEC                         
F3C9: A9 69           LDA     #$69                  
F3CB: ED C8 00        SBC     $00C8                   
F3CE: CD 0F F9        CMP     $F90F                   
F3D1: F0 08           BEQ     $F3DB                   
F3D3: CD 10 F9        CMP     $F910                   
F3D6: D0 25           BNE     $F3FD                   
F3D8: 8D 0F F8        STA     $F80F                   
F3DB: 18              CLC                         
F3DC: 69 05           ADC     #$05                  
F3DE: 8D 10 F8        STA     $F810                   
F3E1: 4C E4 F3        JMP     $F3E4                   
F3E4: A8              TAY                         
F3E5: A5 BD           LDA     $BD                   
F3E7: 18              CLC                         
F3E8: 69 05           ADC     #$05                  
F3EA: AA              TAX                         
F3EB: 20 6C F4        JSR     $F46C                   
F3EE: 90 08           BCC     $F3F8                   
F3F0: A6 BD           LDX     $BD                   
F3F2: E8              INX                         
F3F3: 20 6C F4        JSR     $F46C                   
F3F6: B0 05           BCS     $F3FD                   
F3F8: AD C8 00        LDA     $00C8                   
F3FB: 85 C2           STA     $C2                   
F3FD: 60              RTS                         
F3FE: 00              BRK                         
F3FF: 00              BRK                         
F400: 0F ; ????
F401: 00              BRK                         
F402: 00              BRK                         
F403: A5 B3           LDA     $B3                   
F405: 18              CLC                         
F406: 69 17           ADC     #$17                  
F408: 29 1F           AND     #$1F                  
F40A: 85 B3           STA     $B3                   
F40C: 60              RTS                         
F40D: 18              CLC                         
F40E: 65 B3           ADC     $B3                   
F410: 4A              LSR     A                   
F411: 4A              LSR     A                   
F412: 4A              LSR     A                   
F413: 4A              LSR     A                   
F414: 4A              LSR     A                   
F415: 49 04           EOR     #$04                  
F417: 38              SEC                         
F418: E9 04           SBC     #$04                  
F41A: 30 03           BMI     $F41F                   
F41C: 29 01           AND     #$01                  
F41E: 60              RTS                         
F41F: A9 FF           LDA     #$FF                  
F421: 60              RTS                         
F422: 86 C7           STX     $C7                   
F424: AD 55 F9        LDA     $F955                   
F427: C9 00           CMP     #$00                  
F429: D0 05           BNE     $F430                   
F42B: A2 00           LDX     #$00                  
F42D: 4C 4D F4        JMP     $F44D                   
F430: C9 01           CMP     #$01                  
F432: D0 05           BNE     $F439                   
F434: A2 06           LDX     #$06                  
F436: 4C 4D F4        JMP     $F44D                   
F439: C9 02           CMP     #$02                  
F43B: D0 05           BNE     $F442                   
F43D: A2 0C           LDX     #$0C                  
F43F: 4C 4D F4        JMP     $F44D                   
F442: C9 03           CMP     #$03                  
F444: D0 05           BNE     $F44B                   
F446: A2 12           LDX     #$12                  
F448: 4C 4D F4        JMP     $F44D                   
F44B: A2 18           LDX     #$18                  
F44D: BD 46 F5        LDA     $F546,X                 
F450: 85 C9           STA     $C9                   
F452: BD 47 F5        LDA     $F547,X                 
F455: 85 CA           STA     $CA                   
F457: BD 48 F5        LDA     $F548,X                 
F45A: 85 CB           STA     $CB                   
F45C: BD 49 F5        LDA     $F549,X                 
F45F: 85 CC           STA     $CC                   
F461: BD 4A F5        LDA     $F54A,X                 
F464: 85 CD           STA     $CD                   
F466: BD 4B F5        LDA     $F54B,X                 
F469: 85 CE           STA     $CE                   
F46B: 60              RTS                         
F46C: 20 22 F4        JSR     $F422                   
F46F: A6 C7           LDX     $C7                   
F471: E0 10           CPX     #$10                  
F473: B0 0C           BCS     $F481                   
F475: 8A              TXA                         
F476: 4A              LSR     A                   
F477: 4A              LSR     A                   
F478: AA              TAX                         
F479: B1 C9           LDA     ($C9),Y               
F47B: 3D 1E F5        AND     $F51E,X                 
F47E: 4C 14 F5        JMP     $F514                   
F481: E0 30           CPX     #$30                  
F483: B0 0F           BCS     $F494                   
F485: 8A              TXA                         
F486: 38              SEC                         
F487: E9 10           SBC     #$10                  
F489: 4A              LSR     A                   
F48A: 4A              LSR     A                   
F48B: AA              TAX                         
F48C: B1 CB           LDA     ($CB),Y               
F48E: 3D 22 F5        AND     $F522,X                 
F491: 4C 14 F5        JMP     $F514                   
F494: E0 50           CPX     #$50                  
F496: B0 0F           BCS     $F4A7                   
F498: 8A              TXA                         
F499: 38              SEC                         
F49A: E9 30           SBC     #$30                  
F49C: 4A              LSR     A                   
F49D: 4A              LSR     A                   
F49E: AA              TAX                         
F49F: B1 CD           LDA     ($CD),Y               
F4A1: 3D 36 F5        AND     $F536,X                 
F4A4: 4C 14 F5        JMP     $F514                   
F4A7: A5 B1           LDA     $B1                   
F4A9: C9 01           CMP     #$01                  
F4AB: F0 35           BEQ     $F4E2                   
F4AD: E0 60           CPX     #$60                  
F4AF: B0 0F           BCS     $F4C0                   
F4B1: 8A              TXA                         
F4B2: 38              SEC                         
F4B3: E9 50           SBC     #$50                  
F4B5: 4A              LSR     A                   
F4B6: 4A              LSR     A                   
F4B7: AA              TAX                         
F4B8: B1 C9           LDA     ($C9),Y               
F4BA: 3D 1E F5        AND     $F51E,X                 
F4BD: 4C 14 F5        JMP     $F514                   
F4C0: E0 80           CPX     #$80                  
F4C2: B0 0F           BCS     $F4D3                   
F4C4: 8A              TXA                         
F4C5: 38              SEC                         
F4C6: E9 60           SBC     #$60                  
F4C8: 4A              LSR     A                   
F4C9: 4A              LSR     A                   
F4CA: AA              TAX                         
F4CB: B1 CB           LDA     ($CB),Y               
F4CD: 3D 22 F5        AND     $F522,X                 
F4D0: 4C 14 F5        JMP     $F514                   
F4D3: 8A              TXA                         
F4D4: 38              SEC                         
F4D5: E9 80           SBC     #$80                  
F4D7: 4A              LSR     A                   
F4D8: 4A              LSR     A                   
F4D9: AA              TAX                         
F4DA: B1 CD           LDA     ($CD),Y               
F4DC: 3D 36 F5        AND     $F536,X                 
F4DF: 4C 14 F5        JMP     $F514                   
F4E2: E0 70           CPX     #$70                  
F4E4: B0 0F           BCS     $F4F5                   
F4E6: 8A              TXA                         
F4E7: 38              SEC                         
F4E8: E9 50           SBC     #$50                  
F4EA: 4A              LSR     A                   
F4EB: 4A              LSR     A                   
F4EC: AA              TAX                         
F4ED: B1 CD           LDA     ($CD),Y               
F4EF: 3D 3E F5        AND     $F53E,X                 
F4F2: 4C 14 F5        JMP     $F514                   
F4F5: E0 90           CPX     #$90                  
F4F7: B0 0F           BCS     $F508                   
F4F9: 8A              TXA                         
F4FA: 38              SEC                         
F4FB: E9 70           SBC     #$70                  
F4FD: 4A              LSR     A                   
F4FE: 4A              LSR     A                   
F4FF: AA              TAX                         
F500: B1 CB           LDA     ($CB),Y               
F502: 3D 36 F5        AND     $F536,X                 
F505: 4C 14 F5        JMP     $F514                   
F508: 8A              TXA                         
F509: 38              SEC                         
F50A: E9 90           SBC     #$90                  
F50C: 4A              LSR     A                   
F50D: 4A              LSR     A                   
F50E: AA              TAX                         
F50F: B1 C9           LDA     ($C9),Y               
F511: 3D 32 F5        AND     $F532,X                 
F514: D0 04           BNE     $F51A                   
F516: 18              CLC                         
F517: 4C 1B F5        JMP     $F51B                   
F51A: 38              SEC                         
F51B: A6 C7           LDX     $C7                   
F51D: 60              RTS                         
F51E: 10 20           BPL     $F540                   
F520: 40              RTI                         
F521: 80 ; ????
F522: 80 ; ????
F523: 40              RTI                         
F524: 20 10 08        JSR     $0810                   
F527: 04 ; ????
F528: 02 ; ????
F529: 01 80           ORA     ($80,X)               
F52B: 40              RTI                         
F52C: 20 10 10        JSR     $1010                   
F52F: 20 40 80        JSR     $8040                   
F532: 80 ; ????
F533: 40              RTI                         
F534: 20 10 01        JSR     $0110                   
F537: 02 ; ????
F538: 04 ; ????
F539: 08              PHP                         
F53A: 10 20           BPL     $F55C                   
F53C: 40              RTI                         
F53D: 80 ; ????
F53E: 80 ; ????
F53F: 40              RTI                         
F540: 20 10 08        JSR     $0810                   
F543: 04 ; ????
F544: 02 ; ????
F545: 01 00           ORA     ($00,X)               
F547: FB ; ????
F548: 80 ; ????
F549: FB ; ????
F54A: 00              BRK                         
F54B: FC ; ????
F54C: 01 FB           ORA     ($FB,X)               
F54E: 81 FB           STA     ($FB,X)               
F550: 01 FC           ORA     ($FC,X)               
F552: 02 ; ????
F553: FB ; ????
F554: 82 ; ????
F555: FB ; ????
F556: 02 ; ????
F557: FC ; ????
F558: 03 ; ????
F559: FB ; ????
F55A: 83 ; ????
F55B: FB ; ????
F55C: 03 ; ????
F55D: FC ; ????
F55E: 04 ; ????
F55F: FB ; ????
F560: 84 FB           STY     $FB                   
F562: 04 ; ????
F563: FC ; ????
F564: AD 0A F9        LDA     $F90A                   
F567: D0 05           BNE     $F56E                   
F569: AD 0B F9        LDA     $F90B                   
F56C: F0 09           BEQ     $F577                   
F56E: AD 0E F9        LDA     $F90E                   
F571: 18              CLC                         
F572: 69 01           ADC     #$01                  
F574: 8D 0E F8        STA     $F80E                   
F577: AD 0E F9        LDA     $F90E                   
F57A: 4A              LSR     A                   
F57B: 29 07           AND     #$07                  
F57D: 8D 4C F8        STA     $F84C                   
F580: AA              TAX                         
F581: AD 48 F9        LDA     $F948                   
F584: C9 00           CMP     #$00                  
F586: F0 08           BEQ     $F590                   
F588: C9 02           CMP     #$02                  
F58A: F0 17           BEQ     $F5A3                   
F58C: C9 06           CMP     #$06                  
F58E: F0 28           BEQ     $F5B8                   
F590: BD CD F5        LDA     $F5CD,X                 
F593: 8D 0C F8        STA     $F80C                   
F596: BD D5 F5        LDA     $F5D5,X                 
F599: 8D 0D F8        STA     $F80D                   
F59C: A5 DF           LDA     $DF                   
F59E: 29 F0           AND     #$F0                  
F5A0: 85 DF           STA     $DF                   
F5A2: 60              RTS                         
F5A3: BD DD F5        LDA     $F5DD,X                 
F5A6: 8D 0C F8        STA     $F80C                   
F5A9: BD E5 F5        LDA     $F5E5,X                 
F5AC: 8D 0D F8        STA     $F80D                   
F5AF: A5 DF           LDA     $DF                   
F5B1: 29 F0           AND     #$F0                  
F5B3: 09 01           ORA     #$01                  
F5B5: 85 DF           STA     $DF                   
F5B7: 60              RTS                         
F5B8: BD ED F5        LDA     $F5ED,X                 
F5BB: 8D 0C F8        STA     $F80C                   
F5BE: BD F5 F5        LDA     $F5F5,X                 
F5C1: 8D 0D F8        STA     $F80D                   
F5C4: A5 DF           LDA     $DF                   
F5C6: 29 F0           AND     #$F0                  
F5C8: 09 02           ORA     #$02                  
F5CA: 85 DF           STA     $DF                   
F5CC: 60              RTS                         
F5CD: 79 79 79        ADC     $7979,Y                 
F5D0: 79 79 79        ADC     $7979,Y                 
F5D3: 79 79 F1        ADC     $F179,Y                 
F5D6: F1 F5           SBC     ($F5),Y               
F5D8: F5 F1           SBC     $F1,X                 
F5DA: F1 F5           SBC     ($F5),Y               
F5DC: F5 79           SBC     $79,X                 
F5DE: 79 79 79        ADC     $7979,Y                 
F5E1: 79 79 79        ADC     $7979,Y                 
F5E4: 79 F2 F2        ADC     $F2F2,Y                 
F5E7: F3 ; ????
F5E8: F3 ; ????
F5E9: F2 ; ????
F5EA: F2 ; ????
F5EB: F3 ; ????
F5EC: F3 ; ????
F5ED: 79 79 79        ADC     $7979,Y                 
F5F0: 79 79 79        ADC     $7979,Y                 
F5F3: 79 79 F0        ADC     $F079,Y                 
F5F6: F0 F4           BEQ     $F5EC                   
F5F8: F4 ; ????
F5F9: F0 F0           BEQ     $F5EB                   
F5FB: F4 ; ????
F5FC: F4 ; ????
F5FD: A5 F5           LDA     $F5                   
F5FF: D0 08           BNE     $F609                   
F601: 20 0C F6        JSR     $F60C                   
F604: A9 01           LDA     #$01                  
F606: 85 F5           STA     $F5                   
F608: 60              RTS                         
F609: A9 00           LDA     #$00                  
F60B: 60              RTS                         
F60C: AD E8 FF        LDA     $FFE8                   ; RAM bank 0
F60F: AD 09 F9        LDA     $F909                   
F612: 10 33           BPL     $F647                   
F614: AD 08 F9        LDA     $F908                   
F617: 0A              ASL     A                   
F618: AA              TAX                         
F619: BD 89 F6        LDA     $F689,X                 
F61C: 85 CD           STA     $CD                   
F61E: BD 8A F6        LDA     $F68A,X                 
F621: 85 CE           STA     $CE                   
F623: BD 91 F6        LDA     $F691,X                 
F626: 85 CF           STA     $CF                   
F628: BD 92 F6        LDA     $F692,X                 
F62B: 85 D0           STA     $D0                   
F62D: A0 35           LDY     #$35                  
F62F: B9 55 F9        LDA     $F955,Y                 
F632: 91 CD           STA     ($CD),Y               
F634: 88              DEY                         
F635: 10 F8           BPL     $F62F                   
F637: AD E9 FF        LDA     $FFE9                   ; RAM bank 1
F63A: A0 31           LDY     #$31                  
F63C: B9 81 00        LDA     $0081,Y                 
F63F: 91 CF           STA     ($CF),Y               
F641: 88              DEY                         
F642: 10 F8           BPL     $F63C                   
F644: AD E8 FF        LDA     $FFE8                   ; RAM bank 0
F647: 60              RTS                         

F648: AD E8 FF        LDA     $FFE8                   ; RAM bank 0
F64B: AD 09 F9        LDA     $F909                   
F64E: 10 38           BPL     $F688                   
F650: AD 08 F9        LDA     $F908                   
F653: 49 01           EOR     #$01                  
F655: 8D 08 F8        STA     $F808                   
F658: 0A              ASL     A                   
F659: AA              TAX                         
F65A: BD 8D F6        LDA     $F68D,X                 
F65D: 85 CD           STA     $CD                   
F65F: BD 8E F6        LDA     $F68E,X                 
F662: 85 CE           STA     $CE                   
F664: BD 95 F6        LDA     $F695,X                 
F667: 85 CF           STA     $CF                   
F669: BD 96 F6        LDA     $F696,X                 
F66C: 85 D0           STA     $D0                   
F66E: A0 35           LDY     #$35                  
F670: B1 CD           LDA     ($CD),Y               
F672: 99 55 F8        STA     $F855,Y                 
F675: 88              DEY                         
F676: 10 F8           BPL     $F670                   
F678: AD E9 FF        LDA     $FFE9                   ; RAM bank 1
F67B: A0 31           LDY     #$31                  
F67D: B1 CF           LDA     ($CF),Y               
F67F: 99 81 00        STA     $0081,Y                 
F682: 88              DEY                         
F683: 10 F8           BPL     $F67D                   
F685: AD E8 FF        LDA     $FFE8                   ; RAM bank 0
F688: 60              RTS                         
F689: 8B ; ????
F68A: F8              SED                         
F68B: C1 F8           CMP     ($F8,X)               
F68D: 8B ; ????
F68E: F9 C1 F9        SBC     $F9C1,Y                 
F691: 00              BRK                         
F692: F8              SED                         
F693: 37 ; ????
F694: F8              SED                         
F695: 00              BRK                         
F696: F9 37 F9        SBC     $F937,Y                 
F699: A9 02           LDA     #$02                  
F69B: 85 01           STA     $01                   
F69D: A9 39           LDA     #$39                  
F69F: 8D 96 02        STA     $0296                   
F6A2: A5 F5           LDA     $F5                   
F6A4: F0 08           BEQ     $F6AE                   
F6A6: 20 48 F6        JSR     $F648                   
F6A9: A9 00           LDA     #$00                  
F6AB: 85 F5           STA     $F5                   
F6AD: 60              RTS                         
F6AE: 2C 82 02        BIT     $0282                   
F6B1: AD 82 02        LDA     $0282                   
F6B4: 85 F6           STA     $F6                   
F6B6: 4A              LSR     A                   
F6B7: A9 01           LDA     #$01                  
F6B9: 60              RTS                         
F6BA: AD 55 F9        LDA     $F955                   
F6BD: 18              CLC                         
F6BE: 69 01           ADC     #$01                  
F6C0: C9 05           CMP     #$05                  
F6C2: D0 02           BNE     $F6C6                   
F6C4: A9 00           LDA     #$00                  
F6C6: 8D 55 F8        STA     $F855                   
F6C9: AD 8A F9        LDA     $F98A                   
F6CC: 18              CLC                         
F6CD: 69 01           ADC     #$01                  
F6CF: C9 19           CMP     #$19                  
F6D1: F0 03           BEQ     $F6D6                   
F6D3: 8D 8A F8        STA     $F88A                   
F6D6: 20 89 F0        JSR     $F089                   
F6D9: AD 56 F9        LDA     $F956                   
F6DC: 29 EF           AND     #$EF                  
F6DE: 8D 56 F8        STA     $F856                   
F6E1: 60              RTS                         
F6E2: A5 DE           LDA     $DE                   
F6E4: 2A              ROL     A                   
F6E5: 2A              ROL     A                   
F6E6: 29 01           AND     #$01                  
F6E8: AA              TAX                         
F6E9: 18              CLC                         
F6EA: 69 01           ADC     #$01                  
F6EC: 85 CD           STA     $CD                   
F6EE: BD 43 F7        LDA     $F743,X                 
F6F1: AA              TAX                         
F6F2: BD A5 F9        LDA     $F9A5,X                 
F6F5: 8D 6F F8        STA     $F86F                   
F6F8: BD A6 F9        LDA     $F9A6,X                 
F6FB: 8D 70 F8        STA     $F870                   
F6FE: BD A7 F9        LDA     $F9A7,X                 
F701: 8D 71 F8        STA     $F871                   
F704: A9 A0           LDA     #$A0                  
F706: 05 CD           ORA     $CD                   
F708: 8D 58 F8        STA     $F858                   
F70B: A9 BC           LDA     #$BC                  
F70D: 8D 57 F8        STA     $F857                   
F710: 60              RTS                         
F711: AD 56 F9        LDA     $F956                   
F714: 29 8F           AND     #$8F                  
F716: 8D 56 F8        STA     $F856                   
F719: AD 08 F9        LDA     $F908                   
F71C: 49 01           EOR     #$01                  
F71E: AA              TAX                         
F71F: BD 43 F7        LDA     $F743,X                 
F722: AA              TAX                         
F723: BD 8C F9        LDA     $F98C,X                 
F726: 60              RTS                         
F727: A2 13           LDX     #$13                  
F729: BD 1A F9        LDA     $F91A,X                 
F72C: D0 05           BNE     $F733                   
F72E: CA              DEX                         
F72F: 10 F8           BPL     $F729                   
F731: 18              CLC                         
F732: 60              RTS                         
F733: 38              SEC                         
F734: 60              RTS                         
F735: AD 08 F9        LDA     $F908                   
F738: 49 01           EOR     #$01                  
F73A: AA              TAX                         
F73B: BD 43 F7        LDA     $F743,X                 
F73E: AA              TAX                         
F73F: BD 8C F9        LDA     $F98C,X                 
F742: 60              RTS                         
F743: 00              BRK                         
F744: 36 

F745: 00 00 00 00 00 00 00 00 00 00 00
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