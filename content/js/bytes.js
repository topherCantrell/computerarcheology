/**
 * This module contains access methods for reading bytes of data from a disassembly file.
 */

var dataCache = null;
var dataOrigin = null;

//Tracks a data cursor for byte-at-a-time access
var cursor = null;

function loadDataCache() {
    var lines = htmlUpper.split("\n");
    dataCache = new Array();
    for (var x=0;x<lines.length;x=x+1) {
        var line = lines[x].trim();
        var i = line.indexOf(";");
        if (i>=0) {
            line = line.substring(0,i).trim();
        }
        
        while (true) {
            i = line.indexOf("<");
            if (i<0) {
                line = line.trim();
                break;
            }
            j = line.indexOf(">",i);
            if(j<0) {
                break;
            }
            line = line.substring(0,i)+line.substring(j+1)
        }
        
        if (line.length<5 || line[4]!=':') {
            continue;
        }
        var adr = parseInt(line.substring(0,5),16);
        if (dataOrigin==null) {
            dataOrigin = adr;
        }
        
        if (adr-dataOrigin != dataCache.length) {
            alert("Data continuency error: "+adr);
        }
        
        line = line.substring(5).trim();
        
        while(true) {        
            if (line.length<3) {
                if (isTwoDigitHex(line)) {
                    dataCache.push(parseInt(line,16));
                }
                break;
            }
            if(line[2]!=' ') {
                break;
            }
            var a = line.substring(0,2);
            line = line.substring(2).trim();
            if (!isTwoDigitHex(a)) {
                break;
            }
            dataCache.push(parseInt(a,16));
            
        }
    }
    
}

/**
 * This function sets the data cursor to the given address. Once set, callers
 * can use "getNextByte" to fetch bytes one at a time.
 * @param address the address to start reading from
 */
function setDataCursor(address) {    
    if (dataCache==null) {
        loadDataCache()
    }
	cursor = address - dataOrigin;	
}

/**
 * This function gets the next byte of data from the cursor and advanced
 * the cursor.
 * @returns the next byte
 */
function getNextByte() {    
    return dataCache[cursor++];
}

/**
 * This function reads multiple lines of disassembly data to build up an
 * array of bytes of the given size.
 * @return the array of data
 */
function getData(start,size) {		
	var ret = new Array();
	
	if (dataCache == null) {
	    loadDataCache();
	}
	
	for (var x=0;x<size;x=x+1) {
	    ret.push(dataCache[start - dataOrigin + x])
	}
	return ret;
}

function isTwoDigitHex(s) {
	if (s.length<2) {
		return false;
	}
	if(s.length>2 && s.charAt(2)!=" ") {
		return false;
	}
	var c = s.charAt(0);
	if ( !((c>='0' && c<='9') || (c>='A' && c<='F')) ){
		return false;
	}
	c = s.charAt(1);
	if ( !((c>='0' && c<='9') || (c>='A' && c<='F')) ){
		return false;
	}
	return true;
}

/**
 * This function reads a single line of disassembly data starting with the
 * address and a ":". This is old and slow. Callers should use the cached
 * data functions above.
 * @param address the address of data to get
 * @param ret the data array to append to
 * @return number of bytes parsed
 */
function getLineOfData(address,ret) {
	
	var addrHex = address.toString(16).toUpperCase() + ":";
	var text = htmlUpper;
	
	var ind = text.indexOf(addrHex);
	var j = text.indexOf(";",ind);
	var k = text.indexOf("\n",ind);
	
	if(j<0 || k<j) {
		j = k;
	}
	
	text = text.substring(ind+addrHex.length+1,j).trim();
		
	var sizeAdded = 0;	
	while(text.length>0) {
		text = text.trim()
		if (!isTwoDigitHex(text)) {
			break;
		}
		++sizeAdded;
		ret.push(parseInt(text.substring(0,2),16));
		text = text.substring(2);
	}
			
	return sizeAdded;
	
}