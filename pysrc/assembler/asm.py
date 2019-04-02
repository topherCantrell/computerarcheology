
import importlib


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

    def load_lines(self, filename):
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
                ret = ret + self.load_lines(n)
                continue
            ret.append({
                'file_name': filename,
                'line_number': pos,
                'text': n
            })
        return ret

    def remove_comments_and_blanks(self, lines):
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

    def process_directive_data(self, line, pass_number):
        n = line['text'][1:].split(',')
        if pass_number == 0:
            line['data'] = [0] * len(n)
        else:
            line['data'] = []
            for v in n:
                line['data'].append(self.parse_numeric(v))

    def parse_numeric(self, s):
        z = {**self.labels, **self.defines}
        v = eval(s, None, z)
        return v

    def print_listing(self):
        print('#### Labels')
        keys = self.labels.keys()
        keys = sorted(keys)
        for label in keys:
            print('{:16} = 0x{:04X}'.format(label, self.labels[label]))
        print()
        print('#### Defines')
        keys = self.defines.keys()
        keys = sorted(keys)
        for define in keys:
            v = self.defines[define]
            if isinstance(v, str):
                print('{:16} = {}'.format(define, v))
            else:
                print('{:16} = 0x{:04X}'.format(define, v))
        print()

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
            print('{} {:16} {}'.format(addr, data, txt))

    def write_binary(self):
        # TODO
        pass

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
            lib = importlib.import_module('cpu.cpu_' + value)
            self.cpu = lib.get_cpu()
        self.defines[key] = value

    def assemble(self):

        for pass_number in range(2):

            address = 0

            for line in self.code:
                n = line['text']

                # Directives start with a '.'
                if n.startswith('.'):

                    # Define (key = value)
                    if '=' in n:
                        # TODO could be a string with an "=" in it
                        self.process_define(line, pass_number)

                    # Data (list of bytes/words)
                    elif n.startswith('. '):  # TODO or n.startswith('.W')
                        self.process_directive_data(line, pass_number)
                        line['address'] = address

                    else:
                        raise Exception('Unknown directive: ' + n)

                elif n.endswith(':'):
                    # Label (or origin)
                    if pass_number == 1:  # second pass only
                        n = n[:-1].strip()
                        if n in self.labels or n in self.defines:
                            raise ASMException('Multiply defined: ' + n, line)

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
                    # Opcode
                    op = self.cpu.find_opcode(n)
                    line['data'] = self.cpu.fill_in_opcode(op, pass_number)

                if 'data' in line:
                    address = address + len(line['data'])
