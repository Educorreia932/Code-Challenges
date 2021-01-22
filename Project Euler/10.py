# Summation of primes

from math import sqrt

is_prime = lambda n: [i for i in range(2, int(sqrt(n) + 1)) if n % i == 0] == []

n = 1000

answer = sum(i for i in range(2, n) if is_prime(i))

print(answer)
