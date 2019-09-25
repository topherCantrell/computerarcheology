![Entombed](Entombed.jpg)

# Chess

>>> cpu 6502

>>> memoryTable hard 
[Hardware Info](../Stella.md)

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

```code
B000: 4C 85 B0       JMP     $B085           

B003: 00             BRK                     
B004: 38             SEC                     
B005: 44                                  
B006: 44                                  
B007: 44                                  
B008: 44                                  
B009: 44                                  
B00A: 38             SEC                     
B00B: 00             BRK                     
B00C: 38             SEC                     
B00D: 10 10          BPL     $B01F           
B00F: 10 10          BPL     $B021           
B011: 30 10          BMI     $B023           
B013: 00             BRK                     
B014: 7C                                  
B015: 40             RTI                     
B016: 40             RTI                     
B017: 38             SEC                     
B018: 04                                  
B019: 44                                  
B01A: 38             SEC                     
B01B: 00             BRK                     
B01C: 38             SEC                     
B01D: 44                                  
B01E: 04                                  
B01F: 18             CLC                     
B020: 04                                  
B021: 44                                  
B022: 38             SEC                     
B023: 00             BRK                     
B024: 08             PHP                     
B025: 08             PHP                     
B026: 7C                                  
B027: 48             PHA                     
B028: 28             PLP                     
B029: 18             CLC                     
B02A: 08             PHP                     
B02B: 00             BRK                     
B02C: 38             SEC                     
B02D: 44                                  
B02E: 04                                  
B02F: 04                                  
B030: 78             SEI                     
B031: 40             RTI                     
B032: 7C                                  
B033: 00             BRK                     
B034: 38             SEC                     
B035: 44                                  
B036: 44                                  
B037: 78             SEI                     
B038: 40             RTI                     
B039: 20 1C 00       JSR     $001C           
B03C: 20 20 20       JSR     $2020           
B03F: 10 08          BPL     $B049           
B041: 04                                  
B042: 7C                                  
B043: 00             BRK                     
B044: 38             SEC                     
B045: 44                                  
B046: 44                                  
B047: 38             SEC                     
B048: 44                                  
B049: 44                                  
B04A: 38             SEC                     
B04B: 00             BRK                     
B04C: 70 08          BVS     $B056           
B04E: 04                                  
B04F: 3C                                  
B050: 44                                  
B051: 44                                  
B052: 38             SEC                     
B053: 00             BRK                     
B054: 00             BRK                     
B055: 00             BRK                     
B056: 00             BRK                     
B057: 00             BRK                     
B058: 00             BRK                     
B059: 00             BRK                     
B05A: 00             BRK                     
B05B: 3C                                  
B05C: 42                                  
B05D: 99 91 99       STA     $9991,Y         
B060: 42                                  
B061: 3C                                  
B062: 00             BRK                     
B063: 40             RTI                     
B064: 40             RTI                     
B065: 11 87          ORA     ($87),Y         
B067: 40             RTI                     
B068: 80                                  
B069: 0F                                  
B06A: 04                                  
B06B: 04                                  
B06C: 01 00          ORA     ($00,X)         
B06E: 03                                  
B06F: B0 03          BCS     $B074           
B071: B0 03          BCS     $B076           
B073: B0 03          BCS     $B078           
B075: B0 04          BCS     $B07B           
B077: 18             CLC                     
B078: 13                                  
B079: BE 33 01       LDX     $0133,Y         
B07C: 0C                                  
B07D: 09 62          ORA     #$62            
B07F: BF                                  
B080: 6D BF 78       ADC     $78BF           
B083: BF                                  
B084: 8A             TXA                     
```

# Start

