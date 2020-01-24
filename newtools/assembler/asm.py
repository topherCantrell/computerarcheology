import os

from cpu.cpu_common import CPU


class ASMException(Exception):
    def __init__(self, message, line):
        super().__init__(message)
        self.line = line


class Assembler:

    def __init__(self, filename):
        self.lines = self.load_lines(filename)
        self.code = self.remove_comments_and_blanks(self.lines)
        self.defines = {}
        self.labels = {}
        self.cpu = None

    def load_lines(self, filename: str):
        '''Load the lines from the given file

        This method also recurses into include files.

        The information on a line like is:
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

        abs = os.path.abspath(filename)
        basep = os.path.dirname(abs)

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

    def _process_data_term(self, line, pass_number, cur_term):
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

    def process_directive_data(self, line, pass_number):

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
                        dtt = self._process_data_term(line, pass_number, cur_term)
                        for d in dtt:
                            line['data'].append(d)
                    cur_term = ''
                else:
                    cur_term = cur_term + c

        if in_string:
            raise ASMException('Missing closing quotes', line)

        cur_term = cur_term.strip()
        if cur_term:
            dtt = self._process_data_term(line, pass_number, cur_term)
            for d in dtt:
                line['data'].append(d)

    def parse_numeric(self, s):
        z = {**self.labels, **self.defines}
        v = eval(s, None, z)
        return v

    def process_define(self, line, pass_number):

        n = line['text']
        i = n.index('=')
        v = n[i + 1:].strip()
        n = n[1:i].strip()
        if pass_number == 2 and (n in self.labels or n in self.defines):
            raise ASMException('Multiply defined: ' + n, line)
        if n.startswith('_'):
            self.process_config_define(n, v)
        else:
            v = self.parse_numeric(v)
            self.defines[n] = v

    def process_config_define(self, key, value):
        if key == '_CPU':
            self.cpu = CPU.get_cpu(value)
        self.defines[key] = value

    def process_directive_data(self, line, pass_number):
        pass

    def assemble(self):

        for pass_number in range(2):

            address = 0

            for line in self.code:

                n = line['text']

                if n.startswith('.'):
                    # Define (key = value)
                    if '=' in n:
                        # TODO could be a string with an "=" in it
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
                    except:
                        # Not a number ... this is a label to remember
                        self.labels[n] = address
                else:
                    line['address'] = address
                    if not self.cpu:
                        raise ASMException('No CPU defined', line)
                    # Opcode
                    op = self.cpu.find_opcode(n, self)
                    if not op:
                        raise ASMException('Unknown opcode: ' + n, line)
                    line['data'] = self.cpu.fill_in_opcode(
                        self, address, op, pass_number)

                if 'data' in line:
                    address = address + len(line['data'])


if __name__ == '__main__':

    a = Assembler('../../../devboard8051/test.asm')
    a.assemble()
