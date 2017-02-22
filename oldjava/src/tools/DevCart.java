package tools;

import java.io.FileInputStream;

//import jssc.SerialPort;
//import jssc.SerialPortException;
//import jssc.SerialPortList;
import tools.code.CU;

/**
 * This class interfaces to the development-cartridge for old computer systems. 
 */
public class DevCart 
{
	
	//SerialPort serialPort;
	
	public static void main(String [] args) throws Exception
	{
		
		//listPorts();
		
		// run fileName destAddress    LOAD + EXECUTE
				
		DevCart devCart = new DevCart(args[0]);
		
		int pos = 1;
		while(pos<args.length) {
			
			if(args[pos].equals("run")) {
				++pos;
				FileInputStream fis = new FileInputStream(args[pos++]);
				int [] data = new int[fis.available()];
				for(int x=0;x<data.length;++x) {
					data[x] = fis.read();
				}
				fis.close();
				int dest = CU.parseIntValue(args[pos++]);
				devCart.execute(dest, data);				
			} else if(args[pos].equals("ram")) {
				
				//COM10 ram 128 kidicarus.bin
				
				++pos;
				/*int size = */Integer.parseInt(args[pos++]);
				FileInputStream fis = new FileInputStream(args[pos++]);
				int [] data = new int[fis.available()];
				for(int x=0;x<data.length;++x) {
					data[x] = fis.read();
				}
				fis.close();
				
				int checksum = 0;
				for(int i : data) {
					checksum+=i;
					devCart.writeByte(i);								
				}
												
				byte [] b = devCart.readBytes(8);			
				System.out.println(":"+Integer.toHexString(checksum)+":"+new String(b)+":");
				
				return;
				
			}
			
			else {
				throw new RuntimeException("Unknown DevCart command '"+args[pos]);
			}
		}
				
		Thread.sleep(1000);		
		
		//devCart.stop();
	}
		
			
	public DevCart(String portName) throws Exception
	{
		
		//serialPort = new SerialPort(portName);
		//serialPort.openPort();
		//serialPort.setParams(SerialPort.BAUDRATE_57600,SerialPort.DATABITS_8,
		//		SerialPort.STOPBITS_1,SerialPort.PARITY_NONE);		
		
	}
	
	public static void listPorts() {
		/*
		System.out.println("List Ports:");
		String[] portNames = SerialPortList.getPortNames();
        for(int i = 0; i < portNames.length; i++){
            System.out.println(portNames[i]);
        }
        */
		
	}
	
	/*
	public void stop() throws SerialPortException
	{
		serialPort.closePort();
	}
	*/
	
	public void execute(int address, int [] data) throws Exception
	{
		writeByte('X');
		writeWord(address);
		writeWord(data.length);
		for(int x=0;x<data.length;++x) {
			writeByte(data[x]);			
		}
	}
	
	private void writeWord(int value) throws Exception
	{
		// MSB first then LSB
		writeByte(value>>8);
		writeByte(value&0xFF);		
	}
	
	private void writeByte(int value) throws Exception
	{
		//serialPort.writeByte((byte) value);
		Thread.sleep(50);
		// ?? serialPort.purgePort();
	}
	
	private byte [] readBytes(int size) throws Exception
	{
		return null; //serialPort.readBytes(size);
	}	
			
}
