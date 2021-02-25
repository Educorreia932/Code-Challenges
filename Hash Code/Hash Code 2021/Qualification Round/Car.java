import java.util.ArrayList;

public class Car {
    private ArrayList<Street> path;

    Car(){
        this.path = new ArrayList<Street>();
    }

    void addStreet(Street street){
        this.path.add(street);
    }
}