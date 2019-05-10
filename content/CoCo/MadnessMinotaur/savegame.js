
binaryData = makeBinaryDataMadness();

var ROOM_DESC = [
'STONE TOWER', 'EMPTY ROOM', 'GUARD ROOM', 'PILE OF BONES', 'CLEAN ROOM', 'TROPHY ROOM', 'EMPTY CLOSET', 'SLOPING SHAFT',
'MARBLE FLOOR', 'NARCISSUS PLANTS', 'TABLE AND CHAIR', 'PAINTING', 'BROKEN GLASS', 'BROKEN TILES', 'BED ROOM', 'NO WINDOWS',
'WEST, POOL', 'EAST, POOL', 'SMALL LIBRARY', 'ANCIENT CARVINGS', 'GREEN MARBLE', 'WINE CELLAR', 'THE KING', 'MIST SWIRLING',
'WIDE HALL', 'MARBLE PORTAL', 'ROYAL COURT', 'VOICES, DEAD', 'DARK CHAMBER', 'GREEN MIST', 'BROKEN SHADOW', 'CEILING, SLOPING',
'TWISTING STAIR', 'DARK, TOWER', 'SUNKEN PIT', 'SERVANT CHAMBER', 'PANTRY', 'GREAT BEER', 'EMPTY CHAMBER', 'TEMPLE OF ZEUS',
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE, PIT', 'MAZE', 'MAZE', 'MAZE',
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
// 64
'GREAT PIT', 'STONE WALL', 'SMALL ROOM', 'GREAT CRYPT', 'BONES, WALL', 'CHILL MIST', 'FOUL SMELLING', 'STONE SHAFT',
'HALL, COURT', 'EMPTY CHAMBER', 'LARGE POOL','LARGE CAVERN', 'TWISTING PASSAGE', 'SHALLOW HOLE', 'CHASM,SOUTH', 'STONE, CARVINGS',
'TWISTING MUSTY', 'SUNKEN ROOM', 'CHILL DAMP', 'CAVERN, STONE', 'WINDING PASSAGE', 'TWISTING WINDING', 'SMALL CHAMBER', 'SHALLOW PIT',
'MUSTY, CORRIDOR', 'EDGE, SHAFT', 'TOMB, SKULL', 'STONE TILES', 'WIDE ROOM', 'WOOD PASSAGE', 'WIDE HALL', 'STONE TUNNEL',
'MUSTY PASSAGE', 'TWISTING PASSAGE', 'BROKEN PASSAGE', 'BROKEN STONE', 'STONE CHAPEL', 'LONG PASSAGE', 'ANCIENT KING', 'CAVE, VOICES',
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
// 128
'NARROW TUNNEL', 'SMOOTH MARBLE', 'HALL, CORNER', 'STONE CORRIDOR', 'PATH, TRACKS', 'DEEP PIT', 'DEAD END', 'MINOTAUR TRACKS',
'SMALL CAVERN', 'GREAT STONE', 'DARK CHAMBER', 'NARROW TUNNEL', 'NARROW TWISTING', 'NARROW TWISTING', 'MUSTY, BONES','NORTH, PIT',
'HIGH NARROW', 'FOUL SMELLING', 'NARROW TUNNEL', 'NARROW, CORRIDOR', 'TWISTING, WINDING', 'NARROW WINDING', 'LAIR, DEAD', 'SOUTH,PIT',
'GREAT TUNNEL', 'LARGE CAVERN', 'GREAT STONE', 'TWISTING CORRIDOR', 'CAVERN, BONES', 'WINDING TWISTING', 'LAIR, MINOTAUR', 'SLOPING TRAIL',
'BROKEN BONES', 'LARGE STONE', 'STONE CROSS', 'LARGE WIDE','NARROW PATH', 'BURIED TEMPLE', 'SHALLOW, CAVER', 'GREAT CAVERN',
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
// 192
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
'MAZE', 'MAZE', 'GREAT FOREST', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
]

