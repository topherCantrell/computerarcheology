from assembler import asm

if __name__ == '__main__':

    asa = asm.Assembler('hello.asm')

    try:
        asa.assemble()
        asa.print_listing()
        asa.write_binary('hello.bin')
    except asm.ASMException as ex:
        print(ex, ex.line)
