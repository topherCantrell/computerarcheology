import string

class PageTree:
    
    def __init__(self):
        
        self._tree = {
            'level' : 1,
            'children' : []
        }
        
        self._node = self._tree    
        
        self._used_anchors = []
        
    def _make_valid_anchor(self,text):        
        
        tt = ''
        for t in text:
            if t in string.ascii_letters or t in '0123456789':
                tt+=t
        text = tt
        
        if text in self._used_anchors:
            i = 1
            while True:
                g = text+str(i)
                if not g in self._used_anchors:
                    text = g
                    break
                i += 1
        
        self._used_anchors.append(text)
        return text        
    
    def add_page_nav(self, line):
        
        lev = 0
        while line[lev]=='#':
            lev = lev + 1
            
        text = line[lev:].strip()
        anchor = self._make_valid_anchor(text)
            
        if lev>(self._node['level']+1):
            raise Exception('Missing a level before '+line)
            
        if lev==self._node['level']:
            # This is in the current node ... easy
            self._node['children'].append([anchor,text])
        elif lev>self._node['level']:
            new_level = {
                'level' : lev,
                'children' : [[anchor,text]],
                'parent' : self._node
            }
            self._node['children'].append(new_level)
            self._node = new_level        
        else:
            while self._node['level']!=lev:
                self._node = self._node['parent']
            self._node['children'].append([anchor,text])        
                
    def _to_html_rec(self,node):
        ret = '<ul>'
        for g in node['children']:
            if type(g) is dict:
                ret += self._to_html_rec(g)
            else:
                ret = ret + '<a href="'+g[0]+'">'+g[1]+'</a>'
        ret += '</ul>'
        return ret
    
    def to_html(self):
        # Each string is a <li>
        # Each dict is a <ul>
        ret = self._to_html_rec(self._tree)
        print(ret)
        return ret