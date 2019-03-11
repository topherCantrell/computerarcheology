![RAM](Bedlam.jpg)

# Bedlam RAM Use

>>>memory

| | | | |
| --- | --- | --- | --- |
| 88:89     | printCursor           | screen pointer used by BASIC                 |          |
| 01A7:01A8 |  tmp1A7               | used in decoding the input                   | :B4C,B5A,C17,C23,C32 | 
| 01A9      | tmp1A9                | used in comparing X to Y                     | :A99,A9D |
| 01AA      | not1AA                | never used                                   |          |
| 01AB      | tmp1AB                | used in lots of places                       | :91F,947,94A,9E8,9F1,A01,A07,A19,A22,A28,A30,A38,A43,A4E,BD3,BF8,C0E,C2F,C38,D3C,D4E,D67,D85,E51,E5C,1069,108F,10CA,10E9,1115,1122,113D,1156,1159,115C,1161,11A6,11A9,11B5,11BB,12E6 |
| 01AC      | not1AC                | never used                                   |          |
| 01AD      | tmp1AD                | used in the phrase decoding                  | :95F,974 |
| 01AE      | not1AE                | never used                                   |          |
| 01AF      | not1AF                | never used                                   |          |
| 01B0      | not1B0                | never used                                   |          |
| 01B1      | not1B1                | never used                                   |          |
| 01B2      | tmp1B2                | used in word decoding                        | :64D,868,8CD,915,94F,954,96D |
| 01B3      | verbWord              | input verb word number                       | :650,6E7,6EC,743,792 |
| 01B4      | perpWord              | preposition word number                      | :659,738,79E,9A0 |
| 01B5      | prepGiven             | preposition given flag                       | :65C,6F5,712,73B,762,7D9,99B |
| 01B6      | phrasePrep            | used in phrase decoding                      | :79B,9B1 |
| 01B7      | adjWord               | adjective word number                        | :644,6FF,70F,72E,871,890,8AD,959,980 |
| 01B8      | commandTarg           | target object of input command               | :656,6BF,812 |
| 01B9      | not1B9                | cleared before decode but never used         | :653     |
| 01BA      | lsbAdj1               | screen LSB of 1st adjective                  | :647,704,715,733 |
| 01BB      | lsbVerb               | screen LSB of verb                           | :64A,7B2,BC7 |
| 01BC      | lsbCursor             | screen lsb used in decoding the input line   | :7D1,996,BC4,C2C |
| 01BD      | lsbError              | screen lsb used for flashing error messages  | :7B5,7D4,9BE,9C8,A57 |
| 01BE      | lastChar              | last character printed to screen             | :11D5,11F2,1229,1238,1255 |
| 01BF      | VAR_OBJ_NUMBER        | variable object number                       | :65F,863,8B6,8C0,8DE,CF8,D06,D0F,EF8,F82,FC3,FE2,FFD |
| 01C0:01C1 | VAR_OBJ_DATA          | variable object data                         | :8C3,8DB,CF2,D00,D17,EF5,F06,F17,F7F,FC0,FDF,FFA,1033,10CF,1142 |
| 01C2      | not1C2                | never used                                   |          |
| 01C3      | FIRST_NOUN_NUM        | first input noun number                      | :662,71A,75C,768,7AD,7C1,801,80F,CF5,D2B,D41,D73,ED2,F5B,F8C |
| 01C4      | firstNounAdj          | first input noun adjective word number       |          |
| 01C5      | firstNounLSB          | first input noun screen LSB                  | :720     |
| 01C6:01C7 | FIRST_NOUN_DATA       | first input noun object data                 | :75F,765,809,CEF,D1E,D4B,D80,ECF,F65,F89 |
| 01C8      | firstNounParams       | first input noun parameter bits              | :774     |
| 01C9      | SECOND_NOUN_NUM       | second input noun number                     | :665,71D,750,77A,7CC,7E5,80C,D03,D28,D51,D76,EF0,F3F,FB9 |
| 01CA      | secondNounAdj         | second input noun adjective word number      |          |
| 01CB      | secondNounLSB         | second input noun noun screen LSB            | :723     |
| 01CC:01CD | SECOND_NOUN_DATA      | second input noun object data                | :753,777,806,CFD,D23,D59,D7B,EED,F44,FB6 |
| 01CE      | secondNounParams      | second input noun parameter bits             | :786     |
| 01CF      | tmp1CF                | another screen pointer used in decode        | :876,98D,9D1,B85,BB6 |
| 01D0      | tmp1DO                | used in making index of data fields          | :BD6,BFD,1054,105F,1083 |
| 01D1      | PHRASE_FORM           | decoded phrase form                          | :7F9,D30,D37,D6E,F00 |
| 01D2      | ACTIVE_OBJ_NUM        | active object                                | :617,66A,823,903,D8B,DA5,DBC,E31,E3B,E65,EA8,F0C,1041,1086,116A |
| 01D3:01D4 | ACTIVE_OBJ_DATA       | active object data                           | :670,826,CE0,E41,108C |
| 01D5      | CUR_ROOM              | current room number                          | :678,8EE,CD2,CE6,DCF,F1D,10A3 |
| 01D6:1D7  | CUR_ROOM_DATA         | current room data                            | :681,CDD,D96,F28,10AC |
| 01D8:1D9  | nextToken             | used in decoding input                       | :687,93D,95C,BAF,BBB,ED5,EE6 |
| 01DA      | tmp1DA                | used in unpacking bytes                      | :1276,1285 |
| 01DB      | tmp1DB                | used in unpacking bytes                      | :1279,1291,129D,12AE,12B6,12C3 |
| 01DC      | tmp1DC                | used in unpacking bytes                      | :127C,128E,1294 |
| 01DD      | tmp1DD                | used in unpacking bytes                      | :1269,1282 |
| 01DE      | tmp1DE                | used in unpacking bytes                      | :1264,127F |
| 01DF      | tmp1DF                | used in unpacking bytes                      | :12A3,12A8,12B3 |
| 01E0      | tmp1EO                | used in unpacking bytes                      | :129A    |
| 01E1      | tmp1E1                | used in making index of data fields          | :885,8D3,918,92D,977,A65,A6E |
| 01E2      | tmp1E2                | used in input processing                     | :888,8BD,8D0 |
| 01E3      | tillMORE              | rows left until MORE prompt                  | :602,641,1171,1195,120A,1232,123F |


$01E4     inputTokens           input token buffer

$03FF     stack                 top of stack (just below screen memory)
