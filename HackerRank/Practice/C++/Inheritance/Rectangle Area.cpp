#include <iostream>

using namespace std;

class Rectangle {
    protected:
        int width, height;

    public:
        Rectangle(int width, int height) {
            this->width = width;
            this->height = height;
        }

        void display() {
            cout << width << " " << height << endl;
        }
};

class RectangleArea : public Rectangle {
    public:
        RectangleArea() : Rectangle(0, 0) {
            
        }

        void read_input() {
            cin >> width >> height; 
        }

        void display() {
            cout << width * height << endl;
        }
};
