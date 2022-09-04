var Binary = (function() {

    var my = {} // For public export    

    /**
     * Load data from a binary file. 
     * The file is loaded synchronously, so don't get carried away.
     * @param {string} fname the URL of the binary file
     * @returns {Uint8Array} the data
     */
    my.readBinary = function(url) {
        var req = new XMLHttpRequest()
        req.open( "GET", url, false ) // false for synchronous request
        req.overrideMimeType('text\/plain; charset=x-user-defined')
        req.send(null)
        str = req.response
        var buf = new ArrayBuffer(str.length)
        var bufView = new Uint8Array(buf)
        for (var i=0, strLen=str.length; i<strLen; i++) {
            bufView[i] = str.charCodeAt(i)
        }
        return bufView
    }

    /**
     * Convert a binary value to a 8-bit binary text string
     * @param {int} value 
     * @returns str the 8-bits
     */
    my.padBinaryTo8Bits = function(value) {
    	var ret = value.toString(2)
    	while(ret.length<8) ret="0"+ret
    	return ret
    }

    return my

}())
