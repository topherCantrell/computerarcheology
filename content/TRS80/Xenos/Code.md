![Xenos](Xenos.png)

# Xenos

>>> cpu Z80

>>> binary 5D00:roms/xenos.bin

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](../HardwareDisk.md)

```code
Start:
5D00: 31 9A BF        LD      SP,$BF9A            ; Stack
5D03: 21 C0 3F        LD      HL,$3FC0            ; Set cursor to ...
5D06: 22 20 40        LD      ($4020),HL          ; {hard.Cursor Pointer} ... start of last row on screen
5D09: 3E 01           LD      A,$01               
5D0B: 32 FA 71        LD      ($71FA),A           ; {}
5D0E: 3E 01           LD      A,$01               
5D10: 32 1E 72        LD      ($721E),A           ; {}
5D13: 47              LD      B,A                 
5D14: CD 57 70        CALL    $7057               ; {code.FindSubList}
5D17: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
5D1A: 3A 21 72        LD      A,($7221)           ; {}
5D1D: 77              LD      (HL),A              
5D1E: 23              INC     HL                  
5D1F: 3A FA 71        LD      A,($71FA)           ; {}
5D22: 77              LD      (HL),A              
5D23: 21 67 72        LD      HL,$7267            
5D26: CD 57 63        CALL    $6357               ; {}
5D29: 3E 0D           LD      A,$0D               
5D2B: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces}
5D2E: CD 99 62        CALL    $6299               ; {code.GetKey}
5D31: 97              SUB     A                   
5D32: 21 66 72        LD      HL,$7266            
5D35: CD 57 63        CALL    $6357               ; {}
5D38: 31 9A BF        LD      SP,$BF9A            
5D3B: CD 52 62        CALL    $6252               ; {}
5D3E: 97              SUB     A                   
5D3F: 32 03 72        LD      ($7203),A           ; {}
5D42: 32 06 72        LD      ($7206),A           ; {}
5D45: 32 08 72        LD      ($7208),A           ; {}
5D48: 32 FE 71        LD      ($71FE),A           ; {}
5D4B: 32 FF 71        LD      ($71FF),A           ; {}
5D4E: 32 05 72        LD      ($7205),A           ; {}
5D51: 32 04 72        LD      ($7204),A           ; {}
5D54: 32 00 72        LD      ($7200),A           ; {}
5D57: 32 01 72        LD      ($7201),A           ; {}
5D5A: 32 0B 72        LD      ($720B),A           ; {}
5D5D: 32 0F 72        LD      ($720F),A           ; {}
5D60: 32 15 72        LD      ($7215),A           ; {}
5D63: 3E 01           LD      A,$01               
5D65: 32 1E 72        LD      ($721E),A           ; {}
5D68: 47              LD      B,A                 
5D69: CD 57 70        CALL    $7057               ; {code.FindSubList}
5D6C: 22 1F 72        LD      ($721F),HL          ; {}
5D6F: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
5D72: 7E              LD      A,(HL)              
5D73: A7              AND     A                   
5D74: FA 83 5D        JP      M,$5D83             ; {}
5D77: 47              LD      B,A                 
5D78: CD 57 70        CALL    $7057               ; {code.FindSubList}
5D7B: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
5D7E: 7E              LD      A,(HL)              
5D7F: A7              AND     A                   
5D80: F2 77 5D        JP      P,$5D77             ; {}
5D83: 32 21 72        LD      ($7221),A           ; {}
5D86: 47              LD      B,A                 
5D87: 21 00 52        LD      HL,$5200            ; {+ram.sectionData}
5D8A: CD A5 61        CALL    $61A5               ; {}
5D8D: 22 22 72        LD      ($7222),HL          ; {}
5D90: A7              AND     A                   
5D91: C3 9A 5D        JP      $5D9A               ; {}
5D94: 21 2B 76        LD      HL,$762B            ; {+code.KnownWords}
5D97: CD 57 63        CALL    $6357               ; {}
5D9A: 21 47 72        LD      HL,$7247            
5D9D: 22 24 72        LD      ($7224),HL          ; {}
5DA0: 36 00           LD      (HL),$00            
5DA2: 21 C0 3F        LD      HL,$3FC0            
5DA5: CD A5 62        CALL    $62A5               ; {}
5DA8: CA BB 5D        JP      Z,$5DBB             ; {}
5DAB: 7E              LD      A,(HL)              
5DAC: FE 20           CP      $20                 
5DAE: CA A5 5D        JP      Z,$5DA5             ; {}
5DB1: 7D              LD      A,L                 
5DB2: FE FF           CP      $FF                 
5DB4: CA BB 5D        JP      Z,$5DBB             ; {}
5DB7: 23              INC     HL                  
5DB8: C3 AB 5D        JP      $5DAB               ; {}
5DBB: 7D              LD      A,L                 
5DBC: FE FF           CP      $FF                 
5DBE: C2 A5 5D        JP      NZ,$5DA5            ; {}
5DC1: 2A 24 72        LD      HL,($7224)          ; {}
5DC4: 36 00           LD      (HL),$00            
5DC6: 21 47 72        LD      HL,$7247            
5DC9: 7E              LD      A,(HL)              
5DCA: A7              AND     A                   
5DCB: CA 6B 5E        JP      Z,$5E6B             ; {}
5DCE: FE 02           CP      $02                 
5DD0: C2 E1 5D        JP      NZ,$5DE1            ; {}
5DD3: 23              INC     HL                  
5DD4: 7E              LD      A,(HL)              
5DD5: 2B              DEC     HL                  
5DD6: FE 09           CP      $09                 
5DD8: D2 E1 5D        JP      NC,$5DE1            ; {}
5DDB: 32 04 72        LD      ($7204),A           ; {}
5DDE: 23              INC     HL                  
5DDF: 23              INC     HL                  
5DE0: 23              INC     HL                  
5DE1: 7E              LD      A,(HL)              
5DE2: 23              INC     HL                  
5DE3: A7              AND     A                   
5DE4: CA 6B 5E        JP      Z,$5E6B             ; {}
5DE7: 46              LD      B,(HL)              
5DE8: 23              INC     HL                  
5DE9: 4E              LD      C,(HL)              
5DEA: 23              INC     HL                  
5DEB: E5              PUSH    HL                  
5DEC: 3D              DEC     A                   
5DED: C2 14 5E        JP      NZ,$5E14            ; {}
5DF0: 21 DF 72        LD      HL,$72DF            
5DF3: CD A5 61        CALL    $61A5               ; {}
5DF6: D2 0D 5E        JP      NC,$5E0D            ; {}
5DF9: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
5DFC: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE}
5DFF: D2 0D 5E        JP      NC,$5E0D            ; {}
5E02: 3A FF 71        LD      A,($71FF)           ; {}
5E05: BE              CP      (HL)                
5E06: 23              INC     HL                  
5E07: 7E              LD      A,(HL)              
5E08: 23              INC     HL                  
5E09: C2 FC 5D        JP      NZ,$5DFC            ; {}
5E0C: 47              LD      B,A                 
5E0D: 78              LD      A,B                 
5E0E: 32 FF 71        LD      ($71FF),A           ; {}
5E11: C3 67 5E        JP      $5E67               ; {}
5E14: 3D              DEC     A                   
5E15: C2 51 5E        JP      NZ,$5E51            ; {}
5E18: 3A 01 72        LD      A,($7201)           ; {}
5E1B: A7              AND     A                   
5E1C: CA 3F 5E        JP      Z,$5E3F             ; {}
5E1F: 21 15 72        LD      HL,$7215            
5E22: 70              LD      (HL),B              
5E23: 23              INC     HL                  
5E24: 3A 03 72        LD      A,($7203)           ; {}
5E27: 77              LD      (HL),A              
5E28: 23              INC     HL                  
5E29: 3A 06 72        LD      A,($7206)           ; {}
5E2C: 77              LD      (HL),A              
5E2D: A7              AND     A                   
5E2E: C2 32 5E        JP      NZ,$5E32            ; {}
5E31: 71              LD      (HL),C              
5E32: 97              SUB     A                   
5E33: 32 03 72        LD      ($7203),A           ; {}
5E36: 32 01 72        LD      ($7201),A           ; {}
5E39: 32 06 72        LD      ($7206),A           ; {}
5E3C: C3 67 5E        JP      $5E67               ; {}
5E3F: 2A 0F 72        LD      HL,($720F)          ; {}
5E42: 22 15 72        LD      ($7215),HL          ; {}
5E45: 3A 11 72        LD      A,($7211)           ; {}
5E48: 32 17 72        LD      ($7217),A           ; {}
5E4B: 21 0F 72        LD      HL,$720F            
5E4E: C3 22 5E        JP      $5E22               ; {}
5E51: 3D              DEC     A                   
5E52: C2 60 5E        JP      NZ,$5E60            ; {}
5E55: 78              LD      A,B                 
5E56: 32 03 72        LD      ($7203),A           ; {}
5E59: 79              LD      A,C                 
5E5A: 32 06 72        LD      ($7206),A           ; {}
5E5D: C3 67 5E        JP      $5E67               ; {}
5E60: 78              LD      A,B                 
5E61: 32 00 72        LD      ($7200),A           ; {}
5E64: 32 01 72        LD      ($7201),A           ; {}
5E67: E1              POP     HL                  
5E68: C3 E1 5D        JP      $5DE1               ; {}
5E6B: 3A FF 71        LD      A,($71FF)           ; {}
5E6E: A7              AND     A                   
5E6F: CA 3D 61        JP      Z,$613D             ; {}
5E72: 21 15 72        LD      HL,$7215            
5E75: CD 99 5F        CALL    $5F99               ; {}
5E78: 32 15 72        LD      ($7215),A           ; {}
5E7B: 22 18 72        LD      ($7218),HL          ; {}
5E7E: 21 0F 72        LD      HL,$720F            
5E81: CD 99 5F        CALL    $5F99               ; {}
5E84: 32 0F 72        LD      ($720F),A           ; {}
5E87: 22 12 72        LD      ($7212),HL          ; {}
5E8A: 97              SUB     A                   
5E8B: 32 01 72        LD      ($7201),A           ; {}
5E8E: 2A 12 72        LD      HL,($7212)          ; {}
5E91: 3A 0F 72        LD      A,($720F)           ; {}
5E94: A7              AND     A                   
5E95: CA 9E 5E        JP      Z,$5E9E             ; {}
5E98: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
5E9B: 23              INC     HL                  
5E9C: 23              INC     HL                  
5E9D: 7E              LD      A,(HL)              
5E9E: 32 14 72        LD      ($7214),A           ; {}
5EA1: 2A 18 72        LD      HL,($7218)          ; {}
5EA4: 3A 15 72        LD      A,($7215)           ; {}
5EA7: A7              AND     A                   
5EA8: CA B1 5E        JP      Z,$5EB1             ; {}
5EAB: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
5EAE: 23              INC     HL                  
5EAF: 23              INC     HL                  
5EB0: 7E              LD      A,(HL)              
5EB1: 32 1A 72        LD      ($721A),A           ; {}
5EB4: 21 E1 72        LD      HL,$72E1            
5EB7: 7E              LD      A,(HL)              
5EB8: A7              AND     A                   
5EB9: CA F3 60        JP      Z,$60F3             ; {}
5EBC: 3A FF 71        LD      A,($71FF)           ; {}
5EBF: BE              CP      (HL)                
5EC0: 23              INC     HL                  
5EC1: C2 23 5F        JP      NZ,$5F23            ; {}
5EC4: 7E              LD      A,(HL)              
5EC5: 32 02 72        LD      ($7202),A           ; {}
5EC8: 3A 00 72        LD      A,($7200)           ; {}
5ECB: A7              AND     A                   
5ECC: CA D3 5E        JP      Z,$5ED3             ; {}
5ECF: BE              CP      (HL)                
5ED0: C2 23 5F        JP      NZ,$5F23            ; {}
5ED3: 23              INC     HL                  
5ED4: 7E              LD      A,(HL)              
5ED5: A7              AND     A                   
5ED6: CA EF 5E        JP      Z,$5EEF             ; {}
5ED9: 3A 0F 72        LD      A,($720F)           ; {}
5EDC: A7              AND     A                   
5EDD: C2 F6 5E        JP      NZ,$5EF6            ; {}
5EE0: 3A 08 72        LD      A,($7208)           ; {}
5EE3: 32 09 72        LD      ($7209),A           ; {}
5EE6: 11 0F 72        LD      DE,$720F            
5EE9: CD 70 60        CALL    $6070               ; {}
5EEC: C3 F6 5E        JP      $5EF6               ; {}
5EEF: 3A 0F 72        LD      A,($720F)           ; {}
5EF2: A7              AND     A                   
5EF3: C2 24 5F        JP      NZ,$5F24            ; {}
5EF6: 23              INC     HL                  
5EF7: 7E              LD      A,(HL)              
5EF8: A7              AND     A                   
5EF9: CA 17 5F        JP      Z,$5F17             ; {}
5EFC: 3A 15 72        LD      A,($7215)           ; {}
5EFF: A7              AND     A                   
5F00: C2 1E 5F        JP      NZ,$5F1E            ; {}
5F03: 3A 07 72        LD      A,($7207)           ; {}
5F06: 32 09 72        LD      ($7209),A           ; {}
5F09: 3E 01           LD      A,$01               
5F0B: 32 01 72        LD      ($7201),A           ; {}
5F0E: 11 15 72        LD      DE,$7215            
5F11: CD 70 60        CALL    $6070               ; {}
5F14: C3 1E 5F        JP      $5F1E               ; {}
5F17: 3A 15 72        LD      A,($7215)           ; {}
5F1A: A7              AND     A                   
5F1B: C2 25 5F        JP      NZ,$5F25            ; {}
5F1E: 23              INC     HL                  
5F1F: 7E              LD      A,(HL)              
5F20: C3 2A 5F        JP      $5F2A               ; {}
5F23: 23              INC     HL                  
5F24: 23              INC     HL                  
5F25: 23              INC     HL                  
5F26: 23              INC     HL                  
5F27: C3 B7 5E        JP      $5EB7               ; {}
5F2A: 32 1D 72        LD      ($721D),A           ; {}
5F2D: 21 FF 3F        LD      HL,$3FFF            
5F30: 22 20 40        LD      ($4020),HL          ; {hard.Cursor Pointer}
5F33: 3A 0F 72        LD      A,($720F)           ; {}
5F36: A7              AND     A                   
5F37: C2 46 5F        JP      NZ,$5F46            ; {}
5F3A: 2A 18 72        LD      HL,($7218)          ; {}
5F3D: 22 12 72        LD      ($7212),HL          ; {}
5F40: 3A 15 72        LD      A,($7215)           ; {}
5F43: 32 0F 72        LD      ($720F),A           ; {}
5F46: 3A 04 72        LD      A,($7204)           ; {}
5F49: A7              AND     A                   
5F4A: CA 7D 5F        JP      Z,$5F7D             ; {}
5F4D: 21 48 72        LD      HL,$7248            
5F50: 7E              LD      A,(HL)              
5F51: 36 00           LD      (HL),$00            
5F53: 2B              DEC     HL                  
5F54: 77              LD      (HL),A              
5F55: CD 99 5F        CALL    $5F99               ; {}
5F58: 32 1E 72        LD      ($721E),A           ; {}
5F5B: 22 1F 72        LD      ($721F),HL          ; {}
5F5E: 3E 0D           LD      A,$0D               
5F60: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces}
5F63: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
5F66: 23              INC     HL                  
5F67: 23              INC     HL                  
5F68: 23              INC     HL                  
5F69: 06 0B           LD      B,$0B               
5F6B: CD AD 61        CALL    $61AD               ; {}
5F6E: DA 74 5F        JP      C,$5F74             ; {}
5F71: C3 8B 5F        JP      $5F8B               ; {}
5F74: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
5F77: CD 57 63        CALL    $6357               ; {}
5F7A: C3 8B 5F        JP      $5F8B               ; {}
5F7D: 3E 0D           LD      A,$0D               
5F7F: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces}
5F82: 21 4E 7D        LD      HL,$7D4E            
5F85: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
5F88: CD 57 63        CALL    $6357               ; {}
5F8B: CD B2 6C        CALL    $6CB2               ; {}
5F8E: 3E 0D           LD      A,$0D               
5F90: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces}
5F93: 3A 1D 72        LD      A,($721D)           ; {}
5F96: C3 38 5D        JP      $5D38               ; {}
5F99: 97              SUB     A                   
5F9A: 32 0B 72        LD      ($720B),A           ; {}
5F9D: 7E              LD      A,(HL)              
5F9E: 32 FE 71        LD      ($71FE),A           ; {}
5FA1: 47              LD      B,A                 
5FA2: A7              AND     A                   
5FA3: C8              RET     Z                   
5FA4: 23              INC     HL                  
5FA5: 7E              LD      A,(HL)              
5FA6: 32 03 72        LD      ($7203),A           ; {}
5FA9: 23              INC     HL                  
5FAA: 7E              LD      A,(HL)              
5FAB: 32 1B 72        LD      ($721B),A           ; {}
5FAE: 21 7A 88        LD      HL,$887A            
5FB1: CD A5 61        CALL    $61A5               ; {}
5FB4: D2 14 60        JP      NC,$6014            ; {}
5FB7: D5              PUSH    DE                  
5FB8: E5              PUSH    HL                  
5FB9: 3A F1 71        LD      A,($71F1)           ; {}
5FBC: 32 F2 71        LD      ($71F2),A           ; {}
5FBF: CD 23 60        CALL    $6023               ; {}
5FC2: C2 1F 60        JP      NZ,$601F            ; {}
5FC5: 3A 03 72        LD      A,($7203)           ; {}
5FC8: A7              AND     A                   
5FC9: CA EE 5F        JP      Z,$5FEE             ; {}
5FCC: E1              POP     HL                  
5FCD: E5              PUSH    HL                  
5FCE: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
5FD1: 01 03 00        LD      BC,$0003            
5FD4: 09              ADD     HL,BC               
5FD5: 06 01           LD      B,$01               
5FD7: CD AD 61        CALL    $61AD               ; {}
5FDA: D2 EE 5F        JP      NC,$5FEE            ; {}
5FDD: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
5FE0: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE}
5FE3: D2 1F 60        JP      NC,$601F            ; {}
5FE6: 3A 03 72        LD      A,($7203)           ; {}
5FE9: BE              CP      (HL)                
5FEA: 23              INC     HL                  
5FEB: C2 E0 5F        JP      NZ,$5FE0            ; {}
5FEE: E1              POP     HL                  
5FEF: 3A 0B 72        LD      A,($720B)           ; {}
5FF2: A7              AND     A                   
5FF3: C2 34 61        JP      NZ,$6134            ; {}
5FF6: 3A F2 71        LD      A,($71F2)           ; {}
5FF9: 32 0B 72        LD      ($720B),A           ; {}
5FFC: 22 0C 72        LD      ($720C),HL          ; {}
5FFF: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6002: EB              EX      DE,HL               
6003: D1              POP     DE                  
6004: 3A FE 71        LD      A,($71FE)           ; {}
6007: 47              LD      B,A                 
6008: 3A F2 71        LD      A,($71F2)           ; {}
600B: 32 F1 71        LD      ($71F1),A           ; {}
600E: CD AD 61        CALL    $61AD               ; {}
6011: DA B7 5F        JP      C,$5FB7             ; {}
6014: 3A 0B 72        LD      A,($720B)           ; {}
6017: 2A 0C 72        LD      HL,($720C)          ; {}
601A: A7              AND     A                   
601B: C0              RET     NZ                  
601C: C3 EA 60        JP      $60EA               ; {}
601F: E1              POP     HL                  
6020: C3 FF 5F        JP      $5FFF               ; {}
6023: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6026: 3A 21 72        LD      A,($7221)           ; {}
6029: BE              CP      (HL)                
602A: C2 41 60        JP      NZ,$6041            ; {}
602D: 7E              LD      A,(HL)              
602E: E6 80           AND     $80                 
6030: CA 41 60        JP      Z,$6041             ; {}
6033: 23              INC     HL                  
6034: 3A FA 71        LD      A,($71FA)           ; {}
6037: 47              LD      B,A                 
6038: 7E              LD      A,(HL)              
6039: E6 0F           AND     $0F                 
603B: B8              CP      B                   
603C: 2B              DEC     HL                  
603D: C8              RET     Z                   
603E: C3 6D 60        JP      $606D               ; {}
6041: 7E              LD      A,(HL)              
6042: A7              AND     A                   
6043: CA 6D 60        JP      Z,$606D             ; {}
6046: 3C              INC     A                   
6047: C8              RET     Z                   
6048: 7E              LD      A,(HL)              
6049: E6 80           AND     $80                 
604B: C2 6D 60        JP      NZ,$606D            ; {}
604E: 46              LD      B,(HL)              
604F: 3A 1E 72        LD      A,($721E)           ; {}
6052: B8              CP      B                   
6053: C8              RET     Z                   
6054: CD 57 70        CALL    $7057               ; {code.FindSubList}
6057: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
605A: 23              INC     HL                  
605B: 7E              LD      A,(HL)              
605C: 2B              DEC     HL                  
605D: E6 80           AND     $80                 
605F: C2 26 60        JP      NZ,$6026            ; {}
6062: 23              INC     HL                  
6063: 7E              LD      A,(HL)              
6064: 2B              DEC     HL                  
6065: E6 20           AND     $20                 
6067: C2 6D 60        JP      NZ,$606D            ; {}
606A: C3 26 60        JP      $6026               ; {}
606D: F6 01           OR      $01                 
606F: C9              RET                         
6070: E5              PUSH    HL                  
6071: 97              SUB     A                   
6072: 32 FE 71        LD      ($71FE),A           ; {}
6075: 32 F1 71        LD      ($71F1),A           ; {}
6078: D5              PUSH    DE                  
6079: 4E              LD      C,(HL)              
607A: 21 7A 88        LD      HL,$887A            
607D: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6080: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE}
6083: D2 CB 60        JP      NC,$60CB            ; {}
6086: 3A F1 71        LD      A,($71F1)           ; {}
6089: 3C              INC     A                   
608A: 32 F1 71        LD      ($71F1),A           ; {}
608D: D5              PUSH    DE                  
608E: E5              PUSH    HL                  
608F: CD 23 60        CALL    $6023               ; {}
6092: E1              POP     HL                  
6093: C2 C5 60        JP      NZ,$60C5            ; {}
6096: 46              LD      B,(HL)              
6097: 22 24 72        LD      ($7224),HL          ; {}
609A: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
609D: 23              INC     HL                  
609E: 23              INC     HL                  
609F: 7E              LD      A,(HL)              
60A0: A1              AND     C                   
60A1: B9              CP      C                   
60A2: C2 C0 60        JP      NZ,$60C0            ; {}
60A5: 3A FE 71        LD      A,($71FE)           ; {}
60A8: A7              AND     A                   
60A9: C2 FC 60        JP      NZ,$60FC            ; {}
60AC: 78              LD      A,B                 
60AD: 32 FE 71        LD      ($71FE),A           ; {}
60B0: 3A F1 71        LD      A,($71F1)           ; {}
60B3: 32 F2 71        LD      ($71F2),A           ; {}
60B6: 7E              LD      A,(HL)              
60B7: 32 03 72        LD      ($7203),A           ; {}
60BA: 2A 24 72        LD      HL,($7224)          ; {}
60BD: 22 26 72        LD      ($7226),HL          ; {}
60C0: EB              EX      DE,HL               
60C1: D1              POP     DE                  
60C2: C3 80 60        JP      $6080               ; {}
60C5: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
60C8: C3 C0 60        JP      $60C0               ; {}
60CB: 3A FE 71        LD      A,($71FE)           ; {}
60CE: A7              AND     A                   
60CF: CA FC 60        JP      Z,$60FC             ; {}
60D2: D1              POP     DE                  
60D3: 2A 26 72        LD      HL,($7226)          ; {}
60D6: 3A F2 71        LD      A,($71F2)           ; {}
60D9: 12              LD      (DE),A              
60DA: 13              INC     DE                  
60DB: 13              INC     DE                  
60DC: 13              INC     DE                  
60DD: 7D              LD      A,L                 
60DE: 12              LD      (DE),A              
60DF: 13              INC     DE                  
60E0: 7C              LD      A,H                 
60E1: 12              LD      (DE),A              
60E2: 13              INC     DE                  
60E3: 3A 03 72        LD      A,($7203)           ; {}
60E6: 12              LD      (DE),A              
60E7: E1              POP     HL                  
60E8: 97              SUB     A                   
60E9: C9              RET                         
60EA: 11 2F 72        LD      DE,$722F            
60ED: 3A 1B 72        LD      A,($721B)           ; {}
60F0: C3 42 61        JP      $6142               ; {}
60F3: 11 3E 72        LD      DE,$723E            
60F6: 3A 07 72        LD      A,($7207)           ; {}
60F9: C3 42 61        JP      $6142               ; {}
60FC: 3A 01 72        LD      A,($7201)           ; {}
60FF: A7              AND     A                   
6100: CA 2B 61        JP      Z,$612B             ; {}
6103: 3A 00 72        LD      A,($7200)           ; {}
6106: A7              AND     A                   
6107: C2 2B 61        JP      NZ,$612B            ; {}
610A: 16 00           LD      D,$00               
610C: 21 DB 7C        LD      HL,$7CDB            
610F: 7E              LD      A,(HL)              
6110: A7              AND     A                   
6111: CA 2B 61        JP      Z,$612B             ; {}
6114: E5              PUSH    HL                  
6115: 5E              LD      E,(HL)              
6116: 23              INC     HL                  
6117: 19              ADD     HL,DE               
6118: 3A 02 72        LD      A,($7202)           ; {}
611B: BE              CP      (HL)                
611C: CA 24 61        JP      Z,$6124             ; {}
611F: 23              INC     HL                  
6120: C1              POP     BC                  
6121: C3 0F 61        JP      $610F               ; {}
6124: D1              POP     DE                  
6125: 3A 09 72        LD      A,($7209)           ; {}
6128: CD 7E 61        CALL    $617E               ; {}
612B: 11 2F 72        LD      DE,$722F            
612E: 3A 09 72        LD      A,($7209)           ; {}
6131: C3 42 61        JP      $6142               ; {}
6134: 11 36 72        LD      DE,$7236            
6137: 3A 1B 72        LD      A,($721B)           ; {}
613A: C3 42 61        JP      $6142               ; {}
613D: 11 28 72        LD      DE,$7228            
6140: 3E C0           LD      A,$C0               
6142: 31 9A BF        LD      SP,$BF9A            
6145: 21 C0 3F        LD      HL,$3FC0            
6148: CD 7E 61        CALL    $617E               ; {}
614B: 1A              LD      A,(DE)              
614C: 4F              LD      C,A                 
614D: E5              PUSH    HL                  
614E: 36 20           LD      (HL),$20            
6150: 23              INC     HL                  
6151: 0D              DEC     C                   
6152: C2 4E 61        JP      NZ,$614E            ; {}
6155: CD 73 61        CALL    $6173               ; {}
6158: E1              POP     HL                  
6159: 05              DEC     B                   
615A: C2 6D 61        JP      NZ,$616D            ; {}
615D: 1A              LD      A,(DE)              
615E: 3C              INC     A                   
615F: 4F              LD      C,A                 
6160: CD 61 62        CALL    $6261               ; {}
6163: 0D              DEC     C                   
6164: C2 60 61        JP      NZ,$6160            ; {}
6167: CD E5 61        CALL    $61E5               ; {}
616A: C3 3E 5D        JP      $5D3E               ; {}
616D: CD 8D 61        CALL    $618D               ; {}
6170: C3 4B 61        JP      $614B               ; {}
6173: 3E 32           LD      A,$32               
6175: 0D              DEC     C                   
6176: C2 75 61        JP      NZ,$6175            ; {}
6179: 3D              DEC     A                   
617A: C2 75 61        JP      NZ,$6175            ; {}
617D: C9              RET                         
617E: 6F              LD      L,A                 
617F: 1A              LD      A,(DE)              
6180: 3C              INC     A                   
6181: 4F              LD      C,A                 
6182: D5              PUSH    DE                  
6183: CD 78 62        CALL    $6278               ; {}
6186: 0D              DEC     C                   
6187: C2 83 61        JP      NZ,$6183            ; {}
618A: D1              POP     DE                  
618B: 06 08           LD      B,$08               
618D: 1A              LD      A,(DE)              
618E: 4F              LD      C,A                 
618F: D5              PUSH    DE                  
6190: E5              PUSH    HL                  
6191: 13              INC     DE                  
6192: 1A              LD      A,(DE)              
6193: 77              LD      (HL),A              
6194: 23              INC     HL                  
6195: 13              INC     DE                  
6196: 0D              DEC     C                   
6197: C2 92 61        JP      NZ,$6192            ; {}
619A: 2C              INC     L                   
619B: 7D              LD      A,L                 
619C: 32 09 72        LD      ($7209),A           ; {}
619F: CD 73 61        CALL    $6173               ; {}
61A2: E1              POP     HL                  
61A3: D1              POP     DE                  
61A4: C9              RET                         

61A5: 23              INC     HL                  
61A6: CD C9 61        CALL    $61C9               ; {}
61A9: 97              SUB     A                   
61AA: 32 F1 71        LD      ($71F1),A           ; {}
61AD: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE}
61B0: D0              RET     NC                  
61B1: 3A F1 71        LD      A,($71F1)           ; {}
61B4: 3C              INC     A                   
61B5: 32 F1 71        LD      ($71F1),A           ; {}
61B8: 78              LD      A,B                 
61B9: BE              CP      (HL)                
61BA: CA C6 61        JP      Z,$61C6             ; {}
61BD: D5              PUSH    DE                  
61BE: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
61C1: EB              EX      DE,HL               
61C2: D1              POP     DE                  
61C3: C3 AD 61        JP      $61AD               ; {}
61C6: 37              SCF                         
61C7: C9              RET                         

GetListInfo:
; Returns pointer to first entry in HL
; Returns one past last byte in DE
61C8: 23              INC     HL                  ; Skip list ID
61C9: 16 00           LD      D,$00               ; MSB of 0 for 1 byte length
61CB: 7E              LD      A,(HL)              ; First byte of length
61CC: E6 80           AND     $80                 ; Two byte length?
61CE: CA D6 61        JP      Z,$61D6             ; {} No, we have the one byte length
61D1: 7E              LD      A,(HL)              ; MSB again
61D2: E6 7F           AND     $7F                 ; Drop flag bit
61D4: 57              LD      D,A                 ; MSB to D (for DE)
61D5: 23              INC     HL                  ; Point to LSB
;
61D6: 5E              LD      E,(HL)              ; Get the LSB to E (length now in DE)
61D7: 23              INC     HL                  ; Point to first entry
61D8: EB              EX      DE,HL               ; DE ...
61D9: 19              ADD     HL,DE               ; ... points to ...
61DA: EB              EX      DE,HL               ; ... one past end
61DB: C9              RET                         

CompareHLandDE:
; Return Z set if HL and DE are the same
61DC: 7C              LD      A,H                 ; Compare ...
61DD: BA              CP      D                   ; ... MSBs
61DE: C0              RET     NZ                  ; Not the same, DE != HL
61DF: 7D              LD      A,L                 ; Compare ...
61E0: BB              CP      E                   ; ... LSBs
61E1: C9              RET                         

GetUserInput:
61E2: 21 C0 3F        LD      HL,$3FC0            ; Start of bottom row of screen
61E5: CD 93 62        CALL    $6293               ; {}
61E8: CD 99 62        CALL    $6299               ; {code.GetKey}
61EB: FE 18           CP      $18                 
61ED: CA 19 62        JP      Z,$6219             ; {}
61F0: FE 19           CP      $19                 
61F2: CA 29 62        JP      Z,$6229             ; {}
61F5: FE 09           CP      $09                 
61F7: CA 39 62        JP      Z,$6239             ; {}
61FA: FE 0D           CP      $0D                 ; Is the key a CR?
61FC: CA 4E 62        JP      Z,$624E             ; {} Yes ... handle it and done
61FF: FE 1F           CP      $1F                 
6201: CA 52 62        JP      Z,$6252             ; {}
6204: FE 08           CP      $08                 ; Is the key a backspace?
6206: CA 41 62        JP      Z,$6241             ; {} Yes ... handle and get another
6209: 47              LD      B,A                 
620A: 7D              LD      A,L                 
620B: FE FF           CP      $FF                 
620D: CA E8 61        JP      Z,$61E8             ; {}
6210: 78              LD      A,B                 
6211: CD 78 62        CALL    $6278               ; {}
6214: 77              LD      (HL),A              
6215: 23              INC     HL                  
6216: C3 E8 61        JP      $61E8               ; {}
6219: 7D              LD      A,L                 
621A: FE C0           CP      $C0                 
621C: CA E8 61        JP      Z,$61E8             ; {}
621F: 2B              DEC     HL                  
6220: 7E              LD      A,(HL)              
6221: 23              INC     HL                  
6222: 77              LD      (HL),A              
6223: 2B              DEC     HL                  
6224: 36 8F           LD      (HL),$8F            
6226: C3 E8 61        JP      $61E8               ; {}
6229: 7D              LD      A,L                 
622A: FE FF           CP      $FF                 
622C: CA E8 61        JP      Z,$61E8             ; {}
622F: 23              INC     HL                  
6230: 7E              LD      A,(HL)              
6231: 2B              DEC     HL                  
6232: 77              LD      (HL),A              
6233: 23              INC     HL                  
6234: 36 8F           LD      (HL),$8F            
6236: C3 E8 61        JP      $61E8               ; {}
6239: CD 61 62        CALL    $6261               ; {}
623C: 36 8F           LD      (HL),$8F            
623E: C3 E8 61        JP      $61E8               ; {}
6241: 7D              LD      A,L                 
6242: FE C0           CP      $C0                 
6244: CA E8 61        JP      Z,$61E8             ; {}
6247: 2B              DEC     HL                  
6248: CD 61 62        CALL    $6261               ; {}
624B: C3 E8 61        JP      $61E8               ; {}
624E: CD 61 62        CALL    $6261               ; {}
6251: C9              RET                         

6252: 21 C0 3F        LD      HL,$3FC0            
6255: 06 40           LD      B,$40               
6257: 36 20           LD      (HL),$20            
6259: 23              INC     HL                  
625A: 05              DEC     B                   
625B: C2 57 62        JP      NZ,$6257            ; {}
625E: C3 E2 61        JP      $61E2               ; {code.GetUserInput}
6261: 54              LD      D,H                 
6262: 5D              LD      E,L                 
6263: 45              LD      B,L                 
6264: 36 20           LD      (HL),$20            
6266: 13              INC     DE                  
6267: 7B              LD      A,E                 
6268: A7              AND     A                   
6269: C8              RET     Z                   
626A: FE 01           CP      $01                 
626C: C8              RET     Z                   
626D: 1A              LD      A,(DE)              
626E: 77              LD      (HL),A              
626F: 2C              INC     L                   
6270: 1C              INC     E                   
6271: C2 6D 62        JP      NZ,$626D            ; {}
6274: 36 20           LD      (HL),$20            
6276: 68              LD      L,B                 
6277: C9              RET                         
6278: F5              PUSH    AF                  
6279: 7D              LD      A,L                 
627A: FE FF           CP      $FF                 
627C: CA 91 62        JP      Z,$6291             ; {}
627F: 45              LD      B,L                 
6280: 21 FF 3F        LD      HL,$3FFF            
6283: 11 FE 3F        LD      DE,$3FFE            
6286: 1A              LD      A,(DE)              
6287: 77              LD      (HL),A              
6288: 2B              DEC     HL                  
6289: 1B              DEC     DE                  
628A: 7D              LD      A,L                 
628B: B8              CP      B                   
628C: C2 86 62        JP      NZ,$6286            ; {}
628F: 36 20           LD      (HL),$20            
6291: F1              POP     AF                  
6292: C9              RET                         
6293: CD 78 62        CALL    $6278               ; {}
6296: 36 8F           LD      (HL),$8F            
6298: C9              RET                         

GetKey:
6299: CD C6 71        CALL    $71C6               ; {code.COM_2B_random} Get random number (entropy while we wait)
629C: CD 2B 00        CALL    $002B               ; {hard.GetKey} Get keyboard input
629F: A7              AND     A                   ; Did the user press a key?
62A0: CA 99 62        JP      Z,$6299             ; {code.GetKey} No ... keep waiting
62A3: C9              RET                         

62A4: 23              INC     HL                  
62A5: 7D              LD      A,L                 
62A6: 32 1B 72        LD      ($721B),A           ; {}
62A9: FE FF           CP      $FF                 
62AB: C8              RET     Z                   
62AC: 7E              LD      A,(HL)              
62AD: FE 20           CP      $20                 
62AF: CA A4 62        JP      Z,$62A4             ; {}
62B2: FE 41           CP      $41                 
62B4: DA A4 62        JP      C,$62A4             ; {}
62B7: 11 2C 76        LD      DE,$762C            
62BA: CD F1 62        CALL    $62F1               ; {}
62BD: CA A5 62        JP      Z,$62A5             ; {}
62C0: 06 01           LD      B,$01               
62C2: 13              INC     DE                  
62C3: CD F1 62        CALL    $62F1               ; {}
62C6: CA D2 62        JP      Z,$62D2             ; {}
62C9: 04              INC     B                   
62CA: 78              LD      A,B                 
62CB: FE 05           CP      $05                 
62CD: C2 C2 62        JP      NZ,$62C2            ; {}
62D0: A7              AND     A                   
62D1: C9              RET                         
62D2: EB              EX      DE,HL               
62D3: 2A 24 72        LD      HL,($7224)          ; {}
62D6: 70              LD      (HL),B              
62D7: 23              INC     HL                  
62D8: 77              LD      (HL),A              
62D9: 23              INC     HL                  
62DA: 3A 1B 72        LD      A,($721B)           ; {}
62DD: 77              LD      (HL),A              
62DE: 23              INC     HL                  
62DF: 22 24 72        LD      ($7224),HL          ; {}
62E2: EB              EX      DE,HL               
62E3: 78              LD      A,B                 
62E4: FE 01           CP      $01                 
62E6: C2 EF 62        JP      NZ,$62EF            ; {}
62E9: 3A 07 72        LD      A,($7207)           ; {}
62EC: 32 08 72        LD      ($7208),A           ; {}
62EF: 97              SUB     A                   
62F0: C9              RET                         
62F1: 1A              LD      A,(DE)              
62F2: A7              AND     A                   
62F3: C2 F9 62        JP      NZ,$62F9            ; {}
62F6: F6 01           OR      $01                 
62F8: C9              RET                         
62F9: 4F              LD      C,A                 
62FA: 32 1C 72        LD      ($721C),A           ; {}
62FD: E5              PUSH    HL                  
62FE: 13              INC     DE                  
62FF: 7E              LD      A,(HL)              
6300: FE 20           CP      $20                 
6302: CA 4D 63        JP      Z,$634D             ; {}
6305: 7D              LD      A,L                 
6306: A7              AND     A                   
6307: CA 4D 63        JP      Z,$634D             ; {}
630A: 7E              LD      A,(HL)              
630B: FE 41           CP      $41                 
630D: D2 14 63        JP      NC,$6314            ; {}
6310: 23              INC     HL                  
6311: C3 FF 62        JP      $62FF               ; {}
6314: 1A              LD      A,(DE)              
6315: BE              CP      (HL)                
6316: C2 4D 63        JP      NZ,$634D            ; {}
6319: 13              INC     DE                  
631A: 23              INC     HL                  
631B: 0D              DEC     C                   
631C: C2 FF 62        JP      NZ,$62FF            ; {}
631F: 3A 1C 72        LD      A,($721C)           ; {}
6322: FE 06           CP      $06                 
6324: CA 32 63        JP      Z,$6332             ; {}
6327: 7E              LD      A,(HL)              
6328: FE 41           CP      $41                 
632A: DA 32 63        JP      C,$6332             ; {}
632D: FE 20           CP      $20                 
632F: C2 52 63        JP      NZ,$6352            ; {}
6332: 1A              LD      A,(DE)              
6333: D1              POP     DE                  
6334: 4F              LD      C,A                 
6335: 7E              LD      A,(HL)              
6336: FE 20           CP      $20                 
6338: CA 45 63        JP      Z,$6345             ; {}
633B: 7D              LD      A,L                 
633C: FE FF           CP      $FF                 
633E: CA 47 63        JP      Z,$6347             ; {}
6341: 23              INC     HL                  
6342: C3 35 63        JP      $6335               ; {}
6345: 7D              LD      A,L                 
6346: 3C              INC     A                   
6347: 32 07 72        LD      ($7207),A           ; {}
634A: 97              SUB     A                   
634B: 79              LD      A,C                 
634C: C9              RET                         
634D: 13              INC     DE                  
634E: 0D              DEC     C                   
634F: C2 4D 63        JP      NZ,$634D            ; {}
6352: E1              POP     HL                  
6353: 13              INC     DE                  
6354: C3 F1 62        JP      $62F1               ; {}

6357: 7E              LD      A,(HL)              
6358: 47              LD      B,A                 
6359: 23              INC     HL                  
635A: E6 80           AND     $80                 
635C: CA 73 63        JP      Z,$6373             ; {}
635F: E5              PUSH    HL                  
6360: D5              PUSH    DE                  
6361: 21 AF B3        LD      HL,$B3AF            
6364: CD A5 61        CALL    $61A5               ; {}
6367: D2 70 63        JP      NC,$6370            ; {}
636A: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
636D: CD 57 63        CALL    $6357               ; {}
6370: D1              POP     DE                  
6371: E1              POP     HL                  
6372: C9              RET                         

6373: 78              LD      A,B                 
6374: 11 68 72        LD      DE,$7268            
6377: 07              RLCA                        
6378: 83              ADD     A,E                 
6379: 5F              LD      E,A                 
637A: 7A              LD      A,D                 
637B: CE 00           ADC     $00                 
637D: 57              LD      D,A                 
637E: 1A              LD      A,(DE)              
637F: 32 88 63        LD      ($6388),A           ; {}
6382: 13              INC     DE                  
6383: 1A              LD      A,(DE)              
6384: 32 89 63        LD      ($6389),A           ; {}
6387: C3 87 63        JP      $6387               ; {}

Com_0D_while_pass:
; while_pass:
638A: CD C9 61        CALL    $61C9               ; {}
638D: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE}
6390: D2 9D 63        JP      NC,$639D            ; {}
6393: D5              PUSH    DE                  
6394: CD 57 63        CALL    $6357               ; {}
6397: D1              POP     DE                  
6398: CA 8D 63        JP      Z,$638D             ; {}
639B: EB              EX      DE,HL               
639C: C9              RET                         
639D: EB              EX      DE,HL               
639E: 97              SUB     A                   
639F: C9              RET                         

Com_0E_while_fail:
; while_fail:
63A0: CD C9 61        CALL    $61C9               ; {}
63A3: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE}
63A6: D2 B3 63        JP      NC,$63B3            ; {}
63A9: D5              PUSH    DE                  
63AA: CD 57 63        CALL    $6357               ; {}
63AD: D1              POP     DE                  
63AE: C2 A3 63        JP      NZ,$63A3            ; {}
63B1: EB              EX      DE,HL               
63B2: C9              RET                         
63B3: EB              EX      DE,HL               
63B4: F6 01           OR      $01                 
63B6: C9              RET                         

Com_0B_switch:
; switch:
63B7: CD C9 61        CALL    $61C9               ; {}
63BA: 46              LD      B,(HL)              
63BB: 23              INC     HL                  
63BC: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE}
63BF: D2 B3 63        JP      NC,$63B3            ; {}
63C2: D5              PUSH    DE                  
63C3: C5              PUSH    BC                  
63C4: 78              LD      A,B                 
63C5: CD 74 63        CALL    $6374               ; {}
63C8: C1              POP     BC                  
63C9: CA D4 63        JP      Z,$63D4             ; {}
63CC: CD C9 61        CALL    $61C9               ; {}
63CF: EB              EX      DE,HL               
63D0: D1              POP     DE                  
63D1: C3 BC 63        JP      $63BC               ; {}
63D4: CD C9 61        CALL    $61C9               ; {}
63D7: CD 57 63        CALL    $6357               ; {}
63DA: E1              POP     HL                  
63DB: C9              RET                         

COM_00_move_ACTIVE_and_look:
63DC: CD F5 63        CALL    $63F5               ; {code.COM_19_move_ACTIVE} Move the active object
63DF: E5              PUSH    HL                  
63E0: 2A 22 72        LD      HL,($7222)          ; {}
63E3: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
63E6: 7E              LD      A,(HL)              ; ?? byte from the script to indicate if
63E7: 32 F0 71        LD      ($71F0),A           ; {code.stopAtPeriod} ... stop after short ??
63EA: 36 01           LD      (HL),$01            
63EC: CD C1 64        CALL    $64C1               ; {}
63EF: E1              POP     HL                  
63F0: 97              SUB     A                   ; Clear stop printing after ...
63F1: 32 F0 71        LD      ($71F0),A           ; {code.stopAtPeriod} ... period flag
63F4: C9              RET                         

COM_19_move_ACTIVE:
; move_ACTIVE(room)
63F5: 7E              LD      A,(HL)              
63F6: 23              INC     HL                  
63F7: E5              PUSH    HL                  
63F8: 32 21 72        LD      ($7221),A           ; {}
63FB: 47              LD      B,A                 
63FC: 21 00 52        LD      HL,$5200            ; {+ram.sectionData} Room descriptions
63FF: CD A5 61        CALL    $61A5               ; {}
6402: 22 22 72        LD      ($7222),HL          ; {}
6405: 2A 1F 72        LD      HL,($721F)          ; {}
6408: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
640B: 3A 21 72        LD      A,($7221)           ; {}
640E: 77              LD      (HL),A              
640F: E1              POP     HL                  
6410: 97              SUB     A                   
6411: C9              RET                         

6412: 06 01           LD      B,$01               
6414: E5              PUSH    HL                  
6415: CD 57 70        CALL    $7057               ; {code.FindSubList}
6418: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
641B: 7E              LD      A,(HL)              
641C: E1              POP     HL                  
641D: A7              AND     A                   
641E: F8              RET     M                   
641F: 47              LD      B,A                 
6420: E5              PUSH    HL                  
6421: 32 0B 72        LD      ($720B),A           ; {}
6424: CD 57 70        CALL    $7057               ; {code.FindSubList}
6427: 22 0C 72        LD      ($720C),HL          ; {}
642A: E1              POP     HL                  
642B: 97              SUB     A                   
;
642C: E5              PUSH    HL                  
642D: 2A 12 72        LD      HL,($7212)          ; {}
6430: 22 0C 72        LD      ($720C),HL          ; {}
6433: 3A 0F 72        LD      A,($720F)           ; {}
6436: 32 0B 72        LD      ($720B),A           ; {}
6439: E1              POP     HL                  
643A: 97              SUB     A                   
643B: C9              RET                         

Com_1B_set_VAR_to_second_noun:
; set_VAR_to_second_noun()
643C: E5              PUSH    HL                  
643D: 2A 18 72        LD      HL,($7218)          ; {}
6440: 22 0C 72        LD      ($720C),HL          ; {}
6443: 3A 15 72        LD      A,($7215)           ; {}
6446: 32 0B 72        LD      ($720B),A           ; {}
6449: E1              POP     HL                  
644A: 97              SUB     A                   
644B: C9              RET                         

Com_XX_setVAR:
644C: 46              LD      B,(HL)              
644D: 23              INC     HL                  
644E: E5              PUSH    HL                  
644F: 78              LD      A,B                 
6450: 32 0B 72        LD      ($720B),A           ; {}
6453: A7              AND     A                   
6454: CA 5D 64        JP      Z,$645D             ; {}
6457: CD 57 70        CALL    $7057               ; {code.FindSubList}
645A: 22 0C 72        LD      ($720C),HL          ; {}
645D: E1              POP     HL                  
645E: 97              SUB     A                   
645F: C9              RET                         

Com_21_execute_phrase:
; execute_phrase(phrase,first_noun,second_noun)
6460: EB              EX      DE,HL               
6461: 2A 12 72        LD      HL,($7212)          ; {}
6464: E5              PUSH    HL                  
6465: 2A 18 72        LD      HL,($7218)          ; {}
6468: E5              PUSH    HL                  
6469: 3A 0F 72        LD      A,($720F)           ; {}
646C: 47              LD      B,A                 
646D: 3A 15 72        LD      A,($7215)           ; {}
6470: 4F              LD      C,A                 
6471: C5              PUSH    BC                  
6472: 3A 1D 72        LD      A,($721D)           ; {}
6475: 47              LD      B,A                 
6476: C5              PUSH    BC                  
6477: EB              EX      DE,HL               
6478: 7E              LD      A,(HL)              
6479: 32 1D 72        LD      ($721D),A           ; {}
647C: 23              INC     HL                  
647D: 46              LD      B,(HL)              
647E: 23              INC     HL                  
647F: 4E              LD      C,(HL)              
6480: 23              INC     HL                  
6481: E5              PUSH    HL                  
6482: 78              LD      A,B                 
6483: 32 0F 72        LD      ($720F),A           ; {}
6486: A7              AND     A                   
6487: CA 90 64        JP      Z,$6490             ; {}
648A: CD 57 70        CALL    $7057               ; {code.FindSubList}
648D: 22 12 72        LD      ($7212),HL          ; {}
6490: 79              LD      A,C                 
6491: 32 15 72        LD      ($7215),A           ; {}
6494: A7              AND     A                   
6495: CA 9F 64        JP      Z,$649F             ; {}
6498: 47              LD      B,A                 
6499: CD 57 70        CALL    $7057               ; {code.FindSubList}
649C: 22 18 72        LD      ($7218),HL          ; {}
649F: 21 4E 7D        LD      HL,$7D4E            
64A2: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
64A5: CD 57 63        CALL    $6357               ; {}
64A8: D1              POP     DE                  
64A9: C1              POP     BC                  
64AA: 78              LD      A,B                 
64AB: 32 1D 72        LD      ($721D),A           ; {}
64AE: C1              POP     BC                  
64AF: 78              LD      A,B                 
64B0: 32 0F 72        LD      ($720F),A           ; {}
64B3: 79              LD      A,C                 
64B4: 32 15 72        LD      ($7215),A           ; {}
64B7: E1              POP     HL                  
64B8: 22 18 72        LD      ($7218),HL          ; {}
64BB: E1              POP     HL                  
64BC: 22 12 72        LD      ($7212),HL          ; {}
64BF: EB              EX      DE,HL               
64C0: C9              RET                         

64C1: 3A 1E 72        LD      A,($721E)           ; {}
64C4: FE 38           CP      $38                 
64C6: CA CC 64        JP      Z,$64CC             ; {}
64C9: FE 01           CP      $01                 
64CB: C0              RET     NZ                  
64CC: 06 01           LD      B,$01               
64CE: CD 57 70        CALL    $7057               ; {code.FindSubList}
64D1: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
64D4: 7E              LD      A,(HL)              
64D5: E6 80           AND     $80                 
64D7: C2 F6 64        JP      NZ,$64F6            ; {}
64DA: 46              LD      B,(HL)              
64DB: CD 57 70        CALL    $7057               ; {code.FindSubList}
64DE: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
64E1: 23              INC     HL                  
64E2: 23              INC     HL                  
64E3: 23              INC     HL                  
64E4: 06 02           LD      B,$02               
64E6: CD AD 61        CALL    $61AD               ; {}
64E9: D2 F6 64        JP      NC,$64F6            ; {}
64EC: 23              INC     HL                  
64ED: CD 6F 70        CALL    $706F               ; {code.PrintPackedAutoWrap}
64F0: 21 7B 65        LD      HL,$657B            
64F3: CD 57 63        CALL    $6357               ; {}
64F6: 2A 22 72        LD      HL,($7222)          ; {}
64F9: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
64FC: 23              INC     HL                  
64FD: 06 03           LD      B,$03               
64FF: CD AD 61        CALL    $61AD               ; {}
6502: D2 10 65        JP      NC,$6510            ; {}
6505: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6508: EB              EX      DE,HL               
6509: 22 7E 65        LD      ($657E),HL          ; {}
650C: EB              EX      DE,HL               
650D: CD 57 63        CALL    $6357               ; {}
6510: 21 7A 88        LD      HL,$887A            
6513: 97              SUB     A                   
6514: 32 F8 71        LD      ($71F8),A           ; {}
6517: 32 F0 71        LD      ($71F0),A           ; {code.stopAtPeriod}
651A: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
651D: D5              PUSH    DE                  
651E: 3A F8 71        LD      A,($71F8)           ; {}
6521: 3C              INC     A                   
6522: 32 F8 71        LD      ($71F8),A           ; {}
6525: 32 0B 72        LD      ($720B),A           ; {}
6528: 22 0C 72        LD      ($720C),HL          ; {}
652B: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
652E: 3A 21 72        LD      A,($7221)           ; {}
6531: BE              CP      (HL)                
6532: C2 71 65        JP      NZ,$6571            ; {}
6535: 23              INC     HL                  
6536: 3A FA 71        LD      A,($71FA)           ; {}
6539: 47              LD      B,A                 
653A: 7E              LD      A,(HL)              
653B: 32 F5 71        LD      ($71F5),A           ; {}
653E: E6 0F           AND     $0F                 
6540: B8              CP      B                   
6541: C2 71 65        JP      NZ,$6571            ; {}
6544: 23              INC     HL                  
6545: 7E              LD      A,(HL)              
6546: 32 F6 71        LD      ($71F6),A           ; {}
6549: 23              INC     HL                  
654A: 22 F3 71        LD      ($71F3),HL          ; {}
654D: 06 03           LD      B,$03               
654F: CD AD 61        CALL    $61AD               ; {}
6552: D2 5D 65        JP      NC,$655D            ; {}
6555: D5              PUSH    DE                  
6556: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6559: CD 57 63        CALL    $6357               ; {}
655C: D1              POP     DE                  
655D: 2A F3 71        LD      HL,($71F3)          ; {}
6560: 06 02           LD      B,$02               
6562: D5              PUSH    DE                  
6563: CD AD 61        CALL    $61AD               ; {}
6566: D1              POP     DE                  
6567: D2 71 65        JP      NC,$6571            ; {}
656A: 23              INC     HL                  
656B: 22 F3 71        LD      ($71F3),HL          ; {}
656E: CD B2 65        CALL    $65B2               ; {}
6571: EB              EX      DE,HL               
6572: D1              POP     DE                  
6573: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE}
6576: DA 1D 65        JP      C,$651D             ; {}
6579: C9              RET                         
657A: B1              OR      C                   
657B: 8B              ADC     A,E                 
657C: B4              OR      H                   
657D: B2              OR      D                   
657E: 00              NOP                         
657F: 00              NOP                         
6580: E5              PUSH    HL                  
6581: 97              SUB     A                   
6582: 32 FB 66        LD      ($66FB),A           ; {}
6585: 32 FA 66        LD      ($66FA),A           ; {}
6588: 3C              INC     A                   
6589: 32 FC 66        LD      ($66FC),A           ; {}
658C: 2A 0C 72        LD      HL,($720C)          ; {}
658F: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6592: 23              INC     HL                  
6593: 7E              LD      A,(HL)              
6594: 32 F5 71        LD      ($71F5),A           ; {}
6597: 23              INC     HL                  
6598: 7E              LD      A,(HL)              
6599: 32 F6 71        LD      ($71F6),A           ; {}
659C: 3A 0B 72        LD      A,($720B)           ; {}
659F: 32 F8 71        LD      ($71F8),A           ; {}
65A2: CD BC 65        CALL    $65BC               ; {}
65A5: E1              POP     HL                  
65A6: 3A FB 66        LD      A,($66FB)           ; {}
65A9: A7              AND     A                   
65AA: CA AF 65        JP      Z,$65AF             ; {}
65AD: 97              SUB     A                   
65AE: C9              RET                         
65AF: F6 01           OR      $01                 
65B1: C9              RET                         
65B2: 97              SUB     A                   
65B3: 32 FA 66        LD      ($66FA),A           ; {}
65B6: 32 FC 66        LD      ($66FC),A           ; {}
65B9: 32 FD 66        LD      ($66FD),A           ; {}
65BC: D5              PUSH    DE                  
65BD: 3A F9 66        LD      A,($66F9)           ; {}
65C0: 3C              INC     A                   
65C1: 32 F9 66        LD      ($66F9),A           ; {}
65C4: 3A F6 71        LD      A,($71F6)           ; {}
65C7: E6 02           AND     $02                 
65C9: CA 45 66        JP      Z,$6645             ; {}
65CC: 3A F5 71        LD      A,($71F5)           ; {}
65CF: E6 20           AND     $20                 
65D1: CA DC 65        JP      Z,$65DC             ; {}
65D4: 3A F5 71        LD      A,($71F5)           ; {}
65D7: E6 80           AND     $80                 
65D9: CA 45 66        JP      Z,$6645             ; {}
65DC: 97              SUB     A                   
65DD: 32 F7 71        LD      ($71F7),A           ; {}
65E0: 32 F9 71        LD      ($71F9),A           ; {}
65E3: 21 7A 88        LD      HL,$887A            
65E6: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
65E9: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE}
65EC: D2 45 66        JP      NC,$6645            ; {}
65EF: 3A F9 71        LD      A,($71F9)           ; {}
65F2: 3C              INC     A                   
65F3: 32 F9 71        LD      ($71F9),A           ; {}
65F6: D5              PUSH    DE                  
65F7: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
65FA: 3A F8 71        LD      A,($71F8)           ; {}
65FD: BE              CP      (HL)                
65FE: C2 40 66        JP      NZ,$6640            ; {}
6601: D5              PUSH    DE                  
6602: 3A F7 71        LD      A,($71F7)           ; {}
6605: A7              AND     A                   
6606: C2 34 66        JP      NZ,$6634            ; {}
6609: 3E 01           LD      A,$01               
660B: 32 F7 71        LD      ($71F7),A           ; {}
660E: 32 FB 66        LD      ($66FB),A           ; {}
6611: E5              PUSH    HL                  
6612: 3A F9 66        LD      A,($66F9)           ; {}
6615: FE 01           CP      $01                 
6617: CA 25 66        JP      Z,$6625             ; {}
661A: 21 7B 65        LD      HL,$657B            
661D: CD 57 63        CALL    $6357               ; {}
6620: 3E 01           LD      A,$01               
6622: 32 FD 66        LD      ($66FD),A           ; {}
6625: 21 7A 65        LD      HL,$657A            
6628: CD 57 63        CALL    $6357               ; {}
662B: 3E 01           LD      A,$01               
662D: 32 FA 66        LD      ($66FA),A           ; {}
6630: E1              POP     HL                  
6631: C3 3C 66        JP      $663C               ; {}
6634: E5              PUSH    HL                  
6635: 21 7C 65        LD      HL,$657C            
6638: CD 57 63        CALL    $6357               ; {}
663B: E1              POP     HL                  
663C: CD FE 66        CALL    $66FE               ; {}
663F: D1              POP     DE                  
6640: EB              EX      DE,HL               
6641: D1              POP     DE                  
6642: C3 E9 65        JP      $65E9               ; {}
6645: 3A F7 71        LD      A,($71F7)           ; {}
6648: A7              AND     A                   
6649: CA 62 66        JP      Z,$6662             ; {}
664C: 3A FA 66        LD      A,($66FA)           ; {}
664F: A7              AND     A                   
6650: CA 62 66        JP      Z,$6662             ; {}
6653: 97              SUB     A                   
6654: 32 FA 66        LD      ($66FA),A           ; {}
6657: 21 7B 65        LD      HL,$657B            
665A: CD 57 63        CALL    $6357               ; {}
665D: 3E 01           LD      A,$01               
665F: 32 FD 66        LD      ($66FD),A           ; {}
6662: 3A F6 71        LD      A,($71F6)           ; {}
6665: E6 01           AND     $01                 
6667: CA D3 66        JP      Z,$66D3             ; {}
666A: 97              SUB     A                   
666B: 32 F7 71        LD      ($71F7),A           ; {}
666E: 32 F9 71        LD      ($71F9),A           ; {}
6671: 21 7A 88        LD      HL,$887A            
6674: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6677: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE}
667A: D2 D3 66        JP      NC,$66D3            ; {}
667D: 3A F9 71        LD      A,($71F9)           ; {}
6680: 3C              INC     A                   
6681: 32 F9 71        LD      ($71F9),A           ; {}
6684: D5              PUSH    DE                  
6685: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6688: 3A F8 71        LD      A,($71F8)           ; {}
668B: BE              CP      (HL)                
668C: C2 CE 66        JP      NZ,$66CE            ; {}
668F: D5              PUSH    DE                  
6690: 3A F7 71        LD      A,($71F7)           ; {}
6693: A7              AND     A                   
6694: C2 C2 66        JP      NZ,$66C2            ; {}
6697: 3E 01           LD      A,$01               
6699: 32 F7 71        LD      ($71F7),A           ; {}
669C: 32 FB 66        LD      ($66FB),A           ; {}
669F: E5              PUSH    HL                  
66A0: 3A F9 66        LD      A,($66F9)           ; {}
66A3: FE 01           CP      $01                 
66A5: CA B3 66        JP      Z,$66B3             ; {}
66A8: 21 7B 65        LD      HL,$657B            
66AB: CD 57 63        CALL    $6357               ; {}
66AE: 3E 01           LD      A,$01               
66B0: 32 FD 66        LD      ($66FD),A           ; {}
66B3: 21 7D 65        LD      HL,$657D            
66B6: CD 57 63        CALL    $6357               ; {}
66B9: E1              POP     HL                  
66BA: 3E 01           LD      A,$01               
66BC: 32 FA 66        LD      ($66FA),A           ; {}
66BF: C3 CA 66        JP      $66CA               ; {}
66C2: E5              PUSH    HL                  
66C3: 21 7C 65        LD      HL,$657C            
66C6: CD 57 63        CALL    $6357               ; {}
66C9: E1              POP     HL                  
66CA: CD FE 66        CALL    $66FE               ; {}
66CD: D1              POP     DE                  
66CE: EB              EX      DE,HL               
66CF: D1              POP     DE                  
66D0: C3 77 66        JP      $6677               ; {}
66D3: 3A F7 71        LD      A,($71F7)           ; {}
66D6: A7              AND     A                   
66D7: CA F0 66        JP      Z,$66F0             ; {}
66DA: 3A FA 66        LD      A,($66FA)           ; {}
66DD: A7              AND     A                   
66DE: CA F0 66        JP      Z,$66F0             ; {}
66E1: 97              SUB     A                   
66E2: 32 FA 66        LD      ($66FA),A           ; {}
66E5: 21 7B 65        LD      HL,$657B            
66E8: CD 57 63        CALL    $6357               ; {}
66EB: 3E 01           LD      A,$01               
66ED: 32 FD 66        LD      ($66FD),A           ; {}
66F0: D1              POP     DE                  
66F1: 3A F9 66        LD      A,($66F9)           ; {}
66F4: 3D              DEC     A                   
66F5: 32 F9 66        LD      ($66F9),A           ; {}
66F8: C9              RET                         
66F9: 00              NOP                         
66FA: 00              NOP                         
66FB: 00              NOP                         
66FC: 00              NOP                         
66FD: 00              NOP                         
66FE: E5              PUSH    HL                  
66FF: 23              INC     HL                  
6700: 23              INC     HL                  
6701: 23              INC     HL                  
6702: 06 02           LD      B,$02               
6704: CD AD 61        CALL    $61AD               ; {}
6707: D2 7C 67        JP      NC,$677C            ; {}
670A: 23              INC     HL                  
670B: 3E 41           LD      A,$41               
670D: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces}
6710: 3E 20           LD      A,$20               
6712: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces}
6715: CD 6F 70        CALL    $706F               ; {code.PrintPackedAutoWrap}
6718: D1              POP     DE                  
6719: 3A FB 66        LD      A,($66FB)           ; {}
671C: F5              PUSH    AF                  
671D: 2A F5 71        LD      HL,($71F5)          ; {}
6720: E5              PUSH    HL                  
6721: 2A F7 71        LD      HL,($71F7)          ; {}
6724: E5              PUSH    HL                  
6725: 3A F9 71        LD      A,($71F9)           ; {}
6728: F5              PUSH    AF                  
6729: 32 F8 71        LD      ($71F8),A           ; {}
672C: 3A 0B 72        LD      A,($720B)           ; {}
672F: F5              PUSH    AF                  
6730: 2A 0C 72        LD      HL,($720C)          ; {}
6733: E5              PUSH    HL                  
6734: 3A F8 71        LD      A,($71F8)           ; {}
6737: 47              LD      B,A                 
6738: 32 0B 72        LD      ($720B),A           ; {}
673B: D5              PUSH    DE                  
673C: CD 57 70        CALL    $7057               ; {code.FindSubList}
673F: 22 0C 72        LD      ($720C),HL          ; {}
6742: D1              POP     DE                  
6743: EB              EX      DE,HL               
6744: 23              INC     HL                  
6745: 7E              LD      A,(HL)              
6746: 32 F5 71        LD      ($71F5),A           ; {}
6749: 23              INC     HL                  
674A: 7E              LD      A,(HL)              
674B: 32 F6 71        LD      ($71F6),A           ; {}
674E: 97              SUB     A                   
674F: 32 FB 66        LD      ($66FB),A           ; {}
6752: 32 F7 71        LD      ($71F7),A           ; {}
6755: CD BC 65        CALL    $65BC               ; {}
6758: E1              POP     HL                  
6759: 22 0C 72        LD      ($720C),HL          ; {}
675C: F1              POP     AF                  
675D: 32 0B 72        LD      ($720B),A           ; {}
6760: F1              POP     AF                  
6761: 32 F9 71        LD      ($71F9),A           ; {}
6764: E1              POP     HL                  
6765: 22 F7 71        LD      ($71F7),HL          ; {}
6768: E1              POP     HL                  
6769: 22 F5 71        LD      ($71F5),HL          ; {}
676C: 3A FB 66        LD      A,($66FB)           ; {}
676F: A7              AND     A                   
6770: CA 77 67        JP      Z,$6777             ; {}
6773: 97              SUB     A                   
6774: 32 F7 71        LD      ($71F7),A           ; {}
6777: F1              POP     AF                  
6778: 32 FB 66        LD      ($66FB),A           ; {}
677B: C9              RET                         
677C: E1              POP     HL                  
677D: C9              RET                         

COM_01__is_in_pack_or_current_room:
677E: 46              LD      B,(HL)              
677F: 23              INC     HL                  
6780: E5              PUSH    HL                  
6781: CD 57 70        CALL    $7057               ; {code.FindSubList}
6784: CD 23 60        CALL    $6023               ; {}
6787: E1              POP     HL                  
6788: C9              RET                         
6789: 3A 1E 72        LD      A,($721E)           ; {}
678C: BE              CP      (HL)                
678D: 23              INC     HL                  
678E: C9              RET                         
678F: 46              LD      B,(HL)              
6790: 23              INC     HL                  
6791: E5              PUSH    HL                  
6792: 78              LD      A,B                 
6793: 32 1E 72        LD      ($721E),A           ; {}
6796: CD 57 70        CALL    $7057               ; {code.FindSubList}
6799: 22 1F 72        LD      ($721F),HL          ; {}
679C: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
679F: 7E              LD      A,(HL)              
67A0: E6 80           AND     $80                 
67A2: 7E              LD      A,(HL)              
67A3: C2 AE 67        JP      NZ,$67AE            ; {}
67A6: 47              LD      B,A                 
67A7: CD 57 70        CALL    $7057               ; {code.FindSubList}
67AA: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
67AD: 7E              LD      A,(HL)              
67AE: 32 21 72        LD      ($7221),A           ; {}
67B1: 47              LD      B,A                 
67B2: 21 00 52        LD      HL,$5200            ; {+ram.sectionData}
67B5: CD A5 61        CALL    $61A5               ; {}
67B8: 22 22 72        LD      ($7222),HL          ; {}
67BB: E1              POP     HL                  
67BC: 97              SUB     A                   
67BD: C9              RET                         

Com_30__:
67BE: 7E              LD      A,(HL)              
67BF: 23              INC     HL                  
67C0: 32 21 72        LD      ($7221),A           ; {}
67C3: 97              SUB     A                   
67C4: C9              RET                         

67C5: 46              LD      B,(HL)              
67C6: 23              INC     HL                  
67C7: C3 AB 6C        JP      $6CAB               ; {}

67CA: 4E              LD      C,(HL)              
67CB: 23              INC     HL                  
67CC: 46              LD      B,(HL)              
67CD: 23              INC     HL                  
67CE: E5              PUSH    HL                  
67CF: CD 57 70        CALL    $7057               ; {code.FindSubList}
67D2: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
67D5: 5E              LD      E,(HL)              
67D6: 23              INC     HL                  
67D7: 7E              LD      A,(HL)              
67D8: E1              POP     HL                  
67D9: 7B              LD      A,E                 
67DA: B9              CP      C                   
67DB: C9              RET                         
67DC: F6 01           OR      $01                 
67DE: C9              RET                         
67DF: 3A 1E 72        LD      A,($721E)           ; {}
67E2: FE 38           CP      $38                 
67E4: CA 00 68        JP      Z,$6800             ; {}
67E7: FE 01           CP      $01                 
67E9: C2 F9 67        JP      NZ,$67F9            ; {}
67EC: 06 01           LD      B,$01               
67EE: E5              PUSH    HL                  
67EF: CD 57 70        CALL    $7057               ; {code.FindSubList}
67F2: CD 23 60        CALL    $6023               ; {}
67F5: E1              POP     HL                  
67F6: CA 00 68        JP      Z,$6800             ; {}
67F9: CD C9 61        CALL    $61C9               ; {}
67FC: EB              EX      DE,HL               
67FD: C3 03 68        JP      $6803               ; {}
6800: CD 6F 70        CALL    $706F               ; {code.PrintPackedAutoWrap}
6803: 97              SUB     A                   
6804: C9              RET                         
6805: CD C1 64        CALL    $64C1               ; {}
6808: 97              SUB     A                   
6809: 32 F0 71        LD      ($71F0),A           ; {code.stopAtPeriod}
680C: C9              RET                         
680D: E5              PUSH    HL                  
680E: 3E 0D           LD      A,$0D               
6810: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces}
6813: 97              SUB     A                   
6814: 32 F8 71        LD      ($71F8),A           ; {}
6817: 21 7A 88        LD      HL,$887A            
681A: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
681D: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE}
6820: D2 7D 68        JP      NC,$687D            ; {}
6823: 3A F8 71        LD      A,($71F8)           ; {}
6826: 3C              INC     A                   
6827: 32 F8 71        LD      ($71F8),A           ; {}
682A: 32 0B 72        LD      ($720B),A           ; {}
682D: 22 0C 72        LD      ($720C),HL          ; {}
6830: D5              PUSH    DE                  
6831: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6834: 46              LD      B,(HL)              
6835: 3A 1E 72        LD      A,($721E)           ; {}
6838: B8              CP      B                   
6839: C2 78 68        JP      NZ,$6878            ; {}
683C: 23              INC     HL                  
683D: 7E              LD      A,(HL)              
683E: 32 F5 71        LD      ($71F5),A           ; {}
6841: 23              INC     HL                  
6842: 7E              LD      A,(HL)              
6843: 32 F6 71        LD      ($71F6),A           ; {}
6846: E6 20           AND     $20                 
6848: CA 78 68        JP      Z,$6878             ; {}
684B: 23              INC     HL                  
684C: 06 02           LD      B,$02               
684E: CD AD 61        CALL    $61AD               ; {}
6851: D2 78 68        JP      NC,$6878            ; {}
6854: 23              INC     HL                  
6855: 22 F3 71        LD      ($71F3),HL          ; {}
6858: D5              PUSH    DE                  
6859: 3E 41           LD      A,$41               
685B: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces}
685E: 3E 20           LD      A,$20               
6860: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces}
6863: CD 66 70        CALL    $7066               ; {code.PrintPackedAndLF}
6866: D1              POP     DE                  
6867: CD B2 65        CALL    $65B2               ; {}
686A: 3A FD 66        LD      A,($66FD)           ; {}
686D: A7              AND     A                   
686E: CA 78 68        JP      Z,$6878             ; {}
6871: 3E 0D           LD      A,$0D               
6873: D5              PUSH    DE                  
6874: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces}
6877: D1              POP     DE                  
6878: EB              EX      DE,HL               
6879: D1              POP     DE                  
687A: C3 1D 68        JP      $681D               ; {}
687D: 97              SUB     A                   
687E: E1              POP     HL                  
687F: C9              RET                         
6880: E5              PUSH    HL                  
6881: 2A 12 72        LD      HL,($7212)          ; {}
6884: 3A 0F 72        LD      A,($720F)           ; {}
6887: 22 24 72        LD      ($7224),HL          ; {}
688A: E1              POP     HL                  
688B: A7              AND     A                   
688C: 46              LD      B,(HL)              
688D: 23              INC     HL                  
688E: CA A8 68        JP      Z,$68A8             ; {}
6891: 4F              LD      C,A                 
6892: 78              LD      A,B                 
6893: A7              AND     A                   
6894: 79              LD      A,C                 
6895: CA A8 68        JP      Z,$68A8             ; {}
6898: E5              PUSH    HL                  
6899: CD 57 70        CALL    $7057               ; {code.FindSubList}
689C: EB              EX      DE,HL               
689D: E1              POP     HL                  
689E: 3A 24 72        LD      A,($7224)           ; {}
68A1: BB              CP      E                   
68A2: C0              RET     NZ                  
68A3: 3A 25 72        LD      A,($7225)           ; {}
68A6: BA              CP      D                   
68A7: C9              RET                         
68A8: B8              CP      B                   
68A9: C9              RET                         
68AA: E5              PUSH    HL                  
68AB: 2A 18 72        LD      HL,($7218)          ; {}
68AE: 3A 15 72        LD      A,($7215)           ; {}
68B1: C3 87 68        JP      $6887               ; {}
68B4: E5              PUSH    HL                  

Com_2D__:
68B5: 2A 0C 72        LD      HL,($720C)          ; {}
68B8: 3A 0B 72        LD      A,($720B)           ; {}
68BB: C3 87 68        JP      $6887               ; {}

68BE: 46              LD      B,(HL)              
68BF: 23              INC     HL                  
68C0: 3A 1D 72        LD      A,($721D)           ; {}
68C3: B8              CP      B                   
68C4: C9              RET                         
68C5: E5              PUSH    HL                  
68C6: 06 01           LD      B,$01               
68C8: CD 57 70        CALL    $7057               ; {code.FindSubList}
68CB: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
68CE: 4E              LD      C,(HL)              
68CF: 2A 0C 72        LD      HL,($720C)          ; {}
68D2: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
68D5: 79              LD      A,C                 
68D6: A7              AND     A                   
68D7: FA E3 68        JP      M,$68E3             ; {}
68DA: 7E              LD      A,(HL)              
68DB: A7              AND     A                   
68DC: F2 E3 68        JP      P,$68E3             ; {}
68DF: E1              POP     HL                  
68E0: F6 01           OR      $01                 
68E2: C9              RET                         
68E3: 3A 1E 72        LD      A,($721E)           ; {}
68E6: 77              LD      (HL),A              
68E7: 23              INC     HL                  
68E8: 7E              LD      A,(HL)              
68E9: E6 F0           AND     $F0                 
68EB: 77              LD      (HL),A              
68EC: 97              SUB     A                   
68ED: E1              POP     HL                  
68EE: C9              RET                         
68EF: E5              PUSH    HL                  
68F0: 2A 0C 72        LD      HL,($720C)          ; {}
68F3: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
68F6: 3A 21 72        LD      A,($7221)           ; {}
68F9: 77              LD      (HL),A              
68FA: 23              INC     HL                  
68FB: 7E              LD      A,(HL)              
68FC: E6 F0           AND     $F0                 
68FE: 47              LD      B,A                 
68FF: 3A FA 71        LD      A,($71FA)           ; {}
6902: B0              OR      B                   
6903: 77              LD      (HL),A              
6904: 97              SUB     A                   
6905: E1              POP     HL                  
6906: C9              RET                         
6907: E5              PUSH    HL                  
6908: 2A 22 72        LD      HL,($7222)          ; {}
690B: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
690E: 23              INC     HL                  
690F: 06 04           LD      B,$04               
6911: CD AD 61        CALL    $61AD               ; {}
6914: D2 20 69        JP      NC,$6920            ; {}
6917: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
691A: CD 57 63        CALL    $6357               ; {}
691D: CA 63 69        JP      Z,$6963             ; {}
6920: 3A 15 72        LD      A,($7215)           ; {}
6923: A7              AND     A                   
6924: CA 41 69        JP      Z,$6941             ; {}
6927: 2A 18 72        LD      HL,($7218)          ; {}
692A: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
692D: 23              INC     HL                  
692E: 23              INC     HL                  
692F: 23              INC     HL                  
6930: 06 06           LD      B,$06               
6932: CD AD 61        CALL    $61AD               ; {}
6935: D2 41 69        JP      NC,$6941            ; {}
6938: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
693B: CD 57 63        CALL    $6357               ; {}
693E: CA 63 69        JP      Z,$6963             ; {}
6941: 3A 0F 72        LD      A,($720F)           ; {}
6944: A7              AND     A                   
6945: C2 4C 69        JP      NZ,$694C            ; {}
6948: E1              POP     HL                  
6949: F6 01           OR      $01                 
694B: C9              RET                         
694C: 2A 12 72        LD      HL,($7212)          ; {}
694F: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6952: 23              INC     HL                  
6953: 23              INC     HL                  
6954: 23              INC     HL                  
6955: 06 07           LD      B,$07               
6957: CD AD 61        CALL    $61AD               ; {}
695A: D2 48 69        JP      NC,$6948            ; {}
695D: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6960: CD 57 63        CALL    $6357               ; {}
6963: E1              POP     HL                  
6964: C9              RET                         
6965: E5              PUSH    HL                  
6966: 2A 0C 72        LD      HL,($720C)          ; {}
6969: 3A 0B 72        LD      A,($720B)           ; {}
696C: C3 76 69        JP      $6976               ; {}
696F: E5              PUSH    HL                  
6970: 2A 12 72        LD      HL,($7212)          ; {}
6973: 3A 0F 72        LD      A,($720F)           ; {}
6976: A7              AND     A                   
6977: CA 63 69        JP      Z,$6963             ; {}
697A: 06 01           LD      B,$01               
697C: E5              PUSH    HL                  
697D: CD 57 70        CALL    $7057               ; {code.FindSubList}
6980: CD 23 60        CALL    $6023               ; {}
6983: E1              POP     HL                  
6984: C2 99 69        JP      NZ,$6999            ; {}
6987: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
698A: 23              INC     HL                  
698B: 23              INC     HL                  
698C: 23              INC     HL                  
698D: 06 02           LD      B,$02               
698F: CD AD 61        CALL    $61AD               ; {}
6992: D2 99 69        JP      NC,$6999            ; {}
6995: 23              INC     HL                  
6996: CD 6F 70        CALL    $706F               ; {code.PrintPackedAutoWrap}
6999: E1              POP     HL                  
699A: 97              SUB     A                   
699B: C9              RET                         
699C: E5              PUSH    HL                  
699D: 3A 15 72        LD      A,($7215)           ; {}
69A0: 2A 18 72        LD      HL,($7218)          ; {}
69A3: C3 76 69        JP      $6976               ; {}
69A6: E5              PUSH    HL                  
69A7: 2A 0C 72        LD      HL,($720C)          ; {}
69AA: 3A 0B 72        LD      A,($720B)           ; {}
69AD: A7              AND     A                   
69AE: CA BC 69        JP      Z,$69BC             ; {}
69B1: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
69B4: 23              INC     HL                  
69B5: 23              INC     HL                  
69B6: 7E              LD      A,(HL)              
69B7: E1              POP     HL                  
69B8: A6              AND     (HL)                
69B9: AE              XOR     (HL)                
69BA: 23              INC     HL                  
69BB: C9              RET                         
69BC: E1              POP     HL                  
69BD: 23              INC     HL                  
69BE: F6 01           OR      $01                 
69C0: C9              RET                         

Com_2F__:
69C1: E5              PUSH    HL                  
69C2: 2A 0C 72        LD      HL,($720C)          ; {}
69C5: 3A 0B 72        LD      A,($720B)           ; {}
69C8: A7              AND     A                   
69C9: CA 48 69        JP      Z,$6948             ; {}
69CC: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
69CF: C3 B5 69        JP      $69B5               ; {}
69D2: E5              PUSH    HL                  
69D3: 2A 0C 72        LD      HL,($720C)          ; {}
69D6: 3A 0B 72        LD      A,($720B)           ; {}
69D9: A7              AND     A                   
69DA: CA 48 69        JP      Z,$6948             ; {}
69DD: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
69E0: 23              INC     HL                  
69E1: 7E              LD      A,(HL)              
69E2: EE 20           XOR     $20                 
69E4: 77              LD      (HL),A              
69E5: E1              POP     HL                  
69E6: 97              SUB     A                   
69E7: C9              RET                         
69E8: E5              PUSH    HL                  
69E9: 2A 0C 72        LD      HL,($720C)          ; {}
69EC: 3A 0B 72        LD      A,($720B)           ; {}
69EF: A7              AND     A                   
69F0: CA 48 69        JP      Z,$6948             ; {}
69F3: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
69F6: 23              INC     HL                  
69F7: 7E              LD      A,(HL)              
69F8: EE 40           XOR     $40                 
69FA: 77              LD      (HL),A              
69FB: E1              POP     HL                  
69FC: 97              SUB     A                   
69FD: C9              RET                         
69FE: 7E              LD      A,(HL)              
69FF: C6 30           ADD     $30                 
6A01: 32 EC 6A        LD      ($6AEC),A           ; {}
6A04: 7E              LD      A,(HL)              
6A05: 32 FA 71        LD      ($71FA),A           ; {}
;
6A08: 21 06 6B        LD      HL,$6B06            
6A0B: 11 E5 6A        LD      DE,$6AE5            
6A0E: 06 21           LD      B,$21               
6A10: 1A              LD      A,(DE)              
6A11: 77              LD      (HL),A              
6A12: 23              INC     HL                  
6A13: 13              INC     DE                  
6A14: 05              DEC     B                   
6A15: C2 10 6A        JP      NZ,$6A10            ; {}
;
6A18: 06 1F           LD      B,$1F               
6A1A: 36 20           LD      (HL),$20            
6A1C: 23              INC     HL                  
6A1D: 05              DEC     B                   
6A1E: C2 1A 6A        JP      NZ,$6A1A            ; {}
6A21: 21 49 6B        LD      HL,$6B49            
6A24: 11 06 6B        LD      DE,$6B06            
6A27: 06 00           LD      B,$00               
6A29: CD 24 44        CALL    $4424               ; {hard.OPEN_EXISTING} Open existing file
6A2C: C2 D0 6A        JP      NZ,$6AD0            ; {}
6A2F: 11 06 6B        LD      DE,$6B06            
6A32: CD 36 44        CALL    $4436               ; {hard.READ_RECORD} Read a record
6A35: 21 00 52        LD      HL,$5200            ; {+ram.sectionData} Overlay room description destination
6A38: 11 49 6B        LD      DE,$6B49            
6A3B: CD AA 6A        CALL    $6AAA               ; {}
6A3E: FE 01           CP      $01                 
6A40: C2 66 6A        JP      NZ,$6A66            ; {}
6A43: CD AA 6A        CALL    $6AAA               ; {}
6A46: CD AA 6A        CALL    $6AAA               ; {}
6A49: CD AA 6A        CALL    $6AAA               ; {}
6A4C: 01 00 01        LD      BC,$0100            
6A4F: 7D              LD      A,L                 
6A50: A7              AND     A                   
6A51: C2 5A 6A        JP      NZ,$6A5A            ; {}
6A54: 7C              LD      A,H                 
6A55: FE 5D           CP      $5D                 
6A57: CA 66 6A        JP      Z,$6A66             ; {}
6A5A: CD AA 6A        CALL    $6AAA               ; {}
6A5D: 77              LD      (HL),A              
6A5E: 23              INC     HL                  
6A5F: 0D              DEC     C                   
6A60: C2 4F 6A        JP      NZ,$6A4F            ; {}
6A63: C3 3B 6A        JP      $6A3B               ; {}
6A66: 11 06 6B        LD      DE,$6B06            
6A69: CD 28 44        CALL    $4428               ; {hard.CLOSE_FILE} Close a file overlay
6A6C: C2 D0 6A        JP      NZ,$6AD0            ; {}
6A6F: 3A 21 72        LD      A,($7221)           ; {}
6A72: 47              LD      B,A                 
6A73: 21 00 52        LD      HL,$5200            ; {+ram.sectionData}
6A76: CD A5 61        CALL    $61A5               ; {}
6A79: 22 22 72        LD      ($7222),HL          ; {}
6A7C: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6A7F: 7E              LD      A,(HL)              
6A80: 32 F0 71        LD      ($71F0),A           ; {code.stopAtPeriod}
6A83: 36 01           LD      (HL),$01            
6A85: 06 01           LD      B,$01               
6A87: CD 57 70        CALL    $7057               ; {code.FindSubList}
6A8A: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6A8D: 3A 21 72        LD      A,($7221)           ; {}
6A90: 77              LD      (HL),A              
6A91: 23              INC     HL                  
6A92: 7E              LD      A,(HL)              
6A93: E6 F0           AND     $F0                 
6A95: 47              LD      B,A                 
6A96: 3A FA 71        LD      A,($71FA)           ; {}
6A99: B0              OR      B                   
6A9A: 77              LD      (HL),A              
6A9B: CD C1 64        CALL    $64C1               ; {}
6A9E: 97              SUB     A                   
6A9F: 32 F0 71        LD      ($71F0),A           ; {code.stopAtPeriod}
6AA2: 3E 0D           LD      A,$0D               
6AA4: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces}
6AA7: C3 38 5D        JP      $5D38               ; {}

6AAA: 7B              LD      A,E                 
6AAB: FE 49           CP      $49                 
6AAD: C2 E2 6A        JP      NZ,$6AE2            ; {}
6AB0: 7A              LD      A,D                 
6AB1: FE 6C           CP      $6C                 
6AB3: C2 E2 6A        JP      NZ,$6AE2            ; {}
6AB6: 11 06 6B        LD      DE,$6B06            
6AB9: E5              PUSH    HL                  
6ABA: C5              PUSH    BC                  
6ABB: CD 36 44        CALL    $4436               ; {hard.READ_RECORD} Seek to record
6ABE: C1              POP     BC                  
6ABF: E1              POP     HL                  
6AC0: 11 49 6B        LD      DE,$6B49            
6AC3: CA AA 6A        JP      Z,$6AAA             ; {}
6AC6: FE 1C           CP      $1C                 
6AC8: CA 66 6A        JP      Z,$6A66             ; {}
6ACB: FE 1D           CP      $1D                 
6ACD: CA 66 6A        JP      Z,$6A66             ; {}
6AD0: 21 48 6B        LD      HL,$6B48            
6AD3: CD 57 63        CALL    $6357               ; {}
6AD6: 11 06 6B        LD      DE,$6B06            
6AD9: CD 28 44        CALL    $4428               ; {hard.CLOSE_FILE} Close a file overlay
6ADC: CA 08 6A        JP      Z,$6A08             ; {}
6ADF: C3 D0 6A        JP      $6AD0               ; {}
6AE2: 1A              LD      A,(DE)              
6AE3: 13              INC     DE                  
6AE4: C9              RET                         

; SECTION0/DAT.DOG:0$
6AE5: 53 45 43 54 49 4F 4E 30 2F 44 41 54 2E 44 4F 47 3A 30 24        
6AF8: 20 20 20 20 20 20 20 20 20 20 20 20 20 20

; SECTION0/DAT.DOG:0$
6B06: 53 45 43 54 49 4F 4E 30 2F 44 41 54 2E 44 4F 47 3A 30 24          
6B19: 20 20 20 20 20 20 20 20 20 20 20 20 20 20 

6B27: 20 20
6B29: 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20
6B39: 20 20 20 20 20 20 20 20 20 20 20 20 20 20
6B47: 20 B3
6B49: 00                     
6B4A: FF              RST     0X38                
6B4B: 00              NOP                         
6B4C: FF              RST     0X38                
6B4D: 00              NOP                         
6B4E: FF              RST     0X38                
6B4F: 00              NOP                         
6B50: FF              RST     0X38                
6B51: 00              NOP                         
6B52: FF              RST     0X38                
6B53: 00              NOP                         
6B54: FF              RST     0X38                
6B55: 00              NOP                         
6B56: FF              RST     0X38                
6B57: 00              NOP                         
6B58: FF              RST     0X38                
6B59: 00              NOP                         
6B5A: FF              RST     0X38                
6B5B: 00              NOP                         
6B5C: FF              RST     0X38                
6B5D: 00              NOP                         
6B5E: FF              RST     0X38                
6B5F: 00              NOP                         
6B60: FF              RST     0X38                
6B61: 00              NOP                         
6B62: FF              RST     0X38                
6B63: 00              NOP                         
6B64: FF              RST     0X38                
6B65: 00              NOP                         
6B66: FF              RST     0X38                
6B67: 00              NOP                         
6B68: FF              RST     0X38                
6B69: 00              NOP                         
6B6A: FF              RST     0X38                
6B6B: 00              NOP                         
6B6C: FF              RST     0X38                
6B6D: 00              NOP                         
6B6E: FF              RST     0X38                
6B6F: 00              NOP                         
6B70: FF              RST     0X38                
6B71: 00              NOP                         
6B72: FF              RST     0X38                
6B73: 00              NOP                         
6B74: FF              RST     0X38                
6B75: 00              NOP                         
6B76: FF              RST     0X38                
6B77: 00              NOP                         
6B78: FF              RST     0X38                
6B79: 00              NOP                         
6B7A: FF              RST     0X38                
6B7B: 00              NOP                         
6B7C: FF              RST     0X38                
6B7D: 00              NOP                         
6B7E: FF              RST     0X38                
6B7F: 00              NOP                         
6B80: F9              LD      SP,HL               
6B81: 00              NOP                         
6B82: FF              RST     0X38                
6B83: 00              NOP                         
6B84: FF              RST     0X38                
6B85: 00              NOP                         
6B86: FF              RST     0X38                
6B87: 00              NOP                         
6B88: FF              RST     0X38                
6B89: 00              NOP                         
6B8A: FF              RST     0X38                
6B8B: 00              NOP                         
6B8C: FF              RST     0X38                
6B8D: 00              NOP                         
6B8E: FF              RST     0X38                
6B8F: 00              NOP                         
6B90: FF              RST     0X38                
6B91: 00              NOP                         
6B92: FF              RST     0X38                
6B93: 00              NOP                         
6B94: FF              RST     0X38                
6B95: 00              NOP                         
6B96: FF              RST     0X38                
6B97: 00              NOP                         
6B98: FF              RST     0X38                
6B99: 00              NOP                         
6B9A: FF              RST     0X38                
6B9B: 00              NOP                         
6B9C: FF              RST     0X38                
6B9D: 00              NOP                         
6B9E: FF              RST     0X38                
6B9F: 00              NOP                         
6BA0: FF              RST     0X38                
6BA1: 00              NOP                         
6BA2: FF              RST     0X38                
6BA3: 00              NOP                         
6BA4: FF              RST     0X38                
6BA5: 00              NOP                         
6BA6: FF              RST     0X38                
6BA7: 00              NOP                         
6BA8: FF              RST     0X38                
6BA9: 00              NOP                         
6BAA: FF              RST     0X38                
6BAB: 00              NOP                         
6BAC: FF              RST     0X38                
6BAD: 00              NOP                         
6BAE: FF              RST     0X38                
6BAF: 00              NOP                         
6BB0: FF              RST     0X38                
6BB1: 00              NOP                         
6BB2: FF              RST     0X38                
6BB3: 00              NOP                         
6BB4: FF              RST     0X38                
6BB5: 00              NOP                         
6BB6: FF              RST     0X38                
6BB7: 00              NOP                         
6BB8: FF              RST     0X38                
6BB9: 00              NOP                         
6BBA: FF              RST     0X38                
6BBB: 00              NOP                         
6BBC: FF              RST     0X38                
6BBD: 00              NOP                         
6BBE: FF              RST     0X38                
6BBF: 00              NOP                         
6BC0: FF              RST     0X38                
6BC1: 00              NOP                         
6BC2: FF              RST     0X38                
6BC3: 00              NOP                         
6BC4: FF              RST     0X38                
6BC5: 00              NOP                         
6BC6: FF              RST     0X38                
6BC7: 00              NOP                         
6BC8: FF              RST     0X38                
6BC9: 00              NOP                         
6BCA: FF              RST     0X38                
6BCB: 00              NOP                         
6BCC: FF              RST     0X38                
6BCD: 00              NOP                         
6BCE: FF              RST     0X38                
6BCF: 00              NOP                         
6BD0: FF              RST     0X38                
6BD1: 00              NOP                         
6BD2: FF              RST     0X38                
6BD3: 00              NOP                         
6BD4: FF              RST     0X38                
6BD5: 00              NOP                         
6BD6: FF              RST     0X38                
6BD7: 00              NOP                         
6BD8: FF              RST     0X38                
6BD9: 00              NOP                         
6BDA: FF              RST     0X38                
6BDB: 00              NOP                         
6BDC: FF              RST     0X38                
6BDD: 00              NOP                         
6BDE: FF              RST     0X38                
6BDF: 00              NOP                         
6BE0: FF              RST     0X38                
6BE1: 00              NOP                         
6BE2: FF              RST     0X38                
6BE3: 00              NOP                         
6BE4: FF              RST     0X38                
6BE5: 00              NOP                         
6BE6: FF              RST     0X38                
6BE7: 00              NOP                         
6BE8: FF              RST     0X38                
6BE9: 00              NOP                         
6BEA: FF              RST     0X38                
6BEB: 00              NOP                         
6BEC: FF              RST     0X38                
6BED: 00              NOP                         
6BEE: FF              RST     0X38                
6BEF: 00              NOP                         
6BF0: FF              RST     0X38                
6BF1: 00              NOP                         
6BF2: FF              RST     0X38                
6BF3: 00              NOP                         
6BF4: FF              RST     0X38                
6BF5: 00              NOP                         
6BF6: FF              RST     0X38                
6BF7: 00              NOP                         
6BF8: FF              RST     0X38                
6BF9: 00              NOP                         
6BFA: FF              RST     0X38                
6BFB: 00              NOP                         
6BFC: FF              RST     0X38                
6BFD: 00              NOP                         
6BFE: FF              RST     0X38                
6BFF: 00              NOP                         
6C00: FF              RST     0X38                
6C01: 00              NOP                         
6C02: FF              RST     0X38                
6C03: 00              NOP                         
6C04: FF              RST     0X38                
6C05: 00              NOP                         
6C06: FF              RST     0X38                
6C07: 00              NOP                         
6C08: FF              RST     0X38                
6C09: 00              NOP                         
6C0A: FF              RST     0X38                
6C0B: 00              NOP                         
6C0C: FF              RST     0X38                
6C0D: 00              NOP                         
6C0E: FF              RST     0X38                
6C0F: 00              NOP                         
6C10: FF              RST     0X38                
6C11: 00              NOP                         
6C12: FF              RST     0X38                
6C13: 00              NOP                         
6C14: FF              RST     0X38                
6C15: 00              NOP                         
6C16: FF              RST     0X38                
6C17: 00              NOP                         
6C18: FF              RST     0X38                
6C19: 00              NOP                         
6C1A: FF              RST     0X38                
6C1B: 00              NOP                         
6C1C: FF              RST     0X38                
6C1D: 00              NOP                         
6C1E: FF              RST     0X38                
6C1F: 00              NOP                         
6C20: FF              RST     0X38                
6C21: 00              NOP                         
6C22: FF              RST     0X38                
6C23: 00              NOP                         
6C24: FF              RST     0X38                
6C25: 00              NOP                         
6C26: FF              RST     0X38                
6C27: 00              NOP                         
6C28: FF              RST     0X38                
6C29: 00              NOP                         
6C2A: FF              RST     0X38                
6C2B: 00              NOP                         
6C2C: FF              RST     0X38                
6C2D: 00              NOP                         
6C2E: FF              RST     0X38                
6C2F: 00              NOP                         
6C30: FF              RST     0X38                
6C31: 00              NOP                         
6C32: FF              RST     0X38                
6C33: 00              NOP                         
6C34: FF              RST     0X38                
6C35: 00              NOP                         
6C36: FF              RST     0X38                
6C37: 00              NOP                         
6C38: FF              RST     0X38                
6C39: 00              NOP                         
6C3A: FF              RST     0X38                
6C3B: 00              NOP                         
6C3C: FF              RST     0X38                
6C3D: 00              NOP                         
6C3E: FF              RST     0X38                
6C3F: 00              NOP                         
6C40: FF              RST     0X38                
6C41: 00              NOP                         
6C42: FF              RST     0X38                
6C43: 00              NOP                         
6C44: FF              RST     0X38                
6C45: 00              NOP                         
6C46: FF              RST     0X38                
6C47: 00              NOP                         
6C48: FF              RST     0X38                


6C49: CD 57 63        CALL    $6357               ; {}
6C4C: C2 52 6C        JP      NZ,$6C52            ; {}
6C4F: F6 01           OR      $01                 
6C51: C9              RET                         
6C52: 97              SUB     A                   
6C53: C9              RET                         

6C54: E5              PUSH    HL                  
6C55: 2A 18 72        LD      HL,($7218)          ; {}
6C58: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6C5B: 3A 0B 72        LD      A,($720B)           ; {}
6C5E: 77              LD      (HL),A              
6C5F: 23              INC     HL                  
6C60: 7E              LD      A,(HL)              
6C61: E6 F0           AND     $F0                 
6C63: 77              LD      (HL),A              
6C64: E1              POP     HL                  
6C65: 97              SUB     A                   
6C66: C9              RET                         

6C67: E5              PUSH    HL                  
6C68: 2A 12 72        LD      HL,($7212)          ; {}
6C6B: C3 58 6C        JP      $6C58               ; {}

Com_17_move_to:
6C6E: 46              LD      B,(HL)              
6C6F: 23              INC     HL                  
6C70: E5              PUSH    HL                  
6C71: CD 57 70        CALL    $7057               ; {code.FindSubList}
6C74: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6C77: D1              POP     DE                  
6C78: 1A              LD      A,(DE)              
6C79: 77              LD      (HL),A              
6C7A: 23              INC     HL                  
6C7B: E6 80           AND     $80                 
6C7D: CA 8C 6C        JP      Z,$6C8C             ; {}
6C80: 7E              LD      A,(HL)              
6C81: E6 F0           AND     $F0                 
6C83: 47              LD      B,A                 
6C84: 3A FA 71        LD      A,($71FA)           ; {}
6C87: B0              OR      B                   
6C88: 77              LD      (HL),A              
6C89: C3 90 6C        JP      $6C90               ; {}
6C8C: 7E              LD      A,(HL)              
6C8D: E6 F0           AND     $F0                 
6C8F: 77              LD      (HL),A              
6C90: EB              EX      DE,HL               
6C91: 23              INC     HL                  
6C92: 97              SUB     A                   
6C93: C9              RET                         

6C94: E5              PUSH    HL                  
6C95: 2A 0C 72        LD      HL,($720C)          ; {}
6C98: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6C9B: 46              LD      B,(HL)              
6C9C: 78              LD      A,B                 
6C9D: A7              AND     A                   
6C9E: E1              POP     HL                  
6C9F: CA 6D 60        JP      Z,$606D             ; {}
6CA2: 3A 1E 72        LD      A,($721E)           ; {}
6CA5: B8              CP      B                   
6CA6: C8              RET     Z                   
6CA7: 78              LD      A,B                 
6CA8: E6 80           AND     $80                 
6CAA: C0              RET     NZ                  

6CAB: E5              PUSH    HL                  
6CAC: CD 57 70        CALL    $7057               ; {code.FindSubList}
6CAF: C3 98 6C        JP      $6C98               ; {}
6CB2: 21 7A 88        LD      HL,$887A            
6CB5: 97              SUB     A                   
6CB6: 32 1C 72        LD      ($721C),A           ; {}
6CB9: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6CBC: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE}
6CBF: D0              RET     NC                  
6CC0: 3A 1C 72        LD      A,($721C)           ; {}
6CC3: 3C              INC     A                   
6CC4: 32 1C 72        LD      ($721C),A           ; {}
6CC7: D5              PUSH    DE                  
6CC8: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6CCB: 4E              LD      C,(HL)              
6CCC: D5              PUSH    DE                  
6CCD: 7E              LD      A,(HL)              
6CCE: A7              AND     A                   
6CCF: CA 46 6D        JP      Z,$6D46             ; {}
6CD2: E6 80           AND     $80                 
6CD4: C2 F6 6C        JP      NZ,$6CF6            ; {}
6CD7: E5              PUSH    HL                  
6CD8: 46              LD      B,(HL)              
6CD9: CD 57 70        CALL    $7057               ; {code.FindSubList}
6CDC: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6CDF: 7E              LD      A,(HL)              
6CE0: A7              AND     A                   
6CE1: CA F2 6C        JP      Z,$6CF2             ; {}
6CE4: E6 80           AND     $80                 
6CE6: CA D8 6C        JP      Z,$6CD8             ; {}
6CE9: 23              INC     HL                  
6CEA: 7E              LD      A,(HL)              
6CEB: E1              POP     HL                  
6CEC: D1              POP     DE                  
6CED: D5              PUSH    DE                  
6CEE: 23              INC     HL                  
6CEF: C3 F8 6C        JP      $6CF8               ; {}
6CF2: E1              POP     HL                  
6CF3: C3 46 6D        JP      $6D46               ; {}
6CF6: 23              INC     HL                  
6CF7: 7E              LD      A,(HL)              
6CF8: E6 0F           AND     $0F                 
6CFA: 47              LD      B,A                 
6CFB: 3A FA 71        LD      A,($71FA)           ; {}
6CFE: B8              CP      B                   
6CFF: C2 46 6D        JP      NZ,$6D46            ; {}
6D02: 23              INC     HL                  
6D03: 23              INC     HL                  
6D04: 06 08           LD      B,$08               
6D06: CD AD 61        CALL    $61AD               ; {}
6D09: D2 46 6D        JP      NC,$6D46            ; {}
6D0C: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6D0F: E5              PUSH    HL                  
6D10: CD C6 71        CALL    $71C6               ; {code.COM_2B_random}
6D13: 3A 1C 72        LD      A,($721C)           ; {}
6D16: 32 1E 72        LD      ($721E),A           ; {}
6D19: 47              LD      B,A                 
6D1A: CD 57 70        CALL    $7057               ; {code.FindSubList}
6D1D: 22 1F 72        LD      ($721F),HL          ; {}
6D20: 79              LD      A,C                 
6D21: A7              AND     A                   
6D22: FA 35 6D        JP      M,$6D35             ; {}
6D25: 47              LD      B,A                 
6D26: CD 57 70        CALL    $7057               ; {code.FindSubList}
6D29: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6D2C: 7E              LD      A,(HL)              
6D2D: A7              AND     A                   
6D2E: C2 21 6D        JP      NZ,$6D21            ; {}
6D31: E1              POP     HL                  
6D32: C3 46 6D        JP      $6D46               ; {}
6D35: 32 21 72        LD      ($7221),A           ; {}
6D38: 21 00 52        LD      HL,$5200            ; {+ram.sectionData}
6D3B: 47              LD      B,A                 
6D3C: CD A5 61        CALL    $61A5               ; {}
6D3F: 22 22 72        LD      ($7222),HL          ; {}
6D42: E1              POP     HL                  
6D43: CD 57 63        CALL    $6357               ; {}
6D46: E1              POP     HL                  
6D47: D1              POP     DE                  
6D48: C3 BC 6C        JP      $6CBC               ; {}

Com_05_is_less_equal_last_random:
6D4B: 3A EC 71        LD      A,($71EC)           ; {code.RandomSeed2}
6D4E: BE              CP      (HL)                
6D4F: 23              INC     HL                  
6D50: DA 59 6D        JP      C,$6D59             ; {}
6D53: CA 59 6D        JP      Z,$6D59             ; {}
6D56: F6 01           OR      $01                 
6D58: C9              RET                         

6D59: 97              SUB     A                   
6D5A: C9              RET                         
6D5B: 4E              LD      C,(HL)              
6D5C: 23              INC     HL                  
6D5D: E5              PUSH    HL                  
6D5E: 2A 0C 72        LD      HL,($720C)          ; {}
6D61: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6D64: 23              INC     HL                  
6D65: 23              INC     HL                  
6D66: 23              INC     HL                  
6D67: E5              PUSH    HL                  
6D68: D5              PUSH    DE                  
6D69: 06 09           LD      B,$09               
6D6B: CD AD 61        CALL    $61AD               ; {}
6D6E: D2 96 6D        JP      NC,$6D96            ; {}
6D71: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6D74: 23              INC     HL                  
6D75: 7E              LD      A,(HL)              
6D76: 91              SUB     C                   
6D77: D2 7B 6D        JP      NC,$6D7B            ; {}
6D7A: 97              SUB     A                   
6D7B: 77              LD      (HL),A              
6D7C: D1              POP     DE                  
6D7D: E1              POP     HL                  
6D7E: A7              AND     A                   
6D7F: CA 85 6D        JP      Z,$6D85             ; {}
6D82: 97              SUB     A                   
6D83: E1              POP     HL                  
6D84: C9              RET                         
6D85: 06 0A           LD      B,$0A               
6D87: CD AD 61        CALL    $61AD               ; {}
6D8A: D2 82 6D        JP      NC,$6D82            ; {}
6D8D: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6D90: CD 57 63        CALL    $6357               ; {}
6D93: C3 82 6D        JP      $6D82               ; {}
6D96: D1              POP     DE                  
6D97: E1              POP     HL                  
6D98: C3 82 6D        JP      $6D82               ; {}
6D9B: 46              LD      B,(HL)              
6D9C: 23              INC     HL                  
6D9D: 4E              LD      C,(HL)              
6D9E: 23              INC     HL                  
6D9F: E5              PUSH    HL                  
6DA0: CD 57 70        CALL    $7057               ; {code.FindSubList}
6DA3: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6DA6: 5E              LD      E,(HL)              
6DA7: 41              LD      B,C                 
6DA8: E5              PUSH    HL                  
6DA9: D5              PUSH    DE                  
6DAA: CD 57 70        CALL    $7057               ; {code.FindSubList}
6DAD: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6DB0: D1              POP     DE                  
6DB1: 7E              LD      A,(HL)              
6DB2: 73              LD      (HL),E              
6DB3: E1              POP     HL                  
6DB4: 77              LD      (HL),A              
6DB5: E1              POP     HL                  
6DB6: 97              SUB     A                   
6DB7: C9              RET                         
6DB8: 4E              LD      C,(HL)              
6DB9: 23              INC     HL                  
6DBA: E5              PUSH    HL                  
6DBB: 2A 0C 72        LD      HL,($720C)          ; {}
6DBE: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6DC1: 23              INC     HL                  
6DC2: 23              INC     HL                  
6DC3: 23              INC     HL                  
6DC4: 06 09           LD      B,$09               
6DC6: CD AD 61        CALL    $61AD               ; {}
6DC9: D2 D8 6D        JP      NC,$6DD8            ; {}
6DCC: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6DCF: 23              INC     HL                  
6DD0: 7E              LD      A,(HL)              
6DD1: B9              CP      C                   
6DD2: DA DC 6D        JP      C,$6DDC             ; {}
6DD5: CA DC 6D        JP      Z,$6DDC             ; {}
6DD8: E1              POP     HL                  
6DD9: F6 01           OR      $01                 
6DDB: C9              RET                         
6DDC: 97              SUB     A                   
6DDD: E1              POP     HL                  
6DDE: C9              RET                         
6DDF: 4E              LD      C,(HL)              
6DE0: 23              INC     HL                  
6DE1: E5              PUSH    HL                  
6DE2: 2A 0C 72        LD      HL,($720C)          ; {}
6DE5: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6DE8: 23              INC     HL                  
6DE9: 23              INC     HL                  
6DEA: 23              INC     HL                  
6DEB: 06 09           LD      B,$09               
6DED: CD AD 61        CALL    $61AD               ; {}
6DF0: D2 DC 6D        JP      NC,$6DDC            ; {}
6DF3: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6DF6: 56              LD      D,(HL)              
6DF7: 23              INC     HL                  
6DF8: 7E              LD      A,(HL)              
6DF9: 81              ADD     A,C                 
6DFA: BA              CP      D                   
6DFB: DA FF 6D        JP      C,$6DFF             ; {}
6DFE: 7A              LD      A,D                 
6DFF: 77              LD      (HL),A              
6E00: C3 DC 6D        JP      $6DDC               ; {}
6E03: 3A 1E 72        LD      A,($721E)           ; {}
6E06: FE 01           CP      $01                 
6E08: C2 10 6E        JP      NZ,$6E10            ; {}
6E0B: 3E 0D           LD      A,$0D               
6E0D: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces}
6E10: 97              SUB     A                   
6E11: C9              RET                         
6E12: E5              PUSH    HL                  
6E13: 2A 0C 72        LD      HL,($720C)          ; {}
6E16: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6E19: 7E              LD      A,(HL)              
6E1A: E6 80           AND     $80                 
6E1C: C2 3E 6E        JP      NZ,$6E3E            ; {}
6E1F: 46              LD      B,(HL)              
6E20: 48              LD      C,B                 
6E21: CD 57 70        CALL    $7057               ; {code.FindSubList}
6E24: 54              LD      D,H                 
6E25: 5D              LD      E,L                 
6E26: D5              PUSH    DE                  
6E27: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6E2A: D1              POP     DE                  
6E2B: 23              INC     HL                  
6E2C: 7E              LD      A,(HL)              
6E2D: E6 20           AND     $20                 
6E2F: CA 3E 6E        JP      Z,$6E3E             ; {}
6E32: 79              LD      A,C                 
6E33: 32 0B 72        LD      ($720B),A           ; {}
6E36: EB              EX      DE,HL               
6E37: 22 0C 72        LD      ($720C),HL          ; {}
6E3A: E1              POP     HL                  
6E3B: F6 01           OR      $01                 
6E3D: C9              RET                         
6E3E: E1              POP     HL                  
6E3F: 97              SUB     A                   
6E40: C9              RET                         
6E41: C3 2D 40        JP      $402D               
6E44: 3E 55           LD      A,$55               
6E46: 32 4F 6F        LD      ($6F4F),A           ; {}
6E49: 3E 39           LD      A,$39               
6E4B: 32 1E 6F        LD      ($6F1E),A           ; {}
6E4E: 3E 20           LD      A,$20               
6E50: 32 03 6F        LD      ($6F03),A           ; {}
6E53: E5              PUSH    HL                  
6E54: 06 92           LD      B,$92               
6E56: CD 57 70        CALL    $7057               ; {code.FindSubList}
6E59: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6E5C: 23              INC     HL                  
6E5D: 3A FA 71        LD      A,($71FA)           ; {}
6E60: 77              LD      (HL),A              
6E61: 06 9B           LD      B,$9B               
6E63: CD 57 70        CALL    $7057               ; {code.FindSubList}
6E66: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6E69: 77              LD      (HL),A              
6E6A: C3 DA 6E        JP      $6EDA               ; {}
6E6D: 3E 55           LD      A,$55               
6E6F: 32 4F 6F        LD      ($6F4F),A           ; {}
6E72: 3E 36           LD      A,$36               
6E74: 32 1E 6F        LD      ($6F1E),A           ; {}
6E77: 3E 24           LD      A,$24               
6E79: 32 03 6F        LD      ($6F03),A           ; {}
6E7C: E5              PUSH    HL                  
6E7D: 21 85 6E        LD      HL,$6E85            
6E80: E3              EX      (SP),HL             
6E81: E5              PUSH    HL                  
6E82: C3 DA 6E        JP      $6EDA               ; {}
6E85: 06 9B           LD      B,$9B               
6E87: CD 57 70        CALL    $7057               ; {code.FindSubList}
6E8A: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6E8D: 7E              LD      A,(HL)              
6E8E: 06 01           LD      B,$01               
6E90: CD 57 70        CALL    $7057               ; {code.FindSubList}
6E93: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6E96: 7E              LD      A,(HL)              
6E97: E6 80           AND     $80                 
6E99: 7E              LD      A,(HL)              
6E9A: C2 A5 6E        JP      NZ,$6EA5            ; {}
6E9D: 46              LD      B,(HL)              
6E9E: CD 57 70        CALL    $7057               ; {code.FindSubList}
6EA1: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6EA4: 7E              LD      A,(HL)              
6EA5: 32 21 72        LD      ($7221),A           ; {}
6EA8: 06 92           LD      B,$92               
6EAA: CD 57 70        CALL    $7057               ; {code.FindSubList}
6EAD: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6EB0: 23              INC     HL                  
6EB1: 3A FA 71        LD      A,($71FA)           ; {}
6EB4: BE              CP      (HL)                
6EB5: CA 6F 6A        JP      Z,$6A6F             ; {}
6EB8: C3 FE 69        JP      $69FE               ; {}
6EBB: 3E 20           LD      A,$20               
6EBD: 32 03 6F        LD      ($6F03),A           ; {}
6EC0: 3E 39           LD      A,$39               
6EC2: C3 CC 6E        JP      $6ECC               ; {}
6EC5: 3E 24           LD      A,$24               
6EC7: 32 03 6F        LD      ($6F03),A           ; {}
6ECA: 3E 36           LD      A,$36               
6ECC: 32 1E 6F        LD      ($6F1E),A           ; {}
6ECF: 3E 53           LD      A,$53               
6ED1: 32 4F 6F        LD      ($6F4F),A           ; {}
6ED4: E5              PUSH    HL                  
6ED5: 3E 30           LD      A,$30               
6ED7: 32 A2 6F        LD      ($6FA2),A           ; {}
6EDA: 21 4F 6F        LD      HL,$6F4F            
6EDD: 11 62 6F        LD      DE,$6F62            
6EE0: 06 13           LD      B,$13               
6EE2: 7E              LD      A,(HL)              
6EE3: 12              LD      (DE),A              
6EE4: 23              INC     HL                  
6EE5: 13              INC     DE                  
6EE6: 05              DEC     B                   
6EE7: C2 E2 6E        JP      NZ,$6EE2            ; {}
6EEA: 3E 20           LD      A,$20               
6EEC: 06 2D           LD      B,$2D               
6EEE: 12              LD      (DE),A              
6EEF: 13              INC     DE                  
6EF0: 05              DEC     B                   
6EF1: C2 EE 6E        JP      NZ,$6EEE            ; {}
6EF4: 3A A2 6F        LD      A,($6FA2)           ; {}
6EF7: 32 73 6F        LD      ($6F73),A           ; {}
6EFA: 21 6E BD        LD      HL,$BD6E            
6EFD: 11 62 6F        LD      DE,$6F62            
6F00: 06 03           LD      B,$03               
6F02: CD 20 44        CALL    $4420               ; {hard.EXECUTE} ?? Open new file overlay vector ??
6F05: C2 47 6F        JP      NZ,$6F47            ; {}
6F08: 21 7A 88        LD      HL,$887A            
6F0B: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6F0E: D5              PUSH    DE                  
6F0F: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6F12: D5              PUSH    DE                  
6F13: 23              INC     HL                  
6F14: 23              INC     HL                  
6F15: 23              INC     HL                  
6F16: E5              PUSH    HL                  
6F17: 2B              DEC     HL                  
6F18: 2B              DEC     HL                  
6F19: 2B              DEC     HL                  
6F1A: 11 62 6F        LD      DE,$6F62            
6F1D: CD 39 44        CALL    $4439               ; {hard.WRITE_RECORD}
6F20: C2 47 6F        JP      NZ,$6F47            ; {}
6F23: E1              POP     HL                  
6F24: D1              POP     DE                  
6F25: D5              PUSH    DE                  
6F26: 06 09           LD      B,$09               
6F28: CD AD 61        CALL    $61AD               ; {}
6F2B: D2 33 6F        JP      NC,$6F33            ; {}
6F2E: D5              PUSH    DE                  
6F2F: 23              INC     HL                  
6F30: C3 1A 6F        JP      $6F1A               ; {}
6F33: E1              POP     HL                  
6F34: D1              POP     DE                  
6F35: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE}
6F38: DA 0E 6F        JP      C,$6F0E             ; {}
6F3B: 11 62 6F        LD      DE,$6F62            
6F3E: CD 28 44        CALL    $4428               ; {hard.CLOSE_FILE}
6F41: C2 47 6F        JP      NZ,$6F47            ; {}
6F44: E1              POP     HL                  
6F45: 97              SUB     A                   
6F46: C9              RET                         
6F47: F6 80           OR      $80                 

6F49: CD 09 44        CALL    $4409               ; {hard.ERROR_SYS4} Error handler: PUSH AF then loads SYS4 overlay
6F4C: C3 38 5D        JP      $5D38               ; {}

6F4F: 53              LD      D,E                 
6F50: 53              LD      D,E                 
6F51: 56              LD      D,(HL)              
6F52: 44              LD      B,H                 
6F53: 4F              LD      C,A                 
6F54: 42              LD      B,D                 
6F55: 4A              LD      C,D                 
6F56: 53              LD      D,E                 
6F57: 2F              CPL                         
6F58: 44              LD      B,H                 
6F59: 41              LD      B,C                 
6F5A: 54              LD      D,H                 
6F5B: 2E 44           LD      L,$44               
6F5D: 4F              LD      C,A                 
6F5E: 47              LD      B,A                 
6F5F: 3A 30 24        LD      A,($2430)           
6F62: 20 20           JR      NZ,$6F84            ; {}
6F64: 20 20           JR      NZ,$6F86            ; {}
6F66: 20 20           JR      NZ,$6F88            ; {}
6F68: 20 20           JR      NZ,$6F8A            ; {}
6F6A: 20 20           JR      NZ,$6F8C            ; {}
6F6C: 20 20           JR      NZ,$6F8E            ; {}
6F6E: 20 20           JR      NZ,$6F90            ; {}
6F70: 20 20           JR      NZ,$6F92            ; {}
6F72: 20 20           JR      NZ,$6F94            ; {}
6F74: 20 20           JR      NZ,$6F96            ; {}
6F76: 20 20           JR      NZ,$6F98            ; {}
6F78: 20 20           JR      NZ,$6F9A            ; {}
6F7A: 20 20           JR      NZ,$6F9C            ; {}
6F7C: 20 20           JR      NZ,$6F9E            ; {}
6F7E: 20 20           JR      NZ,$6FA0            ; {}
6F80: 20 20           JR      NZ,$6FA2            ; {}
6F82: 20 20           JR      NZ,$6FA4            ; {}
6F84: 20 20           JR      NZ,$6FA6            ; {}
6F86: 20 20           JR      NZ,$6FA8            ; {}
6F88: 20 20           JR      NZ,$6FAA            ; {}
6F8A: 20 20           JR      NZ,$6FAC            ; {}
6F8C: 20 20           JR      NZ,$6FAE            ; {}
6F8E: 20 20           JR      NZ,$6FB0            ; {}
6F90: 20 20           JR      NZ,$6FB2            ; {}
6F92: 20 20           JR      NZ,$6FB4            ; {}
6F94: 20 20           JR      NZ,$6FB6            ; {}
6F96: 20 20           JR      NZ,$6FB8            ; {}
6F98: 20 20           JR      NZ,$6FBA            ; {}
6F9A: 20 20           JR      NZ,$6FBC            ; {}
6F9C: 20 20           JR      NZ,$6FBE            ; {}
6F9E: 20 20           JR      NZ,$6FC0            ; {}
6FA0: 20 20           JR      NZ,$6FC2            ; {}
6FA2: 30 00           JR      NC,$6FA4            ; {}
6FA4: 1A              LD      A,(DE)              
6FA5: A7              AND     A                   
6FA6: C8              RET     Z                   
6FA7: D5              PUSH    DE                  
6FA8: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces}
6FAB: D1              POP     DE                  
6FAC: 13              INC     DE                  
6FAD: C3 A4 6F        JP      $6FA4               ; {}
6FB0: E5              PUSH    HL                  
6FB1: 06 92           LD      B,$92               
6FB3: CD 57 70        CALL    $7057               ; {code.FindSubList}
6FB6: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6FB9: 7E              LD      A,(HL)              
6FBA: 32 FB 71        LD      ($71FB),A           ; {}
6FBD: 3A FB 71        LD      A,($71FB)           ; {}
6FC0: E6 0F           AND     $0F                 
6FC2: C6 30           ADD     $30                 
6FC4: 47              LD      B,A                 
6FC5: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces}
6FC8: 3E 00           LD      A,$00               
6FCA: E6 0F           AND     $0F                 
6FCC: C6 30           ADD     $30                 
6FCE: 47              LD      B,A                 
6FCF: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces}
6FD2: 3E 20           LD      A,$20               
6FD4: 47              LD      B,A                 
6FD5: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces}
6FD8: E1              POP     HL                  
6FD9: 97              SUB     A                   
6FDA: C9              RET                         
6FDB: E5              PUSH    HL                  
6FDC: 06 92           LD      B,$92               
6FDE: CD 57 70        CALL    $7057               ; {code.FindSubList}
6FE1: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6FE4: 7E              LD      A,(HL)              
6FE5: C6 01           ADD     $01                 
6FE7: 27              DAA                         
6FE8: 77              LD      (HL),A              
6FE9: E1              POP     HL                  
6FEA: 97              SUB     A                   
6FEB: C9              RET                         

6FEC: E5              PUSH    HL                  
6FED: 21 7A 88        LD      HL,$887A            
6FF0: 97              SUB     A                   
6FF1: 32 1C 72        LD      ($721C),A           ; {}
6FF4: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
6FF7: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE}
6FFA: D2 E9 6F        JP      NC,$6FE9            ; {}
6FFD: D5              PUSH    DE                  
6FFE: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
7001: 7E              LD      A,(HL)              
7002: FE 01           CP      $01                 
7004: C2 23 70        JP      NZ,$7023            ; {}
7007: 23              INC     HL                  
7008: 23              INC     HL                  
7009: 23              INC     HL                  
700A: 06 0C           LD      B,$0C               
700C: CD AD 61        CALL    $61AD               ; {}
700F: D2 23 70        JP      NC,$7023            ; {}
7012: D5              PUSH    DE                  
7013: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
7016: 3A 1C 72        LD      A,($721C)           ; {}
7019: 86              ADD     A,(HL)              
701A: 32 1C 72        LD      ($721C),A           ; {}
701D: D1              POP     DE                  
701E: FE 47           CP      $47                 
7020: D2 28 70        JP      NC,$7028            ; {}
7023: EB              EX      DE,HL               
7024: D1              POP     DE                  
7025: C3 F7 6F        JP      $6FF7               ; {}
7028: D1              POP     DE                  
7029: E1              POP     HL                  
702A: F6 01           OR      $01                 
702C: C9              RET                         
702D: E5              PUSH    HL                  
702E: 21 00 3C        LD      HL,$3C00            
7031: 11 00 04        LD      DE,$0400            
7034: 36 20           LD      (HL),$20            
7036: 23              INC     HL                  
7037: 1B              DEC     DE                  
7038: 7A              LD      A,D                 
7039: B3              OR      E                   
703A: C2 34 70        JP      NZ,$7034            ; {}
703D: E1              POP     HL                  
703E: 97              SUB     A                   
703F: C9              RET                         

7040: E5              PUSH    HL                  ; Hold
7041: CD 99 62        CALL    $6299               ; {code.GetKey} Wait for a key
7044: FE 30           CP      $30                 ; 
7046: DA 41 70        JP      C,$7041             ; {}
7049: FE 34           CP      $34                 
704B: D2 41 70        JP      NC,$7041            ; {}
704E: 32 A2 6F        LD      ($6FA2),A           ; {}
7051: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces}
7054: E1              POP     HL                  
7055: 97              SUB     A                   
7056: C9              RET                         

FindSubList: ; ?? Of what ... what is 887A?
7057: 21 7A 88        LD      HL,$887A            ; Objects??
705A: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
705D: 05              DEC     B                   
705E: C8              RET     Z                   
705F: CD C8 61        CALL    $61C8               ; {code.GetListInfo}
7062: EB              EX      DE,HL               
7063: C3 5D 70        JP      $705D               ; {}

PrintPackedAndLF:
7066: CD 6F 70        CALL    $706F               ; {code.PrintPackedAutoWrap} Print the packed message
7069: 3E 0D           LD      A,$0D               ; Print ...
706B: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces} ... line feed
706E: C9              RET                         

PrintPackedAutoWrap:
706F: 01 00 00        LD      BC,$0000            ; Building length
7072: 7E              LD      A,(HL)              ; First byte of length
7073: E6 80           AND     $80                 ; Is this a 2 byte length?
7075: CA 7D 70        JP      Z,$707D             ; {} No, just use the LSB
7078: 7E              LD      A,(HL)              ; MSB again
7079: E6 7F           AND     $7F                 ; Drop the upper bit flag
707B: 47              LD      B,A                 ; MSB of BC
707C: 23              INC     HL                  ; Point to LSB
;
707D: 4E              LD      C,(HL)              ; Get the LSB of length
707E: 23              INC     HL                  ; Skip the LSB
707F: 78              LD      A,B                 ; Are ...
7080: A7              AND     A                   ; ... there ...
7081: C2 8A 70        JP      NZ,$708A            ; {} ... at least ...
7084: 79              LD      A,C                 ; ... two ...
7085: FE 02           CP      $02                 ; ... bytes left?
7087: DA D4 70        JP      C,$70D4             ; {} No, print these last chars as-is
708A: 3A F0 71        LD      A,($71F0)           ; {code.stopAtPeriod}
708D: A7              AND     A                   
708E: FA E2 70        JP      M,$70E2             ; {}
7091: CD 1B 71        CALL    $711B               ; {code.PrintPackedString}
7094: 0B              DEC     BC                  
7095: 0B              DEC     BC                  
7096: 3A 20 40        LD      A,($4020)           ; {hard.Cursor Pointer}
7099: FE FB           CP      $FB                 
709B: DA 7F 70        JP      C,$707F             ; {}
709E: E5              PUSH    HL                  
709F: 2A 20 40        LD      HL,($4020)          ; {hard.Cursor Pointer}
70A2: 11 BF FF        LD      DE,$FFBF            
70A5: 19              ADD     HL,DE               
70A6: 3E 0D           LD      A,$0D               
70A8: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces}
70AB: 3E 20           LD      A,$20               
70AD: 32 0A 72        LD      ($720A),A           ; {code.lastChar}
70B0: 7E              LD      A,(HL)              
70B1: FE 20           CP      $20                 
70B3: CA BA 70        JP      Z,$70BA             ; {}
70B6: 2B              DEC     HL                  
70B7: C3 B0 70        JP      $70B0               ; {}
70BA: 23              INC     HL                  
70BB: 7E              LD      A,(HL)              
70BC: FE 20           CP      $20                 
70BE: CA D0 70        JP      Z,$70D0             ; {}
70C1: 36 20           LD      (HL),$20            
70C3: FE 1B           CP      $1B                 
70C5: D2 CA 70        JP      NC,$70CA            ; {}
70C8: C6 40           ADD     $40                 
70CA: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces}
70CD: C3 BA 70        JP      $70BA               ; {}
70D0: E1              POP     HL                  
70D1: C3 7F 70        JP      $707F               ; {}
;
70D4: 79              LD      A,C                 ; Any remaining ...
70D5: A7              AND     A                   ; ... characters?
70D6: CA E5 70        JP      Z,$70E5             ; {} No, done
70D9: 7E              LD      A,(HL)              ; Get the extra character
70DA: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces} Print it
70DD: 23              INC     HL                  ; Point to next extra
70DE: 0D              DEC     C                   ; Count of extra chars
70DF: C3 D4 70        JP      $70D4               ; {} Do all extra chars
;
70E2: 21 9A BF        LD      HL,$BF9A            ; ?? Top of stack ?? What the heck ??
;
70E5: 3E 20           LD      A,$20               ; Print a space ...
70E7: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces} ... on the end
70EA: C9              RET                         

PrintCharCullSpaces:
; Print a character and remember the last character printed. Ignore double spaces
; and spaces before punctuation ".", "?", and "!".
70EB: F5              PUSH    AF                  ; Hold the output character
70EC: 3A 0A 72        LD      A,($720A)           ; {code.lastChar} Last printed ...
70EF: FE 20           CP      $20                 ; ... was a space?
70F1: C2 13 71        JP      NZ,$7113            ; {} No ... print it and out
70F4: F1              POP     AF                  ; Restore the output character
70F5: FE 20           CP      $20                 ; Printing a space?
70F7: C8              RET     Z                   ; Yes ... just skip it (done)
70F8: FE 2E           CP      $2E                 ; A period?
70FA: CA 07 71        JP      Z,$7107             ; {} Yes ... remove leading space
70FD: FE 3F           CP      $3F                 ; A question mark?
70FF: CA 07 71        JP      Z,$7107             ; {} Yes ... remove leading space
7102: FE 21           CP      $21                 ; An exclamation mark?
7104: C2 14 71        JP      NZ,$7114            ; {} No ... print and out
;
7107: E5              PUSH    HL                  ; Hold HL
7108: 2A 20 40        LD      HL,($4020)          ; {hard.Cursor Pointer} Back screen ...
710B: 2B              DEC     HL                  ; ... pointer up ...
710C: 22 20 40        LD      ($4020),HL          ; {hard.Cursor Pointer} ... over ignored space
710F: E1              POP     HL                  ; Restore HL
7110: C3 14 71        JP      $7114               ; {} Print character and out
;
7113: F1              POP     AF                  ; Restore character to print
;
7114: 32 0A 72        LD      ($720A),A           ; {code.lastChar} Remember this last printed char
7117: CD 33 00        CALL    $0033               ; {hard.PrintChar} Print the character
711A: C9              RET                         

PrintPackedString:
; If the "stopAfterPeriod" flag is 0, then we print the entire string. Otherwise, we
; print up till the first period (used for short room descriptions).
711B: 11 C2 71        LD      DE,$71C2            ; {+code.unpackBuffer} Pointer to 3-byte unpack buffer
711E: C5              PUSH    BC                  ; Preserve BC
711F: 06 03           LD      B,$03               ; Three characters to extract from word
7121: 7E              LD      A,(HL)              ; Get the MSB of the word
7122: 23              INC     HL                  ; Get the ...
7123: 4E              LD      C,(HL)              ; ... LSB of the word
7124: 23              INC     HL                  ; Update the pointer ...
7125: E5              PUSH    HL                  ; ... to data
7126: 61              LD      H,C                 ; Data word ...
7127: 6F              LD      L,A                 ; ... to HL
7128: 13              INC     DE                  ; Skip to end ...
7129: 13              INC     DE                  ; ... we are storing in reverse
712A: EB              EX      DE,HL               ; Now HL=buffer and DE=data
712B: E5              PUSH    HL                  ; Hold pointer to the buffer
712C: C5              PUSH    BC                  ; Hold our count to 3
;
712D: 21 28 00        LD      HL,$0028            ; The value ...
7130: 22 C0 71        LD      ($71C0),HL          ; {code.valueOfForty} ... 40 for division (repeated subtraction)
7133: 21 63 71        LD      HL,$7163            ; Pointer to shift count
7136: 36 11           LD      (HL),$11            ; Initialize shift count to 11 (end + 1 = 17)
7138: 01 00 00        LD      BC,$0000            ; Value we are extracting
713B: C5              PUSH    BC                  ; 
713C: 7B              LD      A,E                 ; 
713D: 17              RLA                         ; 
713E: 5F              LD      E,A                 ; 
713F: 7A              LD      A,D                 ; 
7140: 17              RLA                         ; TODO decode this like in Pyramid ...
7141: 57              LD      D,A                 ; ... exactly the same code
7142: 35              DEC     (HL)                ; 
7143: E1              POP     HL                  ; 
7144: CA 64 71        JP      Z,$7164             ; {}
7147: 3E 00           LD      A,$00               ; 
7149: CE 00           ADC     $00                 ; 
714B: 29              ADD     HL,HL               ; 
714C: 44              LD      B,H                 ; 
714D: 85              ADD     A,L                 ; 
714E: 2A C0 71        LD      HL,($71C0)          ; {code.valueOfForty}
7151: 95              SUB     L                   ; 
7152: 4F              LD      C,A                 ; 
7153: 78              LD      A,B                 ; 
7154: 9C              SBC     H                   ; 
7155: 47              LD      B,A                 ; 
7156: C5              PUSH    BC                  ; 
7157: D2 5C 71        JP      NC,$715C            ; {}
715A: 09              ADD     HL,BC               ; 
715B: E3              EX      (SP),HL             ; 
715C: 21 63 71        LD      HL,$7163            ; 
715F: 3F              CCF                         ; 
7160: C3 3C 71        JP      $713C               ; {} Do all bits

shiftCount:
7163: 00  ; Count of shifts during the unpack algorithm

7164: 01 97 71        LD      BC,$7197            ; {+code.CharTable} Offset to character table
7167: 09              ADD     HL,BC               ; Offset to the character in the table
7168: 7E              LD      A,(HL)              ; Get the character
7169: C1              POP     BC                  ; Restore the count in B
716A: E1              POP     HL                  ; Restore the pointer to buffer
716B: 77              LD      (HL),A              ; Store the character in the buffer
716C: 2B              DEC     HL                  ; Working backwards in sets of 3
716D: 05              DEC     B                   ; All 3 values extracted?
716E: C2 2B 71        JP      NZ,$712B            ; {} No, go extract them all
;
7171: 21 C2 71        LD      HL,$71C2            ; Pointer to three byte buffer we just filled
7174: 06 03           LD      B,$03               ; Three unpacked characters to print
7176: 7E              LD      A,(HL)              ; Get unpacked character
7177: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces} Print it on the screen
717A: 3A F0 71        LD      A,($71F0)           ; {code.stopAtPeriod} Stopping after ...
717D: A7              AND     A                   ; ... short description?
717E: CA 8F 71        JP      Z,$718F             ; {} No ... print all characters
7181: 7E              LD      A,(HL)              ; Character again
7182: FE 2E           CP      $2E                 ; Did we print a period?
7184: C2 8F 71        JP      NZ,$718F            ; {} No ... keep printing
7187: 3E 80           LD      A,$80               ; ?? flag for stopping short
7189: 32 F0 71        LD      ($71F0),A           ; {code.stopAtPeriod} ??
718C: C3 94 71        JP      $7194               ; {} Abort printing after the short description
718F: 23              INC     HL                  ; Next unpacked
7190: 05              DEC     B                   ; All 3 done?
7191: C2 76 71        JP      NZ,$7176            ; {} Do all 3 characters
7194: E1              POP     HL                  ; Restore ...
7195: C1              POP     BC                  ; ... things we mangled
7196: C9              RET                         

CharTable:
7197: 3F 21 32 20 22 27 3C 3E 2F 30 33                 ; ?!2_"'<>/03
71A2: 41 42 43 44 45 46 47 48 49 4A 4B 4C 4D 4E 4F 50  ; ABCDEFGHIJKLMNOP        
71B2: 51 52 53 54 55 56 57 58 59 5A 2D 2C 2E           ; QRSTUVWXYZ-,.

71BF: 00 ; count of number of words to unpack in TRS80 pyramid engine

valueOfForty:
71C0: 00 00 ; For division by 40 in the unpack

unpackBuffer:
71C2: 00 00 00              

71C5: 00              

COM_2B_random:
71C6: C5              PUSH    BC                  ; Algorithm for random number from seed
71C7: E5              PUSH    HL                  ; 
71C8: 2A EC 71        LD      HL,($71EC)          ; {code.RandomSeed2}
71CB: 06 17           LD      B,$17               ; 
71CD: 7D              LD      A,L                 ; 
71CE: E6 06           AND     $06                 ; 
71D0: 37              SCF                         ; 
71D1: EA D5 71        JP      PE,$71D5            ; {}
71D4: 3F              CCF                         ; 
71D5: 7C              LD      A,H                 ; 
71D6: 1F              RRA                         ; 
71D7: 67              LD      H,A                 ; 
71D8: 7D              LD      A,L                 ; 
71D9: 1F              RRA                         ; 
71DA: E6 FE           AND     $FE                 ; 
71DC: 6F              LD      L,A                 ; 
71DD: 05              DEC     B                   ; 
71DE: C2 CE 71        JP      NZ,$71CE            ; {}
71E1: 22 EC 71        LD      ($71EC),HL          ; {code.RandomSeed2}
71E4: 97              SUB     A                   ; 
71E5: E1              POP     HL                  ; 
71E6: C1              POP     BC                  ; 
71E7: C9              RET                         

RandomSeed1:
71E8: 12 23 44 1D       ; Exact same seed from Bedlam
RandomSeed2:
71EC: 27 4D 2D 13

stopAtPeriod:
71F0: 00  ;  0 means print all. non-zero means stop printing after first period (short description of room)

71F1: 00              NOP                         
71F2: 00              NOP                         
71F3: 00              NOP                         
71F4: 00              NOP                         
71F5: 00              NOP                         
71F6: 00              NOP                         
71F7: 00              NOP                         
71F8: 00              NOP                         
71F9: 00              NOP                         
71FA: 00              NOP                         
71FB: 00              NOP                         
71FC: 00              NOP                         
71FD: 00              NOP                         
71FE: 00              NOP                         
71FF: 00              NOP                         

; Section data loads here ??

7200: 00              NOP                         
7201: 00              NOP                         
7202: 00              NOP                         
7203: 00              NOP                         
7204: 00              NOP                         
7205: 00              NOP                         
7206: 00              NOP                         
7207: 00              NOP                         
7208: 00              NOP                         
7209: 00              NOP                         

lastChar:
720A: 00  ; last character printed

720B: 00              NOP                         
720C: 00              NOP                         
720D: 00              NOP                         
720E: 00              NOP                         
720F: 00              NOP                         
7210: 00              NOP                         
7211: 00              NOP                         
7212: 00              NOP                         
7213: 00              NOP                         
7214: 00              NOP                         
7215: 00              NOP                         
7216: 00              NOP                         
7217: 00              NOP                         
7218: 00              NOP                         
7219: 00              NOP                         
721A: 00              NOP                         
721B: 00              NOP                         
721C: 00              NOP                         
721D: 00              NOP                         
721E: 01 00 00        LD      BC,$0000            
7221: 81              ADD     A,C                 
7222: 03              INC     BC                  
7223: 52              LD      D,D                 
7224: 48              LD      C,B                 
7225: 72              LD      (HL),D              
7226: 00              NOP                         
7227: 00              NOP                         
7228: 06 3F           LD      B,$3F               
722A: 56              LD      D,(HL)              
722B: 45              LD      B,L                 
722C: 52              LD      D,D                 
722D: 42              LD      B,D                 
722E: 3F              CCF                         
722F: 06 3F           LD      B,$3F               
7231: 57              LD      D,A                 
7232: 48              LD      C,B                 
7233: 41              LD      B,C                 
7234: 54              LD      D,H                 
7235: 3F              CCF                         
7236: 07              RLCA                        
7237: 3F              CCF                         
7238: 57              LD      D,A                 
7239: 48              LD      C,B                 
723A: 49              LD      C,C                 
723B: 43              LD      B,E                 
723C: 48              LD      C,B                 
723D: 3F              CCF                         
723E: 08              EX      AF,AF'              
723F: 3F              CCF                         
7240: 50              LD      D,B                 
7241: 48              LD      C,B                 
7242: 52              LD      D,D                 
7243: 41              LD      B,C                 
7244: 53              LD      D,E                 
7245: 45              LD      B,L                 
7246: 3F              CCF                         
7247: D4 00 00        CALL    NC,$0000            
724A: 00              NOP                         
724B: 00              NOP                         
724C: 00              NOP                         
724D: 00              NOP                         
724E: 00              NOP                         
724F: 00              NOP                         
7250: 00              NOP                         
7251: 00              NOP                         
7252: 00              NOP                         
7253: 00              NOP                         
7254: 00              NOP                         
7255: 00              NOP                         
7256: 00              NOP                         
7257: 00              NOP                         
7258: 00              NOP                         
7259: 00              NOP                         
725A: 00              NOP                         
725B: 00              NOP                         
725C: 00              NOP                         
725D: 00              NOP                         
725E: 00              NOP                         
725F: 00              NOP                         
7260: 00              NOP                         
7261: 00              NOP                         
7262: 00              NOP                         
7263: 00              NOP                         
7264: 00              NOP                         
7265: 00              NOP                         
7266: 94              SUB     H                   
7267: A3              AND     E                   

CommandJumpTable:
7268: DC 63        ; 00 move_ACTIVE_and_look(room)
726A: 7E 67        ; 01 is_in_pack_or_current_room(object)
726C: C5 67        ; 02
726E: CA 67        ; 03
7270: DF 67        ; 04
7272: 4B 6D        ; 05
7274: 0D 68        ; 06
7276: 05 68        ; 07
7278: 80 68        ; 08
727A: AA 68        ; 09
727C: BE 68        ; 0A
727E: B7 63        ; 0B
7280: DC 67        ; 0C
7282: 8A 63        ; 0D
7284: A0 63        ; 0E
7286: C5 68        ; 0F
7288: EF 68        ; 10
728A: 6F 69        ; 11
728C: 9C 69        ; 12
728E: 07 69        ; 13
7290: 49 6C        ; 14
7292: A6 69        ; 15
7294: 65 69        ; 16
7296: 6E 6C        ; 17
7298: 94 6C        ; 18
729A: F5 63        ; 19
729C: 2C 64        ; 1A
729E: 3C 64        ; 1B
72A0: 4C 64        ; 1C
72A2: 5B 6D        ; 1D
72A4: 9B 6D        ; 1E
72A6: EC 67        ; 1F
72A8: 89 67        ; 20
72AA: 60 64        ; 21
72AC: B8 6D        ; 22
72AE: DF 6D        ; 23
72B0: 41 6E        ; 24
72B2: 03 6E        ; 25
72B4: B0 6F        ; 26
72B6: 6D 6E        ; 27
72B8: 44 6E        ; 28
72BA: D2 69        ; 29
72BC: E8 69        ; 2A
72BE: C6 71        ; COM_2B_random
72C0: 8F 67        ; 2C
72C2: B4 68        ; 2D
;
72C4: C1 69        ; 2E
72C6: FE 69        ; 2F
72C8: BE 67        ; 30
72CA: 54 6C        ; 31
72CC: 67 6C        ; 32
72CE: 80 65        ; 33
72D0: BB 6E        ; 34
72D2: C5 6E        ; 35
72D4: 12 6E        ; 36
72D6: 12 64        ; 37
72D8: DB 6F        ; 39
72DA: EC 6F        ; 39
72DC: 2D 70        ; 3A
72DE: 40 70        ; 3B
72E0: 00
```

# Phrase List

Very similar to Bedlam.

Many words map to the same word number. For instance GET, HOLD, TAKE, SQUEEZ, REMOVE, and CARRY
all map to verb number 09. The words HANDGR and HANDLE both map to noun number 67.

The phrase list below shows only the first word from the list of possible words for verbs and
prepositions. These possible words can be used interchangably. For instance, user inputs 
"CARRY HANDLE", "GET HANDLE" and "SQUEEZe HANDGRip"  would all map to phrase 05 below with 
the same target object (noun 67). These three user inputs all do the same thing.

```code
PhraseList:
72E1: 05 00 00 00 01     ; 01:  NORTH    *          *           *    
72E6: 06 00 00 00 02     ; 02:  SOUTH    *          *           *    
72EB: 07 00 00 00 03     ; 03:  EAST     *          *           *    
72F0: 08 00 00 00 04     ; 04:  WEST     *          *           *    
72F5: 09 00 20 00 05     ; 05:  GET      ..C.....   *           *    
72FA: 09 02 20 20 43     ; 43:  GET      ..C.....   WITH     ..C.....
72FF: 34 07 00 80 05     ; 05:  PICK     *          UP       u.......
7304: 34 07 80 00 05     ; 05:  PICK     u.......   UP          *    
7309: 0A 00 20 00 06     ; 06:  DROP     ..C.....   *           *    
730E: 0A 05 20 02 0F     ; 0F:  DROP     ..C.....   IN       ......O.
7313: 0A 0C 20 01 4B     ; 4B:  DROP     ..C.....   ON       .......L
7318: 25 00 80 00 4F     ; 4F:  DRINK    u.......   *           *    
731D: 29 00 80 00 4E     ; 4E:  POUR     u.......   *           *    
7322: 29 05 80 02 4E     ; 4E:  POUR     u.......   IN       ......O.
7327: 29 0C 80 01 4E     ; 4E:  POUR     u.......   ON       .......L
732C: 2A 02 02 80 4D     ; 4D:  FILL     ......O.   WITH     u.......
7331: 0A 06 00 08 16     ; 16:  DROP     *          OUT      ....A...
7336: 0B 00 00 00 07     ; 07:  INVENT   *          *           *    
733B: 01 00 04 00 08     ; 08:  READ     .....?..   *           *    
7340: 04 02 10 40 09     ; 09:  ATTACK   ...P....   WITH     .v......
7345: 0C 00 00 00 0A     ; 0A:  LOOK     *          *           *    
734A: 0C 03 00 80 0B     ; 0B:  LOOK     *          AT       u.......
734F: 0C 04 00 80 0C     ; 0C:  LOOK     *          UNDER    u.......
7354: 0C 05 00 02 10     ; 10:  LOOK     *          IN       ......O.
7359: 0C 0C 00 01 4C     ; 4C:  LOOK     *          ON       .......L
735E: 03 03 60 10 0D     ; 0D:  THROW    .vC.....   AT       ...P....
7363: 03 05 20 80 39     ; 39:  THROW    ..C.....   IN       u.......
7368: 03 08 00 20 06     ; 06:  THROW    *          DOWN     ..C.....
736D: 03 01 80 10 0E     ; 0E:  THROW    u.......   TO       ...P....
7372: 0D 01 80 10 0E     ; 0E:  GIVE     u.......   TO       ...P....
7377: 0E 00 00 00 0A     ; 0A:  EXAMIN   *          *           *    
737C: 0E 00 80 00 0B     ; 0B:  EXAMIN   u.......   *           *    
7381: 0E 05 00 80 0B     ; 0B:  EXAMIN   *          IN       u.......
7386: 0F 00 80 00 11     ; 11:  OPEN     u.......   *           *    
738B: 0F 02 80 80 3A     ; 3A:  OPEN     u.......   WITH     u.......
7390: 38 00 08 00 40     ; 40:  CLOSE    ....A...   *           *    
7395: 39 02 08 80 41     ; 41:  LOCK     ....A...   WITH     u.......
739A: 3A 02 80 80 42     ; 42:  UNLOCK   u.......   WITH     u.......
739F: 10 00 80 00 12     ; 12:  PULL     u.......   *           *    
73A4: 10 08 00 80 12     ; 12:  PULL     *          DOWN     u.......
73A9: 10 08 80 00 12     ; 12:  PULL     u.......   DOWN        *    
73AE: 10 06 00 80 05     ; 05:  PULL     *          OUT      u.......
73B3: 10 06 80 00 05     ; 05:  PULL     u.......   OUT         *    
73B8: 10 07 00 80 2D     ; 2D:  PULL     *          UP       u.......
73BD: 10 07 80 00 2D     ; 2D:  PULL     u.......   UP          *    
73C2: 10 02 80 80 12     ; 12:  PULL     u.......   WITH     u.......
73C7: 11 02 08 08 14     ; 14:  LIGHT    ....A...   WITH     ....A...
73CC: 12 00 80 00 15     ; 15:  EAT      u.......   *           *    
73D1: 13 06 00 08 16     ; 16:  BLOW     *          OUT      ....A...
73D6: 14 00 08 00 16     ; 16:  EXTING   ....A...   *           *    
73DB: 15 00 80 00 17     ; 17:  CLIMB    u.......   *           *    
73E0: 15 07 00 00 54     ; 54:  CLIMB    *          UP          *    
73E5: 15 08 00 00 55     ; 55:  CLIMB    *          DOWN        *    
73EA: 15 07 00 80 54     ; 54:  CLIMB    *          UP       u.......
73EF: 15 08 00 80 55     ; 55:  CLIMB    *          DOWN     u.......
73F4: 15 09 00 80 17     ; 17:  CLIMB    *          OVER     u.......
73F9: 15 0C 00 80 17     ; 17:  CLIMB    *          ON       u.......
73FE: 41 00 00 00 36     ; 36:  ENTER    *          *           *    
7403: 41 00 80 00 36     ; 36:  ENTER    u.......   *           *    
7408: 41 05 00 00 36     ; 36:  ENTER    *          IN          *    
740D: 41 05 00 80 36     ; 36:  ENTER    *          IN       u.......
7412: 15 05 00 00 36     ; 36:  CLIMB    *          IN          *    
7417: 15 05 00 80 36     ; 36:  CLIMB    *          IN       u.......
741C: 15 06 00 00 37     ; 37:  CLIMB    *          OUT         *    
7421: 15 06 00 80 37     ; 37:  CLIMB    *          OUT      u.......
7426: 15 04 00 80 38     ; 38:  CLIMB    *          UNDER    u.......
742B: 16 00 80 00 18     ; 18:  RUB      u.......   *           *    
7430: 17 00 00 00 19     ; 19:  DIAGNO   *          *           *    
7435: 18 00 00 00 1A     ; 1A:  ??       *          *           *    
743A: 05 01 00 00 01     ; 01:  NORTH    *          TO          *    
743F: 06 01 00 00 02     ; 02:  SOUTH    *          TO          *    
7444: 07 01 00 00 03     ; 03:  EAST     *          TO          *    
7449: 08 01 00 00 04     ; 04:  WEST     *          TO          *    
744E: 0A 08 00 20 06     ; 06:  DROP     *          DOWN     ..C.....
7453: 0A 08 20 00 06     ; 06:  DROP     ..C.....   DOWN        *    
7458: 0A 0A 20 80 06     ; 06:  DROP     ..C.....   BEHIND   u.......
745D: 0A 04 20 80 06     ; 06:  DROP     ..C.....   UNDER    u.......
7462: 0C 07 00 00 0A     ; 0A:  LOOK     *          UP          *    
7467: 0C 08 00 00 0A     ; 0A:  LOOK     *          DOWN        *    
746C: 0C 09 80 00 0B     ; 0B:  LOOK     u.......   OVER        *    
7471: 0C 09 00 80 0A     ; 0A:  LOOK     *          OVER     u.......
7476: 0C 0B 00 00 0A     ; 0A:  LOOK     *          AROUND      *    
747B: 0C 0A 00 00 0A     ; 0A:  LOOK     *          BEHIND      *    
7480: 0C 0B 00 80 1B     ; 1B:  LOOK     *          AROUND   u.......
7485: 0C 0A 00 80 1C     ; 1C:  LOOK     *          BEHIND   u.......
748A: 0C 06 00 00 1D     ; 1D:  LOOK     *          OUT         *    
748F: 2F 00 00 00 1E     ; 1E:  YES      *          *           *    
7494: 30 00 00 00 1F     ; 1F:  NO       *          *           *    
7499: 32 00 00 00 21     ; 21:  PLUGH    *          *           *    
749E: 2B 00 00 00 22     ; 22:  SCREAM   *          *           *    
74A3: 2D 00 00 00 23     ; 23:  QUIT     *          *           *    
74A8: 2C 00 00 00 25     ; 25:  LEAVE    *          *           *    
74AD: 2C 00 20 00 06     ; 06:  LEAVE    ..C.....   *           *    
74B2: 3B 00 00 00 44     ; 44:  HELLO    *          *           *    
74B7: 3B 00 10 00 45     ; 45:  HELLO    ...P....   *           *    
74BC: 3B 01 00 00 44     ; 44:  HELLO    *          TO          *    
74C1: 3B 01 00 10 45     ; 45:  HELLO    *          TO       ...P....
74C6: 3B 01 10 00 45     ; 45:  HELLO    ...P....   TO          *    
74CB: 3C 00 00 00 46     ; 46:  WHAT     *          *           *    
74D0: 3C 00 80 00 47     ; 47:  WHAT     u.......   *           *    
74D5: 21 00 00 00 25     ; 25:  GO       *          *           *    
74DA: 21 01 00 80 3D     ; 3D:  GO       *          TO       u.......
74DF: 21 05 00 00 36     ; 36:  GO       *          IN          *    
74E4: 21 05 00 80 36     ; 36:  GO       *          IN       u.......
74E9: 21 0C 00 80 36     ; 36:  GO       *          ON       u.......
74EE: 21 06 00 00 37     ; 37:  GO       *          OUT         *    
74F3: 21 06 00 80 37     ; 37:  GO       *          OUT      u.......
74F8: 21 0D 00 80 37     ; 37:  GO       *          OFF      u.......
74FD: 21 04 00 80 38     ; 38:  GO       *          UNDER    u.......
7502: 21 07 00 00 54     ; 54:  GO       *          UP          *    
7507: 21 08 00 00 55     ; 55:  GO       *          DOWN        *    
750C: 21 07 00 80 54     ; 54:  GO       *          UP       u.......
7511: 21 08 00 80 55     ; 55:  GO       *          DOWN     u.......
7516: 21 0B 00 80 26     ; 26:  GO       *          AROUND   u.......
751B: 23 00 80 00 27     ; 27:  KICK     u.......   *           *    
7520: 23 08 00 80 27     ; 27:  KICK     *          DOWN     u.......
7525: 23 05 00 80 27     ; 27:  KICK     *          IN       u.......
752A: 24 02 10 80 28     ; 28:  FEED     ...P....   WITH     u.......
752F: 24 01 80 10 29     ; 29:  FEED     u.......   TO       ...P....
7534: 26 00 80 00 2A     ; 2A:  ??       u.......   *           *    
7539: 28 00 00 00 2C     ; 2C:  SCORE    *          *           *    
753E: 1C 00 80 00 2D     ; 2D:  LIFT     u.......   *           *    
7543: 1F 00 00 00 2F     ; 2F:  WAIT     *          *           *    
7548: 1F 0B 00 00 2F     ; 2F:  WAIT     *          AROUND      *    
754D: 09 07 00 00 54     ; 54:  GET      *          UP          *    
7552: 09 08 00 00 55     ; 55:  GET      *          DOWN        *    
7557: 09 05 00 00 36     ; 36:  GET      *          IN          *    
755C: 09 05 00 80 36     ; 36:  GET      *          IN       u.......
7561: 09 06 00 00 37     ; 37:  GET      *          OUT         *    
7566: 09 06 00 80 37     ; 37:  GET      *          OUT      u.......
756B: 09 0C 00 80 36     ; 36:  GET      *          ON       u.......
7570: 09 0D 00 80 37     ; 37:  GET      *          OFF      u.......
7575: 1A 00 80 00 31     ; 31:  FIND     u.......   *           *    
757A: 20 09 00 80 34     ; 34:  JUMP     *          OVER     u.......
757F: 20 05 00 00 36     ; 36:  JUMP     *          IN          *    
7584: 20 05 00 80 36     ; 36:  JUMP     *          IN       u.......
7589: 20 06 00 80 37     ; 37:  JUMP     *          OUT      u.......
758E: 20 0C 00 80 35     ; 35:  JUMP     *          ON       u.......
7593: 1D 09 00 80 34     ; 34:  STEP     *          OVER     u.......
7598: 1D 05 00 00 36     ; 36:  STEP     *          IN          *    
759D: 1D 05 00 80 36     ; 36:  STEP     *          IN       u.......
75A2: 1D 06 00 80 37     ; 37:  STEP     *          OUT      u.......
75A7: 1D 0C 00 80 35     ; 35:  STEP     *          ON       u.......
75AC: 36 00 00 00 3E     ; 3E:  LOAD     *          *           *    
75B1: 37 00 00 00 3F     ; 3F:  SAVE     *          *           *    
75B6: 3D 00 80 00 48     ; 48:  LOWER    u.......   *           *    
75BB: 3E 08 80 00 48     ; 48:  LET      u.......   DOWN        *    
75C0: 3E 08 00 80 48     ; 48:  LET      *          DOWN     u.......
75C5: 09 08 00 80 48     ; 48:  GET      *          DOWN     u.......
75CA: 09 08 80 00 48     ; 48:  GET      u.......   DOWN        *    
75CF: 3F 00 00 00 4A     ; 4A:  COME     *          *           *    
75D4: 3F 02 00 00 4A     ; 4A:  COME     *          WITH        *    
75D9: 40 00 80 00 49     ; 49:  MEET     u.......   *           *    
75DE: 40 01 80 80 49     ; 49:  MEET     u.......   TO       u.......
75E3: 42 00 80 00 52     ; 52:  START    u.......   *           *    
75E8: 43 00 80 00 53     ; 53:  STRIKE   u.......   *           *    
75ED: 44 0C 00 80 50     ; 50:  TURN     *          ON       u.......
75F2: 44 0C 80 00 50     ; 50:  TURN     u.......   ON          *    
75F7: 44 0D 00 80 51     ; 51:  TURN     *          OFF      u.......
75FC: 44 0D 80 00 51     ; 51:  TURN     u.......   OFF         *    
7601: 45 02 80 80 56     ; 56:  DIG      u.......   WITH     u.......
7606: 46 02 80 80 57     ; 57:  SHOOT    u.......   WITH     u.......
760B: 47 00 80 00 58     ; 58:  POINT    u.......   *           *    
7610: 47 01 00 80 58     ; 58:  POINT    *          TO       u.......
7615: 47 03 00 80 58     ; 58:  POINT    *          AT       u.......
761A: 48 00 80 00 59     ; 59:  TASTE    u.......   *           *    
761F: 49 00 00 00 5A     ; 5A:  THUM     *          *           *    
7624: 49 00 80 00 5A     ; 5A:  THUM     u.......   *           * 

7629: 00                 
762A: 00                  

KnownWords:
762B: CA 
762C: 00
;
762D: 04 52 45 41 44               01 ; READ
7633: 03 47 45 54                  09 ; GET
7638: 04 48 4F 4C 44               09 ; HOLD
763E: 05 54 48 52 4F 57            03 ; THROW
7645: 04 54 4F 53 53               03 ; TOSS
764B: 06 41 54 54 41 43 4B         04 ; ATTACK
7653: 04 4B 49 4C 4C               04 ; KILL
7659: 03 48 49 54                  04 ; HIT
765E: 06 44 45 53 54 52 4F         04 ; DESTRO
7666: 05 4E 4F 52 54 48            05 ; NORTH
766D: 01 4E                        05 ; N
7670: 06 4E 55 52 47 4C 45         05 ; NURGLE
7678: 05 53 4F 55 54 48            06 ; SOUTH
767F: 01 53                        06 ; S
7682: 06 53 4F 52 57 49 54         06 ; SORWIT
768A: 04 45 41 53 54               07 ; EAST
7690: 01 45                        07 ; E
7693: 06 45 4E 55 52 47 4C         07 ; ENURGL
769B: 04 57 45 53 54               08 ; WEST
76A1: 01 57                        08 ; W
76A4: 06 57 49 54 53 4F 52         08 ; WITSOR
76AC: 04 54 41 4B 45               09 ; TAKE
76B2: 04 47 52 41 42               09 ; GRAB
76B8: 06 53 51 55 45 45 5A         09 ; SQUEEZ
76C0: 06 52 45 4D 4F 56 45         09 ; REMOVE
76C8: 05 43 41 52 52 59            09 ; CARRY
76CF: 04 44 52 4F 50               0A ; DROP
76D5: 06 52 45 4C 45 41 53         0A ; RELEAS
76DD: 03 50 55 54                  0A ; PUT
76E2: 06 49 4E 56 45 4E 54         0B ; INVENT
76EA: 01 49                        0B ; I
76ED: 04 4C 4F 4F 4B               0C ; LOOK
76F3: 01 4C                        0C ; L
76F6: 04 47 49 56 45               0D ; GIVE
76FC: 05 4F 46 46 45 52            0D ; OFFER
7703: 06 45 58 41 4D 49 4E         0E ; EXAMIN
770B: 06 44 45 53 43 52 49         0E ; DESCRI
7713: 06 53 45 41 52 43 48         0E ; SEARCH
771B: 04 4F 50 45 4E               0F ; OPEN
7721: 05 42 52 45 41 4B            0F ; BREAK
7728: 04 50 55 4C 4C               10 ; PULL
772E: 05 4C 49 47 48 54            11 ; LIGHT
7735: 04 42 55 52 4E               11 ; BURN
773B: 06 49 47 4E 49 54 45         11 ; IGNITE
7743: 03 45 41 54                  12 ; EAT
7748: 04 42 4C 4F 57               13 ; BLOW
774E: 06 45 58 54 49 4E 47         14 ; EXTING
7756: 05 43 4C 49 4D 42            15 ; CLIMB
775D: 06 41 53 43 45 4E 44         15 ; ASCEND
7765: 06 44 45 53 43 45 4E         15 ; DESCEN
776D: 03 52 55 42                  16 ; RUB
7772: 04 57 49 50 45               16 ; WIPE
7778: 06 50 4F 4C 49 53 48         16 ; POLISH
7780: 06 44 49 41 47 4E 4F         17 ; DIAGNO
7788: 04 46 49 4E 44               1A ; FIND
778E: 04 4C 49 46 54               1C ; LIFT
7794: 04 53 54 45 50               1D ; STEP
779A: 04 57 41 49 54               1F ; WAIT
77A0: 05 50 41 55 53 45            1F ; PAUSE
77A7: 04 53 54 41 59               1F ; STAY
77AD: 04 4A 55 4D 50               20 ; JUMP
77B3: 02 47 4F                     21 ; GO
77B7: 03 53 49 54                  21 ; SIT
77BC: 03 52 55 4E                  21 ; RUN
77C1: 04 4C 45 46 54               21 ; LEFT
77C7: 05 52 49 47 48 54            21 ; RIGHT
77CE: 04 50 55 53 48               10 ; PUSH
77D4: 05 50 52 45 53 53            10 ; PRESS
77DB: 04 4D 4F 56 45               10 ; MOVE
77E1: 04 4B 49 43 4B               23 ; KICK
77E7: 04 46 45 45 44               24 ; FEED
77ED: 05 44 52 49 4E 4B            25 ; DRINK
77F4: 03 53 41 59                  27 ; SAY
77F9: 05 53 43 4F 52 45            28 ; SCORE
7800: 04 50 4F 55 52               29 ; POUR
7806: 04 44 55 4D 50               29 ; DUMP
780C: 04 46 49 4C 4C               2A ; FILL
7812: 06 53 43 52 45 41 4D         2B ; SCREAM
781A: 04 59 45 4C 4C               2B ; YELL
7820: 04 51 55 49 54               2D ; QUIT
7826: 04 53 54 4F 50               2D ; STOP
782C: 03 59 45 53                  2F ; YES
7831: 02 4E 4F                     30 ; NO
7835: 05 50 4C 55 47 48            32 ; PLUGH
783C: 05 4C 45 41 56 45            2C ; LEAVE
7843: 04 50 49 43 4B               34 ; PICK
7849: 04 4C 4F 41 44               36 ; LOAD
784F: 04 53 41 56 45               37 ; SAVE
7855: 05 43 4C 4F 53 45            38 ; CLOSE
785C: 04 4C 4F 43 4B               39 ; LOCK
7862: 06 55 4E 4C 4F 43 4B         3A ; UNLOCK
786A: 05 48 45 4C 4C 4F            3B ; HELLO
7871: 02 48 49                     3B ; HI
7875: 04 57 48 41 54               3C ; WHAT
787B: 03 57 48 59                  3C ; WHY
7880: 03 48 4F 57                  3C ; HOW
7885: 05 57 48 45 52 45            3C ; WHERE
788C: 03 57 48 4F                  3C ; WHO
7891: 04 57 48 45 4E               3C ; WHEN
7897: 05 4C 4F 57 45 52            3D ; LOWER
789E: 05 55 4E 54 49 45            3D ; UNTIE
78A5: 03 4C 45 54                  3E ; LET
78AA: 04 43 4F 4D 45               3F ; COME
78B0: 06 46 4F 4C 4C 4F 57         3F ; FOLLOW
78B8: 04 4D 45 45 54               40 ; MEET
78BE: 06 49 4E 54 52 4F 44         40 ; INTROD
78C6: 05 45 4E 54 45 52            41 ; ENTER
78CD: 05 53 54 41 52 54            42 ; START
78D4: 05 44 52 49 56 45            42 ; DRIVE
78DB: 06 53 54 52 49 4B 45         43 ; STRIKE
78E3: 04 54 55 52 4E               44 ; TURN
78E9: 03 44 49 47                  45 ; DIG
78EE: 05 53 48 4F 4F 54            46 ; SHOOT
78F5: 05 50 4F 49 4E 54            47 ; POINT
78FC: 05 54 41 53 54 45            48 ; TASTE
7903: 04 54 48 55 4D               49 ; THUM
7909: 00
;
790A: 03 4B 45 59                  16 ; KEY
790F: 05 55 4B 4F 52 4B            16 ; UKORK
7916: 04 44 45 53 4B               1A ; DESK
791C: 05 54 41 42 4C 45            1A ; TABLE
7923: 06 53 50 48 4F 52 58         1A ; SPHORX
792B: 06 44 52 41 57 45 52         1B ; DRAWER
7933: 04 44 4F 4F 52               10 ; DOOR
7939: 05 44 4F 4F 52 53            10 ; DOORS
7940: 05 45 53 4E 45 4C            10 ; ESNEL
7947: 06 43 41 42 49 4E 45         19 ; CABINE
794F: 06 43 52 4F 57 42 41         37 ; CROWBA
7957: 06 50 4F 53 54 45 52         38 ; POSTER
795F: 06 53 48 4F 54 47 55         39 ; SHOTGU
7967: 03 47 55 4E                  39 ; GUN
796C: 04 50 55 4D 50               3A ; PUMP
7972: 06 50 41 44 4C 4F 43         29 ; PADLOC
797A: 04 48 41 4E 44               1F ; HAND
7980: 05 48 41 4E 44 53            1F ; HANDS
7987: 04 4A 41 43 4B               31 ; JACK
798D: 04 4A 45 45 50               32 ; JEEP
7993: 04 54 49 52 45               21 ; TIRE
7999: 04 50 49 43 4B               3B ; PICK
799F: 06 53 48 4F 56 45 4C         26 ; SHOVEL
79A7: 05 53 4E 41 4B 45            0C ; SNAKE
79AE: 05 4D 4F 4E 45 59            27 ; MONEY
79B5: 04 46 4F 4F 44               1C ; FOOD
79BB: 04 57 41 4C 4C               25 ; WALL
79C1: 05 57 41 4C 4C 53            25 ; WALLS
79C8: 05 46 4C 41 53 4D            25 ; FLASM
79CF: 04 53 41 46 45               1D ; SAFE
79D5: 06 44 59 4E 41 4D 49         1E ; DYNAMI
79DD: 05 53 54 49 43 4B            1E ; STICK
79E4: 04 52 4F 4F 4D               2A ; ROOM
79EA: 05 46 4C 4F 4F 52            2B ; FLOOR
79F1: 06 47 52 4F 55 4E 44         2B ; GROUND
79F9: 04 45 58 49 54               2C ; EXIT
79FF: 04 5A 49 54 45               2C ; ZITE
7A05: 06 50 41 53 53 41 47         2D ; PASSAG
7A0D: 06 50 4C 4F 4F 4E 41         2D ; PLOONA
7A15: 04 48 4F 4C 45               2E ; HOLE
7A1B: 06 43 4F 52 52 49 44         2F ; CORRID
7A23: 06 48 41 4C 4C 57 41         33 ; HALLWA
7A2B: 06 43 48 41 4D 42 45         34 ; CHAMBE
7A33: 06 45 4E 54 52 41 4E         36 ; ENTRAN
7A3B: 06 43 45 49 4C 49 4E         3B ; CEILIN
7A43: 04 52 4F 4F 46               3B ; ROOF
7A49: 06 42 4F 54 54 4C 45         11 ; BOTTLE
7A51: 06 57 48 49 53 4B 45         4C ; WHISKE
7A59: 06 53 4F 4C 55 54 49         4C ; SOLUTI
7A61: 03 42 41 52                  4D ; BAR
7A66: 05 52 41 44 49 4F            12 ; RADIO
7A6D: 06 42 4C 55 52 4E 55         12 ; BLURNU
7A75: 06 42 55 54 54 4F 4E         4A ; BUTTON
7A7D: 05 57 41 54 45 52            4F ; WATER
7A84: 04 53 49 4E 4B               4E ; SINK
7A8A: 06 43 4F 55 4E 54 45         50 ; COUNTE
7A92: 06 44 52 45 53 53 45         51 ; DRESSE
7A9A: 04 48 4F 4F 44               52 ; HOOD
7AA0: 04 46 55 53 45               1E ; FUSE
7AA6: 03 42 45 44                  55 ; BED
7AAB: 05 43 48 41 49 52            53 ; CHAIR
7AB2: 06 42 4F 55 4C 44 45         54 ; BOULDE
7ABA: 04 52 4F 43 4B               54 ; ROCK
7AC0: 05 52 4F 43 4B 53            54 ; ROCKS
7AC7: 05 53 54 4F 4E 45            54 ; STONE
7ACE: 06 53 54 4F 4E 45 53         54 ; STONES
7AD6: 04 53 41 4E 44               57 ; SAND
7ADC: 04 44 49 52 54               57 ; DIRT
7AE2: 06 41 51 55 41 52 49         58 ; AQUARI
7AEA: 04 53 49 47 4E               56 ; SIGN
7AF0: 05 53 49 47 4E 53            56 ; SIGNS
7AF7: 06 4D 45 53 53 41 47         56 ; MESSAG
7AFF: 06 57 49 4E 44 4F 57         59 ; WINDOW
7B07: 06 53 48 45 4C 54 45         5A ; SHELTE
7B0F: 05 41 4C 49 45 4E            5B ; ALIEN
7B16: 06 43 52 45 41 54 55         5B ; CREATU
7B1E: 04 41 4E 54 53               5B ; ANTS
7B24: 03 41 4E 54                  5B ; ANT
7B29: 04 43 55 42 45               5C ; CUBE
7B2F: 06 50 49 43 54 55 52         5D ; PICTUR
7B37: 06 43 59 4C 49 4E 44         5E ; CYLIND
7B3F: 05 47 4C 4F 42 45            5E ; GLOBE
7B46: 06 47 4C 4F 42 45 53         5E ; GLOBES
7B4E: 06 4C 49 47 48 54 53         5F ; LIGHTS
7B56: 06 43 4F 4E 53 4F 4C         62 ; CONSOL
7B5E: 05 50 41 4E 45 4C            62 ; PANEL
7B65: 06 53 43 52 45 45 4E         63 ; SCREEN
7B6D: 05 45 41 52 54 48            64 ; EARTH
7B74: 04 4D 4F 4F 4E               65 ; MOON
7B7A: 04 53 48 49 50               66 ; SHIP
7B80: 06 48 41 4E 44 47 52         67 ; HANDGR
7B88: 06 48 41 4E 44 4C 45         67 ; HANDLE
7B90: 04 56 49 41 4C               68 ; VIAL
7B96: 06 50 45 44 45 53 54         69 ; PEDEST
7B9E: 03 52 4F 44                  6E ; ROD
7BA3: 06 4D 41 43 48 49 4E         6F ; MACHIN
7BAB: 06 50 52 4F 53 50 45         70 ; PROSPE
7BB3: 06 47 4F 4F 4C 55 42         71 ; GOOLUB
7BBB: 00
;
7BBC: 04 47 52 45 59               6C ; GREY
7BC2: 04 47 52 41 59               6C ; GRAY
7BC8: 04 49 4E 43 48               6D ; INCH
7BCE: 06 4D 41 52 4F 4F 4E         61 ; MAROON
7BD6: 05 57 48 49 54 45            60 ; WHITE
7BDD: 05 47 52 45 45 4E            6A ; GREEN
7BE4: 06 59 45 4C 4C 4F 57         48 ; YELLOW
7BEC: 06 4F 52 41 4E 47 45         49 ; ORANGE
7BF4: 03 52 45 44                  13 ; RED
7BF9: 06 4D 41 53 54 45 52         14 ; MASTER
7C01: 05 42 52 41 53 53            15 ; BRASS
7C08: 06 53 45 43 52 45 54         3D ; SECRET
7C10: 06 53 4B 45 4C 45 54         17 ; SKELET
7C18: 05 53 54 45 45 4C            18 ; STEEL
7C1F: 03 43 41 42                  4B ; CAB
7C24: 03 42 49 47                  0E ; BIG
7C29: 05 4C 41 52 47 45            0E ; LARGE
7C30: 05 53 4D 41 4C 4C            0F ; SMALL
7C37: 06 4C 49 54 54 4C 45         0F ; LITTLE
7C3F: 03 54 4F 50                  28 ; TOP
7C44: 06 4D 49 44 44 4C 45         3C ; MIDDLE
7C4C: 06 42 4F 54 54 4F 4D         3E ; BOTTOM
7C54: 04 46 4C 41 54               22 ; FLAT
7C5A: 05 53 50 41 52 45            23 ; SPARE
7C61: 04 42 4C 55 45               0D ; BLUE
7C67: 06 4D 41 53 53 49 56         3F ; MASSIV
7C6F: 04 42 41 4E 4B               40 ; BANK
7C75: 06 53 41 4C 4F 4F 4E         41 ; SALOON
7C7D: 06 53 48 45 52 49 46         42 ; SHERIF
7C85: 06 4F 46 46 49 43 45         42 ; OFFICE
7C8D: 06 53 4C 49 4D 27 53         43 ; SLIM'S
7C95: 05 53 4C 49 4D 53            43 ; SLIMS
7C9C: 05 42 4F 42 27 53            44 ; BOB'S
7CA3: 04 42 4F 42 53               44 ; BOBS
7CA9: 06 44 4F 55 42 4C 45         45 ; DOUBLE
7CB1: 05 48 4F 54 45 4C            47 ; HOTEL
7CB8: 06 53 57 49 4E 47 49         46 ; SWINGI
7CC0: 04 54 53 4F 4D               6B ; TSOM
7CC6: 04 43 4F 4F 4C               72 ; COOL
7CCC: 05 43 4C 45 41 52            74 ; CLEAR
7CD3: 05 42 52 4F 57 4E            73 ; BROWN
7CDA: 00
;
7CDB: 02 54 4F                     01 ; TO
7CDF: 04 57 49 54 48               02 ; WITH
7CE5: 05 55 53 49 4E 47            02 ; USING
7CEC: 02 41 54                     03 ; AT
7CF0: 05 55 4E 44 45 52            04 ; UNDER
7CF7: 02 49 4E                     05 ; IN
7CFB: 04 49 4E 54 4F               05 ; INTO
7D01: 06 49 4E 53 49 44 45         05 ; INSIDE
7D09: 04 54 48 52 55               05 ; THRU
7D0F: 06 54 48 52 4F 55 47         05 ; THROUG
7D17: 03 4F 55 54                  06 ; OUT
7D1C: 06 4F 55 54 53 49 44         06 ; OUTSID
7D24: 02 55 50                     07 ; UP
7D28: 04 44 4F 57 4E               08 ; DOWN
7D2E: 04 4F 56 45 52               09 ; OVER
7D34: 06 42 45 48 49 4E 44         0A ; BEHIND
7D3C: 06 41 52 4F 55 4E 44         0B ; AROUND
7D44: 02 4F 4E                     0C ; ON
7D48: 03 4F 46 46                  0D ; OFF
7D4D: 00

; ObjectData: ??
; GeneralScript: ??
; CommonCommands: ??
7D4E: 00 8B 29        
;
7D51: 0E 8B 26 
7D54: 0D            
7D55: 3F             
7D56: 0E 08        
7D58: 0A    
7D59: 01 0A 02      
7D5C: 0A              LD      A,(BC)              
7D5D: 03              INC     BC                  
7D5E: 0A              LD      A,(BC)              
7D5F: 04              INC     B                   
7D60: 0E 33           LD      C,$33               
7D62: 0D              DEC     C                   
7D63: 20 14           JR      NZ,$7D79            ; {}
7D65: 37              SCF                         
7D66: 0E 1C           LD      C,$1C               
7D68: 13              INC     DE                  
7D69: 0D              DEC     C                   
7D6A: 19              ADD     HL,DE               
7D6B: 20 01           JR      NZ,$7D6E            ; {}
7D6D: 04 15                         ; PRINT, Length: 0x0015
;
; YOU WALK AIMLESSLY INTO A WALL.
;
7D6F:    C7 DE F3 17 CB 8C CF 47 F5 8B D3 B8 D0 15 6B BF ; 
7D7F:    59 45 46 48 2E             ; 
7D84: 0D 0F                         ; WHILE PASS, Length: 0x000F
7D86:    04 0B                      ;   PRINT, Length: 0x000B
;
; YOU ARE STILL IN
;
7D88:       C7 DE 94 14 55 5E 8E BE 0B 8A 4E ; 
7D93:    AA                         ;   COMMAND 0xAA
7D94:    8B                         ;   COMMAND 0x8B
7D95: 0B 8A E2 0A                   ; SWITCH, Length: 0x0AE2, Function to call: 0x0A
7D99:    05                         ;   Phrase number: 0x05
7D9A:    0A                         ;   ELSE go to: 0x7DA5
7D9B:       0E 08                   ;     WHILE FAIL, Length: 0x0008
7D9D:          A2                   ;       COMMAND 0xA2
7D9E: 13              INC     DE                  
7D9F: 0D              DEC     C                   
7DA0: 02              LD      (BC),A              
7DA1: 1A              LD      A,(DE)              
7DA2: 8F              ADC     A,A                 
7DA3: 14              INC     D                   
7DA4: 0C              INC     C                   
7DA5: 43              LD      B,E                 
7DA6: 0D              DEC     C                   
7DA7: 0E 0B           LD      C,$0B               
7DA9: A2              AND     D                   
7DAA: 13              INC     DE                  
7DAB: 0D              DEC     C                   
7DAC: 03              INC     BC                  
7DAD: 1B              DEC     DE                  
7DAE: 14              INC     D                   
7DAF: 8F              ADC     A,A                 
7DB0: 0D              DEC     C                   
7DB1: 02              LD      (BC),A              
7DB2: 1A              LD      A,(DE)              
7DB3: 8F              ADC     A,A                 
7DB4: 06 23           LD      B,$23               
7DB6: 0E 21           LD      C,$21               
7DB8: 13              INC     DE                  
7DB9: 0D              DEC     C                   
7DBA: 13              INC     DE                  
7DBB: 1A              LD      A,(DE)              
7DBC: 14              INC     D                   
7DBD: 15              DEC     D                   
7DBE: 20 
7DBF: 04 0B                         ; PRINT, Length: 0x000B
;
; HOW CAN YOU DROP
;
7DC1:    89 74 D3 14 9B 96 1B A1 F9 5B 50 ; 
7DCC: A8                            ; COMMAND 0xA8
7DCD: 8B                            ; COMMAND 0x8B
7DCE: 0D 09                         ; WHILE PASS, Length: 0x0009
7DD0:    10                         ;   DROP VAR
7DD1:    04 06                      ;   PRINT, Length: 0x0006
;
; DROPPED. 
;
7DD3:       F9 5B 9F A6 9B 5D       ;        
7DD9: 08              EX      AF,AF'              
7DDA: 17              RLA                         
7DDB: 0E 15           LD      C,$15               
7DDD: 13              INC     DE                  
7DDE: 0D              DEC     C                   
7DDF: 12              LD      (DE),A              
7DE0: 04              INC     B                   
7DE1: 0E 5F           LD      C,$5F               
7DE3: BE              CP      (HL)                
7DE4: 5D              LD      E,L                 
7DE5: B1              OR      C                   
7DE6: D0              RET     NC                  
7DE7: B5              OR      L                   
7DE8: D9              EXX                         
7DE9: 9C              SBC     H                   
7DEA: 16 B2           LD      D,$B2               
7DEC: 91              SUB     C                   
7DED: 7A              LD      A,D                 
7DEE: C0              RET     NZ                  
7DEF: 16 A8           LD      D,$A8               
7DF1: 8B              ADC     A,E                 
7DF2: 11 15 0E        LD      DE,$0E15            
7DF5: 13              INC     DE                  
7DF6: 13              INC     DE                  
7DF7: 92              SUB     D                   
7DF8: 0D              DEC     C                   
7DF9: 0D              DEC     C                   
7DFA: 1A              LD      A,(DE)              
7DFB: 2E 40           LD      L,$40               
7DFD: A8              XOR     B                   
7DFE: 04              INC     B                   
7DFF: 07              RLCA                        
7E00: 4B              LD      C,E                 
7E01: 7B              LD      A,E                 
7E02: 75              LD      (HL),L              
7E03: 8D              ADC     A,L                 
7E04: A6              AND     (HL)                
7E05: 85              ADD     A,L                 
7E06: 2E A5           LD      L,$A5               
7E08: A6              AND     (HL)                
7E09: 3A 11 0E        LD      A,($0E11)           
7E0C: 0F              RRCA                        
7E0D: 0D              DEC     C                   
7E0E: 03              INC     BC                  
7E0F: 1B              DEC     DE                  
7E10: 14              INC     D                   
7E11: 8F              ADC     A,A                 
7E12: 13              INC     DE                  
7E13: 92              SUB     D                   
7E14: A5              AND     L                   
7E15: 0D              DEC     C                   
7E16: 04              INC     B                   
7E17: 2E 40           LD      L,$40               
7E19: 2A 0C A6        LD      HL,($A60C)          ; {}
7E1C: 40              LD      B,B                 
7E1D: 24              INC     H                   
7E1E: 0E 22           LD      C,$22               
7E20: 13              INC     DE                  
7E21: 92              SUB     D                   
7E22: 0D              DEC     C                   
7E23: 0E 1A           LD      C,$1A               
7E25: 2E 20           LD      L,$20               
7E27: A8              XOR     B                   
7E28: 04              INC     B                   
7E29: 08              EX      AF,AF'              
7E2A: 4B              LD      C,E                 
7E2B: 7B              LD      A,E                 
7E2C: 06 9A           LD      B,$9A               
7E2E: C2 16 A7        JP      NZ,$A716            ; {}
7E31: 61              LD      H,C                 
7E32: 0D              DEC     C                   
7E33: 0E 29           LD      C,$29               
7E35: A8              XOR     B                   
7E36: 04              INC     B                   
7E37: 0A              LD      A,(BC)              
7E38: 4B              LD      C,E                 
7E39: 7B              LD      A,E                 
7E3A: 09              ADD     HL,BC               
7E3B: 9A              SBC     D                   
7E3C: DE 14           SBC     $14                 
7E3E: D7              RST     0X10                
7E3F: A0              AND     B                   
7E40: 9B              SBC     E                   
7E41: 5D              LD      E,L                 
7E42: 42              LD      B,D                 
7E43: 2D              DEC     L                   
7E44: 0E 2B           LD      C,$2B               
7E46: 0D              DEC     C                   
7E47: 03              INC     BC                  
7E48: 1B              DEC     DE                  
7E49: 14              INC     D                   
7E4A: 8F              ADC     A,A                 
7E4B: 13              INC     DE                  
7E4C: 92              SUB     D                   
7E4D: 0D              DEC     C                   
7E4E: 11 1A 14        LD      DE,$141A            
7E51: 2E 40           LD      L,$40               
7E53: A8              XOR     B                   
7E54: 04              INC     B                   
7E55: 0A              LD      A,(BC)              
7E56: 4B              LD      C,E                 
7E57: 7B              LD      A,E                 
7E58: 06 9A           LD      B,$9A               
7E5A: 49              LD      C,C                 
7E5B: 16 97           LD      D,$97               
7E5D: 54              LD      D,H                 
7E5E: 9B              SBC     E                   
7E5F: 5D              LD      E,L                 
7E60: 0D              DEC     C                   
7E61: 0F              RRCA                        
7E62: 2A A8 04        LD      HL,($04A8)          
7E65: 0B              DEC     BC                  
7E66: 4B              LD      C,E                 
7E67: 7B              LD      A,E                 
7E68: 09              ADD     HL,BC               
7E69: 9A              SBC     D                   
7E6A: B0              OR      B                   
7E6B: 17              RLA                         
7E6C: 75              LD      (HL),L              
7E6D: 8D              ADC     A,L                 
7E6E: A6              AND     (HL)                
7E6F: 85              ADD     A,L                 
7E70: 2E 41           LD      L,$41               
7E72: 45              LD      B,L                 
7E73: 0E 43           LD      C,$43               
7E75: 0D              DEC     C                   
7E76: 03              INC     BC                  
7E77: 1B              DEC     DE                  
7E78: 14              INC     D                   
7E79: 8F              ADC     A,A                 
7E7A: 13              INC     DE                  
7E7B: 92              SUB     D                   
7E7C: 0D              DEC     C                   
7E7D: 17              RLA                         
7E7E: 14              INC     D                   
7E7F: 09              ADD     HL,BC               
7E80: 14              INC     D                   
7E81: 04              INC     B                   
7E82: 0A              LD      A,(BC)              
7E83: C7              RST     0X00                
7E84: DE D3           SBC     $D3                 
7E86: 14              INC     D                   
7E87: E6 96           AND     $96                 
7E89: 49              LD      C,C                 
7E8A: 16 8B           LD      D,$8B               
7E8C: 54              LD      D,H                 
7E8D: A8              XOR     B                   
7E8E: 04              INC     B                   
7E8F: 03              INC     BC                  
7E90: 56              LD      D,(HL)              
7E91: D1              POP     DE                  
7E92: 48              LD      C,B                 
7E93: A9              XOR     C                   
7E94: 8B              ADC     A,E                 
7E95: 0D              DEC     C                   
7E96: 11 1A 2E        LD      DE,$2E1A            
7E99: 40              LD      B,B                 
7E9A: A8              XOR     B                   
7E9B: 04              INC     B                   
7E9C: 0B              DEC     BC                  
7E9D: 4B              LD      C,E                 
7E9E: 7B              LD      A,E                 
7E9F: 06 9A           LD      B,$9A               
7EA1: B0              OR      B                   
7EA2: 17              RLA                         
7EA3: 75              LD      (HL),L              
7EA4: 8D              ADC     A,L                 
7EA5: A6              AND     (HL)                
7EA6: 85              ADD     A,L                 
7EA7: 2E 0D           LD      L,$0D               
7EA9: 0E 2A           LD      C,$2A               
7EAB: A8              XOR     B                   
7EAC: 04              INC     B                   
7EAD: 0A              LD      A,(BC)              
7EAE: 4B              LD      C,E                 
7EAF: 7B              LD      A,E                 
7EB0: 09              ADD     HL,BC               
7EB1: 9A              SBC     D                   
7EB2: 49              LD      C,C                 
7EB3: 16 97           LD      D,$97               
7EB5: 54              LD      D,H                 
7EB6: 9B              SBC     E                   
7EB7: 5D              LD      E,L                 
7EB8: 12              LD      (DE),A              
7EB9: 28 0E           JR      Z,$7EC9             ; {}
7EBB: 26 13           LD      H,$13               
7EBD: 0D              DEC     C                   
7EBE: 05              DEC     B                   
7EBF: 1A              LD      A,(DE)              
7EC0: 14              INC     D                   
7EC1: 15              DEC     D                   
7EC2: 20 C2           JR      NZ,$7E86            ; {}
7EC4: 0D              DEC     C                   
7EC5: 1C              INC     E                   
7EC6: 04              INC     B                   
7EC7: 13              INC     DE                  
7EC8: 33              INC     SP                  
7EC9: D1              POP     DE                  
7ECA: 09              ADD     HL,BC               
7ECB: 15              DEC     D                   
7ECC: E6 96           AND     $96                 
7ECE: 51              LD      D,C                 
7ECF: 18 4E           JR      $7F1F               ; {}
7ED1: C2 98 5F        JP      NZ,$5F98            ; {}
7ED4: 56              LD      D,(HL)              
7ED5: 5E              LD      E,(HL)              
7ED6: DB 72           IN      A,($72)             
7ED8: 81              ADD     A,C                 
7ED9: A6              AND     (HL)                
7EDA: 52              LD      D,D                 
7EDB: 11 04 04        LD      DE,$0404            
7EDE: 49              LD      C,C                 
7EDF: 48              LD      C,B                 
7EE0: 7F              LD      A,A                 
7EE1: 98              SBC     B                   
7EE2: 09              ADD     HL,BC               
7EE3: 57              LD      D,A                 
7EE4: 0E 55           LD      C,$55               
7EE6: 14              INC     D                   
7EE7: 1B              DEC     DE                  
7EE8: 14              INC     D                   
7EE9: 0E 03           LD      C,$03               
7EEB: 09              ADD     HL,BC               
7EEC: 37              SCF                         
7EED: 8F              ADC     A,A                 
7EEE: 0E 3E           LD      C,$3E               
7EF0: 0D              DEC     C                   
7EF1: 17              RLA                         
7EF2: 14              INC     D                   
7EF3: 15              DEC     D                   
7EF4: 40              LD      B,B                 
7EF5: 04              INC     B                   
7EF6: 0A              LD      A,(BC)              
7EF7: C7              RST     0X00                
7EF8: DE D3           SBC     $D3                 
7EFA: 14              INC     D                   
7EFB: E6 96           AND     $96                 
7EFD: AF              XOR     A                   
7EFE: 15              DEC     D                   
7EFF: B3              OR      E                   
7F00: B3              OR      E                   
7F01: A8              XOR     B                   
7F02: 04              INC     B                   
7F03: 03              INC     BC                  
7F04: 56              LD      D,(HL)              
7F05: D1              POP     DE                  
7F06: 48              LD      C,B                 
7F07: A9              XOR     C                   
7F08: 8B              ADC     A,E                 
7F09: 13              INC     DE                  
7F0A: 0D              DEC     C                   
7F0B: 22 1A 14        LD      ($141A),HL          
7F0E: 15              DEC     D                   
7F0F: 10 04           DJNZ    $7F15               ; {}
7F11: 13              INC     DE                  
7F12: 73              LD      (HL),E              
7F13: 7B              LD      A,E                 
7F14: 77              LD      (HL),A              
7F15: 5B              LD      E,E                 
7F16: D0              RET     NC                  
7F17: B5              OR      L                   
7F18: C9              RET                         
7F19: 9C              SBC     H                   
7F1A: 36 A0           LD      (HL),$A0            
7F1C: 89              ADC     A,C                 
7F1D: 17              RLA                         
7F1E: AF              XOR     A                   
7F1F: 14              INC     D                   
7F20: 73              LD      (HL),E              
7F21: 49              LD      C,C                 
7F22: 03              INC     BC                  
7F23: A0              AND     B                   
7F24: 41              LD      B,C                 
7F25: 11 04 04        LD      DE,$0404            
7F28: 56              LD      D,(HL)              
7F29: D1              POP     DE                  
7F2A: 03              INC     BC                  
7F2B: 71              LD      (HL),C              
7F2C: 12              LD      (DE),A              
7F2D: 8B              ADC     A,E                 
7F2E: 0D              DEC     C                   
7F2F: 0B              DEC     BC                  
7F30: A8              XOR     B                   
7F31: 04              INC     B                   
7F32: 08              EX      AF,AF'              
7F33: 4B              LD      C,E                 
7F34: 7B              LD      A,E                 
7F35: 92              SUB     D                   
7F36: C5              PUSH    BC                  
7F37: 37              SCF                         
7F38: 49              LD      C,C                 
7F39: 17              RLA                         
7F3A: 60              LD      H,B                 
7F3B: 0A              LD      A,(BC)              
7F3C: 01 07 15        LD      BC,$1507            
7F3F: 26 0E           LD      H,$0E               
7F41: 24              INC     H                   
7F42: 13              INC     DE                  
7F43: 0D              DEC     C                   
7F44: 21 04 0A        LD      HL,$0A04            
7F47: 80              ADD     A,B                 
7F48: 5B              LD      E,E                 
7F49: F3              DI                          
7F4A: 23              INC     HL                  
7F4B: 5B              LD      E,E                 
7F4C: 4D              LD      C,L                 
7F4D: 4E              LD      C,(HL)              
7F4E: B8              CP      B                   
7F4F: F9              LD      SP,HL               
7F50: 8E              ADC     A,(HL)              
7F51: A8              XOR     B                   
7F52: 04              INC     B                   
7F53: 12              LD      (DE),A              
7F54: 47              LD      B,A                 
7F55: D2 C8 8B        JP      NC,$8BC8            ; {}
7F58: F3              DI                          
7F59: 23              INC     HL                  
7F5A: 55              LD      D,L                 
7F5B: BD              CP      L                   
7F5C: DB BD           IN      A,($BD)             
7F5E: 41              LD      B,C                 
7F5F: 6E              LD      L,(HL)              
7F60: 03              INC     BC                  
7F61: 58              LD      E,B                 
7F62: 99              SBC     C                   
7F63: 9B              SBC     E                   
7F64: 5F              LD      E,A                 
7F65: 4A              LD      C,D                 
7F66: 59              LD      E,C                 
7F67: 13              INC     DE                  
7F68: 0E 11           LD      C,$11               
7F6A: 13              INC     DE                  
7F6B: 0D              DEC     C                   
7F6C: 0E 04           LD      C,$04               
7F6E: 0B              DEC     BC                  
7F6F: 73              LD      (HL),E              
7F70: 7B              LD      A,E                 
7F71: 55              LD      D,L                 
7F72: BD              CP      L                   
7F73: F5              PUSH    AF                  
7F74: BD              CP      L                   
7F75: 43              LD      B,E                 
7F76: 16 9B           LD      D,$9B               
7F78: 85              ADD     A,L                 
7F79: 41              LD      B,C                 
7F7A: 11 17 4C        LD      DE,$4C17            
7F7D: 0E 4A           LD      C,$4A               
7F7F: 13              INC     DE                  
7F80: 0D              DEC     C                   
7F81: 22 1A 15        LD      ($151A),HL          
7F84: 10 04           DJNZ    $7F8A               ; {}
7F86: 09              ADD     HL,BC               
7F87: 46              LD      B,(HL)              
7F88: 77              LD      (HL),A              
7F89: 05              DEC     B                   
7F8A: A0              AND     B                   
7F8B: 16 BC           LD      D,$BC               
7F8D: 90              SUB     B                   
7F8E: 73              LD      (HL),E              
7F8F: 4B              LD      C,E                 
7F90: A8              XOR     B                   
7F91: 04              INC     B                   
7F92: 11 4E D1        LD      DE,$D14E            
7F95: 15              DEC     D                   
7F96: 8A              ADC     A,D                 
7F97: 50              LD      D,B                 
7F98: BD              CP      L                   
7F99: 15              DEC     D                   
7F9A: 58              LD      E,B                 
7F9B: 8E              ADC     A,(HL)              
7F9C: BE              CP      (HL)                
7F9D: 08              EX      AF,AF'              
7F9E: 8A              ADC     A,D                 
7F9F: BE              CP      (HL)                
7FA0: A0              AND     B                   
7FA1: 56              LD      D,(HL)              
7FA2: 72              LD      (HL),D              
7FA3: 2E 0D           LD      L,$0D               
7FA5: 23              INC     HL                  
7FA6: 04              INC     B                   
7FA7: 10 CF           DJNZ    $7F78               ; {}
7FA9: 62              LD      H,D                 
7FAA: 8B              ADC     A,E                 
7FAB: 96              SUB     (HL)                
7FAC: 9B              SBC     E                   
7FAD: 64              LD      H,H                 
7FAE: 1B              DEC     DE                  
7FAF: A1              AND     C                   
7FB0: 47              LD      B,A                 
7FB1: 55              LD      D,L                 
7FB2: B3              OR      E                   
7FB3: 8B              ADC     A,E                 
7FB4: C3 54 A3        JP      $A354               ; {}
7FB7: 91              SUB     C                   
7FB8: A8              XOR     B                   
7FB9: 04              INC     B                   
7FBA: 0E 73           LD      C,$73               
7FBC: 7B              LD      A,E                 
7FBD: 47              LD      B,A                 
7FBE: D2 C8 8B        JP      NC,$8BC8            ; {}
7FC1: F3              DI                          
7FC2: 23              INC     HL                  
7FC3: EE 72           XOR     $72                 
7FC5: 1B              DEC     DE                  
7FC6: A3              AND     E                   
7FC7: 3F              CCF                         
7FC8: A1              AND     C                   
7FC9: 16 12           LD      D,$12               
7FCB: 0E 10           LD      C,$10               
7FCD: 13              INC     DE                  
7FCE: 0D              DEC     C                   
7FCF: 0D              DEC     C                   
7FD0: A8              XOR     B                   
7FD1: 04              INC     B                   
7FD2: 0A              LD      A,(BC)              
7FD3: 4B              LD      C,E                 
7FD4: 7B              LD      A,E                 
7FD5: 06 9A           LD      B,$9A               
7FD7: BF              CP      A                   
7FD8: 14              INC     D                   
7FD9: D3 B2           OUT     ($B2),A             
7FDB: CF              RST     0X08                
7FDC: 98              SBC     B                   
7FDD: 18 2E           JR      $800D               ; {}
7FDF: 0E 2C           LD      C,$2C               
7FE1: 13              INC     DE                  
7FE2: 0D              DEC     C                   
7FE3: 15              DEC     D                   
7FE4: 1A              LD      A,(DE)              
7FE5: 15              DEC     D                   
7FE6: 10 04           DJNZ    $7FEC               ; {}
7FE8: 0E 5B           LD      C,$5B               
7FEA: BE              CP      (HL)                
7FEB: 65              LD      H,L                 
7FEC: BC              CP      H                   
7FED: 99              SBC     C                   
7FEE: 16 F3           LD      D,$F3               
7FF0: 17              RLA                         
7FF1: 56              LD      D,(HL)              
7FF2: DB CA           IN      A,($CA)             
7FF4: 9C              SBC     H                   
7FF5: 3E C6           LD      A,$C6               
7FF7: AA              XOR     D                   
7FF8: 8B              ADC     A,E                 
7FF9: 0D              DEC     C                   
7FFA: 12              LD      (DE),A              
7FFB: A8              XOR     B                   
7FFC: 04              INC     B                   
7FFD: 0F              RRCA                        
7FFE: 81              ADD     A,C                 
7FFF: 8D              ADC     A,L                 
8000: CB 87           RES     0,A                 
8002: A5              AND     L                   
8003: 94              SUB     H                   
8004: 04              INC     B                   
8005: 71              LD      (HL),C              
8006: 8E              ADC     A,(HL)              
8007: 62              LD      H,D                 
8008: 23              INC     HL                  
8009: 62              LD      H,D                 
800A: 09              ADD     HL,BC               
800B: 9A              SBC     D                   
800C: 2E 0B           LD      L,$0B               
800E: 65              LD      H,L                 
800F: 0E 63           LD      C,$63               
8011: 13              INC     DE                  
8012: 0D              DEC     C                   
8013: 17              RLA                         
8014: 1A              LD      A,(DE)              
8015: 15              DEC     D                   
8016: 04              INC     B                   
8017: 04              INC     B                   
8018: 10 3F           DJNZ    $8059               ; {}
801A: B9              CP      C                   
801B: 82              ADD     A,D                 
801C: 62              LD      H,D                 
801D: 91              SUB     C                   
801E: 7A              LD      A,D                 
801F: D5              PUSH    DE                  
8020: 15              DEC     D                   
8021: 04              INC     B                   
8022: 18 8E           JR      $7FB2               ; {}
8024: 7B              LD      A,E                 
8025: 83              ADD     A,E                 
8026: 61              LD      H,C                 
8027: 03              INC     BC                  
8028: A0              AND     B                   
8029: AA              XOR     D                   
802A: 8B              ADC     A,E                 
802B: 0D              DEC     C                   
802C: 0D              DEC     C                   
802D: 2E 20           LD      L,$20               
802F: 04              INC     B                   
8030: 09              ADD     HL,BC               
8031: 73              LD      (HL),E              
8032: 7B              LD      A,E                 
8033: 4B              LD      C,E                 
8034: 7B              LD      A,E                 
8035: C9              RET                         
8036: 54              LD      D,H                 
8037: A6              AND     (HL)                
8038: B7              OR      A                   
8039: 2E 0D           LD      L,$0D               
803B: 0D              DEC     C                   
803C: 2E 40           LD      L,$40               
803E: 04              INC     B                   
803F: 09              ADD     HL,BC               
8040: 73              LD      (HL),E              
8041: 7B              LD      A,E                 
8042: 4B              LD      C,E                 
8043: 7B              LD      A,E                 
8044: 75              LD      (HL),L              
8045: 8D              ADC     A,L                 
8046: A6              AND     (HL)                
8047: 85              ADD     A,L                 
8048: 2E 0D           LD      L,$0D               
804A: 0A              LD      A,(BC)              
804B: 15              DEC     D                   
804C: 02              LD      (BC),A              
804D: 0E 05           LD      C,$05               
804F: 2E 80           LD      L,$80               
8051: 14              INC     D                   
8052: 2E 20           LD      L,$20               
8054: 33              INC     SP                  
8055: 0D              DEC     C                   
8056: 03              INC     BC                  
8057: 15              DEC     D                   
8058: 01 33 0D        LD      BC,$0D33            
805B: 18 04           JR      $8061               ; {}
805D: 14              INC     D                   
805E: 5F              LD      E,A                 
805F: BE              CP      (HL)                
8060: 5D              LD      E,L                 
8061: B1              OR      C                   
8062: D0              RET     NC                  
8063: B5              OR      L                   
8064: 02              LD      (BC),A              
8065: A1              AND     C                   
8066: 91              SUB     C                   
8067: 7A              LD      A,D                 
8068: 62              LD      H,D                 
8069: 17              RLA                         
806A: DB 5F           IN      A,($5F)             
806C: 33              INC     SP                  
806D: 48              LD      C,B                 
806E: B9              CP      C                   
806F: 46              LD      B,(HL)              
8070: 73              LD      (HL),E              
8071: C6 A8           ADD     $A8                 
8073: 8B              ADC     A,E                 
8074: 0C              INC     C                   
8075: 17              RLA                         
8076: 0E 15           LD      C,$15               
8078: 13              INC     DE                  
8079: 0D              DEC     C                   
807A: 12              LD      (DE),A              
807B: 04              INC     B                   
807C: 0E 5F           LD      C,$5F               
807E: BE              CP      (HL)                
807F: 5D              LD      E,L                 
8080: B1              OR      C                   
8081: D0              RET     NC                  
8082: B5              OR      L                   
8083: 02              LD      (BC),A              
8084: A1              AND     C                   
8085: 91              SUB     C                   
8086: 7A              LD      A,D                 
8087: B0              OR      B                   
8088: 17              RLA                         
8089: F4 59 A8        CALL    P,$A859             ; {}
808C: 8B              ADC     A,E                 
808D: 10 4C           DJNZ    $80DB               ; {}
808F: 0E 4A           LD      C,$4A               
8091: 13              INC     DE                  
8092: 0D              DEC     C                   
8093: 2A 1B 14        LD      HL,($141B)          
8096: 15              DEC     D                   
8097: 02              LD      (BC),A              
8098: 04              INC     B                   
8099: 22 40 55        LD      ($5540),HL          
809C: B0              OR      B                   
809D: 53              LD      D,E                 
809E: EB              EX      DE,HL               
809F: BF              CP      A                   
80A0: DB BD           IN      A,($BD)             
80A2: 4B              LD      C,E                 
80A3: 49              LD      C,C                 
80A4: C7              RST     0X00                
80A5: DE 63           SBC     $63                 
80A7: 16 B3           LD      D,$B3               
80A9: E0              RET     PO                  
80AA: C7              RST     0X00                
80AB: DE D3           SBC     $D3                 
80AD: 14              INC     D                   
80AE: 90              SUB     B                   
80AF: 96              SUB     (HL)                
80B0: F3              DI                          
80B1: A0              AND     B                   
80B2: A7              AND     A                   
80B3: B7              OR      A                   
80B4: 90              SUB     B                   
80B5: 14              INC     D                   
80B6: 82              ADD     A,D                 
80B7: DF              RST     0X18                
80B8: 91              SUB     C                   
80B9: 7A              LD      A,D                 
80BA: D0              RET     NC                  
80BB: 15              DEC     D                   
80BC: A9              XOR     C                   
80BD: 8B              ADC     A,E                 
80BE: 0D              DEC     C                   
80BF: 0F              RRCA                        
80C0: 14              INC     D                   
80C1: 2E 80           LD      L,$80               
80C3: 2E 20           LD      L,$20               
80C5: A9              XOR     C                   
80C6: 04              INC     B                   
80C7: 07              RLCA                        
80C8: 4B              LD      C,E                 
80C9: 7B              LD      A,E                 
80CA: C9              RET                         
80CB: 54              LD      D,H                 
80CC: A6              AND     (HL)                
80CD: B7              OR      A                   
80CE: 2E 33           LD      L,$33               
80D0: 0D              DEC     C                   
80D1: 09              ADD     HL,BC               
80D2: A9              XOR     C                   
80D3: 04              INC     B                   
80D4: 06 4B           LD      B,$4B               
80D6: 7B              LD      A,E                 
80D7: 72              LD      (HL),D              
80D8: 61              LD      H,C                 
80D9: 1F              RRA                         
80DA: C1              POP     BC                  
80DB: 4C              LD      C,H                 
80DC: 51              LD      D,C                 
80DD: 0E 4F           LD      C,$4F               
80DF: 13              INC     DE                  
80E0: 0D              DEC     C                   
80E1: 1A              LD      A,(DE)              
80E2: 1B              DEC     DE                  
80E3: 15              DEC     D                   
80E4: 04              INC     B                   
80E5: 04              INC     B                   
80E6: 13              INC     DE                  
80E7: 5F              LD      E,A                 
80E8: BE              CP      (HL)                
80E9: 5D              LD      E,L                 
80EA: B1              OR      C                   
80EB: D5              PUSH    DE                  
80EC: B5              OR      L                   
80ED: E7              RST     0X20                
80EE: 9F              SBC     A                   
80EF: 63              LD      H,E                 
80F0: BE              CP      (HL)                
80F1: AB              XOR     E                   
80F2: 98              SBC     B                   
80F3: B3              OR      E                   
80F4: D2 3F C0        JP      NC,$C03F            
80F7: 91              SUB     C                   
80F8: 96              SUB     (HL)                
80F9: 4E              LD      C,(HL)              
80FA: A9              XOR     C                   
80FB: 8B              ADC     A,E                 
80FC: 0D              DEC     C                   
80FD: 1D              DEC     E                   
80FE: 14              INC     D                   
80FF: 15              DEC     D                   
8100: 01 04 16        LD      BC,$1604            
8103: 5F              LD      E,A                 
8104: BE              CP      (HL)                
8105: 5D              LD      E,L                 
8106: B1              OR      C                   
8107: D0              RET     NC                  
8108: B5              OR      L                   
8109: 02              LD      (BC),A              
810A: A1              AND     C                   
810B: 91              SUB     C                   
810C: 7A              LD      A,D                 
810D: 99              SBC     C                   
810E: 16 F9           LD      D,$F9               
8110: BD              CP      L                   
8111: BE              CP      (HL)                
8112: A0              AND     B                   
8113: FB              EI                          
8114: 75              LD      (HL),L              
8115: B9              CP      C                   
8116: 46              LD      B,(HL)              
8117: 73              LD      (HL),E              
8118: C6 A9           ADD     $A9                 
811A: 8B              ADC     A,E                 
811B: 33              INC     SP                  
811C: 0D              DEC     C                   
811D: 10 04           DJNZ    $8123               ; {}
811F: 0C              INC     C                   
8120: 5F              LD      E,A                 
8121: BE              CP      (HL)                
8122: 5D              LD      E,L                 
8123: B1              OR      C                   
8124: D0              RET     NC                  
8125: B5              OR      L                   
8126: 02              LD      (BC),A              
8127: A1              AND     C                   
8128: 91              SUB     C                   
8129: 7A              LD      A,D                 
812A: C0              RET     NZ                  
812B: 16 A9           LD      D,$A9               
812D: 8B              ADC     A,E                 
812E: 1B              DEC     DE                  
812F: 1E 0E           LD      E,$0E               
8131: 1C              INC     E                   
8132: 13              INC     DE                  
8133: 0D              DEC     C                   
8134: 03              INC     BC                  
8135: 08              EX      AF,AF'              
8136: 00              NOP                         
8137: 07              RLCA                        
8138: 0D              DEC     C                   
8139: 14              INC     D                   
813A: 04              INC     B                   
813B: 10 5F           DJNZ    $819C               ; {}
813D: BE              CP      (HL)                
813E: 5B              LD      E,E                 
813F: B1              OR      C                   
8140: 4B              LD      C,E                 
8141: 7B              LD      A,E                 
8142: 06 9A           LD      B,$9A               
8144: 90              SUB     B                   
8145: 73              LD      (HL),E              
8146: C3 6A 07        JP      $076A               
8149: B3              OR      E                   
814A: 33              INC     SP                  
814B: 98              SBC     B                   
814C: A8              XOR     B                   
814D: 8B              ADC     A,E                 
814E: 1C              INC     E                   
814F: 32 0E 30        LD      ($300E),A           
8152: 13              INC     DE                  
8153: 0D              DEC     C                   
8154: 17              RLA                         
8155: 08              EX      AF,AF'              
8156: 00              NOP                         
8157: 04              INC     B                   
8158: 13              INC     DE                  
8159: 5F              LD      E,A                 
815A: BE              CP      (HL)                
815B: 5B              LD      E,E                 
815C: B1              OR      C                   
815D: 4B              LD      C,E                 
815E: 7B              LD      A,E                 
815F: 06 9A           LD      B,$9A               
8161: 90              SUB     B                   
8162: 73              LD      (HL),E              
8163: C4 6A A3        CALL    NZ,$A36A            ; {}
8166: 60              LD      H,B                 
8167: 33              INC     SP                  
8168: 98              SBC     B                   
8169: C7              RST     0X00                
816A: DE 2E           SBC     $2E                 
816C: 0D              DEC     C                   
816D: 14              INC     D                   
816E: 04              INC     B                   
816F: 10 5F           DJNZ    $81D0               ; {}
8171: BE              CP      (HL)                
8172: 5B              LD      E,E                 
8173: B1              OR      C                   
8174: 4B              LD      C,E                 
8175: 7B              LD      A,E                 
8176: 06 9A           LD      B,$9A               
8178: 90              SUB     B                   
8179: 73              LD      (HL),E              
817A: C4 6A A3        CALL    NZ,$A36A            ; {}
817D: 60              LD      H,B                 
817E: 33              INC     SP                  
817F: 98              SBC     B                   
8180: A8              XOR     B                   
8181: 8B              ADC     A,E                 
8182: 1D              DEC     E                   
8183: 16 04           LD      D,$04               
8185: 14              INC     D                   
8186: 9F              SBC     A                   
8187: 77              LD      (HL),A              
8188: AF              XOR     A                   
8189: 14              INC     D                   
818A: 91              SUB     C                   
818B: 7A              LD      A,D                 
818C: 95              SUB     L                   
818D: 14              INC     D                   
818E: D3 14           OUT     ($14),A             
8190: 68              LD      L,B                 
8191: B1              OR      C                   
8192: 33              INC     SP                  
8193: C5              PUSH    BC                  
8194: 4B              LD      C,E                 
8195: 49              LD      C,C                 
8196: 45              LD      B,L                 
8197: 77              LD      (HL),A              
8198: 81              ADD     A,C                 
8199: 48              LD      C,B                 
819A: 1E 04           LD      E,$04               
819C: 04              INC     B                   
819D: 02              LD      (BC),A              
819E: E9              JP      (HL)                
819F: 99              SBC     C                   
81A0: 1F              RRA                         
81A1: 05              DEC     B                   
81A2: 04              INC     B                   
81A3: 03              INC     BC                  
81A4: 35              DEC     (HL)                
81A5: DD 21 21 1C     LD      IX,$1C21            
81A9: 04              INC     B                   
81AA: 1A              LD      A,(DE)              
81AB: 44              LD      B,H                 
81AC: B9              CP      C                   
81AD: 9E              SBC     (HL)                
81AE: B4              OR      H                   
81AF: BB              CP      E                   
81B0: 15              DEC     D                   
81B1: 80              ADD     A,B                 
81B2: 5B              LD      E,E                 
81B3: F3              DI                          
81B4: 23              INC     HL                  
81B5: 6E              LD      L,(HL)              
81B6: 4D              LD      C,L                 
81B7: 38 79           JR      C,$8232             ; {}
81B9: 4B              LD      C,E                 
81BA: 5E              LD      E,(HL)              
81BB: 8F              ADC     A,A                 
81BC: 96              SUB     (HL)                
81BD: 7B              LD      A,E                 
81BE: 47              LD      B,A                 
81BF: D9              EXX                         
81C0: 51              LD      D,C                 
81C1: AE              XOR     (HL)                
81C2: A0              AND     B                   
81C3: 5B              LD      E,E                 
81C4: BB              CP      E                   
81C5: 5A              LD      E,D                 
81C6: 1B              DEC     DE                  
81C7: 04              INC     B                   
81C8: 19              ADD     HL,DE               
81C9: 25              DEC     H                   
81CA: A1              AND     C                   
81CB: AB              XOR     E                   
81CC: 70              LD      (HL),B              
81CD: 56              LD      D,(HL)              
81CE: 77              LD      (HL),A              
81CF: BE              CP      (HL)                
81D0: 9F              SBC     A                   
81D1: 51              LD      D,C                 
81D2: 18 B3           JR      $8187               ; {}
81D4: C7              RST     0X00                
81D5: 5B              LD      E,E                 
81D6: BE              CP      (HL)                
81D7: 0B              DEC     BC                  
81D8: C0              RET     NZ                  
81D9: 06 9A           LD      B,$9A               
81DB: E9              JP      (HL)                
81DC: 16 DB           LD      D,$DB               
81DE: B9              CP      C                   
81DF: 7F              LD      A,A                 
81E0: 4E              LD      C,(HL)              
81E1: 21 22 12        LD      HL,$1222            
81E4: 04              INC     B                   
81E5: 10 5B           DJNZ    $8242               ; {}
81E7: E0              RET     PO                  
81E8: 27              DAA                         
81E9: 60              LD      H,B                 
81EA: 31 60 41        LD      SP,$4160            
81ED: A0              AND     B                   
81EE: 49              LD      C,C                 
81EF: A0              AND     B                   
81F0: 89              ADC     A,C                 
81F1: D3 89           OUT     ($89),A             
81F3: D3 69           OUT     ($69),A             
81F5: CE 23           ADC     $23                 
81F7: 01 24 2C        LD      BC,$2C24            
81FA: 01 C9 3E        LD      BC,$3EC9            
81FD: 04              INC     B                   
81FE: 0D              DEC     C                   
81FF: 02              LD      (BC),A              
8200: C6 27           ADD     $27                 
8202: 3F              CCF                         
8203: 04              INC     B                   
8204: 0D              DEC     C                   
8205: 02              LD      (BC),A              
8206: C6 28           ADD     $28                 
8208: 25              DEC     H                   
8209: 20 04           JR      NZ,$820F            ; {}
820B: 1E C7           LD      E,$C7               
820D: DE AF           SBC     $AF                 
820F: 23              INC     HL                  
8210: 99              SBC     C                   
8211: 16 09           LD      D,$09               
8213: BC              CP      H                   
8214: 8E              ADC     A,(HL)              
8215: 62              LD      H,D                 
8216: 91              SUB     C                   
8217: 7A              LD      A,D                 
8218: 90              SUB     B                   
8219: 14              INC     D                   
821A: FA DF 2F        JP      M,$2FDF             
821D: 62              LD      H,D                 
821E: 16 EE           LD      D,$EE               
8220: 7B              LD      A,E                 
8221: B4              OR      H                   
8222: 46              LD      B,(HL)              
8223: 45              LD      B,L                 
8224: 2F              CPL                         
8225: 7B              LD      A,E                 
8226: 03              INC     BC                  
8227: 56              LD      D,(HL)              
8228: 27              DAA                         
8229: A0              AND     B                   
822A: 26 20           LD      H,$20               
822C: 0E 1E           LD      C,$1E               
822E: 13              INC     DE                  
822F: 0D              DEC     C                   
8230: 13              INC     DE                  
8231: 1A              LD      A,(DE)              
8232: 15              DEC     D                   
8233: 10 A8           DJNZ    $81DD               ; {}
8235: 04              INC     B                   
8236: 0D              DEC     C                   
8237: 40              LD      B,B                 
8238: D2 F3 23        JP      NC,$23F3            
823B: F6 8B           OR      $8B                 
823D: 51              LD      D,C                 
823E: 18 52           JR      $8292               ; {}
8240: C2 65 49        JP      NZ,$4965            
8243: 21 04 06        LD      HL,$0604            
8246: 09              ADD     HL,BC               
8247: 9A              SBC     D                   
8248: FA 17 70        JP      M,$7017             ; {}
824B: 49              LD      C,C                 
824C: 3D              DEC     A                   
824D: 01 91 27        LD      BC,$2791            
8250: 0E 0E           LD      C,$0E               
8252: 0C              INC     C                   
8253: 13              INC     DE                  
8254: 04              INC     B                   
8255: 09              ADD     HL,BC               
8256: 25              DEC     H                   
8257: A1              AND     C                   
8258: AB              XOR     E                   
8259: 70              LD      (HL),B              
825A: 3B              DEC     SP                  
825B: 95              SUB     L                   
825C: 77              LD      (HL),A              
825D: BF              CP      A                   
825E: 21 44 09        LD      HL,$0944            
8261: 04              INC     B                   
8262: 07              RLCA                        
8263: AF              XOR     A                   
8264: 6E              LD      L,(HL)              
8265: 83              ADD     A,E                 
8266: 62              LD      H,D                 
8267: C5              PUSH    BC                  
8268: 98              SBC     B                   
8269: 21 45 30        LD      HL,$3045            
826C: 0E 2E           LD      C,$2E               
826E: 13              INC     DE                  
826F: 0D              DEC     C                   
8270: 12              LD      (DE),A              
8271: 1A              LD      A,(DE)              
8272: 15              DEC     D                   
8273: 10 A8           DJNZ    $821D               ; {}
8275: 04              INC     B                   
8276: 0C              INC     C                   
8277: 72              LD      (HL),D              
8278: B1              OR      C                   
8279: 87              ADD     A,A                 
827A: 8C              ADC     A,H                 
827B: 33              INC     SP                  
827C: BB              CP      E                   
827D: DF              RST     0X18                
827E: 1B              DEC     DE                  
827F: 09              ADD     HL,BC               
8280: 8D              ADC     A,L                 
8281: 63              LD      H,E                 
8282: F4 0D 17        CALL    P,$170D             
8285: 04              INC     B                   
8286: 13              INC     DE                  
8287: 16 A0           LD      D,$A0               
8289: 43              LD      B,E                 
828A: DB E4           IN      A,($E4)             
828C: 14              INC     D                   
828D: 83              ADD     A,E                 
828E: 4A              LD      C,D                 
828F: 01 18 3E        LD      BC,$3E18            
8292: C5              PUSH    BC                  
8293: 7B              LD      A,E                 
8294: 17              RLA                         
8295: CB 8C           RES     1,H                 
8297: 6B              LD      L,E                 
8298: BF              CP      A                   
8299: 41              LD      B,C                 
829A: 11 8B 46        LD      DE,$468B            
829D: 08              EX      AF,AF'              
829E: 04              INC     B                   
829F: 06 46           LD      B,$46               
82A1: 77              LD      (HL),A              
82A2: 98              SBC     B                   
82A3: C5              PUSH    BC                  
82A4: 5B              LD      E,E                 
82A5: A2              AND     D                   
82A6: 47              LD      B,A                 
82A7: 09              ADD     HL,BC               
82A8: 04              INC     B                   
82A9: 07              RLCA                        
82AA: 29              ADD     HL,HL               
82AB: D1              POP     DE                  
82AC: 20 16           JR      NZ,$82C4            ; {}
82AE: 85              ADD     A,L                 
82AF: A1              AND     C                   
82B0: 3F              CCF                         
82B1: 4A              LD      C,D                 
82B2: 18 0E           JR      $82C2               ; {}
82B4: 16 13           LD      D,$13               
82B6: 0D              DEC     C                   
82B7: 13              INC     DE                  
82B8: 04              INC     B                   
82B9: 11 9E 77        LD      DE,$779E            
82BC: 08              EX      AF,AF'              
82BD: 8A              ADC     A,D                 
82BE: C6 9F           ADD     $9F                 
82C0: 6B              LD      L,E                 
82C1: A1              AND     C                   
82C2: C7              RST     0X00                
82C3: DE 90           SBC     $90                 
82C5: 14              INC     D                   
82C6: FA DF 2F        JP      M,$2FDF             
82C9: 62              LD      H,D                 
82CA: 21 49 26        LD      HL,$2649            
82CD: 0E 24           LD      C,$24               
82CF: 13              INC     DE                  
82D0: 0D              DEC     C                   
82D1: 11 09 00        LD      DE,$0009            
82D4: A8              XOR     B                   
82D5: 04              INC     B                   
82D6: 0C              INC     C                   
82D7: 09              ADD     HL,BC               
82D8: 4F              LD      C,A                 
82D9: CB B5           RES     6,L                 
82DB: 89              ADC     A,C                 
82DC: 96              SUB     (HL)                
82DD: 67              LD      H,A                 
82DE: B1              OR      C                   
82DF: 90              SUB     B                   
82E0: BE              CP      (HL)                
82E1: 5B              LD      E,E                 
82E2: 70              LD      (HL),B              
82E3: 04              INC     B                   
82E4: 0E 5F           LD      C,$5F               
82E6: BE              CP      (HL)                
82E7: 44              LD      B,H                 
82E8: DB 6B           IN      A,($6B)             
82EA: A1              AND     C                   
82EB: 83              ADD     A,E                 
82EC: 7A              LD      A,D                 
82ED: AF              XOR     A                   
82EE: 6E              LD      L,(HL)              
82EF: 83              ADD     A,E                 
82F0: 62              LD      H,D                 
82F1: CF              RST     0X08                
82F2: 98              SBC     B                   
82F3: 28 36           JR      Z,$832B             ; {}
82F5: 0E 34           LD      C,$34               
82F7: 13              INC     DE                  
82F8: 0D              DEC     C                   
82F9: 16 1A           LD      D,$1A               
82FB: 15              DEC     D                   
82FC: 10 A8           DJNZ    $82A6               ; {}
82FE: 04              INC     B                   
82FF: 10 60           DJNZ    $8361               ; {}
8301: 7B              LD      A,E                 
8302: F3              DI                          
8303: 23              INC     HL                  
8304: 70              LD      (HL),B              
8305: 75              LD      (HL),L              
8306: C3 6E 33        JP      $336E               
8309: 17              RLA                         
830A: 2E 6D           LD      L,$6D               
830C: 99              SBC     C                   
830D: 16 5B           LD      D,$5B               
830F: D4 0D 19        CALL    NC,$190D            
8312: 04              INC     B                   
8313: 0D              DEC     C                   
8314: 80              ADD     A,B                 
8315: 5B              LD      E,E                 
8316: F3              DI                          
8317: 23              INC     HL                  
8318: C7              RST     0X00                
8319: DE 20           SBC     $20                 
831B: 16 6B           LD      D,$6B               
831D: A1              AND     C                   
831E: 5B              LD      E,E                 
831F: BE              CP      (HL)                
8320: 54              LD      D,H                 
8321: A8              XOR     B                   
8322: 04              INC     B                   
8323: 07              RLCA                        
8324: 10 53           DJNZ    $8379               ; {}
8326: F3              DI                          
8327: 23              INC     HL                  
8328: 96              SUB     (HL)                
8329: 5F              LD      E,A                 
832A: 21 29 34        LD      HL,$3429            
832D: 0E 32           LD      C,$32               
832F: 13              INC     DE                  
8330: 0D              DEC     C                   
8331: 14              INC     D                   
8332: 1B              DEC     DE                  
8333: 15              DEC     D                   
8334: 10 A9           DJNZ    $82DF               ; {}
8336: 04              INC     B                   
8337: 0E 47           LD      C,$47               
8339: D2 B3 8B        JP      NC,$8BB3            ; {}
833C: D6 B0           SUB     $B0                 
833E: F4 72 23        CALL    P,$2372             
8341: 15              DEC     D                   
8342: 1B              DEC     DE                  
8343: BC              CP      H                   
8344: 19              ADD     HL,DE               
8345: A1              AND     C                   
8346: 0D              DEC     C                   
8347: 19              ADD     HL,DE               
8348: 04              INC     B                   
8349: 17              RLA                         
834A: 43              LD      B,E                 
834B: 79              LD      A,C                 
834C: C7              RST     0X00                
834D: DE D3           SBC     $D3                 
834F: 14              INC     D                   
8350: 88              ADC     A,B                 
8351: 96              SUB     (HL)                
8352: 8E              ADC     A,(HL)              
8353: 7A              LD      A,D                 
8354: 7B              LD      A,E                 
8355: 14              INC     D                   
8356: C7              RST     0X00                
8357: 93              SUB     E                   
8358: 76              HALT                        
8359: BE              CP      (HL)                
835A: BD              CP      L                   
835B: 15              DEC     D                   
835C: 49              LD      C,C                 
835D: 90              SUB     B                   
835E: 67              LD      H,A                 
835F: 48              LD      C,B                 
8360: 21 2F 07        LD      HL,$072F            
8363: 04              INC     B                   
8364: 05              DEC     B                   
8365: 9B              SBC     E                   
8366: 29              ADD     HL,HL               
8367: 57              LD      D,A                 
8368: C6 3E           ADD     $3E                 
836A: 31 17 04        LD      SP,$0417            
836D: 15              DEC     D                   
836E: 36 9F           LD      (HL),$9F            
8370: D6 15           SUB     $15                 
8372: CB 23           SLA     E                   
8374: 39              ADD     HL,SP               
8375: 49              LD      C,C                 
8376: 8E              ADC     A,(HL)              
8377: C5              PUSH    BC                  
8378: 9F              SBC     A                   
8379: 15              DEC     D                   
837A: 5B              LD      E,E                 
837B: B1              OR      C                   
837C: 3F              CCF                         
837D: B9              CP      C                   
837E: FA 62 2F        JP      M,$2F62             
8381: 62              LD      H,D                 
8382: 2E 2D           LD      L,$2D               
8384: 09              ADD     HL,BC               
8385: 0E 07           LD      C,$07               
8387: 13              INC     DE                  
8388: 0D              DEC     C                   
8389: 02              LD      (BC),A              
838A: 1A              LD      A,(DE)              
838B: 8F              ADC     A,A                 
838C: 14              INC     D                   
838D: 0C              INC     C                   
838E: 48              LD      C,B                 
838F: 11 0E 0F        LD      DE,$0F0E            
8392: 13              INC     DE                  
8393: 04              INC     B                   
8394: 0C              INC     C                   
8395: C7              RST     0X00                
8396: DE D3           SBC     $D3                 
8398: 14              INC     D                   
8399: E6 96           AND     $96                 
839B: 09              ADD     HL,BC               
839C: 15              DEC     D                   
839D: 82              ADD     A,D                 
839E: 17              RLA                         
839F: 97              SUB     A                   
83A0: 49              LD      C,C                 
83A1: 33              INC     SP                  
83A2: 27              DAA                         
83A3: 0E 25           LD      C,$25               
83A5: 13              INC     DE                  
83A6: 04              INC     B                   
83A7: 22 0F A0        LD      ($A00F),HL          ; {}
83AA: 5F              LD      E,A                 
83AB: 17              RLA                         
83AC: 46              LD      B,(HL)              
83AD: 48              LD      C,B                 
83AE: 66              LD      H,(HL)              
83AF: 17              RLA                         
83B0: D3 61           OUT     ($61),A             
83B2: 04              INC     B                   
83B3: 68              LD      L,B                 
83B4: 63              LD      H,E                 
83B5: 16 5B           LD      D,$5B               
83B7: 99              SBC     C                   
83B8: 56              LD      D,(HL)              
83B9: 98              SBC     B                   
83BA: C0              RET     NZ                  
83BB: 16 49           LD      D,$49               
83BD: 5E              LD      E,(HL)              
83BE: 90              SUB     B                   
83BF: 78              LD      A,B                 
83C0: 0E BC           LD      C,$BC               
83C2: 92              SUB     D                   
83C3: 5F              LD      E,A                 
83C4: 59              LD      E,C                 
83C5: 15              DEC     D                   
83C6: 9B              SBC     E                   
83C7: AF              XOR     A                   
83C8: 19              ADD     HL,DE               
83C9: A1              AND     C                   
83CA: 34              INC     (HL)                
83CB: 23              INC     HL                  
83CC: 0E 21           LD      C,$21               
83CE: 13              INC     DE                  
83CF: 04              INC     B                   
83D0: 1E C7           LD      E,$C7               
83D2: DE 95           SBC     $95                 
83D4: AF              XOR     A                   
83D5: D5              PUSH    DE                  
83D6: C3 65 62        JP      $6265               ; {}
83D9: D5              PUSH    DE                  
83DA: 15              DEC     D                   
83DB: 67              LD      H,A                 
83DC: 16 67           LD      D,$67               
83DE: 49              LD      C,C                 
83DF: 66              LD      H,(HL)              
83E0: B1              OR      C                   
83E1: D0              RET     NC                  
83E2: 15              DEC     D                   
83E3: 3F              CCF                         
83E4: 16 ED           LD      D,$ED               
83E6: 48              LD      C,B                 
83E7: 90              SUB     B                   
83E8: 14              INC     D                   
83E9: 04              INC     B                   
83EA: 58              LD      E,B                 
83EB: 30 A1           JR      NC,$838E            ; {}
83ED: 09              ADD     HL,BC               
83EE: 5C              LD      E,H                 
83EF: 35              DEC     (HL)                
83F0: 1C              INC     E                   
83F1: 0E 1A           LD      C,$1A               
83F3: 13              INC     DE                  
83F4: 04              INC     B                   
83F5: 17              RLA                         
83F6: C7              RST     0X00                
83F7: DE 73           SBC     $73                 
83F9: 21 76 4D        LD      HL,$4D76            
83FC: F4 BD F3        CALL    P,$F3BD             
83FF: 17              RLA                         
8400: 9A              SBC     D                   
8401: BD              CP      L                   
8402: FA 17 2F        JP      M,$2F17             
8405: 62              LD      H,D                 
8406: 51              LD      D,C                 
8407: 18 55           JR      $845E               ; {}
8409: C2 F2 BD        JP      NZ,$BDF2            
840C: 21 36 04        LD      HL,$0436            
840F: 0E 02           LD      C,$02               
8411: 13              INC     DE                  
8412: 91              SUB     C                   
8413: 37              SCF                         
8414: 04              INC     B                   
8415: 0E 02           LD      C,$02               
8417: 13              INC     DE                  
8418: 91              SUB     C                   
8419: 54              LD      D,H                 
841A: 17              RLA                         
841B: 0E 15           LD      C,$15               
841D: 13              INC     DE                  
841E: 04              INC     B                   
841F: 12              LD      (DE),A              
8420: 5F              LD      E,A                 
8421: BE              CP      (HL)                
8422: 5B              LD      E,E                 
8423: B1              OR      C                   
8424: 4B              LD      C,E                 
8425: 7B              LD      A,E                 
8426: EB              EX      DE,HL               
8427: 99              SBC     C                   
8428: FB              EI                          
8429: A5              AND     L                   
842A: 9B              SBC     E                   
842B: 53              LD      D,E                 
842C: 6B              LD      L,E                 
842D: BF              CP      A                   
842E: 2B              DEC     HL                  
842F: 6E              LD      L,(HL)              
8430: F7              RST     0X30                
8431: C5              PUSH    BC                  
8432: 55              LD      D,L                 
8433: 19              ADD     HL,DE               
8434: 0E 17           LD      C,$17               
8436: 13              INC     DE                  
8437: 04              INC     B                   
8438: 14              INC     D                   
8439: 5F              LD      E,A                 
843A: BE              CP      (HL)                
843B: 5B              LD      E,E                 
843C: B1              OR      C                   
843D: 4B              LD      C,E                 
843E: 7B              LD      A,E                 
843F: EB              EX      DE,HL               
8440: 99              SBC     C                   
8441: FB              EI                          
8442: A5              AND     L                   
8443: 9B              SBC     E                   
8444: 53              LD      D,E                 
8445: 6B              LD      L,E                 
8446: BF              CP      A                   
8447: 2B              DEC     HL                  
8448: 6E              LD      L,(HL)              
8449: 89              ADC     A,C                 
844A: 5B              LD      E,E                 
844B: 1B              DEC     DE                  
844C: 9C              SBC     H                   
844D: 38 1D           JR      C,$846C             ; {}
844F: 0E 1B           LD      C,$1B               
8451: 13              INC     DE                  
8452: 0D              DEC     C                   
8453: 18 04           JR      $8459               ; {}
8455: 14              INC     D                   
8456: 5F              LD      E,A                 
8457: BE              CP      (HL)                
8458: 5B              LD      E,E                 
8459: B1              OR      C                   
845A: 4B              LD      C,E                 
845B: 7B              LD      A,E                 
845C: 06 9A           LD      B,$9A               
845E: 30 15           JR      NC,$8475            ; {}
8460: 29              ADD     HL,HL               
8461: A1              AND     C                   
8462: 14              INC     D                   
8463: 71              LD      (HL),C              
8464: 3F              CCF                         
8465: A0              AND     B                   
8466: B0              OR      B                   
8467: 17              RLA                         
8468: F4 59 A8        CALL    P,$A859             ; {}
846B: 8B              ADC     A,E                 
846C: 39              ADD     HL,SP               
846D: 1D              DEC     E                   
846E: 0E 1B           LD      C,$1B               
8470: 13              INC     DE                  
8471: 0D              DEC     C                   
8472: 18 04           JR      $8478               ; {}
8474: 16 C7           LD      D,$C7               
8476: DE FB           SBC     $FB                 
8478: 17              RLA                         
8479: F3              DI                          
847A: 8C              ADC     A,H                 
847B: 58              LD      E,B                 
847C: 72              LD      (HL),D              
847D: 56              LD      D,(HL)              
847E: 5E              LD      E,(HL)              
847F: D2 9C 73        JP      NC,$739C            ; {}
8482: C6 73           ADD     $73                 
8484: 7B              LD      A,E                 
8485: 83              ADD     A,E                 
8486: 7A              LD      A,D                 
8487: 5F              LD      E,A                 
8488: BE              CP      (HL)                
8489: 7F              LD      A,A                 
848A: B1              OR      C                   
848B: 0D              DEC     C                   
848C: 2B              DEC     HL                  
848D: 0E 29           LD      C,$29               
848F: 0D              DEC     C                   
8490: 25              DEC     H                   
8491: 1A              LD      A,(DE)              
8492: 8F              ADC     A,A                 
8493: 0E 21           LD      C,$21               
8495: 13              INC     DE                  
8496: 0D              DEC     C                   
8497: 1E 0E           LD      E,$0E               
8499: 07              RLCA                        
849A: 14              INC     D                   
849B: 15              DEC     D                   
849C: 10 1B           DJNZ    $84B9               ; {}
849E: 14              INC     D                   
849F: 15              DEC     D                   
84A0: 40              LD      B,B                 
84A1: A8              XOR     B                   
84A2: 04              INC     B                   
84A3: 0F              RRCA                        
84A4: 07              RLCA                        
84A5: 4F              LD      C,A                 
84A6: 17              RLA                         
84A7: 98              SBC     B                   
84A8: CA B5 37        JP      Z,$37B5             
84AB: 49              LD      C,C                 
84AC: F5              PUSH    AF                  
84AD: 8B              ADC     A,E                 
84AE: D3 B8           OUT     ($B8),A             
84B0: B8              CP      B                   
84B1: 16 46           LD      D,$46               
84B3: A9              XOR     C                   
84B4: 8B              ADC     A,E                 
84B5: 10 14           DJNZ    $84CB               ; {}
84B7: 0C              INC     C                   
84B8: 57              LD      D,A                 
84B9: 81              ADD     A,C                 
84BA: 09              ADD     HL,BC               
84BB: 0E 81           LD      C,$81               
84BD: 06 13           LD      B,$13               
84BF: 0D              DEC     C                   
84C0: 0F              RRCA                        
84C1: 14              INC     D                   
84C2: 09              ADD     HL,BC               
84C3: 28 A9           JR      Z,$846E             ; {}
84C5: 04              INC     B                   
84C6: 09              ADD     HL,BC               
84C7: 60              LD      H,B                 
84C8: 7B              LD      A,E                 
84C9: F3              DI                          
84CA: 23              INC     HL                  
84CB: 73              LD      (HL),E              
84CC: 8D              ADC     A,L                 
84CD: E6 59           AND     $59                 
84CF: 2E 0D           LD      L,$0D               
84D1: 0A              LD      A,(BC)              
84D2: 14              INC     D                   
84D3: 03              INC     BC                  
84D4: 28 29           JR      Z,$84FF             ; {}
84D6: 04              INC     B                   
84D7: 04              INC     B                   
84D8: C3 54 AF        JP      $AF54               ; {}
84DB: 54              LD      D,H                 
84DC: 0D              DEC     C                   
84DD: 80              ADD     A,B                 
84DE: CB 04           RLC     H                   
84E0: 04              INC     B                   
84E1: 7B              LD      A,E                 
84E2: 4E              LD      C,(HL)              
84E3: EB              EX      DE,HL               
84E4: 8F              ADC     A,A                 
84E5: 0B              DEC     BC                  
84E6: 80              ADD     A,B                 
84E7: C2 08 33        JP      NZ,$3308            
84EA: 0E 0D           LD      C,$0D               
84EC: 0C              INC     C                   
84ED: 04              INC     B                   
84EE: 07              RLCA                        
84EF: 41              LD      B,C                 
84F0: 6E              LD      L,(HL)              
84F1: 15              DEC     D                   
84F2: 58              LD      E,B                 
84F3: 86              ADD     A,(HL)              
84F4: 74              LD      (HL),H              
84F5: 21 1A 1D        LD      HL,$1D1A            
84F8: 64              LD      H,H                 
84F9: 62              LD      H,D                 
84FA: 4D              LD      C,L                 
84FB: 0D              DEC     C                   
84FC: 4B              LD      C,E                 
84FD: 04              INC     B                   
84FE: 45              LD      B,L                 
84FF: 5F              LD      E,A                 
8500: BE              CP      (HL)                
8501: 8E              ADC     A,(HL)              
8502: 14              INC     D                   
8503: 30 79           JR      NC,$857E            ; {}
8505: D5              PUSH    DE                  
8506: 15              DEC     D                   
8507: 43              LD      B,E                 
8508: 16 BF           LD      D,$BF               
850A: 68              LD      L,B                 
850B: 03              INC     BC                  
850C: 58              LD      E,B                 
850D: 33              INC     SP                  
850E: 98              SBC     B                   
850F: 6C              LD      L,H                 
8510: BE              CP      (HL)                
8511: 80              ADD     A,B                 
8512: A1              AND     C                   
8513: AB              XOR     E                   
8514: 14              INC     D                   
8515: A9              XOR     C                   
8516: 54              LD      D,H                 
8517: 2E 49           LD      L,$49               
8519: C4 B5 56        CALL    NZ,$56B5            
851C: DB DB           IN      A,($DB)             
851E: 72              LD      (HL),D              
851F: 72              LD      (HL),D              
8520: 7A              LD      A,D                 
8521: E6 46           AND     $46                 
8523: B8              CP      B                   
8524: 16 82           LD      D,$82               
8526: 17              RLA                         
8527: 44              LD      B,H                 
8528: 5E              LD      E,(HL)              
8529: 55              LD      D,L                 
852A: 8B              ADC     A,E                 
852B: 9B              SBC     E                   
852C: C1              POP     BC                  
852D: 8D              ADC     A,L                 
852E: 7B              LD      A,E                 
852F: 43              LD      B,E                 
8530: 16 D3           LD      D,$D3               
8532: 93              SUB     E                   
8533: F6 4E           OR      $4E                 
8535: 48              LD      C,B                 
8536: DB 46           IN      A,($46)             
8538: 48              LD      C,B                 
8539: D6 B5           SUB     $B5                 
853B: D6 9C           SUB     $9C                 
853D: DB 72           IN      A,($72)             
853F: B9              CP      C                   
8540: 6E              LD      L,(HL)              
8541: 8E              ADC     A,(HL)              
8542: C5              PUSH    BC                  
8543: 2E 1C           LD      L,$1C               
8545: 62              LD      H,D                 
8546: 1D              DEC     E                   
8547: 15              DEC     D                   
8548: 89              ADC     A,C                 
8549: 60              LD      H,B                 
854A: 0D              DEC     C                   
854B: 5E              LD      E,(HL)              
854C: 04              INC     B                   
854D: 58              LD      E,B                 
854E: 5F              LD      E,A                 
854F: BE              CP      (HL)                
8550: 5A              LD      E,D                 
8551: 17              RLA                         
8552: 01 A1 83        LD      BC,$83A1            
8555: C5              PUSH    BC                  
8556: F3              DI                          
8557: B2              OR      D                   
8558: 8B              ADC     A,E                 
8559: B3              OR      E                   
855A: E3              EX      (SP),HL             
855B: 59              LD      E,C                 
855C: 70              LD      (HL),B              
855D: 66              LD      H,(HL)              
855E: 91              SUB     C                   
855F: 7A              LD      A,D                 
8560: 1E 8F           LD      E,$8F               
8562: BF              CP      A                   
8563: 14              INC     D                   
8564: 0A              LD      A,(BC)              
8565: BC              CP      H                   
8566: 4B              LD      C,E                 
8567: 49              LD      C,C                 
8568: 96              SUB     (HL)                
8569: 8C              ADC     A,H                 
856A: FF              RST     0X38                
856B: BE              CP      (HL)                
856C: 28 15           JR      Z,$8583             ; {}
856E: 65              LD      H,L                 
856F: 66              LD      H,(HL)              
8570: 11 BC 96        LD      DE,$96BC            
8573: 96              SUB     (HL)                
8574: DB 72           IN      A,($72)             
8576: 18 D0           JR      $8548               ; {}
8578: 51              LD      D,C                 
8579: 5E              LD      E,(HL)              
857A: 95              SUB     L                   
857B: 64              LD      H,H                 
857C: 8E              ADC     A,(HL)              
857D: 91              SUB     C                   
857E: 04              INC     B                   
857F: 8A              ADC     A,D                 
8580: 45              LD      B,L                 
8581: 8B              ADC     A,E                 
8582: C5              PUSH    BC                  
8583: 83              ADD     A,E                 
8584: 63              LD      H,E                 
8585: B1              OR      C                   
8586: 74              LD      (HL),H              
8587: C0              RET     NZ                  
8588: 4B              LD      C,E                 
8589: 62              LD      H,D                 
858A: 5B              LD      E,E                 
858B: BE              CP      (HL)                
858C: 19              ADD     HL,DE               
858D: BC              CP      H                   
858E: 5A              LD      E,D                 
858F: 49              LD      C,C                 
8590: C8              RET     Z                   
8591: 16 23           LD      D,$23               
8593: 62              LD      H,D                 
8594: C7              RST     0X00                
8595: DE 15           SBC     $15                 
8597: EE 90           XOR     $90                 
8599: BE              CP      (HL)                
859A: 50              LD      D,B                 
859B: 6D              LD      L,L                 
859C: DB 6A           IN      A,($6A)             
859E: 1B              DEC     DE                  
859F: A1              AND     C                   
85A0: 6B              LD      L,E                 
85A1: BF              CP      A                   
85A2: E3              EX      (SP),HL             
85A3: 59              LD      E,C                 
85A4: 77              LD      (HL),A              
85A5: BE              CP      (HL)                
85A6: 1C              INC     E                   
85A7: 01 1D 4B        LD      BC,$4B1D            
85AA: 0D              DEC     C                   
85AB: 18 04           JR      $85B1               ; {}
85AD: 14              INC     D                   
85AE: 5F              LD      E,A                 
85AF: BE              CP      (HL)                
85B0: 5B              LD      E,E                 
85B1: B1              OR      C                   
85B2: 2F              CPL                         
85B3: 49              LD      C,C                 
85B4: 57              LD      D,A                 
85B5: 17              RLA                         
85B6: 74              LD      (HL),H              
85B7: CA 33 48        JP      Z,$4833             
85BA: 79              LD      A,C                 
85BB: 98              SBC     B                   
85BC: A9              XOR     C                   
85BD: 15              DEC     D                   
85BE: F5              PUSH    AF                  
85BF: 8B              ADC     A,E                 
85C0: D0              RET     NC                  
85C1: 15              DEC     D                   
85C2: A8              XOR     B                   
85C3: 8B              ADC     A,E                 
85C4: 0E 13           LD      C,$13               
85C6: 0E 11           LD      C,$11               
85C8: 13              INC     DE                  
85C9: 0D              DEC     C                   
85CA: 0E A9           LD      C,$A9               
85CC: 04              INC     B                   
85CD: 0B              DEC     BC                  
85CE: 77              LD      (HL),A              
85CF: 5B              LD      E,E                 
85D0: 05              DEC     B                   
85D1: B9              CP      C                   
85D2: 19              ADD     HL,DE               
85D3: BC              CP      H                   
85D4: 9E              SBC     (HL)                
85D5: 48              LD      C,B                 
85D6: D6 15           SUB     $15                 
85D8: 2E 0F           LD      L,$0F               
85DA: 1D              DEC     E                   
85DB: 0E 1B           LD      C,$1B               
85DD: 0D              DEC     C                   
85DE: 06 1A           LD      B,$1A               
85E0: 14              INC     D                   
85E1: 2E 10           LD      L,$10               
85E3: 14              INC     D                   
85E4: 8F              ADC     A,A                 
85E5: 14              INC     D                   
85E6: BF              CP      A                   
85E7: 0D              DEC     C                   
85E8: 05              DEC     B                   
85E9: 1B              DEC     DE                  
85EA: 14              INC     D                   
85EB: 15              DEC     D                   
85EC: 02              LD      (BC),A              
85ED: B6              OR      (HL)                
85EE: B7              OR      A                   
85EF: 0D              DEC     C                   
85F0: 04              INC     B                   
85F1: 1B              DEC     DE                  
85F2: 32 B5 0C        LD      ($0CB5),A           
85F5: 13              INC     DE                  
85F6: 14              INC     D                   
85F7: 0C              INC     C                   
85F8: 4D              LD      C,L                 
85F9: 23              INC     HL                  
85FA: 0E 21           LD      C,$21               
85FC: 0D              DEC     C                   
85FD: 05              DEC     B                   
85FE: 1B              DEC     DE                  
85FF: 14              INC     D                   
8600: 2E 10           LD      L,$10               
8602: B8              CP      B                   
8603: 14              INC     D                   
8604: BF              CP      A                   
8605: 0D              DEC     C                   
8606: 05              DEC     B                   
8607: 1A              LD      A,(DE)              
8608: 14              INC     D                   
8609: 15              DEC     D                   
860A: 02              LD      (BC),A              
860B: B6              OR      (HL)                
860C: B7              OR      A                   
860D: 0D              DEC     C                   
860E: 05              DEC     B                   
860F: 1B              DEC     DE                  
8610: 14              INC     D                   
8611: 2E 10           LD      L,$10               
8613: B8              CP      B                   
8614: 0D              DEC     C                   
8615: 04              INC     B                   
8616: 1A              LD      A,(DE)              
8617: 31 B5 0C        LD      SP,$0CB5            
861A: 13              INC     DE                  
861B: 14              INC     D                   
861C: 0C              INC     C                   
861D: 4E              LD      C,(HL)              
861E: 3F              CCF                         
861F: 0E 3D           LD      C,$3D               
8621: 0D              DEC     C                   
8622: 0A              LD      A,(BC)              
8623: 1A              LD      A,(DE)              
8624: 14              INC     D                   
8625: 2E 10           LD      L,$10               
8627: 04              INC     B                   
8628: 03              INC     BC                  
8629: 81              ADD     A,C                 
862A: A6              AND     (HL)                
862B: 52              LD      D,D                 
862C: 11 14 BF        LD      DE,$BF14            
862F: 0D              DEC     C                   
8630: 10 09           DJNZ    $863B               ; {}
8632: 00              NOP                         
8633: 1C              INC     E                   
8634: 00              NOP                         
8635: 32 A8 04        LD      ($04A8),A           
8638: 08              EX      AF,AF'              
8639: 4B              LD      C,E                 
863A: 7B              LD      A,E                 
863B: 09              ADD     HL,BC               
863C: 9A              SBC     D                   
863D: 81              ADD     A,C                 
863E: 15              DEC     D                   
863F: 7F              LD      A,A                 
8640: 98              SBC     B                   
8641: 0D              DEC     C                   
8642: 12              LD      (DE),A              
8643: 1B              DEC     DE                  
8644: 14              INC     D                   
8645: 15              DEC     D                   
8646: 02              LD      (BC),A              
8647: A9              XOR     C                   
8648: 04              INC     B                   
8649: 08              EX      AF,AF'              
864A: 4B              LD      C,E                 
864B: 7B              LD      A,E                 
864C: 09              ADD     HL,BC               
864D: 9A              SBC     D                   
864E: FB              EI                          
864F: 14              INC     D                   
8650: F7              RST     0X30                
8651: 93              SUB     E                   
8652: 1C              INC     E                   
8653: 00              NOP                         
8654: 32 0D 04        LD      ($040D),A           
8657: 1B              DEC     DE                  
8658: 32 B5 0C        LD      ($0CB5),A           
865B: 13              INC     DE                  
865C: 14              INC     D                   
865D: 0C              INC     C                   
865E: 4F              LD      C,A                 
865F: 52              LD      D,D                 
8660: 0E 50           LD      C,$50               
8662: 0D              DEC     C                   
8663: 32 1A 14        LD      ($141A),A           
8666: 2E 10           LD      L,$10               
8668: 04              INC     B                   
8669: 2A C7 DE        LD      HL,($DEC7)          
866C: AF              XOR     A                   
866D: 23              INC     HL                  
866E: 5B              LD      E,E                 
866F: 17              RLA                         
8670: AE              XOR     (HL)                
8671: 54              LD      D,H                 
8672: BF              CP      A                   
8673: 14              INC     D                   
8674: 10 BC           DJNZ    $8632               ; {}
8676: F3              DI                          
8677: A0              AND     B                   
8678: 4E              LD      C,(HL)              
8679: 72              LD      (HL),D              
867A: 83              ADD     A,E                 
867B: 64              LD      H,H                 
867C: D5              PUSH    DE                  
867D: B5              OR      L                   
867E: DD ; ????
867F: 78              LD      A,B                 
8680: 95              SUB     L                   
8681: 14              INC     D                   
8682: 51              LD      D,C                 
8683: 18 59           JR      $86DE               ; {}
8685: C2 2E A1        JP      NZ,$A12E            ; {}
8688: 04              INC     B                   
8689: 58              LD      E,B                 
868A: 4B              LD      C,E                 
868B: 5E              LD      E,(HL)              
868C: 9B              SBC     E                   
868D: 64              LD      H,H                 
868E: 1B              DEC     DE                  
868F: A1              AND     C                   
8690: EB              EX      DE,HL               
8691: 5B              LD      E,E                 
8692: 4B              LD      C,E                 
8693: 99              SBC     C                   
8694: A8              XOR     B                   
8695: 8B              ADC     A,E                 
8696: 14              INC     D                   
8697: BF              CP      A                   
8698: 0D              DEC     C                   
8699: 04              INC     B                   
869A: 13              INC     DE                  
869B: 1C              INC     E                   
869C: 00              NOP                         
869D: 32 0D 12        LD      ($120D),A           
86A0: 1C              INC     E                   
86A1: 00              NOP                         
86A2: 32 04 0D        LD      ($0D04),A           
86A5: C7              RST     0X00                
86A6: DE 4F           SBC     $4F                 
86A8: 15              DEC     D                   
86A9: 33              INC     SP                  
86AA: 61              LD      H,C                 
86AB: 68              LD      L,B                 
86AC: B1              OR      C                   
86AD: 75              LD      (HL),L              
86AE: B1              OR      C                   
86AF: E6 72           AND     $72                 
86B1: 2E 4B           LD      L,$4B               
86B3: 43              LD      B,E                 
86B4: 0E 41           LD      C,$41               
86B6: 13              INC     DE                  
86B7: 0D              DEC     C                   
86B8: 06 1A           LD      B,$1A               
86BA: 14              INC     D                   
86BB: 2E 10           LD      L,$10               
86BD: 14              INC     D                   
86BE: 8F              ADC     A,A                 
86BF: 0D              DEC     C                   
86C0: 16 2E           LD      D,$2E               
86C2: 10 0E           DJNZ    $86D2               ; {}
86C4: 12              LD      (DE),A              
86C5: 14              INC     D                   
86C6: BF              CP      A                   
86C7: 0D              DEC     C                   
86C8: 0E A9           LD      C,$A9               
86CA: 04              INC     B                   
86CB: 08              EX      AF,AF'              
86CC: 4B              LD      C,E                 
86CD: 7B              LD      A,E                 
86CE: 09              ADD     HL,BC               
86CF: 9A              SBC     D                   
86D0: F7              RST     0X30                
86D1: 17              RLA                         
86D2: 9B              SBC     E                   
86D3: C1              POP     BC                  
86D4: 1C              INC     E                   
86D5: 00              NOP                         
86D6: 32 0D 16        LD      ($160D),A           
86D9: 1B              DEC     DE                  
86DA: 14              INC     D                   
86DB: 15              DEC     D                   
86DC: 01 04 10        LD      BC,$1004            
86DF: 5F              LD      E,A                 
86E0: BE              CP      (HL)                
86E1: 5D              LD      E,L                 
86E2: B1              OR      C                   
86E3: D0              RET     NC                  
86E4: B5              OR      L                   
86E5: F3              DI                          
86E6: A0              AND     B                   
86E7: 99              SBC     C                   
86E8: 61              LD      H,C                 
86E9: 7A              LD      A,D                 
86EA: C4 39 17        CALL    NZ,$1739            
86ED: FF              RST     0X38                
86EE: 9F              SBC     A                   
86EF: 0D              DEC     C                   
86F0: 04              INC     B                   
86F1: 1B              DEC     DE                  
86F2: 32 B5 0C        LD      ($0CB5),A           
86F5: 14              INC     D                   
86F6: 0C              INC     C                   
86F7: 19              ADD     HL,DE               
86F8: 80              ADD     A,B                 
86F9: EB              EX      DE,HL               
86FA: 0D              DEC     C                   
86FB: 80              ADD     A,B                 
86FC: E8              RET     PE                  
86FD: 1C              INC     E                   
86FE: 01 0B 80        LD      BC,$800B            
8701: E3              EX      (SP),HL             
8702: 22 05 24        LD      ($2405),HL          
8705: 04              INC     B                   
8706: 22 C7 DE        LD      ($DEC7),HL          
8709: 94              SUB     H                   
870A: 14              INC     D                   
870B: 51              LD      D,C                 
870C: 5E              LD      E,(HL)              
870D: 9B              SBC     E                   
870E: 96              SUB     (HL)                
870F: 34              INC     (HL)                
8710: A1              AND     C                   
8711: 3B              DEC     SP                  
8712: 16 F3           LD      D,$F3               
8714: B9              CP      C                   
8715: E9              JP      (HL)                
8716: 8B              ADC     A,E                 
8717: 5B              LD      E,E                 
8718: BB              CP      E                   
8719: A3              AND     E                   
871A: 48              LD      C,B                 
871B: 63              LD      H,E                 
871C: BE              CP      (HL)                
871D: AB              XOR     E                   
871E: 98              SBC     B                   
871F: 47              LD      B,A                 
8720: 55              LD      D,L                 
8721: B3              OR      E                   
8722: 8B              ADC     A,E                 
8723: 4E              LD      C,(HL)              
8724: 86              ADD     A,(HL)              
8725: 1B              DEC     DE                  
8726: 8A              ADC     A,D                 
8727: 19              ADD     HL,DE               
8728: A1              AND     C                   
8729: 14              INC     D                   
872A: 1C              INC     E                   
872B: 04              INC     B                   
872C: 1A              LD      A,(DE)              
872D: 0F              RRCA                        
872E: A0              AND     B                   
872F: 71              LD      (HL),C              
8730: 16 5B           LD      D,$5B               
8732: B1              OR      C                   
8733: 41              LD      B,C                 
8734: 6E              LD      L,(HL)              
8735: 0B              DEC     BC                  
8736: 58              LD      E,B                 
8737: 3F              CCF                         
8738: 99              SBC     C                   
8739: 7B              LD      A,E                 
873A: B4              OR      H                   
873B: 8E              ADC     A,(HL)              
873C: 48              LD      C,B                 
873D: 51              LD      D,C                 
873E: 18 A8           JR      $86E8               ; {}
8740: C2 4A 5E        JP      NZ,$5E4A            ; {}
8743: F3              DI                          
8744: 46              LD      B,(HL)              
8745: 71              LD      (HL),C              
8746: 7B              LD      A,E                 
8747: 23              INC     HL                  
8748: 22 04 20        LD      ($2004),HL          
874B: C7              RST     0X00                
874C: DE 94           SBC     $94                 
874E: 14              INC     D                   
874F: 48              LD      C,B                 
8750: 5E              LD      E,(HL)              
8751: 2E 60           LD      L,$60               
8753: 91              SUB     C                   
8754: 7A              LD      A,D                 
8755: 17              RLA                         
8756: 17              RLA                         
8757: 7F              LD      A,A                 
8758: 7B              LD      A,E                 
8759: CE 15           ADC     $15                 
875B: 9B              SBC     E                   
875C: 8F              ADC     A,A                 
875D: 52              LD      D,D                 
875E: 77              LD      (HL),A              
875F: 75              LD      (HL),L              
8760: B1              OR      C                   
8761: B3              OR      E                   
8762: 55              LD      D,L                 
8763: 5B              LD      E,E                 
8764: 4D              LD      C,L                 
8765: 17              RLA                         
8766: 53              LD      D,E                 
8767: 91              SUB     C                   
8768: BE              CP      (HL)                
8769: 2B              DEC     HL                  
876A: 96              SUB     (HL)                
876B: 33              INC     SP                  
876C: 32 04 30        LD      ($3004),A           
876F: C7              RST     0X00                
8770: DE 94           SBC     $94                 
8772: 14              INC     D                   
8773: 50              LD      D,B                 
8774: 5E              LD      E,(HL)              
8775: F3              DI                          
8776: A0              AND     B                   
8777: 67              LD      H,A                 
8778: 66              LD      H,(HL)              
8779: 90              SUB     B                   
877A: 8C              ADC     A,H                 
877B: D7              RST     0X10                
877C: 6A              LD      L,D                 
877D: 16 A3           LD      D,$A3               
877F: D2 9C 47        JP      NC,$479C            
8782: 49              LD      C,C                 
8783: 51              LD      D,C                 
8784: 18 55           JR      $87DB               ; {}
8786: C2 87 74        JP      NZ,$7487            ; {}
8789: B3              OR      E                   
878A: 8B              ADC     A,E                 
878B: 4D              LD      C,L                 
878C: BD              CP      L                   
878D: 44              LD      B,H                 
878E: 5E              LD      E,(HL)              
878F: 8E              ADC     A,(HL)              
8790: 62              LD      H,D                 
8791: 23              INC     HL                  
8792: 62              LD      H,D                 
8793: 14              INC     D                   
8794: 53              LD      D,E                 
8795: 51              LD      D,C                 
8796: 5E              LD      E,(HL)              
8797: 9B              SBC     E                   
8798: 64              LD      H,H                 
8799: 34              INC     (HL)                
879A: A1              AND     C                   
879B: AE              XOR     (HL)                
879C: B7              OR      A                   
879D: 1B              DEC     DE                  
879E: 6A              LD      L,D                 
879F: 44              LD      B,H                 
87A0: 24              INC     H                   
87A1: 04              INC     B                   
87A2: 22 C7 DE        LD      ($DEC7),HL          
87A5: AF              XOR     A                   
87A6: 23              INC     HL                  
87A7: 4F              LD      C,A                 
87A8: 15              DEC     D                   
87A9: 43              LD      B,E                 
87AA: 61              LD      H,C                 
87AB: AB              XOR     E                   
87AC: 98              SBC     B                   
87AD: EF              RST     0X28                
87AE: A6              AND     (HL)                
87AF: 53              LD      D,E                 
87B0: C0              RET     NZ                  
87B1: 81              ADD     A,C                 
87B2: 15              DEC     D                   
87B3: 73              LD      (HL),E              
87B4: 9E              SBC     (HL)                
87B5: 8E              ADC     A,(HL)              
87B6: C5              PUSH    BC                  
87B7: 23              INC     HL                  
87B8: 62              LD      H,D                 
87B9: 5F              LD      E,A                 
87BA: BE              CP      (HL)                
87BB: DB 14           IN      A,($14)             
87BD: 27              DAA                         
87BE: B1              OR      C                   
87BF: 66              LD      H,(HL)              
87C0: 94              SUB     H                   
87C1: 8D              ADC     A,L                 
87C2: 48              LD      C,B                 
87C3: 6F              LD      L,A                 
87C4: 62              LD      H,D                 
87C5: FF              RST     0X38                
87C6: 1E 04           LD      E,$04               
87C8: 1C              INC     E                   
87C9: C7              RST     0X00                
87CA: DE 4F           SBC     $4F                 
87CC: 15              DEC     D                   
87CD: 33              INC     SP                  
87CE: 61              LD      H,C                 
87CF: 4B              LD      C,E                 
87D0: 49              LD      C,C                 
87D1: 41              LD      B,C                 
87D2: 6E              LD      L,(HL)              
87D3: 03              INC     BC                  
87D4: 58              LD      E,B                 
87D5: D6 B5           SUB     $B5                 
87D7: DB 72           IN      A,($72)             
87D9: 5B              LD      E,E                 
87DA: 59              LD      E,C                 
87DB: 51              LD      D,C                 
87DC: 18 59           JR      $8837               ; {}
87DE: C2 2F 62        JP      NZ,$622F            ; {}
87E1: B9              CP      C                   
87E2: 14              INC     D                   
87E3: E7              RST     0X20                
87E4: B2              OR      D                   
87E5: 52              LD      D,D                 
87E6: 04              INC     B                   
87E7: 0E 02           LD      C,$02               
87E9: 13              INC     DE                  
87EA: B8              CP      B                   
87EB: 56              LD      D,(HL)              
87EC: 11 0E 0F        LD      DE,$0F0E            
87EF: 13              INC     DE                  
87F0: 04              INC     B                   
87F1: 0C              INC     C                   
87F2: 46              LD      B,(HL)              
87F3: 77              LD      (HL),A              
87F4: 6B              LD      L,E                 
87F5: 79              LD      A,C                 
87F6: 73              LD      (HL),E              
87F7: 7B              LD      A,E                 
87F8: 81              ADD     A,C                 
87F9: BF              CP      A                   
87FA: 0F              RRCA                        
87FB: EE 81           XOR     $81                 
87FD: 48              LD      C,B                 
87FE: 50              LD      D,B                 
87FF: 11 0E 0F        LD      DE,$0F0E            
8802: 13              INC     DE                  
8803: 04              INC     B                   
8804: 0C              INC     C                   
8805: C7              RST     0X00                
8806: DE D3           SBC     $D3                 
8808: 14              INC     D                   
8809: E6 96           AND     $96                 
880B: 09              ADD     HL,BC               
880C: 15              DEC     D                   
880D: 82              ADD     A,D                 
880E: 17              RLA                         
880F: 71              LD      (HL),C              
8810: 49              LD      C,C                 
8811: 51              LD      D,C                 
8812: 2B              DEC     HL                  
8813: 0E 29           LD      C,$29               
8815: 13              INC     DE                  
8816: 04              INC     B                   
8817: 26 68           LD      H,$68               
8819: 4D              LD      C,L                 
881A: AF              XOR     A                   
881B: A0              AND     B                   
881C: 51              LD      D,C                 
881D: 18 45           JR      $8864               ; {}
881F: C2 83 48        JP      NZ,$4883            
8822: 74              LD      (HL),H              
8823: C0              RET     NZ                  
8824: 95              SUB     L                   
8825: 96              SUB     (HL)                
8826: E7              RST     0X20                
8827: 9F              SBC     A                   
8828: 63              LD      H,E                 
8829: BE              CP      (HL)                
882A: AB              XOR     E                   
882B: 98              SBC     B                   
882C: D0              RET     NC                  
882D: 9E              SBC     (HL)                
882E: 0B              DEC     BC                  
882F: EE 0F           XOR     $0F                 
8831: BC              CP      H                   
8832: 66              LD      H,(HL)              
8833: C6 AF           ADD     $AF                 
8835: 14              INC     D                   
8836: 8F              ADC     A,A                 
8837: 17              RLA                         
8838: CF              RST     0X08                
8839: B2              OR      D                   
883A: 11 58 1B        LD      DE,$1B58            
883D: 9C              SBC     H                   
883E: 53              LD      D,E                 
883F: 0F              RRCA                        
8840: 0E 0D           LD      C,$0D               
8842: 13              INC     DE                  
8843: 0D              DEC     C                   
8844: 0A              LD      A,(BC)              
8845: 04              INC     B                   
8846: 08              EX      AF,AF'              
8847: 57              LD      D,A                 
8848: C6 93           ADD     $93                 
884A: 13              INC     DE                  
884B: 3B              DEC     SP                  
884C: C0              RET     NZ                  
884D: 8D              ADC     A,L                 
884E: 54              LD      D,H                 
884F: 58              LD      E,B                 
8850: 0D              DEC     C                   
8851: 0E 0B           LD      C,$0B               
8853: 13              INC     DE                  
8854: 0D              DEC     C                   
8855: 08              EX      AF,AF'              
8856: 04              INC     B                   
8857: 06 55           LD      B,$55               
8859: 77              LD      (HL),A              
885A: 1B              DEC     DE                  
885B: 60              LD      H,B                 
885C: 97              SUB     A                   
885D: 7B              LD      A,E                 
885E: 07              RLCA                        
885F: 1A              LD      A,(DE)              
8860: 0D              DEC     C                   
8861: 18 04           JR      $8867               ; {}
8863: 15              DEC     D                   
8864: C7              RST     0X00                
8865: DE 94           SBC     $94                 
8867: 14              INC     D                   
8868: 45              LD      B,L                 
8869: 5E              LD      E,(HL)              
886A: 3C              INC     A                   
886B: 49              LD      C,C                 
886C: D0              RET     NC                  
886D: DD ; ????
886E: D6 6A           SUB     $6A                 
8870: DB 72           IN      A,($72)             
8872: FE 67           CP      $67                 
8874: 89              ADC     A,C                 
8875: 8D              ADC     A,L                 
8876: 91              SUB     C                   
8877: 7A              LD      A,D                 
8878: 3A 06 

; ?? List of something ??
887A: 00 AB 32 
;
887D: 01 80
887F: 87              ADD     A,A                 
8880: 80              ADD     A,B                 
8881: 01 80 0A        LD      BC,$0A80            
8884: 35              DEC     (HL)                
8885: 0D              DEC     C                   
8886: 33              INC     SP                  
8887: 0E 24           LD      C,$24               
8889: 0D              DEC     C                   
888A: 20 03           JR      NZ,$888F            ; {}
888C: 01 35 1F        LD      BC,$1F35            
888F: 1B              DEC     DE                  
8890: 5F              LD      E,A                 
8891: BE              CP      (HL)                
8892: 60              LD      H,B                 
8893: 17              RLA                         
8894: 17              RLA                         
8895: 48              LD      C,B                 
8896: CF              RST     0X08                
8897: 17              RLA                         
8898: FF              RST     0X38                
8899: 99              SBC     C                   
889A: F3              DI                          
889B: 17              RLA                         
889C: C7              RST     0X00                
889D: B5              OR      L                   
889E: 4C              LD      C,H                 
889F: D9              EXX                         
88A0: 67              LD      H,A                 
88A1: 61              LD      H,C                 
88A2: FB              EI                          
88A3: 8E              ADC     A,(HL)              
88A4: 7B              LD      A,E                 
88A5: A6              AND     (HL)                
88A6: 40              LD      B,B                 
88A7: B9              CP      C                   
88A8: 35              DEC     (HL)                
88A9: A1              AND     C                   
88AA: 21 14 0C        LD      HL,$0C14            
88AD: 1F              RRA                         
88AE: 09              ADD     HL,BC               
88AF: C7              RST     0X00                
88B0: DE 94           SBC     $94                 
88B2: 14              INC     D                   
88B3: 46              LD      B,(HL)              
88B4: 5E              LD      E,(HL)              
88B5: 86              ADD     A,(HL)              
88B6: 5F              LD      E,A                 
88B7: 2E C9           LD      L,$C9               
88B9: 24              INC     H                   
88BA: 08              EX      AF,AF'              
88BB: 43              LD      B,E                 
88BC: 0E 41           LD      C,$41               
88BE: 0D              DEC     C                   
88BF: 1E 03           LD      E,$03               
88C1: 39              ADD     HL,SP               
88C2: 4B              LD      C,E                 
88C3: 14              INC     D                   
88C4: 01 39 0E        LD      BC,$0E39            
88C7: 06 03           LD      B,$03               
88C9: 9C              SBC     H                   
88CA: 01 03 99        LD      BC,$9903            
88CD: 01 0E 06        LD      BC,$060E            
88D0: 03              INC     BC                  
88D1: 9A              SBC     D                   
88D2: 39              ADD     HL,SP               
88D3: 03              INC     BC                  
88D4: 9D              SBC     L                   
88D5: 39              ADD     HL,SP               
88D6: 1F              RRA                         
88D7: 06 01           LD      B,$01               
88D9: 4F              LD      C,A                 
88DA: 41              LD      B,C                 
88DB: A0              AND     B                   
88DC: D9              EXX                         
88DD: 9F              SBC     A                   
88DE: 0D              DEC     C                   
88DF: 1F              RRA                         
88E0: 03              INC     BC                  
88E1: 39              ADD     HL,SP               
88E2: 4B              LD      C,E                 
88E3: 14              INC     D                   
88E4: 01 39 1F        LD      BC,$1F39            
88E7: 17              RLA                         
88E8: 5F              LD      E,A                 
88E9: BE              CP      (HL)                
88EA: 13              INC     DE                  
88EB: 15              DEC     D                   
88EC: CF              RST     0X08                
88ED: 97              SUB     A                   
88EE: 7F              LD      A,A                 
88EF: 7B              LD      A,E                 
88F0: 77              LD      (HL),A              
88F1: 16 F3           LD      D,$F3               
88F3: B9              CP      C                   
88F4: 58              LD      E,B                 
88F5: 72              LD      (HL),D              
88F6: 44              LD      B,H                 
88F7: 5E              LD      E,(HL)              
88F8: 30 60           JR      NC,$895A            ; {}
88FA: 7B              LD      A,E                 
88FB: 14              INC     D                   
88FC: 66              LD      H,(HL)              
88FD: 5C              LD      E,H                 
88FE: 21 02 02        LD      HL,$0202            
8901: C7              RST     0X00                
8902: DE 09           SBC     $09                 
8904: 02              LD      (BC),A              
8905: 46              LD      B,(HL)              
8906: 46              LD      B,(HL)              
8907: 10 08           DJNZ    $8911               ; {}
8909: 83              ADD     A,E                 
890A: 01 88 02        LD      BC,$0288            
890D: 03              INC     BC                  
890E: 81              ADD     A,C                 
890F: 5B              LD      E,E                 
8910: 52              LD      D,D                 
8911: 10 08           DJNZ    $891B               ; {}
8913: 82              ADD     A,D                 
8914: 21 88 02        LD      HL,$0288            
8917: 03              INC     BC                  
8918: 81              ADD     A,C                 
8919: 5B              LD      E,E                 
891A: 52              LD      D,D                 
891B: 10 2E           DJNZ    $894B               ; {}
891D: 88              ADC     A,B                 
891E: 61              LD      H,C                 
891F: 8C              ADC     A,H                 
8920: 07              RLCA                        
8921: 24              INC     H                   
8922: 0E 22           LD      C,$22               
8924: 0D              DEC     C                   
8925: 0A              LD      A,(BC)              
8926: 0E 04           LD      C,$04               
8928: 0A              LD      A,(BC)              
8929: 3A 0A 42        LD      A,($420A)           
892C: 14              INC     D                   
892D: 09              ADD     HL,BC               
892E: 1C              INC     E                   
892F: BA              CP      D                   
8930: 0D              DEC     C                   
8931: 14              INC     D                   
8932: 0A              LD      A,(BC)              
8933: 08              EX      AF,AF'              
8934: 04              INC     B                   
8935: 10 73           DJNZ    $89AA               ; {}
8937: 7B              LD      A,E                 
8938: 4B              LD      C,E                 
8939: 7B              LD      A,E                 
893A: EB              EX      DE,HL               
893B: 99              SBC     C                   
893C: 80              ADD     A,B                 
893D: 8D              ADC     A,L                 
893E: B4              OR      H                   
893F: 6C              LD      L,H                 
8940: 3F              CCF                         
8941: 16 44           LD      D,$44               
8943: 6D              LD      L,L                 
8944: FF              RST     0X38                
8945: 8B              ADC     A,E                 
8946: 02              LD      (BC),A              
8947: 03              INC     BC                  
8948: 81              ADD     A,C                 
8949: 5B              LD      E,E                 
894A: 52              LD      D,D                 
894B: 10 08           DJNZ    $8955               ; {}
894D: DA 01 88        JP      C,$8801             ; {}
8950: 02              LD      (BC),A              
8951: 03              INC     BC                  
8952: 81              ADD     A,C                 
8953: 5B              LD      E,E                 
8954: 52              LD      D,D                 
8955: 10 2C           DJNZ    $8983               ; {}
8957: 8D              ADC     A,L                 
8958: 22 88 03        LD      ($0388),HL          
895B: 19              ADD     HL,DE               
895C: 04              INC     B                   
895D: 17              RLA                         
895E: 7B              LD      A,E                 
895F: BA              CP      D                   
8960: BB              CP      E                   
8961: 98              SBC     B                   
8962: AB              XOR     E                   
8963: 98              SBC     B                   
8964: 81              ADD     A,C                 
8965: 5B              LD      E,E                 
8966: 8B              ADC     A,E                 
8967: B3              OR      E                   
8968: E3              EX      (SP),HL             
8969: 8B              ADC     A,E                 
896A: 16 58           LD      D,$58               
896C: D6 9C           SUB     $9C                 
896E: DB 72           IN      A,($72)             
8970: 0E B7           LD      C,$B7               
8972: 40              LD      B,B                 
8973: A0              AND     B                   
8974: 2E 01           LD      L,$01               
8976: 02              LD      (BC),A              
8977: 41              LD      B,C                 
8978: 46              LD      B,(HL)              
8979: 02              LD      (BC),A              

897A: 08              EX      AF,AF'              
897B: 0E B7           LD      C,$B7               
897D: 40              LD      B,B                 
897E: A0              AND     B                   
897F: 09              ADD     HL,BC               
8980: 15              DEC     D                   
8981: A3              AND     E                   
8982: A0              AND     B                   
8983: 10 08           DJNZ    $898D               ; {}
8985: A2              AND     D                   
8986: 02              LD      (BC),A              
8987: 88              ADC     A,B                 
8988: 02              LD      (BC),A              
8989: 03              INC     BC                  
898A: 81              ADD     A,C                 
898B: 5B              LD      E,E                 
898C: 52              LD      D,D                 
898D: 10 41           DJNZ    $89D0               ; {}
898F: 8D              ADC     A,L                 
8990: 62              LD      H,D                 
8991: 88              ADC     A,B                 
8992: 03              INC     BC                  
8993: 1B              DEC     DE                  
8994: 04              INC     B                   
8995: 19              ADD     HL,DE               
8996: 46              LD      B,(HL)              
8997: 45              LD      B,L                 
8998: 44              LD      B,H                 
8999: A0              AND     B                   
899A: 3F              CCF                         
899B: 16 0D           LD      D,$0D               
899D: 47              LD      B,A                 
899E: 89              ADC     A,C                 
899F: 17              RLA                         
89A0: 82              ADD     A,D                 
89A1: 17              RLA                         
89A2: 55              LD      D,L                 
89A3: 5E              LD      E,(HL)              
89A4: F4 72 50        CALL    P,$5072             
89A7: 79              LD      A,C                 
89A8: CB 23           SLA     E                   
89AA: D0              RET     NC                  
89AB: 9E              SBC     (HL)                
89AC: D7              RST     0X10                
89AD: 78              LD      A,B                 
89AE: 2E 07           LD      L,$07               
89B0: 0C              INC     C                   
89B1: 0D              DEC     C                   
89B2: 0A              LD      A,(BC)              
89B3: 0E 04           LD      C,$04               
89B5: 0A              LD      A,(BC)              
89B6: 3A 0A 42        LD      A,($420A)           
89B9: 14              INC     D                   
89BA: 09              ADD     HL,BC               
89BB: 1B              DEC     DE                  
89BC: BA              CP      D                   
89BD: 01 01 42        LD      BC,$4201            
89C0: 02              LD      (BC),A              
89C1: 0E 1F           LD      C,$1F               
89C3: B8              CP      B                   
89C4: 08              EX      AF,AF'              
89C5: B2              OR      D                   
89C6: E5              PUSH    HL                  
89C7: 64              LD      H,H                 
89C8: B8              CP      B                   
89C9: 16 05           LD      D,$05               
89CB: 67              LD      H,A                 
89CC: 46              LD      B,(HL)              
89CD: 5E              LD      E,(HL)              
89CE: 44              LD      B,H                 
89CF: A0              AND     B                   
89D0: 10 08           DJNZ    $89DA               ; {}
89D2: 8E              ADC     A,(HL)              
89D3: 02              LD      (BC),A              
89D4: 88              ADC     A,B                 
89D5: 02              LD      (BC),A              
89D6: 03              INC     BC                  
89D7: 81              ADD     A,C                 
89D8: 5B              LD      E,E                 
89D9: 52              LD      D,D                 
89DA: 10 08           DJNZ    $89E4               ; {}
89DC: A6              AND     (HL)                
89DD: 03              INC     BC                  
89DE: 88              ADC     A,B                 
89DF: 02              LD      (BC),A              
89E0: 03              INC     BC                  
89E1: 81              ADD     A,C                 
89E2: 5B              LD      E,E                 
89E3: 52              LD      D,D                 
89E4: 10 34           DJNZ    $8A1A               ; {}
89E6: 93              SUB     E                   
89E7: 23              INC     HL                  
89E8: 88              ADC     A,B                 
89E9: 03              INC     BC                  
89EA: 12              LD      (DE),A              
89EB: 04              INC     B                   
89EC: 10 46           DJNZ    $8A34               ; {}
89EE: 45              LD      B,L                 
89EF: 44              LD      B,H                 
89F0: A0              AND     B                   
89F1: 3F              CCF                         
89F2: 16 0D           LD      D,$0D               
89F4: 47              LD      B,A                 
89F5: 89              ADC     A,C                 
89F6: 17              RLA                         
89F7: 5E              LD      E,(HL)              
89F8: 17              RLA                         
89F9: 5D              LD      E,L                 
89FA: 7A              LD      A,D                 
89FB: 5B              LD      E,E                 
89FC: BB              CP      E                   
89FD: 07              RLCA                        
89FE: 0C              INC     C                   
89FF: 0D              DEC     C                   
8A00: 0A              LD      A,(BC)              
8A01: 0E 04           LD      C,$04               
8A03: 0A              LD      A,(BC)              
8A04: 3A 0A 42        LD      A,($420A)           
8A07: 14              INC     D                   
8A08: 09              ADD     HL,BC               
8A09: 1E BA           LD      E,$BA               
8A0B: 01 01 43        LD      BC,$4301            
8A0E: 02              LD      (BC),A              
8A0F: 0A              LD      A,(BC)              
8A10: 81              ADD     A,C                 
8A11: 5B              LD      E,E                 
8A12: 96              SUB     (HL)                
8A13: AF              XOR     A                   
8A14: D5              PUSH    DE                  
8A15: 9C              SBC     H                   
8A16: 8F              ADC     A,A                 
8A17: 8C              ADC     A,H                 
8A18: CB 23           SLA     E                   
8A1A: 10 24           DJNZ    $8A40               ; {}
8A1C: 93              SUB     E                   
8A1D: 23              INC     HL                  
8A1E: 88              ADC     A,B                 
8A1F: 03              INC     BC                  
8A20: 11 04 0F        LD      DE,$0F04            
8A23: 46              LD      B,(HL)              
8A24: 45              LD      B,L                 
8A25: 44              LD      B,H                 
8A26: A0              AND     B                   
8A27: 3F              CCF                         
8A28: 16 0D           LD      D,$0D               
8A2A: 47              LD      B,A                 
8A2B: 89              ADC     A,C                 
8A2C: 17              RLA                         
8A2D: B9              CP      C                   
8A2E: 14              INC     D                   
8A2F: E5              PUSH    HL                  
8A30: 4B              LD      C,E                 
8A31: 2E 01           LD      L,$01               
8A33: 01 44 02        LD      BC,$0244            
8A36: 09              ADD     HL,BC               
8A37: 81              ADD     A,C                 
8A38: 5B              LD      E,E                 
8A39: 96              SUB     (HL)                
8A3A: AF              XOR     A                   
8A3B: C4 9C 25        CALL    NZ,$259C            
8A3E: 9E              SBC     (HL)                
8A3F: 53              LD      D,E                 
8A40: 10 08           DJNZ    $8A4A               ; {}
8A42: 94              SUB     H                   
8A43: 03              INC     BC                  
8A44: 88              ADC     A,B                 
8A45: 02              LD      (BC),A              
8A46: 03              INC     BC                  
8A47: 81              ADD     A,C                 
8A48: 5B              LD      E,E                 
8A49: 52              LD      D,D                 
8A4A: 10 32           DJNZ    $8A7E               ; {}
8A4C: 99              SBC     C                   
8A4D: 24              INC     H                   
8A4E: 88              ADC     A,B                 
8A4F: 03              INC     BC                  
8A50: 20 04           JR      NZ,$8A56            ; {}
8A52: 1E 5F           LD      E,$5F               
8A54: BE              CP      (HL)                
8A55: 5B              LD      E,E                 
8A56: B1              OR      C                   
8A57: 2F              CPL                         
8A58: 49              LD      C,C                 
8A59: 09              ADD     HL,BC               
8A5A: 15              DEC     D                   
8A5B: B6              OR      (HL)                
8A5C: C3 46 5E        JP      $5E46               ; {}
8A5F: 44              LD      B,H                 
8A60: A0              AND     B                   
8A61: CE B5           ADC     $B5                 
8A63: 86              ADD     A,(HL)              
8A64: 5F              LD      E,A                 
8A65: 91              SUB     C                   
8A66: 7A              LD      A,D                 
8A67: 89              ADC     A,C                 
8A68: 17              RLA                         
8A69: 82              ADD     A,D                 
8A6A: 17              RLA                         
8A6B: 4A              LD      C,D                 
8A6C: 5E              LD      E,(HL)              
8A6D: FF              RST     0X38                
8A6E: A0              AND     B                   
8A6F: 9B              SBC     E                   
8A70: 8F              ADC     A,A                 
8A71: 01 02 45        LD      BC,$4502            
8A74: 47              LD      B,A                 
8A75: 02              LD      (BC),A              
8A76: 07              RLCA                        
8A77: 86              ADD     A,(HL)              
8A78: 74              LD      (HL),H              
8A79: 33              INC     SP                  
8A7A: 61              LD      H,C                 
8A7B: 81              ADD     A,C                 
8A7C: 5B              LD      E,E                 
8A7D: 52              LD      D,D                 
8A7E: 10 08           DJNZ    $8A88               ; {}
8A80: AA              XOR     D                   
8A81: 04              INC     B                   
8A82: 88              ADC     A,B                 
8A83: 02              LD      (BC),A              
8A84: 03              INC     BC                  
8A85: 81              ADD     A,C                 
8A86: 5B              LD      E,E                 
8A87: 52              LD      D,D                 
8A88: 10 39           DJNZ    $8AC3               ; {}
8A8A: 99              SBC     C                   
8A8B: 64              LD      H,H                 
8A8C: 88              ADC     A,B                 
8A8D: 02              LD      (BC),A              
8A8E: 08              EX      AF,AF'              
8A8F: 95              SUB     L                   
8A90: 91              SUB     C                   
8A91: 58              LD      E,B                 
8A92: B8              CP      B                   
8A93: 46              LD      B,(HL)              
8A94: 5E              LD      E,(HL)              
8A95: 44              LD      B,H                 
8A96: A0              AND     B                   
8A97: 07              RLCA                        
8A98: 0C              INC     C                   
8A99: 0D              DEC     C                   
8A9A: 0A              LD      A,(BC)              
8A9B: 0E 04           LD      C,$04               
8A9D: 0A              LD      A,(BC)              
8A9E: 3A 0A 42        LD      A,($420A)           
8AA1: 14              INC     D                   
8AA2: 09              ADD     HL,BC               
8AA3: 1D              DEC     E                   
8AA4: BA              CP      D                   
8AA5: 01 02 3F        LD      BC,$3F02            
8AA8: 40              LD      B,B                 
8AA9: 03              INC     BC                  
8AAA: 18 04           JR      $8AB0               ; {}
8AAC: 16 4F           LD      D,$4F               
8AAE: 45              LD      B,L                 
8AAF: 65              LD      H,L                 
8AB0: 49              LD      C,C                 
8AB1: CF              RST     0X08                
8AB2: 7B              LD      A,E                 
8AB3: 09              ADD     HL,BC               
8AB4: 15              DEC     D                   
8AB5: A3              AND     E                   
8AB6: A0              AND     B                   
8AB7: E3              EX      (SP),HL             
8AB8: 8B              ADC     A,E                 
8AB9: 0B              DEC     BC                  
8ABA: 5C              LD      E,H                 
8ABB: 6B              LD      L,E                 
8ABC: BF              CP      A                   
8ABD: 5F              LD      E,A                 
8ABE: BE              CP      (HL)                
8ABF: AB              XOR     E                   
8AC0: 14              INC     D                   
8AC1: 6F              LD      L,A                 
8AC2: 99              SBC     C                   
8AC3: 10 08           DJNZ    $8ACD               ; {}
8AC5: 9A              SBC     D                   
8AC6: 04              INC     B                   
8AC7: 88              ADC     A,B                 
8AC8: 02              LD      (BC),A              
8AC9: 03              INC     BC                  
8ACA: 81              ADD     A,C                 
8ACB: 5B              LD      E,E                 
8ACC: 52              LD      D,D                 
8ACD: 10 03           DJNZ    $8AD2               ; {}
8ACF: 00              NOP                         
8AD0: 00              NOP                         
8AD1: 00              NOP                         
8AD2: 10 03           DJNZ    $8AD7               ; {}
8AD4: 00              NOP                         
8AD5: 00              NOP                         
8AD6: 00              NOP                         
8AD7: 10 1D           DJNZ    $8AF6               ; {}
8AD9: 00              NOP                         
8ADA: 22 88 03        LD      ($0388),HL          
8ADD: 13              INC     DE                  
8ADE: 04              INC     B                   
8ADF: 11 46 45        LD      DE,$4546            
8AE2: 44              LD      B,H                 
8AE3: A0              AND     B                   
8AE4: 3F              CCF                         
8AE5: 16 0D           LD      D,$0D               
8AE7: 47              LD      B,A                 
8AE8: B0              OR      B                   
8AE9: 17              RLA                         
8AEA: F4 59 B9        CALL    P,$B959             
8AED: 6E              LD      L,(HL)              
8AEE: 8E              ADC     A,(HL)              
8AEF: C5              PUSH    BC                  
8AF0: 2E 02           LD      L,$02               
8AF2: 03              INC     BC                  
8AF3: 81              ADD     A,C                 
8AF4: 5B              LD      E,E                 
8AF5: 52              LD      D,D                 
8AF6: 10 08           DJNZ    $8B00               ; {}
8AF8: DB 02           IN      A,($02)             
8AFA: 88              ADC     A,B                 
8AFB: 02              LD      (BC),A              
8AFC: 03              INC     BC                  
8AFD: 81              ADD     A,C                 
8AFE: 5B              LD      E,E                 
8AFF: 52              LD      D,D                 
8B00: 10 30           DJNZ    $8B32               ; {}
8B02: DD ; ????
8B03: 64              LD      H,H                 
8B04: 88              ADC     A,B                 
8B05: 03              INC     BC                  
8B06: 12              LD      (DE),A              
8B07: 04              INC     B                   
8B08: 10 54           DJNZ    $8B5E               ; {}
8B0A: 45              LD      B,L                 
8B0B: F3              DI                          
8B0C: 5F              LD      E,A                 
8B0D: 81              ADD     A,C                 
8B0E: 5B              LD      E,E                 
8B0F: 8E              ADC     A,(HL)              
8B10: AF              XOR     A                   
8B11: 86              ADD     A,(HL)              
8B12: 5F              LD      E,A                 
8B13: D0              RET     NC                  
8B14: B5              OR      L                   
8B15: BE              CP      (HL)                
8B16: A0              AND     B                   
8B17: 9B              SBC     E                   
8B18: 76              HALT                        
8B19: 07              RLCA                        
8B1A: 0C              INC     C                   
8B1B: 0D              DEC     C                   
8B1C: 0A              LD      A,(BC)              
8B1D: 0E 04           LD      C,$04               
8B1F: 0A              LD      A,(BC)              
8B20: 3A 0A 42        LD      A,($420A)           
8B23: 14              INC     D                   
8B24: 09              ADD     HL,BC               
8B25: 1A              LD      A,(DE)              
8B26: BA              CP      D                   
8B27: 01 01 13        LD      BC,$1301            
8B2A: 02              LD      (BC),A              
8B2B: 06 66           LD      B,$66               
8B2D: B1              OR      C                   
8B2E: 09              ADD     HL,BC               
8B2F: 15              DEC     D                   
8B30: A3              AND     E                   
8B31: A0              AND     B                   
8B32: 10 08           DJNZ    $8B3C               ; {}
8B34: DE 04           SBC     $04                 
8B36: 88              ADC     A,B                 
8B37: 02              LD      (BC),A              
8B38: 03              INC     BC                  
8B39: 81              ADD     A,C                 
8B3A: 5B              LD      E,E                 
8B3B: 52              LD      D,D                 
8B3C: 10 30           DJNZ    $8B6E               ; {}
8B3E: DD ; ????
8B3F: 64              LD      H,H                 
8B40: 88              ADC     A,B                 
8B41: 03              INC     BC                  
8B42: 12              LD      (DE),A              
8B43: 04              INC     B                   
8B44: 10 44           DJNZ    $8B8A               ; {}
8B46: 45              LD      B,L                 
8B47: 67              LD      H,A                 
8B48: 8E              ADC     A,(HL)              
8B49: 09              ADD     HL,BC               
8B4A: 15              DEC     D                   
8B4B: A3              AND     E                   
8B4C: A0              AND     B                   
8B4D: E3              EX      (SP),HL             
8B4E: 8B              ADC     A,E                 
8B4F: 0B              DEC     BC                  
8B50: 5C              LD      E,H                 
8B51: 47              LD      B,A                 
8B52: B9              CP      C                   
8B53: 77              LD      (HL),A              
8B54: BE              CP      (HL)                
8B55: 01 01 0D        LD      BC,$0D01            
8B58: 07              RLCA                        
8B59: 0C              INC     C                   
8B5A: 0D              DEC     C                   
8B5B: 0A              LD      A,(BC)              
8B5C: 0E 04           LD      C,$04               
8B5E: 0A              LD      A,(BC)              
8B5F: 3A 0A 42        LD      A,($420A)           
8B62: 14              INC     D                   
8B63: 09              ADD     HL,BC               
8B64: 1A              LD      A,(DE)              
8B65: BA              CP      D                   
8B66: 02              LD      (BC),A              
8B67: 06 8F           LD      B,$8F               
8B69: 4E              LD      C,(HL)              
8B6A: 46              LD      B,(HL)              
8B6B: 5E              LD      E,(HL)              
8B6C: 44              LD      B,H                 
8B6D: A0              AND     B                   
8B6E: 10 08           DJNZ    $8B78               ; {}
8B70: DF              RST     0X18                
8B71: 04              INC     B                   
8B72: 88              ADC     A,B                 
8B73: 02              LD      (BC),A              
8B74: 03              INC     BC                  
8B75: 81              ADD     A,C                 
8B76: 5B              LD      E,E                 
8B77: 52              LD      D,D                 
8B78: 16 3E           LD      D,$3E               
8B7A: 47              LD      B,A                 
8B7B: 00              NOP                         
8B7C: A4              AND     H                   
8B7D: 03              INC     BC                  
8B7E: 14              INC     D                   
8B7F: 04              INC     B                   
8B80: 12              LD      (DE),A              
8B81: 5F              LD      E,A                 
8B82: BE              CP      (HL)                
8B83: 5B              LD      E,E                 
8B84: B1              OR      C                   
8B85: 4B              LD      C,E                 
8B86: 7B              LD      A,E                 
8B87: 4F              LD      C,A                 
8B88: 45              LD      B,L                 
8B89: 66              LD      H,(HL)              
8B8A: 49              LD      C,C                 
8B8B: 23              INC     HL                  
8B8C: 62              LD      H,D                 
8B8D: BB              CP      E                   
8B8E: 85              ADD     A,L                 
8B8F: 9F              SBC     A                   
8B90: 15              DEC     D                   
8B91: 7F              LD      A,A                 
8B92: B1              OR      C                   
8B93: 01 01 14        LD      BC,$1401            
8B96: 0C              INC     C                   
8B97: 01 02 07        LD      BC,$0702            
8B9A: 14              INC     D                   
8B9B: 0D              DEC     C                   
8B9C: 12              LD      (DE),A              
8B9D: 0A              LD      A,(BC)              
8B9E: 08              EX      AF,AF'              
8B9F: 04              INC     B                   
8BA0: 0E C5           LD      C,$C5               
8BA2: 1A              LD      A,(DE)              
8BA3: 1B              DEC     DE                  
8BA4: 92              SUB     D                   
8BA5: 95              SUB     L                   
8BA6: 91              SUB     C                   
8BA7: F4 BD 17        CALL    P,$17BD             
8BAA: 16 45           LD      D,$45               
8BAC: DB 5C           IN      A,($5C)             
8BAE: A2              AND     D                   
8BAF: 02              LD      (BC),A              
8BB0: 07              RLCA                        
8BB1: 95              SUB     L                   
8BB2: 91              SUB     C                   
8BB3: F4 BD 17        CALL    P,$17BD             
8BB6: 16 59           LD      D,$59               
8BB8: 16 36           LD      D,$36               
8BBA: 48              LD      C,B                 
8BBB: 00              NOP                         
8BBC: A4              AND     H                   
8BBD: 03              INC     BC                  
8BBE: 14              INC     D                   
8BBF: 04              INC     B                   
8BC0: 12              LD      (DE),A              
8BC1: 5F              LD      E,A                 
8BC2: BE              CP      (HL)                
8BC3: 5B              LD      E,E                 
8BC4: B1              OR      C                   
8BC5: 4B              LD      C,E                 
8BC6: 7B              LD      A,E                 
8BC7: 44              LD      B,H                 
8BC8: 45              LD      B,L                 
8BC9: D5              PUSH    DE                  
8BCA: B0              OR      B                   
8BCB: CD B5 3B        CALL    $3BB5               
8BCE: 63              LD      H,E                 
8BCF: F4 72 DB        CALL    P,$DB72             
8BD2: 63              LD      H,E                 
8BD3: 0C              INC     C                   
8BD4: 01 02 01        LD      BC,$0102            
8BD7: 02              LD      (BC),A              
8BD8: 15              DEC     D                   
8BD9: 42              LD      B,D                 
8BDA: 07              RLCA                        
8BDB: 0C              INC     C                   
8BDC: 0D              DEC     C                   
8BDD: 0A              LD      A,(BC)              
8BDE: 0A              LD      A,(BC)              
8BDF: 08              EX      AF,AF'              
8BE0: 04              INC     B                   
8BE1: 06 9A           LD      B,$9A               
8BE3: 1D              DEC     E                   
8BE4: 33              INC     SP                  
8BE5: 62              LD      H,D                 
8BE6: 84              ADD     A,H                 
8BE7: 66              LD      H,(HL)              
8BE8: 02              LD      (BC),A              
8BE9: 06 6B           LD      B,$6B               
8BEB: 4F              LD      C,A                 
8BEC: CB B9           RES     7,C                 
8BEE: BB              CP      E                   
8BEF: 85              ADD     A,L                 
8BF0: 16 2B           LD      D,$2B               
8BF2: 49              LD      C,C                 
8BF3: 00              NOP                         
8BF4: A0              AND     B                   
8BF5: 03              INC     BC                  
8BF6: 16 04           LD      D,$04               
8BF8: 14              INC     D                   
8BF9: 5F              LD      E,A                 
8BFA: BE              CP      (HL)                
8BFB: 5B              LD      E,E                 
8BFC: B1              OR      C                   
8BFD: 4B              LD      C,E                 
8BFE: 7B              LD      A,E                 
8BFF: 55              LD      D,L                 
8C00: 45              LD      B,L                 
8C01: AE              XOR     (HL)                
8C02: 85              ADD     A,L                 
8C03: 89              ADC     A,C                 
8C04: 62              LD      H,D                 
8C05: 8D              ADC     A,L                 
8C06: 96              SUB     (HL)                
8C07: 3B              DEC     SP                  
8C08: 63              LD      H,E                 
8C09: F4 72 DB        CALL    P,$DB72             
8C0C: 63              LD      H,E                 
8C0D: 0C              INC     C                   
8C0E: 01 02 01        LD      BC,$0102            
8C11: 01 17 02        LD      BC,$0217            
8C14: 08              EX      AF,AF'              
8C15: 97              SUB     A                   
8C16: B8              CP      B                   
8C17: F6 8B           OR      $8B                 
8C19: 03              INC     BC                  
8C1A: A0              AND     B                   
8C1B: BB              CP      E                   
8C1C: 85              ADD     A,L                 
8C1D: 16 3A           LD      D,$3A               
8C1F: 21 00 A4        LD      HL,$A400            
8C22: 03              INC     BC                  
8C23: 16 04           LD      D,$04               
8C25: 14              INC     D                   
8C26: 5F              LD      E,A                 
8C27: BE              CP      (HL)                
8C28: 5B              LD      E,E                 
8C29: B1              OR      C                   
8C2A: 4B              LD      C,E                 
8C2B: 7B              LD      A,E                 
8C2C: 44              LD      B,H                 
8C2D: 45              LD      B,L                 
8C2E: 6B              LD      L,E                 
8C2F: 79              LD      A,C                 
8C30: FF              RST     0X38                
8C31: B9              CP      C                   
8C32: 33              INC     SP                  
8C33: 61              LD      H,C                 
8C34: BB              CP      E                   
8C35: 85              ADD     A,L                 
8C36: 9F              SBC     A                   
8C37: 15              DEC     D                   
8C38: 7F              LD      A,A                 
8C39: B1              OR      C                   
8C3A: 0C              INC     C                   
8C3B: 01 02 01        LD      BC,$0102            
8C3E: 03              INC     BC                  
8C3F: 40              LD      B,B                 
8C40: 18 0E           JR      $8C50               ; {}
8C42: 07              RLCA                        
8C43: 0A              LD      A,(BC)              
8C44: 0D              DEC     C                   
8C45: 08              EX      AF,AF'              
8C46: 0A              LD      A,(BC)              
8C47: 08              EX      AF,AF'              
8C48: 04              INC     B                   
8C49: 04              INC     B                   
8C4A: EB              EX      DE,HL               
8C4B: 1A              LD      A,(DE)              
8C4C: 4C              LD      C,H                 
8C4D: 99              SBC     C                   
8C4E: 02              LD      (BC),A              
8C4F: 09              ADD     HL,BC               
8C50: 09              ADD     HL,BC               
8C51: 4E              LD      C,(HL)              
8C52: 66              LD      H,(HL)              
8C53: 17              RLA                         
8C54: 2E 60           LD      L,$60               
8C56: 17              RLA                         
8C57: 16 59           LD      D,$59               
8C59: 16 33           LD      D,$33               
8C5B: 21 00 A4        LD      HL,$A400            
8C5E: 03              INC     BC                  
8C5F: 12              LD      (DE),A              
8C60: 04              INC     B                   
8C61: 10 5F           DJNZ    $8CC2               ; {}
8C63: BE              CP      (HL)                
8C64: 5B              LD      E,E                 
8C65: B1              OR      C                   
8C66: 4B              LD      C,E                 
8C67: 7B              LD      A,E                 
8C68: 54              LD      D,H                 
8C69: 45              LD      B,L                 
8C6A: F3              DI                          
8C6B: 5F              LD      E,A                 
8C6C: BB              CP      E                   
8C6D: 85              ADD     A,L                 
8C6E: 9F              SBC     A                   
8C6F: 15              DEC     D                   
8C70: 7F              LD      A,A                 
8C71: B1              OR      C                   
8C72: 0C              INC     C                   
8C73: 01 02 01        LD      BC,$0102            
8C76: 02              LD      (BC),A              
8C77: 43              LD      B,E                 
8C78: 13              INC     DE                  
8C79: 07              RLCA                        
8C7A: 0C              INC     C                   
8C7B: 0D              DEC     C                   
8C7C: 0A              LD      A,(BC)              
8C7D: 0A              LD      A,(BC)              
8C7E: 08              EX      AF,AF'              
8C7F: 04              INC     B                   
8C80: 06 9E           LD      B,$9E               
8C82: 1D              DEC     E                   
8C83: 5D              LD      E,L                 
8C84: 7A              LD      A,D                 
8C85: E3              EX      (SP),HL             
8C86: B5              OR      L                   
8C87: 02              LD      (BC),A              
8C88: 05              DEC     B                   
8C89: 66              LD      H,(HL)              
8C8A: B1              OR      C                   
8C8B: 17              RLA                         
8C8C: 16 59           LD      D,$59               
8C8E: 16 34           LD      D,$34               
8C90: 21 00 A4        LD      HL,$A400            
8C93: 03              INC     BC                  
8C94: 14              INC     D                   
8C95: 04              INC     B                   
8C96: 12              LD      (DE),A              
8C97: 5F              LD      E,A                 
8C98: BE              CP      (HL)                
8C99: 5B              LD      E,E                 
8C9A: B1              OR      C                   
8C9B: 4B              LD      C,E                 
8C9C: 7B              LD      A,E                 
8C9D: 55              LD      D,L                 
8C9E: 45              LD      B,L                 
8C9F: 8E              ADC     A,(HL)              
8CA0: 91              SUB     C                   
8CA1: 0D              DEC     C                   
8CA2: 8A              ADC     A,D                 
8CA3: 3B              DEC     SP                  
8CA4: 63              LD      H,E                 
8CA5: F4 72 DB        CALL    P,$DB72             
8CA8: 63              LD      H,E                 
8CA9: 0C              INC     C                   
8CAA: 01 02 01        LD      BC,$0102            
8CAD: 02              LD      (BC),A              
8CAE: 4B              LD      C,E                 
8CAF: 0F              RRCA                        
8CB0: 07              RLCA                        
8CB1: 0A              LD      A,(BC)              
8CB2: 0D              DEC     C                   
8CB3: 08              EX      AF,AF'              
8CB4: 0A              LD      A,(BC)              
8CB5: 08              EX      AF,AF'              
8CB6: 04              INC     B                   
8CB7: 04              INC     B                   
8CB8: 13              INC     DE                  
8CB9: 1B              DEC     DE                  
8CBA: A3              AND     E                   
8CBB: 4B              LD      C,E                 
8CBC: 02              LD      (BC),A              
8CBD: 06 E3           LD      B,$E3               
8CBF: B8              CP      B                   
8CC0: F3              DI                          
8CC1: 8C              ADC     A,H                 
8CC2: BB              CP      E                   
8CC3: 85              ADD     A,L                 
8CC4: 1A              LD      A,(DE)              
8CC5: 32 8E 02        LD      ($028E),A           
8CC8: 81              ADD     A,C                 
8CC9: 07              RLCA                        
8CCA: 28 0D           JR      Z,$8CD9             ; {}
8CCC: 26 0E           LD      H,$0E               
8CCE: 08              EX      AF,AF'              
8CCF: 0A              LD      A,(BC)              
8CD0: 11 0A 42        LD      DE,$420A            
8CD3: 0A              LD      A,(BC)              
8CD4: 40              LD      B,B                 
8CD5: 0A              LD      A,(BC)              
8CD6: 3A 04 1A        LD      A,($1A04)           
8CD9: 03              INC     BC                  
8CDA: C0              RET     NZ                  
8CDB: 7B              LD      A,E                 
8CDC: 14              INC     D                   
8CDD: EB              EX      DE,HL               
8CDE: 5B              LD      E,E                 
8CDF: B4              OR      H                   
8CE0: D0              RET     NC                  
8CE1: CE 13           ADC     $13                 
8CE3: 76              HALT                        
8CE4: A0              AND     B                   
8CE5: 6B              LD      L,E                 
8CE6: 16 C6           LD      D,$C6               
8CE8: 59              LD      E,C                 
8CE9: B3              OR      E                   
8CEA: 63              LD      H,E                 
8CEB: A3              AND     E                   
8CEC: A0              AND     B                   
8CED: 06 4F           LD      B,$4F               
8CEF: 7F              LD      A,A                 
8CF0: BF              CP      A                   
8CF1: DB 31           IN      A,($31)             
8CF3: 02              LD      (BC),A              
8CF4: 03              INC     BC                  
8CF5: F5              PUSH    AF                  
8CF6: 59              LD      E,C                 
8CF7: 4B              LD      C,E                 
8CF8: 1B              DEC     DE                  
8CF9: 54              LD      D,H                 
8CFA: 8E              ADC     A,(HL)              
8CFB: 62              LD      H,D                 
8CFC: 8A              ADC     A,D                 
8CFD: 07              RLCA                        
8CFE: 43              LD      B,E                 
8CFF: 0E 41           LD      C,$41               
8D01: 0D              DEC     C                   
8D02: 3E 0E           LD      A,$0E               
8D04: 04              INC     B                   
8D05: 0A              LD      A,(BC)              
8D06: 3A 0A 42        LD      A,($420A)           
8D09: 1A              LD      A,(DE)              
8D0A: 2E 40           LD      L,$40               
8D0C: 2E 20           LD      L,$20               
8D0E: 09              ADD     HL,BC               
8D0F: 24              INC     H                   
8D10: 04              INC     B                   
8D11: 2B              DEC     HL                  
8D12: 5F              LD      E,A                 
8D13: BE              CP      (HL)                
8D14: 5B              LD      E,E                 
8D15: B1              OR      C                   
8D16: 4B              LD      C,E                 
8D17: 7B              LD      A,E                 
8D18: 55              LD      D,L                 
8D19: 45              LD      B,L                 
8D1A: AF              XOR     A                   
8D1B: 55              LD      D,L                 
8D1C: DA 5F B8        JP      C,$B85F             
8D1F: 16 89           LD      D,$89               
8D21: 17              RLA                         
8D22: CF              RST     0X08                
8D23: B3              OR      E                   
8D24: 66              LD      H,(HL)              
8D25: B1              OR      C                   
8D26: 67              LD      H,A                 
8D27: 16 4E           LD      D,$4E               
8D29: BD              CP      L                   
8D2A: 90              SUB     B                   
8D2B: 14              INC     D                   
8D2C: 16 58           LD      D,$58               
8D2E: DB 72           IN      A,($72)             
8D30: EB              EX      DE,HL               
8D31: 5B              LD      E,E                 
8D32: B4              OR      H                   
8D33: D0              RET     NC                  
8D34: BF              CP      A                   
8D35: 14              INC     D                   
8D36: A6              AND     (HL)                
8D37: B3              OR      E                   
8D38: D1              POP     DE                  
8D39: B5              OR      L                   
8D3A: F0              RET     P                   
8D3B: A4              AND     H                   
8D3C: 21 1A 2A        LD      HL,$2A1A            
8D3F: A6              AND     (HL)                
8D40: 38 BA           JR      C,$8CFC             ; {}
8D42: 01 01 28        LD      BC,$2801            
8D45: 02              LD      (BC),A              
8D46: 07              RLCA                        
8D47: 82              ADD     A,D                 
8D48: BF              CP      A                   
8D49: 0C              INC     C                   
8D4A: 15              DEC     D                   
8D4B: F7              RST     0X30                
8D4C: 49              LD      C,C                 
8D4D: 52              LD      D,D                 
8D4E: 1B              DEC     DE                  
8D4F: 43              LD      B,E                 
8D50: 8E              ADC     A,(HL)              
8D51: 62              LD      H,D                 
8D52: 8A              ADC     A,D                 
8D53: 07              RLCA                        
8D54: 30 0E           JR      NC,$8D64            ; {}
8D56: 2E 0D           LD      L,$0D               
8D58: 2B              DEC     HL                  
8D59: 0E 04           LD      C,$04               
8D5B: 0A              LD      A,(BC)              
8D5C: 3A 0A 42        LD      A,($420A)           
8D5F: 1A              LD      A,(DE)              
8D60: 2E 40           LD      L,$40               
8D62: 2E 20           LD      L,$20               
8D64: 09              ADD     HL,BC               
8D65: 24              INC     H                   
8D66: 04              INC     B                   
8D67: 19              ADD     HL,DE               
8D68: 56              LD      D,(HL)              
8D69: D1              POP     DE                  
8D6A: 03              INC     BC                  
8D6B: 71              LD      (HL),C              
8D6C: E4 14 8D        CALL    PO,$8D14            ; {}
8D6F: C5              PUSH    BC                  
8D70: 73              LD      (HL),E              
8D71: 76              HALT                        
8D72: 5F              LD      E,A                 
8D73: BE              CP      (HL)                
8D74: 0C              INC     C                   
8D75: 15              DEC     D                   
8D76: F7              RST     0X30                
8D77: 49              LD      C,C                 
8D78: 88              ADC     A,B                 
8D79: AF              XOR     A                   
8D7A: 87              ADD     A,A                 
8D7B: 8C              ADC     A,H                 
8D7C: D1              POP     DE                  
8D7D: B5              OR      L                   
8D7E: F0              RET     P                   
8D7F: A4              AND     H                   
8D80: 21 1A 2A        LD      HL,$2A1A            
8D83: A6              AND     (HL)                
8D84: BA              CP      D                   
8D85: 01 01 3C        LD      BC,$3C01            
8D88: 02              LD      (BC),A              
8D89: 09              ADD     HL,BC               
8D8A: C6 92           ADD     $92                 
8D8C: FF              RST     0X38                
8D8D: 5A              LD      E,D                 
8D8E: 0C              INC     C                   
8D8F: 15              DEC     D                   
8D90: F7              RST     0X30                
8D91: 49              LD      C,C                 
8D92: 52              LD      D,D                 
8D93: 1B              DEC     DE                  
8D94: 1C              INC     E                   
8D95: 8E              ADC     A,(HL)              
8D96: 22 8A 07        LD      ($078A),HL          
8D99: 09              ADD     HL,BC               
8D9A: 0D              DEC     C                   
8D9B: 07              RLCA                        
8D9C: 0E 04           LD      C,$04               
8D9E: 0A              LD      A,(BC)              
8D9F: 3A 0A 42        LD      A,($420A)           
8DA2: BA              CP      D                   
8DA3: 01 01 3E        LD      BC,$3E01            
8DA6: 02              LD      (BC),A              
8DA7: 09              ADD     HL,BC               
8DA8: 06 4F           LD      B,$4F               
8DAA: 7F              LD      A,A                 
8DAB: BF              CP      A                   
8DAC: 0C              INC     C                   
8DAD: 15              DEC     D                   
8DAE: F7              RST     0X30                
8DAF: 49              LD      C,C                 
8DB0: 52              LD      D,D                 
8DB1: 37              SCF                         
8DB2: 29              ADD     HL,HL               
8DB3: 49              LD      C,C                 
8DB4: 00              NOP                         
8DB5: E0              RET     PO                  
8DB6: 03              INC     BC                  
8DB7: 16 04           LD      D,$04               
8DB9: 14              INC     D                   
8DBA: 5F              LD      E,A                 
8DBB: BE              CP      (HL)                
8DBC: 5B              LD      E,E                 
8DBD: B1              OR      C                   
8DBE: 4B              LD      C,E                 
8DBF: 7B              LD      A,E                 
8DC0: 55              LD      D,L                 
8DC1: 45              LD      B,L                 
8DC2: 8E              ADC     A,(HL)              
8DC3: 91              SUB     C                   
8DC4: 05              DEC     B                   
8DC5: 8A              ADC     A,D                 
8DC6: 09              ADD     HL,BC               
8DC7: B3              OR      E                   
8DC8: D4 4C 9F        CALL    NC,$9F4C            ; {}
8DCB: 15              DEC     D                   
8DCC: 7F              LD      A,A                 
8DCD: B1              OR      C                   
8DCE: 0C              INC     C                   
8DCF: 01 10 02        LD      BC,$0210            
8DD2: 09              ADD     HL,BC               
8DD3: E3              EX      (SP),HL             
8DD4: B8              CP      B                   
8DD5: F3              DI                          
8DD6: 8C              ADC     A,H                 
8DD7: B9              CP      C                   
8DD8: 55              LD      D,L                 
8DD9: 2B              DEC     HL                  
8DDA: D0              RET     NC                  
8DDB: 52              LD      D,D                 
8DDC: 38 68           JR      C,$8E46             ; {}
8DDE: 22 00 A4        LD      ($A400),HL          ; {}
8DE1: 03              INC     BC                  
8DE2: 16 04           LD      D,$04               
8DE4: 14              INC     D                   
8DE5: 5F              LD      E,A                 
8DE6: BE              CP      (HL)                
8DE7: 5B              LD      E,E                 
8DE8: B1              OR      C                   
8DE9: 4B              LD      C,E                 
8DEA: 7B              LD      A,E                 
8DEB: 59              LD      E,C                 
8DEC: 45              LD      B,L                 
8DED: 9E              SBC     (HL)                
8DEE: 48              LD      C,B                 
8DEF: F3              DI                          
8DF0: 5F              LD      E,A                 
8DF1: 85              ADD     A,L                 
8DF2: A6              AND     (HL)                
8DF3: F4 BD 9F        CALL    P,$9FBD             ; {}
8DF6: 15              DEC     D                   
8DF7: 7F              LD      A,A                 
8DF8: B1              OR      C                   
8DF9: 07              RLCA                        
8DFA: 40              LD      B,B                 
8DFB: 0D              DEC     C                   
8DFC: 3E 0A           LD      A,$0A               
8DFE: 08              EX      AF,AF'              
8DFF: 04              INC     B                   
8E00: 3A 33 1E        LD      A,($1E33)           
8E03: BF              CP      A                   
8E04: 9A              SBC     D                   
8E05: AB              XOR     E                   
8E06: 57              LD      D,A                 
8E07: 86              ADD     A,(HL)              
8E08: 91              SUB     C                   
8E09: 09              ADD     HL,BC               
8E0A: 15              DEC     D                   
8E0B: D6 6A           SUB     $6A                 
8E0D: 74              LD      (HL),H              
8E0E: 75              LD      (HL),L              
8E0F: 90              SUB     B                   
8E10: 91              SUB     C                   
8E11: 03              INC     BC                  
8E12: EE 83           XOR     $83                 
8E14: 8C              ADC     A,H                 
8E15: CC B5 59        CALL    Z,$59B5             
8E18: F4 56 F4        CALL    P,$F456             
8E1B: 74              LD      (HL),H              
8E1C: 75              LD      (HL),L              
8E1D: 90              SUB     B                   
8E1E: 91              SUB     C                   
8E1F: 08              EX      AF,AF'              
8E20: EE A3           XOR     $A3                 
8E22: A0              AND     B                   
8E23: 87              ADD     A,A                 
8E24: 5B              LD      E,E                 
8E25: 7F              LD      A,A                 
8E26: 4E              LD      C,(HL)              
8E27: DB 16           IN      A,($16)             
8E29: 5B              LD      E,E                 
8E2A: B2              OR      D                   
8E2B: AB              XOR     E                   
8E2C: 98              SBC     B                   
8E2D: 83              ADD     A,E                 
8E2E: 7A              LD      A,D                 
8E2F: 4A              LD      C,D                 
8E30: 45              LD      B,L                 
8E31: E2 A0 7B        JP      PO,$7BA0            ; {}
8E34: 7B              LD      A,E                 
8E35: 1C              INC     E                   
8E36: 8A              ADC     A,D                 
8E37: 0F              RRCA                        
8E38: A0              AND     B                   
8E39: 63              LD      H,E                 
8E3A: F4 02 09        CALL    P,$0902             
8E3D: 10 D0           DJNZ    $8E0F               ; {}
8E3F: E6 BD           AND     $BD                 
8E41: E9              JP      (HL)                
8E42: 16 FF           LD      D,$FF               
8E44: B9              CP      C                   
8E45: 52              LD      D,D                 
8E46: 19              ADD     HL,DE               
8E47: 80              ADD     A,B                 
8E48: 8A              ADC     A,D                 
8E49: 8E              ADC     A,(HL)              
8E4A: E2 8A 07        JP      PO,$078A            
8E4D: 7B              LD      A,E                 
8E4E: 0E 79           LD      C,$79               
8E50: 0D              DEC     C                   
8E51: 41              LD      B,C                 
8E52: 0E 04           LD      C,$04               
8E54: 0A              LD      A,(BC)              
8E55: 3A 0A 42        LD      A,($420A)           
8E58: 03              INC     BC                  
8E59: 8E              ADC     A,(HL)              
8E5A: 27              DAA                         
8E5B: 09              ADD     HL,BC               
8E5C: 1F              RRA                         
8E5D: 04              INC     B                   
8E5E: 29              ADD     HL,HL               
8E5F: 5F              LD      E,A                 
8E60: BE              CP      (HL)                
8E61: 17              RLA                         
8E62: 16 56           LD      D,$56               
8E64: DB 38           IN      A,($38)             
8E66: C6 33           ADD     $33                 
8E68: BB              CP      E                   
8E69: 5F              LD      E,A                 
8E6A: BE              CP      (HL)                
8E6B: 49              LD      C,C                 
8E6C: 16 8B           LD      D,$8B               
8E6E: 54              LD      D,H                 
8E6F: C3 54 A5        JP      $A554               ; {}
8E72: 54              LD      D,H                 
8E73: 03              INC     BC                  
8E74: EE 33           XOR     $33                 
8E76: 98              SBC     B                   
8E77: 5F              LD      E,A                 
8E78: BE              CP      (HL)                
8E79: D3 14           OUT     ($14),A             
8E7B: 10 4E           DJNZ    $8ECB               ; {}
8E7D: 73              LD      (HL),E              
8E7E: 62              LD      H,D                 
8E7F: 6C              LD      L,H                 
8E80: B9              CP      C                   
8E81: 91              SUB     C                   
8E82: 7A              LD      A,D                 
8E83: D1              POP     DE                  
8E84: B5              OR      L                   
8E85: F0              RET     P                   
8E86: A4              AND     H                   
8E87: 21 17 27        LD      HL,$2717            
8E8A: 00              NOP                         
8E8B: 17              RLA                         
8E8C: 28 26           JR      Z,$8EB4             ; {}
8E8E: 1C              INC     E                   
8E8F: 26 29           LD      H,$29               
8E91: 2A 38 0D        LD      HL,($0D38)          
8E94: 28 0E           JR      Z,$8EA4             ; {}
8E96: 04              INC     B                   
8E97: 0A              LD      A,(BC)              
8E98: 3A 0A 42        LD      A,($420A)           
8E9B: 09              ADD     HL,BC               
8E9C: 24              INC     H                   
8E9D: 04              INC     B                   
8E9E: 1C              INC     E                   
8E9F: 5F              LD      E,A                 
8EA0: BE              CP      (HL)                
8EA1: 49              LD      C,C                 
8EA2: 16 8B           LD      D,$8B               
8EA4: 54              LD      D,H                 
8EA5: 03              INC     BC                  
8EA6: A0              AND     B                   
8EA7: 5F              LD      E,A                 
8EA8: BE              CP      (HL)                
8EA9: D3 14           OUT     ($14),A             
8EAB: 10 4E           DJNZ    $8EFB               ; {}
8EAD: 73              LD      (HL),E              
8EAE: 62              LD      H,D                 
8EAF: 4B              LD      C,E                 
8EB0: 7B              LD      A,E                 
8EB1: 81              ADD     A,C                 
8EB2: BF              CP      A                   
8EB3: 66              LD      H,(HL)              
8EB4: 17              RLA                         
8EB5: 00              NOP                         
8EB6: B3              OR      E                   
8EB7: C8              RET     Z                   
8EB8: 6A              LD      L,D                 
8EB9: A3              AND     E                   
8EBA: A0              AND     B                   
8EBB: A9              XOR     C                   
8EBC: 8B              ADC     A,E                 
8EBD: 0D              DEC     C                   
8EBE: 0A              LD      A,(BC)              
8EBF: 0E 04           LD      C,$04               
8EC1: 0A              LD      A,(BC)              
8EC2: 3A 0A 42        LD      A,($420A)           
8EC5: 14              INC     D                   
8EC6: 09              ADD     HL,BC               
8EC7: 1F              RRA                         
8EC8: BA              CP      D                   
8EC9: 02              LD      (BC),A              
8ECA: 08              EX      AF,AF'              
8ECB: 30 6F           JR      NC,$8F3C            ; {}
8ECD: D3 14           OUT     ($14),A             
8ECF: 10 4E           DJNZ    $8F1F               ; {}
8ED1: 73              LD      (HL),E              
8ED2: 62              LD      H,D                 
8ED3: 39              ADD     HL,SP               
8ED4: 53              LD      D,E                 
8ED5: 8E              ADC     A,(HL)              
8ED6: 02              LD      (BC),A              
8ED7: C0              RET     NZ                  
8ED8: 03              INC     BC                  
8ED9: 2C              INC     L                   
8EDA: 04              INC     B                   
8EDB: 2A 5F BE        LD      HL,($BE5F)          
8EDE: 5B              LD      E,E                 
8EDF: B1              OR      C                   
8EE0: 4B              LD      C,E                 
8EE1: 7B              LD      A,E                 
8EE2: 4E              LD      C,(HL)              
8EE3: 45              LD      B,L                 
8EE4: 06 9E           LD      B,$9E               
8EE6: F3              DI                          
8EE7: 5F              LD      E,A                 
8EE8: 87              ADD     A,A                 
8EE9: 5B              LD      E,E                 
8EEA: 7F              LD      A,A                 
8EEB: 4E              LD      C,(HL)              
8EEC: AB              XOR     E                   
8EED: 14              INC     D                   
8EEE: 6F              LD      L,A                 
8EEF: B3              OR      E                   
8EF0: 15              DEC     D                   
8EF1: 8A              ADC     A,D                 
8EF2: 86              ADD     A,(HL)              
8EF3: 74              LD      (HL),H              
8EF4: 30 6F           JR      NC,$8F65            ; {}
8EF6: 49              LD      C,C                 
8EF7: 16 97           LD      D,$97               
8EF9: 54              LD      D,H                 
8EFA: 0B              DEC     BC                  
8EFB: 58              LD      E,B                 
8EFC: 96              SUB     (HL)                
8EFD: 96              SUB     (HL)                
8EFE: DB 72           IN      A,($72)             
8F00: 04              INC     B                   
8F01: 53              LD      D,E                 
8F02: 8F              ADC     A,A                 
8F03: 7A              LD      A,D                 
8F04: 9B              SBC     E                   
8F05: C1              POP     BC                  
8F06: 07              RLCA                        
8F07: 19              ADD     HL,DE               
8F08: 0D              DEC     C                   
8F09: 17              RLA                         
8F0A: 0E 04           LD      C,$04               
8F0C: 0A              LD      A,(BC)              
8F0D: 05              DEC     B                   
8F0E: 0A              LD      A,(BC)              
8F0F: 43              LD      B,E                 
8F10: 04              INC     B                   
8F11: 0F              RRCA                        
8F12: 5F              LD      E,A                 
8F13: BE              CP      (HL)                
8F14: D3 14           OUT     ($14),A             
8F16: 10 4E           DJNZ    $8F66               ; {}
8F18: 73              LD      (HL),E              
8F19: 62              LD      H,D                 
8F1A: 4B              LD      C,E                 
8F1B: 7B              LD      A,E                 
8F1C: 75              LD      (HL),L              
8F1D: 8D              ADC     A,L                 
8F1E: A6              AND     (HL)                
8F1F: 85              ADD     A,L                 
8F20: 2E 02           LD      L,$02               
8F22: 05              DEC     B                   
8F23: 29              ADD     HL,HL               
8F24: B8              CP      B                   
8F25: 47              LD      B,A                 
8F26: BE              CP      (HL)                
8F27: 4E              LD      C,(HL)              
8F28: 39              ADD     HL,SP               
8F29: 2E 00           LD      L,$00               
8F2B: 00              NOP                         
8F2C: E0              RET     PO                  
8F2D: 03              INC     BC                  
8F2E: 01 80 07        LD      BC,$0780            
8F31: 1C              INC     E                   
8F32: 0D              DEC     C                   
8F33: 1A              LD      A,(DE)              
8F34: 0E 06           LD      C,$06               
8F36: 0A              LD      A,(BC)              
8F37: 0B              DEC     BC                  
8F38: 0A              LD      A,(BC)              
8F39: 10 0A           DJNZ    $8F45               ; {}
8F3B: 4C              LD      C,H                 
8F3C: 0E 06           LD      C,$06               
8F3E: 03              INC     BC                  
8F3F: 28 29           JR      Z,$8F6A             ; {}
8F41: 03              INC     BC                  
8F42: 28 2A           JR      Z,$8F6E             ; {}
8F44: A8              XOR     B                   
8F45: 04              INC     B                   
8F46: 07              RLCA                        
8F47: 4B              LD      C,E                 
8F48: 7B              LD      A,E                 
8F49: 73              LD      (HL),E              
8F4A: 8D              ADC     A,L                 
8F4B: E6 59           AND     $59                 
8F4D: 21 0C 01        LD      HL,$010C            
8F50: 15              DEC     D                   
8F51: 02              LD      (BC),A              
8F52: 05              DEC     B                   
8F53: 29              ADD     HL,HL               
8F54: B8              CP      B                   
8F55: 47              LD      B,A                 
8F56: BE              CP      (HL)                
8F57: 4E              LD      C,(HL)              
8F58: 00              NOP                         
8F59: 0E 28           LD      C,$28               
8F5B: 00              NOP                         
8F5C: A0              AND     B                   
8F5D: 08              EX      AF,AF'              
8F5E: 09              ADD     HL,BC               
8F5F: 0D              DEC     C                   
8F60: 07              RLCA                        
8F61: 14              INC     D                   
8F62: 03              INC     BC                  
8F63: 28 2A           JR      Z,$8F8F             ; {}
8F65: 1C              INC     E                   
8F66: 29              ADD     HL,HL               
8F67: BC              CP      H                   
8F68: 00              NOP                         
8F69: 0A              LD      A,(BC)              
8F6A: 28 00           JR      Z,$8F6C             ; {}
8F6C: A0              AND     B                   
8F6D: 08              EX      AF,AF'              
8F6E: 05              DEC     B                   
8F6F: 0D              DEC     C                   
8F70: 03              INC     BC                  
8F71: 1C              INC     E                   
8F72: 2A BC 3A        LD      HL,($3ABC)          
8F75: 6C              LD      L,H                 
8F76: 82              ADD     A,D                 
8F77: 01 81 03        LD      BC,$0381            
8F7A: 22 04 20        LD      ($2004),HL          
8F7D: 83              ADD     A,E                 
8F7E: 48              LD      C,B                 
8F7F: BE              CP      (HL)                
8F80: 9F              SBC     A                   
8F81: 4B              LD      C,E                 
8F82: 15              DEC     D                   
8F83: 23              INC     HL                  
8F84: B8              CP      B                   
8F85: 0F              RRCA                        
8F86: A0              AND     B                   
8F87: 09              ADD     HL,BC               
8F88: 58              LD      E,B                 
8F89: 55              LD      D,L                 
8F8A: 8B              ADC     A,E                 
8F8B: D6 B5           SUB     $B5                 
8F8D: 53              LD      D,E                 
8F8E: A0              AND     B                   
8F8F: 15              DEC     D                   
8F90: 6C              LD      L,H                 
8F91: EF              RST     0X28                
8F92: 16 D3           LD      D,$D3               
8F94: 93              SUB     E                   
8F95: FB              EI                          
8F96: B9              CP      C                   
8F97: 4D              LD      C,L                 
8F98: 98              SBC     B                   
8F99: 9F              SBC     A                   
8F9A: 15              DEC     D                   
8F9B: 7F              LD      A,A                 
8F9C: B1              OR      C                   
8F9D: 07              RLCA                        
8F9E: 3B              DEC     SP                  
8F9F: 0D              DEC     C                   
8FA0: 39              ADD     HL,SP               
8FA1: 0E 04           LD      C,$04               
8FA3: 0A              LD      A,(BC)              
8FA4: 08              EX      AF,AF'              
8FA5: 0A              LD      A,(BC)              
8FA6: 0B              DEC     BC                  
8FA7: 04              INC     B                   
8FA8: 31 3B 95        LD      SP,$953B            
8FAB: 41              LD      B,C                 
8FAC: 6E              LD      L,(HL)              
8FAD: 4F              LD      C,A                 
8FAE: 5B              LD      E,E                 
8FAF: C9              RET                         
8FB0: B9              CP      C                   
8FB1: D6 15           SUB     $15                 
8FB3: 53              LD      D,E                 
8FB4: 17              RLA                         
8FB5: 6E              LD      L,(HL)              
8FB6: DF              RST     0X18                
8FB7: 6A              LD      L,D                 
8FB8: 13              INC     DE                  
8FB9: 05              DEC     B                   
8FBA: 3F              CCF                         
8FBB: 9E              SBC     (HL)                
8FBC: 61              LD      H,C                 
8FBD: D2 B5 23        JP      NC,$23B5            
8FC0: 62              LD      H,D                 
8FC1: 0E 6C           LD      C,$6C               
8FC3: 80              ADD     A,B                 
8FC4: 8D              ADC     A,L                 
8FC5: 63              LD      H,E                 
8FC6: F4 96 77        CALL    P,$7796             ; {}
8FC9: AF              XOR     A                   
8FCA: 14              INC     D                   
8FCB: 16 BC           LD      D,$BC               
8FCD: F4 72 A5        CALL    P,$A572             ; {}
8FD0: 5E              LD      E,(HL)              
8FD1: 99              SBC     C                   
8FD2: 16 73           LD      D,$73               
8FD4: 15              DEC     D                   
8FD5: CE B5           ADC     $B5                 
8FD7: 5E              LD      E,(HL)              
8FD8: 60              LD      H,B                 
8FD9: 2E 02           LD      L,$02               
8FDB: 06 15           LD      B,$15               
8FDD: 6C              LD      L,H                 
8FDE: EF              RST     0X28                
8FDF: 16 D3           LD      D,$D3               
8FE1: 93              SUB     E                   
8FE2: 29              ADD     HL,HL               
8FE3: 0D              DEC     C                   
8FE4: 2B              DEC     HL                  
8FE5: 60              LD      H,B                 
8FE6: 88              ADC     A,B                 
8FE7: 07              RLCA                        
8FE8: 01 BA 02        LD      BC,$02BA            
8FEB: 05              DEC     B                   
8FEC: 46              LD      B,(HL)              
8FED: A4              AND     H                   
8FEE: 75              LD      (HL),L              
8FEF: 8D              ADC     A,L                 
8FF0: 4B              LD      C,E                 
8FF1: 31 5D 83        LD      SP,$835D            
8FF4: 01 A4 03        LD      BC,$03A4            

8FF7: 10 
8FF8: 04 0E                         ; PRINT, Length: 0x000E
;
; THERE IS A JACK HERE.
;
8FFA:    5F BE 5B B1 4B 7B 4C 45 DD 46 9F 15 7F B1 ; 

9008: 07                            ; PRINT ROOM DESCRIPTION
;  
9009: 3E                            ; ??Attribute 3E??
900A: 0D 3C                         ; WHILE PASS, Length: 0x003C
900C:    0A 08                      ;   IS INPUT PHRASE, Phrase number: 0x08
900E:    04 15                      ;   PRINT, Length: 0x0015
;
; "JACK-O-MATIC DELUXE MODEL 333"
;
9010:    2B 1C AD 54 1F A2 83 49 C6 51 4F 61 DB D6 B6 93 ; 
9020:    33 61 1A 40 22             ; 
9025: 25 04    
9027: 20 2B           JR      NZ,$9054            ; {}
9029: 1C              INC     E                   
902A: 8B              ADC     A,E                 
902B: 54              LD      D,H                 
902C: 57              LD      D,A                 
902D: C6 D0           ADD     $D0                 
902F: 15              DEC     D                   
9030: 3F              CCF                         
9031: 3F              CCF                         
9032: 3F              CCF                         
9033: 3F              CCF                         
9034: 3F              CCF                         
9035: 35              DEC     (HL)                
9036: 3F              CCF                         
9037: 3F              CCF                         
9038: 3F              CCF                         
9039: 3F              CCF                         
903A: 3F              CCF                         
903B: 3F              CCF                         
903C: 23              INC     HL                  
903D: 3F              CCF                         
903E: 3F              CCF                         
903F: 3F              CCF                         
9040: 3F              CCF                         
9041: 3F              CCF                         
9042: 3F              CCF                         
9043: 3F              CCF                         
9044: 3F              CCF                         
9045: 3F              CCF                         
9046: 3F              CCF                         
9047: 3F              CCF                         
9048: 3F              CCF                         
9049: 3F              CCF                         
904A: 3F              CCF                         
904B: 3F              CCF                         
904C: 3F              CCF                         
904D: 3F              CCF                         
904E: 3F              CCF                         
904F: 3F              CCF                         
9050: 3F              CCF                         
9051: 3F              CCF                         
9052: 07              RLCA                        
9053: 00              NOP                         
9054: 00              NOP                         
9055: 00              NOP                         
9056: 00              NOP                         
9057: 00              NOP                         
9058: 00              NOP                         
9059: 00              NOP                         
905A: 00              NOP                         
905B: 00              NOP                         
905C: 00              NOP                         
905D: 00              NOP                         
905E: 00              NOP                         
905F: 00              NOP                         
9060: 00              NOP                         
9061: 00              NOP                         
9062: 00              NOP                         
9063: 00              NOP                         
9064: 00              NOP                         
9065: 00              NOP                         
9066: 00              NOP                         
9067: 00              NOP                         
9068: 00              NOP                         
9069: 00              NOP                         
906A: 00              NOP                         
906B: 00              NOP                         
906C: 00              NOP                         
906D: 00              NOP                         
906E: 00              NOP                         
906F: 00              NOP                         
9070: 00              NOP                         
9071: 00              NOP                         
9072: 00              NOP                         
9073: 00              NOP                         
9074: 00              NOP                         
9075: 00              NOP                         
9076: 00              NOP                         
9077: 00              NOP                         
9078: 00              NOP                         
9079: 00              NOP                         
907A: 00              NOP                         
907B: 00              NOP                         
907C: 00              NOP                         
907D: 00              NOP                         
907E: 00              NOP                         
907F: 00              NOP                         
9080: 00              NOP                         
9081: 00              NOP                         
9082: 00              NOP                         
9083: 00              NOP                         
9084: 00              NOP                         
9085: 00              NOP                         
9086: 00              NOP                         
9087: 00              NOP                         
9088: 00              NOP                         
9089: 00              NOP                         
908A: 00              NOP                         
908B: 00              NOP                         
908C: 00              NOP                         
908D: 00              NOP                         
908E: 00              NOP                         
908F: 00              NOP                         
9090: 00              NOP                         
9091: 00              NOP                         
9092: 00              NOP                         
9093: 00              NOP                         
9094: 00              NOP                         
9095: 00              NOP                         
9096: 00              NOP                         
9097: 00              NOP                         
9098: 00              NOP                         
9099: 00              NOP                         
909A: 00              NOP                         
909B: 00              NOP                         
909C: 00              NOP                         
909D: 00              NOP                         
909E: 00              NOP                         
909F: 00              NOP                         
90A0: 00              NOP                         
90A1: 00              NOP                         
90A2: 00              NOP                         
90A3: 00              NOP                         
90A4: 00              NOP                         
90A5: 00              NOP                         
90A6: 00              NOP                         
90A7: 00              NOP                         
90A8: 00              NOP                         
90A9: 00              NOP                         
90AA: 00              NOP                         
90AB: 00              NOP                         
90AC: 00              NOP                         
90AD: 00              NOP                         
90AE: 00              NOP                         
90AF: 00              NOP                         
90B0: 00              NOP                         
90B1: 00              NOP                         
90B2: 00              NOP                         
90B3: 00              NOP                         
90B4: 00              NOP                         
90B5: 00              NOP                         
90B6: 00              NOP                         
90B7: 00              NOP                         
90B8: 00              NOP                         
90B9: 00              NOP                         
90BA: 00              NOP                         
90BB: 00              NOP                         
90BC: 00              NOP                         
90BD: 00              NOP                         
90BE: 00              NOP                         
90BF: 00              NOP                         
90C0: 00              NOP                         
90C1: 00              NOP                         
90C2: 00              NOP                         
90C3: 00              NOP                         
90C4: 00              NOP                         
90C5: 00              NOP                         
90C6: 00              NOP                         
90C7: 00              NOP                         
90C8: 00              NOP                         
90C9: 00              NOP                         
90CA: 00              NOP                         
90CB: 00              NOP                         
90CC: 00              NOP                         
90CD: 00              NOP                         
90CE: 00              NOP                         
90CF: 00              NOP                         
90D0: 00              NOP                         
90D1: 00              NOP                         
90D2: 00              NOP                         
90D3: 00              NOP                         
90D4: 00              NOP                         
90D5: 00              NOP                         
90D6: 00              NOP                         
90D7: 00              NOP                         
90D8: 00              NOP                         
90D9: 00              NOP                         
90DA: 00              NOP                         
90DB: 00              NOP                         
90DC: 00              NOP                         
90DD: 00              NOP                         
90DE: 00              NOP                         
90DF: 00              NOP                         
90E0: 00              NOP                         
90E1: 00              NOP                         
90E2: 00              NOP                         
90E3: 00              NOP                         
90E4: 00              NOP                         
90E5: 00              NOP                         
90E6: 00              NOP                         
90E7: 00              NOP                         
90E8: 00              NOP                         
90E9: 00              NOP                         
90EA: 00              NOP                         
90EB: 00              NOP                         
90EC: 00              NOP                         
90ED: 00              NOP                         
90EE: 00              NOP                         
90EF: 00              NOP                         
90F0: 00              NOP                         
90F1: 00              NOP                         
90F2: 00              NOP                         
90F3: 00              NOP                         
90F4: 00              NOP                         
90F5: 00              NOP                         
90F6: 00              NOP                         
90F7: 00              NOP                         
90F8: 00              NOP                         
90F9: 00              NOP                         
90FA: 00              NOP                         
90FB: 00              NOP                         
90FC: 00              NOP                         

90FD: 00              NOP                         
90FE: D3 8F           OUT     ($8F),A             
9100: 93              SUB     E                   
9101: 33              INC     SP                  
9102: 98              SBC     B                   
9103: C3 9E 10        JP      $109E               
9106: B7              OR      A                   
9107: 44              LD      B,H                 
9108: 56              LD      D,(HL)              
9109: 5F              LD      E,A                 
910A: AA              XOR     D                   
910B: 04              INC     B                   
910C: 84              ADD     A,H                 
910D: 07              RLCA                        
910E: 55              LD      D,L                 
910F: 0D              DEC     C                   
9110: 53              LD      D,E                 
9111: 0A              LD      A,(BC)              
9112: 08              EX      AF,AF'              
9113: 04 4F                         ; PRINT, Length: 0x004F
;
; "WARNING, IN CASE OF TORNADO ALL HOTEL GUESTS SHOULD MEET AT THE WEST SIDE OF THE SALOON AND ENTER THE STORM SHELTER."
;
9115:    33 1E D3 B2 CE 98 D0 15 D3 14 9B B7 C3 9E 84 BF ; 
9125:    C6 97 C3 9C F3 8C 86 74 33 61 27 6F 0D BA 5A 17 ; 
9135:    2E A1 0F 58 36 60 96 14 82 17 59 5E 66 62 5B 17 ; 
9145:    DB 59 C3 9E 5F BE 53 17 81 8D 83 96 33 98 9E 61 ; 
9155:    23 62 5F BE 66 17 B7 A0 5A 17 4E 61 47 62 22 ; 
9164: 02 03       
9166: 49              LD      C,C                 
9167: B8              CP      B                   
9168: 4E              LD      C,(HL)              
9169: 56              LD      D,(HL)              
916A: 2A 81 01        LD      HL,($0181)          
916D: 84              ADD     A,H                 
916E: 07              RLCA                        
916F: 1E 0D           LD      E,$0D               
9171: 1C              INC     E                   
9172: 0A              LD      A,(BC)              
9173: 08              EX      AF,AF'              
9174: 04 18                         ; PRINT, Length: 0x0018
;
; "LAST CHANCE, NEXT GAS SIXTY MILES."
;
9176:    7B 1C F3 B9 1B 54 17 98 10 EE 2E 63 73 15 D5 B5 ; 
9186:    2E 7C 4F DB 3F 7A 5C BB    ; 
918E: 02              LD      (BC),A              
918F: 05              DEC     B                   
9190: 35              DEC     (HL)                
9191: 92              SUB     D                   
9192: 09              ADD     HL,BC               
9193: B7              OR      A                   
9194: 45              LD      B,L                 
9195: 56              LD      D,(HL)              
9196: 17              RLA                         
9197: 96              SUB     (HL)                
9198: 03              INC     BC                  
9199: 84              ADD     A,H                 
919A: 07              RLCA                        
919B: 0A              LD      A,(BC)              
919C: 0D              DEC     C                   
919D: 08              EX      AF,AF'              
919E: 0A              LD      A,(BC)              
919F: 08              EX      AF,AF'              
91A0: 04              INC     B                   
91A1: 04              INC     B                   
91A2: EB              EX      DE,HL               
91A3: 1A              LD      A,(DE)              
91A4: A3              AND     E                   
91A5: AF              XOR     A                   
91A6: 02              LD      (BC),A              
91A7: 06 71           LD      B,$71               
91A9: 98              SBC     B                   
91AA: 95              SUB     L                   
91AB: 96              SUB     (HL)                
91AC: 80              ADD     A,B                 
91AD: 79              LD      A,C                 
91AE: 58              LD      E,B                 
91AF: 0B              DEC     BC                  
91B0: A6              AND     (HL)                
91B1: 03              INC     BC                  
91B2: 8A              ADC     A,D                 
91B3: 02              LD      (BC),A              
91B4: 06 17           LD      B,$17               
91B6: 49              LD      C,C                 
91B7: 33              INC     SP                  
91B8: 49              LD      C,C                 
91B9: 5B              LD      E,E                 
91BA: C5              PUSH    BC                  
91BB: 54              LD      D,H                 
91BC: 26 00           LD      H,$00               
91BE: 05              DEC     B                   
91BF: 80              ADD     A,B                 
91C0: 03              INC     BC                  
91C1: 21 
91C2: 04 1F                         ; PRINT, Length: 0x001F
;
; THE ENTRANCE TO THE SHIP HAS BEEN BLOWN CLEAR.
;
91C4:    5F BE 30 15 EB BF 17 98 89 17 82 17 55 5E 92 73 ; 
91D4:    9B 15 C4 B5 30 60 B6 14 80 A1 DE 14 94 5F 2E ; 
91E3: 56          
91E4: 18 89           JR      $916F               ; {}
91E6: 01 84 07        LD      BC,$0784            
91E9: 0E 0D           LD      C,$0D               
91EB: 0C              INC     C                   
91EC: 0A              LD      A,(BC)              
91ED: 08              EX      AF,AF'              
91EE: 04 08                         ; PRINT, Length: 0x0008
;
; "CITY LIMIT"
;
91F0:    1B 1B FB C0 8F 8C 74 7B    ; 
91F8: 02              LD      (BC),A              
91F9: 03              INC     BC                  
91FA: 49              LD      C,C                 
91FB: B8              CP      B                   
91FC: 4E              LD      C,(HL)              
91FD: 1F              RRA                         
91FE: 2C              INC     L                   
91FF: 01 00 C0        LD      BC,$C000            
9202: 02              LD      (BC),A              
9203: 09              ADD     HL,BC               
9204: 4B              LD      C,E                 
9205: A4              AND     H                   
9206: 91              SUB     C                   
9207: AF              XOR     A                   
9208: 8A              ADC     A,D                 
9209: 64              LD      H,H                 
920A: 8E              ADC     A,(HL)              
920B: 48              LD      C,B                 
920C: 53              LD      D,E                 
920D: 07              RLCA                        
920E: 1C              INC     E                   
920F: 0D              DEC     C                   
9210: 1A              LD      A,(DE)              
9211: 0A              LD      A,(BC)              
9212: 06 
9213: 04 16                         ; PRINT, Length: 0x0016
;
; YOU LOWER YOUR HANDS IN DISGUST. 
;
9215:    C7 DE 49 16 B4 D0 51 18 23 C6 50 72 0B 5C 83 7A ; 
9225:    95 5A 35 6F 9B C1          ; 
922B: 59              LD      E,C                 
922C: 47              LD      B,A                 
922D: 8F              ADC     A,A                 
922E: 02              LD      (BC),A              
922F: 80              ADD     A,B                 
9230: 07              RLCA                        
9231: 37              SCF                         
9232: 0D              DEC     C                   
9233: 35              DEC     (HL)                
9234: 0E 04           LD      C,$04               
9236: 0A              LD      A,(BC)              
9237: 10 0A           DJNZ    $9243               ; {}
9239: 0B              DEC     BC                  
923A: 04 2D                         ; PRINT, Length: 0x002D
;
; LOOKING IN THE WINDOW, YOU CAN BARELY SEE A DESK AND A GUN CABINET.
;
923C:    81 8D 50 86 CB 6A 96 96 DB 72 50 D1 89 5B 1B EE ; 
924C:    1B A1 10 53 AB 14 6E B1 55 DB 1B 60 46 45 5D 62 ; 
925C:    90 14 03 58 87 15 85 96 B3 46 76 98 2E ; 
9269: 02 
926A: 09              ADD     HL,BC               
926B: D4 4C 66        CALL    NC,$664C            ; {}
926E: B1              OR      C                   
926F: FB              EI                          
9270: 17              RLA                         
9271: 49              LD      C,C                 
9272: 98              SBC     B                   
9273: 57              LD      D,A                 
9274: 59              LD      E,C                 
9275: 3A 8E 02        LD      A,($028E)           
9278: 80              ADD     A,B                 
9279: 07              RLCA                        
927A: 2A 0D 28        LD      HL,($280D)          
927D: 0E 04           LD      C,$04               
927F: 0A              LD      A,(BC)              
9280: 10 0A           DJNZ    $928C               ; {}
9282: 0B              DEC     BC                  
9283: 04 20                         ; PRINT, Length: 0x0020
;
; YOU SEE EMPTY DESERT STRETCHING TO THE HORIZON. 
;
9285:    C7 DE 57 17 47 5E EE 93 46 DB 57 62 B3 B3 0C BA ; 
9295:    7D 62 90 73 D6 6A D6 9C DB 72 84 74 79 7C 1B 9C ;  
92A5: 02              LD      (BC),A              
92A6: 09              ADD     HL,BC               
92A7: D4 4C 66        CALL    NC,$664C            ; {}
92AA: B1              OR      C                   
92AB: FB              EI                          
92AC: 17              RLA                         
92AD: 49              LD      C,C                 
92AE: 98              SBC     B                   
92AF: 57              LD      D,A                 
92B0: 5A              LD      E,D                 
92B1: 0D              DEC     C                   
92B2: A0              AND     B                   
92B3: 02              LD      (BC),A              
92B4: 80              ADD     A,B                 
92B5: 07              RLCA                        
92B6: 01 BB 02        LD      BC,$02BB            
92B9: 05              DEC     B                   
92BA: 1F              RRA                         
92BB: B8              CP      B                   
92BC: 3F              CCF                         
92BD: 8E              ADC     A,(HL)              
92BE: 52              LD      D,D                 
92BF: 5A              LD      E,D                 
92C0: 0D              DEC     C                   
92C1: DB 02           IN      A,($02)             
92C3: 80              ADD     A,B                 
92C4: 07              RLCA                        
92C5: 01 BB 02        LD      BC,$02BB            
92C8: 05              DEC     B                   
92C9: 1F              RRA                         
92CA: B8              CP      B                   
92CB: 3F              CCF                         
92CC: 8E              ADC     A,(HL)              
92CD: 52              LD      D,D                 
92CE: 2B              DEC     HL                  
92CF: 09              ADD     HL,BC               
92D0: 01 00 80        LD      BC,$8000            
92D3: 02              LD      (BC),A              
92D4: 04              INC     B                   
92D5: B9              CP      C                   
92D6: 6E              LD      L,(HL)              
92D7: 8E              ADC     A,(HL)              
92D8: C5              PUSH    BC                  
92D9: 5B              LD      E,E                 
92DA: 85              ADD     A,L                 
92DB: 24              INC     H                   
92DC: C3 05 90        JP      $9005               ; {}
92DF: 03              INC     BC                  
92E0: 01 BD 09        LD      BC,$09BD            
92E3: 02              LD      (BC),A              
92E4: 14              INC     D                   
92E5: 14              INC     D                   
92E6: 0A              LD      A,(BC)              
92E7: 33              INC     SP                  
92E8: 0D              DEC     C                   
92E9: 31 1F 28        LD      SP,$281F            
92EC: 5F              LD      E,A                 
92ED: BE              CP      (HL)                
92EE: 8E              ADC     A,(HL)              
92EF: 14              INC     D                   
92F0: 30 79           JR      NC,$936B            ; {}
92F2: 03              INC     BC                  
92F3: 15              DEC     D                   
92F4: 4B              LD      C,E                 
92F5: 62              LD      H,D                 
92F6: 8E              ADC     A,(HL)              
92F7: 48              LD      C,B                 
92F8: 2B              DEC     HL                  
92F9: 17              RLA                         
92FA: 86              ADD     A,(HL)              
92FB: A5              AND     L                   
92FC: FB              EI                          
92FD: 8E              ADC     A,(HL)              
92FE: E5              PUSH    HL                  
92FF: 59              LD      E,C                 
9300: 55              LD      D,L                 
9301: 4A              LD      C,D                 
9302: 89              ADC     A,C                 
9303: 17              RLA                         
9304: 0F              RRCA                        
9305: 15              DEC     D                   
9306: F3              DI                          
9307: B9              CP      C                   
9308: 68              LD      L,B                 
9309: 4D              LD      C,L                 
930A: AF              XOR     A                   
930B: A0              AND     B                   
930C: 51              LD      D,C                 
930D: 18 23           JR      $9332               ; {}
930F: C6 47           ADD     $47                 
9311: 63              LD      H,E                 
9312: 5B              LD      E,E                 
9313: BB              CP      E                   
9314: 17              RLA                         
9315: 62              LD      H,D                 
9316: C3 1C 62        JP      $621C               ; {}
9319: 23              INC     HL                  
931A: 4B              LD      C,E                 
931B: 07              RLCA                        
931C: 82              ADD     A,D                 
931D: DE 0D           SBC     $0D                 
931F: 82              ADD     A,D                 
9320: DB 0A           IN      A,($0A)             
9322: 09              ADD     HL,BC               
9323: 0E 82           LD      C,$82               
9325: D6 0D           SUB     $0D                 
9327: 81              ADD     A,C                 
9328: 65              LD      H,L                 
9329: 09              ADD     HL,BC               
932A: 5C              LD      E,H                 
932B: 0B              DEC     BC                  
932C: 81              ADD     A,C                 
932D: 60              LD      H,B                 
932E: 05              DEC     B                   
932F: 26 44           LD      H,$44               
9331: 0D              DEC     C                   
9332: 42              LD      B,D                 
9333: 04 3C                         ; PRINT, Length: 0x003C
;
; THE ALIEN STAGGERS BACK AS YOUR FISTS POUND INTO ITS FACE, GREEN ICHOR COVERS YOUR HANDS! 
;
9335:    5F BE 8E 14 30 79 66 17 79 47 3D 62 AB 14 8B 54 ; 
9345:    4B 49 C7 DE 88 AF 66 7B D2 B5 30 A1 0B 58 C9 9A ; 
9355:    D6 15 C8 B5 D7 46 09 EE 67 B1 8B 96 29 54 85 AF ; 
9365:    4F A1 8B B3 C7 DE 8A AF 8E 48 6B B5 ; 
9371: 1C              INC     E                   
9372: 62              LD      H,D                 
9373: 1D              DEC     E                   
9374: 09              ADD     HL,BC               
9375: 5A              LD      E,D                 
9376: 3E 0D           LD      A,$0D               
9378: 3C              INC     A                   
9379: 04 36                         ; PRINT, Length: 0x0036
;
; THE ALIEN IS SENT REELING BY A WELL PLACED KICK. YOU FEEL BONES CRUNCH WITHIN IT!
;
937B:    5F BE 8E 14 30 79 D5 15 57 17 B3 9A 67 B1 90 8C ; 
938B:    C4 6A 43 DB F7 17 F3 8C FB A5 A6 53 1B 16 AF 54 ; 
939B:    51 18 48 C2 2E 60 B9 14 75 98 E4 14 8D C5 19 71 ; 
93AB:    82 7B 83 7A 71 7B          ; 
93B1: 1C              INC     E                   
93B2: 62              LD      H,D                 
93B3: 1D              DEC     E                   
93B4: 06 8D           LD      B,$8D               
93B6: 54              LD      D,H                 
93B7: 0D              DEC     C                   
93B8: 52              LD      D,D                 
93B9: 04              INC     B                   
93BA: 4C              LD      C,H                 
93BB: 5F              LD      E,A                 
93BC: BE              CP      (HL)                
93BD: 5A              LD      E,D                 
93BE: 17              RLA                         
93BF: 79              LD      A,C                 
93C0: 47              LD      B,A                 
93C1: 44              LD      B,H                 
93C2: DB 09           IN      A,($09)             
93C4: B3              OR      E                   
93C5: 88              ADC     A,B                 
93C6: 96              SUB     (HL)                
93C7: 23              INC     HL                  
93C8: C6 58           ADD     $58                 
93CA: 6D              LD      L,L                 
93CB: 4B              LD      C,E                 
93CC: 62              LD      H,D                 
93CD: C7              RST     0X00                
93CE: DE 7B           SBC     $7B                 
93D0: 14              INC     D                   
93D1: 14              INC     D                   
93D2: 67              LD      H,A                 
93D3: 49              LD      C,C                 
93D4: 90              SUB     B                   
93D5: 12              LD      (DE),A              
93D6: B2              OR      D                   
93D7: 95              SUB     L                   
93D8: 14              INC     D                   
93D9: 51              LD      D,C                 
93DA: 18 4A           JR      $9426               ; {}
93DC: C2 55 9F        JP      NZ,$9F55            ; {}
93DF: 16 BC           LD      D,$BC               
93E1: DB 72           IN      A,($72)             
93E3: 43              LD      B,E                 
93E4: 48              LD      C,B                 
93E5: 83              ADD     A,E                 
93E6: 61              LD      H,C                 
93E7: 4F              LD      C,A                 
93E8: A1              AND     C                   
93E9: 9B              SBC     E                   
93EA: AF              XOR     A                   
93EB: 34              INC     (HL)                
93EC: A1              AND     C                   
93ED: 9F              SBC     A                   
93EE: 15              DEC     D                   
93EF: F3              DI                          
93F0: 46              LD      B,(HL)              
93F1: 8E              ADC     A,(HL)              
93F2: 48              LD      C,B                 
93F3: 5F              LD      E,A                 
93F4: 17              RLA                         
93F5: 5A              LD      E,D                 
93F6: 49              LD      C,C                 
93F7: A3              AND     E                   
93F8: 15              DEC     D                   
93F9: 43              LD      B,E                 
93FA: 90              SUB     B                   
93FB: 0B              DEC     BC                  
93FC: 6C              LD      L,H                 
93FD: A6              AND     (HL)                
93FE: 9A              SBC     D                   
93FF: 82              ADD     A,D                 
9400: 17              RLA                         
9401: 49              LD      C,C                 
9402: 5E              LD      E,(HL)              
9403: 07              RLCA                        
9404: B3              OR      E                   
9405: 31 98 1C        LD      SP,$1C98            
9408: 62              LD      H,D                 
9409: 1D              DEC     E                   
940A: 04              INC     B                   
940B: B3              OR      E                   
940C: 2B              DEC     HL                  
940D: 04 29                         ; PRINT, Length: 0x0029
;
; YOUR SWING MISSES THE ALIEN AND YOU ALMOST LOSE YOUR BALANCE.
;
940F:    C7 DE 95 AF 50 D1 CF 6A 65 7B 4B 62 5F BE 8E 14 ; 
941F:    30 79 90 14 1B 58 1B A1 47 48 E6 A0 49 16 9B B7 ; 
942F:    C7 DE 84 AF 3B 48 17 98 2E ; 
9438: D9     
9439: 2B              DEC     HL                  
943A: 04 29                         ; PRINT, Length: 0x0029
;
; THE ALIEN BLOCKS YOUR BLOWS WITH HIS ARMS AND RUSHES FORWARD.
;
943C:    5F BE 8E 14 30 79 B6 14 5D 9E DB B5 34 A1 B6 14 ; 
944C:    85 A1 FB 17 53 BE 95 73 94 14 4B 94 8E 48 3F 17 ; 
945C:    1F B8 C8 B5 C1 A0 2E 49 2E ; 
9465: FF              
9466: 27              DAA                         
9467: 04              INC     B                   
9468: 25              DEC     H                   
9469: 5F              LD      E,A                 
946A: BE              CP      (HL)                
946B: 8E              ADC     A,(HL)              
946C: 14              INC     D                   
946D: 30 79           JR      NC,$94E8            ; {}
946F: 0F              RRCA                        
9470: 15              DEC     D                   
9471: A5              AND     L                   
9472: 54              LD      D,H                 
9473: B0              OR      B                   
9474: 17              RLA                         
9475: F4 59 7B        CALL    P,$7B59             ; {}
9478: 14              INC     D                   
9479: 4E              LD      C,(HL)              
947A: D1              POP     DE                  
947B: 0D              DEC     C                   
947C: 58              LD      E,B                 
947D: DD ; ????
947E: 78              LD      A,B                 
947F: 5B              LD      E,E                 
9480: F4 1B A1        CALL    P,$A11B             ; {}
9483: 65              LD      H,L                 
9484: B1              OR      C                   
9485: 4F              LD      C,A                 
9486: A1              AND     C                   
9487: 93              SUB     E                   
9488: AF              XOR     A                   
9489: C5              PUSH    BC                  
948A: C4 D3 86        CALL    NZ,$86D3            ; {}
948D: 2E 0D           LD      L,$0D               
948F: 81              ADD     A,C                 
9490: 6B              LD      L,E                 
9491: 0E 06           LD      C,$06               
9493: 09              ADD     HL,BC               
9494: 32 09 28        LD      ($2809),A           
9497: 09              ADD     HL,BC               
9498: 24              INC     H                   
9499: 0B              DEC     BC                  
949A: 81              ADD     A,C                 
949B: 60              LD      H,B                 
949C: 05              DEC     B                   
949D: 19              ADD     HL,DE               
949E: 3F              CCF                         
949F: 0D              DEC     C                   
94A0: 3D              DEC     A                   
94A1: 04              INC     B                   
94A2: 03              INC     BC                  
94A3: C7              RST     0X00                
94A4: DE 52           SBC     $52                 
94A6: 12              LD      (DE),A              
94A7: 04 31                         ; PRINT, Length: 0x0031
;
; SMASHES DOWN UPON THE HEAD OF THE ALIEN, GREEN ICHOR SPRAYS YOUR CLOTHES!
;
94A9:    E3 B8 1F B8 C6 B5 80 A1 B2 17 03 A0 5F BE 9F 15 ; 
94B9:    F3 46 C3 9E 5F BE 8E 14 30 79 09 EE 67 B1 8B 96 ; 
94C9:    29 54 95 AF EB A6 4B DF C7 DE 85 AF 86 8D F5 72 ; 
94D9:    21    
94DA: 1C 62            
94DC: 1D              DEC     E                   
94DD: 15              DEC     D                   
94DE: 3F              CCF                         
94DF: 53              LD      D,E                 
94E0: 0D              DEC     C                   
94E1: 51              LD      D,C                 
94E2: 04              INC     B                   
94E3: 03              INC     BC                  
94E4: C7              RST     0X00                
94E5: DE 52           SBC     $52                 
94E7: 12              LD      (DE),A              
94E8: 04              INC     B                   
94E9: 45              LD      B,L                 
94EA: 0C              INC     C                   
94EB: BA              CP      D                   
94EC: 17              RLA                         
94ED: 7A              LD      A,D                 
94EE: D6 B5           SUB     $B5                 
94F0: DB 72           IN      A,($72)             
94F2: 43              LD      B,E                 
94F3: 48              LD      C,B                 
94F4: 83              ADD     A,E                 
94F5: 61              LD      H,C                 
94F6: 83              ADD     A,E                 
94F7: 7A              LD      A,D                 
94F8: 8D              ADC     A,L                 
94F9: 7B              LD      A,E                 
94FA: 5B              LD      E,E                 
94FB: 17              RLA                         
94FC: FE 59           CP      $59                 
94FE: 51              LD      D,C                 
94FF: 18 48           JR      $9549               ; {}
9501: C2 2E 60        JP      NZ,$602E            ; {}
9504: B9              CP      C                   
9505: 14              INC     D                   
9506: 75              LD      (HL),L              
9507: 98              SBC     B                   
9508: E4 14 8D        CALL    PO,$8D14            ; {}
950B: C5              PUSH    BC                  
950C: 19              ADD     HL,DE               
950D: 71              LD      (HL),C              
950E: 82              ADD     A,D                 
950F: 7B              LD      A,E                 
9510: 83              ADD     A,E                 
9511: 7A              LD      A,D                 
9512: 97              SUB     A                   
9513: 7B              LD      A,E                 
9514: 82              ADD     A,D                 
9515: 17              RLA                         
9516: 43              LD      B,E                 
9517: 5E              LD      E,(HL)              
9518: 87              ADD     A,A                 
9519: 8C              ADC     A,H                 
951A: 95              SUB     L                   
951B: 96              SUB     (HL)                
951C: 04              INC     B                   
951D: 9A              SBC     D                   
951E: 0B              DEC     BC                  
951F: C0              RET     NZ                  
9520: 4F              LD      C,A                 
9521: 45              LD      B,L                 
9522: 66              LD      H,(HL)              
9523: 7B              LD      A,E                 
9524: B8              CP      B                   
9525: 16 84           LD      D,$84               
9527: 15              DEC     D                   
9528: 30 60           JR      NC,$958A            ; {}
952A: B6              OR      (HL)                
952B: 14              INC     D                   
952C: 36 A0           LD      (HL),$A0            
952E: 2E 1C           LD      L,$1C               
9530: 62              LD      H,D                 
9531: 1D              DEC     E                   
9532: 0B              DEC     BC                  
9533: 72              LD      (HL),D              
9534: 48              LD      C,B                 
9535: 0D              DEC     C                   
9536: 46              LD      B,(HL)              
9537: 04              INC     B                   
9538: 03              INC     BC                  
9539: C7              RST     0X00                
953A: DE 52           SBC     $52                 
953C: 12              LD      (DE),A              
953D: 04              INC     B                   
953E: 3A 96 73        LD      A,($7396)           ; {}
9541: D6 B5           SUB     $B5                 
9543: DB 72           IN      A,($72)             
9545: 43              LD      B,E                 
9546: 48              LD      C,B                 
9547: 85              ADD     A,L                 
9548: 61              LD      H,C                 
9549: C3 B5 9B        JP      $9BB5               ; {}
954C: B2              OR      D                   
954D: F4 4F 03        CALL    P,$034F             
9550: BA              CP      D                   
9551: AB              XOR     E                   
9552: 98              SBC     B                   
9553: 5F              LD      E,A                 
9554: BE              CP      (HL)                
9555: 56              LD      D,(HL)              
9556: 15              DEC     D                   
9557: 5A              LD      E,D                 
9558: 62              LD      H,D                 
9559: C2 16 A7        JP      NZ,$A716            ; {}
955C: 61              LD      H,C                 
955D: 84              ADD     A,H                 
955E: 15              DEC     D                   
955F: 30 60           JR      NC,$95C1            ; {}
9561: C5              PUSH    BC                  
9562: 15              DEC     D                   
9563: 84              ADD     A,H                 
9564: 74              LD      (HL),H              
9565: 56              LD      D,(HL)              
9566: 15              DEC     D                   
9567: 85              ADD     A,L                 
9568: A1              AND     C                   
9569: 5C              LD      E,H                 
956A: 15              DEC     D                   
956B: 2E 60           LD      L,$60               
956D: 48              LD      C,B                 
956E: DB FF           IN      A,($FF)             
9570: B2              OR      D                   
9571: 82              ADD     A,D                 
9572: 17              RLA                         
9573: 59              LD      E,C                 
9574: 5E              LD      E,(HL)              
9575: 30 A1           JR      NC,$9518            ; {}
9577: AB              XOR     E                   
9578: 57              LD      D,A                 
9579: 1C              INC     E                   
957A: 62              LD      H,D                 
957B: 1D              DEC     E                   
957C: 06 A5           LD      B,$A5               
957E: 25              DEC     H                   
957F: 0D              DEC     C                   
9580: 23              INC     HL                  
9581: 04              INC     B                   
9582: 03              INC     BC                  
9583: C7              RST     0X00                
9584: DE 52           SBC     $52                 
9586: 12              LD      (DE),A              
9587: 04              INC     B                   
9588: 1B              DEC     DE                  
9589: BB              CP      E                   
958A: 6D              LD      L,L                 
958B: 17              RLA                         
958C: 98              SBC     B                   
958D: CA B5 37        JP      Z,$37B5             
9590: 49              LD      C,C                 
9591: F5              PUSH    AF                  
9592: 8B              ADC     A,E                 
9593: D3 B8           OUT     ($B8),A             
9595: B8              CP      B                   
9596: 16 96           LD      D,$96               
9598: 64              LD      H,H                 
9599: DB 72           IN      A,($72)             
959B: 43              LD      B,E                 
959C: 48              LD      C,B                 
959D: 85              ADD     A,L                 
959E: 61              LD      H,C                 
959F: C4 B5 93        CALL    NZ,$93B5            ; {}
95A2: 9E              SBC     (HL)                
95A3: 2E CB           LD      L,$CB               
95A5: 26 0D           LD      H,$0D               
95A7: 24              INC     H                   
95A8: 04              INC     B                   
95A9: 03              INC     BC                  
95AA: C7              RST     0X00                
95AB: DE 52           SBC     $52                 
95AD: 12              LD      (DE),A              
95AE: 04              INC     B                   
95AF: 1C              INC     E                   
95B0: D5              PUSH    DE                  
95B1: 92              SUB     D                   
95B2: B5              OR      L                   
95B3: B7              OR      A                   
95B4: 82              ADD     A,D                 
95B5: 17              RLA                         
95B6: 43              LD      B,E                 
95B7: 5E              LD      E,(HL)              
95B8: 87              ADD     A,A                 
95B9: 8C              ADC     A,H                 
95BA: 83              ADD     A,E                 
95BB: 96              SUB     (HL)                
95BC: CB B5           RES     6,L                 
95BE: 16 BC           LD      D,$BC               
95C0: 55              LD      D,L                 
95C1: D1              POP     DE                  
95C2: 0B              DEC     BC                  
95C3: C0              RET     NZ                  
95C4: 6B              LD      L,E                 
95C5: BF              CP      A                   
95C6: 0F              RRCA                        
95C7: A0              AND     B                   
95C8: 5B              LD      E,E                 
95C9: 17              RLA                         
95CA: FF              RST     0X38                
95CB: 59              LD      E,C                 
95CC: FF              RST     0X38                
95CD: 2E 0D           LD      L,$0D               
95CF: 2C              INC     L                   
95D0: 04              INC     B                   
95D1: 23              INC     HL                  
95D2: 5F              LD      E,A                 
95D3: BE              CP      (HL)                
95D4: 8E              ADC     A,(HL)              
95D5: 14              INC     D                   
95D6: 30 79           JR      NC,$9651            ; {}
95D8: 30 15           JR      NC,$95EF            ; {}
95DA: 50              LD      D,B                 
95DB: BD              CP      L                   
95DC: BF              CP      A                   
95DD: 6D              LD      L,L                 
95DE: DB B5           IN      A,($B5)             
95E0: 34              INC     (HL)                
95E1: A1              AND     C                   
95E2: 94              SUB     H                   
95E3: 14              INC     D                   
95E4: 6E              LD      L,(HL)              
95E5: 94              SUB     H                   
95E6: EC 16 CF        CALL    PE,$CF16            
95E9: 62              LD      H,D                 
95EA: C3 9A AB        JP      $AB9A               ; {}
95ED: 98              SBC     B                   
95EE: 5F              LD      E,A                 
95EF: BE              CP      (HL)                
95F0: B5              OR      L                   
95F1: 17              RLA                         
95F2: 51              LD      D,C                 
95F3: 5E              LD      E,(HL)              
95F4: 46              LD      B,(HL)              
95F5: A9              XOR     C                   
95F6: 04              INC     B                   
95F7: 04              INC     B                   
95F8: 03              INC     BC                  
95F9: A0              AND     B                   
95FA: 97              SUB     A                   
95FB: 7B              LD      A,E                 
95FC: 08              EX      AF,AF'              
95FD: 81              ADD     A,C                 
95FE: F1              POP     AF                  
95FF: 0E 81           LD      C,$81               
9601: EE 0D           XOR     $0D                 
9603: 47              LD      B,A                 
9604: 14              INC     D                   
9605: 01 01 14        LD      BC,$1401            
9608: 03              INC     BC                  
9609: C3 62 14        JP      $1462               
960C: 0E 06           LD      C,$06               
960E: 03              INC     BC                  
960F: DB 01           IN      A,($01)             
9611: 03              INC     BC                  
9612: E8              RET     PE                  
9613: 01 0B 19        LD      BC,$190B            
9616: 0A              LD      A,(BC)              
9617: 04              INC     B                   
9618: 04              INC     B                   
9619: 21 04 00        LD      HL,$0004            
961C: 00              NOP                         
961D: 03              INC     BC                  
961E: 04              INC     B                   
961F: 21 03 00        LD      HL,$0003            
9622: 00              NOP                         
9623: 01 04 21        LD      BC,$2104            
9626: 01 00 00        LD      BC,$0000            
9629: 02              LD      (BC),A              
962A: 04              INC     B                   
962B: 21 02 00        LD      HL,$0002            
962E: 00              NOP                         
962F: 01 01 1F        LD      BC,$1F01            
9632: 18 3F           JR      $9673               ; {}
9634: B9              CP      C                   
9635: 82              ADD     A,D                 
9636: 62              LD      H,D                 
9637: 91              SUB     C                   
9638: 7A              LD      A,D                 
9639: 57              LD      D,A                 
963A: 17              RLA                         
963B: 75              LD      (HL),L              
963C: 61              LD      H,C                 
963D: 89              ADC     A,C                 
963E: 17              RLA                         
963F: AF              XOR     A                   
9640: 14              INC     D                   
9641: 59              LD      E,C                 
9642: 15              DEC     D                   
9643: 09              ADD     HL,BC               
9644: 8D              ADC     A,L                 
9645: 50              LD      D,B                 
9646: D1              POP     DE                  
9647: DB 6A           IN      A,($6A)             
9649: 3F              CCF                         
964A: A1              AND     C                   

964B: 0D 1E                         ; WHILE PASS, Length: 0x001E
964D:    14                         ;   EXECUTE AND REVERSE STATUS
964E:    01 01                      ;   IS IN PACK OR CURRENT ROOM, Object number: 0x01
9650:    05 26                      ;   IS LESS OR EQUAL TO LAST RANDOM, Value: 0x26
9652:    0E 08                      ;   WHILE FAIL, Length: 0x0008
9654:       0A 01                   ;     IS INPUT PHRASE, Phrase number: 0x01
9656:       0A 02                   ;     IS INPUT PHRASE, Phrase number: 0x02
9658:       0A 03                   ;     IS INPUT PHRASE, Phrase number: 0x03
965A:       0A 04                   ;     IS INPUT PHRASE, Phrase number: 0x04
965C:    14                         ;   EXECUTE AND REVERSE STATUS
965D:    0E 06                      ;   WHILE FAIL, Length: 0x0006
965F:       03 DB 01                ;     IS LOCATED, Room number: 0xDB, Object number: 0x01
9662:       03 E8 01                ;     IS LOCATED, Room number: 0xE8, Object number: 0x01
9665:    2C 01                      ;   SET ACTIVE, Object number: 0x01
9667:    1C 62                      ;   SET VAR OBJECT, Object number: 0x62
9669:    10                         ;   DROP VAR
966A:    BD                         ;   COMMAND 0xBD
966B: 14                            ; EXECUTE AND REVERSE STATUS
966C: 01 01                         ; IS IN PACK OR CURRENT ROOM, Object number: 0x01
966E: 0B 81 7F 05                   ; SWITCH, Length: 0x017F, Function to call: 0x05
9672:    19                         ;   Phrase number: 0x19
9673:    46                         ;   ELSE go to: 0x96BA
9674:       0D 44                   ;     WHILE PASS, Length: 0x0044
9676:          1F 3B                ;       PRINT, Length: 0x003B
;
; A WAVE OF BLINDING PAIN FLOODS THROUGH YOUR BODY AS RAZOR SHARP TEETH PIERCE YOUR FLESH!
;
9678:             59 45 CF 49 B8 16 B6 14 8E 7A 91 7A DB 16 83 7A ; 
9688:             89 67 8D 9E 82 17 07 B3 13 6D C7 DE 84 AF 93 9E ; 
9698:             95 14 2B 17 04 E5 5A 17 3A 49 7F 17 82 62 E3 16 ; 
96A8:             2D 62 5B 5E 34 A1 56 15 5A 62 21 ; 
96B3:          1C 01                ;       SET VAR OBJECT, Object number: 0x01
96B5:          1D 09                ;       ATTACK VAR, Points: 0x09
96B7:          17 91 01             ;       MOVE TO, Object number: 0x91, Destination room: 0x01
96BA:    34                         ;   Phrase number: 0x34
96BB:    34                         ;   ELSE go to: 0x96F0
96BC:       0D 32                   ;     WHILE PASS, Length: 0x0032
96BE:          1F 29                ;       PRINT, Length: 0x0029
;
; YOU FEEL A SEARING PAIN AS THE ALIEN'S CLAWS REND YOUR FLESH!
;
96C0:             C7 DE 4F 15 33 61 55 45 94 5F 91 7A DB 16 83 7A ; 
96D0:             4B 49 5F BE 8E 14 30 79 CB 23 BB 54 CB D2 70 B1 ; 
96E0:             1B 58 34 A1 56 15 5A 62 21 ; 
96E9:          1C 01                ;       SET VAR OBJECT, Object number: 0x01
96EB:          1D 06                ;       ATTACK VAR, Points: 0x06
96ED:          17 91 01             ;       MOVE TO, Object number: 0x91, Destination room: 0x01
96F0:    5A                         ;   Phrase number: 0x5A
96F1:    4C                         ;   ELSE go to: 0x973E
96F2:       0D 4A                   ;     WHILE PASS, Length: 0x004A
96F4:          1F 44                ;       PRINT, Length: 0x0044
;
; THE ALIEN GRAPPLES YOU! AS ITS SLIMY ARMS TRY TO CRUSH THE LIFE OUT OF YOU, YOUR RIBS BEGIN TO BEND...
;
96F6:             5F BE 8E 14 30 79 84 15 EA 48 F5 8B 51 18 EB C1 ; 
9706:             4B 49 8D 7B 5E 17 7B 7A 94 14 4B 94 03 C0 89 17 ; 
9716:             E4 14 5A C6 82 17 4E 5E 4F 79 C7 16 11 BC 9B 64 ; 
9726:             3E A1 51 18 23 C6 04 B2 C4 B5 7B 60 96 96 C4 9C ; 
9736:             8E 61 FF F9       ; 
973A:          1C 01                ;       SET VAR OBJECT, Object number: 0x01
973C:          1D 03                ;       ATTACK VAR, Points: 0x03
973E:    8D                         ;   Phrase number: 0x8D
973F:    43                         ;   ELSE go to: 0x9783
9740:       1F 41                   ;     PRINT, Length: 0x0041
;
; THE ALIEN'S SLAVERING TEETH PUSH FORWARD TOWARDS YOU, BUT YOU TWIST TO THE SIDE AND KICK IT BACK.
;
9742:          5F BE 8E 14 30 79 CB 23 BB B8 74 CA 91 7A 7F 17 ; 
9752:          82 62 EF 16 13 B8 04 68 14 D0 16 58 73 A1 4D B1 ; 
9762:          51 18 B3 C7 F6 4F 51 18 56 C2 55 D1 16 BC D6 9C ; 
9772:          DB 72 46 B8 43 5E 33 98 45 86 CB 83 04 BC DD 46 ; 
9782:          2E                   ; 
9783:    C0                         ;   Phrase number: 0xC0
9784:    3C                         ;   ELSE go to: 0x97C1
9785:       1F 3A                   ;     PRINT, Length: 0x003A
;
; THE ALIEN'S CLAWS RIP THROUGH YOUR CLOTHES. BUT BY JUMPING BACKWARDS YOU AVOID INJURY. 
;
9787:          5F BE 8E 14 30 79 CB 23 BB 54 CB D2 12 B2 82 17 ; 
9797:          07 B3 13 6D C7 DE 85 AF 86 8D F5 72 44 F4 73 C6 ; 
97A7:          7B 50 EF 81 90 A5 C4 6A DD 46 14 D0 0B 5C C7 DE ; 
97B7:          98 14 46 9F D0 15 F4 81 DB E0 ; 
97C1:    FF                         ;   Phrase number: 0xFF
97C2:    2D                         ;   ELSE go to: 0x97F0
97C3:       1F 2B                   ;     PRINT, Length: 0x002B
;
; THE ALIEN RUSHES PAST YOU IN ITS FRENZIED ATTEMPT TO ATTACK YOU.
;
97C5:          5F BE 8E 14 30 79 3F 17 1F B8 D2 B5 66 49 51 18 ; 
97D5:          4B C2 8B 96 0B C0 6F 68 B3 9B F3 5F 8E 49 72 61 ; 
97E5:          16 BC C3 9C 3B C0 8B 54 C7 DE 2E ; 
97F0: 02 0E 29                      ; IS OWNED BY, A=0x29, Object number: 0x0E
97F3: B8                            ; COMMAND 0xB8
97F4: B3                            ; COMMAND 0xB3
97F5: B3                            ; COMMAND 0xB3
97F6: 1B                            ; SET VAR TO SECOND NOUN
97F7: B8                            ; COMMAND 0xB8
97F8: 0B 6D E4                      ; SWITCH, Length: 0x006D, Function to call: 0xE4

97FB: 14 96      
97FD: 5F              LD      E,A                 
97FE: 2F              CPL                         
97FF: C6 5C           ADD     $5C                 
9801: 42              LD      B,D                 
9802: 65              LD      H,L                 
9803: 00              NOP                         
9804: A0              AND     B                   
9805: 03              INC     BC                  
9806: 27              DAA                         
9807: 04              INC     B                   
9808: 25              DEC     H                   
9809: 5F              LD      E,A                 
980A: BE              CP      (HL)                
980B: 5B              LD      E,E                 
980C: B1              OR      C                   
980D: 4B              LD      C,E                 
980E: 7B              LD      A,E                 
980F: 46              LD      B,(HL)              
9810: 45              LD      B,L                 
9811: 35              DEC     (HL)                
9812: 49              LD      C,C                 
9813: 84              ADD     A,H                 
9814: 15              DEC     D                   
9815: 3B              DEC     SP                  
9816: 63              LD      H,E                 
9817: C1              POP     BC                  
9818: C0              RET     NZ                  
9819: D0              RET     NC                  
981A: 15              DEC     D                   
981B: 13              INC     DE                  
981C: 54              LD      D,H                 
981D: 97              SUB     A                   
981E: B9              CP      C                   
981F: 2F              CPL                         
9820: 49              LD      C,C                 
9821: 67              LD      H,A                 
9822: 16 4E           LD      D,$4E               
9824: BD              CP      L                   
9825: CB 78           BIT     7,B                 
9827: 24              INC     H                   
9828: 56              LD      D,(HL)              
9829: 4A              LD      C,D                 
982A: 5E              LD      E,(HL)              
982B: 2F              CPL                         
982C: 62              LD      H,D                 
982D: 2E 01           LD      L,$01               
982F: 03              INC     BC                  
9830: 6C              LD      L,H                 
9831: 0F              RRCA                        
9832: 6D              LD      L,L                 
9833: 0C              INC     C                   
9834: 01 04 02        LD      BC,$0204            
9837: 0C              INC     C                   
9838: C1              POP     BC                  
9839: C0              RET     NZ                  
983A: D0              RET     NC                  
983B: 15              DEC     D                   
983C: 13              INC     DE                  
983D: 54              LD      D,H                 
983E: AF              XOR     A                   
983F: 6E              LD      L,(HL)              
9840: 45              LD      B,L                 
9841: DB AF           IN      A,($AF)             
9843: C3 5C 3B        JP      $3B5C               
9846: 00              NOP                         
9847: 00              NOP                         
9848: A0              AND     B                   
9849: 03              INC     BC                  
984A: 1F              RRA                         
984B: 04              INC     B                   
984C: 1D              DEC     E                   
984D: 5F              LD      E,A                 
984E: BE              CP      (HL)                
984F: 5B              LD      E,E                 
9850: B1              OR      C                   
9851: 4B              LD      C,E                 
9852: 7B              LD      A,E                 
9853: 59              LD      E,C                 
9854: 45              LD      B,L                 
9855: 96              SUB     (HL)                
9856: 73              LD      (HL),E              
9857: 56              LD      D,(HL)              
9858: 5E              LD      E,(HL)              
9859: 2B              DEC     HL                  
985A: D2 8D 7A        JP      NC,$7A8D            ; {}
985D: 15              DEC     D                   
985E: 71              LD      (HL),C              
985F: A3              AND     E                   
9860: AD              XOR     L                   
9861: 5B              LD      E,E                 
9862: B1              OR      C                   
9863: 24              INC     H                   
9864: 56              LD      D,(HL)              
9865: 4A              LD      C,D                 
9866: 5E              LD      E,(HL)              
9867: 2F              CPL                         
9868: 62              LD      H,D                 
9869: 2E 01           LD      L,$01               
986B: 03              INC     BC                  
986C: 60              LD      H,B                 
986D: 0F              RRCA                        
986E: 6D              LD      L,L                 
986F: 0C              INC     C                   
9870: 01 06 02        LD      BC,$0206            
9873: 0D              DEC     C                   
9874: C1              POP     BC                  
9875: C0              RET     NZ                  
9876: D0              RET     NC                  
9877: 15              DEC     D                   
9878: 13              INC     DE                  
9879: 54              LD      D,H                 
987A: 23              INC     HL                  
987B: D1              POP     DE                  
987C: DB BD           IN      A,($BD)             
987E: 24              INC     H                   
987F: 56              LD      D,(HL)              
9880: 45              LD      B,L                 
9881: 1A              LD      A,(DE)              
9882: 09              ADD     HL,BC               
9883: 86              ADD     A,(HL)              
9884: 08              EX      AF,AF'              
9885: 81              ADD     A,C                 
9886: 02              LD      (BC),A              
9887: 04              INC     B                   
9888: 44              LD      B,H                 
9889: BD              CP      L                   
988A: DB 8B           IN      A,($8B)             
988C: 2E 09           LD      L,$09               
988E: 86              ADD     A,(HL)              
988F: 08              EX      AF,AF'              
9890: 82              ADD     A,D                 
9891: 02              LD      (BC),A              
9892: 04              INC     B                   
9893: 65              LD      H,L                 
9894: B1              OR      C                   
9895: 65              LD      H,L                 
9896: 62              LD      H,D                 
9897: 2E 08           LD      L,$08               
9899: 80              ADD     A,B                 
989A: 07              RLCA                        
989B: 82              ADD     A,D                 
989C: 02              LD      (BC),A              
989D: 03              INC     BC                  
989E: 7E              LD      A,(HL)              
989F: 74              LD      (HL),H              
98A0: 45              LD      B,L                 
98A1: 2E 62           LD      L,$62               
98A3: 9E              SBC     (HL)                
98A4: 08              EX      AF,AF'              
98A5: 82              ADD     A,D                 
98A6: 06 58           LD      B,$58               
98A8: 0D              DEC     C                   
98A9: 56              LD      D,(HL)              
98AA: 0A              LD      A,(BC)              
98AB: 0F              RRCA                        
98AC: 08              EX      AF,AF'              
98AD: 64              LD      H,H                 
98AE: 04              INC     B                   
98AF: 4C              LD      C,H                 
98B0: 5F              LD      E,A                 
98B1: BE              CP      (HL)                
98B2: E7              RST     0X20                
98B3: 14              INC     D                   
98B4: 5B              LD      E,E                 
98B5: 4D              LD      C,L                 
98B6: 69              LD      L,C                 
98B7: 4D              LD      C,L                 
98B8: 9D              SBC     L                   
98B9: 7A              LD      A,D                 
98BA: 89              ADC     A,C                 
98BB: 17              RLA                         
98BC: 7E              LD      A,(HL)              
98BD: 15              DEC     D                   
98BE: 6B              LD      L,E                 
98BF: A1              AND     C                   
98C0: 73              LD      (HL),E              
98C1: 4F              LD      C,A                 
98C2: 2E 6D           LD      L,$6D               
98C4: 1F              RRA                         
98C5: 8F              ADC     A,A                 
98C6: 84              ADD     A,H                 
98C7: 14              INC     D                   
98C8: 4F              LD      C,A                 
98C9: A1              AND     C                   
98CA: 51              LD      D,C                 
98CB: 18 23           JR      $98F0               ; {}
98CD: C6 E3           ADD     $E3                 
98CF: 72              LD      (HL),D              
98D0: 03              INC     BC                  
98D1: 58              LD      E,B                 
98D2: 87              ADD     A,A                 
98D3: 96              SUB     (HL)                
98D4: 53              LD      D,E                 
98D5: B7              OR      A                   
98D6: DB A4           IN      A,($A4)             
98D8: 56              LD      D,(HL)              
98D9: 72              LD      (HL),D              
98DA: 13              INC     DE                  
98DB: 54              LD      D,H                 
98DC: 5F              LD      E,A                 
98DD: A0              AND     B                   
98DE: 8B              ADC     A,E                 
98DF: 9A              SBC     D                   
98E0: 8E              ADC     A,(HL)              
98E1: 48              LD      C,B                 
98E2: 90              SUB     B                   
98E3: 14              INC     D                   
98E4: 98              SBC     B                   
98E5: 14              INC     D                   
98E6: 3B              DEC     SP                  
98E7: 48              LD      C,B                 
98E8: 1A              LD      A,(DE)              
98E9: 98              SBC     B                   
98EA: 51              LD      D,C                 
98EB: 5E              LD      E,(HL)              
98EC: 84              ADD     A,H                 
98ED: 64              LD      H,H                 
98EE: 2E A1           LD      L,$A1               
98F0: F4 59 C5        CALL    P,$C559             
98F3: B5              OR      L                   
98F4: F5              PUSH    AF                  
98F5: B3              OR      E                   
98F6: F5              PUSH    AF                  
98F7: 72              LD      (HL),D              
98F8: 51              LD      D,C                 
98F9: 18 EB           JR      $98E6               ; {}
98FB: C1              POP     BC                  
98FC: 1C              INC     E                   
98FD: 01 1D 6E        LD      BC,$6E1D            
9900: 02              LD      (BC),A              
9901: 03              INC     BC                  
9902: 7E              LD      A,(HL)              
9903: 74              LD      (HL),H              
9904: 45              LD      B,L                 
9905: 5D              LD      E,L                 
9906: 0A              LD      A,(BC)              
9907: 82              ADD     A,D                 
9908: 07              RLCA                        
9909: 80              ADD     A,B                 
990A: 02              LD      (BC),A              
990B: 05              DEC     B                   
990C: 85              ADD     A,L                 
990D: A5              AND     L                   
990E: 74              LD      (HL),H              
990F: C0              RET     NZ                  
9910: 45              LD      B,L                 
9911: 5E              LD      E,(HL)              
9912: 80              ADD     A,B                 
9913: 82              ADD     A,D                 
9914: 85              ADD     A,L                 
9915: 87              ADD     A,A                 
9916: 8A              ADC     A,D                 
9917: 07              RLCA                        
9918: 71              LD      (HL),C              
9919: 0B              DEC     BC                  
991A: 6F              LD      L,A                 
991B: 0A              LD      A,(BC)              
991C: 11 01 C2        LD      DE,$C201            
991F: 40              LD      B,B                 
9920: 01 C2 36        LD      BC,$36C2            
9923: 35              DEC     (HL)                
9924: 0E 33           LD      C,$33               
9926: 0D              DEC     C                   
9927: 21 1B 14        LD      HL,$141B            
992A: 2E 20           LD      L,$20               
992C: 17              RLA                         
992D: 01 6A 04        LD      BC,$046A            
9930: 18 C7           JR      $98F9               ; {}
9932: DE 5E           SBC     $5E                 
9934: 17              RLA                         
9935: 7E              LD      A,(HL)              
9936: A1              AND     C                   
9937: 45              LD      B,L                 
9938: DB 8F           IN      A,($8F)             
993A: 8C              ADC     A,H                 
993B: 8B              ADC     A,E                 
993C: 4B              LD      C,E                 
993D: C9              RET                         
993E: 9A              SBC     D                   
993F: 82              ADD     A,D                 
9940: 17              RLA                         
9941: 45              LD      B,L                 
9942: 5E              LD      E,(HL)              
9943: 43              LD      B,E                 
9944: DE 3F           SBC     $3F                 
9946: 98              SBC     B                   
9947: 1B              DEC     DE                  
9948: B5              OR      L                   
9949: 0D              DEC     C                   
994A: 0E 1B           LD      C,$1B               
994C: 2E 20           LD      L,$20               
994E: 04              INC     B                   
994F: 09              ADD     HL,BC               
9950: 73              LD      (HL),E              
9951: 7B              LD      A,E                 
9952: 4B              LD      C,E                 
9953: 7B              LD      A,E                 
9954: C9              RET                         
9955: 54              LD      D,H                 
9956: A6              AND     (HL)                
9957: B7              OR      A                   
9958: 2E 37           LD      L,$37               
995A: 2F              CPL                         
995B: 0E 2D           LD      C,$2D               
995D: 0D              DEC     C                   
995E: 1B              DEC     DE                  
995F: 1B              DEC     DE                  
9960: 14              INC     D                   
9961: 2E 20           LD      L,$20               
9963: 1C              INC     E                   
9964: 01 10 04        LD      BC,$0410            
9967: 12              LD      (DE),A              
9968: C7              RST     0X00                
9969: DE 99           SBC     $99                 
996B: 16 D5           LD      D,$D5               
996D: CE 50           ADC     $50                 
996F: BD              CP      L                   
9970: 11 58 96        LD      DE,$9658            
9973: 96              SUB     (HL)                
9974: DB 72           IN      A,($72)             
9976: 89              ADC     A,C                 
9977: 67              LD      H,A                 
9978: C7              RST     0X00                
9979: A0              AND     B                   
997A: 0D              DEC     C                   
997B: 0E 1B           LD      C,$1B               
997D: 2E 20           LD      L,$20               
997F: 04              INC     B                   
9980: 09              ADD     HL,BC               
9981: 73              LD      (HL),E              
9982: 7B              LD      A,E                 
9983: 4B              LD      C,E                 
9984: 7B              LD      A,E                 
9985: C9              RET                         
9986: 54              LD      D,H                 
9987: A6              AND     (HL)                
9988: B7              OR      A                   
9989: 2E 02           LD      L,$02               
998B: 0A              LD      A,(BC)              
998C: BB              CP      E                   
998D: 6D              LD      L,L                 
998E: CB B9           RES     7,C                 
9990: CE 56           ADC     $56                 
9992: 8E              ADC     A,(HL)              
9993: 7A              LD      A,D                 
9994: 23              INC     HL                  
9995: 62              LD      H,D                 
9996: 4A              LD      C,D                 
9997: 53              LD      D,E                 
9998: 6A              LD      L,D                 
9999: 00              NOP                         
999A: 80              ADD     A,B                 
999B: 01 01 60        LD      BC,$6001            
999E: 07              RLCA                        
999F: 41              LD      B,C                 
99A0: 0D              DEC     C                   
99A1: 3F              CCF                         
99A2: 0A              LD      A,(BC)              
99A3: 12              LD      (DE),A              
99A4: 0E 3B           LD      C,$3B               
99A6: 0D              DEC     C                   
99A7: 1E 03           LD      E,$03               
99A9: 85              ADD     A,L                 
99AA: 6D              LD      L,L                 
99AB: 17              RLA                         
99AC: 6D              LD      L,L                 
99AD: 00              NOP                         
99AE: 04              INC     B                   
99AF: 16 C3           LD      D,$C3               
99B1: 54              LD      D,H                 
99B2: AF              XOR     A                   
99B3: 54              LD      D,H                 
99B4: 82              ADD     A,D                 
99B5: 17              RLA                         
99B6: 4E              LD      C,(HL)              
99B7: 5E              LD      E,(HL)              
99B8: 7A              LD      A,D                 
99B9: 79              LD      A,C                 
99BA: 0B              DEC     BC                  
99BB: C0              RET     NZ                  
99BC: 58              LD      E,B                 
99BD: 72              LD      (HL),D              
99BE: 49              LD      C,C                 
99BF: 5E              LD      E,(HL)              
99C0: 0F              RRCA                        
99C1: A0              AND     B                   
99C2: C7              RST     0X00                
99C3: 16 9B           LD      D,$9B               
99C5: C1              POP     BC                  
99C6: 0D              DEC     C                   
99C7: 19              ADD     HL,DE               
99C8: 03              INC     BC                  
99C9: 00              NOP                         
99CA: 6D              LD      L,L                 
99CB: 17              RLA                         
99CC: 6D              LD      L,L                 
99CD: 85              ADD     A,L                 
99CE: 04              INC     B                   
99CF: 11 C3 54        LD      DE,$54C3            
99D2: AF              XOR     A                   
99D3: 54              LD      D,H                 
99D4: 82              ADD     A,D                 
99D5: 17              RLA                         
99D6: 4E              LD      C,(HL)              
99D7: 5E              LD      E,(HL)              
99D8: 7A              LD      A,D                 
99D9: 79              LD      A,C                 
99DA: 14              INC     D                   
99DB: BC              CP      H                   
99DC: 8F              ADC     A,A                 
99DD: 62              LD      H,D                 
99DE: DD ; ????
99DF: B2              OR      D                   
99E0: 2E 02           LD      L,$02               
99E2: 08              EX      AF,AF'              
99E3: 23              INC     HL                  
99E4: D1              POP     DE                  
99E5: DB BD           IN      A,($BD)             
99E7: F6 4F           OR      $4F                 
99E9: 80              ADD     A,B                 
99EA: BF              CP      A                   
99EB: 4A              LD      C,D                 
99EC: 80              ADD     A,B                 
99ED: F2 6A 00        JP      P,$006A             
99F0: 80              ADD     A,B                 
99F1: 01 01 61        LD      BC,$6101            
99F4: 07              RLCA                        
99F5: 80              ADD     A,B                 
99F6: DE 0D           SBC     $0D                 
99F8: 80              ADD     A,B                 
99F9: DB 0A           IN      A,($0A)             
99FB: 12              LD      (DE),A              
99FC: 0E 80           LD      C,$80               
99FE: D6 0D           SUB     $0D                 
9A00: 80              ADD     A,B                 
9A01: 95              SUB     L                   
9A02: 03              INC     BC                  
9A03: 85              ADD     A,L                 
9A04: 01 04 80        LD      BC,$8004            
9A07: 8B              ADC     A,E                 
9A08: C3 54 AF        JP      $AF54               ; {}
9A0B: 54              LD      D,H                 
9A0C: 5A              LD      E,D                 
9A0D: 17              RLA                         
9A0E: 40              LD      B,B                 
9A0F: D2 6B 83        JP      NC,$836B            ; {}
9A12: C7              RST     0X00                
9A13: DE 99           SBC     $99                 
9A15: 16 85           LD      D,$85               
9A17: BE              CP      (HL)                
9A18: 56              LD      D,(HL)              
9A19: 5E              LD      E,(HL)              
9A1A: 56              LD      D,(HL)              
9A1B: 72              LD      (HL),D              
9A1C: 82              ADD     A,D                 
9A1D: 17              RLA                         
9A1E: 45              LD      B,L                 
9A1F: 5E              LD      E,(HL)              
9A20: E3              EX      (SP),HL             
9A21: 8B              ADC     A,E                 
9A22: 8E              ADC     A,(HL)              
9A23: AF              XOR     A                   
9A24: F3              DI                          
9A25: 78              LD      A,B                 
9A26: C3 9E 5F        JP      $5F9E               ; {}
9A29: BE              CP      (HL)                
9A2A: EB              EX      DE,HL               
9A2B: 14              INC     D                   
9A2C: 90              SUB     B                   
9A2D: 8C              ADC     A,H                 
9A2E: F4 59 9B        CALL    P,$9B59             ; {}
9A31: 15              DEC     D                   
9A32: C5              PUSH    BC                  
9A33: B5              OR      L                   
9A34: 85              ADD     A,L                 
9A35: 8D              ADC     A,L                 
9A36: 17              RLA                         
9A37: 60              LD      H,B                 
9A38: FA 17 3F        JP      M,$3F17             
9A3B: 7A              LD      A,D                 
9A3C: 09              ADD     HL,BC               
9A3D: 15              DEC     D                   
9A3E: 91              SUB     C                   
9A3F: 7A              LD      A,D                 
9A40: 61              LD      H,C                 
9A41: 17              RLA                         
9A42: 0B              DEC     BC                  
9A43: EE 15           XOR     $15                 
9A45: BC              CP      H                   
9A46: CF              RST     0X08                
9A47: 62              LD      H,D                 
9A48: 66              LD      H,(HL)              
9A49: B1              OR      C                   
9A4A: 51              LD      D,C                 
9A4B: 18 23           JR      $9A70               ; {}
9A4D: C6 37           ADD     $37                 
9A4F: 49              LD      C,C                 
9A50: 59              LD      E,C                 
9A51: F4 8E 73        CALL    P,$738E             ; {}
9A54: 55              LD      D,L                 
9A55: 5E              LD      E,(HL)              
9A56: 54              LD      D,H                 
9A57: BD              CP      L                   
9A58: 10 B2           DJNZ    $9A0C               ; {}
9A5A: C3 6A 16        JP      $166A               
9A5D: BC              CP      H                   
9A5E: DB 72           IN      A,($72)             
9A60: 95              SUB     L                   
9A61: 5A              LD      E,D                 
9A62: 2F              CPL                         
9A63: 92              SUB     D                   
9A64: 74              LD      (HL),H              
9A65: 4D              LD      C,L                 
9A66: F3              DI                          
9A67: 5F              LD      E,A                 
9A68: 37              SCF                         
9A69: 49              LD      C,C                 
9A6A: D0              RET     NC                  
9A6B: 15              DEC     D                   
9A6C: 82              ADD     A,D                 
9A6D: 17              RLA                         
9A6E: 45              LD      B,L                 
9A6F: 5E              LD      E,(HL)              
9A70: 43              LD      B,E                 
9A71: DE 3F           SBC     $3F                 
9A73: 98              SBC     B                   
9A74: F3              DI                          
9A75: B4              OR      H                   
9A76: C7              RST     0X00                
9A77: DE DB           SBC     $DB                 
9A79: 16 CB           LD      D,$CB               
9A7B: B9              CP      C                   
9A7C: 36 A1           LD      (HL),$A1            
9A7E: 90              SUB     B                   
9A7F: 14              INC     D                   
9A80: 07              RLCA                        
9A81: 58              LD      E,B                 
9A82: 70              LD      (HL),B              
9A83: CA 63 C0        JP      Z,$C063             
9A86: 13              INC     DE                  
9A87: 8D              ADC     A,L                 
9A88: B6              OR      (HL)                
9A89: 14              INC     D                   
9A8A: 26 60           LD      H,$60               
9A8C: 89              ADC     A,C                 
9A8D: 17              RLA                         
9A8E: FF              RST     0X38                
9A8F: 14              INC     D                   
9A90: 82              ADD     A,D                 
9A91: 49              LD      C,C                 
9A92: 2E 1C           LD      L,$1C               
9A94: 01 1D 64        LD      BC,$641D            
9A97: 0D              DEC     C                   
9A98: 1E 1C           LD      E,$1C               
9A9A: 6A              LD      L,D                 
9A9B: 2E 20           LD      L,$20               
9A9D: 29              ADD     HL,HL               
9A9E: 04              INC     B                   
9A9F: 17              RLA                         
9AA0: C3 54 AF        JP      $AF54               ; {}
9AA3: 54              LD      D,H                 
9AA4: 5A              LD      E,D                 
9AA5: 17              RLA                         
9AA6: 52              LD      D,D                 
9AA7: D1              POP     DE                  
9AA8: AB              XOR     E                   
9AA9: A2              AND     D                   
9AAA: 5F              LD      E,A                 
9AAB: BE              CP      (HL)                
9AAC: EB              EX      DE,HL               
9AAD: 14              INC     D                   
9AAE: 90              SUB     B                   
9AAF: 8C              ADC     A,H                 
9AB0: F4 59 C2        CALL    P,$C259             
9AB3: 16 9D           LD      D,$9D               
9AB5: 61              LD      H,C                 
9AB6: 2E 0D           LD      L,$0D               
9AB8: 1C              INC     E                   
9AB9: 04              INC     B                   
9ABA: 17              RLA                         
9ABB: C3 54 AF        JP      $AF54               ; {}
9ABE: 54              LD      D,H                 
9ABF: 5A              LD      E,D                 
9AC0: 17              RLA                         
9AC1: 4D              LD      C,L                 
9AC2: D1              POP     DE                  
9AC3: D6 06           SUB     $06                 
9AC5: DB 72           IN      A,($72)             
9AC7: CE 56           ADC     $56                 
9AC9: 8E              ADC     A,(HL)              
9ACA: 7A              LD      A,D                 
9ACB: 23              INC     HL                  
9ACC: 62              LD      H,D                 
9ACD: C9              RET                         
9ACE: 54              LD      D,H                 
9ACF: B5              OR      L                   
9AD0: B7              OR      A                   
9AD1: 2E 1C           LD      L,$1C               
9AD3: 6A              LD      L,D                 
9AD4: 29              ADD     HL,HL               
9AD5: 02              LD      (BC),A              
9AD6: 09              ADD     HL,BC               
9AD7: 94              SUB     H                   
9AD8: 91              SUB     C                   
9AD9: 40              LD      B,B                 
9ADA: A0              AND     B                   
9ADB: BF              CP      A                   
9ADC: 14              INC     D                   
9ADD: 49              LD      C,C                 
9ADE: C0              RET     NZ                  
9ADF: 4E              LD      C,(HL)              
9AE0: 5F              LD      E,A                 
9AE1: 09              ADD     HL,BC               
9AE2: 85              ADD     A,L                 
9AE3: 07              RLCA                        
9AE4: 80              ADD     A,B                 
9AE5: 02              LD      (BC),A              
9AE6: 04              INC     B                   
9AE7: 89              ADC     A,C                 
9AE8: 8C              ADC     A,H                 
9AE9: 4D              LD      C,L                 
9AEA: 75              LD      (HL),L              
9AEB: 62              LD      H,D                 
9AEC: 0A              LD      A,(BC)              
9AED: 9C              SBC     H                   
9AEE: 08              EX      AF,AF'              
9AEF: 81              ADD     A,C                 
9AF0: 02              LD      (BC),A              
9AF1: 05              DEC     B                   
9AF2: 40              LD      B,B                 
9AF3: 55              LD      D,L                 
9AF4: 3E B9           LD      A,$B9               
9AF6: 45              LD      B,L                 
9AF7: 53              LD      D,E                 
9AF8: 0C              INC     C                   
9AF9: 9C              SBC     H                   
9AFA: 08              EX      AF,AF'              
9AFB: 80              ADD     A,B                 
9AFC: 07              RLCA                        
9AFD: 01 C5 02        LD      BC,$02C5            
9B00: 04              INC     B                   
9B01: 1B              DEC     DE                  
9B02: 54              LD      D,H                 
9B03: 23              INC     HL                  
9B04: 7B              LD      A,E                 
9B05: 4A              LD      C,D                 
9B06: 5D              LD      E,L                 
9B07: 6E              LD      L,(HL)              
9B08: 00              NOP                         
9B09: 80              ADD     A,B                 
9B0A: 01 01 60        LD      BC,$6001            
9B0D: 07              RLCA                        
9B0E: 4B              LD      C,E                 
9B0F: 0D              DEC     C                   
9B10: 49              LD      C,C                 
9B11: 0A              LD      A,(BC)              
9B12: 12              LD      (DE),A              
9B13: 0E 45           LD      C,$45               
9B15: 0D              DEC     C                   
9B16: 1D              DEC     E                   
9B17: 03              INC     BC                  
9B18: 72              LD      (HL),D              
9B19: 73              LD      (HL),E              
9B1A: 04              INC     B                   
9B1B: 0F              RRCA                        
9B1C: 5F              LD      E,A                 
9B1D: BE              CP      (HL)                
9B1E: 55              LD      D,L                 
9B1F: 17              RLA                         
9B20: 67              LD      H,A                 
9B21: B1              OR      C                   
9B22: 89              ADC     A,C                 
9B23: 96              SUB     (HL)                
9B24: B5              OR      L                   
9B25: 9E              SBC     (HL)                
9B26: B6              OR      (HL)                
9B27: 14              INC     D                   
9B28: 95              SUB     L                   
9B29: 48              LD      C,B                 
9B2A: 2E 17           LD      L,$17               
9B2C: 73              LD      (HL),E              
9B2D: 00              NOP                         
9B2E: 17              RLA                         
9B2F: 74              LD      (HL),H              
9B30: 00              NOP                         
9B31: 17              RLA                         
9B32: 75              LD      (HL),L              
9B33: 00              NOP                         
9B34: 0D              DEC     C                   
9B35: 24              INC     H                   
9B36: 04              INC     B                   
9B37: 16 5F           LD      D,$5F               
9B39: BE              CP      (HL)                
9B3A: D3 17           OUT     ($17),A             
9B3C: FB              EI                          
9B3D: 62              LD      H,D                 
9B3E: AB              XOR     E                   
9B3F: 98              SBC     B                   
9B40: 64              LD      H,H                 
9B41: B7              OR      A                   
9B42: 30 60           JR      NC,$9BA4            ; {}
9B44: D5              PUSH    DE                  
9B45: 15              DEC     D                   
9B46: 85              ADD     A,L                 
9B47: 14              INC     D                   
9B48: 98              SBC     B                   
9B49: BE              CP      (HL)                
9B4A: 7F              LD      A,A                 
9B4B: 49              LD      C,C                 
9B4C: 9B              SBC     E                   
9B4D: 5D              LD      E,L                 
9B4E: 17              RLA                         
9B4F: 73              LD      (HL),E              
9B50: 72              LD      (HL),D              
9B51: 17              RLA                         
9B52: 74              LD      (HL),H              
9B53: 72              LD      (HL),D              
9B54: 17              RLA                         
9B55: 75              LD      (HL),L              
9B56: 72              LD      (HL),D              
9B57: 1C              INC     E                   
9B58: 72              LD      (HL),D              
9B59: 33              INC     SP                  
9B5A: 02              LD      (BC),A              
9B5B: 08              EX      AF,AF'              
9B5C: 23              INC     HL                  
9B5D: D1              POP     DE                  
9B5E: DB BD           IN      A,($BD)             
9B60: F6 4F           OR      $4F                 
9B62: 80              ADD     A,B                 
9B63: BF              CP      A                   
9B64: 4A              LD      C,D                 
9B65: 80              ADD     A,B                 
9B66: 80              ADD     A,B                 
9B67: 6E              LD      L,(HL)              
9B68: 00              NOP                         
9B69: 80              ADD     A,B                 
9B6A: 01 01 6A        LD      BC,$6A01            
9B6D: 07              RLCA                        
9B6E: 6E              LD      L,(HL)              
9B6F: 0D              DEC     C                   
9B70: 6C              LD      L,H                 
9B71: 0A              LD      A,(BC)              
9B72: 12              LD      (DE),A              
9B73: 0E 68           LD      C,$68               
9B75: 0D              DEC     C                   
9B76: 10 03           DJNZ    $9B7B               ; {}
9B78: 73              LD      (HL),E              
9B79: 00              NOP                         
9B7A: 04              INC     B                   
9B7B: 0B              DEC     BC                  
9B7C: 06 9A           LD      B,$9A               
9B7E: 90              SUB     B                   
9B7F: 73              LD      (HL),E              
9B80: CA 6A EA        JP      Z,$EA6A             
9B83: 48              LD      C,B                 
9B84: 9D              SBC     L                   
9B85: 61              LD      H,C                 
9B86: 2E 0D           LD      L,$0D               
9B88: 52              LD      D,D                 
9B89: 04              INC     B                   
9B8A: 14              INC     D                   
9B8B: A2              AND     D                   
9B8C: 1D              DEC     E                   
9B8D: 74              LD      (HL),H              
9B8E: 8E              ADC     A,(HL)              
9B8F: D4 6A 53        CALL    NC,$536A            
9B92: 79              LD      A,C                 
9B93: CC 51 BE        CALL    Z,$BE51             
9B96: A0              AND     B                   
9B97: 00              NOP                         
9B98: B3              OR      E                   
9B99: D4 9C 91        CALL    NC,$919C            ; {}
9B9C: C5              PUSH    BC                  
9B9D: DC 63 03        CALL    C,$0363             
9BA0: 01 80 04        LD      BC,$0480            
9BA3: 37              SCF                         
9BA4: 3F              CCF                         
9BA5: B9              CP      C                   
9BA6: A9              XOR     C                   
9BA7: 60              LD      H,B                 
9BA8: DB CE           IN      A,($CE)             
9BAA: 1B              DEC     DE                  
9BAB: A1              AND     C                   
9BAC: 8E              ADC     A,(HL)              
9BAD: C5              PUSH    BC                  
9BAE: 3D              DEC     A                   
9BAF: 62              LD      H,D                 
9BB0: 50              LD      D,B                 
9BB1: BD              CP      L                   
9BB2: 16 58           LD      D,$58               
9BB4: 95              SUB     L                   
9BB5: 73              LD      (HL),E              
9BB6: 89              ADC     A,C                 
9BB7: 17              RLA                         
9BB8: 67              LD      H,A                 
9BB9: 16 A6           LD      D,$A6               
9BBB: 48              LD      C,B                 
9BBC: 81              ADD     A,C                 
9BBD: 13              INC     DE                  
9BBE: 92              SUB     D                   
9BBF: 5F              LD      E,A                 
9BC0: 03              INC     BC                  
9BC1: A0              AND     B                   
9BC2: E6 46           AND     $46                 
9BC4: CB 7B           BIT     7,E                 
9BC6: E6 BD           AND     $BD                 
9BC8: 8B              ADC     A,E                 
9BC9: 18 7B           JR      $9C46               ; {}
9BCB: A6              AND     (HL)                
9BCC: B3              OR      E                   
9BCD: 9A              SBC     D                   
9BCE: 6B              LD      L,E                 
9BCF: BF              CP      A                   
9BD0: F5              PUSH    AF                  
9BD1: 59              LD      E,C                 
9BD2: 2F              CPL                         
9BD3: 7B              LD      A,E                 
9BD4: 16 58           LD      D,$58               
9BD6: 31 49 97        LD      SP,$9749            
9BD9: 62              LD      H,D                 
9BDA: 22 14 0C        LD      ($0C14),HL          
9BDD: 02              LD      (BC),A              
9BDE: 08              EX      AF,AF'              
9BDF: AF              XOR     A                   
9BE0: 6E              LD      L,(HL)              
9BE1: 83              ADD     A,E                 
9BE2: 61              LD      H,C                 
9BE3: F6 4F           OR      $4F                 
9BE5: 80              ADD     A,B                 
9BE6: BF              CP      A                   
9BE7: 63              LD      H,E                 
9BE8: 0F              RRCA                        
9BE9: 9C              SBC     H                   
9BEA: 08              EX      AF,AF'              
9BEB: 81              ADD     A,C                 
9BEC: 02              LD      (BC),A              
9BED: 0A              LD      A,(BC)              
9BEE: 07              RLCA                        
9BEF: CB 50           BIT     2,B                 
9BF1: D1              POP     DE                  
9BF2: D5              PUSH    DE                  
9BF3: 6A              LD      L,D                 
9BF4: AF              XOR     A                   
9BF5: 55              LD      D,L                 
9BF6: 83              ADD     A,E                 
9BF7: 61              LD      H,C                 
9BF8: 64              LD      H,H                 
9BF9: 57              LD      D,A                 
9BFA: 00              NOP                         
9BFB: 00              NOP                         
9BFC: 80              ADD     A,B                 
9BFD: 07              RLCA                        
9BFE: 42              LD      B,D                 
9BFF: 0D              DEC     C                   
9C00: 40              LD      B,B                 
9C01: 0A              LD      A,(BC)              
9C02: 58              LD      E,B                 
9C03: 04              INC     B                   
9C04: 38 59           JR      C,$9C5F             ; {}
9C06: 45              LD      B,L                 
9C07: 92              SUB     D                   
9C08: 5F              LD      E,A                 
9C09: 03              INC     BC                  
9C0A: A0              AND     B                   
9C0B: 83              ADD     A,E                 
9C0C: 7A              LD      A,D                 
9C0D: 5F              LD      E,A                 
9C0E: BE              CP      (HL)                
9C0F: 5A              LD      E,D                 
9C10: 17              RLA                         
9C11: D3 7A           OUT     ($7A),A             
9C13: 4B              LD      C,E                 
9C14: 7B              LD      A,E                 
9C15: 14              INC     D                   
9C16: 67              LD      H,A                 
9C17: F3              DI                          
9C18: 5F              LD      E,A                 
9C19: 8E              ADC     A,(HL)              
9C1A: 48              LD      C,B                 
9C1B: 82              ADD     A,D                 
9C1C: 17              RLA                         
9C1D: 52              LD      D,D                 
9C1E: 5E              LD      E,(HL)              
9C1F: 50              LD      D,B                 
9C20: 8B              ADC     A,E                 
9C21: 73              LD      (HL),E              
9C22: 62              LD      H,D                 
9C23: 94              SUB     H                   
9C24: 5F              LD      E,A                 
9C25: 53              LD      D,E                 
9C26: BE              CP      (HL)                
9C27: 4B              LD      C,E                 
9C28: 7B              LD      A,E                 
9C29: F5              PUSH    AF                  
9C2A: 59              LD      E,C                 
9C2B: F9              LD      SP,HL               
9C2C: BF              CP      A                   
9C2D: 26 DD           LD      H,$DD               
9C2F: 10 EE           DJNZ    $9C1F               ; {}
9C31: F3              DI                          
9C32: A0              AND     B                   
9C33: 6B              LD      L,E                 
9C34: BF              CP      A                   
9C35: 30 92           JR      NC,$9BC9            ; {}
9C37: 91              SUB     C                   
9C38: BE              CP      (HL)                
9C39: 9B              SBC     E                   
9C3A: 96              SUB     (HL)                
9C3B: 3F              CCF                         
9C3C: A1              AND     C                   
9C3D: 1C              INC     E                   
9C3E: 01 1D 6E        LD      BC,$6E1D            
9C41: 02              LD      (BC),A              
9C42: 0E 95           LD      C,$95               
9C44: 5A              LD      E,D                 
9C45: FB              EI                          
9C46: A5              AND     L                   
9C47: 51              LD      D,C                 
9C48: DB 96           IN      A,($96)             
9C4A: 64              LD      H,H                 
9C4B: DB 72           IN      A,($72)             
9C4D: 94              SUB     H                   
9C4E: 5F              LD      E,A                 
9C4F: 53              LD      D,E                 
9C50: BE              CP      (HL)                
9C51: 65              LD      H,L                 
9C52: 80              ADD     A,B                 
9C53: 92              SUB     D                   
9C54: 00              NOP                         
9C55: 00              NOP                         
9C56: 80              ADD     A,B                 
9C57: 07              RLCA                        
9C58: 7E              LD      A,(HL)              
9C59: 0D              DEC     C                   
9C5A: 7C              LD      A,H                 
9C5B: 0A              LD      A,(BC)              
9C5C: 58              LD      E,B                 
9C5D: 04              INC     B                   
9C5E: 74              LD      (HL),H              
9C5F: 5F              LD      E,A                 
9C60: BE              CP      (HL)                
9C61: 5A              LD      E,D                 
9C62: 17              RLA                         
9C63: D5              PUSH    DE                  
9C64: 7A              LD      A,D                 
9C65: D9              EXX                         
9C66: B5              OR      L                   
9C67: 92              SUB     D                   
9C68: 5F              LD      E,A                 
9C69: 03              INC     BC                  
9C6A: A0              AND     B                   
9C6B: 14              INC     D                   
9C6C: 67              LD      H,A                 
9C6D: 4B              LD      C,E                 
9C6E: 62              LD      H,D                 
9C6F: 8E              ADC     A,(HL)              
9C70: 48              LD      C,B                 
9C71: 51              LD      D,C                 
9C72: 18 50           JR      $9CC4               ; {}
9C74: C2 03 A1        JP      NZ,$A103            ; {}
9C77: 9B              SBC     E                   
9C78: 53              LD      D,E                 
9C79: 03              INC     BC                  
9C7A: A0              AND     B                   
9C7B: 5F              LD      E,A                 
9C7C: BE              CP      (HL)                
9C7D: 55              LD      D,L                 
9C7E: 17              RLA                         
9C7F: 67              LD      H,A                 
9C80: B1              OR      C                   
9C81: 96              SUB     (HL)                
9C82: 96              SUB     (HL)                
9C83: 56              LD      D,(HL)              
9C84: 72              LD      (HL),D              
9C85: 82              ADD     A,D                 
9C86: 17              RLA                         
9C87: 4F              LD      C,A                 
9C88: 5E              LD      E,(HL)              
9C89: 40              LD      B,B                 
9C8A: A0              AND     B                   
9C8B: D5              PUSH    DE                  
9C8C: 15              DEC     D                   
9C8D: FF              RST     0X38                
9C8E: 14              INC     D                   
9C8F: 0C              INC     C                   
9C90: BA              CP      D                   
9C91: C7              RST     0X00                
9C92: A1              AND     C                   
9C93: 9B              SBC     E                   
9C94: 5D              LD      E,L                 
9C95: 83              ADD     A,E                 
9C96: 48              LD      C,B                 
9C97: 9D              SBC     L                   
9C98: 7A              LD      A,D                 
9C99: 50              LD      D,B                 
9C9A: BD              CP      L                   
9C9B: 0E BC           LD      C,$BC               
9C9D: 7F              LD      A,A                 
9C9E: 49              LD      C,C                 
9C9F: F3              DI                          
9CA0: B4              OR      H                   
9CA1: 54              LD      D,H                 
9CA2: 8B              ADC     A,E                 
9CA3: 9B              SBC     E                   
9CA4: 6C              LD      L,H                 
9CA5: 6B              LD      L,E                 
9CA6: 68              LD      L,B                 
9CA7: E7              RST     0X20                
9CA8: 6D              LD      L,L                 
9CA9: CD 9A B8        CALL    $B89A               
9CAC: 16 71           LD      D,$71               
9CAE: 16 03           LD      D,$03               
9CB0: A0              AND     B                   
9CB1: 3E 55           LD      A,$55               
9CB3: 86              ADD     A,(HL)              
9CB4: 8C              ADC     A,H                 
9CB5: 59              LD      E,C                 
9CB6: 5E              LD      E,(HL)              
9CB7: 82              ADD     A,D                 
9CB8: 7B              LD      A,E                 
9CB9: 82              ADD     A,D                 
9CBA: 17              RLA                         
9CBB: 47              LD      B,A                 
9CBC: 5E              LD      E,(HL)              
9CBD: 3E 49           LD      A,$49               
9CBF: 73              LD      (HL),E              
9CC0: 76              HALT                        
9CC1: F5              PUSH    AF                  
9CC2: 59              LD      E,C                 
9CC3: F9              LD      SP,HL               
9CC4: BF              CP      A                   
9CC5: D0              RET     NC                  
9CC6: DD ; ????
9CC7: CB 6A           BIT     5,D                 
9CC9: 03              INC     BC                  
9CCA: BC              CP      H                   
9CCB: 33              INC     SP                  
9CCC: 98              SBC     B                   
9CCD: C7              RST     0X00                
9CCE: DE 16           SBC     $16                 
9CD0: EE 4F           XOR     $4F                 
9CD2: A0              AND     B                   
9CD3: 1C              INC     E                   
9CD4: 01 1D 6E        LD      BC,$6E1D            
9CD7: 02              LD      (BC),A              
9CD8: 0D              DEC     C                   
9CD9: 95              SUB     L                   
9CDA: 5A              LD      E,D                 
9CDB: FB              EI                          
9CDC: A5              AND     L                   
9CDD: 51              LD      D,C                 
9CDE: DB 96           IN      A,($96)             
9CE0: 64              LD      H,H                 
9CE1: DB 72           IN      A,($72)             
9CE3: C1              POP     BC                  
9CE4: 93              SUB     E                   
9CE5: 4E              LD      C,(HL)              
9CE6: 66              LD      H,(HL)              
9CE7: 80              ADD     A,B                 
9CE8: 91              SUB     C                   
9CE9: 00              NOP                         
9CEA: 00              NOP                         
9CEB: 80              ADD     A,B                 
9CEC: 07              RLCA                        
9CED: 78              LD      A,B                 
9CEE: 0D              DEC     C                   
9CEF: 76              HALT                        
9CF0: 0A              LD      A,(BC)              
9CF1: 58              LD      E,B                 
9CF2: 04              INC     B                   
9CF3: 62              LD      H,D                 
9CF4: 83              ADD     A,E                 
9CF5: 48              LD      C,B                 
9CF6: 8F              ADC     A,A                 
9CF7: 61              LD      H,C                 
9CF8: CB B1           RES     6,C                 
9CFA: AF              XOR     A                   
9CFB: 14              INC     D                   
9CFC: 5B              LD      E,E                 
9CFD: 48              LD      C,B                 
9CFE: EA 48 94        JP      PE,$9448            ; {}
9D01: 5F              LD      E,A                 
9D02: D1              POP     DE                  
9D03: B5              OR      L                   
9D04: 96              SUB     (HL)                
9D05: 96              SUB     (HL)                
9D06: DB 72           IN      A,($72)             
9D08: 64              LD      H,H                 
9D09: B7              OR      A                   
9D0A: 30 60           JR      NC,$9D6C            ; {}
9D0C: 90              SUB     B                   
9D0D: 14              INC     D                   
9D0E: 1B              DEC     DE                  
9D0F: 58              LD      E,B                 
9D10: 1B              DEC     DE                  
9D11: A1              AND     C                   
9D12: 16 D0           LD      D,$D0               
9D14: 13              INC     DE                  
9D15: 54              LD      D,H                 
9D16: 4B              LD      C,E                 
9D17: 49              LD      C,C                 
9D18: 73              LD      (HL),E              
9D19: 7B              LD      A,E                 
9D1A: F5              PUSH    AF                  
9D1B: 59              LD      E,C                 
9D1C: F9              LD      SP,HL               
9D1D: BF              CP      A                   
9D1E: 4B              LD      C,E                 
9D1F: DF              RST     0X18                
9D20: 5F              LD      E,A                 
9D21: BE              CP      (HL)                
9D22: 71              LD      (HL),C              
9D23: 16 5F           LD      D,$5F               
9D25: BE              CP      (HL)                
9D26: 95              SUB     L                   
9D27: AF              XOR     A                   
9D28: 92              SUB     D                   
9D29: 73              LD      (HL),E              
9D2A: D6 06           SUB     $06                 
9D2C: DB 72           IN      A,($72)             
9D2E: F6 4F           OR      $4F                 
9D30: 80              ADD     A,B                 
9D31: BF              CP      A                   
9D32: D4 B5 D7        CALL    NC,$D7B5            
9D35: 5F              LD      E,A                 
9D36: DB 59           IN      A,($59)             
9D38: 9E              SBC     (HL)                
9D39: 7A              LD      A,D                 
9D3A: D6 9C           SUB     $9C                 
9D3C: DB 72           IN      A,($72)             
9D3E: 40              LD      B,B                 
9D3F: 55              LD      D,L                 
9D40: 3E B9           LD      A,$B9               
9D42: 43              LD      B,E                 
9D43: 5E              LD      E,(HL)              
9D44: 33              INC     SP                  
9D45: 98              SBC     B                   
9D46: 5F              LD      E,A                 
9D47: BE              CP      (HL)                
9D48: 55              LD      D,L                 
9D49: 17              RLA                         
9D4A: 67              LD      H,A                 
9D4B: B1              OR      C                   
9D4C: 86              ADD     A,(HL)              
9D4D: 96              SUB     (HL)                
9D4E: 85              ADD     A,L                 
9D4F: 5F              LD      E,A                 
9D50: 98              SBC     B                   
9D51: BE              CP      (HL)                
9D52: 7F              LD      A,A                 
9D53: 49              LD      C,C                 
9D54: 5B              LD      E,E                 
9D55: BB              CP      E                   
9D56: 17              RLA                         
9D57: 73              LD      (HL),E              
9D58: 00              NOP                         
9D59: 17              RLA                         
9D5A: 74              LD      (HL),H              
9D5B: 00              NOP                         
9D5C: 17              RLA                         
9D5D: 75              LD      (HL),L              
9D5E: 00              NOP                         
9D5F: 17              RLA                         
9D60: 70              LD      (HL),B              
9D61: 00              NOP                         
9D62: 17              RLA                         
9D63: 71              LD      (HL),C              
9D64: 00              NOP                         
9D65: 38 02           JR      C,$9D69             ; {}
9D67: 12              LD      (DE),A              
9D68: 95              SUB     L                   
9D69: 5A              LD      E,D                 
9D6A: FB              EI                          
9D6B: A5              AND     L                   
9D6C: 51              LD      D,C                 
9D6D: DB 96           IN      A,($96)             
9D6F: 64              LD      H,H                 
9D70: DB 72           IN      A,($72)             
9D72: C6 93           ADD     $93                 
9D74: F4 72 5A        CALL    P,$5A72             
9D77: 17              RLA                         
9D78: D3 7A           OUT     ($7A),A             
9D7A: 53              LD      D,E                 
9D7B: 0C              INC     C                   
9D7C: 8A              ADC     A,D                 
9D7D: 08              EX      AF,AF'              
9D7E: 82              ADD     A,D                 
9D7F: 07              RLCA                        
9D80: 01 C5 02        LD      BC,$02C5            
9D83: 04              INC     B                   
9D84: 1B              DEC     DE                  
9D85: 54              LD      D,H                 
9D86: 23              INC     HL                  
9D87: 7B              LD      A,E                 
9D88: 67              LD      H,A                 
9D89: 77              LD      (HL),A              
9D8A: 8A              ADC     A,D                 
9D8B: 08              EX      AF,AF'              
9D8C: A0              AND     B                   
9D8D: 07              RLCA                        
9D8E: 6A              LD      L,D                 
9D8F: 0E 68           LD      C,$68               
9D91: 0D              DEC     C                   
9D92: 4E              LD      C,(HL)              
9D93: 0E 08           LD      C,$08               
9D95: 0A              LD      A,(BC)              
9D96: 05              DEC     B                   
9D97: 0A              LD      A,(BC)              
9D98: 43              LD      B,E                 
9D99: 0A              LD      A,(BC)              
9D9A: 2D              DEC     L                   
9D9B: 0A              LD      A,(BC)              
9D9C: 12              LD      (DE),A              
9D9D: 14              INC     D                   
9D9E: A2              AND     D                   
9D9F: 04              INC     B                   
9DA0: 02              LD      (BC),A              
9DA1: 11 9F 34        LD      DE,$349F            
9DA4: 1A              LD      A,(DE)              
9DA5: 8F              ADC     A,A                 
9DA6: 25              DEC     H                   
9DA7: 04              INC     B                   
9DA8: 33              INC     SP                  
9DA9: 26 BA           LD      H,$BA               
9DAB: F0              RET     P                   
9DAC: 59              LD      E,C                 
9DAD: 1E 8F           LD      E,$8F               
9DAF: 51              LD      D,C                 
9DB0: 18 23           JR      $9DD5               ; {}
9DB2: C6 34           ADD     $34                 
9DB4: BA              CP      D                   
9DB5: 07              RLCA                        
9DB6: B3              OR      E                   
9DB7: 43              LD      B,E                 
9DB8: 98              SBC     B                   
9DB9: C5              PUSH    BC                  
9DBA: 98              SBC     B                   
9DBB: AF              XOR     A                   
9DBC: 14              INC     D                   
9DBD: 50              LD      D,B                 
9DBE: 6D              LD      L,L                 
9DBF: 89              ADC     A,C                 
9DC0: 17              RLA                         
9DC1: 03              INC     BC                  
9DC2: 15              DEC     D                   
9DC3: E1              POP     HL                  
9DC4: B9              CP      C                   
9DC5: 8F              ADC     A,A                 
9DC6: 8E              ADC     A,(HL)              
9DC7: 90              SUB     B                   
9DC8: 14              INC     D                   
9DC9: 10 58           DJNZ    $9E23               ; {}
9DCB: EB              EX      DE,HL               
9DCC: 62              LD      H,D                 
9DCD: 0F              RRCA                        
9DCE: A0              AND     B                   
9DCF: D6 B5           SUB     $B5                 
9DD1: 17              RLA                         
9DD2: 48              LD      C,B                 
9DD3: 82              ADD     A,D                 
9DD4: 17              RLA                         
9DD5: D4 60 E6        CALL    NC,$E660            
9DD8: 16 D7           LD      D,$D7               
9DDA: 46              LD      B,(HL)              
9DDB: 21 25 30        LD      HL,$3025            
9DDE: 81              ADD     A,C                 
9DDF: 2F              CPL                         
9DE0: 09              ADD     HL,BC               
9DE1: 0D              DEC     C                   
9DE2: 16 0E           LD      D,$0E               
9DE4: 0C              INC     C                   
9DE5: 0A              LD      A,(BC)              
9DE6: 06 0A           LD      B,$0A               
9DE8: 0D              DEC     C                   
9DE9: 0A              LD      A,(BC)              
9DEA: 0F              RRCA                        
9DEB: 0A              LD      A,(BC)              
9DEC: 4B              LD      C,E                 
9DED: 0A              LD      A,(BC)              
9DEE: 0E 0A           LD      C,$0A               
9DF0: 39              ADD     HL,SP               
9DF1: 03              INC     BC                  
9DF2: 01 77 35        LD      BC,$3577            
9DF5: 30 8A           JR      NC,$9D81            ; {}
9DF7: 2F              CPL                         
9DF8: 08              EX      AF,AF'              
9DF9: 02              LD      (BC),A              
9DFA: 06 50           LD      B,$50               
9DFC: 72              LD      (HL),D              
9DFD: 44              LD      B,H                 
9DFE: 5A              LD      E,D                 
9DFF: D3 7A           OUT     ($7A),A             
9E01: 53              LD      D,E                 
9E02: 0C              INC     C                   
9E03: 8D              ADC     A,L                 
9E04: 07              RLCA                        
9E05: 80              ADD     A,B                 
9E06: 07              RLCA                        
9E07: 01 C5 02        LD      BC,$02C5            
9E0A: 04              INC     B                   
9E0B: 1B              DEC     DE                  
9E0C: 54              LD      D,H                 
9E0D: 23              INC     HL                  
9E0E: 7B              LD      A,E                 
9E0F: 5C              LD      E,H                 
9E10: 0F              RRCA                        
9E11: 8D              ADC     A,L                 
9E12: 07              RLCA                        
9E13: 81              ADD     A,C                 
9E14: 01 01 0E        LD      BC,$0E01            
9E17: 02              LD      (BC),A              
9E18: 07              RLCA                        
9E19: 54              LD      D,H                 
9E1A: 8B              ADC     A,E                 
9E1B: 9B              SBC     E                   
9E1C: 6C              LD      L,H                 
9E1D: 24              INC     H                   
9E1E: 56              LD      D,(HL)              
9E1F: 45              LD      B,L                 
9E20: 2E 80           LD      L,$80               
9E22: B2              OR      D                   
9E23: 8D              ADC     A,L                 
9E24: 07              RLCA                        
9E25: 82              ADD     A,D                 
9E26: 06 80           LD      B,$80               
9E28: A1              AND     C                   
9E29: 0E 80           LD      C,$80               
9E2B: 9E              SBC     (HL)                
9E2C: 0D              DEC     C                   
9E2D: 60              LD      H,B                 
9E2E: 14              INC     D                   
9E2F: 03              INC     BC                  
9E30: 01 80 0A        LD      BC,$0A80            
9E33: 0F              RRCA                        
9E34: 08              EX      AF,AF'              
9E35: 64              LD      H,H                 
9E36: 17              RLA                         
9E37: 64              LD      H,H                 
9E38: 00              NOP                         
9E39: 04              INC     B                   
9E3A: 4C              LD      C,H                 
9E3B: 44              LD      B,H                 
9E3C: 45              LD      B,L                 
9E3D: 0E B2           LD      C,$B2               
9E3F: 83              ADD     A,E                 
9E40: 8C              ADC     A,H                 
9E41: B3              OR      E                   
9E42: 9A              SBC     D                   
9E43: 7B              LD      A,E                 
9E44: 67              LD      H,A                 
9E45: 13              INC     DE                  
9E46: B8              CP      B                   
9E47: C3 9E 89        JP      $899E               ; {}
9E4A: 8C              ADC     A,H                 
9E4B: 33              INC     SP                  
9E4C: 75              LD      (HL),L              
9E4D: 63              LD      H,E                 
9E4E: 98              SBC     B                   
9E4F: 93              SUB     E                   
9E50: B2              OR      D                   
9E51: B6              OR      (HL)                
9E52: 14              INC     D                   
9E53: 8E              ADC     A,(HL)              
9E54: 7A              LD      A,D                 
9E55: DB B5           IN      A,($B5)             
9E57: 1B              DEC     DE                  
9E58: A1              AND     C                   
9E59: 8E              ADC     A,(HL)              
9E5A: 48              LD      C,B                 
9E5B: 51              LD      D,C                 
9E5C: 18 48           JR      $9EA6               ; {}
9E5E: C2 2E 60        JP      NZ,$602E            ; {}
9E61: 61              LD      H,C                 
9E62: 17              RLA                         
9E63: 39              ADD     HL,SP               
9E64: 92              SUB     D                   
9E65: 56              LD      D,(HL)              
9E66: 72              LD      (HL),D              
9E67: FB              EI                          
9E68: 17              RLA                         
9E69: B4              OR      H                   
9E6A: B7              OR      A                   
9E6B: 82              ADD     A,D                 
9E6C: 17              RLA                         
9E6D: 83              ADD     A,E                 
9E6E: 48              LD      C,B                 
9E6F: 68              LD      L,B                 
9E70: 4D              LD      C,L                 
9E71: AF              XOR     A                   
9E72: A0              AND     B                   
9E73: D6 06           SUB     $06                 
9E75: DB 72           IN      A,($72)             
9E77: 96              SUB     (HL)                
9E78: 8C              ADC     A,H                 
9E79: FF              RST     0X38                
9E7A: BE              CP      (HL)                
9E7B: E7              RST     0X20                
9E7C: 14              INC     D                   
9E7D: 5B              LD      E,E                 
9E7E: 4D              LD      C,L                 
9E7F: 74              LD      (HL),H              
9E80: C0              RET     NZ                  
9E81: 8B              ADC     A,E                 
9E82: 9A              SBC     D                   
9E83: AF              XOR     A                   
9E84: 6E              LD      L,(HL)              
9E85: DB E0           IN      A,($E0)             
9E87: 17              RLA                         
9E88: 80              ADD     A,B                 
9E89: 01 17 63        LD      BC,$6317            
9E8C: 7A              LD      A,D                 
9E8D: 38 0D           JR      C,$9E9C             ; {}
9E8F: 3A 0A 0F        LD      A,($0F0A)           
9E92: 08              EX      AF,AF'              
9E93: 64              LD      H,H                 
9E94: 04              INC     B                   
9E95: 30 C7           JR      NC,$9E5E            ; {}
9E97: DE 3A           SBC     $3A                 
9E99: 15              DEC     D                   
9E9A: F4 A4 30        CALL    P,$30A4             
9E9D: 79              LD      A,C                 
9E9E: 9B              SBC     E                   
9E9F: 53              LD      D,E                 
9EA0: 99              SBC     C                   
9EA1: 48              LD      C,B                 
9EA2: 5F              LD      E,A                 
9EA3: BE              CP      (HL)                
9EA4: 84              ADD     A,H                 
9EA5: AF              XOR     A                   
9EA6: 0E B2           LD      C,$B2               
9EA8: 83              ADD     A,E                 
9EA9: 8C              ADC     A,H                 
9EAA: B3              OR      E                   
9EAB: 9A              SBC     D                   
9EAC: 7B              LD      A,E                 
9EAD: 67              LD      H,A                 
9EAE: 13              INC     DE                  
9EAF: B8              CP      B                   
9EB0: C3 9E 89        JP      $899E               ; {}
9EB3: 8C              ADC     A,H                 
9EB4: 33              INC     SP                  
9EB5: 75              LD      (HL),L              
9EB6: 4B              LD      C,E                 
9EB7: 49              LD      C,C                 
9EB8: C7              RST     0X00                
9EB9: DE 84           SBC     $84                 
9EBB: AF              XOR     A                   
9EBC: CB B0           RES     6,B                 
9EBE: 87              ADD     A,A                 
9EBF: 96              SUB     (HL)                
9EC0: A6              AND     (HL)                
9EC1: D8              RET     C                   
9EC2: 7F              LD      A,A                 
9EC3: 9E              SBC     (HL)                
9EC4: 6B              LD      L,E                 
9EC5: B5              OR      L                   
9EC6: 1C              INC     E                   
9EC7: 01 1D 64        LD      BC,$641D            
9ECA: 02              LD      (BC),A              
9ECB: 09              ADD     HL,BC               
9ECC: C1              POP     BC                  
9ECD: C0              RET     NZ                  
9ECE: D0              RET     NC                  
9ECF: 15              DEC     D                   
9ED0: 13              INC     DE                  
9ED1: 54              LD      D,H                 
9ED2: 7E              LD      A,(HL)              
9ED3: 74              LD      (HL),H              
9ED4: 45              LD      B,L                 
9ED5: 1A              LD      A,(DE)              
9ED6: 09              ADD     HL,BC               
9ED7: 8E              ADC     A,(HL)              
9ED8: 08              EX      AF,AF'              
9ED9: 81              ADD     A,C                 
9EDA: 02              LD      (BC),A              
9EDB: 04              INC     B                   
9EDC: 44              LD      B,H                 
9EDD: BD              CP      L                   
9EDE: DB 8B           IN      A,($8B)             
9EE0: 68              LD      L,B                 
9EE1: 31 7B A0        LD      SP,$A07B            
9EE4: AA              XOR     D                   
9EE5: 03              INC     BC                  
9EE6: 1C              INC     E                   
9EE7: 04              INC     B                   
9EE8: 1A              LD      A,(DE)              
9EE9: 5F              LD      E,A                 
9EEA: BE              CP      (HL)                
9EEB: 5B              LD      E,E                 
9EEC: B1              OR      C                   
9EED: 4B              LD      C,E                 
9EEE: 7B              LD      A,E                 
9EEF: 55              LD      D,L                 
9EF0: 45              LD      B,L                 
9EF1: 8E              ADC     A,(HL)              
9EF2: 91              SUB     C                   
9EF3: 16 8A           LD      D,$8A               
9EF5: D0              RET     NC                  
9EF6: B0              OR      B                   
9EF7: 5B              LD      E,E                 
9EF8: B9              CP      C                   
9EF9: 70              LD      (HL),B              
9EFA: B1              OR      C                   
9EFB: 18 BC           JR      $9EB9               ; {}
9EFD: 8E              ADC     A,(HL)              
9EFE: 78              LD      A,B                 
9EFF: 9F              SBC     A                   
9F00: 15              DEC     D                   
9F01: 7F              LD      A,A                 
9F02: B1              OR      C                   
9F03: 0C              INC     C                   
9F04: 01 06 02        LD      BC,$0206            
9F07: 0B              DEC     BC                  
9F08: EB              EX      DE,HL               
9F09: BF              CP      A                   
9F0A: A2              AND     D                   
9F0B: 9A              SBC     D                   
9F0C: 2F              CPL                         
9F0D: 49              LD      C,C                 
9F0E: B3              OR      E                   
9F0F: 9A              SBC     D                   
9F10: 03              INC     BC                  
9F11: CB 4C           BIT     1,H                 
9F13: 4C              LD      C,H                 
9F14: 6C              LD      L,H                 
9F15: 7C              LD      A,H                 
9F16: 10 A0           DJNZ    $9EB8               ; {}
9F18: 07              RLCA                        
9F19: 59              LD      E,C                 
9F1A: 0E 57           LD      C,$57               
9F1C: 0D              DEC     C                   
9F1D: 30 0A           JR      NC,$9F29            ; {}
9F1F: 59              LD      E,C                 
9F20: 0E 2C           LD      C,$2C               
9F22: 14              INC     D                   
9F23: BF              CP      A                   
9F24: 0D              DEC     C                   
9F25: 28 04           JR      Z,$9F2B             ; {}
9F27: 22 33 D1        LD      ($D133),HL          
9F2A: 16 EE           LD      D,$EE               
9F2C: DB 72           IN      A,($72)             
9F2E: 34              INC     (HL)                
9F2F: 92              SUB     D                   
9F30: 56              LD      D,(HL)              
9F31: 5E              LD      E,(HL)              
9F32: 66              LD      H,(HL)              
9F33: 49              LD      C,C                 
9F34: 51              LD      D,C                 
9F35: 5E              LD      E,(HL)              
9F36: 96              SUB     (HL)                
9F37: 64              LD      H,H                 
9F38: 95              SUB     L                   
9F39: 73              LD      (HL),E              
9F3A: 66              LD      H,(HL)              
9F3B: 17              RLA                         
9F3C: 50              LD      D,B                 
9F3D: C4 D0 15        CALL    NZ,$15D0            
9F40: 09              ADD     HL,BC               
9F41: CB AB           RES     5,E                 
9F43: A0              AND     B                   
9F44: F5              PUSH    AF                  
9F45: BD              CP      L                   
9F46: 51              LD      D,C                 
9F47: 18 EB           JR      $9F34               ; {}
9F49: C1              POP     BC                  
9F4A: 1C              INC     E                   
9F4B: 01 23 05        LD      BC,$0523            
9F4E: 0D              DEC     C                   
9F4F: 23              INC     HL                  
9F50: 0A              LD      A,(BC)              
9F51: 4F              LD      C,A                 
9F52: 0E 1F           LD      C,$1F               
9F54: 14              INC     D                   
9F55: BF              CP      A                   
9F56: 0D              DEC     C                   
9F57: 1B              DEC     DE                  
9F58: 1C              INC     E                   
9F59: 01 23 64        LD      BC,$6423            
9F5C: 04              INC     B                   
9F5D: 12              LD      (DE),A              
9F5E: 49              LD      C,C                 
9F5F: D2 D6 06        JP      NC,$06D6            
9F62: 56              LD      D,(HL)              
9F63: 72              LD      (HL),D              
9F64: F3              DI                          
9F65: 17              RLA                         
9F66: D4 B5 8E        CALL    NC,$8EB5            ; {}
9F69: 5F              LD      E,A                 
9F6A: FB              EI                          
9F6B: 8E              ADC     A,(HL)              
9F6C: 41              LD      B,C                 
9F6D: 6E              LD      L,(HL)              
9F6E: AB              XOR     E                   
9F6F: 57              LD      D,A                 
9F70: 17              RLA                         
9F71: 91              SUB     C                   
9F72: 00              NOP                         
9F73: 01 01 6B        LD      BC,$6B01            
9F76: 02              LD      (BC),A              
9F77: 09              ADD     HL,BC               
9F78: 21 C0 55        LD      HL,$55C0            
9F7B: 90              SUB     B                   
9F7C: CF              RST     0X08                
9F7D: 9F              SBC     A                   
9F7E: 91              SUB     C                   
9F7F: BE              CP      (HL)                
9F80: 4E              LD      C,(HL)              
9F81: 69              LD      L,C                 
9F82: 0B              DEC     BC                  
9F83: 90              SUB     B                   
9F84: 08              EX      AF,AF'              
9F85: 81              ADD     A,C                 
9F86: 02              LD      (BC),A              
9F87: 06 E6           LD      B,$E6               
9F89: A4              AND     H                   
9F8A: 66              LD      H,(HL)              
9F8B: 62              LD      H,D                 
9F8C: 33              INC     SP                  
9F8D: 48              LD      C,B                 
9F8E: 2E 5A           LD      L,$5A               
9F90: 90              SUB     B                   
9F91: 08              EX      AF,AF'              
9F92: 82              ADD     A,D                 
9F93: 06 4A           LD      B,$4A               
9F95: 0D              DEC     C                   
9F96: 48              LD      C,B                 
9F97: 0A              LD      A,(BC)              
9F98: 0F              RRCA                        
9F99: 08              EX      AF,AF'              
9F9A: 63              LD      H,E                 
9F9B: 17              RLA                         
9F9C: 63              LD      H,E                 
9F9D: 00              NOP                         
9F9E: 04              INC     B                   
9F9F: 3C              INC     A                   
9FA0: 1A              LD      A,(DE)              
9FA1: B9              CP      C                   
9FA2: A4              AND     H                   
9FA3: EA D5 86        JP      PE,$86D5            ; {}
9FA6: 91              SUB     C                   
9FA7: A6              AND     (HL)                
9FA8: 82              ADD     A,D                 
9FA9: 17              RLA                         
9FAA: 4E              LD      C,(HL)              
9FAB: 5E              LD      E,(HL)              
9FAC: 8E              ADC     A,(HL)              
9FAD: 7B              LD      A,E                 
9FAE: DB 8B           IN      A,($8B)             
9FB0: 24              INC     H                   
9FB1: 56              LD      D,(HL)              
9FB2: 44              LD      B,H                 
9FB3: 5E              LD      E,(HL)              
9FB4: 7B              LD      A,E                 
9FB5: 60              LD      H,B                 
9FB6: 8B              ADC     A,E                 
9FB7: 9A              SBC     D                   
9FB8: 6B              LD      L,E                 
9FB9: BF              CP      A                   
9FBA: C9              RET                         
9FBB: 6D              LD      L,L                 
9FBC: C4 CE 09        CALL    NZ,$09CE            
9FBF: B2              OR      D                   
9FC0: 46              LD      B,(HL)              
9FC1: 75              LD      (HL),L              
9FC2: B3              OR      E                   
9FC3: E0              RET     PO                  
9FC4: 5F              LD      E,A                 
9FC5: BE              CP      (HL)                
9FC6: 95              SUB     L                   
9FC7: 96              SUB     (HL)                
9FC8: 8E              ADC     A,(HL)              
9FC9: 62              LD      H,D                 
9FCA: F5              PUSH    AF                  
9FCB: 8B              ADC     A,E                 
9FCC: D0              RET     NC                  
9FCD: 15              DEC     D                   
9FCE: 6B              LD      L,E                 
9FCF: BF              CP      A                   
9FD0: 55              LD      D,L                 
9FD1: 45              LD      B,L                 
9FD2: 46              LD      B,(HL)              
9FD3: 72              LD      (HL),D              
9FD4: 51              LD      D,C                 
9FD5: 5E              LD      E,(HL)              
9FD6: 99              SBC     C                   
9FD7: 64              LD      H,H                 
9FD8: 96              SUB     (HL)                
9FD9: 73              LD      (HL),E              
9FDA: DB 63           IN      A,($63)             
9FDC: 17              RLA                         
9FDD: 64              LD      H,H                 
9FDE: 7F              LD      A,A                 
9FDF: 02              LD      (BC),A              
9FE0: 09              ADD     HL,BC               
9FE1: C1              POP     BC                  
9FE2: C0              RET     NZ                  
9FE3: D0              RET     NC                  
9FE4: 15              DEC     D                   
9FE5: 13              INC     DE                  
9FE6: 54              LD      D,H                 
9FE7: 7E              LD      A,(HL)              
9FE8: 74              LD      (HL),H              
9FE9: 45              LD      B,L                 
9FEA: 00              NOP                         
9FEB: 03              INC     BC                  
9FEC: 00              NOP                         
9FED: 00              NOP                         
9FEE: 80              ADD     A,B                 
9FEF: 5C              LD      E,H                 
9FF0: 55              LD      D,L                 
9FF1: DB 05           IN      A,($05)             
9FF3: A0              AND     B                   
9FF4: 03              INC     BC                  
9FF5: 1A              LD      A,(DE)              
9FF6: 04              INC     B                   
9FF7: 18 5F           JR      $A058               ; {}
9FF9: BE              CP      (HL)                
9FFA: 5B              LD      E,E                 
9FFB: B1              OR      C                   
9FFC: 4B              LD      C,E                 
9FFD: 7B              LD      A,E                 
9FFE: 56              LD      D,(HL)              
9FFF: 45              LD      B,L                 
A000: 2B              DEC     HL                  
A001: D2 8D 7A        JP      NC,$7A8D            ; {}
A004: 09              ADD     HL,BC               
A005: 71              LD      (HL),C              
A006: 67              LD      H,A                 
A007: B1              OR      C                   
A008: 85              ADD     A,L                 
A009: 96              SUB     (HL)                
A00A: AF              XOR     A                   
A00B: C3 9F 15        JP      $159F               
A00E: 7F              LD      A,A                 
A00F: B1              OR      C                   
A010: 07              RLCA                        
A011: 1F              RRA                         
A012: 0D              DEC     C                   
A013: 1D              DEC     E                   
A014: 0E 04           LD      C,$04               
A016: 0A              LD      A,(BC)              
A017: 05              DEC     B                   
A018: 0A              LD      A,(BC)              
A019: 43              LD      B,E                 
A01A: 03              INC     BC                  
A01B: 67              LD      H,A                 
A01C: 81              ADD     A,C                 
A01D: 03              INC     BC                  
A01E: 3F              CCF                         
A01F: 3E 04           LD      A,$04               
A021: 0D              DEC     C                   
A022: 5F              LD      E,A                 
A023: BE              CP      (HL)                
A024: C8              RET     Z                   
A025: 16 33           LD      D,$33               
A027: 48              LD      C,B                 
A028: C9              RET                         
A029: 54              LD      D,H                 
A02A: B5              OR      L                   
A02B: B7              OR      A                   
A02C: B2              OR      D                   
A02D: 17              RLA                         
A02E: 2E 9E           LD      L,$9E               
A030: 0C              INC     C                   
A031: 0C              INC     C                   
A032: 01 06 01        LD      BC,$0106            
A035: 01 6A 02        LD      BC,$026A            
A038: 0D              DEC     C                   
A039: C1              POP     BC                  
A03A: C0              RET     NZ                  
A03B: D0              RET     NC                  
A03C: 15              DEC     D                   
A03D: 13              INC     DE                  
A03E: 54              LD      D,H                 
A03F: AF              XOR     A                   
A040: 6E              LD      L,(HL)              
A041: 83              ADD     A,E                 
A042: 61              LD      H,C                 
A043: 24              INC     H                   
A044: 56              LD      D,(HL)              
A045: 45              LD      B,L                 
A046: 6E              LD      L,(HL)              
A047: 80              ADD     A,B                 
A048: AE              XOR     (HL)                
A049: DB 05           IN      A,($05)             
A04B: A0              AND     B                   
A04C: 03              INC     BC                  
A04D: 1D              DEC     E                   
A04E: 04              INC     B                   
A04F: 1B              DEC     DE                  
A050: 5F              LD      E,A                 
A051: BE              CP      (HL)                
A052: 5B              LD      E,E                 
A053: B1              OR      C                   
A054: 4B              LD      C,E                 
A055: 7B              LD      A,E                 
A056: 54              LD      D,H                 
A057: 45              LD      B,L                 
A058: 73              LD      (HL),E              
A059: 9E              SBC     (HL)                
A05A: 56              LD      D,(HL)              
A05B: D1              POP     DE                  
A05C: 03              INC     BC                  
A05D: 71              LD      (HL),C              
A05E: 84              ADD     A,H                 
A05F: 15              DEC     D                   
A060: 30 60           JR      NC,$A0C2            ; {}
A062: 62              LD      H,D                 
A063: 17              RLA                         
A064: F4 72 4A        CALL    P,$4A72             
A067: 5E              LD      E,(HL)              
A068: 2F              CPL                         
A069: 62              LD      H,D                 
A06A: 2E 0C           LD      L,$0C               
A06C: 01 10 08        LD      BC,$0810            
A06F: 77              LD      (HL),A              
A070: 0E 75           LD      C,$75               
A072: 0D              DEC     C                   
A073: 25              DEC     H                   
A074: 03              INC     BC                  
A075: 90              SUB     B                   
A076: 01 1F 20        LD      BC,$201F            
A079: 5F              LD      E,A                 
A07A: BE              CP      (HL)                
A07B: 84              ADD     A,H                 
A07C: 15              DEC     D                   
A07D: 30 60           JR      NC,$A0DF            ; {}
A07F: 62              LD      H,D                 
A080: 17              RLA                         
A081: F4 72 4B        CALL    P,$4B72             
A084: 5E              LD      E,(HL)              
A085: D5              PUSH    DE                  
A086: B5              OR      L                   
A087: 89              ADC     A,C                 
A088: 8D              ADC     A,L                 
A089: FB              EI                          
A08A: 8E              ADC     A,(HL)              
A08B: 7B              LD      A,E                 
A08C: 67              LD      H,A                 
A08D: 23              INC     HL                  
A08E: B8              CP      B                   
A08F: AB              XOR     E                   
A090: 98              SBC     B                   
A091: 8E              ADC     A,(HL)              
A092: 48              LD      C,B                 
A093: AF              XOR     A                   
A094: 14              INC     D                   
A095: E3              EX      (SP),HL             
A096: 61              LD      H,C                 
A097: CF              RST     0X08                
A098: 98              SBC     B                   
A099: 0D              DEC     C                   
A09A: 25              DEC     H                   
A09B: 03              INC     BC                  
A09C: 91              SUB     C                   
A09D: 01 1F 20        LD      BC,$201F            
A0A0: 5F              LD      E,A                 
A0A1: BE              CP      (HL)                
A0A2: 84              ADD     A,H                 
A0A3: 15              DEC     D                   
A0A4: 30 60           JR      NC,$A106            ; {}
A0A6: 62              LD      H,D                 
A0A7: 17              RLA                         
A0A8: F4 72 4B        CALL    P,$4B72             
A0AB: 5E              LD      E,(HL)              
A0AC: C8              RET     Z                   
A0AD: B5              OR      L                   
A0AE: 55              LD      D,L                 
A0AF: 8B              ADC     A,E                 
A0B0: 90              SUB     B                   
A0B1: 73              LD      (HL),E              
A0B2: C3 6A 33        JP      $336A               
A0B5: 98              SBC     B                   
A0B6: 67              LD      H,A                 
A0B7: 4D              LD      C,L                 
A0B8: 90              SUB     B                   
A0B9: A5              AND     L                   
A0BA: CE 6A           ADC     $6A                 
A0BC: 26 A1           LD      H,$A1               
A0BE: 47              LD      B,A                 
A0BF: 62              LD      H,D                 
A0C0: 0D              DEC     C                   
A0C1: 25              DEC     H                   
A0C2: 03              INC     BC                  
A0C3: 92              SUB     D                   
A0C4: 01 1F 20        LD      BC,$201F            
A0C7: 5F              LD      E,A                 
A0C8: BE              CP      (HL)                
A0C9: 84              ADD     A,H                 
A0CA: 15              DEC     D                   
A0CB: 30 60           JR      NC,$A12D            ; {}
A0CD: 62              LD      H,D                 
A0CE: 17              RLA                         
A0CF: F4 72 4B        CALL    P,$4B72             
A0D2: 5E              LD      E,(HL)              
A0D3: C8              RET     Z                   
A0D4: B5              OR      L                   
A0D5: 55              LD      D,L                 
A0D6: 8B              ADC     A,E                 
A0D7: 90              SUB     B                   
A0D8: 73              LD      (HL),E              
A0D9: C3 6A 33        JP      $336A               
A0DC: 98              SBC     B                   
A0DD: 67              LD      H,A                 
A0DE: 4D              LD      C,L                 
A0DF: 90              SUB     B                   
A0E0: A5              AND     L                   
A0E1: D9              EXX                         
A0E2: 6A              LD      L,D                 
A0E3: 3E 7A           LD      A,$7A               
A0E5: F9              LD      SP,HL               
A0E6: 8E              ADC     A,(HL)              
A0E7: 02              LD      (BC),A              
A0E8: 0E F6           LD      C,$F6               
A0EA: B2              OR      D                   
A0EB: FB              EI                          
A0EC: 17              RLA                         
A0ED: 53              LD      D,E                 
A0EE: BE              CP      (HL)                
A0EF: AF              XOR     A                   
A0F0: 6E              LD      L,(HL)              
A0F1: 83              ADD     A,E                 
A0F2: 61              LD      H,C                 
A0F3: 62              LD      H,D                 
A0F4: B9              CP      C                   
A0F5: 2F              CPL                         
A0F6: 62              LD      H,D                 
A0F7: 00              NOP                         
A0F8: 03              INC     BC                  
A0F9: 00              NOP                         
A0FA: 00              NOP                         
A0FB: 80              ADD     A,B                 
A0FC: 00              NOP                         
A0FD: 03              INC     BC                  
A0FE: 00              NOP                         
A0FF: 00              NOP                         
A100: 80              ADD     A,B                 
A101: 5E              LD      E,(HL)              
A102: 2B              DEC     HL                  
A103: 94              SUB     H                   
A104: 07              RLCA                        
A105: 80              ADD     A,B                 
A106: 07              RLCA                        
A107: 1E 0D           LD      E,$0D               
A109: 1C              INC     E                   
A10A: C4 04 15        CALL    NZ,$1504            
A10D: 1D              DEC     E                   
A10E: 85              ADD     A,L                 
A10F: 01 4F 41        LD      BC,$414F            
A112: A0              AND     B                   
A113: EB              EX      DE,HL               
A114: 8F              ADC     A,A                 
A115: C7              RST     0X00                
A116: DE 57           SBC     $57                 
A118: 17              RLA                         
A119: 11 BC 83        LD      DE,$83BC            
A11C: 66              LD      H,(HL)              
A11D: 44              LD      B,H                 
A11E: 45              LD      B,L                 
A11F: E4 9F 21        CALL    PO,$219F            
A122: 1C              INC     E                   
A123: 01 1D 4B        LD      BC,$4B1D            
A126: 02              LD      (BC),A              
A127: 06 CE           LD      B,$CE               
A129: 56              LD      D,(HL)              
A12A: 8E              ADC     A,(HL)              
A12B: 7A              LD      A,D                 
A12C: 23              INC     HL                  
A12D: 62              LD      H,D                 
A12E: 5E              LD      E,(HL)              
A12F: 5C              LD      E,H                 
A130: 95              SUB     L                   
A131: 07              RLCA                        
A132: 80              ADD     A,B                 
A133: 07              RLCA                        
A134: 4F              LD      C,A                 
A135: 0D              DEC     C                   
A136: 4D              LD      C,L                 
A137: C4 04 46        CALL    NZ,$4604            
A13A: 13              INC     DE                  
A13B: 9F              SBC     A                   
A13C: E9              JP      (HL)                
A13D: 99              SBC     C                   
A13E: C0              RET     NZ                  
A13F: 16 51           LD      D,$51               
A141: 5E              LD      E,(HL)              
A142: 96              SUB     (HL)                
A143: 64              LD      H,H                 
A144: DB 72           IN      A,($72)             
A146: CE 56           ADC     $56                 
A148: 8E              ADC     A,(HL)              
A149: 7A              LD      A,D                 
A14A: 3D              DEC     A                   
A14B: 62              LD      H,D                 
A14C: 4F              LD      C,A                 
A14D: 15              DEC     D                   
A14E: F3              DI                          
A14F: 8C              ADC     A,H                 
A150: 6B              LD      L,E                 
A151: BF              CP      A                   
A152: 5F              LD      E,A                 
A153: BE              CP      (HL)                
A154: 56              LD      D,(HL)              
A155: 15              DEC     D                   
A156: 44              LD      B,H                 
A157: A0              AND     B                   
A158: 90              SUB     B                   
A159: 14              INC     D                   
A15A: 04              INC     B                   
A15B: 58              LD      E,B                 
A15C: FD ; ????
A15D: B2              OR      D                   
A15E: EB              EX      DE,HL               
A15F: 5D              LD      E,L                 
A160: 73              LD      (HL),E              
A161: 7B              LD      A,E                 
A162: 4B              LD      C,E                 
A163: 7B              LD      A,E                 
A164: 6E              LD      L,(HL)              
A165: B1              OR      C                   
A166: 95              SUB     L                   
A167: 5F              LD      E,A                 
A168: 91              SUB     C                   
A169: 7A              LD      A,D                 
A16A: 73              LD      (HL),E              
A16B: 15              DEC     D                   
A16C: 6B              LD      L,E                 
A16D: B5              OR      L                   
A16E: 47              LD      B,A                 
A16F: 55              LD      D,L                 
A170: 36 6D           LD      (HL),$6D            
A172: E1              POP     HL                  
A173: 14              INC     D                   
A174: 7A              LD      A,D                 
A175: C4 09 EE        CALL    NZ,$EE09            
A178: 62              LD      H,D                 
A179: 49              LD      C,C                 
A17A: D2 06 55        JP      NC,$5506            
A17D: 9F              SBC     A                   
A17E: 01 A0 1C        LD      BC,$1CA0            
A181: 01 1D 4B        LD      BC,$4B1D            
A184: 02              LD      (BC),A              
A185: 06 CE           LD      B,$CE               
A187: 56              LD      D,(HL)              
A188: 8E              ADC     A,(HL)              
A189: 7A              LD      A,D                 
A18A: 23              INC     HL                  
A18B: 62              LD      H,D                 
A18C: 5E              LD      E,(HL)              
A18D: 69              LD      L,C                 
A18E: 97              SUB     A                   
A18F: 07              RLCA                        
A190: 80              ADD     A,B                 
A191: 07              RLCA                        
A192: 5C              LD      E,H                 
A193: 0D              DEC     C                   
A194: 5A              LD      E,D                 
A195: C4 04 54        CALL    NZ,$5404            
A198: E9              JP      (HL)                
A199: C5              PUSH    BC                  
A19A: 84              ADD     A,H                 
A19B: 96              SUB     (HL)                
A19C: D0              RET     NC                  
A19D: 60              LD      H,B                 
A19E: C6 6A           ADD     $6A                 
A1A0: 66              LD      H,(HL)              
A1A1: 7B              LD      A,E                 
A1A2: 2C              INC     L                   
A1A3: C6 16           ADD     $16                 
A1A5: 60              LD      H,B                 
A1A6: 82              ADD     A,D                 
A1A7: 17              RLA                         
A1A8: 49              LD      C,C                 
A1A9: 5E              LD      E,(HL)              
A1AA: 74              LD      (HL),H              
A1AB: 8D              ADC     A,L                 
A1AC: 51              LD      D,C                 
A1AD: 5E              LD      E,(HL)              
A1AE: F0              RET     P                   
A1AF: A4              AND     H                   
A1B0: C3 B5 33        JP      $33B5               
A1B3: 98              SBC     B                   
A1B4: 4A              LD      C,D                 
A1B5: 45              LD      B,L                 
A1B6: 14              INC     D                   
A1B7: 9E              SBC     (HL)                
A1B8: 11 58 96        LD      DE,$9658            
A1BB: 64              LD      H,H                 
A1BC: EF              RST     0X28                
A1BD: 74              LD      (HL),H              
A1BE: 4B              LD      C,E                 
A1BF: 5E              LD      E,(HL)              
A1C0: 1A              LD      A,(DE)              
A1C1: 98              SBC     B                   
A1C2: 49              LD      C,C                 
A1C3: 16 AB           LD      D,$AB               
A1C5: 98              SBC     B                   
A1C6: 9E              SBC     (HL)                
A1C7: 48              LD      C,B                 
A1C8: CB B5           RES     6,L                 
A1CA: D4 B5 3F        CALL    NC,$3FB5            
A1CD: 61              LD      H,C                 
A1CE: 57              LD      D,A                 
A1CF: 49              LD      C,C                 
A1D0: AB              XOR     E                   
A1D1: 57              LD      D,A                 
A1D2: 5F              LD      E,A                 
A1D3: BE              CP      (HL)                
A1D4: 44              LD      B,H                 
A1D5: DB 7B           IN      A,($7B)             
A1D7: 60              LD      H,B                 
A1D8: 85              ADD     A,L                 
A1D9: 96              SUB     (HL)                
A1DA: D9              EXX                         
A1DB: B0              OR      B                   
A1DC: 90              SUB     B                   
A1DD: 8C              ADC     A,H                 
A1DE: C3 6A F3        JP      $F36A               
A1E1: 8C              ADC     A,H                 
A1E2: 4F              LD      C,A                 
A1E3: A1              AND     C                   
A1E4: 96              SUB     (HL)                
A1E5: AF              XOR     A                   
A1E6: DB 72           IN      A,($72)             
A1E8: FB              EI                          
A1E9: A5              AND     L                   
A1EA: 99              SBC     C                   
A1EB: 53              LD      D,E                 
A1EC: 17              RLA                         
A1ED: 89              ADC     A,C                 
A1EE: 97              SUB     A                   
A1EF: 02              LD      (BC),A              
A1F0: 06 CE           LD      B,$CE               
A1F2: 56              LD      D,(HL)              
A1F3: 8E              ADC     A,(HL)              
A1F4: 7A              LD      A,D                 
A1F5: 23              INC     HL                  
A1F6: 62              LD      H,D                 
A1F7: 5E              LD      E,(HL)              
A1F8: 2E 99           LD      L,$99               
A1FA: 07              RLCA                        
A1FB: 80              ADD     A,B                 
A1FC: 07              RLCA                        
A1FD: 21 0D 1F        LD      HL,$1F0D            
A200: C4 04 1C        CALL    NZ,$1C04            
A203: C7              RST     0X00                
A204: DE 94           SBC     $94                 
A206: 14              INC     D                   
A207: 57              LD      D,A                 
A208: 5E              LD      E,(HL)              
A209: C4 97 DB        CALL    NZ,$DB97            
A20C: 8B              ADC     A,E                 
A20D: 6B              LD      L,E                 
A20E: BF              CP      A                   
A20F: 50              LD      D,B                 
A210: 47              LD      B,A                 
A211: E6 5F           AND     $5F                 
A213: 82              ADD     A,D                 
A214: 17              RLA                         
A215: 57              LD      D,A                 
A216: 62              LD      H,D                 
A217: EB              EX      DE,HL               
A218: 14              INC     D                   
A219: 90              SUB     B                   
A21A: 8C              ADC     A,H                 
A21B: F4 59 5B        CALL    P,$5B59             
A21E: BB              CP      E                   
A21F: 02              LD      (BC),A              
A220: 06 CE           LD      B,$CE               
A222: 56              LD      D,(HL)              
A223: 8E              ADC     A,(HL)              
A224: 7A              LD      A,D                 
A225: 23              INC     HL                  
A226: 62              LD      H,D                 
A227: 5B              LD      E,E                 
A228: 81              ADD     A,C                 
A229: 6B              LD      L,E                 
A22A: 00              NOP                         
A22B: 00              NOP                         
A22C: 90              SUB     B                   
A22D: 03              INC     BC                  
A22E: 22 04 20        LD      ($2004),HL          
A231: 6C              LD      L,H                 
A232: BE              CP      (HL)                
A233: 1B              DEC     DE                  
A234: 60              LD      H,B                 
A235: 8D              ADC     A,L                 
A236: 7A              LD      A,D                 
A237: 03              INC     BC                  
A238: 71              LD      (HL),C              
A239: CD 9A 94        CALL    $949A               ; {}
A23C: 14              INC     D                   
A23D: 45              LD      B,L                 
A23E: 5E              LD      E,(HL)              
A23F: D9              EXX                         
A240: B0              OR      B                   
A241: 90              SUB     B                   
A242: 8C              ADC     A,H                 
A243: C3 6A F3        JP      $F36A               
A246: 8C              ADC     A,H                 
A247: 4F              LD      C,A                 
A248: A1              AND     C                   
A249: 96              SUB     (HL)                
A24A: AF              XOR     A                   
A24B: DB 72           IN      A,($72)             
A24D: FB              EI                          
A24E: A5              AND     L                   
A24F: 99              SBC     C                   
A250: 53              LD      D,E                 
A251: 07              RLCA                        
A252: 81              ADD     A,C                 
A253: 1C              INC     E                   
A254: 0D              DEC     C                   
A255: 81              ADD     A,C                 
A256: 19              ADD     HL,DE               
A257: 0A              LD      A,(BC)              
A258: 09              ADD     HL,BC               
A259: 0E 81           LD      C,$81               
A25B: 14              INC     D                   
A25C: 0D              DEC     C                   
A25D: 80              ADD     A,B                 
A25E: 81              ADD     A,C                 
A25F: 09              ADD     HL,BC               
A260: 5C              LD      E,H                 
A261: 04              INC     B                   
A262: 79              LD      A,C                 
A263: 09              ADD     HL,BC               
A264: BA              CP      D                   
A265: E3              EX      (SP),HL             
A266: 93              SUB     E                   
A267: AB              XOR     E                   
A268: 98              SBC     B                   
A269: 8E              ADC     A,(HL)              
A26A: 48              LD      C,B                 
A26B: 5E              LD      E,(HL)              
A26C: 17              RLA                         
A26D: EA 48 91        JP      PE,$9148            ; {}
A270: 7A              LD      A,D                 
A271: 96              SUB     (HL)                
A272: 14              INC     D                   
A273: 82              ADD     A,D                 
A274: 17              RLA                         
A275: 56              LD      D,(HL)              
A276: 5E              LD      E,(HL)              
A277: 87              ADD     A,A                 
A278: 74              LD      (HL),H              
A279: 10 B7           DJNZ    $A232               ; {}
A27B: 0B              DEC     BC                  
A27C: 5C              LD      E,H                 
A27D: C3 9E AF        JP      $AF9E               ; {}
A280: 55              LD      D,L                 
A281: 8F              ADC     A,A                 
A282: 49              LD      C,C                 
A283: 75              LD      (HL),L              
A284: B1              OR      C                   
A285: 51              LD      D,C                 
A286: 18 4D           JR      $A2D5               ; {}
A288: C2 46 7A        JP      NZ,$7A46            ; {}
A28B: 63              LD      H,E                 
A28C: 16 9F           LD      D,$9F               
A28E: 9B              SBC     E                   
A28F: BF              CP      A                   
A290: 14              INC     D                   
A291: 03              INC     BC                  
A292: BC              CP      H                   
A293: DB B5           IN      A,($B5)             
A295: 1B              DEC     DE                  
A296: A1              AND     C                   
A297: 67              LD      H,A                 
A298: 66              LD      H,(HL)              
A299: 16 8A           LD      D,$8A               
A29B: DB 72           IN      A,($72)             
A29D: 70              LD      (HL),B              
A29E: CA DB 9F        JP      Z,$9FDB             ; {}
A2A1: C3 9E 5F        JP      $5F9E               ; {}
A2A4: BE              CP      (HL)                
A2A5: 23              INC     HL                  
A2A6: 7B              LD      A,E                 
A2A7: 03              INC     BC                  
A2A8: BA              CP      D                   
A2A9: CE 98           ADC     $98                 
A2AB: 51              LD      D,C                 
A2AC: 18 54           JR      $A302               ; {}
A2AE: C2 8E 5F        JP      NZ,$5F8E            ; {}
A2B1: 6F              LD      L,A                 
A2B2: 7C              LD      A,H                 
A2B3: 51              LD      D,C                 
A2B4: 18 23           JR      $A2D9               ; {}
A2B6: C6 FE           ADD     $FE                 
A2B8: 67              LD      H,A                 
A2B9: 1F              RRA                         
A2BA: 8F              ADC     A,A                 
A2BB: A9              XOR     C                   
A2BC: 15              DEC     D                   
A2BD: B8              CP      B                   
A2BE: D0              RET     NC                  
A2BF: 46              LD      B,(HL)              
A2C0: 62              LD      H,D                 
A2C1: D6 15           SUB     $15                 
A2C3: D5              PUSH    DE                  
A2C4: 15              DEC     D                   
A2C5: 89              ADC     A,C                 
A2C6: 17              RLA                         
A2C7: CE 9C           ADC     $9C                 
A2C9: 7F              LD      A,A                 
A2CA: 49              LD      C,C                 
A2CB: 89              ADC     A,C                 
A2CC: 17              RLA                         
A2CD: 09              ADD     HL,BC               
A2CE: 15              DEC     D                   
A2CF: 90              SUB     B                   
A2D0: 14              INC     D                   
A2D1: 82              ADD     A,D                 
A2D2: DF              RST     0X18                
A2D3: 91              SUB     C                   
A2D4: 7A              LD      A,D                 
A2D5: 84              ADD     A,H                 
A2D6: 14              INC     D                   
A2D7: 36 A1           LD      (HL),$A1            
A2D9: D6 15           SUB     $15                 
A2DB: 2E 1C           LD      L,$1C               
A2DD: 01 1D 4B        LD      BC,$4B1D            
A2E0: 0D              DEC     C                   
A2E1: 80              ADD     A,B                 
A2E2: 8D              ADC     A,L                 
A2E3: 0E 06           LD      C,$06               
A2E5: 09              ADD     HL,BC               
A2E6: 32 09 28        LD      ($2809),A           
A2E9: 09              ADD     HL,BC               
A2EA: 24              INC     H                   
A2EB: 04              INC     B                   
A2EC: 7F              LD      A,A                 
A2ED: C7              RST     0X00                
A2EE: DE 2B           SBC     $2B                 
A2F0: 17              RLA                         
A2F1: 83              ADD     A,E                 
A2F2: 7A              LD      A,D                 
A2F3: 89              ADC     A,C                 
A2F4: 4E              LD      C,(HL)              
A2F5: CB D2           SET     2,D                 
A2F7: 89              ADC     A,C                 
A2F8: 5B              LD      E,E                 
A2F9: 91              SUB     C                   
A2FA: 96              SUB     (HL)                
A2FB: 96              SUB     (HL)                
A2FC: 96              SUB     (HL)                
A2FD: DB 72           IN      A,($72)             
A2FF: 90              SUB     B                   
A300: 91              SUB     C                   
A301: 45              LD      B,L                 
A302: DB 63           IN      A,($63)             
A304: B1              OR      C                   
A305: 74              LD      (HL),H              
A306: C0              RET     NZ                  
A307: 4B              LD      C,E                 
A308: 62              LD      H,D                 
A309: AB              XOR     E                   
A30A: 55              LD      D,L                 
A30B: C3 D1 AB        JP      $ABD1               ; {}
A30E: 98              SBC     B                   
A30F: 03              INC     BC                  
A310: A0              AND     B                   
A311: 5F              LD      E,A                 
A312: BE              CP      (HL)                
A313: 56              LD      D,(HL)              
A314: 15              DEC     D                   
A315: 44              LD      B,H                 
A316: A0              AND     B                   
A317: 55              LD      D,L                 
A318: F4 FE C3        CALL    P,$C3FE             
A31B: 96              SUB     (HL)                
A31C: 61              LD      H,C                 
A31D: 5B              LD      E,E                 
A31E: DB 1B           IN      A,($1B)             
A320: A1              AND     C                   
A321: 67              LD      H,A                 
A322: 66              LD      H,(HL)              
A323: 03              INC     BC                  
A324: 8A              ADC     A,D                 
A325: BF              CP      A                   
A326: 14              INC     D                   
A327: D3 B2           OUT     ($B2),A             
A329: AB              XOR     E                   
A32A: 98              SBC     B                   
A32B: 4B              LD      C,E                 
A32C: A4              AND     H                   
A32D: 91              SUB     C                   
A32E: 96              SUB     (HL)                
A32F: 9B              SBC     E                   
A330: 96              SUB     (HL)                
A331: 34              INC     (HL)                
A332: A1              AND     C                   
A333: 3F              CCF                         
A334: 16 C3           LD      D,$C3               
A336: 6A              LD      L,D                 
A337: D1              POP     DE                  
A338: B5              OR      L                   
A339: 5B              LD      E,E                 
A33A: 98              SBC     B                   
A33B: C3 9E 5F        JP      $5F9E               ; {}
A33E: BE              CP      (HL)                
A33F: E4 14 96        CALL    PO,$9614            ; {}
A342: 5F              LD      E,A                 
A343: 2F              CPL                         
A344: C6 D5           ADD     $D5                 
A346: B5              OR      L                   
A347: 90              SUB     B                   
A348: BE              CP      (HL)                
A349: CB 6E           BIT     5,(HL)              
A34B: C7              RST     0X00                
A34C: DE 5B           SBC     $5B                 
A34E: F4 1B A1        CALL    P,$A11B             ; {}
A351: 55              LD      D,L                 
A352: A4              AND     H                   
A353: D1              POP     DE                  
A354: B5              OR      L                   
A355: 73              LD      (HL),E              
A356: C6 A5           ADD     $A5                 
A358: B7              OR      A                   
A359: 0E A0           LD      C,$A0               
A35B: CE B5           ADC     $B5                 
A35D: 7F              LD      A,A                 
A35E: 49              LD      C,C                 
A35F: F3              DI                          
A360: B4              OR      H                   
A361: 78              LD      A,B                 
A362: 98              SBC     B                   
A363: 23              INC     HL                  
A364: 62              LD      H,D                 
A365: 6B              LD      L,E                 
A366: BF              CP      A                   
A367: F3              DI                          
A368: 49              LD      C,C                 
A369: B0              OR      B                   
A36A: 85              ADD     A,L                 
A36B: 2E 1C           LD      L,$1C               
A36D: 01 1D 4B        LD      BC,$4B1D            
A370: 08              EX      AF,AF'              
A371: 18 1F           JR      $A392               ; {}
A373: 16 5F           LD      D,$5F               
A375: BE              CP      (HL)                
A376: 90              SUB     B                   
A377: 14              INC     D                   
A378: 0B              DEC     BC                  
A379: C0              RET     NZ                  
A37A: 2F              CPL                         
A37B: 49              LD      C,C                 
A37C: E4 14 FE        CALL    PO,$FE14            
A37F: 49              LD      C,C                 
A380: 91              SUB     C                   
A381: 7A              LD      A,D                 
A382: 38 15           JR      C,$A399             ; {}
A384: 43              LD      B,E                 
A385: 62              LD      H,D                 
A386: 1F              RRA                         
A387: D1              POP     DE                  
A388: 59              LD      E,C                 
A389: B1              OR      C                   
A38A: 02              LD      (BC),A              
A38B: 09              ADD     HL,BC               
A38C: 73              LD      (HL),E              
A38D: 74              LD      (HL),H              
A38E: 33              INC     SP                  
A38F: B1              OR      C                   
A390: C3 9E 9E        JP      $9E9E               ; {}
A393: 48              LD      C,B                 
A394: 53              LD      D,E                 
A395: 5B              LD      E,E                 
A396: 22 00 00        LD      ($0000),HL          
A399: 80              ADD     A,B                 
A39A: 03              INC     BC                  
A39B: 14              INC     D                   
A39C: 04              INC     B                   
A39D: 12              LD      (DE),A              
A39E: 5F              LD      E,A                 
A39F: BE              CP      (HL)                
A3A0: 5B              LD      E,E                 
A3A1: B1              OR      C                   
A3A2: 4B              LD      C,E                 
A3A3: 7B              LD      A,E                 
A3A4: 46              LD      B,(HL)              
A3A5: 45              LD      B,L                 
A3A6: 86              ADD     A,(HL)              
A3A7: 5F              LD      E,A                 
A3A8: 8E              ADC     A,(HL)              
A3A9: 14              INC     D                   
A3AA: 30 79           JR      NC,$A425            ; {}
A3AC: 9F              SBC     A                   
A3AD: 15              DEC     D                   
A3AE: 7F              LD      A,A                 
A3AF: B1              OR      C                   
A3B0: 02              LD      (BC),A              
A3B1: 07              RLCA                        
A3B2: E3              EX      (SP),HL             
A3B3: 59              LD      E,C                 
A3B4: 03              INC     BC                  
A3B5: 58              LD      E,B                 
A3B6: 87              ADD     A,A                 
A3B7: 8C              ADC     A,H                 
A3B8: 4E              LD      C,(HL)              
A3B9: 5B              LD      E,E                 
A3BA: 7C              LD      A,H                 
A3BB: DB 05           IN      A,($05)             
A3BD: 90              SUB     B                   
A3BE: 03              INC     BC                  
A3BF: 77              LD      (HL),A              
A3C0: 0D              DEC     C                   
A3C1: 75              LD      (HL),L              
A3C2: 17              RLA                         
A3C3: 8B              ADC     A,E                 
A3C4: 00              NOP                         
A3C5: 17              RLA                         
A3C6: 8A              ADC     A,D                 
A3C7: DB 38           IN      A,($38)             
A3C9: 04              INC     B                   
A3CA: 6C              LD      L,H                 
A3CB: 63              LD      H,E                 
A3CC: 98              SBC     B                   
A3CD: 03              INC     BC                  
A3CE: B1              OR      C                   
A3CF: 03              INC     BC                  
A3D0: EE 83           XOR     $83                 
A3D2: 96              SUB     (HL)                
A3D3: 87              ADD     A,A                 
A3D4: 8C              ADC     A,H                 
A3D5: 84              ADD     A,H                 
A3D6: 96              SUB     (HL)                
A3D7: D0              RET     NC                  
A3D8: 60              LD      H,B                 
A3D9: CB 6A           BIT     5,D                 
A3DB: D5              PUSH    DE                  
A3DC: B5              OR      L                   
A3DD: AB              XOR     E                   
A3DE: AD              XOR     L                   
A3DF: AB              XOR     E                   
A3E0: B2              OR      D                   
A3E1: AB              XOR     E                   
A3E2: 98              SBC     B                   
A3E3: 03              INC     BC                  
A3E4: A0              AND     B                   
A3E5: 5F              LD      E,A                 
A3E6: BE              CP      (HL)                
A3E7: 84              ADD     A,H                 
A3E8: 15              DEC     D                   
A3E9: 30 A1           JR      NC,$A38C            ; {}
A3EB: AB              XOR     E                   
A3EC: 57              LD      D,A                 
A3ED: 73              LD      (HL),E              
A3EE: 7B              LD      A,E                 
A3EF: 81              ADD     A,C                 
A3F0: 8D              ADC     A,L                 
A3F1: CB 87           RES     0,A                 
A3F3: D3 C5           OUT     ($C5),A             
A3F5: 73              LD      (HL),E              
A3F6: 49              LD      C,C                 
A3F7: C7              RST     0X00                
A3F8: DE 90           SBC     $90                 
A3FA: 14              INC     D                   
A3FB: 15              DEC     D                   
A3FC: 58              LD      E,B                 
A3FD: 55              LD      D,L                 
A3FE: 4A              LD      C,D                 
A3FF: 71              LD      (HL),C              
A400: 13              INC     DE                  
A401: E7              RST     0X20                
A402: 8B              ADC     A,E                 
A403: 81              ADD     A,C                 
A404: A6              AND     (HL)                
A405: AC              XOR     H                   
A406: A2              AND     D                   
A407: 9F              SBC     A                   
A408: 15              DEC     D                   
A409: E9              JP      (HL)                
A40A: 16 9E           LD      D,$9E               
A40C: 7A              LD      A,D                 
A40D: C3 B5 16        JP      $16B5               
A410: BC              CP      H                   
A411: DB 72           IN      A,($72)             
A413: 24              INC     H                   
A414: 56              LD      D,(HL)              
A415: 43              LD      B,E                 
A416: 5E              LD      E,(HL)              
A417: 33              INC     SP                  
A418: 98              SBC     B                   
A419: 5F              LD      E,A                 
A41A: BE              CP      (HL)                
A41B: 92              SUB     D                   
A41C: 96              SUB     (HL)                
A41D: 50              LD      D,B                 
A41E: 9F              SBC     A                   
A41F: 0B              DEC     BC                  
A420: C0              RET     NZ                  
A421: B5              OR      L                   
A422: D0              RET     NC                  
A423: 9B              SBC     E                   
A424: C1              POP     BC                  
A425: DB 72           IN      A,($72)             
A427: 5F              LD      E,A                 
A428: BE              CP      (HL)                
A429: 84              ADD     A,H                 
A42A: 96              SUB     (HL)                
A42B: E1              POP     HL                  
A42C: 5F              LD      E,A                 
A42D: 35              DEC     (HL)                
A42E: 92              SUB     D                   
A42F: CF              RST     0X08                
A430: 17              RLA                         
A431: 7B              LD      A,E                 
A432: B4              OR      H                   
A433: 03              INC     BC                  
A434: BA              CP      D                   
A435: 17              RLA                         
A436: 8D              ADC     A,L                 
A437: 70              LD      (HL),B              
A438: 81              ADD     A,C                 
A439: BD              CP      L                   
A43A: E8              RET     PE                  
A43B: 05              DEC     B                   
A43C: 90              SUB     B                   
A43D: 03              INC     BC                  
A43E: 2C              INC     L                   
A43F: 04              INC     B                   
A440: 2A 83 48        LD      HL,($4883)          
A443: BE              CP      (HL)                
A444: 9F              SBC     A                   
A445: EC 16 E2        CALL    PE,$E216            
A448: A0              AND     B                   
A449: E6 5F           AND     $5F                 
A44B: A3              AND     E                   
A44C: A0              AND     B                   
A44D: FB              EI                          
A44E: B9              CP      C                   
A44F: 4D              LD      C,L                 
A450: 98              SBC     B                   
A451: 9F              SBC     A                   
A452: 15              DEC     D                   
A453: 7F              LD      A,A                 
A454: B1              OR      C                   
A455: 9F              SBC     A                   
A456: 15              DEC     D                   
A457: 57              LD      D,A                 
A458: 17              RLA                         
A459: 75              LD      (HL),L              
A45A: 61              LD      H,C                 
A45B: 89              ADC     A,C                 
A45C: 17              RLA                         
A45D: AF              XOR     A                   
A45E: 14              INC     D                   
A45F: DE 14           SBC     $14                 
A461: 90              SUB     B                   
A462: 5F              LD      E,A                 
A463: 91              SUB     C                   
A464: 7A              LD      A,D                 
A465: A3              AND     E                   
A466: 15              DEC     D                   
A467: C9              RET                         
A468: B5              OR      L                   
A469: A7              AND     A                   
A46A: C5              PUSH    BC                  
A46B: 07              RLCA                        
A46C: 62              LD      H,D                 
A46D: 0D              DEC     C                   
A46E: 60              LD      H,B                 
A46F: 0E 05           LD      C,$05               
A471: C4 0A 0E        CALL    NZ,$0E0A            
A474: 0A              LD      A,(BC)              
A475: 57              LD      D,A                 
A476: 04              INC     B                   
A477: 53              LD      D,E                 
A478: 4B              LD      C,E                 
A479: 49              LD      C,C                 
A47A: C7              RST     0X00                
A47B: DE AF           SBC     $AF                 
A47D: 14              INC     D                   
A47E: 50              LD      D,B                 
A47F: 6D              LD      L,L                 
A480: 89              ADC     A,C                 
A481: 17              RLA                         
A482: 71              LD      (HL),C              
A483: 16 7E           LD      D,$7E               
A485: CA 9F 15        JP      Z,$159F             
A488: 2B              DEC     HL                  
A489: 17              RLA                         
A48A: 57              LD      D,A                 
A48B: 7B              LD      A,E                 
A48C: CA B5 4B        JP      Z,$4BB5             
A48F: 7B              LD      A,E                 
A490: 30 6F           JR      NC,$A501            ; {}
A492: 90              SUB     B                   
A493: 14              INC     D                   
A494: 12              LD      (DE),A              
A495: 58              LD      E,B                 
A496: 50              LD      D,B                 
A497: 9F              SBC     A                   
A498: 0B              DEC     BC                  
A499: C0              RET     NZ                  
A49A: 73              LD      (HL),E              
A49B: 7B              LD      A,E                 
A49C: 73              LD      (HL),E              
A49D: 49              LD      C,C                 
A49E: C7              RST     0X00                
A49F: DE BF           SBC     $BF                 
A4A1: 06 44           LD      B,$44               
A4A3: 2C              INC     L                   
A4A4: 4F              LD      C,A                 
A4A5: 8B              ADC     A,E                 
A4A6: BE              CP      (HL)                
A4A7: 06 FC           LD      B,$FC               
A4A9: 25              DEC     H                   
A4AA: 46              LD      B,(HL)              
A4AB: 6E              LD      L,(HL)              
A4AC: 43              LD      B,E                 
A4AD: 18 C6           JR      $A475               ; {}
A4AF: 06 64           LD      B,$64               
A4B1: C5              PUSH    BC                  
A4B2: DB 14           IN      A,($14)             
A4B4: FB              EI                          
A4B5: C0              RET     NZ                  
A4B6: FE 67           CP      $67                 
A4B8: 33              INC     SP                  
A4B9: 89              ADC     A,C                 
A4BA: 59              LD      E,C                 
A4BB: 77              LD      (HL),A              
A4BC: 60              LD      H,B                 
A4BD: 49              LD      C,C                 
A4BE: F3              DI                          
A4BF: 23              INC     HL                  
A4C0: 04              INC     B                   
A4C1: 4F              LD      C,A                 
A4C2: 9B              SBC     E                   
A4C3: 96              SUB     (HL)                
A4C4: 66              LD      H,(HL)              
A4C5: 62              LD      H,D                 
A4C6: 2E 62           LD      L,$62               
A4C8: 19              ADD     HL,DE               
A4C9: 60              LD      H,B                 
A4CA: 22 1C 01        LD      ($011C),HL          
A4CD: 1D              DEC     E                   
A4CE: 4B              LD      C,E                 
A4CF: 08              EX      AF,AF'              
A4D0: 81              ADD     A,C                 
A4D1: 1C              INC     E                   
A4D2: 0E 81           LD      C,$81               
A4D4: 19              ADD     HL,DE               
A4D5: 0D              DEC     C                   
A4D6: 1F              RRA                         
A4D7: 03              INC     BC                  
A4D8: 01 8D 1F        LD      BC,$1F8D            
A4DB: 1A              LD      A,(DE)              
A4DC: 91              SUB     C                   
A4DD: 1E 55           LD      E,$55               
A4DF: C2 8E BE        JP      NZ,$BE8E            
A4E2: 0A              LD      A,(BC)              
A4E3: 8A              ADC     A,D                 
A4E4: 2F              CPL                         
A4E5: 62              LD      H,D                 
A4E6: A3              AND     E                   
A4E7: 00              NOP                         
A4E8: 1B              DEC     DE                  
A4E9: B7              OR      A                   
A4EA: D6 B5           SUB     $B5                 
A4EC: DB 72           IN      A,($72)             
A4EE: F9              LD      SP,HL               
A4EF: A6              AND     (HL)                
A4F0: 5F              LD      E,A                 
A4F1: B9              CP      C                   
A4F2: 09              ADD     HL,BC               
A4F3: 56              LD      D,(HL)              
A4F4: 1B              DEC     DE                  
A4F5: B5              OR      L                   
A4F6: 0D              DEC     C                   
A4F7: 80              ADD     A,B                 
A4F8: F5              PUSH    AF                  
A4F9: 14              INC     D                   
A4FA: 0E 08           LD      C,$08               
A4FC: 0A              LD      A,(BC)              
A4FD: 03              INC     BC                  
A4FE: 0A              LD      A,(BC)              
A4FF: 04              INC     B                   
A500: 0A              LD      A,(BC)              
A501: 01 0A 02        LD      BC,$020A            
A504: 01 01 1F        LD      BC,$1F01            
A507: 80              ADD     A,B                 
A508: E2 5F BE        JP      PO,$BE5F            
A50B: EC 16 E2        CALL    PE,$E216            
A50E: A0              AND     B                   
A50F: E6 5F           AND     $5F                 
A511: A3              AND     E                   
A512: A0              AND     B                   
A513: 81              ADD     A,C                 
A514: 8D              ADC     A,L                 
A515: CB 87           RES     0,A                 
A517: C7              RST     0X00                
A518: DE 03           SBC     $03                 
A51A: 15              DEC     D                   
A51B: 65              LD      H,L                 
A51C: B1              OR      C                   
A51D: 13              INC     DE                  
A51E: BF              CP      A                   
A51F: D0              RET     NC                  
A520: 15              DEC     D                   
A521: 82              ADD     A,D                 
A522: 17              RLA                         
A523: 47              LD      B,A                 
A524: 5E              LD      E,(HL)              
A525: 35              DEC     (HL)                
A526: DD ; ????
A527: 90              SUB     B                   
A528: 14              INC     D                   
A529: 15              DEC     D                   
A52A: 58              LD      E,B                 
A52B: 55              LD      D,L                 
A52C: 4A              LD      C,D                 
A52D: FC ED 55        CALL    M,$55ED             
A530: 77              LD      (HL),A              
A531: 30 60           JR      NC,$A593            ; {}
A533: 7B              LD      A,E                 
A534: 14              INC     D                   
A535: 0C              INC     C                   
A536: BA              CP      D                   
A537: 91              SUB     C                   
A538: 48              LD      C,B                 
A539: 56              LD      D,(HL)              
A53A: 5E              LD      E,(HL)              
A53B: 90              SUB     B                   
A53C: 73              LD      (HL),E              
A53D: D1              POP     DE                  
A53E: 6A              LD      L,D                 
A53F: 73              LD      (HL),E              
A540: C6 B5           ADD     $B5                 
A542: D0              RET     NC                  
A543: AB              XOR     E                   
A544: BB              CP      E                   
A545: 3F              CCF                         
A546: B9              CP      C                   
A547: 4D              LD      C,L                 
A548: 5E              LD      E,(HL)              
A549: 8E              ADC     A,(HL)              
A54A: 7A              LD      A,D                 
A54B: B8              CP      B                   
A54C: 16 E4           LD      D,$E4               
A54E: 14              INC     D                   
A54F: 96              SUB     (HL)                
A550: 5F              LD      E,A                 
A551: 2F              CPL                         
A552: C6 CB           ADD     $CB                 
A554: 06 5A           LD      B,$5A               
A556: 17              RLA                         
A557: F3              DI                          
A558: A0              AND     B                   
A559: 8F              ADC     A,A                 
A55A: 73              LD      (HL),E              
A55B: FA 17 83        JP      M,$8317             ; {}
A55E: 61              LD      H,C                 
A55F: 55              LD      D,L                 
A560: 77              LD      (HL),A              
A561: 30 60           JR      NC,$A5C3            ; {}
A563: A3              AND     E                   
A564: 15              DEC     D                   
A565: DB 95           IN      A,($95)             
A567: 43              LD      B,E                 
A568: 79              LD      A,C                 
A569: C7              RST     0X00                
A56A: DE 94           SBC     $94                 
A56C: 14              INC     D                   
A56D: 46              LD      B,(HL)              
A56E: 5E              LD      E,(HL)              
A56F: 64              LD      H,H                 
A570: C5              PUSH    BC                  
A571: 30 15           JR      NC,$A588            ; {}
A573: 29              ADD     HL,HL               
A574: A1              AND     C                   
A575: 16 71           LD      D,$71               
A577: CA 9C 86        JP      Z,$869C             ; {}
A57A: 5F              LD      E,A                 
A57B: 82              ADD     A,D                 
A57C: 17              RLA                         
A57D: 73              LD      (HL),E              
A57E: 49              LD      C,C                 
A57F: 1B              DEC     DE                  
A580: D0              RET     NC                  
A581: 0E EE           LD      C,$EE               
A583: 3D              DEC     A                   
A584: A0              AND     B                   
A585: C7              RST     0X00                
A586: 16 08           LD      D,$08               
A588: BC              CP      H                   
A589: A3              AND     E                   
A58A: A0              AND     B                   
A58B: 5F              LD      E,A                 
A58C: BE              CP      (HL)                
A58D: 63              LD      H,E                 
A58E: 16 0F           LD      D,$0F               
A590: 6E              LD      L,(HL)              
A591: 85              ADD     A,L                 
A592: BE              CP      (HL)                
A593: A0              AND     B                   
A594: 13              INC     DE                  
A595: E3              EX      (SP),HL             
A596: 9F              SBC     A                   
A597: 13              INC     DE                  
A598: 8D              ADC     A,L                 
A599: 5B              LD      E,E                 
A59A: F4 1B A1        CALL    P,$A11B             ; {}
A59D: 47              LD      B,A                 
A59E: 55              LD      D,L                 
A59F: B3              OR      E                   
A5A0: 8B              ADC     A,E                 
A5A1: 5F              LD      E,A                 
A5A2: B9              CP      C                   
A5A3: 33              INC     SP                  
A5A4: 98              SBC     B                   
A5A5: 5F              LD      E,A                 
A5A6: BE              CP      (HL)                
A5A7: 2F              CPL                         
A5A8: 17              RLA                         
A5A9: F3              DI                          
A5AA: B9              CP      C                   
A5AB: C3 9E C7        JP      $C79E               
A5AE: DE 8E           SBC     $8E                 
A5B0: AF              XOR     A                   
A5B1: 4F              LD      C,A                 
A5B2: 79              LD      A,C                 
A5B3: D0              RET     NC                  
A5B4: 15              DEC     D                   
A5B5: 82              ADD     A,D                 
A5B6: 17              RLA                         
A5B7: 4B              LD      C,E                 
A5B8: 7B              LD      A,E                 
A5B9: F5              PUSH    AF                  
A5BA: 59              LD      E,C                 
A5BB: 3E 62           LD      A,$62               
A5BD: D0              RET     NC                  
A5BE: 06 8E           LD      B,$8E               
A5C0: A1              AND     C                   
A5C1: 71              LD      (HL),C              
A5C2: 16 5B           LD      D,$5B               
A5C4: CA 49 48        JP      Z,$4849             
A5C7: AB              XOR     E                   
A5C8: 98              SBC     B                   
A5C9: 98              SBC     B                   
A5CA: 45              LD      B,L                 
A5CB: AF              XOR     A                   
A5CC: A0              AND     B                   
A5CD: BB              CP      E                   
A5CE: 15              DEC     D                   
A5CF: 29              ADD     HL,HL               
A5D0: B8              CP      B                   
A5D1: F3              DI                          
A5D2: A0              AND     B                   
A5D3: C7              RST     0X00                
A5D4: DE E3           SBC     $E3                 
A5D6: 06 DB           LD      B,$DB               
A5D8: 72              LD      (HL),D              
A5D9: 77              LD      (HL),A              
A5DA: 5B              LD      E,E                 
A5DB: 05              DEC     B                   
A5DC: B9              CP      C                   
A5DD: 15              DEC     D                   
A5DE: BC              CP      H                   
A5DF: 2F              CPL                         
A5E0: 60              LD      H,B                 
A5E1: CF              RST     0X08                
A5E2: 17              RLA                         
A5E3: 7B              LD      A,E                 
A5E4: B4              OR      H                   
A5E5: 73              LD      (HL),E              
A5E6: 68              LD      L,B                 
A5E7: 8E              ADC     A,(HL)              
A5E8: 61              LD      H,C                 
A5E9: 1F              RRA                         
A5EA: 8F              ADC     A,A                 
A5EB: 17              RLA                         
A5EC: 8D              ADC     A,L                 
A5ED: 01 02 07        LD      BC,$0702            
A5F0: F9              LD      SP,HL               
A5F1: A6              AND     (HL)                
A5F2: 5F              LD      E,A                 
A5F3: B9              CP      C                   
A5F4: 09              ADD     HL,BC               
A5F5: 56              LD      D,(HL)              
A5F6: 52              LD      D,D                 
A5F7: 00              NOP                         
A5F8: 03              INC     BC                  
A5F9: 00              NOP                         
A5FA: 00              NOP                         
A5FB: 80              ADD     A,B                 
A5FC: 6F              LD      L,A                 
A5FD: 0A              LD      A,(BC)              
A5FE: 9B              SBC     E                   
A5FF: 08              EX      AF,AF'              
A600: 80              ADD     A,B                 
A601: 02              LD      (BC),A              
A602: 05              DEC     B                   
A603: 85              ADD     A,L                 
A604: 91              SUB     C                   
A605: 90              SUB     B                   
A606: 73              LD      (HL),E              
A607: 45              LD      B,L                 
A608: 4A              LD      C,D                 
A609: 80              ADD     A,B                 
A60A: 87              ADD     A,A                 
A60B: 3A 00 80        LD      A,($8000)           ; {}
A60E: 01 01 60        LD      BC,$6001            
A611: 07              RLCA                        
A612: 75              LD      (HL),L              
A613: 0D              DEC     C                   
A614: 73              LD      (HL),E              
A615: 0A              LD      A,(BC)              
A616: 12              LD      (DE),A              
A617: 0E 6F           LD      C,$6F               
A619: 0D              DEC     C                   
A61A: 6B              LD      L,E                 
A61B: 04              INC     B                   
A61C: 42              LD      B,D                 
A61D: C3 54 AF        JP      $AF54               ; {}
A620: 54              LD      D,H                 
A621: 51              LD      D,C                 
A622: 18 4A           JR      $A66E               ; {}
A624: C2 94 5F        JP      NZ,$5F94            ; {}
A627: 7B              LD      A,E                 
A628: 14              INC     D                   
A629: 87              ADD     A,A                 
A62A: 8D              ADC     A,L                 
A62B: 14              INC     D                   
A62C: 58              LD      E,B                 
A62D: 64              LD      H,H                 
A62E: C5              PUSH    BC                  
A62F: DB 8B           IN      A,($8B)             
A631: 4B              LD      C,E                 
A632: 49              LD      C,C                 
A633: 5F              LD      E,A                 
A634: BE              CP      (HL)                
A635: 5A              LD      E,D                 
A636: 17              RLA                         
A637: D3 7A           OUT     ($7A),A             
A639: 74              LD      (HL),H              
A63A: 8E              ADC     A,(HL)              
A63B: 1F              RRA                         
A63C: 54              LD      D,H                 
A63D: C8              RET     Z                   
A63E: B5              OR      L                   
A63F: A3              AND     E                   
A640: A0              AND     B                   
A641: 4F              LD      C,A                 
A642: 45              LD      B,L                 
A643: E7              RST     0X20                
A644: 9F              SBC     A                   
A645: D7              RST     0X10                
A646: 9A              SBC     D                   
A647: 82              ADD     A,D                 
A648: 17              RLA                         
A649: 83              ADD     A,E                 
A64A: 61              LD      H,C                 
A64B: 58              LD      E,B                 
A64C: 45              LD      B,L                 
A64D: 45              LD      B,L                 
A64E: 9F              SBC     A                   
A64F: 55              LD      D,L                 
A650: 5E              LD      E,(HL)              
A651: 55              LD      D,L                 
A652: 4A              LD      C,D                 
A653: FC ED 6F        CALL    M,$6FED             ; {}
A656: CC 44 5E        CALL    Z,$5E44             ; {}
A659: 03              INC     BC                  
A65A: A0              AND     B                   
A65B: 56              LD      D,(HL)              
A65C: B8              CP      B                   
A65D: 2C              INC     L                   
A65E: E1              POP     HL                  
A65F: 03              INC     BC                  
A660: 01 80 04        LD      BC,$0480            
A663: 22 C7 DE        LD      ($DEC7),HL          
A666: B0              OR      B                   
A667: 17              RLA                         
A668: F4 59 FB        CALL    P,$FB59             
A66B: B9              CP      C                   
A66C: 33              INC     SP                  
A66D: 98              SBC     B                   
A66E: 63              LD      H,E                 
A66F: BE              CP      (HL)                
A670: D6 B5           SUB     $B5                 
A672: CF              RST     0X08                
A673: 9C              SBC     H                   
A674: 90              SUB     B                   
A675: 5F              LD      E,A                 
A676: FC ED 91        CALL    M,$91ED             ; {}
A679: 61              LD      H,C                 
A67A: 8F              ADC     A,A                 
A67B: 7A              LD      A,D                 
A67C: C3 B5 5B        JP      $5BB5               
A67F: B1              OR      C                   
A680: 4F              LD      C,A                 
A681: 59              LD      E,C                 
A682: 77              LD      (HL),A              
A683: 47              LD      B,A                 
A684: 9C              SBC     H                   
A685: 5D              LD      E,L                 
A686: 14              INC     D                   
A687: 0C              INC     C                   
A688: 02              LD      (BC),A              
A689: 08              EX      AF,AF'              
A68A: 23              INC     HL                  
A68B: D1              POP     DE                  
A68C: DB BD           IN      A,($BD)             
A68E: F6 4F           OR      $4F                 
A690: 80              ADD     A,B                 
A691: BF              CP      A                   
A692: 53              LD      D,E                 
A693: 0C              INC     C                   
A694: 89              ADC     A,C                 
A695: 07              RLCA                        
A696: 80              ADD     A,B                 
A697: 07              RLCA                        
A698: 01 C5 02        LD      BC,$02C5            
A69B: 04              INC     B                   
A69C: 1B              DEC     DE                  
A69D: 54              LD      D,H                 
A69E: 23              INC     HL                  
A69F: 7B              LD      A,E                 
A6A0: 00              NOP                         
A6A1: 09              ADD     HL,BC               
A6A2: 00              NOP                         
A6A3: 00              NOP                         
A6A4: A0              AND     B                   
A6A5: 02              LD      (BC),A              
A6A6: 04              INC     B                   
A6A7: 7B              LD      A,E                 
A6A8: A6              AND     (HL)                
A6A9: 40              LD      B,B                 
A6AA: B9              CP      C                   
A6AB: 00              NOP                         
A6AC: 03              INC     BC                  
A6AD: 00              NOP                         
A6AE: 00              NOP                         
A6AF: 00              NOP                         
A6B0: 10 09           DJNZ    $A6BB               ; {}
A6B2: 83              ADD     A,E                 
A6B3: 29              ADD     HL,HL               
A6B4: 88              ADC     A,B                 
A6B5: 02              LD      (BC),A              
A6B6: 04              INC     B                   
A6B7: 60              LD      H,B                 
A6B8: 62              LD      H,D                 
A6B9: 33              INC     SP                  
A6BA: 61              LD      H,C                 
A6BB: 71              LD      (HL),C              
A6BC: 32 31 00        LD      ($0031),A           
A6BF: 90              SUB     B                   
A6C0: 07              RLCA                        
A6C1: 27              DAA                         
A6C2: 0D              DEC     C                   
A6C3: 25              DEC     H                   
A6C4: 0E 05           LD      C,$05               
A6C6: C4 0A 09        CALL    NZ,$090A            
A6C9: 0A              LD      A,(BC)              
A6CA: 57              LD      D,A                 
A6CB: 04              INC     B                   
A6CC: 0E E9           LD      C,$E9               
A6CE: C5              PUSH    BC                  
A6CF: 84              ADD     A,H                 
A6D0: 96              SUB     (HL)                
A6D1: D0              RET     NC                  
A6D2: 60              LD      H,B                 
A6D3: C6 6A           ADD     $6A                 
A6D5: 66              LD      H,(HL)              
A6D6: 7B              LD      A,E                 
A6D7: 2C              INC     L                   
A6D8: C6 16           ADD     $16                 
A6DA: 60              LD      H,B                 
A6DB: A8              XOR     B                   
A6DC: 04              INC     B                   
A6DD: 08              EX      AF,AF'              
A6DE: 83              ADD     A,E                 
A6DF: 67              LD      H,A                 
A6E0: 4B              LD      C,E                 
A6E1: 62              LD      H,D                 
A6E2: F3              DI                          
A6E3: 49              LD      C,C                 
A6E4: DB E0           IN      A,($E0)             
A6E6: 17              RLA                         
A6E7: 94              SUB     H                   
A6E8: 00              NOP                         
A6E9: 02              LD      (BC),A              
A6EA: 04              INC     B                   
A6EB: 41              LD      B,C                 
A6EC: 6E              LD      L,(HL)              
A6ED: 64              LD      H,H                 
A6EE: 8E              ADC     A,(HL)              
A6EF: 10 2C           DJNZ    $A71D               ; {}
A6F1: 87              ADD     A,A                 
A6F2: 69              LD      L,C                 
A6F3: 88              ADC     A,B                 
A6F4: 07              RLCA                        
A6F5: 21 0E 1F        LD      HL,$1F0E            
A6F8: 0D              DEC     C                   
A6F9: 0C              INC     C                   
A6FA: 0E 06           LD      C,$06               
A6FC: 0A              LD      A,(BC)              
A6FD: 3A 0A 42        LD      A,($420A)           
A700: 0A              LD      A,(BC)              
A701: 41              LD      B,C                 
A702: 14              INC     D                   
A703: 09              ADD     HL,BC               
A704: 97              SUB     A                   
A705: BA              CP      D                   
A706: 0D              DEC     C                   
A707: 0F              RRCA                        
A708: 0A              LD      A,(BC)              
A709: 11 1A 2E        LD      DE,$2E1A            
A70C: 40              LD      B,B                 
A70D: A8              XOR     B                   
A70E: 04              INC     B                   
A70F: 07              RLCA                        
A710: 4B              LD      C,E                 
A711: 7B              LD      A,E                 
A712: 44              LD      B,H                 
A713: 87              ADD     A,A                 
A714: B0              OR      B                   
A715: 85              ADD     A,L                 
A716: 2E 02           LD      L,$02               
A718: 04              INC     B                   
A719: 60              LD      H,B                 
A71A: 62              LD      H,D                 
A71B: 33              INC     SP                  
A71C: 61              LD      H,C                 
A71D: 10 2C           DJNZ    $A74B               ; {}
A71F: 89              ADC     A,C                 
A720: 69              LD      L,C                 
A721: 88              ADC     A,B                 
A722: 07              RLCA                        
A723: 21 0E 1F        LD      HL,$1F0E            
A726: 0D              DEC     C                   
A727: 0C              INC     C                   
A728: 0E 06           LD      C,$06               
A72A: 0A              LD      A,(BC)              
A72B: 3A 0A 42        LD      A,($420A)           
A72E: 0A              LD      A,(BC)              
A72F: 41              LD      B,C                 
A730: 14              INC     D                   
A731: 09              ADD     HL,BC               
A732: 97              SUB     A                   
A733: BA              CP      D                   
A734: 0D              DEC     C                   
A735: 0F              RRCA                        
A736: 0A              LD      A,(BC)              
A737: 11 1A 2E        LD      DE,$2E1A            
A73A: 40              LD      B,B                 
A73B: A8              XOR     B                   
A73C: 04              INC     B                   
A73D: 07              RLCA                        
A73E: 4B              LD      C,E                 
A73F: 7B              LD      A,E                 
A740: 44              LD      B,H                 
A741: 87              ADD     A,A                 
A742: B0              OR      B                   
A743: 85              ADD     A,L                 
A744: 2E 02           LD      L,$02               
A746: 04              INC     B                   
A747: 60              LD      H,B                 
A748: 62              LD      H,D                 
A749: 33              INC     SP                  
A74A: 61              LD      H,C                 
A74B: 16 77           LD      D,$77               
A74D: 86              ADD     A,(HL)              
A74E: 09              ADD     HL,BC               
A74F: A4              AND     H                   
A750: 03              INC     BC                  
A751: 15              DEC     D                   
A752: 04              INC     B                   
A753: 13              INC     DE                  
A754: 5F              LD      E,A                 
A755: BE              CP      (HL)                
A756: 5B              LD      E,E                 
A757: B1              OR      C                   
A758: 4B              LD      C,E                 
A759: 7B              LD      A,E                 
A75A: 55              LD      D,L                 
A75B: 45              LD      B,L                 
A75C: 8E              ADC     A,(HL)              
A75D: 91              SUB     C                   
A75E: 17              RLA                         
A75F: 8A              ADC     A,D                 
A760: 44              LD      B,H                 
A761: 87              ADD     A,A                 
A762: CA 83 2F        JP      Z,$2F83             
A765: 62              LD      H,D                 
A766: 2E 07           LD      L,$07               
A768: 51              LD      D,C                 
A769: 0D              DEC     C                   
A76A: 4F              LD      C,A                 
A76B: 0A              LD      A,(BC)              
A76C: 08              EX      AF,AF'              
A76D: 04              INC     B                   
A76E: 0F              RRCA                        
A76F: 04              INC     B                   
A770: 1D              DEC     E                   
A771: AE              XOR     (HL)                
A772: 85              ADD     A,L                 
A773: EB              EX      DE,HL               
A774: B8              CP      B                   
A775: 18 BC           JR      $A733               ; {}
A777: 67              LD      H,A                 
A778: B1              OR      C                   
A779: 05              DEC     B                   
A77A: 4F              LD      C,A                 
A77B: 4E              LD      C,(HL)              
A77C: BD              CP      L                   
A77D: 22 0E 3A        LD      ($3A0E),HL          
A780: 0D              DEC     C                   
A781: 36 03           LD      (HL),$03            
A783: 01 80 04        LD      BC,$0480            
A786: 31 FA 17        LD      SP,$17FA            
A789: DA 78 67        JP      C,$6778             ; {}
A78C: 16 9D           LD      D,$9D               
A78E: 48              LD      C,B                 
A78F: FC ED 43        CALL    M,$43ED             
A792: 79              LD      A,C                 
A793: 07              RLCA                        
A794: 68              LD      L,B                 
A795: 56              LD      D,(HL)              
A796: 98              SBC     B                   
A797: 0C              INC     C                   
A798: 15              DEC     D                   
A799: 53              LD      D,E                 
A79A: A0              AND     B                   
A79B: 83              ADD     A,E                 
A79C: 7A              LD      A,D                 
A79D: A3              AND     E                   
A79E: 48              LD      C,B                 
A79F: 63              LD      H,E                 
A7A0: 16 3C           LD      D,$3C               
A7A2: 7A              LD      A,D                 
A7A3: B7              OR      A                   
A7A4: A1              AND     C                   
A7A5: 2F              CPL                         
A7A6: 17              RLA                         
A7A7: 74              LD      (HL),H              
A7A8: C0              RET     NZ                  
A7A9: 92              SUB     D                   
A7AA: 96              SUB     (HL)                
A7AB: E6 A0           AND     $A0                 
A7AD: 77              LD      (HL),A              
A7AE: 47              LD      B,A                 
A7AF: 87              ADD     A,A                 
A7B0: 15              DEC     D                   
A7B1: 3F              CCF                         
A7B2: 49              LD      C,C                 
A7B3: BF              CP      A                   
A7B4: 9A              SBC     D                   
A7B5: 17              RLA                         
A7B6: 60              LD      H,B                 
A7B7: 22 14 0C        LD      ($0C14),HL          
A7BA: 02              LD      (BC),A              
A7BB: 08              EX      AF,AF'              
A7BC: E3              EX      (SP),HL             
A7BD: B8              CP      B                   
A7BE: F3              DI                          
A7BF: 8C              ADC     A,H                 
A7C0: 21 C5 4B        LD      HL,$4BC5            
A7C3: B2              OR      D                   
A7C4: 12              LD      (DE),A              
A7C5: 81              ADD     A,C                 
A7C6: 87              ADD     A,A                 
A7C7: 8B              ADC     A,E                 
A7C8: 09              ADD     HL,BC               
A7C9: 80              ADD     A,B                 
A7CA: 07              RLCA                        
A7CB: 81              ADD     A,C                 
A7CC: 7A              LD      A,D                 
A7CD: 0E 81           LD      C,$81               
A7CF: 77              LD      (HL),A              
A7D0: 0D              DEC     C                   
A7D1: 73              LD      (HL),E              
A7D2: 0A              LD      A,(BC)              
A7D3: 50              LD      D,B                 
A7D4: 03              INC     BC                  
A7D5: 00              NOP                         
A7D6: 71              LD      (HL),C              
A7D7: 04              INC     B                   
A7D8: 6C              LD      L,H                 
A7D9: C2 1D 4B        JP      NZ,$4B1D            
A7DC: 5E              LD      E,(HL)              
A7DD: 0B              DEC     BC                  
A7DE: 9B              SBC     E                   
A7DF: 51              LD      D,C                 
A7E0: B8              CP      B                   
A7E1: 91              SUB     C                   
A7E2: 96              SUB     (HL)                
A7E3: 96              SUB     (HL)                
A7E4: 64              LD      H,H                 
A7E5: DB 72           IN      A,($72)             
A7E7: FB              EI                          
A7E8: A5              AND     L                   
A7E9: 76              HALT                        
A7EA: 98              SBC     B                   
A7EB: 55              LD      D,L                 
A7EC: 17              RLA                         
A7ED: 0F              RRCA                        
A7EE: B2              OR      D                   
A7EF: 00              NOP                         
A7F0: 81              ADD     A,C                 
A7F1: D5              PUSH    DE                  
A7F2: 15              DEC     D                   
A7F3: 81              ADD     A,C                 
A7F4: 15              DEC     D                   
A7F5: 91              SUB     C                   
A7F6: 7A              LD      A,D                 
A7F7: F7              RST     0X30                
A7F8: 17              RLA                         
A7F9: 17              RLA                         
A7FA: 8D              ADC     A,L                 
A7FB: D6 15           SUB     $15                 
A7FD: 9B              SBC     E                   
A7FE: 15              DEC     D                   
A7FF: C4 B5 30        CALL    NZ,$30B5            
A802: 60              LD      H,B                 
A803: FF              RST     0X38                
A804: 14              INC     D                   
A805: F4 BD D0        CALL    P,$D0BD             
A808: 92              SUB     D                   
A809: F3              DI                          
A80A: 5F              LD      E,A                 
A80B: 5B              LD      E,E                 
A80C: BE              CP      (HL)                
A80D: 15              DEC     D                   
A80E: BC              CP      H                   
A80F: B3              OR      E                   
A810: 55              LD      D,L                 
A811: F9              LD      SP,HL               
A812: 92              SUB     D                   
A813: 8B              ADC     A,E                 
A814: 96              SUB     (HL)                
A815: CF              RST     0X08                
A816: B5              OR      L                   
A817: DA C3 71        JP      C,$71C3             ; {}
A81A: 16 5B           LD      D,$5B               
A81C: B1              OR      C                   
A81D: 2B              DEC     HL                  
A81E: BA              CP      D                   
A81F: 44              LD      B,H                 
A820: BD              CP      L                   
A821: DB 8B           IN      A,($8B)             
A823: 6B              LD      L,E                 
A824: BF              CP      A                   
A825: 34              INC     (HL)                
A826: A1              AND     C                   
A827: 8F              ADC     A,A                 
A828: 16 0D           LD      D,$0D               
A82A: 60              LD      H,B                 
A82B: AF              XOR     A                   
A82C: 14              INC     D                   
A82D: 17              RLA                         
A82E: 53              LD      D,E                 
A82F: BE              CP      (HL)                
A830: B7              OR      A                   
A831: AA              XOR     D                   
A832: 17              RLA                         
A833: 07              RLCA                        
A834: EE 3E           XOR     $3E                 
A836: 49              LD      C,C                 
A837: 0B              DEC     BC                  
A838: 71              LD      (HL),C              
A839: D6 B5           SUB     $B5                 
A83B: 4E              LD      C,(HL)              
A83C: A0              AND     B                   
A83D: AA              XOR     D                   
A83E: 17              RLA                         
A83F: 15              DEC     D                   
A840: EE 8E           XOR     $8E                 
A842: 91              SUB     C                   
A843: 9C              SBC     H                   
A844: 8F              ADC     A,A                 
A845: 0D              DEC     C                   
A846: 80              ADD     A,B                 
A847: 9B              SBC     E                   
A848: 0A              LD      A,(BC)              
A849: 50              LD      D,B                 
A84A: 03              INC     BC                  
A84B: 01 80 0A        LD      BC,$0A80            
A84E: 50              LD      D,B                 
A84F: 04              INC     B                   
A850: 80              ADD     A,B                 
A851: 91              SUB     C                   
A852: 7A              LD      A,D                 
A853: 1B              DEC     DE                  
A854: B2              OR      D                   
A855: 53              LD      D,E                 
A856: 08              EX      AF,AF'              
A857: BC              CP      H                   
A858: A3              AND     E                   
A859: A0              AND     B                   
A85A: 5F              LD      E,A                 
A85B: BE              CP      (HL)                
A85C: E4 14 5A        CALL    PO,$5A14            
A85F: 49              LD      C,C                 
A860: B8              CP      B                   
A861: 16 82           LD      D,$82               
A863: 17              RLA                         
A864: 55              LD      D,L                 
A865: 5E              LD      E,(HL)              
A866: 47              LD      B,A                 
A867: 55              LD      D,L                 
A868: 15              DEC     D                   
A869: BC              CP      H                   
A86A: 92              SUB     D                   
A86B: 73              LD      (HL),E              
A86C: 16 EE           LD      D,$EE               
A86E: DB 72           IN      A,($72)             
A870: A0              AND     B                   
A871: 7A              LD      A,D                 
A872: 5B              LD      E,E                 
A873: 49              LD      C,C                 
A874: 03              INC     BC                  
A875: A0              AND     B                   
A876: C3 9E 5F        JP      $5F9E               ; {}
A879: BE              CP      (HL)                
A87A: E6 16           AND     $16                 
A87C: 8F              ADC     A,A                 
A87D: 48              LD      C,B                 
A87E: 07              RLCA                        
A87F: BC              CP      H                   
A880: 3E 49           LD      A,$49               
A882: 0B              DEC     BC                  
A883: 71              LD      (HL),C              
A884: C9              RET                         
A885: B5              OR      L                   
A886: 50              LD      D,B                 
A887: 9F              SBC     A                   
A888: D9              EXX                         
A889: 6A              LD      L,D                 
A88A: 46              LD      B,(HL)              
A88B: 61              LD      H,C                 
A88C: 56              LD      D,(HL)              
A88D: F4 DB 72        CALL    P,$72DB             ; {}
A890: C6 93           ADD     $93                 
A892: F4 72 5A        CALL    P,$5A72             
A895: 17              RLA                         
A896: D3 7A           OUT     ($7A),A             
A898: 4B              LD      C,E                 
A899: 7B              LD      A,E                 
A89A: 09              ADD     HL,BC               
A89B: 9A              SBC     D                   
A89C: D0              RET     NC                  
A89D: 15              DEC     D                   
A89E: C4 16 16        CALL    NZ,$1616            
A8A1: 4E              LD      C,(HL)              
A8A2: 03              INC     BC                  
A8A3: EE 33           XOR     $33                 
A8A5: 98              SBC     B                   
A8A6: 4E              LD      C,(HL)              
A8A7: D1              POP     DE                  
A8A8: 15              DEC     D                   
A8A9: 8A              ADC     A,D                 
A8AA: 40              LD      B,B                 
A8AB: A0              AND     B                   
A8AC: AF              XOR     A                   
A8AD: 14              INC     D                   
A8AE: 50              LD      D,B                 
A8AF: 6D              LD      L,L                 
A8B0: 82              ADD     A,D                 
A8B1: 17              RLA                         
A8B2: 52              LD      D,D                 
A8B3: 5E              LD      E,(HL)              
A8B4: 31 C6 51        LD      SP,$51C6            
A8B7: 5E              LD      E,(HL)              
A8B8: 8E              ADC     A,(HL)              
A8B9: 64              LD      H,H                 
A8BA: 4F              LD      C,A                 
A8BB: 79              LD      A,C                 
A8BC: 59              LD      E,C                 
A8BD: 15              DEC     D                   
A8BE: B5              OR      L                   
A8BF: B2              OR      D                   
A8C0: 54              LD      D,H                 
A8C1: F4 E9 61        CALL    P,$61E9             ; {}
A8C4: B3              OR      E                   
A8C5: B3              OR      E                   
A8C6: 6B              LD      L,E                 
A8C7: BF              CP      A                   
A8C8: C7              RST     0X00                
A8C9: DE 95           SBC     $95                 
A8CB: AF              XOR     A                   
A8CC: 09              ADD     HL,BC               
A8CD: A6              AND     (HL)                
A8CE: 0F              RRCA                        
A8CF: A0              AND     B                   
A8D0: F6 B0           OR      $B0                 
A8D2: A3              AND     E                   
A8D3: 46              LD      B,(HL)              
A8D4: 83              ADD     A,E                 
A8D5: 7A              LD      A,D                 
A8D6: 6C              LD      L,H                 
A8D7: BE              CP      (HL)                
A8D8: 1B              DEC     DE                  
A8D9: 60              LD      H,B                 
A8DA: 7F              LD      A,A                 
A8DB: 67              LD      H,A                 
A8DC: 30 60           JR      NC,$A93E            ; {}
A8DE: 69              LD      L,C                 
A8DF: B9              CP      C                   
A8E0: 2F              CPL                         
A8E1: C0              RET     NZ                  
A8E2: 22 0D 56        LD      ($560D),HL          
A8E5: 0A              LD      A,(BC)              
A8E6: 50              LD      D,B                 
A8E7: 04              INC     B                   
A8E8: 52              LD      D,D                 
A8E9: 5D              LD      E,L                 
A8EA: 1E 33           LD      E,$33               
A8EC: A7              AND     A                   
A8ED: BD              CP      L                   
A8EE: 55              LD      D,L                 
A8EF: 15              DEC     D                   
A8F0: 71              LD      (HL),C              
A8F1: F3              DI                          
A8F2: 55              LD      D,L                 
A8F3: 2A B8 10        LD      HL,($10B8)          
A8F6: EE A0           XOR     $A0                 
A8F8: CC E6 16        CALL    Z,$16E6             
A8FB: B3              OR      E                   
A8FC: 9A              SBC     D                   
A8FD: C2 B3 80        JP      NZ,$80B3            ; {}
A900: 15              DEC     D                   
A901: D9              EXX                         
A902: 6A              LD      L,D                 
A903: 17              RLA                         
A904: 8D              ADC     A,L                 
A905: 76              HALT                        
A906: 16 E3           LD      D,$E3               
A908: 74              LD      (HL),H              
A909: 2A B8 83        LD      HL,($83B8)          ; {}
A90C: 16 FE           LD      D,$FE               
A90E: B0              OR      B                   
A90F: 8E              ADC     A,(HL)              
A910: 16 FE           LD      D,$FE               
A912: 17              RLA                         
A913: 15              DEC     D                   
A914: 8A              ADC     A,D                 
A915: 95              SUB     L                   
A916: 96              SUB     (HL)                
A917: FE BF           CP      $BF                 
A919: EC 16 C8        CALL    PE,$C816            
A91C: 6A              LD      L,D                 
A91D: 40              LD      B,B                 
A91E: 16 5C           LD      D,$5C               
A920: 15              DEC     D                   
A921: 6F              LD      L,A                 
A922: 94              SUB     H                   
A923: 3A 17 B3        LD      A,($B317)           ; {}
A926: B3              OR      E                   
A927: 1B              DEC     DE                  
A928: BC              CP      H                   
A929: 95              SUB     L                   
A92A: AF              XOR     A                   
A92B: 08              EX      AF,AF'              
A92C: A6              AND     (HL)                
A92D: F6 B0           OR      $B0                 
A92F: 90              SUB     B                   
A930: 4B              LD      C,E                 
A931: 82              ADD     A,D                 
A932: 17              RLA                         
A933: 88              ADC     A,B                 
A934: AF              XOR     A                   
A935: 5D              LD      E,L                 
A936: 8D              ADC     A,L                 
A937: 4D              LD      C,L                 
A938: A7              AND     A                   
A939: 63              LD      H,E                 
A93A: F4 0D 0A        CALL    P,$0A0D             
A93D: 0A              LD      A,(BC)              
A93E: 0B              DEC     BC                  
A93F: A8              XOR     B                   
A940: 04              INC     B                   
A941: 05              DEC     B                   
A942: 4B              LD      C,E                 
A943: 7B              LD      A,E                 
A944: D0              RET     NC                  
A945: 9E              SBC     (HL)                
A946: 2E 02           LD      L,$02               
A948: 05              DEC     B                   
A949: 8F              ADC     A,A                 
A94A: 4E              LD      C,(HL)              
A94B: DF              RST     0X18                
A94C: B2              OR      D                   
A94D: 4D              LD      C,L                 
A94E: 66              LD      H,(HL)              
A94F: 08              EX      AF,AF'              
A950: 9D              SBC     L                   
A951: 05              DEC     B                   
A952: 80              ADD     A,B                 
A953: 02              LD      (BC),A              
A954: 03              INC     BC                  
A955: 23              INC     HL                  
A956: B8              CP      B                   
A957: 50              LD      D,B                 
A958: 25              DEC     H                   
A959: 08              EX      AF,AF'              
A95A: 01 00 80        LD      BC,$8000            
A95D: 02              LD      (BC),A              
A95E: 03              INC     BC                  
A95F: 0E D0           LD      C,$D0               
A961: 4C              LD      C,H                 
A962: 00              NOP                         
A963: 03              INC     BC                  
A964: 00              NOP                         
A965: 00              NOP                         
A966: 00              NOP                         
A967: 66              LD      H,(HL)              
A968: 08              EX      AF,AF'              
A969: 80              ADD     A,B                 
A96A: 07              RLCA                        
A96B: 80              ADD     A,B                 
A96C: 02              LD      (BC),A              
A96D: 03              INC     BC                  
A96E: 23              INC     HL                  
A96F: B8              CP      B                   
A970: 50              LD      D,B                 
A971: 00              NOP                         
A972: 81              ADD     A,C                 
A973: 3B              DEC     SP                  
A974: 00              NOP                         
A975: 00              NOP                         
A976: 80              ADD     A,B                 
A977: 08              EX      AF,AF'              
A978: 81              ADD     A,C                 
A979: 35              DEC     (HL)                
A97A: 0D              DEC     C                   
A97B: 81              ADD     A,C                 
A97C: 32 1C 01        LD      ($011C),A           
A97F: 1D              DEC     E                   
A980: 02              LD      (BC),A              
A981: 0B              DEC     BC                  
A982: 81              ADD     A,C                 
A983: 2B              DEC     HL                  
A984: 22 01 01        LD      ($0101),HL          
A987: 1A              LD      A,(DE)              
A988: 03              INC     BC                  
A989: 33              INC     SP                  
A98A: 1F              RRA                         
A98B: 31 C7 DE        LD      SP,$DEC7            
A98E: E1              POP     HL                  
A98F: 14              INC     D                   
A990: FB              EI                          
A991: 8C              ADC     A,H                 
A992: 17              RLA                         
A993: A7              AND     A                   
A994: FB              EI                          
A995: 17              RLA                         
A996: 53              LD      D,E                 
A997: BE              CP      (HL)                
A998: 22 63 B5        LD      ($B563),HL          ; {}
A99B: 49              LD      C,C                 
A99C: 91              SUB     C                   
A99D: BE              CP      (HL)                
A99E: 1B              DEC     DE                  
A99F: 9C              SBC     H                   
A9A0: 43              LD      B,E                 
A9A1: 79              LD      A,C                 
A9A2: C7              RST     0X00                
A9A3: DE 9B           SBC     $9B                 
A9A5: 15              DEC     D                   
A9A6: 5B              LD      E,E                 
A9A7: CA A3 48        JP      Z,$48A3             
A9AA: F3              DI                          
A9AB: 17              RLA                         
A9AC: F4 BD 04        CALL    P,$04BD             
A9AF: EE 8E           XOR     $8E                 
A9B1: 62              LD      H,D                 
A9B2: 23              INC     HL                  
A9B3: 62              LD      H,D                 
A9B4: F3              DI                          
A9B5: 5B              LD      E,E                 
A9B6: 4B              LD      C,E                 
A9B7: 99              SBC     C                   
A9B8: 73              LD      (HL),E              
A9B9: 7B              LD      A,E                 
A9BA: 09              ADD     HL,BC               
A9BB: 9A              SBC     D                   
A9BC: 21 08 01        LD      HL,$0108            
A9BF: 1A              LD      A,(DE)              
A9C0: 0A              LD      A,(BC)              
A9C1: 22 1F 20        LD      ($201F),HL          
A9C4: C7              RST     0X00                
A9C5: DE D3           SBC     $D3                 
A9C7: 14              INC     D                   
A9C8: 90              SUB     B                   
A9C9: 96              SUB     (HL)                
A9CA: F3              DI                          
A9CB: A0              AND     B                   
A9CC: A7              AND     A                   
A9CD: 85              ADD     A,L                 
A9CE: 09              ADD     HL,BC               
A9CF: A3              AND     E                   
A9D0: 50              LD      D,B                 
A9D1: 9F              SBC     A                   
A9D2: D9              EXX                         
A9D3: 6A              LD      L,D                 
A9D4: 82              ADD     A,D                 
A9D5: 7B              LD      A,E                 
A9D6: 36 A1           LD      (HL),$A1            
A9D8: 61              LD      H,C                 
A9D9: 17              RLA                         
A9DA: 1B              DEC     DE                  
A9DB: 92              SUB     D                   
A9DC: 6E              LD      L,(HL)              
A9DD: B1              OR      C                   
A9DE: 28 79           JR      Z,$AA59             ; {}
A9E0: 61              LD      H,C                 
A9E1: 17              RLA                         
A9E2: 01 A0 12        LD      BC,$12A0            
A9E5: 01 1A 14        LD      BC,$141A            
A9E8: 0C              INC     C                   
A9E9: 1F              RRA                         
A9EA: 0A              LD      A,(BC)              
A9EB: 45              LD      B,L                 
A9EC: 6E              LD      L,(HL)              
A9ED: 0B              DEC     BC                  
A9EE: 71              LD      (HL),C              
A9EF: DB 22           IN      A,($22)             
A9F1: 94              SUB     H                   
A9F2: BE              CP      (HL)                
A9F3: F1              POP     AF                  
A9F4: 5F              LD      E,A                 
A9F5: 1C              INC     E                   
A9F6: 01 1A 1E        LD      BC,$1E1A            
A9F9: 1C              INC     E                   
A9FA: 1F              RRA                         
A9FB: 1A              LD      A,(DE)              
A9FC: C7              RST     0X00                
A9FD: DE D3           SBC     $D3                 
A9FF: 14              INC     D                   
AA00: E6 96           AND     $96                 
AA02: 7B              LD      A,E                 
AA03: 17              RLA                         
AA04: 9B              SBC     E                   
AA05: 85              ADD     A,L                 
AA06: A5              AND     L                   
AA07: 94              SUB     H                   
AA08: 0F              RRCA                        
AA09: 71              LD      (HL),C              
AA0A: AF              XOR     A                   
AA0B: A0              AND     B                   
AA0C: B8              CP      B                   
AA0D: 16 82           LD      D,$82               
AA0F: 17              RLA                         
AA10: 4B              LD      C,E                 
AA11: 7B              LD      A,E                 
AA12: E3              EX      (SP),HL             
AA13: 72              LD      (HL),D              
AA14: AB              XOR     E                   
AA15: BB              CP      E                   
AA16: 26 01           LD      H,$01               
AA18: 1A              LD      A,(DE)              
AA19: 28 10           JR      Z,$AA2B             ; {}
AA1B: 1F              RRA                         
AA1C: 0E 0B           LD      C,$0B               
AA1E: 4F              LD      C,A                 
AA1F: 0B              DEC     BC                  
AA20: EE DB           XOR     $DB                 
AA22: 22 2B B9        LD      ($B92B),HL          
AA25: 63              LD      H,E                 
AA26: BE              CP      (HL)                
AA27: A6              AND     (HL)                
AA28: B3              OR      E                   
AA29: EB              EX      DE,HL               
AA2A: DA 30 01        JP      C,$0130             
AA2D: 1A              LD      A,(DE)              
AA2E: 32 1E 1F        LD      ($1F1E),A           
AA31: 1C              INC     E                   
AA32: 4A              LD      C,D                 
AA33: 77              LD      (HL),A              
AA34: 5F              LD      E,A                 
AA35: A0              AND     B                   
AA36: 51              LD      D,C                 
AA37: 18 44           JR      $AA7D               ; {}
AA39: C2 07 B3        JP      NZ,$B307            ; {}
AA3C: 2E 6D           LD      L,$6D               
AA3E: 49              LD      C,C                 
AA3F: 16 0B           LD      D,$0B               
AA41: C0              RET     NZ                  
AA42: C3 9E 01        JP      $019E               
AA45: 68              LD      L,B                 
AA46: 03              INC     BC                  
AA47: 58              LD      E,B                 
AA48: 33              INC     SP                  
AA49: 98              SBC     B                   
AA4A: 16 D0           LD      D,$D0               
AA4C: 21 62 3A        LD      HL,$3A62            
AA4F: 01 1A 3C        LD      BC,$3C1A            
AA52: 34              INC     (HL)                
AA53: 1F              RRA                         
AA54: 32 C7 DE        LD      ($DEC7),A           
AA57: D3 14           OUT     ($14),A             
AA59: 94              SUB     H                   
AA5A: 96              SUB     (HL)                
AA5B: 8E              ADC     A,(HL)              
AA5C: 5F              LD      E,A                 
AA5D: FB              EI                          
AA5E: 8E              ADC     A,(HL)              
AA5F: 67              LD      H,A                 
AA60: 66              LD      H,(HL)              
AA61: 16 8A           LD      D,$8A               
AA63: DB 72           IN      A,($72)             
AA65: E3              EX      (SP),HL             
AA66: 72              LD      (HL),D              
AA67: 11 BC 96        LD      DE,$96BC            
AA6A: 64              LD      H,H                 
AA6B: DB 72           IN      A,($72)             
AA6D: 30 BA           JR      NC,$AA29            ; {}
AA6F: BF              CP      A                   
AA70: 14              INC     D                   
AA71: D3 B2           OUT     ($B2),A             
AA73: AB              XOR     E                   
AA74: 98              SBC     B                   
AA75: 89              ADC     A,C                 
AA76: 5B              LD      E,E                 
AA77: 91              SUB     C                   
AA78: 96              SUB     (HL)                
AA79: 9B              SBC     E                   
AA7A: 96              SUB     (HL)                
AA7B: 1B              DEC     DE                  
AA7C: A1              AND     C                   
AA7D: 83              ADD     A,E                 
AA7E: 7A              LD      A,D                 
AA7F: 63              LD      H,E                 
AA80: BE              CP      (HL)                
AA81: C6 B5           ADD     $B5                 
AA83: 57              LD      D,A                 
AA84: 62              LD      H,D                 
AA85: B1              OR      C                   
AA86: B3              OR      E                   
AA87: 41              LD      B,C                 
AA88: 01 1A 43        LD      BC,$431A            
AA8B: 20 1F           JR      NZ,$AAAC            ; {}
AA8D: 1E 0B           LD      E,$0B               
AA8F: 4F              LD      C,A                 
AA90: 16 EE           LD      D,$EE               
AA92: 95              SUB     L                   
AA93: 73              LD      (HL),E              
AA94: FF              RST     0X38                
AA95: 14              INC     D                   
AA96: B4              OR      H                   
AA97: B7              OR      A                   
AA98: 0B              DEC     BC                  
AA99: BC              CP      H                   
AA9A: C9              RET                         
AA9B: B5              OR      L                   
AA9C: 18 A0           JR      $AA3E               ; {}
AA9E: 44              LD      B,H                 
AA9F: 45              LD      B,L                 
AAA0: 56              LD      D,(HL)              
AAA1: 5E              LD      E,(HL)              
AAA2: 29              ADD     HL,HL               
AAA3: A1              AND     C                   
AAA4: 16 71           LD      D,$71               
AAA6: C5              PUSH    BC                  
AAA7: 9C              SBC     H                   
AAA8: 05              DEC     B                   
AAA9: B3              OR      E                   
AAAA: 6B              LD      L,E                 
AAAB: B5              OR      L                   
AAAC: FF              RST     0X38                
AAAD: 01 1A 00        LD      BC,$001A            
AAB0: 89              ADC     A,C                 
AAB1: BC              CP      H                   
AAB2: 81              ADD     A,C                 
AAB3: 10 04           DJNZ    $AAB9               ; {}
AAB5: 0E 5F           LD      C,$5F               
AAB7: BE              CP      (HL)                
AAB8: 5B              LD      E,E                 
AAB9: B1              OR      C                   
AABA: 4B              LD      C,E                 
AABB: 7B              LD      A,E                 
AABC: 46              LD      B,(HL)              
AABD: 45              LD      B,L                 
AABE: 44              LD      B,H                 
AABF: A0              AND     B                   
AAC0: 9F              SBC     A                   
AAC1: 15              DEC     D                   
AAC2: 7F              LD      A,A                 
AAC3: B1              OR      C                   
AAC4: 80              ADD     A,B                 
AAC5: 12              LD      (DE),A              
AAC6: 04              INC     B                   
AAC7: 10 5F           DJNZ    $AB28               ; {}
AAC9: BE              CP      (HL)                
AACA: 5B              LD      E,E                 
AACB: B1              OR      C                   
AACC: 4B              LD      C,E                 
AACD: 7B              LD      A,E                 
AACE: 55              LD      D,L                 
AACF: 45              LD      B,L                 
AAD0: 86              ADD     A,(HL)              
AAD1: 74              LD      (HL),H              
AAD2: 30 6F           JR      NC,$AB43            ; {}
AAD4: 9F              SBC     A                   
AAD5: 15              DEC     D                   
AAD6: 7F              LD      A,A                 
AAD7: B1              OR      C                   
AAD8: 8B              ADC     A,E                 
AAD9: 04              INC     B                   
AADA: 04              INC     B                   
AADB: 02              LD      (BC),A              
AADC: 3B              DEC     SP                  
AADD: F4 AB 15        CALL    P,$15AB             
AAE0: 04              INC     B                   
AAE1: 13              INC     DE                  
AAE2: C7              RST     0X00                
AAE3: DE 94           SBC     $94                 
AAE5: 14              INC     D                   
AAE6: 55              LD      D,L                 
AAE7: 5E              LD      E,(HL)              
AAE8: 8E              ADC     A,(HL)              
AAE9: BE              CP      (HL)                
AAEA: 0B              DEC     BC                  
AAEB: 8A              ADC     A,D                 
AAEC: 96              SUB     (HL)                
AAED: 96              SUB     (HL)                
AAEE: DB 72           IN      A,($72)             
AAF0: F5              PUSH    AF                  
AAF1: 59              LD      E,C                 
AAF2: 3E 62           LD      A,$62               
AAF4: 2E 95           LD      L,$95               
AAF6: 23              INC     HL                  
AAF7: 04              INC     B                   
AAF8: 21 55 45        LD      HL,$4555            
AAFB: 8E              ADC     A,(HL)              
AAFC: 91              SUB     C                   
AAFD: 16 8A           LD      D,$8A               
AAFF: CB B0           RES     6,B                 
AB01: 0F              RRCA                        
AB02: 8A              ADC     A,D                 
AB03: 90              SUB     B                   
AB04: 5F              LD      E,A                 
AB05: F4 59 C8        CALL    P,$C859             
AB08: B5              OR      L                   
AB09: FF              RST     0X38                
AB0A: B2              OR      D                   
AB0B: 82              ADD     A,D                 
AB0C: 17              RLA                         
AB0D: 47              LD      B,A                 
AB0E: 5E              LD      E,(HL)              
AB0F: 66              LD      H,(HL)              
AB10: 49              LD      C,C                 
AB11: 89              ADC     A,C                 
AB12: 17              RLA                         
AB13: 82              ADD     A,D                 
AB14: 17              RLA                         
AB15: 59              LD      E,C                 
AB16: 5E              LD      E,(HL)              
AB17: 66              LD      H,(HL)              
AB18: 62              LD      H,D                 
AB19: 2E 96           LD      L,$96               
AB1B: 1E 04           LD      E,$04               
AB1D: 1C              INC     E                   
AB1E: 58              LD      E,B                 
AB1F: 45              LD      B,L                 
AB20: 66              LD      H,(HL)              
AB21: 49              LD      C,C                 
AB22: CF              RST     0X08                
AB23: 15              DEC     D                   
AB24: 55              LD      D,L                 
AB25: A4              AND     H                   
AB26: 04              INC     B                   
AB27: B7              OR      A                   
AB28: DB 8B           IN      A,($8B)             
AB2A: 10 53           DJNZ    $AB7F               ; {}
AB2C: C0              RET     NZ                  
AB2D: DE C2           SBC     $C2                 
AB2F: 16 9D           LD      D,$9D               
AB31: 61              LD      H,C                 
AB32: AF              XOR     A                   
AB33: 14              INC     D                   
AB34: 04              INC     B                   
AB35: 68              LD      L,B                 
AB36: 5B              LD      E,E                 
AB37: 5E              LD      E,(HL)              
AB38: 3F              CCF                         
AB39: A1              AND     C                   
AB3A: 97              SUB     A                   
AB3B: 1D              DEC     E                   
AB3C: 04              INC     B                   
AB3D: 1B              DEC     DE                  
AB3E: 6B              LD      L,E                 
AB3F: BF              CP      A                   
AB40: 2B              DEC     HL                  
AB41: 6E              LD      L,(HL)              
AB42: 5B              LD      E,E                 
AB43: BE              CP      (HL)                
AB44: 19              ADD     HL,DE               
AB45: BC              CP      H                   
AB46: 3B              DEC     SP                  
AB47: 4A              LD      C,D                 
AB48: 47              LD      B,A                 
AB49: D2 B3 8B        JP      NC,$8BB3            ; {}
AB4C: 23              INC     HL                  
AB4D: 92              SUB     D                   
AB4E: 85              ADD     A,L                 
AB4F: 96              SUB     (HL)                
AB50: 3E 62           LD      A,$62               
AB52: D0              RET     NC                  
AB53: 47              LD      B,A                 
AB54: FF              RST     0X38                
AB55: 14              INC     D                   
AB56: 82              ADD     A,D                 
AB57: 49              LD      C,C                 
AB58: 21 99 50        LD      HL,$5099            
AB5B: 0D              DEC     C                   
AB5C: 4E              LD      C,(HL)              
AB5D: 04              INC     B                   
AB5E: 46              LD      B,(HL)              
AB5F: 83              ADD     A,E                 
AB60: 46              LD      B,(HL)              
AB61: 94              SUB     H                   
AB62: 46              LD      B,(HL)              
AB63: 7C              LD      A,H                 
AB64: B3              OR      E                   
AB65: 7C              LD      A,H                 
AB66: B3              OR      E                   
AB67: F9              LD      SP,HL               
AB68: 6C              LD      L,H                 
AB69: 22 6D 62        LD      ($626D),HL          ; {}
AB6C: 73              LD      (HL),E              
AB6D: C3 06 3C        JP      $3C06               
AB70: 49              LD      C,C                 
AB71: FA 6C AB        JP      M,$AB6C             ; {}
AB74: 70              LD      (HL),B              
AB75: 94              SUB     H                   
AB76: 14              INC     D                   
AB77: BA              CP      D                   
AB78: B1              OR      C                   
AB79: AB              XOR     E                   
AB7A: 70              LD      (HL),B              
AB7B: 5F              LD      E,A                 
AB7C: BE              CP      (HL)                
AB7D: D3 14           OUT     ($14),A             
AB7F: 91              SUB     C                   
AB80: 9B              SBC     E                   
AB81: 99              SBC     C                   
AB82: 96              SUB     (HL)                
AB83: 46              LD      B,(HL)              
AB84: 48              LD      C,B                 
AB85: C7              RST     0X00                
AB86: B5              OR      L                   
AB87: 29              ADD     HL,HL               
AB88: 54              LD      D,H                 
AB89: 51              LD      D,C                 
AB8A: 18 23           JR      $ABAF               ; {}
AB8C: C6 64           ADD     $64                 
AB8E: B7              OR      A                   
AB8F: 8F              ADC     A,A                 
AB90: 5F              LD      E,A                 
AB91: 95              SUB     L                   
AB92: 14              INC     D                   
AB93: 51              LD      D,C                 
AB94: 18 52           JR      $ABE8               ; {}
AB96: C2 70 8E        JP      NZ,$8E70            ; {}
AB99: 9B              SBC     E                   
AB9A: 6C              LD      L,H                 
AB9B: 6B              LD      L,E                 
AB9C: BF              CP      A                   
AB9D: C7              RST     0X00                
AB9E: DE 86           SBC     $86                 
ABA0: AF              XOR     A                   
ABA1: 96              SUB     (HL)                
ABA2: 5F              LD      E,A                 
ABA3: AB              XOR     E                   
ABA4: 70              LD      (HL),B              
ABA5: 20 01           JR      NZ,$ABA8            ; {}
ABA7: 1C              INC     E                   
ABA8: 01 1D 64        LD      BC,$641D            
ABAB: 9A              SBC     D                   
ABAC: 31 04 2F        LD      SP,$2F04            
ABAF: 5F              LD      E,A                 
ABB0: BE              CP      (HL)                
ABB1: D3 14           OUT     ($14),A             
ABB3: 91              SUB     C                   
ABB4: 9B              SBC     E                   
ABB5: 99              SBC     C                   
ABB6: 96              SUB     (HL)                
ABB7: 46              LD      B,(HL)              
ABB8: 48              LD      C,B                 
ABB9: D4 B5 57        CALL    NC,$57B5            
ABBC: 7B              LD      A,E                 
ABBD: 84              ADD     A,H                 
ABBE: 14              INC     D                   
ABBF: 4F              LD      C,A                 
ABC0: A1              AND     C                   
ABC1: 51              LD      D,C                 
ABC2: 18 52           JR      $AC16               ; {}
ABC4: C2 78 B1        JP      NZ,$B178            ; {}
ABC7: 9E              SBC     (HL)                
ABC8: 61              LD      H,C                 
ABC9: 91              SUB     C                   
ABCA: 7A              LD      A,D                 
ABCB: 71              LD      (HL),C              
ABCC: 16 6F           LD      D,$6F               
ABCE: CA 9E 61        JP      Z,$619E             ; {}
ABD1: D0              RET     NC                  
ABD2: 15              DEC     D                   
ABD3: 82              ADD     A,D                 
ABD4: 17              RLA                         
ABD5: 4B              LD      C,E                 
ABD6: 7B              LD      A,E                 
ABD7: 94              SUB     H                   
ABD8: 5A              LD      E,D                 
ABD9: E6 5F           AND     $5F                 
ABDB: C0              RET     NZ                  
ABDC: 7A              LD      A,D                 
ABDD: 2E 98           LD      L,$98               
ABDF: 28 04           JR      Z,$ABE5             ; {}
ABE1: 26 6B           LD      H,$6B               
ABE3: BF              CP      A                   
ABE4: 5F              LD      E,A                 
ABE5: BE              CP      (HL)                
ABE6: 23              INC     HL                  
ABE7: 15              DEC     D                   
ABE8: F3              DI                          
ABE9: B9              CP      C                   
ABEA: C7              RST     0X00                
ABEB: DE D3           SBC     $D3                 
ABED: 14              INC     D                   
ABEE: 95              SUB     L                   
ABEF: 96              SUB     (HL)                
ABF0: 1B              DEC     DE                  
ABF1: 60              LD      H,B                 
ABF2: 1B              DEC     DE                  
ABF3: D1              POP     DE                  
ABF4: 03              INC     BC                  
ABF5: BC              CP      H                   
ABF6: 9F              SBC     A                   
ABF7: A6              AND     (HL)                
ABF8: 3D              DEC     A                   
ABF9: 49              LD      C,C                 
ABFA: 89              ADC     A,C                 
ABFB: 17              RLA                         
ABFC: AF              XOR     A                   
ABFD: 14              INC     D                   
ABFE: 7B              LD      A,E                 
ABFF: 14              INC     D                   
AC00: 54              LD      D,H                 
AC01: 8B              ADC     A,E                 
AC02: 9B              SBC     E                   
AC03: 6C              LD      L,H                 
AC04: 4D              LD      C,L                 
AC05: 8B              ADC     A,E                 
AC06: DB 63           IN      A,($63)             
AC08: 9B              SBC     E                   
AC09: 1C              INC     E                   
AC0A: 04              INC     B                   
AC0B: 1A              LD      A,(DE)              
AC0C: 83              ADD     A,E                 
AC0D: 48              LD      C,B                 
AC0E: 72              LD      (HL),D              
AC0F: 61              LD      H,C                 
AC10: FB              EI                          
AC11: C0              RET     NZ                  
AC12: 89              ADC     A,C                 
AC13: 73              LD      (HL),E              
AC14: B3              OR      E                   
AC15: 75              LD      (HL),L              
AC16: 56              LD      D,(HL)              
AC17: DB D8           IN      A,($D8)             
AC19: B0              OR      B                   
AC1A: 4D              LD      C,L                 
AC1B: 61              LD      H,C                 
AC1C: 23              INC     HL                  
AC1D: 15              DEC     D                   
AC1E: F3              DI                          
AC1F: B9              CP      C                   
AC20: 8E              ADC     A,(HL)              
AC21: 48              LD      C,B                 
AC22: F7              RST     0X30                
AC23: 17              RLA                         
AC24: 17              RLA                         
AC25: BA              CP      D                   
AC26: 8D              ADC     A,L                 
AC27: 0E 0D           LD      C,$0D               
AC29: 0C              INC     C                   
AC2A: 2E 20           LD      L,$20               
AC2C: AA              XOR     D                   
AC2D: 04              INC     B                   
AC2E: 07              RLCA                        
AC2F: 4B              LD      C,E                 
AC30: 7B              LD      A,E                 
AC31: C9              RET                         
AC32: 54              LD      D,H                 
AC33: A6              AND     (HL)                
AC34: B7              OR      A                   
AC35: 2E C7           LD      L,$C7               
AC37: 0E 0D           LD      C,$0D               
AC39: 0C              INC     C                   
AC3A: 2E 20           LD      L,$20               
AC3C: AA              XOR     D                   
AC3D: 04              INC     B                   
AC3E: 07              RLCA                        
AC3F: 4B              LD      C,E                 
AC40: 7B              LD      A,E                 
AC41: 04              INC     B                   
AC42: B2              OR      D                   
AC43: 48              LD      C,B                 
AC44: C5              PUSH    BC                  
AC45: 2E 8F           LD      L,$8F               
AC47: 80              ADD     A,B                 
AC48: 94              SUB     H                   
AC49: 0D              DEC     C                   
AC4A: 80              ADD     A,B                 
AC4B: 91              SUB     C                   
AC4C: 0E 80           LD      C,$80               
AC4E: 8D              ADC     A,L                 
AC4F: 14              INC     D                   
AC50: BF              CP      A                   
AC51: 0D              DEC     C                   
AC52: 23              INC     HL                  
AC53: 2E 10           LD      L,$10               
AC55: AA              XOR     D                   
AC56: 04              INC     B                   
AC57: 1E C3           LD      E,$C3               
AC59: B8              CP      B                   
AC5A: 0B              DEC     BC                  
AC5B: A7              AND     A                   
AC5C: 6C              LD      L,H                 
AC5D: BE              CP      (HL)                
AC5E: 29              ADD     HL,HL               
AC5F: A1              AND     C                   
AC60: 1B              DEC     DE                  
AC61: 71              LD      (HL),C              
AC62: 34              INC     (HL)                
AC63: A1              AND     C                   
AC64: 53              LD      D,E                 
AC65: 15              DEC     D                   
AC66: B7              OR      A                   
AC67: 98              SBC     B                   
AC68: AE              XOR     (HL)                
AC69: B3              OR      E                   
AC6A: 3F              CCF                         
AC6B: 16 D3           LD      D,$D3               
AC6D: 49              LD      C,C                 
AC6E: AB              XOR     E                   
AC6F: 98              SBC     B                   
AC70: 5F              LD      E,A                 
AC71: BE              CP      (HL)                
AC72: 59              LD      E,C                 
AC73: 90              SUB     B                   
AC74: 97              SUB     A                   
AC75: 62              LD      H,D                 
AC76: 0D              DEC     C                   
AC77: 1A              LD      A,(DE)              
AC78: 15              DEC     D                   
AC79: 10 04           DJNZ    $AC7F               ; {}
AC7B: 16 46           LD      D,$46               
AC7D: 77              LD      (HL),A              
AC7E: 05              DEC     B                   
AC7F: A0              AND     B                   
AC80: 16 BC           LD      D,$BC               
AC82: 90              SUB     B                   
AC83: 73              LD      (HL),E              
AC84: CA 83 59        JP      Z,$5983             
AC87: 5E              LD      E,(HL)              
AC88: 46              LD      B,(HL)              
AC89: 7A              LD      A,D                 
AC8A: E1              POP     HL                  
AC8B: 14              INC     D                   
AC8C: 5F              LD      E,A                 
AC8D: A0              AND     B                   
AC8E: D6 B0           SUB     $B0                 
AC90: DB 63           IN      A,($63)             
AC92: 0D              DEC     C                   
AC93: 22 14 15        LD      ($1514),HL          
AC96: 20 14           JR      NZ,$ACAC            ; {}
AC98: 2D              DEC     L                   
AC99: 5C              LD      E,H                 
AC9A: 04              INC     B                   
AC9B: 18 C7           JR      $AC64               ; {}
AC9D: DE 94           SBC     $94                 
AC9F: 14              INC     D                   
ACA0: 53              LD      D,E                 
ACA1: 5E              LD      E,(HL)              
ACA2: D6 C4           SUB     $C4                 
ACA4: 4B              LD      C,E                 
ACA5: 5E              LD      E,(HL)              
ACA6: 13              INC     DE                  
ACA7: 98              SBC     B                   
ACA8: 44              LD      B,H                 
ACA9: A4              AND     H                   
ACAA: DB 8B           IN      A,($8B)             
ACAC: C3 9E 6F        JP      $6F9E               ; {}
ACAF: B1              OR      C                   
ACB0: 53              LD      D,E                 
ACB1: A1              AND     C                   
ACB2: AB              XOR     E                   
ACB3: 98              SBC     B                   
ACB4: AA              XOR     D                   
ACB5: 8B              ADC     A,E                 
ACB6: 18 0D           JR      $ACC5               ; {}
ACB8: 18 0F           JR      $ACC9               ; {}
ACBA: 14              INC     D                   
ACBB: 39              ADD     HL,SP               
ACBC: 04              INC     B                   
ACBD: 12              LD      (DE),A              
ACBE: C7              RST     0X00                
ACBF: DE D3           SBC     $D3                 
ACC1: 14              INC     D                   
ACC2: E6 96           AND     $96                 
ACC4: D3 14           OUT     ($14),A             
ACC6: 83              ADD     A,E                 
ACC7: B3              OR      E                   
ACC8: 82              ADD     A,D                 
ACC9: 17              RLA                         
ACCA: 73              LD      (HL),E              
ACCB: 49              LD      C,C                 
ACCC: A5              AND     L                   
ACCD: 94              SUB     H                   
ACCE: 9B              SBC     E                   
ACCF: 76              HALT                        
ACD0: 10 0D           DJNZ    $ACDF               ; {}
ACD2: 08              EX      AF,AF'              
ACD3: 0F              RRCA                        
ACD4: AA              XOR     D                   
ACD5: 04              INC     B                   
ACD6: 04              INC     B                   
ACD7: 4D              LD      C,L                 
ACD8: BD              CP      L                   
ACD9: A7              AND     A                   
ACDA: 61              LD      H,C                 
ACDB: C1              POP     BC                  
ACDC: 18 A2           JR      $AC80               ; {}
ACDE: 13              INC     DE                  
ACDF: 0D              DEC     C                   
ACE0: 11 1A 18        LD      DE,$181A            
ACE3: 04              INC     B                   
ACE4: 0B              DEC     BC                  
ACE5: C7              RST     0X00                
ACE6: DE 8E           SBC     $8E                 
ACE8: 14              INC     D                   
ACE9: 63              LD      H,E                 
ACEA: B1              OR      C                   
ACEB: FB              EI                          
ACEC: 5C              LD      E,H                 
ACED: 58              LD      E,B                 
ACEE: 72              LD      (HL),D              
ACEF: 45              LD      B,L                 
ACF0: AA              XOR     D                   
ACF1: 8B              ADC     A,E                 
ACF2: 90              SUB     B                   
ACF3: 09              ADD     HL,BC               
ACF4: 0B              DEC     BC                  
ACF5: 07              RLCA                        
ACF6: 0A              LD      A,(BC)              
ACF7: 36 01           LD      (HL),$01            
ACF9: 91              SUB     C                   
ACFA: 37              SCF                         
ACFB: 01 91 91        LD      BC,$9191            
ACFE: 19              ADD     HL,DE               
ACFF: 1F              RRA                         
AD00: 17              RLA                         
AD01: FF              RST     0X38                
AD02: A5              AND     L                   
AD03: 57              LD      D,A                 
AD04: 49              LD      C,C                 
AD05: B5              OR      L                   
AD06: 17              RLA                         
AD07: 46              LD      B,(HL)              
AD08: 5E              LD      E,(HL)              
AD09: 2F              CPL                         
AD0A: 7B              LD      A,E                 
AD0B: 03              INC     BC                  
AD0C: 56              LD      D,(HL)              
AD0D: 1D              DEC     E                   
AD0E: A0              AND     B                   
AD0F: A6              AND     (HL)                
AD10: 16 3F           LD      D,$3F               
AD12: BB              CP      E                   
AD13: 11 EE 99        LD      DE,$99EE            
AD16: AF              XOR     A                   
AD17: 2E 92           LD      L,$92               
AD19: 1F              RRA                         
AD1A: 0D              DEC     C                   
AD1B: 1D              DEC     E                   
AD1C: 1A              LD      A,(DE)              
AD1D: 14              INC     D                   
AD1E: 15              DEC     D                   
AD1F: 08              EX      AF,AF'              
AD20: 04              INC     B                   
AD21: 17              RLA                         
AD22: C7              RST     0X00                
AD23: DE 8C           SBC     $8C                 
AD25: 17              RLA                         
AD26: 26 79           LD      H,$79               
AD28: 04              INC     B                   
AD29: EE 73           XOR     $73                 
AD2B: C6 C7           ADD     $C7                 
AD2D: DE E1           SBC     $E1                 
AD2F: 14              INC     D                   
AD30: 3E C5           LD      A,$C5               
AD32: E6 96           AND     $96                 
AD34: 09              ADD     HL,BC               
AD35: 15              DEC     D                   
AD36: D6 15           SUB     $15                 
AD38: 2E 94           LD      L,$94               
AD3A: 06 0D           LD      B,$0D               
AD3C: 04              INC     B                   
AD3D: 30 80           JR      NC,$ACBF            ; {}
AD3F: 2F              CPL                         
AD40: 01 A3 36        LD      BC,$36A3            
AD43: 0D              DEC     C                   
AD44: 34              INC     (HL)                
AD45: 3A 2C 01        LD      A,($012C)           
AD48: 30 80           JR      NC,$ACCA            ; {}
AD4A: 17              RLA                         
AD4B: 01 80 1F        LD      BC,$1F80            
AD4E: 1A              LD      A,(DE)              
AD4F: DF              RST     0X18                
AD50: 2C              INC     L                   
AD51: DF              RST     0X18                
AD52: 2C              INC     L                   
AD53: DF              RST     0X18                
AD54: 2C              INC     L                   
AD55: DF              RST     0X18                
AD56: 2C              INC     L                   
AD57: DF              RST     0X18                
AD58: 2C              INC     L                   
AD59: 5A              LD      E,D                 
AD5A: 2C              INC     L                   
AD5B: 99              SBC     C                   
AD5C: 61              LD      H,C                 
AD5D: BE              CP      (HL)                
AD5E: B5              OR      L                   
AD5F: 76              HALT                        
AD60: 26 76           LD      H,$76               
AD62: 26 76           LD      H,$76               
AD64: 26 76           LD      H,$76               
AD66: 26 76           LD      H,$76               
AD68: 26 25           LD      H,$25               
AD6A: 1F              RRA                         
AD6B: 0C              INC     C                   
AD6C: 0C              INC     C                   
AD6D: BA              CP      D                   
AD6E: 91              SUB     C                   
AD6F: 48              LD      C,B                 
AD70: 46              LD      B,(HL)              
AD71: 62              LD      H,D                 
AD72: AF              XOR     A                   
AD73: 14              INC     D                   
AD74: 14              INC     D                   
AD75: D0              RET     NC                  
AD76: EB              EX      DE,HL               
AD77: 5D              LD      E,L                 
AD78: 25              DEC     H                   
AD79: A5              AND     L                   
AD7A: 12              LD      (DE),A              
AD7B: 0D              DEC     C                   
AD7C: 10 14           DJNZ    $AD92               ; {}
AD7E: 2E 20           LD      L,$20               
AD80: A8              XOR     B                   
AD81: 04              INC     B                   
AD82: 0A              LD      A,(BC)              
AD83: 4B              LD      C,E                 
AD84: 7B              LD      A,E                 
AD85: 06 9A           LD      B,$9A               
AD87: DE 14           SBC     $14                 
AD89: D7              RST     0X10                
AD8A: A0              AND     B                   
AD8B: 9B              SBC     E                   
AD8C: 5D              LD      E,L                 
AD8D: A6              AND     (HL)                
AD8E: 26 0E           LD      H,$0E               
AD90: 24              INC     H                   
AD91: 0D              DEC     C                   
AD92: 0D              DEC     C                   
AD93: 29              ADD     HL,HL               
AD94: A8              XOR     B                   
AD95: 04              INC     B                   
AD96: 08              EX      AF,AF'              
AD97: 4B              LD      C,E                 
AD98: 7B              LD      A,E                 
AD99: 09              ADD     HL,BC               
AD9A: 9A              SBC     D                   
AD9B: C2 16 A7        JP      NZ,$A716            ; {}
AD9E: 61              LD      H,C                 
AD9F: 0C              INC     C                   
ADA0: 0D              DEC     C                   
ADA1: 11 1A 15        LD      DE,$151A            
ADA4: 02              LD      (BC),A              
ADA5: 14              INC     D                   
ADA6: 2E 80           LD      L,$80               
ADA8: 14              INC     D                   
ADA9: 33              INC     SP                  
ADAA: A8              XOR     B                   
ADAB: 04              INC     B                   
ADAC: 06 4B           LD      B,$4B               
ADAE: 7B              LD      A,E                 
ADAF: 72              LD      (HL),D              
ADB0: 61              LD      H,C                 
ADB1: 1F              RRA                         
ADB2: C1              POP     BC                  
ADB3: 14              INC     D                   
ADB4: 0C              INC     C                   
ADB5: A8              XOR     B                   
ADB6: 0C              INC     C                   
ADB7: 0D              DEC     C                   
ADB8: 0A              LD      A,(BC)              
ADB9: 1A              LD      A,(DE)              
ADBA: 0E 06           LD      C,$06               
ADBC: 15              DEC     D                   
ADBD: 10 1F           DJNZ    $ADDE               ; {}
ADBF: 02              LD      (BC),A              
ADC0: 5F              LD      E,A                 
ADC1: BE              CP      (HL)                
ADC2: 11 A9 0C        LD      DE,$0CA9            
ADC5: 0D              DEC     C                   
ADC6: 0A              LD      A,(BC)              
ADC7: 1B              DEC     DE                  
ADC8: 0E 06           LD      C,$06               
ADCA: 15              DEC     D                   
ADCB: 10 1F           DJNZ    $ADEC               ; {}
ADCD: 02              LD      (BC),A              
ADCE: 5F              LD      E,A                 
ADCF: BE              CP      (HL)                
ADD0: 12              LD      (DE),A              
ADD1: AA              XOR     D                   
ADD2: 0B              DEC     BC                  
ADD3: 0D              DEC     C                   
ADD4: 09              ADD     HL,BC               
ADD5: 0E 06           LD      C,$06               
ADD7: 15              DEC     D                   
ADD8: 10 1F           DJNZ    $ADF9               ; {}
ADDA: 02              LD      (BC),A              
ADDB: 5F              LD      E,A                 
ADDC: BE              CP      (HL)                
ADDD: 16 9C           LD      D,$9C               
ADDF: 53              LD      D,E                 
ADE0: 0D              DEC     C                   
ADE1: 51              LD      D,C                 
ADE2: 04              INC     B                   
ADE3: 04              INC     B                   
ADE4: 52              LD      D,D                 
ADE5: 86              ADD     A,(HL)              
ADE6: 5B              LD      E,E                 
ADE7: B9              CP      C                   
ADE8: 0E 08           LD      C,$08               
ADEA: C3 04 05        JP      $0504               
ADED: D4 47 75        CALL    NC,$7547            ; {}
ADF0: 8D              ADC     A,L                 
ADF1: 4B              LD      C,E                 
ADF2: 8B              ADC     A,E                 
ADF3: 04              INC     B                   
ADF4: 3E C7           LD      A,$C7               
ADF6: DE 94           SBC     $94                 
ADF8: 14              INC     D                   
ADF9: 4B              LD      C,E                 
ADFA: 5E              LD      E,(HL)              
ADFB: 83              ADD     A,E                 
ADFC: 96              SUB     (HL)                
ADFD: 5F              LD      E,A                 
ADFE: 17              RLA                         
ADFF: 46              LD      B,(HL)              
AE00: 48              LD      C,B                 
AE01: 84              ADD     A,H                 
AE02: 15              DEC     D                   
AE03: 3B              DEC     SP                  
AE04: 63              LD      H,E                 
AE05: 01 B3 DB        LD      BC,$DBB3            
AE08: 95              SUB     L                   
AE09: 5F              LD      E,A                 
AE0A: BE              CP      (HL)                
AE0B: 5B              LD      E,E                 
AE0C: B1              OR      C                   
AE0D: 4B              LD      C,E                 
AE0E: 7B              LD      A,E                 
AE0F: 52              LD      D,D                 
AE10: 45              LD      B,L                 
AE11: 8F              ADC     A,A                 
AE12: 48              LD      C,B                 
AE13: 19              ADD     HL,DE               
AE14: 8A              ADC     A,D                 
AE15: 82              ADD     A,D                 
AE16: 7B              LD      A,E                 
AE17: 91              SUB     C                   
AE18: 17              RLA                         
AE19: C4 9C 8E        CALL    NZ,$8E9C            ; {}
AE1C: C6 1D           ADD     $1D                 
AE1E: A0              AND     B                   
AE1F: 11 EE 5B        LD      DE,$5BEE            
AE22: 98              SBC     B                   
AE23: 4B              LD      C,E                 
AE24: 7B              LD      A,E                 
AE25: 66              LD      H,(HL)              
AE26: B1              OR      C                   
AE27: 90              SUB     B                   
AE28: 14              INC     D                   
AE29: 11 58 5B        LD      DE,$5B58            
AE2C: 98              SBC     B                   
AE2D: 4B              LD      C,E                 
AE2E: 7B              LD      A,E                 
AE2F: 8F              ADC     A,A                 
AE30: 4E              LD      C,(HL)              
AE31: DB 63           IN      A,($63)             
AE33: B0              OR      B                   
AE34: 5F              LD      E,A                 
AE35: 0D              DEC     C                   
AE36: 5D              LD      E,L                 
AE37: 04              INC     B                   
AE38: 04              INC     B                   
AE39: 52              LD      D,D                 
AE3A: 86              ADD     A,(HL)              
AE3B: 5B              LD      E,E                 
AE3C: B9              CP      C                   
AE3D: 0E 08           LD      C,$08               
AE3F: C3 04 05        JP      $0504               
AE42: D4 47 75        CALL    NC,$7547            ; {}
AE45: 8D              ADC     A,L                 
AE46: 4B              LD      C,E                 
AE47: 8B              ADC     A,E                 
AE48: 04              INC     B                   
AE49: 4A              LD      C,D                 
AE4A: C7              RST     0X00                
AE4B: DE 94           SBC     $94                 
AE4D: 14              INC     D                   
AE4E: 4B              LD      C,E                 
AE4F: 5E              LD      E,(HL)              
AE50: 83              ADD     A,E                 
AE51: 96              SUB     (HL)                
AE52: 5F              LD      E,A                 
AE53: 17              RLA                         
AE54: 46              LD      B,(HL)              
AE55: 48              LD      C,B                 
AE56: 84              ADD     A,H                 
AE57: 15              DEC     D                   
AE58: 3B              DEC     SP                  
AE59: 4A              LD      C,D                 
AE5A: 01 B3 DB        LD      BC,$DBB3            
AE5D: 95              SUB     L                   
AE5E: 5F              LD      E,A                 
AE5F: BE              CP      (HL)                
AE60: 5B              LD      E,E                 
AE61: B1              OR      C                   
AE62: 4B              LD      C,E                 
AE63: 7B              LD      A,E                 
AE64: 52              LD      D,D                 
AE65: 45              LD      B,L                 
AE66: 8F              ADC     A,A                 
AE67: 48              LD      C,B                 
AE68: 19              ADD     HL,DE               
AE69: 8A              ADC     A,D                 
AE6A: 82              ADD     A,D                 
AE6B: 7B              LD      A,E                 
AE6C: 82              ADD     A,D                 
AE6D: 17              RLA                         
AE6E: 67              LD      H,A                 
AE6F: B1              OR      C                   
AE70: BF              CP      A                   
AE71: 14              INC     D                   
AE72: 49              LD      C,C                 
AE73: C0              RET     NZ                  
AE74: AE              XOR     (HL)                
AE75: 9A              SBC     D                   
AE76: C0              RET     NZ                  
AE77: 16 4B           LD      D,$4B               
AE79: 5E              LD      E,(HL)              
AE7A: D4 B5 16        CALL    NC,$16B5            
AE7D: 60              LD      H,B                 
AE7E: C0              RET     NZ                  
AE7F: 16 4B           LD      D,$4B               
AE81: 5E              LD      E,(HL)              
AE82: C4 B5 67        CALL    NZ,$67B5            ; {}
AE85: 8E              ADC     A,(HL)              
AE86: 03              INC     BC                  
AE87: EE 33           XOR     $33                 
AE89: 98              SBC     B                   
AE8A: 0F              RRCA                        
AE8B: A0              AND     B                   
AE8C: D5              PUSH    DE                  
AE8D: 15              DEC     D                   
AE8E: 47              LD      B,A                 
AE8F: 18 09           JR      $AE9A               ; {}
AE91: 8D              ADC     A,L                 
AE92: 5B              LD      E,E                 
AE93: D4 9D 74        CALL    NC,$749D            ; {}
AE96: 0D              DEC     C                   
AE97: 72              LD      (HL),D              
AE98: 04              INC     B                   
AE99: 05              DEC     B                   
AE9A: 89              ADC     A,C                 
AE9B: 4E              LD      C,(HL)              
AE9C: E2 87 41        JP      PO,$4187            
AE9F: 0E 06           LD      C,$06               
AEA1: C3 04 03        JP      $0304               
AEA4: 23              INC     HL                  
AEA5: 63              LD      H,E                 
AEA6: 54              LD      D,H                 
AEA7: 8B              ADC     A,E                 
AEA8: 04              INC     B                   
AEA9: 60              LD      H,B                 
AEAA: C7              RST     0X00                
AEAB: DE 94           SBC     $94                 
AEAD: 14              INC     D                   
AEAE: 4B              LD      C,E                 
AEAF: 5E              LD      E,(HL)              
AEB0: 83              ADD     A,E                 
AEB1: 96              SUB     (HL)                
AEB2: 5F              LD      E,A                 
AEB3: 17              RLA                         
AEB4: 46              LD      B,(HL)              
AEB5: 48              LD      C,B                 
AEB6: E7              RST     0X20                
AEB7: 14              INC     D                   
AEB8: 05              DEC     B                   
AEB9: 4E              LD      C,(HL)              
AEBA: FF              RST     0X38                
AEBB: 8B              ADC     A,E                 
AEBC: 82              ADD     A,D                 
AEBD: 17              RLA                         
AEBE: 2F              CPL                         
AEBF: 62              LD      H,D                 
AEC0: D5              PUSH    DE                  
AEC1: 15              DEC     D                   
AEC2: 7B              LD      A,E                 
AEC3: 14              INC     D                   
AEC4: 2E DD           LD      L,$DD               
AEC6: 89              ADC     A,C                 
AEC7: 8D              ADC     A,L                 
AEC8: BF              CP      A                   
AEC9: 14              INC     D                   
AECA: 49              LD      C,C                 
AECB: C0              RET     NZ                  
AECC: 91              SUB     C                   
AECD: 96              SUB     (HL)                
AECE: 96              SUB     (HL)                
AECF: 96              SUB     (HL)                
AED0: DB 72           IN      A,($72)             
AED2: 6A              LD      L,D                 
AED3: A0              AND     B                   
AED4: DB A0           IN      A,($A0)             
AED6: DB BD           IN      A,($BD)             
AED8: 0E D0           LD      C,$D0               
AEDA: 9B              SBC     E                   
AEDB: 8F              ADC     A,A                 
AEDC: 03              INC     BC                  
AEDD: A0              AND     B                   
AEDE: 5F              LD      E,A                 
AEDF: BE              CP      (HL)                
AEE0: 8F              ADC     A,A                 
AEE1: 16 23           LD      D,$23               
AEE3: 49              LD      C,C                 
AEE4: 0E D0           LD      C,$D0               
AEE6: 16 8A           LD      D,$8A               
AEE8: F4 72 4B        CALL    P,$4B72             
AEEB: 5E              LD      E,(HL)              
AEEC: C3 B5 5F        JP      $5FB5               ; {}
AEEF: 17              RLA                         
AEF0: 46              LD      B,(HL)              
AEF1: 48              LD      C,B                 
AEF2: 63              LD      H,E                 
AEF3: 17              RLA                         
AEF4: 94              SUB     H                   
AEF5: C3 4A 5E        JP      $5E4A               ; {}
AEF8: BF              CP      A                   
AEF9: 9F              SBC     A                   
AEFA: 84              ADD     A,H                 
AEFB: 14              INC     D                   
AEFC: 36 A1           LD      (HL),$A1            
AEFE: 91              SUB     C                   
AEFF: 17              RLA                         
AF00: CB 9C           RES     3,H                 
AF02: 1A              LD      A,(DE)              
AF03: 98              SBC     B                   
AF04: 4B              LD      C,E                 
AF05: 62              LD      H,D                 
AF06: E7              RST     0X20                
AF07: 59              LD      E,C                 
AF08: 9B              SBC     E                   
AF09: A8              XOR     B                   
AF0A: 9E              SBC     (HL)                
AF0B: 03              INC     BC                  
AF0C: 17              RLA                         
AF0D: 3E 00           LD      A,$00               
AF0F: 9F              SBC     A                   
AF10: 0A              LD      A,(BC)              
AF11: 0D              DEC     C                   
AF12: 08              EX      AF,AF'              
AF13: 0A              LD      A,(BC)              
AF14: 12              LD      (DE),A              
AF15: 08              EX      AF,AF'              
AF16: 3F              CCF                         
AF17: AD              XOR     L                   
AF18: 17              RLA                         
AF19: 3E 3F           LD      A,$3F               
AF1B: A0              AND     B                   
AF1C: 0A              LD      A,(BC)              
AF1D: 0D              DEC     C                   
AF1E: 08              EX      AF,AF'              
AF1F: 0A              LD      A,(BC)              
AF20: 12              LD      (DE),A              
AF21: 08              EX      AF,AF'              
AF22: 40              LD      B,B                 
AF23: AD              XOR     L                   
AF24: 17              RLA                         
AF25: 3E 40           LD      A,$40               
AF27: A1              AND     C                   
AF28: 0A              LD      A,(BC)              
AF29: 0D              DEC     C                   
AF2A: 08              EX      AF,AF'              
AF2B: 0A              LD      A,(BC)              
AF2C: 12              LD      (DE),A              
AF2D: 08              EX      AF,AF'              
AF2E: 41              LD      B,C                 
AF2F: AD              XOR     L                   
AF30: 17              RLA                         
AF31: 3E 41           LD      A,$41               
AF33: AC              XOR     H                   
AF34: 0A              LD      A,(BC)              
AF35: 0D              DEC     C                   
AF36: 08              EX      AF,AF'              
AF37: 0A              LD      A,(BC)              
AF38: 12              LD      (DE),A              
AF39: 08              EX      AF,AF'              
AF3A: 42              LD      B,D                 
AF3B: AD              XOR     L                   
AF3C: 17              RLA                         
AF3D: 3E 42           LD      A,$42               
AF3F: AD              XOR     L                   
AF40: 54              LD      D,H                 
AF41: 0E 52           LD      C,$52               
AF43: 0D              DEC     C                   
AF44: 3B              DEC     SP                  
AF45: 14              INC     D                   
AF46: 37              SCF                         
AF47: 03              INC     BC                  
AF48: 00              NOP                         
AF49: 3E 04           LD      A,$04               
AF4B: 34              INC     (HL)                
AF4C: 44              LD      B,H                 
AF4D: 45              LD      B,L                 
AF4E: 45              LD      B,L                 
AF4F: 8B              ADC     A,E                 
AF50: D1              POP     DE                  
AF51: 83              ADD     A,E                 
AF52: CE C9           ADC     $C9                 
AF54: 92              SUB     D                   
AF55: 14              INC     D                   
AF56: E3              EX      (SP),HL             
AF57: A4              AND     H                   
AF58: 8B              ADC     A,E                 
AF59: B3              OR      E                   
AF5A: 03              INC     BC                  
AF5B: A0              AND     B                   
AF5C: 5F              LD      E,A                 
AF5D: BE              CP      (HL)                
AF5E: F3              DI                          
AF5F: 17              RLA                         
AF60: F3              DI                          
AF61: 8C              ADC     A,H                 
AF62: 8E              ADC     A,(HL)              
AF63: 48              LD      C,B                 
AF64: 3A 15 50        LD      A,($5015)           
AF67: A4              AND     H                   
AF68: 0B              DEC     BC                  
AF69: 5C              LD      E,H                 
AF6A: 6B              LD      L,E                 
AF6B: BF              CP      A                   
AF6C: 47              LD      B,A                 
AF6D: 48              LD      C,B                 
AF6E: E6 A0           AND     $A0                 
AF70: 63              LD      H,E                 
AF71: 16 95           LD      D,$95               
AF73: 96              SUB     (HL)                
AF74: 6F              LD      L,A                 
AF75: 7C              LD      A,H                 
AF76: 12              LD      (DE),A              
AF77: 58              LD      E,B                 
AF78: 02              LD      (BC),A              
AF79: B3              OR      E                   
AF7A: BE              CP      (HL)                
AF7B: A0              AND     B                   
AF7C: C0              RET     NZ                  
AF7D: 7A              LD      A,D                 
AF7E: 5B              LD      E,E                 
AF7F: BB              CP      E                   
AF80: 0D              DEC     C                   
AF81: 0F              RRCA                        
AF82: 14              INC     D                   
AF83: 37              SCF                         
AF84: 04              INC     B                   
AF85: 0B              DEC     BC                  
AF86: 06 9A           LD      B,$9A               
AF88: 90              SUB     B                   
AF89: 73              LD      (HL),E              
AF8A: CA 6A EA        JP      Z,$EA6A             
AF8D: 48              LD      C,B                 
AF8E: 9D              SBC     L                   
AF8F: 61              LD      H,C                 
AF90: 2E 0D           LD      L,$0D               
AF92: 02              LD      (BC),A              
AF93: 1A              LD      A,(DE)              
AF94: C1              POP     BC                  
AF95: AE              XOR     (HL)                
AF96: 21 0D 1F        LD      HL,$1F0D            
AF99: 03              INC     BC                  
AF9A: 00              NOP                         
AF9B: 3E 04           LD      A,$04               
AF9D: 1A              LD      A,(DE)              
AF9E: C7              RST     0X00                
AF9F: DE FB           SBC     $FB                 
AFA1: 17              RLA                         
AFA2: F3              DI                          
AFA3: 8C              ADC     A,H                 
AFA4: 58              LD      E,B                 
AFA5: 72              LD      (HL),D              
AFA6: 56              LD      D,(HL)              
AFA7: 5E              LD      E,(HL)              
AFA8: D2 9C 5A        JP      NC,$5A9C            
AFAB: C6 7B           ADD     $7B                 
AFAD: 14              INC     D                   
AFAE: F6 4F           OR      $4F                 
AFB0: 80              ADD     A,B                 
AFB1: BF              CP      A                   
AFB2: 06 EE           LD      B,$EE               
AFB4: 6F              LD      L,A                 
AFB5: C5              PUSH    BC                  
AFB6: EB              EX      DE,HL               
AFB7: DA AF 13        JP      C,$13AF             
AFBA: 0D              DEC     C                   
AFBB: 11 0A 12        LD      DE,$120A            
AFBE: 04              INC     B                   
AFBF: 06 55           LD      B,$55               
AFC1: 77              LD      (HL),A              
AFC2: 1B              DEC     DE                  
AFC3: 60              LD      H,B                 
AFC4: EB              EX      DE,HL               
AFC5: 99              SBC     C                   
AFC6: 11 04 04        LD      DE,$0404            
AFC9: F4 72 DB        CALL    P,$DB72             
AFCC: 63              LD      H,E                 
AFCD: B1              OR      C                   
AFCE: 0E 0D           LD      C,$0D               
AFD0: 0C              INC     C                   
AFD1: 04              INC     B                   
AFD2: 01 20 AA        LD      BC,$AA20            
AFD5: 04              INC     B                   
AFD6: 06 40           LD      B,$40               
AFD8: 55              LD      D,L                 
AFD9: 4B              LD      C,E                 
AFDA: BD              CP      L                   
AFDB: 8B              ADC     A,E                 
AFDC: 9A              SBC     D                   
AFDD: B2              OR      D                   
AFDE: 11 0D 0F        LD      DE,$0F0D            
AFE1: 04              INC     B                   
AFE2: 02              LD      (BC),A              
AFE3: C0              RET     NZ                  
AFE4: 16 AA           LD      D,$AA               
AFE6: 04              INC     B                   
AFE7: 08              EX      AF,AF'              
AFE8: 10 53           DJNZ    $B03D               ; {}
AFEA: AF              XOR     A                   
AFEB: 14              INC     D                   
AFEC: 57              LD      D,A                 
AFED: 17              RLA                         
AFEE: 83              ADD     A,E                 
AFEF: 61              LD      H,C                 
AFF0: B3              OR      E                   
AFF1: 0C              INC     C                   
AFF2: 0D              DEC     C                   
AFF3: 0A              LD      A,(BC)              
AFF4: 1F              RRA                         
AFF5: 07              RLCA                        
AFF6: 95              SUB     L                   
AFF7: 5A              LD      E,D                 
AFF8: C7              RST     0X00                
AFF9: 83              ADD     A,E                 
AFFA: 79              LD      A,C                 
AFFB: B3              OR      E                   
AFFC: 52              LD      D,D                 
AFFD: 25              DEC     H                   
AFFE: B4              OR      H                   
AFFF: 04              INC     B                   
B000: 04              INC     B                   
B001: 02              LD      (BC),A              
B002: 8E              ADC     A,(HL)              
B003: 48              LD      C,B                 
B004: B5              OR      L                   
B005: 0D              DEC     C                   
B006: 04              INC     B                   
B007: 0B              DEC     BC                  
B008: 7B              LD      A,E                 
B009: 50              LD      D,B                 
B00A: C7              RST     0X00                
B00B: DE 85           SBC     $85                 
B00D: AF              XOR     A                   
B00E: EF              RST     0X28                
B00F: 9F              SBC     A                   
B010: 8E              ADC     A,(HL)              
B011: 48              LD      C,B                 
B012: 2E B6           LD      L,$B6               
B014: 3C              INC     A                   
B015: 04              INC     B                   
B016: 3A 73 7B        LD      A,($7B73)           ; {}
B019: 4B              LD      C,E                 
B01A: 7B              LD      A,E                 
B01B: 73              LD      (HL),E              
B01C: A5              AND     L                   
B01D: 45              LD      B,L                 
B01E: B8              CP      B                   
B01F: 46              LD      B,(HL)              
B020: 48              LD      C,B                 
B021: 4B              LD      C,E                 
B022: DB E9           IN      A,($E9)             
B024: 93              SUB     E                   
B025: DB B9           IN      A,($B9)             
B027: 7F              LD      A,A                 
B028: 4E              LD      C,(HL)              
B029: 59              LD      E,C                 
B02A: 15              DEC     D                   
B02B: 96              SUB     (HL)                
B02C: AF              XOR     A                   
B02D: 2B              DEC     HL                  
B02E: D2 34 9E        JP      NC,$9E34            ; {}
B031: E6 5F           AND     $5F                 
B033: D6 B5           SUB     $B5                 
B035: D1              POP     DE                  
B036: 9C              SBC     H                   
B037: 67              LD      H,A                 
B038: 53              LD      D,E                 
B039: FB              EI                          
B03A: A7              AND     A                   
B03B: 5F              LD      E,A                 
B03C: BE              CP      (HL)                
B03D: 53              LD      D,E                 
B03E: 17              RLA                         
B03F: 1B              DEC     DE                  
B040: 92              SUB     D                   
B041: 5B              LD      E,E                 
B042: B9              CP      C                   
B043: 9B              SBC     E                   
B044: 53              LD      D,E                 
B045: 73              LD      (HL),E              
B046: 49              LD      C,C                 
B047: 5F              LD      E,A                 
B048: BE              CP      (HL)                
B049: 53              LD      D,E                 
B04A: 17              RLA                         
B04B: 1B              DEC     DE                  
B04C: 92              SUB     D                   
B04D: 8F              ADC     A,A                 
B04E: BE              CP      (HL)                
B04F: DB 63           IN      A,($63)             
B051: B7              OR      A                   
B052: 16 0D           LD      D,$0D               
B054: 14              INC     D                   
B055: 2E 20           LD      L,$20               
B057: 04              INC     B                   
B058: 0E C7           LD      C,$C7               
B05A: DE FB           SBC     $FB                 
B05C: 17              RLA                         
B05D: F3              DI                          
B05E: 8C              ADC     A,H                 
B05F: 58              LD      E,B                 
B060: 72              LD      (HL),D              
B061: 56              LD      D,(HL)              
B062: 5E              LD      E,(HL)              
B063: D1              POP     DE                  
B064: 9C              SBC     H                   
B065: F0              RET     P                   
B066: A4              AND     H                   
B067: AA              XOR     D                   
B068: 8B              ADC     A,E                 
B069: B8              CP      B                   
B06A: 24              INC     H                   
B06B: 04              INC     B                   
B06C: 22 C7 DE        LD      ($DEC7),HL          
B06F: 20 16           JR      NZ,$B087            ; {}
B071: 6B              LD      L,E                 
B072: A1              AND     C                   
B073: C7              RST     0X00                
B074: DE D3           SBC     $D3                 
B076: 14              INC     D                   
B077: E6 96           AND     $96                 
B079: 09              ADD     HL,BC               
B07A: 15              DEC     D                   
B07B: 82              ADD     A,D                 
B07C: 17              RLA                         
B07D: 73              LD      (HL),E              
B07E: 49              LD      C,C                 
B07F: 14              INC     D                   
B080: 6C              LD      L,H                 
B081: C9              RET                         
B082: 4C              LD      C,H                 
B083: 4B              LD      C,E                 
B084: 5E              LD      E,(HL)              
B085: 96              SUB     (HL)                
B086: 96              SUB     (HL)                
B087: F5              PUSH    AF                  
B088: 72              LD      (HL),D              
B089: 49              LD      C,C                 
B08A: 5E              LD      E,(HL)              
B08B: 67              LD      H,A                 
B08C: 48              LD      C,B                 
B08D: 6B              LD      L,E                 
B08E: B5              OR      L                   
B08F: B9              CP      C                   
B090: 2E 04           LD      L,$04               
B092: 2C              INC     L                   
B093: 83              ADD     A,E                 
B094: 7A              LD      A,D                 
B095: 5F              LD      E,A                 
B096: BE              CP      (HL)                
B097: E1              POP     HL                  
B098: 14              INC     D                   
B099: CF              RST     0X08                
B09A: B2              OR      D                   
B09B: 95              SUB     L                   
B09C: AF              XOR     A                   
B09D: 50              LD      D,B                 
B09E: BD              CP      L                   
B09F: 0B              DEC     BC                  
B0A0: 5C              LD      E,H                 
B0A1: 83              ADD     A,E                 
B0A2: 48              LD      C,B                 
B0A3: 8D              ADC     A,L                 
B0A4: 48              LD      C,B                 
B0A5: 30 79           JR      NC,$B120            ; {}
B0A7: 14              INC     D                   
B0A8: BC              CP      H                   
B0A9: 03              INC     BC                  
B0AA: 47              LD      B,A                 
B0AB: C3 9C 07        JP      $079C               
B0AE: 4F              LD      C,A                 
B0AF: 16 BC           LD      D,$BC               
B0B1: DB 72           IN      A,($72)             
B0B3: 5C              LD      E,H                 
B0B4: B8              CP      B                   
B0B5: 51              LD      D,C                 
B0B6: 5E              LD      E,(HL)              
B0B7: 83              ADD     A,E                 
B0B8: 64              LD      H,H                 
B0B9: FF              RST     0X38                
B0BA: 15              DEC     D                   
B0BB: A4              AND     H                   
B0BC: 85              ADD     A,L                 
B0BD: B7              OR      A                   
B0BE: A1              AND     C                   
B0BF: BA              CP      D                   
B0C0: 65              LD      H,L                 
B0C1: 0D              DEC     C                   
B0C2: 63              LD      H,E                 
B0C3: 0E 04           LD      C,$04               
B0C5: 0A              LD      A,(BC)              
B0C6: 3A 0A 42        LD      A,($420A)           
B0C9: 0E 5B           LD      C,$5B               
B0CB: 0D              DEC     C                   
B0CC: 28 09           JR      Z,$B0D7             ; {}
B0CE: 24              INC     H                   
B0CF: 1A              LD      A,(DE)              
B0D0: 14              INC     D                   
B0D1: 2E 40           LD      L,$40               
B0D3: 04              INC     B                   
B0D4: 1A              LD      A,(DE)              
B0D5: EB              EX      DE,HL               
B0D6: 99              SBC     C                   
B0D7: 67              LD      H,A                 
B0D8: 98              SBC     B                   
B0D9: 16 58           LD      D,$58               
B0DB: C4 9C 58        CALL    NZ,$589C            
B0DE: 5E              LD      E,(HL)              
B0DF: BE              CP      (HL)                
B0E0: 7A              LD      A,D                 
B0E1: 9E              SBC     (HL)                
B0E2: 61              LD      H,C                 
B0E3: 0B              DEC     BC                  
B0E4: EE 0B           XOR     $0B                 
B0E6: C0              RET     NZ                  
B0E7: 06 9A           LD      B,$9A               
B0E9: 49              LD      C,C                 
B0EA: 16 97           LD      D,$97               
B0EC: 54              LD      D,H                 
B0ED: AB              XOR     E                   
B0EE: 57              LD      D,A                 
B0EF: 0E 04           LD      C,$04               
B0F1: 14              INC     D                   
B0F2: 2E 20           LD      L,$20               
B0F4: A6              AND     (HL)                
B0F5: 0D              DEC     C                   
B0F6: 1C              INC     E                   
B0F7: 09              ADD     HL,BC               
B0F8: 24              INC     H                   
B0F9: 04              INC     B                   
B0FA: 18 C7           JR      $B0C3               ; {}
B0FC: DE 96           SBC     $96                 
B0FE: AF              XOR     A                   
B0FF: 3E A0           LD      A,$A0               
B101: D5              PUSH    DE                  
B102: 15              DEC     D                   
B103: 89              ADC     A,C                 
B104: 17              RLA                         
B105: D5              PUSH    DE                  
B106: 9C              SBC     H                   
B107: 8E              ADC     A,(HL)              
B108: 91              SUB     C                   
B109: 08              EX      AF,AF'              
B10A: 8A              ADC     A,D                 
B10B: A3              AND     E                   
B10C: A0              AND     B                   
B10D: 5F              LD      E,A                 
B10E: BE              CP      (HL)                
B10F: F9              LD      SP,HL               
B110: 15              DEC     D                   
B111: 1B              DEC     DE                  
B112: 51              LD      D,C                 
B113: 0D              DEC     C                   
B114: 11 A9 04        LD      DE,$04A9            
B117: 0E 77           LD      C,$77               
B119: 5B              LD      E,E                 
B11A: 05              DEC     B                   
B11B: B9              CP      C                   
B11C: 15              DEC     D                   
B11D: BC              CP      H                   
B11E: 2F              CPL                         
B11F: 60              LD      H,B                 
B120: 89              ADC     A,C                 
B121: 17              RLA                         
B122: 01 18 6F        LD      BC,$6F18            
B125: B2              OR      D                   
B126: BB              CP      E                   
B127: 23              INC     HL                  
B128: 0D              DEC     C                   
B129: 21 0E 04        LD      HL,$040E            
B12C: 0A              LD      A,(BC)              
B12D: 10 0A           DJNZ    $B139               ; {}
B12F: 0B              DEC     BC                  
B130: 04              INC     B                   
B131: 19              ADD     HL,DE               
B132: 8D              ADC     A,L                 
B133: 7B              LD      A,E                 
B134: 89              ADC     A,C                 
B135: 17              RLA                         
B136: C6 9C           ADD     $9C                 
B138: 35              DEC     (HL)                
B139: 49              LD      C,C                 
B13A: 89              ADC     A,C                 
B13B: 17              RLA                         
B13C: 57              LD      D,A                 
B13D: 17              RLA                         
B13E: 4F              LD      C,A                 
B13F: 5E              LD      E,(HL)              
B140: DA C3 B8        JP      C,$B8C3             
B143: 16 90           LD      D,$90               
B145: 14              INC     D                   
B146: 82              ADD     A,D                 
B147: DF              RST     0X18                
B148: 91              SUB     C                   
B149: 7A              LD      A,D                 
B14A: 2E BC           LD      L,$BC               
B14C: 07              RLCA                        
B14D: 0D              DEC     C                   
B14E: 05              DEC     B                   
B14F: 0A              LD      A,(BC)              
B150: 57              LD      D,A                 
B151: 09              ADD     HL,BC               
B152: 28 10           JR      Z,$B164             ; {}
B154: BD              CP      L                   
B155: 42              LD      B,D                 
B156: 1F              RRA                         
B157: 40              LD      B,B                 
B158: 56              LD      D,(HL)              
B159: 45              LD      B,L                 
B15A: EF              RST     0X28                
B15B: 74              LD      (HL),H              
B15C: 48              LD      C,B                 
B15D: 5E              LD      E,(HL)              
B15E: 46              LD      B,(HL)              
B15F: A0              AND     B                   
B160: 7B              LD      A,E                 
B161: 17              RLA                         
B162: F3              DI                          
B163: 8C              ADC     A,H                 
B164: 1B              DEC     DE                  
B165: B8              CP      B                   
B166: 0B              DEC     BC                  
B167: 6D              LD      L,L                 
B168: E4 14 96        CALL    PO,$9614            ; {}
B16B: 5F              LD      E,A                 
B16C: 2F              CPL                         
B16D: C6 FB           ADD     $FB                 
B16F: 17              RLA                         
B170: 53              LD      D,E                 
B171: BE              CP      (HL)                
B172: DC B0 A3        CALL    C,$A3B0             ; {}
B175: A0              AND     B                   
B176: 1B              DEC     DE                  
B177: B8              CP      B                   
B178: 13              INC     DE                  
B179: B3              OR      E                   
B17A: BB              CP      E                   
B17B: 54              LD      D,H                 
B17C: CB D2           SET     2,D                 
B17E: 8E              ADC     A,(HL)              
B17F: 48              LD      C,B                 
B180: 5E              LD      E,(HL)              
B181: 17              RLA                         
B182: CF              RST     0X08                
B183: 49              LD      C,C                 
B184: 10 B2           DJNZ    $B138               ; {}
B186: D6 6A           SUB     $6A                 
B188: 36 60           LD      (HL),$60            
B18A: 15              DEC     D                   
B18B: 71              LD      (HL),C              
B18C: 50              LD      D,B                 
B18D: BD              CP      L                   
B18E: 0B              DEC     BC                  
B18F: 5C              LD      E,H                 
B190: 68              LD      L,B                 
B191: 4D              LD      C,L                 
B192: AF              XOR     A                   
B193: A0              AND     B                   
B194: 51              LD      D,C                 
B195: 18 DB           JR      $B172               ; {}
B197: C7              RST     0X00                
B198: BE              CP      (HL)                
B199: 26 04           LD      H,$04               
B19B: 24              INC     H                   
B19C: 48              LD      C,B                 
B19D: 45              LD      B,L                 
B19E: AD              XOR     L                   
B19F: A0              AND     B                   
B1A0: 48              LD      C,B                 
B1A1: 5E              LD      E,(HL)              
B1A2: 2E 79           LD      L,$79               
B1A4: 12              LD      (DE),A              
B1A5: 58              LD      E,B                 
B1A6: 78              LD      A,B                 
B1A7: B1              OR      C                   
B1A8: 9E              SBC     (HL)                
B1A9: 61              LD      H,C                 
B1AA: DB B5           IN      A,($B5)             
B1AC: 1B              DEC     DE                  
B1AD: A1              AND     C                   
B1AE: 79              LD      A,C                 
B1AF: 68              LD      L,B                 
B1B0: 49              LD      C,C                 
B1B1: 90              SUB     B                   
B1B2: 50              LD      D,B                 
B1B3: 9F              SBC     A                   
B1B4: D6 6A           SUB     $6A                 
B1B6: 56              LD      D,(HL)              
B1B7: 72              LD      (HL),D              
B1B8: 03              INC     BC                  
B1B9: 15              DEC     D                   
B1BA: 65              LD      H,L                 
B1BB: B1              OR      C                   
B1BC: 91              SUB     C                   
B1BD: BE              CP      (HL)                
B1BE: 1B              DEC     DE                  
B1BF: 9C              SBC     H                   
B1C0: BF              CP      A                   
B1C1: 10 0E           DJNZ    $B1D1               ; {}
B1C3: 0E 36           LD      C,$36               
B1C5: 0D              DEC     C                   
B1C6: 0B              DEC     BC                  
B1C7: AA              XOR     D                   
B1C8: 04              INC     B                   
B1C9: 07              RLCA                        
B1CA: 4B              LD      C,E                 
B1CB: 7B              LD      A,E                 
B1CC: C9              RET                         
B1CD: 54              LD      D,H                 
B1CE: A6              AND     (HL)                
B1CF: B7              OR      A                   
B1D0: 2E 0C           LD      L,$0C               
B1D2: C0              RET     NZ                  
B1D3: 06 0D           LD      B,$0D               
B1D5: 04              INC     B                   
B1D6: 08              EX      AF,AF'              
B1D7: 00              NOP                         
B1D8: 09              ADD     HL,BC               
B1D9: 00              NOP                         
B1DA: C1              POP     BC                  
B1DB: 18 0D           JR      $B1EA               ; {}
B1DD: 16 04           LD      D,$04               
B1DF: 0A              LD      A,(BC)              
B1E0: C7              RST     0X00                
B1E1: DE D3           SBC     $D3                 
B1E3: 14              INC     D                   
B1E4: E6 96           AND     $96                 
B1E6: 2F              CPL                         
B1E7: 17              RLA                         
B1E8: DA 46 AA        JP      C,$AA46             ; {}
B1EB: 04              INC     B                   
B1EC: 07              RLCA                        
B1ED: 79              LD      A,C                 
B1EE: 68              LD      L,B                 
B1EF: 4A              LD      C,D                 
B1F0: 90              SUB     B                   
B1F1: 2F              CPL                         
B1F2: 62              LD      H,D                 
B1F3: 2E C2           LD      L,$C2               
B1F5: 10 0D           DJNZ    $B204               ; {}
B1F7: 0E 04           LD      C,$04               
B1F9: 0A              LD      A,(BC)              
B1FA: C7              RST     0X00                
B1FB: DE D3           SBC     $D3                 
B1FD: 14              INC     D                   
B1FE: E6 96           AND     $96                 
B200: BF              CP      A                   
B201: 14              INC     D                   
B202: 37              SCF                         
B203: 5A              LD      E,D                 
B204: A8              XOR     B                   
B205: 8B              ADC     A,E                 
B206: C3 04 14        JP      $1404               
B209: 03              INC     BC                  
B20A: 01 80 C4        LD      BC,$C480            
B20D: 1C              INC     E                   
B20E: 0E 1A           LD      C,$1A               
B210: 0A              LD      A,(BC)              
B211: 11 0A 3A        LD      DE,$3A0A            
B214: 0A              LD      A,(BC)              
B215: 05              DEC     B                   
B216: 0A              LD      A,(BC)              
B217: 43              LD      B,E                 
B218: 0A              LD      A,(BC)              
B219: 09              ADD     HL,BC               
B21A: 0A              LD      A,(BC)              
B21B: 27              DAA                         
B21C: 0A              LD      A,(BC)              
B21D: 2D              DEC     L                   
B21E: 0A              LD      A,(BC)              
B21F: 12              LD      (DE),A              
B220: 0A              LD      A,(BC)              
B221: 18 0A           JR      $B22D               ; {}
B223: 0F              RRCA                        
B224: 0A              LD      A,(BC)              
B225: 4B              LD      C,E                 
B226: 0A              LD      A,(BC)              
B227: 4D              LD      C,L                 
B228: 0A              LD      A,(BC)              
B229: 40              LD      B,B                 
B22A: C5              PUSH    BC                  
B22B: 28 0B           JR      Z,$B238             ; {}
B22D: 26 0A           LD      H,$0A               
B22F: 36 0F           LD      (HL),$0F            
B231: 0D              DEC     C                   
B232: 0D              DEC     C                   
B233: 04              INC     B                   
B234: 09              ADD     HL,BC               
B235: C7              RST     0X00                
B236: DE AF           SBC     $AF                 
B238: 23              INC     HL                  
B239: 99              SBC     C                   
B23A: 16 CB           LD      D,$CB               
B23C: CE 4E           ADC     $4E                 
B23E: A8              XOR     B                   
B23F: 8B              ADC     A,E                 
B240: 37              SCF                         
B241: 12              LD      (DE),A              
B242: 0D              DEC     C                   
B243: 10 04           DJNZ    $B249               ; {}
B245: 0C              INC     C                   
B246: C7              RST     0X00                
B247: DE AF           SBC     $AF                 
B249: 23              INC     HL                  
B24A: 99              SBC     C                   
B24B: 16 D1           LD      D,$D1               
B24D: CE 73           ADC     $73                 
B24F: C6 C3           ADD     $C3                 
B251: 9E              SBC     (HL)                
B252: A8              XOR     B                   
B253: 8B              ADC     A,E                 
B254: C6 1E           ADD     $1E                 
B256: 0D              DEC     C                   
B257: 1C              INC     E                   
B258: 04              INC     B                   
B259: 18 18           JR      $B273               ; {}
B25B: B7              OR      A                   
B25C: 46              LD      B,(HL)              
B25D: 5E              LD      E,(HL)              
B25E: 5D              LD      E,L                 
B25F: 7B              LD      A,E                 
B260: D5              PUSH    DE                  
B261: 15              DEC     D                   
B262: D0              RET     NC                  
B263: 15              DEC     D                   
B264: FA 17 DA        JP      M,$DA17             
B267: 78              LD      A,B                 
B268: 0C              INC     C                   
B269: 15              DEC     D                   
B26A: CF              RST     0X08                
B26B: 7B              LD      A,E                 
B26C: B9              CP      C                   
B26D: 13              INC     DE                  
B26E: D7              RST     0X10                
B26F: E8              RET     PE                  
B270: C3 12 3B        JP      $3B12               
B273: 25              DEC     H                   
B274: C8              RET     Z                   
B275: 81              ADD     A,C                 
B276: 80              ADD     A,B                 
B277: 0E 81           LD      C,$81               
B279: 7D              LD      A,L                 
B27A: 0D              DEC     C                   
B27B: 80              ADD     A,B                 
B27C: 8C              ADC     A,H                 
B27D: 03              INC     BC                  
B27E: 01 91 04        LD      BC,$0491            
B281: 80              ADD     A,B                 
B282: 82              ADD     A,D                 
B283: AE              XOR     (HL)                
B284: D0              RET     NC                  
B285: 73              LD      (HL),E              
B286: 8F              ADC     A,A                 
B287: 73              LD      (HL),E              
B288: 7B              LD      A,E                 
B289: A7              AND     A                   
B28A: B7              OR      A                   
B28B: 4B              LD      C,E                 
B28C: 94              SUB     H                   
B28D: C7              RST     0X00                
B28E: DE 63           SBC     $63                 
B290: 16 DB           LD      D,$DB               
B292: 59              LD      E,C                 
B293: 73              LD      (HL),E              
B294: 7B              LD      A,E                 
B295: E4 46 E5        CALL    PO,$E546            
B298: A0              AND     B                   
B299: 82              ADD     A,D                 
B29A: 17              RLA                         
B29B: 46              LD      B,(HL)              
B29C: 5E              LD      E,(HL)              
B29D: 57              LD      D,A                 
B29E: 62              LD      H,D                 
B29F: B1              OR      C                   
B2A0: B3              OR      E                   
B2A1: A9              XOR     C                   
B2A2: 15              DEC     D                   
B2A3: B8              CP      B                   
B2A4: D0              RET     NC                  
B2A5: 46              LD      B,(HL)              
B2A6: 62              LD      H,D                 
B2A7: FA 17 83        JP      M,$8317             ; {}
B2AA: 61              LD      H,C                 
B2AB: 5B              LD      E,E                 
B2AC: BE              CP      (HL)                
B2AD: 10 BC           DJNZ    $B26B               ; {}
B2AF: 66              LD      H,(HL)              
B2B0: 49              LD      C,C                 
B2B1: 45              LD      B,L                 
B2B2: DB 63           IN      A,($63)             
B2B4: B1              OR      C                   
B2B5: 74              LD      (HL),H              
B2B6: C0              RET     NZ                  
B2B7: 4B              LD      C,E                 
B2B8: 5E              LD      E,(HL)              
B2B9: 96              SUB     (HL)                
B2BA: 96              SUB     (HL)                
B2BB: DB 72           IN      A,($72)             
B2BD: F5              PUSH    AF                  
B2BE: 59              LD      E,C                 
B2BF: 3E 62           LD      A,$62               
B2C1: 96              SUB     (HL)                
B2C2: 14              INC     D                   
B2C3: 45              LD      B,L                 
B2C4: BD              CP      L                   
B2C5: A6              AND     (HL)                
B2C6: 85              ADD     A,L                 
B2C7: 51              LD      D,C                 
B2C8: 18 B3           JR      $B27D               ; {}
B2CA: C7              RST     0X00                
B2CB: C7              RST     0X00                
B2CC: DE F7           SBC     $F7                 
B2CE: 17              RLA                         
B2CF: 5B              LD      E,E                 
B2D0: B1              OR      C                   
B2D1: 7B              LD      A,E                 
B2D2: A6              AND     (HL)                
B2D3: 40              LD      B,B                 
B2D4: B9              CP      C                   
B2D5: F1              POP     AF                  
B2D6: 5F              LD      E,A                 
B2D7: DF              RST     0X18                
B2D8: 16 DB           LD      D,$DB               
B2DA: B1              OR      C                   
B2DB: 0B              DEC     BC                  
B2DC: A7              AND     A                   
B2DD: 3F              CCF                         
B2DE: B9              CP      C                   
B2DF: 43              LD      B,E                 
B2E0: 5E              LD      E,(HL)              
B2E1: C3 9A 86        JP      $869A               ; {}
B2E4: 5B              LD      E,E                 
B2E5: 45              LD      B,L                 
B2E6: 5E              LD      E,(HL)              
B2E7: 2E A1           LD      L,$A1               
B2E9: 0A              LD      A,(BC)              
B2EA: 58              LD      E,B                 
B2EB: CF              RST     0X08                
B2EC: 49              LD      C,C                 
B2ED: 53              LD      D,E                 
B2EE: 17              RLA                         
B2EF: 66              LD      H,(HL)              
B2F0: CA 51 18        JP      Z,$1851             
B2F3: DB C7           IN      A,($C7)             
B2F5: F6 4F           OR      $4F                 
B2F7: 0B              DEC     BC                  
B2F8: EE 0B           XOR     $0B                 
B2FA: BC              CP      H                   
B2FB: D6 B5           SUB     $B5                 
B2FD: 2B              DEC     HL                  
B2FE: A0              AND     B                   
B2FF: 56              LD      D,(HL)              
B300: 8B              ADC     A,E                 
B301: 50              LD      D,B                 
B302: 5E              LD      E,(HL)              
B303: 8F              ADC     A,A                 
B304: A1              AND     C                   
B305: 1C              INC     E                   
B306: 01 1D 64        LD      BC,$641D            
B309: 0D              DEC     C                   
B30A: 80              ADD     A,B                 
B30B: E9              JP      (HL)                
B30C: 03              INC     BC                  
B30D: 00              NOP                         
B30E: 71              LD      (HL),C              
B30F: 04              INC     B                   
B310: 80              ADD     A,B                 
B311: E2 C7 DE        JP      PO,$DEC7            
B314: 9B              SBC     E                   
B315: 15              DEC     D                   
B316: 5B              LD      E,E                 
B317: CA 86 91        JP      Z,$9186             ; {}
B31A: 4B              LD      C,E                 
B31B: 5E              LD      E,(HL)              
B31C: 04              INC     B                   
B31D: BC              CP      H                   
B31E: DD 46 89        LD      B,(IX+$89)          
B321: 17              RLA                         
B322: 89              ADC     A,C                 
B323: 17              RLA                         
B324: 01 D2 82        LD      BC,$82D2            
B327: 17              RLA                         
B328: 56              LD      D,(HL)              
B329: 5E              LD      E,(HL)              
B32A: 80              ADD     A,B                 
B32B: A1              AND     C                   
B32C: C8              RET     Z                   
B32D: B5              OR      L                   
B32E: C5              PUSH    BC                  
B32F: 9F              SBC     A                   
B330: 9B              SBC     E                   
B331: 15              DEC     D                   
B332: 5B              LD      E,E                 
B333: CA 76 B1        JP      Z,$B176             ; {}
B336: 38 C6           JR      C,$B2FE             ; {}
B338: F3              DI                          
B339: 5F              LD      E,A                 
B33A: 8E              ADC     A,(HL)              
B33B: 48              LD      C,B                 
B33C: 82              ADD     A,D                 
B33D: 17              RLA                         
B33E: 3B              DEC     SP                  
B33F: 63              LD      H,E                 
B340: 1F              RRA                         
B341: 54              LD      D,H                 
B342: 23              INC     HL                  
B343: 62              LD      H,D                 
B344: C7              RST     0X00                
B345: DE 95           SBC     $95                 
B347: AF              XOR     A                   
B348: D5              PUSH    DE                  
B349: C3 65 62        JP      $6265               ; {}
B34C: 43              LD      B,E                 
B34D: F4 B3 14        CALL    P,$14B3             
B350: C5              PUSH    BC                  
B351: 6A              LD      L,D                 
B352: 3F              CCF                         
B353: 61              LD      H,C                 
B354: 6B              LD      L,E                 
B355: 4F              LD      C,A                 
B356: 91              SUB     C                   
B357: BE              CP      (HL)                
B358: 8B              ADC     A,E                 
B359: 96              SUB     (HL)                
B35A: D2 B5 72        JP      NC,$72B5            ; {}
B35D: B1              OR      C                   
B35E: 2F              CPL                         
B35F: 49              LD      C,C                 
B360: 03              INC     BC                  
B361: 58              LD      E,B                 
B362: 33              INC     SP                  
B363: 98              SBC     B                   
B364: 5F              LD      E,A                 
B365: BE              CP      (HL)                
B366: 4F              LD      C,A                 
B367: 15              DEC     D                   
B368: 03              INC     BC                  
B369: BA              CP      D                   
B36A: 16 CB           LD      D,$CB               
B36C: 35              DEC     (HL)                
B36D: 79              LD      A,C                 
B36E: 3B              DEC     SP                  
B36F: 16 F3           LD      D,$F3               
B371: B9              CP      C                   
B372: 46              LD      B,(HL)              
B373: 48              LD      C,B                 
B374: 93              SUB     E                   
B375: 16 2E           LD      D,$2E               
B377: 6D              LD      L,L                 
B378: 56              LD      D,(HL)              
B379: F4 DB 72        CALL    P,$72DB             ; {}
B37C: 94              SUB     H                   
B37D: 5F              LD      E,A                 
B37E: 53              LD      D,E                 
B37F: BE              CP      (HL)                
B380: 55              LD      D,L                 
B381: 72              LD      (HL),D              
B382: AF              XOR     A                   
B383: 14              INC     D                   
B384: 83              ADD     A,E                 
B385: 61              LD      H,C                 
B386: 18 B7           JR      $B33F               ; {}
B388: F1              POP     AF                  
B389: 5F              LD      E,A                 
B38A: 8A              ADC     A,D                 
B38B: 14              INC     D                   
B38C: 19              ADD     HL,DE               
B38D: EE 46           XOR     $46                 
B38F: 61              LD      H,C                 
B390: 10 EE           DJNZ    $B380               ; {}
B392: 6B              LD      L,E                 
B393: A1              AND     C                   
B394: C7              RST     0X00                
B395: DE 77           SBC     $77                 
B397: 16 F3           LD      D,$F3               
B399: B9              CP      C                   
B39A: 76              HALT                        
B39B: B1              OR      C                   
B39C: 38 C6           JR      C,$B364             ; {}
B39E: 89              ADC     A,C                 
B39F: 17              RLA                         
B3A0: 82              ADD     A,D                 
B3A1: 17              RLA                         
B3A2: 46              LD      B,(HL)              
B3A3: 5E              LD      E,(HL)              
B3A4: BE              CP      (HL)                
B3A5: 9F              SBC     A                   
B3A6: EF              RST     0X28                
B3A7: B3              OR      E                   
B3A8: D1              POP     DE                  
B3A9: B5              OR      L                   
B3AA: 9B              SBC     E                   
B3AB: 64              LD      H,H                 
B3AC: 34              INC     (HL)                
B3AD: A1              AND     C                   
B3AE: 99              SBC     C                   
B3AF: 16 A3           LD      D,$A3               
B3B1: B2              OR      D                   
B3B2: 04              INC     B                   
B3B3: 8A              ADC     A,D                 
B3B4: B3              OR      E                   
B3B5: A0              AND     B                   
B3B6: AB              XOR     E                   
B3B7: 98              SBC     B                   
B3B8: 88              ADC     A,B                 
B3B9: 8C              ADC     A,H                 
B3BA: DB 63           IN      A,($63)             
B3BC: F4 A4 52        CALL    P,$52A4             
B3BF: 72              LD      (HL),D              
B3C0: 33              INC     SP                  
B3C1: BB              CP      E                   
B3C2: C7              RST     0X00                
B3C3: DE 82           SBC     $82                 
B3C5: 17              RLA                         
B3C6: 95              SUB     L                   
B3C7: 7A              LD      A,D                 
B3C8: 15              DEC     D                   
B3C9: EE E7           XOR     $E7                 
B3CB: 9F              SBC     A                   
B3CC: 5B              LD      E,E                 
B3CD: 59              LD      E,C                 
B3CE: 90              SUB     B                   
B3CF: 14              INC     D                   
B3D0: 02              LD      (BC),A              
B3D1: A1              AND     C                   
B3D2: 23              INC     HL                  
B3D3: 62              LD      H,D                 
B3D4: 59              LD      E,C                 
B3D5: C4 FB 17        CALL    NZ,$17FB            
B3D8: F3              DI                          
B3D9: 8C              ADC     A,H                 
B3DA: 3F              CCF                         
B3DB: 55              LD      D,L                 
B3DC: 43              LD      B,E                 
B3DD: 5E              LD      E,(HL)              
B3DE: 33              INC     SP                  
B3DF: 98              SBC     B                   
B3E0: C7              RST     0X00                
B3E1: DE D3           SBC     $D3                 
B3E3: 14              INC     D                   
B3E4: 8B              ADC     A,E                 
B3E5: 96              SUB     (HL)                
B3E6: 0F              RRCA                        
B3E7: 9B              SBC     E                   
B3E8: 03              INC     BC                  
B3E9: BA              CP      D                   
B3EA: 16 6C           LD      D,$6C               
B3EC: 51              LD      D,C                 
B3ED: 5E              LD      E,(HL)              
B3EE: 17              RLA                         
B3EF: 98              SBC     B                   
B3F0: 71              LD      (HL),C              
B3F1: 16 7F           LD      D,$7F               
B3F3: B1              OR      C                   
B3F4: 24              INC     H                   
B3F5: 14              INC     D                   
B3F6: 0C              INC     C                   
B3F7: C9              RET                         
B3F8: 23              INC     HL                  
B3F9: 0D              DEC     C                   
B3FA: 21 1F 0C        LD      HL,$0C1F            
B3FD: C7              RST     0X00                
B3FE: DE 9B           SBC     $9B                 
B400: 15              DEC     D                   
B401: 5B              LD      E,E                 
B402: CA 3F 55        JP      Z,$553F             
B405: FF              RST     0X38                
B406: A5              AND     L                   
B407: E6 BD           AND     $BD                 
B409: 26 1F           LD      H,$1F               
B40B: 10 F4           DJNZ    $B401               ; {}
B40D: A4              AND     H                   
B40E: B0              OR      B                   
B40F: 53              LD      D,E                 
B410: 11 BC 9B        LD      DE,$9BBC            
B413: 64              LD      H,H                 
B414: 34              INC     (HL)                
B415: A1              AND     C                   
B416: 6B              LD      L,E                 
B417: 16 DB           LD      D,$DB               
B419: B9              CP      C                   
B41A: 27              DAA                         
B41B: A0              AND     B                   
B41C: CA 50 0D        JP      Z,$0D50             
B41F: 4E              LD      C,(HL)              
B420: 25              DEC     H                   
B421: 25              DEC     H                   
B422: 1F              RRA                         
B423: 46              LD      B,(HL)              
B424: 26 BA           LD      H,$BA               
B426: F0              RET     P                   
B427: 59              LD      E,C                 
B428: 1E 8F           LD      E,$8F               
B42A: 5C              LD      E,H                 
B42B: 15              DEC     D                   
B42C: DB 9F           IN      A,($9F)             
B42E: A7              AND     A                   
B42F: B7              OR      A                   
B430: D0              RET     NC                  
B431: 92              SUB     D                   
B432: D3 6D           OUT     ($6D),A             
B434: 99              SBC     C                   
B435: 16 1F           LD      D,$1F               
B437: D1              POP     DE                  
B438: 7E              LD      A,(HL)              
B439: B1              OR      C                   
B43A: 90              SUB     B                   
B43B: 14              INC     D                   
B43C: 30 15           JR      NC,$B453            ; {}
B43E: 31 62 44        LD      SP,$4462            
B441: DB 8F           IN      A,($8F)             
B443: 5F              LD      E,A                 
B444: 30 15           JR      NC,$B45B            ; {}
B446: 6E              LD      L,(HL)              
B447: CA 5F A0        JP      Z,$A05F             ; {}
B44A: DB B5           IN      A,($B5)             
B44C: 19              ADD     HL,DE               
B44D: A1              AND     C                   
B44E: 51              LD      D,C                 
B44F: 18 23           JR      $B474               ; {}
B451: C6 74           ADD     $74                 
B453: CA 4E DB        JP      Z,$DB4E             
B456: 4F              LD      C,A                 
B457: 79              LD      A,C                 
B458: D5              PUSH    DE                  
B459: 15              DEC     D                   
B45A: EF              RST     0X28                
B45B: 16 B7           LD      D,$B7               
B45D: B1              OR      C                   
B45E: 08              EX      AF,AF'              
B45F: 58              LD      E,B                 
B460: FF              RST     0X38                
B461: B2              OR      D                   
B462: 51              LD      D,C                 
B463: 18 23           JR      $B488               ; {}
B465: C6 F6           ADD     $F6                 
B467: 4E              LD      C,(HL)              
B468: EB              EX      DE,HL               
B469: DA 1C 01        JP      C,$011C             
B46C: 1D              DEC     E                   
B46D: 64              LD      H,H                 
B46E: 00              NOP                         
B46F: 00              NOP                         
B470: 00              NOP                         
B471: 00              NOP                         
B472: 00              NOP                         
B473: 00              NOP                         
B474: 00              NOP                         
B475: 00              NOP                         
B476: 01 00 01        LD      BC,$0100            
B479: 00              NOP                         
B47A: 00              NOP                         
B47B: 00              NOP                         
B47C: 00              NOP                         
B47D: 00              NOP                         
B47E: 00              NOP                         
B47F: 00              NOP                         
B480: A3              AND     E                   
B481: 22 63 23        LD      ($2363),HL          
B484: 63              LD      H,E                 
B485: A3              AND     E                   
B486: 62              LD      H,D                 
B487: 22 63 23        LD      ($2363),HL          
B48A: A7              AND     A                   
B48B: E3              EX      (SP),HL             
B48C: 63              LD      H,E                 
B48D: E3              EX      (SP),HL             
B48E: 67              LD      H,A                 
B48F: E3              EX      (SP),HL             
B490: 23              INC     HL                  
B491: E7              RST     0X20                
B492: 67              LD      H,A                 
B493: 22 22 03        LD      ($0322),HL          
B496: 22 22 E7        LD      ($E722),HL          
B499: E2 E7 63        JP      PO,$63E7            ; {}
B49C: E7              RST     0X20                
B49D: E6 E7           AND     $E7                 
B49F: E7              RST     0X20                
B4A0: 62              LD      H,D                 
B4A1: E2 62 63        JP      PO,$6362            ; {}
B4A4: E7              RST     0X20                
B4A5: E7              RST     0X20                
B4A6: E6 C7           AND     $C7                 
B4A8: C7              RST     0X00                
B4A9: C7              RST     0X00                
B4AA: C3 02 02        JP      $0202               
B4AD: 02              LD      (BC),A              
B4AE: 02              LD      (BC),A              
B4AF: 02              LD      (BC),A              
B4B0: C2 C2 42        JP      NZ,$42C2            
B4B3: 62              LD      H,D                 
B4B4: 23              INC     HL                  
B4B5: 02              LD      (BC),A              
B4B6: 23              INC     HL                  
B4B7: 02              LD      (BC),A              
B4B8: 02              LD      (BC),A              
B4B9: 02              LD      (BC),A              
B4BA: 03              INC     BC                  
B4BB: 22 23 02        LD      ($0223),HL          
B4BE: 23              INC     HL                  
B4BF: 02              LD      (BC),A              
B4C0: 02              LD      (BC),A              
B4C1: 02              LD      (BC),A              
B4C2: 02              LD      (BC),A              
B4C3: 02              LD      (BC),A              
B4C4: 02              LD      (BC),A              
B4C5: 02              LD      (BC),A              
B4C6: 02              LD      (BC),A              
B4C7: 02              LD      (BC),A              
B4C8: 02              LD      (BC),A              
B4C9: 02              LD      (BC),A              
B4CA: 02              LD      (BC),A              
B4CB: 02              LD      (BC),A              
B4CC: 02              LD      (BC),A              
B4CD: 02              LD      (BC),A              
B4CE: 02              LD      (BC),A              
B4CF: 02              LD      (BC),A              
B4D0: 02              LD      (BC),A              
B4D1: 02              LD      (BC),A              
B4D2: 02              LD      (BC),A              
B4D3: 02              LD      (BC),A              
B4D4: 02              LD      (BC),A              
B4D5: 02              LD      (BC),A              
B4D6: 02              LD      (BC),A              
B4D7: 02              LD      (BC),A              
B4D8: 02              LD      (BC),A              
B4D9: 02              LD      (BC),A              
B4DA: 02              LD      (BC),A              
B4DB: 02              LD      (BC),A              
B4DC: 02              LD      (BC),A              
B4DD: 02              LD      (BC),A              
B4DE: 02              LD      (BC),A              
B4DF: 02              LD      (BC),A              
B4E0: 02              LD      (BC),A              
B4E1: 02              LD      (BC),A              
B4E2: 02              LD      (BC),A              
B4E3: 02              LD      (BC),A              
B4E4: 02              LD      (BC),A              
B4E5: 02              LD      (BC),A              
B4E6: 02              LD      (BC),A              
B4E7: 02              LD      (BC),A              
B4E8: 02              LD      (BC),A              
B4E9: 02              LD      (BC),A              
B4EA: 02              LD      (BC),A              
B4EB: 02              LD      (BC),A              
B4EC: 02              LD      (BC),A              
B4ED: 02              LD      (BC),A              
B4EE: 02              LD      (BC),A              
B4EF: 02              LD      (BC),A              
B4F0: 02              LD      (BC),A              
B4F1: 02              LD      (BC),A              
B4F2: 02              LD      (BC),A              
B4F3: 02              LD      (BC),A              
B4F4: 02              LD      (BC),A              
B4F5: 02              LD      (BC),A              
B4F6: 02              LD      (BC),A              
B4F7: 02              LD      (BC),A              
B4F8: 02              LD      (BC),A              
B4F9: 02              LD      (BC),A              
B4FA: 00              NOP                         
B4FB: 02              LD      (BC),A              
B4FC: 02              LD      (BC),A              
B4FD: 02              LD      (BC),A              
B4FE: 02              LD      (BC),A              
B4FF: 02              LD      (BC),A              
B500: B3              OR      E                   
B501: F2 FF FF        JP      P,$FFFF             
B504: FF              RST     0X38                
B505: FF              RST     0X38                
B506: 73              LD      (HL),E              
B507: 62              LD      H,D                 
B508: FF              RST     0X38                
B509: FF              RST     0X38                
B50A: BF              CP      A                   
B50B: FF              RST     0X38                
B50C: FB              EI                          
B50D: FF              RST     0X38                
B50E: FF              RST     0X38                
B50F: FF              RST     0X38                
B510: FB              EI                          
B511: FF              RST     0X38                
B512: FF              RST     0X38                
B513: FF              RST     0X38                
B514: DF              RST     0X18                
B515: FB              EI                          
B516: DE F2           SBC     $F2                 
B518: FF              RST     0X38                
B519: FE FF           CP      $FF                 
B51B: FF              RST     0X38                
B51C: FF              RST     0X38                
B51D: FF              RST     0X38                
B51E: FF              RST     0X38                
B51F: FF              RST     0X38                
B520: FC FF FF        CALL    M,$FFFF             
B523: FF              RST     0X38                
B524: FF              RST     0X38                
B525: FF              RST     0X38                
B526: FE DF           CP      $DF                 
B528: DF              RST     0X18                
B529: DF              RST     0X18                
B52A: DF              RST     0X18                
B52B: DE DE           SBC     $DE                 
B52D: DE DE           SBC     $DE                 
B52F: DE DF           SBC     $DF                 
B531: DF              RST     0X18                
B532: 5F              LD      E,A                 
B533: 7F              LD      A,A                 
B534: 5F              LD      E,A                 
B535: 5F              LD      E,A                 
B536: 7F              LD      A,A                 
B537: 5F              LD      E,A                 
B538: 4A              LD      C,D                 
B539: 5F              LD      E,A                 
B53A: 5F              LD      E,A                 
B53B: 7F              LD      A,A                 
B53C: FF              RST     0X38                
B53D: DF              RST     0X18                
B53E: FD ; ????
B53F: DF              RST     0X18                
B540: 82              ADD     A,D                 
B541: 00              NOP                         
B542: 00              NOP                         
B543: 00              NOP                         
B544: 00              NOP                         
B545: 00              NOP                         
B546: 00              NOP                         
B547: 00              NOP                         
B548: 00              NOP                         
B549: 00              NOP                         
B54A: 00              NOP                         
B54B: 00              NOP                         
B54C: 00              NOP                         
B54D: 00              NOP                         
B54E: 00              NOP                         
B54F: 00              NOP                         
B550: 00              NOP                         
B551: 00              NOP                         
B552: 00              NOP                         
B553: 00              NOP                         
B554: 00              NOP                         
B555: 00              NOP                         
B556: 00              NOP                         
B557: 00              NOP                         
B558: 00              NOP                         
B559: 00              NOP                         
B55A: 00              NOP                         
B55B: 00              NOP                         
B55C: 00              NOP                         
B55D: 00              NOP                         
B55E: 00              NOP                         
B55F: 00              NOP                         
B560: 00              NOP                         
B561: 00              NOP                         
B562: 00              NOP                         
B563: 00              NOP                         
B564: 00              NOP                         
B565: 00              NOP                         
B566: 00              NOP                         
B567: 00              NOP                         
B568: 00              NOP                         
B569: 00              NOP                         
B56A: 00              NOP                         
B56B: 10 92           DJNZ    $B4FF               ; {}
B56D: 82              ADD     A,D                 
B56E: 80              ADD     A,B                 
B56F: 80              ADD     A,B                 
B570: 80              ADD     A,B                 
B571: 80              ADD     A,B                 
B572: 90              SUB     B                   
B573: 90              SUB     B                   
B574: 80              ADD     A,B                 
B575: 80              ADD     A,B                 
B576: 90              SUB     B                   
B577: 80              ADD     A,B                 
B578: 10 00           DJNZ    $B57A               ; {}
B57A: 00              NOP                         
B57B: 00              NOP                         
B57C: 00              NOP                         
B57D: 00              NOP                         
B57E: 00              NOP                         
B57F: 00              NOP                         
B580: B3              OR      E                   
B581: A2              AND     D                   
B582: B7              OR      A                   
B583: AF              XOR     A                   
B584: AF              XOR     A                   
B585: BF              CP      A                   
B586: 23              INC     HL                  
B587: 22 AF 3F        LD      ($3FAF),HL          
B58A: AF              XOR     A                   
B58B: BF              CP      A                   
B58C: AB              XOR     E                   
B58D: BF              CP      A                   
B58E: BF              CP      A                   
B58F: BF              CP      A                   
B590: A3              AND     E                   
B591: BF              CP      A                   
B592: BF              CP      A                   
B593: 3F              CCF                         
B594: 3F              CCF                         
B595: 93              SUB     E                   
B596: 26 B2           LD      H,$B2               
B598: BF              CP      A                   
B599: BE              CP      (HL)                
B59A: BF              CP      A                   
B59B: 3F              CCF                         
B59C: BF              CP      A                   
B59D: BF              CP      A                   
B59E: BF              CP      A                   
B59F: BF              CP      A                   
B5A0: AC              XOR     H                   
B5A1: BE              CP      (HL)                
B5A2: 3E 3F           LD      A,$3F               
B5A4: BF              CP      A                   
B5A5: BF              CP      A                   
B5A6: BE              CP      (HL)                
B5A7: 9F              SBC     A                   
B5A8: 9F              SBC     A                   
B5A9: 9F              SBC     A                   
B5AA: 9F              SBC     A                   
B5AB: 1E 9E           LD      E,$9E               
B5AD: 0E 96           LD      C,$96               
B5AF: 9E              SBC     (HL)                
B5B0: DF              RST     0X18                
B5B1: 86              ADD     A,(HL)              
B5B2: 0F              RRCA                        
B5B3: 27              DAA                         
B5B4: 27              DAA                         
B5B5: 17              RLA                         
B5B6: 27              DAA                         
B5B7: 17              RLA                         
B5B8: 02              LD      (BC),A              
B5B9: 1F              RRA                         
B5BA: 07              RLCA                        
B5BB: 27              DAA                         
B5BC: 27              DAA                         
B5BD: 9F              SBC     A                   
B5BE: 27              DAA                         
B5BF: 17              RLA                         
B5C0: 02              LD      (BC),A              
B5C1: 00              NOP                         
B5C2: 00              NOP                         
B5C3: 00              NOP                         
B5C4: 00              NOP                         
B5C5: 00              NOP                         
B5C6: 00              NOP                         
B5C7: 00              NOP                         
B5C8: 00              NOP                         
B5C9: 00              NOP                         
B5CA: 02              LD      (BC),A              
B5CB: 00              NOP                         
B5CC: 00              NOP                         
B5CD: 00              NOP                         
B5CE: 00              NOP                         
B5CF: 00              NOP                         
B5D0: 00              NOP                         
B5D1: 00              NOP                         
B5D2: 00              NOP                         
B5D3: 00              NOP                         
B5D4: 00              NOP                         
B5D5: 00              NOP                         
B5D6: 00              NOP                         
B5D7: 00              NOP                         
B5D8: 00              NOP                         
B5D9: 00              NOP                         
B5DA: 00              NOP                         
B5DB: 00              NOP                         
B5DC: 00              NOP                         
B5DD: 00              NOP                         
B5DE: 00              NOP                         
B5DF: 00              NOP                         
B5E0: 00              NOP                         
B5E1: 00              NOP                         
B5E2: 00              NOP                         
B5E3: 00              NOP                         
B5E4: 00              NOP                         
B5E5: 00              NOP                         
B5E6: 02              LD      (BC),A              
B5E7: 00              NOP                         
B5E8: 00              NOP                         
B5E9: 00              NOP                         
B5EA: 00              NOP                         
B5EB: 00              NOP                         
B5EC: 00              NOP                         
B5ED: 00              NOP                         
B5EE: 00              NOP                         
B5EF: 00              NOP                         
B5F0: 00              NOP                         
B5F1: 00              NOP                         
B5F2: 00              NOP                         
B5F3: 00              NOP                         
B5F4: 00              NOP                         
B5F5: 00              NOP                         
B5F6: 00              NOP                         
B5F7: 00              NOP                         
B5F8: 02              LD      (BC),A              
B5F9: 00              NOP                         
B5FA: 00              NOP                         
B5FB: 00              NOP                         
B5FC: 00              NOP                         
B5FD: 00              NOP                         
B5FE: 00              NOP                         
B5FF: 00              NOP                         
B600: B3              OR      E                   
B601: E2 EF EF        JP      PO,$EFEF            
B604: EF              RST     0X28                
B605: EF              RST     0X28                
B606: 63              LD      H,E                 
B607: 62              LD      H,D                 
B608: EF              RST     0X28                
B609: EF              RST     0X28                
B60A: AF              XOR     A                   
B60B: EF              RST     0X28                
B60C: EB              EX      DE,HL               
B60D: EF              RST     0X28                
B60E: EF              RST     0X28                
B60F: EF              RST     0X28                
B610: EB              EX      DE,HL               
B611: EF              RST     0X28                
B612: EF              RST     0X28                
B613: EF              RST     0X28                
B614: EF              RST     0X28                
B615: EB              EX      DE,HL               
B616: EE E2           XOR     $E2                 
B618: EF              RST     0X28                
B619: EE EF           XOR     $EF                 
B61B: EF              RST     0X28                
B61C: EF              RST     0X28                
B61D: EF              RST     0X28                
B61E: EF              RST     0X28                
B61F: EF              RST     0X28                
B620: EC FE 6E        CALL    PE,$6EFE            ; {}
B623: 6F              LD      L,A                 
B624: EF              RST     0X28                
B625: EF              RST     0X28                
B626: FE EF           CP      $EF                 
B628: CF              RST     0X08                
B629: DF              RST     0X18                
B62A: CF              RST     0X08                
B62B: CE CE           ADC     $CE                 
B62D: CE CA           ADC     $CA                 
B62F: CE DF           ADC     $DF                 
B631: CF              RST     0X08                
B632: 5F              LD      E,A                 
B633: 6F              LD      L,A                 
B634: 6F              LD      L,A                 
B635: 6F              LD      L,A                 
B636: 6F              LD      L,A                 
B637: 4F              LD      C,A                 
B638: 4A              LD      C,D                 
B639: 4F              LD      C,A                 
B63A: 4F              LD      C,A                 
B63B: 6F              LD      L,A                 
B63C: ED ; ????
B63D: EF              RST     0X28                
B63E: ED ; ????
B63F: EF              RST     0X28                
B640: 82              ADD     A,D                 
B641: 00              NOP                         
B642: 00              NOP                         
B643: 00              NOP                         
B644: 00              NOP                         
B645: 00              NOP                         
B646: 00              NOP                         
B647: 00              NOP                         
B648: 00              NOP                         
B649: 00              NOP                         
B64A: 00              NOP                         
B64B: 00              NOP                         
B64C: 00              NOP                         
B64D: 00              NOP                         
B64E: 00              NOP                         
B64F: 00              NOP                         
B650: 00              NOP                         
B651: 00              NOP                         
B652: 00              NOP                         
B653: 00              NOP                         
B654: 00              NOP                         
B655: 00              NOP                         
B656: 00              NOP                         
B657: 00              NOP                         
B658: 00              NOP                         
B659: 00              NOP                         
B65A: 00              NOP                         
B65B: 00              NOP                         
B65C: 00              NOP                         
B65D: 00              NOP                         
B65E: 00              NOP                         
B65F: 00              NOP                         
B660: 00              NOP                         
B661: 00              NOP                         
B662: 00              NOP                         
B663: 00              NOP                         
B664: 00              NOP                         
B665: 00              NOP                         
B666: 00              NOP                         
B667: 00              NOP                         
B668: 00              NOP                         
B669: 00              NOP                         
B66A: 00              NOP                         
B66B: 00              NOP                         
B66C: 80              ADD     A,B                 
B66D: 80              ADD     A,B                 
B66E: 00              NOP                         
B66F: 00              NOP                         
B670: 00              NOP                         
B671: 00              NOP                         
B672: 00              NOP                         
B673: 00              NOP                         
B674: 00              NOP                         
B675: 00              NOP                         
B676: 00              NOP                         
B677: 00              NOP                         
B678: 00              NOP                         
B679: 00              NOP                         
B67A: 00              NOP                         
B67B: 00              NOP                         
B67C: 00              NOP                         
B67D: 00              NOP                         
B67E: 00              NOP                         
B67F: 00              NOP                         
B680: B3              OR      E                   
B681: E2 EF EF        JP      PO,$EFEF            
B684: EF              RST     0X28                
B685: EF              RST     0X28                
B686: 62              LD      H,D                 
B687: 62              LD      H,D                 
B688: EF              RST     0X28                
B689: EF              RST     0X28                
B68A: AF              XOR     A                   
B68B: EF              RST     0X28                
B68C: EB              EX      DE,HL               
B68D: EF              RST     0X28                
B68E: EF              RST     0X28                
B68F: EF              RST     0X28                
B690: EB              EX      DE,HL               
B691: EF              RST     0X28                
B692: EF              RST     0X28                
B693: EF              RST     0X28                
B694: EF              RST     0X28                
B695: EB              EX      DE,HL               
B696: EE E2           XOR     $E2                 
B698: EF              RST     0X28                
B699: EE 00           XOR     $00                 
B69B: EF              RST     0X28                
B69C: EF              RST     0X28                
B69D: EF              RST     0X28                
B69E: EF              RST     0X28                
B69F: EF              RST     0X28                
B6A0: EC EE 6E        CALL    PE,$6EEE            ; {}
B6A3: 6F              LD      L,A                 
B6A4: EF              RST     0X28                
B6A5: EF              RST     0X28                
B6A6: EE CF           XOR     $CF                 
B6A8: CF              RST     0X08                
B6A9: CF              RST     0X08                
B6AA: CF              RST     0X08                
B6AB: CE CE           ADC     $CE                 
B6AD: CA CA CE        JP      Z,$CECA             
B6B0: CE CE           ADC     $CE                 
B6B2: 4F              LD      C,A                 
B6B3: 6F              LD      L,A                 
B6B4: 67              LD      H,A                 
B6B5: 6A              LD      L,D                 
B6B6: 6F              LD      L,A                 
B6B7: 42              LD      B,D                 
B6B8: 4A              LD      C,D                 
B6B9: 4B              LD      C,E                 
B6BA: 4F              LD      C,A                 
B6BB: 6A              LD      L,D                 
B6BC: 6F              LD      L,A                 
B6BD: EA EF EA        JP      PE,$EAEF            
B6C0: 02              LD      (BC),A              
B6C1: 00              NOP                         
B6C2: 00              NOP                         
B6C3: 00              NOP                         
B6C4: 00              NOP                         
B6C5: 00              NOP                         
B6C6: 00              NOP                         
B6C7: 00              NOP                         
B6C8: 00              NOP                         
B6C9: 00              NOP                         
B6CA: 00              NOP                         
B6CB: 00              NOP                         
B6CC: 00              NOP                         
B6CD: 00              NOP                         
B6CE: 00              NOP                         
B6CF: 00              NOP                         
B6D0: 00              NOP                         
B6D1: 00              NOP                         
B6D2: 00              NOP                         
B6D3: 00              NOP                         
B6D4: 00              NOP                         
B6D5: 00              NOP                         
B6D6: 00              NOP                         
B6D7: 00              NOP                         
B6D8: 00              NOP                         
B6D9: 00              NOP                         
B6DA: 00              NOP                         
B6DB: 00              NOP                         
B6DC: 00              NOP                         
B6DD: 00              NOP                         
B6DE: 00              NOP                         
B6DF: 00              NOP                         
B6E0: 00              NOP                         
B6E1: 00              NOP                         
B6E2: 00              NOP                         
B6E3: 00              NOP                         
B6E4: 00              NOP                         
B6E5: 00              NOP                         
B6E6: 00              NOP                         
B6E7: 00              NOP                         
B6E8: 00              NOP                         
B6E9: 00              NOP                         
B6EA: 00              NOP                         
B6EB: 00              NOP                         
B6EC: 80              ADD     A,B                 
B6ED: 80              ADD     A,B                 
B6EE: 00              NOP                         
B6EF: 00              NOP                         
B6F0: 00              NOP                         
B6F1: 00              NOP                         
B6F2: 00              NOP                         
B6F3: 00              NOP                         
B6F4: 00              NOP                         
B6F5: 00              NOP                         
B6F6: 00              NOP                         
B6F7: 00              NOP                         
B6F8: 00              NOP                         
B6F9: 00              NOP                         
B6FA: 00              NOP                         
B6FB: 00              NOP                         
B6FC: 00              NOP                         
B6FD: 00              NOP                         
B6FE: 00              NOP                         
B6FF: 00              NOP                         
B700: EF              RST     0X28                
B701: EF              RST     0X28                
B702: 63              LD      H,E                 
B703: 62              LD      H,D                 
B704: EF              RST     0X28                
B705: EF              RST     0X28                
B706: AF              XOR     A                   
B707: EF              RST     0X28                
B708: EB              EX      DE,HL               
B709: EF              RST     0X28                
B70A: EF              RST     0X28                
B70B: EF              RST     0X28                
B70C: EB              EX      DE,HL               
B70D: EF              RST     0X28                
B70E: EF              RST     0X28                
B70F: EF              RST     0X28                
B710: EF              RST     0X28                
B711: EB              EX      DE,HL               
B712: EE E2           XOR     $E2                 
B714: EF              RST     0X28                
B715: EE EF           XOR     $EF                 
B717: EF              RST     0X28                
B718: EF              RST     0X28                
B719: EF              RST     0X28                
B71A: EF              RST     0X28                
B71B: EF              RST     0X28                
B71C: EC FE 6E        CALL    PE,$6EFE            ; {}
B71F: 6F              LD      L,A                 
B720: EF              RST     0X28                
B721: EF              RST     0X28                
B722: FE EF           CP      $EF                 
B724: CF              RST     0X08                
B725: DF              RST     0X18                
B726: CF              RST     0X08                
B727: CE CE           ADC     $CE                 
B729: CE CA           ADC     $CA                 
B72B: CE DF           ADC     $DF                 
B72D: CF              RST     0X08                
B72E: 5F              LD      E,A                 
B72F: 6F              LD      L,A                 
B730: 6F              LD      L,A                 
B731: 6F              LD      L,A                 
B732: 6F              LD      L,A                 
B733: 4F              LD      C,A                 
B734: 4A              LD      C,D                 
B735: 4F              LD      C,A                 
B736: 4F              LD      C,A                 
B737: 6F              LD      L,A                 
B738: ED ; ????
B739: EF              RST     0X28                
B73A: ED ; ????
B73B: EF              RST     0X28                
B73C: 82              ADD     A,D                 
B73D: 00              NOP                         
B73E: 00              NOP                         
B73F: 00              NOP                         
B740: 00              NOP                         
B741: 00              NOP                         
B742: 00              NOP                         
B743: 00              NOP                         
B744: 00              NOP                         
B745: 00              NOP                         
B746: 00              NOP                         
B747: 00              NOP                         
B748: 00              NOP                         
B749: 00              NOP                         
B74A: 00              NOP                         
B74B: 00              NOP                         
B74C: 00              NOP                         
B74D: 00              NOP                         
B74E: 00              NOP                         
B74F: 00              NOP                         
B750: 00              NOP                         
B751: 00              NOP                         
B752: 00              NOP                         
B753: 00              NOP                         
B754: 00              NOP                         
B755: 00              NOP                         
B756: 00              NOP                         
B757: 00              NOP                         
B758: 00              NOP                         
B759: 00              NOP                         
B75A: 00              NOP                         
B75B: 00              NOP                         
B75C: 00              NOP                         
B75D: 00              NOP                         
B75E: 00              NOP                         
B75F: 00              NOP                         
B760: 00              NOP                         
B761: 00              NOP                         
B762: 00              NOP                         
B763: 00              NOP                         
B764: 00              NOP                         
B765: 00              NOP                         
B766: 00              NOP                         
B767: 00              NOP                         
B768: 80              ADD     A,B                 
B769: 80              ADD     A,B                 
B76A: 00              NOP                         
B76B: 00              NOP                         
B76C: 00              NOP                         
B76D: 00              NOP                         
B76E: 00              NOP                         
B76F: 00              NOP                         
B770: 00              NOP                         
B771: 00              NOP                         
B772: 00              NOP                         
B773: 00              NOP                         
B774: 00              NOP                         
B775: 00              NOP                         
B776: 00              NOP                         
B777: 00              NOP                         
B778: 00              NOP                         
B779: 00              NOP                         
B77A: 00              NOP                         
B77B: 00              NOP                         
B77C: B3              OR      E                   
B77D: E2 EF EF        JP      PO,$EFEF            
B780: EF              RST     0X28                
B781: EF              RST     0X28                
B782: 62              LD      H,D                 
B783: 62              LD      H,D                 
B784: EF              RST     0X28                
B785: EF              RST     0X28                
B786: AF              XOR     A                   
B787: EF              RST     0X28                
B788: EB              EX      DE,HL               
B789: EF              RST     0X28                
B78A: EF              RST     0X28                
B78B: EF              RST     0X28                
B78C: EB              EX      DE,HL               
B78D: EF              RST     0X28                
B78E: EF              RST     0X28                
B78F: EF              RST     0X28                
B790: EF              RST     0X28                
B791: EB              EX      DE,HL               
B792: EE E2           XOR     $E2                 
```

