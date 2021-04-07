# Circular primes

from math import sqrt
from itertools import permutations


def is_prime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False

    return True


def digit_rotations(n):
    rotations = set()

    for i in range(len(str(n))):
        m = int(str(n)[i:] + str(n)[:i])
        rotations.add(m)

    return rotations


def is_circular_prime(n):
    if not is_prime(n) or "2" in str(n) or "4" in str(n) or "6" in str(n) or "8" in str(n) or "5" in str(n) or "0" in str(n):
        return False

    return False not in [is_prime(x) for x in digit_rotations(n)]


solution = 2

for i in range(2, 1000001):
    if is_circular_prime(i):
        solution += 1

print(solution)
