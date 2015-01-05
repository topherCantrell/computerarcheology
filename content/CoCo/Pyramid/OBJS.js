
// The code assumes a specific order to the objects. For instance, "WATER IN BOTTLE" must be placed in object lists
// after "BOTTLE" for it to read correctly. Objects are kept here in an array (instead of a map-by-name) to preserve 
// the original order. 

// If an object is packable then it has a "short" description used with "inventory".
// If an object is visible in a room then it has a "long" description. The room description for room 56
// includes a description of the stream object fixed in it, and thus "stream_56" has no long description 
// to print.

var OBJS = function () {

	var objData = [	
	    {name: '#bridge_15',	location: '', packable: false, treasure: false, long: 'A STONE BRIDGE NOW SPANS THE BOTTOMLESS PIT.'},
		{name: '#bridge_18',	location: '', packable: false, treasure: false, long: 'A STONE BRIDGE NOW SPANS THE BOTTOMLESS PIT.'},
		{name: '#-3-',			location: '', packable: false, treasure: false},
		{name: '#-4-',			location: '', packable: false, treasure: false},
		{name: '#-5-',			location: '', packable: false, treasure: false},
		{name: '#MACHINE',		location: 'room_51', packable: false, treasure: false, long: 'THERE IS A MASSIVE VENDING MACHINE HERE. THE INSTRUCTIONS ON IT READ- "DROP COINS HERE TO RECIEVE FRESH BATTERIES".'},
		{name: '#PLANT_A',		location: 'room_81', packable: false, treasure: false, long: 'THERE IS A TINY PLANT IN THE PIT, MURMURING "WATER, WATER, ..."'},
		{name: '#PLANT_B',		location: '', packable: false, treasure: false, long: 'THERE IS A TWELVE FOOT BEAN STALK STRETCHING UP OUT OF THE PIT, BELLOWING "WATER... WATER..."'},
		{name: '#PLANT_C',		location: '', packable: false, treasure: false, long: 'THERE IS A GIGANTIC BEAN STALK STRETCHING ALL THE WAY UP TO THE HOLE.'},
		{name: '#-10-',			location: '', packable: false, treasure: false},
		{name: '#SERPENT',		location: 'room_16', packable: false, treasure: false, long: 'A HUGE GREEN FIERCE SERPENT BARS THE WAY!'},
		{name: '#-12-',			location: '', packable: false, treasure: false},
		{name: '#-13-',			location: '', packable: false, treasure: false},
		{name: '#LAMP_off',		location: 'room_2', packable: true,  treasure: false, short: 'BRASS LANTERN', long: 'THERE IS A SHINY BRASS LAMP NEARBY.'},
		{name: '#LAMP_on',		location: '', packable: true,  treasure: false, short: 'BRASS LANTERN', long: 'THERE IS A LAMP SHINING NEARBY.', time: 310},
		{name: '#BOX',			location: 'room_8', packable: true,  treasure: false, short: 'STATUE BOX', long: 'THERE IS A SMALL STATUE BOX DISCARDED NEARBY.'},
		{name: '#SCEPTER',		location: 'room_9', packable: true,  treasure: false, short: 'SCEPTER', long: 'A THREE FOOT SCEPTER WITH AN ANKH ON AN END LIES NEARBY.'},
		{name: '#PILLOW',		location: 'room_72', packable: true,  treasure: false, short: 'VELVET PILLOW', long: 'A SMALL VELVET PILLOW LIES ON THE FLOOR.'},
		{name: '#BIRD',			location: 'room_11', packable: true,  treasure: false, short: 'THERE IS A BIRD STATUE IN THE BOX.', long: 'A STATUE OF THE BIRD GOD IS SITTING HERE.'},
		{name: '#BIRD_boxed',	location: '', packable: false, treasure: false, long: 'THERE IS A BIRD STATUE IN THE BOX.', short: 'THERE IS A BIRD STATUE IN THE BOX.'},
		{name: '#POTTERY',		location: '', packable: false, treasure: false, long: 'THE FLOOR IS LITTERED WITH WORTHLESS SHARDS OF POTTERY.'},
		{name: '#PEARL',		location: '', packable: true,  treasure: true,  short: 'GLISTENING PEARL', long: 'OFF TO ONE SIDE LIES A GLISTENING PEARL!'},
		{name: '#SARCOPH_full',	location: 'room_61', packable: true,  treasure: false, short: 'SARCOPHAGUS >GROAN<', long: 'THERE IS A SARCOPHAGUS HERE WITH IT\'S COVER TIGHTLY CLOSED.'},
		{name: '#SARCOPH_empty', location: '', packable: true,  treasure: false, short: 'SARCOPHAGUS >GROAN<', long: 'THERE IS A SARCOPHAGUS HERE WITH IT\'S COVER TIGHTLY CLOSED.'},
		{name: '#MAGAZINES',	location: 'room_59', packable: true,  treasure: false, short: '"EGYPTIAN WEEKLY"', long: 'THERE ARE A FEW RECENT ISSUES OF "EGYPTIAN WEEKLY" MAGAZINE HERE.'},
		{name: '#FOOD',			location: 'room_2', packable: true,  treasure: false, short: 'TASTY FOOD', long: 'THERE IS FOOD HERE.'},
		{name: '#BOTTLE',		location: 'room_2', packable: true,  treasure: false, short: 'SMALL BOTTLE', long: 'THERE IS A BOTTLE HERE.'},
		{name: '#WATER',		location: '#BOTTLE', packable: true,  treasure: false, short: 'WATER IN THE BOTTLE', long: 'THERE IS WATER IN THE BOTTLE.'},
		{name: '#-29-',			location: '', packable: false, treasure: false},
		{name: '#stream_56',	location: 'room_56', packable: false, treasure: false},
		{name: '#EMERALD',		location: 'room_76', packable: true,  treasure: true,  short: 'EGG-SIZED EMERALD', long: 'THERE IS AN EMERALD HERE THE SIZE OF A PLOVER\'S EGG!'},
		{name: '#VASE_pillow',	location: '', packable: true,  treasure: true,  short: 'VASE\n', long: 'THE VASE IS NOW RESTING, DELICATELY, ON A VELVET PILLOW.'},
		{name: '#VASE_solo',	location: 'room_73', packable: true,  treasure: true,  short: 'VASE', long: 'THERE IS A DELICATE, PRECIOUS, VASE HERE!'},
		{name: '#KEY',			location: 'room_68', packable: true,  treasure: true,  short: 'JEWELED KEY', long: 'THERE IS A JEWEL-ENCRUSTED KEY HERE!'},
		{name: '#BATTERIES_fresh', location: '', packable: true,  treasure: false, short: 'BATTERIES', long: 'THERE ARE FRESH BATTERIES HERE.'},
		{name: '#BATTERIES_worn', location: '', packable: true,  treasure: false, short: 'BATTERIES', long: 'SOME WORN-OUT BATTERIES HAVE BEEN DISCARDED NEARBY.'},
		{name: '#GOLD',			location: 'room_14', packable: true,  treasure: true,  short: 'LARGE GOLD NUGGET', long: 'THERE IS A LARGE SPARKLING NUGGET OF GOLD HERE!'},
		{name: '#DIAMONDS',		location: 'room_17', packable: true,  treasure: true,  short: 'SEVERAL DIAMONDS', long: 'THERE ARE DIAMONDS HERE!'},
		{name: '#SILVER',		location: 'room_25', packable: true,  treasure: true,  short: 'SILVER BARS', long: 'THERE ARE BARS OF SILVER HERE!'},
		{name: '#JEWELRY',		location: 'room_18', packable: true,  treasure: true,  short: 'PRECIOUS JEWELRY', long: 'THERE IS PRECIOUS JEWELRY HERE!'},
		{name: '#COINS',		location: 'room_24', packable: true,  treasure: true,  short: 'RARE COINS', long: 'THERE ARE MANY COINS HERE!'},
		{name: '#CHEST',		location: '', packable: true,  treasure: true,  short: 'TREASURE CHEST', long: 'THE PHARAOH\'S TREASURE CHEST IS HERE!'},
		{name: '#NEST',			location: 'room_71', packable: true,  treasure: true,  short: 'GOLDEN EGGS', long: 'THERE IS A LARGE NEST HERE, FULL OF GOLDEN EGGS!'},
		{name: '#LAMP_dead',	location: '', packable: true,  treasure: false, short: 'BRASS LANTERN', long: 'THERE IS A SHINY BRASS LAMP NEARBY.'}
    ];
        
    /**
     * This function returns the object with the given name.
     * @param obj the object name
     * @return the object or undefined
     */
	var getExactObjectByName = function (name) {
		for (var x = 0;x < objData.length;++x) {
			if (objData[x].name === name) {
				return objData[x];
			}
		}
		return null;
	};
    
    /**
     * This function returns the object with the given name walking
     * parent containers to the top level object.
     * @param obj the object name
     * @return the object or undefined
     */
	var getTopObjectByName = function (name) {
		var obj = getExactObjectByName(name);
		if (obj.location && obj.location.charAt(0) === '#') {
			obj = getTopObjectByName(obj.location);
		}
		return obj;
	};
        
    /**
     * This method returns an array of all objects.
     * @return array of all objects
     */
    var getAllObjects = function () {
        return objData;
    };
			
    /**
     * This method returns an array of all objects at a particular location. This walks
     * objects to their containers (if water is in the bottle, then the water is where
     * the bottle is).
     * @param location the room name (or "pack") 
     * @return the list of objects
     */
    var getObjectsAtLocation = function (location) {    
        var ret = [];
        for (var x = 0;x < objData.length;++x) {
            if (getTopObjectByName(objData[x].name).location === location) {
                ret.push(objData[x]);
            }
        }               
        return ret;
    };
        
    // Public API
    return {
        getExactObjectByName : getExactObjectByName,
        getTopObjectByName : getTopObjectByName,
        getAllObjects : getAllObjects,
        getObjectsAtLocation : getObjectsAtLocation       
    };
    
}();