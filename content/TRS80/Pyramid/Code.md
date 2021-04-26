![TRS-80 Pyramid](TRS80Pyramid.jpg)

# Pyramid

>>> cpu Z80

>>> binary 4300:roms/Pyramid.bin

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](../Hardware.md)

# Start

```code
Start: 
4300: 31 BF 47        LD      SP,$47BF            ; Small stack space
4303: 3E 0E           LD      A,$0E               ; Clear ....
4305: CD 33 00        CALL    $0033               ; {hard.PrintChar} ... the screen
4308: 21 82 47        LD      HL,$4782            ; "WELCOME TO PYRAMID!!"
430B: CD D0 45        CALL    $45D0               ; {} Print the message
430E: CD EE 45        CALL    $45EE               ; {code.WaitForKey} Wait for a key

4311: 3E 01           LD      A,$01               ; Starting room is ...
4313: 32 3F 50        LD      ($503F),A           ; {ram.CurrentRoom} ... room 1
4316: CD 45 52        CALL    $5245               ; {} Print room description

4319: 97              SUB     A                   ; A=0
431A: 32 7B 46        LD      ($467B),A           ; {ram.Noun} Clear noun (object within reach)
431D: 32 7C 46        LD      ($467C),A           ; {ram.Verb} Clear verb (throw, north, rub, etc)
4320: 32 7D 46        LD      ($467D),A           ; {ram.Grammar} Grammar type (verb, verb+nounInReach, verb+nounInPack)
4323: CD CF 43        CALL    $43CF               ; {code.ParseUserInput} Get user input line and parse
4326: 3A 3F 50        LD      A,($503F)           ; {ram.CurrentRoom} Room number
4329: 21 88 48        LD      HL,$4888            ; Room descriptors
432C: CD 6B 43        CALL    $436B               ; {} Get 4 bytes for room
432F: 23              INC     HL                  ; Skip over ...
4330: 23              INC     HL                  ; ... to room's script pointer
4331: 7E              LD      A,(HL)              ; Script ...
4332: 23              INC     HL                  ; ... pointer ...
4333: 66              LD      H,(HL)              ; ... to ...
4334: 6F              LD      L,A                 ; ... HL
4335: CD 7D 43        CALL    $437D               ; {code.ProcessRoomScript} Process the room script
4338: C2 4A 43        JP      NZ,$434A            ; {} ZF clear ... script was successful. Move on.
433B: 21 B0 59        LD      HL,$59B0            ; General script
433E: CD 7D 43        CALL    $437D               ; {code.ProcessRoomScript} Process the script
4341: C2 4A 43        JP      NZ,$434A            ; {} Process the script
4344: 21 71 74        LD      HL,$7471            ; General fail message
4347: CD AE 45        CALL    $45AE               ; {code.PrintPacked} Print message
434A: CD D9 50        CALL    $50D9               ; {} After every turn
434D: C3 19 43        JP      $4319               ; {} Back to get user input
```

# Get Object Info

```code
GetObjectInfo:  
; Return ZF set if found in desired location
; Return HL points to object location structure
4350: 21 E7 4F        LD      HL,$4FE7            
4353: CD 61 43        CALL    $4361               ; {}
4356: 7E              LD      A,(HL)              
4357: E6 80           AND     $80                 
4359: 23              INC     HL                  
435A: 7E              LD      A,(HL)              
435B: C2 50 43        JP      NZ,$4350            ; {code.GetObjectInfo}
435E: 2B              DEC     HL                  
435F: BB              CP      E                   
4360: C9              RET                         

; HL = HL + (A-1)*2
4361: D5              PUSH    DE                  
4362: EB              EX      DE,HL               
4363: 6F              LD      L,A                 
4364: 2D              DEC     L                   
4365: 26 00           LD      H,$00               
4367: 29              ADD     HL,HL               
4368: 19              ADD     HL,DE               
4369: D1              POP     DE                  
436A: C9              RET                         

; HL = HL + (A-1)*4
436B: D5              PUSH    DE                  
436C: EB              EX      DE,HL               
436D: 6F              LD      L,A                 
436E: 2D              DEC     L                   
436F: 26 00           LD      H,$00               
4371: 29              ADD     HL,HL               
4372: 29              ADD     HL,HL               
4373: 19              ADD     HL,DE               
4374: D1              POP     DE                  
4375: C9              RET                         

; Set object's location
4376: CD 50 43        CALL    $4350               ; {code.GetObjectInfo}
4379: 23              INC     HL                  
437A: 73              LD      (HL),E              
437B: 2B              DEC     HL                  
437C: C9              RET                         
```

# Process Room Script

```code
; Process the user input against the script for a room
ProcessRoomScript: 
437D: 7E              LD      A,(HL)              
437E: A7              AND     A                   
437F: C8              RET     Z                   
4380: 3A 7C 46        LD      A,($467C)           ; {ram.Verb}
4383: BE              CP      (HL)                
4384: 23              INC     HL                  
4385: CA 8F 43        JP      Z,$438F             ; {}
4388: 4E              LD      C,(HL)              
4389: 06 00           LD      B,$00               
438B: 09              ADD     HL,BC               
438C: C3 7D 43        JP      $437D               ; {code.ProcessRoomScript}
438F: CD 96 43        CALL    $4396               ; {code.RunScript}
4392: C0              RET     NZ                  
4393: C3 7D 43        JP      $437D               ; {code.ProcessRoomScript}
```

# Run Script

```code
RunScript: 
4396: E5              PUSH    HL                  
4397: 4E              LD      C,(HL)              
4398: 06 00           LD      B,$00               
439A: 09              ADD     HL,BC               
439B: E3              EX      (SP),HL             
439C: 23              INC     HL                  
;              
RunScriptCommand: 
439D: 7E              LD      A,(HL)              
439E: 23              INC     HL                  
439F: E5              PUSH    HL                  
43A0: 21 9F 50        LD      HL,$509F            
43A3: CD 61 43        CALL    $4361               ; {}
43A6: 7E              LD      A,(HL)              
43A7: 23              INC     HL                  
43A8: 66              LD      H,(HL)              
43A9: 6F              LD      L,A                 
43AA: E9              JP      (HL)                
```

# Script Command PASS

```code
ScriptCommandPASS:     
43AB: E1              POP     HL                  
43AC: D1              POP     DE                  
43AD: 7C              LD      A,H                 
43AE: BA              CP      D                   
43AF: C2 BA 43        JP      NZ,$43BA            ; {}
43B2: 7D              LD      A,L                 
43B3: BB              CP      E                   
43B4: C2 BA 43        JP      NZ,$43BA            ; {}
43B7: F6 01           OR      $01                 
43B9: C9              RET                         
43BA: D5              PUSH    DE                  
43BB: C3 9D 43        JP      $439D               ; {code.RunScriptCommand}
```

# Script Command FAIL

```code
ScriptCommandFAIL: 
43BE: E1              POP     HL                  
43BF: E1              POP     HL                  
43C0: AF              XOR     A                   
43C1: C9              RET                         
```

# Script Command 06

```code
ScriptCommand06: 
; SubscriptAbortAllIfPass(...)
; Run the subscript. If the subscript passes then abort the current script and
; all parent scripts. If the subscript fails then continue on to the next command.
;
; How does this abort all current scripts, you ask?
; 43F6 only has two callers: the primary caller and the code here at 4423. The RET
; at 442E returns either to that primary caller or to 4426. The code at 4426 keeps
; the zero flag clear which continues to call return for subscripts eventually
; getting back to the primary caller.
43C2: E1              POP     HL                  
43C3: CD 96 43        CALL    $4396               ; {code.RunScript}
43C6: E5              PUSH    HL                  
43C7: CA AB 43        JP      Z,$43AB             ; {code.ScriptCommandPASS}
; The subscript failed. Bail out (with a PASS)
43CA: E1              POP     HL                  
43CB: E1              POP     HL                  
43CC: F6 01           OR      $01                 
43CE: C9              RET                         
```

# Parse User Input

```code
ParseUserInput: 
43CF: CD 05 46        CALL    $4605               ; {code.PromptAndReadLine}
43D2: CD A2 44        CALL    $44A2               ; {}
43D5: 2A AA 45        LD      HL,($45AA)          ; {}
43D8: 3A A8 45        LD      A,($45A8)           ; {}
43DB: 47              LD      B,A                 
43DC: 3A 7D 46        LD      A,($467D)           ; {ram.Grammar}
43DF: FE 03           CP      $03                 
43E1: CA CF 43        JP      Z,$43CF             ; {code.ParseUserInput}
43E4: 3A 7B 46        LD      A,($467B)           ; {ram.Noun}
43E7: A7              AND     A                   
43E8: C2 1C 44        JP      NZ,$441C            ; {}
43EB: 3A 7C 46        LD      A,($467C)           ; {ram.Verb}
43EE: A7              AND     A                   
43EF: C2 0D 44        JP      NZ,$440D            ; {}
43F2: 3A 7E 46        LD      A,($467E)           ; {}
43F5: 3C              INC     A                   
43F6: E6 03           AND     $03                 
43F8: 32 7E 46        LD      ($467E),A           ; {}
43FB: 21 7F 46        LD      HL,$467F            
43FE: 07              RLCA                        
43FF: 4F              LD      C,A                 
4400: 06 00           LD      B,$00               
4402: 09              ADD     HL,BC               
4403: 7E              LD      A,(HL)              
4404: 23              INC     HL                  
4405: 66              LD      H,(HL)              
4406: 6F              LD      L,A                 
4407: CD D0 45        CALL    $45D0               ; {}
440A: C3 CF 43        JP      $43CF               ; {code.ParseUserInput}
440D: 3A 7D 46        LD      A,($467D)           ; {ram.Grammar}
4410: FE C0           CP      $C0                 
4412: C8              RET     Z                   
4413: 21 FD 46        LD      HL,$46FD            
4416: CD D0 45        CALL    $45D0               ; {}
4419: C3 CF 43        JP      $43CF               ; {code.ParseUserInput}
441C: 22 AA 45        LD      ($45AA),HL          ; {}
441F: 3A A1 44        LD      A,($44A1)           ; {}
4422: A7              AND     A                   
4423: C2 8E 44        JP      NZ,$448E            ; {}
4426: 7E              LD      A,(HL)              
4427: 23              INC     HL                  
4428: 22 AA 45        LD      ($45AA),HL          ; {}
442B: 1E FF           LD      E,$FF               
442D: C5              PUSH    BC                  
442E: CD 50 43        CALL    $4350               ; {code.GetObjectInfo}
4431: C1              POP     BC                  
4432: CA 86 44        JP      Z,$4486             ; {}
4435: 3A 7D 46        LD      A,($467D)           ; {ram.Grammar}
4438: FE 40           CP      $40                 
443A: CA 4E 44        JP      Z,$444E             ; {}
443D: 2A AA 45        LD      HL,($45AA)          ; {}
4440: 2B              DEC     HL                  
4441: 3A 3F 50        LD      A,($503F)           ; {ram.CurrentRoom}
4444: 5F              LD      E,A                 
4445: 7E              LD      A,(HL)              
4446: C5              PUSH    BC                  
4447: CD 50 43        CALL    $4350               ; {code.GetObjectInfo}
444A: C1              POP     BC                  
444B: CA 86 44        JP      Z,$4486             ; {}
444E: 2A AA 45        LD      HL,($45AA)          ; {}
4451: 05              DEC     B                   
4452: C2 26 44        JP      NZ,$4426            ; {}
4455: 3A 7D 46        LD      A,($467D)           ; {ram.Grammar}
4458: FE 40           CP      $40                 
445A: C2 63 44        JP      NZ,$4463            ; {}
445D: 21 98 46        LD      HL,$4698            
4460: C3 7C 44        JP      $447C               ; {}
4463: 21 87 46        LD      HL,$4687            
4466: CD D0 45        CALL    $45D0               ; {}
4469: 3E 01           LD      A,$01               
446B: 32 FB 46        LD      ($46FB),A           ; {}
446E: 21 D3 46        LD      HL,$46D3            
4471: CD D0 45        CALL    $45D0               ; {}
4474: 3E 3F           LD      A,$3F               
4476: 32 FB 46        LD      ($46FB),A           ; {}
4479: 21 91 46        LD      HL,$4691            
447C: CD D0 45        CALL    $45D0               ; {}
447F: 97              SUB     A                   
4480: 32 7B 46        LD      ($467B),A           ; {ram.Noun}
4483: C3 CF 43        JP      $43CF               ; {code.ParseUserInput}
4486: 2A AA 45        LD      HL,($45AA)          ; {}
4489: 2B              DEC     HL                  
448A: 7E              LD      A,(HL)              
448B: 32 7B 46        LD      ($467B),A           ; {ram.Noun}
448E: 3A 7C 46        LD      A,($467C)           ; {ram.Verb}
4491: A7              AND     A                   
4492: C0              RET     NZ                  
4493: 21 B0 46        LD      HL,$46B0            
4496: CD D0 45        CALL    $45D0               ; {}
4499: 3E 01           LD      A,$01               
449B: 32 A1 44        LD      ($44A1),A           ; {}
449E: C3 CF 43        JP      $43CF               ; {code.ParseUserInput}
           
44A1: 00 ; 1 if there was a lone object last input 
                   
44A2: 21 5A 46        LD      HL,$465A            
44A5: 97              SUB     A                   
44A6: 32 A9 45        LD      ($45A9),A           ; {}
44A9: 32 7D 46        LD      ($467D),A           ; {ram.Grammar}
44AC: 11 CE 56        LD      DE,$56CE            
44AF: EB              EX      DE,HL               
44B0: 22 79 47        LD      ($4779),HL          ; {}
44B3: EB              EX      DE,HL               
44B4: 7E              LD      A,(HL)              
44B5: FE 20           CP      $20                 
44B7: C2 BE 44        JP      NZ,$44BE            ; {}
44BA: 23              INC     HL                  
44BB: C3 B4 44        JP      $44B4               ; {}
44BE: 22 7B 47        LD      ($477B),HL          ; {}
44C1: A7              AND     A                   
44C2: CA 5C 45        JP      Z,$455C             ; {}
44C5: 3E 01           LD      A,$01               
44C7: 32 A9 45        LD      ($45A9),A           ; {}
44CA: E5              PUSH    HL                  
44CB: 1A              LD      A,(DE)              
44CC: A7              AND     A                   
44CD: CA 67 45        JP      Z,$4567             ; {}
44D0: 32 81 47        LD      ($4781),A           ; {}
44D3: E6 07           AND     $07                 
44D5: 4F              LD      C,A                 
44D6: 32 7D 47        LD      ($477D),A           ; {}
44D9: 3A 81 47        LD      A,($4781)           ; {}
44DC: E6 38           AND     $38                 
44DE: 0F              RRCA                        
44DF: 0F              RRCA                        
44E0: 0F              RRCA                        
44E1: 47              LD      B,A                 
44E2: EB              EX      DE,HL               
44E3: 22 79 47        LD      ($4779),HL          ; {}
44E6: EB              EX      DE,HL               
44E7: 13              INC     DE                  
44E8: 1A              LD      A,(DE)              
44E9: BE              CP      (HL)                
44EA: C2 4E 45        JP      NZ,$454E            ; {}
44ED: 23              INC     HL                  
44EE: 13              INC     DE                  
44EF: 0D              DEC     C                   
44F0: C2 E8 44        JP      NZ,$44E8            ; {}
44F3: 3A 7D 47        LD      A,($477D)           ; {}
44F6: FE 06           CP      $06                 
44F8: CA 05 45        JP      Z,$4505             ; {}
44FB: 7E              LD      A,(HL)              
44FC: FE 20           CP      $20                 
44FE: CA 13 45        JP      Z,$4513             ; {}
4501: A7              AND     A                   
4502: C2 53 45        JP      NZ,$4553            ; {}
4505: 7E              LD      A,(HL)              
4506: FE 20           CP      $20                 
4508: CA 13 45        JP      Z,$4513             ; {}
450B: A7              AND     A                   
450C: CA 13 45        JP      Z,$4513             ; {}
450F: 23              INC     HL                  
4510: C3 05 45        JP      $4505               ; {}
4513: 3A 81 47        LD      A,($4781)           ; {}
4516: E6 C0           AND     $C0                 
4518: CA 2D 45        JP      Z,$452D             ; {}
451B: 32 7D 46        LD      ($467D),A           ; {ram.Grammar}
451E: 1A              LD      A,(DE)              
451F: 32 7C 46        LD      ($467C),A           ; {ram.Verb}
4522: E5              PUSH    HL                  
4523: 21 FD 46        LD      HL,$46FD            
4526: CD 85 45        CALL    $4585               ; {}
4529: E1              POP     HL                  
452A: C3 46 45        JP      $4546               ; {}
452D: 1A              LD      A,(DE)              
452E: 32 7B 46        LD      ($467B),A           ; {ram.Noun}
4531: EB              EX      DE,HL               
4532: 22 AA 45        LD      ($45AA),HL          ; {}
4535: EB              EX      DE,HL               
4536: 78              LD      A,B                 
4537: 32 A8 45        LD      ($45A8),A           ; {}
453A: 97              SUB     A                   
453B: 32 A1 44        LD      ($44A1),A           ; {}
453E: E5              PUSH    HL                  
453F: 21 D3 46        LD      HL,$46D3            
4542: CD 85 45        CALL    $4585               ; {}
4545: E1              POP     HL                  
4546: 7E              LD      A,(HL)              
4547: FE 20           CP      $20                 
4549: D1              POP     DE                  
454A: CA AC 44        JP      Z,$44AC             ; {}
454D: C9              RET                         
454E: 13              INC     DE                  
454F: 0D              DEC     C                   
4550: C2 4E 45        JP      NZ,$454E            ; {}
4553: 13              INC     DE                  
4554: 05              DEC     B                   
4555: C2 53 45        JP      NZ,$4553            ; {}
4558: E1              POP     HL                  
4559: C3 B4 44        JP      $44B4               ; {}
455C: 3A A9 45        LD      A,($45A9)           ; {}
455F: A7              AND     A                   
4560: C0              RET     NZ                  
4561: 3E 03           LD      A,$03               
4563: 32 7D 46        LD      ($467D),A           ; {ram.Grammar}
4566: C9              RET                         
4567: E1              POP     HL                  
4568: 97              SUB     A                   
4569: 32 7C 46        LD      ($467C),A           ; {ram.Verb}
456C: 32 7B 46        LD      ($467B),A           ; {ram.Noun}
456F: 7E              LD      A,(HL)              
4570: FE 20           CP      $20                 
4572: C2 79 45        JP      NZ,$4579            ; {}
4575: 23              INC     HL                  
4576: C3 6F 45        JP      $456F               ; {}
4579: 7E              LD      A,(HL)              
457A: A7              AND     A                   
457B: C8              RET     Z                   
457C: FE 20           CP      $20                 
457E: CA AC 44        JP      Z,$44AC             ; {}
4581: 23              INC     HL                  
4582: C3 79 45        JP      $4579               ; {}
4585: EB              EX      DE,HL               
4586: 2A 7B 47        LD      HL,($477B)          ; {}
4589: 06 28           LD      B,$28               
458B: 7E              LD      A,(HL)              
458C: A7              AND     A                   
458D: CA 9F 45        JP      Z,$459F             ; {}
4590: FE 20           CP      $20                 
4592: CA 9F 45        JP      Z,$459F             ; {}
4595: 12              LD      (DE),A              
4596: 23              INC     HL                  
4597: 13              INC     DE                  
4598: 05              DEC     B                   
4599: 78              LD      A,B                 
459A: FE 01           CP      $01                 
459C: C2 8B 45        JP      NZ,$458B            ; {}
459F: 3E 40           LD      A,$40               
45A1: 12              LD      (DE),A              
45A2: 13              INC     DE                  
45A3: 05              DEC     B                   
45A4: C2 9F 45        JP      NZ,$459F            ; {}
45A7: C9              RET                         

; RAM used in parsing input
45A8: 00             
45A9: 00                  
45AA: 00                   
45AB: 00                   
45AC: 00                   
45AD: 00 
```

# Print Packed

```code
PrintPacked: 
; Unpack a message (or multiple packed message) and print.
; HL is pointer to message                        
45AE: 7E              LD      A,(HL)              
45AF: A7              AND     A                   
45B0: C8              RET     Z                   
45B1: 23              INC     HL                  
45B2: 11 5A 46        LD      DE,$465A            
45B5: CD C2 47        CALL    $47C2               ; {}
45B8: 7E              LD      A,(HL)              
45B9: A7              AND     A                   
45BA: CA E7 45        JP      Z,$45E7             ; {}
45BD: FE 01           CP      $01                 
45BF: C8              RET     Z                   
45C0: 47              LD      B,A                 
45C1: E5              PUSH    HL                  
45C2: CD FF 45        CALL    $45FF               ; {code.PrintChar}
45C5: E1              POP     HL                  
45C6: 7E              LD      A,(HL)              
45C7: FE 0A           CP      $0A                 
45C9: 23              INC     HL                  
45CA: CA AE 45        JP      Z,$45AE             ; {code.PrintPacked}
45CD: C3 B8 45        JP      $45B8               ; {}

; HL points to message terminated by
;  - 0 : add a CR on the end and return
;  - 1 : no CR on the end and return
; Return with B holding last character (if any) sent to ROM routine.
;
45D0: 7E              LD      A,(HL)              
45D1: A7              AND     A                   
45D2: CA E7 45        JP      Z,$45E7             ; {}
45D5: FE 01           CP      $01                 
45D7: C8              RET     Z                   
45D8: FE 40           CP      $40                 
45DA: CA E3 45        JP      Z,$45E3             ; {}
45DD: 47              LD      B,A                 
45DE: E5              PUSH    HL                  
45DF: CD FF 45        CALL    $45FF               ; {code.PrintChar}
45E2: E1              POP     HL                  
45E3: 23              INC     HL                  
45E4: C3 D0 45        JP      $45D0               ; {}
45E7: 06 0D           LD      B,$0D               
45E9: 78              LD      A,B                 
45EA: CD FF 45        CALL    $45FF               ; {code.PrintChar}
45ED: C9              RET                         
```

# Wait for Key

```code
WaitForKey: 
45EE: D5              PUSH    DE                  
45EF: 3A 74 47        LD      A,($4774)           ; {}
45F2: 3C              INC     A                   
45F3: 32 74 47        LD      ($4774),A           ; {}
45F6: CD 2B 00        CALL    $002B               
45F9: A7              AND     A                   
45FA: CA EF 45        JP      Z,$45EF             ; {}
45FD: D1              POP     DE                  
45FE: C9              RET                         
```

# Print Char

```code
PrintChar:    
45FF: D5              PUSH    DE                  
4600: CD 33 00        CALL    $0033               ; {hard.PrintChar}
4603: D1              POP     DE                  
4604: C9              RET                         
```

# Prompt And Read Line

```code
PromptAndReadLine: 
4605: 06 3A           LD      B,$3A               
4607: 78              LD      A,B                 
4608: CD FF 45        CALL    $45FF               ; {code.PrintChar}
460B: 21 5A 46        LD      HL,$465A            
460E: 0E 00           LD      C,$00               
;
4610: E5              PUSH    HL                  
4611: C5              PUSH    BC                  
4612: D5              PUSH    DE                  
4613: CD EE 45        CALL    $45EE               ; {code.WaitForKey}
4616: D1              POP     DE                  
4617: C1              POP     BC                  
4618: E1              POP     HL                  
4619: 47              LD      B,A                 
461A: FE 08           CP      $08                 
461C: CA 41 46        JP      Z,$4641             ; {}
461F: 77              LD      (HL),A              
4620: CD FF 45        CALL    $45FF               ; {code.PrintChar}
4623: FE 0D           CP      $0D                 
4625: CA 57 46        JP      Z,$4657             ; {}
4628: 0C              INC     C                   
4629: 23              INC     HL                  
462A: 11 7A 46        LD      DE,$467A            
462D: 7C              LD      A,H                 
462E: BA              CP      D                   
462F: DA 10 46        JP      C,$4610             ; {}
4632: 7D              LD      A,L                 
4633: BB              CP      E                   
4634: DA 10 46        JP      C,$4610             ; {}
4637: 06 08           LD      B,$08               
4639: 78              LD      A,B                 
463A: CD FF 45        CALL    $45FF               ; {code.PrintChar}
463D: 2B              DEC     HL                  
463E: C3 10 46        JP      $4610               ; {}
4641: 2B              DEC     HL                  
4642: 3E 46           LD      A,$46               
4644: BC              CP      H                   
4645: DA 4E 46        JP      C,$464E             ; {}
4648: 7D              LD      A,L                 
4649: FE 5A           CP      $5A                 
464B: DA 0B 46        JP      C,$460B             ; {}
464E: 3E 08           LD      A,$08               
4650: 47              LD      B,A                 
4651: CD FF 45        CALL    $45FF               ; {code.PrintChar}
4654: C3 10 46        JP      $4610               ; {}
4657: 36 00           LD      (HL),$00            
4659: C9              RET                         
```

# Input Buffer

```code
; Input buffer (with some uninitialized leftover data!)
InputBuffer: 
;      A  N T  _  M  E  _  T  O  _  D  O  _  W  I  T
465A: 41 4E 54 20 4D 45 20 54 4F 20 44 4F 20 57 49 54             
;     H  _  T  H  E  _  ,  A  CR -- 0  0  0  0  _  _
466A: 48 20 54 48 45 20 2C 41 0D 12 30 30 30 30 20 20    

; Used in input parsing
467A: 00                   
467B: 00                    
467C: 00                   
467D: 00                    
467E: 00                   
;
467F: 25 47           
4681: 2C 47         
4683: 44 47       
4685: 58 47

; I_SEE_NO_
4687: 49 20 53 45 45 20 4E 4F 20 01

; _HERE.[CR]
4691: 20 48 45 52 45 2E 00

; YOU_AREN'T_CARRYING_IT.[CR]
4698: 59 4F 55 20 41 52 45 4E 27 54 20 43 41 52 52 59 49 4E 47 20 49 54 2E 00

; WHAT_DO_YOU_WANT_ME_TO_DO_WITH_THE_
46B0: 57 48 41 54 20 44 4F 20 59 4F 55 20 57 41 4E 54 20 4D 45 20 54 4F 20 44 4F 20 57 49 54 48 20 54
46D0: 48 45 20 
; 40 byte buffer for unknown noun word
46D3: 4F 57 20 54 48 41 54 20 57 4F 
46DD: 52 44 2E 00 49 20 44 4F 4E 27                
46E7: 54 20 55 4E 44 45 52 53 54 41            
46F1: 4E 44 2E 00 49 20 44 4F 4E 27
; "?"                   
46FB: 3F 00                 

; 40 byte buffer for unknown verb
46FD: 4B 4E 4F 57 20 57 48 41 54 20 
4707: 59 4F 55 20 4D 45 41 4E 2E 00
4711: 00 00 00 00 00 00 00 00 00 00                     
471B: 00 00 00 00 57 45 4C 43 4F 4D             

;" WHAT?",0
4725: 20 57 48 41 54 3F 00                  

; "I DON'T KNOW THAT WORD.",0
472C: 49 20 44 4F 4E 27 54 20 4B 4E 4F 57 20 54 48 41 54 20 57 4F 52 44 2E 00 

; "I DON'T UNDERSTAND.",0          
4744: 49 20 44 4F 4E 27 54 20 55 4E 44 45 52 53 54 41 4E 44 2E 00 
 
; "I DON'T KNOW WHAT YOU MEAN.",0          
4758: 49 20 44 4F 4E 27 54 20 4B 4E 4F 57 20 57 48 41 54 20 59 4F 55 20 4D 45 41 4E 2E 00  
          
4774: 00                    
4775: 00                              
4776: 00                              
4777: 00                              
4778: 00                              
4779: 00                              
477A: 00                              
477B: 00                              
477C: 00                              
477D: 00                              
477E: 00                              
477F: 00                              
4780: 00                              
4781: 00                              

; "WELCOME TO PYRAMID!!",0
4782: 57 45 4C 43 4F 4D 45 20 54 4F 20 50 59 52 41 4D 49 44 21 21 00 
        
4797: E1              POP     HL                  
4798: CA B8 47        JP      Z,$47B8             ; {}
479B: 3E 00           LD      A,$00               
479D: CE 00           ADC     $00                 
479F: 29              ADD     HL,HL               
47A0: 44              LD      B,H                 
47A1: 85              ADD     A,L                 
47A2: 2A 22 48        LD      HL,($4822)          ; {}
47A5: 95              SUB     L                   
47A6: 4F              LD      C,A                 
47A7: 78              LD      A,B                 
47A8: 9C              SBC     H                   
47A9: 47              LD      B,A                 
47AA: C5              PUSH    BC                  
47AB: D2 B0 47        JP      NC,$47B0            ; {}
47AE: 09              ADD     HL,BC               
47AF: E3              EX      (SP),HL             
47B0: 21 B7 47        LD      HL,$47B7            
47B3: 3F              CCF                         
47B4: C3 90 47        JP      $4790               ; {}
47B7: 00              NOP                         
47B8: 01 F9 47        LD      BC,$47F9            
47BB: 09              ADD     HL,BC               
47BC: 7E              LD      A,(HL)              
47BD: C1              POP     BC                  
47BE: E1              POP     HL                  
47BF: 00              NOP                         
47C0: 00              NOP                         
47C1: 00              NOP                         
47C2: 32 84 48        LD      ($4884),A           ; {}
47C5: 3E 01           LD      A,$01               
47C7: 32 87 48        LD      ($4887),A           ; {}
47CA: C3 D4 47        JP      $47D4               ; {}
47CD: 32 84 48        LD      ($4884),A           ; {}
47D0: 97              SUB     A                   
47D1: 32 87 48        LD      ($4887),A           ; {}
47D4: E5              PUSH    HL                  
47D5: 06 03           LD      B,$03               
47D7: E1              POP     HL                  
47D8: 7E              LD      A,(HL)              
47D9: 23              INC     HL                  
47DA: 4E              LD      C,(HL)              
47DB: 23              INC     HL                  
47DC: E5              PUSH    HL                  
47DD: 61              LD      H,C                 
47DE: 6F              LD      L,A                 
47DF: 13              INC     DE                  
47E0: 13              INC     DE                  
47E1: EB              EX      DE,HL               
47E2: E5              PUSH    HL                  
47E3: C5              PUSH    BC                  
47E4: 21 28 00        LD      HL,$0028            
47E7: 22 85 48        LD      ($4885),HL          ; {}
47EA: 21 1A 48        LD      HL,$481A            
47ED: 36 11           LD      (HL),$11            
47EF: 01 00 00        LD      BC,$0000            
47F2: C5              PUSH    BC                  
47F3: 7B              LD      A,E                 
47F4: 17              RLA                         
47F5: 5F              LD      E,A                 
47F6: 7A              LD      A,D                 
47F7: 17              RLA                         
47F8: 57              LD      D,A                 
47F9: 35              DEC     (HL)                
47FA: E1              POP     HL                  
47FB: CA 1B 48        JP      Z,$481B             ; {}
47FE: 3E 00           LD      A,$00               
4800: CE 00           ADC     $00                 
4802: 29              ADD     HL,HL               
4803: 44              LD      B,H                 
4804: 85              ADD     A,L                 
4805: 2A 85 48        LD      HL,($4885)          ; {}
4808: 95              SUB     L                   
4809: 4F              LD      C,A                 
480A: 78              LD      A,B                 
480B: 9C              SBC     H                   
480C: 47              LD      B,A                 
480D: C5              PUSH    BC                  
480E: D2 13 48        JP      NC,$4813            ; {}
4811: 09              ADD     HL,BC               
4812: E3              EX      (SP),HL             
4813: 21 1A 48        LD      HL,$481A            
4816: 3F              CCF                         
4817: C3 F3 47        JP      $47F3               ; {}
481A: 00              NOP                         
481B: 01 5C 48        LD      BC,$485C            
481E: 09              ADD     HL,BC               
481F: 7E              LD      A,(HL)              
4820: C1              POP     BC                  
4821: E1              POP     HL                  
4822: 77              LD      (HL),A              
4823: 2B              DEC     HL                  
4824: 05              DEC     B                   
4825: C2 E2 47        JP      NZ,$47E2            ; {}
4828: 3A 87 48        LD      A,($4887)           ; {}
482B: A7              AND     A                   
482C: CA 44 48        JP      Z,$4844             ; {}
482F: E5              PUSH    HL                  
4830: C5              PUSH    BC                  
4831: D5              PUSH    DE                  
4832: 1E 03           LD      E,$03               
4834: 23              INC     HL                  
4835: 46              LD      B,(HL)              
4836: E5              PUSH    HL                  
4837: 78              LD      A,B                 
4838: CD FF 45        CALL    $45FF               ; {code.PrintChar}
483B: E1              POP     HL                  
483C: 23              INC     HL                  
483D: 1D              DEC     E                   
483E: C2 35 48        JP      NZ,$4835            ; {}
4841: D1              POP     DE                  
4842: C1              POP     BC                  
4843: E1              POP     HL                  
4844: EB              EX      DE,HL               
4845: 13              INC     DE                  
4846: 3A 87 48        LD      A,($4887)           ; {}
4849: A7              AND     A                   
484A: C2 50 48        JP      NZ,$4850            ; {}
484D: 13              INC     DE                  
484E: 13              INC     DE                  
484F: 13              INC     DE                  
4850: 3A 84 48        LD      A,($4884)           ; {}
4853: 3D              DEC     A                   
4854: 32 84 48        LD      ($4884),A           ; {}
4857: C2 D5 47        JP      NZ,$47D5            ; {}
485A: E1              POP     HL                  
485B: C9              RET                         
```

# Character Table

```code
; Character compression table
CharTable:            
485C: 3F 21 32 20 22 27 3C 3E 2F 30 33                 ; ?!2_"'<>/03 
4867: 41 42 43 44 45 46 47 48 49 4A 4B 4C 4D 4E 4F 50  ; ABCDEFGHIJKLMNOP
4877: 51 52 53 54 55 56 57 58 59 5A 2D 2C 2E           ; QRSTUVWXYZ-,.

; RAM used by unpack
4884: 00           
4885: 00                    
4886: 00                    
4887: 00
```

# Room Table

 Each entry is 4 bytes. The first word is the packed room description. 
 The second word is the room's command script.

