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
5D06: 22 20 40        LD      ($4020),HL          ; {hard.CursorPointer} ... start of last row on screen
5D09: 3E 01           LD      A,$01               ; Current section is SECTION1.DAT
5D0B: 32 FA 71        LD      ($71FA),A           ; {code.currentLoadedSection}
5D0E: 3E 01           LD      A,$01               ; ?? Player
5D10: 32 1E 72        LD      ($721E),A           ; {code.activeObject}
5D13: 47              LD      B,A                 
5D14: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex} ?? Looking up player object ?
5D17: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
5D1A: 3A 21 72        LD      A,($7221)           ; {code.currentRoom}
5D1D: 77              LD      (HL),A              
5D1E: 23              INC     HL                  
5D1F: 3A FA 71        LD      A,($71FA)           ; {code.currentLoadedSection}
5D22: 77              LD      (HL),A              
;
5D23: 21 67 72        LD      HL,$7267            ; Splash message
5D26: CD 57 63        CALL    $6357               ; {code.ExecuteCommand} Welcome the player
;
5D29: 3E 0D           LD      A,$0D               ; Print a ...
5D2B: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces} ... linefeed
;
5D2E: CD 99 62        CALL    $6299               ; {code.GetKey} Wait for a key to start the game
5D31: 97              SUB     A                   
5D32: 21 66 72        LD      HL,$7266            ; Initialize ...
5D35: CD 57 63        CALL    $6357               ; {code.ExecuteCommand} ... the game (this loads SECTION1.DAT)

GameLoop:
5D38: 31 9A BF        LD      SP,$BF9A            ; Reset the stack
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
5D5A: 32 0B 72        LD      ($720B),A           ; {code.varObject}
5D5D: 32 0F 72        LD      ($720F),A           ; {}
5D60: 32 15 72        LD      ($7215),A           ; {}
;
5D63: 3E 01           LD      A,$01               ; Set active object ...
5D65: 32 1E 72        LD      ($721E),A           ; {code.activeObject} ... to the player
5D68: 47              LD      B,A                 ; Get the player ...
5D69: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex} ... object pointer
5D6C: 22 1F 72        LD      ($721F),HL          ; {code.activeObjectPtr} Hold this for others
5D6F: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd} Get to the data
5D72: 7E              LD      A,(HL)              ; Get the player's room number
5D73: A7              AND     A                   ; Is the player in a room (as opposed to an object)?
5D74: FA 83 5D        JP      M,$5D83             ; {} Yes ... use it
5D77: 47              LD      B,A                 ; Must be an object ...
5D78: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex} ... find object ...
5D7B: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd} ... that has the player
5D7E: 7E              LD      A,(HL)              ; Is this object contained ...
5D7F: A7              AND     A                   ; ... by yet another object?
5D80: F2 77 5D        JP      P,$5D77             ; {} Yes ... recurse up the container tree to a room
;
5D83: 32 21 72        LD      ($7221),A           ; {code.currentRoom} Room that has the player
5D86: 47              LD      B,A                 ; Look up ...
5D87: 21 00 52        LD      HL,$5200            ; {+ram.sectionData} ... the room ...
5D8A: CD A5 61        CALL    $61A5               ; {code.FindCollectionItemByID} ... object
5D8D: 22 22 72        LD      ($7222),HL          ; {code.currentRoomPtr} Hold onto the current room ptr
5D90: A7              AND     A                   ; Did we find the room number in the section?
5D91: C3 9A 5D        JP      $5D9A               ; {} Skip over the DIE sequence (this should be a "JP NZ,$5D9A")
;
; !! These two instructions are never reached from other parts of the code. I believe the original idea was to
; kill the player if the room number is 0, which it should never be. This might be kind of a safeguard in case
; something goes wrong with the rest of the code or disk file. The "AND A" should be followed by a "JP NZ" 
; instead of an "always jump".
;
5D94: 21 2B 76        LD      HL,$762B            ; {+code.DieEnergyBeamCommand} This is the DIE ENERGY BEAM from nowhere function
5D97: CD 57 63        CALL    $6357               ; {code.ExecuteCommand} Kill the player and end the program
;
5D9A: 21 47 72        LD      HL,$7247            ; ?? input token buffer
5D9D: 22 24 72        LD      ($7224),HL          ; {} ?? next token
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
5DF3: CD A5 61        CALL    $61A5               ; {code.FindCollectionItemByID}
5DF6: D2 0D 5E        JP      NC,$5E0D            ; {}
5DF9: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
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
5E98: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
5E9B: 23              INC     HL                  
5E9C: 23              INC     HL                  
5E9D: 7E              LD      A,(HL)              
5E9E: 32 14 72        LD      ($7214),A           ; {}
5EA1: 2A 18 72        LD      HL,($7218)          ; {}
5EA4: 3A 15 72        LD      A,($7215)           ; {}
5EA7: A7              AND     A                   
5EA8: CA B1 5E        JP      Z,$5EB1             ; {}
5EAB: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
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
5F30: 22 20 40        LD      ($4020),HL          ; {hard.CursorPointer}
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
5F58: 32 1E 72        LD      ($721E),A           ; {code.activeObject}
5F5B: 22 1F 72        LD      ($721F),HL          ; {code.activeObjectPtr}
5F5E: 3E 0D           LD      A,$0D               
5F60: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces}
5F63: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
5F66: 23              INC     HL                  
5F67: 23              INC     HL                  
5F68: 23              INC     HL                  
5F69: 06 0B           LD      B,$0B               ; IF_GIVEN_COMMAND section (no object has this)
5F6B: CD AD 61        CALL    $61AD               ; {code.FindObjectField}
5F6E: DA 74 5F        JP      C,$5F74             ; {}
5F71: C3 8B 5F        JP      $5F8B               ; {}
;
5F74: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
5F77: CD 57 63        CALL    $6357               ; {code.ExecuteCommand}
5F7A: C3 8B 5F        JP      $5F8B               ; {}
;
5F7D: 3E 0D           LD      A,$0D               
5F7F: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces}
5F82: 21 4E 7D        LD      HL,$7D4E            ; {+code.GeneralScript}
5F85: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
5F88: CD 57 63        CALL    $6357               ; {code.ExecuteCommand}
5F8B: CD B2 6C        CALL    $6CB2               ; {}
5F8E: 3E 0D           LD      A,$0D               
5F90: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces}
5F93: 3A 1D 72        LD      A,($721D)           ; {}
5F96: C3 38 5D        JP      $5D38               ; {code.GameLoop}
5F99: 97              SUB     A                   
5F9A: 32 0B 72        LD      ($720B),A           ; {code.varObject}
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
5FB1: CD A5 61        CALL    $61A5               ; {code.FindCollectionItemByID}
5FB4: D2 14 60        JP      NC,$6014            ; {}
5FB7: D5              PUSH    DE                  
5FB8: E5              PUSH    HL                  
5FB9: 3A F1 71        LD      A,($71F1)           ; {}
5FBC: 32 F2 71        LD      ($71F2),A           ; {}
5FBF: CD 23 60        CALL    $6023               ; {code.InInRoomOrPack}
5FC2: C2 1F 60        JP      NZ,$601F            ; {}
5FC5: 3A 03 72        LD      A,($7203)           ; {}
5FC8: A7              AND     A                   
5FC9: CA EE 5F        JP      Z,$5FEE             ; {}
5FCC: E1              POP     HL                  
5FCD: E5              PUSH    HL                  
5FCE: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
5FD1: 01 03 00        LD      BC,$0003            
5FD4: 09              ADD     HL,BC               
5FD5: 06 01           LD      B,$01               ; ADJECTIVES section
5FD7: CD AD 61        CALL    $61AD               ; {code.FindObjectField}
5FDA: D2 EE 5F        JP      NC,$5FEE            ; {}
5FDD: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
5FE0: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE}
5FE3: D2 1F 60        JP      NC,$601F            ; {}
5FE6: 3A 03 72        LD      A,($7203)           ; {}
5FE9: BE              CP      (HL)                
5FEA: 23              INC     HL                  
5FEB: C2 E0 5F        JP      NZ,$5FE0            ; {}
5FEE: E1              POP     HL                  
5FEF: 3A 0B 72        LD      A,($720B)           ; {code.varObject}
5FF2: A7              AND     A                   
5FF3: C2 34 61        JP      NZ,$6134            ; {}
5FF6: 3A F2 71        LD      A,($71F2)           ; {}
5FF9: 32 0B 72        LD      ($720B),A           ; {code.varObject}
5FFC: 22 0C 72        LD      ($720C),HL          ; {code.varObjectPtr}
5FFF: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6002: EB              EX      DE,HL               
6003: D1              POP     DE                  
6004: 3A FE 71        LD      A,($71FE)           ; {}
6007: 47              LD      B,A                 
6008: 3A F2 71        LD      A,($71F2)           ; {}
600B: 32 F1 71        LD      ($71F1),A           ; {}
600E: CD AD 61        CALL    $61AD               ; {code.FindObjectField}
6011: DA B7 5F        JP      C,$5FB7             ; {}
6014: 3A 0B 72        LD      A,($720B)           ; {code.varObject}
6017: 2A 0C 72        LD      HL,($720C)          ; {code.varObjectPtr}
601A: A7              AND     A                   
601B: C0              RET     NZ                  
601C: C3 EA 60        JP      $60EA               ; {}
601F: E1              POP     HL                  
6020: C3 FF 5F        JP      $5FFF               ; {}

InInRoomOrPack:
6023: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd} Skip to object data
6026: 3A 21 72        LD      A,($7221)           ; {code.currentRoom} Is object ...
6029: BE              CP      (HL)                ; ... in current room?
602A: C2 41 60        JP      NZ,$6041            ; {} No ... look in pack
602D: 7E              LD      A,(HL)              ; Object location
602E: E6 80           AND     $80                 ; Is this object being held?
6030: CA 41 60        JP      Z,$6041             ; {}
6033: 23              INC     HL                  
6034: 3A FA 71        LD      A,($71FA)           ; {code.currentLoadedSection}
6037: 47              LD      B,A                 
6038: 7E              LD      A,(HL)              
6039: E6 0F           AND     $0F                 
603B: B8              CP      B                   ; And the room's loaded section
603C: 2B              DEC     HL                  
603D: C8              RET     Z                   
603E: C3 6D 60        JP      $606D               ; {}
;
6041: 7E              LD      A,(HL)              
6042: A7              AND     A                   
6043: CA 6D 60        JP      Z,$606D             ; {}
6046: 3C              INC     A                   
6047: C8              RET     Z                   
6048: 7E              LD      A,(HL)              
6049: E6 80           AND     $80                 
604B: C2 6D 60        JP      NZ,$606D            ; {}
604E: 46              LD      B,(HL)              
604F: 3A 1E 72        LD      A,($721E)           ; {code.activeObject}
6052: B8              CP      B                   
6053: C8              RET     Z                   
6054: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
6057: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
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
;
606D: F6 01           OR      $01                 ; Z=0 FAIL
606F: C9              RET                         


6070: E5              PUSH    HL                  
6071: 97              SUB     A                   
6072: 32 FE 71        LD      ($71FE),A           ; {}
6075: 32 F1 71        LD      ($71F1),A           ; {}
6078: D5              PUSH    DE                  
6079: 4E              LD      C,(HL)              
607A: 21 7A 88        LD      HL,$887A            
607D: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6080: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE}
6083: D2 CB 60        JP      NC,$60CB            ; {}
6086: 3A F1 71        LD      A,($71F1)           ; {}
6089: 3C              INC     A                   
608A: 32 F1 71        LD      ($71F1),A           ; {}
608D: D5              PUSH    DE                  
608E: E5              PUSH    HL                  
608F: CD 23 60        CALL    $6023               ; {code.InInRoomOrPack}
6092: E1              POP     HL                  
6093: C2 C5 60        JP      NZ,$60C5            ; {}
6096: 46              LD      B,(HL)              
6097: 22 24 72        LD      ($7224),HL          ; {}
609A: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
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
60C5: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
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

; Collections of the form:
; aa mm mm     : collection id and multi-byte length
;    i1 mm mm  : item id and multi-byte length
;       .....  : data for the item
;    i2 mm mm  : item id and multi-byte length
;       .....  : data for the item
;    ..

FindCollectionItemByID:
; B is the desired item ID
; 71F1 is the index of the item in the list of items
61A5: 23              INC     HL                  ; Skip collection ID
61A6: CD C9 61        CALL    $61C9               ; {code.GetMultiByteLength}
61A9: 97              SUB     A                   ; Keep up with ...
61AA: 32 F1 71        LD      ($71F1),A           ; {} ... index of the object we are checking

FindObjectField:
; B is the field number
61AD: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE} Are we at the end of the list?
61B0: D0              RET     NC                  ; Yes ... done with CF=0
61B1: 3A F1 71        LD      A,($71F1)           ; {} Bump ...
61B4: 3C              INC     A                   ; ... the ...
61B5: 32 F1 71        LD      ($71F1),A           ; {} ... index count
61B8: 78              LD      A,B                 ; Is this the ...
61B9: BE              CP      (HL)                ; ... item we are looking for?
61BA: CA C6 61        JP      Z,$61C6             ; {} Yes ... set CF and done (found)
61BD: D5              PUSH    DE                  ; Hold
61BE: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd} No ... get the length of this field
61C1: EB              EX      DE,HL               ; Move to the start of the next item
61C2: D1              POP     DE                  ; Restore
61C3: C3 AD 61        JP      $61AD               ; {code.FindObjectField} Keep going
;
61C6: 37              SCF                         ; CF=1 if we found
61C7: C9              RET                         

SkipIDCalcEnd:
; Returns pointer to first entry in HL
; Returns one past last byte in DE
61C8: 23              INC     HL                  ; Skip list ID
;
GetMultiByteLength:
61C9: 16 00           LD      D,$00               ; MSB of 0 for 1 byte length
61CB: 7E              LD      A,(HL)              ; First byte of length
61CC: E6 80           AND     $80                 ; Two byte length?
61CE: CA D6 61        JP      Z,$61D6             ; {} No, we have the one byte length
61D1: 7E              LD      A,(HL)              ; MSB again
61D2: E6 7F           AND     $7F                 ; Drop flag bit
61D4: 57              LD      D,A                 ; MSB to D (for DE)
61D5: 23              INC     HL                  ; Point to LSB
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
62F6: F6 01           OR      $01                 ; Z=0 FAIL
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

ExecuteCommand:
6357: 7E              LD      A,(HL)              ; Get command number
6358: 47              LD      B,A                 ; To B for find collection
6359: 23              INC     HL                  ; Next byte in script
635A: E6 80           AND     $80                 ; Is this a custom command?
635C: CA 73 63        JP      Z,$6373             ; {} No, execute a regular command
;
635F: E5              PUSH    HL                  ; Hold
6360: D5              PUSH    DE                  ; Hold
6361: 21 AF B3        LD      HL,$B3AF            ; {+code.SubroutineCommands} Subroutine commands
6364: CD A5 61        CALL    $61A5               ; {code.FindCollectionItemByID}
6367: D2 70 63        JP      NC,$6370            ; {} Not found, out
636A: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
636D: CD 57 63        CALL    $6357               ; {code.ExecuteCommand}
6370: D1              POP     DE                  ; Restore
6371: E1              POP     HL                  ; Restore
6372: C9              RET                         

6373: 78              LD      A,B                 ; Command number
6374: 11 68 72        LD      DE,$7268            ; {+code.CommandJumpTable} command jump table
6377: 07              RLCA                        ; Two bytes per command pointer
6378: 83              ADD     A,E                 ; Add ...
6379: 5F              LD      E,A                 ; ... the ...
637A: 7A              LD      A,D                 ; ... offset ...
637B: CE 00           ADC     $00                 ; ... to ...
637D: 57              LD      D,A                 ; ... the command
637E: 1A              LD      A,(DE)              ; LSB of the command
637F: 32 88 63        LD      ($6388),A           ; {} Write it into JP instruction below
6382: 13              INC     DE                  ; MSB ...
6383: 1A              LD      A,(DE)              ; ... of the command
6384: 32 89 63        LD      ($6389),A           ; {} Write it into JP instruction below
;
6387: C3 87 63        JP      $6387               ; {} This jump destination is modified by code above

COM_0D_while_pass:
; Execute commands while they are passing
638A: CD C9 61        CALL    $61C9               ; {code.GetMultiByteLength}
638D: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE}
6390: D2 9D 63        JP      NC,$639D            ; {}
6393: D5              PUSH    DE                  
6394: CD 57 63        CALL    $6357               ; {code.ExecuteCommand}
6397: D1              POP     DE                  
6398: CA 8D 63        JP      Z,$638D             ; {}
639B: EB              EX      DE,HL               
639C: C9              RET                         
639D: EB              EX      DE,HL               
639E: 97              SUB     A                   ; Z=1 PASS
639F: C9              RET                         

COM_0E_while_fail:
; Execute commands while they are failing
63A0: CD C9 61        CALL    $61C9               ; {code.GetMultiByteLength}
63A3: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE}
63A6: D2 B3 63        JP      NC,$63B3            ; {}
63A9: D5              PUSH    DE                  
63AA: CD 57 63        CALL    $6357               ; {code.ExecuteCommand}
63AD: D1              POP     DE                  
63AE: C2 A3 63        JP      NZ,$63A3            ; {}
63B1: EB              EX      DE,HL               
63B2: C9              RET                         
;
63B3: EB              EX      DE,HL               ; Point script to next construct
63B4: F6 01           OR      $01                 ; Z=0 FAIL
63B6: C9              RET                         

COM_0B_switch:
; switch:
63B7: CD C9 61        CALL    $61C9               ; {code.GetMultiByteLength} Get the length and pointer to end
63BA: 46              LD      B,(HL)              ; Get the command number ...
63BB: 23              INC     HL                  ; ... to call for each
63BC: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE} Have we reached the end of the list?
63BF: D2 B3 63        JP      NC,$63B3            ; {} At or beyond ... FAIL
63C2: D5              PUSH    DE                  
63C3: C5              PUSH    BC                  
63C4: 78              LD      A,B                 
63C5: CD 74 63        CALL    $6374               ; {} Execute the switch test command
63C8: C1              POP     BC                  
63C9: CA D4 63        JP      Z,$63D4             ; {} Test passed ... this is our list
63CC: CD C9 61        CALL    $61C9               ; {code.GetMultiByteLength}
63CF: EB              EX      DE,HL               
63D0: D1              POP     DE                  
63D1: C3 BC 63        JP      $63BC               ; {}
;
63D4: CD C9 61        CALL    $61C9               ; {code.GetMultiByteLength} Length of block to execute
63D7: CD 57 63        CALL    $6357               ; {code.ExecuteCommand} Execute the  matching script
63DA: E1              POP     HL                  ; Restore script pointer
63DB: C9              RET                         

COM_00_move_ACTIVE_and_look:
63DC: CD F5 63        CALL    $63F5               ; {code.COM_19_move_ACTIVE} Move the active object
63DF: E5              PUSH    HL                  ; Hold script pointer
63E0: 2A 22 72        LD      HL,($7222)          ; {code.currentRoomPtr} Point to the room's ...
63E3: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd} ... data byte
63E6: 7E              LD      A,(HL)              ; If we have been here before ...
63E7: 32 F0 71        LD      ($71F0),A           ; {code.stopAtPeriod} ... stop at first period
63EA: 36 01           LD      (HL),$01            ; Set the flag now that we have been here
63EC: CD C1 64        CALL    $64C1               ; {code.PrintObjectsInRoom} Print objects in room
63EF: E1              POP     HL                  ; Restore script pointer
63F0: 97              SUB     A                   ; Clear stop printing after ...
63F1: 32 F0 71        LD      ($71F0),A           ; {code.stopAtPeriod} ... period flag
63F4: C9              RET                         

COM_19_move_ACTIVE:
; move_ACTIVE(room)
63F5: 7E              LD      A,(HL)              ; New room number
63F6: 23              INC     HL                  ; Advance pointer
63F7: E5              PUSH    HL                  ; Hold
63F8: 32 21 72        LD      ($7221),A           ; {code.currentRoom} Set new room number
63FB: 47              LD      B,A                 ; To B for finding
63FC: 21 00 52        LD      HL,$5200            ; {+ram.sectionData} Room descriptions
63FF: CD A5 61        CALL    $61A5               ; {code.FindCollectionItemByID} Find the room data
6402: 22 22 72        LD      ($7222),HL          ; {code.currentRoomPtr} Store pointer to current room
6405: 2A 1F 72        LD      HL,($721F)          ; {code.activeObjectPtr}
6408: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
640B: 3A 21 72        LD      A,($7221)           ; {code.currentRoom}
640E: 77              LD      (HL),A              
640F: E1              POP     HL                  
6410: 97              SUB     A                   ; Z=1 PASS
6411: C9              RET                         

COM_37__:
6412: 06 01           LD      B,$01               ; Player object number
6414: E5              PUSH    HL                  ; Hold
6415: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex} Get the player object
6418: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd} Start of the data
641B: 7E              LD      A,(HL)              ; Player's room number
641C: E1              POP     HL                  ; Restore
641D: A7              AND     A                   
641E: F8              RET     M                   
641F: 47              LD      B,A                 
6420: E5              PUSH    HL                  
6421: 32 0B 72        LD      ($720B),A           ; {code.varObject} ?? Object the player is in?
6424: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
6427: 22 0C 72        LD      ($720C),HL          ; {code.varObjectPtr} ?? Object the player is in?
642A: E1              POP     HL                  
642B: 97              SUB     A                   

COM_1A_set_var_to_first_noun:
642C: E5              PUSH    HL                  
642D: 2A 12 72        LD      HL,($7212)          ; {}
6430: 22 0C 72        LD      ($720C),HL          ; {code.varObjectPtr}
6433: 3A 0F 72        LD      A,($720F)           ; {}
6436: 32 0B 72        LD      ($720B),A           ; {code.varObject}
6439: E1              POP     HL                  
643A: 97              SUB     A                   ; Z=1 PASS
643B: C9              RET                         

COM_1B_set_VAR_to_second_noun:
; set_VAR_to_second_noun()
643C: E5              PUSH    HL                  
643D: 2A 18 72        LD      HL,($7218)          ; {}
6440: 22 0C 72        LD      ($720C),HL          ; {code.varObjectPtr}
6443: 3A 15 72        LD      A,($7215)           ; {}
6446: 32 0B 72        LD      ($720B),A           ; {code.varObject}
6449: E1              POP     HL                  
644A: 97              SUB     A                   ; Z=1 PASS
644B: C9              RET                         

COM_1C_setVAR:
644C: 46              LD      B,(HL)              
644D: 23              INC     HL                  
644E: E5              PUSH    HL                  
644F: 78              LD      A,B                 
6450: 32 0B 72        LD      ($720B),A           ; {code.varObject}
6453: A7              AND     A                   
6454: CA 5D 64        JP      Z,$645D             ; {}
6457: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
645A: 22 0C 72        LD      ($720C),HL          ; {code.varObjectPtr}
645D: E1              POP     HL                  
645E: 97              SUB     A                   ; Z=1 PASS
645F: C9              RET                         

COM_21_execute_phrase:
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
648A: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
648D: 22 12 72        LD      ($7212),HL          ; {}
6490: 79              LD      A,C                 
6491: 32 15 72        LD      ($7215),A           ; {}
6494: A7              AND     A                   
6495: CA 9F 64        JP      Z,$649F             ; {}
6498: 47              LD      B,A                 
6499: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
649C: 22 18 72        LD      ($7218),HL          ; {}
649F: 21 4E 7D        LD      HL,$7D4E            ; {+code.GeneralScript}
64A2: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
64A5: CD 57 63        CALL    $6357               ; {code.ExecuteCommand}
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

PrintObjectsInRoom: ; ??
64C1: 3A 1E 72        LD      A,($721E)           ; {code.activeObject} Active object number
64C4: FE 38           CP      $38                 ; Is this the system object number? !! From the BEDLAM code. Not used here.
64C6: CA CC 64        JP      Z,$64CC             ; {} Yes ... keep going
64C9: FE 01           CP      $01                 ; Is this the player object?
64CB: C0              RET     NZ                  ; No ... print nothing
;
64CC: 06 01           LD      B,$01               ; Find the ...
64CE: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex} ... first object ??player?? ...
64D1: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd} ... object
64D4: 7E              LD      A,(HL)              ; Location of player
64D5: E6 80           AND     $80                 ; ?? Owned by something??
64D7: C2 F6 64        JP      NZ,$64F6            ; {} Skip printing the room description
64DA: 46              LD      B,(HL)              ; Find the ...
64DB: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex} ... player's room
64DE: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd} Skip the length
64E1: 23              INC     HL                  ; Skip ...
64E2: 23              INC     HL                  ; ...
64E3: 23              INC     HL                  
64E4: 06 02           LD      B,$02               ; SHORT_NAME ...
64E6: CD AD 61        CALL    $61AD               ; {code.FindObjectField} ... section
64E9: D2 F6 64        JP      NC,$64F6            ; {} Skip this object if it has no short name
64EC: 23              INC     HL                  ; Skip to the length
64ED: CD 6F 70        CALL    $706F               ; {code.PrintPackedAutoWrap} Print the object's short name
64F0: 21 7B 65        LD      HL,$657B            
64F3: CD 57 63        CALL    $6357               ; {code.ExecuteCommand}
;
64F6: 2A 22 72        LD      HL,($7222)          ; {code.currentRoomPtr}
64F9: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
64FC: 23              INC     HL                  
64FD: 06 03           LD      B,$03               ; DESCRIPTION ...
64FF: CD AD 61        CALL    $61AD               ; {code.FindObjectField} ... section
6502: D2 10 65        JP      NC,$6510            ; {} No script, ignore this object
6505: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6508: EB              EX      DE,HL               
6509: 22 7E 65        LD      ($657E),HL          ; {}
650C: EB              EX      DE,HL               
650D: CD 57 63        CALL    $6357               ; {code.ExecuteCommand} Execute the description script
;
6510: 21 7A 88        LD      HL,$887A            ; {+code.ObjectData}
6513: 97              SUB     A                   
6514: 32 F8 71        LD      ($71F8),A           ; {}
6517: 32 F0 71        LD      ($71F0),A           ; {code.stopAtPeriod}
651A: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
651D: D5              PUSH    DE                  
651E: 3A F8 71        LD      A,($71F8)           ; {}
6521: 3C              INC     A                   
6522: 32 F8 71        LD      ($71F8),A           ; {}
6525: 32 0B 72        LD      ($720B),A           ; {code.varObject}
6528: 22 0C 72        LD      ($720C),HL          ; {code.varObjectPtr}
652B: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
652E: 3A 21 72        LD      A,($7221)           ; {code.currentRoom}
6531: BE              CP      (HL)                
6532: C2 71 65        JP      NZ,$6571            ; {}
6535: 23              INC     HL                  
6536: 3A FA 71        LD      A,($71FA)           ; {code.currentLoadedSection}
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
654D: 06 03           LD      B,$03               ; DESCRIPTION section
654F: CD AD 61        CALL    $61AD               ; {code.FindObjectField}
6552: D2 5D 65        JP      NC,$655D            ; {}
6555: D5              PUSH    DE                  
6556: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6559: CD 57 63        CALL    $6357               ; {code.ExecuteCommand}
655C: D1              POP     DE                  
655D: 2A F3 71        LD      HL,($71F3)          ; {}
6560: 06 02           LD      B,$02               ; SHORT_NAME section
6562: D5              PUSH    DE                  
6563: CD AD 61        CALL    $61AD               ; {code.FindObjectField}
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

657A: B1 ; Routine B1 PRINT_SPACE
657B: 8B ; Routine 8B PRINT_PERIOD
657C: B4 ; Routine B4 PRINT_AND
657D: B2 ; Routine B2: ?? " ON <THE VAR> CAN BE SEEN"

657E: 00 00

COM_33__:
6580: E5              PUSH    HL                  
6581: 97              SUB     A                   
6582: 32 FB 66        LD      ($66FB),A           ; {}
6585: 32 FA 66        LD      ($66FA),A           ; {}
6588: 3C              INC     A                   
6589: 32 FC 66        LD      ($66FC),A           ; {}
658C: 2A 0C 72        LD      HL,($720C)          ; {code.varObjectPtr}
658F: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6592: 23              INC     HL                  
6593: 7E              LD      A,(HL)              
6594: 32 F5 71        LD      ($71F5),A           ; {}
6597: 23              INC     HL                  
6598: 7E              LD      A,(HL)              
6599: 32 F6 71        LD      ($71F6),A           ; {}
659C: 3A 0B 72        LD      A,($720B)           ; {code.varObject}
659F: 32 F8 71        LD      ($71F8),A           ; {}
65A2: CD BC 65        CALL    $65BC               ; {}
65A5: E1              POP     HL                  
65A6: 3A FB 66        LD      A,($66FB)           ; {}
65A9: A7              AND     A                   
65AA: CA AF 65        JP      Z,$65AF             ; {}
65AD: 97              SUB     A                   ; Z=1 PASS
65AE: C9              RET                         
65AF: F6 01           OR      $01                 ; Z=0 FAIL
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
65E6: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
65E9: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE}
65EC: D2 45 66        JP      NC,$6645            ; {}
65EF: 3A F9 71        LD      A,($71F9)           ; {}
65F2: 3C              INC     A                   
65F3: 32 F9 71        LD      ($71F9),A           ; {}
65F6: D5              PUSH    DE                  
65F7: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
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
661D: CD 57 63        CALL    $6357               ; {code.ExecuteCommand}
6620: 3E 01           LD      A,$01               
6622: 32 FD 66        LD      ($66FD),A           ; {}
6625: 21 7A 65        LD      HL,$657A            
6628: CD 57 63        CALL    $6357               ; {code.ExecuteCommand}
662B: 3E 01           LD      A,$01               
662D: 32 FA 66        LD      ($66FA),A           ; {}
6630: E1              POP     HL                  
6631: C3 3C 66        JP      $663C               ; {}
6634: E5              PUSH    HL                  
6635: 21 7C 65        LD      HL,$657C            
6638: CD 57 63        CALL    $6357               ; {code.ExecuteCommand}
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
665A: CD 57 63        CALL    $6357               ; {code.ExecuteCommand}
665D: 3E 01           LD      A,$01               
665F: 32 FD 66        LD      ($66FD),A           ; {}
6662: 3A F6 71        LD      A,($71F6)           ; {}
6665: E6 01           AND     $01                 
6667: CA D3 66        JP      Z,$66D3             ; {}
666A: 97              SUB     A                   
666B: 32 F7 71        LD      ($71F7),A           ; {}
666E: 32 F9 71        LD      ($71F9),A           ; {}
6671: 21 7A 88        LD      HL,$887A            
6674: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6677: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE}
667A: D2 D3 66        JP      NC,$66D3            ; {}
667D: 3A F9 71        LD      A,($71F9)           ; {}
6680: 3C              INC     A                   
6681: 32 F9 71        LD      ($71F9),A           ; {}
6684: D5              PUSH    DE                  
6685: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
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
66AB: CD 57 63        CALL    $6357               ; {code.ExecuteCommand}
66AE: 3E 01           LD      A,$01               
66B0: 32 FD 66        LD      ($66FD),A           ; {}
66B3: 21 7D 65        LD      HL,$657D            
66B6: CD 57 63        CALL    $6357               ; {code.ExecuteCommand}
66B9: E1              POP     HL                  
66BA: 3E 01           LD      A,$01               
66BC: 32 FA 66        LD      ($66FA),A           ; {}
66BF: C3 CA 66        JP      $66CA               ; {}
66C2: E5              PUSH    HL                  
66C3: 21 7C 65        LD      HL,$657C            
66C6: CD 57 63        CALL    $6357               ; {code.ExecuteCommand}
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
66E8: CD 57 63        CALL    $6357               ; {code.ExecuteCommand}
66EB: 3E 01           LD      A,$01               
66ED: 32 FD 66        LD      ($66FD),A           ; {}
66F0: D1              POP     DE                  
66F1: 3A F9 66        LD      A,($66F9)           ; {}
66F4: 3D              DEC     A                   
66F5: 32 F9 66        LD      ($66F9),A           ; {}
66F8: C9              RET                         
66F9: 00                         
66FA: 00                         
66FB: 00                         
66FC: 00                         
66FD: 00                         
66FE: E5              PUSH    HL                  
66FF: 23              INC     HL                  
6700: 23              INC     HL                  
6701: 23              INC     HL                  
6702: 06 02           LD      B,$02               ; SHORT_NAME section
6704: CD AD 61        CALL    $61AD               ; {code.FindObjectField}
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
672C: 3A 0B 72        LD      A,($720B)           ; {code.varObject}
672F: F5              PUSH    AF                  
6730: 2A 0C 72        LD      HL,($720C)          ; {code.varObjectPtr}
6733: E5              PUSH    HL                  
6734: 3A F8 71        LD      A,($71F8)           ; {}
6737: 47              LD      B,A                 
6738: 32 0B 72        LD      ($720B),A           ; {code.varObject}
673B: D5              PUSH    DE                  
673C: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
673F: 22 0C 72        LD      ($720C),HL          ; {code.varObjectPtr}
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
6759: 22 0C 72        LD      ($720C),HL          ; {code.varObjectPtr}
675C: F1              POP     AF                  
675D: 32 0B 72        LD      ($720B),A           ; {code.varObject}
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

COM_01_is_in_pack_or_current_room:
677E: 46              LD      B,(HL)              ; Get the object number
677F: 23              INC     HL                  ; Bump script pointer
6780: E5              PUSH    HL                  ; Hold script pointer
6781: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex} Find the requested object
6784: CD 23 60        CALL    $6023               ; {code.InInRoomOrPack} Check if object is in room or pack
6787: E1              POP     HL                  ; Restore script pointer
6788: C9              RET                         

COM_20_is_active_this:
6789: 3A 1E 72        LD      A,($721E)           ; {code.activeObject} Get the active object number
678C: BE              CP      (HL)                ; Does it match target in script?
678D: 23              INC     HL                  ; Bump script pointer
678E: C9              RET                         

COM_2C_set_active:
678F: 46              LD      B,(HL)              ; Get object number from script
6790: 23              INC     HL                  ; Bump script
6791: E5              PUSH    HL                  ; Hold
6792: 78              LD      A,B                 ; Set the ...
6793: 32 1E 72        LD      ($721E),A           ; {code.activeObject} ... active object number
6796: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex} Find the object structure
6799: 22 1F 72        LD      ($721F),HL          ; {code.activeObjectPtr} Hold the active object structure
679C: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
679F: 7E              LD      A,(HL)              
67A0: E6 80           AND     $80                 
67A2: 7E              LD      A,(HL)              
67A3: C2 AE 67        JP      NZ,$67AE            ; {}
67A6: 47              LD      B,A                 
67A7: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
67AA: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
67AD: 7E              LD      A,(HL)              
67AE: 32 21 72        LD      ($7221),A           ; {code.currentRoom}
67B1: 47              LD      B,A                 
67B2: 21 00 52        LD      HL,$5200            ; {+ram.sectionData}
67B5: CD A5 61        CALL    $61A5               ; {code.FindCollectionItemByID}
67B8: 22 22 72        LD      ($7222),HL          ; {code.currentRoomPtr}
67BB: E1              POP     HL                  
67BC: 97              SUB     A                   ; Z=1 PASS
67BD: C9              RET                         

COM_30_set_current_room:
67BE: 7E              LD      A,(HL)              ; Value from the script
67BF: 23              INC     HL                  ; Advance the script pointer
67C0: 32 21 72        LD      ($7221),A           ; {code.currentRoom} Set the current room
67C3: 97              SUB     A                   ; Z=1 PASS
67C4: C9              RET                         

COM_02_is_owned:
67C5: 46              LD      B,(HL)              
67C6: 23              INC     HL                  
67C7: C3 AB 6C        JP      $6CAB               ; {}

COM_03_is_located:
67CA: 4E              LD      C,(HL)              
67CB: 23              INC     HL                  
67CC: 46              LD      B,(HL)              
67CD: 23              INC     HL                  
67CE: E5              PUSH    HL                  
67CF: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
67D2: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
67D5: 5E              LD      E,(HL)              
67D6: 23              INC     HL                  
67D7: 7E              LD      A,(HL)              
67D8: E1              POP     HL                  
67D9: 7B              LD      A,E                 
67DA: B9              CP      C                   
67DB: C9              RET                         

COM_0C_fail:
67DC: F6 01           OR      $01                 ; Z=0 FAIL
67DE: C9              RET                         

COM_04_print_message:
67DF: 3A 1E 72        LD      A,($721E)           ; {code.activeObject} Get the active object number
67E2: FE 38           CP      $38                 ; Is this the system object? !! From the BEDLAM code. Not used here.
67E4: CA 00 68        JP      Z,$6800             ; {} Yes ... print the message
67E7: FE 01           CP      $01                 ; Is this the player object?
67E9: C2 F9 67        JP      NZ,$67F9            ; {} No ...

COM_1F_print2:
67EC: 06 01           LD      B,$01               ; Find player object
67EE: E5              PUSH    HL                  ; Hold
67EF: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
67F2: CD 23 60        CALL    $6023               ; {code.InInRoomOrPack}
67F5: E1              POP     HL                  
67F6: CA 00 68        JP      Z,$6800             ; {}
67F9: CD C9 61        CALL    $61C9               ; {code.GetMultiByteLength}
67FC: EB              EX      DE,HL               
67FD: C3 03 68        JP      $6803               ; {}
;
6800: CD 6F 70        CALL    $706F               ; {code.PrintPackedAutoWrap}
6803: 97              SUB     A                   ; Z=1 PASS
6804: C9              RET                         

COM_07_print_room_description:
6805: CD C1 64        CALL    $64C1               ; {code.PrintObjectsInRoom}
6808: 97              SUB     A                   
6809: 32 F0 71        LD      ($71F0),A           ; {code.stopAtPeriod}
680C: C9              RET                         

COM_06_print_inventory:
680D: E5              PUSH    HL                  ; Hold
680E: 3E 0D           LD      A,$0D               ; Print a ...
6810: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces} ... line feed
6813: 97              SUB     A                   
6814: 32 F8 71        LD      ($71F8),A           ; {}
6817: 21 7A 88        LD      HL,$887A            ; {+code.ObjectData} Pointer to objects
681A: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd} Get the list of objects
;
681D: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE} End of object list?
6820: D2 7D 68        JP      NC,$687D            ; {} Yes ... return PASS
6823: 3A F8 71        LD      A,($71F8)           ; {}
6826: 3C              INC     A                   
6827: 32 F8 71        LD      ($71F8),A           ; {}
682A: 32 0B 72        LD      ($720B),A           ; {code.varObject}
682D: 22 0C 72        LD      ($720C),HL          ; {code.varObjectPtr}
6830: D5              PUSH    DE                  
6831: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6834: 46              LD      B,(HL)              
6835: 3A 1E 72        LD      A,($721E)           ; {code.activeObject}
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
684C: 06 02           LD      B,$02               ; SHORT_NAME
684E: CD AD 61        CALL    $61AD               ; {code.FindObjectField} ... section
6851: D2 78 68        JP      NC,$6878            ; {} Skip object if it has no short name
6854: 23              INC     HL                  ; Bump to length
6855: 22 F3 71        LD      ($71F3),HL          ; {}
6858: D5              PUSH    DE                  ; Hold
6859: 3E 41           LD      A,$41               ; Print ...
685B: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces} ... "A"
685E: 3E 20           LD      A,$20               ; Print ...
6860: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces} ... space
6863: CD 66 70        CALL    $7066               ; {code.PrintPackedAndLF} Print the object short name
6866: D1              POP     DE                  ; Restore
6867: CD B2 65        CALL    $65B2               ; {}
686A: 3A FD 66        LD      A,($66FD)           ; {}
686D: A7              AND     A                   
686E: CA 78 68        JP      Z,$6878             ; {}
6871: 3E 0D           LD      A,$0D               ; Print ...
6873: D5              PUSH    DE                  ; ...
6874: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces} ... line feed
6877: D1              POP     DE                  ; Restore
6878: EB              EX      DE,HL               
6879: D1              POP     DE                  
687A: C3 1D 68        JP      $681D               ; {}
;
687D: 97              SUB     A                   ; Z=1 PASS
687E: E1              POP     HL                  ; Restore script pointer
687F: C9              RET                         

COM_08_is_first_noun:
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
6899: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
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

COM_09_compare_to_second_noun:
68AA: E5              PUSH    HL                  
68AB: 2A 18 72        LD      HL,($7218)          ; {}
68AE: 3A 15 72        LD      A,($7215)           ; {}
68B1: C3 87 68        JP      $6887               ; {}

COM_2D__:
68B4: E5              PUSH    HL                  
68B5: 2A 0C 72        LD      HL,($720C)          ; {code.varObjectPtr}
68B8: 3A 0B 72        LD      A,($720B)           ; {code.varObject}
68BB: C3 87 68        JP      $6887               ; {}

COM_0A_compare_to_second_noun:
68BE: 46              LD      B,(HL)              
68BF: 23              INC     HL                  
68C0: 3A 1D 72        LD      A,($721D)           ; {}
68C3: B8              CP      B                   
68C4: C9              RET                         

COM_0F__:
68C5: E5              PUSH    HL                  ; Hold
68C6: 06 01           LD      B,$01               ; Look up ...
68C8: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex} ... the player object
68CB: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd} Find end of player object
68CE: 4E              LD      C,(HL)              ; Player's room number
68CF: 2A 0C 72        LD      HL,($720C)          ; {code.varObjectPtr}
68D2: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
68D5: 79              LD      A,C                 
68D6: A7              AND     A                   
68D7: FA E3 68        JP      M,$68E3             ; {}
68DA: 7E              LD      A,(HL)              
68DB: A7              AND     A                   
68DC: F2 E3 68        JP      P,$68E3             ; {}
68DF: E1              POP     HL                  
68E0: F6 01           OR      $01                 ; Z=0 FAIL
68E2: C9              RET                         
;
68E3: 3A 1E 72        LD      A,($721E)           ; {code.activeObject}
68E6: 77              LD      (HL),A              
68E7: 23              INC     HL                  
68E8: 7E              LD      A,(HL)              
68E9: E6 F0           AND     $F0                 
68EB: 77              LD      (HL),A              
68EC: 97              SUB     A                   ; Z=1 PASS
68ED: E1              POP     HL                  
68EE: C9              RET                         

COM_10_drop_var:
68EF: E5              PUSH    HL                  ; Hold script pointer
68F0: 2A 0C 72        LD      HL,($720C)          ; {code.varObjectPtr} The current VAR object ptr
68F3: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd} Skip to the data
68F6: 3A 21 72        LD      A,($7221)           ; {code.currentRoom} Store the ...
68F9: 77              LD      (HL),A              ; ... current room number
68FA: 23              INC     HL                  ; 2nd data is section number
68FB: 7E              LD      A,(HL)              ; Get the section number
68FC: E6 F0           AND     $F0                 ; We are replacing the lower nibble
68FE: 47              LD      B,A                 ; Hold upper nibble ?? Must be other data in the upper nibble ... what ??
68FF: 3A FA 71        LD      A,($71FA)           ; {code.currentLoadedSection} Currently loaded sector
6902: B0              OR      B                   ; To the lower nibble (keeping object's upper nibble)
6903: 77              LD      (HL),A              ; Remember which section (room numbers aren't unique)
6904: 97              SUB     A                   ; Z=1 PASS
6905: E1              POP     HL                  ; Restore script pointer
6906: C9              RET                         

COM_13_process_phrase_by_room_first_second:
6907: E5              PUSH    HL                  
6908: 2A 22 72        LD      HL,($7222)          ; {code.currentRoomPtr}
690B: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
690E: 23              INC     HL                  
690F: 06 04           LD      B,$04               ; COMMANDS section
6911: CD AD 61        CALL    $61AD               ; {code.FindObjectField}
6914: D2 20 69        JP      NC,$6920            ; {}
6917: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
691A: CD 57 63        CALL    $6357               ; {code.ExecuteCommand}
691D: CA 63 69        JP      Z,$6963             ; {}
6920: 3A 15 72        LD      A,($7215)           ; {}
6923: A7              AND     A                   
6924: CA 41 69        JP      Z,$6941             ; {}
6927: 2A 18 72        LD      HL,($7218)          ; {}
692A: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
692D: 23              INC     HL                  
692E: 23              INC     HL                  
692F: 23              INC     HL                  
6930: 06 06           LD      B,$06               ; IF_SECOND_NOUN section
6932: CD AD 61        CALL    $61AD               ; {code.FindObjectField}
6935: D2 41 69        JP      NC,$6941            ; {}
6938: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
693B: CD 57 63        CALL    $6357               ; {code.ExecuteCommand}
693E: CA 63 69        JP      Z,$6963             ; {}
6941: 3A 0F 72        LD      A,($720F)           ; {}
6944: A7              AND     A                   
6945: C2 4C 69        JP      NZ,$694C            ; {}
;
6948: E1              POP     HL                  ; Restore script
6949: F6 01           OR      $01                 ; Z=0 FAIL
694B: C9              RET                         

694C: 2A 12 72        LD      HL,($7212)          ; {}
694F: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6952: 23              INC     HL                  
6953: 23              INC     HL                  
6954: 23              INC     HL                  
6955: 06 07           LD      B,$07               ; IF_FIRST_NOUN section
6957: CD AD 61        CALL    $61AD               ; {code.FindObjectField}
695A: D2 48 69        JP      NC,$6948            ; {}
695D: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6960: CD 57 63        CALL    $6357               ; {code.ExecuteCommand}
6963: E1              POP     HL                  
6964: C9              RET                         

COM_16_print_var:
6965: E5              PUSH    HL                  
6966: 2A 0C 72        LD      HL,($720C)          ; {code.varObjectPtr}
6969: 3A 0B 72        LD      A,($720B)           ; {code.varObject}
696C: C3 76 69        JP      $6976               ; {}

COM_11_print_first_noun:
696F: E5              PUSH    HL                  
6970: 2A 12 72        LD      HL,($7212)          ; {}
6973: 3A 0F 72        LD      A,($720F)           ; {}
6976: A7              AND     A                   
6977: CA 63 69        JP      Z,$6963             ; {}
697A: 06 01           LD      B,$01               
697C: E5              PUSH    HL                  
697D: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
6980: CD 23 60        CALL    $6023               ; {code.InInRoomOrPack}
6983: E1              POP     HL                  
6984: C2 99 69        JP      NZ,$6999            ; {}
6987: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
698A: 23              INC     HL                  
698B: 23              INC     HL                  
698C: 23              INC     HL                  
698D: 06 02           LD      B,$02               ; SHORT_NAME section
698F: CD AD 61        CALL    $61AD               ; {code.FindObjectField}
6992: D2 99 69        JP      NC,$6999            ; {}
6995: 23              INC     HL                  
6996: CD 6F 70        CALL    $706F               ; {code.PrintPackedAutoWrap}
6999: E1              POP     HL                  
699A: 97              SUB     A                   ; Z=1 PASS
699B: C9              RET                         

COM_12_print_second_noun:
699C: E5              PUSH    HL                  
699D: 3A 15 72        LD      A,($7215)           ; {}
69A0: 2A 18 72        LD      HL,($7218)          ; {}
69A3: C3 76 69        JP      $6976               ; {}

COM_15_check_var:
; Bits from the next byte in the script
69A6: E5              PUSH    HL                  ; Hold script pointer
69A7: 2A 0C 72        LD      HL,($720C)          ; {code.varObjectPtr} Pointer to the var object
69AA: 3A 0B 72        LD      A,($720B)           ; {code.varObject} Var object number
69AD: A7              AND     A                   ; If the "nowhere" ...
69AE: CA BC 69        JP      Z,$69BC             ; {} ... object, Fail
69B1: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd} Point to data
69B4: 23              INC     HL                  ; Point to ...
69B5: 23              INC     HL                  ; ... attributes
69B6: 7E              LD      A,(HL)              ; Attributes from object
69B7: E1              POP     HL                  ; Restore script pointer
69B8: A6              AND     (HL)                ; Mask off all but target bits
69B9: AE              XOR     (HL)                ; Check the target bits (Z=1 PASS if all bits were set)
69BA: 23              INC     HL                  ; Skip over check bits
69BB: C9              RET                         
;
69BC: E1              POP     HL                  ; Restore script pointer
69BD: 23              INC     HL                  ; Skip over check bits
69BE: F6 01           OR      $01                 ; Z=0 FAIL
69C0: C9              RET                         

COM_2E__:
69C1: E5              PUSH    HL                  ; Hold script pointer
69C2: 2A 0C 72        LD      HL,($720C)          ; {code.varObjectPtr}
69C5: 3A 0B 72        LD      A,($720B)           ; {code.varObject}
69C8: A7              AND     A                   ; If the "nowhere" ...
69C9: CA 48 69        JP      Z,$6948             ; {} ... object, FAIL
69CC: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd} Point to data
69CF: C3 B5 69        JP      $69B5               ; {} Skip to the health-points byte

COM_29_print_open_var:
69D2: E5              PUSH    HL                  
69D3: 2A 0C 72        LD      HL,($720C)          ; {code.varObjectPtr}
69D6: 3A 0B 72        LD      A,($720B)           ; {code.varObject}
69D9: A7              AND     A                   
69DA: CA 48 69        JP      Z,$6948             ; {}
69DD: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
69E0: 23              INC     HL                  
69E1: 7E              LD      A,(HL)              
69E2: EE 20           XOR     $20                 
69E4: 77              LD      (HL),A              
69E5: E1              POP     HL                  
69E6: 97              SUB     A                   ; Z=1 PASS
69E7: C9              RET                         

COM_2A__:
69E8: E5              PUSH    HL                  
69E9: 2A 0C 72        LD      HL,($720C)          ; {code.varObjectPtr}
69EC: 3A 0B 72        LD      A,($720B)           ; {code.varObject}
69EF: A7              AND     A                   
69F0: CA 48 69        JP      Z,$6948             ; {}
69F3: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
69F6: 23              INC     HL                  
69F7: 7E              LD      A,(HL)              
69F8: EE 40           XOR     $40                 
69FA: 77              LD      (HL),A              
69FB: E1              POP     HL                  
69FC: 97              SUB     A                   ; Z=1 PASS
69FD: C9              RET                         

; https://oldcomputers-ddns.org/public/pub/rechner/tandy/manuals/newdos-80%20manual.pdf
; File Control Block: https://www.trs-80.com/sub-reference-dos-trsdos-13-internals.htm#FCB

COM_2F_load_disk_section:
; Loads the section from the disk. This command aborts the current script and returns to the
; top of the game loop for the next user input. This makes since as the new script is
; overwriting the old.
69FE: 7E              LD      A,(HL)              ; Get the section number (1-9)
69FF: C6 30           ADD     $30                 ; Now an ASCII digit for filename
6A01: 32 EC 6A        LD      ($6AEC),A           ; {code.sectionLetter} Build the filename
6A04: 7E              LD      A,(HL)              ; Section number again
6A05: 32 FA 71        LD      ($71FA),A           ; {code.currentLoadedSection} Remember what's loaded
;
6A08: 21 06 6B        LD      HL,$6B06            ; {+code.diskFileControlBlock} The FCB we are building
6A0B: 11 E5 6A        LD      DE,$6AE5            ; {+} The filename
6A0E: 06 21           LD      B,$21               ; Copy ...
6A10: 1A              LD      A,(DE)              ; ...
6A11: 77              LD      (HL),A              ; ...
6A12: 23              INC     HL                  ; ... 17 bytes of filename
6A13: 13              INC     DE                  ; ...
6A14: 05              DEC     B                   ; ...
6A15: C2 10 6A        JP      NZ,$6A10            ; {} ...
6A18: 06 1F           LD      B,$1F               ; Clear rest of ...
6A1A: 36 20           LD      (HL),$20            ; ... FCB ...
6A1C: 23              INC     HL                  ; ... with ...
6A1D: 05              DEC     B                   ; ... blank ...
6A1E: C2 1A 6A        JP      NZ,$6A1A            ; {} ... spaces
6A21: 21 49 6B        LD      HL,$6B49            ; {+code.sectorBuffer} Start of 256 byte sector buffer
6A24: 11 06 6B        LD      DE,$6B06            ; File control block
6A27: 06 00           LD      B,$00               ; Logical record length LRECL=0 means 256 bytes
6A29: CD 24 44        CALL    $4424               ; {hard.OPEN_EXISTING} Open an existing file
6A2C: C2 D0 6A        JP      NZ,$6AD0            ; {} If there is an error, retry
6A2F: 11 06 6B        LD      DE,$6B06            ; The FCB for the file
6A32: CD 36 44        CALL    $4436               ; {hard.READ_RECORD} B=0 -- 4 byte block header + 256 bytes data
6A35: 21 00 52        LD      HL,$5200            ; {+ram.sectionData} Destination for the loaded data
6A38: 11 49 6B        LD      DE,$6B49            ; The buffer we just read into
;
6A3B: CD AA 6A        CALL    $6AAA               ; {} Get the first byte of 4-byte block header
6A3E: FE 01           CP      $01                 ; File type 1 - object code or load block
6A40: C2 66 6A        JP      NZ,$6A66            ; {} Incorrect block type ... finish up
6A43: CD AA 6A        CALL    $6AAA               ; {} Skip length byte in header
6A46: CD AA 6A        CALL    $6AAA               ; {} Skip suggested ...
6A49: CD AA 6A        CALL    $6AAA               ; {} ... load address (7200 for some reason)
6A4C: 01 00 01        LD      BC,$0100            ; 256 bytes to move. Note we never use B in the loop
6A4F: 7D              LD      A,L                 ; Has our pointer maxed at ...
6A50: A7              AND     A                   ; ... location 5D00 (LSB)?
6A51: C2 5A 6A        JP      NZ,$6A5A            ; {} No, copy next byte
6A54: 7C              LD      A,H                 ; Has our pointer maxed at ...
6A55: FE 5D           CP      $5D                 ; ... location 5D00 (MSB)?
6A57: CA 66 6A        JP      Z,$6A66             ; {} Yes, done
6A5A: CD AA 6A        CALL    $6AAA               ; {} Get the next byte from the file
6A5D: 77              LD      (HL),A              ; Store the byte
6A5E: 23              INC     HL                  ; Bump the destination pointer
6A5F: 0D              DEC     C                   ; All 256 bytes moved?
6A60: C2 4F 6A        JP      NZ,$6A4F            ; {} No, go move them all
6A63: C3 3B 6A        JP      $6A3B               ; {} Check/ignore the next block header
;
6A66: 11 06 6B        LD      DE,$6B06            ; FCB for the file we are reading
6A69: CD 28 44        CALL    $4428               ; {hard.CLOSE_FILE} Close the file
6A6C: C2 D0 6A        JP      NZ,$6AD0            ; {} Error closing. We will retry.
;
; ?? describe current room
6A6F: 3A 21 72        LD      A,($7221)           ; {code.currentRoom}
6A72: 47              LD      B,A                 
6A73: 21 00 52        LD      HL,$5200            ; {+ram.sectionData}
6A76: CD A5 61        CALL    $61A5               ; {code.FindCollectionItemByID}
6A79: 22 22 72        LD      ($7222),HL          ; {code.currentRoomPtr}
6A7C: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6A7F: 7E              LD      A,(HL)              
6A80: 32 F0 71        LD      ($71F0),A           ; {code.stopAtPeriod}
6A83: 36 01           LD      (HL),$01            
6A85: 06 01           LD      B,$01               
6A87: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
6A8A: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6A8D: 3A 21 72        LD      A,($7221)           ; {code.currentRoom}
6A90: 77              LD      (HL),A              
6A91: 23              INC     HL                  
6A92: 7E              LD      A,(HL)              
6A93: E6 F0           AND     $F0                 
6A95: 47              LD      B,A                 
6A96: 3A FA 71        LD      A,($71FA)           ; {code.currentLoadedSection}
6A99: B0              OR      B                   
6A9A: 77              LD      (HL),A              
6A9B: CD C1 64        CALL    $64C1               ; {code.PrintObjectsInRoom}
6A9E: 97              SUB     A                   ; Don't stop at first period
6A9F: 32 F0 71        LD      ($71F0),A           ; {code.stopAtPeriod} Print full description
6AA2: 3E 0D           LD      A,$0D               ; Line feed before ...
6AA4: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces} ... user input
6AA7: C3 38 5D        JP      $5D38               ; {code.GameLoop} Back to the user input loop (any script we were running is gone)

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
;
6AD0: 21 48 6B        LD      HL,$6B48            
6AD3: CD 57 63        CALL    $6357               ; {code.ExecuteCommand}
6AD6: 11 06 6B        LD      DE,$6B06            
6AD9: CD 28 44        CALL    $4428               ; {hard.CLOSE_FILE} Close a file overlay
6ADC: CA 08 6A        JP      Z,$6A08             ; {}
6ADF: C3 D0 6A        JP      $6AD0               ; {}

6AE2: 1A              LD      A,(DE)              
6AE3: 13              INC     DE                  
6AE4: C9              RET                         

; name1[/ext1][.password1][:dn1]
;
; SECTION0/DAT
6AE5: 53 45 43 54 49 4F 4E 
sectionLetter:
6AEC: 30 
6AED: 2F 44 41 54 20 20 20 20 20 20 24        
6AF8: 20 20 20 20 20 20 20 20 20 20 20 20 20 20

diskFileControlBlock:
; 32 byte FCB (also called DCB)
6B06: 53 45 43 54 49 4F 4E 30 2F 44 41 54 20 20 20 20 ; SECTION0/DAT
6B16: 20 20 24 20 20 20 20 20 20 20 20 20 20 20 20 20 
6B26: 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 
6B36: 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 

6B46: 20 20 B3

sectorBuffer:
; 256 bytes for disk I/O
6B49: 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF    
6B59: 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF
6B69: 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF
6B79: 00 FF 00 FF 00 FF 00 F9 00 FF 00 FF 00 FF 00 FF
6B89: 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF
6B99: 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF
6BA9: 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF
6BB9: 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF
6BC9: 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF
6BD9: 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF
6BE9: 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF
6BF9: 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF
6C09: 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF
6C19: 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF
6C29: 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF
6C39: 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF 00 FF

COM_14_execute_and_reverse_status:
6C49: CD 57 63        CALL    $6357               ; {code.ExecuteCommand} Execute the requested command
6C4C: C2 52 6C        JP      NZ,$6C52            ; {} Command failed ... reverse it to passed
6C4F: F6 01           OR      $01                 ; Z=0 FAIL
6C51: C9              RET                         
;
6C52: 97              SUB     A                   ; Z=1 PASS
6C53: C9              RET                         

COM_31__:
6C54: E5              PUSH    HL                  
6C55: 2A 18 72        LD      HL,($7218)          ; {}
6C58: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6C5B: 3A 0B 72        LD      A,($720B)           ; {code.varObject}
6C5E: 77              LD      (HL),A              
6C5F: 23              INC     HL                  
6C60: 7E              LD      A,(HL)              
6C61: E6 F0           AND     $F0                 
6C63: 77              LD      (HL),A              
6C64: E1              POP     HL                  
6C65: 97              SUB     A                   ; Z=1 PASS
6C66: C9              RET                         

COM_32__:
6C67: E5              PUSH    HL                  
6C68: 2A 12 72        LD      HL,($7212)          ; {}
6C6B: C3 58 6C        JP      $6C58               ; {}

COM_17_move_to: ; ?? move to
6C6E: 46              LD      B,(HL)              
6C6F: 23              INC     HL                  
6C70: E5              PUSH    HL                  
6C71: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
6C74: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6C77: D1              POP     DE                  
6C78: 1A              LD      A,(DE)              
6C79: 77              LD      (HL),A              
6C7A: 23              INC     HL                  
6C7B: E6 80           AND     $80                 
6C7D: CA 8C 6C        JP      Z,$6C8C             ; {}
6C80: 7E              LD      A,(HL)              
6C81: E6 F0           AND     $F0                 
6C83: 47              LD      B,A                 
6C84: 3A FA 71        LD      A,($71FA)           ; {code.currentLoadedSection}
6C87: B0              OR      B                   
6C88: 77              LD      (HL),A              
6C89: C3 90 6C        JP      $6C90               ; {}
;
6C8C: 7E              LD      A,(HL)              
6C8D: E6 F0           AND     $F0                 
6C8F: 77              LD      (HL),A              
6C90: EB              EX      DE,HL               
6C91: 23              INC     HL                  
6C92: 97              SUB     A                   ; Z=1 PASS
6C93: C9              RET                         

COM_18_is_var_owned_by_active:
6C94: E5              PUSH    HL                  
6C95: 2A 0C 72        LD      HL,($720C)          ; {code.varObjectPtr}
6C98: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6C9B: 46              LD      B,(HL)              
6C9C: 78              LD      A,B                 
6C9D: A7              AND     A                   
6C9E: E1              POP     HL                  
6C9F: CA 6D 60        JP      Z,$606D             ; {}
6CA2: 3A 1E 72        LD      A,($721E)           ; {code.activeObject}
6CA5: B8              CP      B                   
6CA6: C8              RET     Z                   
6CA7: 78              LD      A,B                 
6CA8: E6 80           AND     $80                 
6CAA: C0              RET     NZ                  

6CAB: E5              PUSH    HL                  
6CAC: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
6CAF: C3 98 6C        JP      $6C98               ; {}

6CB2: 21 7A 88        LD      HL,$887A            
6CB5: 97              SUB     A                   
6CB6: 32 1C 72        LD      ($721C),A           ; {}
6CB9: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6CBC: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE}
6CBF: D0              RET     NC                  
6CC0: 3A 1C 72        LD      A,($721C)           ; {}
6CC3: 3C              INC     A                   
6CC4: 32 1C 72        LD      ($721C),A           ; {}
6CC7: D5              PUSH    DE                  
6CC8: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6CCB: 4E              LD      C,(HL)              
6CCC: D5              PUSH    DE                  
6CCD: 7E              LD      A,(HL)              
6CCE: A7              AND     A                   
6CCF: CA 46 6D        JP      Z,$6D46             ; {}
6CD2: E6 80           AND     $80                 
6CD4: C2 F6 6C        JP      NZ,$6CF6            ; {}
6CD7: E5              PUSH    HL                  
6CD8: 46              LD      B,(HL)              
6CD9: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
6CDC: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
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
6CFB: 3A FA 71        LD      A,($71FA)           ; {code.currentLoadedSection}
6CFE: B8              CP      B                   
6CFF: C2 46 6D        JP      NZ,$6D46            ; {}
6D02: 23              INC     HL                  
6D03: 23              INC     HL                  
6D04: 06 08           LD      B,$08               ; EVERY_TURN section
6D06: CD AD 61        CALL    $61AD               ; {code.FindObjectField}
6D09: D2 46 6D        JP      NC,$6D46            ; {}
6D0C: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6D0F: E5              PUSH    HL                  
6D10: CD C6 71        CALL    $71C6               ; {code.COM_2B_random}
6D13: 3A 1C 72        LD      A,($721C)           ; {}
6D16: 32 1E 72        LD      ($721E),A           ; {code.activeObject}
6D19: 47              LD      B,A                 
6D1A: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
6D1D: 22 1F 72        LD      ($721F),HL          ; {code.activeObjectPtr}
6D20: 79              LD      A,C                 
6D21: A7              AND     A                   
6D22: FA 35 6D        JP      M,$6D35             ; {}
6D25: 47              LD      B,A                 
6D26: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
6D29: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6D2C: 7E              LD      A,(HL)              
6D2D: A7              AND     A                   
6D2E: C2 21 6D        JP      NZ,$6D21            ; {}
6D31: E1              POP     HL                  
6D32: C3 46 6D        JP      $6D46               ; {}
6D35: 32 21 72        LD      ($7221),A           ; {code.currentRoom}
6D38: 21 00 52        LD      HL,$5200            ; {+ram.sectionData}
6D3B: 47              LD      B,A                 
6D3C: CD A5 61        CALL    $61A5               ; {code.FindCollectionItemByID}
6D3F: 22 22 72        LD      ($7222),HL          ; {code.currentRoomPtr}
6D42: E1              POP     HL                  
6D43: CD 57 63        CALL    $6357               ; {code.ExecuteCommand}
6D46: E1              POP     HL                  
6D47: D1              POP     DE                  
6D48: C3 BC 6C        JP      $6CBC               ; {}

COM_05_is_less_equal_last_random:
6D4B: 3A EC 71        LD      A,($71EC)           ; {code.RandomSeed2}
6D4E: BE              CP      (HL)                ; Compare to target value
6D4F: 23              INC     HL                  ; Bump the script pointer
6D50: DA 59 6D        JP      C,$6D59             ; {} If less, return 0
6D53: CA 59 6D        JP      Z,$6D59             ; {} If same, return 0
;
6D56: F6 01           OR      $01                 ; Z=0 FAIL
6D58: C9              RET                         
;
6D59: 97              SUB     A                   ; Z=1 PASS
6D5A: C9              RET                         

COM_1D_attack_VAR:
6D5B: 4E              LD      C,(HL)              
6D5C: 23              INC     HL                  
6D5D: E5              PUSH    HL                  
6D5E: 2A 0C 72        LD      HL,($720C)          ; {code.varObjectPtr}
6D61: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6D64: 23              INC     HL                  
6D65: 23              INC     HL                  
6D66: 23              INC     HL                  
6D67: E5              PUSH    HL                  
6D68: D5              PUSH    DE                  
6D69: 06 09           LD      B,$09               ; HIT_POINTS section
6D6B: CD AD 61        CALL    $61AD               ; {code.FindObjectField}
6D6E: D2 96 6D        JP      NC,$6D96            ; {}
6D71: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
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
6D82: 97              SUB     A                   ; Z=1 PASS
6D83: E1              POP     HL                  
6D84: C9              RET                         
6D85: 06 0A           LD      B,$0A               ; UPON_DEATH section
6D87: CD AD 61        CALL    $61AD               ; {code.FindObjectField}
6D8A: D2 82 6D        JP      NC,$6D82            ; {}
6D8D: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6D90: CD 57 63        CALL    $6357               ; {code.ExecuteCommand}
6D93: C3 82 6D        JP      $6D82               ; {}
6D96: D1              POP     DE                  
6D97: E1              POP     HL                  
6D98: C3 82 6D        JP      $6D82               ; {}

COM_1E_swap:
6D9B: 46              LD      B,(HL)              
6D9C: 23              INC     HL                  
6D9D: 4E              LD      C,(HL)              
6D9E: 23              INC     HL                  
6D9F: E5              PUSH    HL                  
6DA0: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
6DA3: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6DA6: 5E              LD      E,(HL)              
6DA7: 41              LD      B,C                 
6DA8: E5              PUSH    HL                  
6DA9: D5              PUSH    DE                  
6DAA: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
6DAD: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6DB0: D1              POP     DE                  
6DB1: 7E              LD      A,(HL)              
6DB2: 73              LD      (HL),E              
6DB3: E1              POP     HL                  
6DB4: 77              LD      (HL),A              
6DB5: E1              POP     HL                  
6DB6: 97              SUB     A                   ; Z=1 PASS
6DB7: C9              RET                         

COM_22__:
6DB8: 4E              LD      C,(HL)              
6DB9: 23              INC     HL                  
6DBA: E5              PUSH    HL                  
6DBB: 2A 0C 72        LD      HL,($720C)          ; {code.varObjectPtr}
6DBE: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6DC1: 23              INC     HL                  
6DC2: 23              INC     HL                  
6DC3: 23              INC     HL                  
6DC4: 06 09           LD      B,$09               ; HIT_POINTS section
6DC6: CD AD 61        CALL    $61AD               ; {code.FindObjectField}
6DC9: D2 D8 6D        JP      NC,$6DD8            ; {}
6DCC: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6DCF: 23              INC     HL                  
6DD0: 7E              LD      A,(HL)              
6DD1: B9              CP      C                   
6DD2: DA DC 6D        JP      C,$6DDC             ; {}
6DD5: CA DC 6D        JP      Z,$6DDC             ; {}
6DD8: E1              POP     HL                  
6DD9: F6 01           OR      $01                 ; Z=0 FAIL
6DDB: C9              RET                         
;
6DDC: 97              SUB     A                   ; Z=1 PASS
6DDD: E1              POP     HL                  
6DDE: C9              RET                         

COM_23_heal_var:
6DDF: 4E              LD      C,(HL)              
6DE0: 23              INC     HL                  
6DE1: E5              PUSH    HL                  
6DE2: 2A 0C 72        LD      HL,($720C)          ; {code.varObjectPtr}
6DE5: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6DE8: 23              INC     HL                  
6DE9: 23              INC     HL                  
6DEA: 23              INC     HL                  
6DEB: 06 09           LD      B,$09               ; HIT_POINTS section
6DED: CD AD 61        CALL    $61AD               ; {code.FindObjectField}
6DF0: D2 DC 6D        JP      NC,$6DDC            ; {}
6DF3: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6DF6: 56              LD      D,(HL)              
6DF7: 23              INC     HL                  
6DF8: 7E              LD      A,(HL)              
6DF9: 81              ADD     A,C                 
6DFA: BA              CP      D                   
6DFB: DA FF 6D        JP      C,$6DFF             ; {}
6DFE: 7A              LD      A,D                 
6DFF: 77              LD      (HL),A              
6E00: C3 DC 6D        JP      $6DDC               ; {}

COM_25_print_linefeed:
6E03: 3A 1E 72        LD      A,($721E)           ; {code.activeObject} Is the player ...
6E06: FE 01           CP      $01                 ; ... the active object?
6E08: C2 10 6E        JP      NZ,$6E10            ; {} No, ignore line feed
6E0B: 3E 0D           LD      A,$0D               ; Print ...
6E0D: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces} ... line feed
6E10: 97              SUB     A                   ; Z=1 PASS
6E11: C9              RET                         

COM_36__: ; ??
6E12: E5              PUSH    HL                  
6E13: 2A 0C 72        LD      HL,($720C)          ; {code.varObjectPtr}
6E16: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6E19: 7E              LD      A,(HL)              
6E1A: E6 80           AND     $80                 
6E1C: C2 3E 6E        JP      NZ,$6E3E            ; {}
6E1F: 46              LD      B,(HL)              
6E20: 48              LD      C,B                 
6E21: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
6E24: 54              LD      D,H                 
6E25: 5D              LD      E,L                 
6E26: D5              PUSH    DE                  
6E27: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6E2A: D1              POP     DE                  
6E2B: 23              INC     HL                  
6E2C: 7E              LD      A,(HL)              
6E2D: E6 20           AND     $20                 
6E2F: CA 3E 6E        JP      Z,$6E3E             ; {}
6E32: 79              LD      A,C                 
6E33: 32 0B 72        LD      ($720B),A           ; {code.varObject}
6E36: EB              EX      DE,HL               
6E37: 22 0C 72        LD      ($720C),HL          ; {code.varObjectPtr}
6E3A: E1              POP     HL                  
6E3B: F6 01           OR      $01                 ; Z=0 FAIL
6E3D: C9              RET                         
6E3E: E1              POP     HL                  
6E3F: 97              SUB     A                   ; Z=1 PASS
6E40: C9              RET                         

COM_24_end_program:
6E41: C3 2D 40        JP      $402D               ; {hard.EndProgram} Exit program normally

COM_28__:
6E44: 3E 55           LD      A,$55               ; "U" prefix
6E46: 32 4F 6F        LD      ($6F4F),A           ; {}
6E49: 3E 39           LD      A,$39               ; 4439 - WRITE RECORD
6E4B: 32 1E 6F        LD      ($6F1E),A           ; {}
6E4E: 3E 20           LD      A,$20               ; 4420 - OPEN EXISTING
6E50: 32 03 6F        LD      ($6F03),A           ; {}
6E53: E5              PUSH    HL                  
6E54: 06 92           LD      B,$92               ; Look up ...
6E56: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex} ... score object
6E59: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd} Skip to data
6E5C: 23              INC     HL                  ; Second byte of data
6E5D: 3A FA 71        LD      A,($71FA)           ; {code.currentLoadedSection} Write section number ...
6E60: 77              LD      (HL),A              ; ... to the score object
6E61: 06 9B           LD      B,$9B               ; ?? Object 9B ??
6E63: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
6E66: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6E69: 77              LD      (HL),A              ; ?? loaded section number to ??
6E6A: C3 DA 6E        JP      $6EDA               ; {}

COM_27__:
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
6E87: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
6E8A: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6E8D: 7E              LD      A,(HL)              
6E8E: 06 01           LD      B,$01               
6E90: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
6E93: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6E96: 7E              LD      A,(HL)              
6E97: E6 80           AND     $80                 
6E99: 7E              LD      A,(HL)              
6E9A: C2 A5 6E        JP      NZ,$6EA5            ; {}
6E9D: 46              LD      B,(HL)              
6E9E: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
6EA1: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6EA4: 7E              LD      A,(HL)              
6EA5: 32 21 72        LD      ($7221),A           ; {code.currentRoom}
6EA8: 06 92           LD      B,$92               
6EAA: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex}
6EAD: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
6EB0: 23              INC     HL                  
6EB1: 3A FA 71        LD      A,($71FA)           ; {code.currentLoadedSection}
6EB4: BE              CP      (HL)                ; Is the target disk sction already loaded?
6EB5: CA 6F 6A        JP      Z,$6A6F             ; {} Yes ... go print the room description
6EB8: C3 FE 69        JP      $69FE               ; {code.COM_2F_load_disk_section} No ... load the section and print description

COM_34__:
6EBB: 3E 20           LD      A,$20               ; 4420 - OPEN EXISTING
6EBD: 32 03 6F        LD      ($6F03),A           ; {}
6EC0: 3E 39           LD      A,$39               ; 4439 - WRITE RECORD
6EC2: C3 CC 6E        JP      $6ECC               ; {}

COM_35__:
6EC5: 3E 24           LD      A,$24               ; 4424 - OPEN NEW OR EXISTING
6EC7: 32 03 6F        LD      ($6F03),A           ; {}
6ECA: 3E 36           LD      A,$36               ; 4436 - READ RECORD
;
6ECC: 32 1E 6F        LD      ($6F1E),A           ; {}
6ECF: 3E 53           LD      A,$53               ; "S" prefix
6ED1: 32 4F 6F        LD      ($6F4F),A           ; {}
6ED4: E5              PUSH    HL                  
6ED5: 3E 30           LD      A,$30               
6ED7: 32 A2 6F        LD      ($6FA2),A           ; {}
;
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
;
;
;
; Various spots in the code change the LSB of this call. Interesting
;
6F02: CD 20 44        CALL    $4420               ; {hard.OPEN_NEW_EXISTING} Open new or existing
6F05: C2 47 6F        JP      NZ,$6F47            ; {}
6F08: 21 7A 88        LD      HL,$887A            ; Object data
6F0B: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd} Pointer to player object
6F0E: D5              PUSH    DE                  ; Hold
6F0F: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd} Pointer to player data
6F12: D5              PUSH    DE                  ; Hold
6F13: 23              INC     HL                  ; Pointer ...
6F14: 23              INC     HL                  ; ... to ...
6F15: 23              INC     HL                  ; ... upon death script
6F16: E5              PUSH    HL                  ; Hold it
6F17: 2B              DEC     HL                  ; Back ...
6F18: 2B              DEC     HL                  ; ... to ...
6F19: 2B              DEC     HL                  ; ... player data
6F1A: 11 62 6F        LD      DE,$6F62            
6F1D: CD 39 44        CALL    $4439               ; {hard.WRITE_RECORD}
6F20: C2 47 6F        JP      NZ,$6F47            ; {}
6F23: E1              POP     HL                  
6F24: D1              POP     DE                  
6F25: D5              PUSH    DE                  
6F26: 06 09           LD      B,$09               ; HIT_POINTS section
6F28: CD AD 61        CALL    $61AD               ; {code.FindObjectField}
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
6F45: 97              SUB     A                   ; Z=1 PASS
6F46: C9              RET                         
;
6F47: F6 80           OR      $80                 ; DOS prints the error and returns here
6F49: CD 09 44        CALL    $4409               ; {hard.ERROR_SYS4} Print the disk error
6F4C: C3 38 5D        JP      $5D38               ; {code.GameLoop} Restart the game loop

6F4F: 53          ; SSVDOBJS/DAT
6F50: 53                         
6F51: 56                       
6F52: 44                             
6F53: 4F                             
6F54: 42                              
6F55: 4A                             
6F56: 53                             
6F57: 2F                                     
6F58: 44                              
6F59: 41                            
6F5A: 54                           
6F5B: 20 20                      
6F5D: 20                            
6F5E: 20                          
6F5F: 20 20 

6F61: 24
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
6F82: 20 20           JR      NZ,$6FA4            ; {code.PrintAsciiString}
6F84: 20 20           JR      NZ,$6FA6            ; {}
6F86: 20 20           JR      NZ,$6FA8            ; {}
6F88: 20 20           JR      NZ,$6FAA            ; {}
6F8A: 20 20           JR      NZ,$6FAC            ; {}
6F8C: 20 20           JR      NZ,$6FAE            ; {}
6F8E: 20 20           JR      NZ,$6FB0            ; {code.COM_26_print_score}
6F90: 20 20           JR      NZ,$6FB2            ; {}
6F92: 20 20           JR      NZ,$6FB4            ; {}
6F94: 20 20           JR      NZ,$6FB6            ; {}
6F96: 20 20           JR      NZ,$6FB8            ; {}
6F98: 20 20           JR      NZ,$6FBA            ; {}
6F9A: 20 20           JR      NZ,$6FBC            ; {}
6F9C: 20 20           JR      NZ,$6FBE            ; {}
6F9E: 20 20           JR      NZ,$6FC0            ; {}
6FA0: 20 20           JR      NZ,$6FC2            ; {}
6FA2: 30 00           JR      NC,$6FA4            ; {code.PrintAsciiString}

PrintAsciiString: ; Doesn't seem to be called
; DE points to null-terminated string
6FA4: 1A              LD      A,(DE)              ; Get the next character
6FA5: A7              AND     A                   ; End of list?
6FA6: C8              RET     Z                   ; Yes ... done
6FA7: D5              PUSH    DE                  ; Hold the pointer
6FA8: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces} Print the character
6FAB: D1              POP     DE                  ; Restore
6FAC: 13              INC     DE                  ; Point to next character
6FAD: C3 A4 6F        JP      $6FA4               ; {code.PrintAsciiString} Do all characters

COM_26_print_score:
; Score is kept in a BCD nibble printed as "X0" with a trailing 0.
; Thus score is "00", "10", "20", "30", etc
6FB0: E5              PUSH    HL                  ; Hold
6FB1: 06 92           LD      B,$92               ; Look up the ...
6FB3: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex} ... score object
6FB6: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd} Skip to data
6FB9: 7E              LD      A,(HL)              ; Get the score value
6FBA: 32 FB 71        LD      ($71FB),A           ; {} Hold on to score value ?? why
6FBD: 3A FB 71        LD      A,($71FB)           ; {} Get score value
6FC0: E6 0F           AND     $0F                 ; Kepp lower nibble
6FC2: C6 30           ADD     $30                 ; Convert to number
6FC4: 47              LD      B,A                 ; Print ...
6FC5: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces} ... digit
6FC8: 3E 00           LD      A,$00               ; Number 0
6FCA: E6 0F           AND     $0F                 ; Maybe there was a 2nd digit at one time?
6FCC: C6 30           ADD     $30                 ; Convert to number
6FCE: 47              LD      B,A                 ; Print ...
6FCF: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces} ... trailing zero
6FD2: 3E 20           LD      A,$20               ; Print ...
6FD4: 47              LD      B,A                 ; ... trailing ...
6FD5: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces} ... space on end
6FD8: E1              POP     HL                  ; Restore
6FD9: 97              SUB     A                   ; Z=1 PASS
6FDA: C9              RET                         

COM_38_bump_score:
6FDB: E5              PUSH    HL                  ; Hold
6FDC: 06 92           LD      B,$92               ; Look up ...
6FDE: CD 57 70        CALL    $7057               ; {code.GetObjectScriptByIndex} ... the score object
6FE1: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd} Skip to data
6FE4: 7E              LD      A,(HL)              ; Current score nibble
6FE5: C6 01           ADD     $01                 ; Bump the score
6FE7: 27              DAA                         ; Adjust for BCD
6FE8: 77              LD      (HL),A              ; Store new score
6FE9: E1              POP     HL                  ; Restore
6FEA: 97              SUB     A                   ; Z=1 PASS
6FEB: C9              RET                         

COM_39_check_weight_70: ; Never used
; PASS if weight is 70 or less
; FAIL if too heavy
6FEC: E5              PUSH    HL                  ; Hold script
6FED: 21 7A 88        LD      HL,$887A            ; {+code.ObjectData} Run the list of objects
6FF0: 97              SUB     A                   ; Total weight ...
6FF1: 32 1C 72        LD      ($721C),A           ; {} ... in backpack
6FF4: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd} Skip to ...
6FF7: CD DC 61        CALL    $61DC               ; {code.CompareHLandDE} ... first object
6FFA: D2 E9 6F        JP      NC,$6FE9            ; {} All objects added, PASS
6FFD: D5              PUSH    DE                  ; Hold end of script
6FFE: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd} Skip to object's data
7001: 7E              LD      A,(HL)              ; Object's location
7002: FE 01           CP      $01                 ; Is object in player's backpack?
7004: C2 23 70        JP      NZ,$7023            ; {} No, ignore this object
7007: 23              INC     HL                  ; Skip ...
7008: 23              INC     HL                  ; ... over ...
7009: 23              INC     HL                  ; ... object base data
700A: 06 0C           LD      B,$0C               ; WEIGHT section
700C: CD AD 61        CALL    $61AD               ; {code.FindObjectField} Find the weight
700F: D2 23 70        JP      NC,$7023            ; {} This object has no weight, ignore it
7012: D5              PUSH    DE                  ; Hold end of object
7013: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd}
7016: 3A 1C 72        LD      A,($721C)           ; {} Add ...
7019: 86              ADD     A,(HL)              ; ... this weight ...
701A: 32 1C 72        LD      ($721C),A           ; {} ... to running total
701D: D1              POP     DE                  ; Restore end of object
701E: FE 47           CP      $47                 ; 70 or less?
7020: D2 28 70        JP      NC,$7028            ; {} No, FAIL weight check
;
7023: EB              EX      DE,HL               ; Point to next object
7024: D1              POP     DE                  ; Restore end of script
7025: C3 F7 6F        JP      $6FF7               ; {} Next object
;
7028: D1              POP     DE                  ; Restore end of script
7029: E1              POP     HL                  ; Restore script pointer
702A: F6 01           OR      $01                 ; Z=0 FAIL
702C: C9              RET                         

COM_3A_clear_screen:
702D: E5              PUSH    HL                  ; Hold script pointer
702E: 21 00 3C        LD      HL,$3C00            ; Start of screen
7031: 11 00 04        LD      DE,$0400            ; Number of bytes on the screen
7034: 36 20           LD      (HL),$20            ; Set character ...
7036: 23              INC     HL                  ; ... to space
7037: 1B              DEC     DE                  ; Dec the count
7038: 7A              LD      A,D                 ; Counter ...
7039: B3              OR      E                   ; ... reached zero?
703A: C2 34 70        JP      NZ,$7034            ; {} No ... clear the whole screen
703D: E1              POP     HL                  ; Restore script pointer
703E: 97              SUB     A                   ; Z=1 PASS
703F: C9              RET                         

COM_3B_wait_for_key_123:
7040: E5              PUSH    HL                  ; Hold script pointer
7041: CD 99 62        CALL    $6299               ; {code.GetKey} Wait for a key
7044: FE 30           CP      $30                 ; Less than "0"?
7046: DA 41 70        JP      C,$7041             ; {} Yes ... ignore
7049: FE 34           CP      $34                 ; Less than "4"
704B: D2 41 70        JP      NC,$7041            ; {} No ... ignore
704E: 32 A2 6F        LD      ($6FA2),A           ; {} Hold the player's choice
7051: CD EB 70        CALL    $70EB               ; {code.PrintCharCullSpaces} Print the player's choice
7054: E1              POP     HL                  ; Restore script pointer
7055: 97              SUB     A                   ; Z=1 PASS
7056: C9              RET                         

GetObjectScriptByIndex:
; B is object index
; Return pointer to object in HL
7057: 21 7A 88        LD      HL,$887A            ; Object scripts
705A: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd} Start to HL, End to DE
705D: 05              DEC     B                   ; Is this the index we want?
705E: C8              RET     Z                   ; Yes ... done
705F: CD C8 61        CALL    $61C8               ; {code.SkipIDCalcEnd} Find end of this object
7062: EB              EX      DE,HL               ; Move to the end
7063: C3 5D 70        JP      $705D               ; {} Keep looking

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
7096: 3A 20 40        LD      A,($4020)           ; {hard.CursorPointer}
7099: FE FB           CP      $FB                 
709B: DA 7F 70        JP      C,$707F             ; {}
709E: E5              PUSH    HL                  
709F: 2A 20 40        LD      HL,($4020)          ; {hard.CursorPointer}
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
70E2: 21 9A BF        LD      HL,$BF9A            ; This is past all calculated string ends.
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
7108: 2A 20 40        LD      HL,($4020)          ; {hard.CursorPointer} Back screen ...
710B: 2B              DEC     HL                  ; ... pointer up ...
710C: 22 20 40        LD      ($4020),HL          ; {hard.CursorPointer} ... over ignored space
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
71E4: 97              SUB     A                   ; Z=1 PASS
71E5: E1              POP     HL                  ; 
71E6: C1              POP     BC                  ; 
71E7: C9              RET                         

RandomSeed1:
71E8: 12 23 44 1D       ; Exact same seed from Bedlam
RandomSeed2:
71EC: 27 4D 2D 13

stopAtPeriod:
71F0: 00  ;  0 means print all. non-zero means stop printing after first period (short description of room)

71F1: 00                         
71F2: 00                         
71F3: 00                         
71F4: 00                         
71F5: 00                         
71F6: 00                         
71F7: 00                         
71F8: 00                         
71F9: 00

currentLoadedSection:                 
71FA: 00 ; the currently loaded sction number (1-9)            

71FB: 00 ; Score is written here during print                        
71FC: 00                         
71FD: 00                         
71FE: 00                         
71FF: 00                         

; Section data loads here ??

7200: 00                         
7201: 00                         
7202: 00                         
7203: 00                         
7204: 00                         
7205: 00                         
7206: 00                         
7207: 00                         
7208: 00                         
7209: 00                         

lastChar:
720A: 00  ; last character printed

varObject:
720B: 00     
varObjectPtr:
720C: 00 00

720E: 00                    
720F: 00                      
7210: 00                     
7211: 00                         
7212: 00                         
7213: 00                         
7214: 00                         
7215: 00                         
7216: 00                         
7217: 00                         
7218: 00                         
7219: 00                         
721A: 00                         
721B: 00                         
721C: 00                         
721D: 00

activeObject:
721E: 01 ; 1=player, 38=system
activeObjectPtr:
721F: 00 00

currentRoom: 
7221: 81          ; we start in room 81
currentRoomPtr:
7222: 03 52       ; 5203 is first room loaded from SECTION1.DAT

7224: 48              LD      C,B                 
7225: 72              LD      (HL),D              
7226: 00                         
7227: 00                         
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

;?? input tokens input buffer
7247: D4 00
7249: 00
724A: 00                         
724B: 00                         
724C: 00                         
724D: 00                         
724E: 00                         
724F: 00                         
7250: 00                         
7251: 00                         
7252: 00                         
7253: 00                         
7254: 00                         
7255: 00                         
7256: 00                         
7257: 00                         
7258: 00                         
7259: 00                         
725A: 00                         
725B: 00                         
725C: 00                         
725D: 00                         
725E: 00                         
725F: 00                         
7260: 00                         
7261: 00                         
7262: 00                         
7263: 00                         
7264: 00                         
7265: 00


InitScript:
7266: 94  ; Initialization script (Load SECTION1.DAT)           

SplashMessage: 
7267: A3  ; Print ">>>> XENOS <<<<" and "STRANGER, BEWARE!"

CommandJumpTable:
7268: DC 63        ; COM_00_move_ACTIVE_and_look(room_num)
726A: 7E 67        ; COM_01_is_in_pack_or_current_room(obj_num)
726C: C5 67        ; COM_02_is_owned(obj_num)
726E: CA 67        ; COM_03_is_located(room_num, obj_num)
7270: DF 67        ; COM_04_print_message(mlength)
7272: 4B 6D        ; COM_05_is_less_equal_last_random(value)
7274: 0D 68        ; COM_06_print_inventory()
7276: 05 68        ; COM_07_print_room_description()
7278: 80 68        ; COM_08_is_first_noun(word_num)
727A: AA 68        ; COM_09_compare_to_second_noun(word_num)
727C: BE 68        ; COM_0A_is_input_phrase(phrase_num)
727E: B7 63        ; COM_0B_switch(mlength, com_num)
7280: DC 67        ; COM_0C_fail()
7282: 8A 63        ; COM_0D_while_pass(mlength)
7284: A0 63        ; COM_0E_while_fail(mlength)
7286: C5 68        ; COM_0F__ ?? pick up var
7288: EF 68        ; COM_10_drop_var()
728A: 6F 69        ; COM_11_print_first_noun()
728C: 9C 69        ; COM_12_print_second_noun()
728E: 07 69        ; COM_13_process_phrase_by_room_first_second()
7290: 49 6C        ; COM_14_execute_and_reverse_status()
7292: A6 69        ; COM_15_check_var()
7294: 65 69        ; COM_16_print_var()
7296: 6E 6C        ; COM_17_move_to()
7298: 94 6C        ; COM_18_is_var_owned_by_active()
729A: F5 63        ; COM_19_move_ACTIVE(room_num) ?? player is the only active?
729C: 2C 64        ; COM_1A_set_var_to_first_noun()
729E: 3C 64        ; COM_1B_set_var_to_second_noun()
72A0: 4C 64        ; COM_1C_set_var_object(obj_num)
72A2: 5B 6D        ; COM_1D_attack_VAR(points)
72A4: 9B 6D        ; COM_1E_swap(obj_num1, obj_num2)
72A6: EC 67        ; COM_1F_print2(mlength)
72A8: 89 67        ; COM_20_is_active_this(obj_num)
72AA: 60 64        ; COM_21_execute_phrase(phrase_num, first_noun_num, second_noun_num)
72AC: B8 6D        ; COM_22__is_less_equal_health(points)
72AE: DF 6D        ; COM_23_heal_var(points)
72B0: 41 6E        ; COM_24_end_program()
72B2: 03 6E        ; COM_25_print_linefeed()
72B4: B0 6F        ; COM_26_print_score()
72B6: 6D 6E        ; COM_27__ ??
72B8: 44 6E        ; COM_28__ ??
72BA: D2 69        ; COM_29_print_open_var() ?? toggle_open_VAR()
72BC: E8 69        ; COM_2A__ ?? toggle_lock_VAR()
72BE: C6 71        ; COM_2B_random()
72C0: 8F 67        ; COM_2C_set_active(obj_num)
72C2: B4 68        ; COM_2D__ ?? is_VAR(object)
;
72C4: C1 69        ; COM_2E__ ??
72C6: FE 69        ; COM_2F_load_disk_section(section_num)
72C8: BE 67        ; COM_30_set_current_room(room_num)
72CA: 54 6C        ; COM_31__ ??
72CC: 67 6C        ; COM_32__ ??
72CE: 80 65        ; COM_33__ ??
72D0: BB 6E        ; COM_34__ ??
72D2: C5 6E        ; COM_35__ ??
72D4: 12 6E        ; COM_36__ ??
72D6: 12 64        ; COM_37__ ??
72D8: DB 6F        ; COM_38_bump_score()
72DA: EC 6F        ; COM_39_check_weight_70() Never used
72DC: 2D 70        ; 3A_clear_screen()
72DE: 40 70        ; COM_3B_wait_for_key_123()
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

DieEnergyBeamCommand:
762B: CA ; DIE_ENERGY_BEAM routine

KnownWords:
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

GeneralScript:
7D4E: 00 8B 29        ; End+1 = 887A
;
7D51: 0E 8B 26                           ; COM_0E_while_fail length=0x0B26
7D54:    0D 3F                           ;   COM_0D_while_pass length=0x003F
7D56:       0E 08                        ;     COM_0E_while_fail length=0x0008
7D58:          0A 01                     ;       COM_0A_is_input_phrase(phrase=NORTH * * *)
7D5A:          0A 02                     ;       COM_0A_is_input_phrase(phrase=SOUTH * * *)
7D5C:          0A 03                     ;       COM_0A_is_input_phrase(phrase=EAST * * *)
7D5E:          0A 04                     ;       COM_0A_is_input_phrase(phrase=WEST * * *)
7D60:       0E 33                        ;     COM_0E_while_fail length=0x0033
7D62:          0D 20                     ;       COM_0D_while_pass length=0x0020
7D64:             14                     ;         COM_14_execute_and_reverse_status next command
7D65:             37                     ;         UNKNOWN37
7D66:             0E 1C                  ;         COM_0E_while_fail length=0x001C
7D68:                13                  ;           UNKNOWN13
7D69:                0D 19               ;           COM_0D_while_pass length=0x0019
7D6B:                   20 01            ;             COM_20_is_active_this(obj=OBJ_01_PLAYER)
7D6D:                   04 15            ;             COM_04_print_command length=0x0015
7D6F:                      C7 DE F3 17 CB 8C CF 47 F5 8B D3 B8 D0 15 6B BF ; 
7D7F:                      59 45 46 48 2E ; 
;
;                          YOU WALK AIMLESSLY INTO A WALL.
;
7D84:          0D 0F                     ;       COM_0D_while_pass length=0x000F
7D86:             04 0B                  ;         COM_04_print_command length=0x000B
7D88:                C7 DE 94 14 55 5E 8E BE 0B 8A 4E ; 
;
;                    YOU ARE STILL IN
;
7D93:             AA                     ;         FN_AA_PRINT_THE_var
7D94:             8B                     ;         FN_8B_PRINT_PERIOD
7D95:    0B 8A E2 0A                     ;   COM_0B_switch length=0x0AE2, function=COM_0A_is_input_phrase(phrase_num)
7D99:       05                           ;     COM_0A_is_input_phrase("GET ..C..... * *")
7D9A:       0A                           ;     ELSE goto=0x7DA5
7D9B:          0E 08                     ;       COM_0E_while_fail length=0x0008
7D9D:             A2                     ;         FN_A2_PRINT_ALREADY_HAVE_THE_var
7D9E:             13                     ;         UNKNOWN13
7D9F:             0D 02                  ;         COM_0D_while_pass length=0x0002
7DA1:                1A                  ;           COM_1A_set_var_to_first_noun()
7DA2:                8F                  ;           FN_8F_TRY_TO_GET_OBJECT
7DA3:             14                     ;         COM_14_execute_and_reverse_status next command
7DA4:             0C                     ;         COM_0C_fail()
7DA5:       43                           ;     COM_0A_is_input_phrase("GET ..C..... WITH ..C.....")
7DA6:       0D                           ;     ELSE goto=0x7DB4
7DA7:          0E 0B                     ;       COM_0E_while_fail length=0x000B
7DA9:             A2                     ;         FN_A2_PRINT_ALREADY_HAVE_THE_var
7DAA:             13                     ;         UNKNOWN13
7DAB:             0D 03                  ;         COM_0D_while_pass length=0x0003
7DAD:                1B                  ;           COM_1B_set_var_to_second_noun()
7DAE:                14                  ;           COM_14_execute_and_reverse_status next command
7DAF:                8F                  ;           FN_8F_TRY_TO_GET_OBJECT
7DB0:             0D 02                  ;         COM_0D_while_pass length=0x0002
7DB2:                1A                  ;           COM_1A_set_var_to_first_noun()
7DB3:                8F                  ;           FN_8F_TRY_TO_GET_OBJECT
7DB4:       06                           ;     COM_0A_is_input_phrase("DROP ..C..... * *")
7DB5:       23                           ;     ELSE goto=0x7DD9
7DB6:          0E 21                     ;       COM_0E_while_fail length=0x0021
7DB8:             13                     ;         UNKNOWN13
7DB9:             0D 13                  ;         COM_0D_while_pass length=0x0013
7DBB:                1A                  ;           COM_1A_set_var_to_first_noun()
7DBC:                14                  ;           COM_14_execute_and_reverse_status next command
7DBD:                15 20               ;           COM_15_check_var(value=0x20)
7DBF:                04 0B               ;           COM_04_print_command length=0x000B
7DC1:                   89 74 D3 14 9B 96 1B A1 F9 5B 50 ; 
;
;                       HOW CAN YOU DROP
;
7DCC:                A8                  ;           FN_A8_PRINT_noun1
7DCD:                8B                  ;           FN_8B_PRINT_PERIOD
7DCE:             0D 09                  ;         COM_0D_while_pass length=0x0009
7DD0:                10                  ;           COM_10_drop_var()
7DD1:                04 06               ;           COM_04_print_command length=0x0006
7DD3:                   F9 5B 9F A6 9B 5D ; 
;
;                       DROPPED. 
;
7DD9:       08                           ;     COM_0A_is_input_phrase("READ .....?.. * *")
7DDA:       17                           ;     ELSE goto=0x7DF2
7DDB:          0E 15                     ;       COM_0E_while_fail length=0x0015
7DDD:             13                     ;         UNKNOWN13
7DDE:             0D 12                  ;         COM_0D_while_pass length=0x0012
7DE0:                04 0E               ;           COM_04_print_command length=0x000E
7DE2:                   5F BE 5D B1 D0 B5 D9 9C 16 B2 91 7A C0 16 ; 
;
;                       THERE'S NO WRITING ON
;
7DF0:                A8                  ;           FN_A8_PRINT_noun1
7DF1:                8B                  ;           FN_8B_PRINT_PERIOD
7DF2:       11                           ;     COM_0A_is_input_phrase("OPEN u....... * *")
7DF3:       15                           ;     ELSE goto=0x7E09
7DF4:          0E 13                     ;       COM_0E_while_fail length=0x0013
7DF6:             13                     ;         UNKNOWN13
7DF7:             92                     ;         FN_92_PRINT_TRIED_BUT_COULDNT
7DF8:             0D 0D                  ;         COM_0D_while_pass length=0x000D
7DFA:                1A                  ;           COM_1A_set_var_to_first_noun()
7DFB:                2E 40               ;           UNKNOWN2E, Value: 0x40
7DFD:                A8                  ;           FN_A8_PRINT_noun1
7DFE:                04 07               ;           COM_04_print_command length=0x0007
7E00:                   4B 7B 75 8D A6 85 2E ; 
;
;                       IS LOCKED.
;
7E07:             A5                     ;         FN_A5_VERIFY_OPEN
7E08:             A6                     ;         FN_A6_ATTEMPT_TO_OPEN
7E09:       3A                           ;     COM_0A_is_input_phrase("OPEN u....... WITH u.......")
7E0A:       11                           ;     ELSE goto=0x7E1C
7E0B:          0E 0F                     ;       COM_0E_while_fail length=0x000F
7E0D:             0D 03                  ;         COM_0D_while_pass length=0x0003
7E0F:                1B                  ;           COM_1B_set_var_to_second_noun()
7E10:                14                  ;           COM_14_execute_and_reverse_status next command
7E11:                8F                  ;           FN_8F_TRY_TO_GET_OBJECT
7E12:             13                     ;         UNKNOWN13
7E13:             92                     ;         FN_92_PRINT_TRIED_BUT_COULDNT
7E14:             A5                     ;         FN_A5_VERIFY_OPEN
7E15:             0D 04                  ;         COM_0D_while_pass length=0x0004
7E17:                2E 40               ;           UNKNOWN2E, Value: 0x40
7E19:                2A                  ;           UNKNOWN2A
7E1A:                0C                  ;           COM_0C_fail()
7E1B:             A6                     ;         FN_A6_ATTEMPT_TO_OPEN
7E1C:       40                           ;     COM_0A_is_input_phrase("CLOSE ....A... * *")
7E1D:       24                           ;     ELSE goto=0x7E42
7E1E:          0E 22                     ;       COM_0E_while_fail length=0x0022
7E20:             13                     ;         UNKNOWN13
7E21:             92                     ;         FN_92_PRINT_TRIED_BUT_COULDNT
7E22:             0D 0E                  ;         COM_0D_while_pass length=0x000E
7E24:                1A                  ;           COM_1A_set_var_to_first_noun()
7E25:                2E 20               ;           UNKNOWN2E, Value: 0x20
7E27:                A8                  ;           FN_A8_PRINT_noun1
7E28:                04 08               ;           COM_04_print_command length=0x0008
7E2A:                   4B 7B 06 9A C2 16 A7 61 ; 
;
;                       IS NOT OPEN.
;
7E32:             0D 0E                  ;         COM_0D_while_pass length=0x000E
7E34:                29                  ;           COM_29_print_open_var()
7E35:                A8                  ;           FN_A8_PRINT_noun1
7E36:                04 0A               ;           COM_04_print_command length=0x000A
7E38:                   4B 7B 09 9A DE 14 D7 A0 9B 5D ; 
;
;                       IS NOW CLOSED. 
;
7E42:       42                           ;     COM_0A_is_input_phrase("UNLOCK u....... WITH u.......")
7E43:       2D                           ;     ELSE goto=0x7E71
7E44:          0E 2B                     ;       COM_0E_while_fail length=0x002B
7E46:             0D 03                  ;         COM_0D_while_pass length=0x0003
7E48:                1B                  ;           COM_1B_set_var_to_second_noun()
7E49:                14                  ;           COM_14_execute_and_reverse_status next command
7E4A:                8F                  ;           FN_8F_TRY_TO_GET_OBJECT
7E4B:             13                     ;         UNKNOWN13
7E4C:             92                     ;         FN_92_PRINT_TRIED_BUT_COULDNT
7E4D:             0D 11                  ;         COM_0D_while_pass length=0x0011
7E4F:                1A                  ;           COM_1A_set_var_to_first_noun()
7E50:                14                  ;           COM_14_execute_and_reverse_status next command
7E51:                2E 40               ;           UNKNOWN2E, Value: 0x40
7E53:                A8                  ;           FN_A8_PRINT_noun1
7E54:                04 0A               ;           COM_04_print_command length=0x000A
7E56:                   4B 7B 06 9A 49 16 97 54 9B 5D ; 
;
;                       IS NOT LOCKED. 
;
7E60:             0D 0F                  ;         COM_0D_while_pass length=0x000F
7E62:                2A                  ;           UNKNOWN2A
7E63:                A8                  ;           FN_A8_PRINT_noun1
7E64:                04 0B               ;           COM_04_print_command length=0x000B
7E66:                   4B 7B 09 9A B0 17 75 8D A6 85 2E ; 
;
;                       IS NOW UNLOCKED.
;
7E71:       41                           ;     COM_0A_is_input_phrase("LOCK ....A... WITH u.......")
7E72:       45                           ;     ELSE goto=0x7EB8
7E73:          0E 43                     ;       COM_0E_while_fail length=0x0043
7E75:             0D 03                  ;         COM_0D_while_pass length=0x0003
7E77:                1B                  ;           COM_1B_set_var_to_second_noun()
7E78:                14                  ;           COM_14_execute_and_reverse_status next command
7E79:                8F                  ;           FN_8F_TRY_TO_GET_OBJECT
7E7A:             13                     ;         UNKNOWN13
7E7B:             92                     ;         FN_92_PRINT_TRIED_BUT_COULDNT
7E7C:             0D 17                  ;         COM_0D_while_pass length=0x0017
7E7E:                14                  ;           COM_14_execute_and_reverse_status next command
7E7F:                09 14               ;           COM_09_compare_to_second_noun(obj=OBJ_14_DOOR_COVERED_SHELTER)
7E81:                04 0A               ;           COM_04_print_command length=0x000A
7E83:                   C7 DE D3 14 E6 96 49 16 8B 54 ; 
;
;                       YOU CAN'T LOCK 
;
7E8D:                A8                  ;           FN_A8_PRINT_noun1
7E8E:                04 03               ;           COM_04_print_command length=0x0003
7E90:                   56 D1 48         ; 
;
;                       WITH
;
7E93:                A9                  ;           FN_A9_PRINT_noun2
7E94:                8B                  ;           FN_8B_PRINT_PERIOD
7E95:             0D 11                  ;         COM_0D_while_pass length=0x0011
7E97:                1A                  ;           COM_1A_set_var_to_first_noun()
7E98:                2E 40               ;           UNKNOWN2E, Value: 0x40
7E9A:                A8                  ;           FN_A8_PRINT_noun1
7E9B:                04 0B               ;           COM_04_print_command length=0x000B
7E9D:                   4B 7B 06 9A B0 17 75 8D A6 85 2E ; 
;
;                       IS NOT UNLOCKED.
;
7EA8:             0D 0E                  ;         COM_0D_while_pass length=0x000E
7EAA:                2A                  ;           UNKNOWN2A
7EAB:                A8                  ;           FN_A8_PRINT_noun1
7EAC:                04 0A               ;           COM_04_print_command length=0x000A
7EAE:                   4B 7B 09 9A 49 16 97 54 9B 5D ; 
;
;                       IS NOW LOCKED. 
;
7EB8:       12                           ;     COM_0A_is_input_phrase("PULL u....... * *")
7EB9:       28                           ;     ELSE goto=0x7EE2
7EBA:          0E 26                     ;       COM_0E_while_fail length=0x0026
7EBC:             13                     ;         UNKNOWN13
7EBD:             0D 05                  ;         COM_0D_while_pass length=0x0005
7EBF:                1A                  ;           COM_1A_set_var_to_first_noun()
7EC0:                14                  ;           COM_14_execute_and_reverse_status next command
7EC1:                15 20               ;           COM_15_check_var(value=0x20)
7EC3:                C2                  ;           FN_C2_PRINT_CANT_BUDGE_noun1
7EC4:             0D 1C                  ;         COM_0D_while_pass length=0x001C
7EC6:                04 13               ;           COM_04_print_command length=0x0013
7EC8:                   33 D1 09 15 E6 96 51 18 4E C2 98 5F 56 5E DB 72 ; 
7ED8:                   81 A6 52         ; 
;
;                       WHY DON'T YOU LEAVE THE POOR
;
7EDB:                11                  ;           COM_11_print_first_noun()
7EDC:                04 04               ;           COM_04_print_command length=0x0004
7EDE:                   49 48 7F 98      ; 
;
;                       ALONE.
;
7EE2:       09                           ;     COM_0A_is_input_phrase("ATTACK ...P.... WITH .v......")
7EE3:       57                           ;     ELSE goto=0x7F3B
7EE4:          0E 55                     ;       COM_0E_while_fail length=0x0055
7EE6:             14                     ;         COM_14_execute_and_reverse_status next command
7EE7:             1B                     ;         COM_1B_set_var_to_second_noun()
7EE8:             14                     ;         COM_14_execute_and_reverse_status next command
7EE9:             0E 03                  ;         COM_0E_while_fail length=0x0003
7EEB:                09 37               ;           COM_09_compare_to_second_noun(obj=OBJ_37_STEEL_SAFE)
7EED:                8F                  ;           FN_8F_TRY_TO_GET_OBJECT
7EEE:             0E 3E                  ;         COM_0E_while_fail length=0x003E
7EF0:                0D 17               ;           COM_0D_while_pass length=0x0017
7EF2:                   14               ;             COM_14_execute_and_reverse_status next command
7EF3:                   15 40            ;             COM_15_check_var(value=0x40)
7EF5:                   04 0A            ;             COM_04_print_command length=0x000A
7EF7:                      C7 DE D3 14 E6 96 AF 15 B3 B3 ; 
;
;                          YOU CAN'T HURT 
;
7F01:                   A8               ;             FN_A8_PRINT_noun1
7F02:                   04 03            ;             COM_04_print_command length=0x0003
7F04:                      56 D1 48      ; 
;
;                          WITH
;
7F07:                   A9               ;             FN_A9_PRINT_noun2
7F08:                   8B               ;             FN_8B_PRINT_PERIOD
7F09:                13                  ;           UNKNOWN13
7F0A:                0D 22               ;           COM_0D_while_pass length=0x0022
7F0C:                   1A               ;             COM_1A_set_var_to_first_noun()
7F0D:                   14               ;             COM_14_execute_and_reverse_status next command
7F0E:                   15 10            ;             COM_15_check_var(value=0x10)
7F10:                   04 13            ;             COM_04_print_command length=0x0013
7F12:                      73 7B 77 5B D0 B5 C9 9C 36 A0 89 17 AF 14 73 49 ; 
7F22:                      03 A0 41      ; 
;
;                          IT DOES NO GOOD TO BEAT ON A
;
7F25:                   11               ;             COM_11_print_first_noun()
7F26:                   04 04            ;             COM_04_print_command length=0x0004
7F28:                      56 D1 03 71   ; 
;
;                          WITH A
;
7F2C:                   12               ;             COM_12_print_second_noun()
7F2D:                   8B               ;             FN_8B_PRINT_PERIOD
7F2E:             0D 0B                  ;         COM_0D_while_pass length=0x000B
7F30:                A8                  ;           FN_A8_PRINT_noun1
7F31:                04 08               ;           COM_04_print_command length=0x0008
7F33:                   4B 7B 92 C5 37 49 17 60 ; 
;
;                       IS UNHARMED.
;
7F3B:       0A                           ;     COM_0A_is_input_phrase("LOOK * * *")
7F3C:       01                           ;     ELSE goto=0x7F3E
7F3D:          07                        ;       COM_07_print_room_description()
7F3E:       15                           ;     COM_0A_is_input_phrase("EAT u....... * *")
7F3F:       26                           ;     ELSE goto=0x7F66
7F40:          0E 24                     ;       COM_0E_while_fail length=0x0024
7F42:             13                     ;         UNKNOWN13
7F43:             0D 21                  ;         COM_0D_while_pass length=0x0021
7F45:                04 0A               ;           COM_04_print_command length=0x000A
7F47:                   80 5B F3 23 5B 4D 4E B8 F9 8E ; 
;
;                       DON'T BE SILLY!
;
7F51:                A8                  ;           FN_A8_PRINT_noun1
7F52:                04 12               ;           COM_04_print_command length=0x0012
7F54:                   47 D2 C8 8B F3 23 55 BD DB BD 41 6E 03 58 99 9B ; 
7F64:                   5F 4A            ; 
;
;                       WOULDN'T TASTE GOOD ANYWAY.
;
7F66:       59                           ;     COM_0A_is_input_phrase("TASTE u....... * *")
7F67:       13                           ;     ELSE goto=0x7F7B
7F68:          0E 11                     ;       COM_0E_while_fail length=0x0011
7F6A:             13                     ;         UNKNOWN13
7F6B:             0D 0E                  ;         COM_0D_while_pass length=0x000E
7F6D:                04 0B               ;           COM_04_print_command length=0x000B
7F6F:                   73 7B 55 BD F5 BD 43 16 9B 85 41 ; 
;
;                       IT TASTES LIKE A
;
7F7A:                11                  ;           COM_11_print_first_noun()
7F7B:       17                           ;     COM_0A_is_input_phrase("CLIMB u....... * *")
7F7C:       4C                           ;     ELSE goto=0x7FC9
7F7D:          0E 4A                     ;       COM_0E_while_fail length=0x004A
7F7F:             13                     ;         UNKNOWN13
7F80:             0D 22                  ;         COM_0D_while_pass length=0x0022
7F82:                1A                  ;           COM_1A_set_var_to_first_noun()
7F83:                15 10               ;           COM_15_check_var(value=0x10)
7F85:                04 09               ;           COM_04_print_command length=0x0009
7F87:                   46 77 05 A0 16 BC 90 73 4B ; 
;
;                       I DON'T THINK
;
7F90:                A8                  ;           FN_A8_PRINT_noun1
7F91:                04 11               ;           COM_04_print_command length=0x0011
7F93:                   4E D1 15 8A 50 BD 15 58 8E BE 08 8A BE A0 56 72 ; 
7FA3:                   2E               ; 
;
;                       WILL STAND STILL FORTHAT.
;
7FA4:             0D 23                  ;         COM_0D_while_pass length=0x0023
7FA6:                04 10               ;           COM_04_print_command length=0x0010
7FA8:                   CF 62 8B 96 9B 64 1B A1 47 55 B3 8B C3 54 A3 91 ; 
;
;                       EVEN IF YOU COULD CLIMB 
;
7FB8:                A8                  ;           FN_A8_PRINT_noun1
7FB9:                04 0E               ;           COM_04_print_command length=0x000E
7FBB:                   73 7B 47 D2 C8 8B F3 23 EE 72 1B A3 3F A1 ; 
;
;                       IT WOULDN'T HELP YOU.
;
7FC9:       16                           ;     COM_0A_is_input_phrase("DROP * OUT ....A...")
7FCA:       12                           ;     ELSE goto=0x7FDD
7FCB:          0E 10                     ;       COM_0E_while_fail length=0x0010
7FCD:             13                     ;         UNKNOWN13
7FCE:             0D 0D                  ;         COM_0D_while_pass length=0x000D
7FD0:                A8                  ;           FN_A8_PRINT_noun1
7FD1:                04 0A               ;           COM_04_print_command length=0x000A
7FD3:                   4B 7B 06 9A BF 14 D3 B2 CF 98 ; 
;
;                       IS NOT BURNING.
;
7FDD:       18                           ;     COM_0A_is_input_phrase("RUB u....... * *")
7FDE:       2E                           ;     ELSE goto=0x800D
7FDF:          0E 2C                     ;       COM_0E_while_fail length=0x002C
7FE1:             13                     ;         UNKNOWN13
7FE2:             0D 15                  ;         COM_0D_while_pass length=0x0015
7FE4:                1A                  ;           COM_1A_set_var_to_first_noun()
7FE5:                15 10               ;           COM_15_check_var(value=0x10)
7FE7:                04 0E               ;           COM_04_print_command length=0x000E
7FE9:                   5B BE 65 BC 99 16 F3 17 56 DB CA 9C 3E C6 ; 
;
;                       THAT'S NO WAY TO HURT
;
7FF7:                AA                  ;           FN_AA_PRINT_THE_var
7FF8:                8B                  ;           FN_8B_PRINT_PERIOD
7FF9:             0D 12                  ;         COM_0D_while_pass length=0x0012
7FFB:                A8                  ;           FN_A8_PRINT_noun1
7FFC:                04 0F               ;           COM_04_print_command length=0x000F
7FFE:                   81 8D CB 87 A5 94 04 71 8E 62 23 62 09 9A 2E ; 
;
;                       LOOKS MUCH BETTER NOW.
;
800D:       0B                           ;     COM_0A_is_input_phrase("LOOK * AT u.......")
800E:       65                           ;     ELSE goto=0x8074
800F:          0E 63                     ;       COM_0E_while_fail length=0x0063
8011:             13                     ;         UNKNOWN13
8012:             0D 17                  ;         COM_0D_while_pass length=0x0017
8014:                1A                  ;           COM_1A_set_var_to_first_noun()
8015:                15 04               ;           COM_15_check_var(value=0x04)
8017:                04 10               ;           COM_04_print_command length=0x0010
8019:                   3F B9 82 62 91 7A D5 15 04 18 8E 7B 83 61 03 A0 ; 
;
;                       SOMETHING IS WRITTEN ON 
;
8029:                AA                  ;           FN_AA_PRINT_THE_var
802A:                8B                  ;           FN_8B_PRINT_PERIOD
802B:             0D 0D                  ;         COM_0D_while_pass length=0x000D
802D:                2E 20               ;           UNKNOWN2E, Value: 0x20
802F:                04 09               ;           COM_04_print_command length=0x0009
8031:                   73 7B 4B 7B C9 54 A6 B7 2E ; 
;
;                       IT IS CLOSED.
;
803A:             0D 0D                  ;         COM_0D_while_pass length=0x000D
803C:                2E 40               ;           UNKNOWN2E, Value: 0x40
803E:                04 09               ;           COM_04_print_command length=0x0009
8040:                   73 7B 4B 7B 75 8D A6 85 2E ; 
;
;                       IT IS LOCKED.
;
8049:             0D 0A                  ;         COM_0D_while_pass length=0x000A
804B:                15 02               ;           COM_15_check_var(value=0x02)
804D:                0E 05               ;           COM_0E_while_fail length=0x0005
804F:                   2E 80            ;             UNKNOWN2E, Value: 0x80
8051:                   14               ;             COM_14_execute_and_reverse_status next command
8052:                   2E 20            ;             UNKNOWN2E, Value: 0x20
8054:                33                  ;           UNKNOWN33
8055:             0D 03                  ;         COM_0D_while_pass length=0x0003
8057:                15 01               ;           COM_15_check_var(value=0x01)
8059:                33                  ;           UNKNOWN33
805A:             0D 18                  ;         COM_0D_while_pass length=0x0018
805C:                04 14               ;           COM_04_print_command length=0x0014
805E:                   5F BE 5D B1 D0 B5 02 A1 91 7A 62 17 DB 5F 33 48 ; 
806E:                   B9 46 73 C6      ; 
;
;                       THERE'S NOTHING SPECIAL ABOUT 
;
8072:                A8                  ;           FN_A8_PRINT_noun1
8073:                8B                  ;           FN_8B_PRINT_PERIOD
8074:       0C                           ;     COM_0A_is_input_phrase("LOOK * UNDER u.......")
8075:       17                           ;     ELSE goto=0x808D
8076:          0E 15                     ;       COM_0E_while_fail length=0x0015
8078:             13                     ;         UNKNOWN13
8079:             0D 12                  ;         COM_0D_while_pass length=0x0012
807B:                04 0E               ;           COM_04_print_command length=0x000E
807D:                   5F BE 5D B1 D0 B5 02 A1 91 7A B0 17 F4 59 ; 
;
;                       THERE'S NOTHING UNDER
;
808B:                A8                  ;           FN_A8_PRINT_noun1
808C:                8B                  ;           FN_8B_PRINT_PERIOD
808D:       10                           ;     COM_0A_is_input_phrase("LOOK * IN ......O.")
808E:       4C                           ;     ELSE goto=0x80DB
808F:          0E 4A                     ;       COM_0E_while_fail length=0x004A
8091:             13                     ;         UNKNOWN13
8092:             0D 2A                  ;         COM_0D_while_pass length=0x002A
8094:                1B                  ;           COM_1B_set_var_to_second_noun()
8095:                14                  ;           COM_14_execute_and_reverse_status next command
8096:                15 02               ;           COM_15_check_var(value=0x02)
8098:                04 22               ;           COM_04_print_command length=0x0022
809A:                   40 55 B0 53 EB BF DB BD 4B 49 C7 DE 63 16 B3 E0 ; 
80AA:                   C7 DE D3 14 90 96 F3 A0 A7 B7 90 14 82 DF 91 7A ; 
80BA:                   D0 15            ; 
;
;                       CONCENTRATE AS YOU MAY, YOU CAN NOT SEE ANYTHING IN
;
80BC:                A9                  ;           FN_A9_PRINT_noun2
80BD:                8B                  ;           FN_8B_PRINT_PERIOD
80BE:             0D 0F                  ;         COM_0D_while_pass length=0x000F
80C0:                14                  ;           COM_14_execute_and_reverse_status next command
80C1:                2E 80               ;           UNKNOWN2E, Value: 0x80
80C3:                2E 20               ;           UNKNOWN2E, Value: 0x20
80C5:                A9                  ;           FN_A9_PRINT_noun2
80C6:                04 07               ;           COM_04_print_command length=0x0007
80C8:                   4B 7B C9 54 A6 B7 2E ; 
;
;                       IS CLOSED.
;
80CF:             33                     ;         UNKNOWN33
80D0:             0D 09                  ;         COM_0D_while_pass length=0x0009
80D2:                A9                  ;           FN_A9_PRINT_noun2
80D3:                04 06               ;           COM_04_print_command length=0x0006
80D5:                   4B 7B 72 61 1F C1 ; 
;
;                       IS EMPTY.
;
80DB:       4C                           ;     COM_0A_is_input_phrase("LOOK * ON .......L")
80DC:       51                           ;     ELSE goto=0x812E
80DD:          0E 4F                     ;       COM_0E_while_fail length=0x004F
80DF:             13                     ;         UNKNOWN13
80E0:             0D 1A                  ;         COM_0D_while_pass length=0x001A
80E2:                1B                  ;           COM_1B_set_var_to_second_noun()
80E3:                15 04               ;           COM_15_check_var(value=0x04)
80E5:                04 13               ;           COM_04_print_command length=0x0013
80E7:                   5F BE 5D B1 D5 B5 E7 9F 63 BE AB 98 B3 D2 3F C0 ; 
80F7:                   91 96 4E         ; 
;
;                       THERE'S SOMETHING WRITTEN ON
;
80FA:                A9                  ;           FN_A9_PRINT_noun2
80FB:                8B                  ;           FN_8B_PRINT_PERIOD
80FC:             0D 1D                  ;         COM_0D_while_pass length=0x001D
80FE:                14                  ;           COM_14_execute_and_reverse_status next command
80FF:                15 01               ;           COM_15_check_var(value=0x01)
8101:                04 16               ;           COM_04_print_command length=0x0016
8103:                   5F BE 5D B1 D0 B5 02 A1 91 7A 99 16 F9 BD BE A0 ; 
8113:                   FB 75 B9 46 73 C6 ; 
;
;                       THERE'S NOTHING NOTEWORTHY ABOUT 
;
8119:                A9                  ;           FN_A9_PRINT_noun2
811A:                8B                  ;           FN_8B_PRINT_PERIOD
811B:             33                     ;         UNKNOWN33
811C:             0D 10                  ;         COM_0D_while_pass length=0x0010
811E:                04 0C               ;           COM_04_print_command length=0x000C
8120:                   5F BE 5D B1 D0 B5 02 A1 91 7A C0 16 ; 
;
;                       THERE'S NOTHING ON
;
812C:                A9                  ;           FN_A9_PRINT_noun2
812D:                8B                  ;           FN_8B_PRINT_PERIOD
812E:       1B                           ;     COM_0A_is_input_phrase("LOOK * AROUND u.......")
812F:       1E                           ;     ELSE goto=0x814E
8130:          0E 1C                     ;       COM_0E_while_fail length=0x001C
8132:             13                     ;         UNKNOWN13
8133:             0D 03                  ;         COM_0D_while_pass length=0x0003
8135:                08 00               ;           COM_08_is_first_noun(obj=nothing)
8137:                07                  ;           COM_07_print_room_description()
8138:             0D 14                  ;         COM_0D_while_pass length=0x0014
813A:                04 10               ;           COM_04_print_command length=0x0010
813C:                   5F BE 5B B1 4B 7B 06 9A 90 73 C3 6A 07 B3 33 98 ; 
;
;                       THERE IS NOTHING AROUND 
;
814C:                A8                  ;           FN_A8_PRINT_noun1
814D:                8B                  ;           FN_8B_PRINT_PERIOD
814E:       1C                           ;     COM_0A_is_input_phrase("LOOK * BEHIND u.......")
814F:       32                           ;     ELSE goto=0x8182
8150:          0E 30                     ;       COM_0E_while_fail length=0x0030
8152:             13                     ;         UNKNOWN13
8153:             0D 17                  ;         COM_0D_while_pass length=0x0017
8155:                08 00               ;           COM_08_is_first_noun(obj=nothing)
8157:                04 13               ;           COM_04_print_command length=0x0013
8159:                   5F BE 5B B1 4B 7B 06 9A 90 73 C4 6A A3 60 33 98 ; 
8169:                   C7 DE 2E         ; 
;
;                       THERE IS NOTHING BEHIND YOU.
;
816C:             0D 14                  ;         COM_0D_while_pass length=0x0014
816E:                04 10               ;           COM_04_print_command length=0x0010
8170:                   5F BE 5B B1 4B 7B 06 9A 90 73 C4 6A A3 60 33 98 ; 
;
;                       THERE IS NOTHING BEHIND 
;
8180:                A8                  ;           FN_A8_PRINT_noun1
8181:                8B                  ;           FN_8B_PRINT_PERIOD
8182:       1D                           ;     COM_0A_is_input_phrase("LOOK * OUT *")
8183:       16                           ;     ELSE goto=0x819A
8184:          04 14                     ;       COM_04_print_command length=0x0014
8186:             9F 77 AF 14 91 7A 95 14 D3 14 68 B1 33 C5 4B 49 ; 
8196:             45 77 81 48            ; 
;
;                 I'M BEING AS CAREFUL AS I CAN!
;
819A:       1E                           ;     COM_0A_is_input_phrase("YES * * *")
819B:       04                           ;     ELSE goto=0x81A0
819C:          04 02                     ;       COM_04_print_command length=0x0002
819E:             E9 99                  ; 
;
;                 NO!
;
81A0:       1F                           ;     COM_0A_is_input_phrase("NO * * *")
81A1:       05                           ;     ELSE goto=0x81A7
81A2:          04 03                     ;       COM_04_print_command length=0x0003
81A4:             35 DD 21               ; 
;
;                 YES!
;
81A7:       21                           ;     COM_0A_is_input_phrase("PLUGH * * *")
81A8:       1C                           ;     ELSE goto=0x81C5
81A9:          04 1A                     ;       COM_04_print_command length=0x001A
81AB:             44 B9 9E B4 BB 15 80 5B F3 23 6E 4D 38 79 4B 5E ; 
81BB:             8F 96 7B 47 D9 51 AE A0 5B BB ; 
;
;                 SORRY, I DON'T BELIEVE IN MAGIC WORDS. 
;
81C5:       5A                           ;     COM_0A_is_input_phrase("THUM * * *")
81C6:       1B                           ;     ELSE goto=0x81E2
81C7:          04 19                     ;       COM_04_print_command length=0x0019
81C9:             25 A1 AB 70 56 77 BE 9F 51 18 B3 C7 5B BE 0B C0 ; 
81D9:             06 9A E9 16 DB B9 7F 4E 21 ; 
;
;                 OUCH! I TOLD YOU, THATS NOT POSSIBLE!
;
81E2:       22                           ;     COM_0A_is_input_phrase("SCREAM * * *")
81E3:       12                           ;     ELSE goto=0x81F6
81E4:          04 10                     ;       COM_04_print_command length=0x0010
81E6:             5B E0 27 60 31 60 41 A0 49 A0 89 D3 89 D3 69 CE ; 
;
;                 YYYEEEEEOOOOOOWWWWWWWW!!
;
81F6:       23                           ;     COM_0A_is_input_phrase("QUIT * * *")
81F7:       01                           ;     ELSE goto=0x81F9
81F8:          24                        ;       COM_24_exit_program()
81F9:       2C                           ;     COM_0A_is_input_phrase("SCORE * * *")
81FA:       01                           ;     ELSE goto=0x81FC
81FB:          C9                        ;       FN_C9_PRINT_COMPLETED_PERCENT
81FC:       3E                           ;     COM_0A_is_input_phrase("LOAD * * *")
81FD:       04                           ;     ELSE goto=0x8202
81FE:          0D 02                     ;       COM_0D_while_pass length=0x0002
8200:             C6                     ;         FN_C6_PROMPT_FOR_DRIVE_NUMBER
8201:             27                     ;         UNKNOWN27
8202:       3F                           ;     COM_0A_is_input_phrase("SAVE * * *")
8203:       04                           ;     ELSE goto=0x8208
8204:          0D 02                     ;       COM_0D_while_pass length=0x0002
8206:             C6                     ;         FN_C6_PROMPT_FOR_DRIVE_NUMBER
8207:             28                     ;         UNKNOWN28
8208:       25                           ;     COM_0A_is_input_phrase("LEAVE * * *")
8209:       20                           ;     ELSE goto=0x822A
820A:          04 1E                     ;       COM_04_print_command length=0x001E
820C:             C7 DE AF 23 99 16 09 BC 8E 62 91 7A 90 14 FA DF ; 
821C:             2F 62 16 EE 7B B4 46 45 2F 7B 03 56 27 A0 ; 
;
;                 YOU'RE NOT GETTING ANYWHERE, TRY A DIRECTION.
;
822A:       26                           ;     COM_0A_is_input_phrase("GO * AROUND u.......")
822B:       20                           ;     ELSE goto=0x824C
822C:          0E 1E                     ;       COM_0E_while_fail length=0x001E
822E:             13                     ;         UNKNOWN13
822F:             0D 13                  ;         COM_0D_while_pass length=0x0013
8231:                1A                  ;           COM_1A_set_var_to_first_noun()
8232:                15 10               ;           COM_15_check_var(value=0x10)
8234:                A8                  ;           FN_A8_PRINT_noun1
8235:                04 0D               ;           COM_04_print_command length=0x000D
8237:                   40 D2 F3 23 F6 8B 51 18 52 C2 65 49 21 ; 
;
;                       WON'T LET YOU PASS!
;
8244:             04 06                  ;         COM_04_print_command length=0x0006
8246:                09 9A FA 17 70 49   ; 
;
;                    NOW WHAT?
;
824C:       3D                           ;     COM_0A_is_input_phrase("GO * TO u.......")
824D:       01                           ;     ELSE goto=0x824F
824E:          91                        ;       FN_91_PRINT_USE_DIRECTIONS
824F:       27                           ;     COM_0A_is_input_phrase("KICK u....... * *")
8250:       0E                           ;     ELSE goto=0x825F
8251:          0E 0C                     ;       COM_0E_while_fail length=0x000C
8253:             13                     ;         UNKNOWN13
8254:             04 09                  ;         COM_04_print_command length=0x0009
8256:                25 A1 AB 70 3B 95 77 BF 21 ; 
;
;                    OUCH! MY TOE!
;
825F:       44                           ;     COM_0A_is_input_phrase("HELLO * * *")
8260:       09                           ;     ELSE goto=0x826A
8261:          04 07                     ;       COM_04_print_command length=0x0007
8263:             AF 6E 83 62 C5 98 21   ; 
;
;                 GREETINGS!
;
826A:       45                           ;     COM_0A_is_input_phrase("HELLO ...P.... * *")
826B:       30                           ;     ELSE goto=0x829C
826C:          0E 2E                     ;       COM_0E_while_fail length=0x002E
826E:             13                     ;         UNKNOWN13
826F:             0D 12                  ;         COM_0D_while_pass length=0x0012
8271:                1A                  ;           COM_1A_set_var_to_first_noun()
8272:                15 10               ;           COM_15_check_var(value=0x10)
8274:                A8                  ;           FN_A8_PRINT_noun1
8275:                04 0C               ;           COM_04_print_command length=0x000C
8277:                   72 B1 87 8C 33 BB DF 1B 09 8D 63 F4 ; 
;
;                       REPLIES, "HELLO." 
;
8283:             0D 17                  ;         COM_0D_while_pass length=0x0017
8285:                04 13               ;           COM_04_print_command length=0x0013
8287:                   16 A0 43 DB E4 14 83 4A 01 18 3E C5 7B 17 CB 8C ; 
8297:                   6B BF 41         ; 
;
;                       ONLY A CRAZY WOULD TALK TO A
;
829A:                11                  ;           COM_11_print_first_noun()
829B:                8B                  ;           FN_8B_PRINT_PERIOD
829C:       46                           ;     COM_0A_is_input_phrase("WHAT * * *")
829D:       08                           ;     ELSE goto=0x82A6
829E:          04 06                     ;       COM_04_print_command length=0x0006
82A0:             46 77 98 C5 5B A2      ; 
;
;                 I DUNNO. 
;
82A6:       47                           ;     COM_0A_is_input_phrase("WHAT u....... * *")
82A7:       09                           ;     ELSE goto=0x82B1
82A8:          04 07                     ;       COM_04_print_command length=0x0007
82AA:             29 D1 20 16 85 A1 3F   ; 
;
;                 WHO KNOWS?
;
82B1:       4A                           ;     COM_0A_is_input_phrase("COME * * *")
82B2:       18                           ;     ELSE goto=0x82CB
82B3:          0E 16                     ;       COM_0E_while_fail length=0x0016
82B5:             13                     ;         UNKNOWN13
82B6:             0D 13                  ;         COM_0D_while_pass length=0x0013
82B8:                04 11               ;           COM_04_print_command length=0x0011
82BA:                   9E 77 08 8A C6 9F 6B A1 C7 DE 90 14 FA DF 2F 62 ; 
82CA:                   21               ; 
;
;                       I'LL FOLLOW YOU ANYWHERE!
;
82CB:       49                           ;     COM_0A_is_input_phrase("MEET u....... * *")
82CC:       26                           ;     ELSE goto=0x82F3
82CD:          0E 24                     ;       COM_0E_while_fail length=0x0024
82CF:             13                     ;         UNKNOWN13
82D0:             0D 11                  ;         COM_0D_while_pass length=0x0011
82D2:                09 00               ;           COM_09_compare_to_second_noun(obj=nothing)
82D4:                A8                  ;           FN_A8_PRINT_noun1
82D5:                04 0C               ;           COM_04_print_command length=0x000C
82D7:                   09 4F CB B5 89 96 67 B1 90 BE 5B 70 ; 
;
;                       BOWS IN GREETING. 
;
82E3:             04 0E                  ;         COM_04_print_command length=0x000E
82E5:                5F BE 44 DB 6B A1 83 7A AF 6E 83 62 CF 98 ; 
;
;                    THEY BOW IN GREETING.
;
82F3:       28                           ;     COM_0A_is_input_phrase("FEED ...P.... WITH u.......")
82F4:       36                           ;     ELSE goto=0x832B
82F5:          0E 34                     ;       COM_0E_while_fail length=0x0034
82F7:             13                     ;         UNKNOWN13
82F8:             0D 16                  ;         COM_0D_while_pass length=0x0016
82FA:                1A                  ;           COM_1A_set_var_to_first_noun()
82FB:                15 10               ;           COM_15_check_var(value=0x10)
82FD:                A8                  ;           FN_A8_PRINT_noun1
82FE:                04 10               ;           COM_04_print_command length=0x0010
8300:                   60 7B F3 23 70 75 C3 6E 33 17 2E 6D 99 16 5B D4 ; 
;
;                       ISN'T HUNGRY RIGHT NOW. 
;
8310:             0D 19                  ;         COM_0D_while_pass length=0x0019
8312:                04 0D               ;           COM_04_print_command length=0x000D
8314:                   80 5B F3 23 C7 DE 20 16 6B A1 5B BE 54 ; 
;
;                       DON'T YOU KNOW THAT
;
8321:                A8                  ;           FN_A8_PRINT_noun1
8322:                04 07               ;           COM_04_print_command length=0x0007
8324:                   10 53 F3 23 96 5F 21 ; 
;
;                       CAN'T EAT!
;
832B:       29                           ;     COM_0A_is_input_phrase("FEED u....... TO ...P....")
832C:       34                           ;     ELSE goto=0x8361
832D:          0E 32                     ;       COM_0E_while_fail length=0x0032
832F:             13                     ;         UNKNOWN13
8330:             0D 14                  ;         COM_0D_while_pass length=0x0014
8332:                1B                  ;           COM_1B_set_var_to_second_noun()
8333:                15 10               ;           COM_15_check_var(value=0x10)
8335:                A9                  ;           FN_A9_PRINT_noun2
8336:                04 0E               ;           COM_04_print_command length=0x000E
8338:                   47 D2 B3 8B D6 B0 F4 72 23 15 1B BC 19 A1 ; 
;
;                       WOULD RATHER EAT YOU!
;
8346:             0D 19                  ;         COM_0D_while_pass length=0x0019
8348:                04 17               ;           COM_04_print_command length=0x0017
834A:                   43 79 C7 DE D3 14 88 96 8E 7A 7B 14 C7 93 76 BE ; 
835A:                   BD 15 49 90 67 48 21 ; 
;
;                       IF YOU CAN FIND A MOUTH, I'M GAME!
;
8361:       2F                           ;     COM_0A_is_input_phrase("WAIT * * *")
8362:       07                           ;     ELSE goto=0x836A
8363:          04 05                     ;       COM_04_print_command length=0x0005
8365:             9B 29 57 C6 3E         ; 
;
;                 <PAUSE>
;
836A:       31                           ;     COM_0A_is_input_phrase("FIND u....... * *")
836B:       17                           ;     ELSE goto=0x8383
836C:          04 15                     ;       COM_04_print_command length=0x0015
836E:             36 9F D6 15 CB 23 39 49 8E C5 9F 15 5B B1 3F B9 ; 
837E:             FA 62 2F 62 2E         ; 
;
;                 OH, IT'S AROUND HERE SOMEWHERE.
;
8383:       2D                           ;     COM_0A_is_input_phrase("PULL * UP u.......")
8384:       09                           ;     ELSE goto=0x838E
8385:          0E 07                     ;       COM_0E_while_fail length=0x0007
8387:             13                     ;         UNKNOWN13
8388:             0D 02                  ;         COM_0D_while_pass length=0x0002
838A:                1A                  ;           COM_1A_set_var_to_first_noun()
838B:                8F                  ;           FN_8F_TRY_TO_GET_OBJECT
838C:             14                     ;         COM_14_execute_and_reverse_status next command
838D:             0C                     ;         COM_0C_fail()
838E:       48                           ;     COM_0A_is_input_phrase("LOWER u....... * *")
838F:       11                           ;     ELSE goto=0x83A1
8390:          0E 0F                     ;       COM_0E_while_fail length=0x000F
8392:             13                     ;         UNKNOWN13
8393:             04 0C                  ;         COM_04_print_command length=0x000C
8395:                C7 DE D3 14 E6 96 09 15 82 17 97 49 ; 
;
;                    YOU CAN'T DO THAT.
;
83A1:       33                           ;     COM_0A_is_input_phrase("??33??")
83A2:       27                           ;     ELSE goto=0x83CA
83A3:          0E 25                     ;       COM_0E_while_fail length=0x0025
83A5:             13                     ;         UNKNOWN13
83A6:             04 22                  ;         COM_04_print_command length=0x0022
83A8:                0F A0 5F 17 46 48 66 17 D3 61 04 68 63 16 5B 99 ; 
83B8:                56 98 C0 16 49 5E 90 78 0E BC 92 5F 59 15 9B AF ; 
83C8:                19 A1               ; 
;
;                    ONE SMALL STEP FOR MANKIND, ONE GIANT LEAP FOR YOU!
;
83CA:       34                           ;     COM_0A_is_input_phrase("JUMP * OVER u.......")
83CB:       23                           ;     ELSE goto=0x83EF
83CC:          0E 21                     ;       COM_0E_while_fail length=0x0021
83CE:             13                     ;         UNKNOWN13
83CF:             04 1E                  ;         COM_04_print_command length=0x001E
83D1:                C7 DE 95 AF D5 C3 65 62 D5 15 67 16 67 49 66 B1 ; 
83E1:                D0 15 3F 16 ED 48 90 14 04 58 30 A1 09 5C ; 
;
;                    YOUR SUCCESS IS MEASURED IN LEAPS AND BOUNDS!
;
83EF:       35                           ;     COM_0A_is_input_phrase("JUMP * ON u.......")
83F0:       1C                           ;     ELSE goto=0x840D
83F1:          0E 1A                     ;       COM_0E_while_fail length=0x001A
83F3:             13                     ;         UNKNOWN13
83F4:             04 17                  ;         COM_04_print_command length=0x0017
83F6:                C7 DE 73 21 76 4D F4 BD F3 17 9A BD FA 17 2F 62 ; 
8406:                51 18 55 C2 F2 BD 21 ; 
;
;                    YOU'D BETTER WATCH WHERE YOU STEP!
;
840D:       36                           ;     COM_0A_is_input_phrase("ENTER * * *")
840E:       04                           ;     ELSE goto=0x8413
840F:          0E 02                     ;       COM_0E_while_fail length=0x0002
8411:             13                     ;         UNKNOWN13
8412:             91                     ;         FN_91_PRINT_USE_DIRECTIONS
8413:       37                           ;     COM_0A_is_input_phrase("CLIMB * OUT *")
8414:       04                           ;     ELSE goto=0x8419
8415:          0E 02                     ;       COM_0E_while_fail length=0x0002
8417:             13                     ;         UNKNOWN13
8418:             91                     ;         FN_91_PRINT_USE_DIRECTIONS
8419:       54                           ;     COM_0A_is_input_phrase("CLIMB * UP *")
841A:       17                           ;     ELSE goto=0x8432
841B:          0E 15                     ;       COM_0E_while_fail length=0x0015
841D:             13                     ;         UNKNOWN13
841E:             04 12                  ;         COM_04_print_command length=0x0012
8420:                5F BE 5B B1 4B 7B EB 99 FB A5 9B 53 6B BF 2B 6E ; 
8430:                F7 C5               ; 
;
;                    THERE IS NO PLACE TO GO UP.
;
8432:       55                           ;     COM_0A_is_input_phrase("CLIMB * DOWN *")
8433:       19                           ;     ELSE goto=0x844D
8434:          0E 17                     ;       COM_0E_while_fail length=0x0017
8436:             13                     ;         UNKNOWN13
8437:             04 14                  ;         COM_04_print_command length=0x0014
8439:                5F BE 5B B1 4B 7B EB 99 FB A5 9B 53 6B BF 2B 6E ; 
8449:                89 5B 1B 9C         ; 
;
;                    THERE IS NO PLACE TO GO DOWN. 
;
844D:       38                           ;     COM_0A_is_input_phrase("CLIMB * UNDER u.......")
844E:       1D                           ;     ELSE goto=0x846C
844F:          0E 1B                     ;       COM_0E_while_fail length=0x001B
8451:             13                     ;         UNKNOWN13
8452:             0D 18                  ;         COM_0D_while_pass length=0x0018
8454:                04 14               ;           COM_04_print_command length=0x0014
8456:                   5F BE 5B B1 4B 7B 06 9A 30 15 29 A1 14 71 3F A0 ; 
8466:                   B0 17 F4 59      ; 
;
;                       THERE IS NOT ENOUGH ROOM UNDER
;
846A:                A8                  ;           FN_A8_PRINT_noun1
846B:                8B                  ;           FN_8B_PRINT_PERIOD
846C:       39                           ;     COM_0A_is_input_phrase("THROW ..C..... IN u.......")
846D:       1D                           ;     ELSE goto=0x848B
846E:          0E 1B                     ;       COM_0E_while_fail length=0x001B
8470:             13                     ;         UNKNOWN13
8471:             0D 18                  ;         COM_0D_while_pass length=0x0018
8473:                04 16               ;           COM_04_print_command length=0x0016
8475:                   C7 DE FB 17 F3 8C 58 72 56 5E D2 9C 73 C6 73 7B ; 
8485:                   83 7A 5F BE 7F B1 ; 
;
;                       YOU WILL HAVE TO PUT IT IN THERE.
;
848B:       0D                           ;     COM_0A_is_input_phrase("THROW .vC..... AT ...P....")
848C:       2B                           ;     ELSE goto=0x84B8
848D:          0E 29                     ;       COM_0E_while_fail length=0x0029
848F:             0D 25                  ;         COM_0D_while_pass length=0x0025
8491:                1A                  ;           COM_1A_set_var_to_first_noun()
8492:                8F                  ;           FN_8F_TRY_TO_GET_OBJECT
8493:                0E 21               ;           COM_0E_while_fail length=0x0021
8495:                   13               ;             UNKNOWN13
8496:                   0D 1E            ;             COM_0D_while_pass length=0x001E
8498:                      0E 07         ;               COM_0E_while_fail length=0x0007
849A:                         14         ;                 COM_14_execute_and_reverse_status next command
849B:                         15 10      ;                 COM_15_check_var(value=0x10)
849D:                         1B         ;                 COM_1B_set_var_to_second_noun()
849E:                         14         ;                 COM_14_execute_and_reverse_status next command
849F:                         15 40      ;                 COM_15_check_var(value=0x40)
84A1:                      A8            ;               FN_A8_PRINT_noun1
84A2:                      04 0F         ;               COM_04_print_command length=0x000F
84A4:                         07 4F 17 98 CA B5 37 49 F5 8B D3 B8 B8 16 46 ; 
;
;                             BOUNCES HARMLESSLY OFF
;
84B3:                      A9            ;               FN_A9_PRINT_noun2
84B4:                      8B            ;               FN_8B_PRINT_PERIOD
84B5:                      10            ;               COM_10_drop_var()
84B6:             14                     ;         COM_14_execute_and_reverse_status next command
84B7:             0C                     ;         COM_0C_fail()
84B8:       57                           ;     COM_0A_is_input_phrase("SHOOT u....... WITH u.......")
84B9:       81 09                        ;     ELSE goto=0x85C4
84BB:          0E 81 06                  ;       COM_0E_while_fail length=0x0106
84BE:             13                     ;         UNKNOWN13
84BF:             0D 0F                  ;         COM_0D_while_pass length=0x000F
84C1:                14                  ;           COM_14_execute_and_reverse_status next command
84C2:                09 28               ;           COM_09_compare_to_second_noun(obj=OBJ_28_SHOTGUN)
84C4:                A9                  ;           FN_A9_PRINT_noun2
84C5:                04 09               ;           COM_04_print_command length=0x0009
84C7:                   60 7B F3 23 73 8D E6 59 2E ; 
;
;                       ISN'T LOADED.
;
84D0:             0D 0A                  ;         COM_0D_while_pass length=0x000A
84D2:                14                  ;           COM_14_execute_and_reverse_status next command
84D3:                03 28 29            ;           COM_03_is_located(owner=OBJ_28_SHOTGUN, obj=OBJ_29_??)
84D6:                04 04               ;           COM_04_print_command length=0x0004
84D8:                   C3 54 AF 54      ; 
;
;                       CLICK.
;
84DC:             0D 80 CB               ;         COM_0D_while_pass length=0x00CB
84DF:                04 04               ;           COM_04_print_command length=0x0004
84E1:                   7B 4E EB 8F      ; 
;
;                       BLAM! 
;
84E5:                0B 80 C2 08         ;           COM_0B_switch length=0x00C2, function=COM_08_is_first_noun(word_num)
84E9:                   33               ;             COM_08_is_first_noun(object_num=OBJ_33_RATTLE_SNAKE)
84EA:                   0E               ;             ELSE goto=0x84F9
84EB:                      0D 0C         ;               COM_0D_while_pass length=0x000C
84ED:                         04 07      ;                 COM_04_print_command length=0x0007
84EF:                            41 6E 15 58 86 74 21 ; 
;
;                                GOOD SHOT!
;
84F6:                         1A         ;                 COM_1A_set_var_to_first_noun()
84F7:                         1D 64      ;                 COM_1D_attack_var(points=100)
84F9:                   62               ;             COM_08_is_first_noun(object_num=OBJ_62_SHAGGY_CREATURE)
84FA:                   4D               ;             ELSE goto=0x8548
84FB:                      0D 4B         ;               COM_0D_while_pass length=0x004B
84FD:                         04 45      ;                 COM_04_print_command length=0x0045
84FF:                            5F BE 8E 14 30 79 D5 15 43 16 BF 68 03 58 33 98 ; 
850F:                            6C BE 80 A1 AB 14 A9 54 2E 49 C4 B5 56 DB DB 72 ; 
851F:                            72 7A E6 46 B8 16 82 17 44 5E 55 8B 9B C1 8D 7B ; 
852F:                            43 16 D3 93 F6 4E 48 DB 46 48 D6 B5 D6 9C DB 72 ; 
853F:                            B9 6E 8E C5 2E ; 
;
;                                THE ALIEN IS LIFTED AND THROWN BACKWARDS BY THE IMPACT OF
;                                THE BLAST. ITS LIMP BODY FALLS TO THE GROUND.
;
8544:                         1C 62      ;                 COM_1C_set_var_object(obj=OBJ_62_SHAGGY_CREATURE)
8546:                         1D 15      ;                 COM_1D_attack_var(points=21)
8548:                   89               ;             COM_08_is_first_noun(object_num=OBJ_89_ALIEN_ANTS)
8549:                   60               ;             ELSE goto=0x85AA
854A:                      0D 5E         ;               COM_0D_while_pass length=0x005E
854C:                         04 58      ;                 COM_04_print_command length=0x0058
854E:                            5F BE 5A 17 01 A1 83 C5 F3 B2 8B B3 E3 59 70 66 ; 
855E:                            91 7A 1E 8F BF 14 0A BC 4B 49 96 8C FF BE 28 15 ; 
856E:                            65 66 11 BC 96 96 DB 72 18 D0 51 5E 95 64 8E 91 ; 
857E:                            04 8A 45 8B C5 83 63 B1 74 C0 4B 62 5B BE 19 BC ; 
858E:                            5A 49 C8 16 23 62 C7 DE 15 EE 90 BE 50 6D DB 6A ; 
859E:                            1B A1 6B BF E3 59 77 BE ; 
;
;                                THE SHOTGUN ROARS DEAFENINGLY, BUT HAS LITTLE EFFECT ON THE
;                                WAVE OF SMALL BLACK CREATURES THAT WASH OVER YOU, STINGING
;                                YOU TO DEATH.
;
85A6:                         1C 01      ;                 COM_1C_set_var_object(obj=OBJ_01_PLAYER)
85A8:                         1D 4B      ;                 COM_1D_attack_var(points=75)
85AA:             0D 18                  ;         COM_0D_while_pass length=0x0018
85AC:                04 14               ;           COM_04_print_command length=0x0014
85AE:                   5F BE 5B B1 2F 49 57 17 74 CA 33 48 79 98 A9 15 ; 
85BE:                   F5 8B D0 15      ; 
;
;                       THERE ARE SEVERAL NEW HOLES IN
;
85C2:                A8                  ;           FN_A8_PRINT_noun1
85C3:                8B                  ;           FN_8B_PRINT_PERIOD
85C4:       0E                           ;     COM_0A_is_input_phrase("THROW u....... TO ...P....")
85C5:       13                           ;     ELSE goto=0x85D9
85C6:          0E 11                     ;       COM_0E_while_fail length=0x0011
85C8:             13                     ;         UNKNOWN13
85C9:             0D 0E                  ;         COM_0D_while_pass length=0x000E
85CB:                A9                  ;           FN_A9_PRINT_noun2
85CC:                04 0B               ;           COM_04_print_command length=0x000B
85CE:                   77 5B 05 B9 19 BC 9E 48 D6 15 2E ; 
;
;                       DOESN'T WANT IT.
;
85D9:       0F                           ;     COM_0A_is_input_phrase("DROP ..C..... IN ......O.")
85DA:       1D                           ;     ELSE goto=0x85F8
85DB:          0E 1B                     ;       COM_0E_while_fail length=0x001B
85DD:             0D 06                  ;         COM_0D_while_pass length=0x0006
85DF:                1A                  ;           COM_1A_set_var_to_first_noun()
85E0:                14                  ;           COM_14_execute_and_reverse_status next command
85E1:                2E 10               ;           UNKNOWN2E, Value: 0x10
85E3:                14                  ;           COM_14_execute_and_reverse_status next command
85E4:                8F                  ;           FN_8F_TRY_TO_GET_OBJECT
85E5:             14                     ;         COM_14_execute_and_reverse_status next command
85E6:             BF                     ;         FN_BF_??
85E7:             0D 05                  ;         COM_0D_while_pass length=0x0005
85E9:                1B                  ;           COM_1B_set_var_to_second_noun()
85EA:                14                  ;           COM_14_execute_and_reverse_status next command
85EB:                15 02               ;           COM_15_check_var(value=0x02)
85ED:                B6                  ;           FN_B6_PRINT_TWO_SAME_SPACE
85EE:             B7                     ;         FN_B7_PRINT_HAVE_TO_OPEN_var
85EF:             0D 04                  ;         COM_0D_while_pass length=0x0004
85F1:                1B                  ;           COM_1B_set_var_to_second_noun()
85F2:                32                  ;           UNKNOWN32
85F3:                B5                  ;           FN_B5_PRINT_BY_YOUR_COMMAND
85F4:                0C                  ;           COM_0C_fail()
85F5:             13                     ;         UNKNOWN13
85F6:             14                     ;         COM_14_execute_and_reverse_status next command
85F7:             0C                     ;         COM_0C_fail()
85F8:       4D                           ;     COM_0A_is_input_phrase("FILL ......O. WITH u.......")
85F9:       23                           ;     ELSE goto=0x861D
85FA:          0E 21                     ;       COM_0E_while_fail length=0x0021
85FC:             0D 05                  ;         COM_0D_while_pass length=0x0005
85FE:                1B                  ;           COM_1B_set_var_to_second_noun()
85FF:                14                  ;           COM_14_execute_and_reverse_status next command
8600:                2E 10               ;           UNKNOWN2E, Value: 0x10
8602:                B8                  ;           FN_B8_PRINT_GARBAGE_GAMES
8603:             14                     ;         COM_14_execute_and_reverse_status next command
8604:             BF                     ;         FN_BF_??
8605:             0D 05                  ;         COM_0D_while_pass length=0x0005
8607:                1A                  ;           COM_1A_set_var_to_first_noun()
8608:                14                  ;           COM_14_execute_and_reverse_status next command
8609:                15 02               ;           COM_15_check_var(value=0x02)
860B:                B6                  ;           FN_B6_PRINT_TWO_SAME_SPACE
860C:             B7                     ;         FN_B7_PRINT_HAVE_TO_OPEN_var
860D:             0D 05                  ;         COM_0D_while_pass length=0x0005
860F:                1B                  ;           COM_1B_set_var_to_second_noun()
8610:                14                  ;           COM_14_execute_and_reverse_status next command
8611:                2E 10               ;           UNKNOWN2E, Value: 0x10
8613:                B8                  ;           FN_B8_PRINT_GARBAGE_GAMES
8614:             0D 04                  ;         COM_0D_while_pass length=0x0004
8616:                1A                  ;           COM_1A_set_var_to_first_noun()
8617:                31                  ;           UNKNOWN31
8618:                B5                  ;           FN_B5_PRINT_BY_YOUR_COMMAND
8619:                0C                  ;           COM_0C_fail()
861A:             13                     ;         UNKNOWN13
861B:             14                     ;         COM_14_execute_and_reverse_status next command
861C:             0C                     ;         COM_0C_fail()
861D:       4E                           ;     COM_0A_is_input_phrase("POUR u....... * *")
861E:       3F                           ;     ELSE goto=0x865E
861F:          0E 3D                     ;       COM_0E_while_fail length=0x003D
8621:             0D 0A                  ;         COM_0D_while_pass length=0x000A
8623:                1A                  ;           COM_1A_set_var_to_first_noun()
8624:                14                  ;           COM_14_execute_and_reverse_status next command
8625:                2E 10               ;           UNKNOWN2E, Value: 0x10
8627:                04 03               ;           COM_04_print_command length=0x0003
8629:                   81 A6 52         ; 
;
;                       POOR
;
862C:                11                  ;           COM_11_print_first_noun()
862D:             14                     ;         COM_14_execute_and_reverse_status next command
862E:             BF                     ;         FN_BF_??
862F:             0D 10                  ;         COM_0D_while_pass length=0x0010
8631:                09 00               ;           COM_09_compare_to_second_noun(obj=nothing)
8633:                1C 00               ;           COM_1C_set_var_object(obj=nothing)
8635:                32                  ;           UNKNOWN32
8636:                A8                  ;           FN_A8_PRINT_noun1
8637:                04 08               ;           COM_04_print_command length=0x0008
8639:                   4B 7B 09 9A 81 15 7F 98 ; 
;
;                       IS NOW GONE.
;
8641:             0D 12                  ;         COM_0D_while_pass length=0x0012
8643:                1B                  ;           COM_1B_set_var_to_second_noun()
8644:                14                  ;           COM_14_execute_and_reverse_status next command
8645:                15 02               ;           COM_15_check_var(value=0x02)
8647:                A9                  ;           FN_A9_PRINT_noun2
8648:                04 08               ;           COM_04_print_command length=0x0008
864A:                   4B 7B 09 9A FB 14 F7 93 ; 
;
;                       IS NOW DAMP.
;
8652:                1C 00               ;           COM_1C_set_var_object(obj=nothing)
8654:                32                  ;           UNKNOWN32
8655:             0D 04                  ;         COM_0D_while_pass length=0x0004
8657:                1B                  ;           COM_1B_set_var_to_second_noun()
8658:                32                  ;           UNKNOWN32
8659:                B5                  ;           FN_B5_PRINT_BY_YOUR_COMMAND
865A:                0C                  ;           COM_0C_fail()
865B:             13                     ;         UNKNOWN13
865C:             14                     ;         COM_14_execute_and_reverse_status next command
865D:             0C                     ;         COM_0C_fail()
865E:       4F                           ;     COM_0A_is_input_phrase("DRINK u....... * *")
865F:       52                           ;     ELSE goto=0x86B2
8660:          0E 50                     ;       COM_0E_while_fail length=0x0050
8662:             0D 32                  ;         COM_0D_while_pass length=0x0032
8664:                1A                  ;           COM_1A_set_var_to_first_noun()
8665:                14                  ;           COM_14_execute_and_reverse_status next command
8666:                2E 10               ;           UNKNOWN2E, Value: 0x10
8668:                04 2A               ;           COM_04_print_command length=0x002A
866A:                   C7 DE AF 23 5B 17 AE 54 BF 14 10 BC F3 A0 4E 72 ; 
867A:                   83 64 D5 B5 DD 78 95 14 51 18 59 C2 2E A1 04 58 ; 
868A:                   4B 5E 9B 64 1B A1 EB 5B 4B 99 ; 
;
;                       YOU'RE SICK, BUT NOT HALF AS SICK AS YOU WOULD BE IF YOU
;                       DRANK
;
8694:                A8                  ;           FN_A8_PRINT_noun1
8695:                8B                  ;           FN_8B_PRINT_PERIOD
8696:             14                     ;         COM_14_execute_and_reverse_status next command
8697:             BF                     ;         FN_BF_??
8698:             0D 04                  ;         COM_0D_while_pass length=0x0004
869A:                13                  ;           UNKNOWN13
869B:                1C 00               ;           COM_1C_set_var_object(obj=nothing)
869D:                32                  ;           UNKNOWN32
869E:             0D 12                  ;         COM_0D_while_pass length=0x0012
86A0:                1C 00               ;           COM_1C_set_var_object(obj=nothing)
86A2:                32                  ;           UNKNOWN32
86A3:                04 0D               ;           COM_04_print_command length=0x000D
86A5:                   C7 DE 4F 15 33 61 68 B1 75 B1 E6 72 2E ; 
;
;                       YOU FEEL REFRESHED.
;
86B2:       4B                           ;     COM_0A_is_input_phrase("DROP ..C..... ON .......L")
86B3:       43                           ;     ELSE goto=0x86F7
86B4:          0E 41                     ;       COM_0E_while_fail length=0x0041
86B6:             13                     ;         UNKNOWN13
86B7:             0D 06                  ;         COM_0D_while_pass length=0x0006
86B9:                1A                  ;           COM_1A_set_var_to_first_noun()
86BA:                14                  ;           COM_14_execute_and_reverse_status next command
86BB:                2E 10               ;           UNKNOWN2E, Value: 0x10
86BD:                14                  ;           COM_14_execute_and_reverse_status next command
86BE:                8F                  ;           FN_8F_TRY_TO_GET_OBJECT
86BF:             0D 16                  ;         COM_0D_while_pass length=0x0016
86C1:                2E 10               ;           UNKNOWN2E, Value: 0x10
86C3:                0E 12               ;           COM_0E_while_fail length=0x0012
86C5:                   14               ;             COM_14_execute_and_reverse_status next command
86C6:                   BF               ;             FN_BF_??
86C7:                   0D 0E            ;             COM_0D_while_pass length=0x000E
86C9:                      A9            ;               FN_A9_PRINT_noun2
86CA:                      04 08         ;               COM_04_print_command length=0x0008
86CC:                         4B 7B 09 9A F7 17 9B C1 ; 
;
;                             IS NOW WET. 
;
86D4:                      1C 00         ;               COM_1C_set_var_object(obj=nothing)
86D6:                      32            ;               UNKNOWN32
86D7:             0D 16                  ;         COM_0D_while_pass length=0x0016
86D9:                1B                  ;           COM_1B_set_var_to_second_noun()
86DA:                14                  ;           COM_14_execute_and_reverse_status next command
86DB:                15 01               ;           COM_15_check_var(value=0x01)
86DD:                04 10               ;           COM_04_print_command length=0x0010
86DF:                   5F BE 5D B1 D0 B5 F3 A0 99 61 7A C4 39 17 FF 9F ; 
;
;                       THERE'S NOT ENOUGH ROOM.
;
86EF:             0D 04                  ;         COM_0D_while_pass length=0x0004
86F1:                1B                  ;           COM_1B_set_var_to_second_noun()
86F2:                32                  ;           UNKNOWN32
86F3:                B5                  ;           FN_B5_PRINT_BY_YOUR_COMMAND
86F4:                0C                  ;           COM_0C_fail()
86F5:             14                     ;         COM_14_execute_and_reverse_status next command
86F6:             0C                     ;         COM_0C_fail()
86F7:       19                           ;     COM_0A_is_input_phrase("DIAGNO * * *")
86F8:       80 EB                        ;     ELSE goto=0x87E5
86FA:          0D 80 E8                  ;       COM_0D_while_pass length=0x00E8
86FD:             1C 01                  ;         COM_1C_set_var_object(obj=OBJ_01_PLAYER)
86FF:             0B 80 E3 22            ;         COM_0B_switch length=0x00E3, function=COM_22_is_less_equal_health(points)
8703:                05                  ;           COM_22_is_less_equal_health(points=5)
8704:                24                  ;           ELSE goto=0x8729
8705:                   04 22            ;             COM_04_print_command length=0x0022
8707:                      C7 DE 94 14 51 5E 9B 96 34 A1 3B 16 F3 B9 E9 8B ; 
8717:                      5B BB A3 48 63 BE AB 98 47 55 B3 8B 4E 86 1B 8A ; 
8727:                      19 A1         ; 
;
;                          YOU ARE ON YOUR LAST LEGS. ANYTHING COULD KILL YOU!
;
8729:                14                  ;           COM_22_is_less_equal_health(points=20)
872A:                1C                  ;           ELSE goto=0x8747
872B:                   04 1A            ;             COM_04_print_command length=0x001A
872D:                      0F A0 71 16 5B B1 41 6E 0B 58 3F 99 7B B4 8E 48 ; 
873D:                      51 18 A8 C2 4A 5E F3 46 71 7B ; 
;
;                          ONE MORE GOOD INJURY AND YOU'VE HAD IT!
;
8747:                23                  ;           COM_22_is_less_equal_health(points=35)
8748:                22                  ;           ELSE goto=0x876B
8749:                   04 20            ;             COM_04_print_command length=0x0020
874B:                      C7 DE 94 14 48 5E 2E 60 91 7A 17 17 7F 7B CE 15 ; 
875B:                      9B 8F 52 77 75 B1 B3 55 5B 4D 17 53 91 BE 2B 96 ; 
;
;                          YOU ARE FEELING QUITE ILL. I PRESCRIBE CAUTION! 
;
876B:                33                  ;           COM_22_is_less_equal_health(points=51)
876C:                32                  ;           ELSE goto=0x879F
876D:                   04 30            ;             COM_04_print_command length=0x0030
876F:                      C7 DE 94 14 50 5E F3 A0 67 66 90 8C D7 6A 16 A3 ; 
877F:                      D2 9C 47 49 51 18 55 C2 87 74 B3 8B 4D BD 44 5E ; 
878F:                      8E 62 23 62 14 53 51 5E 9B 64 34 A1 AE B7 1B 6A ; 
;
;                          YOU ARE NOT FEELING UP TO PAR. YOU SHOULD TAKE BETTER CARE
;                          OF YOURSELF.
;
879F:                44                  ;           COM_22_is_less_equal_health(points=68)
87A0:                24                  ;           ELSE goto=0x87C5
87A1:                   04 22            ;             COM_04_print_command length=0x0022
87A3:                      C7 DE AF 23 4F 15 43 61 AB 98 EF A6 53 C0 81 15 ; 
87B3:                      73 9E 8E C5 23 62 5F BE DB 14 27 B1 66 94 8D 48 ; 
87C3:                      6F 62         ; 
;
;                          YOU'RE FEELING PRETTY GOOD UNDER THE CIRCUMSTANCES.
;
87C5:                FF                  ;           COM_22_is_less_equal_health(points=255)
87C6:                1E                  ;           ELSE goto=0x87E5
87C7:                   04 1C            ;             COM_04_print_command length=0x001C
87C9:                      C7 DE 4F 15 33 61 4B 49 41 6E 03 58 D6 B5 DB 72 ; 
87D9:                      5B 59 51 18 59 C2 2F 62 B9 14 E7 B2 ; 
;
;                          YOU FEEL AS GOOD AS THE DAY YOU WERE BORN.
;
87E5:       52                           ;     COM_0A_is_input_phrase("START u....... * *")
87E6:       04                           ;     ELSE goto=0x87EB
87E7:          0E 02                     ;       COM_0E_while_fail length=0x0002
87E9:             13                     ;         UNKNOWN13
87EA:             B8                     ;         FN_B8_PRINT_GARBAGE_GAMES
87EB:       56                           ;     COM_0A_is_input_phrase("DIG u....... WITH u.......")
87EC:       11                           ;     ELSE goto=0x87FE
87ED:          0E 0F                     ;       COM_0E_while_fail length=0x000F
87EF:             13                     ;         UNKNOWN13
87F0:             04 0C                  ;         COM_04_print_command length=0x000C
87F2:                46 77 6B 79 73 7B 81 BF 0F EE 81 48 ; 
;
;                    I DIG IT TOO, MAN!
;
87FE:       50                           ;     COM_0A_is_input_phrase("TURN * ON u.......")
87FF:       11                           ;     ELSE goto=0x8811
8800:          0E 0F                     ;       COM_0E_while_fail length=0x000F
8802:             13                     ;         UNKNOWN13
8803:             04 0C                  ;         COM_04_print_command length=0x000C
8805:                C7 DE D3 14 E6 96 09 15 82 17 71 49 ; 
;
;                    YOU CAN'T DO THAT!
;
8811:       51                           ;     COM_0A_is_input_phrase("TURN * OFF u.......")
8812:       2B                           ;     ELSE goto=0x883E
8813:          0E 29                     ;       COM_0E_while_fail length=0x0029
8815:             13                     ;         UNKNOWN13
8816:             04 26                  ;         COM_04_print_command length=0x0026
8818:                68 4D AF A0 51 18 45 C2 83 48 74 C0 95 96 E7 9F ; 
8828:                63 BE AB 98 D0 9E 0B EE 0F BC 66 C6 AF 14 8F 17 ; 
8838:                CF B2 11 58 1B 9C   ; 
;
;                    BEFORE YOU CAN TURN SOMETHING OFF, IT MUST BE TURNED ON. 
;
883E:       53                           ;     COM_0A_is_input_phrase("STRIKE u....... * *")
883F:       0F                           ;     ELSE goto=0x884F
8840:          0E 0D                     ;       COM_0E_while_fail length=0x000D
8842:             13                     ;         UNKNOWN13
8843:             0D 0A                  ;         COM_0D_while_pass length=0x000A
8845:                04 08               ;           COM_04_print_command length=0x0008
8847:                   57 C6 93 13 3B C0 8D 54 ; 
;
;                       USE 'ATTACK'
;
884F:       58                           ;     COM_0A_is_input_phrase("POINT u....... * *")
8850:       0D                           ;     ELSE goto=0x885E
8851:          0E 0B                     ;       COM_0E_while_fail length=0x000B
8853:             13                     ;         UNKNOWN13
8854:             0D 08                  ;         COM_0D_while_pass length=0x0008
8856:                04 06               ;           COM_04_print_command length=0x0006
8858:                   55 77 1B 60 97 7B ; 
;
;                       I SEE IT.
;
885E:       07                           ;     COM_0A_is_input_phrase("INVENT * * *")
885F:       1A                           ;     ELSE goto=0x887A
8860:          0D 18                     ;       COM_0D_while_pass length=0x0018
8862:             04 15                  ;         COM_04_print_command length=0x0015
8864:                C7 DE 94 14 45 5E 3C 49 D0 DD D6 6A DB 72 FE 67 ; 
8874:                89 8D 91 7A 3A      ; 
;
;                    YOU ARE CARRYING THE FOLLOWING:
;
8879:             06                     ;         COM_06_print_inventory()
```

# Object Data

Some of the object scripts reference room numbers. Room numbers are
unique to the disk section but NOT the game in general. There are
multiple room 85, for instance.

If an object has no formal description, it won't be shown in a room. But
the player could still interact with it even if it doesn't show up. The
player just needs to know where to look! Check and document these ghosts.

For instance, the handgrip is in room 0x8A but has no description. The description
for one of room 8A talks about the handgrip. Sections 2, 6, 8, and 9 all have
a room 8A. The check for the handgrip might work in all of them.

Hopefully, the object that references the room is stuck in a particular
room and can't be moved to another room with the same ID. Here are
the room references in the object scripts. TODO investigate these.

```
# Room 85 could be 1, 6, 7, 9
# Room 8E could be 2, 6, or 8
# Room 90 could be 3, 6, or 8
# Room 91 could be 3, 6, or 8
# Room 92 could be 3, 6, or 8
# Room 99 could be 4, 5, or 7
# Room 9A could be 4, 5, or 8
# Room 9C could be 4, 5, or 8
# Room 9D could be 4, 5, or 8
# Room C3 only 5
# Room DB could be 2 or 5
# Room E8 only 5
```

```code
ObjectData:
887A: 00 AB 32  ; List_ID=0x00, length=0x2B32

; -------------- Object OBJ_01_PLAYER --------------
887D: 01 80 87                           ; Word_num=0x01 -player-, length=0x0087
8880: 80 01 80                           ; Location=0x80, disk_section=1, data=0, attributes=0b10000000
8883:    0A 35                           ;   Section=0A:SECTION_0A_UPON_DEATH, length=0x0035
8885:       0D 33                        ;     COM_0D_while_pass length=0x0033
8887:          0E 24                     ;       COM_0E_while_fail length=0x0024
8889:             0D 20                  ;         COM_0D_while_pass length=0x0020
888B:                03 01 35            ;           COM_03_is_located(owner=OBJ_01_PLAYER, obj=OBJ_35_??)
888E:                1F 1B               ;           COM_1F_print2 length=0x001B
8890:                   5F BE 60 17 17 48 CF 17 FF 99 F3 17 C7 B5 4C D9 ; 
88A0:                   67 61 FB 8E 7B A6 40 B9 35 A1 21 ; 
;
;                       THE SNAKE VENOM WAS EXTREMELY POISONOUS!
;
88AB:             14                     ;         COM_14_execute_and_reverse_status next command
88AC:             0C                     ;         COM_0C_fail()
88AD:          1F 09                     ;       COM_1F_print2 length=0x0009
88AF:             C7 DE 94 14 46 5E 86 5F 2E ; 
;
;                 YOU ARE DEAD.
;
88B8:          C9                        ;       FN_C9_PRINT_COMPLETED_PERCENT
88B9:          24                        ;       COM_24_exit_program()
88BA:    08 43                           ;   Section=08:SECTION_08_EVERY_TURN, length=0x0043
88BC:       0E 41                        ;     COM_0E_while_fail length=0x0041
88BE:          0D 1E                     ;       COM_0D_while_pass length=0x001E
88C0:             03 39 4B               ;         COM_03_is_located(owner=OBJ_39_DYNAMITE, obj=OBJ_4B_??)
88C3:             14                     ;         COM_14_execute_and_reverse_status next command
88C4:             01 39                  ;         COM_01_is_in_pack_or_room(obj=OBJ_39_DYNAMITE)
88C6:             0E 06                  ;         COM_0E_while_fail length=0x0006
88C8:                03 9C 01            ;           COM_03_is_located(owner=RM_1_9C_??, obj=OBJ_01_PLAYER)
88CB:                03 99 01            ;           COM_03_is_located(owner=RM_1_99_??, obj=OBJ_01_PLAYER)
88CE:             0E 06                  ;         COM_0E_while_fail length=0x0006
88D0:                03 9A 39            ;           COM_03_is_located(owner=RM_1_9A_??, obj=OBJ_39_DYNAMITE)
88D3:                03 9D 39            ;           COM_03_is_located(owner=RM_1_9D_??, obj=OBJ_39_DYNAMITE)
88D6:             1F 06                  ;         COM_1F_print2 length=0x0006
88D8:                01 4F 41 A0 D9 9F   ; 
;
;                    BOOOOOOM!
;
88DE:          0D 1F                     ;       COM_0D_while_pass length=0x001F
88E0:             03 39 4B               ;         COM_03_is_located(owner=OBJ_39_DYNAMITE, obj=OBJ_4B_??)
88E3:             14                     ;         COM_14_execute_and_reverse_status next command
88E4:             01 39                  ;         COM_01_is_in_pack_or_room(obj=OBJ_39_DYNAMITE)
88E6:             1F 17                  ;         COM_1F_print2 length=0x0017
88E8:                5F BE 13 15 CF 97 7F 7B 77 16 F3 B9 58 72 44 5E ; 
88F8:                30 60 7B 14 66 5C 21 ; 
;
;                    THE DYNAMITE MUST HAVE BEEN A DUD!
;
88FF:    02 02                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0002
;           YOU
8901:       C7 DE                        ; 
8903:    09 02                           ;   Section=09:SECTION_09_HIT_POINTS, length=0x0002
8905:       46 46                        ;     Hit_points=70_of_70

; -------------- Object OBJ_02_DOOR_GAS_STATION --------------
8907: 10 08                              ; Word_num=0x10 DOOR, length=0x0008
8909: 83 01 88                           ; Location=0x83, disk_section=1, data=0, attributes=0b10001000
890C:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           DOOR
890E:       81 5B 52                     ; 

; -------------- Object OBJ_03_DOOR_FRONT_OF_STATION --------------
8911: 10 08                              ; Word_num=0x10 DOOR, length=0x0008
8913: 82 21 88                           ; Location=0x82, disk_section=1, data=2, attributes=0b10001000
8916:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           DOOR
8918:       81 5B 52                     ; 

; -------------- Object OBJ_04_DOOR_EAST_OF_STATION --------------
891B: 10 2E                              ; Word_num=0x10 DOOR, length=0x002E
891D: 88 61 8C                           ; Location=0x88, disk_section=1, data=6, attributes=0b10001100
8920:    07 24                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0024
8922:       0E 22                        ;     COM_0E_while_fail length=0x0022
8924:          0D 0A                     ;       COM_0D_while_pass length=0x000A
8926:             0E 04                  ;         COM_0E_while_fail length=0x0004
8928:                0A 3A               ;           COM_0A_is_input_phrase(phrase=OPEN u....... WITH u.......)
892A:                0A 42               ;           COM_0A_is_input_phrase(phrase=UNLOCK u....... WITH u.......)
892C:             14                     ;         COM_14_execute_and_reverse_status next command
892D:             09 1C                  ;         COM_09_compare_to_second_noun(obj=OBJ_1C_SKELETON_KEY)
892F:             BA                     ;         FN_BA_??
8930:          0D 14                     ;       COM_0D_while_pass length=0x0014
8932:             0A 08                  ;         COM_0A_is_input_phrase(phrase=READ .....?.. * *)
8934:             04 10                  ;         COM_04_print_command length=0x0010
8936:                73 7B 4B 7B EB 99 80 8D B4 6C 3F 16 44 6D FF 8B ; 
;
;                    IT IS NO LONGER LEGIBLE.
;
8946:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           DOOR
8948:       81 5B 52                     ; 

; -------------- Object OBJ_05_DOOR_RESTROOM --------------
894B: 10 08                              ; Word_num=0x10 DOOR, length=0x0008
894D: DA 01 88                           ; Location=0xDA, disk_section=1, data=0, attributes=0b10001000
8950:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           DOOR
8952:       81 5B 52                     ; 

; -------------- Object OBJ_06_DOOR_MAIN_STREET_WEST --------------
8955: 10 2C                              ; Word_num=0x10 DOOR, length=0x002C
8957: 8D 22 88                           ; Location=0x8D, disk_section=2, data=2, attributes=0b10001000
895A:    03 19                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0019
895C:       04 17                        ;     COM_04_print_command length=0x0017
895E:          7B BA BB 98 AB 98 81 5B 8B B3 E3 8B 16 58 D6 9C ; 
896E:          DB 72 0E B7 40 A0 2E      ; 
;
;              SWINGING DOORS LEAD TO THE SALOON.
;
8975:    01 02                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0002
8977:       41                           ;     SALOON
8978:       46                           ;     SWINGI
8979:    02 08                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0008
;           SALOON DOOR 
897B:       0E B7 40 A0 09 15 A3 A0      ; 

; -------------- Object OBJ_07_DOOR_SALOON --------------
8983: 10 08                              ; Word_num=0x10 DOOR, length=0x0008
8985: A2 02 88                           ; Location=0xA2, disk_section=2, data=0, attributes=0b10001000
8988:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           DOOR
898A:       81 5B 52                     ; 

; -------------- Object OBJ_08_DOOR_MAIN_STREET_WEST --------------
898D: 10 41                              ; Word_num=0x10 DOOR, length=0x0041
898F: 8D 62 88                           ; Location=0x8D, disk_section=2, data=6, attributes=0b10001000
8992:    03 1B                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x001B
8994:       04 19                        ;     COM_04_print_command length=0x0019
8996:          46 45 44 A0 3F 16 0D 47 89 17 82 17 55 5E F4 72 ; 
89A6:          50 79 CB 23 D0 9E D7 78 2E ; 
;
;              A DOOR LEADS TO THE SHERIFF'S OFFICE.
;
89AF:    07 0C                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x000C
89B1:       0D 0A                        ;     COM_0D_while_pass length=0x000A
89B3:          0E 04                     ;       COM_0E_while_fail length=0x0004
89B5:             0A 3A                  ;         COM_0A_is_input_phrase(phrase=OPEN u....... WITH u.......)
89B7:             0A 42                  ;         COM_0A_is_input_phrase(phrase=UNLOCK u....... WITH u.......)
89B9:          14                        ;       COM_14_execute_and_reverse_status next command
89BA:          09 1B                     ;       COM_09_compare_to_second_noun(obj=OBJ_1B_BRASS_KEY_SHERIFF)
89BC:          BA                        ;       FN_BA_??
89BD:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
89BF:       42                           ;     SHERIF
89C0:    02 0E                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x000E
;           SHERIFF'S OFFICE DOOR
89C2:       1F B8 08 B2 E5 64 B8 16 05 67 46 5E 44 A0 ; 

; -------------- Object OBJ_09_DOOR_SHERIFFS_OFFICE --------------
89D0: 10 08                              ; Word_num=0x10 DOOR, length=0x0008
89D2: 8E 02 88                           ; Location=0x8E, disk_section=2, data=0, attributes=0b10001000
89D5:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           DOOR
89D7:       81 5B 52                     ; 

; -------------- Object OBJ_0A_DOOR_HARDWARE_SOUTH --------------
89DA: 10 08                              ; Word_num=0x10 DOOR, length=0x0008
89DC: A6 03 88                           ; Location=0xA6, disk_section=3, data=0, attributes=0b10001000
89DF:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           DOOR
89E1:       81 5B 52                     ; 

; -------------- Object OBJ_0B_DOOR_TOWN_CENTER_SLIMS --------------
89E4: 10 34                              ; Word_num=0x10 DOOR, length=0x0034
89E6: 93 23 88                           ; Location=0x93, disk_section=3, data=2, attributes=0b10001000
89E9:    03 12                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0012
89EB:       04 10                        ;     COM_04_print_command length=0x0010
89ED:          46 45 44 A0 3F 16 0D 47 89 17 5E 17 5D 7A 5B BB ; 
;
;              A DOOR LEADS TO SLIM'S. 
;
89FD:    07 0C                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x000C
89FF:       0D 0A                        ;     COM_0D_while_pass length=0x000A
8A01:          0E 04                     ;       COM_0E_while_fail length=0x0004
8A03:             0A 3A                  ;         COM_0A_is_input_phrase(phrase=OPEN u....... WITH u.......)
8A05:             0A 42                  ;         COM_0A_is_input_phrase(phrase=UNLOCK u....... WITH u.......)
8A07:          14                        ;       COM_14_execute_and_reverse_status next command
8A08:          09 1E                     ;       COM_09_compare_to_second_noun(obj=OBJ_1E_RED_KEY_SLIMS)
8A0A:          BA                        ;       FN_BA_??
8A0B:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
8A0D:       43                           ;     SLIM'S
8A0E:    02 0A                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x000A
;           DOOR TO SLIM'S 
8A10:       81 5B 96 AF D5 9C 8F 8C CB 23 ; 

; -------------- Object OBJ_0C_DOOR_TOWN_CENTER_BOBS --------------
8A1A: 10 24                              ; Word_num=0x10 DOOR, length=0x0024
8A1C: 93 23 88                           ; Location=0x93, disk_section=3, data=2, attributes=0b10001000
8A1F:    03 11                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0011
8A21:       04 0F                        ;     COM_04_print_command length=0x000F
8A23:          46 45 44 A0 3F 16 0D 47 89 17 B9 14 E5 4B 2E ; 
;
;              A DOOR LEADS TO BOB'S.
;
8A32:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
8A34:       44                           ;     BOB'S
8A35:    02 09                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0009
;           DOOR TO BOB'S
8A37:       81 5B 96 AF C4 9C 25 9E 53   ; 

; -------------- Object OBJ_0D_DOOR_SLIMS_GROCERY --------------
8A40: 10 08                              ; Word_num=0x10 DOOR, length=0x0008
8A42: 94 03 88                           ; Location=0x94, disk_section=3, data=0, attributes=0b10001000
8A45:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           DOOR
8A47:       81 5B 52                     ; 

; -------------- Object OBJ_0E_DOOR_MAIN_STREET_EAST_HOTEL --------------
8A4A: 10 32                              ; Word_num=0x10 DOOR, length=0x0032
8A4C: 99 24 88                           ; Location=0x99, disk_section=4, data=2, attributes=0b10001000
8A4F:    03 20                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0020
8A51:       04 1E                        ;     COM_04_print_command length=0x001E
8A53:          5F BE 5B B1 2F 49 09 15 B6 C3 46 5E 44 A0 CE B5 ; 
8A63:          86 5F 91 7A 89 17 82 17 4A 5E FF A0 9B 8F ; 
;
;              THERE ARE DOUBLE DOORS LEADING TO THE HOTEL. 
;
8A71:    01 02                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0002
8A73:       45                           ;     DOUBLE
8A74:       47                           ;     HOTEL
8A75:    02 07                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0007
;           HOTEL DOOR
8A77:       86 74 33 61 81 5B 52         ; 

; -------------- Object OBJ_0F_DOOR_HOTEL_LOBBY --------------
8A7E: 10 08                              ; Word_num=0x10 DOOR, length=0x0008
8A80: AA 04 88                           ; Location=0xAA, disk_section=4, data=0, attributes=0b10001000
8A83:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           DOOR
8A85:       81 5B 52                     ; 

; -------------- Object OBJ_10_DOOR_MAIN_STREET_EAST_BANK --------------
8A88: 10 39                              ; Word_num=0x10 DOOR, length=0x0039
8A8A: 99 64 88                           ; Location=0x99, disk_section=4, data=6, attributes=0b10001000
8A8D:    02 08                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0008
;           MASSIVE DOOR
8A8F:       95 91 58 B8 46 5E 44 A0      ; 
8A97:    07 0C                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x000C
8A99:       0D 0A                        ;     COM_0D_while_pass length=0x000A
8A9B:          0E 04                     ;       COM_0E_while_fail length=0x0004
8A9D:             0A 3A                  ;         COM_0A_is_input_phrase(phrase=OPEN u....... WITH u.......)
8A9F:             0A 42                  ;         COM_0A_is_input_phrase(phrase=UNLOCK u....... WITH u.......)
8AA1:          14                        ;       COM_14_execute_and_reverse_status next command
8AA2:          09 1D                     ;       COM_09_compare_to_second_noun(obj=OBJ_1D_STEEL_KEY_BANK)
8AA4:          BA                        ;       FN_BA_??
8AA5:    01 02                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0002
8AA7:       3F                           ;     MASSIV
8AA8:       40                           ;     BANK
8AA9:    03 18                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0018
8AAB:       04 16                        ;     COM_04_print_command length=0x0016
8AAD:          4F 45 65 49 CF 7B 09 15 A3 A0 E3 8B 0B 5C 6B BF ; 
8ABD:          5F BE AB 14 6F 99         ; 
;
;              A MASSIVE DOOR LEADS TO THE BANK.
;

; -------------- Object OBJ_11_DOOR_BANK --------------
8AC3: 10 08                              ; Word_num=0x10 DOOR, length=0x0008
8AC5: 9A 04 88                           ; Location=0x9A, disk_section=4, data=0, attributes=0b10001000
8AC8:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           DOOR
8ACA:       81 5B 52                     ; 

; -------------- Object OBJ_12_DOOR --------------
8ACD: 10 03                              ; Word_num=0x10 DOOR, length=0x0003
8ACF: 00 00 00                           ; Location=0x00, disk_section=0, data=0, attributes=0b00000000

; -------------- Object OBJ_13_DOOR --------------
8AD2: 10 03                              ; Word_num=0x10 DOOR, length=0x0003
8AD4: 00 00 00                           ; Location=0x00, disk_section=0, data=0, attributes=0b00000000

; -------------- Object OBJ_14_DOOR_COVERED_SHELTER --------------
8AD7: 10 1D                              ; Word_num=0x10 DOOR, length=0x001D
8AD9: 00 22 88                           ; Location=0x00, disk_section=2, data=2, attributes=0b10001000
8ADC:    03 13                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0013
8ADE:       04 11                        ;     COM_04_print_command length=0x0011
8AE0:          46 45 44 A0 3F 16 0D 47 B0 17 F4 59 B9 6E 8E C5 ; 
8AF0:          2E                        ; 
;
;              A DOOR LEADS UNDERGROUND.
;
8AF1:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           DOOR
8AF3:       81 5B 52                     ; 

; -------------- Object OBJ_15_DOOR_SHELTER --------------
8AF6: 10 08                              ; Word_num=0x10 DOOR, length=0x0008
8AF8: DB 02 88                           ; Location=0xDB, disk_section=2, data=0, attributes=0b10001000
8AFB:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           DOOR
8AFD:       81 5B 52                     ; 

; -------------- Object OBJ_16_RED_DOOR_HALLWAY --------------
8B00: 10 30                              ; Word_num=0x10 DOOR, length=0x0030
8B02: DD 64 88                           ; Location=0xDD, disk_section=4, data=6, attributes=0b10001000
8B05:    03 12                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0012
8B07:       04 10                        ;     COM_04_print_command length=0x0010
8B09:          54 45 F3 5F 81 5B 8E AF 86 5F D0 B5 BE A0 9B 76 ; 
;
;              A RED DOOR LEADS NORTH. 
;
8B19:    07 0C                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x000C
8B1B:       0D 0A                        ;     COM_0D_while_pass length=0x000A
8B1D:          0E 04                     ;       COM_0E_while_fail length=0x0004
8B1F:             0A 3A                  ;         COM_0A_is_input_phrase(phrase=OPEN u....... WITH u.......)
8B21:             0A 42                  ;         COM_0A_is_input_phrase(phrase=UNLOCK u....... WITH u.......)
8B23:          14                        ;       COM_14_execute_and_reverse_status next command
8B24:          09 1A                     ;       COM_09_compare_to_second_noun(obj=OBJ_1A_MASTER_KEY)
8B26:          BA                        ;       FN_BA_??
8B27:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
8B29:       13                           ;     RED
8B2A:    02 06                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0006
;           RED DOOR 
8B2C:       66 B1 09 15 A3 A0            ; 

; -------------- Object OBJ_17_DOOR_NORTH_ROOM --------------
8B32: 10 08                              ; Word_num=0x10 DOOR, length=0x0008
8B34: DE 04 88                           ; Location=0xDE, disk_section=4, data=0, attributes=0b10001000
8B37:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           DOOR
8B39:       81 5B 52                     ; 

; -------------- Object OBJ_18_BLUE_DOOR_HALLWAY --------------
8B3C: 10 30                              ; Word_num=0x10 DOOR, length=0x0030
8B3E: DD 64 88                           ; Location=0xDD, disk_section=4, data=6, attributes=0b10001000
8B41:    03 12                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0012
8B43:       04 10                        ;     COM_04_print_command length=0x0010
8B45:          44 45 67 8E 09 15 A3 A0 E3 8B 0B 5C 47 B9 77 BE ; 
;
;              A BLUE DOOR LEADS SOUTH.
;
8B55:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
8B57:       0D                           ;     BLUE
8B58:    07 0C                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x000C
8B5A:       0D 0A                        ;     COM_0D_while_pass length=0x000A
8B5C:          0E 04                     ;       COM_0E_while_fail length=0x0004
8B5E:             0A 3A                  ;         COM_0A_is_input_phrase(phrase=OPEN u....... WITH u.......)
8B60:             0A 42                  ;         COM_0A_is_input_phrase(phrase=UNLOCK u....... WITH u.......)
8B62:          14                        ;       COM_14_execute_and_reverse_status next command
8B63:          09 1A                     ;       COM_09_compare_to_second_noun(obj=OBJ_1A_MASTER_KEY)
8B65:          BA                        ;       FN_BA_??
8B66:    02 06                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0006
;           BLUE DOOR
8B68:       8F 4E 46 5E 44 A0            ; 

; -------------- Object OBJ_19_DOOR_SOUTH_ROOM --------------
8B6E: 10 08                              ; Word_num=0x10 DOOR, length=0x0008
8B70: DF 04 88                           ; Location=0xDF, disk_section=4, data=0, attributes=0b10001000
8B73:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           DOOR
8B75:       81 5B 52                     ; 

; -------------- Object OBJ_1A_MASTER_KEY --------------
8B78: 16 3E                              ; Word_num=0x16 KEY, length=0x003E
8B7A: 47 00 A4                           ; Location=0x47, disk_section=0, data=0, attributes=0b10100100
8B7D:    03 14                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0014
8B7F:       04 12                        ;     COM_04_print_command length=0x0012
8B81:          5F BE 5B B1 4B 7B 4F 45 66 49 23 62 BB 85 9F 15 ; 
8B91:          7F B1                     ; 
;
;              THERE IS A MASTER KEY HERE.
;
8B93:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
8B95:       14                           ;     MASTER
8B96:    0C 01                           ;   Section=0C:SECTION_0C_WEIGHT, length=0x0001
8B98:       02                           ;     Weight=2
8B99:    07 14                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0014
8B9B:       0D 12                        ;     COM_0D_while_pass length=0x0012
8B9D:          0A 08                     ;       COM_0A_is_input_phrase(phrase=READ .....?.. * *)
8B9F:          04 0E                     ;       COM_04_print_command length=0x000E
8BA1:             C5 1A 1B 92 95 91 F4 BD 17 16 45 DB 5C A2 ; 
;
;                 "ACME MASTER KEY CO."
;
8BAF:    02 07                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0007
;           MASTER KEY
8BB1:       95 91 F4 BD 17 16 59         ; 

; -------------- Object OBJ_1B_BRASS_KEY_SHERIFF --------------
8BB8: 16 36                              ; Word_num=0x16 KEY, length=0x0036
8BBA: 48 00 A4                           ; Location=0x48, disk_section=0, data=0, attributes=0b10100100
8BBD:    03 14                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0014
8BBF:       04 12                        ;     COM_04_print_command length=0x0012
8BC1:          5F BE 5B B1 4B 7B 44 45 D5 B0 CD B5 3B 63 F4 72 ; 
8BD1:          DB 63                     ; 
;
;              THERE IS A BRASS KEY HERE. 
;
8BD3:    0C 01                           ;   Section=0C:SECTION_0C_WEIGHT, length=0x0001
8BD5:       02                           ;     Weight=2
8BD6:    01 02                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0002
8BD8:       15                           ;     BRASS
8BD9:       42                           ;     SHERIF
8BDA:    07 0C                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x000C
8BDC:       0D 0A                        ;     COM_0D_while_pass length=0x000A
8BDE:          0A 08                     ;       COM_0A_is_input_phrase(phrase=READ .....?.. * *)
8BE0:          04 06                     ;       COM_04_print_command length=0x0006
8BE2:             9A 1D 33 62 84 66      ; 
;
;                 "SHERIFF"
;
8BE8:    02 06                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0006
;           BRASS KEY
8BEA:       6B 4F CB B9 BB 85            ; 

; -------------- Object OBJ_1C_SKELETON_KEY --------------
8BF0: 16 2B                              ; Word_num=0x16 KEY, length=0x002B
8BF2: 49 00 A0                           ; Location=0x49, disk_section=0, data=0, attributes=0b10100000
8BF5:    03 16                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0016
8BF7:       04 14                        ;     COM_04_print_command length=0x0014
8BF9:          5F BE 5B B1 4B 7B 55 45 AE 85 89 62 8D 96 3B 63 ; 
8C09:          F4 72 DB 63               ; 
;
;              THERE IS A SKELETON KEY HERE. 
;
8C0D:    0C 01                           ;   Section=0C:SECTION_0C_WEIGHT, length=0x0001
8C0F:       02                           ;     Weight=2
8C10:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
8C12:       17                           ;     SKELET
8C13:    02 08                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0008
;           SKELETON KEY
8C15:       97 B8 F6 8B 03 A0 BB 85      ; 

; -------------- Object OBJ_1D_STEEL_KEY_BANK --------------
8C1D: 16 3A                              ; Word_num=0x16 KEY, length=0x003A
8C1F: 21 00 A4                           ; Location=0x21, disk_section=0, data=0, attributes=0b10100100
8C22:    03 16                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0016
8C24:       04 14                        ;     COM_04_print_command length=0x0014
8C26:          5F BE 5B B1 4B 7B 44 45 6B 79 FF B9 33 61 BB 85 ; 
8C36:          9F 15 7F B1               ; 
;
;              THERE IS A BIG STEEL KEY HERE.
;
8C3A:    0C 01                           ;   Section=0C:SECTION_0C_WEIGHT, length=0x0001
8C3C:       02                           ;     Weight=2
8C3D:    01 03                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0003
8C3F:       40                           ;     BANK
8C40:       18                           ;     STEEL
8C41:       0E                           ;     BIG
8C42:    07 0A                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x000A
8C44:       0D 08                        ;     COM_0D_while_pass length=0x0008
8C46:          0A 08                     ;       COM_0A_is_input_phrase(phrase=READ .....?.. * *)
8C48:          04 04                     ;       COM_04_print_command length=0x0004
8C4A:             EB 1A 4C 99            ; 
;
;                 "BANK"
;
8C4E:    02 09                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0009
;           BIG STEEL KEY
8C50:       09 4E 66 17 2E 60 17 16 59   ; 

; -------------- Object OBJ_1E_RED_KEY_SLIMS --------------
8C59: 16 33                              ; Word_num=0x16 KEY, length=0x0033
8C5B: 21 00 A4                           ; Location=0x21, disk_section=0, data=0, attributes=0b10100100
8C5E:    03 12                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0012
8C60:       04 10                        ;     COM_04_print_command length=0x0010
8C62:          5F BE 5B B1 4B 7B 54 45 F3 5F BB 85 9F 15 7F B1 ; 
;
;              THERE IS A RED KEY HERE.
;
8C72:    0C 01                           ;   Section=0C:SECTION_0C_WEIGHT, length=0x0001
8C74:       02                           ;     Weight=2
8C75:    01 02                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0002
8C77:       43                           ;     SLIM'S
8C78:       13                           ;     RED
8C79:    07 0C                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x000C
8C7B:       0D 0A                        ;     COM_0D_while_pass length=0x000A
8C7D:          0A 08                     ;       COM_0A_is_input_phrase(phrase=READ .....?.. * *)
8C7F:          04 06                     ;       COM_04_print_command length=0x0006
8C81:             9E 1D 5D 7A E3 B5      ; 
;
;                 "SLIM'S" 
;
8C87:    02 05                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0005
;           RED KEY
8C89:       66 B1 17 16 59               ; 

; -------------- Object OBJ_1F_SMALL_KEY_CAB --------------
8C8E: 16 34                              ; Word_num=0x16 KEY, length=0x0034
8C90: 21 00 A4                           ; Location=0x21, disk_section=0, data=0, attributes=0b10100100
8C93:    03 14                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0014
8C95:       04 12                        ;     COM_04_print_command length=0x0012
8C97:          5F BE 5B B1 4B 7B 55 45 8E 91 0D 8A 3B 63 F4 72 ; 
8CA7:          DB 63                     ; 
;
;              THERE IS A SMALL KEY HERE. 
;
8CA9:    0C 01                           ;   Section=0C:SECTION_0C_WEIGHT, length=0x0001
8CAB:       02                           ;     Weight=2
8CAC:    01 02                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0002
8CAE:       4B                           ;     CAB
8CAF:       0F                           ;     SMALL
8CB0:    07 0A                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x000A
8CB2:       0D 08                        ;     COM_0D_while_pass length=0x0008
8CB4:          0A 08                     ;       COM_0A_is_input_phrase(phrase=READ .....?.. * *)
8CB6:          04 04                     ;       COM_04_print_command length=0x0004
8CB8:             13 1B A3 4B            ; 
;
;                 "CAB" 
;
8CBC:    02 06                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0006
;           SMALL KEY
8CBE:       E3 B8 F3 8C BB 85            ; 

; -------------- Object OBJ_20_DESK --------------
8CC4: 1A 32                              ; Word_num=0x1A DESK, length=0x0032
8CC6: 8E 02 81                           ; Location=0x8E, disk_section=2, data=0, attributes=0b10000001
8CC9:    07 28                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0028
8CCB:       0D 26                        ;     COM_0D_while_pass length=0x0026
8CCD:          0E 08                     ;       COM_0E_while_fail length=0x0008
8CCF:             0A 11                  ;         COM_0A_is_input_phrase(phrase=OPEN u....... * *)
8CD1:             0A 42                  ;         COM_0A_is_input_phrase(phrase=UNLOCK u....... WITH u.......)
8CD3:             0A 40                  ;         COM_0A_is_input_phrase(phrase=CLOSE ....A... * *)
8CD5:             0A 3A                  ;         COM_0A_is_input_phrase(phrase=OPEN u....... WITH u.......)
8CD7:          04 1A                     ;       COM_04_print_command length=0x001A
8CD9:             03 C0 7B 14 EB 5B B4 D0 CE 13 76 A0 6B 16 C6 59 ; 
8CE9:             B3 63 A3 A0 06 4F 7F BF DB 31 ; 
;
;                 TRY A DRAWER <TOP, MIDDLE, OR BOTTOM>. 
;
8CF3:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           DESK
8CF5:       F5 59 4B                     ; 

; -------------- Object OBJ_21_TOP_DRAWER --------------
8CF8: 1B 54                              ; Word_num=0x1B DRAWER, length=0x0054
8CFA: 8E 62 8A                           ; Location=0x8E, disk_section=2, data=6, attributes=0b10001010
8CFD:    07 43                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0043
8CFF:       0E 41                        ;     COM_0E_while_fail length=0x0041
8D01:          0D 3E                     ;       COM_0D_while_pass length=0x003E
8D03:             0E 04                  ;         COM_0E_while_fail length=0x0004
8D05:                0A 3A               ;           COM_0A_is_input_phrase(phrase=OPEN u....... WITH u.......)
8D07:                0A 42               ;           COM_0A_is_input_phrase(phrase=UNLOCK u....... WITH u.......)
8D09:             1A                     ;         COM_1A_set_var_to_first_noun()
8D0A:             2E 40                  ;         UNKNOWN2E, Value: 0x40
8D0C:             2E 20                  ;         UNKNOWN2E, Value: 0x20
8D0E:             09 24                  ;         COM_09_compare_to_second_noun(obj=OBJ_24_CROWBAR)
8D10:             04 2B                  ;         COM_04_print_command length=0x002B
8D12:                5F BE 5B B1 4B 7B 55 45 AF 55 DA 5F B8 16 89 17 ; 
8D22:                CF B3 66 B1 67 16 4E BD 90 14 16 58 DB 72 EB 5B ; 
8D32:                B4 D0 BF 14 A6 B3 D1 B5 F0 A4 21 ; 
;
;                    THERE IS A SCREECH OF TORTURED METAL AND THE DRAWER BURSTS
;                    OPEN!
;
8D3D:             1A                     ;         COM_1A_set_var_to_first_noun()
8D3E:             2A                     ;         UNKNOWN2A
8D3F:             A6                     ;         FN_A6_ATTEMPT_TO_OPEN
8D40:             38                     ;         COM_38_bump_score()
8D41:          BA                        ;       FN_BA_??
8D42:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
8D44:       28                           ;     TOP
8D45:    02 07                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0007
;           TOP DRAWER
8D47:       82 BF 0C 15 F7 49 52         ; 

; -------------- Object OBJ_22_MIDDLE_DRAWER --------------
8D4E: 1B 43                              ; Word_num=0x1B DRAWER, length=0x0043
8D50: 8E 62 8A                           ; Location=0x8E, disk_section=2, data=6, attributes=0b10001010
8D53:    07 30                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0030
8D55:       0E 2E                        ;     COM_0E_while_fail length=0x002E
8D57:          0D 2B                     ;       COM_0D_while_pass length=0x002B
8D59:             0E 04                  ;         COM_0E_while_fail length=0x0004
8D5B:                0A 3A               ;           COM_0A_is_input_phrase(phrase=OPEN u....... WITH u.......)
8D5D:                0A 42               ;           COM_0A_is_input_phrase(phrase=UNLOCK u....... WITH u.......)
8D5F:             1A                     ;         COM_1A_set_var_to_first_noun()
8D60:             2E 40                  ;         UNKNOWN2E, Value: 0x40
8D62:             2E 20                  ;         UNKNOWN2E, Value: 0x20
8D64:             09 24                  ;         COM_09_compare_to_second_noun(obj=OBJ_24_CROWBAR)
8D66:             04 19                  ;         COM_04_print_command length=0x0019
8D68:                56 D1 03 71 E4 14 8D C5 73 76 5F BE 0C 15 F7 49 ; 
8D78:                88 AF 87 8C D1 B5 F0 A4 21 ; 
;
;                    WITH A CRUNCH, THE DRAWER FLIES OPEN!
;
8D81:             1A                     ;         COM_1A_set_var_to_first_noun()
8D82:             2A                     ;         UNKNOWN2A
8D83:             A6                     ;         FN_A6_ATTEMPT_TO_OPEN
8D84:          BA                        ;       FN_BA_??
8D85:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
8D87:       3C                           ;     MIDDLE
8D88:    02 09                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0009
;           MIDDLE DRAWER
8D8A:       C6 92 FF 5A 0C 15 F7 49 52   ; 

; -------------- Object OBJ_23_BOTTOM_DRAWER --------------
8D93: 1B 1C                              ; Word_num=0x1B DRAWER, length=0x001C
8D95: 8E 22 8A                           ; Location=0x8E, disk_section=2, data=2, attributes=0b10001010
8D98:    07 09                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0009
8D9A:       0D 07                        ;     COM_0D_while_pass length=0x0007
8D9C:          0E 04                     ;       COM_0E_while_fail length=0x0004
8D9E:             0A 3A                  ;         COM_0A_is_input_phrase(phrase=OPEN u....... WITH u.......)
8DA0:             0A 42                  ;         COM_0A_is_input_phrase(phrase=UNLOCK u....... WITH u.......)
8DA2:          BA                        ;       FN_BA_??
8DA3:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
8DA5:       3E                           ;     BOTTOM
8DA6:    02 09                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0009
;           BOTTOM DRAWER
8DA8:       06 4F 7F BF 0C 15 F7 49 52   ; 

; -------------- Object OBJ_24_CROWBAR --------------
8DB1: 37 29                              ; Word_num=0x37 CROWBA, length=0x0029
8DB3: 49 00 E0                           ; Location=0x49, disk_section=0, data=0, attributes=0b11100000
8DB6:    03 16                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0016
8DB8:       04 14                        ;     COM_04_print_command length=0x0014
8DBA:          5F BE 5B B1 4B 7B 55 45 8E 91 05 8A 09 B3 D4 4C ; 
8DCA:          9F 15 7F B1               ; 
;
;              THERE IS A SMALL CROWBAR HERE.
;
8DCE:    0C 01                           ;   Section=0C:SECTION_0C_WEIGHT, length=0x0001
8DD0:       10                           ;     Weight=16
8DD1:    02 09                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0009
;           SMALL CROWBAR
8DD3:       E3 B8 F3 8C B9 55 2B D0 52   ; 

; -------------- Object OBJ_25_WANTED_POSTER --------------
8DDC: 38 68                              ; Word_num=0x38 POSTER, length=0x0068
8DDE: 22 00 A4                           ; Location=0x22, disk_section=0, data=0, attributes=0b10100100
8DE1:    03 16                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0016
8DE3:       04 14                        ;     COM_04_print_command length=0x0014
8DE5:          5F BE 5B B1 4B 7B 59 45 9E 48 F3 5F 85 A6 F4 BD ; 
8DF5:          9F 15 7F B1               ; 
;
;              THERE IS A WANTED POSTER HERE.
;
8DF9:    07 40                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0040
8DFB:       0D 3E                        ;     COM_0D_while_pass length=0x003E
8DFD:          0A 08                     ;       COM_0A_is_input_phrase(phrase=READ .....?.. * *)
8DFF:          04 3A                     ;       COM_04_print_command length=0x003A
8E01:             33 1E BF 9A AB 57 86 91 09 15 D6 6A 74 75 90 91 ; 
8E11:             03 EE 83 8C CC B5 59 F4 56 F4 74 75 90 91 08 EE ; 
8E21:             A3 A0 87 5B 7F 4E DB 16 5B B2 AB 98 83 7A 4A 45 ; 
8E31:             E2 A0 7B 7B 1C 8A 0F A0 63 F4 ; 
;
;                 "WANTED! MAD DOG THURMAN, ALIAS J. W. THURMAN, FOR DOUBLE
;                 PARKING IN A HOSPITAL ZONE."
;
8E3B:    02 09                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0009
;           WANTED POSTER
8E3D:       10 D0 E6 BD E9 16 FF B9 52   ; 

; -------------- Object OBJ_26_GUN_CABINET --------------
8E46: 19 80 8A                           ; Word_num=0x19 CABINE, length=0x008A
8E49: 8E E2 8A                           ; Location=0x8E, disk_section=2, data=14, attributes=0b10001010
8E4C:    07 7B                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x007B
8E4E:       0E 79                        ;     COM_0E_while_fail length=0x0079
8E50:          0D 41                     ;       COM_0D_while_pass length=0x0041
8E52:             0E 04                  ;         COM_0E_while_fail length=0x0004
8E54:                0A 3A               ;           COM_0A_is_input_phrase(phrase=OPEN u....... WITH u.......)
8E56:                0A 42               ;           COM_0A_is_input_phrase(phrase=UNLOCK u....... WITH u.......)
8E58:             03 8E 27               ;         COM_03_is_located(owner=RM_1_8E_??, obj=OBJ_27_SHOTGUN)
8E5B:             09 1F                  ;         COM_09_compare_to_second_noun(obj=OBJ_1F_SMALL_KEY_CAB)
8E5D:             04 29                  ;         COM_04_print_command length=0x0029
8E5F:                5F BE 17 16 56 DB 38 C6 33 BB 5F BE 49 16 8B 54 ; 
8E6F:                C3 54 A5 54 03 EE 33 98 5F BE D3 14 10 4E 73 62 ; 
8E7F:                6C B9 91 7A D1 B5 F0 A4 21 ; 
;
;                    THE KEY TURNS, THE LOCK CLICKS, AND THE CABINET SPRINGS
;                    OPEN!
;
8E88:             17 27 00               ;         COM_17_move_to(obj=OBJ_27_SHOTGUN, destination=nowhere)
8E8B:             17 28 26               ;         COM_17_move_to(obj=OBJ_28_SHOTGUN, destination=OBJ_26_GUN_CABINET)
8E8E:             1C 26                  ;         COM_1C_set_var_object(obj=OBJ_26_GUN_CABINET)
8E90:             29                     ;         COM_29_print_open_var()
8E91:             2A                     ;         UNKNOWN2A
8E92:             38                     ;         COM_38_bump_score()
8E93:          0D 28                     ;       COM_0D_while_pass length=0x0028
8E95:             0E 04                  ;         COM_0E_while_fail length=0x0004
8E97:                0A 3A               ;           COM_0A_is_input_phrase(phrase=OPEN u....... WITH u.......)
8E99:                0A 42               ;           COM_0A_is_input_phrase(phrase=UNLOCK u....... WITH u.......)
8E9B:             09 24                  ;         COM_09_compare_to_second_noun(obj=OBJ_24_CROWBAR)
8E9D:             04 1C                  ;         COM_04_print_command length=0x001C
8E9F:                5F BE 49 16 8B 54 03 A0 5F BE D3 14 10 4E 73 62 ; 
8EAF:                4B 7B 81 BF 66 17 00 B3 C8 6A A3 A0 ; 
;
;                    THE LOCK ON THE CABINET IS TOO STRONG FOR 
;
8EBB:             A9                     ;         FN_A9_PRINT_noun2
8EBC:             8B                     ;         FN_8B_PRINT_PERIOD
8EBD:          0D 0A                     ;       COM_0D_while_pass length=0x000A
8EBF:             0E 04                  ;         COM_0E_while_fail length=0x0004
8EC1:                0A 3A               ;           COM_0A_is_input_phrase(phrase=OPEN u....... WITH u.......)
8EC3:                0A 42               ;           COM_0A_is_input_phrase(phrase=UNLOCK u....... WITH u.......)
8EC5:             14                     ;         COM_14_execute_and_reverse_status next command
8EC6:             09 1F                  ;         COM_09_compare_to_second_noun(obj=OBJ_1F_SMALL_KEY_CAB)
8EC8:             BA                     ;         FN_BA_??
8EC9:    02 08                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0008
;           GUN CABINET 
8ECB:       30 6F D3 14 10 4E 73 62      ; 

; -------------- Object OBJ_27_SHOTGUN --------------
8ED3: 39 53                              ; Word_num=0x39 SHOTGU, length=0x0053
8ED5: 8E 02 C0                           ; Location=0x8E, disk_section=2, data=0, attributes=0b11000000
8ED8:    03 2C                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x002C
8EDA:       04 2A                        ;     COM_04_print_command length=0x002A
8EDC:          5F BE 5B B1 4B 7B 4E 45 06 9E F3 5F 87 5B 7F 4E ; 
8EEC:          AB 14 6F B3 15 8A 86 74 30 6F 49 16 97 54 0B 58 ; 
8EFC:          96 96 DB 72 04 53 8F 7A 9B C1 ; 
;
;              THERE IS A LOADED DOUBLE BARREL SHOTGUN LOCKED IN THE
;              CABINET.
;
8F06:    07 19                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0019
8F08:       0D 17                        ;     COM_0D_while_pass length=0x0017
8F0A:          0E 04                     ;       COM_0E_while_fail length=0x0004
8F0C:             0A 05                  ;         COM_0A_is_input_phrase(phrase=GET ..C..... * *)
8F0E:             0A 43                  ;         COM_0A_is_input_phrase(phrase=GET ..C..... WITH ..C.....)
8F10:          04 0F                     ;       COM_04_print_command length=0x000F
8F12:             5F BE D3 14 10 4E 73 62 4B 7B 75 8D A6 85 2E ; 
;
;                 THE CABINET IS LOCKED.
;
8F21:    02 05                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0005
;           SHOTGUN
8F23:       29 B8 47 BE 4E               ; 

; -------------- Object OBJ_28_SHOTGUN --------------
8F28: 39 2E                              ; Word_num=0x39 SHOTGU, length=0x002E
8F2A: 00 00 E0                           ; Location=0x00, disk_section=0, data=0, attributes=0b11100000
8F2D:    03 01                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0001
8F2F:       80                           ;     FN_80_PRINT_SHOTGUN_HERE
8F30:    07 1C                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x001C
8F32:       0D 1A                        ;     COM_0D_while_pass length=0x001A
8F34:          0E 06                     ;       COM_0E_while_fail length=0x0006
8F36:             0A 0B                  ;         COM_0A_is_input_phrase(phrase=LOOK * AT u.......)
8F38:             0A 10                  ;         COM_0A_is_input_phrase(phrase=LOOK * IN ......O.)
8F3A:             0A 4C                  ;         COM_0A_is_input_phrase(phrase=LOOK * ON .......L)
8F3C:          0E 06                     ;       COM_0E_while_fail length=0x0006
8F3E:             03 28 29               ;         COM_03_is_located(owner=OBJ_28_SHOTGUN, obj=OBJ_29_??)
8F41:             03 28 2A               ;         COM_03_is_located(owner=OBJ_28_SHOTGUN, obj=OBJ_2A_??)
8F44:          A8                        ;       FN_A8_PRINT_noun1
8F45:          04 07                     ;       COM_04_print_command length=0x0007
8F47:             4B 7B 73 8D E6 59 21   ; 
;
;                 IS LOADED!
;
8F4E:    0C 01                           ;   Section=0C:SECTION_0C_WEIGHT, length=0x0001
8F50:       15                           ;     Weight=21
8F51:    02 05                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0005
;           SHOTGUN
8F53:       29 B8 47 BE 4E               ; 

; -------------- Object OBJ_29_?? --------------
8F58: 00 0E                              ; Word_num=0x00 -none-, length=0x000E
8F5A: 28 00 A0                           ; Location=0x28, disk_section=0, data=0, attributes=0b10100000
8F5D:    08 09                           ;   Section=08:SECTION_08_EVERY_TURN, length=0x0009
8F5F:       0D 07                        ;     COM_0D_while_pass length=0x0007
8F61:          14                        ;       COM_14_execute_and_reverse_status next command
8F62:          03 28 2A                  ;       COM_03_is_located(owner=OBJ_28_SHOTGUN, obj=OBJ_2A_??)
8F65:          1C 29                     ;       COM_1C_set_var_object(obj=OBJ_29_??)
8F67:          BC                        ;       FN_BC_??

; -------------- Object OBJ_2A_?? --------------
8F68: 00 0A                              ; Word_num=0x00 -none-, length=0x000A
8F6A: 28 00 A0                           ; Location=0x28, disk_section=0, data=0, attributes=0b10100000
8F6D:    08 05                           ;   Section=08:SECTION_08_EVERY_TURN, length=0x0005
8F6F:       0D 03                        ;     COM_0D_while_pass length=0x0003
8F71:          1C 2A                     ;       COM_1C_set_var_object(obj=OBJ_2A_??)
8F73:          BC                        ;       FN_BC_??

; -------------- Object OBJ_2B_GAS_PUMP --------------
8F74: 3A 6C                              ; Word_num=0x3A PUMP, length=0x006C
8F76: 82 01 81                           ; Location=0x82, disk_section=1, data=0, attributes=0b10000001
8F79:    03 22                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0022
8F7B:       04 20                        ;     COM_04_print_command length=0x0020
8F7D:          83 48 BE 9F 4B 15 23 B8 0F A0 09 58 55 8B D6 B5 ; 
8F8D:          53 A0 15 6C EF 16 D3 93 FB B9 4D 98 9F 15 7F B1 ; 
;
;              AN OLD FASHIONED GLASS TOP GAS PUMP STANDS HERE.
;
8F9D:    07 3B                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x003B
8F9F:       0D 39                        ;     COM_0D_while_pass length=0x0039
8FA1:          0E 04                     ;       COM_0E_while_fail length=0x0004
8FA3:             0A 08                  ;         COM_0A_is_input_phrase(phrase=READ .....?.. * *)
8FA5:             0A 0B                  ;         COM_0A_is_input_phrase(phrase=LOOK * AT u.......)
8FA7:          04 31                     ;       COM_04_print_command length=0x0031
8FA9:             3B 95 41 6E 4F 5B C9 B9 D6 15 53 17 6E DF 6A 13 ; 
8FB9:             05 3F 9E 61 D2 B5 23 62 0E 6C 80 8D 63 F4 96 77 ; 
8FC9:             AF 14 16 BC F4 72 A5 5E 99 16 73 15 CE B5 5E 60 ; 
8FD9:             2E                     ; 
;
;                 MY GOODNESS! IT SAYS, "33 CENTS PER GALLON." I'D BET
;                 THERE'S NO GAS LEFT.
;
8FDA:    02 06                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0006
;           GAS PUMP 
8FDC:       15 6C EF 16 D3 93            ; 

; -------------- Object OBJ_2C_PADLOCK --------------
8FE2: 29 0D                              ; Word_num=0x29 PADLOC, length=0x000D
8FE4: 2B 60 88                           ; Location=0x2B, disk_section=0, data=6, attributes=0b10001000
8FE7:    07 01                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0001
8FE9:       BA                           ;     FN_BA_??
8FEA:    02 05                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0005
;           PADLOCK
8FEC:       46 A4 75 8D 4B               ; 

; -------------- Object OBJ_2D_JACK-O-MATIC --------------
8FF1: 31 5D                              ; Word_num=0x31 JACK, length=0x005D
8FF3: 83 01 A4                           ; Location=0x83, disk_section=1, data=0, attributes=0b10100100
8FF6:    03 10                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0010
8FF8:       04 0E                        ;     COM_04_print_command length=0x000E
8FFA:          5F BE 5B B1 4B 7B 4C 45 DD 46 9F 15 7F B1 ; 
;
;              THERE IS A JACK HERE.
;
9008:    07 3E                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x003E
900A:       0D 3C                        ;     COM_0D_while_pass length=0x003C
900C:          0A 08                     ;       COM_0A_is_input_phrase(phrase=READ .....?.. * *)
900E:          04 15                     ;       COM_04_print_command length=0x0015
9010:             2B 1C AD 54 1F A2 83 49 C6 51 4F 61 DB D6 B6 93 ; 
9020:             33 61 1A 40 22         ; 
;
;                 "JACK-O-MATIC DELUXE MODEL 333"
;
9025:          25                        ;       COM_25_print_linefeed()
9026:          04 20                     ;       COM_04_print_command length=0x0020
9028:             2B 1C 8B 54 57 C6 D0 15 0C BA E6 C3 C0 7A 33 BB ; 
9038:             76 A7 EB 15 8B 54 03 A0 8F 2A 85 73 DF 8B 63 F4 ; 
;
;                 "JACK USE INSTRUCTIONS, PUT JACK ON <VEHICLE>." 
;
9048:    07 01                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0001
904A:       29                           ;     COM_29_print_open_var()
904B:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           JACK
904D:       C5 7E 4B                     ; 

; -------------- Object OBJ_2E_RUSTY_JEEP --------------
9050: 32 77                              ; Word_num=0x32 JEEP, length=0x0077
9052: 86 01 81                           ; Location=0x86, disk_section=1, data=0, attributes=0b10000001
9055:    03 14                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0014
9057:       04 12                        ;     COM_04_print_command length=0x0012
9059:          5F BE 5B B1 4B 7B 54 45 66 C6 4C DB 32 60 9F 15 ; 
9069:          7F B1                     ; 
;
;              THERE IS A RUSTY JEEP HERE.
;
906B:    07 53                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0053
906D:       0B 51 0A                     ;     COM_0B_switch length=0x0051, function=COM_0A_is_input_phrase(phrase_num)
9070:          36                        ;       COM_0A_is_input_phrase("ENTER * * *")
9071:          17                        ;       ELSE goto=0x9089
9072:             0D 15                  ;         COM_0D_while_pass length=0x0015
9074:                17 01 2E            ;           COM_17_move_to(obj=OBJ_01_PLAYER, destination=OBJ_2E_RUSTY_JEEP)
9077:                04 10               ;           COM_04_print_command length=0x0010
9079:                   C7 DE 94 14 50 5E 6B A1 83 7A 5F BE EF 15 F7 61 ; 
;
;                       YOU ARE NOW IN THE JEEP.
;
9089:          37                        ;       COM_0A_is_input_phrase("CLIMB * OUT *")
908A:          1A                        ;       ELSE goto=0x90A5
908B:             0D 18                  ;         COM_0D_while_pass length=0x0018
908D:                1C 01               ;           COM_1C_set_var_object(obj=OBJ_01_PLAYER)
908F:                10                  ;           COM_10_drop_var()
9090:                04 13               ;           COM_04_print_command length=0x0013
9092:                   C7 DE 94 14 50 5E 6B A1 36 A1 B8 16 82 17 4C 5E ; 
90A2:                   32 60 2E         ; 
;
;                       YOU ARE NOW OUT OF THE JEEP.
;
90A5:          52                        ;       COM_0A_is_input_phrase("START u....... * *")
90A6:          19                        ;       ELSE goto=0x90C0
90A7:             04 17                  ;         COM_04_print_command length=0x0017
90A9:                06 9A 90 73 5B 70 5F BE AB 14 3F C0 7B B4 B5 94 ; 
90B9:                04 BC 46 5E 86 5F 21 ; 
;
;                    NOTHING. THE BATTERY MUST BE DEAD!
;
90C0:    02 07                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0007
;           RUSTY JEEP
90C2:       F5 B3 FB C0 67 7F 50         ; 

; -------------- Object OBJ_2F_FLAT_TIRE --------------
90C9: 21 45                              ; Word_num=0x21 TIRE, length=0x0045
90CB: 2E 00 A0                           ; Location=0x2E, disk_section=0, data=0, attributes=0b10100000
90CE:    03 14                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0014
90D0:       04 12                        ;     COM_04_print_command length=0x0012
90D2:          5F BE 5B B1 4B 7B 48 45 56 8B 83 17 5B B1 F4 72 ; 
90E2:          DB 63                     ; 
;
;              THERE IS A FLAT TIRE HERE. 
;
90E4:    07 1C                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x001C
90E6:       0D 1A                        ;     COM_0D_while_pass length=0x001A
90E8:          0E 04                     ;       COM_0E_while_fail length=0x0004
90EA:             0A 05                  ;         COM_0A_is_input_phrase(phrase=GET ..C..... * *)
90EC:             0A 43                  ;         COM_0A_is_input_phrase(phrase=GET ..C..... WITH ..C.....)
90EE:          14                        ;       COM_14_execute_and_reverse_status next command
90EF:          03 2E 2D                  ;       COM_03_is_located(owner=OBJ_2E_RUSTY_JEEP, obj=OBJ_2D_JACK-O-MATIC)
90F2:          04 0E                     ;       COM_04_print_command length=0x000E
90F4:             C7 DE 77 16 F3 B9 57 C6 7B 14 C5 7E 5B 89 ; 
;
;                 YOU MUST USE A JACK. 
;
9102:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
9104:       22                           ;     FLAT
9105:    0C 01                           ;   Section=0C:SECTION_0C_WEIGHT, length=0x0001
9107:       29                           ;     Weight=41
9108:    02 06                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0006
;           FLAT TIRE
910A:       7B 67 16 BC 2F 7B            ; 

; -------------- Object OBJ_30_SPARE_TIRE --------------
9110: 21 42                              ; Word_num=0x21 TIRE, length=0x0042
9112: 86 01 A0                           ; Location=0x86, disk_section=1, data=0, attributes=0b10100000
9115:    03 14                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0014
9117:       04 12                        ;     COM_04_print_command length=0x0012
9119:          5F BE 5B B1 4B 7B 55 45 54 A4 56 5E 2F 7B 9F 15 ; 
9129:          7F B1                     ; 
;
;              THERE IS A SPARE TIRE HERE.
;
912B:    07 18                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0018
912D:       0D 16                        ;     COM_0D_while_pass length=0x0016
912F:          0A 4B                     ;       COM_0A_is_input_phrase(phrase=DROP ..C..... ON .......L)
9131:          14                        ;       COM_14_execute_and_reverse_status next command
9132:          03 2E 2D                  ;       COM_03_is_located(owner=OBJ_2E_RUSTY_JEEP, obj=OBJ_2D_JACK-O-MATIC)
9135:          04 0E                     ;       COM_04_print_command length=0x000E
9137:             C7 DE 77 16 F3 B9 57 C6 7B 14 C5 7E 5B 89 ; 
;
;                 YOU MUST USE A JACK. 
;
9145:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
9147:       23                           ;     SPARE
9148:    0C 01                           ;   Section=0C:SECTION_0C_WEIGHT, length=0x0001
914A:       29                           ;     Weight=41
914B:    02 07                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0007
;           SPARE TIRE
914D:       5B B9 5B B1 94 BE 45         ; 

; -------------- Object OBJ_31_SPHORX --------------
9154: 1A 09                              ; Word_num=0x1A DESK, length=0x0009
9156: 85 09 81                           ; Location=0x85, disk_section=9, data=0, attributes=0b10000001
9159:    02 04                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0004
;           SPHORX
915B:       62 B9 C2 A0                  ; 

; -------------- Object OBJ_32_SHOVEL --------------
915F: 26 20                              ; Word_num=0x26 SHOVEL, length=0x0020
9161: DC 03 E0                           ; Location=0xDC, disk_section=3, data=0, attributes=0b11100000
9164:    03 12                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0012
9166:       04 10                        ;     COM_04_print_command length=0x0010
9168:          5F BE 5B B1 4B 7B 55 45 88 74 33 61 F4 72 DB 63 ; 
;
;              THERE IS A SHOVEL HERE. 
;
9178:    0C 01                           ;   Section=0C:SECTION_0C_WEIGHT, length=0x0001
917A:       15                           ;     Weight=21
917B:    02 04                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0004
;           SHOVEL
917D:       29 B8 6E CA                  ; 

; -------------- Object OBJ_33_RATTLE_SNAKE --------------
9181: 0C 81 B2                           ; Word_num=0x0C SNAKE, length=0x01B2
9184: DC 03 90                           ; Location=0xDC, disk_section=3, data=0, attributes=0b10010000
9187:    03 2F                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x002F
9189:       04 2D                        ;     COM_04_print_command length=0x002D
918B:          5F BE 5B B1 4B 7B 50 45 8F 7A 59 15 F3 A0 83 5A ; 
919B:          C0 93 04 58 DD 46 2B 17 46 C0 55 5E CD 97 45 5E ; 
91AB:          4E 9F F3 5F 03 A0 5F BE 56 15 44 A0 2E ; 
;
;              THERE IS A NINE FOOT DIAMOND BACK RATTLE SNAKE COILED ON
;              THE FLOOR.
;
91B8:    09 02                           ;   Section=09:SECTION_09_HIT_POINTS, length=0x0002
91BA:       46 46                        ;     Hit_points=70_of_70
91BC:    07 6E                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x006E
91BE:       0E 6C                        ;     COM_0E_while_fail length=0x006C
91C0:          0D 3A                     ;       COM_0D_while_pass length=0x003A
91C2:             0A 09                  ;         COM_0A_is_input_phrase(phrase=ATTACK ...P.... WITH .v......)
91C4:             0E 06                  ;         COM_0E_while_fail length=0x0006
91C6:                09 28               ;           COM_09_compare_to_second_noun(obj=OBJ_28_SHOTGUN)
91C8:                09 32               ;           COM_09_compare_to_second_noun(obj=OBJ_32_SHOVEL)
91CA:                09 24               ;           COM_09_compare_to_second_noun(obj=OBJ_24_CROWBAR)
91CC:             04 06                  ;         COM_04_print_command length=0x0006
91CE:                C7 DE 2B 17 57 7B   ; 
;
;                    YOU RAISE
;
91D4:             A9                     ;         FN_A9_PRINT_noun2
91D5:             04 22                  ;         COM_04_print_command length=0x0022
91D7:                4F A1 9B AF 34 A1 9F 15 F3 46 8E 48 81 13 4F 72 ; 
91E7:                E3 06 E3 59 0A 8A 5B 7A 48 45 34 79 9B 53 89 4E ; 
91F7:                6B CE               ; 
;
;                    OVER YOUR HEAD AND "WHAM!" DEAL HIM A FIERCE BLOW! 
;
91F9:             1A                     ;         COM_1A_set_var_to_first_noun()
91FA:             1D 28                  ;         COM_1D_attack_var(points=40)
91FC:          0D 2E                     ;       COM_0D_while_pass length=0x002E
91FE:             0E 06                  ;         COM_0E_while_fail length=0x0006
9200:                0A 09               ;           COM_0A_is_input_phrase(phrase=ATTACK ...P.... WITH .v......)
9202:                0A 05               ;           COM_0A_is_input_phrase(phrase=GET ..C..... * *)
9204:                0A 43               ;           COM_0A_is_input_phrase(phrase=GET ..C..... WITH ..C.....)
9206:             0E 04                  ;         COM_0E_while_fail length=0x0004
9208:                09 5C               ;           COM_09_compare_to_second_noun(obj=OBJ_5C_PAIR_HANDS)
920A:                09 00               ;           COM_09_compare_to_second_noun(obj=nothing)
920C:             04 1E                  ;         COM_04_print_command length=0x001E
920E:                C7 DE 81 15 0B BC AB BB C7 DE 81 15 0B BC AB BB ; 
921E:                42 A0 6B B5 C7 DE 0C 15 6A A0 F3 5F 97 7B ; 
;
;                    YOU GOT IT! YOU GOT IT! OOPS! YOU DROPPED IT.
;
922C:    08 80 D7                        ;   Section=08:SECTION_08_EVERY_TURN, length=0x00D7
922F:       0D 80 D4                     ;     COM_0D_while_pass length=0x00D4
9232:          01 01                     ;       COM_01_is_in_pack_or_room(obj=OBJ_01_PLAYER)
9234:          14                        ;       COM_14_execute_and_reverse_status next command
9235:          0E 04                     ;       COM_0E_while_fail length=0x0004
9237:             0A 01                  ;         COM_0A_is_input_phrase(phrase=NORTH * * *)
9239:             0A 03                  ;         COM_0A_is_input_phrase(phrase=EAST * * *)
923B:          0B 80 C5 05               ;       COM_0B_switch length=0x00C5, function=COM_05_is_less_equal_last_random(value)
923F:             55                     ;         COM_05_is_less_equal_last_random(value=85)
9240:             46                     ;         ELSE goto=0x9287
9241:                1F 44               ;           COM_1F_print2 length=0x0044
9243:                   5F BE 57 17 1F B3 B3 9A 83 67 C5 98 D6 15 AE B7 ; 
9253:                   96 64 73 A1 4D B1 51 18 EB C1 68 4D AF A0 51 18 ; 
9263:                   45 C2 83 48 63 B1 16 56 A3 15 D0 B5 26 60 DB 8B ; 
9273:                   1B B8 13 B3 D0 65 CB 6E 87 A5 17 B1 51 18 23 C6 ; 
9283:                   9B B8 1B 9C      ; 
;
;                       THE SERPENT FLINGS ITSELF TOWARDS YOU! BEFORE YOU CAN
;                       REACT, HIS NEEDLE SHARP FANGS PIERCE YOUR SKIN.
;
9287:             AA                     ;         COM_05_is_less_equal_last_random(value=170)
9288:             3C                     ;         ELSE goto=0x92C5
9289:                1F 3A               ;           COM_1F_print2 length=0x003A
928B:                   C7 DE 87 AF 3D 49 33 17 AB 98 56 D1 16 71 DB 72 ; 
929B:                   47 B9 33 98 C3 9E C7 DE 95 AF AF 55 5B 48 4B 49 ; 
92AB:                   5F BE 60 17 17 48 CB 23 E7 BD 53 BE F0 A4 8C 62 ; 
92BB:                   7F 49 51 18 23 C6 7F 67 11 B8 ; 
;
;                       YOUR EARS RING WITH THE SOUND OF YOUR SCREAM AS THE SNAKE'S
;                       TEETH PENETRATE YOUR FLESH!
;
92C5:             FF                     ;         COM_05_is_less_equal_last_random(value=255)
92C6:             3C                     ;         ELSE goto=0x9303
92C7:                1F 3A               ;           COM_1F_print2 length=0x003A
92C9:                   5F BE 60 17 17 48 66 17 0D B2 49 62 51 18 48 C2 ; 
92D9:                   2E 60 7B 14 29 B8 03 A1 AB 98 4B A4 8B 96 9B 96 ; 
92E9:                   34 A1 3F 16 C3 6A CA B5 4B 7B D0 65 CB 6E 87 A5 ; 
92F9:                   17 B1 90 14 94 14 F4 BD DB E0 ; 
;
;                       THE SNAKE STRIKES! YOU FEEL A SHOOTING PAIN IN YOUR LEG AS
;                       HIS FANGS PIERCE AN ARTERY.
;
9303:          17 35 01                  ;       COM_17_move_to(obj=OBJ_35_??, destination=OBJ_01_PLAYER)
9306:    0A 14                           ;   Section=0A:SECTION_0A_UPON_DEATH, length=0x0014
9308:       0D 12                        ;     COM_0D_while_pass length=0x0012
930A:          04 0C                     ;       COM_04_print_command length=0x000C
930C:             5F BE 60 17 17 48 D5 15 FF 14 17 47 ; 
;
;                 THE SNAKE IS DEAD.
;
9318:          38                        ;       COM_38_bump_score()
9319:          1E 33 34                  ;       COM_1E_swap(obj1=OBJ_33_RATTLE_SNAKE, obj2=OBJ_34_DEAD_SNAKE)
931C:    02 18                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0018
;           NINE FOOT DIAMOND BACK RATTLE SNAKE 
931E:       10 99 48 5E 46 A0 03 15 71 48 33 98 C5 4C D4 83 ; 
932E:       8E 49 DB 8B 0B B9 9B 85      ; 

; -------------- Object OBJ_34_DEAD_SNAKE --------------
9336: 0C 25                              ; Word_num=0x0C SNAKE, length=0x0025
9338: 00 03 A0                           ; Location=0x00, disk_section=3, data=0, attributes=0b10100000
933B:    03 14                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0014
933D:       04 12                        ;     COM_04_print_command length=0x0012
933F:          5F BE 5B B1 4B 7B 46 45 86 5F 60 17 17 48 9F 15 ; 
934F:          7F B1                     ; 
;
;              THERE IS A DEAD SNAKE HERE.
;
9351:    0C 01                           ;   Section=0C:SECTION_0C_WEIGHT, length=0x0001
9353:       09                           ;     Weight=9
9354:    02 07                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0007
;           DEAD SNAKE
9356:       E3 59 15 58 CD 97 45         ; 

; -------------- Object OBJ_35_?? --------------
935D: 20 0D                              ; Word_num=0x20 ??20??, length=0x000D
935F: 00 00 80                           ; Location=0x00, disk_section=0, data=0, attributes=0b10000000
9362:    08 08                           ;   Section=08:SECTION_08_EVERY_TURN, length=0x0008
9364:       0D 06                        ;     COM_0D_while_pass length=0x0006
9366:          01 01                     ;       COM_01_is_in_pack_or_room(obj=OBJ_01_PLAYER)
9368:          1C 01                     ;       COM_1C_set_var_object(obj=OBJ_01_PLAYER)
936A:          1D 11                     ;       COM_1D_attack_var(points=17)

; -------------- Object OBJ_36_FOOD --------------
936C: 1C 58                              ; Word_num=0x1C FOOD, length=0x0058
936E: 94 03 A0                           ; Location=0x94, disk_section=3, data=0, attributes=0b10100000
9371:    03 12                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0012
9373:       04 10                        ;     COM_04_print_command length=0x0010
9375:          5F BE 5B B1 4B 7B 3F B9 48 5E 36 A0 9F 15 7F B1 ; 
;
;              THERE IS SOME FOOD HERE.
;
9385:    07 2C                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x002C
9387:       0D 2A                        ;     COM_0D_while_pass length=0x002A
9389:          0A 15                     ;       COM_0A_is_input_phrase(phrase=EAT u....... * *)
938B:          A8                        ;       FN_A8_PRINT_noun1
938C:          04 21                     ;       COM_04_print_command length=0x0021
938E:             15 D0 66 17 3F 48 04 EE 73 C6 03 BA F3 8C C3 9E ; 
939E:             89 73 10 71 8C C6 83 7B 0B A0 05 8A 1E A0 9E 61 ; 
93AE:             2E                     ; 
;
;                 WAS STALE, BUT STILL OF HIGH NUTRITIONAL CONTENT.
;
93AF:          1C 01                     ;       COM_1C_set_var_object(obj=OBJ_01_PLAYER)
93B1:          23 23                     ;       COM_23_heal_var(points=35)
93B3:    0C 01                           ;   Section=0C:SECTION_0C_WEIGHT, length=0x0001
93B5:       06                           ;     Weight=6
93B6:    02 0E                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x000E
;           SMALL AMOUNT OF FOOD 
93B8:       E3 B8 F3 8C 71 48 9E C5 B8 16 59 15 73 9E ; 

; -------------- Object OBJ_37_STEEL_SAFE --------------
93C6: 1D 31                              ; Word_num=0x1D SAFE, length=0x0031
93C8: 9A 64 8A                           ; Location=0x9A, disk_section=4, data=6, attributes=0b10001010
93CB:    03 24                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0024
93CD:       04 22                        ;     COM_04_print_command length=0x0022
93CF:          83 7A 5F BE 61 17 82 C6 F3 17 16 8D 51 18 45 C2 ; 
93DF:          83 48 A7 B7 7B 14 54 8B 9B 6C FF B9 33 61 08 B7 ; 
93EF:          DB 63                     ; 
;
;              IN THE SOUTH WALL, YOU CAN SEE A LARGE STEEL SAFE. 
;
93F1:    07 01                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0001
93F3:       BA                           ;     FN_BA_??
93F4:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           SAFE
93F6:       08 B7 45                     ; 

; -------------- Object OBJ_38_MONEY --------------
93F9: 27 49                              ; Word_num=0x27 MONEY, length=0x0049
93FB: 4C 00 A4                           ; Location=0x4C, disk_section=0, data=0, attributes=0b10100100
93FE:    03 13                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0013
9400:       04 11                        ;     COM_04_print_command length=0x0011
9402:          5F BE 5B B1 4B 7B 3F B9 4F 5E 0F A0 4A DB 2F 62 ; 
9412:          2E                        ; 
;
;              THERE IS SOME MONEY HERE.
;
9413:    07 1C                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x001C
9415:       0D 1A                        ;     COM_0D_while_pass length=0x001A
9417:          0A 08                     ;       COM_0A_is_input_phrase(phrase=READ .....?.. * *)
9419:          04 16                     ;       COM_04_print_command length=0x0016
941B:             10 1C 81 15 19 58 56 5E F5 B3 9B C1 B7 C0 D3 9A ; 
942B:             09 15 FB 8C 8C B3      ; 
;
;                 "IN GOD WE TRUST. TWENTY DOLLARS"
;
9431:    0C 01                           ;   Section=0C:SECTION_0C_WEIGHT, length=0x0001
9433:       06                           ;     Weight=6
9434:    02 0E                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x000E
;           LARGE AMOUNT OF MONEY
9436:       54 8B 9B 6C 71 48 9E C5 B8 16 71 16 7B 98 ; 

; -------------- Object OBJ_39_DYNAMITE --------------
9444: 1E 81 21                           ; Word_num=0x1E DYNAMI, length=0x0121
9447: DB 02 A4                           ; Location=0xDB, disk_section=2, data=0, attributes=0b10100100
944A:    03 19                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0019
944C:       04 17                        ;     COM_04_print_command length=0x0017
944E:          5F BE 5B B1 4B 7B 55 45 85 BE D1 83 86 64 8B DE ; 
945E:          D6 92 4A 5E 2F 62 2E      ; 
;
;              THERE IS A STICK OF DYNAMITE HERE.
;
9465:    0C 01                           ;   Section=0C:SECTION_0C_WEIGHT, length=0x0001
9467:       08                           ;     Weight=8
9468:    07 80 8A                        ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x008A
946B:       0B 80 87 0A                  ;     COM_0B_switch length=0x0087, function=COM_0A_is_input_phrase(phrase_num)
946F:          08                        ;       COM_0A_is_input_phrase("READ .....?.. * *")
9470:          5C                        ;       ELSE goto=0x94CD
9471:             0D 5A                  ;         COM_0D_while_pass length=0x005A
9473:                04 12               ;           COM_04_print_command length=0x0012
9475:                   09 1C F4 99 DB 8B 9E 61 3A 62 15 B2 6E 62 D0 15 ; 
9485:                   5C 57            ; 
;
;                       "IGNOBLE ENTERPRISES, INC."
;
9487:                25                  ;           COM_25_print_linefeed()
9488:                25                  ;           COM_25_print_linefeed()
9489:                04 15               ;           COM_04_print_command length=0x0015
948B:                   7E 19 15 26 40 61 C9 15 16 99 91 7A 13 15 CF 97 ; 
949B:                   7F 7B DF 13 22   ; 
;
;                       " << SELF IGNITING DYNAMITE >>"
;
94A0:                25                  ;           COM_25_print_linefeed()
94A1:                04 0D               ;           COM_04_print_command length=0x000D
94A3:                   DB 1B 46 98 59 5E 82 7B D3 14 59 B1 22 ; 
;
;                       "HANDLE WITH CARE!"
;
94B0:                25                  ;           COM_25_print_linefeed()
94B1:                04 1A               ;           COM_04_print_command length=0x001A
94B3:                   C9 1D B5 17 B3 63 E6 23 0D B2 48 5E 57 C6 C7 1F ; 
94C3:                   C5 C9 96 C3 43 5E 63 B1 E3 06 ; 
;
;                       "TO USE, 'STRIKE FUSE' EVACUATE AREA!" 
;
94CD:          53                        ;       COM_0A_is_input_phrase("STRIKE u....... * *")
94CE:          26                        ;       ELSE goto=0x94F5
94CF:             0D 24                  ;         COM_0D_while_pass length=0x0024
94D1:                1A                  ;           COM_1A_set_var_to_first_noun()
94D2:                8F                  ;           FN_8F_TRY_TO_GET_OBJECT
94D3:                04 1D               ;           COM_04_print_command length=0x001D
94D5:                   5F BE 13 15 CF 97 7F 7B AF 14 50 6D CA B5 65 7B ; 
94E5:                   91 7A 90 14 15 58 76 A7 F4 BD 91 7A 21 ; 
;
;                       THE DYNAMITE BEGINS HISSING AND SPUTTERING!
;
94F2:                17 4B 39            ;           COM_17_move_to(obj=OBJ_4B_??, destination=OBJ_39_DYNAMITE)
94F5:    08 63                           ;   Section=08:SECTION_08_EVERY_TURN, length=0x0063
94F7:       0E 61                        ;     COM_0E_while_fail length=0x0061
94F9:          14                        ;       COM_14_execute_and_reverse_status next command
94FA:          03 39 4B                  ;       COM_03_is_located(owner=OBJ_39_DYNAMITE, obj=OBJ_4B_??)
94FD:          0D 14                     ;       COM_0D_while_pass length=0x0014
94FF:             0E 04                  ;         COM_0E_while_fail length=0x0004
9501:                0A 53               ;           COM_0A_is_input_phrase(phrase=STRIKE u....... * *)
9503:                0A 06               ;           COM_0A_is_input_phrase(phrase=DROP ..C..... * *)
9505:             1F 0C                  ;         COM_1F_print2 length=0x000C
9507:                E3 1B E5 B9 15 EE 76 A7 F4 BD E3 06 ; 
;
;                    "HISSS, SPUTTER!" 
;
9513:          0D 27                     ;       COM_0D_while_pass length=0x0027
9515:             01 01                  ;         COM_01_is_in_pack_or_room(obj=OBJ_01_PLAYER)
9517:             1C 01                  ;         COM_1C_set_var_object(obj=OBJ_01_PLAYER)
9519:             1F 19                  ;         COM_1F_print2 length=0x0019
951B:                01 4F 41 A0 EB 8F C7 DE 9B 15 5B CA 67 4D 84 96 ; 
952B:                89 8D 96 96 C4 9C 8D 7B 21 ; 
;
;                    BOOOOOM! YOU HAVE BEEN BLOWN TO BITS!
;
9534:             1D 69                  ;         COM_1D_attack_var(points=105)
9536:             17 39 00               ;         COM_17_move_to(obj=OBJ_39_DYNAMITE, destination=nowhere)
9539:             17 4B 00               ;         COM_17_move_to(obj=OBJ_4B_??, destination=nowhere)
953C:          0D 0B                     ;       COM_0D_while_pass length=0x000B
953E:             01 37                  ;         COM_01_is_in_pack_or_room(obj=OBJ_37_STEEL_SAFE)
9540:             1E 37 4C               ;         COM_1E_swap(obj1=OBJ_37_STEEL_SAFE, obj2=OBJ_4C_BLASTED_SAFE)
9543:             17 39 00               ;         COM_17_move_to(obj=OBJ_39_DYNAMITE, destination=nowhere)
9546:             17 4B 00               ;         COM_17_move_to(obj=OBJ_4B_??, destination=nowhere)
9549:          0D 0C                     ;       COM_0D_while_pass length=0x000C
954B:             01 4E                  ;         COM_01_is_in_pack_or_room(obj=OBJ_4E_BOULDER)
954D:             1E 4E 5A               ;         COM_1E_swap(obj1=OBJ_4E_BOULDER, obj2=OBJ_5A_ENTRANCE_CLEAR)
9550:             17 39 00               ;         COM_17_move_to(obj=OBJ_39_DYNAMITE, destination=nowhere)
9553:             38                     ;         COM_38_bump_score()
9554:             17 4B 00               ;         COM_17_move_to(obj=OBJ_4B_??, destination=nowhere)
9557:          17 4B 00                  ;       COM_17_move_to(obj=OBJ_4B_??, destination=nowhere)
955A:    02 0C                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x000C
;           STICK OF DYNAMITE 
955C:       03 BA 8B 54 C3 9E 10 5D 6B 48 DB BD ; 

; -------------- Object OBJ_3A_CONTROL_PANEL --------------
9568: 62 0E                              ; Word_num=0x62 CONSOL, length=0x000E
956A: 89 07 81                           ; Location=0x89, disk_section=7, data=0, attributes=0b10000001
956D:    02 09                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0009
;           CONTROL PANEL
956F:       40 55 F9 BF 12 8A 8F 48 4C   ; 

; -------------- Object OBJ_3B_RADIO --------------
9578: 12 80 BB                           ; Word_num=0x12 RADIO, length=0x00BB
957B: A2 02 80                           ; Location=0xA2, disk_section=2, data=0, attributes=0b10000000
957E:    03 01                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0001
9580:       B9                           ;     FN_B9_PRINT_JUKEBOX
9581:    07 80 AC                        ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x00AC
9584:       0D 80 A9                     ;     COM_0D_while_pass length=0x00A9
9587:          0A 50                     ;       COM_0A_is_input_phrase(phrase=TURN * ON u.......)
9589:          04 80 A0                  ;       COM_04_print_command length=0x00A0
958C:             24 1B 83 46 D5 83 AF 55 3F 60 DB F9 8E 48 82 17 ; 
959C:             48 5E 71 48 4B C6 75 5B 84 BF FF 18 DC F8 27 60 ; 
95AC:             4F 15 34 60 7C B3 3F B5 55 F4 8E BE 0B 8A 0F 9B ; 
95BC:             03 BA 16 6C 91 7A 82 17 55 5E EB BF B7 98 A8 17 ; 
95CC:             CE 9C 8E 48 91 7A D0 15 82 17 46 5E 57 62 D7 B3 ; 
95DC:             DF 16 66 A0 43 5E 5B B1 CB 62 23 56 90 BE D6 6A ; 
95EC:             DB 72 2F 49 48 45 A3 A0 CE 92 4B 62 39 49 8E C5 ; 
95FC:             59 F4 50 5E 6B A1 76 B1 38 C6 89 17 C7 16 94 AF ; 
960C:             87 60 54 8B EC 16 04 9F 7F 48 96 19 DB 72 C6 B0 ; 
961C:             AB 7A 69 4D 9D 7A E6 16 4B 4A AB 98 B5 94 EF 78 ; 
;
;                 "CRAAAK SCREEE... AND THE FAMOUS DOCTOR ...VREEE
;                 FEEERRRRR... STILL INVESTIGATING THE STRANGE UFO LANDING IN
;                 THE DESERT. PEOPLE ARE EVACUATING THE AREA FOR MILES
;                 AROUND. WE NOW RETURN TO OUR REGULAR PROGRAM." THE RADIO
;                 BEGINS PLAYING MUSIC.
;
962C:          1E 3B 3C                  ;       COM_1E_swap(obj1=OBJ_3B_RADIO, obj2=OBJ_3C_RADIO)
962F:          38                        ;       COM_38_bump_score()
9630:    02 04                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0004
;           RADIO 
9632:       C6 B0 AB 7A                  ; 

; -------------- Object OBJ_3C_RADIO --------------
9636: 12 64                              ; Word_num=0x12 RADIO, length=0x0064
9638: 00 02 80                           ; Location=0x00, disk_section=2, data=0, attributes=0b10000000
963B:    03 1E                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x001E
963D:       04 1C                        ;     COM_04_print_command length=0x001C
963F:          5F BE 2B 17 91 5A D0 15 82 17 45 5E B8 A0 23 62 ; 
964F:          4B 7B FB A5 D0 DD CF 6A 5B C6 5B 57 ; 
;
;              THE RADIO IN THE CORNER IS PLAYING MUSIC. 
;
965B:    07 39                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0039
965D:       0E 37                        ;     COM_0E_while_fail length=0x0037
965F:          0D 17                     ;       COM_0D_while_pass length=0x0017
9661:             0A 51                  ;         COM_0A_is_input_phrase(phrase=TURN * OFF u.......)
9663:             04 10                  ;         COM_04_print_command length=0x0010
9665:                5F BE 2B 17 91 5A AF 14 3F 55 4B 62 AB AD 97 62 ; 
;
;                    THE RADIO BECOMES QUIET.
;
9675:             1E 3C 4F               ;         COM_1E_swap(obj1=OBJ_3C_RADIO, obj2=OBJ_4F_RADIO)
9678:          0D 1C                     ;       COM_0D_while_pass length=0x001C
967A:             0A 50                  ;         COM_0A_is_input_phrase(phrase=TURN * ON u.......)
967C:             04 18                  ;         COM_04_print_command length=0x0018
967E:                43 77 EF 8D 13 47 9F 15 23 49 5F BE 77 16 45 B8 ; 
968E:                05 EE 85 48 1B BC 18 A1 ; 
;
;                    I ALREADY HEAR THE MUSIC, CAN'T YOU?
;
9696:    02 04                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0004
;           RADIO 
9698:       C6 B0 AB 7A                  ; 

; -------------- Object OBJ_3D_BOTTLE --------------
969C: 11 38                              ; Word_num=0x11 BOTTLE, length=0x0038
969E: 44 A0 AE                           ; Location=0x44, disk_section=0, data=10, attributes=0b10101110
96A1:    03 12                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0012
96A3:       04 10                        ;     COM_04_print_command length=0x0010
96A5:          5F BE 5B B1 4B 7B 44 45 0E A1 DB 8B F4 72 DB 63 ; 
;
;              THERE IS A BOTTLE HERE. 
;
96B5:    07 16                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0016
96B7:       0D 14                        ;     COM_0D_while_pass length=0x0014
96B9:          0A 08                     ;       COM_0A_is_input_phrase(phrase=READ .....?.. * *)
96BB:          04 10                     ;       COM_04_print_command length=0x0010
96BD:             C1 1B 73 9E 04 68 FA 17 73 49 CE 47 DB B5 DC 4A ; 
;
;                 "GOOD FOR WHAT AILS YA."
;
96CD:    0C 01                           ;   Section=0C:SECTION_0C_WEIGHT, length=0x0001
96CF:       06                           ;     Weight=6
96D0:    02 04                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0004
;           BOTTLE
96D2:       06 4F FF BE                  ; 

; -------------- Object OBJ_3E_?? --------------
96D6: 4A 06                              ; Word_num=0x4A BUTTON, length=0x0006
96D8: 00 07 00                           ; Location=0x00, disk_section=7, data=0, attributes=0b00000000
96DB:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
96DD:       15                           ;     BRASS

; -------------- Object OBJ_3F_YELLOW_BUTTON --------------
96DE: 4A 14                              ; Word_num=0x4A BUTTON, length=0x0014
96E0: FF 07 80                           ; Location=0xFF, disk_section=7, data=0, attributes=0b10000000
96E3:    07 01                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0001
96E5:       AF                           ;     FN_AF_PRINT_I_SEE_NO_noun1_HERE
96E6:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
96E8:       48                           ;     YELLOW
96E9:    02 09                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0009
;           YELLOW BUTTON
96EB:       2E DD 89 8D BF 14 49 C0 4E   ; 

; -------------- Object OBJ_40_RED_BUTTON --------------
96F4: 4A 12                              ; Word_num=0x4A BUTTON, length=0x0012
96F6: FF 07 80                           ; Location=0xFF, disk_section=7, data=0, attributes=0b10000000
96F9:    07 01                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0001
96FB:       AF                           ;     FN_AF_PRINT_I_SEE_NO_noun1_HERE
96FC:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
96FE:       13                           ;     RED
96FF:    02 07                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0007
;           RED BUTTON
9701:       66 B1 BF 14 49 C0 4E         ; 

; -------------- Object OBJ_41_BLUE_BUTTON --------------
9708: 4A 13                              ; Word_num=0x4A BUTTON, length=0x0013
970A: FF 07 80                           ; Location=0xFF, disk_section=7, data=0, attributes=0b10000000
970D:    07 01                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0001
970F:       AF                           ;     FN_AF_PRINT_I_SEE_NO_noun1_HERE
9710:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
9712:       0D                           ;     BLUE
9713:    02 08                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0008
;           BLUE BUTTON 
9715:       8F 4E 44 5E 8E C6 03 A0      ; 

; -------------- Object OBJ_42_ORANGE_BUTTON --------------
971D: 4A 14                              ; Word_num=0x4A BUTTON, length=0x0014
971F: FF 07 80                           ; Location=0xFF, disk_section=7, data=0, attributes=0b10000000
9722:    07 01                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0001
9724:       AF                           ;     FN_AF_PRINT_I_SEE_NO_noun1_HERE
9725:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
9727:       49                           ;     ORANGE
9728:    02 09                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0009
;           ORANGE BUTTON
972A:       AB A0 B7 98 BF 14 49 C0 4E   ; 

; -------------- Object OBJ_43_BROWN_LIQUID --------------
9733: 4C 3B                              ; Word_num=0x4C WHISKE, length=0x003B
9735: 3D 10 A0                           ; Location=0x3D, disk_section=0, data=1, attributes=0b10100000
9738:    01 02                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0002
973A:       74                           ;     CLEAR
973B:       73                           ;     BROWN
973C:    07 22                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0022
973E:       0E 20                        ;     COM_0E_while_fail length=0x0020
9740:          0D 12                     ;       COM_0D_while_pass length=0x0012
9742:             0A 4F                  ;         COM_0A_is_input_phrase(phrase=DRINK u....... * *)
9744:             04 0A                  ;         COM_04_print_command length=0x000A
9746:                13 9F E9 99 E9 16 61 7B 2B 96 ; 
;
;                    OH NO! POISON! 
;
9750:             1C 01                  ;         COM_1C_set_var_object(obj=OBJ_01_PLAYER)
9752:             1D 6E                  ;         COM_1D_attack_var(points=110)
9754:          0D 0A                     ;       COM_0D_while_pass length=0x000A
9756:             0A 59                  ;         COM_0A_is_input_phrase(phrase=TASTE u....... * *)
9758:             04 06                  ;         COM_04_print_command length=0x0006
975A:                23 D1 97 B8 EB DA   ; 
;
;                    WHISKEY! 
;
9760:    02 0E                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x000E
;           CLEAR BROWN SOLUTION 
9762:       BF 54 23 49 79 4F 03 D2 3E B9 83 C6 03 A0 ; 

; -------------- Object OBJ_44_BAR --------------
9770: 4D 07                              ; Word_num=0x4D BAR, length=0x0007
9772: A2 02 81                           ; Location=0xA2, disk_section=2, data=0, attributes=0b10000001
9775:    02 02                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0002
;           BAR
9777:       D4 4C                        ; 

; -------------- Object OBJ_45_SINK --------------
9779: 4E 25                              ; Word_num=0x4E SINK, length=0x0025
977B: A2 02 82                           ; Location=0xA2, disk_section=2, data=0, attributes=0b10000010
977E:    03 1B                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x001B
9780:       04 19                        ;     COM_04_print_command length=0x0019
9782:          6A 4D 8E 7A 82 17 44 5E 23 49 5F BE 5B B1 4B 7B ; 
9792:          55 45 8E 91 15 8A 95 7A 2E ; 
;
;              BEHIND THE BAR THERE IS A SMALL SINK.
;
979B:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           SINK
979D:       50 B8 4B                     ; 

; -------------- Object OBJ_46_WATER --------------
97A0: 4F 4E                              ; Word_num=0x4F WATER, length=0x004E
97A2: 45 10 A0                           ; Location=0x45, disk_section=0, data=1, attributes=0b10100000
97A5:    01 02                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0002
97A7:       72                           ;     COOL
97A8:       74                           ;     CLEAR
97A9:    07 2D                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x002D
97AB:       0E 2B                        ;     COM_0E_while_fail length=0x002B
97AD:          0D 12                     ;       COM_0D_while_pass length=0x0012
97AF:             0A 59                  ;         COM_0A_is_input_phrase(phrase=TASTE u....... * *)
97B1:             04 0E                  ;         COM_04_print_command length=0x000E
97B3:                2F 74 56 F4 66 49 4B 62 8B 9F 6B BF 3F 92 ; 
;
;                    HMM. TASTES OK TO ME.
;
97C1:          0D 15                     ;       COM_0D_while_pass length=0x0015
97C3:             0A 4F                  ;         COM_0A_is_input_phrase(phrase=DRINK u....... * *)
97C5:             04 0D                  ;         COM_04_print_command length=0x000D
97C7:                C7 DE 4F 15 33 61 68 B1 75 B1 E6 72 2E ; 
;
;                    YOU FEEL REFRESHED.
;
97D4:             1C 01                  ;         COM_1C_set_var_object(obj=OBJ_01_PLAYER)
97D6:             23 19                  ;         COM_23_heal_var(points=25)
97D8:    02 16                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0016
;           SMALL AMOUNT OF COOL CLEAR WATER 
97DA:       E3 B8 F3 8C 71 48 9E C5 B8 16 E1 14 B3 9F BF 54 ; 
97EA:       23 49 16 D0 23 62            ; 

; -------------- Object OBJ_47_COUNTER --------------
97F0: 50 0A                              ; Word_num=0x50 COUNTE, length=0x000A
97F2: AA 04 81                           ; Location=0xAA, disk_section=4, data=0, attributes=0b10000001
97F5:    02 05                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0005
;           COUNTER
97F7:       47 55 BF 9A 52               ; 

; -------------- Object OBJ_48_DRESSER --------------
97FC: 51 0A                              ; Word_num=0x51 DRESSE, length=0x000A
97FE: DE 24 8A                           ; Location=0xDE, disk_section=4, data=2, attributes=0b10001010
9801:    02 05                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0005
;           DRESSER
9803:       EF 5B D7 B9 52               ; 

; -------------- Object OBJ_49_TABLE --------------
9808: 1A 09                              ; Word_num=0x1A DESK, length=0x0009
980A: 83 01 81                           ; Location=0x83, disk_section=1, data=0, attributes=0b10000001
980D:    02 04                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0004
;           TABLE 
980F:       44 BD DB 8B                  ; 

; -------------- Object OBJ_4A_HOOD --------------
9813: 52 3E                              ; Word_num=0x52 HOOD, length=0x003E
9815: 86 21 88                           ; Location=0x86, disk_section=1, data=2, attributes=0b10001000
9818:    07 34                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0034
981A:       0D 32                        ;     COM_0D_while_pass length=0x0032
981C:          0E 04                     ;       COM_0E_while_fail length=0x0004
981E:             0A 11                  ;         COM_0A_is_input_phrase(phrase=OPEN u....... * *)
9820:             0A 2D                  ;         COM_0A_is_input_phrase(phrase=PULL * UP u.......)
9822:          04 2A                     ;       COM_04_print_command length=0x002A
9824:             E9 C5 91 96 F0 A4 91 7A 82 17 4A 5E 36 A0 51 18 ; 
9834:             46 C2 55 7B 4F A1 96 AF 56 72 82 17 47 5E BB 98 ; 
9844:             5B 98 4B 7B D5 92 50 B8 6B 6A ; 
;
;                 UPON OPENING THE HOOD YOU DISCOVER THAT THE ENGINE IS
;                 MISSING!
;
984E:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           HOOD
9850:       81 74 44                     ; 

; -------------- Object OBJ_4B_?? --------------
9853: 00 03                              ; Word_num=0x00 -none-, length=0x0003
9855: 00 00 80                           ; Location=0x00, disk_section=0, data=0, attributes=0b10000000

; -------------- Object OBJ_4C_BLASTED_SAFE --------------
9858: 1D 3A                              ; Word_num=0x1D SAFE, length=0x003A
985A: 00 04 82                           ; Location=0x00, disk_section=4, data=0, attributes=0b10000010
985D:    03 2B                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x002B
985F:       04 29                        ;     COM_04_print_command length=0x0029
9861:          5F BE 53 17 5B 66 03 A0 5F BE 61 17 82 C6 5B 17 ; 
9871:          DB 59 C3 9E 5F BE 39 17 DB 9F 55 72 AF 14 83 61 ; 
9881:          7B 4E FF B9 11 58 F0 A4 2E ; 
;
;              THE SAFE ON THE SOUTH SIDE OF THE ROOM HAS BEEN BLASTED
;              OPEN.
;
988A:    02 08                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0008
;           BLASTED SAFE
988C:       7B 4E FF B9 15 58 4F 47      ; 

; -------------- Object OBJ_4D_DOOR --------------
9894: 10 08                              ; Word_num=0x10 DOOR, length=0x0008
9896: 9D 05 88                           ; Location=0x9D, disk_section=5, data=0, attributes=0b10001000
9899:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           DOOR
989B:       81 5B 52                     ; 

; -------------- Object OBJ_4E_BOULDER --------------
989E: 54 5F                              ; Word_num=0x54 BOULDE, length=0x005F
98A0: 9D 05 80                           ; Location=0x9D, disk_section=5, data=0, attributes=0b10000000
98A3:    03 25                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0025
98A5:       04 23                        ;     COM_04_print_command length=0x0023
98A7:          4F 45 65 49 CF 7B B9 14 3E C5 23 62 89 4E A5 54 ; 
98B7:          82 17 47 5E CC 9A 8D 48 4B 5E C9 9A 82 17 55 5E ; 
98C7:          92 73 2E                  ; 
;
;              A MASSIVE BOULDER BLOCKS THE ENTRANCE INTO THE SHIP.
;
98CA:    07 2C                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x002C
98CC:       0D 2A                        ;     COM_0D_while_pass length=0x002A
98CE:          0E 04                     ;       COM_0E_while_fail length=0x0004
98D0:             0A 09                  ;         COM_0A_is_input_phrase(phrase=ATTACK ...P.... WITH .v......)
98D2:             0A 56                  ;         COM_0A_is_input_phrase(phrase=DIG u....... WITH u.......)
98D4:          09 32                     ;       COM_09_compare_to_second_noun(obj=OBJ_32_SHOVEL)
98D6:          04 20                     ;       COM_04_print_command length=0x0020
98D8:             55 45 8E 91 12 8A 25 79 51 5E 96 64 DB 72 07 4F ; 
98E8:             BF 8B 85 AF EF B3 7F 4E CB B5 C9 9A 0F 15 17 BA ; 
;
;                 A SMALL PIECE OF THE BOULDER CRUMBLES INTO DUST.
;
98F8:    02 05                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0005
;           BOULDER
98FA:       07 4F BF 8B 52               ; 

; -------------- Object OBJ_4F_RADIO --------------
98FF: 12 2C                              ; Word_num=0x12 RADIO, length=0x002C
9901: 00 02 80                           ; Location=0x00, disk_section=2, data=0, attributes=0b10000000
9904:    03 01                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0001
9906:       B9                           ;     FN_B9_PRINT_JUKEBOX
9907:    07 1E                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x001E
9909:       0D 1C                        ;     COM_0D_while_pass length=0x001C
990B:          0A 50                     ;       COM_0A_is_input_phrase(phrase=TURN * ON u.......)
990D:          04 15                     ;       COM_04_print_command length=0x0015
990F:             5F BE 2B 17 91 5A AF 14 50 6D D2 B5 5B 8B 91 7A ; 
991F:             77 16 45 B8 2E         ; 
;
;                 THE RADIO BEGINS PLAYING MUSIC.
;
9924:          1E 3C 4F                  ;       COM_1E_swap(obj1=OBJ_3C_RADIO, obj2=OBJ_4F_RADIO)
9927:    02 04                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0004
;           RADIO 
9929:       C6 B0 AB 7A                  ; 

; -------------- Object OBJ_50_DRESSER --------------
992D: 51 0A                              ; Word_num=0x51 DRESSE, length=0x000A
992F: DF 24 8A                           ; Location=0xDF, disk_section=4, data=2, attributes=0b10001010
9932:    02 05                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0005
;           DRESSER
9934:       EF 5B D7 B9 52               ; 

; -------------- Object OBJ_51_CHAIR --------------
9939: 53 0C                              ; Word_num=0x53 CHAIR, length=0x000C
993B: DE 04 80                           ; Location=0xDE, disk_section=4, data=0, attributes=0b10000000
993E:    07 01                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0001
9940:       C5                           ;     FN_C5_??
9941:    02 04                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0004
;           CHAIR 
9943:       1B 54 23 7B                  ; 

; -------------- Object OBJ_52_CHAIR --------------
9947: 53 0C                              ; Word_num=0x53 CHAIR, length=0x000C
9949: DF 04 80                           ; Location=0xDF, disk_section=4, data=0, attributes=0b10000000
994C:    07 01                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0001
994E:       C5                           ;     FN_C5_??
994F:    02 04                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0004
;           CHAIR 
9951:       1B 54 23 7B                  ; 

; -------------- Object OBJ_53_BED --------------
9955: 55 0A                              ; Word_num=0x55 BED, length=0x000A
9957: DE 04 80                           ; Location=0xDE, disk_section=4, data=0, attributes=0b10000000
995A:    07 01                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0001
995C:       C5                           ;     FN_C5_??
995D:    02 02                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0002
;           BED
995F:       66 4D                        ; 

; -------------- Object OBJ_54_BED --------------
9961: 55 0A                              ; Word_num=0x55 BED, length=0x000A
9963: DF 04 80                           ; Location=0xDF, disk_section=4, data=0, attributes=0b10000000
9966:    07 01                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0001
9968:       C5                           ;     FN_C5_??
9969:    02 02                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0002
;           BED
996B:       66 4D                        ; 

; -------------- Object OBJ_55_MOUND_SAND --------------
996D: 57 80 98                           ; Word_num=0x57 SAND, length=0x0098
9970: A0 02 80                           ; Location=0xA0, disk_section=2, data=0, attributes=0b10000000
9973:    03 34                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0034
9975:       04 32                        ;     COM_04_print_command length=0x0032
9977:          5F BE 5B B1 2F 49 99 16 D3 17 44 B8 DB 8B 9E 61 ; 
9987:          D0 B0 B5 53 56 F4 DB 72 F5 59 3E 62 53 17 33 98 ; 
9997:          4B 7B D0 4C A6 85 89 14 D0 47 F3 B9 5F BE F3 17 ; 
99A7:          17 8D                     ; 
;
;              THERE ARE NO VISIBLE ENTRANCES. THE DESERT SAND IS BANKED
;              AGAINST THE WALL.
;
99A9:    07 52                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0052
99AB:       0E 50                        ;     COM_0E_while_fail length=0x0050
99AD:          0D 2A                     ;       COM_0D_while_pass length=0x002A
99AF:             0E 04                  ;         COM_0E_while_fail length=0x0004
99B1:                0A 56               ;           COM_0A_is_input_phrase(phrase=DIG u....... WITH u.......)
99B3:                0A 12               ;           COM_0A_is_input_phrase(phrase=PULL u....... * *)
99B5:             09 32                  ;         COM_09_compare_to_second_noun(obj=OBJ_32_SHOVEL)
99B7:             04 19                  ;         COM_04_print_command length=0x0019
99B9:                70 4D 96 5F 16 71 DB 72 10 B7 1B 58 1B A1 95 5A ; 
99C9:                48 55 23 62 46 45 44 A0 21 ; 
;
;                    BENEATH THE SAND YOU DISCOVER A DOOR!
;
99D2:             17 14 A0               ;         COM_17_move_to(obj=OBJ_14_DOOR_COVERED_SHELTER, destination=RM_1_A0_??)
99D5:             17 55 00               ;         COM_17_move_to(obj=OBJ_55_MOUND_SAND, destination=nowhere)
99D8:             38                     ;         COM_38_bump_score()
99D9:          0D 22                     ;       COM_0D_while_pass length=0x0022
99DB:             0E 04                  ;         COM_0E_while_fail length=0x0004
99DD:                0A 56               ;           COM_0A_is_input_phrase(phrase=DIG u....... WITH u.......)
99DF:                0A 12               ;           COM_0A_is_input_phrase(phrase=PULL u....... * *)
99E1:             09 00                  ;         COM_09_compare_to_second_noun(obj=nothing)
99E3:             04 18                  ;         COM_04_print_command length=0x0018
99E5:                5F BE 53 17 33 98 48 B8 0B C0 6C BE 29 A1 1B 71 ; 
99F5:                34 A1 53 15 B7 98 AF B3 ; 
;
;                    THE SAND SIFTS THROUGH YOUR FINGERS.
;
99FD:    02 09                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0009
;           MOUND OF SAND
99FF:       C7 93 33 98 C3 9E 10 B7 44   ; 

; -------------- Object OBJ_56_SIGN --------------
9A08: 56 5F                              ; Word_num=0x56 SIGN, length=0x005F
9A0A: AA 04 84                           ; Location=0xAA, disk_section=4, data=0, attributes=0b10000100
9A0D:    07 55                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0055
9A0F:       0D 53                        ;     COM_0D_while_pass length=0x0053
9A11:          0A 08                     ;       COM_0A_is_input_phrase(phrase=READ .....?.. * *)
9A13:          04 4F                     ;       COM_04_print_command length=0x004F
9A15:             33 1E D3 B2 CE 98 D0 15 D3 14 9B B7 C3 9E 84 BF ; 
9A25:             C6 97 C3 9C F3 8C 86 74 33 61 27 6F 0D BA 5A 17 ; 
9A35:             2E A1 0F 58 36 60 96 14 82 17 59 5E 66 62 5B 17 ; 
9A45:             DB 59 C3 9E 5F BE 53 17 81 8D 83 96 33 98 9E 61 ; 
9A55:             23 62 5F BE 66 17 B7 A0 5A 17 4E 61 47 62 22 ; 
;
;                 "WARNING, IN CASE OF TORNADO ALL HOTEL GUESTS SHOULD MEET
;                 AT THE WEST SIDE OF THE SALOON AND ENTER THE STORM SHELTER."
;
9A64:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           SIGN
9A66:       49 B8 4E                     ; 

; -------------- Object OBJ_57_MESSAGE --------------
9A69: 56 2A                              ; Word_num=0x56 SIGN, length=0x002A
9A6B: 81 01 84                           ; Location=0x81, disk_section=1, data=0, attributes=0b10000100
9A6E:    07 1E                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x001E
9A70:       0D 1C                        ;     COM_0D_while_pass length=0x001C
9A72:          0A 08                     ;       COM_0A_is_input_phrase(phrase=READ .....?.. * *)
9A74:          04 18                     ;       COM_04_print_command length=0x0018
9A76:             7B 1C F3 B9 1B 54 17 98 10 EE 2E 63 73 15 D5 B5 ; 
9A86:             2E 7C 4F DB 3F 7A 5C BB ; 
;
;                 "LAST CHANCE, NEXT GAS SIXTY MILES."
;
9A8E:    02 05                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0005
;           MESSAGE
9A90:       35 92 09 B7 45               ; 

; -------------- Object OBJ_58_NEON_SIGN --------------
9A95: 56 17                              ; Word_num=0x56 SIGN, length=0x0017
9A97: 96 03 84                           ; Location=0x96, disk_section=3, data=0, attributes=0b10000100
9A9A:    07 0A                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x000A
9A9C:       0D 08                        ;     COM_0D_while_pass length=0x0008
9A9E:          0A 08                     ;       COM_0A_is_input_phrase(phrase=READ .....?.. * *)
9AA0:          04 04                     ;       COM_04_print_command length=0x0004
9AA2:             EB 1A A3 AF            ; 
;
;                 "BAR" 
;
9AA6:    02 06                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0006
;           NEON SIGN
9AA8:       71 98 95 96 80 79            ; 

; -------------- Object OBJ_59_AQUARIUM --------------
9AAE: 58 0B                              ; Word_num=0x58 AQUARI, length=0x000B
9AB0: A6 03 8A                           ; Location=0xA6, disk_section=3, data=0, attributes=0b10001010
9AB3:    02 06                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0006
;           AQUARIUM 
9AB5:       17 49 33 49 5B C5            ; 

; -------------- Object OBJ_5A_ENTRANCE_CLEAR --------------
9ABB: 54 26                              ; Word_num=0x54 BOULDE, length=0x0026
9ABD: 00 05 80                           ; Location=0x00, disk_section=5, data=0, attributes=0b10000000
9AC0:    03 21                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0021
9AC2:       04 1F                        ;     COM_04_print_command length=0x001F
9AC4:          5F BE 30 15 EB BF 17 98 89 17 82 17 55 5E 92 73 ; 
9AD4:          9B 15 C4 B5 30 60 B6 14 80 A1 DE 14 94 5F 2E ; 
;
;              THE ENTRANCE TO THE SHIP HAS BEEN BLOWN CLEAR.
;

; -------------- Object OBJ_5B_LIMIT_SIGN --------------
9AE3: 56 18                              ; Word_num=0x56 SIGN, length=0x0018
9AE5: 89 01 84                           ; Location=0x89, disk_section=1, data=0, attributes=0b10000100
9AE8:    07 0E                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x000E
9AEA:       0D 0C                        ;     COM_0D_while_pass length=0x000C
9AEC:          0A 08                     ;       COM_0A_is_input_phrase(phrase=READ .....?.. * *)
9AEE:          04 08                     ;       COM_04_print_command length=0x0008
9AF0:             1B 1B FB C0 8F 8C 74 7B ; 
;
;                 "CITY LIMIT"
;
9AF8:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           SIGN
9AFA:       49 B8 4E                     ; 

; -------------- Object OBJ_5C_PAIR_HANDS --------------
9AFD: 1F 2C                              ; Word_num=0x1F HAND, length=0x002C
9AFF: 01 00 C0                           ; Location=0x01, disk_section=0, data=0, attributes=0b11000000
9B02:    02 09                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0009
;           PAIR OF HANDS
9B04:       4B A4 91 AF 8A 64 8E 48 53   ; 
9B0D:    07 1C                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x001C
9B0F:       0D 1A                        ;     COM_0D_while_pass length=0x001A
9B11:          0A 06                     ;       COM_0A_is_input_phrase(phrase=DROP ..C..... * *)
9B13:          04 16                     ;       COM_04_print_command length=0x0016
9B15:             C7 DE 49 16 B4 D0 51 18 23 C6 50 72 0B 5C 83 7A ; 
9B25:             95 5A 35 6F 9B C1      ; 
;
;                 YOU LOWER YOUR HANDS IN DISGUST. 
;

; -------------- Object OBJ_5D_BARRED_WINDOW_OUTSIDE --------------
9B2B: 59 47                              ; Word_num=0x59 WINDOW, length=0x0047
9B2D: 8F 02 80                           ; Location=0x8F, disk_section=2, data=0, attributes=0b10000000
9B30:    07 37                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0037
9B32:       0D 35                        ;     COM_0D_while_pass length=0x0035
9B34:          0E 04                     ;       COM_0E_while_fail length=0x0004
9B36:             0A 10                  ;         COM_0A_is_input_phrase(phrase=LOOK * IN ......O.)
9B38:             0A 0B                  ;         COM_0A_is_input_phrase(phrase=LOOK * AT u.......)
9B3A:          04 2D                     ;       COM_04_print_command length=0x002D
9B3C:             81 8D 50 86 CB 6A 96 96 DB 72 50 D1 89 5B 1B EE ; 
9B4C:             1B A1 10 53 AB 14 6E B1 55 DB 1B 60 46 45 5D 62 ; 
9B5C:             90 14 03 58 87 15 85 96 B3 46 76 98 2E ; 
;
;                 LOOKING IN THE WINDOW, YOU CAN BARELY SEE A DESK AND A GUN
;                 CABINET.
;
9B69:    02 09                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0009
;           BARRED WINDOW
9B6B:       D4 4C 66 B1 FB 17 49 98 57   ; 

; -------------- Object OBJ_5E_BARRED_WINDOW_INSIDE --------------
9B74: 59 3A                              ; Word_num=0x59 WINDOW, length=0x003A
9B76: 8E 02 80                           ; Location=0x8E, disk_section=2, data=0, attributes=0b10000000
9B79:    07 2A                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x002A
9B7B:       0D 28                        ;     COM_0D_while_pass length=0x0028
9B7D:          0E 04                     ;       COM_0E_while_fail length=0x0004
9B7F:             0A 10                  ;         COM_0A_is_input_phrase(phrase=LOOK * IN ......O.)
9B81:             0A 0B                  ;         COM_0A_is_input_phrase(phrase=LOOK * AT u.......)
9B83:          04 20                     ;       COM_04_print_command length=0x0020
9B85:             C7 DE 57 17 47 5E EE 93 46 DB 57 62 B3 B3 0C BA ; 
9B95:             7D 62 90 73 D6 6A D6 9C DB 72 84 74 79 7C 1B 9C ; 
;
;                 YOU SEE EMPTY DESERT STRETCHING TO THE HORIZON. 
;
9BA5:    02 09                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0009
;           BARRED WINDOW
9BA7:       D4 4C 66 B1 FB 17 49 98 57   ; 

; -------------- Object OBJ_5F_SHELTER --------------
9BB0: 5A 0D                              ; Word_num=0x5A SHELTE, length=0x000D
9BB2: A0 02 80                           ; Location=0xA0, disk_section=2, data=0, attributes=0b10000000
9BB5:    07 01                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0001
9BB7:       BB                           ;     FN_BB_PRINT_LOOK_IN_AT
9BB8:    02 05                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0005
;           SHELTER
9BBA:       1F B8 3F 8E 52               ; 

; -------------- Object OBJ_60_SHELTER --------------
9BBF: 5A 0D                              ; Word_num=0x5A SHELTE, length=0x000D
9BC1: DB 02 80                           ; Location=0xDB, disk_section=2, data=0, attributes=0b10000000
9BC4:    07 01                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0001
9BC6:       BB                           ;     FN_BB_PRINT_LOOK_IN_AT
9BC7:    02 05                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0005
;           SHELTER
9BC9:       1F B8 3F 8E 52               ; 

; -------------- Object OBJ_61_GROUND --------------
9BCE: 2B 09                              ; Word_num=0x2B FLOOR, length=0x0009
9BD0: 01 00 80                           ; Location=0x01, disk_section=0, data=0, attributes=0b10000000
9BD3:    02 04                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0004
;           GROUND
9BD5:       B9 6E 8E C5                  ; 

; -------------- Object OBJ_62_SHAGGY_CREATURE --------------
9BD9: 5B 85 24                           ; Word_num=0x5B ALIEN, length=0x0524
9BDC: C3 05 90                           ; Location=0xC3, disk_section=5, data=0, attributes=0b10010000
9BDF:    03 01                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0001
9BE1:       BD                           ;     FN_BD_PRINT_SHAGGY_CREATURE
9BE2:    09 02                           ;   Section=09:SECTION_09_HIT_POINTS, length=0x0002
9BE4:       14 14                        ;     Hit_points=20_of_20
9BE6:    0A 33                           ;   Section=0A:SECTION_0A_UPON_DEATH, length=0x0033
9BE8:       0D 31                        ;     COM_0D_while_pass length=0x0031
9BEA:          1F 28                     ;       COM_1F_print2 length=0x0028
9BEC:             5F BE 8E 14 30 79 03 15 4B 62 8E 48 2B 17 86 A5 ; 
9BFC:             FB 8E E5 59 55 4A 89 17 0F 15 F3 B9 68 4D AF A0 ; 
9C0C:             51 18 23 C6 47 63 5B BB ; 
;
;                 THE ALIEN DIES AND RAPIDLY DECAYS TO DUST BEFORE YOUR EYES. 
;
9C14:          17 62 C3                  ;       COM_17_move_to(obj=OBJ_62_SHAGGY_CREATURE, destination=RM_1_C3_??)
9C17:          1C 62                     ;       COM_1C_set_var_object(obj=OBJ_62_SHAGGY_CREATURE)
9C19:          23 4B                     ;       COM_23_heal_var(points=75)
9C1B:    07 82 DE                        ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x02DE
9C1E:       0D 82 DB                     ;     COM_0D_while_pass length=0x02DB
9C21:          0A 09                     ;       COM_0A_is_input_phrase(phrase=ATTACK ...P.... WITH .v......)
9C23:          0E 82 D6                  ;       COM_0E_while_fail length=0x02D6
9C26:             0D 81 65               ;         COM_0D_while_pass length=0x0165
9C29:                09 5C               ;           COM_09_compare_to_second_noun(obj=OBJ_5C_PAIR_HANDS)
9C2B:                0B 81 60 05         ;           COM_0B_switch length=0x0160, function=COM_05_is_less_equal_last_random(value)
9C2F:                   26               ;             COM_05_is_less_equal_last_random(value=38)
9C30:                   44               ;             ELSE goto=0x9C75
9C31:                      0D 42         ;               COM_0D_while_pass length=0x0042
9C33:                         04 3C      ;                 COM_04_print_command length=0x003C
9C35:                            5F BE 8E 14 30 79 66 17 79 47 3D 62 AB 14 8B 54 ; 
9C45:                            4B 49 C7 DE 88 AF 66 7B D2 B5 30 A1 0B 58 C9 9A ; 
9C55:                            D6 15 C8 B5 D7 46 09 EE 67 B1 8B 96 29 54 85 AF ; 
9C65:                            4F A1 8B B3 C7 DE 8A AF 8E 48 6B B5 ; 
;
;                                THE ALIEN STAGGERS BACK AS YOUR FISTS POUND INTO ITS FACE,
;                                GREEN ICHOR COVERS YOUR HANDS!
;
9C71:                         1C 62      ;                 COM_1C_set_var_object(obj=OBJ_62_SHAGGY_CREATURE)
9C73:                         1D 09      ;                 COM_1D_attack_var(points=9)
9C75:                   5A               ;             COM_05_is_less_equal_last_random(value=90)
9C76:                   3E               ;             ELSE goto=0x9CB5
9C77:                      0D 3C         ;               COM_0D_while_pass length=0x003C
9C79:                         04 36      ;                 COM_04_print_command length=0x0036
9C7B:                            5F BE 8E 14 30 79 D5 15 57 17 B3 9A 67 B1 90 8C ; 
9C8B:                            C4 6A 43 DB F7 17 F3 8C FB A5 A6 53 1B 16 AF 54 ; 
9C9B:                            51 18 48 C2 2E 60 B9 14 75 98 E4 14 8D C5 19 71 ; 
9CAB:                            82 7B 83 7A 71 7B ; 
;
;                                THE ALIEN IS SENT REELING BY A WELL PLACED KICK. YOU FEEL
;                                BONES CRUNCH WITHIN IT!
;
9CB1:                         1C 62      ;                 COM_1C_set_var_object(obj=OBJ_62_SHAGGY_CREATURE)
9CB3:                         1D 06      ;                 COM_1D_attack_var(points=6)
9CB5:                   8D               ;             COM_05_is_less_equal_last_random(value=141)
9CB6:                   54               ;             ELSE goto=0x9D0B
9CB7:                      0D 52         ;               COM_0D_while_pass length=0x0052
9CB9:                         04 4C      ;                 COM_04_print_command length=0x004C
9CBB:                            5F BE 5A 17 79 47 44 DB 09 B3 88 96 23 C6 58 6D ; 
9CCB:                            4B 62 C7 DE 7B 14 14 67 49 90 12 B2 95 14 51 18 ; 
9CDB:                            4A C2 55 9F 16 BC DB 72 43 48 83 61 4F A1 9B AF ; 
9CEB:                            34 A1 9F 15 F3 46 8E 48 5F 17 5A 49 A3 15 43 90 ; 
9CFB:                            0B 6C A6 9A 82 17 49 5E 07 B3 31 98 ; 
;
;                                THE SHAGGY BROWN FUR GIVES YOU A FIRM GRIP AS YOU HOIST THE
;                                ALIEN OVER YOUR HEAD AND SMASH HIM AGAINST THE GROUND!
;
9D07:                         1C 62      ;                 COM_1C_set_var_object(obj=OBJ_62_SHAGGY_CREATURE)
9D09:                         1D 04      ;                 COM_1D_attack_var(points=4)
9D0B:                   B3               ;             COM_05_is_less_equal_last_random(value=179)
9D0C:                   2B               ;             ELSE goto=0x9D38
9D0D:                      04 29         ;               COM_04_print_command length=0x0029
9D0F:                         C7 DE 95 AF 50 D1 CF 6A 65 7B 4B 62 5F BE 8E 14 ; 
9D1F:                         30 79 90 14 1B 58 1B A1 47 48 E6 A0 49 16 9B B7 ; 
9D2F:                         C7 DE 84 AF 3B 48 17 98 2E ; 
;
;                             YOUR SWING MISSES THE ALIEN AND YOU ALMOST LOSE YOUR
;                             BALANCE.
;
9D38:                   D9               ;             COM_05_is_less_equal_last_random(value=217)
9D39:                   2B               ;             ELSE goto=0x9D65
9D3A:                      04 29         ;               COM_04_print_command length=0x0029
9D3C:                         5F BE 8E 14 30 79 B6 14 5D 9E DB B5 34 A1 B6 14 ; 
9D4C:                         85 A1 FB 17 53 BE 95 73 94 14 4B 94 8E 48 3F 17 ; 
9D5C:                         1F B8 C8 B5 C1 A0 2E 49 2E ; 
;
;                             THE ALIEN BLOCKS YOUR BLOWS WITH HIS ARMS AND RUSHES
;                             FORWARD.
;
9D65:                   FF               ;             COM_05_is_less_equal_last_random(value=255)
9D66:                   27               ;             ELSE goto=0x9D8E
9D67:                      04 25         ;               COM_04_print_command length=0x0025
9D69:                         5F BE 8E 14 30 79 0F 15 A5 54 B0 17 F4 59 7B 14 ; 
9D79:                         4E D1 0D 58 DD 78 5B F4 1B A1 65 B1 4F A1 93 AF ; 
9D89:                         C5 C4 D3 86 2E ; 
;
;                             THE ALIEN DUCKS UNDER A WILD KICK. YOU RECOVER QUICKLY.
;
9D8E:             0D 81 6B               ;         COM_0D_while_pass length=0x016B
9D91:                0E 06               ;           COM_0E_while_fail length=0x0006
9D93:                   09 32            ;             COM_09_compare_to_second_noun(obj=OBJ_32_SHOVEL)
9D95:                   09 28            ;             COM_09_compare_to_second_noun(obj=OBJ_28_SHOTGUN)
9D97:                   09 24            ;             COM_09_compare_to_second_noun(obj=OBJ_24_CROWBAR)
9D99:                0B 81 60 05         ;           COM_0B_switch length=0x0160, function=COM_05_is_less_equal_last_random(value)
9D9D:                   19               ;             COM_05_is_less_equal_last_random(value=25)
9D9E:                   3F               ;             ELSE goto=0x9DDE
9D9F:                      0D 3D         ;               COM_0D_while_pass length=0x003D
9DA1:                         04 03      ;                 COM_04_print_command length=0x0003
9DA3:                            C7 DE 52 ; 
;
;                                YOUR
;
9DA6:                         12         ;                 COM_12_print_second_noun()
9DA7:                         04 31      ;                 COM_04_print_command length=0x0031
9DA9:                            E3 B8 1F B8 C6 B5 80 A1 B2 17 03 A0 5F BE 9F 15 ; 
9DB9:                            F3 46 C3 9E 5F BE 8E 14 30 79 09 EE 67 B1 8B 96 ; 
9DC9:                            29 54 95 AF EB A6 4B DF C7 DE 85 AF 86 8D F5 72 ; 
9DD9:                            21      ; 
;
;                                SMASHES DOWN UPON THE HEAD OF THE ALIEN, GREEN ICHOR SPRAYS
;                                YOUR CLOTHES!
;
9DDA:                         1C 62      ;                 COM_1C_set_var_object(obj=OBJ_62_SHAGGY_CREATURE)
9DDC:                         1D 15      ;                 COM_1D_attack_var(points=21)
9DDE:                   3F               ;             COM_05_is_less_equal_last_random(value=63)
9DDF:                   53               ;             ELSE goto=0x9E33
9DE0:                      0D 51         ;               COM_0D_while_pass length=0x0051
9DE2:                         04 03      ;                 COM_04_print_command length=0x0003
9DE4:                            C7 DE 52 ; 
;
;                                YOUR
;
9DE7:                         12         ;                 COM_12_print_second_noun()
9DE8:                         04 45      ;                 COM_04_print_command length=0x0045
9DEA:                            0C BA 17 7A D6 B5 DB 72 43 48 83 61 83 7A 8D 7B ; 
9DFA:                            5B 17 FE 59 51 18 48 C2 2E 60 B9 14 75 98 E4 14 ; 
9E0A:                            8D C5 19 71 82 7B 83 7A 97 7B 82 17 43 5E 87 8C ; 
9E1A:                            95 96 04 9A 0B C0 4F 45 66 7B B8 16 84 15 30 60 ; 
9E2A:                            B6 14 36 A0 2E ; 
;
;                                STRIKES THE ALIEN IN ITS SIDE, YOU FEEL BONES CRUNCH WITHIN
;                                IT. THE ALIEN SNORTS A MIST OF GREEN BLOOD.
;
9E2F:                         1C 62      ;                 COM_1C_set_var_object(obj=OBJ_62_SHAGGY_CREATURE)
9E31:                         1D 0B      ;                 COM_1D_attack_var(points=11)
9E33:                   72               ;             COM_05_is_less_equal_last_random(value=114)
9E34:                   48               ;             ELSE goto=0x9E7D
9E35:                      0D 46         ;               COM_0D_while_pass length=0x0046
9E37:                         04 03      ;                 COM_04_print_command length=0x0003
9E39:                            C7 DE 52 ; 
;
;                                YOUR
;
9E3C:                         12         ;                 COM_12_print_second_noun()
9E3D:                         04 3A      ;                 COM_04_print_command length=0x003A
9E3F:                            96 73 D6 B5 DB 72 43 48 85 61 C3 B5 9B B2 F4 4F ; 
9E4F:                            03 BA AB 98 5F BE 56 15 5A 62 C2 16 A7 61 84 15 ; 
9E5F:                            30 60 C5 15 84 74 56 15 85 A1 5C 15 2E 60 48 DB ; 
9E6F:                            FF B2 82 17 59 5E 30 A1 AB 57 ; 
;
;                                HITS THE ALIEN'S ARM BURSTING THE FLESH OPEN. GREEN ICHOR
;                                FLOWS FREELY FROM THE WOUND!
;
9E79:                         1C 62      ;                 COM_1C_set_var_object(obj=OBJ_62_SHAGGY_CREATURE)
9E7B:                         1D 06      ;                 COM_1D_attack_var(points=6)
9E7D:                   A5               ;             COM_05_is_less_equal_last_random(value=165)
9E7E:                   25               ;             ELSE goto=0x9EA4
9E7F:                      0D 23         ;               COM_0D_while_pass length=0x0023
9E81:                         04 03      ;                 COM_04_print_command length=0x0003
9E83:                            C7 DE 52 ; 
;
;                                YOUR
;
9E86:                         12         ;                 COM_12_print_second_noun()
9E87:                         04 1B      ;                 COM_04_print_command length=0x001B
9E89:                            BB 6D 17 98 CA B5 37 49 F5 8B D3 B8 B8 16 96 64 ; 
9E99:                            DB 72 43 48 85 61 C4 B5 93 9E 2E ; 
;
;                                GLANCES HARMLESSLY OFF THE ALIEN'S BODY.
;
9EA4:                   CB               ;             COM_05_is_less_equal_last_random(value=203)
9EA5:                   26               ;             ELSE goto=0x9ECC
9EA6:                      0D 24         ;               COM_0D_while_pass length=0x0024
9EA8:                         04 03      ;                 COM_04_print_command length=0x0003
9EAA:                            C7 DE 52 ; 
;
;                                YOUR
;
9EAD:                         12         ;                 COM_12_print_second_noun()
9EAE:                         04 1C      ;                 COM_04_print_command length=0x001C
9EB0:                            D5 92 B5 B7 82 17 43 5E 87 8C 83 96 CB B5 16 BC ; 
9EC0:                            55 D1 0B C0 6B BF 0F A0 5B 17 FF 59 ; 
;
;                                MISSES THE ALIEN AS IT TWISTS TO ONE SIDE.
;
9ECC:                   FF               ;             COM_05_is_less_equal_last_random(value=255)
9ECD:                   2E               ;             ELSE goto=0x9EFC
9ECE:                      0D 2C         ;               COM_0D_while_pass length=0x002C
9ED0:                         04 23      ;                 COM_04_print_command length=0x0023
9ED2:                            5F BE 8E 14 30 79 30 15 50 BD BF 6D DB B5 34 A1 ; 
9EE2:                            94 14 6E 94 EC 16 CF 62 C3 9A AB 98 5F BE B5 17 ; 
9EF2:                            51 5E 46 ; 
;
;                                THE ALIEN ENTANGLES YOUR ARMS, PREVENTING THE USE OF
;
9EF5:                         A9         ;                 FN_A9_PRINT_noun2
9EF6:                         04 04      ;                 COM_04_print_command length=0x0004
9EF8:                            03 A0 97 7B ; 
;
;                                ON IT.
;
9EFC:    08 81 F1                        ;   Section=08:SECTION_08_EVERY_TURN, length=0x01F1
9EFF:       0E 81 EE                     ;     COM_0E_while_fail length=0x01EE
9F02:          0D 47                     ;       COM_0D_while_pass length=0x0047
9F04:             14                     ;         COM_14_execute_and_reverse_status next command
9F05:             01 01                  ;         COM_01_is_in_pack_or_room(obj=OBJ_01_PLAYER)
9F07:             14                     ;         COM_14_execute_and_reverse_status next command
9F08:             03 C3 62               ;         COM_03_is_located(owner=RM_1_C3_??, obj=OBJ_62_SHAGGY_CREATURE)
9F0B:             14                     ;         COM_14_execute_and_reverse_status next command
9F0C:             0E 06                  ;         COM_0E_while_fail length=0x0006
9F0E:                03 DB 01            ;           COM_03_is_located(owner=RM_1_DB_??, obj=OBJ_01_PLAYER)
9F11:                03 E8 01            ;           COM_03_is_located(owner=RM_1_E8_??, obj=OBJ_01_PLAYER)
9F14:             0B 19 0A               ;         COM_0B_switch length=0x0019, function=COM_0A_is_input_phrase(phrase_num)
9F17:                04                  ;           COM_0A_is_input_phrase("WEST * * *")
9F18:                04                  ;           ELSE goto=0x9F1D
9F19:                   21 04 00 00      ;             COM_21_execute_phrase(phrase=WEST * * *, obj1=nothing, obj2=nothing)
9F1D:                03                  ;           COM_0A_is_input_phrase("EAST * * *")
9F1E:                04                  ;           ELSE goto=0x9F23
9F1F:                   21 03 00 00      ;             COM_21_execute_phrase(phrase=EAST * * *, obj1=nothing, obj2=nothing)
9F23:                01                  ;           COM_0A_is_input_phrase("NORTH * * *")
9F24:                04                  ;           ELSE goto=0x9F29
9F25:                   21 01 00 00      ;             COM_21_execute_phrase(phrase=NORTH * * *, obj1=nothing, obj2=nothing)
9F29:                02                  ;           COM_0A_is_input_phrase("SOUTH * * *")
9F2A:                04                  ;           ELSE goto=0x9F2F
9F2B:                   21 02 00 00      ;             COM_21_execute_phrase(phrase=SOUTH * * *, obj1=nothing, obj2=nothing)
9F2F:             01 01                  ;         COM_01_is_in_pack_or_room(obj=OBJ_01_PLAYER)
9F31:             1F 18                  ;         COM_1F_print2 length=0x0018
9F33:                3F B9 82 62 91 7A 57 17 75 61 89 17 AF 14 59 15 ; 
9F43:                09 8D 50 D1 DB 6A 3F A1 ; 
;
;                    SOMETHING SEEMS TO BE FOLLOWING YOU.
;
9F4B:          0D 1E                     ;       COM_0D_while_pass length=0x001E
9F4D:             14                     ;         COM_14_execute_and_reverse_status next command
9F4E:             01 01                  ;         COM_01_is_in_pack_or_room(obj=OBJ_01_PLAYER)
9F50:             05 26                  ;         COM_05_is_less_equal_last_random(value=38)
9F52:             0E 08                  ;         COM_0E_while_fail length=0x0008
9F54:                0A 01               ;           COM_0A_is_input_phrase(phrase=NORTH * * *)
9F56:                0A 02               ;           COM_0A_is_input_phrase(phrase=SOUTH * * *)
9F58:                0A 03               ;           COM_0A_is_input_phrase(phrase=EAST * * *)
9F5A:                0A 04               ;           COM_0A_is_input_phrase(phrase=WEST * * *)
9F5C:             14                     ;         COM_14_execute_and_reverse_status next command
9F5D:             0E 06                  ;         COM_0E_while_fail length=0x0006
9F5F:                03 DB 01            ;           COM_03_is_located(owner=RM_1_DB_??, obj=OBJ_01_PLAYER)
9F62:                03 E8 01            ;           COM_03_is_located(owner=RM_1_E8_??, obj=OBJ_01_PLAYER)
9F65:             2C 01                  ;         COM_2C_set_active(obj=OBJ_01_PLAYER)
9F67:             1C 62                  ;         COM_1C_set_var_object(obj=OBJ_62_SHAGGY_CREATURE)
9F69:             10                     ;         COM_10_drop_var()
9F6A:             BD                     ;         FN_BD_PRINT_SHAGGY_CREATURE
9F6B:          14                        ;       COM_14_execute_and_reverse_status next command
9F6C:          01 01                     ;       COM_01_is_in_pack_or_room(obj=OBJ_01_PLAYER)
9F6E:          0B 81 7F 05               ;       COM_0B_switch length=0x017F, function=COM_05_is_less_equal_last_random(value)
9F72:             19                     ;         COM_05_is_less_equal_last_random(value=25)
9F73:             46                     ;         ELSE goto=0x9FBA
9F74:                0D 44               ;           COM_0D_while_pass length=0x0044
9F76:                   1F 3B            ;             COM_1F_print2 length=0x003B
9F78:                      59 45 CF 49 B8 16 B6 14 8E 7A 91 7A DB 16 83 7A ; 
9F88:                      89 67 8D 9E 82 17 07 B3 13 6D C7 DE 84 AF 93 9E ; 
9F98:                      95 14 2B 17 04 E5 5A 17 3A 49 7F 17 82 62 E3 16 ; 
9FA8:                      2D 62 5B 5E 34 A1 56 15 5A 62 21 ; 
;
;                          A WAVE OF BLINDING PAIN FLOODS THROUGH YOUR BODY AS RAZOR
;                          SHARP TEETH PIERCE YOUR FLESH!
;
9FB3:                   1C 01            ;             COM_1C_set_var_object(obj=OBJ_01_PLAYER)
9FB5:                   1D 09            ;             COM_1D_attack_var(points=9)
9FB7:                   17 91 01         ;             COM_17_move_to(obj=OBJ_91_POISON, destination=OBJ_01_PLAYER)
9FBA:             34                     ;         COM_05_is_less_equal_last_random(value=52)
9FBB:             34                     ;         ELSE goto=0x9FF0
9FBC:                0D 32               ;           COM_0D_while_pass length=0x0032
9FBE:                   1F 29            ;             COM_1F_print2 length=0x0029
9FC0:                      C7 DE 4F 15 33 61 55 45 94 5F 91 7A DB 16 83 7A ; 
9FD0:                      4B 49 5F BE 8E 14 30 79 CB 23 BB 54 CB D2 70 B1 ; 
9FE0:                      1B 58 34 A1 56 15 5A 62 21 ; 
;
;                          YOU FEEL A SEARING PAIN AS THE ALIEN'S CLAWS REND YOUR
;                          FLESH!
;
9FE9:                   1C 01            ;             COM_1C_set_var_object(obj=OBJ_01_PLAYER)
9FEB:                   1D 06            ;             COM_1D_attack_var(points=6)
9FED:                   17 91 01         ;             COM_17_move_to(obj=OBJ_91_POISON, destination=OBJ_01_PLAYER)
9FF0:             5A                     ;         COM_05_is_less_equal_last_random(value=90)
9FF1:             4C                     ;         ELSE goto=0xA03E
9FF2:                0D 4A               ;           COM_0D_while_pass length=0x004A
9FF4:                   1F 44            ;             COM_1F_print2 length=0x0044
9FF6:                      5F BE 8E 14 30 79 84 15 EA 48 F5 8B 51 18 EB C1 ; 
A006:                      4B 49 8D 7B 5E 17 7B 7A 94 14 4B 94 03 C0 89 17 ; 
A016:                      E4 14 5A C6 82 17 4E 5E 4F 79 C7 16 11 BC 9B 64 ; 
A026:                      3E A1 51 18 23 C6 04 B2 C4 B5 7B 60 96 96 C4 9C ; 
A036:                      8E 61 FF F9   ; 
;
;                          THE ALIEN GRAPPLES YOU! AS ITS SLIMY ARMS TRY TO CRUSH THE
;                          LIFE OUT OF YOU, YOUR RIBS BEGIN TO BEND...
;
A03A:                   1C 01            ;             COM_1C_set_var_object(obj=OBJ_01_PLAYER)
A03C:                   1D 03            ;             COM_1D_attack_var(points=3)
A03E:             8D                     ;         COM_05_is_less_equal_last_random(value=141)
A03F:             43                     ;         ELSE goto=0xA083
A040:                1F 41               ;           COM_1F_print2 length=0x0041
A042:                   5F BE 8E 14 30 79 CB 23 BB B8 74 CA 91 7A 7F 17 ; 
A052:                   82 62 EF 16 13 B8 04 68 14 D0 16 58 73 A1 4D B1 ; 
A062:                   51 18 B3 C7 F6 4F 51 18 56 C2 55 D1 16 BC D6 9C ; 
A072:                   DB 72 46 B8 43 5E 33 98 45 86 CB 83 04 BC DD 46 ; 
A082:                   2E               ; 
;
;                       THE ALIEN'S SLAVERING TEETH PUSH FORWARD TOWARDS YOU, BUT
;                       YOU TWIST TO THE SIDE AND KICK IT BACK.
;
A083:             C0                     ;         COM_05_is_less_equal_last_random(value=192)
A084:             3C                     ;         ELSE goto=0xA0C1
A085:                1F 3A               ;           COM_1F_print2 length=0x003A
A087:                   5F BE 8E 14 30 79 CB 23 BB 54 CB D2 12 B2 82 17 ; 
A097:                   07 B3 13 6D C7 DE 85 AF 86 8D F5 72 44 F4 73 C6 ; 
A0A7:                   7B 50 EF 81 90 A5 C4 6A DD 46 14 D0 0B 5C C7 DE ; 
A0B7:                   98 14 46 9F D0 15 F4 81 DB E0 ; 
;
;                       THE ALIEN'S CLAWS RIP THROUGH YOUR CLOTHES. BUT BY JUMPING
;                       BACKWARDS YOU AVOID INJURY.
;
A0C1:             FF                     ;         COM_05_is_less_equal_last_random(value=255)
A0C2:             2D                     ;         ELSE goto=0xA0F0
A0C3:                1F 2B               ;           COM_1F_print2 length=0x002B
A0C5:                   5F BE 8E 14 30 79 3F 17 1F B8 D2 B5 66 49 51 18 ; 
A0D5:                   4B C2 8B 96 0B C0 6F 68 B3 9B F3 5F 8E 49 72 61 ; 
A0E5:                   16 BC C3 9C 3B C0 8B 54 C7 DE 2E ; 
;
;                       THE ALIEN RUSHES PAST YOU IN ITS FRENZIED ATTEMPT TO ATTACK
;                       YOU.
;
A0F0:    02 0E                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x000E
;           SHORT SHAGGY CREATURE
A0F2:       29 B8 B3 B3 1B B8 0B 6D E4 14 96 5F 2F C6 ; 

; -------------- Object OBJ_63_GREY_CUBE --------------
A100: 5C 42                              ; Word_num=0x5C CUBE, length=0x0042
A102: 65 00 A0                           ; Location=0x65, disk_section=0, data=0, attributes=0b10100000
A105:    03 27                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0027
A107:       04 25                        ;     COM_04_print_command length=0x0025
A109:          5F BE 5B B1 4B 7B 46 45 35 49 84 15 3B 63 C1 C0 ; 
A119:          D0 15 13 54 97 B9 2F 49 67 16 4E BD CB 78 24 56 ; 
A129:          4A 5E 2F 62 2E            ; 
;
;              THERE IS A DARK GREY TWO INCH SQUARE METALIC CUBE HERE.
;
A12E:    01 03                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0003
A130:       6C                           ;     GREY
A131:       0F                           ;     SMALL
A132:       6D                           ;     INCH
A133:    0C 01                           ;   Section=0C:SECTION_0C_WEIGHT, length=0x0001
A135:       04                           ;     Weight=4
A136:    02 0C                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x000C
;           TWO INCH GREY CUBE
A138:       C1 C0 D0 15 13 54 AF 6E 45 DB AF C3 ; 

; -------------- Object OBJ_64_WHITE_CUBE --------------
A144: 5C 3B                              ; Word_num=0x5C CUBE, length=0x003B
A146: 00 00 A0                           ; Location=0x00, disk_section=0, data=0, attributes=0b10100000
A149:    03 1F                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x001F
A14B:       04 1D                        ;     COM_04_print_command length=0x001D
A14D:          5F BE 5B B1 4B 7B 59 45 96 73 56 5E 2B D2 8D 7A ; 
A15D:          15 71 A3 AD 5B B1 24 56 4A 5E 2F 62 2E ; 
;
;              THERE IS A WHITE TWO INCH SQUARE CUBE HERE.
;
A16A:    01 03                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0003
A16C:       60                           ;     WHITE
A16D:       0F                           ;     SMALL
A16E:       6D                           ;     INCH
A16F:    0C 01                           ;   Section=0C:SECTION_0C_WEIGHT, length=0x0001
A171:       06                           ;     Weight=6
A172:    02 0D                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x000D
;           TWO INCH WHITE CUBE
A174:       C1 C0 D0 15 13 54 23 D1 DB BD 24 56 45 ; 

; -------------- Object OBJ_65_TABLE --------------
A181: 1A 09                              ; Word_num=0x1A DESK, length=0x0009
A183: 86 08 81                           ; Location=0x86, disk_section=8, data=0, attributes=0b10000001
A186:    02 04                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0004
;           TABLE 
A188:       44 BD DB 8B                  ; 

; -------------- Object OBJ_66_RECESS --------------
A18C: 2E 09                              ; Word_num=0x2E HOLE, length=0x0009
A18E: 86 08 82                           ; Location=0x86, disk_section=8, data=0, attributes=0b10000010
A191:    02 04                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0004
;           RECESS
A193:       65 B1 65 62                  ; 

; -------------- Object OBJ_67_HOLE --------------
A197: 2E 08                              ; Word_num=0x2E HOLE, length=0x0008
A199: 80 07 82                           ; Location=0x80, disk_section=7, data=0, attributes=0b10000010
A19C:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           HOLE
A19E:       7E 74 45                     ; 

; -------------- Object OBJ_68_HOLE_BOULDERS --------------
A1A1: 2E 62                              ; Word_num=0x2E HOLE, length=0x0062
A1A3: 9E 08 82                           ; Location=0x9E, disk_section=8, data=0, attributes=0b10000010
A1A6:    06 58                           ;   Section=06:SECTION_06_IF_SECOND_NOUN, length=0x0058
A1A8:       0D 56                        ;     COM_0D_while_pass length=0x0056
A1AA:          0A 0F                     ;       COM_0A_is_input_phrase(phrase=DROP ..C..... IN ......O.)
A1AC:          08 64                     ;       COM_08_is_first_noun(obj=OBJ_64_WHITE_CUBE)
A1AE:          04 4C                     ;       COM_04_print_command length=0x004C
A1B0:             5F BE E7 14 5B 4D 69 4D 9D 7A 89 17 7E 15 6B A1 ; 
A1C0:             73 4F 2E 6D 1F 8F 84 14 4F A1 51 18 23 C6 E3 72 ; 
A1D0:             03 58 87 96 53 B7 DB A4 56 72 13 54 5F A0 8B 9A ; 
A1E0:             8E 48 90 14 98 14 3B 48 1A 98 51 5E 84 64 2E A1 ; 
A1F0:             F4 59 C5 B5 F5 B3 F5 72 51 18 EB C1 ; 
;
;                 THE CUBE BEGINS TO GLOW BRIGHTLY. ABOVE YOUR HEAD AN ESCAPE
;                 HATCH OPENS AND AN AVALANCHE OF BOULDERS CRUSHES YOU!
;
A1FC:          1C 01                     ;       COM_1C_set_var_object(obj=OBJ_01_PLAYER)
A1FE:          1D 6E                     ;       COM_1D_attack_var(points=110)
A200:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           HOLE
A202:       7E 74 45                     ; 

; -------------- Object OBJ_69_PICTURE --------------
A205: 5D 0A                              ; Word_num=0x5D PICTUR, length=0x000A
A207: 82 07 80                           ; Location=0x82, disk_section=7, data=0, attributes=0b10000000
A20A:    02 05                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0005
;           PICTURE
A20C:       85 A5 74 C0 45               ; 

; -------------- Object OBJ_6A_GLASS_CYLINDER --------------
A211: 5E 80 82                           ; Word_num=0x5E CYLIND, length=0x0082
A214: 85 87 8A                           ; Location=0x85, disk_section=7, data=8, attributes=0b10001010
A217:    07 71                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0071
A219:       0B 6F 0A                     ;     COM_0B_switch length=0x006F, function=COM_0A_is_input_phrase(phrase_num)
A21C:          11                        ;       COM_0A_is_input_phrase("OPEN u....... * *")
A21D:          01                        ;       ELSE goto=0xA21F
A21E:             C2                     ;         FN_C2_PRINT_CANT_BUDGE_noun1
A21F:          40                        ;       COM_0A_is_input_phrase("CLOSE ....A... * *")
A220:          01                        ;       ELSE goto=0xA222
A221:             C2                     ;         FN_C2_PRINT_CANT_BUDGE_noun1
A222:          36                        ;       COM_0A_is_input_phrase("ENTER * * *")
A223:          35                        ;       ELSE goto=0xA259
A224:             0E 33                  ;         COM_0E_while_fail length=0x0033
A226:                0D 21               ;           COM_0D_while_pass length=0x0021
A228:                   1B               ;             COM_1B_set_var_to_second_noun()
A229:                   14               ;             COM_14_execute_and_reverse_status next command
A22A:                   2E 20            ;             UNKNOWN2E, Value: 0x20
A22C:                   17 01 6A         ;             COM_17_move_to(obj=OBJ_01_PLAYER, destination=OBJ_6A_GLASS_CYLINDER)
A22F:                   04 18            ;             COM_04_print_command length=0x0018
A231:                      C7 DE 5E 17 7E A1 45 DB 8F 8C 8B 4B C9 9A 82 17 ; 
A241:                      45 5E 43 DE 3F 98 1B B5 ; 
;
;                          YOU SLOWLY CLIMB INTO THE CYLINDER. 
;
A249:                0D 0E               ;           COM_0D_while_pass length=0x000E
A24B:                   1B               ;             COM_1B_set_var_to_second_noun()
A24C:                   2E 20            ;             UNKNOWN2E, Value: 0x20
A24E:                   04 09            ;             COM_04_print_command length=0x0009
A250:                      73 7B 4B 7B C9 54 A6 B7 2E ; 
;
;                          IT IS CLOSED.
;
A259:          37                        ;       COM_0A_is_input_phrase("CLIMB * OUT *")
A25A:          2F                        ;       ELSE goto=0xA28A
A25B:             0E 2D                  ;         COM_0E_while_fail length=0x002D
A25D:                0D 1B               ;           COM_0D_while_pass length=0x001B
A25F:                   1B               ;             COM_1B_set_var_to_second_noun()
A260:                   14               ;             COM_14_execute_and_reverse_status next command
A261:                   2E 20            ;             UNKNOWN2E, Value: 0x20
A263:                   1C 01            ;             COM_1C_set_var_object(obj=OBJ_01_PLAYER)
A265:                   10               ;             COM_10_drop_var()
A266:                   04 12            ;             COM_04_print_command length=0x0012
A268:                      C7 DE 99 16 D5 CE 50 BD 11 58 96 96 DB 72 89 67 ; 
A278:                      C7 A0         ; 
;
;                          YOU NOW STAND ON THE FLOOR.
;
A27A:                0D 0E               ;           COM_0D_while_pass length=0x000E
A27C:                   1B               ;             COM_1B_set_var_to_second_noun()
A27D:                   2E 20            ;             UNKNOWN2E, Value: 0x20
A27F:                   04 09            ;             COM_04_print_command length=0x0009
A281:                      73 7B 4B 7B C9 54 A6 B7 2E ; 
;
;                          IT IS CLOSED.
;
A28A:    02 0A                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x000A
;           GLASS CYLINDER 
A28C:       BB 6D CB B9 CE 56 8E 7A 23 62 ; 

; -------------- Object OBJ_6B_WHITE_BUTTON_LIGHTS --------------
A296: 4A 53                              ; Word_num=0x4A BUTTON, length=0x0053
A298: 6A 00 80                           ; Location=0x6A, disk_section=0, data=0, attributes=0b10000000
A29B:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
A29D:       60                           ;     WHITE
A29E:    07 41                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0041
A2A0:       0D 3F                        ;     COM_0D_while_pass length=0x003F
A2A2:          0A 12                     ;       COM_0A_is_input_phrase(phrase=PULL u....... * *)
A2A4:          0E 3B                     ;       COM_0E_while_fail length=0x003B
A2A6:             0D 1E                  ;         COM_0D_while_pass length=0x001E
A2A8:                03 85 6D            ;           COM_03_is_located(owner=RM_1_SOUTHWEST_OF_STATION, obj=OBJ_6D_LIGHTS)
A2AB:                17 6D 00            ;           COM_17_move_to(obj=OBJ_6D_LIGHTS, destination=nowhere)
A2AE:                04 16               ;           COM_04_print_command length=0x0016
A2B0:                   C3 54 AF 54 82 17 4E 5E 7A 79 0B C0 58 72 49 5E ; 
A2C0:                   0F A0 C7 16 9B C1 ; 
;
;                       CLICK. THE LIGHTS HAVE GONE OUT. 
;
A2C6:             0D 19                  ;         COM_0D_while_pass length=0x0019
A2C8:                03 00 6D            ;           COM_03_is_located(owner=nowhere, obj=OBJ_6D_LIGHTS)
A2CB:                17 6D 85            ;           COM_17_move_to(obj=OBJ_6D_LIGHTS, destination=RM_1_SOUTHWEST_OF_STATION)
A2CE:                04 11               ;           COM_04_print_command length=0x0011
A2D0:                   C3 54 AF 54 82 17 4E 5E 7A 79 14 BC 8F 62 DD B2 ; 
A2E0:                   2E               ; 
;
;                       CLICK. THE LIGHT RETURNS.
;
A2E1:    02 08                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0008
;           WHITE BUTTON
A2E3:       23 D1 DB BD F6 4F 80 BF      ; 

; -------------- Object OBJ_6C_MAROON_BUTTON --------------
A2EB: 4A 80 F2                           ; Word_num=0x4A BUTTON, length=0x00F2
A2EE: 6A 00 80                           ; Location=0x6A, disk_section=0, data=0, attributes=0b10000000
A2F1:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
A2F3:       61                           ;     MAROON
A2F4:    07 80 DE                        ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x00DE
A2F7:       0D 80 DB                     ;     COM_0D_while_pass length=0x00DB
A2FA:          0A 12                     ;       COM_0A_is_input_phrase(phrase=PULL u....... * *)
A2FC:          0E 80 D6                  ;       COM_0E_while_fail length=0x00D6
A2FF:             0D 80 95               ;         COM_0D_while_pass length=0x0095
A302:                03 85 01            ;           COM_03_is_located(owner=RM_1_SOUTHWEST_OF_STATION, obj=OBJ_01_PLAYER)
A305:                04 80 8B            ;           COM_04_print_command length=0x008B
A308:                   C3 54 AF 54 5A 17 40 D2 6B 83 C7 DE 99 16 85 BE ; 
A318:                   56 5E 56 72 82 17 45 5E E3 8B 8E AF F3 78 C3 9E ; 
A328:                   5F BE EB 14 90 8C F4 59 9B 15 C5 B5 85 8D 17 60 ; 
A338:                   FA 17 3F 7A 09 15 91 7A 61 17 0B EE 15 BC CF 62 ; 
A348:                   66 B1 51 18 23 C6 37 49 59 F4 8E 73 55 5E 54 BD ; 
A358:                   10 B2 C3 6A 16 BC DB 72 95 5A 2F 92 74 4D F3 5F ; 
A368:                   37 49 D0 15 82 17 45 5E 43 DE 3F 98 F3 B4 C7 DE ; 
A378:                   DB 16 CB B9 36 A1 90 14 07 58 70 CA 63 C0 13 8D ; 
A388:                   B6 14 26 60 89 17 FF 14 82 49 2E ; 
;
;                       CLICK. SHWONK! YOU NOTICE THAT THE CLEAR LID OF THE
;                       CYLINDER HAS CLOSED. WHILE DOING SO, IT SEVERED YOUR ARM.
;                       WHILE STARRING AT THE DISMEMBERED ARM IN THE CYLINDER, YOU
;                       PASS OUT AND EVENTUALLY BLEED TO DEATH.
;
A393:                1C 01               ;           COM_1C_set_var_object(obj=OBJ_01_PLAYER)
A395:                1D 64               ;           COM_1D_attack_var(points=100)
A397:             0D 1E                  ;         COM_0D_while_pass length=0x001E
A399:                1C 6A               ;           COM_1C_set_var_object(obj=OBJ_6A_GLASS_CYLINDER)
A39B:                2E 20               ;           UNKNOWN2E, Value: 0x20
A39D:                29                  ;           COM_29_print_open_var()
A39E:                04 17               ;           COM_04_print_command length=0x0017
A3A0:                   C3 54 AF 54 5A 17 52 D1 AB A2 5F BE EB 14 90 8C ; 
A3B0:                   F4 59 C2 16 9D 61 2E ; 
;
;                       CLICK. SHWIPP! THE CYLINDER OPENS.
;
A3B7:             0D 1C                  ;         COM_0D_while_pass length=0x001C
A3B9:                04 17               ;           COM_04_print_command length=0x0017
A3BB:                   C3 54 AF 54 5A 17 4D D1 D6 06 DB 72 CE 56 8E 7A ; 
A3CB:                   23 62 C9 54 B5 B7 2E ; 
;
;                       CLICK. SHWIK! THE CYLINDER CLOSES.
;
A3D2:                1C 6A               ;           COM_1C_set_var_object(obj=OBJ_6A_GLASS_CYLINDER)
A3D4:                29                  ;           COM_29_print_open_var()
A3D5:    02 09                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0009
;           MAROON BUTTON
A3D7:       94 91 40 A0 BF 14 49 C0 4E   ; 

; -------------- Object OBJ_6D_LIGHTS --------------
A3E0: 5F 09                              ; Word_num=0x5F LIGHTS, length=0x0009
A3E2: 85 07 80                           ; Location=0x85, disk_section=7, data=0, attributes=0b10000000
A3E5:    02 04                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0004
;           LIGHTS
A3E7:       89 8C 4D 75                  ; 

; -------------- Object OBJ_6E_CONSOLE --------------
A3EB: 62 0A                              ; Word_num=0x62 CONSOL, length=0x000A
A3ED: 9C 08 81                           ; Location=0x9C, disk_section=8, data=0, attributes=0b10000001
A3F0:    02 05                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0005
;           CONSOLE
A3F2:       40 55 3E B9 45               ; 

; -------------- Object OBJ_6F_CHAIR --------------
A3F7: 53 0C                              ; Word_num=0x53 CHAIR, length=0x000C
A3F9: 9C 08 80                           ; Location=0x9C, disk_section=8, data=0, attributes=0b10000000
A3FC:    07 01                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0001
A3FE:       C5                           ;     FN_C5_??
A3FF:    02 04                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0004
;           CHAIR 
A401:       1B 54 23 7B                  ; 

; -------------- Object OBJ_70_WHITE_BUTTON_SCREEN --------------
A405: 4A 5D                              ; Word_num=0x4A BUTTON, length=0x005D
A407: 6E 00 80                           ; Location=0x6E, disk_section=0, data=0, attributes=0b10000000
A40A:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
A40C:       60                           ;     WHITE
A40D:    07 4B                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x004B
A40F:       0D 49                        ;     COM_0D_while_pass length=0x0049
A411:          0A 12                     ;       COM_0A_is_input_phrase(phrase=PULL u....... * *)
A413:          0E 45                     ;       COM_0E_while_fail length=0x0045
A415:             0D 1D                  ;         COM_0D_while_pass length=0x001D
A417:                03 72 73            ;           COM_03_is_located(owner=OBJ_72_VIEWING_SCREEN, obj=OBJ_73_DISPLAY_EARTH)
A41A:                04 0F               ;           COM_04_print_command length=0x000F
A41C:                   5F BE 55 17 67 B1 89 96 B5 9E B6 14 95 48 2E ; 
;
;                       THE SCREEN GOES BLANK.
;
A42B:                17 73 00            ;           COM_17_move_to(obj=OBJ_73_DISPLAY_EARTH, destination=nowhere)
A42E:                17 74 00            ;           COM_17_move_to(obj=OBJ_74_DISPLAY_MOON, destination=nowhere)
A431:                17 75 00            ;           COM_17_move_to(obj=OBJ_75_DISPLAY_MOTHER_SHIP, destination=nowhere)
A434:             0D 24                  ;         COM_0D_while_pass length=0x0024
A436:                04 16               ;           COM_04_print_command length=0x0016
A438:                   5F BE D3 17 FB 62 AB 98 64 B7 30 60 D5 15 85 14 ; 
A448:                   98 BE 7F 49 9B 5D ; 
;
;                       THE VIEWING SCREEN IS ACTIVATED. 
;
A44E:                17 73 72            ;           COM_17_move_to(obj=OBJ_73_DISPLAY_EARTH, destination=OBJ_72_VIEWING_SCREEN)
A451:                17 74 72            ;           COM_17_move_to(obj=OBJ_74_DISPLAY_MOON, destination=OBJ_72_VIEWING_SCREEN)
A454:                17 75 72            ;           COM_17_move_to(obj=OBJ_75_DISPLAY_MOTHER_SHIP, destination=OBJ_72_VIEWING_SCREEN)
A457:                1C 72               ;           COM_1C_set_var_object(obj=OBJ_72_VIEWING_SCREEN)
A459:                33                  ;           UNKNOWN33
A45A:    02 08                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0008
;           WHITE BUTTON
A45C:       23 D1 DB BD F6 4F 80 BF      ; 

; -------------- Object OBJ_71_GREEN_BUTTON_WEAPON --------------
A464: 4A 80 80                           ; Word_num=0x4A BUTTON, length=0x0080
A467: 6E 00 80                           ; Location=0x6E, disk_section=0, data=0, attributes=0b10000000
A46A:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
A46C:       6A                           ;     GREEN
A46D:    07 6E                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x006E
A46F:       0D 6C                        ;     COM_0D_while_pass length=0x006C
A471:          0A 12                     ;       COM_0A_is_input_phrase(phrase=PULL u....... * *)
A473:          0E 68                     ;       COM_0E_while_fail length=0x0068
A475:             0D 10                  ;         COM_0D_while_pass length=0x0010
A477:                03 73 00            ;           COM_03_is_located(owner=OBJ_73_DISPLAY_EARTH, obj=nothing)
A47A:                04 0B               ;           COM_04_print_command length=0x000B
A47C:                   06 9A 90 73 CA 6A EA 48 9D 61 2E ; 
;
;                       NOTHING HAPPENS.
;
A487:             0D 52                  ;         COM_0D_while_pass length=0x0052
A489:                04 14               ;           COM_04_print_command length=0x0014
A48B:                   A2 1D 74 8E D4 6A 53 79 CC 51 BE A0 00 B3 D4 9C ; 
A49B:                   91 C5 DC 63      ; 
;
;                       "SPLURG RIFIC JORTRONO RUNGE."
;
A49F:                03 01 80            ;           COM_03_is_located(owner=OBJ_01_PLAYER, obj=OBJ_80_WISDOM)
A4A2:                04 37               ;           COM_04_print_command length=0x0037
A4A4:                   3F B9 A9 60 DB CE 1B A1 8E C5 3D 62 50 BD 16 58 ; 
A4B4:                   95 73 89 17 67 16 A6 48 81 13 92 5F 03 A0 E6 46 ; 
A4C4:                   CB 7B E6 BD 8B 18 7B A6 B3 9A 6B BF F5 59 2F 7B ; 
A4D4:                   16 58 31 49 97 62 22 ; 
;
;                       SOMEHOW YOU UNDERSTAND THIS TO MEAN, "WEAPON ACTIVATED -
;                       POINT TO DESIRED TARGET."
;
A4DB:             14                     ;         COM_14_execute_and_reverse_status next command
A4DC:             0C                     ;         COM_0C_fail()
A4DD:    02 08                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0008
;           GREEN BUTTON
A4DF:       AF 6E 83 61 F6 4F 80 BF      ; 

; -------------- Object OBJ_72_VIEWING_SCREEN --------------
A4E7: 63 0F                              ; Word_num=0x63 SCREEN, length=0x000F
A4E9: 9C 08 81                           ; Location=0x9C, disk_section=8, data=0, attributes=0b10000001
A4EC:    02 0A                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x000A
;           VIEWING SCREEN 
A4EE:       07 CB 50 D1 D5 6A AF 55 83 61 ; 

; -------------- Object OBJ_73_DISPLAY_EARTH --------------
A4F8: 64 57                              ; Word_num=0x64 EARTH, length=0x0057
A4FA: 00 00 80                           ; Location=0x00, disk_section=0, data=0, attributes=0b10000000
A4FD:    07 42                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0042
A4FF:       0D 40                        ;     COM_0D_while_pass length=0x0040
A501:          0A 58                     ;       COM_0A_is_input_phrase(phrase=POINT u....... * *)
A503:          04 38                     ;       COM_04_print_command length=0x0038
A505:             59 45 92 5F 03 A0 83 7A 5F BE 5A 17 D3 7A 4B 7B ; 
A515:             14 67 F3 5F 8E 48 82 17 52 5E 50 8B 73 62 94 5F ; 
A525:             53 BE 4B 7B F5 59 F9 BF 26 DD 10 EE F3 A0 6B BF ; 
A535:             30 92 91 BE 9B 96 3F A1 ; 
;
;                 A WEAPON IN THE SHIP IS FIRED AND THE PLANET EARTH IS
;                 DESTROYED, NOT TO MENTION YOU.
;
A53D:          1C 01                     ;       COM_1C_set_var_object(obj=OBJ_01_PLAYER)
A53F:          1D 6E                     ;       COM_1D_attack_var(points=110)
A541:    02 0E                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x000E
;           DISPLAY OF THE EARTH 
A543:       95 5A FB A5 51 DB 96 64 DB 72 94 5F 53 BE ; 

; -------------- Object OBJ_74_DISPLAY_MOON --------------
A551: 65 80 92                           ; Word_num=0x65 MOON, length=0x0092
A554: 00 00 80                           ; Location=0x00, disk_section=0, data=0, attributes=0b10000000
A557:    07 7E                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x007E
A559:       0D 7C                        ;     COM_0D_while_pass length=0x007C
A55B:          0A 58                     ;       COM_0A_is_input_phrase(phrase=POINT u....... * *)
A55D:          04 74                     ;       COM_04_print_command length=0x0074
A55F:             5F BE 5A 17 D5 7A D9 B5 92 5F 03 A0 14 67 4B 62 ; 
A56F:             8E 48 51 18 50 C2 03 A1 9B 53 03 A0 5F BE 55 17 ; 
A57F:             67 B1 96 96 56 72 82 17 4F 5E 40 A0 D5 15 FF 14 ; 
A58F:             0C BA C7 A1 9B 5D 83 48 9D 7A 50 BD 0E BC 7F 49 ; 
A59F:             F3 B4 54 8B 9B 6C 6B 68 E7 6D CD 9A B8 16 71 16 ; 
A5AF:             03 A0 3E 55 86 8C 59 5E 82 7B 82 17 47 5E 3E 49 ; 
A5BF:             73 76 F5 59 F9 BF D0 DD CB 6A 03 BC 33 98 C7 DE ; 
A5CF:             16 EE 4F A0            ; 
;
;                 THE SHIP'S WEAPON FIRES AND YOU NOTICE ON THE SCREEN THAT
;                 THE MOON IS DESTROYED. AN INSTANT LATER, LARGE FRAGMENTS OF
;                 MOON COLLIDE WITH THE EARTH, DESTROYING IT AND YOU, TOO.
;
A5D3:          1C 01                     ;       COM_1C_set_var_object(obj=OBJ_01_PLAYER)
A5D5:          1D 6E                     ;       COM_1D_attack_var(points=110)
A5D7:    02 0D                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x000D
;           DISPLAY OF THE MOON
A5D9:       95 5A FB A5 51 DB 96 64 DB 72 C1 93 4E ; 

; -------------- Object OBJ_75_DISPLAY_MOTHER_SHIP --------------
A5E6: 66 80 91                           ; Word_num=0x66 SHIP, length=0x0091
A5E9: 00 00 80                           ; Location=0x00, disk_section=0, data=0, attributes=0b10000000
A5EC:    07 78                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0078
A5EE:       0D 76                        ;     COM_0D_while_pass length=0x0076
A5F0:          0A 58                     ;       COM_0A_is_input_phrase(phrase=POINT u....... * *)
A5F2:          04 62                     ;       COM_04_print_command length=0x0062
A5F4:             83 48 8F 61 CB B1 AF 14 5B 48 EA 48 94 5F D1 B5 ; 
A604:             96 96 DB 72 64 B7 30 60 90 14 1B 58 1B A1 16 D0 ; 
A614:             13 54 4B 49 73 7B F5 59 F9 BF 4B DF 5F BE 71 16 ; 
A624:             5F BE 95 AF 92 73 D6 06 DB 72 F6 4F 80 BF D4 B5 ; 
A634:             D7 5F DB 59 9E 7A D6 9C DB 72 40 55 3E B9 43 5E ; 
A644:             33 98 5F BE 55 17 67 B1 86 96 85 5F 98 BE 7F 49 ; 
A654:             5B BB                  ; 
;
;                 AN ENERGY BEAM APPEARS ON THE SCREEN AND YOU WATCH AS IT
;                 DESTROYS THE MOTHER SHIP! THE BUTTONS RECEDE INTO THE
;                 CONSOLE AND THE SCREEN DEACTIVATES.
;
A656:          17 73 00                  ;       COM_17_move_to(obj=OBJ_73_DISPLAY_EARTH, destination=nowhere)
A659:          17 74 00                  ;       COM_17_move_to(obj=OBJ_74_DISPLAY_MOON, destination=nowhere)
A65C:          17 75 00                  ;       COM_17_move_to(obj=OBJ_75_DISPLAY_MOTHER_SHIP, destination=nowhere)
A65F:          17 70 00                  ;       COM_17_move_to(obj=OBJ_70_WHITE_BUTTON_SCREEN, destination=nowhere)
A662:          17 71 00                  ;       COM_17_move_to(obj=OBJ_71_GREEN_BUTTON_WEAPON, destination=nowhere)
A665:          38                        ;       COM_38_bump_score()
A666:    02 12                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0012
;           DISPLAY OF THE MOTHER SHIP 
A668:       95 5A FB A5 51 DB 96 64 DB 72 C6 93 F4 72 5A 17 ; 
A678:       D3 7A                        ; 

; -------------- Object OBJ_76_CHAIR --------------
A67A: 53 0C                              ; Word_num=0x53 CHAIR, length=0x000C
A67C: 8A 08 82                           ; Location=0x8A, disk_section=8, data=0, attributes=0b10000010
A67F:    07 01                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0001
A681:       C5                           ;     FN_C5_??
A682:    02 04                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0004
;           CHAIR 
A684:       1B 54 23 7B                  ; 

; -------------- Object OBJ_77_HANDGRIP --------------
A688: 67 77                              ; Word_num=0x67 HANDGR, length=0x0077
A68A: 8A 08 A0                           ; Location=0x8A, disk_section=8, data=0, attributes=0b10100000
A68D:    07 6A                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x006A
A68F:       0E 68                        ;     COM_0E_while_fail length=0x0068
A691:          0D 4E                     ;       COM_0D_while_pass length=0x004E
A693:             0E 08                  ;         COM_0E_while_fail length=0x0008
A695:                0A 05               ;           COM_0A_is_input_phrase(phrase=GET ..C..... * *)
A697:                0A 43               ;           COM_0A_is_input_phrase(phrase=GET ..C..... WITH ..C.....)
A699:                0A 2D               ;           COM_0A_is_input_phrase(phrase=PULL * UP u.......)
A69B:                0A 12               ;           COM_0A_is_input_phrase(phrase=PULL u....... * *)
A69D:             14                     ;         COM_14_execute_and_reverse_status next command
A69E:             A2                     ;         FN_A2_PRINT_ALREADY_HAVE_THE_var
A69F:             04 02                  ;         COM_04_print_command length=0x0002
A6A1:                11 9F               ; 
;
;                    OH!
;
A6A3:             34                     ;         UNKNOWN34
A6A4:             1A                     ;         COM_1A_set_var_to_first_noun()
A6A5:             8F                     ;         FN_8F_TRY_TO_GET_OBJECT
A6A6:             25                     ;         COM_25_print_linefeed()
A6A7:             04 33                  ;         COM_04_print_command length=0x0033
A6A9:                26 BA F0 59 1E 8F 51 18 23 C6 34 BA 07 B3 43 98 ; 
A6B9:                C5 98 AF 14 50 6D 89 17 03 15 E1 B9 8F 8E 90 14 ; 
A6C9:                10 58 EB 62 0F A0 D6 B5 17 48 82 17 D4 60 E6 16 ; 
A6D9:                D7 46 21            ; 
;
;                    SUDDENLY, YOUR SURROUNDINGS BEGIN TO DISSOLVE AND NEW ONES
;                    TAKE THEIR PLACE!
;
A6DC:             25                     ;         COM_25_print_linefeed()
A6DD:             30 81                  ;         COM_30_set_current_room(room=RM_9_SURFACE)
A6DF:             2F 09                  ;         COM_2F_load_section_from_disk(section=9)
A6E1:          0D 16                     ;       COM_0D_while_pass length=0x0016
A6E3:             0E 0C                  ;         COM_0E_while_fail length=0x000C
A6E5:                0A 06               ;           COM_0A_is_input_phrase(phrase=DROP ..C..... * *)
A6E7:                0A 0D               ;           COM_0A_is_input_phrase(phrase=THROW .vC..... AT ...P....)
A6E9:                0A 0F               ;           COM_0A_is_input_phrase(phrase=DROP ..C..... IN ......O.)
A6EB:                0A 4B               ;           COM_0A_is_input_phrase(phrase=DROP ..C..... ON .......L)
A6ED:                0A 0E               ;           COM_0A_is_input_phrase(phrase=THROW u....... TO ...P....)
A6EF:                0A 39               ;           COM_0A_is_input_phrase(phrase=THROW ..C..... IN u.......)
A6F1:             03 01 77               ;         COM_03_is_located(owner=OBJ_01_PLAYER, obj=OBJ_77_HANDGRIP)
A6F4:             35                     ;         UNKNOWN35
A6F5:             30 8A                  ;         COM_30_set_current_room(room=RM_8_??8A??)
A6F7:             2F 08                  ;         COM_2F_load_section_from_disk(section=8)
A6F9:    02 06                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0006
;           HANDGRIP 
A6FB:       50 72 44 5A D3 7A            ; 

; -------------- Object OBJ_78_CHAIR --------------
A701: 53 0C                              ; Word_num=0x53 CHAIR, length=0x000C
A703: 8D 07 80                           ; Location=0x8D, disk_section=7, data=0, attributes=0b10000000
A706:    07 01                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0001
A708:       C5                           ;     FN_C5_??
A709:    02 04                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0004
;           CHAIR 
A70B:       1B 54 23 7B                  ; 

; -------------- Object OBJ_79_LARGE_CUBE --------------
A70F: 5C 0F                              ; Word_num=0x5C CUBE, length=0x000F
A711: 8D 07 81                           ; Location=0x8D, disk_section=7, data=0, attributes=0b10000001
A714:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
A716:       0E                           ;     BIG
A717:    02 07                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0007
;           LARGE CUBE
A719:       54 8B 9B 6C 24 56 45         ; 

; -------------- Object OBJ_7A_HOLE_WISER --------------
A720: 2E 80 B2                           ; Word_num=0x2E HOLE, length=0x00B2
A723: 8D 07 82                           ; Location=0x8D, disk_section=7, data=0, attributes=0b10000010
A726:    06 80 A1                        ;   Section=06:SECTION_06_IF_SECOND_NOUN, length=0x00A1
A729:       0E 80 9E                     ;     COM_0E_while_fail length=0x009E
A72C:          0D 60                     ;       COM_0D_while_pass length=0x0060
A72E:             14                     ;         COM_14_execute_and_reverse_status next command
A72F:             03 01 80               ;         COM_03_is_located(owner=OBJ_01_PLAYER, obj=OBJ_80_WISDOM)
A732:             0A 0F                  ;         COM_0A_is_input_phrase(phrase=DROP ..C..... IN ......O.)
A734:             08 64                  ;         COM_08_is_first_noun(obj=OBJ_64_WHITE_CUBE)
A736:             17 64 00               ;         COM_17_move_to(obj=OBJ_64_WHITE_CUBE, destination=nowhere)
A739:             04 4C                  ;         COM_04_print_command length=0x004C
A73B:                44 45 0E B2 83 8C B3 9A 7B 67 13 B8 C3 9E 89 8C ; 
A74B:                33 75 63 98 93 B2 B6 14 8E 7A DB B5 1B A1 8E 48 ; 
A75B:                51 18 48 C2 2E 60 61 17 39 92 56 72 FB 17 B4 B7 ; 
A76B:                82 17 83 48 68 4D AF A0 D6 06 DB 72 96 8C FF BE ; 
A77B:                E7 14 5B 4D 74 C0 8B 9A AF 6E DB E0 ; 
;
;                    A BRILLIANT FLASH OF LIGHT NEARLY BLINDS YOU AND YOU FEEL
;                    SOMEWHAT WISER THAN BEFORE! THE LITTLE CUBE TURNS GREY.
;
A787:             17 80 01               ;         COM_17_move_to(obj=OBJ_80_WISDOM, destination=OBJ_01_PLAYER)
A78A:             17 63 7A               ;         COM_17_move_to(obj=OBJ_63_GREY_CUBE, destination=OBJ_7A_HOLE_WISER)
A78D:             38                     ;         COM_38_bump_score()
A78E:          0D 3A                     ;       COM_0D_while_pass length=0x003A
A790:             0A 0F                  ;         COM_0A_is_input_phrase(phrase=DROP ..C..... IN ......O.)
A792:             08 64                  ;         COM_08_is_first_noun(obj=OBJ_64_WHITE_CUBE)
A794:             04 30                  ;         COM_04_print_command length=0x0030
A796:                C7 DE 3A 15 F4 A4 30 79 9B 53 99 48 5F BE 84 AF ; 
A7A6:                0E B2 83 8C B3 9A 7B 67 13 B8 C3 9E 89 8C 33 75 ; 
A7B6:                4B 49 C7 DE 84 AF CB B0 87 96 A6 D8 7F 9E 6B B5 ; 
;
;                    YOU EXPERIENCE ANOTHER BRILLIANT FLASH OF LIGHT AS YOUR
;                    BRAIN EXPLODES!
;
A7C6:             1C 01                  ;         COM_1C_set_var_object(obj=OBJ_01_PLAYER)
A7C8:             1D 64                  ;         COM_1D_attack_var(points=100)
A7CA:    02 09                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0009
;           TWO INCH HOLE
A7CC:       C1 C0 D0 15 13 54 7E 74 45   ; 

; -------------- Object OBJ_7B_TABLE --------------
A7D5: 1A 09                              ; Word_num=0x1A DESK, length=0x0009
A7D7: 8E 08 81                           ; Location=0x8E, disk_section=8, data=0, attributes=0b10000001
A7DA:    02 04                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0004
;           TABLE 
A7DC:       44 BD DB 8B                  ; 

; -------------- Object OBJ_7C_TRANSPARENT_VIAL --------------
A7E0: 68 31                              ; Word_num=0x68 VIAL, length=0x0031
A7E2: 7B A0 AA                           ; Location=0x7B, disk_section=0, data=10, attributes=0b10101010
A7E5:    03 1C                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x001C
A7E7:       04 1A                        ;     COM_04_print_command length=0x001A
A7E9:          5F BE 5B B1 4B 7B 55 45 8E 91 16 8A D0 B0 5B B9 ; 
A7F9:          70 B1 18 BC 8E 78 9F 15 7F B1 ; 
;
;              THERE IS A SMALL TRANSPARENT VIAL HERE.
;
A803:    0C 01                           ;   Section=0C:SECTION_0C_WEIGHT, length=0x0001
A805:       06                           ;     Weight=6
A806:    02 0B                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x000B
;           TRANSPARENT VIAL
A808:       EB BF A2 9A 2F 49 B3 9A 03 CB 4C ; 

; -------------- Object OBJ_7D_TSOM_SOLUTION --------------
A813: 4C 6C                              ; Word_num=0x4C WHISKE, length=0x006C
A815: 7C 10 A0                           ; Location=0x7C, disk_section=0, data=1, attributes=0b10100000
A818:    07 59                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0059
A81A:       0E 57                        ;     COM_0E_while_fail length=0x0057
A81C:          0D 30                     ;       COM_0D_while_pass length=0x0030
A81E:             0A 59                  ;         COM_0A_is_input_phrase(phrase=TASTE u....... * *)
A820:             0E 2C                  ;         COM_0E_while_fail length=0x002C
A822:                14                  ;           COM_14_execute_and_reverse_status next command
A823:                BF                  ;           FN_BF_??
A824:                0D 28               ;           COM_0D_while_pass length=0x0028
A826:                   04 22            ;             COM_04_print_command length=0x0022
A828:                      33 D1 16 EE DB 72 34 92 56 5E 66 49 51 5E 96 64 ; 
A838:                      95 73 66 17 50 C4 D0 15 09 CB AB A0 F5 BD 51 18 ; 
A848:                      EB C1         ; 
;
;                          WHY, THE MERE TASTE OF THIS STUFF INVIGORATES YOU! 
;
A84A:                   1C 01            ;             COM_1C_set_var_object(obj=OBJ_01_PLAYER)
A84C:                   23 05            ;             COM_23_heal_var(points=5)
A84E:          0D 23                     ;       COM_0D_while_pass length=0x0023
A850:             0A 4F                  ;         COM_0A_is_input_phrase(phrase=DRINK u....... * *)
A852:             0E 1F                  ;         COM_0E_while_fail length=0x001F
A854:                14                  ;           COM_14_execute_and_reverse_status next command
A855:                BF                  ;           FN_BF_??
A856:                0D 1B               ;           COM_0D_while_pass length=0x001B
A858:                   1C 01            ;             COM_1C_set_var_object(obj=OBJ_01_PLAYER)
A85A:                   23 64            ;             COM_23_heal_var(points=100)
A85C:                   04 12            ;             COM_04_print_command length=0x0012
A85E:                      49 D2 D6 06 56 72 F3 17 D4 B5 8E 5F FB 8E 41 6E ; 
A86E:                      AB 57         ; 
;
;                          WOW! THAT WAS REALLY GOOD! 
;
A870:                   17 91 00         ;             COM_17_move_to(obj=OBJ_91_POISON, destination=nowhere)
A873:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
A875:       6B                           ;     TSOM
A876:    02 09                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0009
;           TSOM SOLUTION
A878:       21 C0 55 90 CF 9F 91 BE 4E   ; 

; -------------- Object OBJ_7E_PEDESTAL --------------
A881: 69 0B                              ; Word_num=0x69 PEDEST, length=0x000B
A883: 90 08 81                           ; Location=0x90, disk_section=8, data=0, attributes=0b10000001
A886:    02 06                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0006
;           PEDESTAL 
A888:       E6 A4 66 62 33 48            ; 

; -------------- Object OBJ_7F_TWO_INCH_HOLE --------------
A88E: 2E 5A                              ; Word_num=0x2E HOLE, length=0x005A
A890: 90 08 82                           ; Location=0x90, disk_section=8, data=0, attributes=0b10000010
A893:    06 4A                           ;   Section=06:SECTION_06_IF_SECOND_NOUN, length=0x004A
A895:       0D 48                        ;     COM_0D_while_pass length=0x0048
A897:          0A 0F                     ;       COM_0A_is_input_phrase(phrase=DROP ..C..... IN ......O.)
A899:          08 63                     ;       COM_08_is_first_noun(obj=OBJ_63_GREY_CUBE)
A89B:          17 63 00                  ;       COM_17_move_to(obj=OBJ_63_GREY_CUBE, destination=nowhere)
A89E:          04 3C                     ;       COM_04_print_command length=0x003C
A8A0:             1A B9 A4 EA D5 86 91 A6 82 17 4E 5E 8E 7B DB 8B ; 
A8B0:             24 56 44 5E 7B 60 8B 9A 6B BF C9 6D C4 CE 09 B2 ; 
A8C0:             46 75 B3 E0 5F BE 95 96 8E 62 F5 8B D0 15 6B BF ; 
A8D0:             55 45 46 72 51 5E 99 64 96 73 DB 63 ; 
;
;                 SNP-KRKL-PP! THE LITTLE CUBE BEGINS TO GLOW BRIGHTLY, THEN
;                 SETTLES INTO A SHADE OF WHITE.
;
A8DC:          17 64 7F                  ;       COM_17_move_to(obj=OBJ_64_WHITE_CUBE, destination=OBJ_7F_TWO_INCH_HOLE)
A8DF:    02 09                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0009
;           TWO INCH HOLE
A8E1:       C1 C0 D0 15 13 54 7E 74 45   ; 

; -------------- Object OBJ_80_WISDOM --------------
A8EA: 00 03                              ; Word_num=0x00 -none-, length=0x0003
A8EC: 00 00 80                           ; Location=0x00, disk_section=0, data=0, attributes=0b10000000

; -------------- Object OBJ_81_GREEN_CUBE --------------
A8EF: 5C 55                              ; Word_num=0x5C CUBE, length=0x0055
A8F1: DB 05 A0                           ; Location=0xDB, disk_section=5, data=0, attributes=0b10100000
A8F4:    03 1A                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x001A
A8F6:       04 18                        ;     COM_04_print_command length=0x0018
A8F8:          5F BE 5B B1 4B 7B 56 45 2B D2 8D 7A 09 71 67 B1 ; 
A908:          85 96 AF C3 9F 15 7F B1   ; 
;
;              THERE IS A TWO INCH GREEN CUBE HERE.
;
A910:    07 1F                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x001F
A912:       0D 1D                        ;     COM_0D_while_pass length=0x001D
A914:          0E 04                     ;       COM_0E_while_fail length=0x0004
A916:             0A 05                  ;         COM_0A_is_input_phrase(phrase=GET ..C..... * *)
A918:             0A 43                  ;         COM_0A_is_input_phrase(phrase=GET ..C..... WITH ..C.....)
A91A:          03 67 81                  ;       COM_03_is_located(owner=OBJ_67_HOLE, obj=OBJ_81_GREEN_CUBE)
A91D:          03 3F 3E                  ;       COM_03_is_located(owner=OBJ_3F_YELLOW_BUTTON, obj=OBJ_3E_??)
A920:          04 0D                     ;       COM_04_print_command length=0x000D
A922:             5F BE C8 16 33 48 C9 54 B5 B7 B2 17 2E ; 
;
;                 THE OVAL CLOSES UP.
;
A92F:          9E                        ;       FN_9E_??
A930:          0C                        ;       COM_0C_fail()
A931:    0C 01                           ;   Section=0C:SECTION_0C_WEIGHT, length=0x0001
A933:       06                           ;     Weight=6
A934:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
A936:       6A                           ;     GREEN
A937:    02 0D                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x000D
;           TWO INCH GREEN CUBE
A939:       C1 C0 D0 15 13 54 AF 6E 83 61 24 56 45 ; 

; -------------- Object OBJ_82_ROD_WITH_SPHERE --------------
A946: 6E 80 AE                           ; Word_num=0x6E ROD, length=0x00AE
A949: DB 05 A0                           ; Location=0xDB, disk_section=5, data=0, attributes=0b10100000
A94C:    03 1D                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x001D
A94E:       04 1B                        ;     COM_04_print_command length=0x001B
A950:          5F BE 5B B1 4B 7B 54 45 73 9E 56 D1 03 71 84 15 ; 
A960:          30 60 62 17 F4 72 4A 5E 2F 62 2E ; 
;
;              THERE IS A ROD WITH A GREEN SPHERE HERE.
;
A96B:    0C 01                           ;   Section=0C:SECTION_0C_WEIGHT, length=0x0001
A96D:       10                           ;     Weight=16
A96E:    08 77                           ;   Section=08:SECTION_08_EVERY_TURN, length=0x0077
A970:       0E 75                        ;     COM_0E_while_fail length=0x0075
A972:          0D 25                     ;       COM_0D_while_pass length=0x0025
A974:             03 90 01               ;         COM_03_is_located(owner=RM_1_90_??, obj=OBJ_01_PLAYER)
A977:             1F 20                  ;         COM_1F_print2 length=0x0020
A979:                5F BE 84 15 30 60 62 17 F4 72 4B 5E D5 B5 89 8D ; 
A989:                FB 8E 7B 67 23 B8 AB 98 8E 48 AF 14 E3 61 CF 98 ; 
;
;                    THE GREEN SPHERE IS SLOWLY FLASHING AND BEEPING.
;
A999:          0D 25                     ;       COM_0D_while_pass length=0x0025
A99B:             03 91 01               ;         COM_03_is_located(owner=RM_1_91_??, obj=OBJ_01_PLAYER)
A99E:             1F 20                  ;         COM_1F_print2 length=0x0020
A9A0:                5F BE 84 15 30 60 62 17 F4 72 4B 5E C8 B5 55 8B ; 
A9B0:                90 73 C3 6A 33 98 67 4D 90 A5 CE 6A 26 A1 47 62 ; 
;
;                    THE GREEN SPHERE IS FLASHING AND BEEPING LOUDER.
;
A9C0:          0D 25                     ;       COM_0D_while_pass length=0x0025
A9C2:             03 92 01               ;         COM_03_is_located(owner=RM_1_92_??, obj=OBJ_01_PLAYER)
A9C5:             1F 20                  ;         COM_1F_print2 length=0x0020
A9C7:                5F BE 84 15 30 60 62 17 F4 72 4B 5E C8 B5 55 8B ; 
A9D7:                90 73 C3 6A 33 98 67 4D 90 A5 D9 6A 3E 7A F9 8E ; 
;
;                    THE GREEN SPHERE IS FLASHING AND BEEPING WILDLY!
;
A9E7:    02 0E                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x000E
;           ROD WITH GREEN SPHERE
A9E9:       F6 B2 FB 17 53 BE AF 6E 83 61 62 B9 2F 62 ; 

; -------------- Object OBJ_83_?? --------------
A9F7: 00 03                              ; Word_num=0x00 -none-, length=0x0003
A9F9: 00 00 80                           ; Location=0x00, disk_section=0, data=0, attributes=0b10000000

; -------------- Object OBJ_84_?? --------------
A9FC: 00 03                              ; Word_num=0x00 -none-, length=0x0003
A9FE: 00 00 80                           ; Location=0x00, disk_section=0, data=0, attributes=0b10000000

; -------------- Object OBJ_85_CYLINDER_BOMB --------------
AA01: 5E 2B                              ; Word_num=0x5E CYLIND, length=0x002B
AA03: 94 07 80                           ; Location=0x94, disk_section=7, data=0, attributes=0b10000000
AA06:    07 1E                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x001E
AA08:       0D 1C                        ;     COM_0D_while_pass length=0x001C
AA0A:          C4                        ;       FN_C4_??
AA0B:          04 15                     ;       COM_04_print_command length=0x0015
AA0D:             1D 85 01 4F 41 A0 EB 8F C7 DE 57 17 11 BC 83 66 ; 
AA1D:             44 45 E4 9F 21         ; 
;
;                 KA-BOOOOOM! YOU SET OFF A BOMB!
;
AA22:          1C 01                     ;       COM_1C_set_var_object(obj=OBJ_01_PLAYER)
AA24:          1D 4B                     ;       COM_1D_attack_var(points=75)
AA26:    02 06                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0006
;           CYLINDER 
AA28:       CE 56 8E 7A 23 62            ; 

; -------------- Object OBJ_86_CYLINDER_POISON --------------
AA2E: 5E 5C                              ; Word_num=0x5E CYLIND, length=0x005C
AA30: 95 07 80                           ; Location=0x95, disk_section=7, data=0, attributes=0b10000000
AA33:    07 4F                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x004F
AA35:       0D 4D                        ;     COM_0D_while_pass length=0x004D
AA37:          C4                        ;       FN_C4_??
AA38:          04 46                     ;       COM_04_print_command length=0x0046
AA3A:             13 9F E9 99 C0 16 51 5E 96 64 DB 72 CE 56 8E 7A ; 
AA4A:             3D 62 4F 15 F3 8C 6B BF 5F BE 56 15 44 A0 90 14 ; 
AA5A:             04 58 FD B2 EB 5D 73 7B 4B 7B 6E B1 95 5F 91 7A ; 
AA6A:             73 15 6B B5 47 55 36 6D E1 14 7A C4 09 EE 62 49 ; 
AA7A:             D2 06 55 9F 01 A0      ; 
;
;                 OH NO! ONE OF THE CYLINDERS FELL TO THE FLOOR AND BROKE! IT
;                 IS RELEASING GAS! COUGH, COUGH, GASP! POISON!
;
AA80:          1C 01                     ;       COM_1C_set_var_object(obj=OBJ_01_PLAYER)
AA82:          1D 4B                     ;       COM_1D_attack_var(points=75)
AA84:    02 06                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0006
;           CYLINDER 
AA86:       CE 56 8E 7A 23 62            ; 

; -------------- Object OBJ_87_CYLINDER_ANTS --------------
AA8C: 5E 69                              ; Word_num=0x5E CYLIND, length=0x0069
AA8E: 97 07 80                           ; Location=0x97, disk_section=7, data=0, attributes=0b10000000
AA91:    07 5C                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x005C
AA93:       0D 5A                        ;     COM_0D_while_pass length=0x005A
AA95:          C4                        ;       FN_C4_??
AA96:          04 54                     ;       COM_04_print_command length=0x0054
AA98:             E9 C5 84 96 D0 60 C6 6A 66 7B 2C C6 16 60 82 17 ; 
AAA8:             49 5E 74 8D 51 5E F0 A4 C3 B5 33 98 4A 45 14 9E ; 
AAB8:             11 58 96 64 EF 74 4B 5E 1A 98 49 16 AB 98 9E 48 ; 
AAC8:             CB B5 D4 B5 3F 61 57 49 AB 57 5F BE 44 DB 7B 60 ; 
AAD8:             85 96 D9 B0 90 8C C3 6A F3 8C 4F A1 96 AF DB 72 ; 
AAE8:             FB A5 99 53            ; 
;
;                 UPON BEING DISTURBED, THE GLOBE OPENS AND A HOARD OF THREE
;                 INCH LONG ANTS IS RELEASED! THEY BEGIN CRAWLING ALL OVER
;                 THE PLACE!
;
AAEC:          17 89 97                  ;       COM_17_move_to(obj=OBJ_89_ALIEN_ANTS, destination=RM_1_97_??)
AAEF:    02 06                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0006
;           CYLINDER 
AAF1:       CE 56 8E 7A 23 62            ; 

; -------------- Object OBJ_88_CYLINDERS_UNABLE --------------
AAF7: 5E 2E                              ; Word_num=0x5E CYLIND, length=0x002E
AAF9: 99 07 80                           ; Location=0x99, disk_section=7, data=0, attributes=0b10000000
AAFC:    07 21                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0021
AAFE:       0D 1F                        ;     COM_0D_while_pass length=0x001F
AB00:          C4                        ;       FN_C4_??
AB01:          04 1C                     ;       COM_04_print_command length=0x001C
AB03:             C7 DE 94 14 57 5E C4 97 DB 8B 6B BF 50 47 E6 5F ; 
AB13:             82 17 57 62 EB 14 90 8C F4 59 5B BB ; 
;
;                 YOU ARE UNABLE TO AFFECT THESE CYLINDERS. 
;
AB1F:    02 06                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0006
;           CYLINDER 
AB21:       CE 56 8E 7A 23 62            ; 

; -------------- Object OBJ_89_ALIEN_ANTS --------------
AB27: 5B 81 6B                           ; Word_num=0x5B ALIEN, length=0x016B
AB2A: 00 00 90                           ; Location=0x00, disk_section=0, data=0, attributes=0b10010000
AB2D:    03 22                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0022
AB2F:       04 20                        ;     COM_04_print_command length=0x0020
AB31:          6C BE 1B 60 8D 7A 03 71 CD 9A 94 14 45 5E D9 B0 ; 
AB41:          90 8C C3 6A F3 8C 4F A1 96 AF DB 72 FB A5 99 53 ; 
;
;              THREE INCH ANTS ARE CRAWLING ALL OVER THE PLACE!
;
AB51:    07 81 1C                        ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x011C
AB54:       0D 81 19                     ;     COM_0D_while_pass length=0x0119
AB57:          0A 09                     ;       COM_0A_is_input_phrase(phrase=ATTACK ...P.... WITH .v......)
AB59:          0E 81 14                  ;       COM_0E_while_fail length=0x0114
AB5C:             0D 80 81               ;         COM_0D_while_pass length=0x0081
AB5F:                09 5C               ;           COM_09_compare_to_second_noun(obj=OBJ_5C_PAIR_HANDS)
AB61:                04 79               ;           COM_04_print_command length=0x0079
AB63:                   09 BA E3 93 AB 98 8E 48 5E 17 EA 48 91 7A 96 14 ; 
AB73:                   82 17 56 5E 87 74 10 B7 0B 5C C3 9E AF 55 8F 49 ; 
AB83:                   75 B1 51 18 4D C2 46 7A 63 16 9F 9B BF 14 03 BC ; 
AB93:                   DB B5 1B A1 67 66 16 8A DB 72 70 CA DB 9F C3 9E ; 
ABA3:                   5F BE 23 7B 03 BA CE 98 51 18 54 C2 8E 5F 6F 7C ; 
ABB3:                   51 18 23 C6 FE 67 1F 8F A9 15 B8 D0 46 62 D6 15 ; 
ABC3:                   D5 15 89 17 CE 9C 7F 49 89 17 09 15 90 14 82 DF ; 
ABD3:                   91 7A 84 14 36 A1 D6 15 2E ; 
;
;                       STOMPING AND SLAPPING AT THE THOUSANDS OF CREATURES YOU
;                       KILL MANY. BUT AS YOU FEEL THE VENOM OF THEIR STING, YOU
;                       REALIZE YOUR FOLLY. HOWEVER, IT IS TOO LATE TO DO ANYTHING
;                       ABOUT IT.
;
ABDC:                1C 01               ;           COM_1C_set_var_object(obj=OBJ_01_PLAYER)
ABDE:                1D 4B               ;           COM_1D_attack_var(points=75)
ABE0:             0D 80 8D               ;         COM_0D_while_pass length=0x008D
ABE3:                0E 06               ;           COM_0E_while_fail length=0x0006
ABE5:                   09 32            ;             COM_09_compare_to_second_noun(obj=OBJ_32_SHOVEL)
ABE7:                   09 28            ;             COM_09_compare_to_second_noun(obj=OBJ_28_SHOTGUN)
ABE9:                   09 24            ;             COM_09_compare_to_second_noun(obj=OBJ_24_CROWBAR)
ABEB:                04 7F               ;           COM_04_print_command length=0x007F
ABED:                   C7 DE 2B 17 83 7A 89 4E CB D2 89 5B 91 96 96 96 ; 
ABFD:                   DB 72 90 91 45 DB 63 B1 74 C0 4B 62 AB 55 C3 D1 ; 
AC0D:                   AB 98 03 A0 5F BE 56 15 44 A0 55 F4 FE C3 96 61 ; 
AC1D:                   5B DB 1B A1 67 66 03 8A BF 14 D3 B2 AB 98 4B A4 ; 
AC2D:                   91 96 9B 96 34 A1 3F 16 C3 6A D1 B5 5B 98 C3 9E ; 
AC3D:                   5F BE E4 14 96 5F 2F C6 D5 B5 90 BE CB 6E C7 DE ; 
AC4D:                   5B F4 1B A1 55 A4 D1 B5 73 C6 A5 B7 0E A0 CE B5 ; 
AC5D:                   7F 49 F3 B4 78 98 23 62 6B BF F3 49 B0 85 2E ; 
;
;                       YOU RAIN BLOWS DOWN ON THE MANY CREATURES CRAWLING ON THE
;                       FLOOR. SUDDENLY YOU FEEL A BURNING PAIN ON YOUR LEG AS ONE
;                       OF THE CREATURES STINGS YOU. YOU PASS OUT SECONDS LATER,
;                       NEVER TO AWAKEN.
;
AC6C:                1C 01               ;           COM_1C_set_var_object(obj=OBJ_01_PLAYER)
AC6E:                1D 4B               ;           COM_1D_attack_var(points=75)
AC70:    08 18                           ;   Section=08:SECTION_08_EVERY_TURN, length=0x0018
AC72:       1F 16                        ;     COM_1F_print2 length=0x0016
AC74:          5F BE 90 14 0B C0 2F 49 E4 14 FE 49 91 7A 38 15 ; 
AC84:          43 62 1F D1 59 B1         ; 
;
;              THE ANTS ARE CRAWLING EVERYWHERE!
;
AC8A:    02 09                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0009
;           HOARD OF ANTS
AC8C:       73 74 33 B1 C3 9E 9E 48 53   ; 

; -------------- Object OBJ_8A_DEAD_ALIEN --------------
AC95: 5B 22                              ; Word_num=0x5B ALIEN, length=0x0022
AC97: 00 00 80                           ; Location=0x00, disk_section=0, data=0, attributes=0b10000000
AC9A:    03 14                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0014
AC9C:       04 12                        ;     COM_04_print_command length=0x0012
AC9E:          5F BE 5B B1 4B 7B 46 45 86 5F 8E 14 30 79 9F 15 ; 
ACAE:          7F B1                     ; 
;
;              THERE IS A DEAD ALIEN HERE.
;
ACB0:    02 07                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0007
;           DEAD ALIEN
ACB2:       E3 59 03 58 87 8C 4E         ; 

; -------------- Object OBJ_8B_SQUIRMING_ALIEN --------------
ACB9: 5B 7C                              ; Word_num=0x5B ALIEN, length=0x007C
ACBB: DB 05 90                           ; Location=0xDB, disk_section=5, data=0, attributes=0b10010000
ACBE:    03 77                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0077
ACC0:       0D 75                        ;     COM_0D_while_pass length=0x0075
ACC2:          17 8B 00                  ;       COM_17_move_to(obj=OBJ_8B_SQUIRMING_ALIEN, destination=nowhere)
ACC5:          17 8A DB                  ;       COM_17_move_to(obj=OBJ_8A_DEAD_ALIEN, destination=RM_1_DB_??)
ACC8:          38                        ;       COM_38_bump_score()
ACC9:          04 6C                     ;       COM_04_print_command length=0x006C
ACCB:             63 98 03 B1 03 EE 83 96 87 8C 84 96 D0 60 CB 6A ; 
ACDB:             D5 B5 AB AD AB B2 AB 98 03 A0 5F BE 84 15 30 A1 ; 
ACEB:             AB 57 73 7B 81 8D CB 87 D3 C5 73 49 C7 DE 90 14 ; 
ACFB:             15 58 55 4A 71 13 E7 8B 81 A6 AC A2 9F 15 E9 16 ; 
AD0B:             9E 7A C3 B5 16 BC DB 72 24 56 43 5E 33 98 5F BE ; 
AD1B:             92 96 50 9F 0B C0 B5 D0 9B C1 DB 72 5F BE 84 96 ; 
AD2B:             E1 5F 35 92 CF 17 7B B4 03 BA 17 8D ; 
;
;                 NEARBY, AN ALIEN BEING IS SQUIRMING ON THE GROUND! IT LOOKS
;                 UP AT YOU AND SAYS "GLEEPOOP!" HE POINTS AT THE CUBE AND
;                 THEN POINTS WEST. HE THEN BECOMES VERY STILL.
;

; -------------- Object OBJ_8C_PROSPECTOR --------------
AD37: 70 81 BD                           ; Word_num=0x70 PROSPE, length=0x01BD
AD3A: E8 05 90                           ; Location=0xE8, disk_section=5, data=0, attributes=0b10010000
AD3D:    03 2C                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x002C
AD3F:       04 2A                        ;     COM_04_print_command length=0x002A
AD41:          83 48 BE 9F EC 16 E2 A0 E6 5F A3 A0 FB B9 4D 98 ; 
AD51:          9F 15 7F B1 9F 15 57 17 75 61 89 17 AF 14 DE 14 ; 
AD61:          90 5F 91 7A A3 15 C9 B5 A7 C5 ; 
;
;              AN OLD PROSPECTOR STANDS HERE. HE SEEMS TO BE CLEANING HIS
;              GUN.
;
AD6B:    07 62                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0062
AD6D:       0D 60                        ;     COM_0D_while_pass length=0x0060
AD6F:          0E 05                     ;       COM_0E_while_fail length=0x0005
AD71:             C4                     ;         FN_C4_??
AD72:             0A 0E                  ;         COM_0A_is_input_phrase(phrase=THROW u....... TO ...P....)
AD74:             0A 57                  ;         COM_0A_is_input_phrase(phrase=SHOOT u....... WITH u.......)
AD76:          04 53                     ;       COM_04_print_command length=0x0053
AD78:             4B 49 C7 DE AF 14 50 6D 89 17 71 16 7E CA 9F 15 ; 
AD88:             2B 17 57 7B CA B5 4B 7B 30 6F 90 14 12 58 50 9F ; 
AD98:             0B C0 73 7B 73 49 C7 DE BF 06 44 2C 4F 8B BE 06 ; 
ADA8:             FC 25 46 6E 43 18 C6 06 64 C5 DB 14 FB C0 FE 67 ; 
ADB8:             33 89 59 77 60 49 F3 23 04 4F 9B 96 66 62 2E 62 ; 
ADC8:             19 60 22               ; 
;
;                 AS YOU BEGIN TO MOVE, HE RAISES HIS GUN AND POINTS IT AT
;                 YOU! >> BLAM! << "GOT YA! DUMB CITY FOLK, I WASN'T BORN
;                 YESTERDEE!"
;
ADCB:          1C 01                     ;       COM_1C_set_var_object(obj=OBJ_01_PLAYER)
ADCD:          1D 4B                     ;       COM_1D_attack_var(points=75)
ADCF:    08 81 1C                        ;   Section=08:SECTION_08_EVERY_TURN, length=0x011C
ADD2:       0E 81 19                     ;     COM_0E_while_fail length=0x0119
ADD5:          0D 1F                     ;       COM_0D_while_pass length=0x001F
ADD7:             03 01 8D               ;         COM_03_is_located(owner=OBJ_01_PLAYER, obj=OBJ_8D_??)
ADDA:             1F 1A                  ;         COM_1F_print2 length=0x001A
ADDC:                91 1E 55 C2 8E BE 0A 8A 2F 62 A3 00 1B B7 D6 B5 ; 
ADEC:                DB 72 F9 A6 5F B9 09 56 1B B5 ; 
;
;                    "YOU STILL HERE?" SAYS THE PROSPECTOR. 
;
ADF6:          0D 80 F5                  ;       COM_0D_while_pass length=0x00F5
ADF9:             14                     ;         COM_14_execute_and_reverse_status next command
ADFA:             0E 08                  ;         COM_0E_while_fail length=0x0008
ADFC:                0A 03               ;           COM_0A_is_input_phrase(phrase=EAST * * *)
ADFE:                0A 04               ;           COM_0A_is_input_phrase(phrase=WEST * * *)
AE00:                0A 01               ;           COM_0A_is_input_phrase(phrase=NORTH * * *)
AE02:                0A 02               ;           COM_0A_is_input_phrase(phrase=SOUTH * * *)
AE04:             01 01                  ;         COM_01_is_in_pack_or_room(obj=OBJ_01_PLAYER)
AE06:             1F 80 E2               ;         COM_1F_print2 length=0x00E2
AE09:                5F BE EC 16 E2 A0 E6 5F A3 A0 81 8D CB 87 C7 DE ; 
AE19:                03 15 65 B1 13 BF D0 15 82 17 47 5E 35 DD 90 14 ; 
AE29:                15 58 55 4A FC ED 55 77 30 60 7B 14 0C BA 91 48 ; 
AE39:                56 5E 90 73 D1 6A 73 C6 B5 D0 AB BB 3F B9 4D 5E ; 
AE49:                8E 7A B8 16 E4 14 96 5F 2F C6 CB 06 5A 17 F3 A0 ; 
AE59:                8F 73 FA 17 83 61 55 77 30 60 A3 15 DB 95 43 79 ; 
AE69:                C7 DE 94 14 46 5E 64 C5 30 15 29 A1 16 71 CA 9C ; 
AE79:                86 5F 82 17 73 49 1B D0 0E EE 3D A0 C7 16 08 BC ; 
AE89:                A3 A0 5F BE 63 16 0F 6E 85 BE A0 13 E3 9F 13 8D ; 
AE99:                5B F4 1B A1 47 55 B3 8B 5F B9 33 98 5F BE 2F 17 ; 
AEA9:                F3 B9 C3 9E C7 DE 8E AF 4F 79 D0 15 82 17 4B 7B ; 
AEB9:                F5 59 3E 62 D0 06 8E A1 71 16 5B CA 49 48 AB 98 ; 
AEC9:                98 45 AF A0 BB 15 29 B8 F3 A0 C7 DE E3 06 DB 72 ; 
AED9:                77 5B 05 B9 15 BC 2F 60 CF 17 7B B4 73 68 8E 61 ; 
AEE9:                1F 8F               ; 
;
;                    THE PROSPECTOR LOOKS YOU DIRECTLY IN THE EYES AND SAYS, "I
;                    SEEN A STRANGE THING OUT WEST! SOME KIND OF CREATURE! I
;                    SHOT HIM WHEN I SEEN HIM. IF YOU ARE DUMB ENOUGH TO HEAD
;                    THAT WAY, LOOK OUT FOR THE MAGNETIC 'NOMALLY. YOU COULD
;                    SPEND THE REST OF YOUR LIFE IN THIS DESERT! NOW, MOVE ALONG
;                    A'FORE I SHOOT YOU!" HE DOESN'T SEEM VERY FRIENDLY.
;
AEEB:             17 8D 01               ;         COM_17_move_to(obj=OBJ_8D_??, destination=OBJ_01_PLAYER)
AEEE:    02 07                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0007
;           PROSPECTOR
AEF0:       F9 A6 5F B9 09 56 52         ; 

; -------------- Object OBJ_8D_?? --------------
AEF7: 00 03                              ; Word_num=0x00 -none-, length=0x0003
AEF9: 00 00 80                           ; Location=0x00, disk_section=0, data=0, attributes=0b10000000

; -------------- Object OBJ_8E_MACHINE --------------
AEFC: 6F 0A                              ; Word_num=0x6F MACHIN, length=0x000A
AEFE: 9B 08 80                           ; Location=0x9B, disk_section=8, data=0, attributes=0b10000000
AF01:    02 05                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0005
;           MACHINE
AF03:       85 91 90 73 45               ; 

; -------------- Object OBJ_8F_WHITE_BUTTON_ENGINES --------------
AF08: 4A 80 87                           ; Word_num=0x4A BUTTON, length=0x0087
AF0B: 3A 00 80                           ; Location=0x3A, disk_section=0, data=0, attributes=0b10000000
AF0E:    01 01                           ;   Section=01:SECTION_01_ADJECTIVES, length=0x0001
AF10:       60                           ;     WHITE
AF11:    07 75                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0075
AF13:       0D 73                        ;     COM_0D_while_pass length=0x0073
AF15:          0A 12                     ;       COM_0A_is_input_phrase(phrase=PULL u....... * *)
AF17:          0E 6F                     ;       COM_0E_while_fail length=0x006F
AF19:             0D 6B                  ;         COM_0D_while_pass length=0x006B
AF1B:                04 42               ;           COM_04_print_command length=0x0042
AF1D:                   C3 54 AF 54 51 18 4A C2 94 5F 7B 14 87 8D 14 58 ; 
AF2D:                   64 C5 DB 8B 4B 49 5F BE 5A 17 D3 7A 74 8E 1F 54 ; 
AF3D:                   C8 B5 A3 A0 4F 45 E7 9F D7 9A 82 17 83 61 58 45 ; 
AF4D:                   45 9F 55 5E 55 4A FC ED 6F CC 44 5E 03 A0 56 B8 ; 
AF5D:                   2C E1            ; 
;
;                       CLICK. YOU HEAR A LOUD RUMBLE AS THE SHIP LURCHES FOR A
;                       MOMENT. THEN A VOICE SAYS, "VREE BON SITZ!"
;
AF5F:                03 01 80            ;           COM_03_is_located(owner=OBJ_01_PLAYER, obj=OBJ_80_WISDOM)
AF62:                04 22               ;           COM_04_print_command length=0x0022
AF64:                   C7 DE B0 17 F4 59 FB B9 33 98 63 BE D6 B5 CF 9C ; 
AF74:                   90 5F FC ED 91 61 8F 7A C3 B5 5B B1 4F 59 77 47 ; 
AF84:                   9C 5D            ; 
;
;                       YOU UNDERSTAND THIS TO MEAN, "ENGINES ARE DAMAGED."
;
AF86:             14                     ;         COM_14_execute_and_reverse_status next command
AF87:             0C                     ;         COM_0C_fail()
AF88:    02 08                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0008
;           WHITE BUTTON
AF8A:       23 D1 DB BD F6 4F 80 BF      ; 

; -------------- Object OBJ_90_CHAIR --------------
AF92: 53 0C                              ; Word_num=0x53 CHAIR, length=0x000C
AF94: 89 07 80                           ; Location=0x89, disk_section=7, data=0, attributes=0b10000000
AF97:    07 01                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0001
AF99:       C5                           ;     FN_C5_??
AF9A:    02 04                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0004
;           CHAIR 
AF9C:       1B 54 23 7B                  ; 

; -------------- Object OBJ_91_POISON --------------
AFA0: 00 09                              ; Word_num=0x00 -none-, length=0x0009
AFA2: 00 00 A0                           ; Location=0x00, disk_section=0, data=0, attributes=0b10100000
AFA5:    02 04                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0004
;           POISON
AFA7:       7B A6 40 B9                  ; 

; -------------- Object OBJ_92_SCORE --------------
AFAB: 00 03                              ; Word_num=0x00 -none-, length=0x0003
AFAD: 00 00 00                           ; Location=0x00, disk_section=0, data=0, attributes=0b00000000

; -------------- Object OBJ_93_DOOR_ESNEL --------------
AFB0: 10 09                              ; Word_num=0x10 DOOR, length=0x0009
AFB2: 83 29 88                           ; Location=0x83, disk_section=9, data=2, attributes=0b10001000
AFB5:    02 04                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0004
;           ESNEL 
AFB7:       60 62 33 61                  ; 

; -------------- Object OBJ_94_GOOLUB --------------
AFBB: 71 32                              ; Word_num=0x71 GOOLUB, length=0x0032
AFBD: 31 00 90                           ; Location=0x31, disk_section=0, data=0, attributes=0b10010000
AFC0:    07 27                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0027
AFC2:       0D 25                        ;     COM_0D_while_pass length=0x0025
AFC4:          0E 05                     ;       COM_0E_while_fail length=0x0005
AFC6:             C4                     ;         FN_C4_??
AFC7:             0A 09                  ;         COM_0A_is_input_phrase(phrase=ATTACK ...P.... WITH .v......)
AFC9:             0A 57                  ;         COM_0A_is_input_phrase(phrase=SHOOT u....... WITH u.......)
AFCB:          04 0E                     ;       COM_04_print_command length=0x000E
AFCD:             E9 C5 84 96 D0 60 C6 6A 66 7B 2C C6 16 60 ; 
;
;                 UPON BEING DISTURBED,
;
AFDB:          A8                        ;       FN_A8_PRINT_noun1
AFDC:          04 08                     ;       COM_04_print_command length=0x0008
AFDE:             83 67 4B 62 F3 49 DB E0 ; 
;
;                 FLIES AWAY. 
;
AFE6:          17 94 00                  ;       COM_17_move_to(obj=OBJ_94_GOOLUB, destination=nowhere)
AFE9:    02 04                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0004
;           GOOLUB
AFEB:       41 6E 64 8E                  ; 

; -------------- Object OBJ_95_DOOR_ESNEL --------------
AFEF: 10 2C                              ; Word_num=0x10 DOOR, length=0x002C
AFF1: 87 69 88                           ; Location=0x87, disk_section=9, data=6, attributes=0b10001000
AFF4:    07 21                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0021
AFF6:       0E 1F                        ;     COM_0E_while_fail length=0x001F
AFF8:          0D 0C                     ;       COM_0D_while_pass length=0x000C
AFFA:             0E 06                  ;         COM_0E_while_fail length=0x0006
AFFC:                0A 3A               ;           COM_0A_is_input_phrase(phrase=OPEN u....... WITH u.......)
AFFE:                0A 42               ;           COM_0A_is_input_phrase(phrase=UNLOCK u....... WITH u.......)
B000:                0A 41               ;           COM_0A_is_input_phrase(phrase=LOCK ....A... WITH u.......)
B002:             14                     ;         COM_14_execute_and_reverse_status next command
B003:             09 97                  ;         COM_09_compare_to_second_noun(obj=OBJ_97_SMALL_UKORK_KEY)
B005:             BA                     ;         FN_BA_??
B006:          0D 0F                     ;       COM_0D_while_pass length=0x000F
B008:             0A 11                  ;         COM_0A_is_input_phrase(phrase=OPEN u....... * *)
B00A:             1A                     ;         COM_1A_set_var_to_first_noun()
B00B:             2E 40                  ;         UNKNOWN2E, Value: 0x40
B00D:             A8                     ;         FN_A8_PRINT_noun1
B00E:             04 07                  ;         COM_04_print_command length=0x0007
B010:                4B 7B 44 87 B0 85 2E ; 
;
;                    IS KORKEN.
;
B017:    02 04                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0004
;           ESNEL 
B019:       60 62 33 61                  ; 

; -------------- Object OBJ_96_DOOR_ESNEL --------------
B01D: 10 2C                              ; Word_num=0x10 DOOR, length=0x002C
B01F: 89 69 88                           ; Location=0x89, disk_section=9, data=6, attributes=0b10001000
B022:    07 21                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0021
B024:       0E 1F                        ;     COM_0E_while_fail length=0x001F
B026:          0D 0C                     ;       COM_0D_while_pass length=0x000C
B028:             0E 06                  ;         COM_0E_while_fail length=0x0006
B02A:                0A 3A               ;           COM_0A_is_input_phrase(phrase=OPEN u....... WITH u.......)
B02C:                0A 42               ;           COM_0A_is_input_phrase(phrase=UNLOCK u....... WITH u.......)
B02E:                0A 41               ;           COM_0A_is_input_phrase(phrase=LOCK ....A... WITH u.......)
B030:             14                     ;         COM_14_execute_and_reverse_status next command
B031:             09 97                  ;         COM_09_compare_to_second_noun(obj=OBJ_97_SMALL_UKORK_KEY)
B033:             BA                     ;         FN_BA_??
B034:          0D 0F                     ;       COM_0D_while_pass length=0x000F
B036:             0A 11                  ;         COM_0A_is_input_phrase(phrase=OPEN u....... * *)
B038:             1A                     ;         COM_1A_set_var_to_first_noun()
B039:             2E 40                  ;         UNKNOWN2E, Value: 0x40
B03B:             A8                     ;         FN_A8_PRINT_noun1
B03C:             04 07                  ;         COM_04_print_command length=0x0007
B03E:                4B 7B 44 87 B0 85 2E ; 
;
;                    IS KORKEN.
;
B045:    02 04                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0004
;           ESNEL 
B047:       60 62 33 61                  ; 

; -------------- Object OBJ_97_SMALL_UKORK_KEY --------------
B04B: 16 77                              ; Word_num=0x16 KEY, length=0x0077
B04D: 86 09 A4                           ; Location=0x86, disk_section=9, data=0, attributes=0b10100100
B050:    03 15                           ;   Section=03:SECTION_03_DESCRIPTION, length=0x0015
B052:       04 13                        ;     COM_04_print_command length=0x0013
B054:          5F BE 5B B1 4B 7B 55 45 8E 91 17 8A 44 87 CA 83 ; 
B064:          2F 62 2E                  ; 
;
;              THERE IS A SMALL UKORK HERE.
;
B067:    07 51                           ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x0051
B069:       0D 4F                        ;     COM_0D_while_pass length=0x004F
B06B:          0A 08                     ;       COM_0A_is_input_phrase(phrase=READ .....?.. * *)
B06D:          04 0F                     ;       COM_04_print_command length=0x000F
B06F:             04 1D AE 85 EB B8 18 BC 67 B1 05 4F 4E BD 22 ; 
;
;                 "ORKELSMIT VREEBOSTAL"
;
B07E:          0E 3A                     ;       COM_0E_while_fail length=0x003A
B080:             0D 36                  ;         COM_0D_while_pass length=0x0036
B082:                03 01 80            ;           COM_03_is_located(owner=OBJ_01_PLAYER, obj=OBJ_80_WISDOM)
B085:                04 31               ;           COM_04_print_command length=0x0031
B087:                   FA 17 DA 78 67 16 9D 48 FC ED 43 79 07 68 56 98 ; 
B097:                   0C 15 53 A0 83 7A A3 48 63 16 3C 7A B7 A1 2F 17 ; 
B0A7:                   74 C0 92 96 E6 A0 77 47 87 15 3F 49 BF 9A 17 60 ; 
B0B7:                   22               ; 
;
;                        WHICH MEANS, "IF FOUND, DROP IN ANY MAILBOX. RETURN
;                       POSTAGE GUARUNTEED."
;
B0B8:             14                     ;         COM_14_execute_and_reverse_status next command
B0B9:             0C                     ;         COM_0C_fail()
B0BA:    02 08                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0008
;           SMALL UKORK 
B0BC:       E3 B8 F3 8C 21 C5 4B B2      ; 

; -------------- Object OBJ_98_BLURNUM_RADIO --------------
B0C4: 12 81 87                           ; Word_num=0x12 RADIO, length=0x0187
B0C7: 8B 09 80                           ; Location=0x8B, disk_section=9, data=0, attributes=0b10000000
B0CA:    07 81 7A                        ;   Section=07:SECTION_07_IF_FIRST_NOUN, length=0x017A
B0CD:       0E 81 77                     ;     COM_0E_while_fail length=0x0177
B0D0:          0D 73                     ;       COM_0D_while_pass length=0x0073
B0D2:             0A 50                  ;         COM_0A_is_input_phrase(phrase=TURN * ON u.......)
B0D4:             03 00 71               ;         COM_03_is_located(owner=nowhere, obj=OBJ_71_GREEN_BUTTON_WEAPON)
B0D7:             04 6C                  ;         COM_04_print_command length=0x006C
B0D9:                C2 1D 4B 5E 0B 9B 51 B8 91 96 96 64 DB 72 FB A5 ; 
B0E9:                76 98 55 17 0F B2 00 81 D5 15 81 15 91 7A F7 17 ; 
B0F9:                17 8D D6 15 9B 15 C4 B5 30 60 FF 14 F4 BD D0 92 ; 
B109:                F3 5F 5B BE 15 BC B3 55 F9 92 8B 96 CF B5 DA C3 ; 
B119:                71 16 5B B1 2B BA 44 BD DB 8B 6B BF 34 A1 8F 16 ; 
B129:                0D 60 AF 14 17 53 BE B7 AA 17 07 EE 3E 49 0B 71 ; 
B139:                D6 B5 4E A0 AA 17 15 EE 8E 91 9C 8F ; 
;
;                    "THE INVASION OF THE PLANET SCRIMJON IS GOING WELL. IT HAS
;                    BEEN DETERMINED THAT SCRIMJON IS MUCH MORE SUITABLE TO OUR
;                    NEEDS BECAUSE, UH, EARTH IS TOO, UH, SMALL."
;
B145:          0D 80 9B                  ;       COM_0D_while_pass length=0x009B
B148:             0A 50                  ;         COM_0A_is_input_phrase(phrase=TURN * ON u.......)
B14A:             03 01 80               ;         COM_03_is_located(owner=OBJ_01_PLAYER, obj=OBJ_80_WISDOM)
B14D:             0A 50                  ;         COM_0A_is_input_phrase(phrase=TURN * ON u.......)
B14F:             04 80 91               ;         COM_04_print_command length=0x0091
B152:                7A 1B B2 53 08 BC A3 A0 5F BE E4 14 5A 49 B8 16 ; 
B162:                82 17 55 5E 47 55 15 BC 92 73 16 EE DB 72 A0 7A ; 
B172:                5B 49 03 A0 C3 9E 5F BE E6 16 8F 48 07 BC 3E 49 ; 
B182:                0B 71 C9 B5 50 9F D9 6A 46 61 56 F4 DB 72 C6 93 ; 
B192:                F4 72 5A 17 D3 7A 4B 7B 09 9A D0 15 C4 16 16 4E ; 
B1A2:                03 EE 33 98 4E D1 15 8A 40 A0 AF 14 50 6D 82 17 ; 
B1B2:                52 5E 31 C6 51 5E 8E 64 4F 79 59 15 B5 B2 54 F4 ; 
B1C2:                E9 61 B3 B3 6B BF C7 DE 95 AF 09 A6 0F A0 F6 B0 ; 
B1D2:                A3 46 83 7A 6C BE 1B 60 7F 67 30 60 69 B9 2F C0 ; 
B1E2:                22                  ; 
;
;                    "EXCEPT FOR THE CRASH OF THE SCOUT SHIP, THE INVASION OF
;                    THE PLANET EARTH IS GOING WELL. THE MOTHER SHIP IS NOW IN
;                    ORBIT, AND WILL SOON BEGIN THE PURGE OF LIFE FORMS. REPORT
;                    TO YOUR SPLOONERBLAB IN THREE FLEEENSPOTS."
;
B1E3:          0D 56                     ;       COM_0D_while_pass length=0x0056
B1E5:             0A 50                  ;         COM_0A_is_input_phrase(phrase=TURN * ON u.......)
B1E7:             04 52                  ;         COM_04_print_command length=0x0052
B1E9:                5D 1E 33 A7 BD 55 15 71 F3 55 2A B8 10 EE A0 CC ; 
B1F9:                E6 16 B3 9A C2 B3 80 15 D9 6A 17 8D 76 16 E3 74 ; 
B209:                2A B8 83 16 FE B0 8E 16 FE 17 15 8A 95 96 FE BF ; 
B219:                EC 16 C8 6A 40 16 5C 15 6F 94 3A 17 B3 B3 1B BC ; 
B229:                95 AF 08 A6 F6 B0 90 4B 82 17 88 AF 5D 8D 4D A7 ; 
B239:                63 F4               ; 
;
;                    "XCPT CRSH SCT SHP, NVSN PLNT RTH GNG WLL. MTHR SHP N RBT
;                    ND WLL SN STRT PRG F LF FRMS. RPRT T YR SPLNRBLB N THR
;                    FLNSPTS."
;
B23B:          0D 0A                     ;       COM_0D_while_pass length=0x000A
B23D:             0A 0B                  ;         COM_0A_is_input_phrase(phrase=LOOK * AT u.......)
B23F:             A8                     ;         FN_A8_PRINT_noun1
B240:             04 05                  ;         COM_04_print_command length=0x0005
B242:                4B 7B D0 9E 2E      ; 
;
;                    IS OFF.
;
B247:    02 05                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0005
;           BLURNUM
B249:       8F 4E DF B2 4D               ; 

; -------------- Object OBJ_99_SHIP --------------
B24E: 66 08                              ; Word_num=0x66 SHIP, length=0x0008
B250: 9D 05 80                           ; Location=0x9D, disk_section=5, data=0, attributes=0b10000000
B253:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           SHIP
B255:       23 B8 50                     ; 

; -------------- Object OBJ_9A_WALL --------------
B258: 25 08                              ; Word_num=0x25 WALL, length=0x0008
B25A: 01 00 80                           ; Location=0x01, disk_section=0, data=0, attributes=0b10000000
B25D:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           WALL
B25F:       0E D0 4C                     ; 

; -------------- Object OBJ_9B_?? --------------
B262: 00 03                              ; Word_num=0x00 -none-, length=0x0003
B264: 00 00 00                           ; Location=0x00, disk_section=0, data=0, attributes=0b00000000

; -------------- Object OBJ_9C_SHIP --------------
B267: 66 08                              ; Word_num=0x66 SHIP, length=0x0008
B269: 80 07 80                           ; Location=0x80, disk_section=7, data=0, attributes=0b10000000
B26C:    02 03                           ;   Section=02:SECTION_02_SHORT_NAME, length=0x0003
;           SHIP
B26E:       23 B8 50                     ; 

; -------------- Object OBJ_9D_THIRST_TRACKER --------------
B271: 00 81 3B                           ; Word_num=0x00 -none-, length=0x013B
B274: 00 00 80                           ; Location=0x00, disk_section=0, data=0, attributes=0b10000000
B277:    08 81 35                        ;   Section=08:SECTION_08_EVERY_TURN, length=0x0135
B27A:       0D 81 32                     ;     COM_0D_while_pass length=0x0132
B27D:          1C 01                     ;       COM_1C_set_var_object(obj=OBJ_01_PLAYER)
B27F:          1D 02                     ;       COM_1D_attack_var(points=2)
B281:          0B 81 2B 22               ;       COM_0B_switch length=0x012B, function=COM_22_is_less_equal_health(points)
B285:             01                     ;         COM_22_is_less_equal_health(points=1)
B286:             01                     ;         ELSE goto=0xB288
B287:                1A                  ;           COM_1A_set_var_to_first_noun()
B288:             03                     ;         COM_22_is_less_equal_health(points=3)
B289:             33                     ;         ELSE goto=0xB2BD
B28A:                1F 31               ;           COM_1F_print2 length=0x0031
B28C:                   C7 DE E1 14 FB 8C 17 A7 FB 17 53 BE 22 63 B5 49 ; 
B29C:                   91 BE 1B 9C 43 79 C7 DE 9B 15 5B CA A3 48 F3 17 ; 
B2AC:                   F4 BD 04 EE 8E 62 23 62 F3 5B 4B 99 73 7B 09 9A ; 
B2BC:                   21               ; 
;
;                       YOU COLLAPSE WITH EXHAUSTION. IF YOU HAVE ANY WATER, BETTER
;                       DRINK IT NOW!
;
B2BD:             08                     ;         COM_22_is_less_equal_health(points=8)
B2BE:             01                     ;         ELSE goto=0xB2C0
B2BF:                1A                  ;           COM_1A_set_var_to_first_noun()
B2C0:             0A                     ;         COM_22_is_less_equal_health(points=10)
B2C1:             22                     ;         ELSE goto=0xB2E4
B2C2:                1F 20               ;           COM_1F_print2 length=0x0020
B2C4:                   C7 DE D3 14 90 96 F3 A0 A7 85 09 A3 50 9F D9 6A ; 
B2D4:                   82 7B 36 A1 61 17 1B 92 6E B1 28 79 61 17 01 A0 ; 
;
;                       YOU CAN NOT KEEP GOING WITHOUT SOME RELIEF SOON!
;
B2E4:             12                     ;         COM_22_is_less_equal_health(points=18)
B2E5:             01                     ;         ELSE goto=0xB2E7
B2E6:                1A                  ;           COM_1A_set_var_to_first_noun()
B2E7:             14                     ;         COM_22_is_less_equal_health(points=20)
B2E8:             0C                     ;         ELSE goto=0xB2F5
B2E9:                1F 0A               ;           COM_1F_print2 length=0x000A
B2EB:                   45 6E 0B 71 DB 22 94 BE F1 5F ; 
;
;                       GOSH I'M TIRED!
;
B2F5:             1C                     ;         COM_22_is_less_equal_health(points=28)
B2F6:             01                     ;         ELSE goto=0xB2F8
B2F7:                1A                  ;           COM_1A_set_var_to_first_noun()
B2F8:             1E                     ;         COM_22_is_less_equal_health(points=30)
B2F9:             1C                     ;         ELSE goto=0xB316
B2FA:                1F 1A               ;           COM_1F_print2 length=0x001A
B2FC:                   C7 DE D3 14 E6 96 7B 17 9B 85 A5 94 0F 71 AF A0 ; 
B30C:                   B8 16 82 17 4B 7B E3 72 AB BB ; 
;
;                       YOU CAN'T TAKE MUCH MORE OF THIS HEAT! 
;
B316:             26                     ;         COM_22_is_less_equal_health(points=38)
B317:             01                     ;         ELSE goto=0xB319
B318:                1A                  ;           COM_1A_set_var_to_first_noun()
B319:             28                     ;         COM_22_is_less_equal_health(points=40)
B31A:             10                     ;         ELSE goto=0xB32B
B31B:                1F 0E               ;           COM_1F_print2 length=0x000E
B31D:                   0B 4F 0B EE DB 22 2B B9 63 BE A6 B3 EB DA ; 
;
;                       BOY, I'M SO THIRSTY! 
;
B32B:             30                     ;         COM_22_is_less_equal_health(points=48)
B32C:             01                     ;         ELSE goto=0xB32E
B32D:                1A                  ;           COM_1A_set_var_to_first_noun()
B32E:             32                     ;         COM_22_is_less_equal_health(points=50)
B32F:             1E                     ;         ELSE goto=0xB34E
B330:                1F 1C               ;           COM_1F_print2 length=0x001C
B332:                   4A 77 5F A0 51 18 44 C2 07 B3 2E 6D 49 16 0B C0 ; 
B342:                   C3 9E 01 68 03 58 33 98 16 D0 21 62 ; 
;
;                       I HOPE YOU BROUGHT LOTS OF FOOD AND WATER!
;
B34E:             3A                     ;         COM_22_is_less_equal_health(points=58)
B34F:             01                     ;         ELSE goto=0xB351
B350:                1A                  ;           COM_1A_set_var_to_first_noun()
B351:             3C                     ;         COM_22_is_less_equal_health(points=60)
B352:             34                     ;         ELSE goto=0xB387
B353:                1F 32               ;           COM_1F_print2 length=0x0032
B355:                   C7 DE D3 14 94 96 8E 5F FB 8E 67 66 16 8A DB 72 ; 
B365:                   E3 72 11 BC 96 64 DB 72 30 BA BF 14 D3 B2 AB 98 ; 
B375:                   89 5B 91 96 9B 96 1B A1 83 7A 63 BE C6 B5 57 62 ; 
B385:                   B1 B3            ; 
;
;                       YOU CAN REALLY FEEL THE HEAT OF THE SUN BURNING DOWN ON YOU
;                       IN THIS DESERT!
;
B387:             41                     ;         COM_22_is_less_equal_health(points=65)
B388:             01                     ;         ELSE goto=0xB38A
B389:                1A                  ;           COM_1A_set_var_to_first_noun()
B38A:             43                     ;         COM_22_is_less_equal_health(points=67)
B38B:             20                     ;         ELSE goto=0xB3AC
B38C:                1F 1E               ;           COM_1F_print2 length=0x001E
B38E:                   0B 4F 16 EE 95 73 FF 14 B4 B7 0B BC C9 B5 18 A0 ; 
B39E:                   44 45 56 5E 29 A1 16 71 C5 9C 05 B3 6B B5 ; 
;
;                       BOY, THIS DESERT IS GONNA BE TOUGH TO CROSS! 
;
B3AC:             FF                     ;         COM_22_is_less_equal_health(points=255)
B3AD:             01                     ;         ELSE goto=0xB3AF
B3AE:                1A                  ;           COM_1A_set_var_to_first_noun()










; ?? Is CA:DIE_ENERGY_BEAM ever used?

SubroutineCommands:
B3AF: 00 89 BC  ; List_ID=0x00, length=0x09BC

; -------------- Routine FN_81_PRINT_DOOR_HERE
;
B3B2: 81 10                              ; Routine Number: 0x81, Length: 0x0010
B3B4:       04 0E                        ;     COM_04_print_command length=0x000E
B3B6:          5F BE 5B B1 4B 7B 46 45 44 A0 9F 15 7F B1 ; 
;
;              THERE IS A DOOR HERE.
;

; -------------- Routine FN_80_PRINT_SHOTGUN_HERE
;
B3C4: 80 12                              ; Routine Number: 0x80, Length: 0x0012
B3C6:       04 10                        ;     COM_04_print_command length=0x0010
B3C8:          5F BE 5B B1 4B 7B 55 45 86 74 30 6F 9F 15 7F B1 ; 
;
;              THERE IS A SHOTGUN HERE.
;

; -------------- Routine FN_8B_PRINT_PERIOD
;
B3D8: 8B 04                              ; Routine Number: 0x8B, Length: 0x0004
B3DA:       04 02                        ;     COM_04_print_command length=0x0002
B3DC:          3B F4                     ; 
;
;              .  
;

; -------------- Routine FN_AB_PRINT_STILL_IN_DESERT
;
B3DE: AB 15                              ; Routine Number: 0xAB, Length: 0x0015
B3E0:       04 13                        ;     COM_04_print_command length=0x0013
B3E2:          C7 DE 94 14 55 5E 8E BE 0B 8A 96 96 DB 72 F5 59 ; 
B3F2:          3E 62 2E                  ; 
;
;              YOU ARE STILL IN THE DESERT.
;

; -------------- Routine FN_95_PRINT_TRAIL_MEANDERS
;
B3F5: 95 23                              ; Routine Number: 0x95, Length: 0x0023
B3F7:       04 21                        ;     COM_04_print_command length=0x0021
B3F9:          55 45 8E 91 16 8A CB B0 0F 8A 90 5F F4 59 C8 B5 ; 
B409:          FF B2 82 17 47 5E 66 49 89 17 82 17 59 5E 66 62 ; 
B419:          2E                        ; 
;
;              A SMALL TRAIL MEANDERS FROM THE EAST TO THE WEST.
;

; -------------- Routine FN_96_PRINT_VAST_CANYON
;
B41A: 96 1E                              ; Routine Number: 0x96, Length: 0x001E
B41C:       04 1C                        ;     COM_04_print_command length=0x001C
B41E:          58 45 66 49 CF 15 55 A4 04 B7 DB 8B 10 53 C0 DE ; 
B42E:          C2 16 9D 61 AF 14 04 68 5B 5E 3F A1 ; 
;
;              A VAST IMPASSABLE CANYON OPENS BEFORE YOU.
;

; -------------- Routine FN_97_PRINT_CERTAIN_DEATH
;
B43A: 97 1D                              ; Routine Number: 0x97, Length: 0x001D
B43C:       04 1B                        ;     COM_04_print_command length=0x001B
B43E:          6B BF 2B 6E 5B BE 19 BC 3B 4A 47 D2 B3 8B 23 92 ; 
B44E:          85 96 3E 62 D0 47 FF 14 82 49 21 ; 
;
;              TO GO THAT WAY WOULD MEAN CERTAIN DEATH!
;

; -------------- Routine FN_99_DIE_CANYON_PLUNGE
;
B459: 99 50                              ; Routine Number: 0x99, Length: 0x0050
B45B:       0D 4E                        ;     COM_0D_while_pass length=0x004E
B45D:          04 46                     ;       COM_04_print_command length=0x0046
B45F:             83 46 94 46 7C B3 7C B3 F9 6C 22 6D 62 73 C3 06 ; 
B46F:             3C 49 FA 6C AB 70 94 14 BA B1 AB 70 5F BE D3 14 ; 
B47F:             91 9B 99 96 46 48 C7 B5 29 54 51 18 23 C6 64 B7 ; 
B48F:             8F 5F 95 14 51 18 52 C2 70 8E 9B 6C 6B BF C7 DE ; 
B49F:             86 AF 96 5F AB 70      ; 
;
;                 AAAAARRRRRRRGGGGHHHHH! AARRGGHH!  ARRGHH! THE CANYON WALLS
;                 ECHO YOUR SCREAM AS YOU PLUNGE TO YOUR DEATH!
;
B4A5:          20 01                     ;       COM_20_is_active_this(obj=OBJ_01_PLAYER)
B4A7:          1C 01                     ;       COM_1C_set_var_object(obj=OBJ_01_PLAYER)
B4A9:          1D 64                     ;       COM_1D_attack_var(points=100)

; -------------- Routine FN_9A_PRINT_CANYON_PREVENTS
;
B4AB: 9A 31                              ; Routine Number: 0x9A, Length: 0x0031
B4AD:       04 2F                        ;     COM_04_print_command length=0x002F
B4AF:          5F BE D3 14 91 9B 99 96 46 48 D4 B5 57 7B 84 14 ; 
B4BF:          4F A1 51 18 52 C2 78 B1 9E 61 91 7A 71 16 6F CA ; 
B4CF:          9E 61 D0 15 82 17 4B 7B 94 5A E6 5F C0 7A 2E ; 
;
;              THE CANYON WALLS RISE ABOVE YOU PREVENTING MOVEMENT IN THIS
;              DIRECTION.
;

; -------------- Routine FN_98_PRINT_LAKE
;
B4DE: 98 28                              ; Routine Number: 0x98, Length: 0x0028
B4E0:       04 26                        ;     COM_04_print_command length=0x0026
B4E2:          6B BF 5F BE 23 15 F3 B9 C7 DE D3 14 95 96 1B 60 ; 
B4F2:          1B D1 03 BC 9F A6 3D 49 89 17 AF 14 7B 14 54 8B ; 
B502:          9B 6C 4D 8B DB 63         ; 
;
;              TO THE EAST YOU CAN SEE WHAT APPEARS TO BE A LARGE LAKE. 
;

; -------------- Routine FN_9B_PRINT_EMPTY_HIGHWAY
;
B508: 9B 1C                              ; Routine Number: 0x9B, Length: 0x001C
B50A:       04 1A                        ;     COM_04_print_command length=0x001A
B50C:          83 48 72 61 FB C0 89 73 B3 75 56 DB D8 B0 4D 61 ; 
B51C:          23 15 F3 B9 8E 48 F7 17 17 BA ; 
;
;              AN EMPTY HIGHWAY TRAVELS EAST AND WEST.
;

; -------------- Routine FN_8D_PRINT_OBJECT_IS_CLOSED
;
B526: 8D 0E                              ; Routine Number: 0x8D, Length: 0x000E
B528:       0D 0C                        ;     COM_0D_while_pass length=0x000C
B52A:          2E 20                     ;       UNKNOWN2E, Value: 0x20
B52C:          AA                        ;       FN_AA_PRINT_THE_var
B52D:          04 07                     ;       COM_04_print_command length=0x0007
B52F:             4B 7B C9 54 A6 B7 2E   ; 
;
;                 IS CLOSED.
;

; -------------- Routine FN_C7_??
;
B536: C7 0E                              ; Routine Number: 0xC7, Length: 0x000E
B538:       0D 0C                        ;     COM_0D_while_pass length=0x000C
B53A:          2E 20                     ;       UNKNOWN2E, Value: 0x20
B53C:          AA                        ;       FN_AA_PRINT_THE_var
B53D:          04 07                     ;       COM_04_print_command length=0x0007
B53F:             4B 7B 04 B2 48 C5 2E   ; 
;
;                 IS RIBULN.
;

; -------------- Routine FN_8F_TRY_TO_GET_OBJECT
;
B546: 8F 80 94                           ; Routine Number: 0x8F, Length: 0x0094
B549:       0D 80 91                     ;     COM_0D_while_pass length=0x0091
B54C:          0E 80 8D                  ;       COM_0E_while_fail length=0x008D
B54F:             14                     ;         COM_14_execute_and_reverse_status next command
B550:             BF                     ;         FN_BF_??
B551:             0D 23                  ;         COM_0D_while_pass length=0x0023
B553:                2E 10               ;           UNKNOWN2E, Value: 0x10
B555:                AA                  ;           FN_AA_PRINT_THE_var
B556:                04 1E               ;           COM_04_print_command length=0x001E
B558:                   C3 B8 0B A7 6C BE 29 A1 1B 71 34 A1 53 15 B7 98 ; 
B568:                   AE B3 3F 16 D3 49 AB 98 5F BE 59 90 97 62 ; 
;
;                       SLIPS THROUGH YOUR FINGERS, LEAVING THEM WET.
;
B576:             0D 1A                  ;         COM_0D_while_pass length=0x001A
B578:                15 10               ;           COM_15_check_var(value=0x10)
B57A:                04 16               ;           COM_04_print_command length=0x0016
B57C:                   46 77 05 A0 16 BC 90 73 CA 83 59 5E 46 7A E1 14 ; 
B58C:                   5F A0 D6 B0 DB 63 ; 
;
;                       I DON'T THINK HE WILL COOPERATE. 
;
B592:             0D 22                  ;         COM_0D_while_pass length=0x0022
B594:                14                  ;           COM_14_execute_and_reverse_status next command
B595:                15 20               ;           COM_15_check_var(value=0x20)
B597:                14                  ;           COM_14_execute_and_reverse_status next command
B598:                2D 5C               ;           UNKNOWN2D, Value: 0x5C
B59A:                04 18               ;           COM_04_print_command length=0x0018
B59C:                   C7 DE 94 14 53 5E D6 C4 4B 5E 13 98 44 A4 DB 8B ; 
B5AC:                   C3 9E 6F B1 53 A1 AB 98 ; 
;
;                       YOU ARE QUITE INCAPABLE OF REMOVING 
;
B5B4:                AA                  ;           FN_AA_PRINT_THE_var
B5B5:                8B                  ;           FN_8B_PRINT_PERIOD
B5B6:             18                     ;         COM_18_is_var_owned_by_active()
B5B7:             0D 18                  ;         COM_0D_while_pass length=0x0018
B5B9:                0F                  ;           UNKNOWN0F
B5BA:                14                  ;           COM_14_execute_and_reverse_status next command
B5BB:                39                  ;           UNKNOWN39
B5BC:                04 12               ;           COM_04_print_command length=0x0012
B5BE:                   C7 DE D3 14 E6 96 D3 14 83 B3 82 17 73 49 A5 94 ; 
B5CE:                   9B 76            ; 
;
;                       YOU CAN'T CARRY THAT MUCH. 
;
B5D0:                10                  ;           COM_10_drop_var()
B5D1:             0D 08                  ;         COM_0D_while_pass length=0x0008
B5D3:                0F                  ;           UNKNOWN0F
B5D4:                AA                  ;           FN_AA_PRINT_THE_var
B5D5:                04 04               ;           COM_04_print_command length=0x0004
B5D7:                   4D BD A7 61      ; 
;
;                       TAKEN.
;
B5DB:             C1                     ;         FN_C1_PRINT_CANT_REACH_var
B5DC:          18                        ;       COM_18_is_var_owned_by_active()

; -------------- Routine FN_A2_PRINT_ALREADY_HAVE_THE_var
;
B5DD: A2 13                              ; Routine Number: 0xA2, Length: 0x0013
B5DF:       0D 11                        ;     COM_0D_while_pass length=0x0011
B5E1:          1A                        ;       COM_1A_set_var_to_first_noun()
B5E2:          18                        ;       COM_18_is_var_owned_by_active()
B5E3:          04 0B                     ;       COM_04_print_command length=0x000B
B5E5:             C7 DE 8E 14 63 B1 FB 5C 58 72 45 ; 
;
;                 YOU ALREADY HAVE
;
B5F0:          AA                        ;       FN_AA_PRINT_THE_var
B5F1:          8B                        ;       FN_8B_PRINT_PERIOD

; -------------- Routine FN_90_PRINT_ERROR_CLIMB_ENTER
;
B5F2: 90 09                              ; Routine Number: 0x90, Length: 0x0009
B5F4:       0B 07 0A                     ;     COM_0B_switch length=0x0007, function=COM_0A_is_input_phrase(phrase_num)
B5F7:          36                        ;       COM_0A_is_input_phrase("ENTER * * *")
B5F8:          01                        ;       ELSE goto=0xB5FA
B5F9:             91                     ;         FN_91_PRINT_USE_DIRECTIONS
B5FA:          37                        ;       COM_0A_is_input_phrase("CLIMB * OUT *")
B5FB:          01                        ;       ELSE goto=0xB5FD
B5FC:             91                     ;         FN_91_PRINT_USE_DIRECTIONS

; -------------- Routine FN_91_PRINT_USE_DIRECTIONS
;
B5FD: 91 19                              ; Routine Number: 0x91, Length: 0x0019
B5FF:       1F 17                        ;     COM_1F_print2 length=0x0017
B601:          FF A5 57 49 B5 17 46 5E 2F 7B 03 56 1D A0 A6 16 ; 
B611:          3F BB 11 EE 99 AF 2E      ; 
;
;              PLEASE USE DIRECTIONS N,S,E, OR W.
;

; -------------- Routine FN_92_PRINT_TRIED_BUT_COULDNT
;
B618: 92 1F                              ; Routine Number: 0x92, Length: 0x001F
B61A:       0D 1D                        ;     COM_0D_while_pass length=0x001D
B61C:          1A                        ;       COM_1A_set_var_to_first_noun()
B61D:          14                        ;       COM_14_execute_and_reverse_status next command
B61E:          15 08                     ;       COM_15_check_var(value=0x08)
B620:          04 17                     ;       COM_04_print_command length=0x0017
B622:             C7 DE 8C 17 26 79 04 EE 73 C6 C7 DE E1 14 3E C5 ; 
B632:             E6 96 09 15 D6 15 2E   ; 
;
;                 YOU TRIED, BUT YOU COULDN'T DO IT.
;

; -------------- Routine FN_94_INIT_GAME
;
B639: 94 06                              ; Routine Number: 0x94, Length: 0x0006
B63B:       0D 04                        ;     COM_0D_while_pass length=0x0004
B63D:          30 80                     ;       COM_30_set_current_room(room=RM_1_HIGHWAY_WEST)
B63F:          2F 01                     ;       COM_2F_load_section_from_disk(section=1)

; -------------- Routine FN_A3_PRINT_WELCOME_MESSAGE
;
B641: A3 36                              ; Routine Number: 0xA3, Length: 0x0036
B643:       0D 34                        ;     COM_0D_while_pass length=0x0034
B645:          3A                        ;       COM_3A_clear_screen()
B646:          2C 01                     ;       COM_2C_set_active(obj=OBJ_01_PLAYER)
B648:          30 80                     ;       COM_30_set_current_room(room=RM_1_HIGHWAY_WEST)
B64A:          17 01 80                  ;       COM_17_move_to(obj=OBJ_01_PLAYER, destination=RM_1_HIGHWAY_WEST)
B64D:          1F 1A                     ;       COM_1F_print2 length=0x001A
B64F:             DF 2C DF 2C DF 2C DF 2C DF 2C 5A 2C 99 61 BE B5 ; 
B65F:             76 26 76 26 76 26 76 26 76 26 ; 
;
;                 >>>>>>>>>>>>>>>> XENOS <<<<<<<<<<<<<<<<
;
B669:          25                        ;       COM_25_print_linefeed()
B66A:          1F 0C                     ;       COM_1F_print2 length=0x000C
B66C:             0C BA 91 48 46 62 AF 14 14 D0 EB 5D ; 
;
;                 STRANGER, BEWARE! 
;
B678:          25                        ;       COM_25_print_linefeed()

; -------------- Routine FN_A5_VERIFY_OPEN
;
B679: A5 12                              ; Routine Number: 0xA5, Length: 0x0012
B67B:       0D 10                        ;     COM_0D_while_pass length=0x0010
B67D:          14                        ;       COM_14_execute_and_reverse_status next command
B67E:          2E 20                     ;       UNKNOWN2E, Value: 0x20
B680:          A8                        ;       FN_A8_PRINT_noun1
B681:          04 0A                     ;       COM_04_print_command length=0x000A
B683:             4B 7B 06 9A DE 14 D7 A0 9B 5D ; 
;
;                 IS NOT CLOSED. 
;

; -------------- Routine FN_A6_ATTEMPT_TO_OPEN
;
B68D: A6 26                              ; Routine Number: 0xA6, Length: 0x0026
B68F:       0E 24                        ;     COM_0E_while_fail length=0x0024
B691:          0D 0D                     ;       COM_0D_while_pass length=0x000D
B693:             29                     ;         COM_29_print_open_var()
B694:             A8                     ;         FN_A8_PRINT_noun1
B695:             04 08                  ;         COM_04_print_command length=0x0008
B697:                4B 7B 09 9A C2 16 A7 61 ; 
;
;                    IS NOW OPEN.
;
B69F:             0C                     ;         COM_0C_fail()
B6A0:          0D 11                     ;       COM_0D_while_pass length=0x0011
B6A2:             1A                     ;         COM_1A_set_var_to_first_noun()
B6A3:             15 02                  ;         COM_15_check_var(value=0x02)
B6A5:             14                     ;         COM_14_execute_and_reverse_status next command
B6A6:             2E 80                  ;         UNKNOWN2E, Value: 0x80
B6A8:             14                     ;         COM_14_execute_and_reverse_status next command
B6A9:             33                     ;         UNKNOWN33
B6AA:             A8                     ;         FN_A8_PRINT_noun1
B6AB:             04 06                  ;         COM_04_print_command length=0x0006
B6AD:                4B 7B 72 61 1F C1   ; 
;
;                    IS EMPTY.
;
B6B3:          14                        ;       COM_14_execute_and_reverse_status next command
B6B4:          0C                        ;       COM_0C_fail()

; -------------- Routine FN_A8_PRINT_noun1
;
B6B5: A8 0C                              ; Routine Number: 0xA8, Length: 0x000C
B6B7:       0D 0A                        ;     COM_0D_while_pass length=0x000A
B6B9:          1A                        ;       COM_1A_set_var_to_first_noun()
B6BA:          0E 06                     ;       COM_0E_while_fail length=0x0006
B6BC:             15 10                  ;         COM_15_check_var(value=0x10)
B6BE:             1F 02                  ;         COM_1F_print2 length=0x0002
B6C0:                5F BE               ; 
;
;                    THE
;
B6C2:          11                        ;       COM_11_print_first_noun()

; -------------- Routine FN_A9_PRINT_noun2
;
B6C3: A9 0C                              ; Routine Number: 0xA9, Length: 0x000C
B6C5:       0D 0A                        ;     COM_0D_while_pass length=0x000A
B6C7:          1B                        ;       COM_1B_set_var_to_second_noun()
B6C8:          0E 06                     ;       COM_0E_while_fail length=0x0006
B6CA:             15 10                  ;         COM_15_check_var(value=0x10)
B6CC:             1F 02                  ;         COM_1F_print2 length=0x0002
B6CE:                5F BE               ; 
;
;                    THE
;
B6D0:          12                        ;       COM_12_print_second_noun()

; -------------- Routine FN_AA_PRINT_THE_var
;
B6D1: AA 0B                              ; Routine Number: 0xAA, Length: 0x000B
B6D3:       0D 09                        ;     COM_0D_while_pass length=0x0009
B6D5:          0E 06                     ;       COM_0E_while_fail length=0x0006
B6D7:             15 10                  ;         COM_15_check_var(value=0x10)
B6D9:             1F 02                  ;         COM_1F_print2 length=0x0002
B6DB:                5F BE               ; 
;
;                    THE
;
B6DD:          16                        ;       COM_16_print_var()

; -------------- Routine FN_9C_??
;
B6DE: 9C 53                              ; Routine Number: 0x9C, Length: 0x0053
B6E0:       0D 51                        ;     COM_0D_while_pass length=0x0051
B6E2:          04 04                     ;       COM_04_print_command length=0x0004
B6E4:             52 86 5B B9            ; 
;
;                 KIPSPA
;
B6E8:          0E 08                     ;       COM_0E_while_fail length=0x0008
B6EA:             C3                     ;         FN_C3_PLAYER_LACKS_WISDOM
B6EB:             04 05                  ;         COM_04_print_command length=0x0005
B6ED:                D4 47 75 8D 4B      ; 
;
;                    AIRLOCK
;
B6F2:          8B                        ;       FN_8B_PRINT_PERIOD
B6F3:          04 3E                     ;       COM_04_print_command length=0x003E
B6F5:             C7 DE 94 14 4B 5E 83 96 5F 17 46 48 84 15 3B 63 ; 
B705:             01 B3 DB 95 5F BE 5B B1 4B 7B 52 45 8F 48 19 8A ; 
B715:             82 7B 91 17 C4 9C 8E C6 1D A0 11 EE 5B 98 4B 7B ; 
B725:             66 B1 90 14 11 58 5B 98 4B 7B 8F 4E DB 63 ; 
;
;                 YOU ARE IN A SMALL GREY ROOM. THERE IS A PANEL WITH TWO
;                 BUTTONS, ONE IS RED AND ONE IS BLUE.
;

; -------------- Routine FN_B0_??
;
B733: B0 5F                              ; Routine Number: 0xB0, Length: 0x005F
B735:       0D 5D                        ;     COM_0D_while_pass length=0x005D
B737:          04 04                     ;       COM_04_print_command length=0x0004
B739:             52 86 5B B9            ; 
;
;                 KIPSPA
;
B73D:          0E 08                     ;       COM_0E_while_fail length=0x0008
B73F:             C3                     ;         FN_C3_PLAYER_LACKS_WISDOM
B740:             04 05                  ;         COM_04_print_command length=0x0005
B742:                D4 47 75 8D 4B      ; 
;
;                    AIRLOCK
;
B747:          8B                        ;       FN_8B_PRINT_PERIOD
B748:          04 4A                     ;       COM_04_print_command length=0x004A
B74A:             C7 DE 94 14 4B 5E 83 96 5F 17 46 48 84 15 3B 4A ; 
B75A:             01 B3 DB 95 5F BE 5B B1 4B 7B 52 45 8F 48 19 8A ; 
B76A:             82 7B 82 17 67 B1 BF 14 49 C0 AE 9A C0 16 4B 5E ; 
B77A:             D4 B5 16 60 C0 16 4B 5E C4 B5 67 8E 03 EE 33 98 ; 
B78A:             0F A0 D5 15 47 18 09 8D 5B D4 ; 
;
;                 YOU ARE IN A SMALL GRAY ROOM. THERE IS A PANEL WITH THREE
;                 BUTTONS, ONE IS RED, ONE IS BLUE, AND ONE IS YELLOW.
;

; -------------- Routine FN_9D_??
;
B794: 9D 74                              ; Routine Number: 0x9D, Length: 0x0074
B796:       0D 72                        ;     COM_0D_while_pass length=0x0072
B798:          04 05                     ;       COM_04_print_command length=0x0005
B79A:             89 4E E2 87 41         ; 
;
;                 BLOKSPA
;
B79F:          0E 06                     ;       COM_0E_while_fail length=0x0006
B7A1:             C3                     ;         FN_C3_PLAYER_LACKS_WISDOM
B7A2:             04 03                  ;         COM_04_print_command length=0x0003
B7A4:                23 63 54            ; 
;
;                    EXIT
;
B7A7:          8B                        ;       FN_8B_PRINT_PERIOD
B7A8:          04 60                     ;       COM_04_print_command length=0x0060
B7AA:             C7 DE 94 14 4B 5E 83 96 5F 17 46 48 E7 14 05 4E ; 
B7BA:             FF 8B 82 17 2F 62 D5 15 7B 14 2E DD 89 8D BF 14 ; 
B7CA:             49 C0 91 96 96 96 DB 72 6A A0 DB A0 DB BD 0E D0 ; 
B7DA:             9B 8F 03 A0 5F BE 8F 16 23 49 0E D0 16 8A F4 72 ; 
B7EA:             4B 5E C3 B5 5F 17 46 48 63 17 94 C3 4A 5E BF 9F ; 
B7FA:             84 14 36 A1 91 17 CB 9C 1A 98 4B 62 E7 59 9B A8 ; 
;
;                 YOU ARE IN A SMALL CUBICLE. THERE IS A YELLOW BUTTON ON THE
;                 OPPOSITE WALL. ON THE NEAR WALL THERE IS A SMALL SQUARE
;                 HOLE ABOUT TWO INCHES DEEP.
;

; -------------- Routine FN_9E_??
;
B80A: 9E 03                              ; Routine Number: 0x9E, Length: 0x0003
B80C:       17 3E 00                     ;     COM_17_move_to(obj=OBJ_3E_??, destination=nowhere)

; -------------- Routine FN_9F_??
;
B80F: 9F 0A                              ; Routine Number: 0x9F, Length: 0x000A
B811:       0D 08                        ;     COM_0D_while_pass length=0x0008
B813:          0A 12                     ;       COM_0A_is_input_phrase(phrase=PULL u....... * *)
B815:          08 3F                     ;       COM_08_is_first_noun(obj=OBJ_3F_YELLOW_BUTTON)
B817:          AD                        ;       FN_AD_??
B818:          17 3E 3F                  ;       COM_17_move_to(obj=OBJ_3E_??, destination=OBJ_3F_YELLOW_BUTTON)

; -------------- Routine FN_A0_??
;
B81B: A0 0A                              ; Routine Number: 0xA0, Length: 0x000A
B81D:       0D 08                        ;     COM_0D_while_pass length=0x0008
B81F:          0A 12                     ;       COM_0A_is_input_phrase(phrase=PULL u....... * *)
B821:          08 40                     ;       COM_08_is_first_noun(obj=OBJ_40_RED_BUTTON)
B823:          AD                        ;       FN_AD_??
B824:          17 3E 40                  ;       COM_17_move_to(obj=OBJ_3E_??, destination=OBJ_40_RED_BUTTON)

; -------------- Routine FN_A1_??
;
B827: A1 0A                              ; Routine Number: 0xA1, Length: 0x000A
B829:       0D 08                        ;     COM_0D_while_pass length=0x0008
B82B:          0A 12                     ;       COM_0A_is_input_phrase(phrase=PULL u....... * *)
B82D:          08 41                     ;       COM_08_is_first_noun(obj=OBJ_41_BLUE_BUTTON)
B82F:          AD                        ;       FN_AD_??
B830:          17 3E 41                  ;       COM_17_move_to(obj=OBJ_3E_??, destination=OBJ_41_BLUE_BUTTON)

; -------------- Routine FN_AC_??
;
B833: AC 0A                              ; Routine Number: 0xAC, Length: 0x000A
B835:       0D 08                        ;     COM_0D_while_pass length=0x0008
B837:          0A 12                     ;       COM_0A_is_input_phrase(phrase=PULL u....... * *)
B839:          08 42                     ;       COM_08_is_first_noun(obj=OBJ_42_ORANGE_BUTTON)
B83B:          AD                        ;       FN_AD_??
B83C:          17 3E 42                  ;       COM_17_move_to(obj=OBJ_3E_??, destination=OBJ_42_ORANGE_BUTTON)

; -------------- Routine FN_AD_??
;
B83F: AD 54                              ; Routine Number: 0xAD, Length: 0x0054
B841:       0E 52                        ;     COM_0E_while_fail length=0x0052
B843:          0D 3B                     ;       COM_0D_while_pass length=0x003B
B845:             14                     ;         COM_14_execute_and_reverse_status next command
B846:             37                     ;         UNKNOWN37
B847:             03 00 3E               ;         COM_03_is_located(owner=nowhere, obj=OBJ_3E_??)
B84A:             04 34                  ;         COM_04_print_command length=0x0034
B84C:                44 45 45 8B D1 83 CE C9 92 14 E3 A4 8B B3 03 A0 ; 
B85C:                5F BE F3 17 F3 8C 8E 48 3A 15 50 A4 0B 5C 6B BF ; 
B86C:                47 48 E6 A0 63 16 95 96 6F 7C 12 58 02 B3 BE A0 ; 
B87C:                C0 7A 5B BB         ; 
;
;                    A BLACK OVAL APPEARS ON THE WALL AND EXPANDS TO ALMOST MAN
;                    SIZED PROPORTIONS.
;
B880:          0D 0F                     ;       COM_0D_while_pass length=0x000F
B882:             14                     ;         COM_14_execute_and_reverse_status next command
B883:             37                     ;         UNKNOWN37
B884:             04 0B                  ;         COM_04_print_command length=0x000B
B886:                06 9A 90 73 CA 6A EA 48 9D 61 2E ; 
;
;                    NOTHING HAPPENS.
;
B891:          0D 02                     ;       COM_0D_while_pass length=0x0002
B893:             1A                     ;         COM_1A_set_var_to_first_noun()
B894:             C1                     ;         FN_C1_PRINT_CANT_REACH_var

; -------------- Routine FN_AE_??
;
B895: AE 21                              ; Routine Number: 0xAE, Length: 0x0021
B897:       0D 1F                        ;     COM_0D_while_pass length=0x001F
B899:          03 00 3E                  ;       COM_03_is_located(owner=nowhere, obj=OBJ_3E_??)
B89C:          04 1A                     ;       COM_04_print_command length=0x001A
B89E:             C7 DE FB 17 F3 8C 58 72 56 5E D2 9C 5A C6 7B 14 ; 
B8AE:             F6 4F 80 BF 06 EE 6F C5 EB DA ; 
;
;                 YOU WILL HAVE TO PUSH A BUTTON, DUMMY! 
;

; -------------- Routine FN_AF_PRINT_I_SEE_NO_noun1_HERE
;
B8B8: AF 13                              ; Routine Number: 0xAF, Length: 0x0013
B8BA:       0D 11                        ;     COM_0D_while_pass length=0x0011
B8BC:          0A 12                     ;       COM_0A_is_input_phrase(phrase=PULL u....... * *)
B8BE:          04 06                     ;       COM_04_print_command length=0x0006
B8C0:             55 77 1B 60 EB 99      ; 
;
;                 I SEE NO 
;
B8C6:          11                        ;       COM_11_print_first_noun()
B8C7:          04 04                     ;       COM_04_print_command length=0x0004
B8C9:             F4 72 DB 63            ; 
;
;                 HERE. 
;

; -------------- Routine FN_B1_PRINT_var_CONTAINS
;
B8CD: B1 0E                              ; Routine Number: 0xB1, Length: 0x000E
B8CF:       0D 0C                        ;     COM_0D_while_pass length=0x000C
B8D1:          04 01                     ;       COM_04_print_command length=0x0001
B8D3:             20                     ; 
;
;                  
;
B8D4:          AA                        ;       FN_AA_PRINT_THE_var
B8D5:          04 06                     ;       COM_04_print_command length=0x0006
B8D7:             40 55 4B BD 8B 9A      ; 
;
;                 CONTAINS 
;

; -------------- Routine FN_B2_PRINT_ON_var_CAN_BE_SEEN
;
B8DD: B2 11                              ; Routine Number: 0xB2, Length: 0x0011
B8DF:       0D 0F                        ;     COM_0D_while_pass length=0x000F
B8E1:          04 02                     ;       COM_04_print_command length=0x0002
B8E3:             C0 16                  ; 
;
;                  ON
;
B8E5:          AA                        ;       FN_AA_PRINT_THE_var
B8E6:          04 08                     ;       COM_04_print_command length=0x0008
B8E8:             10 53 AF 14 57 17 83 61 ; 
;
;                 CAN BE SEEN 
;

; -------------- Routine FN_B3_PRINT_DISK_ERROR
;
B8F0: B3 0C                              ; Routine Number: 0xB3, Length: 0x000C
B8F2:       0D 0A                        ;     COM_0D_while_pass length=0x000A
B8F4:          1F 07                     ;       COM_1F_print2 length=0x0007
B8F6:             95 5A C7 83 79 B3 52   ; 
;
;                 DISK ERROR
;
B8FD:          25                        ;       COM_25_print_linefeed()

; -------------- Routine FN_B4_PRINT_AND
;
B8FE: B4 04                              ; Routine Number: 0xB4, Length: 0x0004
B900:       04 02                        ;     COM_04_print_command length=0x0002
B902:          8E 48                     ; 
;
;              AND
;

; -------------- Routine FN_B5_PRINT_BY_YOUR_COMMAND
;
B904: B5 0D                              ; Routine Number: 0xB5, Length: 0x000D
B906:       04 0B                        ;     COM_04_print_command length=0x000B
B908:          7B 50 C7 DE 85 AF EF 9F 8E 48 2E ; 
;
;              BY YOUR COMMAND.
;

; -------------- Routine FN_B6_PRINT_TWO_SAME_SPACE
;
B913: B6 3C                              ; Routine Number: 0xB6, Length: 0x003C
B915:       04 3A                        ;     COM_04_print_command length=0x003A
B917:          73 7B 4B 7B 73 A5 45 B8 46 48 4B DB E9 93 DB B9 ; 
B927:          7F 4E 59 15 96 AF 2B D2 34 9E E6 5F D6 B5 D1 9C ; 
B937:          67 53 FB A7 5F BE 53 17 1B 92 5B B9 9B 53 73 49 ; 
B947:          5F BE 53 17 1B 92 8F BE DB 63 ; 
;
;              IT IS PHYSICALLY IMPOSSIBLE FOR TWO OBJECTS TO OCCUPY THE
;              SAME SPACE AT THE SAME TIME.
;

; -------------- Routine FN_B7_PRINT_HAVE_TO_OPEN_var
;
B951: B7 16                              ; Routine Number: 0xB7, Length: 0x0016
B953:       0D 14                        ;     COM_0D_while_pass length=0x0014
B955:          2E 20                     ;       UNKNOWN2E, Value: 0x20
B957:          04 0E                     ;       COM_04_print_command length=0x000E
B959:             C7 DE FB 17 F3 8C 58 72 56 5E D1 9C F0 A4 ; 
;
;                 YOU WILL HAVE TO OPEN
;
B967:          AA                        ;       FN_AA_PRINT_THE_var
B968:          8B                        ;       FN_8B_PRINT_PERIOD

; -------------- Routine FN_B8_PRINT_GARBAGE_GAMES
;
B969: B8 24                              ; Routine Number: 0xB8, Length: 0x0024
B96B:       04 22                        ;     COM_04_print_command length=0x0022
B96D:          C7 DE 20 16 6B A1 C7 DE D3 14 E6 96 09 15 82 17 ; 
B97D:          73 49 14 6C C9 4C 4B 5E 96 96 F5 72 49 5E 67 48 ; 
B98D:          6B B5                     ; 
;
;              YOU KNOW YOU CAN'T DO THAT GARBAGE IN THESE GAMES! 
;

; -------------- Routine FN_B9_PRINT_JUKEBOX
;
B98F: B9 2E                              ; Routine Number: 0xB9, Length: 0x002E
B991:       04 2C                        ;     COM_04_print_command length=0x002C
B993:          83 7A 5F BE E1 14 CF B2 95 AF 50 BD 0B 5C 83 48 ; 
B9A3:          8D 48 30 79 14 BC 03 47 C3 9C 07 4F 16 BC DB 72 ; 
B9B3:          5C B8 51 5E 83 64 FF 15 A4 85 B7 A1 ; 
;
;              IN THE CORNER STANDS AN ANCIENT RADIO ABOUT THE SIZE OF A
;              JUKEBOX.
;

; -------------- Routine FN_BA_??
;
B9BF: BA 65                              ; Routine Number: 0xBA, Length: 0x0065
B9C1:       0D 63                        ;     COM_0D_while_pass length=0x0063
B9C3:          0E 04                     ;       COM_0E_while_fail length=0x0004
B9C5:             0A 3A                  ;         COM_0A_is_input_phrase(phrase=OPEN u....... WITH u.......)
B9C7:             0A 42                  ;         COM_0A_is_input_phrase(phrase=UNLOCK u....... WITH u.......)
B9C9:          0E 5B                     ;       COM_0E_while_fail length=0x005B
B9CB:             0D 28                  ;         COM_0D_while_pass length=0x0028
B9CD:                09 24               ;           COM_09_compare_to_second_noun(obj=OBJ_24_CROWBAR)
B9CF:                1A                  ;           COM_1A_set_var_to_first_noun()
B9D0:                14                  ;           COM_14_execute_and_reverse_status next command
B9D1:                2E 40               ;           UNKNOWN2E, Value: 0x40
B9D3:                04 1A               ;           COM_04_print_command length=0x001A
B9D5:                   EB 99 67 98 16 58 C4 9C 58 5E BE 7A 9E 61 0B EE ; 
B9E5:                   0B C0 06 9A 49 16 97 54 AB 57 ; 
;
;                       NO NEED TO BE VIOLENT, ITS NOT LOCKED! 
;
B9EF:                0E 04               ;           COM_0E_while_fail length=0x0004
B9F1:                   14               ;             COM_14_execute_and_reverse_status next command
B9F2:                   2E 20            ;             UNKNOWN2E, Value: 0x20
B9F4:                   A6               ;             FN_A6_ATTEMPT_TO_OPEN
B9F5:             0D 1C                  ;         COM_0D_while_pass length=0x001C
B9F7:                09 24               ;           COM_09_compare_to_second_noun(obj=OBJ_24_CROWBAR)
B9F9:                04 18               ;           COM_04_print_command length=0x0018
B9FB:                   C7 DE 96 AF 3E A0 D5 15 89 17 D5 9C 8E 91 08 8A ; 
BA0B:                   A3 A0 5F BE F9 15 1B 51 ; 
;
;                       YOUR TOOL IS TOO SMALL FOR THE JOB. 
;
BA13:             0D 11                  ;         COM_0D_while_pass length=0x0011
BA15:                A9                  ;           FN_A9_PRINT_noun2
BA16:                04 0E               ;           COM_04_print_command length=0x000E
BA18:                   77 5B 05 B9 15 BC 2F 60 89 17 01 18 6F B2 ; 
;
;                       DOESN'T SEEM TO WORK.
;

; -------------- Routine FN_BB_PRINT_LOOK_IN_AT
;
BA26: BB 23                              ; Routine Number: 0xBB, Length: 0x0023
BA28:       0D 21                        ;     COM_0D_while_pass length=0x0021
BA2A:          0E 04                     ;       COM_0E_while_fail length=0x0004
BA2C:             0A 10                  ;         COM_0A_is_input_phrase(phrase=LOOK * IN ......O.)
BA2E:             0A 0B                  ;         COM_0A_is_input_phrase(phrase=LOOK * AT u.......)
BA30:          04 19                     ;       COM_04_print_command length=0x0019
BA32:             8D 7B 89 17 C6 9C 35 49 89 17 57 17 4F 5E DA C3 ; 
BA42:             B8 16 90 14 82 DF 91 7A 2E ; 
;
;                 ITS TOO DARK TO SEE MUCH OF ANYTHING.
;

; -------------- Routine FN_BC_??
;
BA4B: BC 07                              ; Routine Number: 0xBC, Length: 0x0007
BA4D:       0D 05                        ;     COM_0D_while_pass length=0x0005
BA4F:          0A 57                     ;       COM_0A_is_input_phrase(phrase=SHOOT u....... WITH u.......)
BA51:          09 28                     ;       COM_09_compare_to_second_noun(obj=OBJ_28_SHOTGUN)
BA53:          10                        ;       COM_10_drop_var()

; -------------- Routine FN_BD_PRINT_SHAGGY_CREATURE
;
BA54: BD 42                              ; Routine Number: 0xBD, Length: 0x0042
BA56:       1F 40                        ;     COM_1F_print2 length=0x0040
BA58:          56 45 EF 74 48 5E 46 A0 7B 17 F3 8C 1B B8 0B 6D ; 
BA68:          E4 14 96 5F 2F C6 FB 17 53 BE DC B0 A3 A0 1B B8 ; 
BA78:          13 B3 BB 54 CB D2 8E 48 5E 17 CF 49 10 B2 D6 6A ; 
BA88:          36 60 15 71 50 BD 0B 5C 68 4D AF A0 51 18 DB C7 ; 
;
;              A THREE FOOT TALL SHAGGY CREATURE WITH RAZOR SHARP CLAWS
;              AND SLAVERING TEETH STANDS BEFORE YOU.
;

; -------------- Routine FN_BE_PRINT_FORCE_FIELD
;
BA98: BE 26                              ; Routine Number: 0xBE, Length: 0x0026
BA9A:       04 24                        ;     COM_04_print_command length=0x0024
BA9C:          48 45 AD A0 48 5E 2E 79 12 58 78 B1 9E 61 DB B5 ; 
BAAC:          1B A1 79 68 49 90 50 9F D6 6A 56 72 03 15 65 B1 ; 
BABC:          91 BE 1B 9C               ; 
;
;              A FORCE FIELD PREVENTS YOU FROM GOING THAT DIRECTION. 
;

; -------------- Routine FN_BF_??
;
BAC0: BF 10                              ; Routine Number: 0xBF, Length: 0x0010
BAC2:       0E 0E                        ;     COM_0E_while_fail length=0x000E
BAC4:          36                        ;       UNKNOWN36
BAC5:          0D 0B                     ;       COM_0D_while_pass length=0x000B
BAC7:             AA                     ;         FN_AA_PRINT_THE_var
BAC8:             04 07                  ;         COM_04_print_command length=0x0007
BACA:                4B 7B C9 54 A6 B7 2E ; 
;
;                    IS CLOSED.
;
BAD1:             0C                     ;         COM_0C_fail()

; -------------- Routine FN_C0_??
;
BAD2: C0 06                              ; Routine Number: 0xC0, Length: 0x0006
BAD4:       0D 04                        ;     COM_0D_while_pass length=0x0004
BAD6:          08 00                     ;       COM_08_is_first_noun(obj=nothing)
BAD8:          09 00                     ;       COM_09_compare_to_second_noun(obj=nothing)

; -------------- Routine FN_C1_PRINT_CANT_REACH_var
;
BADA: C1 18                              ; Routine Number: 0xC1, Length: 0x0018
BADC:       0D 16                        ;     COM_0D_while_pass length=0x0016
BADE:          04 0A                     ;       COM_04_print_command length=0x000A
BAE0:             C7 DE D3 14 E6 96 2F 17 DA 46 ; 
;
;                 YOU CAN'T REACH
;
BAEA:          AA                        ;       FN_AA_PRINT_THE_var
BAEB:          04 07                     ;       COM_04_print_command length=0x0007
BAED:             79 68 4A 90 2F 62 2E   ; 
;
;                 FROM HERE.
;

; -------------- Routine FN_C2_PRINT_CANT_BUDGE_noun1
;
BAF4: C2 10                              ; Routine Number: 0xC2, Length: 0x0010
BAF6:       0D 0E                        ;     COM_0D_while_pass length=0x000E
BAF8:          04 0A                     ;       COM_04_print_command length=0x000A
BAFA:             C7 DE D3 14 E6 96 BF 14 37 5A ; 
;
;                 YOU CAN'T BUDGE
;
BB04:          A8                        ;       FN_A8_PRINT_noun1
BB05:          8B                        ;       FN_8B_PRINT_PERIOD

; -------------- Routine FN_C3_PLAYER_LACKS_WISDOM
;
BB06: C3 04                              ; Routine Number: 0xC3, Length: 0x0004
BB08:       14                           ;     COM_14_execute_and_reverse_status next command
BB09:       03 01 80                     ;     COM_03_is_located(owner=OBJ_01_PLAYER, obj=OBJ_80_WISDOM)

; -------------- Routine FN_C4_??
;
BB0C: C4 1C                              ; Routine Number: 0xC4, Length: 0x001C
BB0E:       0E 1A                        ;     COM_0E_while_fail length=0x001A
BB10:          0A 11                     ;       COM_0A_is_input_phrase(phrase=OPEN u....... * *)
BB12:          0A 3A                     ;       COM_0A_is_input_phrase(phrase=OPEN u....... WITH u.......)
BB14:          0A 05                     ;       COM_0A_is_input_phrase(phrase=GET ..C..... * *)
BB16:          0A 43                     ;       COM_0A_is_input_phrase(phrase=GET ..C..... WITH ..C.....)
BB18:          0A 09                     ;       COM_0A_is_input_phrase(phrase=ATTACK ...P.... WITH .v......)
BB1A:          0A 27                     ;       COM_0A_is_input_phrase(phrase=KICK u....... * *)
BB1C:          0A 2D                     ;       COM_0A_is_input_phrase(phrase=PULL * UP u.......)
BB1E:          0A 12                     ;       COM_0A_is_input_phrase(phrase=PULL u....... * *)
BB20:          0A 18                     ;       COM_0A_is_input_phrase(phrase=RUB u....... * *)
BB22:          0A 0F                     ;       COM_0A_is_input_phrase(phrase=DROP ..C..... IN ......O.)
BB24:          0A 4B                     ;       COM_0A_is_input_phrase(phrase=DROP ..C..... ON .......L)
BB26:          0A 4D                     ;       COM_0A_is_input_phrase(phrase=FILL ......O. WITH u.......)
BB28:          0A 40                     ;       COM_0A_is_input_phrase(phrase=CLOSE ....A... * *)

; -------------- Routine FN_C5_??
;
BB2A: C5 28                              ; Routine Number: 0xC5, Length: 0x0028
BB2C:       0B 26 0A                     ;     COM_0B_switch length=0x0026, function=COM_0A_is_input_phrase(phrase_num)
BB2F:          36                        ;       COM_0A_is_input_phrase("ENTER * * *")
BB30:          0F                        ;       ELSE goto=0xBB40
BB31:             0D 0D                  ;         COM_0D_while_pass length=0x000D
BB33:                04 09               ;           COM_04_print_command length=0x0009
BB35:                   C7 DE AF 23 99 16 CB CE 4E ; 
;
;                       YOU'RE NOW IN
;
BB3E:                A8                  ;           FN_A8_PRINT_noun1
BB3F:                8B                  ;           FN_8B_PRINT_PERIOD
BB40:          37                        ;       COM_0A_is_input_phrase("CLIMB * OUT *")
BB41:          12                        ;       ELSE goto=0xBB54
BB42:             0D 10                  ;         COM_0D_while_pass length=0x0010
BB44:                04 0C               ;           COM_04_print_command length=0x000C
BB46:                   C7 DE AF 23 99 16 D1 CE 73 C6 C3 9E ; 
;
;                       YOU'RE NOW OUT OF 
;
BB52:                A8                  ;           FN_A8_PRINT_noun1
BB53:                8B                  ;           FN_8B_PRINT_PERIOD

; -------------- Routine FN_C6_PROMPT_FOR_DRIVE_NUMBER
;
BB54: C6 1E                              ; Routine Number: 0xC6, Length: 0x001E
BB56:       0D 1C                        ;     COM_0D_while_pass length=0x001C
BB58:          04 18                     ;       COM_04_print_command length=0x0018
BB5A:             18 B7 46 5E 5D 7B D5 15 D0 15 FA 17 DA 78 0C 15 ; 
BB6A:             CF 7B B9 13 D7 E8 C3 12 ; 
;
;                 SAVE DISK IS IN WHICH DRIVE <0-3> ? 
;
BB72:          3B                        ;       COM_3B_wait_for_key123()
BB73:          25                        ;       COM_25_print_linefeed()

; -------------- Routine FN_C8_BACK_TO_TOWN
;
BB74: C8 81 80                           ; Routine Number: 0xC8, Length: 0x0180
BB77:       0E 81 7D                     ;     COM_0E_while_fail length=0x017D
BB7A:          0D 80 8C                  ;       COM_0D_while_pass length=0x008C
BB7D:             03 01 91               ;         COM_03_is_located(owner=OBJ_01_PLAYER, obj=OBJ_91_POISON)
BB80:             04 80 82               ;         COM_04_print_command length=0x0082
BB83:                AE D0 73 8F 73 7B A7 B7 4B 94 C7 DE 63 16 DB 59 ; 
BB93:                73 7B E4 46 E5 A0 82 17 46 5E 57 62 B1 B3 A9 15 ; 
BBA3:                B8 D0 46 62 FA 17 83 61 5B BE 10 BC 66 49 45 DB ; 
BBB3:                63 B1 74 C0 4B 5E 96 96 DB 72 F5 59 3E 62 96 14 ; 
BBC3:                45 BD A6 85 51 18 B3 C7 C7 DE F7 17 5B B1 7B A6 ; 
BBD3:                40 B9 F1 5F DF 16 DB B1 0B A7 3F B9 43 5E C3 9A ; 
BBE3:                86 5B 45 5E 2E A1 0A 58 CF 49 53 17 66 CA 51 18 ; 
BBF3:                DB C7 F6 4F 0B EE 0B BC D6 B5 2B A0 56 8B 50 5E ; 
BC03:                8F A1               ; 
;
;                    WELL, IT SEEMS YOU MADE IT ACROSS THE DESERT! HOWEVER, WHEN
;                    THAT NASTY CREATURE IN THE DESERT ATTACKED YOU, YOU WERE
;                    POISONED! PERHAPS SOME ANTIDOTE COULD HAVE SAVED YOU. BUT,
;                    IT IS TOO LATE NOW.
;
BC05:             1C 01                  ;         COM_1C_set_var_object(obj=OBJ_01_PLAYER)
BC07:             1D 64                  ;         COM_1D_attack_var(points=100)
BC09:          0D 80 E9                  ;       COM_0D_while_pass length=0x00E9
BC0C:             03 00 71               ;         COM_03_is_located(owner=nowhere, obj=OBJ_71_GREEN_BUTTON_WEAPON)
BC0F:             04 80 E2               ;         COM_04_print_command length=0x00E2
BC12:                C7 DE 9B 15 5B CA 86 91 4B 5E 04 BC DD 46 89 17 ; 
BC22:                89 17 01 D2 82 17 56 5E 80 A1 C8 B5 C5 9F 9B 15 ; 
BC32:                5B CA 76 B1 38 C6 F3 5F 8E 48 82 17 3B 63 1F 54 ; 
BC42:                23 62 C7 DE 95 AF D5 C3 65 62 43 F4 B3 14 C5 6A ; 
BC52:                3F 61 6B 4F 91 BE 8B 96 D2 B5 72 B1 2F 49 03 58 ; 
BC62:                33 98 5F BE 4F 15 03 BA 16 CB 35 79 3B 16 F3 B9 ; 
BC72:                46 48 93 16 2E 6D 56 F4 DB 72 94 5F 53 BE 55 72 ; 
BC82:                AF 14 83 61 18 B7 F1 5F 8A 14 19 EE 46 61 10 EE ; 
BC92:                6B A1 C7 DE 77 16 F3 B9 76 B1 38 C6 89 17 82 17 ; 
BCA2:                46 5E BE 9F EF B3 D1 B5 9B 64 34 A1 99 16 A3 B2 ; 
BCB2:                04 8A B3 A0 AB 98 88 8C DB 63 F4 A4 52 72 33 BB ; 
BCC2:                C7 DE 82 17 95 7A 15 EE E7 9F 5B 59 90 14 02 A1 ; 
BCD2:                23 62 59 C4 FB 17 F3 8C 3F 55 43 5E 33 98 C7 DE ; 
BCE2:                D3 14 8B 96 0F 9B 03 BA 16 6C 51 5E 17 98 71 16 ; 
BCF2:                7F B1               ; 
;
;                    YOU HAVE MADE IT BACK TO TOWN! THE TOWNS FOLK HAVE RETURNED
;                    AND THEY CHEER YOUR SUCCESS. A BIG CELEBRATION IS PREPARED
;                    AND THE FESTIVITIES LAST ALL NIGHT. THE EARTH HAS BEEN
;                    SAVED! AH, WELL, NOW YOU MUST RETURN TO THE DOLDRUMS OF
;                    YOUR NORMAL BORING LIFE. PERHAPS, YOU THINK, SOMEDAY
;                    ANOTHER UFO WILL COME AND YOU CAN INVESTIGATE ONCE MORE.
;
BCF4:             24                     ;         COM_24_exit_program()
BCF5:          14                        ;       COM_14_execute_and_reverse_status next command
BCF6:          0C                        ;       COM_0C_fail()

; -------------- Routine FN_C9_PRINT_COMPLETED_PERCENT
;
BCF7: C9 23                              ; Routine Number: 0xC9, Length: 0x0023
BCF9:       0D 21                        ;     COM_0D_while_pass length=0x0021
BCFB:          1F 0C                     ;       COM_1F_print2 length=0x000C
BCFD:             C7 DE 9B 15 5B CA 3F 55 FF A5 E6 BD ; 
;
;                 YOU HAVE COMPLETED
;
BD09:          26                        ;       COM_26_print_score()
BD0A:          1F 10                     ;       COM_1F_print2 length=0x0010
BD0C:             F4 A4 B0 53 11 BC 9B 64 34 A1 6B 16 DB B9 27 A0 ; 
;
;                 PERCENT OF YOUR MISSION.
;

; -------------- Routine FN_CA_DIE_ENERGY_BEAM
;
BD1C: CA 50                              ; Routine Number: 0xCA, Length: 0x0050
BD1E:       0D 4E                        ;     COM_0D_while_pass length=0x004E
BD20:          25                        ;       COM_25_print_linefeed()
BD21:          25                        ;       COM_25_print_linefeed()
BD22:          1F 46                     ;       COM_1F_print2 length=0x0046
BD24:             26 BA F0 59 1E 8F 5C 15 DB 9F A7 B7 D0 92 D3 6D ; 
BD34:             99 16 1F D1 7E B1 90 14 30 15 31 62 44 DB 8F 5F ; 
BD44:             30 15 6E CA 5F A0 DB B5 19 A1 51 18 23 C6 74 CA ; 
BD54:             4E DB 4F 79 D5 15 EF 16 B7 B1 08 58 FF B2 51 18 ; 
BD64:             23 C6 F6 4E EB DA      ; 
;
;                 SUDDENLY, FROM SEEMINGLY NOWHERE, AN ENERGY BEAM ENVELOPES
;                 YOU! YOUR VERY LIFE IS PURGED FROM YOUR BODY!
;
BD6A:          1C 01                     ;       COM_1C_set_var_object(obj=OBJ_01_PLAYER)
BD6C:          1D 64                     ;       COM_1D_attack_var(points=100)















BD6E: 00                         
BD6F: 00                         
BD70: 00                         
BD71: 00                         
BD72: 00                         
BD73: 00                         
BD74: 00                         
BD75: 00                         
BD76: 01 00 01           
BD79: 00                         
BD7A: 00                         
BD7B: 00                         
BD7C: 00                         
BD7D: 00                         
BD7E: 00                         
BD7F: 00                         
BD80: A3              AND     E                   
BD81: 22 63 23        LD      ($2363),HL          
BD84: 63              LD      H,E                 
BD85: A3              AND     E                   
BD86: 62              LD      H,D                 
BD87: 22 63 23        LD      ($2363),HL          
BD8A: A7              AND     A                   
BD8B: E3              EX      (SP),HL             
BD8C: 63              LD      H,E                 
BD8D: E3              EX      (SP),HL             
BD8E: 67              LD      H,A                 
BD8F: E3              EX      (SP),HL             
BD90: 23              INC     HL                  
BD91: E7              RST     0X20                
BD92: 67              LD      H,A                 
BD93: 22 22 03        LD      ($0322),HL          
BD96: 22 22 E7        LD      ($E722),HL          
BD99: E2 E7 63        JP      PO,$63E7            ; {}
BD9C: E7              RST     0X20                
BD9D: E6 E7           AND     $E7                 
BD9F: E7              RST     0X20                
BDA0: 62              LD      H,D                 
BDA1: E2 62 63        JP      PO,$6362            ; {}
BDA4: E7              RST     0X20                
BDA5: E7              RST     0X20                
BDA6: E6 C7           AND     $C7                 
BDA8: C7              RST     0X00                
BDA9: C7              RST     0X00                
BDAA: C3 02 02        JP      $0202               
BDAD: 02              LD      (BC),A              
BDAE: 02              LD      (BC),A              
BDAF: 02              LD      (BC),A              
BDB0: C2 C2 42        JP      NZ,$42C2            
BDB3: 62              LD      H,D                 
BDB4: 23              INC     HL                  
BDB5: 02              LD      (BC),A              
BDB6: 23              INC     HL                  
BDB7: 02              LD      (BC),A              
BDB8: 02              LD      (BC),A              
BDB9: 02              LD      (BC),A              
BDBA: 03              INC     BC                  
BDBB: 22 23 02        LD      ($0223),HL          
BDBE: 23              INC     HL                  
BDBF: 02              LD      (BC),A              
BDC0: 02              LD      (BC),A              
BDC1: 02              LD      (BC),A              
BDC2: 02              LD      (BC),A              
BDC3: 02              LD      (BC),A              
BDC4: 02              LD      (BC),A              
BDC5: 02              LD      (BC),A              
BDC6: 02              LD      (BC),A              
BDC7: 02              LD      (BC),A              
BDC8: 02              LD      (BC),A              
BDC9: 02              LD      (BC),A              
BDCA: 02              LD      (BC),A              
BDCB: 02              LD      (BC),A              
BDCC: 02              LD      (BC),A              
BDCD: 02              LD      (BC),A              
BDCE: 02              LD      (BC),A              
BDCF: 02              LD      (BC),A              
BDD0: 02              LD      (BC),A              
BDD1: 02              LD      (BC),A              
BDD2: 02              LD      (BC),A              
BDD3: 02              LD      (BC),A              
BDD4: 02              LD      (BC),A              
BDD5: 02              LD      (BC),A              
BDD6: 02              LD      (BC),A              
BDD7: 02              LD      (BC),A              
BDD8: 02              LD      (BC),A              
BDD9: 02              LD      (BC),A              
BDDA: 02              LD      (BC),A              
BDDB: 02              LD      (BC),A              
BDDC: 02              LD      (BC),A              
BDDD: 02              LD      (BC),A              
BDDE: 02              LD      (BC),A              
BDDF: 02              LD      (BC),A              
BDE0: 02              LD      (BC),A              
BDE1: 02              LD      (BC),A              
BDE2: 02              LD      (BC),A              
BDE3: 02              LD      (BC),A              
BDE4: 02              LD      (BC),A              
BDE5: 02              LD      (BC),A              
BDE6: 02              LD      (BC),A              
BDE7: 02              LD      (BC),A              
BDE8: 02              LD      (BC),A              
BDE9: 02              LD      (BC),A              
BDEA: 02              LD      (BC),A              
BDEB: 02              LD      (BC),A              
BDEC: 02              LD      (BC),A              
BDED: 02              LD      (BC),A              
BDEE: 02              LD      (BC),A              
BDEF: 02              LD      (BC),A              
BDF0: 02              LD      (BC),A              
BDF1: 02              LD      (BC),A              
BDF2: 02              LD      (BC),A              
BDF3: 02              LD      (BC),A              
BDF4: 02              LD      (BC),A              
BDF5: 02              LD      (BC),A              
BDF6: 02              LD      (BC),A              
BDF7: 02              LD      (BC),A              
BDF8: 02              LD      (BC),A              
BDF9: 02              LD      (BC),A              
BDFA: 00                         
BDFB: 02              LD      (BC),A              
BDFC: 02              LD      (BC),A              
BDFD: 02              LD      (BC),A              
BDFE: 02              LD      (BC),A              
BDFF: 02              LD      (BC),A              
BE00: B3              OR      E                   
BE01: F2 FF FF        JP      P,$FFFF             
BE04: FF              RST     0X38                
BE05: FF              RST     0X38                
BE06: 73              LD      (HL),E              
BE07: 62              LD      H,D                 
BE08: FF              RST     0X38                
BE09: FF              RST     0X38                
BE0A: BF              CP      A                   
BE0B: FF              RST     0X38                
BE0C: FB              EI                          
BE0D: FF              RST     0X38                
BE0E: FF              RST     0X38                
BE0F: FF              RST     0X38                
BE10: FB              EI                          
BE11: FF              RST     0X38                
BE12: FF              RST     0X38                
BE13: FF              RST     0X38                
BE14: DF              RST     0X18                
BE15: FB              EI                          
BE16: DE F2           SBC     $F2                 
BE18: FF              RST     0X38                
BE19: FE FF           CP      $FF                 
BE1B: FF              RST     0X38                
BE1C: FF              RST     0X38                
BE1D: FF              RST     0X38                
BE1E: FF              RST     0X38                
BE1F: FF              RST     0X38                
BE20: FC FF FF        CALL    M,$FFFF             
BE23: FF              RST     0X38                
BE24: FF              RST     0X38                
BE25: FF              RST     0X38                
BE26: FE DF           CP      $DF                 
BE28: DF              RST     0X18                
BE29: DF              RST     0X18                
BE2A: DF              RST     0X18                
BE2B: DE DE           SBC     $DE                 
BE2D: DE DE           SBC     $DE                 
BE2F: DE DF           SBC     $DF                 
BE31: DF              RST     0X18                
BE32: 5F              LD      E,A                 
BE33: 7F              LD      A,A                 
BE34: 5F              LD      E,A                 
BE35: 5F              LD      E,A                 
BE36: 7F              LD      A,A                 
BE37: 5F              LD      E,A                 
BE38: 4A              LD      C,D                 
BE39: 5F              LD      E,A                 
BE3A: 5F              LD      E,A                 
BE3B: 7F              LD      A,A                 
BE3C: FF              RST     0X38                
BE3D: DF              RST     0X18                
BE3E: FD ; ????
BE3F: DF              RST     0X18                
BE40: 82              ADD     A,D                 
BE41: 00                         
BE42: 00                         
BE43: 00                         
BE44: 00                         
BE45: 00                         
BE46: 00                         
BE47: 00                         
BE48: 00                         
BE49: 00                         
BE4A: 00                         
BE4B: 00                         
BE4C: 00                         
BE4D: 00                         
BE4E: 00                         
BE4F: 00                         
BE50: 00                         
BE51: 00                         
BE52: 00                         
BE53: 00                         
BE54: 00                         
BE55: 00                         
BE56: 00                         
BE57: 00                         
BE58: 00                         
BE59: 00                         
BE5A: 00                         
BE5B: 00                         
BE5C: 00                         
BE5D: 00                         
BE5E: 00                         
BE5F: 00                         
BE60: 00                         
BE61: 00                         
BE62: 00                         
BE63: 00                         
BE64: 00                         
BE65: 00                         
BE66: 00                         
BE67: 00                         
BE68: 00                         
BE69: 00                         
BE6A: 00                         
BE6B: 10 92           DJNZ    $BDFF               ; {}
BE6D: 82              ADD     A,D                 
BE6E: 80              ADD     A,B                 
BE6F: 80              ADD     A,B                 
BE70: 80              ADD     A,B                 
BE71: 80              ADD     A,B                 
BE72: 90              SUB     B                   
BE73: 90              SUB     B                   
BE74: 80              ADD     A,B                 
BE75: 80              ADD     A,B                 
BE76: 90              SUB     B                   
BE77: 80              ADD     A,B                 
BE78: 10 00           DJNZ    $BE7A               ; {}
BE7A: 00                         
BE7B: 00                         
BE7C: 00                         
BE7D: 00                         
BE7E: 00                         
BE7F: 00                         
BE80: B3              OR      E                   
BE81: A2              AND     D                   
BE82: B7              OR      A                   
BE83: AF              XOR     A                   
BE84: AF              XOR     A                   
BE85: BF              CP      A                   
BE86: 23              INC     HL                  
BE87: 22 AF 3F        LD      ($3FAF),HL          
BE8A: AF              XOR     A                   
BE8B: BF              CP      A                   
BE8C: AB              XOR     E                   
BE8D: BF              CP      A                   
BE8E: BF              CP      A                   
BE8F: BF              CP      A                   
BE90: A3              AND     E                   
BE91: BF              CP      A                   
BE92: BF              CP      A                   
BE93: 3F              CCF                         
BE94: 3F              CCF                         
BE95: 93              SUB     E                   
BE96: 26 B2           LD      H,$B2               
BE98: BF              CP      A                   
BE99: BE              CP      (HL)                
BE9A: BF              CP      A                   
BE9B: 3F              CCF                         
BE9C: BF              CP      A                   
BE9D: BF              CP      A                   
BE9E: BF              CP      A                   
BE9F: BF              CP      A                   
BEA0: AC              XOR     H                   
BEA1: BE              CP      (HL)                
BEA2: 3E 3F           LD      A,$3F               
BEA4: BF              CP      A                   
BEA5: BF              CP      A                   
BEA6: BE              CP      (HL)                
BEA7: 9F              SBC     A                   
BEA8: 9F              SBC     A                   
BEA9: 9F              SBC     A                   
BEAA: 9F              SBC     A                   
BEAB: 1E 9E           LD      E,$9E               
BEAD: 0E 96           LD      C,$96               
BEAF: 9E              SBC     (HL)                
BEB0: DF              RST     0X18                
BEB1: 86              ADD     A,(HL)              
BEB2: 0F              RRCA                        
BEB3: 27              DAA                         
BEB4: 27              DAA                         
BEB5: 17              RLA                         
BEB6: 27              DAA                         
BEB7: 17              RLA                         
BEB8: 02              LD      (BC),A              
BEB9: 1F              RRA                         
BEBA: 07              RLCA                        
BEBB: 27              DAA                         
BEBC: 27              DAA                         
BEBD: 9F              SBC     A                   
BEBE: 27              DAA                         
BEBF: 17              RLA                         
BEC0: 02              LD      (BC),A              
BEC1: 00                         
BEC2: 00                         
BEC3: 00                         
BEC4: 00                         
BEC5: 00                         
BEC6: 00                         
BEC7: 00                         
BEC8: 00                         
BEC9: 00                         
BECA: 02              LD      (BC),A              
BECB: 00                         
BECC: 00                         
BECD: 00                         
BECE: 00                         
BECF: 00                         
BED0: 00                         
BED1: 00                         
BED2: 00                         
BED3: 00                         
BED4: 00                         
BED5: 00                         
BED6: 00                         
BED7: 00                         
BED8: 00                         
BED9: 00                         
BEDA: 00                         
BEDB: 00                         
BEDC: 00                         
BEDD: 00                         
BEDE: 00                         
BEDF: 00                         
BEE0: 00                         
BEE1: 00                         
BEE2: 00                         
BEE3: 00                         
BEE4: 00                         
BEE5: 00                         
BEE6: 02              LD      (BC),A              
BEE7: 00                         
BEE8: 00                         
BEE9: 00                         
BEEA: 00                         
BEEB: 00                         
BEEC: 00                         
BEED: 00                         
BEEE: 00                         
BEEF: 00                         
BEF0: 00                         
BEF1: 00                         
BEF2: 00                         
BEF3: 00                         
BEF4: 00                         
BEF5: 00                         
BEF6: 00                         
BEF7: 00                         
BEF8: 02              LD      (BC),A              
BEF9: 00                         
BEFA: 00                         
BEFB: 00                         
BEFC: 00                         
BEFD: 00                         
BEFE: 00                         
BEFF: 00                         
BF00: B3              OR      E                   
BF01: E2 EF EF         
BF04: EF              RST     0X28                
BF05: EF              RST     0X28                
BF06: 63              LD      H,E                 
BF07: 62              LD      H,D                 
BF08: EF              RST     0X28                
BF09: EF              RST     0X28                
BF0A: AF              XOR     A                   
BF0B: EF              RST     0X28                
BF0C: EB              EX      DE,HL               
BF0D: EF              RST     0X28                
BF0E: EF              RST     0X28                
BF0F: EF              RST     0X28                
BF10: EB              EX      DE,HL               
BF11: EF              RST     0X28                
BF12: EF              RST     0X28                
BF13: EF              RST     0X28                
BF14: EF              RST     0X28                
BF15: EB              EX      DE,HL               
BF16: EE E2           XOR     $E2                 
BF18: EF              RST     0X28                
BF19: EE EF           XOR     $EF                 
BF1B: EF              RST     0X28                
BF1C: EF              RST     0X28                
BF1D: EF              RST     0X28                
BF1E: EF              RST     0X28                
BF1F: EF              RST     0X28                
BF20: EC FE 6E        CALL    PE,$6EFE            ; {}
BF23: 6F              LD      L,A                 
BF24: EF              RST     0X28                
BF25: EF              RST     0X28                
BF26: FE EF           CP      $EF                 
BF28: CF              RST     0X08                
BF29: DF              RST     0X18                
BF2A: CF              RST     0X08                
BF2B: CE CE           ADC     $CE                 
BF2D: CE CA           ADC     $CA                 
BF2F: CE DF           ADC     $DF                 
BF31: CF              RST     0X08                
BF32: 5F              LD      E,A                 
BF33: 6F              LD      L,A                 
BF34: 6F              LD      L,A                 
BF35: 6F              LD      L,A                 
BF36: 6F              LD      L,A                 
BF37: 4F              LD      C,A                 
BF38: 4A              LD      C,D                 
BF39: 4F              LD      C,A                 
BF3A: 4F              LD      C,A                 
BF3B: 6F              LD      L,A                 
BF3C: ED ; ????
BF3D: EF              RST     0X28                
BF3E: ED ; ????
BF3F: EF              RST     0X28                
BF40: 82              ADD     A,D                 
BF41: 00                         
BF42: 00                         
BF43: 00                         
BF44: 00                         
BF45: 00                         
BF46: 00                         
BF47: 00                         
BF48: 00                         
BF49: 00                         
BF4A: 00                         
BF4B: 00                         
BF4C: 00                         
BF4D: 00                         
BF4E: 00                         
BF4F: 00                         
BF50: 00                         
BF51: 00                         
BF52: 00                         
BF53: 00                         
BF54: 00                         
BF55: 00                         
BF56: 00                         
BF57: 00                         
BF58: 00                         
BF59: 00                         
BF5A: 00                         
BF5B: 00                         
BF5C: 00                         
BF5D: 00                         
BF5E: 00                         
BF5F: 00                         
BF60: 00                         
BF61: 00                         
BF62: 00                         
BF63: 00                         
BF64: 00                         
BF65: 00                         
BF66: 00                         
BF67: 00                         
BF68: 00                         
BF69: 00                         
BF6A: 00                         
BF6B: 00                         
BF6C: 80              ADD     A,B                 
BF6D: 80              ADD     A,B                 
BF6E: 00                         
BF6F: 00                         
BF70: 00                         
BF71: 00                         
BF72: 00                         
BF73: 00                         
BF74: 00                         
BF75: 00                         
BF76: 00                         
BF77: 00                         
BF78: 00                         
BF79: 00                         
BF7A: 00                         
BF7B: 00                         
BF7C: 00                         
BF7D: 00                         
BF7E: 00                         
BF7F: 00                         
BF80: B3              OR      E                   
BF81: E2 EF EF        JP      PO,$EFEF            
BF84: EF              RST     0X28                
BF85: EF              RST     0X28                
BF86: 62              LD      H,D                 
BF87: 62              LD      H,D                 
BF88: EF              RST     0X28                
BF89: EF              RST     0X28                
BF8A: AF              XOR     A                   
BF8B: EF              RST     0X28                
BF8C: EB              EX      DE,HL               
BF8D: EF              RST     0X28                
BF8E: EF              RST     0X28                
BF8F: EF              RST     0X28                
BF90: EB              EX      DE,HL               
BF91: EF              RST     0X28                
BF92: EF              RST     0X28                
BF93: EF              RST     0X28                
BF94: EF              RST     0X28                
BF95: EB              EX      DE,HL               
BF96: EE E2           XOR     $E2                 
BF98: EF           
BF99: EE 
BF9A: 00 ; Stack builds towards lower from here

BF9B: EF               
BF9C: EF                        
BF9D: EF                      
BF9E: EF                  
BF9F: EF                   
BFA0: EC EE 6E   
BFA3: 6F                      
BFA4: EF                   
BFA5: EF                      
BFA6: EE CF                       
BFA8: CF                        
BFA9: CF                          
BFAA: CF                        
BFAB: CE CE                    
BFAD: CA CA CE             
BFB0: CE CE                       
BFB2: 4F                     
BFB3: 6F                    
BFB4: 67                       
BFB5: 6A                              
BFB6: 6F                           
BFB7: 42                         
BFB8: 4A                           
BFB9: 4B                     
BFBA: 4F                            
BFBB: 6A                           
BFBC: 6F                           
BFBD: EA EF EA     

BFC0: 02             
BFC1: 00                         
BFC2: 00                         
BFC3: 00                         
BFC4: 00                         
BFC5: 00                         
BFC6: 00                         
BFC7: 00                         
BFC8: 00                         
BFC9: 00                         
BFCA: 00                         
BFCB: 00                         
BFCC: 00                         
BFCD: 00                         
BFCE: 00                         
BFCF: 00                         
BFD0: 00                         
BFD1: 00                         
BFD2: 00                         
BFD3: 00                         
BFD4: 00                         
BFD5: 00                         
BFD6: 00                         
BFD7: 00                         
BFD8: 00                         
BFD9: 00                         
BFDA: 00                         
BFDB: 00                         
BFDC: 00                         
BFDD: 00                         
BFDE: 00                         
BFDF: 00                         
BFE0: 00                         
BFE1: 00                         
BFE2: 00                         
BFE3: 00                         
BFE4: 00                         
BFE5: 00                         
BFE6: 00                         
BFE7: 00                         
BFE8: 00                         
BFE9: 00                         
BFEA: 00                         
BFEB: 00                         
BFEC: 80                     
BFED: 80                       
BFEE: 00                         
BFEF: 00                         
BFF0: 00                         
BFF1: 00                         
BFF2: 00                         
BFF3: 00                         
BFF4: 00                         
BFF5: 00                         
BFF6: 00                         
BFF7: 00                         
BFF8: 00                         
BFF9: 00                         
BFFA: 00                         
BFFB: 00                         
BFFC: 00                         
BFFD: 00                         
BFFE: 00                         
BFFF: 00                    
```

