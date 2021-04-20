import os

from carender import markdown
import carender.ENVIRONMENT as ENV
from carender.nav_tree import NavTree
from memory_map import MemoryMap


def load_site_directory(dev_mode=False):
    ''' Recursively load all the deployment information
        Returns:
            the NavTree of information
    '''

    def _load_site_directory_rec(level, tree, current_node, dev_mode):
        src = os.path.join(ENV.CONTENT_DIR, current_node.get_full_path())
        paras = markdown.read_markdown_paragraphs(os.path.join(src, 'README.md'))
        
        # We add the README here so it gets processed. The empty title keeps it
        # from appearing on the web page. 
        # TODO it shouldn't even be on the web page.
        deploy = ['README.md:'] + read_deployment_descriptor(paras)

        for entry in deploy:
            
            special = None
            if entry[0] in '#+':
                special = entry[0]
                entry = entry[1:]
            i = entry.find(':')
            if i >= 0:
                title = entry[i + 1:]
                directory = entry[:i]
            else:
                title = entry
                directory = entry
                if title.endswith('.md'):
                    title = title[0:-3]

            if dev_mode and special == '#':
                # In dev mode, we are building a specific set of things and ignoring others
                # In full mode, we build everything even if it is tagged to ignore
                continue

            if special == '+':
                # These do not contribute to navigation
                current_node.invisibles.append(directory)
            elif os.path.isdir(os.path.join(src, directory)):
                # This is a directory. Make an entry and recurse into it
                n = tree.add_page_nav(level, title, directory, None)
                _load_site_directory_rec(level + 1, tree, n, dev_mode)
            else:
                # This is a file
                # if directory.endswith('.md'):
                #    paras = markdown.read_markdown_paragraphs(os.path.join(src, directory))
                tree.add_page_nav(level, title, directory, None)

    tree = NavTree()
    level = 1
    current_node = tree.root
    _load_site_directory_rec(level, tree, current_node, dev_mode)
    return tree


def read_origin_gaps(markdown):
    ret = []
    for para in markdown:
        if para[0] == 'META' and para[1].startswith('>>> originGap '):
            ret.append(int(para[1][13:].strip(), 16))
    return ret


def read_deployment_descriptor(markdown):

    ret = []

    for para in markdown:
        if para[0] == 'META' and 'deploy:' in para[1]:
            for line in para[2:]:
                line = line[3:].replace('<br>', '')
                line = line.strip()
                ret.append(line)

    return ret


def read_binary_file_name(markdown):
    for para in markdown:
        if para[0] == 'META' and para[1].startswith('>>> binary '):
            ret = para[1][11:]
            ret = ret.replace(' ', '').strip()
            return ret
    return None


def read_code_text_lines(markdown):

    ret = []

    for para in markdown:
        if para[0] == 'BLOCK' and para[1].startswith('```code'):
            ret += para[2:-1]

    return ret


def read_memory_tables(md, directory):
    
    ret = {}
    
    for i in range(len(md)):
        para = md[i]
        if not para[0] == 'META':
            continue
        if not para[1].startswith('>>> memoryTable'):
            continue
        
        if not md[i + 1][0] == 'TEXT':
            raise Exception('Link must follow "memoryTable"')
        
        lnk = md[i + 1][1]
        j = lnk.find('](')
        if j < 0 or lnk[-1] != ')':
            raise Exception('Link must follow "memoryTable":' + lnk)
        
        fname = lnk[j + 2:-1].strip()
        name = para[1][16:].strip()
        
        mdmap = markdown.read_markdown_paragraphs(os.path.join(directory, fname))
        
        tab = MemoryMap(mdmap)
        
        ret[name] = [fname, tab]

    return ret


def read_cpu(md):
    for para in md:
        if para[0] == 'META' and len(para) > 1 and para[1].startswith('>>> cpu '):
            return para[1][8:].strip()
    return None
