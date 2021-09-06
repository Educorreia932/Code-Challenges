#include <bits/stdc++.h>

using namespace std;

string twoStrings(string s1, string s2) {
    set<char> s1_characters, s2_characters; 

    for (char c : s1) 
        s1_characters.insert(c);

    for (char c : s2) 
        s2_characters.insert(c);

    for (char c : s1_characters) 
        if (s2_characters.find(c) != s2_characters.end())
            return "YES";

    return "NO";
}
