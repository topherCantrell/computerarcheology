import copy
import os
import shutil
import sys

from computerarcheology.carender import markdown, cainfo, webrender, nav_tree, names_in_code
import computerarcheology.carender.ENVIRONMENT as ENV

# D:\git\computerarcheology> py -m computerarcheology.carender.app 

# Make sure "opcodetools" is in your path. I put this one-line "opcodetools.pth" file in python11/Lib/site-packages:
# d:/git/opcodetools

# For development, you can pass command line arguments to this script to control which
# markdowns are processed. All other non-md are always processed.
#
# The following things are always generated no matter what work-limit given.

NO_WORK_LIMIT = [
    'content/js',
    'content/css',
    'content/img',
    'content/Contact',        
    'content/Journal',
    'content/misc',
    'content/Tools',
]

def deploy_directory(current_node):
    ''' Recursively deploy a directory

        All files and markdowns in a single directory, and recursively call
        this function for sub directories.

        params:
          current_node (NavNode): the current NavNode deployment information node

    '''
    fp_content = os.path.join(ENV.CONTENT_DIR, current_node.get_full_path())
    fp_deploy = os.path.join(ENV.DEPLOY_DIR, current_node.get_full_path())
    if fp_deploy.endswith('\\'):
        fp_deploy = fp_deploy[:-1]

    for dep in current_node.invisibles:
        # This is just a blind copy -- no processing
        src = os.path.join(fp_content, dep)
        dst = os.path.join(fp_deploy, dep)
        if os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            shutil.copy(src, dst)

    for dep in current_node.children:       
        
        da = dep.anchor
        genbin = False
        if dep.special == '%':            
            genbin = True
        src = os.path.join(fp_content, da)
        dst = os.path.join(fp_deploy, da)
        if os.path.isdir(src):
            os.makedirs(dst)
            deploy_directory(dep)
        else:
            if src.endswith('-'):
                # Divider
                continue
            print(src)
            
            if not src.endswith('.md'):
                shutil.copy(src, dst)
            else:                
                
                skip_work = False
                if not src.endswith('README.md') and work_limit:
                    skip_work = True
                    lim = fp_content[2:].replace('\\','/')                           
                    # Limit the work on md files                    
                    for l in NO_WORK_LIMIT+[work_limit]:                        
                        if l in lim:
                            skip_work = False
                            break

                if skip_work:
                    print('## Work limit. Skipping '+src)
                    continue

                md,bindata = names_in_code.update_names_in_code(fp_content, da,extract_binary=genbin)

                if genbin:                    
                    print('Making binary '+dst+'.bin')
                    with open(dst+'.bin','wb') as f:
                        f.write(bindata)                    
                
                # md = markdown.read_markdown_paragraphs(src)
                
                title = ''
                image = ''
                
                if md[0].group_type == 'TEXT' and md[0].lines[0].text.strip().startswith('!['):
                    txt = md[0].lines[0].text.strip()
                    i = txt.find('](')
                    title = txt[2:i]
                    image = txt[i + 2:-1]
                    md = md[1:]
                                    
                content, page_nav = webrender.render_content(md, fp_content)
                                
                info = {
                    'TITLE': title,
                    'IMAGE': image,
                    'BREAD_CRUMBS': '',  # filled in below
                    'SITE_TREE': '',  # filled in below
                    'PAGE_TREE': page_nav,
                    'CONTENT': content
                } 
                
                # Make the breadcrumbs
                
                cr = []
                n = dep
                if n.anchor != 'README.md':
                    cr.append(n)
                while n.parent is not None:
                    cr = [n.parent] + cr
                    n = n.parent
            
                cr[0] = nav_tree.NavNode(None, 1, 'Home', '', None)
                crumbs = ''
                for n in cr:
                    tt = n.text                    
                    if n == cr[-1]:
                        crumbs += '<li class="active"><span>' + tt + '</span></li>'
                    else:
                        crumbs += '<li><a href="/' + n.get_full_path() + '">' + tt + '</a></li>'
            
                info['BREAD_CRUMBS'] = crumbs
                
                # Make the site tree
            
                # Find the root
                root = dep
                while root.parent:
                    root = root.parent
            
                # Make a copy. We are about to have our way with it.
                cpy = copy.deepcopy(root)            
                
                # Collapse everything
                nav_tree.collapse_all(cpy)
                            
                pics = dep.get_full_path().split('/')
                if pics and pics[0]:                
                    node = cpy
                    for p in pics:
                        node = node.find_child_named(p)                    
                        node.expanded = True
                        node.active_item_path = True
                    if pics[-1] == 'README.md':
                        node.parent.active_item = True
                    else:
                        node.active_item = True                
            
                info['SITE_TREE'] = nav_tree.to_html(cpy)
                              
                with open(os.path.join(ENV.CONTENT_DIR, 'master.template')) as f:
                    txt = f.read()

                txt = webrender.substitute(txt, info)

                if dep.anchor == 'README.md':
                    dep.anchor = 'index.html'
                else:
                    dep.anchor = dep.anchor[0:-2] + 'html'

                with open(os.path.join(ENV.DEPLOY_DIR, dep.get_full_path()), 'w') as f:
                    f.write(txt)

"""
Examples:

py -m computerarcheology.carender.app
py -m computerarcheology.carender.app CoCo/Daggorath

py -m computerarcheology.carender.development_server

"""

work_limit = None
if len(sys.argv)>1:
    work_limit = sys.argv[1]

# Remove and recreate the deployment directory (clean)
if os.path.isdir(ENV.DEPLOY_DIR):
    shutil.rmtree(ENV.DEPLOY_DIR)
os.makedirs(ENV.DEPLOY_DIR)

# Load the info on the site
info = cainfo.load_site_directory()

# Deploy the web pages (locally)
deploy_directory(info.root)
