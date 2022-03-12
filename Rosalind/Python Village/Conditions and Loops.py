def odd_sum(a, b):
    return sum((x for x in range(a, b + 1) if x % 2 != 0))
