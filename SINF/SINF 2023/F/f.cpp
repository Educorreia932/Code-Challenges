#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

typedef vector<pair<ll, ll>> vii;
typedef tuple<ll, ll, ll, ll, ll> tl;
typedef vector<tuple<ll, ll, ll, ll, ll>> v5i;  // time, x1, x2, id1, id2
ll L, d;
vii v;
int main() {  
    cin >> L >> d;
    v.resize(d);
    for (int i = 0; i < d; i++) {
        ll x, direction;
        cin >> x >> direction;
        if (direction == 0) direction = -1;
        v[i] = make_pair(x, direction);
    }
    sort(v.begin(), v.end());
    v5i collisions;
    for (ll i = 1; i < d; i++) {
        if (v[i].second == -1) {
            if (v[i-1].second == 1) {
                collisions.emplace_back((v[i].first - v[i-1].first) / 2, v[i-1].first, v[i].first, i - 1, i);
                // cout << v[i].first - v[i-1].first / 2 << " " << v[i].first << " " << v[i-1].first << endl;
            }
        }
    }
    ll time = 0;
    sort(collisions.rbegin(), collisions.rend());
    while (!collisions.empty()) {
        vector<int> vec;
        auto &[distance, x1, x2, id1, id2] = collisions.back();
        // cout << id1 << " " << id2 << " " << x1 << " " << x2 << " " << distance << endl;
        time += distance + 1;
        collisions.erase(--collisions.end());
        v[id1] = make_pair(v[id1].first + distance * v[id1].second, -v[id1].second);
        v[id2] = make_pair(v[id2].first + distance * v[id2].second, -v[id2].second);
        vec.push_back(id1);
        vec.push_back(id2);
        for (ll i = collisions.size() - 1; i >= 0; i--) {
            auto &[other_d, other_x1, other_x2, other_id1, other_id2] = collisions[i];
            if (other_d == distance) {
                v[other_id1] = make_pair(v[other_id1].first + distance * v[other_id1].second, -v[other_id1].second);
                v[other_id2] = make_pair(v[other_id2].first + distance * v[other_id2].second, -v[other_id2].second);
                collisions.erase(--collisions.end());
                vec.push_back(other_id1);
                vec.push_back(other_id2);
            }
            else {
                other_d -= distance;
                other_x1 += distance;
                other_x2 -= distance;
                v[other_id1] = make_pair(v[other_id1].first + distance * v[other_id1].second, v[other_id1].second);
                v[other_id2] = make_pair(v[other_id2].first + distance * v[other_id2].second, v[other_id2].second);
                collisions[i] = tl(other_d, other_x1, other_x2, other_id1, other_id2);
            }
        }
        for (ll i = 0; i < (ll)vec.size(); i++) {
            ll id = vec[i];
            ll direction = v[id].second;
            if (direction == -1) {
                if (v[id - 1].second == 1) {
                    collisions.emplace_back(v[id].first - v[id-1].first / 2, v[id-1].first, v[id].first, id - 1, id);
                }
            }
            if (direction == 1) {
                if (v[id + 1].second == -1 && find(vec.begin(), vec.end(), id + 1) == vec.end()) {
                    collisions.emplace_back(v[id + 1].first - v[id].first / 2, v[id].first, v[id + 1].first, id, id + 1);
                }
            }
        }
        sort(collisions.rbegin(), collisions.rend());
    }
    ll max_value = 0;
    for (ll i = 0; i < d; i++) {
        ll distance = v[i].second == 1 ? L - v[i].first : v[i].first;
        max_value = max(max_value, distance);
    }
    cout << time + max_value << endl;
    // determine when they fall
    return 0;
}
