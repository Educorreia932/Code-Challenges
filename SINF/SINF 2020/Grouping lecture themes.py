N = int(input())

pairs = []

for i in range(0, 2 * N, 2):
    s1 = input()
    s2 = input()

    pairs.append([s1, s2])

result = []

L = pairs

import itertools, functools

def partition(pred, iterable):
    t1, t2 = itertools.tee(iterable)
    return itertools.filterfalse(pred, t1), filter(pred, t2)

groups = []
for a, b in L:
    unrelated, related = partition(lambda group: any(aa == a or bb == b or aa == b or bb == a for aa, bb in group), groups)
    groups = [*unrelated, sum(related, [(a, b)])]

r = len(groups)


print(r)

