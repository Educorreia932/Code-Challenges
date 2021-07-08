def solution(n):
    G = [0 for i in range(n + 1)]
    G[0] = 1

    for k in range(1, n):
        G = [G[i] if i - k < 0 else G[i] + G[i - k] for i in range(n + 1)]

    return G[n]
