#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int N;

    scanf("%d", &N);

    int* A = (int*) malloc(N * sizeof(int));

    for (int i = 0; i < N; i++)
        scanf("%d ", &A[i]);

    for (int i = N - 1; i >= 0; i--)
        printf("%d ", A[i]);

    return 0;
}