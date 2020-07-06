import json
from digs.raaka_bed.decoder import Decoder

# Nothing in the code ... best we can do is make lists here

OBJECT_SHORT_NAMES = {
    0x00 : 'nowhere',    
    
    0x01 : 'GreenDoorA', # Word is not in CoCo version
    0x02 : 'GreenDoorB',
    0x03 : 'RedDoorA',
    0x04 : 'RedDoorB',
    0x05 : 'GreenDoorC',
    0x06 : 'GreedDoorD',
    0x07 : 'RedDoorC',
    0x08 : 'RedDoorD',
    0x09 : 'GreenDoorE',
    0x0A : 'GreenDoorF',
    0x0B : 'RedDoorE',
    0x0C : 'GreenDoorG',
    0x0D : 'GreenDoorH',
    0x0E : 'RedDoorF',
    0x0F : 'BlueDoorA',
    
    0x10 : 'BlueDoorB',
    0x11 : 'BlueDoorC',
    0x12 : 'BlueDoorD',
    0x13 : 'PLAYER',
    0x14 : 'RedKeyA',
    0x15 : 'BluePillA',
    0x16 : 'WindowHook',
    0x17 : 'Cabinet',
    0x18 : 'Refrigerator',
    0x19 : 'HamburgerMeat',
    0x1A : 'GuardDog',
    0x1B : 'GreenKeyA',
    0x1C : 'RayA',
    0x1D : 'RayB',
    0x1E : 'NapoleanA',
    0x1F : 'Object1F',
    
    0x20 : 'NapoleanB',
    0x21 : 'Object21',
    0x22 : 'PicassoA',
    0x23 : 'Object23',
    0x24 : 'PicassoB',
    0x25 : 'Object25',
    0x26 : 'MerlinA',
    0x27 : 'MerlinB',
    0x28 : 'UnconsciousDoctorA',
    0x29 : 'UnconsciousDoctorB',
    0x2A : 'HoudiniA',
    0x2B : 'HoudiniB',
    0x2C : 'HoudiniC',
    0x2D : 'Woman',
    0x2E : 'Doctor',
    0x2F : 'Walls',
    
    0x30 : 'Room',
    0x31 : 'Floor',
    0x32 : 'Exit',
    0x33 : 'Corner',
    0x34 : 'Hallway',
    0x35 : 'Entrance',
    0x36 : 'Ceiling',
    0x37 : 'Hands',
    0x38 : 'SYSTEM',
    0x39 : 'BluePillB',
    0x3A : 'Object3A',
    0x3B : 'RedKeyB',
    0x3C : 'DeadDog',
    0x3D : 'SecretDoor',
    0x3E : 'PaintedDoorA',
    0x3F : 'PaintedDoorB',
    
    0x40 : 'GreenDoorI',
    0x41 : 'GreenKeyB',
    0x42 : 'Object42',
    
    0xFF : 'everywhere',
        
}

ROOM_SHORT_NAMES = {      
    
    0x81 : 'Maintenance room',
    0x82 : 'Dispensary',
    0x83 : 'Examination room',
    0x84 : 'West end east-west hall',
    0x85 : 'Padded room A',
    0x86 : 'Padded room B',
    0x87 : 'East-west hall A',
    0x88 : 'Small square room',
    0x89 : 'Padded room C',
    0x8A : 'East-west hall B',
    0x8B : 'Padded room D',
    0x8C : 'East end east-west hall',
    0x8D : 'Padded room E',
    0x8E : 'Electroshock room',
    0x8F : 'North end of north-south hall',
    
    0x90 : 'Padded room F',
    0x91 : 'North-south hall',
    0x92 : 'Kitchen',
    0x93 : 'Kennel',
    0x94 : 'Padded room G',
    0x95 : 'Office',
    0x96 : 'South end north-south hall',
    0x97 : 'Dining room',
    0x98 : 'Recreation room',
    0x99 : 'Storage shed',
    
}

