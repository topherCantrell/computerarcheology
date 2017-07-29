package tools.blend;

import java.util.List;
import java.util.StringTokenizer;

import tools.assembler.Assembler;
import tools.blend.expression.ExpressionException;
import tools.blend.expression.ExpressionParser;
import tools.blend.expression.ParseToken;
import tools.blend.expression.ParseTokenType;
import tools.code.CU;
import tools.code.CodeLine;
import tools.code.CodeLineInputStream;
import tools.processor.ProcessorBlendEntry;
import tools.processor.ProcessorFamily;

public class Blender {
	
	static void addCodeLine(List<CodeLine> generatedCode, CodeLine reference, String code)
	{
		addCodeLine(generatedCode,reference,code,"Blended");
	}
	static void addCodeLine(List<CodeLine> generatedCode, CodeLine reference, String code, String comment)
	{
		generatedCode.add(
				new CodeLine(CU.padTo(code,30)+"; "+comment,
						reference.getFilename(), 
						reference.getLineNumber()
						)
				); 
	}
	
	static String parseExpression(			
			List<CodeLine> generatedCode, List<CodeLine> codeLines, CodeLine rootLine, 
			List<ParseToken> expressionTokens, int startExpression, int endExpression,
			List<ProcessorBlendEntry> blendEntries, String blendJump, 
			boolean branchPass, String tag
			) throws ExpressionException
		{

		// We have the expression and the indices for the blocks

		// Turn the list of scanned tokens into a tree of expression sub-lists. Since the 
		// expression is wrapped in a "( ... )" this should result in one root ParseToken
		// in the list of type "SUBLIST".
		ExpressionParser.parseExpressionTree(expressionTokens);
		if(expressionTokens.size()!=1) {
			throw new RuntimeException("Expected one node");
		}
		ParseToken expressionToken = expressionTokens.get(0);
		if(expressionToken.tokenType!=ParseTokenType.SUBLIST){
			throw new RuntimeException("Expected a sublist");
		}												
		// Build the logic tree (this is the secret-sauce)
		List<CompareNode> compareNodes = LogicTree.makeLogicTree(expressionToken,tag);
		String treeName = compareNodes.get(0).getTreeName();

		// Now to make the code	
		
		// For the listing ... show the expression commented out
		for(int x=startExpression;x<=endExpression;++x) {
			CodeLine oc = codeLines.get(x);
			CodeLine nc = new CodeLine(";"+oc.getOriginalText(),oc.getFilename(),oc.getLineNumber());
			generatedCode.add(nc);				
		}

		// Turn each compare node in the expression to code
		for(int x=0;x<compareNodes.size();++x) {				
			CompareNode cn = compareNodes.get(x);				
			String left = "";
			String op="";
			String right = "";

			// Pick out the "left", "op", and "right" of the compare fragment
			ParseToken pt = cn.getExpression();
			if(pt.tokenType == ParseTokenType.SUBLIST) {
				if(pt.subList.size()!=3) {
					throw new ExpressionException("Syntax error '"+cn+"'", pt.codeLine, pt.position);
				}
				ParseToken pt2 = pt.subList.get(0);
				ParseToken pt3 = pt.subList.get(1);
				ParseToken pt4 = pt.subList.get(2);
				if(pt2.tokenType!=ParseTokenType.SYMBOL ||
						pt3.tokenType!=ParseTokenType.COMPARE ||
						pt4.tokenType!=ParseTokenType.SYMBOL) {
					throw new ExpressionException("Syntax error '"+cn+"'", pt.codeLine, pt.position);
				}					
				left = pt2.token;
				op = pt3.token;
				right = pt4.token;					
			} else if(pt.tokenType==ParseTokenType.SYMBOL) {
				left = pt.token;
			} else {
				throw new ExpressionException("Syntax error '"+cn+"'", pt.codeLine, pt.position);
			}

			// Find the matching entry in the family XML
			ProcessorBlendEntry fnd = null;
			for(ProcessorBlendEntry be : blendEntries) {
				if(!be.left.equals("*") && !be.left.equals(left)) continue;
				if(!be.op.equals("*") && !be.op.equals(op)) continue;
				if(!be.right.equals("*") && !be.right.equals(right)) continue;
				fnd = be;
				break;
			}				
			if(fnd==null) {
				throw new ExpressionException("Cannot code for '"+cn+"'", pt.codeLine, pt.position);
			}
			
			String codeSkel = null;
			if(branchPass) {
				// We want to flow through if there is a fail. But if there is is no
				// branchPass (flowFail) then use the flowPass and tack on a jump.
				codeSkel = fnd.branchPass;
				if(codeSkel == null) {
					codeSkel = fnd.branchFail+";"+ProcessorBlendEntry.sub(blendJump,"$DEST$","$PASS$");
				}
			} else {
				// We want to flow through if there is a pass. But if there is is no
				// branchFail (flowPass) then use the flowFail and tack on a jump.
				codeSkel = fnd.branchFail;
				if(codeSkel == null) {
					codeSkel = fnd.branchPass+";"+ProcessorBlendEntry.sub(blendJump,"$DEST$","$FAIL$");
				}
			}

			// Fill in the values and labels
			codeSkel = ProcessorBlendEntry.sub(codeSkel, "$RIGHT$", right);
			codeSkel = ProcessorBlendEntry.sub(codeSkel, "$LEFT$",  left);
			codeSkel = ProcessorBlendEntry.sub(codeSkel, "$PASS$",  cn.labelWhenPass);
			codeSkel = ProcessorBlendEntry.sub(codeSkel, "$FAIL$",  cn.labelWhenFail);

			// Create new CodeLines for each code line
			StringTokenizer st = new StringTokenizer(codeSkel,";");
			boolean first=true;
			int constCnt = 1;
			while(st.hasMoreElements()) {					
				String tok = CU.padTo(st.nextToken(),30);
				CodeLine gc = new CodeLine(tok+"; ("+constCnt+") "+left+op+right, pt.codeLine.getFilename(), pt.codeLine.getLineNumber());
				++constCnt;
				generatedCode.add(gc);
				if(first) {
					first=false;
					gc.getLabels().add(cn.name);
				}
			}				

		}	

		return treeName;

	}
		
	
	static void findOpenBrace(CodeLineInputStream cis) throws ExpressionException
	{
		CodeLine startCodeLine = cis.getCurrentLine();
		int pos = cis.getCurrentPosition();
		
		while(true) {
			int n = cis.read();
			if(n<0) {
				throw new ExpressionException("Could not find an open brace",startCodeLine,pos);
			}
			if(n=='\n' || n==' ' || n=='\t') {
				continue;
			}
			if(n!='{') {
				throw new ExpressionException("Expected an open brace but found '"+(char)n+"'",
						cis.getCurrentLine(),cis.getCurrentPosition()-1);
			}
			return;
		}
	}
	
