![Combat PAL](A2600Combat.jpg)

# Combat PAL

>>> cpu 6502

>>> binary F000:CombatPAL.bin

>>> memoryTable hard 
[Hardware Info](../Stella.md)

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

This is the PAL version of the code.

```html
<script src="/Atari2600/Stella.js"></script>
<script src="/js/TileEngine.js"></script>
<script src="/js/BinaryData.js"></script>
<script src="/js/CANVAS.js"></script>
<script src="Combat.js"></script>

<!-- Cache some commonly-used values -->
<canvas width="0" height="0"
        data-canvasFunction="TileEngine.handleTileCanvas"
        data-labelColor=""
        data-pixWidth="10"
        data-pixHeight="10"
        data-gap="0.25"
        data-gridPad="1">      
</canvas>
<canvas width="0" height="0"
       data-colorsName="TANKPLAYFIELD"
       data-colors='["#BBD46E","#8C2A44"]'>       
</canvas>
<canvas width="0" height="0"
       data-colorsName="PLANEPLAYFIELD"
       data-colors='["#000088","#90B4EC"]'>       
</canvas>
<canvas width="0" height="0"
       data-colorsName="JETPLAYFIELD"
       data-colors='["#783CA4","#689CC0"]'>
</canvas>
<canvas width="0" height="0"
       data-colorsName="TANKP0"
       data-colors='["#BBD46E","#B03C3C"]'>
</canvas>
<canvas width="0" height="0"
       data-colorsName="PLANEP0"
       data-colors='["#000088","#9CCC7C"]'>
</canvas>
<canvas width="0" height="0"
       data-colorsName="JETP0"
       data-colors='["#783CA4","#6E8454"]'>
</canvas>
```

