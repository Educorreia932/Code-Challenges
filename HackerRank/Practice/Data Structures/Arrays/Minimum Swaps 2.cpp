#include <bits/stdc++.h>

using namespace std;

int minimumSwaps(vector<int> arr) {
    int swaps = 0;

    for (int i = 0; i < arr.size(); i++) {
        while (arr[i] != i + 1) {
            int temp = arr[arr[i] - 1];
  
            arr[arr[i] - 1] = arr[i];
            arr[i] = temp;
  
            swaps += 1;
        }
    }

    return swaps;
}
