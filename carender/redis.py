from opcodetools.cpu import cpu_manager

import carender.cacode

fname = 'Bank1F'

cpu = cpu_manager.get_cpu_by_name('Z80GB')

with open(f'../content/gameboy/zelda/{fname}.md') as f:
    with open(f'../content/gameboy/zelda/{fname}.redis.md', 'w') as h:
        for line in f:
            sp = carender.cacode.split_disassembly_line(line)
            if sp['address'] and sp['opcode']:
                ops = cpu.find_opcodes_for_binary(sp['data'], True)[0]
                mn = ops.mnemonic
                i = mn.find(' ')
                j = sp['opcode'].find(' ')
                if i >= 0 and j >= 0:
                    mn = mn[:i].ljust(8, ' ') + sp['opcode'][j + 1:]
                nl = line[0:17] + mn
                if sp['comment'] is not None:
                    nl = nl + ' ;' + sp['comment']
                line = nl + '\n'
            h.write(line)
                
