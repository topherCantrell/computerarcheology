package tools.blend.expression;

import tools.code.CodeLine;

/**
 * This exception class bubbles errors in an expression back through the levels
 * of the recursive algorithms.
 */
public class ExpressionException extends Exception
{
	
	/** The CodeLine where the error occurred */
	public CodeLine codeLine;
	
	/** The position within the CodeLine where the error occurred */
	public int position;

	public ExpressionException(String string, CodeLine codeLine, int position) {
		super(string);
		this.codeLine = codeLine;
		this.position = position;
	}

	private static final long serialVersionUID = 1L;

}
