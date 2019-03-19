![Code](RaakaTu.jpg)

# Raaka Tu Code

>>> cpu 6809

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

 Loaded from cassette at 0x600 (right after text screen memory).
 Executed at 0x0600.

# Start

```code
Start: 
0600: 4F                  CLRA                              ; 256 word (512 bytes on screen)
0601: 8E 04 00            LDX     #$0400                    ; Start of screen
0604: CE 60 60            LDU     #$6060                    ; Space-space
0607: EF 81               STU     ,X++                      ; Clear ...
0609: 4A                  DECA                              ; ... text ...
060A: 26 FB               BNE     $607                      ; ... screen

060C: 10 CE 03 FF         LDS     #$03FF                    ; Stack starts just below screen
0610: 86 1D               LDA     #$1D                      ; Player object ...
0612: B7 01 D2            STA     $01D2                     ; {ram:ACTIVE_OBJ_NUM} ... is the active object number
0615: 8E 05 E0            LDX     #$05E0                    ; Set cursor to ...
0618: 9F 88               STX     <$88                      ; {ram:printCursor} ... bottom row of screen
061A: C6 96               LDB     #$96                      ; Starting ...
061C: F7 01 D5            STB     $01D5                     ; {ram:CUR_ROOM} ... room
061F: 8E 15 23            LDX     #$1523                    ; Room descriptions
0622: BD 0A 1F            JSR     $0A1F                     ; {FindSublist} Find room data
0625: BF 01 D6            STX     $01D6                     ; {ram:CUR_ROOM_DATA} Store current room data
0628: BD 0D 4A            JSR     $0D4A                     ; Print room description
062B: 86 0D               LDA     #$0D                      ; Print ...
062D: BD 11 84            JSR     $1184                     ; {PrintCharacterAutoWrap} ... CR
```

# Main Loop

```code
MainLoop: 
0630: 10 CE 03 FF         LDS     #$03FF                    ; Initialize stack
0634: BD 0A CC            JSR     $0ACC                     ; Get user input

0637: 7F 01 B7            CLR     $01B7                     ; {ram:adjWord} Adjective word number
063A: 7F 01 BA            CLR     $01BA                     ; {ram:lsbAdj1} LSB of 1st adjective in buffer (not used)
063D: 7F 01 BB            CLR     $01BB                     ; {ram:lsbVerb} LSB of verb
0640: 7F 01 B2            CLR     $01B2                     ; {ram:tmp1B2} Misc
0643: 7F 01 B3            CLR     $01B3                     ; {ram:verbWord} Verb word number
0646: 7F 01 B9            CLR     $01B9                     ; {ram:not1B9} Never used again
0649: 7F 01 B8            CLR     $01B8                     ; {ram:commandTarg} Target object of command (not used)
064C: 7F 01 B4            CLR     $01B4                     ; {ram:perpWord} Preposition number
064F: 7F 01 B5            CLR     $01B5                     ; {ram:prepGiven} Preposition given flag (not 0 if given)
0652: 7F 01 BF            CLR     $01BF                     ; {ram:VAR_OBJ_NUMBER} VAR object number
0655: 7F 01 C3            CLR     $01C3                     ; {ram:FIRST_NOUN_NUM} 1st noun word number
0658: 7F 01 C9            CLR     $01C9                     ; {ram:SECOND_NOUN_NUM} 2nd noun word number

065B: C6 1D               LDB     #$1D                      ; Player object ...
065D: F7 01 D2            STB     $01D2                     ; {ram:ACTIVE_OBJ_NUM} ... is active object
0660: BD 11 33            JSR     $1133                     ; Get player object data
0663: BF 01 D3            STX     $01D3                     ; {ram:ACTIVE_OBJ_DATA} Active object's data
0666: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip length
0669: E6 84               LDB     ,X                        ; Get player location
066B: F7 01 D5            STB     $01D5                     ; {ram:CUR_ROOM} Current room
066E: 8E 15 23            LDX     #$1523                    ; Room scripts
0671: BD 0A 1F            JSR     $0A1F                     ; {FindSublist} Find sublist ... script for room
0674: BF 01 D6            STX     $01D6                     ; {ram:CUR_ROOM_DATA} Script for current room
0677: 8E 01 E3            LDX     #$01E3                    ; Input token list area
067A: BF 01 D8            STX     $01D8                     ; {ram:nextToken} Where decoder fills in
067D: 6F 84               CLR     ,X                        ; Empty token ... clear the list
067F: 8E 05 E0            LDX     #$05E0                    ; Bottom row is input buffer
0682: BD 0B 42            JSR     $0B42                     ; Decode input word
0685: 27 0B               BEQ     $692                      ; All words done
0687: A6 80               LDA     ,X+                       ; Next character
0689: 81 60               CMPA    #$60                      ; A space?
068B: 27 F5               BEQ     $682                      ; Yes ... decode next
068D: 8C 06 00            CMPX    #$0600                    ; End of input buffer?
0690: 26 F5               BNE     $687                      ; No ... look for next word
0692: 8C 06 00            CMPX    #$0600                    ; End of input buffer?
0695: 26 EB               BNE     $682                      ; No ... keep looking
0697: 6F 9F 01 D8         CLR     [$01D8]                   ; {ram:nextToken} Terminate token list
069B: 8E 01 E3            LDX     #$01E3                    ; Input buffer
069E: A6 84               LDA     ,X                        ; List number of first word
06A0: 10 27 00 92         LBEQ    $0736                     ; Nothing entered
06A4: 81 02               CMPA    #$02                      ; First word a noun?
06A6: 26 0F               BNE     $6B7                      ; No ... move on
06A8: 30 01               LEAX    1,X                       ; Point to word number
06AA: A6 84               LDA     ,X                        ; Get word number
06AC: 30 1F               LEAX    -1,X                      ; Back to list number
06AE: 81 06               CMPA    #$06                      ; Living things (people, dogs, etc) are <6
06B0: 24 05               BCC     $6B7                      ; Not a living thing
06B2: B7 01 B8            STA     $01B8                     ; {ram:commandTarg} Remember living thing. We are giving them a command so process normally
06B5: 30 03               LEAX    3,X                       ; Next word

06B7: A6 80               LDA     ,X+                       ; Word list
06B9: 27 7B               BEQ     $736                      ; End of list ... go process
06BB: E6 84               LDB     ,X                        ; Word number to B
06BD: EE 81               LDU     ,X++                      ; LSB to LSB of U
06BF: 34 10               PSHS    X                         ; Hold token buffer
06C1: 4A                  DECA                              ; List 1? Verbs?
06C2: 26 21               BNE     $6E5                      ; No ... continue
```

I believe the goal here was to allow multiple verbs given on an input line
to be translated to a single verb. The code finds a replacement list for the
newly given verb and then runs the list two bytes at a time comparing one
of the entries to the last given verb and storing the second byte if there
is a match. I believe that is what is SUPPOSED to happen, but I believe the
code has a bug or two. It actually does nothing at all. The replacement
list for BEDLAM and RAAKATU is empty so the code is never used anyway.

```code
06C4: 8E 13 32            LDX     #$1332                    ;  Multi verb translation list (empty list for BEDLAM and RAAKATU)
06C7: BD 0A 1F            JSR     $0A1F                     ; {FindSublist} Look for an entry for the given verb
06CA: 24 13               BCC     $6DF                      ; No entry ... use the word as-is
06CC: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip length of entry
06CF: BD 0A 58            JSR     $0A58                     ; {CompareXY} End of list?
06D2: 1F 98               TFR     B,A                       ;  ?? Held in A but ...
06D4: 24 09               BCC     $6DF                      ; Reached end of list. This input is the verb.
06D6: E6 80               LDB     ,X+                       ;  ??
06D8: A6 80               LDA     ,X+                       ;  ?? ... A is mangled here?
06DA: F1 01 B3            CMPB    $01B3                     ; {ram:verbWord} ?? Compare to 01B3 ...
06DD: 26 F0               BNE     $6CF                      ; Continue running list
06DF: F7 01 B3            STB     $01B3                     ; {ram:verbWord} ?? ... then store if equal?
06E2: 7E 07 31            JMP     $0731                     ; Continue with next word

06E5: 4A                  DECA                              ;  List 2 Noun
06E6: 26 36               BNE     $71E                      ; Not a noun
06E8: 7D 01 B5            TST     $01B5                     ; {ram:prepGiven} Has prepostion been given?
06EB: 27 20               BEQ     $70D                      ; No ... this is first noun
06ED: 8E 01 C9            LDX     #$01C9                    ;  2nd noun area
06F0: E7 80               STB     ,X+                       ;  Store word number
06F2: B6 01 B7            LDA     $01B7                     ; {ram:adjWord} Last adjective
06F5: A7 80               STA     ,X+                       ;  Keep with noun
06F7: B6 01 BA            LDA     $01BA                     ; {ram:lsbAdj1} LSB of adjective
06FA: A7 84               STA     ,X                        ;  Keep with noun
06FC: 26 04               BNE     $702                      ; There was one ... go on
06FE: 1F 30               TFR     U,D                       ;  Use LSB of ...
0700: E7 84               STB     ,X                        ;  ... noun if no adjective
0702: 7F 01 B7            CLR     $01B7                     ; {ram:adjWord} Adjective moved
0705: 7F 01 B5            CLR     $01B5                     ; {ram:prepGiven} Preposition moved
0708: 7F 01 BA            CLR     $01BA                     ; {ram:lsbAdj1} LSB moved
070B: 20 24               BRA     $731                      ; Continue with next word

070D: BE 01 C3            LDX     $01C3                     ; {ram:FIRST_NOUN_NUM} Copy ...
0710: BF 01 C9            STX     $01C9                     ; {ram:SECOND_NOUN_NUM} ... any ...
0713: BE 01 C5            LDX     $01C5                     ; {ram:firstNounLSB} ... first noun ...
0716: BF 01 CB            STX     $01CB                     ; {ram:secondNounLSB} ... to second
0719: 8E 01 C3            LDX     #$01C3                    ;  First word area
071C: 20 D2               BRA     $6F0                      ; Go fill out first word

071E: 4A                  DECA                              ;  List 3 Adjective
071F: 26 0A               BNE     $72B                      ; Not a proposition
0721: F7 01 B7            STB     $01B7                     ; {ram:adjWord} Store adjective number
0724: 1F 30               TFR     U,D                       ;  Store ...
0726: F7 01 BA            STB     $01BA                     ; {ram:lsbAdj1} ... adjective LSB in buffer
0729: 20 06               BRA     $731                      ; Continue with next word

072B: F7 01 B4            STB     $01B4                     ; {ram:perpWord} Preposition
072E: F7 01 B5            STB     $01B5                     ; {ram:prepGiven} Preoposition given (noun should follow)
0731: 35 10               PULS    X                         ;  Restore token pointer
0733: 7E 06 B7            JMP     $06B7                     ; Next word


0736: 7D 01 B3            TST     $01B3                     ; {ram:verbWord} Verb given?
0739: 10 27 02 58         LBEQ    $0995                     ; No ... ?VERB? error
073D: 8E 01 C9            LDX     #$01C9                    ;  Second noun
0740: BD 08 22            JSR     $0822                     ; Decode it (only returns if OK)
0743: B7 01 C9            STA     $01C9                     ; {ram:SECOND_NOUN_NUM} Hold target object index
0746: BF 01 CC            STX     $01CC                     ; {ram:SECOND_NOUN_DATA} Hold target object pointer
0749: 8E 01 C3            LDX     #$01C3                    ;  First noun
074C: BD 08 22            JSR     $0822                     ; Decode it (only returns if OK)
074F: B7 01 C3            STA     $01C3                     ; {ram:FIRST_NOUN_NUM} Hold target object index
0752: BF 01 C6            STX     $01C6                     ; {ram:FIRST_NOUN_DATA} Hold target object pointer
0755: 7F 01 B5            CLR     $01B5                     ; {ram:prepGiven} Clear preposition flag

0758: BE 01 C6            LDX     $01C6                     ; {ram:FIRST_NOUN_DATA} Pointer to first noun object data
075B: B6 01 C3            LDA     $01C3                     ; {ram:FIRST_NOUN_NUM} First noun index
075E: 27 07               BEQ     $767                      ; No first noun ... store a 0
0760: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip ID and load end
0763: 30 02               LEAX    2,X                       ;  Skip 2 bytes
0765: A6 84               LDA     ,X                        ;  Object parameter bits
0767: B7 01 C8            STA     $01C8                     ; {ram:firstNounParams} Hold first noun's parameter bits

076A: BE 01 CC            LDX     $01CC                     ; {ram:SECOND_NOUN_DATA} Pointer to second noun object data
076D: B6 01 C9            LDA     $01C9                     ; {ram:SECOND_NOUN_NUM} Second noun number
0770: 27 07               BEQ     $779                      ; No second noun ... store 0
0772: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip ID and load end
0775: 30 02               LEAX    2,X                       ;  Skip 2 bytes
0777: A6 84               LDA     ,X                        ;  Object parameter bits
0779: B7 01 CE            STA     $01CE                     ; {ram:secondNounParams} Hold second noun's parameter bits

077C: 8E 13 5B            LDX     #$135B                    ;  Syntax list
077F: A6 84               LDA     ,X                        ;  End of list?
0781: 10 27 01 CC         LBEQ    $0951                     ; Yes ... "?PHRASE?"
0785: B6 01 B3            LDA     $01B3                     ; {ram:verbWord} Verb ...
0788: A1 80               CMPA    ,X+                       ;  ... matches?
078A: 26 5B               BNE     $7E7                      ; No ... move to next entry
078C: A6 84               LDA     ,X                        ;  Phrase's proposition
078E: B7 01 B6            STA     $01B6                     ; {ram:phrasePrep} Hold it
0791: B6 01 B4            LDA     $01B4                     ; {ram:perpWord} Preposition word number
0794: 27 04               BEQ     $79A                      ; None given ... skip prep check
0796: A1 84               CMPA    ,X                        ;  Given prep matches?
0798: 26 4D               BNE     $7E7                      ; No ... move to next phrase
079A: 30 01               LEAX    1,X                       ;  Skip to next phrase component
079C: A6 84               LDA     ,X                        ;  First noun required by phrase
079E: 27 14               BEQ     $7B4                      ; Not given in phrase ... skip check
07A0: B6 01 C3            LDA     $01C3                     ; {ram:FIRST_NOUN_NUM} 1st noun index
07A3: 26 16               BNE     $7BB                      ; Requested by phrase but not given by user ... next phrase
07A5: B6 01 BB            LDA     $01BB                     ; {ram:lsbVerb} LSB of verb ...
07A8: B7 01 BD            STA     $01BD                     ; {ram:lsbError} ... to location of error
07AB: 10 8E 01 C3         LDY     #$01C3                    ;  Descriptor for 1st noun
07AF: BD 08 D2            JSR     $08D2                     ; Decode 1st noun as per phrase
07B2: 20 07               BRA     $7BB                      ; We just processed a first one. We know it is there.
07B4: B6 01 C3            LDA     $01C3                     ; {ram:FIRST_NOUN_NUM} Is there a 1st noun?

07B7: 10 26 01 96         LBNE    $0951                     ; No ... next entry
07BB: 30 01               LEAX    1,X                       ; Next in phrase
07BD: A6 84               LDA     ,X                        ; Phrase wants a second noun?
07BF: 27 19               BEQ     $7DA                      ; No ... skip
07C1: B6 01 C9            LDA     $01C9                     ; {ram:SECOND_NOUN_NUM} User given 2nd noun
07C4: 26 1B               BNE     $7E1                      ; Yes ... use this phrase
07C6: B6 01 BC            LDA     $01BC                     ; {ram:lsbCursor} Location of ...
07C9: B7 01 BD            STA     $01BD                     ; {ram:lsbError} ... error on screen
07CC: 86 01               LDA     #$01                      ; Set preposition ...
07CE: B7 01 B5            STA     $01B5                     ; {ram:prepGiven} ... flag to YES
07D1: 10 8E 01 C9         LDY     #$01C9                    ; 2nd noun index
07D5: BD 08 D2            JSR     $08D2                     ; Decode 2nd noun as per phrase
07D8: 20 07               BRA     $7E1                      ; Use this

07DA: B6 01 C9            LDA     $01C9                     ; {ram:SECOND_NOUN_NUM} Is there a second noun?
07DD: 10 26 01 70         LBNE    $0951                     ; No ... phrase error
07E1: 30 01               LEAX    1,X                       ; Get matched ...
07E3: A6 84               LDA     ,X                        ; ... phrase number
07E5: 20 09               BRA     $7F0                      ; Store and continue
07E7: 30 01               LEAX    1,X                       ; Skip ...
07E9: 30 01               LEAX    1,X                       ; ... to ...
07EB: 30 02               LEAX    2,X                       ; ... next entry
07ED: 7E 07 7F            JMP     $077F                     ; Keep looking

; Unlike BEDLAM, there is no giving a command to something else. Just
; ignore any commanded object and give the phrase to the user.

07F0: B7 01 D1            STA     $01D1                     ; {ram:PHRASE_FORM} Store the phrase number
07F3: 8E 05 FF            LDX     #$05FF                    ; Move cursor to ...
07F6: 9F 88               STX     <$88                      ; {ram:printCursor} ... end of line
07F8: 86 0D               LDA     #$0D                      ; Print ...
07FA: BD 11 84            JSR     $1184                     ; {PrintCharacterAutoWrap} ... CR
07FD: B6 01 C3            LDA     $01C3                     ; {ram:FIRST_NOUN_NUM} First noun given?
0800: 26 0C               BNE     $80E                      ; Yes ... keep what we have
0802: BE 01 CC            LDX     $01CC                     ; {ram:SECOND_NOUN_DATA} Move 2nd ...
0805: BF 01 C6            STX     $01C6                     ; {ram:FIRST_NOUN_DATA} ... noun to ...
0808: B6 01 C9            LDA     $01C9                     ; {ram:SECOND_NOUN_NUM} ... first ...
080B: B7 01 C3            STA     $01C3                     ; {ram:FIRST_NOUN_NUM} ... descriptor
080E: 8E 32 3C            LDX     #$323C                    ; General command scripts
0811: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip over end delta
0814: BD 0C 03            JSR     $0C03                     ; {ProcessCommand} Execute script
0817: BD 0F 66            JSR     $0F66                     ; Allow objects to move
081A: 86 0D               LDA     #$0D                      ; Print ...
081C: BD 11 84            JSR     $1184                     ; {PrintCharacterAutoWrap} ... CR
081F: 7E 06 30            JMP     $0630                     ; {MainLoop} Top of game loop

; This function decodes the NOUN descriptor pointed to by X. The AJECTIVE-NOUN
; pair is compared to all objects in the room (and pack). If no adjective
; is given and there are multiple matching objects (like multiple doors with
; different colors) then the "?WHICH?" prompt is given. If there is no 
; matching object then "?WHAT?" is given. If this function returns then
; the mapping was successful.
;
; @param X pointer to the noun descriptor to decode[[br]]
; @return A index of target object[[br]]
; @return X pointer to target object data[[br]]

0822: 7F 01 BF            CLR     $01BF                     ; {ram:VAR_OBJ_NUMBER} Input object number
0825: E6 80               LDB     ,X+                       ; Word number of noun
0827: F7 01 B2            STB     $01B2                     ; {ram:tmp1B2} Hold it
082A: 26 02               BNE     $82E                      ; Real object ... go decode
082C: 4F                  CLRA                              ; Not found
082D: 39                  RTS                               ; Out
082E: A6 80               LDA     ,X+                       ; Noun's adjective
0830: B7 01 B7            STA     $01B7                     ; {ram:adjWord} Hold it
0833: A6 84               LDA     ,X                        ; LSB of word in buffer
0835: B7 01 CF            STA     $01CF                     ; {ram:tmp1CF} Hold it
0838: 8E 20 FF            LDX     #$20FF                    ; Object data
083B: BD 0A 1F            JSR     $0A1F                     ; {FindSublist} Get pointer to next object that matches word
083E: 24 5A               BCC     $89A                      ; Not found
0840: 34 20               PSHS    Y                         ; Hold end of object data
0842: 34 10               PSHS    X                         ; Hold pointer to noun descriptor
0844: B6 01 E1            LDA     $01E1                     ; {ram:tmp1E1} Index of object in the object list
0847: B7 01 E2            STA     $01E2                     ; {ram:tmp1E2} Remember this
084A: BD 08 AA            JSR     $08AA                     ; Is object in this room or on player?
084D: 26 57               BNE     $8A6                      ; No ... can't be target ... out
084F: B6 01 B7            LDA     $01B7                     ; {ram:adjWord} Noun's adjective
0852: 27 1F               BEQ     $873                      ; No adjective ... skip this
0854: 35 10               PULS    X                         ; Restore pointer to noun descriptor
0856: 34 10               PSHS    X                         ; Hold it again
0858: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip the id and end
085B: 30 03               LEAX    3,X                       ; Skip the object data
085D: C6 01               LDB     #$01                      ; Look up adjective ...
085F: BD 0A 27            JSR     $0A27                     ; ... list for object
0862: 24 0F               BCC     $873                      ; No adjective ... ignore
0864: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip the id and length
0867: BD 0A 58            JSR     $0A58                     ; {CompareXY} End of adjective list?
086A: 24 3A               BCC     $8A6                      ; Yes ... no match ... next object
086C: B6 01 B7            LDA     $01B7                     ; {ram:adjWord} Adjective
086F: A1 80               CMPA    ,X+                       ; In this list?
0871: 26 F4               BNE     $867                      ; No ... keep searching list
0873: 35 10               PULS    X                         ; Restore object pointer
0875: B6 01 BF            LDA     $01BF                     ; {ram:VAR_OBJ_NUMBER} Last object index that matched
0878: 10 26 01 10         LBNE    $098C                     ; Multiple matches ... do "?WHICH?"
087C: B6 01 E2            LDA     $01E2                     ; {ram:tmp1E2} Object index
087F: B7 01 BF            STA     $01BF                     ; {ram:VAR_OBJ_NUMBER} Current guess at matching object index
0882: BF 01 C0            STX     $01C0                     ; {ram:VAR_OBJ_DATA} Input object data
0885: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip id and end
0888: 1F 21               TFR     Y,X                       ; Next object
088A: 35 20               PULS    Y                         ; End of object data
088C: F6 01 B2            LDB     $01B2                     ; {ram:tmp1B2} Restore word number of noun
088F: B6 01 E2            LDA     $01E2                     ; {ram:tmp1E2} Current object index
0892: B7 01 E1            STA     $01E1                     ; {ram:tmp1E1} Start count for next pass
0895: BD 0A 27            JSR     $0A27                     ; Find next matching object
0898: 25 A6               BCS     $840                      ; Got one ... go test it
089A: BE 01 C0            LDX     $01C0                     ; {ram:VAR_OBJ_DATA} Object data to X
089D: B6 01 BF            LDA     $01BF                     ; {ram:VAR_OBJ_NUMBER} Object found?
08A0: 26 03               BNE     $8A5                      ; Yes ...  out
08A2: 7E 09 48            JMP     $0948                     ; No ... "?WHAT?"
08A5: 39                  RTS                               ; Done
08A6: 35 10               PULS    X                         ; Restore object pointer
08A8: 20 DB               BRA     $885                      ; Do next object

; This function checks if the target object is in the current room or being
; held by the active object.

; @param X pointer to target object[[br]]
; @return Z=1 for yes or Z=0 for no

08AA: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip size
08AD: B6 01 D5            LDA     $01D5                     ; {ram:CUR_ROOM} Current room number
08B0: A1 84               CMPA    ,X                        ; Is object in room?
08B2: 27 F1               BEQ     $8A5                      ; Yes ... return OK
08B4: A6 84               LDA     ,X                        ; Get object's room number
08B6: 27 17               BEQ     $8CF                      ; 0 ... fail
08B8: 81 FF               CMPA    #$FF                      ; FF ...
08BA: 27 E9               BEQ     $8A5                      ; ... return OK
08BC: 85 80               BITA    #$80                      ; Upper bit of object location set ...
08BE: 26 0F               BNE     $8CF                      ; ... then fail
08C0: E6 84               LDB     ,X                        ; Location again
08C2: F1 01 D2            CMPB    $01D2                     ; {ram:ACTIVE_OBJ_NUM} Being held by the active object?
08C5: 27 DE               BEQ     $8A5                      ; Yes ... return OK
08C7: 8E 20 FF            LDX     #$20FF                    ; Strange. 117D does this too.
08CA: BD 11 33            JSR     $1133                     ; Get object's container object (if any)
08CD: 20 DB               BRA     $8AA                      ; Repeat check
08CF: 8A 01               ORA     #$01                      ; Mark failure
08D1: 39                  RTS                               ; Out

; This function fills the noun descriptor pointed to by Y with the object
; in current room or on user that matches the parameter value from the
; phrase script. If there is not exactly one such object then flash an error
; like "WITH ?WHAT?" using the current preposition or just "?WHAT?" if there
; isn't one.
;
; @param Y pointer to noun descriptor to fill[[br]]
; @param X pointer to phrase data[[br]]
; @return descriptor filled out with object

08D2: 34 10               PSHS    X                         ; Hold phrase data pointer
08D4: 7F 01 B2            CLR     $01B2                     ; {ram:tmp1B2} Found word flag
08D7: 7F 01 E1            CLR     $01E1                     ; {ram:tmp1E1} Object index starts at 0
08DA: 34 20               PSHS    Y                         ; Hold noun descriptor
08DC: A6 84               LDA     ,X                        ; Object parameter mask bits
08DE: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Hold
08E1: 8E 20 FF            LDX     #$20FF                    ; Object data
08E4: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip ID and load end
08E7: BD 0A 58            JSR     $0A58                     ; {CompareXY} At end of object data?
08EA: 24 40               BCC     $92C                      ; Yes ... done
08EC: 7C 01 E1            INC     $01E1                     ; {ram:tmp1E1} Bump object index
08EF: 34 20               PSHS    Y                         ; Hold end of object
08F1: 34 10               PSHS    X                         ; Hold pointer to object
08F3: BD 08 AA            JSR     $08AA                     ; Is object in room or on player?
08F6: 35 10               PULS    X                         ; Restore pointer to object
08F8: 26 2D               BNE     $927                      ; No ... next object
08FA: E6 84               LDB     ,X                        ; Object word number
08FC: BF 01 D8            STX     $01D8                     ; {ram:nextToken} Pointer to object data
08FF: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip ID and load end
0902: 30 02               LEAX    2,X                       ; Point to object parameters
0904: A6 84               LDA     ,X                        ; Get parameters
0906: B4 01 AB            ANDA    $01AB                     ; {ram:tmp1AB} Compare to phrase data ...
0909: B1 01 AB            CMPA    $01AB                     ; {ram:tmp1AB} ... this is a strange way to do it
090C: 26 13               BNE     $921                      ; Not a match ... next word
090E: B6 01 B2            LDA     $01B2                     ; {ram:tmp1B2} Already got a word number?
0911: 26 47               BNE     $95A                      ; Yes ... error
0913: F7 01 B2            STB     $01B2                     ; {ram:tmp1B2} Found word number
0916: A6 84               LDA     ,X                        ; Remember ...
0918: B7 01 B7            STA     $01B7                     ; {ram:adjWord} ... object parameters
091B: BE 01 D8            LDX     $01D8                     ; {ram:nextToken} Remember ...
091E: BF 01 AD            STX     $01AD                     ; {ram:tmp1AD} ... object pointer
0921: 1E 12               EXG     X,Y                       ; Start of next object to X
0923: 35 20               PULS    Y                         ; Restore end of object pointer
0925: 20 C0               BRA     $8E7                      ; Continue with next object
0927: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip ID and load end
092A: 20 F5               BRA     $921                      ; Try next object
092C: B6 01 B2            LDA     $01B2                     ; {ram:tmp1B2} Did we find an object word?
092F: 27 29               BEQ     $95A                      ; No .... error
0931: 35 20               PULS    Y                         ; Noun descriptor
0933: BE 01 AD            LDX     $01AD                     ; {ram:tmp1AD} Object data pointer
0936: B6 01 E1            LDA     $01E1                     ; {ram:tmp1E1} New ...
0939: A7 A4               STA     ,Y                        ; ... object number
093B: 31 23               LEAY    3,Y                       ; New ...
093D: AF A1               STX     ,Y++                      ; ... pointer to object data
093F: B6 01 B7            LDA     $01B7                     ; {ram:adjWord} New ...
0942: A7 A4               STA     ,Y                        ; ... object parameters
0944: 35 10               PULS    X                         ; Restore phrase data pointer
0946: 4F                  CLRA                              ; Set Z=1
0947: 39                  RTS                               ; Done

0948: 10 8E 13 43         LDY     #$1343                    ; "?WHAT?"
094C: B6 01 CF            LDA     $01CF                     ; {ram:tmp1CF} LSB of screen location
094F: 20 4A               BRA     $99B                      ; Go flash error and try again

0951: 10 8E 13 52         LDY     #$1352                    ; "?PHRASE?"
0955: B6 01 BC            LDA     $01BC                     ; {ram:lsbCursor} LSB of screen location
0958: 20 41               BRA     $99B                      ; Go flash error and try again

095A: B6 01 B5            LDA     $01B5                     ; {ram:prepGiven} Preposition given?
095D: 27 24               BEQ     $983                      ; No ... just plain "?WHAT?"
095F: B6 01 B4            LDA     $01B4                     ; {ram:perpWord} Preposition word number?
0962: 26 1F               BNE     $983                      ; No word ... just plain "?WHAT?"
0964: 8E 3E CF            LDX     #$3ECF                    ; Prepositions list
0967: E6 84               LDB     ,X                        ; Length of word
0969: 27 18               BEQ     $983                      ; Reached the end ... do "?WHAT?"
096B: 34 10               PSHS    X                         ; Hold start of word
096D: E6 80               LDB     ,X+                       ; Get length again
096F: 3A                  ABX                               ; Point to end of word
0970: B6 01 B6            LDA     $01B6                     ; {ram:phrasePrep} Target preposition
0973: A1 80               CMPA    ,X+                       ; Matches?
0975: 27 04               BEQ     $97B                      ; Yes ... error includes this word
0977: 35 06               PULS    A,B                       ; Restore stack
0979: 20 EC               BRA     $967                      ; Next word
097B: 35 20               PULS    Y                         ; Word text to Y
097D: B6 01 BD            LDA     $01BD                     ; {ram:lsbError} LSB of error message
0980: BD 09 E1            JSR     $09E1                     ; Push preposition word
0983: 10 8E 13 43         LDY     #$1343                    ; "?WHAT?"
0987: B6 01 BD            LDA     $01BD                     ; {ram:lsbError} LSB of screen location
098A: 20 0F               BRA     $99B                      ; Go flash error and try again
098C: 10 8E 13 4A         LDY     #$134A                    ; "?WHICH"?
0990: B6 01 CF            LDA     $01CF                     ; {ram:tmp1CF} LSB of screen location
0993: 20 06               BRA     $99B                      ; Go flash error and try again
0995: 10 8E 13 3C         LDY     #$133C                    ; "?VERB?"

0999: 86 E0               LDA     #$E0                      ; LSB of start of input line
099B: 10 CE 03 FF         LDS     #$03FF                    ; Reset the stack (we jump back into the main loop)
099F: 8E 05 E0            LDX     #$05E0                    ; Error goes at start of line
09A2: BD 09 E1            JSR     $09E1                     ; Push error message on and pause
09A5: A6 A4               LDA     ,Y                        ; Get length
09A7: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Hold in counter
09AA: 34 10               PSHS    X                         ; Hold X
09AC: 86 60               LDA     #$60                      ; SPACE
09AE: A7 80               STA     ,X+                       ; Flash off ...
09B0: 7A 01 AB            DEC     $01AB                     ; {ram:tmp1AB} ... error ...
09B3: 26 F7               BNE     $9AC                      ; ... word
09B5: BD 09 D6            JSR     $09D6                     ; Long delay
09B8: 35 10               PULS    X                         ; Restore insertion point
09BA: 5A                  DECB                              ; All flashes done?
09BB: 26 14               BNE     $9D1                      ; No ... keep flashing error word
09BD: A6 A4               LDA     ,Y                        ; Size of error word
09BF: 4C                  INCA                              ; Plus the extra space
09C0: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Hold counter
09C3: BD 0A DB            JSR     $0ADB                     ; Close up the ...
09C6: 7A 01 AB            DEC     $01AB                     ; {ram:tmp1AB} ... error ...
09C9: 26 F8               BNE     $9C3                      ; ... word
09CB: BD 0A 63            JSR     $0A63                     ; Get input line
09CE: 7E 06 37            JMP     $0637                     ; Continue processing
09D1: BD 0A 00            JSR     $0A00                     ; Flash message and pause
09D4: 20 CF               BRA     $9A5                      ; Continue flashing and read new line

;Long delay
09D6: 86 32               LDA     #$32                      ; Outer loop counts
09D8: 7A 01 AB            DEC     $01AB                     ; {ram:tmp1AB} Decrease inner count (doesn't matter what's there)
09DB: 26 FB               BNE     $9D8                      ; Kill inner time
09DD: 4A                  DECA                              ; All 256 loops done?
09DE: 26 F8               BNE     $9D8                      ; No ... keep pausing
09E0: 39                  RTS                               ; Done

09E1: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Hold LSB of cursor
09E4: CC 05 E0            LDD     #$05E0                    ; Start of input line
09E7: F6 01 AB            LDB     $01AB                     ; {ram:tmp1AB} Replace LSB
09EA: 1F 01               TFR     D,X                       ; Place for error word in X
09EC: A6 A4               LDA     ,Y                        ; Get length of message
09EE: 4C                  INCA                              ; Plus a space after
09EF: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Store length
09F2: 34 20               PSHS    Y                         ; Hold message
09F4: BD 0B 06            JSR     $0B06                     ; Slide right past insertion point
09F7: 7A 01 AB            DEC     $01AB                     ; {ram:tmp1AB} Space opened up?
09FA: 26 F8               BNE     $9F4                      ; No ... open all the spaces for the error word
09FC: 35 20               PULS    Y                         ; Restore pointer
09FE: C6 08               LDB     #$08                      ; 8 flashes
0A00: A6 A4               LDA     ,Y                        ; Count again
0A02: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Size of word
0A05: 34 34               PSHS    Y,X,B                     ; Hold all
0A07: 31 21               LEAY    1,Y                       ; Skip size
0A09: A6 A0               LDA     ,Y+                       ; Copy error word ...
0A0B: A7 80               STA     ,X+                       ; ... to screen
0A0D: 7A 01 AB            DEC     $01AB                     ; {ram:tmp1AB} All done?
0A10: 26 F7               BNE     $A09                      ; No ... go back and do all
0A12: 30 01               LEAX    1,X                       ; Bump ...
0A14: 1F 10               TFR     X,D                       ; ... LSB ...
0A16: F7 01 BD            STB     $01BD                     ; {ram:lsbError} ... of screen pointer
0A19: BD 09 D6            JSR     $09D6                     ; Long pause
0A1C: 35 34               PULS    B,X,Y                     ; Restore
0A1E: 39                  RTS                               ; Done
```

# Find Sublist

```code
FindSublist: 
; Find a sublist by ID within a master list.
; X=pointer to master list
; B=sublist ID
; Return sublist pointer in X
; Return C=0 if not found, C=1 if found
0A1F: 30 01               LEAX    1,X                       ; Skip list ID
0A21: BD 0A 44            JSR     $0A44                     ; {LoadEnd} Read end of list to Y
0A24: 7F 01 E1            CLR     $01E1                     ; {ram:tmp1E1} Clear index of sublist
0A27: BD 0A 58            JSR     $0A58                     ; {CompareXY} Compare X to Y
0A2A: 25 01               BCS     $A2D                      ; X is smaller ... keep going
0A2C: 39                  RTS                               ; Done (C=0 not found)
0A2D: 7C 01 E1            INC     $01E1                     ; {ram:tmp1E1} Keep up with index of sublist
0A30: E1 84               CMPB    ,X                        ; Is this the sublist we want?
0A32: 27 0B               BEQ     $A3F                      ; Found ... C=1 and out
0A34: 34 20               PSHS    Y                         ; Hold the end
0A36: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip ID and read end of list to Y
0A39: 1F 21               TFR     Y,X                       ; Jump to the end of this list
0A3B: 35 20               PULS    Y                         ; Restore the end of the master list
0A3D: 20 E8               BRA     $A27                      ; Keep looking for the sublist
;
0A3F: 1A 01               ORCC    #$01                      ; C=1
0A41: 39                  RTS                               ; Done

SkipIDLoadEnd:
; Skip the ID byte and load the end of the list in Y.
0A42: 30 01               LEAX    1,X                       ; Bump script pointer
;
LoadEnd:
; Load the end of the list in Y.
0A44: 4F                  CLRA                              ; Upper is 0
0A45: 34 04               PSHS    B                         ; Hold lower
0A47: E6 80               LDB     ,X+                       ; Get lower
0A49: C5 80               BITB    #$80                      ; One or two byte value?
0A4B: 27 06               BEQ     $A53                      ; Just a one byte ... use it
0A4D: C4 7F               ANDB    #$7F                      ; This is the ...
0A4F: 1F 98               TFR     B,A                       ; ... MSB
0A51: E6 80               LDB     ,X+                       ; Now get 2nd byte (LSB)
0A53: 31 8B               LEAY    D,X                       ; Offset script
0A55: 35 04               PULS    B                         ; Restore B
0A57: 39                  RTS                               ; Done

CompareXY:
; Compare X to Y (flags = X - Y)
0A58: 10 BF 01 A9         STY     $01A9                     ; {ram:tmp1A9} Do compare ...
0A5C: BC 01 A9            CMPX    $01A9                     ; {ram:tmp1A9} X - Y
0A5F: 39                  RTS                               ; Done
```

# Get Input Line

```code
GetInputLine:
0A60: 8E 05 E0            LDX     #$05E0                    ; Start of bottom row
0A63: BD 0B 23            JSR     $0B23                     ; Slide bottom row to right after cursor and draw cursor
0A66: BD 0B 2B            JSR     $0B2B                     ; {GetKey} Get a key from the keyboard
0A69: 81 15               CMPA    #$15                      ; SHIFT-LEFT ARROW ? (true left arrow)
0A6B: 27 20               BEQ     $A8D                      ; Yes ... swap cursor and character to left
0A6D: 81 5D               CMPA    #$5D                      ; SHIFT-RIGHT ARROW ? (true right arrow)
0A6F: 27 2F               BEQ     $AA0                      ; Yes ... swap cursor and character to right
0A71: 81 09               CMPA    #$09                      ; RIGHT-ARROW ? (backspace)
0A73: 27 3E               BEQ     $AB3                      ; Go handle delete
0A75: 81 0D               CMPA    #$0D                      ; CR ?
0A77: 27 4F               BEQ     $AC8                      ; Handle it and out
0A79: 81 0C               CMPA    #$0C                      ; CLEAR ?
0A7B: 27 4F               BEQ     $ACC                      ; Yes ... clear the row
0A7D: 81 08               CMPA    #$08                      ; LEFT-ARROW ? (backspace)
0A7F: 27 3B               BEQ     $ABC                      ; Yes go handle
0A81: 8C 05 FF            CMPX    #$05FF                    ; At the end of the screen?
0A84: 27 E0               BEQ     $A66                      ; Yes ... ignore and get another
0A86: BD 0B 06            JSR     $0B06                     ; Slide bottom row beyond insertion
0A89: A7 80               STA     ,X+                       ; Store character
0A8B: 20 D9               BRA     $A66                      ; Go get another character

0A8D: 8C 05 E0            CMPX    #$05E0                    ; Nothing typed?
0A90: 27 D4               BEQ     $A66                      ; Yes ... ignore and get another
0A92: 30 1F               LEAX    -1,X                      ; Swap ...
0A94: A6 80               LDA     ,X+                       ; ... cursor ...
0A96: A7 84               STA     ,X                        ; ... and ...
0A98: 30 1F               LEAX    -1,X                      ; ... character ...
0A9A: 86 CF               LDA     #$CF                      ; ... to the ...
0A9C: A7 84               STA     ,X                        ; ... left
0A9E: 20 C6               BRA     $A66                      ; Go get another character

0AA0: 8C 05 FF            CMPX    #$05FF                    ; End of screen?
0AA3: 27 C1               BEQ     $A66                      ; Yes ... go get another key
0AA5: 30 01               LEAX    1,X                       ; Swap ...
0AA7: A6 84               LDA     ,X                        ; ... cursor ...
0AA9: 30 1F               LEAX    -1,X                      ; ... and ...
0AAB: A7 80               STA     ,X+                       ; ... character ...
0AAD: 86 CF               LDA     #$CF                      ; ... to the ...
0AAF: A7 84               STA     ,X                        ; ... right
0AB1: 20 B3               BRA     $A66                      ; Go get another key
;
0AB3: BD 0A DB            JSR     $0ADB                     ; Back off trailing cursor block
0AB6: 86 CF               LDA     #$CF                      ; Store ...
0AB8: A7 84               STA     ,X                        ; ... cursor block
0ABA: 20 AA               BRA     $A66                      ; Go get another key
;
0ABC: 8C 05 E0            CMPX    #$05E0                    ; At the start of the row?
0ABF: 27 A5               BEQ     $A66                      ; Yes ... go get another key
0AC1: 30 1F               LEAX    -1,X                      ; Back up one character
0AC3: BD 0A DB            JSR     $0ADB                     ; Erase the end
0AC6: 20 9E               BRA     $A66                      ; Go get another key
;
0AC8: BD 0A DB            JSR     $0ADB                     ; Back off cursor character
0ACB: 39                  RTS                               ; Done
;
0ACC: 8E 05 E0            LDX     #$05E0                    ; Start of bottom row
0ACF: C6 20               LDB     #$20                      ; 32 characters on the row
0AD1: 86 60               LDA     #$60                      ; SPACE character
0AD3: A7 80               STA     ,X+                       ; Clear ...
0AD5: 5A                  DECB                              ; ... the ...
0AD6: 26 FB               BNE     $AD3                      ; ... bottom row
0AD8: 7E 0A 60            JMP     $0A60                     ; {GetInputLine} Go get another key
;
0ADB: 1F 13               TFR     X,U                       ; Hold X
0ADD: 31 01               LEAY    1,X                       ; Clear trailing ...
0ADF: 86 60               LDA     #$60                      ; ... cursor ...
0AE1: A7 84               STA     ,X                        ; ... block
;
0AE3: 10 8C 06 00         CMPY    #$0600                    ; End of screen?
0AE7: 27 E2               BEQ     $ACB                      ; Yes out
0AE9: 10 8C 06 01         CMPY    #$0601                    ; End of screen?
0AED: 27 DC               BEQ     $ACB                      ; Yes out
0AEF: 10 8C 06 02         CMPY    #$0602                    ; End of screen?
0AF3: 27 D6               BEQ     $ACB                      ; Yes out
0AF5: A6 A0               LDA     ,Y+                       ; Back ...
0AF7: A7 80               STA     ,X+                       ; ... up ...
0AF9: 10 8C 06 00         CMPY    #$0600                    ; ... row ...
0AFD: 26 F6               BNE     $AF5                      ; ... over cursor
0AFF: 86 60               LDA     #$60                      ; Clear last ...
0B01: A7 84               STA     ,X                        ; ... character
0B03: 1F 31               TFR     U,X                       ; Restore X
0B05: 39                  RTS                               ; Done
;
0B06: 8C 06 00            CMPX    #$0600                    ; Past end of screen?
0B09: 27 17               BEQ     $B22                      ; Yes ... out
0B0B: BF 01 A7            STX     $01A7                     ; {ram:tmp1A7} Hold insertion point
0B0E: 8E 06 00            LDX     #$0600                    ; End+1
0B11: 10 8E 05 FF         LDY     #$05FF                    ; End
0B15: E6 A2               LDB     ,-Y                       ; Slide bottom row ...
0B17: E7 82               STB     ,-X                       ; ... to the right
0B19: BC 01 A7            CMPX    $01A7                     ; {ram:tmp1A7} At the insertion point?
0B1C: 26 F7               BNE     $B15                      ; No ... slide all
0B1E: C6 60               LDB     #$60                      ; SPACE
0B20: E7 84               STB     ,X                        ; Clear first character
0B22: 39                  RTS                               ; Done
;
0B23: BD 0B 06            JSR     $0B06                     ; Slide row over from cursor
0B26: 86 CF               LDA     #$CF                      ; Cursor character (white block)
0B28: A7 84               STA     ,X                        ; Cursor to screen
0B2A: 39                  RTS                               ; Done

GetKey:
0B2B: BD 12 A8            JSR     $12A8                     ; Get random number every key
0B2E: AD 9F A0 00         JSR     [$A000]                   ; {hard:POLCAT} Get key from user
0B32: 4D                  TSTA                              ; Anything pressed?
0B33: 27 F6               BEQ     $B2B                      ; {GetKey} No ... keep waiting
0B35: 81 41               CMPA    #$41                      ; Letter 'A'
0B37: 24 06               BCC     $B3F                      ; Greater or equal ... use it
0B39: 81 20               CMPA    #$20                      ; Space
0B3B: 25 02               BCS     $B3F                      ; Lower .... use it
0B3D: 8B 40               ADDA    #$40                      ; Not really sure why. '!' becomes 'a'.
0B3F: 39                  RTS                               ; Done
```

# Decode Buffer

```code
DecodeBuffer:
; X=input buffer on screen (1 before)
; 1D8=pointer to result token list
; Return 1CF LSB of first word
; Return 1BB LSB of next word
; Return list of 3-byte tokens filled into buffer pointed to by 1D8:
;   NN WW PP
;     NN = list number
;     WW = word number
;     PP = LSB of word on screen
;
0B40: 30 01               LEAX    1,X                       ; Next in buffer
;
0B42: 1F 10               TFR     X,D                       ; Hold ...
0B44: F7 01 CF            STB     $01CF                     ; {ram:tmp1CF} ... LSB of first word (could be ignored)
0B47: 8C 06 00            CMPX    #$0600                    ; End of buffer?
0B4A: 27 F3               BEQ     $B3F                      ; Yes ... out
0B4C: A6 84               LDA     ,X                        ; Next in input
0B4E: 81 60               CMPA    #$60                      ; Valid character?
0B50: 24 EE               BCC     $B40                      ; {DecodeBuffer} No ... skip till we find one
0B52: 10 8E 3C 29         LDY     #$3C29                    ; Word token table
0B56: BD 0B 8B            JSR     $0B8B                     ; {DecodeWord} Try first list
0B59: 27 E7               BEQ     $B42                      ; Found a match ... ignore it
0B5B: C6 01               LDB     #$01                      ; Staring list number
0B5D: 31 21               LEAY    1,Y                       ; Next list of words
0B5F: BD 0B 8B            JSR     $0B8B                     ; {DecodeWord} Try and match
0B62: 27 08               BEQ     $B6C                      ; Found a match ... record it
0B64: 5C                  INCB                              ; Next list of words
0B65: C1 05               CMPB    #$05                      ; All tried?
0B67: 26 F4               BNE     $B5D                      ; No ... go back and try all
0B69: 8A 01               ORA     #$01                      ; Not-zero ... error
0B6B: 39                  RTS                               ; Done

0B6C: 1E 12               EXG     X,Y                       ; X to Y
0B6E: BE 01 D8            LDX     $01D8                     ; {ram:nextToken} Current result token pointer
0B71: E7 80               STB     ,X+                       ; Store list number
0B73: A7 80               STA     ,X+                       ; Store word number
0B75: B6 01 CF            LDA     $01CF                     ; {ram:tmp1CF} Start of word
0B78: A7 80               STA     ,X+                       ; Store word start
0B7A: BF 01 D8            STX     $01D8                     ; {ram:nextToken} Bump result token pointer
0B7D: 1E 12               EXG     X,Y                       ; Restore X
0B7F: C1 01               CMPB    #$01                      ; Is this the first (VERB) list?
0B81: 26 06               BNE     $B89                      ; No ... skip marking
0B83: B6 01 BC            LDA     $01BC                     ; {ram:lsbCursor} Mark the input buffer location ...
0B86: B7 01 BB            STA     $01BB                     ; {ram:lsbVerb} ... of the verb
0B89: 4F                  CLRA                              ; OK
0B8A: 39                  RTS                               ; Return
```

# Decode Word

```code
DecodeWord: 
; Y=input match table
; X=pointer to input buffer word
; Return word data in A if found
; Return is-zero if found, not-zero if not found
; Return 1AB with word data (if found)
; Return 1BC with LSB of pointer-to-next-word
;
; 1A7,1A8 Temporary
; 1AB Temporary
; 1D0 Temporary 
;
0B8B: A6 A4               LDA     ,Y                        ; Length of word
0B8D: 26 03               BNE     $B92                      ; It is a word ... go check it
0B8F: 8A 01               ORA     #$01                      ; End of list ...
0B91: 39                  RTS                               ; ... return not-zero
0B92: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Temporary
0B95: B7 01 D0            STA     $01D0                     ; {ram:tmp1DO} Temporary
0B98: 34 10               PSHS    X                         ; Hold pointer to input word
0B9A: 31 21               LEAY    1,Y                       ; Skip over word length in table
0B9C: A6 84               LDA     ,X                        ; Character from input (from screen)
0B9E: 81 60               CMPA    #$60                      ; Space?
0BA0: 27 53               BEQ     $BF5                      ; Yes. Didn't match the target word. Next.
0BA2: 8C 06 00            CMPX    #$0600                    ; Past screen (end of buffer)?
0BA5: 27 4E               BEQ     $BF5                      ; Yes. Didn't match the target word. next
0BA7: 81 60               CMPA    #$60                      ; Valid character?
0BA9: 25 04               BCS     $BAF                      ; Yes ... do compare
0BAB: 30 01               LEAX    1,X                       ; No ... skip this
0BAD: 20 ED               BRA     $B9C                      ; Look for valid character
0BAF: A1 A4               CMPA    ,Y                        ; Matches target word?
0BB1: 26 42               BNE     $BF5                      ; No ... next word
0BB3: 30 01               LEAX    1,X                       ; Next in input
0BB5: 31 21               LEAY    1,Y                       ; Next in match
0BB7: 7A 01 AB            DEC     $01AB                     ; {ram:tmp1AB} All done?
0BBA: 26 E0               BNE     $B9C                      ; No ... keep looking
0BBC: B6 01 D0            LDA     $01D0                     ; {ram:tmp1DO} Original length
0BBF: 81 06               CMPA    #$06                      ; Six letter input?
0BC1: 27 06               BEQ     $BC9                      ; Yes ... could be truncated. That's enough of a match.
0BC3: A6 84               LDA     ,X                        ; Next from screen
0BC5: 81 60               CMPA    #$60                      ; Space? End of word?
0BC7: 25 33               BCS     $BFC                      ; No. Try next word
0BC9: A6 A4               LDA     ,Y                        ; Get the word data
0BCB: 35 20               PULS    Y                         ; Drop the input buffer pointer
0BCD: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Hold the word data
0BD0: A6 84               LDA     ,X                        ; Next in input buffer?
0BD2: 81 60               CMPA    #$60                      ; Is it a space?
0BD4: 27 0C               BEQ     $BE2                      ; Yes ... ready for next word
0BD6: BF 01 A7            STX     $01A7                     ; {ram:tmp1A7} Start of next word (in case end of buffer)
0BD9: 8C 06 00            CMPX    #$0600                    ; Is this the end of the input buffer?
0BDC: 27 0A               BEQ     $BE8                      ; Yes. Done
0BDE: 30 01               LEAX    1,X                       ; Skip to next input word
0BE0: 20 EE               BRA     $BD0                      ; Keep looking for input
0BE2: BF 01 A7            STX     $01A7                     ; {ram:tmp1A7} Pointer to ending space
0BE5: 7C 01 A8            INC     $01A8                     ; {ram:tmp1A7} Point to next character past space (start of next word)
0BE8: B6 01 A8            LDA     $01A8                     ; {ram:tmp1A7} Keep ...
0BEB: B7 01 BC            STA     $01BC                     ; {ram:lsbCursor} ... only LSB
0BEE: B6 01 AB            LDA     $01AB                     ; {ram:tmp1AB} Return word data in A
0BF1: 7F 01 A7            CLR     $01A7                     ; {ram:tmp1A7} return is-zero for found
0BF4: 39                  RTS                               ; Done
;
0BF5: 31 21               LEAY    1,Y                       ; Skip next in word data
0BF7: 7A 01 AB            DEC     $01AB                     ; {ram:tmp1AB} All skipped
0BFA: 26 F9               BNE     $BF5                      ; No ... skip all
0BFC: 35 10               PULS    X                         ; Restore pointer to word
0BFE: 31 21               LEAY    1,Y                       ; Skip word data
0C00: 7E 0B 8B            JMP     $0B8B                     ; {DecodeWord} Keep trying
```
    
# Process Command

```code
ProcessCommand: 
; Either a direct command or a common command
0C03: A6 80               LDA     ,X+                       ; Next in script
0C05: 1F 89               TFR     A,B                       ; Hold original command
0C07: 85 80               BITA    #$80                      ; Upper bit set?
0C09: 27 13               BEQ     $C1E                      ; No ... do commands
0C0B: 34 30               PSHS    Y,X                       ; Hold
0C0D: 8E 37 FA            LDX     #$37FA                    ; Common commands
0C10: BD 0A 1F            JSR     $0A1F                     ; {FindSublist} Find common command
0C13: 24 06               BCC     $C1B                      ; Not found ... skip
0C15: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip length of command
0C18: BD 0C 03            JSR     $0C03                     ; {ProcessCommand} Execute command
0C1B: 35 30               PULS    X,Y                       ; Restore
0C1D: 39                  RTS                               ; Out

0C1E: 1F 98               TFR     B,A                       ; Hold original command
0C20: 10 8E 12 E5         LDY     #$12E5                    ; Function table
0C24: 48                  ASLA                              ; Jump to ...
0C25: 6E B6               JMP     [A,Y]                     ; ... command

Com0D_ExecutePassingList:
; Execute a list of commands as long as they pass. Either way end pointing one
; past end.
; Data: LENGTH + list of command
0C27: BD 0A 44            JSR     $0A44                     ; {LoadEnd} Read length of command
0C2A: BD 0A 58            JSR     $0A58                     ; {CompareXY} Are we past the end?
0C2D: 24 0C               BCC     $C3B                      ; Yes ... end successfully
0C2F: 34 20               PSHS    Y                         ; Hold the end
0C31: BD 0C 03            JSR     $0C03                     ; {ProcessCommand} Execute the command
0C34: 35 20               PULS    Y                         ; Restore the end
0C36: 27 F2               BEQ     $C2A                      ; Command successful? Yes ... keep processing
0C38: 1E 12               EXG     X,Y                       ; Fail ... put us at the end
0C3A: 39                  RTS                               ; Done
0C3B: 1E 12               EXG     X,Y                       ; Point to end of list
0C3D: 4F                  CLRA                              ; Z=1 ... success
0C3E: 39                  RTS                               ; Done

Com0E_ExecuteFailingList:
0C3F: BD 0A 44            JSR     $0A44                     ; {LoadEnd} Load the end
0C42: BD 0A 58            JSR     $0A58                     ; {CompareXY} Reached end of list?
0C45: 24 0C               BCC     $C53                      ; Yes ... error
0C47: 34 20               PSHS    Y                         ; Hold end of command
0C49: BD 0C 03            JSR     $0C03                     ; {ProcessCommand} Execute command
0C4C: 35 20               PULS    Y                         ; Restore end
0C4E: 26 F2               BNE     $C42                      ; Command failed ... try next
0C50: 1E 12               EXG     X,Y                       ; Set script pointer to end of list
0C52: 39                  RTS                               ; Out
; 
0C53: 1E 12               EXG     X,Y                       ; Set script pointer to end of list
0C55: 8A 01               ORA     #$01                      ; Return fail
0C57: 39                  RTS                               ; Done

Com0B_Switch:
0C58: BD 0A 44            JSR     $0A44                     ; {LoadEnd} Get size of switch list
0C5B: E6 80               LDB     ,X+                       ; Get function to call
0C5D: BD 0A 58            JSR     $0A58                     ; {CompareXY} End of options?
0C60: 24 F1               BCC     $C53                      ; Yes ... out with error
0C62: 34 20               PSHS    Y                         ; Hold total switch size
0C64: 34 04               PSHS    B                         ; Hold function to call
0C66: 1F 98               TFR     B,A                       ; Call the ...
0C68: BD 0C 20            JSR     $0C20                     ; ... target function
0C6B: 35 04               PULS    B                         ; Restore function to call
0C6D: 27 09               BEQ     $C78                      ; Got our script ... go do it
0C6F: BD 0A 44            JSR     $0A44                     ; {LoadEnd} Size of pass script
0C72: 1E 12               EXG     X,Y                       ; Skip over this option
0C74: 35 20               PULS    Y                         ; End of script
0C76: 20 E5               BRA     $C5D                      ; Keep looking
0C78: BD 0A 44            JSR     $0A44                     ; {LoadEnd} Skip length
0C7B: BD 0C 03            JSR     $0C03                     ; {ProcessCommand} Execute
0C7E: 35 10               PULS    X                         ; Restore script
0C80: 39                  RTS                               ; Done

Com00_MoveActiveObjectToRoomAndLook:
0C81: BD 0C 8D            JSR     $0C8D                     ; {Com19_MoveActiveObjectToRoom} Move active object to new room
0C84: 34 10               PSHS    X                         ; Hold script
0C86: BD 0D 4A            JSR     $0D4A                     ; Print room description and objects
0C89: 35 10               PULS    X                         ; Restore script
0C8B: 4F                  CLRA                              ; OK
0C8C: 39                  RTS                               ; Done

Com19_MoveActiveObjectToRoom:
0C8D: A6 80               LDA     ,X+                       ; New room number
0C8F: 34 10               PSHS    X                         ; Hold script
0C91: B7 01 D5            STA     $01D5                     ; {ram:CUR_ROOM} Store new actvie room number
0C94: 1F 89               TFR     A,B                       ; Store ...
0C96: 8E 15 23            LDX     #$1523                    ; ... pointer ...
0C99: BD 0A 1F            JSR     $0A1F                     ; {FindSublist} ... to ...
0C9C: BF 01 D6            STX     $01D6                     ; {ram:CUR_ROOM_DATA} ... new room
0C9F: BE 01 D3            LDX     $01D3                     ; {ram:ACTIVE_OBJ_DATA} Active object
0CA2: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip size
0CA5: B6 01 D5            LDA     $01D5                     ; {ram:CUR_ROOM} New location
0CA8: A7 84               STA     ,X                        ; Move object to active room
0CAA: 35 10               PULS    X                         ; Restore script
0CAC: 4F                  CLRA                              ; OK
0CAD: 39                  RTS                               ; Done

Com1A_SetVarObjectTo1stNoun:
0CAE: FE 01 C6            LDU     $01C6                     ; {ram:FIRST_NOUN_DATA} Copy 1st noun ...
0CB1: FF 01 C0            STU     $01C0                     ; {ram:VAR_OBJ_DATA} ... data pointer
0CB4: B6 01 C3            LDA     $01C3                     ; {ram:FIRST_NOUN_NUM} Copy 1st noun ...
0CB7: B7 01 BF            STA     $01BF                     ; {ram:VAR_OBJ_NUMBER} ... object number
0CBA: 4F                  CLRA                              ; Z=1 for OK
0CBB: 39                  RTS                               ; Done

Com1B_SetVarObjectTo2ndNoun:
0CBC: FE 01 CC            LDU     $01CC                     ; {ram:SECOND_NOUN_DATA} Copy 2nd noun ...
0CBF: FF 01 C0            STU     $01C0                     ; {ram:VAR_OBJ_DATA} ... data pointer
0CC2: B6 01 C9            LDA     $01C9                     ; {ram:SECOND_NOUN_NUM} Copy 2nd noun ...
0CC5: B7 01 BF            STA     $01BF                     ; {ram:VAR_OBJ_NUMBER} ... object number
0CC8: 4F                  CLRA                              ; Z=1 for OK
0CC9: 39                  RTS                               ; Done

Com1C_SetVarObject:
0CCA: E6 80               LDB     ,X+                       ; Get object number from script
0CCC: 34 10               PSHS    X                         ; Hold script pointer
0CCE: F7 01 BF            STB     $01BF                     ; {ram:VAR_OBJ_NUMBER} Store target object number
0CD1: 27 06               BEQ     $CD9                      ; 0 ... no-object
0CD3: BD 11 33            JSR     $1133                     ; Find object data
0CD6: BF 01 C0            STX     $01C0                     ; {ram:VAR_OBJ_DATA} Store target object data
0CD9: 35 10               PULS    X                         ; Restore script
0CDB: 4F                  CLRA                              ; Return OK
0CDC: 39                  RTS                               ; Done

Com21_RunGeneralWithTempPhrase:
0CDD: FE 01 C6            LDU     $01C6                     ; {ram:FIRST_NOUN_DATA} 1st noun data ...
0CE0: 34 40               PSHS    U                         ; ... on stack
0CE2: FE 01 CC            LDU     $01CC                     ; {ram:SECOND_NOUN_DATA} 2nd noun data ...
0CE5: 34 40               PSHS    U                         ; ... on stack
0CE7: B6 01 C9            LDA     $01C9                     ; {ram:SECOND_NOUN_NUM} 2nd noun number
0CEA: F6 01 C3            LDB     $01C3                     ; {ram:FIRST_NOUN_NUM} 1st noun number
0CED: 34 06               PSHS    B,A                       ; Hold these
0CEF: B6 01 D1            LDA     $01D1                     ; {ram:PHRASE_FORM} Phrase number
0CF2: 34 02               PSHS    A                         ; Hold it
0CF4: A6 80               LDA     ,X+                       ; New temporary ...
0CF6: B7 01 D1            STA     $01D1                     ; {ram:PHRASE_FORM} ... phrase number
0CF9: EC 81               LDD     ,X++                      ; Temporary 1st and 2nd noun numbers
0CFB: F7 01 AB            STB     $01AB                     ; {ram:tmp1AB} Hold 2nd noun for now
0CFE: 34 10               PSHS    X                         ; Hold script
0D00: B7 01 C3            STA     $01C3                     ; {ram:FIRST_NOUN_NUM} Temporary 1st noun
0D03: 1F 89               TFR     A,B                       ; To B (for lookup)
0D05: 27 06               BEQ     $D0D                      ; Not one ... skip
0D07: BD 11 33            JSR     $1133                     ; Lookup object in B
0D0A: BF 01 C6            STX     $01C6                     ; {ram:FIRST_NOUN_DATA} Temporary 1st noun data
0D0D: F6 01 AB            LDB     $01AB                     ; {ram:tmp1AB} Temporary 2nd noun ...
0D10: F7 01 C9            STB     $01C9                     ; {ram:SECOND_NOUN_NUM} ... index
0D13: 27 06               BEQ     $D1B                      ; There isn't one ... skip
0D15: BD 11 33            JSR     $1133                     ; Lookup object in B
0D18: BF 01 CC            STX     $01CC                     ; {ram:SECOND_NOUN_DATA} Temporary 2nd noun
0D1B: 8E 32 3C            LDX     #$323C                    ; General commands
0D1E: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip ID and length
0D21: BD 0C 03            JSR     $0C03                     ; {ProcessCommand} Execute general script
0D24: 1F A8               TFR     CCR,A                     ; Hold the result ...
0D26: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} ... for a moment
0D29: 35 20               PULS    Y                         ;
0D2B: 35 02               PULS    A                         ;
0D2D: B7 01 D1            STA     $01D1                     ; {ram:PHRASE_FORM} Restore ...
0D30: 35 06               PULS    A,B                       ; ... phrase ...
0D32: F7 01 C3            STB     $01C3                     ; {ram:FIRST_NOUN_NUM} ... and ...
0D35: B7 01 C9            STA     $01C9                     ; {ram:SECOND_NOUN_NUM} ... nouns
0D38: 35 40               PULS    U                         ;
0D3A: FF 01 CC            STU     $01CC                     ; {ram:SECOND_NOUN_DATA} 
0D3D: 35 40               PULS    U                         ;
0D3F: FF 01 C6            STU     $01C6                     ; {ram:FIRST_NOUN_DATA} 
0D42: 1E 12               EXG     X,Y                       ;
0D44: B6 01 AB            LDA     $01AB                     ; {ram:tmp1AB} 
0D47: 1F 8A               TFR     A,CCR                     ; Restore result
0D49: 39                  RTS                               ; Done

; Print room description
0D4A: B6 01 D2            LDA     $01D2                     ; {ram:ACTIVE_OBJ_NUM} Actiuve object number
0D4D: 81 1D               CMPA    #$1D                      ; Is this the SYSTEM object?
0D4F: 26 F8               BNE     $D49                      ; No ... return
0D51: BE 01 D6            LDX     $01D6                     ; {ram:CUR_ROOM_DATA} Current room script
0D54: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip length
0D57: 30 01               LEAX    1,X                       ;
0D59: C6 03               LDB     #$03                      ; You are in DESCRIPTION script
0D5B: BD 0A 27            JSR     $0A27                     ; Get room description
0D5E: 24 05               BCC     $D65                      ; No room description ... print objects in room
0D60: 30 01               LEAX    1,X                       ; Assume length is one byte
0D62: BD 11 4C            JSR     $114C                     ; {PrintPackedMessage} Print the packed message
;
; Print object descriptions
;
0D65: 8E 20 FF            LDX     #$20FF                    ; Object data
0D68: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip length
0D6B: 34 20               PSHS    Y                         ; Hold end
0D6D: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip this object's length
0D70: B6 01 D5            LDA     $01D5                     ; {ram:CUR_ROOM} Current room
0D73: A1 84               CMPA    ,X                        ; Object in room?
0D75: 26 12               BNE     $D89                      ; No ... next object
0D77: 30 03               LEAX    3,X                       ; Skip data
0D79: C6 03               LDB     #$03                      ; Get description ...
0D7B: BD 0A 27            JSR     $0A27                     ; ... field
0D7E: 24 09               BCC     $D89                      ; No description ... next object
0D80: 30 01               LEAX    1,X                       ; Skip length
0D82: 34 20               PSHS    Y                         ; Hold end of object
0D84: BD 11 4C            JSR     $114C                     ; {PrintPackedMessage} Print description
0D87: 35 20               PULS    Y                         ; Restore length
0D89: 1E 12               EXG     X,Y                       ; Next object
0D8B: 35 20               PULS    Y                         ; End of objects
0D8D: BD 0A 58            JSR     $0A58                     ; {CompareXY} All done?
0D90: 25 D9               BCS     $D6B                      ; No ... keep printing
0D92: 39                  RTS                               ; Done

Com01_IsObjectInPackOrRoom:
0D93: E6 80               LDB     ,X+                       ; Get object number from script
0D95: 34 10               PSHS    X                         ; Hold script pointer
0D97: BD 11 33            JSR     $1133                     ; Get object data
0D9A: BD 08 AA            JSR     $08AA                     ; See if it is in pack or room
0D9D: 35 10               PULS    X                         ; Restore script
0D9F: 39                  RTS                               ; Out

Com20_CheckActiveObject:
0DA0: B6 01 D2            LDA     $01D2                     ; {ram:ACTIVE_OBJ_NUM} Active object
0DA3: A1 80               CMPA    ,X+                       ; Matches target?
0DA5: 39                  RTS                               ; Done

Com02_CheckObjectIsOwnedByActive:
0DA6: E6 80               LDB     ,X+                       ;
0DA8: 7E 0F 5F            JMP     $0F5F                     ; 

Com03_IsObjectYAtX:
; Check to see if an object is at a target location.
0DAB: EC 81               LDD     ,X++                      ; Room and object
0DAD: 34 10               PSHS    X                         ; Hold script
0DAF: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Remember the room
0DB2: BD 11 33            JSR     $1133                     ; Locate the object
0DB5: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip the length
0DB8: EC 81               LDD     ,X++                      ; Get the room to A
0DBA: B1 01 AB            CMPA    $01AB                     ; {ram:tmp1AB} Is this object in the target place?
0DBD: 35 10               PULS    X                         ; Restore script
0DBF: 39                  RTS                               ; Out

Com0C_FAIL:
; Always fail
0DC0: 8A 01               ORA     #$01                      ; Set the fail flag
0DC2: 39                  RTS                               ; Done

Com04_PrintSYSTEMOrPlayerMessage:
0DC3: B6 01 D2            LDA     $01D2                     ; {ram:ACTIVE_OBJ_NUM} Active object
0DC6: 81 1D               CMPA    #$1D                      ; Is this the player?

0DC8: 26 0E               BNE     $DD8                      ; No ... must be system

Com1F_PrintMessage:
0DCA: C6 1D               LDB     #$1D                      ; Player number
0DCC: 34 10               PSHS    X                         ; Hold script
0DCE: BD 11 33            JSR     $1133                     ; Look up Player
0DD1: BD 08 AA            JSR     $08AA                     ; Is Player in current room?
0DD4: 35 10               PULS    X                         ; Restore
0DD6: 27 07               BEQ     $DDF                      ; Yes ... do printing
0DD8: BD 0A 44            JSR     $0A44                     ; {LoadEnd} Skip to ...
0DDB: 1E 12               EXG     X,Y                       ; ... end of packed message.
0DDD: 20 03               BRA     $DE2                      ; Return OK but no printing
0DDF: BD 11 4C            JSR     $114C                     ; {PrintPackedMessage} Print packed message at X
0DE2: 4F                  CLRA                              ; OK
0DE3: 39                  RTS                               ; Done

Com07_Look:
0DE4: BD 0D 4A            JSR     $0D4A                     ; Print room description
0DE7: 4F                  CLRA                              ; OK
0DE8: 39                  RTS                               ; Done

Com06_Inventory:
0DE9: 34 10               PSHS    X                         ; Hold script pointer
0DEB: 86 0D               LDA     #$0D                      ; Print ...
0DED: BD 11 84            JSR     $1184                     ; {PrintCharacterAutoWrap} ... CR
0DF0: 8E 20 FF            LDX     #$20FF                    ; Objects
0DF3: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip size of objects
;
0DF6: BD 0A 58            JSR     $0A58                     ; {CompareXY} CompareXY
0DF9: 24 24               BCC     $E1F                      ; End of list ... out
0DFB: 34 20               PSHS    Y                         ; Hold end of master list of objects
0DFD: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Get pointer to next object
0E00: E6 84               LDB     ,X                        ; Object location
0E02: F1 01 D2            CMPB    $01D2                     ; {ram:ACTIVE_OBJ_NUM} Active object?
0E05: 26 12               BNE     $E19                      ; No ... skip this object
0E07: 30 03               LEAX    3,X                       ; Skip data
0E09: C6 02               LDB     #$02                      ; Find short name ...
0E0B: BD 0A 27            JSR     $0A27                     ; ... string
0E0E: 24 09               BCC     $E19                      ; No short name ... skip
0E10: 30 01               LEAX    1,X                       ; Skip the 02 data id
0E12: 34 20               PSHS    Y                         ; Hold next-object
0E14: BD 11 43            JSR     $1143                     ; Print packed message and CR
0E17: 35 20               PULS    Y                         ; Restore next-object
0E19: 1E 12               EXG     X,Y                       ; Move to next object
0E1B: 35 20               PULS    Y                         ; End of master list
0E1D: 20 D7               BRA     $DF6                      ; Do all objects
0E1F: 4F                  CLRA                              ; Success
0E20: 35 10               PULS    X                         ; Restore script pointer
0E22: 39                  RTS                               ; Done

Com08_CompareObjectToFirstNoun:
0E23: FE 01 C6            LDU     $01C6                     ; {ram:FIRST_NOUN_DATA} 1st noun data
0E26: B6 01 C3            LDA     $01C3                     ; {ram:FIRST_NOUN_NUM} 1st noun number
;
0E29: FF 01 D8            STU     $01D8                     ; {ram:nextToken} Hold
0E2C: 4D                  TSTA                              ; Is there an object?
0E2D: 27 10               BEQ     $E3F                      ; No ... error
0E2F: E6 80               LDB     ,X+                       ; Object number from script
0E31: 34 10               PSHS    X                         ; Hold script
0E33: BD 11 33            JSR     $1133                     ; Find object
0E36: 1E 12               EXG     X,Y                       ; Pointer of found object to Y
0E38: 35 10               PULS    X                         ; Restore script pointer
0E3A: 10 BC 01 D8         CMPY    $01D8                     ; {ram:nextToken} Object the same?
0E3E: 39                  RTS                               ; Done
0E3F: 5D                  TSTB                              ; B can't be 0 ... Z=0 error
0E40: 39                  RTS                               ; Done

Com09_CompareObjectToSecondNoun:
0E41: FE 01 CC            LDU     $01CC                     ; {ram:SECOND_NOUN_DATA} 2nd noun data
0E44: B6 01 C9            LDA     $01C9                     ; {ram:SECOND_NOUN_NUM} 2nd noun number
0E47: 20 E0               BRA     $E29                      ; Do compare

Com0A_CompareToPhraseForm:
0E49: E6 80               LDB     ,X+                       ; Compare from script ...
0E4B: F1 01 D1            CMPB    $01D1                     ; {ram:PHRASE_FORM} ... to phrase form
0E4E: 39                  RTS                               ; Done

Com0F_PickUpObject:
; Move noun object to pack.
0E4F: 34 10               PSHS    X                         ; Hold script
0E51: BE 01 C0            LDX     $01C0                     ; {ram:VAR_OBJ_DATA} Pointer to noun object
0E54: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip length
0E57: B6 01 D2            LDA     $01D2                     ; {ram:ACTIVE_OBJ_NUM} Back pack "location" value
0E5A: A7 84               STA     ,X                        ; Move object to pack
0E5C: 4F                  CLRA                              ; OK
0E5D: 35 10               PULS    X                         ; Restore script
0E5F: 39                  RTS                               ; Done

Com10_DropObject:
; Move noun object to current room.
0E60: 34 10               PSHS    X                         ; Hold script
0E62: BE 01 C0            LDX     $01C0                     ; {ram:VAR_OBJ_DATA} Pointer to noun object
0E65: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip length
0E68: B6 01 D5            LDA     $01D5                     ; {ram:CUR_ROOM} Current room
0E6B: A7 84               STA     ,X                        ; Move object to room
0E6D: 35 10               PULS    X                         ; Restore script
0E6F: 4F                  CLRA                              ; Done
0E70: 39                  RTS                               ; Out

Com13_PhraseWithRoom1st2nd:
0E71: 34 10               PSHS    X                         ; Save script
0E73: BE 01 D6            LDX     $01D6                     ; {ram:CUR_ROOM_DATA} Current room script
0E76: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip id and length
0E79: 30 01               LEAX    1,X                       ; Skip
0E7B: C6 04               LDB     #$04                      ; Get ...
0E7D: BD 0A 27            JSR     $0A27                     ; ... phrase script
0E80: 24 08               BCC     $E8A                      ; No phrase script ... skip
0E82: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip id and length
0E85: BD 0C 03            JSR     $0C03                     ; {ProcessCommand} Execute
0E88: 27 3B               BEQ     $EC5                      ; Move passed ... OK and out
0E8A: B6 01 C9            LDA     $01C9                     ; {ram:SECOND_NOUN_NUM} Is there a 2nd noun?
0E8D: 27 17               BEQ     $EA6                      ; No ... skip
0E8F: BE 01 CC            LDX     $01CC                     ; {ram:SECOND_NOUN_DATA} Second noun data
0E92: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip ...
0E95: 30 03               LEAX    3,X                       ; ... object header
0E97: C6 06               LDB     #$06                      ; Get "noun is second" ...
0E99: BD 0A 27            JSR     $0A27                     ; ... phrase script
0E9C: 24 08               BCC     $EA6                      ; None ... move on
0E9E: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip header
0EA1: BD 0C 03            JSR     $0C03                     ; {ProcessCommand} Execute script
0EA4: 27 1F               BEQ     $EC5                      ; Script passed ... OK and out
0EA6: B6 01 C3            LDA     $01C3                     ; {ram:FIRST_NOUN_NUM} Is there a 1st noun?
0EA9: 26 05               BNE     $EB0                      ; Yes ... go do it
0EAB: 35 10               PULS    X                         ; Restore script
0EAD: 8A 01               ORA     #$01                      ; Nobody took the phrase ..
0EAF: 39                  RTS                               ; .. error and and out
0EB0: BE 01 C6            LDX     $01C6                     ; {ram:FIRST_NOUN_DATA} First noun data
0EB3: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip ...
0EB6: 30 03               LEAX    3,X                       ; ... object header
0EB8: C6 07               LDB     #$07                      ; Get "noun is first" ...
0EBA: BD 0A 27            JSR     $0A27                     ; ... phrase script
0EBD: 24 EC               BCC     $EAB                      ; None ... error and out
0EBF: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip the id and length
0EC2: BD 0C 03            JSR     $0C03                     ; {ProcessCommand} Execute script (use return)
0EC5: 35 10               PULS    X                         ; Restore script pointer
0EC7: 39                  RTS                               ; Done

Com16_PrintVarShortName:
0EC8: 34 10               PSHS    X                         ; Save script pointer
0ECA: BE 01 C0            LDX     $01C0                     ; {ram:VAR_OBJ_DATA} Var noun data
0ECD: B6 01 BF            LDA     $01BF                     ; {ram:VAR_OBJ_NUMBER} Var noun index
0ED0: 20 08               BRA     $EDA                      ; Print short name

Com11_Print1stNounShortName:
0ED2: 34 10               PSHS    X                         ; Save script pointer
0ED4: BE 01 C6            LDX     $01C6                     ; {ram:FIRST_NOUN_DATA} 1st noun data
0ED7: B6 01 C3            LDA     $01C3                     ; {ram:FIRST_NOUN_NUM} 1st noun index
;
0EDA: 27 E9               BEQ     $EC5                      ; Return Z=1 return
0EDC: C6 1D               LDB     #$1D                      ; User object
0EDE: 34 10               PSHS    X                         ; Hold noun data
0EE0: BD 11 33            JSR     $1133                     ; Lookup user object
0EE3: BD 08 AA            JSR     $08AA                     ; User in current room?
0EE6: 35 10               PULS    X                         ; Restore noun data
0EE8: 26 11               BNE     $EFB                      ; Not in current room ... skip print
0EEA: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip object ...
0EED: 30 03               LEAX    3,X                       ; ... header
0EEF: C6 02               LDB     #$02                      ; Get object ...
0EF1: BD 0A 27            JSR     $0A27                     ; ... short name
0EF4: 24 05               BCC     $EFB                      ; No short name ... out with OK
0EF6: 30 01               LEAX    1,X                       ; Skip the 2
0EF8: BD 11 4C            JSR     $114C                     ; {PrintPackedMessage} Print packed message at X
0EFB: 35 10               PULS    X                         ; Restore script
0EFD: 4F                  CLRA                              ; Return ...
0EFE: 39                  RTS                               ; ... OK

Com12_Print2ndNounShortName:
0EFF: 34 10               PSHS    X                         ; Save script pointer
0F01: BE 01 CC            LDX     $01CC                     ; {ram:SECOND_NOUN_DATA} 2nd noun data
0F04: B6 01 C9            LDA     $01C9                     ; {ram:SECOND_NOUN_NUM} 2nd noun index
0F07: 20 D1               BRA     $EDA                      ; Print short name

Com15_CheckObjBits:
; Check target bits in an object.
0F09: 34 10               PSHS    X                         ; Hold script pointer
0F0B: BE 01 C0            LDX     $01C0                     ; {ram:VAR_OBJ_DATA} Input object pointer
0F0E: B6 01 BF            LDA     $01BF                     ; {ram:VAR_OBJ_NUMBER} Var object number
0F11: 27 0E               BEQ     $F21                      ; No object ... return error
0F13: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip the pointer-to-next object
0F16: 30 02               LEAX    2,X                       ; Skip to data byte
0F18: A6 84               LDA     ,X                        ; Get the object data
0F1A: 35 10               PULS    X                         ; Restore the script
0F1C: A4 84               ANDA    ,X                        ; Mask off all but target bits
0F1E: A8 80               EORA    ,X+                       ; Check target bits  (a 1 result in a pass)
0F20: 39                  RTS                               ; Done

0F21: 35 10               PULS    X                         ; Restore script pointer
0F23: 30 01               LEAX    1,X                       ; Skip data
0F25: 8A 01               ORA     #$01                      ; Set error
0F27: 39                  RTS                               ; Return

Com14_ExecuteCommandAndReverseReturn:
0F28: BD 0C 03            JSR     $0C03                     ; {ProcessCommand} Execute command
0F2B: 26 03               BNE     $F30                      ; Command returned a non-zero ... return zero
0F2D: 8A 01               ORA     #$01                      ; Command returned a zero ... return non-zerio
0F2F: 39                  RTS                               ; Done
0F30: 4F                  CLRA                              ; Zero
0F31: 39                  RTS                               ; Done

Com17_MoveObjectXToLocationY:
0F32: E6 80               LDB     ,X+                       ; Get object number
0F34: 34 10               PSHS    X                         ; Hold script
0F36: BD 11 33            JSR     $1133                     ; Find object
0F39: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip over length
0F3C: 35 20               PULS    Y                         ; Script to Y
0F3E: A6 A0               LDA     ,Y+                       ; Get new location
0F40: A7 84               STA     ,X                        ; Set object's new location
0F42: 1E 12               EXG     X,Y                       ; X now past data
0F44: 4F                  CLRA                              ; OK
0F45: 39                  RTS                               ; Done

Com18_CheckVarOwnedByActiveObject:
0F46: 34 10               PSHS    X                         ; Save script pointer
0F48: BE 01 C0            LDX     $01C0                     ; {ram:VAR_OBJ_DATA} Var object data
0F4B: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip length
0F4E: E6 84               LDB     ,X                        ; Location
0F50: 35 10               PULS    X                         ; Restore script
0F52: 10 27 F9 79         LBEQ    $08CF                     ; Out-of-game ... error and out
0F56: F1 01 D2            CMPB    $01D2                     ; {ram:ACTIVE_OBJ_NUM} Is this the active object?
0F59: 27 EA               BEQ     $F45                      ; Yes ... return OK
0F5B: C5 80               BITB    #$80                      ; Test upper bit
0F5D: 26 E6               BNE     $F45                      ; It is in a room ... error and out
;
0F5F: 34 10               PSHS    X                         ; Hold script
0F61: BD 11 33            JSR     $1133                     ; Look up owner object
0F64: 20 E5               BRA     $F4B                      ; Check again

; Execute any turn-scripts on the objects
0F66: 8E 20 FF            LDX     #$20FF                    ; Start of object data
0F69: 7F 01 D0            CLR     $01D0                     ; {ram:tmp1DO} Object number
0F6C: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip length
0F6F: BD 0A 58            JSR     $0A58                     ; {CompareXY} End of objects?
0F72: 24 D1               BCC     $F45                      ; Yes ... out
0F74: 7C 01 D0            INC     $01D0                     ; {ram:tmp1DO} Next object number
0F77: 34 20               PSHS    Y                         ; Hold end-of-objects
0F79: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip length
0F7C: A6 84               LDA     ,X                        ; Location
0F7E: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Hold
0F81: 34 20               PSHS    Y                         ; End of object
0F83: A6 84               LDA     ,X                        ; Location
0F85: 27 42               BEQ     $FC9                      ; If it is out-of-game it doesn't get a turn
0F87: 30 03               LEAX    3,X                       ; Skip data
0F89: C6 08               LDB     #$08                      ; Turn-script
0F8B: BD 0A 27            JSR     $0A27                     ; Find turn script
0F8E: 24 39               BCC     $FC9                      ; Nothing to do ... next object
0F90: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip length
0F93: 34 10               PSHS    X                         ; Hold pointer
0F95: BD 12 A8            JSR     $12A8                     ; Generate random number
0F98: F6 01 D0            LDB     $01D0                     ; {ram:tmp1DO} Current object number ...
0F9B: F7 01 D2            STB     $01D2                     ; {ram:ACTIVE_OBJ_NUM} ... is now the active object
0F9E: BD 11 33            JSR     $1133                     ; Get its data pointer
0FA1: BF 01 D3            STX     $01D3                     ; {ram:ACTIVE_OBJ_DATA} Hold pointer to active object data
0FA4: F6 01 AB            LDB     $01AB                     ; {ram:tmp1AB} Object's location
0FA7: 5D                  TSTB                              ; Check upper bit
0FA8: 2B 0E               BMI     $FB8                      ; If in a room ... go handle
0FAA: BD 11 33            JSR     $1133                     ; Get object's owner
0FAD: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip length
0FB0: E6 84               LDB     ,X                        ; Get owner location
0FB2: 26 F3               BNE     $FA7                      ; Still in game ... find room location of owner chain
0FB4: 35 10               PULS    X                         ; Restore pointer
0FB6: 20 11               BRA     $FC9                      ; Next object
0FB8: F7 01 D5            STB     $01D5                     ; {ram:CUR_ROOM} Objects location
0FBB: 8E 15 23            LDX     #$1523                    ; Get room ...
0FBE: BD 0A 1F            JSR     $0A1F                     ; {FindSublist} ... scripts for object
0FC1: BF 01 D6            STX     $01D6                     ; {ram:CUR_ROOM_DATA} Hold
0FC4: 35 10               PULS    X                         ; Restore turn-script
0FC6: BD 0C 03            JSR     $0C03                     ; {ProcessCommand} Execute turn-script
0FC9: 35 10               PULS    X                         ; Restore
0FCB: 35 20               PULS    Y                         ; Restore
0FCD: 20 A0               BRA     $F6F                      ; Next object

Com05_IsRandomLessOrEqual:
0FCF: B6 13 38            LDA     $1338                     ; Random value
0FD2: A1 80               CMPA    ,X+                       ; Compare random value to script
0FD4: 25 05               BCS     $FDB                      ; If less than ... OK
0FD6: 27 03               BEQ     $FDB                      ; If the same ... OK
0FD8: 8A 01               ORA     #$01                      ; Greater than ... FAIL
0FDA: 39                  RTS                               ; Done
0FDB: 4F                  CLRA                              ; Less than or equal ... OK
0FDC: 39                  RTS                               ; Done

Com1D_AttackObject:
0FDD: A6 80               LDA     ,X+                       ; Get attack value
0FDF: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Hold attack value
0FE2: 34 10               PSHS    X                         ; Hold script
0FE4: BE 01 C0            LDX     $01C0                     ; {ram:VAR_OBJ_DATA} Target object data
0FE7: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip length
0FEA: 30 03               LEAX    3,X                       ; Skip object data
0FEC: 34 10               PSHS    X                         ; Hold X ...
0FEE: 34 20               PSHS    Y                         ; ... and Y
0FF0: C6 09               LDB     #$09                      ; Get target's ...
0FF2: BD 0A 27            JSR     $0A27                     ; ... combat info
0FF5: 24 29               BCC     $1020                     ; Not found. Do nothing (return OK)
0FF7: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip length
0FFA: 30 01               LEAX    1,X                       ; Hit points
0FFC: A6 84               LDA     ,X                        ; Hit points
0FFE: B0 01 AB            SUBA    $01AB                     ; {ram:tmp1AB} Subtract attack from hit points
1001: 24 01               BCC     $1004                     ; Not negative ... keep it
1003: 4F                  CLRA                              ; Floor the hit points
1004: A7 84               STA     ,X                        ; New hit points
1006: 35 20               PULS    Y                         ; Restore ...
1008: 35 10               PULS    X                         ; ... X and Y
100A: 4D                  TSTA                              ; Hit points zero?
100B: 27 04               BEQ     $1011                     ; Yes ... object dies
100D: 35 10               PULS    X                         ; Restore list
100F: 4F                  CLRA                              ; Return OK
1010: 39                  RTS                               ; Done

;Handle object being killed
1011: C6 0A               LDB     #$0A                      ; Object being killed script
1013: BD 0A 27            JSR     $0A27                     ; Find a script for handling being killed
1016: 24 F5               BCC     $100D                     ; Not found ... nothing happens (return OK)
1018: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip id and length
101B: BD 0C 03            JSR     $0C03                     ; {ProcessCommand} Execute "being killed" script
101E: 20 ED               BRA     $100D                     ; Done (return OK)

1020: 35 20               PULS    Y                         ; Reset ...
1022: 35 10               PULS    X                         ; ... stack
1024: 20 E7               BRA     $100D                     ; Return OK

Com1E_SwapObjects:
1026: E6 80               LDB     ,X+                       ; 1st object number
1028: A6 80               LDA     ,X+                       ; 2nd object
102A: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Hold second object
102D: 34 10               PSHS    X                         ; Hold script
102F: BD 11 33            JSR     $1133                     ; Look up object
1032: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip length
1035: 1F 13               TFR     X,U                       ; 1st object pointer to U
1037: F6 01 AB            LDB     $01AB                     ; {ram:tmp1AB} 2nd object
103A: BD 11 33            JSR     $1133                     ; Look up object
103D: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip length
1040: A6 84               LDA     ,X                        ; Swap ...
1042: E6 C4               LDB     ,U                        ; ... location ...
1044: A7 C4               STA     ,U                        ; ... of ...
1046: E7 84               STB     ,X                        ; ... objects

1048: 35 10               PULS    X                         ; Restore script pointer
104A: 4F                  CLRA                              ; Z=1 OK
104B: 39                  RTS                               ; Done

Com22_CompareHealthToValue:
104C: A6 80               LDA     ,X+                       ; Get value
104E: 34 10               PSHS    X                         ; Hold script pointer
1050: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Hold value
1053: BE 01 C0            LDX     $01C0                     ; {ram:VAR_OBJ_DATA} Var object data
1056: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip length
1059: 30 03               LEAX    3,X                       ; Skip data
105B: C6 09               LDB     #$09                      ; Get object ...
105D: BD 0A 27            JSR     $0A27                     ; ... hit points
1060: 24 0E               BCC     $1070                     ; Doesn't have any ... error and out
1062: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip length
1065: 30 01               LEAX    1,X                       ; Get current ...
1067: A6 84               LDA     ,X                        ; ... hit points
1069: B1 01 AB            CMPA    $01AB                     ; {ram:tmp1AB} Compare hit points to value
106C: 25 07               BCS     $1075                     ; Less than ..
106E: 27 05               BEQ     $1075                     ; ... or equal ... OK and out
1070: 35 10               PULS    X                         ; Restore script
1072: 8A 01               ORA     #$01                      ; Error
1074: 39                  RTS                               ; Done
1075: 35 10               PULS    X                         ; Restore script
1077: 4F                  CLRA                              ; OK
1078: 39                  RTS                               ; Done

Com23_HealVarObject:
1079: A6 80               LDA     ,X+                       ; Get healing value
107B: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Hold it
107E: 34 10               PSHS    X                         ; Hold script
1080: BE 01 C0            LDX     $01C0                     ; {ram:VAR_OBJ_DATA} Var object data
1083: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip length
1086: 30 03               LEAX    3,X                       ; Skip data
1088: C6 09               LDB     #$09                      ; Get object ...
108A: BD 0A 27            JSR     $0A27                     ; ... hit points
108D: 24 E6               BCC     $1075                     ; No entry ... do nothing (but OK)
108F: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip length
1092: EC 84               LDD     ,X                        ; Get HP info
1094: FB 01 AB            ADDB    $01AB                     ; {ram:tmp1AB} Add to health
1097: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Max value
109A: F1 01 AB            CMPB    $01AB                     ; {ram:tmp1AB} Over the max?
109D: 25 03               BCS     $10A2                     ; No ... keep it
109F: F6 01 AB            LDB     $01AB                     ; {ram:tmp1AB} Use max value
10A2: 30 01               LEAX    1,X                       ; Store ...
10A4: E7 84               STB     ,X                        ; ... new health
10A6: 20 CD               BRA     $1075                     ; OK out

Com25_RestartGame:
; No return to script
10A8: 86 0D               LDA     #$0D                      ; Print first ...
10AA: BD 11 84            JSR     $1184                     ; {PrintCharacterAutoWrap} ... CR
10AD: 86 0D               LDA     #$0D                      ; Print second ...
10AF: BD 11 84            JSR     $1184                     ; {PrintCharacterAutoWrap} ... CR
10B2: 7E 06 0C            JMP     $060C                     ; Restart game

Com24_EndlessLoop:
10B5: 20 FE               BRA     $10B5                     ; {Com24_EndlessLoop} Spin forever
```

 This snippet of code is never called by anyone, but this is a print
 for null-terminate ASCII strings. Presumably the PrintScore function
 used this at one time.

```code
10B7: A6 A0               LDA     ,Y+                       ; Get next character
10B9: 27 09               BEQ     $10C4                     ; Null means done
10BB: 34 20               PSHS    Y                         ; Hold Y
10BD: BD 11 84            JSR     $1184                     ; {PrintCharacterAutoWrap} Print character
10C0: 35 20               PULS    Y                         ; Restore Y
10C2: 20 F3               BRA     $10B7                     ; Keep going
10C4: 39                  RTS                               ; Done

Com26_PrintScore:
; Second byte of object data is points. If the object is in the
; treasure room (dropped or carried) it counts double.
10C5: 34 10               PSHS    X           
10C7: 7F 01 AF            CLR     $01AF                     ; {ram:not1AF} Score tally
10CA: 7F 01 B0            CLR     $01B0                     ; {ram:not1B0} 
10CD: B6 01 D5            LDA     $01D5                     ; {ram:CUR_ROOM} Player location
10D0: 81 96               CMPA    #$96                      ; Player in the treasure room?
10D2: 26 03               BNE     $10D7                     ; No ... regular score
10D4: 7C 01 B0            INC     $01B0                     ; {ram:not1B0} Yes ... carried objects count double
10D7: 8E 20 FF            LDX     #$20FF                    ; Object data
10DA: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip header
10DD: BD 0A 58            JSR     $0A58                     ; {CompareXY} Reached end?
10E0: 24 2D               BCC     $110F                     ; Yes ... move on
10E2: 34 20               PSHS    Y                         ; Hold end
10E4: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip object length
10E7: E6 80               LDB     ,X+                       ; Get owner
10E9: C1 96               CMPB    #$96                      ; Treasure room?
10EB: 27 04               BEQ     $10F1                     ; Yes ... count it
10ED: C1 1D               CMPB    #$1D                      ; Carried by user?
10EF: 26 18               BNE     $1109                     ; No ... next object
10F1: B6 01 AF            LDA     $01AF                     ; {ram:not1AF} Score tally
10F4: AB 84               ADDA    ,X                        ; Add to score value
10F6: 19                  DAA                               ; Decimal adjust
10F7: B7 01 AF            STA     $01AF                     ; {ram:not1AF} New score
10FA: C1 96               CMPB    #$96                      ; Treasure room?
10FC: 27 05               BEQ     $1103                     ; Yes ... counts double
10FE: 7D 01 B0            TST     $01B0                     ; {ram:not1B0} Player in treasure room?
1101: 27 06               BEQ     $1109                     ; No ... just count once
1103: AB 84               ADDA    ,X                        ; Double ...
1105: 19                  DAA                               ; ... the ...
1106: B7 01 AF            STA     $01AF                     ; {ram:not1AF} ... score value
1109: 1F 21               TFR     Y,X                       ; Next object
110B: 35 20               PULS    Y                         ; Restore end of list
110D: 20 CE               BRA     $10DD                     ; Do all objects
;        
110F: B6 01 AF            LDA     $01AF                     ; {ram:not1AF} Score value
1112: 47                  ASRA                              ; Left ...
1113: 47                  ASRA                              ; ... most ...
1114: 47                  ASRA                              ; ... digit ...
1115: 47                  ASRA                              ; ... value
1116: 8B 30               ADDA    #$30                      ; Convert to ASCII
1118: BD 11 84            JSR     $1184                     ; {PrintCharacterAutoWrap} Print the left digit
111B: B6 01 AF            LDA     $01AF                     ; {ram:not1AF} Score value
111E: 84 0F               ANDA    #$0F                      ; Mask off the right digit
1120: 8B 30               ADDA    #$30                      ; Convert ot ASCII
1122: BD 11 84            JSR     $1184                     ; {PrintCharacterAutoWrap} Print the right digit
1125: 86 2E               LDA     #$2E                      ; Print ...
1127: BD 11 84            JSR     $1184                     ; {PrintCharacterAutoWrap} ... "."
112A: 86 20               LDA     #$20                      ; Print ...
112C: BD 11 84            JSR     $1184                     ; {PrintCharacterAutoWrap} ... SPACE
112F: 35 10               PULS    X                         ; Restore script
1131: 4F                  CLRA                              ; OK
1132: 39                  RTS                               ; Done

; Find object index in B
1133: 8E 20 FF            LDX     #$20FF                    ; Start of objects
1136: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Skip end
1139: 5A                  DECB                              ; Found desired object?
113A: 27 88               BEQ     $10C4                     ; Yes ... out OK
113C: BD 0A 42            JSR     $0A42                     ; {SkipIDLoadEnd} Length of object
113F: 1E 12               EXG     X,Y                       ; Next object
1141: 20 F6               BRA     $1139                     ; Keep looking

; Print packed message and CR
1143: BD 11 4C            JSR     $114C                     ; {PrintPackedMessage} Print packed message at X
1146: 86 0D               LDA     #$0D                      ; Print ...
1148: BD 11 84            JSR     $1184                     ; {PrintCharacterAutoWrap} ... CR
114B: 39                  RTS                               ; Done
```

# Print Packed Message

```code
PrintPackedMessage: 
; X points to compressed string. First byte (or two) is the length.
114C: 4F                  CLRA                              ; Assume MSB is 0
114D: E6 84               LDB     ,X                        ; Get length
114F: C5 80               BITB    #$80                      ; Is it single byte length?
1151: 27 04               BEQ     $1157                     ; Yes ... use D
1153: A6 80               LDA     ,X+                       ; Get the ...
1155: 84 7F               ANDA    #$7F                      ; ... MSB and ...
1157: E6 80               LDB     ,X+                       ; ... LSB
1159: FD 01 AB            STD     $01AB                     ; {ram:tmp1AB} Store byte count
115C: FC 01 AB            LDD     $01AB                     ; {ram:tmp1AB} Number of bytes left in message
115F: 10 83 00 02         CMPD    #$0002                    ; Less than 2?
1163: 25 0E               BCS     $1173                     ; Yes ... these aren't compressed
1165: BD 11 EC            JSR     $11EC                     ; {UnpackBytes} Decompress and print two bytes pointed to by X
1168: FC 01 AB            LDD     $01AB                     ; {ram:tmp1AB} Get byte count
116B: 83 00 02            SUBD    #$0002                    ; Handled 2
116E: FD 01 AB            STD     $01AB                     ; {ram:tmp1AB} Store count
1171: 20 E9               BRA     $115C                     ; Keep decompressing
1173: 5D                  TSTB                              ; Any characters on the end to print?
1174: 27 08               BEQ     $117E                     ; No ... skip
1176: A6 80               LDA     ,X+                       ; Get character
1178: BD 11 84            JSR     $1184                     ; {PrintCharacterAutoWrap} Print the character
117B: 5A                  DECB                              ; Decrement count
117C: 20 F5               BRA     $1173                     ; Keeop going
117E: 86 20               LDA     #$20                      ; Print ...
1180: BD 11 84            JSR     $1184                     ; {PrintCharacterAutoWrap} ... space on end
1183: 39                  RTS                               ; Done
```
 
# Print Character

```code
PrintCharacterAutoWrap:
; Print character in A to screen. This handles auto word-wrapping and
; auto MORE prompting.
;
1184: 34 06               PSHS    B,A                       ; Hold B and A
1186: B6 01 BE            LDA     $01BE                     ; {ram:lastChar} Last printed character
1189: 81 20               CMPA    #$20                      ; Last printed a space?
118B: 26 1A               BNE     $11A7                     ; No ... print this
118D: 35 06               PULS    A,B                       ; Hold
118F: 81 20               CMPA    #$20                      ; Space now?
1191: 27 57               BEQ     $11EA                     ; Yes ... just ignore
1193: 81 2E               CMPA    #$2E                      ; A '.' ?
1195: 27 08               BEQ     $119F                     ; Yes. Ignore leading space.
1197: 81 3F               CMPA    #$3F                      ; A '?' ?
1199: 27 04               BEQ     $119F                     ; Yes. Ignore leading space.
119B: 81 21               CMPA    #$21                      ; A '!' ?
119D: 26 0A               BNE     $11A9                     ; Yes. Ignore leading space.
119F: DE 88               LDU     <$88                      ; {ram:printCursor} Back screen ...
11A1: 33 5F               LEAU    -1,U                      ; ... pointer up ...
11A3: DF 88               STU     <$88                      ; {ram:printCursor} ... over ignored space
11A5: 20 02               BRA     $11A9                     ; Store and print
11A7: 35 06               PULS    A,B                       ; Restore A and B
11A9: B7 01 BE            STA     $01BE                     ; {ram:lastChar} Last printed character
11AC: AD 9F A0 02         JSR     [$A002]                   ; {hard:CHROUT} Output character
11B0: 96 89               LDA     <$89                      ; {ram:printCursor} LSB of screen position
11B2: 81 FE               CMPA    #$FE                      ; Reached end of screen?
11B4: 25 34               BCS     $11EA                     ; No ... done
11B6: DE 88               LDU     <$88                      ; {ram:printCursor} Cursor position
11B8: 33 C8 DF            LEAU    $-21,U                    ; Back up to end of current row
11BB: 86 0D               LDA     #$0D                      ; CR ...
11BD: AD 9F A0 02         JSR     [$A002]                   ; {hard:CHROUT} ... to screen
11C1: A6 C4               LDA     ,U                        ; Find the ...
11C3: 81 60               CMPA    #$60                      ; ... space before ...
11C5: 27 04               BEQ     $11CB                     ; ... the last ...
11C7: 33 5F               LEAU    -1,U                      ; ... word ...
11C9: 20 F6               BRA     $11C1                     ; ... on the line
11CB: 33 41               LEAU    1,U                       ; Now pointing to last word on line
11CD: A6 C4               LDA     ,U                        ; Get next character in buffer
11CF: 81 60               CMPA    #$60                      ; Is it a space?
11D1: 27 17               BEQ     $11EA                     ; Yes ... all done
11D3: 34 04               PSHS    B                         ; Hold B
11D5: C6 60               LDB     #$60                      ; Put ...
11D7: E7 C4               STB     ,U                        ; ... space
11D9: 35 04               PULS    B                         ; Restore B
11DB: 81 60               CMPA    #$60                      ; Make sure ...
11DD: 25 02               BCS     $11E1                     ; ... upper ...
11DF: 80 40               SUBA    #$40                      ; ... case
11E1: B7 01 BE            STA     $01BE                     ; {ram:lastChar} Last printed character
11E4: AD 9F A0 02         JSR     [$A002]                   ; {hard:CHROUT} Output to screen
11E8: 20 E1               BRA     $11CB                     ; Move overhang to next line
11EA: 39                  RTS                               ; Done
11EB: 39                  RTS                               ; OOPS
```

# Unpack Bytes

```code
UnpackBytes:
; Unpack three characters stored in 2 bytes pointed to by X and print to screen.
; Every 2 bytes holds 3 characters. Each character can be from 0 to 39.
; 40*40*40 = 64000 ... totally ingenious.
;
11EC: 10 8E 12 A4         LDY     #$12A4                    ;
11F0: C6 03               LDB     #$03                      ;
11F2: F7 12 A1            STB     $12A1                     ; 
11F5: A6 80               LDA     ,X+                       ;
11F7: B7 01 DE            STA     $01DE                     ; {ram:tmp1DE} 
11FA: A6 80               LDA     ,X+                       ;
11FC: B7 01 DD            STA     $01DD                     ; {ram:tmp1DD} 
11FF: 31 23               LEAY    3,Y                       ;
1201: CE 00 28            LDU     #$0028                    ;
1204: FF 12 A2            STU     $12A2                     ; 
1207: 86 11               LDA     #$11                      ;
1209: B7 01 DA            STA     $01DA                     ; {ram:tmp1DA} 
120C: 7F 01 DB            CLR     $01DB                     ; {ram:tmp1DB} 
120F: 7F 01 DC            CLR     $01DC                     ; {ram:tmp1DC} 
1212: 79 01 DE            ROL     $01DE                     ; {ram:tmp1DE} 
1215: 79 01 DD            ROL     $01DD                     ; {ram:tmp1DD} 
1218: 7A 01 DA            DEC     $01DA                     ; {ram:tmp1DA} 
121B: 27 39               BEQ     $1256                     ; 
121D: 86 00               LDA     #$00                      ;
121F: 89 00               ADCA    #$00                      ; This algorithm is identical to the decompression
1221: 78 01 DC            ASL     $01DC                     ; {ram:tmp1DC} used in Pyramid2000. Check the comments there for
1224: 79 01 DB            ROL     $01DB                     ; {ram:tmp1DB} more detail.
1227: BB 01 DC            ADDA    $01DC                     ; {ram:tmp1DC} 
122A: B0 12 A3            SUBA    $12A3                     ; 
122D: B7 01 E0            STA     $01E0                     ; {ram:tmp1EO} 
1230: B6 01 DB            LDA     $01DB                     ; {ram:tmp1DB} 
1233: B2 12 A2            SBCA    $12A2                     ; 
1236: B7 01 DF            STA     $01DF                     ; {ram:tmp1DF} 
1239: 24 0B               BCC     $1246                     ; 
123B: FC 01 DF            LDD     $01DF                     ; {ram:tmp1DF} 
123E: F3 12 A2            ADDD    $12A2                     ; 
1241: FD 01 DB            STD     $01DB                     ; {ram:tmp1DB} 
1244: 20 06               BRA     $124C                     ; 
1246: FC 01 DF            LDD     $01DF                     ; {ram:tmp1DF} 
1249: FD 01 DB            STD     $01DB                     ; {ram:tmp1DB} 
; Compliment C flag and continue
124C: 25 04               BCS     $1252                     ; 
124E: 1A 01               ORCC    #$01                      ;
1250: 20 C0               BRA     $1212                     ; 
1252: 1C FE               ANDCC   #$FE                      ;
1254: 20 BC               BRA     $1212                     ; 
; Process the result of the division
1256: FC 01 DB            LDD     $01DB                     ; {ram:tmp1DB} 
1259: C3 12 79            ADDD    #$1279                    ;
125C: 1F 03               TFR     D,U                       ;
125E: A6 C4               LDA     ,U                        ;
1260: A7 A2               STA     ,-Y                       ;
1262: 7A 12 A1            DEC     $12A1                     ; 
1265: 26 9A               BNE     $1201                     ; 
1267: 10 8E 12 A4         LDY     #$12A4                    ;
126B: C6 03               LDB     #$03                      ;
126D: A6 A0               LDA     ,Y+                       ;
126F: BD 11 84            JSR     $1184                     ; {PrintCharacterAutoWrap} Print character
1272: 5A                  DECB                              ;
1273: 26 F8               BNE     $126D                     ; 
1275: FC 01 AB            LDD     $01AB                     ; {ram:tmp1AB} 
1278: 39                  RTS                               ;

; Character translation table
;     ?  !  2  .  "  '  <  >  /  0  3  A  B  C  D  E
1279: 3F 21 32 20 22 27 3C 3E 2F 30 33 41 42 43 44 45                 
;     F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U
1289: 46 47 48 49 4A 4B 4C 4D 4E 4F 50 51 52 53 54 55                 
1299: 56 57 58 59 5A 2D 2C 2E
;     V  W  X  Y  Z  -  ,  .

12A1: 00 00 00 00 00 00 00  ; Temporaries for decompression algorithm above            

; Generate random number
12A8: 34 14               PSHS    X,B                       ; Random number generator. Uses seed at 1338.
12AA: 8E 13 38            LDX     #$1338                    ;
12AD: C6 17               LDB     #$17                      ;
12AF: A6 84               LDA     ,X                        ;
12B1: 30 01               LEAX    1,X                       ;
12B3: 1A 01               ORCC    #$01                      ;
12B5: 84 06               ANDA    #$06                      ;
12B7: 27 07               BEQ     $12C0                     ; 
12B9: 81 06               CMPA    #$06                      ;
12BB: 1A 01               ORCC    #$01                      ;
12BD: 27 01               BEQ     $12C0                     ; 
12BF: 4F                  CLRA                              ;
12C0: A6 84               LDA     ,X                        ;
12C2: 25 03               BCS     $12C7                     ; 
12C4: 44                  LSRA                              ;
12C5: 20 03               BRA     $12CA                     ; 
12C7: 44                  LSRA                              ;
12C8: 8A 80               ORA     #$80                      ;
12CA: A7 84               STA     ,X                        ;
12CC: 30 1F               LEAX    -1,X                      ;
12CE: A6 84               LDA     ,X                        ;
12D0: 25 03               BCS     $12D5                     ; 
12D2: 44                  LSRA                              ;
12D3: 20 03               BRA     $12D8                     ; 
12D5: 44                  LSRA                              ;
12D6: 8A 80               ORA     #$80                      ;
12D8: 84 FE               ANDA    #$FE                      ;
12DA: A7 84               STA     ,X                        ;
12DC: 5A                  DECB                              ;
12DD: 26 D2               BNE     $12B1                     ; 
12DF: B6 13 39            LDA     $1339                     ; 
12E2: 35 14               PULS    B,X                       ;
12E4: 39                  RTS                               ;
```

# Data Section 

## Command Jump Table

```code
CommandJumpTable: 
12E5: 0C 81  ; 00            
12E7: 0D 93  ; 01            
12E9: 0D A6  ; 02            
12EB: 0D AB  ; 03            
12ED: 0D C3  ; 04            
12EF: 0F CF  ; 05            
12F1: 0D E9  ; 06            
12F3: 0D E4  ; 07            
12F5: 0E 23  ; 08            
12F7: 0E 41  ; 09           
12F9: 0E 49  ; 0A            
12FB: 0C 58  ; 0B            
12FD: 0D C0  ; 0C           
12FF: 0C 27  ; 0D           
1301: 0C 3F  ; 0E            
1303: 0E 4F  ; 0F           
1305: 0E 60  ; 10            
1307: 0E D2  ; 11           
1309: 0E FF  ; 12            
130B: 0E 71  ; 13            
130D: 0F 28  ; 14           
130F: 0F 09  ; 15            
1311: 0E C8  ; 16            
1313: 0F 32  ; 17            
1315: 0F 46  ; 18            
1317: 0C 8D  ; 19           
1319: 0C AE  ; 1A           
131B: 0C BC  ; 1B            
131D: 0C CA  ; 1C           
131F: 0F DD  ; 1D            
1321: 10 26  ; 1E
1323: 0D CA  ; 1F          
1325: 0D A0  ; 20            
1327: 0C DD  ; 21            
1329: 10 4C  ; 22                
132B: 10 79  ; 23               
132D: 10 B5  ; 24                
132F: 10 A8  ; 25               
1331: 10 C5  ; 26
  
; Multi-verb replacement list (code doesn't work that uses this anyway)              
1333: 00  ; List is the length. List is pointed to by 1331 which is ignored

; Random number seed
1334: 12 23 44 1D 
1338: 27 4D 2D 13  
```
       
## Feedback Prompts

```code
FeedbackPrompts: 
; "?VERB?"  
133C: 06 3F 56 45 52 42 3F                  
;       
; "?WHAT?"
1343: 06 3F 57 48 41 54 3F          
;          
; "?WHICH?"        
134A: 07 3F 57 48 49 43 48 3F         
;           
; "?PHRASE?"         
1352: 08 3F 50 48 52 41 53 45 3F                  
```

## Phrase List

```code
PhraseList: 
; The noun values are bits that must be set in the target noun. The value for a noun in this table must be 
; non-zero since a zero in the phrase means no-word. If no other bit is flagged then the upper bit is set
; (all objects have the upper bit set). The upper bit is set with "A", but it doesn't have to be.
;
;    Bits: uvCPAXOL
;    v=1 if object is a true weapon (only sword has this set)
;    C=1 if object can be carried
;    P=1 if object is a person;
;    A=1 if open/close-able
;    X=1 if lock/unlock-able 
;    O=1 if closed
;    L=1 if locked
;                                                               ; #   Verb    Prep   Noun1      Noun2
135B: 05 00 00 00 01                                            ; 01: NORTH   *      *          *       
1360: 06 00 00 00 02                                            ; 02: SOUTH   *      *          *       
1365: 07 00 00 00 03                                            ; 03: EAST    *      *          *       
136A: 08 00 00 00 04                                            ; 04: WEST    *      *          *       
136F: 09 00 20 00 05                                            ; 05: GET     *      ..C.....   *       
1374: 34 07 00 80 05                                            ; 05: PICK    UP     *          u.......
1379: 34 07 80 00 05                                            ; 05: PICK    UP     u.......   *       
137E: 0A 00 20 00 06                                            ; 06: DROP    *      ..C.....   *       
1383: 0A 05 80 80 0F                                            ; 0F: DROP    IN     u.......   u.......
1388: 0A 06 00 88 16                                            ; 16: DROP    OUT    *          u...A...
138D: 0B 00 00 00 07                                            ; 07: INVENT  *      *          *       
1392: 01 00 04 00 08                                            ; 08: READ    *      .....X..   *       
1397: 04 02 10 40 09                                            ; 09: ATTACK  WITH   ...P....   .v......
139C: 0C 00 00 00 0A                                            ; 0A: LOOK    *      *          *       
13A1: 0C 03 00 80 0B                                            ; 0B: LOOK    AT     *          u.......
13A6: 0C 04 00 80 0C                                            ; 0C: LOOK    UNDER  *          u.......
13AB: 0C 05 00 80 10                                            ; 10: LOOK    IN     *          u.......
13B0: 03 03 40 10 0D                                            ; 0D: THROW   AT     .v......   ...P....
13B5: 03 05 80 80 39                                            ; 39: THROW   IN     u.......   u.......
13BA: 03 08 00 20 06                                            ; 06: THROW   DOWN   *          ..C.....
13BF: 03 01 80 10 0E                                            ; 0E: THROW   TO     u.......   ...P....
13C4: 0D 01 80 10 0E                                            ; 0E: GIVE    TO     u.......   ...P....
13C9: 0E 00 80 00 0B                                            ; 0B: EXAMIN  *      u.......   *       
13CE: 0E 05 00 80 0B                                            ; 0B: EXAMIN  IN     *          u.......
13D3: 0F 00 80 00 11                                            ; 11: OPEN    *      u.......   *       
13D8: 0F 02 80 80 3A                                            ; 3A: OPEN    WITH   u.......   u.......
13DD: 10 00 80 00 12                                            ; 12: PULL    *      u.......   *       
13E2: 10 08 00 80 12                                            ; 12: PULL    DOWN   *          u.......
13E7: 10 06 00 80 05                                            ; 05: PULL    OUT    *          u.......
13EC: 10 06 80 00 05                                            ; 05: PULL    OUT    u.......   *       
13F1: 10 07 00 80 2D                                            ; 2D: PULL    UP     *          u.......
13F6: 10 07 80 00 2D                                            ; 2D: PULL    UP     u.......   *       
13FB: 11 02 88 88 14                                            ; 14: LIGHT   WITH   u...A...   u...A...
1400: 12 00 80 00 15                                            ; 15: EAT     *      u.......   *       
1405: 13 06 00 88 16                                            ; 16: BLOW    OUT    *          u...A...
140A: 14 00 88 00 16                                            ; 16: EXTING  *      u...A...   *       
140F: 15 00 80 00 17                                            ; 17: CLIMB   *      u.......   *       
1414: 15 07 00 80 17                                            ; 17: CLIMB   UP     *          u.......
1419: 15 08 00 80 17                                            ; 17: CLIMB   DOWN   *          u.......
141E: 15 09 00 80 17                                            ; 17: CLIMB   OVER   *          u.......
1423: 15 0C 00 80 17                                            ; 17: CLIMB   ON     *          u.......
1428: 15 05 00 00 36                                            ; 36: CLIMB   IN     *          *       
142D: 15 05 00 80 36                                            ; 36: CLIMB   IN     *          u.......
1432: 15 06 00 00 37                                            ; 37: CLIMB   OUT    *          *       
1437: 15 06 00 80 37                                            ; 37: CLIMB   OUT    *          u.......
143C: 15 04 00 80 38                                            ; 38: CLIMB   UNDER  *          u.......
1441: 16 00 80 00 18                                            ; 18: RUB     *      u.......   *       
1446: 18 00 00 00 1A                                            ; 1A: ???     *      *          *       
144B: 05 01 00 00 01                                            ; 01: NORTH   TO     *          *       
1450: 06 01 00 00 02                                            ; 02: SOUTH   TO     *          *       
1455: 07 01 00 00 03                                            ; 03: EAST    TO     *          *       
145A: 08 01 00 00 04                                            ; 04: WEST    TO     *          *       
145F: 0A 08 00 20 06                                            ; 06: DROP    DOWN   *          ..C.....
1464: 0A 08 20 00 06                                            ; 06: DROP    DOWN   ..C.....   *       
1469: 0A 0A 20 80 06                                            ; 06: DROP    BEHIND ..C.....   u.......
146E: 0A 04 20 80 06                                            ; 06: DROP    UNDER  ..C.....   u.......
1473: 0A 0C 20 80 06                                            ; 06: DROP    ON     ..C.....   u.......
1478: 0C 07 00 00 0A                                            ; 0A: LOOK    UP     *          *       
147D: 0C 08 00 00 0A                                            ; 0A: LOOK    DOWN   *          *       
1482: 0C 09 80 00 0B                                            ; 0B: LOOK    OVER   u.......   *       
1487: 0C 09 00 80 0B                                            ; 0B: LOOK    OVER   *          u.......
148C: 0C 0B 00 00 0A                                            ; 0A: LOOK    AROUND *          *       
1491: 0C 0A 00 00 0A                                            ; 0A: LOOK    BEHIND *          *       
1496: 0C 0B 00 80 1B                                            ; 1B: LOOK    AROUND *          u.......
149B: 0C 0A 00 80 1C                                            ; 1C: LOOK    BEHIND *          u.......
14A0: 32 00 00 00 21                                            ; 21: PLUGH   *      *          *       
14A5: 2B 00 00 00 22                                            ; 22: SCREAM  *      *          *       
14AA: 2D 00 00 00 23                                            ; 23: QUIT    *      *          *       
14AF: 2C 00 00 00 25                                            ; 25: LEAVE   *      *          *       
14B4: 2C 00 20 00 06                                            ; 06: LEAVE   *      ..C.....   *       
14B9: 21 00 00 00 25                                            ; 25: GO      *      *          *       
14BE: 21 01 00 80 3D                                            ; 3D: GO      TO     *          u.......
14C3: 21 05 00 80 36                                            ; 36: GO      IN     *          u.......
14C8: 21 06 00 80 37                                            ; 37: GO      OUT    *          u.......
14CD: 21 04 00 80 38                                            ; 38: GO      UNDER  *          u.......
14D2: 21 07 00 80 17                                            ; 17: GO      UP     *          u.......
14D7: 21 08 00 80 17                                            ; 17: GO      DOWN   *          u.......
14DC: 21 0B 00 80 26                                            ; 26: GO      AROUND *          u.......
14E1: 23 00 80 00 27                                            ; 27: KICK    *      u.......   *       
14E6: 23 08 00 80 27                                            ; 27: KICK    DOWN   *          u.......
14EB: 23 05 00 80 27                                            ; 27: KICK    IN     *          u.......
14F0: 24 02 10 80 28                                            ; 28: FEED    WITH   ...P....   u.......
14F5: 24 01 80 10 29                                            ; 29: FEED    TO     u.......   ...P....
14FA: 28 00 00 00 2C                                            ; 2C: SCORE   *      *          *       
14FF: 1C 00 80 00 2D                                            ; 2D: LIFT    *      u.......   *       
1504: 1F 00 00 00 2F                                            ; 2F: WAIT    *      *          *       
1509: 1F 0B 00 00 2F                                            ; 2F: WAIT    AROUND *          *       
150E: 09 07 00 00 2F                                            ; 2F: GET     UP     *          *       
1513: 20 09 00 80 34                                            ; 34: JUMP    OVER   *          u.......
1518: 20 05 00 80 36                                            ; 36: JUMP    IN     *          u.......
151D: 20 06 00 80 37                                            ; 37: JUMP    OUT    *          u.......
1522: 00 
```

## Room Descriptions

```code
RoomDescriptions:
1523: 00 8B D9                                                  ; Script list size=0BD9
1526:   81 5E 00                                                ;   Script number=81 size=005E data=00
1529:     03 52                                                 ;     Data tag=03 size=0052
152B:       C7 DE 94 14 4B 5E 83 96 5F 17 46 48                 ;       YOU ARE IN A SMALL ROOM WITH GRANITE WALLS
1537:       39 17 DB 9F 56 D1 09 71 D0 B0 7F 7B                 ;       AND FLOOR. THERE IS A SMALL OPENING TO THE
1543:       F3 17 0D 8D 90 14 08 58 81 8D 1B B5                 ;       EAST AND A LARGE HOLE IN THE CEILING.
154F:       5F BE 5B B1 4B 7B 55 45 8E 91 11 8A                 ;       .
155B:       F0 A4 91 7A 89 17 82 17 47 5E 66 49                 ;       .
1567:       90 14 03 58 3B 16 B7 B1 A9 15 DB 8B                 ;       .
1573:       83 7A 5F BE D7 14 43 7A CF 98                       ;       .
157D:   04 07                                                   ;     Data tag=04 size=0007
157F:         0B 05                                             ;         Command_0B_SWITCH size=05
1581:           0A 03                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
1583:           02                                              ;           IF_NOT_JUMP address=1586
1584:             00 82                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=82
1586:   82 80 C4 00                                             ;   Script number=82 size=00C4 data=00
158A:     03 80 AB                                              ;     Data tag=03 size=00AB
158D:       C7 DE 94 14 4B 5E 83 96 3B 16 B7 B1                 ;       YOU ARE IN A LARGE RECTANGULAR ROOM. ON THE
1599:       2F 17 FB 55 C7 98 54 8B 39 17 FF 9F                 ;       FLOOR OF THE EAST SIDE OF THE ROOM IS AN
15A5:       C0 16 82 17 48 5E 81 8D 91 AF 96 64                 ;       INTRICATE ORIENTAL RUG STRETCHING BETWEEN
15B1:       DB 72 95 5F 15 BC FF 78 B8 16 82 17                 ;       THE NORTH AND SOUTH WALLS. IN THE EAST WALL
15BD:       54 5E 3F A0 D5 15 90 14 D0 15 F3 BF                 ;       IS A HUGE CARVED WOODEN DOOR. TO THE SOUTH,
15C9:       16 53 51 5E 07 B2 BB 9A 14 8A 6B C4                 ;       A SMALL HOLE LEADS TO A DARK PASSAGE WAY.
15D5:       0C BA 7D 62 90 73 C4 6A 91 62 30 60                 ;       .
15E1:       82 17 50 5E BE A0 03 71 33 98 47 B9                 ;       .
15ED:       53 BE 0E D0 2F 8E D0 15 82 17 47 5E                 ;       .
15F9:       66 49 F3 17 F3 8C 4B 7B 4A 45 77 C4                 ;       .
1605:       D3 14 0F B4 19 58 36 A0 83 61 81 5B                 ;       .
1611:       1B B5 6B BF 5F BE 61 17 82 C6 03 EE                 ;       .
161D:       5F 17 46 48 A9 15 DB 8B E3 8B 0B 5C                 ;       .
1629:       6B BF 46 45 35 49 DB 16 D3 B9 9B 6C                 ;       .
1635:       1B D0 2E                                            ;       .
1638:     04 13                                                 ;     Data tag=04 size=0013
163A:         0B 11                                             ;         Command_0B_SWITCH size=11
163C:           0A 04                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
163E:           02                                              ;           IF_NOT_JUMP address=1641
163F:             00 81                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=81
1641:           02                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=02 phrase="02: SOUTH *     *          *       "
1642:           02                                              ;           IF_NOT_JUMP address=1645
1643:             00 83                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=83
1645:           03                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
1646:           06                                              ;           IF_NOT_JUMP address=164D
1647:             0D 04                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=4
1649:               20 1D                                       ;               Command_20_CHECK_ACTIVE_OBJECT object=1D(USER)
164B:               8B                                          ;               CommonCommand_8B
164C:               81                                          ;               CommonCommand_81
164D:   83 3A 00                                                ;   Script number=83 size=003A data=00
1650:     03 2A                                                 ;     Data tag=03 size=002A
1652:       C7 DE 94 14 4B 5E 83 96 FB 14 4B B2                 ;       YOU ARE IN A DARK PASSAGE WAY WHICH SLOPES
165E:       55 A4 09 B7 59 5E 3B 4A 23 D1 13 54                 ;       UP AND TO THE SOUTH.
166A:       C9 B8 F5 A4 B2 17 90 14 16 58 D6 9C                 ;       .
1676:       DB 72 47 B9 77 BE                                   ;       .
167C:     04 0B                                                 ;     Data tag=04 size=000B
167E:         0B 09                                             ;         Command_0B_SWITCH size=09
1680:           0A 01                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=01 phrase="01: NORTH *     *          *       "
1682:           02                                              ;           IF_NOT_JUMP address=1685
1683:             00 82                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=82
1685:           02                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=02 phrase="02: SOUTH *     *          *       "
1686:           02                                              ;           IF_NOT_JUMP address=1689
1687:             00 84                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=84
1689:   84 67 00                                                ;   Script number=84 size=0067 data=00
168C:     03 53                                                 ;     Data tag=03 size=0053
168E:       C7 DE 94 14 43 5E 16 BC DB 72 82 BF                 ;       YOU ARE AT THE TOP OF A PASSAGE WHICH SLOPES
169A:       B8 16 7B 14 55 A4 09 B7 59 5E 85 73                 ;       DOWN AND TO THE NORTH. THERE IS A CORRIDOR
16A6:       15 71 82 8D 4B 62 89 5B 83 96 33 98                 ;       TO THE EAST AND ANOTHER TO THE WEST.
16B2:       6B BF 5F BE 99 16 C2 B3 56 F4 F4 72                 ;       .
16BE:       4B 5E C3 B5 E1 14 73 B3 84 5B 89 17                 ;       .
16CA:       82 17 47 5E 66 49 90 14 03 58 06 9A                 ;       .
16D6:       F4 72 89 17 82 17 59 5E 66 62 2E                    ;       .
16E1:     04 0F                                                 ;     Data tag=04 size=000F
16E3:         0B 0D                                             ;         Command_0B_SWITCH size=0D
16E5:           0A 01                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=01 phrase="01: NORTH *     *          *       "
16E7:           02                                              ;           IF_NOT_JUMP address=16EA
16E8:             00 83                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=83
16EA:           04                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
16EB:           02                                              ;           IF_NOT_JUMP address=16EE
16EC:             00 A1                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=A1
16EE:           03                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
16EF:           02                                              ;           IF_NOT_JUMP address=16F2
16F0:             00 85                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=85
16F2:   85 44 00                                                ;   Script number=85 size=0044 data=00
16F5:     03 26                                                 ;     Data tag=03 size=0026
16F7:       63 BE CB B5 C3 B5 73 17 1B B8 E6 A4                 ;       THIS IS A T SHAPED ROOM WITH EXITS EAST,
1703:       39 17 DB 9F 56 D1 07 71 96 D7 C7 B5                 ;       SOUTH, AND WEST.
170F:       66 49 15 EE 36 A1 73 76 8E 48 F7 17                 ;       .
171B:       17 BA                                               ;       .
171D:     04 19                                                 ;     Data tag=04 size=0019
171F:         0B 17                                             ;         Command_0B_SWITCH size=17
1721:           0A 04                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
1723:           02                                              ;           IF_NOT_JUMP address=1726
1724:             00 84                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=84
1726:           02                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=02 phrase="02: SOUTH *     *          *       "
1727:           02                                              ;           IF_NOT_JUMP address=172A
1728:             00 86                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=86
172A:           03                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
172B:           0C                                              ;           IF_NOT_JUMP address=1738
172C:             0D 0A                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=10
172E:               00 88                                       ;               Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=88
1730:               14                                          ;               Command_14_EXECUTE_COMMAND_REVERSE_STATUS
1731:                 0D 05                                     ;                 Command_0D_EXECUTE_LIST_WHILE_PASS size=5
1733:                   20 1D                                   ;                   Command_20_CHECK_ACTIVE_OBJECT object=1D(USER)
1735:                   01 07                                   ;                   Command_01_IS_OBJECT_IN_PACK_OR_ROOM object=07(StatueWest)
1737:                   82                                      ;                   CommonCommand_82
1738:   86 3F 00                                                ;   Script number=86 size=003F data=00
173B:     03 2F                                                 ;     Data tag=03 size=002F
173D:       C7 DE 94 14 4B 5E 83 96 39 17 DB 9F                 ;       YOU ARE IN A ROOM WITH GRAY STONE WALLS.
1749:       56 D1 09 71 DB B0 66 17 0F A0 F3 17                 ;       PASSAGES LEAD NORTH AND EAST.
1755:       0D 8D 52 F4 65 49 77 47 CE B5 86 5F                 ;       .
1761:       99 16 C2 B3 90 14 07 58 66 49 2E                    ;       .
176C:     04 0B                                                 ;     Data tag=04 size=000B
176E:         0B 09                                             ;         Command_0B_SWITCH size=09
1770:           0A 01                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=01 phrase="01: NORTH *     *          *       "
1772:           02                                              ;           IF_NOT_JUMP address=1775
1773:             00 85                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=85
1775:           03                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
1776:           02                                              ;           IF_NOT_JUMP address=1779
1777:             00 87                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=87
1779:   87 44 00                                                ;   Script number=87 size=0044 data=00
177C:     03 2F                                                 ;     Data tag=03 size=002F
177E:       63 BE CB B5 C3 B5 39 17 8E C5 39 17                 ;       THIS IS A ROUND ROOM WITH HIGH WALLS. THE
178A:       DB 9F 56 D1 0A 71 7A 79 F3 17 0D 8D                 ;       ONLY OPENING IS TO THE WEST.
1796:       56 F4 DB 72 16 A0 51 DB F0 A4 91 7A                 ;       .
17A2:       D5 15 89 17 82 17 59 5E 66 62 2E                    ;       .
17AD:     04 10                                                 ;     Data tag=04 size=0010
17AF:         0B 0E                                             ;         Command_0B_SWITCH size=0E
17B1:           0A 05                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=05 phrase="05: GET *       ..C.....   *       "
17B3:           07                                              ;           IF_NOT_JUMP address=17BB
17B4:             0D 05                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=5
17B6:               08 08                                       ;               Command_08_COMPARE_OBJECT_TO_FIRST_NOUN object=08(GoldRing
17B8:               19 8C                                       ;               Command_19_MOVE_ACTIVE_OBJECT_TO_ROOM room=8C
17BA:               0C                                          ;               Command_0C_FAIL
17BB:           04                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
17BC:           02                                              ;           IF_NOT_JUMP address=17BF
17BD:             00 86                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=86
17BF:   88 79 00                                                ;   Script number=88 size=0079 data=00
17C2:     03 57                                                 ;     Data tag=03 size=0057
17C4:       C7 DE 94 14 4B 5E 83 96 8C 17 90 78                 ;       YOU ARE IN A TRIANGULAR ROOM WITH OPENINGS
17D0:       2E 6F 23 49 01 B3 59 90 82 7B C2 16                 ;       IN THE EAST AND WEST CORNERS. THERE IS A
17DC:       93 61 C5 98 D0 15 82 17 47 5E 66 49                 ;       STATUE IN THE SOUTH CORNER WITH BOW AND
17E8:       90 14 19 58 66 62 E1 14 CF B2 AF B3                 ;       ARROW.
17F4:       82 17 2F 62 D5 15 7B 14 FB B9 67 C0                 ;       .
1800:       D0 15 82 17 55 5E 36 A1 05 71 B8 A0                 ;       .
180C:       23 62 56 D1 04 71 6B A1 8E 48 94 14                 ;       .
1818:       09 B3 2E                                            ;       .
181B:     04 1D                                                 ;     Data tag=04 size=001D
181D:         0B 1B                                             ;         Command_0B_SWITCH size=1B
181F:           0A 04                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
1821:           0B                                              ;           IF_NOT_JUMP address=182D
1822:             0E 09                                         ;             Command_0E_EXECUTE_LIST_WHILE_FAIL size=9
1824:               0D 05                                       ;               Command_0D_EXECUTE_LIST_WHILE_PASS size=5
1826:                 20 1D                                     ;                 Command_20_CHECK_ACTIVE_OBJECT object=1D(USER)
1828:                 01 07                                     ;                 Command_01_IS_OBJECT_IN_PACK_OR_ROOM object=07(StatueWest)
182A:                 82                                        ;                 CommonCommand_82
182B:               00 85                                       ;               Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=85
182D:           03                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
182E:           0B                                              ;           IF_NOT_JUMP address=183A
182F:             0E 09                                         ;             Command_0E_EXECUTE_LIST_WHILE_FAIL size=9
1831:               0D 05                                       ;               Command_0D_EXECUTE_LIST_WHILE_PASS size=5
1833:                 20 1D                                     ;                 Command_20_CHECK_ACTIVE_OBJECT object=1D(USER)
1835:                 01 06                                     ;                 Command_01_IS_OBJECT_IN_PACK_OR_ROOM object=06(StatueEast)
1837:                 82                                        ;                 CommonCommand_82
1838:               00 89                                       ;               Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=89
183A:   89 5D 00                                                ;   Script number=89 size=005D data=00
183D:     03 3F                                                 ;     Data tag=03 size=003F
183F:       C7 DE 94 14 43 5E 16 BC DB 72 47 B9                 ;       YOU ARE AT THE SOUTH END OF THE GREAT
184B:       53 BE 8E 61 B8 16 82 17 49 5E 63 B1                 ;       CENTRAL HALLWAY. EXITS EXIST IN THE EAST AND
1857:       05 BC 9E 61 CE B0 9B 15 11 8D 5F 4A                 ;       WEST WALLS.
1863:       3A 15 8D 7B 3A 15 66 7B D0 15 82 17                 ;       .
186F:       47 5E 66 49 90 14 19 58 66 62 F3 17                 ;       .
187B:       0D 8D 2E                                            ;       .
187E:     04 19                                                 ;     Data tag=04 size=0019
1880:         0B 17                                             ;         Command_0B_SWITCH size=17
1882:           0A 04                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
1884:           0C                                              ;           IF_NOT_JUMP address=1891
1885:             0D 0A                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=10
1887:               00 88                                       ;               Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=88
1889:               14                                          ;               Command_14_EXECUTE_COMMAND_REVERSE_STATUS
188A:                 0D 05                                     ;                 Command_0D_EXECUTE_LIST_WHILE_PASS size=5
188C:                   20 1D                                   ;                   Command_20_CHECK_ACTIVE_OBJECT object=1D(USER)
188E:                   01 06                                   ;                   Command_01_IS_OBJECT_IN_PACK_OR_ROOM object=06(StatueEast)
1890:                   82                                      ;                   CommonCommand_82
1891:           01                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=01 phrase="01: NORTH *     *          *       "
1892:           02                                              ;           IF_NOT_JUMP address=1895
1893:             00 90                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=90
1895:           03                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
1896:           02                                              ;           IF_NOT_JUMP address=1899
1897:             00 8A                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=8A
1899:   8A 3A 00                                                ;   Script number=8A size=003A data=00
189C:     03 26                                                 ;     Data tag=03 size=0026
189E:       63 BE CB B5 C3 B5 73 17 1B B8 E6 A4                 ;       THIS IS A T SHAPED ROOM WITH EXITS EAST,
18AA:       39 17 DB 9F 56 D1 07 71 96 D7 C7 B5                 ;       SOUTH, AND WEST.
18B6:       66 49 15 EE 36 A1 73 76 8E 48 F7 17                 ;       .
18C2:       17 BA                                               ;       .
18C4:     04 0F                                                 ;     Data tag=04 size=000F
18C6:         0B 0D                                             ;         Command_0B_SWITCH size=0D
18C8:           0A 04                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
18CA:           02                                              ;           IF_NOT_JUMP address=18CD
18CB:             00 89                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=89
18CD:           02                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=02 phrase="02: SOUTH *     *          *       "
18CE:           02                                              ;           IF_NOT_JUMP address=18D1
18CF:             00 8B                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=8B
18D1:           03                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
18D2:           02                                              ;           IF_NOT_JUMP address=18D5
18D3:             00 8D                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=8D
18D5:   8B 3F 00                                                ;   Script number=8B size=003F data=00
18D8:     03 2F                                                 ;     Data tag=03 size=002F
18DA:       C7 DE 94 14 4B 5E 83 96 39 17 DB 9F                 ;       YOU ARE IN A ROOM WITH GREY STONE WALLS.
18E6:       56 D1 09 71 7B B1 66 17 0F A0 F3 17                 ;       PASSAGES LEAD NORTH AND EAST.
18F2:       0D 8D 52 F4 65 49 77 47 CE B5 86 5F                 ;       .
18FE:       99 16 C2 B3 90 14 07 58 66 49 2E                    ;       .
1909:     04 0B                                                 ;     Data tag=04 size=000B
190B:         0B 09                                             ;         Command_0B_SWITCH size=09
190D:           0A 01                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=01 phrase="01: NORTH *     *          *       "
190F:           02                                              ;           IF_NOT_JUMP address=1912
1910:             00 8A                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=8A
1912:           03                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
1913:           02                                              ;           IF_NOT_JUMP address=1916
1914:             00 8C                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=8C
1916:   8C 44 00                                                ;   Script number=8C size=0044 data=00
1919:     03 2F                                                 ;     Data tag=03 size=002F
191B:       63 BE CB B5 C3 B5 39 17 8E C5 39 17                 ;       THIS IS A ROUND ROOM WITH HIGH WALLS. THE
1927:       DB 9F 56 D1 0A 71 7A 79 F3 17 0D 8D                 ;       ONLY OPENING IS TO THE WEST.
1933:       56 F4 DB 72 16 A0 51 DB F0 A4 91 7A                 ;       .
193F:       D5 15 89 17 82 17 59 5E 66 62 2E                    ;       .
194A:     04 10                                                 ;     Data tag=04 size=0010
194C:         0B 0E                                             ;         Command_0B_SWITCH size=0E
194E:           0A 05                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=05 phrase="05: GET *       ..C.....   *       "
1950:           07                                              ;           IF_NOT_JUMP address=1958
1951:             0D 05                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=5
1953:               08 08                                       ;               Command_08_COMPARE_OBJECT_TO_FIRST_NOUN object=08(GoldRing
1955:               19 87                                       ;               Command_19_MOVE_ACTIVE_OBJECT_TO_ROOM room=87
1957:               0C                                          ;               Command_0C_FAIL
1958:           04                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
1959:           02                                              ;           IF_NOT_JUMP address=195C
195A:             00 8B                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=8B
195C:   8D 4D 00                                                ;   Script number=8D size=004D data=00
195F:     03 3D                                                 ;     Data tag=03 size=003D
1961:       C7 DE 94 14 4B 5E 83 96 DF 16 96 BE                 ;       YOU ARE IN A PETITE CHAMBER. THERE IS A
196D:       45 5E 4F 72 74 4D 56 F4 F4 72 4B 5E                 ;       LARGER ROOM TO THE NORTH AND A PASSAGE TO
1979:       C3 B5 3B 16 B7 B1 94 AF 3F A0 89 17                 ;       THE WEST.
1985:       82 17 50 5E BE A0 03 71 33 98 52 45                 ;       .
1991:       65 49 77 47 89 17 82 17 59 5E 66 62                 ;       .
199D:       2E                                                  ;       .
199E:     04 0B                                                 ;     Data tag=04 size=000B
19A0:         0B 09                                             ;         Command_0B_SWITCH size=09
19A2:           0A 04                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
19A4:           02                                              ;           IF_NOT_JUMP address=19A7
19A5:             00 8A                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=8A
19A7:           01                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=01 phrase="01: NORTH *     *          *       "
19A8:           02                                              ;           IF_NOT_JUMP address=19AB
19A9:             00 8E                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=8E
19AB:   8E 80 A2 00                                             ;   Script number=8E size=00A2 data=00
19AF:     03 3B                                                 ;     Data tag=03 size=003B
19B1:       C7 DE 94 14 4B 5E 83 96 3B 16 B7 B1                 ;       YOU ARE IN A LARGE ROOM WHICH SMELLS OF
19BD:       39 17 DB 9F 23 D1 13 54 E7 B8 0D 8D                 ;       DECAYING FLESH. THERE ARE EXITS NORTH AND
19C9:       B8 16 FF 14 1B 53 91 7A 56 15 5A 62                 ;       SOUTH.
19D5:       56 F4 F4 72 43 5E 5B B1 23 63 0B C0                 ;       .
19E1:       04 9A 53 BE 8E 48 61 17 82 C6 2E                    ;       .
19EC:     04 62                                                 ;     Data tag=04 size=0062
19EE:         0B 60                                             ;         Command_0B_SWITCH size=60
19F0:           0A 02                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=02 phrase="02: SOUTH *     *          *       "
19F2:           02                                              ;           IF_NOT_JUMP address=19F5
19F3:             00 8D                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=8D
19F5:           01                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=01 phrase="01: NORTH *     *          *       "
19F6:           59                                              ;           IF_NOT_JUMP address=1A50
19F7:             0E 57                                         ;             Command_0E_EXECUTE_LIST_WHILE_FAIL size=87
19F9:               0D 1D                                       ;               Command_0D_EXECUTE_LIST_WHILE_PASS size=29
19FB:                 01 1E                                     ;                 Command_01_IS_OBJECT_IN_PACK_OR_ROOM object=1E(LiveGargoyle)
19FD:                 20 1D                                     ;                 Command_20_CHECK_ACTIVE_OBJECT object=1D(USER)
19FF:                 04                                        ;                 Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
1A00:                   17 5F BE 73 15 C1 B1 3F DE B6 14 5D     ;                   THE GARGOYLE BLOCKS THE WAY NORTH.
1A0C:                   9E D6 B5 DB 72 1B D0 99 16 C2 B3 2E     ;                   .
1A18:               0D 34                                       ;               Command_0D_EXECUTE_LIST_WHILE_PASS size=52
1A1A:                 20 1D                                     ;                 Command_20_CHECK_ACTIVE_OBJECT object=1D(USER)
1A1C:                 01 0A                                     ;                 Command_01_IS_OBJECT_IN_PACK_OR_ROOM object=0A(StoneGargoyle)
1A1E:                 17 0A 00                                  ;                 Command_17_MOVE_OBJECT_TO_LOCATION object=0A(StoneGargoyle) location=00
1A21:                 17 1E 8E                                  ;                 Command_17_MOVE_OBJECT_TO_LOCATION object=1E(LiveGargoyle) location=8E
1A24:                 04                                        ;                 Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
1A25:                   28 5F BE 73 15 C1 B1 3F DE E1 14 35     ;                   THE GARGOYLE COMES TO LIFE AND JUMPS DOWN TO
1A31:                   92 89 17 43 16 5B 66 8E 48 FF 15 ED     ;                   BLOCK YOUR WAY!
1A3D:                   93 09 15 03 D2 6B BF 89 4E 8B 54 C7     ;                   .
1A49:                   DE 99 AF 39 4A                          ;                   .
1A4E:               00 8F                                       ;               Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=8F
1A50:   8F 3A 00                                                ;   Script number=8F size=003A data=00
1A53:     03 2E                                                 ;     Data tag=03 size=002E
1A55:       63 BE CB B5 C3 B5 7B 17 F3 8C 01 B3                 ;       THIS IS A TALL ROOM CARVED OF STONE WITH A
1A61:       45 90 40 49 F3 5F C3 9E 09 BA 5B 98                 ;       SINGLE EXIT TO THE SOUTH. 
1A6D:       56 D1 03 71 5B 17 BE 98 47 5E 96 D7                 ;       .
1A79:       89 17 82 17 55 5E 36 A1 9B 76                       ;       .
1A83:     04 07                                                 ;     Data tag=04 size=0007
1A85:         0B 05                                             ;         Command_0B_SWITCH size=05
1A87:           0A 02                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=02 phrase="02: SOUTH *     *          *       "
1A89:           02                                              ;           IF_NOT_JUMP address=1A8C
1A8A:             00 8E                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=8E
1A8C:   90 80 A2 00                                             ;   Script number=90 size=00A2 data=00
1A90:     03 56                                                 ;     Data tag=03 size=0056
1A92:       C7 DE 94 14 43 5E 16 BC DB 72 04 9A                 ;       YOU ARE AT THE NORTH END OF THE GREAT
1A9E:       53 BE 8E 61 B8 16 82 17 49 5E 63 B1                 ;       CENTRAL HALLWAY. EXITS EXIST IN THE EAST AND
1AAA:       05 BC 9E 61 CE B0 9B 15 11 8D 5F 4A                 ;       WEST WALLS. THERE IS A DOOR ON THE NORTH
1AB6:       3A 15 8D 7B 3A 15 66 7B D0 15 82 17                 ;       WALL.
1AC2:       47 5E 66 49 90 14 19 58 66 62 F3 17                 ;       .
1ACE:       0D 8D 56 F4 F4 72 4B 5E C3 B5 09 15                 ;       .
1ADA:       A3 A0 03 A0 5F BE 99 16 C2 B3 F3 17                 ;       .
1AE6:       17 8D                                               ;       .
1AE8:     04 47                                                 ;     Data tag=04 size=0047
1AEA:         0B 45                                             ;         Command_0B_SWITCH size=45
1AEC:           0A 02                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=02 phrase="02: SOUTH *     *          *       "
1AEE:           02                                              ;           IF_NOT_JUMP address=1AF1
1AEF:             00 89                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=89
1AF1:           03                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
1AF2:           02                                              ;           IF_NOT_JUMP address=1AF5
1AF3:             00 A0                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=A0
1AF5:           01                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=01 phrase="01: NORTH *     *          *       "
1AF6:           36                                              ;           IF_NOT_JUMP address=1B2D
1AF7:             0E 34                                         ;             Command_0E_EXECUTE_LIST_WHILE_FAIL size=52
1AF9:               0D 14                                       ;               Command_0D_EXECUTE_LIST_WHILE_PASS size=20
1AFB:                 01 1B                                     ;                 Command_01_IS_OBJECT_IN_PACK_OR_ROOM object=1B(ClosedDoor)
1AFD:                 04                                        ;                 Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
1AFE:                   10 5F BE 09 15 A3 A0 89 4E A5 54 DB     ;                   THE DOOR BLOCKS PASSAGE.
1B0A:                   16 D3 B9 BF 6C                          ;                   .
1B0F:               0D 1C                                       ;               Command_0D_EXECUTE_LIST_WHILE_PASS size=28
1B11:                 00 91                                     ;                 Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=91
1B13:                 17 1B 91                                  ;                 Command_17_MOVE_OBJECT_TO_LOCATION object=1B(ClosedDoor) location=91
1B16:                 04                                        ;                 Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
1B17:                   12 5F BE 09 15 A3 A0 C9 54 B5 B7 AF     ;                   THE DOOR CLOSES BEHIND YOU.
1B23:                   14 90 73 1B 58 3F A1                    ;                   .
1B2A:                 17 1C 00                                  ;                 Command_17_MOVE_OBJECT_TO_LOCATION object=1C(OpenDoor) location=00
1B2D:           04                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
1B2E:           02                                              ;           IF_NOT_JUMP address=1B31
1B2F:             00 92                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=92
1B31:   91 80 8F 00                                             ;   Script number=91 size=008F data=00
1B35:     03 22                                                 ;     Data tag=03 size=0022
1B37:       C7 DE 94 14 4B 5E 83 96 CB 17 4E C5                 ;       YOU ARE IN A VAULT WITH A LARGE DOOR TO THE
1B43:       FB 17 53 BE 4E 45 31 49 46 5E 44 A0                 ;       SOUTH. 
1B4F:       89 17 82 17 55 5E 36 A1 9B 76                       ;       .
1B59:     04 68                                                 ;     Data tag=04 size=0068
1B5B:         0B 66                                             ;         Command_0B_SWITCH size=66
1B5D:           0A 02                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=02 phrase="02: SOUTH *     *          *       "
1B5F:           2F                                              ;           IF_NOT_JUMP address=1B8F
1B60:             0E 2D                                         ;             Command_0E_EXECUTE_LIST_WHILE_FAIL size=45
1B62:               0D 10                                       ;               Command_0D_EXECUTE_LIST_WHILE_PASS size=16
1B64:                 01 1B                                     ;                 Command_01_IS_OBJECT_IN_PACK_OR_ROOM object=1B(ClosedDoor)
1B66:                 04                                        ;                 Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
1B67:                   0C 5F BE 09 15 A3 A0 4B 7B 2F B8 9B     ;                   THE DOOR IS SHUT. 
1B73:                   C1                                      ;                   .
1B74:               0D 19                                       ;               Command_0D_EXECUTE_LIST_WHILE_PASS size=25
1B76:                 00 90                                     ;                 Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=90
1B78:                 17 1B 90                                  ;                 Command_17_MOVE_OBJECT_TO_LOCATION object=1B(ClosedDoor) location=90
1B7B:                 04                                        ;                 Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
1B7C:                   0F 5F BE 09 15 A3 A0 C9 54 B5 B7 89     ;                   THE DOOR CLOSES AGAIN.
1B88:                   14 D0 47 2E                             ;                   .
1B8C:                 17 1C 00                                  ;                 Command_17_MOVE_OBJECT_TO_LOCATION object=1C(OpenDoor) location=00
1B8F:           11                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=11 phrase="11: OPEN *      u.......   *       "
1B90:           32                                              ;           IF_NOT_JUMP address=1BC3
1B91:             0E 30                                         ;             Command_0E_EXECUTE_LIST_WHILE_FAIL size=48
1B93:               0D 10                                       ;               Command_0D_EXECUTE_LIST_WHILE_PASS size=16
1B95:                 08 1C                                     ;                 Command_08_COMPARE_OBJECT_TO_FIRST_NOUN object=1C(OpenDoor
1B97:                 04                                        ;                 Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
1B98:                   0C 8D 7B 8E 14 63 B1 FB 5C 5F A0 1B     ;                   ITS ALREADY OPEN. 
1BA4:                   9C                                      ;                   .
1BA5:               0D 1C                                       ;               Command_0D_EXECUTE_LIST_WHILE_PASS size=28
1BA7:                 08 1B                                     ;                 Command_08_COMPARE_OBJECT_TO_FIRST_NOUN object=1B(ClosedDoor
1BA9:                 17 1C 91                                  ;                 Command_17_MOVE_OBJECT_TO_LOCATION object=1C(OpenDoor) location=91
1BAC:                 17 1B 00                                  ;                 Command_17_MOVE_OBJECT_TO_LOCATION object=1B(ClosedDoor) location=00
1BAF:                 04                                        ;                 Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
1BB0:                   12 64 B7 B7 C6 B0 C6 D6 6A DB 72 81     ;                   SCRUUUUUNG THE DOOR OPENS. 
1BBC:                   5B 91 AF F0 A4 5B BB                    ;                   .
1BC3:   92 4B 00                                                ;   Script number=92 size=004B data=00
1BC6:     03 3B                                                 ;     Data tag=03 size=003B
1BC8:       C7 DE 94 14 43 5E 16 BC DB 72 9E 61                 ;       YOU ARE AT THE ENTRANCE TO A LONG DARK
1BD4:       D0 B0 9B 53 6B BF 4E 45 11 A0 FB 14                 ;       TUNNEL WHICH LEADS WEST. THERE IS A PASSAGE
1BE0:       4B B2 70 C0 6E 98 FA 17 DA 78 3F 16                 ;       EAST.
1BEC:       0D 47 F7 17 17 BA 82 17 2F 62 D5 15                 ;       .
1BF8:       7B 14 55 A4 09 B7 47 5E 66 49 2E                    ;       .
1C03:     04 0B                                                 ;     Data tag=04 size=000B
1C05:         0B 09                                             ;         Command_0B_SWITCH size=09
1C07:           0A 03                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
1C09:           02                                              ;           IF_NOT_JUMP address=1C0C
1C0A:             00 90                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=90
1C0C:           04                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
1C0D:           02                                              ;           IF_NOT_JUMP address=1C10
1C0E:             00 93                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=93
1C10:   93 22 00                                                ;   Script number=93 size=0022 data=00
1C13:     03 12                                                 ;     Data tag=03 size=0012
1C15:       C7 DE 94 14 4B 5E 96 96 DB 72 54 59                 ;       YOU ARE IN THE DARK TUNNEL.
1C21:       D6 83 98 C5 57 61                                   ;       .
1C27:     04 0B                                                 ;     Data tag=04 size=000B
1C29:         0B 09                                             ;         Command_0B_SWITCH size=09
1C2B:           0A 03                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
1C2D:           02                                              ;           IF_NOT_JUMP address=1C30
1C2E:             00 92                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=92
1C30:           04                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
1C31:           02                                              ;           IF_NOT_JUMP address=1C34
1C32:             00 94                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=94
1C34:   94 58 00                                                ;   Script number=94 size=0058 data=00
1C37:     03 3B                                                 ;     Data tag=03 size=003B
1C39:       C7 DE 94 14 43 5E 16 BC DB 72 9E 61                 ;       YOU ARE AT THE ENTRANCE TO A LONG DARK
1C45:       D0 B0 9B 53 6B BF 4E 45 11 A0 FB 14                 ;       TUNNEL WHICH LEADS EAST. THERE IS A PASSAGE
1C51:       4B B2 70 C0 6E 98 FA 17 DA 78 3F 16                 ;       WEST.
1C5D:       0D 47 23 15 17 BA 82 17 2F 62 D5 15                 ;       .
1C69:       7B 14 55 A4 09 B7 59 5E 66 62 2E                    ;       .
1C74:     04 18                                                 ;     Data tag=04 size=0018
1C76:         0B 16                                             ;         Command_0B_SWITCH size=16
1C78:           0A 03                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
1C7A:           02                                              ;           IF_NOT_JUMP address=1C7D
1C7B:             00 93                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=93
1C7D:           04                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
1C7E:           0F                                              ;           IF_NOT_JUMP address=1C8E
1C7F:             0E 0D                                         ;             Command_0E_EXECUTE_LIST_WHILE_FAIL size=13
1C81:               0D 09                                       ;               Command_0D_EXECUTE_LIST_WHILE_PASS size=9
1C83:                 20 1D                                     ;                 Command_20_CHECK_ACTIVE_OBJECT object=1D(USER)
1C85:                 03 00 16                                  ;                 Command_03_IS_OBJECT_AT_LOCATION object=16(DeadSerpent) location=00
1C88:                 17 15 95                                  ;                 Command_17_MOVE_OBJECT_TO_LOCATION object=15(LiveSerpent) location=95
1C8B:                 0C                                        ;                 Command_0C_FAIL
1C8C:               00 95                                       ;               Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=95
1C8E:   95 32 00                                                ;   Script number=95 size=0032 data=00
1C91:     03 20                                                 ;     Data tag=03 size=0020
1C93:       C7 DE 94 14 4B 5E 83 96 3B 16 B7 B1                 ;       YOU ARE IN A LARGE ROOM WITH A SINGLE EXIT
1C9F:       39 17 DB 9F 56 D1 03 71 5B 17 BE 98                 ;       EAST.
1CAB:       47 5E 96 D7 23 15 17 BA                             ;       .
1CB3:     04 0D                                                 ;     Data tag=04 size=000D
1CB5:         0B 0B                                             ;         Command_0B_SWITCH size=0B
1CB7:           0A 36                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=36 phrase="36: CLIMB IN    *          *       "
1CB9:           01                                              ;           IF_NOT_JUMP address=1CBB
1CBA:             8F                                            ;             CommonCommand_8F
1CBB:           17                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=17 phrase="17: CLIMB *     u.......   *       "
1CBC:           01                                              ;           IF_NOT_JUMP address=1CBE
1CBD:             8F                                            ;             CommonCommand_8F
1CBE:           03                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
1CBF:           02                                              ;           IF_NOT_JUMP address=1CC2
1CC0:             00 94                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=94
1CC2:   96 30 00                                                ;   Script number=96 size=0030 data=00
1CC5:     03 18                                                 ;     Data tag=03 size=0018
1CC7:       C7 DE 94 14 4B 5E 83 96 FF 14 97 9A                 ;       YOU ARE IN A DENSE DARK DAMP JUNGLE.
1CD3:       FB 14 4B B2 4F 59 0C A3 91 C5 FF 8B                 ;       .
1CDF:     04 13                                                 ;     Data tag=04 size=0013
1CE1:         0B 11                                             ;         Command_0B_SWITCH size=11
1CE3:           0A 01                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=01 phrase="01: NORTH *     *          *       "
1CE5:           02                                              ;           IF_NOT_JUMP address=1CE8
1CE6:             00 A3                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=A3
1CE8:           02                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=02 phrase="02: SOUTH *     *          *       "
1CE9:           02                                              ;           IF_NOT_JUMP address=1CEC
1CEA:             00 A4                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=A4
1CEC:           04                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
1CED:           02                                              ;           IF_NOT_JUMP address=1CF0
1CEE:             00 97                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=97
1CF0:           03                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
1CF1:           02                                              ;           IF_NOT_JUMP address=1CF4
1CF2:             00 A4                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=A4
1CF4:   97 30 00                                                ;   Script number=97 size=0030 data=00
1CF7:     03 18                                                 ;     Data tag=03 size=0018
1CF9:       C7 DE 94 14 4B 5E 83 96 FB 14 4B B2                 ;       YOU ARE IN A DARK DENSE DAMP JUNGLE.
1D05:       F0 59 9B B7 4F 59 0C A3 91 C5 FF 8B                 ;       .
1D11:     04 13                                                 ;     Data tag=04 size=0013
1D13:         0B 11                                             ;         Command_0B_SWITCH size=11
1D15:           0A 01                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=01 phrase="01: NORTH *     *          *       "
1D17:           02                                              ;           IF_NOT_JUMP address=1D1A
1D18:             00 A2                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=A2
1D1A:           02                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=02 phrase="02: SOUTH *     *          *       "
1D1B:           02                                              ;           IF_NOT_JUMP address=1D1E
1D1C:             00 96                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=96
1D1E:           03                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
1D1F:           02                                              ;           IF_NOT_JUMP address=1D22
1D20:             00 A3                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=A3
1D22:           04                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
1D23:           02                                              ;           IF_NOT_JUMP address=1D26
1D24:             00 98                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=98
1D26:   98 40 00                                                ;   Script number=98 size=0040 data=00
1D29:     03 28                                                 ;     Data tag=03 size=0028
1D2B:       6C BE 29 A1 16 71 DB 72 F0 81 BF 6D                 ;       THROUGH THE JUNGLE YOU SEE THE EAST WALL OF
1D37:       51 18 55 C2 1B 60 5F BE 23 15 F3 B9                 ;       A GREAT TEMPLE. 
1D43:       0E D0 11 8A 83 64 84 15 96 5F 7F 17                 ;       .
1D4F:       E6 93 DB 63                                         ;       .
1D53:     04 13                                                 ;     Data tag=04 size=0013
1D55:         0B 11                                             ;         Command_0B_SWITCH size=11
1D57:           0A 01                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=01 phrase="01: NORTH *     *          *       "
1D59:           02                                              ;           IF_NOT_JUMP address=1D5C
1D5A:             00 9B                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=9B
1D5C:           02                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=02 phrase="02: SOUTH *     *          *       "
1D5D:           02                                              ;           IF_NOT_JUMP address=1D60
1D5E:             00 99                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=99
1D60:           03                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
1D61:           02                                              ;           IF_NOT_JUMP address=1D64
1D62:             00 97                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=97
1D64:           04                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
1D65:           02                                              ;           IF_NOT_JUMP address=1D68
1D66:             00 9E                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=9E
1D68:   99 44 00                                                ;   Script number=99 size=0044 data=00
1D6B:     03 2C                                                 ;     Data tag=03 size=002C
1D6D:       83 7A 45 45 E3 8B 10 B2 C4 6A 59 60                 ;       IN A CLEARING BEFORE YOU STANDS THE SOUTH
1D79:       5B B1 C7 DE 66 17 8E 48 D6 B5 DB 72                 ;       WALL OF A GREAT TEMPLE. 
1D85:       47 B9 53 BE 0E D0 11 8A 83 64 84 15                 ;       .
1D91:       96 5F 7F 17 E6 93 DB 63                             ;       .
1D99:     04 13                                                 ;     Data tag=04 size=0013
1D9B:         0B 11                                             ;         Command_0B_SWITCH size=11
1D9D:           0A 01                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=01 phrase="01: NORTH *     *          *       "
1D9F:           02                                              ;           IF_NOT_JUMP address=1DA2
1DA0:             00 9F                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=9F
1DA2:           02                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=02 phrase="02: SOUTH *     *          *       "
1DA3:           02                                              ;           IF_NOT_JUMP address=1DA6
1DA4:             00 96                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=96
1DA6:           03                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
1DA7:           02                                              ;           IF_NOT_JUMP address=1DAA
1DA8:             00 98                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=98
1DAA:           04                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
1DAB:           02                                              ;           IF_NOT_JUMP address=1DAE
1DAC:             00 9A                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=9A
1DAE:   9A 59 00                                                ;   Script number=9A size=0059 data=00
1DB1:     03 41                                                 ;     Data tag=03 size=0041
1DB3:       6C BE 29 A1 16 71 DB 72 F0 59 9B B7                 ;       THROUGH THE DENSE UNDERGROWTH, YOU CAN SEE
1DBF:       8E C5 31 62 09 B3 76 BE 51 18 45 C2                 ;       THE GREAT BRONZE GATES ON THE WEST WALL OF
1DCB:       83 48 A7 B7 82 17 49 5E 63 B1 04 BC                 ;       THE TEMPLE.
1DD7:       00 B3 5B E3 16 6C 4B 62 03 A0 5F BE                 ;       .
1DE3:       F7 17 F3 B9 0E D0 11 8A 96 64 DB 72                 ;       .
1DEF:       EF BD FF A5 2E                                      ;       .
1DF4:     04 13                                                 ;     Data tag=04 size=0013
1DF6:         0B 11                                             ;         Command_0B_SWITCH size=11
1DF8:           0A 01                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=01 phrase="01: NORTH *     *          *       "
1DFA:           02                                              ;           IF_NOT_JUMP address=1DFD
1DFB:             00 9B                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=9B
1DFD:           02                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=02 phrase="02: SOUTH *     *          *       "
1DFE:           02                                              ;           IF_NOT_JUMP address=1E01
1DFF:             00 99                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=99
1E01:           03                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
1E02:           02                                              ;           IF_NOT_JUMP address=1E05
1E03:             00 9C                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=9C
1E05:           04                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
1E06:           02                                              ;           IF_NOT_JUMP address=1E09
1E07:             00 A4                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=A4
1E09:   9B 4D 00                                                ;   Script number=9B size=004D data=00
1E0C:     03 35                                                 ;     Data tag=03 size=0035
1E0E:       6C BE 29 A1 03 71 73 15 0B A3 96 96                 ;       THROUGH A GAP IN THE JUNGLE YOU CAN SEE THE
1E1A:       DB 72 F0 81 BF 6D 51 18 45 C2 83 48                 ;       NORTH WALL OF A MAGNIFICENT TEMPLE.
1E26:       A7 B7 82 17 50 5E BE A0 19 71 46 48                 ;       .
1E32:       B8 16 7B 14 89 91 08 99 D7 78 B3 9A                 ;       .
1E3E:       EF BD FF A5 2E                                      ;       .
1E43:     04 13                                                 ;     Data tag=04 size=0013
1E45:         0B 11                                             ;         Command_0B_SWITCH size=11
1E47:           0A 01                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=01 phrase="01: NORTH *     *          *       "
1E49:           02                                              ;           IF_NOT_JUMP address=1E4C
1E4A:             00 A2                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=A2
1E4C:           02                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=02 phrase="02: SOUTH *     *          *       "
1E4D:           02                                              ;           IF_NOT_JUMP address=1E50
1E4E:             00 9D                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=9D
1E50:           04                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
1E51:           02                                              ;           IF_NOT_JUMP address=1E54
1E52:             00 9A                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=9A
1E54:           03                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
1E55:           02                                              ;           IF_NOT_JUMP address=1E58
1E56:             00 98                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=98
1E58:   9C 3A 00                                                ;   Script number=9C size=003A data=00
1E5B:     03 26                                                 ;     Data tag=03 size=0026
1E5D:       C7 DE 94 14 55 5E 50 BD 90 5A C4 6A                 ;       YOU ARE STANDING BEFORE THE WEST ENTRANCE OF
1E69:       59 60 5B B1 5F BE F7 17 F3 B9 9E 61                 ;       THE TEMPLE. 
1E75:       D0 B0 9B 53 C3 9E 5F BE 7F 17 E6 93                 ;       .
1E81:       DB 63                                               ;       .
1E83:     04 0F                                                 ;     Data tag=04 size=000F
1E85:         0B 0D                                             ;         Command_0B_SWITCH size=0D
1E87:           0A 01                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=01 phrase="01: NORTH *     *          *       "
1E89:           02                                              ;           IF_NOT_JUMP address=1E8C
1E8A:             00 9D                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=9D
1E8C:           02                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=02 phrase="02: SOUTH *     *          *       "
1E8D:           02                                              ;           IF_NOT_JUMP address=1E90
1E8E:             00 9F                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=9F
1E90:           04                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
1E91:           02                                              ;           IF_NOT_JUMP address=1E94
1E92:             00 9A                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=9A
1E94:   9D 80 B3 00                                             ;   Script number=9D size=00B3 data=00
1E98:     03 12                                                 ;     Data tag=03 size=0012
1E9A:       C7 DE 94 14 43 5E 16 BC DB 72 04 9A                 ;       YOU ARE AT THE NORTH WALL. 
1EA6:       53 BE 0E D0 9B 8F                                   ;       .
1EAC:     04 80 9B                                              ;     Data tag=04 size=009B
1EAF:         0B 80 98                                          ;         Command_0B_SWITCH size=98
1EB2:           0A 01                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=01 phrase="01: NORTH *     *          *       "
1EB4:           02                                              ;           IF_NOT_JUMP address=1EB7
1EB5:             00 9B                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=9B
1EB7:           03                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
1EB8:           02                                              ;           IF_NOT_JUMP address=1EBB
1EB9:             00 9E                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=9E
1EBB:           17                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=17 phrase="17: CLIMB *     u.......   *       "
1EBC:           80 88                                           ;           IF_NOT_JUMP address=1F46
1EBE:             0D 80 85                                      ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=133
1EC1:               08 21                                       ;               Command_08_COMPARE_OBJECT_TO_FIRST_NOUN object=21(Vines
1EC3:               0E 80 80                                    ;               Command_0E_EXECUTE_LIST_WHILE_FAIL size=128
1EC6:                 0D 54                                     ;                 Command_0D_EXECUTE_LIST_WHILE_PASS size=84
1EC8:                   05 7F                                   ;                   Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=7F
1ECA:                   04                                      ;                   Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
1ECB:                     2A C7 DE DE 14 64 7A 89 17 82 17 54   ;                     YOU CLIMB TO THE ROOF.  AS YOU STEP ON THE
1ED7:                     5E 38 A0 3B F4 4B 49 C7 DE 66 17 D3   ;                     ROOF, IT COLLAPSES. 
1EE3:                     61 03 A0 5F BE 39 17 E6 9E D6 15 E1   ;                     .
1EEF:                     14 FB 8C 17 A7 5B BB                  ;                     .
1EF6:                   17 36 00                                ;                   Command_17_MOVE_OBJECT_TO_LOCATION object=36(Jungle) location=00
1EF9:                   17 29 FF                                ;                   Command_17_MOVE_OBJECT_TO_LOCATION object=29(Floor) location=FF
1EFC:                   17 2A FF                                ;                   Command_17_MOVE_OBJECT_TO_LOCATION object=2A(Exit) location=FF
1EFF:                   17 2B FF                                ;                   Command_17_MOVE_OBJECT_TO_LOCATION object=2B(Passage) location=FF
1F02:                   17 2C FF                                ;                   Command_17_MOVE_OBJECT_TO_LOCATION object=2C(Hole) location=FF
1F05:                   17 2D FF                                ;                   Command_17_MOVE_OBJECT_TO_LOCATION object=2D(Corridor) location=FF
1F08:                   17 2E FF                                ;                   Command_17_MOVE_OBJECT_TO_LOCATION object=2E(Corner) location=FF
1F0B:                   17 31 FF                                ;                   Command_17_MOVE_OBJECT_TO_LOCATION object=31(Hallway) location=FF
1F0E:                   17 34 FF                                ;                   Command_17_MOVE_OBJECT_TO_LOCATION object=34(Entrance) location=FF
1F11:                   17 35 FF                                ;                   Command_17_MOVE_OBJECT_TO_LOCATION object=35(Tunnel) location=FF
1F14:                   17 3A FF                                ;                   Command_17_MOVE_OBJECT_TO_LOCATION object=3A(Ceiling) location=FF
1F17:                   17 3C 00                                ;                   Command_17_MOVE_OBJECT_TO_LOCATION object=3C(Object3C) location=00
1F1A:                   00 81                                   ;                   Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=81
1F1C:                 04                                        ;                 Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
1F1D:                   28 4B 49 C7 DE DE 14 64 7A 16 EE DB     ;                   AS YOU CLIMB, THE VINE GIVES WAY AND YOU
1F29:                   72 10 CB 49 5E CF 7B D9 B5 3B 4A 8E     ;                   FALL TO THE GROUND.
1F35:                   48 51 18 48 C2 46 48 89 17 82 17 49     ;                   .
1F41:                   5E 07 B3 57 98                          ;                   .
1F46:           04                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
1F47:           02                                              ;           IF_NOT_JUMP address=1F4A
1F48:             00 9C                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=9C
1F4A:   9E 25 00                                                ;   Script number=9E size=0025 data=00
1F4D:     03 11                                                 ;     Data tag=03 size=0011
1F4F:       C7 DE 94 14 43 5E 16 BC DB 72 95 5F                 ;       YOU ARE AT THE EAST WALL.
1F5B:       19 BC 46 48 2E                                      ;       .
1F60:     04 0F                                                 ;     Data tag=04 size=000F
1F62:         0B 0D                                             ;         Command_0B_SWITCH size=0D
1F64:           0A 01                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=01 phrase="01: NORTH *     *          *       "
1F66:           02                                              ;           IF_NOT_JUMP address=1F69
1F67:             00 9D                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=9D
1F69:           02                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=02 phrase="02: SOUTH *     *          *       "
1F6A:           02                                              ;           IF_NOT_JUMP address=1F6D
1F6B:             00 9F                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=9F
1F6D:           03                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
1F6E:           02                                              ;           IF_NOT_JUMP address=1F71
1F6F:             00 98                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=98
1F71:   9F 26 00                                                ;   Script number=9F size=0026 data=00
1F74:     03 12                                                 ;     Data tag=03 size=0012
1F76:       C7 DE 94 14 43 5E 16 BC DB 72 47 B9                 ;       YOU ARE AT THE SOUTH WALL. 
1F82:       53 BE 0E D0 9B 8F                                   ;       .
1F88:     04 0F                                                 ;     Data tag=04 size=000F
1F8A:         0B 0D                                             ;         Command_0B_SWITCH size=0D
1F8C:           0A 04                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
1F8E:           02                                              ;           IF_NOT_JUMP address=1F91
1F8F:             00 9C                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=9C
1F91:           03                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
1F92:           02                                              ;           IF_NOT_JUMP address=1F95
1F93:             00 9E                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=9E
1F95:           02                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=02 phrase="02: SOUTH *     *          *       "
1F96:           02                                              ;           IF_NOT_JUMP address=1F99
1F97:             00 99                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=99
1F99:   A0 20 00                                                ;   Script number=A0 size=0020 data=00
1F9C:     03 14                                                 ;     Data tag=03 size=0014
1F9E:       C7 DE 94 14 4B 5E 83 96 CF 17 7B B4                 ;       YOU ARE IN A VERY SMALL ROOM. 
1FAA:       E3 B8 F3 8C 01 B3 DB 95                             ;       .
1FB2:     04 07                                                 ;     Data tag=04 size=0007
1FB4:         0B 05                                             ;         Command_0B_SWITCH size=05
1FB6:           0A 04                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
1FB8:           02                                              ;           IF_NOT_JUMP address=1FBB
1FB9:             00 90                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=90
1FBB:   A1 2C 00                                                ;   Script number=A1 size=002C data=00
1FBE:     03 20                                                 ;     Data tag=03 size=0020
1FC0:       C7 DE 94 14 4B 5E 83 96 5F 17 46 48                 ;       YOU ARE IN A SMALL ROOM WITH A SINGLE EXIT
1FCC:       39 17 DB 9F 56 D1 03 71 5B 17 BE 98                 ;       EAST.
1FD8:       47 5E 96 D7 23 15 17 BA                             ;       .
1FE0:     04 07                                                 ;     Data tag=04 size=0007
1FE2:         0B 05                                             ;         Command_0B_SWITCH size=05
1FE4:           0A 03                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
1FE6:           02                                              ;           IF_NOT_JUMP address=1FE9
1FE7:             00 84                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=84
1FE9:   A2 30 00                                                ;   Script number=A2 size=0030 data=00
1FEC:     03 18                                                 ;     Data tag=03 size=0018
1FEE:       C7 DE 94 14 4B 5E 83 96 FB 14 4B B2                 ;       YOU ARE IN A DARK DAMP DENSE JUNGLE.
1FFA:       4F 59 06 A3 9D 61 4C 5E 91 C5 FF 8B                 ;       .
2006:     04 13                                                 ;     Data tag=04 size=0013
2008:         0B 11                                             ;         Command_0B_SWITCH size=11
200A:           0A 03                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
200C:           02                                              ;           IF_NOT_JUMP address=200F
200D:             00 A4                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=A4
200F:           01                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=01 phrase="01: NORTH *     *          *       "
2010:           02                                              ;           IF_NOT_JUMP address=2013
2011:             00 96                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=96
2013:           02                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=02 phrase="02: SOUTH *     *          *       "
2014:           02                                              ;           IF_NOT_JUMP address=2017
2015:             00 A3                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=A3
2017:           04                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
2018:           02                                              ;           IF_NOT_JUMP address=201B
2019:             00 97                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=97
201B:   A3 30 00                                                ;   Script number=A3 size=0030 data=00
201E:     03 18                                                 ;     Data tag=03 size=0018
2020:       C7 DE 94 14 4B 5E 83 96 FF 14 97 9A                 ;       YOU ARE IN A DENSE DAMP DARK JUNGLE.
202C:       FB 14 D3 93 54 59 CC 83 91 C5 FF 8B                 ;       .
2038:     04 13                                                 ;     Data tag=04 size=0013
203A:         0B 11                                             ;         Command_0B_SWITCH size=11
203C:           0A 03                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
203E:           02                                              ;           IF_NOT_JUMP address=2041
203F:             00 A4                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=A4
2041:           01                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=01 phrase="01: NORTH *     *          *       "
2042:           02                                              ;           IF_NOT_JUMP address=2045
2043:             00 A2                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=A2
2045:           02                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=02 phrase="02: SOUTH *     *          *       "
2046:           02                                              ;           IF_NOT_JUMP address=2049
2047:             00 96                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=96
2049:           04                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
204A:           02                                              ;           IF_NOT_JUMP address=204D
204B:             00 97                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=97
204D:   A4 30 00                                                ;   Script number=A4 size=0030 data=00
2050:     03 18                                                 ;     Data tag=03 size=0018
2052:       C7 DE 94 14 4B 5E 83 96 FB 14 D3 93                 ;       YOU ARE IN A DAMP DARK DENSE JUNGLE.
205E:       54 59 C6 83 9D 61 4C 5E 91 C5 FF 8B                 ;       .
206A:     04 13                                                 ;     Data tag=04 size=0013
206C:         0B 11                                             ;         Command_0B_SWITCH size=11
206E:           0A 03                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
2070:           02                                              ;           IF_NOT_JUMP address=2073
2071:             00 A3                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=A3
2073:           01                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=01 phrase="01: NORTH *     *          *       "
2074:           02                                              ;           IF_NOT_JUMP address=2077
2075:             00 A2                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=A2
2077:           02                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=02 phrase="02: SOUTH *     *          *       "
2078:           02                                              ;           IF_NOT_JUMP address=207B
2079:             00 96                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=96
207B:           04                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
207C:           02                                              ;           IF_NOT_JUMP address=207F
207D:             00 A3                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=A3
207F:   A5 2C 00                                                ;   Script number=A5 size=002C data=00
2082:     03 20                                                 ;     Data tag=03 size=0020
2084:       C7 DE 94 14 4B 5E 96 96 DB 72 A5 B7                 ;       YOU ARE IN THE SECRET PASSAGE WHICH LEADS
2090:       76 B1 DB 16 D3 B9 9B 6C 23 D1 13 54                 ;       EAST. 
209C:       E3 8B 0B 5C 95 5F 9B C1                             ;       .
20A4:     04 07                                                 ;     Data tag=04 size=0007
20A6:         0B 05                                             ;         Command_0B_SWITCH size=05
20A8:           0A 03                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
20AA:           02                                              ;           IF_NOT_JUMP address=20AD
20AB:             00 A6                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=A6
20AD:   A6 50 00                                                ;   Script number=A6 size=0050 data=00
20B0:     03 2C                                                 ;     Data tag=03 size=002C
20B2:       C7 DE 94 14 43 5E 16 BC DB 72 8E 61                 ;       YOU ARE AT THE END OF THE PASSAGE. THERE IS
20BE:       B8 16 82 17 52 5E 65 49 77 47 56 F4                 ;       A HOLE IN THE CEILING.
20CA:       F4 72 4B 5E C3 B5 A9 15 DB 8B 83 7A                 ;       .
20D6:       5F BE D7 14 43 7A CF 98                             ;       .
20DE:     04 1F                                                 ;     Data tag=04 size=001F
20E0:         0B 1D                                             ;         Command_0B_SWITCH size=1D
20E2:           0A 04                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
20E4:           02                                              ;           IF_NOT_JUMP address=20E7
20E5:             00 A5                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=A5
20E7:           17                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=17 phrase="17: CLIMB *     u.......   *       "
20E8:           05                                              ;           IF_NOT_JUMP address=20EE
20E9:             0D 03                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=3
20EB:               08 2C                                       ;               Command_08_COMPARE_OBJECT_TO_FIRST_NOUN object=2C(Hole
20ED:               91                                          ;               CommonCommand_91
20EE:           36                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=36 phrase="36: CLIMB IN    *          *       "
20EF:           05                                              ;           IF_NOT_JUMP address=20F5
20F0:             0D 03                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=3
20F2:               08 2C                                       ;               Command_08_COMPARE_OBJECT_TO_FIRST_NOUN object=2C(Hole
20F4:               91                                          ;               CommonCommand_91
20F5:           37                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=37 phrase="37: CLIMB OUT   *          *       "
20F6:           05                                              ;           IF_NOT_JUMP address=20FC
20F7:             0D 03                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=3
20F9:               08 2C                                       ;               Command_08_COMPARE_OBJECT_TO_FIRST_NOUN object=2C(Hole
20FB:               91                                          ;               CommonCommand_91
20FC:           33                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=33 phrase="??"
20FD:           01                                              ;           IF_NOT_JUMP address=20FF
20FE:             91                                            ;             CommonCommand_91
; ENDOF 1523
```

## Object Data

```code
ObjectData: 
; Objects are referenced by index in this list with the first object being "Object 1".
; The first three data bytes are as follows AA BB CC:
;   AA = location: 00 is nowhere, 01..7F object is held by this object, 80-FE room number, 
;        FF is "everywhere" (the USER object starts at location FF but changes at initialization)
;   BB = score points
;   CC = parameter bits uvCPAXOL
;    u=1 if object is in game play (guard-watcher, for instance, is 0)
;    v=1 if object is a true weapon (only sword has this set)
;    C=1 if object can be carried
;    P=1 if object is a person;
;    A=1 if open/close-able
;    X=1 if lock/unlock-able 
;    O=1 if closed
;    L=1 if locked
;
; Objects can have various fields tagged as follows:
;   01 = list of adjectives (size+bytes) not used in RAAKATU
;   02 = short name (packed string)
;   03 = long description (packed string)
;   04 (never used)
;   05 (never used)
;   06 = command handling if object is second noun (script)
;   07 = command handling if object is first noun (script)
;   08 = turn-script executed for objects turn in game (script)
;   09 = hitpoint information (2 bytess) AA BB. AA=max hit points  BB=current hit points
;   0A = script executed with killed (script) 
;   0B = script executed if command is given to object (script) not used in RAAKATU
;
20FF: 00 91 3A                                                  ; Number=00 size=113A
; Object_01 Object1
2102:   01 03                                                   ;   Number=01 size=0003
2104:     00 00 00                                              ;     room=00 scorePoints=00 bits=00 *       
; Object_02 Object2
2107:   03 03                                                   ;   Number=03 size=0003
2109:     00 00 00                                              ;     room=00 scorePoints=00 bits=00 *       
; Object_03 Rug
210C:   06 48                                                   ;   Number=06 size=0048
210E:     82 00 80                                              ;     room=82 scorePoints=00 bits=80 u.......
2111:     02                                                    ;     02 SHORT NAME
2112:       02 E9 B3                                            ;       RUG
2115:     07 3F                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
2117:       0B 3D                                               ;       Command_0B_SWITCH size=3D
2119:         0A 0C                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=0C phrase="0C: LOOK UNDER  *          u......."
211B:         01                                                ;         IF_NOT_JUMP address=211D
211C:           8C                                              ;           CommonCommand_8C
211D:         36                                                ;         Command_0A_COMPARE_TO_PHRASE_FORM val=36 phrase="36: CLIMB IN    *          *       "
211E:         01                                                ;         IF_NOT_JUMP address=2120
211F:           8A                                              ;           CommonCommand_8A
2120:         33                                                ;         Command_0A_COMPARE_TO_PHRASE_FORM val=33 phrase="??"
2121:         01                                                ;         IF_NOT_JUMP address=2123
2122:           8A                                              ;           CommonCommand_8A
2123:         34                                                ;         Command_0A_COMPARE_TO_PHRASE_FORM val=34 phrase="34: JUMP OVER   *          u......."
2124:         01                                                ;         IF_NOT_JUMP address=2126
2125:           8A                                              ;           CommonCommand_8A
2126:         35                                                ;         Command_0A_COMPARE_TO_PHRASE_FORM val=35 phrase="??"
2127:         01                                                ;         IF_NOT_JUMP address=2129
2128:           8B                                              ;           CommonCommand_8B
2129:         2D                                                ;         Command_0A_COMPARE_TO_PHRASE_FORM val=2D phrase="2D: PULL UP     *          u......."
212A:         01                                                ;         IF_NOT_JUMP address=212C
212B:           8C                                              ;           CommonCommand_8C
212C:         26                                                ;         Command_0A_COMPARE_TO_PHRASE_FORM val=26 phrase="26: GO AROUND   *          u......."
212D:         28                                                ;         IF_NOT_JUMP address=2156
212E:           04                                              ;           Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
212F:             26 C7 DE D3 14 E6 96 16 EE DB 72 E9           ;             YOU CAN'T, THE RUG STRETCHES ALL THE WAY
213B:             B3 66 17 76 B1 1F 54 C3 B5 F3 8C 5F           ;             ACROSS THE ROOM.
2147:             BE F3 17 43 DB B9 55 CB B9 5F BE 39           ;             .
2153:             17 FF 9F                                      ;             .
; Object_04 DoorCarvings
2156:   09 5E                                                   ;   Number=09 size=005E
2158:     82 00 84                                              ;     room=82 scorePoints=00 bits=84 u....X..
215B:     02                                                    ;     02 SHORT NAME
215C:       03 81 5B 52                                         ;       DOOR
2160:     07 54                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
2162:       0E 52                                               ;       Command_0E_EXECUTE_LIST_WHILE_FAIL size=82
2164:         0D 22                                             ;         Command_0D_EXECUTE_LIST_WHILE_PASS size=34
2166:           0A 08                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=08 phrase="08: READ *      .....X..   *       "
2168:           04                                              ;           Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2169:             1E 5F BE D3 14 13 B4 C5 98 C0 16 82           ;             THE CARVINGS ON THE DOOR SAY, "DO NOT
2175:             17 46 5E 44 A0 53 17 B3 E0 49 1B 99           ;             ENTER."
2181:             16 07 BC BF 9A 1C B5                          ;             .
2188:         0D 2C                                             ;         Command_0D_EXECUTE_LIST_WHILE_PASS size=44
218A:           14                                              ;           Command_14_EXECUTE_COMMAND_REVERSE_STATUS
218B:             0A 0B                                         ;             Command_0A_COMPARE_TO_PHRASE_FORM val=0B phrase="0B: LOOK AT     *          u......."
218D:           04                                              ;           Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
218E:             27 C7 DE C6 22 9B 15 5B CA 6B BF 2B           ;             YOU'LL HAVE TO GO TO THE EAST SIDE OF THE
219A:             6E 6B BF 5F BE 23 15 F3 B9 46 B8 51           ;             ROOM TO DO THAT.
21A6:             5E 96 64 DB 72 01 B3 56 90 C6 9C D6           ;             .
21B2:             9C 56 72 2E                                   ;             .
; Object_05 Food
21B6:   0C 2A                                                   ;   Number=0C size=002A
21B8:     84 00 A0                                              ;     room=84 scorePoints=00 bits=A0 u.C.....
21BB:     03                                                    ;     03 DESCRIPTION
21BC:       0D 5F BE 5B B1 4B 7B 01 68 0A 58 2F                 ;       THERE IS FOOD HERE.
21C8:       62 2E                                               ;       .
21CA:     07 11                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
21CC:       0D 0F                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=15
21CE:         0A 15                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=15 phrase="15: EAT *       u.......   *       "
21D0:         04                                                ;         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
21D1:           04 F4 4F AB A2                                  ;           BURP! 
21D6:         17 05 00                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=05(Food) location=00
21D9:         1C 1D                                             ;         Command_1C_SET_VAR_OBJECT object=1D (USER)
21DB:         23 0F                                             ;         Command_23_HEAL_VAR_OBJECT value=0F
21DD:     02                                                    ;     02 SHORT NAME
21DE:       03 01 68 44                                         ;       FOOD
; Object_06 StatueEast
21E2:   0D 2A                                                   ;   Number=0D size=002A
21E4:     88 00 80                                              ;     room=88 scorePoints=00 bits=80 u.......
21E7:     02                                                    ;     02 SHORT NAME
21E8:       04 FB B9 67 C0                                      ;       STATUE
21ED:     07 05                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
21EF:       0D 03                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=3
21F1:         0A 12                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=12 phrase="12: PULL *      u.......   *       "
21F3:         8D                                                ;         CommonCommand_8D
21F4:     03                                                    ;     03 DESCRIPTION
21F5:       18 5F BE 66 17 8F 49 4B 5E C8 B5 DB                 ;       THE STATUE IS FACING THE EAST DOOR. 
2201:       46 AB 98 5F BE 23 15 F3 B9 81 5B 1B                 ;       .
220D:       B5                                                  ;       .
; Object_07 StatueWest
220E:   0D 2A                                                   ;   Number=0D size=002A
2210:     00 00 80                                              ;     room=00 scorePoints=00 bits=80 u.......
2213:     02                                                    ;     02 SHORT NAME
2214:       04 FB B9 67 C0                                      ;       STATUE
2219:     07 05                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
221B:       0D 03                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=3
221D:         0A 12                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=12 phrase="12: PULL *      u.......   *       "
221F:         8D                                                ;         CommonCommand_8D
2220:     03                                                    ;     03 DESCRIPTION
2221:       18 5F BE 66 17 8F 49 4B 5E C8 B5 DB                 ;       THE STATUE IS FACING THE WEST DOOR. 
222D:       46 AB 98 5F BE F7 17 F3 B9 81 5B 1B                 ;       .
2239:       B5                                                  ;       .
; Object_08 GoldRing
223A:   12 44                                                   ;   Number=12 size=0044
223C:     8C 05 A4                                              ;     room=8C scorePoints=05 bits=A4 u.C..X..
223F:     03                                                    ;     03 DESCRIPTION
2240:       14 54 45 91 7A B8 16 53 15 75 98 09                 ;       A RING OF FINEST GOLD IS HERE.
224C:       BC BE 9F D5 15 9F 15 7F B1                          ;       .
2255:     02                                                    ;     02 SHORT NAME
2256:       06 3E 6E 14 58 91 7A                                ;       GOLD RING
225D:     07 21                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
225F:       0D 1F                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=31
2261:         0A 08                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=08 phrase="08: READ *      .....X..   *       "
2263:         04                                                ;         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2264:           1B 5F BE D0 15 64 B7 EE 7A C0 7A 2F             ;           THE INSCRIPTION READS, "RING OF MOTION."
2270:           17 0D 47 FC ED 10 B2 D1 6A 8F 64 03             ;           .
227C:           A1 27 A0 22                                     ;           .
; Object_09 Sword
2280:   0E 42                                                   ;   Number=0E size=0042
2282:     A1 00 E4                                              ;     room=A1 scorePoints=00 bits=E4 uvC..X..
2285:     03                                                    ;     03 DESCRIPTION
2286:       19 5F BE 5B B1 4B 7B 4E 45 31 49 55                 ;       THERE IS A LARGE SWORD LAYING NEARBY.
2292:       5E 44 D2 0E 58 4B 4A AB 98 63 98 03                 ;       .
229E:       B1 2E                                               ;       .
22A0:     07 18                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
22A2:       0D 16                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=22
22A4:         0A 08                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=08 phrase="08: READ *      .....X..   *       "
22A6:         04                                                ;         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
22A7:           12 2C 1D 5F A0 D3 B3 B8 16 43 16 57             ;           "PROPERTY OF LIEYUCHNEBST" 
22B3:           63 28 54 BD 5F 23 BC                            ;           .
22BA:     02                                                    ;     02 SHORT NAME
22BB:       08 54 8B 9B 6C 81 BA 33 B1                          ;       LARGE SWORD 
; Object_0A StoneGargoyle
22C4:   0F 6B                                                   ;   Number=0F size=006B
22C6:     8E 00 80                                              ;     room=8E scorePoints=00 bits=80 u.......
22C9:     03                                                    ;     03 DESCRIPTION
22CA:       34 5F BE 5B B1 4B 7B 4A 45 FF 78 35                 ;       THERE IS A HIDEOUS STONE GARGOYLE PERCHED ON
22D6:       A1 66 17 0F A0 73 15 C1 B1 3F DE DF                 ;       A LEDGE ABOVE THE NORTH PASSAGE. 
22E2:       16 1A B1 F3 5F 03 A0 4E 45 01 60 43                 ;       .
22EE:       5E 08 4F 56 5E DB 72 04 9A 53 BE 55                 ;       .
22FA:       A4 09 B7 DB 63                                      ;       .
22FF:     07 24                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
2301:       0D 22                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=34
2303:         0A 0B                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=0B phrase="0B: LOOK AT     *          u......."
2305:         04                                                ;         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2306:           1E 5F BE 5B B1 EA 48 94 5F D6 B5 C4             ;           THERE APPEARS TO BE DRIED BLOOD ON HIS
2312:           9C 46 5E 07 B2 04 58 81 8D 11 58 8A             ;           CLAWS!
231E:           96 4B 7B BB 54 C9 D2                            ;           .
2325:     02                                                    ;     02 SHORT NAME
2326:       0A 09 BA 5B 98 14 6C 4B 6E DB 8B                    ;       STONE GARGOYLE 
; Object_0B AlterA
2331:   22 58                                                   ;   Number=22 size=0058
2333:     95 00 80                                              ;     room=95 scorePoints=00 bits=80 u.......
2336:     03                                                    ;     03 DESCRIPTION
2337:       32 68 4D AF A0 51 18 55 C2 50 BD 0B                 ;       BEFORE YOU STANDS AN ALTAR, STAINED WITH THE
2343:       5C 83 48 4E 48 46 49 66 17 D0 47 F3                 ;       BLOOD OF COUNTLESS SACRIFICES.
234F:       5F 56 D1 16 71 DB 72 89 4E 73 9E C3                 ;       .
235B:       9E 47 55 C6 9A 65 62 53 17 B3 55 05                 ;       .
2367:       67 6F 62                                            ;       .
236A:     07 10                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
236C:       0B 0E                                               ;       Command_0B_SWITCH size=0E
236E:         0A 12                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=12 phrase="12: PULL *      u.......   *       "
2370:         01                                                ;         IF_NOT_JUMP address=2372
2371:           8E                                              ;           CommonCommand_8E
2372:         0C                                                ;         Command_0A_COMPARE_TO_PHRASE_FORM val=0C phrase="0C: LOOK UNDER  *          u......."
2373:         01                                                ;         IF_NOT_JUMP address=2375
2374:           8E                                              ;           CommonCommand_8E
2375:         38                                                ;         Command_0A_COMPARE_TO_PHRASE_FORM val=38 phrase="38: CLIMB UNDER *          u......."
2376:         05                                                ;         IF_NOT_JUMP address=237C
2377:           0D 03                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=3
2379:             00 A5                                         ;             Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=A5
237B:             90                                            ;             CommonCommand_90
237C:     02                                                    ;     02 SHORT NAME
237D:       0D 89 4E 73 9E FB B9 8F 7A 03 58 3B                 ;       BLOOD STAINED ALTAR
2389:       8E 52                                               ;       .
; Object_0C Idol
238B:   23 2F                                                   ;   Number=23 size=002F
238D:     95 05 A0                                              ;     room=95 scorePoints=05 bits=A0 u.C.....
2390:     03                                                    ;     03 DESCRIPTION
2391:       20 49 45 BE 9F 83 61 09 79 15 8A 50                 ;       A GOLDEN IDOL STANDS IN THE CENTER OF THE
239D:       BD 0B 5C 83 7A 5F BE D7 14 BF 9A 91                 ;       ROOM. 
23A9:       AF 96 64 DB 72 01 B3 DB 95                          ;       .
23B2:     02                                                    ;     02 SHORT NAME
23B3:       08 3E 6E F0 59 C6 15 B3 9F                          ;       GOLDEN IDOL 
; Object_0D BronzeGates
23BC:   27 80 9A                                                ;   Number=27 size=009A
23BF:     9C 00 80                                              ;     room=9C scorePoints=00 bits=80 u.......
23C2:     03                                                    ;     03 DESCRIPTION
23C3:       34 AF 6E 73 49 79 4F AF 9B 73 15 F5                 ;       GREAT BRONZE GATES ENGRAVED WITH IMAGES OF
23CF:       BD 30 15 AB 6E 66 CA FB 17 53 BE 63                 ;       SERPENTS STAND SILENTLY BEFORE YOU.
23DB:       7A B5 6C B8 16 57 17 1F B3 CD 9A 66                 ;       .
23E7:       17 8E 48 5B 17 F0 8B 13 BF AF 14 04                 ;       .
23F3:       68 5B 5E 3F A1                                      ;       .
23F8:     07 55                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
23FA:       0B 53                                               ;       Command_0B_SWITCH size=53
23FC:         0A 11                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=11 phrase="11: OPEN *      u.......   *       "
23FE:         20                                                ;         IF_NOT_JUMP address=241F
23FF:           04                                              ;           Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2400:             1E 5F BE 73 15 F5 BD 94 14 4E 5E 5D           ;             THE GATES ARE LOCKED, YOU CAN NOT OPEN THEM.
240C:             9E 16 60 51 18 45 C2 83 48 06 9A C2           ;             
2418:             16 83 61 5F BE DB 95                          ;             .
241F:         36                                                ;         Command_0A_COMPARE_TO_PHRASE_FORM val=36 phrase="36: CLIMB IN    *          *       "
2420:         10                                                ;         IF_NOT_JUMP address=2431
2421:           04                                              ;           Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2422:             0E 5F BE 73 15 F5 BD 94 14 45 5E 85           ;             THE GATES ARE CLOSED.
242E:             8D 17 60                                      ;             .
2431:         17                                                ;         Command_0A_COMPARE_TO_PHRASE_FORM val=17 phrase="17: CLIMB *     u.......   *       "
2432:         19                                                ;         IF_NOT_JUMP address=244C
2433:           04                                              ;           Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2434:             17 5F BE 73 15 F5 BD 94 14 56 5E 2B           ;             THE GATES ARE TOO SMOOTH TO CLIMB.
2440:             A0 F1 B8 02 A1 89 17 DE 14 64 7A 2E           ;             .
244C:         34                                                ;         Command_0A_COMPARE_TO_PHRASE_FORM val=34 phrase="34: JUMP OVER   *          u......."
244D:         01                                                ;         IF_NOT_JUMP address=244F
244E:           89                                              ;           CommonCommand_89
244F:     02                                                    ;     02 SHORT NAME
2450:       08 79 4F AF 9B 73 15 F5 BD                          ;       BRONZE GATES
; Object_0E UnpulledLever
2459:   16 59                                                   ;   Number=16 size=0059
245B:     91 00 A0                                              ;     room=91 scorePoints=00 bits=A0 u.C.....
245E:     02                                                    ;     02 SHORT NAME
245F:       04 F8 8B 23 62                                      ;       LEVER 
2464:     03                                                    ;     03 DESCRIPTION
2465:       16 44 45 EF 60 AE D0 F3 5F F8 8B 23                 ;       A BEJEWELED LEVER IS ON ONE WALL.
2471:       62 4B 7B 03 A0 0F A0 F3 17 17 8D                    ;       .
247C:     07 36                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
247E:       0D 34                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=52
2480:         0A 12                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=12 phrase="12: PULL *      u.......   *       "
2482:         04                                                ;         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2483:           2F 56 45 D2 B0 09 15 A3 A0 5F A0 8B             ;           A TRAP DOOR OPENS ABOVE YOU.  GOLD DUST
248F:           9A B9 46 5B CA C7 DE 3B F4 3E 6E 06             ;           FILLS THE ROOM AND DROWNS YOU.
249B:           58 66 C6 53 15 0D 8D 82 17 54 5E 3F             ;           .
24A7:           A0 90 14 06 58 09 B3 8B 9A C7 DE 2E             ;           .
24B3:         81                                                ;         CommonCommand_81
; Object_0F PulledLever
24B4:   16 42                                                   ;   Number=16 size=0042
24B6:     00 05 A0                                              ;     room=00 scorePoints=05 bits=A0 u.C.....
24B9:     03                                                    ;     03 DESCRIPTION
24BA:       12 44 45 EF 60 AE D0 F3 5F F8 8B 23                 ;       A BEJEWELED LEVER IS HERE. 
24C6:       62 4B 7B F4 72 DB 63                                ;       .
24CD:     02                                                    ;     02 SHORT NAME
24CE:       0A 6C 4D F7 62 E6 8B 3F 16 74 CA                    ;       BEJEWELED LEVER
24D9:     07 1D                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
24DB:       0D 1B                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=27
24DD:         0A 12                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=12 phrase="12: PULL *      u.......   *       "
24DF:         04                                                ;         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
24E0:           17 5F BE 3F 16 74 CA D3 14 90 96 CE             ;           THE LEVER CAN NO LONGER BE PULLED.
24EC:           9C 11 A0 23 62 5B 4D 6E A7 E6 8B 2E             ;           .
; Object_10 LeverPlaque
24F8:   18 80 C5                                                ;   Number=18 size=00C5
24FB:     91 00 84                                              ;     room=91 scorePoints=00 bits=84 u....X..
24FE:     07 80 98                                              ;     07 COMMAND HANDLING IF FIRST NOUN
2501:       0D 80 95                                            ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=149
2504:         0A 08                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=08 phrase="08: READ *      .....X..   *       "
2506:         04                                                ;         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2507:           80 90 9E C5 BE 9F 33 17 1F 54 CE B5             ;           UNTOLD RICHES LIE WITHIN REACH, HERE- TO ANY
2513:           1B 79 56 D1 90 73 2F 17 DA 46 0A EE             ;           KNOWING, LIVING CREATURE. BE WARY THOUGH, NO
251F:           2F 62 D6 E7 C3 9C 7B 9B 19 87 50 D1             ;           MATTER WHAT THY CREED, THAT THOU HARNESS AND
252B:           33 70 98 8C 91 7A E4 14 96 5F 2F C6             ;           LIMIT THY POWERFUL GREED.  PULL THE LEVER TO
2537:           44 F4 59 5E 43 49 82 17 29 A1 73 76             ;           GAIN THY WEALTH, BE PREPARED TO ... 
2543:           EB 99 96 91 F4 BD FA 17 73 49 73 BE             ;           .
254F:           E4 14 26 60 16 EE 56 72 82 17 1B A1             ;           .
255B:           54 72 75 98 C3 B5 33 98 8F 8C 73 7B             ;           .
2567:           73 BE E9 16 B4 D0 EE 68 84 15 26 60             ;           .
2573:           3B F4 6E A7 16 8A DB 72 F8 8B 23 62             ;           .
257F:           6B BF 0B 6C 96 96 FB 75 A3 D0 42 8E             ;           .
258B:           04 EE 52 5E 72 B1 2F 49 16 58 DF 9C             ;           .
2597:           DB F9                                           ;           .
2599:     03                                                    ;     03 DESCRIPTION
259A:       1F 5F BE 5B B1 4B 7B 52 45 53 8B 1B                 ;       THERE IS A PLAQUE ON THE WALL ABOVE THE
25A6:       C4 03 A0 5F BE F3 17 F3 8C B9 46 5B                 ;       LEVER.
25B2:       CA 5F BE 3F 16 74 CA 2E                             ;       .
25BA:     02                                                    ;     02 SHORT NAME
25BB:       04 FB A5 A7 AD                                      ;       PLAQUE
; Object_11 UnlitCandle
25C0:   19 6F                                                   ;   Number=19 size=006F
25C2:     92 00 A8                                              ;     room=92 scorePoints=00 bits=A8 u.C.A...
25C5:     03                                                    ;     03 DESCRIPTION
25C6:       10 45 45 8E 48 DB 8B 4B 7B 83 7A 5F                 ;       A CANDLE IS IN THE ROOM.
25D2:       BE 39 17 FF 9F                                      ;       .
25D7:     02                                                    ;     02 SHORT NAME
25D8:       04 10 53 FF 5A                                      ;       CANDLE
25DD:     07 52                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
25DF:       0B 50                                               ;       Command_0B_SWITCH size=50
25E1:         0A 14                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=14 phrase="14: LIGHT WITH  u...A...   u...A..."
25E3:         34                                                ;         IF_NOT_JUMP address=2618
25E4:           0E 32                                           ;           Command_0E_EXECUTE_LIST_WHILE_FAIL size=50
25E6:             0D 2F                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=47
25E8:               09 14                                       ;               Command_09_COMPARE_OBJECT_TO_SECOND_NOUN object=14(LitLamp
25EA:               1E 11 12                                    ;               Command_1E_SWAP_OBJECTS objectA=11(UnlitCandle) objectB=12(LitCandle)
25ED:               04                                          ;               Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
25EE:                 28 5F BE D3 14 46 98 4B 5E D0 B5 6B       ;                 THE CANDLE IS NOW BURNING, A SWEET SCENT
25FA:                 A1 F4 4F 10 99 33 70 55 45 A7 D0 15       ;                 PERMEATES THE ROOM.
2606:                 BC B0 53 12 BC 37 62 96 5F 4B 62 5F       ;                 .
2612:                 BE 39 17 FF 9F                            ;                 .
2617:             88                                            ;             CommonCommand_88
2618:         15                                                ;         Command_0A_COMPARE_TO_PHRASE_FORM val=15 phrase="15: EAT *       u.......   *       "
2619:         17                                                ;         IF_NOT_JUMP address=2631
261A:           0D 15                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=21
261C:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
261D:               12 55 BD F5 BD F3 17 1E DA D6 15 D2         ;               TASTES WAXY, ITS POISONOUS!
2629:               B5 55 9F 19 A0 49 C6                        ;               .
2630:             81                                            ;             CommonCommand_81
; Object_12 LitCandle
2631:   19 80 C6                                                ;   Number=19 size=00C6
2634:     00 00 A8                                              ;     room=00 scorePoints=00 bits=A8 u.C.A...
2637:     03                                                    ;     03 DESCRIPTION
2638:       12 45 45 8E 48 DB 8B 4B 7B F4 4F 10                 ;       A CANDLE IS BURNING DIMLY. 
2644:       99 C6 6A 6E 7A DB E0                                ;       .
264B:     02                                                    ;     02 SHORT NAME
264C:       0A F4 4F 10 99 C5 6A 8E 48 DB 8B                    ;       BURNING CANDLE 
2657:     07 59                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
2659:       0E 57                                               ;       Command_0E_EXECUTE_LIST_WHILE_FAIL size=87
265B:         0D 1C                                             ;         Command_0D_EXECUTE_LIST_WHILE_PASS size=28
265D:           0E 04                                           ;           Command_0E_EXECUTE_LIST_WHILE_FAIL size=4
265F:             0A 13                                         ;             Command_0A_COMPARE_TO_PHRASE_FORM val=13 phrase="??"
2661:             0A 14                                         ;             Command_0A_COMPARE_TO_PHRASE_FORM val=14 phrase="14: LIGHT WITH  u...A...   u...A..."
2663:           04                                              ;           Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2664:             14 5F BE D3 14 46 98 4B 5E C3 B5 EF           ;             THE CANDLE IS ALREADY BURNING.
2670:             8D 13 47 BF 14 D3 B2 CF 98                    ;             .
2679:         0D 19                                             ;         Command_0D_EXECUTE_LIST_WHILE_PASS size=25
267B:           0A 16                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=16 phrase="16: DROP OUT    *          u...A..."
267D:           1E 11 12                                        ;           Command_1E_SWAP_OBJECTS objectA=11(UnlitCandle) objectB=12(LitCandle)
2680:           04                                              ;           Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2681:             12 5F BE D3 14 46 98 4B 5E C7 B5 43           ;             THE CANDLE IS EXTINGUISHED.
268D:             D9 C7 98 5A 7B 17 60                          ;             .
2694:         0D 1C                                             ;         Command_0D_EXECUTE_LIST_WHILE_PASS size=28
2696:           0A 15                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=15 phrase="15: EAT *       u.......   *       "
2698:           04                                              ;           Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2699:             18 C7 DE 2F 17 46 48 55 DB 87 74 B3           ;             YOU REALLY SHOULD PUT IT OUT FIRST. 
26A5:             8B 76 A7 D6 15 C7 16 08 BC 3D 7B 9B           ;             .
26B1:             C1                                            ;             .
26B2:     08 46                                                 ;     08 TURN SCRIPT
26B4:       0D 44                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=68
26B6:         1F                                                ;         Command_1F_PRINT_MESSAGE
26B7:           24 5F BE 43 16 2E 6D 5C 15 DB 9F 5F             ;           THE LIGHT FROM THE CANDLE SEEMS TO BE
26C3:           BE D3 14 46 98 55 5E 2F 60 D6 B5 C4             ;           GROWING DIMMER. 
26CF:           9C 49 5E 09 B3 91 7A 03 15 67 93 1B             ;           .
26DB:           B5                                              ;           .
26DC:         0B 1C                                             ;         Command_0B_SWITCH size=1C
26DE:           01 1D                                           ;           Command_01_IS_OBJECT_IN_PACK_OR_ROOM object=1D(USER)
26E0:           07                                              ;           IF_NOT_JUMP address=26E8
26E1:             0D 05                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=5
26E3:               1C 1D                                       ;               Command_1C_SET_VAR_OBJECT object=1D (USER)
26E5:               1D 14                                       ;               Command_1D_ATTACK_OBJECT damage=14
26E7:               0C                                          ;               Command_0C_FAIL
26E8:           1E                                              ;           Command_01_IS_OBJECT_IN_PACK_OR_ROOM object=1E(LiveGargoyle)
26E9:           07                                              ;           IF_NOT_JUMP address=26F1
26EA:             0D 05                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=5
26EC:               1C 1E                                       ;               Command_1C_SET_VAR_OBJECT object=1E (LiveGargoyle)
26EE:               1D 32                                       ;               Command_1D_ATTACK_OBJECT damage=32
26F0:               0C                                          ;               Command_0C_FAIL
26F1:           15                                              ;           Command_01_IS_OBJECT_IN_PACK_OR_ROOM object=15(LiveSerpent)
26F2:           07                                              ;           IF_NOT_JUMP address=26FA
26F3:             0D 05                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=5
26F5:               1C 15                                       ;               Command_1C_SET_VAR_OBJECT object=15 (LiveSerpent)
26F7:               1D 0F                                       ;               Command_1D_ATTACK_OBJECT damage=0F
26F9:               0C                                          ;               Command_0C_FAIL
; Object_13 CrypticRunes
26FA:   18 80 84                                                ;   Number=18 size=0084
26FD:     92 00 84                                              ;     room=92 scorePoints=00 bits=84 u....X..
2700:     07 5B                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
2702:       0D 59                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=89
2704:         0A 08                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=08 phrase="08: READ *      .....X..   *       "
2706:         04                                                ;         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2707:           55 9E 7A D6 9C DB 72 70 C0 6E 98 30             ;           INTO THE TUNNEL ENTERS THE SEEKER, BRAVELY
2713:           15 F4 BD D6 B5 DB 72 A7 B7 B4 85 04             ;           AND WISELY HE GOES. FOR HE WILL RECOGNIZE
271F:           EE D8 B0 53 61 90 14 19 58 57 7B FB             ;           THE REAPER, AS THE LIGHT BEFORE HIM GLOWS.
272B:           8E DB 72 37 6E 5B BB 04 68 9F 15 FB             ;           .
2737:           17 F3 8C 65 B1 00 9F 6F 7C 82 17 54             ;           .
2743:           5E 92 5F 46 62 95 14 82 17 4E 5E 7A             ;           .
274F:           79 04 BC 59 60 5B B1 8F 73 7E 15 85             ;           .
275B:           A1 2E                                           ;           .
275D:     03                                                    ;     03 DESCRIPTION
275E:       1C 5F BE 5B B1 2F 49 E4 14 EE DE CB                 ;       THERE ARE CRYPTIC RUNES ABOVE THE TUNNEL. 
276A:       78 F0 B3 4B 62 B9 46 5B CA 5F BE 8F                 ;       .
2776:       17 CF 99 9B 8F                                      ;       .
277B:     02                                                    ;     02 SHORT NAME
277C:       04 F0 B3 4B 62                                      ;       RUNES 
; Object_14 LitLamp
2781:   1B 80 B5                                                ;   Number=1B size=00B5
2784:     A0 00 AC                                              ;     room=A0 scorePoints=00 bits=AC u.C.AX..
2787:     03                                                    ;     03 DESCRIPTION
2788:       14 5F BE 5B B1 4B 7B 44 45 38 C6 91                 ;       THERE IS A BURNING LAMP HERE. 
2794:       7A 3B 16 D3 93 F4 72 DB 63                          ;       .
279D:     07 80 8F                                              ;     07 COMMAND HANDLING IF FIRST NOUN
27A0:       0E 80 8C                                            ;       Command_0E_EXECUTE_LIST_WHILE_FAIL size=140
27A3:         0D 1B                                             ;         Command_0D_EXECUTE_LIST_WHILE_PASS size=27
27A5:           0E 04                                           ;           Command_0E_EXECUTE_LIST_WHILE_FAIL size=4
27A7:             0A 13                                         ;             Command_0A_COMPARE_TO_PHRASE_FORM val=13 phrase="??"
27A9:             0A 14                                         ;             Command_0A_COMPARE_TO_PHRASE_FORM val=14 phrase="14: LIGHT WITH  u...A...   u...A..."
27AB:           04                                              ;           Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
27AC:             13 5F BE 3B 16 D3 93 4B 7B 4C 48 86           ;             THE LAMP IS ALREADY BURNING.
27B8:             5F 44 DB 38 C6 91 7A 2E                       ;             .
27C0:         0B 6D                                             ;         Command_0B_SWITCH size=6D
27C2:           0A 16                                           ;           Command_0A_COMPARE_TO_PHRASE_FORM val=16 phrase="16: DROP OUT    *          u...A..."
27C4:           12                                              ;           IF_NOT_JUMP address=27D7
27C5:             0D 10                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=16
27C7:               1E 28 14                                    ;               Command_1E_SWAP_OBJECTS objectA=28(UnlitLamp) objectB=14(LitLamp)
27CA:               04                                          ;               Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
27CB:                 0B 5F BE 3B 16 D3 93 4B 7B 36 A1 2E       ;                 THE LAMP IS OUT.
27D7:           18                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=18 phrase="18: RUB *       u.......   *       "
27D8:           2D                                              ;           IF_NOT_JUMP address=2806
27D9:             0D 2B                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=43
27DB:               04                                          ;               Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
27DC:                 26 5F BE 3B 16 D3 93 37 6E D1 B5 97       ;                 THE LAMP GOES OUT. YOU MUST HAVE RUBBED IT
27E8:                 C6 51 18 4F C2 66 C6 9B 15 5B CA E4       ;                 THE WRONG WAY!
27F4:                 B3 66 4D D6 15 82 17 59 5E 00 B3 D9       ;                 .
2800:                 6A 39 4A                                  ;                 .
2803:               1E 28 14                                    ;               Command_1E_SWAP_OBJECTS objectA=28(UnlitLamp) objectB=14(LitLamp)
2806:           08                                              ;           Command_0A_COMPARE_TO_PHRASE_FORM val=08 phrase="08: READ *      .....X..   *       "
2807:           27                                              ;           IF_NOT_JUMP address=282F
2808:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2809:               25 5F BE 3B 16 D3 93 4B 7B 48 55 2F         ;               THE LAMP IS COVERED WITH TARNISH AND YOU
2815:               62 19 58 82 7B 7B 17 D3 B2 13 B8 8E         ;               CAN'T READ IT.
2821:               48 51 18 45 C2 85 48 14 BC 86 5F D6         ;               .
282D:               15 2E                                       ;               .
282F:     02                                                    ;     02 SHORT NAME
2830:       08 F4 4F 10 99 CE 6A 72 48                          ;       BURNING LAMP
; Object_15 LiveSerpent
2839:   24 81 C0                                                ;   Number=24 size=01C0
283C:     00 00 90                                              ;     room=00 scorePoints=00 bits=90 u..P....
283F:     03                                                    ;     03 DESCRIPTION
2840:       1C 4E 45 31 49 55 5E 3A 62 9E 61 43                 ;       A LARGE SERPENT LIES COILED ON THE FLOOR. 
284C:       16 4B 62 3B 55 E6 8B C0 16 82 17 48                 ;       .
2858:       5E 81 8D 1B B5                                      ;       .
285D:     09 02 3C 3C                                           ;     09 HIT POINTS maxHitPoints=3C currentHitPoints=3C
2861:     07 80 B3                                              ;     07 COMMAND HANDLING IF FIRST NOUN
2864:       0B 80 B0                                            ;       Command_0B_SWITCH size=B0
2867:         0A 09                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=09 phrase="09: ATTACK WITH ...P....   .v......"
2869:         80 9A                                             ;         IF_NOT_JUMP address=2905
286B:           0D 80 97                                        ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=151
286E:             1A                                            ;             Command_1A_SET_VAR_OBJECT_TO_FIRST_NOUN
286F:             09 09                                         ;             Command_09_COMPARE_OBJECT_TO_SECOND_NOUN object=09(Sword
2871:             0B 80 91                                      ;             Command_0B_SWITCH size=91
2874:               05 99                                       ;               Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=99
2876:               2B                                          ;               IF_NOT_JUMP address=28A2
2877:                 0D 29                                     ;                 Command_0D_EXECUTE_LIST_WHILE_PASS size=41
2879:                   04                                      ;                   Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
287A:                     03 C7 DE 52                           ;                     YOUR
287E:                   12                                      ;                   Command_12_PRINT_SECOND_NOUN_SHORT_NAME
287F:                   04                                      ;                   Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2880:                     1F 50 B8 CB 87 6B BF 5F BE A3 15 33   ;                     SINKS TO THE HILT IN THE SERPENT'S SCALY
288C:                     8E 83 7A 5F BE 57 17 1F B3 B5 9A D5   ;                     BODY!
2898:                     B5 0E 53 44 DB 93 9E 21               ;                     .
28A0:                   1D 11                                   ;                   Command_1D_ATTACK_OBJECT damage=11
28A2:               CC                                          ;               Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=CC
28A3:               2E                                          ;               IF_NOT_JUMP address=28D2
28A4:                 0D 2C                                     ;                 Command_0D_EXECUTE_LIST_WHILE_PASS size=44
28A6:                   04                                      ;                   Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
28A7:                     03 C7 DE 52                           ;                     YOUR
28AB:                   12                                      ;                   Command_12_PRINT_SECOND_NOUN_SHORT_NAME
28AC:                   04                                      ;                   Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
28AD:                     24 6C BE 85 A1 7B 14 29 B8 B4 D0 B8   ;                     THROWS A SHOWER OF SPARKS AS IT GLANCES OFF
28B9:                     16 62 17 35 49 C3 B5 CB B5 09 BC 50   ;                     THE WALL! 
28C5:                     8B B5 53 B8 16 96 64 DB 72 0E D0 AB   ;                     .
28D1:                     89                                    ;                     .
28D2:               FF                                          ;               Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=FF
28D3:               31                                          ;               IF_NOT_JUMP address=2905
28D4:                 0D 2F                                     ;                 Command_0D_EXECUTE_LIST_WHILE_PASS size=47
28D6:                   04                                      ;                   Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
28D7:                     2B 5F BE 57 17 1F B3 B5 9A CA B5 86   ;                     THE SERPENT'S HEAD IS SEVERED FROM HIS BODY!
28E3:                     5F D5 15 57 17 74 CA F3 5F 79 68 4A   ;                     A MAGNIFICENT BLOW!
28EF:                     90 4B 7B F6 4E EB DA 4F 45 80 47 53   ;                     .
28FB:                     79 B0 53 04 BC 89 8D 21               ;                     .
2903:                   1D FF                                   ;                   Command_1D_ATTACK_OBJECT damage=FF
2905:         15                                                ;         Command_0A_COMPARE_TO_PHRASE_FORM val=15 phrase="15: EAT *       u.......   *       "
2906:         10                                                ;         IF_NOT_JUMP address=2917
2907:           04                                              ;           Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2908:             0E 76 4D F4 BD 1B 16 F3 8C 73 7B 14           ;             BETTER KILL IT FIRST!
2914:             67 F1 B9                                      ;             .
2917:     08 80 C4                                              ;     08 TURN SCRIPT
291A:       0D 80 C1                                            ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=193
291D:         0E 3E                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=62
291F:           0D 32                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=50
2921:             14                                            ;             Command_14_EXECUTE_COMMAND_REVERSE_STATUS
2922:               01 1D                                       ;               Command_01_IS_OBJECT_IN_PACK_OR_ROOM object=1D(USER)
2924:             0B 19                                         ;             Command_0B_SWITCH size=19
2926:               0A 04                                       ;               Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
2928:               04                                          ;               IF_NOT_JUMP address=292D
2929:                 21 04 00 00                               ;                 Command_21_EXECUTE_PHRASE phrase="04: WEST *      *          *       " first=00(NONE)  second=00(NONE)
292D:               03                                          ;               Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
292E:               04                                          ;               IF_NOT_JUMP address=2933
292F:                 21 03 00 00                               ;                 Command_21_EXECUTE_PHRASE phrase="03: EAST *      *          *       " first=00(NONE)  second=00(NONE)
2933:               01                                          ;               Command_0A_COMPARE_TO_PHRASE_FORM val=01 phrase="01: NORTH *     *          *       "
2934:               04                                          ;               IF_NOT_JUMP address=2939
2935:                 21 01 00 00                               ;                 Command_21_EXECUTE_PHRASE phrase="01: NORTH *     *          *       " first=00(NONE)  second=00(NONE)
2939:               02                                          ;               Command_0A_COMPARE_TO_PHRASE_FORM val=02 phrase="02: SOUTH *     *          *       "
293A:               04                                          ;               IF_NOT_JUMP address=293F
293B:                 21 02 00 00                               ;                 Command_21_EXECUTE_PHRASE phrase="02: SOUTH *     *          *       " first=00(NONE)  second=00(NONE)
293F:             1F                                            ;             Command_1F_PRINT_MESSAGE
2940:               12 5F BE 57 17 1F B3 B3 9A 74 A7 27         ;               THE SERPENT PURSUES YOU AND
294C:               BA DB B5 1B A1 8E 48                        ;               .
2953:           1F                                              ;           Command_1F_PRINT_MESSAGE
2954:             08 5F BE 57 17 1F B3 B3 9A                    ;             THE SERPENT 
295D:         0D 7F                                             ;         Command_0D_EXECUTE_LIST_WHILE_PASS size=127
295F:           01 1D                                           ;           Command_01_IS_OBJECT_IN_PACK_OR_ROOM object=1D(USER)
2961:           1C 1D                                           ;           Command_1C_SET_VAR_OBJECT object=1D (USER)
2963:           0B 79                                           ;           Command_0B_SWITCH size=79
2965:             05 33                                         ;             Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=33
2967:             23                                            ;             IF_NOT_JUMP address=298B
2968:               0D 21                                       ;               Command_0D_EXECUTE_LIST_WHILE_PASS size=33
296A:                 1F                                        ;                 Command_1F_PRINT_MESSAGE
296B:                   1D 0C BA 17 7A 33 BB 7B A6 40 B9 E1     ;                   STRIKES, POISON COURSES THROUGH YOUR VEINS!
2977:                   14 3D C6 4B 62 6C BE 29 A1 1B 71 34     ;                   .
2983:                   A1 CF 17 9D 7A 21                       ;                   .
2989:                 1D 14                                     ;                 Command_1D_ATTACK_OBJECT damage=14
298B:             99                                            ;             Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=99
298C:             16                                            ;             IF_NOT_JUMP address=29A3
298D:               1F                                          ;               Command_1F_PRINT_MESSAGE
298E:                 14 0C BA 17 7A 33 BB C7 DE 09 15 37       ;                 STRIKES, YOU DODGE HIS LUNGE! 
299A:                 5A A3 15 CE B5 91 C5 EB 5D                ;                 .
29A3:             CC                                            ;             Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=CC
29A4:             21                                            ;             IF_NOT_JUMP address=29C6
29A5:               0D 1F                                       ;               Command_0D_EXECUTE_LIST_WHILE_PASS size=31
29A7:                 1F                                        ;                 Command_1F_PRINT_MESSAGE
29A8:                   1B 3B 55 0B 8E D2 B0 06 79 43 DB 07     ;                   COILS RAPIDLY AROUND YOU AND CONSTRICTS!
29B4:                   B3 33 98 C7 DE 90 14 05 58 1D A0 F3     ;                   .
29C0:                   BF 0D 56 21                             ;                   .
29C4:                 1D 14                                     ;                 Command_1D_ATTACK_OBJECT damage=14
29C6:             FF                                            ;             Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=FF
29C7:             16                                            ;             IF_NOT_JUMP address=29DE
29C8:               1F                                          ;               Command_1F_PRINT_MESSAGE
29C9:                 14 16 6C F4 72 CB B5 17 C0 03 8C 04       ;                 GATHERS ITSELF FOR AN ATTACK. 
29D5:                 68 90 14 96 14 45 BD 5B 89                ;                 .
29DE:     0A 15                                                 ;     0A UPON DEATH SCRIPT
29E0:       0D 13                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=19
29E2:         1F                                                ;         Command_1F_PRINT_MESSAGE
29E3:           0E 5F BE 57 17 1F B3 B3 9A 4B 7B E3             ;           THE SERPENT IS DEAD. 
29EF:           59 9B 5D                                        ;           .
29F2:         1E 15 16                                          ;         Command_1E_SWAP_OBJECTS objectA=15(LiveSerpent) objectB=16(DeadSerpent)
29F5:     02                                                    ;     02 SHORT NAME
29F6:       05 B4 B7 F0 A4 54                                   ;       SERPENT
; Object_16 DeadSerpent
29FC:   24 40                                                   ;   Number=24 size=0040
29FE:     00 00 80                                              ;     room=00 scorePoints=00 bits=80 u.......
2A01:     03                                                    ;     03 DESCRIPTION
2A02:       1A 4E 45 31 49 46 5E 86 5F 57 17 1F                 ;       A LARGE DEAD SERPENT LIES ON THE FLOOR.
2A0E:       B3 B3 9A 87 8C D1 B5 96 96 DB 72 89                 ;       .
2A1A:       67 C7 A0                                            ;       .
2A1D:     07 15                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
2A1F:       0D 13                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=19
2A21:         0A 15                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=15 phrase="15: EAT *       u.......   *       "
2A23:         04                                                ;         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2A24:           0F A8 77 4E 5E E6 A0 7B 16 92 14 F6             ;           I'VE LOST MY APPETITE!
2A30:           A4 7F 7B 21                                     ;           .
2A34:     02                                                    ;     02 SHORT NAME
2A35:       08 E3 59 15 58 3A 62 9E 61                          ;       DEAD SERPENT
; Object_17 Hands
2A3E:   1F 09                                                   ;   Number=1F size=0009
2A40:     FF 00 80                                              ;     room=FF scorePoints=00 bits=80 u.......
2A43:     02                                                    ;     02 SHORT NAME
2A44:       04 50 72 0B 5C                                      ;       HANDS 
; Object_18 Coin
2A49:   20 34                                                   ;   Number=20 size=0034
2A4B:     9C 05 A4                                              ;     room=9C scorePoints=05 bits=A4 u.C..X..
2A4E:     03                                                    ;     03 DESCRIPTION
2A4F:       14 5F BE 5B B1 4B 7B 45 45 50 9F C0                 ;       THERE IS A COIN ON THE GROUND.
2A5B:       16 82 17 49 5E 07 B3 57 98                          ;       .
2A64:     07 14                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
2A66:       0D 12                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=18
2A68:         0A 08                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=08 phrase="08: READ *      .....X..   *       "
2A6A:         04                                                ;         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2A6B:           0E 2C 1D D5 47 F3 5F 5B 4D C3 B0 1D             ;           "PRAISED BE RAAKA-TU"
2A77:           85 5C C0                                        ;           .
2A7A:     02                                                    ;     02 SHORT NAME
2A7B:       03 3B 55 4E                                         ;       COIN
; Object_19 TinySlot
2A7F:   21 7F                                                   ;   Number=21 size=007F
2A81:     88 00 80                                              ;     room=88 scorePoints=00 bits=80 u.......
2A84:     03                                                    ;     03 DESCRIPTION
2A85:       1D 5F BE 5B B1 4B 7B 56 45 A3 7A 5E                 ;       THERE IS A TINY SLOT CUT IN THE NORTH WALL.
2A91:       17 F3 A0 36 56 D0 15 82 17 50 5E BE                 ;       .
2A9D:       A0 19 71 46 48 2E                                   ;       .
2AA3:     02                                                    ;     02 SHORT NAME
2AA4:       06 90 BE 55 DB 86 8D                                ;       TINY SLOT
2AAB:     06 53                                                 ;     06 COMMAND HANDLING IF SECOND NOUN
2AAD:       0D 51                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=81
2AAF:         0A 0F                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=0F phrase="0F: DROP IN     u.......   u......."
2AB1:         0E 4D                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=77
2AB3:           0D 24                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=36
2AB5:             14                                            ;             Command_14_EXECUTE_COMMAND_REVERSE_STATUS
2AB6:               08 18                                       ;               Command_08_COMPARE_OBJECT_TO_FIRST_NOUN object=18(Coin
2AB8:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2AB9:               02 5F BE                                    ;               THE
2ABC:             11                                            ;             Command_11_PRINT_FIRST_NOUN_SHORT_NAME
2ABD:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2ABE:               1A 4B 7B 81 BF B3 14 D6 6A C8 9C 73         ;               IS TOO BIG TO FIT IN SUCH A TINY SLOT. 
2ACA:               7B 83 7A 25 BA 03 71 83 17 7B 9B C9         ;               .
2AD6:               B8 9B C1                                    ;               .
2AD9:           0D 25                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=37
2ADB:             17 06 00                                      ;             Command_17_MOVE_OBJECT_TO_LOCATION object=06(StatueEast) location=00
2ADE:             17 07 88                                      ;             Command_17_MOVE_OBJECT_TO_LOCATION object=07(StatueWest) location=88
2AE1:             17 18 00                                      ;             Command_17_MOVE_OBJECT_TO_LOCATION object=18(Coin) location=00
2AE4:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2AE5:               1A 5F BE 66 17 8F 49 56 5E 38 C6 D6         ;               THE STATUE TURNS TO FACE THE WEST DOOR.
2AF1:               B5 C8 9C D7 46 82 17 59 5E 66 62 09         ;               .
2AFD:               15 C7 A0                                    ;               .
; Object_1A MessageUnderSlot
2B00:   18 53                                                   ;   Number=18 size=0053
2B02:     88 00 84                                              ;     room=88 scorePoints=00 bits=84 u....X..
2B05:     03                                                    ;     03 DESCRIPTION
2B06:       1C 5F BE 5B B1 4B 7B 4F 45 65 62 77                 ;       THERE IS A MESSAGE CARVED UNDER THE SLOT. 
2B12:       47 D3 14 0F B4 17 58 3F 98 96 AF DB                 ;       .
2B1E:       72 C9 B8 9B C1                                      ;       .
2B23:     02                                                    ;     02 SHORT NAME
2B24:       0A 14 53 66 CA 67 16 D3 B9 9B 6C                    ;       CARVED MESSAGE 
2B2F:     07 24                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
2B31:       0D 22                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=34
2B33:         0A 08                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=08 phrase="08: READ *      .....X..   *       "
2B35:         04                                                ;         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2B36:           1E 5F BE 67 16 D3 B9 9B 6C 1B B7 33             ;           THE MESSAGE SAYS, "SAFE PASSAGE FOR A
2B42:           BB 93 1D 5B 66 55 A4 09 B7 48 5E A3             ;           PRICE."
2B4E:           A0 52 45 05 B2 DC 63                            ;           .
; Object_1B ClosedDoor
2B55:   09 3B                                                   ;   Number=09 size=003B
2B57:     90 00 80                                              ;     room=90 scorePoints=00 bits=80 u.......
2B5A:     03                                                    ;     03 DESCRIPTION
2B5B:       0D 5F BE 09 15 A3 A0 4B 7B C9 54 A6                 ;       THE DOOR IS CLOSED.
2B67:       B7 2E                                               ;       .
2B69:     02                                                    ;     02 SHORT NAME
2B6A:       03 81 5B 52                                         ;       DOOR
2B6E:     07 22                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
2B70:       0D 20                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=32
2B72:         0A 11                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=11 phrase="11: OPEN *      u.......   *       "
2B74:         17 1B 00                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=1B(ClosedDoor) location=00
2B77:         17 1C 90                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=1C(OpenDoor) location=90
2B7A:         04                                                ;         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2B7B:           16 7C B3 6F B3 27 60 2D 60 8B 18 5F             ;           RRRRREEEEEEK - THE DOOR IS OPEN. 
2B87:           BE 09 15 A3 A0 4B 7B 5F A0 1B 9C                ;           .
; Object_1C OpenDoor
2B92:   09 30                                                   ;   Number=09 size=0030
2B94:     00 00 80                                              ;     room=00 scorePoints=00 bits=80 u.......
2B97:     03                                                    ;     03 DESCRIPTION
2B98:       12 5F BE 09 15 A3 A0 4B 7B FB B9 43                 ;       THE DOOR IS STANDING OPEN. 
2BA4:       98 AB 98 5F A0 1B 9C                                ;       .
2BAB:     02                                                    ;     02 SHORT NAME
2BAC:       03 81 5B 52                                         ;       DOOR
2BB0:     07 12                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
2BB2:       0D 10                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=16
2BB4:         0A 11                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=11 phrase="11: OPEN *      u.......   *       "
2BB6:         04                                                ;         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2BB7:           0C 8D 7B 8E 14 63 B1 FB 5C 5F A0 1B             ;           ITS ALREADY OPEN. 
2BC3:           9C                                              ;           .
; Object_1D USER
2BC4:   FF 80 87                                                ;   Number=FF size=0087
2BC7:     96 00 80                                              ;     room=96 scorePoints=00 bits=80 u.......
2BCA:     0A 76                                                 ;     0A UPON DEATH SCRIPT
2BCC:       0E 74                                               ;       Command_0E_EXECUTE_LIST_WHILE_FAIL size=116
2BCE:         0B 07                                             ;         Command_0B_SWITCH size=07
2BD0:           20 1D                                           ;           Command_20_CHECK_ACTIVE_OBJECT object=1D(USER)
2BD2:           01                                              ;           IF_NOT_JUMP address=2BD4
2BD3:             81                                            ;             CommonCommand_81
2BD4:           23                                              ;           Command_20_CHECK_ACTIVE_OBJECT object=23(Guards)
2BD5:           01                                              ;           IF_NOT_JUMP address=2BD7
2BD6:             81                                            ;             CommonCommand_81
2BD7:         0D 69                                             ;         Command_0D_EXECUTE_LIST_WHILE_PASS size=105
2BD9:           1F                                              ;           Command_1F_PRINT_MESSAGE
2BDA:             66 C7 DE DB 16 CB B9 36 A1 59 F4 F0           ;             YOU PASS OUT. WHEN YOU AWAKEN, YOU FIND
2BE6:             72 51 18 43 C2 0D D0 A6 61 51 18 48           ;             YOURSELF CHAINED TO A BLOOD STAINED ALTAR. A
2BF2:             C2 8E 7A 51 18 3D C6 40 61 DA 14 D0           ;             PRIEST IS KNEELING OVER YOU WITH A KNIFE. IT
2BFE:             47 F3 5F 6B BF 44 45 81 8D 15 58 4B           ;             LOOKS LIKE THIS IS IT. 
2C0A:             BD 66 98 8E 14 54 BD 43 F4 EC 16 35           ;             .
2C16:             79 0B BC CD B5 67 98 90 8C D1 6A 74           ;             .
2C22:             CA 51 18 59 C2 82 7B 7B 14 13 87 7F           ;             .
2C2E:             66 D6 15 49 16 A5 9F 43 16 9B 85 63           ;             .
2C3A:             BE CB B5 CB B5 9B C1                          ;             .
2C41:           81                                              ;           CommonCommand_81
2C42:     08 06                                                 ;     08 TURN SCRIPT
2C44:       0D 04                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=4
2C46:         1C 1D                                             ;         Command_1C_SET_VAR_OBJECT object=1D (USER)
2C48:         23 05                                             ;         Command_23_HEAL_VAR_OBJECT value=05
2C4A:     09 02 46 46                                           ;     09 HIT POINTS maxHitPoints=46 currentHitPoints=46
; Object_1E LiveGargoyle
2C4E:   0F 81 B4                                                ;   Number=0F size=01B4
2C51:     00 00 90                                              ;     room=00 scorePoints=00 bits=90 u..P....
2C54:     03                                                    ;     03 DESCRIPTION
2C55:       25 5F BE 5B B1 4B 7B 4A 45 FF 78 35                 ;       THERE IS A HIDEOUS GARGOYLE BLOCKING THE
2C61:       A1 73 15 C1 B1 3F DE B6 14 5D 9E 91                 ;       NORTH PASSAGE.
2C6D:       7A 82 17 50 5E BE A0 12 71 65 49 77                 ;       .
2C79:       47 2E                                               ;       .
2C7B:     02                                                    ;     02 SHORT NAME
2C7C:       06 14 6C 4B 6E DB 8B                                ;       GARGOYLE 
2C83:     09 02 FF FF                                           ;     09 HIT POINTS maxHitPoints=FF currentHitPoints=FF
2C87:     07 22                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
2C89:       0D 20                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=32
2C8B:         0A 15                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=15 phrase="15: EAT *       u.......   *       "
2C8D:         04                                                ;         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2C8E:           1C DD 72 F3 8C 96 5F 51 18 4E C2 11             ;           HE'LL EAT YOU LONG BEFORE YOU'LL EAT HIM! 
2C9A:           A0 AF 14 04 68 5B 5E 1D A1 F3 8C 96             ;           .
2CA6:           5F A3 15 EB 8F                                  ;           .
2CAB:     08 81 29                                              ;     08 TURN SCRIPT
2CAE:       0D 81 26                                            ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=294
2CB1:         01 1D                                             ;         Command_01_IS_OBJECT_IN_PACK_OR_ROOM object=1D(USER)
2CB3:         1C 1D                                             ;         Command_1C_SET_VAR_OBJECT object=1D (USER)
2CB5:         14                                                ;         Command_14_EXECUTE_COMMAND_REVERSE_STATUS
2CB6:           01 12                                           ;           Command_01_IS_OBJECT_IN_PACK_OR_ROOM object=12(LitCandle)
2CB8:         0B 81 1C                                          ;         Command_0B_SWITCH size=11C
2CBB:           05 19                                           ;           Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=19
2CBD:           2E                                              ;           IF_NOT_JUMP address=2CEC
2CBE:             0D 2C                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=44
2CC0:               1F                                          ;               Command_1F_PRINT_MESSAGE
2CC1:                 28 5F BE 73 15 C1 B1 3F DE 81 15 75       ;                 THE GARGOYLE GORES YOU WITH HIS HORN AND
2CCD:                 B1 51 18 59 C2 82 7B A3 15 CA B5 B8       ;                 RIPS YOUR GUTS OUT!
2CD9:                 A0 90 14 14 58 ED 7A 51 18 23 C6 36       ;                 .
2CE5:                 6F D1 B5 71 C6                            ;                 .
2CEA:               1D FF                                       ;               Command_1D_ATTACK_OBJECT damage=FF
2CEC:           3F                                              ;           Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=3F
2CED:           21                                              ;           IF_NOT_JUMP address=2D0F
2CEE:             0D 1F                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=31
2CF0:               1F                                          ;               Command_1F_PRINT_MESSAGE
2CF1:                 1B 5F BE 73 15 C1 B1 3F DE DE 14 05       ;                 THE GARGOYLE CLAWS YOU ACROSS THE CHEST!
2CFD:                 4A 51 18 43 C2 B9 55 CB B9 5F BE DA       ;                 .
2D09:                 14 66 62 21                               ;                 .
2D0D:               1D 32                                       ;               Command_1D_ATTACK_OBJECT damage=32
2D0F:           64                                              ;           Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=64
2D10:           2E                                              ;           IF_NOT_JUMP address=2D3F
2D11:             0D 2C                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=44
2D13:               1F                                          ;               Command_1F_PRINT_MESSAGE
2D14:                 28 C7 DE 4F 15 33 61 5F BE 80 15 5A       ;                 YOU FEEL THE GNASHING OF THE GARGOYLE'S
2D20:                 49 91 7A B8 16 82 17 49 5E 31 49 CE       ;                 TEETH IN YOUR SIDE! 
2D2C:                 A1 A5 5E 7F 17 82 62 D0 15 51 18 23       ;                 .
2D38:                 C6 46 B8 EB 5D                            ;                 .
2D3D:               1D 32                                       ;               Command_1D_ATTACK_OBJECT damage=32
2D3F:           A3                                              ;           Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=A3
2D40:           3C                                              ;           IF_NOT_JUMP address=2D7D
2D41:             0D 3A                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=58
2D43:               1F                                          ;               Command_1F_PRINT_MESSAGE
2D44:                 36 5F BE DE 14 05 4A B8 16 82 17 49       ;                 THE CLAWS OF THE GARGOYLE RIP THROUGH YOUR
2D50:                 5E 31 49 CE A1 54 5E D3 7A 6C BE 29       ;                 ARM IN AN ATTEMPT TO REACH YOUR BODY! 
2D5C:                 A1 1B 71 34 A1 94 14 4B 90 83 96 83       ;                 .
2D68:                 96 3F C0 EE 93 89 17 2F 17 DA 46 51       ;                 .
2D74:                 18 23 C6 F6 4E EB DA                      ;                 .
2D7B:               1D 19                                       ;               Command_1D_ATTACK_OBJECT damage=19
2D7D:           E1                                              ;           Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=E1
2D7E:           3E                                              ;           IF_NOT_JUMP address=2DBD
2D7F:             0D 3C                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=60
2D81:               1F                                          ;               Command_1F_PRINT_MESSAGE
2D82:                 38 5F BE 73 15 C1 B1 3F DE 4F 16 B7       ;                 THE GARGOYLE LUNGES AT YOUR FACE BUT YOU
2D8E:                 98 C3 B5 1B BC 34 A1 4B 15 9B 53 F6       ;                 PULL BACK.  HE BITES YOUR SHOULDER INSTEAD!
2D9A:                 4F 51 18 52 C2 46 C5 AB 14 AF 54 4A       ;                 .
2DA6:                 13 44 5E 7F 7B DB B5 34 A1 5A 17 2E       ;                 .
2DB2:                 A1 F4 59 D0 15 FF B9 F1 46                ;                 .
2DBB:               1D 19                                       ;               Command_1D_ATTACK_OBJECT damage=19
2DBD:           FF                                              ;           Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=FF
2DBE:           18                                              ;           IF_NOT_JUMP address=2DD7
2DBF:             0D 16                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=22
2DC1:               1F                                          ;               Command_1F_PRINT_MESSAGE
2DC2:                 14 C7 DE 09 15 37 5A 82 17 49 5E 31       ;                 YOU DODGE THE GARGOYLE'S HORN.
2DCE:                 49 CE A1 A5 5E A9 15 E7 B2                ;                 .
2DD7:     0A 2C                                                 ;     0A UPON DEATH SCRIPT
2DD9:       0D 2A                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=42
2DDB:         1F                                                ;         Command_1F_PRINT_MESSAGE
2DDC:           22 5F BE 73 15 C1 B1 3F DE 7B 17 B5             ;           THE GARGOYLE TAKES A FINAL BREATH AND THEN
2DE8:           85 7B 14 10 67 33 48 6F 4F 82 49 90             ;           EXPIRES.
2DF4:           14 16 58 F0 72 3A 15 94 A5 6F 62                ;           .
2DFF:         17 1E 00                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=1E(LiveGargoyle) location=00
2E02:         17 1F 8E                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=1F(DeadGargoyle) location=8E
; Object_1F DeadGargoyle
2E05:   0F 53                                                   ;   Number=0F size=0053
2E07:     00 00 80                                              ;     room=00 scorePoints=00 bits=80 u.......
2E0A:     03                                                    ;     03 DESCRIPTION
2E0B:       24 5F BE 5B B1 4B 7B 5F BE FF 14 F3                 ;       THERE IS THE DEAD CARCASS OF AN UGLY
2E17:       46 14 53 15 53 D1 B5 83 64 97 96 D3                 ;       GARGOYLE NEARBY. 
2E23:       6D 73 15 C1 B1 3F DE 8F 16 2C 49 DB                 ;       .
2E2F:       E0                                                  ;       .
2E30:     07 1D                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
2E32:       0D 1B                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=27
2E34:         0A 15                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=15 phrase="15: EAT *       u.......   *       "
2E36:         04                                                ;         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2E37:           17 7A C4 CB 06 82 17 95 7A BD 15 49             ;           UGH! I THINK I'M GOING TO BE SICK!
2E43:           90 50 9F D6 6A C4 9C 55 5E DD 78 21             ;           .
2E4F:     02                                                    ;     02 SHORT NAME
2E50:       09 E3 59 09 58 31 49 CE A1 45                       ;       DEAD GARGOYLE
; Object_20 Wall
2E5A:   25 32                                                   ;   Number=25 size=0032
2E5C:     FF 00 80                                              ;     room=FF scorePoints=00 bits=80 u.......
2E5F:     07 28                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
2E61:       0B 26                                               ;       Command_0B_SWITCH size=26
2E63:         0A 17                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=17 phrase="17: CLIMB *     u.......   *       "
2E65:         20                                                ;         IF_NOT_JUMP address=2E86
2E66:           04                                              ;           Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
2E67:             1E C7 DE D3 14 90 96 F3 A0 C3 54 A3           ;             YOU CAN NOT CLIMB THE WALL, IT IS TOO
2E73:             91 5F BE F3 17 16 8D D6 15 D5 15 89           ;             SMOOTH.
2E7F:             17 D5 9C C1 93 77 BE                          ;             .
2E86:         34                                                ;         Command_0A_COMPARE_TO_PHRASE_FORM val=34 phrase="34: JUMP OVER   *          u......."
2E87:         01                                                ;         IF_NOT_JUMP address=2E89
2E88:           89                                              ;           CommonCommand_89
2E89:     02                                                    ;     02 SHORT NAME
2E8A:       03 0E D0 4C                                         ;       WALL
; Object_21 Vines
2E8E:   26 29                                                   ;   Number=26 size=0029
2E90:     9D 00 80                                              ;     room=9D scorePoints=00 bits=80 u.......
2E93:     03                                                    ;     03 DESCRIPTION
2E94:       1E 4E 45 31 49 50 5E 91 62 B5 A0 B8                 ;       A LARGE NETWORK OF VINES CLINGS TO THE WALL.
2EA0:       16 D3 17 75 98 DE 14 91 7A D6 B5 D6                 ;       
2EAC:       9C DB 72 0E D0 9B 8F                                ;       .
2EB3:     02                                                    ;     02 SHORT NAME
2EB4:       04 10 CB 4B 62                                      ;       VINES 
; Object_22 GoldenChopstick
2EB9:   1E 28                                                   ;   Number=1E size=0028
2EBB:     8F 05 A0                                              ;     room=8F scorePoints=05 bits=A0 u.C.....
2EBE:     03                                                    ;     03 DESCRIPTION
2EBF:       16 5F BE 5B B1 4B 7B 49 45 BE 9F 83                 ;       THERE IS A GOLDEN CHOPSTICK HERE.
2ECB:       61 29 54 26 A7 DD 78 9F 15 7F B1                    ;       .
2ED6:     02                                                    ;     02 SHORT NAME
2ED7:       0B 3E 6E F0 59 DA 14 6D A0 85 BE 4B                 ;       GOLDEN CHOPSTICK
; Object_23 Guards
2EE3:   28 80 CA                                                ;   Number=28 size=00CA
2EE6:     9C 00 90                                              ;     room=9C scorePoints=00 bits=90 u..P....
2EE9:     03                                                    ;     03 DESCRIPTION
2EEA:       27 B8 B7 2B 62 09 8A 94 C3 0B 5C 14                 ;       SEVERAL GUARDS CARRYING LETHAL CROSSBOWS
2EF6:       53 8B B4 AB 98 F6 8B 4E 72 E4 14 E5                 ;       TURN TO FACE YOU.
2F02:       A0 09 4F D6 B5 38 C6 89 17 4B 15 9B                 ;       .
2F0E:       53 C7 DE 2E                                         ;       .
2F12:     08 80 95                                              ;     08 TURN SCRIPT
2F15:       0E 80 92                                            ;       Command_0E_EXECUTE_LIST_WHILE_FAIL size=146
2F18:         0D 2F                                             ;         Command_0D_EXECUTE_LIST_WHILE_PASS size=47
2F1A:           14                                              ;           Command_14_EXECUTE_COMMAND_REVERSE_STATUS
2F1B:             01 1D                                         ;             Command_01_IS_OBJECT_IN_PACK_OR_ROOM object=1D(USER)
2F1D:           0B 29                                           ;           Command_0B_SWITCH size=29
2F1F:             03 9C 23                                      ;             Command_03_IS_OBJECT_AT_LOCATION object=23(Guards) location=9C
2F22:             07                                            ;             IF_NOT_JUMP address=2F2A
2F23:               0D 05                                       ;               Command_0D_EXECUTE_LIST_WHILE_PASS size=5
2F25:                 00 9D                                     ;                 Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=9D
2F27:                 01 1D                                     ;                 Command_01_IS_OBJECT_IN_PACK_OR_ROOM object=1D(USER)
2F29:                 86                                        ;                 CommonCommand_86
2F2A:             9F 23                                         ;             Command_03_IS_OBJECT_AT_LOCATION object=23(Guards) location=9F
2F2C:             07                                            ;             IF_NOT_JUMP address=2F34
2F2D:               0D 05                                       ;               Command_0D_EXECUTE_LIST_WHILE_PASS size=5
2F2F:                 00 9C                                     ;                 Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=9C
2F31:                 01 1D                                     ;                 Command_01_IS_OBJECT_IN_PACK_OR_ROOM object=1D(USER)
2F33:                 86                                        ;                 CommonCommand_86
2F34:             9E 23                                         ;             Command_03_IS_OBJECT_AT_LOCATION object=23(Guards) location=9E
2F36:             07                                            ;             IF_NOT_JUMP address=2F3E
2F37:               0D 05                                       ;               Command_0D_EXECUTE_LIST_WHILE_PASS size=5
2F39:                 00 9F                                     ;                 Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=9F
2F3B:                 01 1D                                     ;                 Command_01_IS_OBJECT_IN_PACK_OR_ROOM object=1D(USER)
2F3D:                 86                                        ;                 CommonCommand_86
2F3E:             9D 23                                         ;             Command_03_IS_OBJECT_AT_LOCATION object=23(Guards) location=9D
2F40:             07                                            ;             IF_NOT_JUMP address=2F48
2F41:               0D 05                                       ;               Command_0D_EXECUTE_LIST_WHILE_PASS size=5
2F43:                 00 9E                                     ;                 Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=9E
2F45:                 01 1D                                     ;                 Command_01_IS_OBJECT_IN_PACK_OR_ROOM object=1D(USER)
2F47:                 86                                        ;                 CommonCommand_86
2F48:           0C                                              ;           Command_0C_FAIL
2F49:         0D 5F                                             ;         Command_0D_EXECUTE_LIST_WHILE_PASS size=95
2F4B:           01 1D                                           ;           Command_01_IS_OBJECT_IN_PACK_OR_ROOM object=1D(USER)
2F4D:           1C 1D                                           ;           Command_1C_SET_VAR_OBJECT object=1D (USER)
2F4F:           1F                                              ;           Command_1F_PRINT_MESSAGE
2F50:             58 A6 1D 51 A0 D0 15 06 67 33 61 79           ;             "STOP! INFIDEL DOG!", THE GUARDS LEVEL THEIR
2F5C:             5B 06 07 82 17 49 5E 94 C3 0B 5C F8           ;             CROSSBOWS AND LOOSE THEIR BOLTS! YOUR BODY
2F68:             8B 33 61 5F BE 23 7B B9 55 D4 B9 85           ;             FALLS TO THE GROUND RIDDLED WITH THE SHAFTS!
2F74:             A1 90 14 0E 58 45 A0 56 5E EB 72 84           ;             .
2F80:             AF CE 9F 6B B5 C7 DE 84 AF 93 9E 4B           ;             .
2F8C:             15 0D 8D 89 17 82 17 49 5E 07 B3 33           ;             .
2F98:             98 06 B2 FF 5A 19 58 82 7B 82 17 55           ;             .
2FA4:             5E 48 72 09 C0                                ;             .
2FA9:           81                                              ;           CommonCommand_81
2FAA:     02                                                    ;     02 SHORT NAME
2FAB:       04 23 6F 4D B1                                      ;       GUARDS
; Object_24 Object24
2FB0:   29 4C                                                   ;   Number=29 size=004C
2FB2:     1D 00 00                                              ;     room=1D scorePoints=00 bits=00 *       
2FB5:     08 47                                                 ;     08 TURN SCRIPT
2FB7:       0B 45                                               ;       Command_0B_SWITCH size=45
2FB9:         03 9C 23                                          ;         Command_03_IS_OBJECT_AT_LOCATION object=23(Guards) location=9C
2FBC:         0E                                                ;         IF_NOT_JUMP address=2FCB
2FBD:           0E 0C                                           ;           Command_0E_EXECUTE_LIST_WHILE_FAIL size=12
2FBF:             0D 04                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=4
2FC1:               03 9A 1D                                    ;               Command_03_IS_OBJECT_AT_LOCATION object=1D(USER) location=9A
2FC4:               85                                          ;               CommonCommand_85
2FC5:             0D 04                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=4
2FC7:               03 99 1D                                    ;               Command_03_IS_OBJECT_AT_LOCATION object=1D(USER) location=99
2FCA:               87                                          ;               CommonCommand_87
2FCB:         9F 23                                             ;         Command_03_IS_OBJECT_AT_LOCATION object=23(Guards) location=9F
2FCD:         0E                                                ;         IF_NOT_JUMP address=2FDC
2FCE:           0E 0C                                           ;           Command_0E_EXECUTE_LIST_WHILE_FAIL size=12
2FD0:             0D 04                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=4
2FD2:               03 99 1D                                    ;               Command_03_IS_OBJECT_AT_LOCATION object=1D(USER) location=99
2FD5:               85                                          ;               CommonCommand_85
2FD6:             0D 04                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=4
2FD8:               03 98 1D                                    ;               Command_03_IS_OBJECT_AT_LOCATION object=1D(USER) location=98
2FDB:               87                                          ;               CommonCommand_87
2FDC:         9E 23                                             ;         Command_03_IS_OBJECT_AT_LOCATION object=23(Guards) location=9E
2FDE:         0E                                                ;         IF_NOT_JUMP address=2FED
2FDF:           0E 0C                                           ;           Command_0E_EXECUTE_LIST_WHILE_FAIL size=12
2FE1:             0D 04                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=4
2FE3:               03 98 1D                                    ;               Command_03_IS_OBJECT_AT_LOCATION object=1D(USER) location=98
2FE6:               85                                          ;               CommonCommand_85
2FE7:             0D 04                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=4
2FE9:               03 9B 1D                                    ;               Command_03_IS_OBJECT_AT_LOCATION object=1D(USER) location=9B
2FEC:               87                                          ;               CommonCommand_87
2FED:         9D 23                                             ;         Command_03_IS_OBJECT_AT_LOCATION object=23(Guards) location=9D
2FEF:         0E                                                ;         IF_NOT_JUMP address=2FFE
2FF0:           0E 0C                                           ;           Command_0E_EXECUTE_LIST_WHILE_FAIL size=12
2FF2:             0D 04                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=4
2FF4:               03 9B 1D                                    ;               Command_03_IS_OBJECT_AT_LOCATION object=1D(USER) location=9B
2FF7:               85                                          ;               CommonCommand_85
2FF8:             0D 04                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=4
2FFA:               03 9A 1D                                    ;               Command_03_IS_OBJECT_AT_LOCATION object=1D(USER) location=9A
2FFD:               87                                          ;               CommonCommand_87
; Object_25 GemA
2FFE:   13 30                                                   ;   Number=13 size=0030
3000:     9C 00 A0                                              ;     room=9C scorePoints=00 bits=A0 u.C.....
3003:     02                                                    ;     02 SHORT NAME
3004:       08 EF A6 51 54 4B C6 AF 6C                          ;       PRECIOUS GEM
300D:     08 21                                                 ;     08 TURN SCRIPT
300F:       0D 1F                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=31
3011:         03 9C 25                                          ;         Command_03_IS_OBJECT_AT_LOCATION object=25(GemA) location=9C
3014:         0B 1A                                             ;         Command_0B_SWITCH size=1A
3016:           05 33                                           ;           Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=33
3018:           03                                              ;           IF_NOT_JUMP address=301C
3019:             17 25 89                                      ;             Command_17_MOVE_OBJECT_TO_LOCATION object=25(GemA) location=89
301C:           66                                              ;           Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=66
301D:           03                                              ;           IF_NOT_JUMP address=3021
301E:             17 25 94                                      ;             Command_17_MOVE_OBJECT_TO_LOCATION object=25(GemA) location=94
3021:           99                                              ;           Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=99
3022:           03                                              ;           IF_NOT_JUMP address=3026
3023:             17 25 86                                      ;             Command_17_MOVE_OBJECT_TO_LOCATION object=25(GemA) location=86
3026:           CC                                              ;           Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=CC
3027:           03                                              ;           IF_NOT_JUMP address=302B
3028:             17 25 8E                                      ;             Command_17_MOVE_OBJECT_TO_LOCATION object=25(GemA) location=8E
302B:           FF                                              ;           Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=FF
302C:           03                                              ;           IF_NOT_JUMP address=3030
302D:             17 25 83                                      ;             Command_17_MOVE_OBJECT_TO_LOCATION object=25(GemA) location=83
; Object_26 GemB
3030:   13 23                                                   ;   Number=13 size=0023
3032:     00 05 A0                                              ;     room=00 scorePoints=05 bits=A0 u.C.....
3035:     02                                                    ;     02 SHORT NAME
3036:       08 EF A6 51 54 4B C6 AF 6C                          ;       PRECIOUS GEM
303F:     03                                                    ;     03 DESCRIPTION
3040:       14 5F BE 5B B1 4B 7B 52 45 65 B1 C7                 ;       THERE IS A PRECIOUS GEM HERE. 
304C:       7A C9 B5 5B 61 F4 72 DB 63                          ;       .
; Object_27 HiddenGem
3055:   2A 32                                                   ;   Number=2A size=0032
3057:     FF 00 00                                              ;     room=FF scorePoints=00 bits=00 *       
305A:     02                                                    ;     02 SHORT NAME
305B:       03 01 B3 4D                                         ;       ROOM
305F:     07 28                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
3061:       0D 26                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=38
3063:         0A 0B                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=0B phrase="0B: LOOK AT     *          u......."
3065:         01 25                                             ;         Command_01_IS_OBJECT_IN_PACK_OR_ROOM object=25(GemA)
3067:         04                                                ;         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3068:           20 C7 DE 03 15 61 B7 74 CA 7B 14 EF             ;           YOU DISCOVER A PRECIOUS GEM HIDDEN IN A
3074:           A6 51 54 4B C6 AF 6C A3 15 BF 59 8B             ;           CREVICE.
3080:           96 83 96 E4 14 D3 62 BF 53                      ;           .
; Object_28 UnlitLamp
3089:   1B 62                                                   ;   Number=1B size=0062
308B:     00 00 AC                                              ;     room=00 scorePoints=00 bits=AC u.C.AX..
308E:     02                                                    ;     02 SHORT NAME
308F:       03 4F 8B 50                                         ;       LAMP
3093:     03                                                    ;     03 DESCRIPTION
3094:       0E 5F BE 5B B1 4B 7B 4E 45 72 48 9F                 ;       THERE IS A LAMP HERE.
30A0:       15 7F B1                                            ;       .
30A3:     07 48                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
30A5:       0B 46                                               ;       Command_0B_SWITCH size=46
30A7:         0A 14                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=14 phrase="14: LIGHT WITH  u...A...   u...A..."
30A9:         1C                                                ;         IF_NOT_JUMP address=30C6
30AA:           0E 1A                                           ;           Command_0E_EXECUTE_LIST_WHILE_FAIL size=26
30AC:             0D 17                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=23
30AE:               09 12                                       ;               Command_09_COMPARE_OBJECT_TO_SECOND_NOUN object=12(LitCandle
30B0:               1E 28 14                                    ;               Command_1E_SWAP_OBJECTS objectA=28(UnlitLamp) objectB=14(LitLamp)
30B3:               04                                          ;               Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
30B4:                 10 5F BE 3B 16 D3 93 4B 7B 09 9A BF       ;                 THE LAMP IS NOW BURNING.
30C0:                 14 D3 B2 CF 98                            ;                 .
30C5:             88                                            ;             CommonCommand_88
30C6:         18                                                ;         Command_0A_COMPARE_TO_PHRASE_FORM val=18 phrase="18: RUB *       u.......   *       "
30C7:         19                                                ;         IF_NOT_JUMP address=30E1
30C8:           04                                              ;           Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
30C9:             17 29 D1 09 15 51 18 56 C2 90 73 DB           ;             WHO DO YOU THINK YOU ARE, ALADDIN?
30D5:             83 1B A1 2F 49 03 EE 46 8B 90 5A 3F           ;             .
30E1:         08                                                ;         Command_0A_COMPARE_TO_PHRASE_FORM val=08 phrase="08: READ *      .....X..   *       "
30E2:         0A                                                ;         IF_NOT_JUMP address=30ED
30E3:           04                                              ;           Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
30E4:             08 49 1B 99 16 14 BC A4 C3                    ;             "DO NOT RUB"
; Object_29 Floor
30ED:   2B 09                                                   ;   Number=2B size=0009
30EF:     00 00 80                                              ;     room=00 scorePoints=00 bits=80 u.......
30F2:     02                                                    ;     02 SHORT NAME
30F3:       04 89 67 A3 A0                                      ;       FLOOR 
; Object_2A Exit
30F8:   2C 0B                                                   ;   Number=2C size=000B
30FA:     00 00 80                                              ;     room=00 scorePoints=00 bits=80 u.......
30FD:     07 01                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
30FF:       93                                                  ;       CommonCommand_93
3100:     02                                                    ;     02 SHORT NAME
3101:       03 23 63 54                                         ;       EXIT
; Object_2B Passage
3105:   2D 0D                                                   ;   Number=2D size=000D
3107:     00 00 80                                              ;     room=00 scorePoints=00 bits=80 u.......
310A:     07 01                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
310C:       93                                                  ;       CommonCommand_93
310D:     02                                                    ;     02 SHORT NAME
310E:       05 55 A4 09 B7 45                                   ;       PASSAGE
; Object_2C Hole
3114:   2E 0B                                                   ;   Number=2E size=000B
3116:     00 00 80                                              ;     room=00 scorePoints=00 bits=80 u.......
3119:     07 01                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
311B:       93                                                  ;       CommonCommand_93
311C:     02                                                    ;     02 SHORT NAME
311D:       03 7E 74 45                                         ;       HOLE
; Object_2D Corridor
3121:   2F 0E                                                   ;   Number=2F size=000E
3123:     00 00 80                                              ;     room=00 scorePoints=00 bits=80 u.......
3126:     07 01                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
3128:       93                                                  ;       CommonCommand_93
3129:     02                                                    ;     02 SHORT NAME
312A:       06 44 55 06 B2 A3 A0                                ;       CORRIDOR 
; Object_2E Corner
3131:   30 09                                                   ;   Number=30 size=0009
3133:     00 00 80                                              ;     room=00 scorePoints=00 bits=80 u.......
3136:     02                                                    ;     02 SHORT NAME
3137:       04 44 55 74 98                                      ;       CORNER
; Object_2F Bow
313C:   31 07                                                   ;   Number=31 size=0007
313E:     88 00 80                                              ;     room=88 scorePoints=00 bits=80 u.......
3141:     02                                                    ;     02 SHORT NAME
3142:       02 09 4F                                            ;       BOW
; Object_30 Arrow
3145:   32 09                                                   ;   Number=32 size=0009
3147:     88 00 80                                              ;     room=88 scorePoints=00 bits=80 u.......
314A:     02                                                    ;     02 SHORT NAME
314B:       04 3C 49 6B A1                                      ;       ARROW 
; Object_31 Hallway
3150:   33 0D                                                   ;   Number=33 size=000D
3152:     00 00 80                                              ;     room=00 scorePoints=00 bits=80 u.......
3155:     07 01                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
3157:       93                                                  ;       CommonCommand_93
3158:     02                                                    ;     02 SHORT NAME
3159:       05 4E 72 B3 8E 59                                   ;       HALLWAY
; Object_32 Chamber
315F:   34 0A                                                   ;   Number=34 size=000A
3161:     8D 00 80                                              ;     room=8D scorePoints=00 bits=80 u.......
3164:     02                                                    ;     02 SHORT NAME
3165:       05 1B 54 AF 91 52                                   ;       CHAMBER
; Object_33 Vault
316B:   35 09                                                   ;   Number=35 size=0009
316D:     91 00 80                                              ;     room=91 scorePoints=00 bits=80 u.......
3170:     02                                                    ;     02 SHORT NAME
3171:       04 D7 C9 33 8E                                      ;       VAULT 
; Object_34 Entrance
3176:   36 0E                                                   ;   Number=36 size=000E
3178:     00 00 80                                              ;     room=00 scorePoints=00 bits=80 u.......
317B:     07 01                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
317D:       93                                                  ;       CommonCommand_93
317E:     02                                                    ;     02 SHORT NAME
317F:       06 9E 61 D0 B0 9B 53                                ;       ENTRANCE 
; Object_35 Tunnel
3186:   37 0C                                                   ;   Number=37 size=000C
3188:     00 00 80                                              ;     room=00 scorePoints=00 bits=80 u.......
318B:     07 01                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
318D:       93                                                  ;       CommonCommand_93
318E:     02                                                    ;     02 SHORT NAME
318F:       04 70 C0 6E 98                                      ;       TUNNEL
; Object_36 Jungle
3194:   38 0C                                                   ;   Number=38 size=000C
3196:     FF 00 80                                              ;     room=FF scorePoints=00 bits=80 u.......
3199:     07 01                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
319B:       93                                                  ;       CommonCommand_93
319C:     02                                                    ;     02 SHORT NAME
319D:       04 F0 81 BF 6D                                      ;       JUNGLE
; Object_37 Temple
31A2:   39 0C                                                   ;   Number=39 size=000C
31A4:     FF 00 80                                              ;     room=FF scorePoints=00 bits=80 u.......
31A7:     07 01                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
31A9:       93                                                  ;       CommonCommand_93
31AA:     02                                                    ;     02 SHORT NAME
31AB:       04 EF BD FF A5                                      ;       TEMPLE
; Object_38 Serpents
31B0:   24 0B                                                   ;   Number=24 size=000B
31B2:     9C 00 80                                              ;     room=9C scorePoints=00 bits=80 u.......
31B5:     02                                                    ;     02 SHORT NAME
31B6:       06 B4 B7 F0 A4 0B C0                                ;       SERPENTS 
; Object_39 Pit
31BD:   3A 31                                                   ;   Number=3A size=0031
31BF:     82 00 80                                              ;     room=82 scorePoints=00 bits=80 u.......
31C2:     07 28                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
31C4:       0B 26                                               ;       Command_0B_SWITCH size=26
31C6:         0A 36                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=36 phrase="36: CLIMB IN    *          *       "
31C8:         01                                                ;         IF_NOT_JUMP address=31CA
31C9:           8A                                              ;           CommonCommand_8A
31CA:         33                                                ;         Command_0A_COMPARE_TO_PHRASE_FORM val=33 phrase="??"
31CB:         01                                                ;         IF_NOT_JUMP address=31CD
31CC:           8A                                              ;           CommonCommand_8A
31CD:         34                                                ;         Command_0A_COMPARE_TO_PHRASE_FORM val=34 phrase="34: JUMP OVER   *          u......."
31CE:         01                                                ;         IF_NOT_JUMP address=31D0
31CF:           8A                                              ;           CommonCommand_8A
31D0:         26                                                ;         Command_0A_COMPARE_TO_PHRASE_FORM val=26 phrase="26: GO AROUND   *          u......."
31D1:         17                                                ;         IF_NOT_JUMP address=31E9
31D2:           04                                              ;           Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
31D3:             15 5F BE 5B B1 4B 7B EB 99 1B D0 94           ;             THERE IS NO WAY AROUND THE PIT.
31DF:             14 30 A1 16 58 DB 72 96 A5 2E                 ;             .
31E9:         17                                                ;         Command_0A_COMPARE_TO_PHRASE_FORM val=17 phrase="17: CLIMB *     u.......   *       "
31EA:         01                                                ;         IF_NOT_JUMP address=31EC
31EB:           8A                                              ;           CommonCommand_8A
31EC:     02                                                    ;     02 SHORT NAME
31ED:       02 96 A5                                            ;       PIT
; Object_3A Ceiling
31F0:   3B 0A                                                   ;   Number=3B size=000A
31F2:     00 00 80                                              ;     room=00 scorePoints=00 bits=80 u.......
31F5:     02                                                    ;     02 SHORT NAME
31F6:       05 AB 53 90 8C 47                                   ;       CEILING
; Object_3B AlterB
31FC:   22 39                                                   ;   Number=22 size=0039
31FE:     A5 00 80                                              ;     room=A5 scorePoints=00 bits=80 u.......
3201:     02                                                    ;     02 SHORT NAME
3202:       04 4E 48 23 62                                      ;       ALTER 
3207:     07 2E                                                 ;     07 COMMAND HANDLING IF FIRST NOUN
3209:       0D 2C                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=44
320B:         0A 12                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=12 phrase="12: PULL *      u.......   *       "
320D:         04                                                ;         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
320E:           28 C7 DE D3 14 90 96 F3 A0 C8 93 56             ;           YOU CAN NOT MOVE THE ALTER FROM BENEATH IT,
321A:           5E DB 72 4E 48 23 62 79 68 44 90 8F             ;           IT IS TOO HEAVY.
3226:           61 82 49 D6 15 0B EE 0B BC D6 B5 2B             ;           .
3232:           A0 E3 72 9F CD                                  ;           .
; Object_3C Object3C
3237:   3C 03                                                   ;   Number=3C size=0003
3239:     1D 00 80                                              ;     room=1D scorePoints=00 bits=80 u.......
; ENDOF 20FF
```

# General Commands

```code
GeneralCommands: 
323C:   00 85 BB 0E 85 B8                                       ;   Command_0E_EXECUTE_LIST_WHILE_FAIL size=1464
3242:     0D 2C                                                 ;     Command_0D_EXECUTE_LIST_WHILE_PASS size=44
3244:       0E 08                                               ;       Command_0E_EXECUTE_LIST_WHILE_FAIL size=8
3246:         0A 01                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=01 phrase="01: NORTH *     *          *       "
3248:         0A 02                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=02 phrase="02: SOUTH *     *          *       "
324A:         0A 03                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=03 phrase="03: EAST *      *          *       "
324C:         0A 04                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=04 phrase="04: WEST *      *          *       "
324E:       0E 20                                               ;       Command_0E_EXECUTE_LIST_WHILE_FAIL size=32
3250:         13                                                ;         Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
3251:         0D 1D                                             ;         Command_0D_EXECUTE_LIST_WHILE_PASS size=29
3253:           04                                              ;           Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3254:             19 5F BE 5B B1 4B 7B EB 99 1B D0 89           ;             THERE IS NO WAY TO GO THAT DIRECTION.
3260:             17 81 15 82 17 73 49 94 5A E6 5F C0           ;             .
326C:             7A 2E                                         ;             .
326E:           20 1D                                           ;           Command_20_CHECK_ACTIVE_OBJECT object=1D(USER)
3270:     0B 85 83                                              ;     Command_0B_SWITCH size=583
3273:       0A 05                                               ;       Command_0A_COMPARE_TO_PHRASE_FORM val=05 phrase="05: GET *       ..C.....   *       "
3275:       21                                                  ;       IF_NOT_JUMP address=3297
3276:         0E 1F                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=31
3278:           0D 19                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=25
327A:             1A                                            ;             Command_1A_SET_VAR_OBJECT_TO_FIRST_NOUN
327B:             18                                            ;             Command_18_CHECK_VAR_OBJECT_OWNED_BY_ACTIVE_OBJECT
327C:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
327D:               13 C7 DE 94 14 43 5E EF 8D 13 47 D3         ;               YOU ARE ALREADY CARRYING THE
3289:               14 83 B3 91 7A 82 17 45                     ;               .
3291:             16                                            ;             Command_16_PRINT_VAR_NOUN_SHORT_NAME
3292:             84                                            ;             CommonCommand_84
3293:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
3294:           83                                              ;           CommonCommand_83
3295:           14                                              ;           Command_14_EXECUTE_COMMAND_REVERSE_STATUS
3296:             0C                                            ;             Command_0C_FAIL
3297:       06                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=06 phrase="06: DROP *      ..C.....   *       "
3298:       0C                                                  ;       IF_NOT_JUMP address=32A5
3299:         0D 0A                                             ;         Command_0D_EXECUTE_LIST_WHILE_PASS size=10
329B:           1A                                              ;           Command_1A_SET_VAR_OBJECT_TO_FIRST_NOUN
329C:           10                                              ;           Command_10_DROP_OBJECT
329D:           04                                              ;           Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
329E:             06 F9 5B 9F A6 9B 5D                          ;             DROPPED. 
32A5:       08                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=08 phrase="08: READ *      .....X..   *       "
32A6:       17                                                  ;       IF_NOT_JUMP address=32BE
32A7:         0E 15                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=21
32A9:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
32AA:           0D 12                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=18
32AC:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
32AD:               0E 89 74 D3 14 9B 96 1B A1 63 B1 16         ;               HOW CAN YOU READ THE 
32B9:               58 DB 72                                    ;               .
32BC:             11                                            ;             Command_11_PRINT_FIRST_NOUN_SHORT_NAME
32BD:             84                                            ;             CommonCommand_84
32BE:       11                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=11 phrase="11: OPEN *      u.......   *       "
32BF:       16                                                  ;       IF_NOT_JUMP address=32D6
32C0:         0E 14                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=20
32C2:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
32C3:           0D 11                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=17
32C5:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
32C6:               0D EB 99 0F A0 D3 14 91 96 F0 A4 82         ;               NO ONE CAN OPEN THE
32D2:               17 45                                       ;               .
32D4:             11                                            ;             Command_11_PRINT_FIRST_NOUN_SHORT_NAME
32D5:             84                                            ;             CommonCommand_84
32D6:       12                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=12 phrase="12: PULL *      u.......   *       "
32D7:       21                                                  ;       IF_NOT_JUMP address=32F9
32D8:         0E 1F                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=31
32DA:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
32DB:           0D 1C                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=28
32DD:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
32DE:               13 33 D1 09 15 E6 96 51 18 4E C2 98         ;               WHY DON'T YOU LEAVE THE POOR
32EA:               5F 56 5E DB 72 81 A6 52                     ;               .
32F2:             11                                            ;             Command_11_PRINT_FIRST_NOUN_SHORT_NAME
32F3:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
32F4:               04 49 48 7F 98                              ;               ALONE.
32F9:       09                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=09 phrase="09: ATTACK WITH ...P....   .v......"
32FA:       81 37                                               ;       IF_NOT_JUMP address=3433
32FC:         0E 81 34                                          ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=308
32FF:           14                                              ;           Command_14_EXECUTE_COMMAND_REVERSE_STATUS
3300:             1B                                            ;             Command_1B_SET_VAR_OBJECT_TO_SECOND_NOUN
3301:           14                                              ;           Command_14_EXECUTE_COMMAND_REVERSE_STATUS
3302:             0E 03                                         ;             Command_0E_EXECUTE_LIST_WHILE_FAIL size=3
3304:               09 17                                       ;               Command_09_COMPARE_OBJECT_TO_SECOND_NOUN object=17(Hands
3306:               83                                          ;               CommonCommand_83
3307:           0E 81 29                                        ;           Command_0E_EXECUTE_LIST_WHILE_FAIL size=297
330A:             0D 1F                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=31
330C:               14                                          ;               Command_14_EXECUTE_COMMAND_REVERSE_STATUS
330D:                 15 40                                     ;                 Command_15_CHECK_OBJECT_BITS bits=40 .v......
330F:               14                                          ;               Command_14_EXECUTE_COMMAND_REVERSE_STATUS
3310:                 09 17                                     ;                 Command_09_COMPARE_OBJECT_TO_SECOND_NOUN object=17(Hands
3312:               04                                          ;               Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3313:                 0C C7 DE D3 14 E6 96 AF 15 B3 B3 5F       ;                 YOU CAN'T HURT THE
331F:                 BE                                        ;                 .
3320:               11                                          ;               Command_11_PRINT_FIRST_NOUN_SHORT_NAME
3321:               04                                          ;               Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3322:                 06 56 D1 16 71 DB 72                      ;                 WITH THE 
3329:               12                                          ;               Command_12_PRINT_SECOND_NOUN_SHORT_NAME
332A:               84                                          ;               CommonCommand_84
332B:             13                                            ;             Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
332C:             0D 1A                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=26
332E:               1A                                          ;               Command_1A_SET_VAR_OBJECT_TO_FIRST_NOUN
332F:               14                                          ;               Command_14_EXECUTE_COMMAND_REVERSE_STATUS
3330:                 15 10                                     ;                 Command_15_CHECK_OBJECT_BITS bits=10 ...P....
3332:               04                                          ;               Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3333:                 12 73 7B 77 5B D0 B5 C9 9C 36 A0 89       ;                 IT DOES NO GOOD TO ATTACK A
333F:                 17 96 14 45 BD C3 83                      ;                 .
3346:               11                                          ;               Command_11_PRINT_FIRST_NOUN_SHORT_NAME
3347:               84                                          ;               CommonCommand_84
3348:             0D 80 D7                                      ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=215
334B:               1A                                          ;               Command_1A_SET_VAR_OBJECT_TO_FIRST_NOUN
334C:               0B 80 D3                                    ;               Command_0B_SWITCH size=D3
334F:                 09 09                                     ;                 Command_09_COMPARE_OBJECT_TO_SECOND_NOUN object=09(Sword
3351:                 80 99                                     ;                 IF_NOT_JUMP address=33EC
3353:                   0B 80 96                                ;                   Command_0B_SWITCH size=96
3356:                     05 52                                 ;                     Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=52
3358:                     28                                    ;                     IF_NOT_JUMP address=3381
3359:                       0D 26                               ;                       Command_0D_EXECUTE_LIST_WHILE_PASS size=38
335B:                         04                                ;                         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
335C:                           17 4F 45 7A 79 FB C0 6C BE 66 C6 04;                           A MIGHTY THRUST, BUT IT MISSES THE
3368:                           EE 73 C6 73 7B D5 92 B5 B7 82 17 45;                           .
3374:                         16                                ;                         Command_16_PRINT_VAR_NOUN_SHORT_NAME
3375:                         04                                ;                         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3376:                           0A 7B 50 4D 45 49 7A 36 92 21 62;                           BY A KILOMETER!
3381:                     A4                                    ;                     Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=A4
3382:                     2D                                    ;                     IF_NOT_JUMP address=33B0
3383:                       0D 2B                               ;                       Command_0D_EXECUTE_LIST_WHILE_PASS size=43
3385:                         04                                ;                         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3386:                           1C 89 4E 73 9E F5 B3 F5 72 59 15 C2;                           BLOOD RUSHES FORTH AS YOU HAVE SLASHED THE
3392:                           B3 95 14 51 18 4A C2 CF 49 5E 17 5A;                           .
339E:                           49 F3 5F 5F BE                  ;                           .
33A3:                         16                                ;                         Command_16_PRINT_VAR_NOUN_SHORT_NAME
33A4:                         04                                ;                         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
33A5:                           08 83 7A 5F BE 94 14 EB 8F      ;                           IN THE ARM! 
33AE:                         1D 0A                             ;                         Command_1D_ATTACK_OBJECT damage=0A
33B0:                     FD                                    ;                     Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=FD
33B1:                     20                                    ;                     IF_NOT_JUMP address=33D2
33B2:                       0D 1E                               ;                       Command_0D_EXECUTE_LIST_WHILE_PASS size=30
33B4:                         04                                ;                         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
33B5:                           1A C7 DE 63 16 C9 97 43 5E 84 15 73;                           YOU MANAGE A GRAZING BLOW TO THE CHEST!
33C1:                           4A AB 98 89 4E D6 CE D6 9C DB 72 1F;                           .
33CD:                           54 F1 B9                        ;                           .
33D0:                         1D 14                             ;                         Command_1D_ATTACK_OBJECT damage=14
33D2:                     FF                                    ;                     Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=FF
33D3:                     18                                    ;                     IF_NOT_JUMP address=33EC
33D4:                       0D 16                               ;                       Command_0D_EXECUTE_LIST_WHILE_PASS size=22
33D6:                         04                                ;                         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
33D7:                           12 4E 45 DD C3 44 DB 89 8D 89 17 82;                           A LUCKY BLOW TO THE HEART! 
33E3:                           17 4A 5E 94 5F AB BB            ;                           .
33EA:                         1D FF                             ;                         Command_1D_ATTACK_OBJECT damage=FF
33EC:                 17                                        ;                 Command_09_COMPARE_OBJECT_TO_SECOND_NOUN object=17(Hands
33ED:                 34                                        ;                 IF_NOT_JUMP address=3422
33EE:                   0B 32                                   ;                   Command_0B_SWITCH size=32
33F0:                     05 AF                                 ;                     Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=AF
33F2:                     14                                    ;                     IF_NOT_JUMP address=3407
33F3:                       04                                  ;                       Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
33F4:                         12 59 45 3E 7A EF 16 1A 98 90 14 1B;                         A WILD PUNCH AND YOU MISS. 
3400:                         58 1B A1 D5 92 5B BB              ;                         .
3407:                     FF                                    ;                     Command_05_IS_LAST_RANDOM_LESS_THAN_OR_EQUAL value=FF
3408:                     19                                    ;                     IF_NOT_JUMP address=3422
3409:                       0D 17                               ;                       Command_0D_EXECUTE_LIST_WHILE_PASS size=23
340B:                         04                                ;                         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
340C:                           13 C7 DE EF 16 1A 98 F3 5F 8F 73 D0;                           YOU PUNCHED HIM IN THE HEAD!
3418:                           15 82 17 4A 5E 86 5F 21         ;                           .
3420:                         1D 03                             ;                         Command_1D_ATTACK_OBJECT damage=03
3422:             0D 0F                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=15
3424:               04                                          ;               Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3425:                 02 5F BE                                  ;                 THE
3428:               11                                          ;               Command_11_PRINT_FIRST_NOUN_SHORT_NAME
3429:               04                                          ;               Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
342A:                 08 4B 7B 92 C5 37 49 17 60                ;                 IS UNHARMED.
3433:       0A                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=0A phrase="0A: LOOK *      *          *       "
3434:       01                                                  ;       IF_NOT_JUMP address=3436
3435:         07                                                ;         Command_07_PRINT_ROOM_DESCRIPTION
3436:       15                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=15 phrase="15: EAT *       u.......   *       "
3437:       29                                                  ;       IF_NOT_JUMP address=3461
3438:         0E 27                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=39
343A:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
343B:           0D 24                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=36
343D:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
343E:               0D 80 5B F3 23 5B 4D 4E B8 F9 8E 82         ;               DON'T BE SILLY! THE
344A:               17 45                                       ;               .
344C:             11                                            ;             Command_11_PRINT_FIRST_NOUN_SHORT_NAME
344D:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
344E:               12 47 D2 C8 8B F3 23 55 BD DB BD 41         ;               WOULDN'T TASTE GOOD ANYWAY.
345A:               6E 03 58 99 9B 5F 4A                        ;               .
3461:       17                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=17 phrase="17: CLIMB *     u.......   *       "
3462:       51                                                  ;       IF_NOT_JUMP address=34B4
3463:         0E 4F                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=79
3465:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
3466:           0D 25                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=37
3468:             1A                                            ;             Command_1A_SET_VAR_OBJECT_TO_FIRST_NOUN
3469:             15 10                                         ;             Command_15_CHECK_OBJECT_BITS bits=10 ...P....
346B:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
346C:               0C 46 77 05 A0 16 BC 90 73 D6 83 DB         ;               I DON'T THINK THE 
3478:               72                                          ;               .
3479:             11                                            ;             Command_11_PRINT_FIRST_NOUN_SHORT_NAME
347A:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
347B:               11 4E D1 15 8A 50 BD 15 58 8E BE 08         ;               WILL STAND STILL FORTHAT.
3487:               8A BE A0 56 72 2E                           ;               .
348D:           0D 25                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=37
348F:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3490:               12 CF 62 8B 96 9B 64 1B A1 47 55 B3         ;               EVEN IF YOU COULD CLIMB THE
349C:               8B C3 54 A3 91 5F BE                        ;               .
34A3:             11                                            ;             Command_11_PRINT_FIRST_NOUN_SHORT_NAME
34A4:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
34A5:               0E 73 7B 47 D2 C8 8B F3 23 EE 72 1B         ;               IT WOULDN'T HELP YOU.
34B1:               A3 3F A1                                    ;               .
34B4:       16                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=16 phrase="16: DROP OUT    *          u...A..."
34B5:       16                                                  ;       IF_NOT_JUMP address=34CC
34B6:         0E 14                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=20
34B8:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
34B9:           0D 11                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=17
34BB:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
34BC:               02 5F BE                                    ;               THE
34BF:             11                                            ;             Command_11_PRINT_FIRST_NOUN_SHORT_NAME
34C0:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
34C1:               0A 4B 7B 06 9A BF 14 D3 B2 CF 98            ;               IS NOT BURNING.
34CC:       18                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=18 phrase="18: RUB *       u.......   *       "
34CD:       35                                                  ;       IF_NOT_JUMP address=3503
34CE:         0E 33                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=51
34D0:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
34D1:           0D 18                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=24
34D3:             1A                                            ;             Command_1A_SET_VAR_OBJECT_TO_FIRST_NOUN
34D4:             15 10                                         ;             Command_15_CHECK_OBJECT_BITS bits=10 ...P....
34D6:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
34D7:               11 5B BE 65 BC 99 16 F3 17 56 DB CA         ;               THAT'S NO WAY TO HURT THE
34E3:               9C 3E C6 82 17 45                           ;               .
34E9:             16                                            ;             Command_16_PRINT_VAR_NOUN_SHORT_NAME
34EA:             84                                            ;             CommonCommand_84
34EB:           0D 16                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=22
34ED:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
34EE:               02 5F BE                                    ;               THE
34F1:             11                                            ;             Command_11_PRINT_FIRST_NOUN_SHORT_NAME
34F2:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
34F3:               0F 81 8D CB 87 A5 94 04 71 8E 62 23         ;               LOOKS MUCH BETTER NOW.
34FF:               62 09 9A 2E                                 ;               .
3503:       0B                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=0B phrase="0B: LOOK AT     *          u......."
3504:       3A                                                  ;       IF_NOT_JUMP address=353F
3505:         0E 38                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=56
3507:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
3508:           0D 19                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=25
350A:             1A                                            ;             Command_1A_SET_VAR_OBJECT_TO_FIRST_NOUN
350B:             15 04                                         ;             Command_15_CHECK_OBJECT_BITS bits=04 .....X..
350D:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
350E:               12 3F B9 82 62 91 7A D5 15 04 18 8E         ;               SOMETHING IS WRITTEN ON THE
351A:               7B 83 61 03 A0 5F BE                        ;               .
3521:             16                                            ;             Command_16_PRINT_VAR_NOUN_SHORT_NAME
3522:             84                                            ;             CommonCommand_84
3523:           0D 1A                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=26
3525:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3526:               16 5F BE 5D B1 D0 B5 02 A1 91 7A 62         ;               THERE'S NOTHING SPECIAL ABOUT THE
3532:               17 DB 5F 33 48 B9 46 73 C6 5F BE            ;               .
353D:             11                                            ;             Command_11_PRINT_FIRST_NOUN_SHORT_NAME
353E:             84                                            ;             CommonCommand_84
353F:       0C                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=0C phrase="0C: LOOK UNDER  *          u......."
3540:       1A                                                  ;       IF_NOT_JUMP address=355B
3541:         0E 18                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=24
3543:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
3544:           0D 15                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=21
3546:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3547:               11 5F BE 5D B1 D0 B5 02 A1 91 7A B0         ;               THERE'S NOTHING UNDER THE
3553:               17 F4 59 82 17 45                           ;               .
3559:             11                                            ;             Command_11_PRINT_FIRST_NOUN_SHORT_NAME
355A:             84                                            ;             CommonCommand_84
355B:       10                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=10 phrase="10: LOOK IN     *          u......."
355C:       18                                                  ;       IF_NOT_JUMP address=3575
355D:         0E 16                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=22
355F:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
3560:           0D 13                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=19
3562:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3563:               0F 5F BE 5D B1 D0 B5 02 A1 91 7A D0         ;               THERE'S NOTHING IN THE
356F:               15 82 17 45                                 ;               .
3573:             11                                            ;             Command_11_PRINT_FIRST_NOUN_SHORT_NAME
3574:             84                                            ;             CommonCommand_84
3575:       1B                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=1B phrase="1B: LOOK AROUND *          u......."
3576:       20                                                  ;       IF_NOT_JUMP address=3597
3577:         0E 1E                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=30
3579:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
357A:           0D 03                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=3
357C:             08 00                                         ;             Command_08_COMPARE_OBJECT_TO_FIRST_NOUN object=00(NONE
357E:             07                                            ;             Command_07_PRINT_ROOM_DESCRIPTION
357F:           0D 16                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=22
3581:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3582:               12 5F BE 5B B1 4B 7B 06 9A 90 73 C3         ;               THERE IS NOTHING AROUND THE
358E:               6A 07 B3 33 98 5F BE                        ;               .
3595:             11                                            ;             Command_11_PRINT_FIRST_NOUN_SHORT_NAME
3596:             84                                            ;             CommonCommand_84
3597:       1C                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=1C phrase="1C: LOOK BEHIND *          u......."
3598:       34                                                  ;       IF_NOT_JUMP address=35CD
3599:         0E 32                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=50
359B:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
359C:           0D 17                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=23
359E:             08 00                                         ;             Command_08_COMPARE_OBJECT_TO_FIRST_NOUN object=00(NONE
35A0:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
35A1:               13 5F BE 5B B1 4B 7B 06 9A 90 73 C4         ;               THERE IS NOTHING BEHIND YOU.
35AD:               6A A3 60 33 98 C7 DE 2E                     ;               .
35B5:           0D 16                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=22
35B7:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
35B8:               12 5F BE 5B B1 4B 7B 06 9A 90 73 C4         ;               THERE IS NOTHING BEHIND THE
35C4:               6A A3 60 33 98 5F BE                        ;               .
35CB:             11                                            ;             Command_11_PRINT_FIRST_NOUN_SHORT_NAME
35CC:             84                                            ;             CommonCommand_84
35CD:       21                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=21 phrase="21: PLUGH *     *          *       "
35CE:       0A                                                  ;       IF_NOT_JUMP address=35D9
35CF:         04                                                ;         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
35D0:           08 B5 6C 8E C5 EB 72 AB BB                      ;           GESUNDHEIT! 
35D9:       22                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=22 phrase="22: SCREAM *    *          *       "
35DA:       12                                                  ;       IF_NOT_JUMP address=35ED
35DB:         04                                                ;         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
35DC:           10 5B E0 27 60 31 60 41 A0 49 A0 89             ;           YYYEEEEEOOOOOOWWWWWWWW!!
35E8:           D3 89 D3 69 CE                                  ;           .
35ED:       23                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=23 phrase="23: QUIT *      *          *       "
35EE:       05                                                  ;       IF_NOT_JUMP address=35F4
35EF:         0D 03                                             ;         Command_0D_EXECUTE_LIST_WHILE_PASS size=3
35F1:           92                                              ;           CommonCommand_92
35F2:           26                                              ;           Command_26_PRINT_SCORE
35F3:           24                                              ;           Command_24_ENDLESS_LOOP
35F4:       2C                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=2C phrase="2C: SCORE *     *          *       "
35F5:       04                                                  ;       IF_NOT_JUMP address=35FA
35F6:         0D 02                                             ;         Command_0D_EXECUTE_LIST_WHILE_PASS size=2
35F8:           92                                              ;           CommonCommand_92
35F9:           26                                              ;           Command_26_PRINT_SCORE
35FA:       3E                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=3E phrase="??"
35FB:       01                                                  ;       IF_NOT_JUMP address=35FD
35FC:         27                                                ;         Command_27_??_UNKNOWN_COMMAND_??
35FD:       3F                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=3F phrase="??"
35FE:       01                                                  ;       IF_NOT_JUMP address=3600
35FF:         28                                                ;         Command_28_??_UNKNOWN_COMMAND_??
3600:       25                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=25 phrase="25: LEAVE *     *          *       "
3601:       0D                                                  ;       IF_NOT_JUMP address=360F
3602:         04                                                ;         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3603:           0B 03 C0 7B 14 94 5A E6 5F C0 7A 2E             ;           TRY A DIRECTION.
360F:       26                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=26 phrase="26: GO AROUND   *          u......."
3610:       24                                                  ;       IF_NOT_JUMP address=3635
3611:         0E 22                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=34
3613:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
3614:           0D 17                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=23
3616:             1A                                            ;             Command_1A_SET_VAR_OBJECT_TO_FIRST_NOUN
3617:             15 10                                         ;             Command_15_CHECK_OBJECT_BITS bits=10 ...P....
3619:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
361A:               02 5F BE                                    ;               THE
361D:             11                                            ;             Command_11_PRINT_FIRST_NOUN_SHORT_NAME
361E:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
361F:               0D 40 D2 F3 23 F6 8B 51 18 52 C2 65         ;               WON'T LET YOU PASS!
362B:               49 21                                       ;               .
362D:           04                                              ;           Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
362E:             06 09 9A FA 17 70 49                          ;             NOW WHAT?
3635:       3D                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=3D phrase="3D: GO TO       *          u......."
3636:       01                                                  ;       IF_NOT_JUMP address=3638
3637:         94                                                ;         CommonCommand_94
3638:       27                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=27 phrase="27: KICK *      u.......   *       "
3639:       0E                                                  ;       IF_NOT_JUMP address=3648
363A:         0E 0C                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=12
363C:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
363D:           04                                              ;           Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
363E:             09 25 A1 AB 70 3B 95 77 BF 21                 ;             OUCH! MY TOE!
3648:       28                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=28 phrase="28: FEED WITH   ...P....   u......."
3649:       0A                                                  ;       IF_NOT_JUMP address=3654
364A:         0E 08                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=8
364C:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
364D:           0D 04                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=4
364F:             1A                                            ;             Command_1A_SET_VAR_OBJECT_TO_FIRST_NOUN
3650:             15 10                                         ;             Command_15_CHECK_OBJECT_BITS bits=10 ...P....
3652:             96                                            ;             CommonCommand_96
3653:           97                                              ;           CommonCommand_97
3654:       29                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=29 phrase="29: FEED TO     u.......   ...P...."
3655:       0A                                                  ;       IF_NOT_JUMP address=3660
3656:         0E 08                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=8
3658:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
3659:           0D 04                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=4
365B:             1B                                            ;             Command_1B_SET_VAR_OBJECT_TO_SECOND_NOUN
365C:             15 10                                         ;             Command_15_CHECK_OBJECT_BITS bits=10 ...P....
365E:             96                                            ;             CommonCommand_96
365F:           97                                              ;           CommonCommand_97
3660:       2F                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=2F phrase="2F: WAIT *      *          *       "
3661:       07                                                  ;       IF_NOT_JUMP address=3669
3662:         04                                                ;         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3663:           05 9B 29 57 C6 3E                               ;           <PAUSE>
3669:       2D                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=2D phrase="2D: PULL UP     *          u......."
366A:       09                                                  ;       IF_NOT_JUMP address=3674
366B:         0E 07                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=7
366D:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
366E:           0D 02                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=2
3670:             1A                                            ;             Command_1A_SET_VAR_OBJECT_TO_FIRST_NOUN
3671:             83                                            ;             CommonCommand_83
3672:           14                                              ;           Command_14_EXECUTE_COMMAND_REVERSE_STATUS
3673:             0C                                            ;             Command_0C_FAIL
3674:       33                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=33 phrase="??"
3675:       04                                                  ;       IF_NOT_JUMP address=367A
3676:         0E 02                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=2
3678:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
3679:           98                                              ;           CommonCommand_98
367A:       34                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=34 phrase="34: JUMP OVER   *          u......."
367B:       04                                                  ;       IF_NOT_JUMP address=3680
367C:         0E 02                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=2
367E:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
367F:           98                                              ;           CommonCommand_98
3680:       36                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=36 phrase="36: CLIMB IN    *          *       "
3681:       17                                                  ;       IF_NOT_JUMP address=3699
3682:         0E 15                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=21
3684:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
3685:           0D 12                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=18
3687:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3688:               0E C7 DE D3 14 E6 96 77 15 0B BC 96         ;               YOU CAN'T GET IN THE 
3694:               96 DB 72                                    ;               .
3697:             11                                            ;             Command_11_PRINT_FIRST_NOUN_SHORT_NAME
3698:             84                                            ;             CommonCommand_84
3699:       37                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=37 phrase="37: CLIMB OUT   *          *       "
369A:       15                                                  ;       IF_NOT_JUMP address=36B0
369B:         0E 13                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=19
369D:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
369E:           0D 10                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=16
36A0:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
36A1:               0C C7 DE 94 14 85 61 0B BC 96 96 DB         ;               YOU AREN'T IN THE 
36AD:               72                                          ;               .
36AE:             11                                            ;             Command_11_PRINT_FIRST_NOUN_SHORT_NAME
36AF:             84                                            ;             CommonCommand_84
36B0:       38                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=38 phrase="38: CLIMB UNDER *          u......."
36B1:       20                                                  ;       IF_NOT_JUMP address=36D2
36B2:         0E 1E                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=30
36B4:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
36B5:           0D 1B                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=27
36B7:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
36B8:               17 5F BE 5B B1 4B 7B 06 9A 30 15 29         ;               THERE IS NOT ENOUGH ROOM UNDER THE
36C4:               A1 14 71 3F A0 B0 17 F4 59 82 17 45         ;               .
36D0:             11                                            ;             Command_11_PRINT_FIRST_NOUN_SHORT_NAME
36D1:             84                                            ;             CommonCommand_84
36D2:       39                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=39 phrase="39: THROW IN    u.......   u......."
36D3:       1D                                                  ;       IF_NOT_JUMP address=36F1
36D4:         0E 1B                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=27
36D6:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
36D7:           0D 18                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=24
36D9:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
36DA:               16 C7 DE FB 17 F3 8C 58 72 56 5E D2         ;               YOU WILL HAVE TO PUT IT IN THERE.
36E6:               9C 73 C6 73 7B 83 7A 5F BE 7F B1            ;               .
36F1:       3A                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=3A phrase="3A: OPEN WITH   u.......   u......."
36F2:       1E                                                  ;       IF_NOT_JUMP address=3711
36F3:         0E 1C                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=28
36F5:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
36F6:           0D 19                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=25
36F8:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
36F9:               0C C7 DE D3 14 E6 96 C2 16 83 61 5F         ;               YOU CAN'T OPEN THE
3705:               BE                                          ;               .
3706:             11                                            ;             Command_11_PRINT_FIRST_NOUN_SHORT_NAME
3707:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3708:               06 56 D1 16 71 DB 72                        ;               WITH THE 
370F:             12                                            ;             Command_12_PRINT_SECOND_NOUN_SHORT_NAME
3710:             84                                            ;             CommonCommand_84
3711:       0D                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=0D phrase="0D: THROW AT    .v......   ...P...."
3712:       34                                                  ;       IF_NOT_JUMP address=3747
3713:         0E 32                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=50
3715:           0D 2E                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=46
3717:             1A                                            ;             Command_1A_SET_VAR_OBJECT_TO_FIRST_NOUN
3718:             83                                            ;             CommonCommand_83
3719:             0E 2A                                         ;             Command_0E_EXECUTE_LIST_WHILE_FAIL size=42
371B:               0D 27                                       ;               Command_0D_EXECUTE_LIST_WHILE_PASS size=39
371D:                 0E 07                                     ;                 Command_0E_EXECUTE_LIST_WHILE_FAIL size=7
371F:                   14                                      ;                   Command_14_EXECUTE_COMMAND_REVERSE_STATUS
3720:                     15 10                                 ;                     Command_15_CHECK_OBJECT_BITS bits=10 ...P....
3722:                   1B                                      ;                   Command_1B_SET_VAR_OBJECT_TO_SECOND_NOUN
3723:                   14                                      ;                   Command_14_EXECUTE_COMMAND_REVERSE_STATUS
3724:                     15 40                                 ;                     Command_15_CHECK_OBJECT_BITS bits=40 .v......
3726:                 04                                        ;                 Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3727:                   02 5F BE                                ;                   THE
372A:                 11                                        ;                 Command_11_PRINT_FIRST_NOUN_SHORT_NAME
372B:                 04                                        ;                 Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
372C:                   14 07 4F 17 98 CA B5 37 49 F5 8B D3     ;                   BOUNCES HARMLESSLY OFF OF THE 
3738:                   B8 B8 16 91 64 96 64 DB 72              ;                   .
3741:                 12                                        ;                 Command_12_PRINT_SECOND_NOUN_SHORT_NAME
3742:                 84                                        ;                 CommonCommand_84
3743:                 10                                        ;                 Command_10_DROP_OBJECT
3744:               13                                          ;               Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
3745:           14                                              ;           Command_14_EXECUTE_COMMAND_REVERSE_STATUS
3746:             0C                                            ;             Command_0C_FAIL
3747:       0E                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=0E phrase="0E: THROW TO    u.......   ...P...."
3748:       39                                                  ;       IF_NOT_JUMP address=3782
3749:         0E 37                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=55
374B:           0D 1B                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=27
374D:             1B                                            ;             Command_1B_SET_VAR_OBJECT_TO_SECOND_NOUN
374E:             14                                            ;             Command_14_EXECUTE_COMMAND_REVERSE_STATUS
374F:               15 10                                       ;               Command_15_CHECK_OBJECT_BITS bits=10 ...P....
3751:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3752:               02 5F BE                                    ;               THE
3755:             12                                            ;             Command_12_PRINT_SECOND_NOUN_SHORT_NAME
3756:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3757:               10 4B 7B 06 9A 85 14 B2 53 90 BE C9         ;               IS NOT ACCEPTING GIFTS. 
3763:               6A 5E 79 5B BB                              ;               .
3768:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
3769:           0D 17                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=23
376B:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
376C:               02 5F BE                                    ;               THE
376F:             12                                            ;             Command_12_PRINT_SECOND_NOUN_SHORT_NAME
3770:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3771:               10 60 7B F3 23 D5 46 EE 61 91 7A BC         ;               ISN'T ACCEPTING BRIBES. 
377D:               14 AF 78 5B BB                              ;               .
3782:       0F                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=0F phrase="0F: DROP IN     u.......   u......."
3783:       19                                                  ;       IF_NOT_JUMP address=379D
3784:         0E 17                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=23
3786:           13                                              ;           Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
3787:           0D 14                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=20
3789:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
378A:               02 5F BE                                    ;               THE
378D:             11                                            ;             Command_11_PRINT_FIRST_NOUN_SHORT_NAME
378E:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
378F:               0B 40 D2 F3 23 16 67 D0 15 82 17 45         ;               WON'T FIT IN THE
379B:             12                                            ;             Command_12_PRINT_SECOND_NOUN_SHORT_NAME
379C:             84                                            ;             CommonCommand_84
379D:       14                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=14 phrase="14: LIGHT WITH  u...A...   u...A..."
379E:       3B                                                  ;       IF_NOT_JUMP address=37DA
379F:         0D 39                                             ;         Command_0D_EXECUTE_LIST_WHILE_PASS size=57
37A1:           1B                                              ;           Command_1B_SET_VAR_OBJECT_TO_SECOND_NOUN
37A2:           83                                              ;           CommonCommand_83
37A3:           0E 35                                           ;           Command_0E_EXECUTE_LIST_WHILE_FAIL size=53
37A5:             0D 18                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=24
37A7:               1A                                          ;               Command_1A_SET_VAR_OBJECT_TO_FIRST_NOUN
37A8:               15 08                                       ;               Command_15_CHECK_OBJECT_BITS bits=08 ....A...
37AA:               0E 04                                       ;               Command_0E_EXECUTE_LIST_WHILE_FAIL size=4
37AC:                 09 12                                     ;                 Command_09_COMPARE_OBJECT_TO_SECOND_NOUN object=12(LitCandle
37AE:                 09 14                                     ;                 Command_09_COMPARE_OBJECT_TO_SECOND_NOUN object=14(LitLamp
37B0:               0E 0D                                       ;               Command_0E_EXECUTE_LIST_WHILE_FAIL size=13
37B2:                 13                                        ;                 Command_13_PROCESS_PHRASE_BY_ROOM_OR_FIRST_OR_SECOND
37B3:                 04                                        ;                 Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
37B4:                   0A 73 7B 40 D2 F3 23 F4 4F 1B 9C        ;                   IT WON'T BURN. 
37BF:             0D 19                                         ;             Command_0D_EXECUTE_LIST_WHILE_PASS size=25
37C1:               04                                          ;               Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
37C2:                 0C C7 DE D3 14 E6 96 BF 14 C3 B2 5F       ;                 YOU CAN'T BURN THE
37CE:                 BE                                        ;                 .
37CF:               11                                          ;               Command_11_PRINT_FIRST_NOUN_SHORT_NAME
37D0:               04                                          ;               Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
37D1:                 06 56 D1 16 71 DB 72                      ;                 WITH THE 
37D8:               12                                          ;               Command_12_PRINT_SECOND_NOUN_SHORT_NAME
37D9:               84                                          ;               CommonCommand_84
37DA:       07                                                  ;       Command_0A_COMPARE_TO_PHRASE_FORM val=07 phrase="07: INVENT *    *          *       "
37DB:       1A                                                  ;       IF_NOT_JUMP address=37F6
37DC:         0D 18                                             ;         Command_0D_EXECUTE_LIST_WHILE_PASS size=24
37DE:           04                                              ;           Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
37DF:             15 C7 DE 94 14 45 5E 3C 49 D0 DD D6           ;             YOU ARE CARRYING THE FOLLOWING:
37EB:             6A DB 72 FE 67 89 8D 91 7A 3A                 ;             .
37F5:           06                                              ;           Command_06_PRINT_INVENTORY
37F6:     04                                                    ;     Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
37F7:       02 00 00                                            ;       ???
; ENDOF 323C
```

# Helper Commands

```code
HelperCommands: 
37FA: 00 84 2C                                                  ; Script list size=042C
37FD:   81 63                                                   ;   Script number=81 size=042C
37FF:       0D 61                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=97
3801:         1F                                                ;         Command_1F_PRINT_MESSAGE
3802:           10 C7 DE AF 23 FF 14 17 47 8C 17 43             ;           YOU'RE DEAD. TRY AGAIN. 
380E:           DB 0B 6C 1B 9C                                  ;           .
3813:         95                                                ;         CommonCommand_95
3814:         17 01 81                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=01(Object1) location=81
3817:         17 05 84                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=05(Food) location=84
381A:         17 06 88                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=06(StatueEast) location=88
381D:         17 07 00                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=07(StatueWest) location=00
3820:         17 08 8C                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=08(GoldRing) location=8C
3823:         17 09 A1                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=09(Sword) location=A1
3826:         17 0A 8E                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=0A(StoneGargoyle) location=8E
3829:         17 0C 95                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=0C(Idol) location=95
382C:         17 0E 91                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=0E(UnpulledLever) location=91
382F:         17 0F 00                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=0F(PulledLever) location=00
3832:         17 11 92                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=11(UnlitCandle) location=92
3835:         17 12 00                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=12(LitCandle) location=00
3838:         17 14 A0                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=14(LitLamp) location=A0
383B:         17 15 00                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=15(LiveSerpent) location=00
383E:         17 16 00                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=16(DeadSerpent) location=00
3841:         17 18 9C                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=18(Coin) location=9C
3844:         17 1E 00                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=1E(LiveGargoyle) location=00
3847:         17 1F 00                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=1F(DeadGargoyle) location=00
384A:         17 22 8F                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=22(GoldenChopstick) location=8F
384D:         17 25 9C                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=25(GemA) location=9C
3850:         17 26 00                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=26(GemB) location=00
3853:         17 28 00                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=28(UnlitLamp) location=00
3856:         1C 15                                             ;         Command_1C_SET_VAR_OBJECT object=15 (LiveSerpent)
3858:         23 3C                                             ;         Command_23_HEAL_VAR_OBJECT value=3C
385A:         1C 1D                                             ;         Command_1C_SET_VAR_OBJECT object=1D (USER)
385C:         23 46                                             ;         Command_23_HEAL_VAR_OBJECT value=46
385E:         17 1D 96                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=1D(USER) location=96
3861:         25                                                ;         Command_25_RESTART_GAME
3862:   82 2C                                                   ;   Script number=82 size=042C
3864:       0D 2A                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=42
3866:         1F                                                ;         Command_1F_PRINT_MESSAGE
3867:           27 5F BE 66 17 8F 49 54 5E 3F 61 57             ;           THE STATUE RELEASES THE ARROW WHICH
3873:           49 D6 B5 DB 72 3C 49 6B A1 23 D1 13             ;           PENETRATES YOUR HEART.
387F:           54 F0 A4 8C 62 7F 49 DB B5 34 A1 9F             ;           .
388B:           15 3E 49 2E                                     ;           .
388F:         81                                                ;         CommonCommand_81
3890:   83 66                                                   ;   Script number=83 size=042C
3892:       0D 64                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=100
3894:         0E 61                                             ;         Command_0E_EXECUTE_LIST_WHILE_FAIL size=97
3896:           0D 08                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=8
3898:             08 0E                                         ;             Command_08_COMPARE_OBJECT_TO_FIRST_NOUN object=0E(UnpulledLever
389A:             17 0E 00                                      ;             Command_17_MOVE_OBJECT_TO_LOCATION object=0E(UnpulledLever) location=00
389D:             1C 0F                                         ;             Command_1C_SET_VAR_OBJECT object=0F (PulledLever)
389F:             0C                                            ;             Command_0C_FAIL
38A0:           0D 08                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=8
38A2:             08 25                                         ;             Command_08_COMPARE_OBJECT_TO_FIRST_NOUN object=25(GemA
38A4:             17 25 00                                      ;             Command_17_MOVE_OBJECT_TO_LOCATION object=25(GemA) location=00
38A7:             1C 26                                         ;             Command_1C_SET_VAR_OBJECT object=26 (GemB)
38A9:             0C                                            ;             Command_0C_FAIL
38AA:           0D 1D                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=29
38AC:             15 10                                         ;             Command_15_CHECK_OBJECT_BITS bits=10 ...P....
38AE:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
38AF:               0C 46 77 05 A0 16 BC 90 73 D6 83 DB         ;               I DON'T THINK THE 
38BB:               72                                          ;               .
38BC:             16                                            ;             Command_16_PRINT_VAR_NOUN_SHORT_NAME
38BD:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
38BE:               0A 4E D1 05 8A 42 A0 2B 62 FF BD            ;               WILL COOPERATE.
38C9:           0D 21                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=33
38CB:             14                                            ;             Command_14_EXECUTE_COMMAND_REVERSE_STATUS
38CC:               15 20                                       ;               Command_15_CHECK_OBJECT_BITS bits=20 ..C.....
38CE:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
38CF:               1A C7 DE 94 14 53 5E D6 C4 4B 5E 13         ;               YOU ARE QUITE INCAPABLE OF REMOVING THE
38DB:               98 44 A4 DB 8B C3 9E 6F B1 53 A1 AB         ;               .
38E7:               98 5F BE                                    ;               .
38EA:             16                                            ;             Command_16_PRINT_VAR_NOUN_SHORT_NAME
38EB:             84                                            ;             CommonCommand_84
38EC:           18                                              ;           Command_18_CHECK_VAR_OBJECT_OWNED_BY_ACTIVE_OBJECT
38ED:           0D 08                                           ;           Command_0D_EXECUTE_LIST_WHILE_PASS size=8
38EF:             0F                                            ;             Command_0F_PICK_UP_OBJECT
38F0:             16                                            ;             Command_16_PRINT_VAR_NOUN_SHORT_NAME
38F1:             04                                            ;             Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
38F2:               04 4D BD A7 61                              ;               TAKEN.
38F7:         18                                                ;         Command_18_CHECK_VAR_OBJECT_OWNED_BY_ACTIVE_OBJECT
38F8:   84 04                                                   ;   Script number=84 size=042C
38FA:       04                                                  ;       Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
38FB:         02 3B F4                                          ;         .  
38FE:   85 29                                                   ;   Script number=85 size=042C
3900:       1F                                                  ;       Command_1F_PRINT_MESSAGE
3901:         27 49 45 07 B3 11 A3 89 64 94 C3 0B               ;         A GROUP OF GUARDS MARCHES AROUND THE CORNER
390D:         5C 94 91 1F 54 C3 B5 07 B3 33 98 5F               ;         TO YOUR RIGHT.
3919:         BE E1 14 CF B2 96 AF DB 9C 34 A1 33               ;         .
3925:         17 2E 6D 2E                                       ;         .
3929:   87 2A                                                   ;   Script number=87 size=042C
392B:       1F                                                  ;       Command_1F_PRINT_MESSAGE
392C:         28 49 45 07 B3 11 A3 89 64 94 C3 0B               ;         A GROUP OF GUARDS DISAPPEARS AROUND THE
3938:         5C 95 5A EA 48 94 5F C3 B5 07 B3 33               ;         CORNER TO YOUR LEFT.
3944:         98 5F BE E1 14 CF B2 96 AF DB 9C 34               ;         .
3950:         A1 3F 16 D7 68                                    ;         .
3955:   86 1E                                                   ;   Script number=86 size=042C
3957:       1F                                                  ;       Command_1F_PRINT_MESSAGE
3958:         1C 49 45 07 B3 11 A3 89 64 94 C3 0B               ;         A GROUP OF GUARDS COMES AROUND THE CORNER.
3964:         5C 3F 55 4B 62 39 49 8E C5 82 17 45               ;         .
3970:         5E B8 A0 47 62                                    ;         .
3975:   88 13                                                   ;   Script number=88 size=042C
3977:       0D 11                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=17
3979:         04                                                ;         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
397A:           02 5F BE                                        ;           THE
397D:         12                                                ;         Command_12_PRINT_SECOND_NOUN_SHORT_NAME
397E:         04                                                ;         Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
397F:           0A 4B 7B 06 9A BF 14 10 B2 5B 70                ;           IS NOT BURING. 
398A:   92 1C                                                   ;   Script number=92 size=042C
398C:       1F                                                  ;       Command_1F_PRINT_MESSAGE
398D:         1A 36 A1 B8 16 7B 14 85 A6 44 B8 DB               ;         OUT OF A POSSIBLE FIFTY, YOUR SCORE IS 
3999:         8B 08 67 1E C1 51 18 23 C6 61 B7 5B               ;         .
39A5:         B1 4B 7B                                          ;         .
39A8:   89 12                                                   ;   Script number=89 size=042C
39AA:       1F                                                  ;       Command_1F_PRINT_MESSAGE
39AB:         10 C7 DE D3 14 E6 96 FF 15 D3 93 5B               ;         YOU CAN'T JUMP THAT FAR!
39B7:         BE 08 BC 21 49                                    ;         .
39BC:   8A 32                                                   ;   Script number=8A size=042C
39BE:       0D 30                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=48
39C0:         1F                                                ;         Command_1F_PRINT_MESSAGE
39C1:           2D C7 DE 3B 16 33 98 03 A0 55 45 8D             ;           YOU LAND ON A SPIKE AT THE BOTTOM OF THE PIT
39CD:           A5 43 5E 16 BC DB 72 06 4F 7F BF B8             ;           WHICH THE RUG COVERED.
39D9:           16 82 17 52 5E 73 7B 23 D1 13 54 5F             ;           .
39E5:           BE 3F 17 C5 6A 4F A1 66 B1 2E                   ;           .
39EF:         81                                                ;         CommonCommand_81
39F0:   8B 79                                                   ;   Script number=8B size=042C
39F2:       0D 77                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=119
39F4:         1F                                                ;         Command_1F_PRINT_MESSAGE
39F5:           74 C7 DE 2F 17 43 48 5B E3 23 D1 DB             ;           YOU REALIZE WHILE YOU'RE FALLING THAT THE
3A01:           8B C7 DE AF 23 4B 15 03 8D AB 98 5B             ;           RUG COVERED A PIT. THE BOTTOM OF THE PIT IS
3A0D:           BE 16 BC DB 72 E9 B3 E1 14 74 CA F3             ;           COVERED WITH SPIKES ABOUT FOUR FEET TALL -
3A19:           5F 52 45 97 7B 82 17 44 5E 0E A1 DB             ;           YOU DON'T HAVE TIME TO MEASURE THEM EXACTLY.
3A25:           9F C3 9E 5F BE E3 16 0B BC C5 B5 4F             ;           
3A31:           A1 66 B1 FB 17 53 BE 63 B9 B5 85 84             ;           .
3A3D:           14 36 A1 59 15 23 C6 67 66 16 BC 46             ;           .
3A49:           48 8B 18 C7 DE 09 15 E6 96 9B 15 5B             ;           .
3A55:           CA 8F BE 56 5E CF 9C 95 5F 2F C6 82             ;           .
3A61:           17 5B 61 1B 63 06 56 DB E0                      ;           .
3A6A:         81                                                ;         CommonCommand_81
3A6B:   8C 49                                                   ;   Script number=8C size=042C
3A6D:       1F                                                  ;       Command_1F_PRINT_MESSAGE
3A6E:         47 C7 DE 03 15 61 B7 74 CA 7B 14 E7               ;         YOU DISCOVER A DEEP DARK PIT WHICH EXTENDS
3A7A:         59 06 A3 35 49 E3 16 19 BC 85 73 07               ;         FROM THE NORTH TO THE SOUTH WALL. THE PIT IS
3A86:         71 3F D9 4D 98 5C 15 DB 9F 5F BE 99               ;         TOO BROAD TO JUMP.
3A92:         16 C2 B3 89 17 82 17 55 5E 36 A1 19               ;         .
3A9E:         71 46 48 56 F4 DB 72 96 A5 D5 15 89               ;         .
3AAA:         17 C4 9C F3 B2 16 58 CC 9C 72 C5 2E               ;         .
3AB6:   8D 20                                                   ;   Script number=8D size=042C
3AB8:       04                                                  ;       Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3AB9:         1E 5F BE 66 17 8F 49 4B 5E CF B5 DA               ;         THE STATUE IS MUCH TOO HEAVY FOR YOU TO
3AC5:         C3 89 17 CA 9C 98 5F 48 DB A3 A0 C7               ;         MOVE.
3AD1:         DE 89 17 71 16 7F CA                              ;         .
3AD8:   8E 3E                                                   ;   Script number=8E size=042C
3ADA:       04                                                  ;       Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3ADB:         3C 7A C4 D9 06 82 7B 84 15 96 5F 03               ;         UGH! WITH GREAT DIFFICULTY YOU MANAGE TO
3AE7:         15 93 66 2E 56 FB C0 C7 DE 63 16 C9               ;         MOVE THE ALTAR AND YOU DISCOVER A SECRET
3AF3:         97 56 5E CF 9C 4F A1 82 17 43 5E 3B               ;         PASSAGE.
3AFF:         8E 83 AF 33 98 C7 DE 03 15 61 B7 74               ;         .
3B0B:         CA 7B 14 A5 B7 76 B1 DB 16 D3 B9 BF               ;         .
3B17:         6C                                                ;         .
3B18:   8F 07                                                   ;   Script number=8F size=042C
3B1A:       0D 05                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=5
3B1C:         08 2B                                             ;         Command_08_COMPARE_OBJECT_TO_FIRST_NOUN object=2B(Passage
3B1E:         00 A5                                             ;         Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=A5
3B20:         90                                                ;         CommonCommand_90
3B21:   90 22                                                   ;   Script number=90 size=042C
3B23:       1F                                                  ;       Command_1F_PRINT_MESSAGE
3B24:         20 5F BE 8E 14 54 BD 71 16 75 CA AB               ;         THE ALTAR MOVES BACK TO SEAL THE HOLE ABOVE
3B30:         14 8B 54 6B BF A3 B7 16 8A DB 72 7E               ;         YOU.
3B3C:         74 43 5E 08 4F 5B 5E 3F A1                        ;         .
3B45:   91 37                                                   ;   Script number=91 size=042C
3B47:       0D 35                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=53
3B49:         1F                                                ;         Command_1F_PRINT_MESSAGE
3B4A:           30 4B 49 C7 DE DE 14 64 7A C7 16 11             ;           AS YOU CLIMB OUT OF THE HOLE, IT SEEMS TO
3B56:           BC 96 64 DB 72 7E 74 B3 63 73 7B A7             ;           MAGICALLY SEAL UP BEHIND YOU. 
3B62:           B7 4B 94 6B BF 89 91 D3 78 13 8D 57             ;           .
3B6E:           17 33 48 D3 C5 6A 4D 8E 7A 51 18 DB             ;           .
3B7A:           C7                                              ;           .
3B7B:         00 9F                                             ;         Command_00_MOVE_ACTIVE_OBJECT_TO_ROOM_AND_LOOK room=9F
3B7D:         95                                                ;         CommonCommand_95
3B7E:   93 09                                                   ;   Script number=93 size=042C
3B80:       0B 07                                               ;       Command_0B_SWITCH size=07
3B82:         0A 36                                             ;         Command_0A_COMPARE_TO_PHRASE_FORM val=36 phrase="36: CLIMB IN    *          *       "
3B84:         01                                                ;         IF_NOT_JUMP address=3B86
3B85:           94                                              ;           CommonCommand_94
3B86:         37                                                ;         Command_0A_COMPARE_TO_PHRASE_FORM val=37 phrase="37: CLIMB OUT   *          *       "
3B87:         01                                                ;         IF_NOT_JUMP address=3B89
3B88:           94                                              ;           CommonCommand_94
3B89:   94 19                                                   ;   Script number=94 size=042C
3B8B:       1F                                                  ;       Command_1F_PRINT_MESSAGE
3B8C:         17 FF A5 57 49 B5 17 46 5E 2F 7B 03               ;         PLEASE USE DIRECTIONS N,S,E, OR W.
3B98:         56 1D A0 A6 16 3F BB 11 EE 99 AF 2E               ;         .
3BA4:   95 26                                                   ;   Script number=95 size=042C
3BA6:       0D 24                                               ;       Command_0D_EXECUTE_LIST_WHILE_PASS size=36
3BA8:         17 36 FF                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=36(Jungle) location=FF
3BAB:         17 29 00                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=29(Floor) location=00
3BAE:         17 2A 00                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=2A(Exit) location=00
3BB1:         17 2B 00                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=2B(Passage) location=00
3BB4:         17 2C 00                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=2C(Hole) location=00
3BB7:         17 2D 00                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=2D(Corridor) location=00
3BBA:         17 2E 00                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=2E(Corner) location=00
3BBD:         17 31 00                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=31(Hallway) location=00
3BC0:         17 34 00                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=34(Entrance) location=00
3BC3:         17 35 00                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=35(Tunnel) location=00
3BC6:         17 3A 00                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=3A(Ceiling) location=00
3BC9:         17 3C 1D                                          ;         Command_17_MOVE_OBJECT_TO_LOCATION object=3C(Object3C) location=1D
3BCC:   96 1A                                                   ;   Script number=96 size=042C
3BCE:       04                                                  ;       Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3BCF:         18 5B BE 65 BC 7B 14 41 6E 19 58 3B               ;         THAT'S A GOOD WAY TO LOSE YOUR HAND!
3BDB:         4A 6B BF 85 8D 5B 5E 34 A1 9B 15 31               ;         .
3BE7:         98                                                ;         .
3BE8:   97 19                                                   ;   Script number=97 size=042C
3BEA:       04                                                  ;       Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3BEB:         17 43 79 C7 DE D3 14 88 96 8E 7A 7B               ;         IF YOU CAN FIND A MOUTH, I'M GAME!
3BF7:         14 C7 93 76 BE BD 15 49 90 67 48 21               ;         .
3C03:   98 24                                                   ;   Script number=98 size=042C
3C05:       04                                                  ;       Command_04_PRINT_SYSTEM_OR_PLAYER_MESSAGE
3C06:         22 0F A0 5F 17 46 48 66 17 D3 61 04               ;         ONE SMALL STEP FOR MANKIND, ONE GIANT LEAP
3C12:         68 63 16 5B 99 56 98 C0 16 49 5E 90               ;         FOR YOU!
3C1E:         78 0E BC 92 5F 59 15 9B AF 19 A1                  ;         .
; ENDOF 37FA
```

# Input Word tables

```code
InputWordTables:
; --- IGNORES --- Maybe for curse words. No words in this list and thus never used.
3C29: 00                
;  
; --- VERBS ---   
3C2A: 04 52 45 41 44 01         ; READ     1
3C30: 03 47 45 54 09            ; GET      9
3C35: 05 54 48 52 4F 57 03      ; THROW    3
3C3C: 06 41 54 54 41 43 4B 04   ; ATTACK   4
3C44: 04 4B 49 4C 4C 04         ; KILL     4
3C4A: 03 48 49 54 04            ; HIT      4
3C4F: 05 4E 4F 52 54 48 05      ; NORTH    5
3C56: 01 4E 05                  ; N        5
3C59: 05 53 4F 55 54 48 06      ; SOUTH    6
3C60: 01 53 06                  ; S        6
3C63: 04 45 41 53 54 07         ; EAST     7
3C69: 01 45 07                  ; E        7
3C6C: 04 57 45 53 54 08         ; WEST     8
3C72: 01 57 08                  ; W        8
3C75: 04 54 41 4B 45 09         ; TAKE     9
3C7B: 04 44 52 4F 50 0A         ; DROP     10
3C81: 03 50 55 54 0A            ; PUT      10
3C86: 06 49 4E 56 45 4E 54 0B   ; INVENT   11
3C8E: 04 4C 4F 4F 4B 0C         ; LOOK     12
3C94: 04 47 49 56 45 0D         ; GIVE     13
3C9A: 05 4F 46 46 45 52 0D      ; OFFER    13
3CA1: 06 45 58 41 4D 49 4E 0E   ; EXAMIN   14
3CA9: 06 53 45 41 52 43 48 0E   ; SEARCH   14
3CB1: 04 4F 50 45 4E 0F         ; OPEN     15
3CB7: 04 50 55 4C 4C 10         ; PULL     16
3CBD: 05 4C 49 47 48 54 11      ; LIGHT    17
3CC4: 04 42 55 52 4E 11         ; BURN     17
3CCA: 03 45 41 54 12            ; EAT      18
3CCF: 05 54 41 53 54 45 12      ; TASTE    18
3CD6: 04 42 4C 4F 57 13         ; BLOW     19
3CDC: 06 45 58 54 49 4E 47 14   ; EXTING   20
3CE4: 05 43 4C 49 4D 42 15      ; CLIMB    21
3CEB: 03 52 55 42 16            ; RUB      22
3CF0: 04 57 49 50 45 16         ; WIPE     22
3CF6: 06 50 4F 4C 49 53 48 16   ; POLISH   22
3CFE: 04 4C 49 46 54 1C         ; LIFT     28
3D04: 04 57 41 49 54 1F         ; WAIT     31
3D0A: 04 53 54 41 59 1F         ; STAY     31
3D10: 04 4A 55 4D 50 20         ; JUMP     32
3D16: 02 47 4F 21               ; GO       33
3D1A: 03 52 55 4E 21            ; RUN      33
3D1F: 05 45 4E 54 45 52 21      ; ENTER    33
3D26: 04 50 55 53 48 10         ; PUSH     16
3D2C: 04 4D 4F 56 45 10         ; MOVE     16
3D32: 04 4B 49 43 4B 23         ; KICK     35
3D38: 04 46 45 45 44 24         ; FEED     36
3D3E: 05 53 43 4F 52 45 28      ; SCORE    40
3D45: 06 53 43 52 45 41 4D 2B   ; SCREAM   43
3D4D: 04 59 45 4C 4C 2B         ; YELL     43
3D53: 04 51 55 49 54 2D         ; QUIT     45
3D59: 04 53 54 4F 50 2D         ; STOP     45
3D5F: 05 50 4C 55 47 48 32      ; PLUGH    50
3D66: 05 4C 45 41 56 45 2C      ; LEAVE    44
3D6D: 04 50 49 43 4B 34         ; PICK     52
3D73: 00
;
; --- NOUNS ---
3D74: 06 50 4F 54 49 4F 4E 03   ; POTION   3
3D7C: 03 52 55 47 06            ; RUG      6
3D81: 04 44 4F 4F 52 09         ; DOOR     9
3D87: 04 46 4F 4F 44 0C         ; FOOD     12
3D8D: 06 53 54 41 54 55 45 0D   ; STATUE   13
3D95: 05 53 57 4F 52 44 0E      ; SWORD    14
3D9C: 06 47 41 52 47 4F 59 0F   ; GARGOY   15
3DA4: 04 52 49 4E 47 12         ; RING     18
3DAA: 03 47 45 4D 13            ; GEM      19
3DAF: 05 4C 45 56 45 52 16      ; LEVER    22
3DB6: 06 50 4C 41 51 55 45 18   ; PLAQUE   24
3DBE: 05 52 55 4E 45 53 18      ; RUNES    24
3DC5: 04 53 49 47 4E 18         ; SIGN     24
3DCB: 06 4D 45 53 53 41 47 18   ; MESSAG   24
3DD3: 06 43 41 4E 44 4C 45 19   ; CANDLE   25
3DDB: 04 4C 41 4D 50 1B         ; LAMP     27
3DE1: 06 43 48 4F 50 53 54 1E   ; CHOPST   30
3DE9: 04 48 41 4E 44 1F         ; HAND     31
3DEF: 05 48 41 4E 44 53 1F      ; HANDS    31
3DF6: 04 43 4F 49 4E 20         ; COIN     32
3DFC: 04 53 4C 4F 54 21         ; SLOT     33
3E02: 05 41 4C 54 41 52 22      ; ALTAR    34
3E09: 04 49 44 4F 4C 23         ; IDOL     35
3E0F: 06 53 45 52 50 45 4E 24   ; SERPEN   36
3E17: 05 53 4E 41 4B 45 24      ; SNAKE    36
3E1E: 04 57 41 4C 4C 25         ; WALL     37
3E24: 05 57 41 4C 4C 53 25      ; WALLS    37
3E2B: 04 56 49 4E 45 26         ; VINE     38
3E31: 05 56 49 4E 45 53 26      ; VINES    38
3E38: 04 47 41 54 45 27         ; GATE     39
3E3E: 05 47 41 54 45 53 27      ; GATES    39
3E45: 05 47 55 41 52 44 28      ; GUARD    40
3E4C: 06 47 55 41 52 44 53 28   ; GUARDS   40
3E54: 04 52 4F 4F 4D 2A         ; ROOM     42
3E5A: 05 46 4C 4F 4F 52 2B      ; FLOOR    43
3E61: 04 45 58 49 54 2C         ; EXIT     44
3E67: 06 50 41 53 53 41 47 2D   ; PASSAG   45
3E6F: 04 48 4F 4C 45 2E         ; HOLE     46
3E75: 06 43 4F 52 52 49 44 2F   ; CORRID   47
3E7D: 03 42 4F 57 31            ; BOW      49
3E82: 05 41 52 52 4F 57 32      ; ARROW    50
3E89: 06 48 41 4C 4C 57 41 33   ; HALLWA   51
3E91: 06 43 48 41 4D 42 45 34   ; CHAMBE   52
3E99: 05 56 41 55 4C 54 35      ; VAULT    53
3EA0: 06 45 4E 54 52 41 4E 36   ; ENTRAN   54
3EA8: 06 54 55 4E 4E 45 4C 37   ; TUNNEL   55
3EB0: 06 4A 55 4E 47 4C 45 38   ; JUNGLE   56
3EB8: 06 54 45 4D 50 4C 45 39   ; TEMPLE   57
3EC0: 03 50 49 54 3A            ; PIT      58
3EC5: 06 43 45 49 4C 49 4E 3B   ; CEILIN   59
3ECD: 00
;
; --- ADJECTIVES ---
3ECE: 00
;
; --- PREPOSITIONS ---
3ECF: 02 54 4F 01               ; TO       1
3ED3: 04 57 49 54 48 02         ; WITH     2
3ED9: 02 41 54 03               ; AT       3
3EDD: 05 55 4E 44 45 52 04      ; UNDER    4
3EE4: 02 49 4E 05               ; IN       5
3EE8: 04 49 4E 54 4F 05         ; INTO     5
3EEE: 03 4F 55 54 06            ; OUT      6
3EF3: 02 55 50 07               ; UP       7
3EF7: 04 44 4F 57 4E 08         ; DOWN     8
3EFD: 04 4F 56 45 52 09         ; OVER     9
3F03: 06 42 45 48 49 4E 44 0A   ; BEHIND   10
3F0B: 06 41 52 4F 55 4E 44 0B   ; AROUND   11
3F13: 02 4F 4E 0C               ; ON       12
3F17: 00
```
