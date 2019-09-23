#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main() {
    string input;
    int counter = 0;
    vector<string> tags, queries;

    cout << "Insert: ";

    while (getline(cin, input)) {
        if (!counter) {
            tags.resize(4); //Change
            queries.resize(3);
        }

        else {

        }

        counter++;
    }

    return 0;
}