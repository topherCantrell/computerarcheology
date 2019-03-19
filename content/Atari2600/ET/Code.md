![ET](A2600ET.jpg)

# ET

>>> cpu 6502

>>> memoryTable hard 
[Hardware Info](../Stella.md)

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

```code
; This cartridge uses the "F8" bank-switching hardware. This is a single 8K ROM 
; with the switching built into it. You read location FFF8 to switch to bank 0. 
; You read location FFF9 to switch to bank 1.

; The upper bits of the ROM address do not matter. But based on the assembly code 
; I can tell that bank 0 was origined at B000 and bank 1 was origined at F000.

B000: AD F8 FF   LDA $FFF8           ; Switch to bank 0 (this bank ... interesting)
B003: 4C 7F BC   JMP $BC7F           ; Continue startup

B006: A2 04      LDX #$04            ; 
B008: 85 02      STA <$02            ;{-2_WSYNC} 
B00A: B5 95      LDA $95,X           ; 
B00C: A8         TAY                 ; 
B00D: B9 00 BC   LDA $BC00,Y         ; 
B010: 95 20      STA $20,X           ; 
B012: 29 0F      AND #$0F            ; 
B014: A8         TAY                 ; 
B015: 88         DEY                 ; 
B016: 10 FD      BPL $B015           ; 
B018: 95 10      STA $10,X           ; 
B01A: CA         DEX                 ; 
B01B: 10 EB      BPL $B008           ; 
B01D: 85 02      STA <$02            ;{-2_WSYNC} 
B01F: 85 2A      STA <$2A            ;{-2_HMOVE} 
B021: 68         PLA                 ; 
B022: 85 96      STA <$96            ; 
B024: AA         TAX                 ; 
B025: BD 00 BC   LDA $BC00,X         ; 
B028: 85 D5      STA <$D5            ; 
B02A: 4C AB BC   JMP $BCAB           ; 
```

# Game Logic

