import math

f = open("Day 3 - Input.txt", "r")

grid = f.read().split("\n")

def part_1():
    i = 0
    result = 0
    length = len(grid[0])

    for line in grid:
        if line[i] == "#":
            result += 1

        i = (i + 3) % length

    print(result)

def part_2():
    slopes = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    )

    result = []
    length = len(grid[0])

    for slope in slopes:
        j = 0
        trees = 0

        for i in range(0, len(grid), slope[1]):
            if grid[i][j] == "#":
                trees += 1

            j = (j + slope[0]) % length

        result.append(trees)

    result = math.prod(result)

    print(result)

part_1()
part_2()
