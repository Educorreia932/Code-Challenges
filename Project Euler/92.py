# Square digit chains

chains = {
    1: 1,
    89: 89
}

sum_digits_squared = lambda n: sum(int(i) ** 2 for i in str(n))

for i in range(1, 10000000):
    chain = [i]

    while i not in chains:
        i = sum_digits_squared(i)
        chain.append(i)

    for n in chain:
        chains[n] = chains[i]

answer = tuple(chains.values()).count(89)

print(answer)
