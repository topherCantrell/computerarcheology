package digs.daggorath;

import java.io.PrintStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

import code.CU;
import digs.daggorath.cpu.CPU6809;

public class Level {

	static boolean isTwoDigitHex(String s, int pos) {
		if(pos>=s.length()) return false;
		char a = s.charAt(pos++);
		if(pos>=s.length()) return false;
		char b = s.charAt(pos++);

		if(pos!=s.length() && s.charAt(pos)!=' ') return false;

		if( (a>='0' && a<='9' || a>='A' && a<='F') && (b>='0' && b<='9' || b>='A' && b<='F') ) {
			return true;
		}
		return false;
	}

	static String replaceAll(String s, String key, String rep) {
		while(true) {
			int i = s.indexOf(key);
			if(i<0) return s;
			s = s.substring(0,i)+rep+s.substring(i+key.length());
		}
	}
	
	static final String holeInFloor="<rect x='15' y='15' width='20' height='20'/>";
	static final String holeInCeiling="<rect x='15' y='15' width='20' height='20' style='fill:none;stroke:rgb(0,0,0)'/>";
	static final String ladderInCeiling=
		  "<rect x='15' y='15' width='20' height='5' style='fill:none;stroke:rgb(0,0,0)'/>"+
		  "<line x1='18' y1='15' x2='18' y2='35' style='stroke:rgb(0,255,255)'/>"+
		  "<line x1='32' y1='15' x2='32' y2='35' style='stroke:rgb(0,255,255)'/>"+
		  "<line x1='18' y1='17' x2='32' y2='17' style='stroke:rgb(0,255,255)'/>"+
		  "<line x1='18' y1='21' x2='32' y2='21' style='stroke:rgb(0,255,255)'/>"+
		  "<line x1='18' y1='25' x2='32' y2='25' style='stroke:rgb(0,255,255)'/>"+
		  "<line x1='18' y1='29' x2='32' y2='29' style='stroke:rgb(0,255,255)'/>"+
		  "<line x1='18' y1='33' x2='32' y2='33' style='stroke:rgb(0,255,255)'/>";
	static final String ladderInFloor=
		  "<rect x='15' y='30' width='20' height='5' style='fill:none;stroke:rgb(0,0,0)'/>"+
		  "<line x1='18' y1='15' x2='18' y2='35' style='stroke:rgb(0,255,255)'/>"+
		  "<line x1='32' y1='15' x2='32' y2='35' style='stroke:rgb(0,255,255)'/>"+
		  "<line x1='18' y1='17' x2='32' y2='17' style='stroke:rgb(0,255,255)'/>"+
		  "<line x1='18' y1='21' x2='32' y2='21' style='stroke:rgb(0,255,255)'/>"+
		  "<line x1='18' y1='25' x2='32' y2='25' style='stroke:rgb(0,255,255)'/>"+
		  "<line x1='18' y1='29' x2='32' y2='29' style='stroke:rgb(0,255,255)'/>"+
		  "<line x1='18' y1='33' x2='32' y2='33' style='stroke:rgb(0,255,255)'/> ";
	
	
	
	
	