var GRAPHICS = 
	'<g transform="translate({{x}},{{y}})">'+
	'<rect x="0" y="0" width="150" height="150" fill="{{room_color}}" stroke="black"/>' + 
    '<text x="5" y="15" font-size="10">{{room}}: {{description}}</text>' + 
    '<text x="145" y="15" font-size="10" text-anchor="end" fill="{{enter_fill}}">{{enter}}</text>' +    
    '<rect x="2" y="22" width="75" height="12" fill="{{block_up_fill}}"/>'+
    '<text x="5" y="30" font-size="10">{{U_room}}{{U_action}}</text>' + 
    '<rect x="79" y="22" width="70" height="12" fill="{{block_down_fill}}"/>'+
    '<text x="145" y="30" font-size="10" text-anchor="end">{{D_room}}{{D_action}}</text>' +     
    '<text x="75" y="70" font-size="12" text-anchor="middle" fill="red">{{monsters}}</text>' +     
    '<text x="5" y="45" font-size="10" fill="{{jump_color}}">{{jump}}</text>' + 
    '<rect x="50" y="85" width="95" height="20" fill="{{spell_fill}}"/>' + 
    '<text x="100" y="98" font-size="10" text-anchor="middle" fill="white">{{spell}}</text>' +     
    '<rect x="5" y="85" width="40" height="20" fill="{{oracle_fill}}"/>' + 
    '<text x="8" y="98" font-size="10" fill="white">{{oracle}}</text>' +     
    '<text x="75" y="125" font-size="10" text-anchor="middle" fill="blue">{{objects}}</text>' +
    
    '<line x1="150" y1="75" x2="187.5" y2="75" stroke="{{E_color}}"/>' + 
    '<line x1="0" y1="75" x2="-37.5" y2="75" stroke="{{W_color}}"/>' + 
    '<line x1="75" y1="0" x2="75" y2="-37.5" stroke="{{N_color}}"/>' + 
    '<line x1="75" y1="150" x2="75" y2="187.5" stroke="{{S_color}}"/>' +
    
    '<text x="-40" y="78" text-anchor="end" font-size="10">{{W_room}}</text>' + 
    '<text x="190" y="78" font-size="10">{{E_room}}</text>' + 
    '<text x="75" y="-40" font-size="10" text-anchor="middle">{{N_room}}</text>' + 
    '<text x="75" y="198" font-size="10" text-anchor="middle">{{S_room}}</text>' +
    
    '<text x="80" y="-5" font-size="10">{{N_action}}</text>' + 
    '<text x="80" y="162" font-size="10">{{S_action}}</text>' + 
    '<text x="-5" y="70" font-size="10" text-anchor="end">{{W_action}}</text>' + 
    '<text x="155" y="70" font-size="10">{{E_action}}</text>' +
    
    '<line x1="0" y1="0" x2="150" y2="150" stroke="{{block_1}}"/>' + 
    '<line x1="150" y1="0" x2="0" y2="150" stroke="{{block_2}}"/>' +
    
    '<rect x="-10" y="65" width="20" height="20" fill="{{block_west_fill}}" fill-opacity=".80"/>'+
    '<rect x="140" y="65" width="20" height="20" fill="{{block_east_fill}}" fill-opacity=".80"/>'+
    '<rect y="-10" x="65" width="20" height="20" fill="{{block_north_fill}}" fill-opacity=".80"/>'+
    '<rect y="140" x="65" width="20" height="20" fill="{{block_south_fill}}" fill-opacity=".80"/>'+
    
    '</g>'

function sub(s,dict) {
	for(key in dict) {
		s = s.replace('{{'+key+'}}',dict[key]);
	}
	return s;
}

function readBinaryData(addr) {
	// The first 256 bytes of memory are copied to the screen area at 240 (0x40 here)
	// 00 - FF
	if(addr<0x100) {
		return saveGameData.charCodeAt(addr);
	}
	// 240 - 600
	if(addr>=0x240 && addr<0x600) {
		return saveGameData.charCodeAt(addr-0x240);
	}
	// 3BC1
	if(addr>=0x3BC1) {
		return saveGameData.charCodeAt(addr-0x3BC1+0x3C0);
	}
}


function getRoomDoors(rn) {
	var d = binaryData.read(0x3DB8+rn);
	//--UDNEWS
	ret = '--';
	if((d&32) != 0) ret=ret+'U';
	else ret=ret+'-';
	if((d&16) != 0) ret=ret+'D';
	else ret=ret+'-';
	if((d&8) != 0) ret=ret+'N';
	else ret=ret+'-';
	if((d&4) != 0) ret=ret+'E';
	else ret=ret+'-';
	if((d&2) != 0) ret=ret+'W';
	else ret=ret+'-';
	if((d&1) != 0) ret=ret+'S';
	else ret=ret+'-';
	return ret;		
}

function getNeighborRoomNumber(rn,dir) {
	if(dir=='U') rn = rn - 64;
	else if(dir=='D') rn = rn + 64;
	else if(dir=='W') rn = rn - 1;
	else if(dir=='E') rn = rn + 1;
	else if(dir=='N') rn = rn - 8;
	else if(dir=='S') rn = rn + 8;
	if(rn>256) rn=rn-256;
	if(rn<0) rn=rn+256;
	return rn;
}

var BETWEEN_ROOM_ACTIONS = {
		0x1AFB : 'A',
		0x1B20 : 'B',
		0x1B03 : 'C',
		0x1B06 : 'D',
		0x1B09 : 'E',
		0x1B34 : 'F',
		0x1B5F : 'G',
		0x1B43 : 'H',
		0x1B4A : 'I'
}

