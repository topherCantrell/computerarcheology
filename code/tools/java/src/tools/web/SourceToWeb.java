package tools.web;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Reader;
import java.util.ArrayList;
import java.util.List;

import tools.code.CU;

public class SourceToWeb 
{
	
	List<String> lines;
		
	String LINE_NUMBER_STYLE = "$value$&nbsp;";
	String NUMBER_STYLE      = "<font style='color:#888800'>$value$</font>";
	String STRING_STYLE      = "<font style='color:#880000'>$value$</font>";
	String COMMENT_STYLE     = "<font style='color:#000088'>$value$</font>";	
	
	String TOKEN_WORD_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_";
	
	String [][] TOKEN_WORDS= {		
		{"<b>$value$</b>","CHIPVER","CLKMODE","_CLKMODE","CLKFREQ","_CLKFREQ","CLKSET","_XINFREQ","_STACK","_FREE","RCFAST","RCSLOW","XINPUT","XTAL1","XTAL2","XTAL3","PLL1X","PLL2X","PLL4X","PLL8X","PLL16X"},
		{"<b>$value$</b>","COGID","COGNEW","COGINIT","COGSTOP","REBOOT"},
		{"<b>$value$</b>","LOCKNEW","LOCKRET","LOCKCLR","LOCKSET","WAITCNT","WAITPEQ","WAITPNE","WAITVID"},
		{"<b>$value$</b>","BYTE","WORD","LONG","BYTEFILL","WORDFILL","LONGFILL","BYTEMOVE","WORDMOVE","LONGMOVE","LOOKUP","LOOKUPZ","LOOKDOWN","LOOKDOWNZ","STRSIZE","STRCOMP"},
		{"<b>$value$</b>","STRING","CONSTANT","FLOAT","ROUND","TRUNC","FILE"},
		{"<b>$value$</b>","DIRA","DIRB","INA","INB","OUTA","OUTB","CNT","CTRA","CTRB","FRQA","FRQB","PHSA","PHSB","VCFG","VSCL","PAR","SPR"},
		{"<b>$value$</b>","TRUE","FALSE","POSX","NEGX","PI"},
		{"<b>$value$</b>","RESULT"},
		{"<b>$value$</b>","CON","VAR","OBJ","PUB","PRI","DAT"},		
		{"<font style='color:#111111'>$value$</font>","ELSEIFNOT","IFNOT","ELSEIF","CASE","REPEAT","FROM","TO","STEP","UNTIL","WHILE","NEXT","QUIT","RETURN","ABORT","IF","ELSE"},
	};
	
	String [][] TOKEN_OPERATORS= {
		{"<font style='color:#00DD00'>$value$</font>",			
			"AND=",			
			"//=", "//=", "#>=", "<#=", "~>=", "<<=", ">>=", "<-=", "->=", "><=", "=<", "<>=",
			"OR=", "===", "=<=", "AND", "=>=", "**=",			
			"+=", "-=", "*=", "**", "=>", "/=", "#>", "<#",	"~>", "<<", ">>", "<-", "->","NOT", 
			"><", "&=", "|=", "^=",	"OR", "==",	"<>", "<=", ">=", ":=", "^^", "||", "~~", "|<", ">|", "@@",		 			
			"?","~","=", "+", "-", "*", "/", "&", "|", "^", ">", "<", "!", "@"}					
	};
	
	static class TokenInfo {
		enum TokenType {CHAR, NUMERIC, SYMBOL, OPERATOR, COMMENT, QUOTE, SPACE};
		int startOfNextToken;
		String token;
		TokenType type;		
	};
	
