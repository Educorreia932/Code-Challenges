#include <sstream>
#include <vector>
#include <iostream>

using namespace std;

vector<int> parseInts(string str) {
    vector<int> ints;
    stringstream ss(str);

    int i;
    char c;
    string temp;

    while(getline(ss, temp, ',')) {
        if (stringstream(temp) >> i) 
            ints.push_back(i);
    }

    return ints;
}

int main() {
    string str;

    cin >> str;

    vector<int> integers = parseInts(str);

    for(int i = 0; i < integers.size(); i++) 
        cout << integers[i] << "\n";
    
    return 0;
}   