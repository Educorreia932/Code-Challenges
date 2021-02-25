#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, q;

    scanf("%d %d", n, q);

    int** N = (int**) malloc(n * sizeof(int**));
    int k, x;

    for (int i = 0; i < n; i++) {
        scanf("%d", &k);

        N[i] = (int*) malloc(k * sizeof(int*));

        for (int j = 1; j <= k; i++) {
            scanf("%d", &x);

            N[i][j - 1] = x;
        }
    }

    for (int i = 0; i < q; i++) {
        int j, k;

        scanf("%d %d", j, k);

        printf("%d", N[j][k]);
    }

    return 0;
}