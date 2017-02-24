$(function() {
    

    function write(addr,value) {
        if(addr<0x3F21) {
            return BinaryData.write(addr,value);
        }
        throw "Unhandled write "+addr+":"+value;
    }
    
    function read(addr) {
        
        // 6809 reset vector (point to game code at 0600)
        if(addr===0xFFFE) return 0x06;
        if(addr===0xFFFF) return 0x00;
        
        // BASIC ROM vector points to character-output
        // routine. We'll intercept 0100 below.
        if(addr===0xA002) return 0x01;
        if(addr===0xA003) return 0x00;
        
        // BASIC ROM vector points to character-input
        // routine. We'll intercept 0200 below.
        if(addr===0xA000) return 0x02;
        if(addr===0xA001) return 0x00;
        
        // Trying to read the code at the character-output routine.
        // Instead we'll print A on the screen and return a 0x39
        // (the opcode for RTS)
        if(addr===0x0100) {
            var status = CPU6809.status();
            console.log(String.fromCharCode(status.a));
            return 0x39;
        }
        
        // Trying to read the code at the character-input routine.
        if(addr===0x0200) {
            throw "Implement me";
        }
        
        // Anything else comes from RAM where the game
        // is loaded.
        if(addr<0x3F21) {
            return BinaryData.read(addr);
        }
        
        // Oops! Not in our address space
        throw "Unhandled read "+addr;
    }
        
    CPU6809.init(write,read,function(){});
    
    BinaryData.loadDataCacheFromURL("/CoCo/Pyramid/Code.html",function() { 
        CPU6809.steps(10000);
    });
    
    
    
});