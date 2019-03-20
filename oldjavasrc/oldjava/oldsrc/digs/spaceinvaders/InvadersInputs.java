package digs.spaceinvaders;

import java.awt.FlowLayout;

import javax.swing.JCheckBox;
import javax.swing.JPanel;

public class InvadersInputs extends JPanel 
{
	
	private static final long serialVersionUID = 1L;
	
	JCheckBox [] bits = new JCheckBox[8];
	
	public int getValue() {
		int ret = 0;
		for(int x=0;x<8;++x) {
			int i = 0;
			if(bits[x].isSelected()) {
				i = 1;
			}
			ret = ret + (i<<(7-x));			
		}
		return ret;
		//return 0;
	}
	
	public InvadersInputs()
	{
		super(new FlowLayout());
		for(int x=0;x<8;++x) {
			bits[x] = new JCheckBox();
			add(bits[x]);
			if(x==4) bits[x].setSelected(true);
		}
	}

}
