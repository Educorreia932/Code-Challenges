#include <bits/stdc++.h>

using namespace std;

long arrayManipulation(int n, vector<vector<int>> queries) {
    long* array = (long*) calloc(n, sizeof(long));
    long max = 0, sum = 0;

    for (vector<int> query : queries) {
        array[query[0] - 1] += query[2];

        if (query[1] < n)
            array[query[1]] -= query[2];
    }

    for (int i = 0; i < n; i++) {
        sum += array[i];

        if (sum > max)
            max = sum;
    }

    return max;
}
