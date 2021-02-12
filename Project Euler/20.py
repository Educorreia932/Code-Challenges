# Factorial digit sum

from math import factorial

n = factorial(100)

solution = sum(int(x) for x in str(n))

print(solution)