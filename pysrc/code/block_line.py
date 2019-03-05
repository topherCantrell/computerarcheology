

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
            #print(line, line.text)
            ret = ret + line.text + '\n'

        ret = ret + '</pre>'

        # TODO references to RAM
        # TODO links in jumps
        # print(code_info['memory'])

        return ret