```code
F000: 78             SEI                     
F001: D8             CLD                     
F002: A2 FF          LDX     #$FF            
F004: 9A             TXS                     
F005: A2 5D          LDX     #$5D            
F007: 20 B3 F5       JSR     $F5B3           
F00A: A9 10          LDA     #$10            
F00C: 8D 83 02       STA     $0283           
F00F: 85 88          STA     $88             
F011: 20 9A F1       JSR     $F19A           
F014: E6 86          INC     $86             
F016: 85 2B          STA     $2B             
F018: A9 02          LDA     #$02            
F01A: 85 02          STA     $02             
F01C: 85 01          STA     $01             
F01E: 85 02          STA     $02             
F020: 85 02          STA     $02             
F022: 85 02          STA     $02             
F024: 85 00          STA     $00             
F026: 85 02          STA     $02             
F028: 85 02          STA     $02             
F02A: A9 00          LDA     #$00            
F02C: 85 02          STA     $02             
F02E: 85 00          STA     $00             
F030: A9 2C          LDA     #$2C            
F032: 8D 96 02       STA     $0296           
F035: 20 4E F1       JSR     $F14E           
F038: 20 1B F3       JSR     $F31B           
F03B: 20 85 F4       JSR     $F485           
F03E: 20 55 F2       JSR     $F255           
F041: 20 EA F2       JSR     $F2EA           
F044: 20 33 F2       JSR     $F233           
F047: A9 08          LDA     #$08            
F049: 85 B4          STA     $B4             
F04B: 85 02          STA     $02             
F04D: 85 2A          STA     $2A             
F04F: AD 84 02       LDA     $0284           
F052: D0 FB          BNE     $F04F           
F054: 85 02          STA     $02             
F056: 85 2C          STA     $2C             
F058: 85 01          STA     $01             
F05A: BA             TSX                     
F05B: 86 D3          STX     $D3             
F05D: A9 02          LDA     #$02            
F05F: 85 0A          STA     $0A             
F061: A6 DC          LDX     $DC             
F063: 85 02          STA     $02             
F065: CA             DEX                     
F066: D0 FB          BNE     $F063           
F068: A5 DC          LDA     $DC             
F06A: C9 0E          CMP     #$0E            
F06C: F0 52          BEQ     $F0C0           
F06E: A2 05          LDX     #$05            
F070: A9 00          LDA     #$00            
F072: 85 DE          STA     $DE             
F074: 85 DF          STA     $DF             
F076: 85 02          STA     $02             
F078: A5 DE          LDA     $DE             
F07A: 85 0E          STA     $0E             
F07C: A4 E2          LDY     $E2             
F07E: B9 BB F5       LDA     $F5BB,Y         
F081: 29 F0          AND     #$F0            
F083: 85 DE          STA     $DE             
F085: A4 E0          LDY     $E0             
F087: B9 BB F5       LDA     $F5BB,Y         
F08A: 29 0F          AND     #$0F            
F08C: 05 DE          ORA     $DE             
F08E: 85 DE          STA     $DE             
F090: A5 DF          LDA     $DF             
F092: 85 0E          STA     $0E             
F094: A4 E3          LDY     $E3             
F096: B9 BB F5       LDA     $F5BB,Y         
F099: 29 F0          AND     #$F0            
F09B: 85 DF          STA     $DF             
F09D: A4 E1          LDY     $E1             
F09F: B9 BB F5       LDA     $F5BB,Y         
F0A2: 25 87          AND     $87             
F0A4: 85 02          STA     $02             
F0A6: 05 DF          ORA     $DF             
F0A8: 85 DF          STA     $DF             
F0AA: A5 DE          LDA     $DE             
F0AC: 85 0E          STA     $0E             
F0AE: CA             DEX                     
F0AF: 30 0F          BMI     $F0C0           
F0B1: E6 E0          INC     $E0             
F0B3: E6 E2          INC     $E2             
F0B5: E6 E1          INC     $E1             
F0B7: E6 E3          INC     $E3             
F0B9: A5 DF          LDA     $DF             
F0BB: 85 0E          STA     $0E             
F0BD: 4C 76 F0       JMP     $F076           
F0C0: A9 00          LDA     #$00            
F0C2: 85 0E          STA     $0E             
F0C4: 85 02          STA     $02             
F0C6: A9 05          LDA     #$05            
F0C8: 85 0A          STA     $0A             
F0CA: A5 D6          LDA     $D6             
F0CC: 85 06          STA     $06             
F0CE: A5 D7          LDA     $D7             
F0D0: 85 07          STA     $07             
F0D2: A2 1E          LDX     #$1E            
F0D4: 9A             TXS                     
F0D5: 38             SEC                     
F0D6: A5 A4          LDA     $A4             
F0D8: E5 B4          SBC     $B4             
F0DA: 29 FE          AND     #$FE            
F0DC: AA             TAX                     
F0DD: 29 F0          AND     #$F0            
F0DF: F0 04          BEQ     $F0E5           
F0E1: A9 00          LDA     #$00            
F0E3: F0 02          BEQ     $F0E7           
F0E5: B5 BD          LDA     $BD,X           
F0E7: 85 02          STA     $02             
F0E9: 85 1B          STA     $1B             
F0EB: A5 A7          LDA     $A7             
F0ED: 45 B4          EOR     $B4             
F0EF: 29 FE          AND     #$FE            
F0F1: 08             PHP                     
F0F2: A5 A6          LDA     $A6             
F0F4: 45 B4          EOR     $B4             
F0F6: 29 FE          AND     #$FE            
F0F8: 08             PHP                     
F0F9: A5 B4          LDA     $B4             
F0FB: 10 02          BPL     $F0FF           
F0FD: 49 F8          EOR     #$F8            
F0FF: C9 08          CMP     #$08            
F101: 90 04          BCC     $F107           
F103: 4A             LSR     A               
F104: 4A             LSR     A               
F105: 4A             LSR     A               
F106: A8             TAY                     
F107: A5 A5          LDA     $A5             
F109: 38             SEC                     
F10A: E5 B4          SBC     $B4             
F10C: E6 B4          INC     $B4             
F10E: EA             NOP                     
F10F: 09 01          ORA     #$01            
F111: AA             TAX                     
F112: 29 F0          AND     #$F0            
F114: F0 04          BEQ     $F11A           
F116: A9 00          LDA     #$00            
F118: F0 02          BEQ     $F11C           
F11A: B5 BD          LDA     $BD,X           
F11C: 24 82          BIT     $82             
F11E: 85 1C          STA     $1C             
F120: 30 0C          BMI     $F12E           
F122: B1 B5          LDA     ($B5),Y         
F124: 85 0D          STA     $0D             
F126: B1 B7          LDA     ($B7),Y         
F128: 85 0E          STA     $0E             
F12A: B1 B9          LDA     ($B9),Y         
F12C: 85 0F          STA     $0F             
F12E: E6 B4          INC     $B4             
F130: A5 B4          LDA     $B4             
F132: 49 04          EOR     #$04            
F134: D0 9C          BNE     $F0D2           
F136: A6 D3          LDX     $D3             
F138: 9A             TXS                     
F139: 85 02          STA     $02             
F13B: 85 1D          STA     $1D             
F13D: 85 1E          STA     $1E             
F13F: 85 1B          STA     $1B             
F141: 85 1C          STA     $1C             
F143: 85 1B          STA     $1B             
F145: 85 0D          STA     $0D             
F147: 85 0E          STA     $0E             
F149: 85 0F          STA     $0F             
F14B: 4C 14 F0       JMP     $F014           
F14E: AD 82 02       LDA     $0282           
F151: 4A             LSR     A               
F152: B0 13          BCS     $F167           
F154: A9 0F          LDA     #$0F            
F156: 85 87          STA     $87             
F158: A9 FF          LDA     #$FF            
F15A: 85 88          STA     $88             
F15C: A9 80          LDA     #$80            
F15E: 85 DD          STA     $DD             
F160: A2 E6          LDX     #$E6            
F162: 20 B3 F5       JSR     $F5B3           
F165: F0 60          BEQ     $F1C7           
F167: A0 02          LDY     #$02            
F169: A5 DD          LDA     $DD             
F16B: 25 88          AND     $88             
F16D: C9 F0          CMP     #$F0            
F16F: 90 08          BCC     $F179           
F171: A5 86          LDA     $86             
F173: 29 30          AND     #$30            
F175: D0 02          BNE     $F179           
F177: A0 0E          LDY     #$0E            
F179: 84 DC          STY     $DC             
F17B: A5 86          LDA     $86             
F17D: 29 3F          AND     #$3F            
F17F: D0 08          BNE     $F189           
F181: 85 89          STA     $89             
F183: E6 DD          INC     $DD             
F185: D0 02          BNE     $F189           
F187: 85 88          STA     $88             
F189: AD 82 02       LDA     $0282           
F18C: 29 02          AND     #$02            
F18E: F0 04          BEQ     $F194           
F190: 85 89          STA     $89             
F192: D0 54          BNE     $F1E8           
F194: 24 89          BIT     $89             
F196: 30 50          BMI     $F1E8           
F198: E6 80          INC     $80             
F19A: A2 DF          LDX     #$DF            
F19C: 20 B3 F5       JSR     $F5B3           
F19F: A9 FF          LDA     #$FF            
F1A1: 85 89          STA     $89             
F1A3: A4 80          LDY     $80             
F1A5: B9 E0 F7       LDA     $F7E0,Y         
F1A8: 85 A3          STA     $A3             
F1AA: 49 FF          EOR     #$FF            
F1AC: D0 04          BNE     $F1B2           
F1AE: A2 DD          LDX     #$DD            
F1B0: D0 EA          BNE     $F19C           
F1B2: A5 81          LDA     $81             
F1B4: F8             SED                     
F1B5: 18             CLC                     
F1B6: 69 01          ADC     #$01            
F1B8: 85 81          STA     $81             
F1BA: 85 A1          STA     $A1             
F1BC: D8             CLD                     
F1BD: 24 A3          BIT     $A3             
F1BF: 10 06          BPL     $F1C7           
F1C1: E6 85          INC     $85             
F1C3: 50 02          BVC     $F1C7           
F1C5: E6 85          INC     $85             
F1C7: 20 66 F5       JSR     $F566           
F1CA: A9 32          LDA     #$32            
F1CC: 85 A5          STA     $A5             
F1CE: A9 86          LDA     #$86            
F1D0: 85 A4          STA     $A4             
F1D2: 24 A3          BIT     $A3             
F1D4: 30 12          BMI     $F1E8           
F1D6: 85 A5          STA     $A5             
F1D8: 85 11          STA     $11             
F1DA: A9 08          LDA     #$08            
F1DC: 85 96          STA     $96             
F1DE: A9 20          LDA     #$20            
F1E0: 85 20          STA     $20             
F1E2: 85 21          STA     $21             
F1E4: 85 02          STA     $02             
F1E6: 85 2A          STA     $2A             
F1E8: A5 A3          LDA     $A3             
F1EA: 29 87          AND     #$87            
F1EC: 30 02          BMI     $F1F0           
F1EE: A9 00          LDA     #$00            
F1F0: 0A             ASL     A               
F1F1: AA             TAX                     
F1F2: BD 53 F7       LDA     $F753,X         
F1F5: 85 04          STA     $04             
F1F7: BD 54 F7       LDA     $F754,X         
F1FA: 85 05          STA     $05             
F1FC: A5 A3          LDA     $A3             
F1FE: 29 C0          AND     #$C0            
F200: 4A             LSR     A               
F201: 4A             LSR     A               
F202: 4A             LSR     A               
F203: 4A             LSR     A               
F204: A8             TAY                     
F205: A5 88          LDA     $88             
F207: 8D 82 02       STA     $0282           
F20A: 49 FF          EOR     #$FF            
F20C: 25 DD          AND     $DD             
F20E: 85 D1          STA     $D1             
F210: A2 FF          LDX     #$FF            
F212: AD 82 02       LDA     $0282           
F215: 29 08          AND     #$08            
F217: D0 04          BNE     $F21D           
F219: A0 10          LDY     #$10            
F21B: A2 0F          LDX     #$0F            
F21D: 86 D2          STX     $D2             
F21F: A2 03          LDX     #$03            
F221: B9 5B F7       LDA     $F75B,Y         
F224: 45 D1          EOR     $D1             
F226: 25 D2          AND     $D2             
F228: 95 06          STA     $06,X           
F22A: 95 D6          STA     $D6,X           
F22C: 95 D8          STA     $D8,X           
F22E: C8             INY                     
F22F: CA             DEX                     
F230: 10 EF          BPL     $F221           
F232: 60             RTS                     
F233: A2 01          LDX     #$01            
F235: B5 A1          LDA     $A1,X           
F237: 29 0F          AND     #$0F            
F239: 85 D2          STA     $D2             
F23B: 0A             ASL     A               
F23C: 0A             ASL     A               
F23D: 18             CLC                     
F23E: 65 D2          ADC     $D2             
F240: 95 E0          STA     $E0,X           
F242: B5 A1          LDA     $A1,X           
F244: 29 F0          AND     #$F0            
F246: 4A             LSR     A               
F247: 4A             LSR     A               
F248: 85 D2          STA     $D2             
F24A: 4A             LSR     A               
F24B: 4A             LSR     A               
F24C: 18             CLC                     
F24D: 65 D2          ADC     $D2             
F24F: 95 E2          STA     $E2,X           
F251: CA             DEX                     
F252: 10 E1          BPL     $F235           
F254: 60             RTS                     
F255: 24 83          BIT     $83             
F257: 50 04          BVC     $F25D           
F259: A9 30          LDA     #$30            
F25B: 10 02          BPL     $F25F           
F25D: A9 20          LDA     #$20            
F25F: 85 B1          STA     $B1             
F261: A2 03          LDX     #$03            
F263: 20 95 F2       JSR     $F295           
F266: CA             DEX                     
F267: 20 95 F2       JSR     $F295           
F26A: CA             DEX                     
F26B: B5 8D          LDA     $8D,X           
F26D: 29 08          AND     #$08            
F26F: 4A             LSR     A               
F270: 4A             LSR     A               
F271: 86 D1          STX     $D1             
F273: 18             CLC                     
F274: 65 D1          ADC     $D1             
F276: A8             TAY                     
F277: B9 A8 00       LDA     $00A8,Y         
F27A: 38             SEC                     
F27B: 30 01          BMI     $F27E           
F27D: 18             CLC                     
F27E: 2A             ROL     A               
F27F: 99 A8 00       STA     $00A8,Y         
F282: 90 0D          BCC     $F291           
F284: B5 AC          LDA     $AC,X           
F286: 29 01          AND     #$01            
F288: 0A             ASL     A               
F289: 0A             ASL     A               
F28A: 0A             ASL     A               
F28B: 0A             ASL     A               
F28C: 85 B1          STA     $B1             
F28E: 20 95 F2       JSR     $F295           
F291: CA             DEX                     
F292: F0 D7          BEQ     $F26B           
F294: 60             RTS                     
F295: F6 AC          INC     $AC,X           
F297: B5 95          LDA     $95,X           
F299: 29 0F          AND     #$0F            
F29B: 18             CLC                     
F29C: 65 B1          ADC     $B1             
F29E: A8             TAY                     
F29F: B9 ED F5       LDA     $F5ED,Y         
F2A2: 85 B0          STA     $B0             
F2A4: 24 82          BIT     $82             
F2A6: 70 13          BVS     $F2BB           
F2A8: B5 95          LDA     $95,X           
F2AA: 38             SEC                     
F2AB: E9 02          SBC     #$02            
F2AD: 29 03          AND     #$03            
F2AF: D0 0A          BNE     $F2BB           
F2B1: B5 AC          LDA     $AC,X           
F2B3: 29 03          AND     #$03            
F2B5: D0 04          BNE     $F2BB           
F2B7: A9 08          LDA     #$08            
F2B9: 85 B0          STA     $B0             
F2BB: A5 B0          LDA     $B0             
F2BD: 95 20          STA     $20,X           
F2BF: 29 0F          AND     #$0F            
F2C1: 38             SEC                     
F2C2: E9 08          SBC     #$08            
F2C4: 85 D4          STA     $D4             
F2C6: 18             CLC                     
F2C7: 75 A4          ADC     $A4,X           
F2C9: 24 A3          BIT     $A3             
F2CB: 30 04          BMI     $F2D1           
F2CD: E0 02          CPX     #$02            
F2CF: B0 10          BCS     $F2E1           
F2D1: C9 F3          CMP     #$F3            
F2D3: B0 04          BCS     $F2D9           
F2D5: C9 12          CMP     #$12            
F2D7: B0 08          BCS     $F2E1           
F2D9: A9 F1          LDA     #$F1            
F2DB: 24 D4          BIT     $D4             
F2DD: 30 02          BMI     $F2E1           
F2DF: A9 13          LDA     #$13            
F2E1: 95 A4          STA     $A4,X           
F2E3: E0 02          CPX     #$02            
F2E5: B0 02          BCS     $F2E9           
F2E7: 95 25          STA     $25,X           
F2E9: 60             RTS                     
F2EA: A9 01          LDA     #$01            
F2EC: 25 86          AND     $86             
F2EE: AA             TAX                     
F2EF: B5 95          LDA     $95,X           
F2F1: 95 0B          STA     $0B,X           
F2F3: 29 0F          AND     #$0F            
F2F5: A8             TAY                     
F2F6: 24 83          BIT     $83             
F2F8: 10 02          BPL     $F2FC           
F2FA: 94 97          STY     $97,X           
F2FC: 8A             TXA                     
F2FD: 49 0E          EOR     #$0E            
F2FF: AA             TAX                     
F300: 98             TYA                     
F301: 0A             ASL     A               
F302: 0A             ASL     A               
F303: 0A             ASL     A               
F304: C9 3F          CMP     #$3F            
F306: 18             CLC                     
F307: 30 03          BMI     $F30C           
F309: 38             SEC                     
F30A: 49 47          EOR     #$47            
F30C: A8             TAY                     
F30D: B1 BB          LDA     ($BB),Y         
F30F: 95 BD          STA     $BD,X           
F311: 90 02          BCC     $F315           
F313: 88             DEY                     
F314: 88             DEY                     
F315: C8             INY                     
F316: CA             DEX                     
F317: CA             DEX                     
F318: 10 F3          BPL     $F30D           
F31A: 60             RTS                     
F31B: A5 8A          LDA     $8A             
F31D: 38             SEC                     
F31E: E9 02          SBC     #$02            
F320: 90 2B          BCC     $F34D           
F322: 85 8A          STA     $8A             
F324: C9 02          CMP     #$02            
F326: 90 24          BCC     $F34C           
F328: 29 01          AND     #$01            
F32A: AA             TAX                     
F32B: F6 95          INC     $95,X           
F32D: B5 D8          LDA     $D8,X           
F32F: 95 D6          STA     $D6,X           
F331: A5 8A          LDA     $8A             
F333: C9 F7          CMP     #$F7            
F335: 90 03          BCC     $F33A           
F337: 20 49 F5       JSR     $F549           
F33A: A5 8A          LDA     $8A             
F33C: 10 0E          BPL     $F34C           
F33E: 4A             LSR     A               
F33F: 4A             LSR     A               
F340: 4A             LSR     A               
F341: 95 19          STA     $19,X           
F343: A9 08          LDA     #$08            
F345: 95 15          STA     $15,X           
F347: BD FE F7       LDA     $F7FE,X         
F34A: 95 17          STA     $17,X           
F34C: 60             RTS                     
F34D: A2 01          LDX     #$01            
F34F: AD 82 02       LDA     $0282           
F352: 85 D5          STA     $D5             
F354: AD 80 02       LDA     $0280           
F357: 24 88          BIT     $88             
F359: 30 02          BMI     $F35D           
F35B: A9 FF          LDA     #$FF            
F35D: 49 FF          EOR     #$FF            
F35F: 29 0F          AND     #$0F            
F361: 85 D2          STA     $D2             
F363: A4 85          LDY     $85             
F365: B9 05 F7       LDA     $F705,Y         
F368: 18             CLC                     
F369: 65 D2          ADC     $D2             
F36B: A8             TAY                     
F36C: B9 08 F7       LDA     $F708,Y         
F36F: 29 0F          AND     #$0F            
F371: 85 D1          STA     $D1             
F373: F0 04          BEQ     $F379           
F375: D5 91          CMP     $91,X           
F377: D0 04          BNE     $F37D           
F379: D6 93          DEC     $93,X           
F37B: D0 0D          BNE     $F38A           
F37D: 95 91          STA     $91,X           
F37F: A9 0F          LDA     #$0F            
F381: 95 93          STA     $93,X           
F383: A5 D1          LDA     $D1             
F385: 18             CLC                     
F386: 75 95          ADC     $95,X           
F388: 95 95          STA     $95,X           
F38A: F6 8D          INC     $8D,X           
F38C: 30 1E          BMI     $F3AC           
F38E: B9 08 F7       LDA     $F708,Y         
F391: 4A             LSR     A               
F392: 4A             LSR     A               
F393: 4A             LSR     A               
F394: 4A             LSR     A               
F395: 24 D5          BIT     $D5             
F397: 30 23          BMI     $F3BC           
F399: 95 8B          STA     $8B,X           
F39B: 0A             ASL     A               
F39C: A8             TAY                     
F39D: B9 2D F6       LDA     $F62D,Y         
F3A0: 95 A8          STA     $A8,X           
F3A2: C8             INY                     
F3A3: B9 2D F6       LDA     $F62D,Y         
F3A6: 95 AA          STA     $AA,X           
F3A8: A9 F0          LDA     #$F0            
F3AA: 95 8D          STA     $8D,X           
F3AC: 20 C1 F3       JSR     $F3C1           
F3AF: AD 80 02       LDA     $0280           
F3B2: 4A             LSR     A               
F3B3: 4A             LSR     A               
F3B4: 4A             LSR     A               
F3B5: 4A             LSR     A               
F3B6: 06 D5          ASL     $D5             
F3B8: CA             DEX                     
F3B9: F0 9C          BEQ     $F357           
F3BB: 60             RTS                     
F3BC: 38             SEC                     
F3BD: E5 85          SBC     $85             
F3BF: 10 D8          BPL     $F399           
F3C1: A5 A3          LDA     $A3             
F3C3: 30 08          BMI     $F3CD           
F3C5: 29 01          AND     #$01            
F3C7: F0 04          BEQ     $F3CD           
F3C9: A5 DB          LDA     $DB             
F3CB: 95 D6          STA     $D6,X           
F3CD: B5 99          LDA     $99,X           
F3CF: F0 27          BEQ     $F3F8           
F3D1: B5 D8          LDA     $D8,X           
F3D3: 95 D6          STA     $D6,X           
F3D5: B5 99          LDA     $99,X           
F3D7: C9 07          CMP     #$07            
F3D9: 90 14          BCC     $F3EF           
F3DB: 24 D5          BIT     $D5             
F3DD: 10 04          BPL     $F3E3           
F3DF: C9 1C          CMP     #$1C            
F3E1: 90 0C          BCC     $F3EF           
F3E3: C9 30          CMP     #$30            
F3E5: 90 1F          BCC     $F406           
F3E7: C9 37          CMP     #$37            
F3E9: B0 21          BCS     $F40C           
F3EB: 24 83          BIT     $83             
F3ED: 50 1D          BVC     $F40C           
F3EF: A9 00          LDA     #$00            
F3F1: 95 99          STA     $99,X           
F3F3: A9 FF          LDA     #$FF            
F3F5: 95 28          STA     $28,X           
F3F7: 60             RTS                     
F3F8: 24 88          BIT     $88             
F3FA: 10 04          BPL     $F400           
F3FC: B5 3C          LDA     $3C,X           
F3FE: 10 37          BPL     $F437           
F400: 20 51 F4       JSR     $F451           
F403: 4C EF F3       JMP     $F3EF           
F406: 20 51 F4       JSR     $F451           
F409: 4C 1F F4       JMP     $F41F           
F40C: B5 9F          LDA     $9F,X           
F40E: F0 0A          BEQ     $F41A           
F410: 20 51 F4       JSR     $F451           
F413: A9 30          LDA     #$30            
F415: 95 99          STA     $99,X           
F417: 4C 1F F4       JMP     $F41F           
F41A: B5 99          LDA     $99,X           
F41C: 20 41 F3       JSR     $F341           
F41F: A5 86          LDA     $86             
F421: 29 03          AND     #$03            
F423: F0 0C          BEQ     $F431           
F425: 24 84          BIT     $84             
F427: 70 0A          BVS     $F433           
F429: 24 82          BIT     $82             
F42B: 50 04          BVC     $F431           
F42D: 29 01          AND     #$01            
F42F: D0 02          BNE     $F433           
F431: D6 99          DEC     $99,X           
F433: A9 00          LDA     #$00            
F435: F0 BE          BEQ     $F3F5           
F437: A9 3F          LDA     #$3F            
F439: 95 99          STA     $99,X           
F43B: 38             SEC                     
F43C: B5 A4          LDA     $A4,X           
F43E: E9 06          SBC     #$06            
F440: 95 A6          STA     $A6,X           
F442: B5 95          LDA     $95,X           
F444: 95 97          STA     $97,X           
F446: A9 1F          LDA     #$1F            
F448: 95 9B          STA     $9B,X           
F44A: A9 00          LDA     #$00            
F44C: 95 9D          STA     $9D,X           
F44E: 4C 0C F4       JMP     $F40C           
F451: B5 9F          LDA     $9F,X           
F453: F0 0D          BEQ     $F462           
F455: A9 04          LDA     #$04            
F457: 95 15          STA     $15,X           
F459: A9 07          LDA     #$07            
F45B: 95 19          STA     $19,X           
F45D: B5 9B          LDA     $9B,X           
F45F: 95 17          STA     $17,X           
F461: 60             RTS                     
F462: A4 85          LDY     $85             
F464: B9 29 F7       LDA     $F729,Y         
F467: 25 88          AND     $88             
F469: 95 19          STA     $19,X           
F46B: B9 2C F7       LDA     $F72C,Y         
F46E: 95 15          STA     $15,X           
F470: 18             CLC                     
F471: A9 00          LDA     #$00            
F473: 88             DEY                     
F474: 30 04          BMI     $F47A           
F476: 69 0C          ADC     #$0C            
F478: 10 F9          BPL     $F473           
F47A: 75 8B          ADC     $8B,X           
F47C: A8             TAY                     
F47D: 8A             TXA                     
F47E: 0A             ASL     A               
F47F: 79 2F F7       ADC     $F72F,Y         
F482: 95 17          STA     $17,X           
F484: 60             RTS                     
F485: A2 01          LDX     #$01            
F487: B5 30          LDA     $30,X           
F489: 10 2C          BPL     $F4B7           
F48B: 24 84          BIT     $84             
F48D: 50 06          BVC     $F495           
F48F: B5 9B          LDA     $9B,X           
F491: C9 1F          CMP     #$1F            
F493: F0 22          BEQ     $F4B7           
F495: F6 95          INC     $95,X           
F497: F6 97          INC     $97,X           
F499: F8             SED                     
F49A: B5 A1          LDA     $A1,X           
F49C: 18             CLC                     
F49D: 69 01          ADC     #$01            
F49F: 95 A1          STA     $A1,X           
F4A1: D8             CLD                     
F4A2: 8A             TXA                     
F4A3: 18             CLC                     
F4A4: 69 FD          ADC     #$FD            
F4A6: 85 8A          STA     $8A             
F4A8: A9 FF          LDA     #$FF            
F4AA: 85 28          STA     $28             
F4AC: 85 29          STA     $29             
F4AE: A9 00          LDA     #$00            
F4B0: 95 19          STA     $19,X           
F4B2: 85 99          STA     $99             
F4B4: 85 9A          STA     $9A             
F4B6: 60             RTS                     
F4B7: 24 A3          BIT     $A3             
F4B9: 10 03          BPL     $F4BE           
F4BB: 4C 42 F5       JMP     $F542           
F4BE: B5 9F          LDA     $9F,X           
F4C0: F0 0A          BEQ     $F4CC           
F4C2: C9 04          CMP     #$04            
F4C4: F6 9F          INC     $9F,X           
F4C6: 90 04          BCC     $F4CC           
F4C8: A9 00          LDA     #$00            
F4CA: 95 9F          STA     $9F,X           
F4CC: B5 34          LDA     $34,X           
F4CE: 30 07          BMI     $F4D7           
F4D0: A9 00          LDA     #$00            
F4D2: 95 9D          STA     $9D,X           
F4D4: 4C 17 F5       JMP     $F517           
F4D7: 24 82          BIT     $82             
F4D9: 50 36          BVC     $F511           
F4DB: B5 9D          LDA     $9D,X           
F4DD: D0 19          BNE     $F4F8           
F4DF: F6 9F          INC     $9F,X           
F4E1: D6 9B          DEC     $9B,X           
F4E3: B5 97          LDA     $97,X           
F4E5: 95 B2          STA     $B2,X           
F4E7: 49 FF          EOR     #$FF            
F4E9: 95 97          STA     $97,X           
F4EB: F6 97          INC     $97,X           
F4ED: B5 97          LDA     $97,X           
F4EF: 29 03          AND     #$03            
F4F1: D0 02          BNE     $F4F5           
F4F3: F6 97          INC     $97,X           
F4F5: 4C 15 F5       JMP     $F515           
F4F8: C9 01          CMP     #$01            
F4FA: F0 0B          BEQ     $F507           
F4FC: C9 03          CMP     #$03            
F4FE: 90 15          BCC     $F515           
F500: D0 13          BNE     $F515           
F502: B5 B2          LDA     $B2,X           
F504: 4C 09 F5       JMP     $F509           
F507: B5 97          LDA     $97,X           
F509: 18             CLC                     
F50A: 69 08          ADC     #$08            
F50C: 95 97          STA     $97,X           
F50E: 4C 15 F5       JMP     $F515           
F511: A9 01          LDA     #$01            
F513: 95 99          STA     $99,X           
F515: F6 9D          INC     $9D,X           
F517: B5 32          LDA     $32,X           
F519: 30 04          BMI     $F51F           
F51B: A5 37          LDA     $37             
F51D: 10 09          BPL     $F528           
F51F: A5 8A          LDA     $8A             
F521: C9 02          CMP     #$02            
F523: 90 09          BCC     $F52E           
F525: 20 49 F5       JSR     $F549           
F528: A9 03          LDA     #$03            
F52A: 95 E4          STA     $E4,X           
F52C: D0 14          BNE     $F542           
F52E: D6 E4          DEC     $E4,X           
F530: 30 06          BMI     $F538           
F532: B5 8B          LDA     $8B,X           
F534: F0 0C          BEQ     $F542           
F536: D0 02          BNE     $F53A           
F538: F6 95          INC     $95,X           
F53A: B5 95          LDA     $95,X           
F53C: 18             CLC                     
F53D: 69 08          ADC     #$08            
F53F: 20 50 F5       JSR     $F550           
F542: CA             DEX                     
F543: 30 03          BMI     $F548           
F545: 4C 87 F4       JMP     $F487           
F548: 60             RTS                     
F549: 8A             TXA                     
F54A: 49 01          EOR     #$01            
F54C: A8             TAY                     
F54D: B9 97 00       LDA     $0097,Y         
F550: 29 0F          AND     #$0F            
F552: A8             TAY                     
F553: B9 1D F6       LDA     $F61D,Y         
F556: 20 BD F2       JSR     $F2BD           
F559: A9 00          LDA     #$00            
F55B: 95 A8          STA     $A8,X           
F55D: 95 AA          STA     $AA,X           
F55F: 95 8D          STA     $8D,X           
F561: B5 D8          LDA     $D8,X           
F563: 95 D6          STA     $D6,X           
F565: 60             RTS                     
F566: A6 85          LDX     $85             
F568: BD CE F7       LDA     $F7CE,X         
F56B: 85 BB          STA     $BB             
F56D: BD D1 F7       LDA     $F7D1,X         
F570: 85 BC          STA     $BC             
F572: A5 A3          LDA     $A3             
F574: 4A             LSR     A               
F575: 4A             LSR     A               
F576: 29 03          AND     #$03            
F578: AA             TAX                     
F579: A5 A3          LDA     $A3             
F57B: 10 0A          BPL     $F587           
F57D: 29 08          AND     #$08            
F57F: F0 04          BEQ     $F585           
F581: A2 03          LDX     #$03            
F583: 10 04          BPL     $F589           
F585: A9 80          LDA     #$80            
F587: 85 82          STA     $82             
F589: A5 A3          LDA     $A3             
F58B: 0A             ASL     A               
F58C: 0A             ASL     A               
F58D: 24 A3          BIT     $A3             
F58F: 30 06          BMI     $F597           
F591: 85 02          STA     $02             
F593: 85 84          STA     $84             
F595: 29 80          AND     #$80            
F597: 85 83          STA     $83             
F599: A9 F7          LDA     #$F7            
F59B: 85 B6          STA     $B6             
F59D: 85 B8          STA     $B8             
F59F: 85 BA          STA     $BA             
F5A1: BD D4 F7       LDA     $F7D4,X         
F5A4: 85 10          STA     $10             
F5A6: 85 B5          STA     $B5             
F5A8: BD D8 F7       LDA     $F7D8,X         
F5AB: 85 B7          STA     $B7             
F5AD: BD DC F7       LDA     $F7DC,X         
F5B0: 85 B9          STA     $B9             
F5B2: 60             RTS                     
F5B3: A9 00          LDA     #$00            
F5B5: E8             INX                     
F5B6: 95 A2          STA     $A2,X           
F5B8: D0 FB          BNE     $F5B5           
F5BA: 60             RTS                     
; -----------------------------------------------------------------------------------------------------------------------------

```
# Data Area

