
import code.markdown_utils

#binary = code.markdown_utils.get_binary('../../../content/CoCo/Downland/Code.md')
binary = code.markdown_utils.get_binary('../../../content/CoCo/megabug/Code.md')

#with open('../../../content/CoCo/Downland/downland1_0.bin','rb') as f:
#    binary = f.read()

with open('mocha.bin','wb') as f:
    f.write(b'\x00\x20\x00\xC0\x00')
    
    f.write(bytearray(binary))
    
    f.write(b'\xFF\x00\x00\xC0\x00')
    
    