```code
RoomTable:
;
; 81 rooms numbered starting at 1
;      Description   Script                
4888: DB 5B CC 49
488C: 10 5C E1 49
4890: 57 5C F2 49
4894: 57 5C 03 4A
4898: 57 5C 14 4A
489C: 57 5C 25 4A
48A0: 68 5C 36 4A
48A4: E2 5C 47 4A
48A8: 28 5D 58 4A
48AC: 7D 5D 69 4A
48B0: A0 5D 7E 4A
48B4: 1E 5E 87 4A
48B8: 8E 5E 9D 4A
48BC: 69 5F C8 4A
48C0: AB 5F D1 4A
48C4: 08 60 0D 4B
48C8: 3C 60 48 4B
48CC: 55 60 51 4B
48D0: 85 60 90 4B
48D4: F1 60 A9 4B
48D8: 5F 61 BE 4B
48DC: AC 61 C7 4B
48E0: D8 61 D8 4B
48E4: E0 61 E1 4B
48E8: 18 62 F2 4B
48EC: 58 62 07 4C
48F0: B0 62 14 4C
48F4: C8 62 21 4C
48F8: C8 62 36 4C
48FC: C8 62 47 4C
4900: C8 62 60 4C
4904: C8 62 69 4C
4908: C8 62 76 4C
490C: C8 62 87 4C
4910: C8 62 98 4C
4914: C8 62 B1 4C
4918: C8 62 C2 4C
491C: C8 62 CB 4C
4920: C8 62 DC 4C
4924: C8 62 E9 4C
4928: C8 62 F6 4C
492C: D8 61 03 4D
4930: D8 61 08 4D
4934: D8 61 0D 4D
4938: D8 61 12 4D
493C: D8 61 17 4D
4940: D8 61 1C 4D
4944: D8 61 21 4D
4948: D8 61 26 4D
494C: D8 61 2B 4D
4950: D8 61 30 4D
4954: EA 62 41 4D
4958: D8 61 56 4D
495C: 49 63 5B 4D
4960: A6 63 68 4D
4964: DA 63 75 4D
4968: 1F 64 93 4D
496C: 7A 64 9C 4D
4970: 0A 65 B1 4D
4974: A1 65 BE 4D
4978: D5 65 06 4E
497C: 82 66 21 4E
4980: E0 66 2A 4E
4984: 07 67 33 4E
4988: 29 67 3C 4E
498C: 89 67 65 4E
4990: 00 00 00 00
4994: D2 6B 3B 4F
4998: 00 00 00 00
499C: B1 6B 32 4F
49A0: 5C 6B 25 4F
49A4: 25 68 6E 4E
49A8: 82 68 77 4E
49AC: 00 00 00 00
49B0: 00 00 00 00
49B4: F6 68 86 4E
49B8: F3 6A 0E 4F
49BC: 3F 69 9B 4E
49C0: 21 6A A8 4E
49C4: 4B 6A B1 4E
49C8: 9D 6A BE 4E
```

# Room Scripts

```code
RoomScripts:  
; "room_1" : {
;     "desc" : "YOU_ARE_STANDING_BEFORE_THE_ENTRANCE_OF_A_PYRAMID.__AROUND_YOU__IS_A_DESERT.[CR]",
;     "commands" : {
49CC: 01 03     ; "N" : [
49CE: 01 02     ;    "MoveToRoomX","room_2"],
49D0: 02 03     ; "E" : [
49D2: 01 03     ;    "MoveToRoomX","room_3"],
49D4: 03 03     ; "S" : [
49D6: 01 04     ;    "MoveToRoomX","room_4"],
49D8: 04 03     ; "W" : [
49DA: 01 05     ;    "MoveToRoomX","room_5"],
49DC: 0B 03     ; "IN" : [
49DE: 01 02     ;    "MoveToRoomX","room_2"],
49E0: 00
;     }
; },

; "room_2" : {
;     "desc" : "YOU_ARE_IN_THE_ENTRANCE_TO_THE_PYRAMID.__A_HOLE_IN_THE_FLOOR____LEADS_TO_A_PASSAGE_BENEATH_THE_SURFACE.[CR]",
;     "commands" : {
49E1: 03 03     ; "S" : [
49E3: 01 01     ;    "MoveToRoomX","room_1"],
49E5: 0A 03     ; "D" : [
49E7: 01 07     ;    "MoveToRoomX","room_7"],
49E9: 0C 03     ; "OUT" : [
49EB: 01 01     ;    "MoveToRoomX","room_1"],
49ED: 12 03     ; "PANEL" : [
49EF: 01 1A     ;    "MoveToRoomX","room_26"],
49F1: 00
;     }
; },

; "room_3" : {
;     "desc" : "YOU_ARE_IN_THE_DESERT.[CR]",
;     "commands" : {
49F2: 01 03     ; "N" : [
49F4: 01 06     ;    "MoveToRoomX","room_6"],
49F6: 02 03     ; "E" : [
49F8: 01 03     ;    "MoveToRoomX","room_3"],
49FA: 03 03     ; "S" : [
49FC: 01 04     ;    "MoveToRoomX","room_4"],
49FE: 04 03     ; "W" : [
4A00: 01 01     ;    "MoveToRoomX","room_1"],
4A02: 00
;     }
; },

; "room_4" : {
;     "desc" : "YOU_ARE_IN_THE_DESERT.[CR]",
;     "commands" : {
4A03: 01 03     ; "N" : [
4A05: 01 01     ;    "MoveToRoomX","room_1"],
4A07: 02 03     ; "E" : [
4A09: 01 03     ;    "MoveToRoomX","room_3"],
4A0B: 03 03     ; "S" : [
4A0D: 01 04     ;    "MoveToRoomX","room_4"],
4A0F: 04 03     ; "W" : [
4A11: 01 05     ;    "MoveToRoomX","room_5"],
4A13: 00
;     }
; },

; "room_5" : {
;     "desc" : "YOU_ARE_IN_THE_DESERT.[CR]",
;     "commands" : {
4A14: 01 03     ; "N" : [
4A16: 01 06     ;    "MoveToRoomX","room_6"],
4A18: 02 03     ; "E" : [
4A1A: 01 01     ;    "MoveToRoomX","room_1"],
4A1C: 03 03     ; "S" : [
4A1E: 01 04     ;    "MoveToRoomX","room_4"],
4A20: 04 03     ; "W" : [
4A22: 01 05     ;    "MoveToRoomX","room_5"],
4A24: 00
;     }
; },

; "room_6" : {
;     "desc" : "YOU_ARE_IN_THE_DESERT.[CR]",
;     "commands" : {
4A25: 01 03     ; "N" : [
4A27: 01 06     ;    "MoveToRoomX","room_6"],
4A29: 02 03     ; "E" : [
4A2B: 01 03     ;    "MoveToRoomX","room_3"],
4A2D: 03 03     ; "S" : [
4A2F: 01 01     ;    "MoveToRoomX","room_1"],
4A31: 04 03     ; "W" : [
4A33: 01 05     ;    "MoveToRoomX","room_5"],
4A35: 00
;     }
; },

; "room_7" : {
;     "desc" : "YOU_ARE_IN_A_SMALL_CHAMBER_BENEATH_A_HOLE_FROM_THE_SURFACE.__A__LOW_CRAWL_LEADS_INWARD_TO_THE_WEST.__HIEROGLYPHICS_ON_THE_WALL__TRANSLATE,_"CURSE_ALL_WHO_ENTER_THIS_SACRED_CRYPT."[CR]",
;     "commands" : {
4A36: 09 03     ; "U" : [
4A38: 01 02     ;    "MoveToRoomX","room_2"],
4A3A: 0C 03     ; "OUT" : [
4A3C: 01 02     ;    "MoveToRoomX","room_2"],
4A3E: 04 03     ; "W" : [
4A40: 01 08     ;    "MoveToRoomX","room_8"],
4A42: 0B 03     ; "IN" : [
4A44: 01 08     ;    "MoveToRoomX","room_8"],
4A46: 00
;     }
; },

; "room_8" : {
;     "desc" : "YOU_ARE_CRAWLING_OVER_PEBBLES_IN_A_LOW_PASSAGE.__THERE_IS_A_DIM_LIGHT_AT_THE_EAST_END_OF_THE_PASSAGE.[CR]",
;     "commands" : {
4A47: 02 03     ; "E" : [
4A49: 01 07     ;    "MoveToRoomX","room_7"],
4A4B: 0C 03     ; "OUT" : [
4A4D: 01 07     ;    "MoveToRoomX","room_7"],
4A4F: 04 03     ; "W" : [
4A51: 01 09     ;    "MoveToRoomX","room_9"],
4A53: 0B 03     ; "IN" : [
4A55: 01 09     ;    "MoveToRoomX","room_9"],
4A57: 00
;     }
; },

; "room_9" : {
;     "desc" : "YOU_ARE_IN_A_ROOM_FILLED_WITH_BROKEN_POTTERY_SHARDS_OF_ANCIENT__EGYPTIAN_CRAFTS.__AN_AWKWARD_CORRIDOR_LEADS_UPWARD_AND_WEST.[CR]",
;     "commands" : {
4A58: 02 03     ; "E" : [
4A5A: 01 08     ;    "MoveToRoomX","room_8"],
4A5C: 0B 03     ; "IN" : [
4A5E: 01 0A     ;    "MoveToRoomX","room_10"],
4A60: 09 03     ; "U" : [
4A62: 01 0A     ;    "MoveToRoomX","room_10"],
4A64: 04 03     ; "W" : [
4A66: 01 0A     ;    "MoveToRoomX","room_10"],
4A68: 00
;     }
; },

; "room_10" : {
;     "desc" : "YOU_ARE_IN_AN_AWKWARD_SLOPING_EAST/WEST_CORRIDOR.[CR]",
;     "commands" : {
4A69: 0A 03     ; "D" : [
4A6B: 01 09     ;    "MoveToRoomX","room_9"],
4A6D: 02 03     ; "E" : [
4A6F: 01 09     ;    "MoveToRoomX","room_9"],
4A71: 0B 03     ; "IN" : [
4A73: 01 0B     ;    "MoveToRoomX","room_11"],
4A75: 04 03     ; "W" : [
4A77: 01 0B     ;    "MoveToRoomX","room_11"],
4A79: 09 03     ; "U" : [
4A7B: 01 0B     ;    "MoveToRoomX","room_11"],
4A7D: 00
;     }
; },

; "room_11" : {
;     "desc" : "YOU_ARE_IN_A_SPLENDID_CHAMBER_THIRTY_FEET_HIGH.__THE_WALLS_ARE__FROZEN_RIVERS_OF_ORANGE_STONE.__AN_AWKWARD_CORRIDOR_AND_A_GOOD__PASSAGE_EXIT_FROM_THE_EAST_AND_WEST_SIDES_OF_THE_CHAMBER.[CR]",
;     "commands" : {
4A7E: 02 03     ; "E" : [
4A80: 01 0A     ;    "MoveToRoomX","room_10"],
4A82: 04 03     ; "W" : [
4A84: 01 0C     ;    "MoveToRoomX","room_12"],
4A86: 00
;     }
; },

; "room_12" : {
;     "desc" : "AT_YOUR_FEET_IS_A_SMALL_PIT_BREATHING_TRACES_OF_WHITE_MIST.__AN_EAST_PASSAGE_ENDS_HERE_EXCEPT_FOR_A_SMALL_CRACK_LEADING_ON._____ROUGH_STONE_STEPS_LEAD_DOWN_THE_PIT.[CR]",
;     "commands" : {
4A87: 02 03     ; "E" : [
4A89: 01 0B     ;    "MoveToRoomX","room_11"],
4A8B: 0A 0B     ; "D" : [
4A8D: 07 07     ;    "SubScripXtAbortIfPass",[
4A8F: 02 25     ;        "AssertObjectXIsInPack","#GOLD",
4A91: 04 71 71  ;        "PrintMessageX","YOU_ARE_AT_THE_BOTTOM_OF_THE_PIT_WITH_A_BROKEN_NECK.[CR]",
4A94: 05        ;        "PrintScoreAndStop"],
4A95: 01 0D     ;    "MoveToRoomX","room_13"],
4A97: 04 04     ; "W" : [
4A99: 04 96 71  ;    "PrintMessageX","THE_CRACK_IS_FAR_TOO_SMALL_FOR_YOU_TO_FOLLOW.[CR]"],
4A9C: 00
;     }
; },

; "room_13" : {
;     "desc" : "YOU_ARE_AT_ONE_END_OF_A_VAST_HALL_STRETCHING_FORWARD_OUT_OF_____SIGHT_TO_THE_WEST.__THERE_ARE_OPENINGS_TO_EITHER_SIDE.__NEARBY,_A_WIDE_STONE_STAIRCASE_LEADS_DOWNWARD.__THE_HALL_IS_VERY_MUSTY__AND_A_COLD_WIND_BLOWS_UP_THE_STAIRCASE.__THERE_IS_A_PASSAGE_AT__THE_TOP_OF_A_DOME_BEHIND_YOU.__ROUGH_STONE_STEPS_LEAD_UP_THE____DOME.[CR]",
;     "commands" : {
4A9D: 03 03     ; "S" : [
4A9F: 01 0E     ;    "MoveToRoomX","room_14"],
4AA1: 04 03     ; "W" : [
4AA3: 01 0F     ;    "MoveToRoomX","room_15"],
4AA5: 0A 03     ; "D" : [
4AA7: 01 10     ;    "MoveToRoomX","room_16"],
4AA9: 01 03     ; "N" : [
4AAB: 01 10     ;    "MoveToRoomX","room_16"],
4AAD: 09 0A     ; "U" : [
4AAF: 07 06     ;    "SubScripXtAbortIfPass",[
4AB1: 02 25     ;        "AssertObjectXIsInPack","#GOLD",
4AB3: 04 B6 71  ;        "PrintMessageX","THE_DOME_IS_UNCLIMBABLE.[CR]"],
4AB6: 01 0C     ;    "MoveToRoomX","room_12"],
4AB8: 02 0A     ; "E" : [
4ABA: 07 06     ;    "SubScripXtAbortIfPass",[
4ABC: 02 25     ;        "AssertObjectXIsInPack","#GOLD",
4ABE: 04 B6 71  ;        "PrintMessageX","THE_DOME_IS_UNCLIMBABLE.[CR]"],
4AC1: 01 0C     ;    "MoveToRoomX","room_12"],
4AC3: 20 03     ; "??20??" : [
4AC5: 01 1A     ;    "MoveToRoomX","room_26"],
4AC7: 00
;     }
; },

; "room_14" : {
;     "desc" : "THIS_IS_A_LOW_ROOM_WITH_A_HIEROGLYPH_ON_THE_WALL.__IT_TRANSLATES"YOU_WON'T_GET_IT_UP_THE_STEPS".[CR]",
;     "commands" : {
4AC8: 0C 03     ; "OUT" : [
4ACA: 01 0D     ;    "MoveToRoomX","room_13"],
4ACC: 01 03     ; "N" : [
4ACE: 01 0D     ;    "MoveToRoomX","room_13"],
4AD0: 00
;     }
; },

; "room_15" : {
;     "desc" : "YOU_ARE_ON_THE_EAST_BANK_OF_A_BOTTOMLESS_PIT_STRETCHING_ACROSS__THE_HALL.__THE_MIST_IS_QUITE_THICK_HERE,_AND_THE_PIT_IS_TOO_WIDETO_JUMP.[CR]",
;     "commands" : {
4AD1: 02 03     ; "E" : [
4AD3: 01 0D     ;    "MoveToRoomX","room_13"],
4AD5: 10 0C     ; "JUMP" : [
4AD7: 07 06     ;    "SubScripXtAbortIfPass",[
4AD9: 03 01     ;        "AssertObjectXIsInCurrentRoomOrPack","#bridge_15",
4ADB: 04 C8 71  ;        "PrintMessageX","I_RESPECTFULLY_SUGGEST_YOU_GO_ACROSS_THE_BRIDGE_INSTEAD_OF______JUMPING.[CR]"],
4ADE: 04 FA 71  ;    "PrintMessageX","YOU_DIDN'T_MAKE_IT.[CR]",
4AE1: 05        ;    "PrintScoreAndStop"],
4AE2: 04 0A     ; "W" : [
4AE4: 07 05     ;    "SubScripXtAbortIfPass",[
4AE6: 03 01     ;        "AssertObjectXIsInCurrentRoomOrPack","#bridge_15",
4AE8: 01 12     ;        "MoveToRoomX","room_18"],
4AEA: 04 09 72  ;    "PrintMessageX","THERE_IS_NO_WAY_ACROSS_THE_BOTTOMLESS_PIT.[CR]"],
4AED: 0D 05     ; "CROSS" : [
4AEF: 03 01     ;    "AssertObjectXIsInCurrentRoomOrPack","#bridge_15",
4AF1: 01 12     ;    "MoveToRoomX","room_18"],
4AF3: 23 18     ; "WAVE" : [
4AF5: 11 11     ;    "AssertObjectXMatchesUserInput","#SCEPTER",
4AF7: 07 0C     ;    "SubScripXtAbortIfPass",[
4AF9: 03 01     ;        "AssertObjectXIsInCurrentRoomOrPack","#bridge_15",
4AFB: 15 01 00  ;        "MoveObjectXToRoomY","#bridge_15","room_0",
4AFE: 15 02 00  ;        "MoveObjectXToRoomY","#bridge_18","room_0",
4B01: 04 DE 7B  ;        "PrintMessageX","THE_STONE_BRIDGE_HAS_RETRACTED![CR]"],
4B04: 18 01     ;    "MoveObjectXToCurrentRoom","#bridge_15",
4B06: 15 02 12  ;    "MoveObjectXToRoomY","#bridge_18","room_18",
4B09: 04 F5 7B  ;    "PrintMessageX","A_STONE_BRIDGE_NOW_SPANS_THE_BOTTOMLESS_PIT.[CR]"],
4B0C: 00
;     }
; },

; "room_16" : {
;     "desc" : "YOU_ARE_IN_THE_PHARAOH'S_CHAMBER,_WITH_PASSAGES_OFF_IN_ALL______DIRECTIONS.[CR]",
;     "commands" : {
4B0D: 09 03     ; "U" : [
4B0F: 01 0D     ;    "MoveToRoomX","room_13"],
4B11: 02 03     ; "E" : [
4B13: 01 0D     ;    "MoveToRoomX","room_13"],
4B15: 03 0A     ; "S" : [
4B17: 07 06     ;    "SubScripXtAbortIfPass",[
4B19: 03 0B     ;        "AssertObjectXIsInCurrentRoomOrPack","#SERPENT",
4B1B: 04 27 72  ;        "PrintMessageX","YOU_CAN'T_GET_BY_THE_SERPENT.[CR]"],
4B1E: 01 11     ;    "MoveToRoomX","room_17"],
4B20: 01 0A     ; "N" : [
4B22: 07 06     ;    "SubScripXtAbortIfPass",[
4B24: 03 0B     ;        "AssertObjectXIsInCurrentRoomOrPack","#SERPENT",
4B26: 04 27 72  ;        "PrintMessageX","YOU_CAN'T_GET_BY_THE_SERPENT.[CR]"],
4B29: 01 19     ;    "MoveToRoomX","room_25"],
4B2B: 04 0A     ; "W" : [
4B2D: 07 06     ;    "SubScripXtAbortIfPass",[
4B2F: 03 0B     ;        "AssertObjectXIsInCurrentRoomOrPack","#SERPENT",
4B31: 04 27 72  ;        "PrintMessageX","YOU_CAN'T_GET_BY_THE_SERPENT.[CR]"],
4B34: 01 18     ;    "MoveToRoomX","room_24"],
4B36: 26 10     ; "THROW" : [
4B38: 11 14     ;    "AssertObjectXMatchesUserInput","#BIRD_boxed",
4B3A: 03 0B     ;    "AssertObjectXIsInCurrentRoomOrPack","#SERPENT",
4B3C: 15 0B 00  ;    "MoveObjectXToRoomY","#SERPENT","room_0",
4B3F: 18 13     ;    "MoveObjectXToCurrentRoom","#BIRD",
4B41: 15 14 00  ;    "MoveObjectXToRoomY","#BIRD_boxed","room_0",
4B44: 04 A1 7C  ;    "PrintMessageX","THE_BIRD_STATUE_COMES_TO_LIFE_AND_ATTACKS_THE_SERPENT_AND_IN_AN_ASTOUNDING_FLURRY,_DRIVES_THE_SERPENT_AWAY.__THE_BIRD_TURNS_BACKINTO_A_STATUE.[CR]"],
4B47: 00
;     }
; },

; "room_17" : {
;     "desc" : "YOU_ARE_IN_THE_SOUTH_SIDE_CHAMBER.[CR]",
;     "commands" : {
4B48: 01 03     ; "N" : [
4B4A: 01 10     ;    "MoveToRoomX","room_16"],
4B4C: 0C 03     ; "OUT" : [
4B4E: 01 10     ;    "MoveToRoomX","room_16"],
4B50: 00
;     }
; },

; "room_18" : {
;     "desc" : "YOU_ARE_ON_THE_WEST_SIDE_OF_THE_BOTTOMLESS_PIT_IN_THE_HALL_OF___GODS.[CR]",
;     "commands" : {
4B51: 10 0C     ; "JUMP" : [
4B53: 07 06     ;    "SubScripXtAbortIfPass",[
4B55: 03 02     ;        "AssertObjectXIsInCurrentRoomOrPack","#bridge_18",
4B57: 04 C8 71  ;        "PrintMessageX","I_RESPECTFULLY_SUGGEST_YOU_GO_ACROSS_THE_BRIDGE_INSTEAD_OF______JUMPING.[CR]"],
4B5A: 04 FA 71  ;    "PrintMessageX","YOU_DIDN'T_MAKE_IT.[CR]",
4B5D: 05        ;    "PrintScoreAndStop"],
4B5E: 02 0A     ; "E" : [
4B60: 07 05     ;    "SubScripXtAbortIfPass",[
4B62: 03 02     ;        "AssertObjectXIsInCurrentRoomOrPack","#bridge_18",
4B64: 01 0F     ;        "MoveToRoomX","room_15"],
4B66: 04 09 72  ;    "PrintMessageX","THERE_IS_NO_WAY_ACROSS_THE_BOTTOMLESS_PIT.[CR]"],
4B69: 01 06     ; "N" : [
4B6B: 04 3D 72  ;    "PrintMessageX","YOU_HAVE_CRAWLED_THROUGH_A_VERY_LOW_WIDE_PASSAGE_PARALLEL_TO_ANDNORTH_OF_THE_HALL_OF_GODS.[CR]",
4B6E: 01 13     ;    "MoveToRoomX","room_19"],
4B70: 0D 05     ; "CROSS" : [
4B72: 03 02     ;    "AssertObjectXIsInCurrentRoomOrPack","#bridge_18",
4B74: 01 0F     ;    "MoveToRoomX","room_15"],
4B76: 23 18     ; "WAVE" : [
4B78: 11 11     ;    "AssertObjectXMatchesUserInput","#SCEPTER",
4B7A: 07 0C     ;    "SubScripXtAbortIfPass",[
4B7C: 03 02     ;        "AssertObjectXIsInCurrentRoomOrPack","#bridge_18",
4B7E: 15 02 00  ;        "MoveObjectXToRoomY","#bridge_18","room_0",
4B81: 15 01 00  ;        "MoveObjectXToRoomY","#bridge_15","room_0",
4B84: 04 DE 7B  ;        "PrintMessageX","THE_STONE_BRIDGE_HAS_RETRACTED![CR]"],
4B87: 18 02     ;    "MoveObjectXToCurrentRoom","#bridge_18",
4B89: 15 01 0F  ;    "MoveObjectXToRoomY","#bridge_15","room_15",
4B8C: 04 F5 7B  ;    "PrintMessageX","A_STONE_BRIDGE_NOW_SPANS_THE_BOTTOMLESS_PIT.[CR]"],
4B8F: 00
;     }
; },

; "room_19" : {
;     "desc" : "YOU_ARE_AT_THE_WEST_END_OF_THE_HALL_OF_GODS.___A_LOW_WIDE_PASS__CONTINUES_WEST_AND_ANOTHER_GOES_NORTH.__TO_THE_SOUTH_IS_A_LITTLEPASSAGE_SIX_FEET_OFF_THE_FLOOR.[CR]",
;     "commands" : {
4B90: 03 03     ; "S" : [
4B92: 01 1C     ;    "MoveToRoomX","room_28"],
4B94: 09 03     ; "U" : [
4B96: 01 1C     ;    "MoveToRoomX","room_28"],
4B98: 11 03     ; "CLIMB" : [
4B9A: 01 1C     ;    "MoveToRoomX","room_28"],
4B9C: 02 03     ; "E" : [
4B9E: 01 12     ;    "MoveToRoomX","room_18"],
4BA0: 01 03     ; "N" : [
4BA2: 01 12     ;    "MoveToRoomX","room_18"],
4BA4: 04 03     ; "W" : [
4BA6: 01 14     ;    "MoveToRoomX","room_20"],
4BA8: 00
;     }
; },

; "room_20" : {
;     "desc" : "YOU_ARE_AT_EAST_END_OF_A_VERY_LONG_HALL_APPARENTLY_WITHOUT_SIDE_CHAMBERS.__TO_THE_EAST_A_LOW_WIDE_CRAWL_SLANTS_UP.__TO_THE_NORTHA_ROUND_TWO_FOOT_HOLE_SLANTS_DOWN.[CR]",
;     "commands" : {
4BA9: 02 03     ; "E" : [
4BAB: 01 13     ;    "MoveToRoomX","room_19"],
4BAD: 09 03     ; "U" : [
4BAF: 01 13     ;    "MoveToRoomX","room_19"],
4BB1: 04 03     ; "W" : [
4BB3: 01 15     ;    "MoveToRoomX","room_21"],
4BB5: 01 03     ; "N" : [
4BB7: 01 16     ;    "MoveToRoomX","room_22"],
4BB9: 0A 03     ; "D" : [
4BBB: 01 16     ;    "MoveToRoomX","room_22"],
4BBD: 00
;     }
; },

; "room_21" : {
;     "desc" : "YOU_ARE_AT_THE_WEST_END_OF_A_VERY_LONG_FEATURELESS_HALL.__THE___HALL_JOINS_UP_WITH_A_NARROW_NORTH/SOUTH_PASSAGE.[CR]",
;     "commands" : {
4BBE: 02 03     ; "E" : [
4BC0: 01 14     ;    "MoveToRoomX","room_20"],
4BC2: 01 03     ; "N" : [
4BC4: 01 16     ;    "MoveToRoomX","room_22"],
4BC6: 00
;     }
; },

; "room_22" : {
;     "desc" : "YOU_ARE_AT_A_CROSSOVER_OF_A_HIGH_N/S_PASSAGE_AND_A_LOW_E/W_ONE.[CR]",
;     "commands" : {
4BC7: 04 03     ; "W" : [
4BC9: 01 14     ;    "MoveToRoomX","room_20"],
4BCB: 01 03     ; "N" : [
4BCD: 01 17     ;    "MoveToRoomX","room_23"],
4BCF: 02 03     ; "E" : [
4BD1: 01 18     ;    "MoveToRoomX","room_24"],
4BD3: 03 03     ; "S" : [
4BD5: 01 15     ;    "MoveToRoomX","room_21"],
4BD7: 00
;     }
; },

; "room_23" : {
;     "desc" : "DEAD_END.[CR]",
;     "commands" : {
4BD8: 03 03     ; "S" : [
4BDA: 01 16     ;    "MoveToRoomX","room_22"],
4BDC: 0C 03     ; "OUT" : [
4BDE: 01 16     ;    "MoveToRoomX","room_22"],
4BE0: 00
;     }
; },

; "room_24" : {
;     "desc" : "YOU_ARE_IN_THE_WEST_THRONE_CHAMBER.__A_PASSAGE_CONTINUES_WEST___AND_UP_FROM_HERE.[CR]",
;     "commands" : {
4BE1: 02 03     ; "E" : [
4BE3: 01 10     ;    "MoveToRoomX","room_16"],
4BE5: 0C 03     ; "OUT" : [
4BE7: 01 10     ;    "MoveToRoomX","room_16"],
4BE9: 04 03     ; "W" : [
4BEB: 01 16     ;    "MoveToRoomX","room_22"],
4BED: 09 03     ; "U" : [
4BEF: 01 16     ;    "MoveToRoomX","room_22"],
4BF1: 00
;     }
; },

; "room_25" : {
;     "desc" : "YOU_ARE_IN_A_LOW_N/S_PASSAGE_AT_A_HOLE_IN_THE_FLOOR.__THE_HOLE__GOES_DOWN_TO_AN_E/W_PASSAGE.[CR]",
;     "commands" : {
4BF2: 0C 03     ; "OUT" : [
4BF4: 01 10     ;    "MoveToRoomX","room_16"],
4BF6: 03 03     ; "S" : [
4BF8: 01 10     ;    "MoveToRoomX","room_16"],
4BFA: 01 03     ; "N" : [
4BFC: 01 1A     ;    "MoveToRoomX","room_26"],
4BFE: 20 03     ; "??20??" : [
4C00: 01 1A     ;    "MoveToRoomX","room_26"],
4C02: 0A 03     ; "D" : [
4C04: 01 36     ;    "MoveToRoomX","room_54"],
4C06: 00
;     }
; },

; "room_26" : {
;     "desc" : "YOU_ARE_IN_A_LARGE_ROOM,_WITH_A_PASSAGE_TO_THE_SOUTH,_AND_A_WALLOF_BROKEN_ROCK_TO_THE_EAST.__THERE_IS_A_PANEL_ON_THE_NORTH_WALL.[CR]",
;     "commands" : {
4C07: 12 03     ; "PANEL" : [
4C09: 01 02     ;    "MoveToRoomX","room_2"],
4C0B: 03 03     ; "S" : [
4C0D: 01 19     ;    "MoveToRoomX","room_25"],
4C0F: 02 03     ; "E" : [
4C11: 01 1B     ;    "MoveToRoomX","room_27"],
4C13: 00
;     }
; },

; "room_27" : {
;     "desc" : "YOU_ARE_IN_THE_CHAMBER_OF_ANUBIS.[CR]",
;     "commands" : {
4C14: 0A 03     ; "D" : [
4C16: 01 1A     ;    "MoveToRoomX","room_26"],
4C18: 20 03     ; "??20??" : [
4C1A: 01 1A     ;    "MoveToRoomX","room_26"],
4C1C: 09 03     ; "U" : [
4C1E: 01 0D     ;    "MoveToRoomX","room_13"],
4C20: 00
;     }
; },

; "room_28" : {
;     "desc" : "YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]",
;     "commands" : {
4C21: 01 03     ; "N" : [
4C23: 01 1C     ;    "MoveToRoomX","room_28"],
4C25: 02 03     ; "E" : [
4C27: 01 20     ;    "MoveToRoomX","room_32"],
4C29: 03 03     ; "S" : [
4C2B: 01 1E     ;    "MoveToRoomX","room_30"],
4C2D: 04 03     ; "W" : [
4C2F: 01 1D     ;    "MoveToRoomX","room_29"],
4C31: 09 03     ; "U" : [
4C33: 01 13     ;    "MoveToRoomX","room_19"],
4C35: 00
;     }
; },

; "room_29" : {
;     "desc" : "YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]",
;     "commands" : {
4C36: 01 03     ; "N" : [
4C38: 01 1C     ;    "MoveToRoomX","room_28"],
4C3A: 02 03     ; "E" : [
4C3C: 01 33     ;    "MoveToRoomX","room_51"],
4C3E: 03 03     ; "S" : [
4C40: 01 1D     ;    "MoveToRoomX","room_29"],
4C42: 04 03     ; "W" : [
4C44: 01 1D     ;    "MoveToRoomX","room_29"],
4C46: 00
;     }
; },

; "room_30" : {
;     "desc" : "YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]",
;     "commands" : {
4C47: 01 03     ; "N" : [
4C49: 01 20     ;    "MoveToRoomX","room_32"],
4C4B: 02 03     ; "E" : [
4C4D: 01 2A     ;    "MoveToRoomX","room_42"],
4C4F: 03 03     ; "S" : [
4C51: 01 2B     ;    "MoveToRoomX","room_43"],
4C53: 04 03     ; "W" : [
4C55: 01 1C     ;    "MoveToRoomX","room_28"],
4C57: 09 03     ; "U" : [
4C59: 01 1F     ;    "MoveToRoomX","room_31"],
4C5B: 0A 03     ; "D" : [
4C5D: 01 1F     ;    "MoveToRoomX","room_31"],
4C5F: 00
;     }
; },

; "room_31" : {
;     "desc" : "YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]",
;     "commands" : {
4C60: 09 03     ; "U" : [
4C62: 01 1E     ;    "MoveToRoomX","room_30"],
4C64: 0A 03     ; "D" : [
4C66: 01 1E     ;    "MoveToRoomX","room_30"],
4C68: 00
;     }
; },

; "room_32" : {
;     "desc" : "YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]",
;     "commands" : {
4C69: 02 03     ; "E" : [
4C6B: 01 1E     ;    "MoveToRoomX","room_30"],
4C6D: 03 03     ; "S" : [
4C6F: 01 21     ;    "MoveToRoomX","room_33"],
4C71: 04 03     ; "W" : [
4C73: 01 1C     ;    "MoveToRoomX","room_28"],
4C75: 00
;     }
; },

; "room_33" : {
;     "desc" : "YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]",
;     "commands" : {
4C76: 01 03     ; "N" : [
4C78: 01 2C     ;    "MoveToRoomX","room_44"],
4C7A: 02 03     ; "E" : [
4C7C: 01 20     ;    "MoveToRoomX","room_32"],
4C7E: 03 03     ; "S" : [
4C80: 01 22     ;    "MoveToRoomX","room_34"],
4C82: 0A 03     ; "D" : [
4C84: 01 2D     ;    "MoveToRoomX","room_45"],
4C86: 00
;     }
; },

; "room_34" : {
;     "desc" : "YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]",
;     "commands" : {
4C87: 02 03     ; "E" : [
4C89: 01 21     ;    "MoveToRoomX","room_33"],
4C8B: 03 03     ; "S" : [
4C8D: 01 23     ;    "MoveToRoomX","room_35"],
4C8F: 04 03     ; "W" : [
4C91: 01 25     ;    "MoveToRoomX","room_37"],
4C93: 0A 03     ; "D" : [
4C95: 01 26     ;    "MoveToRoomX","room_38"],
4C97: 00
;     }
; },

; "room_35" : {
;     "desc" : "YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]",
;     "commands" : {
4C98: 01 03     ; "N" : [
4C9A: 01 24     ;    "MoveToRoomX","room_36"],
4C9C: 02 03     ; "E" : [
4C9E: 01 26     ;    "MoveToRoomX","room_38"],
4CA0: 03 03     ; "S" : [
4CA2: 01 23     ;    "MoveToRoomX","room_35"],
4CA4: 04 03     ; "W" : [
4CA6: 01 22     ;    "MoveToRoomX","room_34"],
4CA8: 09 03     ; "U" : [
4CAA: 01 27     ;    "MoveToRoomX","room_39"],
4CAC: 0A 03     ; "D" : [
4CAE: 01 2F     ;    "MoveToRoomX","room_47"],
4CB0: 00
;     }
; },

; "room_36" : {
;     "desc" : "YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]",
;     "commands" : {
4CB1: 01 03     ; "N" : [
4CB3: 01 24     ;    "MoveToRoomX","room_36"],
4CB5: 02 03     ; "E" : [
4CB7: 01 34     ;    "MoveToRoomX","room_52"],
4CB9: 04 03     ; "W" : [
4CBB: 01 23     ;    "MoveToRoomX","room_35"],
4CBD: 0A 03     ; "D" : [
4CBF: 01 30     ;    "MoveToRoomX","room_48"],
4CC1: 00
;     }
; },

; "room_37" : {
;     "desc" : "YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]",
;     "commands" : {
4CC2: 02 03     ; "E" : [
4CC4: 01 22     ;    "MoveToRoomX","room_34"],
4CC6: 04 03     ; "W" : [
4CC8: 01 26     ;    "MoveToRoomX","room_38"],
4CCA: 00
;     }
; },

; "room_38" : {
;     "desc" : "YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]",
;     "commands" : {
4CCB: 02 03     ; "E" : [
4CCD: 01 23     ;    "MoveToRoomX","room_35"],
4CCF: 03 03     ; "S" : [
4CD1: 01 27     ;    "MoveToRoomX","room_39"],
4CD3: 04 03     ; "W" : [
4CD5: 01 25     ;    "MoveToRoomX","room_37"],
4CD7: 09 03     ; "U" : [
4CD9: 01 22     ;    "MoveToRoomX","room_34"],
4CDB: 00
;     }
; },

; "room_39" : {
;     "desc" : "YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]",
;     "commands" : {
4CDC: 01 03     ; "N" : [
4CDE: 01 23     ;    "MoveToRoomX","room_35"],
4CE0: 03 03     ; "S" : [
4CE2: 01 2E     ;    "MoveToRoomX","room_46"],
4CE4: 04 03     ; "W" : [
4CE6: 01 26     ;    "MoveToRoomX","room_38"],
4CE8: 00
;     }
; },

; "room_40" : {
;     "desc" : "YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]",
;     "commands" : {
4CE9: 01 03     ; "N" : [
4CEB: 01 34     ;    "MoveToRoomX","room_52"],
4CED: 04 03     ; "W" : [
4CEF: 01 29     ;    "MoveToRoomX","room_41"],
4CF1: 08 03     ; "NW" : [
4CF3: 01 35     ;    "MoveToRoomX","room_53"],
4CF5: 00
;     }
; },

; "room_41" : {
;     "desc" : "YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]",
;     "commands" : {
4CF6: 02 03     ; "E" : [
4CF8: 01 28     ;    "MoveToRoomX","room_40"],
4CFA: 03 03     ; "S" : [
4CFC: 01 34     ;    "MoveToRoomX","room_52"],
4CFE: 04 03     ; "W" : [
4D00: 01 32     ;    "MoveToRoomX","room_50"],
4D02: 00
;     }
; },

; "room_42" : {
;     "desc" : "DEAD_END.[CR]",
;     "commands" : {
4D03: 04 03     ; "W" : [
4D05: 01 1E     ;    "MoveToRoomX","room_30"],
4D07: 00
;     }
; },

; "room_43" : {
;     "desc" : "DEAD_END.[CR]",
;     "commands" : {
4D08: 02 03     ; "E" : [
4D0A: 01 1E     ;    "MoveToRoomX","room_30"],
4D0C: 00
;     }
; },

; "room_44" : {
;     "desc" : "DEAD_END.[CR]",
;     "commands" : {
4D0D: 03 03     ; "S" : [
4D0F: 01 21     ;    "MoveToRoomX","room_33"],
4D11: 00
;     }
; },

; "room_45" : {
;     "desc" : "DEAD_END.[CR]",
;     "commands" : {
4D12: 09 03     ; "U" : [
4D14: 01 21     ;    "MoveToRoomX","room_33"],
4D16: 00
;     }
; },

; "room_46" : {
;     "desc" : "DEAD_END.[CR]",
;     "commands" : {
4D17: 04 03     ; "W" : [
4D19: 01 27     ;    "MoveToRoomX","room_39"],
4D1B: 00
;     }
; },

; "room_47" : {
;     "desc" : "DEAD_END.[CR]",
;     "commands" : {
4D1C: 09 03     ; "U" : [
4D1E: 01 23     ;    "MoveToRoomX","room_35"],
4D20: 00
;     }
; },

; "room_48" : {
;     "desc" : "DEAD_END.[CR]",
;     "commands" : {
4D21: 09 03     ; "U" : [
4D23: 01 24     ;    "MoveToRoomX","room_36"],
4D25: 00
;     }
; },

; "room_49" : {
;     "desc" : "DEAD_END.[CR]",
;     "commands" : {
4D26: 02 03     ; "E" : [
4D28: 01 34     ;    "MoveToRoomX","room_52"],
4D2A: 00
;     }
; },

; "room_50" : {
;     "desc" : "DEAD_END.[CR]",
;     "commands" : {
4D2B: 02 03     ; "E" : [
4D2D: 01 29     ;    "MoveToRoomX","room_41"],
4D2F: 00
;     }
; },

; "room_51" : {
;     "desc" : "DEAD_END.[CR]",
;     "commands" : {
4D30: 04 03     ; "W" : [
4D32: 01 1D     ;    "MoveToRoomX","room_29"],
4D34: 21 0B     ; "DROP" : [
4D36: 11 29     ;    "AssertObjectXMatchesUserInput","#COINS",
4D38: 15 29 00  ;    "MoveObjectXToRoomY","#COINS","room_0",
4D3B: 18 23     ;    "MoveObjectXToCurrentRoom","#BATTERIES_fresh",
4D3D: 04 58 7C  ;    "PrintMessageX","THERE_ARE_NOW_SOME_FRESH_BATTERIES_HERE.[CR]"],
4D40: 00
;     }
; },

; "room_52" : {
;     "desc" : "YOU_ARE_ON_THE_BRINK_OF_A_LARGE_PIT.__YOU_COULD_CLIMB_DOWN,_BUT_YOU_WOULD_NOT_BE_ABLE_TO_CLIMB_BACK_UP.__THE_MAZE_CONTINUES_ON__THIS_LEVEL.[CR]",
;     "commands" : {
4D41: 01 03     ; "N" : [
4D43: 01 29     ;    "MoveToRoomX","room_41"],
4D45: 02 03     ; "E" : [
4D47: 01 28     ;    "MoveToRoomX","room_40"],
4D49: 03 03     ; "S" : [
4D4B: 01 31     ;    "MoveToRoomX","room_49"],
4D4D: 04 03     ; "W" : [
4D4F: 01 24     ;    "MoveToRoomX","room_36"],
4D51: 0A 03     ; "D" : [
4D53: 01 0B     ;    "MoveToRoomX","room_11"],
4D55: 00
;     }
; },

; "room_53" : {
;     "desc" : "DEAD_END.[CR]",
;     "commands" : {
4D56: 06 03     ; "SE" : [
4D58: 01 28     ;    "MoveToRoomX","room_40"],
4D5A: 00
;     }
; },

; "room_54" : {
;     "desc" : "YOU_ARE_IN_A_DIRTY_BROKEN_PASSAGE.__TO_THE_EAST_IS_A_CRAWL.__TO_THE_WEST_IS_A_LARGE_PASSAGE.__ABOVE_YOU_IS_A_HOLE_TO_ANOTHER____PASSAGE.[CR]",
;     "commands" : {
4D5B: 02 03     ; "E" : [
4D5D: 01 37     ;    "MoveToRoomX","room_55"],
4D5F: 04 03     ; "W" : [
4D61: 01 39     ;    "MoveToRoomX","room_57"],
4D63: 09 03     ; "U" : [
4D65: 01 19     ;    "MoveToRoomX","room_25"],
4D67: 00
;     }
; },

; "room_55" : {
;     "desc" : "YOU_ARE_ON_THE_BRINK_OF_A_SMALL_CLEAN_CLIMBABLE_PIT.__A_CRAWL___LEADS_WEST.[CR]",
;     "commands" : {
4D68: 04 03     ; "W" : [
4D6A: 01 36     ;    "MoveToRoomX","room_54"],
4D6C: 0A 03     ; "D" : [
4D6E: 01 38     ;    "MoveToRoomX","room_56"],
4D70: 11 03     ; "CLIMB" : [
4D72: 01 38     ;    "MoveToRoomX","room_56"],
4D74: 00
;     }
; },

; "room_56" : {
;     "desc" : "YOU_ARE_IN_THE_BOTTOM_OF_A_SMALL_PIT_WITH_A_LITTLE_STREAM,_WHICHENTERS_AND_EXITS_THROUGH_TINY_SLITS.[CR]",
;     "commands" : {
4D75: 09 03     ; "U" : [
4D77: 01 37     ;    "MoveToRoomX","room_55"],
4D79: 0C 03     ; "OUT" : [
4D7B: 01 37     ;    "MoveToRoomX","room_55"],
4D7D: 11 03     ; "CLIMB" : [
4D7F: 01 37     ;    "MoveToRoomX","room_55"],
4D81: 0A 04     ; "D" : [
4D83: 04 7B 72  ;    "PrintMessageX","YOU_DON'T_FIT_THROUGH_TWO-INCH_SLIT![CR]"],
4D86: 27 0B     ; "FILL" : [
4D88: 07 06     ;    "SubScripXtAbortIfPass",[
4D8A: 02 1C     ;        "AssertObjectXIsInPack","#WATER",
4D8C: 04 37 7B  ;        "PrintMessageX","YOUR_BOTTLE_IS_ALREADY_FULL.[CR]"],
4D8F: 19 1C 1B  ;    "MoveObjectXIntoContainerY","#WATER","#BOTTLE"],
4D92: 00
;     }
; },

; "room_57" : {
;     "desc" : "YOU_ARE_IN_A_THE_ROOM_OF_BES,_WHOSE_PICTURE_IS_ON_THE_WALL._____THERE_IS_A_BIG_HOLE_IN_THE_FLOOR.__THERE_IS_A_PASSAGE_LEADING___EAST.[CR]",
;     "commands" : {
4D93: 02 03     ; "E" : [
4D95: 01 36     ;    "MoveToRoomX","room_54"],
4D97: 0A 03     ; "D" : [
4D99: 01 3A     ;    "MoveToRoomX","room_58"],
4D9B: 00
;     }
; },

; "room_58" : {
;     "desc" : "YOU_ARE_AT_A_COMPLEX_JUNCTION.__A_LOW_HANDS_AND_KNEES_PASSAGE___FROM_THE_NORTH_JOINS_A_HIGHER_CRAWL_FROM_THE_EAST_TO_MAKE_A_____WALKING_PASSAGE_GOING_WEST.__THERE_IS_ALSO_A_LARGE_ROOM_ABOVE.__THE_AIR_IS_DAMP_HERE.[CR]",
;     "commands" : {
4D9C: 01 03     ; "N" : [
4D9E: 01 3D     ;    "MoveToRoomX","room_61"],
4DA0: 02 03     ; "E" : [
4DA2: 01 3B     ;    "MoveToRoomX","room_59"],
4DA4: 04 03     ; "W" : [
4DA6: 01 41     ;    "MoveToRoomX","room_65"],
4DA8: 09 03     ; "U" : [
4DAA: 01 39     ;    "MoveToRoomX","room_57"],
4DAC: 11 03     ; "CLIMB" : [
4DAE: 01 39     ;    "MoveToRoomX","room_57"],
4DB0: 00
;     }
; },

; "room_59" : {
;     "desc" : "YOU_ARE_IN_THE_UNDERWORLD_ANTEROOM_OF_SEKER.__PASSAGES_GO_EAST,_WEST,_AND_UP.__HUMAN_BONES_ARE_STREWN_ABOUT_ON_THE_FLOOR._______HIEROGLYPHICS_ON_THE_WALL_ROUGHLY_TRANSLATE_TO_"THOSE_WHO_______PROCEED_EAST_MAY_NEVER_RETURN."[CR]",
;     "commands" : {
4DB1: 02 03     ; "E" : [
4DB3: 01 3C     ;    "MoveToRoomX","room_60"],
4DB5: 04 03     ; "W" : [
4DB7: 01 41     ;    "MoveToRoomX","room_65"],
4DB9: 09 03     ; "U" : [
4DBB: 01 3A     ;    "MoveToRoomX","room_58"],
4DBD: 00
;     }
; },

; "room_60" : {
;     "desc" : "YOU_ARE_AT_THE_LAND_OF_DEAD.__PASSAGES_LEAD_OFF_IN_>ALL<________DIRECTIONS.[CR]",
;     "commands" : {
4DBE: 01 07     ; "N" : [
4DC0: 07 03     ;    "SubScripXtAbortIfPass",[
4DC2: 0A F0     ;        "AssertRandomIsGreaterThanX","240"],
4DC4: 01 3B     ;    "MoveToRoomX","room_59"],
4DC6: 02 07     ; "E" : [
4DC8: 07 03     ;    "SubScripXtAbortIfPass",[
4DCA: 0A F0     ;        "AssertRandomIsGreaterThanX","240"],
4DCC: 01 3B     ;    "MoveToRoomX","room_59"],
4DCE: 03 07     ; "S" : [
4DD0: 07 03     ;    "SubScripXtAbortIfPass",[
4DD2: 0A F0     ;        "AssertRandomIsGreaterThanX","240"],
4DD4: 01 3B     ;    "MoveToRoomX","room_59"],
4DD6: 05 07     ; "NE" : [
4DD8: 07 03     ;    "SubScripXtAbortIfPass",[
4DDA: 0A F0     ;        "AssertRandomIsGreaterThanX","240"],
4DDC: 01 3B     ;    "MoveToRoomX","room_59"],
4DDE: 06 07     ; "SE" : [
4DE0: 07 03     ;    "SubScripXtAbortIfPass",[
4DE2: 0A F0     ;        "AssertRandomIsGreaterThanX","240"],
4DE4: 01 3B     ;    "MoveToRoomX","room_59"],
4DE6: 07 07     ; "SW" : [
4DE8: 07 03     ;    "SubScripXtAbortIfPass",[
4DEA: 0A F0     ;        "AssertRandomIsGreaterThanX","240"],
4DEC: 01 3B     ;    "MoveToRoomX","room_59"],
4DEE: 08 07     ; "NW" : [
4DF0: 07 03     ;    "SubScripXtAbortIfPass",[
4DF2: 0A F0     ;        "AssertRandomIsGreaterThanX","240"],
4DF4: 01 3B     ;    "MoveToRoomX","room_59"],
4DF6: 09 07     ; "U" : [
4DF8: 07 03     ;    "SubScripXtAbortIfPass",[
4DFA: 0A F0     ;        "AssertRandomIsGreaterThanX","240"],
4DFC: 01 3B     ;    "MoveToRoomX","room_59"],
4DFE: 04 06     ; "W" : [
4E00: 04 CF 72  ;    "PrintMessageX","YOU_HAVE_CRAWLED_AROUND_IN_SOME_LITTLE_HOLES_AND_FOUND_YOUR_WAY_BLOCKED_BY_A_FALLEN_SLAB.__YOU_ARE_NOW_BACK_IN_THE_MAIN_PASSAGE.[CR]",
4E03: 01 3C     ;    "MoveToRoomX","room_60"],
4E05: 00
;     }
; },

; "room_61" : {
;     "desc" : "YOU'RE_IN_A_LARGE_ROOM_WITH_ANCIENT_DRAWINGS_ON_ALL_WALLS.______THE_PICTURES_DEPICT_ATUM,_A_PHARAOH_WEARING_THE_DOUBLE_CROWN.___A_SHALLOW_PASSAGE_PROCEEDS_DOWNWARD,_AND_A_SOMEWHAT_STEEPER_ONE_LEADS_UP.__A_LOW_HANDS_AND_KNEES_PASSAGE_ENTERS_FROM_THE_SOUTH. [CR]",
;     "commands" : {
4E06: 03 11     ; "S" : [
4E08: 07 06     ;    "SubScripXtAbortIfPass",[
4E0A: 02 17     ;        "AssertObjectXIsInPack","#SARCOPH_full",
4E0C: 04 27 73  ;        "PrintMessageX","YOU_CAN'T_FIT_THIS_BIG_SARCOPHAGUS_THROUGH_THAT_LITTLE_PASSAGE![CR]"],
4E0F: 07 06     ;    "SubScripXtAbortIfPass",[
4E11: 02 18     ;        "AssertObjectXIsInPack","#SARCOPH_empty",
4E13: 04 27 73  ;        "PrintMessageX","YOU_CAN'T_FIT_THIS_BIG_SARCOPHAGUS_THROUGH_THAT_LITTLE_PASSAGE![CR]"],
4E16: 01 3A     ;    "MoveToRoomX","room_58"],
4E18: 09 03     ; "U" : [
4E1A: 01 3E     ;    "MoveToRoomX","room_62"],
4E1C: 0A 03     ; "D" : [
4E1E: 01 3F     ;    "MoveToRoomX","room_63"],
4E20: 00
;     }
; },

; "room_62" : {
;     "desc" : "YOU_ARE_IN_A_CHAMBER_WHOSE_WALL_CONTAINS_A_PICTURE_OF_A_MAN_____WEARING_THE_LUNAR_DISK_ON_HIS_HEAD.__HE_IS_THE_GOD_KHONS,_THE___MOON_GOD.[CR]",
;     "commands" : {
4E21: 0A 03     ; "D" : [
4E23: 01 3D     ;    "MoveToRoomX","room_61"],
4E25: 0C 03     ; "OUT" : [
4E27: 01 3D     ;    "MoveToRoomX","room_61"],
4E29: 00
;     }
; },

; "room_63" : {
;     "desc" : "YOU_ARE_IN_A_LONG_SLOPING_CORRIDOR_WITH_RAGGED_WALLS._ [CR]",
;     "commands" : {
4E2A: 09 03     ; "U" : [
4E2C: 01 3D     ;    "MoveToRoomX","room_61"],
4E2E: 0A 03     ; "D" : [
4E30: 01 40     ;    "MoveToRoomX","room_64"],
4E32: 00
;     }
; },

; "room_64" : {
;     "desc" : "YOU_ARE_IN_A_CUL-DE-SAC_ABOUT_EIGHT_FEET_ACROSS.[CR]",
;     "commands" : {
4E33: 09 03     ; "U" : [
4E35: 01 3F     ;    "MoveToRoomX","room_63"],
4E37: 0C 03     ; "OUT" : [
4E39: 01 3F     ;    "MoveToRoomX","room_63"],
4E3B: 00
;     }
; },

; "room_65" : {
;     "desc" : "YOU_ARE_IN_THE_CHAMBER_OF_HORUS,_A_LONG_EAST/WEST_PASSAGE_WITH__HOLES_EVERYWHERE.__TO_EXPLORE_AT_RANDOM,_SELECT_NORTH,_SOUTH,___UP,_OR_DOWN.[CR]",
;     "commands" : {
4E3C: 02 03     ; "E" : [
4E3E: 01 3A     ;    "MoveToRoomX","room_58"],
4E40: 04 03     ; "W" : [
4E42: 01 4E     ;    "MoveToRoomX","room_78"],
4E44: 09 07     ; "U" : [
4E46: 07 03     ;    "SubScripXtAbortIfPass",[
4E48: 0A CC     ;        "AssertRandomIsGreaterThanX","204"],
4E4A: 01 48     ;    "MoveToRoomX","room_72"],
4E4C: 01 07     ; "N" : [
4E4E: 07 03     ;    "SubScripXtAbortIfPass",[
4E50: 0A CC     ;        "AssertRandomIsGreaterThanX","204"],
4E52: 01 49     ;    "MoveToRoomX","room_73"],
4E54: 03 07     ; "S" : [
4E56: 07 03     ;    "SubScripXtAbortIfPass",[
4E58: 0A CC     ;        "AssertRandomIsGreaterThanX","204"],
4E5A: 01 42     ;    "MoveToRoomX","room_66"],
4E5C: 0A 07     ; "D" : [
4E5E: 07 03     ;    "SubScripXtAbortIfPass",[
4E60: 0A CC     ;        "AssertRandomIsGreaterThanX","204"],
4E62: 01 3B     ;    "MoveToRoomX","room_59"],
4E64: 00
;     }
; },

; "room_66" : {
;     "desc" : "YOU_ARE_IN_A_LARGE_LOW_CIRCULAR_CHAMBER_WHOSE_FLOOR_IS_AN_______IMMENSE_SLAB_FALLEN_FROM_THE_CEILING.__EAST_AND_WEST_THERE_ONCE_WHERE_LARGE_PASSAGES,_BUT_THEY_ARE_NOW_FILLED_WITH_SAND.________LOW_SMALL_PASSAGES_GO_NORTH_AND_SOUTH.[CR]",
;     "commands" : {
4E65: 01 03     ; "N" : [
4E67: 01 41     ;    "MoveToRoomX","room_65"],
4E69: 03 03     ; "S" : [
4E6B: 01 50     ;    "MoveToRoomX","room_80"],
4E6D: 00
;     }
; },

; "room_72" : {
;     "desc" : "YOU_ARE_IN_THE_PRIEST'S_BEDROOM.__THE_WALLS_ARE_COVERED_WITH____CURTAINS,_THE_FLOOR_WITH_A_THICK_PILE_CARPET.__MOSS_COVERS_THE__CEILING.[CR]",
;     "commands" : {
4E6E: 04 03     ; "W" : [
4E70: 01 41     ;    "MoveToRoomX","room_65"],
4E72: 0C 03     ; "OUT" : [
4E74: 01 41     ;    "MoveToRoomX","room_65"],
4E76: 00
;     }
; },

; "room_73" : {
;     "desc" : "THIS_IS_THE_CHAMBER_OF_THE_HIGH_PRIEST.___ANCIENT_DRAWINGS_COVERTHE_WALLS.__AN_EXTREMELY_TIGHT_TUNNEL_LEADS_WEST.__IT_LOOKS_LIKEA_TIGHT_SQUEEZE.__ANOTHER_PASSAGE_LEADS_SE.[CR]",
;     "commands" : {
4E77: 04 09     ; "W" : [
4E79: 07 04     ;    "SubScripXtAbortIfPass",[
4E7B: 0D        ;        "AssertPackIsEmptyExceptForEmerald",
4E7C: 01 4C     ;        "MoveToRoomX","room_76"],
4E7E: 04 53 73  ;    "PrintMessageX","SOMETHING_YOU'RE_CARRYING_WON'T_FIT_THROUGH_THE_TUNNEL_WITH_YOU.YOU'D_BEST_TAKE_INVENTORY_AND_DROP_SOMETHING.[CR]"],
4E81: 06 03     ; "SE" : [
4E83: 01 41     ;    "MoveToRoomX","room_65"],
4E85: 00
;     }
; },

; "room_76" : {
;     "desc" : "YOU_ARE_IN_THE_HIGH_PRIEST'S_TREASURE_ROOM_LIT_BY_AN_EERIE_GREENLIGHT.__A_NARROW_TUNNEL_EXITS_TO_THE_EAST.[CR]",
;     "commands" : {
4E86: 02 09     ; "E" : [
4E88: 07 04     ;    "SubScripXtAbortIfPass",[
4E8A: 0D        ;        "AssertPackIsEmptyExceptForEmerald",
4E8B: 01 49     ;        "MoveToRoomX","room_73"],
4E8D: 04 53 73  ;    "PrintMessageX","SOMETHING_YOU'RE_CARRYING_WON'T_FIT_THROUGH_THE_TUNNEL_WITH_YOU.YOU'D_BEST_TAKE_INVENTORY_AND_DROP_SOMETHING.[CR]"],
4E90: 0C 09     ; "OUT" : [
4E92: 07 04     ;    "SubScripXtAbortIfPass",[
4E94: 0D        ;        "AssertPackIsEmptyExceptForEmerald",
4E95: 01 49     ;        "MoveToRoomX","room_73"],
4E97: 04 53 73  ;    "PrintMessageX","SOMETHING_YOU'RE_CARRYING_WON'T_FIT_THROUGH_THE_TUNNEL_WITH_YOU.YOU'D_BEST_TAKE_INVENTORY_AND_DROP_SOMETHING.[CR]"],
4E9A: 00
;     }
; },

; "room_78" : {
;     "desc" : "YOU_ARE_AT_THE_EAST_END_OF_THE_TWOPIT_ROOM.__THE_FLOOR_HERE_IS__LITTERED_WITH_THIN_ROCK_SLABS,_WHICH_MAKE_IT_EASY_TO_DESCEND_THEPITS.__THERE_IS_A_PATH_HERE_BYPASSING_THE_PITS_TO_CONNECT_______PASSAGES_EAST_AND_WEST.__THERE_ARE_HOLES_ALL_OVER,_BUT_THE_ONLY_BIG_ONE_IS_ON_THE_WALL_DIRECTLY_OVER_THE_WEST_PIT_WHERE_YOU_____CAN'T_GET_TO_IT.[CR]",
;     "commands" : {
4E9B: 02 03     ; "E" : [
4E9D: 01 41     ;    "MoveToRoomX","room_65"],
4E9F: 04 03     ; "W" : [
4EA1: 01 50     ;    "MoveToRoomX","room_80"],
4EA3: 0A 03     ; "D" : [
4EA5: 01 4F     ;    "MoveToRoomX","room_79"],
4EA7: 00
;     }
; },

; "room_79" : {
;     "desc" : "YOU_ARE_AT_THE_BOTTOM_OF_THE_EASTERN_PIT_IN_THE_TWOPIT_ROOM.[CR]",
;     "commands" : {
4EA8: 09 03     ; "U" : [
4EAA: 01 4E     ;    "MoveToRoomX","room_78"],
4EAC: 0C 03     ; "OUT" : [
4EAE: 01 4E     ;    "MoveToRoomX","room_78"],
4EB0: 00
;     }
; },

; "room_80" : {
;     "desc" : "YOU_ARE_AT_THE_WEST_END_OF_THE_TWOPIT_ROOM.__THERE_IS_A_LARGE___HOLE_IN_THE_WALL_ABOVE_THE_PIT_AT_THIS_END_OF_THE_ROOM.[CR]",
;     "commands" : {
4EB1: 02 03     ; "E" : [
4EB3: 01 4E     ;    "MoveToRoomX","room_78"],
4EB5: 04 03     ; "W" : [
4EB7: 01 42     ;    "MoveToRoomX","room_66"],
4EB9: 0A 03     ; "D" : [
4EBB: 01 51     ;    "MoveToRoomX","room_81"],
4EBD: 00
;     }
; },

; "room_81" : {
;     "desc" : "YOU_ARE_AT_THE_BOTTOM_OF_THE_WEST_PIT_IN_THE_TWOPIT_ROOM.__THEREIS_A_LARGE_HOLE_IN_THE_WALL_ABOUT_TWENTY_FIVE_FEET_ABOVE_YOU.[CR]",
;     "commands" : {
4EBE: 09 03     ; "U" : [
4EC0: 01 50     ;    "MoveToRoomX","room_80"],
4EC2: 0C 03     ; "OUT" : [
4EC4: 01 50     ;    "MoveToRoomX","room_80"],
4EC6: 11 16     ; "CLIMB" : [
4EC8: 07 08     ;    "SubScripXtAbortIfPass",[
4ECA: 03 09     ;        "AssertObjectXIsInCurrentRoomOrPack","#PLANT_C",
4ECC: 04 9E 73  ;        "PrintMessageX","YOU_CLAMBER_UP_THE_PLANT_AND_SCURRY_THROUGH_THE_HOLE_AT_THE_TOP.[CR]",
4ECF: 01 4D     ;        "MoveToRoomX","room_77"],
4ED1: 07 06     ;    "SubScripXtAbortIfPass",[
4ED3: 03 08     ;        "AssertObjectXIsInCurrentRoomOrPack","#PLANT_B",
4ED5: 04 CB 73  ;        "PrintMessageX","YOU'VE_CLIMBED_UP_THE_PLANT_AND_OUT_OF_THE_PIT.[CR]"],
4ED8: 01 50     ;    "MoveToRoomX","room_80",
4EDA: 04 7D 7D  ;    "PrintMessageX","THERE_IS_NOTHING_HERE_TO_CLIMB.__USE_UP_OR_OUT_TO_LEAVE_THE_PIT.[CR]"],
4EDD: 24 2F     ; "POUR" : [
4EDF: 11 1C     ;    "AssertObjectXMatchesUserInput","#WATER",
4EE1: 15 1C 00  ;    "MoveObjectXToRoomY","#WATER","room_0",
4EE4: 07 0E     ;    "SubScripXtAbortIfPass",[
4EE6: 03 07     ;        "AssertObjectXIsInCurrentRoomOrPack","#PLANT_A",
4EE8: 15 07 00  ;        "MoveObjectXToRoomY","#PLANT_A","room_0",
4EEB: 18 08     ;        "MoveObjectXToCurrentRoom","#PLANT_B",
4EED: 04 02 7D  ;        "PrintMessageX","THE_PLANT_SPURTS_INTO_FURIOUS_GROWTH_FOR_A_FEW_SECONDS.[CR]",
4EF0: 04 71 6E  ;        "PrintMessageX","THERE_IS_A_TWELVE_FOOT_BEAN_STALK_STRETCHING_UP_OUT_OF_THE_PIT,_BELLOWING_"WATER..._WATER..."[CR]"],
4EF3: 07 0E     ;    "SubScripXtAbortIfPass",[
4EF5: 03 08     ;        "AssertObjectXIsInCurrentRoomOrPack","#PLANT_B",
4EF7: 15 08 00  ;        "MoveObjectXToRoomY","#PLANT_B","room_0",
4EFA: 18 09     ;        "MoveObjectXToCurrentRoom","#PLANT_C",
4EFC: 04 29 7D  ;        "PrintMessageX","THE_PLANT_GROWS_EXPLOSIVELY,_ALMOST_FILLING_THE_BOTTOM_OF_THE___PIT.[CR]",
4EFF: 04 B1 6E  ;        "PrintMessageX","THERE_IS_A_GIGANTIC_BEAN_STALK_STRETCHING_ALL_THE_WAY_UP_TO_THE_HOLE.[CR]"],
4F02: 15 09 00  ;    "MoveObjectXToRoomY","#PLANT_C","room_0",
4F05: 18 07     ;    "MoveObjectXToCurrentRoom","#PLANT_A",
4F07: 04 59 7D  ;    "PrintMessageX","YOU'VE_OVER-WATERED_THE_PLANT!__IT'S_SHRIVELING_UP![CR]",
4F0A: 04 45 6E  ;    "PrintMessageX","THERE_IS_A_TINY_PLANT_IN_THE_PIT,_MURMURING_"WATER,_WATER,_..."[CR]"],
4F0D: 00
;     }
; },

; "room_77" : {
;     "desc" : "YOU_ARE_IN_A_LONG,_NARROW_CORRIDOR_STRETCHING_OUT_OF_SIGHT_TO___THE_WEST.__AT_THE_EASTERN_END_IS_A_HOLE_THROUGH_WHICH_YOU_CAN___SEE_A_PROFUSION_OF_LEAVES.[CR]",
;     "commands" : {
4F0E: 02 03     ; "E" : [
4F10: 01 51     ;    "MoveToRoomX","room_81"],
4F12: 0A 03     ; "D" : [
4F14: 01 51     ;    "MoveToRoomX","room_81"],
4F16: 11 03     ; "CLIMB" : [
4F18: 01 51     ;    "MoveToRoomX","room_81"],
4F1A: 10 05     ; "JUMP" : [
4F1C: 04 71 71  ;    "PrintMessageX","YOU_ARE_AT_THE_BOTTOM_OF_THE_PIT_WITH_A_BROKEN_NECK.[CR]",
4F1F: 05        ;    "PrintScoreAndStop"],
4F20: 04 03     ; "W" : [
4F22: 01 47     ;    "MoveToRoomX","room_71"],
4F24: 00
;     }
; },

; "room_71" : {
;     "desc" : "YOU_ARE_IN_THE_CHAMBER_OF_OSIRIS._THE_CEILING_IS_TOO_HIGH_UP_FORYOUR_LAMP_TO_SHOW_IT.__PASSAGES_LEAD_EAST,_NORTH,_AND_SOUTH.[CR]",
;     "commands" : {
4F25: 01 03     ; "N" : [
4F27: 01 44     ;    "MoveToRoomX","room_68"],
4F29: 02 03     ; "E" : [
4F2B: 01 46     ;    "MoveToRoomX","room_70"],
4F2D: 03 03     ; "S" : [
4F2F: 01 4D     ;    "MoveToRoomX","room_77"],
4F31: 00
;     }
; },

; "room_70" : {
;     "desc" : "THE_PASSAGE_HERE_IS_BLOCKED_BY_A_FALLEN_BLOCK.[CR]",
;     "commands" : {
4F32: 03 03     ; "S" : [
4F34: 01 47     ;    "MoveToRoomX","room_71"],
4F36: 0C 03     ; "OUT" : [
4F38: 01 47     ;    "MoveToRoomX","room_71"],
4F3A: 00
;     }
; },

; "room_68" : {
;     "desc" : "YOU_ARE_IN_THE_CHAMBER_OF_NEKHEBET,_A_WOMAN_WITH_THE_HEAD_OF_A__VULTURE,_WEARING_THE_CROWN_OF_EGYPT.__A_PASSAGE_EXITS_TO_THE____SOUTH.[CR]",
;     "commands" : {
4F3B: 03 03     ; "S" : [
4F3D: 01 47     ;    "MoveToRoomX","room_71"],
4F3F: 0C 03     ; "OUT" : [
4F41: 01 47     ;    "MoveToRoomX","room_71"],
4F43: 00
;     }
; },
        
4F44: FF          
```

