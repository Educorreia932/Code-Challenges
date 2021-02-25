import java.util.ArrayList;
import java.util.HashMap;

public class Intersection {
    private int id;
    private ArrayList<Street> departureStreets;
    private HashMap<Street, Integer> schedules; // <arrivalStreet, semaphoreTime>
    int density = 0;

    Intersection(int id) {
        this.id = id;
        this.schedules = new HashMap<Street, Integer>();
        this.departureStreets = new ArrayList<Street>();
    }

    void addArrivalStreet(Street street){
        this.schedules.put(street, 1);
        
    }  

    void addDepartureStreet(Street street){
        this.departureStreets.add(street);
    }

    public int getId(){
        return id;
    }

    int getNumberIncomingStreets(){
        return schedules.size();
    }

    int getNumberScheduledStreets() {
        int result = 0;
        
        for(Street street : schedules.keySet()){
            result += schedules.get(street) > 0 ? 1 : 0;
        }

        return result;
    }

    HashMap<Street, Integer> getSchedule(){
        return schedules;
    }

    void updateDensity(){
        for(Street street : schedules.keySet()){
            this.density += street.getDensity();
        }
    }

    void updateSchedule(){
        for(Street street : schedules.keySet()){
            schedules.put(street, street.getDensity() / street.getL());
        }
    }

}
