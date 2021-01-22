# 10001st prime

from math import sqrt

is_prime = lambda n: [i for i in range(2, int(sqrt(n) + 1)) if n % i == 0] == []

counter = 1
index = 1
result = 0

while index <= 10002:
    if is_prime(counter):
        result = counter
        index += 1

    counter += 1

print(result)
