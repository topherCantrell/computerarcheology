'''
Tags of the form "{...}" are totally controlled by the code. The code will remove them
and add the correct value back.

Tags of the form "{!...}" are not touched. These are manually added by the human.

Tags of the form "{+...}" tell the code to override the "not a name opcode" and to
treat the value as a name. The code will replace the name with the correct value.

Tags of the form "{-}" tell the code to override the "is a name opcode".

  LDA  $4000     ; {lives}
  LDX  #$4000    ; {+lives}
  LDB  $4000,X   ; {!lives}
  LDB  $4000     ; {-}
'''

import opcodetools.cpu.cpu_manager

import cacode
import cainfo
import markdown


def update_names_in_code(filename, directory):

    # if 'Gameboy' in directory:
    #    # TODO lots of work
    #    return

    # Load the markdown file
    md = markdown.read_markdown_paragraphs(filename)

    # Get the code info

    cpu_name = cainfo.read_cpu(md)
    lines = cainfo.read_code_text_lines(md)
    tables = cainfo.read_memory_tables(md, directory)

    if not lines:
        # No code in this file
        return

    cpu = opcodetools.cpu.cpu_manager.get_cpu_by_name(cpu_name)

    # Make sure code binary matches binary file
    gaps = cainfo.read_origin_gaps(md)
    binary_file = cainfo.read_binary_file_name(md)
    info = cacode.load_binary_files(binary_file, directory)
    origin = info['origin']
    binary_org = info['data']
    origin_md, binary_md = cacode.parse_binary(lines, gaps)
    binary_md = bytes(binary_md)
    if origin_md != origin:
        raise Exception('Binary origins are different')
    if len(binary_org) != len(binary_md):
        raise Exception('Binary data has different length')
    for i in range(len(binary_org)):
        if binary_org[i] != binary_md[i]:
            raise Exception('First binary difference at ' + hex(i) + ' ' + hex(binary_md[i]) + ' ' + hex(binary_org[i]))

    # Find the opcodes for all the disassembly lines

    line_details = []
    for line in lines:
        parts = cacode.split_disassembly_line(line)
        opcode = None
        if parts['opcode']:
            opcode = cpu.find_opcodes_for_binary(parts['data'], True)
            if not opcode:
                raise Exception('No opcode found: ' + line)
            # if len(opcode) > 1:
            #    for o in opcode:
            #        print(o.mnemonic)
            #    raise Exception('Multiple opcodes found: ' + line)
            opcode = opcode[0]
            
            a = opcode.mnemonic.split()
            b = parts['opcode'].split()
            if a[0] != b[0]:
                # TODO
                if b[0] != 'BCS' and b[0] != 'ASLB' and b[0] != 'BCC' and b[0] != 'LBCC' and b[0] != 'LBCS' and b[0] != 'LSLA' and b[0] != 'LSLB' and b[0] != 'LSL'  and b[0] != 'ASL':
                    raise Exception('Check on opcode: ' + str(parts) + ' ' + str(opcode.mnemonic))
            
        line_details.append([line, parts, opcode])


if __name__ == '__main__':
    update_names_in_code('../content/arcade/spaceinvaders/code.md', '../content/arcade/spaceinvaders')
