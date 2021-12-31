

class MemoryMapEntry:

    def __init__(self, first, last, name, description, special):
        self.first = first
        self.last = last
        self.name = name
        self.description = description
        self.special = special


class MemoryMap:

    def __init__(self, md=[], entries=None):
        if entries is not None:
            self.entries = entries
            return

        self.entries = []

        for i in range(len(md)):
            group = md[i]
            if group.group_type == 'TABLE' and md[i - 1].group_type == 'META' and md[i - 1].lines[0].text.strip() == '>>> memory':
                for p in group.lines[2:]:
                    data = p.text.split('|')[1:-1]
                    i = data[0].find(':')
                    if i >= 0:
                        first_txt = data[0][:i].strip()
                        last_txt = data[0][i + 1:].strip()
                    else:
                        first_txt = data[0].strip()
                        last_txt = first_txt
                    special = ''
                    for i in range(len(first_txt)):
                        if first_txt[i] in 'pwr':
                            special = first_txt[i:]
                            first_txt = first_txt[:i]
                            break
                    for i in range(len(last_txt)):
                        if last_txt[i] in 'pwr':
                            last_txt = last_txt[:i]
                            break

                    try:
                        first = int(first_txt, 16)
                        last = int(last_txt, 16)
                        self.entries.append(MemoryMapEntry(first, last, data[1].strip(), data[2].strip(), special))
                    except Exception:
                        raise Exception('Invalid map entry:' + data[0])

    def find_entry_by_address(self, address, use):

        for entry in self.entries:

            # Every entry is a port or non-port. Make sure the entry matches any port/non-port
            # in the usage.

            if 'port' in use and 'p' not in entry.special:
                # Requested a port, but this entry isn't one
                continue
            if 'p' in entry.special and 'port' not in use:
                # Requested a non-port, but this entry is one
                continue

            if address >= entry.first and address <= entry.last:

                # This entry matches portness and address. Now check for read/write.

                if 'r' not in entry.special and 'w' not in entry.special:
                    # No direction given to this entry ... use it for all reads and writes
                    return entry

                # Reduce the use to r or w (r in case of neither or both)
                at = 'r'
                if 'w' in use:
                    # Only if pure write
                    at = 'w'

                if at in entry.special:
                    return entry

        return None
