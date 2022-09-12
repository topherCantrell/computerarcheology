var Doubleback = (function() {    
    
    var my = {} // For public export

    my.data = null // Loaded after the page loads
    my.origin = 0
    my.cursiveData = null

    my.ctx = null
    my.can = null
    my.cursivePos = 0
    my.cursiveX = 0x1F
    my.cursiveY = 0x18
    my.cursiveLastX = 0
    my.cursiveLastY = 0

    function clearCursive() {
        my.cursivePos = 0
        my.cursiveX = 0x1F
        my.cursiveY = 0x18
        my.ctx.fillStyle = 'black';
        my.ctx.fillRect(0, 0, my.can.width, my.can.height);
        my.ctx.fillStyle = 'blue';
    }
    
    my.loadCursiveData = function() {
        if(my.cursiveData) {
            return
        }
        my.cursiveData = []
        for(var i=0;i<52;++i) {             
            var c = Binary.padBinaryTo8Bits(my.data[0xCEC3+i*2-my.origin]) + Binary.padBinaryTo8Bits(my.data[0xCEC3+i*2+1-my.origin])
            my.cursiveData.push(parseInt(c.substring(13,16),2))
            my.cursiveData.push(parseInt(c.substring(10,13),2))
            my.cursiveData.push(parseInt(c.substring(7,10),2))
            my.cursiveData.push(parseInt(c.substring(4,7),2))
            my.cursiveData.push(parseInt(c.substring(1,4),2))
        }
        my.can = $('#cursiveArea')[0]
        my.ctx = my.can.getContext('2d')	

	    fastCursive()
    }

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

    my.get8x5Tile = function(number,address) {
        if(address==0) {
            // Number is absolute address
            address = number - my.origin
        } else {
            // Number is tile offset from data address
            address = address - my.origin // Disassembly origin
            address = address + number * 5 // 5 bytes per tile
        }        
        ret = []
		for(var y=0;y<10;y=y+1) {
			var b = Binary.padBinaryTo8Bits(my.data[address+y])
			for(var x=0;x<8;x=x+2) {
				ret.push(parseInt(b.substring(x,x+2),2))
			}
		}				
		return ret        
    }

    dirs = [
        [0,-1],
        [1,-1],
        [1,0],
        [1,1],
        [0,1],
        [-1,1],
        [-1,0],
        [-1,-1]
    ]
    
    function cursiveOne() {
        if(my.cursivePos>=my.cursiveData.length) {
            clearCursive()
        }
        if(my.cursivePos>0) {
            my.ctx.fillStyle='blue'
            my.ctx.fillRect(my.cursiveLastX*5,my.cursiveLastY*5,5,5)
            my.ctx.fillRect((128-my.cursiveLastX)*5,(0x3C-my.cursiveLastY)*5,5,5)
        }
        d = dirs[my.cursiveData[my.cursivePos++]]
        my.cursiveX+=d[0]
        my.cursiveY+=d[1]
        if(my.cursivePos<(my.cursiveData.length-1)) {
            my.ctx.fillStyle='white'
        }
        my.ctx.fillRect(my.cursiveX*5,my.cursiveY*5,5,5)
        my.ctx.fillRect((128-my.cursiveX)*5,(0x3C-my.cursiveY)*5,5,5)
        my.cursiveLastX = my.cursiveX
        my.cursiveLastY = my.cursiveY
        my.ctx.stroke()
    }

    function fastCursive() {
        clearCursive()
        for(i=0;i<my.cursiveData.length;++i) {
            cursiveOne()
        }        
    }

    function nextStep() {
        if(my.cursivePos<my.cursiveData.length) {
            cursiveOne();
            setTimeout(nextStep,50);
        }
    }

    my.slowCursive = function() {
        clearCursive()
        nextStep()
    }    
    my.stepCursive = function () {
        cursiveOne()
    }

    return my

}())
