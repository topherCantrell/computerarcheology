from code.directive_line import Directive
from code.block_line import Block
from code.code_line import CodeLine
from code.table_line import Table
from code.list_line import ListLine
from code.paragraph_line import Paragraph
from code.header_line import HeaderLine

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

def is_text_a_list_item(text):
    g = text.strip()
    # TODO numbered lists too
    if g.startswith('-') or g.startswith('*'):
        return True
    return False
        
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
            
    # Collect all the formal blocks together
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
    
    # Tables are blocks too ... all the lines that start with '|'    
    i = len(lines)
    while i>0:
        i-=1
        md = lines[i]
        if type(md) is MarkdownLine and md.line.strip().startswith('|'):
            table = Table()
            while type(md) is MarkdownLine and md.line.strip().startswith('|'):
                table.lines.insert(0,md)
                del lines[i]
                i -= 1
                md = lines[i]
            lines.insert(i+1,table)                
    
    # Lists are blocks too ... all the lines start with a '-' or '*' or 'n. '
    i = len(lines)
    while i>0:
        i-=1
        md = lines[i]
        if type(md) is MarkdownLine and is_text_a_list_item(md.line):
            lst = ListLine()
            while type(md) is MarkdownLine and is_text_a_list_item(md.line):
                lst.lines.insert(0,md)
                del lines[i]
                i -= 1
                md = lines[i]
            lines.insert(i+1,lst)
        
    # Parse directives
    i = len(lines)
    while i>0:
        i-=1
        md = lines[i]
        if type(md) is MarkdownLine:            
            if md.line.strip().startswith('>>>'):
                lines[i] = Directive(md)
                
    # Parse headers
    i = len(lines)
    while i>0:
        i-=1
        md = lines[i]
        if type(md) is MarkdownLine:            
            if md.line.strip().startswith('#'):
                lines[i] = HeaderLine(md)
                
    # Everything else is a paragraph
    i = len(lines)
    while i>0:
        i-=1
        md = lines[i]
        if type(md) is MarkdownLine:
            text = Paragraph()
            while type(md) is MarkdownLine and md.line.strip()!='':
                text.lines.insert(0,md)
                del lines[i]
                i -= 1
                if i<0:
                    break
                md = lines[i]            
            lines.insert(i+1,text)
            
    # Remove empty paragraphs
    i = len(lines)
    while i>0:
        i-=1
        md = lines[i]
        if type(md) is Paragraph:        
            pc = 0
            for m in md.lines:
                if m.line.strip()!='':
                    pc+=1
            if pc==0:
                del lines[i]    
           
    return lines
    
load_file('../../content/CoCo/Pyramid/Code.md')