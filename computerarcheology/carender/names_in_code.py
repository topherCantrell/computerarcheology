'''
Tags of the form "{...}" are totally controlled by the code. The code will remove them
and add the correct value back.

Tags of the form "{!...}" are not touched. These are manually added by the human.

Tags of the form "{+...}" tell the code to override the "not a name opcode" and to
treat the value as a name. The code will replace the name with the correct value.

Tags of the form "{-}" tell the code to override the "is a name opcode".

  LDA  $4000     ; {lives}
  LDX  #$4000    ; {+lives}
  LDB  $4000,X   ; {!lives}
  LDB  $4000     ; {-}

Use `...` to embed html into a comment

Use `{!...}` to insert a table-reference link into a comment
'''

import os

import opcodetools.cpu.cpu_manager

from computerarcheology.carender import cacode
from computerarcheology.carender import cainfo
from computerarcheology.carender import markdown
from computerarcheology.carender import memory_map


def collect_labels(line_details):
    ret = []
    last_address = None
    for i in range(len(line_details) - 1, -1, -1):
        parts = line_details[i][1]
        if parts['address'] is not None:
            last_address = parts['address']
        if parts['label']:
            if last_address is None:
                raise Exception('Dangling label on end of code')
            ent = memory_map.MemoryMapEntry(last_address, last_address,
                                            parts['label'], '', '')
            ret.append(ent)

    return ret


def extract_constant(txt):
    i = txt.find('$')
    const = ''
    for c in txt[i + 1:]:
        if c not in '0123456789ABCDEF':
            break
        const += c
    return int(const, 16)


def _rebuild_text(line, parts, spacing, cpu_name):

    address_text = hex(parts['address'])[2:].upper()
    address_text = address_text.rjust(spacing['address_size'], '0')

    data_text = ''
    for d in parts['data']:
        dt = hex(d)[2:].upper().rjust(2, '0')
        data_text = data_text + dt + ' '
    data_text = data_text[:-1].ljust(spacing['data'], ' ')

    opcode_text = parts['opcode']

    i = opcode_text.find(' ')
    if i >= 0:
        a = opcode_text[:i]
        b = opcode_text[i + 1:].strip()
        opcode_text = a.ljust(spacing['mnemonic'][0]) + b.ljust(spacing['mnemonic'][1])
    else:
        opcode_text = opcode_text.ljust(spacing['mnemonic'][0] + spacing['mnemonic'][1])

    comment = parts['comment']
    if comment is None:
        comment = ''
    else:
        comment = '; ' + comment.strip()

    line.text = address_text + ': ' + data_text + opcode_text + comment

def extract_data(lines):
    
    for line in lines:
        print(dir(line))
        print(line.data)

