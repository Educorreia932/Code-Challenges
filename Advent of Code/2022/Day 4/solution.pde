int[] assignments;
int SCALE = 10;
int MARGIN = 10;

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

void draw() {
	var j = MARGIN;
	color c1 = #b80f0f;
	color c2 = #FF002B;  

	background(255);

	for (int i = 0; i < assignments.length; i++) {
		var x0 = assignments[i++] * SCALE + MARGIN;
		var y0 = assignments[i++] * SCALE + MARGIN;
		var x1 = assignments[i++] * SCALE + MARGIN;
		var y1 = assignments[i] * SCALE + MARGIN;

		stroke(c1);
		line(x0, j, y0, j);
		circle(x0, j, 3);
		circle(y0, j, 3);

		stroke(c2);
		line(x1, j, y1, j);
		circle(x1, j, 3);
		circle(y1, j, 3);

		j += SCALE;
  	}

	save("output.png");
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

public void settings() {
	size(1000 + MARGIN * 2, (1000 * SCALE) + MARGIN * 2);
}

void setup() {
	noLoop();
	strokeWeight(3);
	
	assignments = readInput(); 

	println(partOne(assignments));
	println(partTwo(assignments));
}
