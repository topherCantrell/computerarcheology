
class CPU:

    def __init__(self, opcodes):
        self._opcodes = opcodes
        self._make_frags()

    def _is_needed(self, text, pos):
        if text[pos] != ' ':
            return True
        if (text[pos - 1].isalpha() or text[pos - 1].isdigit()) and (text[pos + 1].isalpha() or text[pos + 1].isdigit()):
            return True
        return False

    def _remove_unneeded_whitespace(self, text):
        match = text.replace('  ', ' ')
        nmatch = ''
        for i in range(len(match)):
            c = match[i]
            if self._is_needed(match, i):
                nmatch = nmatch + c
        return nmatch

    def _make_frags(self):
        for op in self._opcodes:
            txt = op['mnem']
            op['frags'] = ['']
            for i in range(len(txt)):
                c = txt[i]
                if c.islower():
                    op['frags'].append(c)
                    if i < (len(txt) - 1):
                        op['frags'].append('')
                else:
                    op['frags'][-1] = op['frags'][-1] + c

    def find_opcode(self, text):
        nmatch = self._remove_unneeded_whitespace(text)

        ret = []  # 0 is the opcode
        for op in self._opcodes:
            frags = op['frags']
            found = None
            found_plug = None
            if len(frags) == 1:
                if frags[0] == nmatch.upper():
                    found = op
                    found_plug = None
            elif len(frags) == 2:
                if nmatch.upper().startswith(frags[0]) and len(nmatch) > len(frags[0]):
                    found = op
                    found_plug = nmatch[len(frags[0]):]
            elif len(frags) == 3:
                if nmatch.upper().startswith(frags[0]) and nmatch.upper().endswith(frags[2]):
                    found = op
                    found_plug = nmatch[len(frags[0]):-len(frags[2])]

            if found:
                if not ret:
                    ret.append(found)
                    ret.append(found_plug)
                    continue
                else:
                    if ret[0]['frags'] == found['frags']:
                        # The Z80 has duplicate mnemonic
                        continue
                    if len(found['frags']) > len(ret[0]['frags']):
                        ret[0] = found
                        ret[1] = found_plug

        return ret
