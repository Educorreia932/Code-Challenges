#include<bits/stdc++.h>

using namespace std;

class Box {
    private:
        int l, b, h;
        
    public:
        Box();
        Box(int length, int breadth, int height);
        int getLength();
        int getBreadth();
        int getHeight();
        long long CalculateVolume();

        bool operator<(Box& b);
        friend ostream& operator<<(ostream& out, Box& B);
};

Box::Box() {
    l = b = h = 0;
}

Box::Box(int length, int breadth, int height) {
    l = length;
    b = breadth;
    h = height;
}

int Box::getLength() {
    return l;
}

int Box::getBreadth() {
    return b;
}

int Box::getHeight() {
    return h;
}

long long Box::CalculateVolume() {
    return l * b * h;
}

bool Box::operator<(Box& b) {
    if (l == b.l && this->b == b.b)
        return h < b.h;

    else if (l == b.l)
        return this->b < b.b;

    return l < b.l;
}

ostream& operator<<(ostream& out, Box& B) {
    out << B.l << " " << B.b << " " << B.h;

    return out;
}
