![Bank 1F](GBZelda.jpg)

# Bank 1F

>>> cpu Z80GB

>>> binary 4000:roms/zelda.gb[7C000:80000]

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](../Hardware.md)

```code
4000: C3 09 40        JP      $4009               ; {}
4003: C3 17 7B        JP      $7B17               ; {}
4006: C3 1E 40        JP      $401E               ; {}
4009: 21 00 D3        LD      HL,$D300            
400C: 36 00           LD      (HL),$00            
400E: 2C              INC     L                   
400F: 20 FB           JR      NZ,$400C            ; {}
4011: 3E 80           LD      A,$80               
4013: E0 26           LDFF00  ($26),A             
4015: 3E 77           LD      A,$77               
4017: E0 24           LDFF00  ($24),A             
4019: 3E FF           LD      A,$FF               
401B: E0 25           LDFF00  ($25),A             
401D: C9              RET                         
401E: CD 04 42        CALL    $4204               ; {}
4021: CD ED 53        CALL    $53ED               ; {}
4024: CD E8 64        CALL    $64E8               ; {}
4027: AF              XOR     A                   
4028: EA 60 D3        LD      ($D360),A           
402B: EA 70 D3        LD      ($D370),A           
402E: EA 78 D3        LD      ($D378),A           
4031: C9              RET                         
4032: FF              RST     0X38                
4033: FF              RST     0X38                
4034: FF              RST     0X38                
4035: FF              RST     0X38                
4036: FF              RST     0X38                
4037: FF              RST     0X38                
4038: FF              RST     0X38                
4039: FF              RST     0X38                
403A: FF              RST     0X38                
403B: FF              RST     0X38                
403C: FF              RST     0X38                
403D: FF              RST     0X38                
403E: FF              RST     0X38                
403F: FF              RST     0X38                
4040: FF              RST     0X38                
4041: FF              RST     0X38                
4042: FF              RST     0X38                
4043: FF              RST     0X38                
4044: FF              RST     0X38                
4045: FF              RST     0X38                
4046: FF              RST     0X38                
4047: FF              RST     0X38                
4048: FF              RST     0X38                
4049: FF              RST     0X38                
404A: FF              RST     0X38                
404B: FF              RST     0X38                
404C: FF              RST     0X38                
404D: FF              RST     0X38                
404E: FF              RST     0X38                
404F: FF              RST     0X38                
4050: FF              RST     0X38                
4051: FF              RST     0X38                
4052: FF              RST     0X38                
4053: FF              RST     0X38                
4054: FF              RST     0X38                
4055: FF              RST     0X38                
4056: FF              RST     0X38                
4057: FF              RST     0X38                
4058: FF              RST     0X38                
4059: FF              RST     0X38                
405A: FF              RST     0X38                
405B: FF              RST     0X38                
405C: FF              RST     0X38                
405D: FF              RST     0X38                
405E: FF              RST     0X38                
405F: FF              RST     0X38                
4060: FF              RST     0X38                
4061: FF              RST     0X38                
4062: FF              RST     0X38                
4063: FF              RST     0X38                
4064: FF              RST     0X38                
4065: FF              RST     0X38                
4066: FF              RST     0X38                
4067: FF              RST     0X38                
4068: FF              RST     0X38                
4069: FF              RST     0X38                
406A: FF              RST     0X38                
406B: FF              RST     0X38                
406C: FF              RST     0X38                
406D: FF              RST     0X38                
406E: FF              RST     0X38                
406F: FF              RST     0X38                
4070: FF              RST     0X38                
4071: FF              RST     0X38                
4072: FF              RST     0X38                
4073: FF              RST     0X38                
4074: FF              RST     0X38                
4075: FF              RST     0X38                
4076: FF              RST     0X38                
4077: FF              RST     0X38                
4078: FF              RST     0X38                
4079: FF              RST     0X38                
407A: FF              RST     0X38                
407B: FF              RST     0X38                
407C: FF              RST     0X38                
407D: FF              RST     0X38                
407E: FF              RST     0X38                
407F: FF              RST     0X38                
4080: FF              RST     0X38                
4081: FF              RST     0X38                
4082: FF              RST     0X38                
4083: FF              RST     0X38                
4084: FF              RST     0X38                
4085: FF              RST     0X38                
4086: FF              RST     0X38                
4087: FF              RST     0X38                
4088: FF              RST     0X38                
4089: FF              RST     0X38                
408A: FF              RST     0X38                
408B: FF              RST     0X38                
408C: FF              RST     0X38                
408D: FF              RST     0X38                
408E: FF              RST     0X38                
408F: FF              RST     0X38                
4090: FF              RST     0X38                
4091: FF              RST     0X38                
4092: FF              RST     0X38                
4093: FF              RST     0X38                
4094: FF              RST     0X38                
4095: FF              RST     0X38                
4096: FF              RST     0X38                
4097: FF              RST     0X38                
4098: FF              RST     0X38                
4099: FF              RST     0X38                
409A: FF              RST     0X38                
409B: FF              RST     0X38                
409C: FF              RST     0X38                
409D: FF              RST     0X38                
409E: FF              RST     0X38                
409F: FF              RST     0X38                
40A0: FF              RST     0X38                
40A1: FF              RST     0X38                
40A2: FF              RST     0X38                
40A3: FF              RST     0X38                
40A4: FF              RST     0X38                
40A5: FF              RST     0X38                
40A6: FF              RST     0X38                
40A7: FF              RST     0X38                
40A8: FF              RST     0X38                
40A9: FF              RST     0X38                
40AA: FF              RST     0X38                
40AB: FF              RST     0X38                
40AC: FF              RST     0X38                
40AD: FF              RST     0X38                
40AE: FF              RST     0X38                
40AF: FF              RST     0X38                
40B0: FF              RST     0X38                
40B1: FF              RST     0X38                
40B2: FF              RST     0X38                
40B3: FF              RST     0X38                
40B4: FF              RST     0X38                
40B5: FF              RST     0X38                
40B6: FF              RST     0X38                
40B7: FF              RST     0X38                
40B8: FF              RST     0X38                
40B9: FF              RST     0X38                
40BA: FF              RST     0X38                
40BB: FF              RST     0X38                
40BC: FF              RST     0X38                
40BD: FF              RST     0X38                
40BE: FF              RST     0X38                
40BF: FF              RST     0X38                
40C0: FF              RST     0X38                
40C1: FF              RST     0X38                
40C2: FF              RST     0X38                
40C3: FF              RST     0X38                
40C4: FF              RST     0X38                
40C5: FF              RST     0X38                
40C6: FF              RST     0X38                
40C7: FF              RST     0X38                
40C8: FF              RST     0X38                
40C9: FF              RST     0X38                
40CA: FF              RST     0X38                
40CB: FF              RST     0X38                
40CC: FF              RST     0X38                
40CD: FF              RST     0X38                
40CE: FF              RST     0X38                
40CF: FF              RST     0X38                
40D0: FF              RST     0X38                
40D1: FF              RST     0X38                
40D2: FF              RST     0X38                
40D3: FF              RST     0X38                
40D4: FF              RST     0X38                
40D5: FF              RST     0X38                
40D6: FF              RST     0X38                
40D7: FF              RST     0X38                
40D8: FF              RST     0X38                
40D9: FF              RST     0X38                
40DA: FF              RST     0X38                
40DB: FF              RST     0X38                
40DC: FF              RST     0X38                
40DD: FF              RST     0X38                
40DE: FF              RST     0X38                
40DF: FF              RST     0X38                
40E0: FF              RST     0X38                
40E1: FF              RST     0X38                
40E2: FF              RST     0X38                
40E3: FF              RST     0X38                
40E4: FF              RST     0X38                
40E5: FF              RST     0X38                
40E6: FF              RST     0X38                
40E7: FF              RST     0X38                
40E8: FF              RST     0X38                
40E9: FF              RST     0X38                
40EA: FF              RST     0X38                
40EB: FF              RST     0X38                
40EC: FF              RST     0X38                
40ED: FF              RST     0X38                
40EE: FF              RST     0X38                
40EF: FF              RST     0X38                
40F0: FF              RST     0X38                
40F1: FF              RST     0X38                
40F2: FF              RST     0X38                
40F3: FF              RST     0X38                
40F4: FF              RST     0X38                
40F5: FF              RST     0X38                
40F6: FF              RST     0X38                
40F7: FF              RST     0X38                
40F8: FF              RST     0X38                
40F9: FF              RST     0X38                
40FA: FF              RST     0X38                
40FB: FF              RST     0X38                
40FC: FF              RST     0X38                
40FD: FF              RST     0X38                
40FE: FF              RST     0X38                
40FF: FF              RST     0X38                
4100: 2D              DEC     L                   
4101: 42              LD      B,D                 
4102: 22              LD      (HLI),A             
4103: 43              LD      B,E                 
4104: 6E              LD      L,(HL)              
4105: 43              LD      B,E                 
4106: A3              AND     E                   
4107: 43              LD      B,E                 
4108: E2              LDFF00  (C),A               
4109: 43              LD      B,E                 
410A: 1D              DEC     E                   
410B: 44              LD      B,H                 
410C: 59              LD      E,C                 
410D: 44              LD      B,H                 
410E: 7D              LD      A,L                 
410F: 44              LD      B,H                 
4110: A1              AND     C                   
4111: 44              LD      B,H                 
4112: CE 44           ADC     $44                 
4114: 15              DEC     D                   
4115: 45              LD      B,L                 
4116: 54              LD      D,H                 
4117: 45              LD      B,L                 
4118: 9B              SBC     E                   
4119: 45              LD      B,L                 
411A: AE              XOR     (HL)                
411B: 45              LD      B,L                 
411C: CC 45 F0        CALL    Z,$F045             
411F: 45              LD      B,L                 
4120: F3              DI                          
4121: 45              LD      B,L                 
4122: 4B              LD      C,E                 
4123: 46              LD      B,(HL)              
4124: 9D              SBC     L                   
4125: 46              LD      B,(HL)              
4126: E7              RST     0X20                
4127: 46              LD      B,(HL)              
4128: 01 47 32        LD      BC,$3247            
412B: 47              LD      B,A                 
412C: 45              LD      B,L                 
412D: 47              LD      B,A                 
412E: 8A              ADC     A,D                 
412F: 47              LD      B,A                 
4130: AE              XOR     (HL)                
4131: 47              LD      B,A                 
4132: EF              RST     0X28                
4133: 47              LD      B,A                 
4134: 18 48           JR      $417E               ; {}
4136: 75              LD      (HL),L              
4137: 48              LD      C,B                 
4138: CF              RST     0X08                
4139: 48              LD      C,B                 
413A: 0A              LD      A,(BC)              
413B: 49              LD      C,C                 
413C: 39              ADD     HL,SP               
413D: 49              LD      C,C                 
413E: 75              LD      (HL),L              
413F: 49              LD      C,C                 
4140: B0              OR      B                   
4141: 49              LD      C,C                 
4142: 08 4A 70        LD      ($704A),SP          ; {}
4145: 4A              LD      C,D                 
4146: D9              RETI                        
4147: 4A              LD      C,D                 
4148: EC                              
4149: 4A              LD      C,D                 
414A: 43              LD      B,E                 
414B: 4B              LD      C,E                 
414C: 91              SUB     C                   
414D: 4B              LD      C,E                 
414E: B1              OR      C                   
414F: 4B              LD      C,E                 
4150: F9              LD      SP,HL               
4151: 4B              LD      C,E                 
4152: 19              ADD     HL,DE               
4153: 4C              LD      C,H                 
4154: 2C              INC     L                   
4155: 4C              LD      C,H                 
4156: 81              ADD     A,C                 
4157: 4C              LD      C,H                 
4158: E1              POP     HL                  
4159: 4C              LD      C,H                 
415A: 26 4D           LD      H,$4D               
415C: B7              OR      A                   
415D: 4D              LD      C,L                 
415E: EF              RST     0X28                
415F: 4D              LD      C,L                 
4160: 10 4E           STOP    $4E                 
4162: 56              LD      D,(HL)              
4163: 4E              LD      C,(HL)              
4164: 87              ADD     A,A                 
4165: 4E              LD      C,(HL)              
4166: CA 4E 23        JP      Z,$234E             
4169: 4F              LD      C,A                 
416A: 84              ADD     A,H                 
416B: 4F              LD      C,A                 
416C: F5              PUSH    AF                  
416D: 4F              LD      C,A                 
416E: 3C              INC     A                   
416F: 50              LD      D,B                 
4170: 8E              ADC     A,(HL)              
4171: 50              LD      D,B                 
4172: 20 51           JR      NZ,$41C5            ; {}
4174: 67              LD      H,A                 
4175: 51              LD      D,C                 
4176: B4              OR      H                   
4177: 51              LD      D,C                 
4178: FC                              
4179: 51              LD      D,C                 
417A: 6E              LD      L,(HL)              
417B: 52              LD      D,D                 
417C: 89              ADC     A,C                 
417D: 52              LD      D,D                 
417E: D9              RETI                        
417F: 52              LD      D,D                 
4180: 37              SCF                         
4181: 53              LD      D,E                 
4182: 5A              LD      E,D                 
4183: 42              LD      B,D                 
4184: 28 43           JR      Z,$41C9             ; {}
4186: 77              LD      (HL),A              
4187: 43              LD      B,E                 
4188: B1              OR      C                   
4189: 43              LD      B,E                 
418A: F0 43           LD      A,($43)             
418C: 2B              DEC     HL                  
418D: 44              LD      B,H                 
418E: 5F              LD      E,A                 
418F: 44              LD      B,H                 
4190: 83              ADD     A,E                 
4191: 44              LD      B,H                 
4192: AA              XOR     D                   
4193: 44              LD      B,H                 
4194: E7              RST     0X20                
4195: 44              LD      B,H                 
4196: 23              INC     HL                  
4197: 45              LD      B,L                 
4198: 62              LD      H,D                 
4199: 45              LD      B,L                 
419A: A1              AND     C                   
419B: 45              LD      B,L                 
419C: BF              CP      A                   
419D: 45              LD      B,L                 
419E: D2 45 BB        JP      NC,$BB45            
41A1: 53              LD      D,E                 
41A2: 0F              RRCA                        
41A3: 46              LD      B,(HL)              
41A4: 6F              LD      L,A                 
41A5: 46              LD      B,(HL)              
41A6: B6              OR      (HL)                
41A7: 46              LD      B,(HL)              
41A8: F4                              
41A9: 46              LD      B,(HL)              
41AA: 07              RLCA                        
41AB: 47              LD      B,A                 
41AC: 38 47           JR      C,$41F5             ; {}
41AE: 53              LD      D,E                 
41AF: 47              LD      B,A                 
41B0: 90              SUB     B                   
41B1: 47              LD      B,A                 
41B2: B4              OR      H                   
41B3: 47              LD      B,A                 
41B4: FD                              
41B5: 47              LD      B,A                 
41B6: 26 48           LD      H,$48               
41B8: 83              ADD     A,E                 
41B9: 48              LD      C,B                 
41BA: DA 48 10        JP      C,$1048             
41BD: 49              LD      C,C                 
41BE: 47              LD      B,A                 
41BF: 49              LD      C,C                 
41C0: 8E              ADC     A,(HL)              
41C1: 49              LD      C,C                 
41C2: BE              CP      (HL)                
41C3: 49              LD      C,C                 
41C4: 4F              LD      C,A                 
41C5: 4A              LD      C,D                 
41C6: 7B              LD      A,E                 
41C7: 4A              LD      C,D                 
41C8: DF              RST     0X18                
41C9: 4A              LD      C,D                 
41CA: F7              RST     0X30                
41CB: 4A              LD      C,D                 
41CC: 51              LD      D,C                 
41CD: 4B              LD      C,E                 
41CE: 97              SUB     A                   
41CF: 4B              LD      C,E                 
41D0: B7              OR      A                   
41D1: 4B              LD      C,E                 
41D2: FF              RST     0X38                
41D3: 4B              LD      C,E                 
41D4: 1F              RRA                         
41D5: 4C              LD      C,H                 
41D6: 3A              LD      A,(HLD)             
41D7: 4C              LD      C,H                 
41D8: 8F              ADC     A,A                 
41D9: 4C              LD      C,H                 
41DA: EF              RST     0X28                
41DB: 4C              LD      C,H                 
41DC: 34              INC     (HL)                
41DD: 4D              LD      C,L                 
41DE: C5              PUSH    BC                  
41DF: 4D              LD      C,L                 
41E0: FA 4D 1E        LD      A,($1E4D)           
41E3: 4E              LD      C,(HL)              
41E4: 5C              LD      E,H                 
41E5: 4E              LD      C,(HL)              
41E6: 95              SUB     L                   
41E7: 4E              LD      C,(HL)              
41E8: D8              RET     C                   
41E9: 4E              LD      C,(HL)              
41EA: 31 4F 92        LD      SP,$924F            
41ED: 4F              LD      C,A                 
41EE: 03              INC     BC                  
41EF: 50              LD      D,B                 
41F0: 57              LD      D,A                 
41F1: 50              LD      D,B                 
41F2: 9C              SBC     H                   
41F3: 50              LD      D,B                 
41F4: 2E 51           LD      L,$51               
41F6: 75              LD      (HL),L              
41F7: 51              LD      D,C                 
41F8: C2 51 26        JP      NZ,$2651            
41FB: 52              LD      D,D                 
41FC: 7C              LD      A,H                 
41FD: 52              LD      D,D                 
41FE: 97              SUB     A                   
41FF: 52              LD      D,D                 
4200: E7              RST     0X20                
4201: 52              LD      D,D                 
4202: 3D              DEC     A                   
4203: 53              LD      D,E                 
4204: 21 60 D3        LD      HL,$D360            
4207: 7E              LD      A,(HL)              
4208: A7              AND     A                   
4209: 28 11           JR      Z,$421C             ; {}
420B: FE 01           CP      $01                 
420D: 28 07           JR      Z,$4216             ; {}
420F: FA C6 D3        LD      A,($D3C6)           
4212: A7              AND     A                   
4213: C2 E6 53        JP      NZ,$53E6            ; {}
4216: 7E              LD      A,(HL)              
4217: 21 00 41        LD      HL,$4100            
421A: 18 07           JR      $4223               ; {}
421C: 23              INC     HL                  
421D: 7E              LD      A,(HL)              
421E: A7              AND     A                   
421F: C8              RET     Z                   
4220: 21 82 41        LD      HL,$4182            
4223: CD 60 7A        CALL    $7A60               ; {}
4226: 11 90 D3        LD      DE,$D390            
4229: 01 94 D3        LD      BC,$D394            
422C: E9              JP      (HL)                
422D: AF              XOR     A                   
422E: EA 70 D3        LD      ($D370),A           
4231: EA 71 D3        LD      ($D371),A           
4234: E0 1A           LDFF00  ($1A),A             
4236: 3E 01           LD      A,$01               
4238: EA C8 D3        LD      ($D3C8),A           
423B: 21 2F D3        LD      HL,$D32F            
423E: CB FE           SET     1,E                 
4240: 21 3F D3        LD      HL,$D33F            
4243: CB FE           SET     1,E                 
4245: 21 EB 42        LD      HL,$42EB            
4248: CD 7B 7A        CALL    $7A7B               ; {}
424B: CD 6A 63        CALL    $636A               ; {}
424E: 21 FF 42        LD      HL,$42FF            
4251: CD 81 7A        CALL    $7A81               ; {}
4254: 21 D3 42        LD      HL,$42D3            
4257: C3 95 53        JP      $5395               ; {}
425A: CD 6D 7A        CALL    $7A6D               ; {}
425D: C0              RET     NZ                  
425E: CD 71 7A        CALL    $7A71               ; {}
4261: FE 01           CP      $01                 
4263: 28 0E           JR      Z,$4273             ; {}
4265: FE 02           CP      $02                 
4267: 28 1C           JR      Z,$4285             ; {}
4269: FE 03           CP      $03                 
426B: 28 2A           JR      Z,$4297             ; {}
426D: FE 04           CP      $04                 
426F: 28 38           JR      Z,$42A9             ; {}
4271: 18 48           JR      $42BB               ; {}
4273: 21 D9 42        LD      HL,$42D9            
4276: CD 75 7A        CALL    $7A75               ; {}
4279: 21 F0 42        LD      HL,$42F0            
427C: CD 7B 7A        CALL    $7A7B               ; {}
427F: 21 05 43        LD      HL,$4305            
4282: C3 81 7A        JP      $7A81               ; {}
4285: 21 DF 42        LD      HL,$42DF            
4288: CD 75 7A        CALL    $7A75               ; {}
428B: 21 F5 42        LD      HL,$42F5            
428E: CD 7B 7A        CALL    $7A7B               ; {}
4291: 21 0B 43        LD      HL,$430B            
4294: C3 81 7A        JP      $7A81               ; {}
4297: 21 E5 42        LD      HL,$42E5            
429A: CD 75 7A        CALL    $7A75               ; {}
429D: 21 FA 42        LD      HL,$42FA            
42A0: CD 7B 7A        CALL    $7A7B               ; {}
42A3: 21 11 43        LD      HL,$4311            
42A6: C3 81 7A        JP      $7A81               ; {}
42A9: 21 17 43        LD      HL,$4317            
42AC: CD 75 7A        CALL    $7A75               ; {}
42AF: 21 1D 43        LD      HL,$431D            
42B2: CD 7B 7A        CALL    $7A7B               ; {}
42B5: 21 17 43        LD      HL,$4317            
42B8: C3 81 7A        JP      $7A81               ; {}
42BB: 21 2F D3        LD      HL,$D32F            
42BE: CB BE           RES     1,E                 
42C0: 21 3F D3        LD      HL,$D33F            
42C3: CB BE           RES     1,E                 
42C5: AF              XOR     A                   
42C6: E0 1A           LDFF00  ($1A),A             
42C8: EA C8 D3        LD      ($D3C8),A           
42CB: 3E 01           LD      A,$01               
42CD: EA E7 D3        LD      ($D3E7),A           
42D0: C3 BB 53        JP      $53BB               ; {}
42D3: 00              NOP                         
42D4: 80              ADD     A,B                 
42D5: 80              ADD     A,B                 
42D6: 89              ADC     A,C                 
42D7: 86              ADD     A,(HL)              
42D8: 0A              LD      A,(BC)              
42D9: 00              NOP                         
42DA: 80              ADD     A,B                 
42DB: 80              ADD     A,B                 
42DC: 9E              SBC     (HL)                
42DD: 86              ADD     A,(HL)              
42DE: 0A              LD      A,(BC)              
42DF: 00              NOP                         
42E0: 80              ADD     A,B                 
42E1: 80              ADD     A,B                 
42E2: B2              OR      D                   
42E3: 86              ADD     A,(HL)              
42E4: 0A              LD      A,(BC)              
42E5: 00              NOP                         
42E6: 80              ADD     A,B                 
42E7: 80              ADD     A,B                 
42E8: C4 86 30        CALL    NZ,$3086            
42EB: 00              NOP                         
42EC: C0              RET     NZ                  
42ED: 06 87           LD      B,$87               
42EF: 0A              LD      A,(BC)              
42F0: 00              NOP                         
42F1: C0              RET     NZ                  
42F2: 14              INC     D                   
42F3: 87              ADD     A,A                 
42F4: 0A              LD      A,(BC)              
42F5: 00              NOP                         
42F6: C0              RET     NZ                  
42F7: 21 87 0A        LD      HL,$0A87            
42FA: 00              NOP                         
42FB: C0              RET     NZ                  
42FC: 2D              DEC     L                   
42FD: 87              ADD     A,A                 
42FE: 30 80           JR      NC,$4280            ; {}
4300: 00              NOP                         
4301: 20 6B           JR      NZ,$436E            ; {}
4303: 87              ADD     A,A                 
4304: 0A              LD      A,(BC)              
4305: 80              ADD     A,B                 
4306: 00              NOP                         
4307: 20 73           JR      NZ,$437C            ; {}
4309: 87              ADD     A,A                 
430A: 0A              LD      A,(BC)              
430B: 80              ADD     A,B                 
430C: 00              NOP                         
430D: 20 7B           JR      NZ,$438A            ; {}
430F: 87              ADD     A,A                 
4310: 0A              LD      A,(BC)              
4311: 80              ADD     A,B                 
4312: 00              NOP                         
4313: 20 83           JR      NZ,$4298            ; {}
4315: 87              ADD     A,A                 
4316: 30 00           JR      NC,$4318            ; {}
4318: 00              NOP                         
4319: 00              NOP                         
431A: 00              NOP                         
431B: C0              RET     NZ                  
431C: 20 3F           JR      NZ,$435D            ; {}
431E: 00              NOP                         
431F: 00              NOP                         
4320: C1              POP     BC                  
4321: 20 21           JR      NZ,$4344            ; {}
4323: 53              LD      D,E                 
4324: 43              LD      B,E                 
4325: C3 95 53        JP      $5395               ; {}
4328: CD 6D 7A        CALL    $7A6D               ; {}
432B: C0              RET     NZ                  
432C: CD 71 7A        CALL    $7A71               ; {}
432F: FE 08           CP      $08                 
4331: CA BB 53        JP      Z,$53BB             ; {}
4334: 21 45 43        LD      HL,$4345            
4337: CD 60 7A        CALL    $7A60               ; {}
433A: 3E 80           LD      A,$80               
433C: E0 11           LDFF00  ($11),A             
433E: 3E F1           LD      A,$F1               
4340: E0 12           LDFF00  ($12),A             
4342: C3 DF 53        JP      $53DF               ; {}
4345: 59              LD      E,C                 
4346: 43              LD      B,E                 
4347: 5C              LD      E,H                 
4348: 43              LD      B,E                 
4349: 5F              LD      E,A                 
434A: 43              LD      B,E                 
434B: 62              LD      H,D                 
434C: 43              LD      B,E                 
434D: 65              LD      H,L                 
434E: 43              LD      B,E                 
434F: 68              LD      L,B                 
4350: 43              LD      B,E                 
4351: 6B              LD      L,E                 
4352: 43              LD      B,E                 
4353: 00              NOP                         
4354: 80              ADD     A,B                 
4355: F1              POP     AF                  
4356: A7              AND     A                   
4357: C7              RST     0X00                
4358: 08 A2 C7        LD      ($C7A2),SP          
435B: 08 90 C7        LD      ($C790),SP          
435E: 08 7B C7        LD      ($C77B),SP          
4361: 08 59 C7        LD      ($C759),SP          
4364: 08 97 C7        LD      ($C797),SP          
4367: 08 AC C7        LD      ($C7AC),SP          
436A: 08 BE C7        LD      ($C7BE),SP          
436D: 20 21           JR      NZ,$4390            ; {}
436F: 9D              SBC     L                   
4370: 43              LD      B,E                 
4371: CD B3 7A        CALL    $7AB3               ; {}
4374: C3 9A 53        JP      $539A               ; {}
4377: CD 71 7A        CALL    $7A71               ; {}
437A: FE 0D           CP      $0D                 
437C: CA B5 53        JP      Z,$53B5             ; {}
437F: 21 85 43        LD      HL,$4385            
4382: C3 DD 7A        JP      $7ADD               ; {}
4385: FF              RST     0X38                
4386: C0              RET     NZ                  
4387: FF              RST     0X38                
4388: 80              ADD     A,B                 
4389: FF              RST     0X38                
438A: 00              NOP                         
438B: FE 00           CP      $00                 
438D: 01 00 FF        LD      BC,$FF00            
4390: 00              NOP                         
4391: 01 00 FF        LD      BC,$FF00            
4394: 00              NOP                         
4395: 00              NOP                         
4396: C0              RET     NZ                  
4397: 00              NOP                         
4398: C0              RET     NZ                  
4399: 00              NOP                         
439A: C0              RET     NZ                  
439B: 00              NOP                         
439C: C0              RET     NZ                  
439D: 00              NOP                         
439E: 00              NOP                         
439F: C0              RET     NZ                  
43A0: 80              ADD     A,B                 
43A1: 86              ADD     A,(HL)              
43A2: 01 3E 0E        LD      BC,$0E3E            
43A5: EA BC D3        LD      ($D3BC),A           
43A8: 21 DC 43        LD      HL,$43DC            
43AB: CD B3 7A        CALL    $7AB3               ; {}
43AE: C3 9A 53        JP      $539A               ; {}
43B1: CD 6D 7A        CALL    $7A6D               ; {}
43B4: C0              RET     NZ                  
43B5: FA 79 D3        LD      A,($D379)           
43B8: FE 02           CP      $02                 
43BA: CA B5 53        JP      Z,$53B5             ; {}
43BD: 3E 02           LD      A,$02               
43BF: 12              LD      (DE),A              
43C0: CD 71 7A        CALL    $7A71               ; {}
43C3: FE 03           CP      $03                 
43C5: 28 06           JR      Z,$43CD             ; {}
43C7: 21 D8 43        LD      HL,$43D8            
43CA: C3 DD 7A        JP      $7ADD               ; {}
43CD: CD 96 7A        CALL    $7A96               ; {}
43D0: CA BB 53        JP      Z,$53BB             ; {}
43D3: 3E 01           LD      A,$01               
43D5: 02              LD      (BC),A              
43D6: 18 EF           JR      $43C7               ; {}
43D8: 00              NOP                         
43D9: 20 FF           JR      NZ,$43DA            ; {}
43DB: F0 00           LD      A,($00)             
43DD: 80              ADD     A,B                 
43DE: 87              ADD     A,A                 
43DF: C0              RET     NZ                  
43E0: 86              ADD     A,(HL)              
43E1: 02              LD      (BC),A              
43E2: 3E 04           LD      A,$04               
43E4: EA BC D3        LD      ($D3BC),A           
43E7: 21 17 44        LD      HL,$4417            
43EA: CD B3 7A        CALL    $7AB3               ; {}
43ED: C3 9A 53        JP      $539A               ; {}
43F0: CD 6D 7A        CALL    $7A6D               ; {}
43F3: C0              RET     NZ                  
43F4: 3E 04           LD      A,$04               
43F6: 12              LD      (DE),A              
43F7: CD 71 7A        CALL    $7A71               ; {}
43FA: FE 05           CP      $05                 
43FC: 28 06           JR      Z,$4404             ; {}
43FE: 21 0F 44        LD      HL,$440F            
4401: C3 DD 7A        JP      $7ADD               ; {}
4404: CD 96 7A        CALL    $7A96               ; {}
4407: CA BB 53        JP      Z,$53BB             ; {}
440A: 3E 01           LD      A,$01               
440C: 02              LD      (BC),A              
440D: 18 EF           JR      $43FE               ; {}
440F: 00              NOP                         
4410: 06 00           LD      B,$00               
4412: 04              INC     B                   
4413: 00              NOP                         
4414: 02              LD      (BC),A              
4415: FF              RST     0X38                
4416: F4                              
4417: 00              NOP                         
4418: 00              NOP                         
4419: C5              PUSH    BC                  
441A: D8              RET     C                   
441B: 87              ADD     A,A                 
441C: 04              INC     B                   
441D: 3E 0A           LD      A,$0A               
441F: EA BC D3        LD      ($D3BC),A           
4422: 21 53 44        LD      HL,$4453            
4425: CD B3 7A        CALL    $7AB3               ; {}
4428: C3 95 53        JP      $5395               ; {}
442B: CD 71 7A        CALL    $7A71               ; {}
442E: FE 09           CP      $09                 
4430: 28 06           JR      Z,$4438             ; {}
4432: 21 43 44        LD      HL,$4443            
4435: C3 DD 7A        JP      $7ADD               ; {}
4438: CD 96 7A        CALL    $7A96               ; {}
443B: CA B5 53        JP      Z,$53B5             ; {}
443E: 3E 01           LD      A,$01               
4440: 02              LD      (BC),A              
4441: 18 EF           JR      $4432               ; {}
4443: 00              NOP                         
4444: 40              LD      B,B                 
4445: 00              NOP                         
4446: 80              ADD     A,B                 
4447: 00              NOP                         
4448: 80              ADD     A,B                 
4449: 00              NOP                         
444A: 40              LD      B,B                 
444B: FF              RST     0X38                
444C: D0              RET     NC                  
444D: FF              RST     0X38                
444E: A0              AND     B                   
444F: FF              RST     0X38                
4450: A0              AND     B                   
4451: FF              RST     0X38                
4452: D0              RET     NC                  
4453: 00              NOP                         
4454: 80              ADD     A,B                 
4455: 1B              DEC     DE                  
4456: 00              NOP                         
4457: 82              ADD     A,D                 
4458: 01 21 71        LD      BC,$7121            
445B: 44              LD      B,H                 
445C: C3 9A 53        JP      $539A               ; {}
445F: CD 6D 7A        CALL    $7A6D               ; {}
4462: C0              RET     NZ                  
4463: CD 71 7A        CALL    $7A71               ; {}
4466: FE 02           CP      $02                 
4468: CA BB 53        JP      Z,$53BB             ; {}
446B: 21 77 44        LD      HL,$4477            
446E: C3 75 7A        JP      $7A75               ; {}
4471: 00              NOP                         
4472: 3D              DEC     A                   
4473: F0 D8           LD      A,($D8)             
4475: C7              RST     0X00                
4476: 03              INC     BC                  
4477: 00              NOP                         
4478: 00              NOP                         
4479: 81              ADD     A,C                 
447A: E0 87           LDFF00  ($87),A             
447C: 08 21 95        LD      ($9521),SP          
447F: 44              LD      B,H                 
4480: C3 9A 53        JP      $539A               ; {}
4483: CD 6D 7A        CALL    $7A6D               ; {}
4486: C0              RET     NZ                  
4487: CD 71 7A        CALL    $7A71               ; {}
448A: FE 02           CP      $02                 
448C: CA BB 53        JP      Z,$53BB             ; {}
448F: 21 9B 44        LD      HL,$449B            
4492: C3 75 7A        JP      $7A75               ; {}
4495: 3F              CCF                         
4496: 9E              SBC     (HL)                
4497: 29              ADD     HL,HL               
4498: 80              ADD     A,B                 
4499: C7              RST     0X00                
449A: 08 1F 9F        LD      ($9F1F),SP          
449D: 81              ADD     A,C                 
449E: 20 87           JR      NZ,$4427            ; {}
44A0: 10 21           STOP    $21                 
44A2: C8              RET     Z                   
44A3: 44              LD      B,H                 
44A4: CD B3 7A        CALL    $7AB3               ; {}
44A7: C3 9A 53        JP      $539A               ; {}
44AA: CD 71 7A        CALL    $7A71               ; {}
44AD: FE 09           CP      $09                 
44AF: CA B5 53        JP      Z,$53B5             ; {}
44B2: 21 B8 44        LD      HL,$44B8            
44B5: C3 DD 7A        JP      $7ADD               ; {}
44B8: 01 00 00        LD      BC,$0000            
44BB: C0              RET     NZ                  
44BC: 00              NOP                         
44BD: 80              ADD     A,B                 
44BE: 00              NOP                         
44BF: 40              LD      B,B                 
44C0: FF              RST     0X38                
44C1: C0              RET     NZ                  
44C2: FF              RST     0X38                
44C3: 80              ADD     A,B                 
44C4: FF              RST     0X38                
44C5: 40              LD      B,B                 
44C6: FF              RST     0X38                
44C7: 00              NOP                         
44C8: 00              NOP                         
44C9: 9F              SBC     A                   
44CA: A0              AND     B                   
44CB: 00              NOP                         
44CC: C2 01 FA        JP      NZ,$FA01            
44CF: 61              LD      H,C                 
44D0: D3                              
44D1: FE 13           CP      $13                 
44D3: CA E6 53        JP      Z,$53E6             ; {}
44D6: F0 24           LD      A,($24)             
44D8: FE 77           CP      $77                 
44DA: 20 06           JR      NZ,$44E2            ; {}
44DC: 21 09 45        LD      HL,$4509            
44DF: C3 9A 53        JP      $539A               ; {}
44E2: 21 0F 45        LD      HL,$450F            
44E5: 18 F8           JR      $44DF               ; {}
44E7: CD 6D 7A        CALL    $7A6D               ; {}
44EA: C0              RET     NZ                  
44EB: CD 71 7A        CALL    $7A71               ; {}
44EE: FE 02           CP      $02                 
44F0: CA BB 53        JP      Z,$53BB             ; {}
44F3: F0 24           LD      A,($24)             
44F5: FE 77           CP      $77                 
44F7: 20 0C           JR      NZ,$4505            ; {}
44F9: 3E 10           LD      A,$10               
44FB: E0 12           LDFF00  ($12),A             
44FD: 3E C7           LD      A,$C7               
44FF: E0 14           LDFF00  ($14),A             
4501: 3E 08           LD      A,$08               
4503: 12              LD      (DE),A              
4504: C9              RET                         
4505: 3E 20           LD      A,$20               
4507: 18 F2           JR      $44FB               ; {}
4509: 00              NOP                         
450A: 9F              SBC     A                   
450B: 80              ADD     A,B                 
450C: A0              AND     B                   
450D: C7              RST     0X00                
450E: 02              LD      (BC),A              
450F: 00              NOP                         
4510: 9F              SBC     A                   
4511: F0 A0           LD      A,($A0)             
4513: C7              RST     0X00                
4514: 02              LD      (BC),A              
4515: 3E 05           LD      A,$05               
4517: EA BC D3        LD      ($D3BC),A           
451A: 21 4E 45        LD      HL,$454E            
451D: CD B3 7A        CALL    $7AB3               ; {}
4520: C3 95 53        JP      $5395               ; {}
4523: CD 6D 7A        CALL    $7A6D               ; {}
4526: C0              RET     NZ                  
4527: 3E 02           LD      A,$02               
4529: 12              LD      (DE),A              
452A: CD 71 7A        CALL    $7A71               ; {}
452D: FE 07           CP      $07                 
452F: 28 06           JR      Z,$4537             ; {}
4531: 21 42 45        LD      HL,$4542            
4534: C3 DD 7A        JP      $7ADD               ; {}
4537: CD 96 7A        CALL    $7A96               ; {}
453A: CA BB 53        JP      Z,$53BB             ; {}
453D: 3E 01           LD      A,$01               
453F: 02              LD      (BC),A              
4540: 18 EF           JR      $4531               ; {}
4542: FF              RST     0X38                
4543: C0              RET     NZ                  
4544: FF              RST     0X38                
4545: 80              ADD     A,B                 
4546: FF              RST     0X38                
4547: 40              LD      B,B                 
4548: 00              NOP                         
4549: C0              RET     NZ                  
454A: 00              NOP                         
454B: 80              ADD     A,B                 
454C: 00              NOP                         
454D: 40              LD      B,B                 
454E: 00              NOP                         
454F: 80              ADD     A,B                 
4550: F4                              
4551: 80              ADD     A,B                 
4552: 83              ADD     A,E                 
4553: 01 3E 16        LD      BC,$163E            
4556: EA BC D3        LD      ($D3BC),A           
4559: 21 8F 45        LD      HL,$458F            
455C: CD B3 7A        CALL    $7AB3               ; {}
455F: C3 9A 53        JP      $539A               ; {}
4562: CD 71 7A        CALL    $7A71               ; {}
4565: FE 04           CP      $04                 
4567: 28 06           JR      Z,$456F             ; {}
4569: 21 89 45        LD      HL,$4589            
456C: C3 DD 7A        JP      $7ADD               ; {}
456F: CD 96 7A        CALL    $7A96               ; {}
4572: CA BB 53        JP      Z,$53BB             ; {}
4575: FE 08           CP      $08                 
4577: 28 05           JR      Z,$457E             ; {}
4579: 3E 01           LD      A,$01               
457B: 02              LD      (BC),A              
457C: 18 EB           JR      $4569               ; {}
457E: AF              XOR     A                   
457F: 02              LD      (BC),A              
4580: 21 95 45        LD      HL,$4595            
4583: CD B3 7A        CALL    $7AB3               ; {}
4586: C3 75 7A        JP      $7A75               ; {}
4589: 00              NOP                         
458A: 28 00           JR      Z,$458C             ; {}
458C: 00              NOP                         
458D: FF              RST     0X38                
458E: F0 00           LD      A,($00)             
4590: 83              ADD     A,E                 
4591: 47              LD      B,A                 
4592: C0              RET     NZ                  
4593: 86              ADD     A,(HL)              
4594: 02              LD      (BC),A              
4595: 00              NOP                         
4596: 83              ADD     A,E                 
4597: 47              LD      B,A                 
4598: 00              NOP                         
4599: 87              ADD     A,A                 
459A: 02              LD      (BC),A              
459B: 21 A8 45        LD      HL,$45A8            
459E: C3 9A 53        JP      $539A               ; {}
45A1: CD 6D 7A        CALL    $7A6D               ; {}
45A4: C0              RET     NZ                  
45A5: C3 BB 53        JP      $53BB               ; {}
45A8: 27              DAA                         
45A9: 80              ADD     A,B                 
45AA: C2 48 86        JP      NZ,$8648            
45AD: 18 FA           JR      $45A9               ; {}
45AF: 61              LD      H,C                 
45B0: D3                              
45B1: FE 08           CP      $08                 
45B3: 28 04           JR      Z,$45B9             ; {}
45B5: A7              AND     A                   
45B6: C2 E6 53        JP      NZ,$53E6            ; {}
45B9: 21 C6 45        LD      HL,$45C6            
45BC: C3 9A 53        JP      $539A               ; {}
45BF: CD 6D 7A        CALL    $7A6D               ; {}
45C2: C0              RET     NZ                  
45C3: C3 BB 53        JP      $53BB               ; {}
45C6: 16 AB           LD      D,$AB               
45C8: 20 80           JR      NZ,$454A            ; {}
45CA: C6 05           ADD     $05                 
45CC: 21 E4 45        LD      HL,$45E4            
45CF: C3 9A 53        JP      $539A               ; {}
45D2: CD 6D 7A        CALL    $7A6D               ; {}
45D5: C0              RET     NZ                  
45D6: CD 71 7A        CALL    $7A71               ; {}
45D9: FE 02           CP      $02                 
45DB: CA BB 53        JP      Z,$53BB             ; {}
45DE: 21 EA 45        LD      HL,$45EA            
45E1: C3 75 7A        JP      $7A75               ; {}
45E4: 17              RLA                         
45E5: 80              ADD     A,B                 
45E6: 0B              DEC     BC                  
45E7: 00              NOP                         
45E8: 85              ADD     A,L                 
45E9: 10 17           STOP    $17                 
45EB: 80              ADD     A,B                 
45EC: 0E 00           LD      C,$00               
45EE: C5              PUSH    BC                  
45EF: 10 C3           STOP    $C3                 
45F1: 17              RLA                         
45F2: 7B              LD      A,E                 
45F3: 3E 17           LD      A,$17               
45F5: EA BC D3        LD      ($D3BC),A           
45F8: 21 2F D3        LD      HL,$D32F            
45FB: CB FE           SET     1,E                 
45FD: 21 32 46        LD      HL,$4632            
4600: CD CC 7A        CALL    $7ACC               ; {}
4603: CD 7B 7A        CALL    $7A7B               ; {}
4606: 21 37 46        LD      HL,$4637            
4609: CD B3 7A        CALL    $7AB3               ; {}
460C: C3 9A 53        JP      $539A               ; {}
460F: CD 71 7A        CALL    $7A71               ; {}
4612: FE 02           CP      $02                 
4614: 28 0F           JR      Z,$4625             ; {}
4616: 21 30 46        LD      HL,$4630            
4619: CD 0D 7B        CALL    $7B0D               ; {}
461C: 01 94 D3        LD      BC,$D394            
461F: 21 30 46        LD      HL,$4630            
4622: C3 DD 7A        JP      $7ADD               ; {}
4625: CD 96 7A        CALL    $7A96               ; {}
4628: CA 3D 46        JP      Z,$463D             ; {}
462B: 3E 01           LD      A,$01               
462D: 02              LD      (BC),A              
462E: 18 E6           JR      $4616               ; {}
4630: 00              NOP                         
4631: 21 45 0C        LD      HL,$0C45            
4634: 00              NOP                         
4635: 84              ADD     A,H                 
4636: 12              LD      (DE),A              
4637: 00              NOP                         
4638: 85              ADD     A,L                 
4639: 0B              DEC     BC                  
463A: 00              NOP                         
463B: 81              ADD     A,C                 
463C: 12              LD      (DE),A              
463D: 21 2F D3        LD      HL,$D32F            
4640: CB BE           RES     1,E                 
4642: 21 1D 43        LD      HL,$431D            
4645: CD 7B 7A        CALL    $7A7B               ; {}
4648: C3 B5 53        JP      $53B5               ; {}
464B: FA 61 D3        LD      A,($D361)           
464E: FE 13           CP      $13                 
4650: CA E6 53        JP      Z,$53E6             ; {}
4653: 3E 08           LD      A,$08               
4655: EA BC D3        LD      ($D3BC),A           
4658: 21 2F D3        LD      HL,$D32F            
465B: CB FE           SET     1,E                 
465D: 21 92 46        LD      HL,$4692            
4660: CD CC 7A        CALL    $7ACC               ; {}
4663: CD 7B 7A        CALL    $7A7B               ; {}
4666: 21 97 46        LD      HL,$4697            
4669: CD B3 7A        CALL    $7AB3               ; {}
466C: C3 9A 53        JP      $539A               ; {}
466F: CD 71 7A        CALL    $7A71               ; {}
4672: FE 02           CP      $02                 
4674: 28 0F           JR      Z,$4685             ; {}
4676: 21 90 46        LD      HL,$4690            
4679: CD 0D 7B        CALL    $7B0D               ; {}
467C: 01 94 D3        LD      BC,$D394            
467F: 21 90 46        LD      HL,$4690            
4682: C3 DD 7A        JP      $7ADD               ; {}
4685: CD 96 7A        CALL    $7A96               ; {}
4688: CA 3D 46        JP      Z,$463D             ; {}
468B: 3E 01           LD      A,$01               
468D: 02              LD      (BC),A              
468E: 18 E6           JR      $4676               ; {}
4690: FF              RST     0X38                
4691: D0              RET     NC                  
4692: 40              LD      B,B                 
4693: 0A              LD      A,(BC)              
4694: B0              OR      B                   
4695: 87              ADD     A,A                 
4696: 12              LD      (DE),A              
4697: 00              NOP                         
4698: 80              ADD     A,B                 
4699: 09              ADD     HL,BC               
469A: C0              RET     NZ                  
469B: 86              ADD     A,(HL)              
469C: 12              LD      (DE),A              
469D: 3E 05           LD      A,$05               
469F: EA BC D3        LD      ($D3BC),A           
46A2: F0 24           LD      A,($24)             
46A4: FE 77           CP      $77                 
46A6: 20 09           JR      NZ,$46B1            ; {}
46A8: 21 DB 46        LD      HL,$46DB            
46AB: CD B3 7A        CALL    $7AB3               ; {}
46AE: C3 9A 53        JP      $539A               ; {}
46B1: 21 E1 46        LD      HL,$46E1            
46B4: 18 F5           JR      $46AB               ; {}
46B6: CD 6D 7A        CALL    $7A6D               ; {}
46B9: C0              RET     NZ                  
46BA: 3E 03           LD      A,$03               
46BC: 12              LD      (DE),A              
46BD: CD 71 7A        CALL    $7A71               ; {}
46C0: FE 04           CP      $04                 
46C2: 28 06           JR      Z,$46CA             ; {}
46C4: 21 D5 46        LD      HL,$46D5            
46C7: C3 DD 7A        JP      $7ADD               ; {}
46CA: CD 96 7A        CALL    $7A96               ; {}
46CD: CA B5 53        JP      Z,$53B5             ; {}
46D0: 3E 01           LD      A,$01               
46D2: 02              LD      (BC),A              
46D3: 18 EF           JR      $46C4               ; {}
46D5: 00              NOP                         
46D6: 22              LD      (HLI),A             
46D7: 00              NOP                         
46D8: 19              ADD     HL,DE               
46D9: FF              RST     0X38                
46DA: C5              PUSH    BC                  
46DB: 00              NOP                         
46DC: 80              ADD     A,B                 
46DD: A4              AND     H                   
46DE: 7B              LD      A,E                 
46DF: 87              ADD     A,A                 
46E0: 03              INC     BC                  
46E1: 00              NOP                         
46E2: 80              ADD     A,B                 
46E3: F3              DI                          
46E4: 7B              LD      A,E                 
46E5: 87              ADD     A,A                 
46E6: 03              INC     BC                  
46E7: FA 61 D3        LD      A,($D361)           
46EA: A7              AND     A                   
46EB: C2 E6 53        JP      NZ,$53E6            ; {}
46EE: 21 FB 46        LD      HL,$46FB            
46F1: C3 9A 53        JP      $539A               ; {}
46F4: CD 6D 7A        CALL    $7A6D               ; {}
46F7: C0              RET     NZ                  
46F8: C3 BB 53        JP      $53BB               ; {}
46FB: 35              DEC     (HL)                
46FC: B0              OR      B                   
46FD: 60              LD      H,B                 
46FE: 20 C7           JR      NZ,$46C7            ; {}
4700: 04              INC     B                   
4701: 21 20 47        LD      HL,$4720            
4704: C3 9A 53        JP      $539A               ; {}
4707: CD 6D 7A        CALL    $7A6D               ; {}
470A: C0              RET     NZ                  
470B: CD 71 7A        CALL    $7A71               ; {}
470E: FE 03           CP      $03                 
4710: CA BB 53        JP      Z,$53BB             ; {}
4713: 21 1C 47        LD      HL,$471C            
4716: CD 60 7A        CALL    $7A60               ; {}
4719: C3 75 7A        JP      $7A75               ; {}
471C: 26 47           LD      H,$47               
471E: 2C              INC     L                   
471F: 47              LD      B,A                 
4720: 00              NOP                         
4721: B0              OR      B                   
4722: 19              ADD     HL,DE               
4723: 4F              LD      C,A                 
4724: C7              RST     0X00                
4725: 06 00           LD      B,$00               
4727: B0              OR      B                   
4728: 19              ADD     HL,DE               
4729: 7B              LD      A,E                 
472A: C7              RST     0X00                
472B: 06 00           LD      B,$00               
472D: B0              OR      B                   
472E: 29              ADD     HL,HL               
472F: 9D              SBC     L                   
4730: C7              RST     0X00                
4731: 03              INC     BC                  
4732: 21 3F 47        LD      HL,$473F            
4735: C3 9A 53        JP      $539A               ; {}
4738: CD 6D 7A        CALL    $7A6D               ; {}
473B: C0              RET     NZ                  
473C: C3 BB 53        JP      $53BB               ; {}
473F: 00              NOP                         
4740: 00              NOP                         
4741: 81              ADD     A,C                 
4742: BB              CP      E                   
4743: C7              RST     0X00                
4744: 20 3E           JR      NZ,$4784            ; {}
4746: 2A              LD      A,(HLI)             
4747: EA BC D3        LD      ($D3BC),A           
474A: 21 84 47        LD      HL,$4784            
474D: CD B3 7A        CALL    $7AB3               ; {}
4750: C3 95 53        JP      $5395               ; {}
4753: CD 71 7A        CALL    $7A71               ; {}
4756: FE 03           CP      $03                 
4758: 28 06           JR      Z,$4760             ; {}
475A: 21 7E 47        LD      HL,$477E            
475D: C3 DD 7A        JP      $7ADD               ; {}
4760: CD 96 7A        CALL    $7A96               ; {}
4763: CA BB 53        JP      Z,$53BB             ; {}
4766: FE 0E           CP      $0E                 
4768: 28 09           JR      Z,$4773             ; {}
476A: FE 1C           CP      $1C                 
476C: 28 05           JR      Z,$4773             ; {}
476E: 3E 01           LD      A,$01               
4770: 02              LD      (BC),A              
4771: 18 E7           JR      $475A               ; {}
4773: 21 7E 47        LD      HL,$477E            
4776: CD DD 7A        CALL    $7ADD               ; {}
4779: AF              XOR     A                   
477A: EA 94 D3        LD      ($D394),A           
477D: C9              RET                         
477E: 00              NOP                         
477F: 20 FF           JR      NZ,$4780            ; {}
4781: E8 FF           ADD     SP,$FF              
4783: 90              SUB     B                   
4784: 00              NOP                         
4785: 80              ADD     A,B                 
4786: D7              RST     0X10                
4787: 68              LD      L,B                 
4788: 87              ADD     A,A                 
4789: 01 21 A2        LD      BC,$A221            
478C: 47              LD      B,A                 
478D: C3 9A 53        JP      $539A               ; {}
4790: CD 6D 7A        CALL    $7A6D               ; {}
4793: C0              RET     NZ                  
4794: CD 71 7A        CALL    $7A71               ; {}
4797: FE 02           CP      $02                 
4799: CA B5 53        JP      Z,$53B5             ; {}
479C: 21 A8 47        LD      HL,$47A8            
479F: C3 75 7A        JP      $7A75               ; {}
47A2: 2F              CPL                         
47A3: 80              ADD     A,B                 
47A4: 60              LD      H,B                 
47A5: E0 86           LDFF00  ($86),A             
47A7: 14              INC     D                   
47A8: 2F              CPL                         
47A9: 80              ADD     A,B                 
47AA: 10 E0           STOP    $E0                 
47AC: 86              ADD     A,(HL)              
47AD: 14              INC     D                   
47AE: 21 D1 47        LD      HL,$47D1            
47B1: C3 95 53        JP      $5395               ; {}
47B4: CD 6D 7A        CALL    $7A6D               ; {}
47B7: C0              RET     NZ                  
47B8: CD 71 7A        CALL    $7A71               ; {}
47BB: FE 05           CP      $05                 
47BD: CA BB 53        JP      Z,$53BB             ; {}
47C0: 21 C9 47        LD      HL,$47C9            
47C3: CD 60 7A        CALL    $7A60               ; {}
47C6: C3 75 7A        JP      $7A75               ; {}
47C9: D7              RST     0X10                
47CA: 47              LD      B,A                 
47CB: DD                              
47CC: 47              LD      B,A                 
47CD: E3                              
47CE: 47              LD      B,A                 
47CF: E9              JP      (HL)                
47D0: 47              LD      B,A                 
47D1: 00              NOP                         
47D2: 80              ADD     A,B                 
47D3: C1              POP     BC                  
47D4: A7              AND     A                   
47D5: 87              ADD     A,A                 
47D6: 06 00           LD      B,$00               
47D8: 80              ADD     A,B                 
47D9: C1              POP     BC                  
47DA: B1              OR      C                   
47DB: 87              ADD     A,A                 
47DC: 06 00           LD      B,$00               
47DE: 80              ADD     A,B                 
47DF: C1              POP     BC                  
47E0: BA              CP      D                   
47E1: 87              ADD     A,A                 
47E2: 06 00           LD      B,$00               
47E4: 80              ADD     A,B                 
47E5: C1              POP     BC                  
47E6: BE              CP      (HL)                
47E7: 87              ADD     A,A                 
47E8: 06 00           LD      B,$00               
47EA: 80              ADD     A,B                 
47EB: A3              AND     E                   
47EC: C5              PUSH    BC                  
47ED: 87              ADD     A,A                 
47EE: 20 FA           JR      NZ,$47EA            ; {}
47F0: 61              LD      H,C                 
47F1: D3                              
47F2: FE 1A           CP      $1A                 
47F4: CA E6 53        JP      Z,$53E6             ; {}
47F7: 21 0F 48        LD      HL,$480F            
47FA: C3 9A 53        JP      $539A               ; {}
47FD: CD 6D 7A        CALL    $7A6D               ; {}
4800: C0              RET     NZ                  
4801: CD 71 7A        CALL    $7A71               ; {}
4804: FE 02           CP      $02                 
4806: CA B5 53        JP      Z,$53B5             ; {}
4809: 21 15 48        LD      HL,$4815            
480C: C3 DF 53        JP      $53DF               ; {}
480F: 00              NOP                         
4810: 80              ADD     A,B                 
4811: 34              INC     (HL)                
4812: 90              SUB     B                   
4813: 87              ADD     A,A                 
4814: 01 C8 07        LD      BC,$07C8            
4817: 04              INC     B                   
4818: 3E 03           LD      A,$03               
481A: EA BC D3        LD      ($D3BC),A           
481D: 21 63 48        LD      HL,$4863            
4820: CD B3 7A        CALL    $7AB3               ; {}
4823: C3 95 53        JP      $5395               ; {}
4826: CD 6D 7A        CALL    $7A6D               ; {}
4829: C0              RET     NZ                  
482A: 3E 04           LD      A,$04               
482C: 12              LD      (DE),A              
482D: CD 71 7A        CALL    $7A71               ; {}
4830: FE 08           CP      $08                 
4832: 28 06           JR      Z,$483A             ; {}
4834: 21 55 48        LD      HL,$4855            
4837: C3 DD 7A        JP      $7ADD               ; {}
483A: CD 96 7A        CALL    $7A96               ; {}
483D: CA B5 53        JP      Z,$53B5             ; {}
4840: FE 02           CP      $02                 
4842: 28 0C           JR      Z,$4850             ; {}
4844: 21 6F 48        LD      HL,$486F            
4847: CD B3 7A        CALL    $7AB3               ; {}
484A: 3E 04           LD      A,$04               
484C: 02              LD      (BC),A              
484D: C3 75 7A        JP      $7A75               ; {}
4850: 21 69 48        LD      HL,$4869            
4853: 18 F2           JR      $4847               ; {}
4855: 00              NOP                         
4856: 2A              LD      A,(HLI)             
4857: 00              NOP                         
4858: 2E 00           LD      L,$00               
485A: 25              DEC     H                   
485B: 00              NOP                         
485C: 07              RLCA                        
485D: 00              NOP                         
485E: 15              DEC     D                   
485F: 00              NOP                         
4860: 17              RLA                         
4861: 00              NOP                         
4862: 13              INC     DE                  
4863: 00              NOP                         
4864: 00              NOP                         
4865: 4C              LD      C,H                 
4866: F7              RST     0X30                
4867: 86              ADD     A,(HL)              
4868: 04              INC     B                   
4869: 00              NOP                         
486A: 40              LD      B,B                 
486B: 40              LD      B,B                 
486C: 7B              LD      A,E                 
486D: 87              ADD     A,A                 
486E: 04              INC     B                   
486F: 00              NOP                         
4870: 80              ADD     A,B                 
4871: 10 7B           STOP    $7B                 
4873: 87              ADD     A,A                 
4874: 04              INC     B                   
4875: 3E 2C           LD      A,$2C               
4877: EA BC D3        LD      ($D3BC),A           
487A: 21 C3 48        LD      HL,$48C3            
487D: CD B3 7A        CALL    $7AB3               ; {}
4880: C3 9A 53        JP      $539A               ; {}
4883: CD 71 7A        CALL    $7A71               ; {}
4886: FE 03           CP      $03                 
4888: 28 0A           JR      Z,$4894             ; {}
488A: FE 05           CP      $05                 
488C: 28 22           JR      Z,$48B0             ; {}
488E: 21 BB 48        LD      HL,$48BB            
4891: C3 DD 7A        JP      $7ADD               ; {}
4894: CD 96 7A        CALL    $7A96               ; {}
4897: FE 18           CP      $18                 
4899: 28 09           JR      Z,$48A4             ; {}
489B: FE 17           CP      $17                 
489D: 28 11           JR      Z,$48B0             ; {}
489F: 3E 01           LD      A,$01               
48A1: 02              LD      (BC),A              
48A2: 18 EA           JR      $488E               ; {}
48A4: 3E 02           LD      A,$02               
48A6: 02              LD      (BC),A              
48A7: 21 C9 48        LD      HL,$48C9            
48AA: CD B3 7A        CALL    $7AB3               ; {}
48AD: C3 75 7A        JP      $7A75               ; {}
48B0: CD 96 7A        CALL    $7A96               ; {}
48B3: CA BB 53        JP      Z,$53BB             ; {}
48B6: 3E 03           LD      A,$03               
48B8: 02              LD      (BC),A              
48B9: 18 D3           JR      $488E               ; {}
48BB: 00              NOP                         
48BC: AE              XOR     (HL)                
48BD: FF              RST     0X38                
48BE: 60              LD      H,B                 
48BF: 00              NOP                         
48C0: AA              XOR     D                   
48C1: FF              RST     0X38                
48C2: 60              LD      H,B                 
48C3: 00              NOP                         
48C4: 40              LD      B,B                 
48C5: 0C              INC     C                   
48C6: 00              NOP                         
48C7: 85              ADD     A,L                 
48C8: 01 00 40        LD      BC,$4000            
48CB: A4              AND     H                   
48CC: 40              LD      B,B                 
48CD: 86              ADD     A,(HL)              
48CE: 01 3E 08        LD      BC,$083E            
48D1: EA BC D3        LD      ($D3BC),A           
48D4: 21 01 49        LD      HL,$4901            
48D7: C3 9A 53        JP      $539A               ; {}
48DA: CD 6D 7A        CALL    $7A6D               ; {}
48DD: C0              RET     NZ                  
48DE: 3E 79           LD      A,$79               
48E0: E0 11           LDFF00  ($11),A             
48E2: CD 71 7A        CALL    $7A71               ; {}
48E5: FE 03           CP      $03                 
48E7: 28 09           JR      Z,$48F2             ; {}
48E9: 21 FD 48        LD      HL,$48FD            
48EC: CD 60 7A        CALL    $7A60               ; {}
48EF: C3 DF 53        JP      $53DF               ; {}
48F2: CD 96 7A        CALL    $7A96               ; {}
48F5: CA BB 53        JP      Z,$53BB             ; {}
48F8: 3E 02           LD      A,$02               
48FA: 02              LD      (BC),A              
48FB: 18 EC           JR      $48E9               ; {}
48FD: 07              RLCA                        
48FE: 49              LD      C,C                 
48FF: 04              INC     B                   
4900: 49              LD      C,C                 
4901: 00              NOP                         
4902: 79              LD      A,C                 
4903: E0 C0           LDFF00  ($C0),A             
4905: C4 02 C0        CALL    NZ,$C002            
4908: C4 0C 21        CALL    NZ,$210C            
490B: 2D              DEC     L                   
490C: 49              LD      C,C                 
490D: C3 95 53        JP      $5395               ; {}
4910: CD 6D 7A        CALL    $7A6D               ; {}
4913: C0              RET     NZ                  
4914: CD 71 7A        CALL    $7A71               ; {}
4917: FE 05           CP      $05                 
4919: CA BB 53        JP      Z,$53BB             ; {}
491C: 21 25 49        LD      HL,$4925            
491F: CD 60 7A        CALL    $7A60               ; {}
4922: C3 DF 53        JP      $53DF               ; {}
4925: 33              INC     SP                  
4926: 49              LD      C,C                 
4927: 33              INC     SP                  
4928: 49              LD      C,C                 
4929: 36 49           LD      (HL),$49            
492B: 36 49           LD      (HL),$49            
492D: 1F              RRA                         
492E: A6              AND     (HL)                
492F: E1              POP     HL                  
4930: 00              NOP                         
4931: C7              RST     0X00                
4932: 10 A0           STOP    $A0                 
4934: C6 09           ADD     $09                 
4936: 00              NOP                         
4937: C6 18           ADD     $18                 
4939: 3E 0A           LD      A,$0A               
493B: EA BC D3        LD      ($D3BC),A           
493E: 21 6F 49        LD      HL,$496F            
4941: CD B3 7A        CALL    $7AB3               ; {}
4944: C3 95 53        JP      $5395               ; {}
4947: CD 71 7A        CALL    $7A71               ; {}
494A: FE 09           CP      $09                 
494C: 28 06           JR      Z,$4954             ; {}
494E: 21 5F 49        LD      HL,$495F            
4951: C3 DD 7A        JP      $7ADD               ; {}
4954: CD 96 7A        CALL    $7A96               ; {}
4957: CA B5 53        JP      Z,$53B5             ; {}
495A: 3E 01           LD      A,$01               
495C: 02              LD      (BC),A              
495D: 18 EF           JR      $494E               ; {}
495F: 00              NOP                         
4960: 30 00           JR      NC,$4962            ; {}
4962: 60              LD      H,B                 
4963: 00              NOP                         
4964: 60              LD      H,B                 
4965: 00              NOP                         
4966: 30 FF           JR      NC,$4967            ; {}
4968: C0              RET     NZ                  
4969: FF              RST     0X38                
496A: 80              ADD     A,B                 
496B: FF              RST     0X38                
496C: 80              ADD     A,B                 
496D: FF              RST     0X38                
496E: C0              RET     NZ                  
496F: 00              NOP                         
4970: 80              ADD     A,B                 
4971: 0B              DEC     BC                  
4972: 20 86           JR      NZ,$48FA            ; {}
4974: 01 FA 61        LD      BC,$61FA            
4977: D3                              
4978: FE 20           CP      $20                 
497A: 28 04           JR      Z,$4980             ; {}
497C: A7              AND     A                   
497D: C2 E6 53        JP      NZ,$53E6            ; {}
4980: 3E 08           LD      A,$08               
4982: EA BC D3        LD      ($D3BC),A           
4985: 21 AA 49        LD      HL,$49AA            
4988: CD B3 7A        CALL    $7AB3               ; {}
498B: C3 9A 53        JP      $539A               ; {}
498E: CD 71 7A        CALL    $7A71               ; {}
4991: FE 03           CP      $03                 
4993: 28 06           JR      Z,$499B             ; {}
4995: 21 A6 49        LD      HL,$49A6            
4998: C3 DD 7A        JP      $7ADD               ; {}
499B: CD 96 7A        CALL    $7A96               ; {}
499E: CA BB 53        JP      Z,$53BB             ; {}
49A1: 3E 01           LD      A,$01               
49A3: 02              LD      (BC),A              
49A4: 18 EF           JR      $4995               ; {}
49A6: 00              NOP                         
49A7: C0              RET     NZ                  
49A8: FF              RST     0X38                
49A9: A0              AND     B                   
49AA: 00              NOP                         
49AB: 80              ADD     A,B                 
49AC: F1              POP     AF                  
49AD: 80              ADD     A,B                 
49AE: 83              ADD     A,E                 
49AF: 01 3E 1C        LD      BC,$1C3E            
49B2: EA BC D3        LD      ($D3BC),A           
49B5: 21 F6 49        LD      HL,$49F6            
49B8: CD B3 7A        CALL    $7AB3               ; {}
49BB: C3 9A 53        JP      $539A               ; {}
49BE: CD 71 7A        CALL    $7A71               ; {}
49C1: FE 02           CP      $02                 
49C3: 28 06           JR      Z,$49CB             ; {}
49C5: 21 F4 49        LD      HL,$49F4            
49C8: C3 DD 7A        JP      $7ADD               ; {}
49CB: CD 96 7A        CALL    $7A96               ; {}
49CE: CA B5 53        JP      Z,$53B5             ; {}
49D1: FE 14           CP      $14                 
49D3: 28 09           JR      Z,$49DE             ; {}
49D5: FE 0A           CP      $0A                 
49D7: 28 10           JR      Z,$49E9             ; {}
49D9: 3E 01           LD      A,$01               
49DB: 02              LD      (BC),A              
49DC: 18 E7           JR      $49C5               ; {}
49DE: AF              XOR     A                   
49DF: 02              LD      (BC),A              
49E0: 21 FC 49        LD      HL,$49FC            
49E3: CD B3 7A        CALL    $7AB3               ; {}
49E6: C3 75 7A        JP      $7A75               ; {}
49E9: AF              XOR     A                   
49EA: 02              LD      (BC),A              
49EB: 21 02 4A        LD      HL,$4A02            
49EE: CD B3 7A        CALL    $7AB3               ; {}
49F1: C3 75 7A        JP      $7A75               ; {}
49F4: FF              RST     0X38                
49F5: FF              RST     0X38                
49F6: 00              NOP                         
49F7: 00              NOP                         
49F8: 19              ADD     HL,DE               
49F9: B0              OR      B                   
49FA: 87              ADD     A,A                 
49FB: 01 00 00        LD      BC,$0000            
49FE: 62              LD      H,D                 
49FF: A7              AND     A                   
4A00: 87              ADD     A,A                 
4A01: 01 00 00        LD      BC,$0000            
4A04: 10 A7           STOP    $A7                 
4A06: 87              ADD     A,A                 
4A07: 01 FA 61        LD      BC,$61FA            
4A0A: D3                              
4A0B: FE 22           CP      $22                 
4A0D: CA E6 53        JP      Z,$53E6             ; {}
4A10: 01 D7 D3        LD      BC,$D3D7            
4A13: CD 71 7A        CALL    $7A71               ; {}
4A16: FE 04           CP      $04                 
4A18: 30 06           JR      NC,$4A20            ; {}
4A1A: 21 52 4A        LD      HL,$4A52            
4A1D: C3 9A 53        JP      $539A               ; {}
4A20: FE 06           CP      $06                 
4A22: 30 06           JR      NC,$4A2A            ; {}
4A24: 21 58 4A        LD      HL,$4A58            
4A27: C3 9A 53        JP      $539A               ; {}
4A2A: FE 08           CP      $08                 
4A2C: 30 06           JR      NC,$4A34            ; {}
4A2E: 21 5E 4A        LD      HL,$4A5E            
4A31: C3 9A 53        JP      $539A               ; {}
4A34: FE 09           CP      $09                 
4A36: 30 06           JR      NC,$4A3E            ; {}
4A38: 21 64 4A        LD      HL,$4A64            
4A3B: C3 9A 53        JP      $539A               ; {}
4A3E: FE 0B           CP      $0B                 
4A40: 30 02           JR      NC,$4A44            ; {}
4A42: 18 EA           JR      $4A2E               ; {}
4A44: FE 0D           CP      $0D                 
4A46: 28 02           JR      Z,$4A4A             ; {}
4A48: 18 DA           JR      $4A24               ; {}
4A4A: 3E 01           LD      A,$01               
4A4C: 02              LD      (BC),A              
4A4D: 18 CB           JR      $4A1A               ; {}
4A4F: C3 BB 53        JP      $53BB               ; {}
4A52: 15              DEC     D                   
4A53: 38 30           JR      C,$4A85             ; {}
4A55: 40              LD      B,B                 
4A56: C6 02           ADD     $02                 
4A58: 15              DEC     D                   
4A59: 38 40           JR      C,$4A9B             ; {}
4A5B: 3C              INC     A                   
4A5C: C6 02           ADD     $02                 
4A5E: 15              DEC     D                   
4A5F: 38 60           JR      C,$4AC1             ; {}
4A61: 38 C6           JR      C,$4A29             ; {}
4A63: 02              LD      (BC),A              
4A64: 15              DEC     D                   
4A65: 38 90           JR      C,$49F7             ; {}
4A67: 34              INC     (HL)                
4A68: C6 02           ADD     $02                 
4A6A: 15              DEC     D                   
4A6B: 38 D0           JR      C,$4A3D             ; {}
4A6D: 30 C6           JR      NC,$4A35            ; {}
4A6F: 02              LD      (BC),A              
4A70: 21 2F D3        LD      HL,$D32F            
4A73: CB FE           SET     1,E                 
4A75: 21 AD 4A        LD      HL,$4AAD            
4A78: C3 95 53        JP      $5395               ; {}
4A7B: CD 6D 7A        CALL    $7A6D               ; {}
4A7E: C0              RET     NZ                  
4A7F: CD 71 7A        CALL    $7A71               ; {}
4A82: FE 08           CP      $08                 
4A84: 28 11           JR      Z,$4A97             ; {}
4A86: 21 9F 4A        LD      HL,$4A9F            
4A89: CD 60 7A        CALL    $7A60               ; {}
4A8C: FA 94 D3        LD      A,($D394)           
4A8F: E6 01           AND     $01                 
4A91: C2 7B 7A        JP      NZ,$7A7B            ; {}
4A94: C3 75 7A        JP      $7A75               ; {}
4A97: 21 2F D3        LD      HL,$D32F            
4A9A: CB BE           RES     1,E                 
4A9C: C3 B5 53        JP      $53B5               ; {}
4A9F: B3              OR      E                   
4AA0: 4A              LD      C,D                 
4AA1: B8              CP      B                   
4AA2: 4A              LD      C,D                 
4AA3: BE              CP      (HL)                
4AA4: 4A              LD      C,D                 
4AA5: C3 4A C9        JP      $C94A               
4AA8: 4A              LD      C,D                 
4AA9: CE 4A           ADC     $4A                 
4AAB: D4 4A 00        CALL    NC,$004A            
4AAE: 80              ADD     A,B                 
4AAF: E2              LDFF00  (C),A               
4AB0: A7              AND     A                   
4AB1: 87              ADD     A,A                 
4AB2: 09              ADD     HL,BC               
4AB3: 80              ADD     A,B                 
4AB4: E2              LDFF00  (C),A               
4AB5: A2              AND     D                   
4AB6: 87              ADD     A,A                 
4AB7: 08 00 80        LD      ($8000),SP          
4ABA: E2              LDFF00  (C),A               
4ABB: 90              SUB     B                   
4ABC: 87              ADD     A,A                 
4ABD: 08 80 E2        LD      ($E280),SP          
4AC0: 7B              LD      A,E                 
4AC1: 87              ADD     A,A                 
4AC2: 08 00 80        LD      ($8000),SP          
4AC5: B2              OR      D                   
4AC6: 59              LD      E,C                 
4AC7: 87              ADD     A,A                 
4AC8: 09              ADD     HL,BC               
4AC9: 80              ADD     A,B                 
4ACA: E2              LDFF00  (C),A               
4ACB: 97              SUB     A                   
4ACC: 87              ADD     A,A                 
4ACD: 0A              LD      A,(BC)              
4ACE: 00              NOP                         
4ACF: 80              ADD     A,B                 
4AD0: E2              LDFF00  (C),A               
4AD1: AC              XOR     H                   
4AD2: 87              ADD     A,A                 
4AD3: 0B              DEC     BC                  
4AD4: 80              ADD     A,B                 
4AD5: E2              LDFF00  (C),A               
4AD6: BE              CP      (HL)                
4AD7: 87              ADD     A,A                 
4AD8: 10 21           STOP    $21                 
4ADA: E6 4A           AND     $4A                 
4ADC: C3 9A 53        JP      $539A               ; {}
4ADF: CD 6D 7A        CALL    $7A6D               ; {}
4AE2: C0              RET     NZ                  
4AE3: C3 BB 53        JP      $53BB               ; {}
4AE6: 27              DAA                         
4AE7: 80              ADD     A,B                 
4AE8: 83              ADD     A,E                 
4AE9: 00              NOP                         
4AEA: 86              ADD     A,(HL)              
4AEB: 18 3E           JR      $4B2B               ; {}
4AED: 07              RLCA                        
4AEE: EA BC D3        LD      ($D3BC),A           
4AF1: 21 2B 4B        LD      HL,$4B2B            
4AF4: C3 95 53        JP      $5395               ; {}
4AF7: CD 6D 7A        CALL    $7A6D               ; {}
4AFA: C0              RET     NZ                  
4AFB: CD 71 7A        CALL    $7A71               ; {}
4AFE: FE 06           CP      $06                 
4B00: 28 0D           JR      Z,$4B0F             ; {}
4B02: FE 07           CP      $07                 
4B04: 28 14           JR      Z,$4B1A             ; {}
4B06: 21 1F 4B        LD      HL,$4B1F            
4B09: CD 60 7A        CALL    $7A60               ; {}
4B0C: C3 DF 53        JP      $53DF               ; {}
4B0F: CD 96 7A        CALL    $7A96               ; {}
4B12: CA B5 53        JP      Z,$53B5             ; {}
4B15: 3E 06           LD      A,$06               
4B17: 02              LD      (BC),A              
4B18: 18 EC           JR      $4B06               ; {}
4B1A: 3E 03           LD      A,$03               
4B1C: 02              LD      (BC),A              
4B1D: 18 E7           JR      $4B06               ; {}
4B1F: 31 4B 34        LD      SP,$344B            
4B22: 4B              LD      C,E                 
4B23: 37              SCF                         
4B24: 4B              LD      C,E                 
4B25: 3A              LD      A,(HLD)             
4B26: 4B              LD      C,E                 
4B27: 3D              DEC     A                   
4B28: 4B              LD      C,E                 
4B29: 40              LD      B,B                 
4B2A: 4B              LD      C,E                 
4B2B: 00              NOP                         
4B2C: 80              ADD     A,B                 
4B2D: A5              AND     L                   
4B2E: 06 87           LD      B,$87               
4B30: 02              LD      (BC),A              
4B31: 21 07 02        LD      HL,$0207            
4B34: 39              ADD     HL,SP               
4B35: 07              RLCA                        
4B36: 02              LD      (BC),A              
4B37: 4F              LD      C,A                 
4B38: 07              RLCA                        
4B39: 02              LD      (BC),A              
4B3A: 62              LD      H,D                 
4B3B: 07              RLCA                        
4B3C: 02              LD      (BC),A              
4B3D: 74              LD      (HL),H              
4B3E: 07              RLCA                        
4B3F: 02              LD      (BC),A              
4B40: 06 07           LD      B,$07               
4B42: 02              LD      (BC),A              
4B43: 3E 0E           LD      A,$0E               
4B45: EA BC D3        LD      ($D3BC),A           
4B48: 21 85 4B        LD      HL,$4B85            
4B4B: CD B3 7A        CALL    $7AB3               ; {}
4B4E: C3 95 53        JP      $5395               ; {}
4B51: CD 6D 7A        CALL    $7A6D               ; {}
4B54: C0              RET     NZ                  
4B55: 3E 03           LD      A,$03               
4B57: 12              LD      (DE),A              
4B58: CD 71 7A        CALL    $7A71               ; {}
4B5B: FE 04           CP      $04                 
4B5D: 28 06           JR      Z,$4B65             ; {}
4B5F: 21 7F 4B        LD      HL,$4B7F            
4B62: C3 DD 7A        JP      $7ADD               ; {}
4B65: CD 96 7A        CALL    $7A96               ; {}
4B68: CA BB 53        JP      Z,$53BB             ; {}
4B6B: FE 09           CP      $09                 
4B6D: 28 05           JR      Z,$4B74             ; {}
4B6F: 3E 01           LD      A,$01               
4B71: 02              LD      (BC),A              
4B72: 18 EB           JR      $4B5F               ; {}
4B74: AF              XOR     A                   
4B75: 02              LD      (BC),A              
4B76: 21 8B 4B        LD      HL,$4B8B            
4B79: CD B3 7A        CALL    $7AB3               ; {}
4B7C: C3 75 7A        JP      $7A75               ; {}
4B7F: FF              RST     0X38                
4B80: E0 00           LDFF00  ($00),A             
4B82: 20 FF           JR      NZ,$4B83            ; {}
4B84: FC                              
4B85: 00              NOP                         
4B86: 00              NOP                         
4B87: 0C              INC     C                   
4B88: F0 87           LD      A,($87)             
4B8A: 03              INC     BC                  
4B8B: 00              NOP                         
4B8C: 00              NOP                         
4B8D: A7              AND     A                   
4B8E: DC 87 03        CALL    C,$0387             
4B91: 21 AB 4B        LD      HL,$4BAB            
4B94: C3 9A 53        JP      $539A               ; {}
4B97: CD 6D 7A        CALL    $7A6D               ; {}
4B9A: C0              RET     NZ                  
4B9B: CD 71 7A        CALL    $7A71               ; {}
4B9E: FE 02           CP      $02                 
4BA0: CA B5 53        JP      Z,$53B5             ; {}
4BA3: 3E 1E           LD      A,$1E               
4BA5: E0 10           LDFF00  ($10),A             
4BA7: 3E 18           LD      A,$18               
4BA9: 12              LD      (DE),A              
4BAA: C9              RET                         
4BAB: 14              INC     D                   
4BAC: 40              LD      B,B                 
4BAD: C0              RET     NZ                  
4BAE: 00              NOP                         
4BAF: 81              ADD     A,C                 
4BB0: 0C              INC     C                   
4BB1: 21 DE 4B        LD      HL,$4BDE            
4BB4: C3 9A 53        JP      $539A               ; {}
4BB7: CD 6D 7A        CALL    $7A6D               ; {}
4BBA: C0              RET     NZ                  
4BBB: CD 71 7A        CALL    $7A71               ; {}
4BBE: FE 08           CP      $08                 
4BC0: CA BB 53        JP      Z,$53BB             ; {}
4BC3: 21 D0 4B        LD      HL,$4BD0            
4BC6: CD 60 7A        CALL    $7A60               ; {}
4BC9: 3E BD           LD      A,$BD               
4BCB: E0 11           LDFF00  ($11),A             
4BCD: C3 DF 53        JP      $53DF               ; {}
4BD0: E4                              
4BD1: 4B              LD      C,E                 
4BD2: E7              RST     0X20                
4BD3: 4B              LD      C,E                 
4BD4: EA 4B ED        LD      ($ED4B),A           
4BD7: 4B              LD      C,E                 
4BD8: F0 4B           LD      A,($4B)             
4BDA: F3              DI                          
4BDB: 4B              LD      C,E                 
4BDC: F6 4B           OR      $4B                 
4BDE: 00              NOP                         
4BDF: BD              CP      L                   
4BE0: F0 E0           LD      A,($E0)             
4BE2: C7              RST     0X00                
4BE3: 0C              INC     C                   
4BE4: E0 C7           LDFF00  ($C7),A             
4BE6: 03              INC     BC                  
4BE7: C0              RET     NZ                  
4BE8: C7              RST     0X00                
4BE9: 03              INC     BC                  
4BEA: A0              AND     B                   
4BEB: C7              RST     0X00                
4BEC: 04              INC     B                   
4BED: 80              ADD     A,B                 
4BEE: C7              RST     0X00                
4BEF: 04              INC     B                   
4BF0: 60              LD      H,B                 
4BF1: C7              RST     0X00                
4BF2: 05              DEC     B                   
4BF3: 40              LD      B,B                 
4BF4: C7              RST     0X00                
4BF5: 06 20           LD      B,$20               
4BF7: C7              RST     0X00                
4BF8: 03              INC     BC                  
4BF9: 21 13 4C        LD      HL,$4C13            
4BFC: C3 9A 53        JP      $539A               ; {}
4BFF: CD 6D 7A        CALL    $7A6D               ; {}
4C02: C0              RET     NZ                  
4C03: CD 71 7A        CALL    $7A71               ; {}
4C06: FE 02           CP      $02                 
4C08: CA BB 53        JP      Z,$53BB             ; {}
4C0B: 3E 1E           LD      A,$1E               
4C0D: E0 10           LDFF00  ($10),A             
4C0F: 3E 06           LD      A,$06               
4C11: 12              LD      (DE),A              
4C12: C9              RET                         
4C13: 17              RLA                         
4C14: 96              SUB     (HL)                
4C15: 49              LD      C,C                 
4C16: 60              LD      H,B                 
4C17: C6 04           ADD     $04                 
4C19: 21 26 4C        LD      HL,$4C26            
4C1C: C3 9A 53        JP      $539A               ; {}
4C1F: CD 6D 7A        CALL    $7A6D               ; {}
4C22: C0              RET     NZ                  
4C23: C3 B5 53        JP      $53B5               ; {}
4C26: 16 00           LD      D,$00               
4C28: F0 00           LD      A,($00)             
4C2A: C2 10 3E        JP      NZ,$3E10            
4C2D: 2C              INC     L                   
4C2E: EA BC D3        LD      ($D3BC),A           
4C31: 21 75 4C        LD      HL,$4C75            
4C34: CD B3 7A        CALL    $7AB3               ; {}
4C37: C3 9A 53        JP      $539A               ; {}
4C3A: CD 71 7A        CALL    $7A71               ; {}
4C3D: FE 0B           CP      $0B                 
4C3F: 28 06           JR      Z,$4C47             ; {}
4C41: 21 61 4C        LD      HL,$4C61            
4C44: C3 DD 7A        JP      $7ADD               ; {}
4C47: CD 96 7A        CALL    $7A96               ; {}
4C4A: CA B5 53        JP      Z,$53B5             ; {}
4C4D: FE 0C           CP      $0C                 
4C4F: 28 05           JR      Z,$4C56             ; {}
4C51: 3E 01           LD      A,$01               
4C53: 02              LD      (BC),A              
4C54: 18 EB           JR      $4C41               ; {}
4C56: AF              XOR     A                   
4C57: 02              LD      (BC),A              
4C58: 21 7B 4C        LD      HL,$4C7B            
4C5B: CD B3 7A        CALL    $7AB3               ; {}
4C5E: C3 75 7A        JP      $7A75               ; {}
4C61: 00              NOP                         
4C62: 08 FF F0        LD      ($F0FF),SP          
4C65: 00              NOP                         
4C66: 08 FF FC        LD      ($FCFF),SP          
4C69: 00              NOP                         
4C6A: 06 FF           LD      B,$FF               
4C6C: F8 00           LDHL    SP,$00              
4C6E: 06 FF           LD      B,$FF               
4C70: FA 00 08        LD      A,($0800)           
4C73: FF              RST     0X38                
4C74: FF              RST     0X38                
4C75: 00              NOP                         
4C76: 00              NOP                         
4C77: 0F              RRCA                        
4C78: D0              RET     NC                  
4C79: 87              ADD     A,A                 
4C7A: 02              LD      (BC),A              
4C7B: 00              NOP                         
4C7C: 00              NOP                         
4C7D: F7              RST     0X30                
4C7E: F0 87           LD      A,($87)             
4C80: 04              INC     B                   
4C81: 3E 22           LD      A,$22               
4C83: EA BC D3        LD      ($D3BC),A           
4C86: 21 CF 4C        LD      HL,$4CCF            
4C89: CD B3 7A        CALL    $7AB3               ; {}
4C8C: C3 95 53        JP      $5395               ; {}
4C8F: CD 71 7A        CALL    $7A71               ; {}
4C92: FE 07           CP      $07                 
4C94: 28 06           JR      Z,$4C9C             ; {}
4C96: 21 C3 4C        LD      HL,$4CC3            
4C99: C3 DD 7A        JP      $7ADD               ; {}
4C9C: CD 96 7A        CALL    $7A96               ; {}
4C9F: CA BB 53        JP      Z,$53BB             ; {}
4CA2: FE 1E           CP      $1E                 
4CA4: 28 0C           JR      Z,$4CB2             ; {}
4CA6: FE 06           CP      $06                 
4CA8: 28 14           JR      Z,$4CBE             ; {}
4CAA: 3E 01           LD      A,$01               
4CAC: 01 94 D3        LD      BC,$D394            
4CAF: 02              LD      (BC),A              
4CB0: 18 E4           JR      $4C96               ; {}
4CB2: 21 D5 4C        LD      HL,$4CD5            
4CB5: 3E 01           LD      A,$01               
4CB7: 02              LD      (BC),A              
4CB8: CD B3 7A        CALL    $7AB3               ; {}
4CBB: C3 75 7A        JP      $7A75               ; {}
4CBE: 21 DB 4C        LD      HL,$4CDB            
4CC1: 18 F2           JR      $4CB5               ; {}
4CC3: 00              NOP                         
4CC4: 02              LD      (BC),A              
4CC5: 00              NOP                         
4CC6: 01 FF F0        LD      BC,$F0FF            
4CC9: FF              RST     0X38                
4CCA: E0 FF           LDFF00  ($FF),A             
4CCC: C0              RET     NZ                  
4CCD: 00              NOP                         
4CCE: 71              LD      (HL),C              
4CCF: 00              NOP                         
4CD0: 00              NOP                         
4CD1: 0F              RRCA                        
4CD2: 00              NOP                         
4CD3: 87              ADD     A,A                 
4CD4: 01 00 00        LD      BC,$0000            
4CD7: 40              LD      B,B                 
4CD8: 10 87           STOP    $87                 
4CDA: 01 00 00        LD      BC,$0000            
4CDD: 47              LD      B,A                 
4CDE: 70              LD      (HL),B              
4CDF: 87              ADD     A,A                 
4CE0: 01 3E 03        LD      BC,$033E            
4CE3: EA BC D3        LD      ($D3BC),A           
4CE6: 21 20 4D        LD      HL,$4D20            
4CE9: CD B3 7A        CALL    $7AB3               ; {}
4CEC: C3 95 53        JP      $5395               ; {}
4CEF: CD 6D 7A        CALL    $7A6D               ; {}
4CF2: C0              RET     NZ                  
4CF3: 3E 08           LD      A,$08               
4CF5: 12              LD      (DE),A              
4CF6: CD 71 7A        CALL    $7A71               ; {}
4CF9: FE 05           CP      $05                 
4CFB: 28 06           JR      Z,$4D03             ; {}
4CFD: 21 18 4D        LD      HL,$4D18            
4D00: C3 DD 7A        JP      $7ADD               ; {}
4D03: CD 96 7A        CALL    $7A96               ; {}
4D06: CA BB 53        JP      Z,$53BB             ; {}
4D09: FE 01           CP      $01                 
4D0B: 28 05           JR      Z,$4D12             ; {}
4D0D: 3E 01           LD      A,$01               
4D0F: 02              LD      (BC),A              
4D10: 18 EB           JR      $4CFD               ; {}
4D12: 3E 65           LD      A,$65               
4D14: E0 12           LDFF00  ($12),A             
4D16: 18 F5           JR      $4D0D               ; {}
4D18: 00              NOP                         
4D19: 04              INC     B                   
4D1A: FF              RST     0X38                
4D1B: DD                              
4D1C: 00              NOP                         
4D1D: 06 00           LD      B,$00               
4D1F: 19              ADD     HL,DE               
4D20: 00              NOP                         
4D21: 80              ADD     A,B                 
4D22: 1F              RRA                         
4D23: B6              OR      (HL)                
4D24: 87              ADD     A,A                 
4D25: 08 3E 09        LD      ($093E),SP          
4D28: EA BC D3        LD      ($D3BC),A           
4D2B: 21 AB 4D        LD      HL,$4DAB            
4D2E: CD B3 7A        CALL    $7AB3               ; {}
4D31: C3 9A 53        JP      $539A               ; {}
4D34: CD 71 7A        CALL    $7A71               ; {}
4D37: FE 29           CP      $29                 
4D39: 28 06           JR      Z,$4D41             ; {}
4D3B: 21 5B 4D        LD      HL,$4D5B            
4D3E: C3 DD 7A        JP      $7ADD               ; {}
4D41: CD 96 7A        CALL    $7A96               ; {}
4D44: CA BB 53        JP      Z,$53BB             ; {}
4D47: FE 03           CP      $03                 
4D49: 28 05           JR      Z,$4D50             ; {}
4D4B: 3E 01           LD      A,$01               
4D4D: 02              LD      (BC),A              
4D4E: 18 EB           JR      $4D3B               ; {}
4D50: AF              XOR     A                   
4D51: 02              LD      (BC),A              
4D52: 21 B1 4D        LD      HL,$4DB1            
4D55: CD B3 7A        CALL    $7AB3               ; {}
4D58: C3 75 7A        JP      $7A75               ; {}
4D5B: 00              NOP                         
4D5C: 30 00           JR      NC,$4D5E            ; {}
4D5E: 30 00           JR      NC,$4D60            ; {}
4D60: 30 00           JR      NC,$4D62            ; {}
4D62: 30 00           JR      NC,$4D64            ; {}
4D64: 28 00           JR      Z,$4D66             ; {}
4D66: 28 00           JR      Z,$4D68             ; {}
4D68: 28 00           JR      Z,$4D6A             ; {}
4D6A: 28 00           JR      Z,$4D6C             ; {}
4D6C: 20 00           JR      NZ,$4D6E            ; {}
4D6E: 20 00           JR      NZ,$4D70            ; {}
4D70: 20 00           JR      NZ,$4D72            ; {}
4D72: 20 00           JR      NZ,$4D74            ; {}
4D74: 18 00           JR      $4D76               ; {}
4D76: 18 00           JR      $4D78               ; {}
4D78: 18 00           JR      $4D7A               ; {}
4D7A: 18 00           JR      $4D7C               ; {}
4D7C: 10 00           STOP    $00                 
4D7E: 10 00           STOP    $00                 
4D80: 10 00           STOP    $00                 
4D82: 10 FF           STOP    $FF                 
4D84: F0 FF           LD      A,($FF)             
4D86: F0 FF           LD      A,($FF)             
4D88: F0 FF           LD      A,($FF)             
4D8A: F0 FF           LD      A,($FF)             
4D8C: E8 FF           ADD     SP,$FF              
4D8E: E8 FF           ADD     SP,$FF              
4D90: E8 FF           ADD     SP,$FF              
4D92: E8 FF           ADD     SP,$FF              
4D94: E0 FF           LDFF00  ($FF),A             
4D96: E0 FF           LDFF00  ($FF),A             
4D98: E0 FF           LDFF00  ($FF),A             
4D9A: E0 FF           LDFF00  ($FF),A             
4D9C: D8              RET     C                   
4D9D: FF              RST     0X38                
4D9E: D8              RET     C                   
4D9F: FF              RST     0X38                
4DA0: D8              RET     C                   
4DA1: FF              RST     0X38                
4DA2: D8              RET     C                   
4DA3: FF              RST     0X38                
4DA4: D0              RET     NC                  
4DA5: FF              RST     0X38                
4DA6: D0              RET     NC                  
4DA7: FF              RST     0X38                
4DA8: D0              RET     NC                  
4DA9: FF              RST     0X38                
4DAA: D0              RET     NC                  
4DAB: 00              NOP                         
4DAC: 80              ADD     A,B                 
4DAD: 1D              DEC     E                   
4DAE: 00              NOP                         
4DAF: 81              ADD     A,C                 
4DB0: 10 00           STOP    $00                 
4DB2: 80              ADD     A,B                 
4DB3: F7              RST     0X30                
4DB4: 00              NOP                         
4DB5: 81              ADD     A,C                 
4DB6: 10 3E           STOP    $3E                 
4DB8: 07              RLCA                        
4DB9: EA BC D3        LD      ($D3BC),A           
4DBC: 21 E9 4D        LD      HL,$4DE9            
4DBF: CD B3 7A        CALL    $7AB3               ; {}
4DC2: C3 9A 53        JP      $539A               ; {}
4DC5: CD 71 7A        CALL    $7A71               ; {}
4DC8: FE 07           CP      $07                 
4DCA: 28 06           JR      Z,$4DD2             ; {}
4DCC: 21 DD 4D        LD      HL,$4DDD            
4DCF: C3 DD 7A        JP      $7ADD               ; {}
4DD2: CD 96 7A        CALL    $7A96               ; {}
4DD5: CA B5 53        JP      Z,$53B5             ; {}
4DD8: 3E 01           LD      A,$01               
4DDA: 02              LD      (BC),A              
4DDB: 18 EF           JR      $4DCC               ; {}
4DDD: 00              NOP                         
4DDE: 80              ADD     A,B                 
4DDF: 00              NOP                         
4DE0: 60              LD      H,B                 
4DE1: 00              NOP                         
4DE2: 40              LD      B,B                 
4DE3: FF              RST     0X38                
4DE4: C0              RET     NZ                  
4DE5: FF              RST     0X38                
4DE6: A0              AND     B                   
4DE7: FF              RST     0X38                
4DE8: 88              ADC     A,B                 
4DE9: 00              NOP                         
4DEA: 80              ADD     A,B                 
4DEB: F2                              
4DEC: 00              NOP                         
4DED: 85              ADD     A,L                 
4DEE: 01 3E 0A        LD      BC,$0A3E            
4DF1: EA BC D3        LD      ($D3BC),A           
4DF4: 21 0A 4E        LD      HL,$4E0A            
4DF7: C3 9A 53        JP      $539A               ; {}
4DFA: CD 6D 7A        CALL    $7A6D               ; {}
4DFD: C0              RET     NZ                  
4DFE: CD 96 7A        CALL    $7A96               ; {}
4E01: CA BB 53        JP      Z,$53BB             ; {}
4E04: 21 0A 4E        LD      HL,$4E0A            
4E07: C3 75 7A        JP      $7A75               ; {}
4E0A: 17              RLA                         
4E0B: BC              CP      H                   
4E0C: 64              LD      H,H                 
4E0D: 44              LD      B,H                 
4E0E: C7              RST     0X00                
4E0F: 02              LD      (BC),A              
4E10: 3E 14           LD      A,$14               
4E12: EA BC D3        LD      ($D3BC),A           
4E15: 21 4A 4E        LD      HL,$4E4A            
4E18: CD B3 7A        CALL    $7AB3               ; {}
4E1B: C3 9A 53        JP      $539A               ; {}
4E1E: CD 71 7A        CALL    $7A71               ; {}
4E21: FE 03           CP      $03                 
4E23: 28 06           JR      Z,$4E2B             ; {}
4E25: 21 46 4E        LD      HL,$4E46            
4E28: C3 DD 7A        JP      $7ADD               ; {}
4E2B: CD 96 7A        CALL    $7A96               ; {}
4E2E: CA BB 53        JP      Z,$53BB             ; {}
4E31: FE 10           CP      $10                 
4E33: 28 05           JR      Z,$4E3A             ; {}
4E35: 3E 01           LD      A,$01               
4E37: 02              LD      (BC),A              
4E38: 18 EB           JR      $4E25               ; {}
4E3A: 21 50 4E        LD      HL,$4E50            
4E3D: 3E 01           LD      A,$01               
4E3F: 02              LD      (BC),A              
4E40: CD B3 7A        CALL    $7AB3               ; {}
4E43: C3 75 7A        JP      $7A75               ; {}
4E46: FF              RST     0X38                
4E47: FC                              
4E48: 00              NOP                         
4E49: 02              LD      (BC),A              
4E4A: 00              NOP                         
4E4B: 00              NOP                         
4E4C: 19              ADD     HL,DE               
4E4D: EA 87 01        LD      ($0187),A           
4E50: 00              NOP                         
4E51: 00              NOP                         
4E52: 47              LD      B,A                 
4E53: E0 87           LDFF00  ($87),A             
4E55: 01 21 75        LD      BC,$7521            
4E58: 4E              LD      C,(HL)              
4E59: C3 95 53        JP      $5395               ; {}
4E5C: CD 6D 7A        CALL    $7A6D               ; {}
4E5F: C0              RET     NZ                  
4E60: CD 71 7A        CALL    $7A71               ; {}
4E63: FE 03           CP      $03                 
4E65: CA B5 53        JP      Z,$53B5             ; {}
4E68: 21 71 4E        LD      HL,$4E71            
4E6B: CD 60 7A        CALL    $7A60               ; {}
4E6E: C3 75 7A        JP      $7A75               ; {}
4E71: 7B              LD      A,E                 
4E72: 4E              LD      C,(HL)              
4E73: 81              ADD     A,C                 
4E74: 4E              LD      C,(HL)              
4E75: 1F              RRA                         
4E76: 80              ADD     A,B                 
4E77: 85              ADD     A,L                 
4E78: A0              AND     B                   
4E79: 87              ADD     A,A                 
4E7A: 0C              INC     C                   
4E7B: 1F              RRA                         
4E7C: 80              ADD     A,B                 
4E7D: 47              LD      B,A                 
4E7E: A0              AND     B                   
4E7F: 87              ADD     A,A                 
4E80: 0C              INC     C                   
4E81: 1F              RRA                         
4E82: 8D              ADC     A,L                 
4E83: 20 A0           JR      NZ,$4E25            ; {}
4E85: C7              RST     0X00                
4E86: 0C              INC     C                   
4E87: 3E 02           LD      A,$02               
4E89: EA BC D3        LD      ($D3BC),A           
4E8C: 21 C4 4E        LD      HL,$4EC4            
4E8F: CD B3 7A        CALL    $7AB3               ; {}
4E92: C3 9A 53        JP      $539A               ; {}
4E95: CD 6D 7A        CALL    $7A6D               ; {}
4E98: C0              RET     NZ                  
4E99: 3E 08           LD      A,$08               
4E9B: 12              LD      (DE),A              
4E9C: CD 71 7A        CALL    $7A71               ; {}
4E9F: FE 04           CP      $04                 
4EA1: 28 0A           JR      Z,$4EAD             ; {}
4EA3: FE 05           CP      $05                 
4EA5: 28 11           JR      Z,$4EB8             ; {}
4EA7: 21 BC 4E        LD      HL,$4EBC            
4EAA: C3 DD 7A        JP      $7ADD               ; {}
4EAD: CD 96 7A        CALL    $7A96               ; {}
4EB0: CA B5 53        JP      Z,$53B5             ; {}
4EB3: 3E 04           LD      A,$04               
4EB5: 02              LD      (BC),A              
4EB6: 18 EF           JR      $4EA7               ; {}
4EB8: 3E 01           LD      A,$01               
4EBA: 18 F9           JR      $4EB5               ; {}
4EBC: 00              NOP                         
4EBD: 08 FF FD        LD      ($FDFF),SP          
4EC0: 00              NOP                         
4EC1: 03              INC     BC                  
4EC2: FF              RST     0X38                
4EC3: F8 00           LDHL    SP,$00              
4EC5: 00              NOP                         
4EC6: 60              LD      H,B                 
4EC7: D1              POP     DE                  
4EC8: 87              ADD     A,A                 
4EC9: 08 3E 0C        LD      ($0C3E),SP          
4ECC: EA BC D3        LD      ($D3BC),A           
4ECF: 21 17 4F        LD      HL,$4F17            
4ED2: CD B3 7A        CALL    $7AB3               ; {}
4ED5: C3 9A 53        JP      $539A               ; {}
4ED8: CD 71 7A        CALL    $7A71               ; {}
4EDB: FE 09           CP      $09                 
4EDD: 28 0A           JR      Z,$4EE9             ; {}
4EDF: FE 0A           CP      $0A                 
4EE1: 28 1D           JR      Z,$4F00             ; {}
4EE3: 21 05 4F        LD      HL,$4F05            
4EE6: C3 DD 7A        JP      $7ADD               ; {}
4EE9: CD 96 7A        CALL    $7A96               ; {}
4EEC: CA B5 53        JP      Z,$53B5             ; {}
4EEF: FE 09           CP      $09                 
4EF1: 28 02           JR      Z,$4EF5             ; {}
4EF3: 18 EE           JR      $4EE3               ; {}
4EF5: AF              XOR     A                   
4EF6: 02              LD      (BC),A              
4EF7: 21 1D 4F        LD      HL,$4F1D            
4EFA: CD B3 7A        CALL    $7AB3               ; {}
4EFD: C3 75 7A        JP      $7A75               ; {}
4F00: 3E 01           LD      A,$01               
4F02: 02              LD      (BC),A              
4F03: 18 DE           JR      $4EE3               ; {}
4F05: 00              NOP                         
4F06: 01 00 01        LD      BC,$0100            
4F09: 00              NOP                         
4F0A: 01 00 01        LD      BC,$0100            
4F0D: 00              NOP                         
4F0E: 01 00 01        LD      BC,$0100            
4F11: 00              NOP                         
4F12: 01 00 01        LD      BC,$0100            
4F15: FF              RST     0X38                
4F16: FA 00 00        LD      A,($0000)           
4F19: 1F              RRA                         
4F1A: D0              RET     NC                  
4F1B: 87              ADD     A,A                 
4F1C: 01 00 00        LD      BC,$0000            
4F1F: A7              AND     A                   
4F20: D8              RET     C                   
4F21: 87              ADD     A,A                 
4F22: 01 3E 05        LD      BC,$053E            
4F25: EA BC D3        LD      ($D3BC),A           
4F28: 21 78 4F        LD      HL,$4F78            
4F2B: CD B3 7A        CALL    $7AB3               ; {}
4F2E: C3 9A 53        JP      $539A               ; {}
4F31: CD 6D 7A        CALL    $7A6D               ; {}
4F34: C0              RET     NZ                  
4F35: 3E 02           LD      A,$02               
4F37: 12              LD      (DE),A              
4F38: CD 71 7A        CALL    $7A71               ; {}
4F3B: FE 09           CP      $09                 
4F3D: 28 0A           JR      Z,$4F49             ; {}
4F3F: FE 0A           CP      $0A                 
4F41: 28 13           JR      Z,$4F56             ; {}
4F43: 21 66 4F        LD      HL,$4F66            
4F46: C3 DD 7A        JP      $7ADD               ; {}
4F49: CD 96 7A        CALL    $7A96               ; {}
4F4C: CA B5 53        JP      Z,$53B5             ; {}
4F4F: FE 03           CP      $03                 
4F51: 28 08           JR      Z,$4F5B             ; {}
4F53: 0A              LD      A,(BC)              
4F54: 18 ED           JR      $4F43               ; {}
4F56: 3E 01           LD      A,$01               
4F58: 02              LD      (BC),A              
4F59: 18 E8           JR      $4F43               ; {}
4F5B: AF              XOR     A                   
4F5C: 02              LD      (BC),A              
4F5D: 21 7E 4F        LD      HL,$4F7E            
4F60: CD B3 7A        CALL    $7AB3               ; {}
4F63: C3 75 7A        JP      $7A75               ; {}
4F66: 00              NOP                         
4F67: 10 00           STOP    $00                 
4F69: 10 00           STOP    $00                 
4F6B: 10 00           STOP    $00                 
4F6D: 10 00           STOP    $00                 
4F6F: 0C              INC     C                   
4F70: 00              NOP                         
4F71: 08 00 04        LD      ($0400),SP          
4F74: 00              NOP                         
4F75: 02              LD      (BC),A              
4F76: FF              RST     0X38                
4F77: A2              AND     D                   
4F78: 00              NOP                         
4F79: 80              ADD     A,B                 
4F7A: 1F              RRA                         
4F7B: A0              AND     B                   
4F7C: 86              ADD     A,(HL)              
4F7D: 02              LD      (BC),A              
4F7E: 00              NOP                         
4F7F: 80              ADD     A,B                 
4F80: 87              ADD     A,A                 
4F81: A0              AND     B                   
4F82: 86              ADD     A,(HL)              
4F83: 02              LD      (BC),A              
4F84: 3E 0B           LD      A,$0B               
4F86: EA BC D3        LD      ($D3BC),A           
4F89: 21 EF 4F        LD      HL,$4FEF            
4F8C: CD B3 7A        CALL    $7AB3               ; {}
4F8F: C3 9A 53        JP      $539A               ; {}
4F92: CD 96 7A        CALL    $7A96               ; {}
4F95: 28 24           JR      Z,$4FBB             ; {}
4F97: FA E2 D3        LD      A,($D3E2)           
4F9A: FE 0D           CP      $0D                 
4F9C: 30 11           JR      NC,$4FAF            ; {}
4F9E: E6 01           AND     $01                 
4FA0: 20 09           JR      NZ,$4FAB            ; {}
4FA2: 3E 01           LD      A,$01               
4FA4: 02              LD      (BC),A              
4FA5: 21 E7 4F        LD      HL,$4FE7            
4FA8: C3 DD 7A        JP      $7ADD               ; {}
4FAB: 3E 02           LD      A,$02               
4FAD: 18 F5           JR      $4FA4               ; {}
4FAF: E6 01           AND     $01                 
4FB1: 20 04           JR      NZ,$4FB7            ; {}
4FB3: 3E 03           LD      A,$03               
4FB5: 18 ED           JR      $4FA4               ; {}
4FB7: 3E 04           LD      A,$04               
4FB9: 18 E9           JR      $4FA4               ; {}
4FBB: C5              PUSH    BC                  
4FBC: 01 E2 D3        LD      BC,$D3E2            
4FBF: CD 71 7A        CALL    $7A71               ; {}
4FC2: C1              POP     BC                  
4FC3: FE 05           CP      $05                 
4FC5: 28 14           JR      Z,$4FDB             ; {}
4FC7: FE 22           CP      $22                 
4FC9: CA B5 53        JP      Z,$53B5             ; {}
4FCC: FE 11           CP      $11                 
4FCE: 30 13           JR      NC,$4FE3            ; {}
4FD0: CB 2F           SRA     1,E                 
4FD2: 5F              LD      E,A                 
4FD3: 3E 0B           LD      A,$0B               
4FD5: 93              SUB     E                   
4FD6: EA BC D3        LD      ($D3BC),A           
4FD9: 18 BC           JR      $4F97               ; {}
4FDB: 3E A0           LD      A,$A0               
4FDD: E0 12           LDFF00  ($12),A             
4FDF: 3E 05           LD      A,$05               
4FE1: 18 ED           JR      $4FD0               ; {}
4FE3: 3E 11           LD      A,$11               
4FE5: 18 E9           JR      $4FD0               ; {}
4FE7: 00              NOP                         
4FE8: 20 FF           JR      NZ,$4FE9            ; {}
4FEA: E8 00           ADD     SP,$00              
4FEC: 1C              INC     E                   
4FED: FF              RST     0X38                
4FEE: F0 00           LD      A,($00)             
4FF0: 40              LD      B,B                 
4FF1: 1F              RRA                         
4FF2: 80              ADD     A,B                 
4FF3: 83              ADD     A,E                 
4FF4: 01 3E 10        LD      BC,$103E            
4FF7: EA BC D3        LD      ($D3BC),A           
4FFA: 21 36 50        LD      HL,$5036            
4FFD: CD B3 7A        CALL    $7AB3               ; {}
5000: C3 95 53        JP      $5395               ; {}
5003: CD 71 7A        CALL    $7A71               ; {}
5006: FE 09           CP      $09                 
5008: 28 0A           JR      Z,$5014             ; {}
500A: FE 0A           CP      $0A                 
500C: 28 11           JR      Z,$501F             ; {}
500E: 21 24 50        LD      HL,$5024            
5011: C3 DD 7A        JP      $7ADD               ; {}
5014: CD 96 7A        CALL    $7A96               ; {}
5017: CA B5 53        JP      Z,$53B5             ; {}
501A: 3E 09           LD      A,$09               
501C: 02              LD      (BC),A              
501D: 18 EF           JR      $500E               ; {}
501F: 3E 01           LD      A,$01               
5021: 02              LD      (BC),A              
5022: 18 EA           JR      $500E               ; {}
5024: 00              NOP                         
5025: 40              LD      B,B                 
5026: 00              NOP                         
5027: 30 00           JR      NC,$5029            ; {}
5029: 20 FF           JR      NZ,$502A            ; {}
502B: E0 FF           LDFF00  ($FF),A             
502D: D0              RET     NC                  
502E: FF              RST     0X38                
502F: C0              RET     NZ                  
5030: FF              RST     0X38                
5031: A0              AND     B                   
5032: FF              RST     0X38                
5033: 80              ADD     A,B                 
5034: 00              NOP                         
5035: D0              RET     NC                  
5036: 00              NOP                         
5037: 80              ADD     A,B                 
5038: 80              ADD     A,B                 
5039: 00              NOP                         
503A: 86              ADD     A,(HL)              
503B: 01 FA 61        LD      BC,$61FA            
503E: D3                              
503F: A7              AND     A                   
5040: C2 E6 53        JP      NZ,$53E6            ; {}
5043: FA D6 D3        LD      A,($D3D6)           
5046: A7              AND     A                   
5047: 20 09           JR      NZ,$5052            ; {}
5049: 21 82 50        LD      HL,$5082            
504C: CD B3 7A        CALL    $7AB3               ; {}
504F: C3 9A 53        JP      $539A               ; {}
5052: 21 88 50        LD      HL,$5088            
5055: 18 F5           JR      $504C               ; {}
5057: CD 71 7A        CALL    $7A71               ; {}
505A: FE 0B           CP      $0B                 
505C: 28 06           JR      Z,$5064             ; {}
505E: 21 6E 50        LD      HL,$506E            
5061: C3 DD 7A        JP      $7ADD               ; {}
5064: 21 60 D3        LD      HL,$D360            
5067: 3E 38           LD      A,$38               
5069: 22              LD      (HLI),A             
506A: AF              XOR     A                   
506B: 77              LD      (HL),A              
506C: 18 CE           JR      $503C               ; {}
506E: 00              NOP                         
506F: C0              RET     NZ                  
5070: 00              NOP                         
5071: 90              SUB     B                   
5072: 00              NOP                         
5073: 60              LD      H,B                 
5074: 00              NOP                         
5075: 30 00           JR      NC,$5077            ; {}
5077: 18 FF           JR      $5078               ; {}
5079: E8 FF           ADD     SP,$FF              
507B: D0              RET     NC                  
507C: FF              RST     0X38                
507D: A0              AND     B                   
507E: FF              RST     0X38                
507F: 70              LD      (HL),B              
5080: FF              RST     0X38                
5081: 40              LD      B,B                 
5082: 00              NOP                         
5083: 80              ADD     A,B                 
5084: A0              AND     B                   
5085: 00              NOP                         
5086: 82              ADD     A,D                 
5087: 01 00 80        LD      BC,$8000            
508A: C0              RET     NZ                  
508B: 00              NOP                         
508C: 83              ADD     A,E                 
508D: 01 3E 04        LD      BC,$043E            
5090: EA BC D3        LD      ($D3BC),A           
5093: 21 14 51        LD      HL,$5114            
5096: CD B3 7A        CALL    $7AB3               ; {}
5099: C3 95 53        JP      $5395               ; {}
509C: CD 71 7A        CALL    $7A71               ; {}
509F: FE 0E           CP      $0E                 
50A1: 28 17           JR      Z,$50BA             ; {}
50A3: FE 0F           CP      $0F                 
50A5: 28 1E           JR      Z,$50C5             ; {}
50A7: FA BC D3        LD      A,($D3BC)           
50AA: FE 03           CP      $03                 
50AC: 38 06           JR      C,$50B4             ; {}
50AE: 21 DC 50        LD      HL,$50DC            
50B1: C3 DD 7A        JP      $7ADD               ; {}
50B4: 21 F8 50        LD      HL,$50F8            
50B7: C3 DD 7A        JP      $7ADD               ; {}
50BA: CD 96 7A        CALL    $7A96               ; {}
50BD: CA B5 53        JP      Z,$53B5             ; {}
50C0: 3E 0E           LD      A,$0E               
50C2: 02              LD      (BC),A              
50C3: 18 E2           JR      $50A7               ; {}
50C5: FA BC D3        LD      A,($D3BC)           
50C8: FE 01           CP      $01                 
50CA: 28 05           JR      Z,$50D1             ; {}
50CC: 3E 01           LD      A,$01               
50CE: 02              LD      (BC),A              
50CF: 18 D6           JR      $50A7               ; {}
50D1: AF              XOR     A                   
50D2: 02              LD      (BC),A              
50D3: 21 1A 51        LD      HL,$511A            
50D6: CD B3 7A        CALL    $7AB3               ; {}
50D9: C3 75 7A        JP      $7A75               ; {}
50DC: 00              NOP                         
50DD: C0              RET     NZ                  
50DE: 00              NOP                         
50DF: A0              AND     B                   
50E0: 00              NOP                         
50E1: 80              ADD     A,B                 
50E2: 00              NOP                         
50E3: 60              LD      H,B                 
50E4: 00              NOP                         
50E5: 40              LD      B,B                 
50E6: 00              NOP                         
50E7: 20 FF           JR      NZ,$50E8            ; {}
50E9: E0 FF           LDFF00  ($FF),A             
50EB: E0 FF           LDFF00  ($FF),A             
50ED: D0              RET     NC                  
50EE: FF              RST     0X38                
50EF: D0              RET     NC                  
50F0: FF              RST     0X38                
50F1: C0              RET     NZ                  
50F2: FF              RST     0X38                
50F3: C0              RET     NZ                  
50F4: FF              RST     0X38                
50F5: B0              OR      B                   
50F6: FF              RST     0X38                
50F7: B0              OR      B                   
50F8: 00              NOP                         
50F9: 60              LD      H,B                 
50FA: 00              NOP                         
50FB: 50              LD      D,B                 
50FC: 00              NOP                         
50FD: 40              LD      B,B                 
50FE: 00              NOP                         
50FF: 30 00           JR      NC,$5101            ; {}
5101: 20 00           JR      NZ,$5103            ; {}
5103: 10 FF           STOP    $FF                 
5105: F0 FF           LD      A,($FF)             
5107: F0 FF           LD      A,($FF)             
5109: F0 FF           LD      A,($FF)             
510B: F0 FF           LD      A,($FF)             
510D: E0 FF           LDFF00  ($FF),A             
510F: E0 FF           LDFF00  ($FF),A             
5111: D0              RET     NC                  
5112: FF              RST     0X38                
5113: D0              RET     NC                  
5114: 00              NOP                         
5115: 40              LD      B,B                 
5116: 4D              LD      C,L                 
5117: 80              ADD     A,B                 
5118: 83              ADD     A,E                 
5119: 01 00 80        LD      BC,$8000            
511C: 20 C0           JR      NZ,$50DE            ; {}
511E: 84              ADD     A,H                 
511F: 01 3E 04        LD      BC,$043E            
5122: EA BC D3        LD      ($D3BC),A           
5125: 21 61 51        LD      HL,$5161            
5128: CD B3 7A        CALL    $7AB3               ; {}
512B: C3 9A 53        JP      $539A               ; {}
512E: CD 71 7A        CALL    $7A71               ; {}
5131: FE 09           CP      $09                 
5133: 28 0A           JR      Z,$513F             ; {}
5135: FE 0A           CP      $0A                 
5137: 28 11           JR      Z,$514A             ; {}
5139: 21 4F 51        LD      HL,$514F            
513C: C3 DD 7A        JP      $7ADD               ; {}
513F: CD 96 7A        CALL    $7A96               ; {}
5142: CA BB 53        JP      Z,$53BB             ; {}
5145: 3E 09           LD      A,$09               
5147: 02              LD      (BC),A              
5148: 18 EF           JR      $5139               ; {}
514A: 3E 01           LD      A,$01               
514C: 02              LD      (BC),A              
514D: 18 EA           JR      $5139               ; {}
514F: 00              NOP                         
5150: 12              LD      (DE),A              
5151: 00              NOP                         
5152: 0E 00           LD      C,$00               
5154: 0A              LD      A,(BC)              
5155: 00              NOP                         
5156: 08 00 06        LD      ($0600),SP          
5159: 00              NOP                         
515A: 04              INC     B                   
515B: 00              NOP                         
515C: 02              LD      (BC),A              
515D: 00              NOP                         
515E: 01 FF C1        LD      BC,$C1FF            
5161: 00              NOP                         
5162: 00              NOP                         
5163: A4              AND     H                   
5164: 00              NOP                         
5165: 87              ADD     A,A                 
5166: 01 3E 05        LD      BC,$053E            
5169: EA BC D3        LD      ($D3BC),A           
516C: 21 AE 51        LD      HL,$51AE            
516F: CD B3 7A        CALL    $7AB3               ; {}
5172: C3 9A 53        JP      $539A               ; {}
5175: CD 71 7A        CALL    $7A71               ; {}
5178: FE 0C           CP      $0C                 
517A: 28 0F           JR      Z,$518B             ; {}
517C: FE 0D           CP      $0D                 
517E: 28 06           JR      Z,$5186             ; {}
5180: 21 96 51        LD      HL,$5196            
5183: C3 DD 7A        JP      $7ADD               ; {}
5186: 3E 01           LD      A,$01               
5188: 02              LD      (BC),A              
5189: 18 F5           JR      $5180               ; {}
518B: CD 96 7A        CALL    $7A96               ; {}
518E: CA B5 53        JP      Z,$53B5             ; {}
5191: 3E 0C           LD      A,$0C               
5193: 02              LD      (BC),A              
5194: 18 EA           JR      $5180               ; {}
5196: FF              RST     0X38                
5197: C0              RET     NZ                  
5198: FF              RST     0X38                
5199: A0              AND     B                   
519A: 00              NOP                         
519B: 80              ADD     A,B                 
519C: FF              RST     0X38                
519D: C0              RET     NZ                  
519E: FF              RST     0X38                
519F: A0              AND     B                   
51A0: 00              NOP                         
51A1: 80              ADD     A,B                 
51A2: FF              RST     0X38                
51A3: C0              RET     NZ                  
51A4: FF              RST     0X38                
51A5: A0              AND     B                   
51A6: 00              NOP                         
51A7: 80              ADD     A,B                 
51A8: FF              RST     0X38                
51A9: C0              RET     NZ                  
51AA: FF              RST     0X38                
51AB: A0              AND     B                   
51AC: 01 00 00        LD      BC,$0000            
51AF: 00              NOP                         
51B0: 87              ADD     A,A                 
51B1: 80              ADD     A,B                 
51B2: 87              ADD     A,A                 
51B3: 01 3E 02        LD      BC,$023E            
51B6: EA BC D3        LD      ($D3BC),A           
51B9: 21 F0 51        LD      HL,$51F0            
51BC: CD B3 7A        CALL    $7AB3               ; {}
51BF: C3 9A 53        JP      $539A               ; {}
51C2: CD 71 7A        CALL    $7A71               ; {}
51C5: FE 09           CP      $09                 
51C7: 28 06           JR      Z,$51CF             ; {}
51C9: 21 E0 51        LD      HL,$51E0            
51CC: C3 DD 7A        JP      $7ADD               ; {}
51CF: CD 96 7A        CALL    $7A96               ; {}
51D2: CA B5 53        JP      Z,$53B5             ; {}
51D5: AF              XOR     A                   
51D6: 02              LD      (BC),A              
51D7: 21 F6 51        LD      HL,$51F6            
51DA: CD B3 7A        CALL    $7AB3               ; {}
51DD: C3 75 7A        JP      $7A75               ; {}
51E0: 00              NOP                         
51E1: 02              LD      (BC),A              
51E2: 00              NOP                         
51E3: 02              LD      (BC),A              
51E4: 00              NOP                         
51E5: 02              LD      (BC),A              
51E6: 00              NOP                         
51E7: 02              LD      (BC),A              
51E8: 00              NOP                         
51E9: 01 00 01        LD      BC,$0100            
51EC: 00              NOP                         
51ED: 01 00 01        LD      BC,$0100            
51F0: 00              NOP                         
51F1: 00              NOP                         
51F2: 60              LD      H,B                 
51F3: D0              RET     NC                  
51F4: 87              ADD     A,A                 
51F5: 02              LD      (BC),A              
51F6: 00              NOP                         
51F7: 40              LD      B,B                 
51F8: 10 D0           STOP    $D0                 
51FA: 87              ADD     A,A                 
51FB: 01 FA 61        LD      BC,$61FA            
51FE: D3                              
51FF: FE 04           CP      $04                 
5201: CA E6 53        JP      Z,$53E6             ; {}
5204: FE 05           CP      $05                 
5206: CA E6 53        JP      Z,$53E6             ; {}
5209: FE 07           CP      $07                 
520B: CA E6 53        JP      Z,$53E6             ; {}
520E: FE 03           CP      $03                 
5210: CA E6 53        JP      Z,$53E6             ; {}
5213: FE 0D           CP      $0D                 
5215: CA E6 53        JP      Z,$53E6             ; {}
5218: 3E 0A           LD      A,$0A               
521A: EA BC D3        LD      ($D3BC),A           
521D: 21 62 52        LD      HL,$5262            
5220: CD B3 7A        CALL    $7AB3               ; {}
5223: C3 9A 53        JP      $539A               ; {}
5226: CD 71 7A        CALL    $7A71               ; {}
5229: FE 04           CP      $04                 
522B: 28 0F           JR      Z,$523C             ; {}
522D: FE 05           CP      $05                 
522F: 28 06           JR      Z,$5237             ; {}
5231: 21 5A 52        LD      HL,$525A            
5234: C3 DD 7A        JP      $7ADD               ; {}
5237: 3E 01           LD      A,$01               
5239: 02              LD      (BC),A              
523A: 18 F5           JR      $5231               ; {}
523C: CD 96 7A        CALL    $7A96               ; {}
523F: CA 53 52        JP      Z,$5253             ; {}
5242: FE 07           CP      $07                 
5244: 28 02           JR      Z,$5248             ; {}
5246: 18 E9           JR      $5231               ; {}
5248: AF              XOR     A                   
5249: 02              LD      (BC),A              
524A: 21 68 52        LD      HL,$5268            
524D: CD B3 7A        CALL    $7AB3               ; {}
5250: C3 75 7A        JP      $7A75               ; {}
5253: 3E 3D           LD      A,$3D               
5255: EA 60 D3        LD      ($D360),A           
5258: 18 A2           JR      $51FC               ; {}
525A: 00              NOP                         
525B: C0              RET     NZ                  
525C: 00              NOP                         
525D: 80              ADD     A,B                 
525E: 00              NOP                         
525F: 40              LD      B,B                 
5260: FE 80           CP      $80                 
5262: 00              NOP                         
5263: 40              LD      B,B                 
5264: 19              ADD     HL,DE               
5265: 80              ADD     A,B                 
5266: 83              ADD     A,E                 
5267: 01 00 40        LD      BC,$4000            
526A: 86              ADD     A,(HL)              
526B: 80              ADD     A,B                 
526C: 83              ADD     A,E                 
526D: 01 FA 61        LD      BC,$61FA            
5270: D3                              
5271: FE 3E           CP      $3E                 
5273: CA E6 53        JP      Z,$53E6             ; {}
5276: 21 83 52        LD      HL,$5283            
5279: C3 9A 53        JP      $539A               ; {}
527C: CD 6D 7A        CALL    $7A6D               ; {}
527F: C0              RET     NZ                  
5280: C3 BB 53        JP      $53BB               ; {}
5283: 27              DAA                         
5284: BE              CP      (HL)                
5285: 60              LD      H,B                 
5286: C0              RET     NZ                  
5287: C7              RST     0X00                
5288: 03              INC     BC                  
5289: 3E 09           LD      A,$09               
528B: EA BC D3        LD      ($D3BC),A           
528E: 21 CD 52        LD      HL,$52CD            
5291: CD B3 7A        CALL    $7AB3               ; {}
5294: C3 9A 53        JP      $539A               ; {}
5297: CD 71 7A        CALL    $7A71               ; {}
529A: FE 03           CP      $03                 
529C: 28 0A           JR      Z,$52A8             ; {}
529E: FE 04           CP      $04                 
52A0: 28 15           JR      Z,$52B7             ; {}
52A2: 21 C7 52        LD      HL,$52C7            
52A5: C3 DD 7A        JP      $7ADD               ; {}
52A8: CD 96 7A        CALL    $7A96               ; {}
52AB: CA B5 53        JP      Z,$53B5             ; {}
52AE: FE 06           CP      $06                 
52B0: 28 0A           JR      Z,$52BC             ; {}
52B2: 3E 03           LD      A,$03               
52B4: 02              LD      (BC),A              
52B5: 18 EB           JR      $52A2               ; {}
52B7: 3E 01           LD      A,$01               
52B9: 02              LD      (BC),A              
52BA: 18 E6           JR      $52A2               ; {}
52BC: AF              XOR     A                   
52BD: 02              LD      (BC),A              
52BE: 21 D3 52        LD      HL,$52D3            
52C1: CD B3 7A        CALL    $7AB3               ; {}
52C4: C3 75 7A        JP      $7A75               ; {}
52C7: 00              NOP                         
52C8: 60              LD      H,B                 
52C9: 00              NOP                         
52CA: 40              LD      B,B                 
52CB: FF              RST     0X38                
52CC: 70              LD      (HL),B              
52CD: 00              NOP                         
52CE: 80              ADD     A,B                 
52CF: 19              ADD     HL,DE               
52D0: 00              NOP                         
52D1: 86              ADD     A,(HL)              
52D2: 01 00 80        LD      BC,$8000            
52D5: D1              POP     DE                  
52D6: 10 86           STOP    $86                 
52D8: 01 3E 04        LD      BC,$043E            
52DB: EA BC D3        LD      ($D3BC),A           
52DE: 21 2B 53        LD      HL,$532B            
52E1: CD B3 7A        CALL    $7AB3               ; {}
52E4: C3 9A 53        JP      $539A               ; {}
52E7: CD 96 7A        CALL    $7A96               ; {}
52EA: 28 14           JR      Z,$5300             ; {}
52EC: FA E2 D3        LD      A,($D3E2)           
52EF: FE 06           CP      $06                 
52F1: 30 09           JR      NC,$52FC            ; {}
52F3: 3E 01           LD      A,$01               
52F5: 02              LD      (BC),A              
52F6: 21 27 53        LD      HL,$5327            
52F9: C3 DD 7A        JP      $7ADD               ; {}
52FC: 3E 02           LD      A,$02               
52FE: 18 F5           JR      $52F5               ; {}
5300: C5              PUSH    BC                  
5301: 01 E2 D3        LD      BC,$D3E2            
5304: CD 71 7A        CALL    $7A71               ; {}
5307: C1              POP     BC                  
5308: FE 14           CP      $14                 
530A: CA BB 53        JP      Z,$53BB             ; {}
530D: FE 06           CP      $06                 
530F: CA 19 53        JP      Z,$5319             ; {}
5312: 3E 04           LD      A,$04               
5314: EA BC D3        LD      ($D3BC),A           
5317: 18 D3           JR      $52EC               ; {}
5319: 3E 04           LD      A,$04               
531B: EA BC D3        LD      ($D3BC),A           
531E: 21 31 53        LD      HL,$5331            
5321: CD B3 7A        CALL    $7AB3               ; {}
5324: C3 75 7A        JP      $7A75               ; {}
5327: 00              NOP                         
5328: 10 FF           STOP    $FF                 
532A: F8 00           LDHL    SP,$00              
532C: 80              ADD     A,B                 
532D: 1A              LD      A,(DE)              
532E: 80              ADD     A,B                 
532F: 82              ADD     A,D                 
5330: 01 00 80        LD      BC,$8000            
5333: E5              PUSH    HL                  
5334: 10 84           STOP    $84                 
5336: 01 21 60        LD      BC,$6021            
5339: 53              LD      D,E                 
533A: C3 95 53        JP      $5395               ; {}
533D: CD 6D 7A        CALL    $7A6D               ; {}
5340: C0              RET     NZ                  
5341: CD 71 7A        CALL    $7A71               ; {}
5344: FE 08           CP      $08                 
5346: CA BB 53        JP      Z,$53BB             ; {}
5349: 21 52 53        LD      HL,$5352            
534C: CD 60 7A        CALL    $7A60               ; {}
534F: C3 75 7A        JP      $7A75               ; {}
5352: 78              LD      A,B                 
5353: 53              LD      D,E                 
5354: 66              LD      H,(HL)              
5355: 53              LD      D,E                 
5356: 7E              LD      A,(HL)              
5357: 53              LD      D,E                 
5358: 6C              LD      L,H                 
5359: 53              LD      D,E                 
535A: 84              ADD     A,H                 
535B: 53              LD      D,E                 
535C: 72              LD      (HL),D              
535D: 53              LD      D,E                 
535E: 8A              ADC     A,D                 
535F: 53              LD      D,E                 
5360: 00              NOP                         
5361: 00              NOP                         
5362: C1              POP     BC                  
5363: 7B              LD      A,E                 
5364: 87              ADD     A,A                 
5365: 06 00           LD      B,$00               
5367: 00              NOP                         
5368: C1              POP     BC                  
5369: 8A              ADC     A,D                 
536A: 87              ADD     A,A                 
536B: 06 00           LD      B,$00               
536D: 00              NOP                         
536E: C1              POP     BC                  
536F: 90              SUB     B                   
5370: 87              ADD     A,A                 
5371: 07              RLCA                        
5372: 00              NOP                         
5373: 00              NOP                         
5374: C1              POP     BC                  
5375: B6              OR      (HL)                
5376: 87              ADD     A,A                 
5377: 07              RLCA                        
5378: 00              NOP                         
5379: 00              NOP                         
537A: 62              LD      H,D                 
537B: 7B              LD      A,E                 
537C: 87              ADD     A,A                 
537D: 04              INC     B                   
537E: 00              NOP                         
537F: 00              NOP                         
5380: 62              LD      H,D                 
5381: 8A              ADC     A,D                 
5382: 87              ADD     A,A                 
5383: 04              INC     B                   
5384: 00              NOP                         
5385: 00              NOP                         
5386: 62              LD      H,D                 
5387: 90              SUB     B                   
5388: 87              ADD     A,A                 
5389: 04              INC     B                   
538A: 00              NOP                         
538B: 00              NOP                         
538C: 62              LD      H,D                 
538D: B6              OR      (HL)                
538E: 87              ADD     A,A                 
538F: 04              INC     B                   
5390: 3E 01           LD      A,$01               
5392: EA A0 D3        LD      ($D3A0),A           
5395: 3E 01           LD      A,$01               
5397: EA C6 D3        LD      ($D3C6),A           
539A: FA 60 D3        LD      A,($D360)           
539D: EA 61 D3        LD      ($D361),A           
53A0: AF              XOR     A                   
53A1: EA 90 D3        LD      ($D390),A           
53A4: EA 94 D3        LD      ($D394),A           
53A7: EA E2 D3        LD      ($D3E2),A           
53AA: FA 1F D3        LD      A,($D31F)           
53AD: CB FF           SET     1,E                 
53AF: EA 1F D3        LD      ($D31F),A           
53B2: C3 75 7A        JP      $7A75               ; {}
53B5: 21 D9 53        LD      HL,$53D9            
53B8: CD 75 7A        CALL    $7A75               ; {}
53BB: AF              XOR     A                   
53BC: EA 61 D3        LD      ($D361),A           
53BF: EA 90 D3        LD      ($D390),A           
53C2: E0 10           LDFF00  ($10),A             
53C4: EA 94 D3        LD      ($D394),A           
53C7: EA BC D3        LD      ($D3BC),A           
53CA: EA A0 D3        LD      ($D3A0),A           
53CD: EA C6 D3        LD      ($D3C6),A           
53D0: FA 1F D3        LD      A,($D31F)           
53D3: CB BF           RES     1,E                 
53D5: EA 1F D3        LD      ($D31F),A           
53D8: C9              RET                         
53D9: 00              NOP                         
53DA: 3F              CCF                         
53DB: 00              NOP                         
53DC: 00              NOP                         
53DD: C1              POP     BC                  
53DE: 01 06 02        LD      BC,$0206            
53E1: 0E 13           LD      C,$13               
53E3: C3 8D 7A        JP      $7A8D               ; {}
53E6: AF              XOR     A                   
53E7: EA 60 D3        LD      ($D360),A           
53EA: C3 04 42        JP      $4204               ; {}
53ED: 21 70 D3        LD      HL,$D370            
53F0: 7E              LD      A,(HL)              
53F1: A7              AND     A                   
53F2: 28 11           JR      Z,$5405             ; {}
53F4: FE 14           CP      $14                 
53F6: 28 07           JR      Z,$53FF             ; {}
53F8: FA C8 D3        LD      A,($D3C8)           
53FB: A7              AND     A                   
53FC: C2 85 63        JP      NZ,$6385            ; {}
53FF: 7E              LD      A,(HL)              
5400: 21 1B 54        LD      HL,$541B            
5403: 18 07           JR      $540C               ; {}
5405: 23              INC     HL                  
5406: 7E              LD      A,(HL)              
5407: A7              AND     A                   
5408: C8              RET     Z                   
5409: 21 61 54        LD      HL,$5461            
540C: CD 60 7A        CALL    $7A60               ; {}
540F: 11 92 D3        LD      DE,$D392            
5412: 01 96 D3        LD      BC,$D396            
5415: FA CD D3        LD      A,($D3CD)           
5418: A7              AND     A                   
5419: C0              RET     NZ                  
541A: E9              JP      (HL)                
541B: A7              AND     A                   
541C: 54              LD      D,H                 
541D: F3              DI                          
541E: 54              LD      D,H                 
541F: 38 55           JR      C,$5476             ; {}
5421: 64              LD      H,H                 
5422: 55              LD      D,L                 
5423: B3              OR      E                   
5424: 55              LD      D,L                 
5425: F9              LD      SP,HL               
5426: 55              LD      D,L                 
5427: 45              LD      B,L                 
5428: 56              LD      D,(HL)              
5429: D1              POP     DE                  
542A: 56              LD      D,(HL)              
542B: 32              LD      (HLD),A             
542C: 57              LD      D,A                 
542D: FE 57           CP      $57                 
542F: A3              AND     E                   
5430: 58              LD      E,B                 
5431: 49              LD      C,C                 
5432: 59              LD      E,C                 
5433: 99              SBC     C                   
5434: 59              LD      E,C                 
5435: E1              POP     HL                  
5436: 59              LD      E,C                 
5437: 19              ADD     HL,DE               
5438: 5A              LD      E,D                 
5439: 44              LD      B,H                 
543A: 5A              LD      E,D                 
543B: 67              LD      H,A                 
543C: 5B              LD      E,E                 
543D: C4 5B 0C        CALL    NZ,$0C5B            
5440: 5C              LD      E,H                 
5441: 80              ADD     A,B                 
5442: 5C              LD      E,H                 
5443: B0              OR      B                   
5444: 5C              LD      E,H                 
5445: FC                              
5446: 5C              LD      E,H                 
5447: 84              ADD     A,H                 
5448: 5D              LD      E,L                 
5449: D7              RST     0X10                
544A: 5E              LD      E,(HL)              
544B: 19              ADD     HL,DE               
544C: 5F              LD      E,A                 
544D: 78              LD      A,B                 
544E: 5F              LD      E,A                 
544F: C0              RET     NZ                  
5450: 5F              LD      E,A                 
5451: 1C              INC     E                   
5452: 60              LD      H,B                 
5453: 6C              LD      L,H                 
5454: 60              LD      H,B                 
5455: 6E              LD      L,(HL)              
5456: 60              LD      H,B                 
5457: D4 60 4D        CALL    NC,$4D60            ; {}
545A: 61              LD      H,C                 
545B: A2              AND     D                   
545C: 61              LD      H,C                 
545D: 1C              INC     E                   
545E: 62              LD      H,D                 
545F: 7C              LD      A,H                 
5460: 62              LD      H,D                 
5461: B0              OR      B                   
5462: 54              LD      D,H                 
5463: 04              INC     B                   
5464: 55              LD      D,L                 
5465: 4A              LD      C,D                 
5466: 55              LD      D,L                 
5467: 85              ADD     A,L                 
5468: 55              LD      D,L                 
5469: BC              CP      H                   
546A: 55              LD      D,L                 
546B: 10 56           STOP    $56                 
546D: 5E              LD      E,(HL)              
546E: 56              LD      D,(HL)              
546F: E2              LDFF00  (C),A               
5470: 56              LD      D,(HL)              
5471: 40              LD      B,B                 
5472: 57              LD      D,A                 
5473: 0C              INC     C                   
5474: 58              LD      E,B                 
5475: AF              XOR     A                   
5476: 58              LD      E,B                 
5477: 5A              LD      E,D                 
5478: 59              LD      E,C                 
5479: AA              XOR     D                   
547A: 59              LD      E,C                 
547B: EA 59 2A        LD      ($2A59),A           
547E: 5A              LD      E,D                 
547F: 55              LD      D,L                 
5480: 5A              LD      E,D                 
5481: 78              LD      A,B                 
5482: 5B              LD      E,E                 
5483: D5              PUSH    DE                  
5484: 5B              LD      E,E                 
5485: 1D              DEC     E                   
5486: 5C              LD      E,H                 
5487: 99              SBC     C                   
5488: 5C              LD      E,H                 
5489: B9              CP      C                   
548A: 5C              LD      E,H                 
548B: 1A              LD      A,(DE)              
548C: 5D              LD      E,L                 
548D: A6              AND     (HL)                
548E: 5D              LD      E,L                 
548F: E8 5E           ADD     SP,$5E              
5491: 25              DEC     H                   
5492: 5F              LD      E,A                 
5493: 93              SUB     E                   
5494: 5F              LD      E,A                 
5495: C9              RET                         
5496: 5F              LD      E,A                 
5497: 2D              DEC     L                   
5498: 60              LD      H,B                 
5499: 6D              LD      L,L                 
549A: 60              LD      H,B                 
549B: 84              ADD     A,H                 
549C: 60              LD      H,B                 
549D: EF              RST     0X28                
549E: 60              LD      H,B                 
549F: 63              LD      H,E                 
54A0: 61              LD      H,C                 
54A1: CF              RST     0X08                
54A2: 61              LD      H,C                 
54A3: 31 62 85        LD      SP,$8562            
54A6: 62              LD      H,D                 
54A7: CD 6A 63        CALL    $636A               ; {}
54AA: 21 CF 54        LD      HL,$54CF            
54AD: C3 F3 62        JP      $62F3               ; {}
54B0: CD 6D 7A        CALL    $7A6D               ; {}
54B3: C0              RET     NZ                  
54B4: CD 71 7A        CALL    $7A71               ; {}
54B7: FE 06           CP      $06                 
54B9: CA 2D 63        JP      Z,$632D             ; {}
54BC: 21 C5 54        LD      HL,$54C5            
54BF: CD 60 7A        CALL    $7A60               ; {}
54C2: C3 81 7A        JP      $7A81               ; {}
54C5: D5              PUSH    DE                  
54C6: 54              LD      D,H                 
54C7: DB                              
54C8: 54              LD      D,H                 
54C9: E1              POP     HL                  
54CA: 54              LD      D,H                 
54CB: E7              RST     0X20                
54CC: 54              LD      D,H                 
54CD: ED                              
54CE: 54              LD      D,H                 
54CF: 80              ADD     A,B                 
54D0: EE 20           XOR     $20                 
54D2: CB C7           SET     1,E                 
54D4: 05              DEC     B                   
54D5: 80              ADD     A,B                 
54D6: EE 20           XOR     $20                 
54D8: D1              POP     DE                  
54D9: C7              RST     0X00                
54DA: 05              DEC     B                   
54DB: 80              ADD     A,B                 
54DC: EE 20           XOR     $20                 
54DE: D6 C7           SUB     $C7                 
54E0: 05              DEC     B                   
54E1: 80              ADD     A,B                 
54E2: EE 20           XOR     $20                 
54E4: DD                              
54E5: C7              RST     0X00                
54E6: 07              RLCA                        
54E7: 80              ADD     A,B                 
54E8: EE 40           XOR     $40                 
54EA: DD                              
54EB: C7              RST     0X00                
54EC: 07              RLCA                        
54ED: 80              ADD     A,B                 
54EE: EE 60           XOR     $60                 
54F0: DD                              
54F1: C7              RST     0X00                
54F2: 07              RLCA                        
54F3: 3E 0C           LD      A,$0C               
54F5: EA BE D3        LD      ($D3BE),A           
54F8: CD 6F 63        CALL    $636F               ; {}
54FB: 21 32 55        LD      HL,$5532            
54FE: CD B9 7A        CALL    $7AB9               ; {}
5501: C3 F8 62        JP      $62F8               ; {}
5504: CD 71 7A        CALL    $7A71               ; {}
5507: FE 02           CP      $02                 
5509: 28 0B           JR      Z,$5516             ; {}
550B: FE 0A           CP      $0A                 
550D: CA 27 63        JP      Z,$6327             ; {}
5510: 21 20 55        LD      HL,$5520            
5513: C3 E7 7A        JP      $7AE7               ; {}
5516: CD A2 7A        CALL    $7AA2               ; {}
5519: 28 F5           JR      Z,$5510             ; {}
551B: 3E 01           LD      A,$01               
551D: 02              LD      (BC),A              
551E: 18 F0           JR      $5510               ; {}
5520: 00              NOP                         
5521: 10 00           STOP    $00                 
5523: 40              LD      B,B                 
5524: 00              NOP                         
5525: 40              LD      B,B                 
5526: 00              NOP                         
5527: 30 00           JR      NC,$5529            ; {}
5529: 30 00           JR      NC,$552B            ; {}
552B: 20 00           JR      NZ,$552D            ; {}
552D: 10 FF           STOP    $FF                 
552F: F0 FF           LD      A,($FF)             
5531: E0 80           LDFF00  ($80),A             
5533: 00              NOP                         
5534: 20 80           JR      NZ,$54B6            ; {}
5536: 85              ADD     A,L                 
5537: 02              LD      (BC),A              
5538: 21 CC 63        LD      HL,$63CC            
553B: AF              XOR     A                   
553C: E0 1A           LDFF00  ($1A),A             
553E: CD 47 63        CALL    $6347               ; {}
5541: 21 5E 55        LD      HL,$555E            
5544: CD B9 7A        CALL    $7AB9               ; {}
5547: C3 F8 62        JP      $62F8               ; {}
554A: CD 71 7A        CALL    $7A71               ; {}
554D: FE 05           CP      $05                 
554F: CA 2D 63        JP      Z,$632D             ; {}
5552: 21 58 55        LD      HL,$5558            
5555: C3 E7 7A        JP      $7AE7               ; {}
5558: 01 80 FF        LD      BC,$FF80            
555B: F0 FF           LD      A,($FF)             
555D: E0 80           LDFF00  ($80),A             
555F: EF              RST     0X28                
5560: 20 00           JR      NZ,$5562            ; {}
5562: C6 01           ADD     $01                 
5564: FA 71 D3        LD      A,($D371)           
5567: A7              AND     A                   
5568: C2 85 63        JP      NZ,$6385            ; {}
556B: FA 61 D3        LD      A,($D361)           
556E: FE 01           CP      $01                 
5570: C8              RET     Z                   
5571: FA 61 D3        LD      A,($D361)           
5574: FE 01           CP      $01                 
5576: C8              RET     Z                   
5577: 3E 02           LD      A,$02               
5579: EA BE D3        LD      ($D3BE),A           
557C: CD 6F 63        CALL    $636F               ; {}
557F: 21 A4 55        LD      HL,$55A4            
5582: C3 F8 62        JP      $62F8               ; {}
5585: CD 6D 7A        CALL    $7A6D               ; {}
5588: C0              RET     NZ                  
5589: CD 71 7A        CALL    $7A71               ; {}
558C: FE 02           CP      $02                 
558E: 28 06           JR      Z,$5596             ; {}
5590: 21 AA 55        LD      HL,$55AA            
5593: C3 7E 63        JP      $637E               ; {}
5596: CD A2 7A        CALL    $7AA2               ; {}
5599: CA 2D 63        JP      Z,$632D             ; {}
559C: AF              XOR     A                   
559D: 02              LD      (BC),A              
559E: 21 AD 55        LD      HL,$55AD            
55A1: C3 81 7A        JP      $7A81               ; {}
55A4: 80              ADD     A,B                 
55A5: FA 40 C0        LD      A,($C040)           
55A8: C7              RST     0X00                
55A9: 04              INC     B                   
55AA: E0 C7           LDFF00  ($C7),A             
55AC: 04              INC     B                   
55AD: 80              ADD     A,B                 
55AE: FA 60 C0        LD      A,($C060)           
55B1: C7              RST     0X00                
55B2: 04              INC     B                   
55B3: CD 6A 63        CALL    $636A               ; {}
55B6: 21 F0 55        LD      HL,$55F0            
55B9: C3 F8 62        JP      $62F8               ; {}
55BC: CD 6D 7A        CALL    $7A6D               ; {}
55BF: C0              RET     NZ                  
55C0: CD 71 7A        CALL    $7A71               ; {}
55C3: FE 06           CP      $06                 
55C5: CA 2D 63        JP      Z,$632D             ; {}
55C8: FE 02           CP      $02                 
55CA: CA DB 55        JP      Z,$55DB             ; {}
55CD: FE 04           CP      $04                 
55CF: CA E2 55        JP      Z,$55E2             ; {}
55D2: 21 E6 55        LD      HL,$55E6            
55D5: CD 60 7A        CALL    $7A60               ; {}
55D8: C3 7E 63        JP      $637E               ; {}
55DB: 3E 40           LD      A,$40               
55DD: E0 1C           LDFF00  ($1C),A             
55DF: 0A              LD      A,(BC)              
55E0: 18 F0           JR      $55D2               ; {}
55E2: 3E 60           LD      A,$60               
55E4: 18 F7           JR      $55DD               ; {}
55E6: F6 55           OR      $55                 
55E8: F3              DI                          
55E9: 55              LD      D,L                 
55EA: F6 55           OR      $55                 
55EC: F3              DI                          
55ED: 55              LD      D,L                 
55EE: F6 55           OR      $55                 
55F0: 80              ADD     A,B                 
55F1: FA 20 DA        LD      A,($DA20)           
55F4: C7              RST     0X00                
55F5: 02              LD      (BC),A              
55F6: EA C7 02        LD      ($02C7),A           
55F9: FA 61 D3        LD      A,($D361)           
55FC: FE 01           CP      $01                 
55FE: C8              RET     Z                   
55FF: 3E 0C           LD      A,$0C               
5601: EA BE D3        LD      ($D3BE),A           
5604: CD 65 63        CALL    $6365               ; {}
5607: 21 39 56        LD      HL,$5639            
560A: CD B9 7A        CALL    $7AB9               ; {}
560D: C3 F8 62        JP      $62F8               ; {}
5610: CD 71 7A        CALL    $7A71               ; {}
5613: FE 02           CP      $02                 
5615: 28 11           JR      Z,$5628             ; {}
5617: 21 37 56        LD      HL,$5637            
561A: C3 E7 7A        JP      $7AE7               ; {}
561D: AF              XOR     A                   
561E: 02              LD      (BC),A              
561F: 21 3F 56        LD      HL,$563F            
5622: CD B9 7A        CALL    $7AB9               ; {}
5625: C3 81 7A        JP      $7A81               ; {}
5628: CD A2 7A        CALL    $7AA2               ; {}
562B: CA 27 63        JP      Z,$6327             ; {}
562E: FE 07           CP      $07                 
5630: 28 EB           JR      Z,$561D             ; {}
5632: 3E 01           LD      A,$01               
5634: 02              LD      (BC),A              
5635: 18 E0           JR      $5617               ; {}
5637: 00              NOP                         
5638: 03              INC     BC                  
5639: 80              ADD     A,B                 
563A: D2 40 E0        JP      NC,$E040            
563D: 87              ADD     A,A                 
563E: 01 80 D2        LD      BC,$D280            
5641: 60              LD      H,B                 
5642: E0 87           LDFF00  ($87),A             
5644: 01 FA 71        LD      BC,$71FA            
5647: D3                              
5648: FE 03           CP      $03                 
564A: CA 85 63        JP      Z,$6385             ; {}
564D: 3E 02           LD      A,$02               
564F: EA BE D3        LD      ($D3BE),A           
5652: CD 65 63        CALL    $6365               ; {}
5655: 21 C5 56        LD      HL,$56C5            
5658: CD B9 7A        CALL    $7AB9               ; {}
565B: C3 F8 62        JP      $62F8               ; {}
565E: CD 6D 7A        CALL    $7A6D               ; {}
5661: C0              RET     NZ                  
5662: 3E 01           LD      A,$01               
5664: 12              LD      (DE),A              
5665: CD 71 7A        CALL    $7A71               ; {}
5668: FE 1D           CP      $1D                 
566A: 28 0A           JR      Z,$5676             ; {}
566C: FE 15           CP      $15                 
566E: 30 18           JR      NC,$5688            ; {}
5670: 21 8D 56        LD      HL,$568D            
5673: C3 E7 7A        JP      $7AE7               ; {}
5676: CD A2 7A        CALL    $7AA2               ; {}
5679: CA 27 63        JP      Z,$6327             ; {}
567C: 3E 14           LD      A,$14               
567E: 02              LD      (BC),A              
567F: 21 CB 56        LD      HL,$56CB            
5682: CD B9 7A        CALL    $7AB9               ; {}
5685: C3 81 7A        JP      $7A81               ; {}
5688: 3E 02           LD      A,$02               
568A: 12              LD      (DE),A              
568B: 18 E3           JR      $5670               ; {}
568D: 00              NOP                         
568E: 40              LD      B,B                 
568F: 00              NOP                         
5690: 40              LD      B,B                 
5691: 00              NOP                         
5692: 40              LD      B,B                 
5693: 01 00 00        LD      BC,$0000            
5696: 20 FF           JR      NZ,$5697            ; {}
5698: E0 00           LDFF00  ($00),A             
569A: 40              LD      B,B                 
569B: FF              RST     0X38                
569C: C0              RET     NZ                  
569D: 00              NOP                         
569E: 60              LD      H,B                 
569F: FF              RST     0X38                
56A0: A0              AND     B                   
56A1: 00              NOP                         
56A2: 80              ADD     A,B                 
56A3: FF              RST     0X38                
56A4: 80              ADD     A,B                 
56A5: 00              NOP                         
56A6: A0              AND     B                   
56A7: FF              RST     0X38                
56A8: 60              LD      H,B                 
56A9: 00              NOP                         
56AA: C0              RET     NZ                  
56AB: FF              RST     0X38                
56AC: 40              LD      B,B                 
56AD: 01 00 FF        LD      BC,$FF00            
56B0: 00              NOP                         
56B1: 01 00 FF        LD      BC,$FF00            
56B4: 00              NOP                         
56B5: FF              RST     0X38                
56B6: E0 FF           LDFF00  ($FF),A             
56B8: C0              RET     NZ                  
56B9: FF              RST     0X38                
56BA: A0              AND     B                   
56BB: FF              RST     0X38                
56BC: 80              ADD     A,B                 
56BD: FF              RST     0X38                
56BE: 60              LD      H,B                 
56BF: FF              RST     0X38                
56C0: 40              LD      B,B                 
56C1: FF              RST     0X38                
56C2: 20 FF           JR      NZ,$56C3            ; {}
56C4: 00              NOP                         
56C5: 80              ADD     A,B                 
56C6: 00              NOP                         
56C7: 20 40           JR      NZ,$5709            ; {}
56C9: 84              ADD     A,H                 
56CA: 02              LD      (BC),A              
56CB: 80              ADD     A,B                 
56CC: 00              NOP                         
56CD: 60              LD      H,B                 
56CE: 00              NOP                         
56CF: 86              ADD     A,(HL)              
56D0: 02              LD      (BC),A              
56D1: 3E 08           LD      A,$08               
56D3: EA BE D3        LD      ($D3BE),A           
56D6: CD 79 63        CALL    $6379               ; {}
56D9: 21 16 57        LD      HL,$5716            
56DC: CD B9 7A        CALL    $7AB9               ; {}
56DF: C3 F3 62        JP      $62F3               ; {}
56E2: CD 71 7A        CALL    $7A71               ; {}
56E5: FE 0F           CP      $0F                 
56E7: 28 06           JR      Z,$56EF             ; {}
56E9: 21 FA 56        LD      HL,$56FA            
56EC: C3 E7 7A        JP      $7AE7               ; {}
56EF: CD A2 7A        CALL    $7AA2               ; {}
56F2: CA 27 63        JP      Z,$6327             ; {}
56F5: 3E 01           LD      A,$01               
56F7: 02              LD      (BC),A              
56F8: 18 EF           JR      $56E9               ; {}
56FA: 00              NOP                         
56FB: 0A              LD      A,(BC)              
56FC: 00              NOP                         
56FD: 06 FF           LD      B,$FF               
56FF: F0 00           LD      A,($00)             
5701: 20 00           JR      NZ,$5703            ; {}
5703: 0A              LD      A,(BC)              
5704: 00              NOP                         
5705: 06 FF           LD      B,$FF               
5707: FA FF F6        LD      A,($F6FF)           
570A: 00              NOP                         
570B: 20 00           JR      NZ,$570D            ; {}
570D: 0A              LD      A,(BC)              
570E: 00              NOP                         
570F: 06 FF           LD      B,$FF               
5711: FA FF F6        LD      A,($F6FF)           
5714: FF              RST     0X38                
5715: A8              XOR     B                   
5716: 80              ADD     A,B                 
5717: 00              NOP                         
5718: 20 60           JR      NZ,$577A            ; {}
571A: 87              ADD     A,A                 
571B: 00              NOP                         
571C: 8A              ADC     A,D                 
571D: DF              RST     0X18                
571E: FD                              
571F: A8              XOR     B                   
5720: 87              ADD     A,A                 
5721: 42              LD      B,D                 
5722: 24              INC     H                   
5723: 78              LD      A,B                 
5724: 8A              ADC     A,D                 
5725: DF              RST     0X18                
5726: FD                              
5727: A8              XOR     B                   
5728: 87              ADD     A,A                 
5729: 42              LD      B,D                 
572A: 24              INC     H                   
572B: 78              LD      A,B                 
572C: 21 1C 57        LD      HL,$571C            
572F: C3 5A 63        JP      $635A               ; {}
5732: 21 2F D3        LD      HL,$D32F            
5735: CB FE           SET     1,E                 
5737: CD 2C 57        CALL    $572C               ; {}
573A: 21 90 57        LD      HL,$5790            
573D: C3 F3 62        JP      $62F3               ; {}
5740: CD 6D 7A        CALL    $7A6D               ; {}
5743: C0              RET     NZ                  
5744: CD 71 7A        CALL    $7A71               ; {}
5747: FE 14           CP      $14                 
5749: 28 11           JR      Z,$575C             ; {}
574B: 21 6A 57        LD      HL,$576A            
574E: CD 60 7A        CALL    $7A60               ; {}
5751: FA 96 D3        LD      A,($D396)           
5754: E6 01           AND     $01                 
5756: C2 7B 7A        JP      NZ,$7A7B            ; {}
5759: C3 81 7A        JP      $7A81               ; {}
575C: 21 1D 43        LD      HL,$431D            
575F: CD 7B 7A        CALL    $7A7B               ; {}
5762: 21 2F D3        LD      HL,$D32F            
5765: CB BE           RES     1,E                 
5767: C3 27 63        JP      $6327               ; {}
576A: CC 57 96        CALL    Z,$9657             
576D: 57              LD      D,A                 
576E: D1              POP     DE                  
576F: 57              LD      D,A                 
5770: 9C              SBC     H                   
5771: 57              LD      D,A                 
5772: D6 57           SUB     $57                 
5774: A2              AND     D                   
5775: 57              LD      D,A                 
5776: DB                              
5777: 57              LD      D,A                 
5778: A8              XOR     B                   
5779: 57              LD      D,A                 
577A: E0 57           LDFF00  ($57),A             
577C: AE              XOR     (HL)                
577D: 57              LD      D,A                 
577E: E5              PUSH    HL                  
577F: 57              LD      D,A                 
5780: B4              OR      H                   
5781: 57              LD      D,A                 
5782: EA 57 BA        LD      ($BA57),A           
5785: 57              LD      D,A                 
5786: EF              RST     0X28                
5787: 57              LD      D,A                 
5788: C0              RET     NZ                  
5789: 57              LD      D,A                 
578A: F4                              
578B: 57              LD      D,A                 
578C: C6 57           ADD     $57                 
578E: F9              LD      SP,HL               
578F: 57              LD      D,A                 
5790: 80              ADD     A,B                 
5791: E6 20           AND     $20                 
5793: 8A              ADC     A,D                 
5794: C7              RST     0X00                
5795: 08 80 E6        LD      ($E680),SP          
5798: 20 97           JR      NZ,$5731            ; {}
579A: C7              RST     0X00                
579B: 08 80 60        LD      ($6080),SP          ; {}
579E: 20 9C           JR      NZ,$573C            ; {}
57A0: C7              RST     0X00                
57A1: 08 80 E6        LD      ($E680),SP          
57A4: 20 8A           JR      NZ,$5730            ; {}
57A6: C7              RST     0X00                
57A7: 08 80 E6        LD      ($E680),SP          
57AA: 20 97           JR      NZ,$5743            ; {}
57AC: C7              RST     0X00                
57AD: 08 80 E6        LD      ($E680),SP          
57B0: 20 9C           JR      NZ,$574E            ; {}
57B2: C7              RST     0X00                
57B3: 08 80 E6        LD      ($E680),SP          
57B6: 20 97           JR      NZ,$574F            ; {}
57B8: C7              RST     0X00                
57B9: 08 80 E6        LD      ($E680),SP          
57BC: 20 8A           JR      NZ,$5748            ; {}
57BE: C7              RST     0X00                
57BF: 08 80 E6        LD      ($E680),SP          
57C2: 20 62           JR      NZ,$5826            ; {}
57C4: C7              RST     0X00                
57C5: 08 80 00        LD      ($0080),SP          
57C8: 20 79           JR      NZ,$5843            ; {}
57CA: C7              RST     0X00                
57CB: 08 80 20        LD      ($2080),SP          
57CE: 8A              ADC     A,D                 
57CF: 87              ADD     A,A                 
57D0: 02              LD      (BC),A              
57D1: 80              ADD     A,B                 
57D2: 20 97           JR      NZ,$576B            ; {}
57D4: 87              ADD     A,A                 
57D5: 02              LD      (BC),A              
57D6: 80              ADD     A,B                 
57D7: 20 9C           JR      NZ,$5775            ; {}
57D9: 87              ADD     A,A                 
57DA: 34              INC     (HL)                
57DB: 80              ADD     A,B                 
57DC: 20 8A           JR      NZ,$5768            ; {}
57DE: 87              ADD     A,A                 
57DF: 02              LD      (BC),A              
57E0: 80              ADD     A,B                 
57E1: 20 97           JR      NZ,$577A            ; {}
57E3: 87              ADD     A,A                 
57E4: 02              LD      (BC),A              
57E5: 80              ADD     A,B                 
57E6: 20 9C           JR      NZ,$5784            ; {}
57E8: 87              ADD     A,A                 
57E9: 02              LD      (BC),A              
57EA: 80              ADD     A,B                 
57EB: 20 97           JR      NZ,$5784            ; {}
57ED: 87              ADD     A,A                 
57EE: 02              LD      (BC),A              
57EF: 80              ADD     A,B                 
57F0: 20 8A           JR      NZ,$577C            ; {}
57F2: 87              ADD     A,A                 
57F3: 02              LD      (BC),A              
57F4: 80              ADD     A,B                 
57F5: 20 62           JR      NZ,$5859            ; {}
57F7: 87              ADD     A,A                 
57F8: 02              LD      (BC),A              
57F9: 80              ADD     A,B                 
57FA: 20 79           JR      NZ,$5875            ; {}
57FC: 87              ADD     A,A                 
57FD: 48              LD      C,B                 
57FE: 21 2F D3        LD      HL,$D32F            
5801: CB FE           SET     1,E                 
5803: CD 2C 57        CALL    $572C               ; {}
5806: 21 4B 58        LD      HL,$584B            
5809: C3 F3 62        JP      $62F3               ; {}
580C: CD 6D 7A        CALL    $7A6D               ; {}
580F: C0              RET     NZ                  
5810: CD 71 7A        CALL    $7A71               ; {}
5813: FE 16           CP      $16                 
5815: CA 5C 57        JP      Z,$575C             ; {}
5818: 21 21 58        LD      HL,$5821            
581B: CD 60 7A        CALL    $7A60               ; {}
581E: C3 51 57        JP      $5751               ; {}
5821: 7B              LD      A,E                 
5822: 58              LD      E,B                 
5823: 51              LD      D,C                 
5824: 58              LD      E,B                 
5825: 80              ADD     A,B                 
5826: 58              LD      E,B                 
5827: 57              LD      D,A                 
5828: 58              LD      E,B                 
5829: 85              ADD     A,L                 
582A: 58              LD      E,B                 
582B: 5D              LD      E,L                 
582C: 58              LD      E,B                 
582D: 8A              ADC     A,D                 
582E: 58              LD      E,B                 
582F: 63              LD      H,E                 
5830: 58              LD      E,B                 
5831: 8F              ADC     A,A                 
5832: 58              LD      E,B                 
5833: 69              LD      L,C                 
5834: 58              LD      E,B                 
5835: 94              SUB     H                   
5836: 58              LD      E,B                 
5837: 6F              LD      L,A                 
5838: 58              LD      E,B                 
5839: 99              SBC     C                   
583A: 58              LD      E,B                 
583B: 5D              LD      E,L                 
583C: 58              LD      E,B                 
583D: 8A              ADC     A,D                 
583E: 58              LD      E,B                 
583F: 57              LD      D,A                 
5840: 58              LD      E,B                 
5841: 85              ADD     A,L                 
5842: 58              LD      E,B                 
5843: 51              LD      D,C                 
5844: 58              LD      E,B                 
5845: 80              ADD     A,B                 
5846: 58              LD      E,B                 
5847: 75              LD      (HL),L              
5848: 58              LD      E,B                 
5849: 9E              SBC     (HL)                
584A: 58              LD      E,B                 
584B: 80              ADD     A,B                 
584C: E0 20           LDFF00  ($20),A             
584E: 9D              SBC     L                   
584F: C7              RST     0X00                
5850: 04              INC     B                   
5851: 80              ADD     A,B                 
5852: E0 20           LDFF00  ($20),A             
5854: A7              AND     A                   
5855: C7              RST     0X00                
5856: 04              INC     B                   
5857: 80              ADD     A,B                 
5858: E0 20           LDFF00  ($20),A             
585A: B0              OR      B                   
585B: C7              RST     0X00                
585C: 04              INC     B                   
585D: 80              ADD     A,B                 
585E: E0 20           LDFF00  ($20),A             
5860: B6              OR      (HL)                
5861: C7              RST     0X00                
5862: 04              INC     B                   
5863: 80              ADD     A,B                 
5864: 90              SUB     B                   
5865: 20 BD           JR      NZ,$5824            ; {}
5867: C7              RST     0X00                
5868: 04              INC     B                   
5869: 80              ADD     A,B                 
586A: E0 20           LDFF00  ($20),A             
586C: C4 C7 04        CALL    NZ,$04C7            
586F: 80              ADD     A,B                 
5870: E0 20           LDFF00  ($20),A             
5872: BD              CP      L                   
5873: C7              RST     0X00                
5874: 04              INC     B                   
5875: 80              ADD     A,B                 
5876: 80              ADD     A,B                 
5877: 20 9D           JR      NZ,$5816            ; {}
5879: C7              RST     0X00                
587A: 04              INC     B                   
587B: 80              ADD     A,B                 
587C: 20 9D           JR      NZ,$581B            ; {}
587E: 87              ADD     A,A                 
587F: 07              RLCA                        
5880: 80              ADD     A,B                 
5881: 20 A7           JR      NZ,$582A            ; {}
5883: 87              ADD     A,A                 
5884: 07              RLCA                        
5885: 80              ADD     A,B                 
5886: 20 B0           JR      NZ,$5838            ; {}
5888: 87              ADD     A,A                 
5889: 07              RLCA                        
588A: 80              ADD     A,B                 
588B: 20 B6           JR      NZ,$5843            ; {}
588D: 87              ADD     A,A                 
588E: 07              RLCA                        
588F: 80              ADD     A,B                 
5890: 20 BD           JR      NZ,$584F            ; {}
5892: 87              ADD     A,A                 
5893: 23              INC     HL                  
5894: 80              ADD     A,B                 
5895: 20 C4           JR      NZ,$585B            ; {}
5897: 87              ADD     A,A                 
5898: 07              RLCA                        
5899: 80              ADD     A,B                 
589A: 20 BD           JR      NZ,$5859            ; {}
589C: 87              ADD     A,A                 
589D: 07              RLCA                        
589E: 80              ADD     A,B                 
589F: 20 9D           JR      NZ,$583E            ; {}
58A1: 87              ADD     A,A                 
58A2: 35              DEC     (HL)                
58A3: CD 17 7B        CALL    $7B17               ; {}
58A6: CD 2C 57        CALL    $572C               ; {}
58A9: 21 4B 58        LD      HL,$584B            
58AC: C3 F3 62        JP      $62F3               ; {}
58AF: CD 6D 7A        CALL    $7A6D               ; {}
58B2: C0              RET     NZ                  
58B3: CD 71 7A        CALL    $7A71               ; {}
58B6: FE 12           CP      $12                 
58B8: CA 5C 57        JP      Z,$575C             ; {}
58BB: 21 C4 58        LD      HL,$58C4            
58BE: CD 60 7A        CALL    $7A60               ; {}
58C1: C3 51 57        JP      $5751               ; {}
58C4: 1C              INC     E                   
58C5: 59              LD      E,C                 
58C6: EC                              
58C7: 58              LD      E,B                 
58C8: 21 59 F2        LD      HL,$F259            
58CB: 58              LD      E,B                 
58CC: 26 59           LD      H,$59               
58CE: F8 58           LDHL    SP,$58              
58D0: 2B              DEC     HL                  
58D1: 59              LD      E,C                 
58D2: FE 58           CP      $58                 
58D4: 30 59           JR      NC,$592F            ; {}
58D6: 04              INC     B                   
58D7: 59              LD      E,C                 
58D8: 35              DEC     (HL)                
58D9: 59              LD      E,C                 
58DA: 0A              LD      A,(BC)              
58DB: 59              LD      E,C                 
58DC: 3A              LD      A,(HLD)             
58DD: 59              LD      E,C                 
58DE: 10 59           STOP    $59                 
58E0: 3F              CCF                         
58E1: 59              LD      E,C                 
58E2: 16 59           LD      D,$59               
58E4: 44              LD      B,H                 
58E5: 59              LD      E,C                 
58E6: 80              ADD     A,B                 
58E7: C0              RET     NZ                  
58E8: 20 9D           JR      NZ,$5887            ; {}
58EA: C7              RST     0X00                
58EB: 04              INC     B                   
58EC: 80              ADD     A,B                 
58ED: F0 20           LD      A,($20)             
58EF: 9D              SBC     L                   
58F0: C7              RST     0X00                
58F1: 04              INC     B                   
58F2: 80              ADD     A,B                 
58F3: F0 20           LD      A,($20)             
58F5: 7B              LD      A,E                 
58F6: C7              RST     0X00                
58F7: 04              INC     B                   
58F8: 80              ADD     A,B                 
58F9: F0 20           LD      A,($20)             
58FB: 8E              ADC     A,(HL)              
58FC: C7              RST     0X00                
58FD: 04              INC     B                   
58FE: 80              ADD     A,B                 
58FF: C0              RET     NZ                  
5900: 20 A6           JR      NZ,$58A8            ; {}
5902: C7              RST     0X00                
5903: 04              INC     B                   
5904: 80              ADD     A,B                 
5905: C0              RET     NZ                  
5906: 20 9D           JR      NZ,$58A5            ; {}
5908: C7              RST     0X00                
5909: 04              INC     B                   
590A: 80              ADD     A,B                 
590B: C0              RET     NZ                  
590C: 20 BD           JR      NZ,$58CB            ; {}
590E: C7              RST     0X00                
590F: 04              INC     B                   
5910: 80              ADD     A,B                 
5911: F0 20           LD      A,($20)             
5913: BD              CP      L                   
5914: C7              RST     0X00                
5915: 04              INC     B                   
5916: 80              ADD     A,B                 
5917: 80              ADD     A,B                 
5918: 20 BD           JR      NZ,$58D7            ; {}
591A: C7              RST     0X00                
591B: 04              INC     B                   
591C: 80              ADD     A,B                 
591D: 20 9D           JR      NZ,$58BC            ; {}
591F: 87              ADD     A,A                 
5920: 14              INC     D                   
5921: 80              ADD     A,B                 
5922: 20 9D           JR      NZ,$58C1            ; {}
5924: 87              ADD     A,A                 
5925: 08 80 20        LD      ($2080),SP          
5928: 7B              LD      A,E                 
5929: 87              ADD     A,A                 
592A: 08 80 20        LD      ($2080),SP          
592D: 8E              ADC     A,(HL)              
592E: 87              ADD     A,A                 
592F: 08 80 20        LD      ($2080),SP          
5932: A6              AND     (HL)                
5933: 87              ADD     A,A                 
5934: 14              INC     D                   
5935: 80              ADD     A,B                 
5936: 20 9D           JR      NZ,$58D5            ; {}
5938: 87              ADD     A,A                 
5939: 14              INC     D                   
593A: 80              ADD     A,B                 
593B: 20 BD           JR      NZ,$58FA            ; {}
593D: 87              ADD     A,A                 
593E: 14              INC     D                   
593F: 80              ADD     A,B                 
5940: 20 BD           JR      NZ,$58FF            ; {}
5942: 87              ADD     A,A                 
5943: 08 80 20        LD      ($2080),SP          
5946: BD              CP      L                   
5947: 87              ADD     A,A                 
5948: 2C              INC     L                   
5949: 3E 08           LD      A,$08               
594B: EA BE D3        LD      ($D3BE),A           
594E: CD 6F 63        CALL    $636F               ; {}
5951: 21 8D 59        LD      HL,$598D            
5954: CD B9 7A        CALL    $7AB9               ; {}
5957: C3 F3 62        JP      $62F3               ; {}
595A: CD 71 7A        CALL    $7A71               ; {}
595D: FE 09           CP      $09                 
595F: 28 06           JR      Z,$5967             ; {}
5961: 21 7D 59        LD      HL,$597D            
5964: C3 E7 7A        JP      $7AE7               ; {}
5967: CD A2 7A        CALL    $7AA2               ; {}
596A: CA 27 63        JP      Z,$6327             ; {}
596D: FE 02           CP      $02                 
596F: 28 05           JR      Z,$5976             ; {}
5971: 3E 01           LD      A,$01               
5973: 02              LD      (BC),A              
5974: 18 EB           JR      $5961               ; {}
5976: AF              XOR     A                   
5977: 02              LD      (BC),A              
5978: 3E 60           LD      A,$60               
597A: E0 1C           LDFF00  ($1C),A             
597C: C9              RET                         
597D: FF              RST     0X38                
597E: FE FF           CP      $FF                 
5980: FC                              
5981: FF              RST     0X38                
5982: F8 FF           LDHL    SP,$FF              
5984: E8 00           ADD     SP,$00              
5986: 14              INC     D                   
5987: 00              NOP                         
5988: 02              LD      (BC),A              
5989: 00              NOP                         
598A: 04              INC     B                   
598B: 00              NOP                         
598C: 06 80           LD      B,$80               
598E: 00              NOP                         
598F: 40              LD      B,B                 
5990: C0              RET     NZ                  
5991: 87              ADD     A,A                 
5992: 01 80 00        LD      BC,$0080            
5995: 60              LD      H,B                 
5996: C0              RET     NZ                  
5997: 87              ADD     A,A                 
5998: 01 3E 10        LD      BC,$103E            
599B: EA BE D3        LD      ($D3BE),A           
599E: CD 60 63        CALL    $6360               ; {}
59A1: 21 D5 59        LD      HL,$59D5            
59A4: CD B9 7A        CALL    $7AB9               ; {}
59A7: C3 F8 62        JP      $62F8               ; {}
59AA: CD 71 7A        CALL    $7A71               ; {}
59AD: FE 03           CP      $03                 
59AF: 28 06           JR      Z,$59B7             ; {}
59B1: 21 D1 59        LD      HL,$59D1            
59B4: C3 E7 7A        JP      $7AE7               ; {}
59B7: CD A2 7A        CALL    $7AA2               ; {}
59BA: CA 27 63        JP      Z,$6327             ; {}
59BD: FE 08           CP      $08                 
59BF: 28 05           JR      Z,$59C6             ; {}
59C1: 3E 01           LD      A,$01               
59C3: 02              LD      (BC),A              
59C4: 18 EB           JR      $59B1               ; {}
59C6: AF              XOR     A                   
59C7: 02              LD      (BC),A              
59C8: 21 DB 59        LD      HL,$59DB            
59CB: CD B9 7A        CALL    $7AB9               ; {}
59CE: C3 81 7A        JP      $7A81               ; {}
59D1: FF              RST     0X38                
59D2: A0              AND     B                   
59D3: 00              NOP                         
59D4: C0              RET     NZ                  
59D5: 80              ADD     A,B                 
59D6: 00              NOP                         
59D7: 20 70           JR      NZ,$5A49            ; {}
59D9: 80              ADD     A,B                 
59DA: 02              LD      (BC),A              
59DB: 80              ADD     A,B                 
59DC: 00              NOP                         
59DD: 60              LD      H,B                 
59DE: 70              LD      (HL),B              
59DF: 80              ADD     A,B                 
59E0: 02              LD      (BC),A              
59E1: CD 60 63        CALL    $6360               ; {}
59E4: 21 07 5A        LD      HL,$5A07            
59E7: C3 F8 62        JP      $62F8               ; {}
59EA: CD 6D 7A        CALL    $7A6D               ; {}
59ED: C0              RET     NZ                  
59EE: CD 71 7A        CALL    $7A71               ; {}
59F1: FE 05           CP      $05                 
59F3: CA 2D 63        JP      Z,$632D             ; {}
59F6: 21 FF 59        LD      HL,$59FF            
59F9: CD 60 7A        CALL    $7A60               ; {}
59FC: C3 81 7A        JP      $7A81               ; {}
59FF: 0D              DEC     C                   
5A00: 5A              LD      E,D                 
5A01: 13              INC     DE                  
5A02: 5A              LD      E,D                 
5A03: 0D              DEC     C                   
5A04: 5A              LD      E,D                 
5A05: 07              RLCA                        
5A06: 5A              LD      E,D                 
5A07: 80              ADD     A,B                 
5A08: FB              EI                          
5A09: 20 00           JR      NZ,$5A0B            ; {}
5A0B: C2 03 80        JP      NZ,$8003            
5A0E: FD                              
5A0F: 40              LD      B,B                 
5A10: 80              ADD     A,B                 
5A11: C3 04 80        JP      $8004               
5A14: FD                              
5A15: 60              LD      H,B                 
5A16: 00              NOP                         
5A17: C4 05 FA        CALL    NZ,$FA05            
5A1A: 71              LD      (HL),C              
5A1B: D3                              
5A1C: FE 0F           CP      $0F                 
5A1E: CA 85 63        JP      Z,$6385             ; {}
5A21: CD 6F 63        CALL    $636F               ; {}
5A24: 21 38 5A        LD      HL,$5A38            
5A27: C3 F8 62        JP      $62F8               ; {}
5A2A: CD 71 7A        CALL    $7A71               ; {}
5A2D: FE 02           CP      $02                 
5A2F: CA 2D 63        JP      Z,$632D             ; {}
5A32: 21 3E 5A        LD      HL,$5A3E            
5A35: C3 81 7A        JP      $7A81               ; {}
5A38: 80              ADD     A,B                 
5A39: FB              EI                          
5A3A: 60              LD      H,B                 
5A3B: D2 C7 01        JP      NC,$01C7            
5A3E: 80              ADD     A,B                 
5A3F: FB              EI                          
5A40: 40              LD      B,B                 
5A41: D2 C7 02        JP      NC,$02C7            
5A44: 3E 02           LD      A,$02               
5A46: EA BE D3        LD      ($D3BE),A           
5A49: CD 65 63        CALL    $6365               ; {}
5A4C: 21 5B 5B        LD      HL,$5B5B            
5A4F: CD B9 7A        CALL    $7AB9               ; {}
5A52: C3 F3 62        JP      $62F3               ; {}
5A55: CD 6D 7A        CALL    $7A6D               ; {}
5A58: C0              RET     NZ                  
5A59: 3E 01           LD      A,$01               
5A5B: 12              LD      (DE),A              
5A5C: CD 71 7A        CALL    $7A71               ; {}
5A5F: FE 71           CP      $71                 
5A61: 28 06           JR      Z,$5A69             ; {}
5A63: 21 7B 5A        LD      HL,$5A7B            
5A66: C3 E7 7A        JP      $7AE7               ; {}
5A69: CD A2 7A        CALL    $7AA2               ; {}
5A6C: CA 27 63        JP      Z,$6327             ; {}
5A6F: 3E 60           LD      A,$60               
5A71: 02              LD      (BC),A              
5A72: 21 61 5B        LD      HL,$5B61            
5A75: CD B9 7A        CALL    $7AB9               ; {}
5A78: C3 81 7A        JP      $7A81               ; {}
5A7B: 00              NOP                         
5A7C: B0              OR      B                   
5A7D: 00              NOP                         
5A7E: B0              OR      B                   
5A7F: 00              NOP                         
5A80: B0              OR      B                   
5A81: 00              NOP                         
5A82: B0              OR      B                   
5A83: 00              NOP                         
5A84: 60              LD      H,B                 
5A85: 00              NOP                         
5A86: 60              LD      H,B                 
5A87: 00              NOP                         
5A88: 60              LD      H,B                 
5A89: 00              NOP                         
5A8A: 60              LD      H,B                 
5A8B: 00              NOP                         
5A8C: 20 FF           JR      NZ,$5A8D            ; {}
5A8E: E0 00           LDFF00  ($00),A             
5A90: 40              LD      B,B                 
5A91: FF              RST     0X38                
5A92: C0              RET     NZ                  
5A93: 00              NOP                         
5A94: 60              LD      H,B                 
5A95: FF              RST     0X38                
5A96: A0              AND     B                   
5A97: 00              NOP                         
5A98: 80              ADD     A,B                 
5A99: FF              RST     0X38                
5A9A: 80              ADD     A,B                 
5A9B: 00              NOP                         
5A9C: A0              AND     B                   
5A9D: FF              RST     0X38                
5A9E: 60              LD      H,B                 
5A9F: 00              NOP                         
5AA0: C0              RET     NZ                  
5AA1: FF              RST     0X38                
5AA2: 40              LD      B,B                 
5AA3: 00              NOP                         
5AA4: 80              ADD     A,B                 
5AA5: FF              RST     0X38                
5AA6: 88              ADC     A,B                 
5AA7: 00              NOP                         
5AA8: 80              ADD     A,B                 
5AA9: FF              RST     0X38                
5AAA: 88              ADC     A,B                 
5AAB: 00              NOP                         
5AAC: 90              SUB     B                   
5AAD: FF              RST     0X38                
5AAE: 78              LD      A,B                 
5AAF: 00              NOP                         
5AB0: A0              AND     B                   
5AB1: FF              RST     0X38                
5AB2: 68              LD      L,B                 
5AB3: 00              NOP                         
5AB4: B0              OR      B                   
5AB5: FF              RST     0X38                
5AB6: 56              LD      D,(HL)              
5AB7: 00              NOP                         
5AB8: C0              RET     NZ                  
5AB9: FF              RST     0X38                
5ABA: 46              LD      B,(HL)              
5ABB: 00              NOP                         
5ABC: C0              RET     NZ                  
5ABD: FF              RST     0X38                
5ABE: 44              LD      B,H                 
5ABF: 00              NOP                         
5AC0: C0              RET     NZ                  
5AC1: FF              RST     0X38                
5AC2: 44              LD      B,H                 
5AC3: 00              NOP                         
5AC4: C0              RET     NZ                  
5AC5: FF              RST     0X38                
5AC6: 43              LD      B,E                 
5AC7: 00              NOP                         
5AC8: C0              RET     NZ                  
5AC9: FF              RST     0X38                
5ACA: 43              LD      B,E                 
5ACB: 00              NOP                         
5ACC: C0              RET     NZ                  
5ACD: FF              RST     0X38                
5ACE: 42              LD      B,D                 
5ACF: 00              NOP                         
5AD0: A0              AND     B                   
5AD1: FF              RST     0X38                
5AD2: 62              LD      H,D                 
5AD3: 00              NOP                         
5AD4: 80              ADD     A,B                 
5AD5: FF              RST     0X38                
5AD6: 82              ADD     A,D                 
5AD7: 00              NOP                         
5AD8: 80              ADD     A,B                 
5AD9: FF              RST     0X38                
5ADA: 82              ADD     A,D                 
5ADB: 00              NOP                         
5ADC: 80              ADD     A,B                 
5ADD: FF              RST     0X38                
5ADE: 84              ADD     A,H                 
5ADF: 00              NOP                         
5AE0: 80              ADD     A,B                 
5AE1: FF              RST     0X38                
5AE2: 84              ADD     A,H                 
5AE3: 00              NOP                         
5AE4: 80              ADD     A,B                 
5AE5: FF              RST     0X38                
5AE6: 84              ADD     A,H                 
5AE7: 00              NOP                         
5AE8: 80              ADD     A,B                 
5AE9: FF              RST     0X38                
5AEA: 84              ADD     A,H                 
5AEB: 00              NOP                         
5AEC: 80              ADD     A,B                 
5AED: FF              RST     0X38                
5AEE: B0              OR      B                   
5AEF: 00              NOP                         
5AF0: 80              ADD     A,B                 
5AF1: FF              RST     0X38                
5AF2: B0              OR      B                   
5AF3: 00              NOP                         
5AF4: 80              ADD     A,B                 
5AF5: FF              RST     0X38                
5AF6: 80              ADD     A,B                 
5AF7: 00              NOP                         
5AF8: 80              ADD     A,B                 
5AF9: FF              RST     0X38                
5AFA: 80              ADD     A,B                 
5AFB: 00              NOP                         
5AFC: 80              ADD     A,B                 
5AFD: FF              RST     0X38                
5AFE: 80              ADD     A,B                 
5AFF: 00              NOP                         
5B00: 80              ADD     A,B                 
5B01: FF              RST     0X38                
5B02: 80              ADD     A,B                 
5B03: 00              NOP                         
5B04: 80              ADD     A,B                 
5B05: FF              RST     0X38                
5B06: 68              LD      L,B                 
5B07: 00              NOP                         
5B08: 80              ADD     A,B                 
5B09: FF              RST     0X38                
5B0A: 68              LD      L,B                 
5B0B: 00              NOP                         
5B0C: 80              ADD     A,B                 
5B0D: FF              RST     0X38                
5B0E: 68              LD      L,B                 
5B0F: 00              NOP                         
5B10: 80              ADD     A,B                 
5B11: FF              RST     0X38                
5B12: 68              LD      L,B                 
5B13: 00              NOP                         
5B14: 80              ADD     A,B                 
5B15: FF              RST     0X38                
5B16: 78              LD      A,B                 
5B17: 00              NOP                         
5B18: 80              ADD     A,B                 
5B19: FF              RST     0X38                
5B1A: 78              LD      A,B                 
5B1B: 00              NOP                         
5B1C: A0              AND     B                   
5B1D: FF              RST     0X38                
5B1E: 40              LD      B,B                 
5B1F: 00              NOP                         
5B20: A0              AND     B                   
5B21: FF              RST     0X38                
5B22: 40              LD      B,B                 
5B23: 00              NOP                         
5B24: A0              AND     B                   
5B25: FF              RST     0X38                
5B26: 40              LD      B,B                 
5B27: 00              NOP                         
5B28: A0              AND     B                   
5B29: FF              RST     0X38                
5B2A: 40              LD      B,B                 
5B2B: 00              NOP                         
5B2C: A0              AND     B                   
5B2D: FF              RST     0X38                
5B2E: 40              LD      B,B                 
5B2F: 00              NOP                         
5B30: A0              AND     B                   
5B31: FF              RST     0X38                
5B32: 40              LD      B,B                 
5B33: 00              NOP                         
5B34: A0              AND     B                   
5B35: FF              RST     0X38                
5B36: 40              LD      B,B                 
5B37: 00              NOP                         
5B38: A0              AND     B                   
5B39: FF              RST     0X38                
5B3A: 40              LD      B,B                 
5B3B: 00              NOP                         
5B3C: A0              AND     B                   
5B3D: FF              RST     0X38                
5B3E: 40              LD      B,B                 
5B3F: 00              NOP                         
5B40: A0              AND     B                   
5B41: FF              RST     0X38                
5B42: 40              LD      B,B                 
5B43: 00              NOP                         
5B44: A0              AND     B                   
5B45: FF              RST     0X38                
5B46: 00              NOP                         
5B47: 00              NOP                         
5B48: A0              AND     B                   
5B49: FF              RST     0X38                
5B4A: 00              NOP                         
5B4B: 00              NOP                         
5B4C: 80              ADD     A,B                 
5B4D: FE 80           CP      $80                 
5B4F: 00              NOP                         
5B50: 80              ADD     A,B                 
5B51: FE 80           CP      $80                 
5B53: 00              NOP                         
5B54: 80              ADD     A,B                 
5B55: FE 80           CP      $80                 
5B57: 00              NOP                         
5B58: 80              ADD     A,B                 
5B59: FE 80           CP      $80                 
5B5B: 80              ADD     A,B                 
5B5C: 00              NOP                         
5B5D: 20 A0           JR      NZ,$5AFF            ; {}
5B5F: 81              ADD     A,C                 
5B60: 02              LD      (BC),A              
5B61: 80              ADD     A,B                 
5B62: 00              NOP                         
5B63: 60              LD      H,B                 
5B64: 22              LD      (HLI),A             
5B65: 86              ADD     A,(HL)              
5B66: 02              LD      (BC),A              
5B67: 3E 0C           LD      A,$0C               
5B69: EA BE D3        LD      ($D3BE),A           
5B6C: CD 6A 63        CALL    $636A               ; {}
5B6F: 21 B2 5B        LD      HL,$5BB2            
5B72: CD B9 7A        CALL    $7AB9               ; {}
5B75: C3 F8 62        JP      $62F8               ; {}
5B78: CD 71 7A        CALL    $7A71               ; {}
5B7B: FE 03           CP      $03                 
5B7D: 28 06           JR      Z,$5B85             ; {}
5B7F: 21 AE 5B        LD      HL,$5BAE            
5B82: C3 E7 7A        JP      $7AE7               ; {}
5B85: CD A2 7A        CALL    $7AA2               ; {}
5B88: CA 27 63        JP      Z,$6327             ; {}
5B8B: FE 06           CP      $06                 
5B8D: CA 9E 5B        JP      Z,$5B9E             ; {}
5B90: FE 03           CP      $03                 
5B92: CA A9 5B        JP      Z,$5BA9             ; {}
5B95: 3E 01           LD      A,$01               
5B97: 02              LD      (BC),A              
5B98: 21 AE 5B        LD      HL,$5BAE            
5B9B: C3 E7 7A        JP      $7AE7               ; {}
5B9E: 21 B8 5B        LD      HL,$5BB8            
5BA1: CD B9 7A        CALL    $7AB9               ; {}
5BA4: AF              XOR     A                   
5BA5: 02              LD      (BC),A              
5BA6: C3 81 7A        JP      $7A81               ; {}
5BA9: 21 BE 5B        LD      HL,$5BBE            
5BAC: 18 F3           JR      $5BA1               ; {}
5BAE: 00              NOP                         
5BAF: E0 FF           LDFF00  ($FF),A             
5BB1: A0              AND     B                   
5BB2: 80              ADD     A,B                 
5BB3: 00              NOP                         
5BB4: 20 00           JR      NZ,$5BB6            ; {}
5BB6: 84              ADD     A,H                 
5BB7: 01 80 00        LD      BC,$0080            
5BBA: 40              LD      B,B                 
5BBB: 80              ADD     A,B                 
5BBC: 85              ADD     A,L                 
5BBD: 01 80 00        LD      BC,$0080            
5BC0: 60              LD      H,B                 
5BC1: 80              ADD     A,B                 
5BC2: 85              ADD     A,L                 
5BC3: 01 3E 12        LD      BC,$123E            
5BC6: EA BE D3        LD      ($D3BE),A           
5BC9: CD 6A 63        CALL    $636A               ; {}
5BCC: 21 00 5C        LD      HL,$5C00            
5BCF: CD B9 7A        CALL    $7AB9               ; {}
5BD2: C3 F8 62        JP      $62F8               ; {}
5BD5: CD 71 7A        CALL    $7A71               ; {}
5BD8: FE 03           CP      $03                 
5BDA: 28 06           JR      Z,$5BE2             ; {}
5BDC: 21 FC 5B        LD      HL,$5BFC            
5BDF: C3 E7 7A        JP      $7AE7               ; {}
5BE2: CD A2 7A        CALL    $7AA2               ; {}
5BE5: CA 27 63        JP      Z,$6327             ; {}
5BE8: FE 06           CP      $06                 
5BEA: 28 05           JR      Z,$5BF1             ; {}
5BEC: 3E 01           LD      A,$01               
5BEE: 02              LD      (BC),A              
5BEF: 18 EB           JR      $5BDC               ; {}
5BF1: AF              XOR     A                   
5BF2: 02              LD      (BC),A              
5BF3: 21 06 5C        LD      HL,$5C06            
5BF6: CD B9 7A        CALL    $7AB9               ; {}
5BF9: C3 81 7A        JP      $7A81               ; {}
5BFC: 01 00 FE        LD      BC,$FE00            
5BFF: C0              RET     NZ                  
5C00: 80              ADD     A,B                 
5C01: 00              NOP                         
5C02: 20 40           JR      NZ,$5C44            ; {}
5C04: 86              ADD     A,(HL)              
5C05: 02              LD      (BC),A              
5C06: 80              ADD     A,B                 
5C07: 00              NOP                         
5C08: 60              LD      H,B                 
5C09: C0              RET     NZ                  
5C0A: 84              ADD     A,H                 
5C0B: 02              LD      (BC),A              
5C0C: 3E 04           LD      A,$04               
5C0E: EA BE D3        LD      ($D3BE),A           
5C11: CD 74 63        CALL    $6374               ; {}
5C14: 21 6E 5C        LD      HL,$5C6E            
5C17: CD B9 7A        CALL    $7AB9               ; {}
5C1A: C3 F8 62        JP      $62F8               ; {}
5C1D: CD 6D 7A        CALL    $7A6D               ; {}
5C20: C0              RET     NZ                  
5C21: 3E 01           LD      A,$01               
5C23: 12              LD      (DE),A              
5C24: CD 71 7A        CALL    $7A71               ; {}
5C27: FE 06           CP      $06                 
5C29: 28 23           JR      Z,$5C4E             ; {}
5C2B: FE 07           CP      $07                 
5C2D: 28 06           JR      Z,$5C35             ; {}
5C2F: 21 64 5C        LD      HL,$5C64            
5C32: C3 E7 7A        JP      $7AE7               ; {}
5C35: CD A2 7A        CALL    $7AA2               ; {}
5C38: CA 27 63        JP      Z,$6327             ; {}
5C3B: FE 02           CP      $02                 
5C3D: 28 20           JR      Z,$5C5F             ; {}
5C3F: FE 01           CP      $01                 
5C41: 28 1C           JR      Z,$5C5F             ; {}
5C43: 21 74 5C        LD      HL,$5C74            
5C46: AF              XOR     A                   
5C47: 02              LD      (BC),A              
5C48: CD B9 7A        CALL    $7AB9               ; {}
5C4B: C3 81 7A        JP      $7A81               ; {}
5C4E: FA BE D3        LD      A,($D3BE)           
5C51: FE 01           CP      $01                 
5C53: 28 E0           JR      Z,$5C35             ; {}
5C55: FE 04           CP      $04                 
5C57: C8              RET     Z                   
5C58: 3E 06           LD      A,$06               
5C5A: 12              LD      (DE),A              
5C5B: AF              XOR     A                   
5C5C: E0 1C           LDFF00  ($1C),A             
5C5E: C9              RET                         
5C5F: 21 7A 5C        LD      HL,$5C7A            
5C62: 18 E2           JR      $5C46               ; {}
5C64: 02              LD      (BC),A              
5C65: 40              LD      B,B                 
5C66: 01 40 FF        LD      BC,$FF40            
5C69: F2                              
5C6A: 00              NOP                         
5C6B: 0E FF           LD      C,$FF               
5C6D: F2                              
5C6E: 80              ADD     A,B                 
5C6F: 00              NOP                         
5C70: 20 16           JR      NZ,$5C88            ; {}
5C72: 84              ADD     A,H                 
5C73: 01 80 00        LD      BC,$0080            
5C76: 20 26           JR      NZ,$5C9E            ; {}
5C78: 84              ADD     A,H                 
5C79: 01 80 00        LD      BC,$0080            
5C7C: 20 08           JR      NZ,$5C86            ; {}
5C7E: 84              ADD     A,H                 
5C7F: 01 FA 71        LD      BC,$71FA            
5C82: D3                              
5C83: FE 14           CP      $14                 
5C85: CA 85 63        JP      Z,$6385             ; {}
5C88: 3E 04           LD      A,$04               
5C8A: EA BE D3        LD      ($D3BE),A           
5C8D: CD 6A 63        CALL    $636A               ; {}
5C90: 21 AA 5C        LD      HL,$5CAA            
5C93: CD B9 7A        CALL    $7AB9               ; {}
5C96: C3 F8 62        JP      $62F8               ; {}
5C99: CD A2 7A        CALL    $7AA2               ; {}
5C9C: CA 27 63        JP      Z,$6327             ; {}
5C9F: 3E 01           LD      A,$01               
5CA1: 02              LD      (BC),A              
5CA2: 21 A8 5C        LD      HL,$5CA8            
5CA5: C3 E7 7A        JP      $7AE7               ; {}
5CA8: 00              NOP                         
5CA9: 0E 80           LD      C,$80               
5CAB: 00              NOP                         
5CAC: 40              LD      B,B                 
5CAD: 80              ADD     A,B                 
5CAE: 87              ADD     A,A                 
5CAF: 01 CD 79        LD      BC,$79CD            
5CB2: 63              LD      H,E                 
5CB3: 21 D8 5C        LD      HL,$5CD8            
5CB6: C3 F3 62        JP      $62F3               ; {}
5CB9: CD 6D 7A        CALL    $7A6D               ; {}
5CBC: C0              RET     NZ                  
5CBD: CD 71 7A        CALL    $7A71               ; {}
5CC0: FE 06           CP      $06                 
5CC2: CA 2D 63        JP      Z,$632D             ; {}
5CC5: 21 CE 5C        LD      HL,$5CCE            
5CC8: CD 60 7A        CALL    $7A60               ; {}
5CCB: C3 81 7A        JP      $7A81               ; {}
5CCE: DE 5C           SBC     $5C                 
5CD0: E4                              
5CD1: 5C              LD      E,H                 
5CD2: EA 5C F0        LD      ($F05C),A           
5CD5: 5C              LD      E,H                 
5CD6: F6 5C           OR      $5C                 
5CD8: 80              ADD     A,B                 
5CD9: D0              RET     NC                  
5CDA: 20 40           JR      NZ,$5D1C            ; {}
5CDC: C7              RST     0X00                
5CDD: 14              INC     D                   
5CDE: 80              ADD     A,B                 
5CDF: C0              RET     NZ                  
5CE0: 20 64           JR      NZ,$5D46            ; {}
5CE2: C7              RST     0X00                
5CE3: 0C              INC     C                   
5CE4: 80              ADD     A,B                 
5CE5: 90              SUB     B                   
5CE6: 40              LD      B,B                 
5CE7: 78              LD      A,B                 
5CE8: C7              RST     0X00                
5CE9: 40              LD      B,B                 
5CEA: 80              ADD     A,B                 
5CEB: C0              RET     NZ                  
5CEC: 20 54           JR      NZ,$5D42            ; {}
5CEE: C7              RST     0X00                
5CEF: 06 80           LD      B,$80               
5CF1: C0              RET     NZ                  
5CF2: 40              LD      B,B                 
5CF3: 46              LD      B,(HL)              
5CF4: C7              RST     0X00                
5CF5: 0C              INC     C                   
5CF6: 80              ADD     A,B                 
5CF7: A0              AND     B                   
5CF8: 20 5E           JR      NZ,$5D58            ; {}
5CFA: C7              RST     0X00                
5CFB: 20 FA           JR      NZ,$5CF7            ; {}
5CFD: 71              LD      (HL),C              
5CFE: D3                              
5CFF: FE 03           CP      $03                 
5D01: CA 85 63        JP      Z,$6385             ; {}
5D04: FE 07           CP      $07                 
5D06: CA 85 63        JP      Z,$6385             ; {}
5D09: 3E 02           LD      A,$02               
5D0B: EA BE D3        LD      ($D3BE),A           
5D0E: CD 65 63        CALL    $6365               ; {}
5D11: 21 68 5D        LD      HL,$5D68            
5D14: CD B9 7A        CALL    $7AB9               ; {}
5D17: C3 F8 62        JP      $62F8               ; {}
5D1A: CD 6D 7A        CALL    $7A6D               ; {}
5D1D: C0              RET     NZ                  
5D1E: 3E 01           LD      A,$01               
5D20: 12              LD      (DE),A              
5D21: 0A              LD      A,(BC)              
5D22: FE 07           CP      $07                 
5D24: 30 0D           JR      NC,$5D33            ; {}
5D26: CD 71 7A        CALL    $7A71               ; {}
5D29: FE 10           CP      $10                 
5D2B: 28 0B           JR      Z,$5D38             ; {}
5D2D: 21 4A 5D        LD      HL,$5D4A            
5D30: C3 E7 7A        JP      $7AE7               ; {}
5D33: 3E 03           LD      A,$03               
5D35: 12              LD      (DE),A              
5D36: 18 EE           JR      $5D26               ; {}
5D38: CD A2 7A        CALL    $7AA2               ; {}
5D3B: CA 27 63        JP      Z,$6327             ; {}
5D3E: 3E 03           LD      A,$03               
5D40: 02              LD      (BC),A              
5D41: 21 6E 5D        LD      HL,$5D6E            
5D44: CD B9 7A        CALL    $7AB9               ; {}
5D47: C3 81 7A        JP      $7A81               ; {}
5D4A: 02              LD      (BC),A              
5D4B: 00              NOP                         
5D4C: 02              LD      (BC),A              
5D4D: 00              NOP                         
5D4E: 01 00 00        LD      BC,$0000            
5D51: C0              RET     NZ                  
5D52: FF              RST     0X38                
5D53: 40              LD      B,B                 
5D54: 00              NOP                         
5D55: C0              RET     NZ                  
5D56: FF              RST     0X38                
5D57: 40              LD      B,B                 
5D58: FF              RST     0X38                
5D59: 00              NOP                         
5D5A: FF              RST     0X38                
5D5B: 00              NOP                         
5D5C: FE 00           CP      $00                 
5D5E: FF              RST     0X38                
5D5F: C0              RET     NZ                  
5D60: FF              RST     0X38                
5D61: C0              RET     NZ                  
5D62: FF              RST     0X38                
5D63: C0              RET     NZ                  
5D64: FF              RST     0X38                
5D65: C0              RET     NZ                  
5D66: FF              RST     0X38                
5D67: C0              RET     NZ                  
5D68: 80              ADD     A,B                 
5D69: 00              NOP                         
5D6A: 20 60           JR      NZ,$5DCC            ; {}
5D6C: 80              ADD     A,B                 
5D6D: 02              LD      (BC),A              
5D6E: 80              ADD     A,B                 
5D6F: 00              NOP                         
5D70: 60              LD      H,B                 
5D71: 60              LD      H,B                 
5D72: 85              ADD     A,L                 
5D73: 02              LD      (BC),A              
5D74: 02              LD      (BC),A              
5D75: 46              LD      B,(HL)              
5D76: 8A              ADC     A,D                 
5D77: CE FC           ADC     $FC                 
5D79: 96              SUB     (HL)                
5D7A: 04              INC     B                   
5D7B: 04              INC     B                   
5D7C: 02              LD      (BC),A              
5D7D: 46              LD      B,(HL)              
5D7E: 8A              ADC     A,D                 
5D7F: CE FC           ADC     $FC                 
5D81: 96              SUB     (HL)                
5D82: 04              INC     B                   
5D83: 04              INC     B                   
5D84: 21 4F D3        LD      HL,$D34F            
5D87: CB FE           SET     1,E                 
5D89: 3E 03           LD      A,$03               
5D8B: EA BE D3        LD      ($D3BE),A           
5D8E: 21 B1 5E        LD      HL,$5EB1            
5D91: CD 87 7A        CALL    $7A87               ; {}
5D94: CD 6A 63        CALL    $636A               ; {}
5D97: 21 74 5D        LD      HL,$5D74            
5D9A: CD 5A 63        CALL    $635A               ; {}
5D9D: 21 C5 5E        LD      HL,$5EC5            
5DA0: CD B9 7A        CALL    $7AB9               ; {}
5DA3: C3 F3 62        JP      $62F3               ; {}
5DA6: CD 71 7A        CALL    $7A71               ; {}
5DA9: FE 55           CP      $55                 
5DAB: 28 21           JR      Z,$5DCE             ; {}
5DAD: FE 03           CP      $03                 
5DAF: 28 0A           JR      Z,$5DBB             ; {}
5DB1: FE 07           CP      $07                 
5DB3: 28 0F           JR      Z,$5DC4             ; {}
5DB5: 21 09 5E        LD      HL,$5E09            
5DB8: C3 E7 7A        JP      $7AE7               ; {}
5DBB: 3E 40           LD      A,$40               
5DBD: E0 1C           LDFF00  ($1C),A             
5DBF: 01 96 D3        LD      BC,$D396            
5DC2: 18 F1           JR      $5DB5               ; {}
5DC4: 21 B6 5E        LD      HL,$5EB6            
5DC7: CD 87 7A        CALL    $7A87               ; {}
5DCA: 3E 20           LD      A,$20               
5DCC: 18 EF           JR      $5DBD               ; {}
5DCE: CD A2 7A        CALL    $7AA2               ; {}
5DD1: 28 28           JR      Z,$5DFB             ; {}
5DD3: FE 01           CP      $01                 
5DD5: 28 12           JR      Z,$5DE9             ; {}
5DD7: 3E 40           LD      A,$40               
5DD9: 02              LD      (BC),A              
5DDA: 21 BB 5E        LD      HL,$5EBB            
5DDD: CD 87 7A        CALL    $7A87               ; {}
5DE0: 21 CB 5E        LD      HL,$5ECB            
5DE3: CD B9 7A        CALL    $7AB9               ; {}
5DE6: C3 81 7A        JP      $7A81               ; {}
5DE9: 3E 40           LD      A,$40               
5DEB: 02              LD      (BC),A              
5DEC: 21 C0 5E        LD      HL,$5EC0            
5DEF: CD 87 7A        CALL    $7A87               ; {}
5DF2: 21 D1 5E        LD      HL,$5ED1            
5DF5: CD B9 7A        CALL    $7AB9               ; {}
5DF8: C3 81 7A        JP      $7A81               ; {}
5DFB: 21 4F D3        LD      HL,$D34F            
5DFE: CB BE           RES     1,E                 
5E00: 21 1C 7A        LD      HL,$7A1C            
5E03: CD 87 7A        CALL    $7A87               ; {}
5E06: C3 27 63        JP      $6327               ; {}
5E09: 00              NOP                         
5E0A: 40              LD      B,B                 
5E0B: FF              RST     0X38                
5E0C: E0 00           LDFF00  ($00),A             
5E0E: 40              LD      B,B                 
5E0F: FF              RST     0X38                
5E10: E0 00           LDFF00  ($00),A             
5E12: 30 FF           JR      NC,$5E13            ; {}
5E14: E8 00           ADD     SP,$00              
5E16: 30 FF           JR      NC,$5E17            ; {}
5E18: E8 00           ADD     SP,$00              
5E1A: 20 FF           JR      NZ,$5E1B            ; {}
5E1C: F0 00           LD      A,($00)             
5E1E: 20 FF           JR      NZ,$5E1F            ; {}
5E20: F0 00           LD      A,($00)             
5E22: 10 FF           STOP    $FF                 
5E24: F8 00           LDHL    SP,$00              
5E26: 10 FF           STOP    $FF                 
5E28: F8 00           LDHL    SP,$00              
5E2A: 08 FF F9        LD      ($F9FF),SP          
5E2D: 00              NOP                         
5E2E: 08 FF F9        LD      ($F9FF),SP          
5E31: 00              NOP                         
5E32: 08 FF F9        LD      ($F9FF),SP          
5E35: 00              NOP                         
5E36: 08 FF F9        LD      ($F9FF),SP          
5E39: 00              NOP                         
5E3A: 08 FF F9        LD      ($F9FF),SP          
5E3D: 00              NOP                         
5E3E: 08 FF F9        LD      ($F9FF),SP          
5E41: 00              NOP                         
5E42: 08 FF F8        LD      ($F8FF),SP          
5E45: 00              NOP                         
5E46: 08 FF F8        LD      ($F8FF),SP          
5E49: 00              NOP                         
5E4A: 08 FF F8        LD      ($F8FF),SP          
5E4D: 00              NOP                         
5E4E: 08 FF F8        LD      ($F8FF),SP          
5E51: 00              NOP                         
5E52: 08 FF F7        LD      ($F7FF),SP          
5E55: 00              NOP                         
5E56: 08 FF F7        LD      ($F7FF),SP          
5E59: 00              NOP                         
5E5A: 08 FF F7        LD      ($F7FF),SP          
5E5D: 00              NOP                         
5E5E: 08 FF F7        LD      ($F7FF),SP          
5E61: 00              NOP                         
5E62: 08 FF F7        LD      ($F7FF),SP          
5E65: 00              NOP                         
5E66: 08 FF F7        LD      ($F7FF),SP          
5E69: 00              NOP                         
5E6A: 10 FF           STOP    $FF                 
5E6C: EE 00           XOR     $00                 
5E6E: 10 FF           STOP    $FF                 
5E70: EE 00           XOR     $00                 
5E72: 10 FF           STOP    $FF                 
5E74: EE 00           XOR     $00                 
5E76: 10 FF           STOP    $FF                 
5E78: EE 00           XOR     $00                 
5E7A: 10 FF           STOP    $FF                 
5E7C: EE 00           XOR     $00                 
5E7E: 10 FF           STOP    $FF                 
5E80: EE 00           XOR     $00                 
5E82: 10 FF           STOP    $FF                 
5E84: EE 00           XOR     $00                 
5E86: 10 FF           STOP    $FF                 
5E88: EE 00           XOR     $00                 
5E8A: 10 FF           STOP    $FF                 
5E8C: EE 00           XOR     $00                 
5E8E: 10 FF           STOP    $FF                 
5E90: EE 00           XOR     $00                 
5E92: 10 FF           STOP    $FF                 
5E94: EC                              
5E95: 00              NOP                         
5E96: 10 FF           STOP    $FF                 
5E98: EC                              
5E99: 00              NOP                         
5E9A: 10 FF           STOP    $FF                 
5E9C: EC                              
5E9D: 00              NOP                         
5E9E: 10 FF           STOP    $FF                 
5EA0: EC                              
5EA1: 00              NOP                         
5EA2: 10 FF           STOP    $FF                 
5EA4: EC                              
5EA5: 00              NOP                         
5EA6: 10 FF           STOP    $FF                 
5EA8: EC                              
5EA9: 00              NOP                         
5EAA: 10 FF           STOP    $FF                 
5EAC: EC                              
5EAD: 00              NOP                         
5EAE: 10 FF           STOP    $FF                 
5EB0: EC                              
5EB1: 00              NOP                         
5EB2: 19              ADD     HL,DE               
5EB3: 00              NOP                         
5EB4: 80              ADD     A,B                 
5EB5: 01 00 A0        LD      BC,$A000            
5EB8: 00              NOP                         
5EB9: 80              ADD     A,B                 
5EBA: 01 00 50        LD      BC,$5000            
5EBD: 00              NOP                         
5EBE: 80              ADD     A,B                 
5EBF: 01 00 20        LD      BC,$2000            
5EC2: 00              NOP                         
5EC3: 80              ADD     A,B                 
5EC4: 01 80 00        LD      BC,$0080            
5EC7: 60              LD      H,B                 
5EC8: A0              AND     B                   
5EC9: 86              ADD     A,(HL)              
5ECA: 02              LD      (BC),A              
5ECB: 80              ADD     A,B                 
5ECC: 00              NOP                         
5ECD: 40              LD      B,B                 
5ECE: 20 87           JR      NZ,$5E57            ; {}
5ED0: 02              LD      (BC),A              
5ED1: 80              ADD     A,B                 
5ED2: 00              NOP                         
5ED3: 60              LD      H,B                 
5ED4: 20 87           JR      NZ,$5E5D            ; {}
5ED6: 02              LD      (BC),A              
5ED7: 3E 0E           LD      A,$0E               
5ED9: EA BE D3        LD      ($D3BE),A           
5EDC: CD 65 63        CALL    $6365               ; {}
5EDF: 21 13 5F        LD      HL,$5F13            
5EE2: CD B9 7A        CALL    $7AB9               ; {}
5EE5: C3 F3 62        JP      $62F3               ; {}
5EE8: CD 71 7A        CALL    $7A71               ; {}
5EEB: FE 03           CP      $03                 
5EED: 28 06           JR      Z,$5EF5             ; {}
5EEF: 21 0F 5F        LD      HL,$5F0F            
5EF2: C3 E7 7A        JP      $7AE7               ; {}
5EF5: CD A2 7A        CALL    $7AA2               ; {}
5EF8: CA 27 63        JP      Z,$6327             ; {}
5EFB: FE 07           CP      $07                 
5EFD: 28 05           JR      Z,$5F04             ; {}
5EFF: 3E 01           LD      A,$01               
5F01: 02              LD      (BC),A              
5F02: 18 EB           JR      $5EEF               ; {}
5F04: AF              XOR     A                   
5F05: 02              LD      (BC),A              
5F06: 21 13 5F        LD      HL,$5F13            
5F09: CD B9 7A        CALL    $7AB9               ; {}
5F0C: C3 81 7A        JP      $7A81               ; {}
5F0F: 00              NOP                         
5F10: 60              LD      H,B                 
5F11: FF              RST     0X38                
5F12: 00              NOP                         
5F13: 80              ADD     A,B                 
5F14: 00              NOP                         
5F15: 20 40           JR      NZ,$5F57            ; {}
5F17: 86              ADD     A,(HL)              
5F18: 00              NOP                         
5F19: CD 79 63        CALL    $6379               ; {}
5F1C: 21 72 5F        LD      HL,$5F72            
5F1F: CD B9 7A        CALL    $7AB9               ; {}
5F22: C3 F8 62        JP      $62F8               ; {}
5F25: CD 71 7A        CALL    $7A71               ; {}
5F28: FE 13           CP      $13                 
5F2A: CA 27 63        JP      Z,$6327             ; {}
5F2D: FE 02           CP      $02                 
5F2F: 28 0E           JR      Z,$5F3F             ; {}
5F31: FE 0E           CP      $0E                 
5F33: 28 11           JR      Z,$5F46             ; {}
5F35: FE 10           CP      $10                 
5F37: 28 11           JR      Z,$5F4A             ; {}
5F39: 21 4E 5F        LD      HL,$5F4E            
5F3C: C3 E7 7A        JP      $7AE7               ; {}
5F3F: 3E 20           LD      A,$20               
5F41: E0 1C           LDFF00  ($1C),A             
5F43: 0A              LD      A,(BC)              
5F44: 18 F3           JR      $5F39               ; {}
5F46: 3E 40           LD      A,$40               
5F48: 18 F7           JR      $5F41               ; {}
5F4A: 3E 60           LD      A,$60               
5F4C: 18 F3           JR      $5F41               ; {}
5F4E: FF              RST     0X38                
5F4F: F0 00           LD      A,($00)             
5F51: 12              LD      (DE),A              
5F52: FF              RST     0X38                
5F53: F0 00           LD      A,($00)             
5F55: 12              LD      (DE),A              
5F56: FF              RST     0X38                
5F57: F0 00           LD      A,($00)             
5F59: 12              LD      (DE),A              
5F5A: FF              RST     0X38                
5F5B: E0 00           LDFF00  ($00),A             
5F5D: 1E FF           LD      E,$FF               
5F5F: E0 00           LDFF00  ($00),A             
5F61: 1C              INC     E                   
5F62: FF              RST     0X38                
5F63: E0 00           LDFF00  ($00),A             
5F65: 1A              LD      A,(DE)              
5F66: FF              RST     0X38                
5F67: E0 00           LDFF00  ($00),A             
5F69: 18 FF           JR      $5F6A               ; {}
5F6B: E0 00           LDFF00  ($00),A             
5F6D: 12              LD      (DE),A              
5F6E: FF              RST     0X38                
5F6F: E0 00           LDFF00  ($00),A             
5F71: 14              INC     D                   
5F72: 80              ADD     A,B                 
5F73: 00              NOP                         
5F74: 40              LD      B,B                 
5F75: 30 87           JR      NC,$5EFE            ; {}
5F77: 01 FA 71        LD      BC,$71FA            
5F7A: D3                              
5F7B: FE 03           CP      $03                 
5F7D: CA 85 63        JP      Z,$6385             ; {}
5F80: FE 06           CP      $06                 
5F82: CA 85 63        JP      Z,$6385             ; {}
5F85: FE 07           CP      $07                 
5F87: CA 85 63        JP      Z,$6385             ; {}
5F8A: CD 60 63        CALL    $6360               ; {}
5F8D: 21 AE 5F        LD      HL,$5FAE            
5F90: C3 F8 62        JP      $62F8               ; {}
5F93: CD 6D 7A        CALL    $7A6D               ; {}
5F96: C0              RET     NZ                  
5F97: CD 71 7A        CALL    $7A71               ; {}
5F9A: FE 04           CP      $04                 
5F9C: CA 2D 63        JP      Z,$632D             ; {}
5F9F: 21 A8 5F        LD      HL,$5FA8            
5FA2: CD 60 7A        CALL    $7A60               ; {}
5FA5: C3 81 7A        JP      $7A81               ; {}
5FA8: B4              OR      H                   
5FA9: 5F              LD      E,A                 
5FAA: BA              CP      D                   
5FAB: 5F              LD      E,A                 
5FAC: B4              OR      H                   
5FAD: 5F              LD      E,A                 
5FAE: 80              ADD     A,B                 
5FAF: FD                              
5FB0: 40              LD      B,B                 
5FB1: 20 C0           JR      NZ,$5F73            ; {}
5FB3: 02              LD      (BC),A              
5FB4: 80              ADD     A,B                 
5FB5: FD                              
5FB6: 40              LD      B,B                 
5FB7: 80              ADD     A,B                 
5FB8: C1              POP     BC                  
5FB9: 02              LD      (BC),A              
5FBA: 80              ADD     A,B                 
5FBB: FD                              
5FBC: 40              LD      B,B                 
5FBD: 00              NOP                         
5FBE: C2 02 CD        JP      NZ,$CD02            
5FC1: 79              LD      A,C                 
5FC2: 63              LD      H,E                 
5FC3: 21 EC 5F        LD      HL,$5FEC            
5FC6: C3 F3 62        JP      $62F3               ; {}
5FC9: CD 6D 7A        CALL    $7A6D               ; {}
5FCC: C0              RET     NZ                  
5FCD: CD 71 7A        CALL    $7A71               ; {}
5FD0: FE 08           CP      $08                 
5FD2: CA 2D 63        JP      Z,$632D             ; {}
5FD5: 21 DE 5F        LD      HL,$5FDE            
5FD8: CD 60 7A        CALL    $7A60               ; {}
5FDB: C3 81 7A        JP      $7A81               ; {}
5FDE: 04              INC     B                   
5FDF: 60              LD      H,B                 
5FE0: F2                              
5FE1: 5F              LD      E,A                 
5FE2: 0A              LD      A,(BC)              
5FE3: 60              LD      H,B                 
5FE4: F8 5F           LDHL    SP,$5F              
5FE6: 10 60           STOP    $60                 
5FE8: FE 5F           CP      $5F                 
5FEA: 16 60           LD      D,$60               
5FEC: 80              ADD     A,B                 
5FED: EA 20 62        LD      ($6220),A           ; {}
5FF0: C7              RST     0X00                
5FF1: 06 80           LD      B,$80               
5FF3: EA 20 74        LD      ($7420),A           ; {}
5FF6: C7              RST     0X00                
5FF7: 06 80           LD      B,$80               
5FF9: EA 20 7B        LD      ($7B20),A           ; {}
5FFC: C7              RST     0X00                
5FFD: 06 80           LD      B,$80               
5FFF: EA 20 A7        LD      ($A720),A           
6002: C7              RST     0X00                
6003: 06 80           LD      B,$80               
6005: EA 60 62        LD      ($6260),A           ; {}
6008: C7              RST     0X00                
6009: 06 80           LD      B,$80               
600B: EA 60 74        LD      ($7460),A           ; {}
600E: C7              RST     0X00                
600F: 06 80           LD      B,$80               
6011: EA 60 7B        LD      ($7B60),A           ; {}
6014: C7              RST     0X00                
6015: 06 80           LD      B,$80               
6017: EA 60 A7        LD      ($A760),A           
601A: C7              RST     0X00                
601B: 06 3E           LD      B,$3E               
601D: 04              INC     B                   
601E: EA BE D3        LD      ($D3BE),A           
6021: CD 79 63        CALL    $6379               ; {}
6024: 21 60 60        LD      HL,$6060            
6027: CD B9 7A        CALL    $7AB9               ; {}
602A: C3 F8 62        JP      $62F8               ; {}
602D: CD 71 7A        CALL    $7A71               ; {}
6030: FE 07           CP      $07                 
6032: 28 06           JR      Z,$603A             ; {}
6034: 21 54 60        LD      HL,$6054            
6037: C3 E7 7A        JP      $7AE7               ; {}
603A: CD A2 7A        CALL    $7AA2               ; {}
603D: CA 27 63        JP      Z,$6327             ; {}
6040: FE 02           CP      $02                 
6042: 28 0B           JR      Z,$604F             ; {}
6044: 21 66 60        LD      HL,$6066            
6047: AF              XOR     A                   
6048: 02              LD      (BC),A              
6049: CD B9 7A        CALL    $7AB9               ; {}
604C: C3 81 7A        JP      $7A81               ; {}
604F: 21 60 60        LD      HL,$6060            
6052: 18 F3           JR      $6047               ; {}
6054: 00              NOP                         
6055: 06 00           LD      B,$00               
6057: 04              INC     B                   
6058: 00              NOP                         
6059: 02              LD      (BC),A              
605A: FF              RST     0X38                
605B: F8 FF           LDHL    SP,$FF              
605D: F0 FF           LD      A,($FF)             
605F: E8 80           ADD     SP,$80              
6061: 00              NOP                         
6062: 20 60           JR      NZ,$60C4            ; {}
6064: 87              ADD     A,A                 
6065: 01 80 00        LD      BC,$0080            
6068: 60              LD      H,B                 
6069: 60              LD      H,B                 
606A: 87              ADD     A,A                 
606B: 01 C9 C9        LD      BC,$C9C9            
606E: 3E 07           LD      A,$07               
6070: EA DC D3        LD      ($D3DC),A           
6073: 3E 40           LD      A,$40               
6075: EA BE D3        LD      ($D3BE),A           
6078: CD 60 63        CALL    $6360               ; {}
607B: 21 BE 60        LD      HL,$60BE            
607E: CD B9 7A        CALL    $7AB9               ; {}
6081: C3 F8 62        JP      $62F8               ; {}
6084: CD A2 7A        CALL    $7AA2               ; {}
6087: CA A6 60        JP      Z,$60A6             ; {}
608A: FA DC D3        LD      A,($D3DC)           
608D: FE 07           CP      $07                 
608F: 28 0D           JR      Z,$609E             ; {}
6091: FE 06           CP      $06                 
6093: 28 0D           JR      Z,$60A2             ; {}
6095: 3E 03           LD      A,$03               
6097: 02              LD      (BC),A              
6098: 21 B8 60        LD      HL,$60B8            
609B: C3 E7 7A        JP      $7AE7               ; {}
609E: 3E 01           LD      A,$01               
60A0: 18 F5           JR      $6097               ; {}
60A2: 3E 02           LD      A,$02               
60A4: 18 F1           JR      $6097               ; {}
60A6: D5              PUSH    DE                  
60A7: 11 DC D3        LD      DE,$D3DC            
60AA: CD 6D 7A        CALL    $7A6D               ; {}
60AD: D1              POP     DE                  
60AE: CA 27 63        JP      Z,$6327             ; {}
60B1: 3E 40           LD      A,$40               
60B3: EA BE D3        LD      ($D3BE),A           
60B6: 18 D2           JR      $608A               ; {}
60B8: FF              RST     0X38                
60B9: FF              RST     0X38                
60BA: FF              RST     0X38                
60BB: FE FF           CP      $FF                 
60BD: FB              EI                          
60BE: 80              ADD     A,B                 
60BF: 00              NOP                         
60C0: 20 FF           JR      NZ,$60C1            ; {}
60C2: 87              ADD     A,A                 
60C3: 01 06 C6        LD      BC,$C606            
60C6: 06 C6           LD      B,$C6               
60C8: 06 C6           LD      B,$C6               
60CA: 06 C6           LD      B,$C6               
60CC: 89              ADC     A,C                 
60CD: BD              CP      L                   
60CE: ED                              
60CF: B9              CP      C                   
60D0: 87              ADD     A,A                 
60D1: 53              LD      D,E                 
60D2: 23              INC     HL                  
60D3: 57              LD      D,A                 
60D4: CD 17 7B        CALL    $7B17               ; {}
60D7: 21 C4 60        LD      HL,$60C4            
60DA: CD 5A 63        CALL    $635A               ; {}
60DD: 3E 05           LD      A,$05               
60DF: EA BE D3        LD      ($D3BE),A           
60E2: AF              XOR     A                   
60E3: EA DD D3        LD      ($D3DD),A           
60E6: 21 47 61        LD      HL,$6147            
60E9: CD B9 7A        CALL    $7AB9               ; {}
60EC: C3 F3 62        JP      $62F3               ; {}
60EF: CD A2 7A        CALL    $7AA2               ; {}
60F2: FE 01           CP      $01                 
60F4: 28 1F           JR      Z,$6115             ; {}
60F6: FA DD D3        LD      A,($D3DD)           
60F9: FE 11           CP      $11                 
60FB: 28 10           JR      Z,$610D             ; {}
60FD: FE 0A           CP      $0A                 
60FF: 30 10           JR      NC,$6111            ; {}
6101: 3E 01           LD      A,$01               
6103: 01 96 D3        LD      BC,$D396            
6106: 02              LD      (BC),A              
6107: 21 3D 61        LD      HL,$613D            
610A: C3 E7 7A        JP      $7AE7               ; {}
610D: 3E 05           LD      A,$05               
610F: 18 F2           JR      $6103               ; {}
6111: 3E 03           LD      A,$03               
6113: 18 EE           JR      $6103               ; {}
6115: C5              PUSH    BC                  
6116: 01 DD D3        LD      BC,$D3DD            
6119: CD 71 7A        CALL    $7A71               ; {}
611C: C1              POP     BC                  
611D: FE 12           CP      $12                 
611F: 28 14           JR      Z,$6135             ; {}
6121: C6 05           ADD     $05                 
6123: EA BE D3        LD      ($D3BE),A           
6126: FA DD D3        LD      A,($D3DD)           
6129: FE 0B           CP      $0B                 
612B: 30 04           JR      NC,$6131            ; {}
612D: 3E 02           LD      A,$02               
612F: 18 D2           JR      $6103               ; {}
6131: 3E 04           LD      A,$04               
6133: 18 CE           JR      $6103               ; {}
6135: 3E 59           LD      A,$59               
6137: EA 68 D3        LD      ($D368),A           
613A: C3 27 63        JP      $6327               ; {}
613D: FF              RST     0X38                
613E: F4                              
613F: 00              NOP                         
6140: 32              LD      (HLD),A             
6141: FF              RST     0X38                
6142: F0 00           LD      A,($00)             
6144: 70              LD      (HL),B              
6145: FF              RST     0X38                
6146: E8 80           ADD     SP,$80              
6148: 00              NOP                         
6149: 40              LD      B,B                 
614A: A0              AND     B                   
614B: 87              ADD     A,A                 
614C: 01 CD 60        LD      BC,$60CD            
614F: 63              LD      H,E                 
6150: 3E 03           LD      A,$03               
6152: EA DE D3        LD      ($D3DE),A           
6155: 3E 90           LD      A,$90               
6157: EA BE D3        LD      ($D3BE),A           
615A: 21 9C 61        LD      HL,$619C            
615D: CD B9 7A        CALL    $7AB9               ; {}
6160: C3 F8 62        JP      $62F8               ; {}
6163: CD A2 7A        CALL    $7AA2               ; {}
6166: 28 1C           JR      Z,$6184             ; {}
6168: FA DE D3        LD      A,($D3DE)           
616B: FE 03           CP      $03                 
616D: 28 0D           JR      Z,$617C             ; {}
616F: FE 02           CP      $02                 
6171: 28 0D           JR      Z,$6180             ; {}
6173: 3E 01           LD      A,$01               
6175: 02              LD      (BC),A              
6176: 21 96 61        LD      HL,$6196            
6179: C3 E7 7A        JP      $7AE7               ; {}
617C: 3E 03           LD      A,$03               
617E: 18 F5           JR      $6175               ; {}
6180: 3E 02           LD      A,$02               
6182: 18 F1           JR      $6175               ; {}
6184: D5              PUSH    DE                  
6185: 11 DE D3        LD      DE,$D3DE            
6188: CD 6D 7A        CALL    $7A6D               ; {}
618B: D1              POP     DE                  
618C: CA 27 63        JP      Z,$6327             ; {}
618F: 3E 90           LD      A,$90               
6191: EA BE D3        LD      ($D3BE),A           
6194: 18 D2           JR      $6168               ; {}
6196: 00              NOP                         
6197: 01 00 02        LD      BC,$0200            
619A: 00              NOP                         
619B: 03              INC     BC                  
619C: 80              ADD     A,B                 
619D: 00              NOP                         
619E: 60              LD      H,B                 
619F: 80              ADD     A,B                 
61A0: 84              ADD     A,H                 
61A1: 02              LD      (BC),A              
61A2: 3E 07           LD      A,$07               
61A4: EA BE D3        LD      ($D3BE),A           
61A7: FA 70 D3        LD      A,($D370)           
61AA: EA 71 D3        LD      ($D371),A           
61AD: 3E 01           LD      A,$01               
61AF: EA C8 D3        LD      ($D3C8),A           
61B2: 21 2F D3        LD      HL,$D32F            
61B5: CB FE           SET     1,E                 
61B7: AF              XOR     A                   
61B8: EA 92 D3        LD      ($D392),A           
61BB: EA 96 D3        LD      ($D396),A           
61BE: E0 1A           LDFF00  ($1A),A             
61C0: 21 54 63        LD      HL,$6354            
61C3: CD 81 7A        CALL    $7A81               ; {}
61C6: 21 17 62        LD      HL,$6217            
61C9: CD CC 7A        CALL    $7ACC               ; {}
61CC: C3 7B 7A        JP      $7A7B               ; {}
61CF: CD 71 7A        CALL    $7A71               ; {}
61D2: FE 09           CP      $09                 
61D4: 28 0A           JR      Z,$61E0             ; {}
61D6: FE 0A           CP      $0A                 
61D8: 28 0E           JR      Z,$61E8             ; {}
61DA: 21 05 62        LD      HL,$6205            
61DD: C3 0D 7B        JP      $7B0D               ; {}
61E0: CD A2 7A        CALL    $7AA2               ; {}
61E3: 28 08           JR      Z,$61ED             ; {}
61E5: 0A              LD      A,(BC)              
61E6: 18 F2           JR      $61DA               ; {}
61E8: 3E 01           LD      A,$01               
61EA: 02              LD      (BC),A              
61EB: 18 ED           JR      $61DA               ; {}
61ED: AF              XOR     A                   
61EE: EA 92 D3        LD      ($D392),A           
61F1: EA 96 D3        LD      ($D396),A           
61F4: EA 71 D3        LD      ($D371),A           
61F7: EA C8 D3        LD      ($D3C8),A           
61FA: 21 2F D3        LD      HL,$D32F            
61FD: CB BE           RES     1,E                 
61FF: 21 2F D3        LD      HL,$D32F            
6202: CB BE           RES     1,E                 
6204: C9              RET                         
6205: FF              RST     0X38                
6206: FF              RST     0X38                
6207: FF              RST     0X38                
6208: FE FF           CP      $FF                 
620A: FD                              
620B: FF              RST     0X38                
620C: FC                              
620D: FF              RST     0X38                
620E: FA FF F6        LD      A,($F6FF)           
6211: FF              RST     0X38                
6212: F2                              
6213: FF              RST     0X38                
6214: EE 00           XOR     $00                 
6216: 3A              LD      A,(HLD)             
6217: 00              NOP                         
6218: 97              SUB     A                   
6219: 80              ADD     A,B                 
621A: 87              ADD     A,A                 
621B: 01 3E 2E        LD      BC,$2E3E            
621E: EA BE D3        LD      ($D3BE),A           
6221: AF              XOR     A                   
6222: EA E1 D3        LD      ($D3E1),A           
6225: CD 60 63        CALL    $6360               ; {}
6228: 21 76 62        LD      HL,$6276            
622B: CD B9 7A        CALL    $7AB9               ; {}
622E: C3 F3 62        JP      $62F3               ; {}
6231: CD A2 7A        CALL    $7AA2               ; {}
6234: 28 18           JR      Z,$624E             ; {}
6236: FA E1 D3        LD      A,($D3E1)           
6239: FE 01           CP      $01                 
623B: 28 25           JR      Z,$6262             ; {}
623D: FE 02           CP      $02                 
623F: 28 25           JR      Z,$6266             ; {}
6241: FE 03           CP      $03                 
6243: 28 25           JR      Z,$626A             ; {}
6245: 3E 01           LD      A,$01               
6247: 02              LD      (BC),A              
6248: 21 6E 62        LD      HL,$626E            
624B: C3 E7 7A        JP      $7AE7               ; {}
624E: C5              PUSH    BC                  
624F: 01 E1 D3        LD      BC,$D3E1            
6252: CD 71 7A        CALL    $7A71               ; {}
6255: C1              POP     BC                  
6256: FE 04           CP      $04                 
6258: CA 27 63        JP      Z,$6327             ; {}
625B: 3E 2E           LD      A,$2E               
625D: EA BE D3        LD      ($D3BE),A           
6260: 18 D4           JR      $6236               ; {}
6262: 3E 02           LD      A,$02               
6264: 18 E1           JR      $6247               ; {}
6266: 3E 03           LD      A,$03               
6268: 18 DD           JR      $6247               ; {}
626A: 3E 04           LD      A,$04               
626C: 18 D9           JR      $6247               ; {}
626E: 00              NOP                         
626F: 08 00 06        LD      ($0600),SP          
6272: 00              NOP                         
6273: 04              INC     B                   
6274: 00              NOP                         
6275: 02              LD      (BC),A              
6276: 80              ADD     A,B                 
6277: 00              NOP                         
6278: 40              LD      B,B                 
6279: 30 84           JR      NC,$61FF            ; {}
627B: 01 CD 65        LD      BC,$65CD            
627E: 63              LD      H,E                 
627F: 21 C9 62        LD      HL,$62C9            
6282: C3 F3 62        JP      $62F3               ; {}
6285: CD 6D 7A        CALL    $7A6D               ; {}
6288: C0              RET     NZ                  
6289: CD 71 7A        CALL    $7A71               ; {}
628C: FE 0D           CP      $0D                 
628E: CA 27 63        JP      Z,$6327             ; {}
6291: 21 B1 62        LD      HL,$62B1            
6294: CD 60 7A        CALL    $7A60               ; {}
6297: FA 96 D3        LD      A,($D396)           
629A: FE 01           CP      $01                 
629C: CA 81 7A        JP      Z,$7A81             ; {}
629F: FE 02           CP      $02                 
62A1: CA 81 7A        JP      Z,$7A81             ; {}
62A4: FE 07           CP      $07                 
62A6: CA 81 7A        JP      Z,$7A81             ; {}
62A9: FE 0A           CP      $0A                 
62AB: CA 81 7A        JP      Z,$7A81             ; {}
62AE: C3 7E 63        JP      $637E               ; {}
62B1: CF              RST     0X08                
62B2: 62              LD      H,D                 
62B3: D5              PUSH    DE                  
62B4: 62              LD      H,D                 
62B5: E7              RST     0X20                
62B6: 62              LD      H,D                 
62B7: EA 62 ED        LD      ($ED62),A           
62BA: 62              LD      H,D                 
62BB: F0 62           LD      A,($62)             
62BD: DB                              
62BE: 62              LD      H,D                 
62BF: ED                              
62C0: 62              LD      H,D                 
62C1: F0 62           LD      A,($62)             
62C3: E1              POP     HL                  
62C4: 62              LD      H,D                 
62C5: ED                              
62C6: 62              LD      H,D                 
62C7: F0 62           LD      A,($62)             
62C9: 80              ADD     A,B                 
62CA: F2                              
62CB: 60              LD      H,B                 
62CC: DF              RST     0X18                
62CD: 87              ADD     A,A                 
62CE: 02              LD      (BC),A              
62CF: 80              ADD     A,B                 
62D0: F2                              
62D1: 40              LD      B,B                 
62D2: DF              RST     0X18                
62D3: 87              ADD     A,A                 
62D4: 02              LD      (BC),A              
62D5: 80              ADD     A,B                 
62D6: F2                              
62D7: 20 DF           JR      NZ,$62B8            ; {}
62D9: 87              ADD     A,A                 
62DA: 03              INC     BC                  
62DB: 80              ADD     A,B                 
62DC: F2                              
62DD: 40              LD      B,B                 
62DE: A2              AND     D                   
62DF: 87              ADD     A,A                 
62E0: 03              INC     BC                  
62E1: 80              ADD     A,B                 
62E2: F2                              
62E3: 60              LD      H,B                 
62E4: A2              AND     D                   
62E5: 87              ADD     A,A                 
62E6: 03              INC     BC                  
62E7: BE              CP      (HL)                
62E8: 87              ADD     A,A                 
62E9: 03              INC     BC                  
62EA: A2              AND     D                   
62EB: 87              ADD     A,A                 
62EC: 03              INC     BC                  
62ED: 83              ADD     A,E                 
62EE: 87              ADD     A,A                 
62EF: 03              INC     BC                  
62F0: A7              AND     A                   
62F1: C7              RST     0X00                
62F2: 03              INC     BC                  
62F3: 3E 01           LD      A,$01               
62F5: EA C8 D3        LD      ($D3C8),A           
62F8: FA 70 D3        LD      A,($D370)           
62FB: EA 71 D3        LD      ($D371),A           
62FE: E5              PUSH    HL                  
62FF: 21 3F D3        LD      HL,$D33F            
6302: CB FE           SET     1,E                 
6304: E1              POP     HL                  
6305: AF              XOR     A                   
6306: EA 92 D3        LD      ($D392),A           
6309: EA 96 D3        LD      ($D396),A           
630C: E0 1A           LDFF00  ($1A),A             
630E: C3 81 7A        JP      $7A81               ; {}
6311: 80              ADD     A,B                 
6312: 00              NOP                         
6313: 00              NOP                         
6314: 00              NOP                         
6315: 01 01 00        LD      BC,$0001            
6318: 00              NOP                         
6319: 00              NOP                         
631A: 00              NOP                         
631B: FF              RST     0X38                
631C: FF              RST     0X38                
631D: FF              RST     0X38                
631E: FF              RST     0X38                
631F: 00              NOP                         
6320: 00              NOP                         
6321: 00              NOP                         
6322: 00              NOP                         
6323: FF              RST     0X38                
6324: FF              RST     0X38                
6325: FF              RST     0X38                
6326: FF              RST     0X38                
6327: 21 54 63        LD      HL,$6354            
632A: CD 81 7A        CALL    $7A81               ; {}
632D: AF              XOR     A                   
632E: EA 92 D3        LD      ($D392),A           
6331: EA 96 D3        LD      ($D396),A           
6334: EA 71 D3        LD      ($D371),A           
6337: E0 1A           LDFF00  ($1A),A             
6339: EA C8 D3        LD      ($D3C8),A           
633C: 21 3F D3        LD      HL,$D33F            
633F: CB BE           RES     1,E                 
6341: 3E 01           LD      A,$01               
6343: EA E7 D3        LD      ($D3E7),A           
6346: C9              RET                         
6347: C5              PUSH    BC                  
6348: 0E 30           LD      C,$30               
634A: 2A              LD      A,(HLI)             
634B: E2              LDFF00  (C),A               
634C: 0C              INC     C                   
634D: 79              LD      A,C                 
634E: FE 40           CP      $40                 
6350: 20 F8           JR      NZ,$634A            ; {}
6352: C1              POP     BC                  
6353: C9              RET                         
6354: 80              ADD     A,B                 
6355: 00              NOP                         
6356: 00              NOP                         
6357: 00              NOP                         
6358: 81              ADD     A,C                 
6359: 01 AF E0        LD      BC,$E0AF            
635C: 1A              LD      A,(DE)              
635D: C3 47 63        JP      $6347               ; {}
6360: 21 AC 63        LD      HL,$63AC            
6363: 18 F5           JR      $635A               ; {}
6365: 21 BC 63        LD      HL,$63BC            
6368: 18 F0           JR      $635A               ; {}
636A: 21 9C 63        LD      HL,$639C            
636D: 18 EB           JR      $635A               ; {}
636F: 21 CC 63        LD      HL,$63CC            
6372: 18 E6           JR      $635A               ; {}
6374: 21 DC 63        LD      HL,$63DC            
6377: 18 E1           JR      $635A               ; {}
6379: 21 8C 63        LD      HL,$638C            
637C: 18 DC           JR      $635A               ; {}
637E: 0E 1D           LD      C,$1D               
6380: 06 02           LD      B,$02               
6382: C3 8D 7A        JP      $7A8D               ; {}
6385: AF              XOR     A                   
6386: EA 70 D3        LD      ($D370),A           
6389: C3 ED 53        JP      $53ED               ; {}
638C: 8C              ADC     A,H                 
638D: EF              RST     0X28                
638E: FE C8           CP      $C8                 
6390: 84              ADD     A,H                 
6391: 21 12 48        LD      HL,$4812            
6394: 8C              ADC     A,H                 
6395: EF              RST     0X28                
6396: FE C8           CP      $C8                 
6398: 84              ADD     A,H                 
6399: 21 12 48        LD      HL,$4812            
639C: 00              NOP                         
639D: 22              LD      (HLI),A             
639E: 44              LD      B,H                 
639F: 66              LD      H,(HL)              
63A0: 88              ADC     A,B                 
63A1: AA              XOR     D                   
63A2: CC CC 00        CALL    Z,$00CC             
63A5: 22              LD      (HLI),A             
63A6: 44              LD      B,H                 
63A7: 66              LD      H,(HL)              
63A8: 88              ADC     A,B                 
63A9: AA              XOR     D                   
63AA: CC CC 0F        CALL    Z,$0FCC             
63AD: 0F              RRCA                        
63AE: 1F              RRA                         
63AF: 1F              RRA                         
63B0: 2F              CPL                         
63B1: 2F              CPL                         
63B2: 3F              CCF                         
63B3: 3F              CCF                         
63B4: 40              LD      B,B                 
63B5: 40              LD      B,B                 
63B6: 50              LD      D,B                 
63B7: 50              LD      D,B                 
63B8: 60              LD      H,B                 
63B9: 60              LD      H,B                 
63BA: 70              LD      (HL),B              
63BB: 70              LD      (HL),B              
63BC: 0C              INC     C                   
63BD: 0C              INC     C                   
63BE: 00              NOP                         
63BF: 22              LD      (HLI),A             
63C0: 44              LD      B,H                 
63C1: 88              ADC     A,B                 
63C2: AA              XOR     D                   
63C3: CC EE 00        CALL    Z,$00EE             
63C6: 6C              LD      L,H                 
63C7: 60              LD      H,B                 
63C8: 00              NOP                         
63C9: 6C              LD      L,H                 
63CA: 60              LD      H,B                 
63CB: 00              NOP                         
63CC: FF              RST     0X38                
63CD: FF              RST     0X38                
63CE: EE DD           XOR     $DD                 
63D0: EE DD           XOR     $DD                 
63D2: EE FF           XOR     $FF                 
63D4: FF              RST     0X38                
63D5: C9              RET                         
63D6: 63              LD      H,E                 
63D7: 21 00 00        LD      HL,$0000            
63DA: 04              INC     B                   
63DB: 8C              ADC     A,H                 
63DC: 01 23 45        LD      BC,$4523            
63DF: 67              LD      H,A                 
63E0: 89              ADC     A,C                 
63E1: AC              XOR     H                   
63E2: EE EE           XOR     $EE                 
63E4: FE DC           CP      $DC                 
63E6: BA              CP      D                   
63E7: 98              SBC     B                   
63E8: 76              HALT                        
63E9: 54              LD      D,H                 
63EA: 32              LD      (HLD),A             
63EB: 10 1A           STOP    $1A                 
63ED: 65              LD      H,L                 
63EE: 39              ADD     HL,SP               
63EF: 65              LD      H,L                 
63F0: 83              ADD     A,E                 
63F1: 65              LD      H,L                 
63F2: EB                              
63F3: 65              LD      H,L                 
63F4: 1B              DEC     DE                  
63F5: 66              LD      H,(HL)              
63F6: 69              LD      L,C                 
63F7: 66              LD      H,(HL)              
63F8: 9E              SBC     (HL)                
63F9: 66              LD      H,(HL)              
63FA: DC 66 22        CALL    C,$2266             
63FD: 67              LD      H,A                 
63FE: 5C              LD      E,H                 
63FF: 67              LD      H,A                 
6400: 8E              ADC     A,(HL)              
6401: 67              LD      H,A                 
6402: B0              OR      B                   
6403: 67              LD      H,A                 
6404: F1              POP     AF                  
6405: 67              LD      H,A                 
6406: 2A              LD      A,(HLI)             
6407: 68              LD      L,B                 
6408: 58              LD      E,B                 
6409: 68              LD      L,B                 
640A: 8D              ADC     A,L                 
640B: 68              LD      L,B                 
640C: EC                              
640D: 68              LD      L,B                 
640E: FE 68           CP      $68                 
6410: 3B              DEC     SP                  
6411: 69              LD      L,C                 
6412: C5              PUSH    BC                  
6413: 69              LD      L,C                 
6414: 0B              DEC     BC                  
6415: 6A              LD      L,D                 
6416: 4A              LD      C,D                 
6417: 6A              LD      L,D                 
6418: 7C              LD      A,H                 
6419: 6A              LD      L,D                 
641A: 9E              SBC     (HL)                
641B: 6A              LD      L,D                 
641C: E8 6A           ADD     SP,$6A              
641E: 2E 6B           LD      L,$6B               
6420: 93              SUB     E                   
6421: 6B              LD      L,E                 
6422: 0F              RRCA                        
6423: 6C              LD      L,H                 
6424: 48              LD      C,B                 
6425: 6C              LD      L,H                 
6426: 93              SUB     E                   
6427: 6C              LD      L,H                 
6428: C0              RET     NZ                  
6429: 6C              LD      L,H                 
642A: 07              RLCA                        
642B: 6D              LD      L,L                 
642C: FD                              
642D: 79              LD      A,C                 
642E: 31 6D 6F        LD      SP,$6F6D            
6431: 6D              LD      L,L                 
6432: 91              SUB     C                   
6433: 6D              LD      L,L                 
6434: B3              OR      E                   
6435: 6D              LD      L,L                 
6436: 4A              LD      C,D                 
6437: 6E              LD      L,(HL)              
6438: 83              ADD     A,E                 
6439: 6E              LD      L,(HL)              
643A: D9              RETI                        
643B: 6E              LD      L,(HL)              
643C: 2D              DEC     L                   
643D: 6F              LD      L,A                 
643E: 74              LD      (HL),H              
643F: 6F              LD      L,A                 
6440: D9              RETI                        
6441: 6F              LD      L,A                 
6442: EB                              
6443: 6F              LD      L,A                 
6444: 74              LD      (HL),H              
6445: 70              LD      (HL),B              
6446: C0              RET     NZ                  
6447: 70              LD      (HL),B              
6448: 10 71           STOP    $71                 
644A: 32              LD      (HLD),A             
644B: 71              LD      (HL),C              
644C: C3 71 3A        JP      $3A71               
644F: 72              LD      (HL),D              
6450: 91              SUB     C                   
6451: 72              LD      (HL),D              
6452: E0 72           LDFF00  ($72),A             
6454: 87              ADD     A,A                 
6455: 74              LD      (HL),H              
6456: 8C              ADC     A,H                 
6457: 75              LD      (HL),L              
6458: D6 75           SUB     $75                 
645A: 9D              SBC     L                   
645B: 76              HALT                        
645C: 06 76           LD      B,$76               
645E: 18 77           JR      $64D7               ; {}
6460: 6A              LD      L,D                 
6461: 77              LD      (HL),A              
6462: BC              CP      H                   
6463: 77              LD      (HL),A              
6464: E2              LDFF00  (C),A               
6465: 77              LD      (HL),A              
6466: 01 79 57        LD      BC,$5779            
6469: 79              LD      A,C                 
646A: 25              DEC     H                   
646B: 65              LD      H,L                 
646C: 3F              CCF                         
646D: 65              LD      H,L                 
646E: 89              ADC     A,C                 
646F: 65              LD      H,L                 
6470: F1              POP     AF                  
6471: 65              LD      H,L                 
6472: 38 66           JR      C,$64DA             ; {}
6474: 6F              LD      L,A                 
6475: 66              LD      H,(HL)              
6476: C0              RET     NZ                  
6477: 66              LD      H,(HL)              
6478: EF              RST     0X28                
6479: 66              LD      H,(HL)              
647A: 28 67           JR      Z,$64E3             ; {}
647C: 62              LD      H,D                 
647D: 67              LD      H,A                 
647E: 94              SUB     H                   
647F: 67              LD      H,A                 
6480: C3 67 FC        JP      $FC67               
6483: 67              LD      H,A                 
6484: 30 68           JR      NC,$64EE            ; {}
6486: 65              LD      H,L                 
6487: 68              LD      L,B                 
6488: 98              SBC     B                   
6489: 68              LD      L,B                 
648A: F2                              
648B: 68              LD      L,B                 
648C: 04              INC     B                   
648D: 69              LD      L,C                 
648E: 41              LD      B,C                 
648F: 69              LD      L,C                 
6490: CB 69           BIT     1,E                 
6492: 11 6A 58        LD      DE,$586A            
6495: 6A              LD      L,D                 
6496: 82              ADD     A,D                 
6497: 6A              LD      L,D                 
6498: A4              AND     H                   
6499: 6A              LD      L,D                 
649A: EE 6A           XOR     $6A                 
649C: 34              INC     (HL)                
649D: 6B              LD      L,E                 
649E: AB              XOR     E                   
649F: 6B              LD      L,E                 
64A0: 1A              LD      A,(DE)              
64A1: 6C              LD      L,H                 
64A2: 53              LD      D,E                 
64A3: 6C              LD      L,H                 
64A4: A0              AND     B                   
64A5: 6C              LD      L,H                 
64A6: CB 6C           BIT     1,E                 
64A8: 0D              DEC     C                   
64A9: 6D              LD      L,L                 
64AA: FD                              
64AB: 79              LD      A,C                 
64AC: 37              SCF                         
64AD: 6D              LD      L,L                 
64AE: 75              LD      (HL),L              
64AF: 6D              LD      L,L                 
64B0: 97              SUB     A                   
64B1: 6D              LD      L,L                 
64B2: B9              CP      C                   
64B3: 6D              LD      L,L                 
64B4: 55              LD      D,L                 
64B5: 6E              LD      L,(HL)              
64B6: 89              ADC     A,C                 
64B7: 6E              LD      L,(HL)              
64B8: E4                              
64B9: 6E              LD      L,(HL)              
64BA: 38 6F           JR      C,$652B             ; {}
64BC: 7F              LD      A,A                 
64BD: 6F              LD      L,A                 
64BE: DF              RST     0X18                
64BF: 6F              LD      L,A                 
64C0: F1              POP     AF                  
64C1: 6F              LD      L,A                 
64C2: 7A              LD      A,D                 
64C3: 70              LD      (HL),B              
64C4: CB 70           BIT     1,E                 
64C6: 16 71           LD      D,$71               
64C8: 38 71           JR      C,$653B             ; {}
64CA: C9              RET                         
64CB: 71              LD      (HL),C              
64CC: 40              LD      B,B                 
64CD: 72              LD      (HL),D              
64CE: 97              SUB     A                   
64CF: 72              LD      (HL),D              
64D0: F0 72           LD      A,($72)             
64D2: 92              SUB     D                   
64D3: 74              LD      (HL),H              
64D4: 97              SUB     A                   
64D5: 75              LD      (HL),L              
64D6: E7              RST     0X20                
64D7: 75              LD      (HL),L              
64D8: A3              AND     E                   
64D9: 76              HALT                        
64DA: 0C              INC     C                   
64DB: 76              HALT                        
64DC: 2C              INC     L                   
64DD: 77              LD      (HL),A              
64DE: 8C              ADC     A,H                 
64DF: 77              LD      (HL),A              
64E0: 03              INC     BC                  
64E1: 7A              LD      A,D                 
64E2: E8 77           ADD     SP,$77              
64E4: 07              RLCA                        
64E5: 79              LD      A,C                 
64E6: 5D              LD      E,L                 
64E7: 79              LD      A,C                 
64E8: 21 78 D3        LD      HL,$D378            
64EB: 7E              LD      A,(HL)              
64EC: A7              AND     A                   
64ED: 28 0D           JR      Z,$64FC             ; {}
64EF: FA C9 D3        LD      A,($D3C9)           
64F2: A7              AND     A                   
64F3: C2 28 7A        JP      NZ,$7A28            ; {}
64F6: 7E              LD      A,(HL)              
64F7: 21 EC 63        LD      HL,$63EC            
64FA: 18 08           JR      $6504               ; {}
64FC: 23              INC     HL                  
64FD: 7E              LD      A,(HL)              
64FE: A7              AND     A                   
64FF: 28 0D           JR      Z,$650E             ; {}
6501: 21 6A 64        LD      HL,$646A            
6504: CD 60 7A        CALL    $7A60               ; {}
6507: 11 93 D3        LD      DE,$D393            
650A: 01 98 D3        LD      BC,$D398            
650D: E9              JP      (HL)                
650E: FA 0E C5        LD      A,($C50E)           
6511: A7              AND     A                   
6512: C8              RET     Z                   
6513: 3E 1E           LD      A,$1E               
6515: EA 78 D3        LD      ($D378),A           
6518: 18 CE           JR      $64E8               ; {}
651A: 3E 01           LD      A,$01               
651C: EA 79 D3        LD      ($D379),A           
651F: 21 2F 65        LD      HL,$652F            
6522: C3 87 7A        JP      $7A87               ; {}
6525: AF              XOR     A                   
6526: EA 79 D3        LD      ($D379),A           
6529: 21 34 65        LD      HL,$6534            
652C: C3 87 7A        JP      $7A87               ; {}
652F: 3B              DEC     SP                  
6530: 80              ADD     A,B                 
6531: 07              RLCA                        
6532: C0              RET     NZ                  
6533: 01 00 42        LD      BC,$4200            
6536: 02              LD      (BC),A              
6537: C0              RET     NZ                  
6538: 04              INC     B                   
6539: 21 60 65        LD      HL,$6560            
653C: C3 E5 79        JP      $79E5               ; {}
653F: CD 6D 7A        CALL    $7A6D               ; {}
6542: C0              RET     NZ                  
6543: CD 71 7A        CALL    $7A71               ; {}
6546: FE 07           CP      $07                 
6548: CA 03 7A        JP      Z,$7A03             ; {}
654B: 21 54 65        LD      HL,$6554            
654E: CD 60 7A        CALL    $7A60               ; {}
6551: C3 87 7A        JP      $7A87               ; {}
6554: 65              LD      H,L                 
6555: 65              LD      H,L                 
6556: 6A              LD      L,D                 
6557: 65              LD      H,L                 
6558: 6F              LD      L,A                 
6559: 65              LD      H,L                 
655A: 74              LD      (HL),H              
655B: 65              LD      H,L                 
655C: 79              LD      A,C                 
655D: 65              LD      H,L                 
655E: 7E              LD      A,(HL)              
655F: 65              LD      H,L                 
6560: 00              NOP                         
6561: 40              LD      B,B                 
6562: 21 80 01        LD      HL,$0180            
6565: 00              NOP                         
6566: 50              LD      D,B                 
6567: 22              LD      (HLI),A             
6568: 80              ADD     A,B                 
6569: 01 00 60        LD      BC,$6000            
656C: 23              INC     HL                  
656D: 80              ADD     A,B                 
656E: 01 00 70        LD      BC,$7000            
6571: 24              INC     H                   
6572: 80              ADD     A,B                 
6573: 01 00 80        LD      BC,$8000            
6576: 25              DEC     H                   
6577: 80              ADD     A,B                 
6578: 01 00 90        LD      BC,$9000            
657B: 26 80           LD      H,$80               
657D: 01 3C A0        LD      BC,$A03C            
6580: 27              DAA                         
6581: C0              RET     NZ                  
6582: 01 21 BE        LD      BC,$BE21            
6585: 65              LD      H,L                 
6586: C3 E5 79        JP      $79E5               ; {}
6589: CD 6D 7A        CALL    $7A6D               ; {}
658C: C0              RET     NZ                  
658D: CD 71 7A        CALL    $7A71               ; {}
6590: FE 11           CP      $11                 
6592: CA 03 7A        JP      Z,$7A03             ; {}
6595: 21 9E 65        LD      HL,$659E            
6598: CD 60 7A        CALL    $7A60               ; {}
659B: C3 87 7A        JP      $7A87               ; {}
659E: C3 65 C8        JP      $C865               
65A1: 65              LD      H,L                 
65A2: CD 65 D2        CALL    $D265               
65A5: 65              LD      H,L                 
65A6: D7              RST     0X10                
65A7: 65              LD      H,L                 
65A8: DC 65 E1        CALL    C,$E165             
65AB: 65              LD      H,L                 
65AC: E6 65           AND     $65                 
65AE: E1              POP     HL                  
65AF: 65              LD      H,L                 
65B0: DC 65 D7        CALL    C,$D765             
65B3: 65              LD      H,L                 
65B4: D2 65 CD        JP      NC,$CD65            
65B7: 65              LD      H,L                 
65B8: C8              RET     Z                   
65B9: 65              LD      H,L                 
65BA: C3 65 BE        JP      $BE65               
65BD: 65              LD      H,L                 
65BE: 37              SCF                         
65BF: 10 04           STOP    $04                 
65C1: C0              RET     NZ                  
65C2: 02              LD      (BC),A              
65C3: 00              NOP                         
65C4: 20 06           JR      NZ,$65CC            ; {}
65C6: 80              ADD     A,B                 
65C7: 02              LD      (BC),A              
65C8: 00              NOP                         
65C9: 30 14           JR      NC,$65DF            ; {}
65CB: 80              ADD     A,B                 
65CC: 02              LD      (BC),A              
65CD: 00              NOP                         
65CE: 40              LD      B,B                 
65CF: 16 80           LD      D,$80               
65D1: 02              LD      (BC),A              
65D2: 00              NOP                         
65D3: 50              LD      D,B                 
65D4: 24              INC     H                   
65D5: 80              ADD     A,B                 
65D6: 02              LD      (BC),A              
65D7: 00              NOP                         
65D8: 60              LD      H,B                 
65D9: 26 80           LD      H,$80               
65DB: 02              LD      (BC),A              
65DC: 00              NOP                         
65DD: 70              LD      (HL),B              
65DE: 34              INC     (HL)                
65DF: 80              ADD     A,B                 
65E0: 02              LD      (BC),A              
65E1: 00              NOP                         
65E2: 80              ADD     A,B                 
65E3: 36 80           LD      (HL),$80            
65E5: 02              LD      (BC),A              
65E6: 00              NOP                         
65E7: 90              SUB     B                   
65E8: 44              LD      B,H                 
65E9: 80              ADD     A,B                 
65EA: 02              LD      (BC),A              
65EB: 21 0C 66        LD      HL,$660C            
65EE: C3 E5 79        JP      $79E5               ; {}
65F1: CD 6D 7A        CALL    $7A6D               ; {}
65F4: C0              RET     NZ                  
65F5: CD 71 7A        CALL    $7A71               ; {}
65F8: FE 04           CP      $04                 
65FA: CA 03 7A        JP      Z,$7A03             ; {}
65FD: 21 06 66        LD      HL,$6606            
6600: CD 60 7A        CALL    $7A60               ; {}
6603: C3 87 7A        JP      $7A87               ; {}
6606: 11 66 0C        LD      DE,$0C66            
6609: 66              LD      H,(HL)              
660A: 16 66           LD      D,$66               
660C: 3B              DEC     SP                  
660D: C0              RET     NZ                  
660E: 3E C0           LD      A,$C0               
6610: 01 33 F0        LD      BC,$F033            
6613: 6E              LD      L,(HL)              
6614: C0              RET     NZ                  
6615: 06 36           LD      B,$36               
6617: 70              LD      (HL),B              
6618: 4E              LD      C,(HL)              
6619: C0              RET     NZ                  
661A: 03              INC     BC                  
661B: FA 79 D3        LD      A,($D379)           
661E: FE 02           CP      $02                 
6620: CA 28 7A        JP      Z,$7A28             ; {}
6623: FE 03           CP      $03                 
6625: CA 28 7A        JP      Z,$7A28             ; {}
6628: FE 0C           CP      $0C                 
662A: CA 28 7A        JP      Z,$7A28             ; {}
662D: FE 13           CP      $13                 
662F: CA 28 7A        JP      Z,$7A28             ; {}
6632: 21 55 66        LD      HL,$6655            
6635: C3 E5 79        JP      $79E5               ; {}
6638: CD 6D 7A        CALL    $7A6D               ; {}
663B: C0              RET     NZ                  
663C: CD 71 7A        CALL    $7A71               ; {}
663F: FE 05           CP      $05                 
6641: CA 03 7A        JP      Z,$7A03             ; {}
6644: 21 4D 66        LD      HL,$664D            
6647: CD 60 7A        CALL    $7A60               ; {}
664A: C3 87 7A        JP      $7A87               ; {}
664D: 5A              LD      E,D                 
664E: 66              LD      H,(HL)              
664F: 5F              LD      E,A                 
6650: 66              LD      H,(HL)              
6651: 64              LD      H,H                 
6652: 66              LD      H,(HL)              
6653: 64              LD      H,H                 
6654: 66              LD      H,(HL)              
6655: 30 49           JR      NC,$66A0            ; {}
6657: 60              LD      H,B                 
6658: C0              RET     NZ                  
6659: 06 30           LD      B,$30               
665B: 49              LD      C,C                 
665C: 40              LD      B,B                 
665D: C0              RET     NZ                  
665E: 06 30           LD      B,$30               
6660: 49              LD      C,C                 
6661: 20 C0           JR      NZ,$6623            ; {}
6663: 06 30           LD      B,$30               
6665: 49              LD      C,C                 
6666: 00              NOP                         
6667: C0              RET     NZ                  
6668: 06 21           LD      B,$21               
666A: 8A              ADC     A,D                 
666B: 66              LD      H,(HL)              
666C: C3 E5 79        JP      $79E5               ; {}
666F: CD 6D 7A        CALL    $7A6D               ; {}
6672: C0              RET     NZ                  
6673: CD 71 7A        CALL    $7A71               ; {}
6676: FE 04           CP      $04                 
6678: CA 03 7A        JP      Z,$7A03             ; {}
667B: 21 84 66        LD      HL,$6684            
667E: CD 60 7A        CALL    $7A60               ; {}
6681: C3 87 7A        JP      $7A87               ; {}
6684: 8F              ADC     A,A                 
6685: 66              LD      H,(HL)              
6686: 94              SUB     H                   
6687: 66              LD      H,(HL)              
6688: 99              SBC     C                   
6689: 66              LD      H,(HL)              
668A: 00              NOP                         
668B: 61              LD      H,C                 
668C: 24              INC     H                   
668D: 80              ADD     A,B                 
668E: 0C              INC     C                   
668F: 00              NOP                         
6690: 51              LD      D,C                 
6691: 25              DEC     H                   
6692: 80              ADD     A,B                 
6693: 0C              INC     C                   
6694: 00              NOP                         
6695: 32              LD      (HLD),A             
6696: 27              DAA                         
6697: 80              ADD     A,B                 
6698: 0C              INC     C                   
6699: 00              NOP                         
669A: 22              LD      (HLI),A             
669B: 34              INC     (HL)                
669C: 80              ADD     A,B                 
669D: 0C              INC     C                   
669E: FA 79 D3        LD      A,($D379)           
66A1: FE 05           CP      $05                 
66A3: CA 28 7A        JP      Z,$7A28             ; {}
66A6: FE 08           CP      $08                 
66A8: CA 28 7A        JP      Z,$7A28             ; {}
66AB: FE 0C           CP      $0C                 
66AD: CA 28 7A        JP      Z,$7A28             ; {}
66B0: FE 10           CP      $10                 
66B2: CA 28 7A        JP      Z,$7A28             ; {}
66B5: FE 13           CP      $13                 
66B7: CA 28 7A        JP      Z,$7A28             ; {}
66BA: 21 D2 66        LD      HL,$66D2            
66BD: C3 E5 79        JP      $79E5               ; {}
66C0: CD 6D 7A        CALL    $7A6D               ; {}
66C3: C0              RET     NZ                  
66C4: CD 71 7A        CALL    $7A71               ; {}
66C7: FE 02           CP      $02                 
66C9: CA 03 7A        JP      Z,$7A03             ; {}
66CC: 21 D7 66        LD      HL,$66D7            
66CF: C3 87 7A        JP      $7A87               ; {}
66D2: 3B              DEC     SP                  
66D3: F0 20           LD      A,($20)             
66D5: C0              RET     NZ                  
66D6: 02              LD      (BC),A              
66D7: 39              ADD     HL,SP               
66D8: 40              LD      B,B                 
66D9: 20 C0           JR      NZ,$669B            ; {}
66DB: 08 FA 79        LD      ($79FA),SP          ; {}
66DE: D3                              
66DF: FE 0C           CP      $0C                 
66E1: CA 28 7A        JP      Z,$7A28             ; {}
66E4: 3E 03           LD      A,$03               
66E6: EA BF D3        LD      ($D3BF),A           
66E9: 21 14 67        LD      HL,$6714            
66EC: C3 E5 79        JP      $79E5               ; {}
66EF: CD 6D 7A        CALL    $7A6D               ; {}
66F2: C0              RET     NZ                  
66F3: CD 71 7A        CALL    $7A71               ; {}
66F6: FE 04           CP      $04                 
66F8: 28 09           JR      Z,$6703             ; {}
66FA: 21 0E 67        LD      HL,$670E            
66FD: CD 60 7A        CALL    $7A60               ; {}
6700: C3 21 7A        JP      $7A21               ; {}
6703: CD A8 7A        CALL    $7AA8               ; {}
6706: CA 03 7A        JP      Z,$7A03             ; {}
6709: 3E 01           LD      A,$01               
670B: 02              LD      (BC),A              
670C: 18 EC           JR      $66FA               ; {}
670E: 19              ADD     HL,DE               
670F: 67              LD      H,A                 
6710: 1C              INC     E                   
6711: 67              LD      H,A                 
6712: 1F              RRA                         
6713: 67              LD      H,A                 
6714: 00              NOP                         
6715: A3              AND     E                   
6716: 3C              INC     A                   
6717: 80              ADD     A,B                 
6718: 03              INC     BC                  
6719: 3D              DEC     A                   
671A: 00              NOP                         
671B: 03              INC     BC                  
671C: 3E 00           LD      A,$00               
671E: 03              INC     BC                  
671F: 3F              CCF                         
6720: 00              NOP                         
6721: 03              INC     BC                  
6722: 21 4B 67        LD      HL,$674B            
6725: C3 E5 79        JP      $79E5               ; {}
6728: CD 6D 7A        CALL    $7A6D               ; {}
672B: C0              RET     NZ                  
672C: 3E 33           LD      A,$33               
672E: E0 20           LDFF00  ($20),A             
6730: CD 71 7A        CALL    $7A71               ; {}
6733: FE 06           CP      $06                 
6735: CA 03 7A        JP      Z,$7A03             ; {}
6738: 21 41 67        LD      HL,$6741            
673B: CD 60 7A        CALL    $7A60               ; {}
673E: C3 21 7A        JP      $7A21               ; {}
6741: 50              LD      D,B                 
6742: 67              LD      H,A                 
6743: 53              LD      D,E                 
6744: 67              LD      H,A                 
6745: 56              LD      D,(HL)              
6746: 67              LD      H,A                 
6747: 59              LD      E,C                 
6748: 67              LD      H,A                 
6749: 59              LD      E,C                 
674A: 67              LD      H,A                 
674B: 33              INC     SP                  
674C: A0              AND     B                   
674D: 72              LD      (HL),D              
674E: C0              RET     NZ                  
674F: 04              INC     B                   
6750: 52              LD      D,D                 
6751: C0              RET     NZ                  
6752: 04              INC     B                   
6753: 50              LD      D,B                 
6754: C0              RET     NZ                  
6755: 04              INC     B                   
6756: 30 C0           JR      NC,$6718            ; {}
6758: 04              INC     B                   
6759: 10 C0           STOP    $C0                 
675B: 04              INC     B                   
675C: 21 7F 67        LD      HL,$677F            
675F: C3 E5 79        JP      $79E5               ; {}
6762: CD 6D 7A        CALL    $7A6D               ; {}
6765: C0              RET     NZ                  
6766: CD 71 7A        CALL    $7A71               ; {}
6769: FE 05           CP      $05                 
676B: CA 03 7A        JP      Z,$7A03             ; {}
676E: 21 77 67        LD      HL,$6777            
6771: CD 60 7A        CALL    $7A60               ; {}
6774: C3 87 7A        JP      $7A87               ; {}
6777: 84              ADD     A,H                 
6778: 67              LD      H,A                 
6779: 89              ADC     A,C                 
677A: 67              LD      H,A                 
677B: 84              ADD     A,H                 
677C: 67              LD      H,A                 
677D: 7F              LD      A,A                 
677E: 67              LD      H,A                 
677F: 37              SCF                         
6780: 40              LD      B,B                 
6781: 47              LD      B,A                 
6782: C0              RET     NZ                  
6783: 01 00 60        LD      BC,$6000            
6786: 27              DAA                         
6787: 80              ADD     A,B                 
6788: 02              LD      (BC),A              
6789: 00              NOP                         
678A: A0              AND     B                   
678B: 15              DEC     D                   
678C: 80              ADD     A,B                 
678D: 02              LD      (BC),A              
678E: 21 A6 67        LD      HL,$67A6            
6791: C3 E5 79        JP      $79E5               ; {}
6794: CD 6D 7A        CALL    $7A6D               ; {}
6797: C0              RET     NZ                  
6798: CD 71 7A        CALL    $7A71               ; {}
679B: FE 02           CP      $02                 
679D: CA 03 7A        JP      Z,$7A03             ; {}
67A0: 21 AB 67        LD      HL,$67AB            
67A3: C3 87 7A        JP      $7A87               ; {}
67A6: 3C              INC     A                   
67A7: C0              RET     NZ                  
67A8: 18 C0           JR      $676A               ; {}
67AA: 01 3C 60        LD      BC,$603C            
67AD: 18 C0           JR      $676F               ; {}
67AF: 02              LD      (BC),A              
67B0: FA 79 D3        LD      A,($D379)           
67B3: FE 02           CP      $02                 
67B5: CA 28 7A        JP      Z,$7A28             ; {}
67B8: FE 03           CP      $03                 
67BA: CA 28 7A        JP      Z,$7A28             ; {}
67BD: 21 E0 67        LD      HL,$67E0            
67C0: C3 E5 79        JP      $79E5               ; {}
67C3: CD 6D 7A        CALL    $7A6D               ; {}
67C6: C0              RET     NZ                  
67C7: CD 71 7A        CALL    $7A71               ; {}
67CA: FE 05           CP      $05                 
67CC: CA 03 7A        JP      Z,$7A03             ; {}
67CF: 21 D8 67        LD      HL,$67D8            
67D2: CD 60 7A        CALL    $7A60               ; {}
67D5: C3 21 7A        JP      $7A21               ; {}
67D8: E5              PUSH    HL                  
67D9: 67              LD      H,A                 
67DA: E8 67           ADD     SP,$67              
67DC: EB                              
67DD: 67              LD      H,A                 
67DE: EE 67           XOR     $67                 
67E0: 00              NOP                         
67E1: C6 6A           ADD     $6A                 
67E3: 80              ADD     A,B                 
67E4: 04              INC     B                   
67E5: 6B              LD      L,E                 
67E6: 00              NOP                         
67E7: 05              DEC     B                   
67E8: 6C              LD      L,H                 
67E9: 00              NOP                         
67EA: 06 6D           LD      B,$6D               
67EC: 00              NOP                         
67ED: 07              RLCA                        
67EE: 6E              LD      L,(HL)              
67EF: 00              NOP                         
67F0: 38 3E           JR      C,$6830             ; {}
67F2: 0E EA           LD      C,$EA               
67F4: BF              CP      A                   
67F5: D3                              
67F6: 21 1F 68        LD      HL,$681F            
67F9: C3 E5 79        JP      $79E5               ; {}
67FC: CD 6D 7A        CALL    $7A6D               ; {}
67FF: C0              RET     NZ                  
6800: CD 71 7A        CALL    $7A71               ; {}
6803: FE 03           CP      $03                 
6805: 28 09           JR      Z,$6810             ; {}
6807: 21 1B 68        LD      HL,$681B            
680A: CD 60 7A        CALL    $7A60               ; {}
680D: C3 21 7A        JP      $7A21               ; {}
6810: CD A8 7A        CALL    $7AA8               ; {}
6813: CA FD 79        JP      Z,$79FD             ; {}
6816: 3E 01           LD      A,$01               
6818: 02              LD      (BC),A              
6819: 18 EC           JR      $6807               ; {}
681B: 24              INC     H                   
681C: 68              LD      L,B                 
681D: 27              DAA                         
681E: 68              LD      L,B                 
681F: 00              NOP                         
6820: 67              LD      H,A                 
6821: 0F              RRCA                        
6822: 80              ADD     A,B                 
6823: 02              LD      (BC),A              
6824: 60              LD      H,B                 
6825: 00              NOP                         
6826: 02              LD      (BC),A              
6827: 0F              RRCA                        
6828: 00              NOP                         
6829: 02              LD      (BC),A              
682A: 21 49 68        LD      HL,$6849            
682D: C3 E5 79        JP      $79E5               ; {}
6830: CD 6D 7A        CALL    $7A6D               ; {}
6833: C0              RET     NZ                  
6834: CD 71 7A        CALL    $7A71               ; {}
6837: FE 03           CP      $03                 
6839: CA 03 7A        JP      Z,$7A03             ; {}
683C: 21 45 68        LD      HL,$6845            
683F: CD 60 7A        CALL    $7A60               ; {}
6842: C3 87 7A        JP      $7A87               ; {}
6845: 4E              LD      C,(HL)              
6846: 68              LD      L,B                 
6847: 53              LD      D,E                 
6848: 68              LD      L,B                 
6849: 1E 29           LD      E,$29               
684B: 46              LD      B,(HL)              
684C: C0              RET     NZ                  
684D: 10 00           STOP    $00                 
684F: 29              ADD     HL,HL               
6850: 64              LD      H,H                 
6851: 80              ADD     A,B                 
6852: 08 00 81        LD      ($8100),SP          
6855: 64              LD      H,H                 
6856: 80              ADD     A,B                 
6857: 06 FA           LD      B,$FA               
6859: 79              LD      A,C                 
685A: D3                              
685B: A7              AND     A                   
685C: C2 28 7A        JP      NZ,$7A28            ; {}
685F: 21 7E 68        LD      HL,$687E            
6862: C3 E5 79        JP      $79E5               ; {}
6865: CD 6D 7A        CALL    $7A6D               ; {}
6868: C0              RET     NZ                  
6869: CD 71 7A        CALL    $7A71               ; {}
686C: FE 03           CP      $03                 
686E: CA 03 7A        JP      Z,$7A03             ; {}
6871: 21 7A 68        LD      HL,$687A            
6874: CD 60 7A        CALL    $7A60               ; {}
6877: C3 87 7A        JP      $7A87               ; {}
687A: 83              ADD     A,E                 
687B: 68              LD      L,B                 
687C: 88              ADC     A,B                 
687D: 68              LD      L,B                 
687E: 00              NOP                         
687F: 0F              RRCA                        
6880: 30 80           JR      NC,$6802            ; {}
6882: 20 00           JR      NZ,$6884            ; {}
6884: 60              LD      H,B                 
6885: 03              INC     BC                  
6886: 80              ADD     A,B                 
6887: 30 00           JR      NC,$6889            ; {}
6889: 67              LD      H,A                 
688A: 03              INC     BC                  
688B: 80              ADD     A,B                 
688C: 20 3E           JR      NZ,$68CC            ; {}
688E: 03              INC     BC                  
688F: EA BF D3        LD      ($D3BF),A           
6892: 21 CE 68        LD      HL,$68CE            
6895: C3 E5 79        JP      $79E5               ; {}
6898: CD 6D 7A        CALL    $7A6D               ; {}
689B: C0              RET     NZ                  
689C: CD 71 7A        CALL    $7A71               ; {}
689F: FE 06           CP      $06                 
68A1: 28 09           JR      Z,$68AC             ; {}
68A3: 21 C4 68        LD      HL,$68C4            
68A6: CD 60 7A        CALL    $7A60               ; {}
68A9: C3 21 7A        JP      $7A21               ; {}
68AC: CD A8 7A        CALL    $7AA8               ; {}
68AF: CA FD 79        JP      Z,$79FD             ; {}
68B2: FE 01           CP      $01                 
68B4: 28 09           JR      Z,$68BF             ; {}
68B6: 21 E2 68        LD      HL,$68E2            
68B9: 3E 01           LD      A,$01               
68BB: 02              LD      (BC),A              
68BC: C3 87 7A        JP      $7A87               ; {}
68BF: 21 E7 68        LD      HL,$68E7            
68C2: 18 F5           JR      $68B9               ; {}
68C4: D3                              
68C5: 68              LD      L,B                 
68C6: D6 68           SUB     $68                 
68C8: D9              RETI                        
68C9: 68              LD      L,B                 
68CA: DC 68 DF        CALL    C,$DF68             
68CD: 68              LD      L,B                 
68CE: 00              NOP                         
68CF: E0 48           LDFF00  ($48),A             
68D1: 80              ADD     A,B                 
68D2: 01 4B 00        LD      BC,$004B            
68D5: 01 5E 00        LD      BC,$005E            
68D8: 01 5D 00        LD      BC,$005D            
68DB: 02              LD      (BC),A              
68DC: 6C              LD      L,H                 
68DD: 00              NOP                         
68DE: 02              LD      (BC),A              
68DF: 6F              LD      L,A                 
68E0: 00              NOP                         
68E1: 02              LD      (BC),A              
68E2: 00              NOP                         
68E3: 70              LD      (HL),B              
68E4: 4B              LD      C,E                 
68E5: 80              ADD     A,B                 
68E6: 01 00 20        LD      BC,$2000            
68E9: 4B              LD      C,E                 
68EA: 80              ADD     A,B                 
68EB: 01 21 F9        LD      BC,$F921            
68EE: 68              LD      L,B                 
68EF: C3 E5 79        JP      $79E5               ; {}
68F2: CD 6D 7A        CALL    $7A6D               ; {}
68F5: C0              RET     NZ                  
68F6: C3 FD 79        JP      $79FD               ; {}
68F9: 00              NOP                         
68FA: F0 A0           LD      A,($A0)             
68FC: 80              ADD     A,B                 
68FD: 20 21           JR      NZ,$6920            ; {}
68FF: 27              DAA                         
6900: 69              LD      L,C                 
6901: C3 E5 79        JP      $79E5               ; {}
6904: CD 6D 7A        CALL    $7A6D               ; {}
6907: C0              RET     NZ                  
6908: CD 71 7A        CALL    $7A71               ; {}
690B: FE 08           CP      $08                 
690D: CA FD 79        JP      Z,$79FD             ; {}
6910: 21 19 69        LD      HL,$6919            
6913: CD 60 7A        CALL    $7A60               ; {}
6916: C3 21 7A        JP      $7A21               ; {}
6919: 2C              INC     L                   
691A: 69              LD      L,C                 
691B: 2F              CPL                         
691C: 69              LD      L,C                 
691D: 32              LD      (HLD),A             
691E: 69              LD      L,C                 
691F: 2F              CPL                         
6920: 69              LD      L,C                 
6921: 2C              INC     L                   
6922: 69              LD      L,C                 
6923: 35              DEC     (HL)                
6924: 69              LD      L,C                 
6925: 38 69           JR      C,$6990             ; {}
6927: 00              NOP                         
6928: 69              LD      L,C                 
6929: B8              CP      B                   
692A: 80              ADD     A,B                 
692B: 02              LD      (BC),A              
692C: A8              XOR     B                   
692D: 00              NOP                         
692E: 02              LD      (BC),A              
692F: 98              SBC     B                   
6930: 00              NOP                         
6931: 02              LD      (BC),A              
6932: 88              ADC     A,B                 
6933: 00              NOP                         
6934: 02              LD      (BC),A              
6935: B8              CP      B                   
6936: 00              NOP                         
6937: 02              LD      (BC),A              
6938: C8              RET     Z                   
6939: 00              NOP                         
693A: 02              LD      (BC),A              
693B: 21 98 69        LD      HL,$6998            
693E: C3 E5 79        JP      $79E5               ; {}
6941: CD 6D 7A        CALL    $7A6D               ; {}
6944: C0              RET     NZ                  
6945: CD 71 7A        CALL    $7A71               ; {}
6948: FE 1A           CP      $1A                 
694A: CA 03 7A        JP      Z,$7A03             ; {}
694D: 21 66 69        LD      HL,$6966            
6950: CD 60 7A        CALL    $7A60               ; {}
6953: FA 98 D3        LD      A,($D398)           
6956: FE 11           CP      $11                 
6958: 30 03           JR      NC,$695D            ; {}
695A: C3 87 7A        JP      $7A87               ; {}
695D: 23              INC     HL                  
695E: 23              INC     HL                  
695F: 3E 20           LD      A,$20               
6961: E0 21           LDFF00  ($21),A             
6963: C3 21 7A        JP      $7A21               ; {}
6966: 9D              SBC     L                   
6967: 69              LD      L,C                 
6968: A2              AND     D                   
6969: 69              LD      L,C                 
696A: A7              AND     A                   
696B: 69              LD      L,C                 
696C: AC              XOR     H                   
696D: 69              LD      L,C                 
696E: B1              OR      C                   
696F: 69              LD      L,C                 
6970: B6              OR      (HL)                
6971: 69              LD      L,C                 
6972: BB              CP      E                   
6973: 69              LD      L,C                 
6974: C0              RET     NZ                  
6975: 69              LD      L,C                 
6976: BB              CP      E                   
6977: 69              LD      L,C                 
6978: B6              OR      (HL)                
6979: 69              LD      L,C                 
697A: B1              OR      C                   
697B: 69              LD      L,C                 
697C: AC              XOR     H                   
697D: 69              LD      L,C                 
697E: A7              AND     A                   
697F: 69              LD      L,C                 
6980: A2              AND     D                   
6981: 69              LD      L,C                 
6982: 9D              SBC     L                   
6983: 69              LD      L,C                 
6984: 98              SBC     B                   
6985: 69              LD      L,C                 
6986: C0              RET     NZ                  
6987: 69              LD      L,C                 
6988: BB              CP      E                   
6989: 69              LD      L,C                 
698A: B6              OR      (HL)                
698B: 69              LD      L,C                 
698C: B1              OR      C                   
698D: 69              LD      L,C                 
698E: AC              XOR     H                   
698F: 69              LD      L,C                 
6990: A7              AND     A                   
6991: 69              LD      L,C                 
6992: A2              AND     D                   
6993: 69              LD      L,C                 
6994: 9D              SBC     L                   
6995: 69              LD      L,C                 
6996: 98              SBC     B                   
6997: 69              LD      L,C                 
6998: 37              SCF                         
6999: 20 25           JR      NZ,$69C0            ; {}
699B: C0              RET     NZ                  
699C: 01 00 40        LD      BC,$4000            
699F: 27              DAA                         
69A0: 80              ADD     A,B                 
69A1: 01 00 60        LD      BC,$6000            
69A4: 35              DEC     (HL)                
69A5: 80              ADD     A,B                 
69A6: 01 00 80        LD      BC,$8000            
69A9: 37              SCF                         
69AA: 80              ADD     A,B                 
69AB: 01 00 A0        LD      BC,$A000            
69AE: 4D              LD      C,L                 
69AF: 80              ADD     A,B                 
69B0: 02              LD      (BC),A              
69B1: 00              NOP                         
69B2: B0              OR      B                   
69B3: 4F              LD      C,A                 
69B4: 80              ADD     A,B                 
69B5: 02              LD      (BC),A              
69B6: 00              NOP                         
69B7: C0              RET     NZ                  
69B8: 5D              LD      E,L                 
69B9: 80              ADD     A,B                 
69BA: 02              LD      (BC),A              
69BB: 00              NOP                         
69BC: D0              RET     NC                  
69BD: 5F              LD      E,A                 
69BE: 80              ADD     A,B                 
69BF: 02              LD      (BC),A              
69C0: 00              NOP                         
69C1: E0 6D           LDFF00  ($6D),A             
69C3: 80              ADD     A,B                 
69C4: 02              LD      (BC),A              
69C5: 21 E8 69        LD      HL,$69E8            
69C8: C3 E5 79        JP      $79E5               ; {}
69CB: CD 71 7A        CALL    $7A71               ; {}
69CE: FE 07           CP      $07                 
69D0: CA 03 7A        JP      Z,$7A03             ; {}
69D3: 21 DC 69        LD      HL,$69DC            
69D6: CD 60 7A        CALL    $7A60               ; {}
69D9: C3 87 7A        JP      $7A87               ; {}
69DC: ED                              
69DD: 69              LD      L,C                 
69DE: F2                              
69DF: 69              LD      L,C                 
69E0: F7              RST     0X30                
69E1: 69              LD      L,C                 
69E2: FC                              
69E3: 69              LD      L,C                 
69E4: 01 6A 06        LD      BC,$066A            
69E7: 6A              LD      L,D                 
69E8: 00              NOP                         
69E9: 40              LD      B,B                 
69EA: 5F              LD      E,A                 
69EB: 80              ADD     A,B                 
69EC: 01 00 50        LD      BC,$5000            
69EF: 5D              LD      E,L                 
69F0: 80              ADD     A,B                 
69F1: 01 00 60        LD      BC,$6000            
69F4: 4F              LD      C,A                 
69F5: 80              ADD     A,B                 
69F6: 01 00 70        LD      BC,$7000            
69F9: 4D              LD      C,L                 
69FA: 80              ADD     A,B                 
69FB: 01 00 80        LD      BC,$8000            
69FE: 3F              CCF                         
69FF: 80              ADD     A,B                 
6A00: 01 00 90        LD      BC,$9000            
6A03: 3C              INC     A                   
6A04: 80              ADD     A,B                 
6A05: 01 3C A0        LD      BC,$A03C            
6A08: 2E C0           LD      L,$C0               
6A0A: 01 21 2C        LD      BC,$2C21            
6A0D: 6A              LD      L,D                 
6A0E: C3 E5 79        JP      $79E5               ; {}
6A11: CD 71 7A        CALL    $7A71               ; {}
6A14: FE 06           CP      $06                 
6A16: CA 03 7A        JP      Z,$7A03             ; {}
6A19: 21 22 6A        LD      HL,$6A22            
6A1C: CD 60 7A        CALL    $7A60               ; {}
6A1F: C3 87 7A        JP      $7A87               ; {}
6A22: 31 6A 36        LD      SP,$366A            
6A25: 6A              LD      L,D                 
6A26: 3B              DEC     SP                  
6A27: 6A              LD      L,D                 
6A28: 40              LD      B,B                 
6A29: 6A              LD      L,D                 
6A2A: 45              LD      B,L                 
6A2B: 6A              LD      L,D                 
6A2C: 00              NOP                         
6A2D: 20 47           JR      NZ,$6A76            ; {}
6A2F: 80              ADD     A,B                 
6A30: 02              LD      (BC),A              
6A31: 00              NOP                         
6A32: 40              LD      B,B                 
6A33: 37              SCF                         
6A34: 80              ADD     A,B                 
6A35: 01 00 60        LD      BC,$6000            
6A38: 27              DAA                         
6A39: 80              ADD     A,B                 
6A3A: 01 00 80        LD      BC,$8000            
6A3D: 17              RLA                         
6A3E: 80              ADD     A,B                 
6A3F: 01 00 A0        LD      BC,$A000            
6A42: 07              RLCA                        
6A43: 80              ADD     A,B                 
6A44: 01 3C C0        LD      BC,$C03C            
6A47: 03              INC     BC                  
6A48: C0              RET     NZ                  
6A49: 01 FA 79        LD      BC,$79FA            
6A4C: D3                              
6A4D: FE 03           CP      $03                 
6A4F: CA 28 7A        JP      Z,$7A28             ; {}
6A52: 21 6D 6A        LD      HL,$6A6D            
6A55: C3 E5 79        JP      $79E5               ; {}
6A58: CD 71 7A        CALL    $7A71               ; {}
6A5B: FE 03           CP      $03                 
6A5D: CA 03 7A        JP      Z,$7A03             ; {}
6A60: 21 69 6A        LD      HL,$6A69            
6A63: CD 60 7A        CALL    $7A60               ; {}
6A66: C3 87 7A        JP      $7A87               ; {}
6A69: 72              LD      (HL),D              
6A6A: 6A              LD      L,D                 
6A6B: 77              LD      (HL),A              
6A6C: 6A              LD      L,D                 
6A6D: 00              NOP                         
6A6E: 29              ADD     HL,HL               
6A6F: 68              LD      L,B                 
6A70: 80              ADD     A,B                 
6A71: 10 3C           STOP    $3C                 
6A73: C0              RET     NZ                  
6A74: 50              LD      D,B                 
6A75: C0              RET     NZ                  
6A76: 01 3C C1        LD      BC,$C13C            
6A79: 18 C0           JR      $6A3B               ; {}
6A7B: 01 21 94        LD      BC,$9421            
6A7E: 6A              LD      L,D                 
6A7F: C3 E5 79        JP      $79E5               ; {}
6A82: CD 6D 7A        CALL    $7A6D               ; {}
6A85: C0              RET     NZ                  
6A86: CD 71 7A        CALL    $7A71               ; {}
6A89: FE 02           CP      $02                 
6A8B: CA 03 7A        JP      Z,$7A03             ; {}
6A8E: 21 99 6A        LD      HL,$6A99            
6A91: C3 87 7A        JP      $7A87               ; {}
6A94: 00              NOP                         
6A95: F1              POP     AF                  
6A96: 09              ADD     HL,BC               
6A97: 80              ADD     A,B                 
6A98: 0E 00           LD      C,$00               
6A9A: 62              LD      H,D                 
6A9B: 09              ADD     HL,BC               
6A9C: 80              ADD     A,B                 
6A9D: 10 21           STOP    $21                 
6A9F: C5              PUSH    BC                  
6AA0: 6A              LD      L,D                 
6AA1: C3 E5 79        JP      $79E5               ; {}
6AA4: CD 6D 7A        CALL    $7A6D               ; {}
6AA7: C0              RET     NZ                  
6AA8: CD 71 7A        CALL    $7A71               ; {}
6AAB: FE 07           CP      $07                 
6AAD: CA 03 7A        JP      Z,$7A03             ; {}
6AB0: 21 B9 6A        LD      HL,$6AB9            
6AB3: CD 60 7A        CALL    $7A60               ; {}
6AB6: C3 87 7A        JP      $7A87               ; {}
6AB9: CA 6A CF        JP      Z,$CF6A             
6ABC: 6A              LD      L,D                 
6ABD: D4 6A D9        CALL    NC,$D96A            
6AC0: 6A              LD      L,D                 
6AC1: DE 6A           SBC     $6A                 
6AC3: E3                              
6AC4: 6A              LD      L,D                 
6AC5: 00              NOP                         
6AC6: 20 11           JR      NZ,$6AD9            ; {}
6AC8: 80              ADD     A,B                 
6AC9: 01 00 40        LD      BC,$4000            
6ACC: 21 80 01        LD      HL,$0180            
6ACF: 00              NOP                         
6AD0: 60              LD      H,B                 
6AD1: 39              ADD     HL,SP               
6AD2: 80              ADD     A,B                 
6AD3: 01 00 80        LD      BC,$8000            
6AD6: 49              LD      C,C                 
6AD7: 80              ADD     A,B                 
6AD8: 01 00 A0        LD      BC,$A000            
6ADB: 4B              LD      C,E                 
6ADC: 80              ADD     A,B                 
6ADD: 01 00 C0        LD      BC,$C000            
6AE0: 4D              LD      C,L                 
6AE1: 80              ADD     A,B                 
6AE2: 01 3C E0        LD      BC,$E03C            
6AE5: 4F              LD      C,A                 
6AE6: C0              RET     NZ                  
6AE7: 01 21 17        LD      BC,$1721            
6AEA: 6B              LD      L,E                 
6AEB: C3 E5 79        JP      $79E5               ; {}
6AEE: CD 6D 7A        CALL    $7A6D               ; {}
6AF1: C0              RET     NZ                  
6AF2: CD 71 7A        CALL    $7A71               ; {}
6AF5: FE 0B           CP      $0B                 
6AF7: CA 03 7A        JP      Z,$7A03             ; {}
6AFA: 21 03 6B        LD      HL,$6B03            
6AFD: CD 60 7A        CALL    $7A60               ; {}
6B00: C3 21 7A        JP      $7A21               ; {}
6B03: 1C              INC     E                   
6B04: 6B              LD      L,E                 
6B05: 1F              RRA                         
6B06: 6B              LD      L,E                 
6B07: 22              LD      (HLI),A             
6B08: 6B              LD      L,E                 
6B09: 25              DEC     H                   
6B0A: 6B              LD      L,E                 
6B0B: 28 6B           JR      Z,$6B78             ; {}
6B0D: 25              DEC     H                   
6B0E: 6B              LD      L,E                 
6B0F: 22              LD      (HLI),A             
6B10: 6B              LD      L,E                 
6B11: 1F              RRA                         
6B12: 6B              LD      L,E                 
6B13: 1C              INC     E                   
6B14: 6B              LD      L,E                 
6B15: 2B              DEC     HL                  
6B16: 6B              LD      L,E                 
6B17: 00              NOP                         
6B18: 67              LD      H,A                 
6B19: 2C              INC     L                   
6B1A: 80              ADD     A,B                 
6B1B: 01 3C 00        LD      BC,$003C            
6B1E: 01 4C 00        LD      BC,$004C            
6B21: 01 5C 00        LD      BC,$005C            
6B24: 01 6C 00        LD      BC,$006C            
6B27: 01 7C 00        LD      BC,$007C            
6B2A: 01 09 80        LD      BC,$8009            
6B2D: 30 21           JR      NC,$6B50            ; {}
6B2F: 73              LD      (HL),E              
6B30: 6B              LD      L,E                 
6B31: C3 E0 79        JP      $79E0               ; {}
6B34: CD 6D 7A        CALL    $7A6D               ; {}
6B37: C0              RET     NZ                  
6B38: CD 71 7A        CALL    $7A71               ; {}
6B3B: FE 16           CP      $16                 
6B3D: CA 03 7A        JP      Z,$7A03             ; {}
6B40: 21 49 6B        LD      HL,$6B49            
6B43: CD 60 7A        CALL    $7A60               ; {}
6B46: C3 21 7A        JP      $7A21               ; {}
6B49: 78              LD      A,B                 
6B4A: 6B              LD      L,E                 
6B4B: 7B              LD      A,E                 
6B4C: 6B              LD      L,E                 
6B4D: 7E              LD      A,(HL)              
6B4E: 6B              LD      L,E                 
6B4F: 81              ADD     A,C                 
6B50: 6B              LD      L,E                 
6B51: 84              ADD     A,H                 
6B52: 6B              LD      L,E                 
6B53: 81              ADD     A,C                 
6B54: 6B              LD      L,E                 
6B55: 7E              LD      A,(HL)              
6B56: 6B              LD      L,E                 
6B57: 7B              LD      A,E                 
6B58: 6B              LD      L,E                 
6B59: 7E              LD      A,(HL)              
6B5A: 6B              LD      L,E                 
6B5B: 81              ADD     A,C                 
6B5C: 6B              LD      L,E                 
6B5D: 84              ADD     A,H                 
6B5E: 6B              LD      L,E                 
6B5F: 87              ADD     A,A                 
6B60: 6B              LD      L,E                 
6B61: 8A              ADC     A,D                 
6B62: 6B              LD      L,E                 
6B63: 87              ADD     A,A                 
6B64: 6B              LD      L,E                 
6B65: 84              ADD     A,H                 
6B66: 6B              LD      L,E                 
6B67: 81              ADD     A,C                 
6B68: 6B              LD      L,E                 
6B69: 84              ADD     A,H                 
6B6A: 6B              LD      L,E                 
6B6B: 87              ADD     A,A                 
6B6C: 6B              LD      L,E                 
6B6D: 8A              ADC     A,D                 
6B6E: 6B              LD      L,E                 
6B6F: 8D              ADC     A,L                 
6B70: 6B              LD      L,E                 
6B71: 90              SUB     B                   
6B72: 6B              LD      L,E                 
6B73: 00              NOP                         
6B74: F7              RST     0X30                
6B75: 3D              DEC     A                   
6B76: 80              ADD     A,B                 
6B77: 04              INC     B                   
6B78: 60              LD      H,B                 
6B79: 00              NOP                         
6B7A: 04              INC     B                   
6B7B: 61              LD      H,C                 
6B7C: 00              NOP                         
6B7D: 04              INC     B                   
6B7E: 62              LD      H,D                 
6B7F: 00              NOP                         
6B80: 04              INC     B                   
6B81: 63              LD      H,E                 
6B82: 00              NOP                         
6B83: 04              INC     B                   
6B84: 64              LD      H,H                 
6B85: 00              NOP                         
6B86: 04              INC     B                   
6B87: 65              LD      H,L                 
6B88: 00              NOP                         
6B89: 04              INC     B                   
6B8A: 66              LD      H,(HL)              
6B8B: 00              NOP                         
6B8C: 04              INC     B                   
6B8D: 67              LD      H,A                 
6B8E: 00              NOP                         
6B8F: 04              INC     B                   
6B90: 74              LD      (HL),H              
6B91: 00              NOP                         
6B92: 28 FA           JR      Z,$6B8E             ; {}
6B94: 79              LD      A,C                 
6B95: D3                              
6B96: A7              AND     A                   
6B97: C2 28 7A        JP      NZ,$7A28            ; {}
6B9A: FA D6 D3        LD      A,($D3D6)           
6B9D: A7              AND     A                   
6B9E: 20 06           JR      NZ,$6BA6            ; {}
6BA0: 21 F1 6B        LD      HL,$6BF1            
6BA3: C3 E5 79        JP      $79E5               ; {}
6BA6: 21 05 6C        LD      HL,$6C05            
6BA9: 18 F8           JR      $6BA3               ; {}
6BAB: CD 6D 7A        CALL    $7A6D               ; {}
6BAE: C0              RET     NZ                  
6BAF: CD 71 7A        CALL    $7A71               ; {}
6BB2: FE 03           CP      $03                 
6BB4: 28 1A           JR      Z,$6BD0             ; {}
6BB6: FE 06           CP      $06                 
6BB8: CA D9 6B        JP      Z,$6BD9             ; {}
6BBB: FA D6 D3        LD      A,($D3D6)           
6BBE: A7              AND     A                   
6BBF: 20 0A           JR      NZ,$6BCB            ; {}
6BC1: 21 E3 6B        LD      HL,$6BE3            
6BC4: 0A              LD      A,(BC)              
6BC5: CD 60 7A        CALL    $7A60               ; {}
6BC8: C3 87 7A        JP      $7A87               ; {}
6BCB: 21 ED 6B        LD      HL,$6BED            
6BCE: 18 F4           JR      $6BC4               ; {}
6BD0: FA D6 D3        LD      A,($D3D6)           
6BD3: A7              AND     A                   
6BD4: C2 D9 6B        JP      NZ,$6BD9            ; {}
6BD7: 18 E8           JR      $6BC1               ; {}
6BD9: 21 78 D3        LD      HL,$D378            
6BDC: 3E 1B           LD      A,$1B               
6BDE: 22              LD      (HLI),A             
6BDF: AF              XOR     A                   
6BE0: 77              LD      (HL),A              
6BE1: 18 B0           JR      $6B93               ; {}
6BE3: FB              EI                          
6BE4: 6B              LD      L,E                 
6BE5: F6 6B           OR      $6B                 
6BE7: 00              NOP                         
6BE8: 6C              LD      L,H                 
6BE9: F6 6B           OR      $6B                 
6BEB: 00              NOP                         
6BEC: 6C              LD      L,H                 
6BED: 0A              LD      A,(BC)              
6BEE: 6C              LD      L,H                 
6BEF: 0A              LD      A,(BC)              
6BF0: 6C              LD      L,H                 
6BF1: 37              SCF                         
6BF2: 61              LD      H,C                 
6BF3: 30 80           JR      NC,$6B75            ; {}
6BF5: 03              INC     BC                  
6BF6: 37              SCF                         
6BF7: 41              LD      B,C                 
6BF8: 14              INC     D                   
6BF9: 80              ADD     A,B                 
6BFA: 03              INC     BC                  
6BFB: 37              SCF                         
6BFC: 20 30           JR      NZ,$6C2E            ; {}
6BFE: C0              RET     NZ                  
6BFF: 02              LD      (BC),A              
6C00: 37              SCF                         
6C01: 20 14           JR      NZ,$6C17            ; {}
6C03: C0              RET     NZ                  
6C04: 02              LD      (BC),A              
6C05: 37              SCF                         
6C06: A1              AND     C                   
6C07: 30 80           JR      NC,$6B89            ; {}
6C09: 04              INC     B                   
6C0A: 37              SCF                         
6C0B: 51              LD      D,C                 
6C0C: 14              INC     D                   
6C0D: 80              ADD     A,B                 
6C0E: 04              INC     B                   
6C0F: 3E 06           LD      A,$06               
6C11: EA BF D3        LD      ($D3BF),A           
6C14: 21 3D 6C        LD      HL,$6C3D            
6C17: C3 E5 79        JP      $79E5               ; {}
6C1A: CD 6D 7A        CALL    $7A6D               ; {}
6C1D: C0              RET     NZ                  
6C1E: CD 71 7A        CALL    $7A71               ; {}
6C21: FE 03           CP      $03                 
6C23: 28 09           JR      Z,$6C2E             ; {}
6C25: 21 39 6C        LD      HL,$6C39            
6C28: CD 60 7A        CALL    $7A60               ; {}
6C2B: C3 21 7A        JP      $7A21               ; {}
6C2E: CD A8 7A        CALL    $7AA8               ; {}
6C31: CA FD 79        JP      Z,$79FD             ; {}
6C34: 3E 01           LD      A,$01               
6C36: 02              LD      (BC),A              
6C37: 18 EC           JR      $6C25               ; {}
6C39: 42              LD      B,D                 
6C3A: 6C              LD      L,H                 
6C3B: 45              LD      B,L                 
6C3C: 6C              LD      L,H                 
6C3D: 00              NOP                         
6C3E: C0              RET     NZ                  
6C3F: 58              LD      E,B                 
6C40: 80              ADD     A,B                 
6C41: 02              LD      (BC),A              
6C42: 68              LD      L,B                 
6C43: 80              ADD     A,B                 
6C44: 02              LD      (BC),A              
6C45: 58              LD      E,B                 
6C46: 80              ADD     A,B                 
6C47: 02              LD      (BC),A              
6C48: 3E 78           LD      A,$78               
6C4A: EA BF D3        LD      ($D3BF),A           
6C4D: 21 83 6C        LD      HL,$6C83            
6C50: C3 E0 79        JP      $79E0               ; {}
6C53: CD 6D 7A        CALL    $7A6D               ; {}
6C56: C0              RET     NZ                  
6C57: CD 71 7A        CALL    $7A71               ; {}
6C5A: FE 03           CP      $03                 
6C5C: 28 09           JR      Z,$6C67             ; {}
6C5E: 21 7F 6C        LD      HL,$6C7F            
6C61: CD 60 7A        CALL    $7A60               ; {}
6C64: C3 21 7A        JP      $7A21               ; {}
6C67: CD A8 7A        CALL    $7AA8               ; {}
6C6A: CA FD 79        JP      Z,$79FD             ; {}
6C6D: FE 18           CP      $18                 
6C6F: 28 05           JR      Z,$6C76             ; {}
6C71: 3E 01           LD      A,$01               
6C73: 02              LD      (BC),A              
6C74: 18 E8           JR      $6C5E               ; {}
6C76: 3E 01           LD      A,$01               
6C78: 02              LD      (BC),A              
6C79: 21 88 6C        LD      HL,$6C88            
6C7C: C3 87 7A        JP      $7A87               ; {}
6C7F: 8D              ADC     A,L                 
6C80: 6C              LD      L,H                 
6C81: 90              SUB     B                   
6C82: 6C              LD      L,H                 
6C83: 00              NOP                         
6C84: 2C              INC     L                   
6C85: 7C              LD      A,H                 
6C86: 80              ADD     A,B                 
6C87: 02              LD      (BC),A              
6C88: 00              NOP                         
6C89: F7              RST     0X30                
6C8A: 7C              LD      A,H                 
6C8B: 80              ADD     A,B                 
6C8C: 02              LD      (BC),A              
6C8D: 7D              LD      A,L                 
6C8E: 00              NOP                         
6C8F: 02              LD      (BC),A              
6C90: 7C              LD      A,H                 
6C91: 00              NOP                         
6C92: 02              LD      (BC),A              
6C93: FA 79 D3        LD      A,($D379)           
6C96: A7              AND     A                   
6C97: C2 28 7A        JP      NZ,$7A28            ; {}
6C9A: 21 B6 6C        LD      HL,$6CB6            
6C9D: C3 E5 79        JP      $79E5               ; {}
6CA0: FA 0E C5        LD      A,($C50E)           
6CA3: A7              AND     A                   
6CA4: 28 07           JR      Z,$6CAD             ; {}
6CA6: CD 6D 7A        CALL    $7A6D               ; {}
6CA9: C0              RET     NZ                  
6CAA: C3 03 7A        JP      $7A03               ; {}
6CAD: 21 BB 6C        LD      HL,$6CBB            
6CB0: CD 87 7A        CALL    $7A87               ; {}
6CB3: C3 03 7A        JP      $7A03               ; {}
6CB6: 08 60 00        LD      ($0060),SP          
6CB9: C0              RET     NZ                  
6CBA: 0C              INC     C                   
6CBB: 00              NOP                         
6CBC: 67              LD      H,A                 
6CBD: 00              NOP                         
6CBE: 00              NOP                         
6CBF: 20 3E           JR      NZ,$6CFF            ; {}
6CC1: 14              INC     D                   
6CC2: EA BF D3        LD      ($D3BF),A           
6CC5: 21 F7 6C        LD      HL,$6CF7            
6CC8: C3 E5 79        JP      $79E5               ; {}
6CCB: CD 71 7A        CALL    $7A71               ; {}
6CCE: FE 03           CP      $03                 
6CD0: 28 09           JR      Z,$6CDB             ; {}
6CD2: 21 F3 6C        LD      HL,$6CF3            
6CD5: CD 60 7A        CALL    $7A60               ; {}
6CD8: C3 21 7A        JP      $7A21               ; {}
6CDB: CD A8 7A        CALL    $7AA8               ; {}
6CDE: CA 03 7A        JP      Z,$7A03             ; {}
6CE1: FE 0E           CP      $0E                 
6CE3: 28 05           JR      Z,$6CEA             ; {}
6CE5: 3E 01           LD      A,$01               
6CE7: 02              LD      (BC),A              
6CE8: 18 E8           JR      $6CD2               ; {}
6CEA: 3E 01           LD      A,$01               
6CEC: 02              LD      (BC),A              
6CED: 21 FC 6C        LD      HL,$6CFC            
6CF0: C3 87 7A        JP      $7A87               ; {}
6CF3: 01 6D 04        LD      BC,$046D            
6CF6: 6D              LD      L,L                 
6CF7: 00              NOP                         
6CF8: 1A              LD      A,(DE)              
6CF9: 06 80           LD      B,$80               
6CFB: 01 00 64        LD      BC,$6400            
6CFE: 06 80           LD      B,$80               
6D00: 01 06 00        LD      BC,$0006            
6D03: 01 48 00        LD      BC,$0048            
6D06: 01 21 26        LD      BC,$2621            
6D09: 6D              LD      L,L                 
6D0A: C3 E5 79        JP      $79E5               ; {}
6D0D: CD 71 7A        CALL    $7A71               ; {}
6D10: FE 03           CP      $03                 
6D12: 28 09           JR      Z,$6D1D             ; {}
6D14: 21 22 6D        LD      HL,$6D22            
6D17: CD 60 7A        CALL    $7A60               ; {}
6D1A: C3 21 7A        JP      $7A21               ; {}
6D1D: 3E 01           LD      A,$01               
6D1F: 02              LD      (BC),A              
6D20: 18 F2           JR      $6D14               ; {}
6D22: 2B              DEC     HL                  
6D23: 6D              LD      L,L                 
6D24: 2E 6D           LD      L,$6D               
6D26: 00              NOP                         
6D27: 50              LD      D,B                 
6D28: 0B              DEC     BC                  
6D29: 80              ADD     A,B                 
6D2A: 01 0C 00        LD      BC,$000C            
6D2D: 01 0B 00        LD      BC,$000B            
6D30: 01 21 5C        LD      BC,$5C21            
6D33: 6D              LD      L,L                 
6D34: C3 E0 79        JP      $79E0               ; {}
6D37: CD 6D 7A        CALL    $7A6D               ; {}
6D3A: C0              RET     NZ                  
6D3B: CD 71 7A        CALL    $7A71               ; {}
6D3E: FE 05           CP      $05                 
6D40: CA 03 7A        JP      Z,$7A03             ; {}
6D43: 21 54 6D        LD      HL,$6D54            
6D46: CD 60 7A        CALL    $7A60               ; {}
6D49: FA 98 D3        LD      A,($D398)           
6D4C: FE 01           CP      $01                 
6D4E: CA 87 7A        JP      Z,$7A87             ; {}
6D51: C3 21 7A        JP      $7A21               ; {}
6D54: 61              LD      H,C                 
6D55: 6D              LD      L,L                 
6D56: 66              LD      H,(HL)              
6D57: 6D              LD      L,L                 
6D58: 69              LD      L,C                 
6D59: 6D              LD      L,L                 
6D5A: 6C              LD      L,H                 
6D5B: 6D              LD      L,L                 
6D5C: 00              NOP                         
6D5D: 0F              RRCA                        
6D5E: 60              LD      H,B                 
6D5F: 80              ADD     A,B                 
6D60: 38 00           JR      C,$6D62             ; {}
6D62: F6 60           OR      $60                 
6D64: 80              ADD     A,B                 
6D65: 0C              INC     C                   
6D66: 61              LD      H,C                 
6D67: 00              NOP                         
6D68: 0C              INC     C                   
6D69: 62              LD      H,D                 
6D6A: 00              NOP                         
6D6B: 0C              INC     C                   
6D6C: 63              LD      H,E                 
6D6D: 00              NOP                         
6D6E: 38 21           JR      C,$6D91             ; {}
6D70: 87              ADD     A,A                 
6D71: 6D              LD      L,L                 
6D72: C3 E0 79        JP      $79E0               ; {}
6D75: CD 6D 7A        CALL    $7A6D               ; {}
6D78: C0              RET     NZ                  
6D79: CD 71 7A        CALL    $7A71               ; {}
6D7C: FE 02           CP      $02                 
6D7E: CA FD 79        JP      Z,$79FD             ; {}
6D81: 21 8C 6D        LD      HL,$6D8C            
6D84: C3 87 7A        JP      $7A87               ; {}
6D87: 00              NOP                         
6D88: 0F              RRCA                        
6D89: A8              XOR     B                   
6D8A: 80              ADD     A,B                 
6D8B: A0              AND     B                   
6D8C: 00              NOP                         
6D8D: F7              RST     0X30                
6D8E: A8              XOR     B                   
6D8F: 80              ADD     A,B                 
6D90: 60              LD      H,B                 
6D91: 21 A9 6D        LD      HL,$6DA9            
6D94: C3 E5 79        JP      $79E5               ; {}
6D97: CD 6D 7A        CALL    $7A6D               ; {}
6D9A: C0              RET     NZ                  
6D9B: CD 71 7A        CALL    $7A71               ; {}
6D9E: FE 02           CP      $02                 
6DA0: CA 03 7A        JP      Z,$7A03             ; {}
6DA3: 21 AE 6D        LD      HL,$6DAE            
6DA6: C3 87 7A        JP      $7A87               ; {}
6DA9: 00              NOP                         
6DAA: 29              ADD     HL,HL               
6DAB: 07              RLCA                        
6DAC: 80              ADD     A,B                 
6DAD: 08 00 A7        LD      ($A700),SP          
6DB0: 05              DEC     B                   
6DB1: 80              ADD     A,B                 
6DB2: 50              LD      D,B                 
6DB3: 21 1C 6E        LD      HL,$6E1C            
6DB6: C3 E0 79        JP      $79E0               ; {}
6DB9: CD 6D 7A        CALL    $7A6D               ; {}
6DBC: C0              RET     NZ                  
6DBD: CD 71 7A        CALL    $7A71               ; {}
6DC0: FE 24           CP      $24                 
6DC2: CA FD 79        JP      Z,$79FD             ; {}
6DC5: 21 D6 6D        LD      HL,$6DD6            
6DC8: CD 60 7A        CALL    $7A60               ; {}
6DCB: FA 98 D3        LD      A,($D398)           
6DCE: FE 1E           CP      $1E                 
6DD0: CA 87 7A        JP      Z,$7A87             ; {}
6DD3: C3 21 7A        JP      $7A21               ; {}
6DD6: 27              DAA                         
6DD7: 6E              LD      L,(HL)              
6DD8: 2A              LD      A,(HLI)             
6DD9: 6E              LD      L,(HL)              
6DDA: 2D              DEC     L                   
6DDB: 6E              LD      L,(HL)              
6DDC: 2A              LD      A,(HLI)             
6DDD: 6E              LD      L,(HL)              
6DDE: 27              DAA                         
6DDF: 6E              LD      L,(HL)              
6DE0: 24              INC     H                   
6DE1: 6E              LD      L,(HL)              
6DE2: 27              DAA                         
6DE3: 6E              LD      L,(HL)              
6DE4: 2A              LD      A,(HLI)             
6DE5: 6E              LD      L,(HL)              
6DE6: 2D              DEC     L                   
6DE7: 6E              LD      L,(HL)              
6DE8: 2A              LD      A,(HLI)             
6DE9: 6E              LD      L,(HL)              
6DEA: 27              DAA                         
6DEB: 6E              LD      L,(HL)              
6DEC: 24              INC     H                   
6DED: 6E              LD      L,(HL)              
6DEE: 27              DAA                         
6DEF: 6E              LD      L,(HL)              
6DF0: 2D              DEC     L                   
6DF1: 6E              LD      L,(HL)              
6DF2: 30 6E           JR      NC,$6E62            ; {}
6DF4: 2D              DEC     L                   
6DF5: 6E              LD      L,(HL)              
6DF6: 27              DAA                         
6DF7: 6E              LD      L,(HL)              
6DF8: 24              INC     H                   
6DF9: 6E              LD      L,(HL)              
6DFA: 27              DAA                         
6DFB: 6E              LD      L,(HL)              
6DFC: 2D              DEC     L                   
6DFD: 6E              LD      L,(HL)              
6DFE: 30 6E           JR      NC,$6E6E            ; {}
6E00: 2D              DEC     L                   
6E01: 6E              LD      L,(HL)              
6E02: 27              DAA                         
6E03: 6E              LD      L,(HL)              
6E04: 21 6E 27        LD      HL,$276E            
6E07: 6E              LD      L,(HL)              
6E08: 2A              LD      A,(HLI)             
6E09: 6E              LD      L,(HL)              
6E0A: 2D              DEC     L                   
6E0B: 6E              LD      L,(HL)              
6E0C: 30 6E           JR      NC,$6E7C            ; {}
6E0E: 33              INC     SP                  
6E0F: 6E              LD      L,(HL)              
6E10: 36 6E           LD      (HL),$6E            
6E12: 3B              DEC     SP                  
6E13: 6E              LD      L,(HL)              
6E14: 3E 6E           LD      A,$6E               
6E16: 41              LD      B,C                 
6E17: 6E              LD      L,(HL)              
6E18: 44              LD      B,H                 
6E19: 6E              LD      L,(HL)              
6E1A: 47              LD      B,A                 
6E1B: 6E              LD      L,(HL)              
6E1C: 00              NOP                         
6E1D: F0 8C           LD      A,($8C)             
6E1F: 80              ADD     A,B                 
6E20: 5C              LD      E,H                 
6E21: 8C              ADC     A,H                 
6E22: 00              NOP                         
6E23: 08 8C 00        LD      ($008C),SP          
6E26: 0C              INC     C                   
6E27: 7E              LD      A,(HL)              
6E28: 00              NOP                         
6E29: 04              INC     B                   
6E2A: 7C              LD      A,H                 
6E2B: 00              NOP                         
6E2C: 04              INC     B                   
6E2D: 6E              LD      L,(HL)              
6E2E: 00              NOP                         
6E2F: 04              INC     B                   
6E30: 6D              LD      L,L                 
6E31: 00              NOP                         
6E32: 04              INC     B                   
6E33: 6C              LD      L,H                 
6E34: 00              NOP                         
6E35: 04              INC     B                   
6E36: 00              NOP                         
6E37: F7              RST     0X30                
6E38: 6B              LD      L,E                 
6E39: 80              ADD     A,B                 
6E3A: 0C              INC     C                   
6E3B: 6C              LD      L,H                 
6E3C: 00              NOP                         
6E3D: 0C              INC     C                   
6E3E: 6D              LD      L,L                 
6E3F: 00              NOP                         
6E40: 0C              INC     C                   
6E41: 6E              LD      L,(HL)              
6E42: 00              NOP                         
6E43: 0C              INC     C                   
6E44: 7C              LD      A,H                 
6E45: 00              NOP                         
6E46: 0C              INC     C                   
6E47: 7E              LD      A,(HL)              
6E48: 00              NOP                         
6E49: 34              INC     (HL)                
6E4A: 3E 40           LD      A,$40               
6E4C: EA BF D3        LD      ($D3BF),A           
6E4F: 21 78 6E        LD      HL,$6E78            
6E52: C3 E5 79        JP      $79E5               ; {}
6E55: CD 6D 7A        CALL    $7A6D               ; {}
6E58: C0              RET     NZ                  
6E59: CD 71 7A        CALL    $7A71               ; {}
6E5C: FE 03           CP      $03                 
6E5E: 28 09           JR      Z,$6E69             ; {}
6E60: 21 74 6E        LD      HL,$6E74            
6E63: CD 60 7A        CALL    $7A60               ; {}
6E66: C3 21 7A        JP      $7A21               ; {}
6E69: CD A8 7A        CALL    $7AA8               ; {}
6E6C: CA FD 79        JP      Z,$79FD             ; {}
6E6F: 3E 01           LD      A,$01               
6E71: 02              LD      (BC),A              
6E72: 18 EC           JR      $6E60               ; {}
6E74: 7D              LD      A,L                 
6E75: 6E              LD      L,(HL)              
6E76: 80              ADD     A,B                 
6E77: 6E              LD      L,(HL)              
6E78: 00              NOP                         
6E79: 80              ADD     A,B                 
6E7A: 3A              LD      A,(HLD)             
6E7B: 80              ADD     A,B                 
6E7C: 01 39 80        LD      BC,$8039            
6E7F: 02              LD      (BC),A              
6E80: 3A              LD      A,(HLD)             
6E81: 80              ADD     A,B                 
6E82: 01 21 B6        LD      BC,$B621            
6E85: 6E              LD      L,(HL)              
6E86: C3 E5 79        JP      $79E5               ; {}
6E89: CD 6D 7A        CALL    $7A6D               ; {}
6E8C: C0              RET     NZ                  
6E8D: CD 71 7A        CALL    $7A71               ; {}
6E90: FE 0D           CP      $0D                 
6E92: CA 03 7A        JP      Z,$7A03             ; {}
6E95: 21 9E 6E        LD      HL,$6E9E            
6E98: CD 60 7A        CALL    $7A60               ; {}
6E9B: C3 21 7A        JP      $7A21               ; {}
6E9E: BB              CP      E                   
6E9F: 6E              LD      L,(HL)              
6EA0: BE              CP      (HL)                
6EA1: 6E              LD      L,(HL)              
6EA2: C1              POP     BC                  
6EA3: 6E              LD      L,(HL)              
6EA4: BE              CP      (HL)                
6EA5: 6E              LD      L,(HL)              
6EA6: BB              CP      E                   
6EA7: 6E              LD      L,(HL)              
6EA8: C4 6E C7        CALL    NZ,$C76E            
6EAB: 6E              LD      L,(HL)              
6EAC: CA 6E CD        JP      Z,$CD6E             
6EAF: 6E              LD      L,(HL)              
6EB0: D0              RET     NC                  
6EB1: 6E              LD      L,(HL)              
6EB2: D3                              
6EB3: 6E              LD      L,(HL)              
6EB4: D6 6E           SUB     $6E                 
6EB6: 00              NOP                         
6EB7: C2 5D 80        JP      NZ,$805D            
6EBA: 01 5C 00        LD      BC,$005C            
6EBD: 01 4F 00        LD      BC,$004F            
6EC0: 01 4E 00        LD      BC,$004E            
6EC3: 01 5D 00        LD      BC,$005D            
6EC6: 01 5E 00        LD      BC,$005E            
6EC9: 01 5F 00        LD      BC,$005F            
6ECC: 01 6C 00        LD      BC,$006C            
6ECF: 01 6D 00        LD      BC,$006D            
6ED2: 01 6E 00        LD      BC,$006E            
6ED5: 01 6F 00        LD      BC,$006F            
6ED8: 10 3E           STOP    $3E                 
6EDA: 05              DEC     B                   
6EDB: EA BF D3        LD      ($D3BF),A           
6EDE: 21 19 6F        LD      HL,$6F19            
6EE1: C3 E5 79        JP      $79E5               ; {}
6EE4: CD 6D 7A        CALL    $7A6D               ; {}
6EE7: C0              RET     NZ                  
6EE8: CD 71 7A        CALL    $7A71               ; {}
6EEB: FE 0C           CP      $0C                 
6EED: 28 09           JR      Z,$6EF8             ; {}
6EEF: 21 03 6F        LD      HL,$6F03            
6EF2: CD 60 7A        CALL    $7A60               ; {}
6EF5: C3 21 7A        JP      $7A21               ; {}
6EF8: CD A8 7A        CALL    $7AA8               ; {}
6EFB: CA 03 7A        JP      Z,$7A03             ; {}
6EFE: 3E 04           LD      A,$04               
6F00: 02              LD      (BC),A              
6F01: 18 EC           JR      $6EEF               ; {}
6F03: 21 6F 24        LD      HL,$246F            
6F06: 6F              LD      L,A                 
6F07: 27              DAA                         
6F08: 6F              LD      L,A                 
6F09: 2A              LD      A,(HLI)             
6F0A: 6F              LD      L,A                 
6F0B: 27              DAA                         
6F0C: 6F              LD      L,A                 
6F0D: 24              INC     H                   
6F0E: 6F              LD      L,A                 
6F0F: 21 6F 1E        LD      HL,$1E6F            
6F12: 6F              LD      L,A                 
6F13: 21 6F 24        LD      HL,$246F            
6F16: 6F              LD      L,A                 
6F17: 27              DAA                         
6F18: 6F              LD      L,A                 
6F19: 00              NOP                         
6F1A: 67              LD      H,A                 
6F1B: 6C              LD      L,H                 
6F1C: 80              ADD     A,B                 
6F1D: 01 6C 00        LD      BC,$006C            
6F20: 01 6B 00        LD      BC,$006B            
6F23: 01 6A 00        LD      BC,$006A            
6F26: 01 69 00        LD      BC,$0069            
6F29: 01 68 00        LD      BC,$0068            
6F2C: 02              LD      (BC),A              
6F2D: 3E 05           LD      A,$05               
6F2F: EA BF D3        LD      ($D3BF),A           
6F32: 21 63 6F        LD      HL,$6F63            
6F35: C3 E0 79        JP      $79E0               ; {}
6F38: CD 6D 7A        CALL    $7A6D               ; {}
6F3B: C0              RET     NZ                  
6F3C: CD 71 7A        CALL    $7A71               ; {}
6F3F: FE 07           CP      $07                 
6F41: 28 09           JR      Z,$6F4C             ; {}
6F43: 21 57 6F        LD      HL,$6F57            
6F46: CD 60 7A        CALL    $7A60               ; {}
6F49: C3 21 7A        JP      $7A21               ; {}
6F4C: CD A8 7A        CALL    $7AA8               ; {}
6F4F: CA 03 7A        JP      Z,$7A03             ; {}
6F52: 3E 01           LD      A,$01               
6F54: 02              LD      (BC),A              
6F55: 18 EC           JR      $6F43               ; {}
6F57: 68              LD      L,B                 
6F58: 6F              LD      L,A                 
6F59: 6B              LD      L,E                 
6F5A: 6F              LD      L,A                 
6F5B: 68              LD      L,B                 
6F5C: 6F              LD      L,A                 
6F5D: 6E              LD      L,(HL)              
6F5E: 6F              LD      L,A                 
6F5F: 68              LD      L,B                 
6F60: 6F              LD      L,A                 
6F61: 71              LD      (HL),C              
6F62: 6F              LD      L,A                 
6F63: 00              NOP                         
6F64: F4                              
6F65: 68              LD      L,B                 
6F66: 80              ADD     A,B                 
6F67: 02              LD      (BC),A              
6F68: 6F              LD      L,A                 
6F69: 00              NOP                         
6F6A: 02              LD      (BC),A              
6F6B: 69              LD      L,C                 
6F6C: 00              NOP                         
6F6D: 02              LD      (BC),A              
6F6E: 6A              LD      L,D                 
6F6F: 00              NOP                         
6F70: 02              LD      (BC),A              
6F71: 68              LD      L,B                 
6F72: 00              NOP                         
6F73: 02              LD      (BC),A              
6F74: 3E 08           LD      A,$08               
6F76: EA BF D3        LD      ($D3BF),A           
6F79: 21 BA 6F        LD      HL,$6FBA            
6F7C: C3 E0 79        JP      $79E0               ; {}
6F7F: CD 6D 7A        CALL    $7A6D               ; {}
6F82: C0              RET     NZ                  
6F83: CD 71 7A        CALL    $7A71               ; {}
6F86: FE 0A           CP      $0A                 
6F88: 28 11           JR      Z,$6F9B             ; {}
6F8A: 21 A6 6F        LD      HL,$6FA6            
6F8D: CD 60 7A        CALL    $7A60               ; {}
6F90: FA 98 D3        LD      A,($D398)           
6F93: FE 01           CP      $01                 
6F95: CA 87 7A        JP      Z,$7A87             ; {}
6F98: C3 21 7A        JP      $7A21               ; {}
6F9B: CD A8 7A        CALL    $7AA8               ; {}
6F9E: CA FD 79        JP      Z,$79FD             ; {}
6FA1: 3E 02           LD      A,$02               
6FA3: 02              LD      (BC),A              
6FA4: 18 E4           JR      $6F8A               ; {}
6FA6: BF              CP      A                   
6FA7: 6F              LD      L,A                 
6FA8: C4 6F CA        CALL    NZ,$CA6F            
6FAB: 6F              LD      L,A                 
6FAC: D0              RET     NC                  
6FAD: 6F              LD      L,A                 
6FAE: D6 6F           SUB     $6F                 
6FB0: D3                              
6FB1: 6F              LD      L,A                 
6FB2: D0              RET     NC                  
6FB3: 6F              LD      L,A                 
6FB4: CD 6F CA        CALL    $CA6F               
6FB7: 6F              LD      L,A                 
6FB8: C7              RST     0X00                
6FB9: 6F              LD      L,A                 
6FBA: 00              NOP                         
6FBB: C0              RET     NZ                  
6FBC: 7F              LD      A,A                 
6FBD: 80              ADD     A,B                 
6FBE: 88              ADC     A,B                 
6FBF: 00              NOP                         
6FC0: F4                              
6FC1: 6D              LD      L,L                 
6FC2: 80              ADD     A,B                 
6FC3: 01 74 00        LD      BC,$0074            
6FC6: 01 5F 00        LD      BC,$005F            
6FC9: 01 66 00        LD      BC,$0066            
6FCC: 01 5D 00        LD      BC,$005D            
6FCF: 01 64 00        LD      BC,$0064            
6FD2: 01 4F 00        LD      BC,$004F            
6FD5: 01 62 00        LD      BC,$0062            
6FD8: 01 21 E6        LD      BC,$E621            
6FDB: 6F              LD      L,A                 
6FDC: C3 E5 79        JP      $79E5               ; {}
6FDF: CD 6D 7A        CALL    $7A6D               ; {}
6FE2: C0              RET     NZ                  
6FE3: C3 03 7A        JP      $7A03               ; {}
6FE6: 00              NOP                         
6FE7: F4                              
6FE8: 7D              LD      A,L                 
6FE9: 80              ADD     A,B                 
6FEA: 40              LD      B,B                 
6FEB: 21 34 70        LD      HL,$7034            
6FEE: C3 E5 79        JP      $79E5               ; {}
6FF1: CD 6D 7A        CALL    $7A6D               ; {}
6FF4: C0              RET     NZ                  
6FF5: CD 71 7A        CALL    $7A71               ; {}
6FF8: FE 14           CP      $14                 
6FFA: CA FD 79        JP      Z,$79FD             ; {}
6FFD: 21 0E 70        LD      HL,$700E            
7000: CD 60 7A        CALL    $7A60               ; {}
7003: FA 98 D3        LD      A,($D398)           
7006: FE 13           CP      $13                 
7008: CA 87 7A        JP      Z,$7A87             ; {}
700B: C3 21 7A        JP      $7A21               ; {}
700E: 39              ADD     HL,SP               
700F: 70              LD      (HL),B              
7010: 3C              INC     A                   
7011: 70              LD      (HL),B              
7012: 3F              CCF                         
7013: 70              LD      (HL),B              
7014: 42              LD      B,D                 
7015: 70              LD      (HL),B              
7016: 45              LD      B,L                 
7017: 70              LD      (HL),B              
7018: 48              LD      C,B                 
7019: 70              LD      (HL),B              
701A: 4B              LD      C,E                 
701B: 70              LD      (HL),B              
701C: 4E              LD      C,(HL)              
701D: 70              LD      (HL),B              
701E: 51              LD      D,C                 
701F: 70              LD      (HL),B              
7020: 54              LD      D,H                 
7021: 70              LD      (HL),B              
7022: 57              LD      D,A                 
7023: 70              LD      (HL),B              
7024: 5A              LD      E,D                 
7025: 70              LD      (HL),B              
7026: 5D              LD      E,L                 
7027: 70              LD      (HL),B              
7028: 60              LD      H,B                 
7029: 70              LD      (HL),B              
702A: 63              LD      H,E                 
702B: 70              LD      (HL),B              
702C: 66              LD      H,(HL)              
702D: 70              LD      (HL),B              
702E: 69              LD      L,C                 
702F: 70              LD      (HL),B              
7030: 6C              LD      L,H                 
7031: 70              LD      (HL),B              
7032: 6F              LD      L,A                 
7033: 70              LD      (HL),B              
7034: 26 40           LD      H,$40               
7036: 37              SCF                         
7037: 80              ADD     A,B                 
7038: 06 36           LD      B,$36               
703A: 80              ADD     A,B                 
703B: 06 35           LD      B,$35               
703D: 80              ADD     A,B                 
703E: 06 34           LD      B,$34               
7040: 80              ADD     A,B                 
7041: 06 27           LD      B,$27               
7043: 80              ADD     A,B                 
7044: 06 26           LD      B,$26               
7046: 80              ADD     A,B                 
7047: 06 25           LD      B,$25               
7049: 80              ADD     A,B                 
704A: 06 24           LD      B,$24               
704C: 80              ADD     A,B                 
704D: 06 17           LD      B,$17               
704F: 80              ADD     A,B                 
7050: 06 16           LD      B,$16               
7052: 80              ADD     A,B                 
7053: 06 15           LD      B,$15               
7055: 80              ADD     A,B                 
7056: 06 14           LD      B,$14               
7058: 80              ADD     A,B                 
7059: 06 07           LD      B,$07               
705B: 80              ADD     A,B                 
705C: 06 06           LD      B,$06               
705E: 00              NOP                         
705F: 06 05           LD      B,$05               
7061: 00              NOP                         
7062: 06 04           LD      B,$04               
7064: 00              NOP                         
7065: 06 03           LD      B,$03               
7067: 00              NOP                         
7068: 06 02           LD      B,$02               
706A: 00              NOP                         
706B: 06 01           LD      B,$01               
706D: 00              NOP                         
706E: 06 00           LD      B,$00               
7070: 47              LD      B,A                 
7071: 00              NOP                         
7072: 80              ADD     A,B                 
7073: 20 21           JR      NZ,$7096            ; {}
7075: 9D              SBC     L                   
7076: 70              LD      (HL),B              
7077: C3 E5 79        JP      $79E5               ; {}
707A: CD 6D 7A        CALL    $7A6D               ; {}
707D: C0              RET     NZ                  
707E: CD 71 7A        CALL    $7A71               ; {}
7081: FE 08           CP      $08                 
7083: CA 03 7A        JP      Z,$7A03             ; {}
7086: 21 8F 70        LD      HL,$708F            
7089: CD 60 7A        CALL    $7A60               ; {}
708C: C3 87 7A        JP      $7A87               ; {}
708F: A2              AND     D                   
7090: 70              LD      (HL),B              
7091: A7              AND     A                   
7092: 70              LD      (HL),B              
7093: AC              XOR     H                   
7094: 70              LD      (HL),B              
7095: B1              OR      C                   
7096: 70              LD      (HL),B              
7097: B6              OR      (HL)                
7098: 70              LD      (HL),B              
7099: A7              AND     A                   
709A: 70              LD      (HL),B              
709B: BB              CP      E                   
709C: 70              LD      (HL),B              
709D: 26 29           LD      H,$29               
709F: 40              LD      B,B                 
70A0: C0              RET     NZ                  
70A1: 04              INC     B                   
70A2: 26 10           LD      H,$10               
70A4: 40              LD      B,B                 
70A5: C0              RET     NZ                  
70A6: 02              LD      (BC),A              
70A7: 26 29           LD      H,$29               
70A9: 10 C0           STOP    $C0                 
70AB: 04              INC     B                   
70AC: 26 10           LD      H,$10               
70AE: 10 C0           STOP    $C0                 
70B0: 02              LD      (BC),A              
70B1: 26 19           LD      H,$19               
70B3: 60              LD      H,B                 
70B4: C0              RET     NZ                  
70B5: 04              INC     B                   
70B6: 26 10           LD      H,$10               
70B8: 60              LD      H,B                 
70B9: C0              RET     NZ                  
70BA: 02              LD      (BC),A              
70BB: 26 10           LD      H,$10               
70BD: 10 C0           STOP    $C0                 
70BF: 03              INC     BC                  
70C0: 3E 08           LD      A,$08               
70C2: EA BF D3        LD      ($D3BF),A           
70C5: 21 08 71        LD      HL,$7108            
70C8: C3 E0 79        JP      $79E0               ; {}
70CB: CD 6D 7A        CALL    $7A6D               ; {}
70CE: C0              RET     NZ                  
70CF: CD 71 7A        CALL    $7A71               ; {}
70D2: FE 0C           CP      $0C                 
70D4: 28 11           JR      Z,$70E7             ; {}
70D6: 21 F2 70        LD      HL,$70F2            
70D9: CD 60 7A        CALL    $7A60               ; {}
70DC: FA 98 D3        LD      A,($D398)           
70DF: FE 02           CP      $02                 
70E1: CA 87 7A        JP      Z,$7A87             ; {}
70E4: C3 21 7A        JP      $7A21               ; {}
70E7: CD A8 7A        CALL    $7AA8               ; {}
70EA: CA FD 79        JP      Z,$79FD             ; {}
70ED: 3E 03           LD      A,$03               
70EF: 02              LD      (BC),A              
70F0: 18 E4           JR      $70D6               ; {}
70F2: 0D              DEC     C                   
70F3: 71              LD      (HL),C              
70F4: BF              CP      A                   
70F5: 6F              LD      L,A                 
70F6: C4 6F CA        CALL    NZ,$CA6F            
70F9: 6F              LD      L,A                 
70FA: D0              RET     NC                  
70FB: 6F              LD      L,A                 
70FC: D6 6F           SUB     $6F                 
70FE: D3                              
70FF: 6F              LD      L,A                 
7100: D0              RET     NC                  
7101: 6F              LD      L,A                 
7102: CD 6F CA        CALL    $CA6F               
7105: 6F              LD      L,A                 
7106: C7              RST     0X00                
7107: 6F              LD      L,A                 
7108: 00              NOP                         
7109: C0              RET     NZ                  
710A: 7F              LD      A,A                 
710B: 80              ADD     A,B                 
710C: FF              RST     0X38                
710D: 7F              LD      A,A                 
710E: 80              ADD     A,B                 
710F: 34              INC     (HL)                
7110: 21 28 71        LD      HL,$7128            
7113: C3 E5 79        JP      $79E5               ; {}
7116: CD 6D 7A        CALL    $7A6D               ; {}
7119: C0              RET     NZ                  
711A: CD 71 7A        CALL    $7A71               ; {}
711D: FE 02           CP      $02                 
711F: CA FD 79        JP      Z,$79FD             ; {}
7122: 21 2D 71        LD      HL,$712D            
7125: C3 87 7A        JP      $7A87               ; {}
7128: 00              NOP                         
7129: 19              ADD     HL,DE               
712A: 50              LD      D,B                 
712B: 80              ADD     A,B                 
712C: 06 00           LD      B,$00               
712E: 65              LD      H,L                 
712F: 50              LD      D,B                 
7130: 80              ADD     A,B                 
7131: 20 21           JR      NZ,$7154            ; {}
7133: 91              SUB     C                   
7134: 71              LD      (HL),C              
7135: C3 E5 79        JP      $79E5               ; {}
7138: CD 6D 7A        CALL    $7A6D               ; {}
713B: C0              RET     NZ                  
713C: CD 71 7A        CALL    $7A71               ; {}
713F: FE 23           CP      $23                 
7141: CA 03 7A        JP      Z,$7A03             ; {}
7144: 21 4D 71        LD      HL,$714D            
7147: CD 60 7A        CALL    $7A60               ; {}
714A: C3 87 7A        JP      $7A87               ; {}
714D: 96              SUB     (HL)                
714E: 71              LD      (HL),C              
714F: B9              CP      C                   
7150: 71              LD      (HL),C              
7151: 9B              SBC     E                   
7152: 71              LD      (HL),C              
7153: B9              CP      C                   
7154: 71              LD      (HL),C              
7155: A0              AND     B                   
7156: 71              LD      (HL),C              
7157: B9              CP      C                   
7158: 71              LD      (HL),C              
7159: A5              AND     L                   
715A: 71              LD      (HL),C              
715B: B9              CP      C                   
715C: 71              LD      (HL),C              
715D: A5              AND     L                   
715E: 71              LD      (HL),C              
715F: B9              CP      C                   
7160: 71              LD      (HL),C              
7161: AA              XOR     D                   
7162: 71              LD      (HL),C              
7163: BE              CP      (HL)                
7164: 71              LD      (HL),C              
7165: AF              XOR     A                   
7166: 71              LD      (HL),C              
7167: BE              CP      (HL)                
7168: 71              LD      (HL),C              
7169: B4              OR      H                   
716A: 71              LD      (HL),C              
716B: BE              CP      (HL)                
716C: 71              LD      (HL),C              
716D: AF              XOR     A                   
716E: 71              LD      (HL),C              
716F: BE              CP      (HL)                
7170: 71              LD      (HL),C              
7171: AA              XOR     D                   
7172: 71              LD      (HL),C              
7173: BE              CP      (HL)                
7174: 71              LD      (HL),C              
7175: AF              XOR     A                   
7176: 71              LD      (HL),C              
7177: BE              CP      (HL)                
7178: 71              LD      (HL),C              
7179: B4              OR      H                   
717A: 71              LD      (HL),C              
717B: BE              CP      (HL)                
717C: 71              LD      (HL),C              
717D: AF              XOR     A                   
717E: 71              LD      (HL),C              
717F: BE              CP      (HL)                
7180: 71              LD      (HL),C              
7181: AA              XOR     D                   
7182: 71              LD      (HL),C              
7183: BE              CP      (HL)                
7184: 71              LD      (HL),C              
7185: AF              XOR     A                   
7186: 71              LD      (HL),C              
7187: BE              CP      (HL)                
7188: 71              LD      (HL),C              
7189: B4              OR      H                   
718A: 71              LD      (HL),C              
718B: BE              CP      (HL)                
718C: 71              LD      (HL),C              
718D: AF              XOR     A                   
718E: 71              LD      (HL),C              
718F: BE              CP      (HL)                
7190: 71              LD      (HL),C              
7191: 00              NOP                         
7192: 1C              INC     E                   
7193: 60              LD      H,B                 
7194: 80              ADD     A,B                 
7195: 18 00           JR      $7197               ; {}
7197: 19              ADD     HL,DE               
7198: 50              LD      D,B                 
7199: 80              ADD     A,B                 
719A: 0A              LD      A,(BC)              
719B: 00              NOP                         
719C: 19              ADD     HL,DE               
719D: 30 80           JR      NC,$711F            ; {}
719F: 09              ADD     HL,BC               
71A0: 00              NOP                         
71A1: 19              ADD     HL,DE               
71A2: 40              LD      B,B                 
71A3: 80              ADD     A,B                 
71A4: 07              RLCA                        
71A5: 00              NOP                         
71A6: 19              ADD     HL,DE               
71A7: 50              LD      D,B                 
71A8: 80              ADD     A,B                 
71A9: 06 00           LD      B,$00               
71AB: 19              ADD     HL,DE               
71AC: 60              LD      H,B                 
71AD: 80              ADD     A,B                 
71AE: 06 00           LD      B,$00               
71B0: 19              ADD     HL,DE               
71B1: 60              LD      H,B                 
71B2: 80              ADD     A,B                 
71B3: 04              INC     B                   
71B4: 00              NOP                         
71B5: 19              ADD     HL,DE               
71B6: 50              LD      D,B                 
71B7: 80              ADD     A,B                 
71B8: 02              LD      (BC),A              
71B9: 37              SCF                         
71BA: 40              LD      B,B                 
71BB: 20 C0           JR      NZ,$717D            ; {}
71BD: 02              LD      (BC),A              
71BE: 37              SCF                         
71BF: 20 20           JR      NZ,$71E1            ; {}
71C1: C0              RET     NZ                  
71C2: 02              LD      (BC),A              
71C3: 21 12 72        LD      HL,$7212            
71C6: C3 E0 79        JP      $79E0               ; {}
71C9: CD 6D 7A        CALL    $7A6D               ; {}
71CC: C0              RET     NZ                  
71CD: CD 71 7A        CALL    $7A71               ; {}
71D0: FE 1B           CP      $1B                 
71D2: CA FD 79        JP      Z,$79FD             ; {}
71D5: 21 DE 71        LD      HL,$71DE            
71D8: CD 60 7A        CALL    $7A60               ; {}
71DB: C3 87 7A        JP      $7A87               ; {}
71DE: 17              RLA                         
71DF: 72              LD      (HL),D              
71E0: B9              CP      C                   
71E1: 71              LD      (HL),C              
71E2: 1C              INC     E                   
71E3: 72              LD      (HL),D              
71E4: B9              CP      C                   
71E5: 71              LD      (HL),C              
71E6: 21 72 B9        LD      HL,$B972            
71E9: 71              LD      (HL),C              
71EA: 26 72           LD      H,$72               
71EC: B9              CP      C                   
71ED: 71              LD      (HL),C              
71EE: 26 72           LD      H,$72               
71F0: B9              CP      C                   
71F1: 71              LD      (HL),C              
71F2: 2B              DEC     HL                  
71F3: 72              LD      (HL),D              
71F4: BE              CP      (HL)                
71F5: 71              LD      (HL),C              
71F6: 30 72           JR      NC,$726A            ; {}
71F8: BE              CP      (HL)                
71F9: 71              LD      (HL),C              
71FA: 35              DEC     (HL)                
71FB: 72              LD      (HL),D              
71FC: BE              CP      (HL)                
71FD: 71              LD      (HL),C              
71FE: 30 72           JR      NC,$7272            ; {}
7200: BE              CP      (HL)                
7201: 71              LD      (HL),C              
7202: 2B              DEC     HL                  
7203: 72              LD      (HL),D              
7204: BE              CP      (HL)                
7205: 71              LD      (HL),C              
7206: 30 72           JR      NC,$727A            ; {}
7208: BE              CP      (HL)                
7209: 71              LD      (HL),C              
720A: 35              DEC     (HL)                
720B: 72              LD      (HL),D              
720C: BE              CP      (HL)                
720D: 71              LD      (HL),C              
720E: 30 72           JR      NC,$7282            ; {}
7210: BE              CP      (HL)                
7211: 71              LD      (HL),C              
7212: 00              NOP                         
7213: 00              NOP                         
7214: 00              NOP                         
7215: 80              ADD     A,B                 
7216: 20 00           JR      NZ,$7218            ; {}
7218: 19              ADD     HL,DE               
7219: 27              DAA                         
721A: 80              ADD     A,B                 
721B: 0A              LD      A,(BC)              
721C: 00              NOP                         
721D: 19              ADD     HL,DE               
721E: 26 80           LD      H,$80               
7220: 09              ADD     HL,BC               
7221: 00              NOP                         
7222: 19              ADD     HL,DE               
7223: 24              INC     H                   
7224: 80              ADD     A,B                 
7225: 08 00 19        LD      ($1900),SP          
7228: 23              INC     HL                  
7229: 80              ADD     A,B                 
722A: 07              RLCA                        
722B: 00              NOP                         
722C: 19              ADD     HL,DE               
722D: 17              RLA                         
722E: 80              ADD     A,B                 
722F: 06 00           LD      B,$00               
7231: 19              ADD     HL,DE               
7232: 17              RLA                         
7233: 80              ADD     A,B                 
7234: 04              INC     B                   
7235: 00              NOP                         
7236: 19              ADD     HL,DE               
7237: 16 80           LD      D,$80               
7239: 02              LD      (BC),A              
723A: 21 69 72        LD      HL,$7269            
723D: C3 E5 79        JP      $79E5               ; {}
7240: CD 6D 7A        CALL    $7A6D               ; {}
7243: C0              RET     NZ                  
7244: CD 71 7A        CALL    $7A71               ; {}
7247: FE 0B           CP      $0B                 
7249: CA 03 7A        JP      Z,$7A03             ; {}
724C: 21 55 72        LD      HL,$7255            
724F: CD 60 7A        CALL    $7A60               ; {}
7252: C3 87 7A        JP      $7A87               ; {}
7255: 6E              LD      L,(HL)              
7256: 72              LD      (HL),D              
7257: 73              LD      (HL),E              
7258: 72              LD      (HL),D              
7259: 78              LD      A,B                 
725A: 72              LD      (HL),D              
725B: 73              LD      (HL),E              
725C: 72              LD      (HL),D              
725D: 6E              LD      L,(HL)              
725E: 72              LD      (HL),D              
725F: 69              LD      L,C                 
7260: 72              LD      (HL),D              
7261: 8C              ADC     A,H                 
7262: 72              LD      (HL),D              
7263: 87              ADD     A,A                 
7264: 72              LD      (HL),D              
7265: 82              ADD     A,D                 
7266: 72              LD      (HL),D              
7267: 7D              LD      A,L                 
7268: 72              LD      (HL),D              
7269: 00              NOP                         
726A: 20 30           JR      NZ,$729C            ; {}
726C: 80              ADD     A,B                 
726D: 02              LD      (BC),A              
726E: 00              NOP                         
726F: 40              LD      B,B                 
7270: 40              LD      B,B                 
7271: 80              ADD     A,B                 
7272: 03              INC     BC                  
7273: 00              NOP                         
7274: 80              ADD     A,B                 
7275: 50              LD      D,B                 
7276: 80              ADD     A,B                 
7277: 04              INC     B                   
7278: 00              NOP                         
7279: C0              RET     NZ                  
727A: 60              LD      H,B                 
727B: 80              ADD     A,B                 
727C: 05              DEC     B                   
727D: 37              SCF                         
727E: 10 30           STOP    $30                 
7280: C0              RET     NZ                  
7281: 02              LD      (BC),A              
7282: 00              NOP                         
7283: 10 40           STOP    $40                 
7285: 80              ADD     A,B                 
7286: 03              INC     BC                  
7287: 00              NOP                         
7288: 10 50           STOP    $50                 
728A: 80              ADD     A,B                 
728B: 04              INC     B                   
728C: 00              NOP                         
728D: 10 60           STOP    $60                 
728F: 80              ADD     A,B                 
7290: 05              DEC     B                   
7291: 21 CA 72        LD      HL,$72CA            
7294: C3 E5 79        JP      $79E5               ; {}
7297: CD 6D 7A        CALL    $7A6D               ; {}
729A: C0              RET     NZ                  
729B: CD 71 7A        CALL    $7A71               ; {}
729E: FE 0C           CP      $0C                 
72A0: CA FD 79        JP      Z,$79FD             ; {}
72A3: 21 B4 72        LD      HL,$72B4            
72A6: CD 60 7A        CALL    $7A60               ; {}
72A9: FA 98 D3        LD      A,($D398)           
72AC: FE 06           CP      $06                 
72AE: CA 87 7A        JP      Z,$7A87             ; {}
72B1: C3 21 7A        JP      $7A21               ; {}
72B4: D2 72 CF        JP      NC,$CF72            
72B7: 72              LD      (HL),D              
72B8: D5              PUSH    DE                  
72B9: 72              LD      (HL),D              
72BA: D2 72 D8        JP      NC,$D872            
72BD: 72              LD      (HL),D              
72BE: DB                              
72BF: 72              LD      (HL),D              
72C0: D2 72 CF        JP      NC,$CF72            
72C3: 72              LD      (HL),D              
72C4: D5              PUSH    DE                  
72C5: 72              LD      (HL),D              
72C6: D2 72 D8        JP      NC,$D872            
72C9: 72              LD      (HL),D              
72CA: 00              NOP                         
72CB: 80              ADD     A,B                 
72CC: 48              LD      C,B                 
72CD: 80              ADD     A,B                 
72CE: 02              LD      (BC),A              
72CF: 49              LD      C,C                 
72D0: 80              ADD     A,B                 
72D1: 02              LD      (BC),A              
72D2: 4A              LD      C,D                 
72D3: 80              ADD     A,B                 
72D4: 02              LD      (BC),A              
72D5: 4B              LD      C,E                 
72D6: 80              ADD     A,B                 
72D7: 02              LD      (BC),A              
72D8: 4C              LD      C,H                 
72D9: 80              ADD     A,B                 
72DA: 02              LD      (BC),A              
72DB: 00              NOP                         
72DC: 20 48           JR      NZ,$7326            ; {}
72DE: 80              ADD     A,B                 
72DF: 02              LD      (BC),A              
72E0: 3E 2B           LD      A,$2B               
72E2: EA DF D3        LD      ($D3DF),A           
72E5: 3E 15           LD      A,$15               
72E7: EA E0 D3        LD      ($D3E0),A           
72EA: 21 11 74        LD      HL,$7411            
72ED: C3 E5 79        JP      $79E5               ; {}
72F0: CD 6D 7A        CALL    $7A6D               ; {}
72F3: C0              RET     NZ                  
72F4: CD 71 7A        CALL    $7A71               ; {}
72F7: FE 05           CP      $05                 
72F9: 28 3C           JR      Z,$7337             ; {}
72FB: FE 0D           CP      $0D                 
72FD: 28 60           JR      Z,$735F             ; {}
72FF: FE 1A           CP      $1A                 
7301: 28 43           JR      Z,$7346             ; {}
7303: FE 52           CP      $52                 
7305: CA FD 79        JP      Z,$79FD             ; {}
7308: 21 6F 73        LD      HL,$736F            
730B: CD 60 7A        CALL    $7A60               ; {}
730E: FA 98 D3        LD      A,($D398)           
7311: FE 1A           CP      $1A                 
7313: CA 87 7A        JP      Z,$7A87             ; {}
7316: FE 22           CP      $22                 
7318: CA 87 7A        JP      Z,$7A87             ; {}
731B: FE 2A           CP      $2A                 
731D: CA 87 7A        JP      Z,$7A87             ; {}
7320: FE 32           CP      $32                 
7322: CA 87 7A        JP      Z,$7A87             ; {}
7325: FE 3A           CP      $3A                 
7327: CA 87 7A        JP      Z,$7A87             ; {}
732A: FE 42           CP      $42                 
732C: CA 87 7A        JP      Z,$7A87             ; {}
732F: FE 4A           CP      $4A                 
7331: CA 87 7A        JP      Z,$7A87             ; {}
7334: C3 21 7A        JP      $7A21               ; {}
7337: D5              PUSH    DE                  
7338: 11 DF D3        LD      DE,$D3DF            
733B: CD 6D 7A        CALL    $7A6D               ; {}
733E: D1              POP     DE                  
733F: 28 14           JR      Z,$7355             ; {}
7341: 3E 01           LD      A,$01               
7343: 02              LD      (BC),A              
7344: 18 C2           JR      $7308               ; {}
7346: D5              PUSH    DE                  
7347: 11 E0 D3        LD      DE,$D3E0            
734A: CD 6D 7A        CALL    $7A6D               ; {}
734D: D1              POP     DE                  
734E: 28 0A           JR      Z,$735A             ; {}
7350: 3E 12           LD      A,$12               
7352: 02              LD      (BC),A              
7353: 18 B3           JR      $7308               ; {}
7355: 3E 05           LD      A,$05               
7357: 02              LD      (BC),A              
7358: 18 AE           JR      $7308               ; {}
735A: 3E 1A           LD      A,$1A               
735C: 02              LD      (BC),A              
735D: 18 A9           JR      $7308               ; {}
735F: 3E 20           LD      A,$20               
7361: EA 70 D3        LD      ($D370),A           
7364: CD ED 53        CALL    $53ED               ; {}
7367: 01 98 D3        LD      BC,$D398            
736A: 11 93 D3        LD      DE,$D393            
736D: 18 99           JR      $7308               ; {}
736F: 16 74           LD      D,$74               
7371: 19              ADD     HL,DE               
7372: 74              LD      (HL),H              
7373: 1C              INC     E                   
7374: 74              LD      (HL),H              
7375: 1F              RRA                         
7376: 74              LD      (HL),H              
7377: 22              LD      (HLI),A             
7378: 74              LD      (HL),H              
7379: 25              DEC     H                   
737A: 74              LD      (HL),H              
737B: 28 74           JR      Z,$73F1             ; {}
737D: 2B              DEC     HL                  
737E: 74              LD      (HL),H              
737F: 2E 74           LD      L,$74               
7381: 31 74 34        LD      SP,$3474            
7384: 74              LD      (HL),H              
7385: 37              SCF                         
7386: 74              LD      (HL),H              
7387: 3A              LD      A,(HLD)             
7388: 74              LD      (HL),H              
7389: 3D              DEC     A                   
738A: 74              LD      (HL),H              
738B: 40              LD      B,B                 
738C: 74              LD      (HL),H              
738D: 43              LD      B,E                 
738E: 74              LD      (HL),H              
738F: 46              LD      B,(HL)              
7390: 74              LD      (HL),H              
7391: 49              LD      C,C                 
7392: 74              LD      (HL),H              
7393: 4C              LD      C,H                 
7394: 74              LD      (HL),H              
7395: 4F              LD      C,A                 
7396: 74              LD      (HL),H              
7397: 52              LD      D,D                 
7398: 74              LD      (HL),H              
7399: 55              LD      D,L                 
739A: 74              LD      (HL),H              
739B: 52              LD      D,D                 
739C: 74              LD      (HL),H              
739D: 4F              LD      C,A                 
739E: 74              LD      (HL),H              
739F: 4C              LD      C,H                 
73A0: 74              LD      (HL),H              
73A1: 58              LD      E,B                 
73A2: 74              LD      (HL),H              
73A3: 5D              LD      E,L                 
73A4: 74              LD      (HL),H              
73A5: 60              LD      H,B                 
73A6: 74              LD      (HL),H              
73A7: 63              LD      H,E                 
73A8: 74              LD      (HL),H              
73A9: 66              LD      H,(HL)              
73AA: 74              LD      (HL),H              
73AB: 63              LD      H,E                 
73AC: 74              LD      (HL),H              
73AD: 60              LD      H,B                 
73AE: 74              LD      (HL),H              
73AF: 5D              LD      E,L                 
73B0: 74              LD      (HL),H              
73B1: 69              LD      L,C                 
73B2: 74              LD      (HL),H              
73B3: 5D              LD      E,L                 
73B4: 74              LD      (HL),H              
73B5: 60              LD      H,B                 
73B6: 74              LD      (HL),H              
73B7: 63              LD      H,E                 
73B8: 74              LD      (HL),H              
73B9: 66              LD      H,(HL)              
73BA: 74              LD      (HL),H              
73BB: 63              LD      H,E                 
73BC: 74              LD      (HL),H              
73BD: 60              LD      H,B                 
73BE: 74              LD      (HL),H              
73BF: 5D              LD      E,L                 
73C0: 74              LD      (HL),H              
73C1: 6E              LD      L,(HL)              
73C2: 74              LD      (HL),H              
73C3: 5D              LD      E,L                 
73C4: 74              LD      (HL),H              
73C5: 60              LD      H,B                 
73C6: 74              LD      (HL),H              
73C7: 63              LD      H,E                 
73C8: 74              LD      (HL),H              
73C9: 66              LD      H,(HL)              
73CA: 74              LD      (HL),H              
73CB: 63              LD      H,E                 
73CC: 74              LD      (HL),H              
73CD: 60              LD      H,B                 
73CE: 74              LD      (HL),H              
73CF: 5D              LD      E,L                 
73D0: 74              LD      (HL),H              
73D1: 73              LD      (HL),E              
73D2: 74              LD      (HL),H              
73D3: 5D              LD      E,L                 
73D4: 74              LD      (HL),H              
73D5: 60              LD      H,B                 
73D6: 74              LD      (HL),H              
73D7: 63              LD      H,E                 
73D8: 74              LD      (HL),H              
73D9: 66              LD      H,(HL)              
73DA: 74              LD      (HL),H              
73DB: 63              LD      H,E                 
73DC: 74              LD      (HL),H              
73DD: 60              LD      H,B                 
73DE: 74              LD      (HL),H              
73DF: 5D              LD      E,L                 
73E0: 74              LD      (HL),H              
73E1: 78              LD      A,B                 
73E2: 74              LD      (HL),H              
73E3: 5D              LD      E,L                 
73E4: 74              LD      (HL),H              
73E5: 60              LD      H,B                 
73E6: 74              LD      (HL),H              
73E7: 63              LD      H,E                 
73E8: 74              LD      (HL),H              
73E9: 66              LD      H,(HL)              
73EA: 74              LD      (HL),H              
73EB: 63              LD      H,E                 
73EC: 74              LD      (HL),H              
73ED: 60              LD      H,B                 
73EE: 74              LD      (HL),H              
73EF: 5D              LD      E,L                 
73F0: 74              LD      (HL),H              
73F1: 7D              LD      A,L                 
73F2: 74              LD      (HL),H              
73F3: 5D              LD      E,L                 
73F4: 74              LD      (HL),H              
73F5: 60              LD      H,B                 
73F6: 74              LD      (HL),H              
73F7: 63              LD      H,E                 
73F8: 74              LD      (HL),H              
73F9: 66              LD      H,(HL)              
73FA: 74              LD      (HL),H              
73FB: 63              LD      H,E                 
73FC: 74              LD      (HL),H              
73FD: 60              LD      H,B                 
73FE: 74              LD      (HL),H              
73FF: 5D              LD      E,L                 
7400: 74              LD      (HL),H              
7401: 82              ADD     A,D                 
7402: 74              LD      (HL),H              
7403: 5D              LD      E,L                 
7404: 74              LD      (HL),H              
7405: 60              LD      H,B                 
7406: 74              LD      (HL),H              
7407: 63              LD      H,E                 
7408: 74              LD      (HL),H              
7409: 66              LD      H,(HL)              
740A: 74              LD      (HL),H              
740B: 63              LD      H,E                 
740C: 74              LD      (HL),H              
740D: 60              LD      H,B                 
740E: 74              LD      (HL),H              
740F: 5D              LD      E,L                 
7410: 74              LD      (HL),H              
7411: 00              NOP                         
7412: 80              ADD     A,B                 
7413: 9C              SBC     H                   
7414: 80              ADD     A,B                 
7415: 01 8E 00        LD      BC,$008E            
7418: 01 7E 00        LD      BC,$007E            
741B: 01 8C 00        LD      BC,$008C            
741E: 01 7C 00        LD      BC,$007C            
7421: 01 6F 00        LD      BC,$006F            
7424: 01 6D 00        LD      BC,$006D            
7427: 01 5F 00        LD      BC,$005F            
742A: 01 5D 00        LD      BC,$005D            
742D: 01 4F 00        LD      BC,$004F            
7430: 01 4D 00        LD      BC,$004D            
7433: 01 3F 00        LD      BC,$003F            
7436: 01 3D 00        LD      BC,$003D            
7439: 01 37 80        LD      BC,$8037            
743C: 02              LD      (BC),A              
743D: 35              DEC     (HL)                
743E: 80              ADD     A,B                 
743F: 02              LD      (BC),A              
7440: 27              DAA                         
7441: 80              ADD     A,B                 
7442: 02              LD      (BC),A              
7443: 25              DEC     H                   
7444: 80              ADD     A,B                 
7445: 02              LD      (BC),A              
7446: 17              RLA                         
7447: 80              ADD     A,B                 
7448: 02              LD      (BC),A              
7449: 15              DEC     D                   
744A: 80              ADD     A,B                 
744B: 02              LD      (BC),A              
744C: 14              INC     D                   
744D: 80              ADD     A,B                 
744E: 02              LD      (BC),A              
744F: 07              RLCA                        
7450: 80              ADD     A,B                 
7451: 02              LD      (BC),A              
7452: 06 80           LD      B,$80               
7454: 02              LD      (BC),A              
7455: 05              DEC     B                   
7456: 80              ADD     A,B                 
7457: 02              LD      (BC),A              
7458: 00              NOP                         
7459: 70              LD      (HL),B              
745A: 15              DEC     D                   
745B: 80              ADD     A,B                 
745C: 02              LD      (BC),A              
745D: 14              INC     D                   
745E: 80              ADD     A,B                 
745F: 02              LD      (BC),A              
7460: 07              RLCA                        
7461: 80              ADD     A,B                 
7462: 02              LD      (BC),A              
7463: 06 80           LD      B,$80               
7465: 02              LD      (BC),A              
7466: 05              DEC     B                   
7467: 80              ADD     A,B                 
7468: 02              LD      (BC),A              
7469: 00              NOP                         
746A: 60              LD      H,B                 
746B: 15              DEC     D                   
746C: 80              ADD     A,B                 
746D: 02              LD      (BC),A              
746E: 00              NOP                         
746F: 50              LD      D,B                 
7470: 15              DEC     D                   
7471: 80              ADD     A,B                 
7472: 02              LD      (BC),A              
7473: 00              NOP                         
7474: 40              LD      B,B                 
7475: 15              DEC     D                   
7476: 80              ADD     A,B                 
7477: 02              LD      (BC),A              
7478: 00              NOP                         
7479: 30 15           JR      NC,$7490            ; {}
747B: 80              ADD     A,B                 
747C: 02              LD      (BC),A              
747D: 00              NOP                         
747E: 20 15           JR      NZ,$7495            ; {}
7480: 80              ADD     A,B                 
7481: 02              LD      (BC),A              
7482: 00              NOP                         
7483: 10 15           STOP    $15                 
7485: 80              ADD     A,B                 
7486: 02              LD      (BC),A              
7487: 3E 40           LD      A,$40               
7489: EA BF D3        LD      ($D3BF),A           
748C: 21 E7 74        LD      HL,$74E7            
748F: C3 E5 79        JP      $79E5               ; {}
7492: CD 6D 7A        CALL    $7A6D               ; {}
7495: C0              RET     NZ                  
7496: CD 71 7A        CALL    $7A71               ; {}
7499: FE 21           CP      $21                 
749B: CA FD 79        JP      Z,$79FD             ; {}
749E: 21 A7 74        LD      HL,$74A7            
74A1: CD 60 7A        CALL    $7A60               ; {}
74A4: C3 87 7A        JP      $7A87               ; {}
74A7: EC                              
74A8: 74              LD      (HL),H              
74A9: F1              POP     AF                  
74AA: 74              LD      (HL),H              
74AB: F6 74           OR      $74                 
74AD: FB              EI                          
74AE: 74              LD      (HL),H              
74AF: 00              NOP                         
74B0: 75              LD      (HL),L              
74B1: 05              DEC     B                   
74B2: 75              LD      (HL),L              
74B3: 0A              LD      A,(BC)              
74B4: 75              LD      (HL),L              
74B5: 0F              RRCA                        
74B6: 75              LD      (HL),L              
74B7: 14              INC     D                   
74B8: 75              LD      (HL),L              
74B9: 19              ADD     HL,DE               
74BA: 75              LD      (HL),L              
74BB: 1E 75           LD      E,$75               
74BD: 23              INC     HL                  
74BE: 75              LD      (HL),L              
74BF: 28 75           JR      Z,$7536             ; {}
74C1: 2D              DEC     L                   
74C2: 75              LD      (HL),L              
74C3: 32              LD      (HLD),A             
74C4: 75              LD      (HL),L              
74C5: 37              SCF                         
74C6: 75              LD      (HL),L              
74C7: 3C              INC     A                   
74C8: 75              LD      (HL),L              
74C9: 41              LD      B,C                 
74CA: 75              LD      (HL),L              
74CB: 46              LD      B,(HL)              
74CC: 75              LD      (HL),L              
74CD: 4B              LD      C,E                 
74CE: 75              LD      (HL),L              
74CF: 50              LD      D,B                 
74D0: 75              LD      (HL),L              
74D1: 55              LD      D,L                 
74D2: 75              LD      (HL),L              
74D3: 5A              LD      E,D                 
74D4: 75              LD      (HL),L              
74D5: 5F              LD      E,A                 
74D6: 75              LD      (HL),L              
74D7: 64              LD      H,H                 
74D8: 75              LD      (HL),L              
74D9: 69              LD      L,C                 
74DA: 75              LD      (HL),L              
74DB: 6E              LD      L,(HL)              
74DC: 75              LD      (HL),L              
74DD: 73              LD      (HL),E              
74DE: 75              LD      (HL),L              
74DF: 78              LD      A,B                 
74E0: 75              LD      (HL),L              
74E1: 7D              LD      A,L                 
74E2: 75              LD      (HL),L              
74E3: 82              ADD     A,D                 
74E4: 75              LD      (HL),L              
74E5: 87              ADD     A,A                 
74E6: 75              LD      (HL),L              
74E7: 00              NOP                         
74E8: 20 67           JR      NZ,$7551            ; {}
74EA: 80              ADD     A,B                 
74EB: 02              LD      (BC),A              
74EC: 00              NOP                         
74ED: 20 66           JR      NZ,$7555            ; {}
74EF: 80              ADD     A,B                 
74F0: 02              LD      (BC),A              
74F1: 00              NOP                         
74F2: 20 65           JR      NZ,$7559            ; {}
74F4: 80              ADD     A,B                 
74F5: 02              LD      (BC),A              
74F6: 00              NOP                         
74F7: 20 64           JR      NZ,$755D            ; {}
74F9: 80              ADD     A,B                 
74FA: 03              INC     BC                  
74FB: 00              NOP                         
74FC: 20 57           JR      NZ,$7555            ; {}
74FE: 80              ADD     A,B                 
74FF: 03              INC     BC                  
7500: 00              NOP                         
7501: 20 56           JR      NZ,$7559            ; {}
7503: 80              ADD     A,B                 
7504: 03              INC     BC                  
7505: 00              NOP                         
7506: 20 55           JR      NZ,$755D            ; {}
7508: 80              ADD     A,B                 
7509: 04              INC     B                   
750A: 00              NOP                         
750B: 20 54           JR      NZ,$7561            ; {}
750D: 80              ADD     A,B                 
750E: 04              INC     B                   
750F: 00              NOP                         
7510: 20 47           JR      NZ,$7559            ; {}
7512: 80              ADD     A,B                 
7513: 04              INC     B                   
7514: 00              NOP                         
7515: 20 46           JR      NZ,$755D            ; {}
7517: 80              ADD     A,B                 
7518: 05              DEC     B                   
7519: 00              NOP                         
751A: 20 45           JR      NZ,$7561            ; {}
751C: 80              ADD     A,B                 
751D: 05              DEC     B                   
751E: 00              NOP                         
751F: 20 44           JR      NZ,$7565            ; {}
7521: 80              ADD     A,B                 
7522: 05              DEC     B                   
7523: 00              NOP                         
7524: 20 37           JR      NZ,$755D            ; {}
7526: 80              ADD     A,B                 
7527: 06 00           LD      B,$00               
7529: 20 36           JR      NZ,$7561            ; {}
752B: 80              ADD     A,B                 
752C: 06 00           LD      B,$00               
752E: 20 35           JR      NZ,$7565            ; {}
7530: 80              ADD     A,B                 
7531: 06 00           LD      B,$00               
7533: 20 34           JR      NZ,$7569            ; {}
7535: 80              ADD     A,B                 
7536: 08 00 20        LD      ($2000),SP          
7539: 27              DAA                         
753A: 80              ADD     A,B                 
753B: 08 00 20        LD      ($2000),SP          
753E: 26 80           LD      H,$80               
7540: 0A              LD      A,(BC)              
7541: 00              NOP                         
7542: 20 25           JR      NZ,$7569            ; {}
7544: 80              ADD     A,B                 
7545: 0A              LD      A,(BC)              
7546: 00              NOP                         
7547: 20 24           JR      NZ,$756D            ; {}
7549: 80              ADD     A,B                 
754A: 0C              INC     C                   
754B: 00              NOP                         
754C: 20 17           JR      NZ,$7565            ; {}
754E: 80              ADD     A,B                 
754F: 0C              INC     C                   
7550: 00              NOP                         
7551: 20 16           JR      NZ,$7569            ; {}
7553: 80              ADD     A,B                 
7554: 0E 00           LD      C,$00               
7556: 20 15           JR      NZ,$756D            ; {}
7558: 80              ADD     A,B                 
7559: 0E 00           LD      C,$00               
755B: 20 14           JR      NZ,$7571            ; {}
755D: 80              ADD     A,B                 
755E: 10 00           STOP    $00                 
7560: 20 07           JR      NZ,$7569            ; {}
7562: 80              ADD     A,B                 
7563: 10 00           STOP    $00                 
7565: 20 06           JR      NZ,$756D            ; {}
7567: 80              ADD     A,B                 
7568: 12              LD      (DE),A              
7569: 00              NOP                         
756A: 20 05           JR      NZ,$7571            ; {}
756C: 80              ADD     A,B                 
756D: 12              LD      (DE),A              
756E: 00              NOP                         
756F: 20 04           JR      NZ,$7575            ; {}
7571: 80              ADD     A,B                 
7572: 14              INC     D                   
7573: 00              NOP                         
7574: 20 03           JR      NZ,$7579            ; {}
7576: 80              ADD     A,B                 
7577: 14              INC     D                   
7578: 00              NOP                         
7579: 20 02           JR      NZ,$757D            ; {}
757B: 80              ADD     A,B                 
757C: 16 00           LD      D,$00               
757E: 20 01           JR      NZ,$7581            ; {}
7580: 80              ADD     A,B                 
7581: 16 00           LD      D,$00               
7583: 20 00           JR      NZ,$7585            ; {}
7585: 80              ADD     A,B                 
7586: 18 00           JR      $7588               ; {}
7588: 10 00           STOP    $00                 
758A: 80              ADD     A,B                 
758B: 20 3E           JR      NZ,$75CB            ; {}
758D: 07              RLCA                        
758E: EA BF D3        LD      ($D3BF),A           
7591: 21 C2 75        LD      HL,$75C2            
7594: C3 E0 79        JP      $79E0               ; {}
7597: CD 71 7A        CALL    $7A71               ; {}
759A: FE 09           CP      $09                 
759C: 28 09           JR      Z,$75A7             ; {}
759E: 21 B2 75        LD      HL,$75B2            
75A1: CD 60 7A        CALL    $7A60               ; {}
75A4: C3 21 7A        JP      $7A21               ; {}
75A7: CD A8 7A        CALL    $7AA8               ; {}
75AA: CA 03 7A        JP      Z,$7A03             ; {}
75AD: 3E 01           LD      A,$01               
75AF: 02              LD      (BC),A              
75B0: 18 EC           JR      $759E               ; {}
75B2: C7              RST     0X00                
75B3: 75              LD      (HL),L              
75B4: CA 75 CD        JP      Z,$CD75             
75B7: 75              LD      (HL),L              
75B8: D0              RET     NC                  
75B9: 75              LD      (HL),L              
75BA: D3                              
75BB: 75              LD      (HL),L              
75BC: D0              RET     NC                  
75BD: 75              LD      (HL),L              
75BE: CD 75 CA        CALL    $CA75               
75C1: 75              LD      (HL),L              
75C2: 00              NOP                         
75C3: F4                              
75C4: 0F              RRCA                        
75C5: 80              ADD     A,B                 
75C6: 01 0E 00        LD      BC,$000E            
75C9: 01 0D 00        LD      BC,$000D            
75CC: 01 0C 00        LD      BC,$000C            
75CF: 01 0B 00        LD      BC,$000B            
75D2: 01 0A 00        LD      BC,$000A            
75D5: 01 3E 07        LD      BC,$073E            
75D8: EA BF D3        LD      ($D3BF),A           
75DB: CD 2F 7A        CALL    $7A2F               ; {}
75DE: 21 17 62        LD      HL,$6217            
75E1: CD CC 7A        CALL    $7ACC               ; {}
75E4: C3 7B 7A        JP      $7A7B               ; {}
75E7: CD 71 7A        CALL    $7A71               ; {}
75EA: FE 09           CP      $09                 
75EC: 28 0A           JR      Z,$75F8             ; {}
75EE: FE 0A           CP      $0A                 
75F0: 28 0F           JR      Z,$7601             ; {}
75F2: 21 05 62        LD      HL,$6205            
75F5: C3 0D 7B        JP      $7B0D               ; {}
75F8: CD A8 7A        CALL    $7AA8               ; {}
75FB: CA 4D 7A        JP      Z,$7A4D             ; {}
75FE: 0A              LD      A,(BC)              
75FF: 18 F1           JR      $75F2               ; {}
7601: 3E 01           LD      A,$01               
7603: 02              LD      (BC),A              
7604: 18 EC           JR      $75F2               ; {}
7606: 21 43 76        LD      HL,$7643            
7609: C3 E5 79        JP      $79E5               ; {}
760C: CD 6D 7A        CALL    $7A6D               ; {}
760F: C0              RET     NZ                  
7610: CD 71 7A        CALL    $7A71               ; {}
7613: FE 12           CP      $12                 
7615: CA 03 7A        JP      Z,$7A03             ; {}
7618: 21 21 76        LD      HL,$7621            
761B: CD 60 7A        CALL    $7A60               ; {}
761E: C3 87 7A        JP      $7A87               ; {}
7621: 48              LD      C,B                 
7622: 76              HALT                        
7623: 4D              LD      C,L                 
7624: 76              HALT                        
7625: 52              LD      D,D                 
7626: 76              HALT                        
7627: 57              LD      D,A                 
7628: 76              HALT                        
7629: 5C              LD      E,H                 
762A: 76              HALT                        
762B: 61              LD      H,C                 
762C: 76              HALT                        
762D: 66              LD      H,(HL)              
762E: 76              HALT                        
762F: 6B              LD      L,E                 
7630: 76              HALT                        
7631: 70              LD      (HL),B              
7632: 76              HALT                        
7633: 75              LD      (HL),L              
7634: 76              HALT                        
7635: 7A              LD      A,D                 
7636: 76              HALT                        
7637: 7F              LD      A,A                 
7638: 76              HALT                        
7639: 84              ADD     A,H                 
763A: 76              HALT                        
763B: 89              ADC     A,C                 
763C: 76              HALT                        
763D: 8E              ADC     A,(HL)              
763E: 76              HALT                        
763F: 93              SUB     E                   
7640: 76              HALT                        
7641: 98              SBC     B                   
7642: 76              HALT                        
7643: 00              NOP                         
7644: 20 0C           JR      NZ,$7652            ; {}
7646: 80              ADD     A,B                 
7647: 01 00 40        LD      BC,$4000            
764A: 0D              DEC     C                   
764B: 80              ADD     A,B                 
764C: 01 00 60        LD      BC,$6000            
764F: 0E 80           LD      C,$80               
7651: 01 00 80        LD      BC,$8000            
7654: 0F              RRCA                        
7655: 80              ADD     A,B                 
7656: 01 00 A0        LD      BC,$A000            
7659: 1C              INC     E                   
765A: 80              ADD     A,B                 
765B: 01 00 E0        LD      BC,$E000            
765E: 1D              DEC     E                   
765F: 80              ADD     A,B                 
7660: 01 00 C0        LD      BC,$C000            
7663: 1E 80           LD      E,$80               
7665: 02              LD      (BC),A              
7666: 00              NOP                         
7667: B0              OR      B                   
7668: 1F              RRA                         
7669: 80              ADD     A,B                 
766A: 02              LD      (BC),A              
766B: 00              NOP                         
766C: A0              AND     B                   
766D: 2C              INC     L                   
766E: 80              ADD     A,B                 
766F: 02              LD      (BC),A              
7670: 00              NOP                         
7671: 90              SUB     B                   
7672: 2D              DEC     L                   
7673: 80              ADD     A,B                 
7674: 02              LD      (BC),A              
7675: 00              NOP                         
7676: 80              ADD     A,B                 
7677: 2E 80           LD      L,$80               
7679: 02              LD      (BC),A              
767A: 00              NOP                         
767B: 70              LD      (HL),B              
767C: 2F              CPL                         
767D: 80              ADD     A,B                 
767E: 02              LD      (BC),A              
767F: 00              NOP                         
7680: 60              LD      H,B                 
7681: 3C              INC     A                   
7682: 80              ADD     A,B                 
7683: 02              LD      (BC),A              
7684: 00              NOP                         
7685: 50              LD      D,B                 
7686: 3D              DEC     A                   
7687: 80              ADD     A,B                 
7688: 02              LD      (BC),A              
7689: 00              NOP                         
768A: 40              LD      B,B                 
768B: 3E 80           LD      A,$80               
768D: 02              LD      (BC),A              
768E: 00              NOP                         
768F: 30 3F           JR      NC,$76D0            ; {}
7691: 80              ADD     A,B                 
7692: 02              LD      (BC),A              
7693: 00              NOP                         
7694: 20 4C           JR      NZ,$76E2            ; {}
7696: 80              ADD     A,B                 
7697: 02              LD      (BC),A              
7698: 37              SCF                         
7699: 10 4D           STOP    $4D                 
769B: C0              RET     NZ                  
769C: 02              LD      (BC),A              
769D: 21 D2 76        LD      HL,$76D2            
76A0: C3 E5 79        JP      $79E5               ; {}
76A3: CD 6D 7A        CALL    $7A6D               ; {}
76A6: C0              RET     NZ                  
76A7: CD 71 7A        CALL    $7A71               ; {}
76AA: FE 0E           CP      $0E                 
76AC: CA 03 7A        JP      Z,$7A03             ; {}
76AF: 21 B8 76        LD      HL,$76B8            
76B2: CD 60 7A        CALL    $7A60               ; {}
76B5: C3 87 7A        JP      $7A87               ; {}
76B8: D7              RST     0X10                
76B9: 76              HALT                        
76BA: DC 76 E1        CALL    C,$E176             
76BD: 76              HALT                        
76BE: E6 76           AND     $76                 
76C0: EB                              
76C1: 76              HALT                        
76C2: F0 76           LD      A,($76)             
76C4: F5              PUSH    AF                  
76C5: 76              HALT                        
76C6: FA 76 FF        LD      A,($FF76)           
76C9: 76              HALT                        
76CA: 04              INC     B                   
76CB: 77              LD      (HL),A              
76CC: 09              ADD     HL,BC               
76CD: 77              LD      (HL),A              
76CE: 0E 77           LD      C,$77               
76D0: 13              INC     DE                  
76D1: 77              LD      (HL),A              
76D2: 00              NOP                         
76D3: 30 3D           JR      NC,$7712            ; {}
76D5: 80              ADD     A,B                 
76D6: 02              LD      (BC),A              
76D7: 00              NOP                         
76D8: 60              LD      H,B                 
76D9: 3F              CCF                         
76DA: 80              ADD     A,B                 
76DB: 02              LD      (BC),A              
76DC: 00              NOP                         
76DD: 90              SUB     B                   
76DE: 3D              DEC     A                   
76DF: 80              ADD     A,B                 
76E0: 02              LD      (BC),A              
76E1: 00              NOP                         
76E2: C0              RET     NZ                  
76E3: 3F              CCF                         
76E4: 80              ADD     A,B                 
76E5: 02              LD      (BC),A              
76E6: 00              NOP                         
76E7: F0 3D           LD      A,($3D)             
76E9: 80              ADD     A,B                 
76EA: 02              LD      (BC),A              
76EB: 00              NOP                         
76EC: D0              RET     NC                  
76ED: 3F              CCF                         
76EE: 80              ADD     A,B                 
76EF: 02              LD      (BC),A              
76F0: 00              NOP                         
76F1: B0              OR      B                   
76F2: 3D              DEC     A                   
76F3: 80              ADD     A,B                 
76F4: 02              LD      (BC),A              
76F5: 00              NOP                         
76F6: 90              SUB     B                   
76F7: 3F              CCF                         
76F8: 80              ADD     A,B                 
76F9: 02              LD      (BC),A              
76FA: 00              NOP                         
76FB: 70              LD      (HL),B              
76FC: 3D              DEC     A                   
76FD: 80              ADD     A,B                 
76FE: 03              INC     BC                  
76FF: 00              NOP                         
7700: 50              LD      D,B                 
7701: 3F              CCF                         
7702: 80              ADD     A,B                 
7703: 03              INC     BC                  
7704: 00              NOP                         
7705: 40              LD      B,B                 
7706: 3D              DEC     A                   
7707: 80              ADD     A,B                 
7708: 04              INC     B                   
7709: 00              NOP                         
770A: 30 3F           JR      NC,$774B            ; {}
770C: 80              ADD     A,B                 
770D: 04              INC     B                   
770E: 00              NOP                         
770F: 20 3D           JR      NZ,$774E            ; {}
7711: 80              ADD     A,B                 
7712: 04              INC     B                   
7713: 2F              CPL                         
7714: 10 3F           STOP    $3F                 
7716: C0              RET     NZ                  
7717: 04              INC     B                   
7718: AF              XOR     A                   
7719: EA 61 D3        LD      ($D361),A           
771C: 21 1F D3        LD      HL,$D31F            
771F: CB FE           SET     1,E                 
7721: 3E 01           LD      A,$01               
7723: EA C6 D3        LD      ($D3C6),A           
7726: 21 5A 77        LD      HL,$775A            
7729: C3 E0 79        JP      $79E0               ; {}
772C: CD 6D 7A        CALL    $7A6D               ; {}
772F: C0              RET     NZ                  
7730: CD 71 7A        CALL    $7A71               ; {}
7733: FE 03           CP      $03                 
7735: 28 11           JR      Z,$7748             ; {}
7737: 21 56 77        LD      HL,$7756            
773A: CD 60 7A        CALL    $7A60               ; {}
773D: FA 98 D3        LD      A,($D398)           
7740: FE 01           CP      $01                 
7742: CA 75 7A        JP      Z,$7A75             ; {}
7745: C3 87 7A        JP      $7A87               ; {}
7748: AF              XOR     A                   
7749: E0 10           LDFF00  ($10),A             
774B: EA C6 D3        LD      ($D3C6),A           
774E: 21 1F D3        LD      HL,$D31F            
7751: CB BE           RES     1,E                 
7753: C3 03 7A        JP      $7A03               ; {}
7756: 5F              LD      E,A                 
7757: 77              LD      (HL),A              
7758: 65              LD      H,L                 
7759: 77              LD      (HL),A              
775A: 00              NOP                         
775B: 20 70           JR      NZ,$77CD            ; {}
775D: 80              ADD     A,B                 
775E: 01 1D 51        LD      BC,$511D            
7761: 82              ADD     A,D                 
7762: 59              LD      E,C                 
7763: C7              RST     0X00                
7764: 03              INC     BC                  
7765: 00              NOP                         
7766: 42              LD      B,D                 
7767: 50              LD      D,B                 
7768: 80              ADD     A,B                 
7769: 08 AF EA        LD      ($EAAF),SP          
776C: 61              LD      H,C                 
776D: D3                              
776E: 21 1F D3        LD      HL,$D31F            
7771: CB FE           SET     1,E                 
7773: 3E 01           LD      A,$01               
7775: EA C6 D3        LD      ($D3C6),A           
7778: 21 D2 77        LD      HL,$77D2            
777B: CD E0 79        CALL    $79E0               ; {}
777E: 3E F0           LD      A,$F0               
7780: EA BF D3        LD      ($D3BF),A           
7783: 21 DC 77        LD      HL,$77DC            
7786: CD B3 7A        CALL    $7AB3               ; {}
7789: C3 75 7A        JP      $7A75               ; {}
778C: 21 E6 D3        LD      HL,$D3E6            
778F: 7E              LD      A,(HL)              
7790: A7              AND     A                   
7791: 28 29           JR      Z,$77BC             ; {}
7793: AF              XOR     A                   
7794: 77              LD      (HL),A              
7795: CD A8 7A        CALL    $7AA8               ; {}
7798: 28 22           JR      Z,$77BC             ; {}
779A: FE E0           CP      $E0                 
779C: 28 11           JR      Z,$77AF             ; {}
779E: FE D8           CP      $D8                 
77A0: 30 09           JR      NC,$77AB            ; {}
77A2: 3E 02           LD      A,$02               
77A4: 02              LD      (BC),A              
77A5: 21 CE 77        LD      HL,$77CE            
77A8: C3 DD 7A        JP      $7ADD               ; {}
77AB: 3E 01           LD      A,$01               
77AD: 18 F5           JR      $77A4               ; {}
77AF: 21 D7 77        LD      HL,$77D7            
77B2: CD 87 7A        CALL    $7A87               ; {}
77B5: 3E 01           LD      A,$01               
77B7: 01 98 D3        LD      BC,$D398            
77BA: 18 E8           JR      $77A4               ; {}
77BC: AF              XOR     A                   
77BD: EA C6 D3        LD      ($D3C6),A           
77C0: 21 1F D3        LD      HL,$D31F            
77C3: CB BE           RES     1,E                 
77C5: 21 D9 53        LD      HL,$53D9            
77C8: CD 75 7A        CALL    $7A75               ; {}
77CB: C3 FD 79        JP      $79FD               ; {}
77CE: 00              NOP                         
77CF: 02              LD      (BC),A              
77D0: 00              NOP                         
77D1: 00              NOP                         
77D2: 00              NOP                         
77D3: 1D              DEC     E                   
77D4: 20 80           JR      NZ,$7756            ; {}
77D6: 01 00 60        LD      BC,$6000            
77D9: 20 80           JR      NZ,$775B            ; {}
77DB: 01 00 40        LD      BC,$4000            
77DE: 10 A0           STOP    $A0                 
77E0: 87              ADD     A,A                 
77E1: 01 21 9F        LD      BC,$9F21            
77E4: 78              LD      A,B                 
77E5: C3 E0 79        JP      $79E0               ; {}
77E8: CD 6D 7A        CALL    $7A6D               ; {}
77EB: C0              RET     NZ                  
77EC: CD 71 7A        CALL    $7A71               ; {}
77EF: FE 51           CP      $51                 
77F1: CA FD 79        JP      Z,$79FD             ; {}
77F4: 21 FD 77        LD      HL,$77FD            
77F7: CD 60 7A        CALL    $7A60               ; {}
77FA: C3 21 7A        JP      $7A21               ; {}
77FD: A4              AND     H                   
77FE: 78              LD      A,B                 
77FF: A7              AND     A                   
7800: 78              LD      A,B                 
7801: AA              XOR     D                   
7802: 78              LD      A,B                 
7803: AD              XOR     L                   
7804: 78              LD      A,B                 
7805: B0              OR      B                   
7806: 78              LD      A,B                 
7807: B3              OR      E                   
7808: 78              LD      A,B                 
7809: B0              OR      B                   
780A: 78              LD      A,B                 
780B: AD              XOR     L                   
780C: 78              LD      A,B                 
780D: AA              XOR     D                   
780E: 78              LD      A,B                 
780F: AD              XOR     L                   
7810: 78              LD      A,B                 
7811: B0              OR      B                   
7812: 78              LD      A,B                 
7813: B3              OR      E                   
7814: 78              LD      A,B                 
7815: B6              OR      (HL)                
7816: 78              LD      A,B                 
7817: B9              CP      C                   
7818: 78              LD      A,B                 
7819: BC              CP      H                   
781A: 78              LD      A,B                 
781B: B9              CP      C                   
781C: 78              LD      A,B                 
781D: B6              OR      (HL)                
781E: 78              LD      A,B                 
781F: B3              OR      E                   
7820: 78              LD      A,B                 
7821: B6              OR      (HL)                
7822: 78              LD      A,B                 
7823: B9              CP      C                   
7824: 78              LD      A,B                 
7825: BC              CP      H                   
7826: 78              LD      A,B                 
7827: BF              CP      A                   
7828: 78              LD      A,B                 
7829: C2 78 C5        JP      NZ,$C578            
782C: 78              LD      A,B                 
782D: C2 78 BF        JP      NZ,$BF78            
7830: 78              LD      A,B                 
7831: BC              CP      H                   
7832: 78              LD      A,B                 
7833: BF              CP      A                   
7834: 78              LD      A,B                 
7835: C2 78 C5        JP      NZ,$C578            
7838: 78              LD      A,B                 
7839: C8              RET     Z                   
783A: 78              LD      A,B                 
783B: CB 78           BIT     1,E                 
783D: CE 78           ADC     $78                 
783F: CB 78           BIT     1,E                 
7841: C8              RET     Z                   
7842: 78              LD      A,B                 
7843: C5              PUSH    BC                  
7844: 78              LD      A,B                 
7845: C8              RET     Z                   
7846: 78              LD      A,B                 
7847: CB 78           BIT     1,E                 
7849: CE 78           ADC     $78                 
784B: D1              POP     DE                  
784C: 78              LD      A,B                 
784D: D4 78 D7        CALL    NC,$D778            
7850: 78              LD      A,B                 
7851: D4 78 D1        CALL    NC,$D178            
7854: 78              LD      A,B                 
7855: CE 78           ADC     $78                 
7857: D1              POP     DE                  
7858: 78              LD      A,B                 
7859: D4 78 D7        CALL    NC,$D778            
785C: 78              LD      A,B                 
785D: DA 78 DD        JP      C,$DD78             
7860: 78              LD      A,B                 
7861: E0 78           LDFF00  ($78),A             
7863: DD                              
7864: 78              LD      A,B                 
7865: DA 78 D7        JP      C,$D778             
7868: 78              LD      A,B                 
7869: DA 78 DD        JP      C,$DD78             
786C: 78              LD      A,B                 
786D: E0 78           LDFF00  ($78),A             
786F: E3                              
7870: 78              LD      A,B                 
7871: E6 78           AND     $78                 
7873: E9              JP      (HL)                
7874: 78              LD      A,B                 
7875: E6 78           AND     $78                 
7877: E3                              
7878: 78              LD      A,B                 
7879: E0 78           LDFF00  ($78),A             
787B: E3                              
787C: 78              LD      A,B                 
787D: E6 78           AND     $78                 
787F: E9              JP      (HL)                
7880: 78              LD      A,B                 
7881: EC                              
7882: 78              LD      A,B                 
7883: EF              RST     0X28                
7884: 78              LD      A,B                 
7885: F2                              
7886: 78              LD      A,B                 
7887: EF              RST     0X28                
7888: 78              LD      A,B                 
7889: EC                              
788A: 78              LD      A,B                 
788B: E9              JP      (HL)                
788C: 78              LD      A,B                 
788D: EC                              
788E: 78              LD      A,B                 
788F: EF              RST     0X28                
7890: 78              LD      A,B                 
7891: F2                              
7892: 78              LD      A,B                 
7893: F5              PUSH    AF                  
7894: 78              LD      A,B                 
7895: F8 78           LDHL    SP,$78              
7897: FB              EI                          
7898: 78              LD      A,B                 
7899: FE 78           CP      $78                 
789B: FB              EI                          
789C: 78              LD      A,B                 
789D: FE 78           CP      $78                 
789F: 38 80           JR      C,$7821             ; {}
78A1: 24              INC     H                   
78A2: 80              ADD     A,B                 
78A3: 02              LD      (BC),A              
78A4: 25              DEC     H                   
78A5: 80              ADD     A,B                 
78A6: 02              LD      (BC),A              
78A7: 26 80           LD      H,$80               
78A9: 02              LD      (BC),A              
78AA: 27              DAA                         
78AB: 80              ADD     A,B                 
78AC: 02              LD      (BC),A              
78AD: 34              INC     (HL)                
78AE: 80              ADD     A,B                 
78AF: 02              LD      (BC),A              
78B0: 35              DEC     (HL)                
78B1: 80              ADD     A,B                 
78B2: 02              LD      (BC),A              
78B3: 36 80           LD      (HL),$80            
78B5: 02              LD      (BC),A              
78B6: 37              SCF                         
78B7: 80              ADD     A,B                 
78B8: 02              LD      (BC),A              
78B9: 44              LD      B,H                 
78BA: 80              ADD     A,B                 
78BB: 02              LD      (BC),A              
78BC: 45              LD      B,L                 
78BD: 80              ADD     A,B                 
78BE: 02              LD      (BC),A              
78BF: 46              LD      B,(HL)              
78C0: 80              ADD     A,B                 
78C1: 02              LD      (BC),A              
78C2: 47              LD      B,A                 
78C3: 80              ADD     A,B                 
78C4: 02              LD      (BC),A              
78C5: 3C              INC     A                   
78C6: 80              ADD     A,B                 
78C7: 03              INC     BC                  
78C8: 3D              DEC     A                   
78C9: 80              ADD     A,B                 
78CA: 03              INC     BC                  
78CB: 3E 80           LD      A,$80               
78CD: 03              INC     BC                  
78CE: 3F              CCF                         
78CF: 80              ADD     A,B                 
78D0: 03              INC     BC                  
78D1: 4C              LD      C,H                 
78D2: 80              ADD     A,B                 
78D3: 03              INC     BC                  
78D4: 4D              LD      C,L                 
78D5: 80              ADD     A,B                 
78D6: 03              INC     BC                  
78D7: 4E              LD      C,(HL)              
78D8: 80              ADD     A,B                 
78D9: 03              INC     BC                  
78DA: 4F              LD      C,A                 
78DB: 80              ADD     A,B                 
78DC: 03              INC     BC                  
78DD: 5C              LD      E,H                 
78DE: 80              ADD     A,B                 
78DF: 03              INC     BC                  
78E0: 5D              LD      E,L                 
78E1: 80              ADD     A,B                 
78E2: 03              INC     BC                  
78E3: 5E              LD      E,(HL)              
78E4: 80              ADD     A,B                 
78E5: 03              INC     BC                  
78E6: 5F              LD      E,A                 
78E7: 80              ADD     A,B                 
78E8: 03              INC     BC                  
78E9: 6C              LD      L,H                 
78EA: 80              ADD     A,B                 
78EB: 03              INC     BC                  
78EC: 6D              LD      L,L                 
78ED: C0              RET     NZ                  
78EE: 03              INC     BC                  
78EF: 6E              LD      L,(HL)              
78F0: C0              RET     NZ                  
78F1: 03              INC     BC                  
78F2: 6F              LD      L,A                 
78F3: C0              RET     NZ                  
78F4: 03              INC     BC                  
78F5: 7C              LD      A,H                 
78F6: C0              RET     NZ                  
78F7: 03              INC     BC                  
78F8: 7D              LD      A,L                 
78F9: C0              RET     NZ                  
78FA: 03              INC     BC                  
78FB: 7E              LD      A,(HL)              
78FC: C0              RET     NZ                  
78FD: 03              INC     BC                  
78FE: 7F              LD      A,A                 
78FF: C0              RET     NZ                  
7900: 03              INC     BC                  
7901: 21 2F 79        LD      HL,$792F            
7904: C3 E0 79        JP      $79E0               ; {}
7907: FA E8 D3        LD      A,($D3E8)           
790A: A7              AND     A                   
790B: C0              RET     NZ                  
790C: CD 6D 7A        CALL    $7A6D               ; {}
790F: C0              RET     NZ                  
7910: CD 71 7A        CALL    $7A71               ; {}
7913: FE 08           CP      $08                 
7915: CA 03 7A        JP      Z,$7A03             ; {}
7918: 21 21 79        LD      HL,$7921            
791B: CD 60 7A        CALL    $7A60               ; {}
791E: C3 87 7A        JP      $7A87               ; {}
7921: 34              INC     (HL)                
7922: 79              LD      A,C                 
7923: 39              ADD     HL,SP               
7924: 79              LD      A,C                 
7925: 3E 79           LD      A,$79               
7927: 43              LD      B,E                 
7928: 79              LD      A,C                 
7929: 48              LD      C,B                 
792A: 79              LD      A,C                 
792B: 4D              LD      C,L                 
792C: 79              LD      A,C                 
792D: 52              LD      D,D                 
792E: 79              LD      A,C                 
792F: 00              NOP                         
7930: 1F              RRA                         
7931: 7F              LD      A,A                 
7932: 80              ADD     A,B                 
7933: 01 00 E0        LD      BC,$E000            
7936: 44              LD      B,H                 
7937: 80              ADD     A,B                 
7938: 06 00           LD      B,$00               
793A: C0              RET     NZ                  
793B: 45              LD      B,L                 
793C: 80              ADD     A,B                 
793D: 06 00           LD      B,$00               
793F: A0              AND     B                   
7940: 46              LD      B,(HL)              
7941: 80              ADD     A,B                 
7942: 06 00           LD      B,$00               
7944: 80              ADD     A,B                 
7945: 47              LD      B,A                 
7946: 80              ADD     A,B                 
7947: 06 00           LD      B,$00               
7949: 60              LD      H,B                 
794A: 54              LD      D,H                 
794B: 80              ADD     A,B                 
794C: 06 00           LD      B,$00               
794E: 40              LD      B,B                 
794F: 55              LD      D,L                 
7950: 80              ADD     A,B                 
7951: 06 38           LD      B,$38               
7953: 20 56           JR      NZ,$79AB            ; {}
7955: C0              RET     NZ                  
7956: 06 21           LD      B,$21               
7958: 90              SUB     B                   
7959: 79              LD      A,C                 
795A: C3 E0 79        JP      $79E0               ; {}
795D: CD 6D 7A        CALL    $7A6D               ; {}
7960: C0              RET     NZ                  
7961: CD 71 7A        CALL    $7A71               ; {}
7964: FE 10           CP      $10                 
7966: CA 03 7A        JP      Z,$7A03             ; {}
7969: 21 72 79        LD      HL,$7972            
796C: CD 60 7A        CALL    $7A60               ; {}
796F: C3 87 7A        JP      $7A87               ; {}
7972: 95              SUB     L                   
7973: 79              LD      A,C                 
7974: 9A              SBC     D                   
7975: 79              LD      A,C                 
7976: 9F              SBC     A                   
7977: 79              LD      A,C                 
7978: A4              AND     H                   
7979: 79              LD      A,C                 
797A: A9              XOR     C                   
797B: 79              LD      A,C                 
797C: AE              XOR     (HL)                
797D: 79              LD      A,C                 
797E: B3              OR      E                   
797F: 79              LD      A,C                 
7980: B8              CP      B                   
7981: 79              LD      A,C                 
7982: BD              CP      L                   
7983: 79              LD      A,C                 
7984: C2 79 C7        JP      NZ,$C779            
7987: 79              LD      A,C                 
7988: CC 79 D1        CALL    Z,$D179             
798B: 79              LD      A,C                 
798C: D6 79           SUB     $79                 
798E: DB                              
798F: 79              LD      A,C                 
7990: 00              NOP                         
7991: 20 27           JR      NZ,$79BA            ; {}
7993: 80              ADD     A,B                 
7994: 02              LD      (BC),A              
7995: 00              NOP                         
7996: 40              LD      B,B                 
7997: 25              DEC     H                   
7998: 80              ADD     A,B                 
7999: 02              LD      (BC),A              
799A: 00              NOP                         
799B: 60              LD      H,B                 
799C: 17              RLA                         
799D: 80              ADD     A,B                 
799E: 02              LD      (BC),A              
799F: 00              NOP                         
79A0: 80              ADD     A,B                 
79A1: 15              DEC     D                   
79A2: 80              ADD     A,B                 
79A3: 02              LD      (BC),A              
79A4: 00              NOP                         
79A5: A0              AND     B                   
79A6: 17              RLA                         
79A7: 80              ADD     A,B                 
79A8: 02              LD      (BC),A              
79A9: 00              NOP                         
79AA: C0              RET     NZ                  
79AB: 25              DEC     H                   
79AC: 80              ADD     A,B                 
79AD: 04              INC     B                   
79AE: 00              NOP                         
79AF: B0              OR      B                   
79B0: 27              DAA                         
79B1: 80              ADD     A,B                 
79B2: 04              INC     B                   
79B3: 00              NOP                         
79B4: A0              AND     B                   
79B5: 25              DEC     H                   
79B6: 80              ADD     A,B                 
79B7: 04              INC     B                   
79B8: 00              NOP                         
79B9: 90              SUB     B                   
79BA: 17              RLA                         
79BB: 80              ADD     A,B                 
79BC: 04              INC     B                   
79BD: 00              NOP                         
79BE: 80              ADD     A,B                 
79BF: 15              DEC     D                   
79C0: C0              RET     NZ                  
79C1: 04              INC     B                   
79C2: 00              NOP                         
79C3: 70              LD      (HL),B              
79C4: 17              RLA                         
79C5: 80              ADD     A,B                 
79C6: 04              INC     B                   
79C7: 00              NOP                         
79C8: 60              LD      H,B                 
79C9: 25              DEC     H                   
79CA: 80              ADD     A,B                 
79CB: 04              INC     B                   
79CC: 00              NOP                         
79CD: 50              LD      D,B                 
79CE: 27              DAA                         
79CF: 80              ADD     A,B                 
79D0: 04              INC     B                   
79D1: 00              NOP                         
79D2: 40              LD      B,B                 
79D3: 25              DEC     H                   
79D4: 80              ADD     A,B                 
79D5: 04              INC     B                   
79D6: 00              NOP                         
79D7: 30 17           JR      NC,$79F0            ; {}
79D9: 80              ADD     A,B                 
79DA: 04              INC     B                   
79DB: 2F              CPL                         
79DC: 20 15           JR      NZ,$79F3            ; {}
79DE: C0              RET     NZ                  
79DF: 04              INC     B                   
79E0: 3E 01           LD      A,$01               
79E2: EA C9 D3        LD      ($D3C9),A           
79E5: FA 78 D3        LD      A,($D378)           
79E8: EA 79 D3        LD      ($D379),A           
79EB: AF              XOR     A                   
79EC: EA 93 D3        LD      ($D393),A           
79EF: EA 98 D3        LD      ($D398),A           
79F2: FA 4F D3        LD      A,($D34F)           
79F5: CB FF           SET     1,E                 
79F7: EA 4F D3        LD      ($D34F),A           
79FA: C3 87 7A        JP      $7A87               ; {}
79FD: 21 1C 7A        LD      HL,$7A1C            
7A00: CD 87 7A        CALL    $7A87               ; {}
7A03: AF              XOR     A                   
7A04: EA 79 D3        LD      ($D379),A           
7A07: EA 93 D3        LD      ($D393),A           
7A0A: EA 98 D3        LD      ($D398),A           
7A0D: EA BF D3        LD      ($D3BF),A           
7A10: EA C9 D3        LD      ($D3C9),A           
7A13: FA 4F D3        LD      A,($D34F)           
7A16: CB BF           RES     1,E                 
7A18: EA 4F D3        LD      ($D34F),A           
7A1B: C9              RET                         
7A1C: 00              NOP                         
7A1D: 00              NOP                         
7A1E: 00              NOP                         
7A1F: 00              NOP                         
7A20: 01 06 02        LD      BC,$0206            
7A23: 0E 22           LD      C,$22               
7A25: C3 8D 7A        JP      $7A8D               ; {}
7A28: AF              XOR     A                   
7A29: EA 78 D3        LD      ($D378),A           
7A2C: C3 E8 64        JP      $64E8               ; {}
7A2F: FA 78 D3        LD      A,($D378)           
7A32: EA 79 D3        LD      ($D379),A           
7A35: 21 2F D3        LD      HL,$D32F            
7A38: CB FE           SET     1,E                 
7A3A: 3E 01           LD      A,$01               
7A3C: EA C9 D3        LD      ($D3C9),A           
7A3F: AF              XOR     A                   
7A40: EA 93 D3        LD      ($D393),A           
7A43: EA 98 D3        LD      ($D398),A           
7A46: 21 1C 7A        LD      HL,$7A1C            
7A49: CD 87 7A        CALL    $7A87               ; {}
7A4C: C9              RET                         
7A4D: AF              XOR     A                   
7A4E: EA 93 D3        LD      ($D393),A           
7A51: EA 98 D3        LD      ($D398),A           
7A54: EA 79 D3        LD      ($D379),A           
7A57: EA C9 D3        LD      ($D3C9),A           
7A5A: 21 2F D3        LD      HL,$D32F            
7A5D: CB BE           RES     1,E                 
7A5F: C9              RET                         
7A60: 3D              DEC     A                   
7A61: CB 27           SLA     1,E                 
7A63: 4F              LD      C,A                 
7A64: 06 00           LD      B,$00               
7A66: 09              ADD     HL,BC               
7A67: 4E              LD      C,(HL)              
7A68: 23              INC     HL                  
7A69: 46              LD      B,(HL)              
7A6A: 60              LD      H,B                 
7A6B: 69              LD      L,C                 
7A6C: C9              RET                         
7A6D: 1A              LD      A,(DE)              
7A6E: 3D              DEC     A                   
7A6F: 12              LD      (DE),A              
7A70: C9              RET                         
7A71: 0A              LD      A,(BC)              
7A72: 3C              INC     A                   
7A73: 02              LD      (BC),A              
7A74: C9              RET                         
7A75: 06 05           LD      B,$05               
7A77: 0E 10           LD      C,$10               
7A79: 18 12           JR      $7A8D               ; {}
7A7B: 06 04           LD      B,$04               
7A7D: 0E 16           LD      C,$16               
7A7F: 18 0C           JR      $7A8D               ; {}
7A81: 06 05           LD      B,$05               
7A83: 0E 1A           LD      C,$1A               
7A85: 18 06           JR      $7A8D               ; {}
7A87: 06 04           LD      B,$04               
7A89: 0E 20           LD      C,$20               
7A8B: 18 00           JR      $7A8D               ; {}
7A8D: 2A              LD      A,(HLI)             
7A8E: E2              LDFF00  (C),A               
7A8F: 0C              INC     C                   
7A90: 05              DEC     B                   
7A91: 20 FA           JR      NZ,$7A8D            ; {}
7A93: 7E              LD      A,(HL)              
7A94: 12              LD      (DE),A              
7A95: C9              RET                         
7A96: D5              PUSH    DE                  
7A97: 11 BC D3        LD      DE,$D3BC            
7A9A: 18 12           JR      $7AAE               ; {}
7A9C: D5              PUSH    DE                  
7A9D: 11 BD D3        LD      DE,$D3BD            
7AA0: 18 0C           JR      $7AAE               ; {}
7AA2: D5              PUSH    DE                  
7AA3: 11 BE D3        LD      DE,$D3BE            
7AA6: 18 06           JR      $7AAE               ; {}
7AA8: D5              PUSH    DE                  
7AA9: 11 BF D3        LD      DE,$D3BF            
7AAC: 18 00           JR      $7AAE               ; {}
7AAE: CD 6D 7A        CALL    $7A6D               ; {}
7AB1: D1              POP     DE                  
7AB2: C9              RET                         
7AB3: D5              PUSH    DE                  
7AB4: 11 C0 D3        LD      DE,$D3C0            
7AB7: 18 04           JR      $7ABD               ; {}
7AB9: D5              PUSH    DE                  
7ABA: 11 C4 D3        LD      DE,$D3C4            
7ABD: 23              INC     HL                  
7ABE: 23              INC     HL                  
7ABF: 23              INC     HL                  
7AC0: 2A              LD      A,(HLI)             
7AC1: 12              LD      (DE),A              
7AC2: 1C              INC     E                   
7AC3: 3A              LD      A,(HLD)             
7AC4: E6 0F           AND     $0F                 
7AC6: 12              LD      (DE),A              
7AC7: 2B              DEC     HL                  
7AC8: 2B              DEC     HL                  
7AC9: 2B              DEC     HL                  
7ACA: D1              POP     DE                  
7ACB: C9              RET                         
7ACC: D5              PUSH    DE                  
7ACD: 11 C2 D3        LD      DE,$D3C2            
7AD0: 23              INC     HL                  
7AD1: 23              INC     HL                  
7AD2: 2A              LD      A,(HLI)             
7AD3: 12              LD      (DE),A              
7AD4: 1C              INC     E                   
7AD5: 3A              LD      A,(HLD)             
7AD6: E6 0F           AND     $0F                 
7AD8: 12              LD      (DE),A              
7AD9: 2B              DEC     HL                  
7ADA: 2B              DEC     HL                  
7ADB: D1              POP     DE                  
7ADC: C9              RET                         
7ADD: D5              PUSH    DE                  
7ADE: 11 C1 D3        LD      DE,$D3C1            
7AE1: 0A              LD      A,(BC)              
7AE2: 0E 13           LD      C,$13               
7AE4: C5              PUSH    BC                  
7AE5: 18 0A           JR      $7AF1               ; {}
7AE7: D5              PUSH    DE                  
7AE8: 11 C5 D3        LD      DE,$D3C5            
7AEB: 0A              LD      A,(BC)              
7AEC: 0E 1D           LD      C,$1D               
7AEE: C5              PUSH    BC                  
7AEF: 18 00           JR      $7AF1               ; {}
7AF1: 3D              DEC     A                   
7AF2: CB 27           SLA     1,E                 
7AF4: 4F              LD      C,A                 
7AF5: 06 00           LD      B,$00               
7AF7: 09              ADD     HL,BC               
7AF8: 2A              LD      A,(HLI)             
7AF9: 47              LD      B,A                 
7AFA: 7E              LD      A,(HL)              
7AFB: 4F              LD      C,A                 
7AFC: 1A              LD      A,(DE)              
7AFD: 1D              DEC     E                   
7AFE: 67              LD      H,A                 
7AFF: 1A              LD      A,(DE)              
7B00: 6F              LD      L,A                 
7B01: 09              ADD     HL,BC               
7B02: C1              POP     BC                  
7B03: 7D              LD      A,L                 
7B04: E2              LDFF00  (C),A               
7B05: 12              LD      (DE),A              
7B06: 0C              INC     C                   
7B07: 1C              INC     E                   
7B08: 7C              LD      A,H                 
7B09: E2              LDFF00  (C),A               
7B0A: 12              LD      (DE),A              
7B0B: D1              POP     DE                  
7B0C: C9              RET                         
7B0D: D5              PUSH    DE                  
7B0E: 11 C3 D3        LD      DE,$D3C3            
7B11: 0A              LD      A,(BC)              
7B12: 0E 18           LD      C,$18               
7B14: C5              PUSH    BC                  
7B15: 18 DA           JR      $7AF1               ; {}
7B17: 3E FF           LD      A,$FF               
7B19: E0 25           LDFF00  ($25),A             
7B1B: 3E 03           LD      A,$03               
7B1D: EA 55 D3        LD      ($D355),A           
7B20: AF              XOR     A                   
7B21: EA 69 D3        LD      ($D369),A           
7B24: AF              XOR     A                   
7B25: EA 61 D3        LD      ($D361),A           
7B28: EA 71 D3        LD      ($D371),A           
7B2B: EA 79 D3        LD      ($D379),A           
7B2E: EA 1F D3        LD      ($D31F),A           
7B31: EA 2F D3        LD      ($D32F),A           
7B34: EA 3F D3        LD      ($D33F),A           
7B37: EA 4F D3        LD      ($D34F),A           
7B3A: EA 9E D3        LD      ($D39E),A           
7B3D: EA 9F D3        LD      ($D39F),A           
7B40: EA D9 D3        LD      ($D3D9),A           
7B43: EA DA D3        LD      ($D3DA),A           
7B46: EA B6 D3        LD      ($D3B6),A           
7B49: EA B7 D3        LD      ($D3B7),A           
7B4C: EA B8 D3        LD      ($D3B8),A           
7B4F: EA B9 D3        LD      ($D3B9),A           
7B52: EA BA D3        LD      ($D3BA),A           
7B55: EA BB D3        LD      ($D3BB),A           
7B58: EA 94 D3        LD      ($D394),A           
7B5B: EA 95 D3        LD      ($D395),A           
7B5E: EA 96 D3        LD      ($D396),A           
7B61: EA 98 D3        LD      ($D398),A           
7B64: EA 90 D3        LD      ($D390),A           
7B67: EA 91 D3        LD      ($D391),A           
7B6A: EA 92 D3        LD      ($D392),A           
7B6D: EA 93 D3        LD      ($D393),A           
7B70: EA C6 D3        LD      ($D3C6),A           
7B73: EA C7 D3        LD      ($D3C7),A           
7B76: EA C8 D3        LD      ($D3C8),A           
7B79: EA C9 D3        LD      ($D3C9),A           
7B7C: EA A0 D3        LD      ($D3A0),A           
7B7F: EA A1 D3        LD      ($D3A1),A           
7B82: EA A2 D3        LD      ($D3A2),A           
7B85: EA A3 D3        LD      ($D3A3),A           
7B88: EA CD D3        LD      ($D3CD),A           
7B8B: EA D6 D3        LD      ($D3D6),A           
7B8E: EA D7 D3        LD      ($D3D7),A           
7B91: EA D8 D3        LD      ($D3D8),A           
7B94: EA DC D3        LD      ($D3DC),A           
7B97: EA E7 D3        LD      ($D3E7),A           
7B9A: EA E2 D3        LD      ($D3E2),A           
7B9D: EA E3 D3        LD      ($D3E3),A           
7BA0: EA E4 D3        LD      ($D3E4),A           
7BA3: EA E5 D3        LD      ($D3E5),A           
7BA6: 3E 08           LD      A,$08               
7BA8: E0 12           LDFF00  ($12),A             
7BAA: E0 17           LDFF00  ($17),A             
7BAC: E0 21           LDFF00  ($21),A             
7BAE: 3E 80           LD      A,$80               
7BB0: E0 14           LDFF00  ($14),A             
7BB2: E0 19           LDFF00  ($19),A             
7BB4: E0 23           LDFF00  ($23),A             
7BB6: AF              XOR     A                   
7BB7: E0 10           LDFF00  ($10),A             
7BB9: E0 1A           LDFF00  ($1A),A             
7BBB: C9              RET                         
7BBC: FF              RST     0X38                
7BBD: FF              RST     0X38                
7BBE: FF              RST     0X38                
7BBF: FF              RST     0X38                
7BC0: FF              RST     0X38                
7BC1: FF              RST     0X38                
7BC2: FF              RST     0X38                
7BC3: FF              RST     0X38                
7BC4: FF              RST     0X38                
7BC5: FF              RST     0X38                
7BC6: FF              RST     0X38                
7BC7: FF              RST     0X38                
7BC8: FF              RST     0X38                
7BC9: FF              RST     0X38                
7BCA: FF              RST     0X38                
7BCB: FF              RST     0X38                
7BCC: FF              RST     0X38                
7BCD: FF              RST     0X38                
7BCE: FF              RST     0X38                
7BCF: FF              RST     0X38                
7BD0: FF              RST     0X38                
7BD1: FF              RST     0X38                
7BD2: FF              RST     0X38                
7BD3: FF              RST     0X38                
7BD4: FF              RST     0X38                
7BD5: FF              RST     0X38                
7BD6: FF              RST     0X38                
7BD7: FF              RST     0X38                
7BD8: FF              RST     0X38                
7BD9: FF              RST     0X38                
7BDA: FF              RST     0X38                
7BDB: FF              RST     0X38                
7BDC: FF              RST     0X38                
7BDD: FF              RST     0X38                
7BDE: FF              RST     0X38                
7BDF: FF              RST     0X38                
7BE0: FF              RST     0X38                
7BE1: FF              RST     0X38                
7BE2: FF              RST     0X38                
7BE3: FF              RST     0X38                
7BE4: FF              RST     0X38                
7BE5: FF              RST     0X38                
7BE6: FF              RST     0X38                
7BE7: FF              RST     0X38                
7BE8: FF              RST     0X38                
7BE9: FF              RST     0X38                
7BEA: FF              RST     0X38                
7BEB: FF              RST     0X38                
7BEC: FF              RST     0X38                
7BED: FF              RST     0X38                
7BEE: FF              RST     0X38                
7BEF: FF              RST     0X38                
7BF0: FF              RST     0X38                
7BF1: FF              RST     0X38                
7BF2: FF              RST     0X38                
7BF3: FF              RST     0X38                
7BF4: FF              RST     0X38                
7BF5: FF              RST     0X38                
7BF6: FF              RST     0X38                
7BF7: FF              RST     0X38                
7BF8: FF              RST     0X38                
7BF9: FF              RST     0X38                
7BFA: FF              RST     0X38                
7BFB: FF              RST     0X38                
7BFC: FF              RST     0X38                
7BFD: FF              RST     0X38                
7BFE: FF              RST     0X38                
7BFF: FF              RST     0X38                
7C00: FF              RST     0X38                
7C01: FF              RST     0X38                
7C02: FF              RST     0X38                
7C03: FF              RST     0X38                
7C04: FF              RST     0X38                
7C05: FF              RST     0X38                
7C06: FF              RST     0X38                
7C07: FF              RST     0X38                
7C08: FF              RST     0X38                
7C09: FF              RST     0X38                
7C0A: FF              RST     0X38                
7C0B: FF              RST     0X38                
7C0C: FF              RST     0X38                
7C0D: FF              RST     0X38                
7C0E: FF              RST     0X38                
7C0F: FF              RST     0X38                
7C10: FF              RST     0X38                
7C11: FF              RST     0X38                
7C12: FF              RST     0X38                
7C13: FF              RST     0X38                
7C14: FF              RST     0X38                
7C15: FF              RST     0X38                
7C16: FF              RST     0X38                
7C17: FF              RST     0X38                
7C18: FF              RST     0X38                
7C19: FF              RST     0X38                
7C1A: FF              RST     0X38                
7C1B: FF              RST     0X38                
7C1C: FF              RST     0X38                
7C1D: FF              RST     0X38                
7C1E: FF              RST     0X38                
7C1F: FF              RST     0X38                
7C20: FF              RST     0X38                
7C21: FF              RST     0X38                
7C22: FF              RST     0X38                
7C23: FF              RST     0X38                
7C24: FF              RST     0X38                
7C25: FF              RST     0X38                
7C26: FF              RST     0X38                
7C27: FF              RST     0X38                
7C28: FF              RST     0X38                
7C29: FF              RST     0X38                
7C2A: FF              RST     0X38                
7C2B: FF              RST     0X38                
7C2C: FF              RST     0X38                
7C2D: FF              RST     0X38                
7C2E: FF              RST     0X38                
7C2F: FF              RST     0X38                
7C30: FF              RST     0X38                
7C31: FF              RST     0X38                
7C32: FF              RST     0X38                
7C33: FF              RST     0X38                
7C34: FF              RST     0X38                
7C35: FF              RST     0X38                
7C36: FF              RST     0X38                
7C37: FF              RST     0X38                
7C38: FF              RST     0X38                
7C39: FF              RST     0X38                
7C3A: FF              RST     0X38                
7C3B: FF              RST     0X38                
7C3C: FF              RST     0X38                
7C3D: FF              RST     0X38                
7C3E: FF              RST     0X38                
7C3F: FF              RST     0X38                
7C40: FF              RST     0X38                
7C41: FF              RST     0X38                
7C42: FF              RST     0X38                
7C43: FF              RST     0X38                
7C44: FF              RST     0X38                
7C45: FF              RST     0X38                
7C46: FF              RST     0X38                
7C47: FF              RST     0X38                
7C48: FF              RST     0X38                
7C49: FF              RST     0X38                
7C4A: FF              RST     0X38                
7C4B: FF              RST     0X38                
7C4C: FF              RST     0X38                
7C4D: FF              RST     0X38                
7C4E: FF              RST     0X38                
7C4F: FF              RST     0X38                
7C50: FF              RST     0X38                
7C51: FF              RST     0X38                
7C52: FF              RST     0X38                
7C53: FF              RST     0X38                
7C54: FF              RST     0X38                
7C55: FF              RST     0X38                
7C56: FF              RST     0X38                
7C57: FF              RST     0X38                
7C58: FF              RST     0X38                
7C59: FF              RST     0X38                
7C5A: FF              RST     0X38                
7C5B: FF              RST     0X38                
7C5C: FF              RST     0X38                
7C5D: FF              RST     0X38                
7C5E: FF              RST     0X38                
7C5F: FF              RST     0X38                
7C60: FF              RST     0X38                
7C61: FF              RST     0X38                
7C62: FF              RST     0X38                
7C63: FF              RST     0X38                
7C64: FF              RST     0X38                
7C65: FF              RST     0X38                
7C66: FF              RST     0X38                
7C67: FF              RST     0X38                
7C68: FF              RST     0X38                
7C69: FF              RST     0X38                
7C6A: FF              RST     0X38                
7C6B: FF              RST     0X38                
7C6C: FF              RST     0X38                
7C6D: FF              RST     0X38                
7C6E: FF              RST     0X38                
7C6F: FF              RST     0X38                
7C70: FF              RST     0X38                
7C71: FF              RST     0X38                
7C72: FF              RST     0X38                
7C73: FF              RST     0X38                
7C74: FF              RST     0X38                
7C75: FF              RST     0X38                
7C76: FF              RST     0X38                
7C77: FF              RST     0X38                
7C78: FF              RST     0X38                
7C79: FF              RST     0X38                
7C7A: FF              RST     0X38                
7C7B: FF              RST     0X38                
7C7C: FF              RST     0X38                
7C7D: FF              RST     0X38                
7C7E: FF              RST     0X38                
7C7F: FF              RST     0X38                
7C80: FF              RST     0X38                
7C81: FF              RST     0X38                
7C82: FF              RST     0X38                
7C83: FF              RST     0X38                
7C84: FF              RST     0X38                
7C85: FF              RST     0X38                
7C86: FF              RST     0X38                
7C87: FF              RST     0X38                
7C88: FF              RST     0X38                
7C89: FF              RST     0X38                
7C8A: FF              RST     0X38                
7C8B: FF              RST     0X38                
7C8C: FF              RST     0X38                
7C8D: FF              RST     0X38                
7C8E: FF              RST     0X38                
7C8F: FF              RST     0X38                
7C90: FF              RST     0X38                
7C91: FF              RST     0X38                
7C92: FF              RST     0X38                
7C93: FF              RST     0X38                
7C94: FF              RST     0X38                
7C95: FF              RST     0X38                
7C96: FF              RST     0X38                
7C97: FF              RST     0X38                
7C98: FF              RST     0X38                
7C99: FF              RST     0X38                
7C9A: FF              RST     0X38                
7C9B: FF              RST     0X38                
7C9C: FF              RST     0X38                
7C9D: FF              RST     0X38                
7C9E: FF              RST     0X38                
7C9F: FF              RST     0X38                
7CA0: FF              RST     0X38                
7CA1: FF              RST     0X38                
7CA2: FF              RST     0X38                
7CA3: FF              RST     0X38                
7CA4: FF              RST     0X38                
7CA5: FF              RST     0X38                
7CA6: FF              RST     0X38                
7CA7: FF              RST     0X38                
7CA8: FF              RST     0X38                
7CA9: FF              RST     0X38                
7CAA: FF              RST     0X38                
7CAB: FF              RST     0X38                
7CAC: FF              RST     0X38                
7CAD: FF              RST     0X38                
7CAE: FF              RST     0X38                
7CAF: FF              RST     0X38                
7CB0: FF              RST     0X38                
7CB1: FF              RST     0X38                
7CB2: FF              RST     0X38                
7CB3: FF              RST     0X38                
7CB4: FF              RST     0X38                
7CB5: FF              RST     0X38                
7CB6: FF              RST     0X38                
7CB7: FF              RST     0X38                
7CB8: FF              RST     0X38                
7CB9: FF              RST     0X38                
7CBA: FF              RST     0X38                
7CBB: FF              RST     0X38                
7CBC: FF              RST     0X38                
7CBD: FF              RST     0X38                
7CBE: FF              RST     0X38                
7CBF: FF              RST     0X38                
7CC0: FF              RST     0X38                
7CC1: FF              RST     0X38                
7CC2: FF              RST     0X38                
7CC3: FF              RST     0X38                
7CC4: FF              RST     0X38                
7CC5: FF              RST     0X38                
7CC6: FF              RST     0X38                
7CC7: FF              RST     0X38                
7CC8: FF              RST     0X38                
7CC9: FF              RST     0X38                
7CCA: FF              RST     0X38                
7CCB: FF              RST     0X38                
7CCC: FF              RST     0X38                
7CCD: FF              RST     0X38                
7CCE: FF              RST     0X38                
7CCF: FF              RST     0X38                
7CD0: FF              RST     0X38                
7CD1: FF              RST     0X38                
7CD2: FF              RST     0X38                
7CD3: FF              RST     0X38                
7CD4: FF              RST     0X38                
7CD5: FF              RST     0X38                
7CD6: FF              RST     0X38                
7CD7: FF              RST     0X38                
7CD8: FF              RST     0X38                
7CD9: FF              RST     0X38                
7CDA: FF              RST     0X38                
7CDB: FF              RST     0X38                
7CDC: FF              RST     0X38                
7CDD: FF              RST     0X38                
7CDE: FF              RST     0X38                
7CDF: FF              RST     0X38                
7CE0: FF              RST     0X38                
7CE1: FF              RST     0X38                
7CE2: FF              RST     0X38                
7CE3: FF              RST     0X38                
7CE4: FF              RST     0X38                
7CE5: FF              RST     0X38                
7CE6: FF              RST     0X38                
7CE7: FF              RST     0X38                
7CE8: FF              RST     0X38                
7CE9: FF              RST     0X38                
7CEA: FF              RST     0X38                
7CEB: FF              RST     0X38                
7CEC: FF              RST     0X38                
7CED: FF              RST     0X38                
7CEE: FF              RST     0X38                
7CEF: FF              RST     0X38                
7CF0: FF              RST     0X38                
7CF1: FF              RST     0X38                
7CF2: FF              RST     0X38                
7CF3: FF              RST     0X38                
7CF4: FF              RST     0X38                
7CF5: FF              RST     0X38                
7CF6: FF              RST     0X38                
7CF7: FF              RST     0X38                
7CF8: FF              RST     0X38                
7CF9: FF              RST     0X38                
7CFA: FF              RST     0X38                
7CFB: FF              RST     0X38                
7CFC: FF              RST     0X38                
7CFD: FF              RST     0X38                
7CFE: FF              RST     0X38                
7CFF: FF              RST     0X38                
7D00: FF              RST     0X38                
7D01: FF              RST     0X38                
7D02: FF              RST     0X38                
7D03: FF              RST     0X38                
7D04: FF              RST     0X38                
7D05: FF              RST     0X38                
7D06: FF              RST     0X38                
7D07: FF              RST     0X38                
7D08: FF              RST     0X38                
7D09: FF              RST     0X38                
7D0A: FF              RST     0X38                
7D0B: FF              RST     0X38                
7D0C: FF              RST     0X38                
7D0D: FF              RST     0X38                
7D0E: FF              RST     0X38                
7D0F: FF              RST     0X38                
7D10: FF              RST     0X38                
7D11: FF              RST     0X38                
7D12: FF              RST     0X38                
7D13: FF              RST     0X38                
7D14: FF              RST     0X38                
7D15: FF              RST     0X38                
7D16: FF              RST     0X38                
7D17: FF              RST     0X38                
7D18: FF              RST     0X38                
7D19: FF              RST     0X38                
7D1A: FF              RST     0X38                
7D1B: FF              RST     0X38                
7D1C: FF              RST     0X38                
7D1D: FF              RST     0X38                
7D1E: FF              RST     0X38                
7D1F: FF              RST     0X38                
7D20: FF              RST     0X38                
7D21: FF              RST     0X38                
7D22: FF              RST     0X38                
7D23: FF              RST     0X38                
7D24: FF              RST     0X38                
7D25: FF              RST     0X38                
7D26: FF              RST     0X38                
7D27: FF              RST     0X38                
7D28: FF              RST     0X38                
7D29: FF              RST     0X38                
7D2A: FF              RST     0X38                
7D2B: FF              RST     0X38                
7D2C: FF              RST     0X38                
7D2D: FF              RST     0X38                
7D2E: FF              RST     0X38                
7D2F: FF              RST     0X38                
7D30: FF              RST     0X38                
7D31: FF              RST     0X38                
7D32: FF              RST     0X38                
7D33: FF              RST     0X38                
7D34: FF              RST     0X38                
7D35: FF              RST     0X38                
7D36: FF              RST     0X38                
7D37: FF              RST     0X38                
7D38: FF              RST     0X38                
7D39: FF              RST     0X38                
7D3A: FF              RST     0X38                
7D3B: FF              RST     0X38                
7D3C: FF              RST     0X38                
7D3D: FF              RST     0X38                
7D3E: FF              RST     0X38                
7D3F: FF              RST     0X38                
7D40: FF              RST     0X38                
7D41: FF              RST     0X38                
7D42: FF              RST     0X38                
7D43: FF              RST     0X38                
7D44: FF              RST     0X38                
7D45: FF              RST     0X38                
7D46: FF              RST     0X38                
7D47: FF              RST     0X38                
7D48: FF              RST     0X38                
7D49: FF              RST     0X38                
7D4A: FF              RST     0X38                
7D4B: FF              RST     0X38                
7D4C: FF              RST     0X38                
7D4D: FF              RST     0X38                
7D4E: FF              RST     0X38                
7D4F: FF              RST     0X38                
7D50: FF              RST     0X38                
7D51: FF              RST     0X38                
7D52: FF              RST     0X38                
7D53: FF              RST     0X38                
7D54: FF              RST     0X38                
7D55: FF              RST     0X38                
7D56: FF              RST     0X38                
7D57: FF              RST     0X38                
7D58: FF              RST     0X38                
7D59: FF              RST     0X38                
7D5A: FF              RST     0X38                
7D5B: FF              RST     0X38                
7D5C: FF              RST     0X38                
7D5D: FF              RST     0X38                
7D5E: FF              RST     0X38                
7D5F: FF              RST     0X38                
7D60: FF              RST     0X38                
7D61: FF              RST     0X38                
7D62: FF              RST     0X38                
7D63: FF              RST     0X38                
7D64: FF              RST     0X38                
7D65: FF              RST     0X38                
7D66: FF              RST     0X38                
7D67: FF              RST     0X38                
7D68: FF              RST     0X38                
7D69: FF              RST     0X38                
7D6A: FF              RST     0X38                
7D6B: FF              RST     0X38                
7D6C: FF              RST     0X38                
7D6D: FF              RST     0X38                
7D6E: FF              RST     0X38                
7D6F: FF              RST     0X38                
7D70: FF              RST     0X38                
7D71: FF              RST     0X38                
7D72: FF              RST     0X38                
7D73: FF              RST     0X38                
7D74: FF              RST     0X38                
7D75: FF              RST     0X38                
7D76: FF              RST     0X38                
7D77: FF              RST     0X38                
7D78: FF              RST     0X38                
7D79: FF              RST     0X38                
7D7A: FF              RST     0X38                
7D7B: FF              RST     0X38                
7D7C: FF              RST     0X38                
7D7D: FF              RST     0X38                
7D7E: FF              RST     0X38                
7D7F: FF              RST     0X38                
7D80: FF              RST     0X38                
7D81: FF              RST     0X38                
7D82: FF              RST     0X38                
7D83: FF              RST     0X38                
7D84: FF              RST     0X38                
7D85: FF              RST     0X38                
7D86: FF              RST     0X38                
7D87: FF              RST     0X38                
7D88: FF              RST     0X38                
7D89: FF              RST     0X38                
7D8A: FF              RST     0X38                
7D8B: FF              RST     0X38                
7D8C: FF              RST     0X38                
7D8D: FF              RST     0X38                
7D8E: FF              RST     0X38                
7D8F: FF              RST     0X38                
7D90: FF              RST     0X38                
7D91: FF              RST     0X38                
7D92: FF              RST     0X38                
7D93: FF              RST     0X38                
7D94: FF              RST     0X38                
7D95: FF              RST     0X38                
7D96: FF              RST     0X38                
7D97: FF              RST     0X38                
7D98: FF              RST     0X38                
7D99: FF              RST     0X38                
7D9A: FF              RST     0X38                
7D9B: FF              RST     0X38                
7D9C: FF              RST     0X38                
7D9D: FF              RST     0X38                
7D9E: FF              RST     0X38                
7D9F: FF              RST     0X38                
7DA0: FF              RST     0X38                
7DA1: FF              RST     0X38                
7DA2: FF              RST     0X38                
7DA3: FF              RST     0X38                
7DA4: FF              RST     0X38                
7DA5: FF              RST     0X38                
7DA6: FF              RST     0X38                
7DA7: FF              RST     0X38                
7DA8: FF              RST     0X38                
7DA9: FF              RST     0X38                
7DAA: FF              RST     0X38                
7DAB: FF              RST     0X38                
7DAC: FF              RST     0X38                
7DAD: FF              RST     0X38                
7DAE: FF              RST     0X38                
7DAF: FF              RST     0X38                
7DB0: FF              RST     0X38                
7DB1: FF              RST     0X38                
7DB2: FF              RST     0X38                
7DB3: FF              RST     0X38                
7DB4: FF              RST     0X38                
7DB5: FF              RST     0X38                
7DB6: FF              RST     0X38                
7DB7: FF              RST     0X38                
7DB8: FF              RST     0X38                
7DB9: FF              RST     0X38                
7DBA: FF              RST     0X38                
7DBB: FF              RST     0X38                
7DBC: FF              RST     0X38                
7DBD: FF              RST     0X38                
7DBE: FF              RST     0X38                
7DBF: FF              RST     0X38                
7DC0: FF              RST     0X38                
7DC1: FF              RST     0X38                
7DC2: FF              RST     0X38                
7DC3: FF              RST     0X38                
7DC4: FF              RST     0X38                
7DC5: FF              RST     0X38                
7DC6: FF              RST     0X38                
7DC7: FF              RST     0X38                
7DC8: FF              RST     0X38                
7DC9: FF              RST     0X38                
7DCA: FF              RST     0X38                
7DCB: FF              RST     0X38                
7DCC: FF              RST     0X38                
7DCD: FF              RST     0X38                
7DCE: FF              RST     0X38                
7DCF: FF              RST     0X38                
7DD0: FF              RST     0X38                
7DD1: FF              RST     0X38                
7DD2: FF              RST     0X38                
7DD3: FF              RST     0X38                
7DD4: FF              RST     0X38                
7DD5: FF              RST     0X38                
7DD6: FF              RST     0X38                
7DD7: FF              RST     0X38                
7DD8: FF              RST     0X38                
7DD9: FF              RST     0X38                
7DDA: FF              RST     0X38                
7DDB: FF              RST     0X38                
7DDC: FF              RST     0X38                
7DDD: FF              RST     0X38                
7DDE: FF              RST     0X38                
7DDF: FF              RST     0X38                
7DE0: FF              RST     0X38                
7DE1: FF              RST     0X38                
7DE2: FF              RST     0X38                
7DE3: FF              RST     0X38                
7DE4: FF              RST     0X38                
7DE5: FF              RST     0X38                
7DE6: FF              RST     0X38                
7DE7: FF              RST     0X38                
7DE8: FF              RST     0X38                
7DE9: FF              RST     0X38                
7DEA: FF              RST     0X38                
7DEB: FF              RST     0X38                
7DEC: FF              RST     0X38                
7DED: FF              RST     0X38                
7DEE: FF              RST     0X38                
7DEF: FF              RST     0X38                
7DF0: FF              RST     0X38                
7DF1: FF              RST     0X38                
7DF2: FF              RST     0X38                
7DF3: FF              RST     0X38                
7DF4: FF              RST     0X38                
7DF5: FF              RST     0X38                
7DF6: FF              RST     0X38                
7DF7: FF              RST     0X38                
7DF8: FF              RST     0X38                
7DF9: FF              RST     0X38                
7DFA: FF              RST     0X38                
7DFB: FF              RST     0X38                
7DFC: FF              RST     0X38                
7DFD: FF              RST     0X38                
7DFE: FF              RST     0X38                
7DFF: FF              RST     0X38                
7E00: FF              RST     0X38                
7E01: FF              RST     0X38                
7E02: FF              RST     0X38                
7E03: FF              RST     0X38                
7E04: FF              RST     0X38                
7E05: FF              RST     0X38                
7E06: FF              RST     0X38                
7E07: FF              RST     0X38                
7E08: FF              RST     0X38                
7E09: FF              RST     0X38                
7E0A: FF              RST     0X38                
7E0B: FF              RST     0X38                
7E0C: FF              RST     0X38                
7E0D: FF              RST     0X38                
7E0E: FF              RST     0X38                
7E0F: FF              RST     0X38                
7E10: FF              RST     0X38                
7E11: FF              RST     0X38                
7E12: FF              RST     0X38                
7E13: FF              RST     0X38                
7E14: FF              RST     0X38                
7E15: FF              RST     0X38                
7E16: FF              RST     0X38                
7E17: FF              RST     0X38                
7E18: FF              RST     0X38                
7E19: FF              RST     0X38                
7E1A: FF              RST     0X38                
7E1B: FF              RST     0X38                
7E1C: FF              RST     0X38                
7E1D: FF              RST     0X38                
7E1E: FF              RST     0X38                
7E1F: FF              RST     0X38                
7E20: FF              RST     0X38                
7E21: FF              RST     0X38                
7E22: FF              RST     0X38                
7E23: FF              RST     0X38                
7E24: FF              RST     0X38                
7E25: FF              RST     0X38                
7E26: FF              RST     0X38                
7E27: FF              RST     0X38                
7E28: FF              RST     0X38                
7E29: FF              RST     0X38                
7E2A: FF              RST     0X38                
7E2B: FF              RST     0X38                
7E2C: FF              RST     0X38                
7E2D: FF              RST     0X38                
7E2E: FF              RST     0X38                
7E2F: FF              RST     0X38                
7E30: FF              RST     0X38                
7E31: FF              RST     0X38                
7E32: FF              RST     0X38                
7E33: FF              RST     0X38                
7E34: FF              RST     0X38                
7E35: FF              RST     0X38                
7E36: FF              RST     0X38                
7E37: FF              RST     0X38                
7E38: FF              RST     0X38                
7E39: FF              RST     0X38                
7E3A: FF              RST     0X38                
7E3B: FF              RST     0X38                
7E3C: FF              RST     0X38                
7E3D: FF              RST     0X38                
7E3E: FF              RST     0X38                
7E3F: FF              RST     0X38                
7E40: FF              RST     0X38                
7E41: FF              RST     0X38                
7E42: FF              RST     0X38                
7E43: FF              RST     0X38                
7E44: FF              RST     0X38                
7E45: FF              RST     0X38                
7E46: FF              RST     0X38                
7E47: FF              RST     0X38                
7E48: FF              RST     0X38                
7E49: FF              RST     0X38                
7E4A: FF              RST     0X38                
7E4B: FF              RST     0X38                
7E4C: FF              RST     0X38                
7E4D: FF              RST     0X38                
7E4E: FF              RST     0X38                
7E4F: FF              RST     0X38                
7E50: FF              RST     0X38                
7E51: FF              RST     0X38                
7E52: FF              RST     0X38                
7E53: FF              RST     0X38                
7E54: FF              RST     0X38                
7E55: FF              RST     0X38                
7E56: FF              RST     0X38                
7E57: FF              RST     0X38                
7E58: FF              RST     0X38                
7E59: FF              RST     0X38                
7E5A: FF              RST     0X38                
7E5B: FF              RST     0X38                
7E5C: FF              RST     0X38                
7E5D: FF              RST     0X38                
7E5E: FF              RST     0X38                
7E5F: FF              RST     0X38                
7E60: FF              RST     0X38                
7E61: FF              RST     0X38                
7E62: FF              RST     0X38                
7E63: FF              RST     0X38                
7E64: FF              RST     0X38                
7E65: FF              RST     0X38                
7E66: FF              RST     0X38                
7E67: FF              RST     0X38                
7E68: FF              RST     0X38                
7E69: FF              RST     0X38                
7E6A: FF              RST     0X38                
7E6B: FF              RST     0X38                
7E6C: FF              RST     0X38                
7E6D: FF              RST     0X38                
7E6E: FF              RST     0X38                
7E6F: FF              RST     0X38                
7E70: FF              RST     0X38                
7E71: FF              RST     0X38                
7E72: FF              RST     0X38                
7E73: FF              RST     0X38                
7E74: FF              RST     0X38                
7E75: FF              RST     0X38                
7E76: FF              RST     0X38                
7E77: FF              RST     0X38                
7E78: FF              RST     0X38                
7E79: FF              RST     0X38                
7E7A: FF              RST     0X38                
7E7B: FF              RST     0X38                
7E7C: FF              RST     0X38                
7E7D: FF              RST     0X38                
7E7E: FF              RST     0X38                
7E7F: FF              RST     0X38                
7E80: FF              RST     0X38                
7E81: FF              RST     0X38                
7E82: FF              RST     0X38                
7E83: FF              RST     0X38                
7E84: FF              RST     0X38                
7E85: FF              RST     0X38                
7E86: FF              RST     0X38                
7E87: FF              RST     0X38                
7E88: FF              RST     0X38                
7E89: FF              RST     0X38                
7E8A: FF              RST     0X38                
7E8B: FF              RST     0X38                
7E8C: FF              RST     0X38                
7E8D: FF              RST     0X38                
7E8E: FF              RST     0X38                
7E8F: FF              RST     0X38                
7E90: FF              RST     0X38                
7E91: FF              RST     0X38                
7E92: FF              RST     0X38                
7E93: FF              RST     0X38                
7E94: FF              RST     0X38                
7E95: FF              RST     0X38                
7E96: FF              RST     0X38                
7E97: FF              RST     0X38                
7E98: FF              RST     0X38                
7E99: FF              RST     0X38                
7E9A: FF              RST     0X38                
7E9B: FF              RST     0X38                
7E9C: FF              RST     0X38                
7E9D: FF              RST     0X38                
7E9E: FF              RST     0X38                
7E9F: FF              RST     0X38                
7EA0: FF              RST     0X38                
7EA1: FF              RST     0X38                
7EA2: FF              RST     0X38                
7EA3: FF              RST     0X38                
7EA4: FF              RST     0X38                
7EA5: FF              RST     0X38                
7EA6: FF              RST     0X38                
7EA7: FF              RST     0X38                
7EA8: FF              RST     0X38                
7EA9: FF              RST     0X38                
7EAA: FF              RST     0X38                
7EAB: FF              RST     0X38                
7EAC: FF              RST     0X38                
7EAD: FF              RST     0X38                
7EAE: FF              RST     0X38                
7EAF: FF              RST     0X38                
7EB0: FF              RST     0X38                
7EB1: FF              RST     0X38                
7EB2: FF              RST     0X38                
7EB3: FF              RST     0X38                
7EB4: FF              RST     0X38                
7EB5: FF              RST     0X38                
7EB6: FF              RST     0X38                
7EB7: FF              RST     0X38                
7EB8: FF              RST     0X38                
7EB9: FF              RST     0X38                
7EBA: FF              RST     0X38                
7EBB: FF              RST     0X38                
7EBC: FF              RST     0X38                
7EBD: FF              RST     0X38                
7EBE: FF              RST     0X38                
7EBF: FF              RST     0X38                
7EC0: FF              RST     0X38                
7EC1: FF              RST     0X38                
7EC2: FF              RST     0X38                
7EC3: FF              RST     0X38                
7EC4: FF              RST     0X38                
7EC5: FF              RST     0X38                
7EC6: FF              RST     0X38                
7EC7: FF              RST     0X38                
7EC8: FF              RST     0X38                
7EC9: FF              RST     0X38                
7ECA: FF              RST     0X38                
7ECB: FF              RST     0X38                
7ECC: FF              RST     0X38                
7ECD: FF              RST     0X38                
7ECE: FF              RST     0X38                
7ECF: FF              RST     0X38                
7ED0: FF              RST     0X38                
7ED1: FF              RST     0X38                
7ED2: FF              RST     0X38                
7ED3: FF              RST     0X38                
7ED4: FF              RST     0X38                
7ED5: FF              RST     0X38                
7ED6: FF              RST     0X38                
7ED7: FF              RST     0X38                
7ED8: FF              RST     0X38                
7ED9: FF              RST     0X38                
7EDA: FF              RST     0X38                
7EDB: FF              RST     0X38                
7EDC: FF              RST     0X38                
7EDD: FF              RST     0X38                
7EDE: FF              RST     0X38                
7EDF: FF              RST     0X38                
7EE0: FF              RST     0X38                
7EE1: FF              RST     0X38                
7EE2: FF              RST     0X38                
7EE3: FF              RST     0X38                
7EE4: FF              RST     0X38                
7EE5: FF              RST     0X38                
7EE6: FF              RST     0X38                
7EE7: FF              RST     0X38                
7EE8: FF              RST     0X38                
7EE9: FF              RST     0X38                
7EEA: FF              RST     0X38                
7EEB: FF              RST     0X38                
7EEC: FF              RST     0X38                
7EED: FF              RST     0X38                
7EEE: FF              RST     0X38                
7EEF: FF              RST     0X38                
7EF0: FF              RST     0X38                
7EF1: FF              RST     0X38                
7EF2: FF              RST     0X38                
7EF3: FF              RST     0X38                
7EF4: FF              RST     0X38                
7EF5: FF              RST     0X38                
7EF6: FF              RST     0X38                
7EF7: FF              RST     0X38                
7EF8: FF              RST     0X38                
7EF9: FF              RST     0X38                
7EFA: FF              RST     0X38                
7EFB: FF              RST     0X38                
7EFC: FF              RST     0X38                
7EFD: FF              RST     0X38                
7EFE: FF              RST     0X38                
7EFF: FF              RST     0X38                
7F00: FF              RST     0X38                
7F01: FF              RST     0X38                
7F02: FF              RST     0X38                
7F03: FF              RST     0X38                
7F04: FF              RST     0X38                
7F05: FF              RST     0X38                
7F06: FF              RST     0X38                
7F07: FF              RST     0X38                
7F08: FF              RST     0X38                
7F09: FF              RST     0X38                
7F0A: FF              RST     0X38                
7F0B: FF              RST     0X38                
7F0C: FF              RST     0X38                
7F0D: FF              RST     0X38                
7F0E: FF              RST     0X38                
7F0F: FF              RST     0X38                
7F10: FF              RST     0X38                
7F11: FF              RST     0X38                
7F12: FF              RST     0X38                
7F13: FF              RST     0X38                
7F14: FF              RST     0X38                
7F15: FF              RST     0X38                
7F16: FF              RST     0X38                
7F17: FF              RST     0X38                
7F18: FF              RST     0X38                
7F19: FF              RST     0X38                
7F1A: FF              RST     0X38                
7F1B: FF              RST     0X38                
7F1C: FF              RST     0X38                
7F1D: FF              RST     0X38                
7F1E: FF              RST     0X38                
7F1F: FF              RST     0X38                
7F20: FF              RST     0X38                
7F21: FF              RST     0X38                
7F22: FF              RST     0X38                
7F23: FF              RST     0X38                
7F24: FF              RST     0X38                
7F25: FF              RST     0X38                
7F26: FF              RST     0X38                
7F27: FF              RST     0X38                
7F28: FF              RST     0X38                
7F29: FF              RST     0X38                
7F2A: FF              RST     0X38                
7F2B: FF              RST     0X38                
7F2C: FF              RST     0X38                
7F2D: FF              RST     0X38                
7F2E: FF              RST     0X38                
7F2F: FF              RST     0X38                
7F30: FF              RST     0X38                
7F31: FF              RST     0X38                
7F32: FF              RST     0X38                
7F33: FF              RST     0X38                
7F34: FF              RST     0X38                
7F35: FF              RST     0X38                
7F36: FF              RST     0X38                
7F37: FF              RST     0X38                
7F38: FF              RST     0X38                
7F39: FF              RST     0X38                
7F3A: FF              RST     0X38                
7F3B: FF              RST     0X38                
7F3C: FF              RST     0X38                
7F3D: FF              RST     0X38                
7F3E: FF              RST     0X38                
7F3F: FF              RST     0X38                
7F40: FF              RST     0X38                
7F41: FF              RST     0X38                
7F42: FF              RST     0X38                
7F43: FF              RST     0X38                
7F44: FF              RST     0X38                
7F45: FF              RST     0X38                
7F46: FF              RST     0X38                
7F47: FF              RST     0X38                
7F48: FF              RST     0X38                
7F49: FF              RST     0X38                
7F4A: FF              RST     0X38                
7F4B: FF              RST     0X38                
7F4C: FF              RST     0X38                
7F4D: FF              RST     0X38                
7F4E: FF              RST     0X38                
7F4F: FF              RST     0X38                
7F50: FF              RST     0X38                
7F51: FF              RST     0X38                
7F52: FF              RST     0X38                
7F53: FF              RST     0X38                
7F54: FF              RST     0X38                
7F55: FF              RST     0X38                
7F56: FF              RST     0X38                
7F57: FF              RST     0X38                
7F58: FF              RST     0X38                
7F59: FF              RST     0X38                
7F5A: FF              RST     0X38                
7F5B: FF              RST     0X38                
7F5C: FF              RST     0X38                
7F5D: FF              RST     0X38                
7F5E: FF              RST     0X38                
7F5F: FF              RST     0X38                
7F60: FF              RST     0X38                
7F61: FF              RST     0X38                
7F62: FF              RST     0X38                
7F63: FF              RST     0X38                
7F64: FF              RST     0X38                
7F65: FF              RST     0X38                
7F66: FF              RST     0X38                
7F67: FF              RST     0X38                
7F68: FF              RST     0X38                
7F69: FF              RST     0X38                
7F6A: FF              RST     0X38                
7F6B: FF              RST     0X38                
7F6C: FF              RST     0X38                
7F6D: FF              RST     0X38                
7F6E: FF              RST     0X38                
7F6F: FF              RST     0X38                
7F70: FF              RST     0X38                
7F71: FF              RST     0X38                
7F72: FF              RST     0X38                
7F73: FF              RST     0X38                
7F74: FF              RST     0X38                
7F75: FF              RST     0X38                
7F76: FF              RST     0X38                
7F77: FF              RST     0X38                
7F78: FF              RST     0X38                
7F79: FF              RST     0X38                
7F7A: FF              RST     0X38                
7F7B: FF              RST     0X38                
7F7C: FF              RST     0X38                
7F7D: FF              RST     0X38                
7F7E: FF              RST     0X38                
7F7F: FF              RST     0X38                
7F80: F0 A8           LD      A,($A8)             
7F82: A7              AND     A                   
7F83: 28 19           JR      Z,$7F9E             ; {}
7F85: D6 01           SUB     $01                 
7F87: E0 A8           LDFF00  ($A8),A             
7F89: E6 03           AND     $03                 
7F8B: 20 11           JR      NZ,$7F9E            ; {}
7F8D: F0 A9           LD      A,($A9)             
7F8F: A7              AND     A                   
7F90: 28 03           JR      Z,$7F95             ; {}
7F92: 3D              DEC     A                   
7F93: E0 A9           LDFF00  ($A9),A             
7F95: F0 AA           LD      A,($AA)             
7F97: A7              AND     A                   
7F98: 28 04           JR      Z,$7F9E             ; {}
7F9A: D6 10           SUB     $10                 
7F9C: E0 AA           LDFF00  ($AA),A             
7F9E: F0 AB           LD      A,($AB)             
7FA0: A7              AND     A                   
7FA1: 28 1B           JR      Z,$7FBE             ; {}
7FA3: D6 01           SUB     $01                 
7FA5: E0 AB           LDFF00  ($AB),A             
7FA7: E6 01           AND     $01                 
7FA9: 20 13           JR      NZ,$7FBE            ; {}
7FAB: F0 A9           LD      A,($A9)             
7FAD: FE 07           CP      $07                 
7FAF: 30 03           JR      NC,$7FB4            ; {}
7FB1: 3C              INC     A                   
7FB2: E0 A9           LDFF00  ($A9),A             
7FB4: F0 AA           LD      A,($AA)             
7FB6: FE 70           CP      $70                 
7FB8: 30 04           JR      NC,$7FBE            ; {}
7FBA: C6 10           ADD     $10                 
7FBC: E0 AA           LDFF00  ($AA),A             
7FBE: 21 A9 FF        LD      HL,$FFA9            
7FC1: F0 24           LD      A,($24)             
7FC3: E6 F8           AND     $F8                 
7FC5: B6              OR      (HL)                
7FC6: 23              INC     HL                  
7FC7: E6 8F           AND     $8F                 
7FC9: B6              OR      (HL)                
7FCA: E0 24           LDFF00  ($24),A             
7FCC: F0 F2           LD      A,($F2)             
7FCE: A7              AND     A                   
7FCF: 28 06           JR      Z,$7FD7             ; {}
7FD1: EA 60 D3        LD      ($D360),A           
7FD4: AF              XOR     A                   
7FD5: E0 F2           LDFF00  ($F2),A             
7FD7: F0 F3           LD      A,($F3)             
7FD9: A7              AND     A                   
7FDA: 28 06           JR      Z,$7FE2             ; {}
7FDC: EA 70 D3        LD      ($D370),A           
7FDF: AF              XOR     A                   
7FE0: E0 F3           LDFF00  ($F3),A             
7FE2: F0 F4           LD      A,($F4)             
7FE4: A7              AND     A                   
7FE5: 28 06           JR      Z,$7FED             ; {}
7FE7: EA 78 D3        LD      ($D378),A           
7FEA: AF              XOR     A                   
7FEB: E0 F4           LDFF00  ($F4),A             
7FED: C9              RET                         
7FEE: FF              RST     0X38                
7FEF: FF              RST     0X38                
7FF0: FF              RST     0X38                
7FF1: FF              RST     0X38                
7FF2: FF              RST     0X38                
7FF3: FF              RST     0X38                
7FF4: FF              RST     0X38                
7FF5: FF              RST     0X38                
7FF6: FF              RST     0X38                
7FF7: FF              RST     0X38                
7FF8: FF              RST     0X38                
7FF9: FF              RST     0X38                
7FFA: FF              RST     0X38                
7FFB: FF              RST     0X38                
7FFC: FF              RST     0X38                
7FFD: FF              RST     0X38                
7FFE: FF              RST     0X38                
7FFF: FF              RST     0X38                
```

