#include <bits/stdc++.h>

using namespace std;

long countTriplets(vector<long> arr, long r) {
    long count = 0;
    map<long, long> occurrences;
    map<pair<long, long>, long> pairs;

    for (auto it = arr.rbegin(); it != arr.rend(); it++) {
        long n = *it;
        long _n = n * r;
        long __n = _n * r;

        // 1) n is the first element of the triplet
        count += pairs[pair<long, long>{_n, __n}];

        // 2) n is the second element of the triplet
        pairs[pair<long, long>{n, _n}] += occurrences[_n];
        
        // 3) n is the third element of the triplet
        occurrences[n]++;
    }

    return count;
}
