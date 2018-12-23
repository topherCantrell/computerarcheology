class Block:
    
    def __init__(self,first):
        self.lines = []
        self.type = first.line.strip()[3:].strip()        
        
    def get_type(self):
        return self.type
    
    def add_line(self,line):
        self.lines.append(line)
        
    def make_content(self,code_info):
                
        if self.type=='html':
            return self.make_content_html()
        
        if self.type=='code':
            return self.make_content_code(code_info)
        
        if self.type=='plain':
            return self.make_content_plain()
        
        if self.type=='':
            return self.make_content_none()
        
        raise Exception('Unknown block type '+self.type)
    
    def make_content_plain(self):
        ret = '<pre class="block_plainCode">\n'
        for md in self.lines[1:-1]:
            ret+=md.line+'\n'
        ret += '</pre>'
        return ret            
    
    def make_content_html(self):
        ret = ''
        for md in self.lines[1:-1]:
            ret+=md.line+'\n'
        return ret
    
    def make_content_none(self):
        ret = '<pre>\n'
        for md in self.lines[1:-1]:
            ret+=md.line+'\n'
        ret += '</pre>'
        return ret
    
    def make_content_code(self,code_info):
        # TODO references to RAM
        # TODO links in jumps
        print(code_info['memory'])
        return '<pre>'+str(code_info)+'</pre>'
        
        