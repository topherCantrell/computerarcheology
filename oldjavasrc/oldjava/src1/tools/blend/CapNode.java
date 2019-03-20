package tools.blend;

/**
 * Every blend expression tree has a root (cap) node. This is that node. Its constructor
 * reserves a unique name for the construct.
 */
public class CapNode extends Node
{
	
	// Uniqueness is maintained by a running construction count
	private static int blendConstructNumber = 1;
	
	// Uniqueness of nodes in the expression
	private int blendNumber = 1;
	
	// The base name of all nodes in the blend expression tree
	private String constructName;
	
	/**
	 * This constructs a CapNode and assigns it a unique construct name to
	 * be used by all nodes in the expression and construct.	 
	 * @param tag 
	 */
	public CapNode(String tag)
	{
		super(null,"__Blend_"+blendConstructNumber+"_cap");
		constructName = reserveName(tag);	
	}
	
	public static String reserveName(String tag) {
		String ret="__Blend_"+tag+"_"+blendConstructNumber;
		++blendConstructNumber;
		return ret;
	}
		
	/**
	 * Nodes created under this cap will have a unique name based on the cap name.
	 * This method returns the node name for a new node.
	 * @return the new unique node name
	 */
	public String getNewNodeName()
	{
		String ret = constructName+"_"+blendNumber;
		++blendNumber;
		return ret;
	}
		
	/**
	 * This method returns the unique name of the blend tree.
	 * @return unique name
	 */
	public String getConstructName() {
		return constructName;
	}
	
	@Override
	public String whereDoIGoOnPass(Node whichChildAmI) {
		// No child-check here on purpose
		return constructName+"_pass";
	}

	@Override
	public String whereDoIGoOnFail(Node whichChildAmI) {
		// No child-check here on purpose
		return constructName+"_fail";
	}

}