All data from here down

## Numbers 

```html
<canvas width="900" height="60"
    data-getTileDataFunction="Stella.get8x5Data"
    data-address="F5BB"
    data-gridX="8"
    data-gridY="5"
    data-command="#TANKPLAYFIELD,0,+x,1,+x,2,+x,3,+x,4,+x,5,+x,6,+x,7,+x,8,+x,9">
</canvas>
```

```code
F5BB: 0E 0A 0A 0A 0E  ;  0
 ; .... ***.
 ; .... *.*.
 ; .... *.*.
 ; .... *.*.
 ; .... ****
 
F5C0: 22 22 22 22 22  ; 11  
; ..*. ..*.
; ..*. ..*.
; ..*. ..*.
; ..*. ..*.
; ..*. ..*.

F5C5: EE 22 EE 88 EE  ; 22
; ***. ***.
; ..*. ..*.
; ***. ***.
; *... *...
; ***. ***.

F5CA: EE 22 66 22 EE  ; 33
; ***. ***.
; ..*. ..*.
; .**. .**.
; ..*. ..*.
; ***. ***.

F5CF: AA AA EE 22 22  ; 44
; *.*. *.*.
; *.*. *.*.
; ***. ***.
; ..*. ..*.

F5D4: EE 88 EE 22 EE  ; 55
; ***. ***.
; *... *...
; ***. ***.
; ..*. ..*.
; ***. ***.

F5D9: EE 88 EE AA EE  ; 66
; ***. ***.
; *... *...
; ***. ***.
; *.*. *.*.
; ***. ***.

F5DE: EE 22 22 22 22  ; 77
; ***. ***.
; ..*. ..*.
; ..*. ..*.
; ..*. ..*.
; ..*. ..*.

F5E3: EE AA EE AA EE  ; 88
; ***. ***.
; *.*. *.*.
; ***. ***.
; *.*. *.*.
; ***. ***.

F5E8: EE AA EE 22 EE  ; 99 
; ***. ***.
; *.*. *.*.
; ***. ***.
; ..*. ..*.
; ***. ***.  
      
F5ED: F8                                  
F5EE: F7                           
F5EF: F6 06                 
F5F1: 06 06                  
F5F3: 16 17                  
F5F5: 18                                  
F5F6: 19 1A 0A            
F5F9: 0A                        
F5FA: 0A                        
F5FB: FA                                
F5FC: F9 F8 F7              
F5FF: F6 F6                   
F601: 06 16                      
F603: 16 17                 
  
F605: 18                                
F606: 19 1A 1A             
F609: 0A                           
F60A: FA                                  
F60B: FA                                 
F60C: F9 E8 E6              
F60F: E4 F4                    
F611: 04                                
F612: 14                                 
F613: 24 26                     
F615: 28                                  
F616: 2A                           
F617: 2C 1C 0C                 
F61A: FC                                 
F61B: EC EA C8                  
F61E: C4 C0                      
F620: E0 00                    
F622: 20 40 44                 
F625: 48                                  
F626: 4C 4F 2F                
F629: 0F                                 
F62A: EF                               
F62B: CF                                 
F62C: CC 00 00                 
F62F: 80                                 
F630: 80                                 
F631: 84 20                     
F633: 88                                
F634: 88                                
F635: 92                                 
F636: 48                               
F637: A4 A4                     
F639: A9 52                   
F63B: AA                                
F63C: AA                             
F63D: D5 AA                  
F63F: DA                                 
F640: DA                                 
F641: DB                                 
F642: 6D EE EE            
```

