![Frogger Graphics ROM](Frogger.jpg)

# Frogger Graphics ROM

Tiles are 8x8 pixels. Each pixel is 2-bits (4 colors) chosen from a palette.

One pixel bit comes from 0000-07FF. The other pixel bit comes from 0800-0FFF. Thus a tile
is defined by 16 bytes of data ... 8 bytes from each ROM bank.

The monitor is rotated 90 degrees clockwise in the cabinet. The images shown here have been rotated
to match the monitor.

The D1 and D0 data lines are swapped on the second ROM bank (0800-0FFF). The values shown here
are after the swap as the system would see them.

```html
<script src="Frogger.js"></script>
<script src="/js/TileEngine.js"></script>
<script src="/js/BinaryData.js"></script>
<script src="/js/CANVAS.js"></script>
<!-- Cache some commonly-used values -->
<canvas width="0" height="0"
        data-canvasFunction="TileEngine.handleTileCanvas"
        data-labelColor=""
        data-pixWidth="8"
        data-gridX="8"
        data-gridY="8"
        data-pixHeight="8"
        data-gap="0.25"
        data-gridPad="1"
        data-colorsName="UNUSED"
        data-colors='["#808080","#0000C0","#00C000","#C00000"]'>        
</canvas>
<canvas width="0" height="0"
       data-colorsName="CS0"
       data-colors='["#808080","#000080","#008000","#800000"]'>
</canvas>
```

# Text 

```html
 <canvas width="650" height="330"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#202020","#202020","#C00000"]'
         data-command=":10x5:0,1,2,3,4,5,6,7,8,9,A,B,10,11,12,13,14,15,16,17,
                       18,19,1A,1B,1C,1D,1E,1F,20,21,22,23,24,25,26,27,28,29,
                       2A,2B,4E,4F,,,,,,,,">
 </canvas>
```

# Lives and Level 

```html
 <canvas width="265" height="65"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#21DE00","#EA0FE2","#FFFE00"]'
         data-command=":2x1:4C,4D">
 </canvas>
```

# Time 

```html
 <canvas width="265" height="65"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#21DE00","#EA0FE2","#FFFE00"]'
         data-command=":4x1:C,D,E,F">
 </canvas>
```

# Bonus scores 

```html
 <canvas width="330" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#21DE00","#EA0FE2","#FFFE00"]'
         data-command=":5x2:62,60,,66,64,63,61,,67,65">
 </canvas>
```

# Fly (Bonus score) 

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#1DC300","#E03E00","#00C3D9"]'
         data-command=":2x2:2E,2C,2F,2D">
 </canvas>
```

# Car 1 

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#FFFE00","#FF0000","#9200FA"]'
         data-command=":2x2:52,50,53,51">
 </canvas>
```

# Car 2 

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#05DBF9","#B9DB4E","#FF42F6"]'
         data-command=":2x2:32,30,33,31">
 </canvas>
```

# Car 3 

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#DFDDF7","#FF0000","#22DC05"]'
         data-command=":2x2:A2,A0,A3,A1">
 </canvas>
```

# Dozer 

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#DFDDF7","#FF0000","#22DC05"]'
         data-command=":2x2:A6,A4,A7,A5">
 </canvas>
```

# Truck 

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
        data-colors='["#808080","#DFDDF7","#FF0000","#22DC05"]'
         data-command=":2x2:AA,A8,AB,A9">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#DFDDF7","#FF0000","#22DC05"]'
         data-command=":2x2:AE,AC,AF,AD">
 </canvas>
```

# Base (at top) 
```html
 <canvas width="330" height="200"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#24DE02","#FE4403","#202020"]'
         data-command=":5x3:43,40,47,44,43,,41,47,45,,,42,43,46,">
 </canvas>
```

# Grass 

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#2C00E4","#9500F6","#E40440"]'
         data-command=":2x2:4A,48,4B,49">
 </canvas>
```

# Logs 

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#E7DCE9","#E0694D","#966B4C"]'
         data-command=":2x2:56,54,57,55">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"         
         data-command=":2x2:5A,58,5B,59">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:5E,5C,5F,5D">
 </canvas>
```

# Frog at home 

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#24DE02","#FE4403","#00C3DE"]'
         data-command=":2x2:6E,6C,6F,6D">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:FE,FC,FF,FD">
 </canvas>
