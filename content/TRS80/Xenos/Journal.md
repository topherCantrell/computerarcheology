![Journal](../../img/journal.jpg)

# Journal

## 5/31/2026

Sean Murphy notes that the Gaming after 40 guy wrote about an alien world that we haven't seen. He
asked me to dig into the code and look for it. From his email:

https://gamingafter40.blogspot.com/2010/03/adventure-of-week-xenos-1982.html

"There's a whole alien world to explore if we SQUEEZE HANDGRIP in the ship's recreation room; we're beamed to a fairly large area that distinctly resembles our own culture, as is so often the case in science fiction.  There are thousands of aliens going about their business, and fun areas like a museum and a disco (remember, this game was published in 1982.)  There are even references to American landmarks like GRAND CENTRAL STATION, PITTSBURG [sic] and DETROIT.  We can even pick up some alien language here, though the decoding is straightforward -- NURGLE, ENURGLE, SORWIT and WITSOR represent the cardinal directions; ESNEL = DOOR, and UKORK variously means LOCKED and/or KEY."

I'm going to dig in and find it. First step was to extract all the binary.

The game comes on disk with multiple files. The Z80 code seems to be isolated to the ZENOS.CMD file. The rest seems to be data.
Hopefully, the game is written with the BEDLAM engine and will be easy to decode. X fingers X.

Looking at the code, a lot of it is byte-for-byte duplicate of bedlam. This will be fun.
