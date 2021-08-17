// Non-abundant sums

#include <iostream>
#include <vector>

#define N 20161

using namespace std;

int divisors_sum(int n) {
    int sum = 0;

    for (int i = 1; i < n; i++)
        if (n % i == 0)
            sum += i;

    return sum;
}

int main() {
    int answer = 0;
    vector<int> abundant_numbers;
    vector<bool> can_be_written_as_abundant_sum(N + 1);

    // Find abundant numbers
    for (int i = 12; i <= N; i++) 
        if (divisors_sum(i) > i)
            abundant_numbers.push_back(i);

    for (int n1 : abundant_numbers)
        for (int n2 : abundant_numbers) {
            if (n1 + n2 <= N)
                can_be_written_as_abundant_sum[n1 + n2] = true;

            else
                break;
        }

    for (int i = 0; i < can_be_written_as_abundant_sum.size(); i++)
        if (!can_be_written_as_abundant_sum[i])
            answer += i;

    cout << answer << endl;

    return 0;
}
