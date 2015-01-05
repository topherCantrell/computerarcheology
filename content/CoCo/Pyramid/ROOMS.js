
/*global GAME, valueOrFunction */

// "desc" may be string or function
// commands may be function or string (shortcut for "movePlayerTo")
// "score" can be a function or a constant value (rooms rarely contribute to score)
// "do_afterPlayerTurn" is called on each object if it has the function

var ROOMS = function () {

	var roomData = {
	
			room_1 : {
				   desc : "YOU ARE STANDING BEFORE THE ENTRANCE OF A PYRAMID. AROUND YOU IS A DESERT.",
				   lit  : true,
				   commands : {
				 _n : [
				    "MoveToRoomX","room_2"],
				 _e : [
				    "MoveToRoomX","room_3"],
				 _s : [
				    "MoveToRoomX","room_4"],
				 _w : [
				    "MoveToRoomX","room_5"],
				 _in : [
				    "MoveToRoomX","room_2"]
				   }
				 },

				 room_2 : {
				   desc : "YOU ARE IN THE ENTRANCE TO THE PYRAMID. A HOLE IN THE FLOOR LEADS TO A PASSAGE BENEATH THE SURFACE.",
				   lit  : true,
				   commands : {
				 _s : [
				    "MoveToRoomX","room_1"],
				 _d : [
				    "MoveToRoomX","room_7"],
				 _out : [
				    "MoveToRoomX","room_1"],
				 _panel : [
				    "MoveToRoomX","room_26"]
				   }
				 },

				 room_3 : {
				   desc : "YOU ARE IN THE DESERT.",
				   lit  : true,
				   commands : {
				 _n : [
				    "MoveToRoomX","room_6"],
				 _e : [
				    "MoveToRoomX","room_3"],
				 _s : [
				    "MoveToRoomX","room_4"],
				 _w : [
				    "MoveToRoomX","room_1"]
				   }
				 },

				 room_4 : {
				   desc : "YOU ARE IN THE DESERT.",
				   lit  : true,
				   commands : {
				 _n : [
				    "MoveToRoomX","room_1"],
				 _e : [
				    "MoveToRoomX","room_3"],
				 _s : [
				    "MoveToRoomX","room_4"],
				 _w : [
				    "MoveToRoomX","room_5"]
				   }
				 },

				 room_5 : {
				   desc : "YOU ARE IN THE DESERT.",
				   lit  : true,
				   commands : {
				 _n : [
				    "MoveToRoomX","room_6"],
				 _e : [
				    "MoveToRoomX","room_1"],
				 _s : [
				    "MoveToRoomX","room_4"],
				 _w : [
				    "MoveToRoomX","room_5"]
				   }
				 },

				 room_6 : {
				   desc : "YOU ARE IN THE DESERT.",
				   lit  : true,
				   commands : {
				 _n : [
				    "MoveToRoomX","room_6"],
				 _e : [
				    "MoveToRoomX","room_3"],
				 _s : [
				    "MoveToRoomX","room_1"],
				 _w : [
				    "MoveToRoomX","room_5"]
				   }
				 },

				 room_7 : {
				   desc : "YOU ARE IN A SMALL CHAMBER BENEATH A HOLE FROM THE SURFACE. A LOW CRAWL LEADS INWARD TO THE WEST.  HIEROGLYPHICS ON THE WALL TRANSLATE, \"CURSE ALL WHO ENTER THIS SACRED CRYPT.\"",
				   lit  : true,
				   commands : {
				 _u : [
				    "MoveToRoomX","room_2"],
				 _out : [
				    "MoveToRoomX","room_2"],
				 _w : [
				    "MoveToRoomX","room_8"],
				 _in : [
				    "MoveToRoomX","room_8"]
				   }
				 },

				 room_8 : {
				   desc : "YOU ARE CRAWLING OVER PEBBLES IN A LOW PASSAGE. THERE IS A DIM LIGHT AT THE EAST END OF THE PASSAGE.",
				   commands : {
				 _e : [
				    "MoveToRoomX","room_7"],
				 _out : [
				    "MoveToRoomX","room_7"],
				 _w : [
				    "MoveToRoomX","room_9"],
				 _in : [
				    "MoveToRoomX","room_9"]
				   }
				 },

				 room_9 : {
				   desc : "YOU ARE IN A ROOM FILLED WITH BROKEN POTTERY SHARDS OF ANCIENT EGYPTIAN CRAFTS. AN AWKWARD CORRIDOR LEADS UPWARD AND WEST.",
				   commands : {
				 _e : [
				    "MoveToRoomX","room_8"],
				 _in : [
				    "MoveToRoomX","room_10"],
				 _u : [
				    "MoveToRoomX","room_10"],
				 _w : [
				    "MoveToRoomX","room_10"]
				   }
				 },

				 room_10 : {
				   desc : "YOU ARE IN AN AWKWARD SLOPING EAST/WEST CORRIDOR.",
				   commands : {
				 _d : [
				    "MoveToRoomX","room_9"],
				 _e : [
				    "MoveToRoomX","room_9"],
				 _in : [
				    "MoveToRoomX","room_11"],
				 _w : [
				    "MoveToRoomX","room_11"],
				 _u : [
				    "MoveToRoomX","room_11"]
				   }
				 },

				 room_11 : {
				   desc : "YOU ARE IN A SPLENDID CHAMBER THIRTY FEET HIGH. THE WALLS ARE FROZEN RIVERS OF ORANGE STONE. AN AWKWARD CORRIDOR AND A GOOD PASSAGE EXIT FROM THE EAST AND WEST SIDES OF THE CHAMBER.",
				   commands : {
				 _e : [
				    "MoveToRoomX","room_10"],
				 _w : [
				    "MoveToRoomX","room_12"]
				   }
				 },

				 room_12 : {
				   desc : "AT YOUR FEET IS A SMALL PIT BREATHING TRACES OF WHITE MIST. AN EAST PASSAGE ENDS HERE EXCEPT FOR A SMALL CRACK LEADING ON. ROUGH STONE STEPS LEAD DOWN THE PIT.",
				   commands : {
				 _e : [
				    "MoveToRoomX","room_11"],
				 _d : [
				    "SubScriptXAbortIfPass",[
				        "AssertObjectXIsInPack","#GOLD",
				        "PrintMessageX","YOU ARE AT THE BOTTOM OF THE PIT WITH A BROKEN NECK.",
				        "PlayerDied"],
				    "MoveToRoomX","room_13"],
				 _w : [
				    "PrintMessageX","THE CRACK IS FAR TOO SMALL FOR YOU TO FOLLOW."]
				   }
				 },

				 room_13 : {
				   desc : "YOU ARE AT ONE END OF A VAST HALL STRETCHING FORWARD OUT OF SIGHT TO THE WEST. THERE ARE OPENINGS TO EITHER SIDE. NEARBY, A WIDE STONE STAIRCASE LEADS DOWNWARD. THE HALL IS VERY MUSTY AND A COLD WIND BLOWS UP THE STAIRCASE. THERE IS A PASSAGE AT THE TOP OF A DOME BEHIND YOU. ROUGH STONE STEPS LEAD UP THE DOME.",
				   commands : {
				 _s : [
				    "MoveToRoomX","room_14"],
				 _w : [
				    "MoveToRoomX","room_15"],
				 _d : [
				    "MoveToRoomX","room_16"],
				 _n : [
				    "MoveToRoomX","room_16"],
				 _u : [
				    "SubScriptXAbortIfPass",[
				        "AssertObjectXIsInPack","#GOLD",
				        "PrintMessageX","THE DOME IS UNCLIMBABLE."],
				    "MoveToRoomX","room_12"],
				 _e : [
				    "SubScriptXAbortIfPass",[
				        "AssertObjectXIsInPack","#GOLD",
				        "PrintMessageX","THE DOME IS UNCLIMBABLE."],
				    "MoveToRoomX","room_12"],
				 __20__ : [
				    "MoveToRoomX","room_26"]
				   }
				 },

				 room_14 : {
				   desc : "THIS IS A LOW ROOM WITH A HIEROGLYPH ON THE WALL. IT TRANSLATES \"YOU WON'T GET IT UP THE STEPS\".",
				   commands : {
				 _out : [
				    "MoveToRoomX","room_13"],
				 _n : [
				    "MoveToRoomX","room_13"]
				   }
				 },

				 room_15 : {
				   desc : "YOU ARE ON THE EAST BANK OF A BOTTOMLESS PIT STRETCHING ACROSS THE HALL. THE MIST IS QUITE THICK HERE, AND THE PIT IS TOO WIDE TO JUMP.",
				   commands : {
				 _e : [
				    "MoveToRoomX","room_13"],
				 _jump : [
				    "SubScriptXAbortIfPass",[
				        "AssertObjectXIsInCurrentRoomOrPack","#bridge_15",
				        "PrintMessageX","I RESPECTFULLY SUGGEST YOU GO ACROSS THE BRIDGE INSTEAD OF JUMPING."],
				    "PrintMessageX","YOU DIDN'T MAKE IT.",
				    "PlayerDied"],
				 _w : [
				    "SubScriptXAbortIfPass",[
				        "AssertObjectXIsInCurrentRoomOrPack","#bridge_15",
				        "MoveToRoomX","room_18"],
				    "PrintMessageX","THERE IS NO WAY ACROSS THE BOTTOMLESS PIT."],
				 _cross : [
				    "AssertObjectXIsInCurrentRoomOrPack","#bridge_15",
				    "MoveToRoomX","room_18"],
				 _wave : [
				    "AssertObjectXMatchesUserInput","#SCEPTER",
				    "SubScriptXAbortIfPass",[
				        "AssertObjectXIsInCurrentRoomOrPack","#bridge_15",
				        "MoveObjectXToRoomY","#bridge_15","room_0",
				        "MoveObjectXToRoomY","#bridge_18","room_0",
				        "PrintMessageX","THE STONE BRIDGE HAS RETRACTED!"],
				    "MoveObjectXToCurrentRoom","#bridge_15",
				    "MoveObjectXToRoomY","#bridge_18","room_18",
				    "PrintMessageX","A STONE BRIDGE NOW SPANS THE BOTTOMLESS PIT."]
				   }
				 },

				 room_16 : {
				   desc : "YOU ARE IN THE PHARAOH'S CHAMBER, WITH PASSAGES OFF IN ALL DIRECTIONS.",
				   commands : {
				 _u : [
				    "MoveToRoomX","room_13"],
				 _e : [
				    "MoveToRoomX","room_13"],
				 _s : [
				    "SubScriptXAbortIfPass",[
				        "AssertObjectXIsInCurrentRoomOrPack","#SERPENT",
				        "PrintMessageX","YOU CAN'T GET BY THE SERPENT."],
				    "MoveToRoomX","room_17"],
				 _n : [
				    "SubScriptXAbortIfPass",[
				        "AssertObjectXIsInCurrentRoomOrPack","#SERPENT",
				        "PrintMessageX","YOU CAN'T GET BY THE SERPENT."],
				    "MoveToRoomX","room_25"],
				 _w : [
				    "SubScriptXAbortIfPass",[
				        "AssertObjectXIsInCurrentRoomOrPack","#SERPENT",
				        "PrintMessageX","YOU CAN'T GET BY THE SERPENT."],
				    "MoveToRoomX","room_24"],
				 _throw : [
				    "AssertObjectXMatchesUserInput","#BIRD_boxed",
				    "AssertObjectXIsInCurrentRoomOrPack","#SERPENT",
				    "MoveObjectXToRoomY","#SERPENT","room_0",
				    "MoveObjectXToCurrentRoom","#BIRD",
				    "MoveObjectXToRoomY","#BIRD_boxed","room_0",
				    "PrintMessageX","THE BIRD STATUE COMES TO LIFE AND ATTACKS THE SERPENT AND IN AN ASTOUNDING FLURRY, DRIVES THE SERPENT AWAY. THE BIRD TURNS BACK INTO A STATUE."]
				   }
				 },

				 room_17 : {
				   desc : "YOU ARE IN THE SOUTH SIDE CHAMBER.",
				   commands : {
				 _n : [
				    "MoveToRoomX","room_16"],
				 _out : [
				    "MoveToRoomX","room_16"]
				   }
				 },

				 room_18 : {
				   desc : "YOU ARE ON THE WEST SIDE OF THE BOTTOMLESS PIT IN THE HALL OF GODS.",
				   commands : {
				 _jump : [
				    "SubScriptXAbortIfPass",[
				        "AssertObjectXIsInCurrentRoomOrPack","#bridge_18",
				        "PrintMessageX","I RESPECTFULLY SUGGEST YOU GO ACROSS THE BRIDGE INSTEAD OF JUMPING."],
				    "PrintMessageX","YOU DIDN'T MAKE IT.",
				    "PlayerDied"],
				 _e : [
				    "SubScriptXAbortIfPass",[
				        "AssertObjectXIsInCurrentRoomOrPack","#bridge_18",
				        "MoveToRoomX","room_15"],
				    "PrintMessageX","THERE IS NO WAY ACROSS THE BOTTOMLESS PIT."],
				 _n : [
				    "PrintMessageX","YOU HAVE CRAWLED THROUGH A VERY LOW WIDE PASSAGE PARALLEL TO AND NORTH OF THE HALL OF GODS.",
				    "MoveToRoomX","room_19"],
				 _cross : [
				    "AssertObjectXIsInCurrentRoomOrPack","#bridge_18",
				    "MoveToRoomX","room_15"],
				 _wave : [
				    "AssertObjectXMatchesUserInput","#SCEPTER",
				    "SubScriptXAbortIfPass",[
				        "AssertObjectXIsInCurrentRoomOrPack","#bridge_18",
				        "MoveObjectXToRoomY","#bridge_18","room_0",
				        "MoveObjectXToRoomY","#bridge_15","room_0",
				        "PrintMessageX","THE STONE BRIDGE HAS RETRACTED!"],
				    "MoveObjectXToCurrentRoom","#bridge_18",
				    "MoveObjectXToRoomY","#bridge_15","room_15",
				    "PrintMessageX","A STONE BRIDGE NOW SPANS THE BOTTOMLESS PIT."]
				   }
				 },

				 room_19 : {
				   desc : "YOU ARE AT THE WEST END OF THE HALL OF GODS. A LOW WIDE PASS CONTINUES WEST AND ANOTHER GOES NORTH. TO THE SOUTH IS A LITTLE PASSAGE SIX FEET OFF THE FLOOR.",
				   commands : {
				 _s : [
				    "MoveToRoomX","room_28"],
				 _u : [
				    "MoveToRoomX","room_28"],
				 _climb : [
				    "MoveToRoomX","room_28"],
				 _e : [
				    "MoveToRoomX","room_18"],
				 _n : [
				    "MoveToRoomX","room_18"],
				 _w : [
				    "MoveToRoomX","room_20"]
				   }
				 },

				 room_20 : {
				   desc : "YOU ARE AT EAST END OF A VERY LONG HALL APPARENTLY WITHOUT SIDE CHAMBERS. TO THE EAST A LOW WIDE CRAWL SLANTS UP. TO THE NORTH A ROUND TWO FOOT HOLE SLANTS DOWN.",
				   commands : {
				 _e : [
				    "MoveToRoomX","room_19"],
				 _u : [
				    "MoveToRoomX","room_19"],
				 _w : [
				    "MoveToRoomX","room_21"],
				 _n : [
				    "MoveToRoomX","room_22"],
				 _d : [
				    "MoveToRoomX","room_22"]
				   }
				 },

				 room_21 : {
				   desc : "YOU ARE AT THE WEST END OF A VERY LONG FEATURELESS HALL. THE HALL JOINS UP WITH A NARROW NORTH/SOUTH PASSAGE.",
				   commands : {
				 _e : [
				    "MoveToRoomX","room_20"],
				 _n : [
				    "MoveToRoomX","room_22"]
				   }
				 },

				 room_22 : {
				   desc : "YOU ARE AT A CROSSOVER OF A HIGH N/S PASSAGE AND A LOW E/W ONE.",
				   commands : {
				 _w : [
				    "MoveToRoomX","room_20"],
				 _n : [
				    "MoveToRoomX","room_23"],
				 _e : [
				    "MoveToRoomX","room_24"],
				 _s : [
				    "MoveToRoomX","room_21"]
				   }
				 },

				 room_23 : {
				   desc : "DEAD END.",
				   commands : {
				 _s : [
				    "MoveToRoomX","room_22"],
				 _out : [
				    "MoveToRoomX","room_22"]
				   }
				 },

				 room_24 : {
				   desc : "YOU ARE IN THE WEST THRONE CHAMBER. A PASSAGE CONTINUES WEST AND UP FROM HERE.",
				   commands : {
				 _e : [
				    "MoveToRoomX","room_16"],
				 _out : [
				    "MoveToRoomX","room_16"],
				 _w : [
				    "MoveToRoomX","room_22"],
				 _u : [
				    "MoveToRoomX","room_22"]
				   }
				 },

				 room_25 : {
				   desc : "YOU ARE IN A LOW N/S PASSAGE AT A HOLE IN THE FLOOR. THE HOLE GOES DOWN TO AN E/W PASSAGE.",
				   commands : {
				 _out : [
				    "MoveToRoomX","room_16"],
				 _s : [
				    "MoveToRoomX","room_16"],
				 _n : [
				    "MoveToRoomX","room_26"],
				 __20__ : [
				    "MoveToRoomX","room_26"],
				 _d : [
				    "MoveToRoomX","room_54"]
				   }
				 },

				 room_26 : {
				   desc : "YOU ARE IN A LARGE ROOM, WITH A PASSAGE TO THE SOUTH, AND A WALL OF BROKEN ROCK TO THE EAST. THERE IS A PANEL ON THE NORTH WALL.",
				   commands : {
				 _panel : [
				    "MoveToRoomX","room_2"],
				 _s : [
				    "MoveToRoomX","room_25"],
				 _e : [
				    "MoveToRoomX","room_27"]
				   }
				 },

				 room_27 : {
				   desc : "YOU ARE IN THE CHAMBER OF ANUBIS.",
				   commands : {
				 _d : [
				    "MoveToRoomX","room_26"],
				 __20__ : [
				    "MoveToRoomX","room_26"],
				 _u : [
				    "MoveToRoomX","room_13"]
				   }
				 },

				 room_28 : {
				   desc : "YOU ARE IN A MAZE OF TWISTY PASSAGES, ALL ALIKE.",
				   commands : {
				 _n : [
				    "MoveToRoomX","room_28"],
				 _e : [
				    "MoveToRoomX","room_32"],
				 _s : [
				    "MoveToRoomX","room_30"],
				 _w : [
				    "MoveToRoomX","room_29"],
				 _u : [
				    "MoveToRoomX","room_19"]
				   }
				 },

				 room_29 : {
				   desc : "YOU ARE IN A MAZE OF TWISTY PASSAGES, ALL ALIKE.",
				   commands : {
				 _n : [
				    "MoveToRoomX","room_28"],
				 _e : [
				    "MoveToRoomX","room_51"],
				 _s : [
				    "MoveToRoomX","room_29"],
				 _w : [
				    "MoveToRoomX","room_29"]
				   }
				 },

				 room_30 : {
				   desc : "YOU ARE IN A MAZE OF TWISTY PASSAGES, ALL ALIKE.",
				   commands : {
				 _n : [
				    "MoveToRoomX","room_32"],
				 _e : [
				    "MoveToRoomX","room_42"],
				 _s : [
				    "MoveToRoomX","room_43"],
				 _w : [
				    "MoveToRoomX","room_28"],
				 _u : [
				    "MoveToRoomX","room_31"],
				 _d : [
				    "MoveToRoomX","room_31"]
				   }
				 },

				 room_31 : {
				   desc : "YOU ARE IN A MAZE OF TWISTY PASSAGES, ALL ALIKE.",
				   commands : {
				 _u : [
				    "MoveToRoomX","room_30"],
				 _d : [
				    "MoveToRoomX","room_30"]
				   }
				 },

				 room_32 : {
				   desc : "YOU ARE IN A MAZE OF TWISTY PASSAGES, ALL ALIKE.",
				   commands : {
				 _e : [
				    "MoveToRoomX","room_30"],
				 _s : [
				    "MoveToRoomX","room_33"],
				 _w : [
				    "MoveToRoomX","room_28"]
				   }
				 },

				 room_33 : {
				   desc : "YOU ARE IN A MAZE OF TWISTY PASSAGES, ALL ALIKE.",
				   commands : {
				 _n : [
				    "MoveToRoomX","room_44"],
				 _e : [
				    "MoveToRoomX","room_32"],
				 _s : [
				    "MoveToRoomX","room_34"],
				 _d : [
				    "MoveToRoomX","room_45"]
				   }
				 },

				 room_34 : {
				   desc : "YOU ARE IN A MAZE OF TWISTY PASSAGES, ALL ALIKE.",
				   commands : {
				 _e : [
				    "MoveToRoomX","room_33"],
				 _s : [
				    "MoveToRoomX","room_35"],
				 _w : [
				    "MoveToRoomX","room_37"],
				 _d : [
				    "MoveToRoomX","room_38"]
				   }
				 },

				 room_35 : {
				   desc : "YOU ARE IN A MAZE OF TWISTY PASSAGES, ALL ALIKE.",
				   commands : {
				 _n : [
				    "MoveToRoomX","room_36"],
				 _e : [
				    "MoveToRoomX","room_38"],
				 _s : [
				    "MoveToRoomX","room_35"],
				 _w : [
				    "MoveToRoomX","room_34"],
				 _u : [
				    "MoveToRoomX","room_39"],
				 _d : [
				    "MoveToRoomX","room_47"]
				   }
				 },

				 room_36 : {
				   desc : "YOU ARE IN A MAZE OF TWISTY PASSAGES, ALL ALIKE.",
				   commands : {
				 _n : [
				    "MoveToRoomX","room_36"],
				 _e : [
				    "MoveToRoomX","room_52"],
				 _w : [
				    "MoveToRoomX","room_35"],
				 _d : [
				    "MoveToRoomX","room_48"]
				   }
				 },

				 room_37 : {
				   desc : "YOU ARE IN A MAZE OF TWISTY PASSAGES, ALL ALIKE.",
				   commands : {
				 _e : [
				    "MoveToRoomX","room_34"],
				 _w : [
				    "MoveToRoomX","room_38"]
				   }
				 },

				 room_38 : {
				   desc : "YOU ARE IN A MAZE OF TWISTY PASSAGES, ALL ALIKE.",
				   commands : {
				 _e : [
				    "MoveToRoomX","room_35"],
				 _s : [
				    "MoveToRoomX","room_39"],
				 _w : [
				    "MoveToRoomX","room_37"],
				 _u : [
				    "MoveToRoomX","room_34"]
				   }
				 },

				 room_39 : {
				   desc : "YOU ARE IN A MAZE OF TWISTY PASSAGES, ALL ALIKE.",
				   commands : {
				 _n : [
				    "MoveToRoomX","room_35"],
				 _s : [
				    "MoveToRoomX","room_46"],
				 _w : [
				    "MoveToRoomX","room_38"]
				   }
				 },

				 room_40 : {
				   desc : "YOU ARE IN A MAZE OF TWISTY PASSAGES, ALL ALIKE.",
				   commands : {
				 _n : [
				    "MoveToRoomX","room_52"],
				 _w : [
				    "MoveToRoomX","room_41"],
				 _nw : [
				    "MoveToRoomX","room_53"]
				   }
				 },

				 room_41 : {
				   desc : "YOU ARE IN A MAZE OF TWISTY PASSAGES, ALL ALIKE.",
				   commands : {
				 _e : [
				    "MoveToRoomX","room_40"],
				 _s : [
				    "MoveToRoomX","room_52"],
				 _w : [
				    "MoveToRoomX","room_50"]
				   }
				 },

				 room_42 : {
				   desc : "DEAD END.",
				   commands : {
				 _w : [
				    "MoveToRoomX","room_30"]
				   }
				 },

				 room_43 : {
				   desc : "DEAD END.",
				   commands : {
				 _e : [
				    "MoveToRoomX","room_30"]
				   }
				 },

				 room_44 : {
				   desc : "DEAD END.",
				   commands : {
				 _s : [
				    "MoveToRoomX","room_33"]
				   }
				 },

				 room_45 : {
				   desc : "DEAD END.",
				   commands : {
				 _u : [
				    "MoveToRoomX","room_33"]
				   }
				 },

				 room_46 : {
				   desc : "DEAD END.",
				   commands : {
				 _w : [
				    "MoveToRoomX","room_39"]
				   }
				 },

				 room_47 : {
				   desc : "DEAD END.",
				   commands : {
				 _u : [
				    "MoveToRoomX","room_35"]
				   }
				 },

				 room_48 : {
				   desc : "DEAD END.",
				   commands : {
				 _u : [
				    "MoveToRoomX","room_36"]
				   }
				 },

				 room_49 : {
				   desc : "DEAD END.",
				   commands : {
				 _e : [
				    "MoveToRoomX","room_52"]
				   }
				 },

				 room_50 : {
				   desc : "DEAD END.",
				   commands : {
				 _e : [
				    "MoveToRoomX","room_41"]
				   }
				 },

				 room_51 : {
				   desc : "DEAD END.",
				   commands : {
				 _w : [
				    "MoveToRoomX","room_29"],
				 _drop : [
				    "AssertObjectXMatchesUserInput","#COINS",
				    "MoveObjectXToRoomY","#COINS","room_0",
				    "MoveObjectXToCurrentRoom","#BATTERIES_fresh",
				    "PrintMessageX","THERE ARE NOW SOME FRESH BATTERIES HERE."]
				   }
				 },

				 room_52 : {
				   desc : "YOU ARE ON THE BRINK OF A LARGE PIT. YOU COULD CLIMB DOWN, BUT YOU WOULD NOT BE ABLE TO CLIMB BACK UP. THE MAZE CONTINUES ON THIS LEVEL.",
				   commands : {
				 _n : [
				    "MoveToRoomX","room_41"],
				 _e : [
				    "MoveToRoomX","room_40"],
				 _s : [
				    "MoveToRoomX","room_49"],
				 _w : [
				    "MoveToRoomX","room_36"],
				 _d : [
				    "MoveToRoomX","room_11"]
				   }
				 },

				 room_53 : {
				   desc : "DEAD END.",
				   commands : {
				 _se : [
				    "MoveToRoomX","room_40"]
				   }
				 },

				 room_54 : {
				   desc : "YOU ARE IN A DIRTY BROKEN PASSAGE. TO THE EAST IS A CRAWL. TO THE WEST IS A LARGE PASSAGE. ABOVE YOU IS A HOLE TO ANOTHER PASSAGE.",
				   commands : {
				 _e : [
				    "MoveToRoomX","room_55"],
				 _w : [
				    "MoveToRoomX","room_57"],
				 _u : [
				    "MoveToRoomX","room_25"]
				   }
				 },

				 room_55 : {
				   desc : "YOU ARE ON THE BRINK OF A SMALL CLEAN CLIMBABLE PIT. A CRAWL LEADS WEST.",
				   commands : {
				 _w : [
				    "MoveToRoomX","room_54"],
				 _d : [
				    "MoveToRoomX","room_56"],
				 _climb : [
				    "MoveToRoomX","room_56"]
				   }
				 },

				 room_56 : {
				   desc : "YOU ARE IN THE BOTTOM OF A SMALL PIT WITH A LITTLE STREAM, WHICH ENTERS AND EXITS THROUGH TINY SLITS.",
				   commands : {
				 _u : [
				    "MoveToRoomX","room_55"],
				 _out : [
				    "MoveToRoomX","room_55"],
				 _climb : [
				    "MoveToRoomX","room_55"],
				 _d : [
				    "PrintMessageX","YOU DON'T FIT THROUGH TWO-INCH SLIT!"],
				 _fill : [
				    "SubScriptXAbortIfPass",[
				        "AssertObjectXIsInPack","#WATER",
				        "PrintMessageX","YOUR BOTTLE IS ALREADY FULL."],
				    "MoveObjectXToIntoContainerY","#WATER","#BOTTLE"]
				   }
				 },

				 room_57 : {
				   desc : "YOU ARE IN A THE ROOM OF BES, WHOSE PICTURE IS ON THE WALL. THERE IS A BIG HOLE IN THE FLOOR. THERE IS A PASSAGE LEADING EAST.",
				   commands : {
				 _e : [
				    "MoveToRoomX","room_54"],
				 _d : [
				    "MoveToRoomX","room_58"]
				   }
				 },

				 room_58 : {
				   desc : "YOU ARE AT A COMPLEX JUNCTION. A LOW HANDS AND KNEES PASSAGE FROM THE NORTH JOINS A HIGHER CRAWL FROM THE EAST TO MAKE A WALKING PASSAGE GOING WEST. THERE IS ALSO A LARGE ROOM ABOVE. THE AIR IS DAMP HERE.",
				   commands : {
				 _n : [
				    "MoveToRoomX","room_61"],
				 _e : [
				    "MoveToRoomX","room_59"],
				 _w : [
				    "MoveToRoomX","room_65"],
				 _u : [
				    "MoveToRoomX","room_57"],
				 _climb : [
				    "MoveToRoomX","room_57"]
				   }
				 },

				 room_59 : {
				   desc : "YOU ARE IN THE UNDERWORLD ANTEROOM OF SEKER. PASSAGES GO EAST, WEST, AND UP. HUMAN BONES ARE STREWN ABOUT ON THE FLOOR. HIEROGLYPHICS ON THE WALL ROUGHLY TRANSLATE TO \"THOSE WHO PROCEED EAST MAY NEVER RETURN.\"",
				   commands : {
				 _e : [
				    "MoveToRoomX","room_60"],
				 _w : [
				    "MoveToRoomX","room_65"],
				 _u : [
				    "MoveToRoomX","room_58"]
				   }
				 },

				 room_60 : {
				   desc : "YOU ARE AT THE LAND OF DEAD. PASSAGES LEAD OFF IN >ALL< DIRECTIONS.",
				   commands : {
				 _n : [
				    "SubScriptXAbortIfPass",[
				        "AssertRandomIsGreaterThanX","240"],
				    "MoveToRoomX","room_59"],
				 _e : [
				    "SubScriptXAbortIfPass",[
				        "AssertRandomIsGreaterThanX","240"],
				    "MoveToRoomX","room_59"],
				 _s : [
				    "SubScriptXAbortIfPass",[
				        "AssertRandomIsGreaterThanX","240"],
				    "MoveToRoomX","room_59"],
				 _ne : [
				    "SubScriptXAbortIfPass",[
				        "AssertRandomIsGreaterThanX","240"],
				    "MoveToRoomX","room_59"],
				 _se : [
				    "SubScriptXAbortIfPass",[
				        "AssertRandomIsGreaterThanX","240"],
				    "MoveToRoomX","room_59"],
				 _sw : [
				    "SubScriptXAbortIfPass",[
				        "AssertRandomIsGreaterThanX","240"],
				    "MoveToRoomX","room_59"],
				 _nw : [
				    "SubScriptXAbortIfPass",[
				        "AssertRandomIsGreaterThanX","240"],
				    "MoveToRoomX","room_59"],
				 _u : [
				    "SubScriptXAbortIfPass",[
				        "AssertRandomIsGreaterThanX","240"],
				    "MoveToRoomX","room_59"],
				 _w : [
				    "PrintMessageX","YOU HAVE CRAWLED AROUND IN SOME LITTLE HOLES AND FOUND YOUR WAY BLOCKED BY A FALLEN SLAB. YOU ARE NOW BACK IN THE MAIN PASSAGE.",
				    "MoveToRoomX","room_60"]
				   }
				 },

				 room_61 : {
				   desc : "YOU'RE IN A LARGE ROOM WITH ANCIENT DRAWINGS ON ALL WALLS. THE PICTURES DEPICT ATUM, A PHARAOH WEARING THE DOUBLE CROWN. A SHALLOW PASSAGE PROCEEDS DOWNWARD, AND A SOMEWHAT STEEPER ONE LEADS UP. A LOW HANDS AND KNEES PASSAGE ENTERS FROM THE SOUTH. ",
				   commands : {
				 _s : [
				    "SubScriptXAbortIfPass",[
				        "AssertObjectXIsInPack","#SARCOPH_full",
				        "PrintMessageX","YOU CAN'T FIT THIS BIG SARCOPHAGUS THROUGH THAT LITTLE PASSAGE!"],
				    "SubScriptXAbortIfPass",[
				        "AssertObjectXIsInPack","#SARCOPH_empty",
				        "PrintMessageX","YOU CAN'T FIT THIS BIG SARCOPHAGUS THROUGH THAT LITTLE PASSAGE!"],
				    "MoveToRoomX","room_58"],
				 _u : [
				    "MoveToRoomX","room_62"],
				 _d : [
				    "MoveToRoomX","room_63"]
				   }
				 },

				 room_62 : {
				   desc : "YOU ARE IN A CHAMBER WHOSE WALL CONTAINS A PICTURE OF A MAN WEARING THE LUNAR DISK ON HIS HEAD.  HE IS THE GOD KHONS, THE MOON GOD.",
				   commands : {
				 _d : [
				    "MoveToRoomX","room_61"],
				 _out : [
				    "MoveToRoomX","room_61"]
				   }
				 },

				 room_63 : {
				   desc : "YOU ARE IN A LONG SLOPING CORRIDOR WITH RAGGED WALLS.",
				   commands : {
				 _u : [
				    "MoveToRoomX","room_61"],
				 _d : [
				    "MoveToRoomX","room_64"]
				   }
				 },

				 room_64 : {
				   desc : "YOU ARE IN A CUL-DE-SAC ABOUT EIGHT FEET ACROSS.",
				   commands : {
				 _u : [
				    "MoveToRoomX","room_63"],
				 _out : [
				    "MoveToRoomX","room_63"]
				   }
				 },

				 room_65 : {
				   desc : "YOU ARE IN THE CHAMBER OF HORUS, A LONG EAST/WEST PASSAGE WITH HOLES EVERYWHERE. TO EXPLORE AT RANDOM, SELECT NORTH, SOUTH, UP, OR DOWN.",
				   commands : {
				 _e : [
				    "MoveToRoomX","room_58"],
				 _w : [
				    "MoveToRoomX","room_78"],
				 _u : [
				    "SubScriptXAbortIfPass",[
				        "AssertRandomIsGreaterThanX","204"],
				    "MoveToRoomX","room_72"],
				 _n : [
				    "SubScriptXAbortIfPass",[
				        "AssertRandomIsGreaterThanX","204"],
				    "MoveToRoomX","room_73"],
				 _s : [
				    "SubScriptXAbortIfPass",[
				        "AssertRandomIsGreaterThanX","204"],
				    "MoveToRoomX","room_66"],
				 _d : [
				    "SubScriptXAbortIfPass",[
				        "AssertRandomIsGreaterThanX","204"],
				    "MoveToRoomX","room_59"]
				   }
				 },

				 room_66 : {
				   desc : "YOU ARE IN A LARGE LOW CIRCULAR CHAMBER WHOSE FLOOR IS AN IMMENSE SLAB FALLEN FROM THE CEILING. EAST AND WEST THERE ONCE WERE LARGE PASSAGES, BUT THEY ARE NOW FILLED WITH SAND. LOW SMALL PASSAGES GO NORTH AND SOUTH.",
				   commands : {
				 _n : [
				    "MoveToRoomX","room_65"],
				 _s : [
				    "MoveToRoomX","room_80"]
				   }
				 },

				 room_72 : {
				   desc : "YOU ARE IN THE PRIEST'S BEDROOM. THE WALLS ARE COVERED WITH CURTAINS, THE FLOOR WITH A THICK PILE CARPET. MOSS COVERS THE CEILING.",
				   commands : {
				 _w : [
				    "MoveToRoomX","room_65"],
				 _out : [
				    "MoveToRoomX","room_65"]
				   }
				 },

				 room_73 : {
				   desc : "THIS IS THE CHAMBER OF THE HIGH PRIEST. ANCIENT DRAWINGS COVER THE WALLS. AN EXTREMELY TIGHT TUNNEL LEADS WEST. IT LOOKS LIKE A TIGHT SQUEEZE. ANOTHER PASSAGE LEADS SE.",
				   commands : {
				 _w : [
				    "SubScriptXAbortIfPass",[
				        "AssertPackIsEmptyExceptForEmerald",
				        "MoveToRoomX","room_76"],
				    "PrintMessageX","SOMETHING YOU'RE CARRYING WON'T FIT THROUGH THE TUNNEL WITH YOU. YOU'D BEST TAKE INVENTORY AND DROP SOMETHING."],
				 _se : [
				    "MoveToRoomX","room_65"]
				   }
				 },

				 room_76 : {
				   desc : "YOU ARE IN THE HIGH PRIEST'S TREASURE ROOM LIT BY AN EERIE GREEN LIGHT. A NARROW TUNNEL EXITS TO THE EAST.",
				   lit  : true,
				   commands : {
				 _e : [
				    "SubScriptXAbortIfPass",[
				        "AssertPackIsEmptyExceptForEmerald",
				        "MoveToRoomX","room_73"],
				    "PrintMessageX","SOMETHING YOU'RE CARRYING WON'T FIT THROUGH THE TUNNEL WITH YOU. YOU'D BEST TAKE INVENTORY AND DROP SOMETHING."],
				 _out : [
				    "SubScriptXAbortIfPass",[
				        "AssertPackIsEmptyExceptForEmerald",
				        "MoveToRoomX","room_73"],
				    "PrintMessageX","SOMETHING YOU'RE CARRYING WON'T FIT THROUGH THE TUNNEL WITH YOU. YOU'D BEST TAKE INVENTORY AND DROP SOMETHING."]
				   }
				 },

				 room_78 : {
				   desc : "YOU ARE AT THE EAST END OF THE TWOPIT ROOM. THE FLOOR HERE IS LITTERED WITH THIN ROCK SLABS, WHICH MAKE IT EASY TO DESCEND THE PITS. THERE IS A PATH HERE BYPASSING THE PITS TO CONNECT PASSAGES EAST AND WEST. THERE ARE HOLES ALL OVER, BUT THE ONLY BIG ONE IS ON THE WALL DIRECTLY OVER THE WEST PIT WHERE YOU CAN'T GET TO IT.",
				   commands : {
				 _e : [
				    "MoveToRoomX","room_65"],
				 _w : [
				    "MoveToRoomX","room_80"],
				 _d : [
				    "MoveToRoomX","room_79"]
				   }
				 },

				 room_79 : {
				   desc : "YOU ARE AT THE BOTTOM OF THE EASTERN PIT IN THE TWOPIT ROOM.",
				   commands : {
				 _u : [
				    "MoveToRoomX","room_78"],
				 _out : [
				    "MoveToRoomX","room_78"]
				   }
				 },

				 room_80 : {
				   desc : "YOU ARE AT THE WEST END OF THE TWOPIT ROOM. THERE IS A LARGE HOLE IN THE WALL ABOVE THE PIT AT THIS END OF THE ROOM.",
				   commands : {
				 _e : [
				    "MoveToRoomX","room_78"],
				 _w : [
				    "MoveToRoomX","room_66"],
				 _d : [
				    "MoveToRoomX","room_81"]
				   }
				 },

				 room_81 : {
				   desc : "YOU ARE AT THE BOTTOM OF THE WEST PIT IN THE TWOPIT ROOM. THERE IS A LARGE HOLE IN THE WALL ABOUT TWENTY FIVE FEET ABOVE YOU.",
				   commands : {
				 _u : [
				    "MoveToRoomX","room_80"],
				 _out : [
				    "MoveToRoomX","room_80"],
				 _climb : [
				    "SubScriptXAbortIfPass",[
				        "AssertObjectXIsInCurrentRoomOrPack","#PLANT_C",
				        "PrintMessageX","YOU CLAMBER UP THE PLANT AND SCURRY THROUGH THE HOLE AT THE TOP.",
				        "MoveToRoomX","room_77"],
				    "SubScriptXAbortIfPass",[
				        "AssertObjectXIsInCurrentRoomOrPack","#PLANT_B",
				        "PrintMessageX","YOU'VE CLIMBED UP THE PLANT AND OUT OF THE PIT."],
				    "MoveToRoomX","room_80",
				    "PrintMessageX","THERE IS NOTHING HERE TO CLIMB. USE UP OR OUT TO LEAVE THE PIT."],
				 _pour : [
				    "AssertObjectXMatchesUserInput","#WATER",
				    "MoveObjectXToRoomY","#WATER","room_0",
				    "SubScriptXAbortIfPass",[
				        "AssertObjectXIsInCurrentRoomOrPack","#PLANT_A",
				        "MoveObjectXToRoomY","#PLANT_A","room_0",
				        "MoveObjectXToCurrentRoom","#PLANT_B",
				        "PrintMessageX","THE PLANT SPURTS INTO FURIOUS GROWTH FOR A FEW SECONDS.",
				        "PrintMessageX","THERE IS A TWELVE FOOT BEAN STALK STRETCHING UP OUT OF THE PIT, BELLOWING \"WATER... WATER...\""],
				    "SubScriptXAbortIfPass",[
				        "AssertObjectXIsInCurrentRoomOrPack","#PLANT_B",
				        "MoveObjectXToRoomY","#PLANT_B","room_0",
				        "MoveObjectXToCurrentRoom","#PLANT_C",
				        "PrintMessageX","THE PLANT GROWS EXPLOSIVELY, ALMOST FILLING THE BOTTOM OF THE PIT.",
				        "PrintMessageX","THERE IS A GIGANTIC BEAN STALK STRETCHING ALL THE WAY UP TO THE HOLE."],
				    "MoveObjectXToRoomY","#PLANT_C","room_0",
				    "MoveObjectXToCurrentRoom","#PLANT_A",
				    "PrintMessageX","YOU'VE OVER-WATERED THE PLANT! IT'S SHRIVELING UP!",
				    "PrintMessageX","THERE IS A TINY PLANT IN THE PIT, MURMURING \"WATER, WATER, ...\""]
				   }
				 },

				 room_77 : {
				   desc : "YOU ARE IN A LONG, NARROW CORRIDOR STRETCHING OUT OF SIGHT TO THE WEST. AT THE EASTERN END IS A HOLE THROUGH WHICH YOU CAN SEE A PROFUSION OF LEAVES.",
				   commands : {
				 _e : [
				    "MoveToRoomX","room_81"],
				 _d : [
				    "MoveToRoomX","room_81"],
				 _climb : [
				    "MoveToRoomX","room_81"],
				 _jump : [
				    "PrintMessageX","YOU ARE AT THE BOTTOM OF THE PIT WITH A BROKEN NECK.",
				    "PlayerDied"],
				 _w : [
				    "MoveToRoomX","room_71"]
				   }
				 },

				 room_71 : {
				   desc : "YOU ARE IN THE CHAMBER OF OSIRIS. THE CEILING IS TOO HIGH UP FOR YOUR LAMP TO SHOW IT. PASSAGES LEAD EAST, NORTH, AND SOUTH.",
				   commands : {
				 _n : [
				    "MoveToRoomX","room_68"],
				 _e : [
				    "MoveToRoomX","room_70"],
				 _s : [
				    "MoveToRoomX","room_77"]
				   }
				 },

				 room_70 : {
				   desc : "THE PASSAGE HERE IS BLOCKED BY A FALLEN BLOCK.",
				   commands : {
				 _s : [
				    "MoveToRoomX","room_71"],
				 _out : [
				    "MoveToRoomX","room_71"]
				   }
				 },

				 room_68 : {
				   desc : "YOU ARE IN THE CHAMBER OF NEKHEBET, A WOMAN WITH THE HEAD OF A VULTURE, WEARING THE CROWN OF EGYPT. A PASSAGE EXITS TO THE SOUTH.",
				   commands : {
				 _s : [
				    "MoveToRoomX","room_71"],
				 _out : [
				    "MoveToRoomX","room_71"]
				   }
				 }
	
	};
	    
    //
    // Room handling functions
    //
    
    /**
     * This function returns true if the target room has light (natural or from the lamp).
     * @param room the target room
     * @return true if the room has light
     */
    var isRoomLit = function (room) {
        var ro = ROOMS.getRoom(room);
        
        // The target room may be naturally lit
        if (ro.lit) {
            return true;
        }
                
        // The lit lamp (or it's container)
        var lamp = OBJS.getTopObjectByName("#LAMP_on");
        
        // The lamp may be lit on the floor of the target room or in the pack
        if (lamp.location === room || lamp.location === "pack") {
            return true;
        } 
                
        // No light
        return false;
    };  
				
    /**
     * This function looks up a room by name.
     * @param room the room name
     * @return the room object (or undefined)
     */
	var getRoom = function (room) {
		// Look up the room
		var r = roomData[room];
		
		// Software error if not found
		if (!r) {
			GAME.facePalm("Room '" + room + "' not found");
			return;
		}
		
		return r;
	};
	        
    /**
     * This function calculates the score contribution by each room (usually none).
     * @return score from the rooms
     */
    var calculateScore = function () {
        var score = 0;
        for (var ro in roomData) {
            if (roomData[ro].hasOwnProperty("score")) {
                score = score + valueOrFunction(roomData[ro].score);
            }
        }        
        return score;
    };
    
    // Public API for the "ROOMS" object
    return {
    	isRoomLit : isRoomLit,
        getRoom : getRoom,        
        calculateScore : calculateScore
    };

}();