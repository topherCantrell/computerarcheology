
import importlib
import os


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
        
        if cur_term[0]>='0' and cur_term[0]<='9':
            cur_term = cur_term.replace('_','')
            cur_term = cur_term.replace('.','0')
        
        if pass_number==0:
            if is_word:
                return [0,0]
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
                    if new_org<org:
                        raise Exception('Origin problems')
                    while org<new_org:
                        f.write(bytearray([0xFF]))
                        org = org + 1
                    f.write(bytearray(line['data']))
                    org = org + len(bytearray(line['data']))

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
                #print(line)
                # try:
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
                    op = self.cpu.find_opcode(n,self)
                    if not op:
                        raise ASMException('Unknown opcode: ' + n, line)
                    line['data'] = self.cpu.fill_in_opcode(
                        self, address, op, pass_number)

                if 'data' in line:
                    address = address + len(line['data'])

                # except Exception as e:
                #    raise ASMException(e, line)
