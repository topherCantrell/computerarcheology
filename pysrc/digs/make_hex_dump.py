import code.markdown_utils

binary = code.markdown_utils.get_binary('../../content/CoCo/megabug/Code.md')

pos = 0

for x in range(0x2000):
    print('0x{:02X},'.format(binary[x]),end='')
    pos+=1
    if(pos==32):
        pos = 0
        print()