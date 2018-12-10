
var PARSE = function() {

	// Pyramid uses a fixed set of words, and you can tell which words the code knows
	// by generating error messages. For instance "GET BLAH" produces "GET WHAT?" and
	// "GET LAMP" produces "I SEE NO LAMP HERE."
	
	// Two words can mean the same thing. DROP, FREE, and DISCARD all mean "_drop", where
	// "_drop" is the word's function referenced in scripts.
	
	// Words have a grammar type:
	//  - noun  : the word refers to an object in the current room or in the pack
	//  - alone : the word is a stand-alone action verb (like NORTH or SCORE)
	//  - withNounInPack  : the word is a verb that requires a noun that is in the pack
	//  - withNounInSight : the word is a verb that requires a noun that is in the current room or pack
	
	// The grammar type allows the parser to perform most of the syntax checking. If a verb requires a
	// noun but none was given, the parser generates an error. If the verb requires a noun in the pack
	// but the given noun is not in the pack then the parser generates an error. Thus the individual 
	// scripts don't have to perform extensive sanity checks on the VERB+NOUN combination.
        
    // Several objects might use the same noun word. "WATER" for instance might refer to the
    // water-in-the-bottle or it might refer to the stream-in-room-56. The parser picks the first object
    // from the room or pack that matches the noun. The "object" array indicates what object go
    // with each noun.
    
    var WORDS = {
    
    	// Nouns
        LAMP    : { grammar: 'noun', object: ['#LAMP_off', '#LAMP_on', '#LAMP_dead']},
        LANTER  : { grammar: 'noun', object: ['#LAMP_off', '#LAMP_on', '#LAMP_dead']},
        BOX     : { grammar: 'noun', object: ['#BOX']},
        SCEPTER : { grammar: 'noun', object: ['#SCEPTER']},
        BIRD    : { grammar: 'noun', object: ['#BIRD', '#BIRD_boxed']},
        STATUE  : { grammar: 'noun', object: ['#BIRD', '#BIRD_boxed']},
        PILLOW  : { grammar: 'noun', object: ['#PILLOW']},
        VELVET  : { grammar: 'noun', object: ['#PILLOW']},
        SERPEN  : { grammar: 'noun', object: ['#SERPENT']},
        SARCOP  : { grammar: 'noun', object: ['#SARCOPH_full', '#SARCOPH_empty']},
        MAGAZI  : { grammar: 'noun', object: ['#MAGAZINES']},
        ISSUE   : { grammar: 'noun', object: ['#MAGAZINES']},
        EGYPTI  : { grammar: 'noun', object: ['#MAGAZINES']},
        FOOD    : { grammar: 'noun', object: ['#FOOD']},
        BOTTLE  : { grammar: 'noun', object: ['#BOTTLE']},
        WATER   : { grammar: 'noun', object: ['#WATER', '#STREAM_56']},
        PLANT   : { grammar: 'noun', object: ['#PLANT_A', '#PLANT_B', '#PLANT_C']},
        BEANST  : { grammar: 'noun', object: ['#PLANT_A', '#PLANT_B', '#PLANT_C']},
        MACHIN  : { grammar: 'noun', object: ['#MACHINE']},
        VENDIN  : { grammar: 'noun', object: ['#MACHINE']},
        BATTER  : { grammar: 'noun', object: ['#BATTERIES_fresh', '#BATTERIES_worn']},
        GOLD    : { grammar: 'noun', object: ['#GOLD']},
        NUGGET  : { grammar: 'noun', object: ['#GOLD']},
        DIAMON  : { grammar: 'noun', object: ['#DIAMONDS']},
        SILVER  : { grammar: 'noun', object: ['#SILVER']},
        BARS    : { grammar: 'noun', object: ['#SILVER']},
        JEWELR  : { grammar: 'noun', object: ['#JEWELRY']},
        COINS   : { grammar: 'noun', object: ['#COINS']},
        CHEST   : { grammar: 'noun', object: ['#CHEST']},
        TREASU  : { grammar: 'noun', object: ['#CHEST']},
        EGGS    : { grammar: 'noun', object: ['#NEST']},
        EGG     : { grammar: 'noun', object: ['#NEST']},
        NEST    : { grammar: 'noun', object: ['#NEST']},
        KEY     : { grammar: 'noun', object: ['#KEY']},
        VASE    : { grammar: 'noun', object: ['#VASE_pillow', '#VASE_solo']},
        SHARDS  : { grammar: 'noun', object: ['#POTTERY']},
        POTTER  : { grammar: 'noun', object: ['#POTTERY']},
        EMERAL  : { grammar: 'noun', object: ['#EMERALD']},
        PEARL   : { grammar: 'noun', object: ['#PEARL']},        
        
        // Verbs 
        N       : {grammar: 'alone', func: '_n'},
        NORTH   : {grammar: 'alone', func: '_n'},
        E       : {grammar: 'alone', func: '_e'},
        EAST    : {grammar: 'alone', func: '_e'},
        S       : {grammar: 'alone', func: '_s'},
        SOUTH   : {grammar: 'alone', func: '_s'},
        W       : {grammar: 'alone', func: '_w'},
        WEST    : {grammar: 'alone', func: '_w'},
        NE      : {grammar: 'alone', func: '_ne'},
        NORTHE  : {grammar: 'alone', func: '_ne'},
        SE      : {grammar: 'alone', func: '_se'},
        SOUTHE  : {grammar: 'alone', func: '_se'},
        SW      : {grammar: 'alone', func: '_sw'},
        SOUTHW  : {grammar: 'alone', func: '_sw'},
        NW      : {grammar: 'alone', func: '_nw'},
        NORTHW  : {grammar: 'alone', func: '_nw'},
        U       : {grammar: 'alone', func: '_u'},
        UP      : {grammar: 'alone', func: '_u'},
        D       : {grammar: 'alone', func: '_d'},
        DOWN    : {grammar: 'alone', func: '_d'},
        IN      : {grammar: 'alone', func: '_in'},
        INSIDE  : {grammar: 'alone', func: '_in'},
        OUT     : {grammar: 'alone', func: '_out'},
        OUTSID  : {grammar: 'alone', func: '_out'},
        CROSS   : {grammar: 'alone', func: '_cross'},
        LEFT    : {grammar: 'alone', func: '_left'},
        RIGHT   : {grammar: 'alone', func: '_right'},
        JUMP    : {grammar: 'alone', func: '_jump'},
        CLIMB   : {grammar: 'alone', func: '_climb'},
        PANEL   : {grammar: 'alone', func: '_panel'},
        BACK    : {grammar: 'alone', func: '_back'},
        SWIM    : {grammar: 'alone', func: '_swim'},
        ON      : {grammar: 'alone', func: '_on'},
        OFF     : {grammar: 'alone', func: '_off'},
        QUIT    : {grammar: 'alone', func: '_quit'},
        STOP    : {grammar: 'alone', func: '_quit'},
        SCORE   : {grammar: 'alone', func: '_score'},
        INVENT  : {grammar: 'alone', func: '_inv'},
        LOOK    : {grammar: 'alone', func: '_look'},
        //
        DROP    : {grammar: 'withNounInPack', func: '_drop'},
        RELEAS  : {grammar: 'withNounInPack', func: '_drop'},
        FREE    : {grammar: 'withNounInPack', func: '_drop'},
        DISCAR  : {grammar: 'withNounInPack', func: '_drop'},
        LIGHT   : {grammar: 'withNounInPack', func: '_on'},
        WAVE    : {grammar: 'withNounInPack', func: '_wave'},
        SHAKE   : {grammar: 'withNounInPack', func: '_wave'},
        SWING   : {grammar: 'withNounInPack', func: '_wave'},
        POUR    : {grammar: 'withNounInPack', func: '_pour'},
        RUB     : {grammar: 'withNounInPack', func: '_rub'},
        THROW   : {grammar: 'withNounInPack', func: '_throw'},
        TOSS    : {grammar: 'withNounInPack', func: '_throw'},
        FILL    : {grammar: 'withNounInPack', func: '_fill'},
        //
        TAKE    : {grammar: 'withNounInSight', func: '_get'},
        GET     : {grammar: 'withNounInSight', func: '_get'},
        CARRY   : {grammar: 'withNounInSight', func: '_get'},
        CATCH   : {grammar: 'withNounInSight', func: '_get'},
        STEAL   : {grammar: 'withNounInSight', func: '_get'},
        CAPTUR  : {grammar: 'withNounInSight', func: '_get'},
        OPEN    : {grammar: 'withNounInSight', func: '_open'},
        ATTACK  : {grammar: 'withNounInSight', func: '_attack'},
        KILL    : {grammar: 'withNounInSight', func: '_attack'},
        HIT     : {grammar: 'withNounInSight', func: '_attack'},
        FIGHT   : {grammar: 'withNounInSight', func: '_attack'},
        FEED    : {grammar: 'withNounInSight', func: '_feed'},
        EAT     : {grammar: 'withNounInSight', func: '_eat'},
        DRINK   : {grammar: 'withNounInSight', func: '_drink'},
        BREAK   : {grammar: 'withNounInSight', func: '_break'},        
        SMASH   : {grammar: 'withNounInSight', func: '_break'},
        //
        LOAD    : {grammar: 'alone', func: '_load'},
        SAVE    : {grammar: 'alone', func: '_save'},
        PLUGH   : {grammar: 'alone', func: '_plugh'}
    
    };
    
    // Used to "randomize" general failure error messages  
    var errRoll = 0;   
    var errs = [" WHAT?", "I DON'T KNOW THAT WORD.", "I DON'T UNDERSTAND.", "I DON'T KNOW WHAT YOU MEAN."];
    
    // In case the user gives one and we ask for clarification
    var heldNoun = null;
    var heldVerb = null;
    
    var my = {};
        
    /**
     * This function matches against the words. It stops after 6 characters and
     * skips any remaining user input. This is how Pyramid works.
     * @param input the input word text
     * @return the matching word (if any)
     */
    var findWord = function(input) {
        var inup = input.toUpperCase();        
        for(var word in WORDS) {
            if(WORDS.hasOwnProperty(word)) {
                if(inup==word || (inup.length>5 && word.length>5 && inup.indexOf(word)===0)) {                    
                    return WORDS[word];                   
                }
            }
        }                
    };
        
    /**
     * This function parses a command input into a list of known words and returns at most two
     * of them in VERB+NOUN order.
     * @param command the command input
     * @return undefined -- general error was given (just repeat the command loop)
     * @return {verb} -- single word action command (like "NORTH")
     * @return {verb, noun} -- two word commands like "GET LAMP"
     */
    var parseInput = function(command) {
    	
    	// LOAD is a special command here
    	if(command.toUpperCase().indexOf("LOAD ")==0) {
    		my.loadState = command.substring(5).trim();
    		command = "LOAD";
    	}
    	
        var words = command.toUpperCase().trim().split(/\W+/);
                       
        // Ignore blank input
        if(words[0].length===0) return;
                
        // We got something so parse it into known words. We ignore words we
        var noun = null;
        var verb = null;
        for(var x=0;x<words.length;++x) {
            var p = findWord(words[x]);
            if(p) {
                if(p.grammar=="noun") {
                    noun = {original: words[x], word: p};
                } else {
                    verb = {original: words[x], word: p};
                }
            }            
        }
        
        // General failure. We got SOMETHING but it was nothing we know.
        if(noun===null && verb===null) {
            errRoll = (errRoll+1)&3;
            println(errs[errRoll]);
            heldNoun = null;
            heldVerb = null;        
            return;
        }
        
        // If we are holding a word from last input then use it in place of a word not-given.
        if(!noun && heldNoun) {
        	noun = heldNoun;
            heldNoun = null;                        
        }    
        if(!verb && heldVerb) {
        	verb = heldVerb;
            heldVerb = null;            
        }
        // We don't ever hold words over one turn
        heldNoun = null;
        heldVerb = null;   
        
        // A noun by itself is never a valid command
        if(noun && !verb) {
        	for (var x=0;x<noun.word.object.length;++x) {
        		var o = OBJS.getExactObjectByName(noun.word.object[x]);
        		var po = OBJS.getTopObjectByName(o.name);
        		if (po.location==="pack" || po.location===GAME.currentRoom) {
        			println("WHAT DO YOU WANT ME TO DO WITH THE "+noun.original+"?");
                	heldNoun = noun;
                	return;
        		}
        	}
            println("I SEE NO "+noun.original+" HERE.");
            heldNoun = null;                             
            return;
        }
                        
        // An action command ... ignore noun (if any)
        if(verb && verb.word.grammar=="alone") {
            // Single action word ... OK       
            return {verb: verb.word.func}; 
        }
        
        // Verb that requires a noun, but none given
        if(verb && !noun) {     
            println(verb.original + " WHAT?");  
            heldVerb = verb;                     
            return;        
        }
        
        // At this point we have a verb and a noun
        // The noun could refer to several objects. Figure out
        // which one and store a pointer to it.
        
        if(verb.word.grammar=="withNounInSight") {
        	// Can be in pack or room        
        	for (var x=0;x<noun.word.object.length;++x) {
        		var o = OBJS.getExactObjectByName(noun.word.object[x]);
        		var po = OBJS.getTopObjectByName(o.name);
        		if (po.location==="pack" || po.location==GAME.currentRoom) {
        			noun.obj = o;
        			break;
        		}
        	}        	
        	if (!noun.obj) {
        		println("I SEE NO "+noun.original+" HERE.");
                return;
        	}        
        } else {
            // must be "nounInPack"
            // Must be in pack        
        	for (var x=0;x<noun.word.object.length;++x) {
        		var o = OBJS.getExactObjectByName(noun.word.object[x]);
        		var po = OBJS.getTopObjectByName(o.name);
        		if (po.location==="pack") {
        			noun.obj = o;
        			break;
        		}
        	}        	
        	if (!noun.obj) {
        		println("YOU AREN'T CARRYING IT.");
                return;
        	}                    
        }
                
        // Good verb/noun combo
        return {verb: verb.word.func, noun: noun.obj};                
                        
    };
    
    // Public API
    my.parseInput = parseInput;
    return my;    
   
}();

