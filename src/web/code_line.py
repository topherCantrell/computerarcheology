

class CodeLine:

    # ([])      labels
    # (int)     address
    # ([])      bytes
    # (string)  opcode
    # (int)     printedOpcodeLen
    # (string)  comment
    # (string)  original

    def __init__(self):
        self.labels = []
        self.bytes = []
        self.comment = None
        self.opcode = None
        self.address = None
        self.target = None
        self.numbers = None

    def isFourDigitHex(self, s):
        if len(s) != 4:
            return False
        try:
            int(s, 16)
            return True
        except:
            return False

    def isTwoDigitHex(self, s):
        if len(s) != 2:
            return False
        try:
            int(s, 16)
            return True
        except:
            return False

    def decodeTargetLink(self, s):
        ret = {}
        s = s.strip()
        if s.startswith(">>"):
            ret["placement"] = 'comment'
            s = s[2:].strip()
        elif s.startswith(">"):
            ret["placement"] = 'side'
            s = s[2:].strip()
        else:
            ret["placement"] = 'inline'

        if s.startswith("--"):
            ret["map"] = "hardware"
            s = s[2:].strip()
        elif s.startswith("-"):
            ret["map"] = "ram"
            s = s[1:].strip()
        else:
            ret["map"] = ""

        if ":" in s:
            i = s.index(":")
            ret["target"] = s[0:i].strip()
            ret["text"] = s[i + 1:].strip()
        else:
            ret["target"] = s
            ret["text"] = s

        return ret

    def getNumbersFromOpcode(self):
        ret = []
        pos = 0
        while True:
            if "$" not in self.opcode[pos:]:
                break
            numEntry = {}
            pos = self.opcode.index("$", pos)
            numEntry["startPos"] = pos
            i = pos + 1
            while i < len(self.opcode) and self.opcode[i] in '0123456789ABCDEF':
                i = i + 1
            numEntry["textLen"] = i - pos
            numEntry["value"] = int(self.opcode[pos + 1:i], 16)
            numEntry["text"] = self.opcode[pos:i]
            pos = i + 1
            ret.append(numEntry)
        return ret

    def parse(self, line):
        self.line = line
        s = line.text
        self.original = s
        s = s.strip()
        if ';' in s:
            self.originalCommentPos = self.original.index(";")
            i = s.index(';')
            self.comment = s[i + 1:]
            s = s[0:i].strip()

        first = s
        if ' ' in first:
            first = s[0:s.index(' ')]

        if first.endswith(":"):
            first = first[0:-1]
            if self.isFourDigitHex(first):
                self.address = int(first, 16)
            else:
                self.labels.append(first)

        i = len(first) + 1
        s = s[i:].strip()

        while(True):
            if len(s) < 2:
                break
            if len(s) > 2 and s[2] != ' ':
                break
            if (s[0] in '0123456789ABCDEF') and (s[1] in '0123456789ABCDEF'):
                self.bytes.append(int(s[0:2], 16))
                s = s[2:].strip()
            else:
                break

        if len(s) > 0:
            self.opcode = s
            self.printedOpcodeLen = len(self.opcode)
            self.originalOpcodePos = self.original.index(s)

        if self.comment and "{" in self.comment:
            i = self.comment.index("{")
            j = self.comment.index("}")
            self.target = self.decodeTargetLink(self.comment[i + 1:j])
            self.numbers = self.getNumbersFromOpcode()
            h = self.comment[0:i] + self.comment[j + 1:]
            self.comment = h
