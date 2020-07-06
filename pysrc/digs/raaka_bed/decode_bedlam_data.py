import json
from digs.raaka_bed.decoder import Decoder

# Nothing in the code ... best we can do is make lists here

OBJECT_SHORT_NAMES = {
    0x00 : 'nowhere',
    0xFF : 'everywhere',
    
    0x01 : 'GreenDoorA', # Word is not in CoCo version
        
}

ROOM_SHORT_NAMES = {  
    
    
    0x81 : 'Maintenance room',
    
}

HELPER_SHORT_NAMES = {
    
    0x81: 'PrintAnotherPaddedRoom',
    
}
        
INFO_TRS80 = {
    'binfile'  : '../../../content/TRS80/Bedlam/BEDLAM.bin',
    'codefile' : '../../../content/TRS80/Bedlam/Code.md',
    'origin' : 0x4300,
    #'word_data' : 0x52C2,
    #'phrase_data' : 0x50B9,
    #'object_data' : 0x5651,
    #'general_commands_data' : 0x73FB,
    #'helper_commands_data' : 0x7BCD,
    #'room_descriptions_data' : 0x681F,
    #'command_table': 0x5066,
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
"""
out = []
plat.print_room_descriptions(out)
plat.merge_into(out)
out = []
plat.print_object_data(out)
plat.merge_into(out)
"""
out = []
plat.print_words(out)
plat.merge_into(out)
out = []
plat.print_phrases(out)
plat.merge_into(out)

plat.fix_command_names()

"""
trs80 = Decoder(INFO_TRS80,OBJECT_SHORT_NAMES,ROOM_SHORT_NAMES,HELPER_SHORT_NAMES)
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