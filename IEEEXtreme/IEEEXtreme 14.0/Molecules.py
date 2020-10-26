import numpy as np

T = int(input()) # Number of test cases
matrix = np.array([
    0, 1, 6,
    2, 2, 12,
    1, 2, 6,
]).reshape((3, 3))

for _ in range(T):
    C, H, O = (int(x) for x in input().split(" "))

    b = np.array([C, H, O])

    x = np.linalg.solve(matrix, b)

    print(x)
    