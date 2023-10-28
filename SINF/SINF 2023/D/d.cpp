#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;
ull n;
vector<int> v;
ull number(ull i, ull currWeight, ull remainderWeight) {
    if (currWeight + remainderWeight < 200) return 0;
    if (i >= n) {
        if (currWeight >= 200) return currWeight;
        return 0;
    }
    ull res = 0;
    if (currWeight >= 200) {
        res = currWeight * (ull) pow(2, n-i);
        ull sum = 0;
        for (ull j = i; j < n; j++) {
            sum += v[j];
        }
        return res + sum * (ull) pow(2, n - i - 1);
    }
    res += number(i+1, currWeight + v[i], remainderWeight - v[i]);
    res += number(i + 1, currWeight, remainderWeight - v[i]);
    return res;
}

int main() {
    cin.tie(NULL); ios::sync_with_stdio(false);
    
    cin >> n;
    v.assign(n, 0);
    ull res = 0;
    ull completeWeight = 0;
    for (ull i = 0; i < n; i++) {
        cin >> v[i];
        completeWeight += v[i];
    }
    res = number(0, 0, completeWeight);
    cout << res << endl;
    return 0;
}
