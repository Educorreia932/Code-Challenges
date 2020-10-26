C, N, P, W = (int(x) for x in input().split(" "))

if W < C:
    print(0)

else:
    pockets = [W // N] * N

    for i in range(W % N):
        pockets[i] += 1

    for i in range(N - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            n = C - pockets[i] # Number of necessary extra pieces of wood to craft a table

            if n > 0:
                pockets[i] += n
                pockets[j] -= n

            # If we have the necessary number of pieces of wood to craft a table, do it
            if pockets[i] == C: 
                pockets[i] = "T"
                break

    print(pockets.count("T"))
