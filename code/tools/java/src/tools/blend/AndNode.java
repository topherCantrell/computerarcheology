package tools.blend;


/**
 * An AND node tries all children one by one. If any fail then the
 * path is short-circuited to the parent's fail. If all pass then
 * the flow continues with the parent's pass.
 */
public class AndNode extends Node 
{

	/**
	 * This constructs a new AND node
	 * @param parent the parent node
	 * @param cap the root of the expression
	 */
	public AndNode(Node parent, CapNode cap)
	{
		super(parent,cap.getNewNodeName());		
	}

	@Override
	public String whereDoIGoOnPass(Node whichChildAmI) {
		int ci = this.getChildIndex(whichChildAmI);
		if(ci==(children.size()-1)) {
			return parent.whereDoIGoOnPass(this);
		}
		Node next = children.get(ci+1);
		return next.getStartingCompareNode().getName();		
	}

	@Override
	public String whereDoIGoOnFail(Node whichChildAmI) {
		getChildIndex(whichChildAmI);
		return parent.whereDoIGoOnFail(this);
	}

}
