# Generic Assembler

See the Example Input below.

The assembler recognizes four different kinds of text lines:
  - A blank line (ignored)
  - A label: a single word/number ending with a ":"
  - A directive: a line beginning with a "."
  - Everything else is a line of assembly opcodes
  
# Comments

```
  LD  A,5  ; Five rows per object
```
Everything after a ";" on a line is ignored as a comment. Lines that begin
with a ";" are seen as blank lines (ignored).

# Includes

```
.include hardware.asm
```

# Key/Value Constants

```
._CPU = Z80
.CONST_A = 0x20
```

KEY = VALUE pairs. Keys that begin with "_" are meant for the assembler. 

# Data Definition

## Bytes

```
. 0x01,2,3,4,0x05
```

## Words

```
.W 0x01,0x1234
```

# Example Input

```
; Example assembly input

.include hardware.asm

._CPU = Z80
.CONST_A = 0x20

0x8000:
Start:

   LD  A,0x23     ; A constant
   LD  B,(0x10)
   LD  H,(DataA)
   LD  E,CONST_A
   JP  Start

DataA:
. 0x10,0x20,0x30

DataB:
. 0x20
```