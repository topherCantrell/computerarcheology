import code.markdown_utils
import code.paragraph_line


class Table:

    def __init__(self):
        ''' A table in the markdown '''
        self._lines = []
        self.is_memory = False

    def get_lines(self):
        return self._lines

    def push_line(self, line):
        self._lines.insert(0, line)

    def make_content(self):
        # TODO embellish as needed

        classes = 'table table-condensed'
        if self.is_memory:
            classes += ' memoryMapTable'
        ret = '<table class="' + classes + '">\n'
        ret += '<thead>\n'

        cols = self._lines[0].text.split('|')[1:-1]
        ret += '<tr>'
        for c in cols:
            ret += '<th>' + code.markdown_utils.process_markdown(c) + '</th>'
        ret += '</tr>\n'
        ret += '</thead>\n'

        ret += '<tbody>\n'
        for bod in self._lines[2:]:
            cols = bod.text.split('|')[1:-1]

            if self.is_memory:
                ret += '<tr id="' + cols[1].strip() + '">'
            else:
                ret += '<tr>'

            ret += '<tr>'
            for c in cols:
                ret += '<td>' + \
                    code.markdown_utils.process_markdown(c) + '</td>'
            ret += '</tr>\n'
        ret += '</tbody>\n'

        ret += '</table>\n'
        return ret