## Tank Pictures 

```html
<canvas width="1000" height="100"
    data-getTileDataFunction="Stella.get8x8Data"
    data-address="F645"
    data-gridX="8"
    data-gridY="8"
    data-command="#TANKP0,0,+x,1,+x,2,+x,3,+x,4,+x,5,+x,6,+x,7">
</canvas 
```

```code
F645: 00 FC FC 38 3F 38 FC FC             
F64D: 1C 78 FB 7C 1C 1F 3E 18 
F655: 19 3A 7C FF DF 0E 1C 18        
F65D: 24 64 79 FF FF 4E 0E 04        
F665: 08 08 6B 7F 7F 7F 63 63             
F66D: 24 26 9E FF FF 72 70 20      
F675: 98 5C 3E FF FB 70 38 18       
F67D: 38 1E DF 3E 38 F8 7C 18
```

## Jet Pictures 

```html
<canvas width="1000" height="100"
    data-getTileDataFunction="Stella.get8x8Data"
    data-address="F685"
    data-gridX="8"
    data-gridY="8"
    data-command="#JETP0,0,+x,1,+x,2,+x,3,+x,4,+x,5,+x,6,+x,7">
</canvas>
```

```code        
F685: 60 70 78 FF 78 70 60 00            
F68D: 00 C1 FE 7C 78 30 30 30 
F695: 00 03 06 FC FC 3C 0C 0C               
F69D: 02 04 0C 1C FC FC 1E 06 
F6A5: 10 10 10 38 7C FE FE 10 
F6AD: 40 20 30 38 3F 3F 78 60          
F6B5: 40 60 3F 1F 1E 1E 18 18           
F6BD: 00 83 7F 3E 1E 0C 0C 0C       
```

