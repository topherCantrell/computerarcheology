
class Directive:
    ''' A single directive line (begins with >>>).'''

    def __init__(self, md):
        ''' Params:
              md (MarkdownLine): the markdown line
        '''
        self.original = md
        self.directive = md.text.strip()[3:].strip()

    def make_content(self):
        # No content for directives ... they are info
        return ''
