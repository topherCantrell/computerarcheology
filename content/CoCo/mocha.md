# Using the online JS Mocha - The HTML5 CoCo 2 Emulator

http://www.haplessgenius.com/mocha/

You can pull BIN files from the site like this:

  * http://www.haplessgenius.com/mocha/bin/dung.bin
  * http://www.haplessgenius.com/mocha/bin/downland.bin
  * http://www.haplessgenius.com/mocha/bin/chess.bin

BIN files have a five-byte header and a five byte footer.

For standard games, the format is:

```
00 20 00 C0 00 .............. FF 00 00 C0 00
```

The `app_make_mocha_bin` tool reads a code md file and makes the `mocha.bin` file that can be loaded into the online mocha emulator.

For instance, in Daggorath Code.md change D7D9 to 02 to start with the Elvish Sword.
