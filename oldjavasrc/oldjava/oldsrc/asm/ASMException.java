package asm;

import code.CodeLine;

public class ASMException extends Exception {
		
	private static final long serialVersionUID = 1L;
	
	public CodeLine line;
	
	public ASMException(String message, CodeLine line) {
		super(message);
		this.line = line;
	}

}
