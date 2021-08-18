// Digit fifth powers

#include <iostream>
#include <cmath>

using namespace std;

int fifth_power_sum(int n) {
    if (n > 0)
        return pow(n % 10, 5) + fifth_power_sum(n / 10);
    
    return 0;
}

int main() {
    int answer = 0;
    int n = pow(9, 5) * 6; // Highest number that can be written as the sum of fifth powers of its digits

    for (int i = 2; i < n; i++) 
        if (i == fifth_power_sum(i))
            answer += i;
    
    cout << answer << endl;

    return 0;
}