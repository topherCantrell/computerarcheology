
import os

import code.block_line
import code.code_line
import code.directive_line
import code.header_line
import code.markdown_line
import code.markdown_utils
import code.memory_table
import code.paragraph_line
import code.process_code


# FILE_NAME = '../../content/CoCo/Pyramid/Code.md'
FILE_NAME = '../../content/CoCo/AudioSpectrumAnalyzer/Code.md'

lines = code.markdown_utils.load_file(FILE_NAME)
dirname = os.path.dirname(FILE_NAME)

code_info = {
    'memory': {}
}

# Line by text from the top ... here we go
i = -1
while i < len(lines) - 1:
    i += 1
    # Keeping the index in case we have to look backwards
    md = lines[i]

    if type(md) is code.directive_line.Directive:
        if md.directive.startswith('cpu'):
            name = md.directive[3:].strip()
            code_info['cpu_name'] = name
            if name == '6809':
                import cpu.cpu_6809
                code_info['cpu'] = cpu.cpu_6809.CPU_6809()
            else:
                raise Exception("Unknown CPU " + name)
        elif md.directive.startswith('memoryTable '):
            name = md.directive[12:].strip()
            text = lines[i + 1].lines[0].text
            k = text.index('](')
            j = text.index(')', k)
            code_info['memory'][name] = code.memory_table.MemoryTable(
                os.path.join(dirname, text[k + 2:j]))

code.process_code.process_code(lines, code_info, skip_no_label_jumps=True)

for md in lines:
    if type(md) is code.block_line.Block:
        for m in md.lines:
            if type(m) is code.code_line.CodeLine:
                print(m.original.text)
            else:
                print(m.text)
    elif type(md) is code.paragraph_line.Paragraph or type(md) is code.list_line.ListLine:
        for m in md.lines:
            print(m.text)
    elif type(md) is code.header_line.HeaderLine or type(md) is code.directive_line.Directive:
        print(md.original.text)
    else:
        print(md.text)