	static void findCloseBrace(CodeLineInputStream clis, int initialLevel) throws ExpressionException
	{
		
		CodeLine startCodeLine = clis.getCurrentLine();
		int pos = clis.getCurrentPosition();
		
		int level = initialLevel;
		boolean escapeMode = false;
		char waitClose = 0;		
		
		while(true) {
			int n = clis.read();
			if(n<0) {
				throw new ExpressionException("Missing close brace",startCodeLine,pos);
			}
			
			// If a character was just skip it
			if(escapeMode) {				
				continue;
			}
						
			// Check starting an escape sequence
			if(n=='\\') {
				escapeMode=true;
				continue;
			}
			
			// Ignore new-lines and spaces in an expression
			if(n=='\n' || n==' ' || n=='\t') {
				continue;
			}
						
			// If we are in a quote (or tick) then add blindly until we
			// reach the end of the sequence
			if(waitClose!=0) {
				if(n==waitClose) {
					waitClose=0;
				}
				continue;
			}
			
			// Check if we are starting a sequence
			if(n=='\'' || n=='"') {				
				waitClose = (char)n;
				continue;				
			}
			
			// Close brace
			if(n=='}') {
				--level;
				if(level<0) {
					return;
				}
				continue;
			}
			
			// Open paren ... just count
			if(n=='{') {
				++level;
			}
			
		}		
	}
		
	public static CodeLine blend(List<CodeLine> codeLines, ProcessorFamily family) 
	{
	
		boolean changed = true;
		while(changed) {
			changed = false;
			for(int x=0;x<codeLines.size();++x) {
				CodeLine line = codeLines.get(x);
				if(line.getOpcodeString()==null) continue;
				
				if(line.getOpcodeString().startsWith("if(")) {
					CodeLine err = BlenderIf.parse(codeLines,x,family);
					if(err!=null) {
						return err;
					}
					changed = true;
					break;
				}
				
				if(line.getOpcodeString().startsWith("while(")) {
					CodeLine err = BlenderWhile.parse(codeLines,x,family);
					if(err!=null) {
						return err;
					}
					changed = true;
					break;
				}
				
				if(line.getOpcodeString().startsWith("do{") || line.getOpcodeString().startsWith("do {")) {
					CodeLine err = BlenderDo.parse(codeLines,x,family);
					if(err!=null) {
						return err;
					}
					changed = true;
					break;
				}
				
			}
		}
		
		for(int x=0;x<codeLines.size();++x) {
			CodeLine line = codeLines.get(x);
			String s = line.getOpcodeString();
			if(s==null) continue;
			if(s.equals("break")) {
				int level=0;
				boolean fnd=false;
				for(int y=x+1;y<codeLines.size();++y) {
					s = codeLines.get(y).getOpcodeString().trim();
					if(s==null || !s.startsWith("__Blend_o_")) continue;
					if(s.endsWith("_begin:")) {
						++level;
						continue;
					}
					if(s.endsWith("_end:")) {
						--level;
						continue;
					}
					if(s.endsWith("_break:") && level==0) {
						String jump = family.getBlendJump();
						jump = ProcessorBlendEntry.sub(jump, "$DEST$", s.substring(0,s.length()-1));
						codeLines.set(x, new CodeLine(CU.padTo(jump, 30)+"; "+line.getOriginalText(),line.getFilename(),line.getLineNumber()));
						fnd=true;
						break;
					}
				}
				if(!fnd) {
					line.setError("No 'break' destination found.");
					return line;
				}
			} else if(s.equals("continue")) {
				int level=0;
				boolean fnd=false;
				for(int y=x-1;y>=0;--y) {
					s = codeLines.get(y).getOpcodeString().trim();
					if(s==null || !s.startsWith("__Blend_o_")) continue;
					if(s.endsWith("_begin:")) {
						++level;
						continue;
					}
					if(s.endsWith("_end:")) {
						--level;
						continue;
					}
					if(s.endsWith("_continue:") && level==0) {
						String jump = family.getBlendJump();
						jump = ProcessorBlendEntry.sub(jump, "$DEST$", s.substring(0,s.length()-1));
						codeLines.set(x, new CodeLine(CU.padTo(jump, 30)+"; "+line.getOriginalText(),line.getFilename(),line.getLineNumber()));
						fnd=true;
						break;
					}
				}
				if(!fnd) {
					line.setError("No 'continue' destination found.");
					return line;
				}
			}
		}
				
		return null;
	}
	
	public static void main(String [] args) throws Exception
	{
		
		// Shortcut to the Assembler for testing. The Assembler calls us back.
		Assembler.main(args);
				
	}

}
