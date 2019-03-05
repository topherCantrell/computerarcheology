
import code.block_line
import code.code_line
import code.directive_line
import code.list_line
import code.markdown_line
import code.paragraph_line
import code.table_line


def process_markdown(text):

    # Links and images
    while '](' in text:
        j = text.index('](')
        i = j
        while i > 0 and text[i] != '[':
            i -= 1
        k = text.index(')', j)
        m = i
        is_img = False
        if i > 0 and text[i - 1] == '!':
            m = i - 1
            is_img = True

        if is_img:
            rep = '<img src="' + text[j + 2:k] + '">'
        else:
            rep = '<a href="' + text[j + 2:k] + '">' + text[i + 1:j] + '</a>'

        text = text[0:m] + rep + text[k + 1:]

    # Bold
    while '**' in text:
        i = text.index('**')
        j = text.index('**', i + 1)
        text = text[0:i] + '<strong>' + \
            text[i + 2:j - 1] + '</strong>' + text[j + 2:]

    # TODO italic
    # TODO `stuff`

    return text


def get_deploy(lines):

    ret = [['README.md', '']]

    found = False

    for g in lines:
        if found:
            if type(g) is code.directive_line.Directive:
                g = g.directive
                if '<br>' in g:
                    g = g[0:g.index('<br>')].strip()
                if g == 'README.md':
                    continue

                if ':' in g:
                    i = g.index(':')
                    t = g[i + 1:].strip()
                    g = g[0:i].strip()
                    if g.endswith('/'):
                        g = g[0:-1]
                else:
                    if g.endswith('/'):
                        g = g[0:-1]
                    t = g
                    if t.endswith('.md'):
                        t = t[0:-3]

                ret.append([g, t])
            else:
                return ret
        else:
            if type(g) is code.directive_line.Directive:
                found = True

    return ret


def is_text_a_list_item(text):
    g = text.strip()
    # TODO numbered lists too
    if g.startswith('**'):
        # This is BOLD, not a list
        return False
    if g.startswith('- ') or g.startswith('* '):
        return True
    return False


def load_file(filename):
    '''
    Load all the lines from the markdown file. This function parses the markdown:
      - All the lines in a ``` block are collected into one BlockLine. If this
        is a code block, then the lines are CodeLines. Otherwise they are plain
        MarkdownLines.
      - All the lines in a | | | table are pulled together into a single table text.
        Tables with a leading "memory" directive are marked as such.
      - All the lines in a list are pulled together into a single list text.
      - Directives are parsed into DirectiveLines
      - Headers are parsed into HeaderLines
      - Everything else up to a blank text is parsed into a ParagraphLine. Empty
        paragraphs are removed (multiple blank lines collapse into one blank text)

    Params:
      filename (str): the path/name of the file to load

    Return:
      list: the loaded lines
    '''

    lines = []

    # Everything comes in as a generic text
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if line == '':  # end of the file
                break
            if line.endswith('\n'):  # Strip off the text feed
                line = line[0:-1]
            # Collect all the lines
            lines.append(code.markdown_line.MarkdownLine(
                line, filename, len(lines)))

    # Collect all the formal blocks together
    in_block = False
    lines_n = []
    block = None
    for md in lines:
        if in_block:
            if md.text.strip().startswith('```'):
                block.add_line(md)
                in_block = False
            else:
                # Parse the block types while we are here
                if block.get_type() == 'code':
                    block.add_line(code.code_line.CodeLine(md))
                else:
                    block.add_line(md)
        else:
            if md.text.strip().startswith('```'):
                in_block = True
                block = code.block_line.Block(md)
                block.add_line(md)
                lines_n.append(block)
            else:
                lines_n.append(md)
    lines = lines_n

    # Tables are blocks too ... all the lines that start with '|'
    i = len(lines)
    while i > 0:
        i -= 1
        md = lines[i]
        if type(md) is code.markdown_line.MarkdownLine and md.text.strip().startswith('|'):
            table = code.table_line.Table()
            while type(md) is code.markdown_line.MarkdownLine and md.text.strip().startswith('|'):
                table.push_line(md)
                del lines[i]
                i -= 1
                md = lines[i]
            lines.insert(i + 1, table)

    # Lists are blocks too ... all the lines start with a '-' or '*' or 'n. '
    i = len(lines)
    while i > 0:
        i -= 1
        md = lines[i]
        if type(md) is code.markdown_line.MarkdownLine and is_text_a_list_item(md.text):
            lst = code.list_line.ListLine()
            while type(md) is code.markdown_line.MarkdownLine and is_text_a_list_item(md.text):
                lst.push_line(md)
                del lines[i]
                i -= 1
                md = lines[i]
            lines.insert(i + 1, lst)

    # Parse directives
    i = len(lines)
    while i > 0:
        i -= 1
        md = lines[i]
        if type(md) is code.markdown_line.MarkdownLine:
            if md.text.strip().startswith('>>>'):
                lines[i] = code.directive_line.Directive(md)

    # Parse headers
    i = len(lines)
    while i > 0:
        i -= 1
        md = lines[i]
        if type(md) is code.markdown_line.MarkdownLine:
            if md.text.strip().startswith('#'):
                lines[i] = code.header_line.HeaderLine(md)

    # Everything else is a paragraph
    i = len(lines)
    while i > 0:
        i -= 1
        md = lines[i]
        if type(md) is code.markdown_line.MarkdownLine:
            text = code.paragraph_line.Paragraph()
            while type(md) is code.markdown_line.MarkdownLine and md.text.strip() != '':
                text.push_line(md)
                del lines[i]
                i -= 1
                if i < 0:
                    break
                md = lines[i]
            lines.insert(i + 1, text)

    # Remove empty paragraphs
    i = len(lines)
    while i > 0:
        i -= 1
        md = lines[i]
        if type(md) is code.paragraph_line.Paragraph:
            pc = 0
            for m in md.get_lines():
                if m.text.strip() != '':
                    pc += 1
            if pc == 0:
                del lines[i]

    # Mark memory tables as such
    for i in range(len(lines)):
        md = lines[i]
        if type(md) is code.directive_line.Directive and md.directive == 'memory':
            for m in lines[i + 1:]:
                if type(m) is code.table_line.Table:
                    m.is_memory = True
                    break

    return lines
