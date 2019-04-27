var ROOM_DESC = [
'STONE TOWER', 'EMPTY ROOM', 'GUARD ROOM', 'PILE OF BONES', 'CLEAN ROOM', 'TROPHY ROOM', 'EMPTY CLOSET', 'SLOPING SHAFT',
// 8
'MARBLE FLOOR', 'NARCISSUS PLANTS', 'TABLE AND CHAIR', 'PAINTING', 'BROKEN GLASS', 'BROKEN TILES', 'BED ROOM', 'NO WINDOWS',
// 16
'WEST, POOL', 'EAST, POOL', 'SMALL LIBRARY', 'ANCIENT CARVINGS', 'GREEN MARBLE', 'WINE CELLAR', 'THE KING', 'MIST SWIRLING',
// 24
'WIDE HALL', 'MARBLE PORTAL', 'ROYAL COURT', 'VOICES, DEAD', 'DARK CHAMBER', 'GREEN MIST', 'BROKEN SHADOW', 'CEILING, SLOPING',
// 32
'TWISTING STAIR', 'DARK, TOWER', 'SUNKEN PIT', 'SERVANT CHAMBER', 'PANTRY', 'GREAT BEER', 'EMPTY CHAMBER', 'TEMPLE OF ZEUS',
// 40
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE, PIT', 'MAZE', 'MAZE', 'MAZE',
// 48
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
// 56
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',

// 64
'GREAT PIT', 'STONE WALL', 'SMALL ROOM', 'GREAT CRYPT', 'BONES, WALL', 'CHILL MIST', 'FOUL SMELLING', 'STONE SHAFT',
// 72
'HALL, COURT', 'EMPTY CHAMBER', 'LARGE POOL','LARGE CAVERN', 'TWISTING PASSAGE', 'SHALLOW HOLE', 'CHASM,SOUTH', 'STONE, CARVINGS',
// 80
'TWISTING MUSTY', 'SUNKEN ROOM', 'CHILL DAMP', 'CAVERN, STONE', 'WINDING PASSAGE', 'TWISTING WINDING', 'SMALL CHAMBER', 'SHALLOW PIT',
// 88
'MUSTY, CORRIDOR', 'EDGE, SHAFT', 'TOMB, SKULL', 'STONE TILES', 'WIDE ROOM', 'WOOD PASSAGE', 'WIDE HALL', 'STONE TUNNEL',
// 96
'MUSTY PASSAGE', 'TWISTING PASSAGE', 'BROKEN PASSAGE', 'BROKEN STONE', 'STONE CHAPEL', 'LONG PASSAGE', 'ANCIENT KING', 'CAVE, VOICES',
// 104
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
// 112
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
// 120
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',

// 128
'NARROW TUNNEL', 'SMOOTH MARBLE', 'HALL, CORNER', 'STONE CORRIDOR', 'PATH, TRACKS', 'DEEP PIT', 'DEAD END', 'MINOTAUR TRACKS',
// 136
'SMALL CAVERN', 'GREAT STONE', 'DARK CHAMBER', 'NARROW TUNNEL', 'NARROW TWISTING', 'NARROW TWISTING', 'MUSTY, BONES','NORTH, PIT',
// 144
'HIGH NARROW', 'FOUL SMELLING', 'NARROW TUNNEL', 'NARROW, CORRIDOR', 'TWISTING, WINDING', 'NARROW WINDING', 'LAIR, DEAD', 'SOUTH,PIT',
// 152
'GREAT TUNNEL', 'LARGE CAVERN', 'GREAT STONE', 'TWISTING CORRIDOR', 'CAVERN, BONES', 'WINDING TWISTING', 'LAIR, MINOTAUR', 'SLOPING TRAIL',
// 160
'BROKEN BONES', 'LARGE STONE', 'STONE CROSS', 'LARGE WIDE','NARROW PATH', 'BURIED TEMPLE', 'SHALLOW, CAVER', 'GREAT CAVERN',
// 168
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
// 176
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
// 184
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',

// 192
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
// 200
'MAZE', 'MAZE', 'GREAT FOREST', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 
// 208
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
// 216
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
// 224
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
// 232
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
// 240
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
// 248
'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE', 'MAZE',
]

