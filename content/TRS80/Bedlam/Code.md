![TRS-80 RaakaTu](trs80bedlam.jpg)

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
4AE4: F6 01          OR      $01             
4AE6: C9             RET                     
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
4FC6: 94             SUB     H               
4FC7: A3             AND     E               
4FC8: 69             LD      L,C             
4FC9: 49             LD      C,C             
4FCA: AC             XOR     H               
4FCB: 4A             LD      C,D             
4FCC: CD 4A D2       CALL    $D24A           
4FCF: 4A             LD      C,D             
4FD0: E7             RST     0X20            
4FD1: 4A             LD      C,D             
4FD2: 2F             CPL                     
4FD3: 4D             LD      C,L             
4FD4: 12             LD      (DE),A          
4FD5: 4B             LD      C,E             
4FD6: 0D             DEC     C               
4FD7: 4B             LD      C,E             
4FD8: 4F             LD      C,A             
4FD9: 4B             LD      C,E             
4FDA: 72             LD      (HL),D          
4FDB: 4B             LD      C,E             
4FDC: 86             ADD     A,(HL)          
4FDD: 4B             LD      C,E             
4FDE: 44             LD      B,H             
4FDF: 49             LD      C,C             
4FE0: E4 4A 17       CALL    PO,$174A        
4FE3: 49             LD      C,C             
4FE4: 2D             DEC     L               
4FE5: 49             LD      C,C             
4FE6: 8D             ADC     A,L             
4FE7: 4B             LD      C,E             
4FE8: 9B             SBC     E               
4FE9: 4B             LD      C,E             
4FEA: 11 4C 3E       LD      DE,$3E4C        
4FED: 4C             LD      C,H             
4FEE: A9             XOR     C               
4FEF: 4B             LD      C,E             
4FF0: 8C             ADC     A,H             
4FF1: 4C             LD      C,H             
4FF2: 48             LD      C,B             
4FF3: 4C             LD      C,H             
4FF4: 07             RLCA                    
4FF5: 4C             LD      C,H             
4FF6: 97             SUB     A               
4FF7: 4C             LD      C,H             
4FF8: A7             AND     A               
4FF9: 4C             LD      C,H             
4FFA: 73             LD      (HL),E          
4FFB: 49             LD      C,C             
4FFC: 90             SUB     B               
4FFD: 49             LD      C,C             
4FFE: A0             AND     B               
4FFF: 49             LD      C,C             
5000: B0             OR      B               
5001: 49             LD      C,C             
5002: 3F             CCF                     
5003: 4D             LD      C,L             
5004: 7F             LD      A,A             
5005: 4D             LD      C,L             
5006: F4 4A B7       CALL    P,$B74A         
5009: 4A             LD      C,D             
500A: C0             RET     NZ              
500B: 49             LD      C,C             
500C: 00             NOP                     
500D: 00             NOP                     
500E: 9F             SBC     A               
500F: 4D             LD      C,L             
5010: D2 4D C3       JP      NC,$C34D        
5013: 4D             LD      C,L             
5014: E1             POP     HL              
5015: 4D             LD      C,L             
5016: 00             NOP                     
5017: 00             NOP                     
5018: 00             NOP                     
5019: 00             NOP                     
501A: 5E             LD      E,(HL)          
501B: 4C             LD      C,H             
501C: 75             LD      (HL),L          
501D: 4C             LD      C,H             
501E: 31 4F BD       LD      SP,$BD4F        
5021: 4A             LD      C,D             
5022: 7C             LD      A,H             
5023: 4B             LD      C,E             
5024: 00             NOP                     
5025: 05             DEC     B               
5026: 00             NOP                     
5027: 00             NOP                     
5028: 00             NOP                     
5029: 01 06 00       LD      BC,$0006        
502C: 00             NOP                     
502D: 00             NOP                     
502E: 02             LD      (BC),A          
502F: 07             RLCA                    
5030: 00             NOP                     
5031: 00             NOP                     
5032: 00             NOP                     
5033: 03             INC     BC              
5034: 08             EX      AF,AF'          
5035: 00             NOP                     
5036: 00             NOP                     
5037: 00             NOP                     
5038: 04             INC     B               
5039: 09             ADD     HL,BC           
503A: 00             NOP                     
503B: 20 00          JR      NZ,$503D        
503D: 05             DEC     B               
503E: 09             ADD     HL,BC           
503F: 02             LD      (BC),A          
5040: 20 20          JR      NZ,$5062        
5042: 43             LD      B,E             
5043: 34             INC     (HL)            
5044: 07             RLCA                    
5045: 00             NOP                     
5046: 80             ADD     A,B             
5047: 05             DEC     B               
5048: 34             INC     (HL)            
5049: 07             RLCA                    
504A: 80             ADD     A,B             
504B: 00             NOP                     
504C: 05             DEC     B               
504D: 0A             LD      A,(BC)          
504E: 00             NOP                     
504F: 20 00          JR      NZ,$5051        
5051: 06 0A          LD      B,$0A           
5053: 05             DEC     B               
5054: 80             ADD     A,B             
5055: 80             ADD     A,B             
5056: 0F             RRCA                    
5057: 0B             DEC     BC              
5058: 00             NOP                     
5059: 00             NOP                     
505A: 00             NOP                     
505B: 07             RLCA                    
505C: 04             INC     B               
505D: 02             LD      (BC),A          
505E: 10 40          DJNZ    $50A0           
5060: 09             ADD     HL,BC           
5061: 04             INC     B               
5062: 00             NOP                     
5063: 10 00          DJNZ    $5065           
5065: 09             ADD     HL,BC           
5066: 0C             INC     C               
5067: 00             NOP                     
5068: 00             NOP                     
5069: 00             NOP                     
506A: 0A             LD      A,(BC)          
506B: 0C             INC     C               
506C: 03             INC     BC              
506D: 00             NOP                     
506E: 80             ADD     A,B             
506F: 0B             DEC     BC              
5070: 0C             INC     C               
5071: 04             INC     B               
5072: 00             NOP                     
5073: 80             ADD     A,B             
5074: 0C             INC     C               
5075: 0C             INC     C               
5076: 05             DEC     B               
5077: 00             NOP                     
5078: 80             ADD     A,B             
5079: 10 03          DJNZ    $507E           
507B: 03             INC     BC              
507C: 40             LD      B,B             
507D: 10 0D          DJNZ    $508C           
507F: 03             INC     BC              
5080: 05             DEC     B               
5081: 80             ADD     A,B             
5082: 80             ADD     A,B             
5083: 39             ADD     HL,SP           
5084: 03             INC     BC              
5085: 08             EX      AF,AF'          
5086: 00             NOP                     
5087: 20 06          JR      NZ,$508F        
5089: 03             INC     BC              
508A: 01 80 10       LD      BC,$1080        
508D: 0E 0D          LD      C,$0D           
508F: 01 80 10       LD      BC,$1080        
5092: 0E 0E          LD      C,$0E           
5094: 00             NOP                     
5095: 80             ADD     A,B             
5096: 00             NOP                     
5097: 0B             DEC     BC              
5098: 0E 05          LD      C,$05           
509A: 00             NOP                     
509B: 80             ADD     A,B             
509C: 0B             DEC     BC              
509D: 0F             RRCA                    
509E: 00             NOP                     
509F: 02             LD      (BC),A          
50A0: 00             NOP                     
50A1: 11 0F 02       LD      DE,$020F        
50A4: 02             LD      (BC),A          
50A5: 80             ADD     A,B             
50A6: 3A 38 00       LD      A,($0038)       
50A9: 08             EX      AF,AF'          
50AA: 00             NOP                     
50AB: 40             LD      B,B             
50AC: 39             ADD     HL,SP           
50AD: 02             LD      (BC),A          
50AE: 08             EX      AF,AF'          
50AF: 80             ADD     A,B             
50B0: 41             LD      B,C             
50B1: 3A 02 01       LD      A,($0102)       
50B4: 80             ADD     A,B             
50B5: 42             LD      B,D             
50B6: 10 00          DJNZ    $50B8           
50B8: 80             ADD     A,B             
50B9: 00             NOP                     
50BA: 12             LD      (DE),A          
50BB: 10 08          DJNZ    $50C5           
50BD: 00             NOP                     
50BE: 80             ADD     A,B             
50BF: 12             LD      (DE),A          
50C0: 10 08          DJNZ    $50CA           
50C2: 80             ADD     A,B             
50C3: 00             NOP                     
50C4: 12             LD      (DE),A          
50C5: 10 06          DJNZ    $50CD           
50C7: 00             NOP                     
50C8: 80             ADD     A,B             
50C9: 05             DEC     B               
50CA: 10 06          DJNZ    $50D2           
50CC: 80             ADD     A,B             
50CD: 00             NOP                     
50CE: 05             DEC     B               
50CF: 10 07          DJNZ    $50D8           
50D1: 00             NOP                     
50D2: 80             ADD     A,B             
50D3: 2D             DEC     L               
50D4: 10 07          DJNZ    $50DD           
50D6: 80             ADD     A,B             
50D7: 00             NOP                     
50D8: 2D             DEC     L               
50D9: 12             LD      (DE),A          
50DA: 00             NOP                     
50DB: 80             ADD     A,B             
50DC: 00             NOP                     
50DD: 15             DEC     D               
50DE: 15             DEC     D               
50DF: 00             NOP                     
50E0: 80             ADD     A,B             
50E1: 00             NOP                     
50E2: 17             RLA                     
50E3: 15             DEC     D               
50E4: 07             RLCA                    
50E5: 00             NOP                     
50E6: 80             ADD     A,B             
50E7: 17             RLA                     
50E8: 15             DEC     D               
50E9: 08             EX      AF,AF'          
50EA: 00             NOP                     
50EB: 80             ADD     A,B             
50EC: 17             RLA                     
50ED: 15             DEC     D               
50EE: 09             ADD     HL,BC           
50EF: 00             NOP                     
50F0: 80             ADD     A,B             
50F1: 17             RLA                     
50F2: 15             DEC     D               
50F3: 0C             INC     C               
50F4: 00             NOP                     
50F5: 80             ADD     A,B             
50F6: 17             RLA                     
50F7: 15             DEC     D               
50F8: 05             DEC     B               
50F9: 00             NOP                     
50FA: 00             NOP                     
50FB: 36 15          LD      (HL),$15        
50FD: 05             DEC     B               
50FE: 00             NOP                     
50FF: 80             ADD     A,B             
5100: 36 15          LD      (HL),$15        
5102: 06 00          LD      B,$00           
5104: 00             NOP                     
5105: 37             SCF                     
5106: 15             DEC     D               
5107: 06 00          LD      B,$00           
5109: 80             ADD     A,B             
510A: 37             SCF                     
510B: 15             DEC     D               
510C: 04             INC     B               
510D: 00             NOP                     
510E: 80             ADD     A,B             
510F: 38 18          JR      C,$5129         
5111: 00             NOP                     
5112: 00             NOP                     
5113: 00             NOP                     
5114: 1A             LD      A,(DE)          
5115: 05             DEC     B               
5116: 01 00 00       LD      BC,$0000        
5119: 01 06 01       LD      BC,$0106        
511C: 00             NOP                     
511D: 00             NOP                     
511E: 02             LD      (BC),A          
511F: 07             RLCA                    
5120: 01 00 00       LD      BC,$0000        
5123: 03             INC     BC              
5124: 08             EX      AF,AF'          
5125: 01 00 00       LD      BC,$0000        
5128: 04             INC     B               
5129: 0A             LD      A,(BC)          
512A: 08             EX      AF,AF'          
512B: 00             NOP                     
512C: 20 06          JR      NZ,$5134        
512E: 0A             LD      A,(BC)          
512F: 08             EX      AF,AF'          
5130: 20 00          JR      NZ,$5132        
5132: 06 0A          LD      B,$0A           
5134: 0A             LD      A,(BC)          
5135: 20 80          JR      NZ,$50B7        
5137: 06 0A          LD      B,$0A           
5139: 04             INC     B               
513A: 20 80          JR      NZ,$50BC        
513C: 06 0A          LD      B,$0A           
513E: 0C             INC     C               
513F: 20 80          JR      NZ,$50C1        
5141: 06 0C          LD      B,$0C           
5143: 07             RLCA                    
5144: 00             NOP                     
5145: 00             NOP                     
5146: 0A             LD      A,(BC)          
5147: 0C             INC     C               
5148: 08             EX      AF,AF'          
5149: 00             NOP                     
514A: 00             NOP                     
514B: 0A             LD      A,(BC)          
514C: 0C             INC     C               
514D: 09             ADD     HL,BC           
514E: 80             ADD     A,B             
514F: 00             NOP                     
5150: 0B             DEC     BC              
5151: 0C             INC     C               
5152: 09             ADD     HL,BC           
5153: 00             NOP                     
5154: 80             ADD     A,B             
5155: 0A             LD      A,(BC)          
5156: 0C             INC     C               
5157: 0B             DEC     BC              
5158: 00             NOP                     
5159: 00             NOP                     
515A: 0A             LD      A,(BC)          
515B: 0C             INC     C               
515C: 0A             LD      A,(BC)          
515D: 00             NOP                     
515E: 00             NOP                     
515F: 0A             LD      A,(BC)          
5160: 0C             INC     C               
5161: 0B             DEC     BC              
5162: 00             NOP                     
5163: 80             ADD     A,B             
5164: 1B             DEC     DE              
5165: 0C             INC     C               
5166: 0A             LD      A,(BC)          
5167: 00             NOP                     
5168: 80             ADD     A,B             
5169: 1C             INC     E               
516A: 0C             INC     C               
516B: 06 00          LD      B,$00           
516D: 00             NOP                     
516E: 1D             DEC     E               
516F: 32 00 00       LD      ($0000),A       
5172: 00             NOP                     
5173: 21 2B 00       LD      HL,$002B        
5176: 00             NOP                     
5177: 00             NOP                     
5178: 22 2D 00       LD      ($002D),HL      
517B: 00             NOP                     
517C: 00             NOP                     
517D: 23             INC     HL              
517E: 3B             DEC     SP              
517F: 00             NOP                     
5180: 00             NOP                     
5181: 00             NOP                     
5182: 44             LD      B,H             
5183: 3B             DEC     SP              
5184: 00             NOP                     
5185: 10 00          DJNZ    $5187           
5187: 45             LD      B,L             
5188: 3B             DEC     SP              
5189: 01 00 00       LD      BC,$0000        
518C: 44             LD      B,H             
518D: 3B             DEC     SP              
518E: 01 00 10       LD      BC,$1000        
5191: 45             LD      B,L             
5192: 3B             DEC     SP              
5193: 01 10 00       LD      BC,$0010        
5196: 45             LD      B,L             
5197: 3C             INC     A               
5198: 00             NOP                     
5199: 00             NOP                     
519A: 00             NOP                     
519B: 46             LD      B,(HL)          
519C: 3C             INC     A               
519D: 00             NOP                     
519E: 80             ADD     A,B             
519F: 00             NOP                     
51A0: 47             LD      B,A             
51A1: 21 00 00       LD      HL,$0000        
51A4: 00             NOP                     
51A5: 25             DEC     H               
51A6: 21 01 00       LD      HL,$0001        
51A9: 80             ADD     A,B             
51AA: 3D             DEC     A               
51AB: 21 05 00       LD      HL,$0005        
51AE: 80             ADD     A,B             
51AF: 36 21          LD      (HL),$21        
51B1: 06 00          LD      B,$00           
51B3: 80             ADD     A,B             
51B4: 37             SCF                     
51B5: 21 04 00       LD      HL,$0004        
51B8: 80             ADD     A,B             
51B9: 38 21          JR      C,$51DC         
51BB: 07             RLCA                    
51BC: 00             NOP                     
51BD: 80             ADD     A,B             
51BE: 17             RLA                     
51BF: 21 08 00       LD      HL,$0008        
51C2: 80             ADD     A,B             
51C3: 17             RLA                     
51C4: 21 0B 00       LD      HL,$000B        
51C7: 80             ADD     A,B             
51C8: 26 23          LD      H,$23           
51CA: 00             NOP                     
51CB: 80             ADD     A,B             
51CC: 00             NOP                     
51CD: 27             DAA                     
51CE: 23             INC     HL              
51CF: 08             EX      AF,AF'          
51D0: 00             NOP                     
51D1: 80             ADD     A,B             
51D2: 27             DAA                     
51D3: 23             INC     HL              
51D4: 05             DEC     B               
51D5: 00             NOP                     
51D6: 80             ADD     A,B             
51D7: 27             DAA                     
51D8: 24             INC     H               
51D9: 02             LD      (BC),A          
51DA: 10 80          DJNZ    $515C           
51DC: 28 24          JR      Z,$5202         
51DE: 01 80 10       LD      BC,$1080        
51E1: 29             ADD     HL,HL           
51E2: 1C             INC     E               
51E3: 00             NOP                     
51E4: 80             ADD     A,B             
51E5: 00             NOP                     
51E6: 2D             DEC     L               
51E7: 1F             RRA                     
51E8: 00             NOP                     
51E9: 00             NOP                     
51EA: 00             NOP                     
51EB: 2F             CPL                     
51EC: 1F             RRA                     
51ED: 0B             DEC     BC              
51EE: 00             NOP                     
51EF: 00             NOP                     
51F0: 2F             CPL                     
51F1: 09             ADD     HL,BC           
51F2: 07             RLCA                    
51F3: 00             NOP                     
51F4: 00             NOP                     
51F5: 2F             CPL                     
51F6: 20 09          JR      NZ,$5201        
51F8: 00             NOP                     
51F9: 80             ADD     A,B             
51FA: 34             INC     (HL)            
51FB: 20 05          JR      NZ,$5202        
51FD: 00             NOP                     
51FE: 80             ADD     A,B             
51FF: 36 20          LD      (HL),$20        
5201: 06 00          LD      B,$00           
5203: 80             ADD     A,B             
5204: 37             SCF                     
5205: 3D             DEC     A               
5206: 00             NOP                     
5207: 80             ADD     A,B             
5208: 00             NOP                     
5209: 48             LD      C,B             
520A: 3E 08          LD      A,$08           
520C: 80             ADD     A,B             
520D: 00             NOP                     
520E: 48             LD      C,B             
520F: 3E 08          LD      A,$08           
5211: 00             NOP                     
5212: 80             ADD     A,B             
5213: 48             LD      C,B             
5214: 09             ADD     HL,BC           
5215: 08             EX      AF,AF'          
5216: 00             NOP                     
5217: 80             ADD     A,B             
5218: 48             LD      C,B             
5219: 09             ADD     HL,BC           
521A: 08             EX      AF,AF'          
521B: 80             ADD     A,B             
521C: 00             NOP                     
521D: 48             LD      C,B             
521E: 3F             CCF                     
521F: 00             NOP                     
5220: 00             NOP                     
5221: 00             NOP                     
5222: 4A             LD      C,D             
5223: 3F             CCF                     
5224: 02             LD      (BC),A          
5225: 00             NOP                     
5226: 00             NOP                     
5227: 4A             LD      C,D             
5228: 40             LD      B,B             
5229: 00             NOP                     
522A: 80             ADD     A,B             
522B: 00             NOP                     
522C: 49             LD      C,C             
522D: 40             LD      B,B             
522E: 01 80 80       LD      BC,$8080        
5231: 49             LD      C,C             
5232: 00             NOP                     
5233: AC             XOR     H               
5234: 00             NOP                     
5235: 03             INC     BC              
5236: 47             LD      B,A             
5237: 45             LD      B,L             
5238: 54             LD      D,H             
5239: 09             ADD     HL,BC           
523A: 04             INC     B               
523B: 47             LD      B,A             
523C: 52             LD      D,D             
523D: 41             LD      B,C             
523E: 42             LD      B,D             
523F: 09             ADD     HL,BC           
5240: 05             DEC     B               
5241: 54             LD      D,H             
5242: 48             LD      C,B             
5243: 52             LD      D,D             
5244: 4F             LD      C,A             
5245: 57             LD      D,A             
5246: 03             INC     BC              
5247: 06 41          LD      B,$41           
5249: 54             LD      D,H             
524A: 54             LD      D,H             
524B: 41             LD      B,C             
524C: 43             LD      B,E             
524D: 4B             LD      C,E             
524E: 04             INC     B               
524F: 05             DEC     B               
5250: 42             LD      B,D             
5251: 52             LD      D,D             
5252: 45             LD      B,L             
5253: 41             LD      B,C             
5254: 4B             LD      C,E             
5255: 04             INC     B               
5256: 04             INC     B               
5257: 4B             LD      C,E             
5258: 49             LD      C,C             
5259: 4C             LD      C,H             
525A: 4C             LD      C,H             
525B: 04             INC     B               
525C: 03             INC     BC              
525D: 48             LD      C,B             
525E: 49             LD      C,C             
525F: 54             LD      D,H             
5260: 04             INC     B               
5261: 05             DEC     B               
5262: 4E             LD      C,(HL)          
5263: 4F             LD      C,A             
5264: 52             LD      D,D             
5265: 54             LD      D,H             
5266: 48             LD      C,B             
5267: 05             DEC     B               
5268: 01 4E 05       LD      BC,$054E        
526B: 05             DEC     B               
526C: 53             LD      D,E             
526D: 4F             LD      C,A             
526E: 55             LD      D,L             
526F: 54             LD      D,H             
5270: 48             LD      C,B             
5271: 06 01          LD      B,$01           
5273: 53             LD      D,E             
5274: 06 04          LD      B,$04           
5276: 45             LD      B,L             
5277: 41             LD      B,C             
5278: 53             LD      D,E             
5279: 54             LD      D,H             
527A: 07             RLCA                    
527B: 01 45 07       LD      BC,$0745        
527E: 04             INC     B               
527F: 57             LD      D,A             
5280: 45             LD      B,L             
5281: 53             LD      D,E             
5282: 54             LD      D,H             
5283: 08             EX      AF,AF'          
5284: 01 57 08       LD      BC,$0857        
5287: 04             INC     B               
5288: 54             LD      D,H             
5289: 41             LD      B,C             
528A: 4B             LD      C,E             
528B: 45             LD      B,L             
528C: 09             ADD     HL,BC           
528D: 05             DEC     B               
528E: 43             LD      B,E             
528F: 41             LD      B,C             
5290: 52             LD      D,D             
5291: 52             LD      D,D             
5292: 59             LD      E,C             
5293: 09             ADD     HL,BC           
5294: 04             INC     B               
5295: 44             LD      B,H             
5296: 52             LD      D,D             
5297: 4F             LD      C,A             
5298: 50             LD      D,B             
5299: 0A             LD      A,(BC)          
529A: 03             INC     BC              
529B: 50             LD      D,B             
529C: 55             LD      D,L             
529D: 54             LD      D,H             
529E: 0A             LD      A,(BC)          
529F: 06 49          LD      B,$49           
52A1: 4E             LD      C,(HL)          
52A2: 56             LD      D,(HL)          
52A3: 45             LD      B,L             
52A4: 4E             LD      C,(HL)          
52A5: 54             LD      D,H             
52A6: 0B             DEC     BC              
52A7: 04             INC     B               
52A8: 4C             LD      C,H             
52A9: 4F             LD      C,A             
52AA: 4F             LD      C,A             
52AB: 4B             LD      C,E             
52AC: 0C             INC     C               
52AD: 04             INC     B               
52AE: 47             LD      B,A             
52AF: 49             LD      C,C             
52B0: 56             LD      D,(HL)          
52B1: 45             LD      B,L             
52B2: 0D             DEC     C               
52B3: 05             DEC     B               
52B4: 4F             LD      C,A             
52B5: 46             LD      B,(HL)          
52B6: 46             LD      B,(HL)          
52B7: 45             LD      B,L             
52B8: 52             LD      D,D             
52B9: 0D             DEC     C               
52BA: 06 45          LD      B,$45           
52BC: 58             LD      E,B             
52BD: 41             LD      B,C             
52BE: 4D             LD      C,L             
52BF: 49             LD      C,C             
52C0: 4E             LD      C,(HL)          
52C1: 0E 06          LD      C,$06           
52C3: 53             LD      D,E             
52C4: 45             LD      B,L             
52C5: 41             LD      B,C             
52C6: 52             LD      D,D             
52C7: 43             LD      B,E             
52C8: 48             LD      C,B             
52C9: 0E 04          LD      C,$04           
52CB: 4F             LD      C,A             
52CC: 50             LD      D,B             
52CD: 45             LD      B,L             
52CE: 4E             LD      C,(HL)          
52CF: 0F             RRCA                    
52D0: 04             INC     B               
52D1: 50             LD      D,B             
52D2: 55             LD      D,L             
52D3: 4C             LD      C,H             
52D4: 4C             LD      C,H             
52D5: 10 03          DJNZ    $52DA           
52D7: 45             LD      B,L             
52D8: 41             LD      B,C             
52D9: 54             LD      D,H             
52DA: 12             LD      (DE),A          
52DB: 05             DEC     B               
52DC: 43             LD      B,E             
52DD: 4C             LD      C,H             
52DE: 49             LD      C,C             
52DF: 4D             LD      C,L             
52E0: 42             LD      B,D             
52E1: 15             DEC     D               
52E2: 06 41          LD      B,$41           
52E4: 53             LD      D,E             
52E5: 43             LD      B,E             
52E6: 45             LD      B,L             
52E7: 4E             LD      C,(HL)          
52E8: 44             LD      B,H             
52E9: 15             DEC     D               
52EA: 06 44          LD      B,$44           
52EC: 45             LD      B,L             
52ED: 53             LD      D,E             
52EE: 43             LD      B,E             
52EF: 45             LD      B,L             
52F0: 4E             LD      C,(HL)          
52F1: 15             DEC     D               
52F2: 04             INC     B               
52F3: 4C             LD      C,H             
52F4: 49             LD      C,C             
52F5: 46             LD      B,(HL)          
52F6: 54             LD      D,H             
52F7: 1C             INC     E               
52F8: 04             INC     B               
52F9: 57             LD      D,A             
52FA: 41             LD      B,C             
52FB: 49             LD      C,C             
52FC: 54             LD      D,H             
52FD: 1F             RRA                     
52FE: 04             INC     B               
52FF: 53             LD      D,E             
5300: 54             LD      D,H             
5301: 41             LD      B,C             
5302: 59             LD      E,C             
5303: 1F             RRA                     
5304: 04             INC     B               
5305: 4A             LD      C,D             
5306: 55             LD      D,L             
5307: 4D             LD      C,L             
5308: 50             LD      D,B             
5309: 20 02          JR      NZ,$530D        
530B: 47             LD      B,A             
530C: 4F             LD      C,A             
530D: 21 03 52       LD      HL,$5203        
5310: 55             LD      D,L             
5311: 4E             LD      C,(HL)          
5312: 21 04 4C       LD      HL,$4C04        
5315: 45             LD      B,L             
5316: 46             LD      B,(HL)          
5317: 54             LD      D,H             
5318: 21 05 52       LD      HL,$5205        
531B: 49             LD      C,C             
531C: 47             LD      B,A             
531D: 48             LD      C,B             
531E: 54             LD      D,H             
531F: 21 05 45       LD      HL,$4505        
5322: 4E             LD      C,(HL)          
5323: 54             LD      D,H             
5324: 45             LD      B,L             
5325: 52             LD      D,D             
5326: 21 04 50       LD      HL,$5004        
5329: 55             LD      D,L             
532A: 53             LD      D,E             
532B: 48             LD      C,B             
532C: 10 04          DJNZ    $5332           
532E: 4D             LD      C,L             
532F: 4F             LD      C,A             
5330: 56             LD      D,(HL)          
5331: 45             LD      B,L             
5332: 10 04          DJNZ    $5338           
5334: 4B             LD      C,E             
5335: 49             LD      C,C             
5336: 43             LD      B,E             
5337: 4B             LD      C,E             
5338: 23             INC     HL              
5339: 04             INC     B               
533A: 46             LD      B,(HL)          
533B: 45             LD      B,L             
533C: 45             LD      B,L             
533D: 44             LD      B,H             
533E: 24             INC     H               
533F: 06 53          LD      B,$53           
5341: 43             LD      B,E             
5342: 52             LD      D,D             
5343: 45             LD      B,L             
5344: 41             LD      B,C             
5345: 4D             LD      C,L             
5346: 2B             DEC     HL              
5347: 04             INC     B               
5348: 59             LD      E,C             
5349: 45             LD      B,L             
534A: 4C             LD      C,H             
534B: 4C             LD      C,H             
534C: 2B             DEC     HL              
534D: 04             INC     B               
534E: 51             LD      D,C             
534F: 55             LD      D,L             
5350: 49             LD      C,C             
5351: 54             LD      D,H             
5352: 2D             DEC     L               
5353: 04             INC     B               
5354: 53             LD      D,E             
5355: 54             LD      D,H             
5356: 4F             LD      C,A             
5357: 50             LD      D,B             
5358: 2D             DEC     L               
5359: 05             DEC     B               
535A: 50             LD      D,B             
535B: 4C             LD      C,H             
535C: 55             LD      D,L             
535D: 47             LD      B,A             
535E: 48             LD      C,B             
535F: 32 04 50       LD      ($5004),A       
5362: 49             LD      C,C             
5363: 43             LD      B,E             
5364: 4B             LD      C,E             
5365: 34             INC     (HL)            
5366: 05             DEC     B               
5367: 43             LD      B,E             
5368: 4C             LD      C,H             
5369: 4F             LD      C,A             
536A: 53             LD      D,E             
536B: 45             LD      B,L             
536C: 38 04          JR      C,$5372         
536E: 4C             LD      C,H             
536F: 4F             LD      C,A             
5370: 43             LD      B,E             
5371: 4B             LD      C,E             
5372: 39             ADD     HL,SP           
5373: 06 55          LD      B,$55           
5375: 4E             LD      C,(HL)          
5376: 4C             LD      C,H             
5377: 4F             LD      C,A             
5378: 43             LD      B,E             
5379: 4B             LD      C,E             
537A: 3A 05 48       LD      A,($4805)       
537D: 45             LD      B,L             
537E: 4C             LD      C,H             
537F: 4C             LD      C,H             
5380: 4F             LD      C,A             
5381: 3B             DEC     SP              
5382: 02             LD      (BC),A          
5383: 48             LD      C,B             
5384: 49             LD      C,C             
5385: 3B             DEC     SP              
5386: 03             INC     BC              
5387: 42             LD      B,D             
5388: 4F             LD      C,A             
5389: 57             LD      D,A             
538A: 3B             DEC     SP              
538B: 05             DEC     B               
538C: 47             LD      B,A             
538D: 52             LD      D,D             
538E: 45             LD      B,L             
538F: 45             LD      B,L             
5390: 54             LD      D,H             
5391: 3B             DEC     SP              
5392: 04             INC     B               
5393: 57             LD      D,A             
5394: 48             LD      C,B             
5395: 41             LD      B,C             
5396: 54             LD      D,H             
5397: 3C             INC     A               
5398: 03             INC     BC              
5399: 57             LD      D,A             
539A: 48             LD      C,B             
539B: 59             LD      E,C             
539C: 3C             INC     A               
539D: 03             INC     BC              
539E: 48             LD      C,B             
539F: 4F             LD      C,A             
53A0: 57             LD      D,A             
53A1: 3C             INC     A               
53A2: 05             DEC     B               
53A3: 57             LD      D,A             
53A4: 48             LD      C,B             
53A5: 45             LD      B,L             
53A6: 52             LD      D,D             
53A7: 45             LD      B,L             
53A8: 3C             INC     A               
53A9: 03             INC     BC              
53AA: 57             LD      D,A             
53AB: 48             LD      C,B             
53AC: 4F             LD      C,A             
53AD: 3C             INC     A               
53AE: 04             INC     B               
53AF: 57             LD      D,A             
53B0: 48             LD      C,B             
53B1: 45             LD      B,L             
53B2: 4E             LD      C,(HL)          
53B3: 3C             INC     A               
53B4: 05             DEC     B               
53B5: 4C             LD      C,H             
53B6: 4F             LD      C,A             
53B7: 57             LD      D,A             
53B8: 45             LD      B,L             
53B9: 52             LD      D,D             
53BA: 3D             DEC     A               
53BB: 05             DEC     B               
53BC: 55             LD      D,L             
53BD: 4E             LD      C,(HL)          
53BE: 54             LD      D,H             
53BF: 49             LD      C,C             
53C0: 45             LD      B,L             
53C1: 3D             DEC     A               
53C2: 03             INC     BC              
53C3: 4C             LD      C,H             
53C4: 45             LD      B,L             
53C5: 54             LD      D,H             
53C6: 3E 04          LD      A,$04           
53C8: 43             LD      B,E             
53C9: 4F             LD      C,A             
53CA: 4D             LD      C,L             
53CB: 45             LD      B,L             
53CC: 3F             CCF                     
53CD: 06 46          LD      B,$46           
53CF: 4F             LD      C,A             
53D0: 4C             LD      C,H             
53D1: 4C             LD      C,H             
53D2: 4F             LD      C,A             
53D3: 57             LD      D,A             
53D4: 3F             CCF                     
53D5: 04             INC     B               
53D6: 4D             LD      C,L             
53D7: 45             LD      B,L             
53D8: 45             LD      B,L             
53D9: 54             LD      D,H             
53DA: 40             LD      B,B             
53DB: 06 49          LD      B,$49           
53DD: 4E             LD      C,(HL)          
53DE: 54             LD      D,H             
53DF: 52             LD      D,D             
53E0: 4F             LD      C,A             
53E1: 44             LD      B,H             
53E2: 40             LD      B,B             
53E3: 00             NOP                     
53E4: 03             INC     BC              
53E5: 4B             LD      C,E             
53E6: 45             LD      B,L             
53E7: 59             LD      E,C             
53E8: 16 04          LD      D,$04           
53EA: 50             LD      D,B             
53EB: 49             LD      C,C             
53EC: 4C             LD      C,H             
53ED: 4C             LD      C,H             
53EE: 17             RLA                     
53EF: 04             INC     B               
53F0: 48             LD      C,B             
53F1: 4F             LD      C,A             
53F2: 4F             LD      C,A             
53F3: 4B             LD      C,E             
53F4: 18 04          JR      $53FA           
53F6: 44             LD      B,H             
53F7: 4F             LD      C,A             
53F8: 4F             LD      C,A             
53F9: 52             LD      D,D             
53FA: 0B             DEC     BC              
53FB: 06 43          LD      B,$43           
53FD: 41             LD      B,C             
53FE: 42             LD      B,D             
53FF: 49             LD      C,C             
5400: 4E             LD      C,(HL)          
5401: 45             LD      B,L             
5402: 19             ADD     HL,DE           
5403: 06 52          LD      B,$52           
5405: 45             LD      B,L             
5406: 46             LD      B,(HL)          
5407: 52             LD      D,D             
5408: 49             LD      C,C             
5409: 47             LD      B,A             
540A: 1A             LD      A,(DE)          
540B: 06 48          LD      B,$48           
540D: 41             LD      B,C             
540E: 4D             LD      C,L             
540F: 42             LD      B,D             
5410: 55             LD      D,L             
5411: 52             LD      D,D             
5412: 1B             DEC     DE              
5413: 06 42          LD      B,$42           
5415: 55             LD      D,L             
5416: 52             LD      D,D             
5417: 47             LD      B,A             
5418: 45             LD      B,L             
5419: 52             LD      D,D             
541A: 1B             DEC     DE              
541B: 04             INC     B               
541C: 4D             LD      C,L             
541D: 45             LD      B,L             
541E: 41             LD      B,C             
541F: 54             LD      D,H             
5420: 1B             DEC     DE              
5421: 03             INC     BC              
5422: 44             LD      B,H             
5423: 4F             LD      C,A             
5424: 47             LD      B,A             
5425: 08             EX      AF,AF'          
5426: 04             INC     B               
5427: 48             LD      C,B             
5428: 41             LD      B,C             
5429: 4E             LD      C,(HL)          
542A: 44             LD      B,H             
542B: 1F             RRA                     
542C: 05             DEC     B               
542D: 48             LD      C,B             
542E: 41             LD      B,C             
542F: 4E             LD      C,(HL)          
5430: 44             LD      B,H             
5431: 53             LD      D,E             
5432: 1F             RRA                     
5433: 06 4E          LD      B,$4E           
5435: 41             LD      B,C             
5436: 50             LD      D,B             
5437: 4F             LD      C,A             
5438: 4C             LD      C,H             
5439: 45             LD      B,L             
543A: 02             LD      (BC),A          
543B: 06 42          LD      B,$42           
543D: 4F             LD      C,A             
543E: 4E             LD      C,(HL)          
543F: 41             LD      B,C             
5440: 50             LD      D,B             
5441: 41             LD      B,C             
5442: 02             LD      (BC),A          
5443: 03             INC     BC              
5444: 52             LD      D,D             
5445: 41             LD      B,C             
5446: 59             LD      E,C             
5447: 03             INC     BC              
5448: 04             INC     B               
5449: 58             LD      E,B             
544A: 52             LD      D,D             
544B: 41             LD      B,C             
544C: 59             LD      E,C             
544D: 03             INC     BC              
544E: 06 4A          LD      B,$4A           
5450: 4F             LD      C,A             
5451: 48             LD      C,B             
5452: 4E             LD      C,(HL)          
5453: 53             LD      D,E             
5454: 4F             LD      C,A             
5455: 03             INC     BC              
5456: 06 48          LD      B,$48           
5458: 4F             LD      C,A             
5459: 55             LD      D,L             
545A: 44             LD      B,H             
545B: 49             LD      C,C             
545C: 4E             LD      C,(HL)          
545D: 04             INC     B               
545E: 06 50          LD      B,$50           
5460: 49             LD      C,C             
5461: 43             LD      B,E             
5462: 41             LD      B,C             
5463: 53             LD      D,E             
5464: 53             LD      D,E             
5465: 05             DEC     B               
5466: 06 4D          LD      B,$4D           
5468: 45             LD      B,L             
5469: 52             LD      D,D             
546A: 4C             LD      C,H             
546B: 49             LD      C,C             
546C: 4E             LD      C,(HL)          
546D: 06 06          LD      B,$06           
546F: 44             LD      B,H             
5470: 4F             LD      C,A             
5471: 43             LD      B,E             
5472: 54             LD      D,H             
5473: 4F             LD      C,A             
5474: 52             LD      D,D             
5475: 07             RLCA                    
5476: 05             DEC     B               
5477: 4E             LD      C,(HL)          
5478: 55             LD      D,L             
5479: 52             LD      D,D             
547A: 53             LD      D,E             
547B: 45             LD      B,L             
547C: 01 06 54       LD      BC,$5406        
547F: 48             LD      C,B             
5480: 45             LD      B,L             
5481: 52             LD      D,D             
5482: 41             LD      B,C             
5483: 50             LD      D,B             
5484: 01 04 57       LD      BC,$5704        
5487: 41             LD      B,C             
5488: 4C             LD      C,H             
5489: 4C             LD      C,H             
548A: 25             DEC     H               
548B: 05             DEC     B               
548C: 57             LD      D,A             
548D: 41             LD      B,C             
548E: 4C             LD      C,H             
548F: 4C             LD      C,H             
5490: 53             LD      D,E             
5491: 25             DEC     H               
5492: 04             INC     B               
5493: 52             LD      D,D             
5494: 4F             LD      C,A             
5495: 4F             LD      C,A             
5496: 4D             LD      C,L             
5497: 2A 04 43       LD      HL,($4304)      
549A: 45             LD      B,L             
549B: 4C             LD      C,H             
549C: 4C             LD      C,H             
549D: 2A 06 4F       LD      HL,($4F06)      
54A0: 46             LD      B,(HL)          
54A1: 46             LD      B,(HL)          
54A2: 49             LD      C,C             
54A3: 43             LD      B,E             
54A4: 45             LD      B,L             
54A5: 2A 04 53       LD      HL,($5304)      
54A8: 48             LD      C,B             
54A9: 45             LD      B,L             
54AA: 44             LD      B,H             
54AB: 2A 05 46       LD      HL,($4605)      
54AE: 4C             LD      C,H             
54AF: 4F             LD      C,A             
54B0: 4F             LD      C,A             
54B1: 52             LD      D,D             
54B2: 2B             DEC     HL              
54B3: 04             INC     B               
54B4: 45             LD      B,L             
54B5: 58             LD      E,B             
54B6: 49             LD      C,C             
54B7: 54             LD      D,H             
54B8: 2C             INC     L               
54B9: 04             INC     B               
54BA: 48             LD      C,B             
54BB: 4F             LD      C,A             
54BC: 4C             LD      C,H             
54BD: 45             LD      B,L             
54BE: 19             ADD     HL,DE           
54BF: 06 48          LD      B,$48           
54C1: 41             LD      B,C             
54C2: 4C             LD      C,H             
54C3: 4C             LD      C,H             
54C4: 57             LD      D,A             
54C5: 41             LD      B,C             
54C6: 33             INC     SP              
54C7: 06 45          LD      B,$45           
54C9: 4E             LD      C,(HL)          
54CA: 54             LD      D,H             
54CB: 52             LD      D,D             
54CC: 41             LD      B,C             
54CD: 4E             LD      C,(HL)          
54CE: 36 06          LD      (HL),$06        
54D0: 43             LD      B,E             
54D1: 45             LD      B,L             
54D2: 49             LD      C,C             
54D3: 4C             LD      C,H             
54D4: 49             LD      C,C             
54D5: 4E             LD      C,(HL)          
54D6: 3B             DEC     SP              
54D7: 04             INC     B               
54D8: 52             LD      D,D             
54D9: 4F             LD      C,A             
54DA: 4F             LD      C,A             
54DB: 46             LD      B,(HL)          
54DC: 3B             DEC     SP              
54DD: 00             NOP                     
54DE: 03             INC     BC              
54DF: 52             LD      D,D             
54E0: 45             LD      B,L             
54E1: 44             LD      B,H             
54E2: 13             INC     DE              
54E3: 05             DEC     B               
54E4: 47             LD      B,A             
54E5: 52             LD      D,D             
54E6: 45             LD      B,L             
54E7: 45             LD      B,L             
54E8: 4E             LD      C,(HL)          
54E9: 14             INC     D               
54EA: 04             INC     B               
54EB: 42             LD      B,D             
54EC: 4C             LD      C,H             
54ED: 55             LD      D,L             
54EE: 45             LD      B,L             
54EF: 15             DEC     D               
54F0: 06 53          LD      B,$53           
54F2: 45             LD      B,L             
54F3: 43             LD      B,E             
54F4: 52             LD      D,D             
54F5: 45             LD      B,L             
54F6: 54             LD      D,H             
54F7: 3D             DEC     A               
54F8: 06 50          LD      B,$50           
54FA: 41             LD      B,C             
54FB: 49             LD      C,C             
54FC: 4E             LD      C,(HL)          
54FD: 54             LD      D,H             
54FE: 45             LD      B,L             
54FF: 3E 00          LD      A,$00           
5501: 02             LD      (BC),A          
5502: 54             LD      D,H             
5503: 4F             LD      C,A             
5504: 01 04 57       LD      BC,$5704        
5507: 49             LD      C,C             
5508: 54             LD      D,H             
5509: 48             LD      C,B             
550A: 02             LD      (BC),A          
550B: 05             DEC     B               
550C: 55             LD      D,L             
550D: 53             LD      D,E             
550E: 49             LD      C,C             
550F: 4E             LD      C,(HL)          
5510: 47             LD      B,A             
5511: 02             LD      (BC),A          
5512: 02             LD      (BC),A          
5513: 41             LD      B,C             
5514: 54             LD      D,H             
5515: 03             INC     BC              
5516: 05             DEC     B               
5517: 55             LD      D,L             
5518: 4E             LD      C,(HL)          
5519: 44             LD      B,H             
551A: 45             LD      B,L             
551B: 52             LD      D,D             
551C: 04             INC     B               
551D: 02             LD      (BC),A          
551E: 49             LD      C,C             
551F: 4E             LD      C,(HL)          
5520: 05             DEC     B               
5521: 04             INC     B               
5522: 49             LD      C,C             
5523: 4E             LD      C,(HL)          
5524: 54             LD      D,H             
5525: 4F             LD      C,A             
5526: 05             DEC     B               
5527: 06 49          LD      B,$49           
5529: 4E             LD      C,(HL)          
552A: 53             LD      D,E             
552B: 49             LD      C,C             
552C: 44             LD      B,H             
552D: 45             LD      B,L             
552E: 05             DEC     B               
552F: 03             INC     BC              
5530: 4F             LD      C,A             
5531: 55             LD      D,L             
5532: 54             LD      D,H             
5533: 06 06          LD      B,$06           
5535: 4F             LD      C,A             
5536: 55             LD      D,L             
5537: 54             LD      D,H             
5538: 53             LD      D,E             
5539: 49             LD      C,C             
553A: 44             LD      B,H             
553B: 06 02          LD      B,$02           
553D: 55             LD      D,L             
553E: 50             LD      D,B             
553F: 07             RLCA                    
5540: 04             INC     B               
5541: 44             LD      B,H             
5542: 4F             LD      C,A             
5543: 57             LD      D,A             
5544: 4E             LD      C,(HL)          
5545: 08             EX      AF,AF'          
5546: 04             INC     B               
5547: 4F             LD      C,A             
5548: 56             LD      D,(HL)          
5549: 45             LD      B,L             
554A: 52             LD      D,D             
554B: 09             ADD     HL,BC           
554C: 06 42          LD      B,$42           
554E: 45             LD      B,L             
554F: 48             LD      C,B             
5550: 49             LD      C,C             
5551: 4E             LD      C,(HL)          
5552: 44             LD      B,H             
5553: 0A             LD      A,(BC)          
5554: 06 41          LD      B,$41           
5556: 52             LD      D,D             
5557: 4F             LD      C,A             
5558: 55             LD      D,L             
5559: 4E             LD      C,(HL)          
555A: 44             LD      B,H             
555B: 0B             DEC     BC              
555C: 02             LD      (BC),A          
555D: 4F             LD      C,A             
555E: 4E             LD      C,(HL)          
555F: 0C             INC     C               
5560: 00             NOP                     
5561: 00             NOP                     
5562: 94             SUB     H               
5563: 9D             SBC     L               
5564: 0B             DEC     BC              
5565: 12             LD      (DE),A          
5566: 85             ADD     A,L             
5567: 00             NOP                     
5568: 88             ADC     A,B             
5569: 03             INC     BC              
556A: 01 84 01       LD      BC,$0184        
556D: 01 14 02       LD      BC,$0214        
5570: 07             RLCA                    
5571: AF             XOR     A               
5572: 6E             LD      L,(HL)          
5573: 83             ADD     A,E             
5574: 61             LD      H,C             
5575: 81             ADD     A,C             
5576: 5B             LD      E,E             
5577: 52             LD      D,D             
5578: 0B             DEC     BC              
5579: 12             LD      (DE),A          
557A: 84             ADD     A,H             
557B: 00             NOP                     
557C: 8A             ADC     A,D             
557D: 03             INC     BC              
557E: 01 86 01       LD      BC,$0186        
5581: 01 14 02       LD      BC,$0214        
5584: 07             RLCA                    
5585: AF             XOR     A               
5586: 6E             LD      L,(HL)          
5587: 83             ADD     A,E             
5588: 61             LD      H,C             
5589: 81             ADD     A,C             
558A: 5B             LD      E,E             
558B: 52             LD      D,D             
558C: 0B             DEC     BC              
558D: 11 84 00       LD      DE,$0084        
5590: 8B             ADC     A,E             
5591: 03             INC     BC              
5592: 01 87 01       LD      BC,$0187        
5595: 01 13 02       LD      BC,$0213        
5598: 06 66          LD      B,$66           
559A: B1             OR      C               
559B: 09             ADD     HL,BC           
559C: 15             DEC     D               
559D: A3             AND     E               
559E: A0             AND     B               
559F: 0B             DEC     BC              
55A0: 11 86 00       LD      DE,$0086        
55A3: 88             ADC     A,B             
55A4: 03             INC     BC              
55A5: 01 85 01       LD      BC,$0185        
55A8: 01 13 02       LD      BC,$0213        
55AB: 06 66          LD      B,$66           
55AD: B1             OR      C               
55AE: 09             ADD     HL,BC           
55AF: 15             DEC     D               
55B0: A3             AND     E               
55B1: A0             AND     B               
55B2: 0B             DEC     BC              
55B3: 12             LD      (DE),A          
55B4: 88             ADC     A,B             
55B5: 00             NOP                     
55B6: 8A             ADC     A,D             
55B7: 03             INC     BC              
55B8: 01 84 01       LD      BC,$0184        
55BB: 01 14 02       LD      BC,$0214        
55BE: 07             RLCA                    
55BF: AF             XOR     A               
55C0: 6E             LD      L,(HL)          
55C1: 83             ADD     A,E             
55C2: 61             LD      H,C             
55C3: 81             ADD     A,C             
55C4: 5B             LD      E,E             
55C5: 52             LD      D,D             
55C6: 0B             DEC     BC              
55C7: 12             LD      (DE),A          
55C8: 87             ADD     A,A             
55C9: 00             NOP                     
55CA: 88             ADC     A,B             
55CB: 03             INC     BC              
55CC: 01 86 01       LD      BC,$0186        
55CF: 01 14 02       LD      BC,$0214        
55D2: 07             RLCA                    
55D3: AF             XOR     A               
55D4: 6E             LD      L,(HL)          
55D5: 83             ADD     A,E             
55D6: 61             LD      H,C             
55D7: 81             ADD     A,C             
55D8: 5B             LD      E,E             
55D9: 52             LD      D,D             
55DA: 0B             DEC     BC              
55DB: 11 87 00       LD      DE,$0087        
55DE: 8B             ADC     A,E             
55DF: 03             INC     BC              
55E0: 01 87 01       LD      BC,$0187        
55E3: 01 13 02       LD      BC,$0213        
55E6: 06 66          LD      B,$66           
55E8: B1             OR      C               
55E9: 09             ADD     HL,BC           
55EA: 15             DEC     D               
55EB: A3             AND     E               
55EC: A0             AND     B               
55ED: 0B             DEC     BC              
55EE: 11 89 00       LD      DE,$0089        
55F1: 88             ADC     A,B             
55F2: 03             INC     BC              
55F3: 01 85 01       LD      BC,$0185        
55F6: 01 13 02       LD      BC,$0213        
55F9: 06 66          LD      B,$66           
55FB: B1             OR      C               
55FC: 09             ADD     HL,BC           
55FD: 15             DEC     D               
55FE: A3             AND     E               
55FF: A0             AND     B               
5600: 0B             DEC     BC              
5601: 12             LD      (DE),A          
5602: 8B             ADC     A,E             
5603: 00             NOP                     
5604: 88             ADC     A,B             
5605: 03             INC     BC              
5606: 01 84 01       LD      BC,$0184        
5609: 01 14 02       LD      BC,$0214        
560C: 07             RLCA                    
560D: AF             XOR     A               
560E: 6E             LD      L,(HL)          
560F: 83             ADD     A,E             
5610: 61             LD      H,C             
5611: 81             ADD     A,C             
5612: 5B             LD      E,E             
5613: 52             LD      D,D             
5614: 0B             DEC     BC              
5615: 12             LD      (DE),A          
5616: 8A             ADC     A,D             
5617: 00             NOP                     
5618: 8A             ADC     A,D             
5619: 03             INC     BC              
561A: 01 86 01       LD      BC,$0186        
561D: 01 14 02       LD      BC,$0214        
5620: 07             RLCA                    
5621: AF             XOR     A               
5622: 6E             LD      L,(HL)          
5623: 83             ADD     A,E             
5624: 61             LD      H,C             
5625: 81             ADD     A,C             
5626: 5B             LD      E,E             
5627: 52             LD      D,D             
5628: 0B             DEC     BC              
5629: 11 8A 00       LD      DE,$008A        
562C: 8B             ADC     A,E             
562D: 03             INC     BC              
562E: 01 87 01       LD      BC,$0187        
5631: 01 13 02       LD      BC,$0213        
5634: 06 66          LD      B,$66           
5636: B1             OR      C               
5637: 09             ADD     HL,BC           
5638: 15             DEC     D               
5639: A3             AND     E               
563A: A0             AND     B               
563B: 0B             DEC     BC              
563C: 12             LD      (DE),A          
563D: 8D             ADC     A,L             
563E: 00             NOP                     
563F: 88             ADC     A,B             
5640: 03             INC     BC              
5641: 01 84 01       LD      BC,$0184        
5644: 01 14 02       LD      BC,$0214        
5647: 07             RLCA                    
5648: AF             XOR     A               
5649: 6E             LD      L,(HL)          
564A: 83             ADD     A,E             
564B: 61             LD      H,C             
564C: 81             ADD     A,C             
564D: 5B             LD      E,E             
564E: 52             LD      D,D             
564F: 0B             DEC     BC              
5650: 12             LD      (DE),A          
5651: 8C             ADC     A,H             
5652: 00             NOP                     
5653: 8A             ADC     A,D             
5654: 03             INC     BC              
5655: 01 86 01       LD      BC,$0186        
5658: 01 14 02       LD      BC,$0214        
565B: 07             RLCA                    
565C: AF             XOR     A               
565D: 6E             LD      L,(HL)          
565E: 83             ADD     A,E             
565F: 61             LD      H,C             
5660: 81             ADD     A,C             
5661: 5B             LD      E,E             
5662: 52             LD      D,D             
5663: 0B             DEC     BC              
5664: 11 8F 00       LD      DE,$008F        
5667: 88             ADC     A,B             
5668: 03             INC     BC              
5669: 01 85 01       LD      BC,$0185        
566C: 01 13 02       LD      BC,$0213        
566F: 06 66          LD      B,$66           
5671: B1             OR      C               
5672: 09             ADD     HL,BC           
5673: 15             DEC     D               
5674: A3             AND     E               
5675: A0             AND     B               
5676: 0B             DEC     BC              
5677: 11 8F 00       LD      DE,$008F        
567A: 8A             ADC     A,D             
567B: 02             LD      (BC),A          
567C: 06 8F          LD      B,$8F           
567E: 4E             LD      C,(HL)          
567F: 46             LD      B,(HL)          
5680: 5E             LD      E,(HL)          
5681: 44             LD      B,H             
5682: A0             AND     B               
5683: 01 01 15       LD      BC,$1501        
5686: 03             INC     BC              
5687: 01 88 0B       LD      BC,$0B88        
568A: 11 90 00       LD      DE,$0090        
568D: 88             ADC     A,B             
568E: 03             INC     BC              
568F: 01 89 01       LD      BC,$0189        
5692: 01 15 02       LD      BC,$0215        
5695: 06 8F          LD      B,$8F           
5697: 4E             LD      C,(HL)          
5698: 46             LD      B,(HL)          
5699: 5E             LD      E,(HL)          
569A: 44             LD      B,H             
569B: A0             AND     B               
569C: 0B             DEC     BC              
569D: 11 91 00       LD      DE,$0091        
56A0: 8A             ADC     A,D             
56A1: 03             INC     BC              
56A2: 01 89 01       LD      BC,$0189        
56A5: 01 15 02       LD      BC,$0215        
56A8: 06 8F          LD      B,$8F           
56AA: 4E             LD      C,(HL)          
56AB: 46             LD      B,(HL)          
56AC: 5E             LD      E,(HL)          
56AD: 44             LD      B,H             
56AE: A0             AND     B               
56AF: 0B             DEC     BC              
56B0: 11 94 00       LD      DE,$0094        
56B3: 88             ADC     A,B             
56B4: 03             INC     BC              
56B5: 01 88 01       LD      BC,$0188        
56B8: 01 15 02       LD      BC,$0215        
56BB: 06 8F          LD      B,$8F           
56BD: 4E             LD      C,(HL)          
56BE: 46             LD      B,(HL)          
56BF: 5E             LD      E,(HL)          
56C0: 44             LD      B,H             
56C1: A0             AND     B               
56C2: FF             RST     0X38            
56C3: 42             LD      B,D             
56C4: 88             ADC     A,B             
56C5: 00             NOP                     
56C6: 80             ADD     A,B             
56C7: 08             EX      AF,AF'          
56C8: 06 0D          LD      B,$0D           
56CA: 04             INC     B               
56CB: 03             INC     BC              
56CC: 13             INC     DE              
56CD: 3A 9B 0A       LD      A,($0A9B)       
56D0: 31 0D 2F       LD      SP,$2F0D        
56D3: 1F             RRA                     
56D4: 29             ADD     HL,HL           
56D5: C7             RST     0X00            
56D6: DE DB          SBC     $DB             
56D8: 16 CB          LD      D,$CB           
56DA: B9             CP      C               
56DB: 36 A1          LD      (HL),$A1        
56DD: B0             OR      B               
56DE: 17             RLA                     
56DF: F4 59 82       CALL    P,$8259         
56E2: 17             RLA                     
56E3: 73             LD      (HL),E          
56E4: 49             LD      C,C             
56E5: 55             LD      D,L             
56E6: 8B             ADC     A,E             
56E7: 03             INC     BC              
56E8: BC             CP      H               
56E9: 3B             DEC     SP              
56EA: C0             RET     NZ              
56EB: AF             XOR     A               
56EC: 54             LD      D,H             
56ED: 51             LD      D,C             
56EE: 18 43          JR      $5733           
56F0: C2 0D D0       JP      NZ,$D00D        
56F3: 83             ADD     A,E             
56F4: 61             LD      H,C             
56F5: 83             ADD     A,E             
56F6: 7A             LD      A,D             
56F7: C7             RST     0X00            
56F8: DE 85          SBC     $85             
56FA: AF             XOR     A               
56FB: 46             LD      B,(HL)          
56FC: 61             LD      H,C             
56FD: 2E 2C          LD      L,$2C           
56FF: 13             INC     DE              
5700: 19             ADD     HL,DE           
5701: 88             ADC     A,B             
5702: 09             ADD     HL,BC           
5703: 02             LD      (BC),A          
5704: 46             LD      B,(HL)          
5705: 46             LD      B,(HL)          
5706: 16 21          LD      D,$21           
5708: 00             NOP                     
5709: 00             NOP                     
570A: A0             AND     B               
570B: 03             INC     BC              
570C: 12             LD      (DE),A          
570D: 04             INC     B               
570E: 10 5F          DJNZ    $576F           
5710: BE             CP      (HL)            
5711: 5B             LD      E,E             
5712: B1             OR      C               
5713: 4B             LD      C,E             
5714: 7B             LD      A,E             
5715: 54             LD      D,H             
5716: 45             LD      B,L             
5717: F3             DI                      
5718: 5F             LD      E,A             
5719: BB             CP      E               
571A: 85             ADD     A,L             
571B: 9F             SBC     A               
571C: 15             DEC     D               
571D: 7F             LD      A,A             
571E: B1             OR      C               
571F: 01 01 13       LD      BC,$1301        
5722: 02             LD      (BC),A          
5723: 05             DEC     B               
5724: 66             LD      H,(HL)          
5725: B1             OR      C               
5726: 17             RLA                     
5727: 16 59          LD      D,$59           
5729: 17             RLA                     
572A: 34             INC     (HL)            
572B: 82             ADD     A,D             
572C: 00             NOP                     
572D: A0             AND     B               
572E: 03             INC     BC              
572F: 01 9D 07       LD      BC,$079D        
5732: 24             INC     H               
5733: 0D             DEC     C               
5734: 22 0A 15       LD      ($150A),HL      
5737: 04             INC     B               
5738: 1E A7          LD      E,$A7           
573A: B7             OR      A               
573B: 4B             LD      C,E             
573C: 94             SUB     H               
573D: 15             DEC     D               
573E: B2             OR      D               
573F: DE 88          SBC     $88             
5741: BF             CP      A               
5742: 14             INC     D               
5743: 11 BC 2F       LD      DE,$2FBC        
5746: F7             RST     0X30            
5747: 87             ADD     A,A             
5748: 15             DEC     D               
5749: 91             SUB     C               
574A: 8D             ADC     A,L             
574B: A7             AND     A               
574C: 15             DEC     D               
574D: 7F             LD      A,A             
574E: 93             SUB     E               
574F: 99             SBC     C               
5750: 16 28          LD      D,$28           
5752: 15             DEC     D               
5753: 65             LD      H,L             
5754: 66             LD      H,(HL)          
5755: 83             ADD     A,E             
5756: BB             CP      E               
5757: 02             LD      (BC),A          
5758: 06 8F          LD      B,$8F           
575A: 4E             LD      C,(HL)          
575B: 52             LD      D,D             
575C: 5E             LD      E,(HL)          
575D: 46             LD      B,(HL)          
575E: 7A             LD      A,D             
575F: 18 2C          JR      $578D           
5761: 81             ADD     A,C             
5762: 00             NOP                     
5763: A0             AND     B               
5764: 03             INC     BC              
5765: 1D             DEC     E               
5766: 04             INC     B               
5767: 1B             DEC     DE              
5768: 5F             LD      E,A             
5769: BE             CP      (HL)            
576A: 5B             LD      E,E             
576B: B1             OR      C               
576C: 4B             LD      C,E             
576D: 7B             LD      A,E             
576E: 4E             LD      C,(HL)          
576F: 45             LD      B,L             
5770: 11 A0 9B       LD      DE,$9BA0        
5773: 15             DEC     D               
5774: 46             LD      B,(HL)          
5775: 98             SBC     B               
5776: 59             LD      E,C             
5777: 5E             LD      E,(HL)          
5778: 8E             ADC     A,(HL)          
5779: 7A             LD      A,D             
577A: 6B             LD      L,E             
577B: A1             AND     C               
577C: 81             ADD     A,C             
577D: 74             LD      (HL),H          
577E: CA 83 2F       JP      Z,$2F83         
5781: 62             LD      H,D             
5782: 2E 02          LD      L,$02           
5784: 08             EX      AF,AF'          
5785: 50             LD      D,B             
5786: D1             POP     DE              
5787: 89             ADC     A,C             
5788: 5B             LD      E,E             
5789: A9             XOR     C               
578A: 15             DEC     D               
578B: 8B             ADC     A,E             
578C: 9F             SBC     A               
578D: 19             ADD     HL,DE           
578E: 80             ADD     A,B             
578F: 9C             SBC     H               
5790: 82             ADD     A,D             
5791: 00             NOP                     
5792: 83             ADD     A,E             
5793: 03             INC     BC              
5794: 2A 04 28       LD      HL,($2804)      
5797: 03             INC     BC              
5798: A0             AND     B               
5799: 0F             RRCA                    
579A: A0             AND     B               
579B: F3             DI                      
579C: 17             RLA                     
579D: F3             DI                      
579E: 8C             ADC     A,H             
579F: 4B             LD      C,E             
57A0: 7B             LD      A,E             
57A1: 45             LD      B,L             
57A2: 45             LD      B,L             
57A3: B3             OR      E               
57A4: 46             LD      B,(HL)          
57A5: 76             HALT                    
57A6: 98             SBC     B               
57A7: 56             LD      D,(HL)          
57A8: F4 DB 72       CALL    P,$72DB         
57AB: 04             INC     B               
57AC: 53             LD      D,E             
57AD: 8F             ADC     A,A             
57AE: 7A             LD      A,D             
57AF: 0A             LD      A,(BC)          
57B0: BC             CP      H               
57B1: 4B             LD      C,E             
57B2: 49             LD      C,C             
57B3: 56             LD      D,(HL)          
57B4: 45             LD      B,L             
57B5: A3             AND     E               
57B6: 7A             LD      A,D             
57B7: A9             XOR     C               
57B8: 15             DEC     D               
57B9: DB 8B          IN      A,($8B)         
57BB: 83             ADD     A,E             
57BC: 7A             LD      A,D             
57BD: 97             SUB     A               
57BE: 7B             LD      A,E             
57BF: 07             RLCA                    
57C0: 64             LD      H,H             
57C1: 0E 62          LD      C,$62           
57C3: 0D             DEC     C               
57C4: 23             INC     HL              
57C5: 0E 06          LD      C,$06           
57C7: 0A             LD      A,(BC)          
57C8: 42             LD      B,D             
57C9: 0A             LD      A,(BC)          
57CA: 3A 0A 11       LD      A,($110A)       
57CD: 04             INC     B               
57CE: 19             ADD     HL,DE           
57CF: C7             RST     0X00            
57D0: DE D3          SBC     $D3             
57D2: 14             INC     D               
57D3: E6 96          AND     $96             
57D5: 57             LD      D,A             
57D6: 17             RLA                     
57D7: 5B             LD      E,E             
57D8: 61             LD      H,C             
57D9: 6B             LD      L,E             
57DA: BF             CP      A               
57DB: 96             SUB     (HL)            
57DC: C5             PUSH    BC              
57DD: 5D             LD      E,L             
57DE: 9E             SBC     (HL)            
57DF: 82             ADD     A,D             
57E0: 17             RLA                     
57E1: 45             LD      B,L             
57E2: 5E             LD      E,(HL)          
57E3: B3             OR      E               
57E4: 46             LD      B,(HL)          
57E5: 76             HALT                    
57E6: 98             SBC     B               
57E7: 2E 0D          LD      L,$0D           
57E9: 3B             DEC     SP              
57EA: 0E 04          LD      C,$04           
57EC: 0A             LD      A,(BC)          
57ED: 10 0A          DJNZ    $57F9           
57EF: 0B             DEC     BC              
57F0: 03             INC     BC              
57F1: 82             ADD     A,D             
57F2: 3B             DEC     SP              
57F3: 04             INC     B               
57F4: 30 0C          JR      NC,$5802        
57F6: BA             CP      D               
57F7: D0             RET     NC              
57F8: 47             LD      B,A             
57F9: 91             SUB     C               
57FA: 7A             LD      A,D             
57FB: 89             ADC     A,C             
57FC: 17             RLA                     
57FD: 57             LD      D,A             
57FE: 17             RLA                     
57FF: 56             LD      D,(HL)          
5800: 5E             LD      E,(HL)          
5801: F9             LD      SP,HL           
5802: 74             LD      (HL),H          
5803: 7A             LD      A,D             
5804: C4 82 17       CALL    NZ,$1782        
5807: 56             LD      D,(HL)          
5808: 5E             LD      E,(HL)          
5809: A3             AND     E               
580A: 7A             LD      A,D             
580B: A9             XOR     C               
580C: 15             DEC     D               
580D: FE 8B          CP      $8B             
580F: 51             LD      D,C             
5810: 18 45          JR      $5857           
5812: C2 83 48       JP      NZ,$4883        
5815: F5             PUSH    AF              
5816: 81             ADD     A,C             
5817: 0F             RRCA                    
5818: BC             CP      H               
5819: 17             RLA                     
581A: 48             LD      C,B             
581B: C7             RST     0X00            
581C: 16 03          LD      D,$03           
581E: BC             CP      H               
581F: 2F             CPL                     
5820: 17             RLA                     
5821: 0D             DEC     C               
5822: 58             LD      E,B             
5823: 5F             LD      E,A             
5824: 63             LD      H,E             
5825: 02             LD      (BC),A          
5826: 05             DEC     B               
5827: 04             INC     B               
5828: 53             LD      D,E             
5829: 8F             ADC     A,A             
582A: 7A             LD      A,D             
582B: 54             LD      D,H             
582C: 1A             LD      A,(DE)          
582D: 80             ADD     A,B             
582E: C9             RET                     
582F: 92             SUB     D               
5830: 00             NOP                     
5831: 8A             ADC     A,D             
5832: 03             INC     BC              
5833: 2E 04          LD      L,$04           
5835: 2C             INC     L               
5836: 83             ADD     A,E             
5837: 7A             LD      A,D             
5838: 5F             LD      E,A             
5839: BE             CP      (HL)            
583A: 99             SBC     C               
583B: 16 C2          LD      D,$C2           
583D: B3             OR      E               
583E: 95             SUB     L               
583F: 5F             LD      E,A             
5840: 05             DEC     B               
5841: BC             CP      H               
5842: B8             CP      B               
5843: A0             AND     B               
5844: 23             INC     HL              
5845: 62             LD      H,D             
5846: C3 9E 5F       JP      $5F9E           
5849: BE             CP      (HL)            
584A: 39             ADD     HL,SP           
584B: 17             RLA                     
584C: DB 9F          IN      A,($9F)         
584E: 5F             LD      E,A             
584F: BE             CP      (HL)            
5850: 5B             LD      E,E             
5851: B1             OR      C               
5852: 4B             LD      C,E             
5853: 7B             LD      A,E             
5854: 4E             LD      C,(HL)          
5855: 45             LD      B,L             
5856: 31 49 54       LD      SP,$5449        
5859: 5E             LD      E,(HL)          
585A: 5C             LD      E,H             
585B: 60             LD      H,B             
585C: 77             LD      (HL),A          
585D: 79             LD      A,C             
585E: D6 B0          SUB     $B0             
5860: A3             AND     E               
5861: A0             AND     B               
5862: 06 3D          LD      B,$3D           
5864: 0D             DEC     C               
5865: 3B             DEC     SP              
5866: 0A             LD      A,(BC)          
5867: 0F             RRCA                    
5868: 1B             DEC     DE              
5869: 0D             DEC     C               
586A: 0C             INC     C               
586B: 15             DEC     D               
586C: 02             LD      (BC),A          
586D: A9             XOR     C               
586E: 04             INC     B               
586F: 07             RLCA                    
5870: 4B             LD      C,E             
5871: 7B             LD      A,E             
5872: C9             RET                     
5873: 54             LD      D,H             
5874: A6             AND     (HL)            
5875: B7             OR      A               
5876: 2E A8          LD      L,$A8           
5878: 04             INC     B               
5879: 08             EX      AF,AF'          
587A: CE 65          ADC     $65             
587C: 0B             DEC     BC              
587D: 8E             ADC     A,(HL)          
587E: 36 A1          LD      (HL),$A1        
5880: B8             CP      B               
5881: 16 A9          LD      D,$A9           
5883: 04             INC     B               
5884: 1A             LD      A,(DE)          
5885: 1E A0          LD      E,$A0           
5887: D6 9C          SUB     $9C             
5889: DB 72          IN      A,($72)         
588B: 89             ADC     A,C             
588C: 67             LD      H,A             
588D: A3             AND     E               
588E: A0             AND     B               
588F: 68             LD      L,B             
5890: 4D             LD      C,L             
5891: AF             XOR     A               
5892: A0             AND     B               
5893: C7             RST     0X00            
5894: DE D3          SBC     $D3             
5896: 14             INC     D               
5897: 85             ADD     A,L             
5898: 96             SUB     (HL)            
5899: 85             ADD     A,L             
589A: 8D             ADC     A,L             
589B: 4B             LD      C,E             
589C: 5E             LD      E,(HL)          
589D: 9B             SBC     E               
589E: C1             POP     BC              
589F: 1A             LD      A,(DE)          
58A0: 10 07          DJNZ    $58A9           
58A2: 4B             LD      C,E             
58A3: 0D             DEC     C               
58A4: 49             LD      C,C             
58A5: 0A             LD      A,(BC)          
58A6: 11 1A 15       LD      DE,$151A        
58A9: 02             LD      (BC),A          
58AA: 03             INC     BC              
58AB: 18 42          JR      $58EF           
58AD: 29             ADD     HL,HL           
58AE: 17             RLA                     
58AF: 19             ADD     HL,DE           
58B0: 92             SUB     D               
58B1: 17             RLA                     
58B2: 42             LD      B,D             
58B3: 00             NOP                     
58B4: 04             INC     B               
58B5: 38 1F          JR      C,$58D6         
58B7: D1             POP     DE              
58B8: 9B             SBC     E               
58B9: 96             SUB     (HL)            
58BA: 1B             DEC     DE              
58BB: A1             AND     C               
58BC: 5F             LD      E,A             
58BD: A0             AND     B               
58BE: 96             SUB     (HL)            
58BF: 96             SUB     (HL)            
58C0: DB 72          IN      A,($72)         
58C2: 68             LD      L,B             
58C3: B1             OR      C               
58C4: 09             ADD     HL,BC           
58C5: B2             OR      D               
58C6: 2B             DEC     HL              
58C7: 62             LD      H,D             
58C8: 84             ADD     A,H             
58C9: BF             CP      A               
58CA: 15             DEC     D               
58CB: EE E7          XOR     $E7             
58CD: 9F             SBC     A               
58CE: 9B             SBC     E               
58CF: 15             DEC     D               
58D0: BF             CP      A               
58D1: 91             SUB     C               
58D2: B7             OR      A               
58D3: B1             OR      C               
58D4: 8F             ADC     A,A             
58D5: AF             XOR     A               
58D6: 96             SUB     (HL)            
58D7: 5F             LD      E,A             
58D8: 4B             LD      C,E             
58D9: 15             DEC     D               
58DA: 0D             DEC     C               
58DB: 8D             ADC     A,L             
58DC: C7             RST     0X00            
58DD: 16 11          LD      D,$11           
58DF: BC             CP      H               
58E0: 8B             ADC     A,E             
58E1: 64             LD      H,H             
58E2: 11 BC C9       LD      DE,$C9BC        
58E5: 9A             SBC     D               
58E6: 82             ADD     A,D             
58E7: 17             RLA                     
58E8: 48             LD      C,B             
58E9: 5E             LD      E,(HL)          
58EA: 81             ADD     A,C             
58EB: 8D             ADC     A,L             
58EC: 1B             DEC     DE              
58ED: B5             OR      L               
58EE: 02             LD      (BC),A          
58EF: 08             EX      AF,AF'          
58F0: 68             LD      L,B             
58F1: B1             OR      C               
58F2: 09             ADD     HL,BC           
58F3: B2             OR      D               
58F4: 2B             DEC     HL              
58F5: 62             LD      H,D             
58F6: 84             ADD     A,H             
58F7: BF             CP      A               
58F8: 1B             DEC     DE              
58F9: 6E             LD      L,(HL)          
58FA: 00             NOP                     
58FB: 00             NOP                     
58FC: A0             AND     B               
58FD: 03             INC     BC              
58FE: 19             ADD     HL,DE           
58FF: 04             INC     B               
5900: 17             RLA                     
5901: 5F             LD      E,A             
5902: BE             CP      (HL)            
5903: 5B             LD      E,E             
5904: B1             OR      C               
5905: 4B             LD      C,E             
5906: 7B             LD      A,E             
5907: 3F             CCF                     
5908: B9             CP      C               
5909: 4A             LD      C,D             
590A: 5E             LD      E,(HL)          
590B: 64             LD      H,H             
590C: 48             LD      C,B             
590D: 31 C6 23       LD      SP,$23C6        
5910: 62             LD      H,D             
5911: 23             INC     HL              
5912: 92             SUB     D               
5913: 0A             LD      A,(BC)          
5914: BC             CP      H               
5915: 2F             CPL                     
5916: 62             LD      H,D             
5917: 2E 06          LD      L,$06           
5919: 16 0D          LD      D,$0D           
591B: 14             INC     D               
591C: 0A             LD      A,(BC)          
591D: 0F             RRCA                    
591E: 0E 10          LD      C,$10           
5920: 0D             DEC     C               
5921: 06 08          LD      B,$08           
5923: 15             DEC     D               
5924: 17             RLA                     
5925: 15             DEC     D               
5926: 19             ADD     HL,DE           
5927: A0             AND     B               
5928: 0D             DEC     C               
5929: 06 08          LD      B,$08           
592B: 39             ADD     HL,SP           
592C: 17             RLA                     
592D: 39             ADD     HL,SP           
592E: 19             ADD     HL,DE           
592F: A0             AND     B               
5930: 07             RLCA                    
5931: 2A 0D 28       LD      HL,($280D)      
5934: 0A             LD      A,(BC)          
5935: 15             DEC     D               
5936: 04             INC     B               
5937: 21 F4 4F       LD      HL,$4FF4        
593A: AB             XOR     E               
593B: A2             AND     D               
593C: AB             XOR     E               
593D: AD             XOR     L               
593E: DB BD          IN      A,($BD)         
5940: 41             LD      B,C             
5941: 6E             LD      L,(HL)          
5942: 73             LD      (HL),E          
5943: 5D             LD      E,L             
5944: F6 4F          OR      $4F             
5946: 7B             LD      A,E             
5947: 14             INC     D               
5948: 96             SUB     (HL)            
5949: 8C             ADC     A,H             
594A: FF             RST     0X38            
594B: BE             CP      (HL)            
594C: 2B             DEC     HL              
594D: 17             RLA                     
594E: 5B             LD      E,E             
594F: B1             OR      C               
5950: 04             INC     B               
5951: 68             LD      L,B             
5952: 7B             LD      A,E             
5953: 16 7B          LD      D,$7B           
5955: 17             RLA                     
5956: FF             RST     0X38            
5957: B9             CP      C               
5958: 2E 17          LD      L,$17           
595A: 19             ADD     HL,DE           
595B: 00             NOP                     
595C: 02             LD      (BC),A          
595D: 0A             LD      A,(BC)          
595E: 4F             LD      C,A             
595F: 72             LD      (HL),D          
5960: F4 4F B4       CALL    P,$B44F         
5963: 6C             LD      L,H             
5964: 67             LD      H,A             
5965: 16 73          LD      D,$73           
5967: 49             LD      C,C             
5968: 08             EX      AF,AF'          
5969: 81             ADD     A,C             
596A: 03             INC     BC              
596B: 93             SUB     E               
596C: 00             NOP                     
596D: 90             SUB     B               
596E: 03             INC     BC              
596F: 33             INC     SP              
5970: 04             INC     B               
5971: 31 58 45       LD      SP,$4558        
5974: DB 78          IN      A,($78)         
5976: 35             DEC     (HL)            
5977: A1             AND     C               
5978: 87             ADD     A,A             
5979: 15             DEC     D               
597A: 2E 49          LD      L,$49           
597C: 09             ADD     HL,BC           
597D: 15             DEC     D               
597E: CB 6A          BIT     5,D             
5980: C5             PUSH    BC              
5981: B5             OR      L               
5982: 4B             LD      C,E             
5983: 72             LD      (HL),D          
5984: 66             LD      H,(HL)          
5985: 98             SBC     B               
5986: 89             ADC     A,C             
5987: 17             RLA                     
5988: 82             ADD     A,D             
5989: 17             RLA                     
598A: 55             LD      D,L             
598B: 5E             LD      E,(HL)          
598C: 36 A1          LD      (HL),$A1        
598E: 19             ADD     HL,DE           
598F: 71             LD      (HL),C          
5990: 46             LD      B,(HL)          
5991: 48             LD      C,B             
5992: B6             OR      (HL)            
5993: 14             INC     D               
5994: 5D             LD      E,L             
5995: 9E             SBC     (HL)            
5996: 91             SUB     C               
5997: 7A             LD      A,D             
5998: 82             ADD     A,D             
5999: 17             RLA                     
599A: 55             LD      D,L             
599B: 5E             LD      E,(HL)          
599C: 36 A1          LD      (HL),$A1        
599E: 07             RLCA                    
599F: 71             LD      (HL),C          
59A0: 96             SUB     (HL)            
59A1: D7             RST     0X10            
59A2: 2E 07          LD      L,$07           
59A4: 01 A1 06       LD      BC,$06A1        
59A7: 01 A1 0A       LD      BC,$0AA1        
59AA: 1C             INC     E               
59AB: 0D             DEC     C               
59AC: 1A             LD      A,(DE)          
59AD: 1F             RRA                     
59AE: 15             DEC     D               
59AF: C7             RST     0X00            
59B0: DE 4F          SBC     $4F             
59B2: 24             INC     H               
59B3: 63             LD      H,E             
59B4: 16 C9          LD      D,$C9           
59B6: 97             SUB     A               
59B7: F3             DI                      
59B8: 5F             LD      E,A             
59B9: 6B             LD      L,E             
59BA: BF             CP      A               
59BB: 4E             LD      C,(HL)          
59BC: 86             ADD     A,(HL)          
59BD: 16 8A          LD      D,$8A           
59BF: DB 72          IN      A,($72)         
59C1: 79             LD      A,C             
59C2: 5B             LD      E,E             
59C3: 2E 1E          LD      L,$1E           
59C5: 1A             LD      A,(DE)          
59C6: 3C             INC     A               
59C7: 08             EX      AF,AF'          
59C8: 80             ADD     A,B             
59C9: 94             SUB     H               
59CA: 0E 80          LD      C,$80           
59CC: 91             SUB     C               
59CD: 0D             DEC     C               
59CE: 7D             LD      A,L             
59CF: 0A             LD      A,(BC)          
59D0: 09             ADD     HL,BC           
59D1: 1C             INC     E               
59D2: 13             INC     DE              
59D3: 0B             DEC     BC              
59D4: 77             LD      (HL),A          
59D5: 05             DEC     B               
59D6: 55             LD      D,L             
59D7: 22 0D 20       LD      ($200D),HL      
59DA: 1F             RRA                     
59DB: 1C             INC     E               
59DC: 5F             LD      E,A             
59DD: BE             CP      (HL)            
59DE: 09             ADD     HL,BC           
59DF: 15             DEC     D               
59E0: D6 6A          SUB     $6A             
59E2: 94             SUB     H               
59E3: 5F             LD      E,A             
59E4: C3 B5 1B       JP      $1BB5           
59E7: BC             CP      H               
59E8: 34             INC     (HL)            
59E9: A1             AND     C               
59EA: 3F             CCF                     
59EB: 16 C3          LD      D,$C3           
59ED: 6A             LD      L,D             
59EE: 33             INC     SP              
59EF: 98             SBC     B               
59F0: EB             EX      DE,HL           
59F1: 5B             LD      E,E             
59F2: CB D2          SET     2,D             
59F4: 89             ADC     A,C             
59F5: 4E             LD      C,(HL)          
59F6: 71             LD      (HL),C          
59F7: 9E             SBC     (HL)            
59F8: 1D             DEC     E               
59F9: 06 AF          LD      B,$AF           
59FB: 26 0D          LD      H,$0D           
59FD: 24             INC     H               
59FE: 1F             RRA                     
59FF: 20 5F          JR      NZ,$5A60        
5A01: BE             CP      (HL)            
5A02: 09             ADD     HL,BC           
5A03: 15             DEC     D               
5A04: C4 6A 7F       CALL    NZ,$7F6A        
5A07: 7B             LD      A,E             
5A08: DB B5          IN      A,($B5)         
5A0A: 34             INC     (HL)            
5A0B: A1             AND     C               
5A0C: 94             SUB     H               
5A0D: 14             INC     D               
5A0E: 43             LD      B,E             
5A0F: 90             SUB     B               
5A10: 33             INC     SP              
5A11: 98             SBC     B               
5A12: C7             RST     0X00            
5A13: DE E4          SBC     $E4             
5A15: 14             INC     D               
5A16: 91             SUB     C               
5A17: 7A             LD      A,D             
5A18: 59             LD      E,C             
5A19: 5E             LD      E,(HL)          
5A1A: 82             ADD     A,D             
5A1B: 7B             LD      A,E             
5A1C: DB 16          IN      A,($16)         
5A1E: 81             ADD     A,C             
5A1F: 7A             LD      A,D             
5A20: 1D             DEC     E               
5A21: 07             RLCA                    
5A22: FF             RST     0X38            
5A23: 28 1F          JR      Z,$5A44         
5A25: 26 5F          LD      H,$5F           
5A27: BE             CP      (HL)            
5A28: 09             ADD     HL,BC           
5A29: 15             DEC     D               
5A2A: CE 6A          ADC     $6A             
5A2C: 91             SUB     C               
5A2D: C5             PUSH    BC              
5A2E: 4B             LD      C,E             
5A2F: 62             LD      H,D             
5A30: 04             INC     B               
5A31: 68             LD      L,B             
5A32: 51             LD      D,C             
5A33: 18 23          JR      $5A58           
5A35: C6 65          ADD     $65             
5A37: 98             SBC     B               
5A38: 33             INC     SP              
5A39: 89             ADC     A,C             
5A3A: F6 4F          OR      $4F             
5A3C: 51             LD      D,C             
5A3D: 18 52          JR      $5A91           
5A3F: C2 46 C5       JP      NZ,$C546        
5A42: AB             XOR     E               
5A43: 14             INC     D               
5A44: 8B             ADC     A,E             
5A45: 54             LD      D,H             
5A46: 83             ADD     A,E             
5A47: 7A             LD      A,D             
5A48: 8F             ADC     A,A             
5A49: BE             CP      (HL)            
5A4A: EB             EX      DE,HL           
5A4B: 5D             LD      E,L             
5A4C: 1F             RRA                     
5A4D: 10 41          DJNZ    $5A90           
5A4F: 1E C3          LD      E,$C3           
5A51: 9E             SBC     (HL)            
5A52: B9             CP      C               
5A53: 6E             LD      L,(HL)          
5A54: B3             OR      E               
5A55: D1             POP     DE              
5A56: 41             LD      B,C             
5A57: D2 99 64       JP      NC,$6499        
5A5A: 38 A0          JR      C,$59FC         
5A5C: E3             EX      (SP),HL         
5A5D: 06 09          LD      B,$09           
5A5F: 02             LD      (BC),A          
5A60: 46             LD      B,(HL)          
5A61: 46             LD      B,(HL)          
5A62: 02             LD      (BC),A          
5A63: 0A             LD      A,(BC)          
5A64: 5F             LD      E,A             
5A65: BE             CP      (HL)            
5A66: D3 17          OUT     ($17),A         
5A68: 51             LD      D,C             
5A69: 54             LD      D,H             
5A6A: 4B             LD      C,E             
5A6B: C6 79          ADD     $79             
5A6D: 5B             LD      E,E             
5A6E: 16 24          LD      D,$24           
5A70: 8E             ADC     A,(HL)          
5A71: 00             NOP                     
5A72: A0             AND     B               
5A73: 03             INC     BC              
5A74: 14             INC     D               
5A75: 04             INC     B               
5A76: 12             LD      (DE),A          
5A77: 5F             LD      E,A             
5A78: BE             CP      (HL)            
5A79: 5B             LD      E,E             
5A7A: B1             OR      C               
5A7B: 4B             LD      C,E             
5A7C: 7B             LD      A,E             
5A7D: 49             LD      C,C             
5A7E: 45             LD      B,L             
5A7F: 67             LD      H,A             
5A80: B1             OR      C               
5A81: 8D             ADC     A,L             
5A82: 96             SUB     (HL)            
5A83: 3B             DEC     SP              
5A84: 63             LD      H,E             
5A85: F4 72 DB       CALL    P,$DB72         
5A88: 63             LD      H,E             
5A89: 01 01 14       LD      BC,$1401        
5A8C: 02             LD      (BC),A          
5A8D: 06 AF          LD      B,$AF           
5A8F: 6E             LD      L,(HL)          
5A90: 83             ADD     A,E             
5A91: 61             LD      H,C             
5A92: BB             CP      E               
5A93: 85             ADD     A,L             
5A94: 03             INC     BC              
5A95: 81             ADD     A,C             
5A96: 60             LD      H,B             
5A97: 00             NOP                     
5A98: 00             NOP                     
5A99: 90             SUB     B               
5A9A: 03             INC     BC              
5A9B: 18 04          JR      $5AA1           
5A9D: 16 DB          LD      D,$DB           
5A9F: B0             OR      B               
5AA0: 57             LD      D,A             
5AA1: 17             RLA                     
5AA2: 75             LD      (HL),L          
5AA3: 61             LD      H,C             
5AA4: 89             ADC     A,C             
5AA5: 17             RLA                     
5AA6: AF             XOR     A               
5AA7: 14             INC     D               
5AA8: 3B             DEC     SP              
5AA9: 15             DEC     D               
5AAA: D0             RET     NC              
5AAB: 60             LD      H,B             
5AAC: D6 6A          SUB     $6A             
5AAE: DB 72          IN      A,($72)         
5AB0: 0E D0          LD      C,$D0           
5AB2: 2F             CPL                     
5AB3: 8E             ADC     A,(HL)          
5AB4: 09             ADD     HL,BC           
5AB5: 02             LD      (BC),A          
5AB6: 46             LD      B,(HL)          
5AB7: 46             LD      B,(HL)          
5AB8: 0B             DEC     BC              
5AB9: 81             ADD     A,C             
5ABA: 2D             DEC     L               
5ABB: 0E 81          LD      C,$81           
5ABD: 2A 0D 80       LD      HL,($800D)      
5AC0: DF             RST     0X18            
5AC1: 0E 0A          LD      C,$0A           
5AC3: 0A             LD      A,(BC)          
5AC4: 01 0A 02       LD      BC,$020A        
5AC7: 0A             LD      A,(BC)          
5AC8: 03             INC     BC              
5AC9: 0A             LD      A,(BC)          
5ACA: 04             INC     B               
5ACB: 0A             LD      A,(BC)          
5ACC: 0A             LD      A,(BC)          
5ACD: 1F             RRA                     
5ACE: 0F             RRCA                    
5ACF: DB B0          IN      A,($B0)         
5AD1: 2F             CPL                     
5AD2: 17             RLA                     
5AD3: 84             ADD     A,H             
5AD4: A6             AND     (HL)            
5AD5: 0B             DEC     BC              
5AD6: C0             RET     NZ              
5AD7: DB 72          IN      A,($72)         
5AD9: 10 53          DJNZ    $5B2E           
5ADB: 57             LD      D,A             
5ADC: 17             RLA                     
5ADD: 45             LD      B,L             
5ADE: 1C             INC     E               
5ADF: 38 10          JR      C,$5AF1         
5AE1: 2C             INC     L               
5AE2: 38 0E          JR      C,$5AF2         
5AE4: 80             ADD     A,B             
5AE5: B8             CP      B               
5AE6: 0D             DEC     C               
5AE7: 33             INC     SP              
5AE8: 01 3D 1F       LD      BC,$1F3D        
5AEB: 2E 55          LD      L,$55           
5AED: 45             LD      B,L             
5AEE: E4 5F 73       CALL    PO,$735F        
5AF1: 62             LD      H,D             
5AF2: 81             ADD     A,C             
5AF3: 5B             LD      E,E             
5AF4: 8A             ADC     A,D             
5AF5: AF             XOR     A               
5AF6: 2F             CPL                     
5AF7: 62             LD      H,D             
5AF8: 19             ADD     HL,DE           
5AF9: EE 85          XOR     $85             
5AFB: 73             LD      (HL),E          
5AFC: 0F             RRCA                    
5AFD: 71             LD      (HL),C          
5AFE: 3B             DEC     SP              
5AFF: 4A             LD      C,D             
5B00: E3             EX      (SP),HL         
5B01: 8B             ADC     A,E             
5B02: 16 58          LD      D,$58           
5B04: C7             RST     0X00            
5B05: 9C             SBC     H               
5B06: 53             LD      D,E             
5B07: B7             OR      A               
5B08: FF             RST     0X38            
5B09: A4             AND     H               
5B0A: AF             XOR     A               
5B0B: 14             INC     D               
5B0C: 46             LD      B,(HL)          
5B0D: B8             CP      B               
5B0E: 4B             LD      C,E             
5B0F: 62             LD      H,D             
5B10: 5B             LD      E,E             
5B11: BE             CP      (HL)            
5B12: 73             LD      (HL),E          
5B13: C1             POP     BC              
5B14: 5F             LD      E,A             
5B15: BE             CP      (HL)            
5B16: 5B             LD      E,E             
5B17: B1             OR      C               
5B18: 4B             LD      C,E             
5B19: 7B             LD      A,E             
5B1A: 0C             INC     C               
5B1B: 0D             DEC     C               
5B1C: 3D             DEC     A               
5B1D: 03             INC     BC              
5B1E: 00             NOP                     
5B1F: 22 03 88       LD      ($8803),HL      
5B22: 1C             INC     E               
5B23: 1F             RRA                     
5B24: 34             INC     (HL)            
5B25: 5B             LD      E,E             
5B26: BE             CP      (HL)            
5B27: 04             INC     B               
5B28: BC             CP      H               
5B29: 51             LD      D,C             
5B2A: 63             LD      H,E             
5B2B: 33             INC     SP              
5B2C: 98             SBC     B               
5B2D: 5F             LD      E,A             
5B2E: BE             CP      (HL)            
5B2F: 99             SBC     C               
5B30: 16 C2          LD      D,$C2           
5B32: B3             OR      E               
5B33: F3             DI                      
5B34: 17             RLA                     
5B35: F3             DI                      
5B36: 8C             ADC     A,H             
5B37: 4B             LD      C,E             
5B38: 7B             LD      A,E             
5B39: 52             LD      D,D             
5B3A: 45             LD      B,L             
5B3B: E5             PUSH    HL              
5B3C: A0             AND     B               
5B3D: B6             OR      (HL)            
5B3E: 78             LD      A,B             
5B3F: 47             LD      B,A             
5B40: 5E             LD      E,(HL)          
5B41: 53             LD      D,E             
5B42: B7             OR      A               
5B43: DB A4          IN      A,($A4)         
5B45: 07             RLCA                    
5B46: B3             OR      E               
5B47: FF             RST     0X38            
5B48: BD             CP      L               
5B49: AF             XOR     A               
5B4A: 14             INC     D               
5B4B: 46             LD      B,(HL)          
5B4C: B8             CP      B               
5B4D: 4B             LD      C,E             
5B4E: 62             LD      H,D             
5B4F: 5B             LD      E,E             
5B50: BE             CP      (HL)            
5B51: 73             LD      (HL),E          
5B52: C1             POP     BC              
5B53: 5F             LD      E,A             
5B54: BE             CP      (HL)            
5B55: 5B             LD      E,E             
5B56: B1             OR      C               
5B57: 4B             LD      C,E             
5B58: 7B             LD      A,E             
5B59: 0C             INC     C               
5B5A: 0D             DEC     C               
5B5B: 06 0A          LD      B,$0A           
5B5D: 03             INC     BC              
5B5E: 21 03 00       LD      HL,$0003        
5B61: 00             NOP                     
5B62: 0D             DEC     C               
5B63: 06 0A          LD      B,$0A           
5B65: 04             INC     B               
5B66: 21 04 00       LD      HL,$0004        
5B69: 00             NOP                     
5B6A: 0D             DEC     C               
5B6B: 06 0A          LD      B,$0A           
5B6D: 01 21 01       LD      BC,$0121        
5B70: 00             NOP                     
5B71: 00             NOP                     
5B72: 0D             DEC     C               
5B73: 06 0A          LD      B,$0A           
5B75: 02             LD      (BC),A          
5B76: 21 02 00       LD      HL,$0002        
5B79: 00             NOP                     
5B7A: 1F             RRA                     
5B7B: 22 06 9A       LD      ($9A06),HL      
5B7E: 90             SUB     B               
5B7F: 73             LD      (HL),E          
5B80: 5B             LD      E,E             
5B81: 70             LD      (HL),B          
5B82: B7             OR      A               
5B83: 1C             INC     E               
5B84: F3             DI                      
5B85: B9             CP      C               
5B86: 5B             LD      E,E             
5B87: 4D             LD      C,L             
5B88: 3F             CCF                     
5B89: B9             CP      C               
5B8A: 4E             LD      C,(HL)          
5B8B: 5E             LD      E,(HL)          
5B8C: 86             ADD     A,(HL)          
5B8D: 5F             LD      E,A             
5B8E: C3 EA 66       JP      $66EA           
5B91: 98             SBC     B               
5B92: F3             DI                      
5B93: 17             RLA                     
5B94: 0D             DEC     C               
5B95: 8D             ADC     A,L             
5B96: E3             EX      (SP),HL         
5B97: 06 DB          LD      B,$DB           
5B99: 72             LD      (HL),D          
5B9A: 1B             DEC     DE              
5B9B: B7             OR      A               
5B9C: 5B             LD      E,E             
5B9D: BB             CP      E               
5B9E: 2C             INC     L               
5B9F: 1C             INC     E               
5BA0: 0D             DEC     C               
5BA1: 45             LD      B,L             
5BA2: 0E 06          LD      C,$06           
5BA4: 0A             LD      A,(BC)          
5BA5: 11 0A 42       LD      DE,$420A        
5BA8: 0A             LD      A,(BC)          
5BA9: 09             ADD     HL,BC           
5BAA: 1F             RRA                     
5BAB: 3B             DEC     SP              
5BAC: DB B0          IN      A,($B0)         
5BAE: 63             LD      H,E             
5BAF: 16 B5          LD      D,$B5           
5BB1: 85             ADD     A,L             
5BB2: 7B             LD      A,E             
5BB3: 14             INC     D               
5BB4: 67             LD      H,A             
5BB5: 66             LD      H,(HL)          
5BB6: 7F             LD      A,A             
5BB7: 4E             LD      C,(HL)          
5BB8: 96             SUB     (HL)            
5BB9: 14             INC     D               
5BBA: EF             RST     0X28            
5BBB: BD             CP      L               
5BBC: 33             INC     SP              
5BBD: A7             AND     A               
5BBE: 8E             ADC     A,(HL)          
5BBF: 48             LD      C,B             
5BC0: 82             ADD     A,D             
5BC1: 17             RLA                     
5BC2: 83             ADD     A,E             
5BC3: 61             LD      H,C             
5BC4: EB             EX      DE,HL           
5BC5: 5B             LD      E,E             
5BC6: CB D2          SET     2,D             
5BC8: C5             PUSH    BC              
5BC9: 4C             LD      C,H             
5BCA: 5B             LD      E,E             
5BCB: 89             ADC     A,C             
5BCC: A1             AND     C               
5BCD: 1D             DEC     E               
5BCE: 83             ADD     A,E             
5BCF: B3             OR      E               
5BD0: 0B             DEC     BC              
5BD1: EE 4F          XOR     $4F             
5BD3: 24             INC     H               
5BD4: AF             XOR     A               
5BD5: 14             INC     D               
5BD6: 83             ADD     A,E             
5BD7: 61             LD      H,C             
5BD8: D6 B0          SUB     $B0             
5BDA: F4 72 90       CALL    P,$9072         
5BDD: 14             INC     D               
5BDE: 6B             LD      L,E             
5BDF: 61             LD      H,C             
5BE0: CE 51          ADC     $51             
5BE2: 7F             LD      A,A             
5BE3: 49             LD      C,C             
5BE4: F9             LD      SP,HL           
5BE5: 8E             ADC     A,(HL)          
5BE6: 22 9A 08       LD      ($089A),HL      
5BE9: 06 0D          LD      B,$0D           
5BEB: 04             INC     B               
5BEC: 9C             SBC     H               
5BED: 1C             INC     E               
5BEE: 1C             INC     E               
5BEF: 9E             SBC     (HL)            
5BF0: 07             RLCA                    
5BF1: 01 AB 02       LD      BC,$02AB        
5BF4: 02             LD      (BC),A          
5BF5: DB B0          IN      A,($B0)         
5BF7: 03             INC     BC              
5BF8: 80             ADD     A,B             
5BF9: AE             XOR     (HL)            
5BFA: 00             NOP                     
5BFB: 00             NOP                     
5BFC: 90             SUB     B               
5BFD: 03             INC     BC              
5BFE: 80             ADD     A,B             
5BFF: A8             XOR     B               
5C00: 0D             DEC     C               
5C01: 80             ADD     A,B             
5C02: A5             AND     L               
5C03: 04             INC     B               
5C04: 80             ADD     A,B             
5C05: 9F             SBC     A               
5C06: 4F             LD      C,A             
5C07: 45             LD      B,L             
5C08: 83             ADD     A,E             
5C09: 48             LD      C,B             
5C0A: 83             ADD     A,E             
5C0B: 7A             LD      A,D             
5C0C: 94             SUB     H               
5C0D: 5A             LD      E,D             
5C0E: FB             EI                      
5C0F: C0             RET     NZ              
5C10: 4F             LD      C,A             
5C11: A1             AND     C               
5C12: CE B0          ADC     $B0             
5C14: 0B             DEC     BC              
5C15: 8E             ADC     A,(HL)          
5C16: 8E             ADC     A,(HL)          
5C17: 48             LD      C,B             
5C18: F7             RST     0X30            
5C19: 17             RLA                     
5C1A: 33             INC     SP              
5C1B: 49             LD      C,C             
5C1C: AB             XOR     E               
5C1D: 98             SBC     B               
5C1E: 39             ADD     HL,SP           
5C1F: 6E             LD      L,(HL)          
5C20: BF             CP      A               
5C21: 6D             LD      L,L             
5C22: C3 B5 AC       JP      $ACB5           
5C25: A6             AND     (HL)            
5C26: 05             DEC     B               
5C27: 9E             SBC     (HL)            
5C28: F5             PUSH    AF              
5C29: 72             LD      (HL),D          
5C2A: 51             LD      D,C             
5C2B: 18 43          JR      $5C70           
5C2D: C2 33 98       JP      NZ,$9833        
5C30: 9E             SBC     (HL)            
5C31: 7A             LD      A,D             
5C32: F6 B2          OR      $B2             
5C34: D7             RST     0X10            
5C35: C3 CA B5       JP      $B5CA           
5C38: 75             LD      (HL),L          
5C39: 7A             LD      A,D             
5C3A: 40             LD      B,B             
5C3B: 61             LD      H,C             
5C3C: 3C             INC     A               
5C3D: F4 79 73       CALL    P,$7379         
5C40: 7B             LD      A,E             
5C41: 16 8B          LD      D,$8B           
5C43: 16 1B          LD      D,$1B           
5C45: 92             SUB     D               
5C46: 4B             LD      C,E             
5C47: 7B             LD      A,E             
5C48: EB             EX      DE,HL           
5C49: D8             RET     C               
5C4A: 4C             LD      C,H             
5C4B: DB 28          IN      A,($28)         
5C4D: 9F             SBC     A               
5C4E: 40             LD      B,B             
5C4F: B9             CP      C               
5C50: 04             INC     B               
5C51: EE 73          XOR     $73             
5C53: C6 C7          ADD     $C7             
5C55: DE D3          SBC     $D3             
5C57: 14             INC     D               
5C58: 85             ADD     A,L             
5C59: 96             SUB     (HL)            
5C5A: 46             LD      B,(HL)          
5C5B: 48             LD      C,B             
5C5C: 67             LD      H,A             
5C5D: 16 2B          LD      D,$2B           
5C5F: 17             RLA                     
5C60: DB E0          IN      A,($E0)         
5C62: 4A             LD      C,D             
5C63: 77             LD      (HL),A          
5C64: CF             RST     0X08            
5C65: 49             LD      C,C             
5C66: 2C             INC     L               
5C67: 18 3B          JR      $5CA4           
5C69: 4A             LD      C,D             
5C6A: 15             DEC     D               
5C6B: CB C0          SET     0,B             
5C6D: 7A             LD      A,D             
5C6E: 1B             DEC     DE              
5C6F: EE 1B          XOR     $1B             
5C71: A1             AND     C               
5C72: 19             ADD     HL,DE           
5C73: 87             ADD     A,A             
5C74: 5B             LD      E,E             
5C75: D4 1B B7       CALL    NC,$B71B        
5C78: 1B             DEC     DE              
5C79: EE 1B          XOR     $1B             
5C7B: A1             AND     C               
5C7C: 76             HALT                    
5C7D: 4D             LD      C,L             
5C7E: F4 BD 9B       CALL    P,$9BBD         
5C81: 15             DEC     D               
5C82: 5B             LD      E,E             
5C83: CA 5B BE       JP      Z,$BE5B         
5C86: 15             DEC     D               
5C87: BC             CP      H               
5C88: 86             ADD     A,(HL)          
5C89: A6             AND     (HL)            
5C8A: C0             RET     NZ              
5C8B: 16 51          LD      D,$51           
5C8D: 18 23          JR      $5CB2           
5C8F: C6 E8          ADD     $E8             
5C91: 8B             ADC     A,E             
5C92: 0E BC          LD      C,$BC           
5C94: 91             SUB     C               
5C95: C5             PUSH    BC              
5C96: DA 14 DD       JP      C,$DD14         
5C99: 5F             LD      E,A             
5C9A: F3             DI                      
5C9B: 5F             LD      E,A             
5C9C: 7B             LD      A,E             
5C9D: 50             LD      D,B             
5C9E: 46             LD      B,(HL)          
5C9F: 45             LD      B,L             
5CA0: 66             LD      H,(HL)          
5CA1: 9E             SBC     (HL)            
5CA2: A1             AND     C               
5CA3: A0             AND     B               
5CA4: 22 1E 1C       LD      ($1C1E),HL      
5CA7: 1D             DEC     E               
5CA8: 02             LD      (BC),A          
5CA9: 77             LD      (HL),A          
5CAA: 00             NOP                     
5CAB: 00             NOP                     
5CAC: 90             SUB     B               
5CAD: 03             INC     BC              
5CAE: 01 97 02       LD      BC,$0297        
5CB1: 06 D2          LD      B,$D2           
5CB3: 97             SUB     A               
5CB4: BF             CP      A               
5CB5: 9F             SBC     A               
5CB6: 03             INC     BC              
5CB7: A0             AND     B               
5CB8: 0B             DEC     BC              
5CB9: 58             LD      E,B             
5CBA: 0E 56          LD      C,$56           
5CBC: 0D             DEC     C               
5CBD: 53             LD      D,E             
5CBE: 0E 06          LD      C,$06           
5CC0: 0A             LD      A,(BC)          
5CC1: 11 0A 42       LD      DE,$420A        
5CC4: 0A             LD      A,(BC)          
5CC5: 09             ADD     HL,BC           
5CC6: 1A             LD      A,(DE)          
5CC7: 15             DEC     D               
5CC8: 08             EX      AF,AF'          
5CC9: 1F             RRA                     
5CCA: 46             LD      B,(HL)          
5CCB: D2 97 BF       JP      NC,$BF97        
5CCE: 9F             SBC     A               
5CCF: 03             INC     BC              
5CD0: A0             AND     B               
5CD1: AB             XOR     E               
5CD2: 6E             LD      L,(HL)          
5CD3: 8B             ADC     A,E             
5CD4: 4F             LD      C,A             
5CD5: 96             SUB     (HL)            
5CD6: 7B             LD      A,E             
5CD7: BF             CP      A               
5CD8: 14             INC     D               
5CD9: 0A             LD      A,(BC)          
5CDA: BC             CP      H               
5CDB: 45             LD      B,L             
5CDC: 5E             LD      E,(HL)          
5CDD: 85             ADD     A,L             
5CDE: 48             LD      C,B             
5CDF: 04             INC     B               
5CE0: BC             CP      H               
5CE1: 01 C4 4B       LD      BC,$4BC4        
5CE4: 5E             LD      E,(HL)          
5CE5: AB             XOR     E               
5CE6: BB             CP      E               
5CE7: DB 72          IN      A,($72)         
5CE9: 74             LD      (HL),H          
5CEA: C0             RET     NZ              
5CEB: 8B             ADC     A,E             
5CEC: 9A             SBC     D               
5CED: 6B             LD      L,E             
5CEE: BF             CP      A               
5CEF: C7             RST     0X00            
5CF0: DE 90          SBC     $90             
5CF2: 14             INC     D               
5CF3: 0F             RRCA                    
5CF4: 58             LD      E,B             
5CF5: 64             LD      H,H             
5CF6: C5             PUSH    BC              
5CF7: F5             PUSH    AF              
5CF8: 8B             ADC     A,E             
5CF9: 61             LD      H,C             
5CFA: 17             RLA                     
5CFB: 36 92          LD      (HL),$92        
5CFD: 90             SUB     B               
5CFE: 73             LD      (HL),E          
5CFF: C3 6A 07       JP      $076A           
5D02: 4F             LD      C,A             
5D03: 04             INC     B               
5D04: BC             CP      H               
5D05: D0             RET     NC              
5D06: 60             LD      H,B             
5D07: D4 6A 82       CALL    NC,$826A        
5D0A: 49             LD      C,C             
5D0B: 23             INC     HL              
5D0C: 62             LD      H,D             
5D0D: 94             SUB     H               
5D0E: BE             CP      (HL)            
5D0F: 17             RLA                     
5D10: 60             LD      H,B             
5D11: 9A             SBC     D               
5D12: 07             RLCA                    
5D13: 01 AB 08       LD      BC,$08AB        
5D16: 06 0D          LD      B,$0D           
5D18: 04             INC     B               
5D19: 9C             SBC     H               
5D1A: 1C             INC     E               
5D1B: 1E 9E          LD      E,$9E           
5D1D: 09             ADD     HL,BC           
5D1E: 02             LD      (BC),A          
5D1F: 46             LD      B,(HL)          
5D20: 46             LD      B,(HL)          
5D21: 02             LD      (BC),A          
5D22: 0B             DEC     BC              
5D23: 00             NOP                     
5D24: 00             NOP                     
5D25: 90             SUB     B               
5D26: 03             INC     BC              
5D27: 06 0D          LD      B,$0D           
5D29: 04             INC     B               
5D2A: 96             SUB     (HL)            
5D2B: 1E 1E          LD      E,$1E           
5D2D: 1F             RRA                     
5D2E: 02             LD      (BC),A          
5D2F: 80             ADD     A,B             
5D30: 97             SUB     A               
5D31: 00             NOP                     
5D32: 00             NOP                     
5D33: 90             SUB     B               
5D34: 03             INC     BC              
5D35: 01 97 02       LD      BC,$0297        
5D38: 06 D2          LD      B,$D2           
5D3A: 97             SUB     A               
5D3B: BF             CP      A               
5D3C: 9F             SBC     A               
5D3D: 03             INC     BC              
5D3E: A0             AND     B               
5D3F: 0B             DEC     BC              
5D40: 78             LD      A,B             
5D41: 0E 76          LD      C,$76           
5D43: 0D             DEC     C               
5D44: 73             LD      (HL),E          
5D45: 0E 06          LD      C,$06           
5D47: 0A             LD      A,(BC)          
5D48: 11 0A 42       LD      DE,$420A        
5D4B: 0A             LD      A,(BC)          
5D4C: 09             ADD     HL,BC           
5D4D: 1A             LD      A,(DE)          
5D4E: 15             DEC     D               
5D4F: 08             EX      AF,AF'          
5D50: 0E 66          LD      C,$66           
5D52: 0D             DEC     C               
5D53: 49             LD      C,C             
5D54: 15             DEC     D               
5D55: 02             LD      (BC),A          
5D56: 1F             RRA                     
5D57: 0A             LD      A,(BC)          
5D58: D2 97 BF       JP      NC,$BF97        
5D5B: 9F             SBC     A               
5D5C: 03             INC     BC              
5D5D: A0             AND     B               
5D5E: AB             XOR     E               
5D5F: 6E             LD      L,(HL)          
5D60: 8B             ADC     A,E             
5D61: 4F             LD      C,A             
5D62: A8             XOR     B               
5D63: 1F             RRA                     
5D64: 0C             INC     C               
5D65: 8E             ADC     A,(HL)          
5D66: 48             LD      C,B             
5D67: BF             CP      A               
5D68: 14             INC     D               
5D69: 0D             DEC     C               
5D6A: BA             CP      D               
5D6B: D6 15          SUB     $15             
5D6D: C2 16 81       JP      NZ,$8116        
5D70: 61             LD      H,C             
5D71: 29             ADD     HL,HL           
5D72: 0E 29          LD      C,$29           
5D74: 0D             DEC     C               
5D75: 25             DEC     H               
5D76: 08             EX      AF,AF'          
5D77: 3D             DEC     A               
5D78: 1F             RRA                     
5D79: 20 5F          JR      NZ,$5DDA        
5D7B: BE             CP      (HL)            
5D7C: 57             LD      D,A             
5D7D: 17             RLA                     
5D7E: AF             XOR     A               
5D7F: 55             LD      D,L             
5D80: 06 BC          LD      B,$BC           
5D82: 44             LD      B,H             
5D83: A0             AND     B               
5D84: 3F             CCF                     
5D85: 16 0D          LD      D,$0D           
5D87: 47             LD      B,A             
5D88: 89             ADC     A,C             
5D89: 17             RLA                     
5D8A: 35             DEC     (HL)            
5D8B: 15             DEC     D               
5D8C: 12             LD      (DE),A          
5D8D: 53             LD      D,E             
5D8E: EB             EX      DE,HL           
5D8F: 5D             LD      E,L             
5D90: C7             RST     0X00            
5D91: DE 4F          SBC     $4F             
5D93: 24             INC     H               
5D94: 63             LD      H,E             
5D95: 16 DB          LD      D,$DB           
5D97: 59             LD      E,C             
5D98: 71             LD      (HL),C          
5D99: 7B             LD      A,E             
5D9A: 24             INC     H               
5D9B: 14             INC     D               
5D9C: 0C             INC     C               
5D9D: 0D             DEC     C               
5D9E: 19             ADD     HL,DE           
5D9F: 1F             RRA                     
5DA0: 0E D2          LD      C,$D2           
5DA2: 97             SUB     A               
5DA3: BF             CP      A               
5DA4: 9F             SBC     A               
5DA5: 03             INC     BC              
5DA6: A0             AND     B               
5DA7: 72             LD      (HL),D          
5DA8: B1             OR      C               
5DA9: BE             CP      (HL)            
5DAA: A0             AND     B               
5DAB: D6 B5          SUB     $B5             
5DAD: 56             LD      D,(HL)          
5DAE: 72             LD      (HL),D          
5DAF: A8             XOR     B               
5DB0: 1F             RRA                     
5DB1: 06 4B          LD      B,$4B           
5DB3: 7B             LD      A,E             
5DB4: 5F             LD      E,A             
5DB5: A0             AND     B               
5DB6: 1B             DEC     DE              
5DB7: 9C             SBC     H               
5DB8: 9A             SBC     D               
5DB9: 07             RLCA                    
5DBA: 01 AB 08       LD      BC,$08AB        
5DBD: 06 0D          LD      B,$0D           
5DBF: 04             INC     B               
5DC0: 9C             SBC     H               
5DC1: 1C             INC     E               
5DC2: 20 9E          JR      NZ,$5D62        
5DC4: 09             ADD     HL,BC           
5DC5: 02             LD      (BC),A          
5DC6: 46             LD      B,(HL)          
5DC7: 46             LD      B,(HL)          
5DC8: 02             LD      (BC),A          
5DC9: 0B             DEC     BC              
5DCA: 00             NOP                     
5DCB: 00             NOP                     
5DCC: 90             SUB     B               
5DCD: 03             INC     BC              
5DCE: 06 0D          LD      B,$0D           
5DD0: 04             INC     B               
5DD1: 96             SUB     (HL)            
5DD2: 1E 20          LD      E,$20           
5DD4: 21 05 25       LD      HL,$2505        
5DD7: 00             NOP                     
5DD8: 00             NOP                     
5DD9: 90             SUB     B               
5DDA: 03             INC     BC              
5DDB: 01 99 02       LD      BC,$0299        
5DDE: 05             DEC     B               
5DDF: 85             ADD     A,L             
5DE0: A5             AND     L               
5DE1: 65             LD      H,L             
5DE2: 49             LD      C,C             
5DE3: 4F             LD      C,A             
5DE4: 0B             DEC     BC              
5DE5: 01 9A 07       LD      BC,$079A        
5DE8: 01 AB 08       LD      BC,$08AB        
5DEB: 0C             INC     C               
5DEC: 0E 0A          LD      C,$0A           
5DEE: 0D             DEC     C               
5DEF: 04             INC     B               
5DF0: 9C             SBC     H               
5DF1: 1C             INC     E               
5DF2: 22 9E 14       LD      ($149E),HL      
5DF5: 1C             INC     E               
5DF6: 3F             CCF                     
5DF7: 10 09          DJNZ    $5E02           
5DF9: 02             LD      (BC),A          
5DFA: 46             LD      B,(HL)          
5DFB: 46             LD      B,(HL)          
5DFC: 05             DEC     B               
5DFD: 0B             DEC     BC              
5DFE: 00             NOP                     
5DFF: 00             NOP                     
5E00: 90             SUB     B               
5E01: 03             INC     BC              
5E02: 06 0D          LD      B,$0D           
5E04: 04             INC     B               
5E05: 98             SBC     B               
5E06: 1E 22          LD      E,$22           
5E08: 23             INC     HL              
5E09: 05             DEC     B               
5E0A: 34             INC     (HL)            
5E0B: 00             NOP                     
5E0C: 00             NOP                     
5E0D: 90             SUB     B               
5E0E: 03             INC     BC              
5E0F: 01 99 02       LD      BC,$0299        
5E12: 05             DEC     B               
5E13: 85             ADD     A,L             
5E14: A5             AND     L               
5E15: 65             LD      H,L             
5E16: 49             LD      C,C             
5E17: 4F             LD      C,A             
5E18: 07             RLCA                    
5E19: 01 AB 0B       LD      BC,$0BAB        
5E1C: 01 9A 08       LD      BC,$089A        
5E1F: 1B             DEC     DE              
5E20: 0E 19          LD      C,$19           
5E22: 0D             DEC     C               
5E23: 08             EX      AF,AF'          
5E24: 14             INC     D               
5E25: 03             INC     BC              
5E26: 88             ADC     A,B             
5E27: 24             INC     H               
5E28: 1C             INC     E               
5E29: 3F             CCF                     
5E2A: 10 0C          DJNZ    $5E38           
5E2C: 0D             DEC     C               
5E2D: 07             RLCA                    
5E2E: 03             INC     BC              
5E2F: 88             ADC     A,B             
5E30: 24             INC     H               
5E31: 17             RLA                     
5E32: 3E 88          LD      A,$88           
5E34: 0C             INC     C               
5E35: 0D             DEC     C               
5E36: 04             INC     B               
5E37: 9C             SBC     H               
5E38: 1C             INC     E               
5E39: 24             INC     H               
5E3A: 9E             SBC     (HL)            
5E3B: 09             ADD     HL,BC           
5E3C: 02             LD      (BC),A          
5E3D: 46             LD      B,(HL)          
5E3E: 46             LD      B,(HL)          
5E3F: 05             DEC     B               
5E40: 0B             DEC     BC              
5E41: 00             NOP                     
5E42: 00             NOP                     
5E43: 90             SUB     B               
5E44: 03             INC     BC              
5E45: 06 0D          LD      B,$0D           
5E47: 04             INC     B               
5E48: 98             SBC     B               
5E49: 1E 24          LD      E,$24           
5E4B: 25             DEC     H               
5E4C: 06 80          LD      B,$80           
5E4E: FD                                  
5E4F: 00             NOP                     
5E50: 00             NOP                     
5E51: 90             SUB     B               
5E52: 03             INC     BC              
5E53: 25             DEC     H               
5E54: 04             INC     B               
5E55: 23             INC     HL              
5E56: 34             INC     (HL)            
5E57: 92             SUB     D               
5E58: 90             SUB     B               
5E59: 8C             ADC     A,H             
5E5A: D5             PUSH    DE              
5E5B: 15             DEC     D               
5E5C: 8F             ADC     A,A             
5E5D: 16 2C          LD      D,$2C           
5E5F: 49             LD      C,C             
5E60: B3             OR      E               
5E61: E0             RET     PO              
5E62: 1B             DEC     DE              
5E63: 54             LD      D,H             
5E64: C3 9A AB       JP      $AB9A           
5E67: 98             SBC     B               
5E68: 8E             ADC     A,(HL)          
5E69: 48             LD      C,B             
5E6A: 77             LD      (HL),A          
5E6B: 15             DEC     D               
5E6C: 03             INC     BC              
5E6D: BA             CP      D               
5E6E: 2E 56          LD      L,$56           
5E70: 83             ADD     A,E             
5E71: 49             LD      C,C             
5E72: AB             XOR     E               
5E73: 98             SBC     B               
5E74: 73             LD      (HL),E          
5E75: 49             LD      C,C             
5E76: C7             RST     0X00            
5E77: DE 2E          SBC     $2E             
5E79: 02             LD      (BC),A          
5E7A: 04             INC     B               
5E7B: 34             INC     (HL)            
5E7C: 92             SUB     D               
5E7D: 90             SUB     B               
5E7E: 8C             ADC     A,H             
5E7F: 0B             DEC     BC              
5E80: 01 9A 07       LD      BC,$079A        
5E83: 01 AB 08       LD      BC,$08AB        
5E86: 80             ADD     A,B             
5E87: C0             RET     NZ              
5E88: 0E 80          LD      C,$80           
5E8A: BD             CP      L               
5E8B: 0D             DEC     C               
5E8C: 04             INC     B               
5E8D: 9C             SBC     H               
5E8E: 1C             INC     E               
5E8F: 26 9E          LD      H,$9E           
5E91: 0B             DEC     BC              
5E92: 80             ADD     A,B             
5E93: B4             OR      H               
5E94: 05             DEC     B               
5E95: 08             EX      AF,AF'          
5E96: 30 1F          JR      NC,$5EB7        
5E98: 2E 34          LD      L,$34           
5E9A: 92             SUB     D               
5E9B: 90             SUB     B               
5E9C: 8C             ADC     A,H             
5E9D: 53             LD      D,E             
5E9E: 17             RLA                     
5E9F: 6E             LD      L,(HL)          
5EA0: DF             RST     0X18            
5EA1: 6E             LD      L,(HL)          
5EA2: 13             INC     DE              
5EA3: 71             LD      (HL),C          
5EA4: 61             LD      H,C             
5EA5: F3             DI                      
5EA6: 9B             SBC     E               
5EA7: 45             LD      B,L             
5EA8: 77             LD      (HL),A          
5EA9: EF             RST     0X28            
5EAA: 9F             SBC     A               
5EAB: 8E             ADC     A,(HL)          
5EAC: 48             LD      C,B             
5EAD: 51             LD      D,C             
5EAE: 18 EB          JR      $5E9B           
5EB0: C1             POP     BC              
5EB1: 78             LD      A,B             
5EB2: B1             OR      C               
5EB3: 8E             ADC     A,(HL)          
5EB4: 5F             LD      E,A             
5EB5: 89             ADC     A,C             
5EB6: 17             RLA                     
5EB7: 67             LD      H,A             
5EB8: 16 82          LD      D,$82           
5EBA: 17             RLA                     
5EBB: 46             LD      B,(HL)          
5EBC: 5E             LD      E,(HL)          
5EBD: 44             LD      B,H             
5EBE: A0             AND     B               
5EBF: B8             CP      B               
5EC0: 16 35          LD      D,$35           
5EC2: 15             DEC     D               
5EC3: 12             LD      (DE),A          
5EC4: 53             LD      D,E             
5EC5: EC 5D 10       CALL    PE,$105D        
5EC8: 42             LD      B,D             
5EC9: 1F             RRA                     
5ECA: 40             LD      B,B             
5ECB: 34             INC     (HL)            
5ECC: 92             SUB     D               
5ECD: 90             SUB     B               
5ECE: 8C             ADC     A,H             
5ECF: 77             LD      (HL),A          
5ED0: 15             DEC     D               
5ED1: 0F             RRCA                    
5ED2: BA             CP      D               
5ED3: 75             LD      (HL),L          
5ED4: B1             OR      C               
5ED5: 96             SUB     (HL)            
5ED6: 14             INC     D               
5ED7: 51             LD      D,C             
5ED8: 18 43          JR      $5F1D           
5EDA: C2 33 98       JP      NZ,$9833        
5EDD: 1B             DEC     DE              
5EDE: B7             OR      A               
5EDF: 33             INC     SP              
5EE0: BB             CP      E               
5EE1: FB             EI                      
5EE2: 1B             DEC     DE              
5EE3: 10 53          DJNZ    $5F38           
5EE5: F3             DI                      
5EE6: 23             INC     HL              
5EE7: 8E             ADC     A,(HL)          
5EE8: C5             PUSH    BC              
5EE9: 3D             DEC     A               
5EEA: 62             LD      H,D             
5EEB: 50             LD      D,B             
5EEC: BD             CP      L               
5EED: 0B             DEC     BC              
5EEE: 58             LD      E,B             
5EEF: 9B             SBC     E               
5EF0: C1             POP     BC              
5EF1: 4F             LD      C,A             
5EF2: 77             LD      (HL),A          
5EF3: 66             LD      H,(HL)          
5EF4: C6 9B          ADD     $9B             
5EF6: 15             DEC     D               
5EF7: 5B             LD      E,E             
5EF8: CA 40 55       JP      Z,$5540         
5EFB: F4 81 F3       CALL    P,$F381         
5EFE: 5F             LD      E,A             
5EFF: 5F             LD      E,A             
5F00: BE             CP      (HL)            
5F01: 04             INC     B               
5F02: 18 11          JR      $5F15           
5F04: A0             AND     B               
5F05: FF             RST     0X38            
5F06: 14             INC     D               
5F07: C0             RET     NZ              
5F08: 93             SUB     E               
5F09: 63             LD      H,E             
5F0A: F4 18 3B       CALL    P,$3B18         
5F0D: 1F             RRA                     
5F0E: 39             ADD     HL,SP           
5F0F: 34             INC     (HL)            
5F10: 92             SUB     D               
5F11: 90             SUB     B               
5F12: 8C             ADC     A,H             
5F13: E9             JP      (HL)            
5F14: 16 9E          LD      D,$9E           
5F16: 7A             LD      A,D             
5F17: C3 B5 1B       JP      $1BB5           
5F1A: BC             CP      H               
5F1B: 3E A1          LD      A,$A1           
5F1D: 6F             LD      L,A             
5F1E: 13             INC     DE              
5F1F: 1B             DEC     DE              
5F20: DD                                  
5F21: C3 9E 77       JP      $779E           
5F24: 98             SBC     B               
5F25: F9             LD      SP,HL           
5F26: BF             CP      A               
5F27: F3             DI                      
5F28: 9B             SBC     E               
5F29: 14             INC     D               
5F2A: D0             RET     NC              
5F2B: 11 BC 8A       LD      DE,$8ABC        
5F2E: 64             LD      H,H             
5F2F: 0E 9F          LD      C,$9F           
5F31: FF             RST     0X38            
5F32: 14             INC     D               
5F33: C0             RET     NZ              
5F34: 93             SUB     E               
5F35: 09             ADD     HL,BC           
5F36: 15             DEC     D               
5F37: 82             ADD     A,D             
5F38: 17             RLA                     
5F39: 59             LD      E,C             
5F3A: DB 46          IN      A,($46)         
5F3C: 7A             LD      A,D             
5F3D: 16 EE          LD      D,$EE           
5F3F: F0             RET     P               
5F40: 72             LD      (HL),D          
5F41: AF             XOR     A               
5F42: 14             INC     D               
5F43: 81             ADD     A,C             
5F44: 15             DEC     D               
5F45: 59             LD      E,C             
5F46: 98             SBC     B               
5F47: 22 09 02       LD      ($0209),HL      
5F4A: 46             LD      B,(HL)          
5F4B: 46             LD      B,(HL)          
5F4C: 06 6E          LD      B,$6E           
5F4E: 00             NOP                     
5F4F: 00             NOP                     
5F50: 90             SUB     B               
5F51: 03             INC     BC              
5F52: 69             LD      L,C             
5F53: 0D             DEC     C               
5F54: 67             LD      H,A             
5F55: 04             INC     B               
5F56: 62             LD      H,D             
5F57: 83             ADD     A,E             
5F58: 48             LD      C,B             
5F59: 8D             ADC     A,L             
5F5A: 48             LD      C,B             
5F5B: 30 79          JR      NC,$5FD6        
5F5D: 0F             RRCA                    
5F5E: BC             CP      H               
5F5F: 83             ADD     A,E             
5F60: 48             LD      C,B             
5F61: 83             ADD     A,E             
5F62: 7A             LD      A,D             
5F63: 44             LD      B,H             
5F64: 45             LD      B,L             
5F65: 45             LD      B,L             
5F66: 8B             ADC     A,E             
5F67: C5             PUSH    BC              
5F68: 83             ADD     A,E             
5F69: 73             LD      (HL),E          
5F6A: 8D             ADC     A,L             
5F6B: C3 83 33       JP      $3383           
5F6E: 98             SBC     B               
5F6F: 7B             LD      A,E             
5F70: A6             AND     (HL)            
5F71: BF             CP      A               
5F72: 9A             SBC     D               
5F73: 0A             LD      A,(BC)          
5F74: 58             LD      E,B             
5F75: 73             LD      (HL),E          
5F76: 49             LD      C,C             
5F77: B5             OR      L               
5F78: 6C             LD      L,H             
5F79: 74             LD      (HL),H          
5F7A: C0             RET     NZ              
5F7B: 4B             LD      C,E             
5F7C: 62             LD      H,D             
5F7D: 73             LD      (HL),E          
5F7E: 49             LD      C,C             
5F7F: C7             RST     0X00            
5F80: DE FC          SBC     $FC             
5F82: ED                                  
5F83: EF             RST     0X28            
5F84: 59             LD      E,C             
5F85: 01 A0 BB       LD      BC,$BBA0        
5F88: 15             DEC     D               
5F89: 58             LD      E,B             
5F8A: 72             LD      (HL),D          
5F8B: 55             LD      D,L             
5F8C: 5E             LD      E,(HL)          
5F8D: 6F             LD      L,A             
5F8E: C5             PUSH    BC              
5F8F: 0F             RRCA                    
5F90: A0             AND     B               
5F91: 1B             DEC     DE              
5F92: 58             LD      E,B             
5F93: 19             ADD     HL,DE           
5F94: A1             AND     C               
5F95: BB             CP      E               
5F96: 15             DEC     D               
5F97: 5B             LD      E,E             
5F98: 48             LD      C,B             
5F99: C7             RST     0X00            
5F9A: DE 8F          SBC     $8F             
5F9C: AF             XOR     A               
5F9D: 66             LD      H,(HL)          
5F9E: 49             LD      C,C             
5F9F: 46             LD      B,(HL)          
5FA0: 62             LD      H,D             
5FA1: 67             LD      H,A             
5FA2: 16 83          LD      D,$83           
5FA4: B2             OR      D               
5FA5: 2B             DEC     HL              
5FA6: 96             SUB     (HL)            
5FA7: C7             RST     0X00            
5FA8: DE 77          SBC     $77             
5FAA: 16 F3          LD      D,$F3           
5FAC: B9             CP      C               
5FAD: 2F             CPL                     
5FAE: 9E             SBC     (HL)            
5FAF: 4F             LD      C,A             
5FB0: DB 45          IN      A,($45)         
5FB2: DB EF          IN      A,($EF)         
5FB4: 9F             SBC     A               
5FB5: 8E             ADC     A,(HL)          
5FB6: 48             LD      C,B             
5FB7: E3             EX      (SP),HL         
5FB8: 06 1E          LD      B,$1E           
5FBA: 26 27          LD      H,$27           
5FBC: 07             RLCA                    
5FBD: 54             LD      D,H             
5FBE: 00             NOP                     
5FBF: 00             NOP                     
5FC0: 80             ADD     A,B             
5FC1: 03             INC     BC              
5FC2: 27             DAA                     
5FC3: 04             INC     B               
5FC4: 25             DEC     H               
5FC5: 5F             LD      E,A             
5FC6: BE             CP      (HL)            
5FC7: 7C             LD      A,H             
5FC8: 13             INC     DE              
5FC9: 8E             ADC     A,(HL)          
5FCA: 5F             LD      E,A             
5FCB: 86             ADD     A,(HL)          
5FCC: 19             ADD     HL,DE           
5FCD: 66             LD      H,(HL)          
5FCE: 9E             SBC     (HL)            
5FCF: A3             AND     E               
5FD0: A0             AND     B               
5FD1: 03             INC     BC              
5FD2: BA             CP      D               
5FD3: F3             DI                      
5FD4: 8C             ADC     A,H             
5FD5: 87             ADD     A,A             
5FD6: 8C             ADC     A,H             
5FD7: D7             RST     0X10            
5FD8: B5             OR      L               
5FD9: 21 98 95       LD      HL,$9598        
5FDC: 9A             SBC     D               
5FDD: C7             RST     0X00            
5FDE: 7A             LD      A,D             
5FDF: CB B5          RES     6,L             
5FE1: 96             SUB     (HL)            
5FE2: 96             SUB     (HL)            
5FE3: DB 72          IN      A,($72)         
5FE5: 44             LD      B,H             
5FE6: 55             LD      D,L             
5FE7: 74             LD      (HL),H          
5FE8: 98             SBC     B               
5FE9: 2E 02          LD      L,$02           
5FEB: 0C             INC     C               
5FEC: 8D             ADC     A,L             
5FED: C5             PUSH    BC              
5FEE: 0D             DEC     C               
5FEF: A0             AND     B               
5FF0: C7             RST     0X00            
5FF1: 7A             LD      A,D             
5FF2: C6 B5          ADD     $B5             
5FF4: 66             LD      H,(HL)          
5FF5: 9E             SBC     (HL)            
5FF6: A3             AND     E               
5FF7: A0             AND     B               
5FF8: 0B             DEC     BC              
5FF9: 14             INC     D               
5FFA: 1F             RRA                     
5FFB: 12             LD      (DE),A          
5FFC: 5F             LD      E,A             
5FFD: BE             CP      (HL)            
5FFE: 09             ADD     HL,BC           
5FFF: 15             DEC     D               
6000: 09             ADD     HL,BC           
6001: 56             LD      D,(HL)          
6002: 8B             ADC     A,E             
6003: AF             XOR     A               
6004: D7             RST     0X10            
6005: B5             OR      L               
6006: 21 98 95       LD      HL,$9598        
6009: 9A             SBC     D               
600A: C7             RST     0X00            
600B: 7A             LD      A,D             
600C: 5B             LD      E,E             
600D: BB             CP      E               
600E: 09             ADD     HL,BC           
600F: 02             LD      (BC),A          
6010: 46             LD      B,(HL)          
6011: 01 07 80       LD      BC,$8007        
6014: F5             PUSH    AF              
6015: 00             NOP                     
6016: 00             NOP                     
6017: 90             SUB     B               
6018: 03             INC     BC              
6019: 80             ADD     A,B             
601A: EF             RST     0X28            
601B: 0D             DEC     C               
601C: 80             ADD     A,B             
601D: EC 04 80       CALL    PE,$8004        
6020: E6 5F          AND     $5F             
6022: BE             CP      (HL)            
6023: 5B             LD      E,E             
6024: B1             OR      C               
6025: 4B             LD      C,E             
6026: 7B             LD      A,E             
6027: 4F             LD      C,A             
6028: 45             LD      B,L             
6029: 83             ADD     A,E             
602A: 48             LD      C,B             
602B: 83             ADD     A,E             
602C: 7A             LD      A,D             
602D: 55             LD      D,L             
602E: 45             LD      B,L             
602F: EB             EX      DE,HL           
6030: BF             CP      A               
6031: 73             LD      (HL),E          
6032: 7B             LD      A,E             
6033: C5             PUSH    BC              
6034: 7E             LD      A,(HL)          
6035: B6             OR      (HL)            
6036: 85             ADD     A,L             
6037: D0             RET     NC              
6038: 15             DEC     D               
6039: 82             ADD     A,D             
603A: 17             RLA                     
603B: 45             LD      B,L             
603C: 5E             LD      E,(HL)          
603D: B8             CP      B               
603E: A0             AND     B               
603F: 47             LD      B,A             
6040: 62             LD      H,D             
6041: 9F             SBC     A               
6042: 15             DEC     D               
6043: 49             LD      C,C             
6044: 16 A5          LD      D,$A5           
6046: 9F             SBC     A               
6047: B2             OR      D               
6048: 17             RLA                     
6049: 96             SUB     (HL)            
604A: 14             INC     D               
604B: 51             LD      D,C             
604C: 18 43          JR      $6091           
604E: C2 33 98       JP      NZ,$9833        
6051: AF             XOR     A               
6052: 94             SUB     H               
6053: 7F             LD      A,A             
6054: 4E             LD      C,(HL)          
6055: 33             INC     SP              
6056: BB             CP      E               
6057: FA 1C FF       JP      M,$FF1C         
605A: F9             LD      SP,HL           
605B: 73             LD      (HL),E          
605C: 7B             LD      A,E             
605D: 4B             LD      C,E             
605E: 7B             LD      A,E             
605F: F4 BD 04       CALL    P,$04BD         
6062: B2             OR      D               
6063: FF             RST     0X38            
6064: 8B             ADC     A,E             
6065: F6 F9          OR      $F9             
6067: DB 72          IN      A,($72)         
6069: 75             LD      (HL),L          
606A: 5B             LD      E,E             
606B: 84             ADD     A,H             
606C: BF             CP      A               
606D: 9B             SBC     E               
606E: 15             DEC     D               
606F: C4 B5 E1       CALL    NZ,$E1B5        
6072: 5F             LD      E,A             
6073: 1B             DEC     DE              
6074: 92             SUB     D               
6075: 5F             LD      E,A             
6076: BE             CP      (HL)            
6077: DB 16          IN      A,($16)         
6079: 87             ADD     A,A             
607A: BE             CP      (HL)            
607B: B3             OR      E               
607C: 9A             SBC     D               
607D: 8E             ADC     A,(HL)          
607E: 48             LD      C,B             
607F: 82             ADD     A,D             
6080: 17             RLA                     
6081: 52             LD      D,D             
6082: 5E             LD      E,(HL)          
6083: 83             ADD     A,E             
6084: 49             LD      C,C             
6085: 9E             SBC     (HL)            
6086: 61             LD      H,C             
6087: 82             ADD     A,D             
6088: 17             RLA                     
6089: 46             LD      B,(HL)          
608A: 5E             LD      E,(HL)          
608B: 66             LD      H,(HL)          
608C: 9E             SBC     (HL)            
608D: C7             RST     0X00            
608E: A0             AND     B               
608F: EE F9          XOR     $F9             
6091: 66             LD      H,(HL)          
6092: 7B             LD      A,E             
6093: 83             ADD     A,E             
6094: 61             LD      H,C             
6095: 6B             LD      L,E             
6096: BF             CP      A               
6097: 3F             CCF                     
6098: 92             SUB     D               
6099: EB             EX      DE,HL           
609A: F9             LD      SP,HL           
609B: 8F             ADC     A,A             
609C: 14             INC     D               
609D: 82             ADD     A,D             
609E: 17             RLA                     
609F: 46             LD      B,(HL)          
60A0: 5E             LD      E,(HL)          
60A1: 66             LD      H,(HL)          
60A2: 9E             SBC     (HL)            
60A3: C7             RST     0X00            
60A4: A0             AND     B               
60A5: FB             EI                      
60A6: F9             LD      SP,HL           
60A7: 1B             DEC     DE              
60A8: A1             AND     C               
60A9: B5             OR      L               
60AA: 94             SUB     H               
60AB: 09             ADD     HL,BC           
60AC: BC             CP      H               
60AD: D6 9C          SUB     $9C             
60AF: D6 9C          SUB     $9C             
60B1: DB 72          IN      A,($72)         
60B3: B6             OR      (HL)            
60B4: 49             LD      C,C             
60B5: 84             ADD     A,H             
60B6: 74             LD      (HL),H          
60B7: 83             ADD     A,E             
60B8: 7B             LD      A,E             
60B9: 4B             LD      C,E             
60BA: 62             LD      H,D             
60BB: 8E             ADC     A,(HL)          
60BC: 48             LD      C,B             
60BD: 7F             LD      A,A             
60BE: 17             RLA                     
60BF: F3             DI                      
60C0: 8C             ADC     A,H             
60C1: 5F             LD      E,A             
60C2: BE             CP      (HL)            
60C3: 51             LD      D,C             
60C4: 90             SUB     B               
60C5: 96             SUB     (HL)            
60C6: 64             LD      H,H             
60C7: 95             SUB     L               
60C8: 73             LD      (HL),E          
60C9: 8C             ADC     A,H             
60CA: 17             RLA                     
60CB: CF             RST     0X08            
60CC: 49             LD      C,C             
60CD: 13             INC     DE              
60CE: BA             CP      D               
60CF: CA 06 3C       JP      Z,$3C06         
60D2: C6 B3          ADD     $B3             
60D4: E0             RET     PO              
60D5: 68             LD      L,B             
60D6: 4D             LD      C,L             
60D7: AF             XOR     A               
60D8: A0             AND     B               
60D9: D6 15          SUB     $15             
60DB: D5             PUSH    DE              
60DC: 15             DEC     D               
60DD: 89             ADC     A,C             
60DE: 17             RLA                     
60DF: CE 9C          ADC     $9C             
60E1: 7F             LD      A,A             
60E2: 49             LD      C,C             
60E3: 63             LD      H,E             
60E4: F4 95 73       CALL    P,$7395         
60E7: 3B             DEC     SP              
60E8: 15             DEC     D               
60E9: 4B             LD      C,E             
60EA: 62             LD      H,D             
60EB: FE B2          CP      $B2             
60ED: 04             INC     B               
60EE: 8A             ADC     A,D             
60EF: DD 46 D0       LD      B,(IX+$D0)      
60F2: 15             DEC     D               
60F3: 6B             LD      L,E             
60F4: BF             CP      A               
60F5: 95             SUB     L               
60F6: 73             LD      (HL),E          
60F7: 9F             SBC     A               
60F8: 15             DEC     D               
60F9: F3             DI                      
60FA: 46             LD      B,(HL)          
60FB: 8E             ADC     A,(HL)          
60FC: 48             LD      C,B             
60FD: 9F             SBC     A               
60FE: 15             DEC     D               
60FF: DB 16          IN      A,($16)         
6101: D7             RST     0X10            
6102: B9             CP      C               
6103: D1             POP     DE              
6104: B5             OR      L               
6105: 97             SUB     A               
6106: C6 1E          ADD     $1E             
6108: 28 29          JR      Z,$6133         
610A: 04             INC     B               
610B: 81             ADD     A,C             
610C: 0A             LD      A,(BC)          
610D: 00             NOP                     
610E: 00             NOP                     
610F: 90             SUB     B               
6110: 03             INC     BC              
6111: 29             ADD     HL,HL           
6112: 04             INC     B               
6113: 27             DAA                     
6114: 87             ADD     A,A             
6115: 74             LD      (HL),H          
6116: 90             SUB     B               
6117: 5A             LD      E,D             
6118: 4B             LD      C,E             
6119: 77             LD      (HL),A          
611A: D9             EXX                     
611B: B5             OR      L               
611C: 16 B2          LD      D,$B2           
611E: 90             SUB     B               
611F: 73             LD      (HL),E          
6120: 5B             LD      E,E             
6121: 70             LD      (HL),B          
6122: FD 1B          DEC     DE              
6124: F3             DI                      
6125: 8C             ADC     A,H             
6126: 5B             LD      E,E             
6127: 4D             LD      C,L             
6128: 89             ADC     A,C             
6129: 5B             LD      E,E             
612A: 88             ADC     A,B             
612B: 96             SUB     (HL)            
612C: FF             RST     0X38            
612D: B2             OR      D               
612E: 9F             SBC     A               
612F: 15             DEC     D               
6130: 5B             LD      E,E             
6131: B1             OR      C               
6132: 83             ADD     A,E             
6133: 7A             LD      A,D             
6134: 4F             LD      C,A             
6135: 45             LD      B,L             
6136: 9F             SBC     A               
6137: 7A             LD      A,D             
6138: D9             EXX                     
6139: BD             CP      L               
613A: 22 02 05       LD      ($0502),HL      
613D: 87             ADD     A,A             
613E: 74             LD      (HL),H          
613F: 90             SUB     B               
6140: 5A             LD      E,D             
6141: 49             LD      C,C             
6142: 07             RLCA                    
6143: 80             ADD     A,B             
6144: CB 0D          RRC     L               
6146: 80             ADD     A,B             
6147: C8             RET     Z               
6148: 0E 04          LD      C,$04           
614A: 0A             LD      A,(BC)          
614B: 48             LD      C,B             
614C: 0A             LD      A,(BC)          
614D: 12             LD      (DE),A          
614E: 04             INC     B               
614F: 80             ADD     A,B             
6150: BC             CP      H               
6151: C7             RST     0X00            
6152: DE 3F          SBC     $3F             
6154: 16 0A          LD      D,$0A           
6156: BC             CP      H               
6157: 26 A1          LD      H,$A1           
6159: 93             SUB     E               
615A: 7A             LD      A,D             
615B: 09             ADD     HL,BC           
615C: 15             DEC     D               
615D: 26 D2          LD      H,$D2           
615F: BF             CP      A               
6160: 14             INC     D               
6161: 1B             DEC     DE              
6162: BC             CP      H               
6163: 1B             DEC     DE              
6164: A1             AND     C               
6165: 2F             CPL                     
6166: 49             LD      C,C             
6167: B0             OR      B               
6168: 17             RLA                     
6169: B6             OR      (HL)            
616A: 46             LD      B,(HL)          
616B: 56             LD      D,(HL)          
616C: 5E             LD      E,(HL)          
616D: D4 9C 71       CALL    NC,$719C        
6170: 61             LD      H,C             
6171: 5B             LD      E,E             
6172: CA 95 73       JP      Z,$7395         
6175: 66             LD      H,(HL)          
6176: 17             RLA                     
6177: CB B0          RES     6,B             
6179: 0C             INC     C               
617A: BC             CP      H               
617B: DD 46 97       LD      B,(IX+$97)      
617E: 62             LD      H,D             
617F: A9             XOR     C               
6180: 15             DEC     D               
6181: 03             INC     BC              
6182: C4 FB 98       CALL    NZ,$98FB        
6185: 1B             DEC     DE              
6186: B7             OR      A               
6187: 33             INC     SP              
6188: BB             CP      E               
6189: 91             SUB     C               
618A: 1E 46          LD      E,$46           
618C: C2 08 79       JP      NZ,$7908        
618F: F3             DI                      
6190: 23             INC     HL              
6191: 58             LD      E,B             
6192: 72             LD      (HL),D          
6193: 56             LD      D,(HL)          
6194: 5E             LD      E,(HL)          
6195: C6 9C          ADD     $9C             
6197: D6 9C          SUB     $9C             
6199: 56             LD      D,(HL)          
619A: 72             LD      (HL),D          
619B: CB 06          RLC     (HL)            
619D: 01 18 3E       LD      BC,$3E18        
61A0: C5             PUSH    BC              
61A1: 9B             SBC     E               
61A2: 15             DEC     D               
61A3: 5B             LD      E,E             
61A4: CA 67 4D       JP      Z,$4D67         
61A7: 86             ADD     A,(HL)          
61A8: 96             SUB     (HL)            
61A9: 80             ADD     A,B             
61AA: A1             AND     C               
61AB: D0             RET     NC              
61AC: 15             DEC     D               
61AD: 7B             LD      A,E             
61AE: 14             INC     D               
61AF: D0             RET     NC              
61B0: 92             SUB     D               
61B1: 7F             LD      A,A             
61B2: C6 44          ADD     $44             
61B4: F4 73 C6       CALL    P,$C673         
61B7: 9E             SBC     (HL)            
61B8: 77             LD      (HL),A          
61B9: 15             DEC     D               
61BA: 8A             ADC     A,D             
61BB: 8E             ADC     A,(HL)          
61BC: BE             CP      (HL)            
61BD: 16 8A          LD      D,$8A           
61BF: 17             RLA                     
61C0: 48             LD      C,B             
61C1: 51             LD      D,C             
61C2: 18 59          JR      $621D           
61C4: C2 82 7B       JP      NZ,$7B82        
61C7: 67             LD      H,A             
61C8: 16 FA          LD      D,$FA           
61CA: 17             RLA                     
61CB: 83             ADD     A,E             
61CC: 61             LD      H,C             
61CD: 47             LD      B,A             
61CE: 77             LD      (HL),A          
61CF: 53             LD      D,E             
61D0: B7             OR      A               
61D1: FE A4          CP      $A4             
61D3: FF             RST     0X38            
61D4: 15             DEC     D               
61D5: F3             DI                      
61D6: B9             CP      C               
61D7: 4B             LD      C,E             
61D8: 49             LD      C,C             
61D9: 41             LD      B,C             
61DA: B9             CP      C               
61DB: 83             ADD     A,E             
61DC: 96             SUB     (HL)            
61DD: CB B5          RES     6,L             
61DF: 77             LD      (HL),A          
61E0: 15             DEC     D               
61E1: 11 BC 73       LD      DE,$73BC        
61E4: C6 C3          ADD     $C3             
61E6: 9E             SBC     (HL)            
61E7: 63             LD      H,E             
61E8: BE             CP      (HL)            
61E9: D6 B5          SUB     $B5             
61EB: 90             SUB     B               
61EC: 73             LD      (HL),E          
61ED: 6C             LD      L,H             
61EE: 6A             LD      L,D             
61EF: 9F             SBC     A               
61F0: 15             DEC     D               
61F1: AF             XOR     A               
61F2: 14             INC     D               
61F3: 50             LD      D,B             
61F4: 6D             LD      L,L             
61F5: D9             EXX                     
61F6: B5             OR      L               
61F7: 75             LD      (HL),L          
61F8: B1             OR      C               
61F9: 03             INC     BC              
61FA: BF             CP      A               
61FB: AB             XOR     E               
61FC: 98             SBC     B               
61FD: 56             LD      D,(HL)          
61FE: D1             POP     DE              
61FF: 0A             LD      A,(BC)          
6200: 71             LD      (HL),C          
6201: 4B             LD      C,E             
6202: 7B             LD      A,E             
6203: 0C             INC     C               
6204: BA             CP      D               
6205: D6 47          SUB     $47             
6207: EB             EX      DE,HL           
6208: 15             DEC     D               
6209: 97             SUB     A               
620A: 54             LD      D,H             
620B: 9B             SBC     E               
620C: C1             POP     BC              
620D: 1E 2A          LD      E,$2A           
620F: 2C             INC     L               
6210: 0B             DEC     BC              
6211: 01 9A 09       LD      BC,$099A        
6214: 02             LD      (BC),A          
6215: 46             LD      B,(HL)          
6216: 46             LD      B,(HL)          
6217: 04             INC     B               
6218: 80             ADD     A,B             
6219: D9             EXX                     
621A: 00             NOP                     
621B: 00             NOP                     
621C: 90             SUB     B               
621D: 03             INC     BC              
621E: 80             ADD     A,B             
621F: D3 0D          OUT     ($0D),A         
6221: 80             ADD     A,B             
6222: D0             RET     NC              
6223: 04             INC     B               
6224: 80             ADD     A,B             
6225: CA 5F BE       JP      Z,$BE5F         
6228: 5B             LD      E,E             
6229: B1             OR      C               
622A: 4B             LD      C,E             
622B: 7B             LD      A,E             
622C: 48             LD      C,B             
622D: 45             LD      B,L             
622E: 98             SBC     B               
622F: C5             PUSH    BC              
6230: 4E             LD      C,(HL)          
6231: DB 3D          IN      A,($3D)         
6233: A0             AND     B               
6234: 91             SUB     C               
6235: 7A             LD      A,D             
6236: 63             LD      H,E             
6237: 16 8A          LD      D,$8A           
6239: 96             SUB     (HL)            
623A: 91             SUB     C               
623B: 48             LD      C,B             
623C: 91             SUB     C               
623D: 7A             LD      A,D             
623E: 83             ADD     A,E             
623F: 17             RLA                     
6240: F3             DI                      
6241: 5F             LD      E,A             
6242: 56             LD      D,(HL)          
6243: D1             POP     DE              
6244: 03             INC     BC              
6245: 71             LD      (HL),C          
6246: 39             ADD     HL,SP           
6247: 17             RLA                     
6248: DB A4          IN      A,($A4)         
624A: 7B             LD      A,E             
624B: 50             LD      D,B             
624C: 95             SUB     L               
624D: 73             LD      (HL),E          
624E: 4F             LD      C,A             
624F: 15             DEC     D               
6250: 73             LD      (HL),E          
6251: 62             LD      H,D             
6252: 6B             LD      L,E             
6253: BF             CP      A               
6254: 5F             LD      E,A             
6255: BE             CP      (HL)            
6256: D7             RST     0X10            
6257: 14             INC     D               
6258: 43             LD      B,E             
6259: 7A             LD      A,D             
625A: CF             RST     0X08            
625B: 98             SBC     B               
625C: 9F             SBC     A               
625D: 15             DEC     D               
625E: D5             PUSH    DE              
625F: 15             DEC     D               
6260: F7             RST     0X30            
6261: 17             RLA                     
6262: 33             INC     SP              
6263: 49             LD      C,C             
6264: AB             XOR     E               
6265: 98             SBC     B               
6266: 55             LD      D,L             
6267: 45             LD      B,L             
6268: EB             EX      DE,HL           
6269: BF             CP      A               
626A: 73             LD      (HL),E          
626B: 7B             LD      A,E             
626C: C5             PUSH    BC              
626D: 7E             LD      A,(HL)          
626E: B6             OR      (HL)            
626F: 85             ADD     A,L             
6270: 4A             LD      C,D             
6271: F4 56 5E       CALL    P,$5E56         
6274: 38 C6          JR      C,$623C         
6276: CA B5 4B       JP      Z,$4BB5         
6279: 7B             LD      A,E             
627A: E3             EX      (SP),HL         
627B: 72             LD      (HL),D          
627C: 16 58          LD      D,$58           
627E: 73             LD      (HL),E          
627F: A1             AND     C               
6280: 33             INC     SP              
6281: B1             OR      C               
6282: C7             RST     0X00            
6283: DE FC          SBC     $FC             
6285: ED                                  
6286: EE 72          XOR     $72             
6288: 69             LD      L,C             
6289: 8D             ADC     A,L             
628A: BB             CP      E               
628B: 15             DEC     D               
628C: 5B             LD      E,E             
628D: 48             LD      C,B             
628E: 5F             LD      E,A             
628F: BE             CP      (HL)            
6290: 84             ADD     A,H             
6291: 15             DEC     D               
6292: 96             SUB     (HL)            
6293: 5F             LD      E,A             
6294: A9             XOR     C               
6295: 15             DEC     D               
6296: 03             INC     BC              
6297: C4 F9 98       CALL    NZ,$98F9        
629A: 99             SBC     C               
629B: 16 B9          LD      D,$B9           
629D: 14             INC     D               
629E: 4D             LD      C,L             
629F: 98             SBC     B               
62A0: D3 14          OUT     ($14),A         
62A2: 8A             ADC     A,D             
62A3: 96             SUB     (HL)            
62A4: BE             CP      (HL)            
62A5: 9F             SBC     A               
62A6: 67             LD      H,A             
62A7: 16 10          LD      D,$10           
62A9: EE CE          XOR     $CE             
62AB: 9C             SBC     H               
62AC: 5D             LD      E,L             
62AD: 9E             SBC     (HL)            
62AE: C5             PUSH    BC              
62AF: B5             OR      L               
62B0: 83             ADD     A,E             
62B1: 48             LD      C,B             
62B2: 75             LD      (HL),L          
62B3: B1             OR      C               
62B4: 66             LD      H,(HL)          
62B5: 7B             LD      A,E             
62B6: 67             LD      H,A             
62B7: 16 D9          LD      D,$D9           
62B9: 06 D6          LD      B,$D6           
62BB: 47             LD      B,A             
62BC: 0E EE          LD      C,$EE           
62BE: 73             LD      (HL),E          
62BF: 62             LD      H,D             
62C0: 1B             DEC     DE              
62C1: 92             SUB     D               
62C2: 29             ADD     HL,HL           
62C3: B8             CP      B               
62C4: DB CE          IN      A,($CE)         
62C6: 19             ADD     HL,DE           
62C7: A1             AND     C               
62C8: BB             CP      E               
62C9: 15             DEC     D               
62CA: 10 53          DJNZ    $631F           
62CC: 77             LD      (HL),A          
62CD: 15             DEC     D               
62CE: 17             RLA                     
62CF: BC             CP      H               
62D0: C4 B5 02       CALL    NZ,$02B5        
62D3: A1             AND     C               
62D4: C7             RST     0X00            
62D5: 16 11          LD      D,$11           
62D7: BC             CP      H               
62D8: 96             SUB     (HL)            
62D9: 64             LD      H,H             
62DA: 95             SUB     L               
62DB: 73             LD      (HL),E          
62DC: E6 16          AND     $16             
62DE: D7             RST     0X10            
62DF: 46             LD      B,(HL)          
62E0: E3             EX      (SP),HL         
62E1: 06 DB          LD      B,$DB           
62E3: 72             LD      (HL),D          
62E4: 69             LD      L,C             
62E5: 4D             LD      C,L             
62E6: 9D             SBC     L               
62E7: 7A             LD      A,D             
62E8: 04             INC     B               
62E9: 18 79          JR      $6364           
62EB: 79             LD      A,C             
62EC: 90             SUB     B               
62ED: 8C             ADC     A,H             
62EE: 5B             LD      E,E             
62EF: 70             LD      (HL),B          
62F0: 1E 2A          LD      E,$2A           
62F2: 2B             DEC     HL              
62F3: 04             INC     B               
62F4: 80             ADD     A,B             
62F5: 93             SUB     E               
62F6: 00             NOP                     
62F7: 00             NOP                     
62F8: 90             SUB     B               
62F9: 03             INC     BC              
62FA: 36 04          LD      (HL),$04        
62FC: 34             INC     (HL)            
62FD: 87             ADD     A,A             
62FE: 74             LD      (HL),H          
62FF: 90             SUB     B               
6300: 5A             LD      E,D             
6301: 4B             LD      C,E             
6302: 77             LD      (HL),A          
6303: D9             EXX                     
6304: B5             OR      L               
6305: 75             LD      (HL),L          
6306: B1             OR      C               
6307: 03             INC     BC              
6308: BF             CP      A               
6309: AB             XOR     E               
630A: 98             SBC     B               
630B: 56             LD      D,(HL)          
630C: D1             POP     DE              
630D: 0A             LD      A,(BC)          
630E: 71             LD      (HL),C          
630F: 4B             LD      C,E             
6310: 7B             LD      A,E             
6311: 0C             INC     C               
6312: BA             CP      D               
6313: D6 47          SUB     $47             
6315: EB             EX      DE,HL           
6316: 15             DEC     D               
6317: 97             SUB     A               
6318: 54             LD      D,H             
6319: 9B             SBC     E               
631A: C1             POP     BC              
631B: FD 1B          DEC     DE              
631D: F3             DI                      
631E: 8C             ADC     A,H             
631F: 5B             LD      E,E             
6320: 4D             LD      C,L             
6321: 36 A1          LD      (HL),$A1        
6323: B8             CP      B               
6324: 16 82          LD      D,$82           
6326: 17             RLA                     
6327: 4B             LD      C,E             
6328: 7B             LD      A,E             
6329: 83             ADD     A,E             
632A: 7A             LD      A,D             
632B: EB             EX      DE,HL           
632C: 99             SBC     C               
632D: 8F             ADC     A,A             
632E: BE             CP      (HL)            
632F: EC 5D 02       CALL    PE,$025D        
6332: 05             DEC     B               
6333: 87             ADD     A,A             
6334: 74             LD      (HL),H          
6335: 90             SUB     B               
6336: 5A             LD      E,D             
6337: 49             LD      C,C             
6338: 08             EX      AF,AF'          
6339: 45             LD      B,L             
633A: 0E 43          LD      C,$43           
633C: 0D             DEC     C               
633D: 04             INC     B               
633E: 9C             SBC     H               
633F: 1C             INC     E               
6340: 2C             INC     L               
6341: 9E             SBC     (HL)            
6342: 0B             DEC     BC              
6343: 3B             DEC     SP              
6344: 05             DEC     B               
6345: 08             EX      AF,AF'          
6346: 1A             LD      A,(DE)          
6347: 1F             RRA                     
6348: 18 87          JR      $62D1           
634A: 74             LD      (HL),H          
634B: 90             SUB     B               
634C: 5A             LD      E,D             
634D: 4F             LD      C,A             
634E: 77             LD      (HL),A          
634F: 64             LD      H,H             
6350: C5             PUSH    BC              
6351: F5             PUSH    AF              
6352: 8B             ADC     A,E             
6353: FC ED A3       CALL    M,$A3ED         
6356: 48             LD      C,B             
6357: 6B             LD      L,E             
6358: 16 F6          LD      D,$F6           
635A: 9A             SBC     D               
635B: 50             LD      D,B             
635C: 5E             LD      E,(HL)          
635D: 8F             ADC     A,A             
635E: A1             AND     C               
635F: DC F9 10       CALL    C,$10F9         
6362: 1C             INC     E               
6363: 1F             RRA                     
6364: 1A             LD      A,(DE)          
6365: 87             ADD     A,A             
6366: 74             LD      (HL),H          
6367: 90             SUB     B               
6368: 5A             LD      E,D             
6369: 46             LD      B,(HL)          
636A: 77             LD      (HL),A          
636B: DE 5F          SBC     $5F             
636D: 2F             CPL                     
636E: 49             LD      C,C             
636F: 33             INC     SP              
6370: BB             CP      E               
6371: FD 1B          DEC     DE              
6373: 5B             LD      E,E             
6374: CA 47 48       JP      Z,$4847         
6377: E6 A0          AND     $A0             
6379: 81             ADD     A,C             
637A: 15             DEC     D               
637B: 0B             DEC     BC              
637C: BC             CP      H               
637D: AC             XOR     H               
637E: BB             CP      E               
637F: 07             RLCA                    
6380: 01 AB 0B       LD      BC,$0BAB        
6383: 01 9A 09       LD      BC,$099A        
6386: 02             LD      (BC),A          
6387: 46             LD      B,(HL)          
6388: 46             LD      B,(HL)          
6389: 01 81 CA       LD      BC,$CA81        
638C: 8E             ADC     A,(HL)          
638D: 00             NOP                     
638E: 90             SUB     B               
638F: 03             INC     BC              
6390: 60             LD      H,B             
6391: 04             INC     B               
6392: 5E             LD      E,(HL)          
6393: 5F             LD      E,A             
6394: BE             CP      (HL)            
6395: 5B             LD      E,E             
6396: B1             OR      C               
6397: 4B             LD      C,E             
6398: 7B             LD      A,E             
6399: 58             LD      E,B             
639A: 45             LD      B,L             
639B: 43             LD      B,E             
639C: 62             LD      H,D             
639D: 3B             DEC     SP              
639E: 16 B7          LD      D,$B7           
63A0: B1             OR      C               
63A1: 01 18 90       LD      BC,$9018        
63A4: 91             SUB     C               
63A5: 0C             INC     C               
63A6: 15             DEC     D               
63A7: 65             LD      H,L             
63A8: 62             LD      H,D             
63A9: F3             DI                      
63AA: 5F             LD      E,A             
63AB: 83             ADD     A,E             
63AC: 7A             LD      A,D             
63AD: 57             LD      D,A             
63AE: 45             LD      B,L             
63AF: 08             EX      AF,AF'          
63B0: 99             SBC     C               
63B1: B7             OR      A               
63B2: A0             AND     B               
63B3: 9F             SBC     A               
63B4: 15             DEC     D               
63B5: 7F             LD      A,A             
63B6: B1             OR      C               
63B7: 5A             LD      E,D             
63B8: 17             RLA                     
63B9: 4E             LD      C,(HL)          
63BA: 5E             LD      E,(HL)          
63BB: 3D             DEC     A               
63BC: A0             AND     B               
63BD: CE B5          ADC     $B5             
63BF: 17             RLA                     
63C0: 7A             LD      A,D             
63C1: 82             ADD     A,D             
63C2: 17             RLA                     
63C3: 54             LD      D,H             
63C4: 5E             LD      E,(HL)          
63C5: C6 9F          ADD     $9F             
63C7: 23             INC     HL              
63C8: 62             LD      H,D             
63C9: F4 59 7B       CALL    P,$7B59         
63CC: 50             LD      D,B             
63CD: A7             AND     A               
63CE: AD             XOR     L               
63CF: A7             AND     A               
63D0: 61             LD      H,C             
63D1: 5A             LD      E,D             
63D2: 17             RLA                     
63D3: 4A             LD      C,D             
63D4: 5E             LD      E,(HL)          
63D5: 4B             LD      C,E             
63D6: 49             LD      C,C             
63D7: 4C             LD      C,H             
63D8: 45             LD      B,L             
63D9: 79             LD      A,C             
63DA: 47             LD      B,A             
63DB: F3             DI                      
63DC: 5F             LD      E,A             
63DD: 53             LD      D,E             
63DE: B7             OR      A               
63DF: 8C             ADC     A,H             
63E0: AF             XOR     A               
63E1: 66             LD      H,(HL)          
63E2: C6 AF          ADD     $AF             
63E4: 14             INC     D               
63E5: 89             ADC     A,C             
63E6: 8D             ADC     A,L             
63E7: 9F             SBC     A               
63E8: 15             DEC     D               
63E9: 8A             ADC     A,D             
63EA: AF             XOR     A               
63EB: D4 47 90       CALL    NC,$9047        
63EE: 8C             ADC     A,H             
63EF: DB 63          IN      A,($63)         
63F1: 02             LD      (BC),A          
63F2: 06 5F          LD      B,$5F           
63F4: BE             CP      (HL)            
63F5: 9F             SBC     A               
63F6: 16 97          LD      D,$97           
63F8: B3             OR      E               
63F9: 0B             DEC     BC              
63FA: 01 9A 07       LD      BC,$079A        
63FD: 01 AB 08       LD      BC,$08AB        
6400: 81             ADD     A,C             
6401: 50             LD      D,B             
6402: 0D             DEC     C               
6403: 81             ADD     A,C             
6404: 4D             LD      C,L             
6405: 01 13 0E       LD      BC,$0E13        
6408: 81             ADD     A,C             
6409: 48             LD      C,B             
640A: 0D             DEC     C               
640B: 71             LD      (HL),C          
640C: 0A             LD      A,(BC)          
640D: 03             INC     BC              
640E: 1F             RRA                     
640F: 6D             LD      L,L             
6410: 1F             RRA                     
6411: B8             CP      B               
6412: 8F             ADC     A,A             
6413: 17             RLA                     
6414: DD                                  
6415: B2             OR      D               
6416: 89             ADC     A,C             
6417: 17             RLA                     
6418: 14             INC     D               
6419: D0             RET     NC              
641A: 1B             DEC     DE              
641B: 58             LD      E,B             
641C: 1B             DEC     DE              
641D: A1             AND     C               
641E: 8E             ADC     A,(HL)          
641F: 48             LD      C,B             
6420: 53             LD      D,E             
6421: 17             RLA                     
6422: 6E             LD      L,(HL)          
6423: DF             RST     0X18            
6424: 79             LD      A,C             
6425: 13             INC     DE              
6426: AB             XOR     E               
6427: 70             LD      (HL),B          
6428: C7             RST     0X00            
6429: DE 77          SBC     $77             
642B: 16 F3          LD      D,$F3           
642D: B9             CP      C               
642E: 5B             LD      E,E             
642F: 4D             LD      C,L             
6430: F4 72 48       CALL    P,$4872         
6433: 5E             LD      E,(HL)          
6434: A3             AND     E               
6435: A0             AND     B               
6436: EF             RST     0X28            
6437: BF             CP      A               
6438: 87             ADD     A,A             
6439: 49             LD      C,C             
643A: 9E             SBC     (HL)            
643B: 61             LD      H,C             
643C: 4C             LD      C,H             
643D: F4 66 C6       CALL    P,$C666         
6440: E1             POP     HL              
6441: 14             INC     D               
6442: 1B             DEC     DE              
6443: 92             SUB     D               
6444: 09             ADD     HL,BC           
6445: B2             OR      D               
6446: 33             INC     SP              
6447: 75             LD      (HL),L          
6448: 4F             LD      C,A             
6449: A1             AND     C               
644A: 8A             ADC     A,D             
644B: AF             XOR     A               
644C: 2F             CPL                     
644D: 62             LD      H,D             
644E: FF             RST     0X38            
644F: F9             LD      SP,HL           
6450: 95             SUB     L               
6451: 19             ADD     HL,DE           
6452: DB 72          IN      A,($72)         
6454: B5             OR      L               
6455: 6C             LD      L,H             
6456: 74             LD      (HL),H          
6457: C0             RET     NZ              
6458: 4B             LD      C,E             
6459: 62             LD      H,D             
645A: 89             ADC     A,C             
645B: BF             CP      A               
645C: 2E 49          LD      L,$49           
645E: 61             LD      H,C             
645F: 17             RLA                     
6460: 36 92          LD      (HL),$92        
6462: 90             SUB     B               
6463: 73             LD      (HL),E          
6464: D9             EXX                     
6465: 6A             LD      L,D             
6466: 85             ADD     A,L             
6467: 73             LD      (HL),E          
6468: 0E 71          LD      C,$71           
646A: 3D             DEC     A               
646B: A0             AND     B               
646C: CE B5          ADC     $B5             
646E: 17             RLA                     
646F: 7A             LD      A,D             
6470: 90             SUB     B               
6471: 14             INC     D               
6472: 2E 15          LD      L,$15           
6474: E6 5F          AND     $5F             
6476: 05             DEC     B               
6477: B2             OR      D               
6478: E1             POP     HL              
6479: 14             INC     D               
647A: DA C3 2E       JP      C,$2EC3         
647D: 0D             DEC     C               
647E: 80             ADD     A,B             
647F: D2 1F 73       JP      NC,$731F        
6482: 91             SUB     C               
6483: 1E A4          LD      E,$A4           
6485: C2 50 5E       JP      NZ,$5E50        
6488: F3             DI                      
6489: A0             AND     B               
648A: 41             LD      B,C             
648B: 55             LD      D,L             
648C: F4 A4 83       CALL    P,$83A4         
648F: 49             LD      C,C             
6490: CF             RST     0X08            
6491: 98             SBC     B               
6492: DC F9 15       CALL    C,$15F9         
6495: EE 55          XOR     $55             
6497: 4A             LD      C,D             
6498: 82             ADD     A,D             
6499: 17             RLA                     
649A: 50             LD      D,B             
649B: 5E             LD      E,(HL)          
649C: 3D             DEC     A               
649D: C6 43          ADD     $43             
649F: 5E             LD      E,(HL)          
64A0: D5             PUSH    DE              
64A1: B5             OR      L               
64A2: DB 72          IN      A,($72)         
64A4: 70             LD      (HL),B          
64A5: 8E             ADC     A,(HL)          
64A6: B5             OR      L               
64A7: 6C             LD      L,H             
64A8: 85             ADD     A,L             
64A9: 14             INC     D               
64AA: 05             DEC     B               
64AB: B3             OR      E               
64AC: D6 B5          SUB     $B5             
64AE: DB 72          IN      A,($72)         
64B0: 01 B3 43       LD      BC,$43B3        
64B3: 90             SUB     B               
64B4: 33             INC     SP              
64B5: 98             SBC     B               
64B6: 45             LD      B,L             
64B7: BD             CP      L               
64B8: BF             CP      A               
64B9: 86             ADD     A,(HL)          
64BA: DB B5          IN      A,($B5)         
64BC: 3F             CCF                     
64BD: A1             AND     C               
64BE: 5A             LD      E,D             
64BF: 17             RLA                     
64C0: 46             LD      B,(HL)          
64C1: 5E             LD      E,(HL)          
64C2: C9             RET                     
64C3: B0             OR      B               
64C4: DB B5          IN      A,($B5)         
64C6: 1B             DEC     DE              
64C7: A1             AND     C               
64C8: 6B             LD      L,E             
64C9: BF             CP      A               
64CA: 5F             LD      E,A             
64CB: BE             CP      (HL)            
64CC: E1             POP     HL              
64CD: 14             INC     D               
64CE: DA C3 90       JP      C,$90C3         
64D1: 14             INC     D               
64D2: 15             DEC     D               
64D3: 58             LD      E,B             
64D4: EB             EX      DE,HL           
64D5: BF             CP      A               
64D6: 0B             DEC     BC              
64D7: A7             AND     A               
64D8: C7             RST     0X00            
64D9: DE D0          SBC     $D0             
64DB: 15             DEC     D               
64DC: 56             LD      D,(HL)          
64DD: F4 F0 72       CALL    P,$72F0         
64E0: 5A             LD      E,D             
64E1: 17             RLA                     
64E2: 52             LD      D,D             
64E3: 5E             LD      E,(HL)          
64E4: 46             LD      B,(HL)          
64E5: C5             PUSH    BC              
64E6: C3 B5 91       JP      $91B5           
64E9: 96             SUB     (HL)            
64EA: D0             RET     NC              
64EB: 92             SUB     D               
64EC: 35             DEC     (HL)            
64ED: A1             AND     C               
64EE: 3F             CCF                     
64EF: 16 74          LD      D,$74           
64F1: CA 90 14       JP      Z,$1490         
64F4: 44             LD      B,H             
64F5: 0E 24          LD      C,$24           
64F7: 03             INC     BC              
64F8: 13             INC     DE              
64F9: 3A 1F 1F       LD      A,($1F1F)       
64FC: C7             RST     0X00            
64FD: DE 3A          SBC     $3A             
64FF: 15             DEC     D               
6500: F4 A4 30       CALL    P,$30A4         
6503: 79             LD      A,C             
6504: 9B             SBC     E               
6505: 53             LD      D,E             
6506: 5F             LD      E,A             
6507: BE             CP      (HL)            
6508: AE             XOR     (HL)            
6509: 17             RLA                     
650A: 8F             ADC     A,A             
650B: BE             CP      (HL)            
650C: 7F             LD      A,A             
650D: 49             LD      C,C             
650E: 89             ADC     A,C             
650F: 14             INC     D               
6510: 23             INC     HL              
6511: A0             AND     B               
6512: CF             RST     0X08            
6513: 06 2D          LD      B,$2D           
6515: 62             LD      H,D             
6516: 5F             LD      E,A             
6517: 79             LD      A,C             
6518: 13             INC     DE              
6519: 8D             ADC     A,L             
651A: 2C             INC     L               
651B: 1F             RRA                     
651C: 0A             LD      A,(BC)          
651D: C7             RST     0X00            
651E: DE DB          SBC     $DB             
6520: 16 CB          LD      D,$CB           
6522: B9             CP      C               
6523: 36 A1          LD      (HL),$A1        
6525: FF             RST     0X38            
6526: F9             LD      SP,HL           
6527: 2C             INC     L               
6528: 13             INC     DE              
6529: 19             ADD     HL,DE           
652A: 88             ADC     A,B             
652B: 17             RLA                     
652C: 1B             DEC     DE              
652D: 8E             ADC     A,(HL)          
652E: 17             RLA                     
652F: 41             LD      B,C             
6530: 8C             ADC     A,H             
6531: 1C             INC     E               
6532: 05             DEC     B               
6533: 0E 03          LD      C,$03           
6535: 15             DEC     D               
6536: 02             LD      (BC),A          
6537: 29             ADD     HL,HL           
6538: 1C             INC     E               
6539: 06 0E          LD      B,$0E           
653B: 04             INC     B               
653C: 14             INC     D               
653D: 15             DEC     D               
653E: 02             LD      (BC),A          
653F: 29             ADD     HL,HL           
6540: 1F             RRA                     
6541: 10 C7          DJNZ    $650A           
6543: DE 99          SBC     $99             
6545: 14             INC     D               
6546: 17             RLA                     
6547: 48             LD      C,B             
6548: 8B             ADC     A,E             
6549: 96             SUB     (HL)            
654A: 9B             SBC     E               
654B: 96             SUB     (HL)            
654C: 34             INC     (HL)            
654D: A1             AND     C               
654E: D7             RST     0X10            
654F: 14             INC     D               
6550: 17             RLA                     
6551: 8D             ADC     A,L             
6552: 09             ADD     HL,BC           
6553: 02             LD      (BC),A          
6554: 46             LD      B,(HL)          
6555: 46             LD      B,(HL)          
6556: 07             RLCA                    
6557: 81             ADD     A,C             
6558: AE             XOR     (HL)            
6559: 00             NOP                     
655A: 00             NOP                     
655B: 90             SUB     B               
655C: 03             INC     BC              
655D: 01 9F 02       LD      BC,$029F        
6560: 07             RLCA                    
6561: 5F             LD      E,A             
6562: BE             CP      (HL)            
6563: 09             ADD     HL,BC           
6564: 15             DEC     D               
6565: 09             ADD     HL,BC           
6566: 56             LD      D,(HL)          
6567: 52             LD      D,D             
6568: 08             EX      AF,AF'          
6569: 81             ADD     A,C             
656A: 95             SUB     L               
656B: 0E 81          LD      C,$81           
656D: 92             SUB     D               
656E: 0D             DEC     C               
656F: 1C             INC     E               
6570: 14             INC     D               
6571: 01 13 9B       LD      BC,$9B13        
6574: 1F             RRA                     
6575: 15             DEC     D               
6576: C7             RST     0X00            
6577: DE 9F          SBC     $9F             
6579: 15             DEC     D               
657A: 23             INC     HL              
657B: 49             LD      C,C             
657C: 50             LD      D,B             
657D: 45             LD      B,L             
657E: 55             LD      D,L             
657F: 9F             SBC     A               
6580: 43             LD      B,E             
6581: 5E             LD      E,(HL)          
6582: 33             INC     SP              
6583: 98             SBC     B               
6584: C7             RST     0X00            
6585: DE 99          SBC     $99             
6587: 16 85          LD      D,$85           
6589: BE             CP      (HL)            
658A: 45             LD      B,L             
658B: 9F             SBC     A               
658C: 0D             DEC     C               
658D: 81             ADD     A,C             
658E: 71             LD      (HL),C          
658F: 01 13 1F       LD      BC,$1F13        
6592: 0C             INC     C               
6593: 5F             LD      E,A             
6594: BE             CP      (HL)            
6595: 09             ADD     HL,BC           
6596: 15             DEC     D               
6597: 09             ADD     HL,BC           
6598: 56             LD      D,(HL)          
6599: 95             SUB     L               
659A: AF             XOR     A               
659B: 55             LD      D,L             
659C: 4A             LD      C,D             
659D: FB             EI                      
659E: ED                                  
659F: 0B             DEC     BC              
65A0: 81             ADD     A,C             
65A1: 5E             LD      E,(HL)          
65A2: 05             DEC     B               
65A3: 33             INC     SP              
65A4: 42             LD      B,D             
65A5: 1F             RRA                     
65A6: 40             LD      B,B             
65A7: 91             SUB     C               
65A8: 1E 43          LD      E,$43           
65AA: C2 5B B1       JP      NZ,$B15B        
65AD: 06 9A          LD      B,$9A           
65AF: AF             XOR     A               
65B0: 14             INC     D               
65B1: 91             SUB     C               
65B2: 7A             LD      A,D             
65B3: 7B             LD      A,E             
65B4: 14             INC     D               
65B5: 41             LD      B,C             
65B6: 6E             LD      L,(HL)          
65B7: 0E 58          LD      C,$58           
65B9: 8E             ADC     A,(HL)          
65BA: 7B             LD      A,E             
65BB: DB 8B          IN      A,($8B)         
65BD: 56             LD      D,(HL)          
65BE: A4             AND     H               
65BF: 30 79          JR      NC,$663A        
65C1: AB             XOR     E               
65C2: BB             CP      E               
65C3: 09             ADD     HL,BC           
65C4: 9A             SBC     D               
65C5: 2F             CPL                     
65C6: 17             RLA                     
65C7: 74             LD      (HL),H          
65C8: C0             RET     NZ              
65C9: 96             SUB     (HL)            
65CA: 96             SUB     (HL)            
65CB: DB 9C          IN      A,($9C)         
65CD: 34             INC     (HL)            
65CE: A1             AND     C               
65CF: D7             RST     0X10            
65D0: 14             INC     D               
65D1: 16 8D          LD      D,$8D           
65D3: C4 16 51       CALL    NZ,$5116        
65D6: 18 59          JR      $6631           
65D8: C2 46 7A       JP      NZ,$7A46        
65DB: 8F             ADC     A,A             
65DC: 16 F3          LD      D,$F3           
65DE: 5F             LD      E,A             
65DF: 4E             LD      C,(HL)          
65E0: 45             LD      B,L             
65E1: 39             ADD     HL,SP           
65E2: 9E             SBC     (HL)            
65E3: 7F             LD      A,A             
65E4: BF             CP      A               
65E5: EC DA 66       CALL    PE,$66DA        
65E8: 20 1F          JR      NZ,$6609        
65EA: 1E FB          LD      E,$FB           
65EC: 1B             DEC     DE              
65ED: B9             CP      C               
65EE: 6E             LD      L,(HL)          
65EF: D6 CE          SUB     $CE             
65F1: 2F             CPL                     
65F2: 7B             LD      A,E             
65F3: 11 58 86       LD      DE,$8658        
65F6: 64             LD      H,H             
65F7: 8E             ADC     A,(HL)          
65F8: 5F             LD      E,A             
65F9: 91             SUB     C               
65FA: 7A             LD      A,D             
65FB: FB             EI                      
65FC: 17             RLA                     
65FD: 53             LD      D,E             
65FE: BE             CP      (HL)            
65FF: C7             RST     0X00            
6600: DE D0          SBC     $D0             
6602: 15             DEC     D               
6603: 74             LD      (HL),H          
6604: 66             LD      H,(HL)          
6605: C4 7A 6C       CALL    NZ,$6C7A        
6608: B5             OR      L               
6609: 99             SBC     C               
660A: 22 1F 20       LD      ($201F),HL      
660D: 3A 1E 73       LD      A,($731E)       
6610: 49             LD      C,C             
6611: 2F             CPL                     
6612: 49             LD      C,C             
6613: 51             LD      D,C             
6614: 18 46          JR      $665C           
6616: C2 50 9F       JP      NZ,$9F50        
6619: CA 6A 2F       JP      Z,$2F6A         
661C: 62             LD      H,D             
661D: 89             ADC     A,C             
661E: 00             NOP                     
661F: D9             EXX                     
6620: 9C             SBC     H               
6621: F4 72 5B       CALL    P,$5B72         
6624: 5E             LD      E,(HL)          
6625: 1B             DEC     DE              
6626: A1             AND     C               
6627: 6E             LD      L,(HL)          
6628: 4D             LD      C,L             
6629: 11 A0 E3       LD      DE,$E3A0        
662C: 06 FF          LD      B,$FF           
662E: 80             ADD     A,B             
662F: D0             RET     NC              
6630: 0D             DEC     C               
6631: 80             ADD     A,B             
6632: CD 1F 80       CALL    $801F           
6635: B4             OR      H               
6636: FD 1B          DEC     DE              
6638: 43             LD      B,E             
6639: 90             SUB     B               
663A: 6B             LD      L,E             
663B: 68             LD      L,B             
663C: F3             DI                      
663D: 78             LD      A,B             
663E: 9F             SBC     A               
663F: 77             LD      (HL),A          
6640: 81             ADD     A,C             
6641: 15             DEC     D               
6642: 91             SUB     C               
6643: 7A             LD      A,D             
6644: 89             ADC     A,C             
6645: 17             RLA                     
6646: 9B             SBC     E               
6647: 15             DEC     D               
6648: 5B             LD      E,E             
6649: CA 6B BF       JP      Z,$BF6B         
664C: 58             LD      E,B             
664D: 6D             LD      L,L             
664E: 5B             LD      E,E             
664F: 5E             LD      E,(HL)          
6650: 1B             DEC     DE              
6651: A1             AND     C               
6652: 48             LD      C,B             
6653: 45             LD      B,L             
6654: 00             NOP                     
6655: B3             OR      E               
6656: 4E             LD      C,(HL)          
6657: BD             CP      L               
6658: 49             LD      C,C             
6659: 16 06          LD      D,$06           
665B: 4F             LD      C,A             
665C: FB             EI                      
665D: 9F             SBC     A               
665E: E3             EX      (SP),HL         
665F: 06 DB          LD      B,$DB           
6661: 72             LD      (HL),D          
6662: 03             INC     BC              
6663: BA             CP      D               
6664: A5             AND     L               
6665: 54             LD      D,H             
6666: 51             LD      D,C             
6667: 18 59          JR      $66C2           
6669: C2 82 7B       JP      NZ,$7B82        
666C: A3             AND     E               
666D: 15             DEC     D               
666E: CA B5 E9       JP      Z,$E9B5         
6671: DE 90          SBC     $90             
6673: 14             INC     D               
6674: 1B             DEC     DE              
6675: 58             LD      E,B             
6676: 1B             DEC     DE              
6677: A1             AND     C               
6678: 55             LD      D,L             
6679: A4             AND     H               
667A: D1             POP     DE              
667B: B5             OR      L               
667C: 97             SUB     A               
667D: C6 FA          ADD     $FA             
667F: 17             RLA                     
6680: 83             ADD     A,E             
6681: 61             LD      H,C             
6682: C7             RST     0X00            
6683: DE 99          SBC     $99             
6685: 14             INC     D               
6686: 17             RLA                     
6687: 48             LD      C,B             
6688: F3             DI                      
6689: 9B             SBC     E               
668A: C7             RST     0X00            
668B: DE 4F          SBC     $4F             
668D: 15             DEC     D               
668E: 33             INC     SP              
668F: 61             LD      H,C             
6690: 3F             CCF                     
6691: B9             CP      C               
6692: FA 62 73       JP      M,$7362         
6695: 49             LD      C,C             
6696: 8E             ADC     A,(HL)          
6697: 7A             LD      A,D             
6698: 50             LD      D,B             
6699: 79             LD      A,C             
669A: 2F             CPL                     
669B: 62             LD      H,D             
669C: B3             OR      E               
669D: 9A             SBC     D               
669E: 6B             LD      L,E             
669F: BF             CP      A               
66A0: C7             RST     0X00            
66A1: DE 95          SBC     $95             
66A3: AF             XOR     A               
66A4: 3C             INC     A               
66A5: C6 30          ADD     $30             
66A7: A1             AND     C               
66A8: 90             SUB     B               
66A9: 5A             LD      E,D             
66AA: EF             RST     0X28            
66AB: 6E             LD      L,(HL)          
66AC: 51             LD      D,C             
66AD: 18 50          JR      $66FF           
66AF: C2 03 A1       JP      NZ,$A103        
66B2: 9B             SBC     E               
66B3: 53             LD      D,E             
66B4: 89             ADC     A,C             
66B5: 4E             LD      C,(HL)          
66B6: 73             LD      (HL),E          
66B7: 9E             SBC     (HL)            
66B8: 03             INC     BC              
66B9: A0             AND     B               
66BA: C7             RST     0X00            
66BB: DE 89          SBC     $89             
66BD: AF             XOR     A               
66BE: 80             ADD     A,B             
66BF: A1             AND     C               
66C0: 04             INC     B               
66C1: EE 73          XOR     $73             
66C3: C6 73          ADD     $73             
66C5: 7B             LD      A,E             
66C6: 77             LD      (HL),A          
66C7: 5B             LD      E,E             
66C8: 05             DEC     B               
66C9: B9             CP      C               
66CA: 15             DEC     D               
66CB: BC             CP      H               
66CC: 2F             CPL                     
66CD: 60             LD      H,B             
66CE: 89             ADC     A,C             
66CF: 17             RLA                     
66D0: B9             CP      C               
66D1: 14             INC     D               
66D2: 5F             LD      E,A             
66D3: BE             CP      (HL)            
66D4: 9B             SBC     E               
66D5: AF             XOR     A               
66D6: 3F             CCF                     
66D7: A1             AND     C               
66D8: 51             LD      D,C             
66D9: 18 48          JR      $6723           
66DB: C2 2E 60       JP      NZ,$602E        
66DE: 43             LD      B,E             
66DF: 16 9B          LD      D,$9B           
66E1: 85             ADD     A,L             
66E2: 10 D0          DJNZ    $66B4           
66E4: F4 59 91       CALL    P,$9159         
66E7: 7A             LD      A,D             
66E8: FF             RST     0X38            
66E9: F9             LD      SP,HL           
66EA: 1C             INC     E               
66EB: 05             DEC     B               
66EC: 0E 03          LD      C,$03           
66EE: 15             DEC     D               
66EF: 02             LD      (BC),A          
66F0: 29             ADD     HL,HL           
66F1: 1C             INC     E               
66F2: 06 0E          LD      B,$0E           
66F4: 04             INC     B               
66F5: 14             INC     D               
66F6: 15             DEC     D               
66F7: 02             LD      (BC),A          
66F8: 29             ADD     HL,HL           
66F9: 2C             INC     L               
66FA: 13             INC     DE              
66FB: 17             RLA                     
66FC: 3A 13 19       LD      A,($1913)       
66FF: 88             ADC     A,B             
6700: 0B             DEC     BC              
6701: 01 9A 09       LD      BC,$099A        
6704: 02             LD      (BC),A          
6705: 46             LD      B,(HL)          
6706: 46             LD      B,(HL)          
6707: 25             DEC     H               
6708: 0C             INC     C               
6709: FF             RST     0X38            
670A: 00             NOP                     
670B: 80             ADD     A,B             
670C: 07             RLCA                    
670D: 01 A4 02       LD      BC,$02A4        
6710: 04             INC     B               
6711: 0E D0          LD      C,$D0           
6713: 0B             DEC     BC              
6714: 8E             ADC     A,(HL)          
6715: 2A 0B FF       LD      HL,($FF0B)      
6718: 00             NOP                     
6719: 80             ADD     A,B             
671A: 07             RLCA                    
671B: 01 A4 02       LD      BC,$02A4        
671E: 03             INC     BC              
671F: 01 B3 4D       LD      BC,$4DB3        
6722: 2B             DEC     HL              
6723: 09             ADD     HL,BC           
6724: FF             RST     0X38            
6725: 00             NOP                     
6726: 80             ADD     A,B             
6727: 02             LD      (BC),A          
6728: 04             INC     B               
6729: 89             ADC     A,C             
672A: 67             LD      H,A             
672B: A3             AND     E               
672C: A0             AND     B               
672D: 2C             INC     L               
672E: 08             EX      AF,AF'          
672F: FF             RST     0X38            
6730: 00             NOP                     
6731: 80             ADD     A,B             
6732: 02             LD      (BC),A          
6733: 03             INC     BC              
6734: 23             INC     HL              
6735: 63             LD      H,E             
6736: 54             LD      D,H             
6737: 30 0C          JR      NC,$6745        
6739: FF             RST     0X38            
673A: 00             NOP                     
673B: 80             ADD     A,B             
673C: 07             RLCA                    
673D: 01 A4 02       LD      BC,$02A4        
6740: 04             INC     B               
6741: 44             LD      B,H             
6742: 55             LD      D,L             
6743: 74             LD      (HL),H          
6744: 98             SBC     B               
6745: 33             INC     SP              
6746: 0D             DEC     C               
6747: FF             RST     0X38            
6748: 00             NOP                     
6749: 80             ADD     A,B             
674A: 07             RLCA                    
674B: 01 A4 02       LD      BC,$02A4        
674E: 05             DEC     B               
674F: 4E             LD      C,(HL)          
6750: 72             LD      (HL),D          
6751: B3             OR      E               
6752: 8E             ADC     A,(HL)          
6753: 59             LD      E,C             
6754: 36 0B          LD      (HL),$0B        
6756: FF             RST     0X38            
6757: 00             NOP                     
6758: 80             ADD     A,B             
6759: 02             LD      (BC),A          
675A: 06 9E          LD      B,$9E           
675C: 61             LD      H,C             
675D: D0             RET     NC              
675E: B0             OR      B               
675F: 9B             SBC     E               
6760: 53             LD      D,E             
6761: 3B             DEC     SP              
6762: 0A             LD      A,(BC)          
6763: FF             RST     0X38            
6764: 00             NOP                     
6765: 80             ADD     A,B             
6766: 02             LD      (BC),A          
6767: 05             DEC     B               
6768: AB             XOR     E               
6769: 53             LD      D,E             
676A: 90             SUB     B               
676B: 8C             ADC     A,H             
676C: 47             LD      B,A             
676D: 1F             RRA                     
676E: 09             ADD     HL,BC           
676F: 13             INC     DE              
6770: 00             NOP                     
6771: C0             RET     NZ              
6772: 02             LD      (BC),A          
6773: 04             INC     B               
6774: 50             LD      D,B             
6775: 72             LD      (HL),D          
6776: 0B             DEC     BC              
6777: 5C             LD      E,H             
6778: 20 03          JR      NZ,$677D        
677A: 00             NOP                     
677B: 00             NOP                     
677C: 80             ADD     A,B             
677D: 17             RLA                     
677E: 32 82 00       LD      ($0082),A       
6781: A0             AND     B               
6782: 03             INC     BC              
6783: 01 9D 07       LD      BC,$079D        
6786: 22 0D 20       LD      ($200D),HL      
6789: 0A             LD      A,(BC)          
678A: 15             DEC     D               
678B: 04             INC     B               
678C: 1C             INC     E               
678D: 2E 6F          LD      L,$6F           
678F: AB             XOR     E               
6790: A2             AND     D               
6791: 37             SCF                     
6792: 6E             LD      L,(HL)          
6793: C6 B5          ADD     $B5             
6795: 80             ADD     A,B             
6796: A1             AND     C               
6797: 9B             SBC     E               
6798: 15             DEC     D               
6799: 31 B1 47       LD      SP,$47B1        
679C: 18 5A          JR      $67F8           
679E: 53             LD      D,E             
679F: 16 EE          LD      D,$EE           
67A1: 66             LD      H,(HL)          
67A2: 49             LD      C,C             
67A3: 4B             LD      C,E             
67A4: 62             LD      H,D             
67A5: F8             RET     M               
67A6: 49             LD      C,C             
67A7: 31 C5 02       LD      SP,$02C5        
67AA: 06 8F          LD      B,$8F           
67AC: 4E             LD      C,(HL)          
67AD: 52             LD      D,D             
67AE: 5E             LD      E,(HL)          
67AF: 46             LD      B,(HL)          
67B0: 7A             LD      A,D             
67B1: 3C             INC     A               
67B2: 03             INC     BC              
67B3: 00             NOP                     
67B4: 00             NOP                     
67B5: 00             NOP                     
67B6: 16 80          LD      D,$80           
67B8: 85             ADD     A,L             
67B9: 82             ADD     A,D             
67BA: 00             NOP                     
67BB: 80             ADD     A,B             
67BC: 02             LD      (BC),A          
67BD: 05             DEC     B               
67BE: 66             LD      H,(HL)          
67BF: B1             OR      C               
67C0: 17             RLA                     
67C1: 16 59          LD      D,$59           
67C3: 01 01 13       LD      BC,$1301        
67C6: 07             RLCA                    
67C7: 76             HALT                    
67C8: 0E 74          LD      C,$74           
67CA: 0D             DEC     C               
67CB: 30 0A          JR      NC,$67D7        
67CD: 43             LD      B,E             
67CE: 09             ADD     HL,BC           
67CF: 16 03          LD      D,$03           
67D1: 82             ADD     A,D             
67D2: 3B             DEC     SP              
67D3: 03             INC     BC              
67D4: 00             NOP                     
67D5: 14             INC     D               
67D6: 17             RLA                     
67D7: 3B             DEC     SP              
67D8: 00             NOP                     
67D9: 17             RLA                     
67DA: 14             INC     D               
67DB: 13             INC     DE              
67DC: 04             INC     B               
67DD: 1E C7          LD      E,$C7           
67DF: DE 77          SBC     $77             
67E1: 15             DEC     D               
67E2: 16 BC          LD      D,$BC           
67E4: DB 72          IN      A,($72)         
67E6: BB             CP      E               
67E7: 85             ADD     A,L             
67E8: FB             EI                      
67E9: 17             RLA                     
67EA: 53             LD      D,E             
67EB: BE             CP      (HL)            
67EC: 5F             LD      E,A             
67ED: BE             CP      (HL)            
67EE: A9             XOR     C               
67EF: 15             DEC     D               
67F0: AF             XOR     A               
67F1: 9F             SBC     A               
67F2: 2F             CPL                     
67F3: 17             RLA                     
67F4: 0D             DEC     C               
67F5: 58             LD      E,B             
67F6: 3B             DEC     SP              
67F7: 63             LD      H,E             
67F8: 4D             LD      C,L             
67F9: BD             CP      L               
67FA: A7             AND     A               
67FB: 61             LD      H,C             
67FC: 0D             DEC     C               
67FD: 24             INC     H               
67FE: 0A             LD      A,(BC)          
67FF: 05             DEC     B               
6800: 04             INC     B               
6801: 20 C7          JR      NZ,$67CA        
6803: DE D3          SBC     $D3             
6805: 14             INC     D               
6806: 90             SUB     B               
6807: 96             SUB     (HL)            
6808: F3             DI                      
6809: A0             AND     B               
680A: 85             ADD     A,L             
680B: A6             AND     (HL)            
680C: 44             LD      B,H             
680D: B8             CP      B               
680E: FB             EI                      
680F: 8E             ADC     A,(HL)          
6810: 63             LD      H,E             
6811: B1             OR      C               
6812: 13             INC     DE              
6813: 54             LD      D,H             
6814: 9E             SBC     (HL)            
6815: 7A             LD      A,D             
6816: D6 9C          SUB     $9C             
6818: 56             LD      D,(HL)          
6819: 72             LD      (HL),D          
681A: 83             ADD     A,E             
681B: 17             RLA                     
681C: 7B             LD      A,E             
681D: 9B             SBC     E               
681E: 7E             LD      A,(HL)          
681F: 74             LD      (HL),H          
6820: EB             EX      DE,HL           
6821: 5D             LD      E,L             
6822: 0D             DEC     C               
6823: 1A             LD      A,(DE)          
6824: 0A             LD      A,(BC)          
6825: 43             LD      B,E             
6826: 04             INC     B               
6827: 14             INC     D               
6828: C7             RST     0X00            
6829: DE D3          SBC     $D3             
682B: 14             INC     D               
682C: E6 96          AND     $96             
682E: 77             LD      (HL),A          
682F: 15             DEC     D               
6830: 16 BC          LD      D,$BC           
6832: DB 72          IN      A,($72)         
6834: 66             LD      H,(HL)          
6835: B1             OR      C               
6836: 17             RLA                     
6837: 16 59          LD      D,$59           
6839: DB 82          IN      A,($82)         
683B: 7B             LD      A,E             
683C: A9             XOR     C               
683D: 8B             ADC     A,E             
683E: 08             EX      AF,AF'          
683F: 20 00          JR      NZ,$6841        
6841: 00             NOP                     
6842: A0             AND     B               
6843: 02             LD      (BC),A          
6844: 06 E3          LD      B,$E3           
6846: 59             LD      E,C             
6847: 06 58          LD      B,$58           
6849: EB             EX      DE,HL           
684A: 9E             SBC     (HL)            
684B: 03             INC     BC              
684C: 13             INC     DE              
684D: 04             INC     B               
684E: 11 5F BE       LD      DE,$BE5F        
6851: 5B             LD      E,E             
6852: B1             OR      C               
6853: 4B             LD      C,E             
6854: 7B             LD      A,E             
6855: 46             LD      B,(HL)          
6856: 45             LD      B,L             
6857: 86             ADD     A,(HL)          
6858: 5F             LD      E,A             
6859: 09             ADD     HL,BC           
685A: 15             DEC     D               
685B: CA 6A 2F       JP      Z,$2F6A         
685E: 62             LD      H,D             
685F: 2E 0B          LD      L,$0B           
6861: 42             LD      B,D             
6862: 00             NOP                     
6863: 00             NOP                     
6864: 8A             ADC     A,D             
6865: 07             RLCA                    
6866: 30 0D          JR      NC,$6875        
6868: 2E 0A          LD      L,$0A           
686A: 11 04 2A       LD      DE,$2A04        
686D: 5F             LD      E,A             
686E: BE             CP      (HL)            
686F: 57             LD      D,A             
6870: 17             RLA                     
6871: AF             XOR     A               
6872: 55             LD      D,L             
6873: 06 BC          LD      B,$BC           
6875: 44             LD      B,H             
6876: A0             AND     B               
6877: D5             PUSH    DE              
6878: 15             DEC     D               
6879: 66             LD      H,(HL)          
687A: 17             RLA                     
687B: DD                                  
687C: C3 5B F4       JP      $F45B           
687F: 1B             DEC     DE              
6880: A1             AND     C               
6881: 2F             CPL                     
6882: 49             LD      C,C             
6883: 99             SBC     C               
6884: 16 15          LD      D,$15           
6886: BC             CP      H               
6887: F9             LD      SP,HL           
6888: BF             CP      A               
6889: AB             XOR     E               
688A: 98             SBC     B               
688B: 99             SBC     C               
688C: 61             LD      H,C             
688D: 7A             LD      A,D             
688E: C4 89 17       CALL    NZ,$1789        
6891: C2 16 83       JP      NZ,$8316        
6894: 61             LD      H,C             
6895: 97             SUB     A               
6896: 7B             LD      A,E             
6897: 02             LD      (BC),A          
6898: 08             EX      AF,AF'          
6899: A5             AND     L               
689A: B7             OR      A               
689B: 76             HALT                    
689C: B1             OR      C               
689D: 09             ADD     HL,BC           
689E: 15             DEC     D               
689F: A3             AND     E               
68A0: A0             AND     B               
68A1: 01 01 3D       LD      BC,$3D01        
68A4: 0B             DEC     BC              
68A5: 76             HALT                    
68A6: 00             NOP                     
68A7: 00             NOP                     
68A8: 8A             ADC     A,D             
68A9: 02             LD      (BC),A          
68AA: 08             EX      AF,AF'          
68AB: 4B             LD      C,E             
68AC: A4             AND     H               
68AD: BF             CP      A               
68AE: 9A             SBC     D               
68AF: 06 58          LD      B,$58           
68B1: 44             LD      B,H             
68B2: A0             AND     B               
68B3: 03             INC     BC              
68B4: 24             INC     H               
68B5: 04             INC     B               
68B6: 22 03 A0       LD      ($A003),HL      
68B9: 5F             LD      E,A             
68BA: BE             CP      (HL)            
68BB: 99             SBC     C               
68BC: 16 C2          LD      D,$C2           
68BE: B3             OR      E               
68BF: F3             DI                      
68C0: 17             RLA                     
68C1: F3             DI                      
68C2: 8C             ADC     A,H             
68C3: 4B             LD      C,E             
68C4: 7B             LD      A,E             
68C5: 0F             RRCA                    
68C6: A0             AND     B               
68C7: B8             CP      B               
68C8: 16 E3          LD      D,$E3           
68CA: 16 15          LD      D,$15           
68CC: 53             LD      D,E             
68CD: 2D             DEC     L               
68CE: B9             CP      C               
68CF: D2 B5 D0       JP      NC,$D0B5        
68D2: 47             LD      B,A             
68D3: E6 BD          AND     $BD             
68D5: 09             ADD     HL,BC           
68D6: 15             DEC     D               
68D7: BD             CP      L               
68D8: A0             AND     B               
68D9: 07             RLCA                    
68DA: 3E 0D          LD      A,$0D           
68DC: 3C             INC     A               
68DD: 0E 0A          LD      C,$0A           
68DF: 0A             LD      A,(BC)          
68E0: 11 0A 3A       LD      DE,$3A0A        
68E3: 0A             LD      A,(BC)          
68E4: 41             LD      B,C             
68E5: 0A             LD      A,(BC)          
68E6: 42             LD      B,D             
68E7: 0A             LD      A,(BC)          
68E8: 40             LD      B,B             
68E9: 04             INC     B               
68EA: 2D             DEC     L               
68EB: 5F             LD      E,A             
68EC: BE             CP      (HL)            
68ED: DB 16          IN      A,($16)         
68EF: 9E             SBC     (HL)            
68F0: 7A             LD      A,D             
68F1: F3             DI                      
68F2: 5F             LD      E,A             
68F3: 81             ADD     A,C             
68F4: 5B             LD      E,E             
68F5: 91             SUB     C               
68F6: AF             XOR     A               
68F7: F0             RET     P               
68F8: A4             AND     H               
68F9: D6 B5          SUB     $B5             
68FB: D4 9C CF       CALL    NC,$CF9C        
68FE: 62             LD      H,D             
68FF: 33             INC     SP              
6900: 48             LD      C,B             
6901: 83             ADD     A,E             
6902: 48             LD      C,B             
6903: 55             LD      D,L             
6904: 62             LD      H,D             
6905: DF             RST     0X18            
6906: 48             LD      C,B             
6907: 39             ADD     HL,SP           
6908: 17             RLA                     
6909: 7F             LD      A,A             
690A: C6 DB          ADD     $DB             
690C: 06 1B          LD      B,$1B           
690E: A1             AND     C               
690F: 58             LD      E,B             
6910: 72             LD      (HL),D          
6911: 47             LD      B,A             
6912: 5E             LD      E,(HL)          
6913: 53             LD      D,E             
6914: B7             OR      A               
6915: E6 A4          AND     $A4             
6917: 21 24 01       LD      HL,$0124        
691A: 01 3E 0B       LD      BC,$0B3E        
691D: 3E 00          LD      A,$00           
691F: 00             NOP                     
6920: 80             ADD     A,B             
6921: 02             LD      (BC),A          
6922: 08             EX      AF,AF'          
6923: 4B             LD      C,E             
6924: A4             AND     H               
6925: BF             CP      A               
6926: 9A             SBC     D               
6927: 06 58          LD      B,$58           
6929: 44             LD      B,H             
692A: A0             AND     B               
692B: 07             RLCA                    
692C: 2C             INC     L               
692D: 0D             DEC     C               
692E: 2A 0E 0A       LD      HL,($0A0E)      
6931: 0A             LD      A,(BC)          
6932: 11 0A 3A       LD      DE,$3A0A        
6935: 0A             LD      A,(BC)          
6936: 40             LD      B,B             
6937: 0A             LD      A,(BC)          
6938: 41             LD      B,C             
6939: 0A             LD      A,(BC)          
693A: 42             LD      B,D             
693B: 04             INC     B               
693C: 1C             INC     E               
693D: 2F             CPL                     
693E: 49             LD      C,C             
693F: 51             LD      D,C             
6940: 18 45          JR      $6987           
6942: C2 DC B0       JP      NZ,$B0DC        
6945: C3 DA 73       JP      $73DA           
6948: 7B             LD      A,E             
6949: 4B             LD      C,E             
694A: 7B             LD      A,E             
694B: F5             PUSH    AF              
694C: 81             ADD     A,C             
694D: 03             INC     BC              
694E: BC             CP      H               
694F: DB 16          IN      A,($16)         
6951: 9E             SBC     (HL)            
6952: 7A             LD      A,D             
6953: F3             DI                      
6954: 5F             LD      E,A             
6955: 81             ADD     A,C             
6956: 5B             LD      E,E             
6957: 2B             DEC     HL              
6958: AF             XOR     A               
6959: 01 01 3E       LD      BC,$3E01        
695C: 0B             DEC     BC              
695D: 12             LD      (DE),A          
695E: 99             SBC     C               
695F: 00             NOP                     
6960: 8B             ADC     A,E             
6961: 03             INC     BC              
6962: 01 86 01       LD      BC,$0186        
6965: 01 14 02       LD      BC,$0214        
6968: 07             RLCA                    
6969: AF             XOR     A               
696A: 6E             LD      L,(HL)          
696B: 83             ADD     A,E             
696C: 61             LD      H,C             
696D: 81             ADD     A,C             
696E: 5B             LD      E,E             
696F: 52             LD      D,D             
6970: 16 80          LD      D,$80           
6972: 89             ADC     A,C             
6973: 8C             ADC     A,H             
6974: 00             NOP                     
6975: 80             ADD     A,B             
6976: 02             LD      (BC),A          
6977: 06 AF          LD      B,$AF           
6979: 6E             LD      L,(HL)          
697A: 83             ADD     A,E             
697B: 61             LD      H,C             
697C: BB             CP      E               
697D: 85             ADD     A,L             
697E: 01 01 14       LD      BC,$1401        
6981: 07             RLCA                    
6982: 79             LD      A,C             
6983: 0E 77          LD      C,$77           
6985: 0D             DEC     C               
6986: 32 0A 43       LD      ($430A),A       
6989: 09             ADD     HL,BC           
698A: 16 03          LD      D,$03           
698C: 8C             ADC     A,H             
698D: 41             LD      B,C             
698E: 03             INC     BC              
698F: 8E             ADC     A,(HL)          
6990: 1B             DEC     DE              
6991: 17             RLA                     
6992: 41             LD      B,C             
6993: 00             NOP                     
6994: 17             RLA                     
6995: 1B             DEC     DE              
6996: 13             INC     DE              
6997: 04             INC     B               
6998: 20 C7          JR      NZ,$6961        
699A: DE 77          SBC     $77             
699C: 15             DEC     D               
699D: 16 BC          LD      D,$BC           
699F: DB 72          IN      A,($72)         
69A1: BB             CP      E               
69A2: 85             ADD     A,L             
69A3: FB             EI                      
69A4: 17             RLA                     
69A5: 53             LD      D,E             
69A6: BE             CP      (HL)            
69A7: 5F             LD      E,A             
69A8: BE             CP      (HL)            
69A9: A9             XOR     C               
69AA: 15             DEC     D               
69AB: AF             XOR     A               
69AC: 9F             SBC     A               
69AD: 84             ADD     A,H             
69AE: 15             DEC     D               
69AF: 30 60          JR      NC,$6A11        
69B1: 17             RLA                     
69B2: 16 56          LD      D,$56           
69B4: DB 17          IN      A,($17)         
69B6: 48             LD      C,B             
69B7: 1B             DEC     DE              
69B8: 9C             SBC     H               
69B9: 0D             DEC     C               
69BA: 23             INC     HL              
69BB: 0A             LD      A,(BC)          
69BC: 05             DEC     B               
69BD: 04             INC     B               
69BE: 1F             RRA                     
69BF: C7             RST     0X00            
69C0: DE D3          SBC     $D3             
69C2: 14             INC     D               
69C3: 90             SUB     B               
69C4: 96             SUB     (HL)            
69C5: F3             DI                      
69C6: A0             AND     B               
69C7: 63             LD      H,E             
69C8: B1             OR      C               
69C9: 13             INC     DE              
69CA: 54             LD      D,H             
69CB: 5F             LD      E,A             
69CC: BE             CP      (HL)            
69CD: 84             ADD     A,H             
69CE: 15             DEC     D               
69CF: 30 60          JR      NC,$6A31        
69D1: 17             RLA                     
69D2: 16 48          LD      D,$48           
69D4: DB FF          IN      A,($FF)         
69D6: B2             OR      D               
69D7: C7             RST     0X00            
69D8: 16 0A          LD      D,$0A           
69DA: BC             CP      H               
69DB: 2F             CPL                     
69DC: 62             LD      H,D             
69DD: 2E 0D          LD      L,$0D           
69DF: 1C             INC     E               
69E0: 0A             LD      A,(BC)          
69E1: 43             LD      B,E             
69E2: 04             INC     B               
69E3: 16 C7          LD      D,$C7           
69E5: DE D3          SBC     $D3             
69E7: 14             INC     D               
69E8: E6 96          AND     $96             
69EA: 77             LD      (HL),A          
69EB: 15             DEC     D               
69EC: 16 BC          LD      D,$BC           
69EE: DB 72          IN      A,($72)         
69F0: AF             XOR     A               
69F1: 6E             LD      L,(HL)          
69F2: 83             ADD     A,E             
69F3: 61             LD      H,C             
69F4: BB             CP      E               
69F5: 85             ADD     A,L             
69F6: FB             EI                      
69F7: 17             RLA                     
69F8: 53             LD      D,E             
69F9: BE             CP      (HL)            
69FA: A9             XOR     C               
69FB: 8B             ADC     A,E             
69FC: 42             LD      B,D             
69FD: 03             INC     BC              
69FE: 18 00          JR      $6A00           
6A00: 00             NOP                     
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
6FA0: 21 24 00       LD      HL,$0024        
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
75E3: 3A 06 00       LD      A,($0006)       
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