from rich import print
from copy import deepcopy

def read_file():
    with open(f"{__file__.strip('.py')} - Input.txt", "r") as f:
        return [list(line) for line in f.read().split("\n")]

def adjacent_seats(seats, i, j):
    adjacent = []

    # N
    if i > 0:
        adjacent.append(seats[i - 1][j])

    # S
    if i < len(seats) - 1: 
        adjacent.append(seats[i + 1][j])

    # W
    if j > 0:
        adjacent.append(seats[i][j - 1])

    # E
    if j < len(seats[0]) - 1:
        adjacent.append(seats[i][j + 1])

    # NW
    if i > 0 and j > 0:
        adjacent.append(seats[i - 1][j - 1])

    # NE
    if i > 0 and j < len(seats[0]) - 1:
        adjacent.append(seats[i - 1][j + 1])

    # SW
    if i < len(seats) - 1 and j > 0:
        adjacent.append(seats[i + 1][j - 1])

    # SE
    if i < len(seats) - 1 and j < len(seats[0]) - 1:
        adjacent.append(seats[i + 1][j + 1])

    return adjacent.count("#")

def run(seats):
    next_round = deepcopy(seats)

    for i in range(len(seats)):
        for j in range(len(seats[i])):
            occupied = adjacent_seats(seats, i, j)

            if seats[i][j] == "L" and occupied == 0:
                next_round[i][j] = "#"

            elif seats[i][j] == "#" and occupied >= 4:
                next_round[i][j] = "L"

    return next_round

def part_1(seats):
    while True:
        next_round = run(seats)

        if seats == next_round:
            return sum(row.count("#") for row in seats)

        seats = next_round

def part_2(seats):
    pass

seats = read_file()

# print(f"Part 1: {part_1(seats)}")
print(f"Part 2: {part_2(seats)}")
