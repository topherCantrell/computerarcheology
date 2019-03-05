import code.markdown_utils


class Paragraph:
    ''' A list of plain markdown lines that make up a paragraph. 
    Blank lines flag the end of a paragraph.'''

    def __init__(self):
        self._lines = []

    def push_line(self, line):
        self._lines.insert(0, line)

    def get_lines(self):
        return self._lines

    def make_content(self):
        if len(self._lines) == 0:
            return ''
        ret = '<p>\n'
        for md in self._lines:
            ret += code.markdown_utils.process_markdown(md.text) + '\n'
        ret += '</p>\n'

        return ret
