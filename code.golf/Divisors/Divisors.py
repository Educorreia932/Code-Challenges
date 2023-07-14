for x in range(1, 101):
    print(*[j for j in range(1, x + 1) if x % j < 1])
