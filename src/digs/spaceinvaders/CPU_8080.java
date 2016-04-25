package digs.spaceinvaders;

// Based on the work here, but heavily modified:

/*

Java Emulation Framework

This library contains a framework for creating emulation software.

Copyright (C) 2002 Erik Duijs (erikduijs@yahoo.com)

Contributors:
- Julien Freilat
- Arnon Goncalves Cardoso
- S.C. Wong
- Romain Tisserand
- David Raingeard


This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

 */

public class CPU_8080 {	

	private AddressBusDevice ports;
	private AddressBusDevice system;

	public CPU_8080(AddressBusDevice ports, AddressBusDevice system) {
		this.ports = ports;
		this.system = system;
	}

	public void interruptNMI() {
		NMI = true;
	}

	public void interruptIRQ() {
		IRQ = true;
	}

	// The simulator code breaks these access out to different functions

	private void write16fast(int addr, int value) {
		system.setByte(addr, value&255);
		system.setByte(addr+1, value>>8);		
	}	
	private void write8fast(int addr, int value) {
		system.setByte(addr, value);		
	}
	private int read16(int addr) {
		return (system.getByte(addr+1)<<8) | system.getByte(addr);		
	}
	private void write16(int addr, int value) {
		system.setByte(addr, value&255);
		system.setByte(addr+1, value>>8);			
	}
	private int read16arg(int addr) {
		int ret = (system.getByte(addr+1)<<8) | system.getByte(addr);
		return ret;
	}
	private int read8opc(int addr) {
		return system.getByte(addr);
	}
	private void write8(int addr, int value) {
		system.setByte(addr, value);
	}
	private int read8arg(int addr) {
		return system.getByte(addr);
	}
	private int read8(int addr) {
		return system.getByte(addr);
	}
	
	

	// Original Erik Juijs work
	
	public boolean state_HALT = false;

	// registers
	private int A,F,B,C,D,E,H,L;
	private int A1,F1,B1,C1,D1,E1,H1,L1;
	private int PC,SP;
	
	// interrupt
	private  boolean IFF0 	= false; // IRQ interrupt flip-flop
	private  boolean IFF1 	= false; // NMI interrupt flip-flop
	private  boolean IRQ 	= false; // interrupt request
	private  boolean NMI 	= false; // Non-maskable interrupt
	private boolean goingToirq = false;// used to execute 1 more instruction after an irq

	// Current cycle of execution
	private int cycles_left = 0;

	// Currently executed instruction
	private int CurInstr=0;
	
	private int error=0; 			// holds an unknown instruction opcode if one is encountered
	
	// flag tables
	private static final boolean parity[] 	= new boolean[256];
	private static final int SZ[] 			= new int[256];
	private static final int SZP[] 		= new int[256];
	private static final int SZHV_inc[] 	= new int[256];
	private static final int SZHV_dec[] 	= new int[256];
	private static final int SZHVC_add[] 	= new int[2*256*256];
	private static final int SZHVC_sub[] 	= new int[2*256*256];
	
	// Build some tables to speed up execution
	static {
		int p = 0;

		for ( int i = 0; i < 256; i++ ) {
			boolean	bp = true;
			for ( int j = 0; j < 8; j++ ) {
				if ( (i & (1<<j)) != 0 ) {
					bp = !bp;
				}
			}
			parity[ i ] = bp;

			p = 0;

			if( (i&0x01) != 0 ) ++p;
			if( (i&0x02) != 0 ) ++p;
			if( (i&0x04) != 0 ) ++p;
			if( (i&0x08) != 0 ) ++p;
			if( (i&0x10) != 0 ) ++p;
			if( (i&0x20) != 0 ) ++p;
			if( (i&0x40) != 0 ) ++p;
			if( (i&0x80) != 0 ) ++p;
			SZ[i] = (i != 0) ? i & 0x80 : 0x40;
			SZ[i] |= (i & (0x20 | 0x08)); 	/* undocumented flag bits 5+3 */
			SZP[i] = SZ[i] | (((p & 1)!=0) ? 0 : 0x04);
			SZHV_inc[i] = SZ[i];
			if( i == 0x80 ) { SZHV_inc[i] |= 0x04; }
			if( (i & 0x0f) == 0x00 ) { SZHV_inc[i] |= 0x10; }
			SZHV_dec[i] = SZ[i] | 0x02;
			if( i == 0x7f ) { SZHV_dec[i] |= 0x04; }
			if( (i & 0x0f) == 0x0f ) { SZHV_dec[i] |= 0x10; }
		}

		int oldval, newval, val;
		int padd, padc, psub, psbc;
		int SF = 0x80;
		int ZF = 0x40;
		int YF = 0x20;
		int HF = 0x10;
		int XF = 0x08;
		int VF = 0x04;
		int NF = 0x02;
		int CF = 0x01;
		padd = 0*256;
		padc = 256*256;
		psub = 0*256;
		psbc = 256*256;
		for (oldval = 0; oldval < 256; oldval++)
		{
			for (newval = 0; newval < 256; newval++)
			{
				/* add or adc w/o carry set */
				val = newval - oldval;

				if (newval != 0) {
					if ((newval & 0x80) != 0) {
						SZHVC_add[padd] = SF;
					} else {
						SZHVC_add[padd] = 0;
					}
				} else {
					SZHVC_add[padd] = ZF;
				}

				SZHVC_add[padd] |= (newval & (YF | XF));	/* undocumented flag bits 5+3 */

				if( (newval & 0x0f) < (oldval & 0x0f) ) {
					SZHVC_add[padd] |= HF;
				}
				if( newval < oldval ) {
					SZHVC_add[padd] |= CF;
				}
				if( ((val^oldval^0x80) & (val^newval) & 0x80) != 0 ) {
					SZHVC_add[padd] |= VF;
				}
				padd++;

				/* adc with carry set */
				val = newval - oldval - 1;
				if (newval != 0) {
					if ((newval & 0x80) != 0) {
						SZHVC_add[padc] = SF;
					} else {
						SZHVC_add[padc] = 0;
					}
				} else {
					SZHVC_add[padc] = ZF;
				}


				SZHVC_add[padc] |= (newval & (YF | XF));	/* undocumented flag bits 5+3 */
				if( (newval & 0x0f) <= (oldval & 0x0f) ) {
					SZHVC_add[padc] |= HF;
				}
				if( newval <= oldval ) {
					SZHVC_add[padc] |= CF;
				}
				if( ((val^oldval^0x80) & (val^newval) & 0x80) != 0 ) {
					SZHVC_add[padc] |= VF;
				}
				padc++;

				/* cp, sub or sbc w/o carry set */
				val = oldval - newval;
				if ( newval != 0 ) {
					if ( (newval & 0x80) != 0 ) {
						SZHVC_sub[psub] = NF|SF;
					} else {
						SZHVC_sub[psub] = NF;
					}
				} else {
					SZHVC_sub[psub] = NF|ZF;
				}

				SZHVC_sub[psub] |= (newval & (YF | XF));	/* undocumented flag bits 5+3 */
				if( (newval & 0x0f) > (oldval & 0x0f) ) {
					SZHVC_sub[psub] |= HF;
				}
				if( newval > oldval ) {
					SZHVC_sub[psub] |= CF;
				}
				if( ((val^oldval) & (oldval^newval) & 0x80) != 0 ) {
					SZHVC_sub[psub] |= VF;
				}
				psub++;

				/* sbc with carry set */
				val = oldval - newval - 1;
				if (newval != 0) {
					if ( (newval & 0x80) != 0 ) {
						SZHVC_sub[psbc] = NF|SF;
					} else {
						SZHVC_sub[psbc] = NF;
					}
				} else {
					SZHVC_sub[psbc] = NF|ZF;
				}

				SZHVC_sub[psbc] |= (newval & (YF | XF));	/* undocumented flag bits 5+3 */
				if( (newval & 0x0f) >= (oldval & 0x0f) ) {
					SZHVC_sub[psbc] |= HF;
				}
				if( newval >= oldval ) {
					SZHVC_sub[psbc] |= CF;
				}
				if( ((val^oldval) & (oldval^newval) & 0x80) != 0 ) {
					SZHVC_sub[psbc] |= VF;
				}
				psbc++;
			}
		}
	}	


