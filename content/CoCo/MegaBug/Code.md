../../content/CoCo/MegaBug/Code.md
../../content/CoCo/MegaBug\RAMUse.md
../../content/CoCo/MegaBug\../Hardware.md
../../content/CoCo/MegaBug/Code.md
../../content/CoCo/MegaBug\RAMUse.md
../../content/CoCo/MegaBug\../Hardware.md
![](megabug.jpg)

# Mega-Bug Code

>>> cpu 6809

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

```code
C000: 7E CF DE       JMP     $CFDE                          ; {Start} 
```

# Data

Looks like data from here to the start at CFDE.

```code
C003: 1C C0          ANDCC   #$C0            
C005: 91 00          CMPA    <$00            
C007: B1 00 59       CMPA    $0059           
C00A: B4 A3 54       ANDA    $A354           
C00D: 4A             DECA                    
C00E: E5 94          BITB    [,X]            
C010: 52                                  
C011: 71                                  
C012: 9E 94          LDX     <$94            
C014: 4D             TSTA                    
C015: 9B 7E          ADDA    <$7E            
C017: 8E 52 70       LDX     #$5270          
C01A: A4 71          ANDA    -15,S           
C01C: 7F 38 AD       CLR     $38AD           
C01F: 97 4E          STA     <$4E            
C021: 4A             DECA                    
C022: A1 7B          CMPA    -5,S            
C024: 61                                  
C025: 4A             DECA                    
C026: 98 8B          EORA    <$8B            
C028: 44             LSRA                    
C029: 4C             INCA                    
C02A: 9C 6B          CMPX    <$6B            
C02C: 63 49          COM     9,U             
C02E: A0 66          SUBA    6,S             
C030: 01                                  
C031: 02                                  
C032: 4F             CLRA                    
C033: 65                                  
C034: 80 75          SUBA    #$75            
C036: 53             COMB                    
C037: 4D             TSTA                    
C038: 87                                  
C039: 04 01          LSR     <$01            
C03B: 6C 58          INC     -8,U            
C03D: 58             LSLB                    
C03E: 72                                  
C03F: 77 4E 52       ASR     $4E52           
C042: 7B                                  
C043: 76 56 4B       ROR     $564B           
C046: 6B                                  
C047: 76 5A 46       ROR     $5A46           
C04A: 6E 74          JMP     -12,S           
C04C: 01                                  
C04D: 04 56          LSR     <$56            
C04F: 44             LSRA                    
C050: 65                                  
C051: 85 52          BITA    #$52            
C053: 0A 05          DEC     <$05            
C055: 12             NOP                     
C056: 7F 87 4B       CLR     $874B           
C059: 0B                                  
C05A: 0C 0D          INC     <$0D            
C05C: 7A 89 4A       DEC     $894A           
C05F: 0A 0C          DEC     <$0C            
C061: 0E 77          JMP     <$77            
C063: 87                                  
C064: 4C             INCA                    
C065: 0A 0C          DEC     <$0C            
C067: 0E 59          JMP     <$59            
C069: 02                                  
C06A: 16 88 0D       LBRA    $880D           
C06D: 04 36          LSR     <$36            
C06F: 09 0F          ROL     <$0F            
C071: 0F 53          CLR     <$53            
C073: 04 14          LSR     <$14            
C075: 10                                  
C076: 03 72          COM     <$72            
C078: 0C 08          INC     <$08            
C07A: 1E 01          EXG     $01             
C07C: 13             SYNC                    
C07D: 06 10          ROR     <$10            
C07F: 06 5B          ROR     <$5B            
C081: 04 12          LSR     <$12            
C083: 0A 0B          DEC     <$0B            
C085: 71                                  
C086: 0C 08          INC     <$08            
C088: 34 06          PSHS    B,A             
C08A: 0F 09          CLR     <$09            
C08C: 57             ASRB                    
C08D: 05                                  
C08E: 11                                  
C08F: 0A 0C          DEC     <$0C            
C091: 70 08 0D       NEG     $080D           
C094: 32 08          LEAS    8,X             
C096: 10                                  
C097: 08 16          ASL     <$16            
C099: 09 33          ROL     <$33            
C09B: 05                                  
C09C: 10                                  
C09D: 0B                                  
C09E: 0C 70          INC     <$70            
C0A0: 07 0E          ASR     <$0E            
C0A2: 31 08          LEAY    8,X             
C0A4: 11                                  
C0A5: 07 1A          ASR     <$1A            
C0A7: 01                                  
C0A8: 34 05          PSHS    B,CC            
C0AA: 11                                  
C0AB: 0A 0D          DEC     <$0D            
C0AD: 70 06 0E       NEG     $060E           
C0B0: 32 07          LEAS    7,X             
C0B2: 11                                  
C0B3: 06 51          ROR     <$51            
C0B5: 05                                  
C0B6: 12             NOP                     
C0B7: 0A 0C          DEC     <$0C            
C0B9: 71                                  
C0BA: 04 10          LSR     <$10            
C0BC: 0E 08          JMP     <$08            
C0BE: 1A 05          ORCC    #$05            
C0C0: 11                                  
C0C1: 07 4F          ASR     <$4F            
C0C3: 05                                  
C0C4: 10                                  
C0C5: 0B                                  
C0C6: 06 03          ROR     <$03            
C0C8: 01                                  
C0C9: 07 01          ASR     <$01            
C0CB: 64 04          LSR     4,X             
C0CD: 10                                  
C0CE: 0D 05          TST     <$05            
C0D0: 1F 02          TFR     D,Y             
C0D2: 14                                  
C0D3: 05                                  
C0D4: 4E                                  
C0D5: 05                                  
C0D6: 10                                  
C0D7: 0B                                  
C0D8: 06 0E          ROR     <$0E            
C0DA: 01                                  
C0DB: 66 02          ROR     2,X             
C0DD: 10                                  
C0DE: 0D 05          TST     <$05            
C0E0: 39             RTS                     
C0E1: 04 4D          LSR     <$4D            
C0E3: 05                                  
C0E4: 10                                  
C0E5: 0A 07          DEC     <$07            
C0E7: 0E 01          JMP     <$01            
C0E9: 66 02          ROR     2,X             
C0EB: 10                                  
C0EC: 0B                                  
C0ED: 08 37          ASL     <$37            
C0EF: 05                                  
C0F0: 4B                                  
C0F1: 05                                  
C0F2: 0F 0B          CLR     <$0B            
C0F4: 06 0E          ROR     <$0E            
C0F6: 02                                  
C0F7: 65                                  
C0F8: 02                                  
C0F9: 11                                  
C0FA: 0B                                  
C0FB: 08 37          ASL     <$37            
C0FD: 05                                  
C0FE: 4A             DECA                    
C0FF: 05                                  
C100: 0F 0B          CLR     <$0B            
C102: 06 0E          ROR     <$0E            
C104: 02                                  
C105: 7A 0C 07       DEC     $0C07           
C108: 38                                  
C109: 04 49          LSR     <$49            
C10B: 04 10          LSR     <$10            
C10D: 0B                                  
C10E: 06 0E          ROR     <$0E            
C110: 02                                  
C111: 7A 0C 07       DEC     $0C07           
C114: 86 04          LDA     #$04            
C116: 10                                  
C117: 0B                                  
C118: 06 0E          ROR     <$0E            
C11A: 02                                  
C11B: 7A 0B 09       DEC     $0B09           
C11E: 84 04          ANDA    #$04            
C120: 10                                  
C121: 0B                                  
C122: 06 0F          ROR     <$0F            
C124: 01                                  
C125: 5F             CLRB                    
C126: 01                                  
C127: 17 0B 08       LBSR    $0B08           
C12A: 83 05 10       SUBD    #$0510          
C12D: 09 08          ROL     <$08            
C12F: 0F 01          CLR     <$01            
C131: 5F             CLRB                    
C132: 01                                  
C133: 16 0C 07       LBRA    $0C07           
C136: 83 05 0F       SUBD    #$050F          
C139: 08 09          ASL     <$09            
C13B: 0F 02          CLR     <$02            
C13D: 5E                                  
C13E: 01                                  
C13F: 16 0C 08       LBRA    $0C08           
C142: 82 04          SBCA    #$04            
C144: 10                                  
C145: 07 0A          ASR     <$0A            
C147: 0F 01          CLR     <$01            
C149: 5E                                  
C14A: 02                                  
C14B: 16 0C 07       LBRA    $0C07           
C14E: 82 04          SBCA    #$04            
C150: 10                                  
C151: 06 0A          ROR     <$0A            
C153: 0F 02          CLR     <$02            
C155: 5D             TSTB                    
C156: 02                                  
C157: 16 0B 08       LBRA    $0B08           
C15A: 13             SYNC                    
C15B: 04 67          LSR     <$67            
C15D: 05                                  
C15E: 10                                  
C15F: 06 0B          ROR     <$0B            
C161: 0E 02          JMP     <$02            
C163: 5E                                  
C164: 01                                  
C165: 16 0C 07       LBRA    $0C07           
C168: 13             SYNC                    
C169: 04 68          LSR     <$68            
C16B: 04 07          LSR     <$07            
C16D: 01                                  
C16E: 04 06          LSR     <$06            
C170: 0B                                  
C171: 0F 02          CLR     <$02            
C173: 5D             TSTB                    
C174: 02                                  
C175: 16 0C 07       LBRA    $0C07           
C178: 13             SYNC                    
C179: 04 67          LSR     <$67            
C17B: 05                                  
C17C: 10                                  
C17D: 06 0A          ROR     <$0A            
C17F: 0E 03          JMP     <$03            
C181: 5D             TSTB                    
C182: 02                                  
C183: 16 0C 07       LBRA    $0C07           
C186: 13             SYNC                    
C187: 04 67          LSR     <$67            
C189: 04 07          LSR     <$07            
C18B: 01                                  
C18C: 04 06          LSR     <$06            
C18E: 0B                                  
C18F: 0F 02          CLR     <$02            
C191: 5D             TSTB                    
C192: 02                                  
C193: 15                                  
C194: 08 0C          ASL     <$0C            
C196: 12             NOP                     
C197: 05                                  
C198: 66 04          ROR     4,X             
C19A: 07 01          ASR     <$01            
C19C: 04 06          LSR     <$06            
C19E: 0C 0E          INC     <$0E            
C1A0: 02                                  
C1A1: 5D             TSTB                    
C1A2: 02                                  
C1A3: 15                                  
C1A4: 08 0C          ASL     <$0C            
C1A6: 12             NOP                     
C1A7: 05                                  
C1A8: 65                                  
C1A9: 04 07          LSR     <$07            
C1AB: 01                                  
C1AC: 05                                  
C1AD: 05                                  
C1AE: 0C 0E          INC     <$0E            
C1B0: 03 5C          COM     <$5C            
C1B2: 02                                  
C1B3: 11                                  
C1B4: 0C 0B          INC     <$0B            
C1B6: 13             SYNC                    
C1B7: 04 13          LSR     <$13            
C1B9: 04 4B          LSR     <$4B            
C1BB: 04 07          LSR     <$07            
C1BD: 02                                  
C1BE: 04 06          LSR     <$06            
C1C0: 0B                                  
C1C1: 0F 02          CLR     <$02            
C1C3: 5C             INCB                    
C1C4: 02                                  
C1C5: 12             NOP                     
C1C6: 0B                                  
C1C7: 0C 14          INC     <$14            
C1C9: 02                                  
C1CA: 13             SYNC                    
C1CB: 04 4A          LSR     <$4A            
C1CD: 04 07          LSR     <$07            
C1CF: 01                                  
C1D0: 05                                  
C1D1: 05                                  
C1D2: 0C 0E          INC     <$0E            
C1D4: 02                                  
C1D5: 5E                                  
C1D6: 01                                  
C1D7: 11                                  
C1D8: 0B                                  
C1D9: 0C 2E          INC     <$2E            
C1DB: 04 4A          LSR     <$4A            
C1DD: 03 07          COM     <$07            
C1DF: 01                                  
C1E0: 05                                  
C1E1: 05                                  
C1E2: 0C 0E          INC     <$0E            
C1E4: 03 5C          COM     <$5C            
C1E6: 02                                  
C1E7: 10                                  
C1E8: 0C 0B          INC     <$0B            
C1EA: 7F 04 06       CLR     $0406           
C1ED: 02                                  
C1EE: 05                                  
C1EF: 04 0D          LSR     <$0D            
C1F1: 0E 02          JMP     <$02            
C1F3: 5E                                  
C1F4: 01                                  
C1F5: 11                                  
C1F6: 0B                                  
C1F7: 0A 2F          DEC     <$2F            
C1F9: 03 4A          COM     <$4A            
C1FB: 04 06          LSR     <$06            
C1FD: 03 04          COM     <$04            
C1FF: 05                                  
C200: 0C 0E          INC     <$0E            
C202: 03 72          COM     <$72            
C204: 0B                                  
C205: 0A 2F          DEC     <$2F            
C207: 03 4A          COM     <$4A            
C209: 05                                  
C20A: 06 02          ROR     <$02            
C20C: 04 05          LSR     <$05            
C20E: 0C 0F          INC     <$0F            
C210: 02                                  
C211: 75                                  
C212: 08 0A          ASL     <$0A            
C214: 30 01          LEAX    1,X             
C216: 4C             INCA                    
C217: 03 07          COM     <$07            
C219: 02                                  
C21A: 05                                  
C21B: 05                                  
C21C: 0B                                  
C21D: 0F 02          CLR     <$02            
C21F: 74 09 0B       LSR     $090B           
C222: 2E 03          BGT     $C227                          ; 
C224: 4C             INCA                    
C225: 04 07          LSR     <$07            
C227: 02                                  
C228: 04 05          LSR     <$05            
C22A: 0C 0E          INC     <$0E            
C22C: 02                                  
C22D: 75                                  
C22E: 08 0C          ASL     <$0C            
C230: 2E 01          BGT     $C233                          ; 
C232: 4D             TSTA                    
C233: 04 08          LSR     <$08            
C235: 01                                  
C236: 04 06          LSR     <$06            
C238: 0B                                  
C239: 0F 02          CLR     <$02            
C23B: 76 07 0C       ROR     $070C           
C23E: 15                                  
C23F: 01                                  
C240: 67 04          ASR     4,X             
C242: 07 02          ASR     <$02            
C244: 04 06          LSR     <$06            
C246: 0B                                  
C247: 0E 03          JMP     <$03            
C249: 06 01          ROR     <$01            
C24B: 6E 04          JMP     4,X             
C24D: 0E 12          JMP     <$12            
C24F: 04 13          LSR     <$13            
C251: 03 4E          COM     <$4E            
C253: 04 08          LSR     <$08            
C255: 01                                  
C256: 04 06          LSR     <$06            
C258: 0C 0D          INC     <$0D            
C25A: 02                                  
C25B: 07 01          ASR     <$01            
C25D: 53             COMB                    
C25E: 01                                  
C25F: 18                                  
C260: 03 0E          COM     <$0E            
C262: 11                                  
C263: 05                                  
C264: 13             SYNC                    
C265: 03 4F          COM     <$4F            
C267: 05                                  
C268: 07 02          ASR     <$02            
C26A: 04 06          LSR     <$06            
C26C: 0D 0B          TST     <$0B            
C26E: 03 06          COM     <$06            
C270: 02                                  
C271: 53             COMB                    
C272: 01                                  
C273: 17 02 10       LBSR    $0210           
C276: 07 03          ASR     <$03            
C278: 03 05          COM     <$05            
C27A: 11                                  
C27B: 06 52          ROR     <$52            
C27D: 04 08          LSR     <$08            
C27F: 01                                  
C280: 04 05          LSR     <$05            
C282: 0E 0C          JMP     <$0C            
C284: 03 05          COM     <$05            
C286: 02                                  
C287: 84 07          ANDA    #$07            
C289: 0F 0F          CLR     <$0F            
C28B: 06 5A          ROR     <$5A            
C28D: 02                                  
C28E: 08 03          ASL     <$03            
C290: 03 05          COM     <$05            
C292: 0C 0C          INC     <$0C            
C294: 05                                  
C295: 05                                  
C296: 02                                  
C297: 67 01          ASR     1,X             
C299: 17 06 0E       LBSR    $060E           
C29C: 11                                  
C29D: 07 13          ASR     <$13            
C29F: 04 12          LSR     <$12            
C2A1: 01                                  
C2A2: 33 01          LEAU    1,X             
C2A4: 08 01          ASL     <$01            
C2A6: 19             DAA                     
C2A7: 0B                                  
C2A8: 04 08          LSR     <$08            
C2AA: 01                                  
C2AB: 94 01          ANDA    <$01            
C2AD: 05                                  
C2AE: 0D 05          TST     <$05            
C2B0: 17 01 13       LBSR    $0113           
C2B3: 01                                  
C2B4: 6C 06          INC     6,X             
C2B6: 08 01          ASL     <$01            
C2B8: 06 A4          ROR     <$A4            
C2BA: 03 0C          COM     <$0C            
C2BC: 11                                  
C2BD: 08 A6          ASL     <$A6            
C2BF: EC AC 00       LDD     $00,PC          
C2C2: 01                                  
C2C3: A5 F1          BITA    [,S++]          
C2C5: BC E5 B6       CMPX    $E5B6           
C2C8: DA C2          ORB     <$C2            
C2CA: F1 C5 F6       CMPB    $C5F6                          ; 
C2CD: C4 E2          ANDB    #$E2            
C2CF: DD EB          STD     <$EB            
C2D1: D6 00          LDB     <$00            
C2D3: 14                                  
C2D4: F2 E4 F9       SBCB    $E4F9           
C2D7: F8 00 08       EORB    $0008           
C2DA: EF 00          STU     0,X             
C2DC: 1C 00          ANDCC   #$00            
C2DE: 12             NOP                     
C2DF: 00 07          NEG     <$07            
C2E1: 00 00          NEG     <$00            
C2E3: 00 00          NEG     <$00            
C2E5: 00 00          NEG     <$00            
C2E7: 00 00          NEG     <$00            
C2E9: 00 00          NEG     <$00            
C2EB: 00 00          NEG     <$00            
C2ED: 00 A0          NEG     <$A0            
C2EF: 07 05          ASR     <$05            
C2F1: 04 0A          LSR     <$0A            
C2F3: 07 08          ASR     <$08            
C2F5: 04 07          LSR     <$07            
C2F7: 06 17          ROR     <$17            
C2F9: 01                                  
C2FA: 0D 04          TST     <$04            
C2FC: 0A 04          DEC     <$04            
C2FE: 04 0B          LSR     <$0B            
C300: 02                                  
C301: 05                                  
C302: 05                                  
C303: 0B                                  
C304: 03 06          COM     <$06            
C306: 03 03          COM     <$03            
C308: 06 01          ROR     <$01            
C30A: 05                                  
C30B: 16 04 04       LBRA    $0404           
C30E: 03 10          COM     <$10            
C310: 02                                  
C311: 05                                  
C312: 05                                  
C313: 01                                  
C314: 02                                  
C315: 04 04          LSR     <$04            
C317: 04 20          LSR     <$20            
C319: 01                                  
C31A: 06 03          ROR     <$03            
C31C: 0F 03          CLR     <$03            
C31E: 06 02          ROR     <$02            
C320: 01                                  
C321: 01                                  
C322: 01                                  
C323: 01                                  
C324: 01                                  
C325: 07 08          ASR     <$08            
C327: 06 06          ROR     <$06            
C329: 04 07          LSR     <$07            
C32B: 06 08          ROR     <$08            
C32D: 05                                  
C32E: 06 05          ROR     <$05            
C330: 05                                  
C331: 0B                                  
C332: 05                                  
C333: 04 06          LSR     <$06            
C335: 07 0A          ASR     <$0A            
C337: 01                                  
C338: 05                                  
C339: 0B                                  
C33A: 19             DAA                     
C33B: 02                                  
C33C: 09 08          ROL     <$08            
C33E: 03 05          COM     <$05            
C340: 09 05          ROL     <$05            
C342: 0A 01          DEC     <$01            
C344: 0A 04          DEC     <$04            
C346: 03 0C          COM     <$0C            
C348: 06 03          ROR     <$03            
C34A: 06 19          ROR     <$19            
C34C: 09 06          ROL     <$06            
C34E: 02                                  
C34F: 0D 10          TST     <$10            
C351: 13             SYNC                    
C352: 11                                  
C353: 14                                  
C354: 0E 3B          JMP     <$3B            
C356: 01                                  
C357: 0C 4A          INC     <$4A            
C359: 59             ROLB                    
C35A: 5F             CLRB                    
C35B: 73 08 11       COM     $0811           
C35E: 0B                                  
C35F: 23 76          BLS     $C3D7                          ; 
C361: 09 03          ROL     <$03            
C363: 31 56          LEAY    -10,U           
C365: 7E 58 4C       JMP     $584C           
C368: 5C             INCB                    
C369: AB 4A          ADDA    10,U            
C36B: 45                                  
C36C: 4B                                  
C36D: 44             LSRA                    
C36E: 16 5E 44       LBRA    $5E44           
C371: 34 41          PSHS    U,CC            
C373: 2F 38          BLE     $C3AD                          ; 
C375: 7A 43 2A       DEC     $432A           
C378: 41                                  
C379: 25 35          BCS     $C3B0                          ; 
C37B: 8A 36          ORA     #$36            
C37D: 32 36          LEAS    -10,Y           
C37F: 2B 33          BMI     $C3B4                          ; 
C381: 34 18          PSHS    X,DP            
C383: 42                                  
C384: 28 31          BVC     $C3B7                          ; 
C386: 04 05          LSR     <$05            
C388: 33 2E          LEAU    14,Y            
C38A: 29 38          BVS     $C3C4                          ; 
C38C: 13             SYNC                    
C38D: 04 03          LSR     <$03            
C38F: 3B             RTI                     
C390: 26 34          BNE     $C3C6                          ; 
C392: 2C 34          BGE     $C3C8                          ; 
C394: 2D 30          BLT     $C3C6                          ; 
C396: 1D             SEX                     
C397: 43             COMA                    
C398: 26 35          BNE     $C3CF                          ; 
C39A: 2B 32          BMI     $C3CE                          ; 
C39C: 2B 24          BMI     $C3C2                          ; 
C39E: 1D             SEX                     
C39F: 4C             INCA                    
C3A0: 24 35          BCC     $C3D7                          ; 
C3A2: 2C 2E          BGE     $C3D2                          ; 
C3A4: 2B 25          BMI     $C3CB                          ; 
C3A6: 1D             SEX                     
C3A7: 49             ROLA                    
C3A8: 25 33          BCS     $C3DD                          ; 
C3AA: 2E 21          BGT     $C3CD                          ; 
C3AC: 36 22          PSHU    Y,A             
C3AE: 19             DAA                     
C3AF: 4E                                  
C3B0: 23 30          BLS     $C3E2                          ; 
C3B2: 27 28          BEQ     $C3DC                          ; 
C3B4: 37 21          PULU    CC,Y            
C3B6: 18                                  
C3B7: 4C             INCA                    
C3B8: 22 20          BHI     $C3DA                          ; 
C3BA: 04 08          LSR     <$08            
C3BC: 2A 25          BPL     $C3E3                          ; 
C3BE: 38                                  
C3BF: 1A 1C          ORCC    #$1C            
C3C1: 4C             INCA                    
C3C2: 21 1C          BRN     $C3E0                          ; 
C3C4: 0A 03          DEC     <$03            
C3C6: 2A 26          BPL     $C3EE                          ; 
C3C8: 31 1D          LEAY    -3,X            
C3CA: 20 46          BRA     $C412                          ; 
C3CC: 21 1B          BRN     $C3E9                          ; 
C3CE: 0A 04          DEC     <$04            
C3D0: 2B 24          BMI     $C3F6                          ; 
C3D2: 2E 20          BGT     $C3F4                          ; 
C3D4: 1E 45          EXG     $45             
C3D6: 20 1A          BRA     $C3F2                          ; 
C3D8: 0C 03          INC     <$03            
C3DA: 2C 23          BGE     $C3FF                          ; 
C3DC: 2C 20          BGE     $C3FE                          ; 
C3DE: 19             DAA                     
C3DF: 47             ASRA                    
C3E0: 20 1A          BRA     $C3FC                          ; 
C3E2: 0D 01          TST     <$01            
C3E4: 2D 22          BLT     $C408                          ; 
C3E6: 1F 2D          TFR     Y,?             
C3E8: 19             DAA                     
C3E9: 45                                  
C3EA: 21 19          BRN     $C405                          ; 
C3EC: 0D 01          TST     <$01            
C3EE: 2D 20          BLT     $C410                          ; 
C3F0: 1F 1E          TFR     X,?             
C3F2: 25 47          BCS     $C43B                          ; 
C3F4: 20 18          BRA     $C40E                          ; 
C3F6: 0E 02          JMP     <$02            
C3F8: 2D 1E          BLT     $C418                          ; 
C3FA: 1D             SEX                     
C3FB: 24 25          BCC     $C422                          ; 
C3FD: 42                                  
C3FE: 21 17          BRN     $C417                          ; 
C400: 0E 01          JMP     <$01            
C402: 2E 1D          BGT     $C421                          ; 
C404: 1D             SEX                     
C405: 23 23          BLS     $C42A                          ; 
C407: 43             COMA                    
C408: 21 17          BRN     $C421                          ; 
C40A: 0D 02          TST     <$02            
C40C: 2D 1C          BLT     $C42A                          ; 
C40E: 1E 22          EXG     $22             
C410: 25 40          BCS     $C452                          ; 
C412: 20 17          BRA     $C42B                          ; 
C414: 0E 02          JMP     <$02            
C416: 2D 1B          BLT     $C433                          ; 
C418: 1F 22          TFR     Y,Y             
C41A: 24 3F          BCC     $C45B                          ; 
C41C: 20 16          BRA     $C434                          ; 
C41E: 10                                  
C41F: 01                                  
C420: 19             DAA                     
C421: 01                                  
C422: 0F 1A          CLR     <$1A            
C424: 20 20          BRA     $C446                          ; 
C426: 24 3E          BCC     $C466                          ; 
C428: 20 16          BRA     $C440                          ; 
C42A: 2C 03          BGE     $C42F                          ; 
C42C: 0E 1B          JMP     <$1B            
C42E: 1F 1F          TFR     X,?             
C430: 23 40          BLS     $C472                          ; 
C432: 20 16          BRA     $C44A                          ; 
C434: 2B 04          BMI     $C43A                          ; 
C436: 0E 19          JMP     <$19            
C438: 1F 20          TFR     Y,D             
C43A: 22 40          BHI     $C47C                          ; 
C43C: 1F 16          TFR     X,?             
C43E: 2C 02          BGE     $C442                          ; 
C440: 0F 1C          CLR     <$1C            
C442: 20 1C          BRA     $C460                          ; 
C444: 22 40          BHI     $C486                          ; 
C446: 1F 15          TFR     X,PC            
C448: 40             NEGA                    
C449: 1C 20          ANDCC   #$20            
C44B: 1C 02          ANDCC   #$02            
C44D: 02                                  
C44E: 1A 40          ORCC    #$40            
C450: 1F 15          TFR     X,PC            
C452: 3F             SWI                     
C453: 1C 21          ANDCC   #$21            
C455: 23 1B          BLS     $C472                          ; 
C457: 3E             RESET                   
C458: 20 16          BRA     $C470                          ; 
C45A: 06 08          ROR     <$08            
C45C: 2C 1E          BGE     $C47C                          ; 
C45E: 20 25          BRA     $C485                          ; 
C460: 1B                                  
C461: 3A             ABX                     
C462: 20 28          BRA     $C48C                          ; 
C464: 2B 1E          BMI     $C484                          ; 
C466: 28 24          BVC     $C48C                          ; 
C468: 18                                  
C469: 37 21          PULU    CC,Y            
C46B: 29 2B          BVS     $C498                          ; 
C46D: 1F 1F          TFR     X,?             
C46F: 01                                  
C470: 05                                  
C471: 23 18          BLS     $C48B                          ; 
C473: 35 22          PULS    A,Y             
C475: 2E 03          BGT     $C47A                          ; 
C477: 03 1F          COM     <$1F            
C479: 04 02          LSR     <$02            
C47B: 13             SYNC                    
C47C: 0D 02          TST     <$02            
C47E: 22 1B          BHI     $C49B                          ; 
C480: 13             SYNC                    
C481: 3A             ABX                     
C482: 21 37          BRN     $C4BB                          ; 
C484: 29 08          BVS     $C48E                          ; 
C486: 03 18          COM     <$18            
C488: 20 1E          BRA     $C4A8                          ; 
C48A: 04 47          LSR     <$47            
C48C: 22 37          BHI     $C4C5                          ; 
C48E: 2B 06          BMI     $C496                          ; 
C490: 06 18          ROR     <$18            
C492: 1C 11          ANDCC   #$11            
C494: 01                                  
C495: 5A             DECB                    
C496: 34 28          PSHS    Y,DP            
C498: 34 27          PSHS    Y,B,A,CC        
C49A: 20 01          BRA     $C49D                          ; 
C49C: 04 56          LSR     <$56            
C49E: 34 01          PSHS    CC              
C4A0: 03 23          COM     <$23            
C4A2: 35 30          PULS    X,Y             
C4A4: 21 5B          BRN     $C501                          ; 
C4A6: 32 33          LEAS    -13,Y           
C4A8: 39             RTS                     
C4A9: 2D 2B          BLT     $C4D6                          ; 
C4AB: 04 05          LSR     <$05            
C4AD: 4F             CLRA                    
C4AE: 42                                  
C4AF: 1B                                  
C4B0: 01                                  
C4B1: 04 03          LSR     <$03            
C4B3: 04 43          LSR     <$43            
C4B5: 41                                  
C4B6: 0B                                  
C4B7: 5C             INCB                    
C4B8: 03 05          COM     <$05            
C4BA: 06 04          ROR     <$04            
C4BC: 85 33          BITA    #$33            
C4BE: 14                                  
C4BF: 05                                  
C4C0: 0A 07          DEC     <$07            
C4C2: 09 0D          ROL     <$0D            
C4C4: 0E 15          JMP     <$15            
C4C6: 01                                  
C4C7: 12             NOP                     
C4C8: 2F 2A          BLE     $C4F4                          ; 
C4CA: 71                                  
C4CB: 13             SYNC                    
C4CC: 37 1C          PULU    B,DP,X          
C4CE: 2F 3A          BLE     $C50A                          ; 
C4D0: 53             COMB                    
C4D1: 3B             RTI                     
C4D2: 3C 0F          CWAI    $0F             
C4D4: 30 0F          LEAX    15,X            
C4D6: 81 69          CMPA    #$69            
C4D8: 2B 2B          BMI     $C505                          ; 
C4DA: 34 2C          PSHS    Y,DP,B          
C4DC: 6A 25          DEC     5,Y             
C4DE: 28 28          BVC     $C508                          ; 
C4E0: 2A 24          BPL     $C506                          ; 
C4E2: 29 39          BVS     $C51D                          ; 
C4E4: 4E                                  
C4E5: 26 36          BNE     $C51D                          ; 
C4E7: 35 42          PULS    A,U             
C4E9: 37 31          PULU    CC,X,Y          
C4EB: 2B 3A          BMI     $C527                          ; 
C4ED: AF 93          STX     [,--X]          
C4EF: 2F 47          BLE     $C538                          ; 
C4F1: 30 98 A5       LEAX    [$A5,X]         
C4F4: 93 22          SUBD    <$22            
C4F6: 34 22          PSHS    Y,A             
C4F8: BB 29 19       ADDA    $2919           
C4FB: 2B 11          BMI     $C50E                          ; 
C4FD: 05                                  
C4FE: 92 04          SBCA    <$04            
C500: 11                                  
C501: 12             NOP                     
C502: 0F 07          CLR     <$07            
C504: 4D             TSTA                    
C505: 18                                  
C506: 03 05          COM     <$05            
C508: 17 05 01       LBSR    $0501           
C50B: 04 08          LSR     <$08            
C50D: 03 08          COM     <$08            
C50F: 10                                  
C510: 0F 03          CLR     <$03            
C512: 10                                  
C513: 02                                  
C514: 06 02          ROR     <$02            
C516: 16 05 01       LBRA    $0501           
C519: 06 17          ROR     <$17            
C51B: 06 2A          ROR     <$2A            
C51D: 06 0A          ROR     <$0A            
C51F: 04 1F          LSR     <$1F            
C521: 04 13          LSR     <$13            
C523: 0A 10          DEC     <$10            
C525: 02                                  
C526: 28 04          BVC     $C52C                          ; 
C528: 0D 0B          TST     <$0B            
C52A: 0B                                  
C52B: 06 01          ROR     <$01            
C52D: 04 07          LSR     <$07            
C52F: 1E 0F          EXG     $0F             
C531: 06 11          ROR     <$11            
C533: 03 0A          COM     <$0A            
C535: 05                                  
C536: 05                                  
C537: 04 05          LSR     <$05            
C539: 02                                  
C53A: 05                                  
C53B: 04 06          LSR     <$06            
C53D: 04 09          LSR     <$09            
C53F: 06 0E          ROR     <$0E            
C541: 08 06          ASL     <$06            
C543: 05                                  
C544: 0A 03          DEC     <$03            
C546: 04 03          LSR     <$03            
C548: 05                                  
C549: 04 0A          LSR     <$0A            
C54B: 04 07          LSR     <$07            
C54D: 0A 05          DEC     <$05            
C54F: 02                                  
C550: 05                                  
C551: 02                                  
C552: 04 07          LSR     <$07            
C554: 06 05          ROR     <$05            
C556: 05                                  
C557: 02                                  
C558: 0A 03          DEC     <$03            
C55A: 06 04          ROR     <$04            
C55C: 09 0A          ROL     <$0A            
C55E: 06 07          ROR     <$07            
C560: 07 0A          ASR     <$0A            
C562: 07 04          ASR     <$04            
C564: 18                                  
C565: 01                                  
C566: 05                                  
C567: 05                                  
C568: 07 04          ASR     <$04            
C56A: 05                                  
C56B: 02                                  
C56C: 07 0D          ASR     <$0D            
C56E: 06 02          ROR     <$02            
C570: 03 04          COM     <$04            
C572: 0C 04          INC     <$04            
C574: 0F 04          CLR     <$04            
C576: 06 04          ROR     <$04            
C578: 07 04          ASR     <$04            
C57A: 05                                  
C57B: 03 06          COM     <$06            
C57D: 06 04          ROR     <$04            
C57F: 05                                  
C580: 07 05          ASR     <$05            
C582: 06 04          ROR     <$04            
C584: 05                                  
C585: 03 07          COM     <$07            
C587: 05                                  
C588: 0E 05          JMP     <$05            
C58A: 06 03          ROR     <$03            
C58C: 05                                  
C58D: 03 07          COM     <$07            
C58F: 06 06          ROR     <$06            
C591: 03 05          COM     <$05            
C593: 08 09          ASL     <$09            
C595: 06 01          ROR     <$01            
C597: 05                                  
C598: 0C 05          INC     <$05            
C59A: 03 02          COM     <$02            
C59C: 07 03          ASR     <$03            
C59E: 05                                  
C59F: 04 08          LSR     <$08            
C5A1: 03 06          COM     <$06            
C5A3: 06 06          ROR     <$06            
C5A5: 03 05          COM     <$05            
C5A7: 05                                  
C5A8: 06 04          ROR     <$04            
C5AA: 04 05          LSR     <$05            
C5AC: 0C 05          INC     <$05            
C5AE: 04 03          LSR     <$03            
C5B0: 05                                  
C5B1: 03 05          COM     <$05            
C5B3: 04 0B          LSR     <$0B            
C5B5: 03 04          COM     <$04            
C5B7: 02                                  
C5B8: 09 05          ROL     <$05            
C5BA: 0E 04          JMP     <$04            
C5BC: 08 05          ASL     <$05            
C5BE: 06 03          ROR     <$03            
C5C0: 08 04          ASL     <$04            
C5C2: 04 05          LSR     <$05            
C5C4: 06 03          ROR     <$03            
C5C6: 05                                  
C5C7: 04 06          LSR     <$06            
C5C9: 01                                  
C5CA: 04 01          LSR     <$01            
C5CC: 04 04          LSR     <$04            
C5CE: 05                                  
C5CF: 02                                  
C5D0: 0B                                  
C5D1: 04 09          LSR     <$09            
C5D3: 06 0D          ROR     <$0D            
C5D5: 02                                  
C5D6: 0B                                  
C5D7: 05                                  
C5D8: 05                                  
C5D9: 03 05          COM     <$05            
C5DB: 0A 06          DEC     <$06            
C5DD: 05                                  
C5DE: 04 07          LSR     <$07            
C5E0: 06 04          ROR     <$04            
C5E2: 05                                  
C5E3: 03 06          COM     <$06            
C5E5: 07 08          ASR     <$08            
C5E7: 0D 07          TST     <$07            
C5E9: 06 06          ROR     <$06            
C5EB: 03 05          COM     <$05            
C5ED: 05                                  
C5EE: 06 03          ROR     <$03            
C5F0: 04 05          LSR     <$05            
C5F2: 0C 05          INC     <$05            
C5F4: 06 05          ROR     <$05            
C5F6: 07 06          ASR     <$06            
C5F8: 06 03          ROR     <$03            
C5FA: 04 04          LSR     <$04            
C5FC: 07 02          ASR     <$02            
C5FE: 05                                  
C5FF: 04 0E          LSR     <$0E            
C601: 04 04          LSR     <$04            
C603: 03 07          COM     <$07            
C605: 06 04          ROR     <$04            
C607: 04 05          LSR     <$05            
C609: 06 08          ROR     <$08            
C60B: 04 05          LSR     <$05            
C60D: 08 06          ASL     <$06            
C60F: 04 05          LSR     <$05            
C611: 05                                  
C612: 05                                  
C613: 05                                  
C614: 04 04          LSR     <$04            
C616: 06 02          ROR     <$02            
C618: 05                                  
C619: 06 09          ROR     <$09            
C61B: 05                                  
C61C: 07 06          ASR     <$06            
C61E: 05                                  
C61F: 04 07          LSR     <$07            
C621: 05                                  
C622: 05                                  
C623: 04 05          LSR     <$05            
C625: 03 02          COM     <$02            
C627: 0C 05          INC     <$05            
C629: 04 06          LSR     <$06            
C62B: 05                                  
C62C: 0C 08          INC     <$08            
C62E: 06 05          ROR     <$05            
C630: 0F 06          CLR     <$06            
C632: 05                                  
C633: 02                                  
C634: 05                                  
C635: 09 04          ROL     <$04            
C637: 03 06          COM     <$06            
C639: 04 0D          LSR     <$0D            
C63B: 01                                  
C63C: 05                                  
C63D: 03 04          COM     <$04            
C63F: 03 04          COM     <$04            
C641: 04 0B          LSR     <$0B            
C643: 0B                                  
C644: 02                                  
C645: 02                                  
C646: 04 05          LSR     <$05            
C648: 03 04          COM     <$04            
C64A: 05                                  
C64B: 04 01          LSR     <$01            
C64D: 03 08          COM     <$08            
C64F: 06 04          ROR     <$04            
C651: 01                                  
C652: 08 06          ASL     <$06            
C654: 04 01          LSR     <$01            
C656: 06 06          ROR     <$06            
C658: 05                                  
C659: 05                                  
C65A: 07 01          ASR     <$01            
C65C: 01                                  
C65D: 03 05          COM     <$05            
C65F: 05                                  
C660: 06 03          ROR     <$03            
C662: 08 05          ASL     <$05            
C664: 05                                  
C665: 03 08          COM     <$08            
C667: 08 0B          ASL     <$0B            
C669: 05                                  
C66A: 07 05          ASR     <$05            
C66C: 06 05          ROR     <$05            
C66E: 06 03          ROR     <$03            
C670: 05                                  
C671: 05                                  
C672: 11                                  
C673: 08 05          ASL     <$05            
C675: 06 11          ROR     <$11            
C677: 05                                  
C678: 05                                  
C679: 04 06          LSR     <$06            
C67B: 06 09          ROR     <$09            
C67D: 05                                  
C67E: 05                                  
C67F: 01                                  
C680: 07 05          ASR     <$05            
C682: 05                                  
C683: 06 0B          ROR     <$0B            
C685: 02                                  
C686: 07 0E          ASR     <$0E            
C688: 05                                  
C689: 05                                  
C68A: 09 03          ROL     <$03            
C68C: 04 03          LSR     <$03            
C68E: 04 03          LSR     <$03            
C690: 04 01          LSR     <$01            
C692: 04 03          LSR     <$03            
C694: 04 03          LSR     <$03            
C696: 05                                  
C697: 08 06          ASL     <$06            
C699: 0C 07          INC     <$07            
C69B: 05                                  
C69C: 05                                  
C69D: 04 05          LSR     <$05            
C69F: 02                                  
C6A0: 04 08          LSR     <$08            
C6A2: 09 03          ROL     <$03            
C6A4: 07 06          ASR     <$06            
C6A6: 06 04          ROR     <$04            
C6A8: 04 05          LSR     <$05            
C6AA: 07 05          ASR     <$05            
C6AC: 02                                  
C6AD: 04 07          LSR     <$07            
C6AF: 03 0A          COM     <$0A            
C6B1: 04 05          LSR     <$05            
C6B3: 02                                  
C6B4: 05                                  
C6B5: 03 04          COM     <$04            
C6B7: 05                                  
C6B8: 02                                  
C6B9: 01                                  
C6BA: 06 04          ROR     <$04            
C6BC: 04 05          LSR     <$05            
C6BE: 05                                  
C6BF: 03 07          COM     <$07            
C6C1: 07 05          ASR     <$05            
C6C3: 03 0A          COM     <$0A            
C6C5: 04 04          LSR     <$04            
C6C7: 04 05          LSR     <$05            
C6C9: 01                                  
C6CA: 04 01          LSR     <$01            
C6CC: 04 04          LSR     <$04            
C6CE: 0C 02          INC     <$02            
C6D0: 05                                  
C6D1: 04 07          LSR     <$07            
C6D3: 05                                  
C6D4: 06 04          ROR     <$04            
C6D6: 03 05          COM     <$05            
C6D8: 05                                  
C6D9: 04 06          LSR     <$06            
C6DB: 05                                  
C6DC: 0B                                  
C6DD: 04 04          LSR     <$04            
C6DF: 04 07          LSR     <$07            
C6E1: 06 05          ROR     <$05            
C6E3: 04 06          LSR     <$06            
C6E5: 05                                  
C6E6: 06 04          ROR     <$04            
C6E8: 07 05          ASR     <$05            
C6EA: 06 06          ROR     <$06            
C6EC: 05                                  
C6ED: 03 05          COM     <$05            
C6EF: 06 06          ROR     <$06            
C6F1: 03 06          COM     <$06            
C6F3: 06 04          ROR     <$04            
C6F5: 05                                  
C6F6: 07 05          ASR     <$05            
C6F8: 06 06          ROR     <$06            
C6FA: 03 03          COM     <$03            
C6FC: 06 04          ROR     <$04            
C6FE: 04 04          LSR     <$04            
C700: 05                                  
C701: 03 04          COM     <$04            
C703: 03 05          COM     <$05            
C705: 02                                  
C706: 05                                  
C707: 0C 0A          INC     <$0A            
C709: 02                                  
C70A: 02                                  
C70B: 03 05          COM     <$05            
C70D: 08 0D          ASL     <$0D            
C70F: 0A 0D          DEC     <$0D            
C711: 05                                  
C712: 04 02          LSR     <$02            
C714: 06 02          ROR     <$02            
C716: 03 04          COM     <$04            
C718: 0B                                  
C719: 05                                  
C71A: 0C 03          INC     <$03            
C71C: 04 03          LSR     <$03            
C71E: 05                                  
C71F: 03 04          COM     <$04            
C721: 04 0C          LSR     <$0C            
C723: 09 06          ROL     <$06            
C725: 04 05          LSR     <$05            
C727: 04 05          LSR     <$05            
C729: 03 04          COM     <$04            
C72B: 03 05          COM     <$05            
C72D: 03 07          COM     <$07            
C72F: 04 06          LSR     <$06            
C731: 07 03          ASR     <$03            
C733: 03 05          COM     <$05            
C735: 02                                  
C736: 04 02          LSR     <$02            
C738: 03 03          COM     <$03            
C73A: 04 04          LSR     <$04            
C73C: 05                                  
C73D: 0A 0D          DEC     <$0D            
C73F: 03 05          COM     <$05            
C741: 03 0B          COM     <$0B            
C743: 05                                  
C744: 0B                                  
C745: 04 05          LSR     <$05            
C747: 04 02          LSR     <$02            
C749: 03 05          COM     <$05            
C74B: 04 09          LSR     <$09            
C74D: 05                                  
C74E: 06 01          ROR     <$01            
C750: 05                                  
C751: 02                                  
C752: 05                                  
C753: 03 04          COM     <$04            
C755: 02                                  
C756: 05                                  
C757: 04 0A          LSR     <$0A            
C759: 02                                  
C75A: 0A 05          DEC     <$05            
C75C: 0D 01          TST     <$01            
C75E: 0D 06          TST     <$06            
C760: 0C 0A          INC     <$0A            
C762: 07 03          ASR     <$03            
C764: 04 03          LSR     <$03            
C766: 05                                  
C767: 04 05          LSR     <$05            
C769: 05                                  
C76A: 05                                  
C76B: 04 05          LSR     <$05            
C76D: 0E 03          JMP     <$03            
C76F: 03 0C          COM     <$0C            
C771: 07 02          ASR     <$02            
C773: 0B                                  
C774: 04 05          LSR     <$05            
C776: 03 15          COM     <$15            
C778: 03 06          COM     <$06            
C77A: 03 19          COM     <$19            
C77C: 04 05          LSR     <$05            
C77E: 82 04          SBCA    #$04            
C780: 04 04          LSR     <$04            
C782: 05                                  
C783: 8D 01          BSR     $C786                          ; 
C785: 1F 09          TFR     D,B             
C787: 03 06          COM     <$06            
C789: 03 4D          COM     <$4D            
C78B: 05                                  
C78C: 0C 1C          INC     <$1C            
C78E: 22 03          BHI     $C793                          ; 
C790: 1E 08          EXG     $08             
C792: 12             NOP                     
C793: 66 63          ROR     3,S             
C795: 3D             MUL                     
C796: 47             ASRA                    
C797: 07 0F          ASR     <$0F            
C799: 5E                                  
C79A: 5A             DECB                    
C79B: 48             LSLA                    
C79C: 45                                  
C79D: 79 44 06       ROL     $4406           
C7A0: 0E 31          JMP     <$31            
C7A2: 58             LSLB                    
C7A3: 7C 44 0F       INC     $440F           
C7A6: 06 2D          ROR     <$2D            
C7A8: 42                                  
C7A9: 04 12          LSR     <$12            
C7AB: 7F 44 10       CLR     $4410           
C7AE: 04 2E          LSR     <$2E            
C7B0: 44             LSRA                    
C7B1: 02                                  
C7B2: 11 83 45 10    CMPU    #$4510          
C7B6: 03 2F          COM     <$2F            
C7B8: 4B                                  
C7B9: 07 03          ASR     <$03            
C7BB: 86 46          LDA     #$46            
C7BD: 46             RORA                    
C7BE: 49             ROLA                    
C7BF: 94 47          ANDA    <$47            
C7C1: 47             ASRA                    
C7C2: 47             ASRA                    
C7C3: 98 48          EORA    <$48            
C7C5: 45                                  
C7C6: 46             RORA                    
C7C7: 32 0A          LEAS    10,X            
C7C9: 0F 01          CLR     <$01            
C7CB: 48             LSLA                    
C7CC: 48             LSLA                    
C7CD: 44             LSRA                    
C7CE: 3E             RESET                   
C7CF: 30 2A          LEAX    10,Y            
C7D1: 4B                                  
C7D2: 48             LSLA                    
C7D3: 38                                  
C7D4: 43             COMA                    
C7D5: 33 2E          LEAU    14,Y            
C7D7: 50             NEGB                    
C7D8: 46             RORA                    
C7D9: 34 3C          PSHS    Y,X,DP,B        
C7DB: 3D             MUL                     
C7DC: 2B 5B          BMI     $C839                          ; 
C7DE: 45                                  
C7DF: 32 3C          LEAS    -4,Y            
C7E1: 33 34          LEAU    -12,Y           
C7E3: 67 41          ASR     1,U             
C7E5: 2F 42          BLE     $C829                          ; 
C7E7: 2C 38          BGE     $C821                          ; 
C7E9: 73 3D 31       COM     $3D31           
C7EC: 3F             SWI                     
C7ED: 2D 36          BLT     $C825                          ; 
C7EF: 7A 3D 32       DEC     $3D32           
C7F2: 3C 2D          CWAI    $2D             
C7F4: 36 31          PSHU    Y,X,CC          
C7F6: 0A 43          DEC     <$43            
C7F8: 39             RTS                     
C7F9: 31 40          LEAY    0,U             
C7FB: 2D 36          BLT     $C833                          ; 
C7FD: 32 11          LEAS    -15,X           
C7FF: 42                                  
C800: 35 34          PULS    B,X,Y           
C802: 3C 2F          CWAI    $2F             
C804: 34 31          PSHS    Y,X,CC          
C806: 19             DAA                     
C807: 44             LSRA                    
C808: 33 37          LEAU    -9,Y            
C80A: 33 37          LEAU    -9,Y            
C80C: 32 33          LEAS    -13,Y           
C80E: 19             DAA                     
C80F: 48             LSLA                    
C810: 2F 3A          BLE     $C84C                          ; 
C812: 31 39          LEAY    -7,Y            
C814: 2D 37          BLT     $C84D                          ; 
C816: 20 49          BRA     $C861                          ; 
C818: 25 05          BCS     $C81F                          ; 
C81A: 02                                  
C81B: 39             RTS                     
C81C: 2F 3B          BLE     $C859                          ; 
C81E: 2C 39          BGE     $C859                          ; 
C820: 21 4C          BRN     $C86E                          ; 
C822: 26 44          BNE     $C868                          ; 
C824: 2E 3A          BGT     $C860                          ; 
C826: 2D 38          BLT     $C860                          ; 
C828: 25 4F          BCS     $C879                          ; 
C82A: 29 42          BVS     $C86E                          ; 
C82C: 2F 39          BLE     $C867                          ; 
C82E: 2E 34          BGT     $C864                          ; 
C830: 2B 53          BMI     $C885                          ; 
C832: 29 40          BVS     $C874                          ; 
C834: 2F 38          BLE     $C86E                          ; 
C836: 2F 32          BLE     $C86A                          ; 
C838: 2E 5A          BGT     $C894                          ; 
C83A: 2B 3D          BMI     $C879                          ; 
C83C: 30 38          LEAX    -8,Y            
C83E: 30 2F          LEAX    15,Y            
C840: 32 5E          LEAS    -2,U            
C842: 2C 3C          BGE     $C880                          ; 
C844: 30 36          LEAX    -10,Y           
C846: 32 2B          LEAS    11,Y            
C848: 35 66          PULS    A,B,Y,U         
C84A: 2C 3B          BGE     $C887                          ; 
C84C: 2F 31          BLE     $C87F                          ; 
C84E: 38                                  
C84F: 28 38          BVC     $C889                          ; 
C851: 6F 2B          CLR     11,Y            
C853: 3A             ABX                     
C854: 30 2A          LEAX    10,Y            
C856: 3E             RESET                   
C857: 28 38          BVC     $C891                          ; 
C859: 7A 2A 2D       DEC     $2A2D           
C85C: 04 06          LSR     <$06            
C85E: 30 27          LEAX    7,Y             
C860: 40             NEGA                    
C861: 25 2F          BCS     $C892                          ; 
C863: 91 28          CMPA    <$28            
C865: 2B 3F          BMI     $C8A6                          ; 
C867: 28 3F          BVC     $C8A8                          ; 
C869: 26 2F          BNE     $C89A                          ; 
C86B: 99 29          ADCA    <$29            
C86D: 2C 08          BGE     $C877                          ; 
C86F: 06 2C          ROR     <$2C            
C871: 27 41          BEQ     $C8B4                          ; 
C873: 23 2D          BLS     $C8A2                          ; 
C875: 34 11          PSHS    X,CC            
C877: 5D             TSTB                    
C878: 2A 3E          BPL     $C8B8                          ; 
C87A: 2B 29          BMI     $C8A5                          ; 
C87C: 41                                  
C87D: 24 2D          BCC     $C8AC                          ; 
C87F: A8 2B          EORA    11,Y            
C881: 30 39          LEAX    -7,Y            
C883: 28 3E          BVC     $C8C3                          ; 
C885: 27 2D          BEQ     $C8B4                          ; 
C887: 28 1F          BVC     $C8A8                          ; 
C889: 6D 2D          TST     13,Y            
C88B: 3A             ABX                     
C88C: 2E 29          BGT     $C8B7                          ; 
C88E: 3B             RTI                     
C88F: 29 2D          BVS     $C8BE                          ; 
C891: 31 1B          LEAY    -5,X            
C893: 6E 2E          JMP     14,Y            
C895: 32 35          LEAS    -11,Y           
C897: 2A 3B          BPL     $C8D4                          ; 
C899: 28 30          BVC     $C8CB                          ; 
C89B: 29 23          BVS     $C8C0                          ; 
C89D: 76 2E 31       ROR     $2E31           
C8A0: 36 2A          PSHU    Y,DP,A          
C8A2: 38                                  
C8A3: 2C 2F          BGE     $C8D4                          ; 
C8A5: 2B 1D          BMI     $C8C4                          ; 
C8A7: 7F 2F 2E       CLR     $2F2E           
C8AA: 39             RTS                     
C8AB: 29 37          BVS     $C8E4                          ; 
C8AD: 2D 2E          BLT     $C8DD                          ; 
C8AF: 2C 2A          BGE     $C8DB                          ; 
C8B1: 7B                                  
C8B2: 2D 2C          BLT     $C8E0                          ; 
C8B4: 3B             RTI                     
C8B5: 29 34          BVS     $C8EB                          ; 
C8B7: 32 2E          LEAS    14,Y            
C8B9: 29 2F          BVS     $C8EA                          ; 
C8BB: 85 2B          BITA    #$2B            
C8BD: 29 3F          BVS     $C8FE                          ; 
C8BF: 28 32          BVC     $C8F3                          ; 
C8C1: 35 2F          PULS    CC,A,B,DP,Y     
C8C3: 2B 2D          BMI     $C8F2                          ; 
C8C5: 90 2B          SUBA    <$2B            
C8C7: 2A 3F          BPL     $C908                          ; 
C8C9: 28 33          BVC     $C8FE                          ; 
C8CB: 33 31          LEAU    -15,Y           
C8CD: 2D 38          BLT     $C907                          ; 
C8CF: 94 2A          ANDA    <$2A            
C8D1: 2A 3F          BPL     $C912                          ; 
C8D3: 27 35          BEQ     $C90A                          ; 
C8D5: 32 30          LEAS    -16,Y           
C8D7: 2C 33          BGE     $C90C                          ; 
C8D9: AE 2F          LDX     15,Y            
C8DB: 2D 39          BLT     $C916                          ; 
C8DD: 29 34          BVS     $C913                          ; 
C8DF: 32 32          LEAS    -14,Y           
C8E1: 2F 30          BLE     $C913                          ; 
C8E3: C2 2F          SBCB    #$2F            
C8E5: 2C 3C          BGE     $C923                          ; 
C8E7: 29 35          BVS     $C91E                          ; 
C8E9: 32 30          LEAS    -16,Y           
C8EB: 2F 34          BLE     $C921                          ; 
C8ED: D1 2F          CMPB    <$2F            
C8EF: 29 41          BVS     $C932                          ; 
C8F1: 28 34          BVC     $C927                          ; 
C8F3: 35 31          PULS    CC,X,Y          
C8F5: 2F 35          BLE     $C92C                          ; 
C8F7: D6 31          LDB     <$31            
C8F9: 29 40          BVS     $C93B                          ; 
C8FB: 27 2C          BEQ     $C929                          ; 
C8FD: 3A             ABX                     
C8FE: 31 26          LEAY    6,Y             
C900: 30 24          LEAX    4,Y             
C902: 1D             SEX                     
C903: B8 30 26       EORA    $3026           
C906: 45                                  
C907: 23 2A          BLS     $C933                          ; 
C909: 38                                  
C90A: 31 23          LEAY    3,Y             
C90C: 66                                  
C90D: DE 2D          LDU     <$2D            
C90F: 25 45          BCS     $C956                          ; 
C911: 20 2D          BRA     $C940                          ; 
C913: 30 38          LEAX    -8,Y            
C915: 00 17          NEG     <$17            
C917: 01                                  
C918: 1E 01          EXG     $01             
C91A: 03 17          COM     <$17            
C91C: 1F 33          TFR     U,U             
C91E: 1A 5C          ORCC    #$5C            
C920: 10                                  
C921: 69 27          ROL     7,Y             
C923: 25 D4          BCS     $C8F9                          ; 
C925: 10                                  
C926: 42                                  
C927: 1D             SEX                     
C928: 24 53          BCC     $C97D                          ; 
C92A: 05                                  
C92B: D6 E2          LDB     <$E2            
C92D: 09 2C          ROL     <$2C            
C92F: 18                                  
C930: 0D 01          TST     <$01            
C932: 0C 00          INC     <$00            
C934: 5B                                  
C935: D8 05          EORB    <$05            
C937: 09 0B          ROL     <$0B            
C939: 22 46          BHI     $C981                          ; 
C93B: 05                                  
C93C: 14                                  
C93D: 02                                  
C93E: 3A             ABX                     
C93F: 1D             SEX                     
C940: C0 00          SUBB    #$00            
C942: 18                                  
C943: 09 43          ROL     <$43            
C945: 27 0D          BEQ     $C954                          ; 
C947: 10                                  
C948: 08 50          ASL     <$50            
C94A: 07 EE          ASR     <$EE            
C94C: 00 35          NEG     <$35            
C94E: 0B                                  
C94F: 1D             SEX                     
C950: 69 03          ROL     3,X             
C952: 00 53          NEG     <$53            
C954: 00 51          NEG     <$51            
C956: 00 00          NEG     <$00            
C958: 18                                  
C959: 00 3F          NEG     <$3F            
C95B: 00 00          NEG     <$00            
C95D: 87                                  
C95E: 00 3C          NEG     <$3C            
C960: F8 A8 0C       EORB    $A80C           
C963: 0C A8          INC     <$A8            
C965: F8 CC 84       EORB    $CC84                          ; 
C968: CC 84 FC       LDD     #$84FC          
C96B: 30 7C          LEAX    -4,S            
C96D: 54             LSRB                    
C96E: C0 C0          SUBB    #$C0            
C970: 54             LSRB                    
C971: 7C 30 FC       INC     $30FC           
C974: 84 CC          ANDA    #$CC            
C976: 84 CC          ANDA    #$CC            
C978: 18                                  
C979: F8 AC AC       EORB    $ACAC           
C97C: F8 18 78       EORB    $1878           
C97F: 48             LSLA                    
C980: 78 CC FC       LSL     $CCFC                          ; 
C983: 30 60          LEAX    0,S             
C985: 7C D4 D4       INC     $D4D4                          ; 
C988: 7C 60 30       INC     $6030           
C98B: FC CC 78       LDD     $CC78                          ; 
C98E: 48             LSLA                    
C98F: 78 08 20       LSL     $0820           
C992: 15                                  
C993: 15                                  
C994: 20 82          BRA     $C918                          ; 
C996: 20 80          BRA     $C918                          ; 
C998: 00 00          NEG     <$00            
C99A: 80 00          SUBA    #$00            
C99C: 00 00          NEG     <$00            
C99E: 00 00          NEG     <$00            
C9A0: 00 00          NEG     <$00            
C9A2: 02                                  
C9A3: 08 05          ASL     <$05            
C9A5: 05                                  
C9A6: 08 20          ASL     <$20            
C9A8: 08 20          ASL     <$20            
C9AA: 40             NEGA                    
C9AB: 40             NEGA                    
C9AC: 20 80          BRA     $C92E                          ; 
C9AE: 00 00          NEG     <$00            
C9B0: 00 00          NEG     <$00            
C9B2: 00 00          NEG     <$00            
C9B4: 00 02          NEG     <$02            
C9B6: 01                                  
C9B7: 01                                  
C9B8: 02                                  
C9B9: 08 82          ASL     <$82            
C9BB: 08 50          ASL     <$50            
C9BD: 50             NEGB                    
C9BE: 08 20          ASL     <$20            
C9C0: 00 00          NEG     <$00            
C9C2: 00 00          NEG     <$00            
C9C4: 00 00          NEG     <$00            
C9C6: 00 00          NEG     <$00            
C9C8: 00 00          NEG     <$00            
C9CA: 00 02          NEG     <$02            
C9CC: 20 82          BRA     $C950                          ; 
C9CE: 54             LSRB                    
C9CF: 54             LSRB                    
C9D0: 82 08          SBCA    #$08            
C9D2: 80 00          SUBA    #$00            
C9D4: 00 00          NEG     <$00            
C9D6: 00 00          NEG     <$00            
C9D8: 80 20          SUBA    #$20            
C9DA: 15                                  
C9DB: 95 20          BITA    <$20            
C9DD: 00 00          NEG     <$00            
C9DF: 80 20          SUBA    #$20            
C9E1: 00 80          NEG     <$80            
C9E3: 20 00          BRA     $C9E5                          ; 
C9E5: 00 00          NEG     <$00            
C9E7: 00 00          NEG     <$00            
C9E9: 00 20          NEG     <$20            
C9EB: 08 05          ASL     <$05            
C9ED: 25 08          BCS     $C9F7                          ; 
C9EF: 00 00          NEG     <$00            
C9F1: 20 48          BRA     $CA3B                          ; 
C9F3: 40             NEGA                    
C9F4: 20 08          BRA     $C9FE                          ; 
C9F6: 00 00          NEG     <$00            
C9F8: 00 00          NEG     <$00            
C9FA: 00 00          NEG     <$00            
C9FC: 08 02          ASL     <$02            
C9FE: 01                                  
C9FF: 09 02          ROL     <$02            
CA01: 00 00          NEG     <$00            
CA03: 08 52          ASL     <$52            
CA05: 50             NEGB                    
CA06: 08 02          ASL     <$02            
CA08: 00 00          NEG     <$00            
CA0A: 00 00          NEG     <$00            
CA0C: 00 00          NEG     <$00            
CA0E: 02                                  
CA0F: 00 00          NEG     <$00            
CA11: 02                                  
CA12: 00 00          NEG     <$00            
CA14: 00 82          NEG     <$82            
CA16: 54             LSRB                    
CA17: 54             LSRB                    
CA18: 82 00          SBCA    #$00            
CA1A: 00 00          NEG     <$00            
CA1C: 80 00          SUBA    #$00            
CA1E: 00 80          NEG     <$80            
CA20: 82 20          SBCA    #$20            
CA22: 15                                  
CA23: 15                                  
CA24: 20 08          BRA     $CA2E                          ; 
CA26: 00 80          NEG     <$80            
CA28: 00 00          NEG     <$00            
CA2A: 80 20          SUBA    #$20            
CA2C: 00 00          NEG     <$00            
CA2E: 00 00          NEG     <$00            
CA30: 00 00          NEG     <$00            
CA32: 20 08          BRA     $CA3C                          ; 
CA34: 05                                  
CA35: 05                                  
CA36: 08 02          ASL     <$02            
CA38: 80 20          SUBA    #$20            
CA3A: 40             NEGA                    
CA3B: 40             NEGA                    
CA3C: 20 08          BRA     $CA46                          ; 
CA3E: 00 00          NEG     <$00            
CA40: 00 00          NEG     <$00            
CA42: 00 00          NEG     <$00            
CA44: 08 02          ASL     <$02            
CA46: 01                                  
CA47: 01                                  
CA48: 02                                  
CA49: 00 20          NEG     <$20            
CA4B: 08 50          ASL     <$50            
CA4D: 50             NEGB                    
CA4E: 08 82          ASL     <$82            
CA50: 00 00          NEG     <$00            
CA52: 00 00          NEG     <$00            
CA54: 00 00          NEG     <$00            
CA56: 02                                  
CA57: 00 00          NEG     <$00            
CA59: 00 00          NEG     <$00            
CA5B: 00 08          NEG     <$08            
CA5D: 82 54          SBCA    #$54            
CA5F: 54             LSRB                    
CA60: 82 20          SBCA    #$20            
CA62: 00 00          NEG     <$00            
CA64: 00 00          NEG     <$00            
CA66: 00 80          NEG     <$80            
CA68: 00 20          NEG     <$20            
CA6A: 95 15          BITA    <$15            
CA6C: 20 80          BRA     $C9EE                          ; 
CA6E: 20 80          BRA     $C9F0                          ; 
CA70: 00 20          NEG     <$20            
CA72: 80 00          SUBA    #$00            
CA74: 00 00          NEG     <$00            
CA76: 00 00          NEG     <$00            
CA78: 00 00          NEG     <$00            
CA7A: 00 08          NEG     <$08            
CA7C: 25 05          BCS     $CA83                          ; 
CA7E: 08 20          ASL     <$20            
CA80: 08 20          ASL     <$20            
CA82: 40             NEGA                    
CA83: 48             LSLA                    
CA84: 20 00          BRA     $CA86                          ; 
CA86: 00 00          NEG     <$00            
CA88: 00 00          NEG     <$00            
CA8A: 00 00          NEG     <$00            
CA8C: 00 02          NEG     <$02            
CA8E: 09 01          ROL     <$01            
CA90: 02                                  
CA91: 08 02          ASL     <$02            
CA93: 08 50          ASL     <$50            
CA95: 52                                  
CA96: 08 00          ASL     <$00            
CA98: 00 00          NEG     <$00            
CA9A: 00 00          NEG     <$00            
CA9C: 00 00          NEG     <$00            
CA9E: 00 00          NEG     <$00            
CAA0: 02                                  
CAA1: 00 00          NEG     <$00            
CAA3: 02                                  
CAA4: 00 82          NEG     <$82            
CAA6: 54             LSRB                    
CAA7: 54             LSRB                    
CAA8: 82 00          SBCA    #$00            
CAAA: 80 00          SUBA    #$00            
CAAC: 00 80          NEG     <$80            
CAAE: 00 00          NEG     <$00            
CAB0: 00 00          NEG     <$00            
CAB2: 00 00          NEG     <$00            
CAB4: 00 00          NEG     <$00            
CAB6: 00 00          NEG     <$00            
CAB8: 00 00          NEG     <$00            
CABA: 00 00          NEG     <$00            
CABC: 00 00          NEG     <$00            
CABE: 00 00          NEG     <$00            
CAC0: 01                                  
CAC1: 07 00          ASR     <$00            
CAC3: 00 00          NEG     <$00            
CAC5: 00 01          NEG     <$01            
CAC7: 07 00          ASR     <$00            
CAC9: 00 00          NEG     <$00            
CACB: 00 00          NEG     <$00            
CACD: 00 00          NEG     <$00            
CACF: 01                                  
CAD0: 20 08          BRA     $CADA                          ; 
CAD2: 02                                  
CAD3: 00 00          NEG     <$00            
CAD5: 00 01          NEG     <$01            
CAD7: 05                                  
CAD8: 01                                  
CAD9: 01                                  
CADA: 00 00          NEG     <$00            
CADC: 14                                  
CADD: 21 21          BRN     $CB00                          ; 
CADF: 21 E0          BRN     $CAC1                          ; 
CAE1: 80 14          SUBA    #$14            
CAE3: 21 21          BRN     $CB06                          ; 
CAE5: 21 E1          BRN     $CAC8                          ; 
CAE7: 81 02          CMPA    #$02            
CAE9: 02                                  
CAEA: 02                                  
CAEB: 02                                  
CAEC: 02                                  
CAED: 02                                  
CAEE: 15                                  
CAEF: 54             LSRB                    
CAF0: 00 00          NEG     <$00            
CAF2: 00 80          NEG     <$80            
CAF4: 20 51          BRA     $CB47                          ; 
CAF6: 55                                  
CAF7: 75                                  
CAF8: 55                                  
CAF9: 50             NEGB                    
CAFA: 55                                  
CAFB: 11                                  
CAFC: 55                                  
CAFD: 51                                  
CAFE: 55                                  
CAFF: 51                                  
CB00: 55                                  
CB01: 11                                  
CB02: 55                                  
CB03: 55                                  
CB04: 51                                  
CB05: 55                                  
CB06: 51                                  
CB07: 55                                  
CB08: 95 00          BITA    <$00            
CB0A: 00 00          NEG     <$00            
CB0C: 00 00          NEG     <$00            
CB0E: 00 00          NEG     <$00            
CB10: 00 00          NEG     <$00            
CB12: 02                                  
CB13: 08 20          ASL     <$20            
CB15: 40             NEGA                    
CB16: 50             NEGB                    
CB17: D4 50          ANDB    <$50            
CB19: 50             NEGB                    
CB1A: 40             NEGA                    
CB1B: 00 45          NEG     <$45            
CB1D: 50             NEGB                    
CB1E: 50             NEGB                    
CB1F: 50             NEGB                    
CB20: 41                                  
CB21: 00 45          NEG     <$45            
CB23: 50             NEGB                    
CB24: 50             NEGB                    
CB25: 50             NEGB                    
CB26: 51                                  
CB27: 50             NEGB                    
CB28: 28 08          BVC     $CB32                          ; 
CB2A: 08 08          ASL     <$08            
CB2C: 08 08          ASL     <$08            
CB2E: 15                                  
CB2F: 05                                  
CB30: 20 80          BRA     $CAB2                          ; 
CB32: 00 00          NEG     <$00            
CB34: 00 00          NEG     <$00            
CB36: 00 00          NEG     <$00            
CB38: 00 00          NEG     <$00            
CB3A: 00 00          NEG     <$00            
CB3C: 00 80          NEG     <$80            
CB3E: 80 80          SUBA    #$80            
CB40: E0 78          SUBB    -8,S            
CB42: 00 80          NEG     <$80            
CB44: 80 80          SUBA    #$80            
CB46: E0 78          SUBB    -8,S            
CB48: 00 00          NEG     <$00            
CB4A: 00 00          NEG     <$00            
CB4C: 00 00          NEG     <$00            
CB4E: 00 50          NEG     <$50            
CB50: 00 00          NEG     <$00            
CB52: 00 00          NEG     <$00            
CB54: 00 00          NEG     <$00            
CB56: 00 00          NEG     <$00            
CB58: 00 00          NEG     <$00            
CB5A: 00 00          NEG     <$00            
CB5C: 00 00          NEG     <$00            
CB5E: 00 00          NEG     <$00            
CB60: 01                                  
CB61: 07 00          ASR     <$00            
CB63: 00 00          NEG     <$00            
CB65: 00 01          NEG     <$01            
CB67: 07 00          ASR     <$00            
CB69: 00 00          NEG     <$00            
CB6B: 00 00          NEG     <$00            
CB6D: 01                                  
CB6E: 00 00          NEG     <$00            
CB70: 20 08          BRA     $CB7A                          ; 
CB72: 02                                  
CB73: 00 00          NEG     <$00            
CB75: 00 01          NEG     <$01            
CB77: 05                                  
CB78: 01                                  
CB79: 01                                  
CB7A: 00 00          NEG     <$00            
CB7C: 14                                  
CB7D: 21 21          BRN     $CBA0                          ; 
CB7F: 21 E0          BRN     $CB61                          ; 
CB81: 80 14          SUBA    #$14            
CB83: 21 21          BRN     $CBA6                          ; 
CB85: 21 E1          BRN     $CB68                          ; 
CB87: 81 02          CMPA    #$02            
CB89: 02                                  
CB8A: 02                                  
CB8B: 02                                  
CB8C: 15                                  
CB8D: 54             LSRB                    
CB8E: 00 00          NEG     <$00            
CB90: 00 00          NEG     <$00            
CB92: 00 80          NEG     <$80            
CB94: 20 51          BRA     $CBE7                          ; 
CB96: 55                                  
CB97: 75                                  
CB98: 55                                  
CB99: 50             NEGB                    
CB9A: 55                                  
CB9B: 11                                  
CB9C: 55                                  
CB9D: 51                                  
CB9E: 55                                  
CB9F: 51                                  
CBA0: 55                                  
CBA1: 11                                  
CBA2: 55                                  
CBA3: 55                                  
CBA4: 51                                  
CBA5: 55                                  
CBA6: 51                                  
CBA7: 55                                  
CBA8: 95 00          BITA    <$00            
CBAA: 00 00          NEG     <$00            
CBAC: 00 00          NEG     <$00            
CBAE: 00 00          NEG     <$00            
CBB0: 00 00          NEG     <$00            
CBB2: 02                                  
CBB3: 08 20          ASL     <$20            
CBB5: 40             NEGA                    
CBB6: 50             NEGB                    
CBB7: D4 51          ANDB    <$51            
CBB9: 50             NEGB                    
CBBA: 40             NEGA                    
CBBB: 00 45          NEG     <$45            
CBBD: 50             NEGB                    
CBBE: 51                                  
CBBF: 50             NEGB                    
CBC0: 40             NEGA                    
CBC1: 00 45          NEG     <$45            
CBC3: 50             NEGB                    
CBC4: 50             NEGB                    
CBC5: 50             NEGB                    
CBC6: 50             NEGB                    
CBC7: 50             NEGB                    
CBC8: 28 08          BVC     $CBD2                          ; 
CBCA: 08 08          ASL     <$08            
CBCC: 08 08          ASL     <$08            
CBCE: 15                                  
CBCF: 05                                  
CBD0: 20 80          BRA     $CB52                          ; 
CBD2: 00 00          NEG     <$00            
CBD4: 00 00          NEG     <$00            
CBD6: 00 78          NEG     <$78            
CBD8: E0 80          SUBB    ,X+             
CBDA: 80 80          SUBA    #$80            
CBDC: 00 78          NEG     <$78            
CBDE: E0 80          SUBB    ,X+             
CBE0: 80 80          SUBA    #$80            
CBE2: 00 00          NEG     <$00            
CBE4: 00 00          NEG     <$00            
CBE6: 00 00          NEG     <$00            
CBE8: 00 00          NEG     <$00            
CBEA: 00 00          NEG     <$00            
CBEC: 00 00          NEG     <$00            
CBEE: 00 50          NEG     <$50            
CBF0: 00 00          NEG     <$00            
CBF2: 00 00          NEG     <$00            
CBF4: 00 00          NEG     <$00            
CBF6: 00 07          NEG     <$07            
CBF8: 01                                  
CBF9: 00 00          NEG     <$00            
CBFB: 00 00          NEG     <$00            
CBFD: 07 01          ASR     <$01            
CBFF: 00 00          NEG     <$00            
CC01: 00 00          NEG     <$00            
CC03: 00 00          NEG     <$00            
CC05: 00 00          NEG     <$00            
CC07: 00 00          NEG     <$00            
CC09: 00 00          NEG     <$00            
CC0B: 00 00          NEG     <$00            
CC0D: 00 00          NEG     <$00            
CC0F: 01                                  
CC10: 02                                  
CC11: 08 02          ASL     <$02            
CC13: 00 00          NEG     <$00            
CC15: 00 01          NEG     <$01            
CC17: B5 E1 21       BITA    $E121           
CC1A: 20 20          BRA     $CC3C                          ; 
CC1C: 14                                  
CC1D: 81 E1          CMPA    #$E1            
CC1F: 21 20          BRN     $CC41                          ; 
CC21: 20 14          BRA     $CC37                          ; 
CC23: 01                                  
CC24: 01                                  
CC25: 01                                  
CC26: 01                                  
CC27: 01                                  
CC28: 02                                  
CC29: 02                                  
CC2A: 02                                  
CC2B: 02                                  
CC2C: 02                                  
CC2D: 02                                  
CC2E: 15                                  
CC2F: 54             LSRB                    
CC30: 00 00          NEG     <$00            
CC32: 00 80          NEG     <$80            
CC34: 20 51          BRA     $CC87                          ; 
CC36: 55                                  
CC37: 75                                  
CC38: 55                                  
CC39: 50             NEGB                    
CC3A: 55                                  
CC3B: 11                                  
CC3C: 55                                  
CC3D: 51                                  
CC3E: 55                                  
CC3F: 51                                  
CC40: 55                                  
CC41: 11                                  
CC42: 55                                  
CC43: 55                                  
CC44: 51                                  
CC45: 55                                  
CC46: 51                                  
CC47: 55                                  
CC48: 95 00          BITA    <$00            
CC4A: 00 00          NEG     <$00            
CC4C: 00 00          NEG     <$00            
CC4E: 00 00          NEG     <$00            
CC50: 02                                  
CC51: 00 02          NEG     <$02            
CC53: 08 20          ASL     <$20            
CC55: 40             NEGA                    
CC56: 50             NEGB                    
CC57: D4 50          ANDB    <$50            
CC59: 50             NEGB                    
CC5A: 40             NEGA                    
CC5B: 00 45          NEG     <$45            
CC5D: 50             NEGB                    
CC5E: 50             NEGB                    
CC5F: 50             NEGB                    
CC60: 41                                  
CC61: 00 45          NEG     <$45            
CC63: 50             NEGB                    
CC64: 50             NEGB                    
CC65: 50             NEGB                    
CC66: 51                                  
CC67: 50             NEGB                    
CC68: 28 08          BVC     $CC72                          ; 
CC6A: 08 08          ASL     <$08            
CC6C: 15                                  
CC6D: 05                                  
CC6E: 00 00          NEG     <$00            
CC70: 00 80          NEG     <$80            
CC72: 00 00          NEG     <$00            
CC74: 00 00          NEG     <$00            
CC76: 00 00          NEG     <$00            
CC78: 00 00          NEG     <$00            
CC7A: 00 00          NEG     <$00            
CC7C: 00 80          NEG     <$80            
CC7E: 80 80          SUBA    #$80            
CC80: E0 78          SUBB    -8,S            
CC82: 00 80          NEG     <$80            
CC84: 80 80          SUBA    #$80            
CC86: E0 78          SUBB    -8,S            
CC88: 00 00          NEG     <$00            
CC8A: 00 00          NEG     <$00            
CC8C: 00 50          NEG     <$50            
CC8E: 00 00          NEG     <$00            
CC90: 06 0A          ROR     <$0A            
CC92: 10 2D 00 00    LBLT    $0000           
CC96: 06 0A          ROR     <$0A            
CC98: 10 2D 00 00    LBLT    $0000           
CC9C: 06 0A          ROR     <$0A            
CC9E: 10 2D 00 00    LBLT    $0000           
CCA2: 18                                  
CCA3: 2B 15          BMI     $CCBA                          ; 
CCA5: 98 0D          EORA    <$0D            
CCA7: 99 06          ADCA    <$06            
CCA9: 0A 1B          DEC     <$1B            
CCAB: 35 10          PULS    X               
CCAD: 2D 06          BLT     $CCB5                          ; 
CCAF: 0A 00          DEC     <$00            
CCB1: 00 00          NEG     <$00            
CCB3: 00 06          NEG     <$06            
CCB5: 0A 10          DEC     <$10            
CCB7: 2D 00          BLT     $CCB9                          ; 
CCB9: 00 06          NEG     <$06            
CCBB: 0A 10          DEC     <$10            
CCBD: 2D 00          BLT     $CCBF                          ; 
CCBF: 00 06          NEG     <$06            
CCC1: 0A 10          DEC     <$10            
CCC3: 2D 00          BLT     $CCC5                          ; 
CCC5: 00 18          NEG     <$18            
CCC7: 2B 15          BMI     $CCDE                          ; 
CCC9: 98 0D          EORA    <$0D            
CCCB: 99 06          ADCA    <$06            
CCCD: 0A 1B          DEC     <$1B            
CCCF: 35 10          PULS    X               
CCD1: 2D 1E          BLT     $CCF1                          ; 
CCD3: 35 00          PULS    $00             
CCD5: 00 00          NEG     <$00            
CCD7: 00 06          NEG     <$06            
CCD9: 0A 15          DEC     <$15            
CCDB: 98 0D          EORA    <$0D            
CCDD: 99 06          ADCA    <$06            
CCDF: 0A 15          DEC     <$15            
CCE1: 98 0D          EORA    <$0D            
CCE3: 99 06          ADCA    <$06            
CCE5: 0A 14          DEC     <$14            
CCE7: 60 0C          NEG     12,X            
CCE9: 19             DAA                     
CCEA: 06 0A          ROR     <$0A            
CCEC: 14                                  
CCED: 60 0C          NEG     12,X            
CCEF: 19             DAA                     
CCF0: 06 0A          ROR     <$0A            
CCF2: 12             NOP                     
CCF3: 27 0A          BEQ     $CCFF                          ; 
CCF5: CB 06          ADDB    #$06            
CCF7: 0A 12          DEC     <$12            
CCF9: 27 0A          BEQ     $CD05                          ; 
CCFB: CB 18          ADDB    #$18            
CCFD: 2B 10          BMI     $CD0F                          ; 
CCFF: 2D 0A          BLT     $CD0B                          ; 
CD01: 2F 06          BLE     $CD09                          ; 
CD03: 0A 00          DEC     <$00            
CD05: 00 00          NEG     <$00            
CD07: 00 06          NEG     <$06            
CD09: 0A 10          DEC     <$10            
CD0B: 2D 00          BLT     $CD0D                          ; 
CD0D: 00 06          NEG     <$06            
CD0F: 0A 10          DEC     <$10            
CD11: 2D 00          BLT     $CD13                          ; 
CD13: 00 06          NEG     <$06            
CD15: 0A 10          DEC     <$10            
CD17: 2D 00          BLT     $CD19                          ; 
CD19: 00 18          NEG     <$18            
CD1B: 2B 14          BMI     $CD31                          ; 
CD1D: 60 0C          NEG     12,X            
CD1F: 19             DAA                     
CD20: 06 0A          ROR     <$0A            
CD22: 18                                  
CD23: 35 10          PULS    X               
CD25: 2D 06          BLT     $CD2D                          ; 
CD27: 0A 00          DEC     <$00            
CD29: 00 00          NEG     <$00            
CD2B: 00 06          NEG     <$06            
CD2D: 0A 10          DEC     <$10            
CD2F: 2D 00          BLT     $CD31                          ; 
CD31: 00 06          NEG     <$06            
CD33: 0A 10          DEC     <$10            
CD35: 2D 00          BLT     $CD37                          ; 
CD37: 00 06          NEG     <$06            
CD39: 0A 10          DEC     <$10            
CD3B: 2D 00          BLT     $CD3D                          ; 
CD3D: 00 18          NEG     <$18            
CD3F: 2B 14          BMI     $CD55                          ; 
CD41: 60 0C          NEG     12,X            
CD43: 19             DAA                     
CD44: 06 0A          ROR     <$0A            
CD46: 18                                  
CD47: 35 10          PULS    X               
CD49: 2D 1E          BLT     $CD69                          ; 
CD4B: 35 00          PULS    $00             
CD4D: 00 00          NEG     <$00            
CD4F: 00 06          NEG     <$06            
CD51: 0A 20          DEC     <$20            
CD53: 5B                                  
CD54: 14                                  
CD55: 60 06          NEG     6,X             
CD57: 0A 24          DEC     <$24            
CD59: 51                                  
CD5A: 15                                  
CD5B: 98 06          EORA    <$06            
CD5D: 0A 20          DEC     <$20            
CD5F: 5B                                  
CD60: 14                                  
CD61: 60 06          NEG     6,X             
CD63: 0A 1C          DEC     <$1C            
CD65: D2 12          SBCB    <$12            
CD67: 27 06          BEQ     $CD6F                          ; 
CD69: 0A 1B          DEC     <$1B            
CD6B: 35 10          PULS    X               
CD6D: 2D 06          BLT     $CD75                          ; 
CD6F: 0A 18          DEC     <$18            
CD71: 35 18          PULS    DP,X            
CD73: F4 06 0A       ANDB    $060A           
CD76: 15                                  
CD77: 98 0D          EORA    <$0D            
CD79: 99 70          ADCA    <$70            
CD7B: 88 98          EORA    #$98            
CD7D: A8 C8 88       EORA    $88,U           
CD80: 70 00 00       NEG     $0000           
CD83: 20 60          BRA     $CDE5                          ; 
CD85: 20 20          BRA     $CDA7                          ; 
CD87: 20 20          BRA     $CDA9                          ; 
CD89: 70 00 00       NEG     $0000           
CD8C: 70 88 08       NEG     $8808           
CD8F: 30 40          LEAX    0,U             
CD91: 80 F8          SUBA    #$F8            
CD93: 00 00          NEG     <$00            
CD95: 70 88 08       NEG     $8808           
CD98: 30 08          LEAX    8,X             
CD9A: 88 70          EORA    #$70            
CD9C: 00 00          NEG     <$00            
CD9E: 10                                  
CD9F: 30 50          LEAX    -16,U           
CDA1: F8 10 10       EORB    $1010           
CDA4: 10                                  
CDA5: 00 00          NEG     <$00            
CDA7: F8 80 80       EORB    $8080           
CDAA: F0 08 08       SUBB    $0808           
CDAD: F0 00 00       SUBB    $0000           
CDB0: 70 88 80       NEG     $8880           
CDB3: F0 88 88       SUBB    $8888           
CDB6: 70 00 00       NEG     $0000           
CDB9: F8 88 10       EORB    $8810           
CDBC: 10                                  
CDBD: 20 20          BRA     $CDDF                          ; 
CDBF: 20 00          BRA     $CDC1                          ; 
CDC1: 00 70          NEG     <$70            
CDC3: 88 88          EORA    #$88            
CDC5: 70 88 88       NEG     $8888           
CDC8: 70 00 00       NEG     $0000           
CDCB: 70 88 88       NEG     $8888           
CDCE: 78 08 88       LSL     $0888           
CDD1: 70 00 00       NEG     $0000           
CDD4: 20 50          BRA     $CE26                          ; 
CDD6: 88 F8          EORA    #$F8            
CDD8: 88 88          EORA    #$88            
CDDA: 88 00          EORA    #$00            
CDDC: 00 F0          NEG     <$F0            
CDDE: 48             LSLA                    
CDDF: 48             LSLA                    
CDE0: 70 48 48       NEG     $4848           
CDE3: F0 00 00       SUBB    $0000           
CDE6: 70 88 80       NEG     $8880           
CDE9: 80 80          SUBA    #$80            
CDEB: 88 70          EORA    #$70            
CDED: 00 00          NEG     <$00            
CDEF: F0 48 48       SUBB    $4848           
CDF2: 48             LSLA                    
CDF3: 48             LSLA                    
CDF4: 48             LSLA                    
CDF5: F0 00 00       SUBB    $0000           
CDF8: F8 80 80       EORB    $8080           
CDFB: F0 80 80       SUBB    $8080           
CDFE: F8 00 00       EORB    $0000           
CE01: F8 80 80       EORB    $8080           
CE04: F0 80 80       SUBB    $8080           
CE07: 80 00          SUBA    #$00            
CE09: 00 70          NEG     <$70            
CE0B: 88 80          EORA    #$80            
CE0D: B8 88 88       EORA    $8888           
CE10: 70 00 00       NEG     $0000           
CE13: 88 88          EORA    #$88            
CE15: 88 F8          EORA    #$F8            
CE17: 88 88          EORA    #$88            
CE19: 88 00          EORA    #$00            
CE1B: 00 F8          NEG     <$F8            
CE1D: 20 20          BRA     $CE3F                          ; 
CE1F: 20 20          BRA     $CE41                          ; 
CE21: 20 F8          BRA     $CE1B                          ; 
CE23: 00 00          NEG     <$00            
CE25: 38                                  
CE26: 10                                  
CE27: 10                                  
CE28: 10                                  
CE29: 10                                  
CE2A: 90 60          SUBA    <$60            
CE2C: 00 00          NEG     <$00            
CE2E: 88 90          EORA    #$90            
CE30: A0 C0          SUBA    ,U+             
CE32: A0                                  
CE33: 90 88          SUBA    <$88            
CE35: 00 00          NEG     <$00            
CE37: 80 80          SUBA    #$80            
CE39: 80 80          SUBA    #$80            
CE3B: 80 80          SUBA    #$80            
CE3D: F0 00 00       SUBB    $0000           
CE40: 88 D8          EORA    #$D8            
CE42: A8 A8 88       EORA    $88,Y           
CE45: 88 88          EORA    #$88            
CE47: 00 00          NEG     <$00            
CE49: 88 C8          EORA    #$C8            
CE4B: C8 A8          EORB    #$A8            
CE4D: 98 98          EORA    <$98            
CE4F: 88 00          EORA    #$00            
CE51: 00 70          NEG     <$70            
CE53: 88 88          EORA    #$88            
CE55: 88 88          EORA    #$88            
CE57: 88 70          EORA    #$70            
CE59: 00 00          NEG     <$00            
CE5B: F0 88 88       SUBB    $8888           
CE5E: F0 80 80       SUBB    $8080           
CE61: 80 00          SUBA    #$00            
CE63: 00 70          NEG     <$70            
CE65: 88 88          EORA    #$88            
CE67: 88 A8          EORA    #$A8            
CE69: 90 68          SUBA    <$68            
CE6B: 00 00          NEG     <$00            
CE6D: F0 88 88       SUBB    $8888           
CE70: F0 A0 90       SUBB    $A090           
CE73: 88 00          EORA    #$00            
CE75: 00 70          NEG     <$70            
CE77: 88 80          EORA    #$80            
CE79: 70 08 88       NEG     $0888           
CE7C: 70 00 00       NEG     $0000           
CE7F: F8 A8 20       EORB    $A820           
CE82: 20 20          BRA     $CEA4                          ; 
CE84: 20 20          BRA     $CEA6                          ; 
CE86: 00 00          NEG     <$00            
CE88: 88 88          EORA    #$88            
CE8A: 88 88          EORA    #$88            
CE8C: 88 88          EORA    #$88            
CE8E: 70 00 00       NEG     $0000           
CE91: 88 88          EORA    #$88            
CE93: 88 88          EORA    #$88            
CE95: 50             NEGB                    
CE96: 50             NEGB                    
CE97: 20 00          BRA     $CE99                          ; 
CE99: 00 88          NEG     <$88            
CE9B: 88 88          EORA    #$88            
CE9D: 88 A8          EORA    #$A8            
CE9F: A8 50          EORA    -16,U           
CEA1: 00 00          NEG     <$00            
CEA3: 88 88          EORA    #$88            
CEA5: 50             NEGB                    
CEA6: 20 50          BRA     $CEF8                          ; 
CEA8: 88 88          EORA    #$88            
CEAA: 00 00          NEG     <$00            
CEAC: 88 88          EORA    #$88            
CEAE: 50             NEGB                    
CEAF: 20 20          BRA     $CED1                          ; 
CEB1: 20 20          BRA     $CED3                          ; 
CEB3: 00 00          NEG     <$00            
CEB5: F8 08 10       EORB    $0810           
CEB8: 20 40          BRA     $CEFA                          ; 
CEBA: 80 F8          SUBA    #$F8            
CEBC: 00 00          NEG     <$00            
CEBE: 00 00          NEG     <$00            
CEC0: 60 10          NEG     -16,X           
CEC2: 70 90 68       NEG     $9068           
CEC5: 00 00          NEG     <$00            
CEC7: 80 80          SUBA    #$80            
CEC9: F0 88 88       SUBB    $8888           
CECC: 88 F0          EORA    #$F0            
CECE: 00 00          NEG     <$00            
CED0: 00 00          NEG     <$00            
CED2: 70 88 80       NEG     $8880           
CED5: 88 70          EORA    #$70            
CED7: 00 00          NEG     <$00            
CED9: 08 08          ASL     <$08            
CEDB: 78 88 88       LSL     $8888           
CEDE: 88 78          EORA    #$78            
CEE0: 00 00          NEG     <$00            
CEE2: 00 00          NEG     <$00            
CEE4: 70 88 F8       NEG     $88F8           
CEE7: 80 70          SUBA    #$70            
CEE9: 00 00          NEG     <$00            
CEEB: 20 50          BRA     $CF3D                          ; 
CEED: 40             NEGA                    
CEEE: E0 40          SUBB    0,U             
CEF0: 40             NEGA                    
CEF1: 40             NEGA                    
CEF2: 00 00          NEG     <$00            
CEF4: 00 00          NEG     <$00            
CEF6: 70 88 88       NEG     $8888           
CEF9: 78 08 88       LSL     $0888           
CEFC: 70 80 80       NEG     $8080           
CEFF: B0 C8 88       SUBA    $C888                          ; 
CF02: 88 88          EORA    #$88            
CF04: 00 00          NEG     <$00            
CF06: 20 00          BRA     $CF08                          ; 
CF08: 60 20          NEG     0,Y             
CF0A: 20 20          BRA     $CF2C                          ; 
CF0C: 70 00 00       NEG     $0000           
CF0F: 20 00          BRA     $CF11                          ; 
CF11: 60 20          NEG     0,Y             
CF13: 20 20          BRA     $CF35                          ; 
CF15: 20 A0          BRA     $CEB7                          ; 
CF17: 40             NEGA                    
CF18: 80 80          SUBA    #$80            
CF1A: 90 A0          SUBA    <$A0            
CF1C: C0 A0          SUBB    #$A0            
CF1E: 90 00          SUBA    <$00            
CF20: 00 60          NEG     <$60            
CF22: 20 20          BRA     $CF44                          ; 
CF24: 20 20          BRA     $CF46                          ; 
CF26: 20 70          BRA     $CF98                          ; 
CF28: 00 00          NEG     <$00            
CF2A: 00 00          NEG     <$00            
CF2C: D0 A8          SUBB    <$A8            
CF2E: A8 A8 A8       EORA    $A8,Y           
CF31: 00 00          NEG     <$00            
CF33: 00 00          NEG     <$00            
CF35: B0 C8 88       SUBA    $C888                          ; 
CF38: 88 88          EORA    #$88            
CF3A: 00 00          NEG     <$00            
CF3C: 00 00          NEG     <$00            
CF3E: 70 88 88       NEG     $8888           
CF41: 88 70          EORA    #$70            
CF43: 00 00          NEG     <$00            
CF45: 00 00          NEG     <$00            
CF47: B0 C8 88       SUBA    $C888                          ; 
CF4A: 88 F0          EORA    #$F0            
CF4C: 80 80          SUBA    #$80            
CF4E: 00 00          NEG     <$00            
CF50: 68 98 88       ASL     [$88,X]         
CF53: 98 68          EORA    <$68            
CF55: 08 08          ASL     <$08            
CF57: 00 00          NEG     <$00            
CF59: B0 C8 80       SUBA    $C880                          ; 
CF5C: 80 80          SUBA    #$80            
CF5E: 00 00          NEG     <$00            
CF60: 00 00          NEG     <$00            
CF62: 70 80 70       NEG     $8070           
CF65: 08 70          ASL     <$70            
CF67: 00 00          NEG     <$00            
CF69: 40             NEGA                    
CF6A: 40             NEGA                    
CF6B: E0 40          SUBB    0,U             
CF6D: 40             NEGA                    
CF6E: 50             NEGB                    
CF6F: 20 00          BRA     $CF71                          ; 
CF71: 00 00          NEG     <$00            
CF73: 00 88          NEG     <$88            
CF75: 88 88          EORA    #$88            
CF77: 98 68          EORA    <$68            
CF79: 00 00          NEG     <$00            
CF7B: 00 00          NEG     <$00            
CF7D: 88 88          EORA    #$88            
CF7F: 88 50          EORA    #$50            
CF81: 20 00          BRA     $CF83                          ; 
CF83: 00 00          NEG     <$00            
CF85: 00 88          NEG     <$88            
CF87: A8 A8 A8       EORA    $A8,Y           
CF8A: 50             NEGB                    
CF8B: 00 00          NEG     <$00            
CF8D: 00 00          NEG     <$00            
CF8F: 88 50          EORA    #$50            
CF91: 20 50          BRA     $CFE3                          ; 
CF93: 88 00          EORA    #$00            
CF95: 00 00          NEG     <$00            
CF97: 00 88          NEG     <$88            
CF99: 88 88          EORA    #$88            
CF9B: 78 08 08       LSL     $0808           
CF9E: 70 00 00       NEG     $0000           
CFA1: F8 10 20       EORB    $1020           
CFA4: 40             NEGA                    
CFA5: F8 00 00       EORB    $0000           
CFA8: 00 00          NEG     <$00            
CFAA: 00 00          NEG     <$00            
CFAC: 00 00          NEG     <$00            
CFAE: 00 00          NEG     <$00            
CFB0: 00 20          NEG     <$20            
CFB2: 20 20          BRA     $CFD4                          ; 
CFB4: 20 20          BRA     $CFD6                          ; 
CFB6: 00 20          NEG     <$20            
CFB8: 00 00          NEG     <$00            
CFBA: 00 00          NEG     <$00            
CFBC: 00 F8          NEG     <$F8            
CFBE: 00 00          NEG     <$00            
CFC0: 00 00          NEG     <$00            
CFC2: 00 00          NEG     <$00            
CFC4: 00 00          NEG     <$00            
CFC6: 00 00          NEG     <$00            
CFC8: 20 20          BRA     $CFEA                          ; 
CFCA: 00 00          NEG     <$00            
CFCC: 00 00          NEG     <$00            
CFCE: 20 00          BRA     $CFD0                          ; 
CFD0: 00 20          NEG     <$20            
CFD2: 00 00          NEG     <$00            
CFD4: 00 20          NEG     <$20            
CFD6: 20 40          BRA     $D018                          ; 
CFD8: 00 00          NEG     <$00            
CFDA: 00 00          NEG     <$00            
CFDC: 00 00          NEG     <$00
```

