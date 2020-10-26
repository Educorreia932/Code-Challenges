from math import ceil

W, H, A, B, M, C = (int(x) for x in input().split(" "))

i = W / A
j = H / B

tiles_cost = int(ceil(i * j / 10) * M)
cuts_cost = 0

if W % A != 0:
    cuts_cost += H * C

if H % B != 0:
    cuts_cost += W * C

print(tiles_cost + cuts_cost)