# Lexicographic permutations

from itertools import permutations

p = tuple(permutations(range(0, 10)))
answer = int("".join(map(str, p[1000000 - 1])))

print(answer)
