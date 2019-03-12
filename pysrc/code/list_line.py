import code.markdown_utils


class ListLine:
    ''' A list in the markdown '''

    def __init__(self):
        self._lines = []

    def push_line(self, line):
        self._lines.insert(0, line)

    def get_lines(self):
        return self._lines

    def make_content(self):
        # TODO embellish as needed!
        indent = self._lines[0].text.index('*')
        for md in self._lines:
            i = md.text.index('*')
            if i != indent:
                raise Exception('TODO Nested lists not implemented')

        ret = '<ul>\n'
        for md in self._lines:
            line_strip = md.text.strip()
            line_strip = line_strip[1:].strip()
            ret += '<li>' + \
                code.markdown_utils.process_markdown(line_strip) + '</li>\n'
        ret += '</ul>\n'
        return ret
