#include <bits/stdc++.h>

using namespace std;

int sockMerchant(int n, vector<int> ar) {
    int result = 0;
    map<int, int> socks;

    for (int sock : ar)
        if (socks.count(sock) == 0)
            socks[sock] = 1;

        else
            socks[sock] += 1;

    for (auto sock : socks)
        result += sock.second / 2;

    return result;
}
