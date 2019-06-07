import os

from assembler import asm


if __name__ == '__main__':

    asm_file = '../../doublegap/DoubleGap.asm'

    abpath = os.path.abspath(asm_file)
    i = abpath.rindex('.')
    basepath = abpath[0:i]

    list_file = basepath + '.lst'
    bin_file = basepath + '.bin'

    asa = asm.Assembler(asm_file)

    try:
        asa.assemble()
        asa.write_listing(list_file)
        asa.write_binary(bin_file)
    except asm.ASMException as ex:
        print(ex, ex.line)
