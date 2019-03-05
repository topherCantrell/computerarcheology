

class Block:
    ''' A block of lines in a markdown file. Blocks are
    defined with open and closing ```type. Where type
    is optional.
    '''

    def __init__(self, first):
        ''' Start a block.
        Params:
            first (MarkdownLine): the first line in the block
        '''
        self._lines = []
        self._type = first.text.strip()[3:].strip()

    def get_type(self):
        return self._type

    def add_line(self, line):
        self._lines.append(line)

    def get_lines(self):
        return self._lines

    def make_content(self, code_info, lines):

        if self.get_type() == 'html':
            return self._make_content_html()

        if self.get_type() == 'code':
            return self._make_content_code(code_info, lines)

        if self.get_type() == 'plain':
            return self._make_content_plain()

        if self.get_type() == '':
            return self._make_content_none()

        raise Exception('Unknown block type ' + self.get_type())

    def _make_content_plain(self):
        ret = '<pre class="block_plainCode">\n'
        for md in self._lines[1:-1]:
            ret += md.text + '\n'
        ret += '</pre>'
        return ret

    def _make_content_html(self):
        ret = ''
        for md in self._lines[1:-1]:
            ret += md.text + '\n'
        return ret

    def _make_content_none(self):
        ret = '<pre>\n'
        for md in self._lines[1:-1]:
            ret += md.text + '\n'
        ret += '</pre>'
        return ret

    def _make_content_code(self, code_info, lines):
        import code.process_code
        if not 'processed_code' in code_info:
            code.process_code.process_code(lines, code_info)

        ret = '<pre class="codePreStyle">'

        for line in self._lines[1:-1]:

            html_out = line.text

            if line.link_info:

                # This is the target of a link. Give it an ID for navigation.
                # TODO think about moving this target up to the label before or even the section
                # header above where appropriate?
                if 'is_target' in line.link_info and line.link_info['is_target']:
                    html_out = '<span id="' + \
                        html_out[0:4] + '">' + html_out[0:4] + \
                        '</span>' + html_out[4:]

            ret = ret + html_out + '\n'

        ret = ret + '</pre>'

        # TODO references to RAM
        # TODO links in jumps
        # print(code_info['memory'])

        return ret
