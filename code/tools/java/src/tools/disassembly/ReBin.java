package tools.disassembly;

import java.io.FileOutputStream;

import tools.code.CodeLine;
import tools.file.BinaryFile;
import tools.file.BinaryFiles;

/**
 * This tool repackages a parsed disassembly file into a new binary file. This would
 * be used when a disassembly file is modified in-line and patched to run in an 
 * emulator.
 * 
 * You can specify the ";##PatchOutput" directory name or else the tool will create ".patch"
 * files in the same directory with the input binary.
 */
public class ReBin {
	
	public static void main(String [] args) throws Exception
	{		
		
		// Load the disassembly file
		DisassemblyFile df = new DisassemblyFile("",args[0]);
		BinaryFiles bf = df.getBinaryFiles();
		
		// Write code-line data back to the disassembly files.
		for(CodeLine c : df.getLines()) {
			int ba = c.getAddress();
			int [] dat = c.getData();
			if(dat==null || dat.length==0) continue;
			for(int x=0;x<dat.length;++x) {
				bf.setByte(ba+x, dat[x]);
			}			
		}		
		
		String dir=df.getMachineInfo().getPatchOutput();
		// TODO make sure dir has a "/" and make sure to strip path from b.filename below
		
		// Write the binary data to a new set of files
		for(BinaryFile b : bf.binaryFiles) {			
			FileOutputStream fos = null;
			if(dir==null) {
				// No directory given ... use the
				fos = new FileOutputStream(b.filename+".patch");
			} else {
				fos = new FileOutputStream(dir+b.filename);
			}
			for(int i : b.data) {
				fos.write(i);
			}
			fos.flush();
			fos.close();
		}		
	}

}
