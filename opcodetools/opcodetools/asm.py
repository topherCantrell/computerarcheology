from opcodetools.assembler.assembler import Assembler

import sys

# TODO: lots of command line options:
#  - Listing file (yes/no)
#  - Output file (name)

a = Assembler(sys.argv[1])
a.assemble()

a.write_binary(sys.argv[1] + '.bin')
a.write_listing(sys.argv[1] + '.lst')
