package tools.blend;

import java.util.ArrayList;
import java.util.List;

import tools.blend.expression.ExpressionException;
import tools.blend.expression.ParseToken;
import tools.blend.expression.ParseTokenType;

/**
 * These functions turn a tree of ParseTokens (a scanned and parsed expression) into a list
 * of CompareNodes that are wired together through their pass/fail jump labels. The CompareNodes
 * live in a complex tree of logic operators that serve only to wire them together. Once the
 * tree is built and the CompareNodes wired, there is no need for the tree. The list of
 * CompareNodes is ready to be turned into code.
 */
public final class LogicTree 
{
	
	private LogicTree() {}
	
	/**
	 * This method returns a list of CompareNodes wired together to implement the given expression.
	 * @param expression the scanned and parsed tree of ParseTokens
	 * @param tag 
	 * @return the wired up CompareNodes
	 * @throws ExpressionException if there are errors in the expression
	 */
	public static List<CompareNode> makeLogicTree(ParseToken expression, String tag) throws ExpressionException
	{
		
		// This is what we are after
		List<CompareNode> compareNodes = new ArrayList<CompareNode>();
		
		// This will be the root node of the expression flow
		CapNode cap = new CapNode(tag);

		// Recursively build the tree
		cap.addChild(LogicTree.makeBlendNode(cap,expression,compareNodes,cap));
		
		// Move the first node we hit to the front
		CompareNode n = cap.getStartingCompareNode();
		compareNodes.remove(n);
		compareNodes.add(0,n);
		
		// Resolve all jumps in the tree. Only the CompareNodes are needed now. That was
		// a lot of work just to throw it away.
		for(CompareNode cn : compareNodes) {
			cn.labelWhenPass = cn.whereDoIGoOnPass();
			cn.labelWhenFail = cn.whereDoIGoOnFail();
		}
					
		// Return the compare nodes
		return compareNodes;
	}
	
	// This is a recursive function that builds a sub-tree from the expression node.
	private static Node makeBlendNode(Node parent, ParseToken expression, List<CompareNode> compareNodes, CapNode cap) throws ExpressionException
	{
		
		if(expression.tokenType!=ParseTokenType.SUBLIST){
			CompareNode cn = new CompareNode(parent,expression,cap);
			compareNodes.add(cn);
			return cn;
		}
		
		// Maybe a "()" ... doesn't make sense
		if(expression.subList.size()==0) {
			throw new ExpressionException("Expression is empty",expression.codeLine,expression.position);
		}
		
		// Handle extra parens as in "((A==4))"
		
		if(expression.tokenType==ParseTokenType.SUBLIST && expression.subList.size()==1) {		
			AsIsNode ret = new AsIsNode(parent,cap);
			ret.addChild(makeBlendNode(ret,expression.subList.get(0),compareNodes,cap));
			return ret;			
		}
		
		// Handle "!*" ... NOT expression
		if(expression.subList.size()==2 && expression.subList.get(1).tokenType==ParseTokenType.SUBLIST) {			
			ParseToken pt = expression.subList.get(0);
			if(pt.token.equals("!")) {
				NotNode ret = new NotNode(parent,cap);
				ret.addChild(makeBlendNode(ret,expression.subList.get(1),compareNodes,cap));
				return ret;
			}			
		}
		
		// Check for logic connectors like && or ||
		ParseToken logicTypeToken = null;
		for(int x=0;x<expression.subList.size();++x) {
			if(expression.subList.get(x) instanceof ParseToken) {
				ParseToken pt = (ParseToken)expression.subList.get(x);
				if(pt.tokenType == ParseTokenType.LOGIC) {
					if(logicTypeToken==null) {
						logicTypeToken = pt;
					} else {
						if(!logicTypeToken.token.equals(pt.token)) {
							throw new ExpressionException("Logic operators are not the same: '"+
									pt.token+"' and '"+logicTypeToken.token+"'. Use parenthesis.",pt.codeLine,pt.position);
						}
					}					
				}
			}
		}
		
		// This is not a logic expression ... must be a compare-node leaf
		if(logicTypeToken==null) {			
			CompareNode cn = new CompareNode(parent,expression,cap);
			compareNodes.add(cn);
			return cn;			
		}
		
		// If we get here then this is a logic connector like "A && B && C && D"
		
		// This is a logic connector. Create the correct parent type.
		Node logic = null;
		if(logicTypeToken.token.equals("&&")) {
			logic = new AndNode(parent,cap);
		} else if(logicTypeToken.token.equals("||")) {
			logic = new OrNode(parent,cap);
		} else {
			throw new ExpressionException("Unknown logic operator '"+logicTypeToken.token+"'",
					logicTypeToken.codeLine, logicTypeToken.position);
		}
			
		// Run through the children and break them into mini-expressions between the logic operators
		ParseToken op = null;
		ParseToken lastLogicToken = null;
		for(ParseToken ps : expression.subList) {				
			if(ps.tokenType == ParseTokenType.LOGIC) {
				lastLogicToken = ps;
				if(op==null) {
					throw new ExpressionException("Expression starts with logic operator",ps.codeLine,ps.position);
				}
				logic.addChild(makeBlendNode(logic,op,compareNodes,cap));
				op = null;
			} else {
				if(op==null) {
					op = new ParseToken();
					op.tokenType = ParseTokenType.SUBLIST;
					op.subList = new ArrayList<ParseToken>();
					op.codeLine = ps.codeLine;
					op.position = ps.position;
				}
				op.subList.add(ps);
			}			
		}
		
		// The last child got filled out in the loop above
		if(op==null) {
			throw new ExpressionException("Expression ends with logic operator",lastLogicToken.codeLine,lastLogicToken.position);
		}
		logic.addChild(makeBlendNode(logic,op,compareNodes,cap));
				
		return logic;
	}

}
