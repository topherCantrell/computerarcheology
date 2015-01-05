
/*global GAME, OBJS, println */

// Default commands can be functions or strings (strings are printed)

var DEFAULT = function () {

	var defaultHandler =  {
		 _n : [
		    "PrintMessageX","THERE IS NO WAY FOR YOU TO GO THAT DIRECTION."],
		 _e : [
		    "PrintMessageX","THERE IS NO WAY FOR YOU TO GO THAT DIRECTION."],
		 _s : [
		    "PrintMessageX","THERE IS NO WAY FOR YOU TO GO THAT DIRECTION."],
		 _w : [
		    "PrintMessageX","THERE IS NO WAY FOR YOU TO GO THAT DIRECTION."],
		 _ne : [
		    "PrintMessageX","THERE IS NO WAY FOR YOU TO GO THAT DIRECTION."],
		 _se : [
		    "PrintMessageX","THERE IS NO WAY FOR YOU TO GO THAT DIRECTION."],
		 _sw : [
		    "PrintMessageX","THERE IS NO WAY FOR YOU TO GO THAT DIRECTION."],
		 _nw : [
		    "PrintMessageX","THERE IS NO WAY FOR YOU TO GO THAT DIRECTION."],
		 _u : [
		    "PrintMessageX","THERE IS NO WAY FOR YOU TO GO THAT DIRECTION."],
		 _d : [
		    "PrintMessageX","THERE IS NO WAY FOR YOU TO GO THAT DIRECTION."],
		 _in : [
		    "PrintMessageX","I DON'T KNOW IN FROM OUT HERE. USE COMPASS POINTS."],
		 _out : [
		    "PrintMessageX","I DON'T KNOW IN FROM OUT HERE. USE COMPASS POINTS."],
		 _left : [
		    "PrintMessageX","I AM UNSURE HOW YOU ARE FACING. USE COMPASS POINTS."],
		 _right : [
		    "PrintMessageX","I AM UNSURE HOW YOU ARE FACING. USE COMPASS POINTS."],
		 _panel : [
		    "PrintMessageX","NOTHING HAPPENS."],
		 _back : [
		    "MoveToLastRoom"],
		 _swim : [
		    "PrintMessageX","I DON'T KNOW HOW."],
		 _on : [
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXIsInPack","#LAMP_off",
		        "MoveObjectXToRoomY","#LAMP_off","room_0",
		        "MoveObjectXToRoomY","#LAMP_on","pack",
		        "PrintMessageX","YOUR LAMP IS NOW ON."],
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXIsInPack","#LAMP_on",
		        "PrintMessageX","YOUR LAMP IS NOW ON."],
		    "PrintMessageX","YOU HAVE NO SOURCE OF LIGHT."],
		 _off : [
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXIsInPack","#LAMP_on",
		        "MoveObjectXToRoomY","#LAMP_on","room_0",
		        "MoveObjectXToRoomY","#LAMP_off","pack",
		        "PrintMessageX","YOUR LAMP IS NOW OFF."],
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXIsInPack","#LAMP_off",
		        "PrintMessageX","YOUR LAMP IS NOW OFF."],
		    "PrintMessageX","YOU HAVE NO SOURCE OF LIGHT."],
		 _quit : [
		    "Quit"],
		 _score : [
		    "PrintScore"],
		 _inv : [
		    "PrintInventory"],
		 _look : [
		    "PrintRoomDescription"],
		 _get : [
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#PLANT_A",
		        "PrintMessageX","THE PLANT HAS EXCEPTIONALLY DEEP ROOTS AND CANNOT BE PULLED FREE."],
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#BIRD",
		        "SubScriptXAbortIfPass",[
		            "AssertObjectXIsInPack","#SCEPTER",
		            "PrintMessageX","AS YOU APPROACH THE STATUE, IT COMES TO LIFE AND FLIES ACROSS THE CHAMBER WHERE IT LANDS AND RETURNS TO STONE."],
		        "SubScriptXAbortIfPass",[
		            "AssertObjectXIsInPack","#BOX",
		            "MoveObjectXToRoomY","#BIRD","room_0",
		            "MoveObjectXToIntoContainerY","#BIRD_boxed","#BOX"],
		        "PrintMessageX","YOU CAN LIFT THE STATUE, BUT YOU CANNOT CARRY IT."],
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#VASE_pillow",
		        "GetObjectXFromRoom","#VASE_solo",
		        "MoveObjectXToRoomY","#VASE_pillow","room_0",
		        "MoveObjectXToCurrentRoom","#PILLOW"],
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#stream_56",
		        "SubScriptXAbortIfPass",[
		            "AssertObjectXIsInPack","#WATER",
		            "PrintMessageX","YOUR BOTTLE IS ALREADY FULL."],
		        "MoveObjectXToIntoContainerY","#WATER","#BOTTLE"],
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#PILLOW",
		        "AssertObjectXIsInCurrentRoom","#VASE_pillow",
		        "MoveObjectXToRoomY","#VASE_pillow","room_0",
		        "MoveObjectXToCurrentRoom","#VASE_solo",
		        "GetObjectXFromRoom","#PILLOW"],
		    "GetUserInputObject"],
		 _drop : [
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#VASE_solo",
		        "MoveObjectXToRoomY","#VASE_solo","room_0",
		        "SubScriptXAbortIfPass",[
		            "AssertObjectXIsInCurrentRoom","#PILLOW",
		            "MoveObjectXToCurrentRoom","#VASE_pillow",
		            "PrintMessageX","THE VASE IS NOW RESTING, DELICATELY, ON A VELVET PILLOW."],
		        "MoveObjectXToCurrentRoom","#POTTERY",
		        "PrintMessageX","THE VASE DROPS WITH A DELICATE CRASH."],
		    "DropUserInputObject"],
		 _throw : [
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#VASE_solo",
		        "MoveObjectXToRoomY","#VASE_solo","room_0",
		        "MoveObjectXToCurrentRoom","#POTTERY",
		        "PrintMessageX","YOU HAVE TAKEN THE VASE AND HURLED IT DELICATELY TO THE GROUND."],
		    "DropUserInputObject"],
		 _open : [
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#SARCOPH_full",
		        "SubScriptXAbortIfPass",[
		            "AssertObjectXIsInPack","#SARCOPH_full",
		            "PrintMessageX","I'D ADVISE YOU TO PUT DOWN THE SARCOPHAGUS BEFORE OPENING IT!!"],
		        "SubScriptXAbortIfPass",[
		            "AssertObjectXIsInPack","#KEY",
		            "PrintMessageX","A GLISTENING PEARL FALLS OUT OF THE SARCOPHAGUS AND ROLLS AWAY. THE SARCOPHAGUS SNAPS SHUT AGAIN.",
		            "MoveObjectXToRoomY","#PEARL","room_64",
		            "MoveObjectXToRoomY","#SARCOPH_full","room_0",
		            "MoveObjectXToCurrentRoom","#SARCOPH_empty"],
		        "PrintMessageX","YOU DON'T HAVE ANYTHING STRONG ENOUGH TO OPEN THE SARCOPHAGUS."],
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#SARCOPH_empty",
		        "SubScriptXAbortIfPass",[
		            "AssertObjectXIsInPack","#SARCOPH_empty",
		            "PrintMessageX","I'D ADVISE YOU TO PUT DOWN THE SARCOPHAGUS BEFORE OPENING IT!!"],
		        "SubScriptXAbortIfPass",[
		            "AssertObjectXIsInPack","#KEY",
		            "PrintMessageX","THE SARCOPHAGUS CREAKS OPEN, REVEALING NOTHING INSIDE. IT PROMPTLY SNAPS SHUT AGAIN."],
		        "PrintMessageX","YOU DON'T HAVE ANYTHING STRONG ENOUGH TO OPEN THE SARCOPHAGUS."],
		    "PrintMessageX","I DON'T KNOW HOW TO LOCK OR UNLOCK SUCH A THING."],
		 _wave : [
		    "PrintMessageX","NOTHING HAPPENS."],
		 _pour : [
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#WATER",
		        "MoveObjectXToRoomY","#WATER","room_0",
		        "PrintMessageX","YOUR BOTTLE IS EMPTY AND THE GROUND IS WET."],
		    "PrintMessageX","YOU CAN'T POUR THAT."],
		 _rub : [
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#LAMP_off",
		        "PrintMessageX","RUBBING THE ELECTRIC LAMP IS NOT PARTICULARLY REWARDING. ANYWAY, NOTHING EXCITING HAPPENS."],
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#LAMP_on",
		        "PrintMessageX","RUBBING THE ELECTRIC LAMP IS NOT PARTICULARLY REWARDING. ANYWAY, NOTHING EXCITING HAPPENS."],
		    "PrintMessageX","PECULIAR. NOTHING UNEXPECTED HAPPENS."],
		 _fill : [
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#BOTTLE",
		        "PrintMessageX","THERE IS NOTHING HERE WITH WHICH TO FILL THE BOTTLE."],
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#VASE_solo",
		        "PrintMessageX","DON'T BE RIDICULOUS!"],
		    "PrintMessageX","YOU CAN'T FILL THAT."],
		 _attack : [
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#BIRD",
		        "MoveObjectXToRoomY","#BIRD","room_0",
		        "PrintMessageX","THE BIRD STATUE IS NOW DEAD. ITS BODY DISAPPEARS."],
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#BIRD_boxed",
		        "MoveObjectXToRoomY","#BIRD_boxed","room_0",
		        "PrintMessageX","THE BIRD STATUE IS NOW DEAD. ITS BODY DISAPPEARS."],
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#SARCOPH_full",
		        "PrintMessageX","THE STONE IS VERY STRONG AND IS IMPERVIOUS TO ATTACK."],
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#SARCOPH_empty",
		        "PrintMessageX","THE STONE IS VERY STRONG AND IS IMPERVIOUS TO ATTACK."],
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#SERPENT",
		        "PrintMessageX","ATTACKING THE SERPENT BOTH DOESN'T WORK AND IS VERY DANGEROUS."],
		    "PrintMessageX","YOU CAN'T BE SERIOUS!"],
		 _break : [
		    "PrintMessageX","IT IS BEYOND YOUR POWER TO DO THAT."],
		 _eat : [
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#FOOD",
		        "MoveObjectXToRoomY","#FOOD","room_0",
		        "PrintMessageX","THANK YOU, IT WAS DELICIOUS!"],
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#-10-",
		        "PrintMessageX","I THINK I JUST LOST MY APPETITE."],
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#BIRD",
		        "PrintMessageX","I THINK I JUST LOST MY APPETITE."],
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#BIRD_boxed",
		        "PrintMessageX","I THINK I JUST LOST MY APPETITE."],
		    "PrintMessageX","DON'T BE RIDICULOUS!"],
		 _drink : [
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#WATER",
		        "MoveObjectXToRoomY","#WATER","room_0",
		        "PrintMessageX","THE BOTTLE IS NOW EMPTY."],
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#stream_56",
		        "PrintMessageX","YOU HAVE TAKEN A DRINK FROM THE STREAM. THE WATER TASTES STRONGLY OF MINERALS, BUT IS NOT UNPLEASANT. IT IS EXTREMELY COLD."],
		    "PrintMessageX","YOU CAN'T BE SERIOUS!"],
		 _feed : [
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#BIRD",
		        "PrintMessageX","IT'S NOT HUNGRY. BESIDES, YOU HAVE NO BIRD SEED."],
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#BIRD_boxed",
		        "PrintMessageX","IT'S NOT HUNGRY. BESIDES, YOU HAVE NO BIRD SEED."],
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#SERPENT",
		        "SubScriptXAbortIfPass",[
		            "AssertObjectXIsInPack","#BIRD_boxed",
		            "MoveObjectXToRoomY","#BIRD_boxed","room_0",
		            "PrintMessageX","THE SERPENT HAS NOW DEVOURED YOUR BIRD STATUE."],
		        "PrintMessageX","THERE IS NOTHING HERE IT WANTS TO EAT - EXCEPT PERHAPS YOU."],
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#SARCOPH_full",
		        "PrintMessageX","I'M GAME. WOULD YOU CARE TO EXPLAIN HOW?"],
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#SARCOPH_empty",
		        "PrintMessageX","I'M GAME. WOULD YOU CARE TO EXPLAIN HOW?"],
		    "SubScriptXAbortIfPass",[
		        "AssertObjectXMatchesUserInput","#-13-",
		        "PrintMessageX","THERE IS NOTHING HERE IT WANTS TO EAT - EXCEPT PERHAPS YOU."],
		    "PrintMessageX","DON'T BE RIDICULOUS!"],
		 _plugh : [
		    "JumpToTopOfGameLoop"],
		 _load : [
		    "LoadGame"],
		 _save : [
		    "SaveGame"]
		   };
		
    //
    // Command handlers
    //
			
	var getDefaultScript = function (verb) {
		return defaultHandler[verb];
	};
	
	// Public API
	return {
		getDefaultScript : getDefaultScript		
	};

}();