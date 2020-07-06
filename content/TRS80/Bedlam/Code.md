![TRS-80 Bedlam](trs80bedlam.jpg)

# Bedlam

>>> cpu Z80

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

# Start

```code
4300: 31 10 7E       LD      SP,$7E10        
4303: 21 00 3C       LD      HL,$3C00        
4306: 11 00 04       LD      DE,$0400        
4309: 36 20          LD      (HL),$20        
430B: 23             INC     HL              
430C: 1B             DEC     DE              
430D: 7A             LD      A,D             
430E: B3             OR      E               
430F: C2 09 43       JP      NZ,$4309        
4312: 21 C0 3F       LD      HL,$3FC0        
4315: 22 20 40       LD      ($4020),HL      
4318: 3E 13          LD      A,$13           
431A: 32 7E 4F       LD      ($4F7E),A       
431D: 21 C7 4F       LD      HL,$4FC7        
4320: CD E4 48       CALL    $48E4           
4323: 3E 0D          LD      A,$0D           
4325: CD 6B 4E       CALL    $4E6B           
4328: CD 26 48       CALL    $4826           
432B: 21 C6 4F       LD      HL,$4FC6        
432E: CD E4 48       CALL    $48E4           
4331: 3E 0D          LD      A,$0D           
4333: CD 6B 4E       CALL    $4E6B           
```

# Main Loop

```code
MainLoop: 
4336: 31 10 7E       LD      SP,$7E10        
4339: CD DF 47       CALL    $47DF           
433C: 97             SUB     A               
433D: 32 63 4F       LD      ($4F63),A       
4340: 32 66 4F       LD      ($4F66),A       
4343: 32 68 4F       LD      ($4F68),A       
4346: 32 5E 4F       LD      ($4F5E),A       
4349: 32 5F 4F       LD      ($4F5F),A       
434C: 32 65 4F       LD      ($4F65),A       
434F: 32 64 4F       LD      ($4F64),A       
4352: 32 60 4F       LD      ($4F60),A       
4355: 32 61 4F       LD      ($4F61),A       
4358: 32 6B 4F       LD      ($4F6B),A       
435B: 32 6F 4F       LD      ($4F6F),A       
435E: 32 75 4F       LD      ($4F75),A       
4361: 3E 13          LD      A,$13           ; Player object ...
4363: 32 7E 4F       LD      ($4F7E),A       ; ... is active object number
4366: 47             LD      B,A             
4367: CD E1 4D       CALL    $4DE1           
436A: 22 7F 4F       LD      ($4F7F),HL      
436D: CD 55 47       CALL    $4755           
4370: 7E             LD      A,(HL)          
4371: 32 81 4F       LD      ($4F81),A       
4374: 47             LD      B,A             
4375: 21 01 6A       LD      HL,$6A01        
4378: CD 3D 47       CALL    $473D           
437B: 22 82 4F       LD      ($4F82),HL      
437E: 21 A7 4F       LD      HL,$4FA7        
4381: 22 84 4F       LD      ($4F84),HL      
4384: 36 00          LD      (HL),$00        
4386: 21 C0 3F       LD      HL,$3FC0        
4389: CD 32 48       CALL    $4832           
438C: CA 9F 43       JP      Z,$439F         
438F: 7E             LD      A,(HL)          
4390: FE 20          CP      $20             
4392: CA 89 43       JP      Z,$4389         
4395: 7D             LD      A,L             
4396: FE FF          CP      $FF             
4398: CA 9F 43       JP      Z,$439F         
439B: 23             INC     HL              
439C: C3 8F 43       JP      $438F           
439F: 7D             LD      A,L             
43A0: FE FF          CP      $FF             
43A2: C2 89 43       JP      NZ,$4389        
43A5: 2A 84 4F       LD      HL,($4F84)      
43A8: 36 00          LD      (HL),$00        
43AA: 21 A7 4F       LD      HL,$4FA7        
43AD: 7E             LD      A,(HL)          
43AE: A7             AND     A               
43AF: CA 4F 44       JP      Z,$444F         
43B2: FE 02          CP      $02             
43B4: C2 C5 43       JP      NZ,$43C5        
43B7: 23             INC     HL              
43B8: 7E             LD      A,(HL)          
43B9: 2B             DEC     HL              
43BA: FE 09          CP      $09             
43BC: D2 C5 43       JP      NC,$43C5        
43BF: 32 64 4F       LD      ($4F64),A       
43C2: 23             INC     HL              
43C3: 23             INC     HL              
43C4: 23             INC     HL              
43C5: 7E             LD      A,(HL)          
43C6: 23             INC     HL              
43C7: A7             AND     A               
43C8: CA 4F 44       JP      Z,$444F         
43CB: 46             LD      B,(HL)          
43CC: 23             INC     HL              
43CD: 4E             LD      C,(HL)          
43CE: 23             INC     HL              
43CF: E5             PUSH    HL              
43D0: 3D             DEC     A               
43D1: C2 F8 43       JP      NZ,$43F8        
```

I believe the goal here was to allow multiple verbs given on an input line
to be translated to a single verb. The code finds a replacement list for the
newly given verb and then runs the list two bytes at a time comparing one
of the entries to the last given verb and storing the second byte if there
is a match. I believe that is what is SUPPOSED to happen, but I believe the
code has a bug or two. It actually does nothing at all. The replacement
list for BEDLAM and RAAKATU is empty so the code is never used anyway.

```code
43D4: 21 23 50       LD      HL,$5023        
43D7: CD 3D 47       CALL    $473D           
43DA: D2 F1 43       JP      NC,$43F1        
43DD: CD 55 47       CALL    $4755           
43E0: CD 69 47       CALL    $4769           
43E3: D2 F1 43       JP      NC,$43F1        
43E6: 3A 5F 4F       LD      A,($4F5F)       
43E9: BE             CP      (HL)            
43EA: 23             INC     HL              
43EB: 7E             LD      A,(HL)          
43EC: 23             INC     HL              
43ED: C2 E0 43       JP      NZ,$43E0        
43F0: 47             LD      B,A             
43F1: 78             LD      A,B             
43F2: 32 5F 4F       LD      ($4F5F),A       
43F5: C3 4B 44       JP      $444B           

43F8: 3D             DEC     A               
43F9: C2 35 44       JP      NZ,$4435        
43FC: 3A 61 4F       LD      A,($4F61)       
43FF: A7             AND     A               
4400: CA 23 44       JP      Z,$4423         
4403: 21 75 4F       LD      HL,$4F75        
4406: 70             LD      (HL),B          
4407: 23             INC     HL              
4408: 3A 63 4F       LD      A,($4F63)       
440B: 77             LD      (HL),A          
440C: 23             INC     HL              
440D: 3A 66 4F       LD      A,($4F66)       
4410: 77             LD      (HL),A          
4411: A7             AND     A               
4412: C2 16 44       JP      NZ,$4416        
4415: 71             LD      (HL),C          
4416: 97             SUB     A               
4417: 32 63 4F       LD      ($4F63),A       
441A: 32 61 4F       LD      ($4F61),A       
441D: 32 66 4F       LD      ($4F66),A       
4420: C3 4B 44       JP      $444B           

4423: 2A 6F 4F       LD      HL,($4F6F)      
4426: 22 75 4F       LD      ($4F75),HL      
4429: 3A 71 4F       LD      A,($4F71)       
442C: 32 77 4F       LD      ($4F77),A       
442F: 21 6F 4F       LD      HL,$4F6F        
4432: C3 06 44       JP      $4406           

4435: 3D             DEC     A               
4436: C2 44 44       JP      NZ,$4444        
4439: 78             LD      A,B             
443A: 32 63 4F       LD      ($4F63),A       
443D: 79             LD      A,C             
443E: 32 66 4F       LD      ($4F66),A       
4441: C3 4B 44       JP      $444B           
4444: 78             LD      A,B             
4445: 32 60 4F       LD      ($4F60),A       
4448: 32 61 4F       LD      ($4F61),A       
444B: E1             POP     HL              
444C: C3 C5 43       JP      $43C5           
444F: 3A 5F 4F       LD      A,($4F5F)       
4452: A7             AND     A               
4453: CA D5 46       JP      Z,$46D5         
4456: 21 75 4F       LD      HL,$4F75        
4459: CD 7D 45       CALL    $457D           
445C: 22 78 4F       LD      ($4F78),HL      
445F: 21 6F 4F       LD      HL,$4F6F        
4462: CD 7D 45       CALL    $457D           
4465: 22 72 4F       LD      ($4F72),HL      
4468: 97             SUB     A               
4469: 32 61 4F       LD      ($4F61),A       
446C: 2A 72 4F       LD      HL,($4F72)      
446F: 3A 6F 4F       LD      A,($4F6F)       
4472: A7             AND     A               
4473: CA 7C 44       JP      Z,$447C         
4476: CD 55 47       CALL    $4755           
4479: 23             INC     HL              
447A: 23             INC     HL              
447B: 7E             LD      A,(HL)          
447C: 32 74 4F       LD      ($4F74),A       
447F: 2A 78 4F       LD      HL,($4F78)      
4482: 3A 75 4F       LD      A,($4F75)       
4485: A7             AND     A               
4486: CA 8F 44       JP      Z,$448F         
4489: CD 55 47       CALL    $4755           
448C: 23             INC     HL              
448D: 23             INC     HL              
448E: 7E             LD      A,(HL)          
448F: 32 7A 4F       LD      ($4F7A),A       
4492: 21 25 50       LD      HL,$5025        
4495: 7E             LD      A,(HL)          
4496: A7             AND     A               
4497: CA 8B 46       JP      Z,$468B         
449A: 3A 5F 4F       LD      A,($4F5F)       
449D: BE             CP      (HL)            
449E: 23             INC     HL              
449F: C2 01 45       JP      NZ,$4501        
44A2: 7E             LD      A,(HL)          
44A3: 32 62 4F       LD      ($4F62),A       
44A6: 3A 60 4F       LD      A,($4F60)       
44A9: A7             AND     A               
44AA: CA B1 44       JP      Z,$44B1         
44AD: BE             CP      (HL)            
44AE: C2 01 45       JP      NZ,$4501        
44B1: 23             INC     HL              
44B2: 7E             LD      A,(HL)          
44B3: A7             AND     A               
44B4: CA CD 44       JP      Z,$44CD         
44B7: 3A 6F 4F       LD      A,($4F6F)       
44BA: A7             AND     A               
44BB: C2 D4 44       JP      NZ,$44D4        
44BE: 3A 68 4F       LD      A,($4F68)       
44C1: 32 69 4F       LD      ($4F69),A       
44C4: 11 6F 4F       LD      DE,$4F6F        
44C7: CD 1B 46       CALL    $461B           
44CA: C3 D4 44       JP      $44D4           
44CD: 3A 6F 4F       LD      A,($4F6F)       
44D0: A7             AND     A               
44D1: C2 02 45       JP      NZ,$4502        
44D4: 23             INC     HL              
44D5: 7E             LD      A,(HL)          
44D6: A7             AND     A               
44D7: CA F5 44       JP      Z,$44F5         
44DA: 3A 75 4F       LD      A,($4F75)       
44DD: A7             AND     A               
44DE: C2 FC 44       JP      NZ,$44FC        
44E1: 3A 67 4F       LD      A,($4F67)       
44E4: 32 69 4F       LD      ($4F69),A       
44E7: 3E 01          LD      A,$01           
44E9: 32 61 4F       LD      ($4F61),A       
44EC: 11 75 4F       LD      DE,$4F75        
44EF: CD 1B 46       CALL    $461B           
44F2: C3 FC 44       JP      $44FC           
44F5: 3A 75 4F       LD      A,($4F75)       
44F8: A7             AND     A               
44F9: C2 03 45       JP      NZ,$4503        
44FC: 23             INC     HL              
44FD: 7E             LD      A,(HL)          
44FE: C3 08 45       JP      $4508           
4501: 23             INC     HL              
4502: 23             INC     HL              
4503: 23             INC     HL              
4504: 23             INC     HL              
4505: C3 95 44       JP      $4495           
4508: 32 7D 4F       LD      ($4F7D),A       
450B: 21 FF 3F       LD      HL,$3FFF        
450E: 22 20 40       LD      ($4020),HL      
4511: 3A 6F 4F       LD      A,($4F6F)       
4514: A7             AND     A               
4515: C2 24 45       JP      NZ,$4524        
4518: 2A 78 4F       LD      HL,($4F78)      
451B: 22 72 4F       LD      ($4F72),HL      
451E: 3A 75 4F       LD      A,($4F75)       
4521: 32 6F 4F       LD      ($4F6F),A       
4524: 3A 64 4F       LD      A,($4F64)       
4527: A7             AND     A               
4528: CA 61 45       JP      Z,$4561         
452B: 21 A8 4F       LD      HL,$4FA8        
452E: 7E             LD      A,(HL)          
452F: 36 00          LD      (HL),$00        
4531: 2B             DEC     HL              
4532: 77             LD      (HL),A          
4533: CD 7D 45       CALL    $457D           
4536: 32 7E 4F       LD      ($4F7E),A       
4539: 22 7F 4F       LD      ($4F7F),HL      
453C: 3E 0D          LD      A,$0D           
453E: CD 6B 4E       CALL    $4E6B           
4541: CD 55 47       CALL    $4755           
4544: 23             INC     HL              
4545: 23             INC     HL              
4546: 23             INC     HL              
4547: 06 0B          LD      B,$0B           
4549: CD 41 47       CALL    $4741           
454C: DA 58 45       JP      C,$4558         
454F: 21 33 52       LD      HL,$5233        
4552: CD E4 48       CALL    $48E4           
4555: C3 6F 45       JP      $456F           
4558: CD 55 47       CALL    $4755           
455B: CD E4 48       CALL    $48E4           
455E: C3 6F 45       JP      $456F           
4561: 3E 0D          LD      A,$0D           
4563: CD 6B 4E       CALL    $4E6B           
4566: 21 A2 6F       LD      HL,$6FA2        
4569: CD 55 47       CALL    $4755           
456C: CD E4 48       CALL    $48E4           
456F: CD C5 4C       CALL    $4CC5           
4572: 3E 0D          LD      A,$0D           
4574: CD 6B 4E       CALL    $4E6B           
4577: 3A 7D 4F       LD      A,($4F7D)       
457A: C3 36 43       JP      $4336           
457D: 97             SUB     A               
457E: 32 6B 4F       LD      ($4F6B),A       
4581: 7E             LD      A,(HL)          
4582: 32 5E 4F       LD      ($4F5E),A       
4585: 47             LD      B,A             
4586: A7             AND     A               
4587: C8             RET     Z               
4588: 23             INC     HL              
4589: 7E             LD      A,(HL)          
458A: 32 63 4F       LD      ($4F63),A       
458D: 23             INC     HL              
458E: 7E             LD      A,(HL)          
458F: 32 7B 4F       LD      ($4F7B),A       
4592: 21 61 55       LD      HL,$5561        
4595: CD 3D 47       CALL    $473D           
4598: D2 EA 45       JP      NC,$45EA        
459B: D5             PUSH    DE              
459C: E5             PUSH    HL              
459D: CD F9 45       CALL    $45F9           
45A0: C2 F5 45       JP      NZ,$45F5        
45A3: 3A 63 4F       LD      A,($4F63)       
45A6: A7             AND     A               
45A7: CA CC 45       JP      Z,$45CC         
45AA: E1             POP     HL              
45AB: E5             PUSH    HL              
45AC: CD 55 47       CALL    $4755           
45AF: 01 03 00       LD      BC,$0003        
45B2: 09             ADD     HL,BC           
45B3: 06 01          LD      B,$01           
45B5: CD 41 47       CALL    $4741           
45B8: D2 CC 45       JP      NC,$45CC        
45BB: CD 55 47       CALL    $4755           
45BE: CD 69 47       CALL    $4769           
45C1: D2 F5 45       JP      NC,$45F5        
45C4: 3A 63 4F       LD      A,($4F63)       
45C7: BE             CP      (HL)            
45C8: 23             INC     HL              
45C9: C2 BE 45       JP      NZ,$45BE        
45CC: E1             POP     HL              
45CD: 3A 6B 4F       LD      A,($4F6B)       
45D0: A7             AND     A               
45D1: C2 CC 46       JP      NZ,$46CC        
45D4: 7E             LD      A,(HL)          
45D5: 32 6B 4F       LD      ($4F6B),A       
45D8: 22 6C 4F       LD      ($4F6C),HL      
45DB: CD 55 47       CALL    $4755           
45DE: EB             EX      DE,HL           
45DF: D1             POP     DE              
45E0: 3A 5E 4F       LD      A,($4F5E)       
45E3: 47             LD      B,A             
45E4: CD 41 47       CALL    $4741           
45E7: DA 9B 45       JP      C,$459B         
45EA: 3A 6B 4F       LD      A,($4F6B)       
45ED: 2A 6C 4F       LD      HL,($4F6C)      
45F0: A7             AND     A               
45F1: C0             RET     NZ              
45F2: C3 82 46       JP      $4682           
45F5: E1             POP     HL              
45F6: C3 DB 45       JP      $45DB           
45F9: CD 55 47       CALL    $4755           
45FC: 3A 81 4F       LD      A,($4F81)       
45FF: BE             CP      (HL)            
4600: C8             RET     Z               
4601: 7E             LD      A,(HL)          
4602: A7             AND     A               
4603: CA 18 46       JP      Z,$4618         
4606: 3C             INC     A               
4607: C8             RET     Z               
4608: 3D             DEC     A               
4609: FA 18 46       JP      M,$4618         
460C: 46             LD      B,(HL)          
460D: 3A 7E 4F       LD      A,($4F7E)       
4610: B8             CP      B               
4611: C8             RET     Z               
4612: CD E1 4D       CALL    $4DE1           
4615: C3 F9 45       JP      $45F9           
4618: F6 01          OR      $01             
461A: C9             RET                     
461B: E5             PUSH    HL              
461C: 97             SUB     A               
461D: 32 5E 4F       LD      ($4F5E),A       
4620: D5             PUSH    DE              
4621: 4E             LD      C,(HL)          
4622: 21 61 55       LD      HL,$5561        
4625: CD 55 47       CALL    $4755           
4628: CD 69 47       CALL    $4769           
462B: D2 66 46       JP      NC,$4666        
462E: D5             PUSH    DE              
462F: E5             PUSH    HL              
4630: CD F9 45       CALL    $45F9           
4633: E1             POP     HL              
4634: C2 60 46       JP      NZ,$4660        
4637: 46             LD      B,(HL)          
4638: 22 84 4F       LD      ($4F84),HL      
463B: CD 55 47       CALL    $4755           
463E: 23             INC     HL              
463F: 23             INC     HL              
4640: 7E             LD      A,(HL)          
4641: A1             AND     C               
4642: B9             CP      C               
4643: C2 5B 46       JP      NZ,$465B        
4646: 3A 5E 4F       LD      A,($4F5E)       
4649: A7             AND     A               
464A: C2 94 46       JP      NZ,$4694        
464D: 78             LD      A,B             
464E: 32 5E 4F       LD      ($4F5E),A       
4651: 7E             LD      A,(HL)          
4652: 32 63 4F       LD      ($4F63),A       
4655: 2A 84 4F       LD      HL,($4F84)      
4658: 22 86 4F       LD      ($4F86),HL      
465B: EB             EX      DE,HL           
465C: D1             POP     DE              
465D: C3 28 46       JP      $4628           
4660: CD 55 47       CALL    $4755           
4663: C3 5B 46       JP      $465B           
4666: 3A 5E 4F       LD      A,($4F5E)       
4669: A7             AND     A               
466A: CA 94 46       JP      Z,$4694         
466D: D1             POP     DE              
466E: 2A 86 4F       LD      HL,($4F86)      
4671: 12             LD      (DE),A          
4672: 13             INC     DE              
4673: 13             INC     DE              
4674: 13             INC     DE              
4675: 7D             LD      A,L             
4676: 12             LD      (DE),A          
4677: 13             INC     DE              
4678: 7C             LD      A,H             
4679: 12             LD      (DE),A          
467A: 13             INC     DE              
467B: 3A 63 4F       LD      A,($4F63)       
467E: 12             LD      (DE),A          
467F: E1             POP     HL              
4680: 97             SUB     A               
4681: C9             RET                     
4682: 11 8F 4F       LD      DE,$4F8F        
4685: 3A 7B 4F       LD      A,($4F7B)       
4688: C3 DA 46       JP      $46DA           
468B: 11 9E 4F       LD      DE,$4F9E        
468E: 3A 67 4F       LD      A,($4F67)       
4691: C3 DA 46       JP      $46DA           
4694: 3A 61 4F       LD      A,($4F61)       
4697: A7             AND     A               
4698: CA C3 46       JP      Z,$46C3         
469B: 3A 60 4F       LD      A,($4F60)       
469E: A7             AND     A               
469F: C2 C3 46       JP      NZ,$46C3        
46A2: 16 00          LD      D,$00           
46A4: 21 01 55       LD      HL,$5501        
46A7: 7E             LD      A,(HL)          
46A8: A7             AND     A               
46A9: CA C3 46       JP      Z,$46C3         
46AC: E5             PUSH    HL              
46AD: 5E             LD      E,(HL)          
46AE: 23             INC     HL              
46AF: 19             ADD     HL,DE           
46B0: 3A 62 4F       LD      A,($4F62)       
46B3: BE             CP      (HL)            
46B4: CA BC 46       JP      Z,$46BC         
46B7: 23             INC     HL              
46B8: C1             POP     BC              
46B9: C3 A7 46       JP      $46A7           
46BC: D1             POP     DE              
46BD: 3A 69 4F       LD      A,($4F69)       
46C0: CD 16 47       CALL    $4716           
46C3: 11 8F 4F       LD      DE,$4F8F        
46C6: 3A 69 4F       LD      A,($4F69)       
46C9: C3 DA 46       JP      $46DA           
46CC: 11 96 4F       LD      DE,$4F96        
46CF: 3A 7B 4F       LD      A,($4F7B)       
46D2: C3 DA 46       JP      $46DA           
46D5: 11 88 4F       LD      DE,$4F88        
46D8: 3E C0          LD      A,$C0           
46DA: 31 10 7E       LD      SP,$7E10        
46DD: 21 C0 3F       LD      HL,$3FC0        
46E0: CD 16 47       CALL    $4716           
46E3: 1A             LD      A,(DE)          
46E4: 4F             LD      C,A             
46E5: E5             PUSH    HL              
46E6: 36 20          LD      (HL),$20        
46E8: 23             INC     HL              
46E9: 0D             DEC     C               
46EA: C2 E6 46       JP      NZ,$46E6        
46ED: CD 0B 47       CALL    $470B           
46F0: E1             POP     HL              
46F1: 05             DEC     B               
46F2: C2 05 47       JP      NZ,$4705        
46F5: 1A             LD      A,(DE)          
46F6: 3C             INC     A               
46F7: 4F             LD      C,A             
46F8: CD EE 47       CALL    $47EE           
46FB: 0D             DEC     C               
46FC: C2 F8 46       JP      NZ,$46F8        
46FF: CD 72 47       CALL    $4772           
4702: C3 3C 43       JP      $433C           
4705: CD 25 47       CALL    $4725           
4708: C3 E3 46       JP      $46E3           
470B: 3E 32          LD      A,$32           
470D: 0D             DEC     C               
470E: C2 0D 47       JP      NZ,$470D        
4711: 3D             DEC     A               
4712: C2 0D 47       JP      NZ,$470D        
4715: C9             RET                     
4716: 6F             LD      L,A             
4717: 1A             LD      A,(DE)          
4718: 3C             INC     A               
4719: 4F             LD      C,A             
471A: D5             PUSH    DE              
471B: CD 05 48       CALL    $4805           
471E: 0D             DEC     C               
471F: C2 1B 47       JP      NZ,$471B        
4722: D1             POP     DE              
4723: 06 08          LD      B,$08           
4725: 1A             LD      A,(DE)          
4726: 4F             LD      C,A             
4727: D5             PUSH    DE              
4728: E5             PUSH    HL              
4729: 13             INC     DE              
472A: 1A             LD      A,(DE)          
472B: 77             LD      (HL),A          
472C: 23             INC     HL              
472D: 13             INC     DE              
472E: 0D             DEC     C               
472F: C2 2A 47       JP      NZ,$472A        
4732: 2C             INC     L               
4733: 7D             LD      A,L             
4734: 32 69 4F       LD      ($4F69),A       
4737: CD 0B 47       CALL    $470B           
473A: E1             POP     HL              
473B: D1             POP     DE              
473C: C9             RET                     
473D: 23             INC     HL              
473E: CD 56 47       CALL    $4756           
4741: CD 69 47       CALL    $4769           
4744: D0             RET     NC              
4745: 78             LD      A,B             
4746: BE             CP      (HL)            
4747: CA 53 47       JP      Z,$4753         
474A: D5             PUSH    DE              
474B: CD 55 47       CALL    $4755           
474E: EB             EX      DE,HL           
474F: D1             POP     DE              
4750: C3 41 47       JP      $4741           
4753: 37             SCF                     
4754: C9             RET                     
4755: 23             INC     HL              
4756: 16 00          LD      D,$00           
4758: 7E             LD      A,(HL)          
4759: E6 80          AND     $80             
475B: CA 63 47       JP      Z,$4763         
475E: 7E             LD      A,(HL)          
475F: E6 7F          AND     $7F             
4761: 57             LD      D,A             
4762: 23             INC     HL              
4763: 5E             LD      E,(HL)          
4764: 23             INC     HL              
4765: EB             EX      DE,HL           
4766: 19             ADD     HL,DE           
4767: EB             EX      DE,HL           
4768: C9             RET                     
4769: 7C             LD      A,H             
476A: BA             CP      D               
476B: C0             RET     NZ              
476C: 7D             LD      A,L             
476D: BB             CP      E               
476E: C9             RET                     
476F: 21 C0 3F       LD      HL,$3FC0        
4772: CD 20 48       CALL    $4820           
4775: CD 26 48       CALL    $4826           
4778: FE 18          CP      $18             
477A: CA A6 47       JP      Z,$47A6         
477D: FE 19          CP      $19             
477F: CA B6 47       JP      Z,$47B6         
4782: FE 09          CP      $09             
4784: CA C6 47       JP      Z,$47C6         
4787: FE 0D          CP      $0D             
4789: CA DB 47       JP      Z,$47DB         
478C: FE 1F          CP      $1F             
478E: CA DF 47       JP      Z,$47DF         
4791: FE 08          CP      $08             
4793: CA CE 47       JP      Z,$47CE         
4796: 47             LD      B,A             
4797: 7D             LD      A,L             
4798: FE FF          CP      $FF             
479A: CA 75 47       JP      Z,$4775         
479D: 78             LD      A,B             
479E: CD 05 48       CALL    $4805           
47A1: 77             LD      (HL),A          
47A2: 23             INC     HL              
47A3: C3 75 47       JP      $4775           
47A6: 7D             LD      A,L             
47A7: FE C0          CP      $C0             
47A9: CA 75 47       JP      Z,$4775         
47AC: 2B             DEC     HL              
47AD: 7E             LD      A,(HL)          
47AE: 23             INC     HL              
47AF: 77             LD      (HL),A          
47B0: 2B             DEC     HL              
47B1: 36 8F          LD      (HL),$8F        
47B3: C3 75 47       JP      $4775           
47B6: 7D             LD      A,L             
47B7: FE FF          CP      $FF             
47B9: CA 75 47       JP      Z,$4775         
47BC: 23             INC     HL              
47BD: 7E             LD      A,(HL)          
47BE: 2B             DEC     HL              
47BF: 77             LD      (HL),A          
47C0: 23             INC     HL              
47C1: 36 8F          LD      (HL),$8F        
47C3: C3 75 47       JP      $4775           
47C6: CD EE 47       CALL    $47EE           
47C9: 36 8F          LD      (HL),$8F        
47CB: C3 75 47       JP      $4775           
47CE: 7D             LD      A,L             
47CF: FE C0          CP      $C0             
47D1: CA 75 47       JP      Z,$4775         
47D4: 2B             DEC     HL              
47D5: CD EE 47       CALL    $47EE           
47D8: C3 75 47       JP      $4775           
47DB: CD EE 47       CALL    $47EE           
47DE: C9             RET                     
47DF: 21 C0 3F       LD      HL,$3FC0        
47E2: 06 40          LD      B,$40           
47E4: 36 20          LD      (HL),$20        
47E6: 23             INC     HL              
47E7: 05             DEC     B               
47E8: C2 E4 47       JP      NZ,$47E4        
47EB: C3 6F 47       JP      $476F           
47EE: 54             LD      D,H             
47EF: 5D             LD      E,L             
47F0: 45             LD      B,L             
47F1: 36 20          LD      (HL),$20        
47F3: 13             INC     DE              
47F4: 7B             LD      A,E             
47F5: A7             AND     A               
47F6: C8             RET     Z               
47F7: FE 01          CP      $01             
47F9: C8             RET     Z               
47FA: 1A             LD      A,(DE)          
47FB: 77             LD      (HL),A          
47FC: 2C             INC     L               
47FD: 1C             INC     E               
47FE: C2 FA 47       JP      NZ,$47FA        
4801: 36 20          LD      (HL),$20        
4803: 68             LD      L,B             
4804: C9             RET                     
4805: F5             PUSH    AF              
4806: 7D             LD      A,L             
4807: FE FF          CP      $FF             
4809: CA 1E 48       JP      Z,$481E         
480C: 45             LD      B,L             
480D: 21 FF 3F       LD      HL,$3FFF        
4810: 11 FE 3F       LD      DE,$3FFE        
4813: 1A             LD      A,(DE)          
4814: 77             LD      (HL),A          
4815: 2B             DEC     HL              
4816: 1B             DEC     DE              
4817: 7D             LD      A,L             
4818: B8             CP      B               
4819: C2 13 48       JP      NZ,$4813        
481C: 36 20          LD      (HL),$20        
481E: F1             POP     AF              
481F: C9             RET                     
4820: CD 05 48       CALL    $4805           
4823: 36 8F          LD      (HL),$8F        
4825: C9             RET                     
4826: CD 31 4F       CALL    $4F31           
4829: CD 2B 00       CALL    $002B           
482C: A7             AND     A               
482D: CA 26 48       JP      Z,$4826         
4830: C9             RET                     
4831: 23             INC     HL              
4832: 7D             LD      A,L             
4833: 32 7B 4F       LD      ($4F7B),A       
4836: FE FF          CP      $FF             
4838: C8             RET     Z               
4839: 7E             LD      A,(HL)          
483A: FE 20          CP      $20             
483C: CA 31 48       JP      Z,$4831         
483F: FE 41          CP      $41             
4841: DA 31 48       JP      C,$4831         
4844: 11 34 52       LD      DE,$5234        
4847: CD 7E 48       CALL    $487E           
484A: CA 32 48       JP      Z,$4832         
484D: 06 01          LD      B,$01           
484F: 13             INC     DE              
4850: CD 7E 48       CALL    $487E           
4853: CA 5F 48       JP      Z,$485F         
4856: 04             INC     B               
4857: 78             LD      A,B             
4858: FE 05          CP      $05             
485A: C2 4F 48       JP      NZ,$484F        
485D: A7             AND     A               
485E: C9             RET                     
485F: EB             EX      DE,HL           
4860: 2A 84 4F       LD      HL,($4F84)      
4863: 70             LD      (HL),B          
4864: 23             INC     HL              
4865: 77             LD      (HL),A          
4866: 23             INC     HL              
4867: 3A 7B 4F       LD      A,($4F7B)       
486A: 77             LD      (HL),A          
486B: 23             INC     HL              
486C: 22 84 4F       LD      ($4F84),HL      
486F: EB             EX      DE,HL           
4870: 78             LD      A,B             
4871: FE 01          CP      $01             
4873: C2 7C 48       JP      NZ,$487C        
4876: 3A 67 4F       LD      A,($4F67)       
4879: 32 68 4F       LD      ($4F68),A       
487C: 97             SUB     A               
487D: C9             RET                     
487E: 1A             LD      A,(DE)          
487F: A7             AND     A               
4880: C2 86 48       JP      NZ,$4886        
4883: F6 01          OR      $01             
4885: C9             RET                     
4886: 4F             LD      C,A             
4887: 32 7C 4F       LD      ($4F7C),A       
488A: E5             PUSH    HL              
488B: 13             INC     DE              
488C: 7E             LD      A,(HL)          
488D: FE 20          CP      $20             
488F: CA DA 48       JP      Z,$48DA         
4892: 7D             LD      A,L             
4893: A7             AND     A               
4894: CA DA 48       JP      Z,$48DA         
4897: 7E             LD      A,(HL)          
4898: FE 41          CP      $41             
489A: D2 A1 48       JP      NC,$48A1        
489D: 23             INC     HL              
489E: C3 8C 48       JP      $488C           
48A1: 1A             LD      A,(DE)          
48A2: BE             CP      (HL)            
48A3: C2 DA 48       JP      NZ,$48DA        
48A6: 13             INC     DE              
48A7: 23             INC     HL              
48A8: 0D             DEC     C               
48A9: C2 8C 48       JP      NZ,$488C        
48AC: 3A 7C 4F       LD      A,($4F7C)       
48AF: FE 06          CP      $06             
48B1: CA BF 48       JP      Z,$48BF         
48B4: 7E             LD      A,(HL)          
48B5: FE 41          CP      $41             
48B7: DA BF 48       JP      C,$48BF         
48BA: FE 20          CP      $20             
48BC: C2 DF 48       JP      NZ,$48DF        
48BF: 1A             LD      A,(DE)          
48C0: D1             POP     DE              
48C1: 4F             LD      C,A             
48C2: 7E             LD      A,(HL)          
48C3: FE 20          CP      $20             
48C5: CA D2 48       JP      Z,$48D2         
48C8: 7D             LD      A,L             
48C9: FE FF          CP      $FF             
48CB: CA D4 48       JP      Z,$48D4         
48CE: 23             INC     HL              
48CF: C3 C2 48       JP      $48C2           
48D2: 7D             LD      A,L             
48D3: 3C             INC     A               
48D4: 32 67 4F       LD      ($4F67),A       
48D7: 97             SUB     A               
48D8: 79             LD      A,C             
48D9: C9             RET                     
48DA: 13             INC     DE              
48DB: 0D             DEC     C               
48DC: C2 DA 48       JP      NZ,$48DA        
48DF: E1             POP     HL              
48E0: 13             INC     DE              
48E1: C3 7E 48       JP      $487E           
48E4: 7E             LD      A,(HL)          
48E5: 47             LD      B,A             
48E6: 23             INC     HL              
48E7: E6 80          AND     $80             
48E9: CA 00 49       JP      Z,$4900         
48EC: E5             PUSH    HL              
48ED: D5             PUSH    DE              
48EE: 21 E5 75       LD      HL,$75E5        
48F1: CD 3D 47       CALL    $473D           
48F4: D2 FD 48       JP      NC,$48FD        
48F7: CD 55 47       CALL    $4755           
48FA: CD E4 48       CALL    $48E4           
48FD: D1             POP     DE              
48FE: E1             POP     HL              
48FF: C9             RET                     
4900: 78             LD      A,B             
4901: 11 C8 4F       LD      DE,$4FC8        
4904: 07             RLCA                    
4905: 83             ADD     A,E             
4906: 5F             LD      E,A             
4907: 7A             LD      A,D             
4908: CE 00          ADC     $00             
490A: 57             LD      D,A             
490B: 1A             LD      A,(DE)          
490C: 32 15 49       LD      ($4915),A       
490F: 13             INC     DE              
4910: 1A             LD      A,(DE)          
4911: 32 16 49       LD      ($4916),A       
4914: C3 14 49       JP      $4914  

Com_0D_while_pass:
; while_pass:         
4917: CD 56 47       CALL    $4756           
491A: CD 69 47       CALL    $4769           
491D: D2 2A 49       JP      NC,$492A        
4920: D5             PUSH    DE              
4921: CD E4 48       CALL    $48E4           
4924: D1             POP     DE              
4925: CA 1A 49       JP      Z,$491A         
4928: EB             EX      DE,HL           
4929: C9             RET                     
492A: EB             EX      DE,HL           
492B: 97             SUB     A               
492C: C9             RET                     
492D: CD 56 47       CALL    $4756           
4930: CD 69 47       CALL    $4769           
4933: D2 40 49       JP      NC,$4940        
4936: D5             PUSH    DE              
4937: CD E4 48       CALL    $48E4           
493A: D1             POP     DE              
493B: C2 30 49       JP      NZ,$4930        
493E: EB             EX      DE,HL           
493F: C9             RET                     
4940: EB             EX      DE,HL           
4941: F6 01          OR      $01             
4943: C9             RET                     
4944: CD 56 47       CALL    $4756           
4947: 46             LD      B,(HL)          
4948: 23             INC     HL              
4949: CD 69 47       CALL    $4769           
494C: D2 40 49       JP      NC,$4940        
494F: D5             PUSH    DE              
4950: C5             PUSH    BC              
4951: 78             LD      A,B             
4952: CD 01 49       CALL    $4901           
4955: C1             POP     BC              
4956: CA 61 49       JP      Z,$4961         
4959: CD 56 47       CALL    $4756           
495C: EB             EX      DE,HL           
495D: D1             POP     DE              
495E: C3 49 49       JP      $4949           
4961: CD 56 47       CALL    $4756           
4964: CD E4 48       CALL    $48E4           
4967: E1             POP     HL              
4968: C9             RET                     

Com_00:
;
4969: CD 73 49       CALL    $4973           
496C: E5             PUSH    HL              
496D: CD 20 4A       CALL    $4A20           
4970: E1             POP     HL              
4971: 97             SUB     A               
4972: C9             RET            
         
4973: 7E             LD      A,(HL)          
4974: 23             INC     HL              
4975: E5             PUSH    HL              
4976: 32 81 4F       LD      ($4F81),A       
4979: 47             LD      B,A             
497A: 21 01 6A       LD      HL,$6A01        
497D: CD 3D 47       CALL    $473D           
4980: 22 82 4F       LD      ($4F82),HL      
4983: 2A 7F 4F       LD      HL,($4F7F)      
4986: CD 55 47       CALL    $4755           
4989: 3A 81 4F       LD      A,($4F81)       
498C: 77             LD      (HL),A          
498D: E1             POP     HL              
498E: 97             SUB     A               
498F: C9             RET                     
4990: E5             PUSH    HL              
4991: 2A 72 4F       LD      HL,($4F72)      
4994: 22 6C 4F       LD      ($4F6C),HL      
4997: 3A 6F 4F       LD      A,($4F6F)       
499A: 32 6B 4F       LD      ($4F6B),A       
499D: E1             POP     HL              
499E: 97             SUB     A               
499F: C9             RET                     
49A0: E5             PUSH    HL              
49A1: 2A 78 4F       LD      HL,($4F78)      
49A4: 22 6C 4F       LD      ($4F6C),HL      
49A7: 3A 75 4F       LD      A,($4F75)       
49AA: 32 6B 4F       LD      ($4F6B),A       
49AD: E1             POP     HL              
49AE: 97             SUB     A               
49AF: C9             RET                     
49B0: 46             LD      B,(HL)          
49B1: 23             INC     HL              
49B2: E5             PUSH    HL              
49B3: 78             LD      A,B             
49B4: 32 6B 4F       LD      ($4F6B),A       
49B7: CD E1 4D       CALL    $4DE1           
49BA: 22 6C 4F       LD      ($4F6C),HL      
49BD: E1             POP     HL              
49BE: 97             SUB     A               
49BF: C9             RET                     
49C0: EB             EX      DE,HL           
49C1: 2A 72 4F       LD      HL,($4F72)      
49C4: E5             PUSH    HL              
49C5: 2A 78 4F       LD      HL,($4F78)      
49C8: E5             PUSH    HL              
49C9: 3A 6F 4F       LD      A,($4F6F)       
49CC: 47             LD      B,A             
49CD: 3A 75 4F       LD      A,($4F75)       
49D0: 4F             LD      C,A             
49D1: C5             PUSH    BC              
49D2: 3A 7D 4F       LD      A,($4F7D)       
49D5: 47             LD      B,A             
49D6: C5             PUSH    BC              
49D7: EB             EX      DE,HL           
49D8: 7E             LD      A,(HL)          
49D9: 32 7D 4F       LD      ($4F7D),A       
49DC: 23             INC     HL              
49DD: 46             LD      B,(HL)          
49DE: 23             INC     HL              
49DF: 4E             LD      C,(HL)          
49E0: 23             INC     HL              
49E1: E5             PUSH    HL              
49E2: 78             LD      A,B             
49E3: 32 6F 4F       LD      ($4F6F),A       
49E6: A7             AND     A               
49E7: CA F0 49       JP      Z,$49F0         
49EA: CD E1 4D       CALL    $4DE1           
49ED: 22 72 4F       LD      ($4F72),HL      
49F0: 79             LD      A,C             
49F1: 32 75 4F       LD      ($4F75),A       
49F4: A7             AND     A               
49F5: CA FE 49       JP      Z,$49FE         
49F8: CD E1 4D       CALL    $4DE1           
49FB: 22 78 4F       LD      ($4F78),HL      
49FE: 21 A2 6F       LD      HL,$6FA2        
4A01: CD 55 47       CALL    $4755           
4A04: CD E4 48       CALL    $48E4           
4A07: D1             POP     DE              
4A08: C1             POP     BC              
4A09: 78             LD      A,B             
4A0A: 32 7D 4F       LD      ($4F7D),A       
4A0D: C1             POP     BC              
4A0E: 78             LD      A,B             
4A0F: 32 6F 4F       LD      ($4F6F),A       
4A12: 79             LD      A,C             
4A13: 32 75 4F       LD      ($4F75),A       
4A16: E1             POP     HL              
4A17: 22 78 4F       LD      ($4F78),HL      
4A1A: E1             POP     HL              
4A1B: 22 72 4F       LD      ($4F72),HL      
4A1E: EB             EX      DE,HL           
4A1F: C9             RET                     
4A20: 3A 7E 4F       LD      A,($4F7E)       
4A23: FE 38          CP      $38             
4A25: CA 2B 4A       JP      Z,$4A2B         
4A28: FE 13          CP      $13             
4A2A: C0             RET     NZ              
4A2B: 2A 82 4F       LD      HL,($4F82)      
4A2E: CD 55 47       CALL    $4755           
4A31: 23             INC     HL              
4A32: 06 03          LD      B,$03           
4A34: CD 41 47       CALL    $4741           
4A37: D2 56 4A       JP      NC,$4A56        
4A3A: 3A 7E 4F       LD      A,($4F7E)       
4A3D: FE 38          CP      $38             
4A3F: CA 4A 4A       JP      Z,$4A4A         
4A42: E5             PUSH    HL              
4A43: 21 AB 4A       LD      HL,$4AAB        
4A46: CD E4 48       CALL    $48E4           
4A49: E1             POP     HL              
4A4A: CD 55 47       CALL    $4755           
4A4D: CD E4 48       CALL    $48E4           
4A50: 3A 7E 4F       LD      A,($4F7E)       
4A53: FE 38          CP      $38             
4A55: C8             RET     Z               
4A56: 21 61 55       LD      HL,$5561        
4A59: CD 55 47       CALL    $4755           
4A5C: D5             PUSH    DE              
4A5D: CD 55 47       CALL    $4755           
4A60: 3A 81 4F       LD      A,($4F81)       
4A63: BE             CP      (HL)            
4A64: C2 A0 4A       JP      NZ,$4AA0        
4A67: 23             INC     HL              
4A68: 23             INC     HL              
4A69: 7E             LD      A,(HL)          
4A6A: F5             PUSH    AF              
4A6B: 23             INC     HL              
4A6C: 06 03          LD      B,$03           
4A6E: CD 41 47       CALL    $4741           
4A71: D2 9F 4A       JP      NC,$4A9F        
4A74: D5             PUSH    DE              
4A75: CD 55 47       CALL    $4755           
4A78: CD E4 48       CALL    $48E4           
4A7B: D1             POP     DE              
4A7C: F1             POP     AF              
4A7D: F5             PUSH    AF              
4A7E: E6 08          AND     $08             
4A80: CA 9F 4A       JP      Z,$4A9F         
4A83: F1             POP     AF              
4A84: F5             PUSH    AF              
4A85: E6 0A          AND     $0A             
4A87: EE 0A          XOR     $0A             
4A89: C2 97 4A       JP      NZ,$4A97        
4A8C: D5             PUSH    DE              
4A8D: 21 A9 4A       LD      HL,$4AA9        
4A90: CD E4 48       CALL    $48E4           
4A93: D1             POP     DE              
4A94: C3 9F 4A       JP      $4A9F           
4A97: D5             PUSH    DE              
4A98: 21 AA 4A       LD      HL,$4AAA        
4A9B: CD E4 48       CALL    $48E4           
4A9E: D1             POP     DE              
4A9F: F1             POP     AF              
4AA0: EB             EX      DE,HL           
4AA1: D1             POP     DE              
4AA2: CD 69 47       CALL    $4769           
4AA5: DA 5C 4A       JP      C,$4A5C         
4AA8: C9             RET                     
4AA9: 8A             ADC     A,D             
4AAA: 8B             ADC     A,E             
4AAB: 8C             ADC     A,H             
4AAC: 46             LD      B,(HL)          
4AAD: 23             INC     HL              
4AAE: E5             PUSH    HL              
4AAF: CD E1 4D       CALL    $4DE1           
4AB2: CD F9 45       CALL    $45F9           
4AB5: E1             POP     HL              
4AB6: C9             RET                     
4AB7: 3A 7E 4F       LD      A,($4F7E)       
4ABA: BE             CP      (HL)            
4ABB: 23             INC     HL              
4ABC: C9             RET                     
4ABD: 46             LD      B,(HL)          
4ABE: 23             INC     HL              
4ABF: E5             PUSH    HL              
4AC0: 78             LD      A,B             
4AC1: 32 7E 4F       LD      ($4F7E),A       
4AC4: CD E1 4D       CALL    $4DE1           
4AC7: 22 7F 4F       LD      ($4F7F),HL      
4ACA: E1             POP     HL              
4ACB: 97             SUB     A               
4ACC: C9             RET                     
4ACD: 46             LD      B,(HL)          
4ACE: 23             INC     HL              
4ACF: C3 BE 4C       JP      $4CBE           
4AD2: 4E             LD      C,(HL)          
4AD3: 23             INC     HL              
4AD4: 46             LD      B,(HL)          
4AD5: 23             INC     HL              
4AD6: E5             PUSH    HL              
4AD7: CD E1 4D       CALL    $4DE1           
4ADA: CD 55 47       CALL    $4755           
4ADD: 5E             LD      E,(HL)          
4ADE: 23             INC     HL              
4ADF: 7E             LD      A,(HL)          
4AE0: E1             POP     HL              
4AE1: 7B             LD      A,E             
4AE2: B9             CP      C               
4AE3: C9             RET                     

Com_0C_:
;
4AE4: F6 01          OR      $01             
4AE6: C9             RET                 
 
Com_04_:   
4AE7: 3A 7E 4F       LD      A,($4F7E)       
4AEA: FE 38          CP      $38             
4AEC: CA 08 4B       JP      Z,$4B08         
4AEF: FE 13          CP      $13             
4AF1: C2 01 4B       JP      NZ,$4B01        
4AF4: 06 13          LD      B,$13           
4AF6: E5             PUSH    HL              
4AF7: CD E1 4D       CALL    $4DE1           
4AFA: CD F9 45       CALL    $45F9           
4AFD: E1             POP     HL              
4AFE: CA 08 4B       JP      Z,$4B08         
4B01: CD 56 47       CALL    $4756           
4B04: EB             EX      DE,HL           
4B05: C3 0B 4B       JP      $4B0B           
4B08: CD F9 4D       CALL    $4DF9           
4B0B: 97             SUB     A               
4B0C: C9             RET                     
4B0D: CD 20 4A       CALL    $4A20           
4B10: 97             SUB     A               
4B11: C9             RET                     

Com_06_print_inventory:
4B12: E5             PUSH    HL              
4B13: 3E 0D          LD      A,$0D           
4B15: CD 6B 4E       CALL    $4E6B           
4B18: 21 61 55       LD      HL,$5561        
4B1B: CD 55 47       CALL    $4755           
4B1E: CD 69 47       CALL    $4769           
4B21: D2 4C 4B       JP      NC,$4B4C        
4B24: D5             PUSH    DE              
4B25: CD 55 47       CALL    $4755           
4B28: 46             LD      B,(HL)          
4B29: 3A 7E 4F       LD      A,($4F7E)       
4B2C: B8             CP      B               
4B2D: C2 47 4B       JP      NZ,$4B47        
4B30: 23             INC     HL              
4B31: 23             INC     HL              
4B32: 7E             LD      A,(HL)          
4B33: E6 20          AND     $20             
4B35: CA 47 4B       JP      Z,$4B47         
4B38: 23             INC     HL              
4B39: 06 02          LD      B,$02           
4B3B: CD 41 47       CALL    $4741           
4B3E: D2 47 4B       JP      NC,$4B47        
4B41: 23             INC     HL              
4B42: D5             PUSH    DE              
4B43: CD F0 4D       CALL    $4DF0           
4B46: D1             POP     DE              
4B47: EB             EX      DE,HL           
4B48: D1             POP     DE              
4B49: C3 1E 4B       JP      $4B1E           
4B4C: 97             SUB     A               
4B4D: E1             POP     HL              
4B4E: C9             RET                     
4B4F: E5             PUSH    HL              
4B50: 2A 72 4F       LD      HL,($4F72)      
4B53: 3A 6F 4F       LD      A,($4F6F)       
4B56: 22 84 4F       LD      ($4F84),HL      
4B59: E1             POP     HL              
4B5A: A7             AND     A               
4B5B: CA 70 4B       JP      Z,$4B70         
4B5E: 46             LD      B,(HL)          
4B5F: 23             INC     HL              
4B60: E5             PUSH    HL              
4B61: CD E1 4D       CALL    $4DE1           
4B64: EB             EX      DE,HL           
4B65: E1             POP     HL              
4B66: 3A 84 4F       LD      A,($4F84)       
4B69: BB             CP      E               
4B6A: C0             RET     NZ              
4B6B: 3A 85 4F       LD      A,($4F85)       
4B6E: BA             CP      D               
4B6F: C9             RET                     
4B70: B8             CP      B               
4B71: C9             RET                     
4B72: E5             PUSH    HL              
4B73: 2A 78 4F       LD      HL,($4F78)      
4B76: 3A 75 4F       LD      A,($4F75)       
4B79: C3 56 4B       JP      $4B56           
4B7C: E5             PUSH    HL              
4B7D: 2A 6C 4F       LD      HL,($4F6C)      
4B80: 3A 6B 4F       LD      A,($4F6B)       
4B83: C3 56 4B       JP      $4B56           
4B86: 46             LD      B,(HL)          
4B87: 23             INC     HL              
4B88: 3A 7D 4F       LD      A,($4F7D)       
4B8B: B8             CP      B               
4B8C: C9             RET                     
4B8D: E5             PUSH    HL              
4B8E: 2A 6C 4F       LD      HL,($4F6C)      
4B91: CD 55 47       CALL    $4755           
4B94: 3A 7E 4F       LD      A,($4F7E)       
4B97: 77             LD      (HL),A          
4B98: 97             SUB     A               
4B99: E1             POP     HL              
4B9A: C9             RET                     
4B9B: E5             PUSH    HL              
4B9C: 2A 6C 4F       LD      HL,($4F6C)      
4B9F: CD 55 47       CALL    $4755           
4BA2: 3A 81 4F       LD      A,($4F81)       
4BA5: 77             LD      (HL),A          
4BA6: 97             SUB     A               
4BA7: E1             POP     HL              
4BA8: C9             RET                     
4BA9: E5             PUSH    HL              
4BAA: 2A 82 4F       LD      HL,($4F82)      
4BAD: CD 55 47       CALL    $4755           
4BB0: 23             INC     HL              
4BB1: 06 04          LD      B,$04           
4BB3: CD 41 47       CALL    $4741           
4BB6: D2 C2 4B       JP      NC,$4BC2        
4BB9: CD 55 47       CALL    $4755           
4BBC: CD E4 48       CALL    $48E4           
4BBF: CA 05 4C       JP      Z,$4C05         
4BC2: 3A 75 4F       LD      A,($4F75)       
4BC5: A7             AND     A               
4BC6: CA E3 4B       JP      Z,$4BE3         
4BC9: 2A 78 4F       LD      HL,($4F78)      
4BCC: CD 55 47       CALL    $4755           
4BCF: 23             INC     HL              
4BD0: 23             INC     HL              
4BD1: 23             INC     HL              
4BD2: 06 06          LD      B,$06           
4BD4: CD 41 47       CALL    $4741           
4BD7: D2 E3 4B       JP      NC,$4BE3        
4BDA: CD 55 47       CALL    $4755           
4BDD: CD E4 48       CALL    $48E4           
4BE0: CA 05 4C       JP      Z,$4C05         
4BE3: 3A 6F 4F       LD      A,($4F6F)       
4BE6: A7             AND     A               
4BE7: C2 EE 4B       JP      NZ,$4BEE        
4BEA: E1             POP     HL              
4BEB: F6 01          OR      $01             
4BED: C9             RET                     
4BEE: 2A 72 4F       LD      HL,($4F72)      
4BF1: CD 55 47       CALL    $4755           
4BF4: 23             INC     HL              
4BF5: 23             INC     HL              
4BF6: 23             INC     HL              
4BF7: 06 07          LD      B,$07           
4BF9: CD 41 47       CALL    $4741           
4BFC: D2 EA 4B       JP      NC,$4BEA        
4BFF: CD 55 47       CALL    $4755           
4C02: CD E4 48       CALL    $48E4           
4C05: E1             POP     HL              
4C06: C9             RET                     
4C07: E5             PUSH    HL              
4C08: 2A 6C 4F       LD      HL,($4F6C)      
4C0B: 3A 6B 4F       LD      A,($4F6B)       
4C0E: C3 18 4C       JP      $4C18           
4C11: E5             PUSH    HL              
4C12: 2A 72 4F       LD      HL,($4F72)      
4C15: 3A 6F 4F       LD      A,($4F6F)       
4C18: A7             AND     A               
4C19: CA 05 4C       JP      Z,$4C05         
4C1C: 06 13          LD      B,$13           
4C1E: E5             PUSH    HL              
4C1F: CD E1 4D       CALL    $4DE1           
4C22: CD F9 45       CALL    $45F9           
4C25: E1             POP     HL              
4C26: C2 3B 4C       JP      NZ,$4C3B        
4C29: CD 55 47       CALL    $4755           
4C2C: 23             INC     HL              
4C2D: 23             INC     HL              
4C2E: 23             INC     HL              
4C2F: 06 02          LD      B,$02           
4C31: CD 41 47       CALL    $4741           
4C34: D2 3B 4C       JP      NC,$4C3B        
4C37: 23             INC     HL              
4C38: CD F9 4D       CALL    $4DF9           
4C3B: E1             POP     HL              
4C3C: 97             SUB     A               
4C3D: C9             RET                     
4C3E: E5             PUSH    HL              
4C3F: 3A 75 4F       LD      A,($4F75)       
4C42: 2A 78 4F       LD      HL,($4F78)      
4C45: C3 18 4C       JP      $4C18           
4C48: E5             PUSH    HL              
4C49: 2A 6C 4F       LD      HL,($4F6C)      
4C4C: 3A 6B 4F       LD      A,($4F6B)       
4C4F: A7             AND     A               
4C50: CA EA 4B       JP      Z,$4BEA         
4C53: CD 55 47       CALL    $4755           
4C56: 23             INC     HL              
4C57: 23             INC     HL              
4C58: 7E             LD      A,(HL)          
4C59: E1             POP     HL              
4C5A: A6             AND     (HL)            
4C5B: AE             XOR     (HL)            
4C5C: 23             INC     HL              
4C5D: C9             RET                     
4C5E: E5             PUSH    HL              
4C5F: 2A 6C 4F       LD      HL,($4F6C)      
4C62: 3A 6B 4F       LD      A,($4F6B)       
4C65: A7             AND     A               
4C66: CA EA 4B       JP      Z,$4BEA         
4C69: CD 55 47       CALL    $4755           
4C6C: 23             INC     HL              
4C6D: 23             INC     HL              
4C6E: 7E             LD      A,(HL)          
4C6F: EE 02          XOR     $02             
4C71: 77             LD      (HL),A          
4C72: E1             POP     HL              
4C73: 97             SUB     A               
4C74: C9             RET                     
4C75: E5             PUSH    HL              
4C76: 2A 6C 4F       LD      HL,($4F6C)      
4C79: 3A 6B 4F       LD      A,($4F6B)       
4C7C: A7             AND     A               
4C7D: CA EA 4B       JP      Z,$4BEA         
4C80: CD 55 47       CALL    $4755           
4C83: 23             INC     HL              
4C84: 23             INC     HL              
4C85: 7E             LD      A,(HL)          
4C86: EE 01          XOR     $01             
4C88: 77             LD      (HL),A          
4C89: E1             POP     HL              
4C8A: 97             SUB     A               
4C8B: C9             RET                     
4C8C: CD E4 48       CALL    $48E4           
4C8F: C2 95 4C       JP      NZ,$4C95        
4C92: F6 01          OR      $01             
4C94: C9             RET                     
4C95: 97             SUB     A               
4C96: C9             RET                     
4C97: 46             LD      B,(HL)          
4C98: 23             INC     HL              
4C99: E5             PUSH    HL              
4C9A: CD E1 4D       CALL    $4DE1           
4C9D: CD 55 47       CALL    $4755           
4CA0: D1             POP     DE              
4CA1: 1A             LD      A,(DE)          
4CA2: 77             LD      (HL),A          
4CA3: EB             EX      DE,HL           
4CA4: 23             INC     HL              
4CA5: 97             SUB     A               
4CA6: C9             RET                     
4CA7: E5             PUSH    HL              
4CA8: 2A 6C 4F       LD      HL,($4F6C)      
4CAB: CD 55 47       CALL    $4755           
4CAE: 46             LD      B,(HL)          
4CAF: 78             LD      A,B             
4CB0: A7             AND     A               
4CB1: E1             POP     HL              
4CB2: CA 18 46       JP      Z,$4618         
4CB5: 3A 7E 4F       LD      A,($4F7E)       
4CB8: B8             CP      B               
4CB9: C8             RET     Z               
4CBA: 78             LD      A,B             
4CBB: E6 80          AND     $80             
4CBD: C0             RET     NZ              
4CBE: E5             PUSH    HL              
4CBF: CD E1 4D       CALL    $4DE1           
4CC2: C3 AB 4C       JP      $4CAB           
4CC5: 21 61 55       LD      HL,$5561        
4CC8: 97             SUB     A               
4CC9: 32 7C 4F       LD      ($4F7C),A       
4CCC: CD 55 47       CALL    $4755           
4CCF: CD 69 47       CALL    $4769           
4CD2: D0             RET     NC              
4CD3: 3A 7C 4F       LD      A,($4F7C)       
4CD6: 3C             INC     A               
4CD7: 32 7C 4F       LD      ($4F7C),A       
4CDA: D5             PUSH    DE              
4CDB: CD 55 47       CALL    $4755           
4CDE: 4E             LD      C,(HL)          
4CDF: D5             PUSH    DE              
4CE0: 7E             LD      A,(HL)          
4CE1: A7             AND     A               
4CE2: CA 2A 4D       JP      Z,$4D2A         
4CE5: 23             INC     HL              
4CE6: 23             INC     HL              
4CE7: 23             INC     HL              
4CE8: 06 08          LD      B,$08           
4CEA: CD 41 47       CALL    $4741           
4CED: D2 2A 4D       JP      NC,$4D2A        
4CF0: CD 55 47       CALL    $4755           
4CF3: E5             PUSH    HL              
4CF4: CD 31 4F       CALL    $4F31           
4CF7: 3A 7C 4F       LD      A,($4F7C)       
4CFA: 32 7E 4F       LD      ($4F7E),A       
4CFD: 47             LD      B,A             
4CFE: CD E1 4D       CALL    $4DE1           
4D01: 22 7F 4F       LD      ($4F7F),HL      
4D04: 79             LD      A,C             
4D05: A7             AND     A               
4D06: FA 19 4D       JP      M,$4D19         
4D09: 47             LD      B,A             
4D0A: CD E1 4D       CALL    $4DE1           
4D0D: CD 55 47       CALL    $4755           
4D10: 7E             LD      A,(HL)          
4D11: A7             AND     A               
4D12: C2 05 4D       JP      NZ,$4D05        
4D15: E1             POP     HL              
4D16: C3 2A 4D       JP      $4D2A           
4D19: 32 81 4F       LD      ($4F81),A       
4D1C: 21 01 6A       LD      HL,$6A01        
4D1F: 47             LD      B,A             
4D20: CD 3D 47       CALL    $473D           
4D23: 22 82 4F       LD      ($4F82),HL      
4D26: E1             POP     HL              
4D27: CD E4 48       CALL    $48E4           
4D2A: E1             POP     HL              
4D2B: D1             POP     DE              
4D2C: C3 CF 4C       JP      $4CCF           
4D2F: 3A 57 4F       LD      A,($4F57)       
4D32: BE             CP      (HL)            
4D33: 23             INC     HL              
4D34: DA 3D 4D       JP      C,$4D3D         
4D37: CA 3D 4D       JP      Z,$4D3D         
4D3A: F6 01          OR      $01             
4D3C: C9             RET                     
4D3D: 97             SUB     A               
4D3E: C9             RET                     
4D3F: 4E             LD      C,(HL)          
4D40: 23             INC     HL              
4D41: E5             PUSH    HL              
4D42: 2A 6C 4F       LD      HL,($4F6C)      
4D45: CD 55 47       CALL    $4755           
4D48: 23             INC     HL              
4D49: 23             INC     HL              
4D4A: 23             INC     HL              
4D4B: E5             PUSH    HL              
4D4C: D5             PUSH    DE              
4D4D: 06 09          LD      B,$09           
4D4F: CD 41 47       CALL    $4741           
4D52: D2 7A 4D       JP      NC,$4D7A        
4D55: CD 55 47       CALL    $4755           
4D58: 23             INC     HL              
4D59: 7E             LD      A,(HL)          
4D5A: 91             SUB     C               
4D5B: D2 5F 4D       JP      NC,$4D5F        
4D5E: 97             SUB     A               
4D5F: 77             LD      (HL),A          
4D60: D1             POP     DE              
4D61: E1             POP     HL              
4D62: A7             AND     A               
4D63: CA 69 4D       JP      Z,$4D69         
4D66: 97             SUB     A               
4D67: E1             POP     HL              
4D68: C9             RET                     
4D69: 06 0A          LD      B,$0A           
4D6B: CD 41 47       CALL    $4741           
4D6E: D2 66 4D       JP      NC,$4D66        
4D71: CD 55 47       CALL    $4755           
4D74: CD E4 48       CALL    $48E4           
4D77: C3 66 4D       JP      $4D66           
4D7A: D1             POP     DE              
4D7B: E1             POP     HL              
4D7C: C3 66 4D       JP      $4D66           
4D7F: 46             LD      B,(HL)          
4D80: 23             INC     HL              
4D81: 4E             LD      C,(HL)          
4D82: 23             INC     HL              
4D83: E5             PUSH    HL              
4D84: CD E1 4D       CALL    $4DE1           
4D87: CD 55 47       CALL    $4755           
4D8A: 5E             LD      E,(HL)          
4D8B: 41             LD      B,C             
4D8C: E5             PUSH    HL              
4D8D: D5             PUSH    DE              
4D8E: CD E1 4D       CALL    $4DE1           
4D91: CD 55 47       CALL    $4755           
4D94: D1             POP     DE              
4D95: 7E             LD      A,(HL)          
4D96: 73             LD      (HL),E          
4D97: E1             POP     HL              
4D98: 77             LD      (HL),A          
4D99: E1             POP     HL              
4D9A: 97             SUB     A               
4D9B: C9             RET                     
4D9C: 97             SUB     A               
4D9D: E1             POP     HL              
4D9E: C9             RET                     
4D9F: 4E             LD      C,(HL)          
4DA0: 23             INC     HL              
4DA1: E5             PUSH    HL              
4DA2: 2A 6C 4F       LD      HL,($4F6C)      
4DA5: CD 55 47       CALL    $4755           
4DA8: 23             INC     HL              
4DA9: 23             INC     HL              
4DAA: 23             INC     HL              
4DAB: 06 09          LD      B,$09           
4DAD: CD 41 47       CALL    $4741           
4DB0: D2 9C 4D       JP      NC,$4D9C        
4DB3: CD 55 47       CALL    $4755           
4DB6: 56             LD      D,(HL)          
4DB7: 23             INC     HL              
4DB8: 7E             LD      A,(HL)          
4DB9: 81             ADD     A,C             
4DBA: BA             CP      D               
4DBB: DA BF 4D       JP      C,$4DBF         
4DBE: 7A             LD      A,D             
4DBF: 77             LD      (HL),A          
4DC0: C3 9C 4D       JP      $4D9C           
4DC3: 3A 7E 4F       LD      A,($4F7E)       
4DC6: FE 13          CP      $13             
4DC8: C2 D0 4D       JP      NZ,$4DD0        
4DCB: 3E 0D          LD      A,$0D           
4DCD: CD 6B 4E       CALL    $4E6B           
4DD0: 97             SUB     A               
4DD1: C9             RET                     
4DD2: C3 D2 4D       JP      $4DD2           
4DD5: 1A             LD      A,(DE)          
4DD6: A7             AND     A               
4DD7: C8             RET     Z               
4DD8: D5             PUSH    DE              
4DD9: CD 6B 4E       CALL    $4E6B           
4DDC: D1             POP     DE              
4DDD: 13             INC     DE              
4DDE: C3 D5 4D       JP      $4DD5           
4DE1: 21 61 55       LD      HL,$5561        
4DE4: CD 55 47       CALL    $4755           
4DE7: 05             DEC     B               
4DE8: C8             RET     Z               
4DE9: CD 55 47       CALL    $4755           
4DEC: EB             EX      DE,HL           
4DED: C3 E7 4D       JP      $4DE7           
4DF0: CD F9 4D       CALL    $4DF9           
4DF3: 3E 0D          LD      A,$0D           
4DF5: CD 6B 4E       CALL    $4E6B           
4DF8: C9             RET                     
4DF9: 01 00 00       LD      BC,$0000        
4DFC: 7E             LD      A,(HL)          
4DFD: E6 80          AND     $80             
4DFF: CA 07 4E       JP      Z,$4E07         
4E02: 7E             LD      A,(HL)          
4E03: E6 7F          AND     $7F             
4E05: 47             LD      B,A             
4E06: 23             INC     HL              
4E07: 4E             LD      C,(HL)          
4E08: 23             INC     HL              
4E09: 78             LD      A,B             
4E0A: A7             AND     A               
4E0B: C2 14 4E       JP      NZ,$4E14        
4E0E: 79             LD      A,C             
4E0F: FE 02          CP      $02             
4E11: DA 57 4E       JP      C,$4E57         
4E14: CD 9B 4E       CALL    $4E9B           
4E17: 0B             DEC     BC              
4E18: 0B             DEC     BC              
4E19: 3A 20 40       LD      A,($4020)       
4E1C: FE FB          CP      $FB             
4E1E: DA 09 4E       JP      C,$4E09         
4E21: E5             PUSH    HL              
4E22: 2A 20 40       LD      HL,($4020)      
4E25: 11 BF FF       LD      DE,$FFBF        
4E28: 19             ADD     HL,DE           
4E29: 3E 0D          LD      A,$0D           
4E2B: CD 6B 4E       CALL    $4E6B           
4E2E: 3E 20          LD      A,$20           
4E30: 32 6A 4F       LD      ($4F6A),A       
4E33: 7E             LD      A,(HL)          
4E34: FE 20          CP      $20             
4E36: CA 3D 4E       JP      Z,$4E3D         
4E39: 2B             DEC     HL              
4E3A: C3 33 4E       JP      $4E33           
4E3D: 23             INC     HL              
4E3E: 7E             LD      A,(HL)          
4E3F: FE 20          CP      $20             
4E41: CA 53 4E       JP      Z,$4E53         
4E44: 36 20          LD      (HL),$20        
4E46: FE 1B          CP      $1B             
4E48: D2 4D 4E       JP      NC,$4E4D        
4E4B: C6 40          ADD     $40             
4E4D: CD 6B 4E       CALL    $4E6B           
4E50: C3 3D 4E       JP      $4E3D           
4E53: E1             POP     HL              
4E54: C3 09 4E       JP      $4E09           
4E57: 79             LD      A,C             
4E58: A7             AND     A               
4E59: CA 65 4E       JP      Z,$4E65         
4E5C: 7E             LD      A,(HL)          
4E5D: CD 6B 4E       CALL    $4E6B           
4E60: 23             INC     HL              
4E61: 0D             DEC     C               
4E62: C3 57 4E       JP      $4E57           
4E65: 3E 20          LD      A,$20           
4E67: CD 6B 4E       CALL    $4E6B           
4E6A: C9             RET                     
4E6B: F5             PUSH    AF              
4E6C: 3A 6A 4F       LD      A,($4F6A)       
4E6F: FE 20          CP      $20             
4E71: C2 93 4E       JP      NZ,$4E93        
4E74: F1             POP     AF              
4E75: FE 20          CP      $20             
4E77: C8             RET     Z               
4E78: FE 2E          CP      $2E             
4E7A: CA 87 4E       JP      Z,$4E87         
4E7D: FE 3F          CP      $3F             
4E7F: CA 87 4E       JP      Z,$4E87         
4E82: FE 21          CP      $21             
4E84: C2 94 4E       JP      NZ,$4E94        
4E87: E5             PUSH    HL              
4E88: 2A 20 40       LD      HL,($4020)      
4E8B: 2B             DEC     HL              
4E8C: 22 20 40       LD      ($4020),HL      
4E8F: E1             POP     HL              
4E90: C3 94 4E       JP      $4E94           
4E93: F1             POP     AF              
4E94: 32 6A 4F       LD      ($4F6A),A       
4E97: CD 33 00       CALL    $0033           
4E9A: C9             RET                     
4E9B: 11 2D 4F       LD      DE,$4F2D        
4E9E: C5             PUSH    BC              
4E9F: 06 03          LD      B,$03           
4EA1: 7E             LD      A,(HL)          
4EA2: 23             INC     HL              
4EA3: 4E             LD      C,(HL)          
4EA4: 23             INC     HL              
4EA5: E5             PUSH    HL              
4EA6: 61             LD      H,C             
4EA7: 6F             LD      L,A             
4EA8: 13             INC     DE              
4EA9: 13             INC     DE              
4EAA: EB             EX      DE,HL           
4EAB: E5             PUSH    HL              
4EAC: C5             PUSH    BC              
4EAD: 21 28 00       LD      HL,$0028        
4EB0: 22 2B 4F       LD      ($4F2B),HL      
4EB3: 21 E3 4E       LD      HL,$4EE3        
4EB6: 36 11          LD      (HL),$11        
4EB8: 01 00 00       LD      BC,$0000        
4EBB: C5             PUSH    BC              
4EBC: 7B             LD      A,E             
4EBD: 17             RLA                     
4EBE: 5F             LD      E,A             
4EBF: 7A             LD      A,D             
4EC0: 17             RLA                     
4EC1: 57             LD      D,A             
4EC2: 35             DEC     (HL)            
4EC3: E1             POP     HL              
4EC4: CA E4 4E       JP      Z,$4EE4         
4EC7: 3E 00          LD      A,$00           
4EC9: CE 00          ADC     $00             
4ECB: 29             ADD     HL,HL           
4ECC: 44             LD      B,H             
4ECD: 85             ADD     A,L             
4ECE: 2A 2B 4F       LD      HL,($4F2B)      
4ED1: 95             SUB     L               
4ED2: 4F             LD      C,A             
4ED3: 78             LD      A,B             
4ED4: 9C             SBC     H               
4ED5: 47             LD      B,A             
4ED6: C5             PUSH    BC              
4ED7: D2 DC 4E       JP      NC,$4EDC        
4EDA: 09             ADD     HL,BC           
4EDB: E3             EX      (SP),HL         
4EDC: 21 E3 4E       LD      HL,$4EE3        
4EDF: 3F             CCF                     
4EE0: C3 BC 4E       JP      $4EBC           
4EE3: 00             NOP                     
4EE4: 01 02 4F       LD      BC,$4F02        
4EE7: 09             ADD     HL,BC           
4EE8: 7E             LD      A,(HL)          
4EE9: C1             POP     BC              
4EEA: E1             POP     HL              
4EEB: 77             LD      (HL),A          
4EEC: 2B             DEC     HL              
4EED: 05             DEC     B               
4EEE: C2 AB 4E       JP      NZ,$4EAB        
4EF1: 21 2D 4F       LD      HL,$4F2D        
4EF4: 06 03          LD      B,$03           
4EF6: 7E             LD      A,(HL)          
4EF7: CD 6B 4E       CALL    $4E6B           
4EFA: 23             INC     HL              
4EFB: 05             DEC     B               
4EFC: C2 F6 4E       JP      NZ,$4EF6        
4EFF: E1             POP     HL              
4F00: C1             POP     BC              
4F01: C9             RET                     
4F02: 3F             CCF                     
4F03: 21 32 20       LD      HL,$2032        
4F06: 22 27 3C       LD      ($3C27),HL      
4F09: 3E 2F          LD      A,$2F           
4F0B: 30 33          JR      NC,$4F40        
4F0D: 41             LD      B,C             
4F0E: 42             LD      B,D             
4F0F: 43             LD      B,E             
4F10: 44             LD      B,H             
4F11: 45             LD      B,L             
4F12: 46             LD      B,(HL)          
4F13: 47             LD      B,A             
4F14: 48             LD      C,B             
4F15: 49             LD      C,C             
4F16: 4A             LD      C,D             
4F17: 4B             LD      C,E             
4F18: 4C             LD      C,H             
4F19: 4D             LD      C,L             
4F1A: 4E             LD      C,(HL)          
4F1B: 4F             LD      C,A             
4F1C: 50             LD      D,B             
4F1D: 51             LD      D,C             
4F1E: 52             LD      D,D             
4F1F: 53             LD      D,E             
4F20: 54             LD      D,H             
4F21: 55             LD      D,L             
4F22: 56             LD      D,(HL)          
4F23: 57             LD      D,A             
4F24: 58             LD      E,B             
4F25: 59             LD      E,C             
4F26: 5A             LD      E,D             
4F27: 2D             DEC     L               
4F28: 2C             INC     L               
4F29: 2E 00          LD      L,$00           
4F2B: 00             NOP                     
4F2C: 00             NOP                     
4F2D: 00             NOP                     
4F2E: 00             NOP                     
4F2F: 00             NOP                     
4F30: 00             NOP                     
4F31: C5             PUSH    BC              
4F32: E5             PUSH    HL              
4F33: 2A 57 4F       LD      HL,($4F57)      
4F36: 06 17          LD      B,$17           
4F38: 7D             LD      A,L             
4F39: E6 06          AND     $06             
4F3B: 37             SCF                     
4F3C: EA 40 4F       JP      PE,$4F40        
4F3F: 3F             CCF                     
4F40: 7C             LD      A,H             
4F41: 1F             RRA                     
4F42: 67             LD      H,A             
4F43: 7D             LD      A,L             
4F44: 1F             RRA                     
4F45: E6 FE          AND     $FE             
4F47: 6F             LD      L,A             
4F48: 05             DEC     B               
4F49: C2 39 4F       JP      NZ,$4F39        
4F4C: 22 57 4F       LD      ($4F57),HL      
4F4F: 97             SUB     A               
4F50: E1             POP     HL              
4F51: C1             POP     BC              
4F52: C9             RET                     
4F53: 12             LD      (DE),A          
4F54: 23             INC     HL              
4F55: 44             LD      B,H             
4F56: 1D             DEC     E               
4F57: 27             DAA                     
4F58: 4D             LD      C,L             
4F59: 2D             DEC     L               
4F5A: 13             INC     DE              
4F5B: 00             NOP                     
4F5C: 00             NOP                     
4F5D: 00             NOP                     
4F5E: 00             NOP                     
4F5F: 00             NOP                     
4F60: 00             NOP                     
4F61: 00             NOP                     
4F62: 00             NOP                     
4F63: 00             NOP                     
4F64: 00             NOP                     
4F65: 00             NOP                     
4F66: 00             NOP                     
4F67: 00             NOP                     
4F68: 00             NOP                     
4F69: 00             NOP                     
4F6A: 00             NOP                     
4F6B: 00             NOP                     
4F6C: 00             NOP                     
4F6D: 00             NOP                     
4F6E: 00             NOP                     
4F6F: 00             NOP                     
4F70: 00             NOP                     
4F71: 00             NOP                     
4F72: 00             NOP                     
4F73: 00             NOP                     
4F74: 00             NOP                     
4F75: 00             NOP                     
4F76: 00             NOP                     
4F77: 00             NOP                     
4F78: 00             NOP                     
4F79: 00             NOP                     
4F7A: 00             NOP                     
4F7B: 00             NOP                     
4F7C: 00             NOP                     
4F7D: 00             NOP                     
4F7E: 13             INC     DE              
4F7F: 00             NOP                     
4F80: 00             NOP                     
4F81: 81             ADD     A,C             
4F82: 04             INC     B               
4F83: 6A             LD      L,D             
4F84: A8             XOR     B               
4F85: 4F             LD      C,A             
4F86: 00             NOP                     
4F87: 00             NOP                     
4F88: 06 3F          LD      B,$3F           
4F8A: 56             LD      D,(HL)          
4F8B: 45             LD      B,L             
4F8C: 52             LD      D,D             
4F8D: 42             LD      B,D             
4F8E: 3F             CCF                     
4F8F: 06 3F          LD      B,$3F           
4F91: 57             LD      D,A             
4F92: 48             LD      C,B             
4F93: 41             LD      B,C             
4F94: 54             LD      D,H             
4F95: 3F             CCF                     
4F96: 07             RLCA                    
4F97: 3F             CCF                     
4F98: 57             LD      D,A             
4F99: 48             LD      C,B             
4F9A: 49             LD      C,C             
4F9B: 43             LD      B,E             
4F9C: 48             LD      C,B             
4F9D: 3F             CCF                     
4F9E: 08             EX      AF,AF'          
4F9F: 3F             CCF                     
4FA0: 50             LD      D,B             
4FA1: 48             LD      C,B             
4FA2: 52             LD      D,D             
4FA3: 41             LD      B,C             
4FA4: 53             LD      D,E             
4FA5: 45             LD      B,L             
4FA6: 3F             CCF                     
4FA7: D4 00 00       CALL    NC,$0000        
4FAA: 00             NOP                     
4FAB: 00             NOP                     
4FAC: 00             NOP                     
4FAD: 00             NOP                     
4FAE: 00             NOP                     
4FAF: 00             NOP                     
4FB0: 00             NOP                     
4FB1: 00             NOP                     
4FB2: 00             NOP                     
4FB3: 00             NOP                     
4FB4: 00             NOP                     
4FB5: 00             NOP                     
4FB6: 00             NOP                     
4FB7: 00             NOP                     
4FB8: 00             NOP                     
4FB9: 00             NOP                     
4FBA: 00             NOP                     
4FBB: 00             NOP                     
4FBC: 00             NOP                     
4FBD: 00             NOP                     
4FBE: 00             NOP                     
4FBF: 00             NOP                     
4FC0: 00             NOP                     
4FC1: 00             NOP                     
4FC2: 00             NOP                     
4FC3: 00             NOP                     
4FC4: 00             NOP                     
4FC5: 00             NOP                     
4FC6: 94           
4FC7: A3 
```

# Command Jump Table

```code
CommandJumpTable:              
4FC8: 69 49        ; 
4FCA: AC 4A        ; 
4FCC: CD 4A        ; 
4FCE: D2 4A        ; 
4FD0: E7 4A        ; 
4FD2: 2F 4D        ; 
4FD4: 12 4B        ; 
4FD6: 0D 4B        ; 07      
4FD8: 4F 4B        ; 
4FDA: 72 4B        ; 
4FDC: 86 4B        ; 
4FDE: 44 49        ; 
4FE0: E4 4A        ; 
4FE2: 17 49        ; 0D
4FE4: 2D 49        ; 
4FE6: 8D 4B        ;         
4FE8: 9B 4B        ; 10       
4FEA: 11 4C        ; 
4FEC: 3E 4C        ;      
4FEE: A9 4B        ;    
4FF0: 8C 4C        ;          
4FF2: 48 4C        ;        
4FF4: 07 4C        ;       
4FF6: 97 4C        ;         
4FF8: A7 4C        ; 18       
4FFA: 73 49        ;       
4FFC: 90 49        ;          
4FFE: A0 49        ;     
5000: B0 49        ; 
5002: 3F 4D        ;    
5004: 7F 4D        ; 
5006: F4 4A        ; 
5008: B7 4A        ; 20
500A: C0 49        ; 
500C: 00 00        ;    
500E: 9F 4D        ;       
5010: D2 4D        ; 
5012: C3 4D        ;      
5014: E1 4D        ;  
5016: 00 00        ; 
5018: 00 00        ; 
501A: 5E 4C        ; 
501C: 75 4C        ; 
501E: 31 4F        ; 
5020: BD 4A        ;  
5022: 7C 4B        ; 2D
5024: 00        
```

# Phrase List

```code
5025: 05 00 00 00 01  ; 01: NORTH   *         *       *         
502A: 06 00 00 00 02  ; 02: SOUTH   *         *       *         
502F: 07 00 00 00 03  ; 03: EAST    *         *       *         
5034: 08 00 00 00 04  ; 04: WEST    *         *       *         
5039: 09 00 20 00 05  ; 05: GET     ..C.....  *       *         
503E: 09 02 20 20 43  ; 43: GET     ..C.....  WITH    ..C.....  
5043: 34 07 00 80 05  ; 05: PICK    *         UP      u.......  
5048: 34 07 80 00 05  ; 05: PICK    u.......  UP      *         
504D: 0A 00 20 00 06  ; 06: DROP    ..C.....  *       *         
5052: 0A 05 80 80 0F  ; 0F: DROP    u.......  IN      u.......  
5057: 0B 00 00 00 07  ; 07: INVENT  *         *       *         
505C: 04 02 10 40 09  ; 09: ATTACK  ...P....  WITH    .v......  
5061: 04 00 10 00 09  ; 09: ATTACK  ...P....  *       *         
5066: 0C 00 00 00 0A  ; 0A: LOOK    *         *       *         
506B: 0C 03 00 80 0B  ; 0B: LOOK    *         AT      u.......  
5070: 0C 04 00 80 0C  ; 0C: LOOK    *         UNDER   u.......  
5075: 0C 05 00 80 10  ; 10: LOOK    *         IN      u.......  
507A: 03 03 40 10 0D  ; 0D: THROW   .v......  AT      ...P....  
507F: 03 05 80 80 39  ; 39: THROW   u.......  IN      u.......  
5084: 03 08 00 20 06  ; 06: THROW   *         DOWN    ..C.....  
5089: 03 01 80 10 0E  ; 0E: THROW   u.......  TO      ...P....  
508E: 0D 01 80 10 0E  ; 0E: GIVE    u.......  TO      ...P....  
5093: 0E 00 80 00 0B  ; 0B: EXAMIN  u.......  *       *         
5098: 0E 05 00 80 0B  ; 0B: EXAMIN  *         IN      u.......  
509D: 0F 00 02 00 11  ; 11: OPEN    ......O.  *       *         
50A2: 0F 02 02 80 3A  ; 3A: OPEN    ......O.  WITH    u.......  
50A7: 38 00 08 00 40  ; 40: CLOSE   ....A...  *       *         
50AC: 39 02 08 80 41  ; 41: LOCK    ....A...  WITH    u.......  
50B1: 3A 02 01 80 42  ; 42: UNLOCK  .......L  WITH    u.......  
50B6: 10 00 80 00 12  ; 12: PULL    u.......  *       *         
50BB: 10 08 00 80 12  ; 12: PULL    *         DOWN    u.......  
50C0: 10 08 80 00 12  ; 12: PULL    u.......  DOWN    *         
50C5: 10 06 00 80 05  ; 05: PULL    *         OUT     u.......  
50CA: 10 06 80 00 05  ; 05: PULL    u.......  OUT     *         
50CF: 10 07 00 80 2D  ; 2D: PULL    *         UP      u.......  
50D4: 10 07 80 00 2D  ; 2D: PULL    u.......  UP      *         
50D9: 12 00 80 00 15  ; 15: EAT     u.......  *       *         
50DE: 15 00 80 00 17  ; 17: CLIMB   u.......  *       *         
50E3: 15 07 00 80 17  ; 17: CLIMB   *         UP      u.......  
50E8: 15 08 00 80 17  ; 17: CLIMB   *         DOWN    u.......  
50ED: 15 09 00 80 17  ; 17: CLIMB   *         OVER    u.......  
50F2: 15 0C 00 80 17  ; 17: CLIMB   *         ON      u.......  
50F7: 15 05 00 00 36  ; 36: CLIMB   *         IN      *         
50FC: 15 05 00 80 36  ; 36: CLIMB   *         IN      u.......  
5101: 15 06 00 00 37  ; 37: CLIMB   *         OUT     *         
5106: 15 06 00 80 37  ; 37: CLIMB   *         OUT     u.......  
510B: 15 04 00 80 38  ; 38: CLIMB   *         UNDER   u.......  
5110: 18 00 00 00 1A  ; 1A: ??      *         *       *         
5115: 05 01 00 00 01  ; 01: NORTH   *         TO      *         
511A: 06 01 00 00 02  ; 02: SOUTH   *         TO      *         
511F: 07 01 00 00 03  ; 03: EAST    *         TO      *         
5124: 08 01 00 00 04  ; 04: WEST    *         TO      *         
5129: 0A 08 00 20 06  ; 06: DROP    *         DOWN    ..C.....  
512E: 0A 08 20 00 06  ; 06: DROP    ..C.....  DOWN    *         
5133: 0A 0A 20 80 06  ; 06: DROP    ..C.....  BEHIND  u.......  
5138: 0A 04 20 80 06  ; 06: DROP    ..C.....  UNDER   u.......  
513D: 0A 0C 20 80 06  ; 06: DROP    ..C.....  ON      u.......  
5142: 0C 07 00 00 0A  ; 0A: LOOK    *         UP      *         
5147: 0C 08 00 00 0A  ; 0A: LOOK    *         DOWN    *         
514C: 0C 09 80 00 0B  ; 0B: LOOK    u.......  OVER    *         
5151: 0C 09 00 80 0A  ; 0A: LOOK    *         OVER    u.......  
5156: 0C 0B 00 00 0A  ; 0A: LOOK    *         AROUND  *         
515B: 0C 0A 00 00 0A  ; 0A: LOOK    *         BEHIND  *         
5160: 0C 0B 00 80 1B  ; 1B: LOOK    *         AROUND  u.......  
5165: 0C 0A 00 80 1C  ; 1C: LOOK    *         BEHIND  u.......  
516A: 0C 06 00 00 1D  ; 1D: LOOK    *         OUT     *         
516F: 32 00 00 00 21  ; 21: PLUGH   *         *       *         
5174: 2B 00 00 00 22  ; 22: SCREAM  *         *       *         
5179: 2D 00 00 00 23  ; 23: QUIT    *         *       *         
517E: 3B 00 00 00 44  ; 44: HELLO   *         *       *         
5183: 3B 00 10 00 45  ; 45: HELLO   ...P....  *       *         
5188: 3B 01 00 00 44  ; 44: HELLO   *         TO      *         
518D: 3B 01 00 10 45  ; 45: HELLO   *         TO      ...P....  
5192: 3B 01 10 00 45  ; 45: HELLO   ...P....  TO      *         
5197: 3C 00 00 00 46  ; 46: WHAT    *         *       *         
519C: 3C 00 80 00 47  ; 47: WHAT    u.......  *       *         
51A1: 21 00 00 00 25  ; 25: GO      *         *       *         
51A6: 21 01 00 80 3D  ; 3D: GO      *         TO      u.......  
51AB: 21 05 00 80 36  ; 36: GO      *         IN      u.......  
51B0: 21 06 00 80 37  ; 37: GO      *         OUT     u.......  
51B5: 21 04 00 80 38  ; 38: GO      *         UNDER   u.......  
51BA: 21 07 00 80 17  ; 17: GO      *         UP      u.......  
51BF: 21 08 00 80 17  ; 17: GO      *         DOWN    u.......  
51C4: 21 0B 00 80 26  ; 26: GO      *         AROUND  u.......  
51C9: 23 00 80 00 27  ; 27: KICK    u.......  *       *         
51CE: 23 08 00 80 27  ; 27: KICK    *         DOWN    u.......  
51D3: 23 05 00 80 27  ; 27: KICK    *         IN      u.......  
51D8: 24 02 10 80 28  ; 28: FEED    ...P....  WITH    u.......  
51DD: 24 01 80 10 29  ; 29: FEED    u.......  TO      ...P....  
51E2: 1C 00 80 00 2D  ; 2D: LIFT    u.......  *       *         
51E7: 1F 00 00 00 2F  ; 2F: WAIT    *         *       *         
51EC: 1F 0B 00 00 2F  ; 2F: WAIT    *         AROUND  *         
51F1: 09 07 00 00 2F  ; 2F: GET     *         UP      *         
51F6: 20 09 00 80 34  ; 34: JUMP    *         OVER    u.......  
51FB: 20 05 00 80 36  ; 36: JUMP    *         IN      u.......  
5200: 20 06 00 80 37  ; 37: JUMP    *         OUT     u.......  
5205: 3D 00 80 00 48  ; 48: LOWER   u.......  *       *         
520A: 3E 08 80 00 48  ; 48: LET     u.......  DOWN    *         
520F: 3E 08 00 80 48  ; 48: LET     *         DOWN    u.......  
5214: 09 08 00 80 48  ; 48: GET     *         DOWN    u.......  
5219: 09 08 80 00 48  ; 48: GET     u.......  DOWN    *         
521E: 3F 00 00 00 4A  ; 4A: COME    *         *       *         
5223: 3F 02 00 00 4A  ; 4A: COME    *         WITH    *         
5228: 40 00 80 00 49  ; 49: MEET    u.......  *       *         
522D: 40 01 80 80 49  ; 49: MEET    u.......  TO      u.......  
5232: 00
5233: AC             XOR     H               
```

# Input Word Tables

```code
InputWordTables:

; --- IGNORES ---
5234: 00
;
; --- VERBS ---
5235: 03 47 45 54 09            ; GET      09
523A: 04 47 52 41 42 09         ; GRAB     09
5240: 05 54 48 52 4F 57 03      ; THROW    03
5247: 06 41 54 54 41 43 4B 04   ; ATTACK   04
524F: 05 42 52 45 41 4B 04      ; BREAK    04
5256: 04 4B 49 4C 4C 04         ; KILL     04
525C: 03 48 49 54 04            ; HIT      04
5261: 05 4E 4F 52 54 48 05      ; NORTH    05
5268: 01 4E 05                  ; N        05
526B: 05 53 4F 55 54 48 06      ; SOUTH    06
5272: 01 53 06                  ; S        06
5275: 04 45 41 53 54 07         ; EAST     07
527B: 01 45 07                  ; E        07
527E: 04 57 45 53 54 08         ; WEST     08
5284: 01 57 08                  ; W        08
5287: 04 54 41 4B 45 09         ; TAKE     09
528D: 05 43 41 52 52 59 09      ; CARRY    09
5294: 04 44 52 4F 50 0A         ; DROP     0A
529A: 03 50 55 54 0A            ; PUT      0A
529F: 06 49 4E 56 45 4E 54 0B   ; INVENT   0B
52A7: 04 4C 4F 4F 4B 0C         ; LOOK     0C
52AD: 04 47 49 56 45 0D         ; GIVE     0D
52B3: 05 4F 46 46 45 52 0D      ; OFFER    0D
52BA: 06 45 58 41 4D 49 4E 0E   ; EXAMIN   0E
52C2: 06 53 45 41 52 43 48 0E   ; SEARCH   0E
52CA: 04 4F 50 45 4E 0F         ; OPEN     0F
52D0: 04 50 55 4C 4C 10         ; PULL     10
52D6: 03 45 41 54 12            ; EAT      12
52DB: 05 43 4C 49 4D 42 15      ; CLIMB    15
52E2: 06 41 53 43 45 4E 44 15   ; ASCEND   15
52EA: 06 44 45 53 43 45 4E 15   ; DESCEN   15
52F2: 04 4C 49 46 54 1C         ; LIFT     1C
52F8: 04 57 41 49 54 1F         ; WAIT     1F
52FE: 04 53 54 41 59 1F         ; STAY     1F
5304: 04 4A 55 4D 50 20         ; JUMP     20
530A: 02 47 4F 21               ; GO       21
530E: 03 52 55 4E 21            ; RUN      21
5313: 04 4C 45 46 54 21         ; LEFT     21
5319: 05 52 49 47 48 54 21      ; RIGHT    21
5320: 05 45 4E 54 45 52 21      ; ENTER    21
5327: 04 50 55 53 48 10         ; PUSH     10
532D: 04 4D 4F 56 45 10         ; MOVE     10
5333: 04 4B 49 43 4B 23         ; KICK     23
5339: 04 46 45 45 44 24         ; FEED     24
533F: 06 53 43 52 45 41 4D 2B   ; SCREAM   2B
5347: 04 59 45 4C 4C 2B         ; YELL     2B
534D: 04 51 55 49 54 2D         ; QUIT     2D
5353: 04 53 54 4F 50 2D         ; STOP     2D
5359: 05 50 4C 55 47 48 32      ; PLUGH    32
5360: 04 50 49 43 4B 34         ; PICK     34
5366: 05 43 4C 4F 53 45 38      ; CLOSE    38
536D: 04 4C 4F 43 4B 39         ; LOCK     39
5373: 06 55 4E 4C 4F 43 4B 3A   ; UNLOCK   3A
537B: 05 48 45 4C 4C 4F 3B      ; HELLO    3B
5382: 02 48 49 3B               ; HI       3B
5386: 03 42 4F 57 3B            ; BOW      3B
538B: 05 47 52 45 45 54 3B      ; GREET    3B
5392: 04 57 48 41 54 3C         ; WHAT     3C
5398: 03 57 48 59 3C            ; WHY      3C
539D: 03 48 4F 57 3C            ; HOW      3C
53A2: 05 57 48 45 52 45 3C      ; WHERE    3C
53A9: 03 57 48 4F 3C            ; WHO      3C
53AE: 04 57 48 45 4E 3C         ; WHEN     3C
53B4: 05 4C 4F 57 45 52 3D      ; LOWER    3D
53BB: 05 55 4E 54 49 45 3D      ; UNTIE    3D
53C2: 03 4C 45 54 3E            ; LET      3E
53C7: 04 43 4F 4D 45 3F         ; COME     3F
53CD: 06 46 4F 4C 4C 4F 57 3F   ; FOLLOW   3F
53D5: 04 4D 45 45 54 40         ; MEET     40
53DB: 06 49 4E 54 52 4F 44 40   ; INTROD   40
53E3: 00
;
; --- NOUNS ---
53E4: 03 4B 45 59 16            ; KEY      16
53E9: 04 50 49 4C 4C 17         ; PILL     17
53EF: 04 48 4F 4F 4B 18         ; HOOK     18
53F5: 04 44 4F 4F 52 0B         ; DOOR     0B
53FB: 06 43 41 42 49 4E 45 19   ; CABINE   19
5403: 06 52 45 46 52 49 47 1A   ; REFRIG   1A
540B: 06 48 41 4D 42 55 52 1B   ; HAMBUR   1B
5413: 06 42 55 52 47 45 52 1B   ; BURGER   1B
541B: 04 4D 45 41 54 1B         ; MEAT     1B
5421: 03 44 4F 47 08            ; DOG      08
5426: 04 48 41 4E 44 1F         ; HAND     1F
542C: 05 48 41 4E 44 53 1F      ; HANDS    1F
5433: 06 4E 41 50 4F 4C 45 02   ; NAPOLE   02
543B: 06 42 4F 4E 41 50 41 02   ; BONAPA   02
5443: 03 52 41 59 03            ; RAY      03
5448: 04 58 52 41 59 03         ; XRAY     03
544E: 06 4A 4F 48 4E 53 4F 03   ; JOHNSO   03
5456: 06 48 4F 55 44 49 4E 04   ; HOUDIN   04
545E: 06 50 49 43 41 53 53 05   ; PICASS   05
5466: 06 4D 45 52 4C 49 4E 06   ; MERLIN   06
546E: 06 44 4F 43 54 4F 52 07   ; DOCTOR   07
5476: 05 4E 55 52 53 45 01      ; NURSE    01
547D: 06 54 48 45 52 41 50 01   ; THERAP   01
5485: 04 57 41 4C 4C 25         ; WALL     25
548B: 05 57 41 4C 4C 53 25      ; WALLS    25
5492: 04 52 4F 4F 4D 2A         ; ROOM     2A
5498: 04 43 45 4C 4C 2A         ; CELL     2A
549E: 06 4F 46 46 49 43 45 2A   ; OFFICE   2A
54A6: 04 53 48 45 44 2A         ; SHED     2A
54AC: 05 46 4C 4F 4F 52 2B      ; FLOOR    2B
54B3: 04 45 58 49 54 2C         ; EXIT     2C
54B9: 04 48 4F 4C 45 19         ; HOLE     19
54BF: 06 48 41 4C 4C 57 41 33   ; HALLWA   33
54C7: 06 45 4E 54 52 41 4E 36   ; ENTRAN   36
54CF: 06 43 45 49 4C 49 4E 3B   ; CEILIN   3B
54D7: 04 52 4F 4F 46 3B         ; ROOF     3B
54DD: 00
;
; --- ADJECTIVES ---
54DE: 03 52 45 44 13            ; RED      13
54E3: 05 47 52 45 45 4E 14      ; GREEN    14
54EA: 04 42 4C 55 45 15         ; BLUE     15
54F0: 06 53 45 43 52 45 54 3D   ; SECRET   3D
54F8: 06 50 41 49 4E 54 45 3E   ; PAINTE   3E
5500: 00
;
; --- PREPOSITIONS ---
5501: 02 54 4F 01               ; TO       01
5505: 04 57 49 54 48 02         ; WITH     02
550B: 05 55 53 49 4E 47 02      ; USING    02
5512: 02 41 54 03               ; AT       03
5516: 05 55 4E 44 45 52 04      ; UNDER    04
551D: 02 49 4E 05               ; IN       05
5521: 04 49 4E 54 4F 05         ; INTO     05
5527: 06 49 4E 53 49 44 45 05   ; INSIDE   05
552F: 03 4F 55 54 06            ; OUT      06
5534: 06 4F 55 54 53 49 44 06   ; OUTSID   06
553C: 02 55 50 07               ; UP       07
5540: 04 44 4F 57 4E 08         ; DOWN     08
5546: 04 4F 56 45 52 09         ; OVER     09
554C: 06 42 45 48 49 4E 44 0A   ; BEHIND   0A
5554: 06 41 52 4F 55 4E 44 0B   ; AROUND   0B
555C: 02 4F 4E 0C               ; ON       0C
5560: 00
```

## Object Data

```code
ObjectData:   
5561: 00 94 9D                                                         ; size=149D
;
; Object_01 "GreenDoorA"
5564: 0B 12                                                            ; word=0B size=0012
5566: 85 00 88                                                         ; room=85 scorePoints=00 bits=88
5569:   03 01                                                          ;   03 DESCRIPTION
556B:     84                                                           ;     84(PrintSouthWallGreenDoor)
556C:   01 01                                                          ;   01 ADJECTIVES
556E:   14                                                             ;   TODO WORD
556F:   02 07                                                          ;   02 SHORT_NAME
5571:     AF 6E 83 61 81 5B 52                                         ;     GREEN DOOR
;
; Object_02 "GreenDoorB"
5578: 0B 12                                                            ; word=0B size=0012
557A: 84 00 8A                                                         ; room=84 scorePoints=00 bits=8A
557D:   03 01                                                          ;   03 DESCRIPTION
557F:     86                                                           ;     86(PrintNorthWallGreedDoor)
5580:   01 01                                                          ;   01 ADJECTIVES
5582:   14                                                             ;   TODO WORD
5583:   02 07                                                          ;   02 SHORT_NAME
5585:     AF 6E 83 61 81 5B 52                                         ;     GREEN DOOR
;
; Object_03 "RedDoorA"
558C: 0B 11                                                            ; word=0B size=0011
558E: 84 00 8B                                                         ; room=84 scorePoints=00 bits=8B
5591:   03 01                                                          ;   03 DESCRIPTION
5593:     87                                                           ;     87(PrintSouthWallRedDOor)
5594:   01 01                                                          ;   01 ADJECTIVES
5596:   13                                                             ;   TODO WORD
5597:   02 06                                                          ;   02 SHORT_NAME
5599:     66 B1 09 15 A3 A0                                            ;     RED DOOR
;
; Object_04 "RedDoorB"
559F: 0B 11                                                            ; word=0B size=0011
55A1: 86 00 88                                                         ; room=86 scorePoints=00 bits=88
55A4:   03 01                                                          ;   03 DESCRIPTION
55A6:     85                                                           ;     85(PrintNorthWallRedDoor)
55A7:   01 01                                                          ;   01 ADJECTIVES
55A9:   13                                                             ;   TODO WORD
55AA:   02 06                                                          ;   02 SHORT_NAME
55AC:     66 B1 09 15 A3 A0                                            ;     RED DOOR
;
; Object_05 "GreenDoorC"
55B2: 0B 12                                                            ; word=0B size=0012
55B4: 88 00 8A                                                         ; room=88 scorePoints=00 bits=8A
55B7:   03 01                                                          ;   03 DESCRIPTION
55B9:     84                                                           ;     84(PrintSouthWallGreenDoor)
55BA:   01 01                                                          ;   01 ADJECTIVES
55BC:   14                                                             ;   TODO WORD
55BD:   02 07                                                          ;   02 SHORT_NAME
55BF:     AF 6E 83 61 81 5B 52                                         ;     GREEN DOOR
;
; Object_06 "GreedDoorD"
55C6: 0B 12                                                            ; word=0B size=0012
55C8: 87 00 88                                                         ; room=87 scorePoints=00 bits=88
55CB:   03 01                                                          ;   03 DESCRIPTION
55CD:     86                                                           ;     86(PrintNorthWallGreedDoor)
55CE:   01 01                                                          ;   01 ADJECTIVES
55D0:   14                                                             ;   TODO WORD
55D1:   02 07                                                          ;   02 SHORT_NAME
55D3:     AF 6E 83 61 81 5B 52                                         ;     GREEN DOOR
;
; Object_07 "RedDoorC"
55DA: 0B 11                                                            ; word=0B size=0011
55DC: 87 00 8B                                                         ; room=87 scorePoints=00 bits=8B
55DF:   03 01                                                          ;   03 DESCRIPTION
55E1:     87                                                           ;     87(PrintSouthWallRedDOor)
55E2:   01 01                                                          ;   01 ADJECTIVES
55E4:   13                                                             ;   TODO WORD
55E5:   02 06                                                          ;   02 SHORT_NAME
55E7:     66 B1 09 15 A3 A0                                            ;     RED DOOR
;
; Object_08 "RedDoorD"
55ED: 0B 11                                                            ; word=0B size=0011
55EF: 89 00 88                                                         ; room=89 scorePoints=00 bits=88
55F2:   03 01                                                          ;   03 DESCRIPTION
55F4:     85                                                           ;     85(PrintNorthWallRedDoor)
55F5:   01 01                                                          ;   01 ADJECTIVES
55F7:   13                                                             ;   TODO WORD
55F8:   02 06                                                          ;   02 SHORT_NAME
55FA:     66 B1 09 15 A3 A0                                            ;     RED DOOR
;
; Object_09 "GreenDoorE"
5600: 0B 12                                                            ; word=0B size=0012
5602: 8B 00 88                                                         ; room=8B scorePoints=00 bits=88
5605:   03 01                                                          ;   03 DESCRIPTION
5607:     84                                                           ;     84(PrintSouthWallGreenDoor)
5608:   01 01                                                          ;   01 ADJECTIVES
560A:   14                                                             ;   TODO WORD
560B:   02 07                                                          ;   02 SHORT_NAME
560D:     AF 6E 83 61 81 5B 52                                         ;     GREEN DOOR
;
; Object_0A "GreenDoorF"
5614: 0B 12                                                            ; word=0B size=0012
5616: 8A 00 8A                                                         ; room=8A scorePoints=00 bits=8A
5619:   03 01                                                          ;   03 DESCRIPTION
561B:     86                                                           ;     86(PrintNorthWallGreedDoor)
561C:   01 01                                                          ;   01 ADJECTIVES
561E:   14                                                             ;   TODO WORD
561F:   02 07                                                          ;   02 SHORT_NAME
5621:     AF 6E 83 61 81 5B 52                                         ;     GREEN DOOR
;
; Object_0B "RedDoorE"
5628: 0B 11                                                            ; word=0B size=0011
562A: 8A 00 8B                                                         ; room=8A scorePoints=00 bits=8B
562D:   03 01                                                          ;   03 DESCRIPTION
562F:     87                                                           ;     87(PrintSouthWallRedDOor)
5630:   01 01                                                          ;   01 ADJECTIVES
5632:   13                                                             ;   TODO WORD
5633:   02 06                                                          ;   02 SHORT_NAME
5635:     66 B1 09 15 A3 A0                                            ;     RED DOOR
;
; Object_0C "GreenDoorG"
563B: 0B 12                                                            ; word=0B size=0012
563D: 8D 00 88                                                         ; room=8D scorePoints=00 bits=88
5640:   03 01                                                          ;   03 DESCRIPTION
5642:     84                                                           ;     84(PrintSouthWallGreenDoor)
5643:   01 01                                                          ;   01 ADJECTIVES
5645:   14                                                             ;   TODO WORD
5646:   02 07                                                          ;   02 SHORT_NAME
5648:     AF 6E 83 61 81 5B 52                                         ;     GREEN DOOR
;
; Object_0D "GreenDoorH"
564F: 0B 12                                                            ; word=0B size=0012
5651: 8C 00 8A                                                         ; room=8C scorePoints=00 bits=8A
5654:   03 01                                                          ;   03 DESCRIPTION
5656:     86                                                           ;     86(PrintNorthWallGreedDoor)
5657:   01 01                                                          ;   01 ADJECTIVES
5659:   14                                                             ;   TODO WORD
565A:   02 07                                                          ;   02 SHORT_NAME
565C:     AF 6E 83 61 81 5B 52                                         ;     GREEN DOOR
;
; Object_0E "RedDoorF"
5663: 0B 11                                                            ; word=0B size=0011
5665: 8F 00 88                                                         ; room=8F scorePoints=00 bits=88
5668:   03 01                                                          ;   03 DESCRIPTION
566A:     85                                                           ;     85(PrintNorthWallRedDoor)
566B:   01 01                                                          ;   01 ADJECTIVES
566D:   13                                                             ;   TODO WORD
566E:   02 06                                                          ;   02 SHORT_NAME
5670:     66 B1 09 15 A3 A0                                            ;     RED DOOR
;
; Object_0F "BlueDoorA"
5676: 0B 11                                                            ; word=0B size=0011
5678: 8F 00 8A                                                         ; room=8F scorePoints=00 bits=8A
567B:   02 06                                                          ;   02 SHORT_NAME
567D:     8F 4E 46 5E 44 A0                                            ;     BLUE DOOR
5683:   01 01                                                          ;   01 ADJECTIVES
5685:   15                                                             ;   TODO WORD
5686:   03 01                                                          ;   03 DESCRIPTION
5688:     88                                                           ;     88(PrintEastWallBlueDoor)
;
; Object_10 "BlueDoorB"
5689: 0B 11                                                            ; word=0B size=0011
568B: 90 00 88                                                         ; room=90 scorePoints=00 bits=88
568E:   03 01                                                          ;   03 DESCRIPTION
5690:     89                                                           ;     89(PrintWestWallBlueDoor)
5691:   01 01                                                          ;   01 ADJECTIVES
5693:   15                                                             ;   TODO WORD
5694:   02 06                                                          ;   02 SHORT_NAME
5696:     8F 4E 46 5E 44 A0                                            ;     BLUE DOOR
;
; Object_11 "BlueDoorC"
569C: 0B 11                                                            ; word=0B size=0011
569E: 91 00 8A                                                         ; room=91 scorePoints=00 bits=8A
56A1:   03 01                                                          ;   03 DESCRIPTION
56A3:     89                                                           ;     89(PrintWestWallBlueDoor)
56A4:   01 01                                                          ;   01 ADJECTIVES
56A6:   15                                                             ;   TODO WORD
56A7:   02 06                                                          ;   02 SHORT_NAME
56A9:     8F 4E 46 5E 44 A0                                            ;     BLUE DOOR
;
; Object_12 "BlueDoorD"
56AF: 0B 11                                                            ; word=0B size=0011
56B1: 94 00 88                                                         ; room=94 scorePoints=00 bits=88
56B4:   03 01                                                          ;   03 DESCRIPTION
56B6:     88                                                           ;     88(PrintEastWallBlueDoor)
56B7:   01 01                                                          ;   01 ADJECTIVES
56B9:   15                                                             ;   TODO WORD
56BA:   02 06                                                          ;   02 SHORT_NAME
56BC:     8F 4E 46 5E 44 A0                                            ;     BLUE DOOR
;
; Object_13 "PLAYER"
56C2: FF 42                                                            ; word=FF size=0042
56C4: 88 00 80                                                         ; room=88 scorePoints=00 bits=80
56C7:   08 06                                                          ;   08 TURN SCRIPT
56C9:     0D 04                                                        ;     while_pass: size=0004
56CB:       03 13 3A                                                   ;       is_located(room,object) room=13(Room_13) object=3A(Object3A)
56CE:       9B                                                         ;       9B(??PrintDirs)
56CF:   0A 31                                                          ;   0A UPON DEATH SCRIPT
56D1:     0D 2F                                                        ;     while_pass: size=002F
56D3:       1F 29                                                      ;       print2(msg) size=0029
56D5:         C7 DE DB 16 CB B9 36 A1 B0 17 F4 59 82 17 73 49          ;         YOU PASS OUT UNDER THAT LAST ATTACK. YOU
56E5:         55 8B 03 BC 3B C0 AF 54 51 18 43 C2 0D D0 83 61          ;         AWAKEN IN YOUR CELL.
56F5:         83 7A C7 DE 85 AF 46 61 2E                               ;         ~
56FE:       2C 13                                                      ;       set_ACTIVE(object) object=13(PLAYER)
5700:       19 88                                                      ;       move_ACTIVE(room) room=88(Small square room)
5702:   09 02                                                          ;   HIT POINTS
5704:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
;
; Object_14 "RedKeyA"
5706: 16 21                                                            ; word=16 size=0021
5708: 00 00 A0                                                         ; room=00 scorePoints=00 bits=A0
570B:   03 12                                                          ;   03 DESCRIPTION
570D:     04 10                                                        ;     print(msg) size=0010
570F:       5F BE 5B B1 4B 7B 54 45 F3 5F BB 85 9F 15 7F B1            ;       THERE IS A RED KEY HERE.
571F:   01 01                                                          ;   01 ADJECTIVES
5721:   13                                                             ;   TODO WORD
5722:   02 05                                                          ;   02 SHORT_NAME
5724:     66 B1 17 16 59                                               ;     RED KEY
;
; Object_15 "BluePillA"
5729: 17 34                                                            ; word=17 size=0034
572B: 82 00 A0                                                         ; room=82 scorePoints=00 bits=A0
572E:   03 01                                                          ;   03 DESCRIPTION
5730:     9D                                                           ;     9D(PrintBluePill)
5731:   07 24                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
5733:     0D 22                                                        ;     while_pass: size=0022
5735:       0A 15                                                      ;       compare_input_to(phrase) phrase="15: EAT u....... * *"
5737:       04 1E                                                      ;       print(msg) size=001E
5739:         A7 B7 4B 94 15 B2 DE 88 BF 14 11 BC 2F F7 87 15          ;         SEEMS RISKY, BUT O.K. GULP! HMMM. NO EFF
5749:         91 8D A7 15 7F 93 99 16 28 15 65 66 83 BB                ;         ECT?
5757:   02 06                                                          ;   02 SHORT_NAME
5759:     8F 4E 52 5E 46 7A                                            ;     BLUE PILL
;
; Object_16 "WindowHook"
575F: 18 2C                                                            ; word=18 size=002C
5761: 81 00 A0                                                         ; room=81 scorePoints=00 bits=A0
5764:   03 1D                                                          ;   03 DESCRIPTION
5766:     04 1B                                                        ;     print(msg) size=001B
5768:       5F BE 5B B1 4B 7B 4E 45 11 A0 9B 15 46 98 59 5E            ;       THERE IS A LONG HANDLE WINDOW HOOK HERE.
5778:       8E 7A 6B A1 81 74 CA 83 2F 62 2E                           ;       ~
5783:   02 08                                                          ;   02 SHORT_NAME
5785:     50 D1 89 5B A9 15 8B 9F                                      ;     WINDOW HOOK
;
; Object_17 "Cabinet"
578D: 19 80 9C                                                         ; word=19 size=009C
5790: 82 00 83                                                         ; room=82 scorePoints=00 bits=83
5793:   03 2A                                                          ;   03 DESCRIPTION
5795:     04 28                                                        ;     print(msg) size=0028
5797:       03 A0 0F A0 F3 17 F3 8C 4B 7B 45 45 B3 46 76 98            ;       ON ONE WALL IS A CABINET. THE CABINET HA
57A7:       56 F4 DB 72 04 53 8F 7A 0A BC 4B 49 56 45 A3 7A            ;       S A TINY HOLE IN IT.
57B7:       A9 15 DB 8B 83 7A 97 7B                                    ;       ~
57BF:   07 64                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
57C1:     0E 62                                                        ;     while_fail: size=0062
57C3:       0D 23                                                      ;       while_pass: size=0023
57C5:         0E 06                                                    ;         while_fail: size=0006
57C7:           0A 42                                                  ;           compare_input_to(phrase) phrase="42: UNLOCK .......L WITH u......."
57C9:           0A 3A                                                  ;           compare_input_to(phrase) phrase="3A: OPEN ......O. WITH u......."
57CB:           0A 11                                                  ;           compare_input_to(phrase) phrase="11: OPEN ......O. * *"
57CD:         04 19                                                    ;         print(msg) size=0019
57CF:           C7 DE D3 14 E6 96 57 17 5B 61 6B BF 96 C5 5D 9E        ;           YOU CAN'T SEEM TO UNLOCK THE CABINET.
57DF:           82 17 45 5E B3 46 76 98 2E                             ;           ~
57E8:       0D 3B                                                      ;       while_pass: size=003B
57EA:         0E 04                                                    ;         while_fail: size=0004
57EC:           0A 10                                                  ;           compare_input_to(phrase) phrase="10: LOOK * IN u......."
57EE:           0A 0B                                                  ;           compare_input_to(phrase) phrase="0B: LOOK * AT u......."
57F0:         03 82 3B                                                 ;         is_located(room,object) room=82(Dispensary) object=3B(RedKeyB)
57F3:         04 30                                                    ;         print(msg) size=0030
57F5:           0C BA D0 47 91 7A 89 17 57 17 56 5E F9 74 7A C4        ;           STRAINING TO SEE THROUGH THE TINY HOLE,
5805:           82 17 56 5E A3 7A A9 15 FE 8B 51 18 45 C2 83 48        ;           YOU CAN JUST MAKE OUT A RED KEY.
5815:           F5 81 0F BC 17 48 C7 16 03 BC 2F 17 0D 58 5F 63        ;           ~
5825:   02 05                                                          ;   02 SHORT_NAME
5827:     04 53 8F 7A 54                                               ;     CABINET
;
; Object_18 "Refrigerator"
582C: 1A 80 C9                                                         ; word=1A size=00C9
582F: 92 00 8A                                                         ; room=92 scorePoints=00 bits=8A
5832:   03 2E                                                          ;   03 DESCRIPTION
5834:     04 2C                                                        ;     print(msg) size=002C
5836:       83 7A 5F BE 99 16 C2 B3 95 5F 05 BC B8 A0 23 62            ;       IN THE NORTHEAST CORNER OF THE ROOM THER
5846:       C3 9E 5F BE 39 17 DB 9F 5F BE 5B B1 4B 7B 4E 45            ;       E IS A LARGE REFRIGERATOR
5856:       31 49 54 5E 5C 60 77 79 D6 B0 A3 A0                        ;       ~
5862:   06 3D                                                          ;   06 COMMAND HANDLING IF SECOND NOUN
5864:     0D 3B                                                        ;     while_pass: size=003B
5866:       0A 0F                                                      ;       compare_input_to(phrase) phrase="0F: DROP u....... IN u......."
5868:       1B                                                         ;       set_VAR_to_second_noun()
5869:       0D 0C                                                      ;       while_pass: size=000C
586B:         15 02                                                    ;         check_VAR(bits) bits=02(......O.)
586D:         A9                                                       ;         A9(PrintTheSecondNoun)
586E:         04 07                                                    ;         print(msg) size=0007
5870:           4B 7B C9 54 A6 B7 2E                                   ;           IS CLOSED.
5877:       A8                                                         ;       A8(PrintTheFirstNoun)
5878:       04 08                                                      ;       print(msg) size=0008
587A:         CE 65 0B 8E 36 A1 B8 16                                  ;         FALLS OUT OF
5882:       A9                                                         ;       A9(PrintTheSecondNoun)
5883:       04 1A                                                      ;       print(msg) size=001A
5885:         1E A0 D6 9C DB 72 89 67 A3 A0 68 4D AF A0 C7 DE          ;         ONTO THE FLOOR BEFOREYOU CAN CLOSE IT.
5895:         D3 14 85 96 85 8D 4B 5E 9B C1                            ;         ~
589F:       1A                                                         ;       set_VAR_to_first_noun()
58A0:       10                                                         ;       drop_VAR()
58A1:   07 4B                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
58A3:     0D 49                                                        ;     while_pass: size=0049
58A5:       0A 11                                                      ;       compare_input_to(phrase) phrase="11: OPEN ......O. * *"
58A7:       1A                                                         ;       set_VAR_to_first_noun()
58A8:       15 02                                                      ;       check_VAR(bits) bits=02(......O.)
58AA:       03 18 42                                                   ;       is_located(room,object) room=18(Room_18) object=42(Object42)
58AD:       29                                                         ;       print_open_VAR()
58AE:       17 19 92                                                   ;       move_to(object,room) object=19(HamburgerMeat) room=92(Kitchen)
58B1:       17 42 00                                                   ;       move_to(object,room) object=42(Object42) room=00(Room_00)
58B4:       04 38                                                      ;       print(msg) size=0038
58B6:         1F D1 9B 96 1B A1 5F A0 96 96 DB 72 68 B1 09 B2          ;         WHEN YOU OPEN THE REFRIGERATOR, SOME HAM
58C6:         2B 62 84 BF 15 EE E7 9F 9B 15 BF 91 B7 B1 8F AF          ;         BURGER MEAT FALLS OUT OF IT ONTO THE FLO
58D6:         96 5F 4B 15 0D 8D C7 16 11 BC 8B 64 11 BC C9 9A          ;         OR.
58E6:         82 17 48 5E 81 8D 1B B5                                  ;         ~
58EE:   02 08                                                          ;   02 SHORT_NAME
58F0:     68 B1 09 B2 2B 62 84 BF                                      ;     REFRIGERATOR
;
; Object_19 "HamburgerMeat"
58F8: 1B 6E                                                            ; word=1B size=006E
58FA: 00 00 A0                                                         ; room=00 scorePoints=00 bits=A0
58FD:   03 19                                                          ;   03 DESCRIPTION
58FF:     04 17                                                        ;     print(msg) size=0017
5901:       5F BE 5B B1 4B 7B 3F B9 4A 5E 64 48 31 C6 23 62            ;       THERE IS SOME HAMBURGER MEAT HERE.
5911:       23 92 0A BC 2F 62 2E                                       ;       ~
5918:   06 16                                                          ;   06 COMMAND HANDLING IF SECOND NOUN
591A:     0D 14                                                        ;     while_pass: size=0014
591C:       0A 0F                                                      ;       compare_input_to(phrase) phrase="0F: DROP u....... IN u......."
591E:       0E 10                                                      ;       while_fail: size=0010
5920:         0D 06                                                    ;         while_pass: size=0006
5922:           08 15                                                  ;           is_first_noun(object) object=15(BluePillA)
5924:           17 15 19                                               ;           move_to(object,room) object=15(BluePillA) room=19(Room_19)
5927:           A0                                                     ;           A0(PrintPillInHamburger)
5928:         0D 06                                                    ;         while_pass: size=0006
592A:           08 39                                                  ;           is_first_noun(object) object=39(BluePillB)
592C:           17 39 19                                               ;           move_to(object,room) object=39(BluePillB) room=19(Room_19)
592F:           A0                                                     ;           A0(PrintPillInHamburger)
5930:   07 2A                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
5932:     0D 28                                                        ;     while_pass: size=0028
5934:       0A 15                                                      ;       compare_input_to(phrase) phrase="15: EAT u....... * *"
5936:       04 21                                                      ;       print(msg) size=0021
5938:         F4 4F AB A2 AB AD DB BD 41 6E 73 5D F6 4F 7B 14          ;         BURP! QUITE GOOD, BUT A LITTLE RARE FOR
5948:         96 8C FF BE 2B 17 5B B1 04 68 7B 16 7B 17 FF B9          ;         MY TASTE.
5958:         2E                                                       ;         ~
5959:       17 19 00                                                   ;       move_to(object,room) object=19(HamburgerMeat) room=00(Room_00)
595C:   02 0A                                                          ;   02 SHORT_NAME
595E:     4F 72 F4 4F B4 6C 67 16 73 49                                ;     HAMBURGER MEAT
;
; Object_1A "GuardDog"
5968: 08 81 03                                                         ; word=08 size=0103
596B: 93 00 90                                                         ; room=93 scorePoints=00 bits=90
596E:   03 33                                                          ;   03 DESCRIPTION
5970:     04 31                                                        ;     print(msg) size=0031
5972:       58 45 DB 78 35 A1 87 15 2E 49 09 15 CB 6A C5 B5            ;       A VICIOUS GUARD DOG IS CHAINED TO THE SO
5982:       4B 72 66 98 89 17 82 17 55 5E 36 A1 19 71 46 48            ;       UTH WALL BLOCKING THE SOUTH EXIT.
5992:       B6 14 5D 9E 91 7A 82 17 55 5E 36 A1 07 71 96 D7            ;       ~
59A2:       2E                                                         ;       ~
59A3:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
59A5:     A1                                                           ;     A1(FeedDogMeat)
59A6:   06 01                                                          ;   06 COMMAND HANDLING IF SECOND NOUN
59A8:     A1                                                           ;     A1(FeedDogMeat)
59A9:   0A 1C                                                          ;   0A UPON DEATH SCRIPT
59AB:     0D 1A                                                        ;     while_pass: size=001A
59AD:       1F 15                                                      ;       print2(msg) size=0015
59AF:         C7 DE 4F 24 63 16 C9 97 F3 5F 6B BF 4E 86 16 8A          ;         YOU'VE MANAGED TO KILL THE DOG.
59BF:         DB 72 79 5B 2E                                           ;         ~
59C4:       1E 1A 3C                                                   ;       swap(object_a,object_b) object_a=(GuardDog)1A object_b=3C(DeadDog)
59C7:   08 80 94                                                       ;   08 TURN SCRIPT
59CA:     0E 80 91                                                     ;     while_fail: size=0091
59CD:       0D 7D                                                      ;       while_pass: size=007D
59CF:         0A 09                                                    ;         compare_input_to(phrase) phrase="09: ATTACK ...P.... WITH .v......"
59D1:         1C 13                                                    ;         set_VAR(object) object=13(PLAYER)
59D3:         0B 77 05                                                 ;         switch(is_less_equal_last_random(value)): size=0077
59D6:           55                                                     ;           is_less_equal_last_random(value) value=55
59D7:           22                                                     ;           IF_NOT_GOTO address=59FA
59D8:             0D 20                                                ;             while_pass: size=0020
59DA:               1F 1C                                              ;               print2(msg) size=001C
59DC:                 5F BE 09 15 D6 6A 94 5F C3 B5 1B BC 34 A1 3F 16  ;                 THE DOG TEARS AT YOUR LEG AND DRAWS BLOO
59EC:                 C3 6A 33 98 EB 5B CB D2 89 4E 71 9E              ;                 D!
59F8:               1D 06                                              ;               attack_VAR(points) points=06
59FA:           AF                                                     ;           is_less_equal_last_random(value) value=AF
59FB:           26                                                     ;           IF_NOT_GOTO address=5A22
59FC:             0D 24                                                ;             while_pass: size=0024
59FE:               1F 20                                              ;               print2(msg) size=0020
5A00:                 5F BE 09 15 C4 6A 7F 7B DB B5 34 A1 94 14 43 90  ;                 THE DOG BITES YOUR ARM AND YOU CRINGE WI
5A10:                 33 98 C7 DE E4 14 91 7A 59 5E 82 7B DB 16 81 7A  ;                 TH PAIN!
5A20:               1D 07                                              ;               attack_VAR(points) points=07
5A22:           FF                                                     ;           is_less_equal_last_random(value) value=FF
5A23:           28                                                     ;           IF_NOT_GOTO address=5A4C
5A24:             1F 26                                                ;             print2(msg) size=0026
5A26:               5F BE 09 15 CE 6A 91 C5 4B 62 04 68 51 18 23 C6    ;               THE DOG LUNGES FOR YOUR NECK, BUT YOU PU
5A36:               65 98 33 89 F6 4F 51 18 52 C2 46 C5 AB 14 8B 54    ;               LL BACK IN TIME!
5A46:               83 7A 8F BE EB 5D                                  ;               ~
5A4C:       1F 10                                                      ;       print2(msg) size=0010
5A4E:         41 1E C3 9E B9 6E B3 D1 41 D2 99 64 38 A0 E3 06          ;         "WOOF GROWL WOOF WOOF!"
5A5E:   09 02                                                          ;   HIT POINTS
5A60:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
5A62:   02 0A                                                          ;   02 SHORT_NAME
5A64:     5F BE D3 17 51 54 4B C6 79 5B                                ;     THE VICIOUS DOG
;
; Object_1B "GreenKeyA"
5A6E: 16 24                                                            ; word=16 size=0024
5A70: 8E 00 A0                                                         ; room=8E scorePoints=00 bits=A0
5A73:   03 14                                                          ;   03 DESCRIPTION
5A75:     04 12                                                        ;     print(msg) size=0012
5A77:       5F BE 5B B1 4B 7B 49 45 67 B1 8D 96 3B 63 F4 72            ;       THERE IS A GREEN KEY HERE.
5A87:       DB 63                                                      ;       ~
5A89:   01 01                                                          ;   01 ADJECTIVES
5A8B:   14                                                             ;   TODO WORD
5A8C:   02 06                                                          ;   02 SHORT_NAME
5A8E:     AF 6E 83 61 BB 85                                            ;     GREEN KEY
;
; Object_1C "RayA"
5A94: 03 81 60                                                         ; word=03 size=0160
5A97: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
5A9A:   03 18                                                          ;   03 DESCRIPTION
5A9C:     04 16                                                        ;     print(msg) size=0016
5A9E:       DB B0 57 17 75 61 89 17 AF 14 3B 15 D0 60 D6 6A            ;       RAY SEEMS TO BE EYEING THE WALLS.
5AAE:       DB 72 0E D0 2F 8E                                          ;       ~
5AB4:   09 02                                                          ;   HIT POINTS
5AB6:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
5AB8:   0B 81 2D                                                       ;   0B COMMAND HANDLING IF GIVEN COMMAND
5ABB:     0E 81 2A                                                     ;     while_fail: size=012A
5ABE:       0D 80 DF                                                   ;       while_pass: size=00DF
5AC1:         0E 0A                                                    ;         while_fail: size=000A
5AC3:           0A 01                                                  ;           compare_input_to(phrase) phrase="01: NORTH * * *"
5AC5:           0A 02                                                  ;           compare_input_to(phrase) phrase="02: SOUTH * * *"
5AC7:           0A 03                                                  ;           compare_input_to(phrase) phrase="03: EAST * * *"
5AC9:           0A 04                                                  ;           compare_input_to(phrase) phrase="04: WEST * * *"
5ACB:           0A 0A                                                  ;           compare_input_to(phrase) phrase="0A: LOOK * * *"
5ACD:         1F 0F                                                    ;         print2(msg) size=000F
5ACF:           DB B0 2F 17 84 A6 0B C0 DB 72 10 53 57 17 45           ;           RAY REPORTS HE CAN SEE
5ADE:         1C 38                                                    ;         set_VAR(object) object=38(SYSTEM)
5AE0:         10                                                       ;         drop_VAR()
5AE1:         2C 38                                                    ;         set_ACTIVE(object) object=38(SYSTEM)
5AE3:         0E 80 B8                                                 ;         while_fail: size=00B8
5AE6:           0D 33                                                  ;           while_pass: size=0033
5AE8:             01 3D                                                ;             is_in_pack_or_current_room(object) object=3D(SecretDoor)
5AEA:             1F 2E                                                ;             print2(msg) size=002E
5AEC:               55 45 E4 5F 73 62 81 5B 8A AF 2F 62 19 EE 85 73    ;               A SECRET DOOR HERE, WHICH MAY LEAD TO ES
5AFC:               0F 71 3B 4A E3 8B 16 58 C7 9C 53 B7 FF A4 AF 14    ;               CAPE. BESIDES THAT, THERE IS
5B0C:               46 B8 4B 62 5B BE 73 C1 5F BE 5B B1 4B 7B          ;               ~
5B1A:             0C                                                   ;             fail()
5B1B:           0D 3D                                                  ;           while_pass: size=003D
5B1D:             03 00 22                                             ;             is_located(room,object) room=00(Room_00) object=22(PicassoA)
5B20:             03 88 1C                                             ;             is_located(room,object) room=88(Small square room) object=1C(RayA)
5B23:             1F 34                                                ;             print2(msg) size=0034
5B25:               5B BE 04 BC 51 63 33 98 5F BE 99 16 C2 B3 F3 17    ;               THAT BEYOND THE NORTH WALL IS A POSSIBLE
5B35:               F3 8C 4B 7B 52 45 E5 A0 B6 78 47 5E 53 B7 DB A4    ;               ESCAPE ROUTE. BESIDES THAT, THERE IS
5B45:               07 B3 FF BD AF 14 46 B8 4B 62 5B BE 73 C1 5F BE    ;               ~
5B55:               5B B1 4B 7B                                        ;               ~
5B59:             0C                                                   ;             fail()
5B5A:           0D 06                                                  ;           while_pass: size=0006
5B5C:             0A 03                                                ;             compare_input_to(phrase) phrase="03: EAST * * *"
5B5E:             21 03 00 00                                          ;             execute_phrase(phrase,first_noun,second_noun) phrase="03: EAST * * *" firstNoun=00 secondNoun=00
5B62:           0D 06                                                  ;           while_pass: size=0006
5B64:             0A 04                                                ;             compare_input_to(phrase) phrase="04: WEST * * *"
5B66:             21 04 00 00                                          ;             execute_phrase(phrase,first_noun,second_noun) phrase="04: WEST * * *" firstNoun=00 secondNoun=00
5B6A:           0D 06                                                  ;           while_pass: size=0006
5B6C:             0A 01                                                ;             compare_input_to(phrase) phrase="01: NORTH * * *"
5B6E:             21 01 00 00                                          ;             execute_phrase(phrase,first_noun,second_noun) phrase="01: NORTH * * *" firstNoun=00 secondNoun=00
5B72:           0D 06                                                  ;           while_pass: size=0006
5B74:             0A 02                                                ;             compare_input_to(phrase) phrase="02: SOUTH * * *"
5B76:             21 02 00 00                                          ;             execute_phrase(phrase,first_noun,second_noun) phrase="02: SOUTH * * *" firstNoun=00 secondNoun=00
5B7A:           1F 22                                                  ;           print2(msg) size=0022
5B7C:             06 9A 90 73 5B 70 B7 1C F3 B9 5B 4D 3F B9 4E 5E      ;             NOTHING. "MUST BE SOME LEAD-LINED WALLS!
5B8C:             86 5F C3 EA 66 98 F3 17 0D 8D E3 06 DB 72 1B B7      ;             " HE SAYS.
5B9C:             5B BB                                                ;             ~
5B9E:         2C 1C                                                    ;         set_ACTIVE(object) object=1C(RayA)
5BA0:       0D 45                                                      ;       while_pass: size=0045
5BA2:         0E 06                                                    ;         while_fail: size=0006
5BA4:           0A 11                                                  ;           compare_input_to(phrase) phrase="11: OPEN ......O. * *"
5BA6:           0A 42                                                  ;           compare_input_to(phrase) phrase="42: UNLOCK .......L WITH u......."
5BA8:           0A 09                                                  ;           compare_input_to(phrase) phrase="09: ATTACK ...P.... WITH .v......"
5BAA:         1F 3B                                                    ;         print2(msg) size=003B
5BAC:           DB B0 63 16 B5 85 7B 14 67 66 7F 4E 96 14 EF BD        ;           RAY MAKES A FEEBLE ATTEMPT AND THEN DRAW
5BBC:           33 A7 8E 48 82 17 83 61 EB 5B CB D2 C5 4C 5B 89        ;           S BACK. "SORRY, I'VE BEEN RATHER ANEMIC
5BCC:           A1 1D 83 B3 0B EE 4F 24 AF 14 83 61 D6 B0 F4 72        ;           LATELY!"
5BDC:           90 14 6B 61 CE 51 7F 49 F9 8E 22                       ;           ~
5BE7:       9A                                                         ;       9A(??CommandResponse)
5BE8:   08 06                                                          ;   08 TURN SCRIPT
5BEA:     0D 04                                                        ;     while_pass: size=0004
5BEC:       9C                                                         ;       9C(??MoveHoudiniC)
5BED:       1C 1C                                                      ;       set_VAR(object) object=1C(RayA)
5BEF:       9E                                                         ;       9E(PrintObjectEntersRoom)
5BF0:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
5BF2:     AB                                                           ;     AB(AttackPerson)
5BF3:   02 02                                                          ;   02 SHORT_NAME
5BF5:     DB B0                                                        ;     RAY
;
; Object_1D "RayB"
5BF7: 03 80 AE                                                         ; word=03 size=00AE
5BFA: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
5BFD:   03 80 A8                                                       ;   03 DESCRIPTION
5C00:     0D 80 A5                                                     ;     while_pass: size=00A5
5C03:       04 80 9F                                                   ;       print(msg) size=009F
5C06:         4F 45 83 48 83 7A 94 5A FB C0 4F A1 CE B0 0B 8E          ;         A MAN IN DIRTY OVERALLS AND WEARING GOGG
5C16:         8E 48 F7 17 33 49 AB 98 39 6E BF 6D C3 B5 AC A6          ;         LES APPROACHES YOU AND INTRODUCES HIMSEL
5C26:         05 9E F5 72 51 18 43 C2 33 98 9E 7A F6 B2 D7 C3          ;         F. "HI! MY NAME IS XRAY JOHNSON, BUT YOU
5C36:         CA B5 75 7A 40 61 3C F4 79 73 7B 16 8B 16 1B 92          ;         CAN CALL ME RAY. I HAVE XRAY VISION, YO
5C46:         4B 7B EB D8 4C DB 28 9F 40 B9 04 EE 73 C6 C7 DE          ;         U KNOW. SAY, YOU BETTER HAVE THAT SPOT O
5C56:         D3 14 85 96 46 48 67 16 2B 17 DB E0 4A 77 CF 49          ;         N YOUR LEFT LUNG CHECKED BY A DOCTOR!"
5C66:         2C 18 3B 4A 15 CB C0 7A 1B EE 1B A1 19 87 5B D4          ;         ~
5C76:         1B B7 1B EE 1B A1 76 4D F4 BD 9B 15 5B CA 5B BE          ;         ~
5C86:         15 BC 86 A6 C0 16 51 18 23 C6 E8 8B 0E BC 91 C5          ;         ~
5C96:         DA 14 DD 5F F3 5F 7B 50 46 45 66 9E A1 A0 22             ;         ~
5CA5:       1E 1C 1D                                                   ;       swap(object_a,object_b) object_a=(RayA)1C object_b=1D(RayB)
;
; Object_1E "NapoleanA"
5CA8: 02 77                                                            ; word=02 size=0077
5CAA: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
5CAD:   03 01                                                          ;   03 DESCRIPTION
5CAF:     97                                                           ;     97(PrintNapolean)
5CB0:   02 06                                                          ;   02 SHORT_NAME
5CB2:     D2 97 BF 9F 03 A0                                            ;     NAPOLEON
5CB8:   0B 58                                                          ;   0B COMMAND HANDLING IF GIVEN COMMAND
5CBA:     0E 56                                                        ;     while_fail: size=0056
5CBC:       0D 53                                                      ;       while_pass: size=0053
5CBE:         0E 06                                                    ;         while_fail: size=0006
5CC0:           0A 11                                                  ;           compare_input_to(phrase) phrase="11: OPEN ......O. * *"
5CC2:           0A 42                                                  ;           compare_input_to(phrase) phrase="42: UNLOCK .......L WITH u......."
5CC4:           0A 09                                                  ;           compare_input_to(phrase) phrase="09: ATTACK ...P.... WITH .v......"
5CC6:         1A                                                       ;         set_VAR_to_first_noun()
5CC7:         15 08                                                    ;         check_VAR(bits) bits=08(....A...)
5CC9:         1F 46                                                    ;         print2(msg) size=0046
5CCB:           D2 97 BF 9F 03 A0 AB 6E 8B 4F 96 7B BF 14 0A BC        ;           NAPOLEON GRABS IT, BUT HE CAN'T BUDGE IT
5CDB:           45 5E 85 48 04 BC 01 C4 4B 5E AB BB DB 72 74 C0        ;           ! HE TURNS TO YOU AND MUMBLES SOMETHING
5CEB:           8B 9A 6B BF C7 DE 90 14 0F 58 64 C5 F5 8B 61 17        ;           ABOUT BEING RATHER TIRED.
5CFB:           36 92 90 73 C3 6A 07 4F 04 BC D0 60 D4 6A 82 49        ;           ~
5D0B:           23 62 94 BE 17 60                                      ;           ~
5D11:       9A                                                         ;       9A(??CommandResponse)
5D12:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
5D14:     AB                                                           ;     AB(AttackPerson)
5D15:   08 06                                                          ;   08 TURN SCRIPT
5D17:     0D 04                                                        ;     while_pass: size=0004
5D19:       9C                                                         ;       9C(??MoveHoudiniC)
5D1A:       1C 1E                                                      ;       set_VAR(object) object=1E(NapoleanA)
5D1C:       9E                                                         ;       9E(PrintObjectEntersRoom)
5D1D:   09 02                                                          ;   HIT POINTS
5D1F:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
;
; Object_1F "Object1F"
5D21: 02 0B                                                            ; word=02 size=000B
5D23: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
5D26:   03 06                                                          ;   03 DESCRIPTION
5D28:     0D 04                                                        ;     while_pass: size=0004
5D2A:       96                                                         ;       96(PrintNapoleanIntro)
5D2B:       1E 1E 1F                                                   ;       swap(object_a,object_b) object_a=(NapoleanA)1E object_b=1F(Object1F)
;
; Object_20 "NapoleanB"
5D2E: 02 80 97                                                         ; word=02 size=0097
5D31: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
5D34:   03 01                                                          ;   03 DESCRIPTION
5D36:     97                                                           ;     97(PrintNapolean)
5D37:   02 06                                                          ;   02 SHORT_NAME
5D39:     D2 97 BF 9F 03 A0                                            ;     NAPOLEON
5D3F:   0B 78                                                          ;   0B COMMAND HANDLING IF GIVEN COMMAND
5D41:     0E 76                                                        ;     while_fail: size=0076
5D43:       0D 73                                                      ;       while_pass: size=0073
5D45:         0E 06                                                    ;         while_fail: size=0006
5D47:           0A 11                                                  ;           compare_input_to(phrase) phrase="11: OPEN ......O. * *"
5D49:           0A 42                                                  ;           compare_input_to(phrase) phrase="42: UNLOCK .......L WITH u......."
5D4B:           0A 09                                                  ;           compare_input_to(phrase) phrase="09: ATTACK ...P.... WITH .v......"
5D4D:         1A                                                       ;         set_VAR_to_first_noun()
5D4E:         15 08                                                    ;         check_VAR(bits) bits=08(....A...)
5D50:         0E 66                                                    ;         while_fail: size=0066
5D52:           0D 49                                                  ;           while_pass: size=0049
5D54:             15 02                                                ;             check_VAR(bits) bits=02(......O.)
5D56:             1F 0A                                                ;             print2(msg) size=000A
5D58:               D2 97 BF 9F 03 A0 AB 6E 8B 4F                      ;               NAPOLEON GRABS
5D62:             A8                                                   ;             A8(PrintTheFirstNoun)
5D63:             1F 0C                                                ;             print2(msg) size=000C
5D65:               8E 48 BF 14 0D BA D6 15 C2 16 81 61                ;               AND BUSTS IT OPEN!
5D71:             29                                                   ;             print_open_VAR()
5D72:             0E 29                                                ;             while_fail: size=0029
5D74:               0D 25                                              ;               while_pass: size=0025
5D76:                 08 3D                                            ;                 is_first_noun(object) object=3D(SecretDoor)
5D78:                 1F 20                                            ;                 print2(msg) size=0020
5D7A:                   5F BE 57 17 AF 55 06 BC 44 A0 3F 16 0D 47 89 17;                   THE SECRET DOOR LEADS TO ESCAPE! YOU'VE
5D8A:                   35 15 12 53 EB 5D C7 DE 4F 24 63 16 DB 59 71 7B;                   MADE IT!
5D9A:                 24                                               ;                 endless_loop()
5D9B:               14                                                 ;               execute_and_reverse_status:
5D9C:               0C                                                 ;               fail()
5D9D:           0D 19                                                  ;           while_pass: size=0019
5D9F:             1F 0E                                                ;             print2(msg) size=000E
5DA1:               D2 97 BF 9F 03 A0 72 B1 BE A0 D6 B5 56 72          ;               NAPOLEON REPORTS THAT
5DAF:             A8                                                   ;             A8(PrintTheFirstNoun)
5DB0:             1F 06                                                ;             print2(msg) size=0006
5DB2:               4B 7B 5F A0 1B 9C                                  ;               IS OPEN.
5DB8:       9A                                                         ;       9A(??CommandResponse)
5DB9:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
5DBB:     AB                                                           ;     AB(AttackPerson)
5DBC:   08 06                                                          ;   08 TURN SCRIPT
5DBE:     0D 04                                                        ;     while_pass: size=0004
5DC0:       9C                                                         ;       9C(??MoveHoudiniC)
5DC1:       1C 20                                                      ;       set_VAR(object) object=20(NapoleanB)
5DC3:       9E                                                         ;       9E(PrintObjectEntersRoom)
5DC4:   09 02                                                          ;   HIT POINTS
5DC6:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
;
; Object_21 "Object21"
5DC8: 02 0B                                                            ; word=02 size=000B
5DCA: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
5DCD:   03 06                                                          ;   03 DESCRIPTION
5DCF:     0D 04                                                        ;     while_pass: size=0004
5DD1:       96                                                         ;       96(PrintNapoleanIntro)
5DD2:       1E 20 21                                                   ;       swap(object_a,object_b) object_a=(NapoleanB)20 object_b=21(Object21)
;
; Object_22 "PicassoA"
5DD5: 05 25                                                            ; word=05 size=0025
5DD7: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
5DDA:   03 01                                                          ;   03 DESCRIPTION
5DDC:     99                                                           ;     99(PrintPicasso)
5DDD:   02 05                                                          ;   02 SHORT_NAME
5DDF:     85 A5 65 49 4F                                               ;     PICASSO
5DE4:   0B 01                                                          ;   0B COMMAND HANDLING IF GIVEN COMMAND
5DE6:     9A                                                           ;     9A(??CommandResponse)
5DE7:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
5DE9:     AB                                                           ;     AB(AttackPerson)
5DEA:   08 0C                                                          ;   08 TURN SCRIPT
5DEC:     0E 0A                                                        ;     while_fail: size=000A
5DEE:       0D 04                                                      ;       while_pass: size=0004
5DF0:         9C                                                       ;         9C(??MoveHoudiniC)
5DF1:         1C 22                                                    ;         set_VAR(object) object=22(PicassoA)
5DF3:         9E                                                       ;         9E(PrintObjectEntersRoom)
5DF4:       14                                                         ;       execute_and_reverse_status:
5DF5:       1C 3F                                                      ;       set_VAR(object) object=3F(PaintedDoorB)
5DF7:       10                                                         ;       drop_VAR()
5DF8:   09 02                                                          ;   HIT POINTS
5DFA:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
;
; Object_23 "Object23"
5DFC: 05 0B                                                            ; word=05 size=000B
5DFE: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
5E01:   03 06                                                          ;   03 DESCRIPTION
5E03:     0D 04                                                        ;     while_pass: size=0004
5E05:       98                                                         ;       98(PrintPicassoIntro)
5E06:       1E 22 23                                                   ;       swap(object_a,object_b) object_a=(PicassoA)22 object_b=23(Object23)
;
; Object_24 "PicassoB"
5E09: 05 34                                                            ; word=05 size=0034
5E0B: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
5E0E:   03 01                                                          ;   03 DESCRIPTION
5E10:     99                                                           ;     99(PrintPicasso)
5E11:   02 05                                                          ;   02 SHORT_NAME
5E13:     85 A5 65 49 4F                                               ;     PICASSO
5E18:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
5E1A:     AB                                                           ;     AB(AttackPerson)
5E1B:   0B 01                                                          ;   0B COMMAND HANDLING IF GIVEN COMMAND
5E1D:     9A                                                           ;     9A(??CommandResponse)
5E1E:   08 1B                                                          ;   08 TURN SCRIPT
5E20:     0E 19                                                        ;     while_fail: size=0019
5E22:       0D 08                                                      ;       while_pass: size=0008
5E24:         14                                                       ;         execute_and_reverse_status:
5E25:         03 88 24                                                 ;         is_located(room,object) room=88(Small square room) object=24(PicassoB)
5E28:         1C 3F                                                    ;         set_VAR(object) object=3F(PaintedDoorB)
5E2A:         10                                                       ;         drop_VAR()
5E2B:         0C                                                       ;         fail()
5E2C:       0D 07                                                      ;       while_pass: size=0007
5E2E:         03 88 24                                                 ;         is_located(room,object) room=88(Small square room) object=24(PicassoB)
5E31:         17 3E 88                                                 ;         move_to(object,room) object=3E(PaintedDoorA) room=88(Small square room)
5E34:         0C                                                       ;         fail()
5E35:       0D 04                                                      ;       while_pass: size=0004
5E37:         9C                                                       ;         9C(??MoveHoudiniC)
5E38:         1C 24                                                    ;         set_VAR(object) object=24(PicassoB)
5E3A:         9E                                                       ;         9E(PrintObjectEntersRoom)
5E3B:   09 02                                                          ;   HIT POINTS
5E3D:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
;
; Object_25 "Object25"
5E3F: 05 0B                                                            ; word=05 size=000B
5E41: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
5E44:   03 06                                                          ;   03 DESCRIPTION
5E46:     0D 04                                                        ;     while_pass: size=0004
5E48:       98                                                         ;       98(PrintPicassoIntro)
5E49:       1E 24 25                                                   ;       swap(object_a,object_b) object_a=(PicassoB)24 object_b=25(Object25)
;
; Object_26 "MerlinA"
5E4C: 06 80 FD                                                         ; word=06 size=00FD
5E4F: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
5E52:   03 25                                                          ;   03 DESCRIPTION
5E54:     04 23                                                        ;     print(msg) size=0023
5E56:       34 92 90 8C D5 15 8F 16 2C 49 B3 E0 1B 54 C3 9A            ;       MERLIN IS NEARBY, CHANTING AND GESTICULA
5E66:       AB 98 8E 48 77 15 03 BA 2E 56 83 49 AB 98 73 49            ;       TING AT YOU.
5E76:       C7 DE 2E                                                   ;       ~
5E79:   02 04                                                          ;   02 SHORT_NAME
5E7B:     34 92 90 8C                                                  ;     MERLIN
5E7F:   0B 01                                                          ;   0B COMMAND HANDLING IF GIVEN COMMAND
5E81:     9A                                                           ;     9A(??CommandResponse)
5E82:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
5E84:     AB                                                           ;     AB(AttackPerson)
5E85:   08 80 C0                                                       ;   08 TURN SCRIPT
5E88:     0E 80 BD                                                     ;     while_fail: size=00BD
5E8B:       0D 04                                                      ;       while_pass: size=0004
5E8D:         9C                                                       ;         9C(??MoveHoudiniC)
5E8E:         1C 26                                                    ;         set_VAR(object) object=26(MerlinA)
5E90:         9E                                                       ;         9E(PrintObjectEntersRoom)
5E91:       0B 80 B4 05                                                ;       switch(is_less_equal_last_random(value)): size=00B4
5E95:         08                                                       ;         is_less_equal_last_random(value) value=08
5E96:         30                                                       ;         IF_NOT_GOTO address=5EC7
5E97:           1F 2E                                                  ;           print2(msg) size=002E
5E99:             34 92 90 8C 53 17 6E DF 6E 13 71 61 F3 9B 45 77      ;             MERLIN SAYS, "DEMON, I COMMAND YOU! REVE
5EA9:             EF 9F 8E 48 51 18 EB C1 78 B1 8E 5F 89 17 67 16      ;             AL TO ME THE DOOR OF ESCAPE!"
5EB9:             82 17 46 5E 44 A0 B8 16 35 15 12 53 EC 5D            ;             ~
5EC7:         10                                                       ;         is_less_equal_last_random(value) value=10
5EC8:         42                                                       ;         IF_NOT_GOTO address=5F0B
5EC9:           1F 40                                                  ;           print2(msg) size=0040
5ECB:             34 92 90 8C 77 15 0F BA 75 B1 96 14 51 18 43 C2      ;             MERLIN GESTURES AT YOU AND SAYS, "I CAN'
5EDB:             33 98 1B B7 33 BB FB 1B 10 53 F3 23 8E C5 3D 62      ;             T UNDERSTAND IT. I MUST HAVE CONJURED TH
5EEB:             50 BD 0B 58 9B C1 4F 77 66 C6 9B 15 5B CA 40 55      ;             E WRONG DEMON."
5EFB:             F4 81 F3 5F 5F BE 04 18 11 A0 FF 14 C0 93 63 F4      ;             ~
5F0B:         18                                                       ;         is_less_equal_last_random(value) value=18
5F0C:         3B                                                       ;         IF_NOT_GOTO address=5F48
5F0D:           1F 39                                                  ;           print2(msg) size=0039
5F0F:             34 92 90 8C E9 16 9E 7A C3 B5 1B BC 3E A1 6F 13      ;             MERLIN POINTS AT YOU, "EYE OF NEUTRON, W
5F1F:             1B DD C3 9E 77 98 F9 BF F3 9B 14 D0 11 BC 8A 64      ;             ART OF HOG, DEMON DO THY WILL, THEN BE G
5F2F:             0E 9F FF 14 C0 93 09 15 82 17 59 DB 46 7A 16 EE      ;             ONE!"
5F3F:             F0 72 AF 14 81 15 59 98 22                           ;             ~
5F48:   09 02                                                          ;   HIT POINTS
5F4A:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
;
; Object_27 "MerlinB"
5F4C: 06 6E                                                            ; word=06 size=006E
5F4E: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
5F51:   03 69                                                          ;   03 DESCRIPTION
5F53:     0D 67                                                        ;     while_pass: size=0067
5F55:       04 62                                                      ;       print(msg) size=0062
5F57:         83 48 8D 48 30 79 0F BC 83 48 83 7A 44 45 45 8B          ;         AN ANCIENT MAN IN A BLACK CLOAK AND POIN
5F67:         C5 83 73 8D C3 83 33 98 7B A6 BF 9A 0A 58 73 49          ;         TED HAT GESTURES AT YOU, "DEMON! I HAVE
5F77:         B5 6C 74 C0 4B 62 73 49 C7 DE FC ED EF 59 01 A0          ;         SUMMONED YOU! I AM YOUR MASTER, MERLIN!
5F87:         BB 15 58 72 55 5E 6F C5 0F A0 1B 58 19 A1 BB 15          ;         YOU MUST OBEY MY COMMAND!"
5F97:         5B 48 C7 DE 8F AF 66 49 46 62 67 16 83 B2 2B 96          ;         ~
5FA7:         C7 DE 77 16 F3 B9 2F 9E 4F DB 45 DB EF 9F 8E 48          ;         ~
5FB7:         E3 06                                                    ;         ~
5FB9:       1E 26 27                                                   ;       swap(object_a,object_b) object_a=(MerlinA)26 object_b=27(MerlinB)
;
; Object_28 "UnconsciousDoctorA"
5FBC: 07 54                                                            ; word=07 size=0054
5FBE: 00 00 80                                                         ; room=00 scorePoints=00 bits=80
5FC1:   03 27                                                          ;   03 DESCRIPTION
5FC3:     04 25                                                        ;     print(msg) size=0025
5FC5:       5F BE 7C 13 8E 5F 86 19 66 9E A3 A0 03 BA F3 8C            ;       THE "REAL" DOCTOR STILL LIES UNCONSCIOUS
5FD5:       87 8C D7 B5 21 98 95 9A C7 7A CB B5 96 96 DB 72            ;       IN THE CORNER.
5FE5:       44 55 74 98 2E                                             ;       ~
5FEA:   02 0C                                                          ;   02 SHORT_NAME
5FEC:     8D C5 0D A0 C7 7A C6 B5 66 9E A3 A0                          ;     UNCONCIOUS DOCTOR
5FF8:   0B 14                                                          ;   0B COMMAND HANDLING IF GIVEN COMMAND
5FFA:     1F 12                                                        ;     print2(msg) size=0012
5FFC:       5F BE 09 15 09 56 8B AF D7 B5 21 98 95 9A C7 7A            ;       THE DOCTOR IS UNCONSCIOUS.
600C:       5B BB                                                      ;       ~
600E:   09 02                                                          ;   HIT POINTS
6010:   46 01                                                          ;   maxHitPoints=46 currentHitPoints=01
;
; Object_29 "UnconsciousDoctorB"
6012: 07 80 F5                                                         ; word=07 size=00F5
6015: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
6018:   03 80 EF                                                       ;   03 DESCRIPTION
601B:     0D 80 EC                                                     ;     while_pass: size=00EC
601E:       04 80 E6                                                   ;       print(msg) size=00E6
6021:         5F BE 5B B1 4B 7B 4F 45 83 48 83 7A 55 45 EB BF          ;         THERE IS A MAN IN A STRAIT JACKET IN THE
6031:         73 7B C5 7E B6 85 D0 15 82 17 45 5E B8 A0 47 62          ;         CORNER. HE LOOKS UP AT YOU AND MUMBLES,
6041:         9F 15 49 16 A5 9F B2 17 96 14 51 18 43 C2 33 98          ;         "OH...IT IS TERRIBLE...THE DOCTOR HAS B
6051:         AF 94 7F 4E 33 BB FA 1C FF F9 73 7B 4B 7B F4 BD          ;         ECOME THE PATIENT AND THE PATIENT THE DO
6061:         04 B2 FF 8B F6 F9 DB 72 75 5B 84 BF 9B 15 C4 B5          ;         CTOR...LISTEN TO ME...I AM THE DOCTOR...
6071:         E1 5F 1B 92 5F BE DB 16 87 BE B3 9A 8E 48 82 17          ;         YOU MUST GO TO THE AUTHORITIES AND TELL
6081:         52 5E 83 49 9E 61 82 17 46 5E 66 9E C7 A0 EE F9          ;         THEM OF THIS TRAVESTY! HURRY, BEFORE IT
6091:         66 7B 83 61 6B BF 3F 92 EB F9 8F 14 82 17 46 5E          ;         IS TOO LATE." HIS EYES ROLL BACK INTO HI
60A1:         66 9E C7 A0 FB F9 1B A1 B5 94 09 BC D6 9C D6 9C          ;         S HEAD AND HE PASSES OUT.
60B1:         DB 72 B6 49 84 74 83 7B 4B 62 8E 48 7F 17 F3 8C          ;         ~
60C1:         5F BE 51 90 96 64 95 73 8C 17 CF 49 13 BA CA 06          ;         ~
60D1:         3C C6 B3 E0 68 4D AF A0 D6 15 D5 15 89 17 CE 9C          ;         ~
60E1:         7F 49 63 F4 95 73 3B 15 4B 62 FE B2 04 8A DD 46          ;         ~
60F1:         D0 15 6B BF 95 73 9F 15 F3 46 8E 48 9F 15 DB 16          ;         ~
6101:         D7 B9 D1 B5 97 C6                                        ;         ~
6107:       1E 28 29                                                   ;       swap(object_a,object_b) object_a=(UnconsciousDoctorA)28 object_b=29(UnconsciousDoctorB)
;
; Object_2A "HoudiniA"
610A: 04 81 0A                                                         ; word=04 size=010A
610D: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
6110:   03 29                                                          ;   03 DESCRIPTION
6112:     04 27                                                        ;     print(msg) size=0027
6114:       87 74 90 5A 4B 77 D9 B5 16 B2 90 73 5B 70 FD 1B            ;       HOUDINI IS WRITHING. "I'LL BE DOWN FROM
6124:       F3 8C 5B 4D 89 5B 88 96 FF B2 9F 15 5B B1 83 7A            ;       HERE IN A MINUTE!"
6134:       4F 45 9F 7A D9 BD 22                                       ;       ~
613B:   02 05                                                          ;   02 SHORT_NAME
613D:     87 74 90 5A 49                                               ;     HOUDINI
6142:   07 80 CB                                                       ;   07 COMMAND HANDLING IF FIRST NOUN
6145:     0D 80 C8                                                     ;     while_pass: size=00C8
6148:       0E 04                                                      ;       while_fail: size=0004
614A:         0A 48                                                    ;         compare_input_to(phrase) phrase="48: LOWER u....... * *"
614C:         0A 12                                                    ;         compare_input_to(phrase) phrase="12: PULL u....... * *"
614E:       04 80 BC                                                   ;       print(msg) size=00BC
6151:         C7 DE 3F 16 0A BC 26 A1 93 7A 09 15 26 D2 BF 14          ;         YOU LET HOUDINI DOWN, BUT YOU ARE UNABLE
6161:         1B BC 1B A1 2F 49 B0 17 B6 46 56 5E D4 9C 71 61          ;         TO REMOVE HIS STRAIT JACKET. HOUDINI SA
6171:         5B CA 95 73 66 17 CB B0 0C BC DD 46 97 62 A9 15          ;         YS, "YOU DIDN'T HAVE TO DO THAT! I WOULD
6181:         03 C4 FB 98 1B B7 33 BB 91 1E 46 C2 08 79 F3 23          ;         HAVE BEEN DOWN IN A MINUTE. BUT I'LL ST
6191:         58 72 56 5E C6 9C D6 9C 56 72 CB 06 01 18 3E C5          ;         ILL TAKE YOU WITH ME WHEN I ESCAPE, JUST
61A1:         9B 15 5B CA 67 4D 86 96 80 A1 D0 15 7B 14 D0 92          ;         AS SOON AS I GET OUT OF THIS THING!" HE
61B1:         7F C6 44 F4 73 C6 9E 77 15 8A 8E BE 16 8A 17 48          ;         BEGINS WRESTLING WITH HIS STRAIT JACKET
61C1:         51 18 59 C2 82 7B 67 16 FA 17 83 61 47 77 53 B7          ;         .
61D1:         FE A4 FF 15 F3 B9 4B 49 41 B9 83 96 CB B5 77 15          ;         ~
61E1:         11 BC 73 C6 C3 9E 63 BE D6 B5 90 73 6C 6A 9F 15          ;         ~
61F1:         AF 14 50 6D D9 B5 75 B1 03 BF AB 98 56 D1 0A 71          ;         ~
6201:         4B 7B 0C BA D6 47 EB 15 97 54 9B C1                      ;         ~
620D:       1E 2A 2C                                                   ;       swap(object_a,object_b) object_a=(HoudiniA)2A object_b=2C(HoudiniC)
6210:   0B 01                                                          ;   0B COMMAND HANDLING IF GIVEN COMMAND
6212:     9A                                                           ;     9A(??CommandResponse)
6213:   09 02                                                          ;   HIT POINTS
6215:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
;
; Object_2B "HoudiniB"
6217: 04 80 D9                                                         ; word=04 size=00D9
621A: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
621D:   03 80 D3                                                       ;   03 DESCRIPTION
6220:     0D 80 D0                                                     ;     while_pass: size=00D0
6223:       04 80 CA                                                   ;       print(msg) size=00CA
6226:         5F BE 5B B1 4B 7B 48 45 98 C5 4E DB 3D A0 91 7A          ;         THERE IS A FUNNY LOOKING MAN HANGING TIE
6236:         63 16 8A 96 91 48 91 7A 83 17 F3 5F 56 D1 03 71          ;         D WITH A ROPE BY HIS FEET TO THE CEILING
6246:         39 17 DB A4 7B 50 95 73 4F 15 73 62 6B BF 5F BE          ;         . HE IS WEARING A STRAIT JACKET. HE TURN
6256:         D7 14 43 7A CF 98 9F 15 D5 15 F7 17 33 49 AB 98          ;         S HIS HEAD TOWARD YOU, "HELLO! I AM THE
6266:         55 45 EB BF 73 7B C5 7E B6 85 4A F4 56 5E 38 C6          ;         GREAT HOUDINI! NO BONDS CAN HOLD ME, NO
6276:         CA B5 4B 7B E3 72 16 58 73 A1 33 B1 C7 DE FC ED          ;         LOCKS CAN RESIST ME! WAIT, LET ME SHOW Y
6286:         EE 72 69 8D BB 15 5B 48 5F BE 84 15 96 5F A9 15          ;         OU! I CAN GET US BOTH OUT OF THIS PLACE!
6296:         03 C4 F9 98 99 16 B9 14 4D 98 D3 14 8A 96 BE 9F          ;         " HE BEGINS WRIGGLING.
62A6:         67 16 10 EE CE 9C 5D 9E C5 B5 83 48 75 B1 66 7B          ;         ~
62B6:         67 16 D9 06 D6 47 0E EE 73 62 1B 92 29 B8 DB CE          ;         ~
62C6:         19 A1 BB 15 10 53 77 15 17 BC C4 B5 02 A1 C7 16          ;         ~
62D6:         11 BC 96 64 95 73 E6 16 D7 46 E3 06 DB 72 69 4D          ;         ~
62E6:         9D 7A 04 18 79 79 90 8C 5B 70                            ;         ~
62F0:       1E 2A 2B                                                   ;       swap(object_a,object_b) object_a=(HoudiniA)2A object_b=2B(HoudiniB)
;
; Object_2C "HoudiniC"
62F3: 04 80 93                                                         ; word=04 size=0093
62F6: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
62F9:   03 36                                                          ;   03 DESCRIPTION
62FB:     04 34                                                        ;     print(msg) size=0034
62FD:       87 74 90 5A 4B 77 D9 B5 75 B1 03 BF AB 98 56 D1            ;       HOUDINI IS WRESTLING WITH HIS STRAIT JAC
630D:       0A 71 4B 7B 0C BA D6 47 EB 15 97 54 9B C1 FD 1B            ;       KET. "I'LL BE OUT OF THIS IN NO TIME!"
631D:       F3 8C 5B 4D 36 A1 B8 16 82 17 4B 7B 83 7A EB 99            ;       ~
632D:       8F BE EC 5D                                                ;       ~
6331:   02 05                                                          ;   02 SHORT_NAME
6333:     87 74 90 5A 49                                               ;     HOUDINI
6338:   08 45                                                          ;   08 TURN SCRIPT
633A:     0E 43                                                        ;     while_fail: size=0043
633C:       0D 04                                                      ;       while_pass: size=0004
633E:         9C                                                       ;         9C(??MoveHoudiniC)
633F:         1C 2C                                                    ;         set_VAR(object) object=2C(HoudiniC)
6341:         9E                                                       ;         9E(PrintObjectEntersRoom)
6342:       0B 3B 05                                                   ;       switch(is_less_equal_last_random(value)): size=003B
6345:         08                                                       ;         is_less_equal_last_random(value) value=08
6346:         1A                                                       ;         IF_NOT_GOTO address=6361
6347:           1F 18                                                  ;           print2(msg) size=0018
6349:             87 74 90 5A 4F 77 64 C5 F5 8B FC ED A3 48 6B 16      ;             HOUDINI MUMBLES, "ANY MINUTE NOW..."
6359:             F6 9A 50 5E 8F A1 DC F9                              ;             ~
6361:         10                                                       ;         is_less_equal_last_random(value) value=10
6362:         1C                                                       ;         IF_NOT_GOTO address=637F
6363:           1F 1A                                                  ;           print2(msg) size=001A
6365:             87 74 90 5A 46 77 DE 5F 2F 49 33 BB FD 1B 5B CA      ;             HOUDINI DECLARES, "I'VE ALMOST GOT IT!"
6375:             47 48 E6 A0 81 15 0B BC AC BB                        ;             ~
637F:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
6381:     AB                                                           ;     AB(AttackPerson)
6382:   0B 01                                                          ;   0B COMMAND HANDLING IF GIVEN COMMAND
6384:     9A                                                           ;     9A(??CommandResponse)
6385:   09 02                                                          ;   HIT POINTS
6387:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
;
; Object_2D "Woman"
6389: 01 81 CA                                                         ; word=01 size=01CA
638C: 8E 00 90                                                         ; room=8E scorePoints=00 bits=90
638F:   03 60                                                          ;   03 DESCRIPTION
6391:     04 5E                                                        ;     print(msg) size=005E
6393:       5F BE 5B B1 4B 7B 58 45 43 62 3B 16 B7 B1 01 18            ;       THERE IS A VERY LARGE WOMAN DRESSED IN A
63A3:       90 91 0C 15 65 62 F3 5F 83 7A 57 45 08 99 B7 A0            ;       UNIFORM HERE. SHE LOOKS LIKE THE ROLLER
63B3:       9F 15 7F B1 5A 17 4E 5E 3D A0 CE B5 17 7A 82 17            ;       DERBY QUEEN. SHE HAS A JAGGED SCAR JUST
63C3:       54 5E C6 9F 23 62 F4 59 7B 50 A7 AD A7 61 5A 17            ;       BELOW HER HAIRLINE.
63D3:       4A 5E 4B 49 4C 45 79 47 F3 5F 53 B7 8C AF 66 C6            ;       ~
63E3:       AF 14 89 8D 9F 15 8A AF D4 47 90 8C DB 63                  ;       ~
63F1:   02 06                                                          ;   02 SHORT_NAME
63F3:     5F BE 9F 16 97 B3                                            ;     THE NURSE
63F9:   0B 01                                                          ;   0B COMMAND HANDLING IF GIVEN COMMAND
63FB:     9A                                                           ;     9A(??CommandResponse)
63FC:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
63FE:     AB                                                           ;     AB(AttackPerson)
63FF:   08 81 50                                                       ;   08 TURN SCRIPT
6402:     0D 81 4D                                                     ;     while_pass: size=014D
6405:       01 13                                                      ;       is_in_pack_or_current_room(object) object=13(PLAYER)
6407:       0E 81 48                                                   ;       while_fail: size=0148
640A:         0D 71                                                    ;         while_pass: size=0071
640C:           0A 03                                                  ;           compare_input_to(phrase) phrase="03: EAST * * *"
640E:           1F 6D                                                  ;           print2(msg) size=006D
6410:             1F B8 8F 17 DD B2 89 17 14 D0 1B 58 1B A1 8E 48      ;             SHE TURNS TOWARD YOU AND SAYS, "OH! YOU
6420:             53 17 6E DF 79 13 AB 70 C7 DE 77 16 F3 B9 5B 4D      ;             MUST BE HERE FOR TREATMENT. JUST COME RI
6430:             F4 72 48 5E A3 A0 EF BF 87 49 9E 61 4C F4 66 C6      ;             GHT OVER HERE..." SHE GESTURES TOWARD SO
6440:             E1 14 1B 92 09 B2 33 75 4F A1 8A AF 2F 62 FF F9      ;             METHING WHICH LOOKS LIKE AN ELECTRIC COU
6450:             95 19 DB 72 B5 6C 74 C0 4B 62 89 BF 2E 49 61 17      ;             CH.
6460:             36 92 90 73 D9 6A 85 73 0E 71 3D A0 CE B5 17 7A      ;             ~
6470:             90 14 2E 15 E6 5F 05 B2 E1 14 DA C3 2E               ;             ~
647D:         0D 80 D2                                                 ;         while_pass: size=00D2
6480:           1F 73                                                  ;           print2(msg) size=0073
6482:             91 1E A4 C2 50 5E F3 A0 41 55 F4 A4 83 49 CF 98      ;             "YOU'RE NOT COOPERATING...", SAYS THE NU
6492:             DC F9 15 EE 55 4A 82 17 50 5E 3D C6 43 5E D5 B5      ;             RSE AS SHE LUNGES ACROSS THE ROOM AND TA
64A2:             DB 72 70 8E B5 6C 85 14 05 B3 D6 B5 DB 72 01 B3      ;             CKLES YOU. SHE DRAGS YOU TO THE COUCH AN
64B2:             43 90 33 98 45 BD BF 86 DB B5 3F A1 5A 17 46 5E      ;             D STRAPS YOU IN. THEN SHE PULLS AN OMINO
64C2:             C9 B0 DB B5 1B A1 6B BF 5F BE E1 14 DA C3 90 14      ;             US LEVER AND
64D2:             15 58 EB BF 0B A7 C7 DE D0 15 56 F4 F0 72 5A 17      ;             ~
64E2:             52 5E 46 C5 C3 B5 91 96 D0 92 35 A1 3F 16 74 CA      ;             ~
64F2:             90 14 44                                             ;             ~
64F5:           0E 24                                                  ;           while_fail: size=0024
64F7:             03 13 3A                                             ;             is_located(room,object) room=13(Room_13) object=3A(Object3A)
64FA:             1F 1F                                                ;             print2(msg) size=001F
64FC:               C7 DE 3A 15 F4 A4 30 79 9B 53 5F BE AE 17 8F BE    ;               YOU EXPERIENCE THE ULTIMATE AGONY! MERCI
650C:               7F 49 89 14 23 A0 CF 06 2D 62 5F 79 13 8D 2C       ;               FULLY,
651B:           1F 0A                                                  ;           print2(msg) size=000A
651D:             C7 DE DB 16 CB B9 36 A1 FF F9                        ;             YOU PASS OUT...
6527:           2C 13                                                  ;           set_ACTIVE(object) object=13(PLAYER)
6529:           19 88                                                  ;           move_ACTIVE(room) room=88(Small square room)
652B:           17 1B 8E                                               ;           move_to(object,room) object=1B(GreenKeyA) room=8E(Electroshock room)
652E:           17 41 8C                                               ;           move_to(object,room) object=41(GreenKeyB) room=8C(East end east-west hall)
6531:           1C 05                                                  ;           set_VAR(object) object=05(GreenDoorC)
6533:           0E 03                                                  ;           while_fail: size=0003
6535:             15 02                                                ;             check_VAR(bits) bits=02(......O.)
6537:             29                                                   ;             print_open_VAR()
6538:           1C 06                                                  ;           set_VAR(object) object=06(GreedDoorD)
653A:           0E 04                                                  ;           while_fail: size=0004
653C:             14                                                   ;             execute_and_reverse_status:
653D:             15 02                                                ;             check_VAR(bits) bits=02(......O.)
653F:             29                                                   ;             print_open_VAR()
6540:           1F 10                                                  ;           print2(msg) size=0010
6542:             C7 DE 99 14 17 48 8B 96 9B 96 34 A1 D7 14 17 8D      ;             YOU AWAKEN IN YOUR CELL.
6552:   09 02                                                          ;   HIT POINTS
6554:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
;
; Object_2E "Doctor"
6556: 07 81 AE                                                         ; word=07 size=01AE
6559: 00 00 90                                                         ; room=00 scorePoints=00 bits=90
655C:   03 01                                                          ;   03 DESCRIPTION
655E:     9F                                                           ;     9F(PrintUnshavenMan)
655F:   02 07                                                          ;   02 SHORT_NAME
6561:     5F BE 09 15 09 56 52                                         ;     THE DOCTOR
6568:   08 81 95                                                       ;   08 TURN SCRIPT
656B:     0E 81 92                                                     ;     while_fail: size=0192
656E:       0D 1C                                                      ;       while_pass: size=001C
6570:         14                                                       ;         execute_and_reverse_status:
6571:         01 13                                                    ;         is_in_pack_or_current_room(object) object=13(PLAYER)
6573:         9B                                                       ;         9B(??PrintDirs)
6574:         1F 15                                                    ;         print2(msg) size=0015
6576:           C7 DE 9F 15 23 49 50 45 55 9F 43 5E 33 98 C7 DE        ;           YOU HEAR A NOISE AND YOU NOTICE
6586:           99 16 85 BE 45                                         ;           ~
658B:         9F                                                       ;         9F(PrintUnshavenMan)
658C:       0D 81 71                                                   ;       while_pass: size=0171
658F:         01 13                                                    ;         is_in_pack_or_current_room(object) object=13(PLAYER)
6591:         1F 0C                                                    ;         print2(msg) size=000C
6593:           5F BE 09 15 09 56 95 AF 55 4A FB ED                    ;           THE DOCTOR SAYS,
659F:         0B 81 5E 05                                              ;         switch(is_less_equal_last_random(value)): size=015E
65A3:           33                                                     ;           is_less_equal_last_random(value) value=33
65A4:           42                                                     ;           IF_NOT_GOTO address=65E7
65A5:             1F 40                                                ;             print2(msg) size=0040
65A7:               91 1E 43 C2 5B B1 06 9A AF 14 91 7A 7B 14 41 6E    ;               "YOU ARE NOT BEING A GOOD LITTLE PATIENT
65B7:               0E 58 8E 7B DB 8B 56 A4 30 79 AB BB 09 9A 2F 17    ;               ! NOW RETURN TO YOUR CELL, OR YOU WILL N
65C7:               74 C0 96 96 DB 9C 34 A1 D7 14 16 8D C4 16 51 18    ;               EED A LOBOTOMY!"
65D7:               59 C2 46 7A 8F 16 F3 5F 4E 45 39 9E 7F BF EC DA    ;               ~
65E7:           66                                                     ;           is_less_equal_last_random(value) value=66
65E8:           20                                                     ;           IF_NOT_GOTO address=6609
65E9:             1F 1E                                                ;             print2(msg) size=001E
65EB:               FB 1B B9 6E D6 CE 2F 7B 11 58 86 64 8E 5F 91 7A    ;               "I GROW TIRED OF DEALING WITH YOU INFERI
65FB:               FB 17 53 BE C7 DE D0 15 74 66 C4 7A 6C B5          ;               ORS!"
6609:           99                                                     ;           is_less_equal_last_random(value) value=99
660A:           22                                                     ;           IF_NOT_GOTO address=662D
660B:             1F 20                                                ;             print2(msg) size=0020
660D:               3A 1E 73 49 2F 49 51 18 46 C2 50 9F CA 6A 2F 62    ;               "WHAT ARE YOU DOING HERE? GO WHERE YOU B
661D:               89 00 D9 9C F4 72 5B 5E 1B A1 6E 4D 11 A0 E3 06    ;               ELONG!"
662D:           FF                                                     ;           is_less_equal_last_random(value) value=FF
662E:           80 D0                                                  ;           IF_NOT_GOTO address=66FF
6630:             0D 80 CD                                             ;             while_pass: size=00CD
6633:               1F 80 B4                                           ;               print2(msg) size=00B4
6636:                 FD 1B 43 90 6B 68 F3 78 9F 77 81 15 91 7A 89 17  ;                 "I'M AFRAID I'M GOING TO HAVE TO GIVE YO
6646:                 9B 15 5B CA 6B BF 58 6D 5B 5E 1B A1 48 45 00 B3  ;                 U A FRONTAL LOBOTOMY!" HE STICKS YOU WIT
6656:                 4E BD 49 16 06 4F FB 9F E3 06 DB 72 03 BA A5 54  ;                 H HIS HYPO AND YOU PASS OUT. WHEN YOU AW
6666:                 51 18 59 C2 82 7B A3 15 CA B5 E9 DE 90 14 1B 58  ;                 AKEN, YOU FEEL SOMEWHAT INDIFFERENT TO Y
6676:                 1B A1 55 A4 D1 B5 97 C6 FA 17 83 61 C7 DE 99 14  ;                 OUR SURROUNDINGS. YOU NOTICE BLOOD ON YO
6686:                 17 48 F3 9B C7 DE 4F 15 33 61 3F B9 FA 62 73 49  ;                 UR GOWN, BUT IT DOESN'T SEEM TO BOTHER Y
6696:                 8E 7A 50 79 2F 62 B3 9A 6B BF C7 DE 95 AF 3C C6  ;                 OU. YOU FEEL LIKE WANDERING...
66A6:                 30 A1 90 5A EF 6E 51 18 50 C2 03 A1 9B 53 89 4E  ;                 ~
66B6:                 73 9E 03 A0 C7 DE 89 AF 80 A1 04 EE 73 C6 73 7B  ;                 ~
66C6:                 77 5B 05 B9 15 BC 2F 60 89 17 B9 14 5F BE 9B AF  ;                 ~
66D6:                 3F A1 51 18 48 C2 2E 60 43 16 9B 85 10 D0 F4 59  ;                 ~
66E6:                 91 7A FF F9                                      ;                 ~
66EA:               1C 05                                              ;               set_VAR(object) object=05(GreenDoorC)
66EC:               0E 03                                              ;               while_fail: size=0003
66EE:                 15 02                                            ;                 check_VAR(bits) bits=02(......O.)
66F0:                 29                                               ;                 print_open_VAR()
66F1:               1C 06                                              ;               set_VAR(object) object=06(GreedDoorD)
66F3:               0E 04                                              ;               while_fail: size=0004
66F5:                 14                                               ;                 execute_and_reverse_status:
66F6:                 15 02                                            ;                 check_VAR(bits) bits=02(......O.)
66F8:                 29                                               ;                 print_open_VAR()
66F9:               2C 13                                              ;               set_ACTIVE(object) object=13(PLAYER)
66FB:               17 3A 13                                           ;               move_to(object,room) object=3A(Object3A) room=13(Room_13)
66FE:               19 88                                              ;               move_ACTIVE(room) room=88(Small square room)
6700:   0B 01                                                          ;   0B COMMAND HANDLING IF GIVEN COMMAND
6702:     9A                                                           ;     9A(??CommandResponse)
6703:   09 02                                                          ;   HIT POINTS
6705:   46 46                                                          ;   maxHitPoints=46 currentHitPoints=46
;
; Object_2F "Walls"
6707: 25 0C                                                            ; word=25 size=000C
6709: FF 00 80                                                         ; room=FF scorePoints=00 bits=80
670C:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
670E:     A4                                                           ;     A4(PrintPicassoDoor)
670F:   02 04                                                          ;   02 SHORT_NAME
6711:     0E D0 0B 8E                                                  ;     WALLS
;
; Object_30 "Room"
6715: 2A 0B                                                            ; word=2A size=000B
6717: FF 00 80                                                         ; room=FF scorePoints=00 bits=80
671A:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
671C:     A4                                                           ;     A4(PrintPicassoDoor)
671D:   02 03                                                          ;   02 SHORT_NAME
671F:     01 B3 4D                                                     ;     ROOM
;
; Object_31 "Floor"
6722: 2B 09                                                            ; word=2B size=0009
6724: FF 00 80                                                         ; room=FF scorePoints=00 bits=80
6727:   02 04                                                          ;   02 SHORT_NAME
6729:     89 67 A3 A0                                                  ;     FLOOR
;
; Object_32 "Exit"
672D: 2C 08                                                            ; word=2C size=0008
672F: FF 00 80                                                         ; room=FF scorePoints=00 bits=80
6732:   02 03                                                          ;   02 SHORT_NAME
6734:     23 63 54                                                     ;     EXIT
;
; Object_33 "Corner"
6737: 30 0C                                                            ; word=30 size=000C
6739: FF 00 80                                                         ; room=FF scorePoints=00 bits=80
673C:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
673E:     A4                                                           ;     A4(PrintPicassoDoor)
673F:   02 04                                                          ;   02 SHORT_NAME
6741:     44 55 74 98                                                  ;     CORNER
;
; Object_34 "Hallway"
6745: 33 0D                                                            ; word=33 size=000D
6747: FF 00 80                                                         ; room=FF scorePoints=00 bits=80
674A:   07 01                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
674C:     A4                                                           ;     A4(PrintPicassoDoor)
674D:   02 05                                                          ;   02 SHORT_NAME
674F:     4E 72 B3 8E 59                                               ;     HALLWAY
;
; Object_35 "Entrance"
6754: 36 0B                                                            ; word=36 size=000B
6756: FF 00 80                                                         ; room=FF scorePoints=00 bits=80
6759:   02 06                                                          ;   02 SHORT_NAME
675B:     9E 61 D0 B0 9B 53                                            ;     ENTRANCE
;
; Object_36 "Ceiling"
6761: 3B 0A                                                            ; word=3B size=000A
6763: FF 00 80                                                         ; room=FF scorePoints=00 bits=80
6766:   02 05                                                          ;   02 SHORT_NAME
6768:     AB 53 90 8C 47                                               ;     CEILING
;
; Object_37 "Hands"
676D: 1F 09                                                            ; word=1F size=0009
676F: 13 00 C0                                                         ; room=13 scorePoints=00 bits=C0
6772:   02 04                                                          ;   02 SHORT_NAME
6774:     50 72 0B 5C                                                  ;     HANDS
;
; Object_38 "SYSTEM"
6778: 20 03                                                            ; word=20 size=0003
677A: 00 00 80                                                         ; room=00 scorePoints=00 bits=80
;
; Object_39 "BluePillB"
677D: 17 32                                                            ; word=17 size=0032
677F: 82 00 A0                                                         ; room=82 scorePoints=00 bits=A0
6782:   03 01                                                          ;   03 DESCRIPTION
6784:     9D                                                           ;     9D(PrintBluePill)
6785:   07 22                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
6787:     0D 20                                                        ;     while_pass: size=0020
6789:       0A 15                                                      ;       compare_input_to(phrase) phrase="15: EAT u....... * *"
678B:       04 1C                                                      ;       print(msg) size=001C
678D:         2E 6F AB A2 37 6E C6 B5 80 A1 9B 15 31 B1 47 18          ;         GULP! GOES DOWN HARD! YECCH, TASTES AWFU
679D:         5A 53 16 EE 66 49 4B 62 F8 49 31 C5                      ;         L!
67A9:   02 06                                                          ;   02 SHORT_NAME
67AB:     8F 4E 52 5E 46 7A                                            ;     BLUE PILL
;
; Object_3A "Object3A"
67B1: 3C 03                                                            ; word=3C size=0003
67B3: 00 00 00                                                         ; room=00 scorePoints=00 bits=00
;
; Object_3B "RedKeyB"
67B6: 16 80 85                                                         ; word=16 size=0085
67B9: 82 00 80                                                         ; room=82 scorePoints=00 bits=80
67BC:   02 05                                                          ;   02 SHORT_NAME
67BE:     66 B1 17 16 59                                               ;     RED KEY
67C3:   01 01                                                          ;   01 ADJECTIVES
67C5:   13                                                             ;   TODO WORD
67C6:   07 76                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
67C8:     0E 74                                                        ;     while_fail: size=0074
67CA:       0D 30                                                      ;       while_pass: size=0030
67CC:         0A 43                                                    ;         compare_input_to(phrase) phrase="43: GET ..C..... WITH ..C....."
67CE:         09 16                                                    ;         compare_to_second_noun(object) object=16(WindowHook)
67D0:         03 82 3B                                                 ;         is_located(room,object) room=82(Dispensary) object=3B(RedKeyB)
67D3:         03 00 14                                                 ;         is_located(room,object) room=00(Room_00) object=14(RedKeyA)
67D6:         17 3B 00                                                 ;         move_to(object,room) object=3B(RedKeyB) room=00(Room_00)
67D9:         17 14 13                                                 ;         move_to(object,room) object=14(RedKeyA) room=13(Room_13)
67DC:         04 1E                                                    ;         print(msg) size=001E
67DE:           C7 DE 77 15 16 BC DB 72 BB 85 FB 17 53 BE 5F BE        ;           YOU GET THE KEY WITH THE HOOK. RED KEY T
67EE:           A9 15 AF 9F 2F 17 0D 58 3B 63 4D BD A7 61              ;           AKEN.
67FC:       0D 24                                                      ;       while_pass: size=0024
67FE:         0A 05                                                    ;         compare_input_to(phrase) phrase="05: GET ..C..... * *"
6800:         04 20                                                    ;         print(msg) size=0020
6802:           C7 DE D3 14 90 96 F3 A0 85 A6 44 B8 FB 8E 63 B1        ;           YOU CAN NOT POSSIBLY REACH INTO THAT TIN
6812:           13 54 9E 7A D6 9C 56 72 83 17 7B 9B 7E 74 EB 5D        ;           Y HOLE!
6822:       0D 1A                                                      ;       while_pass: size=001A
6824:         0A 43                                                    ;         compare_input_to(phrase) phrase="43: GET ..C..... WITH ..C....."
6826:         04 14                                                    ;         print(msg) size=0014
6828:           C7 DE D3 14 E6 96 77 15 16 BC DB 72 66 B1 17 16        ;           YOU CAN'T GET THE RED KEY WITH
6838:           59 DB 82 7B                                            ;           ~
683C:         A9                                                       ;         A9(PrintTheSecondNoun)
683D:         8B                                                       ;         8B(PrintPeriod)
;
; Object_3C "DeadDog"
683E: 08 20                                                            ; word=08 size=0020
6840: 00 00 A0                                                         ; room=00 scorePoints=00 bits=A0
6843:   02 06                                                          ;   02 SHORT_NAME
6845:     E3 59 06 58 EB 9E                                            ;     DEAD DOG
684B:   03 13                                                          ;   03 DESCRIPTION
684D:     04 11                                                        ;     print(msg) size=0011
684F:       5F BE 5B B1 4B 7B 46 45 86 5F 09 15 CA 6A 2F 62            ;       THERE IS A DEAD DOG HERE.
685F:       2E                                                         ;       ~
;
; Object_3D "SecretDoor"
6860: 0B 42                                                            ; word=0B size=0042
6862: 00 00 8A                                                         ; room=00 scorePoints=00 bits=8A
6865:   07 30                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
6867:     0D 2E                                                        ;     while_pass: size=002E
6869:       0A 11                                                      ;       compare_input_to(phrase) phrase="11: OPEN ......O. * *"
686B:       04 2A                                                      ;       print(msg) size=002A
686D:         5F BE 57 17 AF 55 06 BC 44 A0 D5 15 66 17 DD C3          ;         THE SECRET DOOR IS STUCK. YOU ARE NOT ST
687D:         5B F4 1B A1 2F 49 99 16 15 BC F9 BF AB 98 99 61          ;         RONG ENOUGH TO OPEN IT.
688D:         7A C4 89 17 C2 16 83 61 97 7B                            ;         ~
6897:   02 08                                                          ;   02 SHORT_NAME
6899:     A5 B7 76 B1 09 15 A3 A0                                      ;     SECRET DOOR
68A1:   01 01                                                          ;   01 ADJECTIVES
68A3:   3D                                                             ;   TODO WORD
;
; Object_3E "PaintedDoorA"
68A4: 0B 76                                                            ; word=0B size=0076
68A6: 00 00 8A                                                         ; room=00 scorePoints=00 bits=8A
68A9:   02 08                                                          ;   02 SHORT_NAME
68AB:     4B A4 BF 9A 06 58 44 A0                                      ;     PAINTED DOOR
68B3:   03 24                                                          ;   03 DESCRIPTION
68B5:     04 22                                                        ;     print(msg) size=0022
68B7:       03 A0 5F BE 99 16 C2 B3 F3 17 F3 8C 4B 7B 0F A0            ;       ON THE NORTH WALL IS ONE OF PICASSO'S PA
68C7:       B8 16 E3 16 15 53 2D B9 D2 B5 D0 47 E6 BD 09 15            ;       INTED DOORS
68D7:       BD A0                                                      ;       ~
68D9:   07 3E                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
68DB:     0D 3C                                                        ;     while_pass: size=003C
68DD:       0E 0A                                                      ;       while_fail: size=000A
68DF:         0A 11                                                    ;         compare_input_to(phrase) phrase="11: OPEN ......O. * *"
68E1:         0A 3A                                                    ;         compare_input_to(phrase) phrase="3A: OPEN ......O. WITH u......."
68E3:         0A 41                                                    ;         compare_input_to(phrase) phrase="41: LOCK ....A... WITH u......."
68E5:         0A 42                                                    ;         compare_input_to(phrase) phrase="42: UNLOCK .......L WITH u......."
68E7:         0A 40                                                    ;         compare_input_to(phrase) phrase="40: CLOSE ....A... * *"
68E9:       04 2D                                                      ;       print(msg) size=002D
68EB:         5F BE DB 16 9E 7A F3 5F 81 5B 91 AF F0 A4 D6 B5          ;         THE PAINTED DOOR OPENS TO REVEAL AN ESCA
68FB:         D4 9C CF 62 33 48 83 48 55 62 DF 48 39 17 7F C6          ;         PE ROUTE! YOU HAVE ESCAPED!
690B:         DB 06 1B A1 58 72 47 5E 53 B7 E6 A4 21                   ;         ~
6918:       24                                                         ;       endless_loop()
6919:   01 01                                                          ;   01 ADJECTIVES
691B:   3E                                                             ;   TODO WORD
;
; Object_3F "PaintedDoorB"
691C: 0B 3E                                                            ; word=0B size=003E
691E: 00 00 80                                                         ; room=00 scorePoints=00 bits=80
6921:   02 08                                                          ;   02 SHORT_NAME
6923:     4B A4 BF 9A 06 58 44 A0                                      ;     PAINTED DOOR
692B:   07 2C                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
692D:     0D 2A                                                        ;     while_pass: size=002A
692F:       0E 0A                                                      ;       while_fail: size=000A
6931:         0A 11                                                    ;         compare_input_to(phrase) phrase="11: OPEN ......O. * *"
6933:         0A 3A                                                    ;         compare_input_to(phrase) phrase="3A: OPEN ......O. WITH u......."
6935:         0A 40                                                    ;         compare_input_to(phrase) phrase="40: CLOSE ....A... * *"
6937:         0A 41                                                    ;         compare_input_to(phrase) phrase="41: LOCK ....A... WITH u......."
6939:         0A 42                                                    ;         compare_input_to(phrase) phrase="42: UNLOCK .......L WITH u......."
693B:       04 1C                                                      ;       print(msg) size=001C
693D:         2F 49 51 18 45 C2 DC B0 C3 DA 73 7B 4B 7B F5 81          ;         ARE YOU CRAZY? IT IS JUST A PAINTED DOOR
694D:         03 BC DB 16 9E 7A F3 5F 81 5B 2B AF                      ;         !
6959:   01 01                                                          ;   01 ADJECTIVES
695B:   3E                                                             ;   TODO WORD
;
; Object_40 "GreenDoorI"
695C: 0B 12                                                            ; word=0B size=0012
695E: 99 00 8B                                                         ; room=99 scorePoints=00 bits=8B
6961:   03 01                                                          ;   03 DESCRIPTION
6963:     86                                                           ;     86(PrintNorthWallGreedDoor)
6964:   01 01                                                          ;   01 ADJECTIVES
6966:   14                                                             ;   TODO WORD
6967:   02 07                                                          ;   02 SHORT_NAME
6969:     AF 6E 83 61 81 5B 52                                         ;     GREEN DOOR
;
; Object_41 "GreenKeyB"
6970: 16 80 89                                                         ; word=16 size=0089
6973: 8C 00 80                                                         ; room=8C scorePoints=00 bits=80
6976:   02 06                                                          ;   02 SHORT_NAME
6978:     AF 6E 83 61 BB 85                                            ;     GREEN KEY
697E:   01 01                                                          ;   01 ADJECTIVES
6980:   14                                                             ;   TODO WORD
6981:   07 79                                                          ;   07 COMMAND HANDLING IF FIRST NOUN
6983:     0E 77                                                        ;     while_fail: size=0077
6985:       0D 32                                                      ;       while_pass: size=0032
6987:         0A 43                                                    ;         compare_input_to(phrase) phrase="43: GET ..C..... WITH ..C....."
6989:         09 16                                                    ;         compare_to_second_noun(object) object=16(WindowHook)
698B:         03 8C 41                                                 ;         is_located(room,object) room=8C(East end east-west hall) object=41(GreenKeyB)
698E:         03 8E 1B                                                 ;         is_located(room,object) room=8E(Electroshock room) object=1B(GreenKeyA)
6991:         17 41 00                                                 ;         move_to(object,room) object=41(GreenKeyB) room=00(Room_00)
6994:         17 1B 13                                                 ;         move_to(object,room) object=1B(GreenKeyA) room=13(Room_13)
6997:         04 20                                                    ;         print(msg) size=0020
6999:           C7 DE 77 15 16 BC DB 72 BB 85 FB 17 53 BE 5F BE        ;           YOU GET THE KEY WITH THE HOOK. GREEN KEY
69A9:           A9 15 AF 9F 84 15 30 60 17 16 56 DB 17 48 1B 9C        ;           TAKEN.
69B9:       0D 23                                                      ;       while_pass: size=0023
69BB:         0A 05                                                    ;         compare_input_to(phrase) phrase="05: GET ..C..... * *"
69BD:         04 1F                                                    ;         print(msg) size=001F
69BF:           C7 DE D3 14 90 96 F3 A0 63 B1 13 54 5F BE 84 15        ;           YOU CAN NOT REACH THE GREEN KEY FROM OUT
69CF:           30 60 17 16 48 DB FF B2 C7 16 0A BC 2F 62 2E           ;           HERE.
69DE:       0D 1C                                                      ;       while_pass: size=001C
69E0:         0A 43                                                    ;         compare_input_to(phrase) phrase="43: GET ..C..... WITH ..C....."
69E2:         04 16                                                    ;         print(msg) size=0016
69E4:           C7 DE D3 14 E6 96 77 15 16 BC DB 72 AF 6E 83 61        ;           YOU CAN'T GET THE GREEN KEY WITH
69F4:           BB 85 FB 17 53 BE                                      ;           ~
69FA:         A9                                                       ;         A9(PrintTheSecondNoun)
69FB:         8B                                                       ;         8B(PrintPeriod)
;
; Object_42 "Object42"
69FC: 42 03                                                            ; word=42 size=0003
69FE: 18 00 00                                                         ; room=18 scorePoints=00 bits=00
```

# Room Descriptions

```code
RoomDescriptions: 
6A01: 00             NOP                     
6A02: 85             ADD     A,L             
6A03: 9E             SBC     (HL)            
6A04: 81             ADD     A,C             
6A05: 3A 00 03       LD      A,($0300)       
6A08: 2A 04 28       LD      HL,($2804)      
6A0B: 5F             LD      E,A             
6A0C: BE             CP      (HL)            
6A0D: 63             LD      H,E             
6A0E: 16 9E          LD      D,$9E           
6A10: 7A             LD      A,D             
6A11: 8B             ADC     A,E             
6A12: 61             LD      H,C             
6A13: 17             RLA                     
6A14: 98             SBC     B               
6A15: 39             ADD     HL,SP           
6A16: 17             RLA                     
6A17: FE 9F          CP      $9F             
6A19: 7B             LD      A,E             
6A1A: 14             INC     D               
6A1B: 54             LD      D,H             
6A1C: 8B             ADC     A,E             
6A1D: 9B             SBC     E               
6A1E: 6C             LD      L,H             
6A1F: 01 B3 59       LD      BC,$59B3        
6A22: 90             SUB     B               
6A23: 82             ADD     A,D             
6A24: 7B             LD      A,E             
6A25: 3A 15 8D       LD      A,($8D15)       
6A28: 7B             LD      A,E             
6A29: 23             INC     HL              
6A2A: 15             DEC     D               
6A2B: F3             DI                      
6A2C: B9             CP      C               
6A2D: 8E             ADC     A,(HL)          
6A2E: 48             LD      C,B             
6A2F: F7             RST     0X30            
6A30: 17             RLA                     
6A31: 17             RLA                     
6A32: BA             CP      D               
6A33: 04             INC     B               
6A34: 0B             DEC     BC              
6A35: 0B             DEC     BC              
6A36: 09             ADD     HL,BC           
6A37: 0A             LD      A,(BC)          
6A38: 04             INC     B               
6A39: 02             LD      (BC),A          
6A3A: 00             NOP                     
6A3B: 95             SUB     L               
6A3C: 03             INC     BC              
6A3D: 02             LD      (BC),A          
6A3E: 00             NOP                     
6A3F: 82             ADD     A,D             
6A40: 82             ADD     A,D             
6A41: 49             LD      C,C             
6A42: 00             NOP                     
6A43: 03             INC     BC              
6A44: 35             DEC     (HL)            
6A45: 04             INC     B               
6A46: 33             INC     SP              
6A47: 5F             LD      E,A             
6A48: BE             CP      (HL)            
6A49: 03             INC     BC              
6A4A: 15             DEC     D               
6A4B: 5F             LD      E,A             
6A4C: B9             CP      C               
6A4D: 93             SUB     E               
6A4E: 9A             SBC     D               
6A4F: 9E             SBC     (HL)            
6A50: B4             OR      H               
6A51: 7B             LD      A,E             
6A52: 14             INC     D               
6A53: E3             EX      (SP),HL         
6A54: B8             CP      B               
6A55: F3             DI                      
6A56: 8C             ADC     A,H             
6A57: 97             SUB     A               
6A58: B9             CP      C               
6A59: 2F             CPL                     
6A5A: 49             LD      C,C             
6A5B: 39             ADD     HL,SP           
6A5C: 17             RLA                     
6A5D: DB 9F          IN      A,($9F)         
6A5F: 56             LD      D,(HL)          
6A60: D1             POP     DE              
6A61: 07             RLCA                    
6A62: 71             LD      (HL),C          
6A63: 96             SUB     (HL)            
6A64: D7             RST     0X10            
6A65: D6 B5          SUB     $B5             
6A67: D6 9C          SUB     $9C             
6A69: DB 72          IN      A,($72)         
6A6B: 95             SUB     L               
6A6C: 5F             LD      E,A             
6A6D: 73             LD      (HL),E          
6A6E: C1             POP     BC              
6A6F: B5             OR      L               
6A70: D0             RET     NC              
6A71: 73             LD      (HL),E          
6A72: C1             POP     BC              
6A73: 8E             ADC     A,(HL)          
6A74: 48             LD      C,B             
6A75: 61             LD      H,C             
6A76: 17             RLA                     
6A77: 82             ADD     A,D             
6A78: C6 2E          ADD     $2E             
6A7A: 04             INC     B               
6A7B: 0F             RRCA                    
6A7C: 0B             DEC     BC              
6A7D: 0D             DEC     C               
6A7E: 0A             LD      A,(BC)          
6A7F: 04             INC     B               
6A80: 02             LD      (BC),A          
6A81: 00             NOP                     
6A82: 81             ADD     A,C             
6A83: 02             LD      (BC),A          
6A84: 02             LD      (BC),A          
6A85: 00             NOP                     
6A86: 83             ADD     A,E             
6A87: 03             INC     BC              
6A88: 02             LD      (BC),A          
6A89: 00             NOP                     
6A8A: 84             ADD     A,H             
6A8B: 83             ADD     A,E             
6A8C: 46             LD      B,(HL)          
6A8D: 00             NOP                     
6A8E: 03             INC     BC              
6A8F: 3A 04 38       LD      A,($3804)       
6A92: 5F             LD      E,A             
6A93: BE             CP      (HL)            
6A94: 3A 15 6B       LD      A,($6B15)       
6A97: 48             LD      C,B             
6A98: D6 97          SUB     $97             
6A9A: C0             RET     NZ              
6A9B: 7A             LD      A,D             
6A9C: 39             ADD     HL,SP           
6A9D: 17             RLA                     
6A9E: DB 9F          IN      A,($9F)         
6AA0: 1F             RRA                     
6AA1: D1             POP     DE              
6AA2: 5B             LD      E,E             
6AA3: B1             OR      C               
6AA4: 5F             LD      E,A             
6AA5: BE             CP      (HL)            
6AA6: 09             ADD     HL,BC           
6AA7: 15             DEC     D               
6AA8: 09             ADD     HL,BC           
6AA9: 56             LD      D,(HL)          
6AAA: 96             SUB     (HL)            
6AAB: AF             XOR     A               
6AAC: 63             LD      H,E             
6AAD: B1             OR      C               
6AAE: 0B             DEC     BC              
6AAF: C0             RET     NZ              
6AB0: 56             LD      D,(HL)          
6AB1: A4             AND     H               
6AB2: 30 79          JR      NC,$6B2D        
6AB4: 2F             CPL                     
6AB5: C0             RET     NZ              
6AB6: 82             ADD     A,D             
6AB7: 17             RLA                     
6AB8: 2F             CPL                     
6AB9: 62             LD      H,D             
6ABA: D5             PUSH    DE              
6ABB: 15             DEC     D               
6ABC: 7B             LD      A,E             
6ABD: 14             INC     D               
6ABE: 50             LD      D,B             
6ABF: B8             CP      B               
6AC0: BF             CP      A               
6AC1: 6D             LD      L,L             
6AC2: 3A 15 73       LD      A,($7315)       
6AC5: 7B             LD      A,E             
6AC6: 04             INC     B               
6AC7: 9A             SBC     D               
6AC8: 77             LD      (HL),A          
6AC9: BE             CP      (HL)            
6ACA: 04             INC     B               
6ACB: 07             RLCA                    
6ACC: 0B             DEC     BC              
6ACD: 05             DEC     B               
6ACE: 0A             LD      A,(BC)          
6ACF: 01 02 00       LD      BC,$0002        
6AD2: 82             ADD     A,D             
6AD3: 84             ADD     A,H             
6AD4: 5B             LD      E,E             
6AD5: 00             NOP                     
6AD6: 03             INC     BC              
6AD7: 37             SCF                     
6AD8: 04             INC     B               
6AD9: 35             DEC     (HL)            
6ADA: 5F             LD      E,A             
6ADB: BE             CP      (HL)            
6ADC: F7             RST     0X30            
6ADD: 17             RLA                     
6ADE: F3             DI                      
6ADF: B9             CP      C               
6AE0: 8E             ADC     A,(HL)          
6AE1: 61             LD      H,C             
6AE2: B8             CP      B               
6AE3: 16 7B          LD      D,$7B           
6AE5: 14             INC     D               
6AE6: 74             LD      (HL),H          
6AE7: CA 4E DB       JP      Z,$DB4E         
6AEA: 11 A0 23       LD      DE,$23A0        
6AED: 15             DEC     D               
6AEE: 15             DEC     D               
6AEF: BA             CP      D               
6AF0: B5             OR      L               
6AF1: D0             RET     NC              
6AF2: 0A             LD      A,(BC)          
6AF3: BC             CP      H               
6AF4: 46             LD      B,(HL)          
6AF5: 48             LD      C,B             
6AF6: 1B             DEC     DE              
6AF7: D0             RET     NC              
6AF8: 56             LD      D,(HL)          
6AF9: F4 F4 72       CALL    P,$72F4         
6AFC: 4B             LD      C,E             
6AFD: 5E             LD      E,(HL)          
6AFE: C3 B5 91       JP      $91B5           
6B01: 96             SUB     (HL)            
6B02: F0             RET     P               
6B03: A4             AND     H               
6B04: 91             SUB     C               
6B05: 7A             LD      A,D             
6B06: 89             ADC     A,C             
6B07: 17             RLA                     
6B08: 82             ADD     A,D             
6B09: 17             RLA                     
6B0A: 59             LD      E,C             
6B0B: 5E             LD      E,(HL)          
6B0C: 66             LD      H,(HL)          
6B0D: 62             LD      H,D             
6B0E: 2E 04          LD      L,$04           
6B10: 1F             RRA                     
6B11: 0B             DEC     BC              
6B12: 1D             DEC     E               
6B13: 0A             LD      A,(BC)          
6B14: 04             INC     B               
6B15: 02             LD      (BC),A          
6B16: 00             NOP                     
6B17: 82             ADD     A,D             
6B18: 03             INC     BC              
6B19: 02             LD      (BC),A          
6B1A: 00             NOP                     
6B1B: 87             ADD     A,A             
6B1C: 01 08 0E       LD      BC,$0E08        
6B1F: 06 14          LD      B,$14           
6B21: 1C             INC     E               
6B22: 02             LD      (BC),A          
6B23: 8D             ADC     A,L             
6B24: 00             NOP                     
6B25: 85             ADD     A,L             
6B26: 02             LD      (BC),A          
6B27: 08             EX      AF,AF'          
6B28: 0E 06          LD      C,$06           
6B2A: 14             INC     D               
6B2B: 1C             INC     E               
6B2C: 03             INC     BC              
6B2D: 8D             ADC     A,L             
6B2E: 00             NOP                     
6B2F: 86             ADD     A,(HL)          
6B30: 85             ADD     A,L             
6B31: 13             INC     DE              
6B32: 00             NOP                     
6B33: 03             INC     BC              
6B34: 01 81 04       LD      BC,$0481        
6B37: 0D             DEC     C               
6B38: 0B             DEC     BC              
6B39: 0B             DEC     BC              
6B3A: 0A             LD      A,(BC)          
6B3B: 02             LD      (BC),A          
6B3C: 08             EX      AF,AF'          
6B3D: 0E 06          LD      C,$06           
6B3F: 14             INC     D               
6B40: 1C             INC     E               
6B41: 01 8D 00       LD      BC,$008D        
6B44: 84             ADD     A,H             
6B45: 86             ADD     A,(HL)          
6B46: 13             INC     DE              
6B47: 00             NOP                     
6B48: 03             INC     BC              
6B49: 01 81 04       LD      BC,$0481        
6B4C: 0D             DEC     C               
6B4D: 0B             DEC     BC              
6B4E: 0B             DEC     BC              
6B4F: 0A             LD      A,(BC)          
6B50: 01 08 0E       LD      BC,$0E08        
6B53: 06 14          LD      B,$14           
6B55: 1C             INC     E               
6B56: 04             INC     B               
6B57: 8D             ADC     A,L             
6B58: 00             NOP                     
6B59: 84             ADD     A,H             
6B5A: 87             ADD     A,A             
6B5B: 25             DEC     H               
6B5C: 00             NOP                     
6B5D: 03             INC     BC              
6B5E: 01 82 04       LD      BC,$0482        
6B61: 1F             RRA                     
6B62: 0B             DEC     BC              
6B63: 1D             DEC     E               
6B64: 0A             LD      A,(BC)          
6B65: 03             INC     BC              
6B66: 02             LD      (BC),A          
6B67: 00             NOP                     
6B68: 8A             ADC     A,D             
6B69: 04             INC     B               
6B6A: 02             LD      (BC),A          
6B6B: 00             NOP                     
6B6C: 84             ADD     A,H             
6B6D: 01 08 0E       LD      BC,$0E08        
6B70: 06 14          LD      B,$14           
6B72: 1C             INC     E               
6B73: 06 8D          LD      B,$8D           
6B75: 00             NOP                     
6B76: 88             ADC     A,B             
6B77: 02             LD      (BC),A          
6B78: 08             EX      AF,AF'          
6B79: 0E 06          LD      C,$06           
6B7B: 14             INC     D               
6B7C: 1C             INC     E               
6B7D: 07             RLCA                    
6B7E: 8D             ADC     A,L             
6B7F: 00             NOP                     
6B80: 89             ADC     A,C             
6B81: 88             ADC     A,B             
6B82: 42             LD      B,D             
6B83: 00             NOP                     
6B84: 03             INC     BC              
6B85: 30 04          JR      NC,$6B8B        
6B87: 2E 55          LD      L,$55           
6B89: 45             LD      B,L             
6B8A: 8E             ADC     A,(HL)          
6B8B: 91             SUB     C               
6B8C: 15             DEC     D               
6B8D: 8A             ADC     A,D             
6B8E: A3             AND     E               
6B8F: AD             XOR     L               
6B90: 5B             LD      E,E             
6B91: B1             OR      C               
6B92: 01 B3 DB       LD      BC,$DBB3        
6B95: 95             SUB     L               
6B96: 46             LD      B,(HL)          
6B97: 48             LD      C,B             
6B98: 59             LD      E,C             
6B99: 15             DEC     D               
6B9A: 23             INC     HL              
6B9B: C6 0E          ADD     $0E             
6B9D: D0             RET     NC              
6B9E: 0B             DEC     BC              
6B9F: 8E             ADC     A,(HL)          
6BA0: 2F             CPL                     
6BA1: 49             LD      C,C             
6BA2: E1             POP     HL              
6BA3: 14             INC     D               
6BA4: 74             LD      (HL),H          
6BA5: CA F3 5F       JP      Z,$5FF3         
6BA8: 56             LD      D,(HL)          
6BA9: D1             POP     DE              
6BAA: 03             INC     BC              
6BAB: 71             LD      (HL),C          
6BAC: 82             ADD     A,D             
6BAD: 17             RLA                     
6BAE: DD                                  
6BAF: 78             LD      A,B             
6BB0: DB 16          IN      A,($16)         
6BB2: C3 59 CF       JP      $CF59           
6BB5: 98             SBC     B               
6BB6: 04             INC     B               
6BB7: 0D             DEC     C               
6BB8: 0B             DEC     BC              
6BB9: 0B             DEC     BC              
6BBA: 0A             LD      A,(BC)          
6BBB: 02             LD      (BC),A          
6BBC: 08             EX      AF,AF'          
6BBD: 0E 06          LD      C,$06           
6BBF: 14             INC     D               
6BC0: 1C             INC     E               
6BC1: 05             DEC     B               
6BC2: 8D             ADC     A,L             
6BC3: 00             NOP                     
6BC4: 87             ADD     A,A             
6BC5: 89             ADC     A,C             
6BC6: 13             INC     DE              
6BC7: 00             NOP                     
6BC8: 03             INC     BC              
6BC9: 01 81 04       LD      BC,$0481        
6BCC: 0D             DEC     C               
6BCD: 0B             DEC     BC              
6BCE: 0B             DEC     BC              
6BCF: 0A             LD      A,(BC)          
6BD0: 01 08 0E       LD      BC,$0E08        
6BD3: 06 14          LD      B,$14           
6BD5: 1C             INC     E               
6BD6: 08             EX      AF,AF'          
6BD7: 8D             ADC     A,L             
6BD8: 00             NOP                     
6BD9: 87             ADD     A,A             
6BDA: 8A             ADC     A,D             
6BDB: 25             DEC     H               
6BDC: 00             NOP                     
6BDD: 03             INC     BC              
6BDE: 01 82 04       LD      BC,$0482        
6BE1: 1F             RRA                     
6BE2: 0B             DEC     BC              
6BE3: 1D             DEC     E               
6BE4: 0A             LD      A,(BC)          
6BE5: 04             INC     B               
6BE6: 02             LD      (BC),A          
6BE7: 00             NOP                     
6BE8: 87             ADD     A,A             
6BE9: 03             INC     BC              
6BEA: 02             LD      (BC),A          
6BEB: 00             NOP                     
6BEC: 8C             ADC     A,H             
6BED: 01 08 0E       LD      BC,$0E08        
6BF0: 06 14          LD      B,$14           
6BF2: 1C             INC     E               
6BF3: 0A             LD      A,(BC)          
6BF4: 8D             ADC     A,L             
6BF5: 00             NOP                     
6BF6: 8B             ADC     A,E             
6BF7: 02             LD      (BC),A          
6BF8: 08             EX      AF,AF'          
6BF9: 0E 06          LD      C,$06           
6BFB: 14             INC     D               
6BFC: 1C             INC     E               
6BFD: 0B             DEC     BC              
6BFE: 8D             ADC     A,L             
6BFF: 00             NOP                     
6C00: 8F             ADC     A,A             
6C01: 8B             ADC     A,E             
6C02: 13             INC     DE              
6C03: 00             NOP                     
6C04: 03             INC     BC              
6C05: 01 81 04       LD      BC,$0481        
6C08: 0D             DEC     C               
6C09: 0B             DEC     BC              
6C0A: 0B             DEC     BC              
6C0B: 0A             LD      A,(BC)          
6C0C: 02             LD      (BC),A          
6C0D: 08             EX      AF,AF'          
6C0E: 0E 06          LD      C,$06           
6C10: 14             INC     D               
6C11: 1C             INC     E               
6C12: 09             ADD     HL,BC           
6C13: 8D             ADC     A,L             
6C14: 00             NOP                     
6C15: 8A             ADC     A,D             
6C16: 8C             ADC     A,H             
6C17: 41             LD      B,C             
6C18: 00             NOP                     
6C19: 03             INC     BC              
6C1A: 27             DAA                     
6C1B: 0D             DEC     C               
6C1C: 25             DEC     H               
6C1D: 04             INC     B               
6C1E: 0A             LD      A,(BC)          
6C1F: 5F             LD      E,A             
6C20: BE             CP      (HL)            
6C21: 23             INC     HL              
6C22: 15             DEC     D               
6C23: F3             DI                      
6C24: B9             CP      C               
6C25: 8E             ADC     A,(HL)          
6C26: 61             LD      H,C             
6C27: B8             CP      B               
6C28: 16 82          LD      D,$82           
6C2A: 04             INC     B               
6C2B: 16 5F          LD      D,$5F           
6C2D: BE             CP      (HL)            
6C2E: 5B             LD      E,E             
6C2F: B1             OR      C               
6C30: 4B             LD      C,E             
6C31: 7B             LD      A,E             
6C32: 83             ADD     A,E             
6C33: 48             LD      C,B             
6C34: 5F             LD      E,A             
6C35: A0             AND     B               
6C36: 10 99          DJNZ    $6BD1           
6C38: D6 6A          SUB     $6A             
6C3A: D6 9C          SUB     $9C             
6C3C: DB 72          IN      A,($72)         
6C3E: 95             SUB     L               
6C3F: 5F             LD      E,A             
6C40: 9B             SBC     E               
6C41: C1             POP     BC              
6C42: 04             INC     B               
6C43: 15             DEC     D               
6C44: 0B             DEC     BC              
6C45: 13             INC     DE              
6C46: 0A             LD      A,(BC)          
6C47: 03             INC     BC              
6C48: 02             LD      (BC),A          
6C49: 00             NOP                     
6C4A: 8E             ADC     A,(HL)          
6C4B: 04             INC     B               
6C4C: 02             LD      (BC),A          
6C4D: 00             NOP                     
6C4E: 8A             ADC     A,D             
6C4F: 01 08 0E       LD      BC,$0E08        
6C52: 06 14          LD      B,$14           
6C54: 1C             INC     E               
6C55: 0D             DEC     C               
6C56: 8D             ADC     A,L             
6C57: 00             NOP                     
6C58: 8D             ADC     A,L             
6C59: 8D             ADC     A,L             
6C5A: 13             INC     DE              
6C5B: 00             NOP                     
6C5C: 03             INC     BC              
6C5D: 01 81 04       LD      BC,$0481        
6C60: 0D             DEC     C               
6C61: 0B             DEC     BC              
6C62: 0B             DEC     BC              
6C63: 0A             LD      A,(BC)          
6C64: 02             LD      (BC),A          
6C65: 08             EX      AF,AF'          
6C66: 0E 06          LD      C,$06           
6C68: 14             INC     D               
6C69: 1C             INC     E               
6C6A: 0C             INC     C               
6C6B: 8D             ADC     A,L             
6C6C: 00             NOP                     
6C6D: 8C             ADC     A,H             
6C6E: 8E             ADC     A,(HL)          
6C6F: 36 00          LD      (HL),$00        
6C71: 03             INC     BC              
6C72: 2A 04 28       LD      HL,($2804)      
6C75: 5F             LD      E,A             
6C76: BE             CP      (HL)            
6C77: 2E 15          LD      L,$15           
6C79: E6 5F          AND     $5F             
6C7B: 05             DEC     B               
6C7C: B3             OR      E               
6C7D: 75             LD      (HL),L          
6C7E: 74             LD      (HL),H          
6C7F: D6 83          SUB     $83             
6C81: F4 72 F3       CALL    P,$F372         
6C84: 48             LD      C,B             
6C85: 39             ADD     HL,SP           
6C86: 17             RLA                     
6C87: FF             RST     0X38            
6C88: 9F             SBC     A               
6C89: 82             ADD     A,D             
6C8A: 17             RLA                     
6C8B: 2F             CPL                     
6C8C: 62             LD      H,D             
6C8D: D5             PUSH    DE              
6C8E: 15             DEC     D               
6C8F: 7B             LD      A,E             
6C90: 14             INC     D               
6C91: 50             LD      D,B             
6C92: B8             CP      B               
6C93: BF             CP      A               
6C94: 6D             LD      L,L             
6C95: 3A 15 73       LD      A,($7315)       
6C98: 7B             LD      A,E             
6C99: B5             OR      L               
6C9A: D0             RET     NC              
6C9B: 9B             SBC     E               
6C9C: C1             POP     BC              
6C9D: 04             INC     B               
6C9E: 07             RLCA                    
6C9F: 0B             DEC     BC              
6CA0: 05             DEC     B               
6CA1: 0A             LD      A,(BC)          
6CA2: 04             INC     B               
6CA3: 02             LD      (BC),A          
6CA4: 00             NOP                     
6CA5: 8C             ADC     A,H             
6CA6: 8F             ADC     A,A             
6CA7: 30 00          JR      NC,$6CA9        
6CA9: 03             INC     BC              
6CAA: 10 0D          DJNZ    $6CB9           
6CAC: 0E 04          LD      C,$04           
6CAE: 0B             DEC     BC              
6CAF: 5F             LD      E,A             
6CB0: BE             CP      (HL)            
6CB1: 99             SBC     C               
6CB2: 16 C2          LD      D,$C2           
6CB4: B3             OR      E               
6CB5: 30 15          JR      NC,$6CCC        
6CB7: 11 58 46       LD      DE,$4658        
6CBA: 83             ADD     A,E             
6CBB: 04             INC     B               
6CBC: 1B             DEC     DE              
6CBD: 0B             DEC     BC              
6CBE: 19             ADD     HL,DE           
6CBF: 0A             LD      A,(BC)          
6CC0: 01 08 0E       LD      BC,$0E08        
6CC3: 06 14          LD      B,$14           
6CC5: 1C             INC     E               
6CC6: 0E 8D          LD      C,$8D           
6CC8: 00             NOP                     
6CC9: 8A             ADC     A,D             
6CCA: 02             LD      (BC),A          
6CCB: 02             LD      (BC),A          
6CCC: 00             NOP                     
6CCD: 91             SUB     C               
6CCE: 03             INC     BC              
6CCF: 08             EX      AF,AF'          
6CD0: 0E 06          LD      C,$06           
6CD2: 14             INC     D               
6CD3: 1C             INC     E               
6CD4: 0F             RRCA                    
6CD5: 8D             ADC     A,L             
6CD6: 00             NOP                     
6CD7: 90             SUB     B               
6CD8: 90             SUB     B               
6CD9: 13             INC     DE              
6CDA: 00             NOP                     
6CDB: 03             INC     BC              
6CDC: 01 81 04       LD      BC,$0481        
6CDF: 0D             DEC     C               
6CE0: 0B             DEC     BC              
6CE1: 0B             DEC     BC              
6CE2: 0A             LD      A,(BC)          
6CE3: 04             INC     B               
6CE4: 08             EX      AF,AF'          
6CE5: 0E 06          LD      C,$06           
6CE7: 14             INC     D               
6CE8: 1C             INC     E               
6CE9: 10 8D          DJNZ    $6C78           
6CEB: 00             NOP                     
6CEC: 8F             ADC     A,A             
6CED: 91             SUB     C               
6CEE: 32 00 03       LD      ($0300),A       
6CF1: 14             INC     D               
6CF2: 0D             DEC     C               
6CF3: 12             LD      (DE),A          
6CF4: 83             ADD     A,E             
6CF5: 04             INC     B               
6CF6: 0F             RRCA                    
6CF7: 5F             LD      E,A             
6CF8: BE             CP      (HL)            
6CF9: 5B             LD      E,E             
6CFA: B1             OR      C               
6CFB: 4B             LD      C,E             
6CFC: 7B             LD      A,E             
6CFD: 83             ADD     A,E             
6CFE: 48             LD      C,B             
6CFF: 23             INC     HL              
6D00: 63             LD      H,E             
6D01: 07             RLCA                    
6D02: BC             CP      H               
6D03: 66             LD      H,(HL)          
6D04: 49             LD      C,C             
6D05: 2E 04          LD      L,$04           
6D07: 19             ADD     HL,DE           
6D08: 0B             DEC     BC              
6D09: 17             RLA                     
6D0A: 0A             LD      A,(BC)          
6D0B: 01 02 00       LD      BC,$0002        
6D0E: 8F             ADC     A,A             
6D0F: 02             LD      (BC),A          
6D10: 02             LD      (BC),A          
6D11: 00             NOP                     
6D12: 96             SUB     (HL)            
6D13: 03             INC     BC              
6D14: 02             LD      (BC),A          
6D15: 00             NOP                     
6D16: 92             SUB     D               
6D17: 04             INC     B               
6D18: 08             EX      AF,AF'          
6D19: 0E 06          LD      C,$06           
6D1B: 14             INC     D               
6D1C: 1C             INC     E               
6D1D: 11 8D 00       LD      DE,$008D        
6D20: 94             SUB     H               
6D21: 92             SUB     D               
6D22: 38 00          JR      C,$6D24         
6D24: 03             INC     BC              
6D25: 24             INC     H               
6D26: 04             INC     B               
6D27: 22 5F BE       LD      ($BE5F),HL      
6D2A: 1B             DEC     DE              
6D2B: 16 9A          LD      D,$9A           
6D2D: BD             CP      L               
6D2E: 83             ADD     A,E             
6D2F: 61             LD      H,C             
6D30: 23             INC     HL              
6D31: D1             POP     DE              
6D32: 13             INC     DE              
6D33: 54             LD      D,H             
6D34: 55             LD      D,L             
6D35: 72             LD      (HL),D          
6D36: 3A 15 8D       LD      A,($8D15)       
6D39: 7B             LD      A,E             
6D3A: 23             INC     HL              
6D3B: 15             DEC     D               
6D3C: 16 BA          LD      D,$BA           
6D3E: F7             RST     0X30            
6D3F: 17             RLA                     
6D40: 16 BA          LD      D,$BA           
6D42: 90             SUB     B               
6D43: 14             INC     D               
6D44: 15             DEC     D               
6D45: 58             LD      E,B             
6D46: 36 A1          LD      (HL),$A1        
6D48: 9B             SBC     E               
6D49: 76             HALT                    
6D4A: 04             INC     B               
6D4B: 0F             RRCA                    
6D4C: 0B             DEC     BC              
6D4D: 0D             DEC     C               
6D4E: 0A             LD      A,(BC)          
6D4F: 03             INC     BC              
6D50: 02             LD      (BC),A          
6D51: 00             NOP                     
6D52: 93             SUB     E               
6D53: 02             LD      (BC),A          
6D54: 02             LD      (BC),A          
6D55: 00             NOP                     
6D56: 97             SUB     A               
6D57: 04             INC     B               
6D58: 02             LD      (BC),A          
6D59: 00             NOP                     
6D5A: 91             SUB     C               
6D5B: 93             SUB     E               
6D5C: 81             ADD     A,C             
6D5D: 0F             RRCA                    
6D5E: 00             NOP                     
6D5F: 03             INC     BC              
6D60: 2B             DEC     HL              
6D61: 04             INC     B               
6D62: 29             ADD     HL,HL           
6D63: 5F             LD      E,A             
6D64: BE             CP      (HL)            
6D65: 17             RLA                     
6D66: 16 CF          LD      D,$CF           
6D68: 99             SBC     C               
6D69: 9B             SBC     E               
6D6A: 8F             ADC     A,A             
6D6B: 5F             LD      E,A             
6D6C: BE             CP      (HL)            
6D6D: 5B             LD      E,E             
6D6E: B1             OR      C               
6D6F: 4B             LD      C,E             
6D70: 7B             LD      A,E             
6D71: 59             LD      E,C             
6D72: 45             LD      B,L             
6D73: 66             LD      H,(HL)          
6D74: 62             LD      H,D             
6D75: 3A 15 73       LD      A,($7315)       
6D78: 7B             LD      A,E             
6D79: 8E             ADC     A,(HL)          
6D7A: 48             LD      C,B             
6D7B: 90             SUB     B               
6D7C: 14             INC     D               
6D7D: C2 16 93       JP      NZ,$9316        
6D80: 61             LD      H,C             
6D81: AB             XOR     E               
6D82: 98             SBC     B               
6D83: 6B             LD      L,E             
6D84: BF             CP      A               
6D85: 5F             LD      E,A             
6D86: BE             CP      (HL)            
6D87: 61             LD      H,C             
6D88: 17             RLA                     
6D89: 82             ADD     A,D             
6D8A: C6 2E          ADD     $2E             
6D8C: 04             INC     B               
6D8D: 80             ADD     A,B             
6D8E: DE 0B          SBC     $0B             
6D90: 80             ADD     A,B             
6D91: DB 0A          IN      A,($0A)         
6D93: 02             LD      (BC),A          
6D94: 80             ADD     A,B             
6D95: D3 0E          OUT     ($0E),A         
6D97: 80             ADD     A,B             
6D98: D0             RET     NC              
6D99: 0D             DEC     C               
6D9A: 18 01          JR      $6D9D           
6D9C: 1A             LD      A,(DE)          
6D9D: 04             INC     B               
6D9E: 14             INC     D               
6D9F: 5F             LD      E,A             
6DA0: BE             CP      (HL)            
6DA1: 09             ADD     HL,BC           
6DA2: 15             DEC     D               
6DA3: D9             EXX                     
6DA4: 6A             LD      L,D             
6DA5: 46             LD      B,(HL)          
6DA6: 7A             LD      A,D             
6DA7: 99             SBC     C               
6DA8: 16 0E          LD      D,$0E           
6DAA: BC             CP      H               
6DAB: 73             LD      (HL),E          
6DAC: 62             LD      H,D             
6DAD: C7             RST     0X00            
6DAE: DE DB          SBC     $DB             
6DB0: 16 C9          LD      D,$C9           
6DB2: B9             CP      C               
6DB3: 0D             DEC     C               
6DB4: 80             ADD     A,B             
6DB5: B3             OR      E               
6DB6: 0E 80          LD      C,$80           
6DB8: B0             OR      B               
6DB9: 0D             DEC     C               
6DBA: 19             ADD     HL,DE           
6DBB: 20 38          JR      NZ,$6DF5        
6DBD: 04             INC     B               
6DBE: 15             DEC     D               
6DBF: C7             RST     0X00            
6DC0: DE 9B          SBC     $9B             
6DC2: 15             DEC     D               
6DC3: 5B             LD      E,E             
6DC4: CA 07 68       JP      Z,$6807         
6DC7: 33             INC     SP              
6DC8: 98             SBC     B               
6DC9: 85             ADD     A,L             
6DCA: A6             AND     (HL)            
6DCB: 44             LD      B,H             
6DCC: B8             CP      B               
6DCD: DB 8B          IN      A,($8B)         
6DCF: 55             LD      D,L             
6DD0: 62             LD      H,D             
6DD1: DF             RST     0X18            
6DD2: 48             LD      C,B             
6DD3: 21 0D 80       LD      HL,$800D        
6DD6: 92             SUB     D               
6DD7: 20 13          JR      NZ,$6DEC        
6DD9: 04             INC     B               
6DDA: 26 4B          LD      H,$4B           
6DDC: 49             LD      C,C             
6DDD: C7             RST     0X00            
6DDE: DE 3F          SBC     $3F             
6DE0: 16 CF          LD      D,$CF           
6DE2: 49             LD      C,C             
6DE3: 15             DEC     D               
6DE4: EE CF          XOR     $CF             
6DE6: 62             LD      H,D             
6DE7: CE B0          ADC     $B0             
6DE9: 87             ADD     A,A             
6DEA: 15             DEC     D               
6DEB: 2E 49          LD      L,$49           
6DED: D2 B5 E6       JP      NC,$E6B5        
6DF0: A0             AND     B               
6DF1: F3             DI                      
6DF2: 5F             LD      E,A             
6DF3: 36 A1          LD      (HL),$A1        
6DF5: 46             LD      B,(HL)          
6DF6: B8             CP      B               
6DF7: 49             LD      C,C             
6DF8: 5E             LD      E,(HL)          
6DF9: C4 B0 51       CALL    NZ,$51B0        
6DFC: 18 43          JR      $6E41           
6DFE: C2 33 98       JP      NZ,$9833        
6E01: 0E 15          LD      C,$15           
6E03: 14             INC     D               
6E04: 0D             DEC     C               
6E05: 05             DEC     B               
6E06: 01 3C 17       LD      BC,$173C        
6E09: 3C             INC     A               
6E0A: 99             SBC     C               
6E0B: 04             INC     B               
6E0C: 0B             DEC     BC              
6E0D: 5F             LD      E,A             
6E0E: BE             CP      (HL)            
6E0F: FF             RST     0X38            
6E10: 14             INC     D               
6E11: F3             DI                      
6E12: 46             LD      B,(HL)          
6E13: 79             LD      A,C             
6E14: 5B             LD      E,E             
6E15: 90             SUB     B               
6E16: 14             INC     D               
6E17: 44             LD      B,H             
6E18: 04             INC     B               
6E19: 40             LD      B,B             
6E1A: 6C             LD      L,H             
6E1B: BE             CP      (HL)            
6E1C: 6B             LD      L,E             
6E1D: A1             AND     C               
6E1E: C7             RST     0X00            
6E1F: DE D0          SBC     $D0             
6E21: 15             DEC     D               
6E22: 7B             LD      A,E             
6E23: 14             INC     D               
6E24: E3             EX      (SP),HL         
6E25: B8             CP      B               
6E26: F3             DI                      
6E27: 8C             ADC     A,H             
6E28: 09             ADD     HL,BC           
6E29: BA             CP      D               
6E2A: C9             RET                     
6E2B: B0             OR      B               
6E2C: 55             LD      D,L             
6E2D: 5E             LD      E,(HL)          
6E2E: E6 72          AND     $72             
6E30: AF             XOR     A               
6E31: 14             INC     D               
6E32: 90             SUB     B               
6E33: 73             LD      (HL),E          
6E34: 16 58          LD      D,$58           
6E36: DB 72          IN      A,($72)         
6E38: EB             EX      DE,HL           
6E39: 4F             LD      C,A             
6E3A: C3 8B CF       JP      $CF8B           
6E3D: 98             SBC     B               
6E3E: 51             LD      D,C             
6E3F: 18 4A          JR      $6E8B           
6E41: C2 94 5F       JP      NZ,$5F94        
6E44: 82             ADD     A,D             
6E45: 17             RLA                     
6E46: 5B             LD      E,E             
6E47: 61             LD      H,C             
6E48: 75             LD      (HL),L          
6E49: 8D             ADC     A,L             
6E4A: D6 83          SUB     $83             
6E4C: DB 72          IN      A,($72)         
6E4E: 81             ADD     A,C             
6E4F: 5B             LD      E,E             
6E50: 83             ADD     A,E             
6E51: AF             XOR     A               
6E52: 33             INC     SP              
6E53: 98             SBC     B               
6E54: 2B             DEC     HL              
6E55: 6E             LD      L,(HL)          
6E56: F3             DI                      
6E57: 49             LD      C,C             
6E58: DB E0          IN      A,($E0)         
6E5A: 1C             INC     E               
6E5B: 40             LD      B,B             
6E5C: 0E 03          LD      C,$03           
6E5E: 15             DEC     D               
6E5F: 02             LD      (BC),A          
6E60: 29             ADD     HL,HL           
6E61: 0E 03          LD      C,$03           
6E63: 15             DEC     D               
6E64: 01 2A 17       LD      BC,$172A        
6E67: 13             INC     DE              
6E68: 99             SBC     C               
6E69: 04             INC     B               
6E6A: 02             LD      (BC),A          
6E6B: 00             NOP                     
6E6C: 92             SUB     D               
6E6D: 94             SUB     H               
6E6E: 13             INC     DE              
6E6F: 00             NOP                     
6E70: 03             INC     BC              
6E71: 01 81 04       LD      BC,$0481        
6E74: 0D             DEC     C               
6E75: 0B             DEC     BC              
6E76: 0B             DEC     BC              
6E77: 0A             LD      A,(BC)          
6E78: 03             INC     BC              
6E79: 08             EX      AF,AF'          
6E7A: 0E 06          LD      C,$06           
6E7C: 14             INC     D               
6E7D: 1C             INC     E               
6E7E: 12             LD      (DE),A          
6E7F: 8D             ADC     A,L             
6E80: 00             NOP                     
6E81: 91             SUB     C               
6E82: 95             SUB     L               
6E83: 29             ADD     HL,HL           
6E84: 00             NOP                     
6E85: 03             INC     BC              
6E86: 1D             DEC     E               
6E87: 04             INC     B               
6E88: 1B             DEC     DE              
6E89: 5F             LD      E,A             
6E8A: BE             CP      (HL)            
6E8B: B8             CP      B               
6E8C: 16 05          LD      D,$05           
6E8E: 67             LD      H,A             
6E8F: DB 63          IN      A,($63)         
6E91: 5F             LD      E,A             
6E92: BE             CP      (HL)            
6E93: 5B             LD      E,E             
6E94: B1             OR      C               
6E95: 4B             LD      C,E             
6E96: 7B             LD      A,E             
6E97: 55             LD      D,L             
6E98: 45             LD      B,L             
6E99: 91             SUB     C               
6E9A: 7A             LD      A,D             
6E9B: DB 8B          IN      A,($8B)         
6E9D: 23             INC     HL              
6E9E: 63             LD      H,E             
6E9F: 07             RLCA                    
6EA0: BC             CP      H               
6EA1: 66             LD      H,(HL)          
6EA2: 49             LD      C,C             
6EA3: 2E 04          LD      L,$04           
6EA5: 07             RLCA                    
6EA6: 0B             DEC     BC              
6EA7: 05             DEC     B               
6EA8: 0A             LD      A,(BC)          
6EA9: 03             INC     BC              
6EAA: 02             LD      (BC),A          
6EAB: 00             NOP                     
6EAC: 81             ADD     A,C             
6EAD: 96             SUB     (HL)            
6EAE: 46             LD      B,(HL)          
6EAF: 00             NOP                     
6EB0: 03             INC     BC              
6EB1: 32 04 30       LD      ($3004),A       
6EB4: 5F             LD      E,A             
6EB5: BE             CP      (HL)            
6EB6: 61             LD      H,C             
6EB7: 17             RLA                     
6EB8: 82             ADD     A,D             
6EB9: C6 30          ADD     $30             
6EBB: 15             DEC     D               
6EBC: 11 58 96       LD      DE,$9658        
6EBF: 64             LD      H,H             
6EC0: DB 72          IN      A,($72)         
6EC2: 04             INC     B               
6EC3: 9A             SBC     D               
6EC4: 75             LD      (HL),L          
6EC5: BE             CP      (HL)            
6EC6: 47             LD      B,A             
6EC7: B9             CP      C               
6EC8: 53             LD      D,E             
6EC9: BE             CP      (HL)            
6ECA: 4E             LD      C,(HL)          
6ECB: 72             LD      (HL),D          
6ECC: B3             OR      E               
6ECD: 8E             ADC     A,(HL)          
6ECE: DB E0          IN      A,($E0)         
6ED0: 5F             LD      E,A             
6ED1: BE             CP      (HL)            
6ED2: 5B             LD      E,E             
6ED3: B1             OR      C               
6ED4: 2F             CPL                     
6ED5: 49             LD      C,C             
6ED6: 23             INC     HL              
6ED7: 15             DEC     D               
6ED8: F3             DI                      
6ED9: B9             CP      C               
6EDA: 8E             ADC     A,(HL)          
6EDB: 48             LD      C,B             
6EDC: F7             RST     0X30            
6EDD: 17             RLA                     
6EDE: F3             DI                      
6EDF: B9             CP      C               
6EE0: 23             INC     HL              
6EE1: 63             LD      H,E             
6EE2: 2F             CPL                     
6EE3: C0             RET     NZ              
6EE4: 04             INC     B               
6EE5: 0F             RRCA                    
6EE6: 0B             DEC     BC              
6EE7: 0D             DEC     C               
6EE8: 0A             LD      A,(BC)          
6EE9: 01 02 00       LD      BC,$0002        
6EEC: 91             SUB     C               
6EED: 04             INC     B               
6EEE: 02             LD      (BC),A          
6EEF: 00             NOP                     
6EF0: 98             SBC     B               
6EF1: 03             INC     BC              
6EF2: 02             LD      (BC),A          
6EF3: 00             NOP                     
6EF4: 97             SUB     A               
6EF5: 97             SUB     A               
6EF6: 32 00 03       LD      ($0300),A       
6EF9: 22 04 20       LD      ($2004),HL      
6EFC: 5F             LD      E,A             
6EFD: BE             CP      (HL)            
6EFE: 03             INC     BC              
6EFF: 15             DEC     D               
6F00: 10 99          DJNZ    $6E9B           
6F02: D4 6A 3F       CALL    NC,$3F6A        
6F05: A0             AND     B               
6F06: 56             LD      D,(HL)          
6F07: F4 F4 72       CALL    P,$72F4         
6F0A: 43             LD      B,E             
6F0B: 5E             LD      E,(HL)          
6F0C: 5B             LD      E,E             
6F0D: B1             OR      C               
6F0E: 23             INC     HL              
6F0F: 63             LD      H,E             
6F10: 0B             DEC     BC              
6F11: C0             RET     NZ              
6F12: 04             INC     B               
6F13: 9A             SBC     D               
6F14: 53             LD      D,E             
6F15: BE             CP      (HL)            
6F16: 8E             ADC     A,(HL)          
6F17: 48             LD      C,B             
6F18: F7             RST     0X30            
6F19: 17             RLA                     
6F1A: 17             RLA                     
6F1B: BA             CP      D               
6F1C: 04             INC     B               
6F1D: 0B             DEC     BC              
6F1E: 0B             DEC     BC              
6F1F: 09             ADD     HL,BC           
6F20: 0A             LD      A,(BC)          
6F21: 01 02 00       LD      BC,$0002        
6F24: 92             SUB     D               
6F25: 04             INC     B               
6F26: 02             LD      (BC),A          
6F27: 00             NOP                     
6F28: 96             SUB     (HL)            
6F29: 98             SBC     B               
6F2A: 37             SCF                     
6F2B: 00             NOP                     
6F2C: 03             INC     BC              
6F2D: 2B             DEC     HL              
6F2E: 04             INC     B               
6F2F: 29             ADD     HL,HL           
6F30: 5F             LD      E,A             
6F31: BE             CP      (HL)            
6F32: 2F             CPL                     
6F33: 17             RLA                     
6F34: AF             XOR     A               
6F35: 55             LD      D,L             
6F36: 83             ADD     A,E             
6F37: 49             LD      C,C             
6F38: 03             INC     BC              
6F39: A0             AND     B               
6F3A: 01 B3 DB       LD      BC,$DBB3        
6F3D: 95             SUB     L               
6F3E: 5F             LD      E,A             
6F3F: BE             CP      (HL)            
6F40: 5B             LD      E,E             
6F41: B1             OR      C               
6F42: 4B             LD      C,E             
6F43: 7B             LD      A,E             
6F44: 16 A0          LD      D,$A0           
6F46: 51             LD      D,C             
6F47: DB 5B          IN      A,($5B)         
6F49: 98             SBC     B               
6F4A: 23             INC     HL              
6F4B: 63             LD      H,E             
6F4C: 19             ADD     HL,DE           
6F4D: BC             CP      H               
6F4E: 85             ADD     A,L             
6F4F: 73             LD      (HL),E          
6F50: 0E 71          LD      C,$71           
6F52: 86             ADD     A,(HL)          
6F53: 5F             LD      E,A             
6F54: C7             RST     0X00            
6F55: B5             OR      L               
6F56: 66             LD      H,(HL)          
6F57: 49             LD      C,C             
6F58: 2E 04          LD      L,$04           
6F5A: 07             RLCA                    
6F5B: 0B             DEC     BC              
6F5C: 05             DEC     B               
6F5D: 0A             LD      A,(BC)          
6F5E: 03             INC     BC              
6F5F: 02             LD      (BC),A          
6F60: 00             NOP                     
6F61: 96             SUB     (HL)            
6F62: 99             SBC     C               
6F63: 3E 00          LD      A,$00           
6F65: 03             INC     BC              
6F66: 0E 04          LD      C,$04           
6F68: 0C             INC     C               
6F69: 5F             LD      E,A             
6F6A: BE             CP      (HL)            
6F6B: 66             LD      H,(HL)          
6F6C: 17             RLA                     
6F6D: AB             XOR     E               
6F6E: A0             AND     B               
6F6F: 9B             SBC     E               
6F70: 6C             LD      L,H             
6F71: 1F             RRA                     
6F72: B8             CP      B               
6F73: 9B             SBC     E               
6F74: 5D             LD      E,L             
6F75: 04             INC     B               
6F76: 2B             DEC     HL              
6F77: 0B             DEC     BC              
6F78: 29             ADD     HL,HL           
6F79: 0A             LD      A,(BC)          
6F7A: 01 26 0E       LD      BC,$0E26        
6F7D: 24             INC     H               
6F7E: 14             INC     D               
6F7F: 1C             INC     E               
6F80: 40             LD      B,B             
6F81: 8D             ADC     A,L             
6F82: 0D             DEC     C               
6F83: 1E 04          LD      E,$04           
6F85: 1B             DEC     DE              
6F86: C7             RST     0X00            
6F87: DE 3A          SBC     $3A             
6F89: 15             DEC     D               
6F8A: 73             LD      (HL),E          
6F8B: 7B             LD      A,E             
6F8C: 5F             LD      E,A             
6F8D: BE             CP      (HL)            
6F8E: 5A             LD      E,D             
6F8F: 17             RLA                     
6F90: F3             DI                      
6F91: 5F             LD      E,A             
6F92: 8E             ADC     A,(HL)          
6F93: 48             LD      C,B             
6F94: 35             DEC     (HL)            
6F95: 15             DEC     D               
6F96: 12             LD      (DE),A          
6F97: 53             LD      D,E             
6F98: 56             LD      D,(HL)          
6F99: 5E             LD      E,(HL)          
6F9A: C8             RET     Z               
6F9B: 9C             SBC     H               
6F9C: 67             LD      H,A             
6F9D: B1             OR      C               
6F9E: 7F             LD      A,A             
6F9F: 5B             LD      E,E             
6FA0: 21 24 
```

# General Commands

```code
GeneralCommands:
6FA2: 00       LD      HL,$0024        
6FA3: 86             ADD     A,(HL)          
6FA4: 40             LD      B,B             
6FA5: 0E 86          LD      C,$86           
6FA7: 3D             DEC     A               
6FA8: 0D             DEC     C               
6FA9: 28 0E          JR      Z,$6FB9         
6FAB: 08             EX      AF,AF'          
6FAC: 0A             LD      A,(BC)          
6FAD: 01 0A 02       LD      BC,$020A        
6FB0: 0A             LD      A,(BC)          
6FB1: 03             INC     BC              
6FB2: 0A             LD      A,(BC)          
6FB3: 04             INC     B               
6FB4: 0E 1C          LD      C,$1C           
6FB6: 13             INC     DE              
6FB7: 0D             DEC     C               
6FB8: 19             ADD     HL,DE           
6FB9: 20 13          JR      NZ,$6FCE        
6FBB: 04             INC     B               
6FBC: 15             DEC     D               
6FBD: C7             RST     0X00            
6FBE: DE F3          SBC     $F3             
6FC0: 17             RLA                     
6FC1: CB 8C          RES     1,H             
6FC3: CF             RST     0X08            
6FC4: 47             LD      B,A             
6FC5: F5             PUSH    AF              
6FC6: 8B             ADC     A,E             
6FC7: D3 B8          OUT     ($B8),A         
6FC9: D0             RET     NC              
6FCA: 15             DEC     D               
6FCB: 6B             LD      L,E             
6FCC: BF             CP      A               
6FCD: 59             LD      E,C             
6FCE: 45             LD      B,L             
6FCF: 46             LD      B,(HL)          
6FD0: 48             LD      C,B             
6FD1: 2E 0B          LD      L,$0B           
6FD3: 86             ADD     A,(HL)          
6FD4: 10 0A          DJNZ    $6FE0           
6FD6: 05             DEC     B               
6FD7: 07             RLCA                    
6FD8: 0E 05          LD      C,$05           
6FDA: A2             AND     D               
6FDB: 13             INC     DE              
6FDC: 8F             ADC     A,A             
6FDD: 14             INC     D               
6FDE: 0C             INC     C               
6FDF: 43             LD      B,E             
6FE0: 0D             DEC     C               
6FE1: 0E 0B          LD      C,$0B           
6FE3: A2             AND     D               
6FE4: 13             INC     DE              
6FE5: 0D             DEC     C               
6FE6: 03             INC     BC              
6FE7: 1B             DEC     DE              
6FE8: 14             INC     D               
6FE9: 8F             ADC     A,A             
6FEA: 0D             DEC     C               
6FEB: 02             LD      (BC),A          
6FEC: 1A             LD      A,(DE)          
6FED: 8F             ADC     A,A             
6FEE: 06 34          LD      B,$34           
6FF0: 0E 32          LD      C,$32           
6FF2: 0D             DEC     C               
6FF3: 0E 1A          LD      C,$1A           
6FF5: 18 14          JR      $700B           
6FF7: 08             EX      AF,AF'          
6FF8: 37             SCF                     
6FF9: 10 04          DJNZ    $6FFF           
6FFB: 06 F9          LD      B,$F9           
6FFD: 5B             LD      E,E             
6FFE: 9F             SBC     A               
6FFF: A6             AND     (HL)            
7000: 9B             SBC     E               
7001: 5D             LD      E,L             
7002: 0D             DEC     C               
7003: 11 14 08       LD      DE,$0814        
7006: 37             SCF                     
7007: 04             INC     B               
7008: 0C             INC     C               
7009: C7             RST     0X00            
700A: DE 09          SBC     $09             
700C: 15             DEC     D               
700D: E6 96          AND     $96             
700F: 9B             SBC     E               
7010: 15             DEC     D               
7011: 5B             LD      E,E             
7012: CA 71 7B       JP      Z,$7B71         
7015: 04             INC     B               
7016: 0D             DEC     C               
7017: C7             RST     0X00            
7018: DE 57          SBC     $57             
701A: 17             RLA                     
701B: 5B             LD      E,E             
701C: 61             LD      H,C             
701D: 95             SUB     L               
701E: 5A             LD      E,D             
701F: 35             DEC     (HL)            
7020: 6F             LD      L,A             
7021: E6 BD          AND     $BD             
7023: 2E 11          LD      L,$11           
7025: 15             DEC     D               
7026: 0E 13          LD      C,$13           
7028: 13             INC     DE              
7029: 92             SUB     D               
702A: 0D             DEC     C               
702B: 0D             DEC     C               
702C: 1A             LD      A,(DE)          
702D: 15             DEC     D               
702E: 01 A8 04       LD      BC,$04A8        
7031: 07             RLCA                    
7032: 4B             LD      C,E             
7033: 7B             LD      A,E             
7034: 75             LD      (HL),L          
7035: 8D             ADC     A,L             
7036: A6             AND     (HL)            
7037: 85             ADD     A,L             
7038: 2E A5          LD      L,$A5           
703A: A6             AND     (HL)            
703B: 3A 12 0E       LD      A,($0E12)       
703E: 10 0D          DJNZ    $704D           
7040: 03             INC     BC              
7041: 1B             DEC     DE              
7042: 14             INC     D               
7043: 8F             ADC     A,A             
7044: 13             INC     DE              
7045: 92             SUB     D               
7046: A5             AND     L               
7047: A7             AND     A               
7048: 0D             DEC     C               
7049: 04             INC     B               
704A: 15             DEC     D               
704B: 01 2A 0C       LD      BC,$0C2A        
704E: A6             AND     (HL)            
704F: 40             LD      B,B             
7050: 24             INC     H               
7051: 0E 22          LD      C,$22           
7053: 13             INC     DE              
7054: 92             SUB     D               
7055: 0D             DEC     C               
7056: 0E 1A          LD      C,$1A           
7058: 15             DEC     D               
7059: 02             LD      (BC),A          
705A: A8             XOR     B               
705B: 04             INC     B               
705C: 08             EX      AF,AF'          
705D: 4B             LD      C,E             
705E: 7B             LD      A,E             
705F: 06 9A          LD      B,$9A           
7061: C2 16 A7       JP      NZ,$A716        
7064: 61             LD      H,C             
7065: 0D             DEC     C               
7066: 0E 29          LD      C,$29           
7068: A8             XOR     B               
7069: 04             INC     B               
706A: 0A             LD      A,(BC)          
706B: 4B             LD      C,E             
706C: 7B             LD      A,E             
706D: 09             ADD     HL,BC           
706E: 9A             SBC     D               
706F: DE 14          SBC     $14             
7071: D7             RST     0X10            
7072: A0             AND     B               
7073: 9B             SBC     E               
7074: 5D             LD      E,L             
7075: 42             LD      B,D             
7076: 2F             CPL                     
7077: 0E 2D          LD      C,$2D           
7079: 0D             DEC     C               
707A: 03             INC     BC              
707B: 1B             DEC     DE              
707C: 14             INC     D               
707D: 8F             ADC     A,A             
707E: 13             INC     DE              
707F: 92             SUB     D               
7080: 0D             DEC     C               
7081: 11 1A 14       LD      DE,$141A        
7084: 15             DEC     D               
7085: 01 A8 04       LD      BC,$04A8        
7088: 0A             LD      A,(BC)          
7089: 4B             LD      C,E             
708A: 7B             LD      A,E             
708B: 06 9A          LD      B,$9A           
708D: 49             LD      C,C             
708E: 16 97          LD      D,$97           
7090: 54             LD      D,H             
7091: 9B             SBC     E               
7092: 5D             LD      E,L             
7093: A5             AND     L               
7094: A7             AND     A               
7095: 0D             DEC     C               
7096: 0F             RRCA                    
7097: 2A A8 04       LD      HL,($04A8)      
709A: 0B             DEC     BC              
709B: 4B             LD      C,E             
709C: 7B             LD      A,E             
709D: 09             ADD     HL,BC           
709E: 9A             SBC     D               
709F: B0             OR      B               
70A0: 17             RLA                     
70A1: 75             LD      (HL),L          
70A2: 8D             ADC     A,L             
70A3: A6             AND     (HL)            
70A4: 85             ADD     A,L             
70A5: 2E 41          LD      L,$41           
70A7: 46             LD      B,(HL)          
70A8: 0E 44          LD      C,$44           
70AA: 0D             DEC     C               
70AB: 03             INC     BC              
70AC: 1B             DEC     DE              
70AD: 14             INC     D               
70AE: 8F             ADC     A,A             
70AF: 13             INC     DE              
70B0: 92             SUB     D               
70B1: A5             AND     L               
70B2: 0D             DEC     C               
70B3: 17             RLA                     
70B4: 14             INC     D               
70B5: 09             ADD     HL,BC           
70B6: 14             INC     D               
70B7: 04             INC     B               
70B8: 0A             LD      A,(BC)          
70B9: C7             RST     0X00            
70BA: DE D3          SBC     $D3             
70BC: 14             INC     D               
70BD: E6 96          AND     $96             
70BF: 49             LD      C,C             
70C0: 16 8B          LD      D,$8B           
70C2: 54             LD      D,H             
70C3: A8             XOR     B               
70C4: 04             INC     B               
70C5: 03             INC     BC              
70C6: 56             LD      D,(HL)          
70C7: D1             POP     DE              
70C8: 48             LD      C,B             
70C9: A9             XOR     C               
70CA: 8B             ADC     A,E             
70CB: 0D             DEC     C               
70CC: 11 1A 15       LD      DE,$151A        
70CF: 01 A8 04       LD      BC,$04A8        
70D2: 0B             DEC     BC              
70D3: 4B             LD      C,E             
70D4: 7B             LD      A,E             
70D5: 06 9A          LD      B,$9A           
70D7: B0             OR      B               
70D8: 17             RLA                     
70D9: 75             LD      (HL),L          
70DA: 8D             ADC     A,L             
70DB: A6             AND     (HL)            
70DC: 85             ADD     A,L             
70DD: 2E 0D          LD      L,$0D           
70DF: 0E 2A          LD      C,$2A           
70E1: A8             XOR     B               
70E2: 04             INC     B               
70E3: 0A             LD      A,(BC)          
70E4: 4B             LD      C,E             
70E5: 7B             LD      A,E             
70E6: 09             ADD     HL,BC           
70E7: 9A             SBC     D               
70E8: 49             LD      C,C             
70E9: 16 97          LD      D,$97           
70EB: 54             LD      D,H             
70EC: 9B             SBC     E               
70ED: 5D             LD      E,L             
70EE: 12             LD      (DE),A          
70EF: 21 0E 1F       LD      HL,$1F0E        
70F2: 13             INC     DE              
70F3: 0D             DEC     C               
70F4: 1C             INC     E               
70F5: 04             INC     B               
70F6: 13             INC     DE              
70F7: 33             INC     SP              
70F8: D1             POP     DE              
70F9: 09             ADD     HL,BC           
70FA: 15             DEC     D               
70FB: E6 96          AND     $96             
70FD: 51             LD      D,C             
70FE: 18 4E          JR      $714E           
7100: C2 98 5F       JP      NZ,$5F98        
7103: 56             LD      D,(HL)          
7104: 5E             LD      E,(HL)          
7105: DB 72          IN      A,($72)         
7107: 81             ADD     A,C             
7108: A6             AND     (HL)            
7109: 52             LD      D,D             
710A: 11 04 04       LD      DE,$0404        
710D: 49             LD      C,C             
710E: 48             LD      C,B             
710F: 7F             LD      A,A             
7110: 98             SBC     B               
7111: 09             ADD     HL,BC           
7112: 80             ADD     A,B             
7113: A1             AND     C               
7114: 0E 80          LD      C,$80           
7116: 9E             SBC     (HL)            
7117: 14             INC     D               
7118: 1B             DEC     DE              
7119: 14             INC     D               
711A: 0E 05          LD      C,$05           
711C: 09             ADD     HL,BC           
711D: 37             SCF                     
711E: 09             ADD     HL,BC           
711F: 00             NOP                     
7120: 8F             ADC     A,A             
7121: 0E 80          LD      C,$80           
7123: 84             ADD     A,H             
7124: 0D             DEC     C               
7125: 1A             LD      A,(DE)          
7126: 14             INC     D               
7127: 15             DEC     D               
7128: 40             LD      B,B             
7129: 14             INC     D               
712A: 09             ADD     HL,BC           
712B: 00             NOP                     
712C: 04             INC     B               
712D: 0A             LD      A,(BC)          
712E: C7             RST     0X00            
712F: DE D3          SBC     $D3             
7131: 14             INC     D               
7132: E6 96          AND     $96             
7134: AF             XOR     A               
7135: 15             DEC     D               
7136: B3             OR      E               
7137: B3             OR      E               
7138: A8             XOR     B               
7139: 04             INC     B               
713A: 03             INC     BC              
713B: 56             LD      D,(HL)          
713C: D1             POP     DE              
713D: 48             LD      C,B             
713E: A9             XOR     C               
713F: 8B             ADC     A,E             
7140: 13             INC     DE              
7141: 0D             DEC     C               
7142: 1C             INC     E               
7143: 1A             LD      A,(DE)          
7144: 14             INC     D               
7145: 15             DEC     D               
7146: 10 04          DJNZ    $714C           
7148: 14             INC     D               
7149: 73             LD      (HL),E          
714A: 7B             LD      A,E             
714B: 77             LD      (HL),A          
714C: 5B             LD      E,E             
714D: D0             RET     NC              
714E: B5             OR      L               
714F: C9             RET                     
7150: 9C             SBC     H               
7151: 36 A0          LD      (HL),$A0        
7153: 89             ADC     A,C             
7154: 17             RLA                     
7155: 96             SUB     (HL)            
7156: 14             INC     D               
7157: 45             LD      B,L             
7158: BD             CP      L               
7159: D6 83          SUB     $83             
715B: DB 72          IN      A,($72)         
715D: 11 8B 0D       LD      DE,$0D8B        
7160: 47             LD      B,A             
7161: 1A             LD      A,(DE)          
7162: 0E 04          LD      C,$04           
7164: 09             ADD     HL,BC           
7165: 37             SCF                     
7166: 09             ADD     HL,BC           
7167: 00             NOP                     
7168: 0B             DEC     BC              
7169: 3E 05          LD      A,$05           
716B: 55             LD      D,L             
716C: 13             INC     DE              
716D: 0D             DEC     C               
716E: 11 04 0D       LD      DE,$0D04        
7171: 44             LD      B,H             
7172: 45             LD      B,L             
7173: 89             ADC     A,C             
7174: 8D             ADC     A,L             
7175: 89             ADC     A,C             
7176: 17             RLA                     
7177: 82             ADD     A,D             
7178: 17             RLA                     
7179: 44             LD      B,H             
717A: 5E             LD      E,(HL)          
717B: 93             SUB     E               
717C: 9E             SBC     (HL)            
717D: 21 1D 04       LD      HL,$041D        
7180: AF             XOR     A               
7181: 14             INC     D               
7182: 04             INC     B               
7183: 12             LD      (DE),A          
7184: 59             LD      E,C             
7185: 45             LD      B,L             
7186: 3E 7A          LD      A,$7A           
7188: EF             RST     0X28            
7189: 16 1A          LD      D,$1A           
718B: 98             SBC     B               
718C: 90             SUB     B               
718D: 14             INC     D               
718E: 1B             DEC     DE              
718F: 58             LD      E,B             
7190: 1B             DEC     DE              
7191: A1             AND     C               
7192: D5             PUSH    DE              
7193: 92             SUB     D               
7194: 5B             LD      E,E             
7195: BB             CP      E               
7196: FF             RST     0X38            
7197: 10 0D          DJNZ    $71A6           
7199: 0E 04          LD      C,$04           
719B: 0A             LD      A,(BC)          
719C: C7             RST     0X00            
719D: DE AF          SBC     $AF             
719F: 14             INC     D               
71A0: 8F             ADC     A,A             
71A1: 48             LD      C,B             
71A2: 0A             LD      A,(BC)          
71A3: 58             LD      E,B             
71A4: 59             LD      E,C             
71A5: 7A             LD      A,D             
71A6: 1D             DEC     E               
71A7: 03             INC     BC              
71A8: 0D             DEC     C               
71A9: 0B             DEC     BC              
71AA: A8             XOR     B               
71AB: 04             INC     B               
71AC: 08             EX      AF,AF'          
71AD: 4B             LD      C,E             
71AE: 7B             LD      A,E             
71AF: 92             SUB     D               
71B0: C5             PUSH    BC              
71B1: 37             SCF                     
71B2: 49             LD      C,C             
71B3: 17             RLA                     
71B4: 60             LD      H,B             
71B5: 0A             LD      A,(BC)          
71B6: 01 07 15       LD      BC,$1507        
71B9: 26 0E          LD      H,$0E           
71BB: 24             INC     H               
71BC: 13             INC     DE              
71BD: 0D             DEC     C               
71BE: 21 04 0A       LD      HL,$0A04        
71C1: 80             ADD     A,B             
71C2: 5B             LD      E,E             
71C3: F3             DI                      
71C4: 23             INC     HL              
71C5: 5B             LD      E,E             
71C6: 4D             LD      C,L             
71C7: 4E             LD      C,(HL)          
71C8: B8             CP      B               
71C9: F9             LD      SP,HL           
71CA: 8E             ADC     A,(HL)          
71CB: A8             XOR     B               
71CC: 04             INC     B               
71CD: 12             LD      (DE),A          
71CE: 47             LD      B,A             
71CF: D2 C8 8B       JP      NC,$8BC8        
71D2: F3             DI                      
71D3: 23             INC     HL              
71D4: 55             LD      D,L             
71D5: BD             CP      L               
71D6: DB BD          IN      A,($BD)         
71D8: 41             LD      B,C             
71D9: 6E             LD      L,(HL)          
71DA: 03             INC     BC              
71DB: 58             LD      E,B             
71DC: 99             SBC     C               
71DD: 9B             SBC     E               
71DE: 5F             LD      E,A             
71DF: 4A             LD      C,D             
71E0: 17             RLA                     
71E1: 4C             LD      C,H             
71E2: 0E 4A          LD      C,$4A           
71E4: 13             INC     DE              
71E5: 0D             DEC     C               
71E6: 22 1A 15       LD      ($151A),HL      
71E9: 10 04          DJNZ    $71EF           
71EB: 09             ADD     HL,BC           
71EC: 46             LD      B,(HL)          
71ED: 77             LD      (HL),A          
71EE: 05             DEC     B               
71EF: A0             AND     B               
71F0: 16 BC          LD      D,$BC           
71F2: 90             SUB     B               
71F3: 73             LD      (HL),E          
71F4: 4B             LD      C,E             
71F5: A8             XOR     B               
71F6: 04             INC     B               
71F7: 11 4E D1       LD      DE,$D14E        
71FA: 15             DEC     D               
71FB: 8A             ADC     A,D             
71FC: 50             LD      D,B             
71FD: BD             CP      L               
71FE: 15             DEC     D               
71FF: 58             LD      E,B             
7200: 8E             ADC     A,(HL)          
7201: BE             CP      (HL)            
7202: 08             EX      AF,AF'          
7203: 8A             ADC     A,D             
7204: BE             CP      (HL)            
7205: A0             AND     B               
7206: 56             LD      D,(HL)          
7207: 72             LD      (HL),D          
7208: 2E 0D          LD      L,$0D           
720A: 23             INC     HL              
720B: 04             INC     B               
720C: 10 CF          DJNZ    $71DD           
720E: 62             LD      H,D             
720F: 8B             ADC     A,E             
7210: 96             SUB     (HL)            
7211: 9B             SBC     E               
7212: 64             LD      H,H             
7213: 1B             DEC     DE              
7214: A1             AND     C               
7215: 47             LD      B,A             
7216: 55             LD      D,L             
7217: B3             OR      E               
7218: 8B             ADC     A,E             
7219: C3 54 A3       JP      $A354           
721C: 91             SUB     C               
721D: A8             XOR     B               
721E: 04             INC     B               
721F: 0E 73          LD      C,$73           
7221: 7B             LD      A,E             
7222: 47             LD      B,A             
7223: D2 C8 8B       JP      NC,$8BC8        
7226: F3             DI                      
7227: 23             INC     HL              
7228: EE 72          XOR     $72             
722A: 1B             DEC     DE              
722B: A3             AND     E               
722C: 3F             CCF                     
722D: A1             AND     C               
722E: 0B             DEC     BC              
722F: 36 0E          LD      (HL),$0E        
7231: 34             INC     (HL)            
7232: 13             INC     DE              
7233: 0D             DEC     C               
7234: 17             RLA                     
7235: 1A             LD      A,(DE)          
7236: 15             DEC     D               
7237: 04             INC     B               
7238: 04             INC     B               
7239: 10 3F          DJNZ    $727A           
723B: B9             CP      C               
723C: 82             ADD     A,D             
723D: 62             LD      H,D             
723E: 91             SUB     C               
723F: 7A             LD      A,D             
7240: D5             PUSH    DE              
7241: 15             DEC     D               
7242: 04             INC     B               
7243: 18 8E          JR      $71D3           
7245: 7B             LD      A,E             
7246: 83             ADD     A,E             
7247: 61             LD      H,C             
7248: 03             INC     BC              
7249: A0             AND     B               
724A: AA             XOR     D               
724B: 8B             ADC     A,E             
724C: 0D             DEC     C               
724D: 18 04          JR      $7253           
724F: 14             INC     D               
7250: 5F             LD      E,A             
7251: BE             CP      (HL)            
7252: 5D             LD      E,L             
7253: B1             OR      C               
7254: D0             RET     NC              
7255: B5             OR      L               
7256: 02             LD      (BC),A          
7257: A1             AND     C               
7258: 91             SUB     C               
7259: 7A             LD      A,D             
725A: 62             LD      H,D             
725B: 17             RLA                     
725C: DB 5F          IN      A,($5F)         
725E: 33             INC     SP              
725F: 48             LD      C,B             
7260: B9             CP      C               
7261: 46             LD      B,(HL)          
7262: 73             LD      (HL),E          
7263: C6 A8          ADD     $A8             
7265: 8B             ADC     A,E             
7266: 0C             INC     C               
7267: 17             RLA                     
7268: 0E 15          LD      C,$15           
726A: 13             INC     DE              
726B: 0D             DEC     C               
726C: 12             LD      (DE),A          
726D: 04             INC     B               
726E: 0E 5F          LD      C,$5F           
7270: BE             CP      (HL)            
7271: 5D             LD      E,L             
7272: B1             OR      C               
7273: D0             RET     NC              
7274: B5             OR      L               
7275: 02             LD      (BC),A          
7276: A1             AND     C               
7277: 91             SUB     C               
7278: 7A             LD      A,D             
7279: B0             OR      B               
727A: 17             RLA                     
727B: F4 59 A8       CALL    P,$A859         
727E: 8B             ADC     A,E             
727F: 10 15          DJNZ    $7296           
7281: 0E 13          LD      C,$13           
7283: 13             INC     DE              
7284: 0D             DEC     C               
7285: 10 04          DJNZ    $728B           
7287: 0C             INC     C               
7288: 5F             LD      E,A             
7289: BE             CP      (HL)            
728A: 5D             LD      E,L             
728B: B1             OR      C               
728C: D0             RET     NC              
728D: B5             OR      L               
728E: 02             LD      (BC),A          
728F: A1             AND     C               
7290: 91             SUB     C               
7291: 7A             LD      A,D             
7292: D0             RET     NC              
7293: 15             DEC     D               
7294: A8             XOR     B               
7295: 8B             ADC     A,E             
7296: 1B             DEC     DE              
7297: 1E 0E          LD      E,$0E           
7299: 1C             INC     E               
729A: 13             INC     DE              
729B: 0D             DEC     C               
729C: 03             INC     BC              
729D: 08             EX      AF,AF'          
729E: 00             NOP                     
729F: 07             RLCA                    
72A0: 0D             DEC     C               
72A1: 14             INC     D               
72A2: 04             INC     B               
72A3: 10 5F          DJNZ    $7304           
72A5: BE             CP      (HL)            
72A6: 5B             LD      E,E             
72A7: B1             OR      C               
72A8: 4B             LD      C,E             
72A9: 7B             LD      A,E             
72AA: 06 9A          LD      B,$9A           
72AC: 90             SUB     B               
72AD: 73             LD      (HL),E          
72AE: C3 6A 07       JP      $076A           
72B1: B3             OR      E               
72B2: 33             INC     SP              
72B3: 98             SBC     B               
72B4: A8             XOR     B               
72B5: 8B             ADC     A,E             
72B6: 1C             INC     E               
72B7: 32 0E 30       LD      ($300E),A       
72BA: 13             INC     DE              
72BB: 0D             DEC     C               
72BC: 17             RLA                     
72BD: 08             EX      AF,AF'          
72BE: 00             NOP                     
72BF: 04             INC     B               
72C0: 13             INC     DE              
72C1: 5F             LD      E,A             
72C2: BE             CP      (HL)            
72C3: 5B             LD      E,E             
72C4: B1             OR      C               
72C5: 4B             LD      C,E             
72C6: 7B             LD      A,E             
72C7: 06 9A          LD      B,$9A           
72C9: 90             SUB     B               
72CA: 73             LD      (HL),E          
72CB: C4 6A A3       CALL    NZ,$A36A        
72CE: 60             LD      H,B             
72CF: 33             INC     SP              
72D0: 98             SBC     B               
72D1: C7             RST     0X00            
72D2: DE 2E          SBC     $2E             
72D4: 0D             DEC     C               
72D5: 14             INC     D               
72D6: 04             INC     B               
72D7: 10 5F          DJNZ    $7338           
72D9: BE             CP      (HL)            
72DA: 5B             LD      E,E             
72DB: B1             OR      C               
72DC: 4B             LD      C,E             
72DD: 7B             LD      A,E             
72DE: 06 9A          LD      B,$9A           
72E0: 90             SUB     B               
72E1: 73             LD      (HL),E          
72E2: C4 6A A3       CALL    NZ,$A36A        
72E5: 60             LD      H,B             
72E6: 33             INC     SP              
72E7: 98             SBC     B               
72E8: A8             XOR     B               
72E9: 8B             ADC     A,E             
72EA: 1D             DEC     E               
72EB: 16 04          LD      D,$04           
72ED: 14             INC     D               
72EE: 9F             SBC     A               
72EF: 77             LD      (HL),A          
72F0: AF             XOR     A               
72F1: 14             INC     D               
72F2: 91             SUB     C               
72F3: 7A             LD      A,D             
72F4: 95             SUB     L               
72F5: 14             INC     D               
72F6: D3 14          OUT     ($14),A         
72F8: 68             LD      L,B             
72F9: B1             OR      C               
72FA: 33             INC     SP              
72FB: C5             PUSH    BC              
72FC: 4B             LD      C,E             
72FD: 49             LD      C,C             
72FE: 45             LD      B,L             
72FF: 77             LD      (HL),A          
7300: 81             ADD     A,C             
7301: 48             LD      C,B             
7302: 21 1A 0E       LD      HL,$0E1A        
7305: 18 0D          JR      $7314           
7307: 05             DEC     B               
7308: 03             INC     BC              
7309: 00             NOP                     
730A: 3A 00 8E       LD      A,($8E00)       
730D: 0D             DEC     C               
730E: 0F             RRCA                    
730F: 04             INC     B               
7310: 0A             LD      A,(BC)          
7311: C7             RST     0X00            
7312: DE 81          SBC     $81             
7314: 15             DEC     D               
7315: 04             INC     B               
7316: BC             CP      H               
7317: 8E             ADC     A,(HL)          
7318: 62             LD      H,D             
7319: 47             LD      B,A             
731A: 62             LD      H,D             
731B: 17             RLA                     
731C: 3A 00 22       LD      A,($2200)       
731F: 12             LD      (DE),A          
7320: 04             INC     B               
7321: 10 5B          DJNZ    $737E           
7323: E0             RET     PO              
7324: 27             DAA                     
7325: 60             LD      H,B             
7326: 31 60 41       LD      SP,$4160        
7329: A0             AND     B               
732A: 49             LD      C,C             
732B: A0             AND     B               
732C: 89             ADC     A,C             
732D: D3 89          OUT     ($89),A         
732F: D3 69          OUT     ($69),A         
7331: CE 23          ADC     $23             
7333: 01 24 25       LD      BC,$2524        
7336: 20 04          JR      NZ,$733C        
7338: 1E C7          LD      E,$C7           
733A: DE AF          SBC     $AF             
733C: 23             INC     HL              
733D: 99             SBC     C               
733E: 16 09          LD      D,$09           
7340: BC             CP      H               
7341: 8E             ADC     A,(HL)          
7342: 62             LD      H,D             
7343: 91             SUB     C               
7344: 7A             LD      A,D             
7345: 90             SUB     B               
7346: 14             INC     D               
7347: FA DF 2F       JP      M,$2FDF         
734A: 62             LD      H,D             
734B: 16 EE          LD      D,$EE           
734D: 7B             LD      A,E             
734E: B4             OR      H               
734F: 46             LD      B,(HL)          
7350: 45             LD      B,L             
7351: 2F             CPL                     
7352: 7B             LD      A,E             
7353: 03             INC     BC              
7354: 56             LD      D,(HL)          
7355: 27             DAA                     
7356: A0             AND     B               
7357: 26 20          LD      H,$20           
7359: 0E 1E          LD      C,$1E           
735B: 13             INC     DE              
735C: 0D             DEC     C               
735D: 13             INC     DE              
735E: 1A             LD      A,(DE)          
735F: 15             DEC     D               
7360: 10 A8          DJNZ    $730A           
7362: 04             INC     B               
7363: 0D             DEC     C               
7364: 40             LD      B,B             
7365: D2 F3 23       JP      NC,$23F3        
7368: F6 8B          OR      $8B             
736A: 51             LD      D,C             
736B: 18 52          JR      $73BF           
736D: C2 65 49       JP      NZ,$4965        
7370: 21 04 06       LD      HL,$0604        
7373: 09             ADD     HL,BC           
7374: 9A             SBC     D               
7375: FA 17 70       JP      M,$7017         
7378: 49             LD      C,C             
7379: 3D             DEC     A               
737A: 01 91 27       LD      BC,$2791        
737D: 0E 0E          LD      C,$0E           
737F: 0C             INC     C               
7380: 13             INC     DE              
7381: 04             INC     B               
7382: 09             ADD     HL,BC           
7383: 25             DEC     H               
7384: A1             AND     C               
7385: AB             XOR     E               
7386: 70             LD      (HL),B          
7387: 3B             DEC     SP              
7388: 95             SUB     L               
7389: 77             LD      (HL),A          
738A: BF             CP      A               
738B: 21 44 09       LD      HL,$0944        
738E: 04             INC     B               
738F: 07             RLCA                    
7390: AF             XOR     A               
7391: 6E             LD      L,(HL)          
7392: 83             ADD     A,E             
7393: 62             LD      H,D             
7394: C5             PUSH    BC              
7395: 98             SBC     B               
7396: 21 45 31       LD      HL,$3145        
7399: 0E 2F          LD      C,$2F           
739B: 13             INC     DE              
739C: 0D             DEC     C               
739D: 12             LD      (DE),A          
739E: 1A             LD      A,(DE)          
739F: 15             DEC     D               
73A0: 10 A8          DJNZ    $734A           
73A2: 04             INC     B               
73A3: 0C             INC     C               
73A4: 72             LD      (HL),D          
73A5: B1             OR      C               
73A6: 87             ADD     A,A             
73A7: 8C             ADC     A,H             
73A8: 33             INC     SP              
73A9: BB             CP      E               
73AA: DF             RST     0X18            
73AB: 1B             DEC     DE              
73AC: 09             ADD     HL,BC           
73AD: 8D             ADC     A,L             
73AE: 63             LD      H,E             
73AF: F4 0D 18       CALL    P,$180D         
73B2: 04             INC     B               
73B3: 14             INC     D               
73B4: 16 A0          LD      D,$A0           
73B6: 43             LD      B,E             
73B7: DB E4          IN      A,($E4)         
73B9: 14             INC     D               
73BA: 83             ADD     A,E             
73BB: 4A             LD      C,D             
73BC: 01 18 3E       LD      BC,$3E18        
73BF: C5             PUSH    BC              
73C0: 7B             LD      A,E             
73C1: 17             RLA                     
73C2: CB 8C          RES     1,H             
73C4: 6B             LD      L,E             
73C5: BF             CP      A               
73C6: 5F             LD      E,A             
73C7: BE             CP      (HL)            
73C8: 11 8B 46       LD      DE,$468B        
73CB: 08             EX      AF,AF'          
73CC: 04             INC     B               
73CD: 06 46          LD      B,$46           
73CF: 77             LD      (HL),A          
73D0: 98             SBC     B               
73D1: C5             PUSH    BC              
73D2: 5B             LD      E,E             
73D3: A2             AND     D               
73D4: 47             LD      B,A             
73D5: 09             ADD     HL,BC           
73D6: 04             INC     B               
73D7: 07             RLCA                    
73D8: 29             ADD     HL,HL           
73D9: D1             POP     DE              
73DA: 20 16          JR      NZ,$73F2        
73DC: 85             ADD     A,L             
73DD: A1             AND     C               
73DE: 3F             CCF                     
73DF: 4A             LD      C,D             
73E0: 18 0E          JR      $73F0           
73E2: 16 13          LD      D,$13           
73E4: 0D             DEC     C               
73E5: 13             INC     DE              
73E6: 04             INC     B               
73E7: 11 9E 77       LD      DE,$779E        
73EA: 08             EX      AF,AF'          
73EB: 8A             ADC     A,D             
73EC: C6 9F          ADD     $9F             
73EE: 6B             LD      L,E             
73EF: A1             AND     C               
73F0: C7             RST     0X00            
73F1: DE 90          SBC     $90             
73F3: 14             INC     D               
73F4: FA DF 2F       JP      M,$2FDF         
73F7: 62             LD      H,D             
73F8: 21 49 26       LD      HL,$2649        
73FB: 0E 24          LD      C,$24           
73FD: 13             INC     DE              
73FE: 0D             DEC     C               
73FF: 11 09 00       LD      DE,$0009        
7402: A8             XOR     B               
7403: 04             INC     B               
7404: 0C             INC     C               
7405: 09             ADD     HL,BC           
7406: 4F             LD      C,A             
7407: CB B5          RES     6,L             
7409: 89             ADC     A,C             
740A: 96             SUB     (HL)            
740B: 67             LD      H,A             
740C: B1             OR      C               
740D: 90             SUB     B               
740E: BE             CP      (HL)            
740F: 5B             LD      E,E             
7410: 70             LD      (HL),B          
7411: 04             INC     B               
7412: 0E 5F          LD      C,$5F           
7414: BE             CP      (HL)            
7415: 44             LD      B,H             
7416: DB 6B          IN      A,($6B)         
7418: A1             AND     C               
7419: 83             ADD     A,E             
741A: 7A             LD      A,D             
741B: AF             XOR     A               
741C: 6E             LD      L,(HL)          
741D: 83             ADD     A,E             
741E: 62             LD      H,D             
741F: CF             RST     0X08            
7420: 98             SBC     B               
7421: 28 36          JR      Z,$7459         
7423: 0E 34          LD      C,$34           
7425: 13             INC     DE              
7426: 0D             DEC     C               
7427: 16 1A          LD      D,$1A           
7429: 15             DEC     D               
742A: 10 A8          DJNZ    $73D4           
742C: 04             INC     B               
742D: 10 60          DJNZ    $748F           
742F: 7B             LD      A,E             
7430: F3             DI                      
7431: 23             INC     HL              
7432: 70             LD      (HL),B          
7433: 75             LD      (HL),L          
7434: C3 6E 33       JP      $336E           
7437: 17             RLA                     
7438: 2E 6D          LD      L,$6D           
743A: 99             SBC     C               
743B: 16 5B          LD      D,$5B           
743D: D4 0D 19       CALL    NC,$190D        
7440: 04             INC     B               
7441: 0D             DEC     C               
7442: 80             ADD     A,B             
7443: 5B             LD      E,E             
7444: F3             DI                      
7445: 23             INC     HL              
7446: C7             RST     0X00            
7447: DE 20          SBC     $20             
7449: 16 6B          LD      D,$6B           
744B: A1             AND     C               
744C: 5B             LD      E,E             
744D: BE             CP      (HL)            
744E: 54             LD      D,H             
744F: A8             XOR     B               
7450: 04             INC     B               
7451: 07             RLCA                    
7452: 10 53          DJNZ    $74A7           
7454: F3             DI                      
7455: 23             INC     HL              
7456: 96             SUB     (HL)            
7457: 5F             LD      E,A             
7458: 21 29 36       LD      HL,$3629        
745B: 0E 34          LD      C,$34           
745D: 13             INC     DE              
745E: 0D             DEC     C               
745F: 16 1B          LD      D,$1B           
7461: 15             DEC     D               
7462: 10 A9          DJNZ    $740D           
7464: 04             INC     B               
7465: 10 60          DJNZ    $74C7           
7467: 7B             LD      A,E             
7468: F3             DI                      
7469: 23             INC     HL              
746A: 70             LD      (HL),B          
746B: 75             LD      (HL),L          
746C: C3 6E 33       JP      $336E           
746F: 17             RLA                     
7470: 2E 6D          LD      L,$6D           
7472: 99             SBC     C               
7473: 16 5B          LD      D,$5B           
7475: D4 0D 19       CALL    NC,$190D        
7478: 04             INC     B               
7479: 17             RLA                     
747A: 43             LD      B,E             
747B: 79             LD      A,C             
747C: C7             RST     0X00            
747D: DE D3          SBC     $D3             
747F: 14             INC     D               
7480: 88             ADC     A,B             
7481: 96             SUB     (HL)            
7482: 8E             ADC     A,(HL)          
7483: 7A             LD      A,D             
7484: 7B             LD      A,E             
7485: 14             INC     D               
7486: C7             RST     0X00            
7487: 93             SUB     E               
7488: 76             HALT                    
7489: BE             CP      (HL)            
748A: BD             CP      L               
748B: 15             DEC     D               
748C: 49             LD      C,C             
748D: 90             SUB     B               
748E: 67             LD      H,A             
748F: 48             LD      C,B             
7490: 21 2F 07       LD      HL,$072F        
7493: 04             INC     B               
7494: 05             DEC     B               
7495: 9B             SBC     E               
7496: 29             ADD     HL,HL           
7497: 57             LD      D,A             
7498: C6 3E          ADD     $3E             
749A: 2D             DEC     L               
749B: 09             ADD     HL,BC           
749C: 0E 07          LD      C,$07           
749E: 13             INC     DE              
749F: 0D             DEC     C               
74A0: 02             LD      (BC),A          
74A1: 1A             LD      A,(DE)          
74A2: 8F             ADC     A,A             
74A3: 14             INC     D               
74A4: 0C             INC     C               
74A5: 48             LD      C,B             
74A6: 11 0E 0F       LD      DE,$0F0E        
74A9: 13             INC     DE              
74AA: 04             INC     B               
74AB: 0C             INC     C               
74AC: C7             RST     0X00            
74AD: DE D3          SBC     $D3             
74AF: 14             INC     D               
74B0: E6 96          AND     $96             
74B2: 09             ADD     HL,BC           
74B3: 15             DEC     D               
74B4: 82             ADD     A,D             
74B5: 17             RLA                     
74B6: 97             SUB     A               
74B7: 49             LD      C,C             
74B8: 33             INC     SP              
74B9: 27             DAA                     
74BA: 0E 25          LD      C,$25           
74BC: 13             INC     DE              
74BD: 04             INC     B               
74BE: 22 0F A0       LD      ($A00F),HL      
74C1: 5F             LD      E,A             
74C2: 17             RLA                     
74C3: 46             LD      B,(HL)          
74C4: 48             LD      C,B             
74C5: 66             LD      H,(HL)          
74C6: 17             RLA                     
74C7: D3 61          OUT     ($61),A         
74C9: 04             INC     B               
74CA: 68             LD      L,B             
74CB: 63             LD      H,E             
74CC: 16 5B          LD      D,$5B           
74CE: 99             SBC     C               
74CF: 56             LD      D,(HL)          
74D0: 98             SBC     B               
74D1: C0             RET     NZ              
74D2: 16 49          LD      D,$49           
74D4: 5E             LD      E,(HL)          
74D5: 90             SUB     B               
74D6: 78             LD      A,B             
74D7: 0E BC          LD      C,$BC           
74D9: 92             SUB     D               
74DA: 5F             LD      E,A             
74DB: 59             LD      E,C             
74DC: 15             DEC     D               
74DD: 9B             SBC     E               
74DE: AF             XOR     A               
74DF: 19             ADD     HL,DE           
74E0: A1             AND     C               
74E1: 34             INC     (HL)            
74E2: 23             INC     HL              
74E3: 0E 21          LD      C,$21           
74E5: 13             INC     DE              
74E6: 04             INC     B               
74E7: 1E C7          LD      E,$C7           
74E9: DE 95          SBC     $95             
74EB: AF             XOR     A               
74EC: D5             PUSH    DE              
74ED: C3 65 62       JP      $6265           
74F0: D5             PUSH    DE              
74F1: 15             DEC     D               
74F2: 67             LD      H,A             
74F3: 16 67          LD      D,$67           
74F5: 49             LD      C,C             
74F6: 66             LD      H,(HL)          
74F7: B1             OR      C               
74F8: D0             RET     NC              
74F9: 15             DEC     D               
74FA: 3F             CCF                     
74FB: 16 ED          LD      D,$ED           
74FD: 48             LD      C,B             
74FE: 90             SUB     B               
74FF: 14             INC     D               
7500: 04             INC     B               
7501: 58             LD      E,B             
7502: 30 A1          JR      NC,$74A5        
7504: 09             ADD     HL,BC           
7505: 5C             LD      E,H             
7506: 36 14          LD      (HL),$14        
7508: 0E 12          LD      C,$12           
750A: 13             INC     DE              
750B: 0D             DEC     C               
750C: 0F             RRCA                    
750D: 04             INC     B               
750E: 0B             DEC     BC              
750F: C7             RST     0X00            
7510: DE D3          SBC     $D3             
7512: 14             INC     D               
7513: E6 96          AND     $96             
7515: 77             LD      (HL),A          
7516: 15             DEC     D               
7517: 0B             DEC     BC              
7518: BC             CP      H               
7519: 4E             LD      C,(HL)          
751A: A8             XOR     B               
751B: 8B             ADC     A,E             
751C: 37             SCF                     
751D: 12             LD      (DE),A          
751E: 0E 10          LD      C,$10           
7520: 13             INC     DE              
7521: 0D             DEC     C               
7522: 0D             DEC     C               
7523: 04             INC     B               
7524: 09             ADD     HL,BC           
7525: C7             RST     0X00            
7526: DE 94          SBC     $94             
7528: 14             INC     D               
7529: 85             ADD     A,L             
752A: 61             LD      H,C             
752B: 0B             DEC     BC              
752C: BC             CP      H               
752D: 4E             LD      C,(HL)          
752E: A8             XOR     B               
752F: 8B             ADC     A,E             
7530: 38 1D          JR      C,$754F         
7532: 0E 1B          LD      C,$1B           
7534: 13             INC     DE              
7535: 0D             DEC     C               
7536: 18 04          JR      $753C           
7538: 14             INC     D               
7539: 5F             LD      E,A             
753A: BE             CP      (HL)            
753B: 5B             LD      E,E             
753C: B1             OR      C               
753D: 4B             LD      C,E             
753E: 7B             LD      A,E             
753F: 06 9A          LD      B,$9A           
7541: 30 15          JR      NC,$7558        
7543: 29             ADD     HL,HL           
7544: A1             AND     C               
7545: 14             INC     D               
7546: 71             LD      (HL),C          
7547: 3F             CCF                     
7548: A0             AND     B               
7549: B0             OR      B               
754A: 17             RLA                     
754B: F4 59 A8       CALL    P,$A859         
754E: 8B             ADC     A,E             
754F: 39             ADD     HL,SP           
7550: 1D             DEC     E               
7551: 0E 1B          LD      C,$1B           
7553: 13             INC     DE              
7554: 0D             DEC     C               
7555: 18 04          JR      $755B           
7557: 16 C7          LD      D,$C7           
7559: DE FB          SBC     $FB             
755B: 17             RLA                     
755C: F3             DI                      
755D: 8C             ADC     A,H             
755E: 58             LD      E,B             
755F: 72             LD      (HL),D          
7560: 56             LD      D,(HL)          
7561: 5E             LD      E,(HL)          
7562: D2 9C 73       JP      NC,$739C        
7565: C6 73          ADD     $73             
7567: 7B             LD      A,E             
7568: 83             ADD     A,E             
7569: 7A             LD      A,D             
756A: 5F             LD      E,A             
756B: BE             CP      (HL)            
756C: 7F             LD      A,A             
756D: B1             OR      C               
756E: 0D             DEC     C               
756F: 2B             DEC     HL              
7570: 0E 29          LD      C,$29           
7572: 0D             DEC     C               
7573: 25             DEC     H               
7574: 1A             LD      A,(DE)          
7575: 8F             ADC     A,A             
7576: 0E 21          LD      C,$21           
7578: 0D             DEC     C               
7579: 1E 0E          LD      E,$0E           
757B: 07             RLCA                    
757C: 14             INC     D               
757D: 15             DEC     D               
757E: 10 1B          DJNZ    $759B           
7580: 14             INC     D               
7581: 15             DEC     D               
7582: 40             LD      B,B             
7583: A8             XOR     B               
7584: 04             INC     B               
7585: 0F             RRCA                    
7586: 07             RLCA                    
7587: 4F             LD      C,A             
7588: 17             RLA                     
7589: 98             SBC     B               
758A: CA B5 37       JP      Z,$37B5         
758D: 49             LD      C,C             
758E: F5             PUSH    AF              
758F: 8B             ADC     A,E             
7590: D3 B8          OUT     ($B8),A         
7592: B8             CP      B               
7593: 16 46          LD      D,$46           
7595: A9             XOR     C               
7596: 8B             ADC     A,E             
7597: 10 13          DJNZ    $75AC           
7599: 14             INC     D               
759A: 0C             INC     C               
759B: 0E 13          LD      C,$13           
759D: 0E 11          LD      C,$11           
759F: 13             INC     DE              
75A0: 0D             DEC     C               
75A1: 0E A9          LD      C,$A9           
75A3: 04             INC     B               
75A4: 0B             DEC     BC              
75A5: 77             LD      (HL),A          
75A6: 5B             LD      E,E             
75A7: 05             DEC     B               
75A8: B9             CP      C               
75A9: 19             ADD     HL,DE           
75AA: BC             CP      H               
75AB: 9E             SBC     (HL)            
75AC: 48             LD      C,B             
75AD: D6 15          SUB     $15             
75AF: 2E 0F          LD      L,$0F           
75B1: 17             RLA                     
75B2: 0E 15          LD      C,$15           
75B4: 0D             DEC     C               
75B5: 03             INC     BC              
75B6: 1A             LD      A,(DE)          
75B7: 14             INC     D               
75B8: 8F             ADC     A,A             
75B9: 13             INC     DE              
75BA: 0D             DEC     C               
75BB: 0D             DEC     C               
75BC: A8             XOR     B               
75BD: 04             INC     B               
75BE: 08             EX      AF,AF'          
75BF: 40             LD      B,B             
75C0: D2 F3 23       JP      NC,$23F3        
75C3: 16 67          LD      D,$67           
75C5: D0             RET     NC              
75C6: 15             DEC     D               
75C7: A9             XOR     C               
75C8: 8B             ADC     A,E             
75C9: 07             RLCA                    
75CA: 1A             LD      A,(DE)          
75CB: 0D             DEC     C               
75CC: 18 04          JR      $75D2           
75CE: 15             DEC     D               
75CF: C7             RST     0X00            
75D0: DE 94          SBC     $94             
75D2: 14             INC     D               
75D3: 45             LD      B,L             
75D4: 5E             LD      E,(HL)          
75D5: 3C             INC     A               
75D6: 49             LD      C,C             
75D7: D0             RET     NC              
75D8: DD                                  
75D9: D6 6A          SUB     $6A             
75DB: DB 72          IN      A,($72)         
75DD: FE 67          CP      $67             
75DF: 89             ADC     A,C             
75E0: 8D             ADC     A,L             
75E1: 91             SUB     C               
75E2: 7A             LD      A,D             
75E3: 3A 06 
```

# Helper Commands

```code
HelperCommands:
75E5: 00   
75E6: 87             ADD     A,A             
75E7: AE             XOR     (HL)            
75E8: 81             ADD     A,C             
75E9: 14             INC     D               
75EA: 04             INC     B               
75EB: 12             LD      (DE),A          
75EC: 99             SBC     C               
75ED: 48             LD      C,B             
75EE: 5F             LD      E,A             
75EF: BE             CP      (HL)            
75F0: 95             SUB     L               
75F1: AF             XOR     A               
75F2: 8E             ADC     A,(HL)          
75F3: 91             SUB     C               
75F4: 12             LD      (DE),A          
75F5: 8A             ADC     A,D             
75F6: FE 46          CP      $46             
75F8: F3             DI                      
75F9: 5F             LD      E,A             
75FA: 01 B3 DB       LD      BC,$DBB3        
75FD: 95             SUB     L               
75FE: 82             ADD     A,D             
75FF: 11 04 0F       LD      DE,$0F04        
7602: 5F             LD      E,A             
7603: BE             CP      (HL)            
7604: 23             INC     HL              
7605: 15             DEC     D               
7606: 15             DEC     D               
7607: BA             CP      D               
7608: B5             OR      L               
7609: D0             RET     NC              
760A: 0A             LD      A,(BC)          
760B: BC             CP      H               
760C: 46             LD      B,(HL)          
760D: 48             LD      C,B             
760E: 1B             DEC     DE              
760F: D0             RET     NC              
7610: 2E 83          LD      L,$83           
7612: 12             LD      (DE),A          
7613: 04             INC     B               
7614: 10 5F          DJNZ    $7675           
7616: BE             CP      (HL)            
7617: 99             SBC     C               
7618: 16 C2          LD      D,$C2           
761A: B3             OR      E               
761B: E1             POP     HL              
761C: EB             EX      DE,HL           
761D: 82             ADD     A,D             
761E: C6 9B          ADD     $9B             
7620: 15             DEC     D               
7621: 11 8D 5F       LD      DE,$5F8D        
7624: 4A             LD      C,D             
7625: 84             ADD     A,H             
7626: 1C             INC     E               
7627: 04             INC     B               
7628: 1A             LD      A,(DE)          
7629: 03             INC     BC              
762A: A0             AND     B               
762B: 5F             LD      E,A             
762C: BE             CP      (HL)            
762D: 61             LD      H,C             
762E: 17             RLA                     
762F: 82             ADD     A,D             
7630: C6 F3          ADD     $F3             
7632: 17             RLA                     
7633: F3             DI                      
7634: 8C             ADC     A,H             
7635: 5F             LD      E,A             
7636: BE             CP      (HL)            
7637: 5B             LD      E,E             
7638: B1             OR      C               
7639: 4B             LD      C,E             
763A: 7B             LD      A,E             
763B: 49             LD      C,C             
763C: 45             LD      B,L             
763D: 67             LD      H,A             
763E: B1             OR      C               
763F: 86             ADD     A,(HL)          
7640: 96             SUB     (HL)            
7641: 44             LD      B,H             
7642: A0             AND     B               
7643: 85             ADD     A,L             
7644: 1B             DEC     DE              
7645: 04             INC     B               
7646: 19             ADD     HL,DE           
7647: 03             INC     BC              
7648: A0             AND     B               
7649: 5F             LD      E,A             
764A: BE             CP      (HL)            
764B: 99             SBC     C               
764C: 16 C2          LD      D,$C2           
764E: B3             OR      E               
764F: F3             DI                      
7650: 17             RLA                     
7651: F3             DI                      
7652: 8C             ADC     A,H             
7653: 5F             LD      E,A             
7654: BE             CP      (HL)            
7655: 5B             LD      E,E             
7656: B1             OR      C               
7657: 4B             LD      C,E             
7658: 7B             LD      A,E             
7659: 54             LD      D,H             
765A: 45             LD      B,L             
765B: F3             DI                      
765C: 5F             LD      E,A             
765D: 81             ADD     A,C             
765E: 5B             LD      E,E             
765F: 52             LD      D,D             
7660: 86             ADD     A,(HL)          
7661: 1C             INC     E               
7662: 04             INC     B               
7663: 1A             LD      A,(DE)          
7664: 03             INC     BC              
7665: A0             AND     B               
7666: 5F             LD      E,A             
7667: BE             CP      (HL)            
7668: 99             SBC     C               
7669: 16 C2          LD      D,$C2           
766B: B3             OR      E               
766C: F3             DI                      
766D: 17             RLA                     
766E: F3             DI                      
766F: 8C             ADC     A,H             
7670: 5F             LD      E,A             
7671: BE             CP      (HL)            
7672: 5B             LD      E,E             
7673: B1             OR      C               
7674: 4B             LD      C,E             
7675: 7B             LD      A,E             
7676: 49             LD      C,C             
7677: 45             LD      B,L             
7678: 67             LD      H,A             
7679: B1             OR      C               
767A: 86             ADD     A,(HL)          
767B: 96             SUB     (HL)            
767C: 44             LD      B,H             
767D: A0             AND     B               
767E: 87             ADD     A,A             
767F: 1B             DEC     DE              
7680: 04             INC     B               
7681: 19             ADD     HL,DE           
7682: 03             INC     BC              
7683: A0             AND     B               
7684: 5F             LD      E,A             
7685: BE             CP      (HL)            
7686: 61             LD      H,C             
7687: 17             RLA                     
7688: 82             ADD     A,D             
7689: C6 F3          ADD     $F3             
768B: 17             RLA                     
768C: F3             DI                      
768D: 8C             ADC     A,H             
768E: 5F             LD      E,A             
768F: BE             CP      (HL)            
7690: 5B             LD      E,E             
7691: B1             OR      C               
7692: 4B             LD      C,E             
7693: 7B             LD      A,E             
7694: 54             LD      D,H             
7695: 45             LD      B,L             
7696: F3             DI                      
7697: 5F             LD      E,A             
7698: 81             ADD     A,C             
7699: 5B             LD      E,E             
769A: 52             LD      D,D             
769B: 88             ADC     A,B             
769C: 1B             DEC     DE              
769D: 04             INC     B               
769E: 19             ADD     HL,DE           
769F: 03             INC     BC              
76A0: A0             AND     B               
76A1: 5F             LD      E,A             
76A2: BE             CP      (HL)            
76A3: 23             INC     HL              
76A4: 15             DEC     D               
76A5: F3             DI                      
76A6: B9             CP      C               
76A7: 0E D0          LD      C,$D0           
76A9: 16 8A          LD      D,$8A           
76AB: F4 72 4B       CALL    P,$4B72         
76AE: 5E             LD      E,(HL)          
76AF: C3 B5 B6       JP      $B6B5           
76B2: 14             INC     D               
76B3: 1B             DEC     DE              
76B4: C4 81 5B       CALL    NZ,$5B81        
76B7: 52             LD      D,D             
76B8: 89             ADC     A,C             
76B9: 1B             DEC     DE              
76BA: 04             INC     B               
76BB: 19             ADD     HL,DE           
76BC: 03             INC     BC              
76BD: A0             AND     B               
76BE: 5F             LD      E,A             
76BF: BE             CP      (HL)            
76C0: F7             RST     0X30            
76C1: 17             RLA                     
76C2: F3             DI                      
76C3: B9             CP      C               
76C4: 0E D0          LD      C,$D0           
76C6: 16 8A          LD      D,$8A           
76C8: F4 72 4B       CALL    P,$4B72         
76CB: 5E             LD      E,(HL)          
76CC: C3 B5 B6       JP      $B6B5           
76CF: 14             INC     D               
76D0: 1B             DEC     DE              
76D1: C4 81 5B       CALL    NZ,$5B81        
76D4: 52             LD      D,D             
76D5: 8A             ADC     A,D             
76D6: 0D             DEC     C               
76D7: 04             INC     B               
76D8: 0B             DEC     BC              
76D9: 23             INC     HL              
76DA: D1             POP     DE              
76DB: 13             INC     DE              
76DC: 54             LD      D,H             
76DD: 4B             LD      C,E             
76DE: 7B             LD      A,E             
76DF: C9             RET                     
76E0: 54             LD      D,H             
76E1: A6             AND     (HL)            
76E2: B7             OR      A               
76E3: 2E 8C          LD      L,$8C           
76E5: 17             RLA                     
76E6: 0B             DEC     BC              
76E7: 15             DEC     D               
76E8: 05             DEC     B               
76E9: 7F             LD      A,A             
76EA: 07             RLCA                    
76EB: 04             INC     B               
76EC: 05             DEC     B               
76ED: 63             LD      H,E             
76EE: BE             CP      (HL)            
76EF: CB B5          RES     6,L             
76F1: 53             LD      D,E             
76F2: FF             RST     0X38            
76F3: 09             ADD     HL,BC           
76F4: 04             INC     B               
76F5: 07             RLCA                    
76F6: C7             RST     0X00            
76F7: DE 94          SBC     $94             
76F9: 14             INC     D               
76FA: 4B             LD      C,E             
76FB: 5E             LD      E,(HL)          
76FC: 4E             LD      C,(HL)          
76FD: 8B             ADC     A,E             
76FE: 04             INC     B               
76FF: 04             INC     B               
7700: 02             LD      (BC),A          
7701: 3B             DEC     SP              
7702: F4 8D 11       CALL    P,$118D         
7705: 0D             DEC     C               
7706: 0F             RRCA                    
7707: 14             INC     D               
7708: 20 38          JR      NZ,$7742        
770A: 15             DEC     D               
770B: 02             LD      (BC),A          
770C: AA             XOR     D               
770D: 04             INC     B               
770E: 07             RLCA                    
770F: 4B             LD      C,E             
7710: 7B             LD      A,E             
7711: C9             RET                     
7712: 54             LD      D,H             
7713: A6             AND     (HL)            
7714: B7             OR      A               
7715: 2E 8F          LD      L,$8F           
7717: 4F             LD      C,A             
7718: 0D             DEC     C               
7719: 4D             LD      C,L             
771A: 0E 4A          LD      C,$4A           
771C: 2D             DEC     L               
771D: 37             SCF                     
771E: 0D             DEC     C               
771F: 1A             LD      A,(DE)          
7720: 15             DEC     D               
7721: 10 04          DJNZ    $7727           
7723: 16 46          LD      D,$46           
7725: 77             LD      (HL),A          
7726: 05             DEC     B               
7727: A0             AND     B               
7728: 16 BC          LD      D,$BC           
772A: 90             SUB     B               
772B: 73             LD      (HL),E          
772C: CA 83 59       JP      Z,$5983         
772F: 5E             LD      E,(HL)          
7730: 46             LD      B,(HL)          
7731: 7A             LD      A,D             
7732: E1             POP     HL              
7733: 14             INC     D               
7734: 5F             LD      E,A             
7735: A0             AND     B               
7736: D6 B0          SUB     $B0             
7738: DB 63          IN      A,($63)         
773A: 0D             DEC     C               
773B: 1F             RRA                     
773C: 14             INC     D               
773D: 15             DEC     D               
773E: 20 04          JR      NZ,$7744        
7740: 18 C7          JR      $7709           
7742: DE 94          SBC     $94             
7744: 14             INC     D               
7745: 53             LD      D,E             
7746: 5E             LD      E,(HL)          
7747: D6 C4          SUB     $C4             
7749: 4B             LD      C,E             
774A: 5E             LD      E,(HL)          
774B: 13             INC     DE              
774C: 98             SBC     B               
774D: 44             LD      B,H             
774E: A4             AND     H               
774F: DB 8B          IN      A,($8B)         
7751: C3 9E 6F       JP      $6F9E           
7754: B1             OR      C               
7755: 53             LD      D,E             
7756: A1             AND     C               
7757: AB             XOR     E               
7758: 98             SBC     B               
7759: AA             XOR     D               
775A: 8B             ADC     A,E             
775B: 18 0D          JR      $776A           
775D: 08             EX      AF,AF'          
775E: 0F             RRCA                    
775F: AA             XOR     D               
7760: 04             INC     B               
7761: 04             INC     B               
7762: 4D             LD      C,L             
7763: BD             CP      L               
7764: A7             AND     A               
7765: 61             LD      H,C             
7766: 18 A2          JR      $770A           
7768: 13             INC     DE              
7769: 0D             DEC     C               
776A: 11 1A 18       LD      DE,$181A        
776D: 04             INC     B               
776E: 0B             DEC     BC              
776F: C7             RST     0X00            
7770: DE 8E          SBC     $8E             
7772: 14             INC     D               
7773: 63             LD      H,E             
7774: B1             OR      C               
7775: FB             EI                      
7776: 5C             LD      E,H             
7777: 58             LD      E,B             
7778: 72             LD      (HL),D          
7779: 45             LD      B,L             
777A: AA             XOR     D               
777B: 8B             ADC     A,E             
777C: 90             SUB     B               
777D: 09             ADD     HL,BC           
777E: 0B             DEC     BC              
777F: 07             RLCA                    
7780: 0A             LD      A,(BC)          
7781: 36 01          LD      (HL),$01        
7783: 91             SUB     C               
7784: 37             SCF                     
7785: 01 91 91       LD      BC,$9191        
7788: 19             ADD     HL,DE           
7789: 1F             RRA                     
778A: 17             RLA                     
778B: FF             RST     0X38            
778C: A5             AND     L               
778D: 57             LD      D,A             
778E: 49             LD      C,C             
778F: B5             OR      L               
7790: 17             RLA                     
7791: 46             LD      B,(HL)          
7792: 5E             LD      E,(HL)          
7793: 2F             CPL                     
7794: 7B             LD      A,E             
7795: 03             INC     BC              
7796: 56             LD      D,(HL)          
7797: 1D             DEC     E               
7798: A0             AND     B               
7799: A6             AND     (HL)            
779A: 16 3F          LD      D,$3F           
779C: BB             CP      E               
779D: 11 EE 99       LD      DE,$99EE        
77A0: AF             XOR     A               
77A1: 2E 92          LD      L,$92           
77A3: 18 0D          JR      $77B2           
77A5: 16 1A          LD      D,$1A           
77A7: 14             INC     D               
77A8: 15             DEC     D               
77A9: 08             EX      AF,AF'          
77AA: 04             INC     B               
77AB: 0E C7          LD      C,$C7           
77AD: DE D3          SBC     $D3             
77AF: 14             INC     D               
77B0: E6 96          AND     $96             
77B2: 09             ADD     HL,BC           
77B3: 15             DEC     D               
77B4: 82             ADD     A,D             
77B5: 17             RLA                     
77B6: 73             LD      (HL),E          
77B7: 49             LD      C,C             
77B8: 6B             LD      L,E             
77B9: BF             CP      A               
77BA: A8             XOR     B               
77BB: 8B             ADC     A,E             
77BC: 94             SUB     H               
77BD: 80             ADD     A,B             
77BE: 8C             ADC     A,H             
77BF: 0D             DEC     C               
77C0: 80             ADD     A,B             
77C1: 89             ADC     A,C             
77C2: 17             RLA                     
77C3: 1C             INC     E               
77C4: 00             NOP                     
77C5: 17             RLA                     
77C6: 1D             DEC     E               
77C7: 00             NOP                     
77C8: 17             RLA                     
77C9: 1E 00          LD      E,$00           
77CB: 17             RLA                     
77CC: 1F             RRA                     
77CD: 00             NOP                     
77CE: 17             RLA                     
77CF: 20 00          JR      NZ,$77D1        
77D1: 17             RLA                     
77D2: 21 00 17       LD      HL,$1700        
77D5: 22 00 17       LD      ($1700),HL      
77D8: 23             INC     HL              
77D9: 00             NOP                     
77DA: 17             RLA                     
77DB: 24             INC     H               
77DC: 00             NOP                     
77DD: 17             RLA                     
77DE: 25             DEC     H               
77DF: 00             NOP                     
77E0: 17             RLA                     
77E1: 26 00          LD      H,$00           
77E3: 17             RLA                     
77E4: 27             DAA                     
77E5: 00             NOP                     
77E6: 17             RLA                     
77E7: 28 00          JR      Z,$77E9         
77E9: 17             RLA                     
77EA: 29             ADD     HL,HL           
77EB: 00             NOP                     
77EC: 17             RLA                     
77ED: 2A 00 17       LD      HL,($1700)      
77F0: 2B             DEC     HL              
77F1: 00             NOP                     
77F2: 17             RLA                     
77F3: 2C             INC     L               
77F4: 00             NOP                     
77F5: 17             RLA                     
77F6: 1B             DEC     DE              
77F7: 8E             ADC     A,(HL)          
77F8: 17             RLA                     
77F9: 14             INC     D               
77FA: 00             NOP                     
77FB: 17             RLA                     
77FC: 16 81          LD      D,$81           
77FE: 17             RLA                     
77FF: 3B             DEC     SP              
7800: 82             ADD     A,D             
7801: 17             RLA                     
7802: 3D             DEC     A               
7803: 00             NOP                     
7804: 17             RLA                     
7805: 15             DEC     D               
7806: 00             NOP                     
7807: 17             RLA                     
7808: 39             ADD     HL,SP           
7809: 00             NOP                     
780A: 17             RLA                     
780B: 41             LD      B,C             
780C: 8C             ADC     A,H             
780D: 0B             DEC     BC              
780E: 2B             DEC     HL              
780F: 05             DEC     B               
7810: 55             LD      D,L             
7811: 0B             DEC     BC              
7812: 0D             DEC     C               
7813: 09             ADD     HL,BC           
7814: 17             RLA                     
7815: 15             DEC     D               
7816: 82             ADD     A,D             
7817: 1C             INC     E               
7818: 1F             RRA                     
7819: 95             SUB     L               
781A: 1C             INC     E               
781B: 23             INC     HL              
781C: 95             SUB     L               
781D: AB             XOR     E               
781E: 0E 0D          LD      C,$0D           
7820: 0C             INC     C               
7821: 17             RLA                     
7822: 39             ADD     HL,SP           
7823: 82             ADD     A,D             
7824: 1C             INC     E               
7825: 21 95 1C       LD      HL,$1C95        
7828: 3D             DEC     A               
7829: 95             SUB     L               
782A: 1C             INC     E               
782B: 23             INC     HL              
782C: 95             SUB     L               
782D: FF             RST     0X38            
782E: 0B             DEC     BC              
782F: 0D             DEC     C               
7830: 09             ADD     HL,BC           
7831: 17             RLA                     
7832: 39             ADD     HL,SP           
7833: 82             ADD     A,D             
7834: 1C             INC     E               
7835: 1F             RRA                     
7836: 95             SUB     L               
7837: 1C             INC     E               
7838: 25             DEC     H               
7839: 95             SUB     L               
783A: 1C             INC     E               
783B: 1D             DEC     E               
783C: 95             SUB     L               
783D: 1C             INC     E               
783E: 27             DAA                     
783F: 95             SUB     L               
7840: 1C             INC     E               
7841: 29             ADD     HL,HL           
7842: 95             SUB     L               
7843: 1C             INC     E               
7844: 2B             DEC     HL              
7845: 95             SUB     L               
7846: 17             RLA                     
7847: 2E 95          LD      L,$95           
7849: 00             NOP                     
784A: 88             ADC     A,B             
784B: 95             SUB     L               
784C: 53             LD      D,E             
784D: 0D             DEC     C               
784E: 51             LD      D,C             
784F: 2B             DEC     HL              
7850: 0B             DEC     BC              
7851: 4E             LD      C,(HL)          
7852: 05             DEC     B               
7853: 18 05          JR      $785A           
7855: 0D             DEC     C               
7856: 03             INC     BC              
7857: 19             ADD     HL,DE           
7858: 85             ADD     A,L             
7859: 10 30          DJNZ    $788B           
785B: 05             DEC     B               
785C: 0D             DEC     C               
785D: 03             INC     BC              
785E: 19             ADD     HL,DE           
785F: 86             ADD     A,(HL)          
7860: 10 47          DJNZ    $78A9           
7862: 05             DEC     B               
7863: 0D             DEC     C               
7864: 03             INC     BC              
7865: 19             ADD     HL,DE           
7866: 89             ADC     A,C             
7867: 10 5E          DJNZ    $78C7           
7869: 05             DEC     B               
786A: 0D             DEC     C               
786B: 03             INC     BC              
786C: 19             ADD     HL,DE           
786D: 8B             ADC     A,E             
786E: 10 75          DJNZ    $78E5           
7870: 05             DEC     B               
7871: 0D             DEC     C               
7872: 03             INC     BC              
7873: 19             ADD     HL,DE           
7874: 8D             ADC     A,L             
7875: 10 8C          DJNZ    $7803           
7877: 05             DEC     B               
7878: 0D             DEC     C               
7879: 03             INC     BC              
787A: 19             ADD     HL,DE           
787B: 90             SUB     B               
787C: 10 A3          DJNZ    $7821           
787E: 05             DEC     B               
787F: 0D             DEC     C               
7880: 03             INC     BC              
7881: 19             ADD     HL,DE           
7882: 92             SUB     D               
7883: 10 BA          DJNZ    $783F           
7885: 05             DEC     B               
7886: 0D             DEC     C               
7887: 03             INC     BC              
7888: 19             ADD     HL,DE           
7889: 96             SUB     (HL)            
788A: 10 D1          DJNZ    $785D           
788C: 05             DEC     B               
788D: 0D             DEC     C               
788E: 03             INC     BC              
788F: 19             ADD     HL,DE           
7890: 97             SUB     A               
7891: 10 E8          DJNZ    $787B           
7893: 05             DEC     B               
7894: 0D             DEC     C               
7895: 03             INC     BC              
7896: 19             ADD     HL,DE           
7897: 98             SBC     B               
7898: 10 FF          DJNZ    $7899           
789A: 05             DEC     B               
789B: 0D             DEC     C               
789C: 03             INC     BC              
789D: 19             ADD     HL,DE           
789E: 94             SUB     H               
789F: 10 A3          DJNZ    $7844           
78A1: 61             LD      H,C             
78A2: 0D             DEC     C               
78A3: 5F             LD      E,A             
78A4: 2C             INC     L               
78A5: 13             INC     DE              
78A6: 19             ADD     HL,DE           
78A7: 88             ADC     A,B             
78A8: 1F             RRA                     
78A9: 59             LD      E,C             
78AA: C7             RST     0X00            
78AB: DE 4F          SBC     $4F             
78AD: 15             DEC     D               
78AE: 33             INC     SP              
78AF: 61             LD      H,C             
78B0: 4B             LD      C,E             
78B1: 49             LD      C,C             
78B2: 69             LD      L,C             
78B3: BE             CP      (HL)            
78B4: 7A             LD      A,D             
78B5: C4 51 18       CALL    NZ,$1851        
78B8: 4A             LD      C,D             
78B9: C2 CF 49       JP      NZ,$49CF        
78BC: FF             RST     0X38            
78BD: 15             DEC     D               
78BE: F3             DI                      
78BF: B9             CP      C               
78C0: F3             DI                      
78C1: 49             LD      C,C             
78C2: B0             OR      B               
78C3: 85             ADD     A,L             
78C4: F3             DI                      
78C5: 5F             LD      E,A             
78C6: 79             LD      A,C             
78C7: 68             LD      L,B             
78C8: 43             LD      B,E             
78C9: 90             SUB     B               
78CA: CF             RST     0X08            
78CB: 17             RLA                     
78CC: 7B             LD      A,E             
78CD: B4             OR      H               
78CE: 80             ADD     A,B             
78CF: 8D             ADC     A,L             
78D0: C4 6A F3       CALL    NZ,$F36A        
78D3: 46             LD      B,(HL)          
78D4: EF             RST     0X28            
78D5: 5B             LD      E,E             
78D6: 5B             LD      E,E             
78D7: 48             LD      C,B             
78D8: B9             CP      C               
78D9: 46             LD      B,(HL)          
78DA: 73             LD      (HL),E          
78DB: C6 75          ADD     $75             
78DD: 5B             LD      E,E             
78DE: 84             ADD     A,H             
78DF: BF             CP      A               
78E0: C3 B5 33       JP      $33B5           
78E3: 98             SBC     B               
78E4: 46             LD      B,(HL)          
78E5: A4             AND     H               
78E6: E6 59          AND     $59             
78E8: 39             ADD     HL,SP           
78E9: 17             RLA                     
78EA: F5             PUSH    AF              
78EB: 9F             SBC     A               
78EC: 5B             LD      E,E             
78ED: F4 34 A1       CALL    P,$A134         
78F0: 82             ADD     A,D             
78F1: 17             RLA                     
78F2: 29             ADD     HL,HL           
78F3: A1             AND     C               
78F4: 4D             LD      C,L             
78F5: 75             LD      (HL),L          
78F6: 94             SUB     H               
78F7: 14             INC     D               
78F8: B3             OR      E               
78F9: 63             LD      H,E             
78FA: 3A 1E 2F       LD      A,($2F1E)       
78FD: 62             LD      H,D             
78FE: 8F             ADC     A,A             
78FF: 14             INC     D               
7900: B8             CP      B               
7901: 15             DEC     D               
7902: 22 96 62       LD      ($6296),HL      
7905: 04             INC     B               
7906: 60             LD      H,B             
7907: 55             LD      D,L             
7908: 45             LD      B,L             
7909: 84             ADD     A,H             
790A: 74             LD      (HL),H          
790B: 73             LD      (HL),E          
790C: C1             POP     BC              
790D: F0             RET     P               
790E: 68             LD      L,B             
790F: 7B             LD      A,E             
7910: 9B             SBC     E               
7911: 81             ADD     A,C             
7912: 8D             ADC     A,L             
7913: 50             LD      D,B             
7914: 86             ADD     A,(HL)          
7915: CF             RST     0X08            
7916: 6A             LD      L,D             
7917: 83             ADD     A,E             
7918: 48             LD      C,B             
7919: FB             EI                      
791A: B9             CP      C               
791B: 4D             LD      C,L             
791C: 98             SBC     B               
791D: 8F             ADC     A,A             
791E: 16 2C          LD      D,$2C           
7920: 49             LD      C,C             
7921: DB E0          IN      A,($E0)         
7923: DB 72          IN      A,($72)         
7925: 81             ADD     A,C             
7926: 8D             ADC     A,L             
7927: CB 87          RES     0,A             
7929: 73             LD      (HL),E          
792A: 49             LD      C,C             
792B: C7             RST     0X00            
792C: DE FC          SBC     $FC             
792E: ED                                  
792F: 09             ADD     HL,BC           
7930: 4F             LD      C,A             
7931: D0             RET     NC              
7932: 15             DEC     D               
7933: 82             ADD     A,D             
7934: 17             RLA                     
7935: 52             LD      D,D             
7936: 5E             LD      E,(HL)          
7937: 75             LD      (HL),L          
7938: B1             OR      C               
7939: 8D             ADC     A,L             
793A: 61             LD      H,C             
793B: 51             LD      D,C             
793C: 5E             LD      E,(HL)          
793D: 90             SUB     B               
793E: 64             LD      H,H             
793F: E9             JP      (HL)            
7940: 48             LD      C,B             
7941: F1             POP     AF              
7942: 8B             ADC     A,E             
7943: 84             ADD     A,H             
7944: 96             SUB     (HL)            
7945: 0B             DEC     BC              
7946: A0             AND     B               
7947: 54             LD      D,H             
7948: A4             AND     H               
7949: D9             EXX                     
794A: BD             CP      L               
794B: BB             CP      E               
794C: 15             DEC     D               
794D: 5B             LD      E,E             
794E: 48             LD      C,B             
794F: 5F             LD      E,A             
7950: BE             CP      (HL)            
7951: 6B             LD      L,E             
7952: 16 2E          LD      D,$2E           
7954: 6D             LD      L,L             
7955: 35             DEC     (HL)            
7956: 79             LD      A,C             
7957: 0E BC          LD      C,$BC           
7959: 86             ADD     A,(HL)          
795A: 5F             LD      E,A             
795B: 23             INC     HL              
795C: 62             LD      H,D             
795D: 83             ADD     A,E             
795E: 7A             LD      A,D             
795F: 5F             LD      E,A             
7960: BE             CP      (HL)            
7961: 01 18 7E       LD      BC,$7E18        
7964: B2             OR      D               
7965: E3             EX      (SP),HL         
7966: 06 97          LD      B,$97           
7968: 20 04          JR      NZ,$796E        
796A: 1E D2          LD      E,$D2           
796C: 97             SUB     A               
796D: BF             CP      A               
796E: 9F             SBC     A               
796F: 03             INC     BC              
7970: A0             AND     B               
7971: 4B             LD      C,E             
7972: 7B             LD      A,E             
7973: F0             RET     P               
7974: B3             OR      E               
7975: 10 99          DJNZ    $7910           
7977: CA 6A 4B       JP      Z,$4B6A         
797A: 7B             LD      A,E             
797B: 50             LD      D,B             
797C: 72             LD      (HL),D          
797D: 0B             DEC     BC              
797E: 5C             LD      E,H             
797F: 4F             LD      C,A             
7980: A1             AND     C               
7981: 96             SUB     (HL)            
7982: AF             XOR     A               
7983: DB 72          IN      A,($72)         
7985: 0E D0          LD      C,$D0           
7987: 2F             CPL                     
7988: 8E             ADC     A,(HL)          
7989: 98             SBC     B               
798A: 80             ADD     A,B             
798B: 80             ADD     A,B             
798C: 04             INC     B               
798D: 7E             LD      A,(HL)          
798E: 4F             LD      C,A             
798F: 45             LD      B,L             
7990: 83             ADD     A,E             
7991: 48             LD      C,B             
7992: 83             ADD     A,E             
7993: 7A             LD      A,D             
7994: 59             LD      E,C             
7995: 45             LD      B,L             
7996: 96             SUB     (HL)            
7997: 73             LD      (HL),E          
7998: 48             LD      C,B             
7999: 5E             LD      E,(HL)          
799A: F5             PUSH    AF              
799B: B2             OR      D               
799C: 33             INC     SP              
799D: 89             ADC     A,C             
799E: 44             LD      B,H             
799F: 45             LD      B,L             
79A0: 2F             CPL                     
79A1: 62             LD      H,D             
79A2: 73             LD      (HL),E          
79A3: C1             POP     BC              
79A4: 8E             ADC     A,(HL)          
79A5: 48             LD      C,B             
79A6: A9             XOR     C               
79A7: 15             DEC     D               
79A8: C3 8B AB       JP      $AB8B           
79AB: 98             SBC     B               
79AC: 52             LD      D,D             
79AD: 45             LD      B,L             
79AE: 3F             CCF                     
79AF: 48             LD      C,B             
79B0: 3F             CCF                     
79B1: C0             RET     NZ              
79B2: 90             SUB     B               
79B3: 14             INC     D               
79B4: 04             INC     B               
79B5: 58             LD      E,B             
79B6: F5             PUSH    AF              
79B7: B3             OR      E               
79B8: 15             DEC     D               
79B9: 71             LD      (HL),C          
79BA: 2F             CPL                     
79BB: 60             LD      H,B             
79BC: D6 B5          SUB     $B5             
79BE: C4 9C 52       CALL    NZ,$529C        
79C1: 5E             LD      E,(HL)          
79C2: D0             RET     NC              
79C3: 47             LD      B,A             
79C4: 90             SUB     B               
79C5: BE             CP      (HL)            
79C6: D9             EXX                     
79C7: 6A             LD      L,D             
79C8: 56             LD      D,(HL)          
79C9: 72             LD      (HL),D          
79CA: 49             LD      C,C             
79CB: 16 A5          LD      D,$A5           
79CD: 9F             SBC     A               
79CE: 43             LD      B,E             
79CF: 16 9B          LD      D,$9B           
79D1: 85             ADD     A,L             
79D2: 46             LD      B,(HL)          
79D3: 45             LD      B,L             
79D4: 44             LD      B,H             
79D5: A0             AND     B               
79D6: C0             RET     NZ              
79D7: 16 C0          LD      D,$C0           
79D9: 16 51          LD      D,$51           
79DB: 5E             LD      E,(HL)          
79DC: 96             SUB     (HL)            
79DD: 64             LD      H,H             
79DE: DB 72          IN      A,($72)         
79E0: 0E D0          LD      C,$D0           
79E2: 2F             CPL                     
79E3: 8E             ADC     A,(HL)          
79E4: 9F             SBC     A               
79E5: 15             DEC     D               
79E6: 49             LD      C,C             
79E7: 16 A5          LD      D,$A5           
79E9: 9F             SBC     A               
79EA: B2             OR      D               
79EB: 17             RLA                     
79EC: FC ED 47       CALL    M,$47ED         
79EF: 63             LD      H,E             
79F0: 8F             ADC     A,A             
79F1: 14             INC     D               
79F2: 7B             LD      A,E             
79F3: 14             INC     D               
79F4: AB             XOR     E               
79F5: 6E             LD      L,(HL)          
79F6: DB BD          IN      A,($BD)         
79F8: 3E 49          LD      A,$49           
79FA: 35             DEC     (HL)            
79FB: 60             LD      H,B             
79FC: AB             XOR     E               
79FD: BB             CP      E               
79FE: 8A             ADC     A,D             
79FF: 91             SUB     C               
7A00: 8B             ADC     A,E             
7A01: 16 47          LD      D,$47           
7A03: 90             SUB     B               
7A04: 63             LD      H,E             
7A05: 63             LD      H,E             
7A06: 85             ADD     A,L             
7A07: A5             AND     L               
7A08: 65             LD      H,L             
7A09: 49             LD      C,C             
7A0A: 6C             LD      L,H             
7A0B: 9C             SBC     H               
7A0C: 99             SBC     C               
7A0D: 22 04 20       LD      ($2004),HL      
7A10: 85             ADD     A,L             
7A11: A5             AND     L               
7A12: 65             LD      H,L             
7A13: 49             LD      C,C             
7A14: D5             PUSH    DE              
7A15: 9C             SBC     H               
7A16: 2F             CPL                     
7A17: 60             LD      H,B             
7A18: D6 B5          SUB     $B5             
7A1A: C4 9C 52       CALL    NZ,$529C        
7A1D: 5E             LD      E,(HL)          
7A1E: D0             RET     NC              
7A1F: 47             LD      B,A             
7A20: 90             SUB     B               
7A21: BE             CP      (HL)            
7A22: C3 6A 09       JP      $096A           
7A25: 15             DEC     D               
7A26: A3             AND     E               
7A27: A0             AND     B               
7A28: 03             INC     BC              
7A29: A0             AND     B               
7A2A: 0F             RRCA                    
7A2B: A0             AND     B               
7A2C: F3             DI                      
7A2D: 17             RLA                     
7A2E: 17             RLA                     
7A2F: 8D             ADC     A,L             
7A30: 9D             SBC     L               
7A31: 14             INC     D               
7A32: 04             INC     B               
7A33: 12             LD      (DE),A          
7A34: 5F             LD      E,A             
7A35: BE             CP      (HL)            
7A36: 5B             LD      E,E             
7A37: B1             OR      C               
7A38: 4B             LD      C,E             
7A39: 7B             LD      A,E             
7A3A: 44             LD      B,H             
7A3B: 45             LD      B,L             
7A3C: 67             LD      H,A             
7A3D: 8E             ADC     A,(HL)          
7A3E: E3             EX      (SP),HL         
7A3F: 16 F3          LD      D,$F3           
7A41: 8C             ADC     A,H             
7A42: F4 72 DB       CALL    P,$DB72         
7A45: 63             LD      H,E             
7A46: 9F             SBC     A               
7A47: 50             LD      D,B             
7A48: 1F             RRA                     
7A49: 4E             LD      C,(HL)          
7A4A: 55             LD      D,L             
7A4B: 45             LD      B,L             
7A4C: 84             ADD     A,H             
7A4D: 74             LD      (HL),H          
7A4E: 73             LD      (HL),E          
7A4F: C1             POP     BC              
7A50: 09             ADD     HL,BC           
7A51: BA             CP      D               
7A52: AB             XOR     E               
7A53: 54             LD      D,H             
7A54: 17             RLA                     
7A55: EE 9A          XOR     $9A             
7A57: 9A             SBC     D               
7A58: CF             RST     0X08            
7A59: 49             LD      C,C             
7A5A: 8F             ADC     A,A             
7A5B: 96             SUB     (HL)            
7A5C: 83             ADD     A,E             
7A5D: 48             LD      C,B             
7A5E: A3             AND     E               
7A5F: D0             RET     NC              
7A60: 10 B2          DJNZ    $7A14           
7A62: C3 6A B6       JP      $B66A           
7A65: 14             INC     D               
7A66: 36 A0          LD      (HL),$A0        
7A68: 59             LD      E,C             
7A69: DB 96          IN      A,($96)         
7A6B: 73             LD      (HL),E          
7A6C: 55             LD      D,L             
7A6D: 5E             LD      E,(HL)          
7A6E: 31 C6 D3       LD      SP,$D3C6        
7A71: 78             LD      A,B             
7A72: 09             ADD     HL,BC           
7A73: 8A             ADC     A,D             
7A74: 80             ADD     A,B             
7A75: A1             AND     C               
7A76: 90             SUB     B               
7A77: 14             INC     D               
7A78: 0A             LD      A,(BC)          
7A79: 58             LD      E,B             
7A7A: BE             CP      (HL)            
7A7B: 9F             SBC     A               
7A7C: 91             SUB     C               
7A7D: 7A             LD      A,D             
7A7E: 7B             LD      A,E             
7A7F: 14             INC     D               
7A80: 54             LD      D,H             
7A81: 8B             ADC     A,E             
7A82: 9B             SBC     E               
7A83: 6C             LD      L,H             
7A84: 12             LD      (DE),A          
7A85: 76             HALT                    
7A86: 7F             LD      A,A             
7A87: 9E             SBC     (HL)            
7A88: AB             XOR     E               
7A89: B2             OR      D               
7A8A: CB 51          BIT     2,C             
7A8C: D5             PUSH    DE              
7A8D: B5             OR      L               
7A8E: 54             LD      D,H             
7A8F: BD             CP      L               
7A90: 91             SUB     C               
7A91: 7A             LD      A,D             
7A92: 96             SUB     (HL)            
7A93: 14             INC     D               
7A94: 51             LD      D,C             
7A95: 18 DB          JR      $7A72           
7A97: C7             RST     0X00            
7A98: 9A             SBC     D               
7A99: 80             ADD     A,B             
7A9A: C5             PUSH    BC              
7A9B: 0E 80          LD      C,$80           
7A9D: C2 0D 20       JP      NZ,$200D        
7AA0: 0E 04          LD      C,$04           
7AA2: 0A             LD      A,(BC)          
7AA3: 46             LD      B,(HL)          
7AA4: 0A             LD      A,(BC)          
7AA5: 47             LD      B,A             
7AA6: 1F             RRA                     
7AA7: 18 91          JR      $7A3A           
7AA9: 1E 59          LD      E,$59           
7AAB: C2 46 7A       JP      NZ,$7A46        
7AAE: 9B             SBC     E               
7AAF: 15             DEC     D               
7AB0: 5B             LD      E,E             
7AB1: CA C7 DE       JP      Z,$DEC7         
7AB4: 83             ADD     A,E             
7AB5: AF             XOR     A               
7AB6: A9             XOR     C               
7AB7: 9A             SBC     D               
7AB8: 23             INC     HL              
7AB9: 62             LD      H,D             
7ABA: 83             ADD     A,E             
7ABB: 7A             LD      A,D             
7ABC: 8F             ADC     A,A             
7ABD: BE             CP      (HL)            
7ABE: DC 63 0D       CALL    C,$0D63         
7AC1: 13             INC     DE              
7AC2: 0A             LD      A,(BC)          
7AC3: 49             LD      C,C             
7AC4: 1F             RRA                     
7AC5: 0F             RRCA                    
7AC6: 5F             LD      E,A             
7AC7: BE             CP      (HL)            
7AC8: 49             LD      C,C             
7AC9: DB 67          IN      A,($67)         
7ACB: B1             OR      C               
7ACC: 07             RLCA                    
7ACD: BC             CP      H               
7ACE: DA 46 C6       JP      C,$C646         
7AD1: 16 F4          LD      D,$F4           
7AD3: 72             LD      (HL),D          
7AD4: 2E 0D          LD      L,$0D           
7AD6: 11 0A 4A       LD      DE,$4A0A        
7AD9: 1F             RRA                     
7ADA: 0D             DEC     C               
7ADB: FD                                  
7ADC: 1C             INC     E               
7ADD: 0E EE          LD      C,$EE           
7ADF: 86             ADD     A,(HL)          
7AE0: 5F             LD      E,A             
7AE1: 82             ADD     A,D             
7AE2: 17             RLA                     
7AE3: 59             LD      E,C             
7AE4: 5E             LD      E,(HL)          
7AE5: 5F             LD      E,A             
7AE6: 4A             LD      C,D             
7AE7: 22 0D 18       LD      ($180D),HL      
7AEA: 0A             LD      A,(BC)          
7AEB: 2F             CPL                     
7AEC: 1F             RRA                     
7AED: 14             INC     D               
7AEE: 91             SUB     C               
7AEF: 1E 59          LD      E,$59           
7AF1: C2 2E A1       JP      NZ,$A12E        
7AF4: 45             LD      B,L             
7AF5: 5B             LD      E,E             
7AF6: 0E BC          LD      C,$BC           
7AF8: 98             SBC     B               
7AF9: 5F             LD      E,A             
7AFA: 4F             LD      C,A             
7AFB: 5E             LD      E,(HL)          
7AFC: 4A             LD      C,D             
7AFD: 5E             LD      E,(HL)          
7AFE: 2F             CPL                     
7AFF: 62             LD      H,D             
7B00: E3             EX      (SP),HL         
7B01: 06 0D          LD      B,$0D           
7B03: 5C             LD      E,H             
7B04: 1F             RRA                     
7B05: 0F             RRCA                    
7B06: 5F             LD      E,A             
7B07: BE             CP      (HL)            
7B08: B4             OR      H               
7B09: 16 03          LD      D,$03           
7B0B: BA             CP      D               
7B0C: D6 97          SUB     $97             
7B0E: 54             LD      D,H             
7B0F: 5E             LD      E,(HL)          
7B10: E6 61          AND     $61             
7B12: 4B             LD      C,E             
7B13: DB 53          IN      A,($53)         
7B15: 0B             DEC     BC              
7B16: 49             LD      C,C             
7B17: 05             DEC     B               
7B18: 41             LD      B,C             
7B19: 14             INC     D               
7B1A: 1F             RRA                     
7B1B: 12             LD      (DE),A          
7B1C: D9             EXX                     
7B1D: 1C             INC     E               
7B1E: 0B             DEC     BC              
7B1F: EE DB          XOR     $DB             
7B21: 22 06 9A       LD      ($9A06),HL      
7B24: 51             LD      D,C             
7B25: 18 23          JR      $7B4A           
7B27: C6 B4          ADD     $B4             
7B29: B7             OR      A               
7B2A: D0             RET     NC              
7B2B: C9             RET                     
7B2C: AC             XOR     H               
7B2D: BB             CP      E               
7B2E: 82             ADD     A,D             
7B2F: 0E 1F          LD      C,$1F           
7B31: 0C             INC     C               
7B32: 49             LD      C,C             
7B33: 1B             DEC     DE              
7B34: D6 15          SUB     $15             
7B36: 51             LD      D,C             
7B37: 18 3D          JR      $7B76           
7B39: C6 40          ADD     $40             
7B3B: 61             LD      H,C             
7B3C: E3             EX      (SP),HL         
7B3D: 06 C3          LD      B,$C3           
7B3F: 10 1F          DJNZ    $7B60           
7B41: 0E 91          LD      C,$91           
7B43: 1E 4F          LD      E,$4F           
7B45: C2 66 C6       JP      NZ,$C666        
7B48: AF             XOR     A               
7B49: 14             INC     D               
7B4A: E4 14 83       CALL    PO,$8314        
7B4D: 4A             LD      C,D             
7B4E: E3             EX      (SP),HL         
7B4F: 06 FF          LD      B,$FF           
7B51: 0E 1F          LD      C,$1F           
7B53: 0C             INC     C               
7B54: FB             EI                      
7B55: 1B             DEC     DE              
7B56: 80             ADD     A,B             
7B57: 5B             LD      E,E             
7B58: F3             DI                      
7B59: 23             INC     HL              
7B5A: 10 D0          DJNZ    $7B2C           
7B5C: 16 BC          LD      D,$BC           
7B5E: 5C             LD      E,H             
7B5F: A2             AND     D               
7B60: 9C             SBC     H               
7B61: 34             INC     (HL)            
7B62: 0B             DEC     BC              
7B63: 32 05 E6       LD      ($E605),A       
7B66: 27             DAA                     
7B67: 0D             DEC     C               
7B68: 25             DEC     H               
7B69: 14             INC     D               
7B6A: 01 13 0E       LD      BC,$0E13        
7B6D: 05             DEC     B               
7B6E: 20 2C          JR      NZ,$7B9C        
7B70: 14             INC     D               
7B71: 01 2C 0B       LD      BC,$0B2C        
7B74: 19             ADD     HL,DE           
7B75: 0A             LD      A,(BC)          
7B76: 04             INC     B               
7B77: 04             INC     B               
7B78: 21 04 00       LD      HL,$0004        
7B7B: 00             NOP                     
7B7C: 03             INC     BC              
7B7D: 04             INC     B               
7B7E: 21 03 00       LD      HL,$0003        
7B81: 00             NOP                     
7B82: 01 04 21       LD      BC,$2104        
7B85: 01 00 00       LD      BC,$0000        
7B88: 02             LD      (BC),A          
7B89: 04             INC     B               
7B8A: 21 02 00       LD      HL,$0002        
7B8D: 00             NOP                     
7B8E: FF             RST     0X38            
7B8F: 06 0D          LD      B,$0D           
7B91: 04             INC     B               
7B92: 14             INC     D               
7B93: 01 13 9B       LD      BC,$9B13        
7B96: 9B             SBC     E               
7B97: 41             LD      B,C             
7B98: 0B             DEC     BC              
7B99: 3F             CCF                     
7B9A: 05             DEC     B               
7B9B: 3F             CCF                     
7B9C: 0D             DEC     C               
7B9D: 0D             DEC     C               
7B9E: 0B             DEC     BC              
7B9F: 25             DEC     H               
7BA0: 04             INC     B               
7BA1: 03             INC     BC              
7BA2: B5             OR      L               
7BA3: D0             RET     NC              
7BA4: 54             LD      D,H             
7BA5: 25             DEC     H               
7BA6: 21 04 00       LD      HL,$0004        
7BA9: 00             NOP                     
7BAA: 7F             LD      A,A             
7BAB: 0D             DEC     C               
7BAC: 0D             DEC     C               
7BAD: 0B             DEC     BC              
7BAE: 25             DEC     H               
7BAF: 04             INC     B               
7BB0: 03             INC     BC              
7BB1: 95             SUB     L               
7BB2: 5F             LD      E,A             
7BB3: 54             LD      D,H             
7BB4: 25             DEC     H               
7BB5: 21 03 00       LD      HL,$0003        
7BB8: 00             NOP                     
7BB9: BF             CP      A               
7BBA: 0E 0D          LD      C,$0D           
7BBC: 0C             INC     C               
7BBD: 25             DEC     H               
7BBE: 04             INC     B               
7BBF: 04             INC     B               
7BC0: 04             INC     B               
7BC1: 9A             SBC     D               
7BC2: 53             LD      D,E             
7BC3: BE             CP      (HL)            
7BC4: 25             DEC     H               
7BC5: 21 01 00       LD      HL,$0001        
7BC8: 00             NOP                     
7BC9: FF             RST     0X38            
7BCA: 0E 0D          LD      C,$0D           
7BCC: 0C             INC     C               
7BCD: 25             DEC     H               
7BCE: 04             INC     B               
7BCF: 04             INC     B               
7BD0: 47             LD      B,A             
7BD1: B9             CP      C               
7BD2: 53             LD      D,E             
7BD3: BE             CP      (HL)            
7BD4: 25             DEC     H               
7BD5: 21 02 00       LD      HL,$0002        
7BD8: 00             NOP                     
7BD9: 9E             SBC     (HL)            
7BDA: 14             INC     D               
7BDB: 0D             DEC     C               
7BDC: 12             LD      (DE),A          
7BDD: 01 13 2C       LD      BC,$2C13        
7BE0: 13             INC     DE              
7BE1: AA             XOR     D               
7BE2: 04             INC     B               
7BE3: 0B             DEC     BC              
7BE4: 9E             SBC     (HL)            
7BE5: 61             LD      H,C             
7BE6: 3D             DEC     A               
7BE7: 62             LD      H,D             
7BE8: 82             ADD     A,D             
7BE9: 17             RLA                     
7BEA: 54             LD      D,H             
7BEB: 5E             LD      E,(HL)          
7BEC: 3F             CCF                     
7BED: A0             AND     B               
7BEE: 2E A0          LD      L,$A0           
7BF0: 20 04          JR      NZ,$7BF6        
7BF2: 1E 5F          LD      E,$5F           
7BF4: BE             CP      (HL)            
7BF5: E3             EX      (SP),HL         
7BF6: 16 F3          LD      D,$F3           
7BF8: 8C             ADC     A,H             
7BF9: A7             AND     A               
7BFA: B7             OR      A               
7BFB: 4B             LD      C,E             
7BFC: 94             SUB     H               
7BFD: 6B             LD      L,E             
7BFE: BF             CP      A               
7BFF: 95             SUB     L               
7C00: 5A             LD      E,D             
7C01: 3E B9          LD      A,$B9           
7C03: 5B             LD      E,E             
7C04: CA 83 7A       JP      Z,$7A83         
7C07: 5F             LD      E,A             
7C08: BE             CP      (HL)            
7C09: 9B             SBC     E               
7C0A: 15             DEC     D               
7C0B: BF             CP      A               
7C0C: 91             SUB     C               
7C0D: B7             OR      A               
7C0E: B1             OR      C               
7C0F: 1B             DEC     DE              
7C10: B5             OR      L               
7C11: A1             AND     C               
7C12: 6F             LD      L,A             
7C13: 0D             DEC     C               
7C14: 6D             LD      L,L             
7C15: 0E 08          LD      C,$08           
7C17: 0A             LD      A,(BC)          
7C18: 28 0A          JR      Z,$7C24         
7C1A: 0E 0A          LD      C,$0A           
7C1C: 29             ADD     HL,HL           
7C1D: 0A             LD      A,(BC)          
7C1E: 0D             DEC     C               
7C1F: 0E 04          LD      C,$04           
7C21: 09             ADD     HL,BC           
7C22: 19             ADD     HL,DE           
7C23: 08             EX      AF,AF'          
7C24: 19             ADD     HL,DE           
7C25: 04             INC     B               
7C26: 28 5F          JR      Z,$7C87         
7C28: BE             CP      (HL)            
7C29: 09             ADD     HL,BC           
7C2A: 15             DEC     D               
7C2B: D9             EXX                     
7C2C: 6A             LD      L,D             
7C2D: C0             RET     NZ              
7C2E: 9F             SBC     A               
7C2F: C6 B5          ADD     $B5             
7C31: 80             ADD     A,B             
7C32: A1             AND     C               
7C33: 82             ADD     A,D             
7C34: 17             RLA                     
7C35: 4A             LD      C,D             
7C36: 5E             LD      E,(HL)          
7C37: 64             LD      H,H             
7C38: 48             LD      C,B             
7C39: 31 C6 47       LD      SP,$47C6        
7C3C: 62             LD      H,D             
7C3D: 9F             SBC     A               
7C3E: 15             DEC     D               
7C3F: 77             LD      (HL),A          
7C40: 16 F3          LD      D,$F3           
7C42: B9             CP      C               
7C43: 5B             LD      E,E             
7C44: 4D             LD      C,L             
7C45: EF             RST     0X28            
7C46: A6             AND     (HL)            
7C47: 53             LD      D,E             
7C48: C0             RET     NZ              
7C49: AF             XOR     A               
7C4A: 15             DEC     D               
7C4B: C4 98 EB       CALL    NZ,$EB98        
7C4E: DA 17 19       JP      C,$1917         
7C51: 00             NOP                     
7C52: 0E 2E          LD      C,$2E           
7C54: 0D             DEC     C               
7C55: 2A 03 19       LD      HL,($1903)      
7C58: 15             DEC     D               
7C59: 04             INC     B               
7C5A: 22 5F BE       LD      ($BE5F),HL      
7C5D: 09             ADD     HL,BC           
7C5E: 15             DEC     D               
7C5F: CE 6A          ADC     $6A             
7C61: 3D             DEC     A               
7C62: A0             AND     B               
7C63: D5             PUSH    DE              
7C64: B5             OR      L               
7C65: DD                                  
7C66: 78             LD      A,B             
7C67: 4A             LD      C,D             
7C68: F4 59 5E       CALL    P,$5E59         
7C6B: 98             SBC     B               
7C6C: 5F             LD      E,A             
7C6D: 4B             LD      C,E             
7C6E: 62             LD      H,D             
7C6F: 8E             ADC     A,(HL)          
7C70: 48             LD      C,B             
7C71: 4B             LD      C,E             
7C72: 15             DEC     D               
7C73: 0D             DEC     C               
7C74: 8D             ADC     A,L             
7C75: C8             RET     Z               
7C76: 16 23          LD      D,$23           
7C78: 62             LD      H,D             
7C79: E3             EX      (SP),HL         
7C7A: 59             LD      E,C             
7C7B: 9B             SBC     E               
7C7C: 5D             LD      E,L             
7C7D: 1E 1A          LD      E,$1A           
7C7F: 3C             INC     A               
7C80: 14             INC     D               
7C81: 0C             INC     C               
7C82: A4             AND     H               
7C83: 43             LD      B,E             
7C84: 0D             DEC     C               
7C85: 41             LD      B,C             
7C86: 0A             LD      A,(BC)          
7C87: 0B             DEC     BC              
7C88: 0E 3D          LD      C,$3D           
7C8A: 0D             DEC     C               
7C8B: 17             RLA                     
7C8C: 01 3D 1F       LD      BC,$1F3D        
7C8F: 13             INC     DE              
7C90: 5F             LD      E,A             
7C91: BE             CP      (HL)            
7C92: 5B             LD      E,E             
7C93: B1             OR      C               
7C94: 4B             LD      C,E             
7C95: 7B             LD      A,E             
7C96: 55             LD      D,L             
7C97: 45             LD      B,L             
7C98: E4 5F 73       CALL    PO,$735F        
7C9B: 62             LD      H,D             
7C9C: 81             ADD     A,C             
7C9D: 5B             LD      E,E             
7C9E: 8A             ADC     A,D             
7C9F: AF             XOR     A               
7CA0: 2F             CPL                     
7CA1: 62             LD      H,D             
7CA2: 2E 0D          LD      L,$0D           
7CA4: 22 0E 04       LD      ($040E),HL      
7CA7: 01 3E 01       LD      BC,$013E        
7CAA: 3F             CCF                     
7CAB: 1F             RRA                     
7CAC: 1A             LD      A,(DE)          
7CAD: 85             ADD     A,L             
7CAE: A5             AND     L               
7CAF: 65             LD      H,L             
7CB0: 49             LD      C,C             
7CB1: CA 9C 4B       JP      Z,$4B9C         
7CB4: 49             LD      C,C             
7CB5: 4B             LD      C,E             
7CB6: A4             AND     H               
7CB7: BF             CP      A               
7CB8: 9A             SBC     D               
7CB9: 03             INC     BC              
7CBA: 58             LD      E,B             
7CBB: 09             ADD     HL,BC           
7CBC: 15             DEC     D               
7CBD: A3             AND     E               
7CBE: A0             AND     B               
7CBF: 03             INC     BC              
7CC0: A0             AND     B               
7CC1: 0F             RRCA                    
7CC2: A0             AND     B               
7CC3: F3             DI                      
7CC4: 17             RLA                     
7CC5: 17             RLA                     
7CC6: 8D             ADC     A,L             
7CC7: A5             AND     L               
7CC8: 12             LD      (DE),A          
7CC9: 0D             DEC     C               
7CCA: 10 14          DJNZ    $7CE0           
7CCC: 15             DEC     D               
7CCD: 02             LD      (BC),A          
7CCE: A8             XOR     B               
7CCF: 04             INC     B               
7CD0: 0A             LD      A,(BC)          
7CD1: 4B             LD      C,E             
7CD2: 7B             LD      A,E             
7CD3: 06 9A          LD      B,$9A           
7CD5: DE 14          SBC     $14             
7CD7: D7             RST     0X10            
7CD8: A0             AND     B               
7CD9: 9B             SBC     E               
7CDA: 5D             LD      E,L             
7CDB: A6             AND     (HL)            
7CDC: 0E 0D          LD      C,$0D           
7CDE: 0C             INC     C               
7CDF: 29             ADD     HL,HL           
7CE0: A8             XOR     B               
7CE1: 04             INC     B               
7CE2: 08             EX      AF,AF'          
7CE3: 4B             LD      C,E             
7CE4: 7B             LD      A,E             
7CE5: 09             ADD     HL,BC           
7CE6: 9A             SBC     D               
7CE7: C2 16 A7       JP      NZ,$A716        
7CEA: 61             LD      H,C             
7CEB: A7             AND     A               
7CEC: 2A 0D 28       LD      HL,($280D)      
7CEF: 15             DEC     D               
7CF0: 01 0E 0F       LD      BC,$0F0E        
7CF3: 0D             DEC     C               
7CF4: 05             DEC     B               
7CF5: 08             EX      AF,AF'          
7CF6: 40             LD      B,B             
7CF7: 14             INC     D               
7CF8: 09             ADD     HL,BC           
7CF9: 1B             DEC     DE              
7CFA: 0D             DEC     C               
7CFB: 06 14          LD      B,$14           
7CFD: 08             EX      AF,AF'          
7CFE: 40             LD      B,B             
7CFF: 14             INC     D               
7D00: 09             ADD     HL,BC           
7D01: 14             INC     D               
7D02: 04             INC     B               
7D03: 0B             DEC     BC              
7D04: C7             RST     0X00            
7D05: DE D3          SBC     $D3             
7D07: 14             INC     D               
7D08: E6 96          AND     $96             
7D0A: B0             OR      B               
7D0B: 17             RLA                     
7D0C: 75             LD      (HL),L          
7D0D: 8D             ADC     A,L             
7D0E: 4B             LD      C,E             
7D0F: A8             XOR     B               
7D10: 04             INC     B               
7D11: 03             INC     BC              
7D12: 56             LD      D,(HL)          
7D13: D1             POP     DE              
7D14: 48             LD      C,B             
7D15: A9             XOR     C               
7D16: 8B             ADC     A,E             
7D17: A8             XOR     B               
7D18: 0C             INC     C               
7D19: 0D             DEC     C               
7D1A: 0A             LD      A,(BC)          
7D1B: 1A             LD      A,(DE)          
7D1C: 0E 06          LD      C,$06           
7D1E: 15             DEC     D               
7D1F: 10 1F          DJNZ    $7D40           
7D21: 02             LD      (BC),A          
7D22: 5F             LD      E,A             
7D23: BE             CP      (HL)            
7D24: 11 A9 0C       LD      DE,$0CA9        
7D27: 0D             DEC     C               
7D28: 0A             LD      A,(BC)          
7D29: 1B             DEC     DE              
7D2A: 0E 06          LD      C,$06           
7D2C: 15             DEC     D               
7D2D: 10 1F          DJNZ    $7D4E           
7D2F: 02             LD      (BC),A          
7D30: 5F             LD      E,A             
7D31: BE             CP      (HL)            
7D32: 12             LD      (DE),A          
7D33: AA             XOR     D               
7D34: 0B             DEC     BC              
7D35: 0D             DEC     C               
7D36: 09             ADD     HL,BC           
7D37: 0E 06          LD      C,$06           
7D39: 15             DEC     D               
7D3A: 10 1F          DJNZ    $7D5B           
7D3C: 02             LD      (BC),A          
7D3D: 5F             LD      E,A             
7D3E: BE             CP      (HL)            
7D3F: 16 AB          LD      D,$AB           
7D41: 35             DEC     (HL)            
7D42: 0D             DEC     C               
7D43: 33             INC     SP              
7D44: 0A             LD      A,(BC)          
7D45: 09             ADD     HL,BC           
7D46: A8             XOR     B               
7D47: 1F             RRA                     
7D48: 2E C5          LD      L,$C5           
7D4A: 4C             LD      C,H             
7D4B: CB 87          RES     0,A             
7D4D: F3             DI                      
7D4E: 49             LD      C,C             
7D4F: 48             LD      C,B             
7D50: DB FF          IN      A,($FF)         
7D52: B2             OR      D               
7D53: 51             LD      D,C             
7D54: 18 23          JR      $7D79           
7D56: C6 8E          ADD     $8E             
7D58: 49             LD      C,C             
7D59: DD 46 03       LD      B,(IX+$03)      
7D5C: EE 33          XOR     $33             
7D5E: 98             SBC     B               
7D5F: 1B             DEC     DE              
7D60: B7             OR      A               
7D61: 33             INC     SP              
7D62: BB             CP      E               
7D63: 91             SUB     C               
7D64: 1E 4F          LD      E,$4F           
7D66: C2 66 C6       JP      NZ,$C666        
7D69: AF             XOR     A               
7D6A: 14             INC     D               
7D6B: 7B             LD      A,E             
7D6C: 14             INC     D               
7D6D: AB             XOR     E               
7D6E: 55             LD      D,L             
7D6F: 7B             LD      A,E             
7D70: E6 F4          AND     $F4             
7D72: A4             AND     H               
7D73: 40             LD      B,B             
7D74: B9             CP      C               
7D75: E3             EX      (SP),HL         
7D76: 06 AC          LD      B,$AC           
7D78: 1D             DEC     E               
7D79: 0D             DEC     C               
7D7A: 1B             DEC     DE              
7D7B: AA             XOR     D               
7D7C: 1F             RRA                     
7D7D: 18 A7          JR      $7D26           
7D7F: B7             OR      A               
7D80: 4B             LD      C,E             
7D81: 94             SUB     H               
7D82: 6B             LD      L,E             
7D83: BF             CP      A               
7D84: 5B             LD      E,E             
7D85: 4D             LD      C,L             
7D86: 80             ADD     A,B             
7D87: 79             LD      A,C             
7D88: B3             OR      E               
7D89: A0             AND     B               
7D8A: AB             XOR     E               
7D8B: 98             SBC     B               
7D8C: C7             RST     0X00            
7D8D: DE 85          SBC     $85             
7D8F: AF             XOR     A               
7D90: EF             RST     0X28            
7D91: 9F             SBC     A               
7D92: 8E             ADC     A,(HL)          
7D93: 48             LD      C,B             
7D94: 5B             LD      E,E             
7D95: BB             CP      E               
7D96: FF             RST     0X38            
7D97: 00             NOP                     
7D98: FF             RST     0X38            
7D99: 00             NOP                     
7D9A: FF             RST     0X38            
7D9B: 00             NOP                     
7D9C: FF             RST     0X38            
7D9D: 00             NOP                     
7D9E: FF             RST     0X38            
7D9F: 00             NOP                     
7DA0: FF             RST     0X38            
7DA1: 00             NOP                     
7DA2: FF             RST     0X38            
7DA3: 00             NOP                     
7DA4: FF             RST     0X38            
7DA5: 00             NOP                     
7DA6: FF             RST     0X38            
7DA7: 00             NOP                     
7DA8: FC 45 56       CALL    M,$5645         
7DAB: 4C             LD      C,H             
7DAC: 24             INC     H               
7DAD: 49             LD      C,C             
7DAE: 61             LD      H,C             
7DAF: 6E             LD      L,(HL)          
7DB0: 3A 49 33       LD      A,($3349)       
7DB3: 49             LD      C,C             
7DB4: 24             INC     H               
7DB5: 49             LD      C,C             
7DB6: 61             LD      H,C             
7DB7: 6E             LD      L,(HL)          
7DB8: 3A 49 33       LD      A,($3349)       
7DBB: 49             LD      C,C             
7DBC: 67             LD      H,A             
7DBD: 49             LD      C,C             
7DBE: 65             LD      H,L             
7DBF: 6E             LD      L,(HL)          
7DC0: 4E             LD      C,(HL)          
7DC1: 47             LD      B,A             
7DC2: 44             LD      B,H             
7DC3: 47             LD      B,A             
7DC4: 89             ADC     A,C             
7DC5: 49             LD      C,C             
7DC6: 70             LD      (HL),B          
7DC7: 49             LD      C,C             
7DC8: 5A             LD      E,D             
7DC9: 6F             LD      L,A             
7DCA: 67             LD      H,A             
7DCB: 49             LD      C,C             
7DCC: 5A             LD      E,D             
7DCD: 6F             LD      L,A             
7DCE: BF             CP      A               
7DCF: 4B             LD      C,E             
7DD0: AF             XOR     A               
7DD1: 6F             LD      L,A             
7DD2: 80             ADD     A,B             
7DD3: 04             INC     B               
7DD4: DD                                  
7DD5: 03             INC     BC              
7DD6: 1D             DEC     E               
7DD7: 40             LD      B,B             
7DD8: 80             ADD     A,B             
7DD9: 04             INC     B               
7DDA: DD                                  
7DDB: 03             INC     BC              
7DDC: 1D             DEC     E               
7DDD: 40             LD      B,B             
7DDE: 15             DEC     D               
7DDF: 40             LD      B,B             
7DE0: 99             SBC     C               
7DE1: 6F             LD      L,A             
7DE2: 00             NOP                     
7DE3: 00             NOP                     
7DE4: 9A             SBC     D               
7DE5: 4E             LD      C,(HL)          
7DE6: 6A             LD      L,D             
7DE7: 4E             LD      C,(HL)          
7DE8: D2 4D 24       JP      NC,$244D        
7DEB: 49             LD      C,C             
7DEC: 9A             SBC     D               
7DED: 6F             LD      L,A             
7DEE: 3A 49 9A       LD      A,($9A49)       
7DF1: 6F             LD      L,A             
7DF2: 67             LD      H,A             
7DF3: 49             LD      C,C             
7DF4: 9A             SBC     D               
7DF5: 6F             LD      L,A             
7DF6: BF             CP      A               
7DF7: 4B             LD      C,E             
7DF8: AF             XOR     A               
7DF9: 6F             LD      L,A             
7DFA: 3A 49 CA       LD      A,($CA49)       
7DFD: 6F             LD      L,A             
7DFE: 24             INC     H               
7DFF: 49             LD      C,C             
7E00: CA 6F 3A       JP      Z,$3A6F         
7E03: 49             LD      C,C             
7E04: DD 75 6F       LD      (IX+$6F),L      
7E07: 45             LD      B,L             
7E08: 00             NOP                     
7E09: 00             NOP                     
7E0A: FF             RST     0X38            
7E0B: 00             NOP                     
7E0C: FF             RST     0X38            
7E0D: 00             NOP                     
7E0E: FF             RST     0X38            
7E0F: 00             NOP                     
7E10: 00             NOP                     
7E11: 00             NOP                     
7E12: FF             RST     0X38            
7E13: 00             NOP                     
7E14: FF             RST     0X38            
7E15: 00             NOP                     
7E16: FF             RST     0X38            
7E17: 00             NOP                     
7E18: FF             RST     0X38            
7E19: 00             NOP                     
7E1A: FF             RST     0X38            
7E1B: 00             NOP                     
7E1C: FF             RST     0X38            
7E1D: 00             NOP                     
7E1E: FF             RST     0X38            
7E1F: 00             NOP                     
7E20: FF             RST     0X38            
7E21: 00             NOP                     
7E22: FF             RST     0X38            
7E23: 00             NOP                     
7E24: FF             RST     0X38            
7E25: 00             NOP                     
7E26: FF             RST     0X38            
7E27: 00             NOP                     
7E28: FF             RST     0X38            
7E29: 00             NOP                     
7E2A: FF             RST     0X38            
7E2B: 00             NOP                     
7E2C: FF             RST     0X38            
7E2D: 00             NOP                     
7E2E: FF             RST     0X38            
7E2F: 00             NOP                     
7E30: FF             RST     0X38            
7E31: 00             NOP                     
7E32: FF             RST     0X38            
7E33: 00             NOP                     
7E34: FF             RST     0X38            
7E35: 00             NOP                     
7E36: FF             RST     0X38            
7E37: 00             NOP                     
7E38: FF             RST     0X38            
7E39: 00             NOP                     
7E3A: FF             RST     0X38            
7E3B: 00             NOP                     
7E3C: FF             RST     0X38            
7E3D: 00             NOP                     
7E3E: FF             RST     0X38            
7E3F: 00             NOP                     
7E40: FF             RST     0X38            
7E41: 00             NOP                     
7E42: FF             RST     0X38            
7E43: 00             NOP                     
7E44: FF             RST     0X38            
7E45: 00             NOP                     
7E46: FF             RST     0X38            
7E47: 00             NOP                     
7E48: FF             RST     0X38            
7E49: 00             NOP                     
7E4A: FF             RST     0X38            
7E4B: 00             NOP                     
7E4C: FF             RST     0X38            
7E4D: 00             NOP                     
7E4E: FF             RST     0X38            
7E4F: 00             NOP                     
7E50: FF             RST     0X38            
7E51: 00             NOP                     
7E52: FF             RST     0X38            
7E53: 00             NOP                     
7E54: FF             RST     0X38            
7E55: 00             NOP                     
7E56: FF             RST     0X38            
7E57: 00             NOP                     
7E58: FF             RST     0X38            
7E59: 00             NOP                     
7E5A: FF             RST     0X38            
7E5B: 00             NOP                     
7E5C: FF             RST     0X38            
7E5D: 00             NOP                     
7E5E: FF             RST     0X38            
7E5F: 00             NOP                     
7E60: FF             RST     0X38            
7E61: 00             NOP                     
7E62: FF             RST     0X38            
7E63: 00             NOP                     
7E64: FF             RST     0X38            
7E65: 00             NOP                     
7E66: FF             RST     0X38            
7E67: 00             NOP                     
7E68: FF             RST     0X38            
7E69: 00             NOP                     
7E6A: FF             RST     0X38            
7E6B: 00             NOP                     
7E6C: FF             RST     0X38            
7E6D: 00             NOP                     
7E6E: FF             RST     0X38            
7E6F: 00             NOP                     
7E70: FF             RST     0X38            
7E71: 00             NOP                     
7E72: FF             RST     0X38            
7E73: 00             NOP                     
7E74: FF             RST     0X38            
7E75: 00             NOP                     
7E76: FF             RST     0X38            
7E77: 00             NOP                     
7E78: FF             RST     0X38            
7E79: 00             NOP                     
7E7A: FF             RST     0X38            
7E7B: 00             NOP                     
7E7C: FF             RST     0X38            
7E7D: 00             NOP                     
7E7E: FF             RST     0X38            
7E7F: 00             NOP                     
7E80: FF             RST     0X38            
7E81: 00             NOP                     
7E82: FF             RST     0X38            
7E83: 00             NOP                     
7E84: FF             RST     0X38            
7E85: 00             NOP                     
7E86: FF             RST     0X38            
7E87: 00             NOP                     
7E88: FF             RST     0X38            
7E89: 00             NOP                     
7E8A: FF             RST     0X38            
7E8B: 00             NOP                     
7E8C: FF             RST     0X38            
7E8D: 00             NOP                     
7E8E: FF             RST     0X38            
7E8F: 00             NOP                     
7E90: FF             RST     0X38            
7E91: 00             NOP                     
7E92: FF             RST     0X38            
7E93: 00             NOP                     
7E94: FF             RST     0X38            
7E95: 00             NOP                     
7E96: FF             RST     0X38            
7E97: 00             NOP                     
7E98: FF             RST     0X38            
7E99: 00             NOP                     
7E9A: FF             RST     0X38            
7E9B: 00             NOP                     
7E9C: FF             RST     0X38            
7E9D: 00             NOP                     
7E9E: FF             RST     0X38            
7E9F: 00             NOP                     
7EA0: FF             RST     0X38            
7EA1: 00             NOP                     
7EA2: FF             RST     0X38            
7EA3: 00             NOP                     
7EA4: FF             RST     0X38            
7EA5: 00             NOP                     
7EA6: FF             RST     0X38            
7EA7: 00             NOP                     
7EA8: FF             RST     0X38            
7EA9: 00             NOP                     
7EAA: FF             RST     0X38            
7EAB: 00             NOP                     
7EAC: FF             RST     0X38            
7EAD: 00             NOP                     
7EAE: FF             RST     0X38            
7EAF: 00             NOP                     
7EB0: FF             RST     0X38            
7EB1: 00             NOP                     
7EB2: FF             RST     0X38            
7EB3: 00             NOP                     
7EB4: FF             RST     0X38            
7EB5: 00             NOP                     
7EB6: FF             RST     0X38            
7EB7: 00             NOP                     
7EB8: FF             RST     0X38            
7EB9: 00             NOP                     
7EBA: FF             RST     0X38            
7EBB: 00             NOP                     
7EBC: FF             RST     0X38            
7EBD: 00             NOP                     
7EBE: FF             RST     0X38            
7EBF: 00             NOP                     
7EC0: FF             RST     0X38            
7EC1: 00             NOP                     
7EC2: FF             RST     0X38            
7EC3: 00             NOP                     
7EC4: FF             RST     0X38            
7EC5: 00             NOP                     
7EC6: FF             RST     0X38            
7EC7: 00             NOP                     
7EC8: FF             RST     0X38            
7EC9: 00             NOP                     
7ECA: FF             RST     0X38            
7ECB: 00             NOP                     
7ECC: FF             RST     0X38            
7ECD: 00             NOP                     
7ECE: FF             RST     0X38            
7ECF: 00             NOP                     
7ED0: FF             RST     0X38            
7ED1: 00             NOP                     
7ED2: FF             RST     0X38            
7ED3: 00             NOP                     
7ED4: FF             RST     0X38            
7ED5: 00             NOP                     
7ED6: FF             RST     0X38            
7ED7: 00             NOP                     
7ED8: FF             RST     0X38            
7ED9: 00             NOP                     
7EDA: FF             RST     0X38            
7EDB: 00             NOP                     
7EDC: FF             RST     0X38            
7EDD: 00             NOP                     
7EDE: FF             RST     0X38            
7EDF: 00             NOP                     
7EE0: FF             RST     0X38            
7EE1: 00             NOP                     
7EE2: FF             RST     0X38            
7EE3: 00             NOP                     
7EE4: FF             RST     0X38            
7EE5: 00             NOP                     
7EE6: FF             RST     0X38            
7EE7: 00             NOP                     
7EE8: FF             RST     0X38            
7EE9: 00             NOP                     
7EEA: FF             RST     0X38            
7EEB: 00             NOP                     
7EEC: FF             RST     0X38            
7EED: 00             NOP                     
7EEE: FF             RST     0X38            
7EEF: 00             NOP                     
7EF0: FF             RST     0X38            
7EF1: 00             NOP                     
7EF2: FF             RST     0X38            
7EF3: 00             NOP                     
7EF4: FF             RST     0X38            
7EF5: 00             NOP                     
7EF6: FF             RST     0X38            
7EF7: 00             NOP                     
7EF8: FF             RST     0X38            
7EF9: 00             NOP                     
7EFA: FF             RST     0X38            
7EFB: 00             NOP                     
7EFC: FF             RST     0X38            
7EFD: 00             NOP                     
7EFE: FF             RST     0X38            
7EFF: 00             NOP                     
7F00: FF             RST     0X38            
7F01: 00             NOP                     
7F02: FF             RST     0X38            
7F03: 00             NOP                     
7F04: FF             RST     0X38            
7F05: 00             NOP                     
7F06: FF             RST     0X38            
7F07: 00             NOP                     
7F08: FF             RST     0X38            
7F09: 00             NOP                     
7F0A: FF             RST     0X38            
7F0B: 00             NOP                     
7F0C: FF             RST     0X38            
7F0D: 00             NOP                     
7F0E: FF             RST     0X38            
7F0F: 00             NOP                     
7F10: FF             RST     0X38            
7F11: 00             NOP                     
7F12: FF             RST     0X38            
7F13: 00             NOP                     
7F14: FF             RST     0X38            
7F15: 00             NOP                     
7F16: FF             RST     0X38            
7F17: 00             NOP                     
7F18: FF             RST     0X38            
7F19: 00             NOP                     
7F1A: FF             RST     0X38            
7F1B: 00             NOP                     
7F1C: FF             RST     0X38            
7F1D: 00             NOP                     
7F1E: FF             RST     0X38            
7F1F: 00             NOP                     
7F20: FF             RST     0X38            
7F21: 00             NOP                     
7F22: FF             RST     0X38            
7F23: 00             NOP                     
7F24: FF             RST     0X38            
7F25: 00             NOP                     
7F26: FF             RST     0X38            
7F27: 00             NOP                     
7F28: FF             RST     0X38            
7F29: 00             NOP                     
7F2A: FF             RST     0X38            
7F2B: 00             NOP                     
7F2C: FF             RST     0X38            
7F2D: 00             NOP                     
7F2E: FF             RST     0X38            
7F2F: 00             NOP                     
7F30: FF             RST     0X38            
7F31: 00             NOP                     
7F32: FF             RST     0X38            
7F33: 00             NOP                     
7F34: FF             RST     0X38            
7F35: 00             NOP                     
7F36: FF             RST     0X38            
7F37: 00             NOP                     
7F38: FF             RST     0X38            
7F39: 00             NOP                     
7F3A: FF             RST     0X38            
7F3B: 00             NOP                     
7F3C: FF             RST     0X38            
7F3D: 00             NOP                     
7F3E: FF             RST     0X38            
7F3F: 00             NOP                     
7F40: FF             RST     0X38            
7F41: 00             NOP                     
7F42: FF             RST     0X38            
7F43: 00             NOP                     
7F44: FF             RST     0X38            
7F45: 00             NOP                     
7F46: FF             RST     0X38            
7F47: 00             NOP                     
7F48: FF             RST     0X38            
7F49: 00             NOP                     
7F4A: FF             RST     0X38            
7F4B: 00             NOP                     
7F4C: FF             RST     0X38            
7F4D: 00             NOP                     
7F4E: FF             RST     0X38            
7F4F: 00             NOP                     
7F50: FF             RST     0X38            
7F51: 00             NOP                     
7F52: FF             RST     0X38            
7F53: 00             NOP                     
7F54: FF             RST     0X38            
7F55: 00             NOP                     
7F56: FF             RST     0X38            
7F57: 00             NOP                     
7F58: FF             RST     0X38            
7F59: 00             NOP                     
7F5A: FF             RST     0X38            
7F5B: 00             NOP                     
7F5C: FF             RST     0X38            
7F5D: 00             NOP                     
7F5E: FF             RST     0X38            
7F5F: 00             NOP                     
7F60: FF             RST     0X38            
7F61: 00             NOP                     
7F62: FF             RST     0X38            
7F63: 00             NOP                     
7F64: FF             RST     0X38            
7F65: 00             NOP                     
7F66: FF             RST     0X38            
7F67: 00             NOP                     
7F68: FF             RST     0X38            
7F69: 00             NOP                     
7F6A: FF             RST     0X38            
7F6B: 00             NOP                     
7F6C: FF             RST     0X38            
7F6D: 00             NOP                     
7F6E: FF             RST     0X38            
7F6F: 00             NOP                     
7F70: FF             RST     0X38            
7F71: 00             NOP                     
7F72: FF             RST     0X38            
7F73: 00             NOP                     
7F74: FF             RST     0X38            
7F75: 00             NOP                     
7F76: FF             RST     0X38            
7F77: 00             NOP                     
7F78: FF             RST     0X38            
7F79: 00             NOP                     
7F7A: FF             RST     0X38            
7F7B: 00             NOP                     
7F7C: FF             RST     0X38            
7F7D: 00             NOP                     
7F7E: FF             RST     0X38            
7F7F: 00             NOP                     
7F80: FB             EI                      
7F81: 00             NOP                     
7F82: FF             RST     0X38            
7F83: 00             NOP                     
7F84: FF             RST     0X38            
7F85: 00             NOP                     
7F86: FF             RST     0X38            
7F87: 00             NOP                     
7F88: FF             RST     0X38            
7F89: 00             NOP                     
7F8A: FF             RST     0X38            
7F8B: 00             NOP                     
7F8C: FF             RST     0X38            
7F8D: 00             NOP                     
7F8E: FF             RST     0X38            
7F8F: 00             NOP                     
7F90: FF             RST     0X38            
7F91: 00             NOP                     
7F92: FF             RST     0X38            
7F93: 00             NOP                     
7F94: FF             RST     0X38            
7F95: 00             NOP                     
7F96: FF             RST     0X38            
7F97: 00             NOP                     
7F98: FF             RST     0X38            
7F99: 00             NOP                     
7F9A: FF             RST     0X38            
7F9B: 00             NOP                     
7F9C: FF             RST     0X38            
7F9D: 00             NOP                     
7F9E: FF             RST     0X38            
7F9F: 00             NOP                     
7FA0: FF             RST     0X38            
7FA1: 00             NOP                     
7FA2: FF             RST     0X38            
7FA3: 00             NOP                     
7FA4: FF             RST     0X38            
7FA5: 00             NOP                     
7FA6: FF             RST     0X38            
7FA7: 00             NOP                     
7FA8: FF             RST     0X38            
7FA9: 00             NOP                     
7FAA: FF             RST     0X38            
7FAB: 00             NOP                     
7FAC: FF             RST     0X38            
7FAD: 00             NOP                     
7FAE: FF             RST     0X38            
7FAF: 00             NOP                     
7FB0: FF             RST     0X38            
7FB1: 00             NOP                     
7FB2: FF             RST     0X38            
7FB3: 00             NOP                     
7FB4: FF             RST     0X38            
7FB5: 00             NOP                     
7FB6: FF             RST     0X38            
7FB7: 00             NOP                     
7FB8: FF             RST     0X38            
7FB9: 00             NOP                     
7FBA: FF             RST     0X38            
7FBB: 00             NOP                     
7FBC: FF             RST     0X38            
7FBD: 00             NOP                     
7FBE: FF             RST     0X38            
7FBF: 00             NOP                     
7FC0: FF             RST     0X38            
7FC1: 00             NOP                     
7FC2: FF             RST     0X38            
7FC3: 00             NOP                     
7FC4: FF             RST     0X38            
7FC5: 00             NOP                     
7FC6: FF             RST     0X38            
7FC7: 00             NOP                     
7FC8: FF             RST     0X38            
7FC9: 00             NOP                     
7FCA: FF             RST     0X38            
7FCB: 00             NOP                     
7FCC: FF             RST     0X38            
7FCD: 00             NOP                     
7FCE: FF             RST     0X38            
7FCF: 00             NOP                     
7FD0: FF             RST     0X38            
7FD1: 00             NOP                     
7FD2: FF             RST     0X38            
7FD3: 00             NOP                     
7FD4: FF             RST     0X38            
7FD5: 00             NOP                     
7FD6: FF             RST     0X38            
7FD7: 00             NOP                     
7FD8: FF             RST     0X38            
7FD9: 00             NOP                     
7FDA: FF             RST     0X38            
7FDB: 00             NOP                     
7FDC: FF             RST     0X38            
7FDD: 00             NOP                     
7FDE: FF             RST     0X38            
7FDF: 00             NOP                     
7FE0: FF             RST     0X38            
7FE1: 00             NOP                     
7FE2: FF             RST     0X38            
7FE3: 00             NOP                     
7FE4: FF             RST     0X38            
7FE5: 00             NOP                     
7FE6: FF             RST     0X38            
7FE7: 00             NOP                     
7FE8: FF             RST     0X38            
7FE9: 00             NOP                     
7FEA: FF             RST     0X38            
7FEB: 00             NOP                     
7FEC: FF             RST     0X38            
7FED: 00             NOP                     
7FEE: FF             RST     0X38            
7FEF: 00             NOP                     
7FF0: FF             RST     0X38            
7FF1: 00             NOP                     
7FF2: FF             RST     0X38            
7FF3: 00             NOP                     
7FF4: FF             RST     0X38            
7FF5: 00             NOP                     
7FF6: FF             RST     0X38            
7FF7: 00             NOP                     
7FF8: FF             RST     0X38            
7FF9: 00             NOP                     
7FFA: FF             RST     0X38            
7FFB: 00             NOP                     
7FFC: FF             RST     0X38            
7FFD: 00             NOP                     
7FFE: FF             RST     0X38            
7FFF: 00             NOP                     
```