var DIRS = {
		1 : 'S',
		2 : 'W',
		4 : 'E',
		8 : 'N',
		16 : 'D',
		32 : 'U'
}

var OPPOSITE_DIR = {'U':'D', 'D':'U', 'N':'S', 'E':'W', 'W':'E', 'S':'N'};

function getBetweenRoomAction(rn,dir) {
	var p = 0x3B4A;
	while(true) {		
		var a = binaryData.read(p);
		var b = binaryData.read(p+1);
		if(b==0) break;
		b = DIRS[b];
		var c = binaryData.read(p+2)*256 + binaryData.read(p+3);
		p += 4;	
		if((rn==a) && (dir==b)) {		
			a = BETWEEN_ROOM_ACTIONS[c];
			if(a=='A' || a=='C' || a=='D' || a=='E') {
				// These actions only trigger in the UP direction.
				// Strangely they appear on a few passages in other
				// directions. They could never trigger. We'll leave
				// them off the map.			
				if(dir!='U') continue;
			}
			return a;
		}		
	}
	// Just like the code ... run the list in the opposite travel direction
	var p = 0x3B4A;
	while(true) {
		var a = binaryData.read(p);
		var b = binaryData.read(p+1);
		if(b==0) break;
		b = DIRS[b];
		var c = binaryData.read(p+2)*256 + binaryData.read(p+3);
		p += 4;	
		a = getNeighborRoomNumber(a,b);
		b = OPPOSITE_DIR[b];
		if( (rn==a) && (dir==b)) {
			a = BETWEEN_ROOM_ACTIONS[c];
			if(a=='A' || a=='C' || a=='D' || a=='E') {
				// These actions only trigger in the UP direction.
				// Strangely they appear on a few passages in other
				// directions. They could never trigger. We'll leave
				// them off the map.			
				if(dir!='U') continue;
			}
			return a;
		}		
	}
	return '';
}

function isEdge(rn,dir) {
	fn = ~~(rn / 64);
	x = (rn%64)%8;
	y = ~~((rn%64)/8);
	if(dir=='U') {
		return fn==0;
	} else if(dir=='D') {
		return fn==3;
	} else if(dir=='N') {
		return y==0;
	} else if(dir=='E') {
		return x==7;
	} else if(dir=='W') {
		return x==0;
	} else if(dir=='S') {
		return y==7;
	}	
}

JUMPS = [
	[143, "PIT",   151, 128,  'D'],
	[151, "PIT",   143, 128,  'F'],
	[16,  "POOL",  7,   128,  'F'],
	[17,  "POOL",  16,  128,  'F'],
	[78,  "CHASM", 86,  64,   'F'],
	[86,  "CHASM", 78,  64,   'F'],
	[44,  "PIT",   182, 10,   'S(10)'],
	[182, "PIT",   44,  20,   'S(20)'],
	[164, "PIT",   202, 160,  'D'],
	[133, "PIT",   203, 192,  'F'],
	[144, "",      133, 20,   'S(20)'],
	[203, "PIT",   202, 128,  'S(30)'],
	[213, "MIST",  212, 70,   'S(20)'],
	[212, "MIST",  213, 70,   'S(20)'],
	[35,  "HOLE",  34,  150,  'S(40)'],
	[34,  "PIT",   35,  120,  'S(20)'],
	[128, "UP",    64,  100,  'F'],
	[166, "UP",    102, 80,   'F'],
	[102, "UP",    38,  160,  'F'],
	[92,  "DOWN",  156, 150,  'S(30)'],
	[70,  "DOWN",  140, 80,   'S(20)'],
	[94,  "DOWN",  158, 90,   'S(10)'],
	[64,  "PIT",   128, 30,   'D'],
	[202, "DOWN",  162, 30,   'S(20)'],
	// Source address assigned along with enter-room-203 (small pit)
	[-1,  "JUMP DOWN", 39,140,'F']
]

function getJump(rn) {
	var i;
	for(i=0;i<JUMPS.length;++i) {
		if(JUMPS[i][0]==rn) {
			return 'Jump:' + JUMPS[i][1]+':'+JUMPS[i][2]+':'+JUMPS[i][3]+':'+JUMPS[i][4];			
		}
	}
	return '';
}

var saveGameData = [];
var SPELL_INFO = [
	{name: 'VETRA',   learned: false, room: -1},
	{name: 'MITRA',   learned: false, room: -1},
	{name: 'OKKAN',   learned: false, room: -1},
	{name: 'AKHIROM', learned: false, room: -1},
	{name: 'NERGAL',  learned: false, room: -1},
	{name: 'BELROG',  learned: false, room: -1},
	{name: 'CROM',    learned: false, room: -1},
	{name: 'ISHTAR',  learned: false, room: -1}		
]
function getSpell(rn) {
	ret = '';
	for(var i=0;i<8;++i) {
		if(SPELL_INFO[i].room==rn && SPELL_INFO[i].learned==false) {
			ret = ret + SPELL_INFO[i].name+',';			
		}
	}
	return ret;
}