	/**
	 * Reset CPU - Only resets the registers
	 */
	public final void reset() {
		SP=0x10000; 	
		// it's actually 0 but since the 1st stack instruction is never a POP
		// we can set it to default 0x10000 in order to prevent AND-ing SP
		// with 0xffff all the time...
		PC=0;A=0;F=0;B=0;C=0;D=0;E=0;H=0;L=0;
		cycles_left=0;
		A1=0;F1=0;B1=0;C1=0;D1=0;E1=0;H1=0;L1=0;
	}
	
	public final void exec(int num_cycles) {
		
		this.cycles_left += num_cycles;

		// Make variables local (executes faster)
		int _error	= this.error;
		boolean _NMI 	= this.NMI;
		boolean _IRQ 	= this.IRQ;
		boolean _IFF0	= this.IFF0;
		boolean _IFF1	= this.IFF1;
		int instruction = this.CurInstr;
		int _PC = this.PC;
		int _SP = this.SP;
		int _B = this.B;
		int _C = this.C;
		int _D = this.D;
		int _E = this.E;
		int _H = this.H;
		int _L = this.L;
		int _A = this.A;		

		int Reg1;
		int Reg2;
		int Reg3;

		while ((cycles_left > 0) && (_error == 0)) {

			if (_NMI || (IFF0 && IRQ)) {
				if (_NMI)	{ // Take _NMI
					if (!goingToirq) {
						state_HALT = false;

						_IFF1 = _IFF0;
						_NMI  = _IFF0 = false;

						_SP-=2; write16fast(_SP,_PC); 	// Push PC
						_PC = 0x0010; 					// ...and jump to 0x0066

						cycles_left-=13;
					} else {
						goingToirq = false; /* CPU has to execute 1 more instruction */
					}
				}

				if (_IFF0 && _IRQ) {	// Take interrupt if enabled
					if (!goingToirq) {
						state_HALT = false;
						_IRQ = _IFF0 = false;
						_SP-=2; write16fast(_SP,_PC); // Push PC
						_PC = 0x0008;
						cycles_left-=13; // RST &38 = 11 cycles    + 2 cycles
					} else {
						goingToirq = false; // CPU has to execute 1 more instruction
					}
				}
			}

			instruction = read8opc(_PC);

			_PC=(_PC+1)&0xffff;
			switch(instruction) {
			case 0x00:  cycles_left-=4; break; 															// NOP			ok
			case 0x01:	cycles_left-=10; _B=read8(_PC+1); _C=read8arg(_PC); _PC+=2; break; 	// LD BC,nn		ok
			case 0x02:  cycles_left-=7; write8((_B<<8)|_C,_A); break; 								// LD (BC),A	ok
			case 0x03:	cycles_left-=6; Reg1=(((_B<<8)|_C)+1)&0xffff; _B=Reg1>>8; _C=Reg1&0xff; break; 	// INC BC		ok
			case 0x04:	cycles_left-=4; _B=inc8(_B); break; 												// INC B		ok
			case 0x05:	cycles_left-=4; _B=dec8(_B); break; 												// DEC B		ok
			case 0x06:  cycles_left-=7; _B=read8arg(_PC++); break; 								// LD B,n		ok
			case 0x07:  cycles_left-=4; _A=rlc_A(_A); break; 					 							// RLCA			ok

			case 0x08:  cycles_left-=4; Reg1=_A; _A=A1; A1=Reg1; Reg1=F; F=F1; F1=Reg1; break;  			// EX AF,AF'	ok
			case 0x09:	cycles_left-=11;Reg1=add16((_H<<8)|_L,(_B<<8)|_C); _L=Reg1&0xff; _H=Reg1>>8; break;// ADD HL,BC	ok
			case 0x0a:  cycles_left-=7; _A=read8((_B<<8)|_C); break; 								// LD A,(BC)	ok
			case 0x0b:	cycles_left-=6; Reg1=(((_B<<8)|_C)-1)&0xffff; _B=Reg1>>8; _C=Reg1&0xff; break; 	// DEC BC		ok
			case 0x0C:	cycles_left-=4; _C=inc8(_C); break; 												// INC C		ok
			case 0x0D:	cycles_left-=4; _C=dec8(_C); break; 												// DEC C		ok
			case 0x0e:  cycles_left-=7; _C=read8arg(_PC++); break; 								// LD C,n		ok
			case 0x0f:  cycles_left-=4; _A=rrc_A(_A); break; 												// RRCA			ok

			case 0x10:  _B=(_B-1)&0xff; 															// DJNZ,n		ok
			if (_B!=0) { Reg1=read8arg(_PC++); cycles_left-=13; _PC+=Reg1-((Reg1&128)<<1); } else { _PC++; cycles_left-=8; }
			break;
			case 0x11:	cycles_left-=10; _D=read8(_PC+1); _E=read8arg(_PC); _PC+=2; break; 	// LD DE,nn		ok
			case 0x12:  cycles_left-=7; write8((_D<<8)|_E,_A); break; 								// LD (DE),A	ok
			case 0x13:	cycles_left-=6; Reg1=(((_D<<8)|_E)+1)&0xffff; _D=Reg1>>8; _E=Reg1&0xff; break; 	// INC DE		ok
			case 0x14:	cycles_left-=4; _D=inc8(_D); break;												// INC D		ok
			case 0x15:	cycles_left-=4; _D=dec8(_D); break;												// DEC D		ok
			case 0x16:  cycles_left-=7; _D=read8arg(_PC++); break; 								// LD D,n		ok
			case 0x17:  cycles_left-=4; _A=rl_A(_A); break;  												// RLA

			case 0x18:  cycles_left-=12; Reg1=read8arg(_PC++); _PC+=Reg1-((Reg1&128)<<1); break;	// JR e			ok
			case 0x19:	cycles_left-=11;Reg1=add16((_H<<8)|_L,(_D<<8)|_E);_L=Reg1&0xff;_H=Reg1>>8; break; // ADD HL,DE	ok
			case 0x1a:  cycles_left-=7; _A=read8((_D<<8)|_E); break; 								// LD A,(DE)	ok
			case 0x1b:	cycles_left-=6; Reg1=(((_D<<8)|_E)-1)&0xffff; _D=Reg1>>8; _E=Reg1&0xff; break; 	// DEC DE		ok
			case 0x1C:	cycles_left-=4; _E=inc8(_E); break; 												// INC E		ok
			case 0x1D:	cycles_left-=4; _E=dec8(_E); break; 												// DEC E		ok
			case 0x1e:  cycles_left-=7; _E=read8arg(_PC++); break; 								// LD E,n		ok
			case 0x1f:  cycles_left-=4; _A=rr_A(_A); break; 												// RRA

			case 0x20:  	if ((F&0x40) == 0)															// JR NZ,e		ok
			{ Reg1=read8arg(_PC++); cycles_left-=12; _PC+=Reg1-((Reg1&128)<<1); } else { _PC++; cycles_left-=7; }
			break;
			case 0x21:	cycles_left-=10; _H=read8(_PC+1); _L=read8arg(_PC); _PC+=2; break; 	// LD HL,nn	ok
			case 0x22:  cycles_left-=16; 																	// LD (nn),HL	ok
			write16(read16arg(_PC),(_H<<8)|_L); _PC+=2; break;
			case 0x23:	cycles_left-=6; Reg1=(((_H<<8)|_L)+1)&0xffff; _H=Reg1>>8; _L=Reg1&0xff; break; 	// INC HL		ok
			case 0x24:	cycles_left-=4; _H=inc8(_H); break; 												// INC H		ok
			case 0x25:	cycles_left-=4; _H=dec8(_H); break; 												// DEC H		ok
			case 0x26:  cycles_left-=7; _H=read8arg(_PC++); break; 								// LD H,n		ok
			case 0x27:	cycles_left-=4; Reg1=_A; Reg2=0; Reg3= (F&1); int c=Reg3;							// DAA		ok
			if ( ((F&0x10)!=0) || ((Reg1 & 0x0f) > 0x09) ) { Reg2 |= 0x06; }
			if ( (Reg3==1) || ( Reg1 > 0x9f) || ((Reg1 > 0x8f) && ((Reg1 & 0x0f) > 0x09))) { Reg2|=0x60; c=1;}
			if ( Reg1 > 0x99 ) { c=1; }
			if ((F&0x02)!=0) { cycles_left-=4; _A=subA_8(Reg2,_A); }
			else { cycles_left-=4; _A=addA_8(Reg2,_A); }
			F = (F&0xfe) | c;
			if (parity[_A]) { F=(F&0xfb)|4; } else { F=(F&0xfb); }
			break;

			case 0x28:   if ((F&0x40)!=0)															// JR Z,e		ok
			{ Reg1=read8arg(_PC++); cycles_left-=12; _PC+=Reg1-((Reg1&128)<<1); } else { _PC++; cycles_left-=7; }
			break;
			case 0x29:	cycles_left-=11;Reg1=add16((_H<<8)|_L,(_H<<8)|_L); _L=Reg1&0xff; _H=Reg1>>8; break;// ADD HL,HL	ok
			case 0x2a:   cycles_left-=16; 																	// LD HL,(nn)	ok
			_H=read8(read16arg(_PC)+1); _L=read8(read16arg(_PC)); _PC+=2; break;
			case 0x2b:	cycles_left-=6; Reg1=(((_H<<8)|_L)-1)&0xffff; _H=Reg1>>8; _L=Reg1&0xff; break; 	// DEC HL		ok
			case 0x2C:	cycles_left-=4; _L=inc8(_L); break; 												// INC L		ok
			case 0x2D:	cycles_left-=4; _L=dec8(_L); break; 												// DEC L		ok
			case 0x2e:   cycles_left-=7; _L=read8arg(_PC++); break; 								// LD L,n		ok
			case 0x2f:   cycles_left-=4; _A^=0xff; F=(F&(0xc5))|0x12|(_A&(0x28));break;					// CPL			ok

			case 0x30:   if ((F&1)==0)																// JR NC,e		ok
			{ Reg1=read8arg(_PC++); cycles_left-=12; _PC+=Reg1-((Reg1&128)<<1); } else { _PC++; cycles_left-=7; }
			break;
			case 0x31:	cycles_left-=10; _SP=read16(_PC); _PC+=2; break; 							// LD _SP,nn	ok
			case 0x32:   cycles_left-=13; write8(read16arg(_PC),_A); _PC+=2; break;	 		// LD (nn),A	ok
			case 0x33:	cycles_left-=6; _SP=(_SP+1)&0xffff; break; 										// INC _SP		ok
			case 0x34:	cycles_left-=11; Reg1=(_H<<8)|_L; write8(Reg1,inc8(read8(Reg1))); break; // INC (HL)		ok
			case 0x35:	cycles_left-=11; Reg1=(_H<<8)|_L; write8(Reg1,dec8(read8(Reg1))); break; // DEC (HL)		ok
			case 0x36:   cycles_left-=10; write8((_H<<8)|_L,read8arg(_PC++)); break; 		// LD (HL),n	ok
			case 0x37:	cycles_left-=4; F=(F&0xc4)|1|(_A&(0x28)); break;				 					// SCF			ok

			case 0x38:   if ((F&1)!=0)																// JR C,e		ok
			{ Reg1=read8arg(_PC++); cycles_left-=12; _PC+=Reg1-((Reg1&128)<<1); } else { _PC++; cycles_left-=7; }
			break;
			case 0x39:	cycles_left-=11; Reg1=add16((_H<<8)|_L, _SP); _L=Reg1&0xff; _H=Reg1>>8; break; 	// ADD HL,_SP	ok
			case 0x3a:   cycles_left-=13; _A=read8(read16arg(_PC)); _PC+=2; break; 			// LD A,(nn)	ok
			case 0x3b:	cycles_left-=6; _SP=(_SP-1)&0xffff; break; 					  					// DEC _SP		ok
			case 0x3C:	cycles_left-=4; _A=inc8(_A); break; 												// INC A		ok
			case 0x3D:	cycles_left-=4; _A=dec8(_A); break; 												// DEC A		ok
			case 0x3e:   cycles_left-=7; _A=read8arg(_PC++); break; 								// LD A,n		ok
			case 0x3f:   cycles_left-=4; F=((F&0xc5)|((F&1)<<4)|(_A&0x28))^1; break;						// CCF			ok

			case 0x40:	cycles_left-=4; break; 															// LD B,B
			case 0x41:	cycles_left-=4; _B=_C; break; 													// LD B,C		ok
			case 0x42:	cycles_left-=4; _B=_D; break; 													// LD B,D		ok
			case 0x43:	cycles_left-=4; _B=_E; break; 													// LD B,E		ok
			case 0x44:	cycles_left-=4; _B=_H; break; 													// LD B,H		ok
			case 0x45:	cycles_left-=4; _B=_L; break; 													// LD B,L		ok
			case 0x46:	cycles_left-=7; _B=read8((_H<<8)|_L); break; 								// LD B,(HL)	ok	ok
			case 0x47:	cycles_left-=4; _B=_A; break; 													// LD B,A		ok

			case 0x48:	cycles_left-=4; _C=_B; break; 													// LD C,B		ok
			case 0x49:	cycles_left-=4; break; 															// LD C,C		ok
			case 0x4a:	cycles_left-=4; _C=_D; break; 													// LD C,D		ok
			case 0x4b:	cycles_left-=4; _C=_E; break; 													// LD C,E		ok
			case 0x4c:	cycles_left-=4; _C=_H; break; 													// LD C,H		ok
			case 0x4d:	cycles_left-=4; _C=_L; break; 													// LD C,L		ok
			case 0x4e:	cycles_left-=7; _C=read8((_H<<8)|_L); break; 								// LD C,(HL)	ok	ok
			case 0x4f:	cycles_left-=4; _C=_A; break; 													// LD C,A	ok

			case 0x50:	cycles_left-=4; _D=_B; break; 													// LD D,B	ok
			case 0x51:	cycles_left-=4; _D=_C; break; 													// LD D,C	ok
			case 0x52:	cycles_left-=4; break; 															// LD D,D	ok
			case 0x53:	cycles_left-=4; _D=_E; break; 													// LD D,E	ok
			case 0x54:	cycles_left-=4; _D=_H; break; 													// LD D,H	ok
			case 0x55:	cycles_left-=4; _D=_L; break; 													// LD D,L	ok
			case 0x56:	cycles_left-=7; _D=read8((_H<<8)|_L); break; 								// LD D,(HL)	ok	ok
			case 0x57:	cycles_left-=4; _D=_A; break; 													// LD D,A	ok

			case 0x58:	cycles_left-=4; _E=_B; break; 													// LD E,B	ok
			case 0x59:	cycles_left-=4; _E=_C; break; 													// LD E,C	ok
			case 0x5a:	cycles_left-=4; _E=_D; break; 													// LD E,D	ok
			case 0x5b:	cycles_left-=4; break; 															// LD E,E	ok
			case 0x5c:	cycles_left-=4; _E=_H; break; 													// LD E,H	ok
			case 0x5d:	cycles_left-=4; _E=_L; break; 													// LD E,L	ok
			case 0x5e:	cycles_left-=7; _E=read8((_H<<8)|_L); break; 											// LD E,(HL)	ok	ok
			case 0x5f:	cycles_left-=4; _E=_A; break; 															// LD E,A	ok

			case 0x60:	cycles_left-=4; _H=_B; break; 															// LD H,B	ok
			case 0x61:	cycles_left-=4; _H=_C; break; 															// LD H,C	ok
			case 0x62:	cycles_left-=4; _H=_D; break; 															// LD H,D	ok
			case 0x63:	cycles_left-=4; _H=_E; break; 															// LD H,E	ok
			case 0x64:	cycles_left-=4; break; 																	// LD H,H	ok
			case 0x65:	cycles_left-=4; _H=_L; break; 															// LD H,L	ok
			case 0x66:	cycles_left-=7; _H=read8((_H<<8)|_L); break; 											// LD H,(HL)	ok	ok
			case 0x67:	cycles_left-=4; _H=_A; break; 															// LD H,A	ok

			case 0x68:	cycles_left-=4; _L=_B; break; 															// LD L,B	ok
			case 0x69:	cycles_left-=4; _L=_C; break; 															// LD L,C	ok
			case 0x6a:	cycles_left-=4; _L=_D; break; 															// LD L,D	ok
			case 0x6b:	cycles_left-=4; _L=_E; break; 															// LD L,E	ok
			case 0x6c:	cycles_left-=4; _L=_H; break; 															// LD L,H	ok
			case 0x6d:	cycles_left-=4; break; 																	// LD L,L	ok
			case 0x6e:	cycles_left-=7; _L=read8((_H<<8)|_L); break; 											// LD L,(HL)	ok	ok
			case 0x6f:	cycles_left-=4; _L=_A; break; 															// LD L,A	ok

			case 0x70:	cycles_left-=7; write8((_H<<8)|_L,_B); break; 										// LD (HL),B	ok
			case 0x71:	cycles_left-=7; write8((_H<<8)|_L,_C); break; 										// LD (HL),C	ok
			case 0x72:	cycles_left-=7; write8((_H<<8)|_L,_D); break; 										// LD (HL),D	ok
			case 0x73:	cycles_left-=7; write8((_H<<8)|_L,_E); break; 										// LD (HL),E	ok
			case 0x74:	cycles_left-=7; write8((_H<<8)|_L,_H); break; 										// LD (HL),H	ok
			case 0x75:	cycles_left-=7; write8((_H<<8)|_L,_L); break; 										// LD (HL),L	ok
			case 0x76:	cycles_left-=4; state_HALT = true; _PC--; cycles_left=0; break;									// HALT			ok
			case 0x77:	cycles_left-=7; write8((_H<<8)|_L,_A); break; 										// LD (HL),A	ok

			case 0x78:	cycles_left-=4; _A=_B; break; 															// LD A,B		ok
			case 0x79:	cycles_left-=4; _A=_C; break; 															// LD A,C	ok
			case 0x7a:	cycles_left-=4; _A=_D; break; 															// LD A,D	ok
			case 0x7b:	cycles_left-=4; _A=_E; break; 															// LD A,E	ok
			case 0x7c:	cycles_left-=4; _A=_H; break; 															// LD A,H	ok
			case 0x7d:	cycles_left-=4; _A=_L; break; 															// LD A,L	ok
			case 0x7e:	cycles_left-=7; _A=read8((_H<<8)|_L); break; 											// LD A,(HL)	ok	ok
			case 0x7f:	cycles_left-=4; break; 																	// LD A,A	ok

			case 0x80:	cycles_left-=4; _A=addA_8(_B,_A); break; 													// ADD A,B	ok
			case 0x81:	cycles_left-=4; _A=addA_8(_C,_A); break; 													// ADD A,C	ok
			case 0x82:	cycles_left-=4; _A=addA_8(_D,_A); break; 													// ADD A,D	ok
			case 0x83:	cycles_left-=4; _A=addA_8(_E,_A); break; 													// ADD A,E	ok
			case 0x84:	cycles_left-=4; _A=addA_8(_H,_A); break; 													// ADD A,H	ok
			case 0x85:	cycles_left-=4; _A=addA_8(_L,_A); break; 													// ADD A,L	ok
			case 0x86:   cycles_left-=7; _A=addA_8(read8((_H<<8)|_L),_A); break; 								// ADD A,(HL)	ok
			case 0x87:	cycles_left-=4; _A=addA_8(_A,_A); break; 													// ADD A,A	ok

			case 0x88:	cycles_left-=4; _A=adcA_8(_B,_A); break; 													// ADC A,B	ok
			case 0x89:	cycles_left-=4; _A=adcA_8(_C,_A); break; 													// ADC A,C	ok
			case 0x8a:	cycles_left-=4; _A=adcA_8(_D,_A); break; 													// ADC A,D	ok
			case 0x8b:	cycles_left-=4; _A=adcA_8(_E,_A); break; 													// ADC A,E	ok
			case 0x8c:	cycles_left-=4; _A=adcA_8(_H,_A); break; 													// ADC A,H	ok
			case 0x8d:	cycles_left-=4; _A=adcA_8(_L,_A); break; 													// ADC A,L	ok
			case 0x8e:   cycles_left-=7; _A=adcA_8(read8((_H<<8)|_L),_A); break; 								// ADC A,(HL)	ok
			case 0x8f:	cycles_left-=4; _A=adcA_8(_A,_A); break; 													// ADC A,A	ok

			case 0x90:	cycles_left-=4; _A=subA_8(_B,_A); break; 													// SUB A,B	ok
			case 0x91:	cycles_left-=4; _A=subA_8(_C,_A); break; 													// SUB A,C	ok
			case 0x92:	cycles_left-=4; _A=subA_8(_D,_A); break; 													// SUB A,D	ok
			case 0x93:	cycles_left-=4; _A=subA_8(_E,_A); break; 													// SUB A,E	ok
			case 0x94:	cycles_left-=4; _A=subA_8(_H,_A); break; 													// SUB A,H	ok
			case 0x95:	cycles_left-=4; _A=subA_8(_L,_A); break; 													// SUB A,L	ok
			case 0x96:   cycles_left-=7; _A=subA_8(read8((_H<<8)|_L),_A); break; 								// SUB A,(HL)	ok
			case 0x97:	cycles_left-=4; _A=subA_8(_A,_A); break; 													// SUB A,A	ok

			case 0x98:	cycles_left-=4; _A=sbcA_8(_B,_A); break; 													// SBC A,B	ok
			case 0x99:	cycles_left-=4; _A=sbcA_8(_C,_A); break; 													// SBC A,C	ok
			case 0x9a:	cycles_left-=4; _A=sbcA_8(_D,_A); break; 													// SBC A,D	ok
			case 0x9b:	cycles_left-=4; _A=sbcA_8(_E,_A); break; 													// SBC A,E	ok
			case 0x9c:	cycles_left-=4; _A=sbcA_8(_H,_A); break; 													// SBC A,H	ok
			case 0x9d:	cycles_left-=4; _A=sbcA_8(_L,_A); break; 													// SBC A,L	ok
			case 0x9e:   cycles_left-=7; _A=sbcA_8(read8((_H<<8)|_L),_A); break; 								// SBC A,(HL)	ok
			case 0x9f:	cycles_left-=4; _A=sbcA_8(_A,_A); break; 													// SBC A,A	ok

			case 0xa0:	cycles_left-=4; _A=andA(_B,_A); break; 													// AND B	ok
			case 0xa1:	cycles_left-=4; _A=andA(_C,_A); break; 													// AND C	ok
			case 0xa2:	cycles_left-=4; _A=andA(_D,_A); break; 													// AND D	ok
			case 0xa3:	cycles_left-=4; _A=andA(_E,_A); break; 													// AND E	ok
			case 0xa4:	cycles_left-=4; _A=andA(_H,_A); break; 													// AND H	ok
			case 0xa5:	cycles_left-=4; _A=andA(_L,_A); break; 													// AND L	ok
			case 0xa6:   cycles_left-=7; _A=andA(read8((_H<<8)|_L),_A); break; 								// AND (HL)	ok
			case 0xa7:	cycles_left-=4; _A=andA(_A,_A); break; 													// AND A	ok

			case 0xa8:	cycles_left-=4; _A=xorA(_B,_A); break; 													// XOR B	ok
			case 0xa9:	cycles_left-=4; _A=xorA(_C,_A); break; 													// XOR C	ok
			case 0xaa:	cycles_left-=4; _A=xorA(_D,_A); break; 													// XOR D	ok
			case 0xab:	cycles_left-=4; _A=xorA(_E,_A); break; 													// XOR E	ok
			case 0xac:	cycles_left-=4; _A=xorA(_H,_A); break; 													// XOR H	ok
			case 0xad:	cycles_left-=4; _A=xorA(_L,_A); break; 													// XOR L	ok
			case 0xae:   cycles_left-=7; _A=xorA(read8((_H<<8)|_L),_A); break; 								// XOR (HL)	ok
			case 0xaf:	cycles_left-=4; _A=xorA(_A,_A); break; 													// XOR A	ok

			case 0xb0:	cycles_left-=4; _A=orA(_B,_A); break; 													// OR B		ok
			case 0xb1:	cycles_left-=4; _A=orA(_C,_A); break; 													// OR C		ok
			case 0xb2:	cycles_left-=4; _A=orA(_D,_A); break; 													// OR D		ok
			case 0xb3:	cycles_left-=4; _A=orA(_E,_A); break; 													// OR E		ok
			case 0xb4:	cycles_left-=4; _A=orA(_H,_A); break; 													// OR H		ok
			case 0xb5:	cycles_left-=4; _A=orA(_L,_A); break; 													// OR L		ok
			case 0xb6:   cycles_left-=7; _A=orA(read8((_H<<8)|_L),_A); break; 									// OR (HL)	ok
			case 0xb7:	cycles_left-=4; _A=orA(_A,_A); break; 													// OR A		ok

			case 0xb8:	cycles_left-=4; cpA_8(_B,_A); break; 														// CP B		ok
			case 0xb9:	cycles_left-=4; cpA_8(_C,_A); break; 														// CP C		ok
			case 0xba:	cycles_left-=4; cpA_8(_D,_A); break; 														// CP D		ok
			case 0xbb:	cycles_left-=4; cpA_8(_E,_A); break; 														// CP E		ok
			case 0xbc:	cycles_left-=4; cpA_8(_H,_A); break; 														// CP H		ok
			case 0xbd:	cycles_left-=4; cpA_8(_L,_A); break; 														// CP L		ok
			case 0xbe:   cycles_left-=7; cpA_8(read8((_H<<8)|_L),_A); break; 									// CP A,(HL)ok
			case 0xbf:	cycles_left-=4; cpA_8(_A,_A); break; 														// CP A		ok

			case 0xc0:	if ((F&0x40) == 0) {cycles_left-=11;_PC=read16arg(_SP);_SP+=2;} else {cycles_left-=5;} break; // RET NZ	ok
			case 0xc1:	cycles_left-=10; _B=read8(_SP+1); _C=read8(_SP); _SP+=2; break;					// POP BC	ok
			case 0xc2:	cycles_left-=10; if ((F&0x40) == 0) { _PC=read16arg(_PC); } else {_PC+=2;}	break;	// JP NZ,nn	ok
			case 0xc3:   cycles_left-=10; _PC=read16arg(_PC); break; 											// JP nn	ok
			case 0xc4:	if ((F&0x40) == 0) { _SP-=2; write16fast(_SP,_PC+2); cycles_left-=17; _PC=read16arg(_PC); } else {_PC+=2;cycles_left-=10;} break; // CALL NZ,nn	ok
			case 0xc5:	cycles_left-=11; write16(_SP-2,((_B<<8)|_C)); _SP-=2; break; 							// PUSH BC	ok
			case 0xc6:   cycles_left-= 7; _A=addA_8(read8(_PC++),_A); break; 									// ADD A,n	ok
			case 0xc7: 	cycles_left-=11; _SP-=2; write16fast(_SP,_PC); _PC=0x00; break; 						// RST $00	ok

			case 0xc8:	if ((F&0x40)!=0) {cycles_left-=11;_PC=read16arg(_SP); _SP+=2; } else {cycles_left-=5;} break; // RET Z	ok
			case 0xc9: 	cycles_left-=10; _PC=read16arg(_SP); _SP+=2; break; 									// RET		ok
			case 0xca:	cycles_left-=10; if ((F&0x40)!=0) { _PC=read16arg(_PC); } else {_PC+=2;} break; 		// JP Z,nn ok
			case 0xcc:	if ((F&0x40)!=0) { _SP-=2; write16fast(_SP,_PC+2); cycles_left-=17; _PC=read16arg(_PC); } else {cycles_left-=10;_PC+=2;} break;	// CALL Z,nn	ok
			case 0xcd:  	cycles_left-=17; _SP-=2; write8fast (_SP+1,(_PC+2)>>8); write8fast (_SP,(_PC+2)&0xff); _PC=read16arg(_PC); break; 	// CALL nn	ok
			case 0xce:   cycles_left-= 7; _A=adcA_8(read8arg(_PC++),_A); break; 								// ADC A,n	ok
			case 0xcf: 	cycles_left-=11; _SP-=2; write16fast(_SP,_PC); _PC=0x08; break; 						// RST $08	ok

			case 0xd0:	if ((F&1)==0) {cycles_left-=11;_PC=read16arg(_SP); _SP+=2; } else {cycles_left-=5;} break; 	// RET NC	ok
			case 0xd1:	cycles_left-=10; _D=read8(_SP+1); _E=read8(_SP); _SP+=2; break; 					// POP DE	ok
			case 0xd2:	cycles_left-=10; if ((F&1)==0) { _PC=read16arg(_PC); } else {_PC+=2;}	break; 		// JP NC,nn	ok
			case 0xd3:   cycles_left-=11; out(read8arg(_PC++),_A); break; 									// OUT (n),A	ok
			case 0xd4:	if ((F&1)==0) { _SP-=2; write16fast(_SP,_PC+2); cycles_left-=17; _PC=read16arg(_PC); } else {cycles_left-=10;_PC+=2;} break; 	// CALL NC,nn	ok
			case 0xd5:	cycles_left-=11; write16(_SP-2,((_D<<8)|_E)); _SP-=2; break; 							// PUSH DE	ok
			case 0xd6:   cycles_left-= 7; _A=subA_8(read8arg(_PC++),_A); break; 								// SUB A,n	ok
			case 0xd7: 	cycles_left-=11; _SP-=2; write16fast(_SP,_PC); _PC=0x10; break; 						// RST $10	ok

			case 0xd8:	if ((F&1)!=0)  {cycles_left-=11;_PC=read16arg(_SP); _SP+=2; } else {cycles_left-= 5;} break;	// RET C	ok
			case 0xd9:   cycles_left-= 4; Reg1=_B; _B=B1; B1=Reg1; Reg1=_C; _C=C1; C1=Reg1; Reg1=_D; _D=D1; D1=Reg1; Reg1=_E; _E=E1; E1=Reg1; Reg1=_H; _H=H1; H1=Reg1; Reg1=_L; _L=L1; L1=Reg1; break; // EXX	ok
			case 0xda:	cycles_left-=10; if ((F&1)!=0) { _PC=read16arg(_PC); } else {_PC+=2;}	break; 		// JP C,nn	ok
			case 0xdb:	cycles_left-=11; _A=in(read8arg(_PC++), _A); break; 									// IN A,(n)	ok
			case 0xdc:	if ((F&1)!=0) { _SP-=2; write16fast(_SP,_PC+2); cycles_left-=17; _PC=read16arg(_PC); } else {cycles_left-=10;_PC+=2;} break; 	// CALL C,nn	ok
			case 0xde:   cycles_left-= 7; _A=sbcA_8(read8arg(_PC++),_A); break; 								// SBC A,n	ok
			case 0xdf: 	cycles_left-=11; _SP-=2; write16fast(_SP,_PC); _PC=0x18; break; 						// RST $18	ok

			case 0xe0:	if ((F&4)==0) {cycles_left-=11;_PC=read16arg(_SP); _SP+=2;} else {cycles_left-= 5;} break;	// RET PO	ok
			case 0xe1:	cycles_left-=10; _H=read8(_SP+1); _L=read8(_SP); _SP+=2; break; 					// POP HL	ok
			case 0xe2:	cycles_left-=10; if ((F&4)==0){ _PC=read16arg(_PC); } else {_PC+=2;}	break; 			// JP PO,nn	ok
			case 0xe3:   cycles_left-=19; 																			// EX (_SP),HL	ok
			Reg1=read8(_SP+1); write8(_SP+1,_H); _H=Reg1; Reg1=read8(_SP); write8(_SP,_L); _L=Reg1; break;
			case 0xe4:	cycles_left-=10; if ((F&4)==0){ _SP-=2; write16fast(_SP,_PC+2); cycles_left-=17; _PC=read16arg(_PC); } else {_PC+=2;} break; // CALL PO,nn	ok
			case 0xe5:	cycles_left-=11; write16(_SP-2,((_H<<8)|_L)); _SP-=2; break; 							// PUSH HL	ok
			case 0xe6:   cycles_left-= 7; _A=andA(read8arg(_PC++),_A); break; 									// AND A,n	ok
			case 0xe7: 	cycles_left-=11; _SP-=2; write16fast(_SP,_PC); _PC=0x20; break; 						// RST $20	ok

			case 0xe8:	if ((F&4)!=0) { cycles_left-=11;_PC=read16arg(_SP); _SP+=2;} else {cycles_left-=5;} break;	// RET PE	ok
			case 0xe9:   cycles_left-= 4; _PC=(_H<<8)|_L; break; 													// JP (HL)	ok
			case 0xea:	cycles_left-=10; if ((F&4)!=0){ _PC=read16arg(_PC); } else {_PC+=2;} break; 			// JP PE,nn	ok
			case 0xeb:   cycles_left-= 4; Reg1=_D; _D=_H; _H=Reg1; Reg1=_E; _E=_L; _L=Reg1;  break; 				// EX DE,HL	ok
			case 0xec:	cycles_left-=10; if ((F&4)!=0){ _SP-=2; write16fast(_SP,_PC+2); cycles_left-=17; _PC=read16arg(_PC); } else {_PC+=2;} break; // CALL PE,nn	ok
			case 0xee:   cycles_left-= 7; _A=xorA(read8arg(_PC++),_A); break; 									// XOR A,n	ok
			case 0xef: 	cycles_left-=11; _SP-=2; write16fast(_SP,_PC); _PC=0x28; break; 						// RST $28	ok

			case 0xf0:	if ((F&0x80) == 0) {cycles_left-=11;_PC=read16arg(_SP); _SP+=2; } else {cycles_left-=5;} break;// RET P	ok
			case 0xf1:	cycles_left-=10; _A=read8(_SP+1); F=read8(_SP); _SP+=2; break;					// POP AF	ok
			case 0xf2:	cycles_left-=10; if ((F&0x80) == 0) { _PC=read16arg(_PC); } else {_PC+=2;}	break; 	// JP P,nn	ok
			case 0xf3:   cycles_left-= 4; _IFF0 = _IFF1 = false; break; 											// DI		ok
			case 0xf4:	cycles_left-=10; if ((F&0x80) == 0) { _SP-=2; write16fast(_SP,_PC+2); cycles_left-=17; _PC=read16arg(_PC); } else {_PC+=2;} break; // CALL P,nn	ok
			case 0xf5:	cycles_left-=11; write16(_SP-2,((_A<<8)|F)); _SP-=2; break; 							// PUSH AF	ok
			case 0xf6:   cycles_left-= 7; _A=orA(read8arg(_PC++),_A); break; 									// OR A,n	ok
			case 0xf7: 	cycles_left-=11; _SP-=2; write16fast(_SP,_PC); _PC=0x30; break; 						// RST $30	ok

			case 0xf8:	if ((F&0x80)!=0) {cycles_left-=11;_PC=read16arg(_SP);_SP+=2;} else {cycles_left-=5;} break;// RET M	ok
			case 0xf9:   cycles_left-= 6; _SP=(_H<<8)|_L; break; 													// LD _SP,HL	ok
			case 0xfa:	cycles_left-=10; if ((F&0x80)!=0) { _PC=read16arg(_PC); } else {_PC+=2;} break; 		// JP M,nn	ok
			case 0xfb:   cycles_left-= 4; _IFF0 = _IFF1 = true; goingToirq = true; break; 							// EI		ok
			case 0xfc:	cycles_left-=10; if ((F&0x80)!=0) { _SP-=2; write16fast(_SP,_PC+2); cycles_left-=17; _PC=read16arg(_PC); } else {_PC+=2;} break; // CALL M,nn	ok
			case 0xfe:   cycles_left-=7; cpA_8(read8arg(_PC++),_A); break; 									// CP A,n	ok
			case 0xff: 	cycles_left-=11; _SP-=2; write16fast(_SP,_PC); _PC=0x38; break; 						// RST $38	ok


			default :   _error=instruction; break; // Not implemented
			}
		}	

		this.CurInstr = instruction;
		this.IRQ	= _IRQ;
		this.NMI	= _NMI;
		this.IFF0	= _IFF0;
		this.IFF1 = _IFF1;
		this.PC	= _PC;
		this.SP	= _SP;
		this.B	= _B;
		this.C	= _C;
		this.D	= _D;
		this.E	= _E;
		this.H	= _H;
		this.L	= _L;
		this.A	= _A;

	}	