# Ambient Light Table 

```code
; 2 bytes per room
; * 0x4000 means there is light in the room (no need for a lamp)
; * 0x0000 means you better have a lamp

AmbientLight: 
4F45:   40 00  ;  1
4F47:   40 00  ;  2
4F49:   40 00  ;  3
4F4B:   40 00  ;  4
4F4D:   40 00  ;  5
4F4F:   40 00  ;  6
4F51:   40 00  ;  7
4F53: 00 00    ;  8
4F55: 00 00    ;  9
4F57: 00 00    ;  10
4F59: 00 00    ;  11
4F5B: 00 00    ;  12
4F5D: 00 00    ;  13
4F5F: 00 00    ;  14
4F61: 00 00    ;  15
4F63: 00 00    ;  16
4F65: 00 00    ;  17
4F67: 00 00    ;  18
4F69: 00 00    ;  19
4F6B: 00 00    ;  20
4F6D: 00 00    ;  21
4F6F: 00 00    ;  22
4F71: 00 00    ;  23
4F73: 00 00    ;  24
4F75: 00 00    ;  25
4F77: 00 00    ;  26
4F79: 00 00    ;  27
4F7B: 00 00    ;  28
4F7D: 00 00    ;  29
4F7F: 00 00    ;  30
4F81: 00 00    ;  31
4F83: 00 00    ;  32
4F85: 00 00    ;  33
4F87: 00 00    ;  34
4F89: 00 00    ;  35
4F8B: 00 00    ;  36
4F8D: 00 00    ;  37
4F8F: 00 00    ;  38
4F91: 00 00    ;  39
4F93: 00 00    ;  40
4F95: 00 00    ;  41
4F97: 00 00    ;  42
4F99: 00 00    ;  43
4F9B: 00 00    ;  44
4F9D: 00 00    ;  45
4F9F: 00 00    ;  46
4FA1: 00 00    ;  47
4FA3: 00 00    ;  48
4FA5: 00 00    ;  49
4FA7: 00 00    ;  50
4FA9: 00 00    ;  51
4FAB: 00 00    ;  52
4FAD: 00 00    ;  53
4FAF: 00 00    ;  54
4FB1: 00 00    ;  55
4FB3: 00 00    ;  56
4FB5: 00 00    ;  57
4FB7: 00 00    ;  58
4FB9: 00 00    ;  59
4FBB: 00 00    ;  60
4FBD: 00 00    ;  61
4FBF: 00 00    ;  62
4FC1: 00 00    ;  63
4FC3: 00 00    ;  64
4FC5: 00 00    ;  65
4FC7: 00 00    ;  66
4FC9: 00 00    ;  67
4FCB: 00 00    ;  68
4FCD: 00 00    ;  69
4FCF: 00 00    ;  70
4FD1: 00 00    ;  71
4FD3: 00 00    ;  72
4FD5: 00 00    ;  73
4FD7: 00 00    ;  74
4FD9: 00 00    ;  75
4FDB:   40 00  ;  76
4FDD: 00 00    ;  77
4FDF: 00 00    ;  78
4FE1: 00 00    ;  79
4FE3: 00 00    ;  80
4FE5: 00 00    ;  81
```

