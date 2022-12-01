#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int count_bit(vector<string> values, int position) {
    int result = 0;

    for (string value : values)
        if (value[position] == '1')
            result++;

        else
            result--;

    return result;
}

int calculate_rating(vector<string> values, bool is_oxygen) {
    for (int i = 0; i < values[0].size(); i++) {
        count_bit(values, i);

        vector<string> filtered;

        char bit = count_bit(values, i) >= 0
            ? (is_oxygen ? '1' : '0') 
            : (is_oxygen ? '0' : '1');

        copy_if(values.begin(), values.end(), back_inserter(filtered), [&](string s) {
            return s[i] == bit;
        });

        values = filtered;
    }

    int rating = stoi(values[0], 0, 2);

    return rating;
}

int part_one(vector<string> input) {
    int epsilon = 0, gamma = 0;
    stringstream epsilon_number, gamma_number;

    for (int i = 0; i < input[0].size(); i++)
        if (count_bit(input, i) > 0) {
            epsilon_number << "1";
            gamma_number << "0";
        }

        else {
            epsilon_number << "0";
            gamma_number << "1";
        }

    epsilon = stoi(epsilon_number.str(), 0, 2);
    gamma = stoi(gamma_number.str(), 0, 2);;

    return epsilon * gamma;
}

int part_two(vector<string> input) {
    int oxygen = calculate_rating(input, true);
    int co2 = calculate_rating(input, false);

    return oxygen * co2;
}

int main() {
    vector<string> input;
    fstream input_file;

    input_file.open("input.txt", ios::in);

    if (input_file.is_open()) {
        string line;

        while (getline(input_file, line))
            input.push_back(line);

        input_file.close();
    }

    cout << "Part 1: " << part_one(input) << endl;
    cout << "Part 2: " << part_two(input) << endl;

    return 0;
}