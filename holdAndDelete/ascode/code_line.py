
# Kinds of code lines:
# - Label : Single word before a comment ending in ':'
# - Data (no mnemonics) : Line begins with XXXX: and is all XX XX XX ...
# - Code (mnemonics) : Line begins with XXXX: and has XX XX XX and non XX parts
# - Other (comments, blanks) : Everything else


class CodeLine:
    # Info about the text: original, line_number, filename
    # text
    # comment
    # label
    # data
    # mnemonicText
    # mnemonic
    # address

    def __init__(self, md, filename=None, line_number=None):
        self.original = md
        self.filename = filename
        self.line_number = line_number
        self.data = None
        self.mnemonic = None
        self.opcode = None
        self.link_info = None

        line = md.text.strip()
        self.text = line

        self.address = None
        self.comment = None
        self._original_comment_start = None

        if ';' in line:
            i = line.index(';')
            self.comment = line[i + 1:].strip()
            line = line[0:i].strip()
            self._original_comment_start = i

        self.label = None
        if not ' ' in line and line.endswith(':'):
            self.type = 'Label'
            self.label = line[0:-1]
            return

        if not line:
            # Blank lines are OK
            return

        if line[4] == ':':
            self.address = int(line[0:4], 16)
            # TODO this is either Data or Code
            line = line[5:].strip()

            self.data = []
            while True:
                if len(line) == 2 or (len(line) > 2 and line[2] == ' '):
                    try:
                        self.data.append(int(line[0:2], 16))
                        line = line[2:].strip()
                        if len(line) == 0:
                            break
                    except:
                        # This is not a number ... done with data
                        break
                else:
                    break

            if len(line) == 0:
                self.type = 'Data'
            else:
                self.type = 'Code'
                self.mnemonicText = line
                if ' ' in line:
                    i = line.index(' ')
                    self.mnemonic = [line[0:i], line[i + 1:].strip()]
                else:
                    self.mnemonic = [line]
            return

        raise Exception('Not disassembly {} {}:{}'.format(
            filename, line_number, line))

    def replace_comment(self, new_comment):
        self.comment = new_comment
        if self._original_comment_start != None:
            self.original.text = self.original.text[0:
                                                    self._original_comment_start] + '; ' + new_comment
        else:
            self.original.text = self.original.text + ' ; ' + new_comment

    def is_address_in(self, addr):
        if(self.address == None or self.data == None or self.data == []):
            return False
        o = addr - self.address
        if o >= 0 and o < len(self.data):
            return True
        return False
