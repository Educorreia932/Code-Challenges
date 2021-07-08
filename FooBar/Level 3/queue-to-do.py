def consecutive_xor(m, n):
    if m % 2 == 0:
        return [n, 1, n ^ 1, 0][(n - m) % 4]

    else:
        return [m, m ^ n, m - 1, (m - 1) ^ n][(n - m) % 4]


def solution(start, length):
    result = start ^ start

    for i in range(1, length + 1):
        end = start + length - i
        result ^= consecutive_xor(start, end)
        
        start += length

    return result