```code
; The code comes here from F4CE after the switch from bank 1. This is the
; vertical retrace period.

; Near the end of scanline 223
B02D: A5 E2      LDA <$E2            ; 
B02F: 10 09      BPL $B03A           ; 
B031: 29 7F      AND #$7F            ; 
B033: 85 80      STA <$80            ; 
B035: 20 E3 BA   JSR $BAE3           ; 
B038: 46 E2      LSR <$E2            ; 
B03A: 24 EB      BIT <$EB            ; 
B03C: 30 06      BMI $B044           ; 
B03E: A5 80      LDA <$80            ; 
B040: C9 08      CMP #$08            ; 
B042: D0 03      BNE $B047           ; 
B044: 4C 38 B4   JMP $B438           ; 
B047: A5 80      LDA <$80            ; 
B049: C9 07      CMP #$07            ; 
B04B: D0 03      BNE $B050           ; 
B04D: 4C 38 B4   JMP $B438           ; 
B050: 24 E3      BIT <$E3            ; 
B052: 10 1B      BPL $B06F           ; 
B054: 50 19      BVC $B06F           ; 
B056: A5 A1      LDA <$A1            ; 
B058: 10 15      BPL $B06F           ; 
B05A: A2 01      LDX #$01            ; 
B05C: 86 A1      STX <$A1            ; 
B05E: 20 90 BE   JSR $BE90           ; 
B061: A9 0E      LDA #$0E            ; 
B063: 85 A3      STA <$A3            ; 
B065: A5 80      LDA <$80            ; 
B067: 85 A6      STA <$A6            ; 
B069: A9 05      LDA #$05            ; 
B06B: 85 A9      STA <$A9            ; 
B06D: 85 AC      STA <$AC            ; 
B06F: 24 94      BIT <$94            ; 
B071: 10 03      BPL $B076           ; 
B073: 4C 53 B1   JMP $B153           ; 
B076: 24 37      BIT <$37            ; 
B078: 10 F9      BPL $B073           ; 
B07A: A6 A1      LDX <$A1            ; 
B07C: 10 03      BPL $B081           ; 
B07E: 4C 39 B1   JMP $B139           ; 
B081: B5 A2      LDA $A2,X           ; 
B083: 30 EE      BMI $B073           ; 
B085: 8A         TXA                 ; 
B086: D0 1E      BNE $B0A6           ; 
B088: A2 02      LDX #$02            ; 
B08A: B5 CA      LDA $CA,X           ; 
B08C: 30 09      BMI $B097           ; 
B08E: CA         DEX                 ; 
B08F: 10 F9      BPL $B08A           ; 
B091: A9 0A      LDA #$0A            ; 
B093: 85 D2      STA <$D2            ; 
B095: D0 08      BNE $B09F           ; 
B097: A5 81      LDA <$81            ; 
B099: 29 0F      AND #$0F            ; 
B09B: 09 20      ORA #$20            ; 
B09D: 95 CA      STA $CA,X           ; 
B09F: A9 9C      LDA #$9C            ; 
B0A1: 85 8A      STA <$8A            ; 
B0A3: 4C 30 B1   JMP $B130           ; 
B0A6: E0 02      CPX #$02            ; 
B0A8: D0 12      BNE $B0BC           ; 
B0AA: A5 91      LDA <$91            ; 
B0AC: 09 40      ORA #$40            ; 
B0AE: 85 91      STA <$91            ; 
B0B0: 26 A2      ROL <$A2            ; 
B0B2: 38         SEC                 ; 
B0B3: 66 A2      ROR <$A2            ; 
B0B5: 26 A3      ROL <$A3            ; 
B0B7: 38         SEC                 ; 
B0B8: 66 A3      ROR <$A3            ; 
B0BA: D0 74      BNE $B130           ; 
B0BC: A9 8C      LDA #$8C            ; 
B0BE: 85 8A      STA <$8A            ; 
B0C0: 24 E3      BIT <$E3            ; 
B0C2: 10 25      BPL $B0E9           ; 
B0C4: A4 E5      LDY <$E5            ; 
B0C6: 10 0B      BPL $B0D3           ; 
B0C8: 26 E4      ROL <$E4            ; 
B0CA: 38         SEC                 ; 
B0CB: 66 E4      ROR <$E4            ; 
B0CD: 20 AA BF   JSR $BFAA           ; 
B0D0: 4C 38 B4   JMP $B438           ; 
B0D3: C6 E5      DEC <$E5            ; 
B0D5: A2 15      LDX #$15            ; 
B0D7: A0 00      LDY #$00            ; 
B0D9: 20 8E BF   JSR $BF8E           ; 
B0DC: 84 8C      STY <$8C            ; 
B0DE: 84 E3      STY <$E3            ; 
B0E0: 88         DEY                 ; 
B0E1: 84 A1      STY <$A1            ; 
B0E3: 84 A6      STY <$A6            ; 
B0E5: 84 A3      STY <$A3            ; 
B0E7: D0 47      BNE $B130           ; 
B0E9: A2 00      LDX #$00            ; 
B0EB: A9 10      LDA #$10            ; 
B0ED: 24 CA      BIT <$CA            ; 
B0EF: D0 0A      BNE $B0FB           ; 
B0F1: E8         INX                 ; 
B0F2: 24 CB      BIT <$CB            ; 
B0F4: D0 05      BNE $B0FB           ; 
B0F6: E8         INX                 ; 
B0F7: 24 CC      BIT <$CC            ; 
B0F9: F0 06      BEQ $B101           ; 
B0FB: A9 80      LDA #$80            ; 
B0FD: 95 CA      STA $CA,X           ; 
B0FF: D0 2F      BNE $B130           ; 
B101: A5 D2      LDA <$D2            ; 
B103: 4A         LSR A               ; 
B104: 4A         LSR A               ; 
B105: 4A         LSR A               ; 
B106: 4A         LSR A               ; 
B107: F0 27      BEQ $B130           ; 
B109: 18         CLC                 ; 
B10A: 65 DD      ADC <$DD            ; 
B10C: 85 DD      STA <$DD            ; 
B10E: A5 D2      LDA <$D2            ; 
B110: C9 90      CMP #$90            ; 
B112: 90 16      BCC $B12A           ; 
B114: A2 02      LDX #$02            ; 
B116: A9 F0      LDA #$F0            ; 
B118: 24 CC      BIT <$CC            ; 
B11A: F0 0A      BEQ $B126           ; 
B11C: CA         DEX                 ; 
B11D: 24 CB      BIT <$CB            ; 
B11F: F0 05      BEQ $B126           ; 
B121: CA         DEX                 ; 
B122: 24 CA      BIT <$CA            ; 
B124: D0 04      BNE $B12A           ; 
B126: A9 10      LDA #$10            ; 
B128: 95 CA      STA $CA,X           ; 
B12A: A5 D2      LDA <$D2            ; 
B12C: 29 0F      AND #$0F            ; 
B12E: 85 D2      STA <$D2            ; 
B130: A6 A1      LDX <$A1            ; 
B132: 36 A2      ROL $A2,X           ; 
B134: 38         SEC                 ; 
B135: 76 A2      ROR <$A2,X          ; 
B137: 30 1A      BMI $B153           ; 
B139: E0 86      CPX #$86            ; 
B13B: B0 16      BCS $B153           ; 
B13D: A9 8D      LDA #$8D            ; 
B13F: 85 8A      STA <$8A            ; 
B141: 8A         TXA                 ; 
B142: 29 0F      AND #$0F            ; 
B144: 38         SEC                 ; 
B145: E9 03      SBC #$03            ; 
B147: AA         TAX                 ; 
B148: C9 03      CMP #$03            ; 
B14A: B0 07      BCS $B153           ; 
B14C: A9 80      LDA #$80            ; 
B14E: 95 CA      STA $CA,X           ; 
B150: 0A         ASL A               ; 
B151: 85 8C      STA <$8C            ; 
B153: A5 80      LDA <$80            ; 
B155: C9 04      CMP #$04            ; 
B157: 90 03      BCC $B15C           ; 
B159: 4C E8 B1   JMP $B1E8           ; 
B15C: 24 91      BIT <$91            ; 
B15E: 70 F9      BVS $B159           ; 
B160: 24 33      BIT <$33            ; 
B162: 30 06      BMI $B16A           ; 
B164: A9 00      LDA #$00            ; 
B166: 85 D9      STA <$D9            ; 
B168: F0 EF      BEQ $B159           ; 
B16A: 24 94      BIT <$94            ; 
B16C: 30 EB      BMI $B159           ; 
B16E: A5 9C      LDA <$9C            ; 
B170: 85 D7      STA <$D7            ; 
B172: A5 96      LDA <$96            ; 
B174: 85 D6      STA <$D6            ; 
B176: A0 00      LDY #$00            ; 
B178: A6 80      LDX <$80            ; 
B17A: 86 D8      STX <$D8            ; 
B17C: F0 20      BEQ $B19E           ; 
B17E: CA         DEX                 ; 
B17F: F0 39      BEQ $B1BA           ; 
B181: CA         DEX                 ; 
B182: F0 04      BEQ $B188           ; 
B184: A2 0C      LDX #$0C            ; 
B186: D0 02      BNE $B18A           ; 
B188: A2 08      LDX #$08            ; 
B18A: 86 83      STX <$83            ; 
B18C: C9 3B      CMP #$3B            ; 
B18E: 90 01      BCC $B191           ; 
B190: C8         INY                 ; 
B191: A5 9C      LDA <$9C            ; 
B193: C9 21      CMP #$21            ; 
B195: 90 02      BCC $B199           ; 
B197: C8         INY                 ; 
B198: C8         INY                 ; 
B199: 98         TYA                 ; 
B19A: 05 83      ORA <$83            ; 
B19C: D0 41      BNE $B1DF           ; 
B19E: C9 29      CMP #$29            ; 
B1A0: B0 04      BCS $B1A6           ; 
B1A2: A9 01      LDA #$01            ; 
B1A4: D0 39      BNE $B1DF           ; 
B1A6: C9 51      CMP #$51            ; 
B1A8: 90 04      BCC $B1AE           ; 
B1AA: A9 02      LDA #$02            ; 
B1AC: D0 31      BNE $B1DF           ; 
B1AE: A5 9C      LDA <$9C            ; 
B1B0: C9 1D      CMP #$1D            ; 
B1B2: A9 00      LDA #$00            ; 
B1B4: 90 29      BCC $B1DF           ; 
B1B6: A9 03      LDA #$03            ; 
B1B8: D0 25      BNE $B1DF           ; 
B1BA: A6 9C      LDX <$9C            ; 
B1BC: E0 13      CPX #$13            ; 
B1BE: 90 06      BCC $B1C6           ; 
B1C0: E0 28      CPX #$28            ; 
B1C2: 90 13      BCC $B1D7           ; 
B1C4: A0 03      LDY #$03            ; 
B1C6: C9 20      CMP #$20            ; 
B1C8: 90 09      BCC $B1D3           ; 
B1CA: C9 60      CMP #$60            ; 
B1CC: B0 05      BCS $B1D3           ; 
B1CE: 98         TYA                 ; 
B1CF: 09 04      ORA #$04            ; 
B1D1: D0 0C      BNE $B1DF           ; 
B1D3: A9 FF      LDA #$FF            ; 
B1D5: D0 08      BNE $B1DF           ; 
B1D7: C8         INY                 ; 
B1D8: C9 40      CMP #$40            ; 
B1DA: 90 F2      BCC $B1CE           ; 
B1DC: C8         INY                 ; 
B1DD: D0 EF      BNE $B1CE           ; 
B1DF: 85 DA      STA <$DA            ; 
B1E1: A9 06      LDA #$06            ; 
B1E3: 85 80      STA <$80            ; 
B1E5: 20 E3 BA   JSR $BAE3           ; 
B1E8: A5 81      LDA <$81            ; 
B1EA: 29 03      AND #$03            ; 
B1EC: C9 03      CMP #$03            ; 
B1EE: F0 54      BEQ $B244           ; 
B1F0: AA         TAX                 ; 
B1F1: B5 A5      LDA $A5,X           ; 
B1F3: 10 29      BPL $B21E           ; 
B1F5: B5 A2      LDA $A2,X           ; 
B1F7: 30 4B      BMI $B244           ; 
B1F9: A9 05      LDA #$05            ; 
B1FB: 20 80 BF   JSR $BF80           ; 
B1FE: B0 44      BCS $B244           ; 
B200: 95 A5      STA $A5,X           ; 
B202: BD 95 BD   LDA $BD95,X         ; 
B205: 95 AB      STA $AB,X           ; 
B207: BD 92 BD   LDA $BD92,X         ; 
B20A: 95 A8      STA $A8,X           ; 
B20C: A9 0B      LDA #$0B            ; 
B20E: 95 A2      STA $A2,X           ; 
B210: A9 05      LDA #$05            ; 
B212: C5 80      CMP <$80            ; 
B214: D0 2E      BNE $B244           ; 
B216: 86 A1      STX <$A1            ; 
B218: 20 90 BE   JSR $BE90           ; 
B21B: 4C 44 B2   JMP $B244           ; 
B21E: 0A         ASL A               ; 
B21F: 0A         ASL A               ; 
B220: 0A         ASL A               ; 
B221: 85 83      STA <$83            ; 
B223: B5 A2      LDA $A2,X           ; 
B225: 10 05      BPL $B22C           ; 
B227: A9 05      LDA #$05            ; 
B229: 18         CLC                 ; 
B22A: 90 06      BCC $B232           ; 
B22C: A5 80      LDA <$80            ; 
B22E: C9 06      CMP #$06            ; 
B230: B0 12      BCS $B244           ; 
B232: 65 83      ADC <$83            ; 
B234: A8         TAY                 ; 
B235: B9 FC BD   LDA $BDFC,Y         ; 
B238: 30 0A      BMI $B244           ; 
B23A: 85 83      STA <$83            ; 
B23C: B5 A2      LDA $A2,X           ; 
B23E: 29 F0      AND #$F0            ; 
B240: 05 83      ORA <$83            ; 
B242: 95 A2      STA $A2,X           ; 
B244: 24 33      BIT <$33            ; 
B246: 50 1F      BVC $B267           ; 
B248: A6 80      LDX <$80            ; 
B24A: E0 04      CPX #$04            ; 
B24C: B0 19      BCS $B267           ; 
B24E: A5 D2      LDA <$D2            ; 
B250: C9 90      CMP #$90            ; 
B252: B0 13      BCS $B267           ; 
B254: 69 10      ADC #$10            ; 
B256: 85 D2      STA <$D2            ; 
B258: A9 9C      LDA #$9C            ; 
B25A: 85 8A      STA <$8A            ; 
B25C: A9 7F      LDA #$7F            ; 
B25E: 85 9F      STA <$9F            ; 
B260: BD 50 BE   LDA $BE50,X         ; 
B263: 25 D1      AND <$D1            ; 
B265: 85 D1      STA <$D1            ; 
B267: A5 82      LDA <$82            ; 
B269: 29 0F      AND #$0F            ; 
B26B: D0 1D      BNE $B28A           ; 
B26D: A5 81      LDA <$81            ; 
B26F: 29 3F      AND #$3F            ; 
B271: C9 17      CMP #$17            ; 
B273: D0 15      BNE $B28A           ; 
B275: A5 D1      LDA <$D1            ; 
B277: 29 0F      AND #$0F            ; 
B279: AA         TAX                 ; 
B27A: A5 DC      LDA <$DC            ; 
B27C: 38         SEC                 ; 
B27D: FD 58 BE   SBC $BE58,X         ; 
B280: 30 08      BMI $B28A           ; 
B282: 85 DC      STA <$DC            ; 
B284: A9 0F      LDA #$0F            ; 
B286: 05 D1      ORA <$D1            ; 
B288: 85 D1      STA <$D1            ; 
B28A: 24 94      BIT <$94            ; 
B28C: 30 03      BMI $B291           ; 
B28E: 4C CE B3   JMP $B3CE           ; 
B291: A5 81      LDA <$81            ; 
B293: 29 03      AND #$03            ; 
B295: D0 25      BNE $B2BC           ; 
B297: 50 26      BVC $B2BF           ; 
B299: 24 D9      BIT <$D9            ; 
B29B: 70 1F      BVS $B2BC           ; 
B29D: C6 94      DEC <$94            ; 
B29F: A5 94      LDA <$94            ; 
B2A1: 29 07      AND #$07            ; 
B2A3: C9 07      CMP #$07            ; 
B2A5: F0 04      BEQ $B2AB           ; 
B2A7: E6 9C      INC <$9C            ; 
B2A9: D0 11      BNE $B2BC           ; 
B2AB: A9 00      LDA #$00            ; 
B2AD: 85 94      STA <$94            ; 
B2AF: E6 9C      INC <$9C            ; 
B2B1: A2 02      LDX #$02            ; 
B2B3: B5 CA      LDA $CA,X           ; 
B2B5: 29 BF      AND #$BF            ; 
B2B7: 95 CA      STA $CA,X           ; 
B2B9: CA         DEX                 ; 
B2BA: 10 F7      BPL $B2B3           ; 
B2BC: 4C A1 B3   JMP $B3A1           ; 
B2BF: E6 94      INC <$94            ; 
B2C1: A5 94      LDA <$94            ; 
B2C3: 29 07      AND #$07            ; 
B2C5: C9 04      CMP #$04            ; 
B2C7: B0 09      BCS $B2D2           ; 
B2C9: A5 9C      LDA <$9C            ; 
B2CB: F0 02      BEQ $B2CF           ; 
B2CD: C6 9C      DEC <$9C            ; 
B2CF: 4C A1 B3   JMP $B3A1           ; 
B2D2: A9 C3      LDA #$C3            ; 
B2D4: 85 94      STA <$94            ; 
B2D6: A2 00      LDX #$00            ; 
B2D8: A0 19      LDY #$19            ; 
B2DA: 20 CF BF   JSR $BFCF           ; 
B2DD: A4 80      LDY <$80            ; 
B2DF: A5 CF      LDA <$CF            ; 
B2E1: 0A         ASL A               ; 
B2E2: AA         TAX                 ; 
B2E3: BD 2F BE   LDA $BE2F,X         ; 
B2E6: 48         PHA                 ; 
B2E7: BD 2E BE   LDA $BE2E,X         ; 
B2EA: 48         PHA                 ; 
B2EB: A5 EA      LDA <$EA            ; 
B2ED: C9 02      CMP #$02            ; 
B2EF: B0 09      BCS $B2FA           ; 
B2F1: A5 A7      LDA <$A7            ; 
B2F3: 10 05      BPL $B2FA           ; 
B2F5: 26 A4      ROL <$A4            ; 
B2F7: 18         CLC                 ; 
B2F8: 66 A4      ROR <$A4            ; 
B2FA: 60         RTS                 ; 
B2FB: 24 E6      BIT <$E6            ; 
B2FD: 30 11      BMI $B310           ; 
B2FF: E6 E5      INC <$E5            ; 
B301: 26 E6      ROL <$E6            ; 
B303: 38         SEC                 ; 
B304: 66 E6      ROR <$E6            ; 
B306: 30 08      BMI $B310           ; 
B308: A9 40      LDA #$40            ; 
B30A: 85 D9      STA <$D9            ; 
B30C: C6 9C      DEC <$9C            ; 
B30E: C6 9C      DEC <$9C            ; 
B310: 4C A1 B3   JMP $B3A1           ; 
B313: A2 02      LDX #$02            ; 
B315: B5 CA      LDA $CA,X           ; 
B317: 29 F0      AND #$F0            ; 
B319: D0 0A      BNE $B325           ; 
B31B: B5 CA      LDA $CA,X           ; 
B31D: 29 0F      AND #$0F            ; 
B31F: 4A         LSR A               ; 
B320: 4A         LSR A               ; 
B321: C5 80      CMP <$80            ; 
B323: F0 06      BEQ $B32B           ; 
B325: CA         DEX                 ; 
B326: 10 ED      BPL $B315           ; 
B328: 4C A1 B3   JMP $B3A1           ; 
B32B: B5 CA      LDA $CA,X           ; 
B32D: 09 40      ORA #$40            ; 
B32F: 95 CA      STA $CA,X           ; 
B331: D0 F5      BNE $B328           ; 
B333: B9 80 BD   LDA $BD80,Y         ; 
B336: 4C 48 B3   JMP $B348           ; 
B339: B9 7A BD   LDA $BD7A,Y         ; 
B33C: 4C 48 B3   JMP $B348           ; 
B33F: B9 86 BD   LDA $BD86,Y         ; 
B342: 4C 48 B3   JMP $B348           ; 
B345: B9 8C BD   LDA $BD8C,Y         ; 
B348: 85 80      STA <$80            ; 
B34A: 20 E3 BA   JSR $BAE3           ; 
B34D: 4C A1 B3   JMP $B3A1           ; 
B350: 26 A3      ROL <$A3            ; 
B352: 18         CLC                 ; 
B353: 66 A3      ROR <$A3            ; 
B355: 10 4A      BPL $B3A1           ; 
B357: A6 A1      LDX <$A1            ; 
B359: 30 09      BMI $B364           ; 
B35B: 2C 82 02   BIT $0282           ; 
B35E: 70 41      BVS $B3A1           ; 
B360: E0 01      CPX #$01            ; 
B362: D0 3D      BNE $B3A1           ; 
B364: A5 D0      LDA <$D0            ; 
B366: 10 39      BPL $B3A1           ; 
B368: 24 CA      BIT <$CA            ; 
B36A: 10 35      BPL $B3A1           ; 
B36C: 24 CB      BIT <$CB            ; 
B36E: 10 31      BPL $B3A1           ; 
B370: 24 CC      BIT <$CC            ; 
B372: 10 2D      BPL $B3A1           ; 
B374: A9 8C      LDA #$8C            ; 
B376: 85 8A      STA <$8A            ; 
B378: A9 3F      LDA #$3F            ; 
B37A: 85 D0      STA <$D0            ; 
B37C: A9 8F      LDA #$8F            ; 
B37E: 85 A2      STA <$A2            ; 
B380: 85 A3      STA <$A3            ; 
B382: 85 A4      STA <$A4            ; 
B384: D0 1B      BNE $B3A1           ; 
B386: A6 A1      LDX <$A1            ; 
B388: 30 17      BMI $B3A1           ; 
B38A: 36 A2      ROL $A2,X           ; 
B38C: 38         SEC                 ; 
B38D: 76 A2      ROR <$A2,X          ; 
B38F: 30 10      BMI $B3A1           ; 
B391: A5 D2      LDA <$D2            ; 
B393: 38         SEC                 ; 
B394: E9 10      SBC #$10            ; 
B396: 90 09      BCC $B3A1           ; 
B398: 85 D2      STA <$D2            ; 
B39A: A2 03      LDX #$03            ; 
B39C: A0 60      LDY #$60            ; 
B39E: 20 8E BF   JSR $BF8E           ; 
B3A1: A2 02      LDX #$02            ; 
B3A3: 24 CC      BIT <$CC            ; 
B3A5: 70 0A      BVS $B3B1           ; 
B3A7: CA         DEX                 ; 
B3A8: 24 CB      BIT <$CB            ; 
B3AA: 70 05      BVS $B3B1           ; 
B3AC: CA         DEX                 ; 
B3AD: 24 CA      BIT <$CA            ; 
B3AF: 50 14      BVC $B3C5           ; 
B3B1: B5 CA      LDA $CA,X           ; 
B3B3: 29 0F      AND #$0F            ; 
B3B5: A8         TAY                 ; 
B3B6: B9 12 BD   LDA $BD12,Y         ; 
B3B9: 85 98      STA <$98            ; 
B3BB: BE 02 BD   LDX $BD02,Y         ; 
B3BE: A5 81      LDA <$81            ; 
B3C0: 6A         ROR A               ; 
B3C1: 6A         ROR A               ; 
B3C2: 6A         ROR A               ; 
B3C3: 90 02      BCC $B3C7           ; 
B3C5: A2 7F      LDX #$7F            ; 
B3C7: 86 9E      STX <$9E            ; 
B3C9: A5 CF      LDA <$CF            ; 
B3CB: 4C 33 B4   JMP $B433           ; 
B3CE: A5 80      LDA <$80            ; 
B3D0: C9 06      CMP #$06            ; 
B3D2: D0 16      BNE $B3EA           ; 
B3D4: A5 A1      LDA <$A1            ; 
B3D6: C9 86      CMP #$86            ; 
B3D8: D0 0C      BNE $B3E6           ; 
B3DA: A5 96      LDA <$96            ; 
B3DC: E5 95      SBC <$95            ; 
B3DE: C9 10      CMP #$10            ; 
B3E0: B0 04      BCS $B3E6           ; 
B3E2: A9 0C      LDA #$0C            ; 
B3E4: D0 4B      BNE $B431           ; 
B3E6: A9 0B      LDA #$0B            ; 
B3E8: D0 47      BNE $B431           ; 
B3EA: A5 96      LDA <$96            ; 
B3EC: 4A         LSR A               ; 
B3ED: 4A         LSR A               ; 
B3EE: 4A         LSR A               ; 
B3EF: 29 0C      AND #$0C            ; 
B3F1: 85 83      STA <$83            ; 
B3F3: A5 9C      LDA <$9C            ; 
B3F5: 4A         LSR A               ; 
B3F6: 4A         LSR A               ; 
B3F7: 4A         LSR A               ; 
B3F8: 4A         LSR A               ; 
B3F9: 05 83      ORA <$83            ; 
B3FB: 4A         LSR A               ; 
B3FC: A8         TAY                 ; 
B3FD: B1 CD      LDA ($CD),Y         ; 
B3FF: 90 04      BCC $B405           ; 
B401: 4A         LSR A               ; 
B402: 4A         LSR A               ; 
B403: 4A         LSR A               ; 
B404: 4A         LSR A               ; 
B405: 29 0F      AND #$0F            ; 
B407: C9 05      CMP #$05            ; 
B409: D0 06      BNE $B411           ; 
B40B: A6 80      LDX <$80            ; 
B40D: E0 04      CPX #$04            ; 
B40F: B0 1E      BCS $B42F           ; 
B411: C9 08      CMP #$08            ; 
B413: D0 06      BNE $B41B           ; 
B415: A2 04      LDX #$04            ; 
B417: E4 80      CPX <$80            ; 
B419: F0 14      BEQ $B42F           ; 
B41B: C9 0A      CMP #$0A            ; 
B41D: D0 06      BNE $B425           ; 
B41F: A2 04      LDX #$04            ; 
B421: E4 80      CPX <$80            ; 
B423: D0 0A      BNE $B42F           ; 
B425: C9 09      CMP #$09            ; 
B427: D0 08      BNE $B431           ; 
B429: A6 DB      LDX <$DB            ; 
B42B: E4 80      CPX <$80            ; 
B42D: F0 02      BEQ $B431           ; 
B42F: A9 00      LDA #$00            ; 
B431: 85 CF      STA <$CF            ; 
B433: 0A         ASL A               ; 
B434: 0A         ASL A               ; 
B435: 0A         ASL A               ; 
B436: 85 BE      STA <$BE            ; 
B438: AD 84 02   LDA $0284           ;{-2_INTIM} 
B43B: D0 FB      BNE $B438           ; 
B43D: A9 02      LDA #$02            ; 
B43F: 85 02      STA <$02            ;{-2_WSYNC} 
B441: 85 00      STA <$00            ;{-2_VSYNC} 
B443: E6 81      INC <$81            ; 
B445: D0 16      BNE $B45D           ; 
B447: 24 E3      BIT <$E3            ; 
B449: 30 12      BMI $B45D           ; 
B44B: A5 EA      LDA <$EA            ; 
B44D: C9 03      CMP #$03            ; 
B44F: B0 0C      BCS $B45D           ; 
B451: A5 A5      LDA <$A5            ; 
B453: 10 08      BPL $B45D           ; 
B455: 24 91      BIT <$91            ; 
B457: 70 04      BVS $B45D           ; 
B459: A9 0F      LDA #$0F            ; 
B45B: 85 A2      STA <$A2            ; 
B45D: 85 02      STA <$02            ;{-2_WSYNC} 
B45F: A9 3F      LDA #$3F            ; 
B461: 25 81      AND <$81            ; 
B463: D0 14      BNE $B479           ; 
B465: E6 82      INC <$82            ; 
B467: AD 82 02   LDA $0282           ;{-2_SWCHB} 
B46A: 29 02      AND #$02            ; 
B46C: D0 0B      BNE $B479           ; 
B46E: A6 EA      LDX <$EA            ; 
B470: E8         INX                 ; 
B471: E0 04      CPX #$04            ; 
B473: 90 02      BCC $B477           ; 
B475: A2 01      LDX #$01            ; 
B477: 86 EA      STX <$EA            ; 
B479: 85 02      STA <$02            ;{-2_WSYNC} 
B47B: A5 80      LDA <$80            ; 
B47D: C9 08      CMP #$08            ; 
B47F: D0 10      BNE $B491           ; 
B481: A9 18      LDA #$18            ; 
B483: 85 95      STA <$95            ; 
B485: A9 41      LDA #$41            ; 
B487: 85 96      STA <$96            ; 
B489: A9 3A      LDA #$3A            ; 
B48B: 85 97      STA <$97            ; 
B48D: A9 5F      LDA #$5F            ; 
B48F: 85 98      STA <$98            ; 
B491: A9 00      LDA #$00            ; 
B493: A2 2F      LDX #$2F            ; 
B495: 85 02      STA <$02            ;{-2_WSYNC} 
B497: 85 00      STA <$00            ;{-2_VSYNC} 
B499: 8E 96 02   STX $0296           ;{-2_TIM64T} 
B49C: 24 EB      BIT <$EB            ; 
B49E: 10 03      BPL $B4A3           ; 
B4A0: 4C 84 B7   JMP $B784           ; 
B4A3: A5 80      LDA <$80            ; 
B4A5: C9 08      CMP #$08            ; 
B4A7: F0 09      BEQ $B4B2           ; 
B4A9: 24 E3      BIT <$E3            ; 
B4AB: 10 2F      BPL $B4DC           ; 
B4AD: A6 A1      LDX <$A1            ; 
B4AF: CA         DEX                 ; 
B4B0: D0 2A      BNE $B4DC           ; 
B4B2: A9 07      LDA #$07            ; 
B4B4: 85 1A      STA <$1A            ;{-2_AUDV1} 
B4B6: A9 0C      LDA #$0C            ; 
B4B8: 85 16      STA <$16            ;{-2_AUDC1} 
B4BA: A6 EE      LDX <$EE            ; 
B4BC: CA         DEX                 ; 
B4BD: 10 0D      BPL $B4CC           ; 
B4BF: A2 0B      LDX #$0B            ; 
B4C1: A4 EF      LDY <$EF            ; 
B4C3: C8         INY                 ; 
B4C4: C0 37      CPY #$37            ; 
B4C6: 90 02      BCC $B4CA           ; 
B4C8: A0 00      LDY #$00            ; 
B4CA: 84 EF      STY <$EF            ; 
B4CC: 86 EE      STX <$EE            ; 
B4CE: A4 EF      LDY <$EF            ; 
B4D0: B9 C4 BE   LDA $BEC4,Y         ; 
B4D3: 85 18      STA <$18            ;{-2_AUDF1} 
B4D5: A9 00      LDA #$00            ; 
B4D7: 85 19      STA <$19            ;{-2_AUDV0} 
B4D9: 4C 48 B5   JMP $B548           ; 
B4DC: 24 D9      BIT <$D9            ; 
B4DE: 10 0E      BPL $B4EE           ; 
B4E0: A9 05      LDA #$05            ; 
B4E2: 85 16      STA <$16            ;{-2_AUDC1} 
B4E4: 0A         ASL A               ; 
B4E5: 85 1A      STA <$1A            ;{-2_AUDV1} 
B4E7: A5 9C      LDA <$9C            ; 
B4E9: 4A         LSR A               ; 
B4EA: 85 18      STA <$18            ;{-2_AUDF1} 
B4EC: D0 5A      BNE $B548           ; 
B4EE: 50 0E      BVC $B4FE           ; 
B4F0: A5 D4      LDA <$D4            ; 
B4F2: 29 0F      AND #$0F            ; 
B4F4: D0 4A      BNE $B540           ; 
B4F6: A9 04      LDA #$04            ; 
B4F8: 85 1A      STA <$1A            ;{-2_AUDV1} 
B4FA: A9 1C      LDA #$1C            ; 
B4FC: D0 46      BNE $B544           ; 
B4FE: A5 94      LDA <$94            ; 
B500: 10 0A      BPL $B50C           ; 
B502: 38         SEC                 ; 
B503: 2A         ROL A               ; 
B504: 38         SEC                 ; 
B505: 2A         ROL A               ; 
B506: 85 1A      STA <$1A            ;{-2_AUDV1} 
B508: A9 0E      LDA #$0E            ; 
B50A: D0 38      BNE $B544           ; 
B50C: AD 80 02   LDA $0280           ;{-2_SWCHA} 
B50F: C9 F0      CMP #$F0            ; 
B511: B0 2D      BCS $B540           ; 
B513: 24 91      BIT <$91            ; 
B515: 10 12      BPL $B529           ; 
B517: A5 81      LDA <$81            ; 
B519: 4A         LSR A               ; 
B51A: 4A         LSR A               ; 
B51B: 29 07      AND #$07            ; 
B51D: 85 18      STA <$18            ;{-2_AUDF1} 
B51F: A9 05      LDA #$05            ; 
B521: 85 16      STA <$16            ;{-2_AUDC1} 
B523: A9 07      LDA #$07            ; 
B525: 85 1A      STA <$1A            ;{-2_AUDV1} 
B527: D0 1F      BNE $B548           ; 
B529: A5 81      LDA <$81            ; 
B52B: 29 07      AND #$07            ; 
B52D: D0 11      BNE $B540           ; 
B52F: A5 81      LDA <$81            ; 
B531: 4A         LSR A               ; 
B532: 4A         LSR A               ; 
B533: 4A         LSR A               ; 
B534: 29 03      AND #$03            ; 
B536: F0 08      BEQ $B540           ; 
B538: A2 07      LDX #$07            ; 
B53A: 86 1A      STX <$1A            ;{-2_AUDV1} 
B53C: 69 16      ADC #$16            ; 
B53E: D0 04      BNE $B544           ; 
B540: A9 00      LDA #$00            ; 
B542: 85 1A      STA <$1A            ;{-2_AUDV1} 
B544: 85 16      STA <$16            ;{-2_AUDC1} 
B546: 85 18      STA <$18            ;{-2_AUDF1} 
B548: A5 80      LDA <$80            ; 
B54A: C9 07      CMP #$07            ; 
B54C: D0 03      BNE $B551           ; 
B54E: 4C 69 BA   JMP $BA69           ; 
B551: C9 08      CMP #$08            ; 
B553: D0 03      BNE $B558           ; 
B555: 4C C7 BA   JMP $BAC7           ; 
B558: A5 D0      LDA <$D0            ; 
B55A: 10 06      BPL $B562           ; 
B55C: A9 00      LDA #$00            ; 
B55E: 85 C0      STA <$C0            ; 
B560: F0 7F      BEQ $B5E1           ; 
B562: A5 81      LDA <$81            ; 
B564: 29 1F      AND #$1F            ; 
B566: D0 69      BNE $B5D1           ; 
B568: C6 D0      DEC <$D0            ; 
B56A: 10 53      BPL $B5BF           ; 
B56C: A9 00      LDA #$00            ; 
B56E: 85 C0      STA <$C0            ; 
B570: A5 CF      LDA <$CF            ; 
B572: C9 0A      CMP #$0A            ; 
B574: D0 43      BNE $B5B9           ; 
B576: A5 A1      LDA <$A1            ; 
B578: 30 09      BMI $B583           ; 
B57A: 2C 82 02   BIT $0282           ; 
B57D: 70 3A      BVS $B5B9           ; 
B57F: C9 01      CMP #$01            ; 
B581: D0 36      BNE $B5B9           ; 
B583: A9 8D      LDA #$8D            ; 
B585: 85 8A      STA <$8A            ; 
B587: A5 D2      LDA <$D2            ; 
B589: 4A         LSR A               ; 
B58A: 4A         LSR A               ; 
B58B: 4A         LSR A               ; 
B58C: 4A         LSR A               ; 
B58D: 18         CLC                 ; 
B58E: 65 DD      ADC <$DD            ; 
B590: 85 83      STA <$83            ; 
B592: 4A         LSR A               ; 
B593: 18         CLC                 ; 
B594: 65 83      ADC <$83            ; 
B596: C9 10      CMP #$10            ; 
B598: B0 02      BCS $B59C           ; 
B59A: A9 10      LDA #$10            ; 
B59C: 85 DC      STA <$DC            ; 
B59E: A2 07      LDX #$07            ; 
B5A0: 20 90 BE   JSR $BE90           ; 
B5A3: A9 F0      LDA #$F0            ; 
B5A5: 85 9B      STA <$9B            ; 
B5A7: A5 96      LDA <$96            ; 
B5A9: 38         SEC                 ; 
B5AA: E9 05      SBC #$05            ; 
B5AC: 10 02      BPL $B5B0           ; 
B5AE: A9 00      LDA #$00            ; 
B5B0: 85 95      STA <$95            ; 
B5B2: A9 C0      LDA #$C0            ; 
B5B4: 85 EB      STA <$EB            ; 
B5B6: 4C 84 B7   JMP $B784           ; 
B5B9: A9 9F      LDA #$9F            ; 
B5BB: 85 8A      STA <$8A            ; 
B5BD: D0 22      BNE $B5E1           ; 
B5BF: A5 D0      LDA <$D0            ; 
B5C1: A2 84      LDX #$84            ; 
B5C3: C9 07      CMP #$07            ; 
B5C5: 90 08      BCC $B5CF           ; 
B5C7: 29 07      AND #$07            ; 
B5C9: C9 07      CMP #$07            ; 
B5CB: D0 04      BNE $B5D1           ; 
B5CD: A2 8C      LDX #$8C            ; 
B5CF: 86 8A      STX <$8A            ; 
B5D1: A5 D0      LDA <$D0            ; 
B5D3: C9 08      CMP #$08            ; 
B5D5: B0 03      BCS $B5DA           ; 
B5D7: 0A         ASL A               ; 
B5D8: 0A         ASL A               ; 
B5D9: 0A         ASL A               ; 
B5DA: 29 38      AND #$38            ; 
B5DC: 18         CLC                 ; 
B5DD: 69 68      ADC #$68            ; 
B5DF: 85 C0      STA <$C0            ; 
B5E1: AD 80 02   LDA $0280           ;{-2_SWCHA} 
B5E4: 4A         LSR A               ; 
B5E5: 4A         LSR A               ; 
B5E6: 4A         LSR A               ; 
B5E7: 4A         LSR A               ; 
B5E8: 85 83      STA <$83            ; 
B5EA: A5 91      LDA <$91            ; 
B5EC: 29 F0      AND #$F0            ; 
B5EE: 05 83      ORA <$83            ; 
B5F0: 85 91      STA <$91            ; 
B5F2: 24 E3      BIT <$E3            ; 
B5F4: 30 38      BMI $B62E           ; 
B5F6: 24 3C      BIT <$3C            ; 
B5F8: 30 2A      BMI $B624           ; 
B5FA: A5 89      LDA <$89            ; 
B5FC: 30 30      BMI $B62E           ; 
B5FE: 09 80      ORA #$80            ; 
B600: 85 89      STA <$89            ; 
B602: AD 80 02   LDA $0280           ;{-2_SWCHA} 
B605: C9 F0      CMP #$F0            ; 
B607: B0 07      BCS $B610           ; 
B609: 26 91      ROL <$91            ; 
B60B: 38         SEC                 ; 
B60C: 66 91      ROR <$91            ; 
B60E: D0 1E      BNE $B62E           ; 
B610: 24 91      BIT <$91            ; 
B612: 70 1A      BVS $B62E           ; 
B614: 24 94      BIT <$94            ; 
B616: 30 16      BMI $B62E           ; 
B618: C6 9C      DEC <$9C            ; 
B61A: 10 02      BPL $B61E           ; 
B61C: E6 9C      INC <$9C            ; 
B61E: A9 80      LDA #$80            ; 
B620: 85 94      STA <$94            ; 
B622: D0 0A      BNE $B62E           ; 
B624: 26 89      ROL <$89            ; 
B626: 18         CLC                 ; 
B627: 66 89      ROR <$89            ; 
B629: 26 91      ROL <$91            ; 
B62B: 18         CLC                 ; 
B62C: 66 91      ROR <$91            ; 
B62E: 24 91      BIT <$91            ; 
B630: 50 22      BVC $B654           ; 
B632: A5 A7      LDA <$A7            ; 
B634: C5 80      CMP <$80            ; 
B636: F0 11      BEQ $B649           ; 
B638: 24 91      BIT <$91            ; 
B63A: 10 08      BPL $B644           ; 
B63C: A5 91      LDA <$91            ; 
B63E: 29 BF      AND #$BF            ; 
B640: 85 91      STA <$91            ; 
B642: D0 0D      BNE $B651           ; 
B644: 85 80      STA <$80            ; 
B646: 20 E3 BA   JSR $BAE3           ; 
B649: A5 9B      LDA <$9B            ; 
B64B: 85 9C      STA <$9C            ; 
B64D: A5 95      LDA <$95            ; 
B64F: 85 96      STA <$96            ; 
B651: 4C E3 B6   JMP $B6E3           ; 
B654: A5 D9      LDA <$D9            ; 
B656: D0 04      BNE $B65C           ; 
B658: 24 94      BIT <$94            ; 
B65A: 10 F5      BPL $B651           ; 
B65C: 29 20      AND #$20            ; 
B65E: F0 19      BEQ $B679           ; 
B660: A6 96      LDX <$96            ; 
B662: A5 91      LDA <$91            ; 
B664: 29 0F      AND #$0F            ; 
B666: 09 03      ORA #$03            ; 
B668: E0 20      CPX #$20            ; 
B66A: B0 02      BCS $B66E           ; 
B66C: 09 04      ORA #$04            ; 
B66E: E0 58      CPX #$58            ; 
B670: 90 02      BCC $B674           ; 
B672: 09 08      ORA #$08            ; 
B674: 85 91      STA <$91            ; 
B676: 4C E3 B6   JMP $B6E3           ; 
B679: 24 D9      BIT <$D9            ; 
B67B: 50 48      BVC $B6C5           ; 
B67D: A5 81      LDA <$81            ; 
B67F: 29 07      AND #$07            ; 
B681: D0 07      BNE $B68A           ; 
B683: A2 00      LDX #$00            ; 
B685: A0 01      LDY #$01            ; 
B687: 20 CF BF   JSR $BFCF           ; 
B68A: A5 80      LDA <$80            ; 
B68C: C9 04      CMP #$04            ; 
B68E: D0 07      BNE $B697           ; 
B690: A9 00      LDA #$00            ; 
B692: 85 D9      STA <$D9            ; 
B694: 4C 84 B7   JMP $B784           ; 
B697: C9 06      CMP #$06            ; 
B699: D0 48      BNE $B6E3           ; 
B69B: A5 9C      LDA <$9C            ; 
B69D: C9 2D      CMP #$2D            ; 
B69F: 90 06      BCC $B6A7           ; 
B6A1: A9 20      LDA #$20            ; 
B6A3: 85 D9      STA <$D9            ; 
B6A5: D0 13      BNE $B6BA           ; 
B6A7: C9 02      CMP #$02            ; 
B6A9: B0 12      BCS $B6BD           ; 
B6AB: A5 D7      LDA <$D7            ; 
B6AD: 85 9C      STA <$9C            ; 
B6AF: A5 D6      LDA <$D6            ; 
B6B1: 85 96      STA <$96            ; 
B6B3: A6 D8      LDX <$D8            ; 
B6B5: 86 80      STX <$80            ; 
B6B7: 20 E3 BA   JSR $BAE3           ; 
B6BA: 4C 84 B7   JMP $B784           ; 
B6BD: A5 91      LDA <$91            ; 
B6BF: 29 0F      AND #$0F            ; 
B6C1: 09 0C      ORA #$0C            ; 
B6C3: D0 AF      BNE $B674           ; 
B6C5: 10 F3      BPL $B6BA           ; 
B6C7: A6 9C      LDX <$9C            ; 
B6C9: E0 31      CPX #$31            ; 
B6CB: B0 04      BCS $B6D1           ; 
B6CD: E6 9C      INC <$9C            ; 
B6CF: D0 E9      BNE $B6BA           ; 
B6D1: A9 9F      LDA #$9F            ; 
B6D3: 85 8A      STA <$8A            ; 
B6D5: A2 02      LDX #$02            ; 
B6D7: A0 69      LDY #$69            ; 
B6D9: 20 CF BF   JSR $BFCF           ; 
B6DC: A9 20      LDA #$20            ; 
B6DE: 85 D9      STA <$D9            ; 
B6E0: 4C 84 B7   JMP $B784           ; 
B6E3: 24 E3      BIT <$E3            ; 
B6E5: 30 F9      BMI $B6E0           ; 
B6E7: A2 00      LDX #$00            ; 
B6E9: A5 91      LDA <$91            ; 
B6EB: 10 01      BPL $B6EE           ; 
B6ED: E8         INX                 ; 
B6EE: 29 0F      AND #$0F            ; 
B6F0: C9 0F      CMP #$0F            ; 
B6F2: F0 2C      BEQ $B720           ; 
B6F4: A5 92      LDA <$92            ; 
B6F6: 18         CLC                 ; 
B6F7: 7D 2C BE   ADC $BE2C,X         ; 
B6FA: 85 92      STA <$92            ; 
B6FC: 90 22      BCC $B720           ; 
B6FE: A5 91      LDA <$91            ; 
B700: A2 01      LDX #$01            ; 
B702: 20 CF BC   JSR $BCCF           ; 
B705: A2 00      LDX #$00            ; 
B707: A0 01      LDY #$01            ; 
B709: 20 CF BF   JSR $BFCF           ; 
B70C: A5 D9      LDA <$D9            ; 
B70E: D0 74      BNE $B784           ; 
B710: A5 91      LDA <$91            ; 
B712: 10 0C      BPL $B720           ; 
B714: A2 01      LDX #$01            ; 
B716: 20 CF BC   JSR $BCCF           ; 
B719: A2 00      LDX #$00            ; 
B71B: A0 01      LDY #$01            ; 
B71D: 20 CF BF   JSR $BFCF           ; 
B720: A6 80      LDX <$80            ; 
B722: A5 96      LDA <$96            ; 
B724: C9 78      CMP #$78            ; 
B726: 90 2A      BCC $B752           ; 
B728: 10 14      BPL $B73E           ; 
B72A: BD 4A BD   LDA $BD4A,X         ; 
B72D: F0 02      BEQ $B731           ; 
B72F: 85 96      STA <$96            ; 
B731: BD 62 BD   LDA $BD62,X         ; 
B734: F0 02      BEQ $B738           ; 
B736: 85 9C      STA <$9C            ; 
B738: BD 7A BD   LDA $BD7A,X         ; 
B73B: 4C 7F B7   JMP $B77F           ; 
B73E: BD 50 BD   LDA $BD50,X         ; 
B741: F0 02      BEQ $B745           ; 
B743: 85 96      STA <$96            ; 
B745: BD 68 BD   LDA $BD68,X         ; 
B748: F0 02      BEQ $B74C           ; 
B74A: 85 9C      STA <$9C            ; 
B74C: BD 80 BD   LDA $BD80,X         ; 
B74F: 4C 7F B7   JMP $B77F           ; 
B752: A5 9C      LDA <$9C            ; 
B754: C9 3B      CMP #$3B            ; 
B756: 90 2C      BCC $B784           ; 
B758: 10 14      BPL $B76E           ; 
B75A: BD 56 BD   LDA $BD56,X         ; 
B75D: F0 02      BEQ $B761           ; 
B75F: 85 96      STA <$96            ; 
B761: BD 6E BD   LDA $BD6E,X         ; 
B764: F0 02      BEQ $B768           ; 
B766: 85 9C      STA <$9C            ; 
B768: BD 86 BD   LDA $BD86,X         ; 
B76B: 4C 7F B7   JMP $B77F           ; 
B76E: BD 5C BD   LDA $BD5C,X         ; 
B771: F0 02      BEQ $B775           ; 
B773: 85 96      STA <$96            ; 
B775: BD 74 BD   LDA $BD74,X         ; 
B778: F0 02      BEQ $B77C           ; 
B77A: 85 9C      STA <$9C            ; 
B77C: BD 8C BD   LDA $BD8C,X         ; 
B77F: 85 80      STA <$80            ; 
B781: 20 E3 BA   JSR $BAE3           ; 
B784: 24 EB      BIT <$EB            ; 
B786: 30 03      BMI $B78B           ; 
B788: 4C 1D B8   JMP $B81D           ; 
B78B: A5 EB      LDA <$EB            ; 
B78D: 70 43      BVS $B7D2           ; 
B78F: 6A         ROR A               ; 
B790: B0 2E      BCS $B7C0           ; 
B792: A5 81      LDA <$81            ; 
B794: 29 03      AND #$03            ; 
B796: D0 11      BNE $B7A9           ; 
B798: E6 9B      INC <$9B            ; 
B79A: E6 9C      INC <$9C            ; 
B79C: A5 9B      LDA <$9B            ; 
B79E: 30 09      BMI $B7A9           ; 
B7A0: C9 20      CMP #$20            ; 
B7A2: 90 05      BCC $B7A9           ; 
B7A4: 66 EB      ROR <$EB            ; 
B7A6: 38         SEC                 ; 
B7A7: 26 EB      ROL <$EB            ; 
B7A9: 20 6C BE   JSR $BE6C           ; 
B7AC: A5 81      LDA <$81            ; 
B7AE: 29 07      AND #$07            ; 
B7B0: D0 0B      BNE $B7BD           ; 
B7B2: A6 B2      LDX <$B2            ; 
B7B4: E8         INX                 ; 
B7B5: E0 E6      CPX #$E6            ; 
B7B7: 90 02      BCC $B7BB           ; 
B7B9: A2 E0      LDX #$E0            ; 
B7BB: 86 B2      STX <$B2            ; 
B7BD: 4C C7 BA   JMP $BAC7           ; 
B7C0: C6 9B      DEC <$9B            ; 
B7C2: A5 9B      LDA <$9B            ; 
B7C4: 10 E3      BPL $B7A9           ; 
B7C6: C9 F0      CMP #$F0            ; 
B7C8: B0 DF      BCS $B7A9           ; 
B7CA: A9 00      LDA #$00            ; 
B7CC: 85 EB      STA <$EB            ; 
B7CE: 85 C0      STA <$C0            ; 
B7D0: F0 EB      BEQ $B7BD           ; 
B7D2: 6A         ROR A               ; 
B7D3: B0 25      BCS $B7FA           ; 
B7D5: A5 81      LDA <$81            ; 
B7D7: 29 03      AND #$03            ; 
B7D9: D0 CE      BNE $B7A9           ; 
B7DB: E6 9B      INC <$9B            ; 
B7DD: A9 40      LDA #$40            ; 
B7DF: 38         SEC                 ; 
B7E0: E5 9B      SBC <$9B            ; 
B7E2: C9 10      CMP #$10            ; 
B7E4: 90 02      BCC $B7E8           ; 
B7E6: A9 10      LDA #$10            ; 
B7E8: 85 8C      STA <$8C            ; 
B7EA: A5 9C      LDA <$9C            ; 
B7EC: 18         CLC                 ; 
B7ED: E9 03      SBC #$03            ; 
B7EF: C5 9B      CMP <$9B            ; 
B7F1: D0 B6      BNE $B7A9           ; 
B7F3: 66 EB      ROR <$EB            ; 
B7F5: 38         SEC                 ; 
B7F6: 26 EB      ROL <$EB            ; 
B7F8: D0 AF      BNE $B7A9           ; 
B7FA: C6 9C      DEC <$9C            ; 
B7FC: C6 9B      DEC <$9B            ; 
B7FE: A9 40      LDA #$40            ; 
B800: 38         SEC                 ; 
B801: E5 9B      SBC <$9B            ; 
B803: C9 10      CMP #$10            ; 
B805: 90 02      BCC $B809           ; 
B807: A9 10      LDA #$10            ; 
B809: 85 8C      STA <$8C            ; 
B80B: A5 9B      LDA <$9B            ; 
B80D: 10 9A      BPL $B7A9           ; 
B80F: C9 F0      CMP #$F0            ; 
B811: B0 96      BCS $B7A9           ; 
B813: A9 00      LDA #$00            ; 
B815: 85 EB      STA <$EB            ; 
B817: 20 AA BF   JSR $BFAA           ; 
B81A: 4C C7 BA   JMP $BAC7           ; 
B81D: A5 94      LDA <$94            ; 
B81F: 30 10      BMI $B831           ; 
B821: A9 5D      LDA #$5D            ; 
B823: 2C 82 02   BIT $0282           ; 
B826: 30 02      BMI $B82A           ; 
B828: A9 3B      LDA #$3B            ; 
B82A: 18         CLC                 ; 
B82B: 65 93      ADC <$93            ; 
B82D: 85 93      STA <$93            ; 
B82F: B0 03      BCS $B834           ; 
B831: 4C 06 BA   JMP $BA06           ; 
B834: A2 03      LDX #$03            ; 
B836: CA         DEX                 ; 
B837: 30 F8      BMI $B831           ; 
B839: B5 A5      LDA $A5,X           ; 
B83B: 30 F9      BMI $B836           ; 
B83D: C9 05      CMP #$05            ; 
B83F: D0 6B      BNE $B8AC           ; 
B841: B4 A2      LDY $A2,X           ; 
B843: 10 67      BPL $B8AC           ; 
B845: BD 95 BD   LDA $BD95,X         ; 
B848: 85 A0      STA <$A0            ; 
B84A: BC 92 BD   LDY $BD92,X         ; 
B84D: 84 9A      STY <$9A            ; 
B84F: D5 AB      CMP $AB,X           ; 
B851: D0 55      BNE $B8A8           ; 
B853: 98         TYA                 ; 
B854: D5 A8      CMP $A8,X           ; 
B856: D0 50      BNE $B8A8           ; 
B858: A9 FF      LDA #$FF            ; 
B85A: 95 A5      STA $A5,X           ; 
B85C: 8A         TXA                 ; 
B85D: D0 12      BNE $B871           ; 
B85F: A9 DF      LDA #$DF            ; 
B861: 25 CA      AND <$CA            ; 
B863: 85 CA      STA <$CA            ; 
B865: A9 DF      LDA #$DF            ; 
B867: 25 CB      AND <$CB            ; 
B869: 85 CB      STA <$CB            ; 
B86B: A9 DF      LDA #$DF            ; 
B86D: 25 CC      AND <$CC            ; 
B86F: 85 CC      STA <$CC            ; 
B871: E0 01      CPX #$01            ; 
B873: D0 1B      BNE $B890           ; 
B875: 24 91      BIT <$91            ; 
B877: 70 17      BVS $B890           ; 
B879: 24 E3      BIT <$E3            ; 
B87B: 30 13      BMI $B890           ; 
B87D: A9 10      LDA #$10            ; 
B87F: 24 CA      BIT <$CA            ; 
B881: D0 08      BNE $B88B           ; 
B883: 24 CB      BIT <$CB            ; 
B885: D0 04      BNE $B88B           ; 
B887: 24 CC      BIT <$CC            ; 
B889: F0 05      BEQ $B890           ; 
B88B: 26 A3      ROL <$A3            ; 
B88D: 18         CLC                 ; 
B88E: 66 A3      ROR <$A3            ; 
B890: E0 02      CPX #$02            ; 
B892: D0 06      BNE $B89A           ; 
B894: A5 91      LDA <$91            ; 
B896: 29 BF      AND #$BF            ; 
B898: 85 91      STA <$91            ; 
B89A: E4 A1      CPX <$A1            ; 
B89C: D0 98      BNE $B836           ; 
B89E: A9 FF      LDA #$FF            ; 
B8A0: 85 A1      STA <$A1            ; 
B8A2: A9 00      LDA #$00            ; 
B8A4: 85 8C      STA <$8C            ; 
B8A6: F0 8E      BEQ $B836           ; 
B8A8: A0 04      LDY #$04            ; 
B8AA: D0 13      BNE $B8BF           ; 
B8AC: C5 80      CMP <$80            ; 
B8AE: D0 15      BNE $B8C5           ; 
B8B0: B4 A2      LDY $A2,X           ; 
B8B2: 30 11      BMI $B8C5           ; 
B8B4: B5 AB      LDA $AB,X           ; 
B8B6: DD 98 BD   CMP $BD98,X         ; 
B8B9: 90 02      BCC $B8BD           ; 
B8BB: D6 AB      DEC $AB,X           ; 
B8BD: A0 00      LDY #$00            ; 
B8BF: 20 E4 BC   JSR $BCE4           ; 
B8C2: 4C 36 B8   JMP $B836           ; 
B8C5: B5 A2      LDA $A2,X           ; 
B8C7: 4A         LSR A               ; 
B8C8: 90 0F      BCC $B8D9           ; 
B8CA: 4A         LSR A               ; 
B8CB: 90 55      BCC $B922           ; 
B8CD: 4A         LSR A               ; 
B8CE: B0 03      BCS $B8D3           ; 
B8D0: 4C 70 B9   JMP $B970           ; 
B8D3: 4A         LSR A               ; 
B8D4: B0 EC      BCS $B8C2           ; 
B8D6: 4C B9 B9   JMP $B9B9           ; 
B8D9: D6 AB      DEC $AB,X           ; 
B8DB: 10 3B      BPL $B918           ; 
B8DD: B4 A5      LDY $A5,X           ; 
B8DF: B9 86 BD   LDA $BD86,Y         ; 
B8E2: 20 80 BF   JSR $BF80           ; 
B8E5: B0 34      BCS $B91B           ; 
B8E7: 95 A5      STA $A5,X           ; 
B8E9: E4 A1      CPX <$A1            ; 
B8EB: D0 08      BNE $B8F5           ; 
B8ED: A9 FF      LDA #$FF            ; 
B8EF: 85 A1      STA <$A1            ; 
B8F1: A9 00      LDA #$00            ; 
B8F3: 85 8C      STA <$8C            ; 
B8F5: B9 6E BD   LDA $BD6E,Y         ; 
B8F8: F0 0C      BEQ $B906           ; 
B8FA: DD 98 BD   CMP $BD98,X         ; 
B8FD: 90 05      BCC $B904           ; 
B8FF: BD 98 BD   LDA $BD98,X         ; 
B902: E9 01      SBC #$01            ; 
B904: 95 AB      STA $AB,X           ; 
B906: B9 56 BD   LDA $BD56,Y         ; 
B909: F0 02      BEQ $B90D           ; 
B90B: 95 A8      STA $A8,X           ; 
B90D: B5 A5      LDA $A5,X           ; 
B90F: C5 80      CMP <$80            ; 
B911: D0 05      BNE $B918           ; 
B913: 86 A1      STX <$A1            ; 
B915: 20 90 BE   JSR $BE90           ; 
B918: 4C 36 B8   JMP $B836           ; 
B91B: F6 AB      INC $AB,X           ; 
B91D: F6 AB      INC $AB,X           ; 
B91F: 4C 36 B8   JMP $B836           ; 
B922: F6 AB      INC $AB,X           ; 
B924: BD 98 BD   LDA $BD98,X         ; 
B927: D5 AB      CMP $AB,X           ; 
B929: B0 3B      BCS $B966           ; 
B92B: B4 A5      LDY $A5,X           ; 
B92D: B9 8C BD   LDA $BD8C,Y         ; 
B930: 20 80 BF   JSR $BF80           ; 
B933: B0 34      BCS $B969           ; 
B935: 95 A5      STA $A5,X           ; 
B937: E4 A1      CPX <$A1            ; 
B939: D0 08      BNE $B943           ; 
B93B: A9 FF      LDA #$FF            ; 
B93D: 85 A1      STA <$A1            ; 
B93F: A9 00      LDA #$00            ; 
B941: 85 8C      STA <$8C            ; 
B943: B9 74 BD   LDA $BD74,Y         ; 
B946: F0 0C      BEQ $B954           ; 
B948: DD 98 BD   CMP $BD98,X         ; 
B94B: 90 05      BCC $B952           ; 
B94D: BD 98 BD   LDA $BD98,X         ; 
B950: E9 01      SBC #$01            ; 
B952: 95 AB      STA $AB,X           ; 
B954: B9 5C BD   LDA $BD5C,Y         ; 
B957: F0 02      BEQ $B95B           ; 
B959: 95 A8      STA $A8,X           ; 
B95B: B5 A5      LDA $A5,X           ; 
B95D: C5 80      CMP <$80            ; 
B95F: D0 05      BNE $B966           ; 
B961: 86 A1      STX <$A1            ; 
B963: 20 90 BE   JSR $BE90           ; 
B966: 4C 36 B8   JMP $B836           ; 
B969: D6 AB      DEC $AB,X           ; 
B96B: D6 AB      DEC $AB,X           ; 
B96D: 4C 36 B8   JMP $B836           ; 
B970: D6 A8      DEC $A8,X           ; 
B972: 10 3B      BPL $B9AF           ; 
B974: B4 A5      LDY $A5,X           ; 
B976: B9 7A BD   LDA $BD7A,Y         ; 
B979: 20 80 BF   JSR $BF80           ; 
B97C: B0 34      BCS $B9B2           ; 
B97E: 95 A5      STA $A5,X           ; 
B980: E4 A1      CPX <$A1            ; 
B982: D0 08      BNE $B98C           ; 
B984: A9 FF      LDA #$FF            ; 
B986: 85 A1      STA <$A1            ; 
B988: A9 00      LDA #$00            ; 
B98A: 85 8C      STA <$8C            ; 
B98C: B9 62 BD   LDA $BD62,Y         ; 
B98F: F0 0C      BEQ $B99D           ; 
B991: DD 98 BD   CMP $BD98,X         ; 
B994: 90 05      BCC $B99B           ; 
B996: BD 98 BD   LDA $BD98,X         ; 
B999: E9 01      SBC #$01            ; 
B99B: 95 AB      STA $AB,X           ; 
B99D: B9 4A BD   LDA $BD4A,Y         ; 
B9A0: F0 02      BEQ $B9A4           ; 
B9A2: 95 A8      STA $A8,X           ; 
B9A4: B5 A5      LDA $A5,X           ; 
B9A6: C5 80      CMP <$80            ; 
B9A8: D0 05      BNE $B9AF           ; 
B9AA: 86 A1      STX <$A1            ; 
B9AC: 20 90 BE   JSR $BE90           ; 
B9AF: 4C 36 B8   JMP $B836           ; 
B9B2: F6 A8      INC $A8,X           ; 
B9B4: F6 A8      INC $A8,X           ; 
B9B6: 4C 36 B8   JMP $B836           ; 
B9B9: F6 A8      INC $A8,X           ; 
B9BB: B4 A8      LDY $A8,X           ; 
B9BD: C0 78      CPY #$78            ; 
B9BF: 90 3B      BCC $B9FC           ; 
B9C1: B4 A5      LDY $A5,X           ; 
B9C3: B9 80 BD   LDA $BD80,Y         ; 
B9C6: 20 80 BF   JSR $BF80           ; 
B9C9: B0 34      BCS $B9FF           ; 
B9CB: 95 A5      STA $A5,X           ; 
B9CD: E4 A1      CPX <$A1            ; 
B9CF: D0 08      BNE $B9D9           ; 
B9D1: A9 FF      LDA #$FF            ; 
B9D3: 85 A1      STA <$A1            ; 
B9D5: A9 00      LDA #$00            ; 
B9D7: 85 8C      STA <$8C            ; 
B9D9: B9 68 BD   LDA $BD68,Y         ; 
B9DC: F0 0C      BEQ $B9EA           ; 
B9DE: DD 98 BD   CMP $BD98,X         ; 
B9E1: 90 05      BCC $B9E8           ; 
B9E3: BD 98 BD   LDA $BD98,X         ; 
B9E6: E9 01      SBC #$01            ; 
B9E8: 95 AB      STA $AB,X           ; 
B9EA: B9 50 BD   LDA $BD50,Y         ; 
B9ED: F0 02      BEQ $B9F1           ; 
B9EF: 95 A8      STA $A8,X           ; 
B9F1: B5 A5      LDA $A5,X           ; 
B9F3: C5 80      CMP <$80            ; 
B9F5: D0 05      BNE $B9FC           ; 
B9F7: 86 A1      STX <$A1            ; 
B9F9: 20 90 BE   JSR $BE90           ; 
B9FC: 4C 36 B8   JMP $B836           ; 
B9FF: D6 A8      DEC $A8,X           ; 
BA01: D6 A8      DEC $A8,X           ; 
BA03: 4C 36 B8   JMP $B836           ; 
BA06: 24 E3      BIT <$E3            ; 
BA08: 10 0E      BPL $BA18           ; 
BA0A: A9 74      LDA #$74            ; 
BA0C: 85 B8      STA <$B8            ; 
BA0E: A9 6E      LDA #$6E            ; 
BA10: 85 B6      STA <$B6            ; 
BA12: A9 06      LDA #$06            ; 
BA14: 85 8D      STA <$8D            ; 
BA16: D0 4B      BNE $BA63           ; 
BA18: A5 94      LDA <$94            ; 
BA1A: 10 14      BPL $BA30           ; 
BA1C: 29 03      AND #$03            ; 
BA1E: AA         TAX                 ; 
BA1F: BD 68 BE   LDA $BE68,X         ; 
BA22: 85 8D      STA <$8D            ; 
BA24: BD 48 BE   LDA $BE48,X         ; 
BA27: 85 B6      STA <$B6            ; 
BA29: BD 4C BE   LDA $BE4C,X         ; 
BA2C: 85 B8      STA <$B8            ; 
BA2E: D0 33      BNE $BA63           ; 
BA30: A9 09      LDA #$09            ; 
BA32: 85 8D      STA <$8D            ; 
BA34: AD 80 02   LDA $0280           ;{-2_SWCHA} 
BA37: C9 F0      CMP #$F0            ; 
BA39: B0 20      BCS $BA5B           ; 
BA3B: A9 03      LDA #$03            ; 
BA3D: 24 91      BIT <$91            ; 
BA3F: 10 01      BPL $BA42           ; 
BA41: 4A         LSR A               ; 
BA42: 25 81      AND <$81            ; 
BA44: D0 1D      BNE $BA63           ; 
BA46: A6 EC      LDX <$EC            ; 
BA48: CA         DEX                 ; 
BA49: 10 02      BPL $BA4D           ; 
BA4B: A2 02      LDX #$02            ; 
BA4D: 86 EC      STX <$EC            ; 
BA4F: BD F6 BD   LDA $BDF6,X         ; 
BA52: 85 B6      STA <$B6            ; 
BA54: BD F9 BD   LDA $BDF9,X         ; 
BA57: 85 B8      STA <$B8            ; 
BA59: D0 08      BNE $BA63           ; 
BA5B: A9 00      LDA #$00            ; 
BA5D: 85 B6      STA <$B6            ; 
BA5F: A9 37      LDA #$37            ; 
BA61: 85 B8      STA <$B8            ; 
BA63: A9 F9      LDA #$F9            ; 
BA65: 85 B7      STA <$B7            ; 
BA67: 85 B9      STA <$B9            ; 
BA69: A5 A1      LDA <$A1            ; 
BA6B: C9 86      CMP #$86            ; 
BA6D: D0 2C      BNE $BA9B           ; 
BA6F: 24 F2      BIT <$F2            ; 
BA71: 10 12      BPL $BA85           ; 
BA73: A2 0A      LDX #$0A            ; 
BA75: 70 08      BVS $BA7F           ; 
BA77: CA         DEX                 ; 
BA78: A5 81      LDA <$81            ; 
BA7A: 29 02      AND #$02            ; 
BA7C: D0 01      BNE $BA7F           ; 
BA7E: CA         DEX                 ; 
BA7F: 20 90 BE   JSR $BE90           ; 
BA82: 4C C7 BA   JMP $BAC7           ; 
BA85: A5 E6      LDA <$E6            ; 
BA87: 4A         LSR A               ; 
BA88: 4A         LSR A               ; 
BA89: 4A         LSR A               ; 
BA8A: 4A         LSR A               ; 
BA8B: 29 03      AND #$03            ; 
BA8D: AA         TAX                 ; 
BA8E: BD 9B BD   LDA $BD9B,X         ; 
BA91: 85 AE      STA <$AE            ; 
BA93: BD 9F BD   LDA $BD9F,X         ; 
BA96: 85 B0      STA <$B0            ; 
BA98: 4C C7 BA   JMP $BAC7           ; 
BA9B: A6 A1      LDX <$A1            ; 
BA9D: 30 28      BMI $BAC7           ; 
BA9F: BD F3 BD   LDA $BDF3,X         ; 
BAA2: 25 81      AND <$81            ; 
BAA4: D0 21      BNE $BAC7           ; 
BAA6: A5 AE      LDA <$AE            ; 
BAA8: 18         CLC                 ; 
BAA9: 7D E8 BD   ADC $BDE8,X         ; 
BAAC: DD E5 BD   CMP $BDE5,X         ; 
BAAF: 90 0C      BCC $BABD           ; 
BAB1: BD AE BD   LDA $BDAE,X         ; 
BAB4: 85 AE      STA <$AE            ; 
BAB6: BD B9 BD   LDA $BDB9,X         ; 
BAB9: 85 B0      STA <$B0            ; 
BABB: D0 0A      BNE $BAC7           ; 
BABD: 85 AE      STA <$AE            ; 
BABF: A5 B0      LDA <$B0            ; 
BAC1: 18         CLC                 ; 
BAC2: 7D E8 BD   ADC $BDE8,X         ; 
BAC5: 85 B0      STA <$B0            ; 
BAC7: A5 80      LDA <$80            ; 
BAC9: C9 07      CMP #$07            ; 
BACB: F0 0C      BEQ $BAD9           ; 
BACD: A6 A1      LDX <$A1            ; 
BACF: 30 08      BMI $BAD9           ; 
BAD1: B5 AB      LDA $AB,X           ; 
BAD3: 85 9B      STA <$9B            ; 
BAD5: B5 A8      LDA $A8,X           ; 
BAD7: 85 95      STA <$95            ; 
BAD9: A5 96      LDA <$96            ; 
BADB: 48         PHA                 ; 
BADC: A9 1E      LDA #$1E            ; 
BADE: 85 96      STA <$96            ; 
BAE0: 4C 06 B0   JMP $B006           ; 
BAE3: A6 80      LDX <$80            ; 
BAE5: BD 32 BD   LDA $BD32,X         ; 
BAE8: 85 BB      STA <$BB            ; 
BAEA: 85 BD      STA <$BD            ; 
BAEC: BD 3A BD   LDA $BD3A,X         ; 
BAEF: 85 BA      STA <$BA            ; 
BAF1: BD 42 BD   LDA $BD42,X         ; 
BAF4: 85 BC      STA <$BC            ; 
BAF6: A9 00      LDA #$00            ; 
BAF8: 85 F2      STA <$F2            ; 
BAFA: 85 F1      STA <$F1            ; 
BAFC: A0 BF      LDY #$BF            ; 
BAFE: 98         TYA                 ; 
BAFF: 25 CA      AND <$CA            ; 
BB01: 85 CA      STA <$CA            ; 
BB03: 98         TYA                 ; 
BB04: 25 CB      AND <$CB            ; 
BB06: 85 CB      STA <$CB            ; 
BB08: 98         TYA                 ; 
BB09: 25 CC      AND <$CC            ; 
BB0B: 85 CC      STA <$CC            ; 
BB0D: A9 7F      LDA #$7F            ; 
BB0F: 85 9D      STA <$9D            ; 
BB11: 85 9E      STA <$9E            ; 
BB13: 85 9F      STA <$9F            ; 
BB15: 24 EB      BIT <$EB            ; 
BB17: 10 2C      BPL $BB45           ; 
BB19: A9 FF      LDA #$FF            ; 
BB1B: 85 A1      STA <$A1            ; 
BB1D: A9 3D      LDA #$3D            ; 
BB1F: 85 96      STA <$96            ; 
BB21: A9 F4      LDA #$F4            ; 
BB23: 85 9C      STA <$9C            ; 
BB25: A9 09      LDA #$09            ; 
BB27: 85 8D      STA <$8D            ; 
BB29: A9 00      LDA #$00            ; 
BB2B: 85 B6      STA <$B6            ; 
BB2D: A9 37      LDA #$37            ; 
BB2F: 85 B8      STA <$B8            ; 
BB31: A9 F9      LDA #$F9            ; 
BB33: 85 B7      STA <$B7            ; 
BB35: 85 B9      STA <$B9            ; 
BB37: A2 07      LDX #$07            ; 
BB39: 20 90 BE   JSR $BE90           ; 
BB3C: A9 38      LDA #$38            ; 
BB3E: 85 95      STA <$95            ; 
BB40: A9 F0      LDA #$F0            ; 
BB42: 85 9B      STA <$9B            ; 
BB44: 60         RTS                 ; 
BB45: E0 07      CPX #$07            ; 
BB47: D0 0D      BNE $BB56           ; 
BB49: 24 E3      BIT <$E3            ; 
BB4B: 10 08      BPL $BB55           ; 
BB4D: A9 33      LDA #$33            ; 
BB4F: 85 9D      STA <$9D            ; 
BB51: A9 40      LDA #$40            ; 
BB53: 85 97      STA <$97            ; 
BB55: 60         RTS                 ; 
BB56: E0 06      CPX #$06            ; 
BB58: F0 51      BEQ $BBAB           ; 
BB5A: 8A         TXA                 ; 
BB5B: A2 02      LDX #$02            ; 
BB5D: D5 A5      CMP $A5,X           ; 
BB5F: F0 0F      BEQ $BB70           ; 
BB61: CA         DEX                 ; 
BB62: 10 F9      BPL $BB5D           ; 
BB64: A9 FF      LDA #$FF            ; 
BB66: 85 A1      STA <$A1            ; 
BB68: A9 00      LDA #$00            ; 
BB6A: 85 8C      STA <$8C            ; 
BB6C: 85 9B      STA <$9B            ; 
BB6E: F0 05      BEQ $BB75           ; 
BB70: 86 A1      STX <$A1            ; 
BB72: 20 90 BE   JSR $BE90           ; 
BB75: A6 80      LDX <$80            ; 
BB77: E0 04      CPX #$04            ; 
BB79: B0 11      BCS $BB8C           ; 
BB7B: BD 54 BE   LDA $BE54,X         ; 
BB7E: 25 D1      AND <$D1            ; 
BB80: F0 0A      BEQ $BB8C           ; 
BB82: BD A3 BB   LDA $BBA3,X         ; 
BB85: 85 9F      STA <$9F            ; 
BB87: BD A7 BB   LDA $BBA7,X         ; 
BB8A: 85 99      STA <$99            ; 
BB8C: A5 80      LDA <$80            ; 
BB8E: C9 06      CMP #$06            ; 
BB90: B0 10      BCS $BBA2           ; 
BB92: 4A         LSR A               ; 
BB93: AA         TAX                 ; 
BB94: B5 E7      LDA $E7,X           ; 
BB96: B0 03      BCS $BB9B           ; 
BB98: 4A         LSR A               ; 
BB99: 10 03      BPL $BB9E           ; 
BB9B: 0A         ASL A               ; 
BB9C: 0A         ASL A               ; 
BB9D: 0A         ASL A               ; 
BB9E: 29 78      AND #$78            ; 
BBA0: 85 CD      STA <$CD            ; 
BBA2: 60         RTS                 ; 
BBA3: 20 20 20   JSR $2020           ; 
BBA6: 20 3C 3C   JSR $3C3C           ; 
BBA9: 26 26      ROL <$26            ; 
BBAB: A9 45      LDA #$45            ; 
BBAD: 85 96      STA <$96            ; 
BBAF: A9 03      LDA #$03            ; 
BBB1: 85 9C      STA <$9C            ; 
BBB3: A9 80      LDA #$80            ; 
BBB5: 85 D9      STA <$D9            ; 
BBB7: 24 E3      BIT <$E3            ; 
BBB9: 30 1F      BMI $BBDA           ; 
BBBB: A2 02      LDX #$02            ; 
BBBD: B5 CA      LDA $CA,X           ; 
BBBF: 29 F0      AND #$F0            ; 
BBC1: D0 08      BNE $BBCB           ; 
BBC3: B5 CA      LDA $CA,X           ; 
BBC5: 29 0F      AND #$0F            ; 
BBC7: C5 DA      CMP <$DA            ; 
BBC9: F0 17      BEQ $BBE2           ; 
BBCB: CA         DEX                 ; 
BBCC: 10 EF      BPL $BBBD           ; 
BBCE: A5 E6      LDA <$E6            ; 
BBD0: 29 0F      AND #$0F            ; 
BBD2: C5 DA      CMP <$DA            ; 
BBD4: D0 04      BNE $BBDA           ; 
BBD6: A9 86      LDA #$86            ; 
BBD8: D0 0B      BNE $BBE5           ; 
BBDA: A2 FF      LDX #$FF            ; 
BBDC: 86 A1      STX <$A1            ; 
BBDE: E8         INX                 ; 
BBDF: 86 8C      STX <$8C            ; 
BBE1: 60         RTS                 ; 
BBE2: 8A         TXA                 ; 
BBE3: 69 82      ADC #$82            ; 
BBE5: 85 A1      STA <$A1            ; 
BBE7: 29 0F      AND #$0F            ; 
BBE9: AA         TAX                 ; 
BBEA: 20 90 BE   JSR $BE90           ; 
BBED: A9 32      LDA #$32            ; 
BBEF: 85 9B      STA <$9B            ; 
BBF1: A9 29      LDA #$29            ; 
BBF3: 85 95      STA <$95            ; 
BBF5: 60         RTS                 ; 
BBF6: 00         BRK                 ; 
BBF7: 00         BRK                 ; 
BBF8: 00         BRK                 ; 
BBF9: 00         BRK                 ; 
BBFA: 00         BRK                 ; 
BBFB: 00         BRK                 ; 
BBFC: 00         BRK                 ; 
BBFD: 00         BRK                 ; 
BBFE: 00         BRK                 ; 
BBFF: 00         BRK                 ; 
BC00: F0 E0      BEQ $BBE2           ; 
BC02: D0 C0      BNE $BBC4           ; 
BC04: B0 A0      BCS $BBA6           ; 
BC06: 90 71      BCC $BC79           ; 
BC08: 61 51      ADC ($51,X)         ; 
BC0A: 41 31      EOR ($31,X)         ; 
BC0C: 21 11      AND ($11,X)         ; 
BC0E: 01 F1      ORA ($F1,X)         ; 
BC10: E1 D1      SBC ($D1,X)         ; 
BC12: C1 B1      CMP ($B1,X)         ; 
BC14: A1 91      LDA ($91,X)         ; 
BC16: 72 
BC17: 62 
BC18: 52 
BC19: 42 
BC1A: 32 
BC1B: 22 
BC1C: 12 
BC1D: 02 
BC1E: F2 
BC1F: E2 
BC20: D2 
BC21: C2 
BC22: B2 
BC23: A2 92      LDX #$92            ; 
BC25: 73 
BC26: 63 
BC27: 53 
BC28: 43 
BC29: 33 
BC2A: 23 
BC2B: 13 
BC2C: 03 
BC2D: F3 
BC2E: E3 
BC2F: D3 
BC30: C3 
BC31: B3 
BC32: A3 
BC33: 93 
BC34: 74 
BC35: 64 
BC36: 54 
BC37: 44 
BC38: 34 
BC39: 24 14      BIT <$14            ; 
BC3B: 04 
BC3C: F4 
BC3D: E4 D4      CPX <$D4            ; 
BC3F: C4 B4      CPY <$B4            ; 
BC41: A4 94      LDY <$94            ; 
BC43: 75 65      ADC <$65,X          ; 
BC45: 55 45      EOR $45,X           ; 
BC47: 35 25      AND $25,X           ; 
BC49: 15 05      ORA $05,X           ; 
BC4B: F5 E5      SBC $E5,X           ; 
BC4D: D5 C5      CMP $C5,X           ; 
BC4F: B5 A5      LDA $A5,X           ; 
BC51: 95 76      STA $76,X           ; 
BC53: 66 56      ROR <$56            ; 
BC55: 46 36      LSR <$36            ; 
BC57: 26 16      ROL <$16            ; 
BC59: 06 F6      ASL <$F6            ; 
BC5B: E6 D6      INC <$D6            ; 
BC5D: C6 B6      DEC <$B6            ; 
BC5F: A6 96      LDX <$96            ; 
BC61: 77 
BC62: 67 
BC63: 57 
BC64: 47 
BC65: 37 
BC66: 27 
BC67: 17 
BC68: 07 
BC69: F7 
BC6A: E7 
BC6B: D7 
BC6C: C7 
BC6D: B7 
BC6E: A7 
BC6F: 97 
BC70: 78         SEI                 ; 
BC71: 68         PLA                 ; 
BC72: 58         CLI                 ; 
BC73: 48         PHA                 ; 
BC74: 38         SEC                 ; 
BC75: 28         PLP                 ; 
BC76: 18         CLC                 ; 
BC77: 08         PHP                 ; 
BC78: F8         SED                 ; 
BC79: E8         INX                 ; 
BC7A: D8         CLD                 ; 
BC7B: C8         INY                 ; 
BC7C: B8         CLV                 ; 
BC7D: A8         TAY                 ; 
BC7E: 98         TYA                 ; 
BC7F: 78         SEI                 ; 
BC80: D8         CLD                 ; 
BC81: A2 FF      LDX #$FF            ; 
BC83: 9A         TXS                 ; 
BC84: E8         INX                 ; 
BC85: 8A         TXA                 ; 
BC86: 95 00      STA $00,X           ; 
BC88: CA         DEX                 ; 
BC89: D0 FB      BNE $BC86           ; 
BC8B: A9 01      LDA #$01            ; 
BC8D: 85 0A      STA <$0A            ;{-2_CTRLPF} 
BC8F: 85 EA      STA <$EA            ; 
BC91: A9 BF      LDA #$BF            ; 
BC93: 85 CE      STA <$CE            ; 
BC95: A9 4A      LDA #$4A            ; 
BC97: 85 90      STA <$90            ; 
BC99: A9 9C      LDA #$9C            ; 
BC9B: 85 8E      STA <$8E            ; 
BC9D: A9 FA      LDA #$FA            ; 
BC9F: 85 8F      STA <$8F            ; 
BCA1: A9 08      LDA #$08            ; 
BCA3: 85 80      STA <$80            ; 
BCA5: 20 E3 BA   JSR $BAE3           ; 
BCA8: 4C 3D B4   JMP $B43D           ; 
BCAB: AD 84 02   LDA $0284           ;{-2_INTIM} 
BCAE: D0 FB      BNE $BCAB           ; 
BCB0: 85 02      STA <$02            ;{-2_WSYNC} WSYNC wait for end of scanline 38
BCB2: 85 02      STA <$02            ;{-2_WSYNC} WSYNC wait for end of scanline 39
; Scanline 40 begins here
```

