package tools.blend;

import tools.blend.expression.ParseToken;
import tools.blend.expression.ParseTokenType;

/**
 * A compare-node is where the action takes place in an expression tree. All
 * other nodes just wire up the compare-nodes.
 */
public class CompareNode extends Node {
	
	ParseToken expression;
	
	String labelWhenFail;
	String labelWhenPass;
	
	String constructName;
	
	/**
	 * This creates a new CompareNode
	 * @param parent the parent node
	 * @param expression the expression to generate code for
	 * @param cap the root of the expression
	 */
	public CompareNode(Node parent, ParseToken expression, CapNode cap)
	{
		super(parent,cap.getNewNodeName());
		this.expression = expression;
		children = null; // In case someone tries to add children
		this.constructName = cap.getConstructName();
	}
	
	/**
	 * This returns the name of the construct unique to the tree the node is in.
	 * @return the tree's name
	 */
	public String getTreeName() {
		return constructName;
	}
	
	/**
	 * This method returns the expression
	 * @return the expression
	 */
	public ParseToken getExpression() {
		return expression;
	}

	public String whereDoIGoOnPass() {
		return parent.whereDoIGoOnPass(this);
	}
	
	public String whereDoIGoOnFail() {
		return parent.whereDoIGoOnFail(this);
	}
	
	@Override
	public String whereDoIGoOnPass(Node whichChildAmI) {
		throw new RuntimeException("Trying to go deeper than a CompareNode");
	}

	@Override
	public String whereDoIGoOnFail(Node whichChildAmI) {
		throw new RuntimeException("Trying to go deeper than a CompareNode");
	}
	
	public String toString()
	{
		if(expression.tokenType==ParseTokenType.SUBLIST){
			String ret = "";
			for(ParseToken pt : expression.subList){
				ret = ret + pt.token;
			}
			return ret;
		}
		return expression.token;
	}

}