var FRAGS = {
		'roomStart' : '<g transform="translate({{x}},{{y}})">'+
		                '<rect x="0" y="0" width="150" height="150" fill="{{color}}" stroke="black"/>'+
		                '<text x="5" y="15" font-size="10">{{room_num}}: {{room_desc}}</text>',
		'roomEnd' : '</g>',
		
		'floorSep'  : '<line x1="100" y1="{{y1}}" x2="1825" y2="{{y2}}" stroke="gray"/>',
		
		'doorUp' : '<text x="5" y="30" font-size="10">Up:{{target}}{{action}}</text>',
		'doorDown': '<text x="145" y="30" font-size="10" text-anchor="end">Down:{{target}}{{action}}</text>', 
		
		'passageTwoWayU' : '<text x="5" y="30" font-size="10">Up:{{target}}{{action}}</text>',	
		'passageTwoWayTargetU' : '',
		'passageTwoWayD' : '<text x="145" y="30" font-size="10" text-anchor="end">Down:{{target}}{{action}}</text>',
		'passageTwoWayTargetD' : '',
		'passageTwoWayN' : '<line x1="{{n_x1}}" y1="{{n_y1}}" x2="{{n_x2}}" y2="{{n_y2}}" stroke="black"/>',
		'passageTwoWayTargetN' : '<text x="{{n_tx}}" y="{{n_ty}}" text-anchor="middle">{{action}}</text>',
		'passageTwoWayS' : '<line x1="{{s_x1}}" y1="{{s_y1}}" x2="{{s_x2}}" y2="{{s_y2}}" stroke="black"/>',
		'passageTwoWayTargetS' : '<text x="{{s_tx}}" y="{{s_ty}}" text-anchor="middle">{{action}}</text>',	
		'passageTwoWayE' : '<line x1="{{e_x1}}" y1="{{e_y1}}" x2="{{e_x2}}" y2="{{e_y2}}" stroke="black"/>',
		'passageTwoWayTargetE' : '<text x="{{e_tx}}" y="{{e_ty}}">{{action}}</text>',
		'passageTwoWayW' : '<line x1="{{w_x1}}" y1="{{w_y1}}" x2="{{w_x2}}" y2="{{w_y2}}" stroke="black"/>',
		'passageTwoWayTargetW' : '<text x="{{w_tx}}" y="{{w_ty}}" text-anchor="end">{{action}}</text>',		
		
		'neighborNumberU' : '',
		'neighborNumberD' : '',
		'neighborNumberN' : '<text x="{{ns_rtx}}" y="{{n_rty}}" text-anchor="middle">{{target}}</text>',
		'neighborNumberE' : '<text x="{{e_rtx}}" y="{{ew_rty}}">{{target}}</text>',
		'neighborNumberW' : '<text x="{{w_rtx}}" y="{{ew_rty}}" text-anchor="end">{{target}}</text>',
		'neighborNumberS' : '<text x="{{ns_rtx}}" y="{{s_rty}}" text-anchor="middle">{{target}}</text>',
		
}

function sub(s,dict) {
	for(key in dict) {
		s = s.replace('{{'+key+'}}',dict[key]);
	}
	return s;
}

binaryData = makeBinaryDataMadness();

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
			return BETWEEN_ROOM_ACTIONS[c];
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
			return BETWEEN_ROOM_ACTIONS[c];
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

function viewSaveFile(data) {
	
	data = atob(data);
	
	// Fix scrolling for the map
	$('.content div').css('overflow','unset');
	
	var g = '<g transform="scale(0.70)">';
	var rn;
	var fn;
	var x,y,color;
	var shown = [];
	for(rn=0;rn<256;++rn) {
		fn = ~~(rn / 64);
		x = (rn%64)%8;
		y = ~~((rn%64)/8);
		
		color = '#EEE';
		if(ROOM_DESC[rn] == 'MAZE') {
			color = '#CCC';
		}
	
		subs = {
				x:(150+75)*x+100,
				y:(150+75)*y+100+2000*fn,
				color:color,
				room_num:rn,
				room_desc:ROOM_DESC[rn]
		}
				
		g = g + sub(FRAGS.roomStart,subs);		
		
		var doors = getRoomDoors(rn);
		
		var dirs = 'UDNEWS';		
		subs = {
			'n_x1' : 75,  'n_y1' : 0,   'n_x2' : 75,   'n_y2' : -38,
			's_x1' : 75,  's_y1' : 150, 's_x2' : 75,   's_y2' : 188,			
			'e_x1' : 150, 'e_y1' : 75,  'e_x2' : 188,  'e_y2' : 75,
			'w_x1' : 0,   'w_y1' : 75,  'w_x2' : -38,  'w_y2' : 75,
			'n_rty' : -42, 's_rty' : 192, 'e_rtx' : 192, 'w_rtx' : -42,
			'ns_rtx' : 75, 'ew_rty' : 80,
			'n_tx' : 85,  'n_ty' : -38,
			's_tx' : 85,  's_ty' : 188,
			'e_tx' : 183, 'e_ty' : 90,
			'w_tx' : -33, 'w_ty' : 90,
		}
		for(var i=0;i<dirs.length;++i) {
			// TODO keep track of actions show between grid rooms and only show them once
			// TODO on grid edges, show the actions like other grid rooms (not part of room number like Up/Down)
			var c = dirs[i];
			var ndn = getNeighborRoomNumber(rn,c);
			var ndoors = getRoomDoors(ndn);
			var action = getBetweenRoomAction(rn,c);
			subs['target'] = ndn
			subs['action'] = action
			if(doors.indexOf(c)>=0) {				
				g = g + sub(FRAGS['passageTwoWay'+c],subs);							
				if(isEdge(rn,c)) {
					// room number
					g = g + sub(FRAGS['neighborNumber'+c],subs);	
					g = g + sub(FRAGS['passageTwoWayTarget'+c],subs);
				} else if(action!='') {
					var sn = ''+rn+':'+ndn+':'+action;
					var sn2 = ''+ndn+':'+rn+':'+action;
					if(shown.indexOf(sn)<0) {						
						shown.push(sn);
						shown.push(sn2);
						g = g + sub(FRAGS['passageTwoWayTarget'+c],subs);	
					} else {
						console.log('skipping')
					}
				}
			} 			
		}
								
		
		g = g + FRAGS.roomEnd;
	
	}
	
	for(y=1;y<4;++y) {
		g = g + sub(FRAGS.floorSep,{y1:y*2000-35,y2:y*2000-35});
	}
	
	// TODO passages
	// TODO passage actions
	// TODO plain jumps
	// TODO targeted jumps
	// TODO objects
	// TODO creatures
	// TODO player
	// TODO spells
	
	g = g + '</g>';
	
	$('#svg').html(g);		
	
}

