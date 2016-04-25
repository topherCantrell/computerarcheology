package digs.spaceinvaders;

public class InvadersPorts implements AddressBusDevice  
{
	int shiftAmount;
	String shiftData = "0000000000000000";		
			
	private void setShiftAmount(int value) {		
		shiftAmount = value;
	}
	
	private void writeShiftData(int value) {
		shiftData = shiftData.substring(0,8);
		String s = Integer.toString(value,2);
		while(s.length()<8) s="0"+s;
		shiftData = s+shiftData;
	}
	
	private int readShiftData() {
		String ret = shiftData.substring(shiftAmount,shiftAmount+8);
		return Integer.parseInt(ret,2);
	}	

	@Override
	public int getByte(int address) {
		
		switch(address) {
		
		case 0: // INP0
			return 0;
		case 1: // INP1
			return 0;
		case 2: // INP2
			return 0;
		case 3: // SHIFT_IN		
			return readShiftData();
			
			default:
				throw new RuntimeException("Unexpected port read "+address);
			
		}		
		
	}

	@Override
	public void setByte(int address, int value) {
		
		switch(address) {
		case 2: // SHIFT_AMOUNT
			setShiftAmount(value);
			break;
		case 3: // SOUND1
			break;
		case 4: // SHIFT_DATA
			writeShiftData(value);
			break;
		case 5: // SOUND2
			break;
		case 6: // WATCHDOG
			break;
			default:
				throw new RuntimeException("Unexpected port write "+address+","+value);
		}
		
	}

}
