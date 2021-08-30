#include <bits/stdc++.h>

using namespace std;

int countingValleys(int steps, string path) {
    int level = 0, result = 0;
    bool in_valey = false;

    for (char step : path) {
        if (step == 'U')
            level += 1;

        else
            level -= 1;

        if (level >= 0 && in_valey) {
            result += 1;
            in_valey = false;
        }

        else if (level < 0 && !in_valey)
            in_valey = true;
    }

    return result;
}
