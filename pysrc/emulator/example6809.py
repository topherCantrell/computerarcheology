#!/usr/bin/env python

"""
    MC6809 Example
    ~~~~~~~~~~~~~~

    A small example how to use the emulated 6809 CPU.

    Here we use a assembler listing to calculate a ZIP 32-bit CRC.
    The origin code by Johann E. Klasek, j AT klasek at

    The CRC32 will be compared with binascii.crc32() (written in C), see:
        https://docs.python.org/library/binascii.html

    Similar code used in unittests:
        MC6809/tests/test_6809_program.py
    ...and is part of the benchmark, too.

    :created: 2015 by Jens Diemer - www.jensdiemer.de
    :copyleft: 2015 by the MC6809 team, see AUTHORS for more details.
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""

import binascii
import string
import time
import sys

from MC6809.components.cpu6809 import CPU
from MC6809.components.memory import Memory
from MC6809.core.configs import BaseConfig


CFG_DICT = {
    "verbosity":None,
    "trace":None,
}


class Config(BaseConfig):
    RAM_START = 0x0000
    RAM_END = 0x7FFF

    ROM_START = 0x8000
    ROM_END = 0xFFFF


class MC6809Example(object):
    def __init__(self):
        cfg = Config(CFG_DICT)
        memory = Memory(cfg)
        self.cpu = CPU(memory, cfg)

    def cpu_test_run(self, start, end, mem):
        assert isinstance(mem, bytearray), "given mem is not a bytearray!"

        print("memory load at $%x: %s", start,
            ", ".join(["$%x" % i for i in mem])
        )
        self.cpu.memory.load(start, mem)
        if end is None:
            end = start + len(mem)
        self.cpu.test_run(start, end)

    def crc32(self, data):
        """
        Calculate a ZIP 32-bit CRC from data in memory.
        Origin code by Johann E. Klasek, j AT klasek at
        """
        data_address = 0x1000 # position of the test data
        self.cpu.memory.load(data_address, data)  # write test data into RAM
        self.cpu.index_x.set(data_address + len(data)) # end address
        addr_hi, addr_lo = divmod(data_address, 0x100) # start address

        self.cpu_test_run(start=0x0100, end=None, mem=bytearray([
            #                              0100|           .ORG  $100
            0x10, 0xCE, 0x40, 0x00, #      0100|           LDS   #$4000
            #                              0104|    CRCHH: EQU   $ED
            #                              0104|    CRCHL: EQU   $B8
            #                              0104|    CRCLH: EQU   $83
            #                              0104|    CRCLL: EQU   $20
            #                              0104| CRCINITH: EQU   $FFFF
            #                              0104| CRCINITL: EQU   $FFFF
            #                              0104|                            ; CRC 32 bit in DP (4 bytes)
            #                              0104|      CRC: EQU   $80
            0xCE, addr_hi, addr_lo, #      0104|           LDU   #....      ; start address in u
            0x34, 0x10, #                  010C|           PSHS  x          ; end address +1 to TOS
            0xCC, 0xFF, 0xFF, #            010E|           LDD   #CRCINITL
            0xDD, 0x82, #                  0111|           STD   crc+2
            0x8E, 0xFF, 0xFF, #            0113|           LDX   #CRCINITH
            0x9F, 0x80, #                  0116|           STX   crc
            #                              0118|                            ; d/x contains the CRC
            #                              0118|       BL:
            0xE8, 0xC0, #                  0118|           EORB  ,u+        ; XOR with lowest byte
            0x10, 0x8E, 0x00, 0x08, #      011A|           LDY   #8         ; bit counter
            #                              011E|       RL:
            0x1E, 0x01, #                  011E|           EXG   d,x
            #                              0120|      RL1:
            0x44, #                        0120|           LSRA             ; shift CRC right, beginning with high word
            0x56, #                        0121|           RORB
            0x1E, 0x01, #                  0122|           EXG   d,x
            0x46, #                        0124|           RORA             ; low word
            0x56, #                        0125|           RORB
            0x24, 0x12, #                  0126|           BCC   cl
            #                              0128|                            ; CRC=CRC XOR polynomic
            0x88, 0x83, #                  0128|           EORA  #CRCLH     ; apply CRC polynomic low word
            0xC8, 0x20, #                  012A|           EORB  #CRCLL
            0x1E, 0x01, #                  012C|           EXG   d,x
            0x88, 0xED, #                  012E|           EORA  #CRCHH     ; apply CRC polynomic high word
            0xC8, 0xB8, #                  0130|           EORB  #CRCHL
            0x31, 0x3F, #                  0132|           LEAY  -1,y       ; bit count down
            0x26, 0xEA, #                  0134|           BNE   rl1
            0x1E, 0x01, #                  0136|           EXG   d,x        ; CRC: restore correct order
            0x27, 0x04, #                  0138|           BEQ   el         ; leave bit loop
            #                              013A|       CL:
            0x31, 0x3F, #                  013A|           LEAY  -1,y       ; bit count down
            0x26, 0xE0, #                  013C|           BNE   rl         ; bit loop
            #                              013E|       EL:
            0x11, 0xA3, 0xE4, #            013E|           CMPU  ,s         ; end address reached?
            0x26, 0xD5, #                  0141|           BNE   bl         ; byte loop
            0xDD, 0x82, #                  0143|           STD   crc+2      ; CRC low word
            0x9F, 0x80, #                  0145|           STX   crc        ; CRC high word
        ]))
        d = self.cpu.accu_d.value
        x = self.cpu.index_x.value
        crc32 = x * 0x10000 + d
        return crc32 ^ 0xFFFFFFFF

    def compare_crc32(self, data):

        if sys.version_info > (3,):
            data = bytes(data, encoding="ASCII")

        print("Compare CRC32 with: %r" % data)

        print("\nCreate CRC32 with binascii:")
        start_time = time.time()
        excpected_crc32 = binascii.crc32(data) & 0xffffffff
        duration = time.time() - start_time
        print("\tbinascii crc32..: $%X calculated in %.6fsec" % (excpected_crc32, duration))

        print("\nCreate CRC32 with Emulated 6809 CPU:")
        start_time = time.time()
        crc32_value = self.crc32(data)
        duration = time.time() - start_time
        print("\tMC6809 crc32..: $%X calculated in %.2fsec" % (crc32_value, duration))
        print()
        if crc32_value==excpected_crc32:
            print(" *** CRC32 values from 6809 and binascii are the same, ok.\n")
            return True
        else:
            print(" *** ERROR: CRC32 are different!\n")
            return False


def run_example():
    mc6809 = MC6809Example()

    data = string.digits + string.ascii_letters + string.punctuation
    ok = mc6809.compare_crc32(data)

    return ok # Used in unittests ;)


if __name__ == '__main__':
    run_example()