## Plane Pictures 

```html
<canvas width="1000" height="100"
    data-getTileDataFunction="Stella.get8x8Data"
    data-address="F6C5"
    data-gridX="8"
    data-gridY="8"
    data-command="#PLANEP0,0,+x,1,+x,2,+x,3,+x,4,+x,5,+x,6,+x,7">
</canvas>
```   

```code
F6C5: 00 8E 84 FF FF 04 0E 00 
F6CD: 00 0E 04 8F 7F 72 07 00                                  
F6D5: 10 36 2E 0C 1F B2 E0 40                    
F6DD: 24 2C 5D 1A 1A 30 F0 60                                  
F6E5: 18 5A 7E 5A 18 18 18 78                                  
F6ED: 34 36 5A 78 2C 0C 06 0C                                 
F6F5: 08 6C 70 B8 DC 4E 07 06                
F6FD: 38 10 F0 7C 4F E3 02 00              
                    
F705: 00                                  
F706: 0B                                
F707: 16 00                   
F709: 10 00                    
F70B: FF                                 
F70C: 01 11                  
F70E: 01 FF                  
F710: 0F                                
F711: 1F                                 
F712: 0F                               
F713: 50 5F                   
F715: 51 FF                
F717: 30 3F                    
F719: 31 FF                
F71B: 70 7F                    
F71D: 71 90                  
F71F: B0 70                  
F721: FF                                 
F722: 91 B1                 
F724: 71 FF            
F726: 9F                                  
F727: BF                                  
F728: 7F                                  
F729: 08                                  
F72A: 02                                 
F72B: 02                                  
F72C: 02                                  
F72D: 03                                  
F72E: 08                                  
F72F: 1D 05 00               
F732: 00                                  
F733: 00                                  
F734: 00                                  
F735: 00                                  
F736: 00                                  
F737: 00                                  
F738: 00                                  
F739: 00                                  
F73A: 00                                  
F73B: 00                                  
F73C: 00                                  
F73D: 1D 1D 16               
F740: 16 0F                 
F742: 0F                              
F743: 00                                
F744: 00                           
F745: 00                             
F746: 00                              
F747: 00                         
F748: 00                              
F749: 00                                
F74A: 00                                
F74B: 00                                
F74C: 12                                 
F74D: 10 10                    
F74F: 0C                                 
F750: 0C                                
F751: 07                                
F752: 07                             

plyrNumSize:
; Number/size of players, width of missile
;                    copies    width            copies    width
F753: 10 10   ; P0 = 1         2           P1 = 1         2 
F755: 11 11   ; P0 = 2 close   2           P1 = 2 close   2        
F757: 10 13   ; P0 = 1         2           P1 = 3 close   2
F759: 27 13   ; P0 = 1 quad    4           P1 = 3 close   2
                     
F75B: 32                                
F75C: 2C 8A DA                
F75F: D2                                  
F760: 2C 6A 3A                  
F763: B2                               
F764: 9C                                 
F765: 5A                                 
F766: 2A                           
F767: B2                                 
F768: 0C                                
F769: 3A                                 
F76A: 6A                          
F76B: 08                                  
F76C: 04                               
F76D: 00                               
F76E: 0E 

; - Empty tank field
; - Simple tank field
; - Complex tank field
; - Clouds
; The empty-air-field is just no playfield at all

; Each pattern has three tables of 15 bytes. Each pattern is used over 8 rows.
; 15*2*8 = 240 rows of the playfield

; 15 bytes each mirrored left, right, top, bottom

; PF0 for all tank levels
F76F: F0 10 10 10 10 10 10 10 10 10 10 10 10 10 10 

; PF1 for complex tanks 
F77E: FF 00 00 00 38 00 00 00 00 60 20 20 20 23 23         

; PF2 for complex tanks   
F78D: FF 80 80 00 00 00 1C 04 04 00 00 00 00 00 00
      
; PF1 and PF2 for blank tanks (vertical line)         
F79C: FF             
         
; PF0 for air (all off)             
F79D: 00 00 00

; PF1 and PF2 for air                  
F7A0: 00 00 00 00 00 00 00 00 00 00 00 00 07 1F 3F              

; If you start the clouds PF1 and PF2 at F7A1 then this makes a fatter cloud!
; You could also back up for smaller clouds. I bet the larger cloud was
; intended for a second air playfield ... different for planes and jets.
; Maybe they ran out of code space to use it. 
F7AF: 7F
                     
; PF1 for simple tanks
F7B0: FF 00 00 00 00 00 00 00 00 00 60 20 20 20 21 

; PF2 for simple tanks 
F7BF: FF 00 00 00 80 80 80 80 00 00 00 00 00 00 07       

; Pointers to player pictures 0=tank, 1=jet, 2=plane         
F7CE: 45 C5 85 ; Picture pointers LSB 
F7D1: F6 F6 F6 ; Picture pointers MSB

; Four different play fields
; F76F, F77E, F78D  ' Complex tanks
; F76F, F79C, F79C  ' Blank tanks
; F76F, F7B0, F7BF  ' Simple tanks
; F79D, F7A0, F7A0  ' Clouds

;      0  1  2  3      
F7D4: 6E 6E 6E 9C ; PF0 LSB (add 1 the drawing loop treats this as entries 1 through 16)            
F7D8: 7D 9B AF 9F ; PF1 LSB (add 1)            
F7DC: 8C 9B BE 9F ; PF2 LSB (add 1)
```

