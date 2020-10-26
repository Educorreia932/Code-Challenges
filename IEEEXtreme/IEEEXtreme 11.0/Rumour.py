import math

def nearest_power(n):
    return int(math.log(n, 2)) + 1

# Number of queries
q = int(input())

for i in range(q):
    i1, i2 = (int(x) for x in input().split(" "))

    distance = 0

    p1 = nearest_power(i1)
    p2 = nearest_power(i2)

    # i1 must be the lowest in the binary tree
    if p1 < p2:
        p1, p2 = p2, p1
        i1, i2 = i2, i1

    # Put the two elements at the same level
    while p1 > p2:
        i1 //= 2
        p1 -= 1
        distance += 1

    distance += i2 + i1 / 2


    print(distance)
        