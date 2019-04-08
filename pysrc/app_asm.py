from assembler import asm

if __name__ == '__main__':

    asa = asm.Assembler('../../RC2014/code/echo.asm')

    try:
        asa.assemble()
        asa.write_listing('../../RC2014/code/echo.lst')
        asa.write_binary('../../RC2014/code/echo.bin')
    except asm.ASMException as ex:
        print(ex, ex.line)
