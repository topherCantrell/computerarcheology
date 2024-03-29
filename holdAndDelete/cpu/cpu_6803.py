OPCODES = [
    {"mnem": "NOP",          "code": "01",     "bus": ""},
    {"mnem": "LSRD",         "code": "04",     "bus": ""},
    {"mnem": "TAP",          "code": "06",     "bus": ""},
    {"mnem": "TPA",          "code": "07",     "bus": ""},
    {"mnem": "INX",          "code": "08",     "bus": ""},
    {"mnem": "DEX",          "code": "09",     "bus": ""},
    {"mnem": "CLV",          "code": "0A",     "bus": ""},
    {"mnem": "SEV",          "code": "0B",     "bus": ""},
    {"mnem": "CLC",          "code": "0C",     "bus": ""},
    {"mnem": "SEC",          "code": "0D",     "bus": ""},
    {"mnem": "CLI",          "code": "0E",     "bus": ""},
    {"mnem": "SEI",          "code": "0F",     "bus": ""},
    {"mnem": "SBA",          "code": "10",     "bus": ""},
    {"mnem": "CBA",          "code": "11",     "bus": ""},
    {"mnem": "TAB",          "code": "16",     "bus": ""},
    {"mnem": "TBA",          "code": "17",     "bus": ""},
    {"mnem": "DAA",          "code": "19",     "bus": ""},
    {"mnem": "ABA",          "code": "1B",     "bus": ""},
    {"mnem": "BRA r",        "code": "20rr",   "bus": "x"},
    {"mnem": "BRN r",        "code": "21rr",   "bus": "x"},
    {"mnem": "BHI r",        "code": "22rr",   "bus": "x"},
    {"mnem": "BLS r",        "code": "23rr",   "bus": "x"},
    {"mnem": "BCC r",        "code": "24rr",   "bus": "x"},
    {"mnem": "BHS r",        "code": "24rr",   "bus": "x"},
    {"mnem": "BCC r",        "code": "24rr",   "bus": "x"},
    {"mnem": "BLO r",        "code": "25rr",   "bus": "x"},
    {"mnem": "BNE r",        "code": "26rr",   "bus": "x"},
    {"mnem": "BEQ r",        "code": "27rr",   "bus": "x"},
    {"mnem": "BVC r",        "code": "28rr",   "bus": "x"},
    {"mnem": "BVS r",        "code": "29rr",   "bus": "x"},
    {"mnem": "BPL r",        "code": "2Arr",   "bus": "x"},
    {"mnem": "BMI r",        "code": "2Brr",   "bus": "x"},
    {"mnem": "BGE r",        "code": "2Crr",   "bus": "x"},
    {"mnem": "BLT r",        "code": "2Drr",   "bus": "x"},
    {"mnem": "BGT r",        "code": "2Err",   "bus": "x"},
    {"mnem": "BLE r",        "code": "2Frr",   "bus": "x"},
    {"mnem": "TSX",          "code": "30",     "bus": ""},
    {"mnem": "INS",          "code": "31",     "bus": ""},
    {"mnem": "PULA",         "code": "32",     "bus": ""},
    {"mnem": "PULB",         "code": "33",     "bus": ""},
    {"mnem": "DES",          "code": "34",     "bus": ""},
    {"mnem": "TXS",          "code": "35",     "bus": ""},
    {"mnem": "PSHA",         "code": "36",     "bus": ""},
    {"mnem": "PSHB",         "code": "37",     "bus": ""},
    {"mnem": "PULX",         "code": "38",     "bus": ""},
    {"mnem": "RTS",          "code": "39",     "bus": ""},
    {"mnem": "ABX",          "code": "3A",     "bus": ""},
    {"mnem": "RTI",          "code": "3B",     "bus": ""},
    {"mnem": "PSHX",         "code": "3C",     "bus": ""},
    {"mnem": "MUL",          "code": "3D",     "bus": ""},
    {"mnem": "WAI",          "code": "3E",     "bus": ""},
    {"mnem": "SWI",          "code": "3F",     "bus": ""},
    {"mnem": "NEGA",         "code": "40",     "bus": ""},
    {"mnem": "COMA",         "code": "43",     "bus": ""},
    {"mnem": "LSRA",         "code": "44",     "bus": ""},
    {"mnem": "RORA",         "code": "46",     "bus": ""},
    {"mnem": "ASRA",         "code": "47",     "bus": ""},
    {"mnem": "LSLA",         "code": "48",     "bus": ""},
    {"mnem": "ASLA",         "code": "48",     "bus": ""},
    {"mnem": "ROLA",         "code": "49",     "bus": ""},
    {"mnem": "DECA",         "code": "4A",     "bus": ""},
    {"mnem": "INCA",         "code": "4C",     "bus": ""},
    {"mnem": "TSTA",         "code": "4D",     "bus": ""},
    {"mnem": "CLRA",         "code": "4F",     "bus": ""},
    {"mnem": "NEGB",         "code": "50",     "bus": ""},
    {"mnem": "COMB",         "code": "53",     "bus": ""},
    {"mnem": "LSRB",         "code": "54",     "bus": ""},
    {"mnem": "RORB",         "code": "56",     "bus": ""},
    {"mnem": "ASRB",         "code": "57",     "bus": ""},
    {"mnem": "LSLB",         "code": "58",     "bus": ""},
    {"mnem": "ASLB",         "code": "58",     "bus": ""},
    {"mnem": "ROLB",         "code": "59",     "bus": ""},
    {"mnem": "DECB",         "code": "5A",     "bus": ""},
    {"mnem": "INCB",         "code": "5C",     "bus": ""},
    {"mnem": "TSTB",         "code": "5D",     "bus": ""},
    {"mnem": "CLRB",         "code": "5F",     "bus": ""},
    {"mnem": "NEG i,X",      "code": "60ii",   "bus": ""},
    {"mnem": "COM i,X",      "code": "63ii",   "bus": ""},
    {"mnem": "LSR i,X",      "code": "64ii",   "bus": ""},
    {"mnem": "ROR i,X",      "code": "66ii",   "bus": ""},
    {"mnem": "ASR i,X",      "code": "67ii",   "bus": ""},
    {"mnem": "ASL i,X",      "code": "68ii",   "bus": ""},
    {"mnem": "LSL i,X",      "code": "68ii",   "bus": ""},
    {"mnem": "ROL i,X",      "code": "69ii",   "bus": ""},
    {"mnem": "DEC i,X",      "code": "6Aii",   "bus": ""},
    {"mnem": "INC i,X",      "code": "6Cii",   "bus": ""},
    {"mnem": "TST i,X",      "code": "6Dii",   "bus": ""},
    {"mnem": "JMP i,X",      "code": "6Eii",   "bus": ""},
    {"mnem": "CLR i,X",      "code": "6Fii",   "bus": ""},
    {"mnem": "NEG t",        "code": "70tmtl", "bus": "rw"},
    {"mnem": "COM t",        "code": "73tmtl", "bus": "rw"},
    {"mnem": "LSR t",        "code": "74tmtl", "bus": "rw"},
    {"mnem": "ROR t",        "code": "76tmtl", "bus": "rw"},
    {"mnem": "ASR t",        "code": "77tmtl", "bus": "rw"},
    {"mnem": "ASL t",        "code": "78tmtl", "bus": "rw"},
    {"mnem": "LSL t",        "code": "78tmtl", "bus": "rw"},
    {"mnem": "ROL t",        "code": "79tmtl", "bus": "rw"},
    {"mnem": "DEC t",        "code": "7Atmtl", "bus": "rw"},
    {"mnem": "INC t",        "code": "7Ctmtl", "bus": "rw"},
    {"mnem": "TST t",        "code": "7Dtmtl", "bus": "r"},
    {"mnem": "JMP t",        "code": "7Etmtl", "bus": "x"},
    {"mnem": "CLR t",        "code": "7Ftmtl", "bus": "r"},
    {"mnem": "SUBA #b",      "code": "80bb",   "bus": ""},
    {"mnem": "CMPA #b",      "code": "81bb",   "bus": ""},
    {"mnem": "SBCA #b",      "code": "82bb",   "bus": ""},
    {"mnem": "SUBD #w",      "code": "83wmwl", "bus": ""},
    {"mnem": "ANDA #b",      "code": "84bb",   "bus": ""},
    {"mnem": "BITA #b",      "code": "85bb",   "bus": ""},
    {"mnem": "LDA #b",       "code": "86bb",   "bus": ""},
    {"mnem": "EORA #b",      "code": "88bb",   "bus": ""},
    {"mnem": "ADCA #b",      "code": "89bb",   "bus": ""},
    {"mnem": "ORA #b",       "code": "8Abb",   "bus": ""},
    {"mnem": "ADDA #b",      "code": "8Bbb",   "bus": ""},
    {"mnem": "CPX #w",       "code": "8Cwmwl", "bus": ""},
    {"mnem": "BSR r",        "code": "8Drr",   "bus": "x"},
    {"mnem": "LDS #w",       "code": "8Ewmwl", "bus": ""},
    {"mnem": "SUBA p",      "code": "90pp",   "bus": "r"},
    {"mnem": "CMPA p",      "code": "91pp",   "bus": "r"},
    {"mnem": "SBCA p",      "code": "92pp",   "bus": "r"},
    {"mnem": "SUBD p",      "code": "93pp",   "bus": "r"},
    {"mnem": "ANDA p",      "code": "94pp",   "bus": "r"},
    {"mnem": "BITA p",      "code": "95pp",   "bus": "r"},
    {"mnem": "LDA p",       "code": "96pp",   "bus": "r"},
    {"mnem": "STA p",       "code": "97pp",   "bus": "w"},
    {"mnem": "EORA p",      "code": "98pp",   "bus": "r"},
    {"mnem": "ADCA p",      "code": "99pp",   "bus": "r"},
    {"mnem": "ORA p",       "code": "9App",   "bus": "r"},
    {"mnem": "ADDA p",      "code": "9Bpp",   "bus": "r"},
    {"mnem": "CPX p",       "code": "9Cpp",   "bus": "r"},
    {"mnem": "JSR p",       "code": "9Dpp",   "bus": "x"},
    {"mnem": "LDS p",       "code": "9Epp",   "bus": "r"},
    {"mnem": "STS p",       "code": "9Fpp",   "bus": "w"},
    {"mnem": "SUBA i,X",    "code": "A0ii",   "bus": ""},
    {"mnem": "CMPA i,X",    "code": "A1ii",   "bus": ""},
    {"mnem": "SBCA i,X",    "code": "A2ii",   "bus": ""},
    {"mnem": "SUBD i,X",    "code": "A3ii",   "bus": ""},
    {"mnem": "ANDA i,X",    "code": "A4ii",   "bus": ""},
    {"mnem": "BITA i,X",    "code": "A5ii",   "bus": ""},
    {"mnem": "LDA i,X",     "code": "A6ii",   "bus": ""},
    {"mnem": "STA i,X",     "code": "A7ii",   "bus": ""},
    {"mnem": "EORA i,X",    "code": "A8ii",   "bus": ""},
    {"mnem": "ADCA i,X",    "code": "A9ii",   "bus": ""},
    {"mnem": "ORA i,X",     "code": "AAii",   "bus": ""},
    {"mnem": "ADDA i,X",    "code": "ABii",   "bus": ""},
    {"mnem": "CPX i,X",     "code": "ACii",   "bus": ""},
    {"mnem": "JSR i,X",     "code": "ADii",   "bus": ""},
    {"mnem": "LDS i,X",     "code": "AEii",   "bus": ""},
    {"mnem": "STS i,X",     "code": "AFii",   "bus": ""},
    {"mnem": "SUBA t",      "code": "B0tmtl", "bus": "r"},
    {"mnem": "CMPA t",      "code": "B1tmtl", "bus": "r"},
    {"mnem": "SBCA t",      "code": "B2tmtl", "bus": "r"},
    {"mnem": "SUBD t",      "code": "B3tmtl", "bus": "r"},
    {"mnem": "ANDA t",      "code": "B4tmtl", "bus": "r"},
    {"mnem": "BITA t",      "code": "B5tmtl", "bus": "r"},
    {"mnem": "LDA t",       "code": "B6tmtl", "bus": "r"},
    {"mnem": "STA t",       "code": "B7tmtl", "bus": "w"},
    {"mnem": "EORA t",      "code": "B8tmtl", "bus": "r"},
    {"mnem": "ADCA t",      "code": "B9tmtl", "bus": "r"},
    {"mnem": "ORA t",       "code": "BAtmtl", "bus": "r"},
    {"mnem": "ADDA t",      "code": "BBtmtl", "bus": "r"},
    {"mnem": "CPX t",       "code": "BCtmtl", "bus": "r"},
    {"mnem": "JSR t",       "code": "BDtmtl", "bus": "x"},
    {"mnem": "LDS t",       "code": "BEtmtl", "bus": "r"},
    {"mnem": "STS t",       "code": "BFtmtl", "bus": "w"},
    {"mnem": "SUBB #b",     "code": "C0bb",   "bus": ""},
    {"mnem": "CMPB #b",     "code": "C1bb",   "bus": ""},
    {"mnem": "SBCB #b",     "code": "C2bb",   "bus": ""},
    {"mnem": "ADDD #w",     "code": "C3wmwl", "bus": ""},
    {"mnem": "ANDB #b",     "code": "C4bb",   "bus": ""},
    {"mnem": "BITB #b",     "code": "C5bb",   "bus": ""},
    {"mnem": "LDB #b",      "code": "C6bb",   "bus": ""},
    {"mnem": "EORB #b",     "code": "C8bb",   "bus": ""},
    {"mnem": "ADCB #b",     "code": "C9bb",   "bus": ""},
    {"mnem": "ORB #b",      "code": "CAbb",   "bus": ""},
    {"mnem": "ADDB #b",     "code": "CBbb",   "bus": ""},
    {"mnem": "LDD #w",      "code": "CCwmwl", "bus": ""},
    {"mnem": "LDX #w",      "code": "CEwmwl", "bus": ""},
    {"mnem": "SUBB p",      "code": "D0pp",   "bus": "r"},
    {"mnem": "CMPB p",      "code": "D1pp",   "bus": "r"},
    {"mnem": "SBCB p",      "code": "D2pp",   "bus": "r"},
    {"mnem": "ADDD p",      "code": "D3pp",   "bus": "r"},
    {"mnem": "ANDB p",      "code": "D4pp",   "bus": "r"},
    {"mnem": "BITB p",      "code": "D5pp",   "bus": "r"},
    {"mnem": "LDB p",       "code": "D6pp",   "bus": "r"},
    {"mnem": "STB p",       "code": "D7pp",   "bus": "w"},
    {"mnem": "EORB p",      "code": "D8pp",   "bus": "r"},
    {"mnem": "ADCB p",      "code": "D9pp",   "bus": "r"},
    {"mnem": "ORB p",       "code": "DApp",   "bus": "r"},
    {"mnem": "ADDB p",      "code": "DBpp",   "bus": "r"},
    {"mnem": "LDD p",       "code": "DCpp",   "bus": "r"},
    {"mnem": "STD p",       "code": "DDpp",   "bus": "w"},
    {"mnem": "LDX p",       "code": "DEpp",   "bus": "r"},
    {"mnem": "STX p",       "code": "DFpp",   "bus": "r"},
    {"mnem": "SUBB i,X",    "code": "E0ii",   "bus": ""},
    {"mnem": "CMPB i,X",    "code": "E1ii",   "bus": ""},
    {"mnem": "SBCB i,X",    "code": "E2ii",   "bus": ""},
    {"mnem": "ADDD i,X",    "code": "E3ii",   "bus": ""},
    {"mnem": "ANDB i,X",    "code": "E4ii",   "bus": ""},
    {"mnem": "BITB i,X",    "code": "E5ii",   "bus": ""},
    {"mnem": "LDB i,X",     "code": "E6ii",   "bus": ""},
    {"mnem": "STB i,X",     "code": "E7ii",   "bus": ""},
    {"mnem": "EORB i,X",    "code": "E8ii",   "bus": ""},
    {"mnem": "ADCB i,X",    "code": "E9ii",   "bus": ""},
    {"mnem": "ORB i,X",     "code": "EAii",   "bus": ""},
    {"mnem": "ADDB i,X",    "code": "EBii",   "bus": ""},
    {"mnem": "LDD i,X",     "code": "ECii",   "bus": ""},
    {"mnem": "STD i,X",     "code": "EDpp",   "bus": ""},
    {"mnem": "LDX i,X",     "code": "EEii",   "bus": ""},
    {"mnem": "STX i,X",     "code": "EFii",   "bus": ""},
    {"mnem": "SUBB t",      "code": "F0tmtl", "bus": "r"},
    {"mnem": "CMPB t",      "code": "F1tmtl", "bus": "r"},
    {"mnem": "SBCB t",      "code": "F2tmtl", "bus": "r"},
    {"mnem": "ADDD t",      "code": "F3tmtl", "bus": "r"},
    {"mnem": "ANDB t",      "code": "F4tmtl", "bus": "r"},
    {"mnem": "BITB t",      "code": "F5tmtl", "bus": "r"},
    {"mnem": "LDB t",       "code": "F6tmtl", "bus": "r"},
    {"mnem": "STB t",       "code": "F7tmtl", "bus": "w"},
    {"mnem": "EORB t",      "code": "F8tmtl", "bus": "r"},
    {"mnem": "ADCB t",      "code": "F9tmtl", "bus": "r"},
    {"mnem": "ORB t",       "code": "FAtmtl", "bus": "r"},
    {"mnem": "ADDB t",      "code": "FBtmtl", "bus": "r"},
    {"mnem": "LDD t",       "code": "FCtmtl", "bus": "r"},
    {"mnem": "STD t",       "code": "FDtmtl", "bus": "w"},
    {"mnem": "LDX t",       "code": "FEtmtl", "bus": "r"},
    {"mnem": "STX t",       "code": "FFtmtl", "bus": "w"}
]

import cpu.cpu_common


class CPU_6803(cpu.cpu_common.CPU):

    def __init__(self):
        super().__init__(OPCODES)


SINGLETON = CPU_6803()


def get_cpu():
    return SINGLETON