```

# Player frog 
```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#21DE00","#EA0FE2","#FFFE00"]'
         data-command=":2x2:72,70,73,71">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:76,74,77,75">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:7A,78,7B,79">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:7E,7C,7F,7D">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:82,80,83,81">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:86,84,87,85">
 </canvas>
```

# Sinking (turtles and player) 

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#C6C6DB","#202020","#1DC300"]'
         data-command=":2x2:8A,88,8B,89">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:8E,8C,8F,8D">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:92,90,93,91">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:96,94,97,95">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:9A,98,9B,99">
 </canvas>
```

# Turtles 

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#C3C3D9","#E00000","#1DC300"]'
         data-command=":2x2:36,38,37,35">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#C3C3D9","#E00000","#1DC300"]'
         data-command=":2x2:3A,3C,3B,39">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#C3C3D9","#E00000","#1DC300"]'
         data-command=":2x2:3E,3C,3F,3D">
 </canvas>
```

# Otter 

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#E7DCE9","#E0694D","#966B4C"]'
         data-command=":2x2:9E,9C,9F,9D">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:E2,E0,E3,E1">
 </canvas>
```

# Snake 

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#28E6B3","#97FF00","#F346F0"]'
         data-command=":2x2:B2,B0,B3,B1">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:B6,B4,B7,B5">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:BA,B8,BB,B9">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:BE,BC,BF,BD">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:C2,C0,C3,C1">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:C6,C4,C7,C5">
 </canvas>
```

# Alligator 

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#E7DCE9","#E0694D","#966B4C"]'
         data-command=":2x2:CA,C8,CB,C9">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:CE,CC,CF,CD">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:D2,D0,D3,D1">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:6A,68,6B,69">
 </canvas>
```

# Splash screen letters 

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
          data-colors='["#808080","#1DC300","#D50BCD","#E0E000"]'
         data-command=":2x2:D6,D4,D7,D5">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:DA,D8,DB,D9">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:DE,DC,DF,DD">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:F6,F4,F7,F5">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:FA,F8,FB,F9">
 </canvas>
```

# Player ran over 

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#E0E000","#E00000","#8500D9"]'
         data-command=":2x2:E6,E4,E7,E5">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:EA,E8,EB,E9">
 </canvas>
```

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-command=":2x2:EE,EC,EF,ED">
 </canvas>
```

# Player death 

```html
 <canvas width="135" height="135"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#E0E000","#E00000","#8500D9"]'
         data-command=":2x2:F2,F0,F3,F1">
 </canvas>
```

# Full Tile Set 

This is the order of all the tiles above in the ROM.

```html
 <canvas width="1040" height="1040"
     data-getTileDataFunction="Frogger.get8x8Data"
         data-labelColor="#FFFFFF"
         data-address="0"
         data-gridX="8"
         data-gridY="8"
         data-colors='["#808080","#800000","#008000","#000080"]'
         data-command=":16x16:0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,
                        10,11,12,13,14,15,16,17,18,19,1A,1B,1C,1D,1E,1F,
                        20,21,22,23,24,25,26,27,28,29,2A,2B,2C,2D,2E,2F,
                        30,31,32,33,34,35,36,37,38,39,3A,3B,3C,3D,3E,3F,
                        40,41,42,43,44,45,46,47,48,49,4A,4B,4C,4D,4E,4F,
                        50,51,52,53,54,55,56,57,58,59,5A,5B,5C,5D,5E,5F,
                        60,61,62,63,64,65,66,67,68,69,6A,6B,6C,6D,6E,6F,
                        70,71,72,73,74,75,76,77,78,79,7A,7B,7C,7D,7E,7F,
                        80,81,82,83,84,85,86,87,88,89,8A,8B,8C,8D,8E,8F,
                        90,91,92,93,94,95,96,97,98,99,9A,9B,9C,9D,9E,9F,
                        A0,A1,A2,A3,A4,A5,A6,A7,A8,A9,AA,AB,AC,AD,AE,AF,
                        B0,B1,B2,B3,B4,B5,B6,B7,B8,B9,BA,BB,BC,BD,BE,BF,
                        C0,C1,C2,C3,C4,C5,C6,C7,C8,C9,CA,CB,CC,CD,CE,CF,
                        D0,D1,D2,D3,D4,D5,D6,D7,D8,D9,DA,DB,DC,DD,DE,DF,
                        E0,E1,E2,E3,E4,E5,E6,E7,E8,E9,EA,EB,EC,ED,EE,EF,
                        F0,F1,F2,F3,F4,F5,F6,F7,F8,F9,FA,FB,FC,FD,FE,FF">
 </canvas>
