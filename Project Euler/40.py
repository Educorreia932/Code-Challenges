from functools import reduce

def get_digit(n):
    s = 0
    k = 0

    while s < n:
        r = s
        s += 9 * 10 ** k * (k + 1)
        k += 1
        
    h = n - r - 1
    t = 10 ** (k - 1) + h // k
    p = h % k
    
    return int(str(t)[p])

solution = reduce(lambda a, b: a * b, [get_digit(n) for n in [10 ** i for i in range(7)]])

print(solution)
