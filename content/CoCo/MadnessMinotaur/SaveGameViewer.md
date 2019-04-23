![Madness and the Minotaur](Madness.jpg)

# Madness and the Minotaur Save-Game Viewer

>>> playMe {

Paste the text of your save-game text file into the box below and click the "Show" button.

```html
</p>
<textarea id="cocoTape" rows="16" style="font-size:8px;width:80ch;" ></textarea>
</p>
<button id="parseData">Show</button>
</p>

<script src="BinaryDataMadness.js"></script>
<script src="madness.js"></script>
<script>
$(function() {

$('#parseData').on('click',function() {
	viewSaveFile($('#cocoTape').val());
});

});
</script>

```

>>> }

