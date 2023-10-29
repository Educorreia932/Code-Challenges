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

n = get_number()
m = get_number()

elevation = np.zeros((n, m))
flow = np.zeros((n, m, 4))
liters = np.full((n, m), 1.0)
split = np.zeros((n, m))
drain_mask = np.zeros((n, m))
drain = np.zeros((n, m))
for i in range(n):
    for j in range(m):
        elevation[i, j] = get_number()

for i in range(n):
    for j in range(m):
        up = 0
        down = 0
        left = 0
        right = 0
        if i != 0:
            up = 1 if elevation[i - 1, j] < elevation[i, j] else 0
        if i != n - 1:
            down = 1 if elevation[i + 1, j] < elevation[i, j] else 0
        if j != 0:
            left = 1 if elevation[i, j - 1] < elevation[i, j] else 0
        if j != m - 1:
            right = 1 if elevation[i, j + 1] < elevation[i, j] else 0

        count = up + down + left + right
        if count == 0:
            drain_mask[i, j] = 1
        else:
            flow_rate = 1 / count
            flow[i, j, 0] = flow_rate * left
            flow[i, j, 1] = flow_rate * up
            flow[i, j, 2] = flow_rate * right
            flow[i, j, 3] = flow_rate * down

for it in range(100):
    for i in range(n):
        for j in range(m):
            if drain_mask[i, j]:
                drain[i, j] += liters[i, j]
                continue

            if i != 0:
                split[i - 1, j] += liters[i, j] * flow[i, j, 1]
            if i != n - 1:
                split[i + 1, j] += liters[i, j] * flow[i, j, 3]
            if j != 0:
                split[i, j - 1] += liters[i, j] * flow[i, j, 0]
            if j != m - 1:
                split[i, j + 1] += liters[i, j] * flow[i, j, 2]

    liters = np.array(split, copy=True)
    split = np.zeros((n, m))

print(drain.max())
