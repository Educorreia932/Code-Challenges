# Longest Collatz sequence

import operator 

collatz = lambda n: n / 2 if n % 2 == 0 else 3 * n + 1

def chain_length(n, sequence):
    if n in sequence:
        return sequence[n]

    return 1 + chain_length(collatz(n), sequence)

sequence = {1: 1}

for i in range(1, 1000000):
    sequence[i] = chain_length(i, sequence)

answer = max(sequence.items(), key=operator.itemgetter(1))[0]

print(answer)
