package digs.spaceinvaders;

import java.awt.BorderLayout;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class Invaders {
	
	static CPU_8080 cpu;

	public static void main(String[] args) throws Exception {
				
		SimpleAddressBus ports = new SimpleAddressBus();
		
		InvadersPorts ip = new InvadersPorts();
		ports.addDevice(0, 256, ip);
		
		SimpleAddressBus sys = new SimpleAddressBus();
				
		ROM rom = new ROM("content/arcade/SpaceInvaders/midway.bin");
		sys.addDevice(0, 8192, rom); // 8K of ROM at 0x0000
		
		RAM ram = new RAM(1024); 
		sys.addDevice(0x2000, 1024, ram); // 1K of RAM at 0x2000
		
		InvadersScreen scr = new InvadersScreen();
		sys.addDevice(0x2400, 8192, scr); // Screen raster (8K) at 0x2400
		
		cpu = new CPU_8080(ports,sys);
		//CPU_SPIN8080 cpu = new CPU_SPIN8080(ports,sys);
		
		JFrame jf = new JFrame("Space Invaders");
		JPanel jp = new JPanel(new BorderLayout());
		jp.add(BorderLayout.CENTER,scr.getComponent());
		jf.setContentPane(jp);
		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		jf.pack();
		jf.setVisible(true);		
		
		// Crude logic here ... just for testing
		while(true) {		
			cpu.exec(50_000);		
			cpu.interruptNMI();
			cpu.exec(50_000);	
			cpu.interruptIRQ();						
			Thread.sleep(20);
		}	
		
	}

}
