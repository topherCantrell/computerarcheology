
/*global doBrowserOutput, document, window, GAME, process */

// In the browser be sure and include these BEFORE this MAIN.js

// #include ROOMS.js
// #include OBJS.js
// #include PARSE.js
// #include GAME.js
// #include DEFAULT.js

/**
 * The browser <input> field must call this with every keystroke. This function
 * watches for ENTER and triggers the command processing.
 */
function doBrowserInput(event) {
    if (GAME.gameOver) {
        return;
    }
    if (event.which === 13 || event.keyCode === 13) {
        var ti = document.getElementById("con_stdin");
        doBrowserOutput(ti.value + "\n");
        GAME.input(ti.value);
        ti.value = "";
    }            
}      
    
/** 
 * This function sends text to the browser's <textarea> and scrolls the field
 * to the bottom.
 */
function doBrowserOutput(text) {
    if (GAME.gameOver) {
        return;
    }
    var ta = document.getElementById("con_stdout");
    ta.value += text;
    ta.scrollTop = ta.scrollHeight;
}

/**
 * This function prints the text followed by a line feed.
 */
function println(text) {
    this.printChars(text + "\n");
}

// Figure out if we are in the browser or nodejs and map the input/output
// functions accordingly.
if (this.hasOwnProperty("window")) {
    // We are running inside of node. Output goes to a textarea in the browser. 
    this.printChars = doBrowserOutput;
    
    // Wait for the output textarea to be created before we try and
    // print to it.
    window.onload = function () {
        GAME.init();
    };

} else {    
    // We are running inside node.
                
    //Output goes to stdout.
    this.printChars = function (text) {    
        if (GAME.gameOver) {
            return;
        }
        process.stdout.write(text);
    };  
    
    // Input comes from stdin.
    process.stdin.resume();
    process.stdin.setEncoding('utf8');  
    process.stdin.on('data', function (chunk) {
        // This gets called every time the ENTER key is pressed.
        if (GAME.gameOver) {
            return;
        }
        GAME.input(chunk);
    });     
    
    GAME.init();
}