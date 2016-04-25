package digs.spaceinvaders;

import java.util.ArrayList;
import java.util.List;

public class CPU_SPIN8080 {

	int regA, regB, regC, regD, regE, regH, regL, regPC, regSP, regF;

	static final int INTERRUPT_IRQ = 0;
	static final int INTERRUPT_NMI = 1;
	
	boolean IRQ = false; // interrupt request
	boolean NMI = false; // Non-maskable interrupt
	
	boolean interruptEnabled;

	private AddressBusDevice ports;

	private AddressBusDevice system;

	public CPU_SPIN8080(AddressBusDevice ports, AddressBusDevice system) {
		this.ports = ports;
		this.system = system;
	}
	
	public void interruptNMI() {
		NMI = true;
	}

	public void interruptIRQ() {
		IRQ = true;
	}

	String [] decodeInfoFlags = {
			"--------",
			"---H--0C",
			"sz-h-v*-",
			"---x--0x",
			"---1--1-",
			"xxxxxxxx",
			"---0--01",
			"---0--0x",
			"sz-u-v1b",
			"sz-1-p00",
			"sz-0-p00",
			"sz-h-v0c",			
	};

	String [] decodeInfo = {
			"00|FF|00|00|--------|00000000|11111111|00_000_000||NOP",
			"01|CF|09|00|---H--0C|00001001|11001111|00_pp_1_001||ADD HL,pp",
			"00|CF|01|02|--------|00000001|11001111|00_pp_0_001|wlwm|LD pp,w",			
			"00|FF|32|02|--------|00110010|11111111|00_11_0_010|wlwm|LD (w),A",
			"00|FF|22|02|--------|00100010|11111111|00_10_0_010|wlwm|LD (w),HL",
			"00|CF|02|00|--------|00000010|11001111|00_qq_0_010||LD (qq),A",				
			"00|FF|3A|02|--------|00111010|11111111|00_11_1_010|wlwm|LD A,(w)",			
			"00|FF|2A|02|--------|00101010|11111111|00_11_1_010|wlwm|LD HL,(w)",
			"00|CF|0A|00|--------|00001010|11001111|00_qq_1_010||LD A,(qq)",			
			"00|C7|03|00|--------|00000011|11000111|00_pp_i_011||INC/DEC pp",
			"02|C7|04|00|sz-h-v*-|00000100|11000111|00_rrr_100||INC r",
			"02|C7|05|00|sz-h-v*-|00000101|11000111|00_rrr_101||DEC r",
			"00|C7|06|01|--------|00000110|11000111|00_rrr_110|bb|LD r,b",
			"03|FF|3F|00|---x--0x|00111111|11111111|00_111_111||CCF",
			"04|FF|2F|00|---1--1-|00101111|11111111|00_101_111||CPL",
			"05|FF|27|00|xxxxxxxx|00100111|11111111|00_100_111||DAA",
			"06|FF|37|00|---0--01|00110111|11111111|00_110_111||SCF",
			"07|E7|07|00|---0--0x|00000111|11100111|00_0kr_111||rotate",
			"05|FF|76|00|xxxxxxxx|01110110|11111111|01_110_110||HALT",
			"00|C0|40|00|--------|01000000|11000000|01_drr_srr||LD dr,sr",			
			"00|F8|90|00|sz-u-v1b|10010000|11111000|10_010_rrr||SUB r",			
			"08|F8|98|00|sz-u-v1b|10011000|11111000|10_011_rrr||SBC r",
			"08|F8|B8|00|sz-u-v1b|10111000|11111000|10_111_rrr||CP r",
			"09|F8|A0|00|sz-1-p00|10100000|11111000|10_100_rrr||AND r",
			"0A|F8|A8|00|sz-0-p00|10101000|11111000|10_101_rrr||XOR r",
			"0A|F8|B0|00|sz-0-p00|10110000|11111000|10_110_rrr||OR r",
			"0B|F8|88|00|sz-h-v0c|10001000|11111000|10_001_rrr||ADC A,r",
			"0B|F8|80|00|sz-h-v0c|10000000|11111000|10_000_rrr||ADD A,r",
			"08|FF|DE|01|sz-u-v1b|11011110|11111111|11_011_110|bb|SBC A,b",
			"08|FF|D6|01|sz-u-v1b|11010110|11111111|11_010_110|bb|SUB A,b",
			"08|FF|FE|01|sz-u-v1b|11111110|11111111|11_111_110|bb|CP b",
			"00|FF|F9|00|--------|11111001|11111111|11_111_001||LD SP,HL",
			"00|FF|E9|00|--------|11101001|11111111|11_101_001||JP (HL)",
			"00|FF|C9|00|--------|11001001|11111111|11_001_001||RET",
			"05|FF|F1|00|xxxxxxxx|11110001|11111111|11_110_001||POP AF",
			"00|FF|C1|00|--------|11000001|11111111|11_000_001||POP BC",
			"00|FF|D1|00|--------|11010001|11111111|11_010_001||POP DE",
			"00|FF|E1|00|--------|11100001|11111111|11_100_001||POP HL",
			"05|FF|F3|00|xxxxxxxx|11110011|11111111|11_110_011||DI",
			"05|FF|FB|00|xxxxxxxx|11111011|11111111|11_111_011||EI",
			"00|FF|E3|00|--------|11100011|11111111|11_100_011||EX (SP),HL",
			"00|FF|EB|00|--------|11101011|11111111|11_101_011||EX DE,HL",
			"00|FF|DB|01|--------|11011011|11111111|11_011_011|oo|IN A,(o)",
			"00|FF|C3|02|--------|11000011|11111111|11_000_011|mlmm|JP m",
			"00|FF|D3|01|--------|11010011|11111111|11_010_011|oo|OUT (o),A",
			"00|FF|F5|00|--------|11110101|11111111|11_110_101||PUSH AF",
			"00|FF|C5|00|--------|11000101|11111111|11_000_101||PUSH BC",
			"00|FF|D5|00|--------|11010101|11111111|11_010_101||PUSH DE",
			"00|FF|E5|00|--------|11100101|11111111|11_100_101||PUSH HL",
			"00|FF|CD|02|--------|11001101|11111111|11_001_101|mlmm|CALL m",
			"0B|FF|CE|01|sz-h-v0c|11001110|11111111|11_001_110|bb|ADC A,b",
			"0B|FF|C6|01|sz-h-v0c|11000110|11111111|11_000_110|bb|ADD A,b",
			"09|FF|E6|01|sz-1-p00|11100110|11111111|11_100_110|bb|AND b",
			"0A|FF|EE|01|sz-0-p00|11101110|11111111|11_101_110|bb|XOR b",
			"0A|FF|F6|01|sz-0-p00|11110110|11111111|11_110_110|bb|OR b",
			"00|C7|C0|00|--------|11000000|11000111|11_cc_v_000||RET cc",
			"00|C7|C2|02|--------|11000010|11000111|11_ccv_010|mlmm|JP C,m",
			"00|C7|C4|02|--------|11000100|11000111|11_ccv_100|mlmm|CALL cc,m",
			"00|C7|C7|00|--------|11000111|11000111|11_rst_111||RST rst",	
	};

