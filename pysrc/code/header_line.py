class HeaderLine:
    ''' A header line -- starts with one or more # '''

    def __init__(self, md):
        ''' Params:
              md (MarkdwonLine): the markdown line
        '''

        self.original = md

        self.level = 0
        line_strip = md.text.strip()
        while line_strip[self.level] == '#':
            self.level += 1
            self.text = line_strip[self.level:].strip()

    def make_content(self, anchor):
        return '<h{level} id="{anchor}">{text}</h{level}>\n'.format(level=self.level, anchor=anchor, text=self.text)
