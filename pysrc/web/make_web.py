import copy
import os
import shutil

from code.block_line import Block
from code.directive_line import Directive
from code.header_line import HeaderLine
from code.list_line import ListLine
import code.markdown_line
import code.markdown_utils
from code.memory_table import MemoryTable
from code.paragraph_line import Paragraph
from code.table_line import Table
import web.ENVIRONMENT as ENV
from web.id_mgr import IDMgr
from web.nav_tree import NavTree
import web.nav_tree


def process_markdown(lines, site_nav_node, fp_content):
    ''' Process a single markdown file

        params:
          lines (list): the lines loaded and pre-parsed from the file
          site_nav_node (NavNode): the navigation node for this file

    '''

    # print(fp_content)

    code_info = {
        'memory': {}
    }

    # Used to make unique anchor ids on this page
    ids = IDMgr()

    # Used to build the page's navigation tab
    page_nav = NavTree()

    # All the different pieces of the page
    ret = {}

    # The HTML content of the page
    content = ''

    # Image and Title ... both before the first header
    fnd = False
    for md in lines:
        if type(md) is HeaderLine:
            break
        if type(md) is not Paragraph:
            continue
        k = 0
        while k < len(md.get_lines()):
            m = md.get_lines()[k]
            if m.text.startswith('!['):
                i = m.text.index('](')
                ret['TITLE'] = m.text[2:i].strip()
                j = m.text.rindex(')')
                ret['IMAGE'] = m.text[i + 2:j].strip()
                if ret['TITLE'] == '':
                    ret['TITLE'] = ret['IMAGE'][0:ret['IMAGE'].rindex('.')]
                del md.get_lines()[k]
                fnd = True
                break
            k += 1
        if fnd:
            break

    # Line by text from the top ... here we go
    i = -1
    while i < len(lines) - 1:
        i += 1
        # Keeping the index in case we have to look backwards
        md = lines[i]

        # Skip over the deploy descriptor
        if type(md) is Directive and md.directive.startswith('deploy:'):
            while type(md) is Directive:
                i += 1
                md = lines[i]

        if type(md) is Directive:
            if md.directive.startswith('playMe'):
                content += '<div class="playMe">'
                continue
            if md.directive.startswith('tourGuide'):
                content += '<div class="tourGuide">'
                continue
            if md.directive.startswith('}'):
                content += '</div>'
                continue
            if md.directive == 'memory':
                continue
            if md.directive.startswith('cpu'):
                name = md.directive[3:].strip()
                code_info['cpu_name'] = name
                if name == '6809':
                    import cpu.cpu_6809
                    code_info['cpu'] = cpu.cpu_6809.CPU_6809()
                elif name == '6502':
                    import cpu.cpu_6502
                    code_info['cpu'] = cpu.cpu_6502.CPU_6502()
                elif name == 'DVG':
                    import cpu.cpu_DVG
                    code_info['cpu'] = cpu.cpu_DVG.CPU_DVG()
                elif name == 'Z80':
                    import cpu.cpu_Z80
                    code_info['cpu'] = cpu.cpu_Z80.CPU_Z80()
                elif name == '6803':
                    import cpu.cpu_6803
                    code_info['cpu'] = cpu.cpu_6803.CPU_6803()
                elif name == 'Z80GB':
                    import cpu.cpu_Z80GB
                    code_info['cpu'] = cpu.cpu_Z80GB.CPU_Z80GB()
                else:
                    raise Exception("Unknown CPU " + name)

                continue
            if md.directive.startswith('code'):
                # TODO any special processing for these? Maybe load the memory
                # tables?
                continue
            if md.directive.startswith('memoryTable '):
                name = md.directive[12:].strip()
                text = lines[i + 1].get_lines()[0].text
                k = text.index('](')
                j = text.index(')', k)
                code_info['memory'][name] = MemoryTable(
                    os.path.join(fp_content, text[k + 2:j]))
                continue

            if md.directive.startswith('directPage '):
                dp = int(md.directive[11:].strip(), 16)
                code_info['dp'] = dp
                continue

            raise Exception('Unknown directive :' + md.directive + ':')

        if type(md) is Block:
            content += md.make_content(code_info, lines)
            continue

        if type(md) is Table:
            content += md.make_content()
            continue

        if type(md) is ListLine:
            content += md.make_content()
            continue

        if type(md) is HeaderLine:
            anchor = ids.add_id(md.text)
            page_nav.add_page_nav(md.level, md.text, anchor)
            content += md.make_content(anchor)
            continue

        if type(md) is Paragraph:
            content += md.make_content()
            # continue

    ret['PAGE_TREE'] = page_nav.to_html(True)
    ret['CONTENT'] = content

    cr = []
    n = site_nav_node
    if n.anchor != 'README.md':
        cr.append(n)
    while n.parent != None:
        cr = [n.parent] + cr
        n = n.parent

    cr[0] = web.nav_tree.NavNode(None, 1, 'Home', '')
    crumbs = ''
    for n in cr:
        if n == cr[-1]:
            crumbs += '<li class="active"><span>' + n.text + '</span></li>'
        else:
            crumbs += '<li><a href="/' + n.get_full_path() + '">' + n.text + '</a></li>'

    ret['BREAD_CRUMBS'] = crumbs

    # Find the root
    root = site_nav_node
    while root.parent:
        root = root.parent

    # Make a copy. We are about to have our way with it.
    cpy = copy.deepcopy(root)

    # Collapse everything
    web.nav_tree.collapse_all(cpy)

    pics = site_nav_node.get_full_path().split('/')
    node = cpy
    for p in pics:
        node = node.find_child_named(p)
        node.expanded = True
        node.active_item_path = True
    if pics[-1] == 'README.md':
        node.parent.active_item = True
    else:
        node.active_item = True

    ret['SITE_TREE'] = web.nav_tree.to_html(cpy)

    # Some basic error checking
    if ret['IMAGE'] == '' or ret['TITLE'] == '':
        raise Exception('IMAGE and TITLE are required')

    return ret


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
        if dep.startswith('+'):
            # This is just a blind copy -- no processing
            dep = dep[1:].strip()
            src = os.path.join(fp_content, dep)
            dst = os.path.join(fp_deploy, dep)
            if os.path.isdir(src):
                shutil.copytree(src, dst)
            else:
                shutil.copy(src, dst)

    def substitute(lines, tag, value):
        tag = '<!-- %%' + tag + '%% -->'
        for i in range(len(lines)):
            if tag in lines[i]:
                lines[i] = lines[i].replace(tag, value)

    for dep in current_node.children:
        src = os.path.join(fp_content, dep.anchor)
        dst = os.path.join(fp_deploy, dep.anchor)
        if os.path.isdir(src):
            os.makedirs(dst)
            deploy_directory(dep)
        else:
            if src.endswith('-'):
                pass
            elif not src.endswith('.md'):
                shutil.copy(src, dst)
            else:
                md, _ = code.markdown_utils.load_file(src)
                cont = process_markdown(md, dep, fp_content)
                f = open(os.path.join(ENV.CONTENT_DIR, 'master.template'), 'r')
                lines = f.readlines()
                f.close()
                substitute(lines, 'TITLE', cont['TITLE'])
                substitute(lines, 'IMAGE', cont['IMAGE'])
                substitute(lines, 'BREAD_CRUMBS', cont['BREAD_CRUMBS'])
                substitute(lines, 'SITE_TREE', cont['SITE_TREE'])
                substitute(lines, 'PAGE_TREE', cont['PAGE_TREE'])
                substitute(lines, 'CONTENT', cont['CONTENT'])
                if dep.anchor == 'README.md':
                    dep.anchor = 'index.html'
                else:
                    dep.anchor = dep.anchor[0:-2] + 'html'
                f = open(os.path.join(ENV.DEPLOY_DIR,
                                      dep.get_full_path()), 'w+')
                f.writelines(lines)
                f.close()


