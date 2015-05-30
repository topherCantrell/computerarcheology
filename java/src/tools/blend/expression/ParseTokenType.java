package tools.blend.expression;

/** The types of expression tokens.
 */
public enum ParseTokenType {
	OPEN,     // Open parenthesis "("
	CLOSE,    // Close parenthesis ")"
	LOGIC,    // A logic operator "&&" or "||"
	NOT,      // The unary NOT operator "!" only allowed before an open parenthesis
	COMPARE,  // A comparison operator like ">" or "<="
	SYMBOL,   // A number of other multi-character symbol
	SUBLIST   // An insertion point for a sublist of other parse tokens
}