var OBJECTS = [];
var OBJECT_NAMES = [
	"FOOD",	"BOTTLE", "DAGGER", "MACE", "AX", "SWORD", "SHIELD", "FLUTE", "MUSHROOM", "PENDANT", "SCEPTER", "LAMP",
	"BASKET", "PARCHMENT", "VIAL", "URN", "TALISMAN", "SCROLL", "GOBLET", "SKULL", "SCARAB", "JEWELBOX", "TABLET", "ROPE",	
	"SPRITE", "TROGLODYTE", "SCORPION", "NYMPH", "SATYR", "MINOTAUR",
	"ORACLE",	
	"GOLD", "SILVER", "DIAMOND", "SPELLBOOK", "RUBY", "FLEECE", "TIARA", "POWDER", "AMULET", "POTION", "POWERRING", 
	"LIGHTRING","TRUTHRING", "CROWN", "OPAL", "SAPPHIRE"
]
function getObjectsInRoom(rn) {	
	ret = '';
	for(var i=0;i<OBJECTS.length;++i) {
		o = OBJECTS[i];
		if(o['in_pack'] || o['spell_creature'] || !o['accessible']) continue;
		if(o['room']==rn) {
			if(o['protected']) ret = ret + '*';
			ret = ret + o['name']+',';
		}		
	}
	return ret;
}
function getMonstersInRoom(rn) {
	ret = '';
	for(var i=0;i<OBJECTS.length;++i) {
		o = OBJECTS[i];
		if(!o['spell_creature'] || !o['accessible']) continue;
		if(o['name']=='ORACLE') continue;
		if(o['room']==rn) {
			ret = ret + o['name']+',';
		}		
	}
	return ret;
}
function isOracleInRoom(rn) {
	for(var i=0;i<OBJECTS.length;++i) {
		o = OBJECTS[i];
		if(o['name']!='ORACLE') continue;
		if(o['room']==rn) {
			return true;
		}		
	}
	return false;
}

function truncList(s) {
	if(s.endsWith(',')) s=s.substring(0,s.length-1);
	return s;
}

ENTER_ROOM_ACTIONS = {
	0x1B6D:'_a',
	0x1B70:'_b',
	0x1B73:'_c',
	0x1B9C:'_d',
	0x1BB3:'_e',
	0x1BB7:'_f',
	0x1BF9:'_g',
	0x1C15:'_h',
	0x1C2C:'_i',
	0x1C2F:'_j',
	0x1C32:'_k',
	0x1C35:'_l',
	0x1C38:'_m',
	0x1C3B:'_n',
	0x1C3E:'_o',
	0x1C41:'_p',
	0x1C68:'_q',
	0x1C7A:'_r',
	0x1C8D:'_s',
	0x1CA9:'_t',
	0x1CCC:'_u',
	0x1CF0:'_v',
	0x1D00:'_x',
	0x1D22:'_203',
	0x1D27:'_213',
	0x1CE0:'_32',
	0x1CD6:'_33',
	0x1BB4:'_z',
	0x1D2D:'_232'
}

function getEnterRoomAction(rn) {
	ret = '';
	// These are hardcoded -- even if there is no save game
	if(rn==203) return '_203';
	if(rn==213) return '_213';
	if(rn==32) return '_32';
	if(rn==33) return '_33';
	if(rn==232) return '_232';	
	for(var i=0;i<36;++i) {
		if(readBinaryData(0x3C8F+i*3)==rn) {
			var a = readBinaryData(0x3C8F+i*3+1)*256 + readBinaryData(0x3C8F+i*3+2);
			ret = ret + ENTER_ROOM_ACTIONS[a]+',';
		}
	}
	return ret;
}

function findRawTextLine(lines,addr,i) {
	while(true) {
		if(lines[i].startsWith(addr+':')) {
			return i;
		}
		++i;
	}
}

function hexPad(val,n) {
	ret = val.toString(16).toUpperCase();
	while(ret.length<n) {
		ret = '0' + ret;
	}
	return ret;
}

function getReplaceTarget(s) {
	var i = s.indexOf('{{');
	var j = s.indexOf('}}');
	return s.substring(i+2,j);
}

function doReplaceTarget(s,k,v) {
	return s.replace('{{'+k+'}}',v);
}

//ASCII to CoCo screen printable
var CHARMAP = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
			  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
			  "@ABCDEFGHIJKLMNOPQRSTUVWXYZ[~]~~"+
			  "_!\"#$%&'()*+,-./0123456789:;<=>?"+
			  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
			  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
			  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+
			  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~";

