#include <bits/stdc++.h>

using namespace std;

int hourglassSum(vector<vector<int>> arr) {
    int max_sum = INT_MIN;

    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++) {
            int sum = arr[i + 1][j + 1];

            for (int k = 0; k < 3; k++) {
                sum += arr[i][j + k];
                sum += arr[i + 2][j + k];
            }

            if (sum > max_sum)
                max_sum = sum;
        }

    return max_sum;
}