```

# ROM data

TODO show the character "1" completely decoded and rotated.

```plainCode
0000: 38 7C C2 82 86 7C 38 00 02 02 FE FE 42 02 00 00
0010: 62 F2 BA 9A 9E CE 46 00 8C DE F2 B2 92 86 04 00
0020: 08 FE FE C8 68 38 18 00 1C BE A2 A2 A2 E6 E4 00
0030: 0C 9E 92 92 D2 7E 3C 00 C0 E0 B0 9E 8E C0 C0 00
0040: 0C 6E 9A 9A B2 F2 6C 00 78 FC 96 92 92 F2 60 00
0050: 3E 7E C8 88 C8 7E 3E 00 6C FE 92 92 92 FE FE 00
0060: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0070: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0080: 00 00 00 00 00 00 00 00 3E 7E C8 88 C8 7E 3E 00
0090: 6C FE 92 92 92 FE FE 00 44 C6 82 82 C6 7C 38 00
00A0: 38 7C C6 82 82 FE FE 00 82 92 92 92 FE FE 00 00
00B0: 80 90 90 90 90 FE FE 00 9E 9E 92 82 C6 7C 38 00
00C0: FE FE 10 10 10 FE FE 00 82 82 FE FE 82 82 00 00
00D0: FC FE 02 02 02 06 04 00 82 C6 6E 3C 18 FE FE 00
00E0: 02 02 02 02 FE FE 00 00 FE FE 70 38 70 FE FE 00
00F0: FE FE 1C 38 70 FE FE 00 7C FE 82 82 82 FE 7C 00
0100: 70 F8 88 88 88 FE FE 00 7A FC 8E 8A 82 FE 7C 00
0110: 72 F6 9E 8C 88 FE FE 00 0C 5E D2 92 92 F6 64 00
0120: 80 80 FE FE 80 80 00 00 FC FE 02 02 02 FE FC 00
0130: F0 F8 1C 0E 1C F8 F0 00 F8 FE 1C 38 1C FE F8 00
0140: C6 EE 7C 38 7C EE C6 00 C0 F0 1E 1E F0 C0 00 00
0150: C2 E2 F2 BA 9E 8E 86 00 10 10 10 10 10 10 10 00
0160: 00 00 00 01 0B 0F 0F 0F 00 00 80 C0 E8 F8 F8 F8
0170: 07 00 02 03 00 00 00 00 F0 80 20 60 00 00 00 00
0180: 00 0F 1C 1C 1C 0F 03 07 00 F0 38 38 38 F0 C0 E0
0190: 0B 08 1C 1F 0F 07 00 00 D0 10 38 F8 F0 E0 00 00
01A0: 00 00 00 00 05 0F 07 07 00 00 80 80 D0 B8 D0 E0
01B0: 07 07 07 0F 05 00 00 00 E0 E0 D0 F8 D0 80 80 00
01C0: 00 01 00 08 19 0F 07 07 00 00 80 88 CC B8 D0 E0
01D0: 07 07 07 0F 19 09 00 00 E0 E0 D0 F8 CC C8 80 80
01E0: 00 00 00 00 01 0F 07 07 00 40 80 80 C0 B8 D0 E0
01F0: 07 07 0F 0F 01 01 00 00 E0 E0 D8 F8 C0 C0 80 80
0200: 00 08 08 00 20 23 06 04 04 24 44 00 00 9C A5 00
0210: 04 44 42 00 06 E4 48 00 42 40 06 04 26 22 00 06
0220: 04 06 23 48 08 00 00 00 00 A5 39 00 08 48 40 00
0230: 00 28 CC 00 40 46 06 06 00 02 02 00 10 10 00 00
0240: 7F 6F 57 EF FD 7A 3D EF FE FE DE AE DE FF F6 6A
0250: 56 6F FF FE 6D 56 EF 7F B7 7E FA F5 7B EE D7 EF
0260: 00 00 40 62 4C 00 00 00 00 38 7C 7C 7C 38 00 00
0270: 3C 42 81 A5 A5 99 42 3C FF 81 81 81 81 81 81 FF
0280: 02 72 73 7A 73 72 01 00 40 4E CE 5E CE 4E 80 00
0290: 02 33 33 39 30 30 00 00 40 CC CC 9C 0C 0C 00 00
02A0: 1E 1E 0F 1F 1F 17 1F 1F F8 F8 D8 F8 10 F8 F8 F8
02B0: 1B 1B 0F 0F 03 00 00 00 E8 78 68 E0 C0 00 00 00
02C0: 1F 1D 1F 0F 1F 1B 1B 1F F8 F8 F8 B8 B0 B8 F8 F8
02D0: 1F 1F 1D 1F 1F 0F 1F 17 F8 E8 E8 E8 F0 78 F8 F8
02E0: 00 00 00 00 01 07 07 07 00 00 00 00 80 E0 30 F8
02F0: 11 1E 1F 17 1F 0F 1F 1F 88 38 B8 F0 B8 B8 F8 F8
0300: 07 08 08 08 07 00 07 08 C0 20 20 20 C0 00 C0 20
0310: 08 08 07 00 00 0F 04 00 20 20 C0 00 20 E0 20 00
0320: 07 08 08 07 00 07 08 08 C0 20 20 C0 00 C0 20 20
0330: 07 00 06 09 08 08 04 00 C0 00 20 20 A0 60 20 00
0340: 00 01 01 00 00 00 00 00 00 D0 50 D0 D0 D0 D0 D0
0350: 01 01 03 03 00 00 01 01 B0 B0 F0 F0 FC FE FE FE
0360: 00 00 00 20 21 00 04 02 00 00 00 00 C0 78 3C 3C
0370: 02 04 00 21 20 00 00 00 3C 3C 78 C0 00 00 00 00
0380: 00 00 00 00 00 0B 13 1F 00 00 00 00 00 80 C0 E0
0390: 0F 12 0B 00 00 00 00 00 A0 40 80 00 00 00 00 00
03A0: 00 00 00 00 00 0B 13 1F 00 00 00 00 00 80 C0 E0
03B0: 0F 12 0B 00 00 00 00 00 A0 40 80 00 00 00 00 00
03C0: 00 00 00 00 00 0B 13 1F 00 00 00 00 00 80 C0 E0
03D0: 0F 12 0B 00 00 00 00 00 A0 40 80 00 00 00 00 00
03E0: 00 00 00 00 00 01 03 07 00 00 00 00 00 80 40 A0
03F0: 07 07 01 05 03 00 00 00 A0 E0 80 A0 40 00 00 00
0400: 00 00 00 00 00 01 03 07 00 00 00 00 00 80 40 A0
0410: 07 07 01 05 03 00 00 00 A0 E0 80 A0 40 00 00 00
0420: 00 00 00 00 00 01 03 07 00 00 00 00 00 80 40 A0
0430: 07 07 01 05 03 00 00 00 A0 E0 80 A0 40 00 00 00
0440: 00 00 00 00 01 07 07 0F 00 00 00 00 80 E0 E0 F0
0450: 0F 07 07 01 00 00 00 00 F0 E0 E0 80 00 00 00 00
0460: 00 00 00 00 00 01 03 07 00 00 00 00 00 80 C0 E0
0470: 07 03 01 00 00 00 00 00 E0 C0 80 00 00 00 00 00
0480: 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 80
0490: 01 00 00 00 00 00 00 00 80 00 00 00 00 00 00 00
04A0: 00 00 00 00 01 03 07 07 00 00 00 00 80 40 A0 A0
04B0: 07 07 03 01 00 00 00 00 A0 E0 C0 80 00 00 00 00
04C0: 00 00 00 00 00 00 00 01 00 00 00 00 00 00 80 80
04D0: 01 01 00 00 00 00 00 00 C0 C0 80 00 00 00 00 00
04E0: 00 01 03 05 05 07 03 01 80 C0 C0 E0 D0 D0 B0 B0
04F0: 00 00 00 00 00 00 00 00 70 30 30 10 10 10 10 00
0500: 00 00 30 30 39 33 33 02 00 00 0C 0C 9C CC CC 40
0510: 00 01 72 73 7A 73 72 02 00 80 4E CE 5E CE 4E 40
0520: 00 00 15 00 08 08 0A 00 00 00 A8 00 10 10 50 00
0530: 33 0A 31 01 31 08 30 00 C0 5C 80 8C 80 1C 00 00
0540: 00 10 10 10 10 00 03 10 00 00 08 08 08 00 C0 08
0550: 10 10 00 08 07 00 00 00 08 08 00 10 E0 00 00 00
0560: 00 00 00 10 10 10 00 00 00 00 00 08 08 08 00 00
0570: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0580: 00 00 00 00 00 03 0D 1F 18 30 38 68 F0 A0 C0 00
0590: 3F 3F 3B 19 08 00 00 00 00 00 00 80 80 40 00 00
05A0: 00 00 00 00 00 00 00 00 20 00 08 08 00 08 18 28
05B0: 00 00 00 00 00 00 00 00 70 A0 C0 C0 A0 F0 60 30
05C0: 00 00 00 00 00 00 01 03 38 18 38 78 60 F0 C0 E0
05D0: 07 0F 0F 0E 06 02 00 00 40 80 C0 C0 C0 80 00 00
05E0: 00 00 00 00 00 00 00 00 08 10 10 20 60 40 80 C0
05F0: 00 00 00 00 00 00 00 00 40 C0 E0 20 70 70 58 30
0600: 00 00 00 00 00 00 00 00 40 C0 C0 70 70 28 38 30
0610: 00 00 01 01 01 00 00 00 78 D8 F0 F0 D0 D0 40 00
0620: 00 00 00 00 00 00 00 00 00 00 80 00 C0 40 20 20
0630: 00 00 00 00 00 00 00 00 30 10 18 18 28 30 50 E0
0640: 00 01 00 00 00 01 00 00 F0 F0 D0 F0 F0 B0 F0 70
0650: 00 00 00 00 00 00 03 00 40 E0 60 20 40 C0 80 00
0660: 01 03 05 03 01 01 03 07 F6 F2 E0 F0 F0 D0 F0 F0
0670: 03 01 01 01 01 03 01 00 7C FE F6 FE F2 B0 F0 E0
0680: 00 00 00 00 60 F0 B0 78 00 10 10 10 10 10 30 30
0690: 1C 0E 07 07 01 01 01 01 10 30 30 F0 FC 3E 7E FE
06A0: 00 20 20 20 20 20 20 20 00 00 00 00 80 80 80 80
06B0: 20 20 00 00 00 00 7F 00 80 80 00 02 02 02 FE 00
06C0: 00 00 00 00 3C 20 21 20 00 82 82 82 02 02 0E 08
06D0: 20 20 00 00 00 00 7F 00 08 08 00 02 02 02 FE 00
06E0: 00 00 00 00 3F 20 20 20 00 08 00 02 F2 02 02 02
06F0: 20 20 00 00 40 00 1F 00 02 02 02 02 0E 08 F8 00
0700: 00 30 70 B2 B7 FF 7F 1F 00 00 00 00 C0 A0 C0 E0
0710: 07 03 03 01 01 00 00 00 C0 E0 E0 E0 E0 E0 60 00
0720: 00 00 00 03 0C 1C 1D 1F 00 00 00 C0 F0 F8 F8 F8
0730: 1F 1D 1C 0C 03 00 00 00 F8 E8 98 F0 C0 00 00 00
0740: 00 00 07 18 2C 09 63 7F 00 00 C0 E0 F0 F8 F8 F8
0750: 7F 63 09 2C 18 07 00 00 F8 F8 E8 90 E0 C0 00 00
0760: 00 03 1F 37 23 60 61 7F 00 C0 F8 FC FC FE FE FE
0770: 7F 61 60 23 37 1F 03 00 FE FE FE F4 CC F8 C0 00
0780: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0790: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
07A0: 00 20 20 20 20 20 21 20 00 02 02 02 F2 82 82 02
07B0: 00 08 40 00 10 00 07 00 02 02 0E 08 38 20 E0 00
07C0: 00 20 20 20 20 20 20 20 00 02 02 82 82 82 82 82
07D0: 00 00 00 00 7F 00 00 00 02 02 02 02 FE 00 00 00
07E0: 00 00 00 60 61 00 06 07 00 00 00 00 C0 78 3C 3C
07F0: 07 06 00 21 20 00 00 00 3C 3C 78 C0 00 00 00 00

