# Amicable numbers

from math import isqrt

def d(n):
    result = 1

    for i in range(2, isqrt(n)):
        if (k := n / i).is_integer():
            result += k + i

    return int(result)

amicable_numbers = set()

for a in range(1, 10000):
    b = d(a)

    if a != b and d(b) == a and b < 10000:
        amicable_numbers.add(a)
        amicable_numbers.add(b)

answer = sum(amicable_numbers)

print(answer)

