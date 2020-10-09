class AssemblyException(Exception):
    pass


class BaseAssembly:
    '''Baseclass of things a CPU needs to implement for assembly'''

    def init_assembly(self):
        '''Initialize the CPU to begin assembly

        This might be expensive. Don't do it until we know we need to.
        '''

        self.make_frags()

    def make_frags(self):
        '''Make opcode fragments for assembly

        The assembly processes needs the mnemonic broken up into fragments for matching.

        This method fills out the fragments for all opcodes. We assume that single lower-case
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

    def remove_unneeded_whitespace(self, text: str):
        '''Remove unneeded whitespace from a string

        ASSUMPTION: All opcodes are of the form
            LDA  (p,X)
        There are at most TWO terms separated by whitespace. All other whitespace
        can be removed.

        Args:
            text (str): the string

        Returns:
            str: the processed string
        '''

        i = text.find(' ')
        if i >= 0:
            ret = text[0:i + 1] + text[i + 1:].replace(' ', '')
        else:
            ret = text.replace(' ', '')

        return ret.strip()

    NON_SUB_CHARS = ',@#$~!?[]{}|'  # Add as needed

    def find_opcode_for_text(self, text: str, assembler):
        '''Find the one opcode that best matches this line of text

        In finding the correct opcode, we parse out all the substitution
        pieces. That information is returned too.

        Args:
            text (str): the line of code
            assembler (Assembler): contains any defines

        Returns:
            Opcode: the requested (opcode,info) (or None)
        '''

        # Ignorable whitespace
        nmatch = self.remove_unneeded_whitespace(text)

        possibles = []
        possibles_info = []
        shortest_frag = 10000
        for op in self._opcodes:
            remain = nmatch
            info = {}
            for fi in range(len(op.frags)):
                if not remain:
                    # We've reached the end of the test
                    # '' means match, None means no match
                    break
                # Next fragment of the opcode being tested
                frag = op.frags[fi]
                if not frag[0].islower():
                    if remain.startswith(frag):
                        # This is a static fragment ... just peel it off
                        remain = remain[len(frag):]
                    else:
                        # This is a static fragment that doesn't match
                        remain = None  # This opcode can't match
                else:
                    # This is a substitution
                    if fi == len(op.frags) - 1:
                        # This is the last fragment ... match the rest of the line
                        i = len(remain)
                    else:
                        # Find the next fragment
                        i = remain.find(op.frags[fi + 1])
                    if i >= 0:
                        term = remain[:i]
                        info[frag[0]] = term
                        remain = remain[i:]
                        for c in self.NON_SUB_CHARS:
                            # These characters can't be in substitution parameters
                            if c in term:
                                remain = None
                                break
                    else:
                        remain = None

            if remain is not None:
                # This opcode is a potential ... add it to the list
                possibles.append(op)
                possibles_info.append(info)
                if len(op.frags) < shortest_frag:
                    shortest_frag = len(op.frags)

        # Rule out all but the most exact matches
        for i in range(len(possibles) - 1, -1, -1):
            if len(possibles[i].frags) != shortest_frag:
                del possibles[i]
                del possibles_info[i]

        n = len(possibles)

        if n == 0:
            # Not found
            return None

        if n == 1:
            return (possibles[0], possibles_info[0])

        # Multiple found. Try and pick one.

        if n == 2 and possibles[0].frags[0] == possibles[1].frags[0]:
            # Special, common case where we can override the addressing mode
            # The mode might be forced with "<" or ">"
            # If not, we might have the address defined. If so, pick based on value.
            sz = 's2'
            if '_default_base_page' in assembler.defines and assembler.defines['_default_base_page'] == 'true':
                sz = 's1'
            if '>' in text:
                sz = 's2'
            elif '<' in text:
                sz = 's1'
            for i in range(len(possibles)):
                op = possibles[i]
                for u in op.use:
                    if sz in op.use[u]:
                        return (op, possibles_info[i])

        raise AssemblyException('Multiple Matches')

    def fill_in_opcode(self, _text, asm, _address, op, pass_number):
        '''
        '''

        opcode = op[0]
        info = op[1]
        if pass_number == 0:
            return [0] * len(opcode.code)
        else:
            for key in info:
                val = asm.parse_numeric(str(info[key]))
                info[key] = [info[key], val]
            ret = []
            for c in opcode.code:
                if isinstance(c, str):
                    numval = info[c[0]][1]
                    # TODO: PCR
                    if c[1] == '1':
                        ret.append((numval >> 8) & 0xFF)
                    else:
                        ret.append(numval & 0xFF)
                    # print('##',text,info,opcode.use)
                else:
                    ret.append(c)
            return ret
