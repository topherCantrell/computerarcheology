package digs.spaceinvaders;

import java.util.ArrayList;
import java.util.List;

public class SimpleAddressBus implements AddressBusDevice {
	
	private static class DeviceMap {
		int start;
		int size;
		AddressBusDevice device;
	}
	
	private List<DeviceMap> devices = new ArrayList<>();
	
	
	public void addDevice(int start, int size, AddressBusDevice device) {
		DeviceMap d = new DeviceMap();
		d.start = start;
		d.size = size;
		d.device = device;
		devices.add(d);
	}
	
	private DeviceMap findDevice(int address) {
		for(DeviceMap d : devices) {
			if(address>=d.start && address<(d.start+d.size)) {
				return d;
			}
		}
		return null;
	}
	

	@Override
	public int getByte(int address) {
		DeviceMap dev = findDevice(address);
		if(dev==null) {
			throw new RuntimeException("READ: No device mapped to "+address);
		}
		return dev.device.getByte(address-dev.start);
	}

	@Override
	public void setByte(int address, int value) {
		DeviceMap dev = findDevice(address);
		if(dev==null) {
			throw new RuntimeException("WRITE: No device mapped to "+address);
		}
		dev.device.setByte(address-dev.start,value);
	}

}