```code
B085: 78             SEI                     
B086: D8             CLD                     
B087: A9 01          LDA     #$01            
B089: 85 F4          STA     $F4             
B08B: A2 FF          LDX     #$FF            
B08D: 9A             TXS                     
B08E: 20 94 BB       JSR     $BB94           
B091: A2 00          LDX     #$00            
B093: 86 F5          STX     $F5             
B095: AD 82 02       LDA     $0282           
B098: 30 01          BMI     $B09B           
B09A: E8             INX                     
B09B: 86 F2          STX     $F2             
B09D: 84 DD          STY     $DD             
B09F: 84 DE          STY     $DE             
B0A1: A9 25          LDA     #$25            
B0A3: 85 0A          STA     $0A             
B0A5: A2 21          LDX     #$21            
B0A7: BC 63 B0       LDY     $B063,X         
B0AA: 94 B0          STY     $B0,X           
B0AC: CA             DEX                     
B0AD: 10 F8          BPL     $B0A7           
B0AF: A9 BD          LDA     #$BD            
B0B1: 85 D9          STA     $D9             
B0B3: 20 A4 B9       JSR     $B9A4           
B0B6: A5 F4          LDA     $F4             
B0B8: D0 03          BNE     $B0BD           
B0BA: 20 C1 B9       JSR     $B9C1           
B0BD: A9 18          LDA     #$18            
B0BF: 85 08          STA     $08             
B0C1: A9 FF          LDA     #$FF            
B0C3: 85 D5          STA     $D5             
B0C5: 85 F6          STA     $F6             
B0C7: 20 16 BF       JSR     $BF16           
B0CA: AD 82 02       LDA     $0282           
B0CD: 29 01          AND     #$01            
B0CF: F0 BA          BEQ     $B08B           
B0D1: 24 37          BIT     $37             
B0D3: 10 03          BPL     $B0D8           
B0D5: 20 18 BA       JSR     $BA18           
B0D8: A5 F0          LDA     $F0             
B0DA: F0 1E          BEQ     $B0FA           
B0DC: C6 DD          DEC     $DD             
B0DE: D0 0A          BNE     $B0EA           
B0E0: E6 C4          INC     $C4             
B0E2: A5 C4          LDA     $C4             
B0E4: 85 08          STA     $08             
B0E6: 69 80          ADC     #$80            
B0E8: 85 09          STA     $09             
B0EA: A9 BE          LDA     #$BE            
B0EC: 85 D9          STA     $D9             
B0EE: 85 D5          STA     $D5             
B0F0: A9 0A          LDA     #$0A            
B0F2: 85 D8          STA     $D8             
B0F4: 20 24 BF       JSR     $BF24           
B0F7: 4C A6 B1       JMP     $B1A6           
B0FA: A5 F3          LDA     $F3             
B0FC: F0 10          BEQ     $B10E           
B0FE: E6 F3          INC     $F3             
B100: 10 E8          BPL     $B0EA           
B102: A9 00          LDA     #$00            
B104: 85 F3          STA     $F3             
B106: 85 ED          STA     $ED             
B108: 85 EC          STA     $EC             
B10A: A9 BD          LDA     #$BD            
B10C: 85 D9          STA     $D9             
B10E: 20 5D B5       JSR     $B55D           
B111: A5 E1          LDA     $E1             
B113: C5 C3          CMP     $C3             
B115: D0 04          BNE     $B11B           
B117: A9 00          LDA     #$00            
B119: 85 E1          STA     $E1             
B11B: C9 00          CMP     #$00            
B11D: F0 06          BEQ     $B125           
B11F: 20 24 BF       JSR     $BF24           
B122: 4C 54 B1       JMP     $B154           
B125: 24 36          BIT     $36             
B127: 10 06          BPL     $B12F           
B129: A5 E9          LDA     $E9             
B12B: 49 FF          EOR     #$FF            
B12D: 85 E9          STA     $E9             
B12F: A5 E9          LDA     $E9             
B131: F0 04          BEQ     $B137           
B133: C6 D2          DEC     $D2             
B135: D0 02          BNE     $B139           
B137: E6 D2          INC     $D2             
B139: A5 DD          LDA     $DD             
B13B: 4A             LSR     A               
B13C: A9 0B          LDA     #$0B            
B13E: 48             PHA                     
B13F: A9 02          LDA     #$02            
B141: A0 07          LDY     #$07            
B143: 85 80          STA     $80             
B145: 84 89          STY     $89             
B147: A9 00          LDA     #$00            
B149: 26 8A          ROL     $8A             
B14B: 68             PLA                     
B14C: 85 88          STA     $88             
B14E: 20 24 BF       JSR     $BF24           
B151: 20 F9 B3       JSR     $B3F9           
B154: 20 8F B5       JSR     $B58F           
B157: 20 31 B6       JSR     $B631           
B15A: E6 E1          INC     $E1             
B15C: A5 ED          LDA     $ED             
B15E: C9 00          CMP     #$00            
B160: D0 1D          BNE     $B17F           
B162: A2 00          LDX     #$00            
B164: A9 1D          LDA     #$1D            
B166: 85 BA          STA     $BA             
B168: AD 80 02       LDA     $0280           
B16B: 20 9D B6       JSR     $B69D           
B16E: B5 3C          LDA     $3C,X           
B170: 10 04          BPL     $B176           
B172: A9 00          LDA     #$00            
B174: 95 B7          STA     $B7,X           
B176: 20 57 B8       JSR     $B857           
B179: 20 D4 B3       JSR     $B3D4           
B17C: 4C A6 B1       JMP     $B1A6           
B17F: A9 6D          LDA     #$6D            
B181: 85 BA          STA     $BA             
B183: AD 80 02       LDA     $0280           
B186: 0A             ASL     A               
B187: 0A             ASL     A               
B188: 0A             ASL     A               
B189: 0A             ASL     A               
B18A: A2 01          LDX     #$01            
B18C: 20 9D B6       JSR     $B69D           
B18F: B5 3C          LDA     $3C,X           
B191: 10 04          BPL     $B197           
B193: A9 00          LDA     #$00            
B195: 95 B7          STA     $B7,X           
B197: 20 57 B8       JSR     $B857           
B19A: A5 B2          LDA     $B2             
B19C: 20 5C B7       JSR     $B75C           
B19F: A2 01          LDX     #$01            
B1A1: 20 27 B6       JSR     $B627           
B1A4: D0 0A          BNE     $B1B0           
B1A6: A5 B3          LDA     $B3             
B1A8: 20 5C B7       JSR     $B75C           
B1AB: A2 01          LDX     #$01            
B1AD: 20 27 B6       JSR     $B627           
B1B0: 20 F7 B4       JSR     $B4F7           
B1B3: A9 13          LDA     #$13            
B1B5: 85 04          STA     $04             
B1B7: 85 05          STA     $05             
B1B9: A9 6D          LDA     #$6D            
B1BB: 85 06          STA     $06             
B1BD: A9 1D          LDA     #$1D            
B1BF: 85 07          STA     $07             
B1C1: A9 23          LDA     #$23            
B1C3: A2 02          LDX     #$02            
B1C5: 20 5C B7       JSR     $B75C           
B1C8: 20 27 B6       JSR     $B627           
B1CB: A9 63          LDA     #$63            
B1CD: A2 03          LDX     #$03            
B1CF: 20 5C B7       JSR     $B75C           
B1D2: 20 27 B6       JSR     $B627           
B1D5: A2 00          LDX     #$00            
B1D7: A5 C7          LDA     $C7             
B1D9: A0 02          LDY     #$02            
B1DB: 94 81          STY     $81,X           
B1DD: 29 03          AND     #$03            
B1DF: C9 03          CMP     #$03            
B1E1: D0 02          BNE     $B1E5           
B1E3: F0 16          BEQ     $B1FB           
B1E5: C9 02          CMP     #$02            
B1E7: D0 06          BNE     $B1EF           
B1E9: A0 11          LDY     #$11            
B1EB: 94 04          STY     $04,X           
B1ED: D0 0C          BNE     $B1FB           
B1EF: C9 01          CMP     #$01            
B1F1: D0 06          BNE     $B1F9           
B1F3: A0 10          LDY     #$10            
B1F5: 94 04          STY     $04,X           
B1F7: D0 02          BNE     $B1FB           
B1F9: 95 81          STA     $81,X           
B1FB: E8             INX                     
B1FC: E0 02          CPX     #$02            
B1FE: F0 09          BEQ     $B209           
B200: A5 C7          LDA     $C7             
B202: 4A             LSR     A               
B203: 4A             LSR     A               
B204: 4A             LSR     A               
B205: 4A             LSR     A               
B206: 4C D9 B1       JMP     $B1D9           
B209: A0 04          LDY     #$04            
B20B: A5 F4          LDA     $F4             
B20D: F0 04          BEQ     $B213           
B20F: A9 00          LDA     #$00            
B211: 85 82          STA     $82             
B213: 20 33 BF       JSR     $BF33           
B216: 85 02          STA     $02             
B218: 85 2A          STA     $2A             
B21A: 85 02          STA     $02             
B21C: A5 81          LDA     $81             
B21E: 85 1D          STA     $1D             
B220: A5 82          LDA     $82             
B222: 85 1E          STA     $1E             
B224: 88             DEY                     
B225: D0 F3          BNE     $B21A           
B227: A9 00          LDA     #$00            
B229: 85 26          STA     $26             
B22B: 85 1D          STA     $1D             
B22D: 85 1E          STA     $1E             
B22F: A9 00          LDA     #$00            
B231: 85 02          STA     $02             
B233: 85 2C          STA     $2C             
B235: 85 0E          STA     $0E             
B237: 85 0F          STA     $0F             
B239: 85 04          STA     $04             
B23B: 85 05          STA     $05             
B23D: A5 BA          LDA     $BA             
B23F: 85 07          STA     $07             
B241: A5 D1          LDA     $D1             
B243: 85 06          STA     $06             
B245: A9 FF          LDA     #$FF            
B247: 85 0D          STA     $0D             
B249: A9 01          LDA     #$01            
B24B: 85 25          STA     $25             
B24D: A5 D5          LDA     $D5             
B24F: 85 D3          STA     $D3             
B251: A9 00          LDA     #$00            
B253: A2 0B          LDX     #$0B            
B255: A4 B6          LDY     $B6             
B257: D0 08          BNE     $B261           
B259: C6 D3          DEC     $D3             
B25B: C6 D4          DEC     $D4             
B25D: 85 02          STA     $02             
B25F: A0 0F          LDY     #$0F            
B261: 85 1B          STA     $1B             
B263: 85 02          STA     $02             
B265: 84 DC          STY     $DC             
B267: A4 D4          LDY     $D4             
B269: B1 D8          LDA     ($D8),Y         
B26B: 85 1C          STA     $1C             
B26D: C6 D4          DEC     $D4             
B26F: B5 91          LDA     $91,X           
B271: 85 0E          STA     $0E             
B273: B5 A1          LDA     $A1,X           
B275: 85 0F          STA     $0F             
B277: C6 D3          DEC     $D3             
B279: A4 D3          LDY     $D3             
B27B: B1 C5          LDA     ($C5),Y         
B27D: E4 E8          CPX     $E8             
B27F: D0 04          BNE     $B285           
B281: A4 EA          LDY     $EA             
B283: 84 1F          STY     $1F             
B285: EA             NOP                     
B286: EA             NOP                     
B287: A4 DC          LDY     $DC             
B289: 88             DEY                     
B28A: D0 D5          BNE     $B261           
B28C: 85 1B          STA     $1B             
B28E: 85 02          STA     $02             
B290: CA             DEX                     
B291: 30 27          BMI     $B2BA           
B293: A4 D4          LDY     $D4             
B295: B1 D8          LDA     ($D8),Y         
B297: 85 1C          STA     $1C             
B299: A9 00          LDA     #$00            
B29B: 85 1F          STA     $1F             
B29D: E6 81          INC     $81             
B29F: E6 81          INC     $81             
B2A1: E6 81          INC     $81             
B2A3: E6 81          INC     $81             
B2A5: A4 D3          LDY     $D3             
B2A7: B1 C5          LDA     ($C5),Y         
B2A9: E0 00          CPX     #$00            
B2AB: D0 B2          BNE     $B25F           
B2AD: 85 1B          STA     $1B             
B2AF: A5 B6          LDA     $B6             
B2B1: F0 07          BEQ     $B2BA           
B2B3: 49 0F          EOR     #$0F            
B2B5: A8             TAY                     
B2B6: D0 AB          BNE     $B263           
B2B8: 85 02          STA     $02             
B2BA: 85 02          STA     $02             
B2BC: A9 00          LDA     #$00            
B2BE: 85 25          STA     $25             
B2C0: 85 0D          STA     $0D             
B2C2: 85 0E          STA     $0E             
B2C4: 85 0F          STA     $0F             
B2C6: 85 1F          STA     $1F             
B2C8: 85 0B          STA     $0B             
B2CA: 85 1B          STA     $1B             
B2CC: 85 1C          STA     $1C             
B2CE: 85 2B          STA     $2B             
B2D0: A9 06          LDA     #$06            
B2D2: 85 04          STA     $04             
B2D4: A9 01          LDA     #$01            
B2D6: 85 26          STA     $26             
B2D8: A9 06          LDA     #$06            
B2DA: 85 05          STA     $05             
B2DC: A0 06          LDY     #$06            
B2DE: 85 02          STA     $02             
B2E0: 85 2A          STA     $2A             
B2E2: 88             DEY                     
B2E3: D0 FD          BNE     $B2E2           
B2E5: 85 10          STA     $10             
B2E7: 85 11          STA     $11             
B2E9: A0 07          LDY     #$07            
B2EB: 85 2A          STA     $2A             
B2ED: A5 F0          LDA     $F0             
B2EF: F0 04          BEQ     $B2F5           
B2F1: A5 C4          LDA     $C4             
B2F3: 85 F6          STA     $F6             
B2F5: B1 C1          LDA     ($C1),Y         
B2F7: AA             TAX                     
B2F8: 85 02          STA     $02             
B2FA: A5 F6          LDA     $F6             
B2FC: 85 06          STA     $06             
B2FE: 85 07          STA     $07             
B300: B1 BD          LDA     ($BD),Y         
B302: 85 1C          STA     $1C             
B304: B1 BB          LDA     ($BB),Y         
B306: 85 1B          STA     $1B             
B308: A9 00          LDA     #$00            
B30A: 85 1C          STA     $1C             
B30C: A9 FF          LDA     #$FF            
B30E: 85 81          STA     $81             
B310: 85 81          STA     $81             
B312: A9 00          LDA     #$00            
B314: 85 1B          STA     $1B             
B316: EA             NOP                     
B317: 86 1C          STX     $1C             
B319: B1 BF          LDA     ($BF),Y         
B31B: 85 1B          STA     $1B             
B31D: 88             DEY                     
B31E: 10 D5          BPL     $B2F5           
B320: A9 00          LDA     #$00            
B322: 85 26          STA     $26             
B324: A5 B6          LDA     $B6             
B326: C9 00          CMP     #$00            
B328: D0 52          BNE     $B37C           
B32A: A5 E1          LDA     $E1             
B32C: C9 01          CMP     #$01            
B32E: D0 4C          BNE     $B37C           
B330: A5 E8          LDA     $E8             
B332: C9 0C          CMP     #$0C            
B334: D0 2B          BNE     $B361           
B336: A9 00          LDA     #$00            
B338: 85 E8          STA     $E8             
B33A: 20 7B B7       JSR     $B77B           
B33D: BD C1 B7       LDA     $B7C1,X         
B340: 85 D2          STA     $D2             
B342: A9 02          LDA     #$02            
B344: 85 EA          STA     $EA             
B346: A5 EF          LDA     $EF             
B348: E6 EF          INC     $EF             
B34A: A5 EF          LDA     $EF             
B34C: C9 05          CMP     #$05            
B34E: D0 13          BNE     $B363           
B350: C6 C3          DEC     $C3             
B352: D0 04          BNE     $B358           
B354: A9 01          LDA     #$01            
B356: 85 C3          STA     $C3             
B358: 20 B9 B5       JSR     $B5B9           
B35B: A9 FF          LDA     #$FF            
B35D: 85 D5          STA     $D5             
B35F: D0 1B          BNE     $B37C           
B361: C9 07          CMP     #$07            
B363: D0 17          BNE     $B37C           
B365: A9 A7          LDA     #$A7            
B367: 85 D5          STA     $D5             
B369: 20 7B B7       JSR     $B77B           
B36C: BD C1 B7       LDA     $B7C1,X         
B36F: 38             SEC                     
B370: E9 03          SBC     #$03            
B372: 85 D6          STA     $D6             
B374: A9 BE          LDA     #$BE            
B376: 85 C6          STA     $C6             
B378: A9 14          LDA     #$14            
B37A: 85 C5          STA     $C5             
B37C: A9 BF          LDA     #$BF            
B37E: 85 CE          STA     $CE             
B380: A5 F0          LDA     $F0             
B382: F0 14          BEQ     $B398           
B384: A9 0C          LDA     #$0C            
B386: 85 C9          STA     $C9             
B388: A9 C5          LDA     #$C5            
B38A: 85 CB          STA     $CB             
B38C: 85 EC          STA     $EC             
B38E: A9 D0          LDA     #$D0            
B390: 85 CD          STA     $CD             
B392: A9 DB          LDA     #$DB            
B394: 85 CF          STA     $CF             
B396: D0 16          BNE     $B3AE           
B398: A5 F3          LDA     $F3             
B39A: F0 12          BEQ     $B3AE           
B39C: A9 04          LDA     #$04            
B39E: 85 C9          STA     $C9             
B3A0: 85 EC          STA     $EC             
B3A2: A9 A4          LDA     #$A4            
B3A4: 85 CB          STA     $CB             
B3A6: A9 AF          LDA     #$AF            
B3A8: 85 CD          STA     $CD             
B3AA: A9 BA          LDA     #$BA            
B3AC: 85 CF          STA     $CF             
B3AE: 20 74 B6       JSR     $B674           
B3B1: A5 F4          LDA     $F4             
B3B3: F0 0C          BEQ     $B3C1           
B3B5: A5 ED          LDA     $ED             
B3B7: F0 08          BEQ     $B3C1           
B3B9: A5 B9          LDA     $B9             
B3BB: 85 D9          STA     $D9             
B3BD: A9 00          LDA     #$00            
B3BF: 85 D8          STA     $D8             
B3C1: A5 ED          LDA     $ED             
B3C3: D0 06          BNE     $B3CB           
B3C5: 20 7E BA       JSR     $BA7E           
B3C8: 4C CE B3       JMP     $B3CE           
B3CB: 20 30 BB       JSR     $BB30           
B3CE: 20 44 BF       JSR     $BF44           
B3D1: 4C C7 B0       JMP     $B0C7           
B3D4: A5 D5          LDA     $D5             
B3D6: 10 04          BPL     $B3DC           
B3D8: C9 A7          CMP     #$A7            
B3DA: B0 1C          BCS     $B3F8           
B3DC: A5 EC          LDA     $EC             
B3DE: D0 18          BNE     $B3F8           
B3E0: A9 01          LDA     #$01            
B3E2: 85 C8          STA     $C8             
B3E4: A9 03          LDA     #$03            
B3E6: 85 C9          STA     $C9             
B3E8: A9 E6          LDA     #$E6            
B3EA: 85 CB          STA     $CB             
B3EC: A9 DA          LDA     #$DA            
B3EE: 85 CD          STA     $CD             
B3F0: A9 BC          LDA     #$BC            
B3F2: 85 CE          STA     $CE             
B3F4: A9 78          LDA     #$78            
B3F6: 85 CF          STA     $CF             
B3F8: 60             RTS                     
B3F9: A5 B6          LDA     $B6             
B3FB: C9 08          CMP     #$08            
B3FD: F0 0A          BEQ     $B409           
B3FF: A5 B6          LDA     $B6             
B401: C9 0F          CMP     #$0F            
B403: D0 11          BNE     $B416           
B405: E6 D9          INC     $D9             
B407: D0 0D          BNE     $B416           
B409: C6 D9          DEC     $D9             
B40B: A5 E8          LDA     $E8             
B40D: D0 07          BNE     $B416           
B40F: A5 F4          LDA     $F4             
B411: F0 03          BEQ     $B416           
B413: 20 C1 B9       JSR     $B9C1           
B416: C6 B6          DEC     $B6             
B418: A5 B6          LDA     $B6             
B41A: 29 0F          AND     #$0F            
B41C: 85 B6          STA     $B6             
B41E: F0 07          BEQ     $B427           
B420: C6 B0          DEC     $B0             
B422: C6 B1          DEC     $B1             
B424: C6 D5          DEC     $D5             
B426: 60             RTS                     
B427: E6 E8          INC     $E8             
B429: A5 91          LDA     $91             
B42B: A2 04          LDX     #$04            
B42D: 0A             ASL     A               
B42E: 0A             ASL     A               
B42F: 26 86          ROL     $86             
B431: CA             DEX                     
B432: D0 F9          BNE     $B42D           
B434: A5 A1          LDA     $A1             
B436: A2 04          LDX     #$04            
B438: 4A             LSR     A               
B439: 4A             LSR     A               
B43A: 26 86          ROL     $86             
B43C: CA             DEX                     
B43D: D0 F9          BNE     $B438           
B43F: A9 20          LDA     #$20            
B441: 85 83          STA     $83             
B443: 20 A5 BC       JSR     $BCA5           
B446: 0A             ASL     A               
B447: 85 85          STA     $85             
B449: A5 86          LDA     $86             
B44B: 26 80          ROL     $80             
B44D: 0A             ASL     A               
B44E: 26 80          ROL     $80             
B450: 0A             ASL     A               
B451: 20 D4 B4       JSR     $B4D4           
B454: A5 86          LDA     $86             
B456: 25 83          AND     $83             
B458: 20 D0 B4       JSR     $B4D0           
B45B: 46 83          LSR     $83             
B45D: D0 F5          BNE     $B454           
B45F: 46 8A          LSR     $8A             
B461: 20 D4 B4       JSR     $B4D4           
B464: A5 87          LDA     $87             
B466: 85 82          STA     $82             
B468: 85 84          STA     $84             
B46A: A2 04          LDX     #$04            
B46C: 4A             LSR     A               
B46D: 26 A0          ROL     $A0             
B46F: 46 82          LSR     $82             
B471: 26 A0          ROL     $A0             
B473: 06 84          ASL     $84             
B475: 26 90          ROL     $90             
B477: 06 87          ASL     $87             
B479: 26 90          ROL     $90             
B47B: CA             DEX                     
B47C: D0 EE          BNE     $B46C           
B47E: A2 1F          LDX     #$1F            
B480: B5 8F          LDA     $8F,X           
B482: 95 90          STA     $90,X           
B484: CA             DEX                     
B485: D0 F9          BNE     $B480           
B487: A6 88          LDX     $88             
B489: B5 90          LDA     $90,X           
B48B: F0 0B          BEQ     $B498           
B48D: 29 80          AND     #$80            
B48F: D0 07          BNE     $B498           
B491: CA             DEX                     
B492: D0 F5          BNE     $B489           
B494: 86 91          STX     $91             
B496: 86 A1          STX     $A1             
B498: A5 A9          LDA     $A9             
B49A: 29 80          AND     #$80            
B49C: 85 81          STA     $81             
B49E: A6 89          LDX     $89             
B4A0: B5 A0          LDA     $A0,X           
B4A2: F0 0B          BEQ     $B4AF           
B4A4: 29 80          AND     #$80            
B4A6: C5 81          CMP     $81             
B4A8: D0 05          BNE     $B4AF           
B4AA: CA             DEX                     
B4AB: D0 F3          BNE     $B4A0           
B4AD: 86 A1          STX     $A1             
B4AF: 60             RTS                     

B4B0: 09 09          ORA     #$09            
B4B2: 09 82          ORA     #$82            
B4B4: 00             BRK                     
B4B5: 00             BRK                     
B4B6: 82                                  
B4B7: 82                                  
B4B8: 09 09          ORA     #$09            
B4BA: 09 09          ORA     #$09            
B4BC: 82                                  
B4BD: 00             BRK                     
B4BE: 00             BRK                     
B4BF: 00             BRK                     
B4C0: 09 09          ORA     #$09            
B4C2: 09 82          ORA     #$82            
B4C4: 00             BRK                     
B4C5: 00             BRK                     
B4C6: 00             BRK                     
B4C7: 00             BRK                     
B4C8: 82                                  
B4C9: 00             BRK                     
B4CA: 09 82          ORA     #$82            
B4CC: 82                                  
B4CD: 00             BRK                     
B4CE: 00             BRK                     
B4CF: 00             BRK                     
```

