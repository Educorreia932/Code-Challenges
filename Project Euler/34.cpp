// Digit factorials

#include <iostream>

using namespace std;

int factorials[10];

int factorial(int n) {
    int result = 1;

    for(int i = n; i > 1; i--)
        result *= i;

    return result;
}

int factorial_sum(int n) {
    if (n > 0)
        return factorials[n % 10] + factorial_sum(n / 10);
    
    return 0;
}

int main() {
    int answer = 0;
    int n = factorial(9) * 7; // Highest number that can be written as the sum of factorials of its digits

    for (int i = 0; i < 10; i++)
        factorials[i] = factorial(i);

    for (int i = 3; i < n; i++) 
        if (i == factorial_sum(i)) 
            answer += i;

    cout << answer << endl;

    return 0;
}