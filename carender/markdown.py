
PARA_STARTS = ['```', '>>>', '#', '*', '|']


def load_raw_lines(fname):
    ret = []
    with open(fname) as f:
        for line in f:
            ret.append(line.strip())
    return ret


def _add_through(ret, data, pos, st):
    endpos = len(data)
    ret[-1].append(data[pos])
    while True:
        pos += 1
        if pos >= endpos:
            return endpos
        line = data[pos]
        det = line.strip()
        if not det.startswith(st):
            return pos
        ret[-1].append(line)


def _read_block(ret, data, pos):
    #print('START BLOCK LINE ' + str(pos + 1))
    start = pos
    ret.append(['BLOCK', data[pos]])
    pos += 1
    endpos = len(data)
    while True:
        if pos >= endpos:
            raise Exception('Missing end of block. Begins on line ' + str(start + 1))
        line = data[pos]
        ret[-1].append(line)
        pos += 1
        if line.strip().startswith('```'):
            return pos


def _read_meta(ret, data, pos):
    ret.append(['META'])
    return _add_through(ret, data, pos, '>>>')


def _read_header(ret, data, pos):
    ret.append(['HEADER', data[pos]])
    return pos + 1


def _read_list(ret, data, pos):
    ret.append(['LIST'])
    return _add_through(ret, data, pos, '*')


def _read_table(ret, data, pos):
    ret.append(['TABLE'])
    return _add_through(ret, data, pos, '|')


def _read_paragraph(ret, data, pos):
    ret.append(['TEXT', data[pos]])
    pos += 1
    endpos = len(data)
    while True:
        if pos >= endpos:
            return endpos
        line = data[pos]
        det = line.strip()
        if not det:
            return pos + 1
        for tag in PARA_STARTS:
            if det.startswith('**'):
                # Bold at the start ... not a list
                break
            if det.startswith(tag):
                return pos
        ret[-1].append(line)
        pos += 1


def read_markdown_paragraphs(data):

    if isinstance(data, str):
        data = load_raw_lines(data)

    ret = []

    endpos = len(data)
    i = 0
    while i < endpos:
        line = data[i]
        det = line.strip()

        if not det:
            # Ignore blank lines before a paragraph
            i += 1
            continue

        if det.startswith('```'):
            i = _read_block(ret, data, i)

        elif det.startswith('>>>'):
            i = _read_meta(ret, data, i)

        elif det.startswith('#'):
            i = _read_header(ret, data, i)

        elif det.startswith('*') and not det.startswith('**'):
            i = _read_list(ret, data, i)

        elif det.startswith('|'):
            i = _read_table(ret, data, i)

        else:
            i = _read_paragraph(ret, data, i)

    return ret
