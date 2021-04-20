import cainfo
from html_id_mgr import IDMgr
from memory_map import MemoryMap
import names_in_code
from nav_tree import NavTree

special_block_type = None
memory_table = False
id_mgr = None
page_nav = None


def substitute(template, info):
    for key, value in info.items():
        template = template.replace('<!-- %%' + key + '%% -->', value)
    return template


def entize(txt):
    if txt.endswith('<br>'):
        return entize(txt[:-4]) + '<br>'
    txt = txt.replace('>', '&gt;')
    txt = txt.replace('<', '&lt;')
    return txt


def bold(txt):
    while '**' in txt:
        i = txt.find('**')
        j = txt.find('**', i + 2)
        if j < 0:
            raise Exception('No closing BOLD in ' + txt)
        txt = txt[0:i] + '<strong>' + txt[i + 2:j] + '</strong>' + txt[j + 2:]
    return txt


def web_links(txt):
    while '](' in txt:
        j = txt.find('](')
        k = txt.find(')', j)
        if k < 0:
            raise Exception('Invalid link in ' + txt)    
        i = j
        while txt[i] != '[':
            i -= 1
            if i < 0:
                raise Exception('Invalid link in ' + txt)
        image = False
        title = txt[i + 1:j]
        url = txt[j + 2:k]
        if not url.startswith('http') and url.endswith('.md'):
            url = url[0:-3] + '.html'
        if i > 0 and txt[i - 1] == '!':
            image = True
            i = i - 1
        if image:
            rep = f'<img src="{url}">'
        else:
            rep = f'<a href="{url}">{title}</a>'
        txt = txt[:i] + rep + txt[k + 1:]
    return txt


def _all_mods(p):
    p = entize(p)
    p = web_links(p)
    p = bold(p)
    return p

# Paragraph rendering


def _render_text(para):
    ret = '<p>'
    for p in para[0:]:
        p = _all_mods(p)
        ret = ret + p + '\n'
    ret += '</p>\n'
    return ret


def _render_header(para):
    cnt = 0
    title = para[0]
    while title[cnt] == '#':
        cnt += 1
    txt = title[cnt:].strip()
    
    i = txt.find('`')
    display_class = ''
    if i >= 0:
        j = txt.find('`', i + 1)
        if j != len(txt) - 1:
            raise Exception('Invalid display class: ' + para[0])
        display_class = txt[i + 1:j]
        txt = txt[:i].strip()
    
    anchor = id_mgr.add_id(txt)
    page_nav.add_page_nav(cnt, txt, anchor, display_class)    
    txt = _all_mods(txt)
    return f'<h{cnt} id="{anchor}">{txt}</h{cnt}>\n'


def _render_meta(para):
    
    global special_block_type, memory_table
    
    metafirst = para[0]
    if len(metafirst) > 3:
        metafirst = metafirst[3:].strip()
    
    if metafirst == 'playMe {':
        if special_block_type:
            raise Exception('Nested special block type not allowed ' + special_block_type)
        special_block_type = 'PLAYME'
        return '<div class="playMe">\n'
    elif metafirst == 'tourGuide {':
        if special_block_type:
            raise Exception('Nested special block type not allowed')
        special_block_type = 'TOURGUIDE'
        return '<div class="tourGuide">\n'
    elif metafirst == '}':
        if special_block_type:
            special_block_type = None
            return '</div>\n'
    elif metafirst == 'memory':
        memory_table = True
        
    return ''


def _render_list(para):
    # TODO multi-level lists (right now just one)
    ret = '<ul>\n'
    for p in para:
        p = _all_mods(p[1:])
        ret += '<li>' + p + '</li>\n' 
    return ret + '</ul>\n'


def _render_table(para):
    
    global memory_table
    
    extra_class = ''
    if memory_table:
        extra_class = ' memoryMapTable'        
    
    header_row = para[0].strip()
    if not header_row.endswith('|'):
        raise Exception('Table row must end with |')
    columns = header_row.split('|')[1:-1]
    if '--' not in para[1]:
        raise Exception('Table must have separator row ' + para[1])
    
    data_rows = []
    for d in para[1:]:
        if not d.endswith('|'):
            raise Exception('Table row must end with |')
        dr = d.split('|')[1:-1]
        if len(dr) != len(columns):
            raise Exception('Data row is missing columns ' + str(dr))
        data_rows.append(dr)    
        
    ret = f'<table class="table table-condensed{extra_class}"><thead>\n<tr>'
    for c in columns:
        ret += f'<th>{c.strip()}</th> '
    ret += '\n</tr></thead><tbody>\n'
    for dr in data_rows[1:]:
        if memory_table:
            ret += f'<tr id="{dr[1].strip()}">'
        else:
            ret += '<tr>'
        for d in dr:
            d = _all_mods(d.strip())
            ret += f'<td>{d}</td> '
        ret += '</tr>\n'
    ret += '</tbody></table>\n'
    
    memory_table = False    
    
    return ret


def _render_block(para):    

    block_type = para[0][3:].strip()

    if block_type == 'html':
        ret = ''
        for p in para[1:-1]:
            ret = ret + p + '\n'
        return ret

    elif block_type == 'code':
        # TODO use the beautified code
        ret = '<pre>'
        for p in para[1:-1]:
            # TODO these are done in the beautification step to count spaces
            p = entize(p)          
            p = web_links(p) 
            # TODO implement code render
            ret = ret + p + '\n'
        ret += '</pre>\n'
        return ret

    elif block_type == '' or block_type == 'plain' or block_type == 'plainCode':
        ret = '<pre>'
        for p in para[1:-1]:  
            p = entize(p)          
            p = web_links(p)            
            ret = ret + p + '\n'
        ret += '</pre>\n'
        return ret
    else:
        raise Exception('Unknown block type: ' + block_type)


def render_content(markdown):
    
    global special_block_type, id_mgr, page_nav
    
    memory_table = False
    id_mgr = IDMgr()
    # Used to build the page's navigation tab
    page_nav = NavTree()
    
    # Verify any memory map tables are correct
    MemoryMap(markdown)    
    
    code_lines = cainfo.read_code_text_lines(markdown)
            
    # We DO process entities in everything (except HTML blocks)
    # We do NOT process markdown (except for web links) in any BLOCK
    
    ret = ''

    for para in markdown:
        para_type = para[0]
        if para_type == 'TEXT':
            ret += _render_text(para[1:])
        elif para_type == 'HEADER':
            ret += _render_header(para[1:])
        elif para_type == 'META':
            ret += _render_meta(para[1:])
        elif para_type == 'LIST':
            ret += _render_list(para[1:])
        elif para_type == 'BLOCK':
            ret += _render_block(para[1:])
        elif para_type == 'TABLE':
            ret += _render_table(para[1:])
        else:
            raise Exception('Unknown markdown paragraph type: ' + para_type)

    if special_block_type:
        raise Exception('Special block type left open: ' + special_block_type)
    
    return ret, page_nav.to_html(True)
