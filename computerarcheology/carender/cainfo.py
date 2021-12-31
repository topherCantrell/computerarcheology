import os

from computerarcheology.carender import markdown
import computerarcheology.carender.ENVIRONMENT as ENV
from computerarcheology.carender.nav_tree import NavTree
from computerarcheology.carender.memory_map import MemoryMap


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
        # TODO it shouldn't even be on the rendered web page.
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


def _get_first_of_type(para, group_type, skip=0):
    '''Helper function for checking the first line of a specific group'''
    if para.group_type == group_type:
        return para.lines[0].text[skip:].strip()
    return None


def read_origin_gaps(md):
    ret = []
    for para in md:
        meta = _get_first_of_type(para, 'META', skip=4)
        if meta and meta.startswith('originGap '):
            ret.append(int(meta[10:].strip(), 16))
    return ret


def read_deployment_descriptor(md):

    ret = []

    for para in md:
        meta = _get_first_of_type(para, 'META', skip=4)
        if meta and meta.startswith('deploy:'):
            for line in para.lines[1:]:
                txt = line.text[3:].replace('<br>', '')
                txt = txt.strip()
                ret.append(txt)
            break

    return ret


def read_binary_file_name(md):
    for para in md:
        meta = _get_first_of_type(para, 'META', skip=4)
        if meta and meta.startswith('binary '):
            ret = meta[7:]
            ret = ret.replace(' ', '').strip()
            return ret
    return None


def read_code_text_lines(md):

    ret = []

    for para in md:
        bt = _get_first_of_type(para, 'BLOCK')
        if bt and bt.startswith('```code'):
            ret += para.lines[1:-1]

    return ret


def read_memory_tables(md, directory):

    ret = {}

    for i in range(len(md)):

        para = md[i]
        meta = _get_first_of_type(para, 'META', skip=4)
        if not meta or not meta.startswith('memoryTable '):
            continue

        if not md[i + 1].group_type == 'TEXT':
            ex = para.lines[0]
            raise Exception(f'Link must follow "memoryTable": {ex.file_name} at {ex.line_number}')            

        lnk = md[i + 1].lines[0].text
        j = lnk.find('](')
        if j < 0 or lnk[-1] != ')':
            ex = md[i + 1].lines[0]
            raise Exception(f'Invalid "memoryTable" link: {ex.file_name} at {ex.line_number}')

        fname = lnk[j + 2:-1].strip()
        name = meta[12:].strip()

        mdmap = markdown.read_markdown_paragraphs(os.path.join(directory, fname))

        tab = MemoryMap(mdmap)

        ret[name] = [fname, tab]

    return ret


def read_cpu(md):
    for para in md:
        if para.group_type == 'META' and len(para.lines[0].text) > 1 and para.lines[0].text.startswith('>>> cpu '):
            return para.lines[0].text[8:].strip()
    return None
