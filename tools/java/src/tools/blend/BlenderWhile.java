package tools.blend;

import java.util.ArrayList;
import java.util.List;

import tools.blend.expression.ExpressionException;
import tools.blend.expression.ExpressionParser;
import tools.blend.expression.ParseToken;
import tools.code.CodeLine;
import tools.code.CodeLineInputStream;
import tools.processor.ProcessorBlendEntry;
import tools.processor.ProcessorFamily;

public class BlenderWhile 
{
	
	static CodeLine parse(List<CodeLine> codeLines, int start, ProcessorFamily family)
	{

		// while(exp) {
		//   #body#
		// }
		//
		// _begin:
		// jump _continue
		// _pass:
		//   #body#		
		// _continue:
		// if(exp) {
		//   jump _pass
		// }
		// _break:
		// _fail:
		// _end:		

		try {

			// This is the code-generation info from the family XML
			List<ProcessorBlendEntry> blendEntries = family.getBlendEntries();
			String blendJump = family.getBlendJump();

			// Character-at-a-time input from the code lines
			//
			CodeLine rootLine = codeLines.get(start);
			int pos = rootLine.getOpcodeString().indexOf("while");
			CodeLineInputStream cis = new CodeLineInputStream(codeLines,start,pos+5);

			// Parse the expression
			//
			int startExpression = cis.getCurrentLineNumber(); 
			// Scan the expression from "(" to matching ")". The cis is left pointing
			// beyond the expression.
			List<ParseToken> expressionTokens = ExpressionParser.scanExpression(cis);
			// Find the line with the open "{". This could be on a line by itself.		
			Blender.findOpenBrace(cis);			
			// Expression ends here ...
			int endExpression = cis.getCurrentLineNumber();			

			// Generate the code for the expression. We get a name for our construct in return.
			List<CodeLine> exprCode = new ArrayList<CodeLine>();
			String treeName = Blender.parseExpression(exprCode, codeLines, rootLine, 
					expressionTokens, startExpression, endExpression, blendEntries, blendJump, true,"o");

			// Extract the loop-block
			//
			// The pass block assembly starts on the very next line after the "{"
			int startPass = cis.getCurrentLineNumber()+1;
			// Find the line with the matching closing "}"
			Blender.findCloseBrace(cis,0);
			int closePass = cis.getCurrentLineNumber();
			// The pass-block assembly ends one before the closing brace
			int endPass = closePass-1;
			// Note an empty block
			if(endPass<startPass) {
				startPass=-1;
				endPass=-1;
			}

			// End of the whole thing
			int endOfConstruct = cis.getCurrentLineNumber();

			// This will hold the generated code
			List<CodeLine> generatedCode = new ArrayList<CodeLine>();




			// Start the whole thing with a label (good in the listing file)
			Blender.addCodeLine(generatedCode, rootLine, treeName+"_begin:");
			
			// Jump to the continue label where the condition is checked
			String jump = ProcessorBlendEntry.sub(blendJump, "$DEST$", treeName+"_continue");
			Blender.addCodeLine(generatedCode, rootLine, jump);
			
			// Label for the body ... loops back to here if expression passes
			Blender.addCodeLine(generatedCode, rootLine, treeName+"_pass:");
			// Add any loop-block lines to the generated code. There may not be any.
			if(startPass>=0) {
				for(int x=startPass;x<=endPass;++x) {
					CodeLine co = codeLines.get(x);
					generatedCode.add(co);					
				}				
			}	
			
			// Start of expression. The "continue" instruction comes here
			Blender.addCodeLine(generatedCode, rootLine, treeName+"_continue:");
			
			// Stick in the expression
			generatedCode.addAll(exprCode);
						
			// Start of expression. The "break" instruction comes here
			Blender.addCodeLine(generatedCode, rootLine, treeName+"_break:");
			
			// If the expression fails then the loop ends here
			Blender.addCodeLine(generatedCode, rootLine, treeName+"_fail:");
			
			// End of the loop
			Blender.addCodeLine(generatedCode, rootLine, treeName+"_end:");
			
			
			
			// Remove the entire list from the original. Insert the newly generated.
			for(int x=0;x<endOfConstruct-start+1;++x) {
				codeLines.remove(start);
			}
			codeLines.addAll(start,generatedCode);		

		} catch (ExpressionException e) {
			// Put as much information about the error as possible into the code line's error note
			e.codeLine.setError("At character "+(e.position+1)+". "+e.getMessage());
			return e.codeLine;
		}

		return null;
	}

}