# Object Data

```code
; This two-byte table contains the object's attributes ("isTreasure" and "isGettable") 
; and the object's current location (a room or inside another object).
;
; The code references the objects by numeric id, but I have given them unique names 
; in the table below. All object names begin with "#". All word names begin with "_".
;
; The format of the two bytes are:
;
;   MCT----- RRRRRRRR
;
;   M - if set, the second byte is an object number (container). if clear, the second byte is a room number.[[br]] 
;   C - if set, object can be picked up.[[br]]
;   T - if set, object is treasure.
;
;   RRRRRRRR - Second byte is the object's location (containing object or room number).

ObjectData:
; Object data table (2 bytes)
;              MCT              # Name             Start location                  
4FE7: 00              NOP                         
4FE8: 00              NOP                         
4FE9: 00              NOP                         
4FEA: 00              NOP                         
4FEB: 00              NOP                         
4FEC: 00              NOP                         
4FED: 00              NOP                         
4FEE: 00              NOP                         
4FEF: 00              NOP                         
4FF0: 00              NOP                         
4FF1: 00              NOP                         
4FF2: 33              INC     SP                  
4FF3: 00              NOP                         
4FF4: 51              LD      D,C                 
4FF5: 00              NOP                         
4FF6: 00              NOP                         
4FF7: 00              NOP                         
4FF8: 00              NOP                         
4FF9: 00              NOP                         
4FFA: 00              NOP                         
4FFB: 00              NOP                         
4FFC: 10 00           DJNZ    $4FFE               ; {}
4FFE: 00              NOP                         
4FFF: 00              NOP                         
5000: 00              NOP                         
5001: 40              LD      B,B                 
5002: 02              LD      (BC),A              
5003: 40              LD      B,B                 
5004: 00              NOP                         
5005: 40              LD      B,B                 
5006: 08              EX      AF,AF'              
5007: 40              LD      B,B                 
5008: 09              ADD     HL,BC               
5009: 40              LD      B,B                 
500A: 48              LD      C,B                 
500B: 40              LD      B,B                 
500C: 0B              DEC     BC                  
500D: 00              NOP                         
500E: 00              NOP                         
500F: 00              NOP                         
5010: 00              NOP                         
5011: 60              LD      H,B                 
5012: 00              NOP                         
5013: 40              LD      B,B                 
5014: 3D              DEC     A                   
5015: 40              LD      B,B                 
5016: 00              NOP                         
5017: 40              LD      B,B                 
5018: 3B              DEC     SP                  
5019: 40              LD      B,B                 
501A: 02              LD      (BC),A              
501B: 40              LD      B,B                 
501C: 02              LD      (BC),A              
501D: C0              RET     NZ                  
501E: 1B              DEC     DE                  
501F: 00              NOP                         
5020: 00              NOP                         
5021: 00              NOP                         
5022: 38 60           JR      C,$5084             ; {}
5024: 4C              LD      C,H                 
5025: 60              LD      H,B                 
5026: 00              NOP                         
5027: 60              LD      H,B                 
5028: 49              LD      C,C                 
5029: 60              LD      H,B                 
502A: 44              LD      B,H                 
502B: 40              LD      B,B                 
502C: 00              NOP                         
502D: 40              LD      B,B                 
502E: 00              NOP                         
502F: 60              LD      H,B                 
5030: 0E 60           LD      C,$60               
5032: 11 60 19        LD      DE,$1960            
5035: 60              LD      H,B                 
5036: 12              LD      (DE),A              
5037: 60              LD      H,B                 
5038: 18 60           JR      $509A               ; {}
503A: 00              NOP                         
503B: 60              LD      H,B                 
503C: 47              LD      B,A                 
503D: 40              LD      B,B                 
503E: 00              NOP                         
```

# Game Variables                      

```code
GameVariables:
503F: 01 00 00        LD      BC,$0000            
5042: 00              NOP                         
5043: 00              NOP                         
5044: 00              NOP                         
5045: 00              NOP                         
5046: 00              NOP                         
```

# Object Table

```code
ObjectDescriptions:
; Object descriptions (44 objects)
; For packable objects each slot points to a message pair. The first is the long
; description and the second is the short (if any).
;                  # Name              Description
5047: 58 6D     ;  1 #bridge_15        Stone bridge room 15      
5049: 58 6D     ;  2 #bridge_18        Stone bridge room 18
504B:   C0 47   ;  3                   -Never used         
504D:   C0 47   ;  4                   -Never used
504F:   C0 47   ;  5                   -Never used
5051: E1 6E     ;  6 #MACHINE          Vending Machine
5053: 45 6E     ;  7 #PLANT_A          Tiny plant
5055: 71 6E     ;  8 #PLANT_B          Twelve foot beanstalk    
5057: B1 6E     ;  9 #PLANT_C          Giant beanstalk  
5059:   00 00   ; 10                   Used in error message ... I think I just lost my appetite            
505B: 3A 6D     ; 11 #SERPENT          Serpent bars the way
505D:   00 00   ; 12                   -Never used               
505F: 00 00     ; 13                   Used in error message ... there is nothing here it wants to eat except you
5061: 2E 6C     ; 14 #LAMP_off         Lamp (not lit)   
5063: 53 6C     ; 15 #LAMP_on          Lamp (lit) 
5065: 75 6C     ; 16 #BOX              Statue box
5067: 9E 6C     ; 17 #SCEPTER          Scepter
5069: 12 6D     ; 18 #PILLOW           Pillow
506B: CD 6C     ; 19 #BIRD             Statue
506D: EB 6C     ; 20 #BIRD_boxed       Statue in box 
506F: ED 70     ; 21 #POTTERY          Pottery
5071: 47 71     ; 22 #PEARL            Pearl
5073: 78 6D     ; 23 #SARCOPH_full     Sarcophagus with pearl
5075: 78 6D     ; 24 #SARCOPH_empty    Sarcophagus empty
5077: B1 6D     ; 25 #MAGAZINES        Magazines   
5079: EC 6D     ; 26 #FOOD             Food
507B: 04 6E     ; 27 #BOTTLE           Bottle 
507D: 20 6E     ; 28 #WATER            Water in the bottle
507F:   C0 47   ; 29                   Not in a room, never referenced       
5081:   C0 47   ; 30 #STREAM_56        Stream in room 56  
5083: 14 71     ; 31 #EMERALD          Emerald    
5085: C5 70     ; 32 #VASE_pillow      Vase on pillow     
5087: A2 70     ; 33 #VASE_solo        Vase    
5089: 7E 70     ; 34 #KEY              Key   
508B: 30 6F     ; 35 #BATTERIES_fresh  Batteries
508D: 4F 6F     ; 36 #BATTERIES_worn   Worn-out batteries      
508F: 7B 6F     ; 37 #GOLD             Gold Nugget       
5091: AB 6F     ; 38 #DIAMNODS         Diamonds     
5093: CA 6F     ; 39 #SILVER           Silver
5095: EA 6F     ; 40 #JEWELRY          Jewelry      
5097: 0E 70     ; 41 #COINS            Coins    
5099: 2B 70     ; 42 #CHEST            Chest   
509B: 52 70     ; 43 #NEST             Nest of golden eggs  
509D: 2E 6C     ; 44 #LAMP_dead        Lamp (dead)
```

# Script Commands 

```code
; This lookup table holds the pointers to the individual script commands. Each command 
; reads 1 or 2 bytes of data from the script. The number of extra bytes read is show 
; for reference in the table.
;
; Script Command Table
; *   b = 2 bytes ... message address
; *   c = 1 byte  ... object number
; *   d = 1 byte  ... room number
; *   e = 2 bytes ... target object and container object 
; *   f = 2 bytes ... target object and room number

ScriptCommands:
;    Address   Number Bytes Type Name
509F: 8A 51   ;   1     1    d   MoveToRoomX           
50A1: C8 52   ;   2     1    c   AssertObjectXIsInPack
50A3: D7 52   ;   3     1    c   AssertObjectXIsInCurrentRoomOrPack
50A5: 5E 53   ;   4     2    b   PrintMessageX
50A7: 49 54   ;   5     0        PrintScoreAndStop
50A9: 00 00   ;   6     -        
50AB: C2 43   ;   7     1    *   SubScripXtAbortIfPass 
50AD: C7 54   ;   8     0        PrintScore
50AF: EF 55   ;   9     0        PrintScoreAndStop
50B1: 18 53   ;  10     1        AssertRandomIsGreaterThanX
50B3: 6B 53   ;  11     1    c   DropObjectX
50B5: 32 53   ;  12     1    d   MoveToRoomXIfItWasLastRoom
50B7: FB 52   ;  13     0        AssertPackIsEmptyExceptForEmerald
50B9: 81 53   ;  14     0        MoveToLastRoom
50BB: 9B 53   ;  15     0        PrintInventory    
50BD: DB 53   ;  16     0        PrintRoomDescription
50BF: E1 53   ;  17     1    c   AssertObjectXMatchesUserInput
50C1: EF 53   ;  18     1    c   GetObjectFromRoom
50C3: 00 00   ;  19     -        
50C5: 2B 54   ;  20     0        PrintOK 
50C7: 34 54   ;  21     2    f   MoveObjectXToRoomY
50C9: 43 53   ;  22     0        GetUserInputObject
50CB: 24 54   ;  23     0        DropUserInputObject
50CD: A5 52   ;  24     1    c   MoveObjectXToCurrentRoom
50CF: B3 52   ;  25     2    e   MoveObjectXIntoContainerY
50D1: EA 52   ;  26     1    c   AssertObjectXIsInCurrentRoom
50D3: F5 55   ;  27     0        LoadGame  
50D5: 54 56   ;  28     0        SaveGame 
50D7: 94 56   ;  29     0        RandomizeDirections
```

# After Every Step 

```code
; This processing takes place after every user input.[[br]]
;  1. Increment the count on the lamp and the number of turns.[[br]]
;  2.  Warn the player if the lamp is going dim and change the batteries automatically.
     
50D9: 3E 0F           LD      A,$0F               
50DB: 21 E7 4F        LD      HL,$4FE7            
50DE: CD 61 43        CALL    $4361               ; {}
50E1: 23              INC     HL                  
50E2: 7E              LD      A,(HL)              
50E3: A7              AND     A                   
50E4: CA 34 51        JP      Z,$5134             ; {}
50E7: 2A 42 50        LD      HL,($5042)          ; {}
50EA: 23              INC     HL                  
50EB: 22 42 50        LD      ($5042),HL          ; {}
50EE: 7C              LD      A,H                 
50EF: FE 01           CP      $01                 
50F1: C2 34 51        JP      NZ,$5134            ; {}
50F4: 7D              LD      A,L                 
50F5: FE 22           CP      $22                 
50F7: C2 03 51        JP      NZ,$5103            ; {}
50FA: 21 C5 79        LD      HL,$79C5            
50FD: CD AE 45        CALL    $45AE               ; {code.PrintPacked}
5100: C3 77 51        JP      $5177               ; {}
5103: FE 36           CP      $36                 
5105: C2 34 51        JP      NZ,$5134            ; {}
5108: 3E 0F           LD      A,$0F               
510A: 21 E7 4F        LD      HL,$4FE7            
510D: CD 61 43        CALL    $4361               ; {}
5110: 23              INC     HL                  
5111: 46              LD      B,(HL)              
5112: 36 00           LD      (HL),$00            
5114: 21 E7 4F        LD      HL,$4FE7            
5117: 3E 2C           LD      A,$2C               
5119: CD 61 43        CALL    $4361               ; {}
511C: 23              INC     HL                  
511D: 70              LD      (HL),B              
511E: 3E 23           LD      A,$23               
5120: 1E FF           LD      E,$FF               
5122: CD 50 43        CALL    $4350               ; {code.GetObjectInfo}
5125: CA 34 51        JP      Z,$5134             ; {}
5128: 21 4A 7A        LD      HL,$7A4A            
512B: CD AE 45        CALL    $45AE               ; {code.PrintPacked}
512E: CD 45 52        CALL    $5245               ; {}
5131: C3 77 51        JP      $5177               ; {}
5134: 2A 42 50        LD      HL,($5042)          ; {}
5137: 11 2C 01        LD      DE,$012C            
513A: 7C              LD      A,H                 
513B: BA              CP      D                   
513C: DA 77 51        JP      C,$5177             ; {}
513F: 7D              LD      A,L                 
5140: BB              CP      E                   
5141: DA 77 51        JP      C,$5177             ; {}
5144: 3E 23           LD      A,$23               
5146: 1E FF           LD      E,$FF               
5148: CD 50 43        CALL    $4350               ; {code.GetObjectInfo}
514B: C2 77 51        JP      NZ,$5177            ; {}
514E: 3E 2C           LD      A,$2C               
5150: 1E FF           LD      E,$FF               
5152: CD 50 43        CALL    $4350               ; {code.GetObjectInfo}
5155: C2 77 51        JP      NZ,$5177            ; {}
5158: 23              INC     HL                  
5159: 36 00           LD      (HL),$00            
515B: 3E 23           LD      A,$23               
515D: 21 E7 4F        LD      HL,$4FE7            
5160: CD 61 43        CALL    $4361               ; {}
5163: 23              INC     HL                  
5164: 36 00           LD      (HL),$00            
5166: 23              INC     HL                  
5167: 23              INC     HL                  
5168: 36 FF           LD      (HL),$FF            
516A: 1E FF           LD      E,$FF               
516C: 3E 0F           LD      A,$0F               
516E: CD 76 43        CALL    $4376               ; {}
5171: 21 91 7A        LD      HL,$7A91            
5174: CD AE 45        CALL    $45AE               ; {code.PrintPacked}
5177: 3A 40 50        LD      A,($5040)           ; {}
517A: C6 01           ADD     $01                 
517C: 27              DAA                         
517D: 32 40 50        LD      ($5040),A           ; {}
5180: 3A 41 50        LD      A,($5041)           ; {}
5183: CE 00           ADC     $00                 
5185: 27              DAA                         
5186: 32 41 50        LD      ($5041),A           ; {}
5189: C9              RET                         
```

# Command 1: Move To Room X 

```code
; This routine moves the player to a new room. If there is light in the new room or light 
; in the old room then the move always works. Otherwise there is a 60% chance the move kills you.
;
; If there is light in the new room then the room description is printed.
;
; After every move the code checks the pack for treasures. If there are 2 or more treasures then 
; the Mummy moves them all to room 53 (the hard-to-find room in the maze). Then the code moves the 
; chest to room 53. Up till now the chest has been in room 0 (out of play). The only way to make the 
; chest appear in the maze is to encounter the Mummy!
;
; Once the chest is in a room (any room) the Mummy no longer appears. You only see the Mummy once.

MoveToRoomX:
518A: E1              POP     HL                  
518B: 46              LD      B,(HL)              
518C: 23              INC     HL                  
518D: E5              PUSH    HL                  
518E: 3A 3F 50        LD      A,($503F)           ; {ram.CurrentRoom}
5191: 5F              LD      E,A                 
5192: 3E 0F           LD      A,$0F               
5194: CD 50 43        CALL    $4350               ; {code.GetObjectInfo}
5197: CA DA 51        JP      Z,$51DA             ; {}
519A: 1E FF           LD      E,$FF               
519C: 3E 0F           LD      A,$0F               
519E: CD 50 43        CALL    $4350               ; {code.GetObjectInfo}
51A1: CA DA 51        JP      Z,$51DA             ; {}
51A4: 21 45 4F        LD      HL,$4F45            
51A7: 3A 3F 50        LD      A,($503F)           ; {ram.CurrentRoom}
51AA: CD 61 43        CALL    $4361               ; {}
51AD: 7E              LD      A,(HL)              
51AE: E6 40           AND     $40                 
51B0: C2 DA 51        JP      NZ,$51DA            ; {}
51B3: 78              LD      A,B                 
51B4: 21 45 4F        LD      HL,$4F45            
51B7: CD 61 43        CALL    $4361               ; {}
51BA: 7E              LD      A,(HL)              
51BB: E6 40           AND     $40                 
51BD: C2 DA 51        JP      NZ,$51DA            ; {}
51C0: 58              LD      E,B                 
51C1: 3E 0F           LD      A,$0F               
51C3: CD 50 43        CALL    $4350               ; {code.GetObjectInfo}
51C6: CA DA 51        JP      Z,$51DA             ; {}
51C9: 3A 74 47        LD      A,($4774)           ; {}
51CC: FE 67           CP      $67                 
51CE: DA DA 51        JP      C,$51DA             ; {}
51D1: 21 04 79        LD      HL,$7904            
51D4: CD AE 45        CALL    $45AE               ; {code.PrintPacked}
51D7: C3 49 54        JP      $5449               ; {}
51DA: 3A 3F 50        LD      A,($503F)           ; {ram.CurrentRoom}
51DD: 32 44 50        LD      ($5044),A           ; {}
51E0: 78              LD      A,B                 
51E1: 32 3F 50        LD      ($503F),A           ; {ram.CurrentRoom}
51E4: CD 45 52        CALL    $5245               ; {}
51E7: 3E 2A           LD      A,$2A               
51E9: 21 E7 4F        LD      HL,$4FE7            
51EC: CD 61 43        CALL    $4361               ; {}
51EF: 23              INC     HL                  
51F0: 7E              LD      A,(HL)              
51F1: A7              AND     A                   
51F2: C2 42 52        JP      NZ,$5242            ; {}
51F5: 21 E7 4F        LD      HL,$4FE7            
51F8: 0E 2C           LD      C,$2C               
51FA: 06 00           LD      B,$00               
51FC: 7E              LD      A,(HL)              
51FD: E6 20           AND     $20                 
51FF: 23              INC     HL                  
5200: CA 0A 52        JP      Z,$520A             ; {}
5203: 7E              LD      A,(HL)              
5204: FE FF           CP      $FF                 
5206: C2 0A 52        JP      NZ,$520A            ; {}
5209: 04              INC     B                   
520A: 23              INC     HL                  
520B: 0D              DEC     C                   
520C: C2 FC 51        JP      NZ,$51FC            ; {}
520F: 78              LD      A,B                 
5210: FE 02           CP      $02                 
5212: DA 42 52        JP      C,$5242             ; {}
5215: 21 E7 4F        LD      HL,$4FE7            
5218: 0E 2C           LD      C,$2C               
521A: 7E              LD      A,(HL)              
521B: E6 20           AND     $20                 
521D: 23              INC     HL                  
521E: CA 30 52        JP      Z,$5230             ; {}
5221: 7E              LD      A,(HL)              
5222: FE FF           CP      $FF                 
5224: C2 30 52        JP      NZ,$5230            ; {}
5227: 36 35           LD      (HL),$35            
5229: 3A 45 50        LD      A,($5045)           ; {}
522C: 3D              DEC     A                   
522D: 32 45 50        LD      ($5045),A           ; {}
5230: 23              INC     HL                  
5231: 0D              DEC     C                   
5232: C2 1A 52        JP      NZ,$521A            ; {}
5235: 1E 35           LD      E,$35               
5237: 3E 2A           LD      A,$2A               
5239: CD 76 43        CALL    $4376               ; {}
523C: 21 4C 7B        LD      HL,$7B4C            
523F: CD AE 45        CALL    $45AE               ; {code.PrintPacked}
5242: C3 AB 43        JP      $43AB               ; {code.ScriptCommandPASS}
5245: 3A 3F 50        LD      A,($503F)           ; {ram.CurrentRoom}
5248: 21 45 4F        LD      HL,$4F45            
524B: CD 61 43        CALL    $4361               ; {}
524E: 7E              LD      A,(HL)              
524F: E6 40           AND     $40                 
5251: C2 71 52        JP      NZ,$5271            ; {}
5254: 3A 3F 50        LD      A,($503F)           ; {ram.CurrentRoom}
5257: 5F              LD      E,A                 
5258: 3E 0F           LD      A,$0F               
525A: CD 50 43        CALL    $4350               ; {code.GetObjectInfo}
525D: CA 71 52        JP      Z,$5271             ; {}
5260: 1E FF           LD      E,$FF               
5262: 3E 0F           LD      A,$0F               
5264: CD 50 43        CALL    $4350               ; {code.GetObjectInfo}
5267: CA 71 52        JP      Z,$5271             ; {}
526A: 21 76 79        LD      HL,$7976            
526D: CD AE 45        CALL    $45AE               ; {code.PrintPacked}
5270: C9              RET                         
5271: 3A 3F 50        LD      A,($503F)           ; {ram.CurrentRoom}
5274: 21 88 48        LD      HL,$4888            
5277: CD 6B 43        CALL    $436B               ; {}
527A: 7E              LD      A,(HL)              
527B: 23              INC     HL                  
527C: 66              LD      H,(HL)              
527D: 6F              LD      L,A                 
527E: CD AE 45        CALL    $45AE               ; {code.PrintPacked}
5281: 06 00           LD      B,$00               
5283: 04              INC     B                   
5284: 3A 3F 50        LD      A,($503F)           ; {ram.CurrentRoom}
5287: 5F              LD      E,A                 
5288: 78              LD      A,B                 
5289: FE 2D           CP      $2D                 
528B: D0              RET     NC                  
528C: CD 50 43        CALL    $4350               ; {code.GetObjectInfo}
528F: C2 83 52        JP      NZ,$5283            ; {}
5292: 78              LD      A,B                 
5293: 21 47 50        LD      HL,$5047            
5296: CD 61 43        CALL    $4361               ; {}
5299: 7E              LD      A,(HL)              
529A: 23              INC     HL                  
529B: 66              LD      H,(HL)              
529C: 6F              LD      L,A                 
529D: C5              PUSH    BC                  
529E: CD AE 45        CALL    $45AE               ; {code.PrintPacked}
52A1: C1              POP     BC                  
52A2: C3 83 52        JP      $5283               ; {}
52A5: E1              POP     HL                  
52A6: 3A 3F 50        LD      A,($503F)           ; {ram.CurrentRoom}
52A9: 5F              LD      E,A                 
52AA: 7E              LD      A,(HL)              
52AB: 23              INC     HL                  
52AC: E5              PUSH    HL                  
52AD: CD 76 43        CALL    $4376               ; {}
52B0: C3 AB 43        JP      $43AB               ; {code.ScriptCommandPASS}
52B3: E1              POP     HL                  
52B4: 7E              LD      A,(HL)              
52B5: 23              INC     HL                  
52B6: 46              LD      B,(HL)              
52B7: 23              INC     HL                  
52B8: E5              PUSH    HL                  
52B9: 21 E7 4F        LD      HL,$4FE7            
52BC: CD 61 43        CALL    $4361               ; {}
52BF: 7E              LD      A,(HL)              
52C0: F6 80           OR      $80                 
52C2: 77              LD      (HL),A              
52C3: 23              INC     HL                  
52C4: 70              LD      (HL),B              
52C5: C3 2B 54        JP      $542B               ; {}
52C8: E1              POP     HL                  
52C9: 7E              LD      A,(HL)              
52CA: 23              INC     HL                  
52CB: E5              PUSH    HL                  
52CC: 1E FF           LD      E,$FF               
52CE: CD 50 43        CALL    $4350               ; {code.GetObjectInfo}
52D1: CA AB 43        JP      Z,$43AB             ; {code.ScriptCommandPASS}
52D4: C3 BE 43        JP      $43BE               ; {code.ScriptCommandFAIL}
52D7: E1              POP     HL                  
52D8: 46              LD      B,(HL)              
52D9: 23              INC     HL                  
52DA: E5              PUSH    HL                  
52DB: 3A 3F 50        LD      A,($503F)           ; {ram.CurrentRoom}
52DE: 5F              LD      E,A                 
52DF: 78              LD      A,B                 
52E0: CD 50 43        CALL    $4350               ; {code.GetObjectInfo}
52E3: CA AB 43        JP      Z,$43AB             ; {code.ScriptCommandPASS}
52E6: 78              LD      A,B                 
52E7: C3 CC 52        JP      $52CC               ; {}
52EA: E1              POP     HL                  
52EB: 3A 3F 50        LD      A,($503F)           ; {ram.CurrentRoom}
52EE: 5F              LD      E,A                 
52EF: 7E              LD      A,(HL)              
52F0: 23              INC     HL                  
52F1: E5              PUSH    HL                  
52F2: CD 50 43        CALL    $4350               ; {code.GetObjectInfo}
52F5: CA AB 43        JP      Z,$43AB             ; {code.ScriptCommandPASS}
52F8: C3 BE 43        JP      $43BE               ; {code.ScriptCommandFAIL}
52FB: 21 E7 4F        LD      HL,$4FE7            
52FE: 0E 01           LD      C,$01               
5300: 23              INC     HL                  
5301: 79              LD      A,C                 
5302: FE 1F           CP      $1F                 
5304: CA 0D 53        JP      Z,$530D             ; {}
5307: 7E              LD      A,(HL)              
5308: FE FF           CP      $FF                 
530A: CA BE 43        JP      Z,$43BE             ; {code.ScriptCommandFAIL}
530D: 23              INC     HL                  
530E: 0C              INC     C                   
530F: 79              LD      A,C                 
5310: FE 2D           CP      $2D                 
5312: C2 00 53        JP      NZ,$5300            ; {}
5315: C3 AB 43        JP      $43AB               ; {code.ScriptCommandPASS}
5318: E1              POP     HL                  
5319: 46              LD      B,(HL)              
531A: 23              INC     HL                  
531B: E5              PUSH    HL                  
531C: 3A 74 47        LD      A,($4774)           ; {}
531F: B8              CP      B                   
5320: CA 26 53        JP      Z,$5326             ; {}
5323: D2 BE 43        JP      NC,$43BE            ; {code.ScriptCommandFAIL}
5326: 21 95 72        LD      HL,$7295            
5329: CD AE 45        CALL    $45AE               ; {code.PrintPacked}
532C: CD 45 52        CALL    $5245               ; {}
532F: C3 AB 43        JP      $43AB               ; {code.ScriptCommandPASS}
5332: E1              POP     HL                  
5333: 46              LD      B,(HL)              
5334: 23              INC     HL                  
5335: E5              PUSH    HL                  
5336: 3A 44 50        LD      A,($5044)           ; {}
5339: B8              CP      B                   
533A: C2 BE 43        JP      NZ,$43BE            ; {code.ScriptCommandFAIL}
533D: E1              POP     HL                  
533E: 2B              DEC     HL                  
533F: E5              PUSH    HL                  
5340: C3 8A 51        JP      $518A               ; {code.MoveToRoomX}
5343: 3A 7B 46        LD      A,($467B)           ; {ram.Noun}
5346: 1E FF           LD      E,$FF               
5348: CD 50 43        CALL    $4350               ; {code.GetObjectInfo}
534B: C2 57 53        JP      NZ,$5357            ; {}
534E: 21 60 75        LD      HL,$7560            
5351: CD AE 45        CALL    $45AE               ; {code.PrintPacked}
5354: C3 AB 43        JP      $43AB               ; {code.ScriptCommandPASS}
5357: 3A 7B 46        LD      A,($467B)           ; {ram.Noun}
535A: 47              LD      B,A                 
535B: C3 F4 53        JP      $53F4               ; {}
535E: E1              POP     HL                  
535F: 5E              LD      E,(HL)              
5360: 23              INC     HL                  
5361: 56              LD      D,(HL)              
5362: 23              INC     HL                  
5363: E5              PUSH    HL                  
5364: EB              EX      DE,HL               
5365: CD AE 45        CALL    $45AE               ; {code.PrintPacked}
5368: C3 AB 43        JP      $43AB               ; {code.ScriptCommandPASS}
536B: E1              POP     HL                  
536C: 46              LD      B,(HL)              
536D: 23              INC     HL                  
536E: E5              PUSH    HL                  
536F: 3A 45 50        LD      A,($5045)           ; {}
5372: 3D              DEC     A                   
5373: 32 45 50        LD      ($5045),A           ; {}
5376: 3A 3F 50        LD      A,($503F)           ; {ram.CurrentRoom}
5379: 5F              LD      E,A                 
537A: 78              LD      A,B                 
537B: CD 76 43        CALL    $4376               ; {}
537E: C3 2B 54        JP      $542B               ; {}
5381: 3A 44 50        LD      A,($5044)           ; {}
5384: A7              AND     A                   
5385: CA 92 53        JP      Z,$5392             ; {}
5388: 47              LD      B,A                 
5389: 3A 3F 50        LD      A,($503F)           ; {ram.CurrentRoom}
538C: 32 44 50        LD      ($5044),A           ; {}
538F: C3 E0 51        JP      $51E0               ; {}
5392: 21 33 75        LD      HL,$7533            
5395: CD AE 45        CALL    $45AE               ; {code.PrintPacked}
5398: C3 AB 43        JP      $43AB               ; {code.ScriptCommandPASS}
539B: 3A 45 50        LD      A,($5045)           ; {}
539E: A7              AND     A                   
539F: C2 AB 53        JP      NZ,$53AB            ; {}
53A2: 21 A6 75        LD      HL,$75A6            
53A5: CD AE 45        CALL    $45AE               ; {code.PrintPacked}
53A8: C3 AB 43        JP      $43AB               ; {code.ScriptCommandPASS}
53AB: 21 BC 75        LD      HL,$75BC            
53AE: CD AE 45        CALL    $45AE               ; {code.PrintPacked}
53B1: 06 00           LD      B,$00               
53B3: 1E FF           LD      E,$FF               
53B5: 04              INC     B                   
53B6: 78              LD      A,B                 
53B7: FE 2D           CP      $2D                 
53B9: D2 AB 43        JP      NC,$43AB            ; {code.ScriptCommandPASS}
53BC: CD 50 43        CALL    $4350               ; {code.GetObjectInfo}
53BF: C2 B3 53        JP      NZ,$53B3            ; {}
53C2: 78              LD      A,B                 
53C3: 21 47 50        LD      HL,$5047            
53C6: CD 61 43        CALL    $4361               ; {}
53C9: 7E              LD      A,(HL)              
53CA: 23              INC     HL                  
53CB: 66              LD      H,(HL)              
53CC: 6F              LD      L,A                 
53CD: 7E              LD      A,(HL)              
53CE: 23              INC     HL                  
53CF: A7              AND     A                   
53D0: C2 CD 53        JP      NZ,$53CD            ; {}
53D3: C5              PUSH    BC                  
53D4: CD AE 45        CALL    $45AE               ; {code.PrintPacked}
53D7: C1              POP     BC                  
53D8: C3 B3 53        JP      $53B3               ; {}
53DB: CD 45 52        CALL    $5245               ; {}
53DE: C3 AB 43        JP      $43AB               ; {code.ScriptCommandPASS}
53E1: E1              POP     HL                  
53E2: 46              LD      B,(HL)              
53E3: 23              INC     HL                  
53E4: E5              PUSH    HL                  
53E5: 3A 7B 46        LD      A,($467B)           ; {ram.Noun}
53E8: B8              CP      B                   
53E9: C2 BE 43        JP      NZ,$43BE            ; {code.ScriptCommandFAIL}
53EC: C3 AB 43        JP      $43AB               ; {code.ScriptCommandPASS}
53EF: E1              POP     HL                  
53F0: 46              LD      B,(HL)              
53F1: 23              INC     HL                  
53F2: E5              PUSH    HL                  
53F3: 78              LD      A,B                 
53F4: CD 50 43        CALL    $4350               ; {code.GetObjectInfo}
53F7: 7E              LD      A,(HL)              
53F8: E6 40           AND     $40                 
53FA: C2 06 54        JP      NZ,$5406            ; {}
53FD: 21 D9 75        LD      HL,$75D9            
5400: CD AE 45        CALL    $45AE               ; {code.PrintPacked}
5403: C3 AB 43        JP      $43AB               ; {code.ScriptCommandPASS}
5406: 3A 45 50        LD      A,($5045)           ; {}
5409: FE 08           CP      $08                 
540B: DA 17 54        JP      C,$5417             ; {}
540E: 21 75 75        LD      HL,$7575            
5411: CD AE 45        CALL    $45AE               ; {code.PrintPacked}
5414: C3 AB 43        JP      $43AB               ; {code.ScriptCommandPASS}
5417: 3C              INC     A                   
5418: 32 45 50        LD      ($5045),A           ; {}
541B: 78              LD      A,B                 
541C: 1E FF           LD      E,$FF               
541E: CD 76 43        CALL    $4376               ; {}
5421: C3 2B 54        JP      $542B               ; {}
5424: 3A 7B 46        LD      A,($467B)           ; {ram.Noun}
5427: 47              LD      B,A                 
5428: C3 6F 53        JP      $536F               ; {}
542B: 21 2F 75        LD      HL,$752F            
542E: CD AE 45        CALL    $45AE               ; {code.PrintPacked}
5431: C3 AB 43        JP      $43AB               ; {code.ScriptCommandPASS}
5434: E1              POP     HL                  
5435: 7E              LD      A,(HL)              
5436: 23              INC     HL                  
5437: 5E              LD      E,(HL)              
5438: 23              INC     HL                  
5439: E5              PUSH    HL                  
543A: 21 E7 4F        LD      HL,$4FE7            
543D: CD 61 43        CALL    $4361               ; {}
5440: 7E              LD      A,(HL)              
5441: E6 7F           AND     $7F                 
5443: 77              LD      (HL),A              
5444: 23              INC     HL                  
5445: 73              LD      (HL),E              
5446: C3 AB 43        JP      $43AB               ; {code.ScriptCommandPASS}
5449: 3A 46 50        LD      A,($5046)           ; {}
544C: 3C              INC     A                   
544D: 32 46 50        LD      ($5046),A           ; {}
5450: FE 03           CP      $03                 
5452: D2 BC 54        JP      NC,$54BC            ; {}
5455: FE 02           CP      $02                 
5457: CA B0 54        JP      Z,$54B0             ; {}
545A: 21 B4 7E        LD      HL,$7EB4            
545D: 22 C5 54        LD      ($54C5),HL          ; {}
5460: 21 AA 7D        LD      HL,$7DAA            
5463: CD AE 45        CALL    $45AE               ; {code.PrintPacked}
5466: CD EE 45        CALL    $45EE               ; {code.WaitForKey}
5469: FE 59           CP      $59                 
546B: C2 EF 55        JP      NZ,$55EF            ; {}
546E: 2A C5 54        LD      HL,($54C5)          ; {}
5471: CD AE 45        CALL    $45AE               ; {code.PrintPacked}
5474: 21 02 50        LD      HL,$5002            
5477: 36 01           LD      (HL),$01            
5479: 23              INC     HL                  
547A: 23              INC     HL                  
547B: 36 00           LD      (HL),$00            
547D: 21 E7 4F        LD      HL,$4FE7            
5480: 3A 3F 50        LD      A,($503F)           ; {ram.CurrentRoom}
5483: 47              LD      B,A                 
5484: 3E FF           LD      A,$FF               
5486: 0E 2C           LD      C,$2C               
5488: 23              INC     HL                  
5489: BE              CP      (HL)                
548A: C2 97 54        JP      NZ,$5497            ; {}
548D: 70              LD      (HL),B              
548E: 3A 45 50        LD      A,($5045)           ; {}
5491: 3D              DEC     A                   
5492: 32 45 50        LD      ($5045),A           ; {}
5495: 3E FF           LD      A,$FF               
5497: 23              INC     HL                  
5498: 0D              DEC     C                   
5499: C2 88 54        JP      NZ,$5488            ; {}
549C: 3E 02           LD      A,$02               
549E: 32 3F 50        LD      ($503F),A           ; {ram.CurrentRoom}
54A1: CD 45 52        CALL    $5245               ; {}
54A4: 31 BF 47        LD      SP,$47BF            
54A7: 21 00 00        LD      HL,$0000            
54AA: 22 42 50        LD      ($5042),HL          ; {}
54AD: C3 19 43        JP      $4319               ; {}
54B0: 21 4E 7F        LD      HL,$7F4E            
54B3: 22 C5 54        LD      ($54C5),HL          ; {}
54B6: 21 1D 7E        LD      HL,$7E1D            
54B9: C3 63 54        JP      $5463               ; {}
54BC: 21 79 7E        LD      HL,$7E79            
54BF: CD AE 45        CALL    $45AE               ; {code.PrintPacked}
54C2: C3 EF 55        JP      $55EF               ; {}
54C5: 00              NOP                         
54C6: 00              NOP                         
54C7: CD CD 54        CALL    $54CD               ; {}
54CA: C3 AB 43        JP      $43AB               ; {code.ScriptCommandPASS}
54CD: 21 00 00        LD      HL,$0000            
54D0: 22 B2 55        LD      ($55B2),HL          ; {}
54D3: 21 45 4F        LD      HL,$4F45            
54D6: 0E 51           LD      C,$51               
54D8: 7E              LD      A,(HL)              
54D9: E6 80           AND     $80                 
54DB: 23              INC     HL                  
54DC: CA F0 54        JP      Z,$54F0             ; {}
54DF: 3A B2 55        LD      A,($55B2)           ; {}
54E2: 86              ADD     A,(HL)              
54E3: 27              DAA                         
54E4: 32 B2 55        LD      ($55B2),A           ; {}
54E7: 3A B3 55        LD      A,($55B3)           ; {}
54EA: CE 00           ADC     $00                 
54EC: 27              DAA                         
54ED: 32 B3 55        LD      ($55B3),A           ; {}
54F0: 23              INC     HL                  
54F1: 0D              DEC     C                   
54F2: C2 D8 54        JP      NZ,$54D8            ; {}
54F5: 21 E7 4F        LD      HL,$4FE7            
54F8: 0E 2C           LD      C,$2C               
54FA: 7E              LD      A,(HL)              
54FB: E6 20           AND     $20                 
54FD: 23              INC     HL                  
54FE: CA 21 55        JP      Z,$5521             ; {}
5501: 7E              LD      A,(HL)              
5502: FE 02           CP      $02                 
5504: 06 20           LD      B,$20               
5506: CA 10 55        JP      Z,$5510             ; {}
5509: FE FF           CP      $FF                 
550B: C2 21 55        JP      NZ,$5521            ; {}
550E: 06 05           LD      B,$05               
5510: 3A B2 55        LD      A,($55B2)           ; {}
5513: 80              ADD     A,B                 
5514: 27              DAA                         
5515: 32 B2 55        LD      ($55B2),A           ; {}
5518: 3A B3 55        LD      A,($55B3)           ; {}
551B: CE 00           ADC     $00                 
551D: 27              DAA                         
551E: 32 B3 55        LD      ($55B3),A           ; {}
5521: 23              INC     HL                  
5522: 0D              DEC     C                   
5523: C2 FA 54        JP      NZ,$54FA            ; {}
5526: 3A 46 50        LD      A,($5046)           ; {}
5529: A7              AND     A                   
552A: CA 48 55        JP      Z,$5548             ; {}
552D: 4F              LD      C,A                 
552E: 06 90           LD      B,$90               
5530: 3A B2 55        LD      A,($55B2)           ; {}
5533: 80              ADD     A,B                 
5534: 27              DAA                         
5535: 32 B2 55        LD      ($55B2),A           ; {}
5538: DA 44 55        JP      C,$5544             ; {}
553B: 3A B3 55        LD      A,($55B3)           ; {}
553E: C6 99           ADD     $99                 
5540: 27              DAA                         
5541: 32 B3 55        LD      ($55B3),A           ; {}
5544: 0D              DEC     C                   
5545: C2 30 55        JP      NZ,$5530            ; {}
5548: 3A B3 55        LD      A,($55B3)           ; {}
554B: FE 90           CP      $90                 
554D: DA 78 55        JP      C,$5578             ; {}
5550: 3E 2D           LD      A,$2D               
5552: 32 BF 55        LD      ($55BF),A           ; {}
5555: 3A B3 55        LD      A,($55B3)           ; {}
5558: 47              LD      B,A                 
5559: 3E 99           LD      A,$99               
555B: 90              SUB     B                   
555C: 32 B3 55        LD      ($55B3),A           ; {}
555F: 3A B2 55        LD      A,($55B2)           ; {}
5562: 47              LD      B,A                 
5563: 3E 99           LD      A,$99               
5565: 90              SUB     B                   
5566: C6 01           ADD     $01                 
5568: 27              DAA                         
5569: 32 B2 55        LD      ($55B2),A           ; {}
556C: 3A B3 55        LD      A,($55B3)           ; {}
556F: CE 00           ADC     $00                 
5571: 27              DAA                         
5572: 32 B3 55        LD      ($55B3),A           ; {}
5575: C3 7D 55        JP      $557D               ; {}
5578: 3E 20           LD      A,$20               
557A: 32 BF 55        LD      ($55BF),A           ; {}
557D: 21 C0 55        LD      HL,$55C0            
5580: 3A B3 55        LD      A,($55B3)           ; {}
5583: CD A2 55        CALL    $55A2               ; {}
5586: 3A B2 55        LD      A,($55B2)           ; {}
5589: CD A2 55        CALL    $55A2               ; {}
558C: 21 E3 55        LD      HL,$55E3            
558F: 3A 41 50        LD      A,($5041)           ; {}
5592: CD A2 55        CALL    $55A2               ; {}
5595: 3A 40 50        LD      A,($5040)           ; {}
5598: CD A2 55        CALL    $55A2               ; {}
559B: 21 B4 55        LD      HL,$55B4            
559E: CD D0 45        CALL    $45D0               ; {}
55A1: C9              RET                         
55A2: F5              PUSH    AF                  
55A3: 0F              RRCA                        
55A4: 0F              RRCA                        
55A5: 0F              RRCA                        
55A6: 0F              RRCA                        
55A7: CD AB 55        CALL    $55AB               ; {}
55AA: F1              POP     AF                  
55AB: E6 0F           AND     $0F                 
55AD: C6 30           ADD     $30                 
55AF: 77              LD      (HL),A              
55B0: 23              INC     HL                  
55B1: C9              RET                         

55B2: 00              NOP                         
55B3: 00              NOP     no                  

; YOU_SCORED_______OUT_OF_A_POSSIBLE_0220,_USING______TURNS.[CR]
55B4: 59 4F 55 20 53 43 4F 52 45 44 20 20 20 20 20 20 20 4F 55 54 20 4F 46 20 41 20 50 4F 53 53 49 42
55D4: 4C 45 20 30 32 32 30 2C 20 55 53 49 4E 47 20 20 20 20 20 20 54 55 52 4E 53 2E 00      

55EF: CD CD 54        CALL    $54CD               ; {}
; Endless loop           
55F2: C3 F2 55        JP      $55F2               ; {}
           
55F5: 21 A0 7F        LD      HL,$7FA0            ; READY CASSETTE
55F8: CD AE 45        CALL    $45AE               ; {code.PrintPacked} Print message
55FB: CD EE 45        CALL    $45EE               ; {code.WaitForKey} Wait on key
55FE: FE 08           CP      $08                 ; Backspace?
5600: CA AB 43        JP      Z,$43AB             ; {code.ScriptCommandPASS} Yes ... abort operation
5603: FE 0D           CP      $0D                 ; Enter?
5605: C2 FB 55        JP      NZ,$55FB            ; {} No ... keep waiting
5608: 97              SUB     A                   ; Make a zero
5609: CD 12 02        CALL    $0212               ; Turn on cassette 0
560C: CD 96 02        CALL    $0296               ; Read tape leader
560F: 21 45 4F        LD      HL,$4F45            ; Load destination
5612: 01 03 01        LD      BC,$0103            ; 259 bytes
5615: 1E 00           LD      E,$00               ; Initialize checksum
5617: E5              PUSH    HL                  ; ROM ...
5618: C5              PUSH    BC                  ; ... mangles ...
5619: D5              PUSH    DE                  ; ... these
561A: CD 35 02        CALL    $0235               ; Read one byte of data
561D: D1              POP     DE                  ; Un ...
561E: C1              POP     BC                  ; ... mangle ...
561F: E1              POP     HL                  ; ... these
5620: 77              LD      (HL),A              ; Store the byte
5621: 83              ADD     A,E                 ; Add to ...
5622: 5F              LD      E,A                 ; ... checksum
5623: 23              INC     HL                  ; Next destination
5624: 0B              DEC     BC                  ; All done?
5625: 78              LD      A,B                 ; Remember, DEC doesn't ...
5626: B1              OR      C                   ; ... affect the zero flag
5627: C2 17 56        JP      NZ,$5617            ; {} Nope ... do all $103 bytes
562A: D5              PUSH    DE                  ; Hold
562B: CD 35 02        CALL    $0235               ; Read the checksum
562E: D1              POP     DE                  ; Restore
562F: BB              CP      E                   ; Checksum OK?
5630: CA 3F 56        JP      Z,$563F             ; {} Yes ... out
5633: 21 AC 7F        LD      HL,$7FAC            ; Error message
5636: CD AE 45        CALL    $45AE               ; {code.PrintPacked} Print error message
5639: CD F8 01        CALL    $01F8               ; Turn off tape drive
563C: C3 F5 55        JP      $55F5               ; {} Go back and try again (you better not abort ... we already changed memory)

563F: CD F8 01        CALL    $01F8               ; Turn off the tape
5642: 21 58 6D        LD      HL,$6D58            
5645: 22 47 50        LD      ($5047),HL          ; {code.ObjectDescriptions}
5648: 22 49 50        LD      ($5049),HL          ; {}
564B: CD 45 52        CALL    $5245               ; {}
564E: 31 BF 47        LD      SP,$47BF            ; Abandon previous stack
5651: C3 19 43        JP      $4319               ; {} Back to input loop

5654: 21 A0 7F        LD      HL,$7FA0            
5657: CD AE 45        CALL    $45AE               ; {code.PrintPacked}
565A: CD EE 45        CALL    $45EE               ; {code.WaitForKey}
565D: FE 08           CP      $08                 
565F: CA AB 43        JP      Z,$43AB             ; {code.ScriptCommandPASS}
5662: FE 0D           CP      $0D                 
5664: C2 5A 56        JP      NZ,$565A            ; {}
5667: 97              SUB     A                   
5668: CD 12 02        CALL    $0212               
566B: CD 87 02        CALL    $0287               
566E: 21 45 4F        LD      HL,$4F45            
5671: 01 03 01        LD      BC,$0103            
5674: 1E 00           LD      E,$00               
5676: E5              PUSH    HL                  
5677: C5              PUSH    BC                  
5678: 7E              LD      A,(HL)              
5679: 83              ADD     A,E                 
567A: 5F              LD      E,A                 
567B: D5              PUSH    DE                  
567C: 7E              LD      A,(HL)              
567D: CD 64 02        CALL    $0264               
5680: D1              POP     DE                  
5681: C1              POP     BC                  
5682: E1              POP     HL                  
5683: 23              INC     HL                  
5684: 0B              DEC     BC                  
5685: 78              LD      A,B                 
5686: B1              OR      C                   
5687: C2 76 56        JP      NZ,$5676            ; {}
568A: 7B              LD      A,E                 
568B: CD 64 02        CALL    $0264               
568E: CD F8 01        CALL    $01F8               
5691: C3 AB 43        JP      $43AB               ; {code.ScriptCommandPASS}

5694: 3A 74 47        LD      A,($4774)           ; {}
5697: E6 03           AND     $03                 
5699: 47              LD      B,A                 
569A: 21 CC 49        LD      HL,$49CC            
569D: 7E              LD      A,(HL)              
569E: 23              INC     HL                  
569F: A7              AND     A                   
56A0: CA 9D 56        JP      Z,$569D             ; {}
56A3: FE FF           CP      $FF                 
56A5: CA C2 56        JP      Z,$56C2             ; {}
56A8: FE 05           CP      $05                 
56AA: D2 B8 56        JP      NC,$56B8            ; {}
56AD: 80              ADD     A,B                 
56AE: 2B              DEC     HL                  
56AF: E6 03           AND     $03                 
56B1: C2 B6 56        JP      NZ,$56B6            ; {}
56B4: 3E 04           LD      A,$04               
56B6: 77              LD      (HL),A              
56B7: 23              INC     HL                  
56B8: 7E              LD      A,(HL)              
56B9: 85              ADD     A,L                 
56BA: 6F              LD      L,A                 
56BB: 7C              LD      A,H                 
56BC: CE 00           ADC     $00                 
56BE: 67              LD      H,A                 
56BF: C3 9D 56        JP      $569D               ; {}
56C2: 21 B8 7F        LD      HL,$7FB8            
56C5: CD AE 45        CALL    $45AE               ; {code.PrintPacked}
56C8: 31 BF 47        LD      SP,$47BF            
56CB: C3 19 43        JP      $4319               ; {}
```