```code
B4D0: 18             CLC                     
B4D1: F0 01          BEQ     $B4D4           
B4D3: 38             SEC                     
B4D4: 26 80          ROL     $80             
B4D6: A5 80          LDA     $80             
B4D8: 29 1F          AND     #$1F            
B4DA: AA             TAX                     
B4DB: 29 FB          AND     #$FB            
B4DD: 85 81          STA     $81             
B4DF: BD B0 B4       LDA     $B4B0,X         
B4E2: 30 07          BMI     $B4EB           
B4E4: 4A             LSR     A               
B4E5: B0 09          BCS     $B4F0           
B4E7: A5 81          LDA     $81             
B4E9: 10 07          BPL     $B4F2           
B4EB: 0A             ASL     A               
B4EC: 26 85          ROL     $85             
B4EE: 90 F7          BCC     $B4E7           
B4F0: 05 81          ORA     $81             
B4F2: 85 80          STA     $80             
B4F4: 26 87          ROL     $87             
B4F6: 60             RTS                     

B4F7: A5 D6          LDA     $D6             
B4F9: 20 5C B7       JSR     $B75C           
B4FC: A2 00          LDX     #$00            
B4FE: 20 27 B6       JSR     $B627           
B501: A9 00          LDA     #$00            
B503: 85 04          STA     $04             
B505: 85 05          STA     $05             
B507: A5 D2          LDA     $D2             
B509: 20 5C B7       JSR     $B75C           
B50C: A2 04          LDX     #$04            
B50E: 20 27 B6       JSR     $B627           
B511: A9 00          LDA     #$00            
B513: 85 0D          STA     $0D             
B515: 85 0E          STA     $0E             
B517: 85 0F          STA     $0F             
B519: A5 F4          LDA     $F4             
B51B: F0 12          BEQ     $B52F           
B51D: A5 ED          LDA     $ED             
B51F: D0 0E          BNE     $B52F           
B521: A5 D9          LDA     $D9             
B523: 85 B9          STA     $B9             
B525: A9 BE          LDA     #$BE            
B527: 85 D9          STA     $D9             
B529: A9 0A          LDA     #$0A            
B52B: 85 D8          STA     $D8             
B52D: 85 B1          STA     $B1             
B52F: A5 ED          LDA     $ED             
B531: C9 00          CMP     #$00            
B533: F0 0D          BEQ     $B542           
B535: A9 00          LDA     #$00            
B537: 85 ED          STA     $ED             
B539: A5 B0          LDA     $B0             
B53B: 18             CLC                     
B53C: 69 09          ADC     #$09            
B53E: 85 D4          STA     $D4             
B540: D0 0B          BNE     $B54D           
B542: A5 B1          LDA     $B1             
B544: 18             CLC                     
B545: 69 09          ADC     #$09            
B547: 85 D4          STA     $D4             
B549: A9 01          LDA     #$01            
B54B: 85 ED          STA     $ED             
B54D: A5 F1          LDA     $F1             
B54F: C9 02          CMP     #$02            
B551: D0 05          BNE     $B558           
B553: A9 08          LDA     #$08            
B555: 85 0B          STA     $0B             
B557: 60             RTS                     

B558: A9 00          LDA     #$00            
B55A: 85 0B          STA     $0B             
B55C: 60             RTS
                     
B55D: A5 F4          LDA     $F4             
B55F: F0 08          BEQ     $B569           
B561: A9 80          LDA     #$80            
B563: 05 C7          ORA     $C7             
B565: 85 C7          STA     $C7             
B567: D0 07          BNE     $B570           
B569: A5 C7          LDA     $C7             
B56B: 29 88          AND     #$88            
B56D: D0 06          BNE     $B575           
B56F: 60             RTS                     
B570: 29 08          AND     #$08            
B572: D0 01          BNE     $B575           
B574: 60             RTS                     
B575: A9 01          LDA     #$01            
B577: 85 B6          STA     $B6             
B579: A9 0B          LDA     #$0B            
B57B: 85 E8          STA     $E8             
B57D: E6 C3          INC     $C3             
B57F: A5 C4          LDA     $C4             
B581: 38             SEC                     
B582: E9 20          SBC     #$20            
B584: 85 C4          STA     $C4             
B586: A5 C3          LDA     $C3             
B588: 85 E1          STA     $E1             
B58A: A9 04          LDA     #$04            
B58C: 85 EF          STA     $EF             
B58E: 60             RTS                     
B58F: A5 ED          LDA     $ED             
B591: C9 00          CMP     #$00            
B593: D0 12          BNE     $B5A7           
B595: 24 23          BIT     $23             
B597: 10 07          BPL     $B5A0           
B599: A9 01          LDA     #$01            
B59B: 05 EE          ORA     $EE             
B59D: 85 EE          STA     $EE             
B59F: 60             RTS                     
B5A0: A9 FE          LDA     #$FE            
B5A2: 25 EE          AND     $EE             
B5A4: 85 EE          STA     $EE             
B5A6: 60             RTS                     
B5A7: 24 23          BIT     $23             
B5A9: 10 07          BPL     $B5B2           
B5AB: A9 02          LDA     #$02            
B5AD: 05 EE          ORA     $EE             
B5AF: 85 EE          STA     $EE             
B5B1: 60             RTS                     
B5B2: A9 FD          LDA     #$FD            
B5B4: 25 EE          AND     $EE             
B5B6: 85 EE          STA     $EE             
B5B8: 60             RTS                     
B5B9: A9 00          LDA     #$00            
B5BB: 85 EF          STA     $EF             
B5BD: A5 C4          LDA     $C4             
B5BF: 18             CLC                     
B5C0: 69 20          ADC     #$20            
B5C2: 85 C4          STA     $C4             
B5C4: 85 08          STA     $08             
B5C6: A9 00          LDA     #$00            
B5C8: 85 B6          STA     $B6             
B5CA: 85 E8          STA     $E8             
B5CC: 85 EA          STA     $EA             
B5CE: A0 1F          LDY     #$1F            
B5D0: 99 90 00       STA     $0090,Y         
B5D3: 88             DEY                     
B5D4: D0 FA          BNE     $B5D0           
B5D6: A5 C7          LDA     $C7             
B5D8: A4 F4          LDY     $F4             
B5DA: D0 06          BNE     $B5E2           
B5DC: 29 88          AND     #$88            
B5DE: F0 06          BEQ     $B5E6           
B5E0: D0 1A          BNE     $B5FC           
B5E2: 29 80          AND     #$80            
B5E4: D0 16          BNE     $B5FC           
B5E6: A9 01          LDA     #$01            
B5E8: 85 C8          STA     $C8             
B5EA: A9 0A          LDA     #$0A            
B5EC: 85 C9          STA     $C9             
B5EE: A9 E6          LDA     #$E6            
B5F0: 85 CB          STA     $CB             
B5F2: A9 8F          LDA     #$8F            
B5F4: 85 CD          STA     $CD             
B5F6: A9 78          LDA     #$78            
B5F8: 85 CF          STA     $CF             
B5FA: D0 00          BNE     $B5FC           
B5FC: A9 40          LDA     #$40            
B5FE: 85 B0          STA     $B0             
B600: 85 B1          STA     $B1             
B602: A9 11          LDA     #$11            
B604: 85 B2          STA     $B2             
B606: A9 87          LDA     #$87            
B608: 85 B3          STA     $B3             
B60A: A9 BD          LDA     #$BD            
B60C: 85 D9          STA     $D9             
B60E: A9 00          LDA     #$00            
B610: 85 D8          STA     $D8             
B612: A5 C7          LDA     $C7             
B614: 29 77          AND     #$77            
B616: 85 C7          STA     $C7             
B618: A9 0A          LDA     #$0A            
B61A: 85 C5          STA     $C5             
B61C: A5 F4          LDA     $F4             
B61E: F0 06          BEQ     $B626           
B620: A5 C7          LDA     $C7             
B622: 09 80          ORA     #$80            
B624: 85 C7          STA     $C7             
B626: 60             RTS                     
B627: 85 02          STA     $02             
B629: 88             DEY                     
B62A: 10 FD          BPL     $B629           
B62C: 95 10          STA     $10,X           
B62E: 95 20          STA     $20,X           
B630: 60             RTS                     
B631: A5 ED          LDA     $ED             
B633: F0 13          BEQ     $B648           
B635: 24 33          BIT     $33             
B637: 50 3A          BVC     $B673           
B639: 20 C1 B9       JSR     $B9C1           
B63C: 20 C1 B9       JSR     $B9C1           
B63F: A5 F2          LDA     $F2             
B641: F0 16          BEQ     $B659           
B643: 20 C1 B9       JSR     $B9C1           
B646: D0 11          BNE     $B659           
B648: 24 23          BIT     $23             
B64A: 50 27          BVC     $B673           
B64C: 20 A4 B9       JSR     $B9A4           
B64F: 20 A4 B9       JSR     $B9A4           
B652: A5 F2          LDA     $F2             
B654: F0 03          BEQ     $B659           
B656: 20 A4 B9       JSR     $B9A4           
B659: A9 00          LDA     #$00            
B65B: 85 EA          STA     $EA             
B65D: A9 01          LDA     #$01            
B65F: 85 C8          STA     $C8             
B661: 85 EC          STA     $EC             
B663: A9 83          LDA     #$83            
B665: 85 CB          STA     $CB             
B667: A9 8F          LDA     #$8F            
B669: 85 CD          STA     $CD             
B66B: A9 99          LDA     #$99            
B66D: 85 CF          STA     $CF             
B66F: A9 02          LDA     #$02            
B671: 85 C9          STA     $C9             
B673: 60             RTS                     
B674: A5 C8          LDA     $C8             
B676: F0 24          BEQ     $B69C           
B678: C6 EB          DEC     $EB             
B67A: 10 20          BPL     $B69C           
B67C: A4 CA          LDY     $CA             
B67E: A5 C9          LDA     $C9             
B680: 85 EB          STA     $EB             
B682: B1 CD          LDA     ($CD),Y         
B684: 85 19          STA     $19             
B686: B1 CB          LDA     ($CB),Y         
B688: 85 17          STA     $17             
B68A: B1 CF          LDA     ($CF),Y         
B68C: 85 15          STA     $15             
B68E: C6 CA          DEC     $CA             
B690: 10 0A          BPL     $B69C           
B692: A0 09          LDY     #$09            
B694: 84 CA          STY     $CA             
B696: A9 00          LDA     #$00            
B698: 85 EC          STA     $EC             
B69A: 85 C8          STA     $C8             
B69C: 60             RTS                     
B69D: 0A             ASL     A               
B69E: 90 45          BCC     $B6E5           
B6A0: 0A             ASL     A               
B6A1: 90 13          BCC     $B6B6           
B6A3: 0A             ASL     A               
B6A4: B0 03          BCS     $B6A9           
B6A6: 4C 1C B7       JMP     $B71C           
B6A9: 0A             ASL     A               
B6AA: B0 03          BCS     $B6AF           
B6AC: 4C 14 B7       JMP     $B714           
B6AF: A0 F0          LDY     #$F0            
B6B1: B5 B0          LDA     $B0,X           
B6B3: 4C 36 B7       JMP     $B736           
B6B6: 2A             ROL     A               
B6B7: 90 06          BCC     $B6BF           
B6B9: 2A             ROL     A               
B6BA: 90 12          BCC     $B6CE           
B6BC: 4C DC B6       JMP     $B6DC           
B6BF: B5 B4          LDA     $B4,X           
B6C1: 29 08          AND     #$08            
B6C3: D0 17          BNE     $B6DC           
B6C5: B5 B4          LDA     $B4,X           
B6C7: 29 01          AND     #$01            
B6C9: F0 E4          BEQ     $B6AF           
B6CB: 4C 1C B7       JMP     $B71C           
B6CE: B5 B4          LDA     $B4,X           
B6D0: 29 08          AND     #$08            
B6D2: D0 08          BNE     $B6DC           
B6D4: B5 B4          LDA     $B4,X           
B6D6: 29 02          AND     #$02            
B6D8: D0 3A          BNE     $B714           
B6DA: F0 D3          BEQ     $B6AF           
B6DC: D6 B2          DEC     $B2,X           
B6DE: D6 B2          DEC     $B2,X           
B6E0: A0 88          LDY     #$88            
B6E2: 4C 36 B7       JMP     $B736           
B6E5: 2A             ROL     A               
B6E6: 2A             ROL     A               
B6E7: 90 05          BCC     $B6EE           
B6E9: 2A             ROL     A               
B6EA: 90 11          BCC     $B6FD           
B6EC: B0 1E          BCS     $B70C           
B6EE: B5 B4          LDA     $B4,X           
B6F0: 29 04          AND     #$04            
B6F2: D0 18          BNE     $B70C           
B6F4: B5 B4          LDA     $B4,X           
B6F6: 29 01          AND     #$01            
B6F8: D0 22          BNE     $B71C           
B6FA: 4C AF B6       JMP     $B6AF           
B6FD: B5 B4          LDA     $B4,X           
B6FF: 29 04          AND     #$04            
B701: D0 09          BNE     $B70C           
B703: B5 B4          LDA     $B4,X           
B705: 29 02          AND     #$02            
B707: D0 0B          BNE     $B714           
B709: 4C AF B6       JMP     $B6AF           
B70C: F6 B2          INC     $B2,X           
B70E: F6 B2          INC     $B2,X           
B710: A0 44          LDY     #$44            
B712: D0 22          BNE     $B736           
B714: D6 B0          DEC     $B0,X           
B716: D6 B0          DEC     $B0,X           
B718: A0 22          LDY     #$22            
B71A: D0 1A          BNE     $B736           
B71C: F6 B0          INC     $B0,X           
B71E: F6 B0          INC     $B0,X           
B720: A5 C3          LDA     $C3             
B722: C9 01          CMP     #$01            
B724: D0 02          BNE     $B728           
B726: F6 B0          INC     $B0,X           
B728: A0 11          LDY     #$11            
B72A: B5 B0          LDA     $B0,X           
B72C: 10 08          BPL     $B736           
B72E: C9 9D          CMP     #$9D            
B730: 90 04          BCC     $B736           
B732: D6 B0          DEC     $B0,X           
B734: D6 B0          DEC     $B0,X           
B736: 20 D1 B7       JSR     $B7D1           
B739: B5 B0          LDA     $B0,X           
B73B: 30 0A          BMI     $B747           
B73D: C9 02          CMP     #$02            
B73F: B0 0A          BCS     $B74B           
B741: 20 18 BA       JSR     $BA18           
B744: 4C 4B B7       JMP     $B74B           
B747: C9 F0          CMP     #$F0            
B749: B0 F6          BCS     $B741           
B74B: C0 F0          CPY     #$F0            
B74D: F0 07          BEQ     $B756           
B74F: 98             TYA                     
B750: D5 B4          CMP     $B4,X           
B752: 94 B4          STY     $B4,X           
B754: D0 05          BNE     $B75B           
B756: 98             TYA                     
B757: 35 B4          AND     $B4,X           
B759: 95 B4          STA     $B4,X           
B75B: 60             RTS                     
B75C: 18             CLC                     
B75D: 69 2E          ADC     #$2E            
B75F: A8             TAY                     
B760: 29 0F          AND     #$0F            
B762: 85 D3          STA     $D3             
B764: 98             TYA                     
B765: 4A             LSR     A               
B766: 4A             LSR     A               
B767: 4A             LSR     A               
B768: 4A             LSR     A               
B769: A8             TAY                     
B76A: 18             CLC                     
B76B: 65 D3          ADC     $D3             
B76D: C9 0F          CMP     #$0F            
B76F: 90 03          BCC     $B774           
B771: E9 0F          SBC     #$0F            
B773: C8             INY                     
B774: 49 07          EOR     #$07            
B776: 0A             ASL     A               
B777: 0A             ASL     A               
B778: 0A             ASL     A               
B779: 0A             ASL     A               
B77A: 60             RTS                     
B77B: 20 A5 BC       JSR     $BCA5           
B77E: 0A             ASL     A               
B77F: 85 85          STA     $85             
B781: 90 21          BCC     $B7A4           
B783: B0 01          BCS     $B786           
B785: EA             NOP                     
B786: A5 91          LDA     $91             
B788: A2 00          LDX     #$00            
B78A: E0 04          CPX     #$04            
B78C: F0 15          BEQ     $B7A3           
B78E: 0A             ASL     A               
B78F: 0A             ASL     A               
B790: 90 03          BCC     $B795           
B792: E8             INX                     
B793: D0 F5          BNE     $B78A           
B795: A5 85          LDA     $85             
B797: 0A             ASL     A               
B798: 85 85          STA     $85             
B79A: 90 01          BCC     $B79D           
B79C: 60             RTS                     
B79D: 18             CLC                     
B79E: 8A             TXA                     
B79F: 69 0C          ADC     #$0C            
B7A1: AA             TAX                     
B7A2: 60             RTS                     
B7A3: EA             NOP                     
B7A4: A5 A1          LDA     $A1             
B7A6: A2 04          LDX     #$04            
B7A8: E0 08          CPX     #$08            
B7AA: F0 D9          BEQ     $B785           
B7AC: 0A             ASL     A               
B7AD: 0A             ASL     A               
B7AE: 90 03          BCC     $B7B3           
B7B0: E8             INX                     
B7B1: D0 F5          BNE     $B7A8           
B7B3: A5 85          LDA     $85             
B7B5: 0A             ASL     A               
B7B6: 85 85          STA     $85             
B7B8: 90 01          BCC     $B7BB           
B7BA: 60             RTS                     
B7BB: 18             CLC                     
B7BC: 8A             TXA                     
B7BD: 69 04          ADC     #$04            
B7BF: AA             TAX                     
B7C0: 60             RTS                     

B7C1: 14                                  
B7C2: 1C                                  
B7C3: 24 2C          BIT     $2C             
B7C5: 4C 44 3C       JMP     $3C44           
B7C8: 34                                  
B7C9: 54                                  
B7CA: 5C                                  
B7CB: 64                                  
B7CC: 6C 8C 84       JMP     ($848C)         
B7CF: 7C                                  
B7D0: 74
                                  
B7D1: E0 00          CPX     #$00            
B7D3: F0 08          BEQ     $B7DD           
B7D5: A5 EE          LDA     $EE             
B7D7: 29 02          AND     #$02            
B7D9: F0 7B          BEQ     $B856           
B7DB: D0 06          BNE     $B7E3           
B7DD: A5 EE          LDA     $EE             
B7DF: 29 01          AND     #$01            
B7E1: F0 73          BEQ     $B856           
B7E3: B5 B4          LDA     $B4,X           
B7E5: 29 0F          AND     #$0F            
B7E7: D0 2E          BNE     $B817           
B7E9: B5 B4          LDA     $B4,X           
B7EB: 29 80          AND     #$80            
B7ED: F0 07          BEQ     $B7F6           
B7EF: F6 B2          INC     $B2,X           
B7F1: F6 B2          INC     $B2,X           
B7F3: 4C 56 B8       JMP     $B856           
B7F6: B5 B4          LDA     $B4,X           
B7F8: 29 40          AND     #$40            
B7FA: F0 07          BEQ     $B803           
B7FC: D6 B2          DEC     $B2,X           
B7FE: D6 B2          DEC     $B2,X           
B800: 4C 56 B8       JMP     $B856           
B803: B5 B4          LDA     $B4,X           
B805: 29 20          AND     #$20            
B807: F0 07          BEQ     $B810           
B809: F6 B0          INC     $B0,X           
B80B: F6 B0          INC     $B0,X           
B80D: 4C 56 B8       JMP     $B856           
B810: D6 B0          DEC     $B0,X           
B812: D6 B0          DEC     $B0,X           
B814: 4C 56 B8       JMP     $B856           
B817: B5 B4          LDA     $B4,X           
B819: 29 08          AND     #$08            
B81B: F0 08          BEQ     $B825           
B81D: F6 B2          INC     $B2,X           
B81F: F6 B2          INC     $B2,X           
B821: F6 B2          INC     $B2,X           
B823: D0 31          BNE     $B856           
B825: B5 B4          LDA     $B4,X           
B827: 29 04          AND     #$04            
B829: F0 09          BEQ     $B834           
B82B: D6 B2          DEC     $B2,X           
B82D: D6 B2          DEC     $B2,X           
B82F: D6 B2          DEC     $B2,X           
B831: 4C 56 B8       JMP     $B856           
B834: B5 B4          LDA     $B4,X           
B836: 29 02          AND     #$02            
B838: F0 08          BEQ     $B842           
B83A: F6 B0          INC     $B0,X           
B83C: F6 B0          INC     $B0,X           
B83E: F6 B0          INC     $B0,X           
B840: D0 14          BNE     $B856           
B842: B5 B4          LDA     $B4,X           
B844: 29 01          AND     #$01            
B846: F0 0E          BEQ     $B856           
B848: D6 B0          DEC     $B0,X           
B84A: D6 B0          DEC     $B0,X           
B84C: D6 B0          DEC     $B0,X           
B84E: A5 C3          LDA     $C3             
B850: C9 01          CMP     #$01            
B852: D0 02          BNE     $B856           
B854: D6 B0          DEC     $B0,X           
B856: 60             RTS                     
B857: B5 3C          LDA     $3C,X           
B859: 10 01          BPL     $B85C           
B85B: 60             RTS                     
B85C: B5 E2          LDA     $E2,X           
B85E: C9 00          CMP     #$00            
B860: D0 01          BNE     $B863           
B862: 60             RTS                     
B863: B5 B7          LDA     $B7,X           
B865: C9 01          CMP     #$01            
B867: D0 01          BNE     $B86A           
B869: 60             RTS                     
B86A: A5 B6          LDA     $B6             
B86C: C9 02          CMP     #$02            
B86E: B0 01          BCS     $B871           
B870: 60             RTS                     
B871: E0 00          CPX     #$00            
B873: F0 07          BEQ     $B87C           
B875: A5 EE          LDA     $EE             
B877: 29 02          AND     #$02            
B879: F0 08          BEQ     $B883           
B87B: 60             RTS                     
B87C: A5 EE          LDA     $EE             
B87E: 29 01          AND     #$01            
B880: F0 01          BEQ     $B883           
B882: 60             RTS                     
B883: A9 01          LDA     #$01            
B885: 95 B7          STA     $B7,X           
B887: 85 C8          STA     $C8             
B889: 85 C9          STA     $C9             
B88B: A9 E6          LDA     #$E6            
B88D: 85 CB          STA     $CB             
B88F: A9 F1          LDA     #$F1            
B891: 85 CD          STA     $CD             
B893: A9 78          LDA     #$78            
B895: 85 CF          STA     $CF             
B897: B5 B0          LDA     $B0,X           
B899: 38             SEC                     
B89A: E5 B6          SBC     $B6             
B89C: 85 81          STA     $81             
B89E: B5 B4          LDA     $B4,X           
B8A0: 29 10          AND     #$10            
B8A2: F0 11          BEQ     $B8B5           
B8A4: A5 81          LDA     $81             
B8A6: 18             CLC                     
B8A7: 69 05          ADC     #$05            
B8A9: 85 81          STA     $81             
B8AB: A5 C3          LDA     $C3             
B8AD: C9 01          CMP     #$01            
B8AF: D0 11          BNE     $B8C2           
B8B1: C6 81          DEC     $81             
B8B3: D0 0D          BNE     $B8C2           
B8B5: B5 B4          LDA     $B4,X           
B8B7: 29 20          AND     #$20            
B8B9: F0 07          BEQ     $B8C2           
B8BB: A5 81          LDA     $81             
B8BD: 18             CLC                     
B8BE: 69 04          ADC     #$04            
B8C0: 85 81          STA     $81             
B8C2: A0 9B          LDY     #$9B            
B8C4: A5 81          LDA     $81             
B8C6: 38             SEC                     
B8C7: 88             DEY                     
B8C8: E9 0F          SBC     #$0F            
B8CA: B0 FB          BCS     $B8C7           
B8CC: B5 B4          LDA     $B4,X           
B8CE: 29 20          AND     #$20            
B8D0: F0 04          BEQ     $B8D6           
B8D2: C8             INY                     
B8D3: C8             INY                     
B8D4: D0 10          BNE     $B8E6           
B8D6: B5 B4          LDA     $B4,X           
B8D8: 29 80          AND     #$80            
B8DA: F0 03          BEQ     $B8DF           
B8DC: C8             INY                     
B8DD: D0 07          BNE     $B8E6           
B8DF: B5 B4          LDA     $B4,X           
B8E1: 29 40          AND     #$40            
B8E3: F0 01          BEQ     $B8E6           
B8E5: C8             INY                     
B8E6: B5 B2          LDA     $B2,X           
B8E8: 85 81          STA     $81             
B8EA: B5 B4          LDA     $B4,X           
B8EC: 29 80          AND     #$80            
B8EE: F0 0E          BEQ     $B8FE           
B8F0: A5 81          LDA     $81             
B8F2: 38             SEC                     
B8F3: E9 06          SBC     #$06            
B8F5: 85 81          STA     $81             
B8F7: 30 26          BMI     $B91F           
B8F9: C9 09          CMP     #$09            
B8FB: B0 22          BCS     $B91F           
B8FD: 60             RTS                     
B8FE: B5 B4          LDA     $B4,X           
B900: 29 40          AND     #$40            
B902: F0 0B          BEQ     $B90F           
B904: A5 81          LDA     $81             
B906: 18             CLC                     
B907: 69 08          ADC     #$08            
B909: 85 81          STA     $81             
B90B: 10 12          BPL     $B91F           
B90D: 30 10          BMI     $B91F           
B90F: B5 B4          LDA     $B4,X           
B911: 29 20          AND     #$20            
B913: F0 05          BEQ     $B91A           
B915: C0 9F          CPY     #$9F            
B917: 90 06          BCC     $B91F           
B919: 60             RTS                     
B91A: C0 91          CPY     #$91            
B91C: B0 01          BCS     $B91F           
B91E: 60             RTS                     
B91F: E6 81          INC     $81             
B921: E6 81          INC     $81             
B923: A5 81          LDA     $81             
B925: 30 0C          BMI     $B933           
B927: C9 30          CMP     #$30            
B929: 90 12          BCC     $B93D           
B92B: C9 50          CMP     #$50            
B92D: 90 22          BCC     $B951           
B92F: C9 70          CMP     #$70            
B931: 90 14          BCC     $B947           
B933: A9 70          LDA     #$70            
B935: 85 E7          STA     $E7             
B937: A9 03          LDA     #$03            
B939: 85 E6          STA     $E6             
B93B: D0 21          BNE     $B95E           
B93D: A9 10          LDA     #$10            
B93F: 85 E7          STA     $E7             
B941: A9 C0          LDA     #$C0            
B943: 85 E6          STA     $E6             
B945: D0 17          BNE     $B95E           
B947: A9 50          LDA     #$50            
B949: 85 E7          STA     $E7             
B94B: A9 C0          LDA     #$C0            
B94D: 85 E6          STA     $E6             
B94F: D0 08          BNE     $B959           
B951: A9 30          LDA     #$30            
B953: 85 E7          STA     $E7             
B955: A9 03          LDA     #$03            
B957: 85 E6          STA     $E6             
B959: 18             CLC                     
B95A: 98             TYA                     
B95B: 69 10          ADC     #$10            
B95D: A8             TAY                     
B95E: 84 E4          STY     $E4             
B960: 18             CLC                     
B961: A5 E7          LDA     $E7             
B963: 69 07          ADC     #$07            
B965: C5 81          CMP     $81             
B967: B0 1F          BCS     $B988           
B969: 18             CLC                     
B96A: 69 08          ADC     #$08            
B96C: A4 E7          LDY     $E7             
B96E: C0 30          CPY     #$30            
B970: 90 0F          BCC     $B981           
B972: C0 50          CPY     #$50            
B974: 90 04          BCC     $B97A           
B976: C0 70          CPY     #$70            
B978: 90 07          BCC     $B981           
B97A: 06 E6          ASL     $E6             
B97C: 06 E6          ASL     $E6             
B97E: 4C 65 B9       JMP     $B965           
B981: 46 E6          LSR     $E6             
B983: 46 E6          LSR     $E6             
B985: 4C 65 B9       JMP     $B965           
B988: A0 00          LDY     #$00            
B98A: 84 E5          STY     $E5             
B98C: B1 E4          LDA     ($E4),Y         
B98E: 45 E6          EOR     $E6             
B990: A0 00          LDY     #$00            
B992: 91 E4          STA     ($E4),Y         
B994: A5 ED          LDA     $ED             
B996: C9 00          CMP     #$00            
B998: F0 06          BEQ     $B9A0           
B99A: 20 FB B9       JSR     $B9FB           
B99D: 4C A3 B9       JMP     $B9A3           
B9A0: 20 DE B9       JSR     $B9DE           
B9A3: 60             RTS                     
B9A4: A0 02          LDY     #$02            
B9A6: B9 BB 00       LDA     $00BB,Y         
B9A9: C9 4B          CMP     #$4B            
B9AB: F0 09          BEQ     $B9B6           
B9AD: 18             CLC                     
B9AE: 69 08          ADC     #$08            
B9B0: 99 BB 00       STA     $00BB,Y         
B9B3: E6 E2          INC     $E2             
B9B5: 60             RTS                     
B9B6: A9 03          LDA     #$03            
B9B8: 99 BB 00       STA     $00BB,Y         
B9BB: 88             DEY                     
B9BC: 88             DEY                     
B9BD: 30 F4          BMI     $B9B3           
B9BF: 10 E5          BPL     $B9A6           
B9C1: A0 02          LDY     #$02            
B9C3: B9 BF 00       LDA     $00BF,Y         
B9C6: C9 4B          CMP     #$4B            
B9C8: F0 09          BEQ     $B9D3           
B9CA: 18             CLC                     
B9CB: 69 08          ADC     #$08            
B9CD: 99 BF 00       STA     $00BF,Y         
B9D0: E6 E3          INC     $E3             
B9D2: 60             RTS                     
B9D3: A9 03          LDA     #$03            
B9D5: 99 BF 00       STA     $00BF,Y         
B9D8: 88             DEY                     
B9D9: 88             DEY                     
B9DA: 30 F4          BMI     $B9D0           
B9DC: 10 E5          BPL     $B9C3           
B9DE: A0 02          LDY     #$02            
B9E0: B9 BB 00       LDA     $00BB,Y         
B9E3: C9 03          CMP     #$03            
B9E5: F0 09          BEQ     $B9F0           
B9E7: 38             SEC                     
B9E8: E9 08          SBC     #$08            
B9EA: 99 BB 00       STA     $00BB,Y         
B9ED: C6 E2          DEC     $E2             
B9EF: 60             RTS                     
B9F0: A9 4B          LDA     #$4B            
B9F2: 99 BB 00       STA     $00BB,Y         
B9F5: 88             DEY                     
B9F6: 88             DEY                     
B9F7: 30 F4          BMI     $B9ED           
B9F9: 10 E5          BPL     $B9E0           
B9FB: A0 02          LDY     #$02            
B9FD: B9 BF 00       LDA     $00BF,Y         
BA00: C9 03          CMP     #$03            
BA02: F0 09          BEQ     $BA0D           
BA04: 38             SEC                     
BA05: E9 08          SBC     #$08            
BA07: 99 BF 00       STA     $00BF,Y         
BA0A: C6 E3          DEC     $E3             
BA0C: 60             RTS                     
BA0D: A9 4B          LDA     #$4B            
BA0F: 99 BF 00       STA     $00BF,Y         
BA12: 88             DEY                     
BA13: 88             DEY                     
BA14: 30 F4          BMI     $BA0A           
BA16: 10 E5          BPL     $B9FD           
BA18: A0 01          LDY     #$01            
BA1A: 84 F3          STY     $F3             
BA1C: 84 C8          STY     $C8             
BA1E: A4 F0          LDY     $F0             
BA20: D0 49          BNE     $BA6B           
BA22: A5 F4          LDA     $F4             
BA24: F0 0C          BEQ     $BA32           
BA26: A5 C7          LDA     $C7             
BA28: 29 07          AND     #$07            
BA2A: C9 01          CMP     #$01            
BA2C: D0 04          BNE     $BA32           
BA2E: A9 01          LDA     #$01            
BA30: 85 F0          STA     $F0             
BA32: A6 ED          LDX     $ED             
BA34: E0 00          CPX     #$00            
BA36: D0 15          BNE     $BA4D           
BA38: A5 C7          LDA     $C7             
BA3A: 29 08          AND     #$08            
BA3C: D0 0E          BNE     $BA4C           
BA3E: C6 C7          DEC     $C7             
BA40: A5 C7          LDA     $C7             
BA42: 09 08          ORA     #$08            
BA44: 85 C7          STA     $C7             
BA46: A9 02          LDA     #$02            
BA48: 95 B0          STA     $B0,X           
BA4A: D0 12          BNE     $BA5E           
BA4C: 60             RTS                     
BA4D: A5 C7          LDA     $C7             
BA4F: 30 19          BMI     $BA6A           
BA51: A5 C7          LDA     $C7             
BA53: 38             SEC                     
BA54: E9 10          SBC     #$10            
BA56: 09 80          ORA     #$80            
BA58: 85 C7          STA     $C7             
BA5A: A9 02          LDA     #$02            
BA5C: 95 B0          STA     $B0,X           
BA5E: A5 C7          LDA     $C7             
BA60: 29 03          AND     #$03            
BA62: F0 07          BEQ     $BA6B           
BA64: A5 C7          LDA     $C7             
BA66: 29 30          AND     #$30            
BA68: F0 01          BEQ     $BA6B           
BA6A: 60             RTS                     
BA6B: A9 01          LDA     #$01            
BA6D: 85 F0          STA     $F0             
BA6F: 85 C8          STA     $C8             
BA71: A9 BE          LDA     #$BE            
BA73: 85 C6          STA     $C6             
BA75: A9 0A          LDA     #$0A            
BA77: 85 C5          STA     $C5             
BA79: A9 00          LDA     #$00            
BA7B: 85 EA          STA     $EA             
BA7D: 60             RTS                     
BA7E: A5 E8          LDA     $E8             
BA80: C9 07          CMP     #$07            
BA82: D0 01          BNE     $BA85           
BA84: 60             RTS                     
BA85: A5 D5          LDA     $D5             
BA87: 10 11          BPL     $BA9A           
BA89: C9 A8          CMP     #$A8            
BA8B: 90 0D          BCC     $BA9A           
BA8D: A9 FF          LDA     #$FF            
BA8F: 85 D5          STA     $D5             
BA91: A9 BE          LDA     #$BE            
BA93: 85 C6          STA     $C6             
BA95: A9 0A          LDA     #$0A            
BA97: 85 C5          STA     $C5             
BA99: 60             RTS                     
BA9A: A5 F5          LDA     $F5             
BA9C: C9 03          CMP     #$03            
BA9E: F0 49          BEQ     $BAE9           
BAA0: C9 01          CMP     #$01            
BAA2: F0 0E          BEQ     $BAB2           
BAA4: A5 E8          LDA     $E8             
BAA6: C9 09          CMP     #$09            
BAA8: D0 04          BNE     $BAAE           
BAAA: A9 00          LDA     #$00            
BAAC: 85 D7          STA     $D7             
BAAE: 24 32          BIT     $32             
BAB0: 30 37          BMI     $BAE9           
BAB2: A5 F1          LDA     $F1             
BAB4: C9 01          CMP     #$01            
BAB6: D0 0B          BNE     $BAC3           
BAB8: E6 D6          INC     $D6             
BABA: A5 D7          LDA     $D7             
BABC: C9 01          CMP     #$01            
BABE: D0 02          BNE     $BAC2           
BAC0: E6 D6          INC     $D6             
BAC2: 60             RTS                     
BAC3: C9 00          CMP     #$00            
BAC5: D0 17          BNE     $BADE           
BAC7: A5 D7          LDA     $D7             
BAC9: F0 08          BEQ     $BAD3           
BACB: E6 DA          INC     $DA             
BACD: A5 DA          LDA     $DA             
BACF: C9 20          CMP     #$20            
BAD1: F0 16          BEQ     $BAE9           
BAD3: C6 D5          DEC     $D5             
BAD5: A5 D7          LDA     $D7             
BAD7: C9 01          CMP     #$01            
BAD9: D0 02          BNE     $BADD           
BADB: C6 D5          DEC     $D5             
BADD: 60             RTS                     
BADE: C6 D6          DEC     $D6             
BAE0: A5 D7          LDA     $D7             
BAE2: C9 01          CMP     #$01            
BAE4: D0 02          BNE     $BAE8           
BAE6: C6 D6          DEC     $D6             
BAE8: 60             RTS                     
BAE9: A5 F1          LDA     $F1             
BAEB: D0 15          BNE     $BB02           
BAED: E6 D5          INC     $D5             
BAEF: E6 D5          INC     $D5             
BAF1: 20 A5 BC       JSR     $BCA5           
BAF4: 0A             ASL     A               
BAF5: 90 02          BCC     $BAF9           
BAF7: B0 1D          BCS     $BB16           
BAF9: A9 01          LDA     #$01            
BAFB: 85 F1          STA     $F1             
BAFD: A9 00          LDA     #$00            
BAFF: 85 0B          STA     $0B             
BB01: 60             RTS                     
BB02: 4A             LSR     A               
BB03: 90 1A          BCC     $BB1F           
BB05: C6 D6          DEC     $D6             
BB07: C6 D6          DEC     $D6             
BB09: 20 A5 BC       JSR     $BCA5           
BB0C: 0A             ASL     A               
BB0D: 90 07          BCC     $BB16           
BB0F: A9 00          LDA     #$00            
BB11: 85 F1          STA     $F1             
BB13: 85 DA          STA     $DA             
BB15: 60             RTS                     
BB16: A9 02          LDA     #$02            
BB18: 85 F1          STA     $F1             
BB1A: A9 08          LDA     #$08            
BB1C: 85 0B          STA     $0B             
BB1E: 60             RTS                     
BB1F: E6 D6          INC     $D6             
BB21: E6 D6          INC     $D6             
BB23: 20 A5 BC       JSR     $BCA5           
BB26: 0A             ASL     A               
BB27: 90 D0          BCC     $BAF9           
BB29: A9 00          LDA     #$00            
BB2B: 85 DA          STA     $DA             
BB2D: 85 F1          STA     $F1             
BB2F: 60             RTS                     
BB30: A4 D7          LDY     $D7             
BB32: C0 01          CPY     #$01            
BB34: F0 1B          BEQ     $BB51           
BB36: C0 03          CPY     #$03            
BB38: F0 50          BEQ     $BB8A           
BB3A: A5 E8          LDA     $E8             
BB3C: C9 08          CMP     #$08            
BB3E: D0 4A          BNE     $BB8A           
BB40: 20 A5 BC       JSR     $BCA5           
BB43: 29 0F          AND     #$0F            
BB45: C9 06          CMP     #$06            
BB47: B0 37          BCS     $BB80           
BB49: A9 3E          LDA     #$3E            
BB4B: 85 D1          STA     $D1             
BB4D: A0 01          LDY     #$01            
BB4F: 84 D7          STY     $D7             
BB51: A5 D6          LDA     $D6             
BB53: 30 0A          BMI     $BB5F           
BB55: C9 10          CMP     #$10            
BB57: B0 0E          BCS     $BB67           
BB59: A9 10          LDA     #$10            
BB5B: 85 D6          STA     $D6             
BB5D: D0 08          BNE     $BB67           
BB5F: C9 89          CMP     #$89            
BB61: 90 04          BCC     $BB67           
BB63: A9 89          LDA     #$89            
BB65: 85 D6          STA     $D6             
BB67: A4 E8          LDY     $E8             
BB69: C0 06          CPY     #$06            
BB6B: D0 08          BNE     $BB75           
BB6D: A0 00          LDY     #$00            
BB6F: 84 D7          STY     $D7             
BB71: A0 88          LDY     #$88            
BB73: 84 D1          STY     $D1             
BB75: 20 A5 BC       JSR     $BCA5           
BB78: 29 0F          AND     #$0F            
BB7A: C9 08          CMP     #$08            
BB7C: D0 07          BNE     $BB85           
BB7E: F0 0F          BEQ     $BB8F           
BB80: A0 03          LDY     #$03            
BB82: 84 D7          STY     $D7             
BB84: 60             RTS                     
BB85: A9 01          LDA     #$01            
BB87: 85 F5          STA     $F5             
BB89: 60             RTS                     
BB8A: A9 02          LDA     #$02            
BB8C: 85 F5          STA     $F5             
BB8E: 60             RTS                     
BB8F: A9 03          LDA     #$03            
BB91: 85 F5          STA     $F5             
BB93: 60             RTS                     
BB94: 20 44 BF       JSR     $BF44           
BB97: 20 9B BC       JSR     $BC9B           
BB9A: 85 2B          STA     $2B             
BB9C: 85 B3          STA     $B3             
BB9E: 20 16 BF       JSR     $BF16           
BBA1: 20 24 BF       JSR     $BF24           
BBA4: A5 B3          LDA     $B3             
BBA6: F0 0C          BEQ     $BBB4           
BBA8: AD 82 02       LDA     $0282           
BBAB: 29 01          AND     #$01            
BBAD: F0 17          BEQ     $BBC6           
BBAF: 4A             LSR     A               
BBB0: 85 B3          STA     $B3             
BBB2: F0 12          BEQ     $BBC6           
BBB4: A5 3C          LDA     $3C             
BBB6: 30 0E          BMI     $BBC6           
BBB8: A0 00          LDY     #$00            
BBBA: C8             INY                     
BBBB: A5 3C          LDA     $3C             
BBBD: 10 FB          BPL     $BBBA           
BBBF: 20 9B BC       JSR     $BC9B           
BBC2: 20 44 BF       JSR     $BF44           
BBC5: 60             RTS                     
BBC6: AD 82 02       LDA     $0282           
BBC9: 29 02          AND     #$02            
BBCB: D0 10          BNE     $BBDD           
BBCD: E6 B2          INC     $B2             
BBCF: A5 B2          LDA     $B2             
BBD1: 29 0F          AND     #$0F            
BBD3: D0 08          BNE     $BBDD           
BBD5: E6 F4          INC     $F4             
BBD7: A5 F4          LDA     $F4             
BBD9: 29 01          AND     #$01            
BBDB: 85 F4          STA     $F4             
BBDD: A9 03          LDA     #$03            
BBDF: 85 04          STA     $04             
BBE1: A9 01          LDA     #$01            
BBE3: 85 05          STA     $05             
BBE5: E6 F6          INC     $F6             
BBE7: A5 F6          LDA     $F6             
BBE9: 85 06          STA     $06             
BBEB: 85 07          STA     $07             
BBED: D0 0C          BNE     $BBFB           
BBEF: E6 81          INC     $81             
BBF1: A5 81          LDA     $81             
BBF3: C9 03          CMP     #$03            
BBF5: D0 04          BNE     $BBFB           
BBF7: 20 44 BF       JSR     $BF44           
BBFA: 60             RTS                     
BBFB: A2 00          LDX     #$00            
BBFD: A9 40          LDA     #$40            
BBFF: 20 90 BC       JSR     $BC90           
BC02: A2 01          LDX     #$01            
BC04: A9 42          LDA     #$42            
BC06: 20 90 BC       JSR     $BC90           
BC09: 20 33 BF       JSR     $BF33           
BC0C: A9 03          LDA     #$03            
BC0E: 85 26          STA     $26             
BC10: 85 02          STA     $02             
BC12: 85 2A          STA     $2A             
BC14: 20 81 BC       JSR     $BC81           
BC17: 20 88 BC       JSR     $BC88           
BC1A: 85 02          STA     $02             
BC1C: A0 09          LDY     #$09            
BC1E: 20 4F BC       JSR     $BC4F           
BC21: 85 02          STA     $02             
BC23: 85 02          STA     $02             
BC25: 85 02          STA     $02             
BC27: A0 13          LDY     #$13            
BC29: 20 4F BC       JSR     $BC4F           
BC2C: AD CA BC       LDA     $BCCA           
BC2F: A0 08          LDY     #$08            
BC31: 99 C0 00       STA     $00C0,Y         
BC34: 88             DEY                     
BC35: 88             DEY                     
BC36: 10 F9          BPL     $BC31           
BC38: 20 88 BC       JSR     $BC88           
BC3B: A0 07          LDY     #$07            
BC3D: A5 F4          LDA     $F4             
BC3F: 0A             ASL     A               
BC40: AA             TAX                     
BC41: BD 5E BF       LDA     $BF5E,X         
BC44: 85 C4          STA     $C4             
BC46: 20 5A BC       JSR     $BC5A           
BC49: 20 44 BF       JSR     $BF44           
BC4C: 4C 9E BB       JMP     $BB9E           
BC4F: A2 09          LDX     #$09            
BC51: B9 4A BF       LDA     $BF4A,Y         
BC54: 95 C0          STA     $C0,X           
BC56: 88             DEY                     
BC57: CA             DEX                     
BC58: 10 F7          BPL     $BC51           
BC5A: A0 07          LDY     #$07            
BC5C: 85 02          STA     $02             
BC5E: B1 C8          LDA     ($C8),Y         
BC60: AA             TAX                     
BC61: 85 02          STA     $02             
BC63: 85 2A          STA     $2A             
BC65: 68             PLA                     
BC66: 48             PHA                     
BC67: EA             NOP                     
BC68: B1 C2          LDA     ($C2),Y         
BC6A: 85 1C          STA     $1C             
BC6C: B1 C0          LDA     ($C0),Y         
BC6E: 85 1B          STA     $1B             
BC70: A5 05          LDA     $05             
BC72: B1 C6          LDA     ($C6),Y         
BC74: 85 1C          STA     $1C             
BC76: B1 C4          LDA     ($C4),Y         
BC78: 85 1B          STA     $1B             
BC7A: 86 1B          STX     $1B             
BC7C: 85 2B          STA     $2B             
BC7E: 88             DEY                     
BC7F: 10 DD          BPL     $BC5E           
BC81: A9 00          LDA     #$00            
BC83: 85 1C          STA     $1C             
BC85: 85 1B          STA     $1B             
BC87: 60             RTS                     
BC88: A0 20          LDY     #$20            
BC8A: 85 02          STA     $02             
BC8C: 88             DEY                     
BC8D: D0 FB          BNE     $BC8A           
BC8F: 60             RTS                     
BC90: 20 5C B7       JSR     $B75C           
BC93: 20 27 B6       JSR     $B627           
BC96: 85 02          STA     $02             
BC98: 85 2A          STA     $2A             
BC9A: 60             RTS                     
BC9B: A9 00          LDA     #$00            
BC9D: A2 F3          LDX     #$F3            
BC9F: 95 00          STA     $00,X           
BCA1: CA             DEX                     
BCA2: D0 FB          BNE     $BC9F           
BCA4: 60             RTS                     
BCA5: A5 DD          LDA     $DD             
BCA7: 85 DF          STA     $DF             
BCA9: A5 DE          LDA     $DE             
BCAB: 85 E0          STA     $E0             
BCAD: 0A             ASL     A               
BCAE: 26 DD          ROL     $DD             
BCB0: 0A             ASL     A               
BCB1: 26 DD          ROL     $DD             
BCB3: 18             CLC                     
BCB4: 65 E0          ADC     $E0             
BCB6: 85 DE          STA     $DE             
BCB8: A9 00          LDA     #$00            
BCBA: 65 DD          ADC     $DD             
BCBC: 18             CLC                     
BCBD: 65 DF          ADC     $DF             
BCBF: 85 DD          STA     $DD             
BCC1: A9 00          LDA     #$00            
BCC3: E6 DE          INC     $DE             
BCC5: 65 DD          ADC     $DD             
BCC7: 85 DD          STA     $DD             
BCC9: 60             RTS                     

BCCA: 53                                  
BCCB: B0 7C          BCS     $BD49           
BCCD: 7C                                  
BCCE: 44                                  
BCCF: 44                                  
BCD0: 44                                  
BCD1: 44                                  
BCD2: 44                                  
BCD3: 00             BRK                     
BCD4: F8             SED                     
BCD5: F8             SED                     
BCD6: 08             PHP                     
BCD7: 08             PHP                     
BCD8: F8             SED                     
BCD9: 80                                  
BCDA: F8             SED                     
BCDB: 00             BRK                     
BCDC: FA                                  
BCDD: FA                                  
BCDE: 8B                                  
BCDF: 9A             TXS                     
BCE0: 82                                  
BCE1: 8B                                  
BCE2: F8             SED                     
BCE3: 00             BRK                     
BCE4: A2 A2          LDX     #$A2            
BCE6: A2 AA          LDX     #$AA            
BCE8: B6 A2          LDX     $A2,Y           
BCEA: 00             BRK                     
BCEB: 00             BRK                     
BCEC: EE 82 82       INC     $8282           
BCEF: CE 88 EE       DEC     $EE88           
BCF2: 00             BRK                     
BCF3: 00             BRK                     
BCF4: 00             BRK                     
BCF5: 00             BRK                     
BCF6: 00             BRK                     
BCF7: 00             BRK                     
BCF8: 0F                                  
BCF9: 0F                                  
BCFA: 0F                                  
BCFB: 0D 0B 09       ORA     $090B           
BCFE: 07                                  
BCFF: 00             BRK                     
BD00: 00             BRK                     
BD01: 00             BRK                     
BD02: 18             CLC                     
BD03: D0 70          BNE     $BD75           
BD05: 20 A0 F8       JSR     $F8A0           
BD08: 28             PLP                     
BD09: 20 00 00       JSR     $0000           
BD0C: 00             BRK                     
BD0D: 00             BRK                     
BD0E: 00             BRK                     
BD0F: 00             BRK                     
BD10: 00             BRK                     
BD11: 00             BRK                     
BD12: 00             BRK                     
BD13: 00             BRK                     
BD14: 00             BRK                     
BD15: 00             BRK                     
BD16: 00             BRK                     
BD17: 00             BRK                     
BD18: 00             BRK                     
BD19: 00             BRK                     
BD1A: 00             BRK                     
BD1B: 00             BRK                     
BD1C: 00             BRK                     
BD1D: 00             BRK                     
BD1E: 00             BRK                     
BD1F: 00             BRK                     
BD20: 00             BRK                     
BD21: 00             BRK                     
BD22: 00             BRK                     
BD23: 00             BRK                     
BD24: 00             BRK                     
BD25: 00             BRK                     
BD26: 00             BRK                     
BD27: 00             BRK                     
BD28: 00             BRK                     
BD29: 00             BRK                     
BD2A: 00             BRK                     
BD2B: 00             BRK                     
BD2C: 00             BRK                     
BD2D: 00             BRK                     
BD2E: 00             BRK                     
BD2F: 00             BRK                     
BD30: 00             BRK                     
BD31: 00             BRK                     
BD32: 00             BRK                     
BD33: 00             BRK                     
BD34: 00             BRK                     
BD35: 00             BRK                     
BD36: 00             BRK                     
BD37: 00             BRK                     
BD38: 00             BRK                     
BD39: 00             BRK                     
BD3A: 00             BRK                     
BD3B: 00             BRK                     
BD3C: 00             BRK                     
BD3D: 00             BRK                     
BD3E: 00             BRK                     
BD3F: 00             BRK                     
BD40: 00             BRK                     
BD41: 00             BRK                     
BD42: 00             BRK                     
BD43: 00             BRK                     
BD44: 00             BRK                     
BD45: 00             BRK                     
BD46: 00             BRK                     
BD47: 00             BRK                     
BD48: 00             BRK                     
BD49: 00             BRK                     
BD4A: 00             BRK                     
BD4B: 00             BRK                     
BD4C: 00             BRK                     
BD4D: 00             BRK                     
BD4E: 00             BRK                     
BD4F: 00             BRK                     
BD50: 00             BRK                     
BD51: 00             BRK                     
BD52: 00             BRK                     
BD53: 00             BRK                     
BD54: 00             BRK                     
BD55: 00             BRK                     
BD56: 00             BRK                     
BD57: 00             BRK                     
BD58: 00             BRK                     
BD59: 00             BRK                     
BD5A: 00             BRK                     
BD5B: 00             BRK                     
BD5C: 00             BRK                     
BD5D: 00             BRK                     
BD5E: 00             BRK                     
BD5F: 00             BRK                     
BD60: 00             BRK                     
BD61: 00             BRK                     
BD62: 00             BRK                     
BD63: 00             BRK                     
BD64: 00             BRK                     
BD65: 00             BRK                     
BD66: 00             BRK                     
BD67: 00             BRK                     
BD68: 00             BRK                     
BD69: 00             BRK                     
BD6A: 00             BRK                     
BD6B: 00             BRK                     
BD6C: 00             BRK                     
BD6D: 00             BRK                     
BD6E: 00             BRK                     
BD6F: 00             BRK                     
BD70: 00             BRK                     
BD71: 00             BRK                     
BD72: 00             BRK                     
BD73: 00             BRK                     
BD74: 00             BRK                     
BD75: 00             BRK                     
BD76: 00             BRK                     
BD77: 00             BRK                     
BD78: 00             BRK                     
BD79: 00             BRK                     
BD7A: 00             BRK                     
BD7B: 00             BRK                     
BD7C: 00             BRK                     
BD7D: 00             BRK                     
BD7E: 00             BRK                     
BD7F: 00             BRK                     
BD80: 00             BRK                     
BD81: 00             BRK                     
BD82: 00             BRK                     
BD83: 00             BRK                     
BD84: 00             BRK                     
BD85: 00             BRK                     
BD86: 00             BRK                     
BD87: 00             BRK                     
BD88: 00             BRK                     
BD89: 00             BRK                     
BD8A: 00             BRK                     
BD8B: 00             BRK                     
BD8C: 00             BRK                     
BD8D: 00             BRK                     
BD8E: 00             BRK                     
BD8F: 00             BRK                     
BD90: 00             BRK                     
BD91: 00             BRK                     
BD92: 00             BRK                     
BD93: 00             BRK                     
BD94: 00             BRK                     
BD95: 00             BRK                     
BD96: 00             BRK                     
BD97: 00             BRK                     
BD98: 00             BRK                     
BD99: 00             BRK                     
BD9A: 00             BRK                     
BD9B: 00             BRK                     
BD9C: 00             BRK                     
BD9D: 00             BRK                     
BD9E: 00             BRK                     
BD9F: 00             BRK                     
BDA0: 00             BRK                     
BDA1: 00             BRK                     
BDA2: 00             BRK                     
BDA3: 00             BRK                     
BDA4: 00             BRK                     
BDA5: 00             BRK                     
BDA6: 00             BRK                     
BDA7: 00             BRK                     
BDA8: 00             BRK                     
BDA9: 00             BRK                     
BDAA: 00             BRK                     
BDAB: 00             BRK                     
BDAC: 00             BRK                     
BDAD: 00             BRK                     
BDAE: 00             BRK                     
BDAF: 00             BRK                     
BDB0: 00             BRK                     
BDB1: 00             BRK                     
BDB2: 00             BRK                     
BDB3: 00             BRK                     
BDB4: 00             BRK                     
BDB5: 00             BRK                     
BDB6: 00             BRK                     
BDB7: 00             BRK                     
BDB8: 00             BRK                     
BDB9: 00             BRK                     
BDBA: 00             BRK                     
BDBB: 00             BRK                     
BDBC: 00             BRK                     
BDBD: 00             BRK                     
BDBE: 00             BRK                     
BDBF: 00             BRK                     
BDC0: 00             BRK                     
BDC1: 00             BRK                     
BDC2: 00             BRK                     
BDC3: 00             BRK                     
BDC4: 00             BRK                     
BDC5: 00             BRK                     
BDC6: 00             BRK                     
BDC7: 00             BRK                     
BDC8: 00             BRK                     
BDC9: 00             BRK                     
BDCA: 00             BRK                     
BDCB: 00             BRK                     
BDCC: 00             BRK                     
BDCD: 00             BRK                     
BDCE: 00             BRK                     
BDCF: 00             BRK                     
BDD0: 00             BRK                     
BDD1: 00             BRK                     
BDD2: 00             BRK                     
BDD3: 00             BRK                     
BDD4: 00             BRK                     
BDD5: 00             BRK                     
BDD6: 00             BRK                     
BDD7: 00             BRK                     
BDD8: 00             BRK                     
BDD9: 00             BRK                     
BDDA: 00             BRK                     
BDDB: 00             BRK                     
BDDC: 00             BRK                     
BDDD: 00             BRK                     
BDDE: 00             BRK                     
BDDF: 00             BRK                     
BDE0: 00             BRK                     
BDE1: 00             BRK                     
BDE2: 00             BRK                     
BDE3: 00             BRK                     
BDE4: 00             BRK                     
BDE5: 00             BRK                     
BDE6: 00             BRK                     
BDE7: 00             BRK                     
BDE8: 00             BRK                     
BDE9: 00             BRK                     
BDEA: 00             BRK                     
BDEB: 00             BRK                     
BDEC: 00             BRK                     
BDED: 00             BRK                     
BDEE: 00             BRK                     
BDEF: 00             BRK                     
BDF0: 00             BRK                     
BDF1: 00             BRK                     
BDF2: 00             BRK                     
BDF3: 00             BRK                     
BDF4: 00             BRK                     
BDF5: 00             BRK                     
BDF6: 00             BRK                     
BDF7: 00             BRK                     
BDF8: 00             BRK                     
BDF9: 00             BRK                     
BDFA: 00             BRK                     
BDFB: 00             BRK                     
BDFC: 00             BRK                     
BDFD: 00             BRK                     
BDFE: 00             BRK                     
BDFF: 00             BRK                     
BE00: 00             BRK                     
BE01: 00             BRK                     
BE02: C0 58          CPY     #$58            
BE04: 70 20          BVS     $BE26           
BE06: 28             PLP                     
BE07: F8             SED                     
BE08: A0 20          LDY     #$20            
BE0A: 00             BRK                     
BE0B: 00             BRK                     
BE0C: 00             BRK                     
BE0D: 00             BRK                     
BE0E: 00             BRK                     
BE0F: 00             BRK                     
BE10: 00             BRK                     
BE11: 00             BRK                     
BE12: 00             BRK                     
BE13: 00             BRK                     
BE14: 00             BRK                     
BE15: 00             BRK                     
BE16: 00             BRK                     
BE17: 00             BRK                     
BE18: 00             BRK                     
BE19: 00             BRK                     
BE1A: 00             BRK                     
BE1B: 00             BRK                     
BE1C: 00             BRK                     
BE1D: 00             BRK                     
BE1E: 00             BRK                     
BE1F: 00             BRK                     
BE20: 00             BRK                     
BE21: 00             BRK                     
BE22: 00             BRK                     
BE23: 00             BRK                     
BE24: 00             BRK                     
BE25: 00             BRK                     
BE26: 00             BRK                     
BE27: 00             BRK                     
BE28: 00             BRK                     
BE29: 00             BRK                     
BE2A: 00             BRK                     
BE2B: 00             BRK                     
BE2C: 00             BRK                     
BE2D: 00             BRK                     
BE2E: 00             BRK                     
BE2F: 00             BRK                     
BE30: 00             BRK                     
BE31: 00             BRK                     
BE32: 00             BRK                     
BE33: 00             BRK                     
BE34: 00             BRK                     
BE35: 00             BRK                     
BE36: 00             BRK                     
BE37: 00             BRK                     
BE38: 00             BRK                     
BE39: 00             BRK                     
BE3A: 00             BRK                     
BE3B: 00             BRK                     
BE3C: 00             BRK                     
BE3D: 00             BRK                     
BE3E: 00             BRK                     
BE3F: 00             BRK                     
BE40: 00             BRK                     
BE41: 00             BRK                     
BE42: 00             BRK                     
BE43: 00             BRK                     
BE44: 00             BRK                     
BE45: 00             BRK                     
BE46: 00             BRK                     
BE47: 00             BRK                     
BE48: 00             BRK                     
BE49: 00             BRK                     
BE4A: 00             BRK                     
BE4B: 00             BRK                     
BE4C: 00             BRK                     
BE4D: 00             BRK                     
BE4E: 00             BRK                     
BE4F: 00             BRK                     
BE50: 00             BRK                     
BE51: 00             BRK                     
BE52: 00             BRK                     
BE53: 00             BRK                     
BE54: 00             BRK                     
BE55: 00             BRK                     
BE56: 00             BRK                     
BE57: 00             BRK                     
BE58: 00             BRK                     
BE59: 00             BRK                     
BE5A: 00             BRK                     
BE5B: 00             BRK                     
BE5C: 00             BRK                     
BE5D: 00             BRK                     
BE5E: 00             BRK                     
BE5F: 00             BRK                     
BE60: 00             BRK                     
BE61: 00             BRK                     
BE62: 00             BRK                     
BE63: 00             BRK                     
BE64: 00             BRK                     
BE65: 00             BRK                     
BE66: 00             BRK                     
BE67: 00             BRK                     
BE68: 00             BRK                     
BE69: 00             BRK                     
BE6A: 00             BRK                     
BE6B: 00             BRK                     
BE6C: 00             BRK                     
BE6D: 00             BRK                     
BE6E: 00             BRK                     
BE6F: 00             BRK                     
BE70: 00             BRK                     
BE71: 00             BRK                     
BE72: 00             BRK                     
BE73: 00             BRK                     
BE74: 00             BRK                     
BE75: 00             BRK                     
BE76: 00             BRK                     
BE77: 00             BRK                     
BE78: 00             BRK                     
BE79: 00             BRK                     
BE7A: 00             BRK                     
BE7B: 00             BRK                     
BE7C: 00             BRK                     
BE7D: 00             BRK                     
BE7E: 00             BRK                     
BE7F: 00             BRK                     
BE80: 00             BRK                     
BE81: 00             BRK                     
BE82: 00             BRK                     
BE83: 00             BRK                     
BE84: 00             BRK                     
BE85: 00             BRK                     
BE86: 00             BRK                     
BE87: 00             BRK                     
BE88: 00             BRK                     
BE89: 00             BRK                     
BE8A: 00             BRK                     
BE8B: 00             BRK                     
BE8C: 00             BRK                     
BE8D: 00             BRK                     
BE8E: 00             BRK                     
BE8F: 00             BRK                     
BE90: 00             BRK                     
BE91: 00             BRK                     
BE92: 00             BRK                     
BE93: 00             BRK                     
BE94: 00             BRK                     
BE95: 00             BRK                     
BE96: 00             BRK                     
BE97: 00             BRK                     
BE98: 00             BRK                     
BE99: 00             BRK                     
BE9A: 00             BRK                     
BE9B: 00             BRK                     
BE9C: 00             BRK                     
BE9D: 00             BRK                     
BE9E: 00             BRK                     
BE9F: 00             BRK                     
BEA0: 00             BRK                     
BEA1: 00             BRK                     
BEA2: 00             BRK                     
BEA3: 00             BRK                     
BEA4: 00             BRK                     
BEA5: 00             BRK                     
BEA6: 00             BRK                     
BEA7: 00             BRK                     
BEA8: 00             BRK                     
BEA9: 00             BRK                     
BEAA: 00             BRK                     
BEAB: 00             BRK                     
BEAC: 00             BRK                     
BEAD: 00             BRK                     
BEAE: 00             BRK                     
BEAF: 00             BRK                     
BEB0: 00             BRK                     
BEB1: 00             BRK                     
BEB2: 00             BRK                     
BEB3: 00             BRK                     
BEB4: 00             BRK                     
BEB5: 00             BRK                     
BEB6: 00             BRK                     
BEB7: 00             BRK                     
BEB8: 00             BRK                     
BEB9: 00             BRK                     
BEBA: 00             BRK                     
BEBB: 00             BRK                     
BEBC: 00             BRK                     
BEBD: 00             BRK                     
BEBE: 00             BRK                     
BEBF: 00             BRK                     
BEC0: 00             BRK                     
BEC1: 00             BRK                     
BEC2: 00             BRK                     
BEC3: 00             BRK                     
BEC4: 00             BRK                     
BEC5: 00             BRK                     
BEC6: 00             BRK                     
BEC7: 00             BRK                     
BEC8: 00             BRK                     
BEC9: 00             BRK                     
BECA: 00             BRK                     
BECB: 00             BRK                     
BECC: 00             BRK                     
BECD: 00             BRK                     
BECE: 00             BRK                     
BECF: 00             BRK                     
BED0: 00             BRK                     
BED1: 00             BRK                     
BED2: 00             BRK                     
BED3: 00             BRK                     
BED4: 00             BRK                     
BED5: 00             BRK                     
BED6: 00             BRK                     
BED7: 00             BRK                     
BED8: 00             BRK                     
BED9: 00             BRK                     
BEDA: 00             BRK                     
BEDB: 00             BRK                     
BEDC: 00             BRK                     
BEDD: 00             BRK                     
BEDE: 00             BRK                     
BEDF: 00             BRK                     
BEE0: 00             BRK                     
BEE1: 00             BRK                     
BEE2: 00             BRK                     
BEE3: 00             BRK                     
BEE4: 00             BRK                     
BEE5: 00             BRK                     
BEE6: 00             BRK                     
BEE7: 00             BRK                     
BEE8: 00             BRK                     
BEE9: 00             BRK                     
BEEA: 00             BRK                     
BEEB: 00             BRK                     
BEEC: 00             BRK                     
BEED: 00             BRK                     
BEEE: 00             BRK                     
BEEF: 00             BRK                     
BEF0: 00             BRK                     
BEF1: 00             BRK                     
BEF2: 00             BRK                     
BEF3: 00             BRK                     
BEF4: 00             BRK                     
BEF5: 00             BRK                     
BEF6: 00             BRK                     
BEF7: 00             BRK                     
BEF8: 00             BRK                     
BEF9: 00             BRK                     
BEFA: 00             BRK                     
BEFB: 00             BRK                     
BEFC: 00             BRK                     
BEFD: 00             BRK                     
BEFE: 00             BRK                     
BEFF: 00             BRK                     
BF00: 00             BRK                     
BF01: 00             BRK                     
BF02: 00             BRK                     
BF03: 00             BRK                     
BF04: 00             BRK                     
BF05: 00             BRK                     
BF06: 00             BRK                     
BF07: 00             BRK                     
BF08: 00             BRK                     
BF09: 00             BRK                     
BF0A: 00             BRK                     
BF0B: 00             BRK                     
BF0C: 66 24          ROR     $24             
BF0E: 3C                                  
BF0F: 18             CLC                     
BF10: 7C                                  
BF11: 54                                  
BF12: 66 00          ROR     $00             
BF14: 00             BRK                     
BF15: 00             BRK                     
```

