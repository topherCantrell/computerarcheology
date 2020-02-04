; On the web: [http://www.alienbill.com/2600/101/docs/stella.html Stella Programmer's Guide]

; The address decoding for the 2600 is very simple. The TIA is accessed
; if A12 is 0 and A7 is 0. The TIA is selected if (address&1080 == 0000).
;
; The TIA chip uses the 6 lower address lines A0-A5. The reads seem to 
; ignore A4 and A5.
;
; The addresses have different read/write definitions and many of them
; are strobes that are triggered by writing any value.
;
; Note that the 6502 has an 8-bit stack pointer. The CPU automatically sets the upper
; byte of the address to 01. The RIOT chip RAM ghosts from 00xx to 01xx putting the stack
; in RAM.

; TIA

; Reads
.CXM0P    = 0x0000 ; Collisions M0/P1
.CXM1P    = 0x0001 ; Collisions M1/P0
.CXP0FB   = 0x0002 ; Collisions M0/PF
.CXP1FB   = 0x0003 ; Collisions P1/PF
.CXM0FB   = 0x0004 ; Collisions M0/PF
.CXM1FB   = 0x0005 ; Collisions M1/PF
.CXBLPF   = 0x0006 ; Collisions BL/PF
.CXPPMM   = 0x0007 ; Collisions P0/P1
.INPT0    = 0x0008 ; Paddle input 0
.INPT1    = 0x0009 ; Paddle input 1
.INPT2    = 0x000A ; Paddle input 2
.INPT3    = 0x000B ; Paddle input 3
.INPT4    = 0x000C ; Latched inputs (joystick buttons)
.INPT5    = 0x000D ; Latched inputs (joystick buttons)

; Writes
.VSYNC    = 0x0000 ; D1=1 starts the vertical sync
.VBLANK   = 0x0001 ; D1=1 starts the vertical blank (D6 and D7 config INPT0-5)
.WSYNC    = 0x0002 ; Halts processor until leading edge of horizontal blank
.RSYNC    = 0x0003 ; Resets sync counter (used in chip testing)
.NUSIZ0   = 0x0004 ; Number and size of player/missile P0
.NUSIZ1   = 0x0005 ; Number and size of player/missile P0
.COLUP0   = 0x0006 ; Color-luminance of player 0
.COLUP1   = 0x0007 ; Color-luminance of player 1
.COLUPF   = 0x0008 ; Color-luminance of play filed
.COLUBK   = 0x0009 ; Color-luminance of background
.CTRLPF   = 0x000A ; Control playfield, priorities, and ball size
.REFP0    = 0x000B ; D3=1 reflects player 0
.PEFP1    = 0x000C ; D3=1 reflects player 1
.PF0      = 0x000D ; Playfield 0 bits (upper 4 bits)
.PF1      = 0x000E ; Playfield 1 bits
.PF2      = 0x000F ; Playfield 2 bits
.RESP0    = 0x0010 ; Set horizontal position of player 0
.RESP1    = 0x0011 ; Set horizontal position of player 1
.RESM0    = 0x0012 ; Set horizontal position of missile 0
.RESM1    = 0x0013 ; Set horizontal position of missile 1
.RESBL    = 0x0014 ; Set horizontal position of ball
.AUDC0    = 0x0015 ; Noise, tone, division control channel 0
.AUDC1    = 0x0016 ; Noise, tone, division control channel 1
.AUDF0    = 0x0017 ; Frequency divider channel 0
.AUDF1    = 0x0018 ; Frequency divider channel 1
.AUDV0    = 0x0019 ; Volume channel 0
.AUDV1    = 0x001A ; Volume channel 1
.GRP0     = 0x001B ; Player 0 graphics
.GRP1     = 0x001C ; Player 1 graphics
.ENAM0    = 0x001D ; D1=1 to enable missile 0
.ENAM1    = 0x001E ; D1=1 to enable missile 1
.ENABL    = 0x001F ; D1=1 to enable ball
.HMP0     = 0x0020 ; Horizontal motion offset for player 0
.HMP1     = 0x0021 ; Horizontal motion offset for player 1
.HMM0     = 0x0022 ; Horizontal motion offset for missile 0
.HMM1     = 0x0023 ; Horizontal motion offset for missile 1
.HMBL     = 0x0024 ; Horizontal motion offset for ball
.VDELP0   = 0x0025 ; D0=1 to delay player 0 one vertical line
.VDELP1   = 0x0026 ; D0=1 to delay player 1 one vertical line
.VDELBL   = 0x0027 ; D0=1 to delay ball one vertical line
.RESMP0   = 0x0028 ; D1=1 to reset missile 0 to player 0
.RESMP1   = 0x0029 ; D1=1 to reset missile 1 to player 1
.HMOVE    = 0x002A ;  Executes horizontal motions
.HMCLR    = 0x002B ; Clears all horizonal motion registers
.CXCLR    = 0x002C ; Clears all collision registers

; PIA

; The PIA (R.I.O.T.) is accessed if A12 is 0 and A7 is 1. If A9 is 0 then the 128 bytes 
; of RAM are selected. If A9 is 1 then the PIA timer registers are selected.
;
; The TIA REGS are selected if (address&1280 == 0280).
;
; The TIA RAM is selected if (address&1280 == 0080).
;
; The PIA chip uses the lower 7 address lines A0-A6. Thus the 007F mask below.

.SWCHA    = 0x0280 ; Port A Hand controllers
.SWACNT   = 0x0281 ; Port A DDR

.SWCHB    = 0x0282 ; Port B Console switches
; D7 : P1 difficulty (0=amateur, 1=pro)
; D6 : P0 difficulty (0=amateur, 1=pro)
; D5 : not used
; D4 : not used
; D3 : color or B/W (0=B/W, 1=color)
; D2 : not used
; D1 : game select (0=pressed)
; D0 : game reset (0=pressed)

.SWBCNT   = 0x0283 ; Port B DDR
.INTIM    = 0x0284 ; Timer output (read only)
.TIM1T    = 0x0294 ; Set 1 clock interval (write only)
.TIM8T    = 0x0295 ; Set 8 clock interval (write only)
.TIM64T   = 0x0296 ; Set 64 clock interval (write only)
.TIM1024T = 0x0297 ; Set 1024 clock interval (write only)
