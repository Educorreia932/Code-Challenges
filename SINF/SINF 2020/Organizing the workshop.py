def powerset(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item

K = int(input())
M = int(input())
N = int(input())

C = []

for i in range(N):
    C.append(int(input()))

result = 0

for item in powerset(C):
    if len(item) < M:
        continue

    if sum(item) == K:
        result += 1

print(result)
