from tools import binary

"""
src = '../../content/CoCo/MegaBug/Code.md'
bin = '../../content/CoCo/MegaBug/MegaBug.bin'
org = 0xC000
binary.compare_source_to_binary(src, bin, org)

src = '../../content/CoCo/RaakaTu/Code.md'
bin = '../../content/CoCo/RaakaTu/RaakaTu.bin'
org = 0x0600
binary.compare_source_to_binary(src, bin, org)

src = '../../content/CoCo/Bedlam/Code.md'
bin = '../../content/CoCo/Bedlam/Bedlam.bin'
org = 0x0600
binary.compare_source_to_binary(src, bin, org)

src = '../../content/TRS80/Pyramid/Code.md'
bin = '../../content/TRS80/Pyramid/rom/Pyramid.bin'
org = 0x4300
binary.compare_source_to_binary(src, bin, org)

src = '../../content/TRS80/RaakaTu/Code.md'
bin = '../../content/TRS80/RaakaTu/RAAKA.bin'
org = 0x4300
binary.compare_source_to_binary(src, bin, org)

src = '../../content/TRS80/Bedlam/Code.md'
bin = '../../content/TRS80/Bedlam/BEDLAM.bin'
org = 0x4300
binary.compare_source_to_binary(src, bin, org)
"""

org = 0xF000
src = 'd:/git/computerarcheology/content/atari2600/burgertime/CodeBank0.md'
bin = 'd:/git/computerarcheology/content/atari2600/burgertime/btBank0.bin'
binary.compare_source_to_binary(src, bin, org)
src = 'd:/git/computerarcheology/content/atari2600/burgertime/CodeBank1.md'
bin = 'd:/git/computerarcheology/content/atari2600/burgertime/btBank1.bin'
binary.compare_source_to_binary(src, bin, org)
src = 'd:/git/computerarcheology/content/atari2600/burgertime/CodeBank2.md'
bin = 'd:/git/computerarcheology/content/atari2600/burgertime/btBank2.bin'
binary.compare_source_to_binary(src, bin, org)
src = 'd:/git/computerarcheology/content/atari2600/burgertime/CodeBank3.md'
bin = 'd:/git/computerarcheology/content/atari2600/burgertime/btBank3.bin'
binary.compare_source_to_binary(src, bin, org)
src = 'd:/git/computerarcheology/content/atari2600/burgertime/CodeBank4.md'
bin = 'd:/git/computerarcheology/content/atari2600/burgertime/btBank4.bin'
binary.compare_source_to_binary(src, bin, org)
src = 'd:/git/computerarcheology/content/atari2600/burgertime/CodeBank5.md'
bin = 'd:/git/computerarcheology/content/atari2600/burgertime/btBank5.bin'
binary.compare_source_to_binary(src, bin, org)
src = 'd:/git/computerarcheology/content/atari2600/burgertime/CodeBank6.md'
bin = 'd:/git/computerarcheology/content/atari2600/burgertime/btBank6.bin'
binary.compare_source_to_binary(src, bin, org)
org = 0xF800
src = 'd:/git/computerarcheology/content/atari2600/burgertime/CodeBank7.md'
bin = 'd:/git/computerarcheology/content/atari2600/burgertime/btBank7.bin'
binary.compare_source_to_binary(src, bin, org)
