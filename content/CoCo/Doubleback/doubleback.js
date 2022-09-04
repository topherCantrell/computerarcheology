var Doubleback = (function() {    
    
    var my = {} // For public export

    my.data = null // Loaded after the page loads
    my.origin = 0

    my.get8x8Tile = function(number,address) {
        if(address==0) {
            // Number is absolute address
            address = number - my.origin
        } else {
            // Number is tile offset from data address
            address = address - my.origin // Disassembly origin
            address = address + number * 16 // 16 bytes per tile
        }        
        ret = []
		for(var y=0;y<16;y=y+2) {
			var b = Binary.padBinaryTo8Bits(my.data[address+y]) + Binary.padBinaryTo8Bits(my.data[address+y+1])
			for(var x=0;x<16;x=x+2) {
				ret.push(parseInt(b.substring(x,x+2),2))
			}
		}				
		return ret        
    }

    return my

}())
