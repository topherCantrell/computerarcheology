package tools.blend;

import java.util.ArrayList;
import java.util.List;

/**
 * This abstract class holds the basic functionality of all blend expression nodes.
 */
public abstract class Node {
	
	String name;
	Node parent = null;
	List<Node> children = new ArrayList<Node>();
	
	/**
	 * This creates a new blend node.
	 * @param parent the parent of this node
	 * @param name the unique name of the node
	 */
	public Node(Node parent, String name)
	{
		this.parent = parent;
		this.name = name;
	}
	
	/**
	 * This returns the first compare node.
	 * @return the starting compare node
	 */
	public CompareNode getStartingCompareNode()
	{
		Node ret = this;
		while(true) {		
			if(ret instanceof CompareNode) return (CompareNode)ret;	
			ret = ret.children.get(0);					
		}
	}
	
	/**
	 * This method adds a child to the node's child list
	 * @param child the child to add
	 */
	public void addChild(Node child) {
		children.add(child);
	}

	
	/**
	 * This method returns this node's unique name.
	 * @return the node name
	 */
	public String getName() {
		return name;
	}
	
	// Just a sanity check to make sure the child is really a listed child
	protected int getChildIndex(Node whichChildAmI) {
		int ret = children.indexOf(whichChildAmI);
		if(ret<0) throw new RuntimeException("Node thinks it is my child");
		return ret;
	}	
	
	/**
	 * When a child node finishes its processing it can either have passed or
	 * failed and needs a destination to jump to (another compare-node or the
	 * pass/fail blocks). This method returns the next place.
	 * @param whichChildAmI which child I am (AND and OR have multiple children)
	 * @return the name of the next jump destination
	 */
	public abstract String whereDoIGoOnPass(Node whichChildAmI);
	public abstract String whereDoIGoOnFail(Node whichChildAmI);

}