	public static void main(String[] args) throws Exception {
		List<String> raw = Files.readAllLines(Paths.get("src/digs/daggorath/DCode.cmark"));
		List<String> lines = new ArrayList<String>();
		
		for(String line : raw) {
			int i = line.indexOf(";");
			if(i>=0) {
				line = line.substring(0,i);
			}
			line = line.trim();
			if(line.isEmpty()) continue;
			if(!line.contains(" ") && line.endsWith(":")) {
				continue;
			}
			line = replaceAll(line,"  "," ");

			for(int pos=6;pos<line.length();pos=pos+3) {
				if(!isTwoDigitHex(line,pos)) {
					line = line.substring(0,pos)+":"+line.substring(pos);
					break;
				}
			}
			lines.add(line);	
		}
		
		
		CPU6809 cpu = new CPU6809(lines);
		cpu.getRegister("DP").writeValue(2);       // Direct Page is 0x200
		cpu.getRegister("SP").writeValue(0x1000);  // Daggorath sets the stack here
		cpu.push(0xFFFF, true);                    // Mark return-to-system
		
		// Fill map with FF		
		for(int x=0x05F4;x<0x09F4;++x) {
			cpu.writeByte(x, 0xFF);
		}
		cpu.writeMemory(0x281,0, false);						
		cpu.run(0xCCA4);
		
		
		
		for(int z=0;z<24;++z) {
			cpu.push(0xFFFF, true);                    // Mark return-to-system
			cpu.run(0xCF97);
			System.out.println(":"+cpu.getRegister("B").readValue()+","+cpu.getRegister("A").readValue());
		}
		
		
		
		
		
	}
	
	
	