```code            
Start:
CFDE: 12             NOP                     
CFDF: 10 CE 03 F0    LDS     #$03F0          
CFE3: 0F B3          CLR     <$B3            
CFE5: 0F B4          CLR     <$B4            
CFE7: 0F B1          CLR     <$B1            
CFE9: 0F B2          CLR     <$B2            
CFEB: 86 A5          LDA     #$A5            
CFED: B7 10 00       STA     $1000           
CFF0: 0F 00          CLR     <$00            
CFF2: A1 8D 40 0A    CMPA    $400A,PC        
CFF6: 27 1D          BEQ     $D015                          ;
 
CFF8: BD D2 BE       JSR     $D2BE                          ; 
CFFB: CE 04 00       LDU     #$0400          
CFFE: DF 9E          STU     <$9E            
D000: BD D4 AE       JSR     $D4AE                          ; Clear 1200 bytes (4K for 3K screen??)
D003: 8E D2 A1       LDX     #$D2A1          
D006: EC 81          LDD     ,X++            
D008: 27 FE          BEQ     $D008                          ; 
D00A: DD AB          STD     <$AB            
D00C: A6 80          LDA     ,X+             
D00E: 97 AD          STA     <$AD            
D010: BD D6 FA       JSR     $D6FA                          ; 
D013: 20 F1          BRA     $D006                          ; 

; Hold something down at start for something? Graphics??
D015: 86 FE          LDA     #$FE            
D017: C6 08          LDB     #$08                           ; Column 4 
D019: B7 FF 02       STA     $FF02                          ; {hard:PIA0_DB} 
D01C: B6 FF 00       LDA     $FF00                          ; {hard:PIA0_DA} 
D01F: 84 40          ANDA    #$40                           ; Row 7
D021: 26 02          BNE     $D025                          ; 
D023: C6 10          LDB     #$10
            
D025: D7 C5          STB     <$C5            
D027: BD D2 DE       JSR     $D2DE                          ; 
D02A: CE 04 00       LDU     #$0400          
D02D: BD D4 AE       JSR     $D4AE                          ; 
D030: 8E CF DE       LDX     #$CFDE          
D033: 9F 72          STX     <$72            
D035: 86 55          LDA     #$55            
D037: 97 71          STA     <$71            
D039: 1A 50          ORCC    #$50            
D03B: 8E D5 46       LDX     #$D546          
D03E: BF 01 0D       STX     $010D                          ; New IRQ interrupt vector
D041: 0F C7          CLR     <$C7                           ; {ram:VisiblePage} 
D043: 86 04          LDA     #$04                           ; Display graphics page 400
D045: 97 92          STA     <$92                           ; {ram:RequestedPage} CURRENT VISIBILE PAGE
D047: 0F B6          CLR     <$B6            
D049: 0F C1          CLR     <$C1            
D04B: 86 34          LDA     #$34            
D04D: B7 FF 01       STA     $FF01                          ; {hard:PIA0_CA} 
D050: B7 FF 21       STA     $FF21                          ; {hard:PIA1_CA} 
D053: 8A 08          ORA     #$08            
D055: A7 8D 2E CA    STA     $2ECA,PC        
D059: 86 35          LDA     #$35            
D05B: B7 FF 03       STA     $FF03                          ; {hard:PIA0_CB} 
D05E: 3C EF          CWAI    $EF             
D060: 10 CE 03 F0    LDS     #$03F0          
D064: 0F C1          CLR     <$C1            
D066: 0F B1          CLR     <$B1            
D068: 0F B2          CLR     <$B2            
D06A: 0F B9          CLR     <$B9            
D06C: 0F B8          CLR     <$B8            
D06E: 0F B7          CLR     <$B7            
D070: 0F B6          CLR     <$B6            
D072: 0F C6          CLR     <$C6            
D074: 96 C5          LDA     <$C5            
D076: 97 A0          STA     <$A0            
D078: CE 10 00       LDU     #$1000          
D07B: DF 9C          STU     <$9C            
D07D: CC 1C 00       LDD     #$1C00          
D080: DD 9A          STD     <$9A            
D082: BD DB 6D       JSR     $DB6D                          ; 
D085: CE 04 00       LDU     #$0400          
D088: BD D4 AE       JSR     $D4AE                          ; 
D08B: 8E D5 EF       LDX     #$D5EF          
D08E: EC 81          LDD     ,X++            
D090: 27 10          BEQ     $D0A2                          ; 
D092: DD AB          STD     <$AB            
D094: A6 80          LDA     ,X+             
D096: 97 AD          STA     <$AD            
D098: CC 04 00       LDD     #$0400          
D09B: DD 9E          STD     <$9E            
D09D: BD D6 FA       JSR     $D6FA                          ; 
D0A0: 20 EC          BRA     $D08E                          ; 
D0A2: 86 01          LDA     #$01            
D0A4: BD DE 01       JSR     $DE01                          ; 
D0A7: 86 FF          LDA     #$FF            
D0A9: 97 AD          STA     <$AD            
D0AB: CE CC 90       LDU     #$CC90          
D0AE: C6 27          LDB     #$27            
D0B0: D7 98          STB     <$98            
D0B2: BD D5 01       JSR     $D501                          ; 
D0B5: 25 1D          BCS     $D0D4                          ; 
D0B7: EC C4          LDD     ,U              
D0B9: 27 10          BEQ     $D0CB                          ; 
D0BB: 8E D5 EF       LDX     #$D5EF          
D0BE: DC 9A          LDD     <$9A            
D0C0: DD 9E          STD     <$9E            
D0C2: EC 81          LDD     ,X++            
D0C4: DD AB          STD     <$AB            
D0C6: 30 01          LEAX    1,X             
D0C8: BD D6 F4       JSR     $D6F4                          ; 
D0CB: BD D7 3F       JSR     $D73F                          ; 
D0CE: 0A 98          DEC     <$98            
D0D0: 26 E0          BNE     $D0B2                          ; 
D0D2: 20 52          BRA     $D126                          ; 
D0D4: 86 FF          LDA     #$FF            
D0D6: 97 B5          STA     <$B5            
D0D8: BD DB 6D       JSR     $DB6D                          ; 
D0DB: 4F             CLRA                    
D0DC: 5F             CLRB                    
D0DD: DD AF          STD     <$AF            
D0DF: DD B1          STD     <$B1            
D0E1: CE 04 00       LDU     #$0400          
D0E4: BD D4 AE       JSR     $D4AE                          ; Clear 1200 bytes at
D0E7: CC 05 21       LDD     #$0521          
D0EA: DD AB          STD     <$AB            
D0EC: CC 04 00       LDD     #$0400          
D0EF: DD 9E          STD     <$9E            
D0F1: 86 AA          LDA     #$AA            
D0F3: 97 AD          STA     <$AD            
D0F5: 8E D5 E8       LDX     #$D5E8          
D0F8: BD D6 FA       JSR     $D6FA                          ; 
D0FB: 96 AF          LDA     <$AF            
D0FD: BD D6 D7       JSR     $D6D7                          ; 
D100: 86 42          LDA     #$42            
D102: BD D6 79       JSR     $D679                          ; 
D105: 96 AC          LDA     <$AC            
D107: 8B 06          ADDA    #$06            
D109: 97 AC          STA     <$AC            
D10B: 96 B0          LDA     <$B0            
D10D: BD D6 D7       JSR     $D6D7                          ; 
D110: CC 54 21       LDD     #$5421          
D113: DD AB          STD     <$AB            
D115: 8E D5 E0       LDX     #$D5E0          
D118: BD D6 FA       JSR     $D6FA                          ; 
D11B: 9E B1          LDX     <$B1            
D11D: BD D6 CB       JSR     $D6CB                          ; 
D120: 86 C0          LDA     #$C0            
D122: 97 C0          STA     <$C0            
D124: 20 38          BRA     $D15E                          ; 
D126: 0F B5          CLR     <$B5            
D128: BD DB 6D       JSR     $DB6D                          ; 
D12B: 8E 08 34       LDX     #$0834          
D12E: 9F C3          STX     <$C3            
D130: CE 04 00       LDU     #$0400          
D133: BD D4 AE       JSR     $D4AE                          ; 
D136: 86 AA          LDA     #$AA            
D138: 97 AD          STA     <$AD            
D13A: CC 04 13       LDD     #$0413          
D13D: DD AB          STD     <$AB            
D13F: CC 04 00       LDD     #$0400          
D142: DD 9E          STD     <$9E            
D144: 8E D5 C2       LDX     #$D5C2          
D147: BD D6 FA       JSR     $D6FA                          ; 
D14A: 9E B3          LDX     <$B3            
D14C: BD D6 CB       JSR     $D6CB                          ; 
D14F: CC 54 04       LDD     #$5404          
D152: DD AB          STD     <$AB            
D154: 8E D5 CE       LDX     #$D5CE          
D157: BD D6 FA       JSR     $D6FA                          ; 
D15A: 86 C0          LDA     #$C0            
D15C: 97 C0          STA     <$C0            
D15E: BD DB 6D       JSR     $DB6D                          ; 
D161: 0F B6          CLR     <$B6            
D163: 0F B7          CLR     <$B7            
D165: 86 31          LDA     #$31            
D167: C6 41          LDB     #$41            
D169: DD A2          STD     <$A2            
D16B: 0F A4          CLR     <$A4            
D16D: BD D4 BD       JSR     $D4BD                          ; 
D170: BD DC 56       JSR     $DC56                          ; 
D173: 0F BA          CLR     <$BA            
D175: 8E 06 00       LDX     #$0600          
D178: CE 04 00       LDU     #$0400          
D17B: EC C4          LDD     ,U              
D17D: ED C9 0C 00    STD     $0C00,U         
D181: ED C9 18 00    STD     $1800,U         
D185: 33 42          LEAU    2,U             
D187: 30 1F          LEAX    -1,X            
D189: 26 F0          BNE     $D17B                          ; 
D18B: 0F A1          CLR     <$A1            
D18D: 0D B5          TST     <$B5            
D18F: 27 1F          BEQ     $D1B0                          ; 
D191: C6 13          LDB     #$13            
D193: 0D C6          TST     <$C6            
D195: 26 02          BNE     $D199                          ; 
D197: C6 27          LDB     #$27            
D199: D7 98          STB     <$98            
D19B: CE CC 90       LDU     #$CC90          
D19E: BD D7 3F       JSR     $D73F                          ; 
D1A1: 8E 12 00       LDX     #$1200          
D1A4: 30 1F          LEAX    -1,X            
D1A6: 26 FC          BNE     $D1A4                          ; 
D1A8: 0A 98          DEC     <$98            
D1AA: 26 F2          BNE     $D19E                          ; 
D1AC: 86 FF          LDA     #$FF            
D1AE: 97 C6          STA     <$C6            
D1B0: BD DA 33       JSR     $DA33                          ; 
D1B3: BD D4 A2       JSR     $D4A2                          ; 
D1B6: 97 92          STA     <$92                           ; {ram:RequestedPage} 
D1B8: 86 0F          LDA     #$0F            
D1BA: 13             SYNC                    
D1BB: 4A             DECA                    
D1BC: 26 FC          BNE     $D1BA                          ; 
D1BE: 86 FF          LDA     #$FF            
D1C0: 97 C1          STA     <$C1            
D1C2: BD DF 70       JSR     $DF70                          ; 
D1C5: BD DB 1F       JSR     $DB1F                          ; 
D1C8: 03 A1          COM     <$A1            
D1CA: 2A 03          BPL     $D1CF                          ; 
D1CC: BD DE 7A       JSR     $DE7A                          ; 
D1CF: BD DF 68       JSR     $DF68                          ; 
D1D2: BD D9 35       JSR     $D935                          ; 
D1D5: DC BE          LDD     <$BE            
D1D7: 10 27 01 69    LBEQ    $0169           
D1DB: 96 B8          LDA     <$B8            
D1DD: 94 B5          ANDA    <$B5            
D1DF: 27 25          BEQ     $D206                          ; 
D1E1: 86 AA          LDA     #$AA            
D1E3: 97 AD          STA     <$AD            
D1E5: CC 54 4B       LDD     #$544B          
D1E8: DD AB          STD     <$AB            
D1EA: DC 9A          LDD     <$9A            
D1EC: DD 9E          STD     <$9E            
D1EE: 9E B1          LDX     <$B1            
D1F0: BD D6 CB       JSR     $D6CB                          ; 
D1F3: 0A B8          DEC     <$B8            
D1F5: 27 0F          BEQ     $D206                          ; 
D1F7: CC 54 4B       LDD     #$544B          
D1FA: DD AB          STD     <$AB            
D1FC: CC 04 00       LDD     #$0400          
D1FF: DD 9E          STD     <$9E            
D201: 9E B1          LDX     <$B1            
D203: BD D6 CB       JSR     $D6CB                          ; 
D206: 96 B9          LDA     <$B9            
D208: 94 B5          ANDA    <$B5            
D20A: 27 3B          BEQ     $D247                          ; 
D20C: 86 AA          LDA     #$AA            
D20E: 97 AD          STA     <$AD            
D210: CC 05 45       LDD     #$0545          
D213: DD AB          STD     <$AB            
D215: DC 9A          LDD     <$9A            
D217: DD 9E          STD     <$9E            
D219: 96 AF          LDA     <$AF            
D21B: BD D6 D7       JSR     $D6D7                          ; 
D21E: 96 AC          LDA     <$AC            
D220: 8B 06          ADDA    #$06            
D222: 97 AC          STA     <$AC            
D224: 96 B0          LDA     <$B0            
D226: BD D6 D7       JSR     $D6D7                          ; 
D229: 0A B9          DEC     <$B9            
D22B: 27 1A          BEQ     $D247                          ; 
D22D: CC 05 45       LDD     #$0545          
D230: DD AB          STD     <$AB            
D232: CC 04 00       LDD     #$0400          
D235: DD 9E          STD     <$9E            
D237: 96 AF          LDA     <$AF            
D239: BD D6 D7       JSR     $D6D7                          ; 
D23C: 96 AC          LDA     <$AC            
D23E: 8B 06          ADDA    #$06            
D240: 97 AC          STA     <$AC            
D242: 96 B0          LDA     <$B0            
D244: BD D6 D7       JSR     $D6D7                          ; 
D247: BD DA 33       JSR     $DA33                          ; 
D24A: 0D BA          TST     <$BA            
D24C: 27 02          BEQ     $D250                          ; 
D24E: 0A BA          DEC     <$BA            
D250: BD D7 D8       JSR     $D7D8                          ; 
D253: BD D8 20       JSR     $D820                          ; 
D256: BD D4 A2       JSR     $D4A2                          ; 
D259: 97 92          STA     <$92                           ; {ram:RequestedPage} 
D25B: 13             SYNC                    
D25C: DC A2          LDD     <$A2            
D25E: DD 8E          STD     <$8E            
D260: BD DF CC       JSR     $DFCC                          ; 
D263: 10 25 00 8C    LBCS    $008C           
D267: 0D B5          TST     <$B5            
D269: 27 1F          BEQ     $D28A                          ; 
D26B: AD 9F A0 00    JSR     [$A000]                        ; {hard:POLCAT} 
D26F: 81 03          CMPA    #$03            
D271: 10 27 FD EB    LBEQ    $FDEB           
D275: 81 0D          CMPA    #$0D            
D277: 10 26 FF 47    LBNE    $FF47           
D27B: 1A 50          ORCC    #$50            
D27D: AD 9F A0 00    JSR     [$A000]                        ; {hard:POLCAT} 
D281: 81 0D          CMPA    #$0D            
D283: 26 F8          BNE     $D27D                          ; 
D285: 1C EF          ANDCC   #$EF            
D287: 7E D1 C2       JMP     $D1C2                          ; 
D28A: BD D5 01       JSR     $D501                          ; 
D28D: 10 25 FE 43    LBCS    $FE43           
D291: 8E 08 00       LDX     #$0800          
D294: 30 1F          LEAX    -1,X            
D296: 26 FC          BNE     $D294                          ; 
D298: 9E C3          LDX     <$C3            
D29A: 10 27 FD C2    LBEQ    $FDC2           
D29E: 7E D1 C2       JMP     $D1C2                          ;
 
D2A1: 0A 01          DEC     <$01            
D2A3: AA 31          ORA     -15,Y           
D2A5: 36 6B          PSHU    S,Y,DP,A,CC     
D2A7: 20 6F          BRA     $D318                          ; 
D2A9: 72                                  
D2AA: 20 6D          BRA     $D319                          ; 
D2AC: 6F 72          CLR     -14,S           
D2AE: 65                                  
D2AF: 20 6F          BRA     $D320                          ; 
D2B1: 66 20          ROR     0,Y             
D2B3: 6D 65          TST     5,S             
D2B5: 6D 6F          TST     15,S            
D2B7: 72                                  
D2B8: 79 00 1E       ROL     $001E           
D2BB: 0D 55          TST     <$55            
D2BD: 69 
D2BE: 73          ROL     -13,S           
D2BF: 20 6E          BRA     $D32F                          ; 
D2C1: 65                                  
D2C2: 65                                  
D2C3: 64 65          LSR     5,S             
D2C5: 64 20          LSR     0,Y             
D2C7: 74 6F 20       LSR     $6F20           
D2CA: 70 6C 61       NEG     $6C61           
D2CD: 79 00 32       ROL     $0032           
D2D0: 2A FF          BPL     $D2D1                          ; 
D2D2: 4D             TSTA                    
D2D3: 65                                  
D2D4: 67 61          ASR     1,S             
D2D6: 22 42          BHI     $D31A                          ; 
D2D8: 75                                  
D2D9: 67 00          ASR     0,X             
D2DB: 00 00          NEG     <$00            
D2DD: 00 B7          NEG     <$B7            
D2DF: FF C0 B7       STU     $C0B7                          ; 
D2E2: FF C2 B7       STU     $C2B7                          ; 
D2E5: FF C5 B7       STU     $C5B7                          ; 
D2E8: FF C7 B7       STU     $C7B7                          ; 
D2EB: FF C8 86       STU     $C886                          ; 
D2EE: FF B7 FF       STU     $B7FF           
D2F1: 22 39          BHI     $D32C                          ; 
D2F3: 0F C1          CLR     <$C1            
D2F5: BD D7 A7       JSR     $D7A7                          ; 
D2F8: 0D B5          TST     <$B5            
D2FA: 10 27 FD 62    LBEQ    $FD62           
D2FE: DC B1          LDD     <$B1            
D300: 10 93 B3       CMPD    <$B3            
D303: 25 02          BCS     $D307                          ; 
D305: DD B3          STD     <$B3            
D307: BD D7 7C       JSR     $D77C                          ; 
D30A: 86 04          LDA     #$04            
D30C: 97 92          STA     <$92                           ; {ram:RequestedPage} 
D30E: 86 0E          LDA     #$0E            
D310: 97 98          STA     <$98            
D312: CE CB 50       LDU     #$CB50          
D315: 96 98          LDA     <$98            
D317: 84 01          ANDA    #$01            
D319: 27 03          BEQ     $D31E                          ; 
D31B: CE CB F0       LDU     #$CBF0          
D31E: BD D4 81       JSR     $D481                          ; 
D321: 86 0A          LDA     #$0A            
D323: 13             SYNC                    
D324: 4A             DECA                    
D325: 26 FC          BNE     $D323                          ; 
D327: 0A 98          DEC     <$98            
D329: 26 E7          BNE     $D312                          ; 
D32B: CE CA B0       LDU     #$CAB0          
D32E: BD D4 81       JSR     $D481                          ; 
D331: 8E 01 2C       LDX     #$012C          
D334: 9F C3          STX     <$C3            
D336: BD D5 01       JSR     $D501                          ; 
D339: 10 25 FD 97    LBCS    $FD97           
D33D: 9E C3          LDX     <$C3            
D33F: 26 F5          BNE     $D336                          ; 
D341: 7E D0 60       JMP     $D060                          ; 
D344: 0F C1          CLR     <$C1            
D346: BD DA 33       JSR     $DA33                          ; 
D349: BD DA 33       JSR     $DA33                          ; 
D34C: BD DA 33       JSR     $DA33                          ; 
D34F: 86 04          LDA     #$04            
D351: 97 92          STA     <$92                           ; {ram:RequestedPage} 
D353: 13             SYNC                    
D354: 8E 06 00       LDX     #$0600          
D357: CE 04 00       LDU     #$0400          
D35A: EC C1          LDD     ,U++            
D35C: ED C9 0B FE    STD     $0BFE,U         
D360: ED C9 17 FE    STD     $17FE,U         
D364: 30 1F          LEAX    -1,X            
D366: 26 F2          BNE     $D35A                          ; 
D368: 86 02          LDA     #$02            
D36A: 97 98          STA     <$98            
D36C: 86 AA          LDA     #$AA            
D36E: 97 AD          STA     <$AD            
D370: 86 C0          LDA     #$C0            
D372: 97 88          STA     <$88            
D374: DE 9A          LDU     <$9A            
D376: 33 C9 01 C5    LEAU    $01C5,U         
D37A: 8E 05 C5       LDX     #$05C5          
D37D: 96 88          LDA     <$88            
D37F: 94 AD          ANDA    <$AD            
D381: 97 89          STA     <$89            
D383: 86 43          LDA     #$43            
D385: 97 99          STA     <$99            
D387: C6 16          LDB     #$16            
D389: A6 80          LDA     ,X+             
D38B: 88 55          EORA    #$55            
D38D: 94 88          ANDA    <$88            
D38F: 26 06          BNE     $D397                          ; 
D391: 96 89          LDA     <$89            
D393: A8 C4          EORA    ,U              
D395: A7 C4          STA     ,U              
D397: 33 41          LEAU    1,U             
D399: 5A             DECB                    
D39A: 26 ED          BNE     $D389                          ; 
D39C: 30 0A          LEAX    10,X            
D39E: 33 4A          LEAU    10,U            
D3A0: 0A 99          DEC     <$99            
D3A2: 26 E3          BNE     $D387                          ; 
D3A4: 04 88          LSR     <$88            
D3A6: 04 88          LSR     <$88            
D3A8: 26 CA          BNE     $D374                          ; 
D3AA: BD D4 A2       JSR     $D4A2                          ; 
D3AD: 96 AD          LDA     <$AD            
D3AF: 8B 55          ADDA    #$55            
D3B1: 97 AD          STA     <$AD            
D3B3: 0A 98          DEC     <$98            
D3B5: 26 B9          BNE     $D370                          ; 
D3B7: 86 04          LDA     #$04            
D3B9: 97 A5          STA     <$A5            
D3BB: C6 28          LDB     #$28            
D3BD: 96 A5          LDA     <$A5            
D3BF: 8B 0C          ADDA    #$0C            
D3C1: 81 28          CMPA    #$28            
D3C3: 25 02          BCS     $D3C7                          ; 
D3C5: 86 04          LDA     #$04            
D3C7: 97 A5          STA     <$A5            
D3C9: 97 92          STA     <$92                           ; {ram:RequestedPage} 
D3CB: 86 06          LDA     #$06            
D3CD: 13             SYNC                    
D3CE: 4A             DECA                    
D3CF: 26 FC          BNE     $D3CD                          ; 
D3D1: 5A             DECB                    
D3D2: 26 E9          BNE     $D3BD                          ; 
D3D4: 86 04          LDA     #$04            
D3D6: 97 92          STA     <$92                           ; {ram:RequestedPage} 
D3D8: 13             SYNC                    
D3D9: BD DB 6D       JSR     $DB6D                          ; 
D3DC: CE 04 00       LDU     #$0400          
D3DF: BD D4 AE       JSR     $D4AE                          ; 
D3E2: 86 01          LDA     #$01            
D3E4: BD DE 01       JSR     $DE01                          ; 
D3E7: 04 C0          LSR     <$C0            
D3E9: 96 A0          LDA     <$A0            
D3EB: 4C             INCA                    
D3EC: 81 20          CMPA    #$20            
D3EE: 24 02          BCC     $D3F2                          ; 
D3F0: 97 A0          STA     <$A0            
D3F2: CE 10 00       LDU     #$1000          
D3F5: DF 9E          STU     <$9E            
D3F7: BD D4 AE       JSR     $D4AE                          ; 
D3FA: 8E D6 5A       LDX     #$D65A          
D3FD: EC 81          LDD     ,X++            
D3FF: DD AB          STD     <$AB            
D401: 27 09          BEQ     $D40C                          ; 
D403: A6 80          LDA     ,X+             
D405: 97 AD          STA     <$AD            
D407: BD D6 FA       JSR     $D6FA                          ; 
D40A: 20 F1          BRA     $D3FD                          ; 
D40C: 86 01          LDA     #$01            
D40E: 97 98          STA     <$98            
D410: 8E C0 00       LDX     #$C000          
D413: 9F A5          STX     <$A5            
D415: 86 06          LDA     #$06            
D417: 8D 4E          BSR     $D467                          ; 
D419: 8D 51          BSR     $D46C                          ; 
D41B: 96 98          LDA     <$98            
D41D: 8B 02          ADDA    #$02            
D41F: 97 98          STA     <$98            
D421: 81 59          CMPA    #$59            
D423: 24 0A          BCC     $D42F                          ; 
D425: BD DB B1       JSR     $DBB1                          ; 
D428: 03 A1          COM     <$A1            
D42A: BD D5 27       JSR     $D527                          ; 
D42D: 20 E6          BRA     $D415                          ; 
D42F: 0F 98          CLR     <$98            
D431: CC 28 5D       LDD     #$285D          
D434: DD AB          STD     <$AB            
D436: 86 FF          LDA     #$FF            
D438: 97 AD          STA     <$AD            
D43A: 86 3F          LDA     #$3F            
D43C: BD D6 79       JSR     $D679                          ; 
D43F: 86 2D          LDA     #$2D            
D441: BD D4 67       JSR     $D467                          ; 
D444: 86 02          LDA     #$02            
D446: 8D 1F          BSR     $D467                          ; 
D448: BD DB DD       JSR     $DBDD                          ; 
D44B: 96 98          LDA     <$98            
D44D: 8B 02          ADDA    #$02            
D44F: 97 98          STA     <$98            
D451: 81 58          CMPA    #$58            
D453: 24 0A          BCC     $D45F                          ; 
D455: BD DB E0       JSR     $DBE0                          ; 
D458: 03 A1          COM     <$A1            
D45A: BD D5 27       JSR     $D527                          ; 
D45D: 20 E5          BRA     $D444                          ; 
D45F: 86 64          LDA     #$64            
D461: BD D4 67       JSR     $D467                          ; 
D464: 7E D0 E7       JMP     $D0E7                          ; 
D467: 13             SYNC                    
D468: 4A             DECA                    
D469: 26 FC          BNE     $D467                          ; 
D46B: 39             RTS                     
D46C: 9E A5          LDX     <$A5            
D46E: C6 80          LDB     #$80            
D470: 6F 82          CLR     ,-X             
D472: 5A             DECB                    
D473: 26 FB          BNE     $D470                          ; 
D475: C6 40          LDB     #$40            
D477: A6 89 F3 FF    LDA     $F3FF,X         
D47B: A7 82          STA     ,-X             
D47D: 5A             DECB                    
D47E: 26 F7          BNE     $D477                          ; 
D480: 39             RTS                     
D481: 8E 08 00       LDX     #$0800          
D484: 86 05          LDA     #$05            
D486: 97 99          STA     <$99            
D488: C6 20          LDB     #$20            
D48A: 34 10          PSHS    X               
D48C: A6 C0          LDA     ,U+             
D48E: A7 88 1B       STA     $1B,X           
D491: A7 84          STA     ,X              
D493: 30 88 20       LEAX    $20,X           
D496: 5A             DECB                    
D497: 26 F3          BNE     $D48C                          ; 
D499: 35 10          PULS    X               
D49B: 30 01          LEAX    1,X             
D49D: 0A 99          DEC     <$99            
D49F: 26 E7          BNE     $D488                          ; 
D4A1: 39             RTS                     
D4A2: 34 10          PSHS    X               
D4A4: DC 9A          LDD     <$9A            
D4A6: 9E 9C          LDX     <$9C            
D4A8: DD 9C          STD     <$9C            
D4AA: 9F 9A          STX     <$9A            
D4AC: 35 90          PULS    X,PC            
D4AE: 34 10          PSHS    X               
D4B0: 8E 06 00       LDX     #$0600          
D4B3: 4F             CLRA                    
D4B4: 5F             CLRB                    
D4B5: ED C1          STD     ,U++            
D4B7: 30 1F          LEAX    -1,X            
D4B9: 26 FA          BNE     $D4B5                          ; 
D4BB: 35 90          PULS    X,PC            
D4BD: 8E 28 08       LDX     #$2808          
D4C0: 96 A0          LDA     <$A0            
D4C2: 97 98          STA     <$98            
D4C4: BD DD 52       JSR     $DD52                          ; 
D4C7: 84 7C          ANDA    #$7C            
D4C9: 81 40          CMPA    #$40            
D4CB: 24 F7          BCC     $D4C4                          ; 
D4CD: 8B 11          ADDA    #$11            
D4CF: A7 88 60       STA     $60,X           
D4D2: A7 84          STA     ,X              
D4D4: BD DD 52       JSR     $DD52                          ; 
D4D7: 84 7C          ANDA    #$7C            
D4D9: 81 50          CMPA    #$50            
D4DB: 24 F7          BCC     $D4D4                          ; 
D4DD: 8B 19          ADDA    #$19            
D4DF: A7 88 61       STA     $61,X           
D4E2: A7 01          STA     1,X             
D4E4: EC 84          LDD     ,X              
D4E6: 90 A2          SUBA    <$A2            
D4E8: 2A 01          BPL     $D4EB                          ; 
D4EA: 40             NEGA                    
D4EB: 81 0A          CMPA    #$0A            
D4ED: 25 D5          BCS     $D4C4                          ; 
D4EF: D0 A3          SUBB    <$A3            
D4F1: 2A 01          BPL     $D4F4                          ; 
D4F3: 50             NEGB                    
D4F4: C1 0A          CMPB    #$0A            
D4F6: 25 CC          BCS     $D4C4                          ; 
D4F8: 6F 02          CLR     2,X             
D4FA: 30 03          LEAX    3,X             
D4FC: 0A 98          DEC     <$98            
D4FE: 26 C4          BNE     $D4C4                          ; 
D500: 39             RTS                     
D501: 86 FF          LDA     #$FF            
D503: B7 FF 02       STA     $FF02                          ; {hard:PIA0_DB} 
D506: F6 FF 00       LDB     $FF00                          ; {hard:PIA0_DA} 
D509: C4 01          ANDB    #$01            
D50B: 26 05          BNE     $D512                          ; 
D50D: 97 C2          STA     <$C2            
D50F: 1A 01          ORCC    #$01            
D511: 39             RTS                     
D512: 86 7F          LDA     #$7F            
D514: B7 FF 02       STA     $FF02                          ; {hard:PIA0_DB} 
D517: A6 8D 29 E5    LDA     $29E5,PC        
D51B: 84 08          ANDA    #$08            
D51D: 26 05          BNE     $D524                          ; 
D51F: 0F C2          CLR     <$C2            
D521: 1A 01          ORCC    #$01            
D523: 39             RTS                     
D524: 1C FE          ANDCC   #$FE            
D526: 39             RTS                     
D527: 86 02          LDA     #$02            
D529: B7 FF 20       STA     $FF20                          ; {hard:PIA1_DA} 
D52C: C6 23          LDB     #$23            
D52E: 1F 98          TFR     B,A             
D530: 4A             DECA                    
D531: 26 FD          BNE     $D530                          ; 
D533: B6 FF 20       LDA     $FF20                          ; {hard:PIA1_DA} 
D536: 88 40          EORA    #$40            
D538: B7 FF 20       STA     $FF20                          ; {hard:PIA1_DA} 
D53B: 5C             INCB                    
D53C: C1 41          CMPB    #$41            
D53E: 25 EE          BCS     $D52E                          ; 
D540: 86 02          LDA     #$02            
D542: B7 FF 20       STA     $FF20                          ; {hard:PIA1_DA} 
D545: 39             RTS
```

