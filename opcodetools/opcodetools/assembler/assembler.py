import os

import opcodetools.cpu.cpu_manager


class ASMException(Exception):
    def __init__(self, message, line):
        super().__init__(message)
        self.line = line


class Assembler:

    def __init__(self, filename: str):
        '''Create a new Assembler object

        Args:
            filename (string) name of file to assemble
        '''

        self.lines = self.load_lines(filename)
        self.code = self.remove_comments_and_blanks(self.lines)
        self.defines = {}
        self.labels = {}
        self.cpu = None

    def load_lines(self, filename: str):
        '''Load the lines from the given file

        This method also recurses into include files.

        The information about a line looks like is:
        {
            'file_name': 'test.asm',
            'line_number' : 4
            'text' : '   MOV A,#$50'
        }

        Args:
            filename (str): the name of the file

        Returns:
            list : list of line information from the file (and includes)
        '''

        absn = os.path.abspath(filename)
        basep = os.path.dirname(absn)

        with open(filename, 'r') as f:
            raw_lines = f.readlines()

        ret = []
        pos = 0
        for line in raw_lines:
            pos += 1
            n = line.strip()
            if n.startswith('.include'):
                # TODO error checking/reporting
                n = n[8:].strip()
                n = os.path.join(basep, n)
                ret = ret + self.load_lines(n)
                continue
            ret.append({
                'file_name': filename,
                'line_number': pos,
                'text': n
            })
        return ret

    def remove_comments_and_blanks(self, lines):
        '''Make a list of code lines (no blanks, no comments)

        For each line returned, the "original_text" has the unaltered

        Args:
            lines (list): complete list of lines from the files

        Returns:
            List : just the lines of code (and without comments)
        '''
        ret = []
        for line in lines:
            n = line['text']
            i = n.find(';')
            if i >= 0:
                n = n[0:i].strip()
            if n:
                line['original_text'] = line['text']
                line['text'] = n
                ret.append(line)
        return ret

    def process_data_term(self, line, pass_number: int, cur_term: str):
        '''Process a numerical value

        Args:
            line: the code line
            pass_number: 0 or 1
            cur_term: the term to parse
        Returns:
            List: a list of bytes (first-pass return all 0s)

        '''
        is_word = False
        if(cur_term.startswith('word ')):
            is_word = True
            cur_term = cur_term[5:].strip()
        elif(cur_term.startswith('byte ')):
            is_word = False
            cur_term = cur_term[5:].strip()

        if cur_term[0] >= '0' and cur_term[0] <= '9':
            cur_term = cur_term.replace('_', '')
            cur_term = cur_term.replace('.', '0')

        if pass_number == 0:
            if is_word:
                return [0, 0]
            else:
                return [0]
        else:
            if is_word:
                return self.cpu.make_word(self.parse_numeric(cur_term))
            else:
                return [self.parse_numeric(cur_term)]

    def process_directive_data(self, line, pass_number: int):
        '''Process a data directive

        Creates the data list for a data-directive command

        Args:
            line : the code line
            pass_number : 0 or 1
        '''

        line['data'] = []

        cur_term = ''
        in_string = False

        for c in line['text'][1:]:
            if in_string:
                if c == '"':
                    in_string = False
                    for t in cur_term:
                        line['data'].append(ord(t))
                    cur_term = ''
                else:
                    cur_term = cur_term + c
            else:
                if c == '"':
                    in_string = True
                    cur_term = ''
                elif c == ',':
                    cur_term = cur_term.strip()
                    if cur_term:
                        dtt = self.process_data_term(line, pass_number, cur_term)
                        for d in dtt:
                            line['data'].append(d)
                    cur_term = ''
                else:
                    cur_term = cur_term + c

        if in_string:
            raise ASMException('Missing closing quotes', line)

        cur_term = cur_term.strip()
        if cur_term:
            dtt = self.process_data_term(line, pass_number, cur_term)
            for d in dtt:
                line['data'].append(d)

    def parse_numeric(self, s: str):
        '''Parse a numeric expression

        Uses the python eval to evalutate expressions,

        Args:
            s (str): the expression

        Returns:
            The evaluation value
        '''
        # TODO: I don't like this here. We need to parse these out while selecting opcodes.
        s = s.replace('>', '')
        s = s.replace('<', '')
        z = {**self.labels, **self.defines}
        v = eval(s, None, z)
        return v

    def process_define(self, line, pass_number: int):
        '''Process a define

        Defines are of the form .VAR = VALUE. This method adds to the
        growing list of defines.

        Args:
            line : the code line
            pass_number (int): 0 or 1

        '''

        n = line['text']
        # print('##',n)
        i = n.index('=')
        v = n[i + 1:].strip()
        n = n[1:i].strip()
        if pass_number == 2 and (n in self.labels or n in self.defines):
            # Second pass ... handle multiply-defined errors
            raise ASMException('Multiply defined: ' + n, line)
        if n.startswith('_'):
            # Handle configs
            self.process_config_define(n, v)
        else:
            # Must be a numeric expression
            v = self.parse_numeric(v)
            self.defines[n] = v

    def process_config_define(self, key: str, value: str):
        '''Process config defines

        Config defines are of the form ._VAR = VALUE.
        '''
        if key == '_CPU':
            self.cpu = opcodetools.cpu.cpu_manager.get_cpu_by_name(value)
            self.cpu.init_assembly()
            if not self.cpu._opcodes[0].frags:
                self.cpu.make_frags()
        self.defines[key] = value

    def assemble(self):
        '''Two-pass assembly
        '''

        for pass_number in range(2):

            address = 0

            for line in self.code:

                n = line['text']

                if n.startswith('.'):
                    # Define (key = value)
                    i = n.find('"')  # In case the right side is a string, which might have '=' in it.
                    if i < 0:
                        i = len(n)
                    j = n.find('=')
                    if j < i and j >= 0:
                        self.process_define(line, pass_number)

                    # Data (list of bytes/words)
                    elif n.startswith('. ') or n.startswith('.word ') or n.startswith('.byte '):
                        self.process_directive_data(line, pass_number)
                        line['address'] = address

                    else:
                        raise ASMException('Unknown directive: ' + n, line)

                elif n.endswith(':'):
                    # Label (or origin)
                    n = n[:-1].strip()
                    if pass_number == 0:
                        if n in self.labels or n in self.defines:
                            raise ASMException(
                                'Multiply defined: ' + n, line)

                    try:
                        # A number ... this is an origin
                        if n.upper().startswith('0X'):
                            address = int(n[2:], 16)
                        else:
                            address = int(n)
                    except Exception:
                        # Not a number ... this is a label to remember
                        self.labels[n] = address
                else:
                    line['address'] = address
                    if not self.cpu:
                        raise ASMException('No CPU defined', line)
                    # Opcode
                    op = self.cpu.find_opcode_for_text(n, self)
                    if not op:
                        raise ASMException('Unknown opcode: ' + n, line)

                    # TODO: here
                    line['data'] = self.cpu.fill_in_opcode(n, self, address, op, pass_number)

                if 'data' in line:
                    address = address + len(line['data'])

    def write_listing(self, fname):
        with open(fname, 'w') as f:
            f.write('#### Labels\n')
            keys = self.labels.keys()
            keys = sorted(keys)
            for label in keys:
                f.write('{:16} = 0x{:04X}\n'.format(label, self.labels[label]))
            f.write('\n')
            f.write('#### Defines\n')
            keys = self.defines.keys()
            keys = sorted(keys)
            for define in keys:
                v = self.defines[define]
                if isinstance(v, str):
                    f.write('{:16} = {}\n'.format(define, v))
                else:
                    f.write('{:16} = 0x{:04X}\n'.format(define, v))
            f.write('\n')

            for line in self.lines:
                addr = ''
                if 'address' in line:
                    addr = '{:04X}:'.format(line['address'])
                data = ''
                if 'data' in line:
                    for d in line['data']:
                        data = data + '{:02X} '.format(d)
                data = data.strip()
                txt = line['text']
                if 'original_text' in line:
                    txt = line['original_text']
                f.write('{} {:16} {}\n'.format(addr, data, txt))

    def write_binary(self, name):
        for line in self.lines:
            if 'address' in line:
                org = line['address']
                break

        with open(name, 'wb') as f:
            for line in self.lines:
                if 'data' in line and line['data']:
                    new_org = line['address']
                    if new_org < org:
                        raise Exception('Origin problems')
                    while org < new_org:
                        f.write(bytearray([0xFF]))
                        org = org + 1
                    f.write(bytearray(line['data']))
                    org = org + len(bytearray(line['data']))


if __name__ == '__main__':

    a = Assembler('../../../devboard8051/test.asm')
    a.assemble()
