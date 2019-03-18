import code.markdown_line
import code.markdown_utils
import code.table_line


class MemoryTable:

    def __init__(self, filename):

        # print(":"+filename+":")

        lines, _ = code.markdown_utils.load_file(filename)

        self.entries = []

        i = filename.find('/content')
        filename = filename[i + 9:]
        filename = filename.replace('\\', '/')
        filename = filename.split('/')

        while True:
            if '..' not in filename:
                break
            i = filename.index('..')
            filename = filename[0:i - 1] + filename[i + 1:]

        filename = '/' + '/'.join(filename)
        filename = filename.replace('.md', '.html')
        self.filename = filename

        for md in lines:
            if type(md) is code.table_line.Table and md.is_memory:
                for m in md.get_lines()[2:]:
                    cols = m.text.split('|')[1:-1]
                    addr = cols[0].strip()
                    if addr == '':
                        continue
                    reading = False
                    writing = False
                    porting = False
                    if 'r' in addr:
                        reading = True
                    if 'w' in addr:
                        writing = True
                    if not reading and not writing:
                        # Not specified ... treat it as both
                        reading = True
                        writing = True
                    if 'p' in addr:
                        porting = True
                    addr = addr.replace('r', '').replace(
                        'w', '').replace('p', '')
                    taddr = addr.split(':')
                    if len(taddr) < 2:
                        taddr.append(taddr[0])
                    taddr[0] = int(taddr[0], 16)
                    taddr[1] = int(taddr[1], 16)
                    name = cols[1].strip()
                    if not name:
                        name = 'm' + str(taddr[0])
                    self.entries.append({
                        'range': taddr,
                        'name': name,
                        'description': cols[2].strip(),
                        'read': reading,
                        'write': writing,
                        'port': porting
                    })

    def find_entry(self, address, bus):

        for e in self.entries:
            if address >= e['range'][0] and address <= e['range'][1]:

                if 'x' in bus and e['port']:
                    # No jumps to port addresses
                    continue

                if 'p' in bus and not e['port']:
                    # The opcode is for port access, but this entry is not a
                    # port ... keep trying
                    continue
                if 'w' in bus and not e['write']:
                    # The opcode is a write, but this is not a writeable
                    # address ... keep trying
                    continue
                if 'r' in bus and not e['read']:
                    # The opcode is a read, but this is not a readable address
                    # ... keep trying
                    continue
                return e
        return None
