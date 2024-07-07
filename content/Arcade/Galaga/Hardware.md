
```
https://github.com/MisterTea/MAMEHub/blob/master/Sources/Emulator/src/mame/video/galaga.c

http://www.arcaderestoration.com/memorymap/3291/Galaga.aspx

https://github.com/MisterTea/MAMEHub/blob/master/Sources/Emulator/src/mame/drivers/galaga.c
```

```
Sprite Memory:

; RAM 1
00: -TTTTTTT     7-bit tile number (upper bit ignored)
01: --CCCCCC     Color (upper two bits ignored)

        static const int gfx_offs[2][2] =
		{
			{ 0, 1 },
			{ 2, 3 }
		};
		int sprite = spriteram[offs] & 0x7f;
		int color = spriteram[offs+1] & 0x3f;
		int sx = spriteram_2[offs+1] - 40 + 0x100*(spriteram_3[offs+1] & 3);
		int sy = 256 - spriteram_2[offs] + 1;   // sprites are buffered and delayed by one scanline
		int flipx = (spriteram_3[offs] & 0x01);
		int flipy = (spriteram_3[offs] & 0x02) >> 1;
		int sizex = (spriteram_3[offs] & 0x04) >> 2;
		int sizey = (spriteram_3[offs] & 0x08) >> 3;

```