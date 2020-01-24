; Special Function Registers

.P0 = $80  ; 11111111 (value after reset)
.SP = $81  ; 00000111
;| 82  | DP0L   | 00000000 |
;| 83  | DP0H   | 00000000 |
;| 84  | DP1L   | 00000000 |
;| 85  | DP1H   | 00000000 |
;| 87  | PCON   | 0xxx0000 |
;| 88  | TCON   | 00000000 |
;| 89  | TMOD   | 00000000 |
;| 8A  | TL0    | 00000000 |
;| 8B  | TL1    | 00000000 |
;| 8C  | TH0    | 00000000 |
;| 8D  | TH1    | 00000000 |
;| 8E  | AUXR   | xxx00xx0 Auxiliary Register |
.P1 = $90  ; 11111111
;| 98  | SCON   | 00000000 |
;| 99  | SBUF   | xxxxxxxx |
;| A0  | P2     | 11111111 |
;| A2  | AUXR1  | xxxxxxx0 Auxiliary Regsister 1 |
;| A6  | WDTRST | xxxxxxxx |
;| A8  | IE     | 0x000000 |
;| B0  | P3     | 11111111 |
;| B8  | IP     | xx000000 |
;| C8  | T2CON  | 00000000 Timer/Counter 2 Control Register |
;| C9  | T2MOD  | xxxxxx00 |
;| CA  | RCAP2L | 00000000 |
;| CB  | RCAP2H | 00000000 |
;| CC  | TL2    | 00000000 |
;| CD  | TH2    | 00000000 |
;| D0  | PSW    | 00000000 |
;| E0  | ACC    | 00000000 |
;| F0  | B      | 00000000 |

; Bit Addressing
;  - 00 – 7FH are assigned to RAM locations of 20 – 2FH.
;  - 80 – 87H are assigned to the PO port.
;  - 88 – 8FH are assigned to the TCON register.
;  - 90 – 97H are assigned to the P1 port.
;  - 98 – 9FH are assigned to the SCON register.
;  - AO – A7H are assigned to the P2 port.
;  - A8 – AFH are assigned to the IE register.
;  - BO – B7H are assigned to the P3 port.
;  - B8 – BFH are assigned to IP.
;  - CO – CFH (not assigned)
;  - DO – D7H are assigned to the PSW register.
;  - D8 – DFH (not assigned)
;  - EO – E7H are assigned to the Accumulator register.
;  - E8 – EFH (not assigned)
;  - FO – F7H are assigned to the B register.

.P0.0 = (bit)$80
.P0.1 = (bit)$81
;| 82b | P0.2   | |
;| 83b | P0.3   | |
;| 84b | P0.4   | |
;| 85b | P0.5   | |
;| 86b | P0.6   | |
;| 87b | P0.7   | |
;| 88b | TCON.0 | |
;| 89b | TCON.1 | |
;| 8Ab | TCON.2 | |
;| 8Bb | TCON.3 | |
;| 8Cb | TCON.4 | |
;| 8Db | TCON.5 | |
;| 8Eb | TCON.6 | |
;| 8Fb | TCON.7 | |
;| 90b | P1.0   | |
;| 91b | P1.1   | |
;| 92b | P1.2   | |
;| 93b | P1.3   | |
;| 94b | P1.4   | |
;| 95b | P1.5   | |
;| 96b | P1.6   | |
;| 97b | P1.7   | |
;| 98b | SCON.0 | |
;| 99b | SCON.1 | |
;| 9Ab | SCON.2 | |
;| 9Bb | SCON.3 | |
;| 9Cb | SCON.4 | |
;| 9Db | SCON.5 | |
;| 9Eb | SCON.6 | |
;| 9Fb | SCON.7 | |
;| A0b | P2.0   | |
;| A1b | P2.1   | |
;| A2b | P2.2   | |
;| A3b | P2.3   | |
;| A4b | P2.4   | |
;| A5b | P2.5   | |
;| A6b | P2.6   | |
;| A7b | P2.7   | |
;| A8b | IE.0   | |
;| A9b | IE.1   | |
;| AAb | IE.2   | |
;| ABb | IE.3   | |
;| ACb | IE.4   | |
;| ADb | IE.5   | |
;| AEb | IE.6   | |
;| AFb | IE.7   | |
;| B0b | P3.0   | |
;| B1b | P3.1   | |
;| B2b | P3.2   | |
;| B3b | P3.3   | |
;| B4b | P3.4   | |
;| B5b | P3.5   | |
;| B6b | P3.6   | |
;| B7b | P3.7   | |
;| B8b | IP.0   | |
;| B9b | IP.1   | |
;| BAb | IP.2   | |
;| BBb | IP.3   | |
;| BCb | IP.4   | |
;| BDb | IP.5   | |
;| BEb | IP.6   | |
;| BFb | IP.7   | |
;| D0b | PSW.0  | |
;| D1b | PSW.1  | |
;| D2b | PSW.2  | |
;| D3b | PSW.3  | |
;| D4b | PSW.4  | |
;| D5b | PSW.5  | |
;| D6b | PSW.6  | |
;| D7b | PSW.7  | |
;| E0b | ACC.0  | |
;| E1b | ACC.1  | |
;| E2b | ACC.2  | |
;| E3b | ACC.3  | |
;| E4b | ACC.4  | |
;| E5b | ACC.5  | |
;| E6b | ACC.6  | |
;| E7b | ACC.7  | |
;| F0b | B.0    | |
;| F1b | B.1    | |
;| F2b | B.2    | |
;| F3b | B.3    | |
;| F4b | B.4    | |
;| F5b | B.5    | |
;| F6b | B.6    | |
;| F7b | B.7    | |
