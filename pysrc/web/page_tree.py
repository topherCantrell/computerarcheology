
class PageTree:
    
    def __init__(self):
        
        self._tree = {
            'level' : 1,
            'children' : []
        }
        
        self._node = self._tree    
        
        self._used_anchors = []
            
    def add_page_nav(self, level, anchor, text):
            
        if level>(self._node['level']+1):
            raise Exception('Missing a level before '+text)
            
        if level==self._node['level']:
            # This is in the current node ... easy
            self._node['children'].append([anchor,text])
        elif level>self._node['level']:
            new_level = {
                'level' : level,
                'children' : [[anchor,text]],
                'parent' : self._node
            }
            self._node['children'].append(new_level)
            self._node = new_level        
        else:
            while self._node['level']!=level:
                self._node = self._node['parent']
            self._node['children'].append([anchor,text])        
    
    '''
    
    <ul>
      <li><a>Dig Sites</a></li>
      <ul> ... Sites ... </ul>
      
      <li><a>Tools</a></li>
      <ul> ... Tools ... </ul
      
    </ul>
    '''
                            
    def _to_html_rec(self,node):
        ret = '<ul>'
        for g in node['children']:
            if type(g) is dict:
                ret += self._to_html_rec(g)
            else:
                ret = ret + '<li class="expanded"><a href="#'+g[0]+'">'+g[1]+'</a></li>'
        ret += '</ul>'
        return ret
    
    def to_html(self):
        # Each string is a <li>
        # Each dict is a <ul>
        ret = self._to_html_rec(self._tree)[4:-5]     
        print(ret)  
        return ret