## Playfields 

```html
<canvas width="410" height="320"
        data-getTileDataFunction="Combat.getPlayfieldPAL"
        data-pixWidth="20"
        data-pixHeight="20"
        data-gap="0.5"
        data-gridPad="2"
        data-gridX="20"
        data-gridY="15"
        data-command="#TANKPLAYFIELD,0">
</canvas> 
<canvas width="325" height="320"
        data-getTileDataFunction="Combat.getPlayfieldPAL"
        data-pixWidth="8"
        data-pixHeight="8"
        data-gap="0.25"
        data-gridPad="1"
        data-gridX="20"
        data-gridY="15"
        data-command="#TANKPLAYFIELD,0,H0,*,V0,VH0">
</canvas><br>
```

```html
<canvas width="410" height="320"
        data-getTileDataFunction="Combat.getPlayfieldPAL"
        data-pixWidth="20"
        data-pixHeight="20"
        data-gap="0.5"
        data-gridPad="2"
        data-gridX="20"
        data-gridY="15"
        data-command="#TANKPLAYFIELD,1">
</canvas> 
<canvas width="325" height="320"
        data-getTileDataFunction="Combat.getPlayfieldPAL"
        data-pixWidth="8"
        data-pixHeight="8"
        data-gap="0.25"
        data-gridPad="1"
        data-gridX="20"
        data-gridY="15"
        data-command="#TANKPLAYFIELD,1,H1,*,V1,VH1">
</canvas><br> 
```

