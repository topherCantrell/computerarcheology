package tools.blend;

/**
 * This class is a "not" relationship between parent and child. This node crosses
 * the pass/fail connectors between parent and child. 
 */
public class NotNode extends Node {

	/**
	 * This creates a new NotNode
	 * @param parent the parent node
	 * @param cap the root of the expression
	 */
	public NotNode(Node parent, CapNode cap)
	{
		super(parent,cap.getNewNodeName());		
	}
	
	@Override
	public String whereDoIGoOnPass(Node whichChildAmI) {
		getChildIndex(whichChildAmI);
		return parent.whereDoIGoOnFail(this);
	}

	@Override
	public String whereDoIGoOnFail(Node whichChildAmI) {
		getChildIndex(whichChildAmI);
		return parent.whereDoIGoOnPass(this);
	}


}
