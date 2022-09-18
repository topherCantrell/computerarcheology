import computerarcheology.carender.cacode
import computerarcheology.carender.cainfo
from computerarcheology.carender.html_id_mgr import IDMgr
from computerarcheology.carender.memory_map import MemoryMap
from computerarcheology.carender.nav_tree import NavTree

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
        if not url.startswith('http'):
            url = url.replace('.md#', '.html#')
            if url.endswith('.md'):
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
    for p in para:
        txt = _all_mods(p.text)
        ret = ret + txt + '\n'
    ret += '</p>\n'
    return ret


def _render_header(para):
    cnt = 0
    title = para[0].text.strip()
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
    ansvg = f'<a class="caanchor" href="#{anchor}"><svg viewBox="0 0 16 16" version="1.1" width="16" height="20" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>'
    return f'<h{cnt} class="cahead" id="{anchor}">{txt}{ansvg}</h{cnt}>\n'


def _render_meta(para):

    global special_block_type, memory_table

    metafirst = para[0].text[3:].strip()

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
        p = _all_mods(p.text.strip()[1:])
        ret += '<li>' + p + '</li>\n'
    return ret + '</ul>\n'


def _render_table(para):

    global memory_table

    extra_class = ''
    if memory_table:
        extra_class = ' memoryMapTable'

    header_row = para[0].text.strip()
    if not header_row.endswith('|'):
        raise Exception('Table row must end with |')
    columns = header_row.split('|')[1:-1]
    if '--' not in para[1].text:
        raise Exception('Table must have separator row ' + para[1])

    data_rows = []
    for d in para[1:]:
        if not d.text.strip().endswith('|'):
            raise Exception('Table row must end with |')
        dr = d.text.strip().split('|')[1:-1]
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


def _find_naked_code_anchors(lines):
    ret = []
    for line in lines:
        txt = line.text
        if '; {}' in txt or '; {+}' in txt:
            i = txt.find('$')
            if i < 0:
                raise Exception('no constant')
            j = i + 1
            while txt[j] in '0123456789ABCDEF':
                j += 1
            ret.append(int(txt[i + 1:j], 16))

    return ret


def _render_code_line(line, code_anchors, tables):
    text = line.text

    comment_starts = text.find(';')
    if comment_starts < 0:
        comment_starts = len(text)
    first_part = text[:comment_starts].strip()
    vis_length = len(first_part)
    second_part = text[comment_starts:].strip()

    # The opcodes are easy to entize -- just single characters. Do this before
    # we start adding HTML.

    first_part = entize(first_part)

    # Insert anchors for jump targets. This includes naked addresses and labels.

    if ':' in first_part:
        if len(first_part) > 4 and first_part[4] == ':' and computerarcheology.carender.cacode.is_hex_4(first_part[0:4]):
            # This is a naked address
            addr = int(first_part[0:4], 16)
            if addr in code_anchors:
                first_part = f'<span id="{first_part[:4]}">{first_part[:4]}</span>{first_part[4:]}'
        else:
            i = first_part.find(':')
            first_part = f'<span id="{first_part[:i]}">{first_part[:i]}</span>{first_part[i:]}'

    if '$' in first_part and second_part.startswith('; {'):
        # We have a numeric substitution to make
        # Find the constant
        i = first_part.find('$')
        j = i + 1
        while j < len(first_part) and first_part[j] in '0123456789ABCDEF_':
            j += 1
        # Find the replacement in the comment
        k = second_part.find('}')
        rep = second_part[3:k]
        if rep.startswith('+'):
            rep = rep[1:]
        # Remove the tag from the comment
        second_part = '; ' + second_part[k + 1:].strip()
        if not rep:
            # This a naked (no-name) reference to a code address
            rep = first_part[i:j]
            rep_org = first_part[i + 1:j]
            rep_org = rep_org.rjust(4, '0')
            rep_html = f'<a class="addr_code" href="#{rep_org}">{rep}</a>'
            first_part = first_part[0:i] + rep_html + first_part[j:]
        else:
            if rep[1] != '-':
                x = rep.find('.')
                if x < 0:
                    raise Exception('No table name')
                table_name = rep[:x]
                rep_org = rep[x + 1:]
                rep = rep_org
                y = rep.find('+')
                if y >= 0:
                    rep = rep[0:y]

                if table_name == 'code':
                    html_name = ''
                    target = ''                    
                else:
                    html_name = tables[table_name][0]
                    target = f' target="{table_name}"'

                if html_name.endswith('.md'):
                    html_name = html_name[:-3] + '.html'
                rep_html = f'<a class="addr_{table_name}" href="{html_name}#{rep}"{target}>{rep_org}</a>'
                vis_length = vis_length - (j - i)  # Removing the constant
                vis_length = vis_length + len(rep_org)  # Adding the link text
                first_part = first_part[0:i] + rep_html + first_part[j:]

    # Now to process special comments in the second part.
    
    new_second = ''
    while second_part:
        i = second_part.find('`')
        if i >= 0:
            j = second_part.find('`', i + 1)
            if j < 0:
                raise Exception(f'Missing closing ` at {line.file_name} {line.line_number}')
            new_second = new_second + entize(second_part[:i]) + second_part[i + 1:j]
            new_second = web_links(new_second)
            second_part = second_part[j + 1:]
        else:
            new_second += entize(second_part)
            new_second = web_links(new_second)
            break

    # Combine the parts together for the final line

    spaces_needed = comment_starts - vis_length
    if spaces_needed > 0:
        first_part = first_part + ' ' * spaces_needed

    return first_part + new_second


