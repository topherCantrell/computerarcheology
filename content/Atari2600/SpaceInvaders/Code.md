![Space Invaders](A26Invaders.jpg)

# Space Invaders

>>> cpu 6502

>>> memoryTable hard 
[Hardware Info](../Stella.md)

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

F000: 85 2B          STA     $2B             
F002: A5 84          LDA     $84             
F004: 30 00          BMI     $F006           
F006: 29 0F          AND     #$0F            
F008: AA             TAX                     
F009: CA             DEX                     
F00A: 10 FD          BPL     $F009           
F00C: B1 F8          LDA     ($F8),Y         
F00E: AA             TAX                     
F00F: B1 EE          LDA     ($EE),Y         
F011: 85 1B          STA     $1B             
F013: B1 F0          LDA     ($F0),Y         
F015: 85 1C          STA     $1C             
F017: B1 F2          LDA     ($F2),Y         
F019: 85 1B          STA     $1B             
F01B: B1 F4          LDA     ($F4),Y         
F01D: 85 1C          STA     $1C             
F01F: B1 F6          LDA     ($F6),Y         
F021: 85 1B          STA     $1B             
F023: 8A             TXA                     
F024: 85 1C          STA     $1C             
F026: 85 1B          STA     $1B             
F028: C6 89          DEC     $89             
F02A: 88             DEY                     
F02B: 48             PHA                     
F02C: 68             PLA                     
F02D: 48             PHA                     
F02E: 68             PLA                     
F02F: B1 F8          LDA     ($F8),Y         
F031: AA             TAX                     
F032: B1 EE          LDA     ($EE),Y         
F034: 85 1B          STA     $1B             
F036: B1 F0          LDA     ($F0),Y         
F038: 85 1C          STA     $1C             
F03A: B1 F2          LDA     ($F2),Y         
F03C: 85 1B          STA     $1B             
F03E: B1 F4          LDA     ($F4),Y         
F040: 85 1C          STA     $1C             
F042: B1 F6          LDA     ($F6),Y         
F044: 85 1B          STA     $1B             
F046: 8A             TXA                     
F047: 85 1C          STA     $1C             
F049: 85 1B          STA     $1B             
F04B: A5 89          LDA     $89             
F04D: C9 04          CMP     #$04            
F04F: 90 04          BCC     $F055           
F051: A9 00          LDA     #$00            
F053: B0 03          BCS     $F058           
F055: EA             NOP                     
F056: A9 02          LDA     #$02            
F058: 8D 1F 00       STA     $001F           
F05B: 88             DEY                     
F05C: 10 AE          BPL     $F00C           
F05E: C8             INY                     
F05F: 84 1B          STY     $1B             
F061: 84 1C          STY     $1C             
F063: 84 2B          STY     $2B             
F065: 84 1B          STY     $1B             
F067: 84 1C          STY     $1C             
F069: 85 02          STA     $02             
F06B: C6 89          DEC     $89             
F06D: A5 89          LDA     $89             
F06F: C9 04          CMP     #$04            
F071: 90 04          BCC     $F077           
F073: A9 00          LDA     #$00            
F075: B0 03          BCS     $F07A           
F077: EA             NOP                     
F078: A9 02          LDA     #$02            
F07A: 85 1F          STA     $1F             
F07C: A4 80          LDY     $80             
F07E: A5 02          LDA     $02             
F080: 05 03          ORA     $03             
F082: 0A             ASL     A               
F083: 30 06          BMI     $F08B           
F085: EA             NOP                     
F086: EA             NOP                     
F087: EA             NOP                     
F088: EA             NOP                     
F089: 10 07          BPL     $F092           
F08B: A5 82          LDA     $82             
F08D: 19 DC FC       ORA     $FCDC,Y         
F090: 85 82          STA     $82             
F092: 85 2C          STA     $2C             
F094: 88             DEY                     
F095: C6 8C          DEC     $8C             
F097: 10 09          BPL     $F0A2           
F099: A9 00          LDA     #$00            
F09B: 85 25          STA     $25             
F09D: 85 26          STA     $26             
F09F: 4C 09 F1       JMP     $F109           
F0A2: 20 E9 FD       JSR     $FDE9           
F0A5: 84 80          STY     $80             
F0A7: B9 92 00       LDA     $0092,Y         
F0AA: 85 F8          STA     $F8             
F0AC: A2 F4          LDX     #$F4            
F0AE: 46 F8          LSR     $F8             
F0B0: 90 07          BCC     $F0B9           
F0B2: B9 D6 FC       LDA     $FCD6,Y         
F0B5: 65 8B          ADC     $8B             
F0B7: D0 04          BNE     $F0BD           
F0B9: 48             PHA                     
F0BA: 68             PLA                     
F0BB: A9 00          LDA     #$00            
F0BD: 95 FA          STA     $FA,X           
F0BF: E8             INX                     
F0C0: E8             INX                     
F0C1: 30 EB          BMI     $F0AE           
F0C3: C6 89          DEC     $89             
F0C5: A5 89          LDA     $89             
F0C7: C9 04          CMP     #$04            
F0C9: 90 04          BCC     $F0CF           
F0CB: A9 00          LDA     #$00            
F0CD: B0 03          BCS     $F0D2           
F0CF: EA             NOP                     
F0D0: A9 02          LDA     #$02            
F0D2: 85 1F          STA     $1F             
F0D4: A5 C8          LDA     $C8             
F0D6: 29 38          AND     #$38            
F0D8: 4A             LSR     A               
F0D9: 4A             LSR     A               
F0DA: 4A             LSR     A               
F0DB: C5 80          CMP     $80             
F0DD: D0 16          BNE     $F0F5           
F0DF: A5 C8          LDA     $C8             
F0E1: 29 07          AND     #$07            
F0E3: 0A             ASL     A               
F0E4: AA             TAX                     
F0E5: A5 C8          LDA     $C8             
F0E7: 2A             ROL     A               
F0E8: 2A             ROL     A               
F0E9: 2A             ROL     A               
F0EA: 29 03          AND     #$03            
F0EC: A8             TAY                     
F0ED: B9 1E FD       LDA     $FD1E,Y         
F0F0: 95 EE          STA     $EE,X           
F0F2: 4C FA F0       JMP     $F0FA           
F0F5: A2 05          LDX     #$05            
F0F7: CA             DEX                     
F0F8: 10 FD          BPL     $F0F7           
F0FA: 85 2B          STA     $2B             
F0FC: 20 B2 FD       JSR     $FDB2           
F0FF: A2 06          LDX     #$06            
F101: CA             DEX                     
F102: 10 FD          BPL     $F101           
F104: A0 09          LDY     #$09            
F106: 4C 00 F0       JMP     $F000           
F109: C6 8E          DEC     $8E             
F10B: 30 06          BMI     $F113           
F10D: 20 B2 FD       JSR     $FDB2           
F110: 4C 09 F1       JMP     $F109           
F113: 24 98          BIT     $98             
F115: 70 03          BVS     $F11A           
F117: 4C B2 F1       JMP     $F1B2           
F11A: A5 DD          LDA     $DD             
F11C: 85 06          STA     $06             
F11E: A9 01          LDA     #$01            
F120: 85 8E          STA     $8E             
F122: A9 00          LDA     #$00            
F124: 85 EF          STA     $EF             
F126: 85 F1          STA     $F1             
F128: 85 F3          STA     $F3             
F12A: A9 AB          LDA     #$AB            
F12C: 85 EE          STA     $EE             
F12E: A9 B4          LDA     #$B4            
F130: 85 F0          STA     $F0             
F132: A9 BD          LDA     #$BD            
F134: 85 F2          STA     $F2             
F136: A9 11          LDA     #$11            
F138: 85 02          STA     $02             
F13A: 85 2B          STA     $2B             
F13C: 85 F4          STA     $F4             
F13E: A5 85          LDA     $85             
F140: 85 20          STA     $20             
F142: 29 0F          AND     #$0F            
F144: A8             TAY                     
F145: 88             DEY                     
F146: 10 FD          BPL     $F145           
F148: 85 10          STA     $10             
F14A: C6 89          DEC     $89             
F14C: A5 89          LDA     $89             
F14E: C9 04          CMP     #$04            
F150: A9 02          LDA     #$02            
F152: 90 01          BCC     $F155           
F154: 4A             LSR     A               
F155: 85 1F          STA     $1F             
F157: 85 02          STA     $02             
F159: 85 2A          STA     $2A             
F15B: A0 00          LDY     #$00            
F15D: A5 85          LDA     $85             
F15F: 10 02          BPL     $F163           
F161: A5 85          LDA     $85             
F163: 29 0F          AND     #$0F            
F165: AA             TAX                     
F166: CA             DEX                     
F167: CA             DEX                     
F168: CA             DEX                     
F169: 10 FD          BPL     $F168           
F16B: B1 EE          LDA     ($EE),Y         
F16D: 85 1B          STA     $1B             
F16F: EA             NOP                     
F170: B1 F0          LDA     ($F0),Y         
F172: 85 1B          STA     $1B             
F174: B1 F2          LDA     ($F2),Y         
F176: 85 1B          STA     $1B             
F178: C6 F4          DEC     $F4             
F17A: 30 12          BMI     $F18E           
F17C: A5 F4          LDA     $F4             
F17E: 4A             LSR     A               
F17F: 90 08          BCC     $F189           
F181: C8             INY                     
F182: A9 20          LDA     #$20            
F184: 4A             LSR     A               
F185: D0 FD          BNE     $F184           
F187: F0 E2          BEQ     $F16B           
F189: 20 E9 FD       JSR     $FDE9           
F18C: 10 DD          BPL     $F16B           
F18E: A9 00          LDA     #$00            
F190: 85 1B          STA     $1B             
F192: 85 02          STA     $02             
F194: A5 02          LDA     $02             
F196: 0A             ASL     A               
F197: 29 80          AND     #$80            
F199: 05 82          ORA     $82             
F19B: 85 82          STA     $82             
F19D: 85 2C          STA     $2C             
F19F: 20 E9 FD       JSR     $FDE9           
F1A2: 85 2B          STA     $2B             
F1A4: 85 02          STA     $02             
F1A6: 85 02          STA     $02             
F1A8: C6 8E          DEC     $8E             
F1AA: 30 06          BMI     $F1B2           
F1AC: 20 B2 FD       JSR     $FDB2           
F1AF: 4C A8 F1       JMP     $F1A8           
F1B2: 24 98          BIT     $98             
F1B4: 10 03          BPL     $F1B9           
F1B6: 4C 82 F2       JMP     $F282           
F1B9: 20 E9 FD       JSR     $FDE9           
F1BC: 85 2B          STA     $2B             
F1BE: 85 02          STA     $02             
F1C0: A5 DF          LDA     $DF             
F1C2: 85 06          STA     $06             
F1C4: A5 86          LDA     $86             
F1C6: 85 20          STA     $20             
F1C8: 29 0F          AND     #$0F            
F1CA: A8             TAY                     
F1CB: 88             DEY                     
F1CC: 10 FD          BPL     $F1CB           
F1CE: 85 10          STA     $10             
F1D0: 85 02          STA     $02             
F1D2: A5 E0          LDA     $E0             
F1D4: 85 07          STA     $07             
F1D6: A5 87          LDA     $87             
F1D8: 85 21          STA     $21             
F1DA: 29 0F          AND     #$0F            
F1DC: A8             TAY                     
F1DD: 88             DEY                     
F1DE: 10 FD          BPL     $F1DD           
F1E0: 85 11          STA     $11             
F1E2: 85 02          STA     $02             
F1E4: 85 2A          STA     $2A             
F1E6: 20 E9 FD       JSR     $FDE9           
F1E9: A9 00          LDA     #$00            
F1EB: 2C 82 02       BIT     $0282           
F1EE: 10 02          BPL     $F1F2           
F1F0: A9 05          LDA     #$05            
F1F2: 85 05          STA     $05             
F1F4: A9 00          LDA     #$00            
F1F6: 50 02          BVC     $F1FA           
F1F8: A9 05          LDA     #$05            
F1FA: 85 04          STA     $04             
F1FC: A5 98          LDA     $98             
F1FE: 29 10          AND     #$10            
F200: F0 02          BEQ     $F204           
F202: A9 0A          LDA     #$0A            
F204: 85 F4          STA     $F4             
F206: A5 98          LDA     $98             
F208: 29 20          AND     #$20            
F20A: F0 02          BEQ     $F20E           
F20C: A9 0A          LDA     #$0A            
F20E: 85 F6          STA     $F6             
F210: A5 AA          LDA     $AA             
F212: 4A             LSR     A               
F213: 85 02          STA     $02             
F215: 90 17          BCC     $F22E           
F217: A6 C9          LDX     $C9             
F219: BD 16 FD       LDA     $FD16,X         
F21C: 85 F8          STA     $F8             
F21E: A9 FF          LDA     #$FF            
F220: 85 F9          STA     $F9             
F222: A5 CA          LDA     $CA             
F224: 29 08          AND     #$08            
F226: D0 04          BNE     $F22C           
F228: 85 F4          STA     $F4             
F22A: 85 F6          STA     $F6             
F22C: 10 25          BPL     $F253           
F22E: A9 00          LDA     #$00            
F230: 85 F8          STA     $F8             
F232: A5 CA          LDA     $CA             
F234: 4A             LSR     A               
F235: 4A             LSR     A               
F236: 4A             LSR     A               
F237: A5 AA          LDA     $AA             
F239: 29 04          AND     #$04            
F23B: F0 08          BEQ     $F245           
F23D: A9 1E          LDA     #$1E            
F23F: B0 02          BCS     $F243           
F241: A9 14          LDA     #$14            
F243: 85 F4          STA     $F4             
F245: A5 AA          LDA     $AA             
F247: 29 02          AND     #$02            
F249: F0 08          BEQ     $F253           
F24B: A9 14          LDA     #$14            
F24D: B0 02          BCS     $F251           
F24F: A9 1E          LDA     #$1E            
F251: 85 F6          STA     $F6             
F253: A2 09          LDX     #$09            
F255: A0 09          LDY     #$09            
F257: 85 02          STA     $02             
F259: A9 00          LDA     #$00            
F25B: 85 0D          STA     $0D             
F25D: B1 F4          LDA     ($F4),Y         
F25F: 85 1B          STA     $1B             
F261: B1 F6          LDA     ($F6),Y         
F263: 85 1C          STA     $1C             
F265: 8A             TXA                     
F266: 4A             LSR     A               
F267: A8             TAY                     
F268: B1 F8          LDA     ($F8),Y         
F26A: 85 0D          STA     $0D             
F26C: 8A             TXA                     
F26D: 4A             LSR     A               
F26E: 90 0D          BCC     $F27D           
F270: C6 89          DEC     $89             
F272: A5 89          LDA     $89             
F274: C9 04          CMP     #$04            
F276: A9 02          LDA     #$02            
F278: 90 01          BCC     $F27B           
F27A: 4A             LSR     A               
F27B: 85 1F          STA     $1F             
F27D: CA             DEX                     
F27E: 8A             TXA                     
F27F: A8             TAY                     
F280: 10 D5          BPL     $F257           
F282: 85 02          STA     $02             
F284: A9 00          LDA     #$00            
F286: 85 04          STA     $04             
F288: 85 05          STA     $05             
F28A: 85 0D          STA     $0D             
F28C: 85 1F          STA     $1F             
F28E: 85 1B          STA     $1B             
F290: 85 1C          STA     $1C             
F292: A5 E4          LDA     $E4             
F294: 85 09          STA     $09             
F296: A5 81          LDA     $81             
F298: 85 10          STA     $10             
F29A: A2 04          LDX     #$04            
F29C: CA             DEX                     
F29D: 10 FD          BPL     $F29C           
F29F: 85 11          STA     $11             
F2A1: 85 2B          STA     $2B             
F2A3: A9 E0          LDA     #$E0            
F2A5: 85 21          STA     $21             
F2A7: 85 02          STA     $02             
F2A9: 85 2A          STA     $2A             
F2AB: A9 C0          LDA     #$C0            
F2AD: 85 1B          STA     $1B             
F2AF: 85 1C          STA     $1C             
F2B1: A2 04          LDX     #$04            
F2B3: A9 00          LDA     #$00            
F2B5: 95 F3          STA     $F3,X           
F2B7: CA             DEX                     
F2B8: D0 FB          BNE     $F2B5           
F2BA: 20 08 FE       JSR     $FE08           
F2BD: E8             INX                     
F2BE: 20 08 FE       JSR     $FE08           
F2C1: A5 AA          LDA     $AA             
F2C3: 29 81          AND     #$81            
F2C5: D0 2F          BNE     $F2F6           
F2C7: 24 02          BIT     $02             
F2C9: 50 06          BVC     $F2D1           
F2CB: A9 04          LDA     #$04            
F2CD: 24 AA          BIT     $AA             
F2CF: F0 0B          BEQ     $F2DC           
F2D1: CA             DEX                     
F2D2: 24 03          BIT     $03             
F2D4: 50 20          BVC     $F2F6           
F2D6: A9 02          LDA     #$02            
F2D8: 24 AA          BIT     $AA             
F2DA: D0 1A          BNE     $F2F6           
F2DC: 05 AA          ORA     $AA             
F2DE: 85 AA          STA     $AA             
F2E0: 85 C6          STA     $C6             
F2E2: 20 75 FE       JSR     $FE75           
F2E5: A9 06          LDA     #$06            
F2E7: 20 7E FE       JSR     $FE7E           
F2EA: A5 C7          LDA     $C7             
F2EC: D0 08          BNE     $F2F6           
F2EE: 24 DB          BIT     $DB             
F2F0: 50 04          BVC     $F2F6           
F2F2: A9 02          LDA     #$02            
F2F4: 95 F4          STA     $F4,X           
F2F6: 85 02          STA     $02             
F2F8: AD 84 02       LDA     $0284           
F2FB: D0 FB          BNE     $F2F8           
F2FD: 85 1B          STA     $1B             
F2FF: 85 1C          STA     $1C             
F301: A9 C8          LDA     #$C8            
F303: 8D 95 02       STA     $0295           
F306: A9 00          LDA     #$00            
F308: 85 F1          STA     $F1             
F30A: AA             TAX                     
F30B: A5 82          LDA     $82             
F30D: 10 5F          BPL     $F36E           
F30F: A5 CA          LDA     $CA             
F311: 4A             LSR     A               
F312: 90 02          BCC     $F316           
F314: A2 04          LDX     #$04            
F316: B5 D1          LDA     $D1,X           
F318: C9 49          CMP     #$49            
F31A: 90 04          BCC     $F320           
F31C: C9 58          CMP     #$58            
F31E: 90 01          BCC     $F321           
F320: E8             INX                     
F321: E0 03          CPX     #$03            
F323: 90 0C          BCC     $F331           
F325: A9 09          LDA     #$09            
F327: 85 EF          STA     $EF             
F329: A9 FF          LDA     #$FF            
F32B: 85 F2          STA     $F2             
F32D: A9 7F          LDA     #$7F            
F32F: D0 0A          BNE     $F33B           
F331: A9 FF          LDA     #$FF            
F333: 85 EF          STA     $EF             
F335: A9 01          LDA     #$01            
F337: 85 F2          STA     $F2             
F339: A9 F6          LDA     #$F6            
F33B: 95 D1          STA     $D1,X           
F33D: B5 D3          LDA     $D3,X           
F33F: A0 03          LDY     #$03            
F341: 18             CLC                     
F342: E5 9B          SBC     $9B             
F344: 88             DEY                     
F345: 18             CLC                     
F346: 69 E0          ADC     #$E0            
F348: 10 FA          BPL     $F344           
F34A: 69 20          ADC     #$20            
F34C: AA             TAX                     
F34D: B9 13 FD       LDA     $FD13,Y         
F350: 85 F0          STA     $F0             
F352: A4 EF          LDY     $EF             
F354: 98             TYA                     
F355: 18             CLC                     
F356: 65 F2          ADC     $F2             
F358: A8             TAY                     
F359: BD 4C FF       LDA     $FF4C,X         
F35C: 49 FF          EOR     #$FF            
F35E: 31 F0          AND     ($F0),Y         
F360: F0 F2          BEQ     $F354           
F362: 20 8F FD       JSR     $FD8F           
F365: 88             DEY                     
F366: 20 8B FD       JSR     $FD8B           
F369: C8             INY                     
F36A: C8             INY                     
F36B: 20 8B FD       JSR     $FD8B           
F36E: A5 CA          LDA     $CA             
F370: 4A             LSR     A               
F371: B0 03          BCS     $F376           
F373: 4C 29 F4       JMP     $F429           
F376: 24 82          BIT     $82             
F378: 50 26          BVC     $F3A0           
F37A: A5 C8          LDA     $C8             
F37C: 29 39          AND     #$39            
F37E: C9 39          CMP     #$39            
F380: F0 1E          BEQ     $F3A0           
F382: A9 39          LDA     #$39            
F384: 85 C8          STA     $C8             
F386: A2 01          LDX     #$01            
F388: A5 98          LDA     $98             
F38A: 29 04          AND     #$04            
F38C: D0 01          BNE     $F38F           
F38E: CA             DEX                     
F38F: A9 04          LDA     #$04            
F391: 85 C6          STA     $C6             
F393: 4A             LSR     A               
F394: 24 DB          BIT     $DB             
F396: 50 01          BVC     $F399           
F398: 4A             LSR     A               
F399: 95 F4          STA     $F4,X           
F39B: A9 05          LDA     #$05            
F39D: 20 8B FE       JSR     $FE8B           
F3A0: A9 06          LDA     #$06            
F3A2: 85 F0          STA     $F0             
F3A4: C6 F0          DEC     $F0             
F3A6: 10 03          BPL     $F3AB           
F3A8: 4C CF F4       JMP     $F4CF           
F3AB: A6 F0          LDX     $F0             
F3AD: A5 82          LDA     $82             
F3AF: 3D DC FC       AND     $FCDC,X         
F3B2: F0 F0          BEQ     $F3A4           
F3B4: A0 01          LDY     #$01            
F3B6: A9 35          LDA     #$35            
F3B8: 38             SEC                     
F3B9: FD 31 FD       SBC     $FD31,X         
F3BC: 18             CLC                     
F3BD: 65 90          ADC     $90             
F3BF: C9 52          CMP     #$52            
F3C1: B0 63          BCS     $F426           
F3C3: C5 D5          CMP     $D5             
F3C5: B0 07          BCS     $F3CE           
F3C7: 69 0D          ADC     #$0D            
F3C9: C5 D5          CMP     $D5             
F3CB: 90 01          BCC     $F3CE           
F3CD: 88             DEY                     
F3CE: 84 EE          STY     $EE             
F3D0: A6 EE          LDX     $EE             
F3D2: A0 FF          LDY     #$FF            
F3D4: A5 9A          LDA     $9A             
F3D6: 18             CLC                     
F3D7: 69 FD          ADC     #$FD            
F3D9: C8             INY                     
F3DA: 69 10          ADC     #$10            
F3DC: D5 D7          CMP     $D7,X           
F3DE: 90 F9          BCC     $F3D9           
F3E0: 84 EF          STY     $EF             
F3E2: A6 F0          LDX     $F0             
F3E4: B9 DC FC       LDA     $FCDC,Y         
F3E7: 35 92          AND     $92,X           
F3E9: F0 3B          BEQ     $F426           
F3EB: 55 92          EOR     $92,X           
F3ED: 95 92          STA     $92,X           
F3EF: A4 EE          LDY     $EE             
F3F1: B9 DE FC       LDA     $FCDE,Y         
F3F4: A0 01          LDY     #$01            
F3F6: 25 98          AND     $98             
F3F8: D0 01          BNE     $F3FB           
F3FA: 88             DEY                     
F3FB: BD 2B FD       LDA     $FD2B,X         
F3FE: 99 F6 00       STA     $00F6,Y         
F401: A9 02          LDA     #$02            
F403: 20 7E FE       JSR     $FE7E           
F406: C6 91          DEC     $91             
F408: D0 0A          BNE     $F414           
F40A: A5 AA          LDA     $AA             
F40C: 09 08          ORA     #$08            
F40E: 85 AA          STA     $AA             
F410: A9 61          LDA     #$61            
F412: 85 CA          STA     $CA             
F414: 20 ED FB       JSR     $FBED           
F417: 8A             TXA                     
F418: 0A             ASL     A               
F419: 0A             ASL     A               
F41A: 0A             ASL     A               
F41B: 05 EF          ORA     $EF             
F41D: 85 C8          STA     $C8             
F41F: A9 F6          LDA     #$F6            
F421: A4 EE          LDY     $EE             
F423: 99 D5 00       STA     $00D5,Y         
F426: 4C A4 F3       JMP     $F3A4           
F429: 4A             LSR     A               
F42A: B0 2D          BCS     $F459           
F42C: A5 C8          LDA     $C8             
F42E: 29 39          AND     #$39            
F430: C9 39          CMP     #$39            
F432: F0 25          BEQ     $F459           
F434: A5 9E          LDA     $9E             
F436: C9 B4          CMP     #$B4            
F438: F0 1F          BEQ     $F459           
F43A: A5 98          LDA     $98             
F43C: 4A             LSR     A               
F43D: B0 06          BCS     $F445           
F43F: C6 9E          DEC     $9E             
F441: D0 16          BNE     $F459           
F443: F0 08          BEQ     $F44D           
F445: E6 9E          INC     $9E             
F447: A5 9E          LDA     $9E             
F449: C9 98          CMP     #$98            
F44B: 90 0C          BCC     $F459           
F44D: A9 B4          LDA     #$B4            
F44F: 85 9E          STA     $9E             
F451: A9 00          LDA     #$00            
F453: 85 CC          STA     $CC             
F455: A9 04          LDA     #$04            
F457: 85 C6          STA     $C6             
F459: AD 80 02       LDA     $0280           
F45C: A8             TAY                     
F45D: 0A             ASL     A               
F45E: 0A             ASL     A               
F45F: 0A             ASL     A               
F460: 0A             ASL     A               
F461: 85 EE          STA     $EE             
F463: 29 80          AND     #$80            
F465: 85 81          STA     $81             
F467: A5 DB          LDA     $DB             
F469: C9 90          CMP     #$90            
F46B: D0 08          BNE     $F475           
F46D: 24 AA          BIT     $AA             
F46F: 50 0E          BVC     $F47F           
F471: A4 EE          LDY     $EE             
F473: 70 0A          BVS     $F47F           
F475: 29 02          AND     #$02            
F477: F0 06          BEQ     $F47F           
F479: 98             TYA                     
F47A: 29 40          AND     #$40            
F47C: 05 81          ORA     $81             
F47E: A8             TAY                     
F47F: A2 01          LDX     #$01            
F481: A5 AA          LDA     $AA             
F483: 3D 60 FD       AND     $FD60,X         
F486: D0 18          BNE     $F4A0           
F488: 24 EE          BIT     $EE             
F48A: 30 02          BMI     $F48E           
F48C: F6 9C          INC     $9C,X           
F48E: 70 02          BVS     $F492           
F490: D6 9C          DEC     $9C,X           
F492: B5 9C          LDA     $9C,X           
F494: C9 76          CMP     #$76            
F496: 90 02          BCC     $F49A           
F498: D6 9C          DEC     $9C,X           
F49A: C9 23          CMP     #$23            
F49C: B0 02          BCS     $F4A0           
F49E: F6 9C          INC     $9C,X           
F4A0: 84 EE          STY     $EE             
F4A2: CA             DEX                     
F4A3: 10 DC          BPL     $F481           
F4A5: A5 CA          LDA     $CA             
F4A7: 4A             LSR     A               
F4A8: 4A             LSR     A               
F4A9: 4A             LSR     A               
F4AA: B0 23          BCS     $F4CF           
F4AC: A5 DC          LDA     $DC             
F4AE: 4A             LSR     A               
F4AF: 90 1E          BCC     $F4CF           
F4B1: A5 AA          LDA     $AA             
F4B3: 29 10          AND     #$10            
F4B5: F0 0A          BEQ     $F4C1           
F4B7: E6 9B          INC     $9B             
F4B9: A5 9B          LDA     $9B             
F4BB: C9 35          CMP     #$35            
F4BD: 90 10          BCC     $F4CF           
F4BF: B0 08          BCS     $F4C9           
F4C1: C6 9B          DEC     $9B             
F4C3: A5 9B          LDA     $9B             
F4C5: C9 21          CMP     #$21            
F4C7: B0 06          BCS     $F4CF           
F4C9: A5 AA          LDA     $AA             
F4CB: 49 10          EOR     #$10            
F4CD: 85 AA          STA     $AA             
F4CF: AD 84 02       LDA     $0284           
F4D2: D0 FB          BNE     $F4CF           
F4D4: A9 02          LDA     #$02            
F4D6: 85 01          STA     $01             
F4D8: 85 02          STA     $02             
F4DA: 24 AA          BIT     $AA             
F4DC: 30 13          BMI     $F4F1           
F4DE: F8             SED                     
F4DF: A2 01          LDX     #$01            
F4E1: B5 E8          LDA     $E8,X           
F4E3: 18             CLC                     
F4E4: 75 F6          ADC     $F6,X           
F4E6: 95 E8          STA     $E8,X           
F4E8: B5 E6          LDA     $E6,X           
F4EA: 75 F4          ADC     $F4,X           
F4EC: 95 E6          STA     $E6,X           
F4EE: CA             DEX                     
F4EF: 10 F0          BPL     $F4E1           
F4F1: D8             CLD                     
F4F2: 85 02          STA     $02             
F4F4: A5 CA          LDA     $CA             
F4F6: 29 07          AND     #$07            
F4F8: D0 12          BNE     $F50C           
F4FA: A5 C8          LDA     $C8             
F4FC: 18             CLC                     
F4FD: 69 40          ADC     #$40            
F4FF: 85 C8          STA     $C8             
F501: C9 40          CMP     #$40            
F503: B0 07          BCS     $F50C           
F505: 20 F1 FB       JSR     $FBF1           
F508: A9 30          LDA     #$30            
F50A: 85 C8          STA     $C8             
F50C: A9 02          LDA     #$02            
F50E: 85 02          STA     $02             
F510: 85 00          STA     $00             
F512: 85 02          STA     $02             
F514: 85 02          STA     $02             
F516: A9 30          LDA     #$30            
F518: 8D 96 02       STA     $0296           
F51B: A9 00          LDA     #$00            
F51D: 85 02          STA     $02             
F51F: 85 00          STA     $00             
F521: A5 CA          LDA     $CA             
F523: 4A             LSR     A               
F524: 90 23          BCC     $F549           
F526: A2 01          LDX     #$01            
F528: B5 D5          LDA     $D5,X           
F52A: C9 79          CMP     #$79            
F52C: D0 04          BNE     $F532           
F52E: A9 F6          LDA     #$F6            
F530: 95 D5          STA     $D5,X           
F532: B5 D5          LDA     $D5,X           
F534: C9 EC          CMP     #$EC            
F536: B0 0C          BCS     $F544           
F538: B5 D5          LDA     $D5,X           
F53A: 69 FE          ADC     #$FE            
F53C: C9 03          CMP     #$03            
F53E: B0 02          BCS     $F542           
F540: A9 F6          LDA     #$F6            
F542: 95 D5          STA     $D5,X           
F544: CA             DEX                     
F545: 10 E1          BPL     $F528           
F547: 30 59          BMI     $F5A2           
F549: A5 CA          LDA     $CA             
F54B: 29 0F          AND     #$0F            
F54D: C9 0F          CMP     #$0F            
F54F: F0 05          BEQ     $F556           
F551: 20 FB FD       JSR     $FDFB           
F554: 85 DA          STA     $DA             
F556: A5 DC          LDA     $DC             
F558: 29 04          AND     #$04            
F55A: 4A             LSR     A               
F55B: 4A             LSR     A               
F55C: 4A             LSR     A               
F55D: A9 01          LDA     #$01            
F55F: AA             TAX                     
F560: 90 01          BCC     $F563           
F562: 0A             ASL     A               
F563: 85 81          STA     $81             
F565: B5 D1          LDA     $D1,X           
F567: C9 EC          CMP     #$EC            
F569: B0 34          BCS     $F59F           
F56B: A5 DC          LDA     $DC             
F56D: 29 02          AND     #$02            
F56F: F0 1F          BEQ     $F590           
F571: A5 DA          LDA     $DA             
F573: E0 00          CPX     #$00            
F575: F0 02          BEQ     $F579           
F577: 0A             ASL     A               
F578: 0A             ASL     A               
F579: 0A             ASL     A               
F57A: 90 14          BCC     $F590           
F57C: 10 0A          BPL     $F588           
F57E: B5 D3          LDA     $D3,X           
F580: C9 81          CMP     #$81            
F582: B0 0C          BCS     $F590           
F584: F6 D3          INC     $D3,X           
F586: D0 08          BNE     $F590           
F588: B5 D3          LDA     $D3,X           
F58A: C9 17          CMP     #$17            
F58C: 90 02          BCC     $F590           
F58E: D6 D3          DEC     $D3,X           
F590: B5 D1          LDA     $D1,X           
F592: 18             CLC                     
F593: 65 81          ADC     $81             
F595: 95 D1          STA     $D1,X           
F597: C9 6C          CMP     #$6C            
F599: 90 04          BCC     $F59F           
F59B: A9 F6          LDA     #$F6            
F59D: 95 D1          STA     $D1,X           
F59F: CA             DEX                     
F5A0: 10 C3          BPL     $F565           
F5A2: C6 CA          DEC     $CA             
F5A4: F0 03          BEQ     $F5A9           
F5A6: 4C 8C F6       JMP     $F68C           
F5A9: A5 C7          LDA     $C7             
F5AB: F0 04          BEQ     $F5B1           
F5AD: E6 C7          INC     $C7             
F5AF: E6 C7          INC     $C7             
F5B1: 24 E5          BIT     $E5             
F5B3: 30 6D          BMI     $F622           
F5B5: A5 AA          LDA     $AA             
F5B7: 29 08          AND     #$08            
F5B9: F0 2A          BEQ     $F5E5           
F5BB: 45 AA          EOR     $AA             
F5BD: 85 AA          STA     $AA             
F5BF: A6 99          LDX     $99             
F5C1: BD 0F FD       LDA     $FD0F,X         
F5C4: 85 90          STA     $90             
F5C6: E0 03          CPX     #$03            
F5C8: B0 02          BCS     $F5CC           
F5CA: E6 99          INC     $99             
F5CC: 24 98          BIT     $98             
F5CE: 30 0F          BMI     $F5DF           
F5D0: 20 FA FE       JSR     $FEFA           
F5D3: A5 AA          LDA     $AA             
F5D5: 29 06          AND     #$06            
F5D7: D0 0C          BNE     $F5E5           
F5D9: A5 AA          LDA     $AA             
F5DB: 09 01          ORA     #$01            
F5DD: 85 AA          STA     $AA             
F5DF: A9 40          LDA     #$40            
F5E1: 85 CA          STA     $CA             
F5E3: D0 3A          BNE     $F61F           
F5E5: 24 98          BIT     $98             
F5E7: 10 0E          BPL     $F5F7           
F5E9: 24 A7          BIT     $A7             
F5EB: 30 22          BMI     $F60F           
F5ED: A5 DB          LDA     $DB             
F5EF: C9 10          CMP     #$10            
F5F1: D0 1C          BNE     $F60F           
F5F3: A9 00          LDA     #$00            
F5F5: F0 31          BEQ     $F628           
F5F7: A5 AA          LDA     $AA             
F5F9: 29 01          AND     #$01            
F5FB: F0 25          BEQ     $F622           
F5FD: 45 AA          EOR     $AA             
F5FF: 85 AA          STA     $AA             
F601: A9 50          LDA     #$50            
F603: 85 D9          STA     $D9             
F605: A9 05          LDA     #$05            
F607: 85 C6          STA     $C6             
F609: A5 C9          LDA     $C9             
F60B: D0 4F          BNE     $F65C           
F60D: E6 C9          INC     $C9             
F60F: A5 E5          LDA     $E5             
F611: 09 80          ORA     #$80            
F613: 85 E5          STA     $E5             
F615: A5 C7          LDA     $C7             
F617: D0 09          BNE     $F622           
F619: A9 BF          LDA     #$BF            
F61B: 85 C7          STA     $C7             
F61D: 10 03          BPL     $F622           
F61F: 4C 89 F6       JMP     $F689           
F622: A5 AA          LDA     $AA             
F624: 29 06          AND     #$06            
F626: F0 40          BEQ     $F668           
F628: 09 01          ORA     #$01            
F62A: 45 AA          EOR     $AA             
F62C: 85 AA          STA     $AA             
F62E: A9 23          LDA     #$23            
F630: 85 9C          STA     $9C             
F632: A9 75          LDA     #$75            
F634: 85 9D          STA     $9D             
F636: A5 DB          LDA     $DB             
F638: C9 10          CMP     #$10            
F63A: D0 1E          BNE     $F65A           
F63C: 24 A7          BIT     $A7             
F63E: 30 1A          BMI     $F65A           
F640: A2 0A          LDX     #$0A            
F642: B4 90          LDY     $90,X           
F644: B5 9F          LDA     $9F,X           
F646: 95 90          STA     $90,X           
F648: 94 9F          STY     $9F,X           
F64A: CA             DEX                     
F64B: 10 F5          BPL     $F642           
F64D: 20 3A FF       JSR     $FF3A           
F650: A5 AA          LDA     $AA             
F652: 49 40          EOR     #$40            
F654: 85 AA          STA     $AA             
F656: 29 40          AND     #$40            
F658: D0 02          BNE     $F65C           
F65A: C6 C9          DEC     $C9             
F65C: A9 40          LDA     #$40            
F65E: 85 CA          STA     $CA             
F660: A9 B4          LDA     #$B4            
F662: 85 9E          STA     $9E             
F664: A9 00          LDA     #$00            
F666: 85 CC          STA     $CC             
F668: C6 C6          DEC     $C6             
F66A: D0 1D          BNE     $F689           
F66C: A5 91          LDA     $91             
F66E: C9 07          CMP     #$07            
F670: 90 17          BCC     $F689           
F672: 20 FB FD       JSR     $FDFB           
F675: 29 01          AND     #$01            
F677: 45 98          EOR     $98             
F679: 85 98          STA     $98             
F67B: 4A             LSR     A               
F67C: A9 98          LDA     #$98            
F67E: 90 02          BCC     $F682           
F680: A9 00          LDA     #$00            
F682: 85 9E          STA     $9E             
F684: A9 04          LDA     #$04            
F686: 20 8B FE       JSR     $FE8B           
F689: 4C 75 F8       JMP     $F875           
F68C: A5 CA          LDA     $CA             
F68E: 4A             LSR     A               
F68F: B0 03          BCS     $F694           
F691: 4C DB F7       JMP     $F7DB           
F694: AD 82 02       LDA     $0282           
F697: 29 03          AND     #$03            
F699: C9 02          CMP     #$02            
F69B: D0 06          BNE     $F6A3           
F69D: 20 B2 FE       JSR     $FEB2           
F6A0: 4C 44 F7       JMP     $F744           
F6A3: AD 82 02       LDA     $0282           
F6A6: 29 02          AND     #$02            
F6A8: F0 09          BEQ     $F6B3           
F6AA: A5 AA          LDA     $AA             
F6AC: 85 ED          STA     $ED             
F6AE: 30 3E          BMI     $F6EE           
F6B0: 4C 47 F7       JMP     $F747           
F6B3: A9 B1          LDA     #$B1            
F6B5: 85 C7          STA     $C7             
F6B7: 24 AA          BIT     $AA             
F6B9: 30 0E          BMI     $F6C9           
F6BB: A5 AA          LDA     $AA             
F6BD: 29 B0          AND     #$B0            
F6BF: 09 80          ORA     #$80            
F6C1: 85 ED          STA     $ED             
F6C3: 20 C0 FE       JSR     $FEC0           
F6C6: 4C 44 F7       JMP     $F744           
F6C9: E6 ED          INC     $ED             
F6CB: A5 ED          LDA     $ED             
F6CD: C9 0F          CMP     #$0F            
F6CF: 90 1D          BCC     $F6EE           
F6D1: AD 82 02       LDA     $0282           
F6D4: 4A             LSR     A               
F6D5: A9 0D          LDA     #$0D            
F6D7: 90 02          BCC     $F6DB           
F6D9: A9 02          LDA     #$02            
F6DB: 85 ED          STA     $ED             
F6DD: A5 98          LDA     $98             
F6DF: 29 F3          AND     #$F3            
F6E1: 85 98          STA     $98             
F6E3: A5 DC          LDA     $DC             
F6E5: 18             CLC                     
F6E6: 69 91          ADC     #$91            
F6E8: F0 02          BEQ     $F6EC           
F6EA: 69 70          ADC     #$70            
F6EC: 85 DC          STA     $DC             
F6EE: A5 AA          LDA     $AA             
F6F0: 09 80          ORA     #$80            
F6F2: 85 AA          STA     $AA             
F6F4: A5 DC          LDA     $DC             
F6F6: 4A             LSR     A               
F6F7: 4A             LSR     A               
F6F8: 4A             LSR     A               
F6F9: 4A             LSR     A               
F6FA: 85 EC          STA     $EC             
F6FC: A8             TAY                     
F6FD: B9 4B FD       LDA     $FD4B,Y         
F700: 85 DB          STA     $DB             
F702: A5 98          LDA     $98             
F704: 29 CF          AND     #$CF            
F706: 19 52 FD       ORA     $FD52,Y         
F709: 85 98          STA     $98             
F70B: A9 AA          LDA     #$AA            
F70D: 85 E7          STA     $E7             
F70F: A9 A2          LDA     #$A2            
F711: 85 E9          STA     $E9             
F713: A0 00          LDY     #$00            
F715: 98             TYA                     
F716: 38             SEC                     
F717: 65 DC          ADC     $DC             
F719: C9 0A          CMP     #$0A            
F71B: 90 06          BCC     $F723           
F71D: C8             INY                     
F71E: E9 0A          SBC     #$0A            
F720: 4C 19 F7       JMP     $F719           
F723: 79 39 FD       ADC     $FD39,Y         
F726: 85 E8          STA     $E8             
F728: A5 DC          LDA     $DC             
F72A: C9 63          CMP     #$63            
F72C: A9 AA          LDA     #$AA            
F72E: 90 02          BCC     $F732           
F730: A9 A1          LDA     #$A1            
F732: 85 E6          STA     $E6             
F734: A5 DC          LDA     $DC             
F736: C9 10          CMP     #$10            
F738: B0 02          BCS     $F73C           
F73A: C6 E9          DEC     $E9             
F73C: C9 09          CMP     #$09            
F73E: B0 04          BCS     $F744           
F740: 69 A1          ADC     #$A1            
F742: 85 E8          STA     $E8             
F744: 4C 75 F8       JMP     $F875           
F747: A5 CA          LDA     $CA             
F749: 4A             LSR     A               
F74A: B0 03          BCS     $F74F           
F74C: 4C DB F7       JMP     $F7DB           
F74F: A5 C7          LDA     $C7             
F751: D0 F9          BNE     $F74C           
F753: 24 98          BIT     $98             
F755: 30 12          BMI     $F769           
F757: A5 AA          LDA     $AA             
F759: 29 07          AND     #$07            
F75B: D0 0C          BNE     $F769           
F75D: A5 DB          LDA     $DB             
F75F: 29 10          AND     #$10            
F761: F0 58          BEQ     $F7BB           
F763: A5 D5          LDA     $D5             
F765: C9 EC          CMP     #$EC            
F767: B0 03          BCS     $F76C           
F769: 4C D8 F7       JMP     $F7D8           
F76C: A5 DB          LDA     $DB             
F76E: C9 14          CMP     #$14            
F770: F0 08          BEQ     $F77A           
F772: C9 90          CMP     #$90            
F774: D0 09          BNE     $F77F           
F776: 24 AA          BIT     $AA             
F778: 50 21          BVC     $F79B           
F77A: 24 0D          BIT     $0D             
F77C: 4C 9D F7       JMP     $F79D           
F77F: A5 DB          LDA     $DB             
F781: 10 0A          BPL     $F78D           
F783: C6 D9          DEC     $D9             
F785: D0 06          BNE     $F78D           
F787: 24 AA          BIT     $AA             
F789: 50 14          BVC     $F79F           
F78B: 70 1E          BVS     $F7AB           
F78D: 24 AA          BIT     $AA             
F78F: 70 16          BVS     $F7A7           
F791: A5 DB          LDA     $DB             
F793: 29 20          AND     #$20            
F795: F0 04          BEQ     $F79B           
F797: 24 0D          BIT     $0D             
F799: 10 04          BPL     $F79F           
F79B: 24 0C          BIT     $0C             
F79D: 30 39          BMI     $F7D8           
F79F: A5 98          LDA     $98             
F7A1: 29 FB          AND     #$FB            
F7A3: A2 00          LDX     #$00            
F7A5: 10 0A          BPL     $F7B1           
F7A7: 24 0D          BIT     $0D             
F7A9: 30 2D          BMI     $F7D8           
F7AB: A2 01          LDX     #$01            
F7AD: A5 98          LDA     $98             
F7AF: 09 04          ORA     #$04            
F7B1: 85 98          STA     $98             
F7B3: A0 00          LDY     #$00            
F7B5: 20 AF FB       JSR     $FBAF           
F7B8: 4C D8 F7       JMP     $F7D8           
F7BB: A0 01          LDY     #$01            
F7BD: A2 01          LDX     #$01            
F7BF: A5 98          LDA     $98             
F7C1: 39 DE FC       AND     $FCDE,Y         
F7C4: D0 01          BNE     $F7C7           
F7C6: CA             DEX                     
F7C7: B9 D5 00       LDA     $00D5,Y         
F7CA: C9 EC          CMP     #$EC            
F7CC: 90 07          BCC     $F7D5           
F7CE: B5 0C          LDA     $0C,X           
F7D0: 30 03          BMI     $F7D5           
F7D2: 20 AF FB       JSR     $FBAF           
F7D5: 88             DEY                     
F7D6: 10 E5          BPL     $F7BD           
F7D8: 4C 75 F8       JMP     $F875           
F7DB: A5 AA          LDA     $AA             
F7DD: 29 07          AND     #$07            
F7DF: D0 F7          BNE     $F7D8           
F7E1: A8             TAY                     
F7E2: A5 91          LDA     $91             
F7E4: F0 F2          BEQ     $F7D8           
F7E6: A9 EB          LDA     #$EB            
F7E8: 85 EE          STA     $EE             
F7EA: C5 D2          CMP     $D2             
F7EC: B0 EA          BCS     $F7D8           
F7EE: 20 FB FD       JSR     $FDFB           
F7F1: 10 1A          BPL     $F80D           
F7F3: 29 03          AND     #$03            
F7F5: 0A             ASL     A               
F7F6: 85 EE          STA     $EE             
F7F8: A5 EA          LDA     $EA             
F7FA: 4A             LSR     A               
F7FB: 4A             LSR     A               
F7FC: AA             TAX                     
F7FD: 8A             TXA                     
F7FE: 38             SEC                     
F7FF: 65 EE          ADC     $EE             
F801: 29 07          AND     #$07            
F803: AA             TAX                     
F804: BD DC FC       LDA     $FCDC,X         
F807: 25 EB          AND     $EB             
F809: F0 F2          BEQ     $F7FD           
F80B: D0 2F          BNE     $F83C           
F80D: A5 98          LDA     $98             
F80F: 29 04          AND     #$04            
F811: F0 01          BEQ     $F814           
F813: C8             INY                     
F814: A2 05          LDX     #$05            
F816: BD DC FC       LDA     $FCDC,X         
F819: 25 EB          AND     $EB             
F81B: F0 10          BEQ     $F82D           
F81D: A5 9A          LDA     $9A             
F81F: 18             CLC                     
F820: 69 FD          ADC     #$FD            
F822: 18             CLC                     
F823: 7D 39 FD       ADC     $FD39,X         
F826: D9 9C 00       CMP     $009C,Y         
F829: 90 06          BCC     $F831           
F82B: 86 EE          STX     $EE             
F82D: CA             DEX                     
F82E: 10 E6          BPL     $F816           
F830: E8             INX                     
F831: A5 EA          LDA     $EA             
F833: 29 10          AND     #$10            
F835: D0 05          BNE     $F83C           
F837: A5 EE          LDA     $EE             
F839: 30 01          BMI     $F83C           
F83B: AA             TAX                     
F83C: 86 EF          STX     $EF             
F83E: BD DC FC       LDA     $FCDC,X         
F841: 85 F0          STA     $F0             
F843: A2 FF          LDX     #$FF            
F845: E8             INX                     
F846: E0 06          CPX     #$06            
F848: B0 2B          BCS     $F875           
F84A: B5 92          LDA     $92,X           
F84C: 25 F0          AND     $F0             
F84E: F0 F5          BEQ     $F845           
F850: A9 3C          LDA     #$3C            
F852: 65 90          ADC     $90             
F854: FD 31 FD       SBC     $FD31,X         
F857: 85 D2          STA     $D2             
F859: 38             SEC                     
F85A: E5 D1          SBC     $D1             
F85C: C9 10          CMP     #$10            
F85E: 90 11          BCC     $F871           
F860: C9 F1          CMP     #$F1            
F862: B0 0D          BCS     $F871           
F864: A4 EF          LDY     $EF             
F866: A5 9A          LDA     $9A             
F868: 79 39 FD       ADC     $FD39,Y         
F86B: 69 04          ADC     #$04            
F86D: 85 D4          STA     $D4             
F86F: D0 04          BNE     $F875           
F871: A9 F6          LDA     #$F6            
F873: 85 D2          STA     $D2             
F875: A5 AA          LDA     $AA             
F877: 29 07          AND     #$07            
F879: D0 7A          BNE     $F8F5           
F87B: 24 98          BIT     $98             
F87D: 30 76          BMI     $F8F5           
F87F: A0 FF          LDY     #$FF            
F881: A5 91          LDA     $91             
F883: F0 70          BEQ     $F8F5           
F885: C8             INY                     
F886: D9 E4 FC       CMP     $FCE4,Y         
F889: 90 FA          BCC     $F885           
F88B: B9 F6 FC       LDA     $FCF6,Y         
F88E: 85 EE          STA     $EE             
F890: B9 ED FC       LDA     $FCED,Y         
F893: 85 EF          STA     $EF             
F895: A5 CA          LDA     $CA             
F897: 29 3F          AND     #$3F            
F899: 85 F0          STA     $F0             
F89B: 18             CLC                     
F89C: 65 EF          ADC     $EF             
F89E: C9 41          CMP     #$41            
F8A0: B0 53          BCS     $F8F5           
F8A2: A5 F0          LDA     $F0             
F8A4: F0 09          BEQ     $F8AF           
F8A6: C5 EF          CMP     $EF             
F8A8: 90 4B          BCC     $F8F5           
F8AA: E5 EF          SBC     $EF             
F8AC: 4C A4 F8       JMP     $F8A4           
F8AF: 24 8B          BIT     $8B             
F8B1: A9 09          LDA     #$09            
F8B3: 70 02          BVS     $F8B7           
F8B5: A9 FF          LDA     #$FF            
F8B7: 85 8B          STA     $8B             
F8B9: A9 01          LDA     #$01            
F8BB: 20 7E FE       JSR     $FE7E           
F8BE: A5 98          LDA     $98             
F8C0: 29 02          AND     #$02            
F8C2: F0 0F          BEQ     $F8D3           
F8C4: A5 9A          LDA     $9A             
F8C6: 18             CLC                     
F8C7: 65 EE          ADC     $EE             
F8C9: 85 9A          STA     $9A             
F8CB: C5 8D          CMP     $8D             
F8CD: 90 26          BCC     $F8F5           
F8CF: A5 8D          LDA     $8D             
F8D1: D0 0D          BNE     $F8E0           
F8D3: A5 9A          LDA     $9A             
F8D5: 38             SEC                     
F8D6: E5 EE          SBC     $EE             
F8D8: 85 9A          STA     $9A             
F8DA: C9 17          CMP     #$17            
F8DC: B0 17          BCS     $F8F5           
F8DE: A9 17          LDA     #$17            
F8E0: 85 9A          STA     $9A             
F8E2: A5 98          LDA     $98             
F8E4: 49 02          EOR     #$02            
F8E6: 85 98          STA     $98             
F8E8: 30 0B          BMI     $F8F5           
F8EA: 24 AA          BIT     $AA             
F8EC: 30 07          BMI     $F8F5           
F8EE: A5 90          LDA     $90             
F8F0: 18             CLC                     
F8F1: 69 05          ADC     #$05            
F8F3: 85 90          STA     $90             
F8F5: A9 05          LDA     #$05            
F8F7: 85 8C          STA     $8C             
F8F9: A9 0B          LDA     #$0B            
F8FB: 38             SEC                     
F8FC: E5 90          SBC     $90             
F8FE: 85 8E          STA     $8E             
F900: 24 98          BIT     $98             
F902: 70 07          BVS     $F90B           
F904: A5 8E          LDA     $8E             
F906: 18             CLC                     
F907: 69 0C          ADC     #$0C            
F909: 85 8E          STA     $8E             
F90B: A2 FB          LDX     #$FB            
F90D: B5 97          LDA     $97,X           
F90F: D0 0C          BNE     $F91D           
F911: C6 8C          DEC     $8C             
F913: A5 8E          LDA     $8E             
F915: 18             CLC                     
F916: 69 09          ADC     #$09            
F918: 85 8E          STA     $8E             
F91A: E8             INX                     
F91B: D0 F0          BNE     $F90D           
F91D: A5 8E          LDA     $8E             
F91F: 10 31          BPL     $F952           
F921: A5 98          LDA     $98             
F923: 29 40          AND     #$40            
F925: F0 0D          BEQ     $F934           
F927: 45 98          EOR     $98             
F929: 85 98          STA     $98             
F92B: A5 8E          LDA     $8E             
F92D: 18             CLC                     
F92E: 69 0C          ADC     #$0C            
F930: 85 8E          STA     $8E             
F932: 10 1E          BPL     $F952           
F934: A9 00          LDA     #$00            
F936: 85 8E          STA     $8E             
F938: A5 98          LDA     $98             
F93A: 30 16          BMI     $F952           
F93C: 09 80          ORA     #$80            
F93E: 85 98          STA     $98             
F940: A4 8C          LDY     $8C             
F942: A5 90          LDA     $90             
F944: 18             CLC                     
F945: 79 F2 FF       ADC     $FFF2,Y         
F948: 85 90          STA     $90             
F94A: 20 75 FE       JSR     $FE75           
F94D: A9 06          LDA     #$06            
F94F: 20 7E FE       JSR     $FE7E           
F952: A2 05          LDX     #$05            
F954: A9 00          LDA     #$00            
F956: 15 92          ORA     $92,X           
F958: CA             DEX                     
F959: 10 FB          BPL     $F956           
F95B: 85 EB          STA     $EB             
F95D: A5 EB          LDA     $EB             
F95F: F0 2D          BEQ     $F98E           
F961: 4A             LSR     A               
F962: B0 18          BCS     $F97C           
F964: 20 ED FB       JSR     $FBED           
F967: A9 3A          LDA     #$3A            
F969: 85 C8          STA     $C8             
F96B: A2 05          LDX     #$05            
F96D: 56 92          LSR     $92,X           
F96F: CA             DEX                     
F970: 10 FB          BPL     $F96D           
F972: A5 9A          LDA     $9A             
F974: 69 10          ADC     #$10            
F976: 85 9A          STA     $9A             
F978: 46 EB          LSR     $EB             
F97A: D0 E1          BNE     $F95D           
F97C: A2 06          LDX     #$06            
F97E: CA             DEX                     
F97F: BD DC FC       LDA     $FCDC,X         
F982: 25 EB          AND     $EB             
F984: F0 F8          BEQ     $F97E           
F986: A9 82          LDA     #$82            
F988: 38             SEC                     
F989: FD 39 FD       SBC     $FD39,X         
F98C: 85 8D          STA     $8D             
F98E: A5 90          LDA     $90             
F990: 85 8F          STA     $8F             
F992: A2 04          LDX     #$04            
F994: B5 99          LDA     $99,X           
F996: 20 67 FD       JSR     $FD67           
F999: CA             DEX                     
F99A: D0 F8          BNE     $F994           
F99C: AD 82 02       LDA     $0282           
F99F: 29 08          AND     #$08            
F9A1: A8             TAY                     
F9A2: F0 02          BEQ     $F9A6           
F9A4: A9 F7          LDA     #$F7            
F9A6: 09 07          ORA     #$07            
F9A8: 85 EE          STA     $EE             
F9AA: A2 F8          LDX     #$F8            
F9AC: B9 FF FC       LDA     $FCFF,Y         
F9AF: 45 C7          EOR     $C7             
F9B1: 25 EE          AND     $EE             
F9B3: 95 E5          STA     $E5,X           
F9B5: C8             INY                     
F9B6: E8             INX                     
F9B7: 30 F3          BMI     $F9AC           
F9B9: 24 AA          BIT     $AA             
F9BB: 30 04          BMI     $F9C1           
F9BD: A5 C7          LDA     $C7             
F9BF: D0 12          BNE     $F9D3           
F9C1: A5 C8          LDA     $C8             
F9C3: 29 38          AND     #$38            
F9C5: C9 30          CMP     #$30            
F9C7: D0 0A          BNE     $F9D3           
F9C9: A5 DC          LDA     $DC             
F9CB: 29 08          AND     #$08            
F9CD: F0 04          BEQ     $F9D3           
F9CF: A5 E3          LDA     $E3             
F9D1: 85 E1          STA     $E1             
F9D3: A5 DE          LDA     $DE             
F9D5: 85 06          STA     $06             
F9D7: A5 E3          LDA     $E3             
F9D9: 85 09          STA     $09             
F9DB: A5 E2          LDA     $E2             
F9DD: 85 08          STA     $08             
F9DF: A5 CA          LDA     $CA             
F9E1: 4A             LSR     A               
F9E2: A2 04          LDX     #$04            
F9E4: B0 02          BCS     $F9E8           
F9E6: A2 00          LDX     #$00            
F9E8: 86 EF          STX     $EF             
F9EA: B5 D1          LDA     $D1,X           
F9EC: D5 D2          CMP     $D2,X           
F9EE: 90 2B          BCC     $FA1B           
F9F0: 85 81          STA     $81             
F9F2: B5 D2          LDA     $D2,X           
F9F4: 95 D1          STA     $D1,X           
F9F6: A5 81          LDA     $81             
F9F8: 95 D2          STA     $D2,X           
F9FA: B5 D3          LDA     $D3,X           
F9FC: 85 81          STA     $81             
F9FE: B5 D4          LDA     $D4,X           
FA00: 95 D3          STA     $D3,X           
FA02: A5 81          LDA     $81             
FA04: 95 D4          STA     $D4,X           
FA06: A5 CA          LDA     $CA             
FA08: 4A             LSR     A               
FA09: 90 10          BCC     $FA1B           
FA0B: A5 98          LDA     $98             
FA0D: 29 0C          AND     #$0C            
FA0F: 4A             LSR     A               
FA10: 4A             LSR     A               
FA11: A8             TAY                     
FA12: A5 98          LDA     $98             
FA14: 29 F3          AND     #$F3            
FA16: 19 1A FD       ORA     $FD1A,Y         
FA19: 85 98          STA     $98             
FA1B: B5 D4          LDA     $D4,X           
FA1D: A2 05          LDX     #$05            
FA1F: 20 67 FD       JSR     $FD67           
FA22: A6 EF          LDX     $EF             
FA24: B5 D1          LDA     $D1,X           
FA26: 85 89          STA     $89             
FA28: B5 D2          LDA     $D2,X           
FA2A: C9 EC          CMP     #$EC            
FA2C: B0 03          BCS     $FA31           
FA2E: 38             SEC                     
FA2F: F5 D1          SBC     $D1,X           
FA31: 85 8A          STA     $8A             
FA33: B5 D3          LDA     $D3,X           
FA35: A2 00          LDX     #$00            
FA37: 20 67 FD       JSR     $FD67           
FA3A: A2 04          LDX     #$04            
FA3C: 20 7E FD       JSR     $FD7E           
FA3F: 85 02          STA     $02             
FA41: 85 2A          STA     $2A             
FA43: AD 84 02       LDA     $0284           
FA46: D0 FB          BNE     $FA43           
FA48: 85 01          STA     $01             
FA4A: 85 2C          STA     $2C             
FA4C: A2 00          LDX     #$00            
FA4E: A9 EA          LDA     #$EA            
FA50: 85 02          STA     $02             
FA52: 8D 96 02       STA     $0296           
FA55: 85 2B          STA     $2B             
FA57: 24 AA          BIT     $AA             
FA59: 30 09          BMI     $FA64           
FA5B: A5 9E          LDA     $9E             
FA5D: C9 B4          CMP     #$B4            
FA5F: F0 03          BEQ     $FA64           
FA61: 4C 0D FB       JMP     $FB0D           
FA64: A2 07          LDX     #$07            
FA66: A0 03          LDY     #$03            
FA68: B9 E6 00       LDA     $00E6,Y         
FA6B: 29 0F          AND     #$0F            
FA6D: 85 F0          STA     $F0             
FA6F: 0A             ASL     A               
FA70: 0A             ASL     A               
FA71: 65 F0          ADC     $F0             
FA73: 69 54          ADC     #$54            
FA75: 95 F0          STA     $F0,X           
FA77: CA             DEX                     
FA78: B9 E6 00       LDA     $00E6,Y         
FA7B: 4A             LSR     A               
FA7C: 4A             LSR     A               
FA7D: 4A             LSR     A               
FA7E: 4A             LSR     A               
FA7F: 85 F0          STA     $F0             
FA81: 0A             ASL     A               
FA82: 0A             ASL     A               
FA83: 65 F0          ADC     $F0             
FA85: 69 54          ADC     #$54            
FA87: 95 F0          STA     $F0,X           
FA89: CA             DEX                     
FA8A: 88             DEY                     
FA8B: 10 DB          BPL     $FA68           
FA8D: 85 02          STA     $02             
FA8F: A5 DF          LDA     $DF             
FA91: 85 06          STA     $06             
FA93: A9 02          LDA     #$02            
FA95: 85 0A          STA     $0A             
FA97: A5 E0          LDA     $E0             
FA99: 85 07          STA     $07             
FA9B: A9 04          LDA     #$04            
FA9D: 85 EE          STA     $EE             
FA9F: A9 FF          LDA     #$FF            
FAA1: 85 EF          STA     $EF             
FAA3: EA             NOP                     
FAA4: EA             NOP                     
FAA5: A2 05          LDX     #$05            
FAA7: CA             DEX                     
FAA8: 10 FD          BPL     $FAA7           
FAAA: A4 F0          LDY     $F0             
FAAC: B1 EE          LDA     ($EE),Y         
FAAE: 85 0D          STA     $0D             
FAB0: A9 00          LDA     #$00            
FAB2: 85 0E          STA     $0E             
FAB4: A4 F5          LDY     $F5             
FAB6: B1 EE          LDA     ($EE),Y         
FAB8: 4A             LSR     A               
FAB9: 4A             LSR     A               
FABA: 4A             LSR     A               
FABB: 4A             LSR     A               
FABC: 85 0F          STA     $0F             
FABE: A4 F2          LDY     $F2             
FAC0: B1 EE          LDA     ($EE),Y         
FAC2: 85 0D          STA     $0D             
FAC4: A4 F7          LDY     $F7             
FAC6: B1 EE          LDA     ($EE),Y         
FAC8: 4A             LSR     A               
FAC9: 4A             LSR     A               
FACA: 4A             LSR     A               
FACB: 4A             LSR     A               
FACC: 85 0F          STA     $0F             
FACE: A4 F4          LDY     $F4             
FAD0: B1 EE          LDA     ($EE),Y         
FAD2: 29 0F          AND     #$0F            
FAD4: 85 81          STA     $81             
FAD6: A4 F1          LDY     $F1             
FAD8: B1 EE          LDA     ($EE),Y         
FADA: 0A             ASL     A               
FADB: 0A             ASL     A               
FADC: 0A             ASL     A               
FADD: 0A             ASL     A               
FADE: 05 81          ORA     $81             
FAE0: 85 0E          STA     $0E             
FAE2: A9 00          LDA     #$00            
FAE4: 85 0D          STA     $0D             
FAE6: 85 0F          STA     $0F             
FAE8: A4 F6          LDY     $F6             
FAEA: B1 EE          LDA     ($EE),Y         
FAEC: 29 0F          AND     #$0F            
FAEE: 85 81          STA     $81             
FAF0: A4 F3          LDY     $F3             
FAF2: B1 EE          LDA     ($EE),Y         
FAF4: 0A             ASL     A               
FAF5: 0A             ASL     A               
FAF6: 0A             ASL     A               
FAF7: 0A             ASL     A               
FAF8: 05 81          ORA     $81             
FAFA: 85 0E          STA     $0E             
FAFC: C6 EE          DEC     $EE             
FAFE: 10 AA          BPL     $FAAA           
FB00: A5 89          LDA     $89             
FB02: 18             CLC                     
FB03: 69 F9          ADC     #$F9            
FB05: 85 89          STA     $89             
FB07: A9 00          LDA     #$00            
FB09: 85 0E          STA     $0E             
FB0B: F0 48          BEQ     $FB55           
FB0D: 20 67 FD       JSR     $FD67           
FB10: 20 7E FD       JSR     $FD7E           
FB13: 20 E9 FD       JSR     $FDE9           
FB16: A9 A0          LDA     #$A0            
FB18: 85 EE          STA     $EE             
FB1A: A9 FC          LDA     #$FC            
FB1C: 85 EF          STA     $EF             
FB1E: A9 00          LDA     #$00            
FB20: 85 04          STA     $04             
FB22: 85 02          STA     $02             
FB24: 85 2A          STA     $2A             
FB26: A5 C8          LDA     $C8             
FB28: 29 39          AND     #$39            
FB2A: C9 39          CMP     #$39            
FB2C: D0 0E          BNE     $FB3C           
FB2E: A5 C8          LDA     $C8             
FB30: 2A             ROL     A               
FB31: 2A             ROL     A               
FB32: 2A             ROL     A               
FB33: 2A             ROL     A               
FB34: 29 03          AND     #$03            
FB36: A8             TAY                     
FB37: B9 1E FD       LDA     $FD1E,Y         
FB3A: 85 EE          STA     $EE             
FB3C: 85 02          STA     $02             
FB3E: 85 2B          STA     $2B             
FB40: 20 E9 FD       JSR     $FDE9           
FB43: A0 09          LDY     #$09            
FB45: 85 02          STA     $02             
FB47: B1 EE          LDA     ($EE),Y         
FB49: 85 1B          STA     $1B             
FB4B: 98             TYA                     
FB4C: 4A             LSR     A               
FB4D: B0 03          BCS     $FB52           
FB4F: 20 E9 FD       JSR     $FDE9           
FB52: 88             DEY                     
FB53: 10 F0          BPL     $FB45           
FB55: A9 00          LDA     #$00            
FB57: 85 02          STA     $02             
FB59: 85 1B          STA     $1B             
FB5B: A5 84          LDA     $84             
FB5D: 85 21          STA     $21             
FB5F: 85 20          STA     $20             
FB61: 29 0F          AND     #$0F            
FB63: A8             TAY                     
FB64: 88             DEY                     
FB65: 10 FD          BPL     $FB64           
FB67: 85 10          STA     $10             
FB69: A9 06          LDA     #$06            
FB6B: 85 11          STA     $11             
FB6D: 85 02          STA     $02             
FB6F: 85 2A          STA     $2A             
FB71: 85 04          STA     $04             
FB73: 85 05          STA     $05             
FB75: A2 0A          LDX     #$0A            
FB77: A9 FC          LDA     #$FC            
FB79: 95 EF          STA     $EF,X           
FB7B: CA             DEX                     
FB7C: CA             DEX                     
FB7D: 10 FA          BPL     $FB79           
FB7F: 20 E9 FD       JSR     $FDE9           
FB82: A5 02          LDA     $02             
FB84: 29 40          AND     #$40            
FB86: 85 82          STA     $82             
FB88: 85 2C          STA     $2C             
FB8A: 85 2B          STA     $2B             
FB8C: A9 F0          LDA     #$F0            
FB8E: 85 21          STA     $21             
FB90: 85 02          STA     $02             
FB92: 85 2A          STA     $2A             
FB94: A5 E1          LDA     $E1             
FB96: 85 06          STA     $06             
FB98: 85 07          STA     $07             
FB9A: C6 8F          DEC     $8F             
FB9C: 10 0B          BPL     $FBA9           
FB9E: A0 05          LDY     #$05            
FBA0: A9 01          LDA     #$01            
FBA2: 85 25          STA     $25             
FBA4: 85 26          STA     $26             
FBA6: 4C A5 F0       JMP     $F0A5           
FBA9: 20 B2 FD       JSR     $FDB2           
FBAC: 4C 9A FB       JMP     $FB9A           
FBAF: 86 F2          STX     $F2             
FBB1: BE 38 FD       LDX     $FD38,Y         
FBB4: B5 D5          LDA     $D5,X           
FBB6: C9 56          CMP     #$56            
FBB8: B0 04          BCS     $FBBE           
FBBA: C9 45          CMP     #$45            
FBBC: B0 2E          BCS     $FBEC           
FBBE: A6 F2          LDX     $F2             
FBC0: A9 55          LDA     #$55            
FBC2: 99 D5 00       STA     $00D5,Y         
FBC5: BD E2 FC       LDA     $FCE2,X         
FBC8: 2D 82 02       AND     $0282           
FBCB: 18             CLC                     
FBCC: F0 02          BEQ     $FBD0           
FBCE: A9 04          LDA     #$04            
FBD0: 69 05          ADC     #$05            
FBD2: 75 9C          ADC     $9C,X           
FBD4: 99 D7 00       STA     $00D7,Y         
FBD7: A9 03          LDA     #$03            
FBD9: 20 8B FE       JSR     $FE8B           
FBDC: A5 DB          LDA     $DB             
FBDE: 29 80          AND     #$80            
FBE0: F0 0A          BEQ     $FBEC           
FBE2: A5 AA          LDA     $AA             
FBE4: 49 40          EOR     #$40            
FBE6: 85 AA          STA     $AA             
FBE8: A9 50          LDA     #$50            
FBEA: 85 D9          STA     $D9             
FBEC: 60             RTS                     
FBED: A5 C8          LDA     $C8             
FBEF: 29 39          AND     #$39            
FBF1: C9 39          CMP     #$39            
FBF3: D0 08          BNE     $FBFD           
FBF5: A9 B4          LDA     #$B4            
FBF7: 85 9E          STA     $9E             
FBF9: A9 00          LDA     #$00            
FBFB: 85 CC          STA     $CC             
FBFD: 60             RTS                     
FBFE: 00             BRK                     
FBFF: 00             BRK                     
FC00: 00             BRK                     
FC01: 00             BRK                     
FC02: 00             BRK                     
FC03: 00             BRK                     
FC04: 00             BRK                     
FC05: 00             BRK                     
FC06: 00             BRK                     
FC07: 00             BRK                     
FC08: 00             BRK                     
FC09: 00             BRK                     
FC0A: FE FE 7C       INC     $7CFE,X         
FC0D: FE 38 38       INC     $3838,X         
FC10: 7C             ???                     
FC11: 38             SEC                     
FC12: 38             SEC                     
FC13: 10 B6          BPL     $FBCB           
FC15: BE 5D 6B       LDX     $6B5D,Y         
FC18: 59 63 3C       EOR     $3C63,Y         
FC1B: 4C 14 28       JMP     $2814           
FC1E: B6 BE          LDX     $BE,Y           
FC20: 5D 5B 24       EOR     $245B,X         
FC23: 85 66          STA     $66             
FC25: 64             ???                     
FC26: 28             PLP                     
FC27: 10 90          BPL     $FBB9           
FC29: 88             DEY                     
FC2A: 88             DEY                     
FC2B: 44             ???                     
FC2C: 42             ???                     
FC2D: 42             ???                     
FC2E: FF             ???                     
FC2F: DB             ???                     
FC30: 5A             ???                     
FC31: 18             CLC                     
FC32: 09 11          ORA     #$11            
FC34: 11 22          ORA     ($22),Y         
FC36: 42             ???                     
FC37: 42             ???                     
FC38: FF             ???                     
FC39: DB             ???                     
FC3A: 7E 18 A5       ROR     $A518,X         
FC3D: A5 A5          LDA     $A5             
FC3F: 99 99 A5       STA     $A599,Y         
FC42: FF             ???                     
FC43: 5A             ???                     
FC44: 7E 3C 42       ROR     $423C,X         
FC47: 5A             ???                     
FC48: 5A             ???                     
FC49: 5A             ???                     
FC4A: 99 A5 FF       STA     $FFA5,Y         
FC4D: 5A             ???                     
FC4E: 7E 3C C3       ROR     $C33C,X         
FC51: 24 18          BIT     $18             
FC53: 18             CLC                     
FC54: 18             CLC                     
FC55: 5A             ???                     
FC56: BD A5 81       LDA     $81A5,X         
FC59: 81 24          STA     ($24,X)         
FC5B: 42             ???                     
FC5C: 24 A5          BIT     $A5             
FC5E: 99 99 BD       STA     $BD99,Y         
FC61: 5A             ???                     
FC62: 18             CLC                     
FC63: 00             BRK                     
FC64: 81 42          STA     ($42,X)         
FC66: 42             ???                     
FC67: 24 24          BIT     $24             
FC69: 3C             ???                     
FC6A: 7E EB 7E       ROR     $7EEB,X         
FC6D: 3C             ???                     
FC6E: 00             BRK                     
FC6F: 24 5A          BIT     $5A             
FC71: 42             ???                     
FC72: 24 3C          BIT     $3C             
FC74: 7E D7 7E       ROR     $7ED7,X         
FC77: 3C             ???                     
FC78: 77             ???                     
FC79: 44             ???                     
FC7A: 44             ???                     
FC7B: 44             ???                     
FC7C: 5C             ???                     
FC7D: FF             ???                     
FC7E: F3             ???                     
FC7F: F3             ???                     
FC80: 7E 3C EE       ROR     $EE3C,X         
FC83: 22             ???                     
FC84: 22             ???                     
FC85: 22             ???                     
FC86: 3A             ???                     
FC87: FF             ???                     
FC88: CF             ???                     
FC89: CF             ???                     
FC8A: 7E 3C E7       ROR     $E73C,X         
FC8D: 42             ???                     
FC8E: 7E 7E 6B       ROR     $6B7E,X         
FC91: 3E 98 A4       ROL     $A498,X         
FC94: 42             ???                     
FC95: 01 C6          ORA     ($C6,X)         
FC97: 42             ???                     
FC98: 7E 7E 56       ROR     $567E,X         
FC9B: 7C             ???                     
FC9C: 19 25 42       ORA     $4225,Y         
FC9F: 80             ???                     
FCA0: 00             BRK                     
FCA1: 38             SEC                     
FCA2: 7C             ???                     
FCA3: FE FE AA       INC     $AAFE,X         
FCA6: FE 7C 38       INC     $387C,X         
FCA9: 00             BRK                     
FCAA: 00             BRK                     
FCAB: 00             BRK                     
FCAC: 00             BRK                     
FCAD: 24 3C          BIT     $3C             
FCAF: 76 5C          ROR     $5C,X           
FCB1: 28             PLP                     
FCB2: 00             BRK                     
FCB3: 00             BRK                     
FCB4: 00             BRK                     
FCB5: 00             BRK                     
FCB6: 00             BRK                     
FCB7: 01 24          ORA     ($24,X)         
FCB9: 95 48          STA     $48,X           
FCBB: C7             ???                     
FCBC: 24 90          BIT     $90             
FCBE: 20 40 5D       JSR     $5D40           
FCC1: BB             ???                     
FCC2: B6 77          LDX     $77,Y           
FCC4: CC 2D 7E       CPY     $7E2D           
FCC7: CD DA 6D       CMP     $6DDA           
FCCA: 77             ???                     
FCCB: 77             ???                     
FCCC: 82             ???                     
FCCD: 54             ???                     
FCCE: 25 53          AND     $53             
FCD0: C3             ???                     
FCD1: 54             ???                     
FCD2: 93             ???                     
FCD3: A5 99          LDA     $99             
FCD5: 81 28          STA     ($28,X)         
FCD7: 78             SEI                     
FCD8: 64             ???                     
FCD9: 50 3C          BVC     $FD17           
FCDB: 8C 01 02       STY     $0201           
FCDE: 04             ???                     
FCDF: 08             PHP                     
FCE0: 10 20          BPL     $FD02           
FCE2: 40             RTI                     
FCE3: 80             ???                     
FCE4: 22             ???                     
FCE5: 16 0C          ASL     $0C,X           
FCE7: 08             PHP                     
FCE8: 05 04          ORA     $04             
FCEA: 03             ???                     
FCEB: 02             ???                     
FCEC: 00             BRK                     
FCED: 20 20 15       JSR     $1520           
FCF0: 15 10          ORA     $10,X           
FCF2: 0B             ???                     
FCF3: 07             ???                     
FCF4: 07             ???                     
FCF5: 04             ???                     
FCF6: 01 01          ORA     ($01,X)         
FCF8: 02             ???                     
FCF9: 02             ???                     
FCFA: 03             ???                     
FCFB: 03             ???                     
FCFC: 03             ???                     
FCFD: 04             ???                     
FCFE: 05 0F          ORA     $0F             
FD00: 0E 0F 00       ASL     $000F           
FD03: 02             ???                     
FD04: 00             BRK                     
FD05: 04             ???                     
FD06: 02             ???                     
FD07: 34             ???                     
FD08: 52             ???                     
FD09: CC F6 14       CPY     $14F6           
FD0C: 0F             ???                     
FD0D: 00             BRK                     
FD0E: E2             ???                     
FD0F: 05 0A          ORA     $0A             
FD11: 0F             ???                     
FD12: 14             ???                     
FD13: BD B4 AB       LDA     $ABB4,X         
FD16: 54             ???                     
FD17: 59 5E 63       EOR     $635E,Y         
FD1A: 00             BRK                     
FD1B: 08             PHP                     
FD1C: 04             ???                     
FD1D: 0C             ???                     
FD1E: AA             TAX                     
FD1F: B6 C0          LDX     $C0,Y           
FD21: CC 3C 7E       CPY     $7E3C           
FD24: 7E 7E 7E       ROR     $7E7E,X         
FD27: FF             ???                     
FD28: FF             ???                     
FD29: FF             ???                     
FD2A: C3             ???                     
FD2B: 05 10          ORA     $10             
FD2D: 15 20          ORA     $20,X           
FD2F: 25 30          AND     $30             
FD31: 00             BRK                     
FD32: 09 12          ORA     #$12            
FD34: 1B             ???                     
FD35: 24 2D          BIT     $2D             
FD37: 36 01          ROL     $01,X           
FD39: 00             BRK                     
FD3A: 10 20          BPL     $FD5C           
FD3C: 30 40          BMI     $FD7E           
FD3E: 50 60          BVC     $FDA0           
FD40: 70 80          BVS     $FCC2           
FD42: 90 00          BCC     $FD44           
FD44: 10 8B          BPL     $FCD1           
FD46: D1 BF          CMP     ($BF),Y         
FD48: 9D D1 D1       STA     $D1D1,X         
FD4B: 18             CLC                     
FD4C: 10 61          BPL     $FDAF           
FD4E: D1 32          CMP     ($32),Y         
FD50: 90 14          BCC     $FD66           
FD52: 10 10          BPL     $FD64           
FD54: 30 30          BMI     $FD86           
FD56: 10 10          BPL     $FD68           
FD58: 10 00          BPL     $FD5A           
FD5A: 00             BRK                     
FD5B: 08             PHP                     
FD5C: 00             BRK                     
FD5D: 00             BRK                     
FD5E: 00             BRK                     
FD5F: 00             BRK                     
FD60: 05 03          ORA     $03             
FD62: 17             ???                     
FD63: 2B             ???                     
FD64: 23             ???                     
FD65: 75 B4          ADC     $B4,X           
FD67: A0 FF          LDY     #$FF            
FD69: 38             SEC                     
FD6A: C8             INY                     
FD6B: E9 0F          SBC     #$0F            
FD6D: B0 FB          BCS     $FD6A           
FD6F: 49 FF          EOR     #$FF            
FD71: E9 06          SBC     #$06            
FD73: 0A             ASL     A               
FD74: 0A             ASL     A               
FD75: 0A             ASL     A               
FD76: 0A             ASL     A               
FD77: 94 83          STY     $83,X           
FD79: 15 83          ORA     $83,X           
FD7B: 95 83          STA     $83,X           
FD7D: 60             RTS                     
FD7E: 85 02          STA     $02             
FD80: EA             NOP                     
FD81: C8             INY                     
FD82: 95 20          STA     $20,X           
FD84: EA             NOP                     
FD85: 88             DEY                     
FD86: 10 FD          BPL     $FD85           
FD88: 95 10          STA     $10,X           
FD8A: 60             RTS                     
FD8B: C0 09          CPY     #$09            
FD8D: B0 22          BCS     $FDB1           
FD8F: 86 EE          STX     $EE             
FD91: E8             INX                     
FD92: 20 FB FD       JSR     $FDFB           
FD95: 29 20          AND     #$20            
FD97: D0 02          BNE     $FD9B           
FD99: CA             DEX                     
FD9A: CA             DEX                     
FD9B: E0 08          CPX     #$08            
FD9D: B0 09          BCS     $FDA8           
FD9F: A5 EA          LDA     $EA             
FDA1: C9 C0          CMP     #$C0            
FDA3: 90 03          BCC     $FDA8           
FDA5: 20 AA FD       JSR     $FDAA           
FDA8: A6 EE          LDX     $EE             
FDAA: B1 F0          LDA     ($F0),Y         
FDAC: 3D 4C FF       AND     $FF4C,X         
FDAF: 91 F0          STA     ($F0),Y         
FDB1: 60             RTS                     
FDB2: C6 89          DEC     $89             
FDB4: A5 89          LDA     $89             
FDB6: 30 0F          BMI     $FDC7           
FDB8: C9 04          CMP     #$04            
FDBA: A9 02          LDA     #$02            
FDBC: 90 01          BCC     $FDBF           
FDBE: 4A             LSR     A               
FDBF: 85 1F          STA     $1F             
FDC1: 85 02          STA     $02             
FDC3: 85 2B          STA     $2B             
FDC5: 10 1D          BPL     $FDE4           
FDC7: 18             CLC                     
FDC8: 65 8A          ADC     $8A             
FDCA: 85 89          STA     $89             
FDCC: A9 00          LDA     #$00            
FDCE: 85 02          STA     $02             
FDD0: 85 2B          STA     $2B             
FDD2: 85 1F          STA     $1F             
FDD4: A5 88          LDA     $88             
FDD6: 85 24          STA     $24             
FDD8: 29 0F          AND     #$0F            
FDDA: A8             TAY                     
FDDB: 88             DEY                     
FDDC: 10 FD          BPL     $FDDB           
FDDE: 85 14          STA     $14             
FDE0: A9 7C          LDA     #$7C            
FDE2: 85 8A          STA     $8A             
FDE4: 85 02          STA     $02             
FDE6: 85 2A          STA     $2A             
FDE8: 60             RTS                     
FDE9: C6 89          DEC     $89             
FDEB: A5 89          LDA     $89             
FDED: C9 04          CMP     #$04            
FDEF: 90 04          BCC     $FDF5           
FDF1: A9 00          LDA     #$00            
FDF3: B0 03          BCS     $FDF8           
FDF5: EA             NOP                     
FDF6: A9 02          LDA     #$02            
FDF8: 85 1F          STA     $1F             
FDFA: 60             RTS                     
FDFB: A5 EA          LDA     $EA             
FDFD: 0A             ASL     A               
FDFE: 0A             ASL     A               
FDFF: 18             CLC                     
FE00: 65 EA          ADC     $EA             
FE02: 18             CLC                     
FE03: 69 59          ADC     #$59            
FE05: 85 EA          STA     $EA             
FE07: 60             RTS                     
FE08: A5 C7          LDA     $C7             
FE0A: D0 5C          BNE     $FE68           
FE0C: F6 CD          INC     $CD,X           
FE0E: B4 CB          LDY     $CB,X           
FE10: F0 56          BEQ     $FE68           
FE12: C0 05          CPY     #$05            
FE14: F0 04          BEQ     $FE1A           
FE16: C0 02          CPY     #$02            
FE18: D0 24          BNE     $FE3E           
FE1A: B4 CD          LDY     $CD,X           
FE1C: C0 08          CPY     #$08            
FE1E: D0 08          BNE     $FE28           
FE20: B5 CB          LDA     $CB,X           
FE22: C9 05          CMP     #$05            
FE24: F0 46          BEQ     $FE6C           
FE26: D0 40          BNE     $FE68           
FE28: B9 EA FF       LDA     $FFEA,Y         
FE2B: 95 17          STA     $17,X           
FE2D: A9 0C          LDA     #$0C            
FE2F: 95 15          STA     $15,X           
FE31: A9 CB          LDA     #$CB            
FE33: C9 05          CMP     #$05            
FE35: A9 04          LDA     #$04            
FE37: 90 02          BCC     $FE3B           
FE39: A9 08          LDA     #$08            
FE3B: 95 19          STA     $19,X           
FE3D: 60             RTS                     
FE3E: B9 44 FD       LDA     $FD44,Y         
FE41: 85 EE          STA     $EE             
FE43: A9 FF          LDA     #$FF            
FE45: 85 EF          STA     $EF             
FE47: B4 CF          LDY     $CF,X           
FE49: B1 EE          LDA     ($EE),Y         
FE4B: D5 CD          CMP     $CD,X           
FE4D: D0 18          BNE     $FE67           
FE4F: C8             INY                     
FE50: B1 EE          LDA     ($EE),Y         
FE52: 30 14          BMI     $FE68           
FE54: C9 3F          CMP     #$3F            
FE56: F0 14          BEQ     $FE6C           
FE58: 95 17          STA     $17,X           
FE5A: C8             INY                     
FE5B: B1 EE          LDA     ($EE),Y         
FE5D: 95 15          STA     $15,X           
FE5F: C8             INY                     
FE60: B1 EE          LDA     ($EE),Y         
FE62: C8             INY                     
FE63: 94 CF          STY     $CF,X           
FE65: 95 19          STA     $19,X           
FE67: 60             RTS                     
FE68: A9 00          LDA     #$00            
FE6A: 95 CB          STA     $CB,X           
FE6C: A9 00          LDA     #$00            
FE6E: 95 19          STA     $19,X           
FE70: 95 CD          STA     $CD,X           
FE72: 95 CF          STA     $CF,X           
FE74: 60             RTS                     
FE75: A5 CA          LDA     $CA             
FE77: 29 01          AND     #$01            
FE79: 09 80          ORA     #$80            
FE7B: 85 CA          STA     $CA             
FE7D: 60             RTS                     
FE7E: C5 CB          CMP     $CB             
FE80: 90 08          BCC     $FE8A           
FE82: 85 CB          STA     $CB             
FE84: A9 00          LDA     #$00            
FE86: 85 CD          STA     $CD             
FE88: 85 CF          STA     $CF             
FE8A: 60             RTS                     
FE8B: C5 CC          CMP     $CC             
FE8D: 90 08          BCC     $FE97           
FE8F: 85 CC          STA     $CC             
FE91: A9 00          LDA     #$00            
FE93: 85 CE          STA     $CE             
FE95: 85 D0          STA     $D0             
FE97: 60             RTS                     

