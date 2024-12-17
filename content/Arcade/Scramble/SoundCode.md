![Scramble Sound](scramble.jpg)

>>> cpu Z80

>>> binary 0:roms/ot1.5c + roms/ot2.5d + roms/ot3.5e

>>> memoryTable ram 

[Sound RAM Usage](SoundRAMUse.md)

>>> memoryTable hard 

[Sound Hardware Info](SoundHardware.md)

```code

0000: C3 72 02        JP      $0272               ; {code.Initialize} Initialization

0003: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF              
0013: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF             
0023: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF            
0033: FF FF FF FF FF              
```

# ISR

```code
0038: 08              EX      AF,AF'              ; Swap ...
0039: D9              EXX                         ; ... registers
003A: 3E 0E           LD      A,$0E               
003C: D3 40           OUT     ($40),A             ; {hard.AY_DATA}
003E: DB 80           IN      A,($80)             ; {}
0040: B7              OR      A                   
0041: 28 13           JR      Z,$56               ; {}
0043: FE 30           CP      $30                 
0045: FA 64 00        JP      M,$0064             ; {}
0048: FE 40           CP      $40                 
004A: F2 6B 00        JP      P,$006B             ; {}
004D: D6 10           SUB     $10                 
004F: CD 6F 00        CALL    $006F               ; {}
0052: D9              EXX                         ; Restore ...
0053: 08              EX      AF,AF'              ; ... registers
0054: FB              EI                          ; Enable interrupts
0055: C9              RET                         ; Out

0056: 06 0C           LD      B,$0C               
0058: 21 00 80        LD      HL,$8000            
005B: 77              LD      (HL),A              
005C: 23              INC     HL                  
005D: 05              DEC     B                   
005E: 20 FB           JR      NZ,$5B              ; {}
0060: D9              EXX                         ; Restore ...
0061: 08              EX      AF,AF'              ; ... registers
0062: FB              EI                          ; Enable interrupts
0063: C9              RET                         ; Out

0064: CD E7 00        CALL    $00E7               ; {}
0067: D9              EXX                         ; Restore ...
0068: 08              EX      AF,AF'              ; ... registers
0069: FB              EI                          ; Enable interrupts
006A: C9              RET                         ; Out

006B: D9              EXX                         ; Restore ...
006C: 08              EX      AF,AF'              ; ... registers
006D: FB              EI                          ; Enable interrupts
006E: C9              RET                         ; Out

006F: CD A6 00        CALL    $00A6               ; {}
0072: B7              OR      A                   
0073: C8              RET     Z                   
0074: FE 01           CP      $01                 ; Voice 1?
0076: 28 15           JR      Z,$8D               ; {} Yes ... ??
0078: FE 02           CP      $02                 ; Voice 2?
007A: 28 16           JR      Z,$92               ; {}
007C: FE 03           CP      $03                 ; Voice 3?
007E: 28 17           JR      Z,$97               ; {}
0080: FE 04           CP      $04                 ; Voice 4?
0082: 28 18           JR      Z,$9C               ; {}
0084: FE 05           CP      $05                 ; Voice 5?
0086: 28 19           JR      Z,$A1               ; {}

0088: AF              XOR     A                   ; Must be voice 6
0089: 32 0A 80        LD      ($800A),A           
008C: C9              RET                         

008D: AF              XOR     A                   
008E: 32 00 80        LD      ($8000),A           
0091: C9              RET                         

0092: AF              XOR     A                   
0093: 32 02 80        LD      ($8002),A           
0096: C9              RET                         

0097: AF              XOR     A                   
0098: 32 04 80        LD      ($8004),A           
009B: C9              RET                         

009C: AF              XOR     A                   
009D: 32 06 80        LD      ($8006),A           
00A0: C9              RET                         

00A1: AF              XOR     A                   
00A2: 32 08 80        LD      ($8008),A           
00A5: C9              RET                         

00A6: 06 00           LD      B,$00               
00A8: 21 00 80        LD      HL,$8000            
00AB: BE              CP      (HL)                
00AC: 28 1B           JR      Z,$C9               ; {}
00AE: 23              INC     HL                  
00AF: 23              INC     HL                  
00B0: BE              CP      (HL)                
00B1: 28 1B           JR      Z,$CE               ; {}
00B3: 23              INC     HL                  
00B4: 23              INC     HL                  
00B5: BE              CP      (HL)                
00B6: 28 1B           JR      Z,$D3               ; {}
00B8: 23              INC     HL                  
00B9: 23              INC     HL                  
00BA: BE              CP      (HL)                
00BB: 28 1B           JR      Z,$D8               ; {}
00BD: 23              INC     HL                  
00BE: 23              INC     HL                  
00BF: BE              CP      (HL)                
00C0: 28 1B           JR      Z,$DD               ; {}
00C2: 23              INC     HL                  
00C3: 23              INC     HL                  
00C4: BE              CP      (HL)                
00C5: 28 1B           JR      Z,$E2               ; {}
00C7: AF              XOR     A                   
00C8: C9              RET                         
00C9: 23              INC     HL                  
00CA: 70              LD      (HL),B              
00CB: 3E 01           LD      A,$01               
00CD: C9              RET                         
00CE: 23              INC     HL                  
00CF: 70              LD      (HL),B              
00D0: 3E 02           LD      A,$02               
00D2: C9              RET                         
00D3: 23              INC     HL                  
00D4: 70              LD      (HL),B              
00D5: 3E 03           LD      A,$03               
00D7: C9              RET                         
00D8: 23              INC     HL                  
00D9: 70              LD      (HL),B              
00DA: 3E 04           LD      A,$04               
00DC: C9              RET                         
00DD: 23              INC     HL                  
00DE: 70              LD      (HL),B              
00DF: 3E 05           LD      A,$05               
00E1: C9              RET                         
00E2: 23              INC     HL                  
00E3: 70              LD      (HL),B              
00E4: 3E 06           LD      A,$06               
00E6: C9              RET                         

00E7: 32 1A 80        LD      ($801A),A           
00EA: CD A6 00        CALL    $00A6               ; {}
00ED: B7              OR      A                   
00EE: C0              RET     NZ                  
00EF: AF              XOR     A                   
00F0: CD A6 00        CALL    $00A6               ; {}
00F3: B7              OR      A                   
00F4: 20 73           JR      NZ,$169             ; {}
00F6: 3A 00 80        LD      A,($8000)           
00F9: CD F1 01        CALL    $01F1               ; {}
00FC: 32 12 80        LD      ($8012),A           
00FF: 3A 02 80        LD      A,($8002)           
0102: CD F1 01        CALL    $01F1               ; {}
0105: 32 13 80        LD      ($8013),A           
0108: 3A 04 80        LD      A,($8004)           
010B: CD F1 01        CALL    $01F1               ; {}
010E: 32 14 80        LD      ($8014),A           
0111: 3A 1A 80        LD      A,($801A)           
0114: CD F1 01        CALL    $01F1               ; {}
0117: 32 15 80        LD      ($8015),A           
011A: CD FA 01        CALL    $01FA               ; {}
011D: 32 17 80        LD      ($8017),A           
0120: 3A 06 80        LD      A,($8006)           
0123: CD F1 01        CALL    $01F1               ; {}
0126: 32 12 80        LD      ($8012),A           
0129: 3A 08 80        LD      A,($8008)           
012C: CD F1 01        CALL    $01F1               ; {}
012F: 32 13 80        LD      ($8013),A           
0132: 3A 0A 80        LD      A,($800A)           
0135: CD F1 01        CALL    $01F1               ; {}
0138: 32 14 80        LD      ($8014),A           
013B: CD FA 01        CALL    $01FA               ; {}
013E: 32 18 80        LD      ($8018),A           
0141: B7              OR      A                   
0142: 28 63           JR      Z,$1A7              ; {}
0144: 3A 17 80        LD      A,($8017)           
0147: B7              OR      A                   
0148: 28 79           JR      Z,$1C3              ; {}
014A: 3A 18 80        LD      A,($8018)           
014D: 21 06 80        LD      HL,$8006            
0150: CD E3 01        CALL    $01E3               ; {}
0153: CD F1 01        CALL    $01F1               ; {}
0156: 47              LD      B,A                 
0157: 3A 17 80        LD      A,($8017)           
015A: 21 00 80        LD      HL,$8000            
015D: CD E3 01        CALL    $01E3               ; {}
0160: CD F1 01        CALL    $01F1               ; {}
0163: B8              CP      B                   
0164: F2 C3 01        JP      P,$01C3             ; {}
0167: 18 3E           JR      $1A7                ; {}
0169: FE 01           CP      $01                 
016B: 28 17           JR      Z,$184              ; {}
016D: FE 02           CP      $02                 
016F: 28 1A           JR      Z,$18B              ; {}
0171: FE 03           CP      $03                 
0173: 28 1D           JR      Z,$192              ; {}
0175: FE 04           CP      $04                 
0177: 28 20           JR      Z,$199              ; {}
0179: FE 05           CP      $05                 
017B: 28 23           JR      Z,$1A0              ; {}
017D: 3A 1A 80        LD      A,($801A)           
0180: 32 0A 80        LD      ($800A),A           
0183: C9              RET                         
0184: 3A 1A 80        LD      A,($801A)           
0187: 32 00 80        LD      ($8000),A           
018A: C9              RET                         
018B: 3A 1A 80        LD      A,($801A)           
018E: 32 02 80        LD      ($8002),A           
0191: C9              RET                         
0192: 3A 1A 80        LD      A,($801A)           
0195: 32 04 80        LD      ($8004),A           
0198: C9              RET                         
0199: 3A 1A 80        LD      A,($801A)           
019C: 32 06 80        LD      ($8006),A           
019F: C9              RET                         
01A0: 3A 1A 80        LD      A,($801A)           
01A3: 32 08 80        LD      ($8008),A           
01A6: C9              RET                         
01A7: 3A 17 80        LD      A,($8017)           
01AA: B7              OR      A                   
01AB: C8              RET     Z                   
01AC: FE 01           CP      $01                 
01AE: 28 09           JR      Z,$1B9              ; {}
01B0: FE 02           CP      $02                 
01B2: 28 0A           JR      Z,$1BE              ; {}
01B4: 21 04 80        LD      HL,$8004            
01B7: 18 18           JR      $1D1                ; {}
01B9: 21 00 80        LD      HL,$8000            
01BC: 18 13           JR      $1D1                ; {}
01BE: 21 02 80        LD      HL,$8002            
01C1: 18 0E           JR      $1D1                ; {}
01C3: 3A 18 80        LD      A,($8018)           
01C6: FE 01           CP      $01                 
01C8: 28 0F           JR      Z,$1D9              ; {}
01CA: FE 02           CP      $02                 
01CC: 28 10           JR      Z,$1DE              ; {}
01CE: 21 0A 80        LD      HL,$800A            
01D1: 3A 1A 80        LD      A,($801A)           
01D4: 77              LD      (HL),A              
01D5: 23              INC     HL                  
01D6: 36 00           LD      (HL),$00            
01D8: C9              RET                         
01D9: 21 06 80        LD      HL,$8006            
01DC: 18 F3           JR      $1D1                ; {}
01DE: 21 08 80        LD      HL,$8008            
01E1: 18 EE           JR      $1D1                ; {}
01E3: FE 01           CP      $01                 
01E5: 28 08           JR      Z,$1EF              ; {}
01E7: 23              INC     HL                  
01E8: 23              INC     HL                  
01E9: FE 02           CP      $02                 
01EB: 28 02           JR      Z,$1EF              ; {}
01ED: 23              INC     HL                  
01EE: 23              INC     HL                  
01EF: 7E              LD      A,(HL)              
01F0: C9              RET                         
01F1: 21 42 02        LD      HL,$0242            
01F4: 5F              LD      E,A                 
01F5: 16 00           LD      D,$00               
01F7: 19              ADD     HL,DE               
01F8: 7E              LD      A,(HL)              
01F9: C9              RET                         
01FA: 3A 12 80        LD      A,($8012)           
01FD: 21 13 80        LD      HL,$8013            
0200: BE              CP      (HL)                
0201: FA 15 02        JP      M,$0215             ; {}
0204: 3A 14 80        LD      A,($8014)           
0207: BE              CP      (HL)                
0208: FA 34 02        JP      M,$0234             ; {}
020B: 3A 15 80        LD      A,($8015)           
020E: BE              CP      (HL)                
020F: FA 40 02        JP      M,$0240             ; {}
0212: 3E 02           LD      A,$02               
0214: C9              RET                         
0215: 21 14 80        LD      HL,$8014            
0218: BE              CP      (HL)                
0219: FA 26 02        JP      M,$0226             ; {}
021C: 3A 15 80        LD      A,($8015)           
021F: BE              CP      (HL)                
0220: FA 32 02        JP      M,$0232             ; {}
0223: 3E 03           LD      A,$03               
0225: C9              RET                         
0226: 21 15 80        LD      HL,$8015            
0229: BE              CP      (HL)                
022A: FA 2F 02        JP      M,$022F             ; {}
022D: AF              XOR     A                   
022E: C9              RET                         
022F: 3E 01           LD      A,$01               
0231: C9              RET                         
0232: AF              XOR     A                   
0233: C9              RET                         
0234: 21 15 80        LD      HL,$8015            
0237: BE              CP      (HL)                
0238: FA 3D 02        JP      M,$023D             ; {}
023B: AF              XOR     A                   
023C: C9              RET                         
023D: 3E 03           LD      A,$03               
023F: C9              RET                         
0240: AF              XOR     A                   
0241: C9              RET                         
0242: 00              NOP                         
0243: 01 02 03        LD      BC,$0302            
0246: 04              INC     B                   
0247: 05              DEC     B                   
0248: 06 07           LD      B,$07               
024A: 08              EX      AF,AF'              
024B: 09              ADD     HL,BC               
024C: 0A              LD      A,(BC)              
024D: 0B              DEC     BC                  
024E: 0C              INC     C                   
024F: 0D              DEC     C                   
0250: 0E 0F           LD      C,$0F               
0252: 10 11           DJNZ    $265                ; {}
0254: 12              LD      (DE),A              
0255: 13              INC     DE                  
0256: 14              INC     D                   
0257: 15              DEC     D                   
0258: 16 17           LD      D,$17               
025A: 18 19           JR      $275                ; {}
025C: 1A              LD      A,(DE)              
025D: 1B              DEC     DE                  
025E: 1C              INC     E                   
025F: 1D              DEC     E                   
0260: 1E 1F           LD      E,$1F               
0262: 20 21           JR      NZ,$285             ; {}
0264: 22 23 24        LD      ($2423),HL          
0267: 25              DEC     H                   
0268: 26 27           LD      H,$27               
026A: 28 29           JR      Z,$295              ; {}
026C: 2A 2B 2C        LD      HL,($2C2B)          
026F: 2D              DEC     L                   
0270: 2E 2F           LD      L,$2F               
```

# Initialize

```code
Initialize:
0272: 06 00           LD      B,$00               
0274: 21 00 80        LD      HL,$8000            
0277: 70              LD      (HL),B              
0278: 23              INC     HL                  
0279: 7C              LD      A,H                 
027A: FE 84           CP      $84                 
027C: 20 F9           JR      NZ,$277             ; {}
027E: 31 00 84        LD      SP,$8400            
0281: ED 56           IM      1                   
0283: 21 00 90        LD      HL,$9000            
0286: 22 0C 80        LD      ($800C),HL          
0289: 77              LD      (HL),A              
028A: 3E 07           LD      A,$07               
028C: D3 40           OUT     ($40),A             ; {hard.AY_DATA}
028E: 3E 3F           LD      A,$3F               
0290: 32 0E 80        LD      ($800E),A           
0293: D3 80           OUT     ($80),A             ; {hard.AY_ADDR}
0295: 3E 07           LD      A,$07               
0297: D3 10           OUT     ($10),A             ; {}
0299: 3E 3F           LD      A,$3F               
029B: 32 0F 80        LD      ($800F),A           
029E: D3 20           OUT     ($20),A             ; {}
02A0: CD 2D 04        CALL    $042D               ; {}
02A3: CD 35 04        CALL    $0435               ; {}
02A6: CD 3D 04        CALL    $043D               ; {}
02A9: CD 45 04        CALL    $0445               ; {}
02AC: CD 4D 04        CALL    $044D               ; {}
02AF: CD 55 04        CALL    $0455               ; {}
```

# Main loop

