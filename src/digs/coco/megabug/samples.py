import code.markdown_utils


binary = code.markdown_utils.get_binary('../../../../content/CoCo/MegaBug/Code.md')

addr = 0xC003
cnt = 0

for i in binary:
    if cnt % 32 == 0:
        print('\n{:04X}:'.format(addr), end='')
    print(' {:02X}'.format(binary[addr - 0xC000]), end='')
    addr += 1
    cnt = cnt + 1
