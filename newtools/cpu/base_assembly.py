class AssemblyException(Exception):
    pass

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
    
    NON_SUB_CHARS = '@#$~!?[]{}|' # Add as needed

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
        
        possibles = []
        shortest_frag = 10000
        for op in self._opcodes:
            remain = nmatch
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
                        remain = None # This opcode can't match
                else:
                    # This is a substitution
                    if fi==len(op.frags)-1:
                        # This is the last fragment ... match the rest of the line
                        i = len(remain)
                    else:                        
                        # Find the next fragment
                        i = remain.find(op.frags[fi+1])
                    if i>=0:
                        term = remain[:i]                        
                        remain = remain[i:]
                        for c in self.NON_SUB_CHARS:
                            # These characters can't be in substitution parameters
                            if c in term:
                                remain = None
                                break                                           
                    else:                
                        remain = None
            if remain != None:
                # This opcode is a potential ... add it to the list
                possibles.append(op)
                if len(op.frags)<shortest_frag:
                    shortest_frag = len(op.frags)
        
        # Rule out all but the most exact matches
        for i in range(len(possibles)-1,-1,-1):
            if len(possibles[i].frags)!=shortest_frag:
                del possibles[i]
                
        if not possibles:
            # Not found
            return None
        
        if len(possibles)>1:
            # Multiple found
            for pos in possibles:
                print(pos.frags)
            raise AssemblyException('Multiple Matches')
            # TODO: size override can narrow down the list maybe look for first frag matching maybe pick the smallest if not specified
        
        # Exactly one found
        return possibles[0]        
       