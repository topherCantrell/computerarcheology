from dataclasses import dataclass
from typing import List

_PARA_STARTS = ['```', '>>>', '#', '*', '|']


@dataclass
class TextLine:
    """A line of text from a markdown file"""
    file_name: str
    line_number: int
    text: str


@dataclass
class Group:
    """A group of lines from a markdown file"""
    group_type: str
    lines: List[TextLine]


def write_markdown_file(fname, md):
    with open(fname, 'w') as f:
        for para in md:
            if para.group_type in ['TEXT', 'HEADER', 'META', 'LIST', 'TABLE', 'BLOCK']:
                for p in para.lines:
                    f.write(p.text + '\n')
                f.write('\n')
            else:
                ex = para.lines[0]
                raise Exception(f'Unknown markdown group type: {para.group_type} before {ex.file_name} line {ex.line_number}')


def _add_through(group, text_lines, pos, st):
    endpos = len(text_lines)
    group.lines.append(text_lines[pos])
    while True:
        pos += 1
        if pos >= endpos:
            return endpos
        line = text_lines[pos]
        det = line.text.strip()
        if not det.startswith(st):
            return pos
        group.lines.append(line)


def _read_block(ret, text_lines, pos):
    group = Group('BLOCK', [])
    ret.append(group)

    start = pos
    group.lines.append(text_lines[pos])
    pos += 1
    endpos = len(text_lines)
    while True:
        if pos >= endpos:
            ex = text_lines[start]
            raise Exception(f'Missing end of block. Block begins: {ex.file_name} line {ex.line_number}')
        line = text_lines[pos]
        group.lines.append(line)
        pos += 1
        if line.text.strip().startswith('```'):
            return pos


def _read_meta(ret, text_lines, pos):
    group = Group('META', [])
    ret.append(group)
    return _add_through(group, text_lines, pos, '>>>')


def _read_header(ret, text_lines, pos):
    group = Group('HEADER', [text_lines[pos]])
    ret.append(group)
    return pos + 1


def _read_list(ret, text_lines, pos):
    group = Group('LIST', [])
    ret.append(group)
    return _add_through(group, text_lines, pos, '*')


def _read_table(ret, text_lines, pos):
    group = Group('TABLE', [])
    ret.append(group)
    return _add_through(group, text_lines, pos, '|')


def _read_paragraph(ret, text_lines, pos):

    group = Group('TEXT', [text_lines[pos]])
    ret.append(group)

    pos += 1
    endpos = len(text_lines)
    while True:
        if pos >= endpos:
            return endpos
        line = text_lines[pos]
        det = line.text.strip()
        if not det:
            return pos + 1
        for tag in _PARA_STARTS:
            if det.startswith('**'):
                # Bold at the start ... not a list
                break
            if det.startswith(tag):
                return pos
        group.lines.append(line)
        pos += 1


def read_markdown_paragraphs(filename):

    text_lines = []

    line_number = 0
    with open(filename) as f:
        for line in f:
            line_number += 1
            if line.endswith('\n'):
                line = line[:-1]
            text_lines.append(TextLine(filename, line_number, line))

    ret = []

    endpos = len(text_lines)
    i = 0
    while i < endpos:
        line = text_lines[i]
        det = line.text.strip()

        if not det:
            # Ignore blank lines before a paragraph
            i += 1
            continue

        if det.startswith('```'):
            i = _read_block(ret, text_lines, i)

        elif det.startswith('>>>'):
            i = _read_meta(ret, text_lines, i)

        elif det.startswith('#'):
            i = _read_header(ret, text_lines, i)

        elif det.startswith('*') and not det.startswith('**'):
            i = _read_list(ret, text_lines, i)

        elif det.startswith('|'):
            i = _read_table(ret, text_lines, i)

        else:
            i = _read_paragraph(ret, text_lines, i)

    return ret