def load_site_directory():
    ''' Recursively load all the deployment information
        Returns:
            the NavTree of information
    '''

    def _load_site_directory_rec(level, tree, current_node):
        src = os.path.join(ENV.CONTENT_DIR, current_node.get_full_path())
        lines, _ = code.markdown_utils.load_file(
            os.path.join(src, 'README.md'))
        info = code.markdown_utils.get_deploy(lines)

        for directory, title in info:
            if directory.startswith('+'):
                # These do not contribute to navigation
                current_node.invisibles.append(directory)
            elif os.path.isdir(os.path.join(src, directory)):
                # This is a directory. Make an entry and recurse into it
                n = tree.add_page_nav(level, title, directory)
                _load_site_directory_rec(level + 1, tree, n)
            else:
                # This is a file
                tree.add_page_nav(level, title, directory)

    tree = NavTree()
    level = 1
    current_node = tree.root
    _load_site_directory_rec(level, tree, current_node)
    return tree


if __name__ == '__main__':

    # Remove and recreate the deployment directory (clean)
    if os.path.isdir(ENV.DEPLOY_DIR):
        shutil.rmtree(ENV.DEPLOY_DIR)
    os.makedirs(ENV.DEPLOY_DIR)

    # Load the site information
    site_nav = load_site_directory()

    # Process all deployment beginning at the root
    deploy_directory(site_nav.root)
