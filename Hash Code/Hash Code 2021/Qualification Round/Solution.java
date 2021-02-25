import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.stream.Stream;
import java.util.*;

public class Solution {
    private int simulationTime;
    private int numIntersections;
    private int n_streets;
    private int n_cars;
    private int carScore;

    private ArrayList<Intersection> intersections;
    private HashMap<String, Street> streets;
    private ArrayList<Car> cars;

    Solution(String filename) {
        readFile(filename);
        scheduleSemaphores();
        //run();
        printSchedule();
    }

    void scheduleSemaphores(){
        
        for(Intersection intersection : intersections){
            intersection.updateDensity();
            intersection.updateSchedule();
        }
    }

    void readFile(String filename) {
        File file = new File(filename);

        try {
            Scanner reader = new Scanner(file);

            String firstLine = reader.nextLine();
            Integer[] firstLineInfo = Stream.of(firstLine.split(" ")).map(Integer::valueOf).toArray(Integer[]::new);

            int simulationTime = firstLineInfo[0];
            numIntersections = firstLineInfo[1];
            int numStreets = firstLineInfo[2];
            int numCars = firstLineInfo[3];
            int carScore = firstLineInfo[4];

            this.intersections = new ArrayList<Intersection>();

            for (int i = 0; i < numIntersections; i++) {
                this.intersections.add(new Intersection(i));
            }

            this.streets = new HashMap<String, Street>();

            // Read intersections information
            for (int i = 0; i < numStreets; i++) {
                String line = reader.nextLine();
                String[] lineInfo = line.split(" ");
                int start = Integer.parseInt(lineInfo[0]);
                int finish = Integer.parseInt(lineInfo[1]);
                String streetName = lineInfo[2];
                int l = Integer.parseInt(lineInfo[3]);

                Street newStreet = new Street(streetName, l, this.intersections.get(start),
                        this.intersections.get(finish));

                this.intersections.get(finish).addArrivalStreet(newStreet);
                this.intersections.get(start).addDepartureStreet(newStreet);

                this.streets.put(streetName, newStreet);
            }

            for (int i = 0; i < numCars; i++) {
                String line = reader.nextLine();
                String[] lineInfo = line.split(" ");
                int n = Integer.parseInt(lineInfo[0]);
                Car car = new Car();
                for (int j = 1; j <= n; j++) {
                    car.addStreet(this.streets.get(lineInfo[j]));
                    this.streets.get(lineInfo[j]).increaseDensity();
                }
            }

            reader.close();
        }

        catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    public List<Street> sortStreets() {
        Comparator<Street> byDensity = new Comparator<>() {
            public int compare (Street s1, Street s2) {
                return Integer.compare(s1.getL()/s1.getDensity(), s2.getL()/s2.getDensity());
            }
        };

        List<Street> sortedStreets = new ArrayList<>(streets.values());
        Collections.sort(sortedStreets, byDensity);
        // System.out.println(Arrays.toString(sortedStreets.toArray()));
        return sortedStreets;
    }

    // Run the simulation and calculate final score
    void run() {

        for (int i = 0; i < simulationTime; i++) {

        }

    }
    
    void printSchedule() {
        // Number traffic light schedules
        System.out.println(numIntersections);

        // Traffic light schedules
        for(Intersection intersection : intersections) {
            System.out.println(intersection.getId());
            System.out.println(intersection.getNumberIncomingStreets());

            for(Street street : intersection.getSchedule().keySet()){
                if (intersection.getSchedule().get(street) > 0)
                    System.out.println(street.getName() + " " + intersection.getSchedule().get(street));
                else{
                    System.out.println(street.getName() + " 1");
                }   
            }
        }
    }
}