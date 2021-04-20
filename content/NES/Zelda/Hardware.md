![Hardware](Zelda.jpg)

# Hardware

# Registers 

>>>memory

| | | | |
| --- | --- | --- | --- |
| 2000  |    P_CNTRL_1     |            | n+sbiaa |
| 2001  |    P_CNTRL_2     |            | |
| 2002  |    P_STATUS      |            | |
| 2003  |    P_SPR_ADDR    |            | destination address for port 2004 and 4014 (incremented with write ... not read) |
| 2004  |    P_SPR_DATA    |            | read/write data |
| 2005  |    P_BKG_SCROLL  |            | |
| 2006  |    P_VRAM_ADDR   |            | |
| 2007  |    P_VRAM_DATA   |            | |
| 4000  | S_SQR1_A     |             | tt_c_d_vvvv t=duty type, c=decay_looping/length, d=decay disable, v=volume/decay_rate |
| 4001  | S_SQR1_B     |             | e_rrr_o_sss e=sweep enable, r=sweep rate, o=decrease/increase, s=right shift amount |
| 4002  | S_SQR1_C     |             | wwwwwwww LSB of wavelength |
| 4003  | S_SQR1_D     |             | nnnnn_xxx n=length counter reload, x=MSB of wavelength |
| 4004  |    S_SQR2_A     |             | tt_c_d_vvvv t=duty type, c=decay_looping/length, d=decay disable, v=volume/decay_rate |
| 4005  |    S_SQR2_B     |             | e_rrr_o_sss e=sweep enable, r=sweep rate, o=decrease/increase, s=right shift amount |
| 4006  |    S_SQR2_C     |             | wwwwwwww LSB of wavelength |
| 4007  |    S_SQR2_D     |             | nnnnn_xxx n=length counter reload, x=MSB of wavelength |
| 4008  |    S_TRI_A      |             | c_aaaaaaa c=linear counter start, a=linear counter load |
| 4009  |    S_TRI_B      |             |  ++++++++ unused |
| 400A  |    S_TRI_C      |             | wwwwwwww LSB of wavelength |
| 400B  |    S_TRI_D      |             | nnnnn_xxx n=length counter reload, x=MSB of wavelength |
| 400C  |    S_NOI_A      |             | ++_c_d_vvvv c=decay_looping/length, d=decay disable, v=volume/decay_rate |
| 400D  |    S_NOI_B      |             | ++++++++ unused |
| 400E  |    S_NOI_C      |             | g_+++_pppp g=random generation type, p=playback rate |
| 400F  |    S_NOI_D      |             | nnnnn_xxx n=length counter reload, x=MSB of wavelength |
| 4010  |    S_DMC_A      |             | mm_++_ffff m=mode, f=frequency |
| 4011  |    S_DMC_B      |             | +_vvvvvv_d v=load value of delta counter, d=LSB of DAC |
| 4012  |    S_DMC_C      |             | aaaaaaaa DMA start address (shl 6) |
| 4013  |    S_DMC_D      |             |  cccccccc Length of DMA data (shl 4) |
| 4014  |    P_SPR_DMA    |             | |
| 4015  |    S_Status     |             | i_q_+_d_ntba i=IRQ(ro) status,q=DMC status, d=DMC, ntba=noise/triangle/square2/square1 |
| 4016  | 4016 | | |
| 4017  |    S_FrameCntr   |            | d_s_++++++ d=divider rate, s=frame counter status |

# Mapper 1: MMC1

>>>memory

| | | |
| --- | --- | --- |
| 8000:9FFFw | MMC1_0 | |
| A000:BFFFw | MMC1_1 | |
| C000:EFFFw | MMC1_2 | |
| E000:FFFFw | MMC1_3 | |

 The Legend of Zelda uses the MMC1 chip to map the RAM/ROM banks for the CPU and PPU.
 MMC1 is controlled by writing to 8000-FFFF (assumes that this area is ROM where
 writes have no effect). There are 4 5-bit registers in the MMC1. Writing to 8000-9FFF
 sends data to register 0. A000-BFFF writes to register 1, C000-DFFF to register 2, and 
 E000-FFFF to register 3.

 The MMC1 register data is shifted in with 5 consecutive writes. Bit 0 of the written value
 goes to bit-0 on the first write then bit-1 on the second. After 5 the bit-pointer goes
 back to bit-0. If bit 7 of the written value is 1 then the 5-bit register is cleared and
 the pointer goes back to bit-0 for the NEXT write.
