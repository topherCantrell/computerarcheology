package tools.assembler;

import java.util.Map;

import tools.code.AddressSpec;
import tools.code.CU;
import tools.code.CodeLine;

public class Expression {
	
	
	public static Integer decodeExpression(CodeLine co, String expression, 
			Map<String,String> defines, Map<String,AddressSpec> addresses) 
	{
		
		// TODO just a couple of simple cases for now. A real expression runner later.
		
		int x = expression.indexOf("-");
		if(x>0) {
			Integer a = decodeTerm(co,expression.substring(0,x),defines,addresses);
			if(a==null) return null;
			Integer b = decodeTerm(co,expression.substring(x+1),defines,addresses);
			if(b==null) return null;
			return a-b;
		}
		
		x = expression.indexOf("+");
		if(x>0) {
			Integer a = decodeTerm(co,expression.substring(0,x),defines,addresses);
			if(a==null) return null;
			Integer b = decodeTerm(co,expression.substring(x+1),defines,addresses);
			if(b==null) return null;
			return a+b;
		}
		
		return decodeTerm(co,expression,defines,addresses);		
		
	}
		
	
	private static Integer decodeTerm(CodeLine co, String expression, 
			Map<String,String> defines, Map<String,AddressSpec> addresses)
	{
		Integer i = null;
		AddressSpec as = addresses.get(expression);
		if(as!=null) {
			i = as.address;
		}
		if(i==null) {
			String s = defines.get(expression);
			if(s==null) s=expression;
			try {				
				i = CU.parseIntValue(s);
			} catch (Exception e) {
				co.setError("Invalid numeric value '"+s+"'");
				return null;
			}
		}
		return i;
	}

}