def update_names_in_code(directory, filename, check_binary=True,extract_binary=False):

    # Load the markdown file

    md = markdown.read_markdown_paragraphs(os.path.join(directory, filename))    

    bp_offset = 0
    # TODO we should allow the DP to change through the code ... not just once at the top
    for m in md:
        if m.group_type=='META':
            if 'directPage' in m.lines[0].text:
                i = m.lines[0].text.find('directPage')
                bp_offset = int(m.lines[0].text[i+11:],16)

    # Get all the code from the markdown (or return if there are no code lines)

    lines = cainfo.read_code_text_lines(md)    
    if not lines:        
        # No code in this file -- nothing to do
        return md,None

    bindata = None
    if extract_binary:        
        gaps = cainfo.read_origin_gaps(md)        
        origin_md, binary_md = cacode.parse_binary(lines, gaps)
        bindata = bytes(binary_md)

    # Get the CPU (if any -- might be data-only with no opcodes)

    cpu_name = cainfo.read_cpu(md)
    cpu = opcodetools.cpu.cpu_manager.get_cpu_by_name(cpu_name)

    # Spacing between fields if we need to clean up lines

    if cpu:
        spacing = cpu.get_field_spacing()

    # Get the hardware/ram address-map table references (if any)

    tables = cainfo.read_memory_tables(md, directory)

    # Make sure code binary matches binary file (if requested)

    #check_binary = False
    if check_binary:
        gaps = cainfo.read_origin_gaps(md)
        binary_file = cainfo.read_binary_file_name(md)
        info = cacode.load_binary_files(binary_file, directory)
        origin = info['origin']
        binary_org = info['data']
        origin_md, binary_md = cacode.parse_binary(lines, gaps)
        binary_md = bytes(binary_md)
        if origin_md != origin:
            raise Exception('Binary origins are different')
        if len(binary_org) != len(binary_md):
            raise Exception('Binary data has different length')
        for i in range(len(binary_org)):
            if binary_org[i] != binary_md[i]:
                raise Exception('First binary difference at ' + hex(i) + ' ' + hex(binary_md[i]) + ' ' + hex(binary_org[i]))

    # Parse each code line into its parts and find the opcode object for each line with an opcode

    code_start = None
    code_end = None

    line_details = []
    for line in lines:
        parts = cacode.split_disassembly_line(line)
        if parts['address'] is not None:
            if code_start is None:
                code_start = parts['address']
            code_end = parts['address']
        opcode = None
        if parts['opcode']:
            a = parts['opcode']
            i = a.find(' ')
            if i >= 0:
                a = a[0:i]            
            opcode = cpu.find_opcodes_for_binary(parts['data'], exact=True, hint=parts['opcode'])
            if not opcode:
                raise Exception('No opcode found: ' + line.text)
            if len(opcode) > 1:                
                mop = None
                for o in opcode:
                    if o.mnemonic.startswith(a):
                        mop = o
                        break
                if not mop:
                    print('>',o.mnemonic,opcode,a,line)
                    raise Exception('Multiple opcode matches found: ' + line)
                opcode = [mop]

            opcode = opcode[0]

            # A sanity check to make sure we aren't mangling things.

            a = opcode.mnemonic.split()
            b = parts['opcode'].split()
            if a[0] != b[0]:
                raise Exception('Check on opcode: ' + str(parts) + ' ' + str(opcode.mnemonic))

        line_details.append([line, parts, opcode])

    # Collect the code labels and add a new address-map to the tables

    labs = collect_labels(line_details)
    code_table = memory_map.MemoryMap(entries=labs)
    tables['code'] = ['', code_table]
    
    # We only support 3 types of memory map tables (ram, hardware, and code)

    for name in tables:
        if name not in ['ram', 'hard', 'code']:
            raise Exception('Unsupported memory map type: ' + name)

    # Here we go ... line by line

    for line, parts, opcode in line_details:

        # Make sure this is a number substitution

        if not opcode:
            # Ignore labels and data
            continue

        if not opcode.use:
            # There are no numbers to process
            _rebuild_text(line, parts, spacing, cpu_name)
            continue

        if len(opcode.use) > 1:
            _rebuild_text(line, parts, spacing, cpu_name)
            continue
            # TODO eventually support this. Needed for "LDX  (IX+ii),bb"
            # raise Exception('Multiple fillins per line not implemented')

        # Look for "+" and "-" override entries
        # Remove and existing labels

        comment = parts['comment']
        flags = None
        if comment:
            comment = comment.strip()
            if comment.startswith('{!'):
                # Explicitly given ... don't change it
                _rebuild_text(line, parts, spacing, cpu_name)
                continue
            elif comment.startswith('{-}'):
                # Explicitly ignore any memory reference
                _rebuild_text(line, parts, spacing, cpu_name)
                continue
            elif comment.startswith('{+'):
                # Treat this as a memory reference no matter what
                flags = '+'

            # Remove any name after {
            if comment.startswith('{'):
                i = 0
                j = comment.find('}')
                if j < 0:
                    raise Exception('Expected } in "' + comment + '"')
                if comment.startswith('{+'):
                    j -= 1
                    i += 2
                else:
                    if len(comment) > j + 1 and comment[j + 1] == ' ':
                        j += 1
                comment = comment[0:i] + comment[j + 1:]

                parts['comment'] = comment

        # How is the number substitution in this opcode being used?

        if flags == '+':
            # Forcing this to a data access
            # TODO force to code, data, or port?
            use = ['data']
        else:
            use = list(opcode.use.values())[0]

        # Ignore if it isn't something we know about

        if 'data' not in use and 'code' not in use and 'port' not in use:
            # Nothing for us to do
            _rebuild_text(line, parts, spacing, cpu_name)
            continue        

        # Get the numeric constant

        if '$' not in line.text:
            raise Exception('Expected to find "$" constant')

        c = extract_constant(line.text)
        
        if 'bp' in use:
            c = c + bp_offset
            #print(c,line)
            #raise 'oops'

        # The search order depends on the type of access

        order = ['hard', 'ram', 'code']  # Default is plain-memory access
        if 'code' in use:
            order = ['code', 'hard', 'ram']  # Search code first
        elif 'port' in use:
            order = ['hard']  # Only search hardware

        # Search the tables for the first match

        fnd = None
        for name in order:
            if name in tables:
                table = tables[name]
                en = table[1].find_entry_by_address(c, use)
                if en:
                    fnd = [name, table, en]
                    break

        if not fnd:
            if c >= code_start and c <= code_end:
                if comment is None:
                    comment = ''
                if not comment.startswith('{+}'):
                        # Leave a note in the comment: {+} or {}
                        # The renderer can tag naked address references
                        comment = '{} ' + comment
                        parts['comment'] = comment

            # No reference in our tables ... just leave the number alone
            _rebuild_text(line, parts, spacing, cpu_name)
            continue

        # Add the reference to the start of the comment

        ref = fnd[0] + '.' + fnd[2].name
        if c != fnd[2].first:
            ofs = c - fnd[2].first
            ofs = hex(ofs)[2:].upper()
            ref = ref + f'+{ofs}'

        if comment is None:
            comment = ''

        if comment.startswith('{+}'):
            comment = '{+' + ref + '}' + comment[3:]
        else:
            comment = '{' + ref + '} ' + comment

        parts['comment'] = comment

        _rebuild_text(line, parts, spacing, cpu_name)

    markdown.write_markdown_file(os.path.join(directory, filename), md)

    return md,bindata


if __name__ == '__main__':
    update_names_in_code('../content/arcade/asteroids', 'vectorrom.md')
