package digs.spaceinvaders;

import java.awt.Dimension;
import java.awt.Graphics;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class InvadersScreen implements AddressBusDevice {
	
	private JPanel panel;
	
	//private int[] raster = new int[256*224/8];
	private int[] raster = new int[8192];
	
	private boolean dirty = true;
	
	private class InvPan extends JPanel implements Runnable {
		
		private static final long serialVersionUID = 1L;
		
		boolean running = true;
		
		InvPan() {
			//this.setPreferredSize(new Dimension(256*2,224*2));
			this.setPreferredSize(new Dimension(224*2,256*2));
			Thread tm = new Thread(this);
			tm.start();
		}
		
		@Override
		public void paint(Graphics g) {
			super.paint(g);			
			int ptr = 0;
			for(int y=0;y<224;++y) {
				for(int x=0;x<32;++x) {
					int v = raster[ptr++];
					int m = 0b1;
					for(int z=0;z<8;++z) {
						if( (v&m)>0 ) {
							g.fillRect(y*2, 256*2 - (x*8+z)*2, 2, 2);
						}
						m = m << 1;
					}
				}
			}	
			dirty = false;
		}

		@Override
		public void run() {
			while(running) {
				if(dirty) {
					this.repaint();
				}
				try {
					Thread.sleep(33);
				} catch (InterruptedException e) {
					// Eating this in case we are being woken up
				}
			}
		}		
	}
	
	public InvadersScreen() {
		panel = new InvPan();
	}
	
	@Override
	public int getByte(int address) {
		return raster[address];
	}
	
	@Override
	public void setByte(int address, int value) {
		raster[address] = value;
		dirty = true;
	}
	
	public JPanel getComponent() {
		return panel;
	}
	
	public static void main(String [] args) throws Exception {
		JFrame jf = new JFrame("Testing");
		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		InvadersScreen is = new InvadersScreen();
		for(int x=0;x<256;++x) {
			is.setByte(x, 0xAA);
		}
		jf.setContentPane(is.getComponent());
		
		jf.pack();
		jf.setVisible(true);
	}

}
