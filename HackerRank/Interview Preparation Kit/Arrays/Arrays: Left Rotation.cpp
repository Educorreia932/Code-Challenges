#include <bits/stdc++.h>

using namespace std;

vector<int> rotLeft(vector<int> a, int d) {
    vector<int> result(a.size());

    for (int i = d; i < a.size(); i++)
        result[i - d] = a[i];

    for (int i = d; i > 0; i--) 
        result[a.size() - i] = a[d - i];

    return result; 
}
