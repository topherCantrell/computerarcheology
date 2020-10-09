![Code](Bedlam.jpg)

# Bedlam Code

>>> cpu 6809

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

Loaded from cassette at 0x600 (right after text screen memory).<br>
Executed at 0x0600.

# Start

```code
Start:
0600: 86 0D               LDA     #$0D                      ; 14 rows left ...
0602: B7 01 E3            STA     $01E3                     ; {ram:tillMORE} ... until MORE prompt
0605: 4F                  CLRA                              ; 256 words (512 bytes on screen)
0606: 8E 04 00            LDX     #$0400                    ; Start of screen
0609: CE 60 60            LDU     #$6060                    ; Space-space
060C: EF 81               STU     ,X++                      ; Clear ...
060E: 4A                  DECA                              ; ... text ...
060F: 26 FB               BNE     $60C                      ; ... screen
;
0611: 10 CE 03 FF         LDS     #$03FF                    ; Stack starts just below screen
;
0615: 86 13               LDA     #$13                      ; Player object ...
0617: B7 01 D2            STA     $01D2                     ; {ram:ACTIVE_OBJ_NUM} ... is the active object number
;
061A: 8E 05 E0            LDX     #$05E0                    ; Set cursor to ...
061D: 9F 88               STX     <$88                      ; {ram:printCursor} ... bottom row of screen
;
061F: 8E 13 55            LDX     #$1355                    ; Splash message ...
0622: BD 0C 44            JSR     $0C44                     ; {ProcessCommand} ... "you feel as though"
;
0625: 86 0D               LDA     #$0D                      ; Print ...
0627: BD 11 D5            JSR     $11D5                     ; {PrintCharacterAutoWrap} .. CR
062A: BD 0B 6C            JSR     $0B6C                     ; {GetKey} Get a key
;
062D: 8E 13 54            LDX     #$1354                    ; Init random game, place player object, ...
0630: BD 0C 44            JSR     $0C44                     ; {ProcessCommand} ... and look
0633: 86 0D               LDA     #$0D                      ; Print ...
0635: BD 11 D5            JSR     $11D5                     ; {PrintCharacterAutoWrap} ... CR
```

# Main Loop

```code
MainLoop: 
0638: 10 CE 03 FF         LDS     #$03FF                    ; Initialize stack
063C: BD 0B 0D            JSR     $0B0D                     ; Get user input
063F: 86 0D               LDA     #$0D                      ; 14 rows left ...
0641: B7 01 E3            STA     $01E3                     ; {ram:tillMORE} ... until MORE prompt

0644: 7F 01 B7            CLR     $01B7                     ; {ram:adjWord} Adjective word number
0647: 7F 01 BA            CLR     $01BA                     ; {ram:lsbAdj1} LSB of 1st adjective in buffer
064A: 7F 01 BB            CLR     $01BB                     ; {ram:lsbVerb} LSB of verb
064D: 7F 01 B2            CLR     $01B2                     ; {ram:tmp1B2} Misc
0650: 7F 01 B3            CLR     $01B3                     ; {ram:verbWord} Verb word number
0653: 7F 01 B9            CLR     $01B9                     ; {ram:not1B9} Never used again
0656: 7F 01 B8            CLR     $01B8                     ; {ram:commandTarg} Target object of command
0659: 7F 01 B4            CLR     $01B4                     ; {ram:perpWord} Preposition number
065C: 7F 01 B5            CLR     $01B5                     ; {ram:prepGiven} Preposition given flag (not 0 if given)
065F: 7F 01 BF            CLR     $01BF                     ; {ram:VAR_OBJ_NUMBER} VAR object number
0662: 7F 01 C3            CLR     $01C3                     ; {ram:FIRST_NOUN_NUM} 1st noun word number
0665: 7F 01 C9            CLR     $01C9                     ; {ram:SECOND_NOUN_NUM} 2nd noun word number

0668: C6 13               LDB     #$13                      ; Player object ...
066A: F7 01 D2            STB     $01D2                     ; {ram:ACTIVE_OBJ_NUM} ... is active object number
066D: BD 11 7D            JSR     $117D                     ; Get player object data
0670: BF 01 D3            STX     $01D3                     ; {ram:ACTIVE_OBJ_DATA} Active object's data
0673: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip length
0676: E6 84               LDB     ,X                        ; Get player location
0678: F7 01 D5            STB     $01D5                     ; {ram:CUR_ROOM} Current room
067B: 8E 15 A1            LDX     #$15A1                    ; Room scripts
067E: BD 0A 60            JSR     $0A60                     ; {FindSublist} Find sublist ... script for current room
0681: BF 01 D6            STX     $01D6                     ; {ram:CUR_ROOM_DATA} Script for current room
;
0684: 8E 01 E4            LDX     #$01E4                    ; Input token list area
0687: BF 01 D8            STX     $01D8                     ; {ram:nextToken} Where decoder fills in
068A: 6F 84               CLR     ,X                        ; Empty token ... clear the list
068C: 8E 05 E0            LDX     #$05E0                    ; Bottom row is input buffer
068F: BD 0B 83            JSR     $0B83                     ; Decode input word
0692: 27 0B               BEQ     $69F                      ; All words done
0694: A6 80               LDA     ,X+                       ; Next character
0696: 81 60               CMPA    #$60                      ; A space?
0698: 27 F5               BEQ     $68F                      ; Decode next
069A: 8C 06 00            CMPX    #$0600                    ; End of input buffer?
069D: 26 F5               BNE     $694                      ; No ... look for next word
069F: 8C 06 00            CMPX    #$0600                    ; End of input buffer?
06A2: 26 EB               BNE     $68F                      ; No ... keep looking
06A4: 6F 9F 01 D8         CLR     [$01D8]                   ; {ram:nextToken} Terminate token list
06A8: 8E 01 E4            LDX     #$01E4                    ; Input buffer
06AB: A6 84               LDA     ,X                        ; List number of first word
06AD: 10 27 00 92         LBEQ    $0743                     ; Nothing entered
06B1: 81 02               CMPA    #$02                      ; First word a noun?
06B3: 26 0F               BNE     $6C4                      ; No ... move on
06B5: 30 01               LEAX    1,X                       ; Point to word number
06B7: A6 84               LDA     ,X                        ; Get word number
06B9: 30 1F               LEAX    -1,X                      ; Back to list number
06BB: 81 09               CMPA    #$09                      ; Living things (people, dogs, etc) are <9
06BD: 24 05               BCC     $6C4                      ; Not a living thing
06BF: B7 01 B8            STA     $01B8                     ; {ram:commandTarg} Remember living thing. We are giving them a command so process normally.
06C2: 30 03               LEAX    3,X                       ; Next word

06C4: A6 80               LDA     ,X+                       ; Word list
06C6: 27 7B               BEQ     $743                      ; End of list ... go process
06C8: E6 84               LDB     ,X                        ; Word number to B
06CA: EE 81               LDU     ,X++                      ; LSB to LSB of U
06CC: 34 10               PSHS    X                         ; Hold token buffer
06CE: 4A                  DECA                              ; List 1? Verbs?
06CF: 26 21               BNE     $6F2                      ; No ... continue
```

I believe the goal here was to allow multiple verbs given on an input line
to be translated to a single verb. The code finds a replacement list for the
newly given verb and then runs the list two bytes at a time comparing one
of the entries to the last given verb and storing the second byte if there
is a match. I believe that is what is SUPPOSED to happen, but I believe the
code has a bug or two. It actually does nothing at all. The replacement
list for BEDLAM and RAAKATU is empty so the code is never used anyway.

```code
06D1: 8E 13 B2            LDX     #$13B2                    ; Multi verb translation list (empty list for BEDLAM and RAAKATU)
06D4: BD 0A 60            JSR     $0A60                     ; {FindSublist} Look for an entry for the given verb
06D7: 24 13               BCC     $6EC                      ; No entry ... use the word as-is
06D9: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip length of entry
06DC: BD 0A 99            JSR     $0A99                     ; {CompareXY} End of list?
06DF: 1F 98               TFR     B,A                       ; ?? Held in A but ...
06E1: 24 09               BCC     $6EC                      ; Reached end of list. This input is the verb.
06E3: E6 80               LDB     ,X+                       ; ??
06E5: A6 80               LDA     ,X+                       ; ?? ... A is mangled here?
06E7: F1 01 B3            CMPB    $01B3                     ; {ram:verbWord} ?? Compare to 01B3 ...
06EA: 26 F0               BNE     $6DC                      ; Continue running list
06EC: F7 01 B3            STB     $01B3                     ; {ram:verbWord} ?? ... then store if equal?
06EF: 7E 07 3E            JMP     $073E                     ; Continue with next word

06F2: 4A                  DECA                              ; List 2 Noun
06F3: 26 36               BNE     $72B                      ; Not a noun
06F5: 7D 01 B5            TST     $01B5                     ; {ram:prepGiven} Has prepostion been given?
06F8: 27 20               BEQ     $71A                      ; No ... this is first noun
06FA: 8E 01 C9            LDX     #$01C9                    ; 2nd noun area
06FD: E7 80               STB     ,X+                       ; Store word number
06FF: B6 01 B7            LDA     $01B7                     ; {ram:adjWord} Last adjective
0702: A7 80               STA     ,X+                       ; Keep with noun
0704: B6 01 BA            LDA     $01BA                     ; {ram:lsbAdj1} LSB of adjective
0707: A7 84               STA     ,X                        ; Keep with noun
0709: 26 04               BNE     $70F                      ; There was one ... go on
070B: 1F 30               TFR     U,D                       ; Use LSB of ...
070D: E7 84               STB     ,X                        ; ... noun if no adjective
070F: 7F 01 B7            CLR     $01B7                     ; {ram:adjWord} Adjective moved
0712: 7F 01 B5            CLR     $01B5                     ; {ram:prepGiven} Preposition moved
0715: 7F 01 BA            CLR     $01BA                     ; {ram:lsbAdj1} LSB moved
0718: 20 24               BRA     $73E                      ; Continue with next word

071A: BE 01 C3            LDX     $01C3                     ; {ram:FIRST_NOUN_NUM} Copy ...
071D: BF 01 C9            STX     $01C9                     ; {ram:SECOND_NOUN_NUM} ... any ...
0720: BE 01 C5            LDX     $01C5                     ; {ram:firstNounLSB} ... first noun ...
0723: BF 01 CB            STX     $01CB                     ; {ram:secondNounLSB} ... to second
0726: 8E 01 C3            LDX     #$01C3                    ; First word area
0729: 20 D2               BRA     $6FD                      ; Go fill out first word

072B: 4A                  DECA                              ; List 3 Adjective
072C: 26 0A               BNE     $738                      ; Not a proposition
072E: F7 01 B7            STB     $01B7                     ; {ram:adjWord} Store adjective number
0731: 1F 30               TFR     U,D                       ; Store ...
0733: F7 01 BA            STB     $01BA                     ; {ram:lsbAdj1} ... adjective LSB in buffer
0736: 20 06               BRA     $73E                      ; Continue with next word

0738: F7 01 B4            STB     $01B4                     ; {ram:perpWord} Preposition
073B: F7 01 B5            STB     $01B5                     ; {ram:prepGiven} Preoposition given (noun should follow)
073E: 35 10               PULS    X                         ; Restore token pointer
0740: 7E 06 C4            JMP     $06C4                     ; Next word

; Process input
0743: 7D 01 B3            TST     $01B3                     ; {ram:verbWord} Verb given?
0746: 10 27 02 8C         LBEQ    $09D6                     ; No ... ?VERB? error
074A: 8E 01 C9            LDX     #$01C9                    ; Second noun
074D: BD 08 63            JSR     $0863                     ; Decode it (only returns if OK)
0750: B7 01 C9            STA     $01C9                     ; {ram:SECOND_NOUN_NUM} Hold target object index
0753: BF 01 CC            STX     $01CC                     ; {ram:SECOND_NOUN_DATA} Hold target object pointer
0756: 8E 01 C3            LDX     #$01C3                    ; First noun
0759: BD 08 63            JSR     $0863                     ; Decode it (only returns if OK)
075C: B7 01 C3            STA     $01C3                     ; {ram:FIRST_NOUN_NUM} Hold target object index
075F: BF 01 C6            STX     $01C6                     ; {ram:FIRST_NOUN_DATA} Hold target object pointer
0762: 7F 01 B5            CLR     $01B5                     ; {ram:prepGiven} Clear preposition flag

0765: BE 01 C6            LDX     $01C6                     ; {ram:FIRST_NOUN_DATA} Pointer to first noun object data
0768: B6 01 C3            LDA     $01C3                     ; {ram:FIRST_NOUN_NUM} First noun index
076B: 27 07               BEQ     $774                      ; No first noun ... store a 0
076D: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip ID and load end
0770: 30 02               LEAX    2,X                       ; Skip 2 bytes
0772: A6 84               LDA     ,X                        ; Object parameter bits
0774: B7 01 C8            STA     $01C8                     ; {ram:firstNounParams} Hold first noun's parameter bits

0777: BE 01 CC            LDX     $01CC                     ; {ram:SECOND_NOUN_DATA} Pointer to second noun object data
077A: B6 01 C9            LDA     $01C9                     ; {ram:SECOND_NOUN_NUM} Second noun number
077D: 27 07               BEQ     $786                      ; No second noun ... store 0
077F: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip ID and load end
0782: 30 02               LEAX    2,X                       ; Skip 2 bytes
0784: A6 84               LDA     ,X                        ; Object parameter bits
0786: B7 01 CE            STA     $01CE                     ; {ram:secondNounParams} Hold second noun's parameter bits

0789: 8E 13 E3            LDX     #$13E3                    ; Syntax list
078C: A6 84               LDA     ,X                        ; End of list?
078E: 10 27 02 00         LBEQ    $0992                     ; Yes ... "?PHRASE?"
0792: B6 01 B3            LDA     $01B3                     ; {ram:verbWord} Verb ...
0795: A1 80               CMPA    ,X+                       ; ... matches?
0797: 26 57               BNE     $7F0                      ; No ... move to next entry
0799: A6 84               LDA     ,X                        ; Phrase's proposition
079B: B7 01 B6            STA     $01B6                     ; {ram:phrasePrep} Hold it
079E: B6 01 B4            LDA     $01B4                     ; {ram:perpWord} Preposition word number
07A1: 27 04               BEQ     $7A7                      ; None given ... skip prep check
07A3: A1 84               CMPA    ,X                        ; Given prep matches?
07A5: 26 49               BNE     $7F0                      ; No ... move to next phrase
07A7: 30 01               LEAX    1,X                       ; Skip to next phrase component
07A9: A6 84               LDA     ,X                        ; First noun required by phrase
07AB: 27 14               BEQ     $7C1                      ; Not given in phrase ... skip check
07AD: B6 01 C3            LDA     $01C3                     ; {ram:FIRST_NOUN_NUM} 1st noun index
07B0: 26 14               BNE     $7C6                      ; Requested by phrase but not given by user ... next phrase
07B2: B6 01 BB            LDA     $01BB                     ; {ram:lsbVerb} LSB of verb ...
07B5: B7 01 BD            STA     $01BD                     ; {ram:lsbError} ... to location of error
07B8: 10 8E 01 C3         LDY     #$01C3                    ; Descriptor for 1st noun
07BC: BD 09 13            JSR     $0913                     ; Decode 1st noun as per phrase
07BF: 20 05               BRA     $7C6                      ; We just processed a first one. We know it is there.
07C1: B6 01 C3            LDA     $01C3                     ; {ram:FIRST_NOUN_NUM} Is there a 1st noun?
07C4: 26 2C               BNE     $7F2                      ; None given ... move to next entry
07C6: 30 01               LEAX    1,X                       ; Next in phrase
07C8: A6 84               LDA     ,X                        ; Phrase wants a second noun?
07CA: 27 19               BEQ     $7E5                      ; No ... skip
07CC: B6 01 C9            LDA     $01C9                     ; {ram:SECOND_NOUN_NUM} User given 2nd noun
07CF: 26 19               BNE     $7EA                      ; Yes ... use this phrase
07D1: B6 01 BC            LDA     $01BC                     ; {ram:lsbCursor} Location of ...
07D4: B7 01 BD            STA     $01BD                     ; {ram:lsbError} ... error on screen
07D7: 86 01               LDA     #$01                      ; Set preposition ...
07D9: B7 01 B5            STA     $01B5                     ; {ram:prepGiven} ... flag to YES
07DC: 10 8E 01 C9         LDY     #$01C9                    ; 2nd noun index
07E0: BD 09 13            JSR     $0913                     ; Decode 2nd noun as per phrase
07E3: 20 05               BRA     $7EA                      ; Use this

07E5: B6 01 C9            LDA     $01C9                     ; {ram:SECOND_NOUN_NUM} Is there a second noun?
07E8: 26 0A               BNE     $7F4                      ; No ... move to next entry
07EA: 30 01               LEAX    1,X                       ; Get matched ...
07EC: A6 84               LDA     ,X                        ; ... phrase number
07EE: 20 09               BRA     $7F9                      ; Store and continue
07F0: 30 01               LEAX    1,X                       ; Skip ...
07F2: 30 01               LEAX    1,X                       ; ... to ...
07F4: 30 02               LEAX    2,X                       ; ... next entry
07F6: 7E 07 8C            JMP     $078C                     ; Keep looking

; Input processing goes like this:
; If this is a phrase given to someone
;   If the target object has field 0B then execute that script
;   Otherwise execute the general "other commanded" script at 1356. For
;   BEDLAM this script just prints the name. Everybody should have an 0B script.
; else
;   Execute the user-script at 2F24

07F9: B7 01 D1            STA     $01D1                     ; {ram:PHRASE_FORM} Store the phrase number
07FC: 8E 05 FF            LDX     #$05FF                    ; Move cursor to ...
07FF: 9F 88               STX     <$88                      ; {ram:printCursor} ... end of line (force line feed on next print)
0801: B6 01 C3            LDA     $01C3                     ; {ram:FIRST_NOUN_NUM} First noun given?
0804: 26 0C               BNE     $812                      ; Yes ... keep what we have
0806: BE 01 CC            LDX     $01CC                     ; {ram:SECOND_NOUN_DATA} Move 2nd ...
0809: BF 01 C6            STX     $01C6                     ; {ram:FIRST_NOUN_DATA} ... noun to ...
080C: B6 01 C9            LDA     $01C9                     ; {ram:SECOND_NOUN_NUM} ... first ...
080F: B7 01 C3            STA     $01C3                     ; {ram:FIRST_NOUN_NUM} ... descriptor
0812: B6 01 B8            LDA     $01B8                     ; {ram:commandTarg} Command given to someone else?
0815: 27 33               BEQ     $84A                      ; No ... go handle it as user
0817: 8E 01 E5            LDX     #$01E5                    ; First word (who was commanded)
081A: A6 84               LDA     ,X                        ; Get the object word
081C: 6F 84               CLR     ,X                        ; Clear adjective for commanded
081E: A7 82               STA     ,-X                       ; Make a descriptor out of the 1st word area
0820: BD 08 63            JSR     $0863                     ; Lookup the object (make sure they are here)
0823: B7 01 D2            STA     $01D2                     ; {ram:ACTIVE_OBJ_NUM} Active object
0826: BF 01 D3            STX     $01D3                     ; {ram:ACTIVE_OBJ_DATA} Active object data
0829: 86 0D               LDA     #$0D                      ; Print ...
082B: BD 11 D5            JSR     $11D5                     ; {PrintCharacterAutoWrap} ... CR
082E: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip ID and load end
0831: 30 03               LEAX    3,X                       ; Skip object data
0833: C6 0B               LDB     #$0B                      ; Get handle-request ...
0835: BD 0A 68            JSR     $0A68                     ; ... script from the object
0838: 25 08               BCS     $842                      ; There is one ... do it
083A: 8E 13 56            LDX     #$1356                    ; General handler for ...
083D: BD 0C 44            JSR     $0C44                     ; {ProcessCommand} ... being commanded
0840: 20 16               BRA     $858                      ; Allow other objects to move
 
0842: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip size
0845: BD 0C 44            JSR     $0C44                     ; {ProcessCommand} Execute command handler
0848: 20 0E               BRA     $858                      ; Continue with giving objects their turns

084A: 86 0D               LDA     #$0D                      ; Print ...
084C: BD 11 D5            JSR     $11D5                     ; {PrintCharacterAutoWrap} ... CR
084F: 8E 2F 24            LDX     #$2F24                    ; General command scripts
0852: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip over end delta
0855: BD 0C 44            JSR     $0C44                     ; {ProcessCommand} Execute script
;
0858: BD 10 51            JSR     $1051                     ; {EveryTurn} Allow objects to move
085B: 86 0D               LDA     #$0D                      ; Print ...
085D: BD 11 D5            JSR     $11D5                     ; {PrintCharacterAutoWrap} ... CR
0860: 7E 06 38            JMP     $0638                     ; {MainLoop} Top of game loop


; This function decodes the NOUN descriptor pointed to by X. The AJECTIVE-NOUN
; pair is compared to all objects in the room (and pack). If no adjective
; is given and there are multiple matching objects (like multiple doors with
; different colors) then the "?WHICH?" prompt is given. If there is no 
; matching object then "?WHAT?" is given. If this function returns then
; the mapping was successful.
;
; @param X pointer to the noun descriptor to decode
; @return A index of target object
; @return X pointer to target object data
;
0863: 7F 01 BF            CLR     $01BF                     ; {ram:VAR_OBJ_NUMBER} Input object number
0866: E6 80               LDB     ,X+                       ; Word number of noun
0868: F7 01 B2            STB     $01B2                     ; {ram:tmp1B2} Hold it
086B: 26 02               BNE     $86F                      ; Real object ... go decode
086D: 4F                  CLRA                              ; Not found
086E: 39                  RTS                               ; Out
086F: A6 80               LDA     ,X+                       ; Noun's adjective
0871: B7 01 B7            STA     $01B7                     ; {ram:adjWord} Hold it
0874: A6 84               LDA     ,X                        ; LSB of word in buffer
0876: B7 01 CF            STA     $01CF                     ; {ram:tmp1CF} Hold it
0879: 8E 1B 42            LDX     #$1B42                    ; Object data
087C: BD 0A 60            JSR     $0A60                     ; {FindSublist} Get pointer to next object that matches word
087F: 24 5A               BCC     $8DB                      ; Not found
0881: 34 20               PSHS    Y                         ; Hold end of object data
0883: 34 10               PSHS    X                         ; Hold pointer to noun descriptor
0885: B6 01 E1            LDA     $01E1                     ; {ram:tmp1E1} Index of object in the object list
0888: B7 01 E2            STA     $01E2                     ; {ram:tmp1E2} Remember this
088B: BD 08 EB            JSR     $08EB                     ; Is object in this room or on player?
088E: 26 57               BNE     $8E7                      ; No ... can't be target ... out
0890: B6 01 B7            LDA     $01B7                     ; {ram:adjWord} Noun's adjective
0893: 27 1F               BEQ     $8B4                      ; No adjective ... skip this
0895: 35 10               PULS    X                         ; Restore pointer to noun descriptor
0897: 34 10               PSHS    X                         ; Hold it again
0899: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip the id and end
089C: 30 03               LEAX    3,X                       ; Skip the object data
089E: C6 01               LDB     #$01                      ; Look up adjective ...
08A0: BD 0A 68            JSR     $0A68                     ; ... list for object
08A3: 24 0F               BCC     $8B4                      ; No adjective ... ignore
08A5: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip the id and length
08A8: BD 0A 99            JSR     $0A99                     ; {CompareXY} End of adjective list?
08AB: 24 3A               BCC     $8E7                      ; Yes ... no match ... next object
08AD: B6 01 B7            LDA     $01B7                     ; {ram:adjWord} Adjective
08B0: A1 80               CMPA    ,X+                       ; In this list?
08B2: 26 F4               BNE     $8A8                      ; No ... keep searching list
08B4: 35 10               PULS    X                         ; Restore object pointer
08B6: B6 01 BF            LDA     $01BF                     ; {ram:VAR_OBJ_NUMBER} Last object index that matched
08B9: 10 26 01 10         LBNE    $09CD                     ; Multiple matches ... do "?WHICH?"
08BD: B6 01 E2            LDA     $01E2                     ; {ram:tmp1E2} Object index
08C0: B7 01 BF            STA     $01BF                     ; {ram:VAR_OBJ_NUMBER} Current guess at matching object index
08C3: BF 01 C0            STX     $01C0                     ; {ram:VAR_OBJ_DATA} Input object data
08C6: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip id and end
08C9: 1F 21               TFR     Y,X                       ; Next object
08CB: 35 20               PULS    Y                         ; End of object data
08CD: F6 01 B2            LDB     $01B2                     ; {ram:tmp1B2} Restore word number of noun
08D0: B6 01 E2            LDA     $01E2                     ; {ram:tmp1E2} Current object index
08D3: B7 01 E1            STA     $01E1                     ; {ram:tmp1E1} Start count for next pass
08D6: BD 0A 68            JSR     $0A68                     ; Find next matching object
08D9: 25 A6               BCS     $881                      ; Got one ... go test it
08DB: BE 01 C0            LDX     $01C0                     ; {ram:VAR_OBJ_DATA} Object data to X
08DE: B6 01 BF            LDA     $01BF                     ; {ram:VAR_OBJ_NUMBER} Object found?
08E1: 26 03               BNE     $8E6                      ; Yes ...  out
08E3: 7E 09 89            JMP     $0989                     ; No ... "?WHAT?"
08E6: 39                  RTS                               ; Done
08E7: 35 10               PULS    X                         ; Restore object pointer
08E9: 20 DB               BRA     $8C6                      ; Do next object

; This function checks if the target object is in the current room or being
; held by the active object.
;
; @param X pointer to target object
; @return Z=1 for yes or Z=0 for no
;
08EB: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip size
08EE: B6 01 D5            LDA     $01D5                     ; {ram:CUR_ROOM} Current room number
08F1: A1 84               CMPA    ,X                        ; Is object in room?
08F3: 27 F1               BEQ     $8E6                      ; Yes ... return OK
08F5: A6 84               LDA     ,X                        ; Get object's room number
08F7: 27 17               BEQ     $910                      ; 0 ... fail
08F9: 81 FF               CMPA    #$FF                      ; FF ...
08FB: 27 E9               BEQ     $8E6                      ; ... return OK
08FD: 85 80               BITA    #$80                      ; Upper bit of object location set ...
08FF: 26 0F               BNE     $910                      ; ... then fail
0901: E6 84               LDB     ,X                        ; Location again
0903: F1 01 D2            CMPB    $01D2                     ; {ram:ACTIVE_OBJ_NUM} Being held by the active object?
0906: 27 DE               BEQ     $8E6                      ; Yes ... return OK
0908: 8E 1B 42            LDX     #$1B42                    ; Strange. 117D does this too.
090B: BD 11 7D            JSR     $117D                     ; Get object's container object (if any)
090E: 20 DB               BRA     $8EB                      ; Repeat check
0910: 8A 01               ORA     #$01                      ; Mark failure
0912: 39                  RTS                               ; Out

; This function fills the noun descriptor pointed to by Y with the object
; in current room or on user that matches the parameter value from the
; phrase script. If there is not exactly one such object then flash an error
; like "WITH ?WHAT?" using the current preposition or just "?WHAT?" if there
; isn't one.
;
; @param Y pointer to noun descriptor to fill
; @param X pointer to phrase data
; @return descriptor filled out with object
;
0913: 34 10               PSHS    X                         ; Hold phrase data pointer
0915: 7F 01 B2            CLR     $01B2                     ; {ram:tmp1B2} Found word flag
0918: 7F 01 E1            CLR     $01E1                     ; {ram:tmp1E1} Object index starts at 0
091B: 34 20               PSHS    Y                         ; Hold noun descriptor
091D: A6 84               LDA     ,X                        ; Object parameter mask bits
091F: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Hold
0922: 8E 1B 42            LDX     #$1B42                    ; Object data
0925: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip ID and load end
0928: BD 0A 99            JSR     $0A99                     ; {CompareXY} At end of object data?
092B: 24 40               BCC     $96D                      ; Yes ... done
092D: 7C 01 E1            INC     $01E1                     ; {ram:tmp1E1} Bump object index
0930: 34 20               PSHS    Y                         ; Hold end of object
0932: 34 10               PSHS    X                         ; Hold pointer to object
0934: BD 08 EB            JSR     $08EB                     ; Is object in room or on player?
0937: 35 10               PULS    X                         ; Restore pointer to object
0939: 26 2D               BNE     $968                      ; No ... next object
093B: E6 84               LDB     ,X                        ; Object word number
093D: BF 01 D8            STX     $01D8                     ; {ram:nextToken} Pointer to object data
0940: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip ID and load end
0943: 30 02               LEAX    2,X                       ; Point to object parameters
0945: A6 84               LDA     ,X                        ; Get parameters
0947: B4 01 AB            ANDA    $01AB                     ; {ram:tmp1AB} Compare to phrase data ...
094A: B1 01 AB            CMPA    $01AB                     ; {ram:tmp1AB} ... this is a strange way to do it
094D: 26 13               BNE     $962                      ; Not a match ... next word
094F: B6 01 B2            LDA     $01B2                     ; {ram:tmp1B2} Already got a word number?
0952: 26 47               BNE     $99B                      ; Yes ... error
0954: F7 01 B2            STB     $01B2                     ; {ram:tmp1B2} Found word number
0957: A6 84               LDA     ,X                        ; Remember ...
0959: B7 01 B7            STA     $01B7                     ; {ram:adjWord} ... object parameters
095C: BE 01 D8            LDX     $01D8                     ; {ram:nextToken} Remember ...
095F: BF 01 AD            STX     $01AD                     ; {ram:tmp1AD} ... object pointer
0962: 1E 12               EXG     X,Y                       ; Start of next object to X
0964: 35 20               PULS    Y                         ; Restore end of object pointer
0966: 20 C0               BRA     $928                      ; Continue with next object
0968: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip ID and load end
096B: 20 F5               BRA     $962                      ; Try next object
096D: B6 01 B2            LDA     $01B2                     ; {ram:tmp1B2} Did we find an object word?
0970: 27 29               BEQ     $99B                      ; No .... error
0972: 35 20               PULS    Y                         ; Noun descriptor
0974: BE 01 AD            LDX     $01AD                     ; {ram:tmp1AD} Object data pointer
0977: B6 01 E1            LDA     $01E1                     ; {ram:tmp1E1} New ...
097A: A7 A4               STA     ,Y                        ; ... object number
097C: 31 23               LEAY    3,Y                       ; New ...
097E: AF A1               STX     ,Y++                      ; ... pointer to object data
0980: B6 01 B7            LDA     $01B7                     ; {ram:adjWord} New ...
0983: A7 A4               STA     ,Y                        ; ... object parameters
0985: 35 10               PULS    X                         ; Restore phrase data pointer
0987: 4F                  CLRA                              ; Set Z=1
0988: 39                  RTS                               ; Done

0989: 10 8E 13 C3         LDY     #$13C3                    ; "?WHAT?"
098D: B6 01 CF            LDA     $01CF                     ; {ram:tmp1CF} LSB of screen location
0990: 20 4A               BRA     $9DC                      ; Go flash error and try again

0992: 10 8E 13 D2         LDY     #$13D2                    ; "?PHRASE?"
0996: B6 01 BC            LDA     $01BC                     ; {ram:lsbCursor} LSB of screen location
0999: 20 41               BRA     $9DC                      ; Go flash error and try again

099B: B6 01 B5            LDA     $01B5                     ; {ram:prepGiven} Preposition given?
099E: 27 24               BEQ     $9C4                      ; No ... just plain "?WHAT?"
09A0: B6 01 B4            LDA     $01B4                     ; {ram:perpWord} Preposition word number?
09A3: 26 1F               BNE     $9C4                      ; No word ... just plain "?WHAT?"
09A5: 8E 3E A2            LDX     #$3EA2                    ; Prepositions list
09A8: E6 84               LDB     ,X                        ; Length of word
09AA: 27 18               BEQ     $9C4                      ; Reached the end ... do "?WHAT?"
09AC: 34 10               PSHS    X                         ; Hold start of word
09AE: E6 80               LDB     ,X+                       ; Get length again
09B0: 3A                  ABX                               ; Point to end of word
09B1: B6 01 B6            LDA     $01B6                     ; {ram:phrasePrep} Target preposition
09B4: A1 80               CMPA    ,X+                       ; Matches?
09B6: 27 04               BEQ     $9BC                      ; Yes ... error includes this word
09B8: 35 06               PULS    A,B                       ; Restore stack
09BA: 20 EC               BRA     $9A8                      ; Next word
09BC: 35 20               PULS    Y                         ; Word text to Y
09BE: B6 01 BD            LDA     $01BD                     ; {ram:lsbError} LSB of error message
09C1: BD 0A 22            JSR     $0A22                     ; Push preposition word
09C4: 10 8E 13 C3         LDY     #$13C3                    ; "?WHAT?"
09C8: B6 01 BD            LDA     $01BD                     ; {ram:lsbError} LSB of screen location
09CB: 20 0F               BRA     $9DC                      ; Go flash error and try again
09CD: 10 8E 13 CA         LDY     #$13CA                    ; "?WHICH"?
09D1: B6 01 CF            LDA     $01CF                     ; {ram:tmp1CF} LSB of screen location
09D4: 20 06               BRA     $9DC                      ; Go flash error and try again
09D6: 10 8E 13 BC         LDY     #$13BC                    ; "?VERB?"
;
09DA: 86 E0               LDA     #$E0                      ; LSB of start of input line
09DC: 10 CE 03 FF         LDS     #$03FF                    ; Reset the stack (we jump back into the main loop)
09E0: 8E 05 E0            LDX     #$05E0                    ; Error goes at start of line
09E3: BD 0A 22            JSR     $0A22                     ; Push error message on and pause
09E6: A6 A4               LDA     ,Y                        ; Get length
09E8: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Hold in counter
09EB: 34 10               PSHS    X                         ; Hold X
09ED: 86 60               LDA     #$60                      ; SPACE
09EF: A7 80               STA     ,X+                       ; Flash off ...
09F1: 7A 01 AB            DEC     $01AB                     ; {ram:tmp1AB} ... error ...
09F4: 26 F7               BNE     $9ED                      ; ... word
09F6: BD 0A 17            JSR     $0A17                     ; Long delay
09F9: 35 10               PULS    X                         ; Restore insertion point
09FB: 5A                  DECB                              ; All flashes done?
09FC: 26 14               BNE     $A12                      ; No ... keep flashing error word
09FE: A6 A4               LDA     ,Y                        ; Size of error word
0A00: 4C                  INCA                              ; Plus the extra space
0A01: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Hold counter
0A04: BD 0B 1C            JSR     $0B1C                     ; Close up the ...
0A07: 7A 01 AB            DEC     $01AB                     ; {ram:tmp1AB} ... error ...
0A0A: 26 F8               BNE     $A04                      ; ... word
0A0C: BD 0A A4            JSR     $0AA4                     ; Get input line
0A0F: 7E 06 44            JMP     $0644                     ; Continue processing
0A12: BD 0A 41            JSR     $0A41                     ; Flash message and pause
0A15: 20 CF               BRA     $9E6                      ; Continue flashing and read new line

;Long delay
0A17: 86 32               LDA     #$32                      ; Outer loop counts
0A19: 7A 01 AB            DEC     $01AB                     ; {ram:tmp1AB} Decrease inner count (doesn't matter what's there)
0A1C: 26 FB               BNE     $A19                      ; Kill inner time
0A1E: 4A                  DECA                              ; All 256 loops done?
0A1F: 26 F8               BNE     $A19                      ; No ... keep pausing
0A21: 39                  RTS                               ; Done

0A22: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Hold LSB of cursor
0A25: CC 05 E0            LDD     #$05E0                    ; Start of input line
0A28: F6 01 AB            LDB     $01AB                     ; {ram:tmp1AB} Replace LSB
0A2B: 1F 01               TFR     D,X                       ; Place for error word in X
0A2D: A6 A4               LDA     ,Y                        ; Get length of message
0A2F: 4C                  INCA                              ; Plus a space after
0A30: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Store length
0A33: 34 20               PSHS    Y                         ; Hold message
0A35: BD 0B 47            JSR     $0B47                     ; Slide right past insertion point
0A38: 7A 01 AB            DEC     $01AB                     ; {ram:tmp1AB} Space opened up?
0A3B: 26 F8               BNE     $A35                      ; No ... open all the spaces for the error word
0A3D: 35 20               PULS    Y                         ; Restore pointer
0A3F: C6 08               LDB     #$08                      ; 8 flashes
0A41: A6 A4               LDA     ,Y                        ; Count again
0A43: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Size of word
0A46: 34 34               PSHS    Y,X,B                     ; Hold all
0A48: 31 21               LEAY    1,Y                       ; Skip size
0A4A: A6 A0               LDA     ,Y+                       ; Copy error word ...
0A4C: A7 80               STA     ,X+                       ; ... to screen
0A4E: 7A 01 AB            DEC     $01AB                     ; {ram:tmp1AB} All done?
0A51: 26 F7               BNE     $A4A                      ; No ... go back and do all
0A53: 30 01               LEAX    1,X                       ; Bump ...
0A55: 1F 10               TFR     X,D                       ; ... LSB ...
0A57: F7 01 BD            STB     $01BD                     ; {ram:lsbError} ... of screen pointer
0A5A: BD 0A 17            JSR     $0A17                     ; Long pause
0A5D: 35 34               PULS    B,X,Y                     ; Restore
0A5F: 39                  RTS                               ; Done

FindSublist:
; Find a sublist by ID within a master list.
; X=pointer to master list
; B=sublist ID
; Return sublist pointer in X
; Return C=0 if not found, C=1 if found
0A60: 30 01               LEAX    1,X                       ; Skip list ID
0A62: BD 0A 85            JSR     $0A85                     ; {LoadEnd} Read end of list to Y
0A65: 7F 01 E1            CLR     $01E1                     ; {ram:tmp1E1} Clear index of sublist
0A68: BD 0A 99            JSR     $0A99                     ; {CompareXY} Compare X to Y
0A6B: 25 01               BCS     $A6E                      ; X is smaller ... keep going
0A6D: 39                  RTS                               ; Done (C=0 not found)
0A6E: 7C 01 E1            INC     $01E1                     ; {ram:tmp1E1} Keep up with index of sublist
0A71: E1 84               CMPB    ,X                        ; Is this the sublist we want?
0A73: 27 0B               BEQ     $A80                      ; Found ... C=1 and out
0A75: 34 20               PSHS    Y                         ; Hold the end
0A77: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip ID and read end of list to Y
0A7A: 1F 21               TFR     Y,X                       ; Jump to the end of this list
0A7C: 35 20               PULS    Y                         ; Restore the end of the master lsit
0A7E: 20 E8               BRA     $A68                      ; Keep looking for the sublist
;
0A80: 1A 01               ORCC    #$01                      ; C=1
0A82: 39                  RTS                               ; Done

SkipIDLoadEnd:
; Skip the ID byte and load the end of the list in Y.
0A83: 30 01               LEAX    1,X                       ; Bump script pointer
;
LoadEnd:
; Load the end of the list in Y.
0A85: 4F                  CLRA                              ; Upper is 0
0A86: 34 04               PSHS    B                         ; Hold lower
0A88: E6 80               LDB     ,X+                       ; Get lower
0A8A: C5 80               BITB    #$80                      ; One or two byte value?
0A8C: 27 06               BEQ     $A94                      ; Just a one byte ... use it
0A8E: C4 7F               ANDB    #$7F                      ; This is the ...
0A90: 1F 98               TFR     B,A                       ; ... MSB
0A92: E6 80               LDB     ,X+                       ; Now get 2nd byte (LSB)
0A94: 31 8B               LEAY    D,X                       ; Offset script
0A96: 35 04               PULS    B                         ; Restore B
0A98: 39                  RTS                               ; Done

CompareXY:
; Compare X to Y (flags = X - Y)
0A99: 10 BF 01 A9         STY     $01A9                     ; {ram:tmp1A9} Do compare ...
0A9D: BC 01 A9            CMPX    $01A9                     ; {ram:tmp1A9} X - Y
0AA0: 39                  RTS                               ; Done
```

# Get Input Line

```code
GetInputLine:
0AA1: 8E 05 E0            LDX     #$05E0                    ; Start of bottom row
0AA4: BD 0B 64            JSR     $0B64                     ; Slide bottom row to right after cursor and draw cursor
0AA7: BD 0B 6C            JSR     $0B6C                     ; {GetKey} Get a key from the keyboard
0AAA: 81 15               CMPA    #$15                      ; SHIFT-LEFT ARROW ? (true left arrow)
0AAC: 27 20               BEQ     $ACE                      ; Swap cursor and character to left
0AAE: 81 5D               CMPA    #$5D                      ;  SHIFT-RIGHT ARROW ? (true right arrow)
0AB0: 27 2F               BEQ     $AE1                      ; Swap cursor and character to right
0AB2: 81 09               CMPA    #$09                      ; Backspace
0AB4: 27 3E               BEQ     $AF4                      ; Go handle backspace
0AB6: 81 0D               CMPA    #$0D                      ; CR?
0AB8: 27 4F               BEQ     $B09                      ; Handle it and out
0ABA: 81 0C               CMPA    #$0C                      ; CLEAR?
0ABC: 27 4F               BEQ     $B0D                      ; Yes ... clear the row
0ABE: 81 08               CMPA    #$08                      ; LEFT-ARROW ? (backspace)
0AC0: 27 3B               BEQ     $AFD                      ; Yes go handle
0AC2: 8C 05 FF            CMPX    #$05FF                    ; At the end of the screen?
0AC5: 27 E0               BEQ     $AA7                      ; Yes ... ignore and get another
0AC7: BD 0B 47            JSR     $0B47                     ; Slide bottom row beyond insertion
0ACA: A7 80               STA     ,X+                       ; Store character
0ACC: 20 D9               BRA     $AA7                      ; Go get another character
;  
0ACE: 8C 05 E0            CMPX    #$05E0                    ; Nothing typed?
0AD1: 27 D4               BEQ     $AA7                      ; Yes ... ignore and get another
0AD3: 30 1F               LEAX    -1,X                      ; Swap ...
0AD5: A6 80               LDA     ,X+                       ; ... cursor ...
0AD7: A7 84               STA     ,X                        ; ... and ...
0AD9: 30 1F               LEAX    -1,X                      ; ... character ...
0ADB: 86 CF               LDA     #$CF                      ; ... to the ...
0ADD: A7 84               STA     ,X                        ; ... left
0ADF: 20 C6               BRA     $AA7                      ; Go get another character
;
0AE1: 8C 05 FF            CMPX    #$05FF                    ; End of screen?
0AE4: 27 C1               BEQ     $AA7                      ; Yes ... go get another key
0AE6: 30 01               LEAX    1,X                       ; Swap ...
0AE8: A6 84               LDA     ,X                        ; ... cursor ...
0AEA: 30 1F               LEAX    -1,X                      ; ... and ...
0AEC: A7 80               STA     ,X+                       ; ... character ...
0AEE: 86 CF               LDA     #$CF                      ; ... to the ...
0AF0: A7 84               STA     ,X                        ; ... right
0AF2: 20 B3               BRA     $AA7                      ; Go get another key
;
0AF4: BD 0B 1C            JSR     $0B1C                     ; Back off trailing cursor block
0AF7: 86 CF               LDA     #$CF                      ; Store ...
0AF9: A7 84               STA     ,X                        ; ... cursor block
0AFB: 20 AA               BRA     $AA7                      ; Go get another key
;
0AFD: 8C 05 E0            CMPX    #$05E0                    ; At the start of the row?
0B00: 27 A5               BEQ     $AA7                      ; Yes ... go get another key
0B02: 30 1F               LEAX    -1,X                      ; Back up one character
0B04: BD 0B 1C            JSR     $0B1C                     ; Erase the end
0B07: 20 9E               BRA     $AA7                      ; Go get another key
;
0B09: BD 0B 1C            JSR     $0B1C                     ; Back off cursor character
0B0C: 39                  RTS                               ; Done
;
0B0D: 8E 05 E0            LDX     #$05E0                    ; Start of bottom row
0B10: C6 20               LDB     #$20                      ; 32 characters on the row
0B12: 86 60               LDA     #$60                      ; SPACE character
0B14: A7 80               STA     ,X+                       ; Clear ...
0B16: 5A                  DECB                              ; ... the ...
0B17: 26 FB               BNE     $B14                      ; ... bottom row
0B19: 7E 0A A1            JMP     $0AA1                     ; {GetInputLine} Go get another key
;   
0B1C: 1F 13               TFR     X,U                       ; Hold X
0B1E: 31 01               LEAY    1,X                       ; Clear trailing ...
0B20: 86 60               LDA     #$60                      ; ... cursor ...
0B22: A7 84               STA     ,X                        ; ... block
;
0B24: 10 8C 06 00         CMPY    #$0600                    ; End of screen?
0B28: 27 E2               BEQ     $B0C                      ; Yes out
0B2A: 10 8C 06 01         CMPY    #$0601                    ; End of screen?
0B2E: 27 DC               BEQ     $B0C                      ; Yes out
0B30: 10 8C 06 02         CMPY    #$0602                    ; End of screen?
0B34: 27 D6               BEQ     $B0C                      ; Yes out
0B36: A6 A0               LDA     ,Y+                       ; Back ...
0B38: A7 80               STA     ,X+                       ; ... up ...
0B3A: 10 8C 06 00         CMPY    #$0600                    ; ... row ...
0B3E: 26 F6               BNE     $B36                      ; ... over cursor
0B40: 86 60               LDA     #$60                      ; Clear last ...
0B42: A7 84               STA     ,X                        ; ... character
0B44: 1F 31               TFR     U,X                       ; Restore X
0B46: 39                  RTS                               ; Done
;
0B47: 8C 06 00            CMPX    #$0600                    ; Past end of screen?
0B4A: 27 17               BEQ     $B63                      ; Yes ... out
0B4C: BF 01 A7            STX     $01A7                     ; {ram:tmp1A7} Hold insertion point
0B4F: 8E 06 00            LDX     #$0600                    ; End+1
0B52: 10 8E 05 FF         LDY     #$05FF                    ; End
0B56: E6 A2               LDB     ,-Y                       ; Slide bottom row ...
0B58: E7 82               STB     ,-X                       ; ... to the right
0B5A: BC 01 A7            CMPX    $01A7                     ; {ram:tmp1A7} At the insertion point?
0B5D: 26 F7               BNE     $B56                      ; No ... slide all
0B5F: C6 60               LDB     #$60                      ; SPACE
0B61: E7 84               STB     ,X                        ; Clear first character
0B63: 39                  RTS                               ; Done
;
0B64: BD 0B 47            JSR     $0B47                     ; Slide row over from cursor
0B67: 86 CF               LDA     #$CF                      ; Cursor character (white block)
0B69: A7 84               STA     ,X                        ; Cursor to screen
0B6B: 39                  RTS                               ; Done
```

# Get Key

```code
GetKey:
0B6C: BD 13 19            JSR     $1319                     ; {Com_2B_GenerateRandomNumber} Get random number every key
0B6F: AD 9F A0 00         JSR     [$A000]                   ; {hard:POLCAT} Get key from user
0B73: 4D                  TSTA                              ; Anything pressed?
0B74: 27 F6               BEQ     $B6C                      ; {GetKey} No ... keep waiting
0B76: 81 41               CMPA    #$41                      ; Letter 'A'
0B78: 24 06               BCC     $B80                      ; Greater or equal ... use it
0B7A: 81 20               CMPA    #$20                      ; Space
0B7C: 25 02               BCS     $B80                      ; Lower .... use it
0B7E: 8B 40               ADDA    #$40                      ; Not really sure why. '!' becomes 'a'.
0B80: 39                  RTS                               ; Done
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
0B81: 30 01               LEAX    1,X                       ; Next in buffer
;
0B83: 1F 10               TFR     X,D                       ; Hold ...
0B85: F7 01 CF            STB     $01CF                     ; {ram:tmp1CF} ... LSB of first word (could be ignored)
0B88: 8C 06 00            CMPX    #$0600                    ; End of buffer?
0B8B: 27 F3               BEQ     $B80                      ; Yes ... out
0B8D: A6 84               LDA     ,X                        ; Next in input
0B8F: 81 60               CMPA    #$60                      ; Valid character?
0B91: 24 EE               BCC     $B81                      ; {DecodeBuffer} No ... skip till we find one
0B93: 10 8E 3B D5         LDY     #$3BD5                    ; Word token table
0B97: BD 0B CC            JSR     $0BCC                     ; {DecodeWord} Try first list
0B9A: 27 E7               BEQ     $B83                      ; Found a match ... ignore it
0B9C: C6 01               LDB     #$01                      ; Staring list number
0B9E: 31 21               LEAY    1,Y                       ; Next list of words
0BA0: BD 0B CC            JSR     $0BCC                     ; {DecodeWord} Try and match
0BA3: 27 08               BEQ     $BAD                      ; Found a match ... record it
0BA5: 5C                  INCB                              ; Next list of words
0BA6: C1 05               CMPB    #$05                      ; All tried?
0BA8: 26 F4               BNE     $B9E                      ; No ... go back and try all
0BAA: 8A 01               ORA     #$01                      ; Not-zero ... error
0BAC: 39                  RTS                               ; Done

0BAD: 1E 12               EXG     X,Y                       ; X to Y
0BAF: BE 01 D8            LDX     $01D8                     ; {ram:nextToken} Current result token pointer
0BB2: E7 80               STB     ,X+                       ; Store list number
0BB4: A7 80               STA     ,X+                       ; Store word number
0BB6: B6 01 CF            LDA     $01CF                     ; {ram:tmp1CF} Start of word
0BB9: A7 80               STA     ,X+                       ; Store word start
0BBB: BF 01 D8            STX     $01D8                     ; {ram:nextToken} Bump result token pointer
0BBE: 1E 12               EXG     X,Y                       ; Restore X
0BC0: C1 01               CMPB    #$01                      ; Is this the first (VERB) list?
0BC2: 26 06               BNE     $BCA                      ; No ... skip marking
0BC4: B6 01 BC            LDA     $01BC                     ; {ram:lsbCursor} Mark the input buffer location ...
0BC7: B7 01 BB            STA     $01BB                     ; {ram:lsbVerb} ... of the verb
0BCA: 4F                  CLRA                              ; OK
0BCB: 39                  RTS                               ; Return

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
0BCC: A6 A4               LDA     ,Y                        ; Length of word
0BCE: 26 03               BNE     $BD3                      ; It is a word ... go check it
0BD0: 8A 01               ORA     #$01                      ; End of list ...
0BD2: 39                  RTS                               ; ... return not-zero
0BD3: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Temporary
0BD6: B7 01 D0            STA     $01D0                     ; {ram:tmp1DO} Temporary
0BD9: 34 10               PSHS    X                         ; Hold pointer to input word
0BDB: 31 21               LEAY    1,Y                       ; Skip over word length in table
0BDD: A6 84               LDA     ,X                        ; Character from input (from screen)
0BDF: 81 60               CMPA    #$60                      ; Space?
0BE1: 27 53               BEQ     $C36                      ; Yes. Didn't match the target word. Next.
0BE3: 8C 06 00            CMPX    #$0600                    ; Past screen (end of buffer)?
0BE6: 27 4E               BEQ     $C36                      ; Yes. Didn't match the target word. next
0BE8: 81 60               CMPA    #$60                      ; Valid character?
0BEA: 25 04               BCS     $BF0                      ; Yes ... do compare
0BEC: 30 01               LEAX    1,X                       ; No ... skip this
0BEE: 20 ED               BRA     $BDD                      ; Look for valid character
0BF0: A1 A4               CMPA    ,Y                        ; Matches target word?
0BF2: 26 42               BNE     $C36                      ; No ... next word
0BF4: 30 01               LEAX    1,X                       ; Next in input
0BF6: 31 21               LEAY    1,Y                       ; Next in match
0BF8: 7A 01 AB            DEC     $01AB                     ; {ram:tmp1AB} All done?
0BFB: 26 E0               BNE     $BDD                      ; No ... keep looking
0BFD: B6 01 D0            LDA     $01D0                     ; {ram:tmp1DO} Original length
0C00: 81 06               CMPA    #$06                      ; Six letter input?
0C02: 27 06               BEQ     $C0A                      ; Yes ... could be truncated. That's enough of a match.
0C04: A6 84               LDA     ,X                        ; Next from screen
0C06: 81 60               CMPA    #$60                      ; Space? End of word?
0C08: 25 33               BCS     $C3D                      ; No. Try next word
0C0A: A6 A4               LDA     ,Y                        ; Get the word data
0C0C: 35 20               PULS    Y                         ; Drop the input buffer pointer
0C0E: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Hold the word data
0C11: A6 84               LDA     ,X                        ; Next in input buffer?
0C13: 81 60               CMPA    #$60                      ; Is it a space?
0C15: 27 0C               BEQ     $C23                      ; Yes ... ready for next word
0C17: BF 01 A7            STX     $01A7                     ; {ram:tmp1A7} Start of next word (in case end of buffer)
0C1A: 8C 06 00            CMPX    #$0600                    ; Is this the end of the input buffer?
0C1D: 27 0A               BEQ     $C29                      ; Yes. Done
0C1F: 30 01               LEAX    1,X                       ; Skip to next input word
0C21: 20 EE               BRA     $C11                      ; Keep looking for input
0C23: BF 01 A7            STX     $01A7                     ; {ram:tmp1A7} Pointer to ending space
0C26: 7C 01 A8            INC     $01A8                     ; {ram:tmp1A7} Point to next character past space (start of next word)
0C29: B6 01 A8            LDA     $01A8                     ; {ram:tmp1A7} Keep ...
0C2C: B7 01 BC            STA     $01BC                     ; {ram:lsbCursor} ... only LSB
0C2F: B6 01 AB            LDA     $01AB                     ; {ram:tmp1AB} Return word data in A
0C32: 7F 01 A7            CLR     $01A7                     ; {ram:tmp1A7} return is-zero for found
0C35: 39                  RTS                               ; Done
;
0C36: 31 21               LEAY    1,Y                       ; Skip next in word data
0C38: 7A 01 AB            DEC     $01AB                     ; {ram:tmp1AB} All skipped
0C3B: 26 F9               BNE     $C36                      ; No ... skip all
0C3D: 35 10               PULS    X                         ; Restore pointer to word
0C3F: 31 21               LEAY    1,Y                       ; Skip word data
0C41: 7E 0B CC            JMP     $0BCC                     ; {DecodeWord} Keep trying
```

# Process Command

```code
ProcessCommand:
; Either a direct command or a common command
0C44: A6 80               LDA     ,X+                       ; Next in script
0C46: 1F 89               TFR     A,B                       ; Hold original command
0C48: 85 80               BITA    #$80                      ; Upper bit set?
0C4A: 27 13               BEQ     $C5F                      ; No ... do commands
0C4C: 34 30               PSHS    Y,X                       ; Hold
0C4E: 8E 33 9C            LDX     #$339C                    ; Common commands
0C51: BD 0A 60            JSR     $0A60                     ; {FindSublist} Find common command
0C54: 24 06               BCC     $C5C                      ; Not found ... skip
0C56: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip length of command
0C59: BD 0C 44            JSR     $0C44                     ; {ProcessCommand} Execute command
0C5C: 35 30               PULS    X,Y                       ; Restore
0C5E: 39                  RTS                               ; Out

0C5F: 1F 98               TFR     B,A                       ; Hold original command
0C61: 10 8E 13 57         LDY     #$1357                    ; Function table
0C65: 48                  ASLA                              ; Jump to ...
0C66: 6E B6               JMP     [A,Y]                     ; ... command

Com_0D_while_pass:
; while_pass:
; Execute a list of commands as long as they pass. Either way end pointing one
; past end.
; Data: LENGTH + list of command
0C68: BD 0A 85            JSR     $0A85                     ; {LoadEnd} Read length of command
0C6B: BD 0A 99            JSR     $0A99                     ; {CompareXY} Are we past the end?
0C6E: 24 0C               BCC     $C7C                      ; Yes ... end successfully
0C70: 34 20               PSHS    Y                         ; Hold the end
0C72: BD 0C 44            JSR     $0C44                     ; {ProcessCommand} Execute the command
0C75: 35 20               PULS    Y                         ; Restore the end
0C77: 27 F2               BEQ     $C6B                      ; Command successful? Yes ... keep processing
0C79: 1E 12               EXG     X,Y                       ; Fail ... put us at the end
0C7B: 39                  RTS                               ; Done
0C7C: 1E 12               EXG     X,Y                       ; Point to end of list
0C7E: 4F                  CLRA                              ; Z=1 ... success
0C7F: 39                  RTS                               ; Done

Com_0E_while_fail:
; while_fail:
0C80: BD 0A 85            JSR     $0A85                     ; {LoadEnd} Load the end
0C83: BD 0A 99            JSR     $0A99                     ; {CompareXY} Reached end of list?
0C86: 24 0C               BCC     $C94                      ; Yes ... error
0C88: 34 20               PSHS    Y                         ; Hold end of command
0C8A: BD 0C 44            JSR     $0C44                     ; {ProcessCommand} Execute command
0C8D: 35 20               PULS    Y                         ; Restore end
0C8F: 26 F2               BNE     $C83                      ; Command failed ... try next
0C91: 1E 12               EXG     X,Y                       ; Set script pointer to end of list
0C93: 39                  RTS                               ; Out
;
0C94: 1E 12               EXG     X,Y                       ; Set script pointer to end of list
0C96: 8A 01               ORA     #$01                      ; Return fail
0C98: 39                  RTS                               ; Done

Com_0B_switch:
; switch:
0C99: BD 0A 85            JSR     $0A85                     ; {LoadEnd} Get size of switch list
0C9C: E6 80               LDB     ,X+                       ; Get function to call
0C9E: BD 0A 99            JSR     $0A99                     ; {CompareXY} End of options?
0CA1: 24 F1               BCC     $C94                      ; Yes ... out with error
0CA3: 34 20               PSHS    Y                         ; Hold total switch size
0CA5: 34 04               PSHS    B                         ; Hold function to call
0CA7: 1F 98               TFR     B,A                       ; Call the ...
0CA9: BD 0C 61            JSR     $0C61                     ; ... target function
0CAC: 35 04               PULS    B                         ; Restore function to call
0CAE: 27 09               BEQ     $CB9                      ; Got our script ... go do it
0CB0: BD 0A 85            JSR     $0A85                     ; {LoadEnd} Size of pass script
0CB3: 1E 12               EXG     X,Y                       ; Skip over this option
0CB5: 35 20               PULS    Y                         ; End of script
0CB7: 20 E5               BRA     $C9E                      ; Keep looking
0CB9: BD 0A 85            JSR     $0A85                     ; {LoadEnd} Skip length
0CBC: BD 0C 44            JSR     $0C44                     ; {ProcessCommand} Execute
0CBF: 35 10               PULS    X                         ; Restore script
0CC1: 39                  RTS                               ; Done

Com_00_move_ACTIVE_and_look:
; move_ACTIVE_and_look(room)
0CC2: BD 0C CE            JSR     $0CCE                     ; {Com_19_MoveActiveObjectToRoom} Move active object to new room
0CC5: 34 10               PSHS    X                         ; Hold script
0CC7: BD 0D 8B            JSR     $0D8B                     ; Print room description and objects
0CCA: 35 10               PULS    X                         ; Restore script
0CCC: 4F                  CLRA                              ; OK
0CCD: 39                  RTS                               ; Done

Com_19_move_ACTIVE:
; move_ACTIVE(room)
0CCE: A6 80               LDA     ,X+                       ; New room number
0CD0: 34 10               PSHS    X                         ; Hold script
0CD2: B7 01 D5            STA     $01D5                     ; {ram:CUR_ROOM} Store new actvie room number
0CD5: 1F 89               TFR     A,B                       ; Store ...
0CD7: 8E 15 A1            LDX     #$15A1                    ; ... pointer ...
0CDA: BD 0A 60            JSR     $0A60                     ; {FindSublist} ... to ...
0CDD: BF 01 D6            STX     $01D6                     ; {ram:CUR_ROOM_DATA} ... new room
0CE0: BE 01 D3            LDX     $01D3                     ; {ram:ACTIVE_OBJ_DATA} Active object
0CE3: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip size
0CE6: B6 01 D5            LDA     $01D5                     ; {ram:CUR_ROOM} New location
0CE9: A7 84               STA     ,X                        ; Move object to active room
0CEB: 35 10               PULS    X                         ; Restore script
0CED: 4F                  CLRA                              ; OK
0CEE: 39                  RTS                               ; Done

Com_1A_set_VAR_to_first_noun:
; set_VAR_to_first_noun()
0CEF: FE 01 C6            LDU     $01C6                     ; {ram:FIRST_NOUN_DATA} Copy 1st noun ...
0CF2: FF 01 C0            STU     $01C0                     ; {ram:VAR_OBJ_DATA} ... data pointer
0CF5: B6 01 C3            LDA     $01C3                     ; {ram:FIRST_NOUN_NUM} Copy 1st noun ...
0CF8: B7 01 BF            STA     $01BF                     ; {ram:VAR_OBJ_NUMBER} ... object number
0CFB: 4F                  CLRA                              ; Z=1 for OK
0CFC: 39                  RTS                               ; Done

Com_1B_set_VAR_to_second_noun:
; set_VAR_to_second_noun()
0CFD: FE 01 CC            LDU     $01CC                     ; {ram:SECOND_NOUN_DATA} Copy 2nd noun ...
0D00: FF 01 C0            STU     $01C0                     ; {ram:VAR_OBJ_DATA} ... data pointer
0D03: B6 01 C9            LDA     $01C9                     ; {ram:SECOND_NOUN_NUM} Copy 2nd noun ...
0D06: B7 01 BF            STA     $01BF                     ; {ram:VAR_OBJ_NUMBER} ... object number
0D09: 4F                  CLRA                              ; Z=1 for OK
0D0A: 39                  RTS                               ; Done

Com_1C_set_VAR:
; set_VAR(object)
0D0B: E6 80               LDB     ,X+                       ; Get object number from script
0D0D: 34 10               PSHS    X                         ; Hold script pointer
0D0F: F7 01 BF            STB     $01BF                     ; {ram:VAR_OBJ_NUMBER} Store target object number
0D12: 27 06               BEQ     $D1A                      ; 0 ... no-object
0D14: BD 11 7D            JSR     $117D                     ; Find object data
0D17: BF 01 C0            STX     $01C0                     ; {ram:VAR_OBJ_DATA} Store target object data
0D1A: 35 10               PULS    X                         ; Restore script
0D1C: 4F                  CLRA                              ; Return OK
0D1D: 39                  RTS                               ; Done

Com_21_execute_phrase:
; execute_phrase(phrase,first_noun,second_noun)
0D1E: FE 01 C6            LDU     $01C6                     ; {ram:FIRST_NOUN_DATA} 1st noun data ...
0D21: 34 40               PSHS    U                         ; ... on stack
0D23: FE 01 CC            LDU     $01CC                     ; {ram:SECOND_NOUN_DATA} 2nd noun data ...
0D26: 34 40               PSHS    U                         ; ... on stack
0D28: B6 01 C9            LDA     $01C9                     ; {ram:SECOND_NOUN_NUM} 2nd noun number
0D2B: F6 01 C3            LDB     $01C3                     ; {ram:FIRST_NOUN_NUM} 1st noun number
0D2E: 34 06               PSHS    B,A                       ; Hold these
0D30: B6 01 D1            LDA     $01D1                     ; {ram:PHRASE_FORM} Phrase number
0D33: 34 02               PSHS    A                         ; Hold it
0D35: A6 80               LDA     ,X+                       ; New temporary ...
0D37: B7 01 D1            STA     $01D1                     ; {ram:PHRASE_FORM} ... phrase number
0D3A: EC 81               LDD     ,X++                      ; Temporary 1st and 2nd noun numbers
0D3C: F7 01 AB            STB     $01AB                     ; {ram:tmp1AB} Hold 2nd noun for now
0D3F: 34 10               PSHS    X                         ; Hold script
0D41: B7 01 C3            STA     $01C3                     ; {ram:FIRST_NOUN_NUM} Temporary 1st noun
0D44: 1F 89               TFR     A,B                       ; To B (for lookup)
0D46: 27 06               BEQ     $D4E                      ; Not one ... skip
0D48: BD 11 7D            JSR     $117D                     ; Lookup object in B
0D4B: BF 01 C6            STX     $01C6                     ; {ram:FIRST_NOUN_DATA} Temporary 1st noun data
0D4E: F6 01 AB            LDB     $01AB                     ; {ram:tmp1AB} Temporary 2nd noun ...
0D51: F7 01 C9            STB     $01C9                     ; {ram:SECOND_NOUN_NUM} ... index
0D54: 27 06               BEQ     $D5C                      ; There isn't one ... skip
0D56: BD 11 7D            JSR     $117D                     ; Lookup object in B
0D59: BF 01 CC            STX     $01CC                     ; {ram:SECOND_NOUN_DATA} Temporary 2nd noun
0D5C: 8E 2F 24            LDX     #$2F24                    ; General commands
0D5F: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip ID and length
0D62: BD 0C 44            JSR     $0C44                     ; {ProcessCommand} Execute general script
0D65: 1F A8               TFR     CCR,A                     ; Hold the result ...
0D67: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} ... for a moment
0D6A: 35 20               PULS    Y                         ;
0D6C: 35 02               PULS    A                         ;
0D6E: B7 01 D1            STA     $01D1                     ; {ram:PHRASE_FORM} Restore ...
0D71: 35 06               PULS    A,B                       ; ... phrase ...
0D73: F7 01 C3            STB     $01C3                     ; {ram:FIRST_NOUN_NUM} ... and ...
0D76: B7 01 C9            STA     $01C9                     ; {ram:SECOND_NOUN_NUM} ... nouns
0D79: 35 40               PULS    U                         ;
0D7B: FF 01 CC            STU     $01CC                     ; {ram:SECOND_NOUN_DATA} 
0D7E: 35 40               PULS    U                         ;
0D80: FF 01 C6            STU     $01C6                     ; {ram:FIRST_NOUN_DATA} 
0D83: 1E 12               EXG     X,Y                       ;
0D85: B6 01 AB            LDA     $01AB                     ; {ram:tmp1AB} 
0D88: 1F 8A               TFR     A,CCR                     ; Restore result
0D8A: 39                  RTS                               ; Done

; Print "YOU ARE IN" + description + objects if active object is Player
; Print just description if active object is SYSTEM.
0D8B: B6 01 D2            LDA     $01D2                     ; {ram:ACTIVE_OBJ_NUM} Active object number
0D8E: 81 38               CMPA    #$38                      ; Is this the SYSTEM object?
0D90: 27 04               BEQ     $D96                      ; Yes ... keep going OK
0D92: 81 13               CMPA    #$13                      ; Is it the Player object?
0D94: 26 F4               BNE     $D8A                      ; No ... error out
0D96: BE 01 D6            LDX     $01D6                     ; {ram:CUR_ROOM_DATA} Current room script
0D99: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip length
0D9C: 30 01               LEAX    1,X                       ;
0D9E: C6 03               LDB     #$03                      ; You are in DESCRIPTION script
0DA0: BD 0A 68            JSR     $0A68                     ; Get room description
0DA3: 24 1F               BCC     $DC4                      ; No room description ... print objects in room
0DA5: B6 01 D2            LDA     $01D2                     ; {ram:ACTIVE_OBJ_NUM} Active object
0DA8: 81 38               CMPA    #$38                      ; Is it the SYSTEM object?
0DAA: 27 0A               BEQ     $DB6                      ; Skip leading "THIS IS" or "YOU ARE IN"
0DAC: 34 10               PSHS    X                         ; Hold script
0DAE: 8E 0E 23            LDX     #$0E23                    ; "THIS IS" or "YOU ARE IN" preamble
0DB1: BD 0C 44            JSR     $0C44                     ; {ProcessCommand} Execute preamble script
0DB4: 35 10               PULS    X                         ; Restore script
0DB6: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip script length
0DB9: BD 0C 44            JSR     $0C44                     ; {ProcessCommand} Execute description script
0DBC: B6 01 D2            LDA     $01D2                     ; {ram:ACTIVE_OBJ_NUM} Active object
0DBF: 81 38               CMPA    #$38                      ; Is this the SYSTEM object?
0DC1: 26 01               BNE     $DC4                      ; No ... print objects in room
0DC3: 39                  RTS                               ; Done
;
; Print object descriptions
;
0DC4: 8E 1B 42            LDX     #$1B42                    ; Object data
0DC7: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip length
0DCA: 34 20               PSHS    Y                         ; Hold end
0DCC: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip this object's length
0DCF: B6 01 D5            LDA     $01D5                     ; {ram:CUR_ROOM} Current room
0DD2: A1 84               CMPA    ,X                        ; Object in room?
0DD4: 26 41               BNE     $E17                      ; No ... next object
0DD6: 30 02               LEAX    2,X                       ; Skip to data
0DD8: A6 80               LDA     ,X+                       ; Get object data
0DDA: 34 02               PSHS    A                         ; Hold value
0DDC: C6 03               LDB     #$03                      ; Get description ...
0DDE: BD 0A 68            JSR     $0A68                     ; ... script
0DE1: 24 32               BCC     $E15                      ; No script ... skip to next object
0DE3: 34 20               PSHS    Y                         ; Hold end of object
0DE5: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip length
0DE8: BD 0C 44            JSR     $0C44                     ; {ProcessCommand} Print object description
0DEB: 35 20               PULS    Y                         ; Restore end of object
0DED: 35 02               PULS    A                         ; Get back ...
0DEF: 34 02               PSHS    A                         ; ... object data
0DF1: 84 08               ANDA    #$08                      ; Open/close-able?
0DF3: 27 20               BEQ     $E15                      ; No ... no need for further status
0DF5: 35 02               PULS    A                         ; Get back ...
0DF7: 34 02               PSHS    A                         ; ... object data
0DF9: 84 0A               ANDA    #$0A                      ; We already checked 08 bit, but OK ...
0DFB: 88 0A               EORA    #$0A                      ; ... see if object is in open state
0DFD: 26 0C               BNE     $E0B                      ; Yes ... skip "which is closed" and print period
0DFF: 34 20               PSHS    Y                         ; Hold end of object
0E01: 8E 0E 21            LDX     #$0E21                    ; "WHICH IS CLOSED."
0E04: BD 0C 44            JSR     $0C44                     ; {ProcessCommand} Print door closed status.
0E07: 35 20               PULS    Y                         ; Restore end of object
0E09: 20 0A               BRA     $E15                      ; Next object
0E0B: 34 20               PSHS    Y                         ; Hold end of object
0E0D: 8E 0E 22            LDX     #$0E22                    ; ".  "
0E10: BD 0C 44            JSR     $0C44                     ; {ProcessCommand} Print period and 2 spaces
0E13: 35 20               PULS    Y                         ; Next object pointer
0E15: 35 02               PULS    A                         ; Discard object data
0E17: 1E 12               EXG     X,Y                       ; Move to next object
0E19: 35 20               PULS    Y                         ; End of object data
0E1B: BD 0A 99            JSR     $0A99                     ; {CompareXY} Are we at the end of objects?
0E1E: 25 AA               BCS     $DCA                      ; No ... go back and do all
0E20: 39                  RTS                               ; Done
;
0E21: 8A  ; "WHICH IS CLOSED."
0E22: 8B  ; ".  "
0E23: 8C  ; "THIS IS" or "YOU ARE IN"

Com_01_is_in_pack_or_current_room:
; is_in_pack_or_current_room(object)
0E24: E6 80               LDB     ,X+                       ; Get object number from script
0E26: 34 10               PSHS    X                         ; Hold script pointer
0E28: BD 11 7D            JSR     $117D                     ; Get object data
0E2B: BD 08 EB            JSR     $08EB                     ; See if it is in pack or room
0E2E: 35 10               PULS    X                         ; Restore script
0E30: 39                  RTS                               ; Out

Com_20_is_ACTIVE_this:
; is_ACTIVE_this(object)
0E31: B6 01 D2            LDA     $01D2                     ; {ram:ACTIVE_OBJ_NUM} Active object
0E34: A1 80               CMPA    ,X+                       ; Matches target?
0E36: 39                  RTS                               ; Done

Com_2C_set_ACTIVE:
; set_ACTIVE(object)
0E37: E6 80               LDB     ,X+                       ; Get number from script
0E39: 34 10               PSHS    X                         ; Hold script
0E3B: F7 01 D2            STB     $01D2                     ; {ram:ACTIVE_OBJ_NUM} Set active object number
0E3E: BD 11 7D            JSR     $117D                     ; Get data
0E41: BF 01 D3            STX     $01D3                     ; {ram:ACTIVE_OBJ_DATA} Set active object data
0E44: 35 10               PULS    X                         ; Restore script
0E46: 4F                  CLRA                              ; Return OK
0E47: 39                  RTS                               ; Done

Com_02_is_owned_by_ACTIVE:
; is_owned_by_ACTIVE(object)
0E48: E6 80               LDB     ,X+                       ; Get object number from script
0E4A: 7E 10 4A            JMP     $104A                     ; Make sure this object is owned by active object

Com_03_is_located:
; is_located(room,object)
; Check to see if an object is at a target location.
0E4D: EC 81               LDD     ,X++                      ; Room and object
0E4F: 34 10               PSHS    X                         ; Hold script
0E51: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Remember the room
0E54: BD 11 7D            JSR     $117D                     ; Locate the object
0E57: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip the length
0E5A: EC 81               LDD     ,X++                      ; Get the room to A
0E5C: B1 01 AB            CMPA    $01AB                     ; {ram:tmp1AB} Is this object in the target place?
0E5F: 35 10               PULS    X                         ; Restore script
0E61: 39                  RTS                               ; Out

Com_0C_fail:
; fail()
; Always fail
0E62: 8A 01               ORA     #$01                      ; Set the fail flag
0E64: 39                  RTS                               ; Done

Com_04_print:
; print(msg)
0E65: B6 01 D2            LDA     $01D2                     ; {ram:ACTIVE_OBJ_NUM} Active object
0E68: 81 38               CMPA    #$38                      ; Is this the SYSTEM?
0E6A: 27 19               BEQ     $E85                      ; Yes ... do print
0E6C: 81 13               CMPA    #$13                      ; Is this the Player?
0E6E: 26 0E               BNE     $E7E                      ; No ... skip printing

Com_1F_print2:
; print2(msg)
0E70: C6 13               LDB     #$13                      ; Player number
0E72: 34 10               PSHS    X                         ; Hold script
0E74: BD 11 7D            JSR     $117D                     ; Look up Player
0E77: BD 08 EB            JSR     $08EB                     ; Is Player in current room?
0E7A: 35 10               PULS    X                         ; Restore
0E7C: 27 07               BEQ     $E85                      ; Yes ... do printing
0E7E: BD 0A 85            JSR     $0A85                     ; {LoadEnd} Skip to ...
0E81: 1E 12               EXG     X,Y                       ; ... end of packed message.
0E83: 20 03               BRA     $E88                      ; Return OK but no printing
0E85: BD 11 99            JSR     $1199                     ; {PrintPackedMessage} Print packed message at X
0E88: 4F                  CLRA                              ; OK
0E89: 39                  RTS                               ; Done

Com_07_print_room_description:
; print_room_description()
0E8A: BD 0D 8B            JSR     $0D8B                     ; Print room description
0E8D: 4F                  CLRA                              ; OK
0E8E: 39                  RTS                               ; Done

Com_06_print_inventory:
; print_inventory()
0E8F: 34 10               PSHS    X                         ; Hold script pointer
0E91: 86 0D               LDA     #$0D                      ; Print ...
0E93: BD 11 D5            JSR     $11D5                     ; {PrintCharacterAutoWrap} ... CR
0E96: 8E 1B 42            LDX     #$1B42                    ; Objects
0E99: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip size of objects
;
0E9C: BD 0A 99            JSR     $0A99                     ; {CompareXY} CompareXY
0E9F: 24 2A               BCC     $ECB                      ; End of list ... out
0EA1: 34 20               PSHS    Y                         ; Hold end of master list of objects
0EA3: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Get pointer to next object
0EA6: E6 84               LDB     ,X                        ; Object location
0EA8: F1 01 D2            CMPB    $01D2                     ; {ram:ACTIVE_OBJ_NUM} Active object?
0EAB: 26 18               BNE     $EC5                      ; No ... skip this object
0EAD: 30 02               LEAX    2,X                       ; Do ...
0EAF: A6 80               LDA     ,X+                       ; ... we print ...
0EB1: 84 20               ANDA    #$20                      ; ... shortname?
0EB3: 27 10               BEQ     $EC5                      ; No ... skip
0EB5: C6 02               LDB     #$02                      ; Find data #2 ...
0EB7: BD 0A 68            JSR     $0A68                     ; ... the short-name
0EBA: 24 09               BCC     $EC5                      ; Not found ... out
0EBC: 30 01               LEAX    1,X                       ; Skip the 02 data id
0EBE: 34 20               PSHS    Y                         ; Hold next-object
0EC0: BD 11 8D            JSR     $118D                     ; Print packed message and CR
0EC3: 35 20               PULS    Y                         ; Restore next-object
0EC5: 1E 12               EXG     X,Y                       ; Move to next object
0EC7: 35 20               PULS    Y                         ; End of master list
0EC9: 20 D1               BRA     $E9C                      ; Do all objects
0ECB: 4F                  CLRA                              ; Success
0ECC: 35 10               PULS    X                         ; Restore script pointer
0ECE: 39                  RTS                               ; Done

Com_08_is_first_noun:
; is_first_noun(object)
0ECF: FE 01 C6            LDU     $01C6                     ; {ram:FIRST_NOUN_DATA} 1st noun data
0ED2: B6 01 C3            LDA     $01C3                     ; {ram:FIRST_NOUN_NUM} 1st noun number
;
0ED5: FF 01 D8            STU     $01D8                     ; {ram:nextToken} Hold
0ED8: 4D                  TSTA                              ; Is there an object?
0ED9: 27 10               BEQ     $EEB                      ; No ... error
0EDB: E6 80               LDB     ,X+                       ; Object number from script
0EDD: 34 10               PSHS    X                         ; Hold script
0EDF: BD 11 7D            JSR     $117D                     ; Find object
0EE2: 1E 12               EXG     X,Y                       ; Pointer of found object to Y
0EE4: 35 10               PULS    X                         ; Restore script pointer
0EE6: 10 BC 01 D8         CMPY    $01D8                     ; {ram:nextToken} Object the same?
0EEA: 39                  RTS                               ; Done
0EEB: 5D                  TSTB                              ; B can't be 0 ... Z=0 error
0EEC: 39                  RTS                               ; Done

Com_09_compare_to_second_noun:
; compare_to_second_noun(object)
0EED: FE 01 CC            LDU     $01CC                     ; {ram:SECOND_NOUN_DATA} 2nd noun data
0EF0: B6 01 C9            LDA     $01C9                     ; {ram:SECOND_NOUN_NUM} 2nd noun number
0EF3: 20 E0               BRA     $ED5                      ; Do compare
        
Com_2D_is_VAR:
; is_VAR(object)
0EF5: FE 01 C0            LDU     $01C0                     ; {ram:VAR_OBJ_DATA} Var noun data
0EF8: B6 01 BF            LDA     $01BF                     ; {ram:VAR_OBJ_NUMBER} Var noun number
0EFB: 7E 0E D5            JMP     $0ED5                     ; Do compare

Com_0A_compare_input_to:
; compare_input_to(phrase)
0EFE: E6 80               LDB     ,X+                       ; Compare from script ...
0F00: F1 01 D1            CMPB    $01D1                     ; {ram:PHRASE_FORM} ... to phrase form
0F03: 39                  RTS                               ; Done

Com_0F_pick_up_VAR:
; pick_up_VAR()
; Move noun object to pack.
0F04: 34 10               PSHS    X                         ; Hold script
0F06: BE 01 C0            LDX     $01C0                     ; {ram:VAR_OBJ_DATA} Pointer to noun object
0F09: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip length
0F0C: B6 01 D2            LDA     $01D2                     ; {ram:ACTIVE_OBJ_NUM} Back pack "location" value
0F0F: A7 84               STA     ,X                        ; Move object to pack
0F11: 4F                  CLRA                              ; OK
0F12: 35 10               PULS    X                         ; Restore script
0F14: 39                  RTS                               ; Done

Com_10_drop_VAR:
; drop_VAR()
; Move noun object to current room.
0F15: 34 10               PSHS    X                         ; Hold script
0F17: BE 01 C0            LDX     $01C0                     ; {ram:VAR_OBJ_DATA} Pointer to noun object
0F1A: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip length
0F1D: B6 01 D5            LDA     $01D5                     ; {ram:CUR_ROOM} Current room
0F20: A7 84               STA     ,X                        ; Move object to room
0F22: 35 10               PULS    X                         ; Restore script
0F24: 4F                  CLRA                              ; Done
0F25: 39                  RTS                               ; Out

Com_13_process_phrase_by_room_first_second:
; process_phrase_by_room_first_second()
0F26: 34 10               PSHS    X                         ; Save script
0F28: BE 01 D6            LDX     $01D6                     ; {ram:CUR_ROOM_DATA} Current room script
0F2B: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip id and length
0F2E: 30 01               LEAX    1,X                       ; Skip
0F30: C6 04               LDB     #$04                      ; Get ...
0F32: BD 0A 68            JSR     $0A68                     ; ... phrase script
0F35: 24 08               BCC     $F3F                      ; No phrase script ... skip
0F37: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip id and length
0F3A: BD 0C 44            JSR     $0C44                     ; {ProcessCommand} Execute
0F3D: 27 3B               BEQ     $F7A                      ; Move passed ... OK and out
0F3F: B6 01 C9            LDA     $01C9                     ; {ram:SECOND_NOUN_NUM} Is there a 2nd noun?
0F42: 27 17               BEQ     $F5B                      ; No ... skip
0F44: BE 01 CC            LDX     $01CC                     ; {ram:SECOND_NOUN_DATA} Second noun data
0F47: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip ...
0F4A: 30 03               LEAX    3,X                       ; ... object header
0F4C: C6 06               LDB     #$06                      ; Get "noun is second" ...
0F4E: BD 0A 68            JSR     $0A68                     ; ... phrase script
0F51: 24 08               BCC     $F5B                      ; None ... move on
0F53: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip header
0F56: BD 0C 44            JSR     $0C44                     ; {ProcessCommand} Execute script
0F59: 27 1F               BEQ     $F7A                      ; Script passed ... OK and out
0F5B: B6 01 C3            LDA     $01C3                     ; {ram:FIRST_NOUN_NUM} Is there a 1st noun?
0F5E: 26 05               BNE     $F65                      ; Yes ... go do it
0F60: 35 10               PULS    X                         ; Restore script
0F62: 8A 01               ORA     #$01                      ; Nobody took the phrase ..
0F64: 39                  RTS                               ; .. error and and out
0F65: BE 01 C6            LDX     $01C6                     ; {ram:FIRST_NOUN_DATA} First noun data
0F68: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip ...
0F6B: 30 03               LEAX    3,X                       ; ... object header
0F6D: C6 07               LDB     #$07                      ; Get "noun is first" ...
0F6F: BD 0A 68            JSR     $0A68                     ; ... phrase script
0F72: 24 EC               BCC     $F60                      ; None ... error and out
0F74: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip the id and length
0F77: BD 0C 44            JSR     $0C44                     ; {ProcessCommand} Execute script (use return)
0F7A: 35 10               PULS    X                         ; Restore script pointer
0F7C: 39                  RTS                               ; Done

Com_16_print_VAR:
; print_VAR()
0F7D: 34 10               PSHS    X                         ; Save script pointer
0F7F: BE 01 C0            LDX     $01C0                     ; {ram:VAR_OBJ_DATA} Var noun data
0F82: B6 01 BF            LDA     $01BF                     ; {ram:VAR_OBJ_NUMBER} Var noun index
0F85: 20 08               BRA     $F8F                      ; Print short name

Com_11_print_first_noun:
; print_first_noun()
0F87: 34 10               PSHS    X                         ; Save script pointer
0F89: BE 01 C6            LDX     $01C6                     ; {ram:FIRST_NOUN_DATA} 1st noun data
0F8C: B6 01 C3            LDA     $01C3                     ; {ram:FIRST_NOUN_NUM} 1st noun index
;
0F8F: 27 E9               BEQ     $F7A                      ; Return Z=1 return
0F91: C6 13               LDB     #$13                      ; User object
0F93: 34 10               PSHS    X                         ; Hold noun data
0F95: BD 11 7D            JSR     $117D                     ; Lookup user object
0F98: BD 08 EB            JSR     $08EB                     ; User in current room?
0F9B: 35 10               PULS    X                         ; Restore noun data
0F9D: 26 11               BNE     $FB0                      ; Not in current room ... skip print
0F9F: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip object ...
0FA2: 30 03               LEAX    3,X                       ; ... header
0FA4: C6 02               LDB     #$02                      ; Get object ...
0FA6: BD 0A 68            JSR     $0A68                     ; ... short name
0FA9: 24 05               BCC     $FB0                      ; No short name ... out with OK
0FAB: 30 01               LEAX    1,X                       ; Skip the 2
0FAD: BD 11 99            JSR     $1199                     ; {PrintPackedMessage} Print packed message at X
0FB0: 35 10               PULS    X                         ; Restore script
0FB2: 4F                  CLRA                              ; Return ...
0FB3: 39                  RTS                               ; ... OK

Com_12_print_second_noun:
; print_second_noun()
0FB4: 34 10               PSHS    X                         ; Save script pointer
0FB6: BE 01 CC            LDX     $01CC                     ; {ram:SECOND_NOUN_DATA} 2nd noun data
0FB9: B6 01 C9            LDA     $01C9                     ; {ram:SECOND_NOUN_NUM} 2nd noun index
0FBC: 20 D1               BRA     $F8F                      ; Print short name

Com_15_check_VAR:
; check_VAR(bits)
; Check target bits in an object.
0FBE: 34 10               PSHS    X                         ; Hold script pointer
0FC0: BE 01 C0            LDX     $01C0                     ; {ram:VAR_OBJ_DATA} Input object pointer
0FC3: B6 01 BF            LDA     $01BF                     ; {ram:VAR_OBJ_NUMBER} Var object number
0FC6: 27 0E               BEQ     $FD6                      ; No object ... return error
0FC8: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip the pointer-to-next object
0FCB: 30 02               LEAX    2,X                       ; Skip to data byte
0FCD: A6 84               LDA     ,X                        ; Get the object data
0FCF: 35 10               PULS    X                         ; Restore the script
0FD1: A4 84               ANDA    ,X                        ; Mask off all but target bits
0FD3: A8 80               EORA    ,X+                       ; Check target bits  (a 1 result in a pass)
0FD5: 39                  RTS                               ; Done
;
0FD6: 35 10               PULS    X                         ; Restore script pointer
0FD8: 30 01               LEAX    1,X                       ; Skip data
0FDA: 8A 01               ORA     #$01                      ; Set error
0FDC: 39                  RTS                               ; Return

Com_29_toggle_open_VAR:
; toggle_open_VAR()
; Toggle open/closed bit on object.
0FDD: 34 10               PSHS    X                         ; Hold script pointer
0FDF: BE 01 C0            LDX     $01C0                     ; {ram:VAR_OBJ_DATA} Input object pointer
0FE2: B6 01 BF            LDA     $01BF                     ; {ram:VAR_OBJ_NUMBER} Var object number
0FE5: 10 27 FF 77         LBEQ    $0F60                     ; No object ... return error
0FE9: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip the pointer-to-next object
0FEC: 30 02               LEAX    2,X                       ; Skip to data byte
0FEE: A6 84               LDA     ,X                        ; Get the value
0FF0: 88 02               EORA    #$02                      ; Flip "open/closed" bit
0FF2: A7 84               STA     ,X                        ; Store the new value
0FF4: 35 10               PULS    X                         ; Restore script
0FF6: 4F                  CLRA                              ; OK
0FF7: 39                  RTS                               ; Done

Com_2A_toggle_lock_VAR:
; toggle_lock_VAR()
; Toggle locked/unlocked bit on object.
0FF8: 34 10               PSHS    X                         ; Hold script pointer
0FFA: BE 01 C0            LDX     $01C0                     ; {ram:VAR_OBJ_DATA} Input object pointer
0FFD: B6 01 BF            LDA     $01BF                     ; {ram:VAR_OBJ_NUMBER} Var object number
1000: 10 27 FF 5C         LBEQ    $0F60                     ; No object ... return error
1004: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip the pointer-to-next object
1007: 30 02               LEAX    2,X                       ; Skip to data byte
1009: A6 84               LDA     ,X                        ; Get the value
100B: 88 01               EORA    #$01                      ; Flip "locked/unlocked" bit
100D: A7 84               STA     ,X                        ; Store the new value
100F: 35 10               PULS    X                         ; Restore script
1011: 4F                  CLRA                              ; OK
1012: 39                  RTS                               ; Done

Com_14_execute_and_reverse_status:
; execute_and_reverse_status:
1013: BD 0C 44            JSR     $0C44                     ; {ProcessCommand} Execute command
1016: 26 03               BNE     $101B                     ; Command returned a non-zero ... return zero
1018: 8A 01               ORA     #$01                      ; Command returned a zero ... return non-zerio
101A: 39                  RTS                               ; Done
101B: 4F                  CLRA                              ; Zero
101C: 39                  RTS                               ; Done

Com_17_move_to:
; move_to(object,room)
101D: E6 80               LDB     ,X+                       ; Get object number
101F: 34 10               PSHS    X                         ; Hold script
1021: BD 11 7D            JSR     $117D                     ; Find object
1024: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip over length
1027: 35 20               PULS    Y                         ; Script to Y
1029: A6 A0               LDA     ,Y+                       ; Get new location
102B: A7 84               STA     ,X                        ; Set object's new location
102D: 1E 12               EXG     X,Y                       ; X now past data
102F: 4F                  CLRA                              ; OK
1030: 39                  RTS                               ; Done

Com_18_is_VAR_owned_by_ACTIVE:
; is_VAR_owned_by_ACTIVE()
1031: 34 10               PSHS    X                         ; Save script pointer
1033: BE 01 C0            LDX     $01C0                     ; {ram:VAR_OBJ_DATA} Var object data
1036: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip length
1039: E6 84               LDB     ,X                        ; Location
103B: 35 10               PULS    X                         ; Restore script
103D: 10 27 F8 CF         LBEQ    $0910                     ; Out-of-game ... error and out
1041: F1 01 D2            CMPB    $01D2                     ; {ram:ACTIVE_OBJ_NUM} Is this the active object?
1044: 27 EA               BEQ     $1030                     ; Yes ... return OK
1046: C5 80               BITB    #$80                      ; Test upper bit
1048: 26 E6               BNE     $1030                     ; It is in a room ... error and out
;
104A: 34 10               PSHS    X                         ; Hold script
104C: BD 11 7D            JSR     $117D                     ; Look up owner object
104F: 20 E5               BRA     $1036                     ; Check again
```

# Every Turn

```code
; Execute any turn-scripts on the objects
EveryTurn:  
1051: 8E 1B 42            LDX     #$1B42                    ; Start of object data
1054: 7F 01 D0            CLR     $01D0                     ; {ram:tmp1DO} Object number
1057: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip length
105A: BD 0A 99            JSR     $0A99                     ; {CompareXY} End of objects?
105D: 24 D1               BCC     $1030                     ; Yes ... out
105F: 7C 01 D0            INC     $01D0                     ; {ram:tmp1DO} Next object number
1062: 34 20               PSHS    Y                         ; Hold end-of-objects
1064: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip length
1067: A6 84               LDA     ,X                        ; Location
1069: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Hold
106C: 34 20               PSHS    Y                         ; End of object
106E: A6 84               LDA     ,X                        ; Location
1070: 27 42               BEQ     $10B4                     ; If it is out-of-game it doesn't get a turn
1072: 30 03               LEAX    3,X                       ; Skip data
1074: C6 08               LDB     #$08                      ; Turn-script
1076: BD 0A 68            JSR     $0A68                     ; Find turn script
1079: 24 39               BCC     $10B4                     ; Nothing to do ... next object
107B: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip length
107E: 34 10               PSHS    X                         ; Hold pointer
1080: BD 13 19            JSR     $1319                     ; {Com_2B_GenerateRandomNumber} Generate random number
1083: F6 01 D0            LDB     $01D0                     ; {ram:tmp1DO} Current object number ...
1086: F7 01 D2            STB     $01D2                     ; {ram:ACTIVE_OBJ_NUM} ... is now the active object
1089: BD 11 7D            JSR     $117D                     ; Get its data pointer
108C: BF 01 D3            STX     $01D3                     ; {ram:ACTIVE_OBJ_DATA} Hold pointer to active object data
108F: F6 01 AB            LDB     $01AB                     ; {ram:tmp1AB} Object's location
1092: 5D                  TSTB                              ; Check upper bit
1093: 2B 0E               BMI     $10A3                     ; If in a room ... go handle
1095: BD 11 7D            JSR     $117D                     ; Get object's owner
1098: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip length
109B: E6 84               LDB     ,X                        ; Get owner location
109D: 26 F3               BNE     $1092                     ; Still in game ... find room location of owner chain
109F: 35 10               PULS    X                         ; Restore pointer
10A1: 20 11               BRA     $10B4                     ; Next object
10A3: F7 01 D5            STB     $01D5                     ; {ram:CUR_ROOM} Objects location
10A6: 8E 15 A1            LDX     #$15A1                    ; Get room ...
10A9: BD 0A 60            JSR     $0A60                     ; {FindSublist} ... scripts for object
10AC: BF 01 D6            STX     $01D6                     ; {ram:CUR_ROOM_DATA} Hold
10AF: 35 10               PULS    X                         ; Restore turn-script
10B1: BD 0C 44            JSR     $0C44                     ; {ProcessCommand} Execute turn-script
10B4: 35 10               PULS    X                         ; Restore
10B6: 35 20               PULS    Y                         ; Restore
10B8: 20 A0               BRA     $105A                     ; Next object

Com_05_is_less_equal_last_random:
; is_less_equal_last_random(value)
10BA: B6 13 B8            LDA     $13B8                     ; Random value
10BD: A1 80               CMPA    ,X+                       ; Compare random value to script
10BF: 25 05               BCS     $10C6                     ; If less than ... OK
10C1: 27 03               BEQ     $10C6                     ; If the same ... OK
10C3: 8A 01               ORA     #$01                      ; Greater than ... FAIL
10C5: 39                  RTS                               ; Done
10C6: 4F                  CLRA                              ; Less than or equal ... OK
10C7: 39                  RTS                               ; Done

Com_1D_attack_VAR:
; attack_VAR(points)
10C8: A6 80               LDA     ,X+                       ; Get attack value
10CA: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Hold attack value
10CD: 34 10               PSHS    X                         ; Hold script
10CF: BE 01 C0            LDX     $01C0                     ; {ram:VAR_OBJ_DATA} Target object data
10D2: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip length
10D5: 30 03               LEAX    3,X                       ; Skip object data
10D7: 34 10               PSHS    X                         ; Hold X ...
10D9: 34 20               PSHS    Y                         ; ... and Y
10DB: C6 09               LDB     #$09                      ; Get target's ...
10DD: BD 0A 68            JSR     $0A68                     ; ... combat info
10E0: 24 29               BCC     $110B                     ; Not found. Do nothing (return OK)
10E2: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip length
10E5: 30 01               LEAX    1,X                       ; Hit points
10E7: A6 84               LDA     ,X                        ; Hit points
10E9: B0 01 AB            SUBA    $01AB                     ; {ram:tmp1AB} Subtract attack from hit points
10EC: 24 01               BCC     $10EF                     ; Not negative ... keep it
10EE: 4F                  CLRA                              ; Floor the hit points
10EF: A7 84               STA     ,X                        ; New hit points
10F1: 35 20               PULS    Y                         ; Restore ...
10F3: 35 10               PULS    X                         ; ... X and Y
10F5: 4D                  TSTA                              ; Hit points zero?
10F6: 27 04               BEQ     $10FC                     ; Yes ... object dies
10F8: 35 10               PULS    X                         ; Restore list
10FA: 4F                  CLRA                              ; Return OK
10FB: 39                  RTS                               ; Done

;Handle object being killed
10FC: C6 0A               LDB     #$0A                      ; Object being killed script
10FE: BD 0A 68            JSR     $0A68                     ; Find a script for handling being killed
1101: 24 F5               BCC     $10F8                     ; Not found ... nothing happens (return OK)
1103: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip id and length
1106: BD 0C 44            JSR     $0C44                     ; {ProcessCommand} Execute "being killed" script
1109: 20 ED               BRA     $10F8                     ; Done (return OK)

110B: 35 20               PULS    Y                         ; Reset ...
110D: 35 10               PULS    X                         ; ... stack
110F: 20 E7               BRA     $10F8                     ; Return OK

Com_1E_swap:
; swap(object_a,object_b)
1111: E6 80               LDB     ,X+                       ; 1st object number
1113: A6 80               LDA     ,X+                       ; 2nd object
1115: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Hold second object
1118: 34 10               PSHS    X                         ; Hold script
111A: BD 11 7D            JSR     $117D                     ; Look up object
111D: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip length
1120: 1F 13               TFR     X,U                       ; 1st object pointer to U
1122: F6 01 AB            LDB     $01AB                     ; {ram:tmp1AB} 2nd object
1125: BD 11 7D            JSR     $117D                     ; Look up object
1128: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip length
112B: A6 84               LDA     ,X                        ; Swap ...
112D: E6 C4               LDB     ,U                        ; ... location ...
112F: A7 C4               STA     ,U                        ; ... of ...
1131: E7 84               STB     ,X                        ; ... objects
1133: 35 10               PULS    X                         ; Restore script
1135: 4F                  CLRA                              ; OK
1136: 39                  RTS                               ; Done

1137: 35 10               PULS    X                         ; Restore script pointer
1139: 4F                  CLRA                              ; Z=1 OK
113A: 39                  RTS                               ; Done

Com_23_heal_VAR:
; heal_VAR(points)
113B: A6 80               LDA     ,X+                       ; Get healing value
113D: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Hold it
1140: 34 10               PSHS    X                         ; Hold script
1142: BE 01 C0            LDX     $01C0                     ; {ram:VAR_OBJ_DATA} Var object data
1145: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip length
1148: 30 03               LEAX    3,X                       ; Skip data
114A: C6 09               LDB     #$09                      ; Get object ...
114C: BD 0A 68            JSR     $0A68                     ; ... hit points
114F: 24 E6               BCC     $1137                     ; No entry ... do nothing (but OK)
1151: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip length
1154: EC 84               LDD     ,X                        ; Get HP info
1156: FB 01 AB            ADDB    $01AB                     ; {ram:tmp1AB} Add to health
1159: B7 01 AB            STA     $01AB                     ; {ram:tmp1AB} Max value
115C: F1 01 AB            CMPB    $01AB                     ; {ram:tmp1AB} Over the max?
115F: 25 03               BCS     $1164                     ; No ... keep it
1161: F6 01 AB            LDB     $01AB                     ; {ram:tmp1AB} Use max value
1164: 30 01               LEAX    1,X                       ; Store ...
1166: E7 84               STB     ,X                        ; ... new health
1168: 20 CD               BRA     $1137                     ; OK out

Com_28_save_game:
; save_game()
116A: B6 01 D2            LDA     $01D2                     ; {ram:ACTIVE_OBJ_NUM} Active object
116D: 81 13               CMPA    #$13                      ; Is this the Player?
116F: 26 08               BNE     $1179                     ; No ... ignore
1171: 7A 01 E3            DEC     $01E3                     ; {ram:tillMORE} Decrement rows-till-more-prompt
1174: 86 0D               LDA     #$0D                      ; Print ...
1176: BD 11 D5            JSR     $11D5                     ; {PrintCharacterAutoWrap} ... CR
1179: 4F                  CLRA                              ; OK
117A: 39                  RTS                               ; Done

Com_24_endless_loop:
; endless_loop()
117B: 20 FE               BRA     $117B                     ; {Com_24_EndlessLoop} Endless loop

; Find object index in B
117D: 8E 1B 42            LDX     #$1B42                    ; Start of objects
1180: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Skip end
1183: 5A                  DECB                              ; Found desired object?
1184: 27 F4               BEQ     $117A                     ; Yes ... out OK
1186: BD 0A 83            JSR     $0A83                     ; {SkipIDLoadEnd} Length of object
1189: 1E 12               EXG     X,Y                       ; Next object
118B: 20 F6               BRA     $1183                     ; Keep looking

; Print packed message and CR
118D: BD 11 99            JSR     $1199                     ; {PrintPackedMessage} Print packed message at X
1190: 86 0D               LDA     #$0D                      ; Print ...
1192: BD 11 D5            JSR     $11D5                     ; {PrintCharacterAutoWrap} ... CR
1195: 7A 01 E3            DEC     $01E3                     ; {ram:tillMORE} Rows till MORE PROMPT
1198: 39                  RTS                               ; Done

PrintPackedMessage:
; X points to compressed string. First byte (or two) is the length.
1199: 4F                  CLRA                              ; Assume MSB is 0
119A: E6 84               LDB     ,X                        ; Get length
119C: C5 80               BITB    #$80                      ; Is it single byte length?
119E: 27 04               BEQ     $11A4                     ; Yes ... use D
11A0: A6 80               LDA     ,X+                       ; Get the ...
11A2: 84 7F               ANDA    #$7F                      ; ... MSB and ...
11A4: E6 80               LDB     ,X+                       ; ... LSB
11A6: FD 01 AB            STD     $01AB                     ; {ram:tmp1AB} Store byte count
11A9: FC 01 AB            LDD     $01AB                     ; {ram:tmp1AB} Number of bytes left in message
11AC: 10 83 00 02         CMPD    #$0002                    ; Less than 2?
11B0: 25 0E               BCS     $11C0                     ; Yes ... these aren't compressed
11B2: BD 12 59            JSR     $1259                     ; {UnpackBytes} Decompress and print two bytes pointed to by X
11B5: FC 01 AB            LDD     $01AB                     ; {ram:tmp1AB} Get byte count
11B8: 83 00 02            SUBD    #$0002                    ; Handled 2
11BB: FD 01 AB            STD     $01AB                     ; {ram:tmp1AB} Store count
11BE: 20 E9               BRA     $11A9                     ; Keep decompressing
11C0: 5D                  TSTB                              ; Any characters on the end to print?
11C1: 27 0C               BEQ     $11CF                     ; No ... skip
11C3: A6 80               LDA     ,X+                       ; Get character
11C5: 34 04               PSHS    B                         ; Hold count
11C7: BD 11 D5            JSR     $11D5                     ; {PrintCharacterAutoWrap} Print character
11CA: 35 04               PULS    B                         ; Restore count
11CC: 5A                  DECB                              ; Decrement count
11CD: 20 F1               BRA     $11C0                     ; Keep going
11CF: 86 20               LDA     #$20                      ; Print ...
11D1: BD 11 D5            JSR     $11D5                     ; {PrintCharacterAutoWrap} ... space on end
11D4: 39                  RTS                               ; Done
```

# Print Character

```code
PrintCharacterAutoWrap:
; Print character in A to screen. This handles auto word-wrapping and
; auto MORE prompting.
;
11D5: F6 01 BE            LDB     $01BE                     ; {ram:lastChar} Last printed character
11D8: C1 20               CMPB    #$20                      ; Last printed a space?
11DA: 26 16               BNE     $11F2                     ; No ... skip on
11DC: 81 20               CMPA    #$20                      ; Printing a second space now?
11DE: 27 52               BEQ     $1232                     ; Yes ... just skip it (MORE and out)
11E0: 81 2E               CMPA    #$2E                      ; A '.' ?
11E2: 27 08               BEQ     $11EC                     ; Yes. Ignore leading space.
11E4: 81 3F               CMPA    #$3F                      ; A '?' ?
11E6: 27 04               BEQ     $11EC                     ; Yes. Ignore leading space.
11E8: 81 21               CMPA    #$21                      ; A '!' ?
11EA: 26 06               BNE     $11F2                     ; Yes. Ignore leading space.
11EC: DE 88               LDU     <$88                      ; {ram:printCursor} Back screen ...
11EE: 33 5F               LEAU    -1,U                      ; ... pointer up ...
11F0: DF 88               STU     <$88                      ; {ram:printCursor} ... over ignored space
11F2: B7 01 BE            STA     $01BE                     ; {ram:lastChar} Store last printed character
11F5: AD 9F A0 02         JSR     [$A002]                   ; {hard:CHROUT} Output a character
11F9: 96 89               LDA     <$89                      ; {ram:printCursor} LSB of screen position (we know MSB is 4 or 5)
11FB: 81 FE               CMPA    #$FE                      ; Have we reached the end of the screen?
11FD: 25 33               BCS     $1232                     ; No ... handle any MORE and out
11FF: DE 88               LDU     <$88                      ; {ram:printCursor} Cursor position
1201: 33 C8 DF            LEAU    $-21,U                    ; Back up to end of current row (where it will be after CR)
1204: 86 0D               LDA     #$0D                      ; CR ...
1206: AD 9F A0 02         JSR     [$A002]                   ; {hard:CHROUT} ... to screen
120A: 7A 01 E3            DEC     $01E3                     ; {ram:tillMORE} Rows left until MORE is needed
120D: A6 C4               LDA     ,U                        ; Find the ...
120F: 81 60               CMPA    #$60                      ; ... space before ...
1211: 27 04               BEQ     $1217                     ; ... the last ...
1213: 33 5F               LEAU    -1,U                      ; ... word ...
1215: 20 F6               BRA     $120D                     ; ... on the line
1217: 33 41               LEAU    1,U                       ; Now pointing to the last word on the line
1219: A6 C4               LDA     ,U                        ; Get next character in buffer
121B: 81 60               CMPA    #$60                      ; Is it a space?
121D: 27 13               BEQ     $1232                     ; Yes ... all done
121F: C6 60               LDB     #$60                      ; Store a space ...
1221: E7 C4               STB     ,U                        ; ... over this on the screen
1223: 81 60               CMPA    #$60                      ; Make sure ...
1225: 25 02               BCS     $1229                     ; ... upper ...
1227: 80 40               SUBA    #$40                      ; ... case
1229: B7 01 BE            STA     $01BE                     ; {ram:lastChar} Store last printed character
122C: AD 9F A0 02         JSR     [$A002]                   ; {hard:CHROUT} Output a character
1230: 20 E5               BRA     $1217                     ; Move overhang to next line
1232: 7D 01 E3            TST     $01E3                     ; {ram:tillMORE} Time for a MORE prompt?
1235: 2B 01               BMI     $1238                     ; {MorePrompt} Yes ... do it and out
1237: 39                  RTS                               ; Done

MorePrompt:
; Print MORE and wait for key
;
1238: B6 01 BE            LDA     $01BE                     ; {ram:lastChar} Last printed character
123B: 34 76               PSHS    U,Y,X,B,A                 ; Hold
123D: 86 0D               LDA     #$0D                      ; Reset MORE ...
123F: B7 01 E3            STA     $01E3                     ; {ram:tillMORE} ... row count
1242: 8E 13 DB            LDX     #$13DB                    ; " MORE" message
1245: E6 80               LDB     ,X+                       ; Length
1247: BD 11 C0            JSR     $11C0                     ; Print message
124A: BD 0B 6C            JSR     $0B6C                     ; {GetKey} Get a key
124D: 9E 88               LDX     <$88                      ; {ram:printCursor} back pointer ...
124F: 30 18               LEAX    -8,X                      ; ... up 8 over ...
1251: 9F 88               STX     <$88                      ; {ram:printCursor} ... MORE prompt
1253: 35 76               PULS    A,B,X,Y,U                 ; Restore
1255: B7 01 BE            STA     $01BE                     ; {ram:lastChar} Restore last printed character
1258: 39                  RTS                               ; Done
```

# Unpack Bytes

```code
UnpackBytes:
; Unpack three characters stored in 2 bytes pointed to by X and print to screen.
; Every 2 bytes holds 3 characters. Each character can be from 0 to 39.
; 40*40*40 = 64000 ... totally ingenious.
;
1259: 10 8E 13 15         LDY     #$1315                    ;
125D: C6 03               LDB     #$03                      ;
125F: F7 13 12            STB     $1312                     ; 
1262: A6 80               LDA     ,X+                       ;
1264: B7 01 DE            STA     $01DE                     ; {ram:tmp1DE} 
1267: A6 80               LDA     ,X+                       ;
1269: B7 01 DD            STA     $01DD                     ; {ram:tmp1DD} 
126C: 31 23               LEAY    3,Y                       ;
126E: CE 00 28            LDU     #$0028                    ;
1271: FF 13 13            STU     $1313                     ; 
1274: 86 11               LDA     #$11                      ;
1276: B7 01 DA            STA     $01DA                     ; {ram:tmp1DA} 
1279: 7F 01 DB            CLR     $01DB                     ; {ram:tmp1DB} 
127C: 7F 01 DC            CLR     $01DC                     ; {ram:tmp1DC} 
127F: 79 01 DE            ROL     $01DE                     ; {ram:tmp1DE} 
1282: 79 01 DD            ROL     $01DD                     ; {ram:tmp1DD} 
1285: 7A 01 DA            DEC     $01DA                     ; {ram:tmp1DA} 
1288: 27 39               BEQ     $12C3                     ; 
128A: 86 00               LDA     #$00                      ;
128C: 89 00               ADCA    #$00                      ; This algorithm is identical to the decompression
128E: 78 01 DC            ASL     $01DC                     ; {ram:tmp1DC} used in Pyramid2000. Check the comments there for
1291: 79 01 DB            ROL     $01DB                     ; {ram:tmp1DB} more detail.
1294: BB 01 DC            ADDA    $01DC                     ; {ram:tmp1DC} 
1297: B0 13 14            SUBA    $1314                     ; 
129A: B7 01 E0            STA     $01E0                     ; {ram:tmp1EO} 
129D: B6 01 DB            LDA     $01DB                     ; {ram:tmp1DB} 
12A0: B2 13 13            SBCA    $1313                     ; 
12A3: B7 01 DF            STA     $01DF                     ; {ram:tmp1DF} 
12A6: 24 0B               BCC     $12B3                     ; 
12A8: FC 01 DF            LDD     $01DF                     ; {ram:tmp1DF} 
12AB: F3 13 13            ADDD    $1313                     ; 
12AE: FD 01 DB            STD     $01DB                     ; {ram:tmp1DB} 
12B1: 20 06               BRA     $12B9                     ; 
12B3: FC 01 DF            LDD     $01DF                     ; {ram:tmp1DF} 
12B6: FD 01 DB            STD     $01DB                     ; {ram:tmp1DB} 
; Compliment C flag and continue
12B9: 25 04               BCS     $12BF                     ; 
12BB: 1A 01               ORCC    #$01                      ;
12BD: 20 C0               BRA     $127F                     ; 
12BF: 1C FE               ANDCC   #$FE                      ;
12C1: 20 BC               BRA     $127F                     ; 
; Process the result of the division
12C3: FC 01 DB            LDD     $01DB                     ; {ram:tmp1DB} 
12C6: C3 12 EA            ADDD    #$12EA                    ;
12C9: 1F 03               TFR     D,U                       ;
12CB: A6 C4               LDA     ,U                        ;
12CD: A7 A2               STA     ,-Y                       ;
12CF: 7A 13 12            DEC     $1312                     ; 
12D2: 26 9A               BNE     $126E                     ; 
12D4: 10 8E 13 15         LDY     #$1315                    ;
12D8: C6 03               LDB     #$03                      ;
12DA: A6 A0               LDA     ,Y+                       ;
12DC: 34 04               PSHS    B                         ;
12DE: BD 11 D5            JSR     $11D5                     ; {PrintCharacterAutoWrap} Print character
12E1: 35 04               PULS    B                         ;
12E3: 5A                  DECB                              ;
12E4: 26 F4               BNE     $12DA                     ; 
12E6: FC 01 AB            LDD     $01AB                     ; {ram:tmp1AB} 
12E9: 39                  RTS                               ;
;
; Character translation table
;     ?  !  2  .  "  '  <  >  /  0  3  A  B  C  D  E
12EA: 3F 21 32 20 22 27 3C 3E 2F 30 33 41 42 43 44 45
;     F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U
12FA: 46 47 48 49 4A 4B 4C 4D 4E 4F 50 51 52 53 54 55
;     V  W  X  Y  Z  -  ,  .
130A: 56 57 58 59 5A 2D 2C 2E            

1312: 00 00 00 00 00 00 00 ; Temporaries for decompression algorithm above
   
Com_2B_generate_random:
; generate_random()
1319: 34 14               PSHS    X,B                       ; Random number generator. Uses seed at 13B8.
131B: 8E 13 B8            LDX     #$13B8                    ;
131E: C6 17               LDB     #$17                      ;
1320: A6 84               LDA     ,X                        ;
1322: 30 01               LEAX    1,X                       ;
1324: 1A 01               ORCC    #$01                      ;
1326: 84 06               ANDA    #$06                      ;
1328: 27 07               BEQ     $1331                     ; 
132A: 81 06               CMPA    #$06                      ;
132C: 1A 01               ORCC    #$01                      ;
132E: 27 01               BEQ     $1331                     ; 
1330: 4F                  CLRA                              ;
1331: A6 84               LDA     ,X                        ;
1333: 25 03               BCS     $1338                     ; 
1335: 44                  LSRA                              ;
1336: 20 03               BRA     $133B                     ; 
1338: 44                  LSRA                              ;
1339: 8A 80               ORA     #$80                      ;
133B: A7 84               STA     ,X                        ;
133D: 30 1F               LEAX    -1,X                      ;
133F: A6 84               LDA     ,X                        ;
1341: 25 03               BCS     $1346                     ; 
1343: 44                  LSRA                              ;
1344: 20 03               BRA     $1349                     ; 
1346: 44                  LSRA                              ;
1347: 8A 80               ORA     #$80                      ;
1349: 84 FE               ANDA    #$FE                      ;
134B: A7 84               STA     ,X                        ;
134D: 5A                  DECB                              ;
134E: 26 D2               BNE     $1322                     ; 
1350: 4F                  CLRA                              ;
1351: 35 14               PULS    B,X                       ;
1353: 39                  RTS                               ;
```

# Data Section 

```code
1354: 94 ; Init game
1355: A3 ; Start of game splash (YOU FEEL AS THOUGH ...)
1356: AC ; Script for command-given-to-someone
```

# Command Jump Table

```code
CommandJumpTable: 
1357: 0C C2  ; 00 move_ACTIVE_and_look(room)
1359: 0E 24  ; 01 is_in_pack_or_current_room(object)
135B: 0E 48  ; 02 is_owned_by_ACTIVE(object)
135D: 0E 4D  ; 03 is_located(room,object)
135F: 0E 65  ; 04 print(msg)
1361: 10 BA  ; 05 is_less_equal_last_random(value)
1363: 0E 8F  ; 06 print_inventory()
1365: 0E 8A  ; 07 print_room_description()
1367: 0E CF  ; 08 is_first_noun(object)
1369: 0E ED  ; 09 compare_to_second_noun(object)
136B: 0E FE  ; 0A compare_input_to(phrase)
136D: 0C 99  ; 0B switch:
136F: 0E 62  ; 0C fail()
1371: 0C 68  ; 0D while_pass:
1373: 0C 80  ; 0E while_fail:
1375: 0F 04  ; 0F pick_up_VAR()
1377: 0F 15  ; 10 drop_VAR()
1379: 0F 87  ; 11 print_first_noun()
137B: 0F B4  ; 12 print_second_noun()
137D: 0F 26  ; 13 process_phrase_by_room_first_second()
137F: 10 13  ; 14 execute_and_reverse_status:
1381: 0F BE  ; 15 check_VAR(bits)
1383: 0F 7D  ; 16 print_VAR()
1385: 10 1D  ; 17 move_to(object,room)
1387: 10 31  ; 18 is_VAR_owned_by_ACTIVE()
1389: 0C CE  ; 19 move_ACTIVE(room)
138B: 0C EF  ; 1A set_VAR_to_first_noun()
138D: 0C FD  ; 1B set_VAR_to_second_noun()
138F: 0D 0B  ; 1C set_VAR(object)
1391: 10 C8  ; 1D attack_VAR(points)
1393: 11 11  ; 1E swap(object_a,object_b)
1395: 0E 70  ; 1F print2(msg)
1397: 0E 31  ; 20 is_ACTIVE_this(object)
1399: 0D 1E  ; 21 execute_phrase(phrase,first_noun,second_noun)
139B: 11 6A  ; 22 is_less_equal_health(points)
139D: 11 3B  ; 23 heal_VAR(points)
139F: 11 7B  ; 24 endless_loop()
13A1: 11 6A  ; 25 restart_game()
13A3: 11 6A  ; 26 print_score()
13A5: 11 6A  ; 27 load_game()
13A7: 11 6A  ; 28 save_game()
13A9: 0F DD  ; 29 toggle_open_VAR()
13AB: 0F F8  ; 2A toggle_lock_VAR()
13AD: 13 19  ; 2B generate_random()
13AF: 0E 37  ; 2C set_ACTIVE(object)
13B1: 0E F5  ; 2D is_VAR(object)

; Multi-verb replacement list (code doesn't work that uses this anyway)
13B3: 00  ; List is the length. List is pointed to by 13B2 which is ignored

; Random number seed
13B4: 12 23 44 1D     
13B8: 27 4D 2D 13    

FeedbackPrompts:
; "?VERB?"      
13BC: 06 3F 56 45 52 42 3F          
;       
; "?WHAT?"
13C3: 06 3F 57 48 41 54 3F              
;          
; "?WHICH?"      
13CA: 07 3F 57 48 49  43 48 3F               
;           
; "?PHRASE?"   
13D2: 08 3F 50 48 52 41 53 45 3F       
;           
; "-&lt;MORE&gt;"
13DB: 07 2D  3C 4D 4F 52 45 3E                             
```

# Phrase List

In TRS80 but not COCO (TRS80 has everything):

```
"0C: LOOK * UNDER u......."
"1A: ?? * * *"
"1B: LOOK * AROUND u......."
"1C: LOOK * BEHIND u......."
"1D: LOOK * OUT *"
"36: CLIMB * IN *"
"36: GO * IN u......."
"36: CLIMB * IN u......."
"36: JUMP * IN u......."
"37: CLIMB * OUT *"
"37: CLIMB * OUT u......."
"37: GO * OUT u......."
"37: JUMP * OUT u......."
"38: CLIMB * UNDER u......."
"38: GO * UNDER u......."
"39: THROW u....... IN u......."
```    

```code
PhraseList: 
13E3: 05 00 00 00 01  ; 01: NORTH   *         *       *         
13E8: 06 00 00 00 02  ; 02: SOUTH   *         *       *         
13ED: 07 00 00 00 03  ; 03: EAST    *         *       *         
13F2: 08 00 00 00 04  ; 04: WEST    *         *       *         
13F7: 09 00 20 00 05  ; 05: GET     ..C.....  *       *         
13FC: 09 02 20 20 43  ; 43: GET     ..C.....  WITH    ..C.....  
1401: 34 07 00 80 05  ; 05: PICK    *         UP      u.......  
1406: 34 07 80 00 05  ; 05: PICK    u.......  UP      *         
140B: 0A 00 20 00 06  ; 06: DROP    ..C.....  *       *         
1410: 0A 05 80 80 0F  ; 0F: DROP    u.......  IN      u.......  
1415: 0B 00 00 00 07  ; 07: INVENT  *         *       *         
141A: 04 02 10 40 09  ; 09: ATTACK  ...P....  WITH    .v......  
141F: 04 00 10 00 09  ; 09: ATTACK  ...P....  *       *         
1424: 0C 00 00 00 0A  ; 0A: LOOK    *         *       *         
1429: 0C 03 00 80 0B  ; 0B: LOOK    *         AT      u.......  
142E: 0C 05 00 80 10  ; 10: LOOK    *         IN      u.......  
1433: 03 03 40 10 0D  ; 0D: THROW   .v......  AT      ...P....  
1438: 03 08 00 20 06  ; 06: THROW   *         DOWN    ..C.....  
143D: 03 01 80 10 0E  ; 0E: THROW   u.......  TO      ...P....  
1442: 0D 01 80 10 0E  ; 0E: GIVE    u.......  TO      ...P....  
1447: 0E 00 80 00 0B  ; 0B: EXAMIN  u.......  *       *         
144C: 0E 05 00 80 0B  ; 0B: EXAMIN  *         IN      u.......  
1451: 0F 00 02 00 11  ; 11: OPEN    ......O.  *       *         
1456: 0F 02 02 80 3A  ; 3A: OPEN    ......O.  WITH    u.......  
145B: 38 00 08 00 40  ; 40: CLOSE   ....A...  *       *         
1460: 39 02 08 80 41  ; 41: LOCK    ....A...  WITH    u.......  
1465: 3A 02 01 80 42  ; 42: UNLOCK  .......L  WITH    u.......  
146A: 10 00 80 00 12  ; 12: PULL    u.......  *       *         
146F: 10 08 80 00 12  ; 12: PULL    u.......  DOWN    *         
1474: 10 08 00 80 12  ; 12: PULL    *         DOWN    u.......  
1479: 10 06 00 80 05  ; 05: PULL    *         OUT     u.......  
147E: 10 06 80 00 05  ; 05: PULL    u.......  OUT     *         
1483: 10 07 00 80 2D  ; 2D: PULL    *         UP      u.......  
1488: 10 07 80 00 2D  ; 2D: PULL    u.......  UP      *         
148D: 12 00 80 00 15  ; 15: EAT     u.......  *       *         
1492: 15 00 80 00 17  ; 17: CLIMB   u.......  *       *         
1497: 15 07 00 80 17  ; 17: CLIMB   *         UP      u.......  
149C: 15 08 00 80 17  ; 17: CLIMB   *         DOWN    u.......  
14A1: 15 09 00 80 17  ; 17: CLIMB   *         OVER    u.......  
14A6: 15 0C 00 80 17  ; 17: CLIMB   *         ON      u.......  
14AB: 05 01 00 00 01  ; 01: NORTH   *         TO      *         
14B0: 06 01 00 00 02  ; 02: SOUTH   *         TO      *         
14B5: 07 01 00 00 03  ; 03: EAST    *         TO      *         
14BA: 08 01 00 00 04  ; 04: WEST    *         TO      *         
14BF: 0A 08 00 20 06  ; 06: DROP    *         DOWN    ..C.....  
14C4: 0A 08 20 00 06  ; 06: DROP    ..C.....  DOWN    *         
14C9: 0A 0A 20 80 06  ; 06: DROP    ..C.....  BEHIND  u.......  
14CE: 0A 04 20 80 06  ; 06: DROP    ..C.....  UNDER   u.......  
14D3: 0A 0C 20 80 06  ; 06: DROP    ..C.....  ON      u.......  
14D8: 0C 07 00 00 0A  ; 0A: LOOK    *         UP      *         
14DD: 0C 08 00 00 0A  ; 0A: LOOK    *         DOWN    *         
14E2: 0C 09 80 00 0B  ; 0B: LOOK    u.......  OVER    *         
14E7: 0C 09 00 80 0A  ; 0A: LOOK    *         OVER    u.......  
14EC: 0C 0B 00 00 0A  ; 0A: LOOK    *         AROUND  *         
14F1: 0C 0A 00 00 0A  ; 0A: LOOK    *         BEHIND  *         
14F6: 32 00 00 00 21  ; 21: PLUGH   *         *       *         
14FB: 2B 00 00 00 22  ; 22: SCREAM  *         *       *         
1500: 2D 00 00 00 23  ; 23: QUIT    *         *       *         
1505: 3B 00 00 00 44  ; 44: HELLO   *         *       *         
150A: 3B 00 10 00 45  ; 45: HELLO   ...P....  *       *         
150F: 3B 01 00 00 44  ; 44: HELLO   *         TO      *         
1514: 3B 01 00 10 45  ; 45: HELLO   *         TO      ...P....  
1519: 3C 00 00 00 46  ; 46: WHAT    *         *       *         
151E: 3C 00 80 00 47  ; 47: WHAT    u.......  *       *         
1523: 3B 01 10 00 45  ; 45: HELLO   ...P....  TO      *         
1528: 21 00 00 00 25  ; 25: GO      *         *       *         
152D: 21 01 00 80 3D  ; 3D: GO      *         TO      u.......  
1532: 21 07 00 80 17  ; 17: GO      *         UP      u.......  
1537: 21 08 00 80 17  ; 17: GO      *         DOWN    u.......  
153C: 21 0B 00 80 26  ; 26: GO      *         AROUND  u.......  
1541: 23 00 80 00 27  ; 27: KICK    u.......  *       *         
1546: 23 08 00 80 27  ; 27: KICK    *         DOWN    u.......  
154B: 23 05 00 80 27  ; 27: KICK    *         IN      u.......  
1550: 24 02 10 80 28  ; 28: FEED    ...P....  WITH    u.......  
1555: 24 01 80 10 29  ; 29: FEED    u.......  TO      ...P....  
155A: 1C 00 80 00 2D  ; 2D: LIFT    u.......  *       *         
155F: 1F 00 00 00 2F  ; 2F: WAIT    *         *       *         
1564: 1F 0B 00 00 2F  ; 2F: WAIT    *         AROUND  *         
1569: 09 07 00 00 2F  ; 2F: GET     *         UP      *         
156E: 20 09 00 80 34  ; 34: JUMP    *         OVER    u.......  
1573: 3D 00 80 00 48  ; 48: LOWER   u.......  *       *         
1578: 3E 08 80 00 48  ; 48: LET     u.......  DOWN    *         
157D: 3E 08 00 80 48  ; 48: LET     *         DOWN    u.......  
1582: 09 08 00 80 48  ; 48: GET     *         DOWN    u.......  
1587: 09 08 80 00 48  ; 48: GET     u.......  DOWN    *         
158C: 3F 00 00 00 4A  ; 4A: COME    *         *       *         
1591: 3F 02 00 00 4A  ; 4A: COME    *         WITH    *         
1596: 40 00 80 00 49  ; 49: MEET    u.......  *       *         
159B: 40 01 80 80 49  ; 49: MEET    u.......  TO      u.......  
15A0: 00
```

# Room Descriptions

```code
RoomDescriptions: 
15A1: 00 85 9E                                                         ; 
;
; Maintenance room
15A4: 81 3A 00                                                         ; roomNumber=81(Maintenance room) size=003A data=00
15A7:   03 2A                                                          ;   03 DESCRIPTION
15A9:     04 28                                                        ;     print(msg) size=0028
15AB:       5F BE 63 16 9E 7A 8B 61 17 98 39 17 FE 9F 7B 14            ;       THE MAINTENANCE ROOM, A LARGE ROOM WITH
15BB:       54 8B 9B 6C 01 B3 59 90 82 7B 3A 15 8D 7B 23 15            ;       EXITS EAST AND WEST.
15CB:       F3 B9 8E 48 F7 17 17 BA                                    ;       ~
15D3:   04 0B                                                          ;   04 COMMAND
15D5:     0B 09 0A                                                     ;     switch(compare_input_to(phrase)): size=0009
15D8:       04                                                         ;       compare_input_to(phrase) phrase="04: WEST * * *"
15D9:       02                                                         ;       IF_NOT_GOTO address=15DC
15DA:         00 95                                                    ;         move_ACTIVE_and_look(room) room=95(Office)
15DC:       03                                                         ;       compare_input_to(phrase) phrase="03: EAST * * *"
15DD:       02                                                         ;       IF_NOT_GOTO address=15E0
15DE:         00 82                                                    ;         move_ACTIVE_and_look(room) room=82(Dispensary)
;
; Dispensary
15E0: 82 49 00                                                         ; roomNumber=82(Dispensary) size=0049 data=00
15E3:   03 35                                                          ;   03 DESCRIPTION
15E5:     04 33                                                        ;     print(msg) size=0033
15E7:       5F BE 03 15 5F B9 93 9A 9E B4 7B 14 E3 B8 F3 8C            ;       THE DISPENSARY, A SMALL SQUARE ROOM WITH
15F7:       97 B9 2F 49 39 17 DB 9F 56 D1 07 71 96 D7 D6 B5            ;       EXITS TO THE EAST, WEST, AND SOUTH.
1607:       D6 9C DB 72 95 5F 73 C1 B5 D0 73 C1 8E 48 61 17            ;       ~
1617:       82 C6 2E                                                   ;       ~
161A:   04 0F                                                          ;   04 COMMAND
161C:     0B 0D 0A                                                     ;     switch(compare_input_to(phrase)): size=000D
161F:       04                                                         ;       compare_input_to(phrase) phrase="04: WEST * * *"
1620:       02                                                         ;       IF_NOT_GOTO address=1623
1621:         00 81                                                    ;         move_ACTIVE_and_look(room) room=81(Maintenance room)
1623:       02                                                         ;       compare_input_to(phrase) phrase="02: SOUTH * * *"
1624:       02                                                         ;       IF_NOT_GOTO address=1627
1625:         00 83                                                    ;         move_ACTIVE_and_look(room) room=83(Examination room)
1627:       03                                                         ;       compare_input_to(phrase) phrase="03: EAST * * *"
1628:       02                                                         ;       IF_NOT_GOTO address=162B
1629:         00 84                                                    ;         move_ACTIVE_and_look(room) room=84(West end east-west hall)
;
; Examination room
162B: 83 46 00                                                         ; roomNumber=83(Examination room) size=0046 data=00
162E:   03 3A                                                          ;   03 DESCRIPTION
1630:     04 38                                                        ;     print(msg) size=0038
1632:       5F BE 3A 15 6B 48 D6 97 C0 7A 39 17 DB 9F 1F D1            ;       THE EXAMINATION ROOM WHERE THE DOCTOR TR
1642:       5B B1 5F BE 09 15 09 56 96 AF 63 B1 0B C0 56 A4            ;       EATS PATIENTS. THERE IS A SINGLE EXIT NO
1652:       30 79 2F C0 82 17 2F 62 D5 15 7B 14 50 B8 BF 6D            ;       RTH.
1662:       3A 15 73 7B 04 9A 77 BE                                    ;       ~
166A:   04 07                                                          ;   04 COMMAND
166C:     0B 05 0A                                                     ;     switch(compare_input_to(phrase)): size=0005
166F:       01                                                         ;       compare_input_to(phrase) phrase="01: NORTH * * *"
1670:       02                                                         ;       IF_NOT_GOTO address=1673
1671:         00 82                                                    ;         move_ACTIVE_and_look(room) room=82(Dispensary)
;
; West end east-west hall
1673: 84 5B 00                                                         ; roomNumber=84(West end east-west hall) size=005B data=00
1676:   03 37                                                          ;   03 DESCRIPTION
1678:     04 35                                                        ;     print(msg) size=0035
167A:       5F BE F7 17 F3 B9 8E 61 B8 16 7B 14 74 CA 4E DB            ;       THE WEST END OF A VERY LONG EAST-WEST HA
168A:       11 A0 23 15 15 BA B5 D0 0A BC 46 48 1B D0 56 F4            ;       LLWAY. THERE IS AN OPENING TO THE WEST.
169A:       F4 72 4B 5E C3 B5 91 96 F0 A4 91 7A 89 17 82 17            ;       ~
16AA:       59 5E 66 62 2E                                             ;       ~
16AF:   04 1F                                                          ;   04 COMMAND
16B1:     0B 1D 0A                                                     ;     switch(compare_input_to(phrase)): size=001D
16B4:       04                                                         ;       compare_input_to(phrase) phrase="04: WEST * * *"
16B5:       02                                                         ;       IF_NOT_GOTO address=16B8
16B6:         00 82                                                    ;         move_ACTIVE_and_look(room) room=82(Dispensary)
16B8:       03                                                         ;       compare_input_to(phrase) phrase="03: EAST * * *"
16B9:       02                                                         ;       IF_NOT_GOTO address=16BC
16BA:         00 87                                                    ;         move_ACTIVE_and_look(room) room=87(East-west hall A)
16BC:       01                                                         ;       compare_input_to(phrase) phrase="01: NORTH * * *"
16BD:       08                                                         ;       IF_NOT_GOTO address=16C6
16BE:         0E 06                                                    ;         while_fail: size=0006
16C0:           14                                                     ;           execute_and_reverse_status:
16C1:           1C 02                                                  ;           set_VAR(object) object=02(GreenDoorB)
16C3:           8D                                                     ;           8D(PrintObjectIsClosed)
16C4:           00 85                                                  ;           move_ACTIVE_and_look(room) room=85(Padded room A)
16C6:       02                                                         ;       compare_input_to(phrase) phrase="02: SOUTH * * *"
16C7:       08                                                         ;       IF_NOT_GOTO address=16D0
16C8:         0E 06                                                    ;         while_fail: size=0006
16CA:           14                                                     ;           execute_and_reverse_status:
16CB:           1C 03                                                  ;           set_VAR(object) object=03(RedDoorA)
16CD:           8D                                                     ;           8D(PrintObjectIsClosed)
16CE:           00 86                                                  ;           move_ACTIVE_and_look(room) room=86(Padded room B)
;
; Padded room A
16D0: 85 13 00                                                         ; roomNumber=85(Padded room A) size=0013 data=00
16D3:   03 01                                                          ;   03 DESCRIPTION
16D5:     81                                                           ;     81(PrintAnotherPaddedRoom)
16D6:   04 0D                                                          ;   04 COMMAND
16D8:     0B 0B 0A                                                     ;     switch(compare_input_to(phrase)): size=000B
16DB:       02                                                         ;       compare_input_to(phrase) phrase="02: SOUTH * * *"
16DC:       08                                                         ;       IF_NOT_GOTO address=16E5
16DD:         0E 06                                                    ;         while_fail: size=0006
16DF:           14                                                     ;           execute_and_reverse_status:
16E0:           1C 01                                                  ;           set_VAR(object) object=01(GreenDoorA)
16E2:           8D                                                     ;           8D(PrintObjectIsClosed)
16E3:           00 84                                                  ;           move_ACTIVE_and_look(room) room=84(West end east-west hall)
;
; Padded room B
16E5: 86 13 00                                                         ; roomNumber=86(Padded room B) size=0013 data=00
16E8:   03 01                                                          ;   03 DESCRIPTION
16EA:     81                                                           ;     81(PrintAnotherPaddedRoom)
16EB:   04 0D                                                          ;   04 COMMAND
16ED:     0B 0B 0A                                                     ;     switch(compare_input_to(phrase)): size=000B
16F0:       01                                                         ;       compare_input_to(phrase) phrase="01: NORTH * * *"
16F1:       08                                                         ;       IF_NOT_GOTO address=16FA
16F2:         0E 06                                                    ;         while_fail: size=0006
16F4:           14                                                     ;           execute_and_reverse_status:
16F5:           1C 04                                                  ;           set_VAR(object) object=04(RedDoorB)
16F7:           8D                                                     ;           8D(PrintObjectIsClosed)
16F8:           00 84                                                  ;           move_ACTIVE_and_look(room) room=84(West end east-west hall)
;
; East-west hall A
16FA: 87 25 00                                                         ; roomNumber=87(East-west hall A) size=0025 data=00
16FD:   03 01                                                          ;   03 DESCRIPTION
16FF:     82                                                           ;     82(PrintEastWestHall)
1700:   04 1F                                                          ;   04 COMMAND
1702:     0B 1D 0A                                                     ;     switch(compare_input_to(phrase)): size=001D
1705:       03                                                         ;       compare_input_to(phrase) phrase="03: EAST * * *"
1706:       02                                                         ;       IF_NOT_GOTO address=1709
1707:         00 8A                                                    ;         move_ACTIVE_and_look(room) room=8A(East-west hall B)
1709:       04                                                         ;       compare_input_to(phrase) phrase="04: WEST * * *"
170A:       02                                                         ;       IF_NOT_GOTO address=170D
170B:         00 84                                                    ;         move_ACTIVE_and_look(room) room=84(West end east-west hall)
170D:       01                                                         ;       compare_input_to(phrase) phrase="01: NORTH * * *"
170E:       08                                                         ;       IF_NOT_GOTO address=1717
170F:         0E 06                                                    ;         while_fail: size=0006
1711:           14                                                     ;           execute_and_reverse_status:
1712:           1C 06                                                  ;           set_VAR(object) object=06(GreedDoorD)
1714:           8D                                                     ;           8D(PrintObjectIsClosed)
1715:           00 88                                                  ;           move_ACTIVE_and_look(room) room=88(Small square room)
1717:       02                                                         ;       compare_input_to(phrase) phrase="02: SOUTH * * *"
1718:       08                                                         ;       IF_NOT_GOTO address=1721
1719:         0E 06                                                    ;         while_fail: size=0006
171B:           14                                                     ;           execute_and_reverse_status:
171C:           1C 07                                                  ;           set_VAR(object) object=07(RedDoorC)
171E:           8D                                                     ;           8D(PrintObjectIsClosed)
171F:           00 89                                                  ;           move_ACTIVE_and_look(room) room=89(Padded room C)
;
; Small square room
1721: 88 42 00                                                         ; roomNumber=88(Small square room) size=0042 data=00
1724:   03 30                                                          ;   03 DESCRIPTION
1726:     04 2E                                                        ;     print(msg) size=002E
1728:       55 45 8E 91 15 8A A3 AD 5B B1 01 B3 DB 95 46 48            ;       A SMALL SQUARE ROOM. ALL FOUR WALLS ARE
1738:       59 15 23 C6 0E D0 0B 8E 2F 49 E1 14 74 CA F3 5F            ;       COVERED WITH A THICK PADDING.
1748:       56 D1 03 71 82 17 DD 78 DB 16 C3 59 CF 98                  ;       ~
1756:   04 0D                                                          ;   04 COMMAND
1758:     0B 0B 0A                                                     ;     switch(compare_input_to(phrase)): size=000B
175B:       02                                                         ;       compare_input_to(phrase) phrase="02: SOUTH * * *"
175C:       08                                                         ;       IF_NOT_GOTO address=1765
175D:         0E 06                                                    ;         while_fail: size=0006
175F:           14                                                     ;           execute_and_reverse_status:
1760:           1C 05                                                  ;           set_VAR(object) object=05(GreenDoorC)
1762:           8D                                                     ;           8D(PrintObjectIsClosed)
1763:           00 87                                                  ;           move_ACTIVE_and_look(room) room=87(East-west hall A)
;
; Padded room C
1765: 89 13 00                                                         ; roomNumber=89(Padded room C) size=0013 data=00
1768:   03 01                                                          ;   03 DESCRIPTION
176A:     81                                                           ;     81(PrintAnotherPaddedRoom)
176B:   04 0D                                                          ;   04 COMMAND
176D:     0B 0B 0A                                                     ;     switch(compare_input_to(phrase)): size=000B
1770:       01                                                         ;       compare_input_to(phrase) phrase="01: NORTH * * *"
1771:       08                                                         ;       IF_NOT_GOTO address=177A
1772:         0E 06                                                    ;         while_fail: size=0006
1774:           14                                                     ;           execute_and_reverse_status:
1775:           1C 08                                                  ;           set_VAR(object) object=08(RedDoorD)
1777:           8D                                                     ;           8D(PrintObjectIsClosed)
1778:           00 87                                                  ;           move_ACTIVE_and_look(room) room=87(East-west hall A)
;
; East-west hall B
177A: 8A 25 00                                                         ; roomNumber=8A(East-west hall B) size=0025 data=00
177D:   03 01                                                          ;   03 DESCRIPTION
177F:     82                                                           ;     82(PrintEastWestHall)
1780:   04 1F                                                          ;   04 COMMAND
1782:     0B 1D 0A                                                     ;     switch(compare_input_to(phrase)): size=001D
1785:       04                                                         ;       compare_input_to(phrase) phrase="04: WEST * * *"
1786:       02                                                         ;       IF_NOT_GOTO address=1789
1787:         00 87                                                    ;         move_ACTIVE_and_look(room) room=87(East-west hall A)
1789:       03                                                         ;       compare_input_to(phrase) phrase="03: EAST * * *"
178A:       02                                                         ;       IF_NOT_GOTO address=178D
178B:         00 8C                                                    ;         move_ACTIVE_and_look(room) room=8C(East end east-west hall)
178D:       01                                                         ;       compare_input_to(phrase) phrase="01: NORTH * * *"
178E:       08                                                         ;       IF_NOT_GOTO address=1797
178F:         0E 06                                                    ;         while_fail: size=0006
1791:           14                                                     ;           execute_and_reverse_status:
1792:           1C 0A                                                  ;           set_VAR(object) object=0A(GreenDoorF)
1794:           8D                                                     ;           8D(PrintObjectIsClosed)
1795:           00 8B                                                  ;           move_ACTIVE_and_look(room) room=8B(Padded room D)
1797:       02                                                         ;       compare_input_to(phrase) phrase="02: SOUTH * * *"
1798:       08                                                         ;       IF_NOT_GOTO address=17A1
1799:         0E 06                                                    ;         while_fail: size=0006
179B:           14                                                     ;           execute_and_reverse_status:
179C:           1C 0B                                                  ;           set_VAR(object) object=0B(RedDoorE)
179E:           8D                                                     ;           8D(PrintObjectIsClosed)
179F:           00 8F                                                  ;           move_ACTIVE_and_look(room) room=8F(North end of north-south hall)
;
; Padded room D
17A1: 8B 13 00                                                         ; roomNumber=8B(Padded room D) size=0013 data=00
17A4:   03 01                                                          ;   03 DESCRIPTION
17A6:     81                                                           ;     81(PrintAnotherPaddedRoom)
17A7:   04 0D                                                          ;   04 COMMAND
17A9:     0B 0B 0A                                                     ;     switch(compare_input_to(phrase)): size=000B
17AC:       02                                                         ;       compare_input_to(phrase) phrase="02: SOUTH * * *"
17AD:       08                                                         ;       IF_NOT_GOTO address=17B6
17AE:         0E 06                                                    ;         while_fail: size=0006
17B0:           14                                                     ;           execute_and_reverse_status:
17B1:           1C 09                                                  ;           set_VAR(object) object=09(GreenDoorE)
17B3:           8D                                                     ;           8D(PrintObjectIsClosed)
17B4:           00 8A                                                  ;           move_ACTIVE_and_look(room) room=8A(East-west hall B)
;
; East end east-west hall
17B6: 8C 41 00                                                         ; roomNumber=8C(East end east-west hall) size=0041 data=00
17B9:   03 27                                                          ;   03 DESCRIPTION
17BB:     0D 25                                                        ;     while_pass: size=0025
17BD:       04 0A                                                      ;       print(msg) size=000A
17BF:         5F BE 23 15 F3 B9 8E 61 B8 16                            ;         THE EAST END OF
17C9:       82                                                         ;       82(PrintEastWestHall)
17CA:       04 16                                                      ;       print(msg) size=0016
17CC:         5F BE 5B B1 4B 7B 83 48 5F A0 10 99 D6 6A D6 9C          ;         THERE IS AN OPENING TO THE EAST.
17DC:         DB 72 95 5F 9B C1                                        ;         ~
17E2:   04 15                                                          ;   04 COMMAND
17E4:     0B 13 0A                                                     ;     switch(compare_input_to(phrase)): size=0013
17E7:       03                                                         ;       compare_input_to(phrase) phrase="03: EAST * * *"
17E8:       02                                                         ;       IF_NOT_GOTO address=17EB
17E9:         00 8E                                                    ;         move_ACTIVE_and_look(room) room=8E(Electroshock room)
17EB:       04                                                         ;       compare_input_to(phrase) phrase="04: WEST * * *"
17EC:       02                                                         ;       IF_NOT_GOTO address=17EF
17ED:         00 8A                                                    ;         move_ACTIVE_and_look(room) room=8A(East-west hall B)
17EF:       01                                                         ;       compare_input_to(phrase) phrase="01: NORTH * * *"
17F0:       08                                                         ;       IF_NOT_GOTO address=17F9
17F1:         0E 06                                                    ;         while_fail: size=0006
17F3:           14                                                     ;           execute_and_reverse_status:
17F4:           1C 0D                                                  ;           set_VAR(object) object=0D(GreenDoorH)
17F6:           8D                                                     ;           8D(PrintObjectIsClosed)
17F7:           00 8D                                                  ;           move_ACTIVE_and_look(room) room=8D(Padded room E)
;
; Padded room E
17F9: 8D 13 00                                                         ; roomNumber=8D(Padded room E) size=0013 data=00
17FC:   03 01                                                          ;   03 DESCRIPTION
17FE:     81                                                           ;     81(PrintAnotherPaddedRoom)
17FF:   04 0D                                                          ;   04 COMMAND
1801:     0B 0B 0A                                                     ;     switch(compare_input_to(phrase)): size=000B
1804:       02                                                         ;       compare_input_to(phrase) phrase="02: SOUTH * * *"
1805:       08                                                         ;       IF_NOT_GOTO address=180E
1806:         0E 06                                                    ;         while_fail: size=0006
1808:           14                                                     ;           execute_and_reverse_status:
1809:           1C 0C                                                  ;           set_VAR(object) object=0C(GreenDoorG)
180B:           8D                                                     ;           8D(PrintObjectIsClosed)
180C:           00 8C                                                  ;           move_ACTIVE_and_look(room) room=8C(East end east-west hall)
;
; Electroshock room
180E: 8E 36 00                                                         ; roomNumber=8E(Electroshock room) size=0036 data=00
1811:   03 2A                                                          ;   03 DESCRIPTION
1813:     04 28                                                        ;     print(msg) size=0028
1815:       5F BE 2E 15 E6 5F 05 B3 75 74 D6 83 F4 72 F3 48            ;       THE ELECTROSHOCK THERAPY ROOM. THERE IS
1825:       39 17 FF 9F 82 17 2F 62 D5 15 7B 14 50 B8 BF 6D            ;       A SINGLE EXIT WEST.
1835:       3A 15 73 7B B5 D0 9B C1                                    ;       ~
183D:   04 07                                                          ;   04 COMMAND
183F:     0B 05 0A                                                     ;     switch(compare_input_to(phrase)): size=0005
1842:       04                                                         ;       compare_input_to(phrase) phrase="04: WEST * * *"
1843:       02                                                         ;       IF_NOT_GOTO address=1846
1844:         00 8C                                                    ;         move_ACTIVE_and_look(room) room=8C(East end east-west hall)
;
; North end of north-south hall
1846: 8F 30 00                                                         ; roomNumber=8F(North end of north-south hall) size=0030 data=00
1849:   03 10                                                          ;   03 DESCRIPTION
184B:     0D 0E                                                        ;     while_pass: size=000E
184D:       04 0B                                                      ;       print(msg) size=000B
184F:         5F BE 99 16 C2 B3 30 15 11 58 46                         ;         THE NORTH END OF
185A:       83                                                         ;       83(PrintNorthSouthHall)
185B:   04 1B                                                          ;   04 COMMAND
185D:     0B 19 0A                                                     ;     switch(compare_input_to(phrase)): size=0019
1860:       01                                                         ;       compare_input_to(phrase) phrase="01: NORTH * * *"
1861:       08                                                         ;       IF_NOT_GOTO address=186A
1862:         0E 06                                                    ;         while_fail: size=0006
1864:           14                                                     ;           execute_and_reverse_status:
1865:           1C 0E                                                  ;           set_VAR(object) object=0E(RedDoorF)
1867:           8D                                                     ;           8D(PrintObjectIsClosed)
1868:           00 8A                                                  ;           move_ACTIVE_and_look(room) room=8A(East-west hall B)
186A:       02                                                         ;       compare_input_to(phrase) phrase="02: SOUTH * * *"
186B:       02                                                         ;       IF_NOT_GOTO address=186E
186C:         00 91                                                    ;         move_ACTIVE_and_look(room) room=91(North-south hall)
186E:       03                                                         ;       compare_input_to(phrase) phrase="03: EAST * * *"
186F:       08                                                         ;       IF_NOT_GOTO address=1878
1870:         0E 06                                                    ;         while_fail: size=0006
1872:           14                                                     ;           execute_and_reverse_status:
1873:           1C 0F                                                  ;           set_VAR(object) object=0F(BlueDoorA)
1875:           8D                                                     ;           8D(PrintObjectIsClosed)
1876:           00 90                                                  ;           move_ACTIVE_and_look(room) room=90(Padded room F)
;
; Padded room F
1878: 90 13 00                                                         ; roomNumber=90(Padded room F) size=0013 data=00
187B:   03 01                                                          ;   03 DESCRIPTION
187D:     81                                                           ;     81(PrintAnotherPaddedRoom)
187E:   04 0D                                                          ;   04 COMMAND
1880:     0B 0B 0A                                                     ;     switch(compare_input_to(phrase)): size=000B
1883:       04                                                         ;       compare_input_to(phrase) phrase="04: WEST * * *"
1884:       08                                                         ;       IF_NOT_GOTO address=188D
1885:         0E 06                                                    ;         while_fail: size=0006
1887:           14                                                     ;           execute_and_reverse_status:
1888:           1C 10                                                  ;           set_VAR(object) object=10(BlueDoorB)
188A:           8D                                                     ;           8D(PrintObjectIsClosed)
188B:           00 8F                                                  ;           move_ACTIVE_and_look(room) room=8F(North end of north-south hall)
;
; North-south hall
188D: 91 32 00                                                         ; roomNumber=91(North-south hall) size=0032 data=00
1890:   03 14                                                          ;   03 DESCRIPTION
1892:     0D 12                                                        ;     while_pass: size=0012
1894:       83                                                         ;       83(PrintNorthSouthHall)
1895:       04 0F                                                      ;       print(msg) size=000F
1897:         5F BE 5B B1 4B 7B 83 48 23 63 07 BC 66 49 2E             ;         THERE IS AN EXIT EAST.
18A6:   04 19                                                          ;   04 COMMAND
18A8:     0B 17 0A                                                     ;     switch(compare_input_to(phrase)): size=0017
18AB:       01                                                         ;       compare_input_to(phrase) phrase="01: NORTH * * *"
18AC:       02                                                         ;       IF_NOT_GOTO address=18AF
18AD:         00 8F                                                    ;         move_ACTIVE_and_look(room) room=8F(North end of north-south hall)
18AF:       02                                                         ;       compare_input_to(phrase) phrase="02: SOUTH * * *"
18B0:       02                                                         ;       IF_NOT_GOTO address=18B3
18B1:         00 96                                                    ;         move_ACTIVE_and_look(room) room=96(South end north-south hall)
18B3:       03                                                         ;       compare_input_to(phrase) phrase="03: EAST * * *"
18B4:       02                                                         ;       IF_NOT_GOTO address=18B7
18B5:         00 92                                                    ;         move_ACTIVE_and_look(room) room=92(Kitchen)
18B7:       04                                                         ;       compare_input_to(phrase) phrase="04: WEST * * *"
18B8:       08                                                         ;       IF_NOT_GOTO address=18C1
18B9:         0E 06                                                    ;         while_fail: size=0006
18BB:           14                                                     ;           execute_and_reverse_status:
18BC:           1C 11                                                  ;           set_VAR(object) object=11(BlueDoorC)
18BE:           8D                                                     ;           8D(PrintObjectIsClosed)
18BF:           00 94                                                  ;           move_ACTIVE_and_look(room) room=94(Padded room G)
;
; Kitchen
18C1: 92 38 00                                                         ; roomNumber=92(Kitchen) size=0038 data=00
18C4:   03 24                                                          ;   03 DESCRIPTION
18C6:     04 22                                                        ;     print(msg) size=0022
18C8:       5F BE 1B 16 9A BD 83 61 23 D1 13 54 55 72 3A 15            ;       THE KITCHEN WHICH HAS EXITS EAST, WEST,
18D8:       8D 7B 23 15 16 BA F7 17 16 BA 90 14 15 58 36 A1            ;       AND SOUTH.
18E8:       9B 76                                                      ;       ~
18EA:   04 0F                                                          ;   04 COMMAND
18EC:     0B 0D 0A                                                     ;     switch(compare_input_to(phrase)): size=000D
18EF:       03                                                         ;       compare_input_to(phrase) phrase="03: EAST * * *"
18F0:       02                                                         ;       IF_NOT_GOTO address=18F3
18F1:         00 93                                                    ;         move_ACTIVE_and_look(room) room=93(Kennel)
18F3:       02                                                         ;       compare_input_to(phrase) phrase="02: SOUTH * * *"
18F4:       02                                                         ;       IF_NOT_GOTO address=18F7
18F5:         00 97                                                    ;         move_ACTIVE_and_look(room) room=97(Dining room)
18F7:       04                                                         ;       compare_input_to(phrase) phrase="04: WEST * * *"
18F8:       02                                                         ;       IF_NOT_GOTO address=18FB
18F9:         00 91                                                    ;         move_ACTIVE_and_look(room) room=91(North-south hall)
;
; Kennel
18FB: 93 81 0F 00                                                      ; roomNumber=93(Kennel) size=010F data=00
18FF:   03 2B                                                          ;   03 DESCRIPTION
1901:     04 29                                                        ;     print(msg) size=0029
1903:       5F BE 17 16 CF 99 9B 8F 5F BE 5B B1 4B 7B 59 45            ;       THE KENNEL. THERE IS A WEST EXIT AND AN
1913:       66 62 3A 15 73 7B 8E 48 90 14 C2 16 93 61 AB 98            ;       OPENING TO THE SOUTH.
1923:       6B BF 5F BE 61 17 82 C6 2E                                 ;       ~
192C:   04 80 DE                                                       ;   04 COMMAND
192F:     0B 80 DB 0A                                                  ;     switch(compare_input_to(phrase)): size=00DB
1933:       02                                                         ;       compare_input_to(phrase) phrase="02: SOUTH * * *"
1934:       80 D3                                                      ;       IF_NOT_GOTO address=1A08
1936:         0E 80 D0                                                 ;         while_fail: size=00D0
1939:           0D 18                                                  ;           while_pass: size=0018
193B:             01 1A                                                ;             is_in_pack_or_current_room(object) object=1A(GuardDog)
193D:             04 14                                                ;             print(msg) size=0014
193F:               5F BE 09 15 D9 6A 46 7A 99 16 0E BC 73 62 C7 DE    ;               THE DOG WILL NOT LET YOU PASS!
194F:               DB 16 C9 B9                                        ;               ~
1953:           0D 80 B3                                               ;           while_pass: size=00B3
1956:             0E 80 B0                                             ;             while_fail: size=00B0
1959:               0D 19                                              ;               while_pass: size=0019
195B:                 20 38                                            ;                 is_ACTIVE_this(object) object=38(SYSTEM)
195D:                 04 15                                            ;                 print(msg) size=0015
195F:                   C7 DE 9B 15 5B CA 07 68 33 98 85 A6 44 B8 DB 8B;                   YOU HAVE FOUND POSSIBLE ESCAPE!
196F:                   55 62 DF 48 21                                 ;                   ~
1974:               0D 80 92                                           ;               while_pass: size=0092
1977:                 20 13                                            ;                 is_ACTIVE_this(object) object=13(PLAYER)
1979:                 04 26                                            ;                 print(msg) size=0026
197B:                   4B 49 C7 DE 3F 16 CF 49 15 EE CF 62 CE B0 87 15;                   AS YOU LEAVE, SEVERAL GUARDS POSTED OUTS
198B:                   2E 49 D2 B5 E6 A0 F3 5F 36 A1 46 B8 49 5E C4 B0;                   IDE GRAB YOU AND
199B:                   51 18 43 C2 33 98                              ;                   ~
19A1:                 0E 15                                            ;                 while_fail: size=0015
19A3:                   14                                             ;                   execute_and_reverse_status:
19A4:                   0D 05                                          ;                   while_pass: size=0005
19A6:                     01 3C                                        ;                     is_in_pack_or_current_room(object) object=3C(DeadDog)
19A8:                     17 3C 99                                     ;                     move_to(object,room) object=3C(DeadDog) room=99(Storage shed)
19AB:                   04 0B                                          ;                   print(msg) size=000B
19AD:                     5F BE FF 14 F3 46 79 5B 90 14 44             ;                     THE DEAD DOG AND
19B8:                 04 40                                            ;                 print(msg) size=0040
19BA:                   6C BE 6B A1 C7 DE D0 15 7B 14 E3 B8 F3 8C 09 BA;                   THROW YOU IN A SMALL STORAGE SHED BEHIND
19CA:                   C9 B0 55 5E E6 72 AF 14 90 73 16 58 DB 72 EB 4F;                   THE BUILDING. YOU HEAR THEM LOCK THE DO
19DA:                   C3 8B CF 98 51 18 4A C2 94 5F 82 17 5B 61 75 8D;                   OR AND GO AWAY.
19EA:                   D6 83 DB 72 81 5B 83 AF 33 98 2B 6E F3 49 DB E0;                   ~
19FA:                 1C 40                                            ;                 set_VAR(object) object=40(GreenDoorI)
19FC:                 0E 03                                            ;                 while_fail: size=0003
19FE:                   15 02                                          ;                   check_VAR(bits) bits=02(......O.)
1A00:                   29                                             ;                   print_open_VAR()
1A01:                 0E 03                                            ;                 while_fail: size=0003
1A03:                   15 01                                          ;                   check_VAR(bits) bits=01(.......L)
1A05:                   2A                                             ;                   toggle_lock_VAR()
1A06:                 17 13 99                                         ;                 move_to(object,room) object=13(PLAYER) room=99(Storage shed)
1A09:       04                                                         ;       compare_input_to(phrase) phrase="04: WEST * * *"
1A0A:       02                                                         ;       IF_NOT_GOTO address=1A0D
1A0B:         00 92                                                    ;         move_ACTIVE_and_look(room) room=92(Kitchen)
;
; Padded room G
1A0D: 94 13 00                                                         ; roomNumber=94(Padded room G) size=0013 data=00
1A10:   03 01                                                          ;   03 DESCRIPTION
1A12:     81                                                           ;     81(PrintAnotherPaddedRoom)
1A13:   04 0D                                                          ;   04 COMMAND
1A15:     0B 0B 0A                                                     ;     switch(compare_input_to(phrase)): size=000B
1A18:       03                                                         ;       compare_input_to(phrase) phrase="03: EAST * * *"
1A19:       08                                                         ;       IF_NOT_GOTO address=1A22
1A1A:         0E 06                                                    ;         while_fail: size=0006
1A1C:           14                                                     ;           execute_and_reverse_status:
1A1D:           1C 12                                                  ;           set_VAR(object) object=12(BlueDoorD)
1A1F:           8D                                                     ;           8D(PrintObjectIsClosed)
1A20:           00 91                                                  ;           move_ACTIVE_and_look(room) room=91(North-south hall)
;
; Office
1A22: 95 29 00                                                         ; roomNumber=95(Office) size=0029 data=00
1A25:   03 1D                                                          ;   03 DESCRIPTION
1A27:     04 1B                                                        ;     print(msg) size=001B
1A29:       5F BE B8 16 05 67 DB 63 5F BE 5B B1 4B 7B 55 45            ;       THE OFFICE. THERE IS A SINGLE EXIT EAST.
1A39:       91 7A DB 8B 23 63 07 BC 66 49 2E                           ;       ~
1A44:   04 07                                                          ;   04 COMMAND
1A46:     0B 05 0A                                                     ;     switch(compare_input_to(phrase)): size=0005
1A49:       03                                                         ;       compare_input_to(phrase) phrase="03: EAST * * *"
1A4A:       02                                                         ;       IF_NOT_GOTO address=1A4D
1A4B:         00 81                                                    ;         move_ACTIVE_and_look(room) room=81(Maintenance room)
;
; South end north-south hall
1A4D: 96 46 00                                                         ; roomNumber=96(South end north-south hall) size=0046 data=00
1A50:   03 32                                                          ;   03 DESCRIPTION
1A52:     04 30                                                        ;     print(msg) size=0030
1A54:       5F BE 61 17 82 C6 30 15 11 58 96 64 DB 72 04 9A            ;       THE SOUTH END OF THE NORTH-SOUTH HALLWAY
1A64:       75 BE 47 B9 53 BE 4E 72 B3 8E DB E0 5F BE 5B B1            ;       . THERE ARE EAST AND WEST EXITS.
1A74:       2F 49 23 15 F3 B9 8E 48 F7 17 F3 B9 23 63 2F C0            ;       ~
1A84:   04 0F                                                          ;   04 COMMAND
1A86:     0B 0D 0A                                                     ;     switch(compare_input_to(phrase)): size=000D
1A89:       01                                                         ;       compare_input_to(phrase) phrase="01: NORTH * * *"
1A8A:       02                                                         ;       IF_NOT_GOTO address=1A8D
1A8B:         00 91                                                    ;         move_ACTIVE_and_look(room) room=91(North-south hall)
1A8D:       04                                                         ;       compare_input_to(phrase) phrase="04: WEST * * *"
1A8E:       02                                                         ;       IF_NOT_GOTO address=1A91
1A8F:         00 98                                                    ;         move_ACTIVE_and_look(room) room=98(Recreation room)
1A91:       03                                                         ;       compare_input_to(phrase) phrase="03: EAST * * *"
1A92:       02                                                         ;       IF_NOT_GOTO address=1A95
1A93:         00 97                                                    ;         move_ACTIVE_and_look(room) room=97(Dining room)
;
; Dining room
1A95: 97 32 00                                                         ; roomNumber=97(Dining room) size=0032 data=00
1A98:   03 22                                                          ;   03 DESCRIPTION
1A9A:     04 20                                                        ;     print(msg) size=0020
1A9C:       5F BE 03 15 10 99 D4 6A 3F A0 56 F4 F4 72 43 5E            ;       THE DINING ROOM. THERE ARE EXITS NORTH A
1AAC:       5B B1 23 63 0B C0 04 9A 53 BE 8E 48 F7 17 17 BA            ;       ND WEST.
1ABC:   04 0B                                                          ;   04 COMMAND
1ABE:     0B 09 0A                                                     ;     switch(compare_input_to(phrase)): size=0009
1AC1:       01                                                         ;       compare_input_to(phrase) phrase="01: NORTH * * *"
1AC2:       02                                                         ;       IF_NOT_GOTO address=1AC5
1AC3:         00 92                                                    ;         move_ACTIVE_and_look(room) room=92(Kitchen)
1AC5:       04                                                         ;       compare_input_to(phrase) phrase="04: WEST * * *"
1AC6:       02                                                         ;       IF_NOT_GOTO address=1AC9
1AC7:         00 96                                                    ;         move_ACTIVE_and_look(room) room=96(South end north-south hall)
;
; Recreation room
1AC9: 98 37 00                                                         ; roomNumber=98(Recreation room) size=0037 data=00
1ACC:   03 2B                                                          ;   03 DESCRIPTION
1ACE:     04 29                                                        ;     print(msg) size=0029
1AD0:       5F BE 2F 17 AF 55 83 49 03 A0 01 B3 DB 95 5F BE            ;       THE RECREATION ROOM. THERE IS ONLY ONE E
1AE0:       5B B1 4B 7B 16 A0 51 DB 5B 98 23 63 19 BC 85 73            ;       XIT WHICH LEADS EAST.
1AF0:       0E 71 86 5F C7 B5 66 49 2E                                 ;       ~
1AF9:   04 07                                                          ;   04 COMMAND
1AFB:     0B 05 0A                                                     ;     switch(compare_input_to(phrase)): size=0005
1AFE:       03                                                         ;       compare_input_to(phrase) phrase="03: EAST * * *"
1AFF:       02                                                         ;       IF_NOT_GOTO address=1B02
1B00:         00 96                                                    ;         move_ACTIVE_and_look(room) room=96(South end north-south hall)
;
; Storage shed
1B02: 99 3E 00                                                         ; roomNumber=99(Storage shed) size=003E data=00
1B05:   03 0E                                                          ;   03 DESCRIPTION
1B07:     04 0C                                                        ;     print(msg) size=000C
1B09:       5F BE 66 17 AB A0 9B 6C 1F B8 9B 5D                        ;       THE STORAGE SHED.
1B15:   04 2B                                                          ;   04 COMMAND
1B17:     0B 29 0A                                                     ;     switch(compare_input_to(phrase)): size=0029
1B1A:       01                                                         ;       compare_input_to(phrase) phrase="01: NORTH * * *"
1B1B:       26                                                         ;       IF_NOT_GOTO address=1B42
1B1C:         0E 24                                                    ;         while_fail: size=0024
1B1E:           14                                                     ;           execute_and_reverse_status:
1B1F:           1C 40                                                  ;           set_VAR(object) object=40(GreenDoorI)
1B21:           8D                                                     ;           8D(PrintObjectIsClosed)
1B22:           0D 1E                                                  ;           while_pass: size=001E
1B24:             04 1B                                                ;             print(msg) size=001B
1B26:               C7 DE 3A 15 73 7B 5F BE 5A 17 F3 5F 8E 48 35 15    ;               YOU EXIT THE SHED AND ESCAPE TO FREEDOM!
1B36:               12 53 56 5E C8 9C 67 B1 7F 5B 21                   ;               ~
1B41:             24                                                   ;             endless_loop()
; ENDOF 15A1
```

# Object Data

```code
ObjectData:
; Objects are referenced by index in this list with the first object being "Object 1".
; The first three data bytes are as follows AA BB CC:
;   AA = location. If >80 then it is a room. If <80 then it is held by an object.
;   BB = score points (not used in BEDLAM)
;   CC = --CPAXOL
;    C=1 if object can be carried
;    P=1 if object is a person;
;    A=1 if open/close-able
;    X=1 if lock/unlock-able 
;    O=1 if closed
;    L=1 if locked
;
; Objects can have various fields tagged as follows:
;   01 = list of adjectives (size+bytes)
;   02 = short name (packed string)
;   03 = long description (packed string)
;   04 (never used)
;   05 (never used)
;   06 = command handling if object is second noun (script)
;   07 = command handling if object is first noun (script)
;   08 = turn-script executed for objects turn in game (script)
;   09 = hitpoint information (2 bytess) AA BB. AA=max hit points  BB=current hit points
;   0A = script executed with killed (script)
;   0B = script executed if command is given to object (script)
;

1B42: 00 93 DF                                                         ; size=13DF
;
; Object_01 "GreenDoorA"
1B45: 0B 12                                                            ; word=0B size=0012
1B47: 85 00 88                                                         ; room=85 scorePoints=00 bits=88
1B4A:   03 01                                                          ;   03 DESCRIPTION
1B4C:     84                                                           ;     84(PrintSouthWallGreenDoor)
1B4D:   01 01                                                          ;   01 ADJECTIVES
1B4F:   14                                                             ;   TODO WORD
1B50:   02 07                                                          ;   02 SHORT_NAME
1B52:     AF 6E 83 61 81 5B 52                                         ;     GREEN DOOR
;
; Object_02 "GreenDoorB"
1B59: 0B 12                                                            ; word=0B size=0012
1B5B: 84 00 8A                                                         ; room=84 scorePoints=00 bits=8A
1B5E:   03 01                                                          ;   03 DESCRIPTION
1B60:     86                                                           ;     86(PrintNorthWallGreedDoor)
1B61:   01 01                                                          ;   01 ADJECTIVES
1B63:   14                                                             ;   TODO WORD
1B64:   02 07                                                          ;   02 SHORT_NAME
1B66:     AF 6E 83 61 81 5B 52                                         ;     GREEN DOOR
;
; Object_03 "RedDoorA"
1B6D: 0B 11                                                            ; word=0B size=0011
1B6F: 84 00 8B                                                         ; room=84 scorePoints=00 bits=8B
1B72:   03 01                                                          ;   03 DESCRIPTION
1B74:     87                                                           ;     87(PrintSouthWallRedDOor)
1B75:   01 01                                                          ;   01 ADJECTIVES
1B77:   13                                                             ;   TODO WORD
1B78:   02 06                                                          ;   02 SHORT_NAME
1B7A:     66 B1 09 15 A3 A0                                            ;     RED DOOR
;
; Object_04 "RedDoorB"
1B80: 0B 11                                                            ; word=0B size=0011
1B82: 86 00 88                                                         ; room=86 scorePoints=00 bits=88
1B85:   03 01                                                          ;   03 DESCRIPTION
1B87:     85                                                           ;     85(PrintNorthWallRedDoor)
1B88:   01 01                                                          ;   01 ADJECTIVES
1B8A:   13                                                             ;   TODO WORD
1B8B:   02 06                                                          ;   02 SHORT_NAME
1B8D:     66 B1 09 15 A3 A0                                            ;     RED DOOR
;
; Object_05 "GreenDoorC"
1B93: 0B 12                                                            ; word=0B size=0012
1B95: 88 00 8A                                                         ; room=88 scorePoints=00 bits=8A
1B98:   03 01                                                          ;   03 DESCRIPTION
1B9A:     84                                                           ;     84(PrintSouthWallGreenDoor)
1B9B:   01 01                                                          ;   01 ADJECTIVES
1B9D:   14                                                             ;   TODO WORD
1B9E:   02 07                                                          ;   02 SHORT_NAME
1BA0:     AF 6E 83 61 81 5B 52                                         ;     GREEN DOOR
;
; Object_06 "GreedDoorD"
1BA7: 0B 12                                                            ; word=0B size=0012
1BA9: 87 00 88                                                         ; room=87 scorePoints=00 bits=88
1BAC:   03 01                                                          ;   03 DESCRIPTION
1BAE:     86                                                           ;     86(PrintNorthWallGreedDoor)
1BAF:   01 01                                                          ;   01 ADJECTIVES
1BB1:   14                                                             ;   TODO WORD
1BB2:   02 07                                                          ;   02 SHORT_NAME
1BB4:     AF 6E 83 61 81 5B 52                                         ;     GREEN DOOR
;
; Object_07 "RedDoorC"
1BBB: 0B 11                                                            ; word=0B size=0011
1BBD: 87 00 8B                                                         ; room=87 scorePoints=00 bits=8B
1BC0:   03 01                                                          ;   03 DESCRIPTION
1BC2:     87                                                           ;     87(PrintSouthWallRedDOor)
1BC3:   01 01                                                          ;   01 ADJECTIVES
1BC5:   13                                                             ;   TODO WORD
1BC6:   02 06                                                          ;   02 SHORT_NAME
1BC8:     66 B1 09 15 A3 A0                                            ;     RED DOOR
;
; Object_08 "RedDoorD"
1BCE: 0B 11                                                            ; word=0B size=0011
1BD0: 89 00 88                                                         ; room=89 scorePoints=00 bits=88
1BD3:   03 01                                                          ;   03 DESCRIPTION
1BD5:     85                                                           ;     85(PrintNorthWallRedDoor)
1BD6:   01 01                                                          ;   01 ADJECTIVES
1BD8:   13                                                             ;   TODO WORD
1BD9:   02 06                                                          ;   02 SHORT_NAME
1BDB:     66 B1 09 15 A3 A0                                            ;     RED DOOR
;
; Object_09 "GreenDoorE"
1BE1: 0B 12                                                            ; word=0B size=0012
1BE3: 8B 00 88                                                         ; room=8B scorePoints=00 bits=88
1BE6:   03 01                                                          ;   03 DESCRIPTION
1BE8:     84                                                           ;     84(PrintSouthWallGreenDoor)
1BE9:   01 01                                                          ;   01 ADJECTIVES
1BEB:   14                                                             ;   TODO WORD
1BEC:   02 07                                                          ;   02 SHORT_NAME
1BEE:     AF 6E 83 61 81 5B 52                                         ;     GREEN DOOR
;
; Object_0A "GreenDoorF"
1BF5: 0B 12                                                            ; word=0B size=0012
1BF7: 8A 00 8A                                                         ; room=8A scorePoints=00 bits=8A
1BFA:   03 01                                                          ;   03 DESCRIPTION
1BFC:     86                                                           ;     86(PrintNorthWallGreedDoor)
1BFD:   01 01                                                          ;   01 ADJECTIVES
1BFF:   14                                                             ;   TODO WORD
1C00:   02 07                                                          ;   02 SHORT_NAME
1C02:     AF 6E 83 61 81 5B 52                                         ;     GREEN DOOR
;
; Object_0B "RedDoorE"
1C09: 0B 11                                                            ; word=0B size=0011
1C0B: 8A 00 8B                                                         ; room=8A scorePoints=00 bits=8B
1C0E:   03 01                                                          ;   03 DESCRIPTION
1C10:     87                                                           ;     87(PrintSouthWallRedDOor)
1C11:   01 01                                                          ;   01 ADJECTIVES
1C13:   13                                                             ;   TODO WORD
1C14:   02 06                                                          ;   02 SHORT_NAME
1C16:     66 B1 09 15 A3 A0                                            ;     RED DOOR
;
; Object_0C "GreenDoorG"
1C1C: 0B 12                                                            ; word=0B size=0012
1C1E: 8D 00 88                                                         ; room=8D scorePoints=00 bits=88
1C21:   03 01                                                          ;   03 DESCRIPTION
1C23:     84                                                           ;     84(PrintSouthWallGreenDoor)
1C24:   01 01                                                          ;   01 ADJECTIVES
1C26:   14                                                             ;   TODO WORD
1C27:   02 07                                                          ;   02 SHORT_NAME
1C29:     AF 6E 83 61 81 5B 52                                         ;     GREEN DOOR
;
; Object_0D "GreenDoorH"
1C30: 0B 12                                                            ; word=0B size=0012
1C32: 8C 00 8A                                                         ; room=8C scorePoints=00 bits=8A
1C35:   03 01                                                          ;   03 DESCRIPTION
1C37:     86                                                           ;     86(PrintNorthWallGreedDoor)
1C38:   01 01                                                          ;   01 ADJECTIVES
1C3A:   14                                                             ;   TODO WORD
1C3B:   02 07                                                          ;   02 SHORT_NAME
1C3D:     AF 6E 83 61 81 5B 52                                         ;     GREEN DOOR
;
; Object_0E "RedDoorF"
1C44: 0B 11                                                            ; word=0B size=0011
1C46: 8F 00 88                                                         ; room=8F scorePoints=00 bits=88
1C49:   03 01                                                          ;   03 DESCRIPTION
1C4B:     85                                                           ;     85(PrintNorthWallRedDoor)
1C4C:   01 01                                                          ;   01 ADJECTIVES
1C4E:   13                                                             ;   TODO WORD
1C4F:   02 06                                                          ;   02 SHORT_NAME
1C51:     66 B1 09 15 A3 A0                                            ;     RED DOOR
;
; Object_0F "BlueDoorA"
1C57: 0B 11                                                            ; word=0B size=0011
1C59: 8F 00 8A                                                         ; room=8F scorePoints=00 bits=8A
1C5C:   02 06                                                          ;   02 SHORT_NAME
1C5E:     8F 4E 46 5E 44 A0                                            ;     BLUE DOOR
1C64:   01 01                                                          ;   01 ADJECTIVES
1C66:   15                                                             ;   TODO WORD
1C67:   03 01                                                          ;   03 DESCRIPTION
1C69:     88                                                           ;     88(PrintEastWallBlueDoor)
;
; Object_10 "BlueDoorB"
1C6A: 0B 11                                                            ; word=0B size=0011
1C6C: 90 00 88                                                         ; room=90 scorePoints=00 bits=88
1C6F:   03 01                                                          ;   03 DESCRIPTION
1C71:     89                                                           ;     89(PrintWestWallBlueDoor)
1C72:   01 01                                                          ;   01 ADJECTIVES
1C74:   15                                                             ;   TODO WORD
1C75:   02 06                                                          ;   02 SHORT_NAME
1C77:     8F 4E 46 5E 44 A0                                            ;     BLUE DOOR
;
; Object_11 "BlueDoorC"
1C7D: 0B 11                                                            ; word=0B size=0011
1C7F: 91 00 8A                                                         ; room=91 scorePoints=00 bits=8A
1C82:   03 01                                                          ;   03 DESCRIPTION
1C84:     89                                                           ;     89(PrintWestWallBlueDoor)
1C85:   01 01                                                          ;   01 ADJECTIVES
1C87:   15                                                             ;   TODO WORD
1C88:   02 06                                                          ;   02 SHORT_NAME
1C8A:     8F 4E 46 5E 44 A0                                            ;     BLUE DOOR
;
; Object_12 "BlueDoorD"
1C90: 0B 11                                                            ; word=0B size=0011
1C92: 94 00 88                                                         ; room=94 scorePoints=00 bits=88
1C95:   03 01                                                          ;   03 DESCRIPTION
1C97:     88                                                           ;     88(PrintEastWallBlueDoor)
1C98:   01 01                                                          ;   01 ADJECTIVES
1C9A:   15                                                             ;   TODO WORD
1C9B:   02 06                                                          ;   02 SHORT_NAME
1C9D:     8F 4E 46 5E 44 A0                                            ;     BLUE DOOR
;
; Object_13 "PLAYER"
1CA3: FF 42                                                            ; word=FF size=0042
1CA5: 88 00 80                                                         ; room=88 scorePoints=00 bits=80
1CA8:   08 06                                                          ;   08 TURN SCRIPT
1CAA:     0D 04                                                        ;     while_pass: size=0004
1CAC:       03 13 3A                                                   ;       is_located(room,object) room=13(Room_13) object=3A(Object3A)
1CAF:       9B                                                         ;       9B(??PrintDirs)
1CB0:   0A 31                                                          ;   0A UPON DEATH SCRIPT
1CB2:     0D 2F                                                        ;     while_pass: size=002F
1CB4:       1F 29                                                      ;       print2(msg) size=0029
1CB6:         C7 DE DB 16 CB B9 36 A1 B0 17 F4 59 82 17 73 49          ;         YOU PASS OUT UNDER THAT LAST ATTACK. YOU
1CC6:         55 8B 03 BC 3B C0 AF 54 51 18 43 C2 0D D0 83 61          ;         AWAKEN IN YOUR CELL.
1CD6:         83 7A C7 DE 85 AF 46 61 2E                               ;         ~
1CDF:       2C 13                                                      ;       set_ACTIVE(object) object=13(PLAYER)
1CE1:       19 88                                                      ;       move_ACTIVE(room) room=88(Small square room)
1CE3:   09 02                                                          ;   HIT POINTS
1CE5:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
;
; Object_14 "RedKeyA"
1CE7: 16 21                                                            ; word=16 size=0021
1CE9: 00 00 A0                                                         ; room=00 scorePoints=00 bits=A0
1CEC:   03 12                                                          ;   03 DESCRIPTION
1CEE:     04 10                                                        ;     print(msg) size=0010
1CF0:       5F BE 5B B1 4B 7B 54 45 F3 5F BB 85 9F 15 7F B1            ;       THERE IS A RED KEY HERE.
1D00:   01 01                                                          ;   01 ADJECTIVES
1D02:   13                                                             ;   TODO WORD
1D03:   02 05                                                          ;   02 SHORT_NAME
1D05:     66 B1 17 16 59                                               ;     RED KEY
;
; Object_15 "BluePillA"
1D0A: 17 11                                                            ; word=17 size=0011
1D0C: 82 00 A0                                                         ; room=82 scorePoints=00 bits=A0
1D0F:   03 01                                                          ;   03 DESCRIPTION
1D11:     9D                                                           ;     9D(PrintBluePill)
1D12:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
1D14:     B0                                                           ;     B0(PrintTastesAweful)
1D15:   02 06                                                          ;   02 SHORT_NAME
1D17:     8F 4E 52 5E 46 7A                                            ;     BLUE PILL
;
; Object_16 "WindowHook"
1D1D: 18 2C                                                            ; word=18 size=002C
1D1F: 81 00 A0                                                         ; room=81 scorePoints=00 bits=A0
1D22:   03 1D                                                          ;   03 DESCRIPTION
1D24:     04 1B                                                        ;     print(msg) size=001B
1D26:       5F BE 5B B1 4B 7B 4E 45 11 A0 9B 15 46 98 59 5E            ;       THERE IS A LONG HANDLE WINDOW HOOK HERE.
1D36:       8E 7A 6B A1 81 74 CA 83 2F 62 2E                           ;       ~
1D41:   02 08                                                          ;   02 SHORT_NAME
1D43:     50 D1 89 5B A9 15 8B 9F                                      ;     WINDOW HOOK
;
; Object_17 "Cabinet"
1D4B: 19 80 9C                                                         ; word=19 size=009C
1D4E: 82 00 83                                                         ; room=82 scorePoints=00 bits=83
1D51:   03 2A                                                          ;   03 DESCRIPTION
1D53:     04 28                                                        ;     print(msg) size=0028
1D55:       03 A0 0F A0 F3 17 F3 8C 4B 7B 45 45 B3 46 76 98            ;       ON ONE WALL IS A CABINET. THE CABINET HA
1D65:       56 F4 DB 72 04 53 8F 7A 0A BC 4B 49 56 45 A3 7A            ;       S A TINY HOLE IN IT.
1D75:       A9 15 DB 8B 83 7A 97 7B                                    ;       ~
1D7D:   07 64                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
1D7F:     0E 62                                                        ;     while_fail: size=0062
1D81:       0D 23                                                      ;       while_pass: size=0023
1D83:         0E 06                                                    ;         while_fail: size=0006
1D85:           0A 42                                                  ;           compare_input_to(phrase) phrase="42: UNLOCK .......L WITH u......."
1D87:           0A 3A                                                  ;           compare_input_to(phrase) phrase="3A: OPEN ......O. WITH u......."
1D89:           0A 11                                                  ;           compare_input_to(phrase) phrase="11: OPEN ......O. * *"
1D8B:         04 19                                                    ;         print(msg) size=0019
1D8D:           C7 DE D3 14 E6 96 57 17 5B 61 6B BF 96 C5 5D 9E        ;           YOU CAN'T SEEM TO UNLOCK THE CABINET.
1D9D:           82 17 45 5E B3 46 76 98 2E                             ;           ~
1DA6:       0D 3B                                                      ;       while_pass: size=003B
1DA8:         0E 04                                                    ;         while_fail: size=0004
1DAA:           0A 10                                                  ;           compare_input_to(phrase) phrase="10: LOOK * IN u......."
1DAC:           0A 0B                                                  ;           compare_input_to(phrase) phrase="0B: LOOK * AT u......."
1DAE:         03 82 3B                                                 ;         is_located(room,object) room=82(Dispensary) object=3B(RedKeyB)
1DB1:         04 30                                                    ;         print(msg) size=0030
1DB3:           0C BA D0 47 91 7A 89 17 57 17 56 5E F9 74 7A C4        ;           STRAINING TO SEE THROUGH THE TINY HOLE,
1DC3:           82 17 56 5E A3 7A A9 15 FE 8B 51 18 45 C2 83 48        ;           YOU CAN JUST MAKE OUT A RED KEY.
1DD3:           F5 81 0F BC 17 48 C7 16 03 BC 2F 17 0D 58 5F 63        ;           ~
1DE3:   02 05                                                          ;   02 SHORT_NAME
1DE5:     04 53 8F 7A 54                                               ;     CABINET
;
; Object_18 "Refrigerator"
1DEA: 1A 80 C9                                                         ; word=1A size=00C9
1DED: 92 00 8A                                                         ; room=92 scorePoints=00 bits=8A
1DF0:   03 2E                                                          ;   03 DESCRIPTION
1DF2:     04 2C                                                        ;     print(msg) size=002C
1DF4:       83 7A 5F BE 99 16 C2 B3 95 5F 05 BC B8 A0 23 62            ;       IN THE NORTHEAST CORNER OF THE ROOM THER
1E04:       C3 9E 5F BE 39 17 DB 9F 5F BE 5B B1 4B 7B 4E 45            ;       E IS A LARGE REFRIGERATOR
1E14:       31 49 54 5E 5C 60 77 79 D6 B0 A3 A0                        ;       ~
1E20:   06 3D                                                          ;   06 COMMAND HANDLING IF SECOND NOUN
1E22:     0D 3B                                                        ;     while_pass: size=003B
1E24:       0A 0F                                                      ;       compare_input_to(phrase) phrase="0F: DROP u....... IN u......."
1E26:       1B                                                         ;       set_VAR_to_second_noun()
1E27:       0D 0C                                                      ;       while_pass: size=000C
1E29:         15 02                                                    ;         check_VAR(bits) bits=02(......O.)
1E2B:         A9                                                       ;         A9(PrintTheSecondNoun)
1E2C:         04 07                                                    ;         print(msg) size=0007
1E2E:           4B 7B C9 54 A6 B7 2E                                   ;           IS CLOSED.
1E35:       A8                                                         ;       A8(PrintTheFirstNoun)
1E36:       04 08                                                      ;       print(msg) size=0008
1E38:         CE 65 0B 8E 36 A1 B8 16                                  ;         FALLS OUT OF
1E40:       A9                                                         ;       A9(PrintTheSecondNoun)
1E41:       04 1A                                                      ;       print(msg) size=001A
1E43:         1E A0 D6 9C DB 72 89 67 A3 A0 68 4D AF A0 C7 DE          ;         ONTO THE FLOOR BEFOREYOU CAN CLOSE IT.
1E53:         D3 14 85 96 85 8D 4B 5E 9B C1                            ;         ~
1E5D:       1A                                                         ;       set_VAR_to_first_noun()
1E5E:       10                                                         ;       drop_VAR()
1E5F:   07 4B                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
1E61:     0D 49                                                        ;     while_pass: size=0049
1E63:       0A 11                                                      ;       compare_input_to(phrase) phrase="11: OPEN ......O. * *"
1E65:       1A                                                         ;       set_VAR_to_first_noun()
1E66:       15 02                                                      ;       check_VAR(bits) bits=02(......O.)
1E68:       03 18 42                                                   ;       is_located(room,object) room=18(Room_18) object=42(Object42)
1E6B:       29                                                         ;       print_open_VAR()
1E6C:       17 19 92                                                   ;       move_to(object,room) object=19(HamburgerMeat) room=92(Kitchen)
1E6F:       17 42 00                                                   ;       move_to(object,room) object=42(Object42) room=00(Room_00)
1E72:       04 38                                                      ;       print(msg) size=0038
1E74:         1F D1 9B 96 1B A1 5F A0 96 96 DB 72 68 B1 09 B2          ;         WHEN YOU OPEN THE REFRIGERATOR, SOME HAM
1E84:         2B 62 84 BF 15 EE E7 9F 9B 15 BF 91 B7 B1 8F AF          ;         BURGER MEAT FALLS OUT OF IT ONTO THE FLO
1E94:         96 5F 4B 15 0D 8D C7 16 11 BC 8B 64 11 BC C9 9A          ;         OR.
1EA4:         82 17 48 5E 81 8D 1B B5                                  ;         ~
1EAC:   02 08                                                          ;   02 SHORT_NAME
1EAE:     68 B1 09 B2 2B 62 84 BF                                      ;     REFRIGERATOR
;
; Object_19 "HamburgerMeat"
1EB6: 1B 6E                                                            ; word=1B size=006E
1EB8: 00 00 A0                                                         ; room=00 scorePoints=00 bits=A0
1EBB:   03 19                                                          ;   03 DESCRIPTION
1EBD:     04 17                                                        ;     print(msg) size=0017
1EBF:       5F BE 5B B1 4B 7B 3F B9 4A 5E 64 48 31 C6 23 62            ;       THERE IS SOME HAMBURGER MEAT HERE.
1ECF:       23 92 0A BC 2F 62 2E                                       ;       ~
1ED6:   06 16                                                          ;   06 COMMAND HANDLING IF SECOND NOUN
1ED8:     0D 14                                                        ;     while_pass: size=0014
1EDA:       0A 0F                                                      ;       compare_input_to(phrase) phrase="0F: DROP u....... IN u......."
1EDC:       0E 10                                                      ;       while_fail: size=0010
1EDE:         0D 06                                                    ;         while_pass: size=0006
1EE0:           08 15                                                  ;           is_first_noun(object) object=15(BluePillA)
1EE2:           17 15 19                                               ;           move_to(object,room) object=15(BluePillA) room=19(Room_19)
1EE5:           A0                                                     ;           A0(PrintPillInHamburger)
1EE6:         0D 06                                                    ;         while_pass: size=0006
1EE8:           08 39                                                  ;           is_first_noun(object) object=39(BluePillB)
1EEA:           17 39 19                                               ;           move_to(object,room) object=39(BluePillB) room=19(Room_19)
1EED:           A0                                                     ;           A0(PrintPillInHamburger)
1EEE:   07 2A                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
1EF0:     0D 28                                                        ;     while_pass: size=0028
1EF2:       0A 15                                                      ;       compare_input_to(phrase) phrase="15: EAT u....... * *"
1EF4:       04 21                                                      ;       print(msg) size=0021
1EF6:         F4 4F AB A2 AB AD DB BD 41 6E 73 5D F6 4F 7B 14          ;         BURP! QUITE GOOD, BUT A LITTLE RARE FOR
1F06:         96 8C FF BE 2B 17 5B B1 04 68 7B 16 7B 17 FF B9          ;         MY TASTE.
1F16:         2E                                                       ;         ~
1F17:       17 19 00                                                   ;       move_to(object,room) object=19(HamburgerMeat) room=00(Room_00)
1F1A:   02 0A                                                          ;   02 SHORT_NAME
1F1C:     4F 72 F4 4F B4 6C 67 16 73 49                                ;     HAMBURGER MEAT
;
; Object_1A "GuardDog"
1F26: 08 81 03                                                         ; word=08 size=0103
1F29: 93 00 90                                                         ; room=93 scorePoints=00 bits=90
1F2C:   03 33                                                          ;   03 DESCRIPTION
1F2E:     04 31                                                        ;     print(msg) size=0031
1F30:       58 45 DB 78 35 A1 87 15 2E 49 09 15 CB 6A C5 B5            ;       A VICIOUS GUARD DOG IS CHAINED TO THE SO
1F40:       4B 72 66 98 89 17 82 17 55 5E 36 A1 19 71 46 48            ;       UTH WALL BLOCKING THE SOUTH EXIT.
1F50:       B6 14 5D 9E 91 7A 82 17 55 5E 36 A1 07 71 96 D7            ;       ~
1F60:       2E                                                         ;       ~
1F61:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
1F63:     A1                                                           ;     A1(FeedDogMeat)
1F64:   06 01                                                          ;   06 COMMAND HANDLING IF SECOND NOUN
1F66:     A1                                                           ;     A1(FeedDogMeat)
1F67:   0A 1C                                                          ;   0A UPON DEATH SCRIPT
1F69:     0D 1A                                                        ;     while_pass: size=001A
1F6B:       1F 15                                                      ;       print2(msg) size=0015
1F6D:         C7 DE 4F 24 63 16 C9 97 F3 5F 6B BF 4E 86 16 8A          ;         YOU'VE MANAGED TO KILL THE DOG.
1F7D:         DB 72 79 5B 2E                                           ;         ~
1F82:       1E 1A 3C                                                   ;       swap(object_a,object_b) object_a=(GuardDog)1A object_b=3C(DeadDog)
1F85:   08 80 94                                                       ;   08 TURN SCRIPT
1F88:     0E 80 91                                                     ;     while_fail: size=0091
1F8B:       0D 7D                                                      ;       while_pass: size=007D
1F8D:         0A 09                                                    ;         compare_input_to(phrase) phrase="09: ATTACK ...P.... WITH .v......"
1F8F:         1C 13                                                    ;         set_VAR(object) object=13(PLAYER)
1F91:         0B 77 05                                                 ;         switch(is_less_equal_last_random(value)): size=0077
1F94:           55                                                     ;           is_less_equal_last_random(value) value=55
1F95:           22                                                     ;           IF_NOT_GOTO address=1FB8
1F96:             0D 20                                                ;             while_pass: size=0020
1F98:               1F 1C                                              ;               print2(msg) size=001C
1F9A:                 5F BE 09 15 D6 6A 94 5F C3 B5 1B BC 34 A1 3F 16  ;                 THE DOG TEARS AT YOUR LEG AND DRAWS BLOO
1FAA:                 C3 6A 33 98 EB 5B CB D2 89 4E 71 9E              ;                 D!
1FB6:               1D 06                                              ;               attack_VAR(points) points=06
1FB8:           AF                                                     ;           is_less_equal_last_random(value) value=AF
1FB9:           26                                                     ;           IF_NOT_GOTO address=1FE0
1FBA:             0D 24                                                ;             while_pass: size=0024
1FBC:               1F 20                                              ;               print2(msg) size=0020
1FBE:                 5F BE 09 15 C4 6A 7F 7B DB B5 34 A1 94 14 43 90  ;                 THE DOG BITES YOUR ARM AND YOU CRINGE WI
1FCE:                 33 98 C7 DE E4 14 91 7A 59 5E 82 7B DB 16 81 7A  ;                 TH PAIN!
1FDE:               1D 07                                              ;               attack_VAR(points) points=07
1FE0:           FF                                                     ;           is_less_equal_last_random(value) value=FF
1FE1:           28                                                     ;           IF_NOT_GOTO address=200A
1FE2:             1F 26                                                ;             print2(msg) size=0026
1FE4:               5F BE 09 15 CE 6A 91 C5 4B 62 04 68 51 18 23 C6    ;               THE DOG LUNGES FOR YOUR NECK, BUT YOU PU
1FF4:               65 98 33 89 F6 4F 51 18 52 C2 46 C5 AB 14 8B 54    ;               LL BACK IN TIME!
2004:               83 7A 8F BE EB 5D                                  ;               ~
200A:       1F 10                                                      ;       print2(msg) size=0010
200C:         41 1E C3 9E B9 6E B3 D1 41 D2 99 64 38 A0 E3 06          ;         "WOOF GROWL WOOF WOOF!"
201C:   09 02                                                          ;   HIT POINTS
201E:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
2020:   02 0A                                                          ;   02 SHORT_NAME
2022:     5F BE D3 17 51 54 4B C6 79 5B                                ;     THE VICIOUS DOG
;
; Object_1B "GreenKeyA"
202C: 16 24                                                            ; word=16 size=0024
202E: 8E 00 A0                                                         ; room=8E scorePoints=00 bits=A0
2031:   03 14                                                          ;   03 DESCRIPTION
2033:     04 12                                                        ;     print(msg) size=0012
2035:       5F BE 5B B1 4B 7B 49 45 67 B1 8D 96 3B 63 F4 72            ;       THERE IS A GREEN KEY HERE.
2045:       DB 63                                                      ;       ~
2047:   01 01                                                          ;   01 ADJECTIVES
2049:   14                                                             ;   TODO WORD
204A:   02 06                                                          ;   02 SHORT_NAME
204C:     AF 6E 83 61 BB 85                                            ;     GREEN KEY
;
; Object_1C "RayA"
2052: 03 81 60                                                         ; word=03 size=0160
2055: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
2058:   03 18                                                          ;   03 DESCRIPTION
205A:     04 16                                                        ;     print(msg) size=0016
205C:       DB B0 57 17 75 61 89 17 AF 14 3B 15 D0 60 D6 6A            ;       RAY SEEMS TO BE EYEING THE WALLS.
206C:       DB 72 0E D0 2F 8E                                          ;       ~
2072:   09 02                                                          ;   HIT POINTS
2074:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
2076:   0B 81 2D                                                       ;   0B COMMAND HANDLING IF GIVEN COMMAND
2079:     0E 81 2A                                                     ;     while_fail: size=012A
207C:       0D 80 DF                                                   ;       while_pass: size=00DF
207F:         0E 0A                                                    ;         while_fail: size=000A
2081:           0A 01                                                  ;           compare_input_to(phrase) phrase="01: NORTH * * *"
2083:           0A 02                                                  ;           compare_input_to(phrase) phrase="02: SOUTH * * *"
2085:           0A 03                                                  ;           compare_input_to(phrase) phrase="03: EAST * * *"
2087:           0A 04                                                  ;           compare_input_to(phrase) phrase="04: WEST * * *"
2089:           0A 0A                                                  ;           compare_input_to(phrase) phrase="0A: LOOK * * *"
208B:         1F 0F                                                    ;         print2(msg) size=000F
208D:           DB B0 2F 17 84 A6 0B C0 DB 72 10 53 57 17 45           ;           RAY REPORTS HE CAN SEE
209C:         1C 38                                                    ;         set_VAR(object) object=38(SYSTEM)
209E:         10                                                       ;         drop_VAR()
209F:         2C 38                                                    ;         set_ACTIVE(object) object=38(SYSTEM)
20A1:         0E 80 B8                                                 ;         while_fail: size=00B8
20A4:           0D 33                                                  ;           while_pass: size=0033
20A6:             01 3D                                                ;             is_in_pack_or_current_room(object) object=3D(SecretDoor)
20A8:             1F 2E                                                ;             print2(msg) size=002E
20AA:               55 45 E4 5F 73 62 81 5B 8A AF 2F 62 19 EE 85 73    ;               A SECRET DOOR HERE, WHICH MAY LEAD TO ES
20BA:               0F 71 3B 4A E3 8B 16 58 C7 9C 53 B7 FF A4 AF 14    ;               CAPE. BESIDES THAT, THERE IS
20CA:               46 B8 4B 62 5B BE 73 C1 5F BE 5B B1 4B 7B          ;               ~
20D8:             0C                                                   ;             fail()
20D9:           0D 3D                                                  ;           while_pass: size=003D
20DB:             03 00 22                                             ;             is_located(room,object) room=00(Room_00) object=22(PicassoA)
20DE:             03 88 1C                                             ;             is_located(room,object) room=88(Small square room) object=1C(RayA)
20E1:             1F 34                                                ;             print2(msg) size=0034
20E3:               5B BE 04 BC 51 63 33 98 5F BE 99 16 C2 B3 F3 17    ;               THAT BEYOND THE NORTH WALL IS A POSSIBLE
20F3:               F3 8C 4B 7B 52 45 E5 A0 B6 78 47 5E 53 B7 DB A4    ;               ESCAPE ROUTE. BESIDES THAT, THERE IS
2103:               07 B3 FF BD AF 14 46 B8 4B 62 5B BE 73 C1 5F BE    ;               ~
2113:               5B B1 4B 7B                                        ;               ~
2117:             0C                                                   ;             fail()
2118:           0D 06                                                  ;           while_pass: size=0006
211A:             0A 03                                                ;             compare_input_to(phrase) phrase="03: EAST * * *"
211C:             21 03 00 00                                          ;             execute_phrase(phrase,first_noun,second_noun) phrase="03: EAST * * *" firstNoun=00 secondNoun=00
2120:           0D 06                                                  ;           while_pass: size=0006
2122:             0A 04                                                ;             compare_input_to(phrase) phrase="04: WEST * * *"
2124:             21 04 00 00                                          ;             execute_phrase(phrase,first_noun,second_noun) phrase="04: WEST * * *" firstNoun=00 secondNoun=00
2128:           0D 06                                                  ;           while_pass: size=0006
212A:             0A 01                                                ;             compare_input_to(phrase) phrase="01: NORTH * * *"
212C:             21 01 00 00                                          ;             execute_phrase(phrase,first_noun,second_noun) phrase="01: NORTH * * *" firstNoun=00 secondNoun=00
2130:           0D 06                                                  ;           while_pass: size=0006
2132:             0A 02                                                ;             compare_input_to(phrase) phrase="02: SOUTH * * *"
2134:             21 02 00 00                                          ;             execute_phrase(phrase,first_noun,second_noun) phrase="02: SOUTH * * *" firstNoun=00 secondNoun=00
2138:           1F 22                                                  ;           print2(msg) size=0022
213A:             06 9A 90 73 5B 70 B7 1C F3 B9 5B 4D 3F B9 4E 5E      ;             NOTHING. "MUST BE SOME LEAD-LINED WALLS!
214A:             86 5F C3 EA 66 98 F3 17 0D 8D E3 06 DB 72 1B B7      ;             " HE SAYS.
215A:             5B BB                                                ;             ~
215C:         2C 1C                                                    ;         set_ACTIVE(object) object=1C(RayA)
215E:       0D 45                                                      ;       while_pass: size=0045
2160:         0E 06                                                    ;         while_fail: size=0006
2162:           0A 11                                                  ;           compare_input_to(phrase) phrase="11: OPEN ......O. * *"
2164:           0A 42                                                  ;           compare_input_to(phrase) phrase="42: UNLOCK .......L WITH u......."
2166:           0A 09                                                  ;           compare_input_to(phrase) phrase="09: ATTACK ...P.... WITH .v......"
2168:         1F 3B                                                    ;         print2(msg) size=003B
216A:           DB B0 63 16 B5 85 7B 14 67 66 7F 4E 96 14 EF BD        ;           RAY MAKES A FEEBLE ATTEMPT AND THEN DRAW
217A:           33 A7 8E 48 82 17 83 61 EB 5B CB D2 C5 4C 5B 89        ;           S BACK. "SORRY, I'VE BEEN RATHER ANEMIC
218A:           A1 1D 83 B3 0B EE 4F 24 AF 14 83 61 D6 B0 F4 72        ;           LATELY!"
219A:           90 14 6B 61 CE 51 7F 49 F9 8E 22                       ;           ~
21A5:       9A                                                         ;       9A(??CommandResponse)
21A6:   08 06                                                          ;   08 TURN SCRIPT
21A8:     0D 04                                                        ;     while_pass: size=0004
21AA:       9C                                                         ;       9C(??MoveHoudiniC)
21AB:       1C 1C                                                      ;       set_VAR(object) object=1C(RayA)
21AD:       9E                                                         ;       9E(PrintObjectEntersRoom)
21AE:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
21B0:     AB                                                           ;     AB(AttackPerson)
21B1:   02 02                                                          ;   02 SHORT_NAME
21B3:     DB B0                                                        ;     RAY
;
; Object_1D "RayB"
21B5: 03 80 AE                                                         ; word=03 size=00AE
21B8: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
21BB:   03 80 A8                                                       ;   03 DESCRIPTION
21BE:     0D 80 A5                                                     ;     while_pass: size=00A5
21C1:       04 80 9F                                                   ;       print(msg) size=009F
21C4:         4F 45 83 48 83 7A 94 5A FB C0 4F A1 CE B0 0B 8E          ;         A MAN IN DIRTY OVERALLS AND WEARING GOGG
21D4:         8E 48 F7 17 33 49 AB 98 39 6E BF 6D C3 B5 AC A6          ;         LES APPROACHES YOU AND INTRODUCES HIMSEL
21E4:         05 9E F5 72 51 18 43 C2 33 98 9E 7A F6 B2 D7 C3          ;         F. "HI! MY NAME IS XRAY JOHNSON, BUT YOU
21F4:         CA B5 75 7A 40 61 3C F4 79 73 7B 16 8B 16 1B 92          ;         CAN CALL ME RAY. I HAVE XRAY VISION, YO
2204:         4B 7B EB D8 4C DB 28 9F 40 B9 04 EE 73 C6 C7 DE          ;         U KNOW. SAY, YOU BETTER HAVE THAT SPOT O
2214:         D3 14 85 96 46 48 67 16 2B 17 DB E0 4A 77 CF 49          ;         N YOUR LEFT LUNG CHECKED BY A DOCTOR!"
2224:         2C 18 3B 4A 15 CB C0 7A 1B EE 1B A1 19 87 5B D4          ;         ~
2234:         1B B7 1B EE 1B A1 76 4D F4 BD 9B 15 5B CA 5B BE          ;         ~
2244:         15 BC 86 A6 C0 16 51 18 23 C6 E8 8B 0E BC 91 C5          ;         ~
2254:         DA 14 DD 5F F3 5F 7B 50 46 45 66 9E A1 A0 22             ;         ~
2263:       1E 1C 1D                                                   ;       swap(object_a,object_b) object_a=(RayA)1C object_b=1D(RayB)
;
; Object_1E "NapoleanA"
2266: 02 77                                                            ; word=02 size=0077
2268: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
226B:   03 01                                                          ;   03 DESCRIPTION
226D:     97                                                           ;     97(PrintNapolean)
226E:   02 06                                                          ;   02 SHORT_NAME
2270:     D2 97 BF 9F 03 A0                                            ;     NAPOLEON
2276:   0B 58                                                          ;   0B COMMAND HANDLING IF GIVEN COMMAND
2278:     0E 56                                                        ;     while_fail: size=0056
227A:       0D 53                                                      ;       while_pass: size=0053
227C:         0E 06                                                    ;         while_fail: size=0006
227E:           0A 11                                                  ;           compare_input_to(phrase) phrase="11: OPEN ......O. * *"
2280:           0A 42                                                  ;           compare_input_to(phrase) phrase="42: UNLOCK .......L WITH u......."
2282:           0A 09                                                  ;           compare_input_to(phrase) phrase="09: ATTACK ...P.... WITH .v......"
2284:         1A                                                       ;         set_VAR_to_first_noun()
2285:         15 08                                                    ;         check_VAR(bits) bits=08(....A...)
2287:         1F 46                                                    ;         print2(msg) size=0046
2289:           D2 97 BF 9F 03 A0 AB 6E 8B 4F 96 7B BF 14 0A BC        ;           NAPOLEON GRABS IT, BUT HE CAN'T BUDGE IT
2299:           45 5E 85 48 04 BC 01 C4 4B 5E AB BB DB 72 74 C0        ;           ! HE TURNS TO YOU AND MUMBLES SOMETHING
22A9:           8B 9A 6B BF C7 DE 90 14 0F 58 64 C5 F5 8B 61 17        ;           ABOUT BEING RATHER TIRED.
22B9:           36 92 90 73 C3 6A 07 4F 04 BC D0 60 D4 6A 82 49        ;           ~
22C9:           23 62 94 BE 17 60                                      ;           ~
22CF:       9A                                                         ;       9A(??CommandResponse)
22D0:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
22D2:     AB                                                           ;     AB(AttackPerson)
22D3:   08 06                                                          ;   08 TURN SCRIPT
22D5:     0D 04                                                        ;     while_pass: size=0004
22D7:       9C                                                         ;       9C(??MoveHoudiniC)
22D8:       1C 1E                                                      ;       set_VAR(object) object=1E(NapoleanA)
22DA:       9E                                                         ;       9E(PrintObjectEntersRoom)
22DB:   09 02                                                          ;   HIT POINTS
22DD:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
;
; Object_1F "Object1F"
22DF: 02 0B                                                            ; word=02 size=000B
22E1: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
22E4:   03 06                                                          ;   03 DESCRIPTION
22E6:     0D 04                                                        ;     while_pass: size=0004
22E8:       96                                                         ;       96(PrintNapoleanIntro)
22E9:       1E 1E 1F                                                   ;       swap(object_a,object_b) object_a=(NapoleanA)1E object_b=1F(Object1F)
;
; Object_20 "NapoleanB"
22EC: 02 80 97                                                         ; word=02 size=0097
22EF: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
22F2:   03 01                                                          ;   03 DESCRIPTION
22F4:     97                                                           ;     97(PrintNapolean)
22F5:   02 06                                                          ;   02 SHORT_NAME
22F7:     D2 97 BF 9F 03 A0                                            ;     NAPOLEON
22FD:   0B 78                                                          ;   0B COMMAND HANDLING IF GIVEN COMMAND
22FF:     0E 76                                                        ;     while_fail: size=0076
2301:       0D 73                                                      ;       while_pass: size=0073
2303:         0E 06                                                    ;         while_fail: size=0006
2305:           0A 11                                                  ;           compare_input_to(phrase) phrase="11: OPEN ......O. * *"
2307:           0A 42                                                  ;           compare_input_to(phrase) phrase="42: UNLOCK .......L WITH u......."
2309:           0A 09                                                  ;           compare_input_to(phrase) phrase="09: ATTACK ...P.... WITH .v......"
230B:         1A                                                       ;         set_VAR_to_first_noun()
230C:         15 08                                                    ;         check_VAR(bits) bits=08(....A...)
230E:         0E 66                                                    ;         while_fail: size=0066
2310:           0D 49                                                  ;           while_pass: size=0049
2312:             15 02                                                ;             check_VAR(bits) bits=02(......O.)
2314:             1F 0A                                                ;             print2(msg) size=000A
2316:               D2 97 BF 9F 03 A0 AB 6E 8B 4F                      ;               NAPOLEON GRABS
2320:             A8                                                   ;             A8(PrintTheFirstNoun)
2321:             1F 0C                                                ;             print2(msg) size=000C
2323:               8E 48 BF 14 0D BA D6 15 C2 16 81 61                ;               AND BUSTS IT OPEN!
232F:             29                                                   ;             print_open_VAR()
2330:             0E 29                                                ;             while_fail: size=0029
2332:               0D 25                                              ;               while_pass: size=0025
2334:                 08 3D                                            ;                 is_first_noun(object) object=3D(SecretDoor)
2336:                 1F 20                                            ;                 print2(msg) size=0020
2338:                   5F BE 57 17 AF 55 06 BC 44 A0 3F 16 0D 47 89 17;                   THE SECRET DOOR LEADS TO ESCAPE! YOU'VE
2348:                   35 15 12 53 EB 5D C7 DE 4F 24 63 16 DB 59 71 7B;                   MADE IT!
2358:                 24                                               ;                 endless_loop()
2359:               14                                                 ;               execute_and_reverse_status:
235A:               0C                                                 ;               fail()
235B:           0D 19                                                  ;           while_pass: size=0019
235D:             1F 0E                                                ;             print2(msg) size=000E
235F:               D2 97 BF 9F 03 A0 72 B1 BE A0 D6 B5 56 72          ;               NAPOLEON REPORTS THAT
236D:             A8                                                   ;             A8(PrintTheFirstNoun)
236E:             1F 06                                                ;             print2(msg) size=0006
2370:               4B 7B 5F A0 1B 9C                                  ;               IS OPEN.
2376:       9A                                                         ;       9A(??CommandResponse)
2377:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
2379:     AB                                                           ;     AB(AttackPerson)
237A:   08 06                                                          ;   08 TURN SCRIPT
237C:     0D 04                                                        ;     while_pass: size=0004
237E:       9C                                                         ;       9C(??MoveHoudiniC)
237F:       1C 20                                                      ;       set_VAR(object) object=20(NapoleanB)
2381:       9E                                                         ;       9E(PrintObjectEntersRoom)
2382:   09 02                                                          ;   HIT POINTS
2384:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
;
; Object_21 "Object21"
2386: 02 0B                                                            ; word=02 size=000B
2388: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
238B:   03 06                                                          ;   03 DESCRIPTION
238D:     0D 04                                                        ;     while_pass: size=0004
238F:       96                                                         ;       96(PrintNapoleanIntro)
2390:       1E 20 21                                                   ;       swap(object_a,object_b) object_a=(NapoleanB)20 object_b=21(Object21)
;
; Object_22 "PicassoA"
2393: 05 25                                                            ; word=05 size=0025
2395: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
2398:   03 01                                                          ;   03 DESCRIPTION
239A:     99                                                           ;     99(PrintPicasso)
239B:   02 05                                                          ;   02 SHORT_NAME
239D:     85 A5 65 49 4F                                               ;     PICASSO
23A2:   0B 01                                                          ;   0B COMMAND HANDLING IF GIVEN COMMAND
23A4:     9A                                                           ;     9A(??CommandResponse)
23A5:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
23A7:     AB                                                           ;     AB(AttackPerson)
23A8:   08 0C                                                          ;   08 TURN SCRIPT
23AA:     0E 0A                                                        ;     while_fail: size=000A
23AC:       0D 04                                                      ;       while_pass: size=0004
23AE:         9C                                                       ;         9C(??MoveHoudiniC)
23AF:         1C 22                                                    ;         set_VAR(object) object=22(PicassoA)
23B1:         9E                                                       ;         9E(PrintObjectEntersRoom)
23B2:       14                                                         ;       execute_and_reverse_status:
23B3:       1C 3F                                                      ;       set_VAR(object) object=3F(PaintedDoorB)
23B5:       10                                                         ;       drop_VAR()
23B6:   09 02                                                          ;   HIT POINTS
23B8:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
;
; Object_23 "Object23"
23BA: 05 0B                                                            ; word=05 size=000B
23BC: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
23BF:   03 06                                                          ;   03 DESCRIPTION
23C1:     0D 04                                                        ;     while_pass: size=0004
23C3:       98                                                         ;       98(PrintPicassoIntro)
23C4:       1E 22 23                                                   ;       swap(object_a,object_b) object_a=(PicassoA)22 object_b=23(Object23)
;
; Object_24 "PicassoB"
23C7: 05 34                                                            ; word=05 size=0034
23C9: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
23CC:   03 01                                                          ;   03 DESCRIPTION
23CE:     99                                                           ;     99(PrintPicasso)
23CF:   02 05                                                          ;   02 SHORT_NAME
23D1:     85 A5 65 49 4F                                               ;     PICASSO
23D6:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
23D8:     AB                                                           ;     AB(AttackPerson)
23D9:   0B 01                                                          ;   0B COMMAND HANDLING IF GIVEN COMMAND
23DB:     9A                                                           ;     9A(??CommandResponse)
23DC:   08 1B                                                          ;   08 TURN SCRIPT
23DE:     0E 19                                                        ;     while_fail: size=0019
23E0:       0D 08                                                      ;       while_pass: size=0008
23E2:         14                                                       ;         execute_and_reverse_status:
23E3:         03 88 24                                                 ;         is_located(room,object) room=88(Small square room) object=24(PicassoB)
23E6:         1C 3F                                                    ;         set_VAR(object) object=3F(PaintedDoorB)
23E8:         10                                                       ;         drop_VAR()
23E9:         0C                                                       ;         fail()
23EA:       0D 07                                                      ;       while_pass: size=0007
23EC:         03 88 24                                                 ;         is_located(room,object) room=88(Small square room) object=24(PicassoB)
23EF:         17 3E 88                                                 ;         move_to(object,room) object=3E(PaintedDoorA) room=88(Small square room)
23F2:         0C                                                       ;         fail()
23F3:       0D 04                                                      ;       while_pass: size=0004
23F5:         9C                                                       ;         9C(??MoveHoudiniC)
23F6:         1C 24                                                    ;         set_VAR(object) object=24(PicassoB)
23F8:         9E                                                       ;         9E(PrintObjectEntersRoom)
23F9:   09 02                                                          ;   HIT POINTS
23FB:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
;
; Object_25 "Object25"
23FD: 05 0B                                                            ; word=05 size=000B
23FF: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
2402:   03 06                                                          ;   03 DESCRIPTION
2404:     0D 04                                                        ;     while_pass: size=0004
2406:       98                                                         ;       98(PrintPicassoIntro)
2407:       1E 24 25                                                   ;       swap(object_a,object_b) object_a=(PicassoB)24 object_b=25(Object25)
;
; Object_26 "MerlinA"
240A: 06 80 FD                                                         ; word=06 size=00FD
240D: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
2410:   03 25                                                          ;   03 DESCRIPTION
2412:     04 23                                                        ;     print(msg) size=0023
2414:       34 92 90 8C D5 15 8F 16 2C 49 B3 E0 1B 54 C3 9A            ;       MERLIN IS NEARBY, CHANTING AND GESTICULA
2424:       AB 98 8E 48 77 15 03 BA 2E 56 83 49 AB 98 73 49            ;       TING AT YOU.
2434:       C7 DE 2E                                                   ;       ~
2437:   02 04                                                          ;   02 SHORT_NAME
2439:     34 92 90 8C                                                  ;     MERLIN
243D:   0B 01                                                          ;   0B COMMAND HANDLING IF GIVEN COMMAND
243F:     9A                                                           ;     9A(??CommandResponse)
2440:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
2442:     AB                                                           ;     AB(AttackPerson)
2443:   08 80 C0                                                       ;   08 TURN SCRIPT
2446:     0E 80 BD                                                     ;     while_fail: size=00BD
2449:       0D 04                                                      ;       while_pass: size=0004
244B:         9C                                                       ;         9C(??MoveHoudiniC)
244C:         1C 26                                                    ;         set_VAR(object) object=26(MerlinA)
244E:         9E                                                       ;         9E(PrintObjectEntersRoom)
244F:       0B 80 B4 05                                                ;       switch(is_less_equal_last_random(value)): size=00B4
2453:         08                                                       ;         is_less_equal_last_random(value) value=08
2454:         30                                                       ;         IF_NOT_GOTO address=2485
2455:           1F 2E                                                  ;           print2(msg) size=002E
2457:             34 92 90 8C 53 17 6E DF 6E 13 71 61 F3 9B 45 77      ;             MERLIN SAYS, "DEMON, I COMMAND YOU! REVE
2467:             EF 9F 8E 48 51 18 EB C1 78 B1 8E 5F 89 17 67 16      ;             AL TO ME THE DOOR OF ESCAPE!"
2477:             82 17 46 5E 44 A0 B8 16 35 15 12 53 EC 5D            ;             ~
2485:         10                                                       ;         is_less_equal_last_random(value) value=10
2486:         42                                                       ;         IF_NOT_GOTO address=24C9
2487:           1F 40                                                  ;           print2(msg) size=0040
2489:             34 92 90 8C 77 15 0F BA 75 B1 96 14 51 18 43 C2      ;             MERLIN GESTURES AT YOU AND SAYS, "I CAN'
2499:             33 98 1B B7 33 BB FB 1B 10 53 F3 23 8E C5 3D 62      ;             T UNDERSTAND IT. I MUST HAVE CONJURED TH
24A9:             50 BD 0B 58 9B C1 4F 77 66 C6 9B 15 5B CA 40 55      ;             E WRONG DEMON."
24B9:             F4 81 F3 5F 5F BE 04 18 11 A0 FF 14 C0 93 63 F4      ;             ~
24C9:         18                                                       ;         is_less_equal_last_random(value) value=18
24CA:         3B                                                       ;         IF_NOT_GOTO address=2506
24CB:           1F 39                                                  ;           print2(msg) size=0039
24CD:             34 92 90 8C E9 16 9E 7A C3 B5 1B BC 3E A1 6F 13      ;             MERLIN POINTS AT YOU, "EYE OF NEUTRON, W
24DD:             1B DD C3 9E 77 98 F9 BF F3 9B 14 D0 11 BC 8A 64      ;             ART OF HOG, DEMON DO THY WILL, THEN BE G
24ED:             0E 9F FF 14 C0 93 09 15 82 17 59 DB 46 7A 16 EE      ;             ONE!"
24FD:             F0 72 AF 14 81 15 59 98 22                           ;             ~
2506:   09 02                                                          ;   HIT POINTS
2508:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
;
; Object_27 "MerlinB"
250A: 06 6E                                                            ; word=06 size=006E
250C: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
250F:   03 69                                                          ;   03 DESCRIPTION
2511:     0D 67                                                        ;     while_pass: size=0067
2513:       04 62                                                      ;       print(msg) size=0062
2515:         83 48 8D 48 30 79 0F BC 83 48 83 7A 44 45 45 8B          ;         AN ANCIENT MAN IN A BLACK CLOAK AND POIN
2525:         C5 83 73 8D C3 83 33 98 7B A6 BF 9A 0A 58 73 49          ;         TED HAT GESTURES AT YOU, "DEMON! I HAVE
2535:         B5 6C 74 C0 4B 62 73 49 C7 DE FC ED EF 59 01 A0          ;         SUMMONED YOU! I AM YOUR MASTER, MERLIN!
2545:         BB 15 58 72 55 5E 6F C5 0F A0 1B 58 19 A1 BB 15          ;         YOU MUST OBEY MY COMMAND!"
2555:         5B 48 C7 DE 8F AF 66 49 46 62 67 16 83 B2 2B 96          ;         ~
2565:         C7 DE 77 16 F3 B9 2F 9E 4F DB 45 DB EF 9F 8E 48          ;         ~
2575:         E3 06                                                    ;         ~
2577:       1E 26 27                                                   ;       swap(object_a,object_b) object_a=(MerlinA)26 object_b=27(MerlinB)
;
; Object_28 "UnconsciousDoctorA"
257A: 07 54                                                            ; word=07 size=0054
257C: 00 00 80                                                         ; room=00 scorePoints=00 bits=80
257F:   03 27                                                          ;   03 DESCRIPTION
2581:     04 25                                                        ;     print(msg) size=0025
2583:       5F BE 7C 13 8E 5F 86 19 66 9E A3 A0 03 BA F3 8C            ;       THE "REAL" DOCTOR STILL LIES UNCONSCIOUS
2593:       87 8C D7 B5 21 98 95 9A C7 7A CB B5 96 96 DB 72            ;       IN THE CORNER.
25A3:       44 55 74 98 2E                                             ;       ~
25A8:   02 0C                                                          ;   02 SHORT_NAME
25AA:     8D C5 0D A0 C7 7A C6 B5 66 9E A3 A0                          ;     UNCONCIOUS DOCTOR
25B6:   0B 14                                                          ;   0B COMMAND HANDLING IF GIVEN COMMAND
25B8:     1F 12                                                        ;     print2(msg) size=0012
25BA:       5F BE 09 15 09 56 8B AF D7 B5 21 98 95 9A C7 7A            ;       THE DOCTOR IS UNCONSCIOUS.
25CA:       5B BB                                                      ;       ~
25CC:   09 02                                                          ;   HIT POINTS
25CE:   46 01                                                          ;   maxHitPoints=46 currentHitPoints=01
;
; Object_29 "UnconsciousDoctorB"
25D0: 07 80 F5                                                         ; word=07 size=00F5
25D3: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
25D6:   03 80 EF                                                       ;   03 DESCRIPTION
25D9:     0D 80 EC                                                     ;     while_pass: size=00EC
25DC:       04 80 E6                                                   ;       print(msg) size=00E6
25DF:         5F BE 5B B1 4B 7B 4F 45 83 48 83 7A 55 45 EB BF          ;         THERE IS A MAN IN A STRAIT JACKET IN THE
25EF:         73 7B C5 7E B6 85 D0 15 82 17 45 5E B8 A0 47 62          ;         CORNER. HE LOOKS UP AT YOU AND MUMBLES,
25FF:         9F 15 49 16 A5 9F B2 17 96 14 51 18 43 C2 33 98          ;         "OH...IT IS TERRIBLE...THE DOCTOR HAS B
260F:         AF 94 7F 4E 33 BB FA 1C FF F9 73 7B 4B 7B F4 BD          ;         ECOME THE PATIENT AND THE PATIENT THE DO
261F:         04 B2 FF 8B F6 F9 DB 72 75 5B 84 BF 9B 15 C4 B5          ;         CTOR...LISTEN TO ME...I AM THE DOCTOR...
262F:         E1 5F 1B 92 5F BE DB 16 87 BE B3 9A 8E 48 82 17          ;         YOU MUST GO TO THE AUTHORITIES AND TELL
263F:         52 5E 83 49 9E 61 82 17 46 5E 66 9E C7 A0 EE F9          ;         THEM OF THIS TRAVESTY! HURRY, BEFORE IT
264F:         66 7B 83 61 6B BF 3F 92 EB F9 8F 14 82 17 46 5E          ;         IS TOO LATE." HIS EYES ROLL BACK INTO HI
265F:         66 9E C7 A0 FB F9 1B A1 B5 94 09 BC D6 9C D6 9C          ;         S HEAD AND HE PASSES OUT.
266F:         DB 72 B6 49 84 74 83 7B 4B 62 8E 48 7F 17 F3 8C          ;         ~
267F:         5F BE 51 90 96 64 95 73 8C 17 CF 49 13 BA CA 06          ;         ~
268F:         3C C6 B3 E0 68 4D AF A0 D6 15 D5 15 89 17 CE 9C          ;         ~
269F:         7F 49 63 F4 95 73 3B 15 4B 62 FE B2 04 8A DD 46          ;         ~
26AF:         D0 15 6B BF 95 73 9F 15 F3 46 8E 48 9F 15 DB 16          ;         ~
26BF:         D7 B9 D1 B5 97 C6                                        ;         ~
26C5:       1E 28 29                                                   ;       swap(object_a,object_b) object_a=(UnconsciousDoctorA)28 object_b=29(UnconsciousDoctorB)
;
; Object_2A "HoudiniA"
26C8: 04 81 0A                                                         ; word=04 size=010A
26CB: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
26CE:   03 29                                                          ;   03 DESCRIPTION
26D0:     04 27                                                        ;     print(msg) size=0027
26D2:       87 74 90 5A 4B 77 D9 B5 16 B2 90 73 5B 70 FD 1B            ;       HOUDINI IS WRITHING. "I'LL BE DOWN FROM
26E2:       F3 8C 5B 4D 89 5B 88 96 FF B2 9F 15 5B B1 83 7A            ;       HERE IN A MINUTE!"
26F2:       4F 45 9F 7A D9 BD 22                                       ;       ~
26F9:   02 05                                                          ;   02 SHORT_NAME
26FB:     87 74 90 5A 49                                               ;     HOUDINI
2700:   07 80 CB                                                       ;   07 COMMAND HANDLING IF FIRST NOUN
2703:     0D 80 C8                                                     ;     while_pass: size=00C8
2706:       0E 04                                                      ;       while_fail: size=0004
2708:         0A 48                                                    ;         compare_input_to(phrase) phrase="48: LOWER u....... * *"
270A:         0A 12                                                    ;         compare_input_to(phrase) phrase="12: PULL u....... * *"
270C:       04 80 BC                                                   ;       print(msg) size=00BC
270F:         C7 DE 3F 16 0A BC 26 A1 93 7A 09 15 26 D2 BF 14          ;         YOU LET HOUDINI DOWN, BUT YOU ARE UNABLE
271F:         1B BC 1B A1 2F 49 B0 17 B6 46 56 5E D4 9C 71 61          ;         TO REMOVE HIS STRAIT JACKET. HOUDINI SA
272F:         5B CA 95 73 66 17 CB B0 0C BC DD 46 97 62 A9 15          ;         YS, "YOU DIDN'T HAVE TO DO THAT! I WOULD
273F:         03 C4 FB 98 1B B7 33 BB 91 1E 46 C2 08 79 F3 23          ;         HAVE BEEN DOWN IN A MINUTE. BUT I'LL ST
274F:         58 72 56 5E C6 9C D6 9C 56 72 CB 06 01 18 3E C5          ;         ILL TAKE YOU WITH ME WHEN I ESCAPE, JUST
275F:         9B 15 5B CA 67 4D 86 96 80 A1 D0 15 7B 14 D0 92          ;         AS SOON AS I GET OUT OF THIS THING!" HE
276F:         7F C6 44 F4 73 C6 9E 77 15 8A 8E BE 16 8A 17 48          ;         BEGINS WRESTLING WITH HIS STRAIT JACKET
277F:         51 18 59 C2 82 7B 67 16 FA 17 83 61 47 77 53 B7          ;         .
278F:         FE A4 FF 15 F3 B9 4B 49 41 B9 83 96 CB B5 77 15          ;         ~
279F:         11 BC 73 C6 C3 9E 63 BE D6 B5 90 73 6C 6A 9F 15          ;         ~
27AF:         AF 14 50 6D D9 B5 75 B1 03 BF AB 98 56 D1 0A 71          ;         ~
27BF:         4B 7B 0C BA D6 47 EB 15 97 54 9B C1                      ;         ~
27CB:       1E 2A 2C                                                   ;       swap(object_a,object_b) object_a=(HoudiniA)2A object_b=2C(HoudiniC)
27CE:   0B 01                                                          ;   0B COMMAND HANDLING IF GIVEN COMMAND
27D0:     9A                                                           ;     9A(??CommandResponse)
27D1:   09 02                                                          ;   HIT POINTS
27D3:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
;
; Object_2B "HoudiniB"
27D5: 04 80 D9                                                         ; word=04 size=00D9
27D8: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
27DB:   03 80 D3                                                       ;   03 DESCRIPTION
27DE:     0D 80 D0                                                     ;     while_pass: size=00D0
27E1:       04 80 CA                                                   ;       print(msg) size=00CA
27E4:         5F BE 5B B1 4B 7B 48 45 98 C5 4E DB 3D A0 91 7A          ;         THERE IS A FUNNY LOOKING MAN HANGING TIE
27F4:         63 16 8A 96 91 48 91 7A 83 17 F3 5F 56 D1 03 71          ;         D WITH A ROPE BY HIS FEET TO THE CEILING
2804:         39 17 DB A4 7B 50 95 73 4F 15 73 62 6B BF 5F BE          ;         . HE IS WEARING A STRAIT JACKET. HE TURN
2814:         D7 14 43 7A CF 98 9F 15 D5 15 F7 17 33 49 AB 98          ;         S HIS HEAD TOWARD YOU, "HELLO! I AM THE
2824:         55 45 EB BF 73 7B C5 7E B6 85 4A F4 56 5E 38 C6          ;         GREAT HOUDINI! NO BONDS CAN HOLD ME, NO
2834:         CA B5 4B 7B E3 72 16 58 73 A1 33 B1 C7 DE FC ED          ;         LOCKS CAN RESIST ME! WAIT, LET ME SHOW Y
2844:         EE 72 69 8D BB 15 5B 48 5F BE 84 15 96 5F A9 15          ;         OU! I CAN GET US BOTH OUT OF THIS PLACE!
2854:         03 C4 F9 98 99 16 B9 14 4D 98 D3 14 8A 96 BE 9F          ;         " HE BEGINS WRIGGLING.
2864:         67 16 10 EE CE 9C 5D 9E C5 B5 83 48 75 B1 66 7B          ;         ~
2874:         67 16 D9 06 D6 47 0E EE 73 62 1B 92 29 B8 DB CE          ;         ~
2884:         19 A1 BB 15 10 53 77 15 17 BC C4 B5 02 A1 C7 16          ;         ~
2894:         11 BC 96 64 95 73 E6 16 D7 46 E3 06 DB 72 69 4D          ;         ~
28A4:         9D 7A 04 18 79 79 90 8C 5B 70                            ;         ~
28AE:       1E 2A 2B                                                   ;       swap(object_a,object_b) object_a=(HoudiniA)2A object_b=2B(HoudiniB)
;
; Object_2C "HoudiniC"
28B1: 04 80 93                                                         ; word=04 size=0093
28B4: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
28B7:   03 36                                                          ;   03 DESCRIPTION
28B9:     04 34                                                        ;     print(msg) size=0034
28BB:       87 74 90 5A 4B 77 D9 B5 75 B1 03 BF AB 98 56 D1            ;       HOUDINI IS WRESTLING WITH HIS STRAIT JAC
28CB:       0A 71 4B 7B 0C BA D6 47 EB 15 97 54 9B C1 FD 1B            ;       KET. "I'LL BE OUT OF THIS IN NO TIME!"
28DB:       F3 8C 5B 4D 36 A1 B8 16 82 17 4B 7B 83 7A EB 99            ;       ~
28EB:       8F BE EC 5D                                                ;       ~
28EF:   02 05                                                          ;   02 SHORT_NAME
28F1:     87 74 90 5A 49                                               ;     HOUDINI
28F6:   08 45                                                          ;   08 TURN SCRIPT
28F8:     0E 43                                                        ;     while_fail: size=0043
28FA:       0D 04                                                      ;       while_pass: size=0004
28FC:         9C                                                       ;         9C(??MoveHoudiniC)
28FD:         1C 2C                                                    ;         set_VAR(object) object=2C(HoudiniC)
28FF:         9E                                                       ;         9E(PrintObjectEntersRoom)
2900:       0B 3B 05                                                   ;       switch(is_less_equal_last_random(value)): size=003B
2903:         08                                                       ;         is_less_equal_last_random(value) value=08
2904:         1A                                                       ;         IF_NOT_GOTO address=291F
2905:           1F 18                                                  ;           print2(msg) size=0018
2907:             87 74 90 5A 4F 77 64 C5 F5 8B FC ED A3 48 6B 16      ;             HOUDINI MUMBLES, "ANY MINUTE NOW..."
2917:             F6 9A 50 5E 8F A1 DC F9                              ;             ~
291F:         10                                                       ;         is_less_equal_last_random(value) value=10
2920:         1C                                                       ;         IF_NOT_GOTO address=293D
2921:           1F 1A                                                  ;           print2(msg) size=001A
2923:             87 74 90 5A 46 77 DE 5F 2F 49 33 BB FD 1B 5B CA      ;             HOUDINI DECLARES, "I'VE ALMOST GOT IT!"
2933:             47 48 E6 A0 81 15 0B BC AC BB                        ;             ~
293D:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
293F:     AB                                                           ;     AB(AttackPerson)
2940:   0B 01                                                          ;   0B COMMAND HANDLING IF GIVEN COMMAND
2942:     9A                                                           ;     9A(??CommandResponse)
2943:   09 02                                                          ;   HIT POINTS
2945:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
;
; Object_2D "Woman"
2947: 01 81 CA                                                         ; word=01 size=01CA
294A: 8E 00 90                                                         ; room=8E scorePoints=00 bits=90
294D:   03 60                                                          ;   03 DESCRIPTION
294F:     04 5E                                                        ;     print(msg) size=005E
2951:       5F BE 5B B1 4B 7B 58 45 43 62 3B 16 B7 B1 01 18            ;       THERE IS A VERY LARGE WOMAN DRESSED IN A
2961:       90 91 0C 15 65 62 F3 5F 83 7A 57 45 08 99 B7 A0            ;       UNIFORM HERE. SHE LOOKS LIKE THE ROLLER
2971:       9F 15 7F B1 5A 17 4E 5E 3D A0 CE B5 17 7A 82 17            ;       DERBY QUEEN. SHE HAS A JAGGED SCAR JUST
2981:       54 5E C6 9F 23 62 F4 59 7B 50 A7 AD A7 61 5A 17            ;       BELOW HER HAIRLINE.
2991:       4A 5E 4B 49 4C 45 79 47 F3 5F 53 B7 8C AF 66 C6            ;       ~
29A1:       AF 14 89 8D 9F 15 8A AF D4 47 90 8C DB 63                  ;       ~
29AF:   02 06                                                          ;   02 SHORT_NAME
29B1:     5F BE 9F 16 97 B3                                            ;     THE NURSE
29B7:   0B 01                                                          ;   0B COMMAND HANDLING IF GIVEN COMMAND
29B9:     9A                                                           ;     9A(??CommandResponse)
29BA:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
29BC:     AB                                                           ;     AB(AttackPerson)
29BD:   08 81 50                                                       ;   08 TURN SCRIPT
29C0:     0D 81 4D                                                     ;     while_pass: size=014D
29C3:       01 13                                                      ;       is_in_pack_or_current_room(object) object=13(PLAYER)
29C5:       0E 81 48                                                   ;       while_fail: size=0148
29C8:         0D 71                                                    ;         while_pass: size=0071
29CA:           0A 03                                                  ;           compare_input_to(phrase) phrase="03: EAST * * *"
29CC:           1F 6D                                                  ;           print2(msg) size=006D
29CE:             1F B8 8F 17 DD B2 89 17 14 D0 1B 58 1B A1 8E 48      ;             SHE TURNS TOWARD YOU AND SAYS, "OH! YOU
29DE:             53 17 6E DF 79 13 AB 70 C7 DE 77 16 F3 B9 5B 4D      ;             MUST BE HERE FOR TREATMENT. JUST COME RI
29EE:             F4 72 48 5E A3 A0 EF BF 87 49 9E 61 4C F4 66 C6      ;             GHT OVER HERE..." SHE GESTURES TOWARD SO
29FE:             E1 14 1B 92 09 B2 33 75 4F A1 8A AF 2F 62 FF F9      ;             METHING WHICH LOOKS LIKE AN ELECTRIC COU
2A0E:             95 19 DB 72 B5 6C 74 C0 4B 62 89 BF 2E 49 61 17      ;             CH.
2A1E:             36 92 90 73 D9 6A 85 73 0E 71 3D A0 CE B5 17 7A      ;             ~
2A2E:             90 14 2E 15 E6 5F 05 B2 E1 14 DA C3 2E               ;             ~
2A3B:         0D 80 D2                                                 ;         while_pass: size=00D2
2A3E:           1F 73                                                  ;           print2(msg) size=0073
2A40:             91 1E A4 C2 50 5E F3 A0 41 55 F4 A4 83 49 CF 98      ;             "YOU'RE NOT COOPERATING...", SAYS THE NU
2A50:             DC F9 15 EE 55 4A 82 17 50 5E 3D C6 43 5E D5 B5      ;             RSE AS SHE LUNGES ACROSS THE ROOM AND TA
2A60:             DB 72 70 8E B5 6C 85 14 05 B3 D6 B5 DB 72 01 B3      ;             CKLES YOU. SHE DRAGS YOU TO THE COUCH AN
2A70:             43 90 33 98 45 BD BF 86 DB B5 3F A1 5A 17 46 5E      ;             D STRAPS YOU IN. THEN SHE PULLS AN OMINO
2A80:             C9 B0 DB B5 1B A1 6B BF 5F BE E1 14 DA C3 90 14      ;             US LEVER AND
2A90:             15 58 EB BF 0B A7 C7 DE D0 15 56 F4 F0 72 5A 17      ;             ~
2AA0:             52 5E 46 C5 C3 B5 91 96 D0 92 35 A1 3F 16 74 CA      ;             ~
2AB0:             90 14 44                                             ;             ~
2AB3:           0E 24                                                  ;           while_fail: size=0024
2AB5:             03 13 3A                                             ;             is_located(room,object) room=13(Room_13) object=3A(Object3A)
2AB8:             1F 1F                                                ;             print2(msg) size=001F
2ABA:               C7 DE 3A 15 F4 A4 30 79 9B 53 5F BE AE 17 8F BE    ;               YOU EXPERIENCE THE ULTIMATE AGONY! MERCI
2ACA:               7F 49 89 14 23 A0 CF 06 2D 62 5F 79 13 8D 2C       ;               FULLY,
2AD9:           1F 0A                                                  ;           print2(msg) size=000A
2ADB:             C7 DE DB 16 CB B9 36 A1 FF F9                        ;             YOU PASS OUT...
2AE5:           2C 13                                                  ;           set_ACTIVE(object) object=13(PLAYER)
2AE7:           19 88                                                  ;           move_ACTIVE(room) room=88(Small square room)
2AE9:           17 1B 8E                                               ;           move_to(object,room) object=1B(GreenKeyA) room=8E(Electroshock room)
2AEC:           17 41 8C                                               ;           move_to(object,room) object=41(GreenKeyB) room=8C(East end east-west hall)
2AEF:           1C 05                                                  ;           set_VAR(object) object=05(GreenDoorC)
2AF1:           0E 03                                                  ;           while_fail: size=0003
2AF3:             15 02                                                ;             check_VAR(bits) bits=02(......O.)
2AF5:             29                                                   ;             print_open_VAR()
2AF6:           1C 06                                                  ;           set_VAR(object) object=06(GreedDoorD)
2AF8:           0E 04                                                  ;           while_fail: size=0004
2AFA:             14                                                   ;             execute_and_reverse_status:
2AFB:             15 02                                                ;             check_VAR(bits) bits=02(......O.)
2AFD:             29                                                   ;             print_open_VAR()
2AFE:           1F 10                                                  ;           print2(msg) size=0010
2B00:             C7 DE 99 14 17 48 8B 96 9B 96 34 A1 D7 14 17 8D      ;             YOU AWAKEN IN YOUR CELL.
2B10:   09 02                                                          ;   HIT POINTS
2B12:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
;
; Object_2E "Doctor"
2B14: 07 81 AE                                                         ; word=07 size=01AE
2B17: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
2B1A:   03 01                                                          ;   03 DESCRIPTION
2B1C:     9F                                                           ;     9F(PrintUnshavenMan)
2B1D:   02 07                                                          ;   02 SHORT_NAME
2B1F:     5F BE 09 15 09 56 52                                         ;     THE DOCTOR
2B26:   08 81 95                                                       ;   08 TURN SCRIPT
2B29:     0E 81 92                                                     ;     while_fail: size=0192
2B2C:       0D 1C                                                      ;       while_pass: size=001C
2B2E:         14                                                       ;         execute_and_reverse_status:
2B2F:         01 13                                                    ;         is_in_pack_or_current_room(object) object=13(PLAYER)
2B31:         9B                                                       ;         9B(??PrintDirs)
2B32:         1F 15                                                    ;         print2(msg) size=0015
2B34:           C7 DE 9F 15 23 49 50 45 55 9F 43 5E 33 98 C7 DE        ;           YOU HEAR A NOISE AND YOU NOTICE
2B44:           99 16 85 BE 45                                         ;           ~
2B49:         9F                                                       ;         9F(PrintUnshavenMan)
2B4A:       0D 81 71                                                   ;       while_pass: size=0171
2B4D:         01 13                                                    ;         is_in_pack_or_current_room(object) object=13(PLAYER)
2B4F:         1F 0C                                                    ;         print2(msg) size=000C
2B51:           5F BE 09 15 09 56 95 AF 55 4A FB ED                    ;           THE DOCTOR SAYS,
2B5D:         0B 81 5E 05                                              ;         switch(is_less_equal_last_random(value)): size=015E
2B61:           33                                                     ;           is_less_equal_last_random(value) value=33
2B62:           42                                                     ;           IF_NOT_GOTO address=2BA5
2B63:             1F 40                                                ;             print2(msg) size=0040
2B65:               91 1E 43 C2 5B B1 06 9A AF 14 91 7A 7B 14 41 6E    ;               "YOU ARE NOT BEING A GOOD LITTLE PATIENT
2B75:               0E 58 8E 7B DB 8B 56 A4 30 79 AB BB 09 9A 2F 17    ;               ! NOW RETURN TO YOUR CELL, OR YOU WILL N
2B85:               74 C0 96 96 DB 9C 34 A1 D7 14 16 8D C4 16 51 18    ;               EED A LOBOTOMY!"
2B95:               59 C2 46 7A 8F 16 F3 5F 4E 45 39 9E 7F BF EC DA    ;               ~
2BA5:           66                                                     ;           is_less_equal_last_random(value) value=66
2BA6:           20                                                     ;           IF_NOT_GOTO address=2BC7
2BA7:             1F 1E                                                ;             print2(msg) size=001E
2BA9:               FB 1B B9 6E D6 CE 2F 7B 11 58 86 64 8E 5F 91 7A    ;               "I GROW TIRED OF DEALING WITH YOU INFERI
2BB9:               FB 17 53 BE C7 DE D0 15 74 66 C4 7A 6C B5          ;               ORS!"
2BC7:           99                                                     ;           is_less_equal_last_random(value) value=99
2BC8:           22                                                     ;           IF_NOT_GOTO address=2BEB
2BC9:             1F 20                                                ;             print2(msg) size=0020
2BCB:               3A 1E 73 49 2F 49 51 18 46 C2 50 9F CA 6A 2F 62    ;               "WHAT ARE YOU DOING HERE? GO WHERE YOU B
2BDB:               89 00 D9 9C F4 72 5B 5E 1B A1 6E 4D 11 A0 E3 06    ;               ELONG!"
2BEB:           FF                                                     ;           is_less_equal_last_random(value) value=FF
2BEC:           80 D0                                                  ;           IF_NOT_GOTO address=2CBD
2BEE:             0D 80 CD                                             ;             while_pass: size=00CD
2BF1:               1F 80 B4                                           ;               print2(msg) size=00B4
2BF4:                 FD 1B 43 90 6B 68 F3 78 9F 77 81 15 91 7A 89 17  ;                 "I'M AFRAID I'M GOING TO HAVE TO GIVE YO
2C04:                 9B 15 5B CA 6B BF 58 6D 5B 5E 1B A1 48 45 00 B3  ;                 U A FRONTAL LOBOTOMY!" HE STICKS YOU WIT
2C14:                 4E BD 49 16 06 4F FB 9F E3 06 DB 72 03 BA A5 54  ;                 H HIS HYPO AND YOU PASS OUT. WHEN YOU AW
2C24:                 51 18 59 C2 82 7B A3 15 CA B5 E9 DE 90 14 1B 58  ;                 AKEN, YOU FEEL SOMEWHAT INDIFFERENT TO Y
2C34:                 1B A1 55 A4 D1 B5 97 C6 FA 17 83 61 C7 DE 99 14  ;                 OUR SURROUNDINGS. YOU NOTICE BLOOD ON YO
2C44:                 17 48 F3 9B C7 DE 4F 15 33 61 3F B9 FA 62 73 49  ;                 UR GOWN, BUT IT DOESN'T SEEM TO BOTHER Y
2C54:                 8E 7A 50 79 2F 62 B3 9A 6B BF C7 DE 95 AF 3C C6  ;                 OU. YOU FEEL LIKE WANDERING...
2C64:                 30 A1 90 5A EF 6E 51 18 50 C2 03 A1 9B 53 89 4E  ;                 ~
2C74:                 73 9E 03 A0 C7 DE 89 AF 80 A1 04 EE 73 C6 73 7B  ;                 ~
2C84:                 77 5B 05 B9 15 BC 2F 60 89 17 B9 14 5F BE 9B AF  ;                 ~
2C94:                 3F A1 51 18 48 C2 2E 60 43 16 9B 85 10 D0 F4 59  ;                 ~
2CA4:                 91 7A FF F9                                      ;                 ~
2CA8:               1C 05                                              ;               set_VAR(object) object=05(GreenDoorC)
2CAA:               0E 03                                              ;               while_fail: size=0003
2CAC:                 15 02                                            ;                 check_VAR(bits) bits=02(......O.)
2CAE:                 29                                               ;                 print_open_VAR()
2CAF:               1C 06                                              ;               set_VAR(object) object=06(GreedDoorD)
2CB1:               0E 04                                              ;               while_fail: size=0004
2CB3:                 14                                               ;                 execute_and_reverse_status:
2CB4:                 15 02                                            ;                 check_VAR(bits) bits=02(......O.)
2CB6:                 29                                               ;                 print_open_VAR()
2CB7:               2C 13                                              ;               set_ACTIVE(object) object=13(PLAYER)
2CB9:               17 3A 13                                           ;               move_to(object,room) object=3A(Object3A) room=13(Room_13)
2CBC:               19 88                                              ;               move_ACTIVE(room) room=88(Small square room)
2CBE:   0B 01                                                          ;   0B COMMAND HANDLING IF GIVEN COMMAND
2CC0:     9A                                                           ;     9A(??CommandResponse)
2CC1:   09 02                                                          ;   HIT POINTS
2CC3:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
;
; Object_2F "Walls"
2CC5: 25 0C                                                            ; word=25 size=000C
2CC7: FF 00 80                                                         ; room=FF scorePoints=00 bits=80
2CCA:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
2CCC:     A4                                                           ;     A4(PrintPicassoDoor)
2CCD:   02 04                                                          ;   02 SHORT_NAME
2CCF:     0E D0 0B 8E                                                  ;     WALLS
;
; Object_30 "Room"
2CD3: 2A 0B                                                            ; word=2A size=000B
2CD5: FF 00 80                                                         ; room=FF scorePoints=00 bits=80
2CD8:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
2CDA:     A4                                                           ;     A4(PrintPicassoDoor)
2CDB:   02 03                                                          ;   02 SHORT_NAME
2CDD:     01 B3 4D                                                     ;     ROOM
;
; Object_31 "Floor"
2CE0: 2B 09                                                            ; word=2B size=0009
2CE2: FF 00 80                                                         ; room=FF scorePoints=00 bits=80
2CE5:   02 04                                                          ;   02 SHORT_NAME
2CE7:     89 67 A3 A0                                                  ;     FLOOR
;
; Object_32 "Exit"
2CEB: 2C 08                                                            ; word=2C size=0008
2CED: FF 00 80                                                         ; room=FF scorePoints=00 bits=80
2CF0:   02 03                                                          ;   02 SHORT_NAME
2CF2:     23 63 54                                                     ;     EXIT
;
; Object_33 "Corner"
2CF5: 30 0C                                                            ; word=30 size=000C
2CF7: FF 00 80                                                         ; room=FF scorePoints=00 bits=80
2CFA:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
2CFC:     A4                                                           ;     A4(PrintPicassoDoor)
2CFD:   02 04                                                          ;   02 SHORT_NAME
2CFF:     44 55 74 98                                                  ;     CORNER
;
; Object_34 "Hallway"
2D03: 33 0D                                                            ; word=33 size=000D
2D05: FF 00 80                                                         ; room=FF scorePoints=00 bits=80
2D08:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
2D0A:     A4                                                           ;     A4(PrintPicassoDoor)
2D0B:   02 05                                                          ;   02 SHORT_NAME
2D0D:     4E 72 B3 8E 59                                               ;     HALLWAY
;
; Object_35 "Entrance"
2D12: 36 0B                                                            ; word=36 size=000B
2D14: FF 00 80                                                         ; room=FF scorePoints=00 bits=80
2D17:   02 06                                                          ;   02 SHORT_NAME
2D19:     9E 61 D0 B0 9B 53                                            ;     ENTRANCE
;
; Object_36 "Ceiling"
2D1F: 3B 0A                                                            ; word=3B size=000A
2D21: FF 00 80                                                         ; room=FF scorePoints=00 bits=80
2D24:   02 05                                                          ;   02 SHORT_NAME
2D26:     AB 53 90 8C 47                                               ;     CEILING
;
; Object_37 "Hands"
2D2B: 1F 09                                                            ; word=1F size=0009
2D2D: 13 00 C0                                                         ; room=13 scorePoints=00 bits=C0
2D30:   02 04                                                          ;   02 SHORT_NAME
2D32:     50 72 0B 5C                                                  ;     HANDS
;
; Object_38 "SYSTEM"
2D36: 20 03                                                            ; word=20 size=0003
2D38: 00 00 80                                                         ; room=00 scorePoints=00 bits=80
;
; Object_39 "BluePillB"
2D3B: 17 11                                                            ; word=17 size=0011
2D3D: 82 00 A0                                                         ; room=82 scorePoints=00 bits=A0
2D40:   03 01                                                          ;   03 DESCRIPTION
2D42:     9D                                                           ;     9D(PrintBluePill)
2D43:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
2D45:     B0                                                           ;     B0(PrintTastesAweful)
2D46:   02 06                                                          ;   02 SHORT_NAME
2D48:     8F 4E 52 5E 46 7A                                            ;     BLUE PILL
;
; Object_3A "Object3A"
2D4E: 3C 03                                                            ; word=3C size=0003
2D50: 00 00 00                                                         ; room=00 scorePoints=00 bits=00
;
; Object_3B "RedKeyB"
2D53: 16 4B                                                            ; word=16 size=004B
2D55: 82 00 80                                                         ; room=82 scorePoints=00 bits=80
2D58:   02 05                                                          ;   02 SHORT_NAME
2D5A:     66 B1 17 16 59                                               ;     RED KEY
2D5F:   01 01                                                          ;   01 ADJECTIVES
2D61:   13                                                             ;   TODO WORD
2D62:   07 3C                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
2D64:     0E 3A                                                        ;     while_fail: size=003A
2D66:       0D 11                                                      ;       while_pass: size=0011
2D68:         0A 43                                                    ;         compare_input_to(phrase) phrase="43: GET ..C..... WITH ..C....."
2D6A:         09 16                                                    ;         compare_to_second_noun(object) object=16(WindowHook)
2D6C:         03 82 3B                                                 ;         is_located(room,object) room=82(Dispensary) object=3B(RedKeyB)
2D6F:         03 00 14                                                 ;         is_located(room,object) room=00(Room_00) object=14(RedKeyA)
2D72:         17 3B 00                                                 ;         move_to(object,room) object=3B(RedKeyB) room=00(Room_00)
2D75:         17 14 13                                                 ;         move_to(object,room) object=14(RedKeyA) room=13(Room_13)
2D78:         B1                                                       ;         B1(PrintYouGetObjectWithObject)
2D79:       0D 24                                                      ;       while_pass: size=0024
2D7B:         0A 05                                                    ;         compare_input_to(phrase) phrase="05: GET ..C..... * *"
2D7D:         04 20                                                    ;         print(msg) size=0020
2D7F:           C7 DE D3 14 90 96 F3 A0 85 A6 44 B8 FB 8E 63 B1        ;           YOU CAN NOT POSSIBLY REACH INTO THAT TIN
2D8F:           13 54 9E 7A D6 9C 56 72 83 17 7B 9B 7E 74 EB 5D        ;           Y HOLE!
2D9F:       B2                                                         ;       B2(PrintCantGetObjectWithObject)
;
; Object_3C "DeadDog"
2DA0: 08 20                                                            ; word=08 size=0020
2DA2: 00 00 A0                                                         ; room=00 scorePoints=00 bits=A0
2DA5:   02 06                                                          ;   02 SHORT_NAME
2DA7:     E3 59 06 58 EB 9E                                            ;     DEAD DOG
2DAD:   03 13                                                          ;   03 DESCRIPTION
2DAF:     04 11                                                        ;     print(msg) size=0011
2DB1:       5F BE 5B B1 4B 7B 46 45 86 5F 09 15 CA 6A 2F 62            ;       THERE IS A DEAD DOG HERE.
2DC1:       2E                                                         ;       ~
;
; Object_3D "SecretDoor"
2DC2: 0B 42                                                            ; word=0B size=0042
2DC4: 00 00 8A                                                         ; room=00 scorePoints=00 bits=8A
2DC7:   07 30                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
2DC9:     0D 2E                                                        ;     while_pass: size=002E
2DCB:       0A 11                                                      ;       compare_input_to(phrase) phrase="11: OPEN ......O. * *"
2DCD:       04 2A                                                      ;       print(msg) size=002A
2DCF:         5F BE 57 17 AF 55 06 BC 44 A0 D5 15 66 17 DD C3          ;         THE SECRET DOOR IS STUCK. YOU ARE NOT ST
2DDF:         5B F4 1B A1 2F 49 99 16 15 BC F9 BF AB 98 99 61          ;         RONG ENOUGH TO OPEN IT.
2DEF:         7A C4 89 17 C2 16 83 61 97 7B                            ;         ~
2DF9:   02 08                                                          ;   02 SHORT_NAME
2DFB:     A5 B7 76 B1 09 15 A3 A0                                      ;     SECRET DOOR
2E03:   01 01                                                          ;   01 ADJECTIVES
2E05:   3D                                                             ;   TODO WORD
;
; Object_3E "PaintedDoorA"
2E06: 0B 76                                                            ; word=0B size=0076
2E08: 00 00 8A                                                         ; room=00 scorePoints=00 bits=8A
2E0B:   02 08                                                          ;   02 SHORT_NAME
2E0D:     4B A4 BF 9A 06 58 44 A0                                      ;     PAINTED DOOR
2E15:   03 24                                                          ;   03 DESCRIPTION
2E17:     04 22                                                        ;     print(msg) size=0022
2E19:       03 A0 5F BE 99 16 C2 B3 F3 17 F3 8C 4B 7B 0F A0            ;       ON THE NORTH WALL IS ONE OF PICASSO'S PA
2E29:       B8 16 E3 16 15 53 2D B9 D2 B5 D0 47 E6 BD 09 15            ;       INTED DOORS
2E39:       BD A0                                                      ;       ~
2E3B:   07 3E                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
2E3D:     0D 3C                                                        ;     while_pass: size=003C
2E3F:       0E 0A                                                      ;       while_fail: size=000A
2E41:         0A 11                                                    ;         compare_input_to(phrase) phrase="11: OPEN ......O. * *"
2E43:         0A 3A                                                    ;         compare_input_to(phrase) phrase="3A: OPEN ......O. WITH u......."
2E45:         0A 41                                                    ;         compare_input_to(phrase) phrase="41: LOCK ....A... WITH u......."
2E47:         0A 42                                                    ;         compare_input_to(phrase) phrase="42: UNLOCK .......L WITH u......."
2E49:         0A 40                                                    ;         compare_input_to(phrase) phrase="40: CLOSE ....A... * *"
2E4B:       04 2D                                                      ;       print(msg) size=002D
2E4D:         5F BE DB 16 9E 7A F3 5F 81 5B 91 AF F0 A4 D6 B5          ;         THE PAINTED DOOR OPENS TO REVEAL AN ESCA
2E5D:         D4 9C CF 62 33 48 83 48 55 62 DF 48 39 17 7F C6          ;         PE ROUTE! YOU HAVE ESCAPED!
2E6D:         DB 06 1B A1 58 72 47 5E 53 B7 E6 A4 21                   ;         ~
2E7A:       24                                                         ;       endless_loop()
2E7B:   01 01                                                          ;   01 ADJECTIVES
2E7D:   3E                                                             ;   TODO WORD
;
; Object_3F "PaintedDoorB"
2E7E: 0B 3E                                                            ; word=0B size=003E
2E80: 00 00 80                                                         ; room=00 scorePoints=00 bits=80
2E83:   02 08                                                          ;   02 SHORT_NAME
2E85:     4B A4 BF 9A 06 58 44 A0                                      ;     PAINTED DOOR
2E8D:   07 2C                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
2E8F:     0D 2A                                                        ;     while_pass: size=002A
2E91:       0E 0A                                                      ;       while_fail: size=000A
2E93:         0A 11                                                    ;         compare_input_to(phrase) phrase="11: OPEN ......O. * *"
2E95:         0A 3A                                                    ;         compare_input_to(phrase) phrase="3A: OPEN ......O. WITH u......."
2E97:         0A 40                                                    ;         compare_input_to(phrase) phrase="40: CLOSE ....A... * *"
2E99:         0A 41                                                    ;         compare_input_to(phrase) phrase="41: LOCK ....A... WITH u......."
2E9B:         0A 42                                                    ;         compare_input_to(phrase) phrase="42: UNLOCK .......L WITH u......."
2E9D:       04 1C                                                      ;       print(msg) size=001C
2E9F:         2F 49 51 18 45 C2 DC B0 C3 DA 73 7B 4B 7B F5 81          ;         ARE YOU CRAZY? IT IS JUST A PAINTED DOOR
2EAF:         03 BC DB 16 9E 7A F3 5F 81 5B 2B AF                      ;         !
2EBB:   01 01                                                          ;   01 ADJECTIVES
2EBD:   3E                                                             ;   TODO WORD
;
; Object_40 "GreenDoorI"
2EBE: 0B 12                                                            ; word=0B size=0012
2EC0: 99 00 8B                                                         ; room=99 scorePoints=00 bits=8B
2EC3:   03 01                                                          ;   03 DESCRIPTION
2EC5:     86                                                           ;     86(PrintNorthWallGreedDoor)
2EC6:   01 01                                                          ;   01 ADJECTIVES
2EC8:   14                                                             ;   TODO WORD
2EC9:   02 07                                                          ;   02 SHORT_NAME
2ECB:     AF 6E 83 61 81 5B 52                                         ;     GREEN DOOR
;
; Object_41 "GreenKeyB"
2ED2: 16 4B                                                            ; word=16 size=004B
2ED4: 8C 00 80                                                         ; room=8C scorePoints=00 bits=80
2ED7:   02 06                                                          ;   02 SHORT_NAME
2ED9:     AF 6E 83 61 BB 85                                            ;     GREEN KEY
2EDF:   01 01                                                          ;   01 ADJECTIVES
2EE1:   14                                                             ;   TODO WORD
2EE2:   07 3B                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
2EE4:     0E 39                                                        ;     while_fail: size=0039
2EE6:       0D 11                                                      ;       while_pass: size=0011
2EE8:         0A 43                                                    ;         compare_input_to(phrase) phrase="43: GET ..C..... WITH ..C....."
2EEA:         09 16                                                    ;         compare_to_second_noun(object) object=16(WindowHook)
2EEC:         03 8C 41                                                 ;         is_located(room,object) room=8C(East end east-west hall) object=41(GreenKeyB)
2EEF:         03 8E 1B                                                 ;         is_located(room,object) room=8E(Electroshock room) object=1B(GreenKeyA)
2EF2:         17 41 00                                                 ;         move_to(object,room) object=41(GreenKeyB) room=00(Room_00)
2EF5:         17 1B 13                                                 ;         move_to(object,room) object=1B(GreenKeyA) room=13(Room_13)
2EF8:         B1                                                       ;         B1(PrintYouGetObjectWithObject)
2EF9:       0D 23                                                      ;       while_pass: size=0023
2EFB:         0A 05                                                    ;         compare_input_to(phrase) phrase="05: GET ..C..... * *"
2EFD:         04 1F                                                    ;         print(msg) size=001F
2EFF:           C7 DE D3 14 90 96 F3 A0 63 B1 13 54 5F BE 84 15        ;           YOU CAN NOT REACH THE GREEN KEY FROM OUT
2F0F:           30 60 17 16 48 DB FF B2 C7 16 0A BC 2F 62 2E           ;           HERE.
2F1E:       B2                                                         ;       B2(PrintCantGetObjectWithObject)
;
; Object_42 "Object42"
2F1F: 42 03                                                            ; word=42 size=0003
2F21: 18 00 00                                                         ; room=18 scorePoints=00 bits=00
; ENDOF 1B42
```

# General Commands

```code
GeneralCommands:
2F24: 00 84 75                                                         ; size=0475
2F27: 0E 84 72                                                         ; while_fail: size=0472
2F2A:   0D 28                                                          ;   while_pass: size=0028
2F2C:     0E 08                                                        ;     while_fail: size=0008
2F2E:       0A 01                                                      ;       compare_input_to(phrase) phrase="01: NORTH * * *"
2F30:       0A 02                                                      ;       compare_input_to(phrase) phrase="02: SOUTH * * *"
2F32:       0A 03                                                      ;       compare_input_to(phrase) phrase="03: EAST * * *"
2F34:       0A 04                                                      ;       compare_input_to(phrase) phrase="04: WEST * * *"
2F36:     0E 1C                                                        ;     while_fail: size=001C
2F38:       13                                                         ;       process_phrase_by_room_first_second()
2F39:       0D 19                                                      ;       while_pass: size=0019
2F3B:         20 13                                                    ;         is_ACTIVE_this(object) object=13(PLAYER)
2F3D:         04 15                                                    ;         print(msg) size=0015
2F3F:           C7 DE F3 17 CB 8C CF 47 F5 8B D3 B8 D0 15 6B BF        ;           YOU WALK AIMLESSLY INTO A WALL.
2F4F:           59 45 46 48 2E                                         ;           ~
2F54:   0B 84 45 0A                                                    ;   switch(compare_input_to(phrase)): size=0445
2F58:     05                                                           ;     compare_input_to(phrase) phrase="05: GET ..C..... * *"
2F59:     07                                                           ;     IF_NOT_GOTO address=2F61
2F5A:       0E 05                                                      ;       while_fail: size=0005
2F5C:         A2                                                       ;         A2(PrintAlreadyHaveObject)
2F5D:         13                                                       ;         process_phrase_by_room_first_second()
2F5E:         8F                                                       ;         8F(??GetObject)
2F5F:         14                                                       ;         execute_and_reverse_status:
2F60:         0C                                                       ;         fail()
2F61:     43                                                           ;     compare_input_to(phrase) phrase="43: GET ..C..... WITH ..C....."
2F62:     0D                                                           ;     IF_NOT_GOTO address=2F70
2F63:       0E 0B                                                      ;       while_fail: size=000B
2F65:         A2                                                       ;         A2(PrintAlreadyHaveObject)
2F66:         13                                                       ;         process_phrase_by_room_first_second()
2F67:         0D 03                                                    ;         while_pass: size=0003
2F69:           1B                                                     ;           set_VAR_to_second_noun()
2F6A:           14                                                     ;           execute_and_reverse_status:
2F6B:           8F                                                     ;           8F(??GetObject)
2F6C:         0D 02                                                    ;         while_pass: size=0002
2F6E:           1A                                                     ;           set_VAR_to_first_noun()
2F6F:           8F                                                     ;           8F(??GetObject)
2F70:     06                                                           ;     compare_input_to(phrase) phrase="06: DROP ..C..... * *"
2F71:     34                                                           ;     IF_NOT_GOTO address=2FA6
2F72:       0E 32                                                      ;       while_fail: size=0032
2F74:         0D 0E                                                    ;         while_pass: size=000E
2F76:           1A                                                     ;           set_VAR_to_first_noun()
2F77:           18                                                     ;           is_VAR_owned_by_ACTIVE()
2F78:           14                                                     ;           execute_and_reverse_status:
2F79:           08 37                                                  ;           is_first_noun(object) object=37(Hands)
2F7B:           10                                                     ;           drop_VAR()
2F7C:           04 06                                                  ;           print(msg) size=0006
2F7E:             F9 5B 9F A6 9B 5D                                    ;             DROPPED.
2F84:         0D 11                                                    ;         while_pass: size=0011
2F86:           14                                                     ;           execute_and_reverse_status:
2F87:           08 37                                                  ;           is_first_noun(object) object=37(Hands)
2F89:           04 0C                                                  ;           print(msg) size=000C
2F8B:             C7 DE 09 15 E6 96 9B 15 5B CA 71 7B                  ;             YOU DON'T HAVE IT!
2F97:         04 0D                                                    ;         print(msg) size=000D
2F99:           C7 DE 57 17 5B 61 95 5A 35 6F E6 BD 2E                 ;           YOU SEEM DISGUSTED.
2FA6:     11                                                           ;     compare_input_to(phrase) phrase="11: OPEN ......O. * *"
2FA7:     15                                                           ;     IF_NOT_GOTO address=2FBD
2FA8:       0E 13                                                      ;       while_fail: size=0013
2FAA:         13                                                       ;         process_phrase_by_room_first_second()
2FAB:         92                                                       ;         92(??YouCantDoThatTo)
2FAC:         0D 0D                                                    ;         while_pass: size=000D
2FAE:           1A                                                     ;           set_VAR_to_first_noun()
2FAF:           15 01                                                  ;           check_VAR(bits) bits=01(.......L)
2FB1:           A8                                                     ;           A8(PrintTheFirstNoun)
2FB2:           04 07                                                  ;           print(msg) size=0007
2FB4:             4B 7B 75 8D A6 85 2E                                 ;             IS LOCKED.
2FBB:         A5                                                       ;         A5(AttemptClose)
2FBC:         A6                                                       ;         A6(AttemptOpen)
2FBD:     3A                                                           ;     compare_input_to(phrase) phrase="3A: OPEN ......O. WITH u......."
2FBE:     12                                                           ;     IF_NOT_GOTO address=2FD1
2FBF:       0E 10                                                      ;       while_fail: size=0010
2FC1:         0D 03                                                    ;         while_pass: size=0003
2FC3:           1B                                                     ;           set_VAR_to_second_noun()
2FC4:           14                                                     ;           execute_and_reverse_status:
2FC5:           8F                                                     ;           8F(??GetObject)
2FC6:         13                                                       ;         process_phrase_by_room_first_second()
2FC7:         92                                                       ;         92(??YouCantDoThatTo)
2FC8:         A5                                                       ;         A5(AttemptClose)
2FC9:         A7                                                       ;         A7(AttemptUnlock)
2FCA:         0D 04                                                    ;         while_pass: size=0004
2FCC:           15 01                                                  ;           check_VAR(bits) bits=01(.......L)
2FCE:           2A                                                     ;           toggle_lock_VAR()
2FCF:           0C                                                     ;           fail()
2FD0:         A6                                                       ;         A6(AttemptOpen)
2FD1:     40                                                           ;     compare_input_to(phrase) phrase="40: CLOSE ....A... * *"
2FD2:     24                                                           ;     IF_NOT_GOTO address=2FF7
2FD3:       0E 22                                                      ;       while_fail: size=0022
2FD5:         13                                                       ;         process_phrase_by_room_first_second()
2FD6:         92                                                       ;         92(??YouCantDoThatTo)
2FD7:         0D 0E                                                    ;         while_pass: size=000E
2FD9:           1A                                                     ;           set_VAR_to_first_noun()
2FDA:           15 02                                                  ;           check_VAR(bits) bits=02(......O.)
2FDC:           A8                                                     ;           A8(PrintTheFirstNoun)
2FDD:           04 08                                                  ;           print(msg) size=0008
2FDF:             4B 7B 06 9A C2 16 A7 61                              ;             IS NOT OPEN.
2FE7:         0D 0E                                                    ;         while_pass: size=000E
2FE9:           29                                                     ;           print_open_VAR()
2FEA:           A8                                                     ;           A8(PrintTheFirstNoun)
2FEB:           04 0A                                                  ;           print(msg) size=000A
2FED:             4B 7B 09 9A DE 14 D7 A0 9B 5D                        ;             IS NOW CLOSED.
2FF7:     42                                                           ;     compare_input_to(phrase) phrase="42: UNLOCK .......L WITH u......."
2FF8:     2F                                                           ;     IF_NOT_GOTO address=3028
2FF9:       0E 2D                                                      ;       while_fail: size=002D
2FFB:         0D 03                                                    ;         while_pass: size=0003
2FFD:           1B                                                     ;           set_VAR_to_second_noun()
2FFE:           14                                                     ;           execute_and_reverse_status:
2FFF:           8F                                                     ;           8F(??GetObject)
3000:         13                                                       ;         process_phrase_by_room_first_second()
3001:         92                                                       ;         92(??YouCantDoThatTo)
3002:         0D 11                                                    ;         while_pass: size=0011
3004:           1A                                                     ;           set_VAR_to_first_noun()
3005:           14                                                     ;           execute_and_reverse_status:
3006:           15 01                                                  ;           check_VAR(bits) bits=01(.......L)
3008:           A8                                                     ;           A8(PrintTheFirstNoun)
3009:           04 0A                                                  ;           print(msg) size=000A
300B:             4B 7B 06 9A 49 16 97 54 9B 5D                        ;             IS NOT LOCKED.
3015:         A5                                                       ;         A5(AttemptClose)
3016:         A7                                                       ;         A7(AttemptUnlock)
3017:         0D 0F                                                    ;         while_pass: size=000F
3019:           2A                                                     ;           toggle_lock_VAR()
301A:           A8                                                     ;           A8(PrintTheFirstNoun)
301B:           04 0B                                                  ;           print(msg) size=000B
301D:             4B 7B 09 9A B0 17 75 8D A6 85 2E                     ;             IS NOW UNLOCKED.
3028:     41                                                           ;     compare_input_to(phrase) phrase="41: LOCK ....A... WITH u......."
3029:     46                                                           ;     IF_NOT_GOTO address=3070
302A:       0E 44                                                      ;       while_fail: size=0044
302C:         0D 03                                                    ;         while_pass: size=0003
302E:           1B                                                     ;           set_VAR_to_second_noun()
302F:           14                                                     ;           execute_and_reverse_status:
3030:           8F                                                     ;           8F(??GetObject)
3031:         13                                                       ;         process_phrase_by_room_first_second()
3032:         92                                                       ;         92(??YouCantDoThatTo)
3033:         A5                                                       ;         A5(AttemptClose)
3034:         0D 17                                                    ;         while_pass: size=0017
3036:           14                                                     ;           execute_and_reverse_status:
3037:           09 14                                                  ;           compare_to_second_noun(object) object=14(RedKeyA)
3039:           04 0A                                                  ;           print(msg) size=000A
303B:             C7 DE D3 14 E6 96 49 16 8B 54                        ;             YOU CAN'T LOCK
3045:           A8                                                     ;           A8(PrintTheFirstNoun)
3046:           04 03                                                  ;           print(msg) size=0003
3048:             56 D1 48                                             ;             WITH
304B:           A9                                                     ;           A9(PrintTheSecondNoun)
304C:           8B                                                     ;           8B(PrintPeriod)
304D:         0D 11                                                    ;         while_pass: size=0011
304F:           1A                                                     ;           set_VAR_to_first_noun()
3050:           15 01                                                  ;           check_VAR(bits) bits=01(.......L)
3052:           A8                                                     ;           A8(PrintTheFirstNoun)
3053:           04 0B                                                  ;           print(msg) size=000B
3055:             4B 7B 06 9A B0 17 75 8D A6 85 2E                     ;             IS NOT UNLOCKED.
3060:         0D 0E                                                    ;         while_pass: size=000E
3062:           2A                                                     ;           toggle_lock_VAR()
3063:           A8                                                     ;           A8(PrintTheFirstNoun)
3064:           04 0A                                                  ;           print(msg) size=000A
3066:             4B 7B 09 9A 49 16 97 54 9B 5D                        ;             IS NOW LOCKED.
3070:     12                                                           ;     compare_input_to(phrase) phrase="12: PULL u....... * *"
3071:     21                                                           ;     IF_NOT_GOTO address=3093
3072:       0E 1F                                                      ;       while_fail: size=001F
3074:         13                                                       ;         process_phrase_by_room_first_second()
3075:         0D 1C                                                    ;         while_pass: size=001C
3077:           04 13                                                  ;           print(msg) size=0013
3079:             33 D1 09 15 E6 96 51 18 4E C2 98 5F 56 5E DB 72      ;             WHY DON'T YOU LEAVE THE POOR
3089:             81 A6 52                                             ;             ~
308C:           11                                                     ;           print_first_noun()
308D:           04 04                                                  ;           print(msg) size=0004
308F:             49 48 7F 98                                          ;             ALONE.
3093:     09                                                           ;     compare_input_to(phrase) phrase="09: ATTACK ...P.... WITH .v......"
3094:     80 A1                                                        ;     IF_NOT_GOTO address=3136
3096:       0E 80 9E                                                   ;       while_fail: size=009E
3099:         14                                                       ;         execute_and_reverse_status:
309A:         1B                                                       ;         set_VAR_to_second_noun()
309B:         14                                                       ;         execute_and_reverse_status:
309C:         0E 05                                                    ;         while_fail: size=0005
309E:           09 37                                                  ;           compare_to_second_noun(object) object=37(Hands)
30A0:           09 00                                                  ;           compare_to_second_noun(object) object=00(nowhere)
30A2:           8F                                                     ;           8F(??GetObject)
30A3:         0E 80 84                                                 ;         while_fail: size=0084
30A6:           0D 1A                                                  ;           while_pass: size=001A
30A8:             14                                                   ;             execute_and_reverse_status:
30A9:             15 40                                                ;             check_VAR(bits) bits=40(.v......)
30AB:             14                                                   ;             execute_and_reverse_status:
30AC:             09 00                                                ;             compare_to_second_noun(object) object=00(nowhere)
30AE:             04 0A                                                ;             print(msg) size=000A
30B0:               C7 DE D3 14 E6 96 AF 15 B3 B3                      ;               YOU CAN'T HURT
30BA:             A8                                                   ;             A8(PrintTheFirstNoun)
30BB:             04 03                                                ;             print(msg) size=0003
30BD:               56 D1 48                                           ;               WITH
30C0:             A9                                                   ;             A9(PrintTheSecondNoun)
30C1:             8B                                                   ;             8B(PrintPeriod)
30C2:           13                                                     ;           process_phrase_by_room_first_second()
30C3:           0D 1C                                                  ;           while_pass: size=001C
30C5:             1A                                                   ;             set_VAR_to_first_noun()
30C6:             14                                                   ;             execute_and_reverse_status:
30C7:             15 10                                                ;             check_VAR(bits) bits=10(...P....)
30C9:             04 14                                                ;             print(msg) size=0014
30CB:               73 7B 77 5B D0 B5 C9 9C 36 A0 89 17 96 14 45 BD    ;               IT DOES NO GOOD TO ATTACK THE
30DB:               D6 83 DB 72                                        ;               ~
30DF:             11                                                   ;             print_first_noun()
30E0:             8B                                                   ;             8B(PrintPeriod)
30E1:           0D 47                                                  ;           while_pass: size=0047
30E3:             1A                                                   ;             set_VAR_to_first_noun()
30E4:             0E 04                                                ;             while_fail: size=0004
30E6:               09 37                                              ;               compare_to_second_noun(object) object=37(Hands)
30E8:               09 00                                              ;               compare_to_second_noun(object) object=00(nowhere)
30EA:             0B 3E 05                                             ;             switch(is_less_equal_last_random(value)): size=003E
30ED:               55                                                 ;               is_less_equal_last_random(value) value=55
30EE:               13                                                 ;               IF_NOT_GOTO address=3102
30EF:                 0D 11                                            ;                 while_pass: size=0011
30F1:                   04 0D                                          ;                   print(msg) size=000D
30F3:                     44 45 89 8D 89 17 82 17 44 5E 93 9E 21       ;                     A BLOW TO THE BODY!
3100:                   1D 04                                          ;                   attack_VAR(points) points=04
3102:               AF                                                 ;               is_less_equal_last_random(value) value=AF
3103:               14                                                 ;               IF_NOT_GOTO address=3118
3104:                 04 12                                            ;                 print(msg) size=0012
3106:                   59 45 3E 7A EF 16 1A 98 90 14 1B 58 1B A1 D5 92;                   A WILD PUNCH AND YOU MISS.
3116:                   5B BB                                          ;                   ~
3118:               FF                                                 ;               is_less_equal_last_random(value) value=FF
3119:               10                                                 ;               IF_NOT_GOTO address=312A
311A:                 0D 0E                                            ;                 while_pass: size=000E
311C:                   04 0A                                          ;                   print(msg) size=000A
311E:                     C7 DE AF 14 8F 48 0A 58 59 7A                ;                     YOU BEANED HIM!
3128:                   1D 03                                          ;                   attack_VAR(points) points=03
312A:         0D 0B                                                    ;         while_pass: size=000B
312C:           A8                                                     ;           A8(PrintTheFirstNoun)
312D:           04 08                                                  ;           print(msg) size=0008
312F:             4B 7B 92 C5 37 49 17 60                              ;             IS UNHARMED.
3137:     0A                                                           ;     compare_input_to(phrase) phrase="0A: LOOK * * *"
3138:     01                                                           ;     IF_NOT_GOTO address=313A
3139:       07                                                         ;       print_room_description()
313A:     15                                                           ;     compare_input_to(phrase) phrase="15: EAT u....... * *"
313B:     26                                                           ;     IF_NOT_GOTO address=3162
313C:       0E 24                                                      ;       while_fail: size=0024
313E:         13                                                       ;         process_phrase_by_room_first_second()
313F:         0D 21                                                    ;         while_pass: size=0021
3141:           04 0A                                                  ;           print(msg) size=000A
3143:             80 5B F3 23 5B 4D 4E B8 F9 8E                        ;             DON'T BE SILLY!
314D:           A8                                                     ;           A8(PrintTheFirstNoun)
314E:           04 12                                                  ;           print(msg) size=0012
3150:             47 D2 C8 8B F3 23 55 BD DB BD 41 6E 03 58 99 9B      ;             WOULDN'T TASTE GOOD ANYWAY.
3160:             5F 4A                                                ;             ~
3162:     17                                                           ;     compare_input_to(phrase) phrase="17: CLIMB u....... * *"
3163:     4C                                                           ;     IF_NOT_GOTO address=31B0
3164:       0E 4A                                                      ;       while_fail: size=004A
3166:         13                                                       ;         process_phrase_by_room_first_second()
3167:         0D 22                                                    ;         while_pass: size=0022
3169:           1A                                                     ;           set_VAR_to_first_noun()
316A:           15 10                                                  ;           check_VAR(bits) bits=10(...P....)
316C:           04 09                                                  ;           print(msg) size=0009
316E:             46 77 05 A0 16 BC 90 73 4B                           ;             I DON'T THINK
3177:           A8                                                     ;           A8(PrintTheFirstNoun)
3178:           04 11                                                  ;           print(msg) size=0011
317A:             4E D1 15 8A 50 BD 15 58 8E BE 08 8A BE A0 56 72      ;             WILL STAND STILL FORTHAT.
318A:             2E                                                   ;             ~
318B:         0D 23                                                    ;         while_pass: size=0023
318D:           04 10                                                  ;           print(msg) size=0010
318F:             CF 62 8B 96 9B 64 1B A1 47 55 B3 8B C3 54 A3 91      ;             EVEN IF YOU COULD CLIMB
319F:           A8                                                     ;           A8(PrintTheFirstNoun)
31A0:           04 0E                                                  ;           print(msg) size=000E
31A2:             73 7B 47 D2 C8 8B F3 23 EE 72 1B A3 3F A1            ;             IT WOULDN'T HELP YOU.
31B0:     0B                                                           ;     compare_input_to(phrase) phrase="0B: LOOK * AT u......."
31B1:     36                                                           ;     IF_NOT_GOTO address=31E8
31B2:       0E 34                                                      ;       while_fail: size=0034
31B4:         13                                                       ;         process_phrase_by_room_first_second()
31B5:         0D 17                                                    ;         while_pass: size=0017
31B7:           1A                                                     ;           set_VAR_to_first_noun()
31B8:           15 04                                                  ;           check_VAR(bits) bits=04(.....X..)
31BA:           04 10                                                  ;           print(msg) size=0010
31BC:             3F B9 82 62 91 7A D5 15 04 18 8E 7B 83 61 03 A0      ;             SOMETHING IS WRITTEN ON
31CC:           AA                                                     ;           AA(PrintTheVarName)
31CD:           8B                                                     ;           8B(PrintPeriod)
31CE:         0D 18                                                    ;         while_pass: size=0018
31D0:           04 14                                                  ;           print(msg) size=0014
31D2:             5F BE 5D B1 D0 B5 02 A1 91 7A 62 17 DB 5F 33 48      ;             THERE'S NOTHING SPECIAL ABOUT
31E2:             B9 46 73 C6                                          ;             ~
31E6:           A8                                                     ;           A8(PrintTheFirstNoun)
31E7:           8B                                                     ;           8B(PrintPeriod)
31E8:     10                                                           ;     compare_input_to(phrase) phrase="10: LOOK * IN u......."
31E9:     15                                                           ;     IF_NOT_GOTO address=31FF
31EA:       0E 13                                                      ;       while_fail: size=0013
31EC:         13                                                       ;         process_phrase_by_room_first_second()
31ED:         0D 10                                                    ;         while_pass: size=0010
31EF:           04 0C                                                  ;           print(msg) size=000C
31F1:             5F BE 5D B1 D0 B5 02 A1 91 7A D0 15                  ;             THERE'S NOTHING IN
31FD:           A8                                                     ;           A8(PrintTheFirstNoun)
31FE:           8B                                                     ;           8B(PrintPeriod)
31FF:     21                                                           ;     compare_input_to(phrase) phrase="21: PLUGH * * *"
3200:     1A                                                           ;     IF_NOT_GOTO address=321B
3201:       0E 18                                                      ;       while_fail: size=0018
3203:         0D 05                                                    ;         while_pass: size=0005
3205:           03 00 3A                                               ;           is_located(room,object) room=00(Room_00) object=3A(Object3A)
3208:           00 8E                                                  ;           move_ACTIVE_and_look(room) room=8E(Electroshock room)
320A:         0D 0F                                                    ;         while_pass: size=000F
320C:           04 0A                                                  ;           print(msg) size=000A
320E:             C7 DE 81 15 04 BC 8E 62 47 62                        ;             YOU GOT BETTER.
3218:           17 3A 00                                               ;           move_to(object,room) object=3A(Object3A) room=00(Room_00)
321B:     22                                                           ;     compare_input_to(phrase) phrase="22: SCREAM * * *"
321C:     12                                                           ;     IF_NOT_GOTO address=322F
321D:       04 10                                                      ;       print(msg) size=0010
321F:         5B E0 27 60 31 60 41 A0 49 A0 89 D3 89 D3 69 CE          ;         YYYEEEEEOOOOOOWWWWWWWW!!
322F:     23                                                           ;     compare_input_to(phrase) phrase="23: QUIT * * *"
3230:     01                                                           ;     IF_NOT_GOTO address=3232
3231:       24                                                         ;       endless_loop()
3232:     25                                                           ;     compare_input_to(phrase) phrase="25: GO * * *"
3233:     01                                                           ;     IF_NOT_GOTO address=3235
3234:       91                                                         ;       91(PrintUseDirections)
3235:     26                                                           ;     compare_input_to(phrase) phrase="26: GO * AROUND u......."
3236:     01                                                           ;     IF_NOT_GOTO address=3238
3237:       91                                                         ;       91(PrintUseDirections)
3238:     3D                                                           ;     compare_input_to(phrase) phrase="3D: GO * TO u......."
3239:     01                                                           ;     IF_NOT_GOTO address=323B
323A:       91                                                         ;       91(PrintUseDirections)
323B:     27                                                           ;     compare_input_to(phrase) phrase="27: KICK u....... * *"
323C:     0E                                                           ;     IF_NOT_GOTO address=324B
323D:       0E 0C                                                      ;       while_fail: size=000C
323F:         13                                                       ;         process_phrase_by_room_first_second()
3240:         04 09                                                    ;         print(msg) size=0009
3242:           25 A1 AB 70 3B 95 77 BF 21                             ;           OUCH! MY TOE!
324B:     44                                                           ;     compare_input_to(phrase) phrase="44: HELLO * * *"
324C:     09                                                           ;     IF_NOT_GOTO address=3256
324D:       04 07                                                      ;       print(msg) size=0007
324F:         AF 6E 83 62 C5 98 21                                     ;         GREETINGS!
3256:     45                                                           ;     compare_input_to(phrase) phrase="45: HELLO ...P.... * *"
3257:     31                                                           ;     IF_NOT_GOTO address=3289
3258:       0E 2F                                                      ;       while_fail: size=002F
325A:         13                                                       ;         process_phrase_by_room_first_second()
325B:         0D 12                                                    ;         while_pass: size=0012
325D:           1A                                                     ;           set_VAR_to_first_noun()
325E:           15 10                                                  ;           check_VAR(bits) bits=10(...P....)
3260:           A8                                                     ;           A8(PrintTheFirstNoun)
3261:           04 0C                                                  ;           print(msg) size=000C
3263:             72 B1 87 8C 33 BB DF 1B 09 8D 63 F4                  ;             REPLIES, "HELLO."
326F:         0D 18                                                    ;         while_pass: size=0018
3271:           04 14                                                  ;           print(msg) size=0014
3273:             16 A0 43 DB E4 14 83 4A 01 18 3E C5 7B 17 CB 8C      ;             ONLY A CRAZY WOULD TALK TO THE
3283:             6B BF 5F BE                                          ;             ~
3287:           11                                                     ;           print_first_noun()
3288:           8B                                                     ;           8B(PrintPeriod)
3289:     46                                                           ;     compare_input_to(phrase) phrase="46: WHAT * * *"
328A:     08                                                           ;     IF_NOT_GOTO address=3293
328B:       04 06                                                      ;       print(msg) size=0006
328D:         46 77 98 C5 5B A2                                        ;         I DUNNO.
3293:     47                                                           ;     compare_input_to(phrase) phrase="47: WHAT u....... * *"
3294:     09                                                           ;     IF_NOT_GOTO address=329E
3295:       04 07                                                      ;       print(msg) size=0007
3297:         29 D1 20 16 85 A1 3F                                     ;         WHO KNOWS?
329E:     4A                                                           ;     compare_input_to(phrase) phrase="4A: COME * * *"
329F:     18                                                           ;     IF_NOT_GOTO address=32B8
32A0:       0E 16                                                      ;       while_fail: size=0016
32A2:         13                                                       ;         process_phrase_by_room_first_second()
32A3:         0D 13                                                    ;         while_pass: size=0013
32A5:           04 11                                                  ;           print(msg) size=0011
32A7:             9E 77 08 8A C6 9F 6B A1 C7 DE 90 14 FA DF 2F 62      ;             I'LL FOLLOW YOU ANYWHERE!
32B7:             21                                                   ;             ~
32B8:     49                                                           ;     compare_input_to(phrase) phrase="49: MEET u....... * *"
32B9:     26                                                           ;     IF_NOT_GOTO address=32E0
32BA:       0E 24                                                      ;       while_fail: size=0024
32BC:         13                                                       ;         process_phrase_by_room_first_second()
32BD:         0D 11                                                    ;         while_pass: size=0011
32BF:           09 00                                                  ;           compare_to_second_noun(object) object=00(nowhere)
32C1:           A8                                                     ;           A8(PrintTheFirstNoun)
32C2:           04 0C                                                  ;           print(msg) size=000C
32C4:             09 4F CB B5 89 96 67 B1 90 BE 5B 70                  ;             BOWS IN GREETING.
32D0:         04 0E                                                    ;         print(msg) size=000E
32D2:           5F BE 44 DB 6B A1 83 7A AF 6E 83 62 CF 98              ;           THEY BOW IN GREETING.
32E0:     28                                                           ;     compare_input_to(phrase) phrase="28: FEED ...P.... WITH u......."
32E1:     0A                                                           ;     IF_NOT_GOTO address=32EC
32E2:       0E 08                                                      ;       while_fail: size=0008
32E4:         13                                                       ;         process_phrase_by_room_first_second()
32E5:         0D 04                                                    ;         while_pass: size=0004
32E7:           1A                                                     ;           set_VAR_to_first_noun()
32E8:           15 10                                                  ;           check_VAR(bits) bits=10(...P....)
32EA:           AD                                                     ;           AD(PrintTheVarNotHungry)
32EB:         AE                                                       ;         AE(PrintFindMouthGame)
32EC:     29                                                           ;     compare_input_to(phrase) phrase="29: FEED u....... TO ...P...."
32ED:     0A                                                           ;     IF_NOT_GOTO address=32F8
32EE:       0E 08                                                      ;       while_fail: size=0008
32F0:         13                                                       ;         process_phrase_by_room_first_second()
32F1:         0D 04                                                    ;         while_pass: size=0004
32F3:           1B                                                     ;           set_VAR_to_second_noun()
32F4:           15 10                                                  ;           check_VAR(bits) bits=10(...P....)
32F6:           AD                                                     ;           AD(PrintTheVarNotHungry)
32F7:         AE                                                       ;         AE(PrintFindMouthGame)
32F8:     2F                                                           ;     compare_input_to(phrase) phrase="2F: WAIT * * *"
32F9:     07                                                           ;     IF_NOT_GOTO address=3301
32FA:       04 05                                                      ;       print(msg) size=0005
32FC:         9B 29 57 C6 3E                                           ;         <PAUSE>
3301:     2D                                                           ;     compare_input_to(phrase) phrase="2D: PULL * UP u......."
3302:     09                                                           ;     IF_NOT_GOTO address=330C
3303:       0E 07                                                      ;       while_fail: size=0007
3305:         13                                                       ;         process_phrase_by_room_first_second()
3306:         0D 02                                                    ;         while_pass: size=0002
3308:           1A                                                     ;           set_VAR_to_first_noun()
3309:           8F                                                     ;           8F(??GetObject)
330A:         14                                                       ;         execute_and_reverse_status:
330B:         0C                                                       ;         fail()
330C:     48                                                           ;     compare_input_to(phrase) phrase="48: LOWER u....... * *"
330D:     11                                                           ;     IF_NOT_GOTO address=331F
330E:       0E 0F                                                      ;       while_fail: size=000F
3310:         13                                                       ;         process_phrase_by_room_first_second()
3311:         04 0C                                                    ;         print(msg) size=000C
3313:           C7 DE D3 14 E6 96 09 15 82 17 97 49                    ;           YOU CAN'T DO THAT.
331F:     33                                                           ;     compare_input_to(phrase) phrase=??? Phrase 33 not found
3320:     01                                                           ;     IF_NOT_GOTO address=3322
3321:       AF                                                         ;       AF(PrintLeapsBounds)
3322:     34                                                           ;     compare_input_to(phrase) phrase="34: JUMP * OVER u......."
3323:     01                                                           ;     IF_NOT_GOTO address=3325
3324:       AF                                                         ;       AF(PrintLeapsBounds)
3325:     0D                                                           ;     compare_input_to(phrase) phrase="0D: THROW .v...... AT ...P...."
3326:     2B                                                           ;     IF_NOT_GOTO address=3352
3327:       0E 29                                                      ;       while_fail: size=0029
3329:         0D 25                                                    ;         while_pass: size=0025
332B:           1A                                                     ;           set_VAR_to_first_noun()
332C:           8F                                                     ;           8F(??GetObject)
332D:           0E 21                                                  ;           while_fail: size=0021
332F:             0D 1E                                                ;             while_pass: size=001E
3331:               0E 07                                              ;               while_fail: size=0007
3333:                 14                                               ;                 execute_and_reverse_status:
3334:                 15 10                                            ;                 check_VAR(bits) bits=10(...P....)
3336:                 1B                                               ;                 set_VAR_to_second_noun()
3337:                 14                                               ;                 execute_and_reverse_status:
3338:                 15 40                                            ;                 check_VAR(bits) bits=40(.v......)
333A:               A8                                                 ;               A8(PrintTheFirstNoun)
333B:               04 0F                                              ;               print(msg) size=000F
333D:                 07 4F 17 98 CA B5 37 49 F5 8B D3 B8 B8 16 46     ;                 BOUNCES HARMLESSLY OFF
334C:               A9                                                 ;               A9(PrintTheSecondNoun)
334D:               8B                                                 ;               8B(PrintPeriod)
334E:               10                                                 ;               drop_VAR()
334F:             13                                                   ;             process_phrase_by_room_first_second()
3350:         14                                                       ;         execute_and_reverse_status:
3351:         0C                                                       ;         fail()
3352:     0E                                                           ;     compare_input_to(phrase) phrase="0E: THROW u....... TO ...P...."
3353:     13                                                           ;     IF_NOT_GOTO address=3367
3354:       0E 11                                                      ;       while_fail: size=0011
3356:         13                                                       ;         process_phrase_by_room_first_second()
3357:         0D 0E                                                    ;         while_pass: size=000E
3359:           A9                                                     ;           A9(PrintTheSecondNoun)
335A:           04 0B                                                  ;           print(msg) size=000B
335C:             77 5B 05 B9 19 BC 9E 48 D6 15 2E                     ;             DOESN'T WANT IT.
3367:     0F                                                           ;     compare_input_to(phrase) phrase="0F: DROP u....... IN u......."
3368:     17                                                           ;     IF_NOT_GOTO address=3380
3369:       0E 15                                                      ;       while_fail: size=0015
336B:         0D 03                                                    ;         while_pass: size=0003
336D:           1A                                                     ;           set_VAR_to_first_noun()
336E:           14                                                     ;           execute_and_reverse_status:
336F:           8F                                                     ;           8F(??GetObject)
3370:         13                                                       ;         process_phrase_by_room_first_second()
3371:         0D 0D                                                    ;         while_pass: size=000D
3373:           A8                                                     ;           A8(PrintTheFirstNoun)
3374:           04 08                                                  ;           print(msg) size=0008
3376:             40 D2 F3 23 16 67 D0 15                              ;             WON'T FIT IN
337E:           A9                                                     ;           A9(PrintTheSecondNoun)
337F:           8B                                                     ;           8B(PrintPeriod)
3380:     07                                                           ;     compare_input_to(phrase) phrase="07: INVENT * * *"
3381:     1A                                                           ;     IF_NOT_GOTO address=339C
3382:       0D 18                                                      ;       while_pass: size=0018
3384:         04 15                                                    ;         print(msg) size=0015
3386:           C7 DE 94 14 45 5E 3C 49 D0 DD D6 6A DB 72 FE 67        ;           YOU ARE CARRYING THE FOLLOWING:
3396:           89 8D 91 7A 3A                                         ;           ~
339B:         06                                                       ;         print_inventory()
; ENDOF 2F24
```

# Helper Commands

```code
HelperCommands:
; List of helper commands. Each is tagged with an ID. In the first case, "81" is a command to
; print "ANOTHER SMALL PADDED ROOM."
339C: 00 88 36                                                         ; size=0836
;
; PrintAnotherPaddedRoom
339F: 81 14                                                            ; Function=81(PrintAnotherPaddedRoom) size=0014
33A1: 04 12                                                            ; print(msg) size=0012
33A3:   99 48 5F BE 95 AF 8E 91 12 8A FE 46 F3 5F 01 B3                ;   ANOTHER SMALL PADDED ROOM.
33B3:   DB 95                                                          ;   ~
;
; PrintEastWestHall
33B5: 82 11                                                            ; Function=82(PrintEastWestHall) size=0011
33B7: 04 0F                                                            ; print(msg) size=000F
33B9:   5F BE 23 15 15 BA B5 D0 0A BC 46 48 1B D0 2E                   ;   THE EAST-WEST HALLWAY.
;
; PrintNorthSouthHall
33C8: 83 12                                                            ; Function=83(PrintNorthSouthHall) size=0012
33CA: 04 10                                                            ; print(msg) size=0010
33CC:   5F BE 99 16 C2 B3 E1 EB 82 C6 9B 15 11 8D 5F 4A                ;   THE NORTH-SOUTH HALLWAY.
;
; PrintSouthWallGreenDoor
33DC: 84 1C                                                            ; Function=84(PrintSouthWallGreenDoor) size=001C
33DE: 04 1A                                                            ; print(msg) size=001A
33E0:   03 A0 5F BE 61 17 82 C6 F3 17 F3 8C 5F BE 5B B1                ;   ON THE SOUTH WALL THERE IS A GREEN DOOR
33F0:   4B 7B 49 45 67 B1 86 96 44 A0                                  ;   ~
;
; PrintNorthWallRedDoor
33FA: 85 1B                                                            ; Function=85(PrintNorthWallRedDoor) size=001B
33FC: 04 19                                                            ; print(msg) size=0019
33FE:   03 A0 5F BE 99 16 C2 B3 F3 17 F3 8C 5F BE 5B B1                ;   ON THE NORTH WALL THERE IS A RED DOOR
340E:   4B 7B 54 45 F3 5F 81 5B 52                                     ;   ~
;
; PrintNorthWallGreedDoor
3417: 86 1C                                                            ; Function=86(PrintNorthWallGreedDoor) size=001C
3419: 04 1A                                                            ; print(msg) size=001A
341B:   03 A0 5F BE 99 16 C2 B3 F3 17 F3 8C 5F BE 5B B1                ;   ON THE NORTH WALL THERE IS A GREEN DOOR
342B:   4B 7B 49 45 67 B1 86 96 44 A0                                  ;   ~
;
; PrintSouthWallRedDOor
3435: 87 1B                                                            ; Function=87(PrintSouthWallRedDOor) size=001B
3437: 04 19                                                            ; print(msg) size=0019
3439:   03 A0 5F BE 61 17 82 C6 F3 17 F3 8C 5F BE 5B B1                ;   ON THE SOUTH WALL THERE IS A RED DOOR
3449:   4B 7B 54 45 F3 5F 81 5B 52                                     ;   ~
;
; PrintEastWallBlueDoor
3452: 88 1B                                                            ; Function=88(PrintEastWallBlueDoor) size=001B
3454: 04 19                                                            ; print(msg) size=0019
3456:   03 A0 5F BE 23 15 F3 B9 0E D0 16 8A F4 72 4B 5E                ;   ON THE EAST WALL THERE IS A BLUE DOOR
3466:   C3 B5 B6 14 1B C4 81 5B 52                                     ;   ~
;
; PrintWestWallBlueDoor
346F: 89 1B                                                            ; Function=89(PrintWestWallBlueDoor) size=001B
3471: 04 19                                                            ; print(msg) size=0019
3473:   03 A0 5F BE F7 17 F3 B9 0E D0 16 8A F4 72 4B 5E                ;   ON THE WEST WALL THERE IS A BLUE DOOR
3483:   C3 B5 B6 14 1B C4 81 5B 52                                     ;   ~
;
; PrintClosed
348C: 8A 0D                                                            ; Function=8A(PrintClosed) size=000D
348E: 04 0B                                                            ; print(msg) size=000B
3490:   23 D1 13 54 4B 7B C9 54 A6 B7 2E                               ;   WHICH IS CLOSED.
;
; PrintThisIsOrYouAreIn
349B: 8C 17                                                            ; Function=8C(PrintThisIsOrYouAreIn) size=0017
349D: 0B 15 05                                                         ; switch(is_less_equal_last_random(value)): size=0015
34A0:   7F                                                             ;   is_less_equal_last_random(value) value=7F
34A1:   07                                                             ;   IF_NOT_GOTO address=34A9
34A2:     04 05                                                        ;     print(msg) size=0005
34A4:       63 BE CB B5 53                                             ;       THIS IS
34A9:   FF                                                             ;   is_less_equal_last_random(value) value=FF
34AA:   09                                                             ;   IF_NOT_GOTO address=34B4
34AB:     04 07                                                        ;     print(msg) size=0007
34AD:       C7 DE 94 14 4B 5E 4E                                       ;       YOU ARE IN
;
; PrintPeriod
34B4: 8B 04                                                            ; Function=8B(PrintPeriod) size=0004
34B6: 04 02                                                            ; print(msg) size=0002
34B8:   3B F4                                                          ;   .
;
; PrintObjectIsClosed
34BA: 8D 11                                                            ; Function=8D(PrintObjectIsClosed) size=0011
34BC: 0D 0F                                                            ; while_pass: size=000F
34BE:   14                                                             ;   execute_and_reverse_status:
34BF:   20 38                                                          ;   is_ACTIVE_this(object) object=38(SYSTEM)
34C1:   15 02                                                          ;   check_VAR(bits) bits=02(......O.)
34C3:   AA                                                             ;   AA(PrintTheVarName)
34C4:   04 07                                                          ;   print(msg) size=0007
34C6:     4B 7B C9 54 A6 B7 2E                                         ;     IS CLOSED.
;
; ??GetObject
34CD: 8F 4F                                                            ; Function=8F(??GetObject) size=004F
34CF: 0D 4D                                                            ; while_pass: size=004D
34D1:   0E 4A                                                          ;   while_fail: size=004A
34D3:     2D 37                                                        ;     compare_to_VAR(object) phrase=??? Phrase 37 not found
34D5:     0D 1A                                                        ;     while_pass: size=001A
34D7:       15 10                                                      ;       check_VAR(bits) bits=10(...P....)
34D9:       04 16                                                      ;       print(msg) size=0016
34DB:         46 77 05 A0 16 BC 90 73 CA 83 59 5E 46 7A E1 14          ;         I DON'T THINK HE WILL COOPERATE.
34EB:         5F A0 D6 B0 DB 63                                        ;         ~
34F1:     0D 1F                                                        ;     while_pass: size=001F
34F3:       14                                                         ;       execute_and_reverse_status:
34F4:       15 20                                                      ;       check_VAR(bits) bits=20(..C.....)
34F6:       04 18                                                      ;       print(msg) size=0018
34F8:         C7 DE 94 14 53 5E D6 C4 4B 5E 13 98 44 A4 DB 8B          ;         YOU ARE QUITE INCAPABLE OF REMOVING
3508:         C3 9E 6F B1 53 A1 AB 98                                  ;         ~
3510:       AA                                                         ;       AA(PrintTheVarName)
3511:       8B                                                         ;       8B(PrintPeriod)
3512:     18                                                           ;     is_VAR_owned_by_ACTIVE()
3513:     0D 08                                                        ;     while_pass: size=0008
3515:       0F                                                         ;       pick_up_VAR()
3516:       AA                                                         ;       AA(PrintTheVarName)
3517:       04 04                                                      ;       print(msg) size=0004
3519:         4D BD A7 61                                              ;         TAKEN.
351D:   18                                                             ;   is_VAR_owned_by_ACTIVE()
;
; PrintAlreadyHaveObject
351E: A2 13                                                            ; Function=A2(PrintAlreadyHaveObject) size=0013
3520: 0D 11                                                            ; while_pass: size=0011
3522:   1A                                                             ;   set_VAR_to_first_noun()
3523:   18                                                             ;   is_VAR_owned_by_ACTIVE()
3524:   04 0B                                                          ;   print(msg) size=000B
3526:     C7 DE 8E 14 63 B1 FB 5C 58 72 45                             ;     YOU ALREADY HAVE
3531:   AA                                                             ;   AA(PrintTheVarName)
3532:   8B                                                             ;   8B(PrintPeriod)
;
; ??SomethingUseDirections
3533: 90 09                                                            ; Function=90(??SomethingUseDirections) size=0009
3535: 0B 07 0A                                                         ; switch(compare_input_to(phrase)): size=0007
3538:   36                                                             ;   compare_input_to(phrase) phrase=??? Phrase 36 not found
3539:   01                                                             ;   IF_NOT_GOTO address=353B
353A:     91                                                           ;     91(PrintUseDirections)
353B:   37                                                             ;   compare_input_to(phrase) phrase=??? Phrase 37 not found
353C:   01                                                             ;   IF_NOT_GOTO address=353E
353D:     91                                                           ;     91(PrintUseDirections)
;
; PrintUseDirections
353E: 91 19                                                            ; Function=91(PrintUseDirections) size=0019
3540: 1F 17                                                            ; print2(msg) size=0017
3542:   FF A5 57 49 B5 17 46 5E 2F 7B 03 56 1D A0 A6 16                ;   PLEASE USE DIRECTIONS N,S,E, OR W.
3552:   3F BB 11 EE 99 AF 2E                                           ;   ~
;
; ??YouCantDoThatTo
3559: 92 18                                                            ; Function=92(??YouCantDoThatTo) size=0018
355B: 0D 16                                                            ; while_pass: size=0016
355D:   1A                                                             ;   set_VAR_to_first_noun()
355E:   14                                                             ;   execute_and_reverse_status:
355F:   15 08                                                          ;   check_VAR(bits) bits=08(....A...)
3561:   04 0E                                                          ;   print(msg) size=000E
3563:     C7 DE D3 14 E6 96 09 15 82 17 73 49 6B BF                    ;     YOU CAN'T DO THAT TO
3571:   A8                                                             ;   A8(PrintTheFirstNoun)
3572:   8B                                                             ;   8B(PrintPeriod)
;
; InitializeGame
3573: 94 80 8C                                                         ; Function=94(InitializeGame) size=008C
3576: 0D 80 89                                                         ; while_pass: size=0089
3579:   17 1C 00                                                       ;   move_to(object,room) object=1C(RayA) room=00(Room_00)
357C:   17 1D 00                                                       ;   move_to(object,room) object=1D(RayB) room=00(Room_00)
357F:   17 1E 00                                                       ;   move_to(object,room) object=1E(NapoleanA) room=00(Room_00)
3582:   17 1F 00                                                       ;   move_to(object,room) object=1F(Object1F) room=00(Room_00)
3585:   17 20 00                                                       ;   move_to(object,room) object=20(NapoleanB) room=00(Room_00)
3588:   17 21 00                                                       ;   move_to(object,room) object=21(Object21) room=00(Room_00)
358B:   17 22 00                                                       ;   move_to(object,room) object=22(PicassoA) room=00(Room_00)
358E:   17 23 00                                                       ;   move_to(object,room) object=23(Object23) room=00(Room_00)
3591:   17 24 00                                                       ;   move_to(object,room) object=24(PicassoB) room=00(Room_00)
3594:   17 25 00                                                       ;   move_to(object,room) object=25(Object25) room=00(Room_00)
3597:   17 26 00                                                       ;   move_to(object,room) object=26(MerlinA) room=00(Room_00)
359A:   17 27 00                                                       ;   move_to(object,room) object=27(MerlinB) room=00(Room_00)
359D:   17 28 00                                                       ;   move_to(object,room) object=28(UnconsciousDoctorA) room=00(Room_00)
35A0:   17 29 00                                                       ;   move_to(object,room) object=29(UnconsciousDoctorB) room=00(Room_00)
35A3:   17 2A 00                                                       ;   move_to(object,room) object=2A(HoudiniA) room=00(Room_00)
35A6:   17 2B 00                                                       ;   move_to(object,room) object=2B(HoudiniB) room=00(Room_00)
35A9:   17 2C 00                                                       ;   move_to(object,room) object=2C(HoudiniC) room=00(Room_00)
35AC:   17 1B 8E                                                       ;   move_to(object,room) object=1B(GreenKeyA) room=8E(Electroshock room)
35AF:   17 14 00                                                       ;   move_to(object,room) object=14(RedKeyA) room=00(Room_00)
35B2:   17 16 81                                                       ;   move_to(object,room) object=16(WindowHook) room=81(Maintenance room)
35B5:   17 3B 82                                                       ;   move_to(object,room) object=3B(RedKeyB) room=82(Dispensary)
35B8:   17 3D 00                                                       ;   move_to(object,room) object=3D(SecretDoor) room=00(Room_00)
35BB:   17 15 00                                                       ;   move_to(object,room) object=15(BluePillA) room=00(Room_00)
35BE:   17 39 00                                                       ;   move_to(object,room) object=39(BluePillB) room=00(Room_00)
35C1:   17 41 8C                                                       ;   move_to(object,room) object=41(GreenKeyB) room=8C(East end east-west hall)
35C4:   0B 2B 05                                                       ;   switch(is_less_equal_last_random(value)): size=002B
35C7:     55                                                           ;     is_less_equal_last_random(value) value=55
35C8:     0B                                                           ;     IF_NOT_GOTO address=35D4
35C9:       0D 09                                                      ;       while_pass: size=0009
35CB:         17 15 82                                                 ;         move_to(object,room) object=15(BluePillA) room=82(Dispensary)
35CE:         1C 1F                                                    ;         set_VAR(object) object=1F(Object1F)
35D0:         95                                                       ;         95(RandomMoveAndDrop)
35D1:         1C 23                                                    ;         set_VAR(object) object=23(Object23)
35D3:         95                                                       ;         95(RandomMoveAndDrop)
35D4:     AB                                                           ;     is_less_equal_last_random(value) value=AB
35D5:     0E                                                           ;     IF_NOT_GOTO address=35E4
35D6:       0D 0C                                                      ;       while_pass: size=000C
35D8:         17 39 82                                                 ;         move_to(object,room) object=39(BluePillB) room=82(Dispensary)
35DB:         1C 21                                                    ;         set_VAR(object) object=21(Object21)
35DD:         95                                                       ;         95(RandomMoveAndDrop)
35DE:         1C 3D                                                    ;         set_VAR(object) object=3D(SecretDoor)
35E0:         95                                                       ;         95(RandomMoveAndDrop)
35E1:         1C 23                                                    ;         set_VAR(object) object=23(Object23)
35E3:         95                                                       ;         95(RandomMoveAndDrop)
35E4:     FF                                                           ;     is_less_equal_last_random(value) value=FF
35E5:     0B                                                           ;     IF_NOT_GOTO address=35F1
35E6:       0D 09                                                      ;       while_pass: size=0009
35E8:         17 39 82                                                 ;         move_to(object,room) object=39(BluePillB) room=82(Dispensary)
35EB:         1C 1F                                                    ;         set_VAR(object) object=1F(Object1F)
35ED:         95                                                       ;         95(RandomMoveAndDrop)
35EE:         1C 25                                                    ;         set_VAR(object) object=25(Object25)
35F0:         95                                                       ;         95(RandomMoveAndDrop)
35F1:   1C 1D                                                          ;   set_VAR(object) object=1D(RayB)
35F3:   95                                                             ;   95(RandomMoveAndDrop)
35F4:   1C 27                                                          ;   set_VAR(object) object=27(MerlinB)
35F6:   95                                                             ;   95(RandomMoveAndDrop)
35F7:   1C 29                                                          ;   set_VAR(object) object=29(UnconsciousDoctorB)
35F9:   95                                                             ;   95(RandomMoveAndDrop)
35FA:   1C 2B                                                          ;   set_VAR(object) object=2B(HoudiniB)
35FC:   95                                                             ;   95(RandomMoveAndDrop)
35FD:   17 2E 95                                                       ;   move_to(object,room) object=2E(Doctor) room=95(Office)
3600:   00 88                                                          ;   move_ACTIVE_and_look(room) room=88(Small square room)
;
; RandomMoveAndDrop
3602: 95 53                                                            ; Function=95(RandomMoveAndDrop) size=0053
3604: 0D 51                                                            ; while_pass: size=0051
3606:   2B                                                             ;   generate_random()
3607:   0B 4E 05                                                       ;   switch(is_less_equal_last_random(value)): size=004E
360A:     18                                                           ;     is_less_equal_last_random(value) value=18
360B:     05                                                           ;     IF_NOT_GOTO address=3611
360C:       0D 03                                                      ;       while_pass: size=0003
360E:         19 85                                                    ;         move_ACTIVE(room) room=85(Padded room A)
3610:         10                                                       ;         drop_VAR()
3611:     30                                                           ;     is_less_equal_last_random(value) value=30
3612:     05                                                           ;     IF_NOT_GOTO address=3618
3613:       0D 03                                                      ;       while_pass: size=0003
3615:         19 86                                                    ;         move_ACTIVE(room) room=86(Padded room B)
3617:         10                                                       ;         drop_VAR()
3618:     47                                                           ;     is_less_equal_last_random(value) value=47
3619:     05                                                           ;     IF_NOT_GOTO address=361F
361A:       0D 03                                                      ;       while_pass: size=0003
361C:         19 89                                                    ;         move_ACTIVE(room) room=89(Padded room C)
361E:         10                                                       ;         drop_VAR()
361F:     5E                                                           ;     is_less_equal_last_random(value) value=5E
3620:     05                                                           ;     IF_NOT_GOTO address=3626
3621:       0D 03                                                      ;       while_pass: size=0003
3623:         19 8B                                                    ;         move_ACTIVE(room) room=8B(Padded room D)
3625:         10                                                       ;         drop_VAR()
3626:     75                                                           ;     is_less_equal_last_random(value) value=75
3627:     05                                                           ;     IF_NOT_GOTO address=362D
3628:       0D 03                                                      ;       while_pass: size=0003
362A:         19 8D                                                    ;         move_ACTIVE(room) room=8D(Padded room E)
362C:         10                                                       ;         drop_VAR()
362D:     8C                                                           ;     is_less_equal_last_random(value) value=8C
362E:     05                                                           ;     IF_NOT_GOTO address=3634
362F:       0D 03                                                      ;       while_pass: size=0003
3631:         19 90                                                    ;         move_ACTIVE(room) room=90(Padded room F)
3633:         10                                                       ;         drop_VAR()
3634:     A3                                                           ;     is_less_equal_last_random(value) value=A3
3635:     05                                                           ;     IF_NOT_GOTO address=363B
3636:       0D 03                                                      ;       while_pass: size=0003
3638:         19 92                                                    ;         move_ACTIVE(room) room=92(Kitchen)
363A:         10                                                       ;         drop_VAR()
363B:     BA                                                           ;     is_less_equal_last_random(value) value=BA
363C:     05                                                           ;     IF_NOT_GOTO address=3642
363D:       0D 03                                                      ;       while_pass: size=0003
363F:         19 96                                                    ;         move_ACTIVE(room) room=96(South end north-south hall)
3641:         10                                                       ;         drop_VAR()
3642:     D1                                                           ;     is_less_equal_last_random(value) value=D1
3643:     05                                                           ;     IF_NOT_GOTO address=3649
3644:       0D 03                                                      ;       while_pass: size=0003
3646:         19 97                                                    ;         move_ACTIVE(room) room=97(Dining room)
3648:         10                                                       ;         drop_VAR()
3649:     E8                                                           ;     is_less_equal_last_random(value) value=E8
364A:     05                                                           ;     IF_NOT_GOTO address=3650
364B:       0D 03                                                      ;       while_pass: size=0003
364D:         19 98                                                    ;         move_ACTIVE(room) room=98(Recreation room)
364F:         10                                                       ;         drop_VAR()
3650:     FF                                                           ;     is_less_equal_last_random(value) value=FF
3651:     05                                                           ;     IF_NOT_GOTO address=3657
3652:       0D 03                                                      ;       while_pass: size=0003
3654:         19 94                                                    ;         move_ACTIVE(room) room=94(Padded room G)
3656:         10                                                       ;         drop_VAR()
;
; AwakenInRoom
3657: A3 61                                                            ; Function=A3(AwakenInRoom) size=0061
3659: 0D 5F                                                            ; while_pass: size=005F
365B:   2C 13                                                          ;   set_ACTIVE(object) object=13(PLAYER)
365D:   19 88                                                          ;   move_ACTIVE(room) room=88(Small square room)
365F:   1F 59                                                          ;   print2(msg) size=0059
3661:     C7 DE 4F 15 33 61 4B 49 69 BE 7A C4 51 18 4A C2              ;     YOU FEEL AS THOUGH YOU HAVE JUST AWAKENE
3671:     CF 49 FF 15 F3 B9 F3 49 B0 85 F3 5F 79 68 43 90              ;     D FROM A VERY LONG BAD DREAM ABOUT DOCTO
3681:     CF 17 7B B4 80 8D C4 6A F3 46 EF 5B 5B 48 B9 46              ;     RS AND PADDED ROOMS. YOUR THOUGHTS ARE,
3691:     73 C6 75 5B 84 BF C3 B5 33 98 46 A4 E6 59 39 17              ;     "WHERE AM I?"
36A1:     F5 9F 5B F4 34 A1 82 17 29 A1 4D 75 94 14 B3 63              ;     ~
36B1:     3A 1E 2F 62 8F 14 B8 15 22                                   ;     ~
;
; PrintNapoleanIntro
36BA: 96 62                                                            ; Function=96(PrintNapoleanIntro) size=0062
36BC: 04 60                                                            ; print(msg) size=0060
36BE:   55 45 84 74 73 C1 F0 68 7B 9B 81 8D 50 86 CF 6A                ;   A SHORT, FUNNY LOOKING MAN STANDS NEARBY
36CE:   83 48 FB B9 4D 98 8F 16 2C 49 DB E0 DB 72 81 8D                ;   . HE LOOKS AT YOU, "BOW IN THE PRESENCE
36DE:   CB 87 73 49 C7 DE FC ED 09 4F D0 15 82 17 52 5E                ;   OF NAPOLEON BONAPARTE! I AM THE MIGHTIES
36EE:   75 B1 8D 61 51 5E 90 64 E9 48 F1 8B 84 96 0B A0                ;   T LEADER IN THE WORLD!"
36FE:   54 A4 D9 BD BB 15 5B 48 5F BE 6B 16 2E 6D 35 79                ;   ~
370E:   0E BC 86 5F 23 62 83 7A 5F BE 01 18 7E B2 E3 06                ;   ~
;
; PrintNapolean
371E: 97 20                                                            ; Function=97(PrintNapolean) size=0020
3720: 04 1E                                                            ; print(msg) size=001E
3722:   D2 97 BF 9F 03 A0 4B 7B F0 B3 10 99 CA 6A 4B 7B                ;   NAPOLEON IS RUNNING HIS HANDS OVER THE W
3732:   50 72 0B 5C 4F A1 96 AF DB 72 0E D0 2F 8E                      ;   ALLS.
;
; PrintPicassoIntro
3740: 98 80 80                                                         ; Function=98(PrintPicassoIntro) size=0080
3743: 04 7E                                                            ; print(msg) size=007E
3745:   4F 45 83 48 83 7A 59 45 96 73 48 5E F5 B2 33 89                ;   A MAN IN A WHITE FROCK, A BERET, AND HOL
3755:   44 45 2F 62 73 C1 8E 48 A9 15 C3 8B AB 98 52 45                ;   DING A PALETTE AND BRUSH SEEMS TO BE PAI
3765:   3F 48 3F C0 90 14 04 58 F5 B3 15 71 2F 60 D6 B5                ;   NTING WHAT LOOKS LIKE A DOOR ON ONE OF T
3775:   C4 9C 52 5E D0 47 90 BE D9 6A 56 72 49 16 A5 9F                ;   HE WALLS. HE LOOKS UP, "EYE AM A GRATE A
3785:   43 16 9B 85 46 45 44 A0 C0 16 C0 16 51 5E 96 64                ;   RTEEST! MAH NAM EEZ PICASSO!"
3795:   DB 72 0E D0 2F 8E 9F 15 49 16 A5 9F B2 17 FC ED                ;   ~
37A5:   47 63 8F 14 7B 14 AB 6E DB BD 3E 49 35 60 AB BB                ;   ~
37B5:   8A 91 8B 16 47 90 63 63 85 A5 65 49 6C 9C                      ;   ~
;
; PrintPicasso
37C3: 99 22                                                            ; Function=99(PrintPicasso) size=0022
37C5: 04 20                                                            ; print(msg) size=0020
37C7:   85 A5 65 49 D5 9C 2F 60 D6 B5 C4 9C 52 5E D0 47                ;   PICASSO SEEMS TO BE PAINTING A DOOR ON O
37D7:   90 BE C3 6A 09 15 A3 A0 03 A0 0F A0 F3 17 17 8D                ;   NE WALL.
;
; PrintBluePill
37E7: 9D 14                                                            ; Function=9D(PrintBluePill) size=0014
37E9: 04 12                                                            ; print(msg) size=0012
37EB:   5F BE 5B B1 4B 7B 44 45 67 8E E3 16 F3 8C F4 72                ;   THERE IS A BLUE PILL HERE.
37FB:   DB 63                                                          ;   ~
;
; PrintUnshavenMan
37FD: 9F 50                                                            ; Function=9F(PrintUnshavenMan) size=0050
37FF: 1F 4E                                                            ; print2(msg) size=004E
3801:   55 45 84 74 73 C1 09 BA AB 54 17 EE 9A 9A CF 49                ;   A SHORT, STOCKY, UNSHAVEN MAN WEARING A
3811:   8F 96 83 48 A3 D0 10 B2 C3 6A B6 14 36 A0 59 DB                ;   BLOODY WHITE SURGICAL GOWN AND HOLDING A
3821:   96 73 55 5E 31 C6 D3 78 09 8A 80 A1 90 14 0A 58                ;   LARGE HYPODERMIC IS STARING AT YOU.
3831:   BE 9F 91 7A 7B 14 54 8B 9B 6C 12 76 7F 9E AB B2                ;   ~
3841:   CB 51 D5 B5 54 BD 91 7A 96 14 51 18 DB C7                      ;   ~
;
; ??CommandResponse
384F: 9A 80 C5                                                         ; Function=9A(??CommandResponse) size=00C5
3852: 0E 80 C2                                                         ; while_fail: size=00C2
3855:   0D 20                                                          ;   while_pass: size=0020
3857:     0E 04                                                        ;     while_fail: size=0004
3859:       0A 46                                                      ;       compare_input_to(phrase) phrase="46: WHAT * * *"
385B:       0A 47                                                      ;       compare_input_to(phrase) phrase="47: WHAT u....... * *"
385D:     1F 18                                                        ;     print2(msg) size=0018
385F:       91 1E 59 C2 46 7A 9B 15 5B CA C7 DE 83 AF A9 9A            ;       "YOU WILL HAVE YOUR ANSWER IN TIME."
386F:       23 62 83 7A 8F BE DC 63                                    ;       ~
3877:   0D 13                                                          ;   while_pass: size=0013
3879:     0A 49                                                        ;     compare_input_to(phrase) phrase="49: MEET u....... * *"
387B:     1F 0F                                                        ;     print2(msg) size=000F
387D:       5F BE 49 DB 67 B1 07 BC DA 46 C6 16 F4 72 2E               ;       THEY GREET EACH OTHER.
388C:   0D 11                                                          ;   while_pass: size=0011
388E:     0A 4A                                                        ;     compare_input_to(phrase) phrase="4A: COME * * *"
3890:     1F 0D                                                        ;     print2(msg) size=000D
3892:       FD 1C 0E EE 86 5F 82 17 59 5E 5F 4A 22                     ;       "OK, LEAD THE WAY."
389F:   0D 18                                                          ;   while_pass: size=0018
38A1:     0A 2F                                                        ;     compare_input_to(phrase) phrase="2F: WAIT * * *"
38A3:     1F 14                                                        ;     print2(msg) size=0014
38A5:       91 1E 59 C2 2E A1 45 5B 0E BC 98 5F 4F 5E 4A 5E            ;       "YOU WOULDN'T LEAVE ME HERE!"
38B5:       2F 62 E3 06                                                ;       ~
38B9:   0D 5C                                                          ;   while_pass: size=005C
38BB:     1F 0F                                                        ;     print2(msg) size=000F
38BD:       5F BE B4 16 03 BA D6 97 54 5E E6 61 4B DB 53               ;       THE OBSTINATE REPLY IS
38CC:     0B 49 05                                                     ;     switch(is_less_equal_last_random(value)): size=0049
38CF:       41                                                         ;       is_less_equal_last_random(value) value=41
38D0:       14                                                         ;       IF_NOT_GOTO address=38E5
38D1:         1F 12                                                    ;         print2(msg) size=0012
38D3:           D9 1C 0B EE DB 22 06 9A 51 18 23 C6 B4 B7 D0 C9        ;           "NO, I'M NOT YOUR SERVANT!"
38E3:           AC BB                                                  ;           ~
38E5:       82                                                         ;       is_less_equal_last_random(value) value=82
38E6:       0E                                                         ;       IF_NOT_GOTO address=38F5
38E7:         1F 0C                                                    ;         print2(msg) size=000C
38E9:           49 1B D6 15 51 18 3D C6 40 61 E3 06                    ;           "DO IT YOURSELF!"
38F5:       C3                                                         ;       is_less_equal_last_random(value) value=C3
38F6:       10                                                         ;       IF_NOT_GOTO address=3907
38F7:         1F 0E                                                    ;         print2(msg) size=000E
38F9:           91 1E 4F C2 66 C6 AF 14 E4 14 83 4A E3 06              ;           "YOU MUST BE CRAZY!"
3907:       FF                                                         ;       is_less_equal_last_random(value) value=FF
3908:       0E                                                         ;       IF_NOT_GOTO address=3917
3909:         1F 0C                                                    ;         print2(msg) size=000C
390B:           FB 1B 80 5B F3 23 10 D0 16 BC 5C A2                    ;           "I DON'T WANT TO."
;
; ??MoveHoudiniC
3917: 9C 34                                                            ; Function=9C(??MoveHoudiniC) size=0034
3919: 0B 32 05                                                         ; switch(is_less_equal_last_random(value)): size=0032
391C:   E6                                                             ;   is_less_equal_last_random(value) value=E6
391D:   27                                                             ;   IF_NOT_GOTO address=3945
391E:     0D 25                                                        ;     while_pass: size=0025
3920:       14                                                         ;       execute_and_reverse_status:
3921:       01 13                                                      ;       is_in_pack_or_current_room(object) object=13(PLAYER)
3923:       0E 05                                                      ;       while_fail: size=0005
3925:         20 2C                                                    ;         is_ACTIVE_this(object) object=2C(HoudiniC)
3927:         14                                                       ;         execute_and_reverse_status:
3928:         01 2C                                                    ;         is_in_pack_or_current_room(object) object=2C(HoudiniC)
392A:       0B 19 0A                                                   ;       switch(compare_input_to(phrase)): size=0019
392D:         04                                                       ;         compare_input_to(phrase) phrase="04: WEST * * *"
392E:         04                                                       ;         IF_NOT_GOTO address=3933
392F:           21 04 00 00                                            ;           execute_phrase(phrase,first_noun,second_noun) phrase="04: WEST * * *" firstNoun=00 secondNoun=00
3933:         03                                                       ;         compare_input_to(phrase) phrase="03: EAST * * *"
3934:         04                                                       ;         IF_NOT_GOTO address=3939
3935:           21 03 00 00                                            ;           execute_phrase(phrase,first_noun,second_noun) phrase="03: EAST * * *" firstNoun=00 secondNoun=00
3939:         01                                                       ;         compare_input_to(phrase) phrase="01: NORTH * * *"
393A:         04                                                       ;         IF_NOT_GOTO address=393F
393B:           21 01 00 00                                            ;           execute_phrase(phrase,first_noun,second_noun) phrase="01: NORTH * * *" firstNoun=00 secondNoun=00
393F:         02                                                       ;         compare_input_to(phrase) phrase="02: SOUTH * * *"
3940:         04                                                       ;         IF_NOT_GOTO address=3945
3941:           21 02 00 00                                            ;           execute_phrase(phrase,first_noun,second_noun) phrase="02: SOUTH * * *" firstNoun=00 secondNoun=00
3945:   FF                                                             ;   is_less_equal_last_random(value) value=FF
3946:   06                                                             ;   IF_NOT_GOTO address=394D
3947:     0D 04                                                        ;     while_pass: size=0004
3949:       14                                                         ;       execute_and_reverse_status:
394A:       01 13                                                      ;       is_in_pack_or_current_room(object) object=13(PLAYER)
394C:       9B                                                         ;       9B(??PrintDirs)
;
; ??PrintDirs
394D: 9B 41                                                            ; Function=9B(??PrintDirs) size=0041
394F: 0B 3F 05                                                         ; switch(is_less_equal_last_random(value)): size=003F
3952:   3F                                                             ;   is_less_equal_last_random(value) value=3F
3953:   0D                                                             ;   IF_NOT_GOTO address=3961
3954:     0D 0B                                                        ;     while_pass: size=000B
3956:       25                                                         ;       restart_game()
3957:       04 03                                                      ;       print(msg) size=0003
3959:         B5 D0 54                                                 ;         WEST
395C:       25                                                         ;       restart_game()
395D:       21 04 00 00                                                ;       execute_phrase(phrase,first_noun,second_noun) phrase="04: WEST * * *" firstNoun=00 secondNoun=00
3961:   7F                                                             ;   is_less_equal_last_random(value) value=7F
3962:   0D                                                             ;   IF_NOT_GOTO address=3970
3963:     0D 0B                                                        ;     while_pass: size=000B
3965:       25                                                         ;       restart_game()
3966:       04 03                                                      ;       print(msg) size=0003
3968:         95 5F 54                                                 ;         EAST
396B:       25                                                         ;       restart_game()
396C:       21 03 00 00                                                ;       execute_phrase(phrase,first_noun,second_noun) phrase="03: EAST * * *" firstNoun=00 secondNoun=00
3970:   BF                                                             ;   is_less_equal_last_random(value) value=BF
3971:   0E                                                             ;   IF_NOT_GOTO address=3980
3972:     0D 0C                                                        ;     while_pass: size=000C
3974:       25                                                         ;       restart_game()
3975:       04 04                                                      ;       print(msg) size=0004
3977:         04 9A 53 BE                                              ;         NORTH
397B:       25                                                         ;       restart_game()
397C:       21 01 00 00                                                ;       execute_phrase(phrase,first_noun,second_noun) phrase="01: NORTH * * *" firstNoun=00 secondNoun=00
3980:   FF                                                             ;   is_less_equal_last_random(value) value=FF
3981:   0E                                                             ;   IF_NOT_GOTO address=3990
3982:     0D 0C                                                        ;     while_pass: size=000C
3984:       25                                                         ;       restart_game()
3985:       04 04                                                      ;       print(msg) size=0004
3987:         47 B9 53 BE                                              ;         SOUTH
398B:       25                                                         ;       restart_game()
398C:       21 02 00 00                                                ;       execute_phrase(phrase,first_noun,second_noun) phrase="02: SOUTH * * *" firstNoun=00 secondNoun=00
;
; PrintObjectEntersRoom
3990: 9E 14                                                            ; Function=9E(PrintObjectEntersRoom) size=0014
3992: 0D 12                                                            ; while_pass: size=0012
3994:   01 13                                                          ;   is_in_pack_or_current_room(object) object=13(PLAYER)
3996:   2C 13                                                          ;   set_ACTIVE(object) object=13(PLAYER)
3998:   AA                                                             ;   AA(PrintTheVarName)
3999:   04 0B                                                          ;   print(msg) size=000B
399B:     9E 61 3D 62 82 17 54 5E 3F A0 2E                             ;     ENTERS THE ROOM.
;
; PrintPillInHamburger
39A6: A0 20                                                            ; Function=A0(PrintPillInHamburger) size=0020
39A8: 04 1E                                                            ; print(msg) size=001E
39AA:   5F BE E3 16 F3 8C A7 B7 4B 94 6B BF 95 5A 3E B9                ;   THE PILL SEEMS TO DISSOLVE IN THE HAMBUR
39BA:   5B CA 83 7A 5F BE 9B 15 BF 91 B7 B1 1B B5                      ;   GER.
;
; FeedDogMeat
39C8: A1 6F                                                            ; Function=A1(FeedDogMeat) size=006F
39CA: 0D 6D                                                            ; while_pass: size=006D
39CC:   0E 08                                                          ;   while_fail: size=0008
39CE:     0A 28                                                        ;     compare_input_to(phrase) phrase="28: FEED ...P.... WITH u......."
39D0:     0A 0E                                                        ;     compare_input_to(phrase) phrase="0E: THROW u....... TO ...P...."
39D2:     0A 29                                                        ;     compare_input_to(phrase) phrase="29: FEED u....... TO ...P...."
39D4:     0A 0D                                                        ;     compare_input_to(phrase) phrase="0D: THROW .v...... AT ...P...."
39D6:   0E 04                                                          ;   while_fail: size=0004
39D8:     09 19                                                        ;     compare_to_second_noun(object) object=19(HamburgerMeat)
39DA:     08 19                                                        ;     is_first_noun(object) object=19(HamburgerMeat)
39DC:   04 28                                                          ;   print(msg) size=0028
39DE:     5F BE 09 15 D9 6A C0 9F C6 B5 80 A1 82 17 4A 5E              ;     THE DOG WOLFS DOWN THE HAMBURGER. HE MUS
39EE:     64 48 31 C6 47 62 9F 15 77 16 F3 B9 5B 4D EF A6              ;     T BE PRETTY HUNGRY!
39FE:     53 C0 AF 15 C4 98 EB DA                                      ;     ~
3A06:   17 19 00                                                       ;   move_to(object,room) object=19(HamburgerMeat) room=00(Room_00)
3A09:   0E 2E                                                          ;   while_fail: size=002E
3A0B:     0D 2A                                                        ;     while_pass: size=002A
3A0D:       03 19 15                                                   ;       is_located(room,object) room=19(Room_19) object=15(BluePillA)
3A10:       04 22                                                      ;       print(msg) size=0022
3A12:         5F BE 09 15 CE 6A 3D A0 D5 B5 DD 78 4A F4 59 5E          ;         THE DOG LOOKS SICK. HE WEAVES AND FALLS
3A22:         98 5F 4B 62 8E 48 4B 15 0D 8D C8 16 23 62 E3 59          ;         OVER DEAD.
3A32:         9B 5D                                                    ;         ~
3A34:       1E 1A 3C                                                   ;       swap(object_a,object_b) object_a=(GuardDog)1A object_b=3C(DeadDog)
3A37:     14                                                           ;     execute_and_reverse_status:
3A38:     0C                                                           ;     fail()
;
; PrintPicassoDoor
3A39: A4 43                                                            ; Function=A4(PrintPicassoDoor) size=0043
3A3B: 0D 41                                                            ; while_pass: size=0041
3A3D:   0A 0B                                                          ;   compare_input_to(phrase) phrase="0B: LOOK * AT u......."
3A3F:   0E 3D                                                          ;   while_fail: size=003D
3A41:     0D 17                                                        ;     while_pass: size=0017
3A43:       01 3D                                                      ;       is_in_pack_or_current_room(object) object=3D(SecretDoor)
3A45:       1F 13                                                      ;       print2(msg) size=0013
3A47:         5F BE 5B B1 4B 7B 55 45 E4 5F 73 62 81 5B 8A AF          ;         THERE IS A SECRET DOOR HERE.
3A57:         2F 62 2E                                                 ;         ~
3A5A:     0D 22                                                        ;     while_pass: size=0022
3A5C:       0E 04                                                      ;       while_fail: size=0004
3A5E:         01 3E                                                    ;         is_in_pack_or_current_room(object) object=3E(PaintedDoorA)
3A60:         01 3F                                                    ;         is_in_pack_or_current_room(object) object=3F(PaintedDoorB)
3A62:       1F 1A                                                      ;       print2(msg) size=001A
3A64:         85 A5 65 49 CA 9C 4B 49 4B A4 BF 9A 03 58 09 15          ;         PICASSO HAS PAINTED A DOOR ON ONE WALL.
3A74:         A3 A0 03 A0 0F A0 F3 17 17 8D                            ;         ~
;
; AttemptClose
3A7E: A5 12                                                            ; Function=A5(AttemptClose) size=0012
3A80: 0D 10                                                            ; while_pass: size=0010
3A82:   14                                                             ;   execute_and_reverse_status:
3A83:   15 02                                                          ;   check_VAR(bits) bits=02(......O.)
3A85:   A8                                                             ;   A8(PrintTheFirstNoun)
3A86:   04 0A                                                          ;   print(msg) size=000A
3A88:     4B 7B 06 9A DE 14 D7 A0 9B 5D                                ;     IS NOT CLOSED.
;
; AttemptOpen
3A92: A6 0E                                                            ; Function=A6(AttemptOpen) size=000E
3A94: 0D 0C                                                            ; while_pass: size=000C
3A96:   29                                                             ;   print_open_VAR()
3A97:   A8                                                             ;   A8(PrintTheFirstNoun)
3A98:   04 08                                                          ;   print(msg) size=0008
3A9A:     4B 7B 09 9A C2 16 A7 61                                      ;     IS NOW OPEN.
;
; AttemptUnlock
3AA2: A7 2A                                                            ; Function=A7(AttemptUnlock) size=002A
3AA4: 0D 28                                                            ; while_pass: size=0028
3AA6:   15 01                                                          ;   check_VAR(bits) bits=01(.......L)
3AA8:   0E 0F                                                          ;   while_fail: size=000F
3AAA:     0D 05                                                        ;     while_pass: size=0005
3AAC:       08 40                                                      ;       is_first_noun(object) object=40(GreenDoorI)
3AAE:       14                                                         ;       execute_and_reverse_status:
3AAF:       09 1B                                                      ;       compare_to_second_noun(object) object=1B(GreenKeyA)
3AB1:     0D 06                                                        ;     while_pass: size=0006
3AB3:       14                                                         ;       execute_and_reverse_status:
3AB4:       08 40                                                      ;       is_first_noun(object) object=40(GreenDoorI)
3AB6:       14                                                         ;       execute_and_reverse_status:
3AB7:       09 14                                                      ;       compare_to_second_noun(object) object=14(RedKeyA)
3AB9:   04 0B                                                          ;   print(msg) size=000B
3ABB:     C7 DE D3 14 E6 96 B0 17 75 8D 4B                             ;     YOU CAN'T UNLOCK
3AC6:   A8                                                             ;   A8(PrintTheFirstNoun)
3AC7:   04 03                                                          ;   print(msg) size=0003
3AC9:     56 D1 48                                                     ;     WITH
3ACC:   A9                                                             ;   A9(PrintTheSecondNoun)
3ACD:   8B                                                             ;   8B(PrintPeriod)
;
; PrintTheFirstNoun
3ACE: A8 0C                                                            ; Function=A8(PrintTheFirstNoun) size=000C
3AD0: 0D 0A                                                            ; while_pass: size=000A
3AD2:   1A                                                             ;   set_VAR_to_first_noun()
3AD3:   0E 06                                                          ;   while_fail: size=0006
3AD5:     15 10                                                        ;     check_VAR(bits) bits=10(...P....)
3AD7:     1F 02                                                        ;     print2(msg) size=0002
3AD9:       5F BE                                                      ;       THE
3ADB:   11                                                             ;   print_first_noun()
;
; PrintTheSecondNoun
3ADC: A9 0C                                                            ; Function=A9(PrintTheSecondNoun) size=000C
3ADE: 0D 0A                                                            ; while_pass: size=000A
3AE0:   1B                                                             ;   set_VAR_to_second_noun()
3AE1:   0E 06                                                          ;   while_fail: size=0006
3AE3:     15 10                                                        ;     check_VAR(bits) bits=10(...P....)
3AE5:     1F 02                                                        ;     print2(msg) size=0002
3AE7:       5F BE                                                      ;       THE
3AE9:   12                                                             ;   print_second_noun
;
; PrintTheVarName
3AEA: AA 0B                                                            ; Function=AA(PrintTheVarName) size=000B
3AEC: 0D 09                                                            ; while_pass: size=0009
3AEE:   0E 06                                                          ;   while_fail: size=0006
3AF0:     15 10                                                        ;     check_VAR(bits) bits=10(...P....)
3AF2:     1F 02                                                        ;     print2(msg) size=0002
3AF4:       5F BE                                                      ;       THE
3AF6:   16                                                             ;   print_VAR
;
; AttackPerson
3AF7: AB 35                                                            ; Function=AB(AttackPerson) size=0035
3AF9: 0D 33                                                            ; while_pass: size=0033
3AFB:   0A 09                                                          ;   compare_input_to(phrase) phrase="09: ATTACK ...P.... WITH .v......"
3AFD:   A8                                                             ;   A8(PrintTheFirstNoun)
3AFE:   1F 2E                                                          ;   print2(msg) size=002E
3B00:     C5 4C CB 87 F3 49 48 DB FF B2 51 18 23 C6 8E 49              ;     BACKS AWAY FROM YOUR ATTACK, AND SAYS, "
3B10:     DD 46 03 EE 33 98 1B B7 33 BB 91 1E 4F C2 66 C6              ;     YOU MUST BE A CRAZY PERSON!"
3B20:     AF 14 7B 14 AB 55 7B E6 F4 A4 40 B9 E3 06                    ;     ~
;
; PrintTheVarName(sameAA)
3B2E: AC 01                                                            ; Function=AC(PrintTheVarName(sameAA)) size=0001
3B30: AA                                                               ; AA(PrintTheVarName)
;
; PrintTheVarNotHungry
3B31: AD 15                                                            ; Function=AD(PrintTheVarNotHungry) size=0015
3B33: 0D 13                                                            ; while_pass: size=0013
3B35:   AA                                                             ;   AA(PrintTheVarName)
3B36:   04 10                                                          ;   print(msg) size=0010
3B38:     60 7B F3 23 70 75 C3 6E 33 17 2E 6D 99 16 5B D4              ;     ISN'T HUNGRY RIGHT NOW.
;
; PrintFindMouthGame
3B48: AE 19                                                            ; Function=AE(PrintFindMouthGame) size=0019
3B4A: 04 17                                                            ; print(msg) size=0017
3B4C:   43 79 C7 DE D3 14 88 96 8E 7A 7B 14 C7 93 76 BE                ;   IF YOU CAN FIND A MOUTH, I'M GAME!
3B5C:   BD 15 49 90 67 48 21                                           ;   ~
;
; PrintLeapsBounds
3B63: AF 23                                                            ; Function=AF(PrintLeapsBounds) size=0023
3B65: 0E 21                                                            ; while_fail: size=0021
3B67:   13                                                             ;   process_phrase_by_room_first_second()
3B68:   04 1E                                                          ;   print(msg) size=001E
3B6A:     C7 DE 95 AF D5 C3 65 62 D5 15 67 16 67 49 66 B1              ;     YOUR SUCCESS IS MEASURED IN LEAPS AND BO
3B7A:     D0 15 3F 16 ED 48 90 14 04 58 30 A1 09 5C                    ;     UNDS!
;
; PrintTastesAweful
3B88: B0 18                                                            ; Function=B0(PrintTastesAweful) size=0018
3B8A: 0D 16                                                            ; while_pass: size=0016
3B8C:   0A 15                                                          ;   compare_input_to(phrase) phrase="15: EAT u....... * *"
3B8E:   04 12                                                          ;   print(msg) size=0012
3B90:     2E 6F AB A2 25 DD 36 54 7B 17 FF B9 C3 B5 DF D0              ;     GULP! YECCH, TASTES AWFUL!
3BA0:     AB 89                                                        ;     ~
;
; PrintYouGetObjectWithObject
3BA2: B1 18                                                            ; Function=B1(PrintYouGetObjectWithObject) size=0018
3BA4: 0D 16                                                            ; while_pass: size=0016
3BA6:   04 05                                                          ;   print(msg) size=0005
3BA8:     C7 DE 77 15 54                                               ;     YOU GET
3BAD:   A8                                                             ;   A8(PrintTheFirstNoun)
3BAE:   04 03                                                          ;   print(msg) size=0003
3BB0:     56 D1 48                                                     ;     WITH
3BB3:   A9                                                             ;   A9(PrintTheSecondNoun)
3BB4:   8B                                                             ;   8B(PrintPeriod)
3BB5:   A8                                                             ;   A8(PrintTheFirstNoun)
3BB6:   04 04                                                          ;   print(msg) size=0004
3BB8:     4D BD A7 61                                                  ;     TAKEN.
;
; PrintCantGetObjectWithObject
3BBC: B2 17                                                            ; Function=B2(PrintCantGetObjectWithObject) size=0017
3BBE: 0D 15                                                            ; while_pass: size=0015
3BC0:   0A 43                                                          ;   compare_input_to(phrase) phrase="43: GET ..C..... WITH ..C....."
3BC2:   04 09                                                          ;   print(msg) size=0009
3BC4:     C7 DE D3 14 E6 96 77 15 54                                   ;     YOU CAN'T GET
3BCD:   A8                                                             ;   A8(PrintTheFirstNoun)
3BCE:   04 03                                                          ;   print(msg) size=0003
3BD0:     56 D1 48                                                     ;     WITH
3BD3:   A9                                                             ;   A9(PrintTheSecondNoun)
3BD4:   8B                                                             ;   8B(PrintPeriod)
; ENDOF 339C
```

# Input Word Tables

Tables are the same in COCO and TRS80.

```code
InputWordTables:

; --- IGNORES ---
3BD5: 00
;
; --- VERBS ---
3BD6: 03 47 45 54 09            ; GET      09
3BDB: 04 47 52 41 42 09         ; GRAB     09
3BE1: 05 54 48 52 4F 57 03      ; THROW    03
3BE8: 06 41 54 54 41 43 4B 04   ; ATTACK   04
3BF0: 05 42 52 45 41 4B 04      ; BREAK    04
3BF7: 04 4B 49 4C 4C 04         ; KILL     04
3BFD: 03 48 49 54 04            ; HIT      04
3C02: 05 4E 4F 52 54 48 05      ; NORTH    05
3C09: 01 4E 05                  ; N        05
3C0C: 05 53 4F 55 54 48 06      ; SOUTH    06
3C13: 01 53 06                  ; S        06
3C16: 04 45 41 53 54 07         ; EAST     07
3C1C: 01 45 07                  ; E        07
3C1F: 04 57 45 53 54 08         ; WEST     08
3C25: 01 57 08                  ; W        08
3C28: 04 54 41 4B 45 09         ; TAKE     09
3C2E: 05 43 41 52 52 59 09      ; CARRY    09
3C35: 04 44 52 4F 50 0A         ; DROP     0A
3C3B: 03 50 55 54 0A            ; PUT      0A
3C40: 06 49 4E 56 45 4E 54 0B   ; INVENT   0B
3C48: 04 4C 4F 4F 4B 0C         ; LOOK     0C
3C4E: 04 47 49 56 45 0D         ; GIVE     0D
3C54: 05 4F 46 46 45 52 0D      ; OFFER    0D
3C5B: 06 45 58 41 4D 49 4E 0E   ; EXAMIN   0E
3C63: 06 53 45 41 52 43 48 0E   ; SEARCH   0E
3C6B: 04 4F 50 45 4E 0F         ; OPEN     0F
3C71: 04 50 55 4C 4C 10         ; PULL     10
3C77: 03 45 41 54 12            ; EAT      12
3C7C: 05 43 4C 49 4D 42 15      ; CLIMB    15
3C83: 06 41 53 43 45 4E 44 15   ; ASCEND   15
3C8B: 06 44 45 53 43 45 4E 15   ; DESCEN   15
3C93: 04 4C 49 46 54 1C         ; LIFT     1C
3C99: 04 57 41 49 54 1F         ; WAIT     1F
3C9F: 04 53 54 41 59 1F         ; STAY     1F
3CA5: 04 4A 55 4D 50 20         ; JUMP     20
3CAB: 02 47 4F 21               ; GO       21
3CAF: 03 52 55 4E 21            ; RUN      21
3CB4: 04 4C 45 46 54 21         ; LEFT     21
3CBA: 05 52 49 47 48 54 21      ; RIGHT    21
3CC1: 05 45 4E 54 45 52 21      ; ENTER    21
3CC8: 04 50 55 53 48 10         ; PUSH     10
3CCE: 04 4D 4F 56 45 10         ; MOVE     10
3CD4: 04 4B 49 43 4B 23         ; KICK     23
3CDA: 04 46 45 45 44 24         ; FEED     24
3CE0: 06 53 43 52 45 41 4D 2B   ; SCREAM   2B
3CE8: 04 59 45 4C 4C 2B         ; YELL     2B
3CEE: 04 51 55 49 54 2D         ; QUIT     2D
3CF4: 04 53 54 4F 50 2D         ; STOP     2D
3CFA: 05 50 4C 55 47 48 32      ; PLUGH    32
3D01: 04 50 49 43 4B 34         ; PICK     34
3D07: 05 43 4C 4F 53 45 38      ; CLOSE    38
3D0E: 04 4C 4F 43 4B 39         ; LOCK     39
3D14: 06 55 4E 4C 4F 43 4B 3A   ; UNLOCK   3A
3D1C: 05 48 45 4C 4C 4F 3B      ; HELLO    3B
3D23: 02 48 49 3B               ; HI       3B
3D27: 03 42 4F 57 3B            ; BOW      3B
3D2C: 05 47 52 45 45 54 3B      ; GREET    3B
3D33: 04 57 48 41 54 3C         ; WHAT     3C
3D39: 03 57 48 59 3C            ; WHY      3C
3D3E: 03 48 4F 57 3C            ; HOW      3C
3D43: 05 57 48 45 52 45 3C      ; WHERE    3C
3D4A: 03 57 48 4F 3C            ; WHO      3C
3D4F: 04 57 48 45 4E 3C         ; WHEN     3C
3D55: 05 4C 4F 57 45 52 3D      ; LOWER    3D
3D5C: 05 55 4E 54 49 45 3D      ; UNTIE    3D
3D63: 03 4C 45 54 3E            ; LET      3E
3D68: 04 43 4F 4D 45 3F         ; COME     3F
3D6E: 06 46 4F 4C 4C 4F 57 3F   ; FOLLOW   3F
3D76: 04 4D 45 45 54 40         ; MEET     40
3D7C: 06 49 4E 54 52 4F 44 40   ; INTROD   40
3D84: 00
;
; --- NOUNS ---
3D85: 03 4B 45 59 16            ; KEY      16
3D8A: 04 50 49 4C 4C 17         ; PILL     17
3D90: 04 48 4F 4F 4B 18         ; HOOK     18
3D96: 04 44 4F 4F 52 0B         ; DOOR     0B
3D9C: 06 43 41 42 49 4E 45 19   ; CABINE   19
3DA4: 06 52 45 46 52 49 47 1A   ; REFRIG   1A
3DAC: 06 48 41 4D 42 55 52 1B   ; HAMBUR   1B
3DB4: 06 42 55 52 47 45 52 1B   ; BURGER   1B
3DBC: 04 4D 45 41 54 1B         ; MEAT     1B
3DC2: 03 44 4F 47 08            ; DOG      08
3DC7: 04 48 41 4E 44 1F         ; HAND     1F
3DCD: 05 48 41 4E 44 53 1F      ; HANDS    1F
3DD4: 06 4E 41 50 4F 4C 45 02   ; NAPOLE   02
3DDC: 06 42 4F 4E 41 50 41 02   ; BONAPA   02
3DE4: 03 52 41 59 03            ; RAY      03
3DE9: 04 58 52 41 59 03         ; XRAY     03
3DEF: 06 4A 4F 48 4E 53 4F 03   ; JOHNSO   03
3DF7: 06 48 4F 55 44 49 4E 04   ; HOUDIN   04
3DFF: 06 50 49 43 41 53 53 05   ; PICASS   05
3E07: 06 4D 45 52 4C 49 4E 06   ; MERLIN   06
3E0F: 06 44 4F 43 54 4F 52 07   ; DOCTOR   07
3E17: 05 4E 55 52 53 45 01      ; NURSE    01
3E1E: 06 54 48 45 52 41 50 01   ; THERAP   01
3E26: 04 57 41 4C 4C 25         ; WALL     25
3E2C: 05 57 41 4C 4C 53 25      ; WALLS    25
3E33: 04 52 4F 4F 4D 2A         ; ROOM     2A
3E39: 04 43 45 4C 4C 2A         ; CELL     2A
3E3F: 06 4F 46 46 49 43 45 2A   ; OFFICE   2A
3E47: 04 53 48 45 44 2A         ; SHED     2A
3E4D: 05 46 4C 4F 4F 52 2B      ; FLOOR    2B
3E54: 04 45 58 49 54 2C         ; EXIT     2C
3E5A: 04 48 4F 4C 45 19         ; HOLE     19
3E60: 06 48 41 4C 4C 57 41 33   ; HALLWA   33
3E68: 06 45 4E 54 52 41 4E 36   ; ENTRAN   36
3E70: 06 43 45 49 4C 49 4E 3B   ; CEILIN   3B
3E78: 04 52 4F 4F 46 3B         ; ROOF     3B
3E7E: 00
;
; --- ADJECTIVES ---
3E7F: 03 52 45 44 13            ; RED      13
3E84: 05 47 52 45 45 4E 14      ; GREEN    14
3E8B: 04 42 4C 55 45 15         ; BLUE     15
3E91: 06 53 45 43 52 45 54 3D   ; SECRET   3D
3E99: 06 50 41 49 4E 54 45 3E   ; PAINTE   3E
3EA1: 00
;
; --- PREPOSITIONS ---
3EA2: 02 54 4F 01               ; TO       01
3EA6: 04 57 49 54 48 02         ; WITH     02
3EAC: 05 55 53 49 4E 47 02      ; USING    02
3EB3: 02 41 54 03               ; AT       03
3EB7: 05 55 4E 44 45 52 04      ; UNDER    04
3EBE: 02 49 4E 05               ; IN       05
3EC2: 04 49 4E 54 4F 05         ; INTO     05
3EC8: 06 49 4E 53 49 44 45 05   ; INSIDE   05
3ED0: 03 4F 55 54 06            ; OUT      06
3ED5: 06 4F 55 54 53 49 44 06   ; OUTSID   06
3EDD: 02 55 50 07               ; UP       07
3EE1: 04 44 4F 57 4E 08         ; DOWN     08
3EE7: 04 4F 56 45 52 09         ; OVER     09
3EED: 06 42 45 48 49 4E 44 0A   ; BEHIND   0A
3EF5: 06 41 52 4F 55 4E 44 0B   ; AROUND   0B
3EFD: 02 4F 4E 0C               ; ON       0C
3F01: 00
``` 

```code
3F02: FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
3F10: DF FF DF FF 80 40 0D 00 03 4B 89 2C 00 87 55 00 
3F20: 00
```

# Disk Loader

There is a disk version of the program here:

https://colorcomputerarchive.com/repo/Disks/Games/

The disk loads to memory at a different starting address and includes a small snippet of code on the end
to relocate it. Here is that relocation:

```
RelocateFromDisk:
5F21: 4F            CLRA                       ; Turn the ...
5F22: B7 FF 40      STA   $FF40                ; ... disk drive off
5F25: 86 34         LDA   #$0D                 ; Disable ...
5F27: B7 FF 03      STA   $FF03                ; .. interrupts
;
5F2A: 8E 04 00      LDX   #$0400               ; Clear ...
5F2D: 86 80         LDA   #$80                 ; ... the ...
5F2F: A7 80         STA   ,X+                  ; ... entire ...
5F31: 8C 06 00      CMPX  #$0600               ; ... text ...
5F34: 2D F9         BLT   $5F2F                ; ... screen
;
5F36: 8E 26 00      LDX   #$2600               ; Start of program loaded from disk
5F39: 10 8E 06 00   LDY   #$0600               ; This is where the program originally lived
5F3D: A6 80         LDA   ,X+                  ; Copy the ...
5F3F: A7 A0         STA   ,Y+                  ; ... program to ...
5F41: 8C 5F 20      CMPX  #$5F21               ; ... its original ...
5F44: 2D F7         BLT   $5F3D                ; ... location
5F46: 0F 71         CLR   <$71                 ; Clear the "warm restart flag" (reset will now perform a cold boot)
5F48: 7E 06 00      JMP   $0600                ; Run the program at its original location
```
