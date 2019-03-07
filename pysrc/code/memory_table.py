import code.markdown_line
import code.markdown_utils
import code.table_line


class MemoryTable:

    def __init__(self, filename):

        # print(":"+filename+":")

        lines = code.markdown_utils.load_file(filename)

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
                    taddr = addr.split(':')
                    if len(taddr) < 2:
                        taddr.append(taddr[0])
                    taddr[0] = int(taddr[0], 16)
                    taddr[1] = int(taddr[1], 16)
                    self.entries.append({
                        'range': taddr,
                        'name': cols[1].strip(),
                        'description': cols[2].strip()
                    })

    def find_entry(self, address):
        for e in self.entries:
            if address >= e['range'][0] and address <= e['range'][1]:
                return e
        return None
