from code.directive_line import Directive
from code.block_line import Block

import code.markdown_line

import os

from code.memory_table import MemoryTable

FILE_NAME = '../../content/CoCo/Pyramid/Code.md'

lines = code.markdown_line.load_file(FILE_NAME)
dirname = os.path.dirname(FILE_NAME)

memory_tables = {}

# Load all the memory tables
for i in range(len(lines)):
    md = lines[i]
    if type(md) is Directive and md.directive.startswith('memoryTable'):
        name = md.directive[11:].strip()
        link = lines[i+1].line
        j = link.index('](')
        k = link.index(')',j+2)
        fname = link[j+2:k]
        path = os.path.join(dirname,fname)
        memory_tables[name] = MemoryTable(path)         
        
# Gather the code together in one list
code = [] 
for md in lines:
    if type(md) == Block and md.type == 'code':
        code += md.lines[1:-1]
    
# Get the addresses of each label in the code
code_labels = {}   
for i in range(len(code)):
    c = code[i]    
    if c.label != None:
        if c.label in code_labels:
            raise Exception("Label '"+c.label+"' has multiple definitions.")
        nc = None
        for j in range(i+1,len(code)):
            if code[j].address!=None:
                nc = code[j]
                break
        if nc==None:
            raise Exception('No address after label '+c.label)                            
        code_labels[c.label] = nc.address

for c in code:
    if c.comment and c.comment.startswith('{'):
        print(c.original.line)