package tools.web;

import tools.processor.OpcodeParamField;

/**
 * This class holds the information about a label substitution for
 * an opcode's parameter field. These labels are used in place of
 * pure numbers in disassembly generated for the web. The labels
 * may have mark-up tags that don't contribute to the printed length.
 * Thus there is a field for printed size for column calculations.
 */
public class OpcodeParamFieldReplaceInfo {
	
	public OpcodeParamField field;
	public String replacement;
	public int replacementPrintedSize;

}
