def rabbit_pairs(n, k):
    if n < 2:
        return n

    return rabbit_pairs(n - 1, k) + k * rabbit_pairs(n - 2, k)