# Bank Switch (to bank 1)

```code
; Asteroids uses a different scheme to switch banks. It uses overlapping code in 
; both banks so that when a switch happens the code continues on to the next 
; instruction, but in a different bank.

; ET writes the six byte switch-then-jump code to RAM and executes it there.

; There are only two switch-points in the code. Bank 1 is called upon to handle 
; the visible part of the screen. Bank 0 handles the invisible part of the screen.

; - BCCC (bank 0) to F548 (bank 1) ... when the screen is being drawn
; - F4EC (bank 1) to B02D (bank 0) ... when the screen is not being drawn

; 0083: AD F9 FF   LDA $FFF9  ; Bank switch to bank 1
; 0086: 4C 48 F5   JMP $F548  ; Start of visible part of screen

BCB4: A9 48      LDA #$48            ; Destination ...
BCB6: 85 87      STA <$87            ; ...
BCB8: A9 F5      LDA #$F5            ; ...
BCBA: 85 88      STA <$88            ; ... F548
;
BCBC: A9 AD      LDA #$AD            ; Opcode ...
BCBE: 85 83      STA <$83            ; ... 
BCC0: A9 F9      LDA #$F9            ; ...
BCC2: 85 84      STA <$84            ; ... 
BCC4: A9 FF      LDA #$FF            ; ...
BCC6: 85 85      STA <$85            ; ... LDA $FFF9
;
BCC8: A9 4C      LDA #$4C            ; Opcode ...
BCCA: 85 86      STA <$86            ; ... JMP (for the destination F548 earlier)
BCCC: 4C 83 00   JMP $0083           ; Jump to RAM to make the switch

BCCF: 6A         ROR A               ; 
BCD0: B0 02      BCS $BCD4           ; 
BCD2: D6 9B      DEC $9B,X           ; 
BCD4: 6A         ROR A               ; 
BCD5: B0 02      BCS $BCD9           ; 
BCD7: F6 9B      INC $9B,X           ; 
BCD9: 6A         ROR A               ; 
BCDA: B0 02      BCS $BCDE           ; 
BCDC: D6 95      DEC $95,X           ; 
BCDE: 6A         ROR A               ; 
BCDF: B0 02      BCS $BCE3           ; 
BCE1: F6 95      INC $95,X           ; 
BCE3: 60         RTS                 ; 
BCE4: B5 AB      LDA $AB,X           ; 
BCE6: D9 9C 00   CMP $009C,Y         ; 
BCE9: F0 08      BEQ $BCF3           ; 
BCEB: B0 04      BCS $BCF1           ; 
BCED: F6 AB      INC $AB,X           ; 
BCEF: D0 02      BNE $BCF3           ; 
BCF1: D6 AB      DEC $AB,X           ; 
BCF3: B5 A8      LDA $A8,X           ; 
BCF5: D9 96 00   CMP $0096,Y         ; 
BCF8: F0 04      BEQ $BCFE           ; 
BCFA: B0 03      BCS $BCFF           ; 
BCFC: F6 A8      INC $A8,X           ; 
BCFE: 60         RTS                 ; 
BCFF: D6 A8      DEC $A8,X           ; 
BD01: 60         RTS                 ; 
BD02: 13 
BD03: 20 20 2C   JSR $2C20           ; 
BD06: 0B 
BD07: 20 20 34   JSR $3420           ; 
BD0A: 15 15      ORA $15,X           ; 
BD0C: 2D 2D 0F   AND $0F2D           ; 
BD0F: 0F 
BD10: 2F 
BD11: 2F 
BD12: 3E 19 65   ROL $6519,X         ; 
BD15: 3E 3E 1E   ROL $1E3E,X         ; 
BD18: 5F 
BD19: 3E 19 64   ROL $6419,X         ; 
BD1C: 1C 
BD1D: 60         RTS                 ; 
BD1E: 1E 5F 1E   ASL $1E5F,X         ; 
BD21: 5F 
BD22: 00         BRK                 ; 
BD23: 00         BRK                 ; 
BD24: 00         BRK                 ; 
BD25: 00         BRK                 ; 
BD26: 00         BRK                 ; 
BD27: 0A         ASL A               ; 
BD28: 09 0B      ORA #$0B            ; 
BD2A: 00         BRK                 ; 
BD2B: 06 05      ASL <$05            ; 
BD2D: 07 
BD2E: 00         BRK                 ; 
BD2F: 0E 0D 0F   ASL $0F0D           ; 
BD32: F8         SED                 ; 
BD33: FB 
BD34: FB 
BD35: FB 
BD36: F8         SED                 ; 
BD37: FD FD FF   SBC $FFFD,X         ; 
BD3A: 00         BRK                 ; 
BD3B: 38         SEC                 ; 
BD3C: 70 00      BVS $BD3E           ; 
BD3E: 73 
BD3F: 79 00 19   ADC $1900,Y         ; 
BD42: 33 
BD43: 38         SEC                 ; 
BD44: A0 00      LDY #$00            ; 
BD46: B3 
BD47: 40         RTI                 ; 
BD48: 99 00 77   STA $7700,Y         ; 
BD4B: 77 
BD4C: 77 
BD4D: 77 
BD4E: 44 
BD4F: 44 
BD50: 01 01      ORA ($01,X)         ; 
BD52: 01 01      ORA ($01,X)         ; 
BD54: 3A 
BD55: 3A 
BD56: 00         BRK                 ; 
BD57: 75 00      ADC <$00,X          ; 
BD59: 04 
BD5A: 00         BRK                 ; 
BD5B: 00         BRK                 ; 
BD5C: 00         BRK                 ; 
BD5D: 04 
BD5E: 00         BRK                 ; 
BD5F: 75 00      ADC <$00,X          ; 
BD61: 00         BRK                 ; 
BD62: 00         BRK                 ; 
BD63: 00         BRK                 ; 
BD64: 00         BRK                 ; 
BD65: 00         BRK                 ; 
BD66: 04 
BD67: 35 00      AND $00,X           ; 
BD69: 00         BRK                 ; 
BD6A: 00         BRK                 ; 
BD6B: 00         BRK                 ; 
BD6C: 04 
BD6D: 35 08      AND $08,X           ; 
BD6F: 24 39      BIT <$39            ; 
BD71: 24 08      BIT <$08            ; 
BD73: 39 02 1C   AND $1C02,Y         ; 
BD76: 32 
BD77: 1C 
BD78: 02 
BD79: 32 
BD7A: 01 02      ORA ($02,X)         ; 
BD7C: 03 
BD7D: 00         BRK                 ; 
BD7E: 03 
BD7F: 01 03      ORA ($03,X)         ; 
BD81: 00         BRK                 ; 
BD82: 01 02      ORA ($02,X)         ; 
BD84: 01 03      ORA ($03,X)         ; 
BD86: 04 
BD87: 04 
BD88: 04 
BD89: 04 
BD8A: 00         BRK                 ; 
BD8B: 00         BRK                 ; 
BD8C: 05 05      ORA <$05            ; 
BD8E: 05 05      ORA <$05            ; 
BD90: 02 
BD91: 02 
BD92: 1C 
BD93: 3C 
BD94: 5E 0F 2F   LSR $2F0F,X         ; 
BD97: 0F 
BD98: 30 34      BMI $BDCE           ; 
BD9A: 30 BE      BMI $BD5A           ; 
BD9C: C5 CC      CMP <$CC            ; 
BD9E: D3 
BD9F: DA 
BDA0: E1 E8      SBC ($E8,X)         ; 
BDA2: EF 
BDA3: FF 
BDA4: FA 
BDA5: FE FE FE   INC $FEFE,X         ; 
BDA8: FE F9 FE   INC $FEF9,X         ; 
BDAB: FB 
BDAC: FB 
BDAD: FF 
BDAE: 5A 
BDAF: 68         PLA                 ; 
BDB0: 00         BRK                 ; 
BDB1: A8         TAY                 ; 
BDB2: B2 
BDB3: BC BE D0   LDY $D0BE,X         ; 
BDB6: EC F4 E9   CPX $E9F4           ; 
BDB9: 92 
BDBA: B4 46      LDY $46,X           ; 
BDBC: AD B7 C1   LDA $C1B7           ; 
BDBF: DA 
BDC0: D0 EC      BNE $BDAE           ; 
BDC2: F4 
BDC3: E9 FF      SBC #$FF            ; 
BDC5: FA 
BDC6: FE FE FE   INC $FEFE,X         ; 
BDC9: FE F9 FE   INC $FEF9,X         ; 
BDCC: FD FD FD   SBC $FDFD,X         ; 
BDCF: CA         DEX                 ; 
BDD0: A9 8C      LDA #$8C            ; 
BDD2: C6 C6      DEC <$C6            ; 
BDD4: C6 F6      DEC <$F6            ; 
BDD6: E0 D1      CPX #$D1            ; 
BDD8: D1 30      CMP ($30),Y         ; 
BDDA: D8         CLD                 ; 
BDDB: F5 9A      SBC $9A,X           ; 
BDDD: CB 
BDDE: CB 
BDDF: CB 
BDE0: F6 E0      INC $E0,X           ; 
BDE2: D1 D1      CMP ($D1),Y         ; 
BDE4: 30 92      BMI $BD78           ; 
BDE6: A9 46      LDA #$46            ; 
BDE8: 0E 0B 0E   ASL $0E0B           ; 
BDEB: 05 05      ORA <$05            ; 
BDED: 05 07      ORA <$07            ; 
BDEF: 10 08      BPL $BDF9           ; 
BDF1: 08         PHP                 ; 
BDF2: 0A         ASL A               ; 
BDF3: 03 
BDF4: 03 
BDF5: 03 
BDF6: 00         BRK                 ; 
BDF7: 7A 
BDF8: 8C 37 83   STY $8337           ; 
BDFB: 95 FF      STA $FF,X           ; 
BDFD: 0B 
BDFE: 0E 07 0E   ASL $0E07           ; 
BE01: 0D F0 F0   ORA $F0F0           ; 
BE04: 07 
BE05: FF 
BE06: 0B 
BE07: 0E 0E 0D   ASL $0D0E           ; 
BE0A: F0 F0      BEQ $BDFC           ; 
BE0C: 0E 07 FF   ASL $FF07           ; 
BE0F: 0B 
BE10: 0E 0D F0   ASL $F00D           ; 
BE13: F0 0B      BEQ $BE20           ; 
BE15: 0D 07 FF   ORA $FF07           ; 
BE18: 0E 0D F0   ASL $F00D           ; 
BE1B: F0 0E      BEQ $BE2B           ; 
BE1D: 07 
BE1E: 0D 0B FF   ORA $FF0B           ; 
BE21: 0D F0 F0   ORA $F0F0           ; 
BE24: 0E 0B 0D   ASL $0D0B           ; 
BE27: 07 
BE28: 0E FF F0   ASL $F0FF           ; 
BE2B: F0 3F      BEQ $BE6C           ; 
BE2D: 81 A0      STA ($A0,X)         ; 
BE2F: B3 
BE30: 38         SEC                 ; 
BE31: B3 
BE32: 32 
BE33: B3 
BE34: 3E B3 44   ROL $44B3,X         ; 
BE37: B3 
BE38: 12 
BE39: B3 
BE3A: 90 B3      BCC $BDEF           ; 
BE3C: 85 B3      STA <$B3            ; 
BE3E: 4F 
BE3F: B3 
BE40: 56 B3      LSR $B3,X           ; 
BE42: A0 B3      LDY #$B3            ; 
BE44: 07 
BE45: B3 
BE46: FA 
BE47: B2 
BE48: 09 13      ORA #$13            ; 
BE4A: 1E 2A 40   ASL $402A,X         ; 
BE4D: 4A         LSR A               ; 
BE4E: 55 61      EOR $61,X           ; 
BE50: FE FD FB   INC $FBFD,X         ; 
BE53: F7 
BE54: 01 02      ORA ($02,X)         ; 
BE56: 04 
BE57: 08         PHP                 ; 
BE58: 04 
BE59: 03 
BE5A: 03 
BE5B: 02 
BE5C: 03 
BE5D: 02 
BE5E: 02 
BE5F: 01 03      ORA ($03,X)         ; 
BE61: 02 
BE62: 02 
BE63: 01 02      ORA ($02,X)         ; 
BE65: 01 01      ORA ($01,X)         ; 
BE67: 00         BRK                 ; 
BE68: 0A         ASL A               ; 
BE69: 0B 
BE6A: 0C 
BE6B: 0D A5 81   ORA $81A5           ; 
BE6E: 09 18      ORA #$18            ; 
BE70: 85 17      STA <$17            ;{-2_AUDF0} 
BE72: 29 07      AND #$07            ; 
BE74: 85 18      STA <$18            ;{-2_AUDF1} 
BE76: A5 81      LDA <$81            ; 
BE78: 4A         LSR A               ; 
BE79: 29 1F      AND #$1F            ; 
BE7B: C9 10      CMP #$10            ; 
BE7D: 90 02      BCC $BE81           ; 
BE7F: 49 0F      EOR #$0F            ; 
BE81: 85 19      STA <$19            ;{-2_AUDV0} 
BE83: 49 0F      EOR #$0F            ; 
BE85: 85 1A      STA <$1A            ;{-2_AUDV1} 
BE87: A9 0F      LDA #$0F            ; 
BE89: 85 15      STA <$15            ;{-2_AUDC0} 
BE8B: A9 0D      LDA #$0D            ; 
BE8D: 85 16      STA <$16            ;{-2_AUDC1} 
BE8F: 60         RTS                 ; 
BE90: BD E8 BD   LDA $BDE8,X         ; 
BE93: 85 8C      STA <$8C            ; 
BE95: BD AE BD   LDA $BDAE,X         ; 
BE98: 85 AE      STA <$AE            ; 
BE9A: BD B9 BD   LDA $BDB9,X         ; 
BE9D: 85 B0      STA <$B0            ; 
BE9F: BD A3 BD   LDA $BDA3,X         ; 
BEA2: 85 AF      STA <$AF            ; 
BEA4: 85 B1      STA <$B1            ; 
BEA6: BD CF BD   LDA $BDCF,X         ; 
BEA9: 85 B2      STA <$B2            ; 
BEAB: BD DA BD   LDA $BDDA,X         ; 
BEAE: 85 B4      STA <$B4            ; 
BEB0: BD C4 BD   LDA $BDC4,X         ; 
BEB3: 85 B3      STA <$B3            ; 
BEB5: 85 B5      STA <$B5            ; 
BEB7: 24 F2      BIT <$F2            ; 
BEB9: 30 08      BMI $BEC3           ; 
BEBB: B5 A8      LDA $A8,X           ; 
BEBD: 85 95      STA <$95            ; 
BEBF: B5 AB      LDA $AB,X           ; 
BEC1: 85 9B      STA <$9B            ; 
BEC3: 60         RTS                 ; 
BEC4: 17 
BEC5: 17 
BEC6: 17 
BEC7: 17 
BEC8: 0F 
BEC9: 0F 
BECA: 0F 
BECB: 0F 
BECC: 11 12      ORA ($12),Y         ; 
BECE: 14 
BECF: 12 
BED0: 17 
BED1: 17 
BED2: 17 
BED3: 17 
BED4: 1F 
BED5: 1F 
BED6: 1F 
BED7: 1F 
BED8: 1F 
BED9: 1F 
BEDA: 1F 
BEDB: 1F 
BEDC: 1B 
BEDD: 1B 
BEDE: 1B 
BEDF: 1B 
BEE0: 0D 0D 0D   ORA $0D0D           ; 
BEE3: 0D 0F 10   ORA $100F           ; 
BEE6: 12 
BEE7: 10 14      BPL $BEFD           ; 
BEE9: 14 
BEEA: 14 
BEEB: 14 
BEEC: 1B 
BEED: 1B 
BEEE: 1B 
BEEF: 1B 
BEF0: 18         CLC                 ; 
BEF1: 18         CLC                 ; 
BEF2: 18         CLC                 ; 
BEF3: 14 
BEF4: 12 
BEF5: 17 
BEF6: 1F 
BEF7: 1F 
BEF8: 1F 
BEF9: 1F 
BEFA: 1F 
BEFB: 00         BRK                 ; 
BEFC: 00         BRK                 ; 
BEFD: 00         BRK                 ; 
BEFE: 00         BRK                 ; 
BEFF: 00         BRK                 ; 
BF00: 37 
BF01: 39 22 4A   AND $4A22,Y         ; 
BF04: 54 
BF05: 81 00      STA ($00,X)         ; 
BF07: 61 A6      ADC ($A6,X)         ; 
BF09: 74 
BF0A: 10 03      BPL $BF0F           ; 
BF0C: 22 
BF0D: 48         PHA                 ; 
BF0E: 59 13 A0   EOR $A013,Y         ; 
BF11: 21 31      AND ($31,X)         ; 
BF13: 63 
BF14: 40         RTI                 ; 
BF15: 45 27      EOR <$27            ; 
BF17: 98         TYA                 ; 
BF18: 43 
BF19: 65 00      ADC <$00            ; 
BF1B: 2A         ROL A               ; 
BF1C: 71 48      ADC ($48),Y         ; 
BF1E: 93 
BF1F: 12 
BF20: 68         PLA                 ; 
BF21: 92 
BF22: 53 
BF23: 31 7A      AND ($7A),Y         ; 
BF25: 41 04      EOR ($04,X)         ; 
BF27: 20 31 A2   JSR $A231           ; 
BF2A: 31 06      AND ($06),Y         ; 
BF2C: 89 
BF2D: 07 
BF2E: 54 
BF2F: 42 
BF30: 64 
BF31: 81 52      STA ($52,X)         ; 
BF33: 21 03      AND ($03,X)         ; 
BF35: 4A         LSR A               ; 
BF36: 39 07 16   AND $1607,Y         ; 
BF39: 73 
BF3A: 03 
BF3B: A5 14      LDA <$14            ; 
BF3D: 04 
BF3E: 89 
BF3F: 22 
BF40: 2A         ROL A               ; 
BF41: 73 
BF42: 04 
BF43: 10 38      BPL $BF7D           ; 
BF45: 45 26      EOR <$26            ; 
BF47: 91 61      STA ($61),Y         ; 
BF49: 29 12      AND #$12            ; 
BF4B: 44 
BF4C: 7A 
BF4D: 03 
BF4E: 80 
BF4F: 53 
BF50: 96 40      STX $40,Y           ; 
BF52: 35 02      AND $02,X           ; 
BF54: 38         SEC                 ; 
BF55: 14 
BF56: 17 
BF57: A2 13      LDX #$13            ; 
BF59: A4 71      LDY <$71            ; 
BF5B: 23 
BF5C: 80 
BF5D: 60         RTS                 ; 
BF5E: 42 
BF5F: 59 42 14   EOR $1442,Y         ; 
BF62: 53 
BF63: 96 13      STX $13,Y           ; 
BF65: 20 A7 80   JSR $80A7           ; 
BF68: 23 
BF69: 84 32      STY <$32            ; 
BF6B: 54 
BF6C: 01 69      ORA ($69,X)         ; 
BF6E: 7A 
BF6F: 10 43      BPL $BFB4           ; 
BF71: 02 
BF72: 97 
BF73: 85 20      STA <$20            ;{-2_HMP0} 
BF75: 43 
BF76: 11 6A      ORA ($6A),Y         ; 
BF78: 24 83      BIT <$83            ; 
BF7A: 43 
BF7B: 01 6A      ORA ($6A,X)         ; 
BF7D: 29 15      AND #$15            ; 
BF7F: 07 
BF80: C5 A5      CMP <$A5            ; 
BF82: F0 09      BEQ $BF8D           ; 
BF84: C5 A6      CMP <$A6            ; 
BF86: F0 05      BEQ $BF8D           ; 
BF88: C5 A7      CMP <$A7            ; 
BF8A: F0 01      BEQ $BF8D           ; 
BF8C: 18         CLC                 ; 
BF8D: 60         RTS                 ; 
BF8E: F8         SED                 ; 
BF8F: 84 83      STY <$83            ; 
BF91: A5 D4      LDA <$D4            ; 
BF93: 18         CLC                 ; 
BF94: 65 83      ADC <$83            ; 
BF96: 85 D4      STA <$D4            ; 
BF98: 86 83      STX <$83            ; 
BF9A: A5 D3      LDA <$D3            ; 
BF9C: 65 83      ADC <$83            ; 
BF9E: 85 D3      STA <$D3            ; 
BFA0: 90 06      BCC $BFA8           ; 
BFA2: A9 99      LDA #$99            ; 
BFA4: 85 D3      STA <$D3            ; 
BFA6: 85 D4      STA <$D4            ; 
BFA8: D8         CLD                 ; 
BFA9: 60         RTS                 ; 
BFAA: A9 07      LDA #$07            ; 
BFAC: 85 80      STA <$80            ; 
BFAE: 85 81      STA <$81            ; 
BFB0: 20 E3 BA   JSR $BAE3           ; 
BFB3: A2 01      LDX #$01            ; 
BFB5: 86 A1      STX <$A1            ; 
BFB7: 20 90 BE   JSR $BE90           ; 
BFBA: A9 3C      LDA #$3C            ; 
BFBC: 85 95      STA <$95            ; 
BFBE: 85 96      STA <$96            ; 
BFC0: A9 0F      LDA #$0F            ; 
BFC2: 85 9B      STA <$9B            ; 
BFC4: A9 30      LDA #$30            ; 
BFC6: 85 9C      STA <$9C            ; 
BFC8: A9 00      LDA #$00            ; 
BFCA: 85 DE      STA <$DE            ; 
BFCC: 85 ED      STA <$ED            ; 
BFCE: 60         RTS                 ; 
BFCF: 84 86      STY <$86            ; 
BFD1: F8         SED                 ; 
BFD2: A5 D4      LDA <$D4            ; 
BFD4: 38         SEC                 ; 
BFD5: E5 86      SBC <$86            ; 
BFD7: 85 D4      STA <$D4            ; 
BFD9: 86 86      STX <$86            ; 
BFDB: A5 D3      LDA <$D3            ; 
BFDD: E5 86      SBC <$86            ; 
BFDF: 85 D3      STA <$D3            ; 
BFE1: B0 0B      BCS $BFEE           ; 
BFE3: A9 00      LDA #$00            ; 
BFE5: 85 D3      STA <$D3            ; 
BFE7: 85 D4      STA <$D4            ; 
BFE9: 26 E3      ROL <$E3            ; 
BFEB: 38         SEC                 ; 
BFEC: 66 E3      ROR <$E3            ; 
BFEE: D8         CLD                 ; 
BFEF: 60         RTS                 ; 
BFF0: 00         BRK                 ; 
BFF1: 00         BRK                 ; 
BFF2: 00         BRK                 ; 
BFF3: 00         BRK                 ; 
BFF4: 00         BRK                 ; 
BFF5: 00         BRK                 ; 
BFF6: 00         BRK                 ; 
BFF7: 00         BRK                 ; 
BFF8: 00         BRK                 ; 
BFF9: 00         BRK                 ; 
```