# IRQ Service Routine

```code
IRQ:
; Set the desired display page                 
D546: 96 92          LDA     <$92                           ; {ram:RequestedPage} Desired page (256-byte boundary)
D548: 91 C7          CMPA    <$C7                           ; {ram:VisiblePage} Already set?
D54A: 27 16          BEQ     $D562                          ; Yes ... nothing to do
D54C: 97 C7          STA     <$C7                           ; {ram:VisiblePage} This is the new set page
D54E: 44             LSRA                                   ; Offset is 512 byte boundary ... ignore the LSB
D54F: C6 05          LDB     #$05                           ; 6 registers (bits) to poke
D551: 8E FF C6       LDX     #$FFC6                         ; Display offset
D554: 44             LSRA                                   ; Is this bit a 0?
D555: 24 06          BCC     $D55D                          ; Yes ... go clear it
D557: 30 01          LEAX    1,X                            ; Next register is the 1 register
D559: A7 80          STA     ,X+                            ; Write a 1
D55B: 20 02          BRA     $D55F                          ; Next bit
D55D: A7 81          STA     ,X++                           ; Write a 0
D55F: 5A             DECB                                   ; All bits done?
D560: 26 F2          BNE     $D554                          ; No ... set all 5 bits

D562: 96 C1          LDA     <$C1            
D564: 94 B5          ANDA    <$B5            
D566: 27 48          BEQ     $D5B0                          ; 
D568: 96 B6          LDA     <$B6            
D56A: 4C             INCA                    
D56B: 97 B6          STA     <$B6            
D56D: 81 3C          CMPA    #$3C            
D56F: 25 1C          BCS     $D58D                          ; 
D571: 0F B6          CLR     <$B6            
D573: DC B1          LDD     <$B1            
D575: 27 16          BEQ     $D58D                          ; 
D577: 86 02          LDA     #$02            
D579: 97 B8          STA     <$B8            
D57B: 96 B2          LDA     <$B2            
D57D: 8B 99          ADDA    #$99            
D57F: 19             DAA                     
D580: 97 B2          STA     <$B2            
D582: 81 99          CMPA    #$99            
D584: 26 07          BNE     $D58D                          ; 
D586: 96 B1          LDA     <$B1            
D588: 8B 99          ADDA    #$99            
D58A: 19             DAA                     
D58B: 97 B1          STA     <$B1            
D58D: 96 B7          LDA     <$B7            
D58F: 4C             INCA                    
D590: 97 B7          STA     <$B7            
D592: 81 3C          CMPA    #$3C            
D594: 25 1A          BCS     $D5B0                          ; 
D596: 0F B7          CLR     <$B7            
D598: 86 02          LDA     #$02            
D59A: 97 B9          STA     <$B9            
D59C: 96 B0          LDA     <$B0            
D59E: 8B 01          ADDA    #$01            
D5A0: 19             DAA                     
D5A1: 97 B0          STA     <$B0            
D5A3: 81 60          CMPA    #$60            
D5A5: 25 09          BCS     $D5B0                          ; 
D5A7: 0F B0          CLR     <$B0            
D5A9: 96 AF          LDA     <$AF            
D5AB: 8B 01          ADDA    #$01            
D5AD: 19             DAA                     
D5AE: 97 AF          STA     <$AF            
D5B0: 9E C3          LDX     <$C3            
D5B2: 27 04          BEQ     $D5B8                          ; 
D5B4: 30 1F          LEAX    -1,X            
D5B6: 9F C3          STX     <$C3            
D5B8: B6 FF 03       LDA     $FF03                          ; {hard:PIA0_CB} 
D5BB: B6 FF 02       LDA     $FF02                          ; {hard:PIA0_DB} 
D5BE: BD DD 52       JSR     $DD52                          ; 
D5C1: 3B             RTI                     

D5C2: 48             LSLA                    
D5C3: 69 67          ROL     7,S             
D5C5: 68 20          ASL     0,Y             
D5C7: 53             COMB                    
D5C8: 63 6F          COM     15,S            
D5CA: 72                                  
D5CB: 65                                  
D5CC: 20 00          BRA     $D5CE                          ; 
D5CE: 20 20          BRA     $D5F0                          ; 
D5D0: 20 50          BRA     $D622                          ; 
D5D2: 6C 61          INC     1,S             
D5D4: 79 20 20       ROL     $2020           
D5D7: 4D             TSTA                    
D5D8: 65                                  
D5D9: 67 61          ASR     1,S             
D5DB: 22 42          BHI     $D61F                          ; 
D5DD: 75                                  
D5DE: 67 00          ASR     0,X             
D5E0: 53             COMB                    
D5E1: 63 6F          COM     15,S            
D5E3: 72                                  
D5E4: 65                                  
D5E5: 24 20          BCC     $D607                          ; 
D5E7: 00 54          NEG     <$54            
D5E9: 69 6D          ROL     13,S            
D5EB: 65                                  
D5EC: 24 20          BCC     $D60E                          ; 
D5EE: 00 07          NEG     <$07            
D5F0: 2A FF          BPL     $D5F1                          ; 
D5F2: 4D             TSTA                    
D5F3: 65                                  
D5F4: 67 61          ASR     1,S             
D5F6: 22 42          BHI     $D63A                          ; 
D5F8: 75                                  
D5F9: 67 00          ASR     0,X             
D5FB: 17 3C 55       LBSR    $3C55           
D5FE: 42                                  
D5FF: 79 00 21       ROL     $0021           
D602: 21 55          BRN     $D659                          ; 
D604: 53             COMB                    
D605: 74 65 76       LSR     $6576           
D608: 65                                  
D609: 20 42          BRA     $D64D                          ; 
D60B: 6A 6F          DEC     15,S            
D60D: 72                                  
D60E: 6B                                  
D60F: 00 31          NEG     <$31            
D611: 18                                  
D612: AA 43          ORA     3,U             
D614: 6F 70          CLR     -16,S           
D616: 79 72 69       ROL     $7269           
D619: 67 68          ASR     8,S             
D61B: 74 20 31       LSR     $2031           
D61E: 39             RTS                     
D61F: 38                                  
D620: 32 00          LEAS    0,X             
D622: 3B             RTI                     
D623: 1B                                  
D624: AA 44          ORA     4,U             
D626: 61                                  
D627: 74 61 73       LSR     $6173           
D62A: 6F 66          CLR     6,S             
D62C: 74 20 49       LSR     $2049           
D62F: 6E 63          JMP     3,S             
D631: 23 00          BLS     $D633                          ; 
D633: 4B                                  
D634: 1E 55          EXG     $55             
D636: 4C             INCA                    
D637: 69 63          ROL     3,S             
D639: 65                                  
D63A: 6E 73          JMP     -13,S           
D63C: 65                                  
D63D: 64 20          LSR     0,Y             
D63F: 74 6F 00       LSR     $6F00           
D642: 55                                  
D643: 0C 55          INC     <$55            
D645: 54             LSRB                    
D646: 61                                  
D647: 6E 64          JMP     4,S             
D649: 79 20 43       ROL     $2043           
D64C: 6F 72          CLR     -14,S           
D64E: 70 6F 72       NEG     $6F72           
D651: 61                                  
D652: 74 69 6F       LSR     $696F           
D655: 6E 00          JMP     0,X             
D657: 00 00          NEG     <$00            
D659: 00 1B          NEG     <$1B            
D65B: 1E 55          EXG     $55             
D65D: 57             ASRB                    
D65E: 65                                  
D65F: 25 6C          BCS     $D6CD                          ; 
D661: 6C 20          INC     0,Y             
D663: 47             ASRA                    
D664: 65                                  
D665: 74 63 68       LSR     $6368           
D668: 61                                  
D669: 00 28          NEG     <$28            
D66B: 27 AA          BEQ     $D617                          ; 
D66D: 4E                                  
D66E: 65                                  
D66F: 78 74 20       LSL     $7420           
D672: 54             LSRB                    
D673: 69 6D          ROL     13,S            
D675: 65                                  
D676: 00 00          NEG     <$00            
D678: 00 34          NEG     <$34            
D67A: 40             NEGA                    
D67B: DE 90          LDU     <$90            
D67D: 6F C9 C0 00    CLR     $C000,U         
D681: CE CD 7A       LDU     #$CD7A          
D684: C6 09          LDB     #$09            
D686: 3D             MUL                     
D687: 33 CB          LEAU    D,U             
D689: DC AB          LDD     <$AB            
D68B: 9E 9E          LDX     <$9E            
D68D: BD DE 5F       JSR     $DE5F                          ; 
D690: 86 09          LDA     #$09            
D692: A7 E2          STA     ,-S             
D694: A6 C0          LDA     ,U+             
D696: 34 16          PSHS    X,B,A           
D698: D7 88          STB     <$88            
D69A: C6 06          LDB     #$06            
D69C: 96 88          LDA     <$88            
D69E: 43             COMA                    
D69F: A4 84          ANDA    ,X              
D6A1: 68 E4          ASL     ,S              
D6A3: 24 08          BCC     $D6AD                          ; 
D6A5: 34 02          PSHS    A               
D6A7: 96 88          LDA     <$88            
D6A9: 94 AD          ANDA    <$AD            
D6AB: AA E0          ORA     ,S+             
D6AD: A7 84          STA     ,X              
D6AF: 04 88          LSR     <$88            
D6B1: 04 88          LSR     <$88            
D6B3: 26 06          BNE     $D6BB                          ; 
D6B5: 30 01          LEAX    1,X             
D6B7: 86 C0          LDA     #$C0            
D6B9: 97 88          STA     <$88            
D6BB: 5A             DECB                    
D6BC: 26 DE          BNE     $D69C                          ; 
D6BE: 35 16          PULS    A,B,X           
D6C0: 30 88 20       LEAX    $20,X           
D6C3: 6A E4          DEC     ,S              
D6C5: 26 CD          BNE     $D694                          ; 
D6C7: 32 61          LEAS    1,S             
D6C9: 35 C0          PULS    U,PC            
D6CB: 86 AA          LDA     #$AA            
D6CD: 97 AD          STA     <$AD            
D6CF: 34 10          PSHS    X               
D6D1: 35 02          PULS    A               
D6D3: 8D 02          BSR     $D6D7                          ; 
D6D5: 35 02          PULS    A               
D6D7: 34 02          PSHS    A               
D6D9: 44             LSRA                    
D6DA: 44             LSRA                    
D6DB: 44             LSRA                    
D6DC: 44             LSRA                    
D6DD: BD D6 79       JSR     $D679                          ; 
D6E0: 35 02          PULS    A               
D6E2: D6 AC          LDB     <$AC            
D6E4: CB 06          ADDB    #$06            
D6E6: D7 AC          STB     <$AC            
D6E8: 84 0F          ANDA    #$0F            
D6EA: BD D6 79       JSR     $D679                          ; 
D6ED: D6 AC          LDB     <$AC            
D6EF: CB 06          ADDB    #$06            
D6F1: D7 AC          STB     <$AC            
D6F3: 39             RTS                     
D6F4: 0F AE          CLR     <$AE            
D6F6: 03 AE          COM     <$AE            
D6F8: 20 02          BRA     $D6FC                          ; 
D6FA: 0F AE          CLR     <$AE            
D6FC: A6 80          LDA     ,X+             
D6FE: 84 7F          ANDA    #$7F            
D700: 80 20          SUBA    #$20            
D702: 25 EF          BCS     $D6F3                          ; 
D704: 81 06          CMPA    #$06            
D706: 24 04          BCC     $D70C                          ; 
D708: 8B 3E          ADDA    #$3E            
D70A: 20 16          BRA     $D722                          ; 
D70C: 80 10          SUBA    #$10            
D70E: 25 E3          BCS     $D6F3                          ; 
D710: 81 0A          CMPA    #$0A            
D712: 25 0E          BCS     $D722                          ; 
D714: 80 07          SUBA    #$07            
D716: 25 DB          BCS     $D6F3                          ; 
D718: 81 24          CMPA    #$24            
D71A: 25 06          BCS     $D722                          ; 
D71C: 80 06          SUBA    #$06            
D71E: 81 3E          CMPA    #$3E            
D720: 24 D1          BCC     $D6F3                          ; 
D722: 34 10          PSHS    X               
D724: BD D6 79       JSR     $D679                          ; 
D727: 35 10          PULS    X               
D729: 96 AC          LDA     <$AC            
D72B: 8B 06          ADDA    #$06            
D72D: 97 AC          STA     <$AC            
D72F: 0D AE          TST     <$AE            
D731: 27 C9          BEQ     $D6FC                          ; 
D733: 96 AD          LDA     <$AD            
D735: 8B 55          ADDA    #$55            
D737: 24 02          BCC     $D73B                          ; 
D739: 86 55          LDA     #$55            
D73B: 97 AD          STA     <$AD            
D73D: 20 BD          BRA     $D6FC                          ; 
D73F: 34 01          PSHS    CC              
D741: 1A 50          ORCC    #$50            
D743: EC C4          LDD     ,U              
D745: 44             LSRA                    
D746: 56             RORB                    
D747: 44             LSRA                    
D748: 56             RORB                    
D749: 44             LSRA                    
D74A: 56             RORB                    
D74B: 34 06          PSHS    B,A             
D74D: EC C1          LDD     ,U++            
D74F: A3 E1          SUBD    ,S++            
D751: 1F 01          TFR     D,X             
D753: EC C1          LDD     ,U++            
D755: DD 80          STD     <$80            
D757: EC C1          LDD     ,U++            
D759: DD 82          STD     <$82            
D75B: 6F E4          CLR     ,S              
D75D: DC 86          LDD     <$86            
D75F: D3 82          ADDD    <$82            
D761: DD 86          STD     <$86            
D763: 66 E4          ROR     ,S              
D765: DC 84          LDD     <$84            
D767: D3 80          ADDD    <$80            
D769: DD 84          STD     <$84            
D76B: A6 E4          LDA     ,S              
D76D: 46             RORA                    
D76E: 44             LSRA                    
D76F: 44             LSRA                    
D770: B8 FF 20       EORA    $FF20                          ; {hard:PIA1_DA} 
D773: B7 FF 20       STA     $FF20                          ; {hard:PIA1_DA} 
D776: 30 1F          LEAX    -1,X            
D778: 26 E1          BNE     $D75B                          ; 
D77A: 35 81          PULS    CC,PC           
D77C: 34 01          PSHS    CC              
D77E: 1A 50          ORCC    #$50            
D780: CE C0 03       LDU     #$C003          
D783: 8E 09 5D       LDX     #$095D          
D786: 86 02          LDA     #$02            
D788: B7 FF 20       STA     $FF20                          ; {hard:PIA1_DA} 
D78B: A6 C0          LDA     ,U+             
D78D: 27 08          BEQ     $D797                          ; 
D78F: F6 FF 20       LDB     $FF20                          ; {hard:PIA1_DA} 
D792: C8 F0          EORB    #$F0            
D794: F7 FF 20       STB     $FF20                          ; {hard:PIA1_DA} 
D797: 21 FE          BRN     $D797                          ; 
D799: 4A             DECA                    
D79A: 26 FB          BNE     $D797                          ; 
D79C: 30 1F          LEAX    -1,X            
D79E: 26 EB          BNE     $D78B                          ; 
D7A0: 86 02          LDA     #$02            
D7A2: B7 FF 20       STA     $FF20                          ; {hard:PIA1_DA} 
D7A5: 35 81          PULS    CC,PC           
D7A7: 86 01          LDA     #$01            
D7A9: 97 A5          STA     <$A5            
D7AB: 34 01          PSHS    CC              
D7AD: 1A 50          ORCC    #$50            
D7AF: C6 02          LDB     #$02            
D7B1: 96 A5          LDA     <$A5            
D7B3: 4A             DECA                    
D7B4: 12             NOP                     
D7B5: 26 FC          BNE     $D7B3                          ; 
D7B7: 86 C2          LDA     #$C2            
D7B9: B7 FF 20       STA     $FF20                          ; {hard:PIA1_DA} 
D7BC: 96 A5          LDA     <$A5            
D7BE: 40             NEGA                    
D7BF: 4A             DECA                    
D7C0: 12             NOP                     
D7C1: 26 FC          BNE     $D7BF                          ; 
D7C3: 86 02          LDA     #$02            
D7C5: B7 FF 20       STA     $FF20                          ; {hard:PIA1_DA} 
D7C8: 5A             DECB                    
D7C9: 26 E6          BNE     $D7B1                          ; 
D7CB: 0C A5          INC     <$A5            
D7CD: 26 E0          BNE     $D7AF                          ; 
D7CF: 8E 40 00       LDX     #$4000          
D7D2: 30 1F          LEAX    -1,X            
D7D4: 26 FC          BNE     $D7D2                          ; 
D7D6: 35 81          PULS    CC,PC           
D7D8: DC A2          LDD     <$A2            
D7DA: 80 02          SUBA    #$02            
D7DC: C0 02          SUBB    #$02            
D7DE: BD DE 59       JSR     $DE59                          ; 
D7E1: 33 84          LEAU    ,X              
D7E3: D7 88          STB     <$88            
D7E5: 10 8E C9 60    LDY     #$C960          
D7E9: D6 A4          LDB     <$A4            
D7EB: 86 06          LDA     #$06            
D7ED: 3D             MUL                     
D7EE: 0D A1          TST     <$A1            
D7F0: 2A 02          BPL     $D7F4                          ; 
D7F2: CB 18          ADDB    #$18            
D7F4: 31 A5          LEAY    B,Y             
D7F6: 86 06          LDA     #$06            
D7F8: 97 99          STA     <$99            
D7FA: A6 A0          LDA     ,Y+             
D7FC: 34 40          PSHS    U               
D7FE: 4D             TSTA                    
D7FF: 2A 06          BPL     $D807                          ; 
D801: E6 C4          LDB     ,U              
D803: DA 88          ORB     <$88            
D805: E7 C4          STB     ,U              
D807: 33 C8 20       LEAU    $20,U           
D80A: 48             LSLA                    
D80B: 26 F2          BNE     $D7FF                          ; 
D80D: 35 40          PULS    U               
D80F: 96 88          LDA     <$88            
D811: 44             LSRA                    
D812: 44             LSRA                    
D813: 26 04          BNE     $D819                          ; 
D815: 86 C0          LDA     #$C0            
D817: 33 41          LEAU    1,U             
D819: 97 88          STA     <$88            
D81B: 0A 99          DEC     <$99            
D81D: 26 DB          BNE     $D7FA                          ; 
D81F: 39             RTS                     
D820: 10 8E 28 08    LDY     #$2808          
D824: 96 A0          LDA     <$A0            
D826: 97 98          STA     <$98            
D828: EC A4          LDD     ,Y              
D82A: 90 A2          SUBA    <$A2            
D82C: 2A 01          BPL     $D82F                          ; 
D82E: 40             NEGA                    
D82F: 81 0B          CMPA    #$0B            
D831: 24 0B          BCC     $D83E                          ; 
D833: D0 A3          SUBB    <$A3            
D835: 2A 01          BPL     $D838                          ; 
D837: 50             NEGB                    
D838: C1 0B          CMPB    #$0B            
D83A: 24 02          BCC     $D83E                          ; 
D83C: 8D 07          BSR     $D845                          ; 
D83E: 31 23          LEAY    3,Y             
D840: 0A 98          DEC     <$98            
D842: 26 E4          BNE     $D828                          ; 
D844: 39             RTS                     
D845: 34 20          PSHS    Y               
D847: EC A4          LDD     ,Y              
D849: 90 A2          SUBA    <$A2            
D84B: D0 A3          SUBB    <$A3            
D84D: 48             LSLA                    
D84E: 58             LSLB                    
D84F: 9B A2          ADDA    <$A2            
D851: DB A3          ADDB    <$A3            
D853: C0 02          SUBB    #$02            
D855: 80 02          SUBA    #$02            
D857: DD 8E          STD     <$8E            
D859: A6 22          LDA     2,Y             
D85B: 84 01          ANDA    #$01            
D85D: 88 01          EORA    #$01            
D85F: C6 48          LDB     #$48            
D861: 3D             MUL                     
D862: 0D A1          TST     <$A1            
D864: 27 03          BEQ     $D869                          ; 
D866: C3 00 90       ADDD    #$0090          
D869: CE C9 90       LDU     #$C990          
D86C: 33 CB          LEAU    D,U             
D86E: 86 12          LDA     #$12            
D870: D6 8F          LDB     <$8F            
D872: C4 03          ANDB    #$03            
D874: 3D             MUL                     
D875: 33 C5          LEAU    B,U             
D877: DC 8E          LDD     <$8E            
D879: BD DE 59       JSR     $DE59                          ; 
D87C: 86 03          LDA     #$03            
D87E: 97 99          STA     <$99            
D880: D6 8F          LDB     <$8F            
D882: 54             LSRB                    
D883: 54             LSRB                    
D884: C4 1F          ANDB    #$1F            
D886: 10 8E 28 C8    LDY     #$28C8          
D88A: 31 A5          LEAY    B,Y             
D88C: A6 A4          LDA     ,Y              
D88E: 27 1E          BEQ     $D8AE                          ; 
D890: 34 50          PSHS    U,X             
D892: C6 06          LDB     #$06            
D894: 9C A9          CMPX    <$A9            
D896: 24 0C          BCC     $D8A4                          ; 
D898: 9C A7          CMPX    <$A7            
D89A: 25 08          BCS     $D8A4                          ; 
D89C: A6 C4          LDA     ,U              
D89E: A4 A4          ANDA    ,Y              
D8A0: AA 84          ORA     ,X              
D8A2: A7 84          STA     ,X              
D8A4: 33 41          LEAU    1,U             
D8A6: 30 88 20       LEAX    $20,X           
D8A9: 5A             DECB                    
D8AA: 26 E8          BNE     $D894                          ; 
D8AC: 35 50          PULS    X,U             
D8AE: 30 01          LEAX    1,X             
D8B0: 33 46          LEAU    6,U             
D8B2: 31 21          LEAY    1,Y             
D8B4: 0A 99          DEC     <$99            
D8B6: 26 D4          BNE     $D88C                          ; 
D8B8: 35 A0          PULS    Y,PC            
D8BA: 96 C2          LDA     <$C2            
D8BC: 26 28          BNE     $D8E6                          ; 
D8BE: 86 F7          LDA     #$F7            
D8C0: C4 01          ANDB    #$01            
D8C2: D7 A5          STB     <$A5            
D8C4: 27 02          BEQ     $D8C8                          ; 
D8C6: 86 DF          LDA     #$DF            
D8C8: B7 FF 02       STA     $FF02                          ; {hard:PIA0_DB} 
D8CB: 5F             CLRB                    
D8CC: B6 FF 00       LDA     $FF00                          ; {hard:PIA0_DA} 
D8CF: 84 08          ANDA    #$08            
D8D1: 27 10          BEQ     $D8E3                          ; 
D8D3: 1A 01          ORCC    #$01            
D8D5: 79 FF 02       ROL     $FF02                          ; {hard:PIA0_DB} 
D8D8: C6 02          LDB     #$02            
D8DA: B6 FF 00       LDA     $FF00                          ; {hard:PIA0_DA} 
D8DD: 84 08          ANDA    #$08            
D8DF: 27 02          BEQ     $D8E3                          ; 
D8E1: C6 80          LDB     #$80            
D8E3: DB A5          ADDB    <$A5            
D8E5: 39             RTS                     
D8E6: B6 FF 23       LDA     $FF23                          ; {hard:PIA1_CB} 
D8E9: 34 02          PSHS    A               
D8EB: 84 F7          ANDA    #$F7            
D8ED: B7 FF 23       STA     $FF23                          ; {hard:PIA1_CB} 
D8F0: B6 FF 20       LDA     $FF20                          ; {hard:PIA1_DA} 
D8F3: 34 02          PSHS    A               
D8F5: C4 01          ANDB    #$01            
D8F7: D7 A5          STB     <$A5            
D8F9: C8 01          EORB    #$01            
D8FB: 58             LSLB                    
D8FC: 58             LSLB                    
D8FD: 58             LSLB                    
D8FE: 34 04          PSHS    B               
D900: F6 FF 01       LDB     $FF01                          ; {hard:PIA0_CA} 
D903: C4 F7          ANDB    #$F7            
D905: EA E0          ORB     ,S+             
D907: F7 FF 01       STB     $FF01                          ; {hard:PIA0_CA} 
D90A: 5F             CLRB                    
D90B: 86 22          LDA     #$22            
D90D: B7 FF 20       STA     $FF20                          ; {hard:PIA1_DA} 
D910: 7D FF 00       TST     $FF00                          ; {hard:PIA0_DA} 
D913: 2A 0E          BPL     $D923                          ; 
D915: 86 DF          LDA     #$DF            
D917: B7 FF 20       STA     $FF20                          ; {hard:PIA1_DA} 
D91A: C6 02          LDB     #$02            
D91C: 7D FF 00       TST     $FF00                          ; {hard:PIA0_DA} 
D91F: 2B 02          BMI     $D923                          ; 
D921: C6 80          LDB     #$80            
D923: 86 34          LDA     #$34            
D925: B7 FF 01       STA     $FF01                          ; {hard:PIA0_CA} 
D928: 35 02          PULS    A               
D92A: B7 FF 20       STA     $FF20                          ; {hard:PIA1_DA} 
D92D: 35 02          PULS    A               
D92F: B7 FF 23       STA     $FF23                          ; {hard:PIA1_CB} 
D932: DB A5          ADDB    <$A5            
D934: 39             RTS                     
D935: 0D B5          TST     <$B5            
D937: 10 27 00 AA    LBEQ    $00AA           
D93B: DC A2          LDD     <$A2            
D93D: BD DA 24       JSR     $DA24                          ; 
D940: 24 0C          BCC     $D94E                          ; 
D942: DC A2          LDD     <$A2            
D944: BD DE 5C       JSR     $DE5C                          ; 
D947: C4 55          ANDB    #$55            
D949: 53             COMB                    
D94A: E4 84          ANDB    ,X              
D94C: E7 84          STB     ,X              
D94E: DC A2          LDD     <$A2            
D950: BD DA 12       JSR     $DA12                          ; 
D953: 24 1D          BCC     $D972                          ; 
D955: D6 A4          LDB     <$A4            
D957: C8 01          EORB    #$01            
D959: BD D8 BA       JSR     $D8BA                          ; 
D95C: 2B 14          BMI     $D972                          ; 
D95E: D7 A5          STB     <$A5            
D960: DC A2          LDD     <$A2            
D962: BD DE 5C       JSR     $DE5C                          ; 
D965: 96 A5          LDA     <$A5            
D967: BD DF 42       JSR     $DF42                          ; 
D96A: 25 06          BCS     $D972                          ; 
D96C: 96 A5          LDA     <$A5            
D96E: 97 A4          STA     <$A4            
D970: 20 09          BRA     $D97B                          ; 
D972: D6 A4          LDB     <$A4            
D974: BD D8 BA       JSR     $D8BA                          ; 
D977: 2B 02          BMI     $D97B                          ; 
D979: D7 A4          STB     <$A4            
D97B: DC A2          LDD     <$A2            
D97D: BD DA 12       JSR     $DA12                          ; 
D980: 24 0C          BCC     $D98E                          ; 
D982: DC A2          LDD     <$A2            
D984: BD DE 5C       JSR     $DE5C                          ; 
D987: 96 A4          LDA     <$A4            
D989: BD DF 42       JSR     $DF42                          ; 
D98C: 25 0F          BCS     $D99D                          ; 
D98E: 8E DE 4F       LDX     #$DE4F          
D991: D6 A4          LDB     <$A4            
D993: 58             LSLB                    
D994: 3A             ABX                     
D995: DC A2          LDD     <$A2            
D997: AB 84          ADDA    ,X              
D999: EB 01          ADDB    1,X             
D99B: DD A2          STD     <$A2            
D99D: DC A2          LDD     <$A2            
D99F: BD DA 24       JSR     $DA24                          ; 
D9A2: 24 40          BCC     $D9E4                          ; 
D9A4: DC A2          LDD     <$A2            
D9A6: BD DE 5C       JSR     $DE5C                          ; 
D9A9: E7 E2          STB     ,-S             
D9AB: A6 84          LDA     ,X              
D9AD: A8 E4          EORA    ,S              
D9AF: A4 E0          ANDA    ,S+             
D9B1: 26 24          BNE     $D9D7                          ; 
D9B3: 86 03          LDA     #$03            
D9B5: 97 BA          STA     <$BA            
D9B7: 96 B5          LDA     <$B5            
D9B9: 27 1C          BEQ     $D9D7                          ; 
D9BB: 96 B2          LDA     <$B2            
D9BD: 8B 10          ADDA    #$10            
D9BF: 19             DAA                     
D9C0: 97 B2          STA     <$B2            
D9C2: 96 B1          LDA     <$B1            
D9C4: 89 00          ADCA    #$00            
D9C6: 19             DAA                     
D9C7: 97 B1          STA     <$B1            
D9C9: 86 02          LDA     #$02            
D9CB: 97 B8          STA     <$B8            
D9CD: 0F B6          CLR     <$B6            
D9CF: DE BE          LDU     <$BE            
D9D1: 27 04          BEQ     $D9D7                          ; 
D9D3: 33 5F          LEAU    -1,U            
D9D5: DF BE          STU     <$BE            
D9D7: 1F 98          TFR     B,A             
D9D9: 53             COMB                    
D9DA: E4 84          ANDB    ,X              
D9DC: 34 04          PSHS    B               
D9DE: 84 AA          ANDA    #$AA            
D9E0: AA E0          ORA     ,S+             
D9E2: A7 84          STA     ,X              
D9E4: 39             RTS                     
D9E5: D6 A4          LDB     <$A4            
D9E7: 58             LSLB                    
D9E8: 8E DE 4F       LDX     #$DE4F          
D9EB: 3A             ABX                     
D9EC: DC A2          LDD     <$A2            
D9EE: AB 84          ADDA    ,X              
D9F0: EB 01          ADDB    1,X             
D9F2: DD 8E          STD     <$8E            
D9F4: BD DF CC       JSR     $DFCC                          ; 
D9F7: 24 08          BCC     $DA01                          ; 
D9F9: 96 A4          LDA     <$A4            
D9FB: 88 02          EORA    #$02            
D9FD: 97 A4          STA     <$A4            
D9FF: 20 0E          BRA     $DA0F                          ; 
DA01: DC A2          LDD     <$A2            
DA03: BD DA 12       JSR     $DA12                          ; 
DA06: 24 07          BCC     $DA0F                          ; 
DA08: 10 8E 00 A2    LDY     #$00A2          
DA0C: BD DE FD       JSR     $DEFD                          ; 
DA0F: 7E D9 7B       JMP     $D97B                          ; 
DA12: 80 11          SUBA    #$11            
DA14: 84 03          ANDA    #$03            
DA16: 26 09          BNE     $DA21                          ; 
DA18: C0 19          SUBB    #$19            
DA1A: C4 03          ANDB    #$03            
DA1C: 26 03          BNE     $DA21                          ; 
DA1E: 1A 01          ORCC    #$01            
DA20: 39             RTS                     
DA21: 1C FE          ANDCC   #$FE            
DA23: 39             RTS                     
DA24: 80 11          SUBA    #$11            
DA26: 84 01          ANDA    #$01            
DA28: 26 F7          BNE     $DA21                          ; 
DA2A: C0 19          SUBB    #$19            
DA2C: C4 01          ANDB    #$01            
DA2E: 26 F1          BNE     $DA21                          ; 
DA30: 1A 01          ORCC    #$01            
DA32: 39             RTS                     

DA33: 8E 28 C8       LDX     #$28C8          
DA36: C6 20          LDB     #$20            
DA38: 6F 80          CLR     ,X+             
DA3A: 5A             DECB                    
DA3B: 26 FB          BNE     $DA38                          ; 
DA3D: 6F 8D 26 7B    CLR     $267B,PC        
DA41: 86 02          LDA     #$02            
DA43: B7 FF 20       STA     $FF20                          ; {hard:PIA1_DA} 
DA46: DC A2          LDD     <$A2            
DA48: 80 11          SUBA    #$11            
DA4A: C0 11          SUBB    #$11            
DA4C: BD DE 59       JSR     $DE59                          ; 
DA4F: 33 84          LEAU    ,X              
DA51: D7 88          STB     <$88            
DA53: BD DB 10       JSR     $DB10                          ; 
DA56: 33 88 20       LEAU    $20,X           
DA59: DF A7          STU     <$A7            
DA5B: 33 84          LEAU    ,X              
DA5D: 04 88          LSR     <$88            
DA5F: 04 88          LSR     <$88            
DA61: 26 06          BNE     $DA69                          ; 
DA63: 33 41          LEAU    1,U             
DA65: C6 C0          LDB     #$C0            
DA67: D7 88          STB     <$88            
DA69: 86 22          LDA     #$22            
DA6B: 97 99          STA     <$99            
DA6D: 0F BD          CLR     <$BD            
DA6F: 0F A5          CLR     <$A5            
DA71: DC A2          LDD     <$A2            
DA73: 83 08 08       SUBD    #$0808          
DA76: BD DE 5C       JSR     $DE5C                          ; 
DA79: 31 84          LEAY    ,X              
DA7B: D7 89          STB     <$89            
DA7D: 8E 28 C8       LDX     #$28C8          
DA80: 1F 30          TFR     U,D             
DA82: C4 1F          ANDB    #$1F            
DA84: 30 85          LEAX    B,X             
DA86: 86 11          LDA     #$11            
DA88: 97 98          STA     <$98            
DA8A: 34 70          PSHS    U,Y,X           
DA8C: 96 88          LDA     <$88            
DA8E: AA C4          ORA     ,U              
DA90: A7 C4          STA     ,U              
DA92: 33 C8 20       LEAU    $20,U           
DA95: 96 88          LDA     <$88            
DA97: AA 84          ORA     ,X              
DA99: A7 84          STA     ,X              
DA9B: 96 BA          LDA     <$BA            
DA9D: 27 0A          BEQ     $DAA9                          ; 
DA9F: 96 BD          LDA     <$BD            
DAA1: 88 40          EORA    #$40            
DAA3: 97 BD          STA     <$BD            
DAA5: 8B 40          ADDA    #$40            
DAA7: 97 BC          STA     <$BC            
DAA9: 8E DB 5C       LDX     #$DB5C          
DAAC: 4F             CLRA                    
DAAD: D6 89          LDB     <$89            
DAAF: E4 A4          ANDB    ,Y              
DAB1: A6 8B          LDA     D,X             
DAB3: 94 88          ANDA    <$88            
DAB5: 34 02          PSHS    A               
DAB7: 96 88          LDA     <$88            
DAB9: 43             COMA                    
DABA: A4 C4          ANDA    ,U              
DABC: AA E4          ORA     ,S              
DABE: A7 C4          STA     ,U              
DAC0: 96 88          LDA     <$88            
DAC2: 43             COMA                    
DAC3: A4 C8 20       ANDA    $20,U           
DAC6: AA E0          ORA     ,S+             
DAC8: A7 C8 20       STA     $20,U           
DACB: 33 C8 40       LEAU    $40,U           
DACE: 96 BB          LDA     <$BB            
DAD0: 9B BC          ADDA    <$BC            
DAD2: 97 BB          STA     <$BB            
DAD4: 24 09          BCC     $DADF                          ; 
DAD6: 86 40          LDA     #$40            
DAD8: A8 8D 24 44    EORA    $2444,PC        
DADC: B7 FF 20       STA     $FF20                          ; {hard:PIA1_DA} 
DADF: 31 A8 20       LEAY    $20,Y           
DAE2: 0A 98          DEC     <$98            
DAE4: 26 C6          BNE     $DAAC                          ; 
DAE6: DF A9          STU     <$A9            
DAE8: D6 88          LDB     <$88            
DAEA: EA C4          ORB     ,U              
DAEC: E7 C4          STB     ,U              
DAEE: DC 88          LDD     <$88            
DAF0: 35 70          PULS    X,Y,U           
DAF2: 03 A5          COM     <$A5            
DAF4: 26 08          BNE     $DAFE                          ; 
DAF6: 54             LSRB                    
DAF7: 54             LSRB                    
DAF8: 26 04          BNE     $DAFE                          ; 
DAFA: 31 21          LEAY    1,Y             
DAFC: C6 C0          LDB     #$C0            
DAFE: 44             LSRA                    
DAFF: 44             LSRA                    
DB00: 26 06          BNE     $DB08                          ; 
DB02: 86 C0          LDA     #$C0            
DB04: 33 41          LEAU    1,U             
DB06: 30 01          LEAX    1,X             
DB08: DD 88          STD     <$88            
DB0A: 0A 99          DEC     <$99            
DB0C: 10 26 FF 76    LBNE    $FF76           
DB10: C6 24          LDB     #$24            
DB12: 96 88          LDA     <$88            
DB14: AA C4          ORA     ,U              
DB16: A7 C4          STA     ,U              
DB18: 33 C8 20       LEAU    $20,U           
DB1B: 5A             DECB                    
DB1C: 26 F4          BNE     $DB12                          ; 
DB1E: 39             RTS                     
DB1F: EC 8D 25 7F    LDD     $257F,PC        
DB23: 80 12          SUBA    #$12            
DB25: 2A 01          BPL     $DB28                          ; 
DB27: 4F             CLRA                    
DB28: C0 16          SUBB    #$16            
DB2A: 34 06          PSHS    B,A             
DB2C: BD DE 59       JSR     $DE59                          ; 
DB2F: 1F 13          TFR     X,U             
DB31: 35 06          PULS    A,B             
DB33: 97 A5          STA     <$A5            
DB35: BD DE 5C       JSR     $DE5C                          ; 
DB38: 86 26          LDA     #$26            
DB3A: 97 99          STA     <$99            
DB3C: 9B A5          ADDA    <$A5            
DB3E: 81 60          CMPA    #$60            
DB40: 25 06          BCS     $DB48                          ; 
DB42: 86 60          LDA     #$60            
DB44: 90 A5          SUBA    <$A5            
DB46: 97 99          STA     <$99            
DB48: C6 0C          LDB     #$0C            
DB4A: A6 80          LDA     ,X+             
DB4C: A7 C0          STA     ,U+             
DB4E: 5A             DECB                    
DB4F: 26 F9          BNE     $DB4A                          ; 
DB51: 30 88 14       LEAX    $14,X           
DB54: 33 C8 14       LEAU    $14,U           
DB57: 0A 99          DEC     <$99            
DB59: 26 ED          BNE     $DB48                          ; 
DB5B: 39             RTS                     
DB5C: 00 55          NEG     <$55            
DB5E: AA FF 55 FF    ORA     [$55FF]         
DB62: FF FF AA       STU     $FFAA           
DB65: FF FF FF       STU     $FFFF                          ; {hard:vectorReset} 
DB68: FF FF FF       STU     $FFFF                          ; {hard:vectorReset} 
DB6B: FF 55 96       STU     $5596           
DB6E: 92 81          SBCA    <$81            
DB70: 1C 27          ANDCC   #$27            
DB72: 03 5F          COM     <$5F            
DB74: 8D 07          BSR     $DB7D                          ; 
DB76: 86 1C          LDA     #$1C            
DB78: 97 92          STA     <$92                           ; {ram:RequestedPage} 
DB7A: 13             SYNC                    
DB7B: 39             RTS                     
DB7C: AA                                  
DB7D: 8E 1C 00       LDX     #$1C00          
DB80: 1F 03          TFR     D,U             
DB82: EC C1          LDD     ,U++            
DB84: ED 81          STD     ,X++            
DB86: 8C 28 00       CMPX    #$2800          
DB89: 25 F7          BCS     $DB82                          ; 
DB8B: 39             RTS                     
DB8C: FF FF FF       STU     $FFFF                          ; {hard:vectorReset} 
DB8F: FF FF FF       STU     $FFFF                          ; {hard:vectorReset} 
DB92: FF FF FF       STU     $FFFF                          ; {hard:vectorReset} 
DB95: FF FF FF       STU     $FFFF                          ; {hard:vectorReset} 
DB98: FF FF FF       STU     $FFFF                          ; {hard:vectorReset} 
DB9B: FF 55 CE       STU     $55CE           
DB9E: C9 EA          ADCB    #$EA            
DBA0: 0D A1          TST     <$A1            
DBA2: 27 03          BEQ     $DBA7                          ; 
DBA4: CE CA 7A       LDU     #$CA7A          
DBA7: 96 98          LDA     <$98            
DBA9: C6 20          LDB     #$20            
DBAB: 3D             MUL                     
DBAC: 8B 1C          ADDA    #$1C            
DBAE: 1F 01          TFR     D,X             
DBB0: 39             RTS                     
DBB1: 8D EA          BSR     $DB9D                          ; 
DBB3: 86 06          LDA     #$06            
DBB5: 97 99          STA     <$99            
DBB7: C6 10          LDB     #$10            
DBB9: D7 A5          STB     <$A5            
DBBB: E6 46          LDB     6,U             
DBBD: A6 C0          LDA     ,U+             
DBBF: ED 81          STD     ,X++            
DBC1: 0A A5          DEC     <$A5            
DBC3: 26 FA          BNE     $DBBF                          ; 
DBC5: 0A 99          DEC     <$99            
DBC7: 26 EE          BNE     $DBB7                          ; 
DBC9: 9F A5          STX     <$A5            
DBCB: 39             RTS                     
DBCC: FF FF FF       STU     $FFFF                          ; {hard:vectorReset} 
DBCF: FF FF FF       STU     $FFFF                          ; {hard:vectorReset} 
DBD2: FF FF FF       STU     $FFFF                          ; {hard:vectorReset} 
DBD5: FF FF FF       STU     $FFFF                          ; {hard:vectorReset} 
DBD8: FF FF FF       STU     $FFFF                          ; {hard:vectorReset} 
DBDB: FF AA C6       STU     $AAC6           
DBDE: FF 86 5F       STU     $865F           
DBE1: D7 88          STB     <$88            
DBE3: 8D B8          BSR     $DB9D                          ; 
DBE5: 30 88 17       LEAX    $17,X           
DBE8: 86 02          LDA     #$02            
DBEA: 34 12          PSHS    X,A             
DBEC: C6 06          LDB     #$06            
DBEE: 96 88          LDA     <$88            
DBF0: 43             COMA                    
DBF1: A4 C0          ANDA    ,U+             
DBF3: 34 02          PSHS    A               
DBF5: 96 88          LDA     <$88            
DBF7: A4 89 F4 00    ANDA    $F400,X         
DBFB: AA E0          ORA     ,S+             
DBFD: A7 84          STA     ,X              
DBFF: 30 88 20       LEAX    $20,X           
DC02: 5A             DECB                    
DC03: 26 E9          BNE     $DBEE                          ; 
DC05: 35 12          PULS    A,X             
DC07: 30 01          LEAX    1,X             
DC09: 4A             DECA                    
DC0A: 26 DE          BNE     $DBEA                          ; 
DC0C: 39             RTS                     
DC0D: FF FF FF       STU     $FFFF                          ; {hard:vectorReset} 
DC10: FF FF FF       STU     $FFFF                          ; {hard:vectorReset} 
DC13: FF FF FF       STU     $FFFF                          ; {hard:vectorReset} 
DC16: FF FF FF       STU     $FFFF                          ; {hard:vectorReset} 
DC19: FF FF FF       STU     $FFFF                          ; {hard:vectorReset} 
DC1C: FF 34 06       STU     $3406           
DC1F: C4 03          ANDB    #$03            
DC21: 8E DE 76       LDX     #$DE76          
DC24: E6 85          LDB     B,X             
DC26: C4 55          ANDB    #$55            
DC28: D7 88          STB     <$88            
DC2A: E6 61          LDB     1,S             
DC2C: 8E 05 C0       LDX     #$05C0          
DC2F: 54             LSRB                    
DC30: 54             LSRB                    
DC31: 3A             ABX                     
DC32: C6 43          LDB     #$43            
DC34: 96 88          LDA     <$88            
DC36: AA 84          ORA     ,X              
DC38: A7 84          STA     ,X              
DC3A: 30 88 20       LEAX    $20,X           
DC3D: 5A             DECB                    
DC3E: 26 F4          BNE     $DC34                          ; 
DC40: 35 86          PULS    A,B,PC          
DC42: 34 06          PSHS    B,A             
DC44: 86 20          LDA     #$20            
DC46: 3D             MUL                     
DC47: C3 04 06       ADDD    #$0406          
DC4A: 1F 01          TFR     D,X             
DC4C: CC 55 14       LDD     #$5514          
DC4F: A7 80          STA     ,X+             
DC51: 5A             DECB                    
DC52: 26 FB          BNE     $DC4F                          ; 
DC54: 35 86          PULS    A,B,PC          
DC56: CE 06 00       LDU     #$0600          
DC59: 8E 08 00       LDX     #$0800          
DC5C: 6F C0          CLR     ,U+             
DC5E: 30 1F          LEAX    -1,X            
DC60: 26 FA          BNE     $DC5C                          ; 
DC62: CE CA B0       LDU     #$CAB0          
DC65: BD D4 81       JSR     $D481                          ; 
DC68: C6 0E          LDB     #$0E            
DC6A: 8D D6          BSR     $DC42                          ; 
DC6C: 5C             INCB                    
DC6D: 8D D3          BSR     $DC42                          ; 
DC6F: 86 10          LDA     #$10            
DC71: CB 04          ADDB    #$04            
DC73: BD DC 42       JSR     $DC42                          ; 
DC76: 4A             DECA                    
DC77: 26 F8          BNE     $DC71                          ; 
DC79: 5C             INCB                    
DC7A: BD DC 42       JSR     $DC42                          ; 
DC7D: C6 16          LDB     #$16            
DC7F: BD DC 1D       JSR     $DC1D                          ; 
DC82: 5C             INCB                    
DC83: BD DC 1D       JSR     $DC1D                          ; 
DC86: 86 14          LDA     #$14            
DC88: CB 04          ADDB    #$04            
DC8A: BD DC 1D       JSR     $DC1D                          ; 
DC8D: 4A             DECA                    
DC8E: 26 F8          BNE     $DC88                          ; 
DC90: 5C             INCB                    
DC91: BD DC 1D       JSR     $DC1D                          ; 
DC94: CE 28 E8       LDU     #$28E8          
DC97: 8E 01 40       LDX     #$0140          
DC9A: 6F C0          CLR     ,U+             
DC9C: 30 1F          LEAX    -1,X            
DC9E: 26 FA          BNE     $DC9A                          ; 
DCA0: 73 29 92       COM     $2992           
DCA3: CE DE 4F       LDU     #$DE4F          
DCA6: 10 8E 2A 28    LDY     #$2A28          
DCAA: 10 9F 8A       STY     <$8A            
DCAD: CC 08 0A       LDD     #$080A          
DCB0: DD 8E          STD     <$8E            
DCB2: EC C4          LDD     ,U              
DCB4: BD DD 63       JSR     $DD63                          ; 
DCB7: 63 84          COM     ,X              
DCB9: EC C1          LDD     ,U++            
DCBB: BD DD 83       JSR     $DD83                          ; 
DCBE: DC 95          LDD     <$95            
DCC0: ED A1          STD     ,Y++            
DCC2: EC C4          LDD     ,U              
DCC4: 26 EC          BNE     $DCB2                          ; 
DCC6: 10 9F 8C       STY     <$8C            
DCC9: 9E 8A          LDX     <$8A            
DCCB: 9C 8C          CMPX    <$8C            
DCCD: 10 27 00 FA    LBEQ    $00FA           
DCD1: EC 81          LDD     ,X++            
DCD3: DD 8E          STD     <$8E            
DCD5: 9F 8A          STX     <$8A            
DCD7: 86 FF          LDA     #$FF            
DCD9: 97 97          STA     <$97            
DCDB: DC 8E          LDD     <$8E            
DCDD: BD DD 6F       JSR     $DD6F                          ; 
DCE0: 86 FF          LDA     #$FF            
DCE2: A7 84          STA     ,X              
DCE4: 0F 88          CLR     <$88            
DCE6: CE DE 4F       LDU     #$DE4F          
DCE9: EC C1          LDD     ,U++            
DCEB: 27 19          BEQ     $DD06                          ; 
DCED: BD DD 63       JSR     $DD63                          ; 
DCF0: 25 F7          BCS     $DCE9                          ; 
DCF2: A6 84          LDA     ,X              
DCF4: 26 F3          BNE     $DCE9                          ; 
DCF6: D6 88          LDB     <$88            
DCF8: 5C             INCB                    
DCF9: D7 88          STB     <$88            
DCFB: 58             LSLB                    
DCFC: 8E 27 FE       LDX     #$27FE          
DCFF: 3A             ABX                     
DD00: EC 5E          LDD     -2,U            
DD02: ED 84          STD     ,X              
DD04: 20 E3          BRA     $DCE9                          ; 
DD06: 96 88          LDA     <$88            
DD08: 27 2E          BEQ     $DD38                          ; 
DD0A: CE 28 00       LDU     #$2800          
DD0D: 4A             DECA                    
DD0E: 27 0C          BEQ     $DD1C                          ; 
DD10: BD DD 52       JSR     $DD52                          ; 
DD13: 84 03          ANDA    #$03            
DD15: 91 88          CMPA    <$88            
DD17: 24 F7          BCC     $DD10                          ; 
DD19: 48             LSLA                    
DD1A: 33 C6          LEAU    A,U             
DD1C: EC C4          LDD     ,U              
DD1E: DD 93          STD     <$93            
DD20: BD DD 83       JSR     $DD83                          ; 
DD23: 0F 97          CLR     <$97            
DD25: 0A 88          DEC     <$88            
DD27: 27 08          BEQ     $DD31                          ; 
DD29: DC 8E          LDD     <$8E            
DD2B: 9E 8C          LDX     <$8C            
DD2D: ED 81          STD     ,X++            
DD2F: 9F 8C          STX     <$8C            
DD31: DC 95          LDD     <$95            
DD33: DD 8E          STD     <$8E            
DD35: 7E DC DB       JMP     $DCDB                          ; 
DD38: 0D 97          TST     <$97            
DD3A: 26 13          BNE     $DD4F                          ; 
DD3C: DC 93          LDD     <$93            
DD3E: BD DD 63       JSR     $DD63                          ; 
DD41: 25 0C          BCS     $DD4F                          ; 
DD43: BD DD 52       JSR     $DD52                          ; 
DD46: 91 C0          CMPA    <$C0            
DD48: 24 05          BCC     $DD4F                          ; 
DD4A: DC 93          LDD     <$93            
DD4C: BD DD 83       JSR     $DD83                          ; 
DD4F: 7E DC C9       JMP     $DCC9                          ; 
DD52: DC 90          LDD     <$90            
DD54: C3 00 15       ADDD    #$0015          
DD57: 84 1F          ANDA    #$1F            
DD59: DD 90          STD     <$90            
DD5B: C3 A0 00       ADDD    #$A000          
DD5E: 34 06          PSHS    B,A             
DD60: A6 F1          LDA     [,S++]          
DD62: 39             RTS                     
DD63: DB 8F          ADDB    <$8F            
DD65: C1 14          CMPB    #$14            
DD67: 24 17          BCC     $DD80                          ; 
DD69: 9B 8E          ADDA    <$8E            
DD6B: 81 10          CMPA    #$10            
DD6D: 24 11          BCC     $DD80                          ; 
DD6F: 34 04          PSHS    B               
DD71: 6F E2          CLR     ,-S             
DD73: C6 14          LDB     #$14            
DD75: 3D             MUL                     
DD76: E3 E1          ADDD    ,S++            
DD78: 8E 28 E8       LDX     #$28E8          
DD7B: 30 8B          LEAX    D,X             
DD7D: 1C FE          ANDCC   #$FE            
DD7F: 39             RTS                     
DD80: 1A 01          ORCC    #$01            
DD82: 39             RTS                     
DD83: 9B 8E          ADDA    <$8E            
DD85: DB 8F          ADDB    <$8F            
DD87: DD 95          STD     <$95            
DD89: D1 8F          CMPB    <$8F            
DD8B: 26 1C          BNE     $DDA9                          ; 
DD8D: 91 8E          CMPA    <$8E            
DD8F: 25 02          BCS     $DD93                          ; 
DD91: 96 8E          LDA     <$8E            
DD93: 48             LSLA                    
DD94: 48             LSLA                    
DD95: 34 04          PSHS    B               
DD97: C6 20          LDB     #$20            
DD99: 3D             MUL                     
DD9A: C3 06 66       ADDD    #$0666          
DD9D: 1F 01          TFR     D,X             
DD9F: E6 E0          LDB     ,S+             
DDA1: 3A             ABX                     
DDA2: A6 84          LDA     ,X              
DDA4: 84 03          ANDA    #$03            
DDA6: A7 84          STA     ,X              
DDA8: 39             RTS                     
DDA9: 25 02          BCS     $DDAD                          ; 
DDAB: D6 8F          LDB     <$8F            
DDAD: 48             LSLA                    
DDAE: 48             LSLA                    
DDAF: 34 04          PSHS    B               
DDB1: C6 20          LDB     #$20            
DDB3: 3D             MUL                     
DDB4: C3 06 06       ADDD    #$0606          
DDB7: 1F 01          TFR     D,X             
DDB9: E6 E0          LDB     ,S+             
DDBB: 3A             ABX                     
DDBC: C6 03          LDB     #$03            
DDBE: A6 84          LDA     ,X              
DDC0: 84 FC          ANDA    #$FC            
DDC2: A7 84          STA     ,X              
DDC4: 30 88 20       LEAX    $20,X           
DDC7: 5A             DECB                    
DDC8: 26 F4          BNE     $DDBE                          ; 
DDCA: 39             RTS                     
DDCB: 8E 06 26       LDX     #$0626          
DDCE: 86 10          LDA     #$10            
DDD0: 97 98          STA     <$98            
DDD2: 5F             CLRB                    
DDD3: A6 85          LDA     B,X             
DDD5: 8A 30          ORA     #$30            
DDD7: A7 85          STA     B,X             
DDD9: 5C             INCB                    
DDDA: C1 14          CMPB    #$14            
DDDC: 25 F5          BCS     $DDD3                          ; 
DDDE: 30 89 00 80    LEAX    $0080,X         
DDE2: 0A 98          DEC     <$98            
DDE4: 26 EC          BNE     $DDD2                          ; 
DDE6: CC 01 3F       LDD     #$013F          
DDE9: ED 8D 22 D1    STD     $22D1,PC        
DDED: 8E 0A 30       LDX     #$0A30          
DDF0: 86 CF          LDA     #$CF            
DDF2: A4 84          ANDA    ,X              
DDF4: A7 84          STA     ,X              
DDF6: 86 FF          LDA     #$FF            
DDF8: 97 A5          STA     <$A5            
DDFA: 8D 05          BSR     $DE01                          ; 
DDFC: 86 04          LDA     #$04                           ; Request show page 0400
DDFE: 97 92          STA     <$92                           ; {ram:RequestedPage} 
DE00: 39             RTS                     

DE01: C6 20          LDB     #$20            
DE03: 3D             MUL                     
DE04: D7 A5          STB     <$A5            
DE06: 86 30          LDA     #$30            
DE08: 97 98          STA     <$98            
DE0A: 8E 21 E0       LDX     #$21E0          
DE0D: 33 88 20       LEAU    $20,X           
DE10: 0D A5          TST     <$A5            
DE12: 2B 28          BMI     $DE3C                          ; 
DE14: 8E 1C 00       LDX     #$1C00          
DE17: CE 27 E0       LDU     #$27E0          
DE1A: 20 20          BRA     $DE3C                          ; 
DE1C: C6 20          LDB     #$20            
DE1E: 34 50          PSHS    U,X             
DE20: A6 89 E8 00    LDA     $E800,X         
DE24: A7 80          STA     ,X+             
DE26: A6 C9 E8 00    LDA     $E800,U         
DE2A: A7 C0          STA     ,U+             
DE2C: 5A             DECB                    
DE2D: 26 F1          BNE     $DE20                          ; 
DE2F: 35 50          PULS    X,U             
DE31: 96 A5          LDA     <$A5            
DE33: 30 86          LEAX    A,X             
DE35: 40             NEGA                    
DE36: 33 C6          LEAU    A,U             
DE38: 0A 98          DEC     <$98            
DE3A: 27 C4          BEQ     $DE00                          ; 
DE3C: 34 50          PSHS    U,X             
DE3E: CC FF 20       LDD     #$FF20          
DE41: 2B 00          BMI     $DE43                          ; 
DE43: A7 80          STA     ,X+             
DE45: A7 C0          STA     ,U+             
DE47: 5A             DECB                    
DE48: 26 F9          BNE     $DE43                          ; 
DE4A: 35 50          PULS    X,U             
DE4C: 13             SYNC                    
DE4D: 20 CD          BRA     $DE1C                          ; 
DE4F: FF 00 00       STU     $0000           
DE52: FF 01 00       STU     $0100           
DE55: 00 01          NEG     <$01            
DE57: 00 00          NEG     <$00            
DE59: 9E 9A          LDX     <$9A            
DE5B: 10 8E 04 00    LDY     #$0400          
DE5F: 34 04          PSHS    B               
DE61: C6 20          LDB     #$20            
DE63: 3D             MUL                     
DE64: 30 8B          LEAX    D,X             
DE66: E6 E4          LDB     ,S              
DE68: 54             LSRB                    
DE69: 54             LSRB                    
DE6A: 3A             ABX                     
DE6B: E6 E0          LDB     ,S+             
DE6D: C4 03          ANDB    #$03            
DE6F: 10 8E DE 76    LDY     #$DE76          
DE73: E6 A5          LDB     B,Y             
DE75: 39             RTS                     
DE76: C0 30          SUBB    #$30            
DE78: 0C 03          INC     <$03            
DE7A: 96 A0          LDA     <$A0            
DE7C: 97 98          STA     <$98            
DE7E: 10 8E 28 08    LDY     #$2808          
DE82: BD DE B6       JSR     $DEB6                          ; 
DE85: 8E DE 4F       LDX     #$DE4F          
DE88: E6 22          LDB     2,Y             
DE8A: 58             LSLB                    
DE8B: 3A             ABX                     
DE8C: EC A4          LDD     ,Y              
DE8E: AB 84          ADDA    ,X              
DE90: EB 01          ADDB    1,X             
DE92: ED A4          STD     ,Y              
DE94: BD DA 24       JSR     $DA24                          ; 
DE97: 24 16          BCC     $DEAF                          ; 
DE99: EC A4          LDD     ,Y              
DE9B: 34 20          PSHS    Y               
DE9D: BD DE 5C       JSR     $DE5C                          ; 
DEA0: 35 20          PULS    Y               
DEA2: 1F 98          TFR     B,A             
DEA4: 84 55          ANDA    #$55            
DEA6: A4 84          ANDA    ,X              
DEA8: 26 05          BNE     $DEAF                          ; 
DEAA: 53             COMB                    
DEAB: E4 84          ANDB    ,X              
DEAD: E7 84          STB     ,X              
DEAF: 31 23          LEAY    3,Y             
DEB1: 0A 98          DEC     <$98            
DEB3: 26 CD          BNE     $DE82                          ; 
DEB5: 39             RTS                     
DEB6: EC A4          LDD     ,Y              
DEB8: BD DA 24       JSR     $DA24                          ; 
DEBB: 24 F8          BCC     $DEB5                          ; 
DEBD: CE DE 4F       LDU     #$DE4F          
DEC0: 0F 88          CLR     <$88            
DEC2: 0F 99          CLR     <$99            
DEC4: EC C1          LDD     ,U++            
DEC6: 48             LSLA                    
DEC7: 58             LSLB                    
DEC8: AB A4          ADDA    ,Y              
DECA: EB 21          ADDB    1,Y             
DECC: 34 20          PSHS    Y               
DECE: BD DE 5C       JSR     $DE5C                          ; 
DED1: 35 20          PULS    Y               
DED3: 34 04          PSHS    B               
DED5: E6 84          LDB     ,X              
DED7: C8 AA          EORB    #$AA            
DED9: E4 E0          ANDB    ,S+             
DEDB: 26 0C          BNE     $DEE9                          ; 
DEDD: D6 88          LDB     <$88            
DEDF: 8E 28 00       LDX     #$2800          
DEE2: 3A             ABX                     
DEE3: 96 99          LDA     <$99            
DEE5: A7 84          STA     ,X              
DEE7: 0C 88          INC     <$88            
DEE9: 96 99          LDA     <$99            
DEEB: 4C             INCA                    
DEEC: 97 99          STA     <$99            
DEEE: 81 04          CMPA    #$04            
DEF0: 25 D2          BCS     $DEC4                          ; 
DEF2: 0D 88          TST     <$88            
DEF4: 26 29          BNE     $DF1F                          ; 
DEF6: EC A4          LDD     ,Y              
DEF8: BD DA 12       JSR     $DA12                          ; 
DEFB: 24 B8          BCC     $DEB5                          ; 
DEFD: EC A4          LDD     ,Y              
DEFF: 34 20          PSHS    Y               
DF01: BD DE 5C       JSR     $DE5C                          ; 
DF04: 35 20          PULS    Y               
DF06: CE 28 00       LDU     #$2800          
DF09: 0F 88          CLR     <$88            
DF0B: 4F             CLRA                    
DF0C: 34 12          PSHS    X,A             
DF0E: 8D 32          BSR     $DF42                          ; 
DF10: 35 12          PULS    A,X             
DF12: 25 06          BCS     $DF1A                          ; 
DF14: D6 88          LDB     <$88            
DF16: A7 C0          STA     ,U+             
DF18: 0C 88          INC     <$88            
DF1A: 4C             INCA                    
DF1B: 81 04          CMPA    #$04            
DF1D: 25 ED          BCS     $DF0C                          ; 
DF1F: 96 88          LDA     <$88            
DF21: CE 28 00       LDU     #$2800          
DF24: 4A             DECA                    
DF25: 27 16          BEQ     $DF3D                          ; 
DF27: BD DD 52       JSR     $DD52                          ; 
DF2A: 84 03          ANDA    #$03            
DF2C: 91 88          CMPA    <$88            
DF2E: 24 F7          BCC     $DF27                          ; 
DF30: CE 28 00       LDU     #$2800          
DF33: 33 C6          LEAU    A,U             
DF35: A6 C4          LDA     ,U              
DF37: A8 22          EORA    2,Y             
DF39: 81 02          CMPA    #$02            
DF3B: 27 EA          BEQ     $DF27                          ; 
DF3D: A6 C4          LDA     ,U              
DF3F: A7 22          STA     2,Y             
DF41: 39             RTS                     
DF42: 85 01          BITA    #$01            
DF44: 27 0F          BEQ     $DF55                          ; 
DF46: 85 02          BITA    #$02            
DF48: 26 02          BNE     $DF4C                          ; 
DF4A: 30 1F          LEAX    -1,X            
DF4C: E6 84          LDB     ,X              
DF4E: C4 01          ANDB    #$01            
DF50: 27 13          BEQ     $DF65                          ; 
DF52: 1A 01          ORCC    #$01            
DF54: 39             RTS                     
DF55: 30 88 40       LEAX    $40,X           
DF58: 85 02          BITA    #$02            
DF5A: 26 03          BNE     $DF5F                          ; 
DF5C: 30 88 80       LEAX    $80,X           
DF5F: E6 84          LDB     ,X              
DF61: C4 10          ANDB    #$10            
DF63: 26 ED          BNE     $DF52                          ; 
DF65: 1C FE          ANDCC   #$FE            
DF67: 39             RTS                     
DF68: C6 FF          LDB     #$FF            
DF6A: 10 8E 28 08    LDY     #$2808          
DF6E: 20 0D          BRA     $DF7D                          ; 
DF70: 5F             CLRB                    
DF71: 10 8E 28 08    LDY     #$2808          
DF75: 0D A1          TST     <$A1            
DF77: 2A 04          BPL     $DF7D                          ; 
DF79: 10 8E 28 68    LDY     #$2868          
DF7D: D7 88          STB     <$88            
DF7F: 96 A0          LDA     <$A0            
DF81: 97 98          STA     <$98            
DF83: E6 21          LDB     1,Y             
DF85: C4 03          ANDB    #$03            
DF87: 8E DE 76       LDX     #$DE76          
DF8A: E6 85          LDB     B,X             
DF8C: 34 04          PSHS    B               
DF8E: A6 A4          LDA     ,Y              
DF90: C6 20          LDB     #$20            
DF92: 3D             MUL                     
DF93: 34 06          PSHS    B,A             
DF95: 4F             CLRA                    
DF96: E6 21          LDB     1,Y             
DF98: 54             LSRB                    
DF99: 54             LSRB                    
DF9A: E3 E1          ADDD    ,S++            
DF9C: 8E 04 00       LDX     #$0400          
DF9F: 30 8B          LEAX    D,X             
DFA1: D3 9A          ADDD    <$9A            
DFA3: 1F 03          TFR     D,U             
DFA5: A6 E4          LDA     ,S              
DFA7: 94 88          ANDA    <$88            
DFA9: 43             COMA                    
DFAA: A4 84          ANDA    ,X              
DFAC: E6 E0          LDB     ,S+             
DFAE: 34 02          PSHS    A               
DFB0: C4 55          ANDB    #$55            
DFB2: D4 88          ANDB    <$88            
DFB4: EA E0          ORB     ,S+             
DFB6: E7 C4          STB     ,U              
DFB8: 96 A1          LDA     <$A1            
DFBA: 2A 09          BPL     $DFC5                          ; 
DFBC: 96 88          LDA     <$88            
DFBE: 26 05          BNE     $DFC5                          ; 
DFC0: EC A8 A0       LDD     $A0,Y           
DFC3: ED A4          STD     ,Y              
DFC5: 31 23          LEAY    3,Y             
DFC7: 0A 98          DEC     <$98            
DFC9: 26 B8          BNE     $DF83                          ; 
DFCB: 39             RTS                     
DFCC: 8E 28 08       LDX     #$2808          
DFCF: 96 A0          LDA     <$A0            
DFD1: 97 98          STA     <$98            
DFD3: EC 84          LDD     ,X              
DFD5: 90 8E          SUBA    <$8E            
DFD7: 2A 01          BPL     $DFDA                          ; 
DFD9: 40             NEGA                    
DFDA: 81 02          CMPA    #$02            
DFDC: 24 09          BCC     $DFE7                          ; 
DFDE: D0 8F          SUBB    <$8F            
DFE0: 2A 01          BPL     $DFE3                          ; 
DFE2: 50             NEGB                    
DFE3: C1 02          CMPB    #$02            
DFE5: 25 09          BCS     $DFF0                          ; 
DFE7: 30 03          LEAX    3,X             
DFE9: 0A 98          DEC     <$98            
DFEB: 26 E6          BNE     $DFD3                          ; 
DFED: 1C FE          ANDCC   #$FE            
DFEF: 39             RTS                     
DFF0: 1A 01          ORCC    #$01            
DFF2: 39             RTS                     

DFF3: FF FF FF       STU     $FFFF                          ; {hard:vectorReset} 
DFF6: FF FF FF       STU     $FFFF                          ; {hard:vectorReset} 
DFF9: FF FF FF       STU     $FFFF                          ; {hard:vectorReset} 
DFFC: FF FF FF       STU     $FFFF                          ; {hard:vectorReset} 
DFFF: FF 00 00       STU     $0000           
```
