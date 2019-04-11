
function makeBinaryDataPyramid() {
    
    var dataOrigin = 0x0300;
    var data = [
    	// TODO
    ];
    
    var my = {};
    
    // Simple read/write
    my.read = function(addr) {
        return data[addr-dataOrigin];
    };
    my.write = function(addr,value) {
       data[addr-dataOrigin] = value;
    };
    
    my.loadDataCacheFromURL = function(url,success) {
        // Simulates an async callback
        success();        
    };
    
    return my;
    
};