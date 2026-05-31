![TRS-80 Pyramid](TRS80Pyramid.jpg)

# Pyramid (For TRS80 Level 1 ROM)

>>> cpu Z80

>>> binary 4200:roms/Pyramid1.bin

>>> memoryTable ram 

[RAM Usage](RAMUse1.md)

>>> memoryTable hard 

[Hardware Info](../Hardware.md)

# Start

```code
Start: 
4200: 31 5C 47        LD      SP,$475C            ; Stack
; ROM Level 2 of the game code clears the screen here
4203: 21 1F 47        LD      HL,$471F            ; {+code.WelcomeMsg} "WELCOME TO PYRAMID!!"
4206: CD CB 44        CALL    $44CB               ; {code.PrintPlain} Print the message
4209: CD E9 44        CALL    $44E9               ; {code.WaitForKey} Wait for a key

420C: 3E 01           LD      A,$01               ; Starting room is ...
420E: 32 DC 4F        LD      ($4FDC),A           ; {ram.CurrentRoom} ... room 1
4211: CD E2 51        CALL    $51E2               ; {code.DescribeRoom} Print room description

GameLoop:
4214: 97              SUB     A                   ; A=0
4215: 32 18 46        LD      ($4618),A           ; {code.noun} Clear noun (object within reach)
4218: 32 19 46        LD      ($4619),A           ; {code.verb} Clear verb (throw, north, rub, etc)
421B: 32 1A 46        LD      ($461A),A           ; {code.grammar} Grammar type (verb, verb+nounInReach, verb+nounInPack)
421E: CD CA 42        CALL    $42CA               ; {code.ParseUserInput} Get user input line and parse
4221: 3A DC 4F        LD      A,($4FDC)           ; {ram.CurrentRoom} Room number
4224: 21 25 48        LD      HL,$4825            ; {+code.RoomTable} Room descriptors
4227: CD 66 42        CALL    $4266               ; {code.TableOffsetFourBytes} Get 4 bytes for room
422A: 23              INC     HL                  ; Skip over ...
422B: 23              INC     HL                  ; ... to room's script pointer
422C: 7E              LD      A,(HL)              ; Script ...
422D: 23              INC     HL                  ; ... pointer ...
422E: 66              LD      H,(HL)              ; ... to ...
422F: 6F              LD      L,A                 ; ... HL
4230: CD 78 42        CALL    $4278               ; {code.ProcessRoomScript} Process the room script
4233: C2 45 42        JP      NZ,$4245            ; {} ZF clear ... script was successful. Move on.
4236: 21 04 59        LD      HL,$5904            ; {+code.GeneralCommandHandler} General script
4239: CD 78 42        CALL    $4278               ; {code.ProcessRoomScript} Process the script
423C: C2 45 42        JP      NZ,$4245            ; {} Process the script
423F: 21 C5 73        LD      HL,$73C5            ; {+code.PS_7F} General fail message (one of 4 that changes)
4242: CD A9 44        CALL    $44A9               ; {code.PrintPacked} Print message
4245: CD 76 50        CALL    $5076               ; {code.AfterEveryStep} After every turn
4248: C3 14 42        JP      $4214               ; {code.GameLoop} Back to get user input
```

# Get Object Info

Every object has a room number. The object might be physically in the room. Or the object
might be inside another object that is physically in the room -- or so on recursively.

This function traverses the containers to find out the room number this object and any
containers are in.

```code
GetObjectInfo:
; Recurse through carriers to find the room number of the requested object. 
; Return HL points to the top level object entry. 
; Return ZF is set if top level object room number matches E.
424B: 21 84 4F        LD      HL,$4F84            ; {+code.ObjectData} Information about all the objects
424E: CD 5C 42        CALL    $425C               ; {code.TableOffsetTwoBytes} Room number to 2-byte table entry
4251: 7E              LD      A,(HL)              ; Upper bit set means 2nd byte is object number
4252: E6 80           AND     $80                 ; Is this object being carried by another?
4254: 23              INC     HL                  ; Second byte (S is not affected)
4255: 7E              LD      A,(HL)              ; Get location (S is not affected)
4256: C2 4B 42        JP      NZ,$424B            ; {code.GetObjectInfo} If this is being carried, recurse to the carrier
4259: 2B              DEC     HL                  ; Back to first entry for return
425A: BB              CP      E                   ; Room number matches E?
425B: C9              RET                         

TableOffsetTwoBytes:
; HL = HL + (A-1)*2
425C: D5              PUSH    DE                  ; Hold DE
425D: EB              EX      DE,HL               ; HL to DE for later add
425E: 6F              LD      L,A                 ; LSB ...
425F: 2D              DEC     L                   ; ... minus one
4260: 26 00           LD      H,$00               ; Upper byte is 0
4262: 29              ADD     HL,HL               ; Times 2 (2 byte entries)
4263: 19              ADD     HL,DE               ; Offset into table
4264: D1              POP     DE                  ; Restore DE
4265: C9              RET                         ; HL = HL + (A-1)*2

TableOffsetFourBytes:
; HL = HL + (A-1)*4
4266: D5              PUSH    DE                  ; Hold DE
4267: EB              EX      DE,HL               ; HL to DE for later add
4268: 6F              LD      L,A                 ; LSB ...
4269: 2D              DEC     L                   ; ... minus one
426A: 26 00           LD      H,$00               ; Upper byte is 0
426C: 29              ADD     HL,HL               ; Times 2
426D: 29              ADD     HL,HL               ; Times 4 (4 byte entries)
426E: 19              ADD     HL,DE               ; Offset into table
426F: D1              POP     DE                  ; Restore DE
4270: C9              RET                         ; HL = HL + (A-1)*4

SetObjectLocation:
; Set object's location by recursing containers to the top
; level container and setting the room number.
; E is the new room number for the top level container
4271: CD 4B 42        CALL    $424B               ; {code.GetObjectInfo} Find the parent container
4274: 23              INC     HL                  ; Second entry is location
4275: 73              LD      (HL),E              ; Set the room number of the parent container
4276: 2B              DEC     HL                  ; Back to 1st entry
4277: C9              RET                         
```

# Process Room Scripts

Each room is a collection of verb and the script commands that go with each verb. We look through
the verb-map for the room and run the list of script commands for that verb.

As soon as an individual command fails, we stop the processing of the list. As long as the commands 
are passing, we continue to run them.

Interestingly, if a command list for a verb FAILS, we continue looking for verb matches in the 
collection. That allows for multiple command lists to be given for the same verb.

If the user verb matches the collection and all the commands pass, we return with NOT ZERO as a sign
of success. If there is no match or if any of the commands fail, we return with ZERO as a sign
of failure.

```code
; Process the user input against the script for a room
ProcessRoomScript:
4278: 7E              LD      A,(HL)              ; Next byte from script
4279: A7              AND     A                   ; Are we at the end?
427A: C8              RET     Z                   ; Yes, we are done. Return ZERO as FAIL.
;
427B: 3A 19 46        LD      A,($4619)           ; {code.verb} User's input verb
427E: BE              CP      (HL)                ; Does the input verb match the script verb?
427F: 23              INC     HL                  ; Point to next byte
4280: CA 8A 42        JP      Z,$428A             ; {} Yes, dive into this script
4283: 4E              LD      C,(HL)              ; No, get the length of this verb section
4284: 06 00           LD      B,$00               ; No script section over 256 bytes!
4286: 09              ADD     HL,BC               ; Jump to next section
4287: C3 78 42        JP      $4278               ; {code.ProcessRoomScript} Try next script verb
;
428A: CD 91 42        CALL    $4291               ; {code.RunScript} Run the script
428D: C0              RET     NZ                  ; All the commands passed. Return not ZERO as SUCCESS
428E: C3 78 42        JP      $4278               ; {code.ProcessRoomScript} In case there are duplicate verbs -- others might succeed
```

# Run Script

```code
RunScript:
4291: E5              PUSH    HL                  ; Hold the script pointer
4292: 4E              LD      C,(HL)              ; Get the length
4293: 06 00           LD      B,$00               ; Point to the end ...
4295: 09              ADD     HL,BC               ; ... of the script
4296: E3              EX      (SP),HL             ; Now the end of the script is on the stack
4297: 23              INC     HL                  ; Next byte is the command
;
RunScriptCommand:
4298: 7E              LD      A,(HL)              ; Get the command number
4299: 23              INC     HL                  ; Next in command
429A: E5              PUSH    HL                  ; Hold our pointer
429B: 21 3C 50        LD      HL,$503C            ; {+code.ScriptCommands} Table of script commands
429E: CD 5C 42        CALL    $425C               ; {code.TableOffsetTwoBytes} Offset into table
42A1: 7E              LD      A,(HL)              ; Hold LSB from table
42A2: 23              INC     HL                  ; Get the ...
42A3: 66              LD      H,(HL)              ; ... msb to H
42A4: 6F              LD      L,A                 ; HL now points to the routine to run
42A5: E9              JP      (HL)                ; Jump to the command
```

# Script Command PASS

When an individual command succeeds, it comes here. If there are no more commands
left in the script, we return with ZF cleared as a sign of success. If there are
commands left, we continue running the next one.

```code
ScriptCommandPASS:
42A6: E1              POP     HL                  ; The current script pointer
42A7: D1              POP     DE                  ; The calculated end of the script
42A8: 7C              LD      A,H                 ; Are we at the ...
42A9: BA              CP      D                   ; ... end of the script?
42AA: C2 B5 42        JP      NZ,$42B5            ; {} No ... keep going
42AD: 7D              LD      A,L                 ; Are we at the ...
42AE: BB              CP      E                   ; ... end of the script?
42AF: C2 B5 42        JP      NZ,$42B5            ; {} No ... keep going
42B2: F6 01           OR      $01                 ; Clear the ZERO flag for success
42B4: C9              RET                         ; Done
;
42B5: D5              PUSH    DE                  ; Put the calculated end of script back on stack
42B6: C3 98 42        JP      $4298               ; {code.RunScriptCommand} Run the next command
```

# Script Command FAIL

When an individual command fails, it comes here. We return ZF set as a sign of failure. No more
commands are run.

```code
ScriptCommandFAIL:
42B9: E1              POP     HL                  ; Pop the script pointer
42BA: E1              POP     HL                  ; Pop the calculated end of the script
42BB: AF              XOR     A                   ; Set the ZERO flag meaning failure
42BC: C9              RET                         
```

# Command 7: StopIfPassElseContinue

```code
StopIfPassElseContinue:
; Run the list of commands (a sub-script). We always return SUCCESS, but if the list completes
; successfully all the way to the end, we abort the outer script. If the sub-script fails,
; the we pass to the next command in the outer script.
;
; This gives us the ability to code a line of if/else commands. We keep trying the sub-lists
; until one finishes completely.
;
42BD: E1              POP     HL                  ; Pop the current pointer
42BE: CD 91 42        CALL    $4291               ; {code.RunScript} Run the list of commands
42C1: E5              PUSH    HL                  ; Current script position
42C2: CA A6 42        JP      Z,$42A6             ; {code.ScriptCommandPASS} The list failed ... treat that as a PASS
; The subscript failed. Bail out (with a PASS)
42C5: E1              POP     HL                  ; Pop the current pointer
42C6: E1              POP     HL                  ; Pop the calculated end of list
42C7: F6 01           OR      $01                 ; Return NOT ZERO ... a PASS
42C9: C9              RET                         
```

# Parse User Input

```code
ParseUserInput:
42CA: CD 98 45        CALL    $4598               ; {code.PromptAndReadLine} Get the command line from the player
42CD: CD 9D 43        CALL    $439D               ; {code.ParseInputString} Parse the input string
42D0: 2A A5 44        LD      HL,($44A5)          ; {code.nounPointer} Pointer to the noun word
42D3: 3A A3 44        LD      A,($44A3)           ; {code.numBytesWordData} Number of bytes ...
42D6: 47              LD      B,A                 ; ... in word data
42D7: 3A 1A 46        LD      A,($461A)           ; {code.grammar} Verb grammar
42DA: FE 03           CP      $03                 ; Value 3 means stand alone verb
42DC: CA CA 42        JP      Z,$42CA             ; {code.ParseUserInput} We needed a noun before but didn't get one. Get it now.
42DF: 3A 18 46        LD      A,($4618)           ; {code.noun} Do we have ..
42E2: A7              AND     A                   ; ... a noun?
42E3: C2 17 43        JP      NZ,$4317            ; {} Yes, go check it
42E6: 3A 19 46        LD      A,($4619)           ; {code.verb} Otherwise, do we have ...
42E9: A7              AND     A                   ; ... a verb?
42EA: C2 08 43        JP      NZ,$4308            ; {} Yes, go handle it
;
; General error message ... didn't understand a thing
42ED: 3A 1B 46        LD      A,($461B)           ; {code.nextErrorString} Last general error message
42F0: 3C              INC     A                   ; Point to next
42F1: E6 03           AND     $03                 ; Roll around over 4 messages
42F3: 32 1B 46        LD      ($461B),A           ; {code.nextErrorString} For next time
42F6: 21 1C 46        LD      HL,$461C            ; {+code.ErrorString1} Table of general error messages
42F9: 07              RLCA                        ; Two bytes each
42FA: 4F              LD      C,A                 ; All ...
42FB: 06 00           LD      B,$00               ; ... this ...
42FD: 09              ADD     HL,BC               ; ... to ...
42FE: 7E              LD      A,(HL)              ; ... add ...
42FF: 23              INC     HL                  ; ... C ...
4300: 66              LD      H,(HL)              ; ... to ...
4301: 6F              LD      L,A                 ; ... HL
4302: CD CB 44        CALL    $44CB               ; {code.PrintPlain} Print the error
4305: C3 CA 42        JP      $42CA               ; {code.ParseUserInput} Back for more
;
4308: 3A 1A 46        LD      A,($461A)           ; {code.grammar} Action word type
430B: FE C0           CP      $C0                 ; 11_000_000 means single word command
430D: C8              RET     Z                   ; Input is just one word, we are done
430E: 21 9A 46        LD      HL,$469A            ; {+code.unknownVerb} Unknown verb
4311: CD CB 44        CALL    $44CB               ; {code.PrintPlain} Print "verb WHAT?" (was expecting an object)
4314: C3 CA 42        JP      $42CA               ; {code.ParseUserInput} Try again
;
; Validate noun
4317: 22 A5 44        LD      ($44A5),HL          ; {code.nounPointer} Save pointer to noun word data
431A: 3A 9C 43        LD      A,($439C)           ; {code.isLoneObject} Was the last input an object and ...
431D: A7              AND     A                   ; ...  we then asked for a verb?
431E: C2 89 43        JP      NZ,$4389            ; {} Yes, skip checking the noun (use what we have)
4321: 7E              LD      A,(HL)              ; Get the object number
4322: 23              INC     HL                  ; Next word
4323: 22 A5 44        LD      ($44A5),HL          ; {code.nounPointer} Noun word data pointer
4326: 1E FF           LD      E,$FF               ; Backpack location
4328: C5              PUSH    BC                  ; Save BC
4329: CD 4B 42        CALL    $424B               ; {code.GetObjectInfo} Look up the requested object
432C: C1              POP     BC                  ; Restore BC
432D: CA 81 43        JP      Z,$4381             ; {} Object is actually in pack ... go use it
4330: 3A 1A 46        LD      A,($461A)           ; {code.grammar} Grammar type
4333: FE 40           CP      $40                 ; 01_000_000 means noun-in-pack
4335: CA 49 43        JP      Z,$4349             ; {} Yes, check the backpack
4338: 2A A5 44        LD      HL,($44A5)          ; {code.nounPointer} Noun word pointer
433B: 2B              DEC     HL                  ; Back up the word pointer
433C: 3A DC 4F        LD      A,($4FDC)           ; {ram.CurrentRoom} Is ...
433F: 5F              LD      E,A                 ; ... this ...
4340: 7E              LD      A,(HL)              ; ... object ...
4341: C5              PUSH    BC                  ; ... in the ...
4342: CD 4B 42        CALL    $424B               ; {code.GetObjectInfo} ... current room?
4345: C1              POP     BC                  ; Restore BC
4346: CA 81 43        JP      Z,$4381             ; {} Yes, go use it
4349: 2A A5 44        LD      HL,($44A5)          ; {code.nounPointer} Restore word data pointer
434C: 05              DEC     B                   ; All objects of this name tried?
434D: C2 21 43        JP      NZ,$4321            ; {} No ... keep looking for matching object
;
; Object not found (either not in pack or not in room depending on verb requirements)
4350: 3A 1A 46        LD      A,($461A)           ; {code.grammar} Grammar type
4353: FE 40           CP      $40                 ; 01_000_000 means noun-in-pack
4355: C2 5E 43        JP      NZ,$435E            ; {} Error ... can't find noun in room
4358: 21 35 46        LD      HL,$4635            ; {+code.MsgNotCarrying} "YOU_AREN'T_CARRYING_IT.[CR]"
435B: C3 77 43        JP      $4377               ; {} Print error and back to try again
435E: 21 24 46        LD      HL,$4624            ; {+code.MsgISeeNo} "I_SEE_NO_"
4361: CD CB 44        CALL    $44CB               ; {code.PrintPlain} First fragment
4364: 3E 01           LD      A,$01               ; Replace '?' with ...
4366: 32 98 46        LD      ($4698),A           ; {code.unknownNounPunct} ... no-CR terminator.
4369: 21 70 46        LD      HL,$4670            ; {+code.unknownNoun} Buffer for unknown word
436C: CD CB 44        CALL    $44CB               ; {code.PrintPlain} Print unknown word
436F: 3E 3F           LD      A,$3F               ; Restore the ...
4371: 32 98 46        LD      ($4698),A           ; {code.unknownNounPunct} ... question mark character
4374: 21 2E 46        LD      HL,$462E            ; {+code.MsgHere} "_HERE."
4377: CD CB 44        CALL    $44CB               ; {code.PrintPlain} Print the last fragment of error
437A: 97              SUB     A                   ; Clear ...
437B: 32 18 46        LD      ($4618),A           ; {code.noun} ... the unknown noun
437E: C3 CA 42        JP      $42CA               ; {code.ParseUserInput} Back to try again
;
; Found object
4381: 2A A5 44        LD      HL,($44A5)          ; {code.nounPointer}
4384: 2B              DEC     HL                  ; Back up to start
4385: 7E              LD      A,(HL)              ; Get the object number
4386: 32 18 46        LD      ($4618),A           ; {code.noun} Hold the noun
4389: 3A 19 46        LD      A,($4619)           ; {code.verb} Get the verb
438C: A7              AND     A                   ; Noun and verb?
438D: C0              RET     NZ                  ; Yes, done
438E: 21 4D 46        LD      HL,$464D            ; {+code.MsgWhatDoWith} "WHAT_DO_YOU_WANT_ME_TO_DO_WITH_THE_"+noun+"?"
4391: CD CB 44        CALL    $44CB               ; {code.PrintPlain} Print first fragment
4394: 3E 01           LD      A,$01               ; Flag that we ...
4396: 32 9C 43        LD      ($439C),A           ; {code.isLoneObject} ... are prompting for a verb only
4399: C3 CA 42        JP      $42CA               ; {code.ParseUserInput} Back to get user input

isLoneObject:
439C: 00 ; 1 if there was a lone object given last input
```

# Tokenize the input

Parse the input into words.

```code
ParseInputString:
439D: 21 F7 45        LD      HL,$45F7            ; {+code.InputBuffer} Start of user input buffer
43A0: 97              SUB     A                   ; Clear the ...
43A1: 32 A4 44        LD      ($44A4),A           ; {code.bufferHasSomething} ... buffer-has-something flag
43A4: 32 1A 46        LD      ($461A),A           ; {code.grammar} ... and the grammar
;
43A7: 11 22 56        LD      DE,$5622            ; {+code.wordTable} Pointer to all the words we know
43AA: EB              EX      DE,HL               ; Now HL=words we know, DE=where we are in the input
43AB: 22 16 47        LD      ($4716),HL          ; {code.currentParsePtr} Hold our current spot in the word table
43AE: EB              EX      DE,HL               ; Now HL=where we are in input, DE=where we are in words
;
; Skip over blank spaces before next word
43AF: 7E              LD      A,(HL)              ; Ignore ...
43B0: FE 20           CP      $20                 ; ... all ...
43B2: C2 B9 43        JP      NZ,$43B9            ; {} ... leading ...
43B5: 23              INC     HL                  ; ... blank ...
43B6: C3 AF 43        JP      $43AF               ; {} ... spaces
43B9: 22 18 47        LD      ($4718),HL          ; {code.startOfWord} start of this word
43BC: A7              AND     A                   ; Nothing but spaces?
43BD: CA 57 44        JP      Z,$4457             ; {} Yes, we are done parsing
;
43C0: 3E 01           LD      A,$01               ; There is SOMETHING ...
43C2: 32 A4 44        LD      ($44A4),A           ; {code.bufferHasSomething} ... in the buffer
43C5: E5              PUSH    HL                  ; Hold the pointer
43C6: 1A              LD      A,(DE)              ; First byte of word table
43C7: A7              AND     A                   ; Reached the end of the table?
43C8: CA 62 44        JP      Z,$4462             ; {} Done tokenizing ... now have a look at the words
43CB: 32 1E 47        LD      ($471E),A           ; {code.wordBeingTested} Hold 1st byte of word being tested
43CE: E6 07           AND     $07                 ; Number of bytes ...
43D0: 4F              LD      C,A                 ; ... in ...
43D1: 32 1A 47        LD      ($471A),A           ; {code.charsInWord} ... current word text
43D4: 3A 1E 47        LD      A,($471E)           ; {code.wordBeingTested} We'll need that info byte several times
43D7: E6 38           AND     $38                 ; Number ...
43D9: 0F              RRCA                        ; ... of ...
43DA: 0F              RRCA                        ; ... bytes ...
43DB: 0F              RRCA                        ; ... in ...
43DC: 47              LD      B,A                 ; word data
43DD: EB              EX      DE,HL               ; Save our current ...
43DE: 22 16 47        LD      ($4716),HL          ; {code.currentParsePtr} ... position in the input
43E1: EB              EX      DE,HL               ; Shuffle our pointers back
43E2: 13              INC     DE                  ; Get next from ...
43E3: 1A              LD      A,(DE)              ; ... input buffer
43E4: BE              CP      (HL)                ; Does it match the word we are testing?
43E5: C2 49 44        JP      NZ,$4449            ; {code.FindEndOfTestWord} No, try next word
43E8: 23              INC     HL                  ; Next in input
43E9: 13              INC     DE                  ; Next in word text
43EA: 0D              DEC     C                   ; All characters of word being tested?
43EB: C2 E3 43        JP      NZ,$43E3            ; {} No, keep testing
43EE: 3A 1A 47        LD      A,($471A)           ; {code.charsInWord} Number of characters in the test word
43F1: FE 06           CP      $06                 ; Six is the max size EXCEPT FOR "SCEPTER" WHICH IS 7 -- BUG?
43F3: CA 00 44        JP      Z,$4400             ; {code.FindEndOfInputWord} Six matched ... ignore the rest of the input
;
43F6: 7E              LD      A,(HL)              ; Not six ... is the next input ...
43F7: FE 20           CP      $20                 ; ... a space?
43F9: CA 0E 44        JP      Z,$440E             ; {} Yes ... we are ready for next word
43FC: A7              AND     A                   ; Maybe the end of the input buffer?
43FD: C2 4E 44        JP      NZ,$444E            ; {code.FindEndOfTestData} No ... not a match
;
FindEndOfInputWord:
4400: 7E              LD      A,(HL)              ; Next in buffer is ...
4401: FE 20           CP      $20                 ; ... a space?
4403: CA 0E 44        JP      Z,$440E             ; {} Yes, end of word success
4406: A7              AND     A                   ; End of input buffer?
4407: CA 0E 44        JP      Z,$440E             ; {} Yes, end of word success
440A: 23              INC     HL                  ; Next character in input
440B: C3 00 44        JP      $4400               ; {code.FindEndOfInputWord} Find end of word
;
440E: 3A 1E 47        LD      A,($471E)           ; {code.wordBeingTested}
4411: E6 C0           AND     $C0                 ; Is the word a noun? (anything else is a verb)
4413: CA 28 44        JP      Z,$4428             ; {} Yes ... record the noun
4416: 32 1A 46        LD      ($461A),A           ; {code.grammar} Hold the verb's grammar
4419: 1A              LD      A,(DE)              ; Get the verb number ...
441A: 32 19 46        LD      ($4619),A           ; {code.verb} ... from script (lots of words might map to same number)
441D: E5              PUSH    HL                  ; Hold input pointer
441E: 21 9A 46        LD      HL,$469A            ; {+code.unknownVerb} Storage for unknownVerb
4421: CD 80 44        CALL    $4480               ; {code.CopyWord} Copy input to the unknownVerb storage
4424: E1              POP     HL                  ; Restore pointer
4425: C3 41 44        JP      $4441               ; {} Skip spaces and next word
;
4428: 1A              LD      A,(DE)              ; Store the ...
4429: 32 18 46        LD      ($4618),A           ; {code.noun} ... noun number (several words might match)
442C: EB              EX      DE,HL               ; Get HL into position
442D: 22 A5 44        LD      ($44A5),HL          ; {code.nounPointer} Store pointer to noun
4430: EB              EX      DE,HL               ; Restore pointer positions
4431: 78              LD      A,B                 ; Number of bytes ...
4432: 32 A3 44        LD      ($44A3),A           ; {code.numBytesWordData} ... of data for this word
4435: 97              SUB     A                   ; Clear the ...
4436: 32 9C 43        LD      ($439C),A           ; {code.isLoneObject} ... isLoneObject flag (we have a verb)
4439: E5              PUSH    HL                  ; Hold
443A: 21 70 46        LD      HL,$4670            ; {+code.unknownNoun} Copy the ...
443D: CD 80 44        CALL    $4480               ; {code.CopyWord} ... input noun
4440: E1              POP     HL                  ; Restore
4441: 7E              LD      A,(HL)              ; From input
4442: FE 20           CP      $20                 ; Is it a space?
4444: D1              POP     DE                  ; Restore
4445: CA A7 43        JP      Z,$43A7             ; {} Yes ... decode the next word
4448: C9              RET                         ; Done
;
FindEndOfTestWord:
4449: 13              INC     DE                  ; Skip ...
444A: 0D              DEC     C                   ; ... all characters ...
444B: C2 49 44        JP      NZ,$4449            ; {code.FindEndOfTestWord} ... in test word
;
FindEndOfTestData:
444E: 13              INC     DE                  ; Next in word text data
444F: 05              DEC     B                   ; Reached the end of the test word?
4450: C2 4E 44        JP      NZ,$444E            ; {code.FindEndOfTestData} No, move to the end
;
4453: E1              POP     HL                  ; Restore pointer to input
4454: C3 AF 43        JP      $43AF               ; {} Skip blank spaces in input
;
4457: 3A A4 44        LD      A,($44A4)           ; {code.bufferHasSomething} Is the buffer ...
445A: A7              AND     A                   ; ... empty?
445B: C0              RET     NZ                  ; YES, we are done
;
445C: 3E 03           LD      A,$03               ; Stand alone ...
445E: 32 1A 46        LD      ($461A),A           ; {code.grammar} ... verb
4461: C9              RET                         ; Done
;
4462: E1              POP     HL                  ; Restore pointer to input
4463: 97              SUB     A                   ; Zero the ...
4464: 32 19 46        LD      ($4619),A           ; {code.verb} ... verb
4467: 32 18 46        LD      ($4618),A           ; {code.noun} And the noun
446A: 7E              LD      A,(HL)              ; Next input
446B: FE 20           CP      $20                 ; Is it a space?
446D: C2 74 44        JP      NZ,$4474            ; {code.SkipInputWord} No, go process it
4470: 23              INC     HL                  ; Skip ...
4471: C3 6A 44        JP      $446A               ; {} ... blank spaces
;
SkipInputWord:
4474: 7E              LD      A,(HL)              ; End of ...
4475: A7              AND     A                   ; ... user input?
4476: C8              RET     Z                   ; Yes, we are done
4477: FE 20           CP      $20                 ; Space?
4479: CA A7 43        JP      Z,$43A7             ; {} Yes, go lookup any word that follows
447C: 23              INC     HL                  ; Keep skipping ...
447D: C3 74 44        JP      $4474               ; {code.SkipInputWord} ... input word

CopyWord:
4480: EB              EX      DE,HL               ; Now DE=storage
4481: 2A 18 47        LD      HL,($4718)          ; {code.startOfWord}
4484: 06 28           LD      B,$28               ; 40 chars max in storage for word
4486: 7E              LD      A,(HL)              ; From input buffer
4487: A7              AND     A                   ; End of the buffer?
4488: CA 9A 44        JP      Z,$449A             ; {} Yes ... done
448B: FE 20           CP      $20                 ; Is it a space betwen words?
448D: CA 9A 44        JP      Z,$449A             ; {} Yes ... done
4490: 12              LD      (DE),A              ; Store input word char to storage
4491: 23              INC     HL                  ; Next input
4492: 13              INC     DE                  ; Next storage
4493: 05              DEC     B                   ; Count down remaining storage
4494: 78              LD      A,B                 ; Storage all ...
4495: FE 01           CP      $01                 ; ... full?
4497: C2 86 44        JP      NZ,$4486            ; {} No ... keep copying
449A: 3E 40           LD      A,$40               ; Fill ...
449C: 12              LD      (DE),A              ; ... remainder of ...
449D: 13              INC     DE                  ; ... storage ...
449E: 05              DEC     B                   ; ... with ...
449F: C2 9A 44        JP      NZ,$449A            ; {} ... the "@" character
44A2: C9              RET                         

numBytesWordData:
44A3: 00         

bufferHasSomething:
44A4: 00 ; 0 if the input buffer is empty or 1 if there is input

nounPointer:
44A5: 00 00               

; unused
44A7: 00 00
```

# Print Packed

```code
PrintPacked:
; Unpack a message (or multiple packed messages) and print.
; HL is pointer to message
44A9: 7E              LD      A,(HL)              ; Next byte of data
44AA: A7              AND     A                   ; Return if we are ...
44AB: C8              RET     Z                   ; ... at the end
;
44AC: 23              INC     HL                  ; Next in string
44AD: 11 F7 45        LD      DE,$45F7            ; {+code.InputBuffer} Destination buffer
44B0: CD 5F 47        CALL    $475F               ; {code.UnpackStringToScreen} Unpack the string
44B3: 7E              LD      A,(HL)              ; Character from string
44B4: A7              AND     A                   ; 0 means end with a carriage return?
44B5: CA E2 44        JP      Z,$44E2             ; {code.PrintCarriageReturn} Yes, print carriage return and out
44B8: FE 01           CP      $01                 ; 1 means end with nothing?
44BA: C8              RET     Z                   ; Yes, just return
44BB: 47              LD      B,A                 ; Print ...
44BC: E5              PUSH    HL                  ; ... the ...
44BD: CD 92 45        CALL    $4592               ; {code.PrintChar} ... character
44C0: E1              POP     HL                  ; Restore pointer to string
44C1: 7E              LD      A,(HL)              ; Character we just printed
44C2: FE 0A           CP      $0A                 ; Line feed means start a new unpack/print?
44C4: 23              INC     HL                  ; Point to next character
44C5: CA A9 44        JP      Z,$44A9             ; {code.PrintPacked} Yes, start a new unpack/print
44C8: C3 B3 44        JP      $44B3               ; {} No, continue with current unpacked string

PrintPlain:
; HL points to message terminated by
;  - 0 : add a CR on the end and return
;  - 1 : no CR on the end and return
; Return with B holding last character (if any) sent to ROM routine.
;
44CB: 7E              LD      A,(HL)              ; Next character
44CC: A7              AND     A                   ; 0 means end with a line feed?
44CD: CA E2 44        JP      Z,$44E2             ; {code.PrintCarriageReturn} Yes, print line feed and out
44D0: FE 01           CP      $01                 ; 1 means end with nothing?
44D2: C8              RET     Z                   ; Yes, just return
44D3: FE 40           CP      $40                 ; Character is 40 (ignore)?
44D5: CA DE 44        JP      Z,$44DE             ; {} Yes, just ingore the character
44D8: 47              LD      B,A                 ; Print ...
44D9: E5              PUSH    HL                  ; ... the ...
44DA: CD 92 45        CALL    $4592               ; {code.PrintChar} ... character
44DD: E1              POP     HL                  ; Restore pointer to string
44DE: 23              INC     HL                  ; Next character in string
44DF: C3 CB 44        JP      $44CB               ; {code.PrintPlain}
;
PrintCarriageReturn:
44E2: 06 0D           LD      B,$0D               ; Print ...
44E4: 78              LD      A,B                 ; ... carriage ...
44E5: CD 92 45        CALL    $4592               ; {code.PrintChar} ... return
44E8: C9              RET                         
```

# Wait for key

```code
WaitForKey:
44E9: D5              PUSH    DE                  ; ROM routine mangles this
44EA: 3A 11 47        LD      A,($4711)           ; {code.keyWaitCounter} Bump the ...
44ED: 3C              INC     A                   ; ... counter used for ...
44EE: 32 11 47        LD      ($4711),A           ; {code.keyWaitCounter} ... random numbers
44F1: CD FA 44        CALL    $44FA               ; {} Call the ROM routine to scan the keyboard
44F4: A7              AND     A                   ; Any key typed?
44F5: CA EA 44        JP      Z,$44EA             ; {} No, keep waiting
44F8: D1              POP     DE                  ; Restore our DE
44F9: C9              RET                         ; Return key in A

; The LEVEL 2 ROM has a ROM function to read the keyboard (002B). The LEVEL 1
; does not. This code simulates that ROM call. I wonder if the LEVEL 2 code
; was written first then back-ported to LEVEL 1. The fact that this routine
; appears after the above caller seems to suggest that.

44FA: E5              PUSH    HL                  
44FB: D5              PUSH    DE                  
44FC: C5              PUSH    BC                  
44FD: CD 04 45        CALL    $4504               ; {}
4500: C1              POP     BC                  
4501: D1              POP     DE                  
4502: E1              POP     HL                  
4503: C9              RET                         

4504: 21 8B 45        LD      HL,$458B            
4507: 01 01 38        LD      BC,$3801            
450A: 16 00           LD      D,$00               
450C: 0A              LD      A,(BC)              
450D: 5F              LD      E,A                 
450E: AE              XOR     (HL)                
450F: 73              LD      (HL),E              
4510: A3              AND     E                   
4511: C2 1D 45        JP      NZ,$451D            ; {}
4514: 14              INC     D                   
4515: 2C              INC     L                   
4516: CB 01           RLC     C                   
4518: F2 0C 45        JP      P,$450C             ; {}
451B: 97              SUB     A                   
451C: C9              RET                         

451D: 5F              LD      E,A                 
451E: C5              PUSH    BC                  
451F: 01 DC 05        LD      BC,$05DC            
4522: CD 7C 45        CALL    $457C               ; {}
4525: C1              POP     BC                  
4526: 0A              LD      A,(BC)              
4527: A3              AND     E                   
4528: C8              RET     Z                   

4529: 7A              LD      A,D                 
452A: 07              RLCA                        
452B: 07              RLCA                        
452C: 07              RLCA                        
452D: 57              LD      D,A                 
452E: 0E 01           LD      C,$01               
4530: 79              LD      A,C                 
4531: A3              AND     E                   
4532: C2 3B 45        JP      NZ,$453B            ; {}
4535: 14              INC     D                   
4536: CB 01           RLC     C                   
4538: C3 30 45        JP      $4530               ; {}
453B: 3A 80 38        LD      A,($3880)           
453E: 47              LD      B,A                 
453F: 7A              LD      A,D                 
4540: C6 40           ADD     $40                 
4542: FE 60           CP      $60                 
4544: D2 51 45        JP      NC,$4551            ; {}
4547: CB 08           RRC     B                   
4549: D2 71 45        JP      NC,$4571            ; {}
454C: C6 20           ADD     $20                 
454E: C3 71 45        JP      $4571               ; {}
4551: D6 70           SUB     $70                 
4553: D2 69 45        JP      NC,$4569            ; {}
4556: C6 40           ADD     $40                 
4558: FE 3C           CP      $3C                 
455A: DA 5F 45        JP      C,$455F             ; {}
455D: EE 10           XOR     $10                 
455F: CB 08           RRC     B                   
4561: D2 71 45        JP      NC,$4571            ; {}
4564: EE 10           XOR     $10                 
4566: C3 71 45        JP      $4571               ; {}
4569: 21 83 45        LD      HL,$4583            
456C: 4F              LD      C,A                 
456D: 06 00           LD      B,$00               
456F: 09              ADD     HL,BC               
4570: 7E              LD      A,(HL)              
4571: 57              LD      D,A                 
4572: 01 AC 0D        LD      BC,$0DAC            
4575: CD 7C 45        CALL    $457C               ; {}
4578: 7A              LD      A,D                 
4579: FE 01           CP      $01                 
457B: C9              RET                         

457C: 0B              DEC     BC                  
457D: 78              LD      A,B                 
457E: B1              OR      C                   
457F: C2 7C 45        JP      NZ,$457C            ; {}
4582: C9              RET                         

4583: 0D 1F 01 5B 0A 08 09 20 
458B: 00 00 00 00 00 00 00                  
```

# Print Char

```code
PrintChar:
4592: D5              PUSH    DE                  ; ROM routine mangles this
4593: CD 10 00        CALL    $0010               ; Send character A to the screen
4596: D1              POP     DE                  ; Restore our DE
4597: C9              RET                         
```

# Prompt And Read Line

```code
PromptAndReadLine:
4598: 06 3A           LD      B,$3A               ; Colon ":"
459A: 78              LD      A,B                 ; User starts typing after ...
459B: CD 92 45        CALL    $4592               ; {code.PrintChar} ... the colon
459E: 21 F7 45        LD      HL,$45F7            ; {+code.InputBuffer} Start of the input buffer
45A1: 0E 00           LD      C,$00               ; Input character count (0 to start)
;
45A3: E5              PUSH    HL                  ; Hold ...
45A4: C5              PUSH    BC                  ; ... all ...
45A5: D5              PUSH    DE                  ; ... our registers
45A6: CD E9 44        CALL    $44E9               ; {code.WaitForKey}
45A9: D1              POP     DE                  ; Restore ...
45AA: C1              POP     BC                  ; ... all ...
45AB: E1              POP     HL                  ; ... our registers
45AC: 47              LD      B,A                 ; Key from the user
45AD: FE 08           CP      $08                 ; Backspace?
45AF: CA D4 45        JP      Z,$45D4             ; {code.BackSpace} Yes, handle erasing a character
45B2: 77              LD      (HL),A              ; Store the key in the bufer
45B3: CD 92 45        CALL    $4592               ; {code.PrintChar} Echo the key to the screen
45B6: FE 0D           CP      $0D                 ; Was it an ENTER?
45B8: CA F4 45        JP      Z,$45F4             ; {code.InputDone} Yes, we are done
45BB: 0C              INC     C                   ; Increment the character count
45BC: 23              INC     HL                  ; Next in buffer
45BD: 11 17 46        LD      DE,$4617            ; {+code.OnePastInput} One past the end of the input buffer
45C0: 7C              LD      A,H                 ; Overflowed the ...
45C1: BA              CP      D                   ; ... buffer?
45C2: DA A3 45        JP      C,$45A3             ; {} No, keep taking keys
45C5: 7D              LD      A,L                 ; Overflowed the ...
45C6: BB              CP      E                   ; ... buffer?
45C7: DA A3 45        JP      C,$45A3             ; {} No, keep taking keys
45CA: 06 08           LD      B,$08               ; Print ...
45CC: 78              LD      A,B                 ; ... backspace to ...
45CD: CD 92 45        CALL    $4592               ; {code.PrintChar} ... ignore input
45D0: 2B              DEC     HL                  ; Remove the input from the end of the buffer
45D1: C3 A3 45        JP      $45A3               ; {} Back for more input

BackSpace:
45D4: 2B              DEC     HL                  ; Back up the buffer pointer
45D5: 3E 45           LD      A,$45               ; Underflowed the ...
45D7: BC              CP      H                   ; ... buffer?
45D8: DA E1 45        JP      C,$45E1             ; {} No ... keep it
45DB: 7D              LD      A,L                 ; Underflowed the ...
45DC: FE F7           CP      $F7                 ; ... buffer?
45DE: DA 9E 45        JP      C,$459E             ; {} Yes ... set to start of buffer
45E1: 3E 08           LD      A,$08               ; Remove the character ...
45E3: 47              LD      B,A                 ; ... from the ...
;
; In the Level 2 ROM, this is where we print the backspace. It is a little different
; here, but the first two instructions of that remain above -- needlessly.
;
; Level 1 ROM code must maintain its own cursor. We use the minus "-", and we write
; it to the screen memory.
;
45E4: E5              PUSH    HL                  ; Hold AL
45E5: 2A 68 40        LD      HL,($4068)          ; ROM's screen cursor
45E8: 36 20           LD      (HL),$20            ; Replace last typed with a space
45EA: 2B              DEC     HL                  ; Back up the ...
45EB: 22 68 40        LD      ($4068),HL          ; ... screen pointer
45EE: 36 5F           LD      (HL),$5F            ; Put a 5F cursor on the end
45F0: E1              POP     HL                  ; Restore HL
45F1: C3 A3 45        JP      $45A3               ; {} Back for more input

InputDone:
45F4: 36 00           LD      (HL),$00            ; Put the null terminator on the end of the input
45F6: C9              RET                         
```

# Input Buffer

```code
; 40 bytes of memory for input
InputBuffer:
; UNINITIALIZED MEMORY
45F7: 20 20 43 41 4C 4C 20 31 46 38 48 0D                 ; "  CALL 1F8H"      
4603: 11 30 30 30 30 20 20 4A 4D 50 20 52 43 4F 4E 54 0D  ; "0000  JMP RCONT"
4614: 08 30 30                                            ; "00" ...
;
; This is from the "Code.md" file at the end of "LoadTape"
; --  "----  CALL 1F8H"  0D  ; Turn cassette off
; 11  "0000  JMP RCONT"  0D  ;
; 08  "00----"           --  ; Must have been a blank like 

OnePastInput: ; Really UNUSED, but having this makes a label reference above
4617: 00 ; Never written to

noun:
4618: 00 

verb:
4619: 00 

grammar:
461A: 00 

nextErrorString:
461B: 00    ; Which error string do we show next? 0, 1, 2, or 3

ErrorString1:
461C: C2 46 ; " WHAT?"
ErrorString2:
461E: C9 46 ; "I DON'T KNOW THAT WORD."
ErrorString3:
4620: E1 46 ; "I DON'T UNDERSTAND."
ErrorString4:
4622: F5 46 ; "I DON'T KNOW WHAT YOUR MEAN."

; I_SEE_NO_
MsgISeeNo:
4624: 49 20 53 45 45 20 4E 4F 20 01 

; _HERE.[CR]
MsgHere:
462E: 20 48 45 52 45 2E 00

; YOU_AREN'T_CARRYING_IT.
MsgNotCarrying:
4635: 59 4F 55 20 41 52 45 4E 27 54 20 43 41 52 52 59 49 4E 47 20 49 54 2E 00 

; WHAT_DO_YOU_WANT_ME_TO_DO_WITH_THE_
MsgWhatDoWith:
464D: 57 48 41 54 20 44 4F 20 59 4F 55 20 57 41 4E 54 20 4D 45 20 54 4F 20 44 4F 20 57 49 54 48 20 54
466D: 48 45 20

; 40 byte buffer for unknown noun word
unknownNoun:
; UNINITIALIZED MEMORY
4670: 2C 41 0D                                                  ; ... ",A",0D
4673: 12 30 30 30 30 20 20 4C 58 49 20 48 2C 52 41 4C 31 0D     ; 12,"0000  LXI H,RAL1",0D
4685: 14 30 30 30 30 20 43 4E 41 4C 4C 20 4D 4F 56 20 41 2C 4D  ; 14,"0000 CNALL MOV A,M",0D

unknownNounPunct:
; "?"
4698: 3F 00 ; The code changes this depending on the sentence

; 40 byte buffer for unknown verb
unknownVerb:
; UNINITIALIZED MEMORY
469A: 30 30 30 30 20 20 49 4E 58 20 48 0D            ; "0000  INX H",0D
46A6: 0D 30 30 30 30 20 20 41 4E 41 20 41 0D         ; 0D,"0000  ANA A",0D
46B3: 10 30 30 30 30 20 20 4A 5A 20 43 4E 41 4C 4C   ; 10,"0000  JZ CNALL"


; Putting the two holes together, it matches the Z80 starting at 55ED:
;
; --  "-----------,A"       0D  -->  55ED: 47        LD   B,A       ; To B
; 12  "0000  LXI H,RAL1"    0D  -->  55EE: 21 69 49  LD   HL,$4969  ; {+code.room_1} start of room scripts
; 14  "0000 CNALL MOV A,M"  --  -->  55F1: 7E        LD   A,(HL)    ; Get the verb number
; --  "0000  INX H"         0D  -->  55F2: 23        INC  HL        ; Next byte
; 0D  "0000  ANA A"         0D  -->  55F3: A7        AND  A         ; End of the script for this room?
; 10  "0000  JZ CNALL"      0D  -->  55F4: CA F1 55  JP   Z,$55F1   ; {code.CNALL} Yes ... ignore the ...

ErrorString1:
;" WHAT?"
46C2: 20 57 48 41 54 3F 00 

ErrorString2:
; "I DON'T KNOW THAT WORD."
46C9: 49 20 44 4F 4E 27 54 20 4B 4E 4F 57 20 54 48 41 54 20 57 4F 52 44 2E 00

ErrorString3:
; "I DON'T UNDERSTAND."
46E1: 49 20 44 4F 4E 27 54 20 55 4E 44 45 52 53 54 41 4E 44 2E 00

ErrorString4:
; "I DON'T KNOW WHAT YOU MEAN."
46F5: 49 20 44 4F 4E 27 54 20 4B 4E 4F 57 20 57 48 41 54 20 59 4F 55 20 4D 45 41 4E 2E 00

keyWaitCounter:
4711: 00 ; Entropy for random numbers

; unused
4712: 00 00 00 00 

currentParsePtr:
4716: 00 00     

startOfWord:
4718: 00 00 ; Input buffer start of word we are tokenizing

charsInWord:
471A: 00 ; Number of characters in the test word while tokenizing

; unused
471B: 00 00 00 

wordBeingTested:
471E: 00

; "WELCOME TO PYRAMID!!"
WelcomeMsg:
471F: 57 45 4C 43 4F 4D 45 20 54 4F 20 50 59 52 41 4D 49 44 21 21 00

; The stack pointer is initialized to 475C. The Z80 SP decrements-before-store.
; Thus stack is 40 bytes of uninitialized memory:
; UNINITIALIZED MEMORY
4734: 4E 41 4C 32 0D                                                ; ... "NAL2"
4739: 0F 30 30 30 30 20 20 4D 56 49 20 41 2C 34 0D                  ; "0000 MVI A,4"
4748: 14 30 30 30 30 20 43 4E 41 4C 32 20 4D 4F 56 20 4D 2C 41 0D   ; "0000 CNAL2 MOV M,A"

; Continuing from the original source above:
;
; --  "---------NAL2"       0D  -->  5605: C2 0A 56  JP  NZ,$560A  ; {code.CNAL2} Are we in 1, ...
; 0F  "0000  MVI A,4"       0D  -->  5608: 3E 04     LD  A,$04     ; We rolled around. 0 becomes 4.
; 14  "0000 CNAL2 MOV M,A"  0D  -->  560A: 77        LD  (HL),A    ; New verb number

TopOfStack:
; The Z80 stack decrements before write. The 40 bytes above are the uninitialized
; memory reserved for the statck.
475C: 00 

EmptyString:
475D: 00 00 ; For objects that have no descriptions
```

# Packed strings

By limiting a character to 40 possible values, we can pack three characters into 2 bytes:

40 x 40 x 40 = 64,000 (just shy of 65,536)

The 40 characters from CharTable: ?!2_"'<>/03ABCDEFGHIJKLMNOPQRSTUVWXYZ-,.

The first byte of a packed string is the number of words to unpack. Other printable characters
may be listed after that with a 0 terminating the string.

For instance, PS_02:

```
; YOU_ARE_IN_THE_DESERT.[CR]
07 C7 DE 94 14 4B 5E 96 96 DB 72 F5 59 3E 62 2E 00
```

There are 7 words to unpack (14 bytes) followed by the "2E" period and the null terminator 0.

Each double word is listed LSB first. The first word to unpack is 0xDEC7.

```
val = 0x1494
c1 = val % 40  # 31 -> 'U'
val //= 40
c2 = val % 40  # 25 -> 'O'
val //= 40
c3 = val % 40  # 35 -> 'Y'
```

Which gives us 'YOU' (reversed order).

Next is 1419:

```
c1 = 28  -> 'R'
c2 = 11  -> 'A'
c3 = 3   -> '_' (really the space character)
```

Bringing us to "YOU_AR", and so on.

```code
UnpackStringToScreen:
475F: 32 21 48        LD      ($4821),A           ; {code.unpackNumWords} Number of words to unpack
4762: 3E 01           LD      A,$01               ; We are unpacking to ...
4764: 32 24 48        LD      ($4824),A           ; {code.unpackFlagToScreen} ... the screen
4767: C3 71 47        JP      $4771               ; {} Do the unpack
;
UnpackStringToBuffer:  ; Never used
476A: 32 21 48        LD      ($4821),A           ; {code.unpackNumWords} Number of words to unpack
476D: 97              SUB     A                   ; We are unpacking to ...
476E: 32 24 48        LD      ($4824),A           ; {code.unpackFlagToScreen} ... the buffer
;
; HL points to data to unpack
; DE points to unpack buffer (just 3 bytes if going to screen)
4771: E5              PUSH    HL                  ; Hold the pointer to the words
;
4772: 06 03           LD      B,$03               ; Three characters to extract from word
4774: E1              POP     HL                  ; Get the ...
4775: 7E              LD      A,(HL)              ; ... MSB of the word
4776: 23              INC     HL                  ; Get the ...
4777: 4E              LD      C,(HL)              ; ... LSB of the word
4778: 23              INC     HL                  ; Update the pointer ...
4779: E5              PUSH    HL                  ; ... to the words
477A: 61              LD      H,C                 ; Data word ...
477B: 6F              LD      L,A                 ; ... to HL
477C: 13              INC     DE                  ; Skip to end ...
477D: 13              INC     DE                  ; ... we are storing in reverse
477E: EB              EX      DE,HL               ; Now HL=buffer and DE=data
477F: E5              PUSH    HL                  ; Hold pointer to the buffer
4780: C5              PUSH    BC                  ; Hold our count to 3
;
4781: 21 28 00        LD      HL,$0028            ; The value of ...
4784: 22 22 48        LD      ($4822),HL          ; {code.valueOfForty} ... 40 for division (repeated subtraction)
4787: 21 B7 47        LD      HL,$47B7            ; {+code.shiftCount} We stop after ...
478A: 36 11           LD      (HL),$11            ; ... 16 shifts (end + 1 = 17)
478C: 01 00 00        LD      BC,$0000            ; Value we are extracting
478F: C5              PUSH    BC                  ; Hold the value on the stack
4790: 7B              LD      A,E                 ; Shift ...
4791: 17              RLA                         ; ... DE ...
4792: 5F              LD      E,A                 ; ... left ...
4793: 7A              LD      A,D                 ; ... one ...
4794: 17              RLA                         ; ... bit ...
4795: 57              LD      D,A                 ; ... bit goes to CF
4796: 35              DEC     (HL)                ; All shifts done?
4797: E1              POP     HL                  ; Current extracted value from stack
4798: CA B8 47        JP      Z,$47B8             ; {} Yes, store the extracted character
479B: 3E 00           LD      A,$00               ; Left bit ...
479D: CE 00           ADC     $00                 ; ... to A
479F: 29              ADD     HL,HL               ; Value = value * 2
47A0: 44              LD      B,H                 ; MSB
47A1: 85              ADD     A,L                 ; 
47A2: 2A 22 48        LD      HL,($4822)          ; {code.valueOfForty}
47A5: 95              SUB     L                   ; 
47A6: 4F              LD      C,A                 ; 
47A7: 78              LD      A,B                 ; TODO figure out the exact math here
47A8: 9C              SBC     H                   ; 
47A9: 47              LD      B,A                 ; 
47AA: C5              PUSH    BC                  ; 
47AB: D2 B0 47        JP      NC,$47B0            ; {} Less than 40 ... skip adding
47AE: 09              ADD     HL,BC               ; Greater or equal, add to the extracted value
47AF: E3              EX      (SP),HL             ; New value back to stack
47B0: 21 B7 47        LD      HL,$47B7            ; {+code.shiftCount}
47B3: 3F              CCF                         ; Clear carry for next math
47B4: C3 90 47        JP      $4790               ; {} Do all bits

shiftCount:
47B7: 00  ; Count of shifts during the unpack algorithm

47B8: 01 F9 47        LD      BC,$47F9            ; {+code.CharTable} Offset to character table
47BB: 09              ADD     HL,BC               ; Offset to the character in the table
47BC: 7E              LD      A,(HL)              ; Get the character
47BD: C1              POP     BC                  ; Restore the count in B
47BE: E1              POP     HL                  ; Restore the pointer to buffer
47BF: 77              LD      (HL),A              ; Store the character in the buffer
47C0: 2B              DEC     HL                  ; Working backwards in sets of 3
47C1: 05              DEC     B                   ; All 3 values extracted?
47C2: C2 7F 47        JP      NZ,$477F            ; {} No, go get them all
47C5: 3A 24 48        LD      A,($4824)           ; {code.unpackFlagToScreen} Unpacking to ...
47C8: A7              AND     A                   ; ... a buffer?
47C9: CA E1 47        JP      Z,$47E1             ; {} Yes, skip screen printing
;
47CC: E5              PUSH    HL                  ; Hold ...
47CD: C5              PUSH    BC                  ; ... our ...
47CE: D5              PUSH    DE                  ; ... progress ...
47CF: 1E 03           LD      E,$03               ; Three characters to print
47D1: 23              INC     HL                  ; Next to print
47D2: 46              LD      B,(HL)              ; Get the character
47D3: E5              PUSH    HL                  ; Hold the buffer pointer
47D4: 78              LD      A,B                 ; To B
47D5: CD 92 45        CALL    $4592               ; {code.PrintChar} Print the unpacked character
47D8: E1              POP     HL                  ; Restore buffer pointer
47D9: 23              INC     HL                  ; Next in buffer
47DA: 1D              DEC     E                   ; All 3 printed?
47DB: C2 D2 47        JP      NZ,$47D2            ; {} No, print the 3 we just unpacked
47DE: D1              POP     DE                  ; Restore ...
47DF: C1              POP     BC                  ; ... our ...
47E0: E1              POP     HL                  ; ... progress
;
47E1: EB              EX      DE,HL               ; Now HL=data and DE=buffer
47E2: 13              INC     DE                  ; Will be next in buffer
47E3: 3A 24 48        LD      A,($4824)           ; {code.unpackFlagToScreen} Are we unpacking ...
47E6: A7              AND     A                   ; ... to the screen?
47E7: C2 ED 47        JP      NZ,$47ED            ; {} Yes ... reuse this 3-byte buffer
47EA: 13              INC     DE                  ; No, move to the ...
47EB: 13              INC     DE                  ; ... next 3-byte slot ...
47EC: 13              INC     DE                  ; ... in the buffer
47ED: 3A 21 48        LD      A,($4821)           ; {code.unpackNumWords} Count down ...
47F0: 3D              DEC     A                   ; ... number of ...
47F1: 32 21 48        LD      ($4821),A           ; {code.unpackNumWords} ... words
47F4: C2 72 47        JP      NZ,$4772            ; {} Go back for all the words
47F7: E1              POP     HL                  ; Point to the next character after the words in the string
47F8: C9              RET                         
```

# Character Table

```code
; Character compression table
CharTable:
47F9: 3F 21 32 20 22 27 3C 3E 2F 30 33                 ; ?!2_"'<>/03
4804: 41 42 43 44 45 46 47 48 49 4A 4B 4C 4D 4E 4F 50  ; ABCDEFGHIJKLMNOP
4814: 51 52 53 54 55 56 57 58 59 5A 2D 2C 2E           ; QRSTUVWXYZ-,.

unpackNumWords:
4821: 00 

valueOfForty:  ; Used in dividing by 40
4822: 00 00

unpackFlagToScreen:
4824: 00 ; Set to 1 to print the characters or 0 to buffer unpack to the buffer
```

# Room Table

Each entry is 4 bytes. The first word is the packed room description.
The second word is the room's command script.

```code
RoomTable:
;
; 81 rooms numbered starting at 1
;      Description   Script
4825: 2F 5B 69 49 ; PS_00 room_1
4829: 64 5B 7E 49 ; PS_01 room_2
482D: AB 5B 8F 49 ; PS_02 room_3
4831: AB 5B A0 49 ; PS_02 room_4
4835: AB 5B B1 49 ; PS_02 room_5
4839: AB 5B C2 49 ; PS_02 room_6
483D: BC 5B D3 49 ; PS_03 room_7
4841: 36 5C E4 49 ; PS_04 room_8
4845: 7C 5C F5 49 ; PS_05 room_9
4849: D1 5C 06 4A ; PS_06 room_10
484D: F4 5C 1B 4A ; PS_07 room_11
4851: 72 5D 24 4A ; PS_08 room_12
4855: E2 5D 3A 4A ; PS_09 room_13
4859: BD 5E 65 4A ; PS_0A room_14
485D: FF 5E 6E 4A ; PS_0B room_15
4861: 5C 5F AA 4A ; PS_0C room_16
4865: 90 5F E5 4A ; PS_0D room_17
4869: A9 5F EE 4A ; PS_0E room_18
486D: D9 5F 2D 4B ; PS_0F room_19
4871: 45 60 46 4B ; PS_10 room_20
4875: B3 60 5B 4B ; PS_11 room_21
4879: 00 61 64 4B ; PS_12 room_22
487D: 2C 61 75 4B ; PS_13 room_23
4881: 34 61 7E 4B ; PS_14 room_24
4885: 6C 61 8F 4B ; PS_15 room_25
4889: AC 61 A4 4B ; PS_16 room_26
488D: 04 62 B1 4B ; PS_17 room_27
4891: 1C 62 BE 4B ; PS_18 room_28
4895: 1C 62 D3 4B ; PS_18 room_29
4899: 1C 62 E4 4B ; PS_18 room_30
489D: 1C 62 FD 4B ; PS_18 room_31
48A1: 1C 62 06 4C ; PS_18 room_32
48A5: 1C 62 13 4C ; PS_18 room_33
48A9: 1C 62 24 4C ; PS_18 room_34
48AD: 1C 62 35 4C ; PS_18 room_35
48B1: 1C 62 4E 4C ; PS_18 room_36
48B5: 1C 62 5F 4C ; PS_18 room_37
48B9: 1C 62 68 4C ; PS_18 room_38
48BD: 1C 62 79 4C ; PS_18 room_39
48C1: 1C 62 86 4C ; PS_18 room_40
48C5: 1C 62 93 4C ; PS_18 room_41
48C9: 2C 61 A0 4C ; PS_13 room_42
48CD: 2C 61 A5 4C ; PS_13 room_43
48D1: 2C 61 AA 4C ; PS_13 room_44
48D5: 2C 61 AF 4C ; PS_13 room_45
48D9: 2C 61 B4 4C ; PS_13 room_46
48DD: 2C 61 B9 4C ; PS_13 room_47
48E1: 2C 61 BE 4C ; PS_13 room_48
48E5: 2C 61 C3 4C ; PS_13 room_49
48E9: 2C 61 C8 4C ; PS_13 room_50
48ED: 2C 61 CD 4C ; PS_13 room_51
48F1: 3E 62 DE 4C ; PS_19 room_52
48F5: 2C 61 F3 4C ; PS_13 room_53
48F9: 9D 62 F8 4C ; PS_1A room_54
48FD: FA 62 05 4D ; PS_1B room_55
4901: 2E 63 12 4D ; PS_1C room_56
4905: 73 63 30 4D ; PS_1D room_57
4909: CE 63 39 4D ; PS_1E room_58
490D: 5E 64 4E 4D ; PS_1F room_59
4911: F5 64 5B 4D ; PS_20 room_60
4915: 29 65 A3 4D ; PS_21 room_61
4919: D6 65 BE 4D ; PS_22 room_62
491D: 34 66 C7 4D ; PS_23 room_63
4921: 5B 66 D0 4D ; PS_24 room_64
4925: 7D 66 D9 4D ; PS_25 room_65
4929: DD 66 02 4E ; PS_26 room_66
492D: 00 00 00 00 ; unused 67
4931: 26 6B D8 4E ; PS_31 room_68
4935: 00 00 00 00 ; unused 69
4939: 05 6B CF 4E ; PS_30 room_70
493D: B0 6A C2 4E ; PS_2F room_71
4941: 79 67 0B 4E ; PS_27 room_72
4945: D6 67 14 4E ; PS_28 room_73
4949: 00 00 00 00 ; unused 74
494D: 00 00 00 00 ; unused 75
4951: 4A 68 23 4E ; PS_29 room_76
4955: 47 6A AB 4E ; PS_2E room_77
4959: 93 68 38 4E ; PS_2A room_78
495D: 75 69 45 4E ; PS_2B room_79
4961: 9F 69 4E 4E ; PS_2C room_80
4965: F1 69 5B 4E ; PS_2D room_81
```

# Room Scripts

```code
RoomScripts:

room_1:
; PS_00
; YOU_ARE_STANDING_BEFORE_THE_ENTRANCE_OF_A_PYRAMID.__AROUND_YOU__
; IS_A_DESERT.[CR]
;
4969: 01 03     ; N
496B: 01 02     ;     MoveToRoom(room_2)
496D: 02 03     ; E
496F: 01 03     ;     MoveToRoom(room_3)
4971: 03 03     ; S
4973: 01 04     ;     MoveToRoom(room_4)
4975: 04 03     ; W
4977: 01 05     ;     MoveToRoom(room_5)
4979: 0B 03     ; IN
497B: 01 02     ;     MoveToRoom(room_2)
497D: 00

room_2:
; PS_01
; YOU_ARE_IN_THE_ENTRANCE_TO_THE_PYRAMID.__A_HOLE_IN_THE_FLOOR____
; LEADS_TO_A_PASSAGE_BENEATH_THE_SURFACE.[CR]
;
497E: 03 03     ; S
4980: 01 01     ;    MoveToRoom(room_1)
4982: 0A 03     ; D
4984: 01 07     ;    MoveToRoom(room_7)
4986: 0C 03     ; OUT
4988: 01 01     ;    MoveToRoom(room_1)
498A: 12 03     ; PANEL
498C: 01 1A     ;    MoveToRoom(room_26)
498E: 00

room_3:
; PS_02
; YOU_ARE_IN_THE_DESERT.[CR]
;
498F: 01 03     ; N
4991: 01 06     ;    MoveToRoom(room_6)
4993: 02 03     ; E
4995: 01 03     ;    MoveToRoom(room_3)
4997: 03 03     ; S
4999: 01 04     ;    MoveToRoom(room_4)
499B: 04 03     ; W
499D: 01 01     ;    MoveToRoom(room_1)
499F: 00

room_4:
; PS_02
; YOU_ARE_IN_THE_DESERT.[CR]
;
49A0: 01 03     ; N
49A2: 01 01     ;    MoveToRoom(room_1)
49A4: 02 03     ; E
49A6: 01 03     ;    MoveToRoom(room_3)
49A8: 03 03     ; S
49AA: 01 04     ;    MoveToRoom(room_4)
49AC: 04 03     ; W
49AE: 01 05     ;    MoveToRoom(room_5)
49B0: 00

room_5:
; PS_02
; YOU_ARE_IN_THE_DESERT.[CR]
;
49B1: 01 03     ; N
49B3: 01 06     ;    MoveToRoom(room_6)
49B5: 02 03     ; E
49B7: 01 01     ;    MoveToRoom(room_1)
49B9: 03 03     ; S
49BB: 01 04     ;    MoveToRoom(room_4)
49BD: 04 03     ; W
49BF: 01 05     ;    MoveToRoom(room_5)
49C1: 00

room_6:
; PS_02
; YOU_ARE_IN_THE_DESERT.[CR]
;
49C2: 01 03     ; N
49C4: 01 06     ;    MoveToRoom(room_6)
49C6: 02 03     ; E
49C8: 01 03     ;    MoveToRoom(room_3)
49CA: 03 03     ; S
49CC: 01 01     ;    MoveToRoom(room_1)
49CE: 04 03     ; W
49D0: 01 05     ;    MoveToRoom(room_5)
49D2: 00

room_7:
; PS_03
; YOU_ARE_IN_A_SMALL_CHAMBER_BENEATH_A_HOLE_FROM_THE_SURFACE.__A__
; LOW_CRAWL_LEADS_INWARD_TO_THE_WEST.__HIEROGLYPHICS_ON_THE_WALL__
; TRANSLATE,_"CURSE_ALL_WHO_ENTER_THIS_SACRED_CRYPT."[CR]
;
49D3: 09 03     ; U
49D5: 01 02     ;    MoveToRoom(room_2)
49D7: 0C 03     ; OUT
49D9: 01 02     ;    MoveToRoom(room_2)
49DB: 04 03     ; W
49DD: 01 08     ;    MoveToRoom(room_8)
49DF: 0B 03     ; IN
49E1: 01 08     ;    MoveToRoom(room_8)
49E3: 00

room_8:
; PS_04
; YOU_ARE_CRAWLING_OVER_PEBBLES_IN_A_LOW_PASSAGE.__THERE_IS_A_DIM_
; LIGHT_AT_THE_EAST_END_OF_THE_PASSAGE.[CR]
;
49E4: 02 03     ; E
49E6: 01 07     ;    MoveToRoom(room_7)
49E8: 0C 03     ; OUT
49EA: 01 07     ;    MoveToRoom(room_7)
49EC: 04 03     ; W
49EE: 01 09     ;    MoveToRoom(room_9)
49F0: 0B 03     ; IN
49F2: 01 09     ;    MoveToRoom(room_9)
49F4: 00

room_9:
; PS_05
; YOU_ARE_IN_A_ROOM_FILLED_WITH_BROKEN_POTTERY_SHARDS_OF_ANCIENT__
; EGYPTIAN_CRAFTS.__AN_AWKWARD_CORRIDOR_LEADS_UPWARD_AND_WEST.[CR]
;
49F5: 02 03     ; E
49F7: 01 08     ;    MoveToRoom(room_8)
49F9: 0B 03     ; IN
49FB: 01 0A     ;    MoveToRoom(room_10)
49FD: 09 03     ; U
49FF: 01 0A     ;    MoveToRoom(room_10)
4A01: 04 03     ; W
4A03: 01 0A     ;    MoveToRoom(room_10)
4A05: 00

room_10:
; PS_06
; YOU_ARE_IN_AN_AWKWARD_SLOPING_EAST/WEST_CORRIDOR.[CR]
;
4A06: 0A 03     ; D
4A08: 01 09     ;    MoveToRoom(room_9)
4A0A: 02 03     ; E
4A0C: 01 09     ;    MoveToRoom(room_9)
4A0E: 0B 03     ; IN
4A10: 01 0B     ;    MoveToRoom(room_11)
4A12: 04 03     ; W
4A14: 01 0B     ;    MoveToRoom(room_11)
4A16: 09 03     ; U
4A18: 01 0B     ;    MoveToRoom(room_11)
4A1A: 00

room_11:
; PS_07
; YOU_ARE_IN_A_SPLENDID_CHAMBER_THIRTY_FEET_HIGH.__THE_WALLS_ARE__
; FROZEN_RIVERS_OF_ORANGE_STONE.__AN_AWKWARD_CORRIDOR_AND_A_GOOD__
; PASSAGE_EXIT_FROM_THE_EAST_AND_WEST_SIDES_OF_THE_CHAMBER.[CR]
;
4A1B: 02 03     ; E
4A1D: 01 0A     ;    MoveToRoom(room_10)
4A1F: 04 03     ; W
4A21: 01 0C     ;    MoveToRoom(room_12)
4A23: 00

room_12:
; PS_08
; AT_YOUR_FEET_IS_A_SMALL_PIT_BREATHING_TRACES_OF_WHITE_MIST.__AN_
; EAST_PASSAGE_ENDS_HERE_EXCEPT_FOR_A_SMALL_CRACK_LEADING_ON._____
; ROUGH_STONE_STEPS_LEAD_DOWN_THE_PIT.[CR]
;
4A24: 02 03     ; E
4A26: 01 0B     ;    MoveToRoom(room_11)
4A28: 0A 0B     ; D
4A2A: 07 07     ;    StopIfPassElseContinue
4A2C: 02 25     ;        AssertObjectIsInPack(obj_GOLD)
4A2E: 04 C5 70  ;        Print(PS_6B:"YOU_ARE_AT_THE_BOTTOM_OF_THE_PIT_WITH_A_BROKEN_NECK.[CR]")
4A31: 05        ;        PrintScoreAndStop
4A32: 01 0D     ;    MoveToRoom(room_13)
4A34: 04 04     ; W
4A36: 04 EA 70  ;    Print(PS_6C:"THE_CRACK_IS_FAR_TOO_SMALL_FOR_YOU_TO_FOLLOW.[CR]")
4A39: 00

room_13:
; PS_09
; YOU_ARE_AT_ONE_END_OF_A_VAST_HALL_STRETCHING_FORWARD_OUT_OF_____
; SIGHT_TO_THE_WEST.__THERE_ARE_OPENINGS_TO_EITHER_SIDE.__NEARBY,_
; A_WIDE_STONE_STAIRCASE_LEADS_DOWNWARD.__THE_HALL_IS_VERY_MUSTY__
; AND_A_COLD_WIND_BLOWS_UP_THE_STAIRCASE.__THERE_IS_A_PASSAGE_AT__
; THE_TOP_OF_A_DOME_BEHIND_YOU.__ROUGH_STONE_STEPS_LEAD_UP_THE____
; DOME.[CR]
;
4A3A: 03 03     ; S
4A3C: 01 0E     ;    MoveToRoom(room_14)
4A3E: 04 03     ; W
4A40: 01 0F     ;    MoveToRoom(room_15)
4A42: 0A 03     ; D
4A44: 01 10     ;    MoveToRoom(room_16)
4A46: 01 03     ; N
4A48: 01 10     ;    MoveToRoom(room_16)
4A4A: 09 0A     ; U
4A4C: 07 06     ;    StopIfPassElseContinue
4A4E: 02 25     ;        AssertObjectIsInPack(obj_GOLD)
4A50: 04 0A 71  ;        Print(PS_6D:"THE_DOME_IS_UNCLIMBABLE.[CR]")
4A53: 01 0C     ;    MoveToRoom(room_12)
4A55: 02 0A     ; E
4A57: 07 06     ;    StopIfPassElseContinue
4A59: 02 25     ;        AssertObjectIsInPack(obj_GOLD)
4A5B: 04 0A 71  ;        Print(PS_6D:"THE_DOME_IS_UNCLIMBABLE.[CR]")
4A5E: 01 0C     ;    MoveToRoom(room_12)
4A60: 20 03     ; ??20??
4A62: 01 1A     ;    MoveToRoom(room_26)
4A64: 00

room_14:
; PS_0A
; THIS_IS_A_LOW_ROOM_WITH_A_HIEROGLYPH_ON_THE_WALL.__IT_TRANSLATES
; "YOU_WON'T_GET_IT_UP_THE_STEPS".[CR]
;
4A65: 0C 03     ; OUT
4A67: 01 0D     ;    MoveToRoom(room_13)
4A69: 01 03     ; N
4A6B: 01 0D     ;    MoveToRoom(room_13)
4A6D: 00

room_15:
; PS_0B
; YOU_ARE_ON_THE_EAST_BANK_OF_A_BOTTOMLESS_PIT_STRETCHING_ACROSS__
; THE_HALL.__THE_MIST_IS_QUITE_THICK_HERE,_AND_THE_PIT_IS_TOO_WIDE
; TO_JUMP.[CR]
;
4A6E: 02 03     ; E
4A70: 01 0D     ;    MoveToRoom(room_13)
4A72: 10 0C     ; JUMP
4A74: 07 06     ;    StopIfPassElseContinue
4A76: 03 01     ;        AssertObjectIsInCurrentRoomOrPack(obj_bridge_15)
4A78: 04 1C 71  ;        Print(PS_6E:"I_RESPECTFULLY_SUGGEST_YOU_GO_ACROSS_THE_BRIDGE_INSTEAD_OF______
;                                     JUMPING.[CR]")
4A7B: 04 4E 71  ;    Print(PS_6F:"YOU_DIDN'T_MAKE_IT.[CR]")
4A7E: 05        ;    PrintScoreAndStop
4A7F: 04 0A     ; W
4A81: 07 05     ;    StopIfPassElseContinue
4A83: 03 01     ;        AssertObjectIsInCurrentRoomOrPack(obj_bridge_15)
4A85: 01 12     ;        MoveToRoom(room_18)
4A87: 04 5D 71  ;    Print(PS_70:"THERE_IS_NO_WAY_ACROSS_THE_BOTTOMLESS_PIT.[CR]")
4A8A: 0D 05     ; CROSS
4A8C: 03 01     ;    AssertObjectIsInCurrentRoomOrPack(obj_bridge_15)
4A8E: 01 12     ;    MoveToRoom(room_18)
4A90: 23 18     ; WAVE
4A92: 11 11     ;    AssertObjectMatchesUserInput(obj_SCEPTER)
4A94: 07 0C     ;    StopIfPassElseContinue
4A96: 03 01     ;        AssertObjectIsInCurrentRoomOrPack(obj_bridge_15)
4A98: 15 01 00  ;        MoveObjectToRoom(obj_bridge_15, room_0)
4A9B: 15 02 00  ;        MoveObjectToRoom(obj_bridge_18, room_0)
4A9E: 04 32 7B  ;        Print(PS_AE:"THE_STONE_BRIDGE_HAS_RETRACTED![CR]")
4AA1: 18 01     ;    MoveObjectToCurrentRoom(obj_bridge_15)
4AA3: 15 02 12  ;    MoveObjectToRoom(obj_bridge_18, room_18)
4AA6: 04 49 7B  ;    Print(PS_AF:"A_STONE_BRIDGE_NOW_SPANS_THE_BOTTOMLESS_PIT.[CR]")
4AA9: 00

room_16:
; PS_0C
; YOU_ARE_IN_THE_PHARAOH'S_CHAMBER,_WITH_PASSAGES_OFF_IN_ALL______
; DIRECTIONS.[CR]
;
4AAA: 09 03     ; U
4AAC: 01 0D     ;    MoveToRoom(room_13)
4AAE: 02 03     ; E
4AB0: 01 0D     ;    MoveToRoom(room_13)
4AB2: 03 0A     ; S
4AB4: 07 06     ;    StopIfPassElseContinue
4AB6: 03 0B     ;        AssertObjectIsInCurrentRoomOrPack(obj_SERPENT)
4AB8: 04 7B 71  ;        Print(PS_71:"YOU_CAN'T_GET_BY_THE_SERPENT.[CR]")
4ABB: 01 11     ;    MoveToRoom(room_17)
4ABD: 01 0A     ; N
4ABF: 07 06     ;    StopIfPassElseContinue
4AC1: 03 0B     ;        AssertObjectIsInCurrentRoomOrPack(obj_SERPENT)
4AC3: 04 7B 71  ;        Print(PS_71:"YOU_CAN'T_GET_BY_THE_SERPENT.[CR]")
4AC6: 01 19     ;    MoveToRoom(room_25)
4AC8: 04 0A     ; W
4ACA: 07 06     ;    StopIfPassElseContinue
4ACC: 03 0B     ;        AssertObjectIsInCurrentRoomOrPack(obj_SERPENT)
4ACE: 04 7B 71  ;        Print(PS_71:"YOU_CAN'T_GET_BY_THE_SERPENT.[CR]")
4AD1: 01 18     ;    MoveToRoom(room_24)
4AD3: 26 10     ; THROW
4AD5: 11 14     ;    AssertObjectMatchesUserInput(obj_BIRD_boxed)
4AD7: 03 0B     ;    AssertObjectIsInCurrentRoomOrPack(obj_SERPENT)
4AD9: 15 0B 00  ;    MoveObjectToRoom(obj_SERPENT, room_0)
4ADC: 18 13     ;    MoveObjectToCurrentRoom(obj_BIRD)
4ADE: 15 14 00  ;    MoveObjectToRoom(obj_BIRD_boxed, room_0)
4AE1: 04 F5 7B  ;    Print(PS_B4:"THE_BIRD_STATUE_COMES_TO_LIFE_AND_ATTACKS_THE_SERPENT_AND_IN_AN_
;                                 ASTOUNDING_FLURRY,_DRIVES_THE_SERPENT_AWAY.__THE_BIRD_TURNS_BACK
;                                 INTO_A_STATUE.[CR]")
4AE4: 00

room_17:
; PS_0D
; YOU_ARE_IN_THE_SOUTH_SIDE_CHAMBER.[CR]
;
4AE5: 01 03     ; N
4AE7: 01 10     ;    MoveToRoom(room_16)
4AE9: 0C 03     ; OUT
4AEB: 01 10     ;    MoveToRoom(room_16)
4AED: 00

room_18:
; PS_0E
; YOU_ARE_ON_THE_WEST_SIDE_OF_THE_BOTTOMLESS_PIT_IN_THE_HALL_OF___
; GODS.[CR]
;
4AEE: 10 0C     ; JUMP
4AF0: 07 06     ;    StopIfPassElseContinue
4AF2: 03 02     ;        AssertObjectIsInCurrentRoomOrPack(obj_bridge_18)
4AF4: 04 1C 71  ;        Print(PS_6E:"I_RESPECTFULLY_SUGGEST_YOU_GO_ACROSS_THE_BRIDGE_INSTEAD_OF______
;                                     JUMPING.[CR]")
4AF7: 04 4E 71  ;    Print(PS_6F:"YOU_DIDN'T_MAKE_IT.[CR]")
4AFA: 05        ;    PrintScoreAndStop
4AFB: 02 0A     ; E
4AFD: 07 05     ;    StopIfPassElseContinue
4AFF: 03 02     ;        AssertObjectIsInCurrentRoomOrPack(obj_bridge_18)
4B01: 01 0F     ;        MoveToRoom(room_15)
4B03: 04 5D 71  ;    Print(PS_70:"THERE_IS_NO_WAY_ACROSS_THE_BOTTOMLESS_PIT.[CR]")
4B06: 01 06     ; N
4B08: 04 91 71  ;    Print(PS_72:"YOU_HAVE_CRAWLED_THROUGH_A_VERY_LOW_WIDE_PASSAGE_PARALLEL_TO_AND
;                                 NORTH_OF_THE_HALL_OF_GODS.[CR]")
4B0B: 01 13     ;    MoveToRoom(room_19)
4B0D: 0D 05     ; CROSS
4B0F: 03 02     ;    AssertObjectIsInCurrentRoomOrPack(obj_bridge_18)
4B11: 01 0F     ;    MoveToRoom(room_15)
4B13: 23 18     ; WAVE
4B15: 11 11     ;    AssertObjectMatchesUserInput(obj_SCEPTER)
4B17: 07 0C     ;    StopIfPassElseContinue
4B19: 03 02     ;        AssertObjectIsInCurrentRoomOrPack(obj_bridge_18)
4B1B: 15 02 00  ;        MoveObjectToRoom(obj_bridge_18, room_0)
4B1E: 15 01 00  ;        MoveObjectToRoom(obj_bridge_15, room_0)
4B21: 04 32 7B  ;        Print(PS_AE:"THE_STONE_BRIDGE_HAS_RETRACTED![CR]")
4B24: 18 02     ;    MoveObjectToCurrentRoom(obj_bridge_18)
4B26: 15 01 0F  ;    MoveObjectToRoom(obj_bridge_15, room_15)
4B29: 04 49 7B  ;    Print(PS_AF:"A_STONE_BRIDGE_NOW_SPANS_THE_BOTTOMLESS_PIT.[CR]")
4B2C: 00

room_19:
; PS_0F
; YOU_ARE_AT_THE_WEST_END_OF_THE_HALL_OF_GODS.___A_LOW_WIDE_PASS__
; CONTINUES_WEST_AND_ANOTHER_GOES_NORTH.__TO_THE_SOUTH_IS_A_LITTLE
; PASSAGE_SIX_FEET_OFF_THE_FLOOR.[CR]
;
4B2D: 03 03     ; S
4B2F: 01 1C     ;    MoveToRoom(room_28)
4B31: 09 03     ; U
4B33: 01 1C     ;    MoveToRoom(room_28)
4B35: 11 03     ; CLIMB
4B37: 01 1C     ;    MoveToRoom(room_28)
4B39: 02 03     ; E
4B3B: 01 12     ;    MoveToRoom(room_18)
4B3D: 01 03     ; N
4B3F: 01 12     ;    MoveToRoom(room_18)
4B41: 04 03     ; W
4B43: 01 14     ;    MoveToRoom(room_20)
4B45: 00

room_20:
; PS_10
; YOU_ARE_AT_EAST_END_OF_A_VERY_LONG_HALL_APPARENTLY_WITHOUT_SIDE_
; CHAMBERS.__TO_THE_EAST_A_LOW_WIDE_CRAWL_SLANTS_UP.__TO_THE_NORTH
; A_ROUND_TWO_FOOT_HOLE_SLANTS_DOWN.[CR]
;
4B46: 02 03     ; E
4B48: 01 13     ;    MoveToRoom(room_19)
4B4A: 09 03     ; U
4B4C: 01 13     ;    MoveToRoom(room_19)
4B4E: 04 03     ; W
4B50: 01 15     ;    MoveToRoom(room_21)
4B52: 01 03     ; N
4B54: 01 16     ;    MoveToRoom(room_22)
4B56: 0A 03     ; D
4B58: 01 16     ;    MoveToRoom(room_22)
4B5A: 00

room_21:
; PS_11
; YOU_ARE_AT_THE_WEST_END_OF_A_VERY_LONG_FEATURELESS_HALL.__THE___
; HALL_JOINS_; UP_WITH_A_NARROW_NORTH/SOUTH_PASSAGE.[CR]
;
4B5B: 02 03     ; E
4B5D: 01 14     ;    MoveToRoom(room_20)
4B5F: 01 03     ; N
4B61: 01 16     ;    MoveToRoom(room_22)
4B63: 00

room_22:
; PS_12
; YOU_ARE_AT_A_CROSSOVER_OF_A_HIGH_N/S_PASSAGE_AND_A_LOW_E/W_ONE.[CR]
;
4B64: 04 03     ; W
4B66: 01 14     ;    MoveToRoom(room_20)
4B68: 01 03     ; N
4B6A: 01 17     ;    MoveToRoom(room_23)
4B6C: 02 03     ; E
4B6E: 01 18     ;    MoveToRoom(room_24)
4B70: 03 03     ; S
4B72: 01 15     ;    MoveToRoom(room_21)
4B74: 00

room_23:
; PS_13
; DEAD_END.[CR]
;
4B75: 03 03     ; S
4B77: 01 16     ;    MoveToRoom(room_22)
4B79: 0C 03     ; OUT
4B7B: 01 16     ;    MoveToRoom(room_22)
4B7D: 00

room_24:
; PS_14
; YOU_ARE_IN_THE_WEST_THRONE_CHAMBER.__A_PASSAGE_CONTINUES_WEST___
; AND_UP_FROM_HERE.[CR]
;
4B7E: 02 03     ; E
4B80: 01 10     ;    MoveToRoom(room_16)
4B82: 0C 03     ; OUT
4B84: 01 10     ;    MoveToRoom(room_16)
4B86: 04 03     ; W
4B88: 01 16     ;    MoveToRoom(room_22)
4B8A: 09 03     ; U
4B8C: 01 16     ;    MoveToRoom(room_22)
4B8E: 00

room_25:
; PS_15
; YOU_ARE_IN_A_LOW_N/S_PASSAGE_AT_A_HOLE_IN_THE_FLOOR.__THE_HOLE__
; GOES_DOWN_TO_AN_E/W_PASSAGE.[CR]
;
4B8F: 0C 03     ; OUT
4B91: 01 10     ;    MoveToRoom(room_16)
4B93: 03 03     ; S
4B95: 01 10     ;    MoveToRoom(room_16)
4B97: 01 03     ; N
4B99: 01 1A     ;    MoveToRoom(room_26)
4B9B: 20 03     ; ??20??
4B9D: 01 1A     ;    MoveToRoom(room_26)
4B9F: 0A 03     ; D
4BA1: 01 36     ;    MoveToRoom(room_54)
4BA3: 00

room_26:
; PS_16
; YOU_ARE_IN_A_LARGE_ROOM,_WITH_A_PASSAGE_TO_THE_SOUTH,_AND_A_WALL
; OF_BROKEN_ROCK_TO_THE_EAST.__THERE_IS_A_PANEL_ON_THE_NORTH_WALL.[CR]
;
4BA4: 12 03     ; PANEL
4BA6: 01 02     ;    MoveToRoom(room_2)
4BA8: 03 03     ; S
4BAA: 01 19     ;    MoveToRoom(room_25)
4BAC: 02 03     ; E
4BAE: 01 1B     ;    MoveToRoom(room_27)
4BB0: 00

room_27:
; PS_17
; YOU_ARE_IN_THE_CHAMBER_OF_ANUBIS.[CR]
;
4BB1: 0A 03     ; D
4BB3: 01 1A     ;    MoveToRoom(room_26)
4BB5: 20 03     ; ??20??
4BB7: 01 1A     ;    MoveToRoom(room_26)
4BB9: 09 03     ; U
4BBB: 01 0D     ;    MoveToRoom(room_13)
4BBD: 00

room_28:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
4BBE: 01 03     ; N
4BC0: 01 1C     ;    MoveToRoom(room_28)
4BC2: 02 03     ; E
4BC4: 01 20     ;    MoveToRoom(room_32)
4BC6: 03 03     ; S
4BC8: 01 1E     ;    MoveToRoom(room_30)
4BCA: 04 03     ; W
4BCC: 01 1D     ;    MoveToRoom(room_29)
4BCE: 09 03     ; U
4BD0: 01 13     ;    MoveToRoom(room_19)
4BD2: 00

room_29:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
4BD3: 01 03     ; N
4BD5: 01 1C     ;    MoveToRoom(room_28)
4BD7: 02 03     ; E
4BD9: 01 33     ;    MoveToRoom(room_51)
4BDB: 03 03     ; S
4BDD: 01 1D     ;    MoveToRoom(room_29)
4BDF: 04 03     ; W
4BE1: 01 1D     ;    MoveToRoom(room_29)
4BE3: 00

room_30:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
4BE4: 01 03     ; N
4BE6: 01 20     ;    MoveToRoom(room_32)
4BE8: 02 03     ; E
4BEA: 01 2A     ;    MoveToRoom(room_42)
4BEC: 03 03     ; S
4BEE: 01 2B     ;    MoveToRoom(room_43)
4BF0: 04 03     ; W
4BF2: 01 1C     ;    MoveToRoom(room_28)
4BF4: 09 03     ; U
4BF6: 01 1F     ;    MoveToRoom(room_31)
4BF8: 0A 03     ; D
4BFA: 01 1F     ;    MoveToRoom(room_31)
4BFC: 00

room_31:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
4BFD: 09 03     ; U
4BFF: 01 1E     ;    MoveToRoom(room_30)
4C01: 0A 03     ; D
4C03: 01 1E     ;    MoveToRoom(room_30)
4C05: 00

room_32:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
4C06: 02 03     ; E
4C08: 01 1E     ;    MoveToRoom(room_30)
4C0A: 03 03     ; S
4C0C: 01 21     ;    MoveToRoom(room_33)
4C0E: 04 03     ; W
4C10: 01 1C     ;    MoveToRoom(room_28)
4C12: 00

room_33:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
4C13: 01 03     ; N
4C15: 01 2C     ;    MoveToRoom(room_44)
4C17: 02 03     ; E
4C19: 01 20     ;    MoveToRoom(room_32)
4C1B: 03 03     ; S
4C1D: 01 22     ;    MoveToRoom(room_34)
4C1F: 0A 03     ; D
4C21: 01 2D     ;    MoveToRoom(room_45)
4C23: 00

room_34:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
4C24: 02 03     ; E
4C26: 01 21     ;    MoveToRoom(room_33)
4C28: 03 03     ; S
4C2A: 01 23     ;    MoveToRoom(room_35)
4C2C: 04 03     ; W
4C2E: 01 25     ;    MoveToRoom(room_37)
4C30: 0A 03     ; D
4C32: 01 26     ;    MoveToRoom(room_38)
4C34: 00

room_35:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
4C35: 01 03     ; N
4C37: 01 24     ;    MoveToRoom(room_36)
4C39: 02 03     ; E
4C3B: 01 26     ;    MoveToRoom(room_38)
4C3D: 03 03     ; S
4C3F: 01 23     ;    MoveToRoom(room_35)
4C41: 04 03     ; W
4C43: 01 22     ;    MoveToRoom(room_34)
4C45: 09 03     ; U
4C47: 01 27     ;    MoveToRoom(room_39)
4C49: 0A 03     ; D
4C4B: 01 2F     ;    MoveToRoom(room_47)
4C4D: 00

room_36:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
4C4E: 01 03     ; N
4C50: 01 24     ;    MoveToRoom(room_36)
4C52: 02 03     ; E
4C54: 01 34     ;    MoveToRoom(room_52)
4C56: 04 03     ; W
4C58: 01 23     ;    MoveToRoom(room_35)
4C5A: 0A 03     ; D
4C5C: 01 30     ;    MoveToRoom(room_48)
4C5E: 00

room_37:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
4C5F: 02 03     ; E
4C61: 01 22     ;    MoveToRoom(room_34)
4C63: 04 03     ; W
4C65: 01 26     ;    MoveToRoom(room_38)
4C67: 00

room_38:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
4C68: 02 03     ; E
4C6A: 01 23     ;    MoveToRoom(room_35)
4C6C: 03 03     ; S
4C6E: 01 27     ;    MoveToRoom(room_39)
4C70: 04 03     ; W
4C72: 01 25     ;    MoveToRoom(room_37)
4C74: 09 03     ; U
4C76: 01 22     ;    MoveToRoom(room_34)
4C78: 00

room_39:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
4C79: 01 03     ; N
4C7B: 01 23     ;    MoveToRoom(room_35)
4C7D: 03 03     ; S
4C7F: 01 2E     ;    MoveToRoom(room_46)
4C81: 04 03     ; W
4C83: 01 26     ;    MoveToRoom(room_38)
4C85: 00

room_40:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
4C86: 01 03     ; N
4C88: 01 34     ;    MoveToRoom(room_52)
4C8A: 04 03     ; W
4C8C: 01 29     ;    MoveToRoom(room_41)
4C8E: 08 03     ; NW
4C90: 01 35     ;    MoveToRoom(room_53)
4C92: 00

room_41:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
4C93: 02 03     ; E
4C95: 01 28     ;    MoveToRoom(room_40)
4C97: 03 03     ; S
4C99: 01 34     ;    MoveToRoom(room_52)
4C9B: 04 03     ; W
4C9D: 01 32     ;    MoveToRoom(room_50)
4C9F: 00

room_42:
; PS_13
; DEAD_END.[CR]
;
4CA0: 04 03     ; W
4CA2: 01 1E     ;    MoveToRoom(room_30)
4CA4: 00

room_43:
; PS_13
; DEAD_END.[CR]
;
4CA5: 02 03     ; E
4CA7: 01 1E     ;    MoveToRoom(room_30)
4CA9: 00

room_44:
; PS_13
; DEAD_END.[CR]
;
4CAA: 03 03     ; S
4CAC: 01 21     ;    MoveToRoom(room_33)
4CAE: 00

room_45:
; PS_13
; DEAD_END.[CR]
;
4CAF: 09 03     ; U
4CB1: 01 21     ;    MoveToRoom(room_33)
4CB3: 00

room_46:
; PS_13
; DEAD_END.[CR]
;
4CB4: 04 03     ; W
4CB6: 01 27     ;    MoveToRoom(room_39)
4CB8: 00

room_47:
; PS_13
; DEAD_END.[CR]
;
4CB9: 09 03     ; U
4CBB: 01 23     ;    MoveToRoom(room_35)
4CBD: 00

room_48:
; PS_13
; DEAD_END.[CR]
;
4CBE: 09 03     ; U
4CC0: 01 24     ;    MoveToRoom(room_36)
4CC2: 00

room_49:
; PS_13
; DEAD_END.[CR]
;
4CC3: 02 03     ; E
4CC5: 01 34     ;    MoveToRoom(room_52)
4CC7: 00

room_50:
; PS_13
; DEAD_END.[CR]
;
4CC8: 02 03     ; E
4CCA: 01 29     ;    MoveToRoom(room_41)
4CCC: 00

room_51:
; PS_13
; DEAD_END.[CR]
;
4CCD: 04 03     ; W
4CCF: 01 1D     ;    MoveToRoom(room_29)
4CD1: 21 0B     ; DROP
4CD3: 11 29     ;    AssertObjectMatchesUserInput(obj_COINS)
4CD5: 15 29 00  ;    MoveObjectToRoom(obj_COINS, room_0)
4CD8: 18 23     ;    MoveObjectToCurrentRoom(obj_BATTERIES_fresh)
4CDA: 04 AC 7B  ;    Print(PS_B2:"THERE_ARE_NOW_SOME_FRESH_BATTERIES_HERE.[CR]")
4CDD: 00

room_52:
; PS_19
; YOU_ARE_ON_THE_BRINK_OF_A_LARGE_PIT.__YOU_COULD_CLIMB_DOWN,_BUT_
; YOU_WOULD_NOT_BE_ABLE_TO_CLIMB_BACK_UP.__THE_MAZE_CONTINUES_ON__
; THIS_LEVEL.[CR]
;
4CDE: 01 03     ; N
4CE0: 01 29     ;    MoveToRoom(room_41)
4CE2: 02 03     ; E
4CE4: 01 28     ;    MoveToRoom(room_40)
4CE6: 03 03     ; S
4CE8: 01 31     ;    MoveToRoom(room_49)
4CEA: 04 03     ; W
4CEC: 01 24     ;    MoveToRoom(room_36)
4CEE: 0A 03     ; D
4CF0: 01 0B     ;    MoveToRoom(room_11)
4CF2: 00

room_53:
; PS_13
; DEAD_END.[CR]
;
4CF3: 06 03     ; SE
4CF5: 01 28     ;    MoveToRoom(room_40)
4CF7: 00

room_54:
; PS_1A
; YOU_ARE_IN_A_DIRTY_BROKEN_PASSAGE.__TO_THE_EAST_IS_A_CRAWL.__TO_
; THE_WEST_IS_A_LARGE_PASSAGE.__ABOVE_YOU_IS_A_HOLE_TO_ANOTHER____
; PASSAGE.[CR]
;
4CF8: 02 03     ; E
4CFA: 01 37     ;    MoveToRoom(room_55)
4CFC: 04 03     ; W
4CFE: 01 39     ;    MoveToRoom(room_57)
4D00: 09 03     ; U
4D02: 01 19     ;    MoveToRoom(room_25)
4D04: 00

room_55:
; PS_1B
; YOU_ARE_ON_THE_BRINK_OF_A_SMALL_CLEAN_CLIMBABLE_PIT.__A_CRAWL___
; LEADS_WEST.[CR]
;
4D05: 04 03     ; W
4D07: 01 36     ;    MoveToRoom(room_54)
4D09: 0A 03     ; D
4D0B: 01 38     ;    MoveToRoom(room_56)
4D0D: 11 03     ; CLIMB
4D0F: 01 38     ;    MoveToRoom(room_56)
4D11: 00

room_56:
; PS_1C
; YOU_ARE_IN_THE_BOTTOM_OF_A_SMALL_PIT_WITH_A_LITTLE_STREAM,_WHICH
; ENTERS_AND_EXITS_THROUGH_TINY_SLITS.[CR]
;
4D12: 09 03     ; U
4D14: 01 37     ;    MoveToRoom(room_55)
4D16: 0C 03     ; OUT
4D18: 01 37     ;    MoveToRoom(room_55)
4D1A: 11 03     ; CLIMB
4D1C: 01 37     ;    MoveToRoom(room_55)
4D1E: 0A 04     ; D
4D20: 04 CF 71  ;    Print(PS_73:"YOU_DON'T_FIT_THROUGH_TWO-INCH_SLIT![CR]")
4D23: 27 0B     ; FILL
4D25: 07 06     ;    StopIfPassElseContinue
4D27: 02 1C     ;        AssertObjectIsInPack(obj_WATER)
4D29: 04 8B 7A  ;        Print(PS_AC:"YOUR_BOTTLE_IS_ALREADY_FULL.[CR]")
4D2C: 19 1C 1B  ;    MoveObjectIntoContainer(obj_WATER, obj_BOTTLE)
4D2F: 00

room_57:
; PS_1D
; YOU_ARE_IN_A_THE_ROOM_OF_BES,_WHOSE_PICTURE_IS_ON_THE_WALL._____
; THERE_IS_A_BIG_HOLE_IN_THE_FLOOR.__THERE_IS_A_PASSAGE_LEADING___
; EAST.[CR]
;
4D30: 02 03     ; E
4D32: 01 36     ;    MoveToRoom(room_54)
4D34: 0A 03     ; D
4D36: 01 3A     ;    MoveToRoom(room_58)
4D38: 00

room_58:
; PS_1E
; YOU_ARE_AT_A_COMPLEX_JUNCTION.__A_LOW_HANDS_AND_KNEES_PASSAGE___
; FROM_THE_NORTH_JOINS_A_HIGHER_CRAWL_FROM_THE_EAST_TO_MAKE_A_____
; WALKING_PASSAGE_GOING_WEST.__THERE_IS_ALSO_A_LARGE_ROOM_ABOVE.__
; THE_AIR_IS_DAMP_HERE.[CR]
;
4D39: 01 03     ; N
4D3B: 01 3D     ;    MoveToRoom(room_61)
4D3D: 02 03     ; E
4D3F: 01 3B     ;    MoveToRoom(room_59)
4D41: 04 03     ; W
4D43: 01 41     ;    MoveToRoom(room_65)
4D45: 09 03     ; U
4D47: 01 39     ;    MoveToRoom(room_57)
4D49: 11 03     ; CLIMB
4D4B: 01 39     ;    MoveToRoom(room_57)
4D4D: 00

room_59:
; PS_1F
; YOU_ARE_IN_THE_UNDERWORLD_ANTEROOM_OF_SEKER.__PASSAGES_GO_EAST,_
; WEST,_AND_UP.__HUMAN_BONES_ARE_STREWN_ABOUT_ON_THE_FLOOR._______
; HIEROGLYPHICS_ON_THE_WALL_ROUGHLY_TRANSLATE_TO_"THOSE_WHO_______
; PROCEED_EAST_MAY_NEVER_RETURN."[CR]
;
4D4E: 02 03     ; E
4D50: 01 3C     ;    MoveToRoom(room_60)
4D52: 04 03     ; W
4D54: 01 41     ;    MoveToRoom(room_65)
4D56: 09 03     ; U
4D58: 01 3A     ;    MoveToRoom(room_58)
4D5A: 00

room_60:
; PS_20
; YOU_ARE_AT_THE_LAND_OF_DEAD.__PASSAGES_LEAD_OFF_IN_>ALL<________
; DIRECTIONS.[CR]
;
4D5B: 01 07     ; N
4D5D: 07 03     ;    StopIfPassElseContinue
4D5F: 0A F0     ;        AssertRandomIsLessOrEqual(240)
4D61: 01 3B     ;    MoveToRoom(room_59)
4D63: 02 07     ; E
4D65: 07 03     ;    StopIfPassElseContinue
4D67: 0A F0     ;        AssertRandomIsLessOrEqual(240)
4D69: 01 3B     ;    MoveToRoom(room_59)
4D6B: 03 07     ; S
4D6D: 07 03     ;    StopIfPassElseContinue
4D6F: 0A F0     ;        AssertRandomIsLessOrEqual(240)
4D71: 01 3B     ;    MoveToRoom(room_59)
4D73: 05 07     ; NE
4D75: 07 03     ;    StopIfPassElseContinue
4D77: 0A F0     ;        AssertRandomIsLessOrEqual(240)
4D79: 01 3B     ;    MoveToRoom(room_59)
4D7B: 06 07     ; SE
4D7D: 07 03     ;    StopIfPassElseContinue
4D7F: 0A F0     ;        AssertRandomIsLessOrEqual(240)
4D81: 01 3B     ;    MoveToRoom(room_59)
4D83: 07 07     ; SW
4D85: 07 03     ;    StopIfPassElseContinue
4D87: 0A F0     ;        AssertRandomIsLessOrEqual(240)
4D89: 01 3B     ;    MoveToRoom(room_59)
4D8B: 08 07     ; NW
4D8D: 07 03     ;    StopIfPassElseContinue
4D8F: 0A F0     ;        AssertRandomIsLessOrEqual(240)
4D91: 01 3B     ;    MoveToRoom(room_59)
4D93: 09 07     ; U
4D95: 07 03     ;    StopIfPassElseContinue
4D97: 0A F0     ;        AssertRandomIsLessOrEqual(240)
4D99: 01 3B     ;    MoveToRoom(room_59)
4D9B: 04 06     ; W
4D9D: 04 23 72  ;    Print(PS_75:"YOU_HAVE_CRAWLED_AROUND_IN_SOME_LITTLE_HOLES_AND_FOUND_YOUR_WAY_
;                                 BLOCKED_BY_A_FALLEN_SLAB.__YOU_ARE_NOW_BACK_IN_THE_MAIN_PASSAGE.[CR]")
4DA0: 01 3C     ;    MoveToRoom(room_60)
4DA2: 00

room_61:
; PS_21
; YOU'RE_IN_A_LARGE_ROOM_WITH_ANCIENT_DRAWINGS_ON_ALL_WALLS.______
; THE_PICTURES_DEPICT_ATUM,_A_PHARAOH_WEARING_THE_DOUBLE_CROWN.___
; A_SHALLOW_PASSAGE_PROCEEDS_DOWNWARD,_AND_A_SOMEWHAT_STEEPER_ONE_
; LEADS_UP.__A_LOW_HANDS_AND_KNEES_PASSAGE_ENTERS_FROM_THE_SOUTH. [CR]
;
4DA3: 03 11     ; S
4DA5: 07 06     ;    StopIfPassElseContinue
4DA7: 02 17     ;        AssertObjectIsInPack(obj_SARCOPH_full)
4DA9: 04 7B 72  ;        Print(PS_76:"YOU_CAN'T_FIT_THIS_BIG_SARCOPHAGUS_THROUGH_THAT_LITTLE_PASSAGE![CR]")
4DAC: 07 06     ;    StopIfPassElseContinue
4DAE: 02 18     ;        AssertObjectIsInPack(obj_SARCOPH_empty)
4DB0: 04 7B 72  ;        Print(PS_76:"YOU_CAN'T_FIT_THIS_BIG_SARCOPHAGUS_THROUGH_THAT_LITTLE_PASSAGE![CR]")
4DB3: 01 3A     ;    MoveToRoom(room_58)
4DB5: 09 03     ; U
4DB7: 01 3E     ;    MoveToRoom(room_62)
4DB9: 0A 03     ; D
4DBB: 01 3F     ;    MoveToRoom(room_63)
4DBD: 00

room_62:
; PS_22
; YOU_ARE_IN_A_CHAMBER_WHOSE_WALL_CONTAINS_A_PICTURE_OF_A_MAN_____
; WEARING_THE_LUNAR_DISK_ON_HIS_HEAD.__HE_IS_THE_GOD_KHONS,_THE___
; MOON_GOD.[CR]
;
4DBE: 0A 03     ; D
4DC0: 01 3D     ;    MoveToRoom(room_61)
4DC2: 0C 03     ; OUT
4DC4: 01 3D     ;    MoveToRoom(room_61)
4DC6: 00

room_63:
; PS_23
; YOU_ARE_IN_A_LONG_SLOPING_CORRIDOR_WITH_RAGGED_WALLS._ [CR]
;
4DC7: 09 03     ; U
4DC9: 01 3D     ;    MoveToRoom(room_61)
4DCB: 0A 03     ; D
4DCD: 01 40     ;    MoveToRoom(room_64)
4DCF: 00

room_64:
; PS_24
; YOU_ARE_IN_A_CUL-DE-SAC_ABOUT_EIGHT_FEET_ACROSS.[CR]
;
4DD0: 09 03     ; U
4DD2: 01 3F     ;    MoveToRoom(room_63)
4DD4: 0C 03     ; OUT
4DD6: 01 3F     ;    MoveToRoom(room_63)
4DD8: 00

room_65:
; PS_25
; YOU_ARE_IN_THE_CHAMBER_OF_HORUS,_A_LONG_EAST/WEST_PASSAGE_WITH__
; HOLES_EVERYWHERE.__TO_EXPLORE_AT_RANDOM,_SELECT_NORTH,_SOUTH,___
; UP,_OR_DOWN.[CR]
;
4DD9: 02 03     ; E
4DDB: 01 3A     ;    MoveToRoom(room_58)
4DDD: 04 03     ; W
4DDF: 01 4E     ;    MoveToRoom(room_78)
4DE1: 09 07     ; U
4DE3: 07 03     ;    StopIfPassElseContinue
4DE5: 0A CC     ;        AssertRandomIsLessOrEqual(204)
4DE7: 01 48     ;    MoveToRoom(room_72)
4DE9: 01 07     ; N
4DEB: 07 03     ;    StopIfPassElseContinue
4DED: 0A CC     ;        AssertRandomIsLessOrEqual(204)
4DEF: 01 49     ;    MoveToRoom(room_73)
4DF1: 03 07     ; S
4DF3: 07 03     ;    StopIfPassElseContinue
4DF5: 0A CC     ;        AssertRandomIsLessOrEqual(204)
4DF7: 01 42     ;    MoveToRoom(room_66)
4DF9: 0A 07     ; D
4DFB: 07 03     ;    StopIfPassElseContinue
4DFD: 0A CC     ;        AssertRandomIsLessOrEqual(204)
4DFF: 01 3B     ;    MoveToRoom(room_59)
4E01: 00

room_66:
; PS_26
; YOU_ARE_IN_A_LARGE_LOW_CIRCULAR_CHAMBER_WHOSE_FLOOR_IS_AN_______
; IMMENSE_SLAB_FALLEN_FROM_THE_CEILING.__EAST_AND_WEST_THERE_ONCE_
; WHERE_LARGE_PASSAGES,_BUT_THEY_ARE_NOW_FILLED_WITH_SAND.________
; LOW_SMALL_PASSAGES_GO_NORTH_AND_SOUTH.[CR]
;
4E02: 01 03     ; N
4E04: 01 41     ;    MoveToRoom(room_65)
4E06: 03 03     ; S
4E08: 01 50     ;    MoveToRoom(room_80)
4E0A: 00

room_72:
; PS_27
; YOU_ARE_IN_THE_PRIEST'S_BEDROOM.__THE_WALLS_ARE_COVERED_WITH____
; CURTAINS,_THE_FLOOR_WITH_A_THICK_PILE_CARPET.__MOSS_COVERS_THE__
; CEILING.[CR]
;
4E0B: 04 03     ; W
4E0D: 01 41     ;    MoveToRoom(room_65)
4E0F: 0C 03     ; OUT
4E11: 01 41     ;    MoveToRoom(room_65)
4E13: 00

room_73:
; PS_28
; THIS_IS_THE_CHAMBER_OF_THE_HIGH_PRIEST.___ANCIENT_DRAWINGS_COVER
; THE_WALLS.__AN_EXTREMELY_TIGHT_TUNNEL_LEADS_WEST.__IT_LOOKS_LIKE
; A_TIGHT_SQUEEZE.__ANOTHER_PASSAGE_LEADS_SE.[CR]
;
4E14: 04 09     ; W
4E16: 07 04     ;    StopIfPassElseContinue
4E18: 0D        ;        AssertPackIsEmptyExceptForEmerald
4E19: 01 4C     ;        MoveToRoom(room_76)
4E1B: 04 A7 72  ;    Print(PS_77:"SOMETHING_YOU'RE_CARRYING_WON'T_FIT_THROUGH_THE_TUNNEL_WITH_YOU.
;                                 YOU'D_BEST_TAKE_INVENTORY_AND_DROP_SOMETHING.[CR]")
4E1E: 06 03     ; SE
4E20: 01 41     ;    MoveToRoom(room_65)
4E22: 00

room_76:
; PS_29
; YOU_ARE_IN_THE_HIGH_PRIEST'S_TREASURE_ROOM_LIT_BY_AN_EERIE_GREEN
; LIGHT.__A_NARROW_TUNNEL_EXITS_TO_THE_EAST.[CR]
;
4E23: 02 09     ; E
4E25: 07 04     ;    StopIfPassElseContinue
4E27: 0D        ;        AssertPackIsEmptyExceptForEmerald
4E28: 01 49     ;        MoveToRoom(room_73)
4E2A: 04 A7 72  ;    Print(PS_77:"SOMETHING_YOU'RE_CARRYING_WON'T_FIT_THROUGH_THE_TUNNEL_WITH_YOU.
;                                 YOU'D_BEST_TAKE_INVENTORY_AND_DROP_SOMETHING.[CR]")
4E2D: 0C 09     ; OUT
4E2F: 07 04     ;    StopIfPassElseContinue
4E31: 0D        ;        AssertPackIsEmptyExceptForEmerald
4E32: 01 49     ;        MoveToRoom(room_73)
4E34: 04 A7 72  ;    Print(PS_77:"SOMETHING_YOU'RE_CARRYING_WON'T_FIT_THROUGH_THE_TUNNEL_WITH_YOU.
;                                 YOU'D_BEST_TAKE_INVENTORY_AND_DROP_SOMETHING.[CR]")
4E37: 00

room_78:
; PS_2A
; YOU_ARE_AT_THE_EAST_END_OF_THE_TWOPIT_ROOM.__THE_FLOOR_HERE_IS__
; LITTERED_WITH_THIN_ROCK_SLABS,_WHICH_MAKE_IT_EASY_TO_DESCEND_THE
; PITS.__THERE_IS_A_PATH_HERE_BYPASSING_THE_PITS_TO_CONNECT_______
; PASSAGES_EAST_AND_WEST.__THERE_ARE_HOLES_ALL_OVER,_BUT_THE_ONLY_
; BIG_ONE_IS_ON_THE_WALL_DIRECTLY_OVER_THE_WEST_PIT_WHERE_YOU_____
; CAN'T_GET_TO_IT.[CR]
;
4E38: 02 03     ; E
4E3A: 01 41     ;    MoveToRoom(room_65)
4E3C: 04 03     ; W
4E3E: 01 50     ;    MoveToRoom(room_80)
4E40: 0A 03     ; D
4E42: 01 4F     ;    MoveToRoom(room_79)
4E44: 00

room_79:
; PS_2B
; YOU_ARE_AT_THE_BOTTOM_OF_THE_EASTERN_PIT_IN_THE_TWOPIT_ROOM.[CR]
;
4E45: 09 03     ; U
4E47: 01 4E     ;    MoveToRoom(room_78)
4E49: 0C 03     ; OUT
4E4B: 01 4E     ;    MoveToRoom(room_78)
4E4D: 00

room_80:
; PS_2C
; YOU_ARE_AT_THE_WEST_END_OF_THE_TWOPIT_ROOM.__THERE_IS_A_LARGE___
; HOLE_IN_THE_WALL_ABOVE_THE_PIT_AT_THIS_END_OF_THE_ROOM.[CR]
;
4E4E: 02 03     ; E
4E50: 01 4E     ;    MoveToRoom(room_78)
4E52: 04 03     ; W
4E54: 01 42     ;    MoveToRoom(room_66)
4E56: 0A 03     ; D
4E58: 01 51     ;    MoveToRoom(room_81)
4E5A: 00

room_81:
; PS_2D
; YOU_ARE_AT_THE_BOTTOM_OF_THE_WEST_PIT_IN_THE_TWOPIT_ROOM.__THERE
; IS_A_LARGE_HOLE_IN_THE_WALL_ABOUT_TWENTY_FIVE_FEET_ABOVE_YOU.[CR]
;
4E5B: 09 03     ; U
4E5D: 01 50     ;    MoveToRoom(room_80)
4E5F: 0C 03     ; OUT
4E61: 01 50     ;    MoveToRoom(room_80)
4E63: 11 16     ; CLIMB
4E65: 07 08     ;    StopIfPassElseContinue
4E67: 03 09     ;        AssertObjectIsInCurrentRoomOrPack(obj_PLANT_C)
4E69: 04 F2 72  ;        Print(PS_78:"YOU_CLAMBER_UP_THE_PLANT_AND_SCURRY_THROUGH_THE_HOLE_AT_THE_TOP.[CR]")
4E6C: 01 4D     ;        MoveToRoom(room_77)
4E6E: 07 06     ;    StopIfPassElseContinue
4E70: 03 08     ;        AssertObjectIsInCurrentRoomOrPack(obj_PLANT_B)
4E72: 04 1F 73  ;        Print(PS_79:"YOU'VE_CLIMBED_UP_THE_PLANT_AND_OUT_OF_THE_PIT.[CR]")
4E75: 01 50     ;    MoveToRoom(room_80)
4E77: 04 D1 7C  ;    Print(PS_B8:"THERE_IS_NOTHING_HERE_TO_CLIMB.__USE_UP_OR_OUT_TO_LEAVE_THE_PIT.[CR]")
4E7A: 24 2F     ; POUR
4E7C: 11 1C     ;    AssertObjectMatchesUserInput(obj_WATER)
4E7E: 15 1C 00  ;    MoveObjectToRoom(obj_WATER, room_0)
4E81: 07 0E     ;    StopIfPassElseContinue
4E83: 03 07     ;        AssertObjectIsInCurrentRoomOrPack(obj_PLANT_A)
4E85: 15 07 00  ;        MoveObjectToRoom(obj_PLANT_A, room_0)
4E88: 18 08     ;        MoveObjectToCurrentRoom(obj_PLANT_B)
4E8A: 04 56 7C  ;        Print(PS_B5:"THE_PLANT_SPURTS_INTO_FURIOUS_GROWTH_FOR_A_FEW_SECONDS.[CR]")
4E8D: 04 C5 6D  ;        Print(PS_4C:"THERE_IS_A_TWELVE_FOOT_BEAN_STALK_STRETCHING_UP_OUT_OF_THE_PIT,_
;                                     BELLOWING_"WATER..._WATER..."[CR]")
4E90: 07 0E     ;    StopIfPassElseContinue
4E92: 03 08     ;        AssertObjectIsInCurrentRoomOrPack(obj_PLANT_B)
4E94: 15 08 00  ;        MoveObjectToRoom(obj_PLANT_B, room_0)
4E97: 18 09     ;        MoveObjectToCurrentRoom(obj_PLANT_C)
4E99: 04 7D 7C  ;        Print(PS_B6:"THE_PLANT_GROWS_EXPLOSIVELY,_ALMOST_FILLING_THE_BOTTOM_OF_THE___
;                                     PIT.[CR]")
4E9C: 04 05 6E  ;        Print(PS_4D:"THERE_IS_A_GIGANTIC_BEAN_STALK_STRETCHING_ALL_THE_WAY_UP_TO_THE_
;                                     HOLE.[CR]")
4E9F: 15 09 00  ;    MoveObjectToRoom(obj_PLANT_C, room_0)
4EA2: 18 07     ;    MoveObjectToCurrentRoom(obj_PLANT_A)
4EA4: 04 AD 7C  ;    Print(PS_B7:"YOU'VE_OVER-WATERED_THE_PLANT!__IT'S_SHRIVELING_UP![CR]")
4EA7: 04 99 6D  ;    Print(PS_4B:"THERE_IS_A_TINY_PLANT_IN_THE_PIT,_MURMURING_"WATER,_WATER,_..."[CR]")
4EAA: 00

room_77:
; PS_2E
; YOU_ARE_IN_A_LONG,_NARROW_CORRIDOR_STRETCHING_OUT_OF_SIGHT_TO___
; THE_WEST.__AT_THE_EASTERN_END_IS_A_HOLE_THROUGH_WHICH_YOU_CAN___
; SEE_A_PROFUSION_OF_LEAVES.[CR]
;
4EAB: 02 03     ; E
4EAD: 01 51     ;    MoveToRoom(room_81)
4EAF: 0A 03     ; D
4EB1: 01 51     ;    MoveToRoom(room_81)
4EB3: 11 03     ; CLIMB
4EB5: 01 51     ;    MoveToRoom(room_81)
4EB7: 10 05     ; JUMP
4EB9: 04 C5 70  ;    Print(PS_6B:"YOU_ARE_AT_THE_BOTTOM_OF_THE_PIT_WITH_A_BROKEN_NECK.[CR]")
4EBC: 05        ;    PrintScoreAndStop
4EBD: 04 03     ; W
4EBF: 01 47     ;    MoveToRoom(room_71)
4EC1: 00

room_71:
; PS_2F
; YOU_ARE_IN_THE_CHAMBER_OF_OSIRIS._THE_CEILING_IS_TOO_HIGH_UP_FOR
; YOUR_LAMP_TO_SHOW_IT.__PASSAGES_LEAD_EAST,_NORTH,_AND_SOUTH.[CR]
;
4EC2: 01 03     ; N
4EC4: 01 44     ;    MoveToRoom(room_68)
4EC6: 02 03     ; E
4EC8: 01 46     ;    MoveToRoom(room_70)
4ECA: 03 03     ; S
4ECC: 01 4D     ;    MoveToRoom(room_77)
4ECE: 00

room_70:
; PS_30
; THE_PASSAGE_HERE_IS_BLOCKED_BY_A_FALLEN_BLOCK.[CR]
;
4ECF: 03 03     ; S
4ED1: 01 47     ;    MoveToRoom(room_71)
4ED3: 0C 03     ; OUT
4ED5: 01 47     ;    MoveToRoom(room_71)
4ED7: 00

room_68:
; PS_31
; YOU_ARE_IN_THE_CHAMBER_OF_NEKHEBET,_A_WOMAN_WITH_THE_HEAD_OF_A__
; VULTURE,_WEARING_THE_CROWN_OF_EGYPT.__A_PASSAGE_EXITS_TO_THE____
; SOUTH.[CR]
;
4ED8: 03 03     ; S
4EDA: 01 47     ;    MoveToRoom(room_71)
4EDC: 0C 03     ; OUT
4EDE: 01 47     ;    MoveToRoom(room_71)
4EE0: 00         

4EE1: FF              
```

# Ambient Light Table

When we calculate the score, we look at the upper bit in each room. If the bit is set, the second value
is added to the score. This mechanism is not used by the existing code -- probably an old feature.

This is the beginning of the save-to-tape. Maybe at one time, the ambient light changed?
It doesn't now, and there is no need to save this table. We could have just started
saving with the object data.

```code
; 2 bytes per room
; * 0x4000 means there is light in the room (no need for a lamp)
; * 0x0000 means you better have a lamp
;
; 2nd byte is BCD score if upper bit is set of 1st byte

AmbientLightTable:
4EE2: 40 00    ;  1 (has natural light)
4EE4: 40 00    ;  2 (has natural light)
4EE6: 40 00    ;  3 (has natural light)
4EE8: 40 00    ;  4 (has natural light)
4EEA: 40 00    ;  5 (has natural light)
4EEC: 40 00    ;  6 (has natural light)
4EEE: 40 00    ;  7 (has natural light)
4EF0: 00 00    ;  8
4EF2: 00 00    ;  9
4EF4: 00 00    ;  10
4EF6: 00 00    ;  11
4EF8: 00 00    ;  12
4EFA: 00 00    ;  13
4EFC: 00 00    ;  14
4EFE: 00 00    ;  15
4F00: 00 00    ;  16
4F02: 00 00    ;  17
4F04: 00 00    ;  18
4F06: 00 00    ;  19
4F08: 00 00    ;  20
4F0A: 00 00    ;  21
4F0C: 00 00    ;  22
4F0E: 00 00    ;  23
4F10: 00 00    ;  24
4F12: 00 00    ;  25
4F14: 00 00    ;  26
4F16: 00 00    ;  27
4F18: 00 00    ;  28
4F1A: 00 00    ;  29
4F1C: 00 00    ;  30
4F1E: 00 00    ;  31
4F20: 00 00    ;  32
4F22: 00 00    ;  33
4F24: 00 00    ;  34
4F26: 00 00    ;  35
4F28: 00 00    ;  36
4F2A: 00 00    ;  37
4F2C: 00 00    ;  38
4F2E: 00 00    ;  39
4F30: 00 00    ;  40
4F32: 00 00    ;  41
4F34: 00 00    ;  42
4F36: 00 00    ;  43
4F38: 00 00    ;  44
4F3A: 00 00    ;  45
4F3C: 00 00    ;  46
4F3E: 00 00    ;  47
4F40: 00 00    ;  48
4F42: 00 00    ;  49
4F44: 00 00    ;  50
4F46: 00 00    ;  51
4F48: 00 00    ;  52
4F4A: 00 00    ;  53
4F4C: 00 00    ;  54
4F4E: 00 00    ;  55
4F50: 00 00    ;  56
4F52: 00 00    ;  57
4F54: 00 00    ;  58
4F56: 00 00    ;  59
4F58: 00 00    ;  60
4F5A: 00 00    ;  61
4F5C: 00 00    ;  62
4F5E: 00 00    ;  63
4F60: 00 00    ;  64
4F62: 00 00    ;  65
4F64: 00 00    ;  66
4F66: 00 00    ;  67
4F68: 00 00    ;  68
4F6A: 00 00    ;  69
4F6C: 00 00    ;  70
4F6E: 00 00    ;  71
4F70: 00 00    ;  72
4F72: 00 00    ;  73
4F74: 00 00    ;  74
4F76: 00 00    ;  75
4F78: 40 00    ;  76 (has light -- "LIT_BY_AN_ERRIE_GREEN_LIGHT")
4F7A: 00 00    ;  77
4F7C: 00 00    ;  78
4F7E: 00 00    ;  79
4F80: 00 00    ;  80
4F82: 00 00    ;  81
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
;   M - if set, the second byte is an object number (container). if clear, the second byte is a room number.
;   C - if set, object can be picked up.
;   T - if set, object is treasure.
;
;   RRRRRRRR - Second byte is the object's location (containing object or room number).

ObjectData:
; Object data table (2 bytes)
;             MCT             #    Name                 Start location
4F84: 00 00 ; 000_00000 00  ; 1    obj_bridge_15        *
4F86: 00 00 ; 000_00000 00  ; 2    obj_bridge_18        *
4F88: 00 00 ;               ; 3
4F8A: 00 00 ;               ; 4
4F8C: 00 00 ;               ; 5 
4F8E: 00 33 ; 000_00000 33  ; 6    obj_MACHINE          (Room 51)
4F90: 00 51 ; 000_00000 51  ; 7    obj_PLANT_A          (Room 81)
4F92: 00 00 ; 000_00000 00  ; 8    obj_PLANT_B          *
4F94: 00 00 ; 000_00000 00  ; 9    obj_PLANT_C          *
4F96: 00 00 ; 000_00000 00  ; 10
4F98: 00 10 ; 000_00000 10  ; 11   obj_SERPENT (Room 16)
4F9A: 00 00 ;               ; 12 
4F9C: 00 00 ;               ; 13
4F9E: 40 02 ; 010_00000 02  ; 14   obj_LAMP_off         (Room 2)
4FA0: 40 00 ; 010_00000 00  ; 15   obj_LAMP_on          *
4FA2: 40 08 ; 010_00000 08  ; 16   obj_BOX              (Room 8)
4FA4: 40 09 ; 010_00000 09  ; 17   obj_SCEPTER          (Room 9)
4FA6: 40 48 ; 010_00000 48  ; 18   obj_PILLOW           (Room 72)
4FA8: 40 0B ; 010_00000 0B  ; 19   obj_BIRD             (Room 11)
4FAA: 00 00 ; 000_00000 00  ; 20   obj_BIRD_boxed       *
4FAC: 00 00 ; 000_00000 00  ; 21   obj_POTTERY          *
4FAE: 60 00 ; 011_00000 00  ; 22   obj_PEARL            *
4FB0: 40 3D ; 010_00000 3D  ; 23   obj_SARCOPH_full     (Room 61)
4FB2: 40 00 ; 010_00000 00  ; 24   obj_SARCOPH_empty    *
4FB4: 40 3B ; 010_00000 3B  ; 25   obj_MAGAZINES        (Room 59)
4FB6: 40 02 ; 010_00000 02  ; 26   obj_FOOD             (Room 2)
4FB8: 40 02 ; 010_00000 02  ; 27   obj_BOTTLE           (Room 2)
4FBA: C0 1B ; 110_00000 1B  ; 28   obj_WATER            (Room 27)
4FBC: 00 00 ;               ; 29
4FBE: 00 38 ; 000_00000 38  ; 30   obj_STREAM_56        (Room 56)
4FC0: 60 4C ; 011_00000 4C  ; 31   obj_EMERALD          (Room 76)
4FC2: 60 00 ; 011_00000 00  ; 32   obj_VASE_pillow      *
4FC4: 60 49 ; 011_00000 49  ; 33   obj_VASE_solo        (Room 73)
4FC6: 60 44 ; 011_00000 44  ; 34   obj_KEY              (Room 68)
4FC8: 40 00 ; 010_00000 00  ; 35   obj_BATTERIES_fresh  *
4FCA: 40 00 ; 010_00000 00  ; 36   obj_BATTERIES_worn   *
4FCC: 60 0E ; 011_00000 0E  ; 37   obj_GOLD             (Room 14)
4FCE: 60 11 ; 011_00000 11  ; 38   obj_DIAMNODS         (Room 17) 
4FD0: 60 19 ; 011_00000 19  ; 39   obj_SILVER           (Room 25)
4FD2: 60 12 ; 011_00000 12  ; 40   obj_JEWELRY          (Room 18)
4FD4: 60 18 ; 011_00000 18  ; 41   obj_COINS            (Room 24)
4FD6: 60 00 ; 011_00000 00  ; 42   obj_CHEST            *
4FD8: 60 47 ; 011_00000 47  ; 43   obj_NEST             (Room 71)
4FDA: 40 00 ; 010_00000 00  ; 44   obj_LAMP_dead        *
```

# Game Variables

```code
currentRoom:
4FDC: 01 

bcdTurnCountLSB:
4FDD: 00 

bcdTurnCountMSB:
4FDE: 00        

lampOnTurnCount:
4FDF: 00 00 ; Number of turns the lamp has been on

lastRoom:
4FE1: 00             

numObjInPack:
4FE2: 00          

numResurrected:
4FE3: 00 ; Number of times resurrected?
```

# Object Info

The LoadGame code restores the 1st four bytes of this table even though only the 1st byte
is mangled (bug in code?).

```code
ObjectDescriptions:
; Object descriptions (44 objects)
; For packable objects each slot points to a message pair. The first is the long
; description and the second is the short description for the backpack.
;                  # Name              Description
4FE4: AC 6C     ;  1 obj_bridge_15        PS_40 Stone bridge room 15
4FE6: AC 6C     ;  2 obj_bridge_18        PS_40 Stone bridge room 18
4FE8: 5D 47     ;  3                   -Never used (points to empty string)
4FEA: 5D 47     ;  4                   -Never used (points to empty string)
4FEC: 5D 47     ;  5                   -Never used (points to empty string)
4FEE: 35 6E     ;  6 obj_MACHINE          PS_4E Vending Machine
4FF0: 99 6D     ;  7 obj_PLANT_A          PS_4B Tiny plant
4FF2: C5 6D     ;  8 obj_PLANT_B          PS_4C Twelve foot beanstalk
4FF4: 05 6E     ;  9 obj_PLANT_C          PS_4D Giant beanstalk
4FF6: 00 00     ; 10                   -Never used (points to null)
4FF8: 8E 6C     ; 11 obj_SERPENT          PS_3F Serpent bars the way
4FFA: 00 00     ; 12                   -Never used (points to null)
4FFC: 00 00     ; 13                   -Never used (points to null)
4FFE: 82 6B     ; 14 obj_LAMP_off         PS_32 Lamp (not lit)
5000: A7 6B     ; 15 obj_LAMP_on          PS_34 Lamp (lit)
5002: C9 6B     ; 16 obj_BOX              PS_36 Statue box
5004: F2 6B     ; 17 obj_SCEPTER          PS_38 Scepter
5006: 66 6C     ; 18 obj_PILLOW           PS_3D Pillow
5008: 21 6C     ; 19 obj_BIRD             PS_3A Statue
500A: 3F 6C     ; 20 obj_BIRD_boxed       PS_3B Statue in box
500C: 41 70     ; 21 obj_POTTERY          PS_66 Pottery
500E: 9B 70     ; 22 obj_PEARL            PS_69 Pearl
5010: CC 6C     ; 23 obj_SARCOPH_full     PS_41 Sarcophagus with pearl
5012: CC 6C     ; 24 obj_SARCOPH_empty    PS_41 Sarcophagus empty
5014: 05 6D     ; 25 obj_MAGAZINES        PS_43 Magazines
5016: 40 6D     ; 26 obj_FOOD             PS_45 Food
5018: 58 6D     ; 27 obj_BOTTLE           PS_47 Bottle
501A: 74 6D     ; 28 obj_WATER            PS_49 Water in the bottle
501C: 5D 47     ; 29                   -Never used (points to empty string)
501E: 5D 47     ; 30 obj_STREAM_56        EmptyString Stream in room 56
5020: 68 70     ; 31 obj_EMERALD          PS_67 Emerald
5022: 19 70     ; 32 obj_VASE_pillow      PS_65 Vase on pillow
5024: F6 6F     ; 33 obj_VASE_solo        PS_63 Vase
5026: D2 6F     ; 34 obj_KEY              PS_61 Key
5028: 84 6E     ; 35 obj_BATTERIES_fresh  PS_4F Batteries
502A: A3 6E     ; 36 obj_BATTERIES_worn   PS_51 Worn-out batteries
502C: CF 6E     ; 37 obj_GOLD             PS_53 Gold Nugget
502E: FF 6E     ; 38 obj_DIAMNODS         PS_55 Diamonds
5030: 1E 6F     ; 39 obj_SILVER           PS_57 Silver
5032: 3E 6F     ; 40 obj_JEWELRY          PS_59 Jewelry
5034: 62 6F     ; 41 obj_COINS            PS_5B Coins
5036: 7F 6F     ; 42 obj_CHEST            PS_5D Chest
5038: A6 6F     ; 43 obj_NEST             PS_5F Nest of golden eggs
503A: 82 6B     ; 44 obj_LAMP_dead        PS_32 Lamp (dead)
```

# Script Commands

```code
; This lookup table holds the pointers to the individual script commands. Each command
; reads 1 or 2 bytes of data from the script. The number of extra bytes read is show
; for reference in the table.

ScriptCommands:
;    Address   Number Bytes Name
503C: 27 51   ;   1     1   MoveToRoom(room_num)
503E: 65 52   ;   2     1   AssertObjectIsInPack(obj_num)
5040: 74 52   ;   3     1   AssertObjectIsInCurrentRoomOrPack(obj_num)
5042: FB 52   ;   4     2   Print(ps_num)
5044: E6 53   ;   5     0   PrintScoreAndStop
5046: 00 00   ;   6     -   -
5048: BD 42   ;   7     1   StopIfPassElseContinue
504A: 64 54   ;   8     0   PrintScore
504C: 8C 55   ;   9     0   PrintScoreAndStop
504E: B5 52   ;  10     1   AssertRandomIsLessOrEqual
5050: 08 53   ;  11     1   DropObject(obj_num) ?? Command B (NEVER USED ??)
5052: CF 52   ;  12     1   MoveToRoomIfItWasLastRoom(room_num) (NEVER USED)
5054: 98 52   ;  13     0   AssertPackIsEmptyExceptForEmerald
5056: 1E 53   ;  14     0   MoveToLastRoom
5058: 38 53   ;  15     0   PrintInventory
505A: 78 53   ;  16     0   PrintRoomDescription
505C: 7E 53   ;  17     1   AssertObjectMatchesUserInput(obj_num)
505E: 8C 53   ;  18     1   GetObjectFromRoom(obj_num)
5060: 00 00   ;  19     -   -
5062: C8 53   ;  20     0   PrintOK
5064: D1 53   ;  21     2   MoveObjectToRoom(obj_num,room_num)
5066: E0 52   ;  22     0   GetUserInputObject
5068: C1 53   ;  23     0   DropUserInputObject
506A: 42 52   ;  24     1   MoveObjectToCurrentRoom(obj_num)
506C: 50 52   ;  25     2   MoveObjectIntoContainer(obj_num,obj_num)
506E: 87 52   ;  26     1   AssertObjectIsInCurrentRoom(obj_num)
5070: 92 55   ;  27     0   LoadGame
5072: C6 55   ;  28     0   SaveGame
5074: E8 55   ;  29     0   RandomizeDirections
```

# After Every Step

```code
; This processing takes place after every user input.[[br]]
;  1. Increment the count on the lamp and the number of turns.[[br]]
;  2.  Warn the player if the lamp is going dim and change the batteries automatically.
AfterEveryStep:
5076: 3E 0F           LD      A,$0F               ; obj_LAMP_on
5078: 21 84 4F        LD      HL,$4F84            ; {+code.ObjectData} Object table
507B: CD 5C 42        CALL    $425C               ; {code.TableOffsetTwoBytes} Lookup the object info
507E: 23              INC     HL                  ; Location
507F: 7E              LD      A,(HL)              ; Is the ...
5080: A7              AND     A                   ; ... lamp turned on?
5081: CA D1 50        JP      Z,$50D1             ; {code.CheckAutoBatteries} No, bump BCD turn count and out
5084: 2A DF 4F        LD      HL,($4FDF)          ; {code.lampOnTurnCount} Bump ...
5087: 23              INC     HL                  ; ... turns the lamp ...
5088: 22 DF 4F        LD      ($4FDF),HL          ; {code.lampOnTurnCount} ... has been on
508B: 7C              LD      A,H                 ; Has lamp been ...
508C: FE 01           CP      $01                 ; ... on 256 turns or more?
508E: C2 D1 50        JP      NZ,$50D1            ; {code.CheckAutoBatteries} No, bump BCD turn count and out
5091: 7D              LD      A,L                 ; Has lamp been lit ...
5092: FE 22           CP      $22                 ; ... exactly 256+34 = 290 turns?
5094: C2 A0 50        JP      NZ,$50A0            ; {} No, skip message
5097: 21 19 79        LD      HL,$7919            ; {+code.PS_A6} "YOUR_LAMP_IS_GETTING_DIM."
509A: CD A9 44        CALL    $44A9               ; {code.PrintPacked} Print message
509D: C3 14 51        JP      $5114               ; {code.BumpBCDTurnCount} Bump BCD turn count and out
50A0: FE 36           CP      $36                 ; Has lamp been lit 256+54 = 310 turns?
50A2: C2 D1 50        JP      NZ,$50D1            ; {code.CheckAutoBatteries} No, bump BCD turn count and out
50A5: 3E 0F           LD      A,$0F               ; obj_LAMP_on
50A7: 21 84 4F        LD      HL,$4F84            ; {+code.ObjectData} Object table
50AA: CD 5C 42        CALL    $425C               ; {code.TableOffsetTwoBytes} Look up the object info
50AD: 23              INC     HL                  ; Point to location
50AE: 46              LD      B,(HL)              ; Current location of the obj_LAMP_on
50AF: 36 00           LD      (HL),$00            ; The obj_LAMP_on is now out of play
50B1: 21 84 4F        LD      HL,$4F84            ; {+code.ObjectData} Look up ...
50B4: 3E 2C           LD      A,$2C               ; ... info for ...
50B6: CD 5C 42        CALL    $425C               ; {code.TableOffsetTwoBytes} ... obj_LAMP_dead
50B9: 23              INC     HL                  ; Location
50BA: 70              LD      (HL),B              ; Replace the obj_LAMP_on with obj_LAMP_dead
50BB: 3E 23           LD      A,$23               ; obj_BATTERIES_fresh
50BD: 1E FF           LD      E,$FF               ; Fresh batteries in ...
50BF: CD 4B 42        CALL    $424B               ; {code.GetObjectInfo} ... backpack?
50C2: CA D1 50        JP      Z,$50D1             ; {code.CheckAutoBatteries} Yes, automatically replace them
50C5: 21 9E 79        LD      HL,$799E            ; {+code.PS_A7} "YOUR_LAMP_HAS_RUN_OUT_OF_POWER.[CR]"
50C8: CD A9 44        CALL    $44A9               ; {code.PrintPacked} Print the message
50CB: CD E2 51        CALL    $51E2               ; {code.DescribeRoom} Describe the dark room
50CE: C3 14 51        JP      $5114               ; {code.BumpBCDTurnCount} Bump the BCD turn count and out
;
CheckAutoBatteries:
50D1: 2A DF 4F        LD      HL,($4FDF)          ; {code.lampOnTurnCount} Get the turns the lamp has been on
50D4: 11 2C 01        LD      DE,$012C            ; Match 300 turns
50D7: 7C              LD      A,H                 ; Has lamp been on ...
50D8: BA              CP      D                   ; ... 300 turns?
50D9: DA 14 51        JP      C,$5114             ; {code.BumpBCDTurnCount} No, bump the BCD turn count and out
50DC: 7D              LD      A,L                 ; Has lamp been on ...
50DD: BB              CP      E                   ; ... 300 turns?
50DE: DA 14 51        JP      C,$5114             ; {code.BumpBCDTurnCount} No, bump the BCD turn count and out
50E1: 3E 23           LD      A,$23               ; Are the ...
50E3: 1E FF           LD      E,$FF               ; obj_BATTERIES_fresh ...
50E5: CD 4B 42        CALL    $424B               ; {code.GetObjectInfo} ... in the backpack?
50E8: C2 14 51        JP      NZ,$5114            ; {code.BumpBCDTurnCount} No, bump the BCD turn count and out
50EB: 3E 2C           LD      A,$2C               ; Is the ...
50ED: 1E FF           LD      E,$FF               ; ... obj_LAMP_dead ...
50EF: CD 4B 42        CALL    $424B               ; {code.GetObjectInfo} ... in the backpack?
50F2: C2 14 51        JP      NZ,$5114            ; {code.BumpBCDTurnCount} No, bump the BCD turn count and out
50F5: 23              INC     HL                  ; The obj_LAMP_dead ...
50F6: 36 00           LD      (HL),$00            ; ... is now out of play
50F8: 3E 23           LD      A,$23               ; Get the ...
50FA: 21 84 4F        LD      HL,$4F84            ; {+code.ObjectData} ... info for ...
50FD: CD 5C 42        CALL    $425C               ; {code.TableOffsetTwoBytes} ... obj_BATTERIES_fresh
5100: 23              INC     HL                  ; Fresh batteries ...
5101: 36 00           LD      (HL),$00            ; ... are now out of play
5103: 23              INC     HL                  ; Bump to ...
5104: 23              INC     HL                  ; ... obj_BATTERIES_worn
5105: 36 FF           LD      (HL),$FF            ; Worn out batteries are now ...
5107: 1E FF           LD      E,$FF               ; ... in the backpack
5109: 3E 0F           LD      A,$0F               ; obj_LAMP_on
510B: CD 71 42        CALL    $4271               ; {code.SetObjectLocation} Move the obj_LAMP_on to the backpack
510E: 21 E5 79        LD      HL,$79E5            ; {+code.PS_A9} "REPLACING__THE_BATTERIES.[CR]"
5111: CD A9 44        CALL    $44A9               ; {code.PrintPacked} Print message
;
BumpBCDTurnCount:
5114: 3A DD 4F        LD      A,($4FDD)           ; {code.bcdTurnCountLSB} Get the lower BCD turn count
5117: C6 01           ADD     $01                 ; Add one to ...
5119: 27              DAA                         ; ... BCD value
511A: 32 DD 4F        LD      ($4FDD),A           ; {code.bcdTurnCountLSB} Store new BCD value
511D: 3A DE 4F        LD      A,($4FDE)           ; {code.bcdTurnCountMSB} Get the upper BCD turn count
5120: CE 00           ADC     $00                 ; Add any ...
5122: 27              DAA                         ; ... carry from lower
5123: 32 DE 4F        LD      ($4FDE),A           ; {code.bcdTurnCountMSB} Update upper BCD count
5126: C9              RET                         
```

# Command 1: MoveToRoom

This routine moves the player to a new room. If there is light in the new room or light
in the old room then the move always works. Otherwise there is a 60% chance the move kills you.

If there is light in the new room then the room description is printed.

After every move the code checks the pack for treasures. If there are 2 or more treasures then
the Mummy moves them all to room 53 (the hard-to-find room in the maze). Then the code moves the
chest to room 53. Up till now the chest has been in room 0 (out of play). The only way to make the
chest appear in the maze is to encounter the mummy. Once the chest is in a room (any room) the 
mummy no longer appears. You only see the mummy once.

The mummy says he is going to take the treasures and "PUT_THEM_IN_THE_CHEST_DEEP_IN_THE_MAZE!".
But he only puts them in the same room -- not actually in the chest. The code does not utilize
the container relationship.

```code
MoveToRoom:
5127: E1              POP     HL                  ; Get the ...
5128: 46              LD      B,(HL)              ; ... target room number
5129: 23              INC     HL                  ; Next byte
512A: E5              PUSH    HL                  ; Update script pointer
512B: 3A DC 4F        LD      A,($4FDC)           ; {ram.CurrentRoom} Checking ...
512E: 5F              LD      E,A                 ; ... current room
512F: 3E 0F           LD      A,$0F               ; obj_LAMP_on
5131: CD 4B 42        CALL    $424B               ; {code.GetObjectInfo} Is the lit-lamp in this room?
5134: CA 77 51        JP      Z,$5177             ; {} Yes, there is light. Make the move.
5137: 1E FF           LD      E,$FF               ; Backpack room number
5139: 3E 0F           LD      A,$0F               ; obj_LAMP_on
513B: CD 4B 42        CALL    $424B               ; {code.GetObjectInfo} Is the lit-lamp in the backpack?
513E: CA 77 51        JP      Z,$5177             ; {} Yes, there is light. Make the move.
5141: 21 E2 4E        LD      HL,$4EE2            ; {+code.AmbientLightTable} Ambient light table
5144: 3A DC 4F        LD      A,($4FDC)           ; {ram.CurrentRoom} Get the light setting ...
5147: CD 5C 42        CALL    $425C               ; {code.TableOffsetTwoBytes} ... for the current room
514A: 7E              LD      A,(HL)              ; Get the ambient light level of the room
514B: E6 40           AND     $40                 ; Check the bit
514D: C2 77 51        JP      NZ,$5177            ; {} There is light in the current room. Make the move.
5150: 78              LD      A,B                 ; Room we are moving to
5151: 21 E2 4E        LD      HL,$4EE2            ; {+code.AmbientLightTable} Ambient light table
5154: CD 5C 42        CALL    $425C               ; {code.TableOffsetTwoBytes} Get the light setting ...
5157: 7E              LD      A,(HL)              ; ... for the destination room
5158: E6 40           AND     $40                 ; Check the bit
515A: C2 77 51        JP      NZ,$5177            ; {} There is light in the next room. Make the move.
515D: 58              LD      E,B                 ; Destination room
515E: 3E 0F           LD      A,$0F               ; obj_LAMP_on
5160: CD 4B 42        CALL    $424B               ; {code.GetObjectInfo} Is the lit-lamp in the next room?
5163: CA 77 51        JP      Z,$5177             ; {} Yes, there is light. Make the move.
5166: 3A 11 47        LD      A,($4711)           ; {code.keyWaitCounter} Random number (key-input wait counter)
5169: FE 67           CP      $67                 ; random(255) < 103? That's 40% of the time.
516B: DA 77 51        JP      C,$5177             ; {} Yes, we were lucky. Make the move.
516E: 21 58 78        LD      HL,$7858            ; {+code.PS_A1} "YOU_FELL_INTO_A_PIT_AND_BROKE_EVERY_BONE_IN_YOUR_BODY. [CR]"
5171: CD A9 44        CALL    $44A9               ; {code.PrintPacked} Print message
5174: C3 E6 53        JP      $53E6               ; {code.PlayerDied} The player died. Resurrect the player.
;
5177: 3A DC 4F        LD      A,($4FDC)           ; {ram.CurrentRoom} Copy current room number ...
517A: 32 E1 4F        LD      ($4FE1),A           ; {code.lastRoom} ... to last room number
517D: 78              LD      A,B                 ; Move player to ...
517E: 32 DC 4F        LD      ($4FDC),A           ; {ram.CurrentRoom} ... current room
5181: CD E2 51        CALL    $51E2               ; {code.DescribeRoom} Print room and room description (with objects)
5184: 3E 2A           LD      A,$2A               ; obj_CHEST
5186: 21 84 4F        LD      HL,$4F84            ; {+code.ObjectData} object info
5189: CD 5C 42        CALL    $425C               ; {code.TableOffsetTwoBytes} Look up the info on the chest
518C: 23              INC     HL                  ; Get the ...
518D: 7E              LD      A,(HL)              ; ... room number of the chest
518E: A7              AND     A                   ; Has the chest been placed in the maze?
518F: C2 DF 51        JP      NZ,$51DF            ; {} Yes, skip themMummy
;
5192: 21 84 4F        LD      HL,$4F84            ; {+code.ObjectData} object info
5195: 0E 2C           LD      C,$2C               ; 44 objects total
5197: 06 00           LD      B,$00               ; Count number of treasures
5199: 7E              LD      A,(HL)              ; Attribute of object
519A: E6 20           AND     $20                 ; Is object a treasure?
519C: 23              INC     HL                  ; Point to 2nd entry
519D: CA A7 51        JP      Z,$51A7             ; {} Not an object, move to next object
51A0: 7E              LD      A,(HL)              ; Is the object ...
51A1: FE FF           CP      $FF                 ; ... in the backpack?
51A3: C2 A7 51        JP      NZ,$51A7            ; {} No, move to next object
51A6: 04              INC     B                   ; Bump the treasure count
51A7: 23              INC     HL                  ; Next object
51A8: 0D              DEC     C                   ; All objects checked?
51A9: C2 99 51        JP      NZ,$5199            ; {} No, go back for all of them
;
51AC: 78              LD      A,B                 ; Two (or more) treasures ...
51AD: FE 02           CP      $02                 ; ... in the backpack?
51AF: DA DF 51        JP      C,$51DF             ; {} No, skip the mummy
;
51B2: 21 84 4F        LD      HL,$4F84            ; {+code.ObjectData} Object info
51B5: 0E 2C           LD      C,$2C               ; 44 objects to check
51B7: 7E              LD      A,(HL)              ; Get the object attribute
51B8: E6 20           AND     $20                 ; Is the object treasure?
51BA: 23              INC     HL                  ; Next byte in entry
51BB: CA CD 51        JP      Z,$51CD             ; {} Not a treasure, move to next object
51BE: 7E              LD      A,(HL)              ; Get the object location
51BF: FE FF           CP      $FF                 ; In the backpack?
51C1: C2 CD 51        JP      NZ,$51CD            ; {} Not in the backpack, move to next object
51C4: 36 35           LD      (HL),$35            ; Move the object to the treasure room in the maze
51C6: 3A E2 4F        LD      A,($4FE2)           ; {code.numObjInPack} Number of objects in pack
51C9: 3D              DEC     A                   ; No longer carying ...
51CA: 32 E2 4F        LD      ($4FE2),A           ; {code.numObjInPack} ... this object
51CD: 23              INC     HL                  ; Next object
51CE: 0D              DEC     C                   ; Have we checked all objects?
51CF: C2 B7 51        JP      NZ,$51B7            ; {} No, go back for them all
51D2: 1E 35           LD      E,$35               ; room_53 in the maze
51D4: 3E 2A           LD      A,$2A               ; obj_CHEST
51D6: CD 71 42        CALL    $4271               ; {code.SetObjectLocation} Place the chest in the maze
51D9: 21 A0 7A        LD      HL,$7AA0            ; {+code.PS_AD} "_____SUDDENLY,_A_MUMMY_CREEPS_UP_BEHIND_YOU!!"
51DC: CD A9 44        CALL    $44A9               ; {code.PrintPacked} Print the message
;
51DF: C3 A6 42        JP      $42A6               ; {code.ScriptCommandPASS} Move passed. Continue the script.

DescribeRoom:
51E2: 3A DC 4F        LD      A,($4FDC)           ; {ram.CurrentRoom} Get the current room number
51E5: 21 E2 4E        LD      HL,$4EE2            ; {+code.AmbientLightTable} Ambient light table
51E8: CD 5C 42        CALL    $425C               ; {code.TableOffsetTwoBytes} Look up the lighting info
51EB: 7E              LD      A,(HL)              ; Is there ...
51EC: E6 40           AND     $40                 ; ... natural light?
51EE: C2 0E 52        JP      NZ,$520E            ; {} Yes, show the room description
51F1: 3A DC 4F        LD      A,($4FDC)           ; {ram.CurrentRoom} Get the current room number
51F4: 5F              LD      E,A                 ; Is the ...
51F5: 3E 0F           LD      A,$0F               ; ... obj_LAMP_ON ...
51F7: CD 4B 42        CALL    $424B               ; {code.GetObjectInfo} ... in the current room?
51FA: CA 0E 52        JP      Z,$520E             ; {} Yes, there is light. Show the room description
51FD: 1E FF           LD      E,$FF               ; Is the ...
51FF: 3E 0F           LD      A,$0F               ; ... obj_LAMP_ON ...
5201: CD 4B 42        CALL    $424B               ; {code.GetObjectInfo} ... in the backpack?
5204: CA 0E 52        JP      Z,$520E             ; {} Yes, there is light. Show the room description
5207: 21 CA 78        LD      HL,$78CA            ; {+code.PS_A4} "IT_IS_NOW_PITCH_DARK.__IF_YOU_PROCEED,_YOU_"
520A: CD A9 44        CALL    $44A9               ; {code.PrintPacked} Print the warning
520D: C9              RET                         ; Out
;
520E: 3A DC 4F        LD      A,($4FDC)           ; {ram.CurrentRoom} Get the current room number
5211: 21 25 48        LD      HL,$4825            ; {+code.RoomTable} Room info table
5214: CD 66 42        CALL    $4266               ; {code.TableOffsetFourBytes} Look up 4-byte entry
5217: 7E              LD      A,(HL)              ; Get the description LSB
5218: 23              INC     HL                  ; Next byte
5219: 66              LD      H,(HL)              ; Get the dscription MSB
521A: 6F              LD      L,A                 ; Move description LSB to HL
521B: CD A9 44        CALL    $44A9               ; {code.PrintPacked} Print the room description
;
521E: 06 00           LD      B,$00               ; Object number (counting up from 1 to 44)
5220: 04              INC     B                   ; Checking this object number
5221: 3A DC 4F        LD      A,($4FDC)           ; {ram.CurrentRoom} Checking ...
5224: 5F              LD      E,A                 ; ... current room
5225: 78              LD      A,B                 ; Have we checked ...
5226: FE 2D           CP      $2D                 ; ... all objects?
5228: D0              RET     NC                  ; Yes, done
;
5229: CD 4B 42        CALL    $424B               ; {code.GetObjectInfo} Get the info about the object
522C: C2 20 52        JP      NZ,$5220            ; {} Ignore object if it isn't in the current room
522F: 78              LD      A,B                 ; Object number
5230: 21 E4 4F        LD      HL,$4FE4            ; {+code.ObjectDescriptions} Object description table
5233: CD 5C 42        CALL    $425C               ; {code.TableOffsetTwoBytes} Look up the object's description
5236: 7E              LD      A,(HL)              ; Get the LSB
5237: 23              INC     HL                  ; Next byte of pointer
5238: 66              LD      H,(HL)              ; Get the description MSB
5239: 6F              LD      L,A                 ; Description pointer now in HL
523A: C5              PUSH    BC                  ; Hold our object count
523B: CD A9 44        CALL    $44A9               ; {code.PrintPacked} Print the object's long description
523E: C1              POP     BC                  ; Restore the object count
523F: C3 20 52        JP      $5220               ; {} Go back for all objects
```

# Command 24: MoveObjectToCurrentRoom

```code
MoveObjectToCurrentRoom:
5242: E1              POP     HL                  ; Get script pointer
5243: 3A DC 4F        LD      A,($4FDC)           ; {ram.CurrentRoom} Get current room
5246: 5F              LD      E,A                 ; Object destination
5247: 7E              LD      A,(HL)              ; Object number from script
5248: 23              INC     HL                  ; Update ...
5249: E5              PUSH    HL                  ; ... the script pointer
524A: CD 71 42        CALL    $4271               ; {code.SetObjectLocation} Move the object
524D: C3 A6 42        JP      $42A6               ; {code.ScriptCommandPASS} Command passes
```

# Command 25: MoveObjectIntoContainer

```code
MoveObjectIntoContainer:
5250: E1              POP     HL                  ; Get script pointer
5251: 7E              LD      A,(HL)              ; Get object number from script
5252: 23              INC     HL                  ; Next byte in script
5253: 46              LD      B,(HL)              ; Get the destination object number from script
5254: 23              INC     HL                  ; Update ...
5255: E5              PUSH    HL                  ; ... the script pointer
5256: 21 84 4F        LD      HL,$4F84            ; {+code.ObjectData} Lookup the ...
5259: CD 5C 42        CALL    $425C               ; {code.TableOffsetTwoBytes} ... target object
525C: 7E              LD      A,(HL)              ; Set ...
525D: F6 80           OR      $80                 ; ... the "is carried" ...
525F: 77              LD      (HL),A              ; ... flag on the target object
5260: 23              INC     HL                  ; Being carried by ...
5261: 70              LD      (HL),B              ; ... container
5262: C3 C8 53        JP      $53C8               ; {code.PrintOK} Print OK and command passes
```

# Command 2: AssertObjectIsInPack

This command checks if the requested object is in the backpack.

```code
AssertObjectIsInPack:
5265: E1              POP     HL                  ; Get the next ...
5266: 7E              LD      A,(HL)              ; ... byte from ...
5267: 23              INC     HL                  ; ... the script
5268: E5              PUSH    HL                  ; Update the script pointer
5269: 1E FF           LD      E,$FF               ; Room location of pack
526B: CD 4B 42        CALL    $424B               ; {code.GetObjectInfo} Find the object. Is it in the pack (at E)?
526E: CA A6 42        JP      Z,$42A6             ; {code.ScriptCommandPASS} Yes, command passes
5271: C3 B9 42        JP      $42B9               ; {code.ScriptCommandFAIL} No, command fails
```

# Command 3: AssertObjectIsInCurrentRoomOrPack

This command checks if the requested object is accessible (current room
or backpack).

```code
AssertObjectIsInCurrentRoomOrPack:
5274: E1              POP     HL                  ; Get the next ...
5275: 46              LD      B,(HL)              ; ... byte from ...
5276: 23              INC     HL                  ; ... the script
5277: E5              PUSH    HL                  ; Update the script pointer
5278: 3A DC 4F        LD      A,($4FDC)           ; {ram.CurrentRoom} Current room number
527B: 5F              LD      E,A                 ; Check for current room
527C: 78              LD      A,B                 ; Requested object number
527D: CD 4B 42        CALL    $424B               ; {code.GetObjectInfo} Get the info about the object
5280: CA A6 42        JP      Z,$42A6             ; {code.ScriptCommandPASS} It is in the room. Return SUCCESS
5283: 78              LD      A,B                 ; Object number
5284: C3 69 52        JP      $5269               ; {} Check the backpack for the object
```

# Command 26: AssertObjectIsInCurrentRoom

This command checks if the request object (or object's top level container) is in
the current room.

```code
AssertObjectIsInCurrentRoom:
5287: E1              POP     HL                  ; Get the script pointer
5288: 3A DC 4F        LD      A,($4FDC)           ; {ram.CurrentRoom} Checking ...
528B: 5F              LD      E,A                 ; ... current room
528C: 7E              LD      A,(HL)              ; Requested object number
528D: 23              INC     HL                  ; Update ...
528E: E5              PUSH    HL                  ; ... script pointer
528F: CD 4B 42        CALL    $424B               ; {code.GetObjectInfo} Get the info about the object
5292: CA A6 42        JP      Z,$42A6             ; {code.ScriptCommandPASS} Success if parent container is in the current room
5295: C3 B9 42        JP      $42B9               ; {code.ScriptCommandFAIL} Otherwise the command fails
```

# Command 13: AssertPackIsEmptyExceptForEmerald

This very specific command checks if the backpack is empty or has just the emerald. This is
used in the script for room_73, the "TIGHT_SQUEEZE" from the "CHAMBER_OF_THE_HIGH_PRIEST".

```code
AssertPackIsEmptyExceptForEmerald:
5298: 21 84 4F        LD      HL,$4F84            ; {+code.ObjectData}
529B: 0E 01           LD      C,$01               ; Start checking with object 1
529D: 23              INC     HL                  ; Location of object
529E: 79              LD      A,C                 ; Is this object ...
529F: FE 1F           CP      $1F                 ; ... the obj_EMERALD?
52A1: CA AA 52        JP      Z,$52AA             ; {} Yes, ignore it
52A4: 7E              LD      A,(HL)              ; Get the location
52A5: FE FF           CP      $FF                 ; Is this object in the backpack?
52A7: CA B9 42        JP      Z,$42B9             ; {code.ScriptCommandFAIL} Yes, fail
52AA: 23              INC     HL                  ; Next object data
52AB: 0C              INC     C                   ; Next object number
52AC: 79              LD      A,C                 ; Past the ...
52AD: FE 2D           CP      $2D                 ; ... last object?
52AF: C2 9D 52        JP      NZ,$529D            ; {} No, keep checking
52B2: C3 A6 42        JP      $42A6               ; {code.ScriptCommandPASS} Success
```

# Command 10: AssertRandomIsLessOrEqual

This command is a very specific move command. If the random value is less than or equal to 
the given target value, then the player stays in the same room. The code prints the "crawled
around" message and reprints the current room description and the command returns success.
If the random value is greater than the given value, the command fails.

This script command is used in two rooms: room_65 (CHAMBER_OF_HORUS) and room_60 (LAND_OF_DEAD).
In all cases, it is wrapped in a "StopIfPassElseContinue" like this:

```
4DEE: 08 07     ; NW
4DF0: 07 03     ;    StopIfPassElseContinue
4DF2: 0A F0     ;        AssertRandomIsLessOrEqual(240)
4DF4: 01 3B     ;    MoveToRoom(room_59)
```

Most of the time (random values 0 through 240) the command passes and the player stays put.
But for values 241 through 255, the command fails and the player moves to room_59
(ANTEROOM_OF_SEKER).

```code
AssertRandomIsLessOrEqual:
52B5: E1              POP     HL                  ; Get target ...
52B6: 46              LD      B,(HL)              ; ... value from script
52B7: 23              INC     HL                  ; Update the ...
52B8: E5              PUSH    HL                  ; ... script pointer
52B9: 3A 11 47        LD      A,($4711)           ; {code.keyWaitCounter} Get the randomish number
52BC: B8              CP      B                   ; Compare with target value
52BD: CA C3 52        JP      Z,$52C3             ; {} The same means pass
52C0: D2 B9 42        JP      NC,$42B9            ; {code.ScriptCommandFAIL} Less than means pass
52C3: 21 E9 71        LD      HL,$71E9            ; {+code.PS_74} "WOUND_UP_BACK__IN_THE_MAIN_PASSAGE.[CR]"
52C6: CD A9 44        CALL    $44A9               ; {code.PrintPacked} Print message
52C9: CD E2 51        CALL    $51E2               ; {code.DescribeRoom} Reprint the current room description
52CC: C3 A6 42        JP      $42A6               ; {code.ScriptCommandPASS} Pass
```

# Command 12: MoveToRoomIfItWasLastRoom (UNUSED)

This command moves the player to the target room but only if the target room was the last room.

If the target room is not the last room, the command fails.

This command is not used in any script.

```code
MoveToRoomIfItWasLastRoom:
52CF: E1              POP     HL                  ; Get destination ...
52D0: 46              LD      B,(HL)              ; ... room
52D1: 23              INC     HL                  ; Update the ...
52D2: E5              PUSH    HL                  ; ... script pointer
52D3: 3A E1 4F        LD      A,($4FE1)           ; {code.lastRoom} Get the last room
52D6: B8              CP      B                   ; Is target room the last room?
52D7: C2 B9 42        JP      NZ,$42B9            ; {code.ScriptCommandFAIL} No, reject the move (fail)
52DA: E1              POP     HL                  ; Back the script ...
52DB: 2B              DEC     HL                  ; ... pointer up so we ...
52DC: E5              PUSH    HL                  ; ... can call MoveToRoom
52DD: C3 27 51        JP      $5127               ; {code.MoveToRoom} Normal move to room (with lighting checks)
```

# Command 22: GetUserInputObject

```code
GetUserInputObject:
52E0: 3A 18 46        LD      A,($4618)           ; {code.noun} Get the object number the player requested
52E3: 1E FF           LD      E,$FF               ; Get the ...
52E5: CD 4B 42        CALL    $424B               ; {code.GetObjectInfo} ... target object's info
52E8: C2 F4 52        JP      NZ,$52F4            ; {} It isn't in the backpack. No error here.
52EB: 21 B4 74        LD      HL,$74B4            ; {+code.PS_87} "YOU_ARE_ALREADY_CARRYING_IT.[CR]"
52EE: CD A9 44        CALL    $44A9               ; {code.PrintPacked} Print the error
52F1: C3 A6 42        JP      $42A6               ; {code.ScriptCommandPASS} Success (the object is in backpack as requested!)
;
52F4: 3A 18 46        LD      A,($4618)           ; {code.noun} Get the input noun again
52F7: 47              LD      B,A                 ; Handle the actual ...
52F8: C3 91 53        JP      $5391               ; {code.GetToBackpack} ... GET operation
```

# Command 4: Print

This command unpacks a string and prints it. This command always succeeds.

```code
Print:
52FB: E1              POP     HL                  ; Get the script pointer
52FC: 5E              LD      E,(HL)              ; Get the LSB of the string
52FD: 23              INC     HL                  ; Next in script
52FE: 56              LD      D,(HL)              ; Get the MSB of the string
52FF: 23              INC     HL                  ; Update the ...
5300: E5              PUSH    HL                  ; ... script pointer
5301: EB              EX      DE,HL               ; String pointer now in HL
5302: CD A9 44        CALL    $44A9               ; {code.PrintPacked} Print the packed string
5305: C3 A6 42        JP      $42A6               ; {code.ScriptCommandPASS} Printing is always a success
```

# Command 11: DropObject (UNUSED)

```code
DropObject:
5308: E1              POP     HL                  ; Get the target ...
5309: 46              LD      B,(HL)              ; ... object from the script
530A: 23              INC     HL                  ; Update the ...
530B: E5              PUSH    HL                  ; ... script pointer
530C: 3A E2 4F        LD      A,($4FE2)           ; {code.numObjInPack} Decrease ...
530F: 3D              DEC     A                   ; ... number of objects ...
5310: 32 E2 4F        LD      ($4FE2),A           ; {code.numObjInPack} ... in pack
5313: 3A DC 4F        LD      A,($4FDC)           ; {ram.CurrentRoom} Current room
5316: 5F              LD      E,A                 ; Move ...
5317: 78              LD      A,B                 ; ... object to ...
5318: CD 71 42        CALL    $4271               ; {code.SetObjectLocation} ... current room
531B: C3 C8 53        JP      $53C8               ; {code.PrintOK} Print OK and command passes
```

# Command 14: MoveToLastRoom

This command is only used by the "BACK" command to return the player to the last room.

This command always passes but prints a message if there was no last room.

```code
531E: 3A E1 4F        LD      A,($4FE1)           ; {code.lastRoom} Was there ...
5321: A7              AND     A                   ; ... a last room?
5322: CA 2F 53        JP      Z,$532F             ; {} No, print error and pass
5325: 47              LD      B,A                 ; Hold last room
5326: 3A DC 4F        LD      A,($4FDC)           ; {ram.CurrentRoom} Current room ...
5329: 32 E1 4F        LD      ($4FE1),A           ; {code.lastRoom} ... to last room
532C: C3 7D 51        JP      $517D               ; {} Continue with MoveToRoom logic (lighting, mummy, etc)
;
532F: 21 87 74        LD      HL,$7487            ; {+code.PS_86} "SORRY,_BUT_I_NO_LONGER_SEEM_TO_REMEMBER_HOW_IT_WAS_YOU_GOT_HERE.[CR]"
5332: CD A9 44        CALL    $44A9               ; {code.PrintPacked} Print string
5335: C3 A6 42        JP      $42A6               ; {code.ScriptCommandPASS} Command passes
```

# Command 15: PrintInventory

```code
PrintInventory:
5338: 3A E2 4F        LD      A,($4FE2)           ; {code.numObjInPack} Is there anything in ...
533B: A7              AND     A                   ; ... the backpack?
533C: C2 48 53        JP      NZ,$5348            ; {} Yes, go list the contents
;
533F: 21 FA 74        LD      HL,$74FA            ; {+code.PS_89} "YOU'RE_NOT_CARRYING_ANYTHING.[CR]"
5342: CD A9 44        CALL    $44A9               ; {code.PrintPacked} Print the message
5345: C3 A6 42        JP      $42A6               ; {code.ScriptCommandPASS} Command passes
;
5348: 21 10 75        LD      HL,$7510            ; {+code.PS_8A} "YOU_ARE_CURRENTLY_HOLDING_THE_FOLLOWING:[CR]"
534B: CD A9 44        CALL    $44A9               ; {code.PrintPacked} Print the banner
534E: 06 00           LD      B,$00               ; Object number through loop
5350: 1E FF           LD      E,$FF               ; Backpack room number
5352: 04              INC     B                   ; Next (or first) object number
5353: 78              LD      A,B                 ; Have we checked ...
5354: FE 2D           CP      $2D                 ; ... all objects?
5356: D2 A6 42        JP      NC,$42A6            ; {code.ScriptCommandPASS} Yes, command passes
;
5359: CD 4B 42        CALL    $424B               ; {code.GetObjectInfo} Get the object info
535C: C2 50 53        JP      NZ,$5350            ; {} Object is not in backpack, move to next object
535F: 78              LD      A,B                 ; Object number
5360: 21 E4 4F        LD      HL,$4FE4            ; {+code.ObjectDescriptions} Object info table
5363: CD 5C 42        CALL    $425C               ; {code.TableOffsetTwoBytes} Look up the description
5366: 7E              LD      A,(HL)              ; Description LSB
5367: 23              INC     HL                  ; Next entry
5368: 66              LD      H,(HL)              ; Description MSB
5369: 6F              LD      L,A                 ; HL now points to long description
536A: 7E              LD      A,(HL)              ; Skip ...
536B: 23              INC     HL                  ; ... to ...
536C: A7              AND     A                   ; ... short ...
536D: C2 6A 53        JP      NZ,$536A            ; {} ... description
5370: C5              PUSH    BC                  ; Hold our counter
5371: CD A9 44        CALL    $44A9               ; {code.PrintPacked} Print the short description
5374: C1              POP     BC                  ; Restore the counter
5375: C3 50 53        JP      $5350               ; {} Check all objects
```

# Command 16: PrintRoomDescription

```code
PrintRoomDescription:
5378: CD E2 51        CALL    $51E2               ; {code.DescribeRoom} Print the room description (with objects)
537B: C3 A6 42        JP      $42A6               ; {code.ScriptCommandPASS} Command passes
```

# Command 17: AssertObjectMatchesUserInput

```code
AssertObjectMatchesUserInput:
537E: E1              POP     HL                  ; Get the script pointer
537F: 46              LD      B,(HL)              ; Get the target object
5380: 23              INC     HL                  ; Update the ...
5381: E5              PUSH    HL                  ; ... script pointer
5382: 3A 18 46        LD      A,($4618)           ; {code.noun} Does user noun ...
5385: B8              CP      B                   ; ... match the target object?
5386: C2 B9 42        JP      NZ,$42B9            ; {code.ScriptCommandFAIL} No, command fails
5389: C3 A6 42        JP      $42A6               ; {code.ScriptCommandPASS} yes, command passes
```

# Command 18: GetObjectFromRoom

```code
GetObjectFromRoom:
538C: E1              POP     HL                  ; Get the script pointer
538D: 46              LD      B,(HL)              ; Get the object number
538E: 23              INC     HL                  ; Update ...
538F: E5              PUSH    HL                  ; ... script pointer
5390: 78              LD      A,B                 ; To parameter register
;
GetToBackpack:
5391: CD 4B 42        CALL    $424B               ; {code.GetObjectInfo} Look up the target object
5394: 7E              LD      A,(HL)              ; Is this object ...
5395: E6 40           AND     $40                 ; ... able to be picked up?
5397: C2 A3 53        JP      NZ,$53A3            ; {} Yes, skip the error
539A: 21 2D 75        LD      HL,$752D            ; {+code.PS_8B} "DON'T_BE_RIDICULOUS![CR]"
539D: CD A9 44        CALL    $44A9               ; {code.PrintPacked} Print the message
53A0: C3 A6 42        JP      $42A6               ; {code.ScriptCommandPASS} Command passes
;
53A3: 3A E2 4F        LD      A,($4FE2)           ; {code.numObjInPack} Get number of objects in pack
53A6: FE 08           CP      $08                 ; Eight is our max
53A8: DA B4 53        JP      C,$53B4             ; {} We have room for another, go get it
53AB: 21 C9 74        LD      HL,$74C9            ; {+code.PS_88} "YOU_CAN'T_CARRY_ANYTHING_MORE."
53AE: CD A9 44        CALL    $44A9               ; {code.PrintPacked} Print the message
53B1: C3 A6 42        JP      $42A6               ; {code.ScriptCommandPASS} Command passes
;
53B4: 3C              INC     A                   ; Add one ...
53B5: 32 E2 4F        LD      ($4FE2),A           ; {code.numObjInPack} ... to pack count
53B8: 78              LD      A,B                 ; Object number
53B9: 1E FF           LD      E,$FF               ; Backpack location
53BB: CD 71 42        CALL    $4271               ; {code.SetObjectLocation} Move the object to the backpack
53BE: C3 C8 53        JP      $53C8               ; {code.PrintOK} Print OK and command passes
```

# Command 23: DropUserInputObject

```code
DropUserInputObject:
53C1: 3A 18 46        LD      A,($4618)           ; {code.noun} Get the player's ...
53C4: 47              LD      B,A                 ; ... noun input
53C5: C3 0C 53        JP      $530C               ; {} Continue with drop
```

# Command 20: PrintOK

```code
PrintOK:
53C8: 21 83 74        LD      HL,$7483            ; {+code.PS_85} "OK_[CR]"
53CB: CD A9 44        CALL    $44A9               ; {code.PrintPacked} Print string
53CE: C3 A6 42        JP      $42A6               ; {code.ScriptCommandPASS} Command passes
```

# Command 21: MoveObjectToRoom

```code
MoveObjectToRoom:
53D1: E1              POP     HL                  ; Get the script pointer
53D2: 7E              LD      A,(HL)              ; Get the object number
53D3: 23              INC     HL                  ; Next in script
53D4: 5E              LD      E,(HL)              ; Get the room number
53D5: 23              INC     HL                  ; Update the ...
53D6: E5              PUSH    HL                  ; ... script pointer
53D7: 21 84 4F        LD      HL,$4F84            ; {+code.ObjectData} Look up the ...
53DA: CD 5C 42        CALL    $425C               ; {code.TableOffsetTwoBytes} ... target object
53DD: 7E              LD      A,(HL)              ; Clear the ...
53DE: E6 7F           AND     $7F                 ; ... being-carried flag
53E0: 77              LD      (HL),A              ; Store the new attributes
53E1: 23              INC     HL                  ; Location entry
53E2: 73              LD      (HL),E              ; Object now in target room
53E3: C3 A6 42        JP      $42A6               ; {code.ScriptCommandPASS} Command passes

PlayerDied:
53E6: 3A E3 4F        LD      A,($4FE3)           ; {code.numResurrected} Number of resurrections
53E9: 3C              INC     A                   ; Add one ...
53EA: 32 E3 4F        LD      ($4FE3),A           ; {code.numResurrected} ... to the count
53ED: FE 03           CP      $03                 ; Third time (or more)?
53EF: D2 59 54        JP      NC,$5459            ; {code.ThirdResurrection} Yes, do the 3rd
53F2: FE 02           CP      $02                 ; 2nd time?
53F4: CA 4D 54        JP      Z,$544D             ; {code.SecondResurrection} Yes, do the 2nd
;
; First time we initialize the message pointer
53F7: 21 08 7E        LD      HL,$7E08            ; {+code.PS_BC} "ALL_RIGHT.__BUT_DON'T_BLAME_ME"
53FA: 22 62 54        LD      ($5462),HL          ; {code.NextResurrectMessage} Next resurrection message
53FD: 21 FE 7C        LD      HL,$7CFE            ; {+code.PS_B9} "YOU_SEEM_TO_HAVE_GOTTEN_YOURSELF_KILLED."
5400: CD A9 44        CALL    $44A9               ; {code.PrintPacked} Print the message
5403: CD E9 44        CALL    $44E9               ; {code.WaitForKey} Wait for the user
5406: FE 59           CP      $59                 ; Is it a "Y" for yes to continuing on?
5408: C2 8C 55        JP      NZ,$558C            ; {code.PrintScoreAndStop} No, print score and stop
540B: 2A 62 54        LD      HL,($5462)          ; {code.NextResurrectMessage} Print resurrection ...
540E: CD A9 44        CALL    $44A9               ; {code.PrintPacked} ... message
5411: 21 9F 4F        LD      HL,$4F9F            ; {+} obj_LAMP_off to ...
5414: 36 01           LD      (HL),$01            ; ... room_1
5416: 23              INC     HL                  ; Point to ...
5417: 23              INC     HL                  ; ... obj_LAMP_on
5418: 36 00           LD      (HL),$00            ; Move it out of play
541A: 21 84 4F        LD      HL,$4F84            ; {+code.ObjectData} Object data
541D: 3A DC 4F        LD      A,($4FDC)           ; {ram.CurrentRoom} Player's ...
5420: 47              LD      B,A                 ; ... current room
5421: 3E FF           LD      A,$FF               ; Backpack location
5423: 0E 2C           LD      C,$2C               ; 44 objects to check
;
5425: 23              INC     HL                  ; Next (or first) object
5426: BE              CP      (HL)                ; Is object in backpack
5427: C2 34 54        JP      NZ,$5434            ; {} No ... leave this object where it is
542A: 70              LD      (HL),B              ; Change backpack to current room
542B: 3A E2 4F        LD      A,($4FE2)           ; {code.numObjInPack} Decrement ...
542E: 3D              DEC     A                   ; ... count of objects ...
542F: 32 E2 4F        LD      ($4FE2),A           ; {code.numObjInPack} ... in pack
5432: 3E FF           LD      A,$FF               ; Retore backpack location (had to use A)
5434: 23              INC     HL                  ; Next object
5435: 0D              DEC     C                   ; All done?
5436: C2 25 54        JP      NZ,$5425            ; {} No, drop all objects in backpack
5439: 3E 02           LD      A,$02               ; Resurrect player ...
543B: 32 DC 4F        LD      ($4FDC),A           ; {ram.CurrentRoom} ... in the entrance (past the lamp at 1 ... sneaky)
543E: CD E2 51        CALL    $51E2               ; {code.DescribeRoom} Print the room description
5441: 31 5C 47        LD      SP,$475C            ; Reset the stack pointer
5444: 21 00 00        LD      HL,$0000            ; Reset the ...
5447: 22 DF 4F        LD      ($4FDF),HL          ; {code.lampOnTurnCount} ... lamp time (very generous)
544A: C3 14 42        JP      $4214               ; {code.GameLoop} Back to the top of the game loop

SecondResurrection:
544D: 21 A2 7E        LD      HL,$7EA2            ; {+code.PS_BD} Next resurrection ...
5450: 22 62 54        LD      ($5462),HL          ; {code.NextResurrectMessage} ... message "WHERE_DID_I_PUT_ORANGE_SMOKE"
5453: 21 71 7D        LD      HL,$7D71            ; {+code.PS_BA} "YOU_CLUMBSY_OAF,_YOU'VE_DONE_IT_AGAIN
5456: C3 00 54        JP      $5400               ; {} Print the message and ressurect

ThirdResurrection:
5459: 21 CD 7D        LD      HL,$7DCD            ; {+code.PS_BB} "HOW_CAN_I_REINCARNATE_YOU____WITHOUT_ORANGE_SMOKE?[CR]"
545C: CD A9 44        CALL    $44A9               ; {code.PrintPacked} Print message
545F: C3 8C 55        JP      $558C               ; {code.PrintScoreAndStop} All lives gone. Print score and stop.

NextResurrectMessage:
5462: 00 00

5464: CD 6A 54        CALL    $546A               ; {code.PrintScore} Print the score
5467: C3 A6 42        JP      $42A6               ; {code.ScriptCommandPASS} Command passes
```

# Command 8: PrintScore

```code
PrintScore:
546A: 21 00 00        LD      HL,$0000            ; Clear score tally
546D: 22 4F 55        LD      ($554F),HL          ; {code.scoreTempLSB}
5470: 21 E2 4E        LD      HL,$4EE2            ; {+code.AmbientLightTable}
5473: 0E 51           LD      C,$51               ; 81 rooms to check
5475: 7E              LD      A,(HL)              ; First byte
5476: E6 80           AND     $80                 ; Was something scored in this room?
5478: 23              INC     HL                  ; Next room
5479: CA 8D 54        JP      Z,$548D             ; {} No ... next room
547C: 3A 4F 55        LD      A,($554F)           ; {code.scoreTempLSB} BCD LSB
547F: 86              ADD     A,(HL)              ; Add in the score from the room
5480: 27              DAA                         ; Adjust for BCD
5481: 32 4F 55        LD      ($554F),A           ; {code.scoreTempLSB} Update LSB
5484: 3A 50 55        LD      A,($5550)           ; {code.scoreTempMSB} Carry into ...
5487: CE 00           ADC     $00                 ; ... the MSB
5489: 27              DAA                         ; Adjust for BCD
548A: 32 50 55        LD      ($5550),A           ; {code.scoreTempMSB} Update MSB
548D: 23              INC     HL                  ; Next room
548E: 0D              DEC     C                   ; All rooms checked?
548F: C2 75 54        JP      NZ,$5475            ; {} No ... check them all
;
5492: 21 84 4F        LD      HL,$4F84            ; {+code.ObjectData} Now check the objects
5495: 0E 2C           LD      C,$2C               ; 44 objects to check
5497: 7E              LD      A,(HL)              ; First byte of object
5498: E6 20           AND     $20                 ; Is this a treasure?
549A: 23              INC     HL                  ; Next in table
549B: CA BE 54        JP      Z,$54BE             ; {} Not a treasure, skip it
549E: 7E              LD      A,(HL)              ; Location of object
549F: FE 02           CP      $02                 ; Is this object (or parent container) in room 2?
54A1: 06 20           LD      B,$20               ; Score 20 points (BCD) if it is
54A3: CA AD 54        JP      Z,$54AD             ; {} It is in the target room ... go score it
54A6: FE FF           CP      $FF                 ; Is it in the backpack?
54A8: C2 BE 54        JP      NZ,$54BE            ; {} No, next object
54AB: 06 05           LD      B,$05               ; Score 5 points if the object is in the backpack
54AD: 3A 4F 55        LD      A,($554F)           ; {code.scoreTempLSB} BCD LSB
54B0: 80              ADD     A,B                 ; Add in score from the object
54B1: 27              DAA                         ; Adjust for BCD
54B2: 32 4F 55        LD      ($554F),A           ; {code.scoreTempLSB} Update LSB
54B5: 3A 50 55        LD      A,($5550)           ; {code.scoreTempMSB} Carry into ...
54B8: CE 00           ADC     $00                 ; ... the MSB
54BA: 27              DAA                         ; Adjust for BCD
54BB: 32 50 55        LD      ($5550),A           ; {code.scoreTempMSB} Update the MSB
;
54BE: 23              INC     HL                  ; Next in object table
54BF: 0D              DEC     C                   ; Have we processed all objects?
54C0: C2 97 54        JP      NZ,$5497            ; {} No, go check them all
;
54C3: 3A E3 4F        LD      A,($4FE3)           ; {code.numResurrected} Number of deaths
54C6: A7              AND     A                   ; No penalty if ...
54C7: CA E5 54        JP      Z,$54E5             ; {} ... we haven't died
54CA: 4F              LD      C,A                 ; Penalized 10 points for each death
54CB: 06 90           LD      B,$90               ; BCD value for "-10"
54CD: 3A 4F 55        LD      A,($554F)           ; {code.scoreTempLSB} LSB of score
54D0: 80              ADD     A,B                 ; Add penalty (negative)
54D1: 27              DAA                         ; Adjust for BCD
54D2: 32 4F 55        LD      ($554F),A           ; {code.scoreTempLSB} Update LSB
54D5: DA E1 54        JP      C,$54E1             ; {} No borrow ... move on
54D8: 3A 50 55        LD      A,($5550)           ; {code.scoreTempMSB} MSB of score
54DB: C6 99           ADD     $99                 ; BCD value for "-1" (borrow)
54DD: 27              DAA                         ; Adjust for BCD
54DE: 32 50 55        LD      ($5550),A           ; {code.scoreTempMSB} Update the MSB
54E1: 0D              DEC     C                   ; All deaths subtracted off?
54E2: C2 CD 54        JP      NZ,$54CD            ; {} No ... do them all
;
54E5: 3A 50 55        LD      A,($5550)           ; {code.scoreTempMSB} Is score ...
54E8: FE 90           CP      $90                 ; ... positive?
54EA: DA 15 55        JP      C,$5515             ; {} Yes ... print a space for the sign
54ED: 3E 2D           LD      A,$2D               ; Add a "-" to ...
54EF: 32 5C 55        LD      ($555C),A           ; {code.scoreSign} ... the score string
54F2: 3A 50 55        LD      A,($5550)           ; {code.scoreTempMSB}
54F5: 47              LD      B,A                 ; 
54F6: 3E 99           LD      A,$99               ; TODO decode the math
54F8: 90              SUB     B                   ; Negative values need fixing up to make them right
54F9: 32 50 55        LD      ($5550),A           ; {code.scoreTempMSB}
54FC: 3A 4F 55        LD      A,($554F)           ; {code.scoreTempLSB}
54FF: 47              LD      B,A                 ; 
5500: 3E 99           LD      A,$99               ; TODO BCD math for negatives
5502: 90              SUB     B                   ; 
5503: C6 01           ADD     $01                 ; 
5505: 27              DAA                         ; 
5506: 32 4F 55        LD      ($554F),A           ; {code.scoreTempLSB}
5509: 3A 50 55        LD      A,($5550)           ; {code.scoreTempMSB}
550C: CE 00           ADC     $00                 ; 
550E: 27              DAA                         ; 
550F: 32 50 55        LD      ($5550),A           ; {code.scoreTempMSB}
5512: C3 1A 55        JP      $551A               ; {} Now update the turns
;
5515: 3E 20           LD      A,$20               ; Space means "+" ...
5517: 32 5C 55        LD      ($555C),A           ; {code.scoreSign} ... in the score message
;
551A: 21 5D 55        LD      HL,$555D            ; {+code.scoreSpot} Turn count in the score message
551D: 3A 50 55        LD      A,($5550)           ; {code.scoreTempMSB} MSB of calculated score
5520: CD 3F 55        CALL    $553F               ; {code.BinaryToASCII} Add MSB of score to string
5523: 3A 4F 55        LD      A,($554F)           ; {code.scoreTempLSB} LSB of calculated score
5526: CD 3F 55        CALL    $553F               ; {code.BinaryToASCII} Add LSB of score to string
5529: 21 80 55        LD      HL,$5580            ; {+code.turnSpot} Turn count spot in string
552C: 3A DE 4F        LD      A,($4FDE)           ; {code.bcdTurnCountMSB} Add MSB of turn ...
552F: CD 3F 55        CALL    $553F               ; {code.BinaryToASCII} ... count to string
5532: 3A DD 4F        LD      A,($4FDD)           ; {code.bcdTurnCountLSB} Add LSB of turn ...
5535: CD 3F 55        CALL    $553F               ; {code.BinaryToASCII} ... count to string
5538: 21 51 55        LD      HL,$5551            ; {+code.ScoreString} The string we just built
553B: CD CB 44        CALL    $44CB               ; {code.PrintPlain} Print the constructed score
553E: C9              RET                         

BinaryToASCII:
553F: F5              PUSH    AF                  ; Hold the lower nibble
5540: 0F              RRCA                        ; Roll ...
5541: 0F              RRCA                        ; ... to ...
5542: 0F              RRCA                        ; ... upper ...
5543: 0F              RRCA                        ; ... nibble
5544: CD 48 55        CALL    $5548               ; {} Convert and store the upper digit
5547: F1              POP     AF                  ; Restore the lower nibble, convert, and store
;
5548: E6 0F           AND     $0F                 ; Only keep 4 bits
554A: C6 30           ADD     $30                 ; Binary to ASCII digit
554C: 77              LD      (HL),A              ; Store in buffer
554D: 23              INC     HL                  ; Bump buffer
554E: C9              RET                         

scoreTempLSB:
554F: 00     

scoreTempMSB:
5550: 00                   

ScoreString:
; YOU_SCORED_______OUT_OF_A_POSSIBLE_0220,_USING______TURNS.[CR]
5551: 59 4F 55 20 53 43 4F 52 45 44 20 
scoreSign:
555C: 20 
scoreSpot:
555D: 20 20 20 20 20 4F 55 54 20 4F 46 20 41 20 50 4F 53 53 49 42
5571: 4C 45 20 30 32 32 30 2C 20 55 53 49 4E 47 20 
turnSpot:
5580: 20 20 20 20 20 54 55 52 4E 53 2E 00           
```

# Command 9: PrintScoreAndStop

```code
PrintScoreAndStop:
558C: CD 6A 54        CALL    $546A               ; {code.PrintScore} Print the score

EndlessLoop:
558F: C3 8F 55        JP      $558F               ; {code.EndlessLoop} Endless loop ... game over
```

# Command 27: LoadGame

```code
LoadGame:
5592: 21 F4 7E        LD      HL,$7EF4            
5595: CD A9 44        CALL    $44A9               ; {code.PrintPacked}
5598: CD E9 44        CALL    $44E9               ; {code.WaitForKey}
559B: FE 08           CP      $08                 ; 
559D: CA A6 42        JP      Z,$42A6             ; {code.ScriptCommandPASS}
55A0: FE 0D           CP      $0D                 ; 
55A2: C2 98 55        JP      NZ,$5598            ; {}
55A5: CD F4 0E        CALL    $0EF4               ; 
55A8: CA B4 55        JP      Z,$55B4             ; {}
55AB: 21 00 7F        LD      HL,$7F00            ; 
55AE: CD A9 44        CALL    $44A9               ; {code.PrintPacked}
55B1: C3 92 55        JP      $5592               ; {code.LoadGame}
55B4: 21 AC 6C        LD      HL,$6CAC            ; 
55B7: 22 E4 4F        LD      ($4FE4),HL          ; {code.ObjectDescriptions}
55BA: 22 E6 4F        LD      ($4FE6),HL          ; {}
55BD: CD E2 51        CALL    $51E2               ; {code.DescribeRoom}
55C0: 31 5C 47        LD      SP,$475C            ; 
55C3: C3 14 42        JP      $4214               ; {code.GameLoop}
```

# Command 28: SaveGame

```code
55C6: 21 F4 7E        LD      HL,$7EF4            
55C9: CD A9 44        CALL    $44A9               ; {code.PrintPacked}
55CC: CD E9 44        CALL    $44E9               ; {code.WaitForKey}
55CF: FE 08           CP      $08                 ; 
55D1: CA A6 42        JP      Z,$42A6             ; {code.ScriptCommandPASS}
55D4: FE 0D           CP      $0D                 ; 
55D6: C2 CC 55        JP      NZ,$55CC            ; {}
55D9: CD E9 0F        CALL    $0FE9               ; 
55DC: 21 E2 4E        LD      HL,$4EE2            ; 
55DF: 11 E6 4F        LD      DE,$4FE6            ; 
55E2: CD 4B 0F        CALL    $0F4B               ; 
55E5: C3 A6 42        JP      $42A6               ; {code.ScriptCommandPASS}
```

# Command 29: RandomizeDirections

```code   
55E8: 3A 11 47        LD      A,($4711)           ; {code.keyWaitCounter} Random value
55EB: E6 03           AND     $03                 ; 0, 1, 2, or 3
55ED: 47              LD      B,A                 ; To B
55EE: 21 69 49        LD      HL,$4969            ; {+code.room_1} start of room scripts
CNALL: ; This is the label from the actual 8080 source code (see Code1)
55F1: 7E              LD      A,(HL)              ; Get the verb number
55F2: 23              INC     HL                  ; Next byte
55F3: A7              AND     A                   ; End of script for this room?
55F4: CA F1 55        JP      Z,$55F1             ; {code.CNALL} Yes ... ignore the terminator and move to next room
55F7: FE FF           CP      $FF                 ; FF means the end of all room scripts
55F9: CA 16 56        JP      Z,$5616             ; {} We are done, print message and out
55FC: FE 05           CP      $05                 ; Is this verb in the script a compass direction?
55FE: D2 0C 56        JP      NC,$560C            ; {} No, skip over this command list
5601: 80              ADD     A,B                 ; Roll the verb
5602: 2B              DEC     HL                  ; Point back to the verb
5603: E6 03           AND     $03                 ; Limit to verbs 1-4
5605: C2 0A 56        JP      NZ,$560A            ; {code.CNAL2} Are we in 1, 2, or 3? Yes, keep it
5608: 3E 04           LD      A,$04               ; We rolled around. 0 becomes 4.
CNAL2: ; This is the label from the actual 8080 source code (see Code1)
560A: 77              LD      (HL),A              ; New verb number
560B: 23              INC     HL                  ; Point to list length
560C: 7E              LD      A,(HL)              ; Get the length
560D: 85              ADD     A,L                 ; Add ...
560E: 6F              LD      L,A                 ; ... length ...
560F: 7C              LD      A,H                 ; ... to ...
5610: CE 00           ADC     $00                 ; ... script ...
5612: 67              LD      H,A                 ; ... pointer
5613: C3 F1 55        JP      $55F1               ; {code.CNALL} Try all the verbs in all rooms
;
5616: 21 0C 7F        LD      HL,$7F0C            ; {+code.PS_C0} "I_NO_LONGER_SEEM_TO_KNOW_WHICH_WAY_IS_NORTH![CR]"
5619: CD A9 44        CALL    $44A9               ; {code.PrintPacked} Print message
561C: 31 5C 47        LD      SP,$475C            ; Reset stack
561F: C3 14 42        JP      $4214               ; {code.GameLoop} Back to top of game loop
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
wordTable:
; Nouns
;                               Objects     AA BBB CCC Word
5622: 1C 4C 41 4D 50            0E 0F 2C  ; 00_011_100 LAMP
562A: 1E 4C 41 4E 54 45 52      0E 0F 2C  ; 00_011_110 LANTER
5634: 0B 42 4F 58               10        ; 00_001_011 BOX
5639: 0F 53 43 45 50 54 45 52   11        ; 00_001_111 SCEPTER
5642: 14 42 49 52 44            13 14     ; 00_010_100 BIRD
5649: 16 53 54 41 54 55 45      13 14     ; 00_010_110 STATUE
5652: 0E 50 49 4C 4C 4F 57      12        ; 00_001_110 PILLOW
565A: 0E 56 45 4C 56 45 54      12        ; 00_001_110 VELVET
5662: 0E 53 45 52 50 45 4E      0B        ; 00_001_110 SERPEN
566A: 16 53 41 52 43 4F 50      17 18     ; 00_010_110 SARCOP
5673: 0E 4D 41 47 41 5A 49      19        ; 00_001_110 MAGAZI
567B: 0D 49 53 53 55 45         19        ; 00_001_101 ISSUE
5682: 0E 45 47 59 50 54 49      19        ; 00_001_110 EGYPTI
568A: 0C 46 4F 4F 44            1A        ; 00_001_100 FOOD
5690: 0E 42 4F 54 54 4C 45      1B        ; 00_001_110 BOTTLE
5698: 15 57 41 54 45 52         1C 1E     ; 00_010_101 WATER
56A0: 1D 50 4C 41 4E 54         07 08 09  ; 00_011_101 PLANT
56A9: 1E 42 45 41 4E 53 54      07 08 09  ; 00_011_110 BEANST
56B3: 0E 4D 41 43 48 49 4E      06        ; 00_001_110 MACHIN
56BB: 0E 56 45 4E 44 49 4E      06        ; 00_001_110 VENDIN
56C3: 16 42 41 54 54 45 52      23 24     ; 00_010_110 BATTER
56CC: 0C 47 4F 4C 44            25        ; 00_001_100 GOLD
56D2: 0E 4E 55 47 47 45 54      25        ; 00_001_110 NUGGET
56DA: 0E 44 49 41 4D 4F 4E      26        ; 00_001_110 DIAMON
56E2: 0E 53 49 4C 56 45 52      27        ; 00_001_110 SILVER
56EA: 0C 42 41 52 53            27        ; 00_001_100 BARS
56F0: 0E 4A 45 57 45 4C 52      28        ; 00_001_110 JEWELR
56F8: 0D 43 4F 49 4E 53         29        ; 00_001_101 COINS
56FF: 0D 43 48 45 53 54         2A        ; 00_001_101 CHEST
5706: 0E 54 52 45 41 53 55      2A        ; 00_001_110 TREASU
570E: 0C 45 47 47 53            2B        ; 00_001_100 EGGS
5714: 0B 45 47 47               2B        ; 00_001_011 EGG
5719: 0C 4E 45 53 54            2B        ; 00_001_100 NEST
571F: 0B 4B 45 59               22        ; 00_001_011 KEY
5724: 14 56 41 53 45            20 21     ; 00_010_100 VASE
572B: 0E 53 48 41 52 44 53      15        ; 00_001_110 SHARDS
5733: 0E 50 4F 54 54 45 52      15        ; 00_001_110 POTTER
573B: 0E 45 4D 45 52 41 4C      1F        ; 00_001_110 EMERAL
5743: 0D 50 45 41 52 4C         16        ; 00_001_101 PEARL
;
; Verbs
574A: C9 4E                     01        ; 11_001_001 N
574D: CD 4E 4F 52 54 48         01        ; 11_001_101 NORTH
5754: C9 45                     02        ; 11_001_001 E
5757: CC 45 41 53 54            02        ; 11_001_100 EAST
575D: C9 53                     03        ; 11_001_001 S
5760: CD 53 4F 55 54 48         03        ; 11_001_101 SOUTH
5767: C9 57                     04        ; 11_001_001 W
576A: CC 57 45 53 54            04        ; 11_001_100 WEST
5770: CA 4E 45                  05        ; 11_001_010 NE
5774: CE 4E 4F 52 54 48 45      05        ; 11_001_110 NORTHE
577C: CA 53 45                  06        ; 11_001_010 SE
5780: CE 53 4F 55 54 48 45      06        ; 11_001_110 SOUTHE
5788: CA 53 57                  07        ; 11_001_010 SW
578C: CE 53 4F 55 54 48 57      07        ; 11_001_110 SOUTHW
5794: CA 4E 57                  08        ; 11_001_010 NW
5798: CE 4E 4F 52 54 48 57      08        ; 11_001_110 NORTHW
57A0: C9 55                     09        ; 11_001_001 U
57A3: CA 55 50                  09        ; 11_001_010 UP
57A7: C9 44                     0A        ; 11_001_001 D
57AA: CC 44 4F 57 4E            0A        ; 11_001_100 DOWN
57B0: CA 49 4E                  0B        ; 11_001_010 IN
57B4: CE 49 4E 53 49 44 45      0B        ; 11_001_110 INSIDE
57BC: CB 4F 55 54               0C        ; 11_001_011 OUT
57C1: CE 4F 55 54 53 49 44      0C        ; 11_001_110 OUTSID
57C9: CD 43 52 4F 53 53         0D        ; 11_001_101 CROSS
57D0: CC 4C 45 46 54            0E        ; 11_001_100 LEFT
57D6: CD 52 49 47 48 54         0F        ; 11_001_101 RIGHT
57DD: CC 4A 55 4D 50            10        ; 11_001_100 JUMP
57E3: CD 43 4C 49 4D 42         11        ; 11_001_101 CLIMB
57EA: CD 50 41 4E 45 4C         12        ; 11_001_101 PANEL
57F1: CC 42 41 43 4B            14        ; 11_001_100 BACK
57F7: CC 53 57 49 4D            16        ; 11_001_100 SWIM
57FD: CA 4F 4E                  17        ; 11_001_010 ON
5801: CB 4F 46 46               18        ; 11_001_011 OFF
5806: CC 51 55 49 54            19        ; 11_001_100 QUIT
580C: CC 53 54 4F 50            19        ; 11_001_100 STOP
5812: CD 53 43 4F 52 45         1A        ; 11_001_101 SCORE
5819: CE 49 4E 56 45 4E 54      1B        ; 11_001_110 INVENT
5821: CC 4C 4F 4F 4B            1C        ; 11_001_100 LOOK
5827: CC 48 45 4C 50            1D        ; 11_001_100 HELP
582D: CC 46 49 4E 44            1E        ; 11_001_100 FIND
5833: 4C 44 52 4F 50            21        ; 01_001_100 DROP
5839: 4E 52 45 4C 45 41 53      21        ; 01_001_110 RELEAS
5841: 4C 46 52 45 45            21        ; 01_001_100 FREE
5847: 4E 44 49 53 43 41 52      21        ; 01_001_110 DISCAR
584F: CD 4C 49 47 48 54         17        ; 11_001_101 LIGHT
5856: 4C 57 41 56 45            23        ; 01_001_100 WAVE
585C: 4D 53 48 41 4B 45         23        ; 01_001_101 SHAKE
5863: 4D 53 57 49 4E 47         23        ; 01_001_101 SWING
586A: 4C 50 4F 55 52            24        ; 01_001_100 POUR
5870: 4B 52 55 42               25        ; 01_001_011 RUB
5875: 4D 54 48 52 4F 57         26        ; 01_001_101 THROW
587C: 4C 54 4F 53 53            26        ; 01_001_100 TOSS
5882: 4C 46 49 4C 4C            27        ; 01_001_100 FILL
5888: 8C 54 41 4B 45            28        ; 10_001_100 TAKE
588E: 8B 47 45 54               28        ; 10_001_011 GET
5893: 8D 43 41 52 52 59         28        ; 10_001_101 CARRY
589A: 8D 43 41 54 43 48         28        ; 10_001_101 CATCH
58A1: 8D 53 54 45 41 4C         28        ; 10_001_101 STEAL
58A8: 8E 43 41 50 54 55 52      28        ; 10_001_110 CAPTUR
58B0: 8C 4F 50 45 4E            29        ; 10_001_100 OPEN
58B6: 8E 41 54 54 41 43 4B      2C        ; 10_001_110 ATTACK
58BE: 8C 4B 49 4C 4C            2C        ; 10_001_100 KILL
58C4: 8B 48 49 54               2C        ; 10_001_011 HIT
58C9: 8D 46 49 47 48 54         2C        ; 10_001_101 FIGHT
58D0: 8C 46 45 45 44            2D        ; 10_001_100 FEED
58D6: 8B 45 41 54               2E        ; 10_001_011 EAT
58DB: 8D 44 52 49 4E 4B         2F        ; 10_001_101 DRINK
58E2: 8D 42 52 45 41 4B         30        ; 10_001_101 BREAK
58E9: 8D 53 4D 41 53 48         30        ; 10_001_101 SMASH
58F0: CC 4C 4F 41 44            3A        ; 11_001_100 LOAD
58F6: CC 53 41 56 45            3B        ; 11_001_100 SAVE
58FC: CD 50 4C 55 47 48         39        ; 11_001_101 PLUGH
5903: 00
```

# General Command Handler

This script is used when the room doesn't have a script for the input command.

```code
GeneralCommandHandler:
5904: 01 04     ; N
5906: 04 41 73  ;    Print(PS_7A:"THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]")
5909: 02 04     ; E
590B: 04 41 73  ;    Print(PS_7A:"THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]")
590E: 03 04     ; S
5910: 04 41 73  ;    Print(PS_7A:"THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]")
5913: 04 04     ; W
5915: 04 41 73  ;    Print(PS_7A:"THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]")
5918: 05 04     ; NE
591A: 04 41 73  ;    Print(PS_7A:"THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]")
591D: 06 04     ; SE
591F: 04 41 73  ;    Print(PS_7A:"THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]")
5922: 07 04     ; SW
5924: 04 41 73  ;    Print(PS_7A:"THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]")
5927: 08 04     ; NW
5929: 04 41 73  ;    Print(PS_7A:"THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]")
592C: 09 04     ; U
592E: 04 41 73  ;    Print(PS_7A:"THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]")
5931: 0A 04     ; D
5933: 04 41 73  ;    Print(PS_7A:"THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]")
5936: 0B 04     ; IN
5938: 04 61 73  ;    Print(PS_7B:"I_DON'T_KNOW_IN_FROM_OUT_HERE.__USE_COMPASS_POINTS.[CR]")
593B: 0C 04     ; OUT
593D: 04 61 73  ;    Print(PS_7B:"I_DON'T_KNOW_IN_FROM_OUT_HERE.__USE_COMPASS_POINTS.[CR]")
5940: 0E 04     ; LEFT
5942: 04 85 73  ;    Print(PS_7C:"I_AM_UNSURE_HOW_YOU_ARE_FACING.__USE_COMPASS_POINTS.[CR]")
5945: 0F 04     ; RIGHT
5947: 04 85 73  ;    Print(PS_7C:"I_AM_UNSURE_HOW_YOU_ARE_FACING.__USE_COMPASS_POINTS.[CR]")
594A: 12 04     ; PANEL
594C: 04 AA 73  ;    Print(PS_7D:"NOTHING_HAPPENS.[CR]")
594F: 14 02     ; BACK
5951: 0E        ;    MoveToLastRoom
5952: 16 04     ; SWIM
5954: 04 B7 73  ;    Print(PS_7E:"I_DON'T_KNOW_HOW.[CR]")
5957: 17 18     ; ON
5959: 07 0C     ;    StopIfPassElseContinue
595B: 02 0E     ;        AssertObjectIsInPack(obj_LAMP_off)
595D: 15 0E 00  ;        MoveObjectToRoom(obj_LAMP_off, room_0)
5960: 15 0F FF  ;        MoveObjectToRoom(obj_LAMP_on, room_255)
5963: 04 E3 73  ;        Print(PS_80:"YOUR_LAMP_IS_NOW_ON.[CR]")
5966: 07 06     ;    StopIfPassElseContinue
5968: 02 0F     ;        AssertObjectIsInPack(obj_LAMP_on)
596A: 04 E3 73  ;        Print(PS_80:"YOUR_LAMP_IS_NOW_ON.[CR]")
596D: 04 F3 73  ;    Print(PS_81:"YOU_HAVE_NO_SOURCE_OF_LIGHT.[CR]")
5970: 18 18     ; OFF
5972: 07 0C     ;    StopIfPassElseContinue
5974: 02 0F     ;        AssertObjectIsInPack(obj_LAMP_on)
5976: 15 0F 00  ;        MoveObjectToRoom(obj_LAMP_on, room_0)
5979: 15 0E FF  ;        MoveObjectToRoom(obj_LAMP_off, room_255)
597C: 04 08 74  ;        Print(PS_82:"YOUR_LAMP_IS_NOW_OFF.[CR]")
597F: 07 06     ;    StopIfPassElseContinue
5981: 02 0E     ;        AssertObjectIsInPack(obj_LAMP_off)
5983: 04 08 74  ;        Print(PS_82:"YOUR_LAMP_IS_NOW_OFF.[CR]")
5986: 04 F3 73  ;    Print(PS_81:"YOU_HAVE_NO_SOURCE_OF_LIGHT.[CR]")
5989: 19 02     ; QUIT
598B: 09        ;    PrintScoreAndStop
598C: 1A 02     ; SCORE
598E: 08        ;    PrintScore
598F: 1B 02     ; INVENT
5991: 0F        ;    PrintInventory
5992: 1C 02     ; LOOK
5994: 10        ;    PrintRoomDescription
5995: 1D 04     ; HELP
5997: 04 18 74  ;    Print(PS_83:"I'M_AS_CONFUSED_AS_YOU_ARE.[CR]")
599A: 1E 04     ; FIND
599C: 04 2C 74  ;    Print(PS_84:"I_CAN_ONLY_TELL_YOU_WHAT_YOU_SEE_AS_YOU_MOVE_ABOUT_AND__________
;                                 MANIPULATE_THINGS.__I_CAN_NOT_TELL_YOU_WHERE_REMOTE_THINGS_ARE.[CR]")
599F: 28 47     ; TAKE
59A1: 07 06     ;    StopIfPassElseContinue
59A3: 11 07     ;        AssertObjectMatchesUserInput(obj_PLANT_A)
59A5: 04 B5 79  ;        Print(PS_A8:"THE_PLANT_HAS_EXCEPTIONALLY_DEEP_ROOTS_AND_CANNOT_BE_PULLED_____
;                                     FREE.[CR]")
59A8: 07 17     ;    StopIfPassElseContinue
59AA: 11 13     ;        AssertObjectMatchesUserInput(obj_BIRD)
59AC: 07 06     ;        StopIfPassElseContinue
59AE: 02 11     ;            AssertObjectIsInPack(obj_SCEPTER)
59B0: 04 1B 7A  ;            Print(PS_AA:"AS_YOU_APPROACH_THE_STATUE,_IT_COMES_TO_LIFE_AND_FLIES_ACROSS___
;                                         THE_CHAMBER_WHERE_IT_LANDS_AND_RETURNS_TO_STONE.[CR]")
59B3: 07 09     ;        StopIfPassElseContinue
59B5: 02 10     ;            AssertObjectIsInPack(obj_BOX)
59B7: 15 13 00  ;            MoveObjectToRoom(obj_BIRD, room_0)
59BA: 19 14 10  ;            MoveObjectIntoContainer(obj_BIRD_boxed, obj_BOX)
59BD: 04 68 7A  ;        Print(PS_AB:"YOU_CAN_LIFT_THE_STATUE,_BUT_YOU_CANNOT_CARRY_IT.[CR]")
59C0: 07 0A     ;    StopIfPassElseContinue
59C2: 11 20     ;        AssertObjectMatchesUserInput(obj_VASE_pillow)
59C4: 12 21     ;        GetObjectFromRoom(obj_VASE_solo)
59C6: 15 20 00  ;        MoveObjectToRoom(obj_VASE_pillow, room_0)
59C9: 18 12     ;        MoveObjectToCurrentRoom(obj_PILLOW)
59CB: 07 0D     ;    StopIfPassElseContinue
59CD: 11 1E     ;        AssertObjectMatchesUserInput(obj_STREAM_56)
59CF: 07 06     ;        StopIfPassElseContinue
59D1: 02 1C     ;            AssertObjectIsInPack(obj_WATER)
59D3: 04 8B 7A  ;            Print(PS_AC:"YOUR_BOTTLE_IS_ALREADY_FULL.[CR]")
59D6: 19 1C 1B  ;        MoveObjectIntoContainer(obj_WATER, obj_BOTTLE)
59D9: 07 0C     ;    StopIfPassElseContinue
59DB: 11 12     ;        AssertObjectMatchesUserInput(obj_PILLOW)
59DD: 1A 20     ;        AssertObjectIsInCurrentRoom(obj_VASE_pillow)
59DF: 15 20 00  ;        MoveObjectToRoom(obj_VASE_pillow, room_0)
59E2: 18 21     ;        MoveObjectToCurrentRoom(obj_VASE_solo)
59E4: 12 12     ;        GetObjectFromRoom(obj_PILLOW)
59E6: 16        ;    GetUserInputObject
59E7: 21 17     ; DROP
59E9: 07 14     ;    StopIfPassElseContinue
59EB: 11 21     ;        AssertObjectMatchesUserInput(obj_VASE_solo)
59ED: 15 21 00  ;        MoveObjectToRoom(obj_VASE_solo, room_0)
59F0: 07 08     ;        StopIfPassElseContinue
59F2: 1A 12     ;            AssertObjectIsInCurrentRoom(obj_PILLOW)
59F4: 18 20     ;            MoveObjectToCurrentRoom(obj_VASE_pillow)
59F6: 04 69 7B  ;            Print(PS_B0:"THE_VASE_IS_NOW_RESTING,_DELICATELY,_ON_A_VELVET_PILLOW.[CR]")
59F9: 18 15     ;        MoveObjectToCurrentRoom(obj_POTTERY)
59FB: 04 91 7B  ;        Print(PS_B1:"THE_VASE_DROPS_WITH_A_DELICATE_CRASH.[CR]")
59FE: 17        ;    DropUserInputObject
59FF: 26 0E     ; THROW
5A01: 07 0B     ;    StopIfPassElseContinue
5A03: 11 21     ;        AssertObjectMatchesUserInput(obj_VASE_solo)
5A05: 15 21 00  ;        MoveObjectToRoom(obj_VASE_solo, room_0)
5A08: 18 15     ;        MoveObjectToCurrentRoom(obj_POTTERY)
5A0A: 04 C9 7B  ;        Print(PS_B3:"YOU_HAVE_TAKEN_THE_VASE_AND_HURLED_IT_DELICATELY_TO_THE_GROUND.[CR]")
5A0D: 17        ;    DropUserInputObject
5A0E: 29 36     ; OPEN
5A10: 07 1C     ;    StopIfPassElseContinue
5A12: 11 17     ;        AssertObjectMatchesUserInput(obj_SARCOPH_full)
5A14: 07 06     ;        StopIfPassElseContinue
5A16: 02 17     ;            AssertObjectIsInPack(obj_SARCOPH_full)
5A18: 04 55 76  ;            Print(PS_94:"I'D_ADVISE_YOU_TO_PUT_DOWN_THE_SARCOPHAGUS_BEFORE_OPENING_IT!![CR]")
5A1B: 07 0E     ;        StopIfPassElseContinue
5A1D: 02 22     ;            AssertObjectIsInPack(obj_KEY)
5A1F: 04 12 76  ;            Print(PS_93:"A_GLISTENING_PEARL_FALLS_OUT_OF_THE_SARCOPHAGUS_AND_ROLLS_AWAY._
;                                         THE_SARCOPHAGUS_SNAPS_SHUT_AGAIN.[CR]")
5A22: 15 16 40  ;            MoveObjectToRoom(obj_PEARL, room_64)
5A25: 15 17 00  ;            MoveObjectToRoom(obj_SARCOPH_full, room_0)
5A28: 18 18     ;            MoveObjectToCurrentRoom(obj_SARCOPH_empty)
5A2A: 04 BF 76  ;        Print(PS_96:"YOU_DON'T_HAVE_ANYTHING_STRONG_ENOUGH_TO_OPEN_THE_SARCOPHAGUS.[CR]")
5A2D: 07 14     ;    StopIfPassElseContinue
5A2F: 11 18     ;        AssertObjectMatchesUserInput(obj_SARCOPH_empty)
5A31: 07 06     ;        StopIfPassElseContinue
5A33: 02 18     ;            AssertObjectIsInPack(obj_SARCOPH_empty)
5A35: 04 55 76  ;            Print(PS_94:"I'D_ADVISE_YOU_TO_PUT_DOWN_THE_SARCOPHAGUS_BEFORE_OPENING_IT!![CR]")
5A38: 07 06     ;        StopIfPassElseContinue
5A3A: 02 22     ;            AssertObjectIsInPack(obj_KEY)
5A3C: 04 81 76  ;            Print(PS_95:"THE_SARCOPHAGUS_CREAKS_OPEN,_REVEALING_NOTHING_INSIDE.__IT______
;                                         PROMPTLY_SNAPS_SHUT_AGAIN.[CR]")
5A3F: 04 BF 76  ;        Print(PS_96:"YOU_DON'T_HAVE_ANYTHING_STRONG_ENOUGH_TO_OPEN_THE_SARCOPHAGUS.[CR]")
5A42: 04 EB 76  ;    Print(PS_97:"I_DON'T_KNOW_HOW_TO_LOCK_OR_UNLOCK_SUCH_A_THING.[CR]")
5A45: 23 04     ; WAVE
5A47: 04 AA 73  ;    Print(PS_7D:"NOTHING_HAPPENS.[CR]")
5A4A: 24 0E     ; POUR
5A4C: 07 09     ;    StopIfPassElseContinue
5A4E: 11 1C     ;        AssertObjectMatchesUserInput(obj_WATER)
5A50: 15 1C 00  ;        MoveObjectToRoom(obj_WATER, room_0)
5A53: 04 3D 75  ;        Print(PS_8C:"YOUR_BOTTLE_IS_EMPTY_AND_THE_GROUND_IS_WET.[CR]")
5A56: 04 5C 75  ;    Print(PS_8D:"YOU_CAN'T_POUR_THAT.[CR]")
5A59: 25 12     ; RUB
5A5B: 07 06     ;    StopIfPassElseContinue
5A5D: 11 0E     ;        AssertObjectMatchesUserInput(obj_LAMP_off)
5A5F: 04 6C 75  ;        Print(PS_8E:"RUBBING_THE_ELECTRIC_LAMP_IS_NOT_PARTICULARLY_REWARDING.________
;                                     ANYWAY,_NOTHING_EXCITING_HAPPENS.[CR]")
5A62: 07 06     ;    StopIfPassElseContinue
5A64: 11 0F     ;        AssertObjectMatchesUserInput(obj_LAMP_on)
5A66: 04 6C 75  ;        Print(PS_8E:"RUBBING_THE_ELECTRIC_LAMP_IS_NOT_PARTICULARLY_REWARDING.________
;                                     ANYWAY,_NOTHING_EXCITING_HAPPENS.[CR]")
5A69: 04 AF 75  ;    Print(PS_8F:"PECULIAR.__NOTHING_UNEXPECTED_HAPPENS.[CR]")
5A6C: 27 12     ; FILL
5A6E: 07 06     ;    StopIfPassElseContinue
5A70: 11 1B     ;        AssertObjectMatchesUserInput(obj_BOTTLE)
5A72: 04 CB 75  ;        Print(PS_90:"THERE_IS_NOTHING_HERE_WITH_WHICH_TO_FILL_THE_BOTTLE.[CR]")
5A75: 07 06     ;    StopIfPassElseContinue
5A77: 11 21     ;        AssertObjectMatchesUserInput(obj_VASE_solo)
5A79: 04 2D 75  ;        Print(PS_8B:"DON'T_BE_RIDICULOUS![CR]")
5A7C: 04 02 76  ;    Print(PS_92:"YOU_CAN'T_FILL_THAT.[CR]")
5A7F: 2C 2D     ; ATTACK
5A81: 07 09     ;    StopIfPassElseContinue
5A83: 11 13     ;        AssertObjectMatchesUserInput(obj_BIRD)
5A85: 15 13 00  ;        MoveObjectToRoom(obj_BIRD, room_0)
5A88: 04 0D 77  ;        Print(PS_98:"THE_BIRD_STATUE_IS_NOW_DEAD.__ITS_BODY_DISAPPEARS.[CR]")
5A8B: 07 09     ;    StopIfPassElseContinue
5A8D: 11 14     ;        AssertObjectMatchesUserInput(obj_BIRD_boxed)
5A8F: 15 14 00  ;        MoveObjectToRoom(obj_BIRD_boxed, room_0)
5A92: 04 0D 77  ;        Print(PS_98:"THE_BIRD_STATUE_IS_NOW_DEAD.__ITS_BODY_DISAPPEARS.[CR]")
5A95: 07 06     ;    StopIfPassElseContinue
5A97: 11 17     ;        AssertObjectMatchesUserInput(obj_SARCOPH_full)
5A99: 04 31 77  ;        Print(PS_99:"THE_STONE_IS_VERY_STRONG_AND_IS_IMPERVIOUS_TO_ATTACK.[CR]")
5A9C: 07 06     ;    StopIfPassElseContinue
5A9E: 11 18     ;        AssertObjectMatchesUserInput(obj_SARCOPH_empty)
5AA0: 04 31 77  ;        Print(PS_99:"THE_STONE_IS_VERY_STRONG_AND_IS_IMPERVIOUS_TO_ATTACK.[CR]")
5AA3: 07 06     ;    StopIfPassElseContinue
5AA5: 11 0B     ;        AssertObjectMatchesUserInput(obj_SERPENT)
5AA7: 04 57 77  ;        Print(PS_9A:"ATTACKING_THE_SERPENT_BOTH_DOESN'T_WORK_AND_IS_VERY_DANGEROUS.[CR]")
5AAA: 04 83 77  ;    Print(PS_9B:"YOU_CAN'T_BE_SERIOUS![CR]")
5AAD: 30 04     ; BREAK
5AAF: 04 93 77  ;    Print(PS_9C:"IT_IS_BEYOND_YOUR_POWER_TO_DO_THAT.[CR]")
5AB2: 2E 23     ; EAT
5AB4: 07 09     ;    StopIfPassElseContinue
5AB6: 11 1A     ;        AssertObjectMatchesUserInput(obj_FOOD)
5AB8: 15 1A 00  ;        MoveObjectToRoom(obj_FOOD, room_0)
5ABB: 04 AD 77  ;        Print(PS_9D:"THANK_YOU,_IT_WAS_DELICIOUS![CR]")
5ABE: 07 06     ;    StopIfPassElseContinue
5AC0: 11 0A     ;        AssertObjectMatchesUserInput(obj_UNUSED_10)
5AC2: 04 C2 77  ;        Print(PS_9E:"I_THINK_I_JUST_LOST_MY_APPETITE.[CR]")
5AC5: 07 06     ;    StopIfPassElseContinue
5AC7: 11 13     ;        AssertObjectMatchesUserInput(obj_BIRD)
5AC9: 04 C2 77  ;        Print(PS_9E:"I_THINK_I_JUST_LOST_MY_APPETITE.[CR]")
5ACC: 07 06     ;    StopIfPassElseContinue
5ACE: 11 14     ;        AssertObjectMatchesUserInput(obj_BIRD_boxed)
5AD0: 04 C2 77  ;        Print(PS_9E:"I_THINK_I_JUST_LOST_MY_APPETITE.[CR]")
5AD3: 04 2D 75  ;    Print(PS_8B:"DON'T_BE_RIDICULOUS![CR]")
5AD6: 2F 15     ; DRINK
5AD8: 07 09     ;    StopIfPassElseContinue
5ADA: 11 1C     ;        AssertObjectMatchesUserInput(obj_WATER)
5ADC: 15 1C 00  ;        MoveObjectToRoom(obj_WATER, room_0)
5ADF: 04 F0 75  ;        Print(PS_91:"THE_BOTTLE_IS_NOW_EMPTY.[CR]")
5AE2: 07 06     ;    StopIfPassElseContinue
5AE4: 11 1E     ;        AssertObjectMatchesUserInput(obj_STREAM_56)
5AE6: 04 DA 77  ;        Print(PS_9F:"YOU_HAVE_TAKEN_A_DRINK_FROM_THE_STREAM.__THE_WATER_TASTES_______
;                                     STRONGLY_OF_MINERALS,_BUT_IS_NOT_UNPLEASANT.__IT_IS_EXTREMELY___
;                                     COLD.[CR]")
5AE9: 04 83 77  ;    Print(PS_9B:"YOU_CAN'T_BE_SERIOUS![CR]")
5AEC: 2D 38     ; FEED
5AEE: 07 06     ;    StopIfPassElseContinue
5AF0: 11 13     ;        AssertObjectMatchesUserInput(obj_BIRD)
5AF2: 04 35 78  ;        Print(PS_A0:"IT'S_NOT_HUNGRY.__BESIDES,_YOU_HAVE_NO_BIRD_SEED.[CR]")
5AF5: 07 06     ;    StopIfPassElseContinue
5AF7: 11 14     ;        AssertObjectMatchesUserInput(obj_BIRD_boxed)
5AF9: 04 35 78  ;        Print(PS_A0:"IT'S_NOT_HUNGRY.__BESIDES,_YOU_HAVE_NO_BIRD_SEED.[CR]")
5AFC: 07 10     ;    StopIfPassElseContinue
5AFE: 11 0B     ;        AssertObjectMatchesUserInput(obj_SERPENT)
5B00: 07 09     ;        StopIfPassElseContinue
5B02: 02 14     ;            AssertObjectIsInPack(obj_BIRD_boxed)
5B04: 15 14 00  ;            MoveObjectToRoom(obj_BIRD_boxed, room_0)
5B07: 04 7F 78  ;            Print(PS_A2:"THE_SERPENT_HAS_NOW_DEVOURED_YOUR_BIRD_STATUE.[CR]")
5B0A: 04 A0 78  ;        Print(PS_A3:"THERE_IS_NOTHING_HERE_IT_WANTS_TO_EAT_-_EXCEPT_PERHAPS_YOU.[CR]")
5B0D: 07 06     ;    StopIfPassElseContinue
5B0F: 11 17     ;        AssertObjectMatchesUserInput(obj_SARCOPH_full)
5B11: 04 FB 78  ;        Print(PS_A5:"I'M_GAME.__WOULD_YOU_CARE_TO_EXPLAIN_HOW?[CR]")
5B14: 07 06     ;    StopIfPassElseContinue
5B16: 11 18     ;        AssertObjectMatchesUserInput(obj_SARCOPH_empty)
5B18: 04 FB 78  ;        Print(PS_A5:"I'M_GAME.__WOULD_YOU_CARE_TO_EXPLAIN_HOW?[CR]")
5B1B: 07 06     ;    StopIfPassElseContinue
5B1D: 11 0D     ;        AssertObjectMatchesUserInput(obj_UNUSED_13)
5B1F: 04 A0 78  ;        Print(PS_A3:"THERE_IS_NOTHING_HERE_IT_WANTS_TO_EAT_-_EXCEPT_PERHAPS_YOU.[CR]")
5B22: 04 2D 75  ;    Print(PS_8B:"DON'T_BE_RIDICULOUS![CR]")
5B25: 39 02     ; PLUGH
5B27: 1D        ;    RandomizeDirections
5B28: 3A 02     ; LOAD
5B2A: 1B        ;    LoadGame
5B2B: 3B 02     ; SAVE
5B2D: 1C        ;    SaveGame
5B2E: 00
```

# Packed strings

```code

; YOU_ARE_STANDING_BEFORE_THE_ENTRANCE_OF_A_PYRAMID.__AROUND_YOU__
; IS_A_DESERT.[CR]
PS_00: ; room_1
5B2F: 19 C7 DE 94 14 55 5E 50 BD 90 5A C4 6A 59 60 5B
5B3F: B1 5F BE 30 15 EB BF 17 98 B8 16 7B 14 14 A8 6B
5B4F: 48 9B 5D 94 14 30 A1 1B 58 1B A1 D5 15 7B 14 F5
5B5F: 59 3E 62 2E 00

; YOU_ARE_IN_THE_ENTRANCE_TO_THE_PYRAMID.__A_HOLE_IN_THE_FLOOR____
; LEADS_TO_A_PASSAGE_BENEATH_THE_SURFACE.[CR]
PS_01: ; room_2
5B64: 22 C7 DE 94 14 4B 5E 96 96 DB 72 9E 61 D0 B0 9B
5B74: 53 6B BF 5F BE F3 16 CF B0 17 79 43 13 A9 15 DB
5B84: 8B 83 7A 5F BE 56 15 44 A0 3B 13 3F 16 0D 47 89
5B94: 17 7B 14 55 A4 09 B7 44 5E 8F 61 82 49 82 17 55
5BA4: 5E 30 C6 D7 46 2E 00

; YOU_ARE_IN_THE_DESERT.[CR]
PS_02: ; room_3, room_4, room_5, room_6
5BAB: 07 C7 DE 94 14 4B 5E 96 96 DB 72 F5 59 3E 62 2E
5BBB: 00

; YOU_ARE_IN_A_SMALL_CHAMBER_BENEATH_A_HOLE_FROM_THE_SURFACE.__A__
; LOW_CRAWL_LEADS_INWARD_TO_THE_WEST.__HIEROGLYPHICS_ON_THE_WALL__
; TRANSLATE,_"CURSE_ALL_WHO_ENTER_THIS_SACRED_CRYPT."[CR]
PS_03: ; room_7
5BBC: 3B C7 DE 94 14 4B 5E 83 96 5F 17 46 48 DA 14 64
5BCC: 48 23 62 70 4D 96 5F 03 71 A9 15 DB 8B 79 68 56
5BDC: 90 DB 72 34 BA C5 65 DB 63 7B 14 49 16 C5 CE D9
5BEC: B0 0E 8A 86 5F CB B5 33 9B 33 B1 6B BF 5F BE F7
5BFC: 17 17 BA 4A 13 34 79 FE 9E E2 DE E5 78 C0 16 82
5C0C: 17 59 5E 46 48 56 13 D0 B0 BB B8 FE BD 6D 13 3D
5C1C: C6 43 5E F3 8C 29 D1 30 15 F4 BD 82 17 4B 7B 05
5C2C: B7 66 B1 E4 14 EE DE 2E 22 00

; YOU_ARE_CRAWLING_OVER_PEBBLES_IN_A_LOW_PASSAGE.__THERE_IS_A_DIM_
; LIGHT_AT_THE_EAST_END_OF_THE_PASSAGE.[CR]
PS_04: ; room_8
5C36: 21 C7 DE 94 14 45 5E D9 B0 90 8C D1 6A 74 CA DF
5C46: 16 F6 4C 4B 62 83 7A 4E 45 6B A1 55 A4 09 B7 DB
5C56: 63 82 17 2F 62 D5 15 7B 14 8F 5A 43 16 2E 6D 96
5C66: 14 82 17 47 5E 66 49 30 15 11 58 96 64 DB 72 55
5C76: A4 09 B7 45 2E 00

; YOU_ARE_IN_A_ROOM_FILLED_WITH_BROKEN_POTTERY_SHARDS_OF_ANCIENT__
; EGYPTIAN_CRAFTS.__AN_AWKWARD_CORRIDOR_LEADS_UPWARD_AND_WEST.[CR]
PS_05: ; room_9
5C7C: 29 C7 DE 94 14 4B 5E 83 96 39 17 DB 9F 0E 67 E6
5C8C: 8B FB 17 53 BE 79 4F B0 85 E9 16 3F C0 7B B4 1B
5C9C: B8 4D B1 B8 16 90 14 47 54 B3 9A 29 15 EE DE 90
5CAC: 78 E4 14 5E 47 5B BB 90 14 99 14 73 88 33 B1 44
5CBC: 55 06 B2 A3 A0 E3 8B 0B 5C F1 C5 2E 49 90 14 19
5CCC: 58 66 62 2E 00

; YOU_ARE_IN_AN_AWKWARD_SLOPING_EAST/WEST_CORRIDOR.[CR]
PS_06: ; room_10
5CD1: 10 C7 DE 94 14 4B 5E 83 96 83 96 A9 D1 2E 49 5E
5CE1: 17 63 A0 AB 98 95 5F E1 BC 66 62 E1 14 73 B3 84
5CF1: 5B 2E 00

; YOU_ARE_IN_A_SPLENDID_CHAMBER_THIRTY_FEET_HIGH.__THE_WALLS_ARE__
; FROZEN_RIVERS_OF_ORANGE_STONE.__AN_AWKWARD_CORRIDOR_AND_A_GOOD__
; PASSAGE_EXIT_FROM_THE_EAST_AND_WEST_SIDES_OF_THE_CHAMBER.[CR]
PS_07: ; room_11
5CF4: 3D C7 DE 94 14 4B 5E 83 96 62 17 F0 8B 86 5A DA
5D04: 14 64 48 23 62 63 BE D3 B3 4F 15 73 62 89 73 9B
5D14: 76 82 17 59 5E 46 48 C3 B5 5B B1 5C 15 EF A1 94
5D24: 96 CF 7B 8B B3 C3 9E AB A0 B7 98 66 17 0F A0 3B
5D34: F4 83 48 FD 49 14 D0 05 58 BC A0 09 79 83 AF 33
5D44: 98 49 45 36 A0 52 13 65 49 77 47 3A 15 73 7B 79
5D54: 68 56 90 DB 72 95 5F 03 BC 33 98 B5 D0 15 BC FF
5D64: 78 D1 B5 96 64 DB 72 1B 54 AF 91 52 2E 00

; AT_YOUR_FEET_IS_A_SMALL_PIT_BREATHING_TRACES_OF_WHITE_MIST.__AN_
; EAST_PASSAGE_ENDS_HERE_EXCEPT_FOR_A_SMALL_CRACK_LEADING_ON._____
; ROUGH_STONE_STEPS_LEAD_DOWN_THE_PIT.[CR]
PS_08: ; room_12
5D72: 36 73 49 C7 DE 88 AF 36 60 D5 15 7B 14 E3 B8 F3
5D82: 8C 96 A5 BC 14 96 5F 90 73 D6 6A C5 B0 4B 62 C3
5D92: 9E 23 D1 DB BD D5 92 9B C1 90 14 23 15 F3 B9 55
5DA2: A4 09 B7 47 5E 4D 98 9F 15 5B B1 1D 63 EE 61 59
5DB2: 15 83 AF 5F 17 46 48 E4 14 DD 46 3F 16 03 47 AB
5DC2: 98 27 A0 3B 13 54 13 29 A1 15 71 80 BF 55 5E F2
5DD2: BD CE B5 86 5F 09 15 03 D2 5F BE E3 16 54 2E 00

; YOU_ARE_AT_ONE_END_OF_A_VAST_HALL_STRETCHING_FORWARD_OUT_OF_____
; SIGHT_TO_THE_WEST.__THERE_ARE_OPENINGS_TO_EITHER_SIDE.__NEARBY,_
; A_WIDE_STONE_STAIRCASE_LEADS_DOWNWARD.__THE_HALL_IS_VERY_MUSTY__
; AND_A_COLD_WIND_BLOWS_UP_THE_STAIRCASE.__THERE_IS_A_PASSAGE_AT__
; THE_TOP_OF_A_DOME_BEHIND_YOU.__ROUGH_STONE_STEPS_LEAD_UP_THE____
; DOME.[CR]
PS_09: ; room_13
5DE2: 6C C7 DE 94 14 43 5E 11 BC 5B 98 8E 61 B8 16 7B
5DF2: 14 D5 C9 0A BC 46 48 66 17 76 B1 23 54 AB 98 04
5E02: 68 14 D0 11 58 73 C6 C3 9E 3B 13 5B 17 2E 6D 89
5E12: 17 82 17 59 5E 66 62 3B F4 5F BE 5B B1 2F 49 C2
5E22: 16 93 61 C5 98 89 17 2B 15 5F BE 95 AF FF 78 3B
5E32: F4 63 98 03 B1 03 EE FB 17 DB 59 09 BA 5B 98 FB
5E42: B9 2D 7B 57 49 3F 16 0D 47 09 15 21 D2 2E 49 3B
5E52: F4 5F BE 9B 15 F3 8C 4B 7B 74 CA 4F DB 66 C6 3B
5E62: DB 8E 48 7B 14 3E 55 19 58 8E 7A B6 14 85 A1 B2
5E72: 17 82 17 55 5E 4B BD 13 B1 BF B7 56 13 F4 72 4B
5E82: 5E C3 B5 DB 16 D3 B9 9B 6C 73 49 82 17 56 5E 53
5E92: A0 C3 9E 46 45 E7 9F AF 14 90 73 1B 58 3F A1 54
5EA2: 13 29 A1 15 71 80 BF 55 5E F2 BD CE B5 86 5F B2
5EB2: 17 82 17 3B 5E 46 13 E7 9F 2E 00

; THIS_IS_A_LOW_ROOM_WITH_A_HIEROGLYPH_ON_THE_WALL.__IT_TRANSLATES
; "YOU_WON'T_GET_IT_UP_THE_STEPS".[CR]
PS_0A: ; room_14
5EBD: 20 63 BE CB B5 C3 B5 49 16 D4 CE 3F A0 FB 17 53
5ECD: BE 4A 45 34 79 FE 9E E2 DE C0 16 82 17 59 5E 46
5EDD: 48 3B F4 73 7B EB BF 9E 9A 7F 49 03 B6 1B A1 40
5EED: D2 F3 23 B6 6C D6 15 B2 17 82 17 55 5E F2 BD 07
5EFD: B6 00

; YOU_ARE_ON_THE_EAST_BANK_OF_A_BOTTOMLESS_PIT_STRETCHING_ACROSS__
; THE_HALL.__THE_MIST_IS_QUITE_THICK_HERE,_AND_THE_PIT_IS_TOO_WIDE
; TO_JUMP.[CR]
PS_0B: ; room_15
5EFF: 2D C7 DE 94 14 51 5E 96 96 DB 72 95 5F 04 BC 95
5F0F: 48 B8 16 7B 14 06 4F 7F BF F5 8B D2 B5 73 7B 0C
5F1F: BA 7D 62 90 73 C3 6A B9 55 CB B9 82 17 4A 5E 46
5F2F: 48 3B F4 5F BE 6B 16 F3 B9 4B 7B AB AD DB BD 63
5F3F: BE 8B 54 F4 72 B3 63 8E 48 82 17 52 5E 73 7B 4B
5F4F: 7B 81 BF FB 17 F6 59 CC 9C 72 C5 2E 00

; YOU_ARE_IN_THE_PHARAOH'S_CHAMBER,_WITH_PASSAGES_OFF_IN_ALL______
; DIRECTIONS.[CR]
PS_0C: ; room_16
5F5C: 19 C7 DE 94 14 4B 5E 96 96 DB 72 5B A5 D1 B0 65
5F6C: 71 DA 14 64 48 46 62 FB 17 53 BE 55 A4 09 B7 4B
5F7C: 62 D0 9E D0 15 8E 14 FB 89 3B 13 03 15 65 B1 91
5F8C: BE AF 9A 00

; YOU_ARE_IN_THE_SOUTH_SIDE_CHAMBER.[CR]
PS_0D: ; room_17
5F90: 0B C7 DE 94 14 4B 5E 96 96 DB 72 47 B9 53 BE 46
5FA0: B8 45 5E 4F 72 74 4D 2E 00

; YOU_ARE_ON_THE_WEST_SIDE_OF_THE_BOTTOMLESS_PIT_IN_THE_HALL_OF___
; GODS.[CR]
PS_0E: ; room_18
5FA9: 17 C7 DE 94 14 51 5E 96 96 DB 72 B5 D0 15 BC FF
5FB9: 78 B8 16 82 17 44 5E 0E A1 EE 9F 65 62 E3 16 0B
5FC9: BC 96 96 DB 72 4E 72 11 8A 7B 64 81 15 2F 5C 00

; YOU_ARE_AT_THE_WEST_END_OF_THE_HALL_OF_GODS.___A_LOW_WIDE_PASS__
; CONTINUES_WEST_AND_ANOTHER_GOES_NORTH.__TO_THE_SOUTH_IS_A_LITTLE
; PASSAGE_SIX_FEET_OFF_THE_FLOOR.[CR]
PS_0F: ; room_19
5FD9: 35 C7 DE 94 14 43 5E 16 BC DB 72 B5 D0 07 BC 33
5FE9: 98 C3 9E 5F BE 9B 15 F3 8C C3 9E 36 6E 5B BB 43
5FF9: 13 49 16 D9 CE FF 78 DB 16 CB B9 E1 14 C3 9A E7
6009: 9A D9 B5 66 62 90 14 03 58 06 9A F4 72 81 15 4B
6019: 62 04 9A 77 BE 56 13 D6 9C DB 72 47 B9 53 BE 4B
6029: 7B 4E 45 8E 7B F2 8B 65 49 77 47 5B 17 08 D5 36
6039: 60 B8 16 96 64 DB 72 89 67 C7 A0 00

; YOU_ARE_AT_EAST_END_OF_A_VERY_LONG_HALL_APPARENTLY_WITHOUT_SIDE_
; CHAMBERS.__TO_THE_EAST_A_LOW_WIDE_CRAWL_SLANTS_UP.__TO_THE_NORTH
; A_ROUND_TWO_FOOT_HOLE_SLANTS_DOWN.[CR]
PS_10: ; room_20
6045: 36 C7 DE 94 14 43 5E 07 BC 66 49 30 15 11 58 83
6055: 64 CF 17 7B B4 80 8D CA 6A 46 48 92 14 54 A4 9E
6065: 61 FB 8E 56 D1 87 74 15 BC FF 78 DA 14 64 48 3D
6075: 62 3B F4 6B BF 5F BE 23 15 F3 B9 4E 45 6B A1 46
6085: D1 45 5E D9 B0 15 8A 50 8B 0B C0 F7 C5 56 13 D6
6095: 9C DB 72 04 9A 5B BE 39 17 8E C5 91 17 C8 9C 46
60A5: A0 A9 15 DB 8B BB B8 CD 9A 09 15 27 D2 00

; YOU_ARE_AT_THE_WEST_END_OF_A_VERY_LONG_FEATURELESS_HALL.__THE___
; HALL_JOINS_; UP_WITH_A_NARROW_NORTH/SOUTH_PASSAGE.[CR]
PS_11: ; room_21
60B3: 25 C7 DE 94 14 43 5E 16 BC DB 72 B5 D0 07 BC 33
60C3: 98 C3 9E 58 45 43 62 49 16 AB 98 63 66 74 C0 3F
60D3: 61 CB B9 4E 72 9B 8F 82 17 3B 5E 9B 15 F3 8C FB
60E3: 80 8B 9A D3 C5 56 D1 03 71 8B 16 79 B3 D0 CE BE
60F3: A0 DD 71 36 A1 12 71 65 49 77 47 2E 00

; YOU_ARE_AT_A_CROSSOVER_OF_A_HIGH_N/S_PASSAGE_AND_A_LOW_E/W_ONE.[CR]
PS_12: ; room_22
6100: 15 C7 DE 94 14 43 5E 03 BC E4 14 E5 A0 4F A1 91
6110: AF 83 64 A3 15 13 6D 5D 97 DB 16 D3 B9 9B 6C 8E
6120: 48 7B 14 89 8D 20 15 D1 CE 7F 98 00

; DEAD_END.[CR]
PS_13: ; room_23, room_42, room_43, room_44, room_45, room_46, room_47, room_48, room_49, room_50, room_51, room_53
612C: 03 E3 59 07 58 57 98 00

; YOU_ARE_IN_THE_WEST_THRONE_CHAMBER.__A_PASSAGE_CONTINUES_WEST___
; AND_UP_FROM_HERE.[CR]
PS_14: ; room_24
6134: 1B C7 DE 94 14 4B 5E 96 96 DB 72 B5 D0 16 BC F9
6144: 74 5B 98 1B 54 AF 91 1B B5 7B 14 55 A4 09 B7 45
6154: 5E 1E A0 9F 7A 4B 62 B5 D0 FB BB 90 14 17 58 08
6164: A3 FF B2 9F 15 7F B1 00

; YOU_ARE_IN_A_LOW_N/S_PASSAGE_AT_A_HOLE_IN_THE_FLOOR.__THE_HOLE__
; GOES_DOWN_TO_AN_E/W_PASSAGE.[CR]
PS_15: ; room_25
616C: 1E C7 DE 94 14 4B 5E 83 96 49 16 D0 CE 8B 36 55
617C: A4 09 B7 43 5E 03 BC A9 15 DB 8B 83 7A 5F BE 56
618C: 15 44 A0 3B F4 5F BE A9 15 DB 8B 81 15 4B 62 89
619C: 5B 96 96 C3 9C 87 96 2B 37 55 A4 09 B7 45 2E 00

; YOU_ARE_IN_A_LARGE_ROOM,_WITH_A_PASSAGE_TO_THE_SOUTH,_AND_A_WALL
; OF_BROKEN_ROCK_TO_THE_EAST.__THERE_IS_A_PANEL_ON_THE_NORTH_WALL.[CR]
PS_16: ; room_26
61AC: 2A C7 DE 94 14 4B 5E 83 96 3B 16 B7 B1 39 17 FE
61BC: 9F FB 17 53 BE 52 45 65 49 77 47 89 17 82 17 55
61CC: 5E 36 A1 73 76 8E 48 7B 14 0E D0 78 8D BC 14 97
61DC: 9F 94 96 5D 9E 89 17 82 17 47 5E 66 49 3B F4 5F
61EC: BE 5B B1 4B 7B 52 45 8F 48 11 8A 96 96 DB 72 04
61FC: 9A 53 BE 0E D0 4C 2E 00

; YOU_ARE_IN_THE_CHAMBER_OF_ANUBIS.[CR]
PS_17: ; room_27
6204: 0B C7 DE 94 14 4B 5E 96 96 DB 72 1B 54 AF 91 91
6214: AF 83 64 E4 9A 6F 7B 00

; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
PS_18: ; room_28, room_29, room_30, room_31, room_32, room_33, room_34, room_35, room_36, room_37, room_38, room_39, room_40, room_41
621C: 10 C7 DE 94 14 4B 5E 83 96 63 16 5B E3 C3 9E BB
622C: C0 13 BA DB 16 D3 B9 B5 6C 03 EE F3 8C 43 48 BF
623C: 85 00

; YOU_ARE_ON_THE_BRINK_OF_A_LARGE_PIT.__YOU_COULD_CLIMB_DOWN,_BUT_
; YOU_WOULD_NOT_BE_ABLE_TO_CLIMB_BACK_UP.__THE_MAZE_CONTINUES_ON__
; THIS_LEVEL.[CR]
PS_19: ; room_52
623E: 2E C7 DE 94 14 51 5E 96 96 DB 72 73 4F 4B 99 C3
624E: 9E 4E 45 31 49 52 5E 97 7B 5B 13 1B A1 47 55 B3
625E: 8B C3 54 A3 91 89 5B F3 9B F6 4F 51 18 59 C2 2E
626E: A1 10 58 F3 A0 5B 4D B6 46 56 5E C5 9C 8F 8C 84
627E: 4B DD 46 B2 17 3B F4 5F BE 63 16 5B E3 40 55 90
628E: BE 35 C4 C0 16 56 13 95 73 3F 16 6E CA 2E 00

; YOU_ARE_IN_A_DIRTY_BROKEN_PASSAGE.__TO_THE_EAST_IS_A_CRAWL.__TO_
; THE_WEST_IS_A_LARGE_PASSAGE.__ABOVE_YOU_IS_A_HOLE_TO_ANOTHER____
; PASSAGE.[CR]
PS_1A: ; room_54
629D: 2D C7 DE 94 14 4B 5E 83 96 03 15 D3 B3 BC 14 97
62AD: 9F 92 96 65 49 77 47 3B F4 6B BF 5F BE 23 15 F3
62BD: B9 4B 7B 45 45 D9 B0 9B 8F 89 17 82 17 59 5E 66
62CD: 62 D5 15 7B 14 54 8B 9B 6C 55 A4 09 B7 DB 63 84
62DD: 14 4F A1 51 18 4B C2 C3 B5 A9 15 DB 8B 6B BF 99
62ED: 48 5F BE 7B AF 52 13 65 49 77 47 2E 00

; YOU_ARE_ON_THE_BRINK_OF_A_SMALL_CLEAN_CLIMBABLE_PIT.__A_CRAWL___
; LEADS_WEST.[CR]
PS_1B: ; room_55
62FA: 19 C7 DE 94 14 51 5E 96 96 DB 72 73 4F 4B 99 C3
630A: 9E 55 45 8E 91 05 8A E3 8B 85 96 8F 8C C4 4C DB
631A: 8B 96 A5 3B F4 45 45 D9 B0 FB 89 3F 16 0D 47 F7
632A: 17 17 BA 00

; YOU_ARE_IN_THE_BOTTOM_OF_A_SMALL_PIT_WITH_A_LITTLE_STREAM,_WHICH
; ENTERS_AND_EXITS_THROUGH_TINY_SLITS.[CR]
PS_1C: ; room_56
632E: 21 C7 DE 94 14 4B 5E 96 96 DB 72 06 4F 7F BF B8
633E: 16 7B 14 E3 B8 F3 8C 96 A5 FB 17 53 BE 4E 45 8E
634E: 7B DB 8B 0C BA 8F 5F 19 EE 85 73 F0 72 F4 BD C3
635E: B5 33 98 23 63 0B C0 6C BE 29 A1 16 71 A3 7A 5E
636E: 17 8D 7B 2E 00

; YOU_ARE_IN_A_THE_ROOM_OF_BES,_WHOSE_PICTURE_IS_ON_THE_WALL._____
; THERE_IS_A_BIG_HOLE_IN_THE_FLOOR.__THERE_IS_A_PASSAGE_LEADING___
; EAST.[CR]
PS_1D: ; room_57
6373: 2C C7 DE 94 14 4B 5E 83 96 82 17 54 5E 3F A0 B8
6383: 16 AF 14 33 BB 29 D1 9B B7 85 A5 74 C0 4B 5E D1
6393: B5 96 96 DB 72 0E D0 9B 8F 3B 13 82 17 2F 62 D5
63A3: 15 7B 14 09 4E A9 15 DB 8B 83 7A 5F BE 56 15 44
63B3: A0 3B F4 5F BE 5B B1 4B 7B 52 45 65 49 77 47 3F
63C3: 16 03 47 AB 98 47 13 66 49 2E 00

; YOU_ARE_AT_A_COMPLEX_JUNCTION.__A_LOW_HANDS_AND_KNEES_PASSAGE___
; FROM_THE_NORTH_JOINS_A_HIGHER_CRAWL_FROM_THE_EAST_TO_MAKE_A_____
; WALKING_PASSAGE_GOING_WEST.__THERE_IS_ALSO_A_LARGE_ROOM_ABOVE.__
; THE_AIR_IS_DAMP_HERE.[CR]
PS_1E: ; room_58
63CE: 47 C7 DE 94 14 43 5E 03 BC E1 14 E6 93 13 63 F0
63DE: 81 03 56 27 A0 43 13 49 16 CA CE 8E 48 C3 B5 33
63EE: 98 0F 87 4B 62 55 A4 09 B7 3B 5E 5C 15 DB 9F 5F
63FE: BE 99 16 C2 B3 F9 15 9D 7A 7B 14 89 73 F4 72 E4
640E: 14 FE 49 5C 15 DB 9F 5F BE 23 15 F3 B9 6B BF 8D
641E: 91 43 5E 3B 13 59 13 45 48 91 7A DB 16 D3 B9 9B
642E: 6C 3B 6E AB 98 B5 D0 9B C1 82 17 2F 62 D5 15 8E
643E: 14 2B B9 4E 45 31 49 54 5E 3F A0 84 14 4F A1 3B
644E: F4 5F BE 8B 14 8B AF C6 B5 72 48 9F 15 7F B1 00

; YOU_ARE_IN_THE_UNDERWORLD_ANTEROOM_OF_SEKER.__PASSAGES_GO_EAST,_
; WEST,_AND_UP.__HUMAN_BONES_ARE_STREWN_ABOUT_ON_THE_FLOOR._______
; HIEROGLYPHICS_ON_THE_WALL_ROUGHLY_TRANSLATE_TO_"THOSE_WHO_______
; PROCEED_EAST_MAY_NEVER_RETURN."[CR]
PS_1F: ; room_59
645E: 4A C7 DE 94 14 4B 5E 96 96 DB 72 8E C5 41 62 B6
646E: A0 03 58 BF 9A 01 B3 51 90 95 64 17 61 1B B5 DB
647E: 16 D3 B9 B5 6C 81 15 23 15 16 BA F7 17 16 BA 90
648E: 14 17 58 9B A8 AF 15 90 91 B9 14 75 98 94 14 55
649E: 5E EF BF 03 D2 B9 46 73 C6 03 A0 5F BE 56 15 44
64AE: A0 3B F4 3B 13 4A 13 34 79 FE 9E E2 DE E5 78 C0
64BE: 16 82 17 59 5E 46 48 39 17 7A C4 FB 8E EB BF 9E
64CE: 9A 7F 49 89 17 7E 13 85 74 59 5E 6B 74 3B 13 3B
64DE: 13 F9 A6 A7 53 07 58 66 49 63 16 50 DB CF 62 94
64EE: AF 8F 62 E7 B2 22 00

; YOU_ARE_AT_THE_LAND_OF_DEAD.__PASSAGES_LEAD_OFF_IN_>ALL<________
; DIRECTIONS.[CR]
PS_20: ; room_60
64F5: 19 C7 DE 94 14 43 5E 16 BC DB 72 50 8B 11 58 86
6505: 64 86 5F 3B F4 55 A4 09 B7 4B 62 E3 8B 11 58 83
6515: 66 83 7A 8E 2D 73 8A 3B 13 3B 13 03 15 65 B1 91
6525: BE AF 9A 00

; YOU'RE_IN_A_LARGE_ROOM_WITH_ANCIENT_DRAWINGS_ON_ALL_WALLS.______
; THE_PICTURES_DEPICT_ATUM,_A_PHARAOH_WEARING_THE_DOUBLE_CROWN.___
; A_SHALLOW_PASSAGE_PROCEEDS_DOWNWARD,_AND_A_SOMEWHAT_STEEPER_ONE_
; LEADS_UP.__A_LOW_HANDS_AND_KNEES_PASSAGE_ENTERS_FROM_THE_SOUTH. [CR]
PS_21: ; room_61
6529: 55 C7 DE AF 23 D0 15 7B 14 54 8B 9B 6C 01 B3 59
6539: 90 82 7B 90 14 47 54 B3 9A EB 5B 50 D1 CB 6E 03
6549: A0 46 48 F3 17 0D 8D 3B F4 3B 13 82 17 52 5E E6
6559: 78 2F C6 C6 B5 E3 61 F3 55 8F 49 B3 95 52 45 54
6569: 72 BA 48 F7 17 33 49 AB 98 5F BE 09 15 B6 C3 45
6579: 5E 09 B3 1B 9C 43 13 5A 17 46 48 6B A1 55 A4 09
6589: B7 52 5E F5 B2 26 60 C6 B5 80 A1 14 D0 73 5D 8E
6599: 48 7B 14 3F B9 FA 62 73 49 FF B9 DF 61 91 AF 5B
65A9: 98 E3 8B 0B 5C F7 C5 43 13 49 16 CA CE 8E 48 C3
65B9: B5 33 98 0F 87 4B 62 55 A4 09 B7 47 5E BF 9A 8B
65C9: B3 79 68 56 90 DB 72 47 B9 77 BE 20 00

; YOU_ARE_IN_A_CHAMBER_WHOSE_WALL_CONTAINS_A_PICTURE_OF_A_MAN_____
; WEARING_THE_LUNAR_DISK_ON_HIS_HEAD.__HE_IS_THE_GOD_KHONS,_THE___
; MOON_GOD.[CR]
PS_22: ; room_62
65D6: 2D C7 DE 94 14 4B 5E 83 96 DA 14 64 48 23 62 29
65E6: D1 9B B7 0E D0 05 8A 1E A0 D0 47 C3 B5 E3 16 0F
65F6: 56 5B B1 C3 9E 4F 45 83 48 3B 13 F7 17 33 49 AB
6606: 98 5F BE 4F 16 D4 97 03 15 8B B8 03 A0 95 73 9F
6616: 15 17 47 4A 13 4B 5E D6 B5 DB 72 36 6E 1A 16 1D
6626: A0 16 EE DB 72 4F 13 40 A0 81 15 44 2E 00

; YOU_ARE_IN_A_LONG_SLOPING_CORRIDOR_WITH_RAGGED_WALLS._ [CR]
PS_23: ; room_63
6634: 12 C7 DE 94 14 4B 5E 83 96 49 16 AB 98 C9 B8 90
6644: A5 C5 6A BC A0 09 79 99 AF 82 7B 2B 17 F7 6C 19
6654: 58 46 48 5B BB 20 00

; YOU_ARE_IN_A_CUL-DE-SAC_ABOUT_EIGHT_FEET_ACROSS.[CR]
PS_24: ; room_64
665B: 10 C7 DE 94 14 4B 5E 83 96 E7 14 56 8F A5 63 CB
666B: 46 B9 46 73 C6 C9 60 33 75 67 66 03 BC B9 55 EF
667B: B9 00

; YOU_ARE_IN_THE_CHAMBER_OF_HORUS,_A_LONG_EAST/WEST_PASSAGE_WITH__
; HOLES_EVERYWHERE.__TO_EXPLORE_AT_RANDOM,_SELECT_NORTH,_SOUTH,___
; UP,_OR_DOWN.[CR]
PS_25: ; room_65
667D: 2E C7 DE 94 14 4B 5E 96 96 DB 72 1B 54 AF 91 91
668D: AF 8A 64 BF A0 33 BB 4E 45 11 A0 23 15 F8 B9 B5
669D: D0 12 BC 65 49 77 47 FB 17 53 BE A9 15 F5 8B 38
66AD: 15 43 62 1F D1 7F B1 56 13 C7 9C A6 D8 AF A0 96
66BD: 14 2B 17 49 98 B3 95 AE B7 E6 5F 99 16 C2 B3 15
66CD: EE 36 A1 73 76 57 13 73 A8 A3 A0 89 5B 4E 2E 00

; YOU_ARE_IN_A_LARGE_LOW_CIRCULAR_CHAMBER_WHOSE_FLOOR_IS_AN_______
; IMMENSE_SLAB_FALLEN_FROM_THE_CEILING.__EAST_AND_WEST_THERE_ONCE_
; WHERE_LARGE_PASSAGES,_BUT_THEY_ARE_NOW_FILLED_WITH_SAND.________
; LOW_SMALL_PASSAGES_GO_NORTH_AND_SOUTH.[CR]
PS_26: ; room_66
66DD: 4C C7 DE 94 14 4B 5E 83 96 3B 16 B7 B1 49 16 C5
66ED: CE 2D 7B 3B C5 85 AF 4F 72 74 4D FA 17 D7 A0 56
66FD: 15 44 A0 D5 15 90 14 3B 13 3B 13 CF 15 30 92 9B
670D: B7 BB B8 88 4B 46 48 83 61 79 68 56 90 DB 72 AB
671D: 53 90 8C 5B 70 23 15 F3 B9 8E 48 F7 17 F3 B9 5F
672D: BE 5B B1 0D A0 59 5E F4 72 4E 5E 31 49 52 5E 65
673D: 49 77 47 33 BB F6 4F 82 17 3B 63 2F 49 99 16 C8
674D: CE 46 7A F3 5F 56 D1 15 71 8E 48 3B F4 3B 13 3B
675D: 13 89 8D 5F 17 46 48 DB 16 D3 B9 B5 6C 81 15 99
676D: 16 C2 B3 90 14 15 58 36 A1 48 2E 00

; YOU_ARE_IN_THE_PRIEST'S_BEDROOM.__THE_WALLS_ARE_COVERED_WITH____
; CURTAINS,_THE_FLOOR_WITH_A_THICK_PILE_CARPET.__MOSS_COVERS_THE__
; CEILING.[CR]
PS_27: ; room_72
6779: 2D C7 DE 94 14 4B 5E 96 96 DB 72 F3 A6 66 62 CB
6789: 23 66 4D 01 B3 DB 95 82 17 59 5E 46 48 C3 B5 5B
6799: B1 48 55 2F 62 19 58 82 7B 3B 13 E7 14 BB B3 9D
67A9: 7A 16 EE DB 72 89 67 A3 A0 56 D1 03 71 82 17 DD
67B9: 78 E3 16 DB 8B 14 53 F6 A4 3B F4 C5 93 C5 B5 4F
67C9: A1 8B B3 5F BE 45 13 CE 60 91 7A 2E 00

; THIS_IS_THE_CHAMBER_OF_THE_HIGH_PRIEST.___ANCIENT_DRAWINGS_COVER
; THE_WALLS.__AN_EXTREMELY_TIGHT_TUNNEL_LEADS_WEST.__IT_LOOKS_LIKE
; A_TIGHT_SQUEEZE.__ANOTHER_PASSAGE_LEADS_SE.[CR]
PS_28: ; room_73
67D6: 39 63 BE CB B5 D6 B5 DB 72 1B 54 AF 91 91 AF 96
67E6: 64 DB 72 89 73 12 71 07 B2 17 BA 3B 13 8D 48 30
67F6: 79 06 BC D9 B0 91 7A C5 B5 4F A1 C2 B3 59 5E 46
6806: 48 5B BB 90 14 3A 15 EF BF 2E 92 56 DB 7A 79 16
6816: BC 98 C5 33 61 E3 8B 0B 5C B5 D0 9B C1 D6 15 49
6826: 16 A5 9F 43 16 A3 85 83 17 2E 6D 63 17 27 C4 7F
6836: E3 43 13 06 9A F4 72 DB 16 D3 B9 9B 6C E3 8B 0B
6846: 5C BF B7 00

; YOU_ARE_IN_THE_HIGH_PRIEST'S_TREASURE_ROOM_LIT_BY_AN_EERIE_GREEN
; LIGHT.__A_NARROW_TUNNEL_EXITS_TO_THE_EAST.[CR]
PS_29: ; room_76
684A: 23 C7 DE 94 14 4B 5E 96 96 DB 72 89 73 12 71 07
685A: B2 F5 B9 D6 B5 63 B1 34 BA 54 5E 3F A0 43 16 04
686A: BC 43 DB 87 96 33 62 49 5E 67 B1 83 99 2E 6D 3B
687A: F4 50 45 3C 49 6B A1 70 C0 6E 98 3A 15 8D 7B 89
688A: 17 82 17 47 5E 66 49 2E 00

; YOU_ARE_AT_THE_EAST_END_OF_THE_TWOPIT_ROOM.__THE_FLOOR_HERE_IS__
; LITTERED_WITH_THIN_ROCK_SLABS,_WHICH_MAKE_IT_EASY_TO_DESCEND_THE
; PITS.__THERE_IS_A_PATH_HERE_BYPASSING_THE_PITS_TO_CONNECT_______
; PASSAGES_EAST_AND_WEST.__THERE_ARE_HOLES_ALL_OVER,_BUT_THE_ONLY_
; BIG_ONE_IS_ON_THE_WALL_DIRECTLY_OVER_THE_WEST_PIT_WHERE_YOU_____
; CAN'T_GET_TO_IT.[CR]
PS_2A: ; room_78
6893: 70 C7 DE 94 14 43 5E 16 BC DB 72 95 5F 07 BC 33
68A3: 98 C3 9E 5F BE 91 17 63 A0 14 BC 3F A0 3B F4 5F
68B3: BE 56 15 44 A0 9F 15 5B B1 4B 7B 43 16 3F C0 66
68C3: B1 FB 17 53 BE 63 BE 94 96 5D 9E 5E 17 BD 46 19
68D3: EE 85 73 0F 71 17 48 D6 15 23 15 BB BA 6B BF F5
68E3: 59 B0 53 16 58 F2 72 8D 7B 3B F4 5F BE 5B B1 4B
68F3: 7B 52 45 82 49 9F 15 5B B1 92 50 65 49 91 7A 82
6903: 17 52 5E 8D 7B 89 17 E1 14 CF 99 F3 55 3B 13 3B
6913: 13 55 A4 09 B7 4B 62 95 5F 03 BC 33 98 B5 D0 9B
6923: C1 82 17 2F 62 94 14 4A 5E BF 9F C3 B5 F3 8C 4F
6933: A1 F3 B4 F6 4F 82 17 51 5E 93 99 B3 14 D1 6A 5B
6943: 98 4B 7B 03 A0 5F BE F3 17 F3 8C 94 5A E6 5F FB
6953: 8E 4F A1 96 AF DB 72 B5 D0 12 BC 73 7B 1F D1 5B
6963: B1 C7 DE 3B 13 45 13 85 48 09 BC 73 62 6B BF 97
6973: 7B 00

; YOU_ARE_AT_THE_BOTTOM_OF_THE_EASTERN_PIT_IN_THE_TWOPIT_ROOM.[CR]
PS_2B: ; room_79
6975: 14 C7 DE 94 14 43 5E 16 BC DB 72 06 4F 7F BF B8
6985: 16 82 17 47 5E 66 49 38 62 E3 16 0B BC 96 96 DB
6995: 72 C1 C0 96 A5 39 17 FF 9F 00

; YOU_ARE_AT_THE_WEST_END_OF_THE_TWOPIT_ROOM.__THERE_IS_A_LARGE___
; HOLE_IN_THE_WALL_ABOVE_THE_PIT_AT_THIS_END_OF_THE_ROOM.[CR]
PS_2C: ; room_80
699F: 27 C7 DE 94 14 43 5E 16 BC DB 72 B5 D0 07 BC 33
69AF: 98 C3 9E 5F BE 91 17 63 A0 14 BC 3F A0 3B F4 5F
69BF: BE 5B B1 4B 7B 4E 45 31 49 3B 5E A9 15 DB 8B 83
69CF: 7A 5F BE F3 17 F3 8C B9 46 5B CA 5F BE E3 16 03
69DF: BC 16 BC 95 73 30 15 11 58 96 64 DB 72 01 B3 4D
69EF: 2E 00

; YOU_ARE_AT_THE_BOTTOM_OF_THE_WEST_PIT_IN_THE_TWOPIT_ROOM.__THERE
; IS_A_LARGE_HOLE_IN_THE_WALL_ABOUT_TWENTY_FIVE_FEET_ABOVE_YOU.[CR]
PS_2D: ; room_81
69F1: 29 C7 DE 94 14 43 5E 16 BC DB 72 06 4F 7F BF B8
6A01: 16 82 17 59 5E 66 62 E3 16 0B BC 96 96 DB 72 C1
6A11: C0 96 A5 39 17 FF 9F 56 13 F4 72 D5 60 7B 14 54
6A21: 8B 9B 6C 7E 74 4B 5E 96 96 DB 72 0E D0 03 8A 07
6A31: 4F 16 BC B0 D0 FB C0 18 67 48 5E 36 60 84 14 4F
6A41: A1 51 18 55 2E 00

; YOU_ARE_IN_A_LONG,_NARROW_CORRIDOR_STRETCHING_OUT_OF_SIGHT_TO___
; THE_WEST.__AT_THE_EASTERN_END_IS_A_HOLE_THROUGH_WHICH_YOU_CAN___
; SEE_A_PROFUSION_OF_LEAVES.[CR]
PS_2E: ; room_77
6A47: 33 C7 DE 94 14 4B 5E 83 96 49 16 CE 98 8B 16 79
6A57: B3 C5 CE BC A0 09 79 95 AF EF BF 9A BD 91 7A C7
6A67: 16 11 BC 95 64 7A 79 16 BC BB 9C 82 17 59 5E 66
6A77: 62 3B F4 73 49 5F BE 23 15 FF B9 C3 B2 8E 61 D5
6A87: 15 7B 14 7E 74 56 5E F9 74 7A C4 FA 17 DA 78 51
6A97: 18 45 C2 83 48 55 13 1B 60 52 45 F8 B2 5B C6 03
6AA7: A0 C3 9E E3 8B 75 CA 2E 00

; YOU_ARE_IN_THE_CHAMBER_OF_OSIRIS._THE_CEILING_IS_TOO_HIGH_UP_FOR
; YOUR_LAMP_TO_SHOW_IT.__PASSAGES_LEAD_EAST,_NORTH,_AND_SOUTH.[CR]
PS_2F: ; room_71
6AB0: 29 C7 DE 94 14 4B 5E 96 96 DB 72 1B 54 AF 91 91
6AC0: AF 91 64 54 B8 6F 7B 82 17 45 5E CE 60 91 7A D5
6AD0: 15 89 17 CA 9C 7A 79 B2 17 59 15 91 B4 23 C6 4F
6AE0: 8B 16 A3 D5 9C 89 74 D6 15 3B F4 55 A4 09 B7 4B
6AF0: 62 E3 8B 07 58 66 49 10 EE BE A0 73 76 8E 48 61
6B00: 17 82 C6 2E 00

; THE_PASSAGE_HERE_IS_BLOCKED_BY_A_FALLEN_BLOCK.[CR]
PS_30: ; room_70
6B05: 0F 5F BE DB 16 D3 B9 9B 6C F4 72 4B 5E C4 B5 75
6B15: 8D A6 85 C3 14 7B 14 CE 65 F0 8B B6 14 5D 9E 2E
6B25: 00

; YOU_ARE_IN_THE_CHAMBER_OF_NEKHEBET,_A_WOMAN_WITH_THE_HEAD_OF_A__
; VULTURE,_WEARING_THE_CROWN_OF_EGYPT.__A_PASSAGE_EXITS_TO_THE____
; SOUTH.[CR]
PS_31: ; room_68
6B26: 2C C7 DE 94 14 4B 5E 96 96 DB 72 1B 54 AF 91 91
6B36: AF 90 64 1A 61 AF 5F 73 C1 59 45 E3 9F 99 96 82
6B46: 7B 82 17 4A 5E 86 5F B8 16 7B 14 DF 17 4F 8E 7E
6B56: B1 F7 17 33 49 AB 98 5F BE E4 14 80 A1 B8 16 29
6B66: 15 EE DE 3B F4 52 45 65 49 77 47 3A 15 8D 7B 89
6B76: 17 82 17 3B 5E 55 13 36 A1 48 2E 00

; THERE_IS_A_SHINY_BRASS_LAMP_NEARBY.[CR]
PS_32:
6B82: 0B 5F BE 5B B1 4B 7B 55 45 90 73 44 DB D5 B0 CE
6B92: B5 72 48 8F 16 2C 49 59 2E 00

; BRASS_LANTERN[CR]
PS_33:
6B9C: 04 6B 4F CB B9 50 8B F4 BD 4E 00

; THERE_IS_A_LAMP_SHINING_NEARBY.[CR]
PS_34:
6BA7: 0A 5F BE 5B B1 4B 7B 4E 45 72 48 5A 17 93 7A AB
6BB7: 98 63 98 03 B1 2E 00

; BRASS_LANTERN[CR]
PS_35:
6BBE: 04 6B 4F CB B9 50 8B F4 BD 4E 00

; THERE_IS_A_SMALL_STATUE_BOX_DISCARDED_NEARBY.[CR]
PS_36:
6BC9: 0F 5F BE 5B B1 4B 7B 55 45 8E 91 15 8A 56 BD 1B
6BD9: C4 0A 4F 03 15 53 B7 3F B1 10 58 94 5F 9F 50 00

; STATUE_BOX[CR]
PS_37:
6BE9: 03 FB B9 67 C0 B9 14 58 00

; A_THREE_FOOT_SCEPTER_WITH_AN_ANKH_ON_AN_END_LIES_NEARBY.[CR]
PS_38:
6BF2: 12 56 45 EF 74 48 5E 46 A0 55 17 EE 61 23 62 56
6C02: D1 03 71 83 96 5A 99 C0 16 90 14 30 15 0E 58 35
6C12: 79 8F 16 2C 49 59 2E 00

; SCEPTER[CR]
PS_39:
6C1A: 02 57 B7 3F A7 52 00

; A_STATUE_OF_THE_BIRD_GOD_IS_SITTING_HERE.[CR]
PS_3A:
6C21: 0D 55 45 56 BD 1B C4 C3 9E 5F BE B3 14 33 B1 36
6C31: 6E D5 15 5B 17 43 C0 AB 98 F4 72 45 2E 00

; THERE_IS_A_BIRD_STATUE_IN_THE_BOX.[CR]
PS_3B:
6C3F: 0B 5F BE 5B B1 4B 7B 44 45 2E 7B 66 17 8F 49 4B
6C4F: 5E 96 96 DB 72 0A 4F 2E 00

; BIRD_STATUE_IN_BOX[CR]
PS_3C:
6C58: 06 14 4E 15 58 56 BD 1B C4 83 7A 0A 4F 00

; A_SMALL_VELVET_PILLOW_LIES_ON_THE_FLOOR.[CR]
PS_3D:
6C66: 0D 55 45 8E 91 18 8A 50 61 73 62 8E A5 89 8D 43
6C76: 16 4B 62 03 A0 5F BE 56 15 44 A0 2E 00

; VELVET_PILLOW[CR]
PS_3E:
6C83: 04 6E CA 76 CA E3 16 09 8D 57 00

; A_HUGE_GREEN_FIERCE_SERPENT_BARS_THE_WAY![CR]
PS_3F:
6C8E: 0D 4A 45 77 C4 84 15 30 60 53 15 2D 62 55 5E 3A
6C9E: 62 9E 61 AB 14 8B B3 5F BE F3 17 59 21 00

; A_STONE_BRIDGE_NOW_SPANS_THE_BOTTOMLESS_PIT.[CR]
PS_40:
6CAC: 0E 55 45 80 BF 44 5E 06 B2 9B 6C 09 9A 62 17 9D
6CBC: 48 82 17 44 5E 0E A1 EE 9F 65 62 E3 16 54 2E 00

; THERE_IS_A_SARCOPHAGUS_HERE_WITH_IT'S_COVER_TIGHTLY_CLOSED.[CR]
PS_41:
6CCC: 13 5F BE 5B B1 4B 7B 55 45 2D 49 62 A0 87 47 CA
6CDC: B5 2F 62 FB 17 53 BE 75 7B C5 B5 4F A1 96 AF 7A
6CEC: 79 13 BF DE 14 D7 A0 44 2E 00

; SARCOPHAGUS_>GROAN<[CR]
PS_42:
6CF6: 06 14 B7 42 55 49 72 4B C6 84 2E 10 9E 3C 00

; THERE_ARE_A_FEW_RECENT_ISSUES_OF_"EGYPTIAN_WEEKLY"_MAGAZINE_HERE[CR]
PS_43:
6D05: 15 5F BE 5B B1 2F 49 7B 14 79 66 2F 17 B0 53 0B
6D15: BC E7 B9 4B 62 C3 9E 69 1B EE DE 90 78 F7 17 1E
6D25: 61 63 DB 89 91 73 4A 5B 98 F4 72 45 00

; "EGYPTIAN_WEEKLY"[CR]
PS_44:
6D32: 05 69 1B EE DE 90 78 F7 17 1E 61 59 22 00

; THERE_IS_FOOD_HERE.[CR]
PS_45:
6D40: 06 5F BE 5B B1 4B 7B 01 68 0A 58 2F 62 2E 00

; TASTY_FOOD[CR]
PS_46:
6D4F: 03 55 BD FB C0 01 68 44 00

; THERE_IS_A_BOTTLE_HERE.[CR]
PS_47:
6D58: 07 5F BE 5B B1 4B 7B 44 45 0E A1 DB 8B F4 72 45
6D68: 2E 00

; SMALL_BOTTLE[CR]
PS_48:
6D6A: 04 E3 B8 F3 8C 06 4F FF BE 00

; THERE_IS_WATER_IN_THE_BOTTLE.[CR]
PS_49:
6D74: 09 5F BE 5B B1 4B 7B 16 D0 23 62 83 7A 5F BE B9
6D84: 14 46 C0 45 2E 00

; WATER_IN_THE_BOTTLE[CR]
PS_4A:
6D8A: 06 16 D0 23 62 83 7A 5F BE B9 14 46 C0 45 00

; THERE_IS_A_TINY_PLANT_IN_THE_PIT,_MURMURING_"WATER,_WATER,_..."[CR]
PS_4B:
6D99: 15 5F BE 5B B1 4B 7B 56 45 A3 7A E6 16 9E 48 D0
6DA9: 15 82 17 52 5E 96 7B 77 16 B7 B2 10 B2 BC 6A 16
6DB9: D0 46 62 F3 17 F4 BD 1F EE DC F9 00

; THERE_IS_A_TWELVE_FOOT_BEAN_STALK_STRETCHING_UP_OUT_OF_THE_PIT,_
; BELLOWING_"WATER..._WATER..."[CR]
PS_4C:
6DC5: 1F 5F BE 5B B1 4B 7B 56 45 AE D0 5B CA 01 68 04
6DD5: BC 90 5F 66 17 45 48 66 17 76 B1 23 54 AB 98 D3
6DE5: C5 36 A1 B8 16 82 17 52 5E 96 7B AF 14 09 8D 50
6DF5: D1 BC 6A 16 D0 47 62 DB F9 16 D0 47 62 DC F9 00

; THERE_IS_A_GIGANTIC_BEAN_STALK_STRETCHING_ALL_THE_WAY_UP_TO_THE_
; HOLE.[CR]
PS_4D:
6E05: 17 5F BE 5B B1 4B 7B 49 45 73 79 C3 9A C4 51 90
6E15: 5F 66 17 45 48 66 17 76 B1 23 54 AB 98 46 48 82
6E25: 17 59 5E 3B 4A D3 C5 6B BF 5F BE A9 15 FF 8B 00

; THERE_IS_A_MASSIVE_VENDING_MACHINE_HERE.__THE_INSTRUCTIONS_ON_IT
; READ-_"DROP_COINS_HERE_TO_RECIEVE_FRESH_BATTERIES".[CR]
PS_4E:
6E35: 26 5F BE 5B B1 4B 7B 4F 45 65 49 CF 7B CF 17 43
6E45: 98 AB 98 85 91 90 73 4A 5E 2F 62 3B F4 5F BE D0
6E55: 15 0C BA E6 C3 C0 7A D1 B5 8B 96 EF BF 15 47 6E
6E65: 13 02 B3 E1 14 9D 7A 9F 15 5B B1 6B BF 65 B1 38
6E75: 79 48 5E 75 B1 04 71 8E 49 33 62 4C 62 2E 00

; THERE_ARE_FRESH_BATTERIES_HERE.[CR]
PS_4F:
6E84: 0A 5F BE 5B B1 2F 49 5C 15 5A 62 AB 14 3F C0 07
6E94: B2 CA B5 2F 62 2E 00

; BATTERIES[CR]
PS_50:
6E9B: 03 D6 4C F4 BD 35 79 00

; SOME_WORN-OUT_BATTERIES_HAVE_BEEN_DISCARDED_NEARBY.[CR]
PS_51:
6EA3: 11 3F B9 59 5E B8 A0 47 EB 04 BC 8E 49 33 62 4B
6EB3: 62 58 72 44 5E 30 60 03 15 53 B7 3F B1 10 58 94
6EC3: 5F 9F 50 00

; BATTERIES[CR]
PS_52:
6EC7: 03 D6 4C F4 BD 35 79 00

; THERE_IS_A_LARGE_SPARKLING_NUGGET_OF_GOLD_HERE![CR]
PS_53:
6ECF: 0F 5F BE 5B B1 4B 7B 4E 45 31 49 55 5E 54 A4 C3
6EDF: 86 AB 98 E9 9A B6 6C B8 16 81 15 B3 8B F4 72 45
6EEF: 21 00

; LARGE_GOLD_NUGGET[CR]
PS_54:
6EF1: 05 54 8B 9B 6C 3E 6E 10 58 79 C4 45 54 00

; THERE_ARE_DIAMONDS_HERE![CR]
PS_55:
6EFF: 08 5F BE 5B B1 2F 49 03 15 71 48 4D 98 9F 15 59
6F0F: B1 00

; SEVERAL_DIAMONDS[CR]
PS_56:
6F11: 05 B8 B7 2B 62 06 8A 8F 78 0E A0 53 00

; THERE_ARE_BARS_OF_SILVER_HERE![CR]
PS_57:
6F1E: 0A 5F BE 5B B1 2F 49 AB 14 8B B3 C3 9E 4E B8 74
6F2E: CA 9F 15 59 B1 00

; SILVER_BARS[CR]
PS_58:
6F34: 03 4E B8 74 CA AB 14 52 53 00

; THERE_IS_PRECIOUS_JEWELRY_HERE![CR]
PS_59:
6F3E: 0A 5F BE 5B B1 4B 7B EF A6 51 54 4B C6 79 7F 4C
6F4E: 61 4A DB 2F 62 21 00

; PRECIOUS_JEWELRY[CR]
PS_5A:
6F55: 05 EF A6 51 54 4B C6 79 7F 4C 61 59 00

; THERE_ARE_MANY_COINS_HERE![CR]
PS_5B:
6F62: 08 5F BE 5B B1 2F 49 63 16 7B 9B 3B 55 8B 9A F4
6F72: 72 45 21 00

; RARE_COINS[CR]
PS_5C:
6F76: 03 D4 B0 45 5E 50 9F 53 00

; THE_PHARAOH'S_TREASURE_CHEST_IS_HERE![CR]
PS_5D:
6F7F: 0C 5F BE E2 16 2B 49 15 9F D6 B5 63 B1 34 BA 45
6F8F: 5E F5 72 0B BC CA B5 2F 62 21 00

; TREASURE_CHEST[CR]
PS_5E:
6F9A: 04 EF BF 67 49 5B B1 1F 54 53 54 00

; THERE_IS_A_LARGE_NEST_HERE,_FULL_OF_GOLDEN_EGGS![CR]
PS_5F:
6FA6: 10 5F BE 5B B1 4B 7B 4E 45 31 49 50 5E 66 62 9F
6FB6: 15 7E B1 5F 15 F3 8C C3 9E 3E 6E F0 59 29 15 C9
6FC6: 6E 00

; GOLDEN_EGGS[CR]
PS_60:
6FC8: 03 3E 6E F0 59 29 15 47 53 00

; THERE_IS_A_JEWEL-ENCRUSTED_KEY_HERE![CR]
PS_61:
6FD2: 0C 5F BE 5B B1 4B 7B 4C 45 F7 62 57 8F 24 98 66
6FE2: C6 F3 5F BB 85 9F 15 59 B1 00

; JEWELED_KEY[CR]
PS_62:
6FEC: 03 79 7F 3F 61 0D 58 45 59 00

; THERE_IS_A_DELICATE,_PRECIOUS,_VASE_HERE![CR]
PS_63:
6FF6: 0D 5F BE 5B B1 4B 7B 46 45 43 61 16 53 B3 63 EF
7006: A6 51 54 6E C6 CB 17 9B B7 F4 72 45 21 00

; VASE[CR]
PS_64:
7014: 01 D5 C9 45 00

; THE_VASE_IS_NOW_RESTING,_DELICATELY,_ON_A_VELVET_PILLOW.[CR]
PS_65:
7019: 12 5F BE CB 17 9B B7 4B 7B 09 9A 2F 17 03 BA CE
7029: 98 FF 14 85 8C 7F 49 1E 8F C0 16 7B 14 6E CA 76
7039: CA E3 16 09 8D 57 2E 00

; THE_FLOOR_IS_LITTERED_WITH_WORTHLESS_SHARDS_OF_POTTERY.[CR]
PS_66:
7041: 12 5F BE 56 15 44 A0 D5 15 43 16 3F C0 66 B1 FB
7051: 17 53 BE 44 D2 66 BE 65 62 5A 17 2E 49 D1 B5 92
7061: 64 0E A1 43 62 2E 00

; THERE_IS_AN_EMERALD_HERE_THE_SIZE_OF_A_PLOVER'S_EGG![CR]
PS_67:
7068: 11 5F BE 5B B1 4B 7B 83 48 67 61 CE B0 0A 58 2F
7078: 62 82 17 55 5E 6F 7C B8 16 7B 14 09 A6 74 CA CB
7088: 23 79 60 21 00

; EGG-SIZED_EMERALD[CR]
PS_68:
708D: 05 79 60 DB EB 66 E3 2F 15 2B 62 4C 44 00

; OFF_TO_ONE_SIDE_LIES_A_GLISTENING_PEARL![CR]
PS_69:
709B: 0D D0 9E 89 17 C0 16 55 5E FF 78 43 16 4B 62 49
70AB: 45 95 8C F0 BD 91 7A DF 16 36 49 21 00

; GLISTENING_PEARL[CR]
PS_6A:
70B8: 05 C3 6D FF B9 10 99 D2 6A 94 5F 4C 00

; YOU_ARE_AT_THE_BOTTOM_OF_THE_PIT_WITH_A_BROKEN_NECK.[CR]
PS_6B:
70C5: 11 C7 DE 94 14 43 5E 16 BC DB 72 06 4F 7F BF B8
70D5: 16 82 17 52 5E 73 7B 56 D1 03 71 BC 14 97 9F 90
70E5: 96 DD 5F 2E 00

; THE_CRACK_IS_FAR_TOO_SMALL_FOR_YOU_TO_FOLLOW.[CR]
PS_6C:
70EA: 0F 5F BE E4 14 DD 46 D5 15 4B 15 96 AF 2B A0 E3
70FA: B8 F3 8C 04 68 51 18 56 C2 C8 9C C6 9F 8F A1 00

; THE_DOME_IS_UNCLIMBABLE.[CR]
PS_6D:
710A: 08 5F BE 09 15 1B 92 4B 7B 8D C5 8F 8C C4 4C FF
711A: 8B 00

; I_RESPECTFULLY_SUGGEST_YOU_GO_ACROSS_THE_BRIDGE_INSTEAD_OF______
; JUMPING.[CR]
PS_6E:
711C: 18 54 77 62 62 E6 5F EE 68 FB 8E 29 BA B5 6C 1B
712C: BC 1B A1 2B 6E E4 46 E5 A0 82 17 44 5E 06 B2 9B
713C: 6C 9D 7A E3 BD 11 58 7B 64 3B 13 FF 15 E3 93 CF
714C: 98 00

; YOU_DIDN'T_MAKE_IT.[CR]
PS_6F:
714E: 06 C7 DE 03 15 45 5B 0F BC 17 48 D6 15 2E 00

; THERE_IS_NO_WAY_ACROSS_THE_BOTTOMLESS_PIT.[CR]
PS_70:
715D: 0E 5F BE 5B B1 4B 7B EB 99 1B D0 85 14 05 B3 D6
716D: B5 DB 72 06 4F 7F BF F5 8B D2 B5 97 7B 00

; YOU_CAN'T_GET_BY_THE_SERPENT.[CR]
PS_71:
717B: 09 C7 DE D3 14 E6 96 77 15 04 BC 56 DB DB 72 B4
718B: B7 F0 A4 54 2E 00

; YOU_HAVE_CRAWLED_THROUGH_A_VERY_LOW_WIDE_PASSAGE_PARALLEL_TO_AND
; NORTH_OF_THE_HALL_OF_GODS.[CR]
PS_72:
7191: 1E C7 DE 9B 15 5B CA AB 55 BF D1 16 58 F9 74 7A
71A1: C4 7B 14 74 CA 4E DB 6B A1 46 D1 52 5E 65 49 77
71B1: 47 DB 16 CE B0 EE 8B 89 17 90 14 59 5B C2 B3 B8
71C1: 16 82 17 4A 5E 46 48 B8 16 81 15 2F 5C 00

; YOU_DON'T_FIT_THROUGH_TWO-INCH_SLIT![CR]
PS_73:
71CF: 0C C7 DE 09 15 E6 96 53 15 16 BC F9 74 7A C4 91
71DF: 17 1B A2 1A 98 5E 17 71 7B 00

; YOU_HAVE_CRAWLED_AROUND_IN_SOME_LITTLE_HOLES_AND_WOUND_UP_BACK__
; IN_THE_MAIN_PASSAGE.[CR]
PS_74:
71E9: 1C C7 DE 9B 15 5B CA AB 55 BF D1 03 58 07 B3 33
71F9: 98 83 7A 3F B9 4E 5E 8E 7B DB 8B 7E 74 4B 62 8E
7209: 48 01 18 8E C5 B2 17 AB 14 8B 54 D0 15 82 17 4F
7219: 5E D0 47 DB 16 D3 B9 BF 6C 00

; YOU_HAVE_CRAWLED_AROUND_IN_SOME_LITTLE_HOLES_AND_FOUND_YOUR_WAY_
; BLOCKED_BY_A_FALLEN_SLAB.__YOU_ARE_NOW_BACK_IN_THE_MAIN_PASSAGE.[CR]
PS_75:
7223: 2A C7 DE 9B 15 5B CA AB 55 BF D1 03 58 07 B3 33
7233: 98 83 7A 3F B9 4E 5E 8E 7B DB 8B 7E 74 4B 62 8E
7243: 48 59 15 8E C5 51 18 23 C6 1B D0 B6 14 5D 9E F3
7253: 5F 7B 50 48 45 46 48 83 61 BB B8 1B 51 51 18 43
7263: C2 5B B1 09 9A AB 14 8B 54 83 7A 5F BE 63 16 83
7273: 7A 55 A4 09 B7 45 2E 00

; YOU_CAN'T_FIT_THIS_BIG_SARCOPHAGUS_THROUGH_THAT_LITTLE_PASSAGE![CR]
PS_76:
727B: 15 C7 DE D3 14 E6 96 53 15 16 BC 95 73 B3 14 D5
728B: 6A 2D 49 62 A0 87 47 D6 B5 F9 74 7A C4 82 17 73
729B: 49 96 8C FF BE DB 16 D3 B9 99 6C 00

; SOMETHING_YOU'RE_CARRYING_WON'T_FIT_THROUGH_THE_TUNNEL_WITH_YOU.
; YOU'D_BEST_TAKE_INVENTORY_AND_DROP_SOMETHING.[CR]
PS_77:
72A7: 24 3F B9 82 62 91 7A 51 18 A4 C2 45 5E 3C 49 D0
72B7: DD D9 6A 05 A0 08 BC 73 7B 6C BE 29 A1 16 71 DB
72C7: 72 70 C0 6E 98 FB 17 53 BE C7 DE 51 F9 96 C2 AF
72D7: 14 F3 B9 4D BD 4B 5E 0F 9B C9 9A 7B B4 8E 48 0C
72E7: 15 53 A0 3F B9 82 62 91 7A 2E 00

; YOU_CLAMBER_UP_THE_PLANT_AND_SCURRY_THROUGH_THE_HOLE_AT_THE_TOP.[CR]
PS_78:
72F2: 15 C7 DE DE 14 64 48 23 62 D3 C5 5F BE E6 16 9E
7302: 48 90 14 15 58 34 56 7B B4 6C BE 29 A1 16 71 DB
7312: 72 7E 74 43 5E 16 BC DB 72 82 BF 2E 00

; YOU'VE_CLIMBED_UP_THE_PLANT_AND_OUT_OF_THE_PIT.[CR]
PS_79:
731F: 0F C7 DE 4F 24 DE 14 64 7A F3 5F D3 C5 5F BE E6
732F: 16 9E 48 90 14 11 58 73 C6 C3 9E 5F BE E3 16 54
733F: 2E 00

; THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]
PS_7A:
7341: 0F 5F BE 5B B1 4B 7B EB 99 1B D0 59 15 9B AF 1B
7351: A1 6B BF 2B 6E 5B BE 06 BC 2F 7B 03 56 27 A0 00

; I_DON'T_KNOW_IN_FROM_OUT_HERE.__USE_COMPASS_POINTS.[CR]
PS_7B:
7361: 11 46 77 05 A0 0D BC 09 9A D0 15 5C 15 DB 9F 36
7371: A1 9F 15 7F B1 57 13 9B B7 3F 55 55 A4 D2 B5 50
7381: 9F 2F C0 00

; I_AM_UNSURE_HOW_YOU_ARE_FACING.__USE_COMPASS_POINTS.[CR]
PS_7C:
7385: 11 43 77 57 90 A7 9A 5B B1 89 74 51 18 43 C2 5B
7395: B1 C5 65 91 7A 3B F4 57 C6 E1 14 DB 93 CB B9 7B
73A5: A6 CD 9A 2E 00

; NOTHING_HAPPENS.[CR]
PS_7D:
73AA: 05 06 9A 90 73 CA 6A EA 48 9D 61 2E 00

; I_DON'T_KNOW_HOW.[CR]
PS_7E:
73B7: 05 46 77 05 A0 0D BC 09 9A A9 15 57 2E 00

; I_DON'T_KNOW_HOW_TO_APPLY_THAT_WORD_HERE.[CR]
PS_7F:
73C5: 0D 46 77 05 A0 0D BC 09 9A A9 15 D6 CE C3 9C A6
73D5: A6 56 DB 56 72 01 18 33 B1 F4 72 45 2E 00

; YOUR_LAMP_IS_NOW_ON.[CR]
PS_80:
73E3: 06 C7 DE 8E AF 72 48 D5 15 99 16 D1 CE 4E 2E 00

; YOU_HAVE_NO_SOURCE_OF_LIGHT.[CR]
PS_81:
73F3: 09 C7 DE 9B 15 5B CA EB 99 47 B9 17 B1 B8 16 43
7403: 16 2E 6D 2E 00

; YOUR_LAMP_IS_NOW_OFF.[CR]
PS_82:
7408: 07 C7 DE 8E AF 72 48 D5 15 99 16 D1 CE A7 66 00

; I'M_AS_CONFUSED_AS_YOU_ARE.[CR]
PS_83:
7418: 09 9F 77 95 14 E1 14 9F 98 A6 B7 95 14 51 18 43
7428: C2 7F B1 00

; I_CAN_ONLY_TELL_YOU_WHAT_YOU_SEE_AS_YOU_MOVE_ABOUT_AND__________
; MANIPULATE_THINGS.__I_CAN_NOT_TELL_YOU_WHERE_REMOTE_THINGS_ARE.[CR]
PS_84:
742C: 2A 45 77 83 48 16 A0 56 DB 46 61 51 18 59 C2 56
743C: 72 51 18 55 C2 1B 60 4B 49 C7 DE 71 16 5B CA B9
744C: 46 73 C6 8E 48 3B 13 3B 13 3B 13 63 16 12 99 3B
745C: C5 DB BD 63 BE C5 98 3B F4 45 77 83 48 06 9A 7F
746C: 17 F3 8C C7 DE FA 17 2F 62 2F 17 C6 93 56 5E 90
747C: 73 CB 6E 2F 49 2E 00

; OK_[CR]
PS_85:
7483: 01 8B 9F 00

; SORRY,_BUT_I_NO_LONGER_SEEM_TO_REMEMBER_HOW_IT_WAS_YOU_GOT_HERE.[CR]
PS_86:
7487: 15 44 B9 9E B4 BF 14 0B BC 99 16 49 16 B7 98 95
7497: AF 2F 60 89 17 2F 17 2F 92 74 4D A9 15 CB CE 19
74A7: BC 4B 49 C7 DE 81 15 0A BC 2F 62 2E 00

; YOU_ARE_ALREADY_CARRYING_IT.[CR]
PS_87:
74B4: 09 C7 DE 94 14 43 5E EF 8D 13 47 D3 14 83 B3 91
74C4: 7A D6 15 2E 00

; YOU_CAN'T_CARRY_ANYTHING_MORE.__YOU'LL_HAVE_TO_DROP_SOMETHING___
; FIRST.[CR]
PS_88:
74C9: 17 C7 DE D3 14 E6 96 D3 14 83 B3 90 14 82 DF 91
74D9: 7A 71 16 7F B1 5B 13 1D A1 F3 8C 58 72 56 5E C6
74E9: 9C 02 B3 61 17 36 92 90 73 BB 6A 53 15 A6 B3 2E
74F9: 00

; YOU'RE_NOT_CARRYING_ANYTHING.[CR]
PS_89:
74FA: 09 C7 DE AF 23 99 16 05 BC 3C 49 D0 DD C3 6A 96
750A: 9B 90 73 47 2E 00

; YOU_ARE_CURRENTLY_HOLDING_THE_FOLLOWING:[CR]
PS_8A:
7510: 0D C7 DE 94 14 45 5E 3C C6 9E 61 FB 8E 7E 74 90
7520: 5A D6 6A DB 72 FE 67 89 8D 91 7A 3A 00

; DON'T_BE_RIDICULOUS![CR]
PS_8B:
752D: 06 80 5B F3 23 5B 4D 06 B2 E7 78 87 8D 53 21 00

; YOUR_BOTTLE_IS_EMPTY_AND_THE_GROUND_IS_WET.[CR]
PS_8C:
753D: 0E C7 DE 84 AF 0E A1 DB 8B 4B 7B 72 61 FB C0 8E
754D: 48 82 17 49 5E 07 B3 33 98 4B 7B B6 D0 2E 00

; YOU_CAN'T_POUR_THAT.[CR]
PS_8D:
755C: 06 C7 DE D3 14 E6 96 E9 16 23 C6 5B BE 54 2E 00

; RUBBING_THE_ELECTRIC_LAMP_IS_NOT_PARTICULARLY_REWARDING.________
; ANYWAY,_NOTHING_EXCITING_HAPPENS.[CR]
PS_8E:
756C: 20 E4 B3 10 4E D6 6A DB 72 3F 61 0C 56 CB 78 4F
757C: 8B 0B A3 D0 B5 F3 A0 54 A4 85 BE 3B C5 93 B2 2F
758C: 17 14 D0 90 5A 5B 70 3B 13 3B 13 90 14 F3 DF B3
759C: E0 06 9A 90 73 C7 6A 9B D6 90 BE CA 6A EA 48 9D
75AC: 61 2E 00

; PECULIAR.__NOTHING_UNEXPECTED_HAPPENS.[CR]
PS_8F:
75AF: 0C E5 A4 43 C5 47 49 50 13 02 A1 91 7A B0 17 2A
75BF: 63 E6 5F F3 5F 52 72 F0 A4 53 2E 00

; THERE_IS_NOTHING_HERE_WITH_WHICH_TO_FILL_THE_BOTTLE.[CR]
PS_90:
75CB: 11 5F BE 5B B1 4B 7B 06 9A 90 73 CA 6A 2F 62 FB
75DB: 17 53 BE 23 D1 13 54 6B BF 0E 67 16 8A DB 72 06
75EB: 4F FF BE 2E 00

; THE_BOTTLE_IS_NOW_EMPTY.[CR]
PS_91:
75F0: 08 5F BE B9 14 46 C0 4B 5E D0 B5 6B A1 72 61 1F
7600: C1 00

; YOU_CAN'T_FILL_THAT.[CR]
PS_92:
7602: 06 C7 DE D3 14 E6 96 53 15 F3 8C 5B BE 54 2E 00

; A_GLISTENING_PEARL_FALLS_OUT_OF_THE_SARCOPHAGUS_AND_ROLLS_AWAY._
; THE_SARCOPHAGUS_SNAPS_SHUT_AGAIN.[CR]
PS_93:
7612: 20 49 45 95 8C F0 BD 91 7A DF 16 36 49 4B 15 0D
7622: 8D C7 16 11 BC 96 64 DB 72 14 B7 42 55 49 72 4B
7632: C6 8E 48 39 17 0D 8D 99 14 5F 4A 82 17 55 5E 2D
7642: 49 62 A0 87 47 D5 B5 D2 97 D5 B5 76 75 89 14 D0
7652: 47 2E 00

; I'D_ADVISE_YOU_TO_PUT_DOWN_THE_SARCOPHAGUS_BEFORE_OPENING_IT!![CR]
PS_94:
7655: 14 96 77 86 14 15 CB 5B 5E 1B A1 6B BF 76 A7 09
7665: 15 03 D2 5F BE 53 17 21 B1 5B A5 35 6F AF 14 04
7675: 68 51 5E F0 A4 91 7A D6 15 21 21 00

; THE_SARCOPHAGUS_CREAKS_OPEN,_REVEALING_NOTHING_INSIDE.__IT______
; PROMPTLY_SNAPS_SHUT_AGAIN.[CR]
PS_95:
7681: 1E 5F BE 53 17 21 B1 5B A5 35 6F E4 14 8D 5F D1
7691: B5 F0 A4 14 EE CF 62 43 48 AB 98 06 9A 90 73 CB
76A1: 6A 9B 9A FF 59 4B 13 FB BB 3B 13 EC 16 F2 9F 13
76B1: BF 60 17 ED 48 5A 17 73 C6 73 47 A7 7A 00

; YOU_DON'T_HAVE_ANYTHING_STRONG_ENOUGH_TO_OPEN_THE_SARCOPHAGUS.[CR]
PS_96:
76BF: 14 C7 DE 09 15 E6 96 9B 15 5B CA A3 48 63 BE AB
76CF: 98 0C BA 11 A0 30 15 29 A1 16 71 D1 9C F0 A4 82
76DF: 17 55 5E 2D 49 62 A0 87 47 53 2E 00

; I_DON'T_KNOW_HOW_TO_LOCK_OR_UNLOCK_SUCH_A_THING.[CR]
PS_97:
76EB: 10 46 77 05 A0 0D BC 09 9A A9 15 D6 CE CE 9C 5D
76FB: 9E C4 16 B0 17 75 8D D5 83 DA C3 7B 14 63 BE CF
770B: 98 00

; THE_BIRD_STATUE_IS_NOW_DEAD.__ITS_BODY_DISAPPEARS.[CR]
PS_98:
770D: 10 5F BE B3 14 33 B1 FB B9 67 C0 D5 15 99 16 C6
771D: CE 86 5F 3B F4 8D 7B B9 14 FB 5C 95 5A EA 48 94
772D: 5F 53 2E 00

; THE_STONE_IS_VERY_STRONG_AND_IS_IMPERVIOUS_TO_ATTACK.[CR]
PS_99:
7731: 11 5F BE 66 17 0F A0 D5 15 CF 17 7B B4 0C BA 11
7741: A0 90 14 0B 58 CB B5 DF 93 13 B4 35 A1 89 17 96
7751: 14 45 BD 4B 2E 00

; ATTACKING_THE_SERPENT_BOTH_DOESN'T_WORK_AND_IS_VERY_DANGEROUS.[CR]
PS_9A:
7757: 14 8E 49 DD 46 91 7A 82 17 55 5E 3A 62 9E 61 B9
7767: 14 53 BE 77 5B 05 B9 19 BC B5 A0 90 14 0B 58 D8
7777: B5 43 62 FB 14 B7 98 07 B3 53 2E 00

; YOU_CAN'T_BE_SERIOUS![CR]
PS_9B:
7783: 07 C7 DE D3 14 E6 96 AF 14 57 17 11 B2 49 C6 00

; IT_IS_BEYOND_YOUR_POWER_TO_DO_THAT.[CR]
PS_9C:
7793: 0B 73 7B 4B 7B 7B 4D 0E A0 51 18 23 C6 89 A6 23
77A3: 62 6B BF 6B 5B 5B BE 54 2E 00

; THANK_YOU,_IT_WAS_DELICIOUS![CR]
PS_9D:
77AD: 09 5B BE 4B 99 C7 DE 0B EE 19 BC 4B 49 EE 59 DB
77BD: 78 35 A1 21 00

; I_THINK_I_JUST_LOST_MY_APPETITE.[CR]
PS_9E:
77C2: 0A 56 77 90 73 CB 83 FF 15 F3 B9 85 8D 0F BC 43
77D2: DB 9F A6 96 BE 45 2E 00

; YOU_HAVE_TAKEN_A_DRINK_FROM_THE_STREAM.__THE_WATER_TASTES_______
; STRONGLY_OF_MINERALS,_BUT_IS_NOT_UNPLEASANT.__IT_IS_EXTREMELY___
; COLD.[CR]
PS_9F:
77DA: 2C C7 DE 9B 15 5B CA 4D BD 83 61 46 45 10 B2 C8
77EA: 83 FF B2 82 17 55 5E EF BF 7F 48 56 13 DB 72 16
77FA: D0 23 62 55 BD F5 BD 3B 13 3B 13 66 17 00 B3 D3
780A: 6D B8 16 6B 16 74 98 4D 48 04 EE 73 C6 4B 7B 06
781A: 9A B0 17 FF A5 53 49 D7 9A 4B 13 0B BC C7 B5 4C
782A: D9 67 61 FB 8E 45 13 BE 9F 2E 00

; IT'S_NOT_HUNGRY.__BESIDES,_YOU_HAVE_NO_BIRD_SEED.[CR]
PS_A0:
7835: 10 75 7B D0 B5 F3 A0 70 75 C3 6E 3B F4 75 4D FF
7845: 78 33 BB C7 DE 9B 15 5B CA EB 99 14 4E 15 58 26
7855: 60 2E 00

; YOU_FELL_INTO_A_PIT_AND_BROKE_EVERY_BONE_IN_YOUR_BODY. [CR]
PS_A1:
7858: 12 C7 DE 4F 15 F3 8C 9E 7A C3 9C E3 16 03 BC 33
7868: 98 79 4F 9B 85 CF 62 7B B4 00 4F 4B 5E 9B 96 34
7878: A1 B9 14 1F 5D 20 00

; THE_SERPENT_HAS_NOW_DEVOURED_YOUR_BIRD_STATUE.[CR]
PS_A2:
787F: 0F 5F BE 57 17 1F B3 B3 9A 55 72 99 16 C6 CE D9
788F: 62 2F C6 1B 58 34 A1 B3 14 33 B1 FB B9 67 C0 2E
789F: 00

; THERE_IS_NOTHING_HERE_IT_WANTS_TO_EAT_-_EXCEPT_PERHAPS_YOU.[CR]
PS_A3:
78A0: 13 5F BE 5B B1 4B 7B 06 9A 90 73 CA 6A 2F 62 D6
78B0: 15 F3 17 CD 9A 89 17 23 15 1D BC 3A 15 B2 53 12
78C0: BC 32 62 ED 48 51 18 55 2E 00

; IT_IS_NOW_PITCH_DARK.__IF_YOU_PROCEED,_YOU_WILL_LIKELY_FALL_INTO
; A_PIT.[CR]
PS_A4:
78CA: 17 73 7B 4B 7B 09 9A E3 16 9A BD FB 14 6F B2 4B
78DA: 13 9B 64 1B A1 F9 A6 A7 53 73 5D C7 DE FB 17 F3
78EA: 8C 8D 8C 53 61 4B 15 F3 8C 9E 7A FB 9D 96 A5 2E
78FA: 00

; I'M_GAME.__WOULD_YOU_CARE_TO_EXPLAIN_HOW?[CR]
PS_A5:
78FB: 0D 9F 77 73 15 3F 92 59 13 2E A1 1B 58 1B A1 14
790B: 53 56 5E C7 9C A6 D8 D0 47 A9 15 57 3F 00

; YOUR_LAMP_IS_GETTING_DIM.__YOU'D_BEST_START_WRAPPING_THIS_UP,___
; UNLESS_YOU_CAN_FIND_SOME_FRESH_BATTERIES.__I_SEEM_TO_RECALL_____
; THERE_IS_A_VENDING_MACHINE_IN_THE_MAZE.__BRING_SOME_COINS_WITH__
; YOU.[CR]
PS_A6:
7919: 41 C7 DE 8E AF 72 48 D5 15 77 15 43 C0 AB 98 8F
7929: 5A 3B F4 C7 DE 73 21 75 4D 15 BC 54 BD 19 BC D2
7939: B0 90 A5 D6 6A 95 73 B2 17 FB ED B0 17 F5 8B DB
7949: B5 1B A1 10 53 53 15 33 98 3F B9 48 5E 75 B1 04
7959: 71 8E 49 33 62 6F 62 4B 13 57 17 5B 61 6B BF 65
7969: B1 46 48 3B 13 56 13 F4 72 4B 5E C3 B5 CF 17 43
7979: 98 AB 98 85 91 90 73 4B 5E 96 96 DB 72 9C 91 DB
7989: 63 BC 14 91 7A 61 17 1B 92 3B 55 8B 9A 56 D1 FB
7999: 70 C7 DE 2E 00

; YOUR_LAMP_HAS_RUN_OUT_OF_POWER.[CR]
PS_A7:
799E: 0A C7 DE 8E AF 72 48 9B 15 D4 B5 83 C5 36 A1 B8
79AE: 16 E9 16 B4 D0 2E 00

; THE_PLANT_HAS_EXCEPTIONALLY_DEEP_ROOTS_AND_CANNOT_BE_PULLED_____
; FREE.[CR]
PS_A8:
79B5: 17 5F BE E6 16 9E 48 9B 15 C7 B5 97 D6 43 A7 0B
79C5: A0 13 8D FF 14 D3 61 01 B3 0B C0 8E 48 D3 14 D9
79D5: 99 04 BC 52 5E 46 C5 F3 5F 3B 13 5C 15 3F 60 00

; YOUR_LAMP_IS_GETTING_DIM.__I'M_TAKING_THE_LIBERTY_OF_REPLACING__
; THE_BATTERIES.[CR]
PS_A9:
79E5: 1A C7 DE 8E AF 72 48 D5 15 77 15 43 C0 AB 98 8F
79F5: 5A 3B F4 9F 77 7B 17 50 86 D6 6A DB 72 84 8C 3E
7A05: 62 51 DB 94 64 E6 61 DB 46 AB 98 82 17 44 5E 8E
7A15: 49 33 62 6F 62 00

; AS_YOU_APPROACH_THE_STATUE,_IT_COMES_TO_LIFE_AND_FLIES_ACROSS___
; THE_CHAMBER_WHERE_IT_LANDS_AND_RETURNS_TO_STONE.[CR]
PS_AA:
7A1B: 25 4B 49 C7 DE 92 14 F9 A6 DA 46 82 17 55 5E 56
7A2B: BD 3E C4 D6 15 E1 14 35 92 89 17 43 16 5B 66 8E
7A3B: 48 56 15 35 79 85 14 05 B3 BB B5 82 17 45 5E 4F
7A4B: 72 74 4D FA 17 2F 62 D6 15 3B 16 4D 98 90 14 14
7A5B: 58 8F 62 DD B2 89 17 66 17 0F A0 2E 00

; YOU_CAN_LIFT_THE_STATUE,_BUT_YOU_CANNOT_CARRY_IT.[CR]
PS_AB:
7A68: 10 C7 DE D3 14 8E 96 5E 79 82 17 55 5E 56 BD 3E
7A78: C4 BF 14 1B BC 1B A1 10 53 06 9A D3 14 83 B3 D6
7A88: 15 2E 00

; YOUR_BOTTLE_IS_ALREADY_FULL.[CR]
PS_AC:
7A8B: 09 C7 DE 84 AF 0E A1 DB 8B 4B 7B 4C 48 86 5F 48
7A9B: DB 46 C5 2E 00

; _____SUDDENLY,_A_MUMMY_CREEPS_UP_BEHIND_YOU!!______"I'M_THE_____
; KEEPER_OF_THE_TOMB",__HE_WAILS,_"I_TAKE_THESE_TREASURES_AND_PUT_
; THEM_IN_THE_CHEST_DEEP_IN_THE_MAZE!"__HE_GRABS_YOUR_TREASURE_AND
; VANISHES_INTO_THE_GLOOM.[CR]
PS_AD:
7AA0: 48 3B 13 55 13 FE C3 96 61 B3 E0 4F 45 6F C5 45
7AB0: DB 67 B1 0B A7 D3 C5 6A 4D 8E 7A 51 18 E9 C1 3B
7AC0: 13 3B 13 FD 1B 56 90 DB 72 3B 13 17 16 DF 61 91
7AD0: AF 96 64 DB 72 7F BF C6 4B 4A 13 59 5E CE 47 33
7AE0: BB FB 1B 4D BD 56 5E F5 72 56 5E 63 B1 34 BA 4B
7AF0: 62 8E 48 EF 16 16 BC EF 72 D0 15 82 17 45 5E F5
7B00: 72 06 BC 32 60 D0 15 82 17 4F 5E 6F 4A E3 06 9F
7B10: 15 84 15 BD 46 51 18 23 C6 EF BF 67 49 5B B1 8E
7B20: 48 D0 C9 5A 7B 4B 62 9E 7A D6 9C DB 72 C9 6D FF
7B30: 9F 00

; THE_STONE_BRIDGE_HAS_RETRACTED![CR]
PS_AE:
7B32: 0A 5F BE 66 17 0F A0 BC 14 01 79 4A 5E 4B 49 76
7B42: B1 C5 B0 E6 BD 21 00

; A_STONE_BRIDGE_NOW_SPANS_THE_BOTTOMLESS_PIT.[CR]
PS_AF:
7B49: 0E 55 45 80 BF 44 5E 06 B2 9B 6C 09 9A 62 17 9D
7B59: 48 82 17 44 5E 0E A1 EE 9F 65 62 E3 16 54 2E 00

; THE_VASE_IS_NOW_RESTING,_DELICATELY,_ON_A_VELVET_PILLOW.[CR]
PS_B0:
7B69: 12 5F BE CB 17 9B B7 4B 7B 09 9A 2F 17 03 BA CE
7B79: 98 FF 14 85 8C 7F 49 1E 8F C0 16 7B 14 6E CA 76
7B89: CA E3 16 09 8D 57 2E 00

; THE_VASE_DROPS_WITH_A_DELICATE_CRASH.[CR]
PS_B1:
7B91: 0C 5F BE CB 17 9B B7 F9 5B 0B A7 56 D1 03 71 FF
7BA1: 14 85 8C 7F 49 E4 14 5A 49 2E 00

; THERE_ARE_NOW_SOME_FRESH_BATTERIES_HERE.[CR]
PS_B2:
7BAC: 0D 5F BE 5B B1 2F 49 99 16 D5 CE E7 9F 5C 15 5A
7BBC: 62 AB 14 3F C0 07 B2 CA B5 2F 62 2E 00

; YOU_HAVE_TAKEN_THE_VASE_AND_HURLED_IT_DELICATELY_TO_THE_GROUND.[CR]
PS_B3:
7BC9: 15 C7 DE 9B 15 5B CA 4D BD 83 61 5F BE CB 17 9B
7BD9: B7 8E 48 AF 15 7F B2 0B 58 06 BC 43 61 16 53 53
7BE9: 61 89 17 82 17 49 5E 07 B3 57 98 00

; THE_BIRD_STATUE_COMES_TO_LIFE_AND_ATTACKS_THE_SERPENT_AND_IN_AN_
; ASTOUNDING_FLURRY,_DRIVES_THE_SERPENT_AWAY.__THE_BIRD_TURNS_BACK
; INTO_A_STATUE.[CR]
PS_B4:
7BF5: 2F 5F BE B3 14 33 B1 FB B9 67 C0 E1 14 35 92 89
7C05: 17 43 16 5B 66 8E 48 96 14 45 BD CB 87 5F BE 57
7C15: 17 1F B3 B3 9A 8E 48 D0 15 90 14 95 14 87 BF 43
7C25: 98 AB 98 8F 67 83 B3 06 EE 18 B2 4B 62 5F BE 57
7C35: 17 1F B3 B3 9A F3 49 DB E0 82 17 44 5E 2E 7B 8F
7C45: 17 DD B2 AB 14 9B 54 C9 9A 7B 14 FB B9 67 C0 2E
7C55: 00

; THE_PLANT_SPURTS_INTO_FURIOUS_GROWTH_FOR_A_FEW_SECONDS.[CR]
PS_B5:
7C56: 12 5F BE E6 16 9E 48 62 17 3E C6 CB B5 C9 9A 5F
7C66: 15 11 B2 4B C6 B9 6E 02 D3 59 15 83 AF 4F 15 D5
7C76: CE E1 5F 4D 98 2E 00

; THE_PLANT_GROWS_EXPLOSIVELY,_ALMOST_FILLING_THE_BOTTOM_OF_THE___
; PIT.[CR]
PS_B6:
7C7D: 16 5F BE E6 16 9E 48 84 15 85 A1 3A 15 09 A6 58
7C8D: B8 53 61 03 EE 31 8D F3 B9 0E 67 90 8C D6 6A DB
7C9D: 72 06 4F 7F BF B8 16 82 17 3B 5E E3 16 54 2E 00

; YOU'VE_OVER-WATERED_THE_PLANT!__IT'S_SHRIVELING_UP![CR]
PS_B7:
7CAD: 11 C7 DE 4F 24 C8 16 45 62 16 D0 2F 62 16 58 DB
7CBD: 72 FB A5 B1 9A 4B 13 65 BC 5A 17 18 B2 43 61 AB
7CCD: 98 D1 C5 00

; THERE_IS_NOTHING_HERE_TO_CLIMB.__USE_UP_OR_OUT_TO_LEAVE_THE_PIT.[CR]
PS_B8:
7CD1: 15 5F BE 5B B1 4B 7B 06 9A 90 73 CA 6A 2F 62 89
7CE1: 17 DE 14 64 7A 3B F4 57 C6 B2 17 C4 16 C7 16 16
7CF1: BC CE 9C 98 5F 56 5E DB 72 96 A5 2E 00

; OH_DEAR,_YOU_SEEM_TO_HAVE_GOTTEN_YOURSELF_KILLED.__I_MIGHT_BE___
; ABLE_TO_HELP_YOU_OUT,_BUT_I'VE_NEVER_REALLY_DONE_THIS_BEFORE.___
; DO_YOU_WANT_ME_TO_TRY_TO_REINCARNATE_YOU?[CR]
PS_B9:
7CFE: 38 13 9F E3 59 F3 B4 C7 DE 57 17 5B 61 6B BF 58
7D0E: 72 49 5E 0E A1 83 61 C7 DE 97 B3 03 8C 4E 86 E6
7D1E: 8B 3B F4 4F 77 7A 79 04 BC 3B 5E 84 14 DB 8B 6B
7D2E: BF EE 72 1B A3 1B A1 36 A1 04 EE 73 C6 A8 77 50
7D3E: 5E CF 62 94 AF 8E 5F FB 8E 80 5B 56 5E 95 73 AF
7D4E: 14 04 68 DB 63 46 13 DB 9C 1B A1 10 D0 0F BC 56
7D5E: 5E D6 9C 7B B4 6B BF 6B B1 13 98 CB B2 DB BD C7
7D6E: DE 3F 00

; YOU_CLUMSY_OAF,_YOU'VE_DONE_IT_AGAIN!__I_DON'T_KNOW_HOW_LONG_I__
; CAN_KEEP_THIS_UP.__DO_YOU_WANT_ME_TO_TRY_REINCARNATING_YOU______
; AGAIN?[CR]
PS_BA:
7D71: 2C C7 DE DE 14 75 C5 51 DB 66 47 51 18 A8 C2 46
7D81: 5E 0F A0 D6 15 89 14 D0 47 BB 06 46 77 05 A0 0D
7D91: BC 09 9A A9 15 CE CE 11 A0 BB 15 D3 14 8D 96 32
7DA1: 60 82 17 4B 7B F7 C5 46 13 DB 9C 1B A1 10 D0 0F
7DB1: BC 56 5E D6 9C 7B B4 6B B1 13 98 CB B2 90 BE DB
7DC1: 6A 1B A1 3B 13 43 13 0B 6C 4E 3F 00

; I_SEEM_TO_BE_OUT_OF_ORANGE_SMOKE.__HOW_CAN_I_REINCARNATE_YOU____
; WITHOUT_ORANGE_SMOKE?[CR]
PS_BB:
7DCD: 1C 55 77 2F 60 89 17 AF 14 C7 16 11 BC 91 64 D0
7DDD: B0 9B 6C F1 B8 BF 85 4A 13 6B A1 10 53 BB 15 6B
7DED: B1 13 98 CB B2 DB BD C7 DE 3B 13 FB 17 69 BE 73
7DFD: C6 AB A0 B7 98 5F 17 97 9F 3F 00

; ALL_RIGHT.__BUT_DON'T_BLAME_ME_IF_SOMETHING_GOES_WR.............
; ______________________----__POOF_!!__----_______________________
; YOU_ARE_ENGULFED_IN_A_CLOUD_OF_ORANGE_SMOKE.__COUGHING_AND______
; GASPING,_YOU_EMERGE_FROM_THE_SMOKE.[CR]
PS_BC:
7E08: 4B 46 48 33 17 2E 6D 3B F4 F6 4F 09 15 E6 96 B6
7E18: 14 67 48 67 16 C8 15 61 17 36 92 90 73 C9 6A B5
7E28: 9E 04 18 FF F9 FF F9 FF F9 FF F9 3B F4 3B 13 3B
7E38: 13 3B 13 3B 13 3B 13 3B 13 5D 13 2D ED 52 13 38
7E48: A0 E9 12 5D 13 2D ED 3B 13 3B 13 3B 13 3B 13 3B
7E58: 13 3B 13 3B 13 5B 13 1B A1 2F 49 30 15 2E 6F 66
7E68: 66 D0 15 7B 14 C9 54 F3 C3 C3 9E AB A0 B7 98 5F
7E78: 17 97 9F 3B F4 47 55 23 6D AB 98 8E 48 3B 13 3B
7E88: 13 15 6C 90 A5 33 70 C7 DE 2F 15 31 62 48 5E FF
7E98: B2 82 17 55 5E BD 93 45 2E 00

; OKAY,_NOW_WHERE_DID_I_PUT_MY_ORANGE_SMOKE?..._>POOF!<___________
; EVERYTHING_DISAPPEARS_IN_A_DENSE_CLOUD_OF_ORANGE_SMOKE.[CR]
PS_BD:
7EA2: 27 93 9F B3 E0 09 9A FA 17 2F 62 03 15 0B 58 EF
7EB2: 16 0F BC 51 DB D0 B0 9B 6C F1 B8 98 85 FF F9 F2
7EC2: 13 38 A0 33 07 3B 13 3B 13 3B 13 38 15 43 62 63
7ED2: BE AB 98 95 5A EA 48 94 5F CB B5 83 96 FF 14 97
7EE2: 9A DE 14 26 A1 B8 16 C4 16 91 48 55 5E BD 93 45
7EF2: 2E 00

; READY_CASSETTE[CR]
PS_BE:
7EF4: 04 63 B1 FB 5C 15 53 B6 B7 54 45 00

; CHECKSUM_ERROR[CR]
PS_BF:
7F00: 04 1F 54 A5 54 5B C5 3C 62 4F 52 00

; OH,_NO!__I_LOST_MY_COMPASS.__I_NO_LONGER_SEEM_TO_KNOW_WHICH_WAY_
; IS_NORTH![CR]
PS_C0:
7F0C: 18 36 9F 99 16 BB 06 4E 77 E6 A0 7B 16 E1 14 DB
7F1C: 93 EF B9 4B 13 99 16 49 16 B7 98 95 AF 2F 60 89
7F2C: 17 20 16 6B A1 23 D1 13 54 1B D0 D5 15 99 16 C2
7F3C: B3 21 00

; Unused data on the end. TODO see what this might be.

7F3F: 5e bd 93 45 2e 00 27 93 9f b3
7F49: e0 09 9a fa 17 2f 62 03 15 0b 58 ef 16 0f bc 51
7F59: db d0 b0 9b 6c f1 b8 98 85 ff f9 f2 13 38 a0 33
7F69: 07 3b 13 3b 13 3b 13 38 15 43 62 63 be ab 98 95
7F79: 5A EA 48 94 5f cb b5 38
```