# Vectors (Bank 0)

```code
BFFA: 7F BC  ; NMI vector to BC7F
BFFC: 7F BC  ; Reset vector to BC7F (Only vector that is used in the Atari2600)
BFFE: 7F BC  ; IRQ/BRK vector to BC7F
```

# ROM Bank 1

```code
F000: AD F8 FF   LDA $FFF8           ; Switch to bank 0
F003: 4C 7F BC   JMP $BC7F           ; We are now in bank 0. This is a shadow of what's in bank 0 (easier to read but never executed)
;
F006: E0 40      CPX #$40            ; 
F008: 90 03      BCC $F00D           ; 
F00A: 4C 33 F1   JMP $F133           ; 
F00D: A9 00      LDA #$00            ; 
F00F: 85 1B      STA <$1B            ;{-2_GRP0} 
F011: 85 87      STA <$87            ; 
F013: A5 81      LDA <$81            ; 
F015: 4A         LSR A               ; 
F016: 29 1F      AND #$1F            ; 
F018: 09 40      ORA #$40            ; 
F01A: 85 06      STA <$06            ;{-2_COLUP0} 
F01C: A5 83      LDA <$83            ; 
F01E: EA         NOP                 ; 
F01F: 4C 4B F0   JMP $F04B           ; 
F022: E4 9F      CPX <$9F            ; 
F024: 08         PHP                 ; 
F025: E4 9E      CPX <$9E            ; 
F027: 08         PHP                 ; 
F028: E4 9D      CPX <$9D            ; 
F02A: 08         PHP                 ; 
F02B: E8         INX                 ; 
F02C: A4 86      LDY <$86            ; 
F02E: 8A         TXA                 ; 
F02F: 38         SEC                 ; 
F030: E5 9B      SBC <$9B            ; 
F032: C5 8C      CMP <$8C            ; 
F034: 84 1C      STY <$1C            ;{-2_GRP1} 
F036: 85 02      STA <$02            ;{-2_WSYNC} 
F038: B0 CC      BCS $F006           ; 
F03A: A8         TAY                 ; 
F03B: B1 AE      LDA ($AE),Y         ; 
F03D: 85 1B      STA <$1B            ;{-2_GRP0} 
F03F: B1 B2      LDA ($B2),Y         ; 
F041: 85 06      STA <$06            ;{-2_COLUP0} 
F043: B1 B0      LDA ($B0),Y         ; 
F045: 85 87      STA <$87            ; 
F047: B1 B4      LDA ($B4),Y         ; 
F049: 85 88      STA <$88            ; 
F04B: 8A         TXA                 ; 
F04C: A2 1F      LDX #$1F            ; 
F04E: 9A         TXS                 ; 
F04F: AA         TAX                 ; 
F050: 38         SEC                 ; 
F051: E5 9C      SBC <$9C            ; 
F053: C5 8D      CMP <$8D            ; 
F055: B0 20      BCS $F077           ; 
F057: A8         TAY                 ; 
F058: B1 B8      LDA ($B8),Y         ; 
F05A: 85 86      STA <$86            ; 
F05C: B1 B6      LDA ($B6),Y         ; 
F05E: 85 1C      STA <$1C            ;{-2_GRP1} 
F060: 85 02      STA <$02            ;{-2_WSYNC} 
F062: A5 87      LDA <$87            ; 
F064: 85 1B      STA <$1B            ;{-2_GRP0} 
F066: A5 88      LDA <$88            ; 
F068: 85 06      STA <$06            ;{-2_COLUP0} 
F06A: 8A         TXA                 ; 
F06B: A8         TAY                 ; 
F06C: B1 BA      LDA ($BA),Y         ; 
F06E: 85 0E      STA <$0E            ;{-2_PF1} 
F070: B1 BC      LDA ($BC),Y         ; 
F072: 85 0F      STA <$0F            ;{-2_PF2} 
F074: 4C 22 F0   JMP $F022           ; 
F077: A9 00      LDA #$00            ; 
F079: 85 1C      STA <$1C            ;{-2_GRP1} 
F07B: 85 86      STA <$86            ; 
F07D: F0 E1      BEQ $F060           ; 
F07F: 85 02      STA <$02            ;{-2_WSYNC} 
F081: E8         INX                 ; 
F082: E0 10      CPX #$10            ; 
F084: 90 F9      BCC $F07F           ; 
F086: A9 24      LDA #$24            ; 
F088: 85 06      STA <$06            ;{-2_COLUP0} 
F08A: 85 07      STA <$07            ;{-2_COLUP1} 
F08C: A9 17      LDA #$17            ; 
F08E: 85 04      STA <$04            ;{-2_NUSIZ0} 
F090: 85 05      STA <$05            ;{-2_NUSIZ1} 
F092: A9 00      LDA #$00            ; 
F094: 85 0B      STA <$0B            ;{-2_REFP0} 
F096: 85 0C      STA <$0C            ;{-2_PEFP1} 
F098: A2 0F      LDX #$0F            ; 
F09A: 85 02      STA <$02            ;{-2_WSYNC} 
F09C: BD 9E F9   LDA $F99E,X         ; 
F09F: 85 1B      STA <$1B            ;{-2_GRP0} 
F0A1: BD AE F9   LDA $F9AE,X         ; 
F0A4: 85 1C      STA <$1C            ;{-2_GRP1} 
F0A6: E0 02      CPX #$02            ; 
F0A8: B0 06      BCS $F0B0           ; 
F0AA: A9 0F      LDA #$0F            ; 
F0AC: 85 1D      STA <$1D            ;{-2_ENAM0} 
F0AE: 85 1E      STA <$1E            ;{-2_ENAM1} 
F0B0: 85 02      STA <$02            ;{-2_WSYNC} 
F0B2: CA         DEX                 ; 
F0B3: 85 02      STA <$02            ;{-2_WSYNC} 
F0B5: 10 E5      BPL $F09C           ; 
F0B7: A9 00      LDA #$00            ; 
F0B9: 85 1B      STA <$1B            ;{-2_GRP0} 
F0BB: 85 1C      STA <$1C            ;{-2_GRP1} 
F0BD: 85 1D      STA <$1D            ;{-2_ENAM0} 
F0BF: 85 1E      STA <$1E            ;{-2_ENAM1} 
F0C1: A2 2F      LDX #$2F            ; 
F0C3: 85 02      STA <$02            ;{-2_WSYNC} 
F0C5: E8         INX                 ; 
F0C6: E0 40      CPX #$40            ; 
F0C8: 90 F9      BCC $F0C3           ; 
F0CA: 85 02      STA <$02            ;{-2_WSYNC} 
F0CC: 85 2A      STA <$2A            ;{-2_HMOVE} 
F0CE: A9 03      LDA #$03            ; 
F0D0: A0 00      LDY #$00            ; 
F0D2: 84 0C      STY <$0C            ;{-2_PEFP1} 
F0D4: 85 04      STA <$04            ;{-2_NUSIZ0} 
F0D6: 85 05      STA <$05            ;{-2_NUSIZ1} 
F0D8: 85 25      STA <$25            ;{-2_VDELP0} 
F0DA: 85 26      STA <$26            ;{-2_VDELP1} 
F0DC: 84 1B      STY <$1B            ;{-2_GRP0} 
F0DE: 84 1C      STY <$1C            ;{-2_GRP1} 
F0E0: 84 1B      STY <$1B            ;{-2_GRP0} 
F0E2: 84 1C      STY <$1C            ;{-2_GRP1} 
F0E4: EA         NOP                 ; 
F0E5: 85 10      STA <$10            ;{-2_RESP0} 
F0E7: 85 11      STA <$11            ;{-2_RESP1} 
F0E9: 84 21      STY <$21            ;{-2_HMP1} 
F0EB: A9 F0      LDA #$F0            ; 
F0ED: 85 20      STA <$20            ;{-2_HMP0} 
F0EF: 84 0B      STY <$0B            ;{-2_REFP0} 
F0F1: 85 02      STA <$02            ;{-2_WSYNC} 
F0F3: 85 2A      STA <$2A            ;{-2_HMOVE} 
F0F5: A9 F7      LDA #$F7            ; 
F0F7: 85 BF      STA <$BF            ; 
F0F9: 85 C1      STA <$C1            ; 
F0FB: 85 C3      STA <$C3            ; 
F0FD: 85 C5      STA <$C5            ; 
F0FF: 85 C7      STA <$C7            ; 
F101: 85 C9      STA <$C9            ; 
F103: A9 21      LDA #$21            ; 
F105: 85 BE      STA <$BE            ; 
F107: A9 49      LDA #$49            ; 
F109: 85 C0      STA <$C0            ; 
F10B: A9 71      LDA #$71            ; 
F10D: 85 C2      STA <$C2            ; 
F10F: A9 99      LDA #$99            ; 
F111: 85 C4      STA <$C4            ; 
F113: A9 C1      LDA #$C1            ; 
F115: 85 C6      STA <$C6            ; 
F117: A9 00      LDA #$00            ; 
F119: 85 C8      STA <$C8            ; 
F11B: 85 02      STA <$02            ;{-2_WSYNC} 
F11D: A9 EA      LDA #$EA            ; 
F11F: 85 06      STA <$06            ;{-2_COLUP0} 
F121: 85 07      STA <$07            ;{-2_COLUP1} 
F123: A9 27      LDA #$27            ; 
F125: 85 83      STA <$83            ; 
F127: 20 09 F5   JSR $F509           ; 
F12A: A2 6E      LDX #$6E            ; 
F12C: 85 02      STA <$02            ;{-2_WSYNC} 
F12E: E8         INX                 ; 
F12F: E0 80      CPX #$80            ; 
F131: 90 F9      BCC $F12C           ; 
F133: 85 02      STA <$02            ;{-2_WSYNC} 
F135: A2 FF      LDX #$FF            ; 
F137: 9A         TXS                 ; 
F138: 86 0E      STX <$0E            ;{-2_PF1} 
F13A: 86 0F      STX <$0F            ;{-2_PF2} 
F13C: E8         INX                 ; 
F13D: 86 1B      STX <$1B            ;{-2_GRP0} 
F13F: 86 1C      STX <$1C            ;{-2_GRP1} 
F141: 86 1D      STX <$1D            ;{-2_ENAM0} 
F143: 86 1E      STX <$1E            ;{-2_ENAM1} 
F145: 86 1F      STX <$1F            ;{-2_ENABL} 
F147: 85 02      STA <$02            ;{-2_WSYNC} 
F149: A5 81      LDA <$81            ; 
F14B: 29 07      AND #$07            ; 
F14D: D0 12      BNE $F161           ; 
F14F: A5 E6      LDA <$E6            ; 
F151: 10 0E      BPL $F161           ; 
F153: 29 7F      AND #$7F            ; 
F155: C9 30      CMP #$30            ; 
F157: B0 08      BCS $F161           ; 
F159: 69 90      ADC #$90            ; 
F15B: 85 E6      STA <$E6            ; 
F15D: A9 83      LDA #$83            ; 
F15F: 85 8A      STA <$8A            ; 
F161: 85 02      STA <$02            ;{-2_WSYNC} 
F163: A9 C0      LDA #$C0            ; 
F165: 85 06      STA <$06            ;{-2_COLUP0} 
F167: 85 07      STA <$07            ;{-2_COLUP1} 
F169: A2 00      LDX #$00            ; 
F16B: 86 20      STX <$20            ;{-2_HMP0} 
F16D: 85 02      STA <$02            ;{-2_WSYNC} 
F16F: 86 0D      STX <$0D            ;{-2_PF0} 
F171: 86 09      STX <$09            ;{-2_COLUBK} 
F173: 86 0E      STX <$0E            ;{-2_PF1} 
F175: 86 0F      STX <$0F            ;{-2_PF2} 
F177: 85 02      STA <$02            ;{-2_WSYNC} 
F179: 85 2A      STA <$2A            ;{-2_HMOVE} 
F17B: A9 03      LDA #$03            ; 
F17D: A0 00      LDY #$00            ; 
F17F: 84 0C      STY <$0C            ;{-2_PEFP1} 
F181: 85 04      STA <$04            ;{-2_NUSIZ0} 
F183: 85 05      STA <$05            ;{-2_NUSIZ1} 
F185: 85 25      STA <$25            ;{-2_VDELP0} 
F187: 85 26      STA <$26            ;{-2_VDELP1} 
F189: 84 1B      STY <$1B            ;{-2_GRP0} 
F18B: 84 1C      STY <$1C            ;{-2_GRP1} 
F18D: 84 1B      STY <$1B            ;{-2_GRP0} 
F18F: 84 1C      STY <$1C            ;{-2_GRP1} 
F191: EA         NOP                 ; 
F192: 85 10      STA <$10            ;{-2_RESP0} 
F194: 85 11      STA <$11            ;{-2_RESP1} 
F196: 84 21      STY <$21            ;{-2_HMP1} 
F198: A9 F0      LDA #$F0            ; 
F19A: 85 20      STA <$20            ;{-2_HMP0} 
F19C: 84 0B      STY <$0B            ;{-2_REFP0} 
F19E: 85 02      STA <$02            ;{-2_WSYNC} 
F1A0: 85 2A      STA <$2A            ;{-2_HMOVE} 
F1A2: A5 D2      LDA <$D2            ; 
F1A4: 85 83      STA <$83            ; 
F1A6: A5 D3      LDA <$D3            ; 
F1A8: 85 84      STA <$84            ; 
F1AA: A5 D4      LDA <$D4            ; 
F1AC: 85 85      STA <$85            ; 
F1AE: A5 80      LDA <$80            ; 
F1B0: C9 08      CMP #$08            ; 
F1B2: D0 08      BNE $F1BC           ; 
F1B4: 24 E4      BIT <$E4            ; 
F1B6: 30 04      BMI $F1BC           ; 
F1B8: A9 FC      LDA #$FC            ; 
F1BA: D0 02      BNE $F1BE           ; 
F1BC: A9 FA      LDA #$FA            ; 
F1BE: 85 BF      STA <$BF            ; 
F1C0: 85 C1      STA <$C1            ; 
F1C2: 85 C3      STA <$C3            ; 
F1C4: 85 C5      STA <$C5            ; 
F1C6: 85 C7      STA <$C7            ; 
F1C8: 85 C9      STA <$C9            ; 
F1CA: 85 02      STA <$02            ;{-2_WSYNC} 
F1CC: A5 80      LDA <$80            ; 
F1CE: C9 07      CMP #$07            ; 
F1D0: 90 0C      BCC $F1DE           ; 
F1D2: A5 DF      LDA <$DF            ; 
F1D4: 85 83      STA <$83            ; 
F1D6: A5 E0      LDA <$E0            ; 
F1D8: 85 84      STA <$84            ; 
F1DA: A5 E1      LDA <$E1            ; 
F1DC: 85 85      STA <$85            ; 
F1DE: 85 02      STA <$02            ;{-2_WSYNC} 
F1E0: A9 9A      LDA #$9A            ; 
F1E2: 85 09      STA <$09            ;{-2_COLUBK} 
F1E4: A5 83      LDA <$83            ; 
F1E6: 29 F0      AND #$F0            ; 
F1E8: D0 02      BNE $F1EC           ; 
F1EA: A9 A0      LDA #$A0            ; 
F1EC: 4A         LSR A               ; 
F1ED: 85 BE      STA <$BE            ; 
F1EF: A5 83      LDA <$83            ; 
F1F1: 29 0F      AND #$0F            ; 
F1F3: 0A         ASL A               ; 
F1F4: 0A         ASL A               ; 
F1F5: 0A         ASL A               ; 
F1F6: 85 C0      STA <$C0            ; 
F1F8: 85 02      STA <$02            ;{-2_WSYNC} 
F1FA: A5 84      LDA <$84            ; 
F1FC: 29 F0      AND #$F0            ; 
F1FE: 4A         LSR A               ; 
F1FF: 85 C2      STA <$C2            ; 
F201: A5 84      LDA <$84            ; 
F203: 29 0F      AND #$0F            ; 
F205: 0A         ASL A               ; 
F206: 0A         ASL A               ; 
F207: 0A         ASL A               ; 
F208: 85 C4      STA <$C4            ; 
F20A: 85 02      STA <$02            ;{-2_WSYNC} 
F20C: A9 69      LDA #$69            ; 
F20E: C5 F1      CMP <$F1            ; 
F210: D0 04      BNE $F216           ; 
F212: A9 BC      LDA #$BC            ; 
F214: 85 85      STA <$85            ; 
F216: A5 85      LDA <$85            ; 
F218: 29 F0      AND #$F0            ; 
F21A: 4A         LSR A               ; 
F21B: 85 C6      STA <$C6            ; 
F21D: A5 85      LDA <$85            ; 
F21F: 29 0F      AND #$0F            ; 
F221: 0A         ASL A               ; 
F222: 0A         ASL A               ; 
F223: 0A         ASL A               ; 
F224: 85 C8      STA <$C8            ; 
F226: 85 02      STA <$02            ;{-2_WSYNC} 
F228: A0 50      LDY #$50            ; 
F22A: A6 80      LDX <$80            ; 
F22C: E0 07      CPX #$07            ; 
F22E: 90 0A      BCC $F23A           ; 
F230: C4 BE      CPY <$BE            ; 
F232: D0 18      BNE $F24C           ; 
F234: A5 C0      LDA <$C0            ; 
F236: D0 14      BNE $F24C           ; 
F238: 84 C0      STY <$C0            ; 
F23A: A5 C2      LDA <$C2            ; 
F23C: D0 0E      BNE $F24C           ; 
F23E: 84 C2      STY <$C2            ; 
F240: A5 C4      LDA <$C4            ; 
F242: D0 08      BNE $F24C           ; 
F244: 84 C4      STY <$C4            ; 
F246: A5 C6      LDA <$C6            ; 
F248: D0 02      BNE $F24C           ; 
F24A: 84 C6      STY <$C6            ; 
F24C: 85 02      STA <$02            ;{-2_WSYNC} 
F24E: A9 FC      LDA #$FC            ; 
F250: C5 BF      CMP <$BF            ; 
F252: D0 18      BNE $F26C           ; 
F254: A9 00      LDA #$00            ; 
F256: 85 BE      STA <$BE            ; 
F258: A9 B0      LDA #$B0            ; 
F25A: 85 C0      STA <$C0            ; 
F25C: A9 B8      LDA #$B8            ; 
F25E: 85 C2      STA <$C2            ; 
F260: A9 C0      LDA #$C0            ; 
F262: 85 C4      STA <$C4            ; 
F264: A9 C8      LDA #$C8            ; 
F266: 85 C6      STA <$C6            ; 
F268: A9 D0      LDA #$D0            ; 
F26A: 85 C8      STA <$C8            ; 
F26C: A9 07      LDA #$07            ; 
F26E: 85 83      STA <$83            ; 
F270: 20 09 F5   JSR $F509           ; 
F273: 85 02      STA <$02            ;{-2_WSYNC} 
F275: A9 02      LDA #$02            ; 
F277: 2D 82 02   AND $0282           ;{-2_SWCHB} 
F27A: D0 0A      BNE $F286           ; 
F27C: A9 88      LDA #$88            ; 
F27E: 85 E2      STA <$E2            ; 
F280: 85 E4      STA <$E4            ; 
F282: A9 00      LDA #$00            ; 
F284: 85 EB      STA <$EB            ; 
;
F286: 85 02      STA <$02            ;{-2_WSYNC} WSYNC end of scanline 216
F288: 85 02      STA <$02            ;{-2_WSYNC} WSYNC end of scanline 217
F28A: 85 02      STA <$02            ;{-2_WSYNC} WSYNC end of scanline 218
F28C: 85 02      STA <$02            ;{-2_WSYNC} WSYNC end of scanline 219
F28E: 85 02      STA <$02            ;{-2_WSYNC} WSYNC end of scanline 220
;
; Beginning of scanline 221
F290: A2 0F      LDX #$0F            ; 
F292: 86 01      STX <$01            ;{-2_VBLANK} 
F294: 20 08 F5   JSR $F508           ; 
F297: 20 08 F5   JSR $F508           ; 
F29A: A2 2D      LDX #$2D            ; 
F29C: 8E 96 02   STX $0296           ;{-2_TIM64T} 
F29F: 6E 82 02   ROR $0282           ;{-2_SWCHB} 
F2A2: B0 0D      BCS $F2B1           ; 
F2A4: A9 40      LDA #$40            ; 
F2A6: 24 89      BIT <$89            ; 
F2A8: 70 0D      BVS $F2B7           ; 
F2AA: 05 89      ORA <$89            ; 
F2AC: 85 89      STA <$89            ; 
F2AE: 4C F3 F3   JMP $F3F3           ; 
F2B1: A5 89      LDA <$89            ; 
F2B3: 29 BF      AND #$BF            ; 
F2B5: 85 89      STA <$89            ; 
F2B7: 20 B6 F6   JSR $F6B6           ; 
F2BA: 20 EB FD   JSR $FDEB           ; 
F2BD: 20 E0 FC   JSR $FCE0           ; 
F2C0: A5 8A      LDA <$8A            ; 
F2C2: 30 4D      BMI $F311           ; 
F2C4: A6 A1      LDX <$A1            ; 
F2C6: 30 0C      BMI $F2D4           ; 
F2C8: A5 80      LDA <$80            ; 
F2CA: C9 07      CMP #$07            ; 
F2CC: F0 43      BEQ $F311           ; 
F2CE: A5 81      LDA <$81            ; 
F2D0: 29 0F      AND #$0F            ; 
F2D2: F0 05      BEQ $F2D9           ; 
F2D4: A9 80      LDA #$80            ; 
F2D6: 4C 15 F3   JMP $F315           ; 
F2D9: A9 13      LDA #$13            ; 
F2DB: 85 15      STA <$15            ;{-2_AUDC0} 
F2DD: 24 81      BIT <$81            ; 
F2DF: D0 02      BNE $F2E3           ; 
F2E1: A9 16      LDA #$16            ; 
F2E3: 85 17      STA <$17            ;{-2_AUDF0} 
F2E5: A5 96      LDA <$96            ; 
F2E7: E5 95      SBC <$95            ; 
F2E9: 10 02      BPL $F2ED           ; 
F2EB: 49 FF      EOR #$FF            ; 
F2ED: 85 83      STA <$83            ; 
F2EF: A5 9C      LDA <$9C            ; 
F2F1: E5 9B      SBC <$9B            ; 
F2F3: 0A         ASL A               ; 
F2F4: 10 02      BPL $F2F8           ; 
F2F6: 49 FF      EOR #$FF            ; 
F2F8: C5 83      CMP <$83            ; 
F2FA: B0 03      BCS $F2FF           ; 
F2FC: 4A         LSR A               ; 
F2FD: 10 02      BPL $F301           ; 
F2FF: 46 83      LSR <$83            ; 
F301: 18         CLC                 ; 
F302: 65 83      ADC <$83            ; 
F304: 10 04      BPL $F30A           ; 
F306: A9 00      LDA #$00            ; 
F308: F0 05      BEQ $F30F           ; 
F30A: 4A         LSR A               ; 
F30B: 4A         LSR A               ; 
F30C: 4A         LSR A               ; 
F30D: 49 0F      EOR #$0F            ; 
F30F: 85 19      STA <$19            ;{-2_AUDV0} 
F311: A5 8A      LDA <$8A            ; 
F313: 10 0F      BPL $F324           ; 
F315: 85 15      STA <$15            ;{-2_AUDC0} 
F317: 85 19      STA <$19            ;{-2_AUDV0} 
F319: 85 17      STA <$17            ;{-2_AUDF0} 
F31B: 0A         ASL A               ; 
F31C: F0 06      BEQ $F324           ; 
F31E: A9 80      LDA #$80            ; 
F320: 85 8A      STA <$8A            ; 
F322: D0 02      BNE $F326           ; 
F324: 46 8A      LSR <$8A            ; 
F326: 24 EB      BIT <$EB            ; 
F328: 30 11      BMI $F33B           ; 
F32A: A5 80      LDA <$80            ; 
F32C: C9 07      CMP #$07            ; 
F32E: F0 25      BEQ $F355           ; 
F330: C9 08      CMP #$08            ; 
F332: D0 0A      BNE $F33E           ; 
F334: 24 3C      BIT <$3C            ; 
F336: 30 03      BMI $F33B           ; 
F338: 4C F3 F3   JMP $F3F3           ; 
F33B: 4C D4 F4   JMP $F4D4           ; 
F33E: 4C A5 F4   JMP $F4A5           ; 
F341: 00         BRK                 ; 
F342: 90 80      BCC $F2C4           ; 
F344: 70 60      BVS $F3A6           ; 
F346: 50 40      BVC $F388           ; 
F348: 30 20      BMI $F36A           ; 
F34A: 10 00      BPL $F34C           ; 
F34C: 04 
F34D: 09 14      ORA #$14            ; 
F34F: 19 24 29   ORA $2924,Y         ; 
F352: 34 
F353: 39 44 A9   AND $A944,Y         ; 
F356: 03 
F357: 25 81      AND <$81            ; 
F359: D0 19      BNE $F374           ; 
F35B: 24 ED      BIT <$ED            ; 
F35D: 10 04      BPL $F363           ; 
F35F: E6 95      INC <$95            ; 
F361: D0 02      BNE $F365           ; 
F363: C6 95      DEC <$95            ; 
F365: A5 95      LDA <$95            ; 
F367: 38         SEC                 ; 
F368: E9 1C      SBC #$1C            ; 
F36A: C9 40      CMP #$40            ; 
F36C: 90 06      BCC $F374           ; 
F36E: A9 80      LDA #$80            ; 
F370: 45 ED      EOR <$ED            ; 
F372: 85 ED      STA <$ED            ; 
F374: 24 DE      BIT <$DE            ; 
F376: 70 34      BVS $F3AC           ; 
F378: A5 81      LDA <$81            ; 
F37A: C9 60      CMP #$60            ; 
F37C: D0 07      BNE $F385           ; 
F37E: A4 D4      LDY <$D4            ; 
F380: A6 D3      LDX <$D3            ; 
F382: 4C A3 F3   JMP $F3A3           ; 
F385: C9 C0      CMP #$C0            ; 
F387: F0 0C      BEQ $F395           ; 
F389: C9 FF      CMP #$FF            ; 
F38B: D0 41      BNE $F3CE           ; 
F38D: A9 40      LDA #$40            ; 
F38F: 05 DE      ORA <$DE            ; 
F391: 85 DE      STA <$DE            ; 
F393: D0 39      BNE $F3CE           ; 
F395: A5 D2      LDA <$D2            ; 
F397: 4A         LSR A               ; 
F398: 4A         LSR A               ; 
F399: 4A         LSR A               ; 
F39A: 4A         LSR A               ; 
F39B: A8         TAY                 ; 
F39C: BE 4B F3   LDX $F34B,Y         ; 
F39F: B9 41 F3   LDA $F341,Y         ; 
F3A2: A8         TAY                 ; 
F3A3: 20 EF F4   JSR $F4EF           ; 
F3A6: A9 8C      LDA #$8C            ; 
F3A8: 85 8A      STA <$8A            ; 
F3AA: D0 22      BNE $F3CE           ; 
F3AC: A4 DD      LDY <$DD            ; 
F3AE: F0 32      BEQ $F3E2           ; 
F3B0: A5 81      LDA <$81            ; 
F3B2: 29 1F      AND #$1F            ; 
F3B4: D0 1B      BNE $F3D1           ; 
F3B6: 88         DEY                 ; 
F3B7: 84 DD      STY <$DD            ; 
F3B9: A9 8F      LDA #$8F            ; 
F3BB: 85 8A      STA <$8A            ; 
F3BD: A9 06      LDA #$06            ; 
F3BF: 85 8B      STA <$8B            ; 
F3C1: A9 01      LDA #$01            ; 
F3C3: 05 DE      ORA <$DE            ; 
F3C5: 85 DE      STA <$DE            ; 
F3C7: A2 07      LDX #$07            ; 
F3C9: A0 70      LDY #$70            ; 
F3CB: 20 EF F4   JSR $F4EF           ; 
F3CE: 4C A2 F4   JMP $F4A2           ; 
F3D1: C9 0F      CMP #$0F            ; 
F3D3: D0 F9      BNE $F3CE           ; 
F3D5: A9 88      LDA #$88            ; 
F3D7: 85 8A      STA <$8A            ; 
F3D9: A5 DE      LDA <$DE            ; 
F3DB: 29 FE      AND #$FE            ; 
F3DD: 85 DE      STA <$DE            ; 
F3DF: 4C A2 F4   JMP $F4A2           ; 
F3E2: 24 E4      BIT <$E4            ; 
F3E4: 10 07      BPL $F3ED           ; 
F3E6: A9 88      LDA #$88            ; 
F3E8: 85 E2      STA <$E2            ; 
F3EA: 4C D4 F4   JMP $F4D4           ; 
F3ED: 24 3C      BIT <$3C            ; 
F3EF: 30 DD      BMI $F3CE           ; 
F3F1: 10 22      BPL $F415           ; 
F3F3: A9 10      LDA #$10            ; 
F3F5: 85 DC      STA <$DC            ; 
F3F7: 85 E4      STA <$E4            ; 
F3F9: A9 02      LDA #$02            ; 
F3FB: 85 E5      STA <$E5            ; 
F3FD: A9 00      LDA #$00            ; 
F3FF: 85 E3      STA <$E3            ; 
F401: 85 DD      STA <$DD            ; 
F403: 85 EB      STA <$EB            ; 
F405: 85 D9      STA <$D9            ; 
F407: 85 94      STA <$94            ; 
F409: 85 91      STA <$91            ; 
F40B: 85 F0      STA <$F0            ; 
F40D: 85 DF      STA <$DF            ; 
F40F: 85 E0      STA <$E0            ; 
F411: A9 03      LDA #$03            ; 
F413: 85 E1      STA <$E1            ; 
F415: 26 89      ROL <$89            ; 
F417: 38         SEC                 ; 
F418: 66 89      ROR <$89            ; 
F41A: 26 F0      ROL <$F0            ; 
F41C: 18         CLC                 ; 
F41D: 66 F0      ROR <$F0            ; 
F41F: A9 84      LDA #$84            ; 
F421: 85 E2      STA <$E2            ; 
F423: 85 EB      STA <$EB            ; 
F425: A9 FF      LDA #$FF            ; 
F427: 85 A2      STA <$A2            ; 
F429: 85 A3      STA <$A3            ; 
F42B: 85 A4      STA <$A4            ; 
F42D: 85 A2      STA <$A2            ; 
F42F: 85 A3      STA <$A3            ; 
F431: 85 A4      STA <$A4            ; 
F433: 85 D0      STA <$D0            ; 
F435: A9 0A      LDA #$0A            ; 
F437: 85 D2      STA <$D2            ; 
F439: A5 81      LDA <$81            ; 
F43B: 45 82      EOR <$82            ; 
F43D: 29 07      AND #$07            ; 
F43F: C9 06      CMP #$06            ; 
F441: 90 02      BCC $F445           ; 
F443: E9 04      SBC #$04            ; 
F445: 85 DB      STA <$DB            ; 
F447: A5 82      LDA <$82            ; 
F449: 29 03      AND #$03            ; 
F44B: AA         TAX                 ; 
F44C: A5 81      LDA <$81            ; 
F44E: 29 0F      AND #$0F            ; 
F450: 85 E6      STA <$E6            ; 
F452: 7D F7 F8   ADC $F8F7,X         ; 
F455: 29 0F      AND #$0F            ; 
F457: 85 CB      STA <$CB            ; 
F459: 7D F7 F8   ADC $F8F7,X         ; 
F45C: 29 0F      AND #$0F            ; 
F45E: 85 CA      STA <$CA            ; 
F460: 7D F7 F8   ADC $F8F7,X         ; 
F463: 29 0F      AND #$0F            ; 
F465: 85 CC      STA <$CC            ; 
F467: A5 81      LDA <$81            ; 
F469: 29 03      AND #$03            ; 
F46B: AA         TAX                 ; 
F46C: A5 82      LDA <$82            ; 
F46E: 85 E7      STA <$E7            ; 
F470: 7D F7 F8   ADC $F8F7,X         ; 
F473: 85 E8      STA <$E8            ; 
F475: 7D F7 F8   ADC $F8F7,X         ; 
F478: 85 E9      STA <$E9            ; 
F47A: A5 DC      LDA <$DC            ; 
F47C: C9 1F      CMP #$1F            ; 
F47E: 90 1A      BCC $F49A           ; 
F480: E9 1F      SBC #$1F            ; 
F482: 4A         LSR A               ; 
F483: AA         TAX                 ; 
F484: BD F1 F7   LDA $F7F1,X         ; 
F487: 85 D3      STA <$D3            ; 
F489: 85 D4      STA <$D4            ; 
F48B: BD E9 F7   LDA $F7E9,X         ; 
F48E: AA         TAX                 ; 
F48F: A0 00      LDY #$00            ; 
F491: 20 EF F4   JSR $F4EF           ; 
F494: A9 1F      LDA #$1F            ; 
F496: 85 DC      STA <$DC            ; 
F498: D0 0B      BNE $F4A5           ; 
F49A: A9 99      LDA #$99            ; 
F49C: 85 D3      STA <$D3            ; 
F49E: 85 D4      STA <$D4            ; 
F4A0: D0 03      BNE $F4A5           ; 
F4A2: 4C D4 F4   JMP $F4D4           ; 
F4A5: 24 E3      BIT <$E3            ; 
F4A7: 10 2B      BPL $F4D4           ; 
F4A9: 70 29      BVS $F4D4           ; 
F4AB: A9 80      LDA #$80            ; 
F4AD: 85 A2      STA <$A2            ; 
F4AF: 85 A3      STA <$A3            ; 
F4B1: 85 A4      STA <$A4            ; 
F4B3: A9 00      LDA #$00            ; 
F4B5: 85 94      STA <$94            ; 
F4B7: A5 80      LDA <$80            ; 
F4B9: C9 06      CMP #$06            ; 
F4BB: D0 11      BNE $F4CE           ; 
F4BD: A5 D9      LDA <$D9            ; 
F4BF: 29 20      AND #$20            ; 
F4C1: D0 0B      BNE $F4CE           ; 
F4C3: A9 80      LDA #$80            ; 
F4C5: 85 D9      STA <$D9            ; 
F4C7: A2 FF      LDX #$FF            ; 
F4C9: 86 A1      STX <$A1            ; 
F4CB: E8         INX                 ; 
F4CC: 86 8C      STX <$8C            ; 
F4CE: A9 40      LDA #$40            ; 
F4D0: 05 E3      ORA <$E3            ; 
F4D2: 85 E3      STA <$E3            ; 
; Near the beginning of scanline 223
```

