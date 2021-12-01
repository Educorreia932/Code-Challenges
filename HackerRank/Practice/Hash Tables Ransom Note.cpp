#include <bits/stdc++.h>

using namespace std;

void checkMagazine(vector<string> magazine, vector<string> note) {
    map<string, int> words;

    for (string word : magazine) 
        if (words.count(word) == 0)
            words[word] = 1;

        else
            words[word]++; 

    for (string word : note)
        if (words.count(word) == 0 || words[word] <= 0) {
            cout << "No";

            return;
        }

        else
            words[word]--;

    cout << "Yes";
}
