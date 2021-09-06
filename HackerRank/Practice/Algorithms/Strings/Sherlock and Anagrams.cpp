#include <bits/stdc++.h>

using namespace std;

int sherlockAndAnagrams(string s) {
    map<string, int> substrings;
    int count = 0;

    for (int i = 0; i < s.size(); i++) 
        for (int j = 1; j < min(s.size() - i + 1, s.size()); j++) {
            string substring = s.substr(i, j);

            sort(substring.begin(), substring.end());
            
            if (substrings.find(substring) != substrings.end())
                count += substrings[substring]++;

            else
                substrings[substring] = 1;
        }

    return count;
}
