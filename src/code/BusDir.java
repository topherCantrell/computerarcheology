package code;

/**
 * A single opcode usually reads (like LDA) or writes (like STA) to an address. Sometimes
 * (like INC) it does both. Some I/O devices behave one way (one descriptive name) if
 * you read them and another way (another descriptive name) if you write to them.
 */
public enum BusDir {
	READ,  // Operation is a read
	WRITE, // Operation is a write
	BOTH   // Operation is both
}