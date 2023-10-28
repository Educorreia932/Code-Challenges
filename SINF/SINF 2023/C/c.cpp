#include <bits/stdc++.h>

using namespace std;
typedef vector<int> vi;

int main() {
    cin.tie(NULL); ios::sync_with_stdio(false);
    stack<int> s;
    vi m;
    int n;
    cin >> n;
    m.assign(n, 0);
    for (int i = 0; i < n; i++) {
        cin >> m[i];
    }
    int max_dist = 0;
    int current = m[0];
    for (int i = 1; i < n; i++) {
        if (m[i] >= current) {
            int min_h = INT_MAX;
            // cout << "value " << current << ", index " << i << endl;
            while (!s.empty()) {
                int v = s.top(); s.pop();
                min_h = min(min_h, v);
            }
            max_dist = max(current - min_h, max_dist);
            // cout << min_h << " " << max_dist << endl;
            current = m[i];
        }
        else {
            s.push(m[i]);
        }
    }
    current = m[n - 1];
    for (int i = n - 2; i >= 0; i--) {
        if (m[i] >= current) {
            int min_h = INT_MAX;
            // cout << "value " << current << ", index " << i << endl;
            while (!s.empty()) {
                int v = s.top(); s.pop();
                min_h = min(min_h, v);
            }
            max_dist = max(current - min_h, max_dist);
            // cout << min_h << " " << max_dist << endl;
            current = m[i];
        }
        else {
            s.push(m[i]);
        }
    }
    cout << max_dist << endl;
    return 0;

}
