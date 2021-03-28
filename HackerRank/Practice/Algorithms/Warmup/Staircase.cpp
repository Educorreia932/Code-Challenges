#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

void staircase(int n) {
    string stairs;

    for (int i = 0; i < n; i++) {
        stairs += "#";

        cout << setw(n) << stairs << endl;
    }
}

int main() {
    int n;
    
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    staircase(n);

    return 0;
}
