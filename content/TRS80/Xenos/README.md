![TRS80 Xenos](Xenos.png)

# Xenos

>>> deploy:<br>
>>>   +Xenos.png<br>
>>>   +combined.bin<br>
>>>   +xenos.js<br>
>>>   RAMUse.md<br>
>>>   Code.md<br>
>>>   Section1.md<br>
>>>   Section2.md<br>
>>>   Section3.md<br>
>>>   Section4.md<br>
>>>   Section5.md<br>
>>>   Section6.md<br>
>>>   Section7.md<br>
>>>   Section8.md<br>
>>>   Section9.md<br>
>>>   SSVDOBJS.md<br>
>>>   USVDOBJS.md<br>
>>>   ----<br>
>>>   Journal.md<br>

>>> playMe {

# Play Me!
Play the game in a TRS80 emulator. Click on the black console and press any key.

```html
<textarea id="xenosConsole" rows="16" style="overflow:hidden;background-color: black;color: white;font-family: monospace;font-size:12px;width:65ch;" data-gramm="false" data-gramm_editor="false" data-enable-grammarly="false"></textarea>

<div id="xenosTapeArea" style="display:none">
The text area below is the virtual disk file. Instead of writing to disk, the emulator writes data as two-digit hex
values to this text area.</p>

The SAVE command will write 480 bytes (960 characters)
to the text box. You must select all the characters (CNTRL-A) and copy them (CNTRL-C). Then store them
in a text file for later use. </p>

Before the LOAD command you must paste the desired saved-data back into the text area.</p>

<textarea id="xenosTape" rows="12" style="font-size:8px;width:100ch;" data-gramm="false" data-gramm_editor="false" data-enable-grammarly="false"></textarea>
</div>
```

>>> }

# Code Links

* [Disassembled Code](Code.html)
* [RAM Usage](RAMUse.html)
* [Hardware](../HardwareDisk.html)

# TODO

Just getting started. Check back soon.

# References

If you seek specific game information, solutions, and online emulators then check out [Sean Murphy's wonderful site](http://www.figmentfly.com).

```html
<script src="/js/Z80.js"></script>
<script src="xenos.js"></script>
<script>
    window.onload = function() {
        startXenos("xenosConsole","xenosTape");
    }
</script>
```