```code
BF16: A9 02          LDA     #$02            
BF18: 85 02          STA     $02             
BF1A: 85 01          STA     $01             
BF1C: 85 00          STA     $00             
BF1E: A9 29          LDA     #$29            
BF20: 8D 95 02       STA     $0295           
BF23: 60             RTS                     
BF24: AD 84 02       LDA     $0284           
BF27: D0 FB          BNE     $BF24           
BF29: 85 02          STA     $02             
BF2B: 85 00          STA     $00             
BF2D: A9 30          LDA     #$30            
BF2F: 8D 96 02       STA     $0296           
BF32: 60             RTS                     
BF33: AD 84 02       LDA     $0284           
BF36: D0 FB          BNE     $BF33           
BF38: 85 02          STA     $02             
BF3A: 85 01          STA     $01             
BF3C: A9 11          LDA     #$11            
BF3E: 8D 97 02       STA     $0297           
BF41: 85 02          STA     $02             
BF43: 60             RTS                     
BF44: AD 84 02       LDA     $0284           
BF47: D0 FB          BNE     $BF44           
BF49: 60             RTS                     

BF4A: CC BC D4       CPY     $D4BC           
BF4D: BC DC BC       LDY     $BCDC,X         
BF50: E4 BC          CPX     $BC             
BF52: EC BC 5B       CPX     $5BBC           
BF55: B0 0B          BCS     $BF62           
BF57: B0 4B          BCS     $BFA4           
BF59: B0 43          BCS     $BF9E           
BF5B: B0 13          BCS     $BF70           
BF5D: B0 13          BCS     $BF72           
BF5F: B0 0B          BCS     $BF6C           
BF61: B0 00          BCS     $BF63           
BF63: 00             BRK                     
BF64: 12                                  
BF65: 13                                  
BF66: 12                                  
BF67: 1D 1D 13       ORA     $131D,X         
BF6A: 12                                  
BF6B: 13                                  
BF6C: 12                                  
BF6D: 00             BRK                     
BF6E: 00             BRK                     
BF6F: 0F                                  
BF70: 0B                                  
BF71: 07                                  
BF72: 0F                                  
BF73: 0B                                  
BF74: 07                                  
BF75: 0F                                  
BF76: 0B                                  
BF77: 07                                  
BF78: 00             BRK                     
BF79: 00             BRK                     
BF7A: 0C                                  
BF7B: 0C                                  
BF7C: 0C                                  
BF7D: 0C                                  
BF7E: 0C                                  
BF7F: 0C                                  
BF80: 0C                                  
BF81: 0C                                  
BF82: 0C                                  
BF83: 00             BRK                     
BF84: 00             BRK                     
BF85: 03                                  
BF86: 04                                  
BF87: 05 06          ORA     $06             
BF89: 07                                  
BF8A: 08             PHP                     
BF8B: 09 0A          ORA     #$0A            
BF8D: 0B                                  
BF8E: 00             BRK                     
BF8F: 00             BRK                     
BF90: 0F                                  
BF91: 0F                                  
BF92: 0F                                  
BF93: 0F                                  
BF94: 0F                                  
BF95: 0F                                  
BF96: 0F                                  
BF97: 0F                                  
BF98: 0F                                  
BF99: 00             BRK                     
BF9A: 00             BRK                     
BF9B: 04                                  
BF9C: 04                                  
BF9D: 04                                  
BF9E: 04                                  
BF9F: 04                                  
BFA0: 04                                  
BFA1: 04                                  
BFA2: 04                                  
BFA3: 04                                  
BFA4: 00             BRK                     
BFA5: 00             BRK                     
BFA6: 0D 0C 0B       ORA     $0B0C           
BFA9: 0A             ASL     A               
BFAA: 09 0A          ORA     #$0A            
BFAC: 0B                                  
BFAD: 0C                                  
BFAE: 0D 00 00       ORA     $0000           
BFB1: 05 0A          ORA     $0A             
BFB3: 0F                                  
BFB4: 05 0A          ORA     $0A             
BFB6: 0F                                  
BFB7: 0F                                  
BFB8: 0A             ASL     A               
BFB9: 0F                                  
BFBA: 00             BRK                     
BFBB: 00             BRK                     
BFBC: 0C                                  
BFBD: 0B                                  
BFBE: 0A             ASL     A               
BFBF: 09 08          ORA     #$08            
BFC1: 06 05          ASL     $05             
BFC3: 04                                  
BFC4: 01 00          ORA     ($00,X)         
BFC6: 00             BRK                     
BFC7: 1D 1D 1D       ORA     $1D1D,X         
BFCA: 18             CLC                     
BFCB: 18             CLC                     
BFCC: 1F                                  
BFCD: 1F                                  
BFCE: 1F                                  
BFCF: 1F                                  
BFD0: 00             BRK                     
BFD1: 00             BRK                     
BFD2: 05 07          ORA     $07             
BFD4: 09 0B          ORA     #$0B            
BFD6: 0C                                  
BFD7: 0D 0E 0F       ORA     $0F0E           
BFDA: 0F                                  
BFDB: 00             BRK                     
BFDC: 00             BRK                     
BFDD: 01 01          ORA     ($01,X)         
BFDF: 01 01          ORA     ($01,X)         
BFE1: 01 08          ORA     ($08,X)         
BFE3: 08             PHP                     
BFE4: 08             PHP                     
BFE5: 08             PHP                     
BFE6: 00             BRK                     
BFE7: 00             BRK                     
BFE8: 17                                  
BFE9: 18             CLC                     
BFEA: 19 18 17       ORA     $1718,Y         
BFED: 19 18 17       ORA     $1718,Y         
BFF0: 19 00 00       ORA     $0000,Y         
BFF3: 00             BRK                     
BFF4: 00             BRK                     
BFF5: 00             BRK                     
BFF6: 00             BRK                     
BFF7: 0A             ASL     A               
BFF8: 00             BRK                     
BFF9: 05      
```

# Vectors

```code      
BFFA: 0A 0F 
BFFC: 00 B0 
BFFE: 00 B0      
```