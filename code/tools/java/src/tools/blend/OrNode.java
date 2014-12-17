package tools.blend;


/**
 * An OR node tries all children one by one. If any pass then the
 * path is short-circuited to the parent's pass. If all fail then
 * the flow continues with the parent's fail.
 */
public class OrNode extends Node {
	
	/**
	 * This constructs a new OR node
	 * @param parent the parent node
	 * @param cap the root of the expression
	 */
	public OrNode(Node parent, CapNode cap)
	{
		super(parent,cap.getNewNodeName());		
	}

	@Override
	public String whereDoIGoOnPass(Node whichChildAmI) {
		getChildIndex(whichChildAmI);
		return parent.whereDoIGoOnPass(this);
	}

	@Override
	public String whereDoIGoOnFail(Node whichChildAmI) {
		int ci = this.getChildIndex(whichChildAmI);
		if(ci==(children.size()-1)) {
			return parent.whereDoIGoOnFail(this);
		}
		Node next = children.get(ci+1);
		return next.getStartingCompareNode().getName();		
	}

}
