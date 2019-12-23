import hashlib

import binary
import code.markdown_utils


#MD_FILE = '../../content/Arcade/moonpatrol/ImageBackgroundColors.md'
#MD_FILE = '../../content/Arcade/moonpatrol/SpriteColors.md'
#MD_FILE = '../../content/Arcade/moonpatrol/TextColors.md'
#MD_FILE = '../../content/Arcade/moonpatrol/SpriteColorSets.md'
#MD_FILE = '../../content/Arcade/moonpatrol/GFX3.md'
#MD_FILE = '../../content/Arcade/moonpatrol/GFX4.md'
MD_FILE = '../../content/Arcade/moonpatrol/GFX5.md'

#data = code.markdown_utils.get_binary(MD_FILE)
data = binary.get_binary(MD_FILE, 0)

# print(data)

print(hashlib.sha1(bytearray(data)).hexdigest())