## Word Table 

Pyramid has a table of known words. Every word has a grammar that describes how it can be used. 
For instance, LAMP is a noun. The verb NORTH is a single-word command that requires no noun 
(in fact it is an error to give one). The verb DROP requires a noun that is in the inventory, 
but the verb DRINK works on a noun that is in the room or the pack.

Multiple words can refer to the same thing. LAMP and LANTERN, for instance, mean the same 
thing. So do GET and STEAL.

Since multiple nouns can have the same word for a name the game logic must be careful not to 
ever have two nouns with the same noun in the same place. The "dead lamp", for instance, is never 
around when the "lit lamp" is. When checking to see if a noun is accessible the code must check 
every noun since multiple nouns can have the same name.

The input routine parses the user input and returns a VERB and a NOUN based on the grammar of the 
words. The game scripts are assured that the grammar is correct and the noun is something the user 
has access to (in the pack or room).

```code
WordTable:
; Info + text + data
;   Info byte:
;   AA_BBB_CCC
;
;   AA = Grammar
;      0 = Noun
;      1 = Verb (and needs noun in pack)
;      2 = Verb (and needs noun in pack or room)
;      3 = Verb (stand alone)
;
;   BBB = number of bytes in token data
;   CCC = number of bytes in token text
;
; Object words
; A single name can refer to several objects. The object data is
; the search order for finding objects in the pack or room. For 
; instance, the LAMP refers to:
;   1) 0x0E unlit lamp
;   2) 0x0F lit lamp
;   3) 0x2C dead lamp
;
; Nouns
;                               Objects     AA BBB CCC Word     
56CE: 1C 4C 41 4D 50            0E 0F 2C  ; 00_011_100 LAMP
56D6: 1E 4C 41 4E 54 45 52      0E 0F 2C  ; 00_011_110 LANTER
56E0: 0B 42 4F 58               10        ; 00_001_011 BOX
56E5: 0F 53 43 45 50 54 45 52   11        ; 00_001_111 SCEPTER
56EE: 14 42 49 52 44            13 14     ; 00_010_100 BIRD
56F5: 16 53 54 41 54 55 45      13 14     ; 00_010_110 STATUE
56FE: 0E 50 49 4C 4C 4F 57      12        ; 00_001_110 PILLOW
5706: 0E 56 45 4C 56 45 54      12        ; 00_001_110 VELVET
570E: 0E 53 45 52 50 45 4E      0B        ; 00_001_110 SERPEN
5716: 16 53 41 52 43 4F 50      17 18     ; 00_010_110 SARCOP
571F: 0E 4D 41 47 41 5A 49      19        ; 00_001_110 MAGAZI
5727: 0D 49 53 53 55 45         19        ; 00_001_101 ISSUE
572E: 0E 45 47 59 50 54 49      19        ; 00_001_110 EGYPTI
5736: 0C 46 4F 4F 44            1A        ; 00_001_100 FOOD
573C: 0E 42 4F 54 54 4C 45      1B        ; 00_001_110 BOTTLE
5744: 15 57 41 54 45 52         1C 1E     ; 00_010_101 WATER
574C: 1D 50 4C 41 4E 54         07 08 09  ; 00_011_101 PLANT
5755: 1E 42 45 41 4E 53 54      07 08 09  ; 00_011_110 BEANST
575F: 0E 4D 41 43 48 49 4E      06        ; 00_001_110 MACHIN
5767: 0E 56 45 4E 44 49 4E      06        ; 00_001_110 VENDIN
576F: 16 42 41 54 54 45 52      23 24     ; 00_010_110 BATTER
5778: 0C 47 4F 4C 44            25        ; 00_001_100 GOLD
577E: 0E 4E 55 47 47 45 54      25        ; 00_001_110 NUGGET
5786: 0E 44 49 41 4D 4F 4E      26        ; 00_001_110 DIAMON
578E: 0E 53 49 4C 56 45 52      27        ; 00_001_110 SILVER
5796: 0C 42 41 52 53            27        ; 00_001_100 BARS
579C: 0E 4A 45 57 45 4C 52      28        ; 00_001_110 JEWELR
57A4: 0D 43 4F 49 4E 53         29        ; 00_001_101 COINS
57AB: 0D 43 48 45 53 54         2A        ; 00_001_101 CHEST
57B2: 0E 54 52 45 41 53 55      2A        ; 00_001_110 TREASU
57BA: 0C 45 47 47 53            2B        ; 00_001_100 EGGS
57C0: 0B 45 47 47               2B        ; 00_001_011 EGG
57C5: 0C 4E 45 53 54            2B        ; 00_001_100 NEST
57CB: 0B 4B 45 59               22        ; 00_001_011 KEY
57D0: 14 56 41 53 45            20 21     ; 00_010_100 VASE
57D7: 0E 53 48 41 52 44 53      15        ; 00_001_110 SHARDS
57DF: 0E 50 4F 54 54 45 52      15        ; 00_001_110 POTTER
57E7: 0E 45 4D 45 52 41 4C      1F        ; 00_001_110 EMERAL
57EF: 0D 50 45 41 52 4C         16        ; 00_001_101 PEARL
;
; Verbs
57F6: C9 4E                     01        ; 11_001_001 N
57F9: CD 4E 4F 52 54 48         01        ; 11_001_101 NORTH
5800: C9 45                     02        ; 11_001_001 E
5803: CC 45 41 53 54            02        ; 11_001_100 EAST
5809: C9 53                     03        ; 11_001_001 S
580C: CD 53 4F 55 54 48         03        ; 11_001_101 SOUTH
5813: C9 57                     04        ; 11_001_001 W
5816: CC 57 45 53 54            04        ; 11_001_100 WEST
581C: CA 4E 45                  05        ; 11_001_010 NE
5820: CE 4E 4F 52 54 48 45      05        ; 11_001_110 NORTHE
5828: CA 53 45                  06        ; 11_001_010 SE
582C: CE 53 4F 55 54 48 45      06        ; 11_001_110 SOUTHE
5834: CA 53 57                  07        ; 11_001_010 SW
5838: CE 53 4F 55 54 48 57      07        ; 11_001_110 SOUTHW
5840: CA 4E 57                  08        ; 11_001_010 NW
5844: CE 4E 4F 52 54 48 57      08        ; 11_001_110 NORTHW
584C: C9 55                     09        ; 11_001_001 U
584F: CA 55 50                  09        ; 11_001_010 UP
5853: C9 44                     0A        ; 11_001_001 D
5856: CC 44 4F 57 4E            0A        ; 11_001_100 DOWN
585C: CA 49 4E                  0B        ; 11_001_010 IN
5860: CE 49 4E 53 49 44 45      0B        ; 11_001_110 INSIDE
5868: CB 4F 55 54               0C        ; 11_001_011 OUT
586D: CE 4F 55 54 53 49 44      0C        ; 11_001_110 OUTSID
5875: CD 43 52 4F 53 53         0D        ; 11_001_101 CROSS
587C: CC 4C 45 46 54            0E        ; 11_001_100 LEFT
5882: CD 52 49 47 48 54         0F        ; 11_001_101 RIGHT
5889: CC 4A 55 4D 50            10        ; 11_001_100 JUMP
588F: CD 43 4C 49 4D 42         11        ; 11_001_101 CLIMB
5896: CD 50 41 4E 45 4C         12        ; 11_001_101 PANEL
589D: CC 42 41 43 4B            14        ; 11_001_100 BACK
58A3: CC 53 57 49 4D            16        ; 11_001_100 SWIM
58A9: CA 4F 4E                  17        ; 11_001_010 ON
58AD: CB 4F 46 46               18        ; 11_001_011 OFF
58B2: CC 51 55 49 54            19        ; 11_001_100 QUIT
58B8: CC 53 54 4F 50            19        ; 11_001_100 STOP
58BE: CD 53 43 4F 52 45         1A        ; 11_001_101 SCORE
58C5: CE 49 4E 56 45 4E 54      1B        ; 11_001_110 INVENT
58CD: CC 4C 4F 4F 4B            1C        ; 11_001_100 LOOK
58D3: CC 48 45 4C 50            1D        ; 11_001_100 HELP
58D9: CC 46 49 4E 44            1E        ; 11_001_100 FIND
58DF: 4C 44 52 4F 50            21        ; 01_001_100 DROP
58E5: 4E 52 45 4C 45 41 53      21        ; 01_001_110 RELEAS
58ED: 4C 46 52 45 45            21        ; 01_001_100 FREE
58F3: 4E 44 49 53 43 41 52      21        ; 01_001_110 DISCAR
58FB: CD 4C 49 47 48 54         17        ; 11_001_101 LIGHT
5902: 4C 57 41 56 45            23        ; 01_001_100 WAVE
5908: 4D 53 48 41 4B 45         23        ; 01_001_101 SHAKE
590F: 4D 53 57 49 4E 47         23        ; 01_001_101 SWING
5916: 4C 50 4F 55 52            24        ; 01_001_100 POUR
591C: 4B 52 55 42               25        ; 01_001_011 RUB
5921: 4D 54 48 52 4F 57         26        ; 01_001_101 THROW
5928: 4C 54 4F 53 53            26        ; 01_001_100 TOSS
592E: 4C 46 49 4C 4C            27        ; 01_001_100 FILL
5934: 8C 54 41 4B 45            28        ; 10_001_100 TAKE
593A: 8B 47 45 54               28        ; 10_001_011 GET
593F: 8D 43 41 52 52 59         28        ; 10_001_101 CARRY
5946: 8D 43 41 54 43 48         28        ; 10_001_101 CATCH
594D: 8D 53 54 45 41 4C         28        ; 10_001_101 STEAL
5954: 8E 43 41 50 54 55 52      28        ; 10_001_110 CAPTUR
595C: 8C 4F 50 45 4E            29        ; 10_001_100 OPEN
5962: 8E 41 54 54 41 43 4B      2C        ; 10_001_110 ATTACK
596A: 8C 4B 49 4C 4C            2C        ; 10_001_100 KILL
5970: 8B 48 49 54               2C        ; 10_001_011 HIT
5975: 8D 46 49 47 48 54         2C        ; 10_001_101 FIGHT
597C: 8C 46 45 45 44            2D        ; 10_001_100 FEED
5982: 8B 45 41 54               2E        ; 10_001_011 EAT
5987: 8D 44 52 49 4E 4B         2F        ; 10_001_101 DRINK
598E: 8D 42 52 45 41 4B         30        ; 10_001_101 BREAK
5995: 8D 53 4D 41 53 48         30        ; 10_001_101 SMASH
599C: CC 4C 4F 41 44            3A        ; 11_001_100 LOAD
59A2: CC 53 41 56 45            3B        ; 11_001_100 SAVE
59A8: CD 50 4C 55 47 48         39        ; 11_001_101 PLUGH       
59AF: 00                    
```

# General Command Handler 

This script is used when the room doesn't have a script for the input command.