```code
; Wait for 0-to-1 transition on 350Hz clock
02B2: FB              EI                          
02B3: 3E 0F           LD      A,$0F               ; AY3 IO Port B
02B5: D3 40           OUT     ($40),A             ; {hard.AY_DATA} Latch address
02B7: DB 80           IN      A,($80)             ; {} Read value
02B9: E6 80           AND     $80                 ; Upper bit (350Hz)
02BB: 20 F6           JR      NZ,$2B3             ; {} Wait for the 0
02BD: 3E 0F           LD      A,$0F               ; AY3 IO Port B
02BF: D3 40           OUT     ($40),A             ; {hard.AY_DATA} Latch address
02C1: DB 80           IN      A,($80)             ; {} Read value
02C3: E6 80           AND     $80                 ; Upper bit (350Hz)
02C5: 28 F6           JR      Z,$2BD              ; {} Wait for the 1
;
02C7: F3              DI                          
02C8: 3E 01           LD      A,$01               ; Voice 1
02CA: 32 10 80        LD      ($8010),A           ; {ram.curVoice}
02CD: 3A 01 80        LD      A,($8001)           
02D0: B7              OR      A                   
02D1: CA 4B 03        JP      Z,$034B             ; {}
02D4: 3A 00 80        LD      A,($8000)           
02D7: CD 04 08        CALL    $0804               ; {}
;
02DA: FB              EI                          
02DB: 00              NOP                         
02DC: 00              NOP                         
02DD: F3              DI                          
;
02DE: 3E 02           LD      A,$02               ; Voice 2
02E0: 32 10 80        LD      ($8010),A           ; {ram.curVoice}
02E3: 3A 03 80        LD      A,($8003)           
02E6: B7              OR      A                   
02E7: CA 54 03        JP      Z,$0354             ; {}
02EA: 3A 02 80        LD      A,($8002)           
02ED: CD 04 08        CALL    $0804               ; {}
;
02F0: FB              EI                          
02F1: 00              NOP                         
02F2: 00              NOP                         
02F3: F3              DI                          
;
02F4: 3E 03           LD      A,$03               ; Voice 3
02F6: 32 10 80        LD      ($8010),A           ; {ram.curVoice}
02F9: 3A 05 80        LD      A,($8005)           
02FC: B7              OR      A                   
02FD: CA 5D 03        JP      Z,$035D             ; {}
0300: 3A 04 80        LD      A,($8004)           
0303: CD 04 08        CALL    $0804               ; {}
;
0306: FB              EI                          
0307: 00              NOP                         
0308: 00              NOP                         
0309: F3              DI                          
;
030A: 3E 04           LD      A,$04               ; Voice 4
030C: 32 10 80        LD      ($8010),A           ; {ram.curVoice}
030F: 3A 07 80        LD      A,($8007)           
0312: B7              OR      A                   
0313: CA 66 03        JP      Z,$0366             ; {}
0316: 3A 06 80        LD      A,($8006)           
0319: CD 04 08        CALL    $0804               ; {}
;
031C: FB              EI                          
031D: 00              NOP                         
031E: 00              NOP                         
031F: F3              DI                          
;
0320: 3E 05           LD      A,$05               ; Voice 5
0322: 32 10 80        LD      ($8010),A           ; {ram.curVoice}
0325: 3A 09 80        LD      A,($8009)           
0328: B7              OR      A                   
0329: CA 6F 03        JP      Z,$036F             ; {}
032C: 3A 08 80        LD      A,($8008)           
032F: CD 04 08        CALL    $0804               ; {}
;
0332: FB              EI                          
0333: 00              NOP                         
0334: 00              NOP                         
0335: F3              DI                          
;
0336: 3E 06           LD      A,$06               ; Voice 6
0338: 32 10 80        LD      ($8010),A           ; {ram.curVoice}
033B: 3A 0B 80        LD      A,($800B)           
033E: B7              OR      A                   
033F: CA 78 03        JP      Z,$0378             ; {}
0342: 3A 0A 80        LD      A,($800A)           
0345: CD 04 08        CALL    $0804               ; {}
0348: C3 B2 02        JP      $02B2               ; {} Back to top of main loop
;
034B: 3A 00 80        LD      A,($8000)           
034E: CD 81 03        CALL    $0381               ; {}
0351: C3 DA 02        JP      $02DA               ; {} Back to main loop voice 2
;
0354: 3A 02 80        LD      A,($8002)           
0357: CD 81 03        CALL    $0381               ; {}
035A: C3 F0 02        JP      $02F0               ; {} Back to main loop voice 3
;
035D: 3A 04 80        LD      A,($8004)           
0360: CD 81 03        CALL    $0381               ; {}
0363: C3 06 03        JP      $0306               ; {} Back to main loop voice 4
;
0366: 3A 06 80        LD      A,($8006)           
0369: CD 81 03        CALL    $0381               ; {}
036C: C3 1C 03        JP      $031C               ; {} Back to main loop voice 5
;
036F: 3A 08 80        LD      A,($8008)           
0372: CD 81 03        CALL    $0381               ; {}
0375: C3 32 03        JP      $0332               ; {} Back to main loop voice 6
;
0378: 3A 0A 80        LD      A,($800A)           
037B: CD 81 03        CALL    $0381               ; {}
037E: C3 B2 02        JP      $02B2               ; {} Back to top of loop voice 1
;
0381: 21 92 03        LD      HL,$0392            ; Retrun to ...
0384: E5              PUSH    HL                  ; ... 0392
0385: 87              ADD     A,A                 
0386: 5F              LD      E,A                 
0387: 16 00           LD      D,$00               
0389: 21 CD 03        LD      HL,$03CD            
038C: 19              ADD     HL,DE               
038D: 5E              LD      E,(HL)              
038E: 23              INC     HL                  
038F: 56              LD      D,(HL)              
0390: EB              EX      DE,HL               
0391: E9              JP      (HL)                ; Call the function (returns to next line)
0392: 3A 10 80        LD      A,($8010)           ; {ram.curVoice}
0395: FE 01           CP      $01                 
0397: 28 16           JR      Z,$3AF              ; {}
0399: FE 02           CP      $02                 
039B: 28 18           JR      Z,$3B5              ; {}
039D: FE 03           CP      $03                 
039F: 28 1A           JR      Z,$3BB              ; {}
03A1: FE 04           CP      $04                 
03A3: 28 1C           JR      Z,$3C1              ; {}
03A5: FE 05           CP      $05                 
03A7: 28 1E           JR      Z,$3C7              ; {}
;
03A9: 3E 01           LD      A,$01               
03AB: 32 0B 80        LD      ($800B),A           
03AE: C9              RET                         
;
03AF: 3E 01           LD      A,$01               
03B1: 32 01 80        LD      ($8001),A           
03B4: C9              RET                         
;
03B5: 3E 01           LD      A,$01               
03B7: 32 03 80        LD      ($8003),A           
03BA: C9              RET                         
;
03BB: 3E 01           LD      A,$01               
03BD: 32 05 80        LD      ($8005),A           
03C0: C9              RET                         
;
03C1: 3E 01           LD      A,$01               
03C3: 32 07 80        LD      ($8007),A           
03C6: C9              RET                         
;
03C7: 3E 01           LD      A,$01               
03C9: 32 09 80        LD      ($8009),A           
03CC: C9              RET                         

03CD: 5D              LD      E,L                 
03CE: 04              INC     B                   
03CF: C0              RET     NZ                  
03D0: 08              EX      AF,AF'              
03D1: 3C              INC     A                   
03D2: 09              ADD     HL,BC               
03D3: B8              CP      B                   
03D4: 09              ADD     HL,BC               
03D5: 34              INC     (HL)                
03D6: 0A              LD      A,(BC)              
03D7: B0              OR      B                   
03D8: 0A              LD      A,(BC)              
03D9: F9              LD      SP,HL               
03DA: 0C              INC     C                   
03DB: 1D              DEC     E                   
03DC: 12              LD      (DE),A              
03DD: A9              XOR     C                   
03DE: 13              INC     DE                  
03DF: B9              CP      C                   
03E0: 0D              DEC     C                   
03E1: C7              RST     0X00                
03E2: 0D              DEC     C                   
03E3: 2E 10           LD      L,$10               
03E5: 3C              INC     A                   
03E6: 10 43           DJNZ    $42B                ; {}
03E8: 10 B2           DJNZ    $39C                ; {}
03EA: 10 C0           DJNZ    $3AC                ; {}
03EC: 10 00           DJNZ    $3EE                ; {}
03EE: 00              NOP                         
03EF: 00              NOP                         
03F0: 00              NOP                         
03F1: 00              NOP                         
03F2: 11 3C 0B        LD      DE,$0B3C            
03F5: E3              EX      (SP),HL             
03F6: 0B              DEC     BC                  
03F7: 6D              LD      L,L                 
03F8: 0C              INC     C                   
03F9: 00              NOP                         
03FA: 00              NOP                         
03FB: 00              NOP                         
03FC: 00              NOP                         
03FD: 00              NOP                         
03FE: 00              NOP                         
03FF: 00              NOP                         
0400: 00              NOP                         
0401: 00              NOP                         
0402: 00              NOP                         
0403: 00              NOP                         
0404: 00              NOP                         
0405: 00              NOP                         
0406: 00              NOP                         
0407: 00              NOP                         
0408: 00              NOP                         
0409: 00              NOP                         
040A: 00              NOP                         
040B: 00              NOP                         
040C: 00              NOP                         
040D: 7A              LD      A,D                 
040E: 0D              DEC     C                   
040F: 80              ADD     A,B                 
0410: 11 19 12        LD      DE,$1219            
0413: B6              OR      (HL)                
0414: 12              LD      (DE),A              
0415: 34              INC     (HL)                
0416: 13              INC     DE                  
0417: 00              NOP                         
0418: 00              NOP                         
0419: 00              NOP                         
041A: 00              NOP                         
041B: 00              NOP                         
041C: 00              NOP                         
041D: 00              NOP                         
041E: 00              NOP                         
041F: 00              NOP                         
0420: 00              NOP                         
0421: 00              NOP                         
0422: 00              NOP                         
0423: 00              NOP                         
0424: 00              NOP                         
0425: 00              NOP                         
0426: 00              NOP                         
0427: 00              NOP                         
0428: 00              NOP                         
0429: 00              NOP                         
042A: 00              NOP                         
042B: 00              NOP                         
042C: 00              NOP                         
042D: 3E 08           LD      A,$08               
042F: D3 40           OUT     ($40),A             ; {hard.AY_DATA}
0431: AF              XOR     A                   
0432: D3 80           OUT     ($80),A             ; {hard.AY_ADDR}
0434: C9              RET                         
0435: 3E 09           LD      A,$09               
0437: D3 40           OUT     ($40),A             ; {hard.AY_DATA}
0439: AF              XOR     A                   
043A: D3 80           OUT     ($80),A             ; {hard.AY_ADDR}
043C: C9              RET                         
043D: 3E 0A           LD      A,$0A               
043F: D3 40           OUT     ($40),A             ; {hard.AY_DATA}
0441: AF              XOR     A                   
0442: D3 80           OUT     ($80),A             ; {hard.AY_ADDR}
0444: C9              RET                         
0445: 3E 08           LD      A,$08               
0447: D3 10           OUT     ($10),A             ; {}
0449: AF              XOR     A                   
044A: D3 20           OUT     ($20),A             ; {}
044C: C9              RET                         
044D: 3E 09           LD      A,$09               
044F: D3 10           OUT     ($10),A             ; {}
0451: AF              XOR     A                   
0452: D3 20           OUT     ($20),A             ; {}
0454: C9              RET                         
0455: 3E 0A           LD      A,$0A               
0457: D3 10           OUT     ($10),A             ; {}
0459: AF              XOR     A                   
045A: D3 20           OUT     ($20),A             ; {}
045C: C9              RET                         
045D: 3A 10 80        LD      A,($8010)           ; {ram.curVoice}
0460: FE 01           CP      $01                 
0462: 28 19           JR      Z,$47D              ; {}
0464: FE 02           CP      $02                 
0466: 28 1E           JR      Z,$486              ; {}
0468: FE 03           CP      $03                 
046A: 28 23           JR      Z,$48F              ; {}
046C: FE 04           CP      $04                 
046E: 28 28           JR      Z,$498              ; {}
0470: FE 05           CP      $05                 
0472: 28 2D           JR      Z,$4A1              ; {}
0474: 06 24           LD      B,$24               
0476: CD B8 04        CALL    $04B8               ; {}
0479: CD 55 04        CALL    $0455               ; {}
047C: C9              RET                         
047D: 06 09           LD      B,$09               
047F: CD AA 04        CALL    $04AA               ; {}
0482: CD 2D 04        CALL    $042D               ; {}
0485: C9              RET                         
0486: 06 12           LD      B,$12               
0488: CD AA 04        CALL    $04AA               ; {}
048B: CD 35 04        CALL    $0435               ; {}
048E: C9              RET                         
048F: 06 24           LD      B,$24               
0491: CD AA 04        CALL    $04AA               ; {}
0494: CD 3D 04        CALL    $043D               ; {}
0497: C9              RET                         
0498: 06 09           LD      B,$09               
049A: CD B8 04        CALL    $04B8               ; {}
049D: CD 45 04        CALL    $0445               ; {}
04A0: C9              RET                         
04A1: 06 12           LD      B,$12               
04A3: CD B8 04        CALL    $04B8               ; {}
04A6: CD 4D 04        CALL    $044D               ; {}
04A9: C9              RET                         
04AA: 3E 07           LD      A,$07               
04AC: D3 40           OUT     ($40),A             ; {hard.AY_DATA}
04AE: 3A 0E 80        LD      A,($800E)           
04B1: B0              OR      B                   
04B2: 32 0E 80        LD      ($800E),A           
04B5: D3 80           OUT     ($80),A             ; {hard.AY_ADDR}
04B7: C9              RET                         
04B8: 3E 07           LD      A,$07               
04BA: D3 10           OUT     ($10),A             ; {}
04BC: 3A 0F 80        LD      A,($800F)           
04BF: B0              OR      B                   
04C0: 32 0F 80        LD      ($800F),A           
04C3: D3 20           OUT     ($20),A             ; {}
04C5: C9              RET                         
04C6: 3A 10 80        LD      A,($8010)           ; {ram.curVoice}
04C9: FE 01           CP      $01                 
04CB: 28 20           JR      Z,$4ED              ; {}
04CD: FE 02           CP      $02                 
04CF: 28 2C           JR      Z,$4FD              ; {}
04D1: FE 03           CP      $03                 
04D3: 28 2C           JR      Z,$501              ; {}
04D5: FE 04           CP      $04                 
04D7: 28 2C           JR      Z,$505              ; {}
04D9: FE 05           CP      $05                 
04DB: 28 2C           JR      Z,$509              ; {}
04DD: 06 04           LD      B,$04               
04DF: 78              LD      A,B                 
04E0: D3 10           OUT     ($10),A             ; {}
04E2: 7D              LD      A,L                 
04E3: D3 20           OUT     ($20),A             ; {}
04E5: 04              INC     B                   
04E6: 78              LD      A,B                 
04E7: D3 10           OUT     ($10),A             ; {}
04E9: 7C              LD      A,H                 
04EA: D3 20           OUT     ($20),A             ; {}
04EC: C9              RET                         
04ED: 06 00           LD      B,$00               
04EF: 78              LD      A,B                 
04F0: D3 40           OUT     ($40),A             ; {hard.AY_DATA}
04F2: 7D              LD      A,L                 
04F3: D3 80           OUT     ($80),A             ; {hard.AY_ADDR}
04F5: 04              INC     B                   
04F6: 78              LD      A,B                 
04F7: D3 40           OUT     ($40),A             ; {hard.AY_DATA}
04F9: 7C              LD      A,H                 
04FA: D3 80           OUT     ($80),A             ; {hard.AY_ADDR}
04FC: C9              RET                         
04FD: 06 02           LD      B,$02               
04FF: 18 EE           JR      $4EF                ; {}
0501: 06 04           LD      B,$04               
0503: 18 EA           JR      $4EF                ; {}
0505: 06 00           LD      B,$00               
0507: 18 D6           JR      $4DF                ; {}
0509: 06 02           LD      B,$02               
050B: 18 D2           JR      $4DF                ; {}
050D: 3A 10 80        LD      A,($8010)           ; {ram.curVoice}
0510: FE 01           CP      $01                 
0512: 28 18           JR      Z,$52C              ; {}
0514: FE 02           CP      $02                 
0516: 28 1C           JR      Z,$534              ; {}
0518: FE 03           CP      $03                 
051A: 28 1E           JR      Z,$53A              ; {}
051C: FE 04           CP      $04                 
051E: 28 20           JR      Z,$540              ; {}
0520: FE 05           CP      $05                 
0522: 28 22           JR      Z,$546              ; {}
0524: 16 FB           LD      D,$FB               
0526: 1E 20           LD      E,$20               
0528: CD 71 05        CALL    $0571               ; {}
052B: C9              RET                         
052C: 16 FE           LD      D,$FE               
052E: 1E 08           LD      E,$08               
0530: CD 62 05        CALL    $0562               ; {}
0533: C9              RET                         
0534: 16 FD           LD      D,$FD               
0536: 1E 10           LD      E,$10               
0538: 18 F6           JR      $530                ; {}
053A: 16 FB           LD      D,$FB               
053C: 1E 20           LD      E,$20               
053E: 18 F0           JR      $530                ; {}
0540: 16 FE           LD      D,$FE               
0542: 1E 08           LD      E,$08               
0544: 18 E2           JR      $528                ; {}
0546: 16 FD           LD      D,$FD               
0548: 1E 10           LD      E,$10               
054A: 18 DC           JR      $528                ; {}
054C: 3A 10 80        LD      A,($8010)           ; {ram.curVoice}
054F: FE 04           CP      $04                 
0551: FA 5B 05        JP      M,$055B             ; {}
0554: 7A              LD      A,D                 
0555: D3 10           OUT     ($10),A             ; {}
0557: 7B              LD      A,E                 
0558: D3 20           OUT     ($20),A             ; {}
055A: C9              RET                         
055B: 7A              LD      A,D                 
055C: D3 40           OUT     ($40),A             ; {hard.AY_DATA}
055E: 7B              LD      A,E                 
055F: D3 80           OUT     ($80),A             ; {hard.AY_ADDR}
0561: C9              RET                         
0562: 3E 07           LD      A,$07               
0564: D3 40           OUT     ($40),A             ; {hard.AY_DATA}
0566: 3A 0E 80        LD      A,($800E)           
0569: A2              AND     D                   
056A: B3              OR      E                   
056B: 32 0E 80        LD      ($800E),A           
056E: D3 80           OUT     ($80),A             ; {hard.AY_ADDR}
0570: C9              RET                         
0571: 3E 07           LD      A,$07               
0573: D3 10           OUT     ($10),A             ; {}
0575: 3A 0F 80        LD      A,($800F)           
0578: A2              AND     D                   
0579: B3              OR      E                   
057A: 32 0F 80        LD      ($800F),A           
057D: D3 20           OUT     ($20),A             ; {}
057F: C9              RET                         
0580: 3A 10 80        LD      A,($8010)           ; {ram.curVoice}
0583: FE 01           CP      $01                 
0585: 28 18           JR      Z,$59F              ; {}
0587: FE 02           CP      $02                 
0589: 28 1C           JR      Z,$5A7              ; {}
058B: FE 03           CP      $03                 
058D: 28 1E           JR      Z,$5AD              ; {}
058F: FE 04           CP      $04                 
0591: 28 20           JR      Z,$5B3              ; {}
0593: FE 05           CP      $05                 
0595: 28 22           JR      Z,$5B9              ; {}
0597: 16 DF           LD      D,$DF               
0599: 1E 04           LD      E,$04               
059B: CD 71 05        CALL    $0571               ; {}
059E: C9              RET                         
059F: 16 F7           LD      D,$F7               
05A1: 1E 01           LD      E,$01               
05A3: CD 62 05        CALL    $0562               ; {}
05A6: C9              RET                         
05A7: 16 EF           LD      D,$EF               
05A9: 1E 02           LD      E,$02               
05AB: 18 F6           JR      $5A3                ; {}
05AD: 16 DF           LD      D,$DF               
05AF: 1E 04           LD      E,$04               
05B1: 18 F0           JR      $5A3                ; {}
05B3: 16 F7           LD      D,$F7               
05B5: 1E 01           LD      E,$01               
05B7: 18 E2           JR      $59B                ; {}
05B9: 16 EF           LD      D,$EF               
05BB: 1E 02           LD      E,$02               
05BD: 18 DC           JR      $59B                ; {}
05BF: 3A 10 80        LD      A,($8010)           ; {ram.curVoice}
05C2: FE 01           CP      $01                 
05C4: 28 18           JR      Z,$5DE              ; {}
05C6: FE 02           CP      $02                 
05C8: 28 1C           JR      Z,$5E6              ; {}
05CA: FE 03           CP      $03                 
05CC: 28 1E           JR      Z,$5EC              ; {}
05CE: FE 04           CP      $04                 
05D0: 28 20           JR      Z,$5F2              ; {}
05D2: FE 05           CP      $05                 
05D4: 28 22           JR      Z,$5F8              ; {}
05D6: 16 DB           LD      D,$DB               
05D8: 1E 00           LD      E,$00               
05DA: CD 71 05        CALL    $0571               ; {}
05DD: C9              RET                         
05DE: 16 F6           LD      D,$F6               
05E0: 1E 00           LD      E,$00               
05E2: CD 62 05        CALL    $0562               ; {}
05E5: C9              RET                         
05E6: 16 ED           LD      D,$ED               
05E8: 1E 00           LD      E,$00               
05EA: 18 F6           JR      $5E2                ; {}
05EC: 16 DB           LD      D,$DB               
05EE: 1E 00           LD      E,$00               
05F0: 18 F0           JR      $5E2                ; {}
05F2: 16 F6           LD      D,$F6               
05F4: 1E 00           LD      E,$00               
05F6: 18 E2           JR      $5DA                ; {}
05F8: 16 ED           LD      D,$ED               
05FA: 1E 00           LD      E,$00               
05FC: 18 DC           JR      $5DA                ; {}
05FE: 3A 10 80        LD      A,($8010)           ; {ram.curVoice}
0601: FE 01           CP      $01                 
0603: 28 18           JR      Z,$61D              ; {}
0605: FE 02           CP      $02                 
0607: 28 1C           JR      Z,$625              ; {}
0609: FE 03           CP      $03                 
060B: 28 1C           JR      Z,$629              ; {}
060D: FE 04           CP      $04                 
060F: 28 1C           JR      Z,$62D              ; {}
0611: FE 05           CP      $05                 
0613: 28 1C           JR      Z,$631              ; {}
0615: 3E 0A           LD      A,$0A               
0617: D3 10           OUT     ($10),A             ; {}
0619: 78              LD      A,B                 
061A: D3 20           OUT     ($20),A             ; {}
061C: C9              RET                         
061D: 3E 08           LD      A,$08               
061F: D3 40           OUT     ($40),A             ; {hard.AY_DATA}
0621: 78              LD      A,B                 
0622: D3 80           OUT     ($80),A             ; {hard.AY_ADDR}
0624: C9              RET                         
0625: 3E 09           LD      A,$09               
0627: 18 F6           JR      $61F                ; {}
0629: 3E 0A           LD      A,$0A               
062B: 18 F2           JR      $61F                ; {}
062D: 3E 08           LD      A,$08               
062F: 18 E6           JR      $617                ; {}
0631: 3E 09           LD      A,$09               
0633: 18 E2           JR      $617                ; {}
0635: 3A 10 80        LD      A,($8010)           ; {ram.curVoice}
0638: FE 04           CP      $04                 
063A: FA 44 06        JP      M,$0644             ; {}
063D: 7A              LD      A,D                 
063E: D3 10           OUT     ($10),A             ; {}
0640: DB 20           IN      A,($20)             ; {}
0642: 5F              LD      E,A                 
0643: C9              RET                         
0644: 7A              LD      A,D                 
0645: D3 40           OUT     ($40),A             ; {hard.AY_DATA}
0647: DB 80           IN      A,($80)             ; {}
0649: 5F              LD      E,A                 
064A: C9              RET                         
064B: 3A 10 80        LD      A,($8010)           ; {ram.curVoice}
064E: FE 01           CP      $01                 
0650: 28 17           JR      Z,$669              ; {}
0652: FE 02           CP      $02                 
0654: 28 1A           JR      Z,$670              ; {}
0656: FE 03           CP      $03                 
0658: 28 1A           JR      Z,$674              ; {}
065A: FE 04           CP      $04                 
065C: 28 1A           JR      Z,$678              ; {}
065E: FE 05           CP      $05                 
0660: 28 1A           JR      Z,$67C              ; {}
0662: 3E 0A           LD      A,$0A               
0664: D3 10           OUT     ($10),A             ; {}
0666: DB 20           IN      A,($20)             ; {}
0668: C9              RET                         
0669: 3E 08           LD      A,$08               
066B: D3 40           OUT     ($40),A             ; {hard.AY_DATA}
066D: DB 80           IN      A,($80)             ; {}
066F: C9              RET                         
0670: 3E 09           LD      A,$09               
0672: 18 F7           JR      $66B                ; {}
0674: 3E 0A           LD      A,$0A               
0676: 18 F3           JR      $66B                ; {}
0678: 3E 08           LD      A,$08               
067A: 18 E8           JR      $664                ; {}
067C: 3E 09           LD      A,$09               
067E: 18 E4           JR      $664                ; {}
0680: 3A 10 80        LD      A,($8010)           ; {ram.curVoice}
0683: FE 01           CP      $01                 
0685: 28 20           JR      Z,$6A7              ; {}
0687: FE 02           CP      $02                 
0689: 28 2C           JR      Z,$6B7              ; {}
068B: FE 03           CP      $03                 
068D: 28 2C           JR      Z,$6BB              ; {}
068F: FE 04           CP      $04                 
0691: 28 2C           JR      Z,$6BF              ; {}
0693: FE 05           CP      $05                 
0695: 28 2C           JR      Z,$6C3              ; {}
0697: 06 04           LD      B,$04               
0699: 78              LD      A,B                 
069A: D3 10           OUT     ($10),A             ; {}
069C: DB 20           IN      A,($20)             ; {}
069E: 6F              LD      L,A                 
069F: 04              INC     B                   
06A0: 78              LD      A,B                 
06A1: D3 10           OUT     ($10),A             ; {}
06A3: DB 20           IN      A,($20)             ; {}
06A5: 67              LD      H,A                 
06A6: C9              RET                         
06A7: 06 00           LD      B,$00               
06A9: 78              LD      A,B                 
06AA: D3 40           OUT     ($40),A             ; {hard.AY_DATA}
06AC: DB 80           IN      A,($80)             ; {}
06AE: 6F              LD      L,A                 
06AF: 04              INC     B                   
06B0: 78              LD      A,B                 
06B1: D3 40           OUT     ($40),A             ; {hard.AY_DATA}
06B3: DB 80           IN      A,($80)             ; {}
06B5: 67              LD      H,A                 
06B6: C9              RET                         
06B7: 06 02           LD      B,$02               
06B9: 18 EE           JR      $6A9                ; {}
06BB: 06 04           LD      B,$04               
06BD: 18 EA           JR      $6A9                ; {}
06BF: 06 00           LD      B,$00               
06C1: 18 D6           JR      $699                ; {}
06C3: 06 02           LD      B,$02               
06C5: 18 D2           JR      $699                ; {}
06C7: 3A 10 80        LD      A,($8010)           ; {ram.curVoice}
06CA: FE 04           CP      $04                 
06CC: 28 21           JR      Z,$6EF              ; {}
06CE: FE 05           CP      $05                 
06D0: 28 22           JR      Z,$6F4              ; {}
06D2: FE 06           CP      $06                 
06D4: 28 23           JR      Z,$6F9              ; {}
06D6: FE 01           CP      $01                 
06D8: 28 24           JR      Z,$6FE              ; {}
06DA: FE 02           CP      $02                 
06DC: 28 25           JR      Z,$703              ; {}
06DE: 11 FF F3        LD      DE,$F3FF            
06E1: 2A 0C 80        LD      HL,($800C)          
06E4: 7A              LD      A,D                 
06E5: A4              AND     H                   
06E6: 67              LD      H,A                 
06E7: 7B              LD      A,E                 
06E8: A5              AND     L                   
06E9: 6F              LD      L,A                 
06EA: 22 0C 80        LD      ($800C),HL          
06ED: 77              LD      (HL),A              
06EE: C9              RET                         
06EF: 11 FC FF        LD      DE,$FFFC            
06F2: 18 ED           JR      $6E1                ; {}
06F4: 11 F3 FF        LD      DE,$FFF3            
06F7: 18 E8           JR      $6E1                ; {}
06F9: 11 CF FF        LD      DE,$FFCF            
06FC: 18 E3           JR      $6E1                ; {}
06FE: 11 3F FF        LD      DE,$FF3F            
0701: 18 DE           JR      $6E1                ; {}
0703: 11 FF FC        LD      DE,$FCFF            
0706: 18 D9           JR      $6E1                ; {}
0708: 3A 10 80        LD      A,($8010)           ; {ram.curVoice}
070B: FE 04           CP      $04                 
070D: 28 20           JR      Z,$72F              ; {}
070F: FE 05           CP      $05                 
0711: 28 21           JR      Z,$734              ; {}
0713: FE 06           CP      $06                 
0715: 28 22           JR      Z,$739              ; {}
0717: FE 01           CP      $01                 
0719: 28 23           JR      Z,$73E              ; {}
071B: FE 02           CP      $02                 
071D: 28 24           JR      Z,$743              ; {}
071F: 11 FF F3        LD      DE,$F3FF            
0722: 2A 0C 80        LD      HL,($800C)          
0725: 7A              LD      A,D                 
0726: A4              AND     H                   
0727: 67              LD      H,A                 
0728: 7B              LD      A,E                 
0729: A5              AND     L                   
072A: 6F              LD      L,A                 
072B: 22 0C 80        LD      ($800C),HL          
072E: C9              RET                         
072F: 11 FC FF        LD      DE,$FFFC            
0732: 18 EE           JR      $722                ; {}
0734: 11 F3 FF        LD      DE,$FFF3            
0737: 18 E9           JR      $722                ; {}
0739: 11 CF FF        LD      DE,$FFCF            
073C: 18 E4           JR      $722                ; {}
073E: 11 3F FF        LD      DE,$FF3F            
0741: 18 DF           JR      $722                ; {}
0743: 11 FF FC        LD      DE,$FCFF            
0746: 18 DA           JR      $722                ; {}
0748: CD 08 07        CALL    $0708               ; {}
074B: 3A 10 80        LD      A,($8010)           ; {ram.curVoice}
074E: FE 04           CP      $04                 
0750: 28 17           JR      Z,$769              ; {}
0752: FE 05           CP      $05                 
0754: 28 18           JR      Z,$76E              ; {}
0756: FE 06           CP      $06                 
0758: 28 19           JR      Z,$773              ; {}
075A: FE 01           CP      $01                 
075C: 28 1A           JR      Z,$778              ; {}
075E: FE 02           CP      $02                 
0760: 28 1B           JR      Z,$77D              ; {}
0762: 11 00 08        LD      DE,$0800            
0765: CD F6 07        CALL    $07F6               ; {}
0768: C9              RET                         
0769: 11 02 00        LD      DE,$0002            
076C: 18 F7           JR      $765                ; {}
076E: 11 08 00        LD      DE,$0008            
0771: 18 F2           JR      $765                ; {}
0773: 11 20 00        LD      DE,$0020            
0776: 18 ED           JR      $765                ; {}
0778: 11 80 00        LD      DE,$0080            
077B: 18 E8           JR      $765                ; {}
077D: 11 00 02        LD      DE,$0200            
0780: 18 E3           JR      $765                ; {}
0782: CD 08 07        CALL    $0708               ; {}
0785: 3A 10 80        LD      A,($8010)           ; {ram.curVoice}
0788: FE 04           CP      $04                 
078A: 28 17           JR      Z,$7A3              ; {}
078C: FE 05           CP      $05                 
078E: 28 18           JR      Z,$7A8              ; {}
0790: FE 06           CP      $06                 
0792: 28 19           JR      Z,$7AD              ; {}
0794: FE 01           CP      $01                 
0796: 28 1A           JR      Z,$7B2              ; {}
0798: FE 02           CP      $02                 
079A: 28 1B           JR      Z,$7B7              ; {}
079C: 11 00 04        LD      DE,$0400            
079F: CD F6 07        CALL    $07F6               ; {}
07A2: C9              RET                         
07A3: 11 01 00        LD      DE,$0001            
07A6: 18 F7           JR      $79F                ; {}
07A8: 11 04 00        LD      DE,$0004            
07AB: 18 F2           JR      $79F                ; {}
07AD: 11 10 00        LD      DE,$0010            
07B0: 18 ED           JR      $79F                ; {}
07B2: 11 40 00        LD      DE,$0040            
07B5: 18 E8           JR      $79F                ; {}
07B7: 11 00 01        LD      DE,$0100            
07BA: 18 E3           JR      $79F                ; {}
07BC: CD 08 07        CALL    $0708               ; {}
07BF: 3A 10 80        LD      A,($8010)           ; {ram.curVoice}
07C2: FE 04           CP      $04                 
07C4: 28 17           JR      Z,$7DD              ; {}
07C6: FE 05           CP      $05                 
07C8: 28 18           JR      Z,$7E2              ; {}
07CA: FE 06           CP      $06                 
07CC: 28 19           JR      Z,$7E7              ; {}
07CE: FE 01           CP      $01                 
07D0: 28 1A           JR      Z,$7EC              ; {}
07D2: FE 02           CP      $02                 
07D4: 28 1B           JR      Z,$7F1              ; {}
07D6: 11 00 0C        LD      DE,$0C00            
07D9: CD F6 07        CALL    $07F6               ; {}
07DC: C9              RET                         
07DD: 11 03 00        LD      DE,$0003            
07E0: 18 F7           JR      $7D9                ; {}
07E2: 11 0C 00        LD      DE,$000C            
07E5: 18 F2           JR      $7D9                ; {}
07E7: 11 30 00        LD      DE,$0030            
07EA: 18 ED           JR      $7D9                ; {}
07EC: 11 C0 00        LD      DE,$00C0            
07EF: 18 E8           JR      $7D9                ; {}
07F1: 11 00 03        LD      DE,$0300            
07F4: 18 E3           JR      $7D9                ; {}
07F6: 2A 0C 80        LD      HL,($800C)          
07F9: 7A              LD      A,D                 
07FA: B4              OR      H                   
07FB: 67              LD      H,A                 
07FC: 7B              LD      A,E                 
07FD: B5              OR      L                   
07FE: 6F              LD      L,A                 
07FF: 22 0C 80        LD      ($800C),HL          
0802: 77              LD      (HL),A              
0803: C9              RET                         

0804: B7              OR      A                   
0805: C8              RET     Z                   
0806: 21 17 08        LD      HL,$0817            
0809: E5              PUSH    HL                  
080A: 87              ADD     A,A                 
080B: 5F              LD      E,A                 
080C: 16 00           LD      D,$00               
080E: 21 60 08        LD      HL,$0860            
0811: 19              ADD     HL,DE               
0812: 5E              LD      E,(HL)              
0813: 23              INC     HL                  
0814: 56              LD      D,(HL)              
0815: EB              EX      DE,HL               
0816: E9              JP      (HL)                
0817: B7              OR      A                   
0818: C8              RET     Z                   
0819: 3A 10 80        LD      A,($8010)           ; {ram.curVoice}
081C: FE 01           CP      $01                 
081E: 28 18           JR      Z,$838              ; {}
0820: FE 02           CP      $02                 
0822: 28 1C           JR      Z,$840              ; {}
0824: FE 03           CP      $03                 
0826: 28 20           JR      Z,$848              ; {}
0828: FE 04           CP      $04                 
082A: 28 24           JR      Z,$850              ; {}
082C: FE 05           CP      $05                 
082E: 28 28           JR      Z,$858              ; {}
0830: AF              XOR     A                   
0831: 32 0A 80        LD      ($800A),A           
0834: 32 0B 80        LD      ($800B),A           
0837: C9              RET                         
0838: AF              XOR     A                   
0839: 32 00 80        LD      ($8000),A           
083C: 32 01 80        LD      ($8001),A           
083F: C9              RET                         
0840: AF              XOR     A                   
0841: 32 02 80        LD      ($8002),A           
0844: 32 03 80        LD      ($8003),A           
0847: C9              RET                         
0848: AF              XOR     A                   
0849: 32 04 80        LD      ($8004),A           
084C: 32 05 80        LD      ($8005),A           
084F: C9              RET                         
0850: AF              XOR     A                   
0851: 32 06 80        LD      ($8006),A           
0854: 32 07 80        LD      ($8007),A           
0857: C9              RET                         
0858: AF              XOR     A                   
0859: 32 08 80        LD      ($8008),A           
085C: 32 09 80        LD      ($8009),A           
085F: C9              RET                         
0860: 00              NOP                         
0861: 00              NOP                         
0862: 39              ADD     HL,SP               
0863: 09              ADD     HL,BC               
0864: B5              OR      L                   
0865: 09              ADD     HL,BC               
0866: 31 0A AD        LD      SP,$AD0A            
0869: 0A              LD      A,(BC)              
086A: 29              ADD     HL,HL               
086B: 0B              DEC     BC                  
086C: 1F              RRA                         
086D: 0D              DEC     C                   
086E: 4E              LD      C,(HL)              
086F: 12              LD      (DE),A              
0870: CE 13           ADC     $13                 
0872: CE 0D           ADC     $0D                 
0874: D4 0D 4A        CALL    NC,$4A0D            
0877: 10 51           DJNZ    $8CA                ; {}
0879: 10 58           DJNZ    $8D3                ; {}
087B: 10 C7           DJNZ    $844                ; {}
087D: 10 CE           DJNZ    $84D                ; {}
087F: 10 00           DJNZ    $881                ; {}
0881: 00              NOP                         
0882: 00              NOP                         
0883: 00              NOP                         
0884: 20 11           JR      NZ,$897             ; {}
0886: 73              LD      (HL),E              
0887: 0B              DEC     BC                  
0888: 12              LD      (DE),A              
0889: 0C              INC     C                   
088A: A3              AND     E                   
088B: 0C              INC     C                   
088C: 00              NOP                         
088D: 00              NOP                         
088E: 00              NOP                         
088F: 00              NOP                         
0890: 00              NOP                         
0891: 00              NOP                         
0892: 00              NOP                         
0893: 00              NOP                         
0894: 00              NOP                         
0895: 00              NOP                         
0896: 00              NOP                         
0897: 00              NOP                         
0898: 00              NOP                         
0899: 00              NOP                         
089A: 00              NOP                         
089B: 00              NOP                         
089C: 00              NOP                         
089D: 00              NOP                         
089E: 00              NOP                         
089F: 00              NOP                         
08A0: 97              SUB     A                   
08A1: 0D              DEC     C                   
08A2: B1              OR      C                   
08A3: 11 1A 12        LD      DE,$121A            
08A6: DE 12           SBC     $12                 
08A8: 5B              LD      E,E                 
08A9: 13              INC     DE                  
08AA: 00              NOP                         
08AB: 00              NOP                         
08AC: 00              NOP                         
08AD: 00              NOP                         
08AE: 00              NOP                         
08AF: 00              NOP                         
08B0: 00              NOP                         
08B1: 00              NOP                         
08B2: 00              NOP                         
08B3: 00              NOP                         
08B4: 00              NOP                         
08B5: 00              NOP                         
08B6: 00              NOP                         
08B7: 00              NOP                         
08B8: 00              NOP                         
08B9: 00              NOP                         
08BA: 00              NOP                         
08BB: 00              NOP                         
08BC: 00              NOP                         
08BD: 00              NOP                         
08BE: 00              NOP                         
08BF: 00              NOP                         
08C0: CD 2C 0B        CALL    $0B2C               ; {}
08C3: 3E 03           LD      A,$03               
08C5: 32 1B 80        LD      ($801B),A           
08C8: 3E 0F           LD      A,$0F               
08CA: 32 1C 80        LD      ($801C),A           
08CD: 3E 1F           LD      A,$1F               
08CF: 32 1D 80        LD      ($801D),A           
08D2: 21 80 00        LD      HL,$0080            
08D5: 22 1E 80        LD      ($801E),HL          
08D8: 22 20 80        LD      ($8020),HL          
08DB: 3E 04           LD      A,$04               
08DD: 32 22 80        LD      ($8022),A           
08E0: 3E 40           LD      A,$40               
08E2: 32 23 80        LD      ($8023),A           
08E5: 32 24 80        LD      ($8024),A           
08E8: 3E 03           LD      A,$03               
08EA: 32 26 80        LD      ($8026),A           
08ED: 3E 0A           LD      A,$0A               
08EF: 32 27 80        LD      ($8027),A           
08F2: 21 00 08        LD      HL,$0800            
08F5: 22 28 80        LD      ($8028),HL          
08F8: 3E 08           LD      A,$08               
08FA: 32 2A 80        LD      ($802A),A           
08FD: 32 2B 80        LD      ($802B),A           
0900: 21 40 00        LD      HL,$0040            
0903: 22 2C 80        LD      ($802C),HL          
0906: 22 2E 80        LD      ($802E),HL          
0909: 3E 0C           LD      A,$0C               
090B: 32 30 80        LD      ($8030),A           
090E: 3E 03           LD      A,$03               
0910: 32 32 80        LD      ($8032),A           
0913: 3E 0A           LD      A,$0A               
0915: 32 33 80        LD      ($8033),A           
0918: 21 00 02        LD      HL,$0200            
091B: 22 34 80        LD      ($8034),HL          
091E: 21 00 08        LD      HL,$0800            
0921: 22 36 80        LD      ($8036),HL          
0924: 21 00 02        LD      HL,$0200            
0927: 22 38 80        LD      ($8038),HL          
092A: 3E 08           LD      A,$08               
092C: 32 3A 80        LD      ($803A),A           
092F: 32 3B 80        LD      ($803B),A           
0932: 21 20 00        LD      HL,$0020            
0935: 22 3D 80        LD      ($803D),HL          
0938: C9              RET                         
0939: 3E FF           LD      A,$FF               
093B: C9              RET                         
093C: CD 2C 0B        CALL    $0B2C               ; {}
093F: 3E 03           LD      A,$03               
0941: 32 1B 80        LD      ($801B),A           
0944: 3E 0F           LD      A,$0F               
0946: 32 1C 80        LD      ($801C),A           
0949: 3E 1F           LD      A,$1F               
094B: 32 1D 80        LD      ($801D),A           
094E: 21 80 00        LD      HL,$0080            
0951: 22 1E 80        LD      ($801E),HL          
0954: 22 20 80        LD      ($8020),HL          
0957: 3E 01           LD      A,$01               
0959: 32 22 80        LD      ($8022),A           
095C: 3E 20           LD      A,$20               
095E: 32 23 80        LD      ($8023),A           
0961: 32 24 80        LD      ($8024),A           
0964: 3E 03           LD      A,$03               
0966: 32 26 80        LD      ($8026),A           
0969: 3E 0D           LD      A,$0D               
096B: 32 27 80        LD      ($8027),A           
096E: 21 00 08        LD      HL,$0800            
0971: 22 28 80        LD      ($8028),HL          
0974: 3E 08           LD      A,$08               
0976: 32 2A 80        LD      ($802A),A           
0979: 32 2B 80        LD      ($802B),A           
097C: 21 40 00        LD      HL,$0040            
097F: 22 2C 80        LD      ($802C),HL          
0982: 22 2E 80        LD      ($802E),HL          
0985: 3E 02           LD      A,$02               
0987: 32 30 80        LD      ($8030),A           
098A: 3E 03           LD      A,$03               
098C: 32 32 80        LD      ($8032),A           
098F: 3E 0E           LD      A,$0E               
0991: 32 33 80        LD      ($8033),A           
0994: 21 00 02        LD      HL,$0200            
0997: 22 34 80        LD      ($8034),HL          
099A: 21 00 08        LD      HL,$0800            
099D: 22 36 80        LD      ($8036),HL          
09A0: 21 01 00        LD      HL,$0001            
09A3: 22 38 80        LD      ($8038),HL          
09A6: 3E 18           LD      A,$18               
09A8: 32 3A 80        LD      ($803A),A           
09AB: 32 3B 80        LD      ($803B),A           
09AE: 21 00 01        LD      HL,$0100            
09B1: 22 3D 80        LD      ($803D),HL          
09B4: C9              RET                         
09B5: 3E FF           LD      A,$FF               
09B7: C9              RET                         
09B8: CD 2C 0B        CALL    $0B2C               ; {}
09BB: 3E 02           LD      A,$02               
09BD: 32 1B 80        LD      ($801B),A           
09C0: 3E 0F           LD      A,$0F               
09C2: 32 1C 80        LD      ($801C),A           
09C5: 3E 08           LD      A,$08               
09C7: 32 1D 80        LD      ($801D),A           
09CA: 21 80 00        LD      HL,$0080            
09CD: 22 1E 80        LD      ($801E),HL          
09D0: 22 20 80        LD      ($8020),HL          
09D3: 3E 01           LD      A,$01               
09D5: 32 22 80        LD      ($8022),A           
09D8: 3E 20           LD      A,$20               
09DA: 32 23 80        LD      ($8023),A           
09DD: 32 24 80        LD      ($8024),A           
09E0: 3E 03           LD      A,$03               
09E2: 32 26 80        LD      ($8026),A           
09E5: 3E 0A           LD      A,$0A               
09E7: 32 27 80        LD      ($8027),A           
09EA: 21 00 08        LD      HL,$0800            
09ED: 22 28 80        LD      ($8028),HL          
09F0: 3E 08           LD      A,$08               
09F2: 32 2A 80        LD      ($802A),A           
09F5: 32 2B 80        LD      ($802B),A           
09F8: 21 40 00        LD      HL,$0040            
09FB: 22 2C 80        LD      ($802C),HL          
09FE: 22 2E 80        LD      ($802E),HL          
0A01: 3E 03           LD      A,$03               
0A03: 32 30 80        LD      ($8030),A           
0A06: 3E 03           LD      A,$03               
0A08: 32 32 80        LD      ($8032),A           
0A0B: 3E 08           LD      A,$08               
0A0D: 32 33 80        LD      ($8033),A           
0A10: 21 00 02        LD      HL,$0200            
0A13: 22 34 80        LD      ($8034),HL          
0A16: 21 00 08        LD      HL,$0800            
0A19: 22 36 80        LD      ($8036),HL          
0A1C: 21 01 00        LD      HL,$0001            
0A1F: 22 38 80        LD      ($8038),HL          
0A22: 3E 20           LD      A,$20               
0A24: 32 3A 80        LD      ($803A),A           
0A27: 32 3B 80        LD      ($803B),A           
0A2A: 21 20 00        LD      HL,$0020            
0A2D: 22 3D 80        LD      ($803D),HL          
0A30: C9              RET                         
0A31: 3E FF           LD      A,$FF               
0A33: C9              RET                         
0A34: CD 2C 0B        CALL    $0B2C               ; {}
0A37: 3E 03           LD      A,$03               
0A39: 32 1B 80        LD      ($801B),A           
0A3C: 3E 0E           LD      A,$0E               
0A3E: 32 1C 80        LD      ($801C),A           
0A41: 3E 1F           LD      A,$1F               
0A43: 32 1D 80        LD      ($801D),A           
0A46: 21 80 00        LD      HL,$0080            
0A49: 22 1E 80        LD      ($801E),HL          
0A4C: 22 20 80        LD      ($8020),HL          
0A4F: 3E 01           LD      A,$01               
0A51: 32 22 80        LD      ($8022),A           
0A54: 3E 20           LD      A,$20               
0A56: 32 23 80        LD      ($8023),A           
0A59: 32 24 80        LD      ($8024),A           
0A5C: 3E 03           LD      A,$03               
0A5E: 32 26 80        LD      ($8026),A           
0A61: 3E 0C           LD      A,$0C               
0A63: 32 27 80        LD      ($8027),A           
0A66: 21 00 08        LD      HL,$0800            
0A69: 22 28 80        LD      ($8028),HL          
0A6C: 3E 08           LD      A,$08               
0A6E: 32 2A 80        LD      ($802A),A           
0A71: 32 2B 80        LD      ($802B),A           
0A74: 21 40 00        LD      HL,$0040            
0A77: 22 2C 80        LD      ($802C),HL          
0A7A: 22 2E 80        LD      ($802E),HL          
0A7D: 3E 03           LD      A,$03               
0A7F: 32 30 80        LD      ($8030),A           
0A82: 3E 03           LD      A,$03               
0A84: 32 32 80        LD      ($8032),A           
0A87: 3E 0F           LD      A,$0F               
0A89: 32 33 80        LD      ($8033),A           
0A8C: 21 00 02        LD      HL,$0200            
0A8F: 22 34 80        LD      ($8034),HL          
0A92: 21 00 08        LD      HL,$0800            
0A95: 22 36 80        LD      ($8036),HL          
0A98: 21 01 00        LD      HL,$0001            
0A9B: 22 38 80        LD      ($8038),HL          
0A9E: 3E 20           LD      A,$20               
0AA0: 32 3A 80        LD      ($803A),A           
0AA3: 32 3B 80        LD      ($803B),A           
0AA6: 21 20 00        LD      HL,$0020            
0AA9: 22 3D 80        LD      ($803D),HL          
0AAC: C9              RET                         
0AAD: 3E FF           LD      A,$FF               
0AAF: C9              RET                         
0AB0: CD 2C 0B        CALL    $0B2C               ; {}
0AB3: 3E 03           LD      A,$03               
0AB5: 32 1B 80        LD      ($801B),A           
0AB8: 3E 0F           LD      A,$0F               
0ABA: 32 1C 80        LD      ($801C),A           
0ABD: 3E 1F           LD      A,$1F               
0ABF: 32 1D 80        LD      ($801D),A           
0AC2: 21 80 00        LD      HL,$0080            
0AC5: 22 1E 80        LD      ($801E),HL          
0AC8: 22 20 80        LD      ($8020),HL          
0ACB: 3E 04           LD      A,$04               
0ACD: 32 22 80        LD      ($8022),A           
0AD0: 3E 40           LD      A,$40               
0AD2: 32 23 80        LD      ($8023),A           
0AD5: 32 24 80        LD      ($8024),A           
0AD8: 3E 03           LD      A,$03               
0ADA: 32 26 80        LD      ($8026),A           
0ADD: 3E 0C           LD      A,$0C               
0ADF: 32 27 80        LD      ($8027),A           
0AE2: 21 00 08        LD      HL,$0800            
0AE5: 22 28 80        LD      ($8028),HL          
0AE8: 3E 08           LD      A,$08               
0AEA: 32 2A 80        LD      ($802A),A           
0AED: 32 2B 80        LD      ($802B),A           
0AF0: 21 30 00        LD      HL,$0030            
0AF3: 22 2C 80        LD      ($802C),HL          
0AF6: 22 2E 80        LD      ($802E),HL          
0AF9: 3E 08           LD      A,$08               
0AFB: 32 30 80        LD      ($8030),A           
0AFE: 3E 03           LD      A,$03               
0B00: 32 32 80        LD      ($8032),A           
0B03: 3E 09           LD      A,$09               
0B05: 32 33 80        LD      ($8033),A           
0B08: 21 00 02        LD      HL,$0200            
0B0B: 22 34 80        LD      ($8034),HL          
0B0E: 21 00 08        LD      HL,$0800            
0B11: 22 36 80        LD      ($8036),HL          
0B14: 21 00 01        LD      HL,$0100            
0B17: 22 38 80        LD      ($8038),HL          
0B1A: 3E 01           LD      A,$01               
0B1C: 32 3A 80        LD      ($803A),A           
0B1F: 32 3B 80        LD      ($803B),A           
0B22: 21 20 00        LD      HL,$0020            
0B25: 22 3D 80        LD      ($803D),HL          
0B28: C9              RET                         
0B29: 3E FF           LD      A,$FF               
0B2B: C9              RET                         
0B2C: 3E 13           LD      A,$13               
0B2E: CD 6F 00        CALL    $006F               ; {}
0B31: 3E 14           LD      A,$14               
0B33: CD 6F 00        CALL    $006F               ; {}
0B36: 3E 15           LD      A,$15               
0B38: CD 6F 00        CALL    $006F               ; {}
0B3B: C9              RET                         
0B3C: 3A 1B 80        LD      A,($801B)           
0B3F: FE 00           CP      $00                 
0B41: 28 21           JR      Z,$B64              ; {}
0B43: FE 01           CP      $01                 
0B45: 28 22           JR      Z,$B69              ; {}
0B47: FE 02           CP      $02                 
0B49: 28 23           JR      Z,$B6E              ; {}
0B4B: CD BC 07        CALL    $07BC               ; {}
0B4E: AF              XOR     A                   
0B4F: 32 25 80        LD      ($8025),A           
0B52: 16 06           LD      D,$06               
0B54: 21 1D 80        LD      HL,$801D            
0B57: 5E              LD      E,(HL)              
0B58: CD 4C 05        CALL    $054C               ; {}
0B5B: CD 80 05        CALL    $0580               ; {}
0B5E: 06 00           LD      B,$00               
0B60: CD FE 05        CALL    $05FE               ; {}
0B63: C9              RET                         
0B64: CD C7 06        CALL    $06C7               ; {}
0B67: 18 E5           JR      $B4E                ; {}
0B69: CD 48 07        CALL    $0748               ; {}
0B6C: 18 E0           JR      $B4E                ; {}
0B6E: CD 82 07        CALL    $0782               ; {}
0B71: 18 DB           JR      $B4E                ; {}
0B73: 16 06           LD      D,$06               
0B75: 21 1D 80        LD      HL,$801D            
0B78: 5E              LD      E,(HL)              
0B79: CD 4C 05        CALL    $054C               ; {}
0B7C: 3A 25 80        LD      A,($8025)           
0B7F: FE 00           CP      $00                 
0B81: 28 1E           JR      Z,$BA1              ; {}
0B83: FE 01           CP      $01                 
0B85: 28 27           JR      Z,$BAE              ; {}
0B87: FE 02           CP      $02                 
0B89: 28 3C           JR      Z,$BC7              ; {}
0B8B: 21 24 80        LD      HL,$8024            
0B8E: 35              DEC     (HL)                
0B8F: 20 0E           JR      NZ,$B9F             ; {}
0B91: 3A 23 80        LD      A,($8023)           
0B94: 77              LD      (HL),A              
0B95: CD 4B 06        CALL    $064B               ; {}
0B98: 3D              DEC     A                   
0B99: 28 3E           JR      Z,$BD9              ; {}
0B9B: 47              LD      B,A                 
0B9C: CD FE 05        CALL    $05FE               ; {}
0B9F: AF              XOR     A                   
0BA0: C9              RET                         
0BA1: 3A 1C 80        LD      A,($801C)           
0BA4: 47              LD      B,A                 
0BA5: CD FE 05        CALL    $05FE               ; {}
0BA8: 21 25 80        LD      HL,$8025            
0BAB: 34              INC     (HL)                
0BAC: 18 DD           JR      $B8B                ; {}
0BAE: 2A 20 80        LD      HL,($8020)          
0BB1: 2B              DEC     HL                  
0BB2: 7C              LD      A,H                 
0BB3: B5              OR      L                   
0BB4: 20 0C           JR      NZ,$BC2             ; {}
0BB6: 2A 1E 80        LD      HL,($801E)          
0BB9: 22 20 80        LD      ($8020),HL          
0BBC: 21 25 80        LD      HL,$8025            
0BBF: 34              INC     (HL)                
0BC0: 18 C9           JR      $B8B                ; {}
0BC2: 22 20 80        LD      ($8020),HL          
0BC5: 18 C4           JR      $B8B                ; {}
0BC7: 21 22 80        LD      HL,$8022            
0BCA: 35              DEC     (HL)                
0BCB: 20 06           JR      NZ,$BD3             ; {}
0BCD: 21 25 80        LD      HL,$8025            
0BD0: 34              INC     (HL)                
0BD1: 18 B8           JR      $B8B                ; {}
0BD3: AF              XOR     A                   
0BD4: 32 25 80        LD      ($8025),A           
0BD7: 18 B2           JR      $B8B                ; {}
0BD9: 16 06           LD      D,$06               
0BDB: 1E 04           LD      E,$04               
0BDD: CD 4C 05        CALL    $054C               ; {}
0BE0: 3E FF           LD      A,$FF               
0BE2: C9              RET                         
0BE3: 3A 26 80        LD      A,($8026)           
0BE6: FE 00           CP      $00                 
0BE8: 28 19           JR      Z,$C03              ; {}
0BEA: FE 01           CP      $01                 
0BEC: 28 1A           JR      Z,$C08              ; {}
0BEE: FE 02           CP      $02                 
0BF0: 28 1B           JR      Z,$C0D              ; {}
0BF2: CD BC 07        CALL    $07BC               ; {}
0BF5: AF              XOR     A                   
0BF6: 32 31 80        LD      ($8031),A           
0BF9: 2A 28 80        LD      HL,($8028)          
0BFC: CD C6 04        CALL    $04C6               ; {}
0BFF: CD 0D 05        CALL    $050D               ; {}
0C02: C9              RET                         
0C03: CD C7 06        CALL    $06C7               ; {}
0C06: 18 ED           JR      $BF5                ; {}
0C08: CD 48 07        CALL    $0748               ; {}
0C0B: 18 E8           JR      $BF5                ; {}
0C0D: CD 82 07        CALL    $0782               ; {}
0C10: 18 E3           JR      $BF5                ; {}
0C12: 3A 31 80        LD      A,($8031)           
0C15: FE 00           CP      $00                 
0C17: 28 1F           JR      Z,$C38              ; {}
0C19: FE 01           CP      $01                 
0C1B: 28 2E           JR      Z,$C4B              ; {}
0C1D: 2A 2E 80        LD      HL,($802E)          
0C20: 2B              DEC     HL                  
0C21: 7C              LD      A,H                 
0C22: B5              OR      L                   
0C23: 20 40           JR      NZ,$C65             ; {}
0C25: 2A 2C 80        LD      HL,($802C)          
0C28: 22 2E 80        LD      ($802E),HL          
0C2B: 21 30 80        LD      HL,$8030            
0C2E: 35              DEC     (HL)                
0C2F: 28 39           JR      Z,$C6A              ; {}
0C31: 21 31 80        LD      HL,$8031            
0C34: 36 00           LD      (HL),$00            
0C36: AF              XOR     A                   
0C37: C9              RET                         
0C38: 3A 27 80        LD      A,($8027)           
0C3B: 47              LD      B,A                 
0C3C: CD FE 05        CALL    $05FE               ; {}
0C3F: 3A 2A 80        LD      A,($802A)           
0C42: 32 2B 80        LD      ($802B),A           
0C45: 21 31 80        LD      HL,$8031            
0C48: 34              INC     (HL)                
0C49: 18 EB           JR      $C36                ; {}
0C4B: 21 2B 80        LD      HL,$802B            
0C4E: 35              DEC     (HL)                
0C4F: 20 CC           JR      NZ,$C1D             ; {}
0C51: 3A 2A 80        LD      A,($802A)           
0C54: 77              LD      (HL),A              
0C55: CD 4B 06        CALL    $064B               ; {}
0C58: 3D              DEC     A                   
0C59: 20 04           JR      NZ,$C5F             ; {}
0C5B: 21 31 80        LD      HL,$8031            
0C5E: 34              INC     (HL)                
0C5F: 47              LD      B,A                 
0C60: CD FE 05        CALL    $05FE               ; {}
0C63: 18 B8           JR      $C1D                ; {}
0C65: 22 2E 80        LD      ($802E),HL          
0C68: 18 CC           JR      $C36                ; {}
0C6A: 3E FF           LD      A,$FF               
0C6C: C9              RET                         
0C6D: 3A 32 80        LD      A,($8032)           
0C70: FE 00           CP      $00                 
0C72: 28 20           JR      Z,$C94              ; {}
0C74: FE 01           CP      $01                 
0C76: 28 21           JR      Z,$C99              ; {}
0C78: FE 02           CP      $02                 
0C7A: 28 22           JR      Z,$C9E              ; {}
0C7C: CD BC 07        CALL    $07BC               ; {}
0C7F: AF              XOR     A                   
0C80: 32 3C 80        LD      ($803C),A           
0C83: 2A 36 80        LD      HL,($8036)          
0C86: CD C6 04        CALL    $04C6               ; {}
0C89: CD 0D 05        CALL    $050D               ; {}
0C8C: 3A 33 80        LD      A,($8033)           
0C8F: 47              LD      B,A                 
0C90: CD FE 05        CALL    $05FE               ; {}
0C93: C9              RET                         
0C94: CD C7 06        CALL    $06C7               ; {}
0C97: 18 E6           JR      $C7F                ; {}
0C99: CD 48 07        CALL    $0748               ; {}
0C9C: 18 E1           JR      $C7F                ; {}
0C9E: CD 82 07        CALL    $0782               ; {}
0CA1: 18 DC           JR      $C7F                ; {}
0CA3: 3A 3C 80        LD      A,($803C)           
0CA6: FE 00           CP      $00                 
0CA8: 28 22           JR      Z,$CCC              ; {}
0CAA: FE 01           CP      $01                 
0CAC: 28 32           JR      Z,$CE0              ; {}
0CAE: CD 80 06        CALL    $0680               ; {}
0CB1: B7              OR      A                   
0CB2: ED 5B 3D 80     LD      DE,($803D)          
0CB6: ED 52           SBC     HL,DE               
0CB8: ED 5B 34 80     LD      DE,($8034)          
0CBC: 7C              LD      A,H                 
0CBD: BA              CP      D                   
0CBE: 20 07           JR      NZ,$CC7             ; {}
0CC0: 7D              LD      A,L                 
0CC1: BB              CP      E                   
0CC2: 20 03           JR      NZ,$CC7             ; {}
0CC4: 2A 36 80        LD      HL,($8036)          
0CC7: CD C6 04        CALL    $04C6               ; {}
0CCA: AF              XOR     A                   
0CCB: C9              RET                         
0CCC: 2A 38 80        LD      HL,($8038)          
0CCF: 2B              DEC     HL                  
0CD0: 7C              LD      A,H                 
0CD1: B5              OR      L                   
0CD2: 20 07           JR      NZ,$CDB             ; {}
0CD4: 3E 01           LD      A,$01               
0CD6: 32 3C 80        LD      ($803C),A           
0CD9: 18 D3           JR      $CAE                ; {}
0CDB: 22 38 80        LD      ($8038),HL          
0CDE: 18 CE           JR      $CAE                ; {}
0CE0: 21 3A 80        LD      HL,$803A            
0CE3: 35              DEC     (HL)                
0CE4: 20 C8           JR      NZ,$CAE             ; {}
0CE6: 3A 3B 80        LD      A,($803B)           
0CE9: 77              LD      (HL),A              
0CEA: CD 4B 06        CALL    $064B               ; {}
0CED: 3D              DEC     A                   
0CEE: 28 06           JR      Z,$CF6              ; {}
0CF0: 47              LD      B,A                 
0CF1: CD FE 05        CALL    $05FE               ; {}
0CF4: 18 B8           JR      $CAE                ; {}
0CF6: 3E FF           LD      A,$FF               
0CF8: C9              RET                         
0CF9: CD 48 07        CALL    $0748               ; {}
0CFC: AF              XOR     A                   
0CFD: 32 43 80        LD      ($8043),A           
0D00: 3E 02           LD      A,$02               
0D02: 32 42 80        LD      ($8042),A           
0D05: CD 0D 05        CALL    $050D               ; {}
0D08: 3E 08           LD      A,$08               
0D0A: 32 3F 80        LD      ($803F),A           
0D0D: 21 20 00        LD      HL,$0020            
0D10: 22 40 80        LD      ($8040),HL          
0D13: 21 40 00        LD      HL,$0040            
0D16: CD C6 04        CALL    $04C6               ; {}
0D19: 06 08           LD      B,$08               
0D1B: CD FE 05        CALL    $05FE               ; {}
0D1E: C9              RET                         
0D1F: 3A 43 80        LD      A,($8043)           
0D22: B7              OR      A                   
0D23: 20 0B           JR      NZ,$D30             ; {}
0D25: 2A 40 80        LD      HL,($8040)          
0D28: 2B              DEC     HL                  
0D29: 7C              LD      A,H                 
0D2A: B5              OR      L                   
0D2B: 28 37           JR      Z,$D64              ; {}
0D2D: 22 40 80        LD      ($8040),HL          
0D30: 21 3F 80        LD      HL,$803F            
0D33: 35              DEC     (HL)                
0D34: 28 1A           JR      Z,$D50              ; {}
0D36: CD 80 06        CALL    $0680               ; {}
0D39: 11 10 00        LD      DE,$0010            
0D3C: 19              ADD     HL,DE               
0D3D: 11 00 02        LD      DE,$0200            
0D40: 7C              LD      A,H                 
0D41: BA              CP      D                   
0D42: 20 07           JR      NZ,$D4B             ; {}
0D44: 7D              LD      A,L                 
0D45: BB              CP      E                   
0D46: 20 03           JR      NZ,$D4B             ; {}
0D48: 21 40 00        LD      HL,$0040            
0D4B: CD C6 04        CALL    $04C6               ; {}
0D4E: AF              XOR     A                   
0D4F: C9              RET                         
0D50: 3E 08           LD      A,$08               
0D52: 32 3F 80        LD      ($803F),A           
0D55: CD 4B 06        CALL    $064B               ; {}
0D58: 3D              DEC     A                   
0D59: 28 06           JR      Z,$D61              ; {}
0D5B: 47              LD      B,A                 
0D5C: CD FE 05        CALL    $05FE               ; {}
0D5F: 18 D5           JR      $D36                ; {}
0D61: 3E FF           LD      A,$FF               
0D63: C9              RET                         
0D64: 21 20 00        LD      HL,$0020            
0D67: 22 40 80        LD      ($8040),HL          
0D6A: 21 42 80        LD      HL,$8042            
0D6D: 35              DEC     (HL)                
0D6E: 20 05           JR      NZ,$D75             ; {}
0D70: 3E 01           LD      A,$01               
0D72: 32 43 80        LD      ($8043),A           
0D75: CD 08 0D        CALL    $0D08               ; {}
0D78: 18 A5           JR      $D1F                ; {}
0D7A: CD 82 07        CALL    $0782               ; {}
0D7D: 3E 08           LD      A,$08               
0D7F: 32 44 80        LD      ($8044),A           
0D82: 21 00 0A        LD      HL,$0A00            
0D85: 22 45 80        LD      ($8045),HL          
0D88: 21 40 00        LD      HL,$0040            
0D8B: CD C6 04        CALL    $04C6               ; {}
0D8E: CD 0D 05        CALL    $050D               ; {}
0D91: 06 0B           LD      B,$0B               
0D93: CD FE 05        CALL    $05FE               ; {}
0D96: C9              RET                         
0D97: 2A 45 80        LD      HL,($8045)          
0D9A: 2B              DEC     HL                  
0D9B: 7C              LD      A,H                 
0D9C: B5              OR      L                   
0D9D: 28 17           JR      Z,$DB6              ; {}
0D9F: 22 45 80        LD      ($8045),HL          
0DA2: 21 44 80        LD      HL,$8044            
0DA5: 35              DEC     (HL)                
0DA6: 20 0C           JR      NZ,$DB4             ; {}
0DA8: 36 08           LD      (HL),$08            
0DAA: CD 80 06        CALL    $0680               ; {}
0DAD: 11 02 00        LD      DE,$0002            
0DB0: 19              ADD     HL,DE               
0DB1: CD C6 04        CALL    $04C6               ; {}
0DB4: AF              XOR     A                   
0DB5: C9              RET                         
0DB6: 3E FF           LD      A,$FF               
0DB8: C9              RET                         
0DB9: CD C7 06        CALL    $06C7               ; {}
0DBC: 3E 00           LD      A,$00               
0DBE: 32 73 80        LD      ($8073),A           
0DC1: CD 0D 05        CALL    $050D               ; {}
0DC4: C3 8E 0F        JP      $0F8E               ; {}
0DC7: CD C7 06        CALL    $06C7               ; {}
0DCA: CD 0D 05        CALL    $050D               ; {}
0DCD: C9              RET                         
0DCE: DD 21 50 80     LD      IX,$8050            
0DD2: 18 06           JR      $DDA                ; {}
0DD4: DD 21 58 80     LD      IX,$8058            
0DD8: 18 00           JR      $DDA                ; {}
0DDA: DD 7E 00        LD      A,(IX+$00)          
0DDD: FE FF           CP      $FF                 
0DDF: C8              RET     Z                   
0DE0: CD E5 0D        CALL    $0DE5               ; {}
0DE3: AF              XOR     A                   
0DE4: C9              RET                         
0DE5: DD 35 01        DEC     (IX+$01)            
0DE8: C0              RET     NZ                  
0DE9: 3A 72 80        LD      A,($8072)           
0DEC: DD 77 01        LD      (IX+$01),A          
0DEF: DD CB 00 46     BIT     0,(IX+$00)          
0DF3: C2 05 0E        JP      NZ,$0E05            ; {}
0DF6: DD 7E 07        LD      A,(IX+$07)          
0DF9: D6 01           SUB     $01                 
0DFB: FA 05 0E        JP      M,$0E05             ; {}
0DFE: DD 77 07        LD      (IX+$07),A          
0E01: 47              LD      B,A                 
0E02: CD FE 05        CALL    $05FE               ; {}
0E05: DD 35 00        DEC     (IX+$00)            
0E08: C0              RET     NZ                  
0E09: DD 6E 02        LD      L,(IX+$02)          
0E0C: DD 66 03        LD      H,(IX+$03)          
0E0F: 7E              LD      A,(HL)              
0E10: 47              LD      B,A                 
0E11: E6 1F           AND     $1F                 
0E13: CA 9A 0E        JP      Z,$0E9A             ; {}
0E16: FE 1F           CP      $1F                 
0E18: C2 B6 0E        JP      NZ,$0EB6            ; {}
0E1B: 23              INC     HL                  
0E1C: DD 75 02        LD      (IX+$02),L          
0E1F: DD 74 03        LD      (IX+$03),H          
0E22: 78              LD      A,B                 
0E23: E6 E0           AND     $E0                 
0E25: 0F              RRCA                        
0E26: 0F              RRCA                        
0E27: 0F              RRCA                        
0E28: 0F              RRCA                        
0E29: 4F              LD      C,A                 
0E2A: 06 00           LD      B,$00               
0E2C: 21 35 0E        LD      HL,$0E35            
0E2F: 09              ADD     HL,BC               
0E30: 5E              LD      E,(HL)              
0E31: 23              INC     HL                  
0E32: 56              LD      D,(HL)              
0E33: D5              PUSH    DE                  
0E34: C9              RET                         
0E35: 45              LD      B,L                 
0E36: 0E 5D           LD      C,$5D               
0E38: 0E 73           LD      C,$73               
0E3A: 0E 90           LD      C,$90               
0E3C: 0E 90           LD      C,$90               
0E3E: 0E 90           LD      C,$90               
0E40: 0E 90           LD      C,$90               
0E42: 0E 90           LD      C,$90               
0E44: 0E DD           LD      C,$DD               
0E46: 6E              LD      L,(HL)              
0E47: 02              LD      (BC),A              
0E48: DD 66 03        LD      H,(IX+$03)          
0E4B: 4E              LD      C,(HL)              
0E4C: CB 21           SLA     C                   
0E4E: 06 00           LD      B,$00               
0E50: 21 E6 0E        LD      HL,$0EE6            
0E53: 09              ADD     HL,BC               
0E54: 5E              LD      E,(HL)              
0E55: 23              INC     HL                  
0E56: 56              LD      D,(HL)              
0E57: ED 53 70 80     LD      ($8070),DE          
0E5B: 18 23           JR      $E80                ; {}
0E5D: DD 6E 02        LD      L,(IX+$02)          
0E60: DD 66 03        LD      H,(IX+$03)          
0E63: 4E              LD      C,(HL)              
0E64: 06 00           LD      B,$00               
0E66: 21 7E 0F        LD      HL,$0F7E            
0E69: 09              ADD     HL,BC               
0E6A: 7E              LD      A,(HL)              
0E6B: 32 72 80        LD      ($8072),A           
0E6E: DD 77 01        LD      (IX+$01),A          
0E71: 18 0D           JR      $E80                ; {}
0E73: DD 6E 02        LD      L,(IX+$02)          
0E76: DD 66 03        LD      H,(IX+$03)          
0E79: 7E              LD      A,(HL)              
0E7A: DD 77 06        LD      (IX+$06),A          
0E7D: DD 77 07        LD      (IX+$07),A          
0E80: DD 6E 02        LD      L,(IX+$02)          
0E83: DD 66 03        LD      H,(IX+$03)          
0E86: 23              INC     HL                  
0E87: DD 75 02        LD      (IX+$02),L          
0E8A: DD 74 03        LD      (IX+$03),H          
0E8D: C3 09 0E        JP      $0E09               ; {}
0E90: 06 00           LD      B,$00               
0E92: CD FE 05        CALL    $05FE               ; {}
0E95: DD 36 00 FF     LD      (IX+$00),$FF        
0E99: C9              RET                         
0E9A: CD A4 0E        CALL    $0EA4               ; {}
0E9D: 06 00           LD      B,$00               
0E9F: CD FE 05        CALL    $05FE               ; {}
0EA2: 18 34           JR      $ED8                ; {}
0EA4: 78              LD      A,B                 
0EA5: E6 E0           AND     $E0                 
0EA7: 07              RLCA                        
0EA8: 07              RLCA                        
0EA9: 07              RLCA                        
0EAA: 47              LD      B,A                 
0EAB: 3E 01           LD      A,$01               
0EAD: 10 04           DJNZ    $EB3                ; {}
0EAF: DD 77 00        LD      (IX+$00),A          
0EB2: C9              RET                         
0EB3: 07              RLCA                        
0EB4: 18 F7           JR      $EAD                ; {}
0EB6: C5              PUSH    BC                  
0EB7: CD A4 0E        CALL    $0EA4               ; {}
0EBA: C1              POP     BC                  
0EBB: 78              LD      A,B                 
0EBC: E6 1F           AND     $1F                 
0EBE: 3D              DEC     A                   
0EBF: 07              RLCA                        
0EC0: 4F              LD      C,A                 
0EC1: 06 00           LD      B,$00               
0EC3: 2A 70 80        LD      HL,($8070)          
0EC6: 09              ADD     HL,BC               
0EC7: 5E              LD      E,(HL)              
0EC8: 23              INC     HL                  
0EC9: 56              LD      D,(HL)              
0ECA: EB              EX      DE,HL               
0ECB: CD C6 04        CALL    $04C6               ; {}
0ECE: DD 46 06        LD      B,(IX+$06)          
0ED1: 78              LD      A,B                 
0ED2: DD 77 07        LD      (IX+$07),A          
0ED5: CD FE 05        CALL    $05FE               ; {}
0ED8: DD 6E 02        LD      L,(IX+$02)          
0EDB: DD 66 03        LD      H,(IX+$03)          
0EDE: 23              INC     HL                  
0EDF: DD 75 02        LD      (IX+$02),L          
0EE2: DD 74 03        LD      (IX+$03),H          
0EE5: C9              RET                         
0EE6: 06 0F           LD      B,$0F               
0EE8: 0A              LD      A,(BC)              
0EE9: 0F              RRCA                        
0EEA: 0E 0F           LD      C,$0F               
0EEC: 12              LD      (DE),A              
0EED: 0F              RRCA                        
0EEE: 16 0F           LD      D,$0F               
0EF0: 1A              LD      A,(DE)              
0EF1: 0F              RRCA                        
0EF2: 1E 0F           LD      E,$0F               
0EF4: 22 0F 26        LD      ($260F),HL          
0EF7: 0F              RRCA                        
0EF8: 2A 0F 2E        LD      HL,($2E0F)          
0EFB: 0F              RRCA                        
0EFC: 32 0F 36        LD      ($360F),A           
0EFF: 0F              RRCA                        
0F00: 3A 0F 3E        LD      A,($3E0F)           
0F03: 0F              RRCA                        
0F04: 42              LD      B,D                 
0F05: 0F              RRCA                        
0F06: 6B              LD      L,E                 
0F07: 08              EX      AF,AF'              
0F08: F2 07 80        JP      P,$8007             
0F0B: 07              RLCA                        
0F0C: 14              INC     D                   
0F0D: 07              RLCA                        
0F0E: AE              XOR     (HL)                
0F0F: 06 4E           LD      B,$4E               
0F11: 06 F3           LD      B,$F3               
0F13: 05              DEC     B                   
0F14: 9E              SBC     (HL)                
0F15: 05              DEC     B                   
0F16: 4E              LD      C,(HL)              
0F17: 05              DEC     B                   
0F18: 01 05 B9        LD      BC,$B905            
0F1B: 04              INC     B                   
0F1C: 76              HALT                        
0F1D: 04              INC     B                   
0F1E: 36 04           LD      (HL),$04            
0F20: F9              LD      SP,HL               
0F21: 03              INC     BC                  
0F22: C0              RET     NZ                  
0F23: 03              INC     BC                  
0F24: 8A              ADC     A,D                 
0F25: 03              INC     BC                  
0F26: 57              LD      D,A                 
0F27: 03              INC     BC                  
0F28: 27              DAA                         
0F29: 03              INC     BC                  
0F2A: FA 02 CF        JP      M,$CF02             
0F2D: 02              LD      (BC),A              
0F2E: A7              AND     A                   
0F2F: 02              LD      (BC),A              
0F30: 81              ADD     A,C                 
0F31: 02              LD      (BC),A              
0F32: 5D              LD      E,L                 
0F33: 02              LD      (BC),A              
0F34: 3B              DEC     SP                  
0F35: 02              LD      (BC),A              
0F36: 1B              DEC     DE                  
0F37: 02              LD      (BC),A              
0F38: FD ; ????
0F39: 01 E0 01        LD      BC,$01E0            
0F3C: C5              PUSH    BC                  
0F3D: 01 AC 01        LD      BC,$01AC            
0F40: 94              SUB     H                   
0F41: 01 7D 01        LD      BC,$017D            
0F44: 68              LD      L,B                 
0F45: 01 53 01        LD      BC,$0153            
0F48: 40              LD      B,B                 
0F49: 01 2E 01        LD      BC,$012E            
0F4C: 1D              DEC     E                   
0F4D: 01 0D 01        LD      BC,$010D            
0F50: FE 00           CP      $00                 
0F52: F0              RET     P                   
0F53: 00              NOP                         
0F54: E3              EX      (SP),HL             
0F55: 00              NOP                         
0F56: D6 00           SUB     $00                 
0F58: CA 00 BE        JP      Z,$BE00             
0F5B: 00              NOP                         
0F5C: B4              OR      H                   
0F5D: 00              NOP                         
0F5E: AA              XOR     D                   
0F5F: 00              NOP                         
0F60: A0              AND     B                   
0F61: 00              NOP                         
0F62: 97              SUB     A                   
0F63: 00              NOP                         
0F64: 8F              ADC     A,A                 
0F65: 00              NOP                         
0F66: 87              ADD     A,A                 
0F67: 00              NOP                         
0F68: 7F              LD      A,A                 
0F69: 00              NOP                         
0F6A: 78              LD      A,B                 
0F6B: 00              NOP                         
0F6C: 71              LD      (HL),C              
0F6D: 00              NOP                         
0F6E: 6B              LD      L,E                 
0F6F: 00              NOP                         
0F70: 65              LD      H,L                 
0F71: 00              NOP                         
0F72: 5F              LD      E,A                 
0F73: 00              NOP                         
0F74: 5A              LD      E,D                 
0F75: 00              NOP                         
0F76: 55              LD      D,L                 
0F77: 00              NOP                         
0F78: 50              LD      D,B                 
0F79: 00              NOP                         
0F7A: 4C              LD      C,H                 
0F7B: 00              NOP                         
0F7C: 47              LD      B,A                 
0F7D: 00              NOP                         
0F7E: 57              LD      D,A                 
0F7F: 42              LD      B,D                 
0F80: 34              INC     (HL)                
0F81: 2C              INC     L                   
0F82: 25              DEC     H                   
0F83: 21 1D 1A        LD      HL,$1A1D            
0F86: 0C              INC     C                   
0F87: 0B              DEC     BC                  
0F88: 0A              LD      A,(BC)              
0F89: 09              ADD     HL,BC               
0F8A: 08              EX      AF,AF'              
0F8B: 07              RLCA                        
0F8C: 06 05           LD      B,$05               
0F8E: 21 C1 0F        LD      HL,$0FC1            
0F91: 11 50 80        LD      DE,$8050            
0F94: 01 18 00        LD      BC,$0018            
0F97: ED B0           LDIR                        
0F99: 3A 73 80        LD      A,($8073)           
0F9C: 07              RLCA                        
0F9D: 4F              LD      C,A                 
0F9E: 07              RLCA                        
0F9F: 07              RLCA                        
0FA0: 91              SUB     C                   
0FA1: 4F              LD      C,A                 
0FA2: 06 00           LD      B,$00               
0FA4: 21 D9 0F        LD      HL,$0FD9            
0FA7: 09              ADD     HL,BC               
0FA8: 11 52 80        LD      DE,$8052            
0FAB: CD B7 0F        CALL    $0FB7               ; {}
0FAE: 11 5A 80        LD      DE,$805A            
0FB1: CD B7 0F        CALL    $0FB7               ; {}
0FB4: 11 62 80        LD      DE,$8062            
0FB7: 7E              LD      A,(HL)              
0FB8: 12              LD      (DE),A              
0FB9: CD BE 0F        CALL    $0FBE               ; {}
0FBC: 7E              LD      A,(HL)              
0FBD: 12              LD      (DE),A              
0FBE: 23              INC     HL                  
0FBF: 13              INC     DE                  
0FC0: C9              RET                         
0FC1: 01 01 00        LD      BC,$0001            
0FC4: 00              NOP                         
0FC5: 00              NOP                         
0FC6: 00              NOP                         
0FC7: 00              NOP                         
0FC8: 00              NOP                         
0FC9: 01 01 00        LD      BC,$0001            
0FCC: 00              NOP                         
0FCD: 00              NOP                         
0FCE: 00              NOP                         
0FCF: 00              NOP                         
0FD0: 00              NOP                         
0FD1: 01 01 00        LD      BC,$0001            
0FD4: 00              NOP                         
0FD5: 00              NOP                         
0FD6: 00              NOP                         
0FD7: 00              NOP                         
0FD8: 00              NOP                         
0FD9: EB              EX      DE,HL               
0FDA: 0F              RRCA                        
0FDB: 0D              DEC     C                   
0FDC: 10 2D           DJNZ    $100B               ; {}
0FDE: 10 5F           DJNZ    $103F               ; {}
0FE0: 10 7C           DJNZ    $105E               ; {}
0FE2: 10 97           DJNZ    $F7B                ; {}
0FE4: 10 D5           DJNZ    $FBB                ; {}
0FE6: 10 EB           DJNZ    $FD3                ; {}
0FE8: 10 FF           DJNZ    $FE9                ; {}
0FEA: 10 1F           DJNZ    $100B               ; {}
0FEC: 0A              LD      A,(BC)              
0FED: 3F              CCF                         
0FEE: 0D              DEC     C                   
0FEF: 5F              LD      E,A                 
0FF0: 09              ADD     HL,BC               
0FF1: AC              XOR     H                   
0FF2: 80              ADD     A,B                 
0FF3: 6C              LD      L,H                 
0FF4: 6C              LD      L,H                 
0FF5: AC              XOR     H                   
0FF6: 80              ADD     A,B                 
0FF7: 6C              LD      L,H                 
0FF8: 6C              LD      L,H                 
0FF9: 8C              ADC     A,H                 
0FFA: 88              ADC     A,B                 
0FFB: 8C              ADC     A,H                 
0FFC: 8F              ADC     A,A                 
0FFD: 8C              ADC     A,H                 
0FFE: 88              ADC     A,B                 
0FFF: 8C              ADC     A,H                 
1000: 88              ADC     A,B                 
1001: 8C              ADC     A,H                 
1002: 8F              ADC     A,A                 
1003: 8C              ADC     A,H                 
1004: 88              ADC     A,B                 
1005: 8C              ADC     A,H                 
1006: 88              ADC     A,B                 
1007: 8C              ADC     A,H                 
1008: 8F              ADC     A,A                 
1009: 8C              ADC     A,H                 
100A: 88              ADC     A,B                 
100B: AF              XOR     A                   
100C: FF              RST     0X38                
100D: 1F              RRA                         
100E: 0A              LD      A,(BC)              
100F: 5F              LD      E,A                 
1010: 09              ADD     HL,BC               
1011: A8              XOR     B                   
1012: 80              ADD     A,B                 
1013: 68              LD      L,B                 
1014: 68              LD      L,B                 
1015: A8              XOR     B                   
1016: 80              ADD     A,B                 
1017: 68              LD      L,B                 
1018: 68              LD      L,B                 
1019: 88              ADC     A,B                 
101A: 83              ADD     A,E                 
101B: 88              ADC     A,B                 
101C: 8C              ADC     A,H                 
101D: 88              ADC     A,B                 
101E: 83              ADD     A,E                 
101F: 88              ADC     A,B                 
1020: 83              ADD     A,E                 
1021: 88              ADC     A,B                 
1022: 8C              ADC     A,H                 
1023: 88              ADC     A,B                 
1024: 83              ADD     A,E                 
1025: 88              ADC     A,B                 
1026: 83              ADD     A,E                 
1027: 88              ADC     A,B                 
1028: 8C              ADC     A,H                 
1029: 88              ADC     A,B                 
102A: 83              ADD     A,E                 
102B: AC              XOR     H                   
102C: FF              RST     0X38                
102D: FF              RST     0X38                
102E: CD C7 06        CALL    $06C7               ; {}
1031: 3E 01           LD      A,$01               
1033: 32 73 80        LD      ($8073),A           
1036: CD 0D 05        CALL    $050D               ; {}
1039: C3 8E 0F        JP      $0F8E               ; {}
103C: CD C7 06        CALL    $06C7               ; {}
103F: CD 0D 05        CALL    $050D               ; {}
1042: C9              RET                         
1043: CD C7 06        CALL    $06C7               ; {}
1046: CD 0D 05        CALL    $050D               ; {}
1049: C9              RET                         
104A: DD 21 50 80     LD      IX,$8050            
104E: C3 DA 0D        JP      $0DDA               ; {}
1051: DD 21 58 80     LD      IX,$8058            
1055: C3 DA 0D        JP      $0DDA               ; {}
1058: DD 21 60 80     LD      IX,$8060            
105C: C3 DA 0D        JP      $0DDA               ; {}
105F: 1F              RRA                         
1060: 0A              LD      A,(BC)              
1061: 3F              CCF                         
1062: 0E 5F           LD      C,$5F               
1064: 08              EX      AF,AF'              
1065: 85              ADD     A,L                 
1066: 85              ADD     A,L                 
1067: 85              ADD     A,L                 
1068: 8A              ADC     A,D                 
1069: 8A              ADC     A,D                 
106A: 8A              ADC     A,D                 
106B: 8A              ADC     A,D                 
106C: 91              SUB     C                   
106D: 91              SUB     C                   
106E: 91              SUB     C                   
106F: 91              SUB     C                   
1070: 8F              ADC     A,A                 
1071: 8F              ADC     A,A                 
1072: D6 93           SUB     $93                 
1074: 8F              ADC     A,A                 
1075: 93              SUB     E                   
1076: B6              OR      (HL)                
1077: 93              SUB     E                   
1078: 8F              ADC     A,A                 
1079: 93              SUB     E                   
107A: B6              OR      (HL)                
107B: FF              RST     0X38                
107C: 1F              RRA                         
107D: 0A              LD      A,(BC)              
107E: 5F              LD      E,A                 
107F: 08              EX      AF,AF'              
1080: 85              ADD     A,L                 
1081: 85              ADD     A,L                 
1082: 85              ADD     A,L                 
1083: 85              ADD     A,L                 
1084: 85              ADD     A,L                 
1085: 85              ADD     A,L                 
1086: 85              ADD     A,L                 
1087: 8E              ADC     A,(HL)              
1088: 8E              ADC     A,(HL)              
1089: 8E              ADC     A,(HL)              
108A: 8E              ADC     A,(HL)              
108B: 8C              ADC     A,H                 
108C: 8C              ADC     A,H                 
108D: D3 8F           OUT     ($8F),A             ; {}
108F: 8C              ADC     A,H                 
1090: 8F              ADC     A,A                 
1091: B3              OR      E                   
1092: 8F              ADC     A,A                 
1093: 8C              ADC     A,H                 
1094: 8F              ADC     A,A                 
1095: B3              OR      E                   
1096: FF              RST     0X38                
1097: 1F              RRA                         
1098: 0A              LD      A,(BC)              
1099: 5F              LD      E,A                 
109A: 08              EX      AF,AF'              
109B: 91              SUB     C                   
109C: 91              SUB     C                   
109D: 91              SUB     C                   
109E: 8A              ADC     A,D                 
109F: 8A              ADC     A,D                 
10A0: 8A              ADC     A,D                 
10A1: 8A              ADC     A,D                 
10A2: 96              SUB     (HL)                
10A3: 96              SUB     (HL)                
10A4: 96              SUB     (HL)                
10A5: 96              SUB     (HL)                
10A6: 94              SUB     H                   
10A7: 94              SUB     H                   
10A8: D6 93           SUB     $93                 
10AA: 8F              ADC     A,A                 
10AB: 93              SUB     E                   
10AC: B6              OR      (HL)                
10AD: 93              SUB     E                   
10AE: 8F              ADC     A,A                 
10AF: 93              SUB     E                   
10B0: B6              OR      (HL)                
10B1: FF              RST     0X38                
10B2: CD C7 06        CALL    $06C7               ; {}
10B5: 3E 02           LD      A,$02               
10B7: 32 73 80        LD      ($8073),A           
10BA: CD 0D 05        CALL    $050D               ; {}
10BD: C3 8E 0F        JP      $0F8E               ; {}
10C0: CD C7 06        CALL    $06C7               ; {}
10C3: CD 0D 05        CALL    $050D               ; {}
10C6: C9              RET                         
10C7: DD 21 50 80     LD      IX,$8050            
10CB: C3 DA 0D        JP      $0DDA               ; {}
10CE: DD 21 58 80     LD      IX,$8058            
10D2: C3 DA 0D        JP      $0DDA               ; {}
10D5: 1F              RRA                         
10D6: 0A              LD      A,(BC)              
10D7: 3F              CCF                         
10D8: 0A              LD      A,(BC)              
10D9: 5F              LD      E,A                 
10DA: 09              ADD     HL,BC               
10DB: 8D              ADC     A,L                 
10DC: 8F              ADC     A,A                 
10DD: 91              SUB     C                   
10DE: 8F              ADC     A,A                 
10DF: 91              SUB     C                   
10E0: 94              SUB     H                   
10E1: 91              SUB     C                   
10E2: 8F              ADC     A,A                 
10E3: 8D              ADC     A,L                 
10E4: 8F              ADC     A,A                 
10E5: 91              SUB     C                   
10E6: 8D              ADC     A,L                 
10E7: 8F              ADC     A,A                 
10E8: 8C              ADC     A,H                 
10E9: AD              XOR     L                   
10EA: FF              RST     0X38                
10EB: 1F              RRA                         
10EC: 0A              LD      A,(BC)              
10ED: 5F              LD      E,A                 
10EE: 09              ADD     HL,BC               
10EF: 8A              ADC     A,D                 
10F0: 8C              ADC     A,H                 
10F1: 8D              ADC     A,L                 
10F2: 8C              ADC     A,H                 
10F3: 8D              ADC     A,L                 
10F4: 8F              ADC     A,A                 
10F5: 8D              ADC     A,L                 
10F6: 8C              ADC     A,H                 
10F7: 8A              ADC     A,D                 
10F8: 8C              ADC     A,H                 
10F9: 8D              ADC     A,L                 
10FA: 8A              ADC     A,D                 
10FB: 8C              ADC     A,H                 
10FC: 88              ADC     A,B                 
10FD: AA              XOR     D                   
10FE: FF              RST     0X38                
10FF: FF              RST     0X38                
1100: CD BC 07        CALL    $07BC               ; {}
1103: 21 00 03        LD      HL,$0300            
1106: 22 83 80        LD      ($8083),HL          
1109: 21 80 80        LD      HL,$8080            
110C: 36 01           LD      (HL),$01            
110E: 21 00 08        LD      HL,$0800            
1111: 22 81 80        LD      ($8081),HL          
1114: CD C6 04        CALL    $04C6               ; {}
1117: CD 0D 05        CALL    $050D               ; {}
111A: 06 0B           LD      B,$0B               
111C: CD FE 05        CALL    $05FE               ; {}
111F: C9              RET                         
1120: 2A 83 80        LD      HL,($8083)          
1123: 2B              DEC     HL                  
1124: 22 83 80        LD      ($8083),HL          
1127: 7D              LD      A,L                 
1128: B4              OR      H                   
1129: 28 52           JR      Z,$117D             ; {}
112B: 3A 80 80        LD      A,($8080)           
112E: FE 00           CP      $00                 
1130: 28 1E           JR      Z,$1150             ; {}
1132: FE 01           CP      $01                 
1134: 28 0E           JR      Z,$1144             ; {}
1136: FE 02           CP      $02                 
1138: 28 05           JR      Z,$113F             ; {}
113A: 21 00 0A        LD      HL,$0A00            
113D: 18 08           JR      $1147               ; {}
113F: 21 00 06        LD      HL,$0600            
1142: 18 03           JR      $1147               ; {}
1144: 21 00 08        LD      HL,$0800            
1147: 22 81 80        LD      ($8081),HL          
114A: CD C6 04        CALL    $04C6               ; {}
114D: AF              XOR     A                   
114E: 18 28           JR      $1178               ; {}
1150: 2A 81 80        LD      HL,($8081)          
1153: 11 20 00        LD      DE,$0020            
1156: ED 52           SBC     HL,DE               
1158: 22 81 80        LD      ($8081),HL          
115B: 7C              LD      A,H                 
115C: FE 00           CP      $00                 
115E: 28 06           JR      Z,$1166             ; {}
1160: CD C6 04        CALL    $04C6               ; {}
1163: AF              XOR     A                   
1164: 18 12           JR      $1178               ; {}
1166: CD C6 04        CALL    $04C6               ; {}
1169: 3A 80 80        LD      A,($8080)           
116C: 3C              INC     A                   
116D: 32 80 80        LD      ($8080),A           
1170: FE 04           CP      $04                 
1172: 28 02           JR      Z,$1176             ; {}
1174: AF              XOR     A                   
1175: C9              RET                         
1176: 3E 01           LD      A,$01               
1178: 32 80 80        LD      ($8080),A           
117B: AF              XOR     A                   
117C: C9              RET                         
117D: 3E FF           LD      A,$FF               
117F: C9              RET                         
1180: CD BC 07        CALL    $07BC               ; {}
1183: 3E 01           LD      A,$01               
1185: 32 86 80        LD      ($8086),A           
1188: 3E 20           LD      A,$20               
118A: 32 87 80        LD      ($8087),A           
118D: 3E 06           LD      A,$06               
118F: 32 88 80        LD      ($8088),A           
1192: AF              XOR     A                   
1193: 32 89 80        LD      ($8089),A           
1196: 32 8A 80        LD      ($808A),A           
1199: 21 00 03        LD      HL,$0300            
119C: 22 8D 80        LD      ($808D),HL          
119F: 21 00 04        LD      HL,$0400            
11A2: 22 8B 80        LD      ($808B),HL          
11A5: CD C6 04        CALL    $04C6               ; {}
11A8: CD 0D 05        CALL    $050D               ; {}
11AB: 06 0B           LD      B,$0B               
11AD: CD FE 05        CALL    $05FE               ; {}
11B0: C9              RET                         
11B1: 2A 8D 80        LD      HL,($808D)          
11B4: 2B              DEC     HL                  
11B5: 7C              LD      A,H                 
11B6: B5              OR      L                   
11B7: 28 5D           JR      Z,$1216             ; {}
11B9: 22 8D 80        LD      ($808D),HL          
11BC: 3A 89 80        LD      A,($8089)           
11BF: FE 00           CP      $00                 
11C1: 28 06           JR      Z,$11C9             ; {}
11C3: FE 01           CP      $01                 
11C5: 28 24           JR      Z,$11EB             ; {}
11C7: AF              XOR     A                   
11C8: C9              RET                         
11C9: 21 86 80        LD      HL,$8086            
11CC: 35              DEC     (HL)                
11CD: 20 F8           JR      NZ,$11C7            ; {}
11CF: 36 01           LD      (HL),$01            
11D1: CD 80 06        CALL    $0680               ; {}
11D4: B7              OR      A                   
11D5: 11 08 00        LD      DE,$0008            
11D8: ED 52           SBC     HL,DE               
11DA: CD C6 04        CALL    $04C6               ; {}
11DD: 21 87 80        LD      HL,$8087            
11E0: 35              DEC     (HL)                
11E1: 20 E4           JR      NZ,$11C7            ; {}
11E3: 36 20           LD      (HL),$20            
11E5: 21 89 80        LD      HL,$8089            
11E8: 34              INC     (HL)                
11E9: 18 DC           JR      $11C7               ; {}
11EB: 2A 8B 80        LD      HL,($808B)          
11EE: 11 30 00        LD      DE,$0030            
11F1: 3A 8A 80        LD      A,($808A)           
11F4: E6 01           AND     $01                 
11F6: 20 1B           JR      NZ,$1213            ; {}
11F8: B7              OR      A                   
11F9: ED 52           SBC     HL,DE               
11FB: 22 8B 80        LD      ($808B),HL          
11FE: CD C6 04        CALL    $04C6               ; {}
1201: 21 88 80        LD      HL,$8088            
1204: 35              DEC     (HL)                
1205: 20 06           JR      NZ,$120D            ; {}
1207: 36 06           LD      (HL),$06            
1209: 21 8A 80        LD      HL,$808A            
120C: 34              INC     (HL)                
120D: 21 89 80        LD      HL,$8089            
1210: 35              DEC     (HL)                
1211: 18 B4           JR      $11C7               ; {}
1213: 19              ADD     HL,DE               
1214: 18 E5           JR      $11FB               ; {}
1216: 3E FF           LD      A,$FF               
1218: C9              RET                         
1219: C9              RET                         
121A: 3E FF           LD      A,$FF               
121C: C9              RET                         
121D: CD 82 07        CALL    $0782               ; {}
1220: 3E 01           LD      A,$01               
1222: 32 A0 80        LD      ($80A0),A           
1225: 3E 20           LD      A,$20               
1227: 32 A1 80        LD      ($80A1),A           
122A: 3E 10           LD      A,$10               
122C: 32 A2 80        LD      ($80A2),A           
122F: AF              XOR     A                   
1230: 32 A5 80        LD      ($80A5),A           
1233: 32 A6 80        LD      ($80A6),A           
1236: 21 00 01        LD      HL,$0100            
1239: 22 A3 80        LD      ($80A3),HL          
123C: 21 00 05        LD      HL,$0500            
123F: 22 A7 80        LD      ($80A7),HL          
1242: CD C6 04        CALL    $04C6               ; {}
1245: CD 0D 05        CALL    $050D               ; {}
1248: 06 0D           LD      B,$0D               
124A: CD FE 05        CALL    $05FE               ; {}
124D: C9              RET                         
124E: 2A A3 80        LD      HL,($80A3)          
1251: 2B              DEC     HL                  
1252: 7C              LD      A,H                 
1253: B5              OR      L                   
1254: 28 5D           JR      Z,$12B3             ; {}
1256: 22 A3 80        LD      ($80A3),HL          
1259: 3A A5 80        LD      A,($80A5)           
125C: FE 00           CP      $00                 
125E: 28 06           JR      Z,$1266             ; {}
1260: FE 01           CP      $01                 
1262: 28 24           JR      Z,$1288             ; {}
1264: AF              XOR     A                   
1265: C9              RET                         
1266: 21 A0 80        LD      HL,$80A0            
1269: 35              DEC     (HL)                
126A: 20 F8           JR      NZ,$1264            ; {}
126C: 36 01           LD      (HL),$01            
126E: CD 80 06        CALL    $0680               ; {}
1271: B7              OR      A                   
1272: 11 04 00        LD      DE,$0004            
1275: ED 52           SBC     HL,DE               
1277: CD C6 04        CALL    $04C6               ; {}
127A: 21 A1 80        LD      HL,$80A1            
127D: 35              DEC     (HL)                
127E: 20 E4           JR      NZ,$1264            ; {}
1280: 36 20           LD      (HL),$20            
1282: 21 A5 80        LD      HL,$80A5            
1285: 34              INC     (HL)                
1286: 18 DC           JR      $1264               ; {}
1288: 2A A7 80        LD      HL,($80A7)          
128B: 11 50 00        LD      DE,$0050            
128E: 3A A6 80        LD      A,($80A6)           
1291: E6 01           AND     $01                 
1293: 20 1B           JR      NZ,$12B0            ; {}
1295: B7              OR      A                   
1296: ED 52           SBC     HL,DE               
1298: 22 A7 80        LD      ($80A7),HL          
129B: CD C6 04        CALL    $04C6               ; {}
129E: 21 A2 80        LD      HL,$80A2            
12A1: 35              DEC     (HL)                
12A2: 20 06           JR      NZ,$12AA            ; {}
12A4: 36 10           LD      (HL),$10            
12A6: 21 A6 80        LD      HL,$80A6            
12A9: 34              INC     (HL)                
12AA: 21 A5 80        LD      HL,$80A5            
12AD: 35              DEC     (HL)                
12AE: 18 B4           JR      $1264               ; {}
12B0: 19              ADD     HL,DE               
12B1: 18 E5           JR      $1298               ; {}
12B3: 3E FF           LD      A,$FF               
12B5: C9              RET                         
12B6: CD C7 06        CALL    $06C7               ; {}
12B9: 3E 18           LD      A,$18               
12BB: 32 B0 80        LD      ($80B0),A           
12BE: 21 00 01        LD      HL,$0100            
12C1: 22 B1 80        LD      ($80B1),HL          
12C4: AF              XOR     A                   
12C5: 32 B3 80        LD      ($80B3),A           
12C8: 21 00 02        LD      HL,$0200            
12CB: 22 B4 80        LD      ($80B4),HL          
12CE: 16 06           LD      D,$06               
12D0: 1E 00           LD      E,$00               
12D2: CD 4C 05        CALL    $054C               ; {}
12D5: CD 80 05        CALL    $0580               ; {}
12D8: 06 03           LD      B,$03               
12DA: CD FE 05        CALL    $05FE               ; {}
12DD: C9              RET                         
12DE: 2A B4 80        LD      HL,($80B4)          
12E1: 2B              DEC     HL                  
12E2: 7C              LD      A,H                 
12E3: B5              OR      L                   
12E4: 28 4B           JR      Z,$1331             ; {}
12E6: 22 B4 80        LD      ($80B4),HL          
12E9: 3A B3 80        LD      A,($80B3)           
12EC: FE 00           CP      $00                 
12EE: 28 1B           JR      Z,$130B             ; {}
12F0: 2A B1 80        LD      HL,($80B1)          
12F3: 2B              DEC     HL                  
12F4: 7C              LD      A,H                 
12F5: B5              OR      L                   
12F6: 20 34           JR      NZ,$132C            ; {}
12F8: 21 00 01        LD      HL,$0100            
12FB: 22 B1 80        LD      ($80B1),HL          
12FE: 16 06           LD      D,$06               
1300: 1E 00           LD      E,$00               
1302: CD 4C 05        CALL    $054C               ; {}
1305: AF              XOR     A                   
1306: 32 B3 80        LD      ($80B3),A           
1309: AF              XOR     A                   
130A: C9              RET                         
130B: 21 B0 80        LD      HL,$80B0            
130E: 35              DEC     (HL)                
130F: 20 F8           JR      NZ,$1309            ; {}
1311: 36 18           LD      (HL),$18            
1313: 16 06           LD      D,$06               
1315: CD 35 06        CALL    $0635               ; {}
1318: 1C              INC     E                   
1319: 7B              LD      A,E                 
131A: FE 08           CP      $08                 
131C: 28 05           JR      Z,$1323             ; {}
131E: CD 4C 05        CALL    $054C               ; {}
1321: 18 E6           JR      $1309               ; {}
1323: CD 4C 05        CALL    $054C               ; {}
1326: 21 B3 80        LD      HL,$80B3            
1329: 34              INC     (HL)                
132A: 18 DD           JR      $1309               ; {}
132C: 22 B1 80        LD      ($80B1),HL          
132F: 18 D8           JR      $1309               ; {}
1331: 3E FF           LD      A,$FF               
1333: C9              RET                         
1334: CD BC 07        CALL    $07BC               ; {}
1337: 3E 01           LD      A,$01               
1339: 32 C0 80        LD      ($80C0),A           
133C: 21 00 08        LD      HL,$0800            
133F: 22 C3 80        LD      ($80C3),HL          
1342: AF              XOR     A                   
1343: 32 C5 80        LD      ($80C5),A           
1346: 21 00 02        LD      HL,$0200            
1349: 22 C6 80        LD      ($80C6),HL          
134C: 21 00 05        LD      HL,$0500            
134F: CD C6 04        CALL    $04C6               ; {}
1352: CD 0D 05        CALL    $050D               ; {}
1355: 06 08           LD      B,$08               
1357: CD FE 05        CALL    $05FE               ; {}
135A: C9              RET                         
135B: 2A C6 80        LD      HL,($80C6)          
135E: 2B              DEC     HL                  
135F: 7C              LD      A,H                 
1360: B5              OR      L                   
1361: 28 43           JR      Z,$13A6             ; {}
1363: 22 C6 80        LD      ($80C6),HL          
1366: 21 C0 80        LD      HL,$80C0            
1369: 35              DEC     (HL)                
136A: 20 2C           JR      NZ,$1398            ; {}
136C: 36 01           LD      (HL),$01            
136E: CD 80 06        CALL    $0680               ; {}
1371: 11 08 00        LD      DE,$0008            
1374: 19              ADD     HL,DE               
1375: ED 5B C3 80     LD      DE,($80C3)          
1379: 7C              LD      A,H                 
137A: BA              CP      D                   
137B: 20 18           JR      NZ,$1395            ; {}
137D: 7D              LD      A,L                 
137E: BB              CP      E                   
137F: 20 14           JR      NZ,$1395            ; {}
1381: 3A C5 80        LD      A,($80C5)           
1384: B7              OR      A                   
1385: 20 13           JR      NZ,$139A            ; {}
1387: 21 00 0B        LD      HL,$0B00            
138A: 22 C3 80        LD      ($80C3),HL          
138D: 3E FF           LD      A,$FF               
138F: 32 C5 80        LD      ($80C5),A           
1392: 21 00 05        LD      HL,$0500            
1395: CD C6 04        CALL    $04C6               ; {}
1398: AF              XOR     A                   
1399: C9              RET                         
139A: 21 00 08        LD      HL,$0800            
139D: 22 C3 80        LD      ($80C3),HL          
13A0: AF              XOR     A                   
13A1: 32 C5 80        LD      ($80C5),A           
13A4: 18 EC           JR      $1392               ; {}
13A6: 3E FF           LD      A,$FF               
13A8: C9              RET                         
13A9: CD 48 07        CALL    $0748               ; {}
13AC: 3E 08           LD      A,$08               
13AE: 32 D0 80        LD      ($80D0),A           
13B1: 3E 05           LD      A,$05               
13B3: 32 D1 80        LD      ($80D1),A           
13B6: 3E 0C           LD      A,$0C               
13B8: 32 D2 80        LD      ($80D2),A           
13BB: AF              XOR     A                   
13BC: 32 D3 80        LD      ($80D3),A           
13BF: 21 50 00        LD      HL,$0050            
13C2: CD C6 04        CALL    $04C6               ; {}
13C5: CD 0D 05        CALL    $050D               ; {}
13C8: 06 00           LD      B,$00               
13CA: CD FE 05        CALL    $05FE               ; {}
13CD: C9              RET                         
13CE: 3A D3 80        LD      A,($80D3)           
13D1: FE 00           CP      $00                 
13D3: 28 18           JR      Z,$13ED             ; {}
13D5: FE 01           CP      $01                 
13D7: 28 26           JR      Z,$13FF             ; {}
13D9: FE 02           CP      $02                 
13DB: 28 27           JR      Z,$1404             ; {}
13DD: FE 03           CP      $03                 
13DF: 28 33           JR      Z,$1414             ; {}
13E1: 21 D2 80        LD      HL,$80D2            
13E4: 35              DEC     (HL)                
13E5: 28 32           JR      Z,$1419             ; {}
13E7: AF              XOR     A                   
13E8: 32 D3 80        LD      ($80D3),A           
13EB: AF              XOR     A                   
13EC: C9              RET                         
13ED: CD 4B 06        CALL    $064B               ; {}
13F0: 3C              INC     A                   
13F1: FE 0A           CP      $0A                 
13F3: 20 04           JR      NZ,$13F9            ; {}
13F5: 21 D3 80        LD      HL,$80D3            
13F8: 34              INC     (HL)                
13F9: 47              LD      B,A                 
13FA: CD FE 05        CALL    $05FE               ; {}
13FD: 18 EC           JR      $13EB               ; {}
13FF: CD 1C 14        CALL    $141C               ; {}
1402: 18 E7           JR      $13EB               ; {}
1404: CD 4B 06        CALL    $064B               ; {}
1407: 3D              DEC     A                   
1408: 20 04           JR      NZ,$140E            ; {}
140A: 21 D3 80        LD      HL,$80D3            
140D: 34              INC     (HL)                
140E: 47              LD      B,A                 
140F: CD FE 05        CALL    $05FE               ; {}
1412: 18 D7           JR      $13EB               ; {}
1414: CD 29 14        CALL    $1429               ; {}
1417: 18 D2           JR      $13EB               ; {}
1419: 3E FF           LD      A,$FF               
141B: C9              RET                         
141C: 21 D0 80        LD      HL,$80D0            
141F: 35              DEC     (HL)                
1420: C0              RET     NZ                  
1421: 3E 08           LD      A,$08               
1423: 77              LD      (HL),A              
1424: 21 D3 80        LD      HL,$80D3            
1427: 34              INC     (HL)                
1428: C9              RET                         
1429: 21 D1 80        LD      HL,$80D1            
142C: 35              DEC     (HL)                
142D: C0              RET     NZ                  
142E: 3E 05           LD      A,$05               
1430: 77              LD      (HL),A              
1431: 21 D3 80        LD      HL,$80D3            
1434: 34              INC     (HL)                
1435: C9              RET                         
1436: FF              RST     0X38                
1437: FF              RST     0X38                
1438: FF              RST     0X38                
1439: FF              RST     0X38                
143A: FF              RST     0X38                
143B: FF              RST     0X38                
143C: FF              RST     0X38                
143D: FF              RST     0X38                
143E: FF              RST     0X38                
143F: FF              RST     0X38                
1440: FF              RST     0X38                
1441: FF              RST     0X38                
1442: FF              RST     0X38                
1443: FF              RST     0X38                
1444: FF              RST     0X38                
1445: FF              RST     0X38                
1446: FF              RST     0X38                
1447: FF              RST     0X38                
1448: FF              RST     0X38                
1449: FF              RST     0X38                
144A: FF              RST     0X38                
144B: FF              RST     0X38                
144C: FF              RST     0X38                
144D: FF              RST     0X38                
144E: FF              RST     0X38                
144F: FF              RST     0X38                
1450: FF              RST     0X38                
1451: FF              RST     0X38                
1452: FF              RST     0X38                
1453: FF              RST     0X38                
1454: FF              RST     0X38                
1455: FF              RST     0X38                
1456: FF              RST     0X38                
1457: FF              RST     0X38                
1458: FF              RST     0X38                
1459: FF              RST     0X38                
145A: FF              RST     0X38                
145B: FF              RST     0X38                
145C: FF              RST     0X38                
145D: FF              RST     0X38                
145E: FF              RST     0X38                
145F: FF              RST     0X38                
1460: FF              RST     0X38                
1461: FF              RST     0X38                
1462: FF              RST     0X38                
1463: FF              RST     0X38                
1464: FF              RST     0X38                
1465: FF              RST     0X38                
1466: FF              RST     0X38                
1467: FF              RST     0X38                
1468: FF              RST     0X38                
1469: FF              RST     0X38                
146A: FF              RST     0X38                
146B: FF              RST     0X38                
146C: FF              RST     0X38                
146D: FF              RST     0X38                
146E: FF              RST     0X38                
146F: FF              RST     0X38                
1470: FF              RST     0X38                
1471: FF              RST     0X38                
1472: FF              RST     0X38                
1473: FF              RST     0X38                
1474: FF              RST     0X38                
1475: FF              RST     0X38                
1476: FF              RST     0X38                
1477: FF              RST     0X38                
1478: FF              RST     0X38                
1479: FF              RST     0X38                
147A: FF              RST     0X38                
147B: FF              RST     0X38                
147C: FF              RST     0X38                
147D: FF              RST     0X38                
147E: FF              RST     0X38                
147F: FF              RST     0X38                
1480: FF              RST     0X38                
1481: FF              RST     0X38                
1482: FF              RST     0X38                
1483: FF              RST     0X38                
1484: FF              RST     0X38                
1485: FF              RST     0X38                
1486: FF              RST     0X38                
1487: FF              RST     0X38                
1488: FF              RST     0X38                
1489: FF              RST     0X38                
148A: FF              RST     0X38                
148B: FF              RST     0X38                
148C: FF              RST     0X38                
148D: FF              RST     0X38                
148E: FF              RST     0X38                
148F: FF              RST     0X38                
1490: FF              RST     0X38                
1491: FF              RST     0X38                
1492: FF              RST     0X38                
1493: FF              RST     0X38                
1494: FF              RST     0X38                
1495: FF              RST     0X38                
1496: FF              RST     0X38                
1497: FF              RST     0X38                
1498: FF              RST     0X38                
1499: FF              RST     0X38                
149A: FF              RST     0X38                
149B: FF              RST     0X38                
149C: FF              RST     0X38                
149D: FF              RST     0X38                
149E: FF              RST     0X38                
149F: FF              RST     0X38                
14A0: FF              RST     0X38                
14A1: FF              RST     0X38                
14A2: FF              RST     0X38                
14A3: FF              RST     0X38                
14A4: FF              RST     0X38                
14A5: FF              RST     0X38                
14A6: FF              RST     0X38                
14A7: FF              RST     0X38                
14A8: FF              RST     0X38                
14A9: FF              RST     0X38                
14AA: FF              RST     0X38                
14AB: FF              RST     0X38                
14AC: FF              RST     0X38                
14AD: FF              RST     0X38                
14AE: FF              RST     0X38                
14AF: FF              RST     0X38                
14B0: FF              RST     0X38                
14B1: FF              RST     0X38                
14B2: FF              RST     0X38                
14B3: FF              RST     0X38                
14B4: FF              RST     0X38                
14B5: FF              RST     0X38                
14B6: FF              RST     0X38                
14B7: FF              RST     0X38                
14B8: FF              RST     0X38                
14B9: FF              RST     0X38                
14BA: FF              RST     0X38                
14BB: FF              RST     0X38                
14BC: FF              RST     0X38                
14BD: FF              RST     0X38                
14BE: FF              RST     0X38                
14BF: FF              RST     0X38                
14C0: FF              RST     0X38                
14C1: FF              RST     0X38                
14C2: FF              RST     0X38                
14C3: FF              RST     0X38                
14C4: FF              RST     0X38                
14C5: FF              RST     0X38                
14C6: FF              RST     0X38                
14C7: FF              RST     0X38                
14C8: FF              RST     0X38                
14C9: FF              RST     0X38                
14CA: FF              RST     0X38                
14CB: FF              RST     0X38                
14CC: FF              RST     0X38                
14CD: FF              RST     0X38                
14CE: FF              RST     0X38                
14CF: FF              RST     0X38                
14D0: FF              RST     0X38                
14D1: FF              RST     0X38                
14D2: FF              RST     0X38                
14D3: FF              RST     0X38                
14D4: FF              RST     0X38                
14D5: FF              RST     0X38                
14D6: FF              RST     0X38                
14D7: FF              RST     0X38                
14D8: FF              RST     0X38                
14D9: FF              RST     0X38                
14DA: FF              RST     0X38                
14DB: FF              RST     0X38                
14DC: FF              RST     0X38                
14DD: FF              RST     0X38                
14DE: FF              RST     0X38                
14DF: FF              RST     0X38                
14E0: FF              RST     0X38                
14E1: FF              RST     0X38                
14E2: FF              RST     0X38                
14E3: FF              RST     0X38                
14E4: FF              RST     0X38                
14E5: FF              RST     0X38                
14E6: FF              RST     0X38                
14E7: FF              RST     0X38                
14E8: FF              RST     0X38                
14E9: FF              RST     0X38                
14EA: FF              RST     0X38                
14EB: FF              RST     0X38                
14EC: FF              RST     0X38                
14ED: FF              RST     0X38                
14EE: FF              RST     0X38                
14EF: FF              RST     0X38                
14F0: FF              RST     0X38                
14F1: FF              RST     0X38                
14F2: FF              RST     0X38                
14F3: FF              RST     0X38                
14F4: FF              RST     0X38                
14F5: FF              RST     0X38                
14F6: FF              RST     0X38                
14F7: FF              RST     0X38                
14F8: FF              RST     0X38                
14F9: FF              RST     0X38                
14FA: FF              RST     0X38                
14FB: FF              RST     0X38                
14FC: FF              RST     0X38                
14FD: FF              RST     0X38                
14FE: FF              RST     0X38                
14FF: FF              RST     0X38                
1500: FF              RST     0X38                
1501: FF              RST     0X38                
1502: FF              RST     0X38                
1503: FF              RST     0X38                
1504: FF              RST     0X38                
1505: FF              RST     0X38                
1506: FF              RST     0X38                
1507: FF              RST     0X38                
1508: FF              RST     0X38                
1509: FF              RST     0X38                
150A: FF              RST     0X38                
150B: FF              RST     0X38                
150C: FF              RST     0X38                
150D: FF              RST     0X38                
150E: FF              RST     0X38                
150F: FF              RST     0X38                
1510: FF              RST     0X38                
1511: FF              RST     0X38                
1512: FF              RST     0X38                
1513: FF              RST     0X38                
1514: FF              RST     0X38                
1515: FF              RST     0X38                
1516: FF              RST     0X38                
1517: FF              RST     0X38                
1518: FF              RST     0X38                
1519: FF              RST     0X38                
151A: FF              RST     0X38                
151B: FF              RST     0X38                
151C: FF              RST     0X38                
151D: FF              RST     0X38                
151E: FF              RST     0X38                
151F: FF              RST     0X38                
1520: FF              RST     0X38                
1521: FF              RST     0X38                
1522: FF              RST     0X38                
1523: FF              RST     0X38                
1524: FF              RST     0X38                
1525: FF              RST     0X38                
1526: FF              RST     0X38                
1527: FF              RST     0X38                
1528: FF              RST     0X38                
1529: FF              RST     0X38                
152A: FF              RST     0X38                
152B: FF              RST     0X38                
152C: FF              RST     0X38                
152D: FF              RST     0X38                
152E: FF              RST     0X38                
152F: FF              RST     0X38                
1530: FF              RST     0X38                
1531: FF              RST     0X38                
1532: FF              RST     0X38                
1533: FF              RST     0X38                
1534: FF              RST     0X38                
1535: FF              RST     0X38                
1536: FF              RST     0X38                
1537: FF              RST     0X38                
1538: FF              RST     0X38                
1539: FF              RST     0X38                
153A: FF              RST     0X38                
153B: FF              RST     0X38                
153C: FF              RST     0X38                
153D: FF              RST     0X38                
153E: FF              RST     0X38                
153F: FF              RST     0X38                
1540: FF              RST     0X38                
1541: FF              RST     0X38                
1542: FF              RST     0X38                
1543: FF              RST     0X38                
1544: FF              RST     0X38                
1545: FF              RST     0X38                
1546: FF              RST     0X38                
1547: FF              RST     0X38                
1548: FF              RST     0X38                
1549: FF              RST     0X38                
154A: FF              RST     0X38                
154B: FF              RST     0X38                
154C: FF              RST     0X38                
154D: FF              RST     0X38                
154E: FF              RST     0X38                
154F: FF              RST     0X38                
1550: FF              RST     0X38                
1551: FF              RST     0X38                
1552: FF              RST     0X38                
1553: FF              RST     0X38                
1554: FF              RST     0X38                
1555: FF              RST     0X38                
1556: FF              RST     0X38                
1557: FF              RST     0X38                
1558: FF              RST     0X38                
1559: FF              RST     0X38                
155A: FF              RST     0X38                
155B: FF              RST     0X38                
155C: FF              RST     0X38                
155D: FF              RST     0X38                
155E: FF              RST     0X38                
155F: FF              RST     0X38                
1560: FF              RST     0X38                
1561: FF              RST     0X38                
1562: FF              RST     0X38                
1563: FF              RST     0X38                
1564: FF              RST     0X38                
1565: FF              RST     0X38                
1566: FF              RST     0X38                
1567: FF              RST     0X38                
1568: FF              RST     0X38                
1569: FF              RST     0X38                
156A: FF              RST     0X38                
156B: FF              RST     0X38                
156C: FF              RST     0X38                
156D: FF              RST     0X38                
156E: FF              RST     0X38                
156F: FF              RST     0X38                
1570: FF              RST     0X38                
1571: FF              RST     0X38                
1572: FF              RST     0X38                
1573: FF              RST     0X38                
1574: FF              RST     0X38                
1575: FF              RST     0X38                
1576: FF              RST     0X38                
1577: FF              RST     0X38                
1578: FF              RST     0X38                
1579: FF              RST     0X38                
157A: FF              RST     0X38                
157B: FF              RST     0X38                
157C: FF              RST     0X38                
157D: FF              RST     0X38                
157E: FF              RST     0X38                
157F: FF              RST     0X38                
1580: FF              RST     0X38                
1581: FF              RST     0X38                
1582: FF              RST     0X38                
1583: FF              RST     0X38                
1584: FF              RST     0X38                
1585: FF              RST     0X38                
1586: FF              RST     0X38                
1587: FF              RST     0X38                
1588: FF              RST     0X38                
1589: FF              RST     0X38                
158A: FF              RST     0X38                
158B: FF              RST     0X38                
158C: FF              RST     0X38                
158D: FF              RST     0X38                
158E: FF              RST     0X38                
158F: FF              RST     0X38                
1590: FF              RST     0X38                
1591: FF              RST     0X38                
1592: FF              RST     0X38                
1593: FF              RST     0X38                
1594: FF              RST     0X38                
1595: FF              RST     0X38                
1596: FF              RST     0X38                
1597: FF              RST     0X38                
1598: FF              RST     0X38                
1599: FF              RST     0X38                
159A: FF              RST     0X38                
159B: FF              RST     0X38                
159C: FF              RST     0X38                
159D: FF              RST     0X38                
159E: FF              RST     0X38                
159F: FF              RST     0X38                
15A0: FF              RST     0X38                
15A1: FF              RST     0X38                
15A2: FF              RST     0X38                
15A3: FF              RST     0X38                
15A4: FF              RST     0X38                
15A5: FF              RST     0X38                
15A6: FF              RST     0X38                
15A7: FF              RST     0X38                
15A8: FF              RST     0X38                
15A9: FF              RST     0X38                
15AA: FF              RST     0X38                
15AB: FF              RST     0X38                
15AC: FF              RST     0X38                
15AD: FF              RST     0X38                
15AE: FF              RST     0X38                
15AF: FF              RST     0X38                
15B0: FF              RST     0X38                
15B1: FF              RST     0X38                
15B2: FF              RST     0X38                
15B3: FF              RST     0X38                
15B4: FF              RST     0X38                
15B5: FF              RST     0X38                
15B6: FF              RST     0X38                
15B7: FF              RST     0X38                
15B8: FF              RST     0X38                
15B9: FF              RST     0X38                
15BA: FF              RST     0X38                
15BB: FF              RST     0X38                
15BC: FF              RST     0X38                
15BD: FF              RST     0X38                
15BE: FF              RST     0X38                
15BF: FF              RST     0X38                
15C0: FF              RST     0X38                
15C1: FF              RST     0X38                
15C2: FF              RST     0X38                
15C3: FF              RST     0X38                
15C4: FF              RST     0X38                
15C5: FF              RST     0X38                
15C6: FF              RST     0X38                
15C7: FF              RST     0X38                
15C8: FF              RST     0X38                
15C9: FF              RST     0X38                
15CA: FF              RST     0X38                
15CB: FF              RST     0X38                
15CC: FF              RST     0X38                
15CD: FF              RST     0X38                
15CE: FF              RST     0X38                
15CF: FF              RST     0X38                
15D0: FF              RST     0X38                
15D1: FF              RST     0X38                
15D2: FF              RST     0X38                
15D3: FF              RST     0X38                
15D4: FF              RST     0X38                
15D5: FF              RST     0X38                
15D6: FF              RST     0X38                
15D7: FF              RST     0X38                
15D8: FF              RST     0X38                
15D9: FF              RST     0X38                
15DA: FF              RST     0X38                
15DB: FF              RST     0X38                
15DC: FF              RST     0X38                
15DD: FF              RST     0X38                
15DE: FF              RST     0X38                
15DF: FF              RST     0X38                
15E0: FF              RST     0X38                
15E1: FF              RST     0X38                
15E2: FF              RST     0X38                
15E3: FF              RST     0X38                
15E4: FF              RST     0X38                
15E5: FF              RST     0X38                
15E6: FF              RST     0X38                
15E7: FF              RST     0X38                
15E8: FF              RST     0X38                
15E9: FF              RST     0X38                
15EA: FF              RST     0X38                
15EB: FF              RST     0X38                
15EC: FF              RST     0X38                
15ED: FF              RST     0X38                
15EE: FF              RST     0X38                
15EF: FF              RST     0X38                
15F0: FF              RST     0X38                
15F1: FF              RST     0X38                
15F2: FF              RST     0X38                
15F3: FF              RST     0X38                
15F4: FF              RST     0X38                
15F5: FF              RST     0X38                
15F6: FF              RST     0X38                
15F7: FF              RST     0X38                
15F8: FF              RST     0X38                
15F9: FF              RST     0X38                
15FA: FF              RST     0X38                
15FB: FF              RST     0X38                
15FC: FF              RST     0X38                
15FD: FF              RST     0X38                
15FE: FF              RST     0X38                
15FF: FF              RST     0X38                
1600: FF              RST     0X38                
1601: FF              RST     0X38                
1602: FF              RST     0X38                
1603: FF              RST     0X38                
1604: FF              RST     0X38                
1605: FF              RST     0X38                
1606: FF              RST     0X38                
1607: FF              RST     0X38                
1608: FF              RST     0X38                
1609: FF              RST     0X38                
160A: FF              RST     0X38                
160B: FF              RST     0X38                
160C: FF              RST     0X38                
160D: FF              RST     0X38                
160E: FF              RST     0X38                
160F: FF              RST     0X38                
1610: FF              RST     0X38                
1611: FF              RST     0X38                
1612: FF              RST     0X38                
1613: FF              RST     0X38                
1614: FF              RST     0X38                
1615: FF              RST     0X38                
1616: FF              RST     0X38                
1617: FF              RST     0X38                
1618: FF              RST     0X38                
1619: FF              RST     0X38                
161A: FF              RST     0X38                
161B: FF              RST     0X38                
161C: FF              RST     0X38                
161D: FF              RST     0X38                
161E: FF              RST     0X38                
161F: FF              RST     0X38                
1620: FF              RST     0X38                
1621: FF              RST     0X38                
1622: FF              RST     0X38                
1623: FF              RST     0X38                
1624: FF              RST     0X38                
1625: FF              RST     0X38                
1626: FF              RST     0X38                
1627: FF              RST     0X38                
1628: FF              RST     0X38                
1629: FF              RST     0X38                
162A: FF              RST     0X38                
162B: FF              RST     0X38                
162C: FF              RST     0X38                
162D: FF              RST     0X38                
162E: FF              RST     0X38                
162F: FF              RST     0X38                
1630: FF              RST     0X38                
1631: FF              RST     0X38                
1632: FF              RST     0X38                
1633: FF              RST     0X38                
1634: FF              RST     0X38                
1635: FF              RST     0X38                
1636: FF              RST     0X38                
1637: FF              RST     0X38                
1638: FF              RST     0X38                
1639: FF              RST     0X38                
163A: FF              RST     0X38                
163B: FF              RST     0X38                
163C: FF              RST     0X38                
163D: FF              RST     0X38                
163E: FF              RST     0X38                
163F: FF              RST     0X38                
1640: FF              RST     0X38                
1641: FF              RST     0X38                
1642: FF              RST     0X38                
1643: FF              RST     0X38                
1644: FF              RST     0X38                
1645: FF              RST     0X38                
1646: FF              RST     0X38                
1647: FF              RST     0X38                
1648: FF              RST     0X38                
1649: FF              RST     0X38                
164A: FF              RST     0X38                
164B: FF              RST     0X38                
164C: FF              RST     0X38                
164D: FF              RST     0X38                
164E: FF              RST     0X38                
164F: FF              RST     0X38                
1650: FF              RST     0X38                
1651: FF              RST     0X38                
1652: FF              RST     0X38                
1653: FF              RST     0X38                
1654: FF              RST     0X38                
1655: FF              RST     0X38                
1656: FF              RST     0X38                
1657: FF              RST     0X38                
1658: FF              RST     0X38                
1659: FF              RST     0X38                
165A: FF              RST     0X38                
165B: FF              RST     0X38                
165C: FF              RST     0X38                
165D: FF              RST     0X38                
165E: FF              RST     0X38                
165F: FF              RST     0X38                
1660: FF              RST     0X38                
1661: FF              RST     0X38                
1662: FF              RST     0X38                
1663: FF              RST     0X38                
1664: FF              RST     0X38                
1665: FF              RST     0X38                
1666: FF              RST     0X38                
1667: FF              RST     0X38                
1668: FF              RST     0X38                
1669: FF              RST     0X38                
166A: FF              RST     0X38                
166B: FF              RST     0X38                
166C: FF              RST     0X38                
166D: FF              RST     0X38                
166E: FF              RST     0X38                
166F: FF              RST     0X38                
1670: FF              RST     0X38                
1671: FF              RST     0X38                
1672: FF              RST     0X38                
1673: FF              RST     0X38                
1674: FF              RST     0X38                
1675: FF              RST     0X38                
1676: FF              RST     0X38                
1677: FF              RST     0X38                
1678: FF              RST     0X38                
1679: FF              RST     0X38                
167A: FF              RST     0X38                
167B: FF              RST     0X38                
167C: FF              RST     0X38                
167D: FF              RST     0X38                
167E: FF              RST     0X38                
167F: FF              RST     0X38                
1680: FF              RST     0X38                
1681: FF              RST     0X38                
1682: FF              RST     0X38                
1683: FF              RST     0X38                
1684: FF              RST     0X38                
1685: FF              RST     0X38                
1686: FF              RST     0X38                
1687: FF              RST     0X38                
1688: FF              RST     0X38                
1689: FF              RST     0X38                
168A: FF              RST     0X38                
168B: FF              RST     0X38                
168C: FF              RST     0X38                
168D: FF              RST     0X38                
168E: FF              RST     0X38                
168F: FF              RST     0X38                
1690: FF              RST     0X38                
1691: FF              RST     0X38                
1692: FF              RST     0X38                
1693: FF              RST     0X38                
1694: FF              RST     0X38                
1695: FF              RST     0X38                
1696: FF              RST     0X38                
1697: FF              RST     0X38                
1698: FF              RST     0X38                
1699: FF              RST     0X38                
169A: FF              RST     0X38                
169B: FF              RST     0X38                
169C: FF              RST     0X38                
169D: FF              RST     0X38                
169E: FF              RST     0X38                
169F: FF              RST     0X38                
16A0: FF              RST     0X38                
16A1: FF              RST     0X38                
16A2: FF              RST     0X38                
16A3: FF              RST     0X38                
16A4: FF              RST     0X38                
16A5: FF              RST     0X38                
16A6: FF              RST     0X38                
16A7: FF              RST     0X38                
16A8: FF              RST     0X38                
16A9: FF              RST     0X38                
16AA: FF              RST     0X38                
16AB: FF              RST     0X38                
16AC: FF              RST     0X38                
16AD: FF              RST     0X38                
16AE: FF              RST     0X38                
16AF: FF              RST     0X38                
16B0: FF              RST     0X38                
16B1: FF              RST     0X38                
16B2: FF              RST     0X38                
16B3: FF              RST     0X38                
16B4: FF              RST     0X38                
16B5: FF              RST     0X38                
16B6: FF              RST     0X38                
16B7: FF              RST     0X38                
16B8: FF              RST     0X38                
16B9: FF              RST     0X38                
16BA: FF              RST     0X38                
16BB: FF              RST     0X38                
16BC: FF              RST     0X38                
16BD: FF              RST     0X38                
16BE: FF              RST     0X38                
16BF: FF              RST     0X38                
16C0: FF              RST     0X38                
16C1: FF              RST     0X38                
16C2: FF              RST     0X38                
16C3: FF              RST     0X38                
16C4: FF              RST     0X38                
16C5: FF              RST     0X38                
16C6: FF              RST     0X38                
16C7: FF              RST     0X38                
16C8: FF              RST     0X38                
16C9: FF              RST     0X38                
16CA: FF              RST     0X38                
16CB: FF              RST     0X38                
16CC: FF              RST     0X38                
16CD: FF              RST     0X38                
16CE: FF              RST     0X38                
16CF: FF              RST     0X38                
16D0: FF              RST     0X38                
16D1: FF              RST     0X38                
16D2: FF              RST     0X38                
16D3: FF              RST     0X38                
16D4: FF              RST     0X38                
16D5: FF              RST     0X38                
16D6: FF              RST     0X38                
16D7: FF              RST     0X38                
16D8: FF              RST     0X38                
16D9: FF              RST     0X38                
16DA: FF              RST     0X38                
16DB: FF              RST     0X38                
16DC: FF              RST     0X38                
16DD: FF              RST     0X38                
16DE: FF              RST     0X38                
16DF: FF              RST     0X38                
16E0: FF              RST     0X38                
16E1: FF              RST     0X38                
16E2: FF              RST     0X38                
16E3: FF              RST     0X38                
16E4: FF              RST     0X38                
16E5: FF              RST     0X38                
16E6: FF              RST     0X38                
16E7: FF              RST     0X38                
16E8: FF              RST     0X38                
16E9: FF              RST     0X38                
16EA: FF              RST     0X38                
16EB: FF              RST     0X38                
16EC: FF              RST     0X38                
16ED: FF              RST     0X38                
16EE: FF              RST     0X38                
16EF: FF              RST     0X38                
16F0: FF              RST     0X38                
16F1: FF              RST     0X38                
16F2: FF              RST     0X38                
16F3: FF              RST     0X38                
16F4: FF              RST     0X38                
16F5: FF              RST     0X38                
16F6: FF              RST     0X38                
16F7: FF              RST     0X38                
16F8: FF              RST     0X38                
16F9: FF              RST     0X38                
16FA: FF              RST     0X38                
16FB: FF              RST     0X38                
16FC: FF              RST     0X38                
16FD: FF              RST     0X38                
16FE: FF              RST     0X38                
16FF: FF              RST     0X38                
1700: FF              RST     0X38                
1701: FF              RST     0X38                
1702: FF              RST     0X38                
1703: FF              RST     0X38                
1704: FF              RST     0X38                
1705: FF              RST     0X38                
1706: FF              RST     0X38                
1707: FF              RST     0X38                
1708: FF              RST     0X38                
1709: FF              RST     0X38                
170A: FF              RST     0X38                
170B: FF              RST     0X38                
170C: FF              RST     0X38                
170D: FF              RST     0X38                
170E: FF              RST     0X38                
170F: FF              RST     0X38                
1710: FF              RST     0X38                
1711: FF              RST     0X38                
1712: FF              RST     0X38                
1713: FF              RST     0X38                
1714: FF              RST     0X38                
1715: FF              RST     0X38                
1716: FF              RST     0X38                
1717: FF              RST     0X38                
1718: FF              RST     0X38                
1719: FF              RST     0X38                
171A: FF              RST     0X38                
171B: FF              RST     0X38                
171C: FF              RST     0X38                
171D: FF              RST     0X38                
171E: FF              RST     0X38                
171F: FF              RST     0X38                
1720: FF              RST     0X38                
1721: FF              RST     0X38                
1722: FF              RST     0X38                
1723: FF              RST     0X38                
1724: FF              RST     0X38                
1725: FF              RST     0X38                
1726: FF              RST     0X38                
1727: FF              RST     0X38                
1728: FF              RST     0X38                
1729: FF              RST     0X38                
172A: FF              RST     0X38                
172B: FF              RST     0X38                
172C: FF              RST     0X38                
172D: FF              RST     0X38                
172E: FF              RST     0X38                
172F: FF              RST     0X38                
1730: FF              RST     0X38                
1731: FF              RST     0X38                
1732: FF              RST     0X38                
1733: FF              RST     0X38                
1734: FF              RST     0X38                
1735: FF              RST     0X38                
1736: FF              RST     0X38                
1737: FF              RST     0X38                
1738: FF              RST     0X38                
1739: FF              RST     0X38                
173A: FF              RST     0X38                
173B: FF              RST     0X38                
173C: FF              RST     0X38                
173D: FF              RST     0X38                
173E: FF              RST     0X38                
173F: FF              RST     0X38                
1740: FF              RST     0X38                
1741: FF              RST     0X38                
1742: FF              RST     0X38                
1743: FF              RST     0X38                
1744: FF              RST     0X38                
1745: FF              RST     0X38                
1746: FF              RST     0X38                
1747: FF              RST     0X38                
1748: FF              RST     0X38                
1749: FF              RST     0X38                
174A: FF              RST     0X38                
174B: FF              RST     0X38                
174C: FF              RST     0X38                
174D: FF              RST     0X38                
174E: FF              RST     0X38                
174F: FF              RST     0X38                
1750: FF              RST     0X38                
1751: FF              RST     0X38                
1752: FF              RST     0X38                
1753: FF              RST     0X38                
1754: FF              RST     0X38                
1755: FF              RST     0X38                
1756: FF              RST     0X38                
1757: FF              RST     0X38                
1758: FF              RST     0X38                
1759: FF              RST     0X38                
175A: FF              RST     0X38                
175B: FF              RST     0X38                
175C: FF              RST     0X38                
175D: FF              RST     0X38                
175E: FF              RST     0X38                
175F: FF              RST     0X38                
1760: FF              RST     0X38                
1761: FF              RST     0X38                
1762: FF              RST     0X38                
1763: FF              RST     0X38                
1764: FF              RST     0X38                
1765: FF              RST     0X38                
1766: FF              RST     0X38                
1767: FF              RST     0X38                
1768: FF              RST     0X38                
1769: FF              RST     0X38                
176A: FF              RST     0X38                
176B: FF              RST     0X38                
176C: FF              RST     0X38                
176D: FF              RST     0X38                
176E: FF              RST     0X38                
176F: FF              RST     0X38                
1770: FF              RST     0X38                
1771: FF              RST     0X38                
1772: FF              RST     0X38                
1773: FF              RST     0X38                
1774: FF              RST     0X38                
1775: FF              RST     0X38                
1776: FF              RST     0X38                
1777: FF              RST     0X38                
1778: FF              RST     0X38                
1779: FF              RST     0X38                
177A: FF              RST     0X38                
177B: FF              RST     0X38                
177C: FF              RST     0X38                
177D: FF              RST     0X38                
177E: FF              RST     0X38                
177F: FF              RST     0X38                
1780: FF              RST     0X38                
1781: FF              RST     0X38                
1782: FF              RST     0X38                
1783: FF              RST     0X38                
1784: FF              RST     0X38                
1785: FF              RST     0X38                
1786: FF              RST     0X38                
1787: FF              RST     0X38                
1788: FF              RST     0X38                
1789: FF              RST     0X38                
178A: FF              RST     0X38                
178B: FF              RST     0X38                
178C: FF              RST     0X38                
178D: FF              RST     0X38                
178E: FF              RST     0X38                
178F: FF              RST     0X38                
1790: FF              RST     0X38                
1791: FF              RST     0X38                
1792: FF              RST     0X38                
1793: FF              RST     0X38                
1794: FF              RST     0X38                
1795: FF              RST     0X38                
1796: FF              RST     0X38                
1797: FF              RST     0X38                
1798: FF              RST     0X38                
1799: FF              RST     0X38                
179A: FF              RST     0X38                
179B: FF              RST     0X38                
179C: FF              RST     0X38                
179D: FF              RST     0X38                
179E: FF              RST     0X38                
179F: FF              RST     0X38                
17A0: FF              RST     0X38                
17A1: FF              RST     0X38                
17A2: FF              RST     0X38                
17A3: FF              RST     0X38                
17A4: FF              RST     0X38                
17A5: FF              RST     0X38                
17A6: FF              RST     0X38                
17A7: FF              RST     0X38                
17A8: FF              RST     0X38                
17A9: FF              RST     0X38                
17AA: FF              RST     0X38                
17AB: FF              RST     0X38                
17AC: FF              RST     0X38                
17AD: FF              RST     0X38                
17AE: FF              RST     0X38                
17AF: FF              RST     0X38                
17B0: FF              RST     0X38                
17B1: FF              RST     0X38                
17B2: FF              RST     0X38                
17B3: FF              RST     0X38                
17B4: FF              RST     0X38                
17B5: FF              RST     0X38                
17B6: FF              RST     0X38                
17B7: FF              RST     0X38                
17B8: FF              RST     0X38                
17B9: FF              RST     0X38                
17BA: FF              RST     0X38                
17BB: FF              RST     0X38                
17BC: FF              RST     0X38                
17BD: FF              RST     0X38                
17BE: FF              RST     0X38                
17BF: FF              RST     0X38                
17C0: FF              RST     0X38                
17C1: FF              RST     0X38                
17C2: FF              RST     0X38                
17C3: FF              RST     0X38                
17C4: FF              RST     0X38                
17C5: FF              RST     0X38                
17C6: FF              RST     0X38                
17C7: FF              RST     0X38                
17C8: FF              RST     0X38                
17C9: FF              RST     0X38                
17CA: FF              RST     0X38                
17CB: FF              RST     0X38                
17CC: FF              RST     0X38                
17CD: FF              RST     0X38                
17CE: FF              RST     0X38                
17CF: FF              RST     0X38                
17D0: FF              RST     0X38                
17D1: FF              RST     0X38                
17D2: FF              RST     0X38                
17D3: FF              RST     0X38                
17D4: FF              RST     0X38                
17D5: FF              RST     0X38                
17D6: FF              RST     0X38                
17D7: FF              RST     0X38                
17D8: FF              RST     0X38                
17D9: FF              RST     0X38                
17DA: FF              RST     0X38                
17DB: FF              RST     0X38                
17DC: FF              RST     0X38                
17DD: FF              RST     0X38                
17DE: FF              RST     0X38                
17DF: FF              RST     0X38                
17E0: FF              RST     0X38                
17E1: FF              RST     0X38                
17E2: FF              RST     0X38                
17E3: FF              RST     0X38                
17E4: FF              RST     0X38                
17E5: FF              RST     0X38                
17E6: FF              RST     0X38                
17E7: FF              RST     0X38                
17E8: FF              RST     0X38                
17E9: FF              RST     0X38                
17EA: FF              RST     0X38                
17EB: FF              RST     0X38                
17EC: FF              RST     0X38                
17ED: FF              RST     0X38                
17EE: FF              RST     0X38                
17EF: FF              RST     0X38                
17F0: FF              RST     0X38                
17F1: FF              RST     0X38                
17F2: FF              RST     0X38                
17F3: FF              RST     0X38                
17F4: FF              RST     0X38                
17F5: FF              RST     0X38                
17F6: FF              RST     0X38                
17F7: FF              RST     0X38                
17F8: FF              RST     0X38                
17F9: FF              RST     0X38                
17FA: FF              RST     0X38                
17FB: FF              RST     0X38                
17FC: FF              RST     0X38                
17FD: FF              RST     0X38                
17FE: FF              RST     0X38                
17FF: FF              RST     0X38                
```