# Startup

All of the 6502 vectors point here.

FE98: D8             CLD                     
FE99: 78             SEI                     
FE9A: A2 00          LDX     #$00            
FE9C: 8A             TXA                     
FE9D: 95 00          STA     $00,X           
FE9F: E8             INX                     
FEA0: D0 FB          BNE     $FE9D           
FEA2: CA             DEX                     
FEA3: 9A             TXS                     
FEA4: 20 B2 FE       JSR     $FEB2           
FEA7: A9 C5          LDA     #$C5            
FEA9: 85 C7          STA     $C7             
FEAB: A9 80          LDA     #$80            
FEAD: 85 AA          STA     $AA             
FEAF: 4C D4 F4       JMP     $F4D4           
FEB2: A9 00          LDA     #$00            
FEB4: 85 E6          STA     $E6             
FEB6: 85 E8          STA     $E8             
FEB8: 85 E7          STA     $E7             
FEBA: 85 E9          STA     $E9             
FEBC: 85 C7          STA     $C7             
FEBE: A9 01          LDA     #$01            
FEC0: 85 AA          STA     $AA             
FEC2: A9 00          LDA     #$00            
FEC4: 85 90          STA     $90             
FEC6: 85 99          STA     $99             
FEC8: 85 C6          STA     $C6             
FECA: 20 75 FE       JSR     $FE75           
FECD: A9 03          LDA     #$03            
FECF: 85 C9          STA     $C9             
FED1: A9 FF          LDA     #$FF            
FED3: 85 8B          STA     $8B             
FED5: A5 98          LDA     $98             
FED7: 29 53          AND     #$53            
FED9: A4 EC          LDY     $EC             
FEDB: 19 52 FD       ORA     $FD52,Y         
FEDE: 19 59 FD       ORA     $FD59,Y         
FEE1: 85 98          STA     $98             
FEE3: A5 E5          LDA     $E5             
FEE5: 29 7F          AND     #$7F            
FEE7: 85 E5          STA     $E5             
FEE9: 20 FA FE       JSR     $FEFA           
FEEC: A2 0A          LDX     #$0A            
FEEE: B5 90          LDA     $90,X           
FEF0: 95 9F          STA     $9F,X           
FEF2: CA             DEX                     
FEF3: 10 F9          BPL     $FEEE           
FEF5: A9 6E          LDA     #$6E            
FEF7: 85 A7          STA     $A7             
FEF9: 60             RTS                     
FEFA: A2 05          LDX     #$05            
FEFC: A9 3F          LDA     #$3F            
FEFE: 95 92          STA     $92,X           
FF00: CA             DEX                     
FF01: 10 FB          BPL     $FEFE           
FF03: 85 EB          STA     $EB             
FF05: 85 D7          STA     $D7             
FF07: 85 D8          STA     $D8             
FF09: 85 D3          STA     $D3             
FF0B: 85 D4          STA     $D4             
FF0D: A9 F6          LDA     #$F6            
FF0F: 85 D5          STA     $D5             
FF11: 85 D6          STA     $D6             
FF13: 85 D1          STA     $D1             
FF15: 85 D2          STA     $D2             
FF17: A2 05          LDX     #$05            
FF19: BD 61 FD       LDA     $FD61,X         
FF1C: 95 99          STA     $99,X           
FF1E: CA             DEX                     
FF1F: D0 F8          BNE     $FF19           
FF21: 8A             TXA                     
FF22: 85 CB          STA     $CB             
FF24: 85 CC          STA     $CC             
FF26: A9 24          LDA     #$24            
FF28: 85 91          STA     $91             
FF2A: A9 42          LDA     #$42            
FF2C: 05 98          ORA     $98             
FF2E: 85 98          STA     $98             
FF30: A9 30          LDA     #$30            
FF32: 85 C8          STA     $C8             
FF34: A5 AA          LDA     $AA             
FF36: 29 F7          AND     #$F7            
FF38: 85 AA          STA     $AA             
FF3A: A2 1A          LDX     #$1A            
FF3C: A0 08          LDY     #$08            
FF3E: B9 22 FD       LDA     $FD22,Y         
FF41: 95 AB          STA     $AB,X           
FF43: 88             DEY                     
FF44: 10 02          BPL     $FF48           
FF46: A0 08          LDY     #$08            
FF48: CA             DEX                     
FF49: 10 F3          BPL     $FF3E           
FF4B: 60             RTS                     
FF4C: 7F             ???                     
FF4D: BF             ???                     
FF4E: DF             ???                     
FF4F: EF             ???                     
FF50: F7             ???                     
FF51: FB             ???                     
FF52: FD FE E7       SBC     $E7FE,X         
FF55: A5 A5          LDA     $A5             
FF57: A5 E7          LDA     $E7             
FF59: E7             ???                     
FF5A: 42             ???                     
FF5B: 42             ???                     
FF5C: 66 42          ROR     $42             
FF5E: E7             ???                     
FF5F: 24 E7          BIT     $E7             
FF61: 81 E7          STA     ($E7,X)         
FF63: E7             ???                     
FF64: 81 E7          STA     ($E7,X)         
FF66: 81 E7          STA     ($E7,X)         
FF68: 81 81          STA     ($81,X)         
FF6A: E7             ???                     
FF6B: A5 A5          LDA     $A5             
FF6D: E7             ???                     
FF6E: 81 E7          STA     ($E7,X)         
FF70: 24 E7          BIT     $E7             
FF72: E7             ???                     
FF73: A5 E7          LDA     $E7             
FF75: 24 24          BIT     $24             
FF77: 81 81          STA     ($81,X)         
FF79: 81 81          STA     ($81,X)         
FF7B: E7             ???                     
FF7C: E7             ???                     
FF7D: A5 E7          LDA     $E7             
FF7F: A5 E7          LDA     $E7             
FF81: 81 81          STA     ($81,X)         
FF83: E7             ???                     
FF84: A5 E7          LDA     $E7             
FF86: 00             BRK                     
FF87: 00             BRK                     
FF88: 00             BRK                     
FF89: 00             BRK                     
FF8A: 00             BRK                     
FF8B: 01 16          ORA     ($16,X)         
FF8D: 09 0A          ORA     #$0A            
FF8F: 02             ???                     
FF90: 19 08 0A       ORA     $0A08,Y         
FF93: 03             ???                     
FF94: 1F             ???                     
FF95: 0C             ???                     
FF96: 08             PHP                     
FF97: 04             ???                     
FF98: 16 0E          ASL     $0E,X           
FF9A: 07             ???                     
FF9B: 06 FF          ASL     $FF             
FF9D: 01 18          ORA     ($18,X)         
FF9F: 0C             ???                     
FFA0: 03             ???                     
FFA1: 03             ???                     
FFA2: 16 0C          ASL     $0C,X           
FFA4: 03             ???                     
FFA5: 05 14          ORA     $14             
FFA7: 0C             ???                     
FFA8: 03             ???                     
FFA9: 07             ???                     
FFAA: 12             ???                     
FFAB: 0C             ???                     
FFAC: 03             ???                     
FFAD: 09 10          ORA     #$10            
FFAF: 0C             ???                     
FFB0: 03             ???                     
FFB1: 0B             ???                     
FFB2: 0E 0C 03       ASL     $030C           
FFB5: 0D 0D 0C       ORA     $0C0D           
FFB8: 03             ???                     
FFB9: 0F             ???                     
FFBA: 10 0C          BPL     $FFC8           
FFBC: 03             ???                     
FFBD: 11 3F          ORA     ($3F),Y         
FFBF: 01 18          ORA     ($18,X)         
FFC1: 08             PHP                     
FFC2: 07             ???                     
FFC3: 04             ???                     
FFC4: 19 08 05       ORA     $0508,Y         
FFC7: 10 1C          BPL     $FFE5           
FFC9: 08             PHP                     
FFCA: 02             ???                     
FFCB: 30 1E          BMI     $FFEB           
FFCD: 08             PHP                     
FFCE: 01 50          ORA     ($50,X)         
FFD0: FF             ???                     
FFD1: 01 18          ORA     ($18,X)         
FFD3: 03             ???                     
FFD4: 0C             ???                     
FFD5: 09 10          ORA     #$10            
FFD7: 0A             ASL     A               
FFD8: 08             PHP                     
FFD9: 11 12          ORA     ($12),Y         
FFDB: 0E 0F 19       ASL     $190F           
FFDE: 16 0E          ASL     $0E,X           
FFE0: 08             PHP                     
FFE1: 29 1A          AND     #$1A            
FFE3: 0E 04 39       ASL     $3904           
FFE6: 1D 0E 02       ORA     $020E,X         
FFE9: 49 FF          EOR     #$FF            
FFEB: 10 0D          BPL     $FFFA           
FFED: 0A             ASL     A               
FFEE: 08             PHP                     
FFEF: 07             ???                     
FFF0: 06 05          ASL     $05             
FFF2: 06 07          ASL     $07             
FFF4: 03             ???                     
FFF5: 04             ???                     
FFF6: 05 06          ORA     $06             
FFF8: 00             BRK                     
FFF9: 00             BRK                

# Vectors 
     
FFFA: 98 FE 
FFFC: 98 FE         
FFFE: 98 FE 