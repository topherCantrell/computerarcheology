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

public class BlenderIf 
{
	
	static CodeLine parse(List<CodeLine> codeLines, int start, ProcessorFamily family)
	{
		
		// if(exp) {
		//   #pass#
		// } else {
		//   #fail#
		// }
		// 
		// Also handles chains of "else if" by moving the "if" part to the next line
		// and adding a "}" to the end of the construct.
		//
		// _begin:
		// expression-code
		// _pass:
		//   #pass#
		// jump _end (skip if no "else" section)
		// _fail:
		//   #fail#  (skip if no "else" section)
		// _end:
		
		try {
			
			// This is the code-generation info from the family XML
			List<ProcessorBlendEntry> blendEntries = family.getBlendEntries();
			String blendJump = family.getBlendJump();
						
			// Character-at-a-time input from the code lines
			//
			CodeLine rootLine = codeLines.get(start);
			int pos = rootLine.getOpcodeString().indexOf("if");
			CodeLineInputStream cis = new CodeLineInputStream(codeLines,start,pos+2);
						
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
					expressionTokens, startExpression, endExpression, blendEntries, blendJump,false,"i");
			
			// Extract the pass-block
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
			
			// Parse the fail-block
			//
			// Check for an "else" on the same line with the closing brace as in " } else "
			int startFail = -1;
			int endFail = -1;
			int endOfConstruct = cis.getCurrentLineNumber();
			
			if(cis.getCurrentLine().getOpcodeString().indexOf("else")>=0) {				
				
				String elseIf = null;
				int ei = cis.getCurrentLine().getOpcodeString().indexOf("else if");
				if(ei>=0) {
					elseIf = cis.getCurrentLine().getOpcodeString().substring(ei+5);
				}
				startFail = cis.getCurrentLineNumber()+1;
				cis = new CodeLineInputStream(codeLines,startFail,0);
				
				while(true) {
					// Find the line with the matching closing "}". Skip through sequences of "else if".
					Blender.findCloseBrace(cis,-1);
					if(cis.getCurrentLine().getOpcodeString().indexOf("else")<0) {
						break;
					}					
				}				
						
				endFail = cis.getCurrentLineNumber()-1;
				
				if(elseIf!=null) {
					// Insert the elseIf as the first line in the fail.									
					CodeLine co = codeLines.get(startFail);
					codeLines.add(startFail,new CodeLine(elseIf,co.getFilename(),co.getLineNumber()));
					++endFail;
					// Insert a "}" line at endFail
					co = codeLines.get(endFail);
					codeLines.add(endFail+1,new CodeLine("}",co.getFilename(),co.getLineNumber()));
					++endFail;
				}				
				
				endOfConstruct = endFail+1;
				
			}
			// Note an empty block
			if(endFail<startFail) {
				startFail=-1;				
			}
									
			// This will hold the generated code
			List<CodeLine> generatedCode = new ArrayList<CodeLine>();
						
			
			
			
			// Start the whole thing with a label (good in the listing file)
			Blender.addCodeLine(generatedCode, rootLine, treeName+"_begin:");
			
			// Next (first) comes the expression code
			generatedCode.addAll(exprCode);
								
			// Add the pass block
			//
			// The code falls into the pass block (if any). Add the label for the pass block.
			Blender.addCodeLine(generatedCode, rootLine, treeName+"_pass:");			
			// Add any pass-block lines to the generated code. There may not be any.
			if(startPass>=0) {
				for(int x=startPass;x<=endPass;++x) {
					CodeLine co = codeLines.get(x);
					generatedCode.add(co);					
				}				
			}			
			// If there is a fail block then we have to jump to the end. Otherwise we can just
			// fall straight through.
			if(startFail>=0) {
				String jump = ProcessorBlendEntry.sub(blendJump, "$DEST$", treeName+"_end");
				Blender.addCodeLine(generatedCode, rootLine, jump);
			}
			
			// Show the commented out end of the pass block brace line
			CodeLine co = codeLines.get(closePass);
			generatedCode.add(new CodeLine(";"+co.getOriginalText(),co.getFilename(),co.getLineNumber()));
			
			// Add the fail (else) block if there is one
			//
			// Add a label for the fail-block
			Blender.addCodeLine(generatedCode, rootLine,treeName+"_fail:"); 
			
			// If there is a fail block, add the lines and the commented out end
			if(startFail>=0) {					
				for(int x=startFail;x<=endFail;++x) {
					co = codeLines.get(x);					
					generatedCode.add(co);
				}
				co = codeLines.get(endFail+1);
				generatedCode.add(new CodeLine(";"+co.getOriginalText(),co.getFilename(),co.getLineNumber()));
			} else if(endFail>0) {
				// In case there was an end but the block was empty
				co = codeLines.get(endFail);
				generatedCode.add(new CodeLine(";"+co.getOriginalText(),co.getFilename(),co.getLineNumber()));
			}
			
			// Add the label for the end of the construct
			Blender.addCodeLine(generatedCode, rootLine,treeName+"_end:"); 
			
			
			
						
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

		return null; // Success

	}

}
