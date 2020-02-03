
class BaseAssembly:

    def init_assembly(self):
        self.make_frags()

    def make_frags(self):
        '''Make opcode fragments for assembly

        The assembly processes needs the mnemonic broken up into fragments for matching.

        This method fills out the fragments for all opcodes. We assume that single lowercase
        letters represent things needing filled in.
        '''

        for op in self._opcodes:
            txt = op.mnemonic
            txt = self.remove_unneeded_whitespace(txt)
            op.frags = ['']
            for i in range(len(txt)):
                c = txt[i]
                if c.islower():
                    op.frags.append(c)
                    if i < (len(txt) - 1):
                        # More to go -- start a new string for the more
                        op.frags.append('')
                else:
                    op.frags[-1] = op.frags[-1] + c

    def is_space_needed(self, text: str, pos: int):
        '''Return true if the target character in the string is needed.

        Args:
            text (str): the string
            pos (int): position in the string
        Returns:
            boolean: True if the character is needed or False if not


        Only whitespace can be not-needed. Spaces between letters and numbers is always needed.
        The rest can go.
        '''
        if text[pos] != ' ':
            # Just in case
            return True
        if (text[pos - 1].isalpha() or text[pos - 1].isdigit()) and (text[pos + 1].isalpha() or text[pos + 1].isdigit()):
            return True
        return False

    def remove_unneeded_whitespace(self, text: str):
        '''Remove unneeded whitespace from a string

        Args:
            text (str): the string

        Returns:
            str: the processed string
        '''
        match = text
        while True:
            g = match.replace('  ', ' ')
            if g == match:
                break
            match = g
        nmatch = ''
        for i in range(len(match)):
            c = match[i]
            if self.is_space_needed(match, i):
                nmatch = nmatch + c
        return nmatch

    def find_opcode_for_text(self, text: str, assembler):
        '''Find the one opcode that matches this line of text

        Args:
            text (str): the line of code
            assembler (Assembler): contains any defines

        Returns:
            Opcode: the requested opcode (or None)
        '''

        # Addressing mode overrides
        if '>' in text:
            size_override = 2
            text = text.replace('>', '')
        elif '<' in text:
            size_override = 1
            text = text.replace('<', '')
        else:
            size_override = 0

        # Ignorable whitespace
        nmatch = self.remove_unneeded_whitespace(text)
        
        ret = []
        for op in self._opcodes:
            frags = op.frags
            if len(frags) == 1:
                if frags[0] == nmatch.upper():
                    ret.append([op, None])
            elif len(frags) == 2:
                if nmatch.upper().startswith(frags[0]) and len(nmatch) > len(frags[0]):
                    ret.append([op, nmatch[len(frags[0]):]])
            elif len(frags) == 3:
                if nmatch.upper().startswith(frags[0]) and nmatch.upper().endswith(frags[2]):
                    ret.append([op, nmatch[len(frags[0]):-len(frags[2])]])

        if not ret:
            return []

        if len(ret) == 1:
            return ret[0]

        num_small = 1000
        num_large = 0
        for r in ret:
            x = len(r[0].frags)
            if x < num_small:
                num_small = x
            if x > num_large:
                num_large = x

        # if num_small is 1, it means we have an exact match -- use that
        # otherwise use the match with the largest fragments
        if num_small == 1:
            num_large = num_small

        for x in range(len(ret) - 1, -1, -1):
            if len(ret[x][0].frags) != num_large:
                del ret[x]

        if len(ret) == 1:
            return ret[0]

        if len(ret) == 2 and ret[0][0].frags[0] == ret[1][0].frags[0]:
            if size_override == 0:
                try:
                    val = assembler.parse_numeric(ret[0][1])
                except:
                    val = 256
                if val < 256:
                    size_override = 1
                else:
                    size_override = 2
            if size_override == 1:
                if len(ret[0][0].code) < len(ret[1][0].code):
                    return ret[0]
                else:
                    return ret[1]
            elif size_override == 2:
                if len(ret[0][0].code) > len(ret[1][0].code):
                    return ret[0]
                else:
                    return ret[1]

        return []
