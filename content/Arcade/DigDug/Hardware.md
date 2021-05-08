![Dig Dug](digdug.jpg)

# DigDug Hardware

>>> memory

|    |     |     |
| -------- | ------- | ----------------- |


```
0x0000-0x3FFF 16384	ROM, Write NOP	(/* the only area different for each CPU */)
0x6800-0x681F	32	Device Write	namco, namco_device, pacman_sound_w
0x6820-0x6827	8	Write	bosco_latch_w (/* misc latches */)
0x6830	1	      Device Write	watchdog, watchdog_timer_device, reset_w
0x7000-0x70FF	256	Device Read/Write	06xx, namco_06xx_device, data_r, data_w
0x7100	1	Device Read/Write	06xx, namco_06xx_device, ctrl_r, ctrl_w
0x8000-0x83FF	1024	RAM Write, Shared	digdug_videoram_w, videoram (/* tilemap RAM (bottom half of RAM 0 */)
0x8400-0x87FF	1024	RAM, Shared	share1 (/* work RAM (top half for RAM 0 */)
0x8800-0x8BFF	1024	RAM, Shared	digdug_objram (/* work RAM + sprite registers */)
0x9000-0x93FF	1024	RAM, Shared	digdug_posram (/* work RAM + sprite registers */)
0x9800-0x9BFF	1024	RAM, Shared	digdug_flpram (/* work RAM + sprite registers */)
0xA000-0xA007	8	Read NOP, Write	digdug_PORT_w (/* video latches (spurious reads when setting latch bits) */)
0xB800-0xB83F	64	Device Read/Write	earom, atari_vg_earom_device, read, write (/* non volatile memory data */)
0xB840	1	Device Write	earom, atari_vg_earom_device, ctrl_w (/* non volatile memory control */)
```