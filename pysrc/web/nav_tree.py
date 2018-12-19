
next_uid = 0

class NavNode:    
        
    def __init__(self,parent,level,text,anchor):
        global next_uid
        self.uid = next_uid
        next_uid += 1
        self.parent = parent          # This node's parent (so we can work backwards)
        self.level = level            # Heading level (starts at 0)
        self.children = []            # Child nodes (if any)
        self.invisibles = []          # Files with no navigation
        self.text = text              # Title shown to the user
        self.anchor = anchor          # The HTML anchor text
        self.expanded = True          # True if the branch is expanded
        self.active_item = False      # True if this item is currently showing
        self.active_item_path = False # True if this item is in the path of the currently showing item
     
    def print_s(self,recurse=True):
        if self.parent:
            par = str(self.parent.uid)
        else:
            par = 'ROOT'
        print('level='+str(self.level)+',anchor='+self.anchor+',id='+str(self.uid)+',parent='+par)
        if recurse:
            for c in self.children:
                c.print_s()
           
    def get_full_path(self):        
        node = self
        ret = node.anchor
        while node.parent:
            ret = node.parent.anchor+'/'+ret
            node = node.parent
        if ret.startswith('/'):
            ret = ret[1:]
        return ret

def collapse_all(node):
    node.expanded = False
    for c in node.children:
        collapse_all(c)                

class NavTree:
    
    def __init__(self):
        
        self.root = NavNode(None,0,'','') # A root node to hold the first levels        
                            
    def add_page_nav(self, level, text, anchor):
        
        # Find the parent level
        node = self.root
        while node.level != (level-1):
            if len(node.children)==0:
                raise Exception('Missing level before '+text)
            node = node.children[-1] # Last child
            
        # Add the new node to the children
        n = NavNode(node,level,text,anchor)
        node.children.append(n)                
        
        return n
    
    '''
    
    <ul>
      <li><a>In the Arcade</a></li>
      <li><a>Dig Sites</a>
        <ul>
          <li><a>Pyramid</a></li>
          <li><a>Invaders</a></li>
        </ul>
      </li>      
      <li><a>Tools</a></li>      
    </ul>
    '''
                            
    def _to_html_rec(self,node,children_only,book_marks):
        
        ret = ''
                
        if not children_only:
        
            classes = ''
            if len(node.children)>0:
                classes += 'branch '  
                if node.expanded:
                    classes += 'expanded '
                else:
                    classes += 'collapsed '                        
            classes = classes.strip()
            
            if classes!='':
                ret = ret+'<li class="'+classes+'">'
            else:
                ret = ret+'<li>'               
            
            classes=''           
            classes = classes.strip()
                                        
            if node.active_item and not book_marks:
                # This is active ... a span
                if len(classes)>0:
                    ret = ret + '<span class="'+classes+'">'+node.text+'</span>'
                else:
                    ret = ret + '<span>'+node.text+'</span>'                
            else:
                # This is not active ... an anchor
                if book_marks:
                    anchor = '#'+node.anchor
                else:
                    anchor = '/'+node.get_full_path()
                    if anchor.endswith('.md'):
                        anchor = anchor[0:-2]+'html'
                if len(classes)>0:
                    ret = ret + '<a href="{anchor}" class="{classes}">{text}</a>'.format(anchor=anchor,classes=classes,text=node.text)
                else:
                    ret = ret + '<a href="{anchor}">{text}</a>'.format(anchor=anchor,text=node.text)     
                
                          
                                
        if len(node.children)>0:
            if not children_only:
                if node.expanded:
                    ret = ret + '<ul>'
                else:
                    ret = ret + '<ul hidden>'                
            for n in node.children:
                ret = ret + self._to_html_rec(n,False,book_marks)
            if not children_only:
                ret = ret + '</ul>'
            
        if not children_only:
            ret = ret + '</li>'
                
        return ret
    
    def to_html(self,book_marks=False):                              
        ret = self._to_html_rec(self.root,True,book_marks)    
        return ret