```code
GeneralCommandHandler:
59B0: 01 04     ; "N" : [
59B2: 04 ED 73  ;    "PrintMessageX","THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]"],
59B5: 02 04     ; "E" : [
59B7: 04 ED 73  ;    "PrintMessageX","THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]"],
59BA: 03 04     ; "S" : [
59BC: 04 ED 73  ;    "PrintMessageX","THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]"],
59BF: 04 04     ; "W" : [
59C1: 04 ED 73  ;    "PrintMessageX","THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]"],
59C4: 05 04     ; "NE" : [
59C6: 04 ED 73  ;    "PrintMessageX","THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]"],
59C9: 06 04     ; "SE" : [
59CB: 04 ED 73  ;    "PrintMessageX","THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]"],
59CE: 07 04     ; "SW" : [
59D0: 04 ED 73  ;    "PrintMessageX","THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]"],
59D3: 08 04     ; "NW" : [
59D5: 04 ED 73  ;    "PrintMessageX","THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]"],
59D8: 09 04     ; "U" : [
59DA: 04 ED 73  ;    "PrintMessageX","THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]"],
59DD: 0A 04     ; "D" : [
59DF: 04 ED 73  ;    "PrintMessageX","THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]"],
59E2: 0B 04     ; "IN" : [
59E4: 04 0D 74  ;    "PrintMessageX","I_DON'T_KNOW_IN_FROM_OUT_HERE.__USE_COMPASS_POINTS.[CR]"],
59E7: 0C 04     ; "OUT" : [
59E9: 04 0D 74  ;    "PrintMessageX","I_DON'T_KNOW_IN_FROM_OUT_HERE.__USE_COMPASS_POINTS.[CR]"],
59EC: 0E 04     ; "LEFT" : [
59EE: 04 31 74  ;    "PrintMessageX","I_AM_UNSURE_HOW_YOU_ARE_FACING.__USE_COMPASS_POINTS.[CR]"],
59F1: 0F 04     ; "RIGHT" : [
59F3: 04 31 74  ;    "PrintMessageX","I_AM_UNSURE_HOW_YOU_ARE_FACING.__USE_COMPASS_POINTS.[CR]"],
59F6: 12 04     ; "PANEL" : [
59F8: 04 56 74  ;    "PrintMessageX","NOTHING_HAPPENS.[CR]"],
59FB: 14 02     ; "BACK" : [
59FD: 0E        ;    "MoveToLastRoom"],
59FE: 16 04     ; "SWIM" : [
5A00: 04 63 74  ;    "PrintMessageX","I_DON'T_KNOW_HOW.[CR]"],
5A03: 17 18     ; "ON" : [
5A05: 07 0C     ;    "SubScripXtAbortIfPass",[
5A07: 02 0E     ;        "AssertObjectXIsInPack","#LAMP_off",
5A09: 15 0E 00  ;        "MoveObjectXToRoomY","#LAMP_off","room_0",
5A0C: 15 0F FF  ;        "MoveObjectXToRoomY","#LAMP_on","room_255",
5A0F: 04 8F 74  ;        "PrintMessageX","YOUR_LAMP_IS_NOW_ON.[CR]"],
5A12: 07 06     ;    "SubScripXtAbortIfPass",[
5A14: 02 0F     ;        "AssertObjectXIsInPack","#LAMP_on",
5A16: 04 8F 74  ;        "PrintMessageX","YOUR_LAMP_IS_NOW_ON.[CR]"],
5A19: 04 9F 74  ;    "PrintMessageX","YOU_HAVE_NO_SOURCE_OF_LIGHT.[CR]"],
5A1C: 18 18     ; "OFF" : [
5A1E: 07 0C     ;    "SubScripXtAbortIfPass",[
5A20: 02 0F     ;        "AssertObjectXIsInPack","#LAMP_on",
5A22: 15 0F 00  ;        "MoveObjectXToRoomY","#LAMP_on","room_0",
5A25: 15 0E FF  ;        "MoveObjectXToRoomY","#LAMP_off","room_255",
5A28: 04 B4 74  ;        "PrintMessageX","YOUR_LAMP_IS_NOW_OFF.[CR]"],
5A2B: 07 06     ;    "SubScripXtAbortIfPass",[
5A2D: 02 0E     ;        "AssertObjectXIsInPack","#LAMP_off",
5A2F: 04 B4 74  ;        "PrintMessageX","YOUR_LAMP_IS_NOW_OFF.[CR]"],
5A32: 04 9F 74  ;    "PrintMessageX","YOU_HAVE_NO_SOURCE_OF_LIGHT.[CR]"],
5A35: 19 02     ; "QUIT" : [
5A37: 09        ;    "PrintScoreAndStop"],
5A38: 1A 02     ; "SCORE" : [
5A3A: 08        ;    "PrintScore"],
5A3B: 1B 02     ; "INVENT" : [
5A3D: 0F        ;    "PrintInventory"],
5A3E: 1C 02     ; "LOOK" : [
5A40: 10        ;    "PrintRoomDescription"],
5A41: 1D 04     ; "HELP" : [
5A43: 04 C4 74  ;    "PrintMessageX","I'M_AS_CONFUSED_AS_YOU_ARE.[CR]"],
5A46: 1E 04     ; "FIND" : [
5A48: 04 D8 74  ;    "PrintMessageX","I_CAN_ONLY_TELL_YOU_WHAT_YOU_SEE_AS_YOU_MOVE_ABOUT_AND__________MANIPULATE_THINGS.__I_CAN_NOT_TELL_YOU_WHERE_REMOTE_THINGS_ARE.[CR]"],
5A4B: 28 47     ; "TAKE" : [
5A4D: 07 06     ;    "SubScripXtAbortIfPass",[
5A4F: 11 07     ;        "AssertObjectXMatchesUserInput","#PLANT_A",
5A51: 04 61 7A  ;        "PrintMessageX","THE_PLANT_HAS_EXCEPTIONALLY_DEEP_ROOTS_AND_CANNOT_BE_PULLED_____FREE.[CR]"],
5A54: 07 17     ;    "SubScripXtAbortIfPass",[
5A56: 11 13     ;        "AssertObjectXMatchesUserInput","#BIRD",
5A58: 07 06     ;        "SubScripXtAbortIfPass",[
5A5A: 02 11     ;            "AssertObjectXIsInPack","#SCEPTER",
5A5C: 04 C7 7A  ;            "PrintMessageX","AS_YOU_APPROACH_THE_STATUE,_IT_COMES_TO_LIFE_AND_FLIES_ACROSS___THE_CHAMBER_WHERE_IT_LANDS_AND_RETURNS_TO_STONE.[CR]"],
5A5F: 07 09     ;        "SubScripXtAbortIfPass",[
5A61: 02 10     ;            "AssertObjectXIsInPack","#BOX",
5A63: 15 13 00  ;            "MoveObjectXToRoomY","#BIRD","room_0",
5A66: 19 14 10  ;            "MoveObjectXIntoContainerY","#BIRD_boxed","#BOX"],
5A69: 04 14 7B  ;        "PrintMessageX","YOU_CAN_LIFT_THE_STATUE,_BUT_YOU_CANNOT_CARRY_IT.[CR]"],
5A6C: 07 0A     ;    "SubScripXtAbortIfPass",[
5A6E: 11 20     ;        "AssertObjectXMatchesUserInput","#VASE_pillow",
5A70: 12 21     ;        "GetObjectFromRoom","#VASE_solo",
5A72: 15 20 00  ;        "MoveObjectXToRoomY","#VASE_pillow","room_0",
5A75: 18 12     ;        "MoveObjectXToCurrentRoom","#PILLOW"],
5A77: 07 0D     ;    "SubScripXtAbortIfPass",[
5A79: 11 1E     ;        "AssertObjectXMatchesUserInput","#STREAM_56",
5A7B: 07 06     ;        "SubScripXtAbortIfPass",[
5A7D: 02 1C     ;            "AssertObjectXIsInPack","#WATER",
5A7F: 04 37 7B  ;            "PrintMessageX","YOUR_BOTTLE_IS_ALREADY_FULL.[CR]"],
5A82: 19 1C 1B  ;        "MoveObjectXIntoContainerY","#WATER","#BOTTLE"],
5A85: 07 0C     ;    "SubScripXtAbortIfPass",[
5A87: 11 12     ;        "AssertObjectXMatchesUserInput","#PILLOW",
5A89: 1A 20     ;        "AssertObjectXIsInCurrentRoom","#VASE_pillow",
5A8B: 15 20 00  ;        "MoveObjectXToRoomY","#VASE_pillow","room_0",
5A8E: 18 21     ;        "MoveObjectXToCurrentRoom","#VASE_solo",
5A90: 12 12     ;        "GetObjectFromRoom","#PILLOW"],
5A92: 16        ;    "GetUserInputObject"],
5A93: 21 17     ; "DROP" : [
5A95: 07 14     ;    "SubScripXtAbortIfPass",[
5A97: 11 21     ;        "AssertObjectXMatchesUserInput","#VASE_solo",
5A99: 15 21 00  ;        "MoveObjectXToRoomY","#VASE_solo","room_0",
5A9C: 07 08     ;        "SubScripXtAbortIfPass",[
5A9E: 1A 12     ;            "AssertObjectXIsInCurrentRoom","#PILLOW",
5AA0: 18 20     ;            "MoveObjectXToCurrentRoom","#VASE_pillow",
5AA2: 04 15 7C  ;            "PrintMessageX","THE_VASE_IS_NOW_RESTING,_DELICATELY,_ON_A_VELVET_PILLOW.[CR]"],
5AA5: 18 15     ;        "MoveObjectXToCurrentRoom","#POTTERY",
5AA7: 04 3D 7C  ;        "PrintMessageX","THE_VASE_DROPS_WITH_A_DELICATE_CRASH.[CR]"],
5AAA: 17        ;    "DropUserInputObject"],
5AAB: 26 0E     ; "THROW" : [
5AAD: 07 0B     ;    "SubScripXtAbortIfPass",[
5AAF: 11 21     ;        "AssertObjectXMatchesUserInput","#VASE_solo",
5AB1: 15 21 00  ;        "MoveObjectXToRoomY","#VASE_solo","room_0",
5AB4: 18 15     ;        "MoveObjectXToCurrentRoom","#POTTERY",
5AB6: 04 75 7C  ;        "PrintMessageX","YOU_HAVE_TAKEN_THE_VASE_AND_HURLED_IT_DELICATELY_TO_THE_GROUND.[CR]"],
5AB9: 17        ;    "DropUserInputObject"],
5ABA: 29 36     ; "OPEN" : [
5ABC: 07 1C     ;    "SubScripXtAbortIfPass",[
5ABE: 11 17     ;        "AssertObjectXMatchesUserInput","#SARCOPH_full",
5AC0: 07 06     ;        "SubScripXtAbortIfPass",[
5AC2: 02 17     ;            "AssertObjectXIsInPack","#SARCOPH_full",
5AC4: 04 01 77  ;            "PrintMessageX","I'D_ADVISE_YOU_TO_PUT_DOWN_THE_SARCOPHAGUS_BEFORE_OPENING_IT!![CR]"],
5AC7: 07 0E     ;        "SubScripXtAbortIfPass",[
5AC9: 02 22     ;            "AssertObjectXIsInPack","#KEY",
5ACB: 04 BE 76  ;            "PrintMessageX","A_GLISTENING_PEARL_FALLS_OUT_OF_THE_SARCOPHAGUS_AND_ROLLS_AWAY._THE_SARCOPHAGUS_SNAPS_SHUT_AGAIN.[CR]",
5ACE: 15 16 40  ;            "MoveObjectXToRoomY","#PEARL","room_64",
5AD1: 15 17 00  ;            "MoveObjectXToRoomY","#SARCOPH_full","room_0",
5AD4: 18 18     ;            "MoveObjectXToCurrentRoom","#SARCOPH_empty"],
5AD6: 04 6B 77  ;        "PrintMessageX","YOU_DON'T_HAVE_ANYTHING_STRONG_ENOUGH_TO_OPEN_THE_SARCOPHAGUS.[CR]"],
5AD9: 07 14     ;    "SubScripXtAbortIfPass",[
5ADB: 11 18     ;        "AssertObjectXMatchesUserInput","#SARCOPH_empty",
5ADD: 07 06     ;        "SubScripXtAbortIfPass",[
5ADF: 02 18     ;            "AssertObjectXIsInPack","#SARCOPH_empty",
5AE1: 04 01 77  ;            "PrintMessageX","I'D_ADVISE_YOU_TO_PUT_DOWN_THE_SARCOPHAGUS_BEFORE_OPENING_IT!![CR]"],
5AE4: 07 06     ;        "SubScripXtAbortIfPass",[
5AE6: 02 22     ;            "AssertObjectXIsInPack","#KEY",
5AE8: 04 2D 77  ;            "PrintMessageX","THE_SARCOPHAGUS_CREAKS_OPEN,_REVEALING_NOTHING_INSIDE.__IT______PROMPTLY_SNAPS_SHUT_AGAIN.[CR]"],
5AEB: 04 6B 77  ;        "PrintMessageX","YOU_DON'T_HAVE_ANYTHING_STRONG_ENOUGH_TO_OPEN_THE_SARCOPHAGUS.[CR]"],
5AEE: 04 97 77  ;    "PrintMessageX","I_DON'T_KNOW_HOW_TO_LOCK_OR_UNLOCK_SUCH_A_THING.[CR]"],
5AF1: 23 04     ; "WAVE" : [
5AF3: 04 56 74  ;    "PrintMessageX","NOTHING_HAPPENS.[CR]"],
5AF6: 24 0E     ; "POUR" : [
5AF8: 07 09     ;    "SubScripXtAbortIfPass",[
5AFA: 11 1C     ;        "AssertObjectXMatchesUserInput","#WATER",
5AFC: 15 1C 00  ;        "MoveObjectXToRoomY","#WATER","room_0",
5AFF: 04 E9 75  ;        "PrintMessageX","YOUR_BOTTLE_IS_EMPTY_AND_THE_GROUND_IS_WET.[CR]"],
5B02: 04 08 76  ;    "PrintMessageX","YOU_CAN'T_POUR_THAT.[CR]"],
5B05: 25 12     ; "RUB" : [
5B07: 07 06     ;    "SubScripXtAbortIfPass",[
5B09: 11 0E     ;        "AssertObjectXMatchesUserInput","#LAMP_off",
5B0B: 04 18 76  ;        "PrintMessageX","RUBBING_THE_ELECTRIC_LAMP_IS_NOT_PARTICULARLY_REWARDING.________ANYWAY,_NOTHING_EXCITING_HAPPENS.[CR]"],
5B0E: 07 06     ;    "SubScripXtAbortIfPass",[
5B10: 11 0F     ;        "AssertObjectXMatchesUserInput","#LAMP_on",
5B12: 04 18 76  ;        "PrintMessageX","RUBBING_THE_ELECTRIC_LAMP_IS_NOT_PARTICULARLY_REWARDING.________ANYWAY,_NOTHING_EXCITING_HAPPENS.[CR]"],
5B15: 04 5B 76  ;    "PrintMessageX","PECULIAR.__NOTHING_UNEXPECTED_HAPPENS.[CR]"],
5B18: 27 12     ; "FILL" : [
5B1A: 07 06     ;    "SubScripXtAbortIfPass",[
5B1C: 11 1B     ;        "AssertObjectXMatchesUserInput","#BOTTLE",
5B1E: 04 77 76  ;        "PrintMessageX","THERE_IS_NOTHING_HERE_WITH_WHICH_TO_FILL_THE_BOTTLE.[CR]"],
5B21: 07 06     ;    "SubScripXtAbortIfPass",[
5B23: 11 21     ;        "AssertObjectXMatchesUserInput","#VASE_solo",
5B25: 04 D9 75  ;        "PrintMessageX","DON'T_BE_RIDICULOUS![CR]"],
5B28: 04 AE 76  ;    "PrintMessageX","YOU_CAN'T_FILL_THAT.[CR]"],
5B2B: 2C 2D     ; "ATTACK" : [
5B2D: 07 09     ;    "SubScripXtAbortIfPass",[
5B2F: 11 13     ;        "AssertObjectXMatchesUserInput","#BIRD",
5B31: 15 13 00  ;        "MoveObjectXToRoomY","#BIRD","room_0",
5B34: 04 B9 77  ;        "PrintMessageX","THE_BIRD_STATUE_IS_NOW_DEAD.__ITS_BODY_DISAPPEARS.[CR]"],
5B37: 07 09     ;    "SubScripXtAbortIfPass",[
5B39: 11 14     ;        "AssertObjectXMatchesUserInput","#BIRD_boxed",
5B3B: 15 14 00  ;        "MoveObjectXToRoomY","#BIRD_boxed","room_0",
5B3E: 04 B9 77  ;        "PrintMessageX","THE_BIRD_STATUE_IS_NOW_DEAD.__ITS_BODY_DISAPPEARS.[CR]"],
5B41: 07 06     ;    "SubScripXtAbortIfPass",[
5B43: 11 17     ;        "AssertObjectXMatchesUserInput","#SARCOPH_full",
5B45: 04 DD 77  ;        "PrintMessageX","THE_STONE_IS_VERY_STRONG_AND_IS_IMPERVIOUS_TO_ATTACK.[CR]"],
5B48: 07 06     ;    "SubScripXtAbortIfPass",[
5B4A: 11 18     ;        "AssertObjectXMatchesUserInput","#SARCOPH_empty",
5B4C: 04 DD 77  ;        "PrintMessageX","THE_STONE_IS_VERY_STRONG_AND_IS_IMPERVIOUS_TO_ATTACK.[CR]"],
5B4F: 07 06     ;    "SubScripXtAbortIfPass",[
5B51: 11 0B     ;        "AssertObjectXMatchesUserInput","#SERPENT",
5B53: 04 03 78  ;        "PrintMessageX","ATTACKING_THE_SERPENT_BOTH_DOESN'T_WORK_AND_IS_VERY_DANGEROUS.[CR]"],
5B56: 04 2F 78  ;    "PrintMessageX","YOU_CAN'T_BE_SERIOUS![CR]"],
5B59: 30 04     ; "BREAK" : [
5B5B: 04 3F 78  ;    "PrintMessageX","IT_IS_BEYOND_YOUR_POWER_TO_DO_THAT.[CR]"],
5B5E: 2E 23     ; "EAT" : [
5B60: 07 09     ;    "SubScripXtAbortIfPass",[
5B62: 11 1A     ;        "AssertObjectXMatchesUserInput","#FOOD",
5B64: 15 1A 00  ;        "MoveObjectXToRoomY","#FOOD","room_0",
5B67: 04 59 78  ;        "PrintMessageX","THANK_YOU,_IT_WAS_DELICIOUS![CR]"],
5B6A: 07 06     ;    "SubScripXtAbortIfPass",[
5B6C: 11 0A     ;        "AssertObjectXMatchesUserInput","#UNUSED_10",
5B6E: 04 6E 78  ;        "PrintMessageX","I_THINK_I_JUST_LOST_MY_APPETITE.[CR]"],
5B71: 07 06     ;    "SubScripXtAbortIfPass",[
5B73: 11 13     ;        "AssertObjectXMatchesUserInput","#BIRD",
5B75: 04 6E 78  ;        "PrintMessageX","I_THINK_I_JUST_LOST_MY_APPETITE.[CR]"],
5B78: 07 06     ;    "SubScripXtAbortIfPass",[
5B7A: 11 14     ;        "AssertObjectXMatchesUserInput","#BIRD_boxed",
5B7C: 04 6E 78  ;        "PrintMessageX","I_THINK_I_JUST_LOST_MY_APPETITE.[CR]"],
5B7F: 04 D9 75  ;    "PrintMessageX","DON'T_BE_RIDICULOUS![CR]"],
5B82: 2F 15     ; "DRINK" : [
5B84: 07 09     ;    "SubScripXtAbortIfPass",[
5B86: 11 1C     ;        "AssertObjectXMatchesUserInput","#WATER",
5B88: 15 1C 00  ;        "MoveObjectXToRoomY","#WATER","room_0",
5B8B: 04 9C 76  ;        "PrintMessageX","THE_BOTTLE_IS_NOW_EMPTY.[CR]"],
5B8E: 07 06     ;    "SubScripXtAbortIfPass",[
5B90: 11 1E     ;        "AssertObjectXMatchesUserInput","#STREAM_56",
5B92: 04 86 78  ;        "PrintMessageX","YOU_HAVE_TAKEN_A_DRINK_FROM_THE_STREAM.__THE_WATER_TASTES_______STRONGLY_OF_MINERALS,_BUT_IS_NOT_UNPLEASANT.__IT_IS_EXTREMELY___COLD.[CR]"],
5B95: 04 2F 78  ;    "PrintMessageX","YOU_CAN'T_BE_SERIOUS![CR]"],
5B98: 2D 38     ; "FEED" : [
5B9A: 07 06     ;    "SubScripXtAbortIfPass",[
5B9C: 11 13     ;        "AssertObjectXMatchesUserInput","#BIRD",
5B9E: 04 E1 78  ;        "PrintMessageX","IT'S_NOT_HUNGRY.__BESIDES,_YOU_HAVE_NO_BIRD_SEED.[CR]"],
5BA1: 07 06     ;    "SubScripXtAbortIfPass",[
5BA3: 11 14     ;        "AssertObjectXMatchesUserInput","#BIRD_boxed",
5BA5: 04 E1 78  ;        "PrintMessageX","IT'S_NOT_HUNGRY.__BESIDES,_YOU_HAVE_NO_BIRD_SEED.[CR]"],
5BA8: 07 10     ;    "SubScripXtAbortIfPass",[
5BAA: 11 0B     ;        "AssertObjectXMatchesUserInput","#SERPENT",
5BAC: 07 09     ;        "SubScripXtAbortIfPass",[
5BAE: 02 14     ;            "AssertObjectXIsInPack","#BIRD_boxed",
5BB0: 15 14 00  ;            "MoveObjectXToRoomY","#BIRD_boxed","room_0",
5BB3: 04 2B 79  ;            "PrintMessageX","THE_SERPENT_HAS_NOW_DEVOURED_YOUR_BIRD_STATUE.[CR]"],
5BB6: 04 4C 79  ;        "PrintMessageX","THERE_IS_NOTHING_HERE_IT_WANTS_TO_EAT_-_EXCEPT_PERHAPS_YOU.[CR]"],
5BB9: 07 06     ;    "SubScripXtAbortIfPass",[
5BBB: 11 17     ;        "AssertObjectXMatchesUserInput","#SARCOPH_full",
5BBD: 04 A7 79  ;        "PrintMessageX","I'M_GAME.__WOULD_YOU_CARE_TO_EXPLAIN_HOW?[CR]"],
5BC0: 07 06     ;    "SubScripXtAbortIfPass",[
5BC2: 11 18     ;        "AssertObjectXMatchesUserInput","#SARCOPH_empty",
5BC4: 04 A7 79  ;        "PrintMessageX","I'M_GAME.__WOULD_YOU_CARE_TO_EXPLAIN_HOW?[CR]"],
5BC7: 07 06     ;    "SubScripXtAbortIfPass",[
5BC9: 11 0D     ;        "AssertObjectXMatchesUserInput","#UNUSED_13",
5BCB: 04 4C 79  ;        "PrintMessageX","THERE_IS_NOTHING_HERE_IT_WANTS_TO_EAT_-_EXCEPT_PERHAPS_YOU.[CR]"],
5BCE: 04 D9 75  ;    "PrintMessageX","DON'T_BE_RIDICULOUS![CR]"],
5BD1: 39 02     ; "PLUGH" : [
5BD3: 1D        ;    "RandomizeDirections"],
5BD4: 3A 02     ; "LOAD" : [
5BD6: 1B        ;    "LoadGame"],
5BD7: 3B 02     ; "SAVE" : [
5BD9: 1C        ;    "SaveGame"]
5BDA: 00
```

# Room Descriptions

```code
RoomDescriptions:

; YOU_ARE_STANDING_BEFORE_THE_ENTRANCE_OF_A_PYRAMID.__AROUND_YOU__IS_A_DESERT.[CR]
5BDB: 19 C7 DE 94 14 55 5E 50 BD 90 5A C4 6A 59 60 5B 
5BEB: B1 5F BE 30 15 EB BF 17 98 B8 16 7B 14 14 A8 6B 
5BFB: 48 9B 5D 94 14 30 A1 1B 58 1B A1 D5 15 7B 14 F5 
5C0B: 59 3E 62 2E 00 

; YOU_ARE_IN_THE_ENTRANCE_TO_THE_PYRAMID.__A_HOLE_IN_THE_FLOOR____LEADS_TO_A_PASSAGE_BENEATH_THE_SURFACE.[CR]
5C10: 22 C7 DE 94 14 4B 5E 96 96 DB 72 9E 61 D0 B0 9B 
5C20: 53 6B BF 5F BE F3 16 CF B0 17 79 43 13 A9 15 DB 
5C30: 8B 83 7A 5F BE 56 15 44 A0 3B 13 3F 16 0D 47 89 
5C40: 17 7B 14 55 A4 09 B7 44 5E 8F 61 82 49 82 17 55 
5C50: 5E 30 C6 D7 46 2E 00 

; YOU_ARE_IN_THE_DESERT.[CR]
5C57: 07 C7 DE 94 14 4B 5E 96 96 DB 72 F5 59 3E 62 2E 
5C67: 00 

; YOU_ARE_IN_A_SMALL_CHAMBER_BENEATH_A_HOLE_FROM_THE_SURFACE.__A__LOW_CRAWL_LEADS_INWARD_TO_THE_WEST.__
; HIEROGLYPHICS_ON_THE_WALL__TRANSLATE,_"CURSE_ALL_WHO_ENTER_THIS_SACRED_CRYPT."[CR]
5C68: 3B C7 DE 94 14 4B 5E 83 96 5F 17 46 48 DA 14 64 
5C78: 48 23 62 70 4D 96 5F 03 71 A9 15 DB 8B 79 68 56 
5C88: 90 DB 72 34 BA C5 65 DB 63 7B 14 49 16 C5 CE D9 
5C98: B0 0E 8A 86 5F CB B5 33 9B 33 B1 6B BF 5F BE F7 
5CA8: 17 17 BA 4A 13 34 79 FE 9E E2 DE E5 78 C0 16 82 
5CB8: 17 59 5E 46 48 56 13 D0 B0 BB B8 FE BD 6D 13 3D 
5CC8: C6 43 5E F3 8C 29 D1 30 15 F4 BD 82 17 4B 7B 05 
5CD8: B7 66 B1 E4 14 EE DE 2E 22 00 

; YOU_ARE_CRAWLING_OVER_PEBBLES_IN_A_LOW_PASSAGE.__THERE_IS_A_DIM_LIGHT_AT_THE_EAST_END_OF_THE_PASSAGE.[CR]
5CE2: 21 C7 DE 94 14 45 5E D9 B0 90 8C D1 6A 74 CA DF 
5CF2: 16 F6 4C 4B 62 83 7A 4E 45 6B A1 55 A4 09 B7 DB 
5D02: 63 82 17 2F 62 D5 15 7B 14 8F 5A 43 16 2E 6D 96 
5D12: 14 82 17 47 5E 66 49 30 15 11 58 96 64 DB 72 55 
5D22: A4 09 B7 45 2E 00 

; YOU_ARE_IN_A_ROOM_FILLED_WITH_BROKEN_POTTERY_SHARDS_OF_ANCIENT__EGYPTIAN_CRAFTS.__AN_AWKWARD_CORRIDOR_LEADS_
; UPWARD_AND_WEST.[CR]
5D28: 29 C7 DE 94 14 4B 5E 83 96 39 17 DB 9F 0E 67 E6 
5D38: 8B FB 17 53 BE 79 4F B0 85 E9 16 3F C0 7B B4 1B 
5D48: B8 4D B1 B8 16 90 14 47 54 B3 9A 29 15 EE DE 90 
5D58: 78 E4 14 5E 47 5B BB 90 14 99 14 73 88 33 B1 44 
5D68: 55 06 B2 A3 A0 E3 8B 0B 5C F1 C5 2E 49 90 14 19 
5D78: 58 66 62 2E 00 

; YOU_ARE_IN_AN_AWKWARD_SLOPING_EAST/WEST_CORRIDOR.[CR]
5D7D: 10 C7 DE 94 14 4B 5E 83 96 83 96 A9 D1 2E 49 5E 
5D8D: 17 63 A0 AB 98 95 5F E1 BC 66 62 E1 14 73 B3 84 
5D9D: 5B 2E 00 

; YOU_ARE_IN_A_SPLENDID_CHAMBER_THIRTY_FEET_HIGH.__THE_WALLS_ARE__FROZEN_RIVERS_OF_ORANGE_STONE.__AN_AWKWARD_
; CORRIDOR_AND_A_GOOD__PASSAGE_EXIT_FROM_THE_EAST_AND_WEST_SIDES_OF_THE_CHAMBER.[CR]
5DA0: 3D C7 DE 94 14 4B 5E 83 96 62 17 F0 8B 86 5A DA 
5DB0: 14 64 48 23 62 63 BE D3 B3 4F 15 73 62 89 73 9B 
5DC0: 76 82 17 59 5E 46 48 C3 B5 5B B1 5C 15 EF A1 94 
5DD0: 96 CF 7B 8B B3 C3 9E AB A0 B7 98 66 17 0F A0 3B 
5DE0: F4 83 48 FD 49 14 D0 05 58 BC A0 09 79 83 AF 33 
5DF0: 98 49 45 36 A0 52 13 65 49 77 47 3A 15 73 7B 79 
5E00: 68 56 90 DB 72 95 5F 03 BC 33 98 B5 D0 15 BC FF 
5E10: 78 D1 B5 96 64 DB 72 1B 54 AF 91 52 2E 00 

; AT_YOUR_FEET_IS_A_SMALL_PIT_BREATHING_TRACES_OF_WHITE_MIST.__AN_EAST_PASSAGE_ENDS_HERE_EXCEPT_FOR_A_SMALL_CRACK_
; LEADING_ON._____ROUGH_STONE_STEPS_LEAD_DOWN_THE_PIT.[CR]
5E1E: 36 73 49 C7 DE 88 AF 36 60 D5 15 7B 14 E3 B8 F3 
5E2E: 8C 96 A5 BC 14 96 5F 90 73 D6 6A C5 B0 4B 62 C3 
5E3E: 9E 23 D1 DB BD D5 92 9B C1 90 14 23 15 F3 B9 55 
5E4E: A4 09 B7 47 5E 4D 98 9F 15 5B B1 1D 63 EE 61 59 
5E5E: 15 83 AF 5F 17 46 48 E4 14 DD 46 3F 16 03 47 AB 
5E6E: 98 27 A0 3B 13 54 13 29 A1 15 71 80 BF 55 5E F2 
5E7E: BD CE B5 86 5F 09 15 03 D2 5F BE E3 16 54 2E 00 

; YOU_ARE_AT_ONE_END_OF_A_VAST_HALL_STRETCHING_FORWARD_OUT_OF_____SIGHT_TO_THE_WEST.__THERE_ARE_OPENINGS_TO_EITHER_
; SIDE.__NEARBY,_A_WIDE_STONE_STAIRCASE_LEADS_DOWNWARD.__THE_HALL_IS_VERY_MUSTY__AND_A_COLD_WIND_BLOWS_UP_THE_
; STAIRCASE.__THERE_IS_A_PASSAGE_AT__THE_TOP_OF_A_DOME_BEHIND_YOU.__ROUGH_STONE_STEPS_LEAD_UP_THE____DOME.[CR]
5E8E: 6C C7 DE 94 14 43 5E 11 BC 5B 98 8E 61 B8 16 7B 
5E9E: 14 D5 C9 0A BC 46 48 66 17 76 B1 23 54 AB 98 04 
5EAE: 68 14 D0 11 58 73 C6 C3 9E 3B 13 5B 17 2E 6D 89 
5EBE: 17 82 17 59 5E 66 62 3B F4 5F BE 5B B1 2F 49 C2 
5ECE: 16 93 61 C5 98 89 17 2B 15 5F BE 95 AF FF 78 3B 
5EDE: F4 63 98 03 B1 03 EE FB 17 DB 59 09 BA 5B 98 FB 
5EEE: B9 2D 7B 57 49 3F 16 0D 47 09 15 21 D2 2E 49 3B 
5EFE: F4 5F BE 9B 15 F3 8C 4B 7B 74 CA 4F DB 66 C6 3B 
5F0E: DB 8E 48 7B 14 3E 55 19 58 8E 7A B6 14 85 A1 B2 
5F1E: 17 82 17 55 5E 4B BD 13 B1 BF B7 56 13 F4 72 4B 
5F2E: 5E C3 B5 DB 16 D3 B9 9B 6C 73 49 82 17 56 5E 53 
5F3E: A0 C3 9E 46 45 E7 9F AF 14 90 73 1B 58 3F A1 54 
5F4E: 13 29 A1 15 71 80 BF 55 5E F2 BD CE B5 86 5F B2 
5F5E: 17 82 17 3B 5E 46 13 E7 9F 2E 00 

; THIS_IS_A_LOW_ROOM_WITH_A_HIEROGLYPH_ON_THE_WALL.__IT_TRANSLATES"YOU_WON'T_GET_IT_UP_THE_STEPS".[CR]
5F69: 20 63 BE CB B5 C3 B5 49 16 D4 CE 3F A0 FB 17 53 
5F79: BE 4A 45 34 79 FE 9E E2 DE C0 16 82 17 59 5E 46 
5F89: 48 3B F4 73 7B EB BF 9E 9A 7F 49 03 B6 1B A1 40 
5F99: D2 F3 23 B6 6C D6 15 B2 17 82 17 55 5E F2 BD 07 
5FA9: B6 00 

; YOU_ARE_ON_THE_EAST_BANK_OF_A_BOTTOMLESS_PIT_STRETCHING_ACROSS__THE_HALL.__THE_MIST_IS_QUITE_THICK_HERE,_AND_THE_
; PIT_IS_TOO_WIDETO_JUMP.[CR]
5FAB: 2D C7 DE 94 14 51 5E 96 96 DB 72 95 5F 04 BC 95 
5FBB: 48 B8 16 7B 14 06 4F 7F BF F5 8B D2 B5 73 7B 0C 
5FCB: BA 7D 62 90 73 C3 6A B9 55 CB B9 82 17 4A 5E 46 
5FDB: 48 3B F4 5F BE 6B 16 F3 B9 4B 7B AB AD DB BD 63 
5FEB: BE 8B 54 F4 72 B3 63 8E 48 82 17 52 5E 73 7B 4B 
5FFB: 7B 81 BF FB 17 F6 59 CC 9C 72 C5 2E 00 

; YOU_ARE_IN_THE_PHARAOH'S_CHAMBER,_WITH_PASSAGES_OFF_IN_ALL______DIRECTIONS.[CR]
6008: 19 C7 DE 94 14 4B 5E 96 96 DB 72 5B A5 D1 B0 65 
6018: 71 DA 14 64 48 46 62 FB 17 53 BE 55 A4 09 B7 4B 
6028: 62 D0 9E D0 15 8E 14 FB 89 3B 13 03 15 65 B1 91 
6038: BE AF 9A 00 

; YOU_ARE_IN_THE_SOUTH_SIDE_CHAMBER.[CR]
603C: 0B C7 DE 94 14 4B 5E 96 96 DB 72 47 B9 53 BE 46 
604C: B8 45 5E 4F 72 74 4D 2E 00 

; YOU_ARE_ON_THE_WEST_SIDE_OF_THE_BOTTOMLESS_PIT_IN_THE_HALL_OF___GODS.[CR]
6055: 17 C7 DE 94 14 51 5E 96 96 DB 72 B5 D0 15 BC FF 
6065: 78 B8 16 82 17 44 5E 0E A1 EE 9F 65 62 E3 16 0B 
6075: BC 96 96 DB 72 4E 72 11 8A 7B 64 81 15 2F 5C 00 

; YOU_ARE_AT_THE_WEST_END_OF_THE_HALL_OF_GODS.___A_LOW_WIDE_PASS__CONTINUES_WEST_AND_ANOTHER_GOES_NORTH.__TO_THE_SOUTH_
; IS_A_LITTLEPASSAGE_SIX_FEET_OFF_THE_FLOOR.[CR]
6085: 35 C7 DE 94 14 43 5E 16 BC DB 72 B5 D0 07 BC 33 
6095: 98 C3 9E 5F BE 9B 15 F3 8C C3 9E 36 6E 5B BB 43 
60A5: 13 49 16 D9 CE FF 78 DB 16 CB B9 E1 14 C3 9A E7 
60B5: 9A D9 B5 66 62 90 14 03 58 06 9A F4 72 81 15 4B 
60C5: 62 04 9A 77 BE 56 13 D6 9C DB 72 47 B9 53 BE 4B 
60D5: 7B 4E 45 8E 7B F2 8B 65 49 77 47 5B 17 08 D5 36 
60E5: 60 B8 16 96 64 DB 72 89 67 C7 A0 00 

; YOU_ARE_AT_EAST_END_OF_A_VERY_LONG_HALL_APPARENTLY_WITHOUT_SIDE_CHAMBERS.__TO_THE_EAST_A_LOW_WIDE_CRAWL_SLANTS_UP.__TO_
; THE_NORTHA_ROUND_TWO_FOOT_HOLE_SLANTS_DOWN.[CR]
60F1: 36 C7 DE 94 14 43 5E 07 BC 66 49 30 15 11 58 83 
6101: 64 CF 17 7B B4 80 8D CA 6A 46 48 92 14 54 A4 9E 
6111: 61 FB 8E 56 D1 87 74 15 BC FF 78 DA 14 64 48 3D 
6121: 62 3B F4 6B BF 5F BE 23 15 F3 B9 4E 45 6B A1 46 
6131: D1 45 5E D9 B0 15 8A 50 8B 0B C0 F7 C5 56 13 D6 
6141: 9C DB 72 04 9A 5B BE 39 17 8E C5 91 17 C8 9C 46 
6151: A0 A9 15 DB 8B BB B8 CD 9A 09 15 27 D2 00 

; YOU_ARE_AT_THE_WEST_END_OF_A_VERY_LONG_FEATURELESS_HALL.__THE___HALL_JOINS_UP_WITH_A_NARROW_NORTH/SOUTH_PASSAGE.[CR]
615F: 25 C7 DE 94 14 43 5E 16 BC DB 72 B5 D0 07 BC 33 
616F: 98 C3 9E 58 45 43 62 49 16 AB 98 63 66 74 C0 3F 
617F: 61 CB B9 4E 72 9B 8F 82 17 3B 5E 9B 15 F3 8C FB 
618F: 80 8B 9A D3 C5 56 D1 03 71 8B 16 79 B3 D0 CE BE 
619F: A0 DD 71 36 A1 12 71 65 49 77 47 2E 00 

; YOU_ARE_AT_A_CROSSOVER_OF_A_HIGH_N/S_PASSAGE_AND_A_LOW_E/W_ONE.[CR]
61AC: 15 C7 DE 94 14 43 5E 03 BC E4 14 E5 A0 4F A1 91 
61BC: AF 83 64 A3 15 13 6D 5D 97 DB 16 D3 B9 9B 6C 8E 
61CC: 48 7B 14 89 8D 20 15 D1 CE 7F 98 00 

; DEAD_END.[CR]
61D8: 03 E3 59 07 58 57 98 00 

; YOU_ARE_IN_THE_WEST_THRONE_CHAMBER.__A_PASSAGE_CONTINUES_WEST___AND_UP_FROM_HERE.[CR]
61E0: 1B C7 DE 94 14 4B 5E 96 96 DB 72 B5 D0 16 BC F9 
61F0: 74 5B 98 1B 54 AF 91 1B B5 7B 14 55 A4 09 B7 45 
6200: 5E 1E A0 9F 7A 4B 62 B5 D0 FB BB 90 14 17 58 08 
6210: A3 FF B2 9F 15 7F B1 00 

; YOU_ARE_IN_A_LOW_N/S_PASSAGE_AT_A_HOLE_IN_THE_FLOOR.__THE_HOLE__GOES_DOWN_TO_AN_E/W_PASSAGE.[CR]
6218: 1E C7 DE 94 14 4B 5E 83 96 49 16 D0 CE 8B 36 55 
6228: A4 09 B7 43 5E 03 BC A9 15 DB 8B 83 7A 5F BE 56 
6238: 15 44 A0 3B F4 5F BE A9 15 DB 8B 81 15 4B 62 89 
6248: 5B 96 96 C3 9C 87 96 2B 37 55 A4 09 B7 45 2E 00 

; YOU_ARE_IN_A_LARGE_ROOM,_WITH_A_PASSAGE_TO_THE_SOUTH,_AND_A_WALLOF_BROKEN_ROCK_TO_THE_EAST.__THERE_IS_A_PANEL_
; ON_THE_NORTH_WALL.[CR]
6258: 2A C7 DE 94 14 4B 5E 83 96 3B 16 B7 B1 39 17 FE 
6268: 9F FB 17 53 BE 52 45 65 49 77 47 89 17 82 17 55 
6278: 5E 36 A1 73 76 8E 48 7B 14 0E D0 78 8D BC 14 97 
6288: 9F 94 96 5D 9E 89 17 82 17 47 5E 66 49 3B F4 5F 
6298: BE 5B B1 4B 7B 52 45 8F 48 11 8A 96 96 DB 72 04 
62A8: 9A 53 BE 0E D0 4C 2E 00 

; YOU_ARE_IN_THE_CHAMBER_OF_ANUBIS.[CR]
62B0: 0B C7 DE 94 14 4B 5E 96 96 DB 72 1B 54 AF 91 91 
62C0: AF 83 64 E4 9A 6F 7B 00 

; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
62C8: 10 C7 DE 94 14 4B 5E 83 96 63 16 5B E3 C3 9E BB 
62D8: C0 13 BA DB 16 D3 B9 B5 6C 03 EE F3 8C 43 48 BF 
62E8: 85 00 

; YOU_ARE_ON_THE_BRINK_OF_A_LARGE_PIT.__YOU_COULD_CLIMB_DOWN,_BUT_YOU_WOULD_NOT_BE_ABLE_TO_CLIMB_BACK_UP.__THE_MAZE_
; CONTINUES_ON__THIS_LEVEL.[CR]
62EA: 2E C7 DE 94 14 51 5E 96 96 DB 72 73 4F 4B 99 C3 
62FA: 9E 4E 45 31 49 52 5E 97 7B 5B 13 1B A1 47 55 B3 
630A: 8B C3 54 A3 91 89 5B F3 9B F6 4F 51 18 59 C2 2E 
631A: A1 10 58 F3 A0 5B 4D B6 46 56 5E C5 9C 8F 8C 84 
632A: 4B DD 46 B2 17 3B F4 5F BE 63 16 5B E3 40 55 90 
633A: BE 35 C4 C0 16 56 13 95 73 3F 16 6E CA 2E 00 

; YOU_ARE_IN_A_DIRTY_BROKEN_PASSAGE.__TO_THE_EAST_IS_A_CRAWL.__TO_THE_WEST_IS_A_LARGE_PASSAGE.__ABOVE_YOU_IS_A_
; HOLE_TO_ANOTHER____PASSAGE.[CR]
6349: 2D C7 DE 94 14 4B 5E 83 96 03 15 D3 B3 BC 14 97 
6359: 9F 92 96 65 49 77 47 3B F4 6B BF 5F BE 23 15 F3 
6369: B9 4B 7B 45 45 D9 B0 9B 8F 89 17 82 17 59 5E 66 
6379: 62 D5 15 7B 14 54 8B 9B 6C 55 A4 09 B7 DB 63 84 
6389: 14 4F A1 51 18 4B C2 C3 B5 A9 15 DB 8B 6B BF 99 
6399: 48 5F BE 7B AF 52 13 65 49 77 47 2E 00 

; YOU_ARE_ON_THE_BRINK_OF_A_SMALL_CLEAN_CLIMBABLE_PIT.__A_CRAWL___LEADS_WEST.[CR]
63A6: 19 C7 DE 94 14 51 5E 96 96 DB 72 73 4F 4B 99 C3 
63B6: 9E 55 45 8E 91 05 8A E3 8B 85 96 8F 8C C4 4C DB 
63C6: 8B 96 A5 3B F4 45 45 D9 B0 FB 89 3F 16 0D 47 F7 
63D6: 17 17 BA 00 

; YOU_ARE_IN_THE_BOTTOM_OF_A_SMALL_PIT_WITH_A_LITTLE_STREAM,_WHICHENTERS_AND_EXITS_THROUGH_TINY_SLITS.[CR]
63DA: 21 C7 DE 94 14 4B 5E 96 96 DB 72 06 4F 7F BF B8 
63EA: 16 7B 14 E3 B8 F3 8C 96 A5 FB 17 53 BE 4E 45 8E 
63FA: 7B DB 8B 0C BA 8F 5F 19 EE 85 73 F0 72 F4 BD C3 
640A: B5 33 98 23 63 0B C0 6C BE 29 A1 16 71 A3 7A 5E 
641A: 17 8D 7B 2E 00 

; YOU_ARE_IN_A_THE_ROOM_OF_BES,_WHOSE_PICTURE_IS_ON_THE_WALL._____THERE_IS_A_BIG_HOLE_IN_THE_FLOOR.__THERE_IS_
; A_PASSAGE_LEADING___EAST.[CR]
641F: 2C C7 DE 94 14 4B 5E 83 96 82 17 54 5E 3F A0 B8 
642F: 16 AF 14 33 BB 29 D1 9B B7 85 A5 74 C0 4B 5E D1 
643F: B5 96 96 DB 72 0E D0 9B 8F 3B 13 82 17 2F 62 D5 
644F: 15 7B 14 09 4E A9 15 DB 8B 83 7A 5F BE 56 15 44 
645F: A0 3B F4 5F BE 5B B1 4B 7B 52 45 65 49 77 47 3F 
646F: 16 03 47 AB 98 47 13 66 49 2E 00 

; YOU_ARE_AT_A_COMPLEX_JUNCTION.__A_LOW_HANDS_AND_KNEES_PASSAGE___FROM_THE_NORTH_JOINS_A_HIGHER_CRAWL_FROM_THE_
; EAST_TO_MAKE_A_____WALKING_PASSAGE_GOING_WEST.__THERE_IS_ALSO_A_LARGE_ROOM_ABOVE.__THE_AIR_IS_DAMP_HERE.[CR]
647A: 47 C7 DE 94 14 43 5E 03 BC E1 14 E6 93 13 63 F0 
648A: 81 03 56 27 A0 43 13 49 16 CA CE 8E 48 C3 B5 33 
649A: 98 0F 87 4B 62 55 A4 09 B7 3B 5E 5C 15 DB 9F 5F 
64AA: BE 99 16 C2 B3 F9 15 9D 7A 7B 14 89 73 F4 72 E4 
64BA: 14 FE 49 5C 15 DB 9F 5F BE 23 15 F3 B9 6B BF 8D 
64CA: 91 43 5E 3B 13 59 13 45 48 91 7A DB 16 D3 B9 9B 
64DA: 6C 3B 6E AB 98 B5 D0 9B C1 82 17 2F 62 D5 15 8E 
64EA: 14 2B B9 4E 45 31 49 54 5E 3F A0 84 14 4F A1 3B 
64FA: F4 5F BE 8B 14 8B AF C6 B5 72 48 9F 15 7F B1 00 

; YOU_ARE_IN_THE_UNDERWORLD_ANTEROOM_OF_SEKER.__PASSAGES_GO_EAST,_WEST,_AND_UP.__HUMAN_BONES_ARE_STREWN_ABOUT_ON_
; THE_FLOOR._______HIEROGLYPHICS_ON_THE_WALL_ROUGHLY_TRANSLATE_TO_"THOSE_WHO_______PROCEED_EAST_MAY_NEVER_RETURN."[CR]
650A: 4A C7 DE 94 14 4B 5E 96 96 DB 72 8E C5 41 62 B6 
651A: A0 03 58 BF 9A 01 B3 51 90 95 64 17 61 1B B5 DB 
652A: 16 D3 B9 B5 6C 81 15 23 15 16 BA F7 17 16 BA 90 
653A: 14 17 58 9B A8 AF 15 90 91 B9 14 75 98 94 14 55 
654A: 5E EF BF 03 D2 B9 46 73 C6 03 A0 5F BE 56 15 44 
655A: A0 3B F4 3B 13 4A 13 34 79 FE 9E E2 DE E5 78 C0 
656A: 16 82 17 59 5E 46 48 39 17 7A C4 FB 8E EB BF 9E 
657A: 9A 7F 49 89 17 7E 13 85 74 59 5E 6B 74 3B 13 3B 
658A: 13 F9 A6 A7 53 07 58 66 49 63 16 50 DB CF 62 94 
659A: AF 8F 62 E7 B2 22 00 

; YOU_ARE_AT_THE_LAND_OF_DEAD.__PASSAGES_LEAD_OFF_IN_>ALL<________DIRECTIONS.[CR]
65A1: 19 C7 DE 94 14 43 5E 16 BC DB 72 50 8B 11 58 86 
65B1: 64 86 5F 3B F4 55 A4 09 B7 4B 62 E3 8B 11 58 83 
65C1: 66 83 7A 8E 2D 73 8A 3B 13 3B 13 03 15 65 B1 91 
65D1: BE AF 9A 00 

; YOU'RE_IN_A_LARGE_ROOM_WITH_ANCIENT_DRAWINGS_ON_ALL_WALLS.______THE_PICTURES_DEPICT_ATUM,_A_PHARAOH_WEARING_THE_DOUBLE_
; CROWN.___A_SHALLOW_PASSAGE_PROCEEDS_DOWNWARD,_AND_A_SOMEWHAT_STEEPER_ONE_LEADS_UP.__A_LOW_HANDS_AND_KNEES_PASSAGE_
; ENTERS_FROM_THE_SOUTH. [CR]
65D5: 55 C7 DE AF 23 D0 15 7B 14 54 8B 9B 6C 01 B3 59 
65E5: 90 82 7B 90 14 47 54 B3 9A EB 5B 50 D1 CB 6E 03 
65F5: A0 46 48 F3 17 0D 8D 3B F4 3B 13 82 17 52 5E E6 
6605: 78 2F C6 C6 B5 E3 61 F3 55 8F 49 B3 95 52 45 54 
6615: 72 BA 48 F7 17 33 49 AB 98 5F BE 09 15 B6 C3 45 
6625: 5E 09 B3 1B 9C 43 13 5A 17 46 48 6B A1 55 A4 09 
6635: B7 52 5E F5 B2 26 60 C6 B5 80 A1 14 D0 73 5D 8E 
6645: 48 7B 14 3F B9 FA 62 73 49 FF B9 DF 61 91 AF 5B 
6655: 98 E3 8B 0B 5C F7 C5 43 13 49 16 CA CE 8E 48 C3 
6665: B5 33 98 0F 87 4B 62 55 A4 09 B7 47 5E BF 9A 8B 
6675: B3 79 68 56 90 DB 72 47 B9 77 BE 20 00 

; YOU_ARE_IN_A_CHAMBER_WHOSE_WALL_CONTAINS_A_PICTURE_OF_A_MAN_____WEARING_THE_LUNAR_DISK_ON_HIS_HEAD.__HE_IS_THE_GOD_
; KHONS,_THE___MOON_GOD.[CR]
6682: 2D C7 DE 94 14 4B 5E 83 96 DA 14 64 48 23 62 29 
6692: D1 9B B7 0E D0 05 8A 1E A0 D0 47 C3 B5 E3 16 0F 
66A2: 56 5B B1 C3 9E 4F 45 83 48 3B 13 F7 17 33 49 AB 
66B2: 98 5F BE 4F 16 D4 97 03 15 8B B8 03 A0 95 73 9F 
66C2: 15 17 47 4A 13 4B 5E D6 B5 DB 72 36 6E 1A 16 1D 
66D2: A0 16 EE DB 72 4F 13 40 A0 81 15 44 2E 00 

; YOU_ARE_IN_A_LONG_SLOPING_CORRIDOR_WITH_RAGGED_WALLS._ [CR]
66E0: 12 C7 DE 94 14 4B 5E 83 96 49 16 AB 98 C9 B8 90 
66F0: A5 C5 6A BC A0 09 79 99 AF 82 7B 2B 17 F7 6C 19 
6700: 58 46 48 5B BB 20 00 

; YOU_ARE_IN_A_CUL-DE-SAC_ABOUT_EIGHT_FEET_ACROSS.[CR]
6707: 10 C7 DE 94 14 4B 5E 83 96 E7 14 56 8F A5 63 CB 
6717: 46 B9 46 73 C6 C9 60 33 75 67 66 03 BC B9 55 EF 
6727: B9 00 

; YOU_ARE_IN_THE_CHAMBER_OF_HORUS,_A_LONG_EAST/WEST_PASSAGE_WITH__HOLES_EVERYWHERE.__TO_EXPLORE_AT_RANDOM,_SELECT_
; NORTH,_SOUTH,___UP,_OR_DOWN.[CR]
6729: 2E C7 DE 94 14 4B 5E 96 96 DB 72 1B 54 AF 91 91 
6739: AF 8A 64 BF A0 33 BB 4E 45 11 A0 23 15 F8 B9 B5 
6749: D0 12 BC 65 49 77 47 FB 17 53 BE A9 15 F5 8B 38 
6759: 15 43 62 1F D1 7F B1 56 13 C7 9C A6 D8 AF A0 96 
6769: 14 2B 17 49 98 B3 95 AE B7 E6 5F 99 16 C2 B3 15 
6779: EE 36 A1 73 76 57 13 73 A8 A3 A0 89 5B 4E 2E 00 

; YOU_ARE_IN_A_LARGE_LOW_CIRCULAR_CHAMBER_WHOSE_FLOOR_IS_AN_______IMMENSE_SLAB_FALLEN_FROM_THE_CEILING.__EAST_AND_
; WEST_THERE_ONCE_WHERE_LARGE_PASSAGES,_BUT_THEY_ARE_NOW_FILLED_WITH_SAND.________LOW_SMALL_PASSAGES_GO_NORTH_
; AND_SOUTH.[CR]
6789: 4C C7 DE 94 14 4B 5E 83 96 3B 16 B7 B1 49 16 C5 
6799: CE 2D 7B 3B C5 85 AF 4F 72 74 4D FA 17 D7 A0 56 
67A9: 15 44 A0 D5 15 90 14 3B 13 3B 13 CF 15 30 92 9B 
67B9: B7 BB B8 88 4B 46 48 83 61 79 68 56 90 DB 72 AB 
67C9: 53 90 8C 5B 70 23 15 F3 B9 8E 48 F7 17 F3 B9 5F 
67D9: BE 5B B1 0D A0 59 5E F4 72 4E 5E 31 49 52 5E 65 
67E9: 49 77 47 33 BB F6 4F 82 17 3B 63 2F 49 99 16 C8 
67F9: CE 46 7A F3 5F 56 D1 15 71 8E 48 3B F4 3B 13 3B 
6809: 13 89 8D 5F 17 46 48 DB 16 D3 B9 B5 6C 81 15 99 
6819: 16 C2 B3 90 14 15 58 36 A1 48 2E 00 

; YOU_ARE_IN_THE_PRIEST'S_BEDROOM.__THE_WALLS_ARE_COVERED_WITH____CURTAINS,_THE_FLOOR_WITH_A_THICK_PILE_
; CARPET.__MOSS_COVERS_THE__CEILING.[CR]
6825: 2D C7 DE 94 14 4B 5E 96 96 DB 72 F3 A6 66 62 CB 
6835: 23 66 4D 01 B3 DB 95 82 17 59 5E 46 48 C3 B5 5B 
6845: B1 48 55 2F 62 19 58 82 7B 3B 13 E7 14 BB B3 9D 
6855: 7A 16 EE DB 72 89 67 A3 A0 56 D1 03 71 82 17 DD 
6865: 78 E3 16 DB 8B 14 53 F6 A4 3B F4 C5 93 C5 B5 4F 
6875: A1 8B B3 5F BE 45 13 CE 60 91 7A 2E 00 

; THIS_IS_THE_CHAMBER_OF_THE_HIGH_PRIEST.___ANCIENT_DRAWINGS_COVERTHE_WALLS.__AN_EXTREMELY_TIGHT_TUNNEL_LEADS_
; WEST.__IT_LOOKS_LIKEA_TIGHT_SQUEEZE.__ANOTHER_PASSAGE_LEADS_SE.[CR]
6882: 39 63 BE CB B5 D6 B5 DB 72 1B 54 AF 91 91 AF 96 
6892: 64 DB 72 89 73 12 71 07 B2 17 BA 3B 13 8D 48 30 
68A2: 79 06 BC D9 B0 91 7A C5 B5 4F A1 C2 B3 59 5E 46 
68B2: 48 5B BB 90 14 3A 15 EF BF 2E 92 56 DB 7A 79 16 
68C2: BC 98 C5 33 61 E3 8B 0B 5C B5 D0 9B C1 D6 15 49 
68D2: 16 A5 9F 43 16 A3 85 83 17 2E 6D 63 17 27 C4 7F 
68E2: E3 43 13 06 9A F4 72 DB 16 D3 B9 9B 6C E3 8B 0B 
68F2: 5C BF B7 00 

; YOU_ARE_IN_THE_HIGH_PRIEST'S_TREASURE_ROOM_LIT_BY_AN_EERIE_GREENLIGHT.__A_NARROW_TUNNEL_EXITS_TO_THE_EAST.[CR]
68F6: 23 C7 DE 94 14 4B 5E 96 96 DB 72 89 73 12 71 07 
6906: B2 F5 B9 D6 B5 63 B1 34 BA 54 5E 3F A0 43 16 04 
6916: BC 43 DB 87 96 33 62 49 5E 67 B1 83 99 2E 6D 3B 
6926: F4 50 45 3C 49 6B A1 70 C0 6E 98 3A 15 8D 7B 89 
6936: 17 82 17 47 5E 66 49 2E 00 

; YOU_ARE_AT_THE_EAST_END_OF_THE_TWOPIT_ROOM.__THE_FLOOR_HERE_IS__LITTERED_WITH_THIN_ROCK_SLABS,_WHICH_MAKE_IT_
; EASY_TO_DESCEND_THEPITS.__THERE_IS_A_PATH_HERE_BYPASSING_THE_PITS_TO_CONNECT_______PASSAGES_EAST_AND_WEST.__THERE_
; ARE_HOLES_ALL_OVER,_BUT_THE_ONLY_BIG_ONE_IS_ON_THE_WALL_DIRECTLY_OVER_THE_WEST_PIT_WHERE_YOU_____CAN'T_GET_TO_IT.[CR]
693F: 70 C7 DE 94 14 43 5E 16 BC DB 72 95 5F 07 BC 33 
694F: 98 C3 9E 5F BE 91 17 63 A0 14 BC 3F A0 3B F4 5F 
695F: BE 56 15 44 A0 9F 15 5B B1 4B 7B 43 16 3F C0 66 
696F: B1 FB 17 53 BE 63 BE 94 96 5D 9E 5E 17 BD 46 19 
697F: EE 85 73 0F 71 17 48 D6 15 23 15 BB BA 6B BF F5 
698F: 59 B0 53 16 58 F2 72 8D 7B 3B F4 5F BE 5B B1 4B 
699F: 7B 52 45 82 49 9F 15 5B B1 92 50 65 49 91 7A 82 
69AF: 17 52 5E 8D 7B 89 17 E1 14 CF 99 F3 55 3B 13 3B 
69BF: 13 55 A4 09 B7 4B 62 95 5F 03 BC 33 98 B5 D0 9B 
69CF: C1 82 17 2F 62 94 14 4A 5E BF 9F C3 B5 F3 8C 4F 
69DF: A1 F3 B4 F6 4F 82 17 51 5E 93 99 B3 14 D1 6A 5B 
69EF: 98 4B 7B 03 A0 5F BE F3 17 F3 8C 94 5A E6 5F FB 
69FF: 8E 4F A1 96 AF DB 72 B5 D0 12 BC 73 7B 1F D1 5B 
6A0F: B1 C7 DE 3B 13 45 13 85 48 09 BC 73 62 6B BF 97 
6A1F: 7B 00 

; YOU_ARE_AT_THE_BOTTOM_OF_THE_EASTERN_PIT_IN_THE_TWOPIT_ROOM.[CR]
6A21: 14 C7 DE 94 14 43 5E 16 BC DB 72 06 4F 7F BF B8 
6A31: 16 82 17 47 5E 66 49 38 62 E3 16 0B BC 96 96 DB 
6A41: 72 C1 C0 96 A5 39 17 FF 9F 00 

; YOU_ARE_AT_THE_WEST_END_OF_THE_TWOPIT_ROOM.__THERE_IS_A_LARGE___HOLE_IN_THE_WALL_ABOVE_THE_PIT_AT_THIS_END_
; OF_THE_ROOM.[CR]
6A4B: 27 C7 DE 94 14 43 5E 16 BC DB 72 B5 D0 07 BC 33 
6A5B: 98 C3 9E 5F BE 91 17 63 A0 14 BC 3F A0 3B F4 5F 
6A6B: BE 5B B1 4B 7B 4E 45 31 49 3B 5E A9 15 DB 8B 83 
6A7B: 7A 5F BE F3 17 F3 8C B9 46 5B CA 5F BE E3 16 03 
6A8B: BC 16 BC 95 73 30 15 11 58 96 64 DB 72 01 B3 4D 
6A9B: 2E 00 

; YOU_ARE_AT_THE_BOTTOM_OF_THE_WEST_PIT_IN_THE_TWOPIT_ROOM.__THEREIS_A_LARGE_HOLE_IN_THE_WALL_ABOUT_TWENTY_FIVE_
; FEET_ABOVE_YOU.[CR]
6A9D: 29 C7 DE 94 14 43 5E 16 BC DB 72 06 4F 7F BF B8 
6AAD: 16 82 17 59 5E 66 62 E3 16 0B BC 96 96 DB 72 C1 
6ABD: C0 96 A5 39 17 FF 9F 56 13 F4 72 D5 60 7B 14 54 
6ACD: 8B 9B 6C 7E 74 4B 5E 96 96 DB 72 0E D0 03 8A 07 
6ADD: 4F 16 BC B0 D0 FB C0 18 67 48 5E 36 60 84 14 4F 
6AED: A1 51 18 55 2E 00 

; YOU_ARE_IN_A_LONG,_NARROW_CORRIDOR_STRETCHING_OUT_OF_SIGHT_TO___THE_WEST.__AT_THE_EASTERN_END_IS_A_HOLE_THROUGH_WHICH_YOU_
; CAN___SEE_A_PROFUSION_OF_LEAVES.[CR]
6AF3: 33 C7 DE 94 14 4B 5E 83 96 49 16 CE 98 8B 16 79 
6B03: B3 C5 CE BC A0 09 79 95 AF EF BF 9A BD 91 7A C7 
6B13: 16 11 BC 95 64 7A 79 16 BC BB 9C 82 17 59 5E 66 
6B23: 62 3B F4 73 49 5F BE 23 15 FF B9 C3 B2 8E 61 D5 
6B33: 15 7B 14 7E 74 56 5E F9 74 7A C4 FA 17 DA 78 51 
6B43: 18 45 C2 83 48 55 13 1B 60 52 45 F8 B2 5B C6 03 
6B53: A0 C3 9E E3 8B 75 CA 2E 00 

; YOU_ARE_IN_THE_CHAMBER_OF_OSIRIS._THE_CEILING_IS_TOO_HIGH_UP_FORYOUR_LAMP_TO_SHOW_IT.__PASSAGES_LEAD_
; EAST,_NORTH,_AND_SOUTH.[CR]
6B5C: 29 C7 DE 94 14 4B 5E 96 96 DB 72 1B 54 AF 91 91 
6B6C: AF 91 64 54 B8 6F 7B 82 17 45 5E CE 60 91 7A D5 
6B7C: 15 89 17 CA 9C 7A 79 B2 17 59 15 91 B4 23 C6 4F 
6B8C: 8B 16 A3 D5 9C 89 74 D6 15 3B F4 55 A4 09 B7 4B 
6B9C: 62 E3 8B 07 58 66 49 10 EE BE A0 73 76 8E 48 61 
6BAC: 17 82 C6 2E 00 

; THE_PASSAGE_HERE_IS_BLOCKED_BY_A_FALLEN_BLOCK.[CR]
6BB1: 0F 5F BE DB 16 D3 B9 9B 6C F4 72 4B 5E C4 B5 75 
6BC1: 8D A6 85 C3 14 7B 14 CE 65 F0 8B B6 14 5D 9E 2E 
6BD1: 00 

; YOU_ARE_IN_THE_CHAMBER_OF_NEKHEBET,_A_WOMAN_WITH_THE_HEAD_OF_A__VULTURE,_WEARING_THE_CROWN_OF_EGYPT.__A_PASSAGE_
; EXITS_TO_THE____SOUTH.[CR]
6BD2: 2C C7 DE 94 14 4B 5E 96 96 DB 72 1B 54 AF 91 91 
6BE2: AF 90 64 1A 61 AF 5F 73 C1 59 45 E3 9F 99 96 82 
6BF2: 7B 82 17 4A 5E 86 5F B8 16 7B 14 DF 17 4F 8E 7E 
6C02: B1 F7 17 33 49 AB 98 5F BE E4 14 80 A1 B8 16 29 
6C12: 15 EE DE 3B F4 52 45 65 49 77 47 3A 15 8D 7B 89 
6C22: 17 82 17 3B 5E 55 13 36 A1 48 2E 00         
```

