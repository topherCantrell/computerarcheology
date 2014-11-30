package tools.processor;

/**
 * This class encapsulates the text and generated code for a single comparison blend entry
 * in the processor XML. For instance:
 * 
 *   A    <=     *
 * left   op   right
 * 
 *  Most comparison implementations have two forms. In one form the code flows through if
 *  the condition passes or branches away if the condition fails. The other form is the
 *  opposite. It flows through if the code fails and branches away if it passes. Different
 *  constructs (if, while, do) are coded optimally with different forms.
 * 
 */
public class ProcessorBlendEntry 
{
	
	public String left;   // * for any, blank for none
	public String op;     // * for any, blank for none
	public String right;  // * for any, blank for none
	
	public String branchPass; // if null use "branchBoth"
	public String branchFail; // if null use "branchBoth"
	
	public static String sub(String s, String target, String replace)
	{
		while(true) {
			int i = s.indexOf(target);
			if(i<0) return s;
			String a = s.substring(0,i)+replace+s.substring(i+target.length());
			s = a;
		}
	}

}