var NAMETABLE = {
	0x19 : 'Sprite',
	0x1A : 'Troglodyte',
	0x1B : 'Scorpion',
	0x1C : 'Nymph',
	0x1D : 'Satyr',
	0x1E : 'Minotaur',
	0x01 : 'Crypt',
	0x02 : 'Crypt of kings',
	0x03 : 'Enter-room-action _u',
	0x04 : 'Enter-room-action _33',
	0x05 : 'Small pit',
	0x06 : 'Ledge',
	0x07 : 'Hydra',
	0x08 : 'Pile of glowing rocks',
	0x09 : 'Eerie glow',
	0x0A : 'Packrat',
	0x0B : 'Enter-room-action _r',
}

var PROTECTIONS = {
  0x1A: {
	  name : 'TROGLODYTE',
	  items : [
		  '45 0B 38 FF ; AX, SCEPTER, MITRA',
		  '23 7D FF ; SPELLBOOK, CROM',
		  '43 07 3B FF ; DAGGER, SHIELD, NERGAL'
	  ]
  },
  0x1D: {
	  name : 'SATYR',
	  items : [
  '46 3B FF ; SWORD, NERGAL',
  '44 2B 38 FF ; MACE, LIGHTRING, MITRA',
  '23 77 FF ; SPELLBOOK, VETAR',
	  ]
  },
  0x1E: {
	  name : 'MINOTAUR',
	  items : [
  '46 07 2A FF ; SWORD, SHIELD, POWERRING',
  '44 0F 0B 38 FF ; MACE, VIAL, SCEPTER, MITRA',
  '45 3B FF ; AX, NERGAL',
	  ]
  },
  0x1B: {
	  name : 'SCORPION',
	  items : [
  '48 3B FF ; FLUTE, NERGAL',
  '14 3D FF ; SKULL, CROM',
  '51 2A FF ; TALISMAN, POWERRING',
	  ]
  },
  0x1C: {
	  name : 'NYMPH',
	  items : [
  '49 2C FF ; MUSHROOM, TRUTHRING',
  '41 0A FF ; FOOD, PENDANT',
  '48 39 FF ; FLUTE, OKKAN',
	  ]
  },
  0x19 : {
	  name : 'SPRITE',
	  items : [
  '54 2A FF ; SKULL, POWERRING',
  '41 3B FF ; FOOD, NERGAL',
  '43 3A FF ; DAGGER, AKHIROM',
	  ]
  },
  0x06: {
	  name : 'SWORD',
	  items : [
  '18 FF ; ROPE',
  '38 FF ; MITRA',
  '0E FF ; PARCHMENT',
	  ]
  },
  0x0F: {
	  name : 'VIAL',
	  items : [
  '09 77 FF ; MUSHROOM, VETAR',
  '0E 38 FF ; PARCHMENT, MITRA',
  '11 38 FF ; TALISMAN, MITRA',
	  ]
  },
  0x07: {
	  name : 'SHIELD',
	  items : [
  '06 FF ; SWORD',
  '04 FF ; MACE',
  '03 FF ; DAGGER',
	  ]
  },
  0x14: {
	  name : 'SKULL',
	  items : [
  '11 0A FF ; TALISMAN, PENDANT',
  '39 FF ; OKKAN',
  '0B FF ; SCEPTER',
	  ]
  },
  0x2A: {
	  name : 'POWERRING',
	  items : [
  '7C FF ; BELROG',
  '07 0B 0E 79 FF ; SHIELD, SCEPTER, PARCHMENT, OKKAN',
  '07 04 14 78 FF ; SHIELD, MACE, SKULL, MITRA',
  '07 06 7A F ; SHIELD, SWORD, AKHIROM',
	  ]
  },
  0x2B: {
	  name : 'LIGHTRING',
	  items : [
  '2A 7D 11 FF ; POWERRING, CROM, TALISMAN',
  '2A 05 39 FF ; POWERRING, AX, OKKAN',
  '2A 18 7B FF ; POWERRING, ROPE, NERGAL',
	  ]
  },
  0x2C: {
	  name : 'TRUTHRING',
	  items : [
  '2B 7D 0D FF ; LIGHTRING, CROM, BASKET',
  '2B 05 39 FF ; LIGHTRING, AX, OKKAN',
  '2B 08 7A FF ; LIGHTRING, FLUTE, AKHIROM',
	  ]
  },
  0x23: {
	  name : 'SPELLBOOK',
	  items : [
  '14 08 FF ; SKULL, FLUTE',
  '0A 7D FF ; PENDANT, CROM',
  '09 13 7C FF ; MUSHROOM, GOBLET, BELROG',
  '2A 7B FF ; POWERRING, NERGAL',
	  ]
  }
}

