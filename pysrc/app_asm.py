from assembler import asm

if __name__ == '__main__':

    asa = asm.Assembler('hello.asm')
    asa.assemble()
    asa.print_listing()
