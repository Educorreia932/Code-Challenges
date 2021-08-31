#include <bits/stdc++.h>

using namespace std;

long repeatedString(string s, long n) {
    long count = 0;

    for (int i = 0; i < s.size(); i++) 
        if (s[i] == 'a')
            count += 1;

    long result = n / s.size() * count;
    
    for (int i = 0; i < n % s.size(); i++) 
        if (s[i] == 'a')
            result += 1;

    return result;
}