	public TokenInfo getStartOfNextToken(String s,int pos)
	{
		int start = pos;
		
		TokenInfo ret = new TokenInfo();
		
		if(pos>=s.length()) return null;
		
		char c = s.charAt(pos);
		
		// Sequences of whitespace
		if(c==' ' || c=='\t') {
			while(true) {
				++pos;
				if(pos==s.length()) {
					ret.startOfNextToken = s.length();
					ret.token = s.substring(start,ret.startOfNextToken);
					ret.type = TokenInfo.TokenType.SPACE;
					return ret;
				}
				if(s.charAt(pos)!=' ' && s.charAt(pos)!='\t') {
					ret.startOfNextToken = pos;
					ret.token = s.substring(start,ret.startOfNextToken);
					ret.type = TokenInfo.TokenType.SPACE;
					return ret;
				}
			}
		}
		
		// Comments go to the end of the line.
		if(c=='\'') {			
			ret.startOfNextToken = s.length();
			ret.token = s.substring(start,ret.startOfNextToken);
			ret.type = TokenInfo.TokenType.COMMENT;
			return ret;
		}
		
		// Strings go the the next quote (skip escaped).
		if(c=='"') {
			++pos;
			while(true) {
				if(pos==s.length()) {
					ret.startOfNextToken = s.length();
					ret.token = s.substring(start);
					ret.type = TokenInfo.TokenType.QUOTE;
					return ret;
				}
				c = s.charAt(pos++);
				if(c!='"') continue;
				if(pos<s.length() && s.charAt(pos)=='"') continue;
				ret.startOfNextToken = pos;
				ret.token = s.substring(start,ret.startOfNextToken);
				ret.type = TokenInfo.TokenType.QUOTE;
				return ret;
			}
		}
		
		// Numeric constant
		if( (c>='0' && c<='9') || c=='$' || c=='%') {
			++pos;
			while(true) {
				if(pos==s.length()) {
					ret.startOfNextToken = s.length();
					ret.token = s.substring(start,ret.startOfNextToken);
					ret.type = TokenInfo.TokenType.NUMERIC;
					return ret;
				}
				c = s.charAt(pos++);
				if( (c>='0' && c<='9') || (c>='a' && c<='z') || (c>='A' && c<='Z') || c=='_') continue;
				ret.startOfNextToken = pos-1;
				ret.token = s.substring(start,ret.startOfNextToken);
				ret.type = TokenInfo.TokenType.NUMERIC;
				return ret;
			}
		}
		
		// Symbols go till a non-symbol character.
		if( (c>='a' && c<='z') || (c>='A' && c<='Z') || (c=='_') ) {
			while(true) {
				if(pos==s.length()) {
					ret.startOfNextToken = pos;
					ret.token = s.substring(start,ret.startOfNextToken);
					ret.type = TokenInfo.TokenType.SYMBOL;
					return ret;
				}
				c = s.charAt(pos++);
				if(TOKEN_WORD_CHARS.indexOf(c)<0) {
					ret.startOfNextToken = pos-1;
					ret.token = s.substring(start,ret.startOfNextToken);
					ret.type = TokenInfo.TokenType.SYMBOL;
					return ret;
				}
			}
		}
		
		// Might be an operator. Find the best match.
		for(int x=1;x<TOKEN_OPERATORS.length;++x) {
			if(s.indexOf(TOKEN_OPERATORS[0][x])==pos) {
				ret.startOfNextToken = pos+TOKEN_OPERATORS[0][x].length();
				ret.token = s.substring(start,ret.startOfNextToken);
				ret.type = TokenInfo.TokenType.OPERATOR;
				return ret;				
			}
		}
		
		// Nothing. Token is a single character.
		
		ret.startOfNextToken = pos+1;
		ret.token = s.substring(start,ret.startOfNextToken);
		ret.type = TokenInfo.TokenType.CHAR;
		return ret;	
		
	}
	
	public static void main(String [] args) throws Exception
	{
		
		// TODO look at first two bytes for UTF-16
		// TODO load styling
		
		args = new String[1];		
		args[0] = "c:\\projects\\SIStick\\Code\\CPU_8080.spin";
		
		SourceToWeb stw = new SourceToWeb(args[0]);
		
		
		stw.processTokens();
		
		
		stw.addLineNumbers();
		
		
		stw.printCode();		
		
	}
	
	public String processToken(TokenInfo ti) {
		
		// {CHAR, SPACE,   NUMERIC, COMMENT, QUOTE,   SYMBOL, OPERATOR}
		switch(ti.type) {
		
		case NUMERIC:
			return CU.replaceAll(NUMBER_STYLE, "$value$", ti.token);
			
		case COMMENT:
			return CU.replaceAll(COMMENT_STYLE, "$value$", ti.token);
			
		case QUOTE:
			return CU.replaceAll(STRING_STYLE, "$value$", ti.token);
			
		case CHAR:
			break;
		case OPERATOR:
			break;
		case SPACE:
			break;
		case SYMBOL:
			break;
		default:
			break;
				
					
		}
		
		return ti.token;
	}
	
	public void processTokens() {
		
		for(int x=0;x<lines.size();++x) {
			
			String s = lines.get(x);
			
			StringBuffer a = new StringBuffer();
			int pos=0;
			
			while(pos!=s.length()) {				
				TokenInfo ti = getStartOfNextToken(s,pos);				
				a.append(processToken(ti));
				pos = ti.startOfNextToken;
			}
			
			lines.set(x, a.toString());
		}
	}
	
	
	public SourceToWeb(String filename) throws IOException
	{
		Reader fr = new InputStreamReader(new FileInputStream(filename),"UTF-16");
		BufferedReader br = new BufferedReader(fr);
		
		lines = new ArrayList<String>();
		
		while(true) {
			String g = br.readLine();
			if(g==null) break;
			lines.add(entize(g));			
		}
		
		br.close();		
	}
	
	public static String entize(String s) {
		
		s = CU.replaceAll(s, "&", "&amp;");
		s = CU.replaceAll(s, "<", "&lt;");
		s = CU.replaceAll(s, ">", "&gt;");
		
		return s;
	}
	
	public void startColorBlock(int startLine, String color) {
		String a = lines.get(startLine);
		a = "<div style='background-color:"+color+"'>"+a;
		lines.set(startLine,a);
	}
	
	public void backgroundColor(int startLine, int stopLine, String color) {
		String a = lines.get(startLine);
		a = "<div style='background-color:"+color+"'>"+a;
		lines.set(startLine,a);
		if(stopLine==lines.size()) {
			lines.add("");
		}
		a = lines.get(stopLine+1);
		a = "</div>"+a;
		lines.set(stopLine, a);
	}
	
	public void addLineNumbers() {
		
		int len = new String(""+lines.size()).length();
		
		for(int x=0;x<lines.size();++x) {
			String a = lines.get(x);
			String n = ""+(x+1);
			int pad = len-n.length();
			for(int y=0;y<pad;++y) {
				n = "&nbsp;" + n;
			}
			n = CU.replaceAll(LINE_NUMBER_STYLE, "$value$", n);			
			lines.set(x, n+a);
		}
		
	}
	
	public void printCode() {
		
		
		System.out.println("<code><pre>");
		for(String s : lines) {
			System.out.println(s);
		}
		System.out.println("</pre></code>");
		
	}

}
