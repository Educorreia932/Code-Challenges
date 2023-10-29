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


def area(points, cut):
    A = -points[cut[-1], 0] * points[cut[0], 1] + points[cut[-1], 1] * points[cut[0], 0]
    for i in range(len(cut) - 1):
        A += (
            -points[cut[i], 0] * points[cut[i + 1], 1]
            + points[cut[i], 1] * points[cut[i + 1], 0]
        )
    return A


N = get_number()
M = get_number()

points = np.zeros((N, 2))
vertices = list(range(N))
cuts = []

for i in range(N):
    points[i, 0] = get_number()
    points[i, 1] = get_number()

cuts.append(list(range(N)))
for i in range(M):
    d1 = get_number() - 1
    d2 = get_number() - 1
    # vertices = cuts.pop()
    for idx, cut in enumerate(cuts):
        if (d1 in cut) and (d2 in cut):
            vertices = cuts.pop(idx)

    cut1 = vertices[d1 : d2 + 1]
    cut2 = vertices[d2:] + vertices[: d1 + 1]
    cuts.append(cut2)
    cuts.append(cut1)

A = 0
B = 0

for idx, cut in enumerate(cuts):
    if idx % 2:
        A += area(points, cut)

    else:
        B += area(points, cut)
        
print(int(max(A, B)))
