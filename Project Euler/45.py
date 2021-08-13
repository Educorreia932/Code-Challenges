# Triangular, pentagonal, and hexagonal

from math import sqrt

def triangle_number(i):
    return (i * (i + 1)) / 2

def is_pentagonal(n):
    i = 1

    while True:
        m = (3 * i * i - i) / 2
        i += 1

        if m >= n:
            break

    return m == n

def is_hexagonal(n):
    val = 8 * n + 1
    x = 1 + sqrt(val)

    m = x / 4

    return (m - int(m)) == 0


i = 286
answer = 0

while True:
    n = triangle_number(i)

    if is_pentagonal(n) and is_hexagonal(n):
        answer = n

        break

    i += 1

print(answer)
