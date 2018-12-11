The "new style" (won't be new for long) is to keep as closely to pure markdown as possible.

Here are the details as I flesh them out.

# General Structure

The landing page of a directory is `README.md`. On the web site, every page has an image that appears at the top of the page. Every 
page has a title that appears in the browser's tab. The page must contain an image link before the first heading. This becomes the page's title image. 
The image's alternate-text is used as the HTML title.

```
![Mad-Min](Madness.jpg)
# Madness and the Minotaur
```

# Deployment Info

The entry point README for a directory must contain deployment information for the files and directories within. For instance:

```
>>> deploy:<br>
>>> Info.md<br>
>>> Other.md<br>
>>> +file.jpg<br>
>>> +file.jpg<br>
>>>     SubDirectory<br>
```

Spacing is optional. The `<br>` is optional. A "+" before a file or directory indicates that the file or directory is to be copied to the
deployment web site but does contribute to the navigation tree.

# Special Areas

The web page allows for special areas like "Play Me" and "Tour Guide". These areas are wrapped in block quote elements like this:

```
>>> playMe {
>>> }

>>> tourGuide {
>>> }
```

# Raw HTML
Sections in tripple-back-ticks are not processed as regular markdown. 

Sections of HTML can be inserted in the markdown like this:
```
    ```html
    <hr>    
    ```
```

Sections of code are placed in code blocks:
```
    ```code
    This is some code
    ````
```

# Address Maps

Memory maps are defined in regular tables with a leading block quote. Like this:
```
>>> memory
| | | |
|:-------- |:------- |:----------------- |
| FF00     | PIA0_DA | I/O data or direction (depends on control setting) |
| FF01     | PIA0_CA | Control |
| FF02     | PIA0_DB | I/O data or direction (depends on control setting) |
| FF03     | PIA0_CB | Control |
```

# Disassembly Files

Disassembly files have this block quote at the top:
```
>>> code
```

You must give the CPU in a block quote near the top (before the first line of disassembly):
```
>>> cpu 6809
```

You link the disassembly to other files containing address maps like this:
```
>>> memoryTable ram  
* [RAM Usage](RAMUse.md)
>>> memoryTable hard 
* [Hardware Info](..\Hardware.md)
```

The `ram` is for RAM variables. The `hard` is for hardware registers. These have special colorings in the final
renderings. You can use any name for other types of mapping files.