function viewSaveFile(data) {
	
	// Reset from last viewing (if any)
	for(var i=0;i<8;++i) {
		SPELL_INFO[i].room = -1;		
		SPELL_INFO[i].learned = false;
	}	
	// Reset jump
	JUMPS[24][0] = -1;
	// Reset current and last room
	PLAYER = -1;
	LAST_ROOM = -1;
	// Reset objects
	OBJECTS = [];
	
	saveGameData = atob(data);
	
	if(saveGameData.length>0) {
		// Read the SPELL information
		for(i=0;i<8;++i) {
			SPELL_INFO[i].room = readBinaryData(0x3BC1+4*i+2);		
			if(readBinaryData(0x3BC1+4*i+3)!=0) { 
				SPELL_INFO[i].learned = true;
			}
		}
		// The random jump (last in the list)
		JUMPS[24][0] = readBinaryData(0x3C59);
		// Player
		PLAYER = readBinaryData(0);
		LAST_ROOM = readBinaryData(1);
		// Objects
		for(var x=0;x<OBJECT_NAMES.length;++x) {
			var co = {'name' : OBJECT_NAMES[x]};
			OBJECTS.push(co);
			co['room'] = readBinaryData(0x3CFC+x*3+0);
			var bits = readBinaryData(0x3CFC+x*3+2);
			co['in_pack'] = (bits&0x80)!=0;
			co['spell_creature'] = (bits&0x40)!=0;
			co['required'] = (bits&0x20)!=0;
			co['protected'] = (bits&0x10)!=0;
			co['fill_status'] = (bits>>2)&3;
			co['dead_creature'] = (bits&0x2)!=0;
			co['accessible'] = (bits&0x1)==0;			
		}
		$('#rawData').show();
		
		// Template for the raw data
		var rawt = $('#rawData').html().split('\n');
		
		// Fill out the engine memory (1 or 2 bytes)
		i = findRawTextLine(rawt,'0000',0);
		j = findRawTextLine(rawt,'0340',i);
		while(i!=j) {
			g = rawt[i];
			if(g[0]!='0') {
				++i;
				continue;
			}
			p = parseInt(g.substring(0,4),16);
			a = readBinaryData(p);
			b = readBinaryData(p+1);			
			k = getReplaceTarget(g);
			if(k=='value1') {
			  g = doReplaceTarget(g,k,hexPad(a,2));
			  if(p<0xFF) {
				  g = doReplaceTarget(g,'value2',hexPad(b,2));
			  }
			  if(a>127) {
				  a = a -256;
			  }
			  a = a + 128;
			  a = ''+a;
			  while(a.length<3) a=a+' ';
			  g = doReplaceTarget(g,'decode','Room '+a);			  
			} else {
				// Must be mvalue_NN
				m = k.indexOf('_');
				z = parseInt(k.substring(m+1));
				s = '';
				while(z>0) {
					s = s + hexPad(readBinaryData(p),2)+' ';
					++p;
					--z;
				}
				g = doReplaceTarget(g,k,s)
			}
									
			rawt[i] = g;
			++i;
		}
		
		// Saved screen
		i = findRawTextLine(rawt,'0340',0);
		j = findRawTextLine(rawt,'3BC1',i);
		
		while(i!=j) {
			g = rawt[i];
			if(g[0]!='0') {
				++i;
				continue;
			}
			p = parseInt(g.substring(0,4),16);			
			
			s = '';
			t = '';
			for(x=0;x<32;++x) {
				s = s + hexPad(readBinaryData(p+x),2)+' ';
				t = t + CHARMAP[readBinaryData(p+x)];
			}
			
			g = doReplaceTarget(g,'value',s);
			rawt[i] = doReplaceTarget(g,'decode',t);
			++i;
		}
						
		// Spells
		p = 0x3BC1;
		for(j=0;j<8;++j) {
			g = rawt[i];
			a = readBinaryData(p+2);
			b = readBinaryData(p+3);
			g = doReplaceTarget(g,'value1',hexPad(a,2));
			g = doReplaceTarget(g,'value2',hexPad(b,2));
						dec = 'Room '+a+' ';
			if(b==0) {
				dec = dec + '(unlearned)';
			} else {
				dec = dec + '(LEARNED)';
			}
			rawt[i] = doReplaceTarget(g,'decode',dec);
			++i;
			p = p + 4;
		}
				
		// Jump info
		i = findRawTextLine(rawt,'3C59',i);
		g = rawt[i];
		a = readBinaryData(0x3C59);		
		rn = ""+a;
		while(rn.length<3) rn=rn+' ';
		
		g = doReplaceTarget(g,'value',hexPad(a,2));
		rawt[i] = doReplaceTarget(g,'decode',rn);
				
		// Who holds what
		i = findRawTextLine(rawt,'3C6F',i);
		p = 0x3C6F;
		for(j=0;j<16;++j) {
			g = rawt[i];
			a = readBinaryData(p);
			g = doReplaceTarget(g,'value',hexPad(a,2));			
			g = doReplaceTarget(g,'decode', NAMETABLE[a]);
			rawt[i] = g;
			++i;
			p = p + 2;
		}		
		
		// Enter Room Actions
		i = findRawTextLine(rawt,'3C8F',i);
		j = findRawTextLine(rawt,'3CFB',i);
		
		while(i!=j) {
			g = rawt[i];
			if(g[0]!='3') {
				++i;
				continue;
			}
			p = parseInt(g.substring(0,4),16);
			
			a = readBinaryData(p);
			g = doReplaceTarget(g,'value',hexPad(a,2));
			rn = ''+a;
			while(rn.length<3) rn=rn+' ';
			rawt[i] = doReplaceTarget(g,'decode',rn);
			++i;			
		}
		
		// Objects
		i = findRawTextLine(rawt,'3CFC',i);
		j = findRawTextLine(rawt,'3DB6',i);		
		while(i!=j) {
			g = rawt[i];
			if(g[0]!='3') {
				++i;
				continue;
			}
			p = parseInt(g.substring(0,4),16);
			
			a = readBinaryData(p);
			b = readBinaryData(p+2);		
			
			rn = ''+a;
						
			dec = 'Room '+rn;
			if((b&0x80)>0) {
				dec = dec + ', in backpack';
			} 
			if((b&0x40)>0) {
				dec = dec + ', spell or creature';
			} 
			if((b&0x20)>0) {
				dec = dec + ', required';
			} 
			if((b&0x10)>0) {
				dec = dec + ', protected';
			} 
			dec = dec + ', fill status '+((b>>2)&3);
			if((b&0x2)>0) {
				dec = dec + ', spell or dead creature';
			} 
			if((b&0x1)>0) {
				dec = dec + ', carried object or creature';
			} 
						
			g = doReplaceTarget(g,'value1',hexPad(a,2));
			g = doReplaceTarget(g,'value2',hexPad(b,2));
			
			rawt[i] = doReplaceTarget(g,'decode',dec);			
			++i;			
		}
		
		// Blocked passages
		i = findRawTextLine(rawt,'3EB8',i);
		j = findRawTextLine(rawt,'3FB8',i);		
		while(i!=j) {
			g = rawt[i];
			if(g[0]!='3') {
				++i;
				continue;
			}
			p = parseInt(g.substring(0,4),16);
			
			s = '';
			t = '';
			for(x=0;x<8;++x) {
				a = readBinaryData(p+x);
				s = s + hexPad(a,2)+' ';
				if((a&32)>0) {t=t+'U';} else {t=t+'.';}
				if((a&16)>0) {t=t+'D';} else {t=t+'.';}
				if((a&8)>0) {t=t+'N';} else {t=t+'.';}
				if((a&4)>0) {t=t+'E';} else {t=t+'.';}
				if((a&2)>0) {t=t+'W';} else {t=t+'.';}
				if((a&1)>0) {t=t+'S';} else {t=t+'.';}
				t = t + ' ';
			}
			
			rawt[i] = doReplaceTarget(g,'mvalue',s+'; '+t);
			++i;
		}
		
		// Protection lists
		g = rawt.pop(); 
		rawt.pop(); // The placeholder address 3FB8:
		
		p = 0x3FB8;		
		for(x=0;x<14;++x) {
			u = hexPad(p,4)+': '
			b = readBinaryData(p++);
			u = u + hexPad(b,2);
			while(u.length<22) u = u +' ';			
			ob = PROTECTIONS[b];
			u = u + '; '+ob.name;
			if(x==0) u = '<span class="sg_value">'+ u;
			rawt.push(u);
			s = '';
			u = hexPad(p,4)+': ';
			while(true) {
				a = readBinaryData(p++);
				s = s + hexPad(a,2)+' ';
				if(a==0xFF) break;
			}
			u=u+s;
			for(y=0;y<ob.items.length;++y) {
				if(ob.items[y].startsWith(s)) {
					s = ob.items[y];
					break;
				}
			}
			while(u.length<22) u=u+' ';
			z = s.indexOf(';');
			u = u + ';    ' + s.substring(z+1);
			rawt.push(u);
		}
		
		rawt.push(hexPad(p++,4)+': FF')
		
		if(p!=0x4000) {
			rawt.push('; Unused');
			u = hexPad(p,4)+':';
			while(p<0x4000) u = u + ' ' + hexPad(readBinaryData(p++),2);
			rawt.push(u);
		}
		
		rawt.push('<\span>');
		rawt.push(g);
		
		// Write the data
		g ='';
		for(i=0;i<rawt.length;++i) {
			g = g + rawt[i]+'\n';
		}
		$('#rawData').html(g);
		
	} else {
		$('#rawData').hide();
	}	
	
	// Fix scrolling for the map
	$('.content div').css('overflow','unset');
	
	var g = '<g transform="scale(0.70)">';
	var rn;
	var fn;
	var x,y,color;
	
	
	for(rn=0;rn<256;++rn) {
		fn = ~~(rn / 64);
		x = (rn%64)%8;
		y = ~~((rn%64)/8);
		
		subs = {
			x:(150+75)*x+100,
			y:(150+75)*y+100+2000*fn,
			description:ROOM_DESC[rn],
			room:rn,
			room_color: '#EEE',
			enter:'',
			enter_fill: 'red',
			up:'',
			down:'',
			monsters: '',
			jump_color:'black',
			jump:'',
			spell_fill: 'none', // 'green'
			spell: '',
			oracle_fill: 'none', // 'blue'
			oracle: '', // 'Oracle'
			objects:'',
			E_color: 'none',
			W_color: 'none',
			N_color: 'none',
			S_color: 'none',
			U_room: '',
			D_room: '',
			E_room: '',
			W_room: '',
			N_room : '',
			S_room : '',
			U_action : '',
			D_action : '',
			N_action : '',
			S_action : '',			
			E_action : '',
			W_action : '',
			block_1 : 'none',
			block_2 : 'none',
			block_up_fill : 'none',
			block_down_fill : 'none',
			block_north_fill : 'none',
			block_south_fill : 'none',
			block_east_fill : 'none',
			block_west_fill : 'none',
		}
					
		// Maze rooms colored differently
		if(ROOM_DESC[rn] == 'MAZE') {
			subs['room_color'] = '#CCC';
		}
		
		// Jumps
		var jump = getJump(rn);
		subs['jump'] = jump;
		if(jump==JUMPS[24]) {
			subs['jump_color'] = 'red';
		}
		
		// Passages and passage-actions
		var doors = getRoomDoors(rn);		
		var dirs = 'UDNEWS';				
		for(var i=0;i<dirs.length;++i) {
			var c = dirs[i];
			var ndn = getNeighborRoomNumber(rn,c);
			var action = getBetweenRoomAction(rn,c);
			if( (c=='U' || c=='D')) {
				// Up and Down actions need a colon
				if(action!='') {
					action = ':'+action;
				}
				//if(ndn!='') {
					if(c=='U') {
						ndn = 'Up:'+ndn;
					} else {
						ndn = 'Down:'+ndn;
					}
				//}
			}			
			if(doors.indexOf(c)>=0) {					
				subs[c+'_action'] = action;
				if(c=='U' || c=='D' || isEdge(rn,c)) {
					subs[c+'_room'] = ndn;
				}
				subs[c+'_color'] = 'black';				
			} 			
		}
		
		// Spells
		subs['spell'] = truncList(getSpell(rn));
		if(subs['spell']!='') {
			subs['spell_fill'] = 'green';
		}
		
		// Player and last room (might be the same)
		if(rn==LAST_ROOM) {
			subs['room_color'] = '#EFE';
		}
		if(rn==PLAYER) {
			subs['room_color'] = '#CFC';
		}
		
		// Objects
		subs['objects'] = truncList(getObjectsInRoom(rn));
		
		// Monsters
		subs['monsters'] = truncList(getMonstersInRoom(rn));
		
		// Oracle
		if(isOracleInRoom(rn)) {
			subs['oracle'] = 'Oracle';
			subs['oracle_fill'] = 'blue';
		}		
		
		// Enter room actions		
		if(rn==213 || rn==32 || rn==33 || rn==203 || rn==232) {
			// These are fixed ... every game the same
			subs['enter_fill'] = 'black';
		}
		subs['enter'] = truncList(getEnterRoomAction(rn));
		
		// Blocked passages
		
		var bits = readBinaryData(0x3EB8+rn);
		if(bits&0x20) subs['block_up_fill'] = '#FCC';
		if(bits&0x10) subs['block_down_fill'] = '#FCC';
		if(bits&0x08) subs['block_north_fill'] = '#FCC';
		if(bits&0x04) subs['block_east_fill'] = '#FCC';
		if(bits&0x02) subs['block_west_fill'] = '#FCC';
		if(bits&0x01) subs['block_south_fill'] = '#FCC';
				
		// TODO data breakdown after map (put it in the HTML but hidden ... fill out and show)		
		// TODO ability to pass in file in URL
		
		g = g + sub(GRAPHICS,subs);		
			
	}
	
	// Floor dividers
	for(y=1;y<4;++y) {
		g = g + '<line x1="30" y1="'+(y*2000-35)+'" x2="1900" y2="' + (y*2000-35)+'" stroke="black"/>';
	}	
	
	g = g + '</g>';
	
	$('#svg').html(g);		
	
}

$(function() {
	var loc = window.location.toString();
	var i = loc.indexOf('?');
	if(i<0) return; // Nothing to load
	
	loc = loc.substring(i+1);
	$.get(loc,function(data) {
		$('#cocoTape').val(data);
		viewSaveFile(data);
	});
	
});

