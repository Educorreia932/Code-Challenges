f = open("input/rosalind_fib.txt", "r")

n, k = [int(x) for x in f.read().split()]

def rabbit_pairs(n, k):
    if n < 2:
        return n

    return rabbit_pairs(n - 1, k) + k * rabbit_pairs(n - 2, k)

print(rabbit_pairs(n, k))
