package bus;

/**
 * There are two types of busses: the main bus and the I/O bus. Most CPUs use the
 * main bus for everything, but the Z80 distinguishes the two.
 */
public enum BusType {
	MAIN,  // The "main" bus 
	PORT   // The "I/O" bus (used by the Z80)
}