#include <bits/stdc++.h>

using namespace std;

int jumpingOnClouds(vector<int> c) {
    set<int, greater<int>> Q;
    map<int, int> dist, prev;

    for (int i = 0; i < c.size(); i++) {
        dist[i] = INT_MAX;
        prev[i] = -1;

        Q.insert(i);
    }

    dist[0] = 0;

    while (!Q.empty()) {
        int u = *Q.rbegin();

        for (int q : Q)
            if (dist[q] < dist[u])
                u = q;

        Q.erase(u);

        for (int q : Q) {
            // To be able to jump onto to a cloud it must: 
            // 1. Have a difference of at most two from the current cloud
            // 2. Not be a thunderhead (clouds to be avoided)
            if ((q - u == 1 || q - u == 2) && !c[q]) {
                int alt = dist[u] + 1;

                if (alt < dist[q]) {
                    dist[q] = alt;
                    prev[q] = alt;
                }
            }

        }
    }

    return dist[c.size() - 1];
}
