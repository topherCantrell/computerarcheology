
class NavNode:
    
    def __init__(self,level,text,anchor):
        self.level = level            # Heading level (starts at 0)
        self.children = []            # Child nodes (if any)
        self.text = text              # Title shown to the user
        self.anchor = anchor          # The HTML anchor text
        self.expanded = True          # True if the branch is expanded
        self.active_item = False      # True if this item is currently showing
        self.active_item_path = False # True if this item is in the path of the currently showing item      

class NavTree:
    
    def __init__(self):
        
        self._tree = NavNode(0,'','') # A root node to hold the first levels        
                            
    def add_page_nav(self, level, text, anchor):
        
        # Find the parent level
        node = self._tree
        while node.level != (level-1):
            if len(node.children)==0:
                raise Exception('Missing level before '+text)
            node = node.children[-1] # Last child
            
        # Add the new node to the children
        n = NavNode(level,text,anchor)
        node.children.append(n)                
    
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
                            
    def _to_html_rec(self,node,children_only=False):
        
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
            if node.expanded and len(node.children)>0:
                classes += 'expanded '
            if node.active_item_path:
                classes += 'activeItemPath '
            if node.active_item:
                classes += 'activeItem '
            classes = classes.strip()
                                        
            if node.active_item:
                # This is active ... a span
                if len(classes)>0:
                    ret = ret + '<span classes="'+classes+'">'+node.text+'</span>'
                else:
                    ret = ret + '<span>'+node.text+'</span>'                
            else:
                # This is not active ... an anchor
                if len(classes)>0:
                    ret = ret + '<a href="{anchor}" classes="{classes}">{text}</a>'.format(anchor=node.anchor,classes=classes,text=node.text)
                else:
                    ret = ret + '<a href="{anchor}">{text}</a>'.format(anchor=node.anchor,text=node.text)               
                                
        if len(node.children)>0:
            if not children_only:
                ret = ret + '<ul>'
            for n in node.children:
                ret = ret + self._to_html_rec(n)
            if not children_only:
                ret = ret + '</ul>'
            
        if not children_only:
            ret = ret + '</li>'
                
        return ret
    
    def to_html(self):                              
        ret = self._to_html_rec(self._tree,True)    
        return ret