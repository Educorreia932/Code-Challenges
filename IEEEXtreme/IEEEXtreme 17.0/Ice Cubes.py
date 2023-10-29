# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(" "))
        for number in data:
            if len(number) > 0:
                yield (number)


input_parser = parser()


def get_word():
    global input_parser
    return next(input_parser)


def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


# numpy and scipy are available for use
import numpy as np
import scipy

T = get_number()

for t in range(T):
    N = get_number()
    M = get_number()
    K = get_number()
    B = get_number()

    grid = np.zeros((N, M))
    grid_path_sum = np.zeros((N, M))

    for i in range(N):
        for j in range(M):
            grid[i, j] = get_number()

    grid_path_sum[0, 0] = grid[0, 0]

    k_acc = K
    for i in range(1, N):
        grid_path_sum[i, 0] = 0 if k_acc == 0 else grid_path_sum[i - 1, 0] + grid[i, 0]
        k_acc = k_acc - 1 if grid[i, 0] < B else K

    k_acc = K
    for j in range(1, M):
        grid_path_sum[0, j] = 0 if k_acc == 0 else grid_path_sum[0, j - 1] + grid[0, j]
        k_acc = k_acc - 1 if grid[0, j] < B else K

    for i in range(1, N):
        for j in range(1, M):
            grid_path_sum[i, j] += (
                max(grid_path_sum[i - 1, j], grid_path_sum[i, j - 1]) + grid[i, j]
            )

    y = N - 1
    x = M - 1
    k_acc = 1
    backtracking = True
    path = []
    while backtracking:
        if x == 0 or y == 0:
            ans = int(grid_path_sum[N - 1, M - 1])
            break
        else:
            if grid_path_sum[x - 1, y] == 0 and grid_path_sum[x, y - 1] == 0:
                grid_path_sum[x, y] = 0
                if len(path) == 0:
                    ans = "IMPOSSIBLE"
                else:
                    step = path.pop()
                    x += step[0]
                    y += step[1]
                    continue

            if grid_path_sum[x - 1, y] > grid_path_sum[x, y - 1]:
                x -= 1
                path.append((1, 0))
            else:
                y -= 1
                path.append((0, 1))

            if grid[x, y] < B:
                k_acc += 1

            if k_acc == K:
                grid_path_sum[x, y] = 0
                while len(path) != 0:
                    step = path.pop()
                    x += step[0]
                    y += step[1]
                    grid_path_sum[x, y] = grid[x, y] + max(
                        grid_path_sum[x - 1, y], grid_path_sum[x, y - 1]
                    )

    print(f"Case {t+1}: {ans}")