0800: 38 7C C2 82 86 7C 38 00 02 02 FE FE 42 02 00 00
0810: 62 F2 BA 9A 9E CE 46 00 8C DE F2 B2 92 86 04 00
0820: 08 FE FE C8 68 38 18 00 1C BE A2 A2 A2 E6 E4 00
0830: 0C 9E 92 92 D2 7E 3C 00 C0 E0 B0 9E 8E C0 C0 00
0840: 0C 6E 9A 9A B2 F2 6C 00 78 FC 96 92 92 F2 60 00
0850: 3E 7E C8 88 C8 7E 3E 00 6C FE 92 92 92 FE FE 00
0860: FF FF FF FF FF FF FF FF FF FF FF FF FF FF 00 00
0870: FF FF FF FF 00 00 00 00 FF FF 00 00 00 00 00 00
0880: 00 00 00 00 00 00 00 00 3E 7E C8 88 C8 7E 3E 00
0890: 6C FE 92 92 92 FE FE 00 44 C6 82 82 C6 7C 38 00
08A0: 38 7C C6 82 82 FE FE 00 82 92 92 92 FE FE 00 00
08B0: 80 90 90 90 90 FE FE 00 9E 9E 92 82 C6 7C 38 00
08C0: FE FE 10 10 10 FE FE 00 82 82 FE FE 82 82 00 00
08D0: FC FE 02 02 02 06 04 00 82 C6 6E 3C 18 FE FE 00
08E0: 02 02 02 02 FE FE 00 00 FE FE 70 38 70 FE FE 00
08F0: FE FE 1C 38 70 FE FE 00 7C FE 82 82 82 FE 7C 00
0900: 70 F8 88 88 88 FE FE 00 7A FC 8E 8A 82 FE 7C 00
0910: 72 F6 9E 8C 88 FE FE 00 0C 5E D2 92 92 F6 64 00
0920: 80 80 FE FE 80 80 00 00 FC FE 02 02 02 FE FC 00
0930: F0 F8 1C 0E 1C F8 F0 00 F8 FE 1C 38 1C FE F8 00
0940: C6 EE 7C 38 7C EE C6 00 C0 F0 1E 1E F0 C0 00 00
0950: C2 E2 F2 BA 9E 8E 86 00 10 10 10 10 10 10 10 00
0960: 00 00 00 00 08 0C 0E 0F 00 00 80 00 08 18 38 78
0970: 07 01 01 00 00 00 00 00 70 40 C0 80 80 00 00 00
0980: 04 0F 0F 0F 0F 0F 07 07 20 F0 F0 F0 F0 F0 E0 E0
0990: 0F 0F 0F 0F 0F 0D 07 00 F0 F0 F0 F0 F0 B0 E0 00
09A0: 00 00 00 00 04 0C 00 00 00 00 80 00 10 58 20 10
09B0: 00 00 00 0C 04 01 00 00 10 10 20 18 10 C0 80 00
09C0: 00 01 00 08 18 0C 00 00 00 00 80 08 0C 58 20 10
09D0: 00 00 00 0C 18 09 01 00 10 10 20 18 0C C8 C0 80
09E0: 00 00 00 08 18 0C 00 00 00 40 80 08 0C 58 20 10
09F0: 00 08 18 0C 00 01 01 00 10 18 2C 18 00 C0 C0 80
0A00: 7D D7 B3 F7 5F CC D8 F8 FB D9 9B BF FF 42 00 00
0A10: E8 B8 98 BC F8 10 00 00 B8 9C B8 F8 58 C8 DC F8
0A20: 78 F8 DC 97 B3 F7 DF 75 00 00 42 FF F7 B3 97 BE
0A30: 00 00 10 F8 BE 98 B8 E8 77 FD BC FD EF E7 ED 7F
0A40: 00 10 38 10 02 07 02 17 00 00 20 70 20 00 08 AC
0A50: 39 10 00 01 13 39 10 00 C8 80 04 0E 84 11 38 10
0A60: 00 1C 3E 1E 3E 1C 00 00 67 3C 3C 7C 3C 3C 67 00
0A70: 3C 42 81 A5 A5 99 42 3C FF 81 81 81 81 81 81 FF
0A80: 02 03 06 0F 06 07 06 07 40 C0 60 F0 60 E0 60 E0
0A90: 07 07 07 0F 07 07 03 01 E0 E0 E0 F0 E0 E0 C0 80
0AA0: 01 01 00 00 00 08 00 00 38 38 38 38 D0 18 18 18
0AB0: 04 04 00 00 00 00 00 00 00 90 80 00 00 00 00 00
0AC0: 00 02 00 00 00 04 04 00 38 18 18 58 50 58 18 38
0AD0: 00 00 02 00 00 00 00 08 38 38 38 38 30 B8 38 38
0AE0: 00 00 00 03 0E 18 18 18 00 00 00 C0 70 18 C8 00
0AF0: 0E 01 00 08 00 00 00 00 78 F8 78 30 78 78 38 38
0B00: 07 08 08 08 07 00 07 08 C0 20 20 20 C0 00 C0 20
0B10: 08 08 07 00 00 0F 04 00 20 20 C0 00 20 E0 20 00
0B20: 07 08 08 07 00 07 08 08 C0 20 20 C0 00 C0 20 20
0B30: 07 00 06 09 08 08 04 00 C0 00 20 20 A0 60 20 00
0B40: 00 00 00 00 00 00 00 00 00 20 20 20 20 22 25 21
0B50: 00 00 00 00 03 03 00 00 40 42 05 01 01 01 41 20
0B60: 01 03 61 90 97 7F 3B 3D E0 F9 FB FF FE FF FC E4
0B70: 3D 3B 7F 97 90 61 03 01 E4 E4 FF FE FF FB F9 E0
0B80: 00 00 10 3C 02 07 1F 1F 00 00 04 1E 30 E0 E0 E0
0B90: 1F 1F 07 02 3C 10 00 00 E0 E0 E0 30 1E 04 00 00
0BA0: 00 00 00 10 3E 07 1F 1F 00 00 00 10 38 EC E3 E0
0BB0: 1F 1F 07 3E 10 00 00 00 E0 E3 EC 38 10 00 00 00
0BC0: 00 00 08 1E 02 07 1F 1F 00 00 20 F0 80 C0 E0 E0
0BD0: 1F 1F 07 02 1E 08 00 00 E0 E0 C0 80 F0 20 00 00
0BE0: 00 10 30 10 18 0F 07 07 00 08 0C 08 18 F0 E0 E0
0BF0: 07 0F 17 13 33 10 00 00 E0 F0 E8 C8 CC 08 00 00
0C00: 00 02 06 0C 18 0F 07 07 00 40 60 30 18 F0 E0 E0
0C10: 07 0F 0F 0B 1B 08 00 00 E0 F0 F0 D0 D8 10 00 00
0C20: 00 00 00 00 10 33 17 1F 00 00 00 00 08 CC E8 F8
0C30: 07 1F 17 33 13 00 00 00 E0 F8 E8 CC C8 00 00 00
0C40: 00 00 02 08 11 07 27 0F 00 00 40 10 88 E0 E4 F0
0C50: 0F 27 07 11 08 02 00 00 F0 E4 E0 88 10 40 00 00
0C60: 00 01 14 20 01 45 03 4F 00 80 28 04 80 A2 C0 F2
0C70: 4F 03 45 01 20 14 01 00 F2 C0 A2 80 04 28 80 00
0C80: 02 00 20 00 02 00 88 01 40 00 04 00 40 00 11 80
0C90: 01 88 00 02 00 20 00 02 80 11 00 40 00 04 00 40
0CA0: 00 00 00 04 09 03 07 07 00 00 00 10 88 C0 E0 E0
0CB0: 07 07 03 11 08 00 00 00 E0 E0 C0 88 10 00 00 00
0CC0: 00 01 00 00 00 02 04 21 00 80 00 00 00 20 90 C2
0CD0: 21 01 04 02 00 00 01 00 C2 C0 90 20 00 00 80 00
0CE0: 01 00 00 02 02 00 00 00 00 08 14 02 22 2A 48 48
0CF0: 00 00 00 00 00 00 00 00 08 00 04 04 05 01 09 08
0D00: 01 03 07 07 0F 07 07 07 80 C0 E0 E0 F0 E0 E0 E0
0D10: 07 06 06 06 0F 06 06 02 E0 60 E0 60 F0 60 E0 40
0D20: 00 2A 2A 3F 08 08 0F 07 00 54 54 FC 10 10 F0 E0
0D30: 07 3F 07 37 07 3F 03 00 EC F0 EC E0 EC F0 CC 00
0D40: 0F 1F 1F 1F 1F 0F 00 1F F0 F0 F8 F8 F8 F0 00 F8
0D50: 1F 1F 0F 07 00 00 00 00 F8 F8 F0 E0 00 00 00 00
0D60: 00 00 0F 1F 1F 1F 0F 0F 00 00 F0 F8 F8 F8 F0 F0
0D70: 0F 0F 0F 0F 0F 0F 0F 0F F0 F0 F0 F0 F0 F0 F0 F0
0D80: 00 00 00 00 00 00 02 00 20 08 00 10 00 40 00 00
0D90: 00 00 22 01 00 00 00 00 00 00 00 00 80 40 00 00
0DA0: 00 00 00 00 00 00 00 00 00 10 00 00 08 00 00 10
0DB0: 00 00 00 00 00 00 00 00 00 40 00 00 40 00 10 00
0DC0: 00 00 00 00 00 00 00 00 00 20 00 00 10 00 20 00
0DD0: 00 00 00 08 00 00 00 00 80 00 00 80 80 80 00 00
0DE0: 00 00 00 00 00 00 00 00 00 00 20 00 00 00 40 00
0DF0: 00 00 00 00 00 00 00 00 80 00 00 40 00 00 20 08
0E00: 00 00 00 00 00 00 00 00 80 00 20 00 00 10 00 08
0E10: 00 00 00 00 01 00 00 00 00 20 00 00 00 00 00 00
0E20: 00 00 00 00 00 00 00 00 00 00 00 80 00 00 40 00
0E30: 00 00 00 00 00 00 00 00 00 08 00 00 10 00 20 00
0E40: 00 00 00 00 00 00 00 00 01 01 65 05 04 44 10 00
0E50: 00 00 00 00 00 00 00 00 22 82 0A 4A 0A 08 10 10
0E60: 00 00 02 00 00 00 00 00 01 01 84 04 00 22 45 01
0E70: 00 00 00 00 00 00 00 00 85 01 09 09 40 44 14 14
0E80: 00 00 00 00 18 00 0C 00 00 00 20 00 20 02 45 01
0E90: 03 00 00 00 06 06 00 00 60 02 05 01 01 C1 81 20
0EA0: C0 E0 E3 E3 E3 E3 E3 E3 00 00 00 80 80 80 80 80
0EB0: E3 E3 FF FF FF FF 00 00 80 80 FC FE FE FE 02 00
0EC0: 7F 7F FF FF C3 E3 E0 E0 0C 8E BE BE FE FE F2 F8
0ED0: E0 E0 FF FF FF FF 00 00 F8 F8 FC FE FE FE 02 00
0EE0: 3F 3F FF FF C0 E0 E0 E0 F0 F8 FC FE 0E 0E 0E 0E
0EF0: E0 E0 FF FF 3F 3F 00 00 0E 0E FE FE F2 F8 08 00
0F00: 00 00 08 40 48 00 00 00 00 08 04 32 2A 4A 28 09
0F10: 00 00 00 00 00 00 01 01 29 01 15 14 14 14 04 20
0F20: 00 00 10 3B 7F 33 13 1F 00 00 08 DC FE FC F8 F8
0F30: 1F 13 33 7F 3B 10 00 00 F8 FC FE DC 08 00 00 00
0F40: 00 30 77 7F 33 37 7F 7F 00 18 D8 FC FC F8 F8 F8
0F50: 7F 7F 37 33 7F 77 30 00 F8 F8 F8 FC FC D8 18 00
0F60: 30 63 FF F8 BC 7F 7F 7F 0C CC FF FF FD FE FE FE
0F70: 7F 7F 7F BC F8 FF 63 30 FE FE FE FD FF FF CC 00
0F80: 0C 0C 02 39 68 DC FE FE 00 00 00 03 83 44 28 10
0F90: FE DC 68 39 02 0C 0C 00 28 44 83 03 00 00 00 00
0FA0: C3 E3 E3 E3 E3 E3 E0 E0 FC FE FE FE 0E 8E 8E 0E
0FB0: F0 F8 3F 3F 0F 0F 00 00 3E 3E F2 F8 C8 E0 20 00
0FC0: C0 E0 E3 E3 E3 E3 E3 E3 0C 0E 0E 8E 8E 8E 8E 8E
0FD0: FF FF FF FF 00 00 00 00 FE FE FE FE 02 00 00 00
0FE0: 01 03 61 90 97 7F 39 38 E0 F9 FB FF FE FF FC E4
0FF0: 38 39 7F 97 90 61 03 01 E4 E4 FF FE FF FB F9 E0
```
