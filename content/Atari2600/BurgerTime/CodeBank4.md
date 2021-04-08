![Burger Time](A2600BT.jpg)

# Burger Time Bank 4

>>> cpu 6502

>>> memoryTable hard 
[Hardware Info](../Stella.md)

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

```code
F000: 00              BRK                         
F001: 00              BRK                         
F002: 00              BRK                         
F003: 00              BRK                         
F004: 00              BRK                         
F005: 00              BRK                         
F006: 00              BRK                         
F007: 00              BRK                         
F008: 00              BRK                         
F009: 00              BRK                         
F00A: 00              BRK                         
F00B: 00              BRK                         
F00C: 00              BRK                         
F00D: 00              BRK                         
F00E: 00              BRK                         
F00F: 00              BRK                         
F010: 00              BRK                         
F011: 00              BRK                         
F012: 00              BRK                         
F013: 00              BRK                         
F014: 00              BRK                         
F015: 00              BRK                         
F016: 00              BRK                         
F017: 00              BRK                         
F018: 00              BRK                         
F019: 00              BRK                         
F01A: 00              BRK                         
F01B: 00              BRK                         
F01C: 00              BRK                         
F01D: 00              BRK                         
F01E: 00              BRK                         
F01F: 00              BRK                         
F020: 00              BRK                         
F021: 00              BRK                         
F022: 00              BRK                         
F023: 00              BRK                         
F024: 00              BRK                         
F025: 00              BRK                         
F026: 00              BRK                         
F027: 00              BRK                         
F028: 00              BRK                         
F029: 00              BRK                         
F02A: 00              BRK                         
F02B: 00              BRK                         
F02C: 00              BRK                         
F02D: 00              BRK                         
F02E: 00              BRK                         
F02F: 00              BRK                         
F030: 00              BRK                         
F031: 00              BRK                         
F032: 00              BRK                         
F033: 00              BRK                         
F034: 00              BRK                         
F035: 00              BRK                         
F036: 00              BRK                         
F037: 00              BRK                         
F038: 00              BRK                         
F039: 00              BRK                         
F03A: 00              BRK                         
F03B: 00              BRK                         
F03C: 00              BRK                         
F03D: 00              BRK                         
F03E: 00              BRK                         
F03F: 00              BRK                         
F040: 00              BRK                         
F041: 00              BRK                         
F042: 00              BRK                         
F043: 00              BRK                         
F044: 00              BRK                         
F045: 00              BRK                         
F046: 00              BRK                         
F047: 00              BRK                         
F048: 00              BRK                         
F049: 00              BRK                         
F04A: 00              BRK                         
F04B: 00              BRK                         
F04C: 00              BRK                         
F04D: 00              BRK                         
F04E: 00              BRK                         
F04F: 00              BRK                         
F050: 00              BRK                         
F051: 00              BRK                         
F052: 00              BRK                         
F053: 00              BRK                         
F054: 00              BRK                         
F055: 00              BRK                         
F056: 00              BRK                         
F057: 00              BRK                         
F058: 00              BRK                         
F059: 00              BRK                         
F05A: 00              BRK                         
F05B: 00              BRK                         
F05C: 00              BRK                         
F05D: 00              BRK                         
F05E: 00              BRK                         
F05F: 00              BRK                         
F060: 00              BRK                         
F061: 00              BRK                         
F062: 00              BRK                         
F063: 00              BRK                         
F064: 00              BRK                         
F065: 00              BRK                         
F066: 00              BRK                         
F067: 00              BRK                         
F068: 00              BRK                         
F069: 7C ; ????
F06A: 54 ; ????
F06B: 4C 5C 4C        JMP     $4C5C                   
F06E: 54 ; ????
F06F: 7C ; ????
F070: 7A ; ????
F071: DB ; ????
F072: ED 2D 6A        SBC     $6A2D                   
F075: 52 ; ????
F076: 12 ; ????
F077: 12 ; ????
F078: 00              BRK                         
F079: 00              BRK                         
F07A: 00              BRK                         
F07B: 00              BRK                         
F07C: 00              BRK                         
F07D: 00              BRK                         
F07E: 00              BRK                         
F07F: 00              BRK                         
F080: 00              BRK                         
F081: 00              BRK                         
F082: 00              BRK                         
F083: 00              BRK                         
F084: 00              BRK                         
F085: 00              BRK                         
F086: 00              BRK                         
F087: 00              BRK                         
F088: 00              BRK                         
F089: 00              BRK                         
F08A: 00              BRK                         
F08B: 00              BRK                         
F08C: 00              BRK                         
F08D: 00              BRK                         
F08E: 00              BRK                         
F08F: 00              BRK                         
F090: 00              BRK                         
F091: 00              BRK                         
F092: 00              BRK                         
F093: 00              BRK                         
F094: 00              BRK                         
F095: 00              BRK                         
F096: 00              BRK                         
F097: 00              BRK                         
F098: 00              BRK                         
F099: 00              BRK                         
F09A: 00              BRK                         
F09B: 00              BRK                         
F09C: 00              BRK                         
F09D: 00              BRK                         
F09E: 00              BRK                         
F09F: 00              BRK                         
F0A0: 00              BRK                         
F0A1: 00              BRK                         
F0A2: 00              BRK                         
F0A3: 00              BRK                         
F0A4: 00              BRK                         
F0A5: 00              BRK                         
F0A6: 00              BRK                         
F0A7: 00              BRK                         
F0A8: 00              BRK                         
F0A9: 00              BRK                         
F0AA: 00              BRK                         
F0AB: 00              BRK                         
F0AC: 00              BRK                         
F0AD: 00              BRK                         
F0AE: 00              BRK                         
F0AF: 00              BRK                         
F0B0: 00              BRK                         
F0B1: 00              BRK                         
F0B2: 00              BRK                         
F0B3: 00              BRK                         
F0B4: 00              BRK                         
F0B5: 00              BRK                         
F0B6: 00              BRK                         
F0B7: 00              BRK                         
F0B8: 00              BRK                         
F0B9: 00              BRK                         
F0BA: 00              BRK                         
F0BB: 00              BRK                         
F0BC: 00              BRK                         
F0BD: 00              BRK                         
F0BE: 00              BRK                         
F0BF: 00              BRK                         
F0C0: 00              BRK                         
F0C1: 00              BRK                         
F0C2: 00              BRK                         
F0C3: 00              BRK                         
F0C4: 00              BRK                         
F0C5: 00              BRK                         
F0C6: 00              BRK                         
F0C7: 00              BRK                         
F0C8: 00              BRK                         
F0C9: 00              BRK                         
F0CA: 00              BRK                         
F0CB: 00              BRK                         
F0CC: 00              BRK                         
F0CD: 00              BRK                         
F0CE: 00              BRK                         
F0CF: 00              BRK                         
F0D0: 00              BRK                         
F0D1: 00              BRK                         
F0D2: 00              BRK                         
F0D3: 00              BRK                         
F0D4: 00              BRK                         
F0D5: 00              BRK                         
F0D6: 00              BRK                         
F0D7: 00              BRK                         
F0D8: 00              BRK                         
F0D9: 00              BRK                         
F0DA: 00              BRK                         
F0DB: 00              BRK                         
F0DC: 00              BRK                         
F0DD: 00              BRK                         
F0DE: 00              BRK                         
F0DF: 00              BRK                         
F0E0: 00              BRK                         
F0E1: 00              BRK                         
F0E2: 06 64           ASL     $64                   
F0E4: 00              BRK                         
F0E5: 3C ; ????
F0E6: 3C ; ????
F0E7: 29 A5           AND     #$A5                  
F0E9: DA ; ????
F0EA: 3C ; ????
F0EB: 28              PLP                         
F0EC: 00              BRK                         
F0ED: 3C ; ????
F0EE: 3C ; ????
F0EF: 7E 7E 00        ROR     $007E,X                 
F0F2: 00              BRK                         
F0F3: 00              BRK                         
F0F4: 00              BRK                         
F0F5: 00              BRK                         
F0F6: 00              BRK                         
F0F7: 00              BRK                         
F0F8: 00              BRK                         
F0F9: 00              BRK                         
F0FA: 00              BRK                         
F0FB: 00              BRK                         
F0FC: 00              BRK                         
F0FD: 00              BRK                         
F0FE: 00              BRK                         
F0FF: 00              BRK                         
F100: 00              BRK                         
F101: 00              BRK                         
F102: 00              BRK                         
F103: 00              BRK                         
F104: 00              BRK                         
F105: 00              BRK                         
F106: 00              BRK                         
F107: 00              BRK                         
F108: 00              BRK                         
F109: 00              BRK                         
F10A: 00              BRK                         
F10B: 00              BRK                         
F10C: 00              BRK                         
F10D: 00              BRK                         
F10E: 00              BRK                         
F10F: 00              BRK                         
F110: 00              BRK                         
F111: 00              BRK                         
F112: 00              BRK                         
F113: 00              BRK                         
F114: 00              BRK                         
F115: 00              BRK                         
F116: 00              BRK                         
F117: 00              BRK                         
F118: 00              BRK                         
F119: 00              BRK                         
F11A: 00              BRK                         
F11B: 00              BRK                         
F11C: 00              BRK                         
F11D: 00              BRK                         
F11E: 00              BRK                         
F11F: 00              BRK                         
F120: 00              BRK                         
F121: 00              BRK                         
F122: 00              BRK                         
F123: 00              BRK                         
F124: 00              BRK                         
F125: 00              BRK                         
F126: 00              BRK                         
F127: 00              BRK                         
F128: 00              BRK                         
F129: 00              BRK                         
F12A: 00              BRK                         
F12B: 00              BRK                         
F12C: 00              BRK                         
F12D: 00              BRK                         
F12E: 00              BRK                         
F12F: 00              BRK                         
F130: 00              BRK                         
F131: 00              BRK                         
F132: 00              BRK                         
F133: 00              BRK                         
F134: 00              BRK                         
F135: 00              BRK                         
F136: 00              BRK                         
F137: 00              BRK                         
F138: 00              BRK                         
F139: 00              BRK                         
F13A: 00              BRK                         
F13B: 00              BRK                         
F13C: 00              BRK                         
F13D: 00              BRK                         
F13E: 00              BRK                         
F13F: 00              BRK                         
F140: 00              BRK                         
F141: 00              BRK                         
F142: 00              BRK                         
F143: 00              BRK                         
F144: 00              BRK                         
F145: 00              BRK                         
F146: 00              BRK                         
F147: 00              BRK                         
F148: 00              BRK                         
F149: 00              BRK                         
F14A: 00              BRK                         
F14B: 00              BRK                         
F14C: 00              BRK                         
F14D: 00              BRK                         
F14E: 00              BRK                         
F14F: 00              BRK                         
F150: 00              BRK                         
F151: 00              BRK                         
F152: 00              BRK                         
F153: 00              BRK                         
F154: 00              BRK                         
F155: 00              BRK                         
F156: 00              BRK                         
F157: 00              BRK                         
F158: 00              BRK                         
F159: 00              BRK                         
F15A: 00              BRK                         
F15B: 00              BRK                         
F15C: 00              BRK                         
F15D: 00              BRK                         
F15E: 00              BRK                         
F15F: 00              BRK                         
F160: 00              BRK                         
F161: 00              BRK                         
F162: 00              BRK                         
F163: 00              BRK                         
F164: 00              BRK                         
F165: 00              BRK                         
F166: 00              BRK                         
F167: 00              BRK                         
F168: 00              BRK                         
F169: 08              PHP                         
F16A: 08              PHP                         
F16B: 1C ; ????
F16C: 1C ; ????
F16D: 3E 3E 3E        ROL     $3E3E,X                 
F170: 1C ; ????
F171: 3E 3E 1C        ROL     $1C3E,X                 
F174: 08              PHP                         
F175: 00              BRK                         
F176: 00              BRK                         
F177: 00              BRK                         
F178: 00              BRK                         
F179: 00              BRK                         
F17A: 00              BRK                         
F17B: 00              BRK                         
F17C: 00              BRK                         
F17D: 00              BRK                         
F17E: 00              BRK                         
F17F: 00              BRK                         
F180: 00              BRK                         
F181: 00              BRK                         
F182: 00              BRK                         
F183: 00              BRK                         
F184: 00              BRK                         
F185: 00              BRK                         
F186: 00              BRK                         
F187: 00              BRK                         
F188: 00              BRK                         
F189: 00              BRK                         
F18A: 00              BRK                         
F18B: 00              BRK                         
F18C: 00              BRK                         
F18D: 00              BRK                         
F18E: 00              BRK                         
F18F: 00              BRK                         
F190: 00              BRK                         
F191: 00              BRK                         
F192: 00              BRK                         
F193: 00              BRK                         
F194: 00              BRK                         
F195: 00              BRK                         
F196: 00              BRK                         
F197: 00              BRK                         
F198: 00              BRK                         
F199: 00              BRK                         
F19A: 00              BRK                         
F19B: 00              BRK                         
F19C: 00              BRK                         
F19D: 00              BRK                         
F19E: 00              BRK                         
F19F: 00              BRK                         
F1A0: 00              BRK                         
F1A1: 00              BRK                         
F1A2: 00              BRK                         
F1A3: 00              BRK                         
F1A4: 00              BRK                         
F1A5: 00              BRK                         
F1A6: 00              BRK                         
F1A7: 00              BRK                         
F1A8: 00              BRK                         
F1A9: 00              BRK                         
F1AA: 00              BRK                         
F1AB: 00              BRK                         
F1AC: 00              BRK                         
F1AD: 00              BRK                         
F1AE: 00              BRK                         
F1AF: 00              BRK                         
F1B0: 00              BRK                         
F1B1: 00              BRK                         
F1B2: 00              BRK                         
F1B3: 00              BRK                         
F1B4: 00              BRK                         
F1B5: 00              BRK                         
F1B6: 00              BRK                         
F1B7: 00              BRK                         
F1B8: 00              BRK                         
F1B9: 00              BRK                         
F1BA: 00              BRK                         
F1BB: 00              BRK                         
F1BC: 00              BRK                         
F1BD: 00              BRK                         
F1BE: 00              BRK                         
F1BF: 00              BRK                         
F1C0: 00              BRK                         
F1C1: 00              BRK                         
F1C2: 00              BRK                         
F1C3: 00              BRK                         
F1C4: 00              BRK                         
F1C5: 00              BRK                         
F1C6: 00              BRK                         
F1C7: 00              BRK                         
F1C8: 00              BRK                         
F1C9: 00              BRK                         
F1CA: 00              BRK                         
F1CB: 00              BRK                         
F1CC: 00              BRK                         
F1CD: 00              BRK                         
F1CE: 00              BRK                         
F1CF: 00              BRK                         
F1D0: 00              BRK                         
F1D1: 00              BRK                         
F1D2: 00              BRK                         
F1D3: 00              BRK                         
F1D4: 00              BRK                         
F1D5: 00              BRK                         
F1D6: 00              BRK                         
F1D7: 00              BRK                         
F1D8: 00              BRK                         
F1D9: 00              BRK                         
F1DA: 00              BRK                         
F1DB: 00              BRK                         
F1DC: 00              BRK                         
F1DD: 00              BRK                         
F1DE: 00              BRK                         
F1DF: 00              BRK                         
F1E0: 00              BRK                         
F1E1: 00              BRK                         
F1E2: 30 26           BMI     $F20A                   
F1E4: 00              BRK                         
F1E5: 3E BF BA        ROL     $BABF,X                 
F1E8: 7C ; ????
F1E9: 00              BRK                         
F1EA: 1C ; ????
F1EB: 1A ; ????
F1EC: 00              BRK                         
F1ED: 3C ; ????
F1EE: 3C ; ????
F1EF: 7E 7E 00        ROR     $007E,X                 
F1F2: 00              BRK                         
F1F3: 00              BRK                         
F1F4: 00              BRK                         
F1F5: 00              BRK                         
F1F6: 00              BRK                         
F1F7: 00              BRK                         
F1F8: 00              BRK                         
F1F9: 00              BRK                         
F1FA: 00              BRK                         
F1FB: 00              BRK                         
F1FC: 00              BRK                         
F1FD: 00              BRK                         
F1FE: 00              BRK                         
F1FF: 00              BRK                         
F200: 00              BRK                         
F201: 00              BRK                         
F202: 00              BRK                         
F203: 00              BRK                         
F204: 00              BRK                         
F205: 00              BRK                         
F206: 00              BRK                         
F207: 00              BRK                         
F208: 00              BRK                         
F209: 00              BRK                         
F20A: 00              BRK                         
F20B: 00              BRK                         
F20C: 00              BRK                         
F20D: 00              BRK                         
F20E: 00              BRK                         
F20F: 00              BRK                         
F210: 00              BRK                         
F211: 00              BRK                         
F212: 00              BRK                         
F213: 00              BRK                         
F214: 00              BRK                         
F215: 00              BRK                         
F216: 00              BRK                         
F217: 00              BRK                         
F218: 00              BRK                         
F219: 00              BRK                         
F21A: 00              BRK                         
F21B: 00              BRK                         
F21C: 00              BRK                         
F21D: 00              BRK                         
F21E: 00              BRK                         
F21F: 00              BRK                         
F220: 00              BRK                         
F221: 00              BRK                         
F222: 00              BRK                         
F223: 00              BRK                         
F224: 00              BRK                         
F225: 00              BRK                         
F226: 00              BRK                         
F227: 00              BRK                         
F228: 00              BRK                         
F229: 00              BRK                         
F22A: 00              BRK                         
F22B: 00              BRK                         
F22C: 00              BRK                         
F22D: 00              BRK                         
F22E: 00              BRK                         
F22F: 00              BRK                         
F230: 00              BRK                         
F231: 00              BRK                         
F232: 00              BRK                         
F233: 00              BRK                         
F234: 00              BRK                         
F235: 00              BRK                         
F236: 00              BRK                         
F237: 00              BRK                         
F238: 00              BRK                         
F239: 00              BRK                         
F23A: 00              BRK                         
F23B: 00              BRK                         
F23C: 00              BRK                         
F23D: 00              BRK                         
F23E: 00              BRK                         
F23F: 00              BRK                         
F240: 00              BRK                         
F241: 00              BRK                         
F242: 00              BRK                         
F243: 00              BRK                         
F244: 00              BRK                         
F245: 00              BRK                         
F246: 00              BRK                         
F247: 00              BRK                         
F248: 00              BRK                         
F249: 00              BRK                         
F24A: 00              BRK                         
F24B: 00              BRK                         
F24C: 00              BRK                         
F24D: 00              BRK                         
F24E: 00              BRK                         
F24F: 00              BRK                         
F250: 00              BRK                         
F251: 00              BRK                         
F252: 00              BRK                         
F253: 00              BRK                         
F254: 00              BRK                         
F255: 00              BRK                         
F256: 00              BRK                         
F257: 00              BRK                         
F258: 00              BRK                         
F259: 00              BRK                         
F25A: 00              BRK                         
F25B: 00              BRK                         
F25C: 00              BRK                         
F25D: 00              BRK                         
F25E: 00              BRK                         
F25F: 00              BRK                         
F260: 00              BRK                         
F261: 00              BRK                         
F262: 00              BRK                         
F263: 00              BRK                         
F264: 00              BRK                         
F265: 00              BRK                         
F266: 00              BRK                         
F267: 00              BRK                         
F268: 00              BRK                         
F269: 3F ; ????
F26A: 3F ; ????
F26B: 3F ; ????
F26C: 21 E1           AND     ($E1,X)               
F26E: A1 A1           LDA     ($A1,X)               
F270: A1 A1           LDA     ($A1,X)               
F272: BF ; ????
F273: A1 E9           LDA     ($E9,X)               
F275: E9 3F           SBC     #$3F                  
F277: 14 ; ????
F278: 21 00           AND     ($00,X)               
F27A: 00              BRK                         
F27B: 00              BRK                         
F27C: 00              BRK                         
F27D: 00              BRK                         
F27E: 00              BRK                         
F27F: 00              BRK                         
F280: 00              BRK                         
F281: 00              BRK                         
F282: 00              BRK                         
F283: 00              BRK                         
F284: 00              BRK                         
F285: 00              BRK                         
F286: 00              BRK                         
F287: 00              BRK                         
F288: 00              BRK                         
F289: 00              BRK                         
F28A: 00              BRK                         
F28B: 00              BRK                         
F28C: 00              BRK                         
F28D: 00              BRK                         
F28E: 00              BRK                         
F28F: 00              BRK                         
F290: 00              BRK                         
F291: 00              BRK                         
F292: 00              BRK                         
F293: 00              BRK                         
F294: 00              BRK                         
F295: 00              BRK                         
F296: 00              BRK                         
F297: 00              BRK                         
F298: 00              BRK                         
F299: 00              BRK                         
F29A: 00              BRK                         
F29B: 00              BRK                         
F29C: 00              BRK                         
F29D: 00              BRK                         
F29E: 00              BRK                         
F29F: 00              BRK                         
F2A0: 00              BRK                         
F2A1: 00              BRK                         
F2A2: 00              BRK                         
F2A3: 00              BRK                         
F2A4: 00              BRK                         
F2A5: 00              BRK                         
F2A6: 00              BRK                         
F2A7: 00              BRK                         
F2A8: 00              BRK                         
F2A9: 00              BRK                         
F2AA: 00              BRK                         
F2AB: 00              BRK                         
F2AC: 00              BRK                         
F2AD: 00              BRK                         
F2AE: 00              BRK                         
F2AF: 00              BRK                         
F2B0: 00              BRK                         
F2B1: 00              BRK                         
F2B2: 00              BRK                         
F2B3: 00              BRK                         
F2B4: 00              BRK                         
F2B5: 00              BRK                         
F2B6: 00              BRK                         
F2B7: 00              BRK                         
F2B8: 00              BRK                         
F2B9: 00              BRK                         
F2BA: 00              BRK                         
F2BB: 00              BRK                         
F2BC: 00              BRK                         
F2BD: 00              BRK                         
F2BE: 00              BRK                         
F2BF: 00              BRK                         
F2C0: 00              BRK                         
F2C1: 00              BRK                         
F2C2: 00              BRK                         
F2C3: 00              BRK                         
F2C4: 00              BRK                         
F2C5: 00              BRK                         
F2C6: 00              BRK                         
F2C7: 00              BRK                         
F2C8: 00              BRK                         
F2C9: 00              BRK                         
F2CA: 00              BRK                         
F2CB: 00              BRK                         
F2CC: 00              BRK                         
F2CD: 00              BRK                         
F2CE: 00              BRK                         
F2CF: 00              BRK                         
F2D0: 00              BRK                         
F2D1: 00              BRK                         
F2D2: 00              BRK                         
F2D3: 00              BRK                         
F2D4: 00              BRK                         
F2D5: 00              BRK                         
F2D6: 00              BRK                         
F2D7: 00              BRK                         
F2D8: 00              BRK                         
F2D9: 00              BRK                         
F2DA: 00              BRK                         
F2DB: 00              BRK                         
F2DC: 00              BRK                         
F2DD: 00              BRK                         
F2DE: 00              BRK                         
F2DF: 00              BRK                         
F2E0: 00              BRK                         
F2E1: 00              BRK                         
F2E2: 60              RTS                         
F2E3: 26 00           ROL     $00                   
F2E5: 3C ; ????
F2E6: 3C ; ????
F2E7: BC BD 67        LDY     $67BD,X                 
F2EA: 00              BRK                         
F2EB: 3C ; ????
F2EC: 00              BRK                         
F2ED: 00              BRK                         
F2EE: 3C ; ????
F2EF: 3C ; ????
F2F0: 7E 7E 00        ROR     $007E,X                 
F2F3: 00              BRK                         
F2F4: 00              BRK                         
F2F5: 00              BRK                         
F2F6: 00              BRK                         
F2F7: 00              BRK                         
F2F8: 00              BRK                         
F2F9: 00              BRK                         
F2FA: 00              BRK                         
F2FB: 00              BRK                         
F2FC: 00              BRK                         
F2FD: 00              BRK                         
F2FE: 00              BRK                         
F2FF: 00              BRK                         
F300: 00              BRK                         
F301: 00              BRK                         
F302: 00              BRK                         
F303: 00              BRK                         
F304: 00              BRK                         
F305: 00              BRK                         
F306: 00              BRK                         
F307: 00              BRK                         
F308: 00              BRK                         
F309: 00              BRK                         
F30A: 00              BRK                         
F30B: 00              BRK                         
F30C: 00              BRK                         
F30D: 00              BRK                         
F30E: 00              BRK                         
F30F: 00              BRK                         
F310: 00              BRK                         
F311: 00              BRK                         
F312: 00              BRK                         
F313: 00              BRK                         
F314: 00              BRK                         
F315: 00              BRK                         
F316: 00              BRK                         
F317: 00              BRK                         
F318: 00              BRK                         
F319: 00              BRK                         
F31A: 00              BRK                         
F31B: 00              BRK                         
F31C: 00              BRK                         
F31D: 00              BRK                         
F31E: 00              BRK                         
F31F: 00              BRK                         
F320: 00              BRK                         
F321: 00              BRK                         
F322: 00              BRK                         
F323: 00              BRK                         
F324: 00              BRK                         
F325: 00              BRK                         
F326: 00              BRK                         
F327: 00              BRK                         
F328: 00              BRK                         
F329: 00              BRK                         
F32A: 00              BRK                         
F32B: 00              BRK                         
F32C: 00              BRK                         
F32D: 00              BRK                         
F32E: 00              BRK                         
F32F: 00              BRK                         
F330: 00              BRK                         
F331: 00              BRK                         
F332: 00              BRK                         
F333: 00              BRK                         
F334: 00              BRK                         
F335: 00              BRK                         
F336: 00              BRK                         
F337: 00              BRK                         
F338: 00              BRK                         
F339: 00              BRK                         
F33A: 00              BRK                         
F33B: 00              BRK                         
F33C: 00              BRK                         
F33D: 00              BRK                         
F33E: 00              BRK                         
F33F: 00              BRK                         
F340: 00              BRK                         
F341: 00              BRK                         
F342: 00              BRK                         
F343: 00              BRK                         
F344: 00              BRK                         
F345: 00              BRK                         
F346: 00              BRK                         
F347: 00              BRK                         
F348: 00              BRK                         
F349: 00              BRK                         
F34A: 00              BRK                         
F34B: 00              BRK                         
F34C: 00              BRK                         
F34D: 00              BRK                         
F34E: 00              BRK                         
F34F: 00              BRK                         
F350: 00              BRK                         
F351: 00              BRK                         
F352: 00              BRK                         
F353: 00              BRK                         
F354: 00              BRK                         
F355: 00              BRK                         
F356: 00              BRK                         
F357: 00              BRK                         
F358: 00              BRK                         
F359: 00              BRK                         
F35A: 00              BRK                         
F35B: 00              BRK                         
F35C: 00              BRK                         
F35D: 00              BRK                         
F35E: 00              BRK                         
F35F: 00              BRK                         
F360: 00              BRK                         
F361: 00              BRK                         
F362: 00              BRK                         
F363: 00              BRK                         
F364: 00              BRK                         
F365: 00              BRK                         
F366: 00              BRK                         
F367: 00              BRK                         
F368: 00              BRK                         
F369: 60              RTS                         
F36A: 63 ; ????
F36B: 03 ; ????
F36C: 18              CLC                         
F36D: 18              CLC                         
F36E: B0 B6           BCS     $F326                   
F370: 06 60           ASL     $60                   
F372: 60              RTS                         
F373: 0B ; ????
F374: 0B ; ????
F375: 00              BRK                         
F376: B0 B0           BCS     $F328                   
F378: 00              BRK                         
F379: 00              BRK                         
F37A: 00              BRK                         
F37B: 00              BRK                         
F37C: 00              BRK                         
F37D: 00              BRK                         
F37E: 00              BRK                         
F37F: 00              BRK                         
F380: 00              BRK                         
F381: 00              BRK                         
F382: 00              BRK                         
F383: 00              BRK                         
F384: 00              BRK                         
F385: 00              BRK                         
F386: 00              BRK                         
F387: 00              BRK                         
F388: 00              BRK                         
F389: 00              BRK                         
F38A: 00              BRK                         
F38B: 00              BRK                         
F38C: 00              BRK                         
F38D: 00              BRK                         
F38E: 00              BRK                         
F38F: 00              BRK                         
F390: 00              BRK                         
F391: 00              BRK                         
F392: 00              BRK                         
F393: 00              BRK                         
F394: 00              BRK                         
F395: 00              BRK                         
F396: 00              BRK                         
F397: 00              BRK                         
F398: 00              BRK                         
F399: 00              BRK                         
F39A: 00              BRK                         
F39B: 00              BRK                         
F39C: 00              BRK                         
F39D: 00              BRK                         
F39E: 00              BRK                         
F39F: 00              BRK                         
F3A0: 00              BRK                         
F3A1: 00              BRK                         
F3A2: 00              BRK                         
F3A3: 00              BRK                         
F3A4: 00              BRK                         
F3A5: 00              BRK                         
F3A6: 00              BRK                         
F3A7: 00              BRK                         
F3A8: 00              BRK                         
F3A9: 00              BRK                         
F3AA: 00              BRK                         
F3AB: 00              BRK                         
F3AC: 00              BRK                         
F3AD: 00              BRK                         
F3AE: 00              BRK                         
F3AF: 00              BRK                         
F3B0: 00              BRK                         
F3B1: 00              BRK                         
F3B2: 00              BRK                         
F3B3: 00              BRK                         
F3B4: 00              BRK                         
F3B5: 00              BRK                         
F3B6: 00              BRK                         
F3B7: 00              BRK                         
F3B8: 00              BRK                         
F3B9: 00              BRK                         
F3BA: 00              BRK                         
F3BB: 00              BRK                         
F3BC: 00              BRK                         
F3BD: 00              BRK                         
F3BE: 00              BRK                         
F3BF: 00              BRK                         
F3C0: 00              BRK                         
F3C1: 00              BRK                         
F3C2: 00              BRK                         
F3C3: 00              BRK                         
F3C4: 00              BRK                         
F3C5: 00              BRK                         
F3C6: 00              BRK                         
F3C7: 00              BRK                         
F3C8: 00              BRK                         
F3C9: 00              BRK                         
F3CA: 00              BRK                         
F3CB: 00              BRK                         
F3CC: 00              BRK                         
F3CD: 00              BRK                         
F3CE: 00              BRK                         
F3CF: 00              BRK                         
F3D0: 00              BRK                         
F3D1: 00              BRK                         
F3D2: 00              BRK                         
F3D3: 00              BRK                         
F3D4: 00              BRK                         
F3D5: 00              BRK                         
F3D6: 00              BRK                         
F3D7: 00              BRK                         
F3D8: 00              BRK                         
F3D9: 00              BRK                         
F3DA: 00              BRK                         
F3DB: 00              BRK                         
F3DC: 00              BRK                         
F3DD: 00              BRK                         
F3DE: 00              BRK                         
F3DF: 00              BRK                         
F3E0: 00              BRK                         
F3E1: 00              BRK                         
F3E2: 06 64           ASL     $64                   
F3E4: 00              BRK                         
F3E5: 3C ; ????
F3E6: 3C ; ????
F3E7: 3D A5 C2        AND     $C2A5,X                 
F3EA: 3C ; ????
F3EB: 00              BRK                         
F3EC: 00              BRK                         
F3ED: 3C ; ????
F3EE: 3C ; ????
F3EF: 7E 7E 00        ROR     $007E,X                 
F3F2: 00              BRK                         
F3F3: 00              BRK                         
F3F4: 00              BRK                         
F3F5: 00              BRK                         
F3F6: 00              BRK                         
F3F7: 00              BRK                         
F3F8: 00              BRK                         
F3F9: 00              BRK                         
F3FA: 00              BRK                         
F3FB: 00              BRK                         
F3FC: 00              BRK                         
F3FD: 00              BRK                         
F3FE: 00              BRK                         
F3FF: 00              BRK                         
F400: 00              BRK                         
F401: 00              BRK                         
F402: 00              BRK                         
F403: 00              BRK                         
F404: 00              BRK                         
F405: 00              BRK                         
F406: 00              BRK                         
F407: 00              BRK                         
F408: 00              BRK                         
F409: 00              BRK                         
F40A: 00              BRK                         
F40B: 00              BRK                         
F40C: 00              BRK                         
F40D: 00              BRK                         
F40E: 00              BRK                         
F40F: 00              BRK                         
F410: 00              BRK                         
F411: 00              BRK                         
F412: 00              BRK                         
F413: 00              BRK                         
F414: 00              BRK                         
F415: 00              BRK                         
F416: 00              BRK                         
F417: 00              BRK                         
F418: 00              BRK                         
F419: 00              BRK                         
F41A: 00              BRK                         
F41B: 00              BRK                         
F41C: 00              BRK                         
F41D: 00              BRK                         
F41E: 00              BRK                         
F41F: 00              BRK                         
F420: 00              BRK                         
F421: 00              BRK                         
F422: 00              BRK                         
F423: 00              BRK                         
F424: 00              BRK                         
F425: 00              BRK                         
F426: 00              BRK                         
F427: 00              BRK                         
F428: 00              BRK                         
F429: 00              BRK                         
F42A: 00              BRK                         
F42B: 00              BRK                         
F42C: 00              BRK                         
F42D: 00              BRK                         
F42E: 00              BRK                         
F42F: 00              BRK                         
F430: 00              BRK                         
F431: 00              BRK                         
F432: 00              BRK                         
F433: 00              BRK                         
F434: 00              BRK                         
F435: 00              BRK                         
F436: 00              BRK                         
F437: 00              BRK                         
F438: 00              BRK                         
F439: 00              BRK                         
F43A: 00              BRK                         
F43B: 00              BRK                         
F43C: 00              BRK                         
F43D: 00              BRK                         
F43E: 00              BRK                         
F43F: 00              BRK                         
F440: 00              BRK                         
F441: 00              BRK                         
F442: 00              BRK                         
F443: 00              BRK                         
F444: 00              BRK                         
F445: 00              BRK                         
F446: 00              BRK                         
F447: 00              BRK                         
F448: 00              BRK                         
F449: 00              BRK                         
F44A: 00              BRK                         
F44B: 00              BRK                         
F44C: 00              BRK                         
F44D: 00              BRK                         
F44E: 00              BRK                         
F44F: 00              BRK                         
F450: 00              BRK                         
F451: 00              BRK                         
F452: 00              BRK                         
F453: 00              BRK                         
F454: 00              BRK                         
F455: 00              BRK                         
F456: 00              BRK                         
F457: 00              BRK                         
F458: 00              BRK                         
F459: 00              BRK                         
F45A: 00              BRK                         
F45B: 00              BRK                         
F45C: 00              BRK                         
F45D: 00              BRK                         
F45E: 00              BRK                         
F45F: 00              BRK                         
F460: 00              BRK                         
F461: 00              BRK                         
F462: 00              BRK                         
F463: 00              BRK                         
F464: 00              BRK                         
F465: 00              BRK                         
F466: 00              BRK                         
F467: 00              BRK                         
F468: 00              BRK                         
F469: 0E 02 E2        ASL     $E202                   
F46C: 1C ; ????
F46D: 3E 3E 3F        ROL     $3F3E,X                 
F470: 1F ; ????
F471: 0F ; ????
F472: 0F ; ????
F473: 0F ; ????
F474: 1F ; ????
F475: 3F ; ????
F476: 16 3E           ASL     $3E,X                 
F478: 1C ; ????
F479: 00              BRK                         
F47A: 00              BRK                         
F47B: 00              BRK                         
F47C: 00              BRK                         
F47D: 00              BRK                         
F47E: 00              BRK                         
F47F: 00              BRK                         
F480: 00              BRK                         
F481: 00              BRK                         
F482: 00              BRK                         
F483: 00              BRK                         
F484: 00              BRK                         
F485: 00              BRK                         
F486: 00              BRK                         
F487: 00              BRK                         
F488: 00              BRK                         
F489: 00              BRK                         
F48A: 00              BRK                         
F48B: 00              BRK                         
F48C: 00              BRK                         
F48D: 00              BRK                         
F48E: 00              BRK                         
F48F: 00              BRK                         
F490: 00              BRK                         
F491: 00              BRK                         
F492: 00              BRK                         
F493: 00              BRK                         
F494: 00              BRK                         
F495: 00              BRK                         
F496: 00              BRK                         
F497: 00              BRK                         
F498: 00              BRK                         
F499: 00              BRK                         
F49A: 00              BRK                         
F49B: 00              BRK                         
F49C: 00              BRK                         
F49D: 00              BRK                         
F49E: 00              BRK                         
F49F: 00              BRK                         
F4A0: 00              BRK                         
F4A1: 00              BRK                         
F4A2: 00              BRK                         
F4A3: 00              BRK                         
F4A4: 00              BRK                         
F4A5: 00              BRK                         
F4A6: 00              BRK                         
F4A7: 00              BRK                         
F4A8: 00              BRK                         
F4A9: 00              BRK                         
F4AA: 00              BRK                         
F4AB: 00              BRK                         
F4AC: 00              BRK                         
F4AD: 00              BRK                         
F4AE: 00              BRK                         
F4AF: 00              BRK                         
F4B0: 00              BRK                         
F4B1: 00              BRK                         
F4B2: 00              BRK                         
F4B3: 00              BRK                         
F4B4: 00              BRK                         
F4B5: 00              BRK                         
F4B6: 00              BRK                         
F4B7: 00              BRK                         
F4B8: 00              BRK                         
F4B9: 00              BRK                         
F4BA: 00              BRK                         
F4BB: 00              BRK                         
F4BC: 00              BRK                         
F4BD: 00              BRK                         
F4BE: 00              BRK                         
F4BF: 00              BRK                         
F4C0: 00              BRK                         
F4C1: 00              BRK                         
F4C2: 00              BRK                         
F4C3: 00              BRK                         
F4C4: 00              BRK                         
F4C5: 00              BRK                         
F4C6: 00              BRK                         
F4C7: 00              BRK                         
F4C8: 00              BRK                         
F4C9: 00              BRK                         
F4CA: 00              BRK                         
F4CB: 00              BRK                         
F4CC: 00              BRK                         
F4CD: 00              BRK                         
F4CE: 00              BRK                         
F4CF: 00              BRK                         
F4D0: 00              BRK                         
F4D1: 00              BRK                         
F4D2: 00              BRK                         
F4D3: 00              BRK                         
F4D4: 00              BRK                         
F4D5: 00              BRK                         
F4D6: 00              BRK                         
F4D7: 00              BRK                         
F4D8: 00              BRK                         
F4D9: 00              BRK                         
F4DA: 00              BRK                         
F4DB: 00              BRK                         
F4DC: 00              BRK                         
F4DD: 00              BRK                         
F4DE: 00              BRK                         
F4DF: 00              BRK                         
F4E0: 00              BRK                         
F4E1: 00              BRK                         
F4E2: 60              RTS                         
F4E3: 26 00           ROL     $00                   
F4E5: 3C ; ????
F4E6: 3C ; ????
F4E7: BC A9 64        LDY     $64A9,X                 
F4EA: 18              CLC                         
F4EB: 3C ; ????
F4EC: 14 ; ????
F4ED: 00              BRK                         
F4EE: 3C ; ????
F4EF: 3C ; ????
F4F0: 7E 7E 00        ROR     $007E,X                 
F4F3: 00              BRK                         
F4F4: 00              BRK                         
F4F5: 00              BRK                         
F4F6: 00              BRK                         
F4F7: 00              BRK                         
F4F8: 00              BRK                         
F4F9: 00              BRK                         
F4FA: 00              BRK                         
F4FB: 00              BRK                         
F4FC: 00              BRK                         
F4FD: 00              BRK                         
F4FE: 00              BRK                         
F4FF: 00              BRK                         
F500: 00              BRK                         
F501: 00              BRK                         
F502: 00              BRK                         
F503: 00              BRK                         
F504: 00              BRK                         
F505: 00              BRK                         
F506: 00              BRK                         
F507: 00              BRK                         
F508: 00              BRK                         
F509: 00              BRK                         
F50A: 00              BRK                         
F50B: 00              BRK                         
F50C: 00              BRK                         
F50D: 00              BRK                         
F50E: 00              BRK                         
F50F: 00              BRK                         
F510: 00              BRK                         
F511: 00              BRK                         
F512: 00              BRK                         
F513: 00              BRK                         
F514: 00              BRK                         
F515: 00              BRK                         
F516: 00              BRK                         
F517: 00              BRK                         
F518: 00              BRK                         
F519: 00              BRK                         
F51A: 00              BRK                         
F51B: 00              BRK                         
F51C: 00              BRK                         
F51D: 00              BRK                         
F51E: 00              BRK                         
F51F: 00              BRK                         
F520: 00              BRK                         
F521: 00              BRK                         
F522: 00              BRK                         
F523: 00              BRK                         
F524: 00              BRK                         
F525: 00              BRK                         
F526: 00              BRK                         
F527: 00              BRK                         
F528: 00              BRK                         
F529: 00              BRK                         
F52A: 00              BRK                         
F52B: 00              BRK                         
F52C: 00              BRK                         
F52D: 00              BRK                         
F52E: 00              BRK                         
F52F: 00              BRK                         
F530: 00              BRK                         
F531: 00              BRK                         
F532: 00              BRK                         
F533: 00              BRK                         
F534: 00              BRK                         
F535: 00              BRK                         
F536: 00              BRK                         
F537: 00              BRK                         
F538: 00              BRK                         
F539: 00              BRK                         
F53A: 00              BRK                         
F53B: 00              BRK                         
F53C: 00              BRK                         
F53D: 00              BRK                         
F53E: 00              BRK                         
F53F: 00              BRK                         
F540: 00              BRK                         
F541: 00              BRK                         
F542: 00              BRK                         
F543: 00              BRK                         
F544: 00              BRK                         
F545: 00              BRK                         
F546: 00              BRK                         
F547: 00              BRK                         
F548: 00              BRK                         
F549: 00              BRK                         
F54A: 00              BRK                         
F54B: 00              BRK                         
F54C: 00              BRK                         
F54D: 00              BRK                         
F54E: 00              BRK                         
F54F: 00              BRK                         
F550: 00              BRK                         
F551: 00              BRK                         
F552: 00              BRK                         
F553: 00              BRK                         
F554: 00              BRK                         
F555: 00              BRK                         
F556: 00              BRK                         
F557: 00              BRK                         
F558: 00              BRK                         
F559: 00              BRK                         
F55A: 00              BRK                         
F55B: 00              BRK                         
F55C: 00              BRK                         
F55D: 00              BRK                         
F55E: 00              BRK                         
F55F: 00              BRK                         
F560: 00              BRK                         
F561: 00              BRK                         
F562: 00              BRK                         
F563: 00              BRK                         
F564: 00              BRK                         
F565: 00              BRK                         
F566: 00              BRK                         
F567: 00              BRK                         
F568: 00              BRK                         
F569: 70 48           BVS     $F5B3                   
F56B: 47 ; ????
F56C: 38              SEC                         
F56D: 7C ; ????
F56E: 7C ; ????
F56F: FC ; ????
F570: F8              SED                         
F571: F0 F0           BEQ     $F563                   
F573: F0 F8           BEQ     $F56D                   
F575: FC ; ????
F576: 68              PLA                         
F577: FC ; ????
F578: 38              SEC                         
F579: 00              BRK                         
F57A: 00              BRK                         
F57B: 00              BRK                         
F57C: 00              BRK                         
F57D: 00              BRK                         
F57E: 00              BRK                         
F57F: 00              BRK                         
F580: 00              BRK                         
F581: 00              BRK                         
F582: 00              BRK                         
F583: 00              BRK                         
F584: 00              BRK                         
F585: 00              BRK                         
F586: 00              BRK                         
F587: 00              BRK                         
F588: 00              BRK                         
F589: 00              BRK                         
F58A: 00              BRK                         
F58B: 00              BRK                         
F58C: 00              BRK                         
F58D: 00              BRK                         
F58E: 00              BRK                         
F58F: 00              BRK                         
F590: 00              BRK                         
F591: 00              BRK                         
F592: 00              BRK                         
F593: 00              BRK                         
F594: 00              BRK                         
F595: 00              BRK                         
F596: 00              BRK                         
F597: 00              BRK                         
F598: 00              BRK                         
F599: 00              BRK                         
F59A: 00              BRK                         
F59B: 00              BRK                         
F59C: 00              BRK                         
F59D: 00              BRK                         
F59E: 00              BRK                         
F59F: 00              BRK                         
F5A0: 00              BRK                         
F5A1: 00              BRK                         
F5A2: 00              BRK                         
F5A3: 00              BRK                         
F5A4: 00              BRK                         
F5A5: 00              BRK                         
F5A6: 00              BRK                         
F5A7: 00              BRK                         
F5A8: 00              BRK                         
F5A9: 00              BRK                         
F5AA: 00              BRK                         
F5AB: 00              BRK                         
F5AC: 00              BRK                         
F5AD: 00              BRK                         
F5AE: 00              BRK                         
F5AF: 00              BRK                         
F5B0: 00              BRK                         
F5B1: 00              BRK                         
F5B2: 00              BRK                         
F5B3: 00              BRK                         
F5B4: 00              BRK                         
F5B5: 00              BRK                         
F5B6: 00              BRK                         
F5B7: 00              BRK                         
F5B8: 00              BRK                         
F5B9: 00              BRK                         
F5BA: 00              BRK                         
F5BB: 00              BRK                         
F5BC: 00              BRK                         
F5BD: 00              BRK                         
F5BE: 00              BRK                         
F5BF: 00              BRK                         
F5C0: 00              BRK                         
F5C1: 00              BRK                         
F5C2: 00              BRK                         
F5C3: 00              BRK                         
F5C4: 00              BRK                         
F5C5: 00              BRK                         
F5C6: 00              BRK                         
F5C7: 00              BRK                         
F5C8: 00              BRK                         
F5C9: 00              BRK                         
F5CA: 00              BRK                         
F5CB: 00              BRK                         
F5CC: 00              BRK                         
F5CD: 00              BRK                         
F5CE: 00              BRK                         
F5CF: 00              BRK                         
F5D0: 00              BRK                         
F5D1: 00              BRK                         
F5D2: 00              BRK                         
F5D3: 00              BRK                         
F5D4: 00              BRK                         
F5D5: 00              BRK                         
F5D6: 00              BRK                         
F5D7: 00              BRK                         
F5D8: 00              BRK                         
F5D9: 00              BRK                         
F5DA: 00              BRK                         
F5DB: 00              BRK                         
F5DC: 00              BRK                         
F5DD: 00              BRK                         
F5DE: 00              BRK                         
F5DF: 00              BRK                         
F5E0: 00              BRK                         
F5E1: 00              BRK                         
F5E2: 06 34           ASL     $34                   
F5E4: 00              BRK                         
F5E5: 3E 26 3E        ROL     $3E26,X                 
F5E8: 3A ; ????
F5E9: 3C ; ????
F5EA: 00              BRK                         
F5EB: 1C ; ????
F5EC: 1A ; ????
F5ED: 00              BRK                         
F5EE: 3C ; ????
F5EF: 3C ; ????
F5F0: 7E 7E 00        ROR     $007E,X                 
F5F3: 00              BRK                         
F5F4: 00              BRK                         
F5F5: 00              BRK                         
F5F6: 00              BRK                         
F5F7: 00              BRK                         
F5F8: 00              BRK                         
F5F9: 00              BRK                         
F5FA: 00              BRK                         
F5FB: 00              BRK                         
F5FC: 00              BRK                         
F5FD: 00              BRK                         
F5FE: 00              BRK                         
F5FF: 00              BRK                         
F600: 00              BRK                         
F601: 00              BRK                         
F602: 00              BRK                         
F603: 00              BRK                         
F604: 00              BRK                         
F605: 00              BRK                         
F606: 00              BRK                         
F607: 00              BRK                         
F608: 00              BRK                         
F609: 00              BRK                         
F60A: 00              BRK                         
F60B: 00              BRK                         
F60C: 00              BRK                         
F60D: 00              BRK                         
F60E: 00              BRK                         
F60F: 00              BRK                         
F610: 00              BRK                         
F611: 00              BRK                         
F612: 00              BRK                         
F613: 00              BRK                         
F614: 00              BRK                         
F615: 00              BRK                         
F616: 00              BRK                         
F617: 00              BRK                         
F618: 00              BRK                         
F619: 00              BRK                         
F61A: 00              BRK                         
F61B: 00              BRK                         
F61C: 00              BRK                         
F61D: 00              BRK                         
F61E: 00              BRK                         
F61F: 00              BRK                         
F620: 00              BRK                         
F621: 00              BRK                         
F622: 00              BRK                         
F623: 00              BRK                         
F624: 00              BRK                         
F625: 00              BRK                         
F626: 00              BRK                         
F627: 00              BRK                         
F628: 00              BRK                         
F629: 00              BRK                         
F62A: 00              BRK                         
F62B: 00              BRK                         
F62C: 00              BRK                         
F62D: 00              BRK                         
F62E: 00              BRK                         
F62F: 00              BRK                         
F630: 00              BRK                         
F631: 00              BRK                         
F632: 00              BRK                         
F633: 00              BRK                         
F634: 00              BRK                         
F635: 00              BRK                         
F636: 00              BRK                         
F637: 00              BRK                         
F638: 00              BRK                         
F639: 00              BRK                         
F63A: 00              BRK                         
F63B: 00              BRK                         
F63C: 00              BRK                         
F63D: 00              BRK                         
F63E: 00              BRK                         
F63F: 00              BRK                         
F640: 00              BRK                         
F641: 00              BRK                         
F642: 00              BRK                         
F643: 00              BRK                         
F644: 00              BRK                         
F645: 00              BRK                         
F646: 00              BRK                         
F647: 00              BRK                         
F648: 00              BRK                         
F649: 00              BRK                         
F64A: 00              BRK                         
F64B: 00              BRK                         
F64C: 00              BRK                         
F64D: 00              BRK                         
F64E: 00              BRK                         
F64F: 00              BRK                         
F650: 00              BRK                         
F651: 00              BRK                         
F652: 00              BRK                         
F653: 00              BRK                         
F654: 00              BRK                         
F655: 00              BRK                         
F656: 00              BRK                         
F657: 00              BRK                         
F658: 00              BRK                         
F659: 00              BRK                         
F65A: 00              BRK                         
F65B: 5A ; ????
F65C: 9C ; ????
F65D: AD 56 F9        LDA     $F956                   
F660: 29 01           AND     #$01                  
F662: D0 0F           BNE     $F673                   
F664: 18              CLC                         
F665: AD 0C F9        LDA     $F90C                   
F668: 65 C2           ADC     $C2                   
F66A: 85 E4           STA     $E4                   
F66C: AD 0D F9        LDA     $F90D                   
F66F: 69 00           ADC     #$00                  
F671: 85 E5           STA     $E5                   
F673: 85 02           STA     $02                   
F675: AD 35 F9        LDA     $F935                   
F678: D0 1C           BNE     $F696                   
F67A: AD 6F F9        LDA     $F96F                   
F67D: 85 F2           STA     $F2                   
F67F: AD 70 F9        LDA     $F970                   
F682: 85 F3           STA     $F3                   
F684: AD 71 F9        LDA     $F971                   
F687: 85 F4           STA     $F4                   
F689: AE 08 F9        LDX     $F908                   
F68C: BD 5B F6        LDA     $F65B,X                 
F68F: 85 06           STA     $06                   
F691: 85 07           STA     $07                   
F693: 4C B1 F6        JMP     $F6B1                   
F696: 38              SEC                         
F697: E9 01           SBC     #$01                  
F699: 8D 35 F8        STA     $F835                   
F69C: AD 32 F9        LDA     $F932                   
F69F: 85 F2           STA     $F2                   
F6A1: AD 33 F9        LDA     $F933                   
F6A4: 85 F3           STA     $F3                   
F6A6: AD 34 F9        LDA     $F934                   
F6A9: 85 F4           STA     $F4                   
F6AB: A9 2F           LDA     #$2F                  
F6AD: 85 06           STA     $06                   
F6AF: 85 07           STA     $07                   
F6B1: A2 05           LDX     #$05                  
F6B3: 20 96 F7        JSR     $F796                   
F6B6: 20 DD F7        JSR     $F7DD                   
F6B9: A9 1A           LDA     #$1A                  
F6BB: 85 08           STA     $08                   
F6BD: A9 00           LDA     #$00                  
F6BF: 85 89           STA     $89                   
F6C1: 85 8A           STA     $8A                   
F6C3: 85 8B           STA     $8B                   
F6C5: 85 8C           STA     $8C                   
F6C7: 85 81           STA     $81                   
F6C9: 85 82           STA     $82                   
F6CB: 85 83           STA     $83                   
F6CD: 85 84           STA     $84                   
F6CF: 85 1D           STA     $1D                   
F6D1: 85 1E           STA     $1E                   
F6D3: 85 1F           STA     $1F                   
F6D5: 60              RTS                         
F6D6: 02 ; ????
F6D7: A9 00           LDA     #$00                  
F6D9: A0 00           LDY     #$00                  
F6DB: A2 00           LDX     #$00                  
F6DD: 85 02           STA     $02                   
F6DF: 85 09           STA     $09                   
F6E1: 85 09           STA     $09                   
F6E3: 84 0A           STY     $0A                   
F6E5: A9 10           LDA     #$10                  
F6E7: 85 20           STA     $20                   
F6E9: A9 20           LDA     #$20                  
F6EB: 85 21           STA     $21                   
F6ED: AC D6 F6        LDY     $F6D6                   
F6F0: EA              NOP                         
F6F1: 88              DEY                         
F6F2: D0 FC           BNE     $F6F0                   
F6F4: 85 10           STA     $10                   
F6F6: 85 11           STA     $11                   
F6F8: 85 02           STA     $02                   
F6FA: 85 2A           STA     $2A                   
F6FC: A9 01           LDA     #$01                  
F6FE: 85 25           STA     $25                   
F700: 85 26           STA     $26                   
F702: A9 00           LDA     #$00                  
F704: 85 02           STA     $02                   
F706: 85 01           STA     $01                   
F708: 85 1B           STA     $1B                   
F70A: 85 1C           STA     $1C                   
F70C: 85 1B           STA     $1B                   
F70E: 85 0B           STA     $0B                   
F710: 85 0C           STA     $0C                   
F712: A0 05           LDY     #$05                  
F714: A9 03           LDA     #$03                  
F716: 85 04           STA     $04                   
F718: 85 05           STA     $05                   
F71A: 85 2B           STA     $2B                   
F71C: B1 DC           LDA     ($DC),Y               
F71E: AA              TAX                         
F71F: B1 D2           LDA     ($D2),Y               
F721: 85 02           STA     $02                   
F723: 84 C7           STY     $C7                   
F725: 84 C7           STY     $C7                   
F727: 85 1B           STA     $1B                   
F729: B1 D4           LDA     ($D4),Y               
F72B: 85 1C           STA     $1C                   
F72D: B1 D6           LDA     ($D6),Y               
F72F: 85 1B           STA     $1B                   
F731: B1 D8           LDA     ($D8),Y               
F733: 85 C8           STA     $C8                   
F735: B1 DA           LDA     ($DA),Y               
F737: A4 C8           LDY     $C8                   
F739: 84 1C           STY     $1C                   
F73B: 85 1B           STA     $1B                   
F73D: 86 1C           STX     $1C                   
F73F: 86 1B           STX     $1B                   
F741: A4 C7           LDY     $C7                   
F743: 88              DEY                         
F744: 10 D6           BPL     $F71C                   
F746: A9 00           LDA     #$00                  
F748: 85 1B           STA     $1B                   
F74A: 85 1C           STA     $1C                   
F74C: 85 1B           STA     $1B                   
F74E: 60              RTS                         
F74F: B1 D8           LDA     ($D8),Y               
F751: AA              TAX                         
F752: B1 D2           LDA     ($D2),Y               
F754: 85 02           STA     $02                   
F756: 84 C7           STY     $C7                   
F758: 84 C7           STY     $C7                   
F75A: 85 1B           STA     $1B                   
F75C: B1 D4           LDA     ($D4),Y               
F75E: 85 1C           STA     $1C                   
F760: A9 00           LDA     #$00                  
F762: 85 1B           STA     $1B                   
F764: 85 C8           STA     $C8                   
F766: 85 C8           STA     $C8                   
F768: 85 C8           STA     $C8                   
F76A: EA              NOP                         
F76B: B1 D6           LDA     ($D6),Y               
F76D: A4 C8           LDY     $C8                   
F76F: 84 1C           STY     $1C                   
F771: 85 1B           STA     $1B                   
F773: 86 1C           STX     $1C                   
F775: 86 1B           STX     $1B                   
F777: A4 C7           LDY     $C7                   
F779: 88              DEY                         
F77A: 10 D3           BPL     $F74F                   
F77C: A9 00           LDA     #$00                  
F77E: 85 25           STA     $25                   
F780: 85 26           STA     $26                   
F782: 85 1B           STA     $1B                   
F784: 85 1C           STA     $1C                   
F786: A2 01           LDX     #$01                  
F788: B5 F0           LDA     $F0,X                 
F78A: 95 04           STA     $04,X                 
F78C: CA              DEX                         
F78D: 10 F9           BPL     $F788                   
F78F: 60              RTS                         

F790: F0 0F F0 0F F0 0F                 

F796: 8A              TXA                         
F797: 4A              LSR     A                   
F798: A8              TAY                         
F799: B9 F2 00        LDA     $00F2,Y                 
F79C: 3D 90 F7        AND     $F790,X                 
F79F: E0 03           CPX     #$03                  
F7A1: F0 0C           BEQ     $F7AF                   
F7A3: E0 01           CPX     #$01                  
F7A5: F0 08           BEQ     $F7AF                   
F7A7: E0 05           CPX     #$05                  
F7A9: F0 04           BEQ     $F7AF                   
F7AB: 4A              LSR     A                   
F7AC: 4A              LSR     A                   
F7AD: 4A              LSR     A                   
F7AE: 4A              LSR     A                   
F7AF: A8              TAY                         
F7B0: 18              CLC                         
F7B1: A9 80           LDA     #$80                  
F7B3: 79 CF F7        ADC     $F7CF,Y                 
F7B6: 85 C7           STA     $C7                   
F7B8: A9 FC           LDA     #$FC                  
F7BA: 69 00           ADC     #$00                  
F7BC: 85 C8           STA     $C8                   
F7BE: 8A              TXA                         
F7BF: 0A              ASL     A                   
F7C0: A8              TAY                         
F7C1: A5 C7           LDA     $C7                   
F7C3: 99 D2 00        STA     $00D2,Y                 
F7C6: A5 C8           LDA     $C8                   
F7C8: 99 D3 00        STA     $00D3,Y                 
F7CB: CA              DEX                         
F7CC: 10 C8           BPL     $F796                   
F7CE: 60              RTS                         


F7CF: 00              
F7D0: 06 0C       
F7D2: 12
F7D3: 18 
F7D4: 1E 24 2A        
F7D7: 30 36    
F7D9: 3C
F7DA: 42
F7DB: 48                  
F7DC: 4E AD 58           
F7DF: F9 85 C7        
F7E2: AD 57 F9
F7E5: 85 D1
F7E7: 60
F7E8: 1F
F7E9: D7
F7EA: 34
F7EB: 1F
F7EC: 18
F7ED: 3C 
F7EE: 3C 
F7EF: 3C 
F7F0: 00          
F7F1: 3C 
F7F2: 3C 
F7F3: 3C 
F7F4: 3C 
F7F5: 00
F7F6: 2C 1C 38
F7F9: 2C 00 3C
F7FC: 3C
F7FD: 3C
F7FE: 18                  
F7FF: 00                      
```