# Bank Switch (to bank 0)

```code
; Asteroids uses a different scheme to switch banks. It uses overlapping code in 
; both banks so that when a switch happens the code continues on to the next 
; instruction, but in a different bank.

; ET writes the six byte switch-then-jump code to RAM and executes it there.

; There are only two switch-points in the code. Bank 1 is called upon to handle 
; the visible part of the screen. Bank 0 handles the invisible part of the screen.

; - BCCC (bank 0) to F548 (bank 1) ... when the screen is being drawn
; - F4EC (bank 1) to B02D (bank 0) ... when the screen is not being drawn

; 0083: AD F8 FF    LDA $FFF8  ; Switch to Bank 0
; 0086: 4C 2D B0    JMP $B02D  ; Jump to B02D

F4D4: A9 2D      LDA #$2D            ; Jump address ...
F4D6: 85 87      STA <$87            ; ...
F4D8: A9 B0      LDA #$B0            ; ...
F4DA: 85 88      STA <$88            ; ... B02D
;
F4DC: A9 AD      LDA #$AD            ; Opcode ...
F4DE: 85 83      STA <$83            ; ...
F4E0: A9 F8      LDA #$F8            ; ...
F4E2: 85 84      STA <$84            ; ...
F4E4: A9 FF      LDA #$FF            ; ...
F4E6: 85 85      STA <$85            ; ... LDA $FFF8
;
F4E8: A9 4C      LDA #$4C            ; Opcode JMP for ...
F4EA: 85 86      STA <$86            ; ... B02D (earlier)
F4EC: 4C 83 00   JMP $0083           ; Jump to RAM to make the switch

F4EF: F8         SED                 ; 
F4F0: 84 83      STY <$83            ; 
F4F2: 18         CLC                 ; 
F4F3: A5 E1      LDA <$E1            ; 
F4F5: 65 83      ADC <$83            ; 
F4F7: 85 E1      STA <$E1            ; 
F4F9: 86 83      STX <$83            ; 
F4FB: A5 E0      LDA <$E0            ; 
F4FD: 65 83      ADC <$83            ; 
F4FF: 85 E0      STA <$E0            ; 
F501: A5 DF      LDA <$DF            ; 
F503: 69 00      ADC #$00            ; 
F505: 85 DF      STA <$DF            ; 
F507: D8         CLD                 ; 
F508: 60         RTS                 ; 
F509: A4 83      LDY <$83            ; 
F50B: B1 BE      LDA ($BE),Y         ; 
F50D: 85 1B      STA <$1B            ;{-2_GRP0} 
F50F: 85 02      STA <$02            ;{-2_WSYNC} 
F511: B1 C0      LDA ($C0),Y         ; 
F513: 85 1C      STA <$1C            ;{-2_GRP1} 
F515: B1 C2      LDA ($C2),Y         ; 
F517: 85 1B      STA <$1B            ;{-2_GRP0} 
F519: B1 C4      LDA ($C4),Y         ; 
F51B: 85 84      STA <$84            ; 
F51D: B1 C6      LDA ($C6),Y         ; 
F51F: AA         TAX                 ; 
F520: B1 C8      LDA ($C8),Y         ; 
F522: A8         TAY                 ; 
F523: A5 84      LDA <$84            ; 
F525: 85 1C      STA <$1C            ;{-2_GRP1} 
F527: 86 1B      STX <$1B            ;{-2_GRP0} 
F529: 84 1C      STY <$1C            ;{-2_GRP1} 
F52B: 84 1B      STY <$1B            ;{-2_GRP0} 
F52D: C6 83      DEC <$83            ; 
F52F: 10 D8      BPL $F509           ; 
F531: A9 00      LDA #$00            ; 
F533: 85 02      STA <$02            ;{-2_WSYNC} 
F535: 85 1B      STA <$1B            ;{-2_GRP0} 
F537: 85 1C      STA <$1C            ;{-2_GRP1} 
F539: 85 1B      STA <$1B            ;{-2_GRP0} 
F53B: 85 1C      STA <$1C            ;{-2_GRP1} 
F53D: 85 04      STA <$04            ;{-2_NUSIZ0} 
F53F: 85 05      STA <$05            ;{-2_NUSIZ1} 
F541: 85 25      STA <$25            ;{-2_VDELP0} 
F543: 85 26      STA <$26            ;{-2_VDELP1} 
F545: 85 02      STA <$02            ;{-2_WSYNC} 
F547: 60         RTS                 ; 
```

