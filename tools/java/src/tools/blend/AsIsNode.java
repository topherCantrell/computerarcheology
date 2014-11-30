package tools.blend;

/**
 * Expression may contain needless parenthesis ... like "(((A==4)))". This node
 * captures that relationship by bridging a single parent node to a single child
 * node as-is.
 */
public class AsIsNode extends Node 
{
	
	/**
	 * This creates a new AsIsNode
	 * @param parent the parent node
	 * @param cap the root of the expression
	 */
	public AsIsNode(Node parent, CapNode cap)
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
		getChildIndex(whichChildAmI);
		return parent.whereDoIGoOnFail(this);
	}

}
