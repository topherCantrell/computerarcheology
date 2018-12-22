import code.paragraph_line

class Table:
    
    def __init__(self):
        self.lines = []
        self.is_memory = False
        
    def make_content(self):
        # TODO embellish as needed
        
        classes = 'table table-condensed'
        if self.is_memory:
            classes += ' memoryMapTable'
        ret = '<table class="'+classes+'">\n'
        ret += '<thead>\n'
        
        cols = self.lines[0].line.split('|')[1:-1]
        ret+='<tr>'
        for c in cols:
            ret += '<th>'+code.paragraph_line.process_markdown(c)+'</th>'
        ret+='</tr>\n'        
        ret += '</thead>\n'
        
        ret += '<tbody>\n'        
        for bod in self.lines[2:]:
            cols = bod.line.split('|')[1:-1]
            ret+='<tr>'
            for c in cols:
                ret += '<td>'+code.paragraph_line.process_markdown(c)+'</td>'   
            ret+='</tr>\n'     
        ret += '</tbody>\n'
        
        ret += '</table>\n'
        return ret