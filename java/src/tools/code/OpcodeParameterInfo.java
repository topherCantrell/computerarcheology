package tools.code;

/**
 * Opcodes have fill-in parameter information. This class encapsulates the
 * info for a single opcode parameter (there may be several within a
 * single opcode).
 */
public class OpcodeParameterInfo 
{
	
	public String paramName; // The character representation of the parameter
	public int startInText;  // Where the parameter starts in the text representation
	public int endInText;    // Where the parameter ends in the text representation
	public String value;     // The parameter's value (might start out as an expression)

}
