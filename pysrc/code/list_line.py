import code.paragraph_line

class ListLine:
    
    def __init__(self):
        self.lines = []
        
    def make_content(self):
        # TODO embellish as needed!
        indent = self.lines[0].line.index('*')
        for md in self.lines:
            i = md.line.index('*')
            if i != indent:
                raise Exception('TODO Nested lists not implemented')
            
        ret = '<ul>\n'
        for md in self.lines:
            line_strip = md.line.strip()
            line_strip = line_strip[1:].strip()
            ret += '<li>' + code.paragraph_line.process_markdown(line_strip)+'</li>\n'        
        ret += '</ul>\n'            
        return ret