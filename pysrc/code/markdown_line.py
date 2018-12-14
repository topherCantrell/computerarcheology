from code.directive_line import Directive
from code.block_line import Block
from code.code_line import CodeLine

class MarkdownLine:
    
    def __init__(self,line,filename,linenumber):
        self.line = line
        self.filename = filename
        self.linenumber = linenumber

def get_deploy(lines):
    
    ret = [['README.md','']]
    
    found = False
    
    for g in lines:
        if found:
            if type(g) is Directive:
                g = g.directive
                if '<br>' in g:
                    g = g[0:g.index('<br>')].strip()
                if g=='README.md':
                    continue
                
                if ':' in g:
                    i = g.index(':')
                    t = g[i+1:].strip()
                    g = g[0:i].strip()
                    if g.endswith('/'):
                        g = g[0:-1]
                else:
                    if g.endswith('/'):
                        g = g[0:-1]
                    t = g
                    if t.endswith('.md'):
                        t = t[0:-3]
                
                ret.append([g,t])
            else:
                return ret
        else:            
            if type(g) is Directive :
                found = True
                
    return ret
        
def load_file(filename):
    
    lines = []
    
    # Everything comes in as a generic line
    with open(filename,'r') as f:
        while True:
            line = f.readline()
            if line=='':
                break
            if line.endswith('\n'):
                line = line[0:-1]
            lines.append(MarkdownLine(line,filename,len(lines)))
            
    # Collect all the blocks together
    in_block = False
    lines_n = []
    block = None
    for md in lines:
        if in_block:            
            if md.line.strip().startswith('```'):
                block.add_line(md)
                in_block = False
            else:
                # Parse the block types while we are here
                if block.type=='code':
                    block.add_line(CodeLine(md))
                else:
                    block.add_line(md)            
        else:
            if md.line.strip().startswith('```'):
                in_block = True
                block = Block(md)
                block.add_line(md)
                lines_n.append(block)
            else:
                lines_n.append(md)
    lines = lines_n                   
        
    # Parse directives
    for i in range(len(lines)):
        md = lines[i]
        if type(md) is MarkdownLine:            
            if md.line.strip().startswith('>>>'):
                lines[i] = Directive(md)
                
    return lines
    
load_file('../../content/CoCo/Pyramid/Code.md')