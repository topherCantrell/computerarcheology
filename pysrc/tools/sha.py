import hashlib

import binary
import code.markdown_utils


#MD_FILE = '../../content/Arcade/moonpatrol/ImageBackgroundColors.md'
#MD_FILE = '../../content/Arcade/moonpatrol/SpriteColors.md'
#MD_FILE = '../../content/Arcade/moonpatrol/TextColors.md'
#MD_FILE = '../../content/Arcade/moonpatrol/SpriteColorSets.md'
#MD_FILE = '../../content/Arcade/moonpatrol/GFX3.md'
#MD_FILE = '../../content/Arcade/moonpatrol/GFX4.md'
#MD_FILE = '../../content/Arcade/moonpatrol/GFX5.md'
#MD_FILE = '../../content/Arcade/moonpatrol/GFX1.md'
#MD_FILE = '../../content/Arcade/moonpatrol/GFX2.md'
#data = binary.get_binary(MD_FILE, 0)

#MD_FILE = '../../content/Arcade/moonpatrol/SoundCode.md'
MD_FILE = '../../content/Arcade/moonpatrol/Code.md'
data = code.markdown_utils.get_binary(MD_FILE)

print(hashlib.sha1(bytearray(data[0:0x1000])).hexdigest())
print(hashlib.sha1(bytearray(data[0x1000:0x2000])).hexdigest())
print(hashlib.sha1(bytearray(data[0x2000:0x3000])).hexdigest())
print(hashlib.sha1(bytearray(data[0x3000:0x4000])).hexdigest())

#print(hashlib.sha1(bytearray(data[0:0x1000])).hexdigest())
#print(hashlib.sha1(bytearray(data[0x1000:])).hexdigest())

