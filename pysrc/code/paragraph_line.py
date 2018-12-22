def process_markdown(text):
    
    # Links and images
    while '](' in text:
        j = text.index('](')
        i = j
        while i>0 and text[i]!='[':
            i -= 1       
        k = text.index(')',j)
        m = i
        is_img = False
        if i>0 and text[i-1]=='!':
            m = i-1
            is_img = True
            print("GOT IMAGE "+text)
            
        if is_img:
            rep = '<img src="'+text[j+2:k]+'">'
        else:
            rep = '<a href="'+text[j+2:k]+'">'+text[i+1:j]+'</a>'
        
        text=text[0:m]+rep+text[k+1:]
        
    # TODO bold, italic
    # TODO `stuff`
        
    return text

class Paragraph:
    
    def __init__(self):
        self.lines = []
        
    def make_content(self):
        if len(self.lines)==0:
            return ''
        ret='<p>\n'
        for md in self.lines:                
            ret += process_markdown(md.line) + '\n'                
        ret+='</p>\n' 
        
        return ret