```html
<canvas width="410" height="320"
        data-getTileDataFunction="Combat.getPlayfieldPAL"
        data-pixWidth="20"
        data-pixHeight="20"
        data-gap="0.5"
        data-gridPad="2"
        data-gridX="20"
        data-gridY="15"
        data-command="#TANKPLAYFIELD,2">
</canvas> 
<canvas width="325" height="320"
        data-getTileDataFunction="Combat.getPlayfieldPAL"
        data-pixWidth="8"
        data-pixHeight="8"
        data-gap="0.25"
        data-gridPad="1"
        data-gridX="20"
        data-gridY="15"
        data-command="#TANKPLAYFIELD,2,H2,*,V2,VH2">
</canvas><br> 
```

```html
<canvas width="410" height="320"
        data-getTileDataFunction="Combat.getPlayfieldPAL"
        data-pixWidth="20"
        data-pixHeight="20"
        data-gap="0.5"
        data-gridPad="2"
        data-gridX="20"
        data-gridY="15"
        data-command="#PLANEPLAYFIELD,3">
</canvas> 
<canvas width="325" height="320"
        data-getTileDataFunction="Combat.getPlayfieldPAL"
        data-pixWidth="8"
        data-pixHeight="8"
        data-gap="0.25"
        data-gridPad="1"
        data-gridX="20"
        data-gridY="15"
        data-command="#PLANEPLAYFIELD,3,H3,*,V3,VH3">
</canvas><br> 
```

```code                  
F7E0: 24 28                    
F7E2: 08                                  
F7E3: 20 00 48                
F7E6: 40                                  
F7E7: 54                                 
F7E8: 58                                  
F7E9: 25 29                     
F7EB: 49 55                     
F7ED: 59 A8 88             
F7F0: 98                                  
F7F1: 90 A1                  
F7F3: 83                                  
F7F4: E8                                  
F7F5: C8                                
F7F6: E0 C0         
F7F8: E9 E2      
```
 
# Vectors

```code 
F7FA: C1 FF        ; NMI Vector (not used -- maybe this was a debugger address)         
F7FC: 00 F0        ; Reset vector to F000
F7FE: 0F 11        ; IRQ/vector to 110F (maybe debug hardware?)
```
