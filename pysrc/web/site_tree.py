import os
import web.ENVIRONMENT as ENV
import web.make_web
import copy

def _load_directory(d):
    info = web.make_web.read_deploy(d)    
    ret = []
    for e in info:
        if e=='README.md' or e.startswith('+'):
            continue
        if os.path.isdir(os.path.join(d,e)):
            ret.append({
                'Name' : e,
                'Children' : _load_directory(os.path.join(d,e)),
                'Hidden' : True,
                'Collapsed' : True,
                'PagePath' : False
                # TODO oops ... site navigation may not be the dir name. For
                # instance: dir /CoCo/MadnessMinotaur is title "/CoCo/Madness & Minotaur"
                # TODO Children need to be:
                #  active   /a/b   bb
                # [False,   href,  text]
            })
        else:
            ret.append(e)
    return ret

'''

<ul>
  <li><a>Arcade</a></li>
  <ul> ... Arcade ... </ul>
  
  <li><a>CoCo</a></li>
  <ul> ... CoCo ... </ul
  
</ul>

Each entry in the tree is a <li> and a <ul> pair. If the <li> is a leaf, then there is
no <ul>. 

If the node has a <ul> then it can be collapsed or open. These are "+" and "-" icons
on the item. If the item is collapsed then the <li> has class "collapsed" and the <ul> 
is hidden. If the item is open then the <li> has class "expanded" and the <ul> is
not hidden.

An <li> without children has no "collapsed" or "expanded" class

Anchors that are active on the right become <span>s with class 'selectedPage'. Thus
these are informational and not clickable.

Anchors that are in the path to the selected item have class 'selectedPagePath'

'''

def _make_site_tree_rec(node):
    ret = '<ul>'
    for n in node:
        if type(n) is dict:
            ret += '<a href="???">'+n['Name']+'<a>'
            ret += _make_site_tree_rec(n['Children'])
        else:
            ret += '<li><a href="???">'+n+'</a></li>'
    ret += '</ul>'
    return ret

# Make a fake root node
_root_navs = _load_directory(ENV.CONTENT_DIR)

def make_site_nav(path):
    global _tree
    ret = copy.deepcopy(_tree)
    # TODO opens and closes here
    # TODO make HTML here
    return _make_site_tree_rec(_root_navs)
    
    
