
def load_lines(filename):
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
            ret = ret + load_lines(n)
            continue
        ret.append({
            'file_name': filename,
            'line_number': pos,
            'text': n
        })
    return ret


def remove_comments_and_blanks(lines):
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


def _dir_data(line, labels, defines, pass_number):
    n = line['text'][1:].split(',')
    if pass_number == 0:
        line['data'] = [0] * len(n)
    else:
        line['data'] = []
        for v in n:
            line['data'].append(_get_numeric(v, labels, defines))


def _get_numeric(s, labels, defines):
    z = {**labels, **defines}
    v = eval(s, None, z)
    return v


def _print_listing(lines, labels, defines):
    print('labels', labels)
    print('defines', defines)
    # TODO
    for line in lines:
        print(line)


def _write_binary(lines):
    # TODO
    pass


def assemble(lines):

    labels = {}
    defines = {}

    for pass_number in range(2):

        address = 0

        for line in lines:
            n = line['text']
            if n.startswith('.'):
                # Directive

                # Define
                if '=' in n:
                    # TODO could be a string with an "=" in it
                    i = n.index('=')
                    v = n[i + 1:].strip()
                    n = n[1:i].strip()
                    if pass_number == 2 and (n in labels or n in defines):
                        raise Exception('Multiply defined: ' + n)
                    if not n.startswith('_'):
                        v = _get_numeric(v, labels, defines)
                    defines[n] = v

                # Data
                elif n.startswith('. '):  # TODO or n.startswith('.W')
                    _dir_data(line, labels, defines, pass_number)

                else:
                    raise Exception('Unknown directive: ' + n)

            elif n.endswith(':'):
                # Label (or origin)
                if pass_number == 1:  # second pass only
                    n = n[:-1].strip()
                    if n in labels or n in defines:
                        raise Exception('Multiply defined: ' + n)

                    try:
                        # A number ... this is an origin
                        if n.upper().startswith('0X'):
                            address = int(n[2:], 16)
                        else:
                            address = int(n)
                    except:
                        # Not a number ... this is a label to remember
                        labels[n] = address

            else:
                line['address'] = address
                # Opcode
                if pass_number == 0:
                    # TODO
                    line['data'] = [7, 8, 9]
                else:
                    # TODO
                    line['data'] = [7, 8, 9]

            if 'data' in line:
                address = address + len(line['data'])

    return (labels, defines)


if __name__ == '__main__':

    lines = remove_comments_and_blanks(load_lines('hello.asm'))
    (labels, defines) = assemble(lines)

    _print_listing(lines, labels, defines)
