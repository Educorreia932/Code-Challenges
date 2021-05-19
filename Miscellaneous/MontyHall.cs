// This was a problem that I solved as part of applying to a summer internship at Semasio 

using System;
using System.Collections.Generic;
					
public class Program {
	static Random random = new Random();
	
	public static void Main() {
		int numIterations = Convert.ToInt32(Console.ReadLine()), stayingWins = 0, changingWins = 0;
		
		for (int i = 0; i < numIterations; i++) {
			List<int> doors = new List<int>() { 0, 1, 2 };
		
			int chosenDoor = doors[random.Next(doors.Count)];  // The door initially chosen by the user
			int carDoor = doors[random.Next(doors.Count)];     // The door that contains the car

			doors.Remove(chosenDoor);
			doors.Remove(carDoor);
 
			int shownDoor = doors[0];     // The door shown to the user by the host. It can't be the chosen door nor the door with the car    

			doors = new List<int>() { 0, 1, 2 };
			doors.Remove(chosenDoor);
			doors.Remove(shownDoor);

			int secondaryDoor = doors[0];  // The secondary door the user didn't initially choose. It can't be the initially chosen door nor the shown door 

			stayingWins += carDoor == chosenDoor? 1 : 0;
			changingWins += carDoor == secondaryDoor? 1 : 0;
		}
		
		Console.WriteLine("Chances of winning by staying with initial choice: " + (float) stayingWins / numIterations);
		Console.WriteLine("Chances of winning by changing initial choice: " + (float) changingWins / numIterations);
	}
}