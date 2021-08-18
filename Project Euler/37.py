# Truncatable primes

from math import sqrt

is_prime = lambda n: n != 1 and [i for i in range(2, int(sqrt(n) + 1)) if n % i == 0] == []

i = 11
count = 0
answer = 0

while count < 11:
    l = len(str(i))

    for j in range(l):
        left_truncated = int(str(i)[j:])
        right_truncated = int(str(i)[:(l - j)])

        if not is_prime(left_truncated) or not is_prime(right_truncated):
            break   

    else:
        answer += i
        count += 1

    i += 1

print(answer)
