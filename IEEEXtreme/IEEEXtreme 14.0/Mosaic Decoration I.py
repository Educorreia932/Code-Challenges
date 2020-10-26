from math import ceil

black_tiles = 0
pink_tiles = 0

N, C_b, C_p, = (int(x) for x in input().split(" "))

for i in range(N):
    B_i, P_i = (int(x) for x in input().split(" "))

    black_tiles += B_i
    pink_tiles += P_i

black_piles = ceil(black_tiles / 10)
pink_piles = ceil(pink_tiles / 10)

print(black_piles * C_b + pink_piles * C_p)
