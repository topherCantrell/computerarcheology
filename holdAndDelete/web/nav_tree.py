
next_uid = 0


class NavNode:

    def __init__(self, parent, level, text, anchor, display_class):
        global next_uid
        text = text.strip()
        self.uid = next_uid
        next_uid += 1
        # This node's parent (so we can work backwards)
        self.parent = parent
        self.level = level            # Heading level (starts at 0)
        self.children = []            # Child nodes (if any)
        self.invisibles = []          # Files with no navigation
        self.text = text              # Title shown to the user
        self.anchor = anchor          # The HTML anchor text
        self.expanded = True          # True if the branch is expanded
        self.active_item = False      # True if this item is currently showing
        self.hidden = False
        # True if this item is in the path of the currently showing item
        self.active_item_path = False
        self.display_type = display_class

    def print_s(self, recurse=True):
        if self.parent:
            par = str(self.parent.uid)
        else:
            par = 'ROOT'
        print('level=' + str(self.level) + ',anchor=' +
              self.anchor + ',id=' + str(self.uid) + ',parent=' + par)
        if recurse:
            for c in self.children:
                c.print_s()

    def get_full_path(self):
        node = self
        ret = node.anchor
        while node.parent:
            ret = node.parent.anchor + '/' + ret
            node = node.parent
        if ret.startswith('/'):
            ret = ret[1:]
        return ret

    def find_child_named(self, anchor):
        for c in self.children:
            if c.anchor == anchor:
                return c
        return None


class NavTree:

    def __init__(self):

        # A root node to hold the first levels
        self.root = NavNode(None, 0, '', '', None)

    def add_page_nav(self, level, text, anchor, display_class):
        # Find the parent level
        node = self.root
        while node.level != (level - 1):
            if len(node.children) == 0:
                raise Exception('Missing level before ' + text)
            node = node.children[-1]  # Last child

        # Add the new node to the children
        n = NavNode(node, level, text, anchor, display_class)
        node.children.append(n)

        return n

    def to_html(self, book_marks=False):
        return to_html(self.root, book_marks)

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


def _to_html_rec(node, children_only, book_marks):

    ret = ''

    if node.text.startswith('*'):
        return ret

    if not children_only:

        classes = ''
        if len(node.children) > 0:
            classes += 'branch '
            if node.expanded:
                classes += 'expanded '
            else:
                classes += 'collapsed '
        classes = classes.strip()

        if classes != '':
            ret = ret + '<li class="' + classes + '">'
        else:
            ret = ret + '<li>'

        # Different anchor syntax for intra/inter page links
        if book_marks:
            anchor = '#' + node.anchor
        else:
            anchor = '/' + node.get_full_path()
            if anchor.endswith('.md'):
                anchor = anchor[0:-2] + 'html'

        disp_class = ''
        if node.display_type:
            disp_class = 'pageNav_' + node.display_type

        if node.text.endswith('-'):
            ret = ret + '<hr class="navSeparator">'
        elif node.active_item:
            ret = ret + '<span class="activeItem ' + \
                disp_class + '">' + node.text + '</span>'
        elif node.active_item_path:
            ret = ret + \
                ('<a href="{anchor}" class="activeItemPath ' + disp_class + '">{text}</a>').format(
                    anchor=anchor, text=node.text)
        else:
            ret = ret + \
                '<a href="{anchor}" class="{disp_class}">{text}</a>'.format(
                    anchor=anchor, disp_class=disp_class, text=node.text)

    if len(node.children) > 0:
        if not children_only:
            if node.expanded:
                ret = ret + '<ul>'
            else:
                ret = ret + '<ul hidden>'
        for n in node.children:
            ret = ret + _to_html_rec(n, False, book_marks)
        if not children_only:
            ret = ret + '</ul>'

    if not children_only:
        ret = ret + '</li>'

    return ret


def collapse_all(node):
    node.expanded = False
    for c in node.children:
        collapse_all(c)


def to_html(node, book_marks=False):
    ret = _to_html_rec(node, True, book_marks)
    return ret