	public static void main2(String[] args) throws Exception {

		List<String> raw = Files.readAllLines(Paths.get("DCode.cmark"));
		List<String> lines = new ArrayList<String>();

		for(String line : raw) {
			int i = line.indexOf(";");
			if(i>=0) {
				line = line.substring(0,i);
			}
			line = line.trim();
			if(line.isEmpty()) continue;
			if(!line.contains(" ") && line.endsWith(":")) {
				continue;
			}
			line = replaceAll(line,"  "," ");

			for(int pos=6;pos<line.length();pos=pos+3) {
				if(!isTwoDigitHex(line,pos)) {
					line = line.substring(0,pos)+":"+line.substring(pos);
					break;
				}
			}
			lines.add(line);			

		}

		PrintStream ps = new PrintStream("test2.html");

		ps.println("<html><body>");

		for(int level=0;level<5;++level) {

			CPU6809 cpu = new CPU6809(lines);
			cpu.getRegister("DP").writeValue(2);       // Direct Page is 0x200
			cpu.getRegister("SP").writeValue(0x1000);  // Daggorath sets the stack here
			cpu.push(0xFFFF, true);                    // Mark return-to-system		
			// Fill map with FF		
			for(int x=0x05F4;x<0x09F4;++x) {
				cpu.writeByte(x, 0xFF);
			}

			cpu.writeMemory(0x281,level, false);						
			cpu.run(0xCCA4);		

			ps.println("<p>");
			ps.println("<svg height='450' width='450'>");

			ps.println("<g transform='scale(0.25)'>");
			ps.println("<rect width='1700' height='1700' style='fill:rgb(150,150,150)'/>");

			for(int y=0;y<32;++y) {
				for(int x=0;x<32;++x) {				
					int c = cpu.readMemory(0x5F4+32*y+x, false);
					if(c==0xFF) {					
					} else {
						ps.println("<g transform='translate("+(x+1)*50+","+(y+1)*50+")'>");
						ps.println("<rect width='50' height='50' style='stroke-width:0;fill:rgb(250,250,250)'/>");
						int wv = (c & 3);
						switch(wv) {
						case 1:
							ps.println("<line x1='0' y1='0' x2='50' y2='0' style='stroke:rgb(0,255,0);stroke-width:4;'/>");
							break;
						case 2:
							ps.println("<line x1='0' y1='0' x2='50' y2='0' style='stroke:rgb(255,0,0);stroke-width:4;' stroke-dasharray='2,2'/>");
							break;
						}
						wv = ((c>>2) & 3);
						switch(wv) {
						case 1:
							ps.println("<line x1='50' y1='0' x2='50' y2='50' style='stroke:rgb(0,255,0);stroke-width:4;'/>");
							break;
						case 2:
							ps.println("<line x1='50' y1='0' x2='50' y2='50' style='stroke:rgb(255,0,0);stroke-width:4;' stroke-dasharray='2,2'/>");
							break;
						}
						wv = ((c>>4) & 3);
						switch(wv) {
						case 1:
							ps.println("<line x1='0' y1='50' x2='50' y2='50' style='stroke:rgb(0,255,0);stroke-width:4;'/>");
							break;
						case 2:
							ps.println("<line x1='0' y1='50' x2='50' y2='50' style='stroke:rgb(255,0,0);stroke-width:4;' stroke-dasharray='2,2'/>");
							break;
						}
						wv = ((c>>6) & 3);
						switch(wv) {
						case 1:
							ps.println("<line x1='0' y1='0' x2='0' y2='50' style='stroke:rgb(0,255,0);stroke-width:4;'/>");
							break;
						case 2:
							ps.println("<line x1='0' y1='0' x2='0' y2='50' style='stroke:rgb(255,0,0);stroke-width:4;' stroke-dasharray='2,2'/>");
							break;
						}
						ps.println("</g>");		
					}						
				}		
			}		
			for(int z=0;z<34;++z) {
				ps.println("<line x1='0' y1='"+z*50+"' x2='1700' y2='"+z*50+"' style='stroke-width:1;stroke:rgb(150,150,150)'/>");
				ps.println("<line x1='"+z*50+"' y1='0' x2='"+z*50+"' y2='1700' style='stroke-width:1;stroke:rgb(150,150,150)'/>");
			}
			
			switch(level) {
			case 0:
				ps.println("<g transform='translate(1200,50)'>"+ladderInFloor+"</g>");
				ps.println("<g transform='translate(250,800)'>"+holeInFloor+"</g>");
				ps.println("<g transform='translate(900,1050)'>"+holeInFloor+"</g>");
				ps.println("<g transform='translate(1550,1450)'>"+ladderInFloor+"</g>");
				ps.println("<g transform='translate(600,850)'><circle cx='25' cy='25' r='15' style='fill:blue'/></g>");
				break;
			case 1:
				ps.println("<g transform='translate(1200,50)'>"+ladderInCeiling+"</g>");
				ps.println("<g transform='translate(250,800)'>"+holeInCeiling+"</g>");
				ps.println("<g transform='translate(900,1050)'>"+holeInCeiling+"</g>");
				ps.println("<g transform='translate(1550,1450)'>"+ladderInCeiling+"</g>");				
				ps.println("<g transform='translate(200,150)'>"+ladderInFloor+"</g>");
				ps.println("<g transform='translate(1600,200)'>"+holeInFloor+"</g>");
				ps.println("<g transform='translate(1050,1000)'>"+holeInFloor+"</g>");
				ps.println("<g transform='translate(50,1600)'>"+holeInFloor+"</g>");				
				break;
			case 2:
				ps.println("<g transform='translate(200,150)'>"+ladderInCeiling+"</g>");
				ps.println("<g transform='translate(1600,200)'>"+holeInCeiling+"</g>");
				ps.println("<g transform='translate(1050,1000)'>"+holeInCeiling+"</g>");
				ps.println("<g transform='translate(50,1600)'>"+holeInCeiling+"</g>");
				break;
			case 3:
				ps.println("<g transform='translate(1600,50)'>"+holeInFloor+"</g>");
				ps.println("<g transform='translate(50,300)'>"+holeInFloor+"</g>");
				ps.println("<g transform='translate(1450,1150)'>"+holeInFloor+"</g>");
				ps.println("<g transform='translate(850,1600)'>"+holeInFloor+"</g>");
				break;
			case 4:
				ps.println("<g transform='translate(1600,50)'>"+holeInCeiling+"</g>");
				ps.println("<g transform='translate(50,300)'>"+holeInCeiling+"</g>");
				ps.println("<g transform='translate(1450,1150)'>"+holeInCeiling+"</g>");
				ps.println("<g transform='translate(850,1600)'>"+holeInCeiling+"</g>");
				break;				
			}
			
			
			
			// 11, 16

			ps.println("</g>");

		}

		ps.println("</svg>");
		ps.println("</body></html>");

		ps.flush();
		ps.close();


	}

}