# Visible Screen

```code
; The code comes here from BCCC after the switch from bank 0.

; Near the middle of scanline 40
F548: A9 06      LDA #$06            ; 
F54A: 85 05      STA <$05            ;{-2_NUSIZ1} 
F54C: A9 52      LDA #$52            ; 
F54E: 85 09      STA <$09            ;{-2_COLUBK} 
F550: A9 00      LDA #$00            ; 
F552: 85 02      STA <$02            ;{-2_WSYNC} 
F554: 85 01      STA <$01            ;{-2_VBLANK} 
F556: 85 2B      STA <$2B            ;{-2_HMCLR} 
F558: 85 2C      STA <$2C            ;{-2_CXCLR} 
F55A: A9 FC      LDA #$FC            ; 
F55C: 85 BF      STA <$BF            ; 
F55E: 85 C1      STA <$C1            ; 
F560: A9 FB      LDA #$FB            ; 
F562: 85 C3      STA <$C3            ; 
F564: 85 02      STA <$02            ;{-2_WSYNC} 
F566: A2 03      LDX #$03            ; 
F568: 24 CA      BIT <$CA            ; 
F56A: 10 01      BPL $F56D           ; 
F56C: CA         DEX                 ; 
F56D: 24 CB      BIT <$CB            ; 
F56F: 10 01      BPL $F572           ; 
F571: CA         DEX                 ; 
F572: 24 CC      BIT <$CC            ; 
F574: 10 01      BPL $F577           ; 
F576: CA         DEX                 ; 
F577: BD E8 FB   LDA $FBE8,X         ; 
F57A: 85 C2      STA <$C2            ; 
F57C: 85 02      STA <$02            ;{-2_WSYNC} 
F57E: A9 00      LDA #$00            ; 
F580: A4 80      LDY <$80            ; 
F582: C0 07      CPY #$07            ; 
F584: 90 1E      BCC $F5A4           ; 
F586: 85 C0      STA <$C0            ; 
F588: 85 C2      STA <$C2            ; 
F58A: D0 0D      BNE $F599           ; 
F58C: A2 30      LDX #$30            ; 
F58E: A5 DE      LDA <$DE            ; 
F590: 6A         ROR A               ; 
F591: 90 02      BCC $F595           ; 
F593: A2 A8      LDX #$A8            ; 
F595: 86 BE      STX <$BE            ; 
F597: D0 0B      BNE $F5A4           ; 
F599: A9 FA      LDA #$FA            ; 
F59B: 85 BF      STA <$BF            ; 
F59D: A5 EA      LDA <$EA            ; 
F59F: 0A         ASL A               ; 
F5A0: 0A         ASL A               ; 
F5A1: 0A         ASL A               ; 
F5A2: 85 BE      STA <$BE            ; 
F5A4: 85 02      STA <$02            ;{-2_WSYNC} 
F5A6: 24 EB      BIT <$EB            ; 
F5A8: 10 06      BPL $F5B0           ; 
F5AA: A9 00      LDA #$00            ; 
F5AC: 85 C0      STA <$C0            ; 
F5AE: 85 C2      STA <$C2            ; 
F5B0: A5 F3      LDA <$F3            ; 
F5B2: F0 04      BEQ $F5B8           ; 
F5B4: A9 D8      LDA #$D8            ; 
F5B6: 85 C0      STA <$C0            ; 
F5B8: A9 07      LDA #$07            ; 
F5BA: 85 83      STA <$83            ; 
F5BC: A4 83      LDY <$83            ; 
F5BE: 85 02      STA <$02            ;{-2_WSYNC} 
F5C0: EA         NOP                 ; 
F5C1: EA         NOP                 ; 
F5C2: A5 8E      LDA <$8E            ; 
F5C4: 48         PHA                 ; 
F5C5: A5 90      LDA <$90            ; 
F5C7: 85 07      STA <$07            ;{-2_COLUP1} 
F5C9: B1 C2      LDA ($C2),Y         ; 
F5CB: 85 1C      STA <$1C            ;{-2_GRP1} 
F5CD: B1 BE      LDA ($BE),Y         ; 
F5CF: AA         TAX                 ; 
F5D0: B1 C0      LDA ($C0),Y         ; 
F5D2: A8         TAY                 ; 
F5D3: 68         PLA                 ; 
F5D4: 85 07      STA <$07            ;{-2_COLUP1} 
F5D6: 86 1C      STX <$1C            ;{-2_GRP1} 
F5D8: A5 8F      LDA <$8F            ; 
F5DA: 85 07      STA <$07            ;{-2_COLUP1} 
F5DC: 84 1C      STY <$1C            ;{-2_GRP1} 
F5DE: C6 83      DEC <$83            ; 
F5E0: 10 DA      BPL $F5BC           ; 
F5E2: 85 02      STA <$02            ;{-2_WSYNC} 
F5E4: A9 00      LDA #$00            ; 
F5E6: 85 1C      STA <$1C            ;{-2_GRP1} 
F5E8: 85 05      STA <$05            ;{-2_NUSIZ1} 
F5EA: 85 02      STA <$02            ;{-2_WSYNC} 
F5EC: 85 02      STA <$02            ;{-2_WSYNC} 
F5EE: 85 02      STA <$02            ;{-2_WSYNC} 
F5F0: A9 00      LDA #$00            ; 
F5F2: 85 09      STA <$09            ;{-2_COLUBK} 
F5F4: A2 01      LDX #$01            ; 
F5F6: 85 02      STA <$02            ;{-2_WSYNC} 
F5F8: EA         NOP                 ; 
F5F9: EA         NOP                 ; 
F5FA: A5 D5      LDA <$D5            ; 
F5FC: A5 D5      LDA <$D5            ; 
F5FE: 95 20      STA $20,X           ; 
F600: 29 0F      AND #$0F            ; 
F602: A8         TAY                 ; 
F603: 88         DEY                 ; 
F604: 10 FD      BPL $F603           ; 
F606: 95 10      STA $10,X           ; 
F608: 85 02      STA <$02            ;{-2_WSYNC} 
F60A: 85 2A      STA <$2A            ;{-2_HMOVE} 
F60C: A9 11      LDA #$11            ; 
F60E: A6 80      LDX <$80            ; 
F610: E0 05      CPX #$05            ; 
F612: D0 02      BNE $F616           ; 
F614: A9 15      LDA #$15            ; 
F616: 85 0A      STA <$0A            ;{-2_CTRLPF} 
F618: A2 FF      LDX #$FF            ; 
F61A: 2C 80 02   BIT $0280           ; 
F61D: 10 01      BPL $F620           ; 
F61F: E8         INX                 ; 
F620: 86 0C      STX <$0C            ;{-2_PEFP1} 
F622: A6 A1      LDX <$A1            ; 
F624: 30 18      BMI $F63E           ; 
F626: 24 91      BIT <$91            ; 
F628: 70 14      BVS $F63E           ; 
F62A: A0 FF      LDY #$FF            ; 
F62C: B5 A2      LDA $A2,X           ; 
F62E: 10 05      BPL $F635           ; 
F630: BD E6 FF   LDA $FFE6,X         ; 
F633: D0 02      BNE $F637           ; 
F635: A5 96      LDA <$96            ; 
F637: C5 95      CMP <$95            ; 
F639: 90 01      BCC $F63C           ; 
F63B: C8         INY                 ; 
F63C: 84 0B      STY <$0B            ;{-2_REFP0} 
F63E: 85 02      STA <$02            ;{-2_WSYNC} 
F640: A6 80      LDX <$80            ; 
F642: E0 07      CPX #$07            ; 
F644: D0 12      BNE $F658           ; 
F646: 24 ED      BIT <$ED            ; 
F648: 10 06      BPL $F650           ; 
F64A: A9 11      LDA #$11            ; 
F64C: 85 0A      STA <$0A            ;{-2_CTRLPF} 
F64E: D0 06      BNE $F656           ; 
F650: A9 15      LDA #$15            ; 
F652: 85 0A      STA <$0A            ;{-2_CTRLPF} 
F654: A9 FF      LDA #$FF            ; 
F656: 85 0B      STA <$0B            ;{-2_REFP0} 
F658: A2 00      LDX #$00            ; 
F65A: 24 E3      BIT <$E3            ; 
F65C: 30 09      BMI $F667           ; 
F65E: A5 D3      LDA <$D3            ; 
F660: 4A         LSR A               ; 
F661: 4A         LSR A               ; 
F662: 4A         LSR A               ; 
F663: 4A         LSR A               ; 
F664: 4A         LSR A               ; 
F665: AA         TAX                 ; 
F666: E8         INX                 ; 
F667: BD F9 F7   LDA $F7F9,X         ; 
F66A: 85 07      STA <$07            ;{-2_COLUP1} 
F66C: 85 02      STA <$02            ;{-2_WSYNC} 
F66E: A6 80      LDX <$80            ; 
F670: BD D9 FD   LDA $FDD9,X         ; 
F673: 85 08      STA <$08            ;{-2_COLUPF} 
F675: A0 FF      LDY #$FF            ; 
F677: 84 0D      STY <$0D            ;{-2_PF0} 
F679: 84 0E      STY <$0E            ;{-2_PF1} 
F67B: 84 0F      STY <$0F            ;{-2_PF2} 
F67D: BD E2 FD   LDA $FDE2,X         ; 
F680: 85 09      STA <$09            ;{-2_COLUBK} 
F682: A9 20      LDA #$20            ; 
F684: 24 EB      BIT <$EB            ; 
F686: 10 02      BPL $F68A           ; 
F688: A9 25      LDA #$25            ; 
F68A: 85 04      STA <$04            ;{-2_NUSIZ0} 
F68C: A9 20      LDA #$20            ; 
F68E: 85 05      STA <$05            ;{-2_NUSIZ1} 
F690: 85 02      STA <$02            ;{-2_WSYNC} 
F692: 85 02      STA <$02            ;{-2_WSYNC} 
F694: 85 02      STA <$02            ;{-2_WSYNC} 
F696: A4 80      LDY <$80            ; 
F698: 85 02      STA <$02            ;{-2_WSYNC} 
F69A: A9 00      LDA #$00            ; 
F69C: 85 0E      STA <$0E            ;{-2_PF1} 
F69E: 85 0F      STA <$0F            ;{-2_PF2} 
F6A0: BE 05 F8   LDX $F805,Y         ; 
F6A3: BD F4 F8   LDA $F8F4,X         ; 
F6A6: 48         PHA                 ; 
F6A7: BD F3 F8   LDA $F8F3,X         ; 
F6AA: 48         PHA                 ; 
F6AB: A9 00      LDA #$00            ; 
F6AD: AA         TAX                 ; 
F6AE: A8         TAY                 ; 
F6AF: 85 86      STA <$86            ; 
F6B1: 85 87      STA <$87            ; 
F6B3: 85 88      STA <$88            ; 
F6B5: 60         RTS                 ; 
F6B6: A5 E6      LDA <$E6            ; 
F6B8: 29 F0      AND #$F0            ; 
F6BA: C9 90      CMP #$90            ; 
F6BC: D0 3D      BNE $F6FB           ; 
F6BE: 24 F0      BIT <$F0            ; 
F6C0: 30 39      BMI $F6FB           ; 
F6C2: A5 DD      LDA <$DD            ; 
F6C4: C9 07      CMP #$07            ; 
F6C6: D0 21      BNE $F6E9           ; 
F6C8: A5 F0      LDA <$F0            ; 
F6CA: 29 03      AND #$03            ; 
F6CC: C9 03      CMP #$03            ; 
F6CE: D0 02      BNE $F6D2           ; 
F6D0: A9 02      LDA #$02            ; 
F6D2: AA         TAX                 ; 
F6D3: B5 CA      LDA $CA,X           ; 
F6D5: 10 12      BPL $F6E9           ; 
F6D7: A6 F0      LDX <$F0            ; 
F6D9: E0 02      CPX #$02            ; 
F6DB: B0 09      BCS $F6E6           ; 
F6DD: BD FD F9   LDA $F9FD,X         ; 
F6E0: 85 F2      STA <$F2            ; 
F6E2: A9 32      LDA #$32            ; 
F6E4: 85 9B      STA <$9B            ; 
F6E6: 38         SEC                 ; 
F6E7: B0 01      BCS $F6EA           ; 
F6E9: 18         CLC                 ; 
F6EA: A5 F0      LDA <$F0            ; 
F6EC: 2A         ROL A               ; 
F6ED: 09 80      ORA #$80            ; 
F6EF: 85 F0      STA <$F0            ; 
F6F1: 29 07      AND #$07            ; 
F6F3: C9 07      CMP #$07            ; 
F6F5: D0 04      BNE $F6FB           ; 
F6F7: A9 69      LDA #$69            ; 
F6F9: 85 F1      STA <$F1            ; 
F6FB: 60         RTS                 ; 
F6FC: 00         BRK                 ; 
F6FD: 00         BRK                 ; 
F6FE: 00         BRK                 ; 
F6FF: 00         BRK                 ; 
F700: D0 00      BNE $F702           ; 
F702: D0 E0      BNE $F6E4           ; 
F704: 10 E0      BPL $F6E6           ; 
F706: 50 F0      BVC $F6F8           ; 
F708: 40         RTI                 ; 
F709: F0 A0      BEQ $F6AB           ; 
F70B: D0 A8      BNE $F6B5           ; 
F70D: F4 
F70E: C8         INY                 ; 
F70F: F0 A8      BEQ $F6B9           ; 
F711: D4 
F712: EC D8 74   CPX $74D8           ; 
F715: F8         SED                 ; 
F716: B4 F8      LDY $F8,X           ; 
F718: F4 
F719: 58         CLI                 ; 
F71A: F8         SED                 ; 
F71B: D8         CLD                 ; 
F71C: D0 D0      BNE $F6EE           ; 
F71E: A0 40      LDY #$40            ; 
F720: 80 
F721: 00         BRK                 ; 
F722: 00         BRK                 ; 
F723: 00         BRK                 ; 
F724: 00         BRK                 ; 
F725: 00         BRK                 ; 
F726: 00         BRK                 ; 
F727: 00         BRK                 ; 
F728: 00         BRK                 ; 
F729: 00         BRK                 ; 
F72A: 00         BRK                 ; 
F72B: 00         BRK                 ; 
F72C: 00         BRK                 ; 
F72D: 00         BRK                 ; 
F72E: 00         BRK                 ; 
F72F: 00         BRK                 ; 
F730: 00         BRK                 ; 
F731: 00         BRK                 ; 
F732: 00         BRK                 ; 
F733: 01 01      ORA ($01,X)         ; 
F735: 03 
F736: 02 
F737: 07 
F738: 05 07      ORA <$07            ; 
F73A: 0D 0F 1D   ORA $1D0F           ; 
F73D: 16 1F      ASL $1F,X           ; 
F73F: 1B 
F740: 1D 1E 0F   ORA $0F1E,X         ; 
F743: 07 
F744: 07 
F745: 07 
F746: 03 
F747: 01 00      ORA ($00,X)         ; 
F749: 00         BRK                 ; 
F74A: 00         BRK                 ; 
F74B: 00         BRK                 ; 
F74C: 00         BRK                 ; 
F74D: 01 03      ORA ($03,X)         ; 
F74F: 06 0D      ASL <$0D            ; 
F751: 08         PHP                 ; 
F752: 1B 
F753: 1B 
F754: 1F 
F755: 0F 
F756: 2F 
F757: 1F 
F758: 37 
F759: 3F 
F75A: DB 
F75B: 7F 
F75C: DD 6F B5   CMP $B56F,X         ; 
F75F: 1B 
F760: 1D 17 3A   ORA $3A17,X         ; 
F763: 1D 1A B5   ORA $B51A,X         ; 
F766: 5E F5 6B   LSR $6BF5,X         ; 
F769: A7 
F76A: 5F 
F76B: BF 
F76C: FF 
F76D: FF 
F76E: FF 
F76F: FE 7B 00   INC $007B,X         ; 
F772: 00         BRK                 ; 
F773: 7F 
F774: C0 AA      CPY #$AA            ; 
F776: 7F 
F777: FF 
F778: EF 
F779: 00         BRK                 ; 
F77A: FF 
F77B: FF 
F77C: FF 
F77D: DF 
F77E: FF 
F77F: FF 
F780: DF 
F781: FF 
F782: FF 
F783: DF 
F784: FF 
F785: FF 
F786: FD 27 25   SBC $2527,X         ; 
F789: FE FB FE   INC $FEFB,X         ; 
F78C: 7B 
F78D: D6 BF      DEC $BF,X           ; 
F78F: D7 
F790: EF 
F791: D7 
F792: FF 
F793: D7 
F794: E7 
F795: D3 
F796: A1 80      LDA ($80,X)         ; 
F798: 00         BRK                 ; 
F799: 01 00      ORA ($00,X)         ; 
F79B: 81 C1      STA ($C1,X)         ; 
F79D: 61 30      ADC ($30,X)         ; 
F79F: 98         TYA                 ; 
F7A0: 9E 
F7A1: 0F 
F7A2: E7 
F7A3: F7 
F7A4: FF 
F7A5: FF 
F7A6: ED FA F7   SBC $F7FA           ; 
F7A9: EF 
F7AA: BF 
F7AB: FD 5A FF   SBC $FF5A,X         ; 
F7AE: D5 A2      CMP $A2,X           ; 
F7B0: 63 
F7B1: E3 
F7B2: 67 
F7B3: E3 
F7B4: A2 D5      LDX #$D5            ; 
F7B6: 7F 
F7B7: AA         TAX                 ; 
F7B8: D5 FB      CMP $FB,X           ; 
F7BA: FF 
F7BB: FF 
F7BC: FF 
F7BD: FF 
F7BE: FF 
F7BF: FF 
F7C0: 2A         ROL A               ; 
F7C1: FF 
F7C2: 15 FF      ORA $FF,X           ; 
F7C4: FF 
F7C5: 4A         LSR A               ; 
F7C6: BF 
F7C7: 5F 
F7C8: 2D 57 BB   AND $BB57           ; 
F7CB: DD EE FB   CMP $FBEE,X         ; 
F7CE: DD EE FF   CMP $FFEE,X         ; 
F7D1: 57 
F7D2: FF 
F7D3: BF 
F7D4: EB 
F7D5: B5 DF      LDA $DF,X           ; 
F7D7: EA         NOP                 ; 
F7D8: FF 
F7D9: 5A 
F7DA: FF 
F7DB: 6D F7 BE   ADC $BEF7           ; 
F7DE: 5F 
F7DF: B6 7E      LDX $7E,Y           ; 
F7E1: F6 F5      INC $F5,X           ; 
F7E3: F4 
F7E4: E8         INX                 ; 
F7E5: D0 80      BNE $F767           ; 
F7E7: 00         BRK                 ; 
F7E8: 00         BRK                 ; 
F7E9: 00         BRK                 ; 
F7EA: 10 22      BPL $F80E           ; 
F7EC: 34 
F7ED: 45 63      EOR <$63            ; 
F7EF: 78         SEI                 ; 
F7F0: 99 99 92   STA $9299,Y         ; 
F7F3: 84 76      STY <$76            ; 
F7F5: 68         PLA                 ; 
F7F6: 59 51 42   EOR $4251,Y         ; 
F7F9: 0E DE DC   ASL $DCDE           ; 
F7FC: DA 
F7FD: DA 
F7FE: DA 
F7FF: 00         BRK                 ; 
F800: 00         BRK                 ; 
F801: 00         BRK                 ; 
F802: 00         BRK                 ; 
F803: 00         BRK                 ; 
F804: 00         BRK                 ; 
F805: 00         BRK                 ; 
F806: 00         BRK                 ; 
F807: 00         BRK                 ; 
F808: 00         BRK                 ; 
F809: 00         BRK                 ; 
F80A: 00         BRK                 ; 
F80B: 00         BRK                 ; 
F80C: 00         BRK                 ; 
F80D: 02 
F80E: 02 
F80F: 02 
F810: 02 
F811: 02 
F812: 07 
F813: 07 
F814: 07 
F815: 07 
F816: 07 
F817: 07 
F818: 07 
F819: 07 
F81A: 0F 
F81B: 0F 
F81C: 0F 
F81D: 0F 
F81E: 0F 
F81F: 0F 
F820: 0F 
F821: 0F 
F822: 0F 
F823: 0F 
F824: 0F 
F825: 0F 
F826: 07 
F827: 07 
F828: 07 
F829: 07 
F82A: 07 
F82B: 07 
F82C: 07 
F82D: 07 
F82E: 02 
F82F: 02 
F830: 02 
F831: 02 
F832: 02 
F833: 00         BRK                 ; 
F834: 00         BRK                 ; 
F835: 00         BRK                 ; 
F836: 00         BRK                 ; 
F837: 00         BRK                 ; 
F838: 00         BRK                 ; 
F839: 00         BRK                 ; 
F83A: 00         BRK                 ; 
F83B: 00         BRK                 ; 
F83C: 00         BRK                 ; 
F83D: 00         BRK                 ; 
F83E: 00         BRK                 ; 
F83F: 00         BRK                 ; 
F840: 00         BRK                 ; 
F841: 00         BRK                 ; 
F842: 00         BRK                 ; 
F843: 80 
F844: C0 E0      CPY #$E0            ; 
F846: E0 E0      CPX #$E0            ; 
F848: C0 80      CPY #$80            ; 
F84A: 00         BRK                 ; 
F84B: 00         BRK                 ; 
F84C: 00         BRK                 ; 
F84D: 01 01      ORA ($01,X)         ; 
F84F: 01 01      ORA ($01,X)         ; 
F851: 01 01      ORA ($01,X)         ; 
F853: 01 01      ORA ($01,X)         ; 
F855: 01 01      ORA ($01,X)         ; 
F857: 01 01      ORA ($01,X)         ; 
F859: 00         BRK                 ; 
F85A: 00         BRK                 ; 
F85B: 00         BRK                 ; 
F85C: 80 
F85D: C0 E0      CPY #$E0            ; 
F85F: E0 E0      CPX #$E0            ; 
F861: C0 80      CPY #$80            ; 
F863: 00         BRK                 ; 
F864: 00         BRK                 ; 
F865: 00         BRK                 ; 
F866: 00         BRK                 ; 
F867: 00         BRK                 ; 
F868: 00         BRK                 ; 
F869: 00         BRK                 ; 
F86A: 00         BRK                 ; 
F86B: 00         BRK                 ; 
F86C: 00         BRK                 ; 
F86D: 00         BRK                 ; 
F86E: 00         BRK                 ; 
F86F: 00         BRK                 ; 
F870: 00         BRK                 ; 
F871: 00         BRK                 ; 
F872: 00         BRK                 ; 
F873: AA         TAX                 ; 
F874: 55 AB      EOR $AB,X           ; 
F876: 57 
F877: A2 C1      LDX #$C1            ; 
F879: C0 55      CPY #$55            ; 
F87B: A2 C1      LDX #$C1            ; 
F87D: C0 55      CPY #$55            ; 
F87F: A2 C1      LDX #$C1            ; 
F881: C0 55      CPY #$55            ; 
F883: A2 C1      LDX #$C1            ; 
F885: D0 55      BNE $F8DC           ; 
F887: BA         TSX                 ; 
F888: 7D FC 55   ADC $55FC,X         ; 
F88B: BA         TSX                 ; 
F88C: 7D FE 54   ADC $54FE,X         ; 
F88F: 38         SEC                 ; 
F890: 7D FE 54   ADC $54FE,X         ; 
F893: 38         SEC                 ; 
F894: 7D FE 54   ADC $54FE,X         ; 
F897: 38         SEC                 ; 
F898: 55 AA      EOR $AA,X           ; 
F89A: 55 2B      EOR $2B,X           ; 
F89C: 47 
F89D: 83 
F89E: 01 AB      ORA ($AB,X)         ; 
F8A0: 47 
F8A1: 83 
F8A2: 01 AB      ORA ($AB,X)         ; 
F8A4: 47 
F8A5: 83 
F8A6: 01 AB      ORA ($AB,X)         ; 
F8A8: 47 
F8A9: 83 
F8AA: 01 AB      ORA ($AB,X)         ; 
F8AC: C5 82      CMP <$82            ; 
F8AE: C1 EA      CMP ($EA,X)         ; 
F8B0: E5 AA      SBC <$AA            ; 
F8B2: D5 55      CMP $55,X           ; 
F8B4: AB 
F8B5: 57 
F8B6: 2F 
F8B7: 15 0B      ORA $0B,X           ; 
F8B9: 55 2A      EOR $2A,X           ; 
F8BB: 15 0E      ORA $0E,X           ; 
F8BD: 5F 
F8BE: 3F 
F8BF: 15 0E      ORA $0E,X           ; 
F8C1: 5F 
F8C2: 3F 
F8C3: 15 0E      ORA $0E,X           ; 
F8C5: 5F 
F8C6: 3F 
F8C7: 15 0E      ORA $0E,X           ; 
F8C9: 5F 
F8CA: 3F 
F8CB: 55 AE      EOR $AE,X           ; 
F8CD: 54 
F8CE: A8         TAY                 ; 
F8CF: D0 EA      BNE $F8BB           ; 
F8D1: F4 
F8D2: A8         TAY                 ; 
F8D3: D0 EA      BNE $F8BF           ; 
F8D5: F4 
F8D6: A8         TAY                 ; 
F8D7: D0 EA      BNE $F8C3           ; 
F8D9: F4 
F8DA: A8         TAY                 ; 
F8DB: D1 EB      CMP ($EB),Y         ; 
F8DD: F7 
F8DE: AA         TAX                 ; 
F8DF: D5 EB      CMP $EB,X           ; 
F8E1: C7 
F8E2: 82 
F8E3: 81 AB      STA ($AB,X)         ; 
F8E5: 47 
F8E6: 82 
F8E7: 01 AB      ORA ($AB,X)         ; 
F8E9: 47 
F8EA: 8A         TXA                 ; 
F8EB: 1D BE 7F   ORA $7FBE,X         ; 
F8EE: AA         TAX                 ; 
F8EF: 1D BE 7F   ORA $7FBE,X         ; 
F8F2: AA         TAX                 ; 
F8F3: 2D F0 7E   AND $7EF0           ; 
F8F6: F0 73      BEQ $F96B           ; 
F8F8: 0D 5B D5   ORA $D55B           ; 
F8FB: 00         BRK                 ; 
F8FC: 00         BRK                 ; 
F8FD: 00         BRK                 ; 
F8FE: 00         BRK                 ; 
F8FF: 00         BRK                 ; 
F900: FE FF C3   INC $C3FF,X         ; 
F903: 0F 
F904: FF 
F905: 3F 
F906: 2B 
F907: E7 
F908: 00         BRK                 ; 
F909: FE FF C3   INC $C3FF,X         ; 
F90C: 03 
F90D: 0F 
F90E: FF 
F90F: 3F 
F910: 2B 
F911: E7 
F912: 00         BRK                 ; 
F913: FE FF C3   INC $C3FF,X         ; 
F916: 03 
F917: 03 
F918: 0F 
F919: FF 
F91A: 3F 
F91B: 2B 
F91C: E7 
F91D: 00         BRK                 ; 
F91E: FE FF C3   INC $C3FF,X         ; 
F921: 03 
F922: 03 
F923: 03 
F924: 0F 
F925: FF 
F926: 3F 
F927: 2B 
F928: E7 
F929: 00         BRK                 ; 
F92A: FE FF 03   INC $03FF,X         ; 
F92D: 03 
F92E: 03 
F92F: 03 
F930: 03 
F931: 0F 
F932: FF 
F933: 3F 
F934: 2B 
F935: E7 
F936: 00         BRK                 ; 
F937: BF 
F938: FF 
F939: 03 
F93A: 1F 
F93B: BF 
F93C: 3F 
F93D: 63 
F93E: 00         BRK                 ; 
F93F: 00         BRK                 ; 
F940: BF 
F941: FF 
F942: 03 
F943: 03 
F944: 1F 
F945: BF 
F946: 3F 
F947: 63 
F948: 00         BRK                 ; 
F949: 00         BRK                 ; 
F94A: BF 
F94B: FF 
F94C: 03 
F94D: 03 
F94E: 03 
F94F: 1F 
F950: BF 
F951: 3F 
F952: 63 
F953: 00         BRK                 ; 
F954: 00         BRK                 ; 
F955: BF 
F956: FF 
F957: 03 
F958: 03 
F959: 03 
F95A: 03 
F95B: 1F 
F95C: BF 
F95D: 3F 
F95E: 63 
F95F: 00         BRK                 ; 
F960: 00         BRK                 ; 
F961: BF 
F962: FF 
F963: 03 
F964: 03 
F965: 03 
F966: 03 
F967: 03 
F968: 1F 
F969: BF 
F96A: 3F 
F96B: 63 
F96C: 00         BRK                 ; 
F96D: 00         BRK                 ; 
F96E: E0 A2      CPX #$A2            ; 
F970: E7 
F971: EE FB 00   INC $00FB           ; 
F974: E0 E3      CPX #$E3            ; 
F976: EF 
F977: ED FF 00   SBC $00FF           ; 
F97A: FE FF C3   INC $C3FF,X         ; 
F97D: 0F 
F97E: FF 
F97F: 3F 
F980: 3F 
F981: 60         RTS                 ; 
F982: 00         BRK                 ; 
F983: BF 
F984: FF 
F985: 03 
F986: 1F 
F987: BF 
F988: 3F 
F989: 27 
F98A: E0 00      CPX #$00            ; 
F98C: FE FF C3   INC $C3FF,X         ; 
F98F: 0F 
F990: FF 
F991: 3F 
F992: 7E 03 00   ROR $0003,X         ; 
F995: BF 
F996: FF 
F997: 03 
F998: 1F 
F999: BF 
F99A: 3F 
F99B: E1 07      SBC ($07,X)         ; 
F99D: 00         BRK                 ; 
F99E: E0 F0      CPX #$F0            ; 
F9A0: F8         SED                 ; 
F9A1: DC 
F9A2: CE C6 E0   DEC $E0C6           ; 
F9A5: F0 D8      BEQ $F97F           ; 
F9A7: CC C6 E0   CPY $E0C6           ; 
F9AA: F0 78      BEQ $FA24           ; 
F9AC: 3C 
F9AD: 1E 10 18   ASL $1810,X         ; 
F9B0: 18         CLC                 ; 
F9B1: 18         CLC                 ; 
F9B2: 18         CLC                 ; 
F9B3: 18         CLC                 ; 
F9B4: 18         CLC                 ; 
F9B5: 18         CLC                 ; 
F9B6: 18         CLC                 ; 
F9B7: 18         CLC                 ; 
F9B8: 18         CLC                 ; 
F9B9: F8         SED                 ; 
F9BA: 78         SEI                 ; 
F9BB: 3C 
F9BC: 1E 0F 00   ASL $000F,X         ; 
F9BF: 00         BRK                 ; 
F9C0: 00         BRK                 ; 
F9C1: 0A         ASL A               ; 
F9C2: 1A 
F9C3: 76 3A      ROR <$3A,X          ; 
F9C5: 00         BRK                 ; 
F9C6: 00         BRK                 ; 
F9C7: 1C 
F9C8: 1C 
F9C9: 20 1C 38   JSR $381C           ; 
F9CC: 00         BRK                 ; 
F9CD: 14 
F9CE: 1C 
F9CF: 10 1C      BPL $F9ED           ; 
F9D1: 10 18      BPL $F9EB           ; 
F9D3: 14 
F9D4: 1C 
F9D5: 14 
F9D6: 08         PHP                 ; 
F9D7: 0C 
F9D8: 08         PHP                 ; 
F9D9: 18         CLC                 ; 
F9DA: 00         BRK                 ; 
F9DB: 00         BRK                 ; 
F9DC: 00         BRK                 ; 
F9DD: 0D 07 40   ORA $4007           ; 
F9E0: 08         PHP                 ; 
F9E1: 00         BRK                 ; 
F9E2: 00         BRK                 ; 
F9E3: 2A         ROL A               ; 
F9E4: 0A         ASL A               ; 
F9E5: 20 0A 08   JSR $080A           ; 
F9E8: 00         BRK                 ; 
F9E9: 2A         ROL A               ; 
F9EA: 2A         ROL A               ; 
F9EB: 10 12      BPL $F9FF           ; 
F9ED: 28         PLP                 ; 
F9EE: 08         PHP                 ; 
F9EF: 2A         ROL A               ; 
F9F0: 2A         ROL A               ; 
F9F1: 08         PHP                 ; 
F9F2: 0A         ASL A               ; 
F9F3: 08         PHP                 ; 
F9F4: 28         PLP                 ; 
F9F5: 08         PHP                 ; 
F9F6: FE FE FC   INC $FCFE,X         ; 
F9F9: 4A         LSR A               ; 
F9FA: 48         PHA                 ; 
F9FB: 46 44      LSR <$44            ; 
F9FD: 80 
F9FE: C0 00      CPY #$00            ; 
FA00: FE 86 86   INC $8686,X         ; 
FA03: 86 82      STX <$82            ; 
FA05: 82 
FA06: FE 00 18   INC $1800,X         ; 
FA09: 18         CLC                 ; 
FA0A: 18         CLC                 ; 
FA0B: 18         CLC                 ; 
FA0C: 08         PHP                 ; 
FA0D: 08         PHP                 ; 
FA0E: 08         PHP                 ; 
FA0F: 00         BRK                 ; 
FA10: FE C0 C0   INC $C0C0,X         ; 
FA13: FE 02 82   INC $8202,X         ; 
FA16: FE 00 FE   INC $FE00,X         ; 
FA19: 86 06      STX <$06            ;{-2_COLUP0} 
FA1B: 7E 02 82   ROR $8202,X         ; 
FA1E: FE 00 06   INC $0600,X         ; 
FA21: 06 FE      ASL <$FE            ; 
FA23: 82 
FA24: 82 
FA25: 80 
FA26: 80 
FA27: 00         BRK                 ; 
FA28: FE 86 06   INC $0686,X         ; 
FA2B: FE 80 82   INC $8280,X         ; 
FA2E: FE 00 FE   INC $FE00,X         ; 
FA31: 86 86      STX <$86            ; 
FA33: FE 80 88   INC $8880,X         ; 
FA36: F8         SED                 ; 
FA37: 00         BRK                 ; 
FA38: 06 06      ASL <$06            ; 
FA3A: 06 06      ASL <$06            ; 
FA3C: 02 
FA3D: 02 
FA3E: FE 00 FE   INC $FE00,X         ; 
FA41: 82 
FA42: 82 
FA43: FE 44 44   INC $4444,X         ; 
FA46: 7C 
FA47: 00         BRK                 ; 
FA48: 06 06      ASL <$06            ; 
FA4A: 06 FE      ASL <$FE            ; 
FA4C: 82 
FA4D: 82 
FA4E: FE 00 00   INC $0000,X         ; 
FA51: 00         BRK                 ; 
FA52: 00         BRK                 ; 
FA53: 00         BRK                 ; 
FA54: 00         BRK                 ; 
FA55: 00         BRK                 ; 
FA56: 00         BRK                 ; 
FA57: 00         BRK                 ; 
FA58: 07 
FA59: 01 57      ORA ($57,X)         ; 
FA5B: 54 
FA5C: 77 
FA5D: 50 50      BVC $FAAF           ; 
FA5F: 00         BRK                 ; 
FA60: 07 
FA61: 55 71      EOR $71,X           ; 
FA63: 73 
FA64: 51 55      EOR ($55),Y         ; 
FA66: 57 
FA67: 00         BRK                 ; 
FA68: 10 38      BPL $FAA2           ; 
FA6A: 18         CLC                 ; 
FA6B: 30 7C      BMI $FAE9           ; 
FA6D: D8         CLD                 ; 
FA6E: 38         SEC                 ; 
FA6F: 38         SEC                 ; 
FA70: EC 82 84   CPX $8482           ; 
FA73: 10 38      BPL $FAAD           ; 
FA75: 18         CLC                 ; 
FA76: 30 78      BMI $FAF0           ; 
FA78: 5C 
FA79: 38         SEC                 ; 
FA7A: 38         SEC                 ; 
FA7B: 6C 60 06   JMP ($0660)         ; 
FA7E: 00         BRK                 ; 
FA7F: 38         SEC                 ; 
FA80: 38         SEC                 ; 
FA81: 00         BRK                 ; 
FA82: 78         SEI                 ; 
FA83: 38         SEC                 ; 
FA84: 78         SEI                 ; 
FA85: 18         CLC                 ; 
FA86: 38         SEC                 ; 
FA87: 20 38 00   JSR $0038           ; 
FA8A: 38         SEC                 ; 
FA8B: 38         SEC                 ; 
FA8C: 00         BRK                 ; 
FA8D: 38         SEC                 ; 
FA8E: 38         SEC                 ; 
FA8F: 38         SEC                 ; 
FA90: 18         CLC                 ; 
FA91: 30 78      BMI $FB0B           ; 
FA93: 00         BRK                 ; 
FA94: 10 38      BPL $FACE           ; 
FA96: 18         CLC                 ; 
FA97: 30 38      BMI $FAD1           ; 
FA99: 78         SEI                 ; 
FA9A: 38         SEC                 ; 
FA9B: 38         SEC                 ; 
FA9C: 68         PLA                 ; 
FA9D: CC 00 10   CPY $1000           ; 
FAA0: 38         SEC                 ; 
FAA1: 18         CLC                 ; 
FAA2: 30 78      BMI $FB1C           ; 
FAA4: DC 
FAA5: 38         SEC                 ; 
FAA6: 18         CLC                 ; 
FAA7: 68         PLA                 ; 
FAA8: CC 00 00   CPY $0000           ; 
FAAB: 48         PHA                 ; 
FAAC: 3A 
FAAD: 3A 
FAAE: 3A 
FAAF: 9A         TXS                 ; 
FAB0: 9A         TXS                 ; 
FAB1: 9A         TXS                 ; 
FAB2: DE DE 38   DEC $38DE,X         ; 
FAB5: 38         SEC                 ; 
FAB6: 00         BRK                 ; 
FAB7: 78         SEI                 ; 
FAB8: 5C 
FAB9: B8         CLV                 ; 
FABA: 38         SEC                 ; 
FABB: 68         PLA                 ; 
FABC: CC 86 00   CPY $0086           ; 
FABF: 38         SEC                 ; 
FAC0: 38         SEC                 ; 
FAC1: 00         BRK                 ; 
FAC2: 78         SEI                 ; 
FAC3: 5C 
FAC4: 78         SEI                 ; 
FAC5: 18         CLC                 ; 
FAC6: 78         SEI                 ; 
FAC7: 60         RTS                 ; 
FAC8: 06 00      ASL <$00            ; 
FACA: 10 38      BPL $FB04           ; 
FACC: 18         CLC                 ; 
FACD: 38         SEC                 ; 
FACE: 78         SEI                 ; 
FACF: 78         SEI                 ; 
FAD0: 38         SEC                 ; 
FAD1: 38         SEC                 ; 
FAD2: 28         PLP                 ; 
FAD3: 38         SEC                 ; 
FAD4: 00         BRK                 ; 
FAD5: 10 38      BPL $FB0F           ; 
FAD7: 18         CLC                 ; 
FAD8: 30 38      BMI $FB12           ; 
FADA: 30 38      BMI $FB14           ; 
FADC: 18         CLC                 ; 
FADD: 30 60      BMI $FB3F           ; 
FADF: 00         BRK                 ; 
FAE0: 38         SEC                 ; 
FAE1: 38         SEC                 ; 
FAE2: 00         BRK                 ; 
FAE3: 38         SEC                 ; 
FAE4: 78         SEI                 ; 
FAE5: 38         SEC                 ; 
FAE6: 18         CLC                 ; 
FAE7: 28         PLP                 ; 
FAE8: 0C 
FAE9: C0 00      CPY #$00            ; 
FAEB: 38         SEC                 ; 
FAEC: 38         SEC                 ; 
FAED: 00         BRK                 ; 
FAEE: 78         SEI                 ; 
FAEF: 5C 
FAF0: B8         CLV                 ; 
FAF1: 18         CLC                 ; 
FAF2: 30 CC      BMI $FAC0           ; 
FAF4: CC 00 48   CPY $4800           ; 
FAF7: 34 
FAF8: 34 
FAF9: 34 
FAFA: 9A         TXS                 ; 
FAFB: 9A         TXS                 ; 
FAFC: 9A         TXS                 ; 
FAFD: 9A         TXS                 ; 
FAFE: DE DE 00   DEC $00DE,X         ; 
FB01: 00         BRK                 ; 
FB02: 00         BRK                 ; 
FB03: 00         BRK                 ; 
FB04: 00         BRK                 ; 
FB05: 00         BRK                 ; 
FB06: 00         BRK                 ; 
FB07: 00         BRK                 ; 
FB08: 00         BRK                 ; 
FB09: 00         BRK                 ; 
FB0A: 00         BRK                 ; 
FB0B: 01 03      ORA ($03,X)         ; 
FB0D: 07 
FB0E: 0F 
FB0F: 1F 
FB10: 1F 
FB11: 0F 
FB12: 07 
FB13: 03 
FB14: 01 00      ORA ($00,X)         ; 
FB16: 00         BRK                 ; 
FB17: 00         BRK                 ; 
FB18: 00         BRK                 ; 
FB19: 00         BRK                 ; 
FB1A: 00         BRK                 ; 
FB1B: 00         BRK                 ; 
FB1C: 00         BRK                 ; 
FB1D: 00         BRK                 ; 
FB1E: 00         BRK                 ; 
FB1F: 00         BRK                 ; 
FB20: 00         BRK                 ; 
FB21: 00         BRK                 ; 
FB22: 00         BRK                 ; 
FB23: 00         BRK                 ; 
FB24: 00         BRK                 ; 
FB25: 00         BRK                 ; 
FB26: 00         BRK                 ; 
FB27: 00         BRK                 ; 
FB28: 00         BRK                 ; 
FB29: 00         BRK                 ; 
FB2A: 00         BRK                 ; 
FB2B: 01 03      ORA ($03,X)         ; 
FB2D: 07 
FB2E: 0F 
FB2F: 1F 
FB30: 1F 
FB31: 0F 
FB32: 07 
FB33: 03 
FB34: 01 00      ORA ($00,X)         ; 
FB36: 00         BRK                 ; 
FB37: 00         BRK                 ; 
FB38: 00         BRK                 ; 
FB39: 00         BRK                 ; 
FB3A: 00         BRK                 ; 
FB3B: 00         BRK                 ; 
FB3C: 00         BRK                 ; 
FB3D: 00         BRK                 ; 
FB3E: 00         BRK                 ; 
FB3F: 00         BRK                 ; 
FB40: C0 F0      CPY #$F0            ; 
FB42: F8         SED                 ; 
FB43: F8         SED                 ; 
FB44: F8         SED                 ; 
FB45: E0 80      CPX #$80            ; 
FB47: 00         BRK                 ; 
FB48: 00         BRK                 ; 
FB49: 00         BRK                 ; 
FB4A: 00         BRK                 ; 
FB4B: 00         BRK                 ; 
FB4C: 00         BRK                 ; 
FB4D: 00         BRK                 ; 
FB4E: 00         BRK                 ; 
FB4F: 00         BRK                 ; 
FB50: 00         BRK                 ; 
FB51: 00         BRK                 ; 
FB52: 00         BRK                 ; 
FB53: 00         BRK                 ; 
FB54: 01 03      ORA ($03,X)         ; 
FB56: 07 
FB57: 0F 
FB58: 0F 
FB59: 07 
FB5A: 03 
FB5B: 01 00      ORA ($00,X)         ; 
FB5D: 00         BRK                 ; 
FB5E: 00         BRK                 ; 
FB5F: 00         BRK                 ; 
FB60: 00         BRK                 ; 
FB61: 00         BRK                 ; 
FB62: 00         BRK                 ; 
FB63: 00         BRK                 ; 
FB64: 00         BRK                 ; 
FB65: 00         BRK                 ; 
FB66: 00         BRK                 ; 
FB67: 00         BRK                 ; 
FB68: 00         BRK                 ; 
FB69: 80 
FB6A: E0 F8      CPX #$F8            ; 
FB6C: F8         SED                 ; 
FB6D: F8         SED                 ; 
FB6E: F0 C0      BEQ $FB30           ; 
FB70: 00         BRK                 ; 
FB71: 00         BRK                 ; 
FB72: 00         BRK                 ; 
FB73: 00         BRK                 ; 
FB74: 00         BRK                 ; 
FB75: 00         BRK                 ; 
FB76: 00         BRK                 ; 
FB77: 00         BRK                 ; 
FB78: 00         BRK                 ; 
FB79: 00         BRK                 ; 
FB7A: 00         BRK                 ; 
FB7B: 00         BRK                 ; 
FB7C: 00         BRK                 ; 
FB7D: 00         BRK                 ; 
FB7E: 00         BRK                 ; 
FB7F: 00         BRK                 ; 
FB80: 00         BRK                 ; 
FB81: 00         BRK                 ; 
FB82: 01 03      ORA ($03,X)         ; 
FB84: 07 
FB85: 0F 
FB86: 07 
FB87: 03 
FB88: 01 00      ORA ($00,X)         ; 
FB8A: 00         BRK                 ; 
FB8B: 00         BRK                 ; 
FB8C: 00         BRK                 ; 
FB8D: 00         BRK                 ; 
FB8E: 00         BRK                 ; 
FB8F: 00         BRK                 ; 
FB90: 00         BRK                 ; 
FB91: 00         BRK                 ; 
FB92: 00         BRK                 ; 
FB93: 00         BRK                 ; 
FB94: 00         BRK                 ; 
FB95: 00         BRK                 ; 
FB96: 00         BRK                 ; 
FB97: 00         BRK                 ; 
FB98: 00         BRK                 ; 
FB99: 00         BRK                 ; 
FB9A: 00         BRK                 ; 
FB9B: 01 07      ORA ($07,X)         ; 
FB9D: 0F 
FB9E: 07 
FB9F: 01 00      ORA ($00,X)         ; 
FBA1: 00         BRK                 ; 
FBA2: 00         BRK                 ; 
FBA3: 00         BRK                 ; 
FBA4: 00         BRK                 ; 
FBA5: 00         BRK                 ; 
FBA6: 00         BRK                 ; 
FBA7: 00         BRK                 ; 
FBA8: 00         BRK                 ; 
FBA9: 00         BRK                 ; 
FBAA: 00         BRK                 ; 
FBAB: 00         BRK                 ; 
FBAC: 00         BRK                 ; 
FBAD: 00         BRK                 ; 
FBAE: 00         BRK                 ; 
FBAF: 00         BRK                 ; 
FBB0: 0F 
FBB1: 0F 
FBB2: 07 
FBB3: 03 
FBB4: 01 00      ORA ($00,X)         ; 
FBB6: 01 03      ORA ($03,X)         ; 
FBB8: 07 
FBB9: 0F 
FBBA: 0F 
FBBB: 00         BRK                 ; 
FBBC: 00         BRK                 ; 
FBBD: 00         BRK                 ; 
FBBE: 00         BRK                 ; 
FBBF: 00         BRK                 ; 
FBC0: 00         BRK                 ; 
FBC1: 00         BRK                 ; 
FBC2: 00         BRK                 ; 
FBC3: 00         BRK                 ; 
FBC4: 00         BRK                 ; 
FBC5: 00         BRK                 ; 
FBC6: 00         BRK                 ; 
FBC7: 00         BRK                 ; 
FBC8: 00         BRK                 ; 
FBC9: 00         BRK                 ; 
FBCA: 00         BRK                 ; 
FBCB: 00         BRK                 ; 
FBCC: 03 
FBCD: 07 
FBCE: 03 
FBCF: 00         BRK                 ; 
FBD0: 00         BRK                 ; 
FBD1: 00         BRK                 ; 
FBD2: 00         BRK                 ; 
FBD3: 00         BRK                 ; 
FBD4: 00         BRK                 ; 
FBD5: 00         BRK                 ; 
FBD6: 00         BRK                 ; 
FBD7: 00         BRK                 ; 
FBD8: 00         BRK                 ; 
FBD9: 00         BRK                 ; 
FBDA: 00         BRK                 ; 
FBDB: 00         BRK                 ; 
FBDC: 00         BRK                 ; 
FBDD: 00         BRK                 ; 
FBDE: 00         BRK                 ; 
FBDF: 00         BRK                 ; 
FBE0: 3C 
FBE1: 20 3C 20   JSR $203C           ; 
FBE4: 3C 
FBE5: 18         CLC                 ; 
FBE6: DB 
FBE7: FF 
FBE8: E0 DD      CPX #$DD            ; 
FBEA: DB 
FBEB: D7 
FBEC: 24 18      BIT <$18            ; 
FBEE: 24 24      BIT <$24            ; 
FBF0: 7E 5A DB   ROR $DB5A,X         ; 
FBF3: 3C 
FBF4: 24 99      BIT <$99            ; 
FBF6: A5 E7      LDA <$E7            ; 
FBF8: 18         CLC                 ; 
FBF9: 18         CLC                 ; 
FBFA: 18         CLC                 ; 
FBFB: 3C 
FBFC: 00         BRK                 ; 
FBFD: 00         BRK                 ; 
FBFE: 00         BRK                 ; 
FBFF: 00         BRK                 ; 
FC00: 00         BRK                 ; 
FC01: 00         BRK                 ; 
FC02: 00         BRK                 ; 
FC03: 00         BRK                 ; 
FC04: 00         BRK                 ; 
FC05: 00         BRK                 ; 
FC06: 00         BRK                 ; 
FC07: 00         BRK                 ; 
FC08: 18         CLC                 ; 
FC09: 30 60      BMI $FC6B           ; 
FC0B: FF 
FC0C: FF 
FC0D: 60         RTS                 ; 
FC0E: 30 18      BMI $FC28           ; 
FC10: 18         CLC                 ; 
FC11: 0C 
FC12: 06 FF      ASL <$FF            ; 
FC14: FF 
FC15: 06 0C      ASL <$0C            ; 
FC17: 18         CLC                 ; 
FC18: 18         CLC                 ; 
FC19: 18         CLC                 ; 
FC1A: 18         CLC                 ; 
FC1B: 18         CLC                 ; 
FC1C: DB 
FC1D: 7E 3C 18   ROR $183C,X         ; 
FC20: 18         CLC                 ; 
FC21: 3C 
FC22: 7E DB 18   ROR $18DB,X         ; 
FC25: 18         CLC                 ; 
FC26: 18         CLC                 ; 
FC27: 18         CLC                 ; 
FC28: 38         SEC                 ; 
FC29: 00         BRK                 ; 
FC2A: 38         SEC                 ; 
FC2B: 1C 
FC2C: 0E 66 7E   ASL $7E66           ; 
FC2F: 3C 
FC30: 00         BRK                 ; 
FC31: 7E C3 99   ROR $99C3,X         ; 
FC34: 99 C3 66   STA $66C3,Y         ; 
FC37: 3C 
FC38: 7F 
FC39: 7F 
FC3A: 2A         ROL A               ; 
FC3B: 2A         ROL A               ; 
FC3C: 2A         ROL A               ; 
FC3D: 2A         ROL A               ; 
FC3E: 3E 7F 02   ROL $027F,X         ; 
FC41: 74 
FC42: C0 F7      CPY #$F7            ; 
FC44: D0 F4      BNE $FC3A           ; 
FC46: 62 
FC47: 01 42      ORA ($42,X)         ; 
FC49: 24 7E      BIT <$7E            ; 
FC4B: BD FF 5A   LDA $5AFF,X         ; 
FC4E: 3C 
FC4F: 24 00      BIT <$00            ; 
FC51: 7F 
FC52: 49 5D      EOR #$5D            ; 
FC54: 77 
FC55: 5D 49 7F   EOR $7F49,X         ; 
FC58: FF 
FC59: 00         BRK                 ; 
FC5A: 18         CLC                 ; 
FC5B: 18         CLC                 ; 
FC5C: 18         CLC                 ; 
FC5D: 7E 3C 18   ROR $183C,X         ; 
FC60: 00         BRK                 ; 
FC61: 3E 63 41   ROL $4163,X         ; 
FC64: 08         PHP                 ; 
FC65: 00         BRK                 ; 
FC66: 22 
FC67: 22 
FC68: 00         BRK                 ; 
FC69: 00         BRK                 ; 
FC6A: 00         BRK                 ; 
FC6B: 00         BRK                 ; 
FC6C: 00         BRK                 ; 
FC6D: 10 30      BPL $FC9F           ; 
FC6F: 70 00      BVS $FC71           ; 
FC71: 00         BRK                 ; 
FC72: 00         BRK                 ; 
FC73: 00         BRK                 ; 
FC74: E0 D0      CPX #$D0            ; 
FC76: B0 70      BCS $FCE8           ; 
FC78: 00         BRK                 ; 
FC79: 80 
FC7A: C0 E0      CPY #$E0            ; 
FC7C: E0 D0      CPX #$D0            ; 
FC7E: B0 70      BCS $FCF0           ; 
FC80: 70 B0      BVS $FC32           ; 
FC82: D0 E0      BNE $FC64           ; 
FC84: E0 D0      CPX #$D0            ; 
FC86: B0 70      BCS $FCF8           ; 
FC88: 7E BC D8   ROR $D8BC,X         ; 
FC8B: E0 E0      CPX #$E0            ; 
FC8D: D0 B0      BNE $FC3F           ; 
FC8F: 70 7E      BVS $FD0F           ; 
FC91: BD DB E7   LDA $E7DB,X         ; 
FC94: E0 D0      CPX #$D0            ; 
FC96: B0 70      BCS $FD08           ; 
FC98: 7E BD DB   ROR $DBBD,X         ; 
FC9B: E7 
FC9C: E7 
FC9D: D3 
FC9E: B1 70      LDA ($70),Y         ; 
FCA0: 7E BD DB   ROR $DBBD,X         ; 
FCA3: E7 
FCA4: E7 
FCA5: DB 
FCA6: BD 7E 00   LDA $007E,X         ; 
FCA9: 3C 
FCAA: 7E C3 7E   ROR $7EC3,X         ; 
FCAD: 3C 
FCAE: 18         CLC                 ; 
FCAF: 00         BRK                 ; 
FCB0: 79 85 B5   ADC $B585,Y         ; 
FCB3: A5 B5      LDA <$B5            ; 
FCB5: 85 79      STA <$79            ; 
FCB7: 00         BRK                 ; 
FCB8: 17 
FCB9: 15 15      ORA $15,X           ; 
FCBB: 77 
FCBC: 55 55      EOR $55,X           ; 
FCBE: 77 
FCBF: 00         BRK                 ; 
FCC0: 71 41      ADC ($41),Y         ; 
FCC2: 41 71      EOR ($71,X)         ; 
FCC4: 11 51      ORA ($51),Y         ; 
FCC6: 70 00      BVS $FCC8           ; 
FCC8: 49 49      EOR #$49            ; 
FCCA: 49 C9      EOR #$C9            ; 
FCCC: 49 49      EOR #$49            ; 
FCCE: BE 00 55   LDX $5500,Y         ; 
FCD1: 55 55      EOR $55,X           ; 
FCD3: D9 55 55   CMP $5555,Y         ; 
FCD6: 99 00 1E   STA $1E00,Y         ; 
FCD9: 1B 
FCDA: 7B 
FCDB: DB 
FCDC: DB 
FCDD: 1E 18 18   ASL $1818,X         ; 
FCE0: A2 00      LDX #$00            ; 
FCE2: A5 EA      LDA <$EA            ; 
FCE4: C5 80      CMP <$80            ; 
FCE6: D0 13      BNE $FCFB           ; 
FCE8: C5 DD      CMP <$DD            ; 
FCEA: D0 0F      BNE $FCFB           ; 
FCEC: C5 A1      CMP <$A1            ; 
FCEE: D0 0B      BNE $FCFB           ; 
FCF0: C9 01      CMP #$01            ; 
FCF2: D0 07      BNE $FCFB           ; 
FCF4: A5 D2      LDA <$D2            ; 
FCF6: C9 20      CMP #$20            ; 
FCF8: B0 01      BCS $FCFB           ; 
FCFA: CA         DEX                 ; 
FCFB: 86 F3      STX <$F3            ; 
FCFD: 60         RTS                 ; 
FCFE: 00         BRK                 ; 
FCFF: 00         BRK                 ; 
FD00: 00         BRK                 ; 
FD01: 00         BRK                 ; 
FD02: 00         BRK                 ; 
FD03: 00         BRK                 ; 
FD04: 00         BRK                 ; 
FD05: 00         BRK                 ; 
FD06: 00         BRK                 ; 
FD07: 80 
FD08: 80 
FD09: 80 
FD0A: 80 
FD0B: 80 
FD0C: C0 C0      CPY #$C0            ; 
FD0E: C0 C0      CPY #$C0            ; 
FD10: C0 C0      CPY #$C0            ; 
FD12: C0 C0      CPY #$C0            ; 
FD14: C0 C0      CPY #$C0            ; 
FD16: C0 C0      CPY #$C0            ; 
FD18: C0 C0      CPY #$C0            ; 
FD1A: C0 E0      CPY #$E0            ; 
FD1C: E0 E0      CPX #$E0            ; 
FD1E: E0 E0      CPX #$E0            ; 
FD20: E0 E0      CPX #$E0            ; 
FD22: E0 E0      CPX #$E0            ; 
FD24: E0 E0      CPX #$E0            ; 
FD26: E0 F0      CPX #$F0            ; 
FD28: F0 F0      BEQ $FD1A           ; 
FD2A: F0 F0      BEQ $FD1C           ; 
FD2C: F0 F0      BEQ $FD1E           ; 
FD2E: F0 F8      BEQ $FD28           ; 
FD30: F8         SED                 ; 
FD31: F8         SED                 ; 
FD32: F8         SED                 ; 
FD33: FC 
FD34: FC 
FD35: FE FF FF   INC $FFFF,X         ; 
FD38: FF 
FD39: FF 
FD3A: FF 
FD3B: FF 
FD3C: FF 
FD3D: FF 
FD3E: FF 
FD3F: FF 
FD40: 00         BRK                 ; 
FD41: 00         BRK                 ; 
FD42: 00         BRK                 ; 
FD43: 00         BRK                 ; 
FD44: 00         BRK                 ; 
FD45: 00         BRK                 ; 
FD46: 00         BRK                 ; 
FD47: 00         BRK                 ; 
FD48: 00         BRK                 ; 
FD49: 1F 
FD4A: 1F 
FD4B: 00         BRK                 ; 
FD4C: 1F 
FD4D: 1F 
FD4E: 04 
FD4F: 04 
FD50: 04 
FD51: 04 
FD52: 04 
FD53: 04 
FD54: 04 
FD55: 04 
FD56: 04 
FD57: 04 
FD58: 04 
FD59: 04 
FD5A: 0F 
FD5B: 1F 
FD5C: 3F 
FD5D: 00         BRK                 ; 
FD5E: 00         BRK                 ; 
FD5F: 00         BRK                 ; 
FD60: 00         BRK                 ; 
FD61: 00         BRK                 ; 
FD62: 00         BRK                 ; 
FD63: 00         BRK                 ; 
FD64: 00         BRK                 ; 
FD65: 00         BRK                 ; 
FD66: 00         BRK                 ; 
FD67: 80 
FD68: C0 E0      CPY #$E0            ; 
FD6A: F0 F8      BEQ $FD64           ; 
FD6C: FC 
FD6D: F4 
FD6E: F0 F0      BEQ $FD60           ; 
FD70: B0 B0      BCS $FD22           ; 
FD72: F0 B0      BEQ $FD24           ; 
FD74: B0 F0      BCS $FD66           ; 
FD76: F0 F0      BEQ $FD68           ; 
FD78: F0 00      BEQ $FD7A           ; 
FD7A: 00         BRK                 ; 
FD7B: 00         BRK                 ; 
FD7C: 00         BRK                 ; 
FD7D: 00         BRK                 ; 
FD7E: 00         BRK                 ; 
FD7F: 00         BRK                 ; 
FD80: 00         BRK                 ; 
FD81: 00         BRK                 ; 
FD82: 3F 
FD83: 3F 
FD84: 00         BRK                 ; 
FD85: 3F 
FD86: 3F 
FD87: 09 09      ORA #$09            ; 
FD89: 09 09      ORA #$09            ; 
FD8B: 09 09      ORA #$09            ; 
FD8D: 09 09      ORA #$09            ; 
FD8F: 09 09      ORA #$09            ; 
FD91: 09 09      ORA #$09            ; 
FD93: 1F 
FD94: 3F 
FD95: 7F 
FD96: 00         BRK                 ; 
FD97: 00         BRK                 ; 
FD98: 00         BRK                 ; 
FD99: 00         BRK                 ; 
FD9A: 00         BRK                 ; 
FD9B: 00         BRK                 ; 
FD9C: 00         BRK                 ; 
FD9D: 00         BRK                 ; 
FD9E: 00         BRK                 ; 
FD9F: 00         BRK                 ; 
FDA0: 00         BRK                 ; 
FDA1: 00         BRK                 ; 
FDA2: 00         BRK                 ; 
FDA3: 00         BRK                 ; 
FDA4: 00         BRK                 ; 
FDA5: 00         BRK                 ; 
FDA6: 00         BRK                 ; 
FDA7: 00         BRK                 ; 
FDA8: 00         BRK                 ; 
FDA9: 00         BRK                 ; 
FDAA: 00         BRK                 ; 
FDAB: 00         BRK                 ; 
FDAC: 00         BRK                 ; 
FDAD: 00         BRK                 ; 
FDAE: 00         BRK                 ; 
FDAF: 00         BRK                 ; 
FDB0: 00         BRK                 ; 
FDB1: 00         BRK                 ; 
FDB2: 00         BRK                 ; 
FDB3: 00         BRK                 ; 
FDB4: 00         BRK                 ; 
FDB5: 00         BRK                 ; 
FDB6: 00         BRK                 ; 
FDB7: 00         BRK                 ; 
FDB8: 00         BRK                 ; 
FDB9: 00         BRK                 ; 
FDBA: 00         BRK                 ; 
FDBB: 00         BRK                 ; 
FDBC: 00         BRK                 ; 
FDBD: 00         BRK                 ; 
FDBE: 00         BRK                 ; 
FDBF: 00         BRK                 ; 
FDC0: 00         BRK                 ; 
FDC1: 00         BRK                 ; 
FDC2: 00         BRK                 ; 
FDC3: 00         BRK                 ; 
FDC4: 00         BRK                 ; 
FDC5: 00         BRK                 ; 
FDC6: 00         BRK                 ; 
FDC7: 00         BRK                 ; 
FDC8: 00         BRK                 ; 
FDC9: 00         BRK                 ; 
FDCA: 00         BRK                 ; 
FDCB: 00         BRK                 ; 
FDCC: 00         BRK                 ; 
FDCD: 00         BRK                 ; 
FDCE: 00         BRK                 ; 
FDCF: 00         BRK                 ; 
FDD0: 00         BRK                 ; 
FDD1: FF 
FDD2: FF 
FDD3: FF 
FDD4: FF 
FDD5: FF 
FDD6: FF 
FDD7: FF 
FDD8: FF 
FDD9: C0 C0      CPY #$C0            ; 
FDDB: C0 C0      CPY #$C0            ; 
FDDD: C0 08      CPY #$08            ; 
FDDF: 00         BRK                 ; 
FDE0: 72 
FDE1: 00         BRK                 ; 
FDE2: D4 
FDE3: D4 
FDE4: D4 
FDE5: D4 
FDE6: D4 
FDE7: 84 06      STY <$06            ;{-2_COLUP0} 
FDE9: 90 80      BCC $FD6B           ; 
FDEB: 24 F2      BIT <$F2            ; 
FDED: 10 0C      BPL $FDFB           ; 
FDEF: 70 0A      BVS $FDFB           ; 
FDF1: A6 9B      LDX <$9B            ; 
FDF3: 10 04      BPL $FDF9           ; 
FDF5: E0 E0      CPX #$E0            ; 
FDF7: 90 02      BCC $FDFB           ; 
FDF9: C6 9B      DEC <$9B            ; 
FDFB: 60         RTS                 ; 
FDFC: 00         BRK                 ; 
FDFD: 00         BRK                 ; 
FDFE: 00         BRK                 ; 
FDFF: 00         BRK                 ; 
FE00: 1A 
FE01: 00         BRK                 ; 
FE02: 1C 
FE03: 18         CLC                 ; 
FE04: 3C 
FE05: 7C 
FE06: 5E 16 3C   LSR $3C16,X         ; 
FE09: 7E FE FE   ROR $FEFE,X         ; 
FE0C: 00         BRK                 ; 
FE0D: E7 
FE0E: 1A 
FE0F: 00         BRK                 ; 
FE10: 1C 
FE11: 18         CLC                 ; 
FE12: 38         SEC                 ; 
FE13: 7C 
FE14: 5C 
FE15: 2E 36 3C   ROL $3C36           ; 
FE18: 7E 7E 00   ROR $007E,X         ; 
FE1B: 7C 
FE1C: 1A 
FE1D: 00         BRK                 ; 
FE1E: 1C 
FE1F: 18         CLC                 ; 
FE20: 38         SEC                 ; 
FE21: 3C 
FE22: 2C 2C 3C   BIT $3C2C           ; 
FE25: 3C 
FE26: 3C 
FE27: 3C 
FE28: 00         BRK                 ; 
FE29: 3C 
FE2A: 1A 
FE2B: 00         BRK                 ; 
FE2C: 1C 
FE2D: 18         CLC                 ; 
FE2E: 38         SEC                 ; 
FE2F: 7C 
FE30: 7C 
FE31: 6C 38 3C   JMP ($3C38)         ; 
FE34: 3C 
FE35: 3C 
FE36: 00         BRK                 ; 
FE37: 76 1A      ROR <$1A,X          ; 
FE39: 00         BRK                 ; 
FE3A: 1C 
FE3B: 18         CLC                 ; 
FE3C: 3C 
FE3D: 7C 
FE3E: 5E 36 7C   LSR $7C36,X         ; 
FE41: 7C 
FE42: 7C 
FE43: 7C 
FE44: 00         BRK                 ; 
FE45: EE 3E 3C   INC $3C3E           ; 
FE48: 1C 
FE49: 38         SEC                 ; 
FE4A: 7C 
FE4B: 7C 
FE4C: 2E 3A 3E   ROL $3E3A           ; 
FE4F: 7E FE FE   ROR $FEFE,X         ; 
FE52: E6 C7      INC <$C7            ; 
FE54: 3E 3C 1C   ROL $1C3C,X         ; 
FE57: 38         SEC                 ; 
FE58: 7C 
FE59: 7C 
FE5A: 7C 
FE5B: 3E 3A 7E   ROL $7E3A,X         ; 
FE5E: 7E 7E 70   ROR $707E,X         ; 
FE61: 1C 
FE62: 3E 3C 1C   ROL $1C3C,X         ; 
FE65: 18         CLC                 ; 
FE66: 38         SEC                 ; 
FE67: 3C 
FE68: 3C 
FE69: 3C 
FE6A: 34 
FE6B: 38         SEC                 ; 
FE6C: 3C 
FE6D: 3C 
FE6E: 3C 
FE6F: 38         SEC                 ; 
FE70: 3E 3C 1C   ROL $1C3C,X         ; 
FE73: 18         CLC                 ; 
FE74: 7C 
FE75: 7C 
FE76: 5C 
FE77: 34 
FE78: 3C 
FE79: 3C 
FE7A: 3C 
FE7B: 3C 
FE7C: 76 70      ROR <$70,X          ; 
FE7E: 3E 3C 1C   ROL $1C3C,X         ; 
FE81: 38         SEC                 ; 
FE82: 7C 
FE83: 7C 
FE84: 6E 7A 7C   ROR $7C7A           ; 
FE87: 7C 
FE88: 7C 
FE89: 7C 
FE8A: EC CE 98   CPX $98CE           ; 
FE8D: 46 46      LSR <$46            ; 
FE8F: 46 0E      LSR <$0E            ; 
FE91: 0C 
FE92: 0A         ASL A               ; 
FE93: 0A         ASL A               ; 
FE94: 0A         ASL A               ; 
FE95: 0A         ASL A               ; 
FE96: 0A         ASL A               ; 
FE97: 08         PHP                 ; 
FE98: 00         BRK                 ; 
FE99: 48         PHA                 ; 
FE9A: 98         TYA                 ; 
FE9B: 46 46      LSR <$46            ; 
FE9D: 0E 0C 0A   ASL $0A0C           ; 
FEA0: 0A         ASL A               ; 
FEA1: 0A         ASL A               ; 
FEA2: 0A         ASL A               ; 
FEA3: 0A         ASL A               ; 
FEA4: 08         PHP                 ; 
FEA5: 08         PHP                 ; 
FEA6: 48         PHA                 ; 
FEA7: 48         PHA                 ; 
FEA8: 90 64      BCC $FF0E           ; 
FEAA: 3F 
FEAB: 64 
FEAC: 90 C8      BCC $FE76           ; 
FEAE: 32 
FEAF: 32 
FEB0: C8         INY                 ; 
FEB1: 00         BRK                 ; 
FEB2: 1F 
FEB3: 54 
FEB4: 54 
FEB5: 15 7C      ORA $7C,X           ; 
FEB7: 3E A8 2A   ROL $2AA8,X         ; 
FEBA: 2A         ROL A               ; 
FEBB: F8         SED                 ; 
FEBC: 3C 
FEBD: C0 AA      CPY #$AA            ; 
FEBF: 0E E0 60   ASL $60E0           ; 
FEC2: FE FE 38   INC $38FE,X         ; 
FEC5: FF 
FEC6: FE FA F6   INC $F6FA,X         ; 
FEC9: F4 
FECA: F2 
FECB: FC 
FECC: F8         SED                 ; 
FECD: E6 E4      INC <$E4            ; 
FECF: E2 
FED0: 18         CLC                 ; 
FED1: 3C 
FED2: 7E FF 42   ROR $42FF,X         ; 
FED5: C3 
FED6: 42 
FED7: C3 
FED8: 42 
FED9: C3 
FEDA: 42 
FEDB: C3 
FEDC: 7E 5A 42   ROR $425A,X         ; 
FEDF: E7 
FEE0: 58         CLI                 ; 
FEE1: 56 54      LSR $54,X           ; 
FEE3: 52 
FEE4: 54 
FEE5: 56 58      LSR $58,X           ; 
FEE7: 56 54      LSR $54,X           ; 
FEE9: 52 
FEEA: 54 
FEEB: 56 58      LSR $58,X           ; 
FEED: 56 54      LSR $54,X           ; 
FEEF: 52 
FEF0: 54 
FEF1: 56 58      LSR $58,X           ; 
FEF3: 56 54      LSR $54,X           ; 
FEF5: 52 
FEF6: 00         BRK                 ; 
FEF7: 00         BRK                 ; 
FEF8: 00         BRK                 ; 
FEF9: 00         BRK                 ; 
FEFA: 00         BRK                 ; 
FEFB: 00         BRK                 ; 
FEFC: 00         BRK                 ; 
FEFD: 00         BRK                 ; 
FEFE: 00         BRK                 ; 
FEFF: 00         BRK                 ; 
FF00: 00         BRK                 ; 
FF01: 00         BRK                 ; 
FF02: 00         BRK                 ; 
FF03: 00         BRK                 ; 
FF04: 00         BRK                 ; 
FF05: 00         BRK                 ; 
FF06: 00         BRK                 ; 
FF07: 80 
FF08: C0 E0      CPY #$E0            ; 
FF0A: F0 F8      BEQ $FF04           ; 
FF0C: FC 
FF0D: F4 
FF0E: F0 F0      BEQ $FF00           ; 
FF10: B0 B0      BCS $FEC2           ; 
FF12: F0 B0      BEQ $FEC4           ; 
FF14: B0 F0      BCS $FF06           ; 
FF16: F0 F0      BEQ $FF08           ; 
FF18: F0 00      BEQ $FF1A           ; 
FF1A: 00         BRK                 ; 
FF1B: 00         BRK                 ; 
FF1C: 00         BRK                 ; 
FF1D: 00         BRK                 ; 
FF1E: 00         BRK                 ; 
FF1F: 00         BRK                 ; 
FF20: 00         BRK                 ; 
FF21: 00         BRK                 ; 
FF22: 00         BRK                 ; 
FF23: 00         BRK                 ; 
FF24: 00         BRK                 ; 
FF25: 00         BRK                 ; 
FF26: 00         BRK                 ; 
FF27: 00         BRK                 ; 
FF28: 00         BRK                 ; 
FF29: 00         BRK                 ; 
FF2A: 00         BRK                 ; 
FF2B: 00         BRK                 ; 
FF2C: 00         BRK                 ; 
FF2D: 00         BRK                 ; 
FF2E: 00         BRK                 ; 
FF2F: 00         BRK                 ; 
FF30: 00         BRK                 ; 
FF31: 00         BRK                 ; 
FF32: 00         BRK                 ; 
FF33: 00         BRK                 ; 
FF34: 00         BRK                 ; 
FF35: 00         BRK                 ; 
FF36: 00         BRK                 ; 
FF37: 00         BRK                 ; 
FF38: 00         BRK                 ; 
FF39: 00         BRK                 ; 
FF3A: 00         BRK                 ; 
FF3B: 00         BRK                 ; 
FF3C: 00         BRK                 ; 
FF3D: 00         BRK                 ; 
FF3E: 00         BRK                 ; 
FF3F: 00         BRK                 ; 
FF40: 00         BRK                 ; 
FF41: 00         BRK                 ; 
FF42: 00         BRK                 ; 
FF43: 00         BRK                 ; 
FF44: 00         BRK                 ; 
FF45: 00         BRK                 ; 
FF46: 00         BRK                 ; 
FF47: 00         BRK                 ; 
FF48: 00         BRK                 ; 
FF49: 00         BRK                 ; 
FF4A: 00         BRK                 ; 
FF4B: 00         BRK                 ; 
FF4C: 00         BRK                 ; 
FF4D: 00         BRK                 ; 
FF4E: 00         BRK                 ; 
FF4F: 00         BRK                 ; 
FF50: 00         BRK                 ; 
FF51: 00         BRK                 ; 
FF52: 00         BRK                 ; 
FF53: 00         BRK                 ; 
FF54: 00         BRK                 ; 
FF55: 00         BRK                 ; 
FF56: 00         BRK                 ; 
FF57: 00         BRK                 ; 
FF58: 00         BRK                 ; 
FF59: 00         BRK                 ; 
FF5A: 1C 
FF5B: 3E 3C 1C   ROL $1C3C,X         ; 
FF5E: 6C 78 6E   JMP ($6E78)         ; 
FF61: 7E 3E 36   ROR $363E,X         ; 
FF64: 7E FE FE   ROR $FEFE,X         ; 
FF67: E7 
FF68: 38         SEC                 ; 
FF69: 7C 
FF6A: 78         SEI                 ; 
FF6B: 38         SEC                 ; 
FF6C: 58         CLI                 ; 
FF6D: 70 7C      BVS $FFEB           ; 
FF6F: 6C 7E 2E   JMP ($2E7E)         ; 
FF72: 3E 3E 3E   ROL $3E3E,X         ; 
FF75: 3E 38 7C   ROL $7C38,X         ; 
FF78: 78         SEI                 ; 
FF79: 38         SEC                 ; 
FF7A: 58         CLI                 ; 
FF7B: F0 FC      BEQ $FF79           ; 
FF7D: DC 
FF7E: FC 
FF7F: 7C 
FF80: 3C 
FF81: 3C 
FF82: 3C 
FF83: 3C 
FF84: 1C 
FF85: 3E 3C 1C   ROL $1C3C,X         ; 
FF88: 2C 78 7E   BIT $7E78           ; 
FF8B: 6E 7E 36   ROR $367E           ; 
FF8E: 7E 7E 7E   ROR $7E7E,X         ; 
FF91: 6E 1C 1C   ROR $1C1C           ; 
FF94: 1C 
FF95: 18         CLC                 ; 
FF96: 76 7E      ROR <$7E,X          ; 
FF98: 76 7C      ROR <$7C,X          ; 
FF9A: 3A 
FF9B: 7E FE FE   ROR $FEFE,X         ; 
FF9E: C6 E7      DEC <$E7            ; 
FFA0: 38         SEC                 ; 
FFA1: 38         SEC                 ; 
FFA2: 38         SEC                 ; 
FFA3: 30 6C      BMI $10011          ; 
FFA5: 7C 
FFA6: 6C 7C 36   JMP ($367C)         ; 
FFA9: 3E 3E 3E   ROL $3E3E,X         ; 
FFAC: 3C 
FFAD: 3E 38 38   ROL $3838,X         ; 
FFB0: 38         SEC                 ; 
FFB1: 30 EC      BMI $FF9F           ; 
FFB3: FC 
FFB4: FC 
FFB5: FC 
FFB6: FC 
FFB7: 1C 
FFB8: 3C 
FFB9: 3C 
FFBA: 38         SEC                 ; 
FFBB: 3C 
FFBC: 1C 
FFBD: 1C 
FFBE: 1C 
FFBF: 18         CLC                 ; 
FFC0: 76 7E      ROR <$7E,X          ; 
FFC2: 7E 74 7E   ROR $7E74,X         ; 
FFC5: 2E 7E 7E   ROL $7E7E           ; 
FFC8: 6C 76 28   JMP ($2876)         ; 
FFCB: 28         PLP                 ; 
FFCC: 48         PHA                 ; 
FFCD: 48         PHA                 ; 
FFCE: 2A         ROL A               ; 
FFCF: 2A         ROL A               ; 
FFD0: 2A         ROL A               ; 
FFD1: 2A         ROL A               ; 
FFD2: 28         PLP                 ; 
FFD3: 28         PLP                 ; 
FFD4: 28         PLP                 ; 
FFD5: 28         PLP                 ; 
FFD6: 26 00      ROL <$00            ; 
FFD8: 28         PLP                 ; 
FFD9: 00         BRK                 ; 
FFDA: 48         PHA                 ; 
FFDB: 2A         ROL A               ; 
FFDC: 2A         ROL A               ; 
FFDD: 2A         ROL A               ; 
FFDE: 2A         ROL A               ; 
FFDF: 2A         ROL A               ; 
FFE0: 28         PLP                 ; 
FFE1: 28         PLP                 ; 
FFE2: 28         PLP                 ; 
FFE3: 26 00      ROL <$00            ; 
FFE5: 00         BRK                 ; 
FFE6: 1C 
FFE7: 3C 
FFE8: 5E 18 3C   LSR $3C18,X         ; 
FFEB: 00         BRK                 ; 
FFEC: 18         CLC                 ; 
FFED: 3C 
FFEE: 5A 
FFEF: 3C 
FFF0: 18         CLC                 ; 
FFF1: 18         CLC                 ; 
FFF2: 3C 
FFF3: 00         BRK                 ; 
FFF4: 00         BRK                 ; 
FFF5: 00         BRK                 ; 
FFF6: 00         BRK                 ; 
FFF7: 00         BRK                 ; 
FFF8: 00         BRK                 ; 
FFF9: 00         BRK                 ; 
FFFA: 00         BRK                 ; 
```

# Vectors (Bank 1)

```code
; Interesting. These appear to be backwards (the 6502 is little-endian)
; F000 would be the correct jump (switches to Bank 0 and starts up)
FFFB: F0 00      ; NMI vector to 00F0
FFFD: F0 00      ; Reset vector to 00F0 (Only vector that is used in the Atari2600)
FFFF: F0 FF      ; IRQ/BRK vector to FF00
```
