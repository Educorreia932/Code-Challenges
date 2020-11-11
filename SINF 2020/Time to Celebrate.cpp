#include <algorithm>
#include <iostream>
#include <string>
#include <sstream> 
#include <vector>

using namespace std;

vector<vector<int>> S;
int result = 0;

void chooseSeat(vector<int> seatsTaken, int index) {
    if (index == seatsTaken.size()) {
        result++;

        return;
    }

    for (int seat : S[index]) {
        if (find(seatsTaken.begin(), seatsTaken.end(), seat) != seatsTaken.end()) {
            seatsTaken.push_back(seat);

            chooseSeat(seatsTaken, index + 1);

            seatsTaken.pop_back();
        }
    }
}

int main() {
    int N;

    cin >> N;

    for (int i = 0; i <= N; i++) {
        string line;
        getline(cin, line);

        stringstream line_stream(line);

        vector<int> seats;

        while (!line_stream.eof()) {
            int n;
            line_stream >> n;

            seats.push_back(n);
        }

        S.push_back(seats);
    }

    sort(S.begin(), S.end());

    chooseSeat(vector<int>(), 0);

    cout << result;

    return 0;
}