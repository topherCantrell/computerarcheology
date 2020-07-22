import json
from digs.raaka_bed.decoder import Decoder

from tools import format as FORM

# Nothing in the code ... best we can do is make lists here

OBJECT_SHORT_NAMES = {
    0x00 : 'nowhere',
    0x01 : 'BOTTLE', # Word is not in CoCo version
    0x1D : 'PLAYER',
    0x24 : 'GUARD REPORTER',
    0x2E : 'CORNER',
    0x3C : 'AMBIENT SOUNDS',
    0xFF : 'everywhere',
}

ROOM_SHORT_NAMES = {
    0x81 : 'Small room granite walls',
    0x82 : 'Oriental rug',
    0x83 : 'Dark passage',
    0x84 : 'Top of a passage',
    0x85 : 'T-shaped room 1',
    0x86 : 'Gray stone walls 1',
    0x87 : 'Round room high walls 1',
    0x88 : 'Triangular room',
    0x89 : 'South end central hall',
    0x8A : 'T-shaped room 2',
    0x8B : 'Grey stone walls 2', # Not the 'GRAY stone walls'
    0x8C : 'Round room high walls 2',
    0x8D : 'Petite chamber',
    0x8E : 'Smells of decaying flesh',
    0x8F : 'Tall room',
    0x90 : 'North end central hall',
    0x91 : 'Vault',
    0x92 : 'Entrance long dark tunnel west',
    0x93 : 'Dark tunnel',
    0x94 : 'Entrance long dark tunnel east',
    0x95 : 'Large room',
    0x96 : 'Dense dark damp jungle',
    0x97 : 'Dark dense damp jungle',
    0x98 : 'See east wall',
    0x99 : 'Stands south wall',
    0x9A : 'See bronze gates',
    0x9B : 'See north wall',
    0x9C : 'Standing west entrance',
    0x9D : 'At north wall',
    0x9E : 'At east wall',
    0x9F : 'At south wall',
    0xA0 : 'Very small room',
    0xA1 : 'Small room',
    0xA2 : 'Dark damp dense jungle',
    0xA3 : 'Dense damp dark jungle',
    0xA4 : 'Damp dark dense jungle',
    0xA5 : 'Secret passage',
    0xA6 : 'End of the passage',
}

HELPER_SHORT_NAMES = {
    0x81: 'ResetGame',
    0x82: 'DeathByStatue',
    0x83: 'Manipulate',
    0x84: 'PrintPeriod',
    0x85: 'PrintGuardsMarchRight',
    0x86: 'PrintGuardsAroundCorner',
    0x87: 'PrintGuardsDisappearLeft',    
    0x88: 'PrintTheNOUNIsNotBurning',    
    0x89: 'PrintCantJumpThatFar',
    0x8A: 'DeathByRugSpike',
    0x8B: 'DeathByHiddenRugSpike',
    0x8C: 'PrintDiscoverPit',
    0x8D: 'PrintStatueTooHeavy',
    0x8E: 'PrintMoveAlter',
    0x8F: 'EnterSecretPassage',
    0x90: 'PrinteAlterMovesBack',
    0x91: 'SealUpHole',
    0x92: 'PrintScore',
    0x93: 'InvalidClimbInOrOut',
    0x94: 'PrintUseDirections',
    0x95: 'ResetDungeon',
    0x96: 'PrintGoodWayToLoseHand',
    0x97: 'PrintMouthImGame',
    0x98: 'PrintGiantLeapForYou'    
}
        
INFO_TRS80 = {
    'binfile'  : '../../../content/TRS80/RaakaTu/RAAKA.bin',
    'codefile' : '../../../content/TRS80/RaakaTu/Code.md',
    'origin' : 0x4300,
    'word_data' : 0x52C2,
    'phrase_data' : 0x50B9,
    'object_data' : 0x5651,
    'general_commands_data' : 0x73FB,
    'helper_commands_data' : 0x7BCD,
    'room_descriptions_data' : 0x681F,
    'command_table': 0x5066,
}

INFO_COCO = {
    'binfile'  : '../../../content/CoCo/RaakaTu/RaakaTu.bin',
    'codefile' : '../../../content/CoCo/RaakaTu/Code.md',
    'origin' : 0x0600,
    'word_data' : 0x3C29,
    'phrase_data' : 0x135B,
    'command_table': 0x12E5,
    
    'object_data' : 0x20FF,    
    'general_commands_data' : 0x323C,
    'helper_commands_data' : 0x37FA,
    'room_descriptions_data' : 0x1523, # same for coco/trs80    
}

coco = Decoder(INFO_COCO,OBJECT_SHORT_NAMES,ROOM_SHORT_NAMES,HELPER_SHORT_NAMES)
trs80 = Decoder(INFO_TRS80,OBJECT_SHORT_NAMES,ROOM_SHORT_NAMES,HELPER_SHORT_NAMES)

"""
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

plat = trs80
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
    
"""
in_trs80 = []
for t in trs80._words:
    for w in trs80._words[t]:
        in_trs80.append(FORM.shex2(w['num'])+' '+w['text'])
        
in_coco = []
for t in coco._words:
    for w in coco._words[t]:
        in_coco.append(FORM.shex2(w['num'])+' '+w['text'])
"""

"""
in_trs80 = []
for ph in trs80._phrases:
    in_trs80.append(trs80.phrase_to_string(ph,True))
    
in_coco = []
for ph in coco._phrases:
    in_coco.append(coco.phrase_to_string(ph,True))    
"""

in_coco=[]
obs = coco.tojson_objects(False)
for o in obs:
    in_coco.append(str(o))
    
in_trs80=[]
obs = trs80.tojson_objects(False)
for o in obs:
    in_trs80.append(str(o))
   

print('In CoCo but not TRS80')
for i in in_coco:
    if not i in in_trs80:
        print(i)
   
print('In TRS80 but not CoCo')
for i in in_trs80:
    if not i in in_coco:
        print(i)
