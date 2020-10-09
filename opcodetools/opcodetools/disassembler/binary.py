from typing import List


def load_binary(names: str) -> List[int]:
    '''Read a group of binary files

    For example "a.bin + b.bin+c.bin"

    Args:
        names (str) : the group of names
    Returns:
        List[int] : the binary data
    '''

    names = names.split('+')
    ret = []
    for n in names:
        n = n.strip()
        with open(n, 'rb') as f:
            data = f.read()
            for d in data:
                ret.append(int(d))

    return ret
