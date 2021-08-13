# Pandigital prime

from itertools import permutations
from math import sqrt

is_prime = lambda n: [i for i in range(2, int(sqrt(n) + 1)) if n % i == 0] == []

def pandigital_numbers():
    numbers = []
    p = []

    n = 0

    for j in range(1, 10):
        n = n * 10 + j
        
        numbers.append(n)

    for number in numbers:
        p += [int("".join(n)) for n in permutations(str(number))]

    return p

pandigital_primes = []

for number in pandigital_numbers():
    if is_prime(number):
        pandigital_primes.append(number)

answer = max(pandigital_primes)

print(answer)
