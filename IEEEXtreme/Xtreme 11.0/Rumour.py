from math import ceil, log, pow, floor
import numpy as np

# Number of queries
q = int(input())

for i in range(q):
    i1, i2 = (int(x) for x in input().split(" "))

    n1 = {i1}
    n2 = {i2}

    d1 = {i1: 0}
    d2 = {i2: 0}

    counter = 0

    while i1 > 1 or i2 > 1:
        counter += 1

        i1 //= 2
        n1.add(i1)
        d1[i1] = counter

        i2 //= 2
        n2.add(i2)
        d2[i2] = counter

    common_elements = n1 & n2
    maximum = max(common_elements)

    distance = d1[maximum] + d2[maximum]

    print(distance)
    