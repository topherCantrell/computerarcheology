/**
 * This module contains access methods for reading bytes of data from a disassembly file.
 */

// Tracks a data cursor for byte-at-a-time access
var lineArray = null;
var lineAddress = 0;
var linePos = 0;

/**
 * This function sets the data cursor to the given address. Once set, callers
 * can use "getNextByte" to fetch bytes one at a time.
 * @param address the address to start reading from
 */
function setDataCursor(address) {
	lineAddress = address;
	lineArray = new Array();
	getLineOfData(lineAddress,lineArray);
	linePos = 0;
}

/**
 * This function gets the next byte of data from the cursor and advanced
 * the cursor.
 * @returns the next byte
 */
function getNextByte() {
	if(linePos>=lineArray.length) {
		setDataCursor(lineAddress);
	}
	++lineAddress;
	return lineArray[linePos++];
}

/**
 * This function reads multiple lines of disassembly data to build up an
 * array of bytes of the given size.
 * @return the array of data
 */
function getData(start,size) {		
	var ret = new Array();
	while(size>ret.length) {
		var nr = getLineOfData(start+ret.length,ret);
		if(nr==0) {
			// ERROR
			return null;
		}
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
 * address and a ":".
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