	private List<Integer> ops = new ArrayList<Integer>();
	
	public final void exec(int num_cycles) {
		
		if(NMI) {
			NMI = false;			
			push(regPC);
			regPC = 0x0010;			
		} else if(interruptEnabled && IRQ) {
			IRQ = false;
			interruptEnabled = false;
			push(regPC);
			regPC = 0x0008;
		}
		
		int instruction = system.getByte(regPC);
		++regPC;

		if(!ops.contains(instruction)) ops.add(instruction);
		
		String di = null;
		for(int x=0;x<decodeInfo.length;++x) {
			int mask = Integer.parseInt(decodeInfo[x].substring(3,5),16);
			int pat = Integer.parseInt(decodeInfo[x].substring(6,8),16);
			if( (instruction&mask)==pat ) {
				di = decodeInfo[x];
				break;
			}
		}
		
		//if(di==null) {
		//	System.out.println("UNKNOWN AT "+CU.fourDigitHex(regPC-1));
		//}

		int flags = Integer.parseInt(di.substring(0,2),16);
		int numbytes = Integer.parseInt(di.substring(9,11),16);
		String decSwitch = di.substring(3,5)+di.substring(6,8);

		// Read any extra information from text
		int extra = 0;
		if(numbytes==1) extra = system.getByte(regPC);
		else if(numbytes==2) extra=system.getByte(regPC)+(system.getByte(regPC+1)<<8);
		regPC = regPC + numbytes;

		if(decSwitch.equals("FF00")) {
			doOpFF00(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFC3")) {
			doOpFFC3(instruction,di,extra,flags);
		} else if(decSwitch.equals("CF09")) {
			doOpCF09(instruction,di,extra,flags);
		} else if(decSwitch.equals("CF01")) {
			doOpCF01(instruction,di,extra,flags);
		} else if(decSwitch.equals("CF02")) {
			doOpCF02(instruction,di,extra,flags);
		} else if(decSwitch.equals("CF0A")) {
			doOpCF0A(instruction,di,extra,flags);
		} else if(decSwitch.equals("C703")) {
			doOpC703(instruction,di,extra,flags);
		} else if(decSwitch.equals("C704")) {
			doOpC704(instruction,di,extra,flags);
		} else if(decSwitch.equals("C705")) {
			doOpC705(instruction,di,extra,flags);
		} else if(decSwitch.equals("C706")) {
			doOpC706(instruction,di,extra,flags);
		} else if(decSwitch.equals("FF3F")) {
			doOpFF3F(instruction,di,extra,flags);
		} else if(decSwitch.equals("FF2F")) {
			doOpFF2F(instruction,di,extra,flags);
		} else if(decSwitch.equals("FF27")) {
			doOpFF27(instruction,di,extra,flags);
		} else if(decSwitch.equals("FF37")) {
			doOpFF37(instruction,di,extra,flags);
		} else if(decSwitch.equals("E707")) {
			doOpE707(instruction,di,extra,flags);
		} else if(decSwitch.equals("FF76")) {
			doOpFF76(instruction,di,extra,flags);
		} else if(decSwitch.equals("C040")) {
			doOpC040(instruction,di,extra,flags);
		} else if(decSwitch.equals("F898")) {
			doOpF898(instruction,di,extra,flags);
		} else if(decSwitch.equals("F8B8")) {
			doOpF8B8(instruction,di,extra,flags);
		} else if(decSwitch.equals("F8A0")) {
			doOpF8A0(instruction,di,extra,flags);
		} else if(decSwitch.equals("F8A8")) {
			doOpF8A8(instruction,di,extra,flags);
		} else if(decSwitch.equals("F8B0")) {
			doOpF8B0(instruction,di,extra,flags);
		} else if(decSwitch.equals("F888")) {
			doOpF888(instruction,di,extra,flags);
		} else if(decSwitch.equals("F880")) {
			doOpF880(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFDE")) {
			doOpFFDE(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFD6")) {
			doOpFFD6(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFFE")) {
			doOpFFFE(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFF9")) {
			doOpFFF9(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFE9")) {
			doOpFFE9(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFC9")) {
			doOpFFC9(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFF1")) {
			doOpFFF1(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFC1")) {
			doOpFFC1(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFD1")) {
			doOpFFD1(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFE1")) {
			doOpFFE1(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFF3")) {
			doOpFFF3(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFFB")) {
			doOpFFFB(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFE3")) {
			doOpFFE3(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFEB")) {
			doOpFFEB(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFDB")) {
			doOpFFDB(instruction,di,extra,flags);
		}  else if(decSwitch.equals("FFD3")) {
			doOpFFD3(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFF5")) {
			doOpFFF5(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFC5")) {
			doOpFFC5(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFD5")) {
			doOpFFD5(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFE5")) {
			doOpFFE5(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFCD")) {
			doOpFFCD(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFCE")) {
			doOpFFCE(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFC6")) {
			doOpFFC6(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFE6")) {
			doOpFFE6(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFEE")) {
			doOpFFEE(instruction,di,extra,flags);
		} else if(decSwitch.equals("FFF6")) {
			doOpFFF6(instruction,di,extra,flags);
		} else if(decSwitch.equals("C7C0")) {
			doOpC7C0(instruction,di,extra,flags);
		} else if(decSwitch.equals("C7C2")) {
			doOpC7C2(instruction,di,extra,flags);
		} else if(decSwitch.equals("C7C4")) {
			doOpC7C4(instruction,di,extra,flags);
		} else if(decSwitch.equals("C7C7")) {
			doOpC7C7(instruction,di,extra,flags);
		} else if(decSwitch.equals("FF32")) {
			doOpFF32(instruction,di,extra,flags);
		} else if(decSwitch.equals("FF3A")) {
			doOpFF3A(instruction,di,extra,flags);
		} else if(decSwitch.equals("FF2A")) {
			doOpFF2A(instruction,di,extra,flags);
		} else if(decSwitch.equals("FF22")) {
			doOpFF22(instruction,di,extra,flags);
		} else if(decSwitch.equals("F890")) {
			doOpF890(instruction,di,extra,flags);
		}

		else {		
			System.out.println(decSwitch+":"+di);
			throw new RuntimeException("UNMAPPED "+decSwitch);
		}		

	}
	
	
	int getQQ(int qq) {
		//00 (BC)
		//01 (DE)
		//10 (HL)				
		int extra=0;
		switch(qq) {
		case 0:
			extra = (regB<<8) | regC;
			break;
		case 1:
			extra = (regD<<8) | regE;
			break;
		case 2:
			extra = (regH<<8) | regL;
			break;
		default:
			throw new RuntimeException("OOPS");
		}
		return system.getByte(extra);
		
	}
	
	void setQQ(int qq, int value) {
		//00 (BC)
		//01 (DE)
		//10 (HL)				
		int extra=0;
		switch(qq) {
		case 0:
			extra = (regB<<8) | regC;
			break;
		case 1:
			extra = (regD<<8) | regE;
			break;
		case 2:
			extra = (regH<<8) | regL;
			break;
		default:
			throw new RuntimeException("OOPS");
		}
		system.setByte(extra,value);		
	}
	
	
	
	int getPP(int pp) {
		switch(pp) {
		case 0:
			return (regB<<8) | regC;			
		case 1:
			return (regD<<8) | regE;
		case 2:
			return (regH<<8) | regL;
		case 3:
			return regSP;
		}
		throw new RuntimeException("OOPS");
	}	
	
	void setPP(int pp, int extra) {
		switch(pp) {
		case 0:
			regB=(extra>>8)&255;
			regC=extra&255;
			break;
		case 1:
			regD=(extra>>8)&255;
			regE=extra&255;
			break;
		case 2:
			regH=(extra>>8)&255;
			regL=extra&255;
			break;
		case 3:
			regSP=extra;
			break;
		}
	}
	
	int getRRR(int rrr) {
		switch(rrr) {
		case 0:
			return regB;
		case 1:
			return regC;
		case 2:
			return regD;
		case 3:
			return regE;
		case 4:
			return regH;
		case 5:
			return regL;
		case 6:
			return system.getByte((regH<<8) | regL);			
		case 7:
			return regA;
		}
		throw new RuntimeException("OOPS");
	}
	
	void setRRR(int rrr, int extra) {
		switch(rrr) {
		case 0:
			regB = extra;
			break;
		case 1:
			regC = extra;
			break;
		case 2:
			regD = extra;
			break;
		case 3:
			regE = extra;
			break;
		case 4:
			regH = extra;
			break;
		case 5:
			regL = extra;
			break;
		case 6:
			system.setByte((regH<<8)|regL, extra);
			break;
		case 7:
			regA = extra;
			break;
		}
	}
	
	void setSubVFlag(int before, int after) {
		// TODO
	}
	
	void setSubHFlag(int before, int after) {
		// If the lower nibble was greater after then there must have been a borrow
		if( (after&0x0f) > (before&0x0f)) {
			regF = regF | 0x10;
		} else {
			regF = regF & (0xFF-0x10);
		}
	}
	
	void setAddHFlag(int before, int after) {
		if( (after&0x0f) < (before&0x0f)) {
			regF = regF | 0x10;
		} else {
			regF = regF & (0xFF-0x10);
		}
	}
	
	void setAddVFlag(int before, int after) {
		// TODO
	}
	
	void setAddCFlag(int after) {
		if(after>255) {
			regF = regF | 1;
		} else {
			regF = regF & (0xFF-1);
		}
	}
	
	
	void setSubBFlag(int after) {
		if(after<0) {
			regF = regF | 1;
		} else {
			regF = regF & (0xFF-1);
		}
	}
	
	void setAddH16Flag(int before, int after) {
		if( (after&0xfff) < (before&0xfff)) {
			regF = regF | 0x10;
		} else {
			regF = regF & (0xFF-0x10);
		}
	}
	
	void setAddC16Flag(int after) {
		if(after>65535) {
			regF = regF | 1;
		} else {
			regF = regF & (0xFF-1);
		}
	}
	
	void setSFlag(int after) {
		if(after<0) after=256+after;
		if( (after&0x80)!=0 ) {
			regF = regF | 0x80;
		} else {
			regF = regF & (0xFF-0x80);
		}
	}
	
	void setZFlag(int after) {
		if(after==0) {
			regF = regF | 0x40;
		} else {
			regF = regF & (0xFF-0x40);
		}
	}
	
	void setPFlag(int after) {
		String s = Integer.toString(after,2);
		int cnt = 0;
		for(int x=0;x<s.length();++x) {
			if(s.charAt(x)=='1') ++cnt;
		}
		if( (cnt&1)==1 ) {
			regF = regF | 4;
		} else {
			regF = regF & 0xFF-4;
		}
	}
	
	void push(int value) {
		// <routine name="push" code="SP=SP-1;[SP]=$1$.up;SP=SP-1;[SP]=$1$.low"/>
		--regSP;
		system.setByte(regSP, value>>8);
		--regSP;
		system.setByte(regSP, value&255);
	}
	
	int pop() {
		int ret = system.getByte(regSP) | (system.getByte(regSP+1)<<8);
		regSP+=2;
		return ret;
	}
	
	
		
		
	
		

	void doOpFF00(int instruction, String di, int extra,int flags) {
		//00|FF|00|00|--------|00000000|11111111|00_000_000||NOP
		// Do nothing
	}

	void doOpFFC3(int instruction, String di, int extra,int flags) {
		//00|FF|C3|02|--------|11000011|11111111|11_000_011|mlmm|JP m
		regPC = extra;
	}
	
	void doOpCF01(int instruction, String di, int extra,int flags) {
		//00|CF|01|02|--------|00000001|11001111|00_pp_0_001|wlwm|LD pp,w
		int pp = (instruction>>4)&3;
		setPP(pp,extra);		
	}
	
	void doOpC706(int instruction, String di, int extra,int flags) {
		//00|C7|06|01|--------|00000110|11000111|00_rrr_110|bb|LD r,b
		int rrr = (instruction>>3)&7;
		setRRR(rrr,extra);
	}
	
	void doOpFFCD(int instruction, String di, int extra,int flags) {
		// 00|FF|CD|02|--------|11001101|11111111|11_001_101|mlmm|CALL m		
		push(regPC);
		regPC = extra;		
	}
	
	void doOpFFC9(int instruction, String di, int extra,int flags) {
		//00|FF|C9|00|--------|11001001|11111111|11_001_001||RET
		regPC = pop();
	}
	
	void doOpCF0A(int instruction, String di, int extra,int flags) {
		//00|CF|0A|00|--------|00001010|11001111|00_qq_1_010||LD A,(qq)
		int qq = (instruction>>4)&3;
		regA = getQQ(qq);				
	}
	
	void doOpCF02(int instruction, String di, int extra,int flags) {
		//00|CF|02|00|--------|00000010|11001111|00_qq_0_010||LD (qq),A
		int qq = (instruction>>4)&3;
		setQQ(qq,regA);
	}
	
	void doOpC040(int instruction, String di, int extra,int flags) {
		//00|C0|40|00|--------|01000000|11000000|01_drr_srr||LD dr,sr
		int dr = (instruction>>3)&7;
		int sr = (instruction)&7;
		setRRR(dr,getRRR(sr));		
	}
	
	void doOpC703(int instruction, String di, int extra,int flags) {
		//00|C7|03|00|--------|00000011|11000111|00_pp_i_011||INC/DEC pp
		int pp = (instruction>>4)&3;
		extra = getPP(pp);
		if( (instruction&8)==0 ) {
			++extra;
		} else {
			--extra;
		}
		setPP(pp,extra);		
	}
	
	void doOpFFFE(int instruction, String di, int extra,int flags) {
		//08|FF|FE|01|sz-u-v1b|11111110|11111111|11_111_110|bb|CP b
		int nv = regA - extra;
		setSubHFlag(regA,nv);
		setSubVFlag(regA,nv);
		setSFlag(nv);
		setZFlag(nv);		
		regF = regF | 2; // subtract
		setSubBFlag(nv);	
		// No result
	}
	
	void doOpFFDE(int instruction, String di, int extra,int flags) {
		//08|FF|DE|01|sz-u-v1b|11011110|11111111|11_011_110|bb|SBC A,b
		int borrow = regF&1;
		int nv = regA - extra - borrow;
		setSubHFlag(regA,nv);
		setSubVFlag(regA,nv);
		setSFlag(nv);
		setZFlag(nv);		
		regF = regF | 2; // subtract
		setSubBFlag(nv);
		if(nv<0) nv=nv+256;
		regA = nv;
	}
	
	void doOpFFD6(int instruction, String di, int extra,int flags) {
		//08|FF|D6|01|sz-u-v1b|11010110|11111111|11_010_110|bb|SUB A,b
		int nv = regA - extra;
		setSubHFlag(regA,nv);
		setSubVFlag(regA,nv);
		setSFlag(nv);
		setZFlag(nv);		
		regF = regF | 2; // subtract
		setSubBFlag(nv);
		if(nv<0) nv=nv+256;
		regA = nv;
	}
	
	void doOpF890(int instruction, String di, int extra,int flags) {
		//08|FF|D6|01|sz-u-v1b|11010110|11111111|11_010_110|bb|SUB A,b
		int rrr = instruction&7;
		extra = getRRR(rrr);
		int nv = regA - extra;
		setSubHFlag(regA,nv);
		setSubVFlag(regA,nv);
		setSFlag(nv);
		setZFlag(nv);		
		regF = regF | 2; // subtract
		setSubBFlag(nv);
		if(nv<0) nv=nv+256;
		regA = nv;
	}
	
	void doOpF8B8(int instruction, String di, int extra,int flags) {
		//08|F8|B8|00|sz-u-v1b|10111000|11111000|10_111_rrr||CP r
		int rrr = (instruction&7);
		int nv = regA - getRRR(rrr);
		setSubHFlag(regA,nv);
		setSubVFlag(regA,nv);
		setSFlag(nv);
		setZFlag(nv);		
		regF = regF | 2; // subtract
		setSubBFlag(nv);
	}
			
	void doOpC705(int instruction, String di, int extra,int flags) {
		//02|C7|05|00|sz-h-v*-|00000101|11000111|00_rrr_101||DEC r
		int rrr = (instruction>>3)&7;
		extra = getRRR(rrr);
		int nv = extra-1;
		setSubHFlag(extra,nv);
		setSubVFlag(extra,nv);
		setSFlag(nv);
		setZFlag(nv);		
		regF = regF | 2; // subtract
		if(nv<0) nv=256+nv;		
		setRRR(rrr,nv);		
	}
	
	void doOpC7C2(int instruction, String di, int extra,int flags) {
		//00|C7|C2|02|--------|11000010|11000111|11_ccv_010|mlmm|JP C,m
		
		int condition = (instruction>>4)&3;
		int v = (instruction>>3)&1;
		
		int flag = 0;
		switch(condition) {
		case 0:
			flag = regF>>6; // Z
			break;
		case 1:
			flag = regF; // C
			break;
		case 2:
			throw new RuntimeException("NOT IMPLEMENTED");
			//flag = regF>>2; // V
			//break;
		case 3:
			flag = regF>>7; // S
			break;
		}
		flag = flag & 1;
		if(v==0) {
			flag = (~flag)&1;
		}
		
		if(flag==1) {
			regPC = extra;
		}
		
	}	
	
	void doOpC7C4(int instruction, String di, int extra,int flags) {
		//00|C7|C4|02|--------|11000100|11000111|11_ccv_100|mlmm|CALL cc,m
		int condition = (instruction>>4)&3;
		int v = (instruction>>3)&1;
		
		int flag = 0;
		switch(condition) {
		case 0:
			flag = regF>>6; // Z
			break;
		case 1:
			flag = regF; // C
			break;
		case 2:
			throw new RuntimeException("NOT IMPLEMENTED");
			//flag = regF>>2; // V
			//break;
		case 3:
			flag = regF>>7; // S
			break;
		}
		flag = flag & 1;
		if(v==0) {
			flag = (~flag)&1;
		}
		
		if(flag==1) {
			push(regPC);
			regPC = extra;
		}
	}
	
	void doOpFFD5(int instruction, String di, int extra,int flags) {
		//00|FF|D5|00|--------|11010101|11111111|11_010_101||PUSH DE
		push( (regD<<8) | regE);
	}
	
	void doOpFFE5(int instruction, String di, int extra,int flags) {
		//00|FF|E5|00|--------|11100101|11111111|11_100_101||PUSH HL
		push( (regH<<8) | regL);
	}
	
	void doOpFFC5(int instruction, String di, int extra,int flags) {
		// 00|FF|C5|00|--------|11000101|11111111|11_000_101||PUSH BC
		push( (regB<<8) | regC);
	}
	
	void doOpFFF5(int instruction, String di, int extra,int flags) {
		//00|FF|F5|00|--------|11110101|11111111|11_110_101||PUSH AF
		push( (regA<<8) | regF);
	}	
	
	void doOpCF09(int instruction, String di, int extra,int flags) {
		//01|CF|09|00|---H--0C|00001001|11001111|00_pp_1_001||ADD HL,pp
		int pp = (instruction>>4)&3;
		int hl = (regH<<8) | regL;
		extra = hl + getPP(pp);
		setAddH16Flag(hl,extra);
		setAddC16Flag(extra);
		regF = regF & (0xFF-2);
		
		regH = extra>>8;
		regL = extra&255;
	}
	
	void doOpFFEB(int instruction, String di, int extra,int flags) {
		//00|FF|EB|00|--------|11101011|11111111|11_101_011||EX DE,HL
		int d = regD;
		int e = regE;
		int h = regH;
		int l = regL;
		regH = d;
		regL = e;
		regD = h;
		regE = l;
	}
	
	void doOpFFE1(int instruction, String di, int extra,int flags) {
		//00|FF|E1|00|--------|11100001|11111111|11_100_001||POP HL
		extra = pop();
		regH = extra>>8;
		regL = extra&255;
	}
	
	void doOpFFD1(int instruction, String di, int extra,int flags) {
		//00|FF|D1|00|--------|11010001|11111111|11_010_001||POP DE
		extra = pop();
		regD = extra>>8;
		regE = extra&255;
	}
	
	void doOpFFC1(int instruction, String di, int extra,int flags) {
		//00|FF|C1|00|--------|11000001|11111111|11_000_001||POP BC
		extra = pop();
		regB = extra>>8;
		regC = extra&255;
	}
	
	void doOpFFF1(int instruction, String di, int extra,int flags) {
		//05|FF|F1|00|xxxxxxxx|11110001|11111111|11_110_001||POP AF
		extra = pop();
		regA = extra>>8;
		regF = extra&255;
	}
	
	void doOpFFDB(int instruction, String di, int extra,int flags) {
		//00|FF|DB|01|--------|11011011|11111111|11_011_011|oo|IN A,(o)
		regA = ports.getByte(extra);
	}
	
	void doOpFFD3(int instruction, String di, int extra,int flags) {
		//00|FF|D3|01|--------|11010011|11111111|11_010_011|oo|OUT (o),A
		ports.setByte(extra, regA);		
	}
	
	void doOpE707(int instruction, String di, int xxx,int flags) {
		//07|E7|07|00|---0--0x|00000111|11100111|00_0kr_111||rotate
		int k = (instruction>>4)&1; // 0=yes C, 1=no C
		int r = (instruction>>3)&1; // 0=RL, 1=RR
				
		regF = regF & (0xFF-18);
		
		int ub =regA>>7;
		int lb = regA&1;
		int ca = regF&1;
		
		if(k==0) {
			if(r==0) {
				//RLCA
				regA = (regA<<1)&255;
				regA = regA | ub;
				regF = regF & 254;
				regF = regF | ub;
			} else {				
				//RRCA
				regA = (regA>>1)&255;
				regA = regA | (lb<<7);
				regF = regF & 254;
				regF = regF | lb;
			}
		} else {
			if(r==0) {
				//RLA		
				regA = (regA<<1)&255;
				regA = regA | ca;
				regF = regF & 254;
				regF = regF | ub;
			} else {
				//RRA	
				regA = (regA>>1)&255;
				regA = regA | (ca<<7);
				regF = regF & 254;
				regF = regF | lb;
			}
		}		
		
	}
	
	void doOpFFE6(int instruction, String di, int extra,int flags) {
		//09|FF|E6|01|sz-1-p00|11100110|11111111|11_100_110|bb|AND b
		regA = regA & extra;
		setSFlag(regA);
		setZFlag(regA);
		setPFlag(regA);
		regF = regF | 8;
		regF = regF & (0xFF - 3);
	}
	
	void doOpFFC6(int instruction, String di, int extra,int flags) {
		//0B|FF|C6|01|sz-h-v0c|11000110|11111111|11_000_110|bb|ADD A,b
		extra = regA + extra;
		setSFlag(extra);
		setZFlag(extra);
		setAddHFlag(regA,extra);
		setAddVFlag(regA,extra);
		setAddCFlag(extra);
		regF = regF & (0xFF-2);
		regA = extra & 0xFF;
	}
	
	void doOpFF32(int instruction, String di, int extra,int flags) {
		//00|FF|32|02|--------|00000010|11001111|00_11_0_010|wlwm|LD (w),A
		system.setByte(extra, regA);		
	}
	
	void doOpFF3A(int instruction, String di, int extra,int flags) {
		//00|FF|3A|02|--------|00001010|11001111|00_11_1_010|wlwm|LD A,(w)
		regA = system.getByte(extra);
	}
	
	void doOpF8A0(int instruction, String di, int extra,int flags) {
		//09|F8|A0|00|sz-1-p00|10100000|11111000|10_100_rrr||AND r
		extra = instruction & 7;
		extra = getRRR(extra);
		regF = regF | 16;
		regF = regF & (255-3);
		regA = regA & extra;
		setPFlag(regA);
		setZFlag(regA);
		setSFlag(regA);
	}	
	
	void doOpF8A8(int instruction, String di, int extra,int flags) {
		//0A|F8|A8|00|sz-0-p00|10101000|11111000|10_101_rrr||XOR r
		extra = instruction & 7;
		extra = getRRR(extra);
		regF = regF & (255 - 19);
		regA = regA ^ extra;
		setPFlag(regA);
		setZFlag(regA);
		setSFlag(regA);
	}
	
	void doOpF8B0(int instruction, String di, int extra,int flags) {
		//0A|F8|B0|00|sz-0-p00|10110000|11111000|10_110_rrr||OR r
		extra = instruction & 7;
		extra = getRRR(extra);
		regF = regF & (255-19);
		regA = regA | extra;
		setPFlag(regA);
		setZFlag(regA);
		setSFlag(regA);
	}
	
	void doOpFFF6(int instruction, String di, int extra,int flags) {
		//0A|FF|F6|01|sz-0-p00|11110110|11111111|11_110_110|bb|OR b
		regF = regF & (255-19);
		regA = regA | extra;
		setPFlag(regA);
		setZFlag(regA);
		setSFlag(regA);
	}
	
	void doOpFFFB(int instruction, String di, int extra,int flags) {
		//IMPLEMENT ME 05|FF|FB|00|xxxxxxxx|11111011|11111111|11_111_011||EI
		interruptEnabled = true;
	}
	
	void doOpC7C0(int instruction, String di, int extra,int flags) {
		//00|C7|C0|00|--------|11000000|11000111|11_cc_v_000||RET cc
		int v = (instruction>>3)&1;
		int condition = (instruction>>4)&3;
		
		int flag = 0;
		switch(condition) {
		case 0:
			flag = regF>>6; // Z
			break;
		case 1:
			flag = regF; // C
			break;
		case 2:
			throw new RuntimeException("NOT IMPLEMENTED");
			//flag = regF>>2; // V
			//break;
		case 3:
			flag = regF>>7; // S
			break;
		}
		flag = flag & 1;
		if(v==0) {
			flag = (~flag)&1;
		}
		
		if(flag==1) {
			regPC = pop();
		}
		
	}
	
	void doOpFF37(int instruction, String di, int extra,int flags) {
		//06|FF|37|00|---0--01|00110111|11111111|00_110_111||SCF
		regF = regF & (0xFF - 18);
		regF = regF | 1;
	}
	
	void doOpFF27(int instruction, String di, int extra,int flags) {
		//05|FF|27|00|xxxxxxxx|00100111|11111111|00_100_111||DAA
		//throw new RuntimeException("IMPLEMENT ME "+di);
		regA=0x11;
	}	
	
	void doOpF888(int instruction, String di, int extra,int flags) {
		//0B|F8|88|00|sz-h-v0c|10001000|11111000|10_001_rrr||ADC A,r
		int carry = regF & 1;
		int rrr = instruction & 7;
		extra = getRRR(rrr);
		extra = regA + extra+carry;
		
		setAddHFlag(regA, extra);
		setAddVFlag(regA, extra);
		setSFlag(extra);
		setZFlag(extra);
		setAddCFlag(extra);
		regF = regF & (0xFF-2);
				
		regA = extra&255;
	}	
	
	void doOpF880(int instruction, String di, int extra,int flags) {
		//0B|F8|80|00|sz-h-v0c|10000000|11111000|10_000_rrr||ADD A,r
		int rrr = instruction & 7;
		extra = getRRR(rrr);
		extra = regA + extra;
		
		setAddHFlag(regA, extra);
		setAddVFlag(regA, extra);
		setSFlag(extra);
		setZFlag(extra);
		setAddCFlag(extra);
		regF = regF & (0xFF-2);
				
		regA = extra&255;
		
	}
	
	void doOpFF22(int instruction, String di, int extra,int flags) {
		//00|FF|22|02|--------|00000010|11001111|00_10_0_010|wlwm|LD (w),HL
		system.setByte(extra, regL);
		system.setByte(extra+1,regH);
	}
	
	void doOpC704(int instruction, String di, int extra,int flags) {
		//02|C7|04|00|sz-h-v0-|00000100|11000111|00_rrr_100||INC r
		int rrr = (instruction>>3)&7;
		extra = getRRR(rrr);
		int nv = extra+1;
		
		setSFlag(nv);
		setZFlag(nv);
		setAddHFlag(extra, nv);
		setAddVFlag(extra, nv);
		regF = regF & (0xFF-2);
		
		setRRR(rrr,nv&255);
		
	}
	
	void doOpFF2A(int instruction, String di, int extra,int flags) {
		//00|FF|2A|02|--------|00001010|11001111|00_11_1_010|wlwm|LD HL,(w)
		regL=system.getByte(extra);
		regH=system.getByte(extra+1);
	}
	
	void doOpFFE3(int instruction, String di, int extra,int flags) {
		//00|FF|E3|00|--------|11100011|11111111|11_100_011||EX (SP),HL
		extra = pop();
		push((regH<<8) | regL);
		regH = extra>>8;
		regL = extra&255;		
	}
	
	void doOpFFE9(int instruction, String di, int extra,int flags) {
		//00|FF|E9|00|--------|11101001|11111111|11_101_001||JP (HL)
		regPC = (regH<<8) | regL;
	}
	
	void doOpFF2F(int instruction, String di, int extra,int flags) {
		//04|FF|2F|00|---1--1-|00101111|11111111|00_101_111||CPL
		regA = (~regA)&255;
		regF = regF | 0x12;
	}
	
	
	
	

	
	
	
	
	
	
	

	

	
	
	void doOpFF3F(int instruction, String di, int extra,int flags) {
		//03|FF|3F|00|---x--0x|00111111|11111111|00_111_111||CCF 10A4
		if( (regF&1)==1) {
			regF=regF&254;
		} else {
			regF=regF|1;
		}		
	}		

	void doOpFF76(int instruction, String di, int extra,int flags) {
		throw new RuntimeException("IMPLEMENT ME "+di);
	}	

	void doOpF898(int instruction, String di, int extra,int flags) {
		throw new RuntimeException("IMPLEMENT ME "+di);
	}	

	void doOpFFF9(int instruction, String di, int extra,int flags) {
		throw new RuntimeException("IMPLEMENT ME "+di);
	}	

	void doOpFFF3(int instruction, String di, int extra,int flags) {
		throw new RuntimeException("IMPLEMENT ME "+di);
	}

	void doOpFFCE(int instruction, String di, int extra,int flags) {
		throw new RuntimeException("IMPLEMENT ME "+di);
	}

	void doOpFFEE(int instruction, String di, int extra,int flags) {
		throw new RuntimeException("IMPLEMENT ME "+di);
	}

	void doOpC7C7(int instruction, String di, int extra,int flags) {
		throw new RuntimeException("IMPLEMENT ME "+di);
	}

	
}
