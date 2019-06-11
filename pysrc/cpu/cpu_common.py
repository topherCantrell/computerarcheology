
class CPU:

    def __init__(self, opcodes):
        self._opcodes = opcodes
        self._make_data_map()
        self._make_frags()

    def _is_needed(self, text, pos):
        if text[pos] != ' ':
            return True
        if (text[pos - 1].isalpha() or text[pos - 1].isdigit()) and (text[pos + 1].isalpha() or text[pos + 1].isdigit()):
            return True
        return False

    def _remove_unneeded_whitespace(self, text):
        match = text
        while True:
            g = match.replace('  ', ' ')
            if g == match:
                break
            match = g
        nmatch = ''
        for i in range(len(match)):
            c = match[i]
            if self._is_needed(match, i):
                nmatch = nmatch + c
        return nmatch

    def _make_data_map(self):
        self._data_map = {}
        for op in self._opcodes:
            g = op['code'][:2]
            if g in self._data_map:
                self._data_map[g].append(op)
            else:
                self._data_map[g] = [op]

    def _make_frags(self):
        for op in self._opcodes:
            txt = op['mnem']
            txt = self._remove_unneeded_whitespace(txt)
            op['frags'] = ['']
            for i in range(len(txt)):
                c = txt[i]
                if c.islower():
                    op['frags'].append(c)
                    if i < (len(txt) - 1):
                        op['frags'].append('')
                else:
                    op['frags'][-1] = op['frags'][-1] + c

    def _does_op_fit(self, g, t):
        if len(g) != len(t):
            return False
        for i in range(len(g)):
            if t[i].islower():
                continue
            if g[i] != t[i]:
                return False
        return True

    def pick_opcode_from_aliases(self, mnem, opcodes):
        for op in opcodes:
            if op['mnem'].startswith(mnem[0]):
                return op
        return None

    def is_bus_x(self, op):
        return 'x' in op['bus']

    def is_bus_r(self, op):
        return 'r' in op['bus']

    def is_bus_w(self, op):
        return 'w' in op['bus']

    def is_bus_rw(self, op):
        return self.is_bus_r(op) and self.is_bus_w(op)

    def is_memory_reference(self, op):
        s = op['code']
        if 'p' in s or 's' in s or 't' in s or 'r' in s:
            return True
        return False

    def get_opcode_from_data(self, data):
        ret = []
        g = ''
        for d in data:
            g = g + '{:02X}'.format(d)
        if not g[:2] in self._data_map:
            return []
        for op in self._data_map[g[:2]]:
            if self._does_op_fit(g, op['code']):
                ret.append(op)
        return ret

    def process_fill_term(self, address, op, fill, decode):
        if not decode:
            return []
        if decode[0] == 'r':
            # Typical relative offset. Override this method if your CPU does
            # something different
            address = address + int(len(op) / 2)
            fill = fill - address
            if fill > 127 or fill < -128:
                raise Exception('Relative jump out of byte range')
            if fill < 0:
                fill = fill + 256

        ret = []
        if len(decode) == 2:
            if fill > 255:
                print(address)
                raise Exception('Bigger than a byte: {:04X}'.format(fill))
            ret.append(fill)
        else:
            if decode[1] == 'm':
                ret.append(fill >> 8)
                ret.append(fill & 0xFF)
            else:
                ret.append(fill & 0xFF)
                ret.append(fill >> 8)

        return ret

    # TODO going to need defines and labels to do this
    def fill_in_opcode(self, asm, address, op, pass_number):
        opcode = op[0]
        fill = op[1]
        if pass_number == 0:
            return [0] * int(len(opcode['code']) / 2)
        else:

            ret = []
            code = op[0]['code']
            fill = op[1]
            dec = ''
            for i in range(0, len(code), 2):
                if code[i].islower():
                    dec = dec + code[i:i + 2]
            if dec:
                fill = asm.parse_numeric(fill)

            fill = self.process_fill_term(address, code, fill, dec)
            p = 0

            for i in range(0, len(code), 2):
                if code[i].islower():
                    ret.append(fill[p])
                    p += 1
                else:
                    ret.append(int(code[i:i + 2], 16))

            return ret

    def find_opcode(self, text, assembler):
        if '>' in text:
            size_override = 2
            text = text.replace('>', '')
        elif '<' in text:
            size_override = 1
            text = text.replace('<', '')
        else:
            size_override = 0

        nmatch = self._remove_unneeded_whitespace(text)
        ret = []
        for op in self._opcodes:
            frags = op['frags']
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
            x = len(r[0]['frags'])
            if x < num_small:
                num_small = x
            if x > num_large:
                num_large = x

        # if num_small is 1, it means we have an exact match -- use that
        # otherwise use the match with the largest fragments
        if num_small == 1:
            num_large = num_small

        for x in range(len(ret) - 1, -1, -1):
            if len(ret[x][0]['frags']) != num_large:
                del ret[x]

        if len(ret) == 1:
            return ret[0]

        if len(ret) == 2 and ret[0][0]['frags'][0] == ret[1][0]['frags'][0]:
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
                if len(ret[0][0]['code']) < len(ret[1][0]['code']):
                    return ret[0]
                else:
                    return ret[1]
            elif size_override == 2:
                if len(ret[0][0]['code']) > len(ret[1][0]['code']):
                    return ret[0]
                else:
                    return ret[1]

        return []