# Object Descriptions

```code
; These are the long (in a room description) and short (in the inventory) strings for each object.

ObjDescriptions:

;Description for objects: 14 "Lamp (not lit)",44 "Lamp (dead)"

; THERE_IS_A_SHINY_BRASS_LAMP_NEARBY.[CR]
6C2E: 0B 5F BE 5B B1 4B 7B 55 45 90 73 44 DB D5 B0 CE 
6C3E: B5 72 48 8F 16 2C 49 59 2E 00 

; BRASS_LANTERN[CR]
6C48: 04 6B 4F CB B9 50 8B F4 BD 4E 00 

; THERE_IS_A_LAMP_SHINING_NEARBY.[CR]
6C53: 0A 5F BE 5B B1 4B 7B 4E 45 72 48 5A 17 93 7A AB 
6C63: 98 63 98 03 B1 2E 00 

; BRASS_LANTERN[CR]
6C6A: 04 6B 4F CB B9 50 8B F4 BD 4E 00 

; THERE_IS_A_SMALL_STATUE_BOX_DISCARDED_NEARBY.[CR]
6C75: 0F 5F BE 5B B1 4B 7B 55 45 8E 91 15 8A 56 BD 1B 
6C85: C4 0A 4F 03 15 53 B7 3F B1 10 58 94 5F 9F 50 00 

; STATUE_BOX[CR]
6C95: 03 FB B9 67 C0 B9 14 58 00 

; A_THREE_FOOT_SCEPTER_WITH_AN_ANKH_ON_AN_END_LIES_NEARBY.[CR]
6C9E: 12 56 45 EF 74 48 5E 46 A0 55 17 EE 61 23 62 56 
6CAE: D1 03 71 83 96 5A 99 C0 16 90 14 30 15 0E 58 35 
6CBE: 79 8F 16 2C 49 59 2E 00 

; SCEPTER[CR]
6CC6: 02 57 B7 3F A7 52 00 

; A_STATUE_OF_THE_BIRD_GOD_IS_SITTING_HERE.[CR]
6CCD: 0D 55 45 56 BD 1B C4 C3 9E 5F BE B3 14 33 B1 36 
6CDD: 6E D5 15 5B 17 43 C0 AB 98 F4 72 45 2E 00 

; THERE_IS_A_BIRD_STATUE_IN_THE_BOX.[CR]
6CEB: 0B 5F BE 5B B1 4B 7B 44 45 2E 7B 66 17 8F 49 4B 
6CFB: 5E 96 96 DB 72 0A 4F 2E 00 

; BIRD_STATUE_IN_BOX[CR]
6D04: 06 14 4E 15 58 56 BD 1B C4 83 7A 0A 4F 00 

; A_SMALL_VELVET_PILLOW_LIES_ON_THE_FLOOR.[CR]
6D12: 0D 55 45 8E 91 18 8A 50 61 73 62 8E A5 89 8D 43 
6D22: 16 4B 62 03 A0 5F BE 56 15 44 A0 2E 00 

; VELVET_PILLOW[CR]
6D2F: 04 6E CA 76 CA E3 16 09 8D 57 00 

; A_HUGE_GREEN_FIERCE_SERPENT_BARS_THE_WAY![CR]
6D3A: 0D 4A 45 77 C4 84 15 30 60 53 15 2D 62 55 5E 3A 
6D4A: 62 9E 61 AB 14 8B B3 5F BE F3 17 59 21 00 

; A_STONE_BRIDGE_NOW_SPANS_THE_BOTTOMLESS_PIT.[CR]
6D58: 0E 55 45 80 BF 44 5E 06 B2 9B 6C 09 9A 62 17 9D 
6D68: 48 82 17 44 5E 0E A1 EE 9F 65 62 E3 16 54 2E 00 

; THERE_IS_A_SARCOPHAGUS_HERE_WITH_IT'S_COVER_TIGHTLY_CLOSED.[CR]
6D78: 13 5F BE 5B B1 4B 7B 55 45 2D 49 62 A0 87 47 CA 
6D88: B5 2F 62 FB 17 53 BE 75 7B C5 B5 4F A1 96 AF 7A 
6D98: 79 13 BF DE 14 D7 A0 44 2E 00 

; SARCOPHAGUS_>GROAN<[CR]
6DA2: 06 14 B7 42 55 49 72 4B C6 84 2E 10 9E 3C 00 

; THERE_ARE_A_FEW_RECENT_ISSUES_OF_"EGYPTIAN_WEEKLY"_MAGAZINE_HERE[CR]
6DB1: 15 5F BE 5B B1 2F 49 7B 14 79 66 2F 17 B0 53 0B 
6DC1: BC E7 B9 4B 62 C3 9E 69 1B EE DE 90 78 F7 17 1E 
6DD1: 61 63 DB 89 91 73 4A 5B 98 F4 72 45 00 

; "EGYPTIAN_WEEKLY"[CR]
6DDE: 05 69 1B EE DE 90 78 F7 17 1E 61 59 22 00 

; THERE_IS_FOOD_HERE.[CR]
6DEC: 06 5F BE 5B B1 4B 7B 01 68 0A 58 2F 62 2E 00 

; TASTY_FOOD[CR]
6DFB: 03 55 BD FB C0 01 68 44 00 

; THERE_IS_A_BOTTLE_HERE.[CR]
6E04: 07 5F BE 5B B1 4B 7B 44 45 0E A1 DB 8B F4 72 45 
6E14: 2E 00 

; SMALL_BOTTLE[CR]
6E16: 04 E3 B8 F3 8C 06 4F FF BE 00 

; THERE_IS_WATER_IN_THE_BOTTLE.[CR]
6E20: 09 5F BE 5B B1 4B 7B 16 D0 23 62 83 7A 5F BE B9 
6E30: 14 46 C0 45 2E 00 

; WATER_IN_THE_BOTTLE[CR]
6E36: 06 16 D0 23 62 83 7A 5F BE B9 14 46 C0 45 00 

; THERE_IS_A_TINY_PLANT_IN_THE_PIT,_MURMURING_"WATER,_WATER,_..."[CR]
6E45: 15 5F BE 5B B1 4B 7B 56 45 A3 7A E6 16 9E 48 D0 
6E55: 15 82 17 52 5E 96 7B 77 16 B7 B2 10 B2 BC 6A 16 
6E65: D0 46 62 F3 17 F4 BD 1F EE DC F9 00 

; THERE_IS_A_TWELVE_FOOT_BEAN_STALK_STRETCHING_UP_OUT_OF_THE_PIT,_BELLOWING_"WATER..._WATER..."[CR]
6E71: 1F 5F BE 5B B1 4B 7B 56 45 AE D0 5B CA 01 68 04 
6E81: BC 90 5F 66 17 45 48 66 17 76 B1 23 54 AB 98 D3 
6E91: C5 36 A1 B8 16 82 17 52 5E 96 7B AF 14 09 8D 50 
6EA1: D1 BC 6A 16 D0 47 62 DB F9 16 D0 47 62 DC F9 00 

; THERE_IS_A_GIGANTIC_BEAN_STALK_STRETCHING_ALL_THE_WAY_UP_TO_THE_HOLE.[CR]
6EB1: 17 5F BE 5B B1 4B 7B 49 45 73 79 C3 9A C4 51 90 
6EC1: 5F 66 17 45 48 66 17 76 B1 23 54 AB 98 46 48 82 
6ED1: 17 59 5E 3B 4A D3 C5 6B BF 5F BE A9 15 FF 8B 00 

; THERE_IS_A_MASSIVE_VENDING_MACHINE_HERE.__THE_INSTRUCTIONS_ON_ITREAD-_"DROP_COINS_HERE_TO_
; RECIEVE_FRESH_BATTERIES".[CR]
6EE1: 26 5F BE 5B B1 4B 7B 4F 45 65 49 CF 7B CF 17 43 
6EF1: 98 AB 98 85 91 90 73 4A 5E 2F 62 3B F4 5F BE D0 
6F01: 15 0C BA E6 C3 C0 7A D1 B5 8B 96 EF BF 15 47 6E 
6F11: 13 02 B3 E1 14 9D 7A 9F 15 5B B1 6B BF 65 B1 38 
6F21: 79 48 5E 75 B1 04 71 8E 49 33 62 4C 62 2E 00 

; THERE_ARE_FRESH_BATTERIES_HERE.[CR]
6F30: 0A 5F BE 5B B1 2F 49 5C 15 5A 62 AB 14 3F C0 07 
6F40: B2 CA B5 2F 62 2E 00 

; BATTERIES[CR]
6F47: 03 D6 4C F4 BD 35 79 00 

; SOME_WORN-OUT_BATTERIES_HAVE_BEEN_DISCARDED_NEARBY.[CR]
6F4F: 11 3F B9 59 5E B8 A0 47 EB 04 BC 8E 49 33 62 4B 
6F5F: 62 58 72 44 5E 30 60 03 15 53 B7 3F B1 10 58 94 
6F6F: 5F 9F 50 00 

; BATTERIES[CR]
6F73: 03 D6 4C F4 BD 35 79 00 

; THERE_IS_A_LARGE_SPARKLING_NUGGET_OF_GOLD_HERE![CR]
6F7B: 0F 5F BE 5B B1 4B 7B 4E 45 31 49 55 5E 54 A4 C3 
6F8B: 86 AB 98 E9 9A B6 6C B8 16 81 15 B3 8B F4 72 45 
6F9B: 21 00 

; LARGE_GOLD_NUGGET[CR]
6F9D: 05 54 8B 9B 6C 3E 6E 10 58 79 C4 45 54 00 

; THERE_ARE_DIAMONDS_HERE![CR]
6FAB: 08 5F BE 5B B1 2F 49 03 15 71 48 4D 98 9F 15 59 
6FBB: B1 00 

; SEVERAL_DIAMONDS[CR]
6FBD: 05 B8 B7 2B 62 06 8A 8F 78 0E A0 53 00 

; THERE_ARE_BARS_OF_SILVER_HERE![CR]
6FCA: 0A 5F BE 5B B1 2F 49 AB 14 8B B3 C3 9E 4E B8 74 
6FDA: CA 9F 15 59 B1 00 

; SILVER_BARS[CR]
6FE0: 03 4E B8 74 CA AB 14 52 53 00 

; THERE_IS_PRECIOUS_JEWELRY_HERE![CR]
6FEA: 0A 5F BE 5B B1 4B 7B EF A6 51 54 4B C6 79 7F 4C 
6FFA: 61 4A DB 2F 62 21 00 

; PRECIOUS_JEWELRY[CR]
7001: 05 EF A6 51 54 4B C6 79 7F 4C 61 59 00 

; THERE_ARE_MANY_COINS_HERE![CR]
700E: 08 5F BE 5B B1 2F 49 63 16 7B 9B 3B 55 8B 9A F4 
701E: 72 45 21 00 

; RARE_COINS[CR]
7022: 03 D4 B0 45 5E 50 9F 53 00 

; THE_PHARAOH'S_TREASURE_CHEST_IS_HERE![CR]
702B: 0C 5F BE E2 16 2B 49 15 9F D6 B5 63 B1 34 BA 45 
703B: 5E F5 72 0B BC CA B5 2F 62 21 00 

; TREASURE_CHEST[CR]
7046: 04 EF BF 67 49 5B B1 1F 54 53 54 00 

; THERE_IS_A_LARGE_NEST_HERE,_FULL_OF_GOLDEN_EGGS![CR]
7052: 10 5F BE 5B B1 4B 7B 4E 45 31 49 50 5E 66 62 9F 
7062: 15 7E B1 5F 15 F3 8C C3 9E 3E 6E F0 59 29 15 C9 
7072: 6E 00 

; GOLDEN_EGGS[CR]
7074: 03 3E 6E F0 59 29 15 47 53 00 

; THERE_IS_A_JEWEL-ENCRUSTED_KEY_HERE![CR]
707E: 0C 5F BE 5B B1 4B 7B 4C 45 F7 62 57 8F 24 98 66 
708E: C6 F3 5F BB 85 9F 15 59 B1 00 

; JEWELED_KEY[CR]
7098: 03 79 7F 3F 61 0D 58 45 59 00 

; THERE_IS_A_DELICATE,_PRECIOUS,_VASE_HERE![CR]
70A2: 0D 5F BE 5B B1 4B 7B 46 45 43 61 16 53 B3 63 EF 
70B2: A6 51 54 6E C6 CB 17 9B B7 F4 72 45 21 00 

; VASE[CR]
70C0: 01 D5 C9 45 00 

; THE_VASE_IS_NOW_RESTING,_DELICATELY,_ON_A_VELVET_PILLOW.[CR]
70C5: 12 5F BE CB 17 9B B7 4B 7B 09 9A 2F 17 03 BA CE 
70D5: 98 FF 14 85 8C 7F 49 1E 8F C0 16 7B 14 6E CA 76 
70E5: CA E3 16 09 8D 57 2E 00 

; THE_FLOOR_IS_LITTERED_WITH_WORTHLESS_SHARDS_OF_POTTERY.[CR]
70ED: 12 5F BE 56 15 44 A0 D5 15 43 16 3F C0 66 B1 FB 
70FD: 17 53 BE 44 D2 66 BE 65 62 5A 17 2E 49 D1 B5 92 
710D: 64 0E A1 43 62 2E 00 

; THERE_IS_AN_EMERALD_HERE_THE_SIZE_OF_A_PLOVER'S_EGG![CR]
7114: 11 5F BE 5B B1 4B 7B 83 48 67 61 CE B0 0A 58 2F 
7124: 62 82 17 55 5E 6F 7C B8 16 7B 14 09 A6 74 CA CB 
7134: 23 79 60 21 00 

; EGG-SIZED_EMERALD[CR]
7139: 05 79 60 DB EB 66 E3 2F 15 2B 62 4C 44 00 

; OFF_TO_ONE_SIDE_LIES_A_GLISTENING_PEARL![CR]
7147: 0D D0 9E 89 17 C0 16 55 5E FF 78 43 16 4B 62 49 
7157: 45 95 8C F0 BD 91 7A DF 16 36 49 21 00 

; GLISTENING_PEARL[CR]
7164: 05 C3 6D FF B9 10 99 D2 6A 94 5F 4C 00 

; YOU_ARE_AT_THE_BOTTOM_OF_THE_PIT_WITH_A_BROKEN_NECK.[CR]
7171: 11 C7 DE 94 14 43 5E 16 BC DB 72 06 4F 7F BF B8 
7181: 16 82 17 52 5E 73 7B 56 D1 03 71 BC 14 97 9F 90 
7191: 96 DD 5F 2E 00 

; THE_CRACK_IS_FAR_TOO_SMALL_FOR_YOU_TO_FOLLOW.[CR]
7196: 0F 5F BE E4 14 DD 46 D5 15 4B 15 96 AF 2B A0 E3 
71A6: B8 F3 8C 04 68 51 18 56 C2 C8 9C C6 9F 8F A1 00 

; THE_DOME_IS_UNCLIMBABLE.[CR]
71B6: 08 5F BE 09 15 1B 92 4B 7B 8D C5 8F 8C C4 4C FF 
71C6: 8B 00 

; I_RESPECTFULLY_SUGGEST_YOU_GO_ACROSS_THE_BRIDGE_INSTEAD_OF______JUMPING.[CR]
71C8: 18 54 77 62 62 E6 5F EE 68 FB 8E 29 BA B5 6C 1B 
71D8: BC 1B A1 2B 6E E4 46 E5 A0 82 17 44 5E 06 B2 9B 
71E8: 6C 9D 7A E3 BD 11 58 7B 64 3B 13 FF 15 E3 93 CF 
71F8: 98 00 

; YOU_DIDN'T_MAKE_IT.[CR]
71FA: 06 C7 DE 03 15 45 5B 0F BC 17 48 D6 15 2E 00 

; THERE_IS_NO_WAY_ACROSS_THE_BOTTOMLESS_PIT.[CR]
7209: 0E 5F BE 5B B1 4B 7B EB 99 1B D0 85 14 05 B3 D6 
7219: B5 DB 72 06 4F 7F BF F5 8B D2 B5 97 7B 00 

; YOU_CAN'T_GET_BY_THE_SERPENT.[CR]
7227: 09 C7 DE D3 14 E6 96 77 15 04 BC 56 DB DB 72 B4 
7237: B7 F0 A4 54 2E 00 

; YOU_HAVE_CRAWLED_THROUGH_A_VERY_LOW_WIDE_PASSAGE_PARALLEL_TO_ANDNORTH_OF_THE_
; HALL_OF_GODS.[CR]
723D: 1E C7 DE 9B 15 5B CA AB 55 BF D1 16 58 F9 74 7A 
724D: C4 7B 14 74 CA 4E DB 6B A1 46 D1 52 5E 65 49 77 
725D: 47 DB 16 CE B0 EE 8B 89 17 90 14 59 5B C2 B3 B8 
726D: 16 82 17 4A 5E 46 48 B8 16 81 15 2F 5C 00 

; YOU_DON'T_FIT_THROUGH_TWO-INCH_SLIT![CR]
727B: 0C C7 DE 09 15 E6 96 53 15 16 BC F9 74 7A C4 91 
728B: 17 1B A2 1A 98 5E 17 71 7B 00 

; YOU_HAVE_CRAWLED_AROUND_IN_SOME_LITTLE_HOLES_AND_WOUND_UP_BACK__IN_THE_MAIN_
; PASSAGE.[CR]
7295: 1C C7 DE 9B 15 5B CA AB 55 BF D1 03 58 07 B3 33 
72A5: 98 83 7A 3F B9 4E 5E 8E 7B DB 8B 7E 74 4B 62 8E 
72B5: 48 01 18 8E C5 B2 17 AB 14 8B 54 D0 15 82 17 4F 
72C5: 5E D0 47 DB 16 D3 B9 BF 6C 00 

; YOU_HAVE_CRAWLED_AROUND_IN_SOME_LITTLE_HOLES_AND_FOUND_YOUR_WAY_BLOCKED_BY_A_FALLEN_
; SLAB.__YOU_ARE_NOW_BACK_IN_THE_MAIN_PASSAGE.[CR]
72CF: 2A C7 DE 9B 15 5B CA AB 55 BF D1 03 58 07 B3 33 
72DF: 98 83 7A 3F B9 4E 5E 8E 7B DB 8B 7E 74 4B 62 8E 
72EF: 48 59 15 8E C5 51 18 23 C6 1B D0 B6 14 5D 9E F3 
72FF: 5F 7B 50 48 45 46 48 83 61 BB B8 1B 51 51 18 43 
730F: C2 5B B1 09 9A AB 14 8B 54 83 7A 5F BE 63 16 83 
731F: 7A 55 A4 09 B7 45 2E 00 

; YOU_CAN'T_FIT_THIS_BIG_SARCOPHAGUS_THROUGH_THAT_LITTLE_PASSAGE![CR]
7327: 15 C7 DE D3 14 E6 96 53 15 16 BC 95 73 B3 14 D5 
7337: 6A 2D 49 62 A0 87 47 D6 B5 F9 74 7A C4 82 17 73 
7347: 49 96 8C FF BE DB 16 D3 B9 99 6C 00 

; SOMETHING_YOU'RE_CARRYING_WON'T_FIT_THROUGH_THE_TUNNEL_WITH_YOU.YOU'D_BEST_TAKE_
; INVENTORY_AND_DROP_SOMETHING.[CR]
7353: 24 3F B9 82 62 91 7A 51 18 A4 C2 45 5E 3C 49 D0 
7363: DD D9 6A 05 A0 08 BC 73 7B 6C BE 29 A1 16 71 DB 
7373: 72 70 C0 6E 98 FB 17 53 BE C7 DE 51 F9 96 C2 AF 
7383: 14 F3 B9 4D BD 4B 5E 0F 9B C9 9A 7B B4 8E 48 0C 
7393: 15 53 A0 3F B9 82 62 91 7A 2E 00 

; YOU_CLAMBER_UP_THE_PLANT_AND_SCURRY_THROUGH_THE_HOLE_AT_THE_TOP.[CR]
739E: 15 C7 DE DE 14 64 48 23 62 D3 C5 5F BE E6 16 9E 
73AE: 48 90 14 15 58 34 56 7B B4 6C BE 29 A1 16 71 DB 
73BE: 72 7E 74 43 5E 16 BC DB 72 82 BF 2E 00 

; YOU'VE_CLIMBED_UP_THE_PLANT_AND_OUT_OF_THE_PIT.[CR]
73CB: 0F C7 DE 4F 24 DE 14 64 7A F3 5F D3 C5 5F BE E6 
73DB: 16 9E 48 90 14 11 58 73 C6 C3 9E 5F BE E3 16 54 
73EB: 2E 00 

; THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]
73ED: 0F 5F BE 5B B1 4B 7B EB 99 1B D0 59 15 9B AF 1B 
73FD: A1 6B BF 2B 6E 5B BE 06 BC 2F 7B 03 56 27 A0 00 

; I_DON'T_KNOW_IN_FROM_OUT_HERE.__USE_COMPASS_POINTS.[CR]
740D: 11 46 77 05 A0 0D BC 09 9A D0 15 5C 15 DB 9F 36 
741D: A1 9F 15 7F B1 57 13 9B B7 3F 55 55 A4 D2 B5 50 
742D: 9F 2F C0 00 

; I_AM_UNSURE_HOW_YOU_ARE_FACING.__USE_COMPASS_POINTS.[CR]
7431: 11 43 77 57 90 A7 9A 5B B1 89 74 51 18 43 C2 5B 
7441: B1 C5 65 91 7A 3B F4 57 C6 E1 14 DB 93 CB B9 7B 
7451: A6 CD 9A 2E 00 

; NOTHING_HAPPENS.[CR]
7456: 05 06 9A 90 73 CA 6A EA 48 9D 61 2E 00 

; I_DON'T_KNOW_HOW.[CR]
7463: 05 46 77 05 A0 0D BC 09 9A A9 15 57 2E 00 

; I_DON'T_KNOW_HOW_TO_APPLY_THAT_WORD_HERE.[CR]
7471: 0D 46 77 05 A0 0D BC 09 9A A9 15 D6 CE C3 9C A6 
7481: A6 56 DB 56 72 01 18 33 B1 F4 72 45 2E 00 

; YOUR_LAMP_IS_NOW_ON.[CR]
748F: 06 C7 DE 8E AF 72 48 D5 15 99 16 D1 CE 4E 2E 00 

; YOU_HAVE_NO_SOURCE_OF_LIGHT.[CR]
749F: 09 C7 DE 9B 15 5B CA EB 99 47 B9 17 B1 B8 16 43 
74AF: 16 2E 6D 2E 00 

; YOUR_LAMP_IS_NOW_OFF.[CR]
74B4: 07 C7 DE 8E AF 72 48 D5 15 99 16 D1 CE A7 66 00 

; I'M_AS_CONFUSED_AS_YOU_ARE.[CR]
74C4: 09 9F 77 95 14 E1 14 9F 98 A6 B7 95 14 51 18 43 
74D4: C2 7F B1 00 

; I_CAN_ONLY_TELL_YOU_WHAT_YOU_SEE_AS_YOU_MOVE_ABOUT_AND__________MANIPULATE_THINGS.__I_CAN_
; NOT_TELL_YOU_WHERE_REMOTE_THINGS_ARE.[CR]
74D8: 2A 45 77 83 48 16 A0 56 DB 46 61 51 18 59 C2 56 
74E8: 72 51 18 55 C2 1B 60 4B 49 C7 DE 71 16 5B CA B9 
74F8: 46 73 C6 8E 48 3B 13 3B 13 3B 13 63 16 12 99 3B 
7508: C5 DB BD 63 BE C5 98 3B F4 45 77 83 48 06 9A 7F 
7518: 17 F3 8C C7 DE FA 17 2F 62 2F 17 C6 93 56 5E 90 
7528: 73 CB 6E 2F 49 2E 00 

; OK_[CR]
752F: 01 8B 9F 00 

; SORRY,_BUT_I_NO_LONGER_SEEM_TO_REMEMBER_HOW_IT_WAS_YOU_GOT_HERE.[CR]
7533: 15 44 B9 9E B4 BF 14 0B BC 99 16 49 16 B7 98 95 
7543: AF 2F 60 89 17 2F 17 2F 92 74 4D A9 15 CB CE 19 
7553: BC 4B 49 C7 DE 81 15 0A BC 2F 62 2E 00 

; YOU_ARE_ALREADY_CARRYING_IT.[CR]
7560: 09 C7 DE 94 14 43 5E EF 8D 13 47 D3 14 83 B3 91 
7570: 7A D6 15 2E 00 

; YOU_CAN'T_CARRY_ANYTHING_MORE.__YOU'LL_HAVE_TO_DROP_SOMETHING___FIRST.[CR]
7575: 17 C7 DE D3 14 E6 96 D3 14 83 B3 90 14 82 DF 91 
7585: 7A 71 16 7F B1 5B 13 1D A1 F3 8C 58 72 56 5E C6 
7595: 9C 02 B3 61 17 36 92 90 73 BB 6A 53 15 A6 B3 2E 
75A5: 00 

; YOU'RE_NOT_CARRYING_ANYTHING.[CR]
75A6: 09 C7 DE AF 23 99 16 05 BC 3C 49 D0 DD C3 6A 96 
75B6: 9B 90 73 47 2E 00 

; YOU_ARE_CURRENTLY_HOLDING_THE_FOLLOWING:[CR]
75BC: 0D C7 DE 94 14 45 5E 3C C6 9E 61 FB 8E 7E 74 90 
75CC: 5A D6 6A DB 72 FE 67 89 8D 91 7A 3A 00 

; DON'T_BE_RIDICULOUS![CR]
75D9: 06 80 5B F3 23 5B 4D 06 B2 E7 78 87 8D 53 21 00 

; YOUR_BOTTLE_IS_EMPTY_AND_THE_GROUND_IS_WET.[CR]
75E9: 0E C7 DE 84 AF 0E A1 DB 8B 4B 7B 72 61 FB C0 8E 
75F9: 48 82 17 49 5E 07 B3 33 98 4B 7B B6 D0 2E 00 

; YOU_CAN'T_POUR_THAT.[CR]
7608: 06 C7 DE D3 14 E6 96 E9 16 23 C6 5B BE 54 2E 00 

; RUBBING_THE_ELECTRIC_LAMP_IS_NOT_PARTICULARLY_REWARDING.________ANYWAY,_NOTHING_
; EXCITING_HAPPENS.[CR]
7618: 20 E4 B3 10 4E D6 6A DB 72 3F 61 0C 56 CB 78 4F 
7628: 8B 0B A3 D0 B5 F3 A0 54 A4 85 BE 3B C5 93 B2 2F 
7638: 17 14 D0 90 5A 5B 70 3B 13 3B 13 90 14 F3 DF B3 
7648: E0 06 9A 90 73 C7 6A 9B D6 90 BE CA 6A EA 48 9D 
7658: 61 2E 00 

; PECULIAR.__NOTHING_UNEXPECTED_HAPPENS.[CR]
765B: 0C E5 A4 43 C5 47 49 50 13 02 A1 91 7A B0 17 2A 
766B: 63 E6 5F F3 5F 52 72 F0 A4 53 2E 00 

; THERE_IS_NOTHING_HERE_WITH_WHICH_TO_FILL_THE_BOTTLE.[CR]
7677: 11 5F BE 5B B1 4B 7B 06 9A 90 73 CA 6A 2F 62 FB 
7687: 17 53 BE 23 D1 13 54 6B BF 0E 67 16 8A DB 72 06 
7697: 4F FF BE 2E 00 

; THE_BOTTLE_IS_NOW_EMPTY.[CR]
769C: 08 5F BE B9 14 46 C0 4B 5E D0 B5 6B A1 72 61 1F 
76AC: C1 00 

; YOU_CAN'T_FILL_THAT.[CR]
76AE: 06 C7 DE D3 14 E6 96 53 15 F3 8C 5B BE 54 2E 00 

; A_GLISTENING_PEARL_FALLS_OUT_OF_THE_SARCOPHAGUS_AND_ROLLS_AWAY._THE_SARCOPHAGUS_SNAPS_
; SHUT_AGAIN.[CR]
76BE: 20 49 45 95 8C F0 BD 91 7A DF 16 36 49 4B 15 0D 
76CE: 8D C7 16 11 BC 96 64 DB 72 14 B7 42 55 49 72 4B 
76DE: C6 8E 48 39 17 0D 8D 99 14 5F 4A 82 17 55 5E 2D 
76EE: 49 62 A0 87 47 D5 B5 D2 97 D5 B5 76 75 89 14 D0 
76FE: 47 2E 00 

; I'D_ADVISE_YOU_TO_PUT_DOWN_THE_SARCOPHAGUS_BEFORE_OPENING_IT!![CR]
7701: 14 96 77 86 14 15 CB 5B 5E 1B A1 6B BF 76 A7 09 
7711: 15 03 D2 5F BE 53 17 21 B1 5B A5 35 6F AF 14 04 
7721: 68 51 5E F0 A4 91 7A D6 15 21 21 00 

; THE_SARCOPHAGUS_CREAKS_OPEN,_REVEALING_NOTHING_INSIDE.__IT______PROMPTLY_SNAPS_SHUT_
; AGAIN.[CR]
772D: 1E 5F BE 53 17 21 B1 5B A5 35 6F E4 14 8D 5F D1 
773D: B5 F0 A4 14 EE CF 62 43 48 AB 98 06 9A 90 73 CB 
774D: 6A 9B 9A FF 59 4B 13 FB BB 3B 13 EC 16 F2 9F 13 
775D: BF 60 17 ED 48 5A 17 73 C6 73 47 A7 7A 00 

; YOU_DON'T_HAVE_ANYTHING_STRONG_ENOUGH_TO_OPEN_THE_SARCOPHAGUS.[CR]
776B: 14 C7 DE 09 15 E6 96 9B 15 5B CA A3 48 63 BE AB 
777B: 98 0C BA 11 A0 30 15 29 A1 16 71 D1 9C F0 A4 82 
778B: 17 55 5E 2D 49 62 A0 87 47 53 2E 00 

; I_DON'T_KNOW_HOW_TO_LOCK_OR_UNLOCK_SUCH_A_THING.[CR]
7797: 10 46 77 05 A0 0D BC 09 9A A9 15 D6 CE CE 9C 5D 
77A7: 9E C4 16 B0 17 75 8D D5 83 DA C3 7B 14 63 BE CF 
77B7: 98 00 

; THE_BIRD_STATUE_IS_NOW_DEAD.__ITS_BODY_DISAPPEARS.[CR]
77B9: 10 5F BE B3 14 33 B1 FB B9 67 C0 D5 15 99 16 C6 
77C9: CE 86 5F 3B F4 8D 7B B9 14 FB 5C 95 5A EA 48 94 
77D9: 5F 53 2E 00 

; THE_STONE_IS_VERY_STRONG_AND_IS_IMPERVIOUS_TO_ATTACK.[CR]
77DD: 11 5F BE 66 17 0F A0 D5 15 CF 17 7B B4 0C BA 11 
77ED: A0 90 14 0B 58 CB B5 DF 93 13 B4 35 A1 89 17 96 
77FD: 14 45 BD 4B 2E 00 

; ATTACKING_THE_SERPENT_BOTH_DOESN'T_WORK_AND_IS_VERY_DANGEROUS.[CR]
7803: 14 8E 49 DD 46 91 7A 82 17 55 5E 3A 62 9E 61 B9 
7813: 14 53 BE 77 5B 05 B9 19 BC B5 A0 90 14 0B 58 D8 
7823: B5 43 62 FB 14 B7 98 07 B3 53 2E 00 

; YOU_CAN'T_BE_SERIOUS![CR]
782F: 07 C7 DE D3 14 E6 96 AF 14 57 17 11 B2 49 C6 00 

; IT_IS_BEYOND_YOUR_POWER_TO_DO_THAT.[CR]
783F: 0B 73 7B 4B 7B 7B 4D 0E A0 51 18 23 C6 89 A6 23 
784F: 62 6B BF 6B 5B 5B BE 54 2E 00 

; THANK_YOU,_IT_WAS_DELICIOUS![CR]
7859: 09 5B BE 4B 99 C7 DE 0B EE 19 BC 4B 49 EE 59 DB 
7869: 78 35 A1 21 00 

; I_THINK_I_JUST_LOST_MY_APPETITE.[CR]
786E: 0A 56 77 90 73 CB 83 FF 15 F3 B9 85 8D 0F BC 43 
787E: DB 9F A6 96 BE 45 2E 00 

; YOU_HAVE_TAKEN_A_DRINK_FROM_THE_STREAM.__THE_WATER_TASTES_______STRONGLY_OF_
; MINERALS,_BUT_IS_NOT_UNPLEASANT.__IT_IS_EXTREMELY___COLD.[CR]
7886: 2C C7 DE 9B 15 5B CA 4D BD 83 61 46 45 10 B2 C8 
7896: 83 FF B2 82 17 55 5E EF BF 7F 48 56 13 DB 72 16 
78A6: D0 23 62 55 BD F5 BD 3B 13 3B 13 66 17 00 B3 D3 
78B6: 6D B8 16 6B 16 74 98 4D 48 04 EE 73 C6 4B 7B 06 
78C6: 9A B0 17 FF A5 53 49 D7 9A 4B 13 0B BC C7 B5 4C 
78D6: D9 67 61 FB 8E 45 13 BE 9F 2E 00 

; IT'S_NOT_HUNGRY.__BESIDES,_YOU_HAVE_NO_BIRD_SEED.[CR]
78E1: 10 75 7B D0 B5 F3 A0 70 75 C3 6E 3B F4 75 4D FF 
78F1: 78 33 BB C7 DE 9B 15 5B CA EB 99 14 4E 15 58 26 
7901: 60 2E 00 

; YOU_FELL_INTO_A_PIT_AND_BROKE_EVERY_BONE_IN_YOUR_BODY. [CR]
7904: 12 C7 DE 4F 15 F3 8C 9E 7A C3 9C E3 16 03 BC 33 
7914: 98 79 4F 9B 85 CF 62 7B B4 00 4F 4B 5E 9B 96 34 
7924: A1 B9 14 1F 5D 20 00 

; THE_SERPENT_HAS_NOW_DEVOURED_YOUR_BIRD_STATUE.[CR]
792B: 0F 5F BE 57 17 1F B3 B3 9A 55 72 99 16 C6 CE D9 
793B: 62 2F C6 1B 58 34 A1 B3 14 33 B1 FB B9 67 C0 2E 
794B: 00 

; THERE_IS_NOTHING_HERE_IT_WANTS_TO_EAT_-_EXCEPT_PERHAPS_YOU.[CR]
794C: 13 5F BE 5B B1 4B 7B 06 9A 90 73 CA 6A 2F 62 D6 
795C: 15 F3 17 CD 9A 89 17 23 15 1D BC 3A 15 B2 53 12 
796C: BC 32 62 ED 48 51 18 55 2E 00 

; IT_IS_NOW_PITCH_DARK.__IF_YOU_PROCEED,_YOU_WILL_LIKELY_FALL_INTOA_PIT.[CR]
7976: 17 73 7B 4B 7B 09 9A E3 16 9A BD FB 14 6F B2 4B 
7986: 13 9B 64 1B A1 F9 A6 A7 53 73 5D C7 DE FB 17 F3 
7996: 8C 8D 8C 53 61 4B 15 F3 8C 9E 7A FB 9D 96 A5 2E 
79A6: 00 

; I'M_GAME.__WOULD_YOU_CARE_TO_EXPLAIN_HOW?[CR]
79A7: 0D 9F 77 73 15 3F 92 59 13 2E A1 1B 58 1B A1 14 
79B7: 53 56 5E C7 9C A6 D8 D0 47 A9 15 57 3F 00 

; YOUR_LAMP_IS_GETTING_DIM.__YOU'D_BEST_START_WRAPPING_THIS_UP,___UNLESS_YOU_CAN_
; FIND_SOME_FRESH_BATTERIES.__I_SEEM_TO_RECALL_____THERE_IS_A_VENDING_MACHINE_IN_
; THE_MAZE.__BRING_SOME_COINS_WITH__YOU.[CR]
79C5: 41 C7 DE 8E AF 72 48 D5 15 77 15 43 C0 AB 98 8F 
79D5: 5A 3B F4 C7 DE 73 21 75 4D 15 BC 54 BD 19 BC D2 
79E5: B0 90 A5 D6 6A 95 73 B2 17 FB ED B0 17 F5 8B DB 
79F5: B5 1B A1 10 53 53 15 33 98 3F B9 48 5E 75 B1 04 
7A05: 71 8E 49 33 62 6F 62 4B 13 57 17 5B 61 6B BF 65 
7A15: B1 46 48 3B 13 56 13 F4 72 4B 5E C3 B5 CF 17 43 
7A25: 98 AB 98 85 91 90 73 4B 5E 96 96 DB 72 9C 91 DB 
7A35: 63 BC 14 91 7A 61 17 1B 92 3B 55 8B 9A 56 D1 FB 
7A45: 70 C7 DE 2E 00 

; YOUR_LAMP_HAS_RUN_OUT_OF_POWER.[CR]
7A4A: 0A C7 DE 8E AF 72 48 9B 15 D4 B5 83 C5 36 A1 B8 
7A5A: 16 E9 16 B4 D0 2E 00 

; THE_PLANT_HAS_EXCEPTIONALLY_DEEP_ROOTS_AND_CANNOT_BE_PULLED_____FREE.[CR]
7A61: 17 5F BE E6 16 9E 48 9B 15 C7 B5 97 D6 43 A7 0B 
7A71: A0 13 8D FF 14 D3 61 01 B3 0B C0 8E 48 D3 14 D9 
7A81: 99 04 BC 52 5E 46 C5 F3 5F 3B 13 5C 15 3F 60 00 

; YOUR_LAMP_IS_GETTING_DIM.__I'M_TAKING_THE_LIBERTY_OF_REPLACING__THE_BATTERIES.[CR]
7A91: 1A C7 DE 8E AF 72 48 D5 15 77 15 43 C0 AB 98 8F 
7AA1: 5A 3B F4 9F 77 7B 17 50 86 D6 6A DB 72 84 8C 3E 
7AB1: 62 51 DB 94 64 E6 61 DB 46 AB 98 82 17 44 5E 8E 
7AC1: 49 33 62 6F 62 00 

; AS_YOU_APPROACH_THE_STATUE,_IT_COMES_TO_LIFE_AND_FLIES_ACROSS___THE_CHAMBER_WHERE_IT_
; LANDS_AND_RETURNS_TO_STONE.[CR]
7AC7: 25 4B 49 C7 DE 92 14 F9 A6 DA 46 82 17 55 5E 56 
7AD7: BD 3E C4 D6 15 E1 14 35 92 89 17 43 16 5B 66 8E 
7AE7: 48 56 15 35 79 85 14 05 B3 BB B5 82 17 45 5E 4F 
7AF7: 72 74 4D FA 17 2F 62 D6 15 3B 16 4D 98 90 14 14 
7B07: 58 8F 62 DD B2 89 17 66 17 0F A0 2E 00 

; YOU_CAN_LIFT_THE_STATUE,_BUT_YOU_CANNOT_CARRY_IT.[CR]
7B14: 10 C7 DE D3 14 8E 96 5E 79 82 17 55 5E 56 BD 3E 
7B24: C4 BF 14 1B BC 1B A1 10 53 06 9A D3 14 83 B3 D6 
7B34: 15 2E 00 

; YOUR_BOTTLE_IS_ALREADY_FULL.[CR]
7B37: 09 C7 DE 84 AF 0E A1 DB 8B 4B 7B 4C 48 86 5F 48 
7B47: DB 46 C5 2E 00 

; _____SUDDENLY,_A_MUMMY_CREEPS_UP_BEHIND_YOU!!______"I'M_THE_____KEEPER_OF_THE_TOMB",__HE_WAILS,_"I_TAKE_
; THESE_TREASURES_AND_PUT_THEM_IN_THE_CHEST_DEEP_IN_THE_MAZE!"__HE_GRABS_YOUR_TREASURE_ANDVANISHES_INTO_THE_GLOOM.[CR]
7B4C: 48 3B 13 55 13 FE C3 96 61 B3 E0 4F 45 6F C5 45 
7B5C: DB 67 B1 0B A7 D3 C5 6A 4D 8E 7A 51 18 E9 C1 3B 
7B6C: 13 3B 13 FD 1B 56 90 DB 72 3B 13 17 16 DF 61 91 
7B7C: AF 96 64 DB 72 7F BF C6 4B 4A 13 59 5E CE 47 33 
7B8C: BB FB 1B 4D BD 56 5E F5 72 56 5E 63 B1 34 BA 4B 
7B9C: 62 8E 48 EF 16 16 BC EF 72 D0 15 82 17 45 5E F5 
7BAC: 72 06 BC 32 60 D0 15 82 17 4F 5E 6F 4A E3 06 9F 
7BBC: 15 84 15 BD 46 51 18 23 C6 EF BF 67 49 5B B1 8E 
7BCC: 48 D0 C9 5A 7B 4B 62 9E 7A D6 9C DB 72 C9 6D FF 
7BDC: 9F 00 

; THE_STONE_BRIDGE_HAS_RETRACTED![CR]
7BDE: 0A 5F BE 66 17 0F A0 BC 14 01 79 4A 5E 4B 49 76 
7BEE: B1 C5 B0 E6 BD 21 00 

; A_STONE_BRIDGE_NOW_SPANS_THE_BOTTOMLESS_PIT.[CR]
7BF5: 0E 55 45 80 BF 44 5E 06 B2 9B 6C 09 9A 62 17 9D 
7C05: 48 82 17 44 5E 0E A1 EE 9F 65 62 E3 16 54 2E 00 

; THE_VASE_IS_NOW_RESTING,_DELICATELY,_ON_A_VELVET_PILLOW.[CR]
7C15: 12 5F BE CB 17 9B B7 4B 7B 09 9A 2F 17 03 BA CE 
7C25: 98 FF 14 85 8C 7F 49 1E 8F C0 16 7B 14 6E CA 76 
7C35: CA E3 16 09 8D 57 2E 00 

; THE_VASE_DROPS_WITH_A_DELICATE_CRASH.[CR]
7C3D: 0C 5F BE CB 17 9B B7 F9 5B 0B A7 56 D1 03 71 FF 
7C4D: 14 85 8C 7F 49 E4 14 5A 49 2E 00 

; THERE_ARE_NOW_SOME_FRESH_BATTERIES_HERE.[CR]
7C58: 0D 5F BE 5B B1 2F 49 99 16 D5 CE E7 9F 5C 15 5A 
7C68: 62 AB 14 3F C0 07 B2 CA B5 2F 62 2E 00 

; YOU_HAVE_TAKEN_THE_VASE_AND_HURLED_IT_DELICATELY_TO_THE_GROUND.[CR]
7C75: 15 C7 DE 9B 15 5B CA 4D BD 83 61 5F BE CB 17 9B 
7C85: B7 8E 48 AF 15 7F B2 0B 58 06 BC 43 61 16 53 53 
7C95: 61 89 17 82 17 49 5E 07 B3 57 98 00 

; THE_BIRD_STATUE_COMES_TO_LIFE_AND_ATTACKS_THE_SERPENT_AND_IN_AN_ASTOUNDING_FLURRY,_DRIVES_THE_SERPENT_
; AWAY.__THE_BIRD_TURNS_BACKINTO_A_STATUE.[CR]
7CA1: 2F 5F BE B3 14 33 B1 FB B9 67 C0 E1 14 35 92 89 
7CB1: 17 43 16 5B 66 8E 48 96 14 45 BD CB 87 5F BE 57 
7CC1: 17 1F B3 B3 9A 8E 48 D0 15 90 14 95 14 87 BF 43 
7CD1: 98 AB 98 8F 67 83 B3 06 EE 18 B2 4B 62 5F BE 57 
7CE1: 17 1F B3 B3 9A F3 49 DB E0 82 17 44 5E 2E 7B 8F 
7CF1: 17 DD B2 AB 14 9B 54 C9 9A 7B 14 FB B9 67 C0 2E 
7D01: 00 

; THE_PLANT_SPURTS_INTO_FURIOUS_GROWTH_FOR_A_FEW_SECONDS.[CR]
7D02: 12 5F BE E6 16 9E 48 62 17 3E C6 CB B5 C9 9A 5F 
7D12: 15 11 B2 4B C6 B9 6E 02 D3 59 15 83 AF 4F 15 D5 
7D22: CE E1 5F 4D 98 2E 00 

; THE_PLANT_GROWS_EXPLOSIVELY,_ALMOST_FILLING_THE_BOTTOM_OF_THE___PIT.[CR]
7D29: 16 5F BE E6 16 9E 48 84 15 85 A1 3A 15 09 A6 58 
7D39: B8 53 61 03 EE 31 8D F3 B9 0E 67 90 8C D6 6A DB 
7D49: 72 06 4F 7F BF B8 16 82 17 3B 5E E3 16 54 2E 00 

; YOU'VE_OVER-WATERED_THE_PLANT!__IT'S_SHRIVELING_UP![CR]
7D59: 11 C7 DE 4F 24 C8 16 45 62 16 D0 2F 62 16 58 DB 
7D69: 72 FB A5 B1 9A 4B 13 65 BC 5A 17 18 B2 43 61 AB 
7D79: 98 D1 C5 00 

; THERE_IS_NOTHING_HERE_TO_CLIMB.__USE_UP_OR_OUT_TO_LEAVE_THE_PIT.[CR]
7D7D: 15 5F BE 5B B1 4B 7B 06 9A 90 73 CA 6A 2F 62 89 
7D8D: 17 DE 14 64 7A 3B F4 57 C6 B2 17 C4 16 C7 16 16 
7D9D: BC CE 9C 98 5F 56 5E DB 72 96 A5 2E 00 

; OH_DEAR,_YOU_SEEM_TO_HAVE_GOTTEN_YOURSELF_KILLED.__I_MIGHT_BE___ABLE_TO_HELP_YOU_OUT,_BUT_I'VE_NEVER_
; REALLY_DONE_THIS_BEFORE.___DO_YOU_WANT_ME_TO_TRY_TO_REINCARNATE_YOU?[CR]
7DAA: 38 13 9F E3 59 F3 B4 C7 DE 57 17 5B 61 6B BF 58 
7DBA: 72 49 5E 0E A1 83 61 C7 DE 97 B3 03 8C 4E 86 E6 
7DCA: 8B 3B F4 4F 77 7A 79 04 BC 3B 5E 84 14 DB 8B 6B 
7DDA: BF EE 72 1B A3 1B A1 36 A1 04 EE 73 C6 A8 77 50 
7DEA: 5E CF 62 94 AF 8E 5F FB 8E 80 5B 56 5E 95 73 AF 
7DFA: 14 04 68 DB 63 46 13 DB 9C 1B A1 10 D0 0F BC 56 
7E0A: 5E D6 9C 7B B4 6B BF 6B B1 13 98 CB B2 DB BD C7 
7E1A: DE 3F 00 

; YOU_CLUMSY_OAF,_YOU'VE_DONE_IT_AGAIN!__I_DON'T_KNOW_HOW_LONG_I__CAN_KEEP_THIS_UP.__DO_YOU_WANT_ME_TO_
; TRY_REINCARNATING_YOU______AGAIN?[CR]
7E1D: 2C C7 DE DE 14 75 C5 51 DB 66 47 51 18 A8 C2 46 
7E2D: 5E 0F A0 D6 15 89 14 D0 47 BB 06 46 77 05 A0 0D 
7E3D: BC 09 9A A9 15 CE CE 11 A0 BB 15 D3 14 8D 96 32 
7E4D: 60 82 17 4B 7B F7 C5 46 13 DB 9C 1B A1 10 D0 0F 
7E5D: BC 56 5E D6 9C 7B B4 6B B1 13 98 CB B2 90 BE DB 
7E6D: 6A 1B A1 3B 13 43 13 0B 6C 4E 3F 00 

; I_SEEM_TO_BE_OUT_OF_ORANGE_SMOKE.__HOW_CAN_I_REINCARNATE_YOU____WITHOUT_ORANGE_SMOKE?[CR]
7E79: 1C 55 77 2F 60 89 17 AF 14 C7 16 11 BC 91 64 D0 
7E89: B0 9B 6C F1 B8 BF 85 4A 13 6B A1 10 53 BB 15 6B 
7E99: B1 13 98 CB B2 DB BD C7 DE 3B 13 FB 17 69 BE 73 
7EA9: C6 AB A0 B7 98 5F 17 97 9F 3F 00 

; ALL_RIGHT.__BUT_DON'T_BLAME_ME_IF_SOMETHING_GOES_WR.............______________________----__
; POOF_!!__----_______________________YOU_ARE_ENGULFED_IN_A_CLOUD_OF_ORANGE_SMOKE.__COUGHING_
; AND______GASPING,_YOU_EMERGE_FROM_THE_SMOKE.[CR]
7EB4: 4B 46 48 33 17 2E 6D 3B F4 F6 4F 09 15 E6 96 B6 
7EC4: 14 67 48 67 16 C8 15 61 17 36 92 90 73 C9 6A B5 
7ED4: 9E 04 18 FF F9 FF F9 FF F9 FF F9 3B F4 3B 13 3B 
7EE4: 13 3B 13 3B 13 3B 13 3B 13 5D 13 2D ED 52 13 38 
7EF4: A0 E9 12 5D 13 2D ED 3B 13 3B 13 3B 13 3B 13 3B 
7F04: 13 3B 13 3B 13 5B 13 1B A1 2F 49 30 15 2E 6F 66 
7F14: 66 D0 15 7B 14 C9 54 F3 C3 C3 9E AB A0 B7 98 5F 
7F24: 17 97 9F 3B F4 47 55 23 6D AB 98 8E 48 3B 13 3B 
7F34: 13 15 6C 90 A5 33 70 C7 DE 2F 15 31 62 48 5E FF 
7F44: B2 82 17 55 5E BD 93 45 2E 00 

; OKAY,_NOW_WHERE_DID_I_PUT_MY_ORANGE_SMOKE?..._>POOF!<___________EVERYTHING_DISAPPEARS_IN_A_
; DENSE_CLOUD_OF_ORANGE_SMOKE.[CR]
7F4E: 27 93 9F B3 E0 09 9A FA 17 2F 62 03 15 0B 58 EF 
7F5E: 16 0F BC 51 DB D0 B0 9B 6C F1 B8 98 85 FF F9 F2 
7F6E: 13 38 A0 33 07 3B 13 3B 13 3B 13 38 15 43 62 63 
7F7E: BE AB 98 95 5A EA 48 94 5F CB B5 83 96 FF 14 97 
7F8E: 9A DE 14 26 A1 B8 16 C4 16 91 48 55 5E BD 93 45 
7F9E: 2E 00 

; READY_CASSETTE[CR]
7FA0: 04 63 B1 FB 5C 15 53 B6 B7 54 45 00 

; CHECKSUM_ERROR[CR]
7FAC: 04 1F 54 A5 54 5B C5 3C 62 4F 52 00 

; OH,_NO!__I_LOST_MY_COMPASS.__I_NO_LONGER_SEEM_TO_KNOW_WHICH_WAY_IS_NORTH![CR]
7FB8: 18 36 9F 99 16 BB 06 4E 77 E6 A0 7B 16 E1 14 DB 
7FC8: 93 EF B9 4B 13 99 16 49 16 B7 98 95 AF 2F 60 89 
7FD8: 17 20 16 6B A1 23 D1 13 54 1B D0 D5 15 99 16 C2 
7FE8: B3 21 00 

; ??
7FEB: 39 00 39 00 39 00 39 00                 
7FF3: 39 00 39 00 39 00 39 00                   
7FFB: 39 00 39 00 47   
;          
8000: 78 00 43 FF FF           
```

