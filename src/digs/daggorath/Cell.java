package digs.daggorath;

public class Cell {
	
	int x;
	int y;		
	
	static Cell getRandomCell() {
		int a = Random.getNextRandom();
		int b = Random.getNextRandom();
		return new Cell(a&0x1F, b&0x1F);
	}
	
	Cell(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	Cell(Cell other) {
		this.x = other.x;
		this.y = other.y;
	}
	
	boolean isValid() {
		if(x<0 || x>31 || x<0 || x>31) return false;
		return true;
	}
	
	void stepInDirection(int dir) {
		switch(dir) {
		case 0:
			y = y - 1;
			break;
		case 1:
			x = x + 1;
			break;
		case 2:
			y = y + 1;
			break;
		case 3:
			x = x - 1;
		}
	}

}
