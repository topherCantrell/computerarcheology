from assembler import asm

if __name__ == '__main__':

    asa = asm.Assembler('../../RC2014/code/monitor.asm')

    try:
        asa.assemble()
        asa.write_listing('../../RC2014/code/monitor.lst')
        asa.write_binary('../../RC2014/code/monitor.bin')
    except asm.ASMException as ex:
        print(ex, ex.line)