	/**
	 * Add value to Accu and set flags accordingly
	 */
	private final int addA_8(int value, int A) {
		int result = (A + value) &0xff;
		F = SZHVC_add[ (A<<8) | result];
		return result;
	}

	/**
	 * Add value with carry to Accu and set flags accordingly
	 */
	private final int adcA_8(int value, int A) {
		int c = F & 1;
		int result = (A + value + c) & 0xff;
		F = SZHVC_add[(c << 16) | (A<<8) | result];
		return result;
	}

	/**
	 * 8 bit increment
	 */
	private final int inc8(int value) {
		value = (value + 1) & 0xff;
		F = (F & 1) | SZHV_inc[value];
		return value;
	}

	/**
	 * 8 bit decrement
	 */
	private final int dec8(int value) {
		value = (value - 1) & 0xff;
		F = (F & 1) | SZHV_dec[value];
		return (value);
	}

	/**
	 * Compare value with Accu
	 */
	private final void cpA_8(int value, int A) {
		int result = (A - value) & 0xff;
		F = SZHVC_sub[(A<<8) | result];
	}

	/**
	 * Subtract value from Accu and set flags accordingly
	 */
	private final int subA_8(int value, int A) {
		int result = (A - value) & 0xff;
		F = SZHVC_sub[ (A<<8) | result];
		return result;
	}

