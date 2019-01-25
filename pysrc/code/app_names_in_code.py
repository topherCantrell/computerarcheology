
import code.markdown_line
import code.process_code
from code.memory_table import MemoryTable

import os
from code.directive_line import Directive
from code.paragraph_line import Paragraph
from code.header_line import HeaderLine
from code.block_line import Block
from code.code_line import CodeLine

# FILE_NAME = '../../content/CoCo/Pyramid/Code.md'
FILE_NAME = '../../content/CoCo/AudioSpectrumAnalyzer/Code.md'

lines = code.markdown_line.load_file(FILE_NAME)
dirname = os.path.dirname(FILE_NAME)

code_info = {
    'memory' : {}
}

# Line by line from the top ... here we go    
i = -1
while i < len(lines)-1:
    i+=1
    # Keeping the index in case we have to look backwards
    md = lines[i]

    if type(md) is Directive:
        if md.directive.startswith('cpu'):
            name = md.directive[3:].strip()
            code_info['cpu_name'] = name
            if name == '6809':
                import cpu.cpu_6809
                code_info['cpu'] = cpu.cpu_6809.CPU_6809()                
            else:
                raise Exception("Unknown CPU "+name)
        elif md.directive.startswith('memoryTable '):                
                name = md.directive[12:].strip()               
                text = lines[i+1].lines[0].line
                k = text.index('](')
                j = text.index(')',k)
                code_info['memory'][name] = MemoryTable(os.path.join(dirname,text[k+2:j]))

code.process_code.process_code(lines,code_info,skip_no_label_jumps=True)

for md in lines:
    if type(md) is Block:
        for m in md.lines:
            if type(m) is CodeLine:
                print(m.original.line)
            else:
                print(m.line)  
    elif type(md) is Paragraph or type(md) is code.list_line.ListLine:        
        for m in md.lines:
            print(m.line)            
    elif type(md) is HeaderLine or type(md) is Directive:
        print(md.original.line)
    else:
        print(md.line)
