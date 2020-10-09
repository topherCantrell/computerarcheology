import sys

from opcodetools.cpu import cpu_manager

# py dasm Z80 1000 "a.bin+b.bin+c.bin"

from opcodetools.disassembler import binary

cpuname = sys.argv[1]
org = int(sys.argv[2], 16)
names = sys.argv[3]

bindata = binary.load_binary(names)

cpu = cpu_manager.get_cpu_by_name(cpuname)

print('; CPU:', cpuname)
print('; ORIGIN:', hex(org))
print('; FILES:', names)
print()

pos = 0

while pos < len(bindata):
    ops = cpu.find_opcodes_for_binary(bindata[pos:])
    if len(ops) != 1:
        print(cpu.binary_to_string_unknown(pos + org, bindata[pos]))
        pos += 1
        continue

    opc = ops[0]

    dat = bindata[pos:pos + len(opc.code)]
    fills = cpu.get_mnemonic_fills(ops[0], dat, 0x1234)
    s = cpu.binary_to_string(opc, dat, pos + org, fills)
    pos += len(dat)

    print(s)
