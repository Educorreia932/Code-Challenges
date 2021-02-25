public class Street {
    private String name;
    private Intersection start_intersection;
    private Intersection final_intersection;
    private int L; 
    private int density;

    Street(String name, int L, Intersection start, Intersection finish){
        this.name = name;
        this.L = L;
        this.start_intersection = start;
        this.final_intersection = finish;
    }

    public void increaseDensity() {
        this.density++;
    }

    public int getDensity() {
        return this.density;
    }

    int getL(){
        return this.L;
    }

    public String getName(){
        return name;
    }

    @Override
    public String toString() {
        return name;
    }
}