def _render_block(para, code_anchors, tables):

    block_type = para[0].text[3:].strip()

    if block_type == 'html':
        ret = ''
        for p in para[1:-1]:
            ret = ret + p.text + '\n'
        return ret

    elif block_type == 'code':
        ret = '<pre class="codePreStyle">'
        for p in para[1:-1]:
            ret = ret + _render_code_line(p, code_anchors, tables) + '\n'
        ret += '</pre>\n'
        return ret

    elif block_type == 'plainCode' or block_type == 'plain':
        # TODO how about a reference to lines of real code
        ret = '<pre class="plainCodePreStyle">'
        for p in para[1:-1]:
            p = entize(p.text)
            p = web_links(p)
            ret = ret + p + '\n'
        ret += '</pre>\n'
        return ret

    elif block_type == '':
        ret = '<pre>'
        for p in para[1:-1]:
            p = entize(p.text)
            p = web_links(p)
            ret = ret + p + '\n'
        ret += '</pre>\n'
        return ret

    else:
        raise Exception('Unknown block type: ' + block_type)


def render_content(md, directory):

    global special_block_type, id_mgr, page_nav

    memory_table = False
    id_mgr = IDMgr()
    # Used to build the page's navigation tab
    page_nav = NavTree()

    # Verify any memory map tables are correct
    MemoryMap(md)

    code_lines = computerarcheology.carender.cainfo.read_code_text_lines(md)
    code_anchors = _find_naked_code_anchors(code_lines)

    tables = computerarcheology.carender.cainfo.read_memory_tables(md, directory)

    # We DO process entities in everything (except HTML blocks)
    # We do NOT process markdown (except for web links) in any BLOCK

    ret = ''

    for group in md:
        if group.group_type == 'TEXT':
            ret += _render_text(group.lines)
        elif group.group_type == 'HEADER':
            ret += _render_header(group.lines)
        elif group.group_type == 'META':
            ret += _render_meta(group.lines)
        elif group.group_type == 'LIST':
            ret += _render_list(group.lines)
        elif group.group_type == 'BLOCK':
            ret += _render_block(group.lines, code_anchors, tables)
        elif group.group_type == 'TABLE':
            ret += _render_table(group.lines)
        else:
            raise Exception('Unknown markdown paragraph type: ' + group.group_type)

    if special_block_type:
        raise Exception('Special block type left open: ' + special_block_type)

    return ret, page_nav.to_html(True)
