int partOne(int[] assignments) {
  	int result = 0;
  
	for (int i = 0; i < assignments.length; i++) {
		var x0 = assignments[i++];
		var y0 = assignments[i++];
		var x1 = assignments[i++];
		var y1 = assignments[i];
		
		if ((x0 >= x1 && y0 <= y1) || (x1 >= x0 && y1 <= y0))
			result++;
	}
  
	return result;
}

int partTwo(int[] assignments) {
	int result = 0;
  
	for (int i = 0; i < assignments.length; i++) {
		var x0 = assignments[i++];
		var y0 = assignments[i++];
		var x1 = assignments[i++];
		var y1 = assignments[i];
	
	if (x0 <= y1 && x1 <= y0)
	  	result++;
  	}
  
  	return result;
}

int[] readInput() {
  	var lines = loadStrings("input.txt");
  	int[] assignments = {};
  
  	for (String line : lines) {
		var pairs = int(splitTokens(line, ",-"));
	
		assignments = concat(assignments, pairs);
  	}
  
  	return assignments;
}

void setup() {
	var assignments = readInput(); 

	println(partOne(assignments));
	println(partTwo(assignments));
}