HELPER_SHORT_NAMES = {
    
    0x81 : 'PrintAnotherPaddedRoom',
    0x82 : 'PrintEastWestHall',
    0x83 : 'PrintNorthSouthHall',
    0x84 : 'PrintSouthWallGreenDoor',
    0x85 : 'PrintNorthWallRedDoor',
    0x86 : 'PrintNorthWallGreedDoor',
    0x87 : 'PrintSouthWallRedDOor',
    0x88 : 'PrintEastWallBlueDoor',
    0x89 : 'PrintWestWallBlueDoor',
    0x8A : 'PrintClosed',
    0x8B : 'PrintPeriod',
    0x8C : 'PrintThisIsOrYouAreIn',
    0x8D : 'PrintObjectIsClosed',
    0x8E : '', # Not given
    0x8F : '??GetObject',
    
    0x90 : '??SomethingUseDirections',
    0x91 : 'PrintUseDirections',
    0x92 : '??YouCantDoThatTo',
    0x93 : '', # Not given
    0x94 : 'InitializeGame',
    0x95 : 'RandomMoveAndDrop',
    0x96 : 'PrintNapoleanIntro',
    0x97 : 'PrintNapolean',
    0x98 : 'PrintPicassoIntro',
    0x99 : 'PrintPicasso',
    0x9A : '??CommandResponse',
    0x9B : '??PrintDirs',
    0x9C : '??MoveHoudiniC',
    0x9D : 'PrintBluePill',
    0x9E : 'PrintObjectEntersRoom',
    0x9F : 'PrintUnshavenMan',
    
    0xA0 : 'PrintPillInHamburger',
    0xA1 : 'FeedDogMeat',
    0xA2 : 'PrintAlreadyHaveObject',
    0xA3 : 'AwakenInRoom',
    0xA4 : 'PrintPicassoDoor',
    0xA5 : 'AttemptClose',
    0xA6 : 'AttemptOpen',
    0xA7 : 'AttemptUnlock',
    0xA8 : 'PrintTheFirstNoun',
    0xA9 : 'PrintTheSecondNoun',
    0xAA : 'PrintTheVarName',
    0xAB : 'AttackPerson',
    0xAC : 'PrintTheVarName(sameAA)',
    0xAD : 'PrintTheVarNotHungry',
    0xAE : 'PrintFindMouthGame',
    0xAF : 'PrintLeapsBounds',
    
    0xB0 : 'PrintTastesAweful',
    0xB1 : 'PrintYouGetObjectWithObject',
    0xB2 : 'PrintCantGetObjectWithObject',    
    
}
        
INFO_TRS80 = {
    'binfile'  : '../../../content/TRS80/Bedlam/BEDLAM.bin',
    'codefile' : '../../../content/TRS80/Bedlam/Code.md',
    'origin' : 0x4300,
    'word_data' : 0x5234,
    'phrase_data' : 0x5025,
    'object_data' : 0x5561,
    'general_commands_data' : 0x6FA2,
    'helper_commands_data' : 0x75E5,
    'room_descriptions_data' : 0x6A01,
    'command_table': 0x4FC8,
}

INFO_COCO = {
    'binfile'  : '../../../content/CoCo/Bedlam/Bedlam.bin',
    'codefile' : '../../../content/CoCo/Bedlam/Code.md',
    'origin' : 0x0600,
    'word_data' : 0x3BD5,
    'phrase_data' : 0x13E3,
    'object_data' : 0x1B42,
    'general_commands_data' : 0x2F24,
    'helper_commands_data' : 0x339C,
    'room_descriptions_data' : 0x15A1,
    'command_table': 0x1357,
}

coco = Decoder(INFO_COCO,OBJECT_SHORT_NAMES,ROOM_SHORT_NAMES,HELPER_SHORT_NAMES)
plat = coco
out = []
plat.print_general_commands(out)
plat.merge_into(out)
out = []
plat.print_helper_commands(out)
plat.merge_into(out)
out = []
plat.print_room_descriptions(out)
plat.merge_into(out)
out = []
plat.print_object_data(out)
plat.merge_into(out)
out = []
plat.print_words(out)
plat.merge_into(out)
out = []
plat.print_phrases(out)
plat.merge_into(out)

plat.fix_command_names()

trs80 = Decoder(INFO_TRS80,OBJECT_SHORT_NAMES,ROOM_SHORT_NAMES,HELPER_SHORT_NAMES)
plat = trs80
out = []
plat.print_general_commands(out)
#plat.merge_into(out)

out = []
plat.print_helper_commands(out)
#plat.merge_into(out)

out = []
plat.print_room_descriptions(out)
#plat.merge_into(out)

out = []
plat.print_object_data(out)
for o in out:
    print(o)
plat.merge_into(out)

out = []
plat.print_words(out)
plat.merge_into(out)

out = []
plat.print_phrases(out)
plat.merge_into(out)

"""
plat.fix_command_names()

with open('rooms_raaka_trs80.json','w') as f:
    js = plat.tojson_room_descriptions()
    js = json.dumps(js,indent=2)
    f.write(js)
with open('objects_raaka_trs80.json','w') as f:
    js = plat.tojson_objects()
    js = json.dumps(js,indent=2)
    f.write(js)    
with open('general_raaka_trs80.json','w') as f:
    js = plat.tojson_general()
    js = json.dumps(js,indent=2)
    f.write(js)    
with open('helper_raakas_trs80.json','w') as f:
    js = plat.tojson_helpers()
    js = json.dumps(js,indent=2)
    f.write(js)    
with open('words_raaka_trs80.json','w') as f:
    js = plat.tojson_words()
    js = json.dumps(js,indent=2)
    f.write(js)
with open('phrases_raaka_trs80.json','w') as f:
    js = plat.tojson_phrases()
    js = json.dumps(js,indent=2)
    f.write(js)
"""