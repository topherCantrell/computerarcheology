package sim;

public class Main {

	public static void main(String[] args) throws Exception {
		
		DissReader reader = new DissReader("content/trs80/hauntedhouse/Code1.cmark");
		
		CPU cpu = new CPUZ80(reader.getCleaned());
		
		//cpu.run(0x42E9);
		
		
		cpu.getRegister("SP").writeValue(0x7000);
		
		cpu.getRegister("A").writeValue(1);
		cpu.getRegister("HL").writeValue(0x4D7C);
		cpu.call(0x46B9);
		
		
	}

}
