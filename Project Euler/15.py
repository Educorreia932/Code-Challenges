# Lattice paths

from copy import deepcopy
from math import factorial

directions = (
    (0, 1),
    (1, 0),
)

# Solution 1


def sum_list(first, second):
    return [x + y for x, y in zip(first, second)]


def path(position, visited, size):
    if position[0] < 0 or position[0] > size or position[1] < 0 or position[1] > size or position in visited:
        return 0

    if position[0] == size and position[1] == size:
        return 1

    visited.append(position)

    routes = 0

    for direction in directions:
        next_position = sum_list(position, direction)

        routes += path(next_position, deepcopy(visited), size)

    return routes

# Solution 2


def central_binomial_coefficient(n):
    return int(factorial(2 * n) / (factorial(n)) ** 2)


routes = central_binomial_coefficient(20)

print(routes)
