

class MarkdownLine:
    ''' The basic information from a line in a markdown file.

    Params:
      text (str): the text of the line (with no line feed)
      filename (str): the filename this line comes from
      linenumber (int): the linenumber of this line
    '''

    def __init__(self, text, filename, linenumber):
        self.text = text
        self.filename = filename
        self.linenumber = linenumber
        self.code = None  # In case this line is really code

    def make_content(self):
        raise Exception('I should be part of something else')