	/**
	 * Subtract value with carry from Accu and set flags accordingly
	 */
	private final int sbcA_8(int value, int A) {
		int c = F & 1;
		int result = (A - value - c) & 0xff;
		F = SZHVC_sub[(c<<16) | (A<<8) | result];
		return result;
	}

	/**
	 * 16bit Add
	 */
	private final int add16( int a, int b ) {
		int result = a + b;
		F = (F & 0xc4) | (((a ^ result ^ b) >> 8) & 0x10) | ((result >> 16) & 1);
		return (result & 0xffff);
	}

	/**
	 * 9-bit left rotate A	- ok
	 */
	private final int rl_A(int A) {
		int old = A;
		A=((A<<1)|(F&1))&0xff; 						// rotate
		F = (F & 0xec) | (old >> 7);
		return A;
	}

	/**
	 * 9-bit right rotate A
	 */
	private final int rr_A(int A) {
		int old = A;
		A=((A>>1)|(F&1)<<7)&0xff; 					// rotate
		F = (F & 0xec) | (old & 1);
		return A;
	}

	/**
	 * left rotate	- ok
	 */
	private final int rlc_A(int A) {
		F = (F & 0xec) | (A >> 7);
		//F = (F & 0xc5) | ((A >> 7) | (A & 0x28));		// including undocumented flags
		return ((A<<1)+((A&128)>>7))&0xff; 				// rotate
	}

	/**
	 * right rotate	A - ok
	 */
	private final int rrc_A(int A) {
		F = (F & 0xec) | (A&0x29);
		return ((A>>1)+((A&1)<<7))&0xff; 				// rotate
	}

	/**
	 * AND	- ok
	 */
	private final int andA( int value, int A ) {
		A &= value;
		F= SZP[A] | 0x10;
		return A;
	}

	/**
	 * OR	- ok
	 */
	private final int orA( int value, int A ) {
		A |= value;
		F = SZP[A];
		return A;
	}

	/**
	 * XOR - ok
	 */
	private final int xorA( int value, int A ) {
		A ^= value;
		F = SZP[A];
		return A;
	}

	private final void out(int port, int value) {
		ports.setByte(port, value);		 
	}

	private final int in(int port, int A) {
		int in=ports.getByte(port);
		F = (F & 1) | SZP[A];
		return in;
	}

}
