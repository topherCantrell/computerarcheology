
'''

A navigation item is a <li> followed by its <ul> of children.

An <li> that has <ul> children is given the class "branch". That creates a +/- box
to expand/collapse the node.

'''

class NavTree:
    
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
            
    def expand_all(self,expand=True,node=None):
        if node==None:
            node = self._tree
        for i in range(len(node['children'])):
            pass
                            
    def _to_html_rec(self,node):
        if len(node['children'])==0:
            return ''        
        ret = '<ul>'
        for i in range(len(node['children'])):
            g = node['children'][i]        
            if type(g) is dict:
                ret += self._to_html_rec(g)
            else:
                if i<len(node['children'])-1 and type(node['children'][i+1])==dict:
                    ret = ret + '<li class="branch expanded"><a href="#'+g[0]+'">'+g[1]+'</a></li>'
                else:
                    ret = ret + '<li><a href="#'+g[0]+'">'+g[1]+'</a></li>'
        ret += '</ul>'
        return ret
    
    def to_html(self):
        # Each string is a <li>
        # Each dict is a <ul>
        ret = self._to_html_rec(self._tree)[4:-5]     
        print